# -*- coding: utf-8 -*-
"""probe_from_diff.py -- THE PROBE-GENERATION CONVENTION (minted b141).

### WHY THIS EXISTS. Mirror and content probes were retyped from memory of what
### had just been written. Three times -- b129, b133, b140 -- a probe returned
### ABSENT and the probe, not the fact, was wrong. Each was caught by looking,
### per b129's rule; the habit that produced it did not change. b139 filed the
### general answer: BUILD THE CHECK RATHER THAN PRAISE THE HABIT. This is that,
### applied to its author.

### THE CONVENTION: probes are EXTRACTED MECHANICALLY from the act's own diff.
### The generator picks distinctive strings from ADDED lines. Nothing is typed.

Usage:
    python probe_from_diff.py <repo> [<rev>] [--zip <path>]

  <repo>  the repository whose diff supplies the probes
  <rev>   what to diff against (default HEAD~1)
  --zip   if given, each probe is checked against every file in the archive and
          the verdict printed; otherwise the probes are printed for use.

### THE RULE THAT MAKES IT WORTH HAVING: the output is used AS PRODUCED. If the
### operator edits the probe list, the convention has failed for that act and
### the act must say so.
"""
import os
import re
import subprocess
import sys
import zipfile

MINLEN, MAXLEN, NPROBE = 28, 70, 12
# strings that carry no discriminating power
BORING = re.compile(r'^[\s\W\d]*$')


def added_lines(repo, rev):
    out = subprocess.run(['git', 'diff', rev, '-U0'], cwd=repo,
                         capture_output=True, text=True,
                         encoding='utf-8', errors='replace').stdout
    cur, rows = None, []
    for line in out.splitlines():
        if line.startswith('+++ b/'):
            cur = line[6:]
        elif line.startswith('+') and not line.startswith('+++') and cur:
            rows.append((cur, line[1:]))
    return rows


def norm(s):
    """THE ONE normalisation. Applied to probe AND haystack alike -- see the
    defect note at the zip check. Never normalise one side only."""
    s = re.sub(r'[*#`>|]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def candidates(rows):
    """Distinctive substrings of added lines, ranked by length then rarity."""
    seen, out = set(), []
    for path, text in rows:
        t = norm(text)
        if len(t) < MINLEN or BORING.match(t):
            continue
        # take the longest clean run of words
        for frag in re.split(r'[.;:()\[\]]', t):
            frag = frag.strip()
            if MINLEN <= len(frag) <= MAXLEN and not BORING.match(frag):
                key = frag.lower()
                if key not in seen:
                    seen.add(key)
                    out.append((path, frag))
                break
    out.sort(key=lambda pf: -len(pf[1]))
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    repo = sys.argv[1]
    rev = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else 'HEAD~1'
    zpath = None
    if '--zip' in sys.argv:
        zpath = sys.argv[sys.argv.index('--zip') + 1]

    rows = added_lines(repo, rev)
    cands = candidates(rows)
    step = max(1, len(cands) // NPROBE)
    probes = cands[::step][:NPROBE]

    print("=" * 78)
    print("PROBES GENERATED MECHANICALLY FROM THE DIFF (probe_from_diff, b141)")
    print("  repo   : %s" % repo)
    print("  against: %s" % rev)
    print("  added lines: %d ; candidate strings: %d ; probes emitted: %d"
          % (len(rows), len(cands), len(probes)))
    print("### NOTHING BELOW WAS TYPED. If the operator edits this list, the")
    print("### convention has failed for that act and the act must say so.")
    print("=" * 78)

    if not zpath:
        for i, (path, frag) in enumerate(probes, 1):
            print("%2d  [%s]\n    %s" % (i, os.path.basename(path), frag))
        return 0

    z = zipfile.ZipFile(zpath)
    names = [n for n in z.namelist() if n != 'MANIFEST.md']
    # ### DEFECT FIXED b141, ON THE CONVENTION'S FIRST USE: the probe was
    # ### normalised (markdown stripped, whitespace collapsed) and the HAYSTACK
    # ### WAS NOT, so every probe spanning a bold or code marker failed against
    # ### text that plainly contained it. 6 of 12 first-run probes died this way.
    # ### BOTH SIDES MUST BE NORMALISED IDENTICALLY, and they are here.
    blobs = {n: norm(z.read(n).decode('utf-8', 'replace')) for n in names}
    miss = 0
    print("  checking against: %s (%d files)\n" % (os.path.basename(zpath), len(names)))
    for i, (path, frag) in enumerate(probes, 1):
        hit = [n for n in names if frag in blobs[n]]
        ok = bool(hit)
        miss += 0 if ok else 1
        print("%2d  %-8s %s" % (i, "PRESENT" if ok else "ABSENT", frag[:62]))
        if ok:
            print("             in %s" % ", ".join(os.path.basename(h) for h in hit))
    print("\n### %d of %d probes PRESENT ; %d absent" % (len(probes) - miss, len(probes), miss))
    print("### VERDICT: %s" % ("CLEAN" if miss == 0 else "INVESTIGATE -- absent probes above"))
    return 0


if __name__ == '__main__':
    sys.exit(main())
