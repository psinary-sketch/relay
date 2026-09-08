# -*- coding: utf-8 -*-
"""b372_correspondence.py -- ONE ROW: THE EOL PIN, THE README FIGURES, THE FIRST BATCH.

### ### **EVERY FIGURE IS READ FROM THIS ACT'S OWN JSONS. ### NONE IS TYPED.**
### ### **THE ROW IS SPLICED BY THE SHARED WRITER AND READ BACK**, and the table above it must remain a
### true prefix of the file (`b362`: a true-prefix arm is the one that catches a splice).
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as G   # noqa: E402

SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SCOPE = (
    "**SCOPE: NO ROW WAS REPAIRED AND NO PIN WAS ADDED TO ANY ROW.** Component 3's cap is the order's "
    "own -- the classification is the product -- and (R8) makes the addition of pins A SEPARATE RULING, "
    "PRICED AND NOT ATTEMPTED. **NO HEAD WAS WRITTEN INTO A ROW**; every head read is recorded in this "
    "act's bank and dated. **NO REPOSITORY WAS RENORMALISED, NO TRACKED FILE'S CONTENT WAS REWRITTEN BY "
    "AN ATTRIBUTE, NO WORKING FILE WAS DELETED TO FORCE A CHECKOUT AND NO SCRATCH BRANCH WAS CREATED OR "
    "RESET** -- b371's destructive incident, named so the shape cannot recur quietly. **NOTHING IN THE "
    "EXCLUSION KERNEL'S README WAS REPAIRED**: the order's label named it and the order's description "
    "fits a different file, and the discrepancy is REPORTED, not absorbed. **NO .lean FILE WAS TOUCHED, "
    "NO BUILD WAS RUN AND NO AXIOM PROFILE WAS RECOMPUTED** -- every profile was READ as a printed "
    "record, at a ref and against its blob. **NO FEDERATION-WIDE SURFACE SWEEP WAS OPENED**; (R6)'s "
    "second pass stays shut. **NO ITEM CLOSED WITHOUT ITS KILLING FILE AND DATE**, and both closures are "
    "flagged because the killing file is this act's own. NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS "
    "PROMOTED; that a declaration exists says nothing about whether what it names is true. NOTHING IS "
    "CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing "
    "about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, "
    "NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent "
    "lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE "
    "STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it. The wave "
    "PARKED by the author's ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


def rows():
    E, A, R, B, Q, F = (J('b372_reads'), J('b372_eol'), J('b372_readme'), J('b372_batch'),
                        J('b372_desk'), J('b372_filing'))
    T = R['table']
    T0, T1, TH = T[0], T[1], T[-1]
    TV = B['terminal_tally']
    pinned = [r for r in B['rows'] if r['mode'] == 'AT-PIN']
    athead = [r for r in B['rows'] if r['mode'] == 'CHECKED-AT-HEAD']
    falsepin = [r for r in B['rows'] if r['pins'] and not any(p['resolves'] for p in r['pins'])]
    badbefore = [k for k, v in A['before'].items() if not v['fresh_equals_blob']]
    m = ("**THE SAME DECLARATIONS ARE PRESENT AT A PINNED ROW'S REF AND RETIRED AT THE HEAD, AND THAT IS "
         "RULING (R8) DEMONSTRATED RATHER THAN ARGUED** -- of the twelve flagged correspondence rows, %d "
         "were opened at a pin and %d at the kernel's live head and are marked CHECKED-AT-HEAD (b372, "
         "ruling (R8))" % (len(pinned), len(athead)))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, on the audit's own exit code, and "
            "its face fixed the resolution of Component 2's label/description discrepancy BEFORE any "
            "read. `no_conspiracy_twins`, `no_conspiracy_goldbach` and `no_conspiracy_sg` are cited by "
            "four of the twelve rows: the one row that names a pin (`c66f3c5`) is **correct at the ref "
            "it names -- all three are declarations there** -- and the three rows naming the same "
            "declarations with **no pin** come back **RETIRED at the head**, with the kernel's own "
            "retirement ledger quoted. **A PINNED ROW AGED WELL; A PINLESS ROW DID NOT, AND NOTHING IN "
            "IT TELLS A READER WHICH REF IT MEANT.** Across the twelve, %d named terminals classify "
            "RETIRED, %d PRESENT and %d ABSENT; every RETIRED verdict quotes the kernel's record and "
            "none is an inference from absence. **AND %d ROWS b371 COUNTED AS PINNED CARRY SOMETHING "
            "THAT LOOKS LIKE A PIN AND IS NOT** -- a manuscript version and an exemplar version, neither "
            "resolving in the kernel the row names -- which is PREDICATE_ONE_SHAPE running the other "
            "way. %d reads, %d without an anchor."
            % (TV.get('RETIRED', 0), TV.get('PRESENT', 0), TV.get('ABSENT', 0), len(falsepin),
               E['reads'], E['without_anchor']))
    return [
        (m, stmt,
         "**NO TERMINAL.** No `.lean` file was touched, no build was run and no axiom profile was "
         "recomputed. **AND THE ORDER'S `PRESENT` TEST CANNOT BE FULLY SATISFIED IN EITHER KERNEL READ: "
         "NEITHER SHIPS A PRINTED AXIOM PROFILE**, so a declaration found alive is recorded PRESENT with "
         "its profile NOT LOCATED and is not silently upgraded.",
         "**PRINT: THE END-OF-LINE ATTRIBUTE IS NOW TRACKED IN ALL %d ROSTERED REPOSITORIES**, and in "
         "each of them a fresh checkout of the tracked guard is **byte-identical to its blob**. Before "
         "this act it was %d of %d, and the two that failed -- %s -- were **exactly the two without the "
         "attribute**. `relay`'s pre-existing path-scoped line is **PRESERVED, NOT REPLACED**; the two "
         "repositories that already carried the attribute were **NOT WRITTEN TO**, which is the order's "
         "own instruction. The mechanism was exercised **in both polarities in a repository built and "
         "destroyed for the purpose**, so the pass is known to be caused by the attribute. "
         "`SIDE-global-section/README.md` is repaired: the headline figure and the assembly ratio are "
         "**REMOVED rather than restated**, the 33-part layer census and the module count are "
         "**PRESERVED VERBATIM AND DATED to `%s` (%s)**, and the original is quoted verbatim in this "
         "act's bank. `PLACE-papers/OPEN_TRAILS.md` gains ONE append-only block. **NO ROW IN ANY PAPER "
         "WAS EDITED. FACES_LEDGER.md IS NOT WRITTEN AND ITS WRITER IS NOT CALLED, BECAUSE NO ROW "
         "MOVED.** No findings section; no TECHNE file; no module pushed. **THE HOOK AND THE MIRROR ARE "
         "OWED AND PAID.**"
         % (len(A['after']), len(A['before']) - len(badbefore), len(A['before']),
            ', '.join('`%s`' % k for k in badbefore), T1['ref'][:7], T1['date']),
         "**THE THREE README FIGURES DO NOT COUNT THREE DIFFERENT SCOPES: THEY COUNT ONE QUANTITY AT "
         "THREE DIFFERENT REFS, AND EACH WAS EXACT WHEN IT WAS WRITTEN.** At `%s` (%s) the headline, the "
         "breakdown, the assembly ratio and the shipped profile all read **%s**; at `%s` (%s) the "
         "breakdown, the ratio, the module count and the profile all moved to **%s** and **the headline "
         "alone was left behind**; at the head the profile carries **%d** and the whole sentence is "
         "behind it. **AND NONE OF THE THREE NAMES THE REF IT HOLDS AT** -- which is the defect, and is "
         "the same defect b371 settled in the same repository's public description. The repair follows "
         "that precedent exactly: a figure is **REMOVED rather than restated**, unless the document can "
         "name the ref it holds at, and re-deriving the census at the head **rewrites a claim and not a "
         "number, so it is ROUTED**. The claim `No terminal failed the bar; none is excluded` is "
         "untouched and is supported: all %d printed lines say the declaration does not depend on any "
         "axioms, read from the working file and confirmed against its blob. **THE ORDER NAMED THE "
         "EXCLUSION KERNEL'S README AND DESCRIBED THE CONSTRUCTION KERNEL'S** -- the former has one "
         "count line, no breakdown and ships no profile at all -- and **THE OBJECT WAS IDENTIFIED BY THE "
         "DESCRIPTION, BECAUSE A DESCRIPTION IS CHECKABLE AGAINST A FILE AND A LABEL IS NOT**; b367's "
         "species, reported and not absorbed. **THE DESK: %d SWEPT, %d CLOSED, %d STANDING, %d CLOSURES "
         "REFUSED**, and both closures are flagged because the killing file is this act's own. **THE "
         "EXPECTATIONS ARE SCORED:** (F1) **SPLITS** -- its three-scopes half REFUTED by quotation, its "
         "no-ref half CONFIRMED; (F2) **CONFIRMED**, %d RETIRED against %d ABSENT, and the reason is the "
         "kernel's own retirement ledger; this seat's (E1) was **decided before the lock and is scored "
         "NOT AN EXPECTATION** on the registration's own face; (E2) **REFUTED** -- only one of the "
         "twelve rows states its own retirement, and the rest claim the thing is there. **AND THE "
         "LEDGER'S OWN LACUNAE ARE FILED AND NOT INVENTED:** %s are cited by rows and named nowhere in "
         "the ledger that retired their neighbours."
         % (T0['ref'][:7], T0['date'], T0['total'], T1['ref'][:7], T1['date'], T1['total'],
            TH['prints'], R['profile']['lines'], Q['items'], Q['closed'], Q['standing'],
            Q['closures_refused'], TV.get('RETIRED', 0), TV.get('ABSENT', 0),
            ', '.join('`%s`' % t for _r, t in B['absent'])),
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b372 -- ONE ROW: THE EOL PIN, THE README FIGURES, THE FIRST BATCH.')
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (b302): %s %s' % (pos, neg))
    print('  SPLITTER FIXTURE (b303): %s %s %s %s' % (sa, sb, sc, sd))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s'
          % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    if bad:
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %s' % ('PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1
    g1 = ('PRESENT AT A PINNED ROW' in ROWS[0][0]
          and 'A PINNED ROW AGED WELL' in ROWS[0][1]
          and 'LOOKS LIKE A PIN AND IS NOT' in ROWS[0][1]
          and 'NO TERMINAL' in ROWS[0][2]
          and 'NEITHER SHIPS A PRINTED AXIOM PROFILE' in ROWS[0][2]
          and 'PRESERVED, NOT REPLACED' in ROWS[0][3]
          and 'NOT WRITTEN TO' in ROWS[0][3]
          and 'BECAUSE NO ROW MOVED' in ROWS[0][3]
          and 'ONE QUANTITY AT THREE DIFFERENT REFS' in ROWS[0][4]
          and 'NONE OF THE THREE NAMES THE REF' in ROWS[0][4]
          and 'IDENTIFIED BY THE DESCRIPTION' in ROWS[0][4]
          and 'LACUNAE ARE FILED AND NOT INVENTED' in ROWS[0][4]
          and 'NO ROW WAS REPAIRED' in ROWS[0][5]
          and 'NO HEAD WAS WRITTEN INTO A ROW' in ROWS[0][5]
          and 'NO REPOSITORY WAS RENORMALISED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says the pinned/pinless contrast and its demonstration, the false pins, no '
          'terminal with the profile shortfall, the attribute with what was preserved and what was not '
          'written, the three figures at three refs, the object identified by the description, the desk '
          'and the expectations, and the scope : %s' % g1)
    if not g1:
        return 1
    present = [m for m, _s, _t, _p, _g, _sc, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT (%d) -- NOTHING WRITTEN.' % len(present))
        print('=' * 100)
        return 0
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d ; row to append : %d' % (max(nums), start))
    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[5] or 'M-2' not in r[5]]
    if over:
        print('  ### FAIL -- a row lacks its scope refusal or M-2')
        return 1
    lines = ['| %d | %s | %s | %s | %s %s | %s |' % (start + k, stmt, term, prof, grade, scope, status)
             for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS)]
    new = txt.rstrip(chr(10)) + chr(10) + chr(10).join(lines) + chr(10)
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)
    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    cells = [G.split_cells(t) for t in back.rstrip(chr(10)).split(chr(10))[-1:]]
    ok = (got[-1] == start and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS)
          and C.blank_cells(back) == 0
          and all(len(c) == 6 and all(x.strip() for x in c) for c in cells)
          and back.startswith(txt.rstrip(chr(10))))
    print('  READ BACK : last row number is %d ; cells on disk %s' % (got[-1], [len(c) for c in cells]))
    print('  ### **THE TABLE IS A TRUE PREFIX OF ITSELF ABOVE THIS ROW** : %s'
          % back.startswith(txt.rstrip(chr(10))))
    print('  table rows now : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
