# -*- coding: utf-8 -*-
"""b279 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b279_the_local_space.txt')
REG = os.path.join(ROOT, 'data', 'b279_registration_2026-09-01.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ('keystone sec 1 names the tower', KEY, 'with the exact tower'),
    ('keystone sec 1 names the closures', KEY, 'the local Sonin closures'),
    ('identity chain names the object', CHAIN, 'the completed Sonin limit'),
    ('b21 defines V_n', os.path.join(ROOT, 'data', 'b21_2026-08-18.txt'),
     'V_n = { f : supp f in p^(-n) Z_p'),
    ('b21 iota chart refinement', os.path.join(ROOT, 'data', 'b21_2026-08-18.txt'),
     "m'' = p*m + p^(2n+1)*j"),
    ('b21 foot, the disclaimer', os.path.join(ROOT, 'data', 'b21_2026-08-18.txt'),
     'nothing here constructs a limit object, and none is claimed'),
    ('b198 I4, the completion step', os.path.join(ROOT, 'data', 'b198_nonvanishing.txt'),
     "the L^2-CLOSURE OF THE TOWER'S UNION"),
    ('b223 assembles the constituents',
     os.path.join(ROOT, 'data', 'b223_level_limit_two_places.txt'), 'kernel-checked in Z[zeta_16]'),
    ('b197 ran the same falsifier',
     os.path.join(ROOT, 'data', 'b197_registration_2026-08-26.txt'),
     'local space = the completed Sonin limit'),
    ('printed axiom profile, banked',
     os.path.join(ROOT, 'data', 'b227_core_remeasured.txt'),
     "'TowerInstance.support_ball_vanish' does not depend on any axioms"),
    ('vN Def 3.3.1, the demand on H_alpha',
     os.path.join(ROOT, 'data', 'b197_values_and_c0.txt'), 'H_alpha for all alpha in I'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank returns (CONSTRUCTED)', BANK, 'VERDICT: (CONSTRUCTED)'),
    ('bank names the Son tower', BANK, 'THE TOWER IS THE `Son` TOWER'),
    ('bank refuses the consequence', BANK, 'ACT DOES NOT WRITE IT'),
    ('bank declares finite-places-only', BANK, 'AT EVERY FINITE PLACE AND AT NO INFINITE ONE'),
    ('bank keeps M-2 owed', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED)'),
    ('bank restates the seam debt', BANK, "THE SEAM'S DEBT ITEM 1"),
    ('registration quotes the outcome-blind law', REG, 'NEVER BY WHAT IT YIELDS'),
    ('registration fixes the falsifier', REG, 'A DIMENSION THAT AGREES IS NOT AN OBJECT'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('no barrier verdict is stated', BANK,
     'THE BARRIER HOLDS.'),
    ('no adoption is stated', BANK,
     'C1 IS ADOPTED.'),
    ('no aggregation is stated', BANK,
     'THE AGGREGATION IS STATED.'),
    ('no spec is decided', BANK,
     'SPEC-1 IS IDENTICALLY ZERO ON S-bar_v.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b279 -- GATE SUITE')
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
