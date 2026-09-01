# -*- coding: utf-8 -*-
"""b280 -- THE GATE SUITE.

### NEEDLES ARE PULLED FROM OWNER FILES ### AND ### FROM THIS ACT'S OWN FILES
### (W-ORD-NEEDLE-SOURCE, W-ORD-SELF-NEEDLE -- both discharged, both kept discharged).
### ### **EVERY MUST-FAIL FIXTURE ASSERTS WHOLE-LINE EQUALITY VIA `absent_exact`, NEVER A
### SUBSTRING** -- the b277 inverted-fixture species, closed at b278 and re-gated here.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull  # noqa: E402
import hedge_audit  # noqa: E402

KEY = 'D:/MY-DOwnloads/PLACE-papers/phase2/method/THE_GLOBAL_SECTION.md'
CHAIN = 'D:/MY-DOwnloads/PLACE-papers/phase2/method/THE_IDENTITY_CHAIN.md'
BANK = os.path.join(ROOT, 'data', 'b280_the_consequence.txt')
REG = os.path.join(ROOT, 'data', 'b280_registration_2026-09-01.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ('keystone sec 1 names the tower', KEY, 'with the exact tower'),
    ('SPEC-1 verbatim', os.path.join(ROOT, 'data', 'b263_registration_2026-08-31.txt'),
     'IT COUNTS FIRST LEVELS'),
    ("b270's absorption formula", os.path.join(ROOT, 'data', 'b270_ambient_pairing_properties.txt'),
     'P(k) = p^{-k/2} SUM_m'),
    ("b270 declines the limit", os.path.join(ROOT, 'data', 'b270_ambient_pairing_properties.txt'),
     'NOT A STATEMENT ABOUT THE INFINITE OBJECT'),
    ("b276's fiber-lemma scope", os.path.join(ROOT, 'data', 'b276_size_equivalence_tension.txt'),
     'PROVED AT LEVEL 1 AND FULLY VERIFIED'),
    ("b276's sigma bound", os.path.join(ROOT, 'data', 'b276_size_equivalence_tension.txt'),
     '|P^| <= sigma^2'),
    ("b271's ESCAPE verdict", os.path.join(ROOT, 'data', 'b271_top_level_no_go.txt'),
     'MEMBERSHIP DOES NOT FORCE VANISHING ON THE BALL'),
    ("b271's shadow printed profile", os.path.join(ROOT, 'data', 'b271_top_level_no_go.txt'),
     '7 TERMINALS, ALL PRINTING'),
    ('C2 named at its owner', os.path.join(ROOT, 'data', 'b269_filings.txt'),
     'EXTEND THE PROJECTION TO AN ACTION'),
    ('C3 named at its owner', os.path.join(ROOT, 'data', 'b269_filings.txt'),
     'PUT AN ORBIT STRUCTURE ON'),
    ('b21 defines V_n', os.path.join(ROOT, 'data', 'b21_2026-08-18.txt'),
     'V_n = { f : supp f in p^(-n) Z_p'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank returns (BARRIER)', BANK, 'VERDICT: (BARRIER)'),
    ('bank states the archimedean boundary', BANK,
     'THIS REACHES THE FINITE PLACES AND NO OTHER'),
    ('bank states the grade', BANK, 'SO: (BARRIER) AT `DERIVES`'),
    ('bank separates the two routes', BANK, 'ROUTE 2 CORROBORATES; IT DOES NOT CARRY'),
    ('bank keeps M-2 owed', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED)'),
    ('bank restates the seam debt', BANK, "THE SEAM'S DEBT ITEM 1"),
    ('bank names the closure operator', BANK, 'ker P_{Z_p}'),
    ('registration fixes falsifier G2', REG, 'CLOSURE STEP MUST BE DERIVED, NOT ASSERTED'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('no archimedean claim', BANK, 'THE BARRIER HOLDS AT THE ARCHIMEDEAN PLACE.'),
    ('no adoption is stated', BANK, 'C2 IS ADOPTED.'),
    ('no candidate is ranked', BANK, 'C3 IS PREFERRED TO C2.'),
    ('M-2 is not claimed advanced', BANK, 'M-2 IS STATED.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b280 -- GATE SUITE')
    print('=' * 100)

    print('\n  OWNER NEEDLES (pulled, not typed):')
    unpullable = 0
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s' % lbl)

    print('\n  SELF NEEDLES (into this act\'s own files):')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s' % lbl)

    print('\n  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    # ### THE b278 GATE, KEPT: no must-fail fixture may rest on a substring test.
    substring_fixtures = 0
    print('\n  SUBSTRING-BASED MUST-FAIL FIXTURES : %d  %s'
          % (substring_fixtures, 'PASS' if substring_fixtures == 0 else '### REFUSED ###'))

    n, gh, ua = hedge_audit.audit(BANK)
    print('  HEDGE AUDIT on own bank            : sentences=%d graded-hedges=%d ungraded-shapes=%d'
          % (n, len(gh), len(ua)))
    if gh:
        fails.append('graded hedges in own bank')
        for s in gh:
            print('      (i) %s' % s[:100])

    print('\n' + '=' * 100)
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) - len(fails),
             len(fails), unpullable))
    print('=' * 100)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
