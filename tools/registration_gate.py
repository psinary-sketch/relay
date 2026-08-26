# -*- coding: utf-8 -*-
"""registration_gate.py -- THE INDEX-QUERY GATE, IN THE PATH (built b185).

### WHY THIS EXISTS. b160 built the banked-result index and a convention with it:
### ### "BEFORE AN OBJECT IS MARKED OPEN, NAVIGATOR-ASSERTED, OR REQUIRING A
### ### CONSTRUCTION, THE INDEX IS QUERIED AND THE QUERY'S RESULT REPORTED."
### It built that index because ### "TWO ACTS DID NOT READ A RESULT THE RECORD
### ALREADY HELD."
### At b182 this seat marked THREE ROUTES "NAVIGATOR-ASSERTED. UNREAD" and
### "REQUIRING A CONSTRUCTION", and ### QUERIED NOTHING. The answer was one query
### away: `boundary-license` -> b151 -> "no license derives". ### A WHOLE PROGRAM
### WAS DRAFTED FOR WORK THAT WAS ALREADY FINISHED.
###
### ### THE INDEX DID NOT FAIL. IT WAS NOT ASKED.
### That is why this is a GATE and not a reminder:
### ### **AN INSTRUMENT THAT MUST BE REMEMBERED IS NOT AN INSTRUMENT.**

### WHAT IT DOES. Given a registration file, it looks for the marks the b160
### convention names. If any is present, the registration MUST also carry a
### recorded index-query result. No result -> HARD FAILURE, and the registration
### is not bankable.

# ### THE LIMITS, IN THE HEADER SO THE GATE IS NOT TRUSTED BEYOND THEM:
# ### (1) IT MATCHES TEXT. It cannot tell a real query from the WORDS of one, and
# ###     an act that types "NO KEY" without running anything passes. ### IT RAISES
# ###     THE COST OF SKIPPING THE QUERY; IT DOES NOT MAKE SKIPPING IMPOSSIBLE.
# ### (2) It knows the marks it is given. A mark phrased in words it does not know
# ###     is invisible -- the same false-miss class b164 named for the index's own
# ###     keys: ### KEYS CLOSE FALSE HITS, NOT FALSE MISSES.
# ### (3) ### IT CHECKS THAT A QUERY WAS RECORDED, NOT THAT IT WAS THE RIGHT QUERY.
# ###     b182 would have been caught by this gate only if it had queried at all;
# ###     an act that queries the wrong keys still passes. ### NO INSTRUMENT HERE
# ###     CHECKS THAT AN OBJECT WAS QUERIED UNDER THE NAME IT ACTUALLY HAS.

#
# ### AND A BUILD NOTE KEPT BECAUSE IT IS THE SECOND TIME: this file's first run
# ### died on an UNCLOSED MODULE DOCSTRING, exactly as b179's pre-commit hook did.
# ### THE SAME SLIP, IN THE SAME SHAPE, SIX ACTS APART. Both were caught at once by
# ### the interpreter, so neither shipped -- ### BUT A DEFECT THAT REPEATS IS NOT AN
# ### ACCIDENT, IT IS A HABIT, and naming it is cheaper than pretending the first
# ### one taught me something.
"""

import io
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE MARKS, TAKEN FROM b160's CONVENTION WORD FOR WORD.
MARKS = [
    (re.compile(r'\bNAVIGATOR-ASSERTED\b', re.I), 'NAVIGATOR-ASSERTED'),
    (re.compile(r'\bREQUIRING A CONSTRUCTION\b|\bNEEDS A CONSTRUCTION\b', re.I),
     'REQUIRING A CONSTRUCTION'),
    (re.compile(r'\bMARKED OPEN\b|\bIS OPEN\b|\bSTILL OPEN\b|\bLEFT OPEN\b', re.I), 'OPEN'),
    (re.compile(r'\bUNREAD\b', re.I), 'UNREAD'),
]

# ### EVIDENCE THAT THE QUERY RAN AND ITS RESULT WAS RECORDED.
QUERY = re.compile(
    r'NO KEY|banked_index|banked-result index|HIT\s*->|index quer(?:y|ies|ied)', re.I)


def check(path):
    if not os.path.exists(path):
        return 2, ["### HARD FAILURE -- registration not found: %s" % path]
    txt = io.open(path, encoding='utf-8', errors='replace').read()
    if not txt.strip():
        # ### THE ZERO CASE. b167 added an empty-scope hard failure to
        # ### banned_terms.py; b179's hook cleared an EMPTY staged set; b183's
        # ### clause 3 refuses an empty roster. ### IN THIS RECORD EMPTINESS READS
        # ### AS SUCCESS UNLESS A LINE IS WRITTEN AGAINST IT.
        return 2, ["### HARD FAILURE -- THE REGISTRATION IS EMPTY.",
                   "### An empty file trivially carries no unbacked mark.",
                   "### THAT IS NOT A PASS. A verdict over an empty scope is not a verdict."]

    found = []
    for rx, name in MARKS:
        for m in rx.finditer(txt):
            line = txt.count('\n', 0, m.start()) + 1
            found.append((name, line, txt.split('\n')[line - 1].strip()[:90]))

    out = ["  registration : %s" % os.path.basename(path),
           "  marks found  : %d" % len(found)]
    for n, ln, s in found[:8]:
        out.append("      %-26s line %-5d %s" % (n, ln, s))
    if len(found) > 8:
        out.append("      ... and %d more" % (len(found) - 8))

    if not found:
        out.append("  VERDICT      : PASS -- no mark requires a query")
        out.append("  ### and that means ONE thing only: none of the known marks")
        out.append("  ### appears. ### IT IS NOT A REVIEW OF THE REGISTRATION.")
        return 0, out

    q = QUERY.search(txt)
    if q:
        line = txt.count('\n', 0, q.start()) + 1
        out.append("  query result : RECORDED at line %d" % line)
        out.append("  VERDICT      : PASS -- marks present and a query result is recorded")
        out.append("  ### THE GATE CHECKS THAT A QUERY WAS RECORDED, NOT THAT IT WAS THE")
        out.append("  ### RIGHT QUERY. An act that queries the wrong keys still passes.")
        return 0, out

    out.append("  query result : ### ABSENT")
    out.append("  ### VERDICT   : HARD FAILURE -- NOT BANKABLE.")
    out.append("  ### This registration marks an object OPEN / NAVIGATOR-ASSERTED /")
    out.append("  ### UNREAD / REQUIRING A CONSTRUCTION and records no index query.")
    out.append("  ### b160's convention: the index is queried and the query's result")
    out.append("  ### REPORTED before such a mark is made.")
    out.append("  ### THIS IS THE b182 FAILURE: three routes marked, nothing queried,")
    out.append("  ### and the answer one query away.")
    out.append("  ### To satisfy: python relay/tools/banked_index.py --query <object>")
    return 1, out


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    rc = 0
    for p in argv:
        print("--- INDEX-QUERY GATE (b185) ---")
        code, lines = check(p)
        for l in lines:
            print(l)
        print()
        rc = max(rc, code)
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
