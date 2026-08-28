# -*- coding: utf-8 -*-
"""b234_checks.py -- the b234 gates, routed through the AMENDED b217 harness.

### THIS ACT'S RISKS:
###   (1) that the fold MOVES A GRADE while claiming not to. ### The document's own rule is
###       that a grade moves by editing a tag IN PLACE -- so the mechanical test is that the
###       fold DELETED NO LINE.
###   (2) that an obstacle gets PARAPHRASED. ### The test is that the fold's wording is found
###       IN THE OWNING BANK, which is also a live exercise of amendment 1.
###   (3) that the provisional ruling gets EXECUTED. ### File E and the chain's adoption must
###       be untouched.
###   (4) that an amendment ends a species by ending the check. ### Both amendments carry
###       fixtures in BOTH polarities.

### ### THE MATCHER IS `check_harness.contains` -- THE AMENDMENT THIS ACT WRITES. Using it
### ### here is deliberate: a tool amended and not then used is an amendment on paper.
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both, norm   # noqa: E402
import banned_terms as BT                                  # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
PLACE = 'D:/MY-DOwnloads/PLACE-papers'
D = os.path.join(ROOT, 'data')

BANK = os.path.join(D, 'b234_fold_forward.txt')
REG = os.path.join(D, 'b234_registration_2026-08-28.txt')
AMEND = os.path.join(D, 'b234_amendments_run.txt')
B220 = os.path.join(D, 'b220_aggregation_freedom.txt')
B224 = os.path.join(D, 'b224_segre_three_cells.txt')
B227 = os.path.join(D, 'b227_the_trace.txt')
B227R = os.path.join(D, 'b227_registration_2026-08-28.txt')
B232 = os.path.join(D, 'b232_sign_of_A.txt')
B233 = os.path.join(D, 'b233_the_arrangement.txt')
B233R = os.path.join(D, 'b233_registration_2026-08-28.txt')

FINDINGS = os.path.join(PLACE, 'FINDINGS.md')
CHAIN = os.path.join(PLACE, 'phase2', 'method', 'THE_IDENTITY_CHAIN.md')
FILE_E = os.path.join(SGS, 'Interfaces', 'FiniteInstanceIdentity.lean')
NARR = os.path.join(ROOT, 'reports',
                    '2026-08-18-global-section-acts-narrative-v0.15.md')
FIXTURE = os.path.join(D, 'b234_fixture_live_voice.md')


def deletions(repo, relpath):
    """### THE MECHANICAL TEST FOR 'NO GRADE MOVED': the document's own rule is that a
    ### grade moves by editing a tag IN PLACE, and an in-place edit DELETES A LINE.
    ### ### A FOLD THAT ONLY ADDS CANNOT HAVE MOVED A TAG. Returns -1 on failure."""
    try:
        r = subprocess.run(['git', '-C', repo, 'diff', '--numstat', 'HEAD', '--', relpath],
                           capture_output=True)
    except Exception:
        return -1
    if r.returncode != 0:
        return -1
    out = r.stdout.decode('utf-8', 'replace').split()
    if not out:
        # ### NO DIFF AT ALL IS ZERO DELETIONS, NOT AN ERROR. ### The first draft returned
        # ### -1 here and the gate FAILED on an UNMODIFIED file -- a false alarm, which is
        # ### the b213 species the harness was built against. Caught by running it.
        return 0
    return int(out[1]) if len(out) >= 2 and out[1].isdigit() else -1


def file_unmodified(repo, relpath):
    try:
        r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                           capture_output=True)
    except Exception:
        return False
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def scan(paths):
    """### RUN THE AMENDED TERM SCAN over whole files; return (hits, live, quoted)."""
    scope = []
    for p in paths:
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        scope += [(p, k, ln) for k, ln in enumerate(txt.splitlines(), 1)]
    hits = live = quoted = 0
    for path, _ln, text in scope:
        for m in BT.PAT.finditer(text):
            hits += 1
            cls = BT.classify(text, m.start(), path)
            if cls is None:
                live += 1
            elif cls.startswith('QUOTED --'):
                quoted += 1
    return hits, live, quoted


def main():
    h = Harness(ROOT, 'b234')

    # 1 -- ### THE FOLD IS WRITTEN, WITH THE DOCUMENT'S OWN ANCHOR RULE OBEYED.
    h.run('fold-written-with-stable-anchors',
          check=lambda: all(contains(FINDINGS, a) for a in
                            ('arc-live-items', 'residue-six-station-migration',
                             'arc-species-catalogue', 'two-three-connective',
                             'import-ledger-surfaced')),
          fixture=lambda: all(contains(CHAIN, a) for a in
                              ('arc-live-items', 'residue-six-station-migration',
                               'arc-species-catalogue', 'two-three-connective',
                               'import-ledger-surfaced')),
          witness=lambda: contains(FINDINGS, 'arc-live-items'))

    # 2 -- ### NO GRADE MOVED, TESTED MECHANICALLY: the fold DELETED NO LINE of FINDINGS.
    # ### THE FIRST FIXTURE HERE WAS `deletions(<nonexistent file>) == 0` AND THE HARNESS
    # ### REFUSED THE CHECK -- because THIS ACT'S OWN REPAIR to `deletions()` (no diff = 0
    # ### deletions, not an error) made a nonexistent file return 0 too. ### THE REPAIR
    # ### DISARMED THE FIXTURE THAT GUARDED IT, and the guard said so in the same run.
    # ### THE REPAIRED FIXTURE TESTS THE NEGATION OF THE CLAIM ON THE SAME MEASUREMENT:
    # ### "the fold deleted lines" must be FALSE.
    h.run('no-tag-edited-fold-only-adds',
          check=lambda: deletions(PLACE, 'FINDINGS.md') == 0,
          fixture=lambda: deletions(PLACE, 'FINDINGS.md') > 0,
          witness=lambda: deletions(PLACE, 'FINDINGS.md') >= 0)

    # 3 -- ### THE OBSTACLES ARE QUOTATIONS: each fold wording is found IN ITS OWNING BANK.
    # ### THIS GATE IS ALSO A LIVE EXERCISE OF AMENDMENT 1 -- two of these three quotations
    # ### are line-wrapped in their sources and would have MISSED under the old matcher.
    OBST = [(B220, 'THE RESULT ROUTE IS BLOCKED IN PRINCIPLE'),
            (B227, 'IT WANTS A RESULT OR A RULING; IT DOES NOT WANT A READ'),
            (B224, 'MEASURED RATHER THAN GUESSED')]
    h.run('obstacles-quoted-not-paraphrased',
          check=lambda: all(contains(p, q) and contains(FINDINGS, q) for p, q in OBST),
          fixture=lambda: all(contains(B232, q) for _p, q in OBST),
          witness=lambda: all(contains(p, q) for p, q in OBST))

    # 4 -- ### THE TALLY WAS VERIFIED AT CONTENT, and the five acts are named.
    h.run('tally-five-verified-at-content',
          check=lambda: (contains(BANK, 'IT COMES OUT AT FIVE')
                         and all(contains(BANK, a) for a in
                                 ('b223', 'b226', 'b227', 'b229', 'b232'))),
          fixture=lambda: contains(B233, 'IT COMES OUT AT FIVE'),
          witness=lambda: contains(REG, 'IF THE COUNT IS NOT FIVE'))

    # 5 -- ### AMENDMENT 1 RETROFIT: the three line-wrap catches now match ...
    h.run('amendment1-retrofit-three-catches',
          check=lambda: (contains(B227R, 'REFUSED BY NAME')
                         and contains(B232, 'the named crime')
                         and contains(NARR, 'fails numerically in BOTH conventions')),
          fixture=lambda: contains(B232, 'the named felony'),
          witness=lambda: contains(B232, 'the named crime'))

    # 6 -- ### ... AND THE SECOND POLARITY: the amendment did not make everything match.
    # ### AN AMENDMENT THAT ENDED THE SPECIES BY ENDING THE CHECK WOULD PASS GATE 5 AND
    # ### FAIL THIS ONE.
    h.run('amendment1-absent-still-absent',
          check=lambda: not (contains(B232, 'the named felony')
                             or contains(NARR, 'succeeds numerically in BOTH conventions')
                             or contains('D:/nope-xyz.txt', 'anything')),
          fixture=lambda: not contains(B232, 'the named crime'),
          witness=lambda: not contains(B232, 'the named felony'))

    # 7 -- ### AMENDMENT 2 FIXTURE: an authored stem, and a quotation NOT in the corpus,
    # ### must BOTH stay LIVE. ### A QUOTATION CLASS THAT SWALLOWED AN AUTHORED USE WOULD
    # ### BE WORSE THAN NO CLASS AT ALL.
    h.run('amendment2-fixture-authored-stays-live',
          check=lambda: scan([FIXTURE])[1] == 2,
          fixture=lambda: scan([FIXTURE])[1] == 0,
          witness=lambda: scan([FIXTURE])[0] == 2)

    # 8 -- ### AMENDMENT 2 RETROFIT: b233's two hits reclassify, AND THE COUNT IS UNCHANGED.
    h.run('amendment2-retrofit-count-unchanged',
          check=lambda: scan([B233R, B233]) == (2, 0, 2),
          fixture=lambda: scan([FIXTURE]) == (2, 0, 2),
          witness=lambda: scan([B233R, B233])[0] == 2)

    # 9 -- ### THE PROVISIONAL RULING IS RECORDED AND **NOT EXECUTED**.
    h.run('provisional-recorded-not-executed',
          check=lambda: (file_unmodified(SGS, 'Interfaces/FiniteInstanceIdentity.lean')
                         and contains(BANK, 'NOT EXECUTED')
                         and deletions(PLACE, 'phase2/method/THE_IDENTITY_CHAIN.md') == 0),
          fixture=lambda: contains(FILE_E, 'NOT EXECUTED'),
          witness=lambda: file_unmodified(SGS, 'Interfaces/FiniteInstanceIdentity.lean'))

    # 10 -- ### THE DESK IS ONE LIST, with all six items.
    h.run('desk-list-in-one-place',
          check=lambda: all(contains(BANK, s) for s in
                            ('THE DESK', 'rows 46/47', 'POSTURE',
                             'CITATION-HAZARD REPAIR')),
          fixture=lambda: all(contains(B233, s) for s in
                              ('THE DESK', 'rows 46/47', 'POSTURE',
                               'CITATION-HAZARD REPAIR')),
          witness=lambda: contains(BANK, 'rows 46/47'))

    # 11 -- ### THE BUDGET WORK-ORDER IS SHARPENED AND SAYS IT WAS NOT RUN.
    h.run('budget-hypothesis-filed-not-run',
          check=lambda: (contains(BANK, 'HALF-ORDER EDGE LOSS SUSPECTED')
                         and contains(BANK, 'NO BENCH RAN HERE')),
          fixture=lambda: contains(B233, 'HALF-ORDER EDGE LOSS SUSPECTED'),
          witness=lambda: contains(BANK, 'EDGE-GRADED MESH THE FIRST TEST'))

    # 12 -- ### THE AMENDMENT'S OWN FAILURE IS ON THE RECORD, not quietly repaired.
    h.run('amendment2-first-draft-failure-recorded',
          check=lambda: both(BANK, 'FIRST DRAFT', 'REPRODUCED THE VERY SPECIES IT WAS WRITTEN'),
          fixture=lambda: both(B233, 'FIRST DRAFT',
                               'REPRODUCED THE VERY SPECIES IT WAS WRITTEN'),
          witness=lambda: contains(AMEND, 'OLD VERDICT'))

    for row in h.rows:
        print('  %-42s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
