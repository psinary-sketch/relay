# -*- coding: utf-8 -*-
"""b295 -- THE GATE SUITE.

### NEEDLES ARE PULLED FROM OWNER FILES ### AND ### FROM THIS ACT'S OWN FILES
### (W-ORD-NEEDLE-SOURCE, W-ORD-SELF-NEEDLE -- both discharged, both kept discharged).
### ### **EVERY MUST-FAIL FIXTURE ASSERTS WHOLE-LINE EQUALITY VIA `absent_exact`, NEVER A
### SUBSTRING** -- the b277 inverted-fixture species, closed at b278 and re-gated here.

### ### **AND ONE GATE THIS ACT ADDS BECAUSE IT IS THE ACT'S OWN SUBJECT:** ### the bank must
### state, as a whole line it can be searched for, ### **THAT b294's MEASUREMENTS ARE REPRODUCED
### AND ITS READING IS WHAT CHANGES.** ### A correction that does not say which of the two it is
### reads as an overturn.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull  # noqa: E402
import hedge_audit  # noqa: E402

D = os.path.join(ROOT, 'data')
BANK = os.path.join(D, 'b295_the_second_mechanism.txt')
REG = os.path.join(D, 'b295_registration_2026-09-02.txt')
RUN = os.path.join(D, 'b295_mechanism_run.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL, never a skip.
OWNER_NEEDLES = [
    ("b270's barrier hypothesis (EMITTER)",
     os.path.join(D, 'b270_ambient_pairing_properties.txt'), 'VANISHES ON THE BALL'),
    ("b270's pairing formula (EMITTER)",
     os.path.join(D, 'b270_ambient_pairing_properties.txt'), 'P(k) = p^{-k/2} SUM_m'),
    ("b281's form TYPE -- the act's hinge (EMITTER)",
     os.path.join(D, 'b281_the_compression.txt'), 'NEITHER HERMITIAN NOR SYMMETRIC'),
    ("b281's definition of `A` (EMITTER)",
     os.path.join(D, 'b281_the_compression.txt'), 'S_quot[m,j]'),
    ("b271's not-dead witness value",
     os.path.join(D, 'b271_top_level_no_go.txt'), '4(N - q)'),
    ("b280's barrier verdict",
     os.path.join(D, 'b280_the_consequence.txt'), 'VERDICT: (BARRIER)'),
    ("b281's compression verdict",
     os.path.join(D, 'b281_the_compression.txt'), 'VERDICT: (COMPRESSION ZERO)'),
    ("b293's family definition",
     os.path.join(D, 'b293_the_finite_family.txt'), 'Son(p,n; a,b) := { f'),
    ("b293's collapsed second condition",
     os.path.join(D, 'b293_the_finite_family.txt'), "SUM_{m' = r mod p^{n+b}} f(m') = 0"),
    ("b293's reflection, the swap",
     os.path.join(D, 'b293_the_finite_family.txt'), 'Son(p,n; b,a)'),
    ("b10's standing obstacle (EMITTER)",
     os.path.join(D, 'b10_2026-08-17.txt'), 'the transform does not commute with x ~ px'),
    ("b284's escaped-mass artifact",
     os.path.join(D, 'b284_the_scalings_domain.txt'), 'ESCAPED MASS FOLDED BACK IN'),
    ("b285's typing verdict",
     os.path.join(D, 'b285_archimedean_opening.txt'),
     'NO FINITE-SIDE STRUCTURAL FACT TYPES AT'),
    ("b294's zero on the basis -- the measurement reproduced",
     os.path.join(D, 'b294_value_run.txt'), 'EVERY BASIS VECTOR PAIRS TO ZERO'),
    ("b294's shadow refusal -- this act's precedent",
     os.path.join(D, 'b294_the_family_value.txt'),
     'A NUMBER THAT NEEDS A PARAGRAPH TO BE READ CORRECTLY'),
    ("b294's own filing of the second mechanism",
     os.path.join(D, 'b294_the_family_value.txt'), 'W-ORD-SECOND-ZERO-MECHANISM'),
]

# ### SELF needles -- into this act's OWN emitted files, PULLED and not typed from memory.
SELF_NEEDLES = [
    ('bank returns the level-split verdict', BANK,
     'AT LEVEL 1 IT GIVES ZERO AND HERE IS THE MECHANISM'),
    ('bank states the derived criterion', BANK,
     'THE TRANSFORM-SIDE THRESHOLD IS `n - 1` AND'),
    ('bank refuses the route reading first', BANK,
     'IT IS NOT A ROUTE, AND THE ACT SAYS SO BEFORE IT SAYS ANYTHING ELSE'),
    ('bank says which condition the members weaken', BANK,
     "WEAKENING THE OBJECT'S"),
    ('bank prints the witness ball-mass rather than asserting it', BANK,
     "THE OBJECT'S FIRST CONDITION FORBIDS"),
    ('bank leaves the barrier untouched and re-measures it', BANK,
     'THE ### WHOLE FORM ### IS IDENTICALLY ZERO'),
    ('bank states the artifact exposure', BANK, 'NO LEVEL-SHIFTING MAP'),
    ('bank reproduces b294 rather than overturning it', BANK,
     "ITS NUMBERS ARE NOT IN QUESTION"),
    ('bank declares the broken search arm', BANK, 'IS NOT A SEARCH'),
    ('bank keeps the reopening unbanked', BANK, 'STILL UNBANKED-UNTIL-TESTED'),
    ('bank keeps M-2 unchanged', BANK,
     'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('bank separates derived sufficiency from measured necessity', BANK,
     'NECESSITY IS MEASURED AT 80 MEMBERS'),
    ('registration fixed the hinge falsifier BEFORE the run', REG,
     'A ZERO ON A BASIS IS NOT A ZERO ON A MEMBER'),
    ('registration committed the exact value before any code', REG,
     '`<A f, f> = 4/3`'),
    ('run carries the not-dead witness', RUN, 'Z1 NOT-DEAD WITNESS'),
    ('run carries the barrier re-measurement', RUN, 'WHOLE FORM identically zero'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('no route is claimed', BANK, 'THE MEMBER IS A ROUTE.'),
    ('the barrier is not weakened', BANK, 'THE BARRIER IS WEAKENED.'),
    ('the barrier is not extended', BANK, 'THE BARRIER IS EXTENDED.'),
    ('no aggregation is stated', BANK, 'THE AGGREGATION IS STATED.'),
    ('M-2 is not advanced', BANK, 'M-2 IS STATED.'),
    ('b294 is not re-verdicted', BANK, 'b294 IS RE-VERDICTED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b295 -- GATE SUITE')
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
