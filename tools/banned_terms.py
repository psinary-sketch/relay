# -*- coding: utf-8 -*-
"""banned_terms.py -- THE BANNED-TERM REVIEW, BUILT (b142).

### WHY THIS EXISTS. Rule 3 bans two stems from the record's own voice. The
### review has been run act after act by hand-rolled one-liners, rewritten each
### time. b139 filed the general answer -- BUILD THE CHECK RATHER THAN PRAISE
### THE HABIT -- and b141 applied it to the probe habit. This applies it to the
### banned-term habit, which was the last discretionary check in the closing
### sequence.

### THE STEMS: "gap" and "blind".
### THE EXCEPTIONS, which are part of the rule and not softenings of it:
###   - QUOTED KERNEL IDENTIFIERS (sector_pattern_gap and its kin);
###   - CLAY / BIBLIOGRAPHY CITATIONS ("mass gap");
###   - RETIRED TERMS QUOTED INSIDE CORRECTION RECORDS (EXECUTOR_RULES sec 5);
###   - this file itself, which cannot state the rule without naming the stems.
### Anything else is a LIVE USE and must be corrected before shipping.

### THE SCOPE, AND IT IS THE WHOLE DIFFICULTY -- SEE THE DEFECT NOTE BELOW.
### The rule governs THE ACT'S OWN VOICE, so the scope is the act's ADDED LINES
### plus the whole of files the act CREATES. It is NOT whole existing files: a
### thirty-thousand-line ledger carries decades of quoted history that the act
### did not write and may not rewrite.

# ### DEFECT FIXED b142, ON THE CHECK'S FIRST RUN, AND IT IS THE SAME SPECIES
# ### AS THE PROBE GENERATOR'S: the first version scanned WHOLE FILES and
# ### returned 178 "live uses", every one of them a pre-existing line in a
# ### ledger this act only appended to. A scanner with no scope control does not
# ### report the rule -- it reports the corpus. ### THE SCOPE IS NOW DERIVED
# ### MECHANICALLY FROM THE ACT'S OWN DIFF, which is the probe-generation
# ### convention's principle carried to the second check that needed it.
# ### A SECOND DEFECT, FIXED IN THE SAME PASS: stdout was inheriting cp1252 and
# ### crashed on the first Greek letter it met. A check that dies on its own
# ### input is not a check.

Usage:
    python banned_terms.py --diff <repo> [<rev>]     scope = added lines vs rev
    python banned_terms.py --new <file> [<file>...]  scope = whole file (new files)
    both may be combined; --new files are appended to the --diff scope.
"""
import io
import os
import re
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

STEMS = ['gap', 'blind']
PAT = re.compile(r'\b(' + '|'.join(STEMS) + r')\w*', re.I)

EXCEPT = [
    (re.compile(r'sector_pattern_gap|\w_gap\b|\bgap_\w|`[^`]*gap[^`]*`', re.I),
     'QUOTED KERNEL IDENTIFIER'),
    (re.compile(r'mass gap', re.I), 'CLAY / BIBLIOGRAPHY CITATION'),
    (re.compile(r'retired|superseded|correction record|formerly|no longer|banned|vocabulary repair',
                re.I), 'RETIRED TERM IN A CORRECTION RECORD'),
    (re.compile(r'STEMS|stems scanned|banned[- ]term', re.I), "THE SCANNER'S OWN RULE TEXT"),
]


def classify(line):
    for rx, name in EXCEPT:
        if rx.search(line):
            return name
    return None


def added_lines(repo, rev):
    """### THE SCOPE, MECHANICALLY DERIVED. Nothing is typed; the act's own diff
    says which lines are the act's voice."""
    out = subprocess.run(['git', 'diff', rev, '-U0'], cwd=repo, capture_output=True,
                         text=True, encoding='utf-8', errors='replace').stdout
    cur, rows, n = None, [], 0
    for line in out.splitlines():
        if line.startswith('+++ b/'):
            cur = line[6:]
        elif line.startswith('@@'):
            m = re.search(r'\+(\d+)', line)
            n = int(m.group(1)) if m else 0
        elif line.startswith('+') and not line.startswith('+++') and cur:
            rows.append((cur, n, line[1:]))
            n += 1
    return rows


def main(argv):
    scope, srcs = [], []
    i = 0
    while i < len(argv):
        if argv[i] == '--diff':
            repo = argv[i + 1]
            rev = argv[i + 2] if i + 2 < len(argv) and not argv[i + 2].startswith('--') else 'HEAD'
            scope += added_lines(repo, rev)
            srcs.append("added lines in %s vs %s" % (repo, rev))
            i += 3 if rev != 'HEAD' or (i + 2 < len(argv) and not argv[i + 2].startswith('--')) else 2
        elif argv[i] == '--new':
            i += 1
            while i < len(argv) and not argv[i].startswith('--'):
                txt = io.open(argv[i], encoding='utf-8', errors='replace').read()
                scope += [(argv[i], k, ln) for k, ln in enumerate(txt.splitlines(), 1)]
                srcs.append("whole file %s (created this act)" % os.path.basename(argv[i]))
                i += 1
        else:
            i += 1

    hits = live = 0
    rows = []
    for path, ln, text in scope:
        if PAT.search(text):
            hits += 1
            cls = classify(text)
            if cls is None:
                live += 1
            rows.append((path, ln, cls, text.strip()[:88]))

    files = sorted({p for p, _, _ in scope})
    print("=" * 78)
    print("BANNED-TERM REVIEW (banned_terms.py, b142) -- RUN, NOT CLAIMED")
    print("=" * 78)
    print("  stems scanned    : %s" % ", ".join(STEMS))
    for s in srcs:
        print("  scope            : %s" % s)
    print("  files in scope   : %d" % len(files))
    print("  lines in scope   : %d   ### the act's own voice, not the corpus" % len(scope))
    print("  hits found       : %d" % hits)
    print("  live uses        : %d" % live)
    if rows:
        print("\n  THE HIT TABLE -- every hit shown with its class; none dropped:")
        for p, ln, cls, text in rows:
            print("   %-32s :%-6d %s" % (os.path.basename(p), ln,
                                         cls or "### LIVE USE -- CORRECT BEFORE SHIPPING"))
            print("      %s" % text)
    print("\n  VERDICT          : %s" % ("CLEAN" if live == 0 else "NOT CLEAN"))
    print("  ### the verdict reads the LIVE count, not the hit count -- a scope may")
    print("  ### carry excepted hits and still be clean, and that is the whole")
    print("  ### reason the classes are printed rather than filtered silently.")
    return 0 if live == 0 else 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
