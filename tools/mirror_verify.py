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
import io
import json
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


### CLAUSE 3 -- THE ARCHIVE'S CONTENTS AGAINST **THE ROSTER**, ADDED b183.
### WHY IT EXISTS. At b182 a file was added to the roster artifact, the mirror was
### rebuilt, and it verified ### CLEAN ON BOTH CLAUSES AT 33 FILES **WITHOUT THE FILE
### IN IT**. ### CLAUSE 1 CHECKS THE ARCHIVE AGAINST ITS OWN MANIFEST -- internally
### consistent by construction -- AND CLAUSE 2 CHECKS ONLY THE SOURCE PIN.
### ### SO A FILE THAT NEVER ENTERED THE STAGING DIRECTORY WAS INVISIBLE TO BOTH.
### That is b130's stale-build law in its THIRD dress (b130: built one commit early;
### b144: a flat-namespace collision dropped a file; b182: a roster edit the builder
### never read). ### THE COMMON SHAPE IS NOT STALENESS. IT IS ### A CHECK WHOSE SCOPE
### EXCLUDES THE DEFECT, AND SUCH A CHECK PASSES **BECAUSE** IT IS BLINKERED, NOT
### DESPITE IT.
###
# ### THE LIMITS OF THIS CLAUSE, IN ITS OWN HEADER SO IT IS NOT TRUSTED BEYOND THEM:
# ### (1) IT REPLICATES THE BUILDER'S FLAT-NAMING RULE IN A SECOND LANGUAGE.
# ###     The builder is PowerShell; this is Python. ### IF ONE IS EDITED AND NOT THE
# ###     OTHER THEY DRIFT, AND THIS CLAUSE WOULD THEN FAIL A GOOD BUILD OR PASS A BAD
# ###     ONE. ### THIS ACT CREATED THAT COUPLING; IT DID NOT CLOSE IT, AND SAYING SO
# ###     IS THE POINT. The mitigation is only that it FAILS CLOSED.
# ### (2) It compares NAMES, not contents -- clause 1 owns bytes and md5s.
# ### (3) It reads the roster from disk. ### A ROSTER THAT IS ITSELF WRONG PRODUCES A
# ###     CLEAN CLAUSE 3, and no clause here checks the roster against the author's
# ###     intent, because no instrument can.
ROSTER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mirror_roster.json')


def staged_names(paths):
    """### Replicate the builder's rule EXACTLY: leaf; on collision parent + '__' +
    ### leaf; if it still collides the builder THROWS, so here it is a hard error."""
    seen, out = set(), []
    for r in paths:
        n = r.replace('\\', '/')
        leaf = n.split('/')[-1]
        parent = n.split('/')[-2] if '/' in n else ''
        if leaf in seen and parent:
            leaf = parent + '__' + leaf
        if leaf in seen:
            raise ValueError("ROSTER COLLISION unresolved for %r -> %r" % (r, leaf))
        seen.add(leaf)
        out.append(leaf)
    return out


def clause3(names, roster_path=None):
    rp = roster_path or ROSTER
    msg = []
    if not os.path.exists(rp):
        msg.append("  ### CLAUSE 3 : HARD FAILURE -- ROSTER NOT FOUND at %s" % rp)
        msg.append("  ### A verification with no roster is not a verification.")
        return False, msg
    try:
        doc = json.loads(io.open(rp, encoding='utf-8-sig').read())
        paths = list(doc.get('files') or [])
    except Exception as e:
        msg.append("  ### CLAUSE 3 : HARD FAILURE -- ROSTER UNREADABLE (%s)" % e)
        return False, msg
    if not paths:
        # ### THE ZERO CASE. b167 had to add an empty-scope hard failure to
        # ### banned_terms.py; b179's hook cleared an EMPTY staged set on its first
        # ### control run. ### IN THIS RECORD EMPTINESS READS AS SUCCESS UNLESS A LINE
        # ### IS WRITTEN AGAINST IT, so here is the line.
        msg.append("  ### CLAUSE 3 : HARD FAILURE -- THE ROSTER IS EMPTY.")
        msg.append("  ### An empty roster trivially matches an empty archive.")
        msg.append("  ### THAT IS NOT A PASS. A verdict over an empty scope is not a verdict.")
        return False, msg
    try:
        expect = set(staged_names(paths))
    except ValueError as e:
        msg.append("  ### CLAUSE 3 : HARD FAILURE -- %s" % e)
        return False, msg
    have = {n for n in names if n.lower() != 'manifest.md'}
    missing = sorted(expect - have)
    extra = sorted(have - expect)
    msg.append("  roster entries (source paths) : %d" % len(paths))
    msg.append("  archive files (excl MANIFEST) : %d" % len(have))
    msg.append("  in roster, MISSING from archive : %d" % len(missing))
    msg.append("  in archive, NOT in roster       : %d" % len(extra))
    for m in missing[:8]:
        msg.append("      MISSING : %s" % m)
    for x in extra[:8]:
        msg.append("      EXTRA   : %s" % x)
    if missing or extra:
        msg.append("  ### CLAUSE 3 : NOT CLEAN -- HARD FAILURE.")
        msg.append("  ### THE ARCHIVE DOES NOT MATCH THE ROSTER, and this is exactly the")
        msg.append("  ### b182 case that clauses 1 and 2 both passed.")
        return False, msg
    msg.append("  CLAUSE 3 : CLEAN -- archive and roster agree, name for name")
    return True, msg


def main(zpath, remote, branch='main'):
    z = zipfile.ZipFile(zpath)
    names = [n for n in z.namelist() if n != 'MANIFEST.md']
    man = z.read('MANIFEST.md').decode('utf-8', 'replace')
    rows = ROW.findall(man)
    byname = {n.split('/')[-1]: n for n in names}

    print("=" * 78)
    print("MIRROR VERIFICATION -- ALL THREE CLAUSES (b142; clause 3 added b183)")
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

    # ---------------- CLAUSE 3 (b183) ----------------
    print("\n--- CLAUSE 3: THE ARCHIVE'S CONTENTS AGAINST THE ROSTER ---")
    c3, rmsg = clause3(names)
    for line in rmsg:
        print(line)

    ok = (bad == 0) and agree and c3
    verdict = ("CLEAN ON ALL THREE CLAUSES" if ok else "NOT CLEAN")
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
    print("  ### NO CLAUSE ALONE IS THE VERIFICATION; THE LAW REQUIRES ALL THREE.")
    print("  ### clause 1 is the archive against ITSELF, clause 2 is the pin, and")
    print("  ### clause 3 is the archive against the ROSTER -- ### THE ONLY ONE OF THE")
    print("  ### THREE THAT CAN SEE A FILE THAT NEVER ENTERED THE STAGING DIRECTORY.")
    return 0 if ok else 1


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(*sys.argv[1:4]))
