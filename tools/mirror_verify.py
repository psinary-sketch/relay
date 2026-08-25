# -*- coding: utf-8 -*-
"""mirror_verify.py -- THE MIRROR VERIFICATION, BOTH CLAUSES, BUILT (b142).

### WHY THIS EXISTS. b130 minted the stale-build law from an export that
### verified CLEAN at 23 files and 0 mismatches while silently missing a
### conventions line the same act had just filed -- because it was built one
### commit early. ### THE MANIFEST CHECK IS INTERNALLY CONSISTENT BY
### CONSTRUCTION AND CANNOT SEE WHAT NEVER ENTERED THE STAGING DIRECTORY.
### The law's answer is two clauses, and running them as two separate ad-hoc
### commands is exactly how one of them gets skipped. They are one command here.

### CLAUSE 1 -- the archive against its own manifest: file count, row count,
###             every md5 and every byte length.
### CLAUSE 2 -- the manifest's declared source HEAD against `ls-remote`.
### ### A CLEAN CLAUSE 1 ON A STALE BUILD IS EXACTLY AS CLEAN-LOOKING AS A
### ### CORRECT ONE. Neither clause alone is the verification.

# ### DEFECT NOTE, b142, ON THIS CHECK'S FIRST RUN: the first pass assumed the
# ### manifest columns were `md5 | bytes` and matched ZERO rows out of 23 --
# ### while still printing 0 md5 mismatches and 0 byte mismatches, because zero
# ### rows produce zero failures. ### THAT IS THE WHOLE FAILURE MODE THIS FILE
# ### EXISTS TO PREVENT, and it appeared in the file's own construction. The row
# ### count is therefore VERIFIED AGAINST THE FILE COUNT and a zero-row manifest
# ### is a HARD FAILURE, never a pass.

Usage:
    python mirror_verify.py <zip> <remote-url-or-repo-path> [<branch>]
"""
import hashlib
import os
import re
import subprocess
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_emit as AE

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROW = re.compile(r'^\|\s*([^|]+?)\s*\|\s*([\d,]+)\s*\|\s*`?([0-9a-fA-F]{32})`?\s*\|', re.M)
HEAD = re.compile(r'@\s*`?([0-9a-f]{7,40})`?')


def main(zpath, remote, branch='main'):
    z = zipfile.ZipFile(zpath)
    names = [n for n in z.namelist() if n != 'MANIFEST.md']
    man = z.read('MANIFEST.md').decode('utf-8', 'replace')
    rows = ROW.findall(man)
    byname = {n.split('/')[-1]: n for n in names}

    print("=" * 78)
    print("MIRROR VERIFICATION -- BOTH CLAUSES OF THE STALE-BUILD LAW (b142)")
    print("  archive: %s" % zpath)
    print("=" * 78)

    print("\n--- CLAUSE 1: THE ARCHIVE AGAINST ITS OWN MANIFEST ---")
    print("  files in archive (excl MANIFEST) : %d" % len(names))
    print("  rows parsed from MANIFEST        : %d" % len(rows))
    if not rows:
        print("  ### HARD FAILURE: ZERO ROWS PARSED. A zero-row manifest yields zero")
        print("  ### mismatches and would read CLEAN. It is a PARSE failure, not a pass.")
        return 2
    if len(rows) != len(names):
        print("  ### HARD FAILURE: row count != file count.")
        return 2

    bad = 0
    for nm, size, md5 in rows:
        key = nm.strip('` ').split('/')[-1]
        if key not in byname:
            print("  !! MANIFEST row with no file in archive: %s" % nm)
            bad += 1
            continue
        b = z.read(byname[key])
        if hashlib.md5(b).hexdigest().lower() != md5.lower():
            print("  !! md5 mismatch  : %s" % nm)
            bad += 1
        if len(b) != int(size.replace(',', '')):
            print("  !! byte mismatch : %s  (archive %d, manifest %s)" % (nm, len(b), size))
            bad += 1
    print("  md5 / byte mismatches            : %d" % bad)
    print("  CLAUSE 1 : %s" % ("CLEAN" if bad == 0 else "NOT CLEAN"))

    print("\n--- CLAUSE 2: THE BUILD'S SOURCE HEAD AGAINST ls-remote ---")
    m = HEAD.search(man)
    if not m:
        print("  ### HARD FAILURE: the manifest declares no source HEAD to check.")
        return 2
    declared = m.group(1)
    out = subprocess.run(['git', 'ls-remote', remote, 'refs/heads/' + branch],
                         capture_output=True, text=True).stdout.strip()
    live = out.split()[0] if out else ''
    print("  manifest declares source HEAD    : %s" % declared)
    print("  ls-remote %s/%s%s: %s" % ("origin", branch, " " * max(1, 18 - len(branch)), live))
    agree = bool(live) and live.startswith(declared)
    print("  CLAUSE 2 : %s" % ("CLEAN -- they agree" if agree else "NOT CLEAN -- STALE BUILD"))

    ok = (bad == 0) and agree
    verdict = "CLEAN ON BOTH CLAUSES" if ok else "NOT CLEAN"
    if '--emit' in sys.argv:
        i = sys.argv.index('--emit')
        act = sys.argv[i + 1] if i + 1 < len(sys.argv) else 'unknown'
        blk, sp = AE.emit('mirror_verify', act, [os.path.basename(zpath)],
                          [('files', len(names)), ('rows', len(rows)),
                           ('mismatch', bad), ('declared', declared),
                           ('ls-remote', live[:12] if live else '-')], verdict)
        print("\n" + blk)
        print("  sidecar written: %s" % sp)
    print("\n  ### VERDICT: %s" % verdict)
    print("  ### neither clause alone is the verification; the law requires both.")
    return 0 if ok else 1


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(*sys.argv[1:4]))
