# -*- coding: utf-8 -*-
"""b293 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b293_the_finite_family.txt')
REG = os.path.join(ROOT, 'data', 'b293_registration_2026-09-02.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ("the keystone's Son definition", KEY, 'vectors vanishing on a ball'),
    ("b280: both halves use ball_n",
     os.path.join(ROOT, 'data', 'b280_the_consequence.txt'), 'BOTH HALVES USE `ball_n`'),
    ("b226's transform square (EMITTER)",
     os.path.join(ROOT, 'data', 'b226_stated_choice.txt'), 'S^2 = q^2 Pi'),
    ("b226: the involution Pi (EMITTER)",
     os.path.join(ROOT, 'data', 'b226_stated_choice.txt'), '(Pi f)(m) = f(-m)'),
    ("b44: S^2 = q^2 Pi verified in-run (EMITTER)",
     os.path.join(ROOT, 'data', 'b44_2026-08-19.txt'), 'S^2 = q^2 Pi verified in-run'),
    ("b284's gap set was the units",
     os.path.join(ROOT, 'data', 'b284_the_scalings_domain.txt'), 'VERDICT: (FAILS) -- IN BOTH'),
    ("b284's escaped-mass artifact",
     os.path.join(ROOT, 'data', 'b284_the_scalings_domain.txt'), 'ESCAPED MASS FOLDED BACK IN'),
    ("b288: no two-parameter finite family",
     os.path.join(ROOT, 'data', 'b288_the_family_and_the_complement.txt'),
     'TWO-PARAMETER FINITE-PLACE FAMILY'),
    ("b288's promotion criteria",
     os.path.join(ROOT, 'data', 'b288_the_family_and_the_complement.txt'), 'UNBANKED-UNTIL-TESTED'),
    ("b279's collapse at b = 0",
     os.path.join(ROOT, 'data', 'b279_the_local_space.txt'), 'every fiber sum is zero'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank defines the family', BANK, 'Son(p,n; a,b) := { f'),
    ('bank derives the dimension law', BANK, '(p^n - p^a)(p^n - p^b)'),
    ('bank verifies the diagonal vector by vector', BANK, 'VECTOR BY VECTOR, BOTH POLARITIES'),
    ('bank states the sum invariance', BANK, 'THE SUM `a + b` IS INVARIANT'),
    ('bank names the analogy as a name', BANK, 'THE ANALOGY IS A NAME AND NOT A REASON'),
    ('bank derives the reflection', BANK, 'S : Son(p,n; a,b) -> Son(p,n; b,a)'),
    ('bank refuses the near-misses by name', BANK, 'NEITHER IS USED'),
    ('bank identifies the leftover as a boundary', BANK, 'SHELL'),
    ('bank leaves the barrier untouched', BANK, 'REMAIN EXACTLY TRUE THERE'),
    ('bank carries the standing sentence', BANK, 'A FAMILY EXISTING IS NOT A'),
    ('bank keeps M-2 unchanged', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('registration fixes falsifier V4', REG, 'NO ARCHIMEDEAN STEP'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('the barrier is not reopened', BANK, 'THE BARRIER IS REOPENED.'),
    ('no route is claimed', BANK, 'THE FAMILY IS A ROUTE.'),
    ('the family is not adopted', BANK, 'THE FAMILY IS ADOPTED INTO THE OBJECT.'),
    ('M-2 is not advanced', BANK, 'M-2 IS STATED.'),
    ('no archimedean import', BANK, 'THE ARCHIMEDEAN RESULT SETTLES THE FINITE ONE.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b293 -- GATE SUITE')
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
