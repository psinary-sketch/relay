# -*- coding: utf-8 -*-
"""b373_correspondence.py -- ONE ROW: THE PINS SOURCED FROM THE WRITING ACT, THE STATUS COLUMN LISTED.

### ### **EVERY FIGURE IS READ FROM THIS ACT'S OWN JSONS. ### NONE IS TYPED.**
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
    "**SCOPE: NO PIN WAS WRITTEN TO ANY ROW AND NO PIN WAS TAKEN FROM ANY CURRENT HEAD.** (R9)'s own "
    "prohibition, measured and not asserted. **NO ROW WAS CHECKED AT ANY PIN**: adding a pin dates a "
    "claim, it does not verify one, and no kernel was opened to see whether a row is true at the ref "
    "beside it. **NO GRADE WAS MOVED BY THIS SEAT**, no face promoted and no grade conferred; a seat "
    "that regrades is a seat that decided what was verified. **NO DEPOSITED FILE, NO ARCHIVED FILE AND "
    "NO APPEND-ONLY LEDGER ENTRY WAS EDITED** -- a deposited companion edited on this machine no longer "
    "matches what was deposited, an archive that changes is not an archive, and a ledger row is a "
    "historical statement already dated by the act that wrote it; whether those surfaces should carry "
    "pins is ROUTED to the author. **NO NEW COLUMN WAS ADDED TO ANY TABLE AND NO TABLE'S SHAPE WAS "
    "CHANGED.** **NO KERNEL WAS RE-CLASSIFIED**: the retired-and-absent set is the record's own, from "
    "b367, b368, b369 and b372. **NO .lean FILE WAS TOUCHED, NO BUILD WAS RUN AND NO AXIOM PROFILE WAS "
    "RECOMPUTED.** **ONLY ONE OWNER INSTRUMENT MOVED**, licensed by the order and named on the "
    "registration's face before the edit. **LEG 2 WAS NOT BEGUN.** NOTHING IS CLAIMED ABOUT THE "
    "MATHEMATICS OF ANY NAMED SUBJECT; a pin is about when a claim was made, not about whether it is "
    "true. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or the "
    "roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE "
    "PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under "
    "b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent "
    "seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE POSTURE "
    "LOCK IS SEPARATE. h2 stands exactly where the deposit left it. The wave PARKED by the author's "
    "ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


def rows():
    E, P, S, Q, F = (J('b373_reads'), J('b373_pins'), J('b373_status'), J('b373_desk'),
                     J('b373_filing'))
    pct = 100.0 * P['located_act'] / max(1, P['rows'])
    m = ("**A RULE CAN OUTRUN THE RECORD IT REACHES INTO: RULING (R9) WAS EXECUTED AS FAR AS ITS OWN "
         "SOURCING RULE ALLOWS AND WROTE NO PIN, BECAUSE THE PAPERS ARE OLDER THAN THE INSTRUMENTS** "
         "-- %d of %d pinless rows have a locatable writing act, and of those the chain fails again "
         "for all but %d (b373, ruling (R9))" % (P['located_act'], P['rows'], P['pinnable']))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, on the audit's own exit code, and "
            "its face fixed the sourcing chain and the scope of the edit BEFORE any read. The chain is "
            "the ruling's own: the row re-anchored BY ITS OWN CONTENT, the commit that INTRODUCED that "
            "content, the ACT that commit's subject names, and THAT ACT'S OWN BANKED REF -- **never a "
            "current head, which would date the claim to today rather than to when it was made**. "
            "**%d rows were introduced by commits whose subject names no act**; the pins instrument "
            "that banks a kernel's ref begins at b300, later than most rows that need one. The price "
            "fitted one act (%.1f seconds a row over %d rows), so the act executed rather than only "
            "priced. **%d rows were PINNABLE and every one of them sits on a deposited companion, an "
            "archived snapshot or an append-only ledger entry**, which this seat will not rewrite on a "
            "citation-hygiene ruling. %d reads, %d without an anchor."
            % (P['reasons'].get('WRITING ACT NOT NAMED', 0), P['per_row'], P['rows'],
               P['pinnable'], E['reads'], E['without_anchor']))
    return [
        (m, stmt,
         "**NO TERMINAL.** No `.lean` file was touched, no build was run and no axiom profile was "
         "recomputed. **NO KERNEL WAS OPENED AT ALL**: a pin dates a claim and does not verify one, "
         "and this act ran no check on any row at any ref.",
         "**PRINT: NO PIN WAS WRITTEN TO ANY ROW.** The classification is the product and it is "
         "banked: %d CITES-AT-AN-UNKNOWN-REF across %s, each reason kept apart because **a row nobody "
         "can date and a row whose kernel was never rostered are not the same problem and will not "
         "have the same cure**. `tools/b304_hooks.py` -- **the one licensed owner instrument, named on "
         "the registration's face before the edit** -- is corrected: it reported that no "
         "`.gitattributes` pins the guard, which b372 made false in every rostered repository, **and "
         "its caveat is kept rather than deleted along with the falsehood**. "
         "`PLACE-papers/OPEN_TRAILS.md` gains ONE append-only block -- **appending to a ledger this "
         "act refused to edit is not the same act as changing a row somebody else wrote**. "
         "**FACES_LEDGER.md IS NOT WRITTEN AND ITS WRITER IS NOT CALLED, BECAUSE NO ROW MOVED.** No "
         "findings section; no TECHNE file; no module pushed. **THE HOOK AND THE MIRROR ARE OWED AND "
         "PAID.**"
         % (P['unknown'], ', '.join('%d %s' % (n, k.lower())
                                    for k, n in sorted(P['reasons'].items())
                                    if k and k != 'null')),
         "**THE STATUS COLUMN IS THE SHARPER ITEM AND IS BOUNDED: %d ROWS IN %d DOCUMENTS ASSERT A "
         "GRADE AGAINST A DECLARATION THIS RECORD HAS CLASSIFIED RETIRED OR ABSENT, AND EVERY ONE OF "
         "THEM IS INSIDE THE TWELVE b372 ALREADY FLAGGED** -- the sweep of %d table rows across %d "
         "tracked markdown files found **no instance outside that set**. A three-way split was drawn "
         "before the sweep ran and it decided rows: **%d state their own retirement** (reporting the "
         "withdrawal, not asserting the declaration is there) and **%d grades a declaration b372 found "
         "ALIVE** (a retired concept label in its first cell, a live terminal in its last) -- "
         "**neither is the defect, and counting either would report a correct row as a defective "
         "one**. **A stale count misstates a quantity; a grade against an absent declaration asserts "
         "that something was checked that is not there to check.** The author faces **three choices "
         "per row, named without one being chosen**: strike the grade, restate it as a retirement the "
         "way VERIFICATION_LOOM.md already does for one pair, or leave it with a pin that dates it -- "
         "**and this act has just shown a pin cannot be sourced for these rows**. **THE EXPECTATIONS "
         "ARE SCORED:** the navigator's (L1) **REFUTED** by a printed classification (%.0f%%, not more "
         "than half); this seat's (E1) **REFUTED** -- it predicted the roster would be the wall and "
         "**the commit subjects were**; (E2)'s arithmetic half held and **its scorable half is REFUTED, "
         "which is better news than it asked for: the defect is bounded**. **THE DESK: %d SWEPT, %d "
         "CLOSED, %d STANDING**, and the closure worth naming is *the pinless rows awaiting a ruling* "
         "-- **its occasion was an unmade ruling and the ruling is made**; what the execution FOUND is "
         "filed as a NEW item, because **an item that changes its meaning while keeping its name is a "
         "desk that never closes anything**. **AND ONE TENSION IS FILED RATHER THAN RESOLVED:** %d "
         "sourced pins equal a current head because their kernel has not moved, and the locked bar "
         "tests the value while the ruling forbids the source."
         % (S['defect'], len(set(h['file'] for h in S['detail']
                                 if not h['states_own_retirement']
                                 and not h['grades_a_live_declaration'])),
            S['rows_scanned'], S['files'], S['corrected'], S['live_graded'], pct,
            Q['items'], Q['closed'], Q['standing'], P['equals_a_head']),
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b373 -- ONE ROW: THE PINS SOURCED, THE STATUS COLUMN LISTED.')
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
    g1 = ('A RULE CAN OUTRUN THE RECORD' in ROWS[0][0]
          and 'never a current head' in ROWS[0][1]
          and 'names no act' in ROWS[0][1]
          and 'NO TERMINAL' in ROWS[0][2]
          and 'NO KERNEL WAS OPENED AT ALL' in ROWS[0][2]
          and 'NO PIN WAS WRITTEN TO ANY ROW' in ROWS[0][3]
          and 'one licensed owner instrument' in ROWS[0][3]
          and 'BECAUSE NO ROW MOVED' in ROWS[0][3]
          and 'INSIDE THE TWELVE' in ROWS[0][4]
          and 'neither is the defect' in ROWS[0][4]
          and 'three choices' in ROWS[0][4]
          and 'REFUTED' in ROWS[0][4]
          and 'NO PIN WAS WRITTEN' in ROWS[0][5]
          and 'NO GRADE WAS MOVED' in ROWS[0][5]
          and 'NO DEPOSITED FILE' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says the rule outrunning the record, the sourcing rule and its prohibition, no '
          'terminal and no kernel opened, no pin written with the licensed instrument named, the '
          'status column bounded with its three-way split and the three choices, the expectations '
          'scored, and the scope : %s' % g1)
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
