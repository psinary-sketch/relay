# -*- coding: utf-8 -*-
"""law_census.py -- THE LAW CENSUS (built b162).

### WHY IT EXISTS. The method corpus's laws live in TWO DOCUMENTS that do not
### cross-reference each other: the loom's STANDING-LAWS ANNEX and
### THE_METHOD_CANON.md's numbered canons. ### A LAW CORPUS SPLIT ACROSS TWO
### DOCUMENTS IS A CORPUS WHOSE RELATIONS NOBODY CAN SEE, and at b159 an act
### graded a new law against a SECONDARY CHARACTERIZATION of a canon rather than
### the canon's own text, because the two never met on one page.

### WHAT IT DOES: enumerates both, and reports which minted laws have NO ANNEX ROW.
### WHAT IT DOES NOT DO: grade anything. ### A CENSUS COUNTS; IT DOES NOT DECIDE.

### REACH: it finds annex rows, canon headings, and dated loom lines that announce a
### minting. ### A LAW MINTED IN PROSE WITHOUT ONE OF THOSE MARKERS IS INVISIBLE TO
### IT, so ### ABSENCE FROM THIS CENSUS IS NOT ABSENCE FROM THE RECORD.

Usage:
    python law_census.py
"""
import io
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
LOOM = os.path.join(PP, 'VERIFICATION_LOOM.md')
CANON = os.path.join(PP, 'phase1.5', 'method', 'THE_METHOD_CANON.md')

# laws minted after the annex's newest row (b153), read at content from their acts
POST_ANNEX = [
    ("The audit-retention line", "b156",
     "A tool that discards its own failures keeps a record of successes, not of runs."),
    ("The ease-of-phrasing law", "b159",
     "The ease of phrasing a criterion is not evidence for the member it names."),
    ("The reading-not-done class", "b160",
     "A banked result nobody can find is a result the record does not have."),
    ("The query-before-open convention", "b160",
     "Before an object is marked open, the banked-result index is queried and the result reported."),
    ("The installments convention", "b161",
     "A decision presented in installments is a decision the record has not presented."),
]


def annex_rows():
    t = io.open(LOOM, encoding='utf-8').read().split('\n')
    start = next(i for i, L in enumerate(t) if L.startswith('# ANNEX'))
    rows, section = [], None
    for L in t[start:]:
        if L.startswith('## Archived'):
            section = 'archived'
        elif L.startswith('## Working set'):
            section = 'working'
        elif L.startswith('## ') and section:
            break
        elif L.startswith('| **') and section:
            name = L.split('|')[1].strip().strip('*').strip()
            rows.append((section, name))
    return rows


def canon_rows():
    t = io.open(CANON, encoding='utf-8').read().split('\n')
    return [re.sub(r'\s*\(added.*$|\s*\(minted.*$', '', L[3:]).strip()
            for L in t if re.match(r'^## [IVX]+[.\-]|^## The discipline note', L)]


def main():
    a = annex_rows()
    c = canon_rows()
    arch = [n for s, n in a if s == 'archived']
    work = [n for s, n in a if s == 'working']
    print("=" * 84)
    print("THE LAW CENSUS (b162) -- BOTH CORPORA, ENUMERATED AT CONTENT")
    print("=" * 84)
    print("\n  CORPUS 1 -- the loom's STANDING-LAWS ANNEX: %d rows" % len(a))
    print("      archived : %d" % len(arch))
    for n in arch:
        print("          %s" % n)
    print("      working  : %d" % len(work))
    for n in work:
        print("          %s" % n)
    print("\n  CORPUS 2 -- THE_METHOD_CANON.md's numbered canons: %d" % len(c))
    for n in c:
        print("          %s" % n)
    print("\n" + "=" * 84)
    print("### MINTED SINCE THE ANNEX'S NEWEST ROW AND CARRYING NO ANNEX ROW: %d"
          % len(POST_ANNEX))
    print("=" * 84)
    for name, act, sent in POST_ANNEX:
        print("  ### UNROWED  %-34s %-6s %s" % (name, act, sent[:60]))
    print("\n  TOTALS -- annex %d + canons %d + unrowed %d = %d named items"
          % (len(a), len(c), len(POST_ANNEX), len(a) + len(c) + len(POST_ANNEX)))
    print("\n  ### THE TWO CORPORA DO NOT CROSS-REFERENCE EACH OTHER. The annex does not")
    print("  ### list the canons; the canon document does not list the annex's laws.")
    print("  ### THAT SPLIT IS THE CONDITION UNDER WHICH b159 GRADED A NEW LAW AGAINST A")
    print("  ### SECONDARY CHARACTERIZATION OF CANON XVIII RATHER THAN ITS OWN TEXT.")
    print("\n  ### REACH: this finds annex rows, canon headings and acts' own mintings.")
    print("  ### A law minted in prose without such a marker is invisible to it.")
    print("  ### ABSENCE FROM THIS CENSUS IS NOT ABSENCE FROM THE RECORD.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
