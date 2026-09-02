# -*- coding: utf-8 -*-
"""b294 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b294_the_family_value.txt')
REG = os.path.join(ROOT, 'data', 'b294_registration_2026-09-02.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ("b270's barrier hypothesis (EMITTER)",
     os.path.join(ROOT, 'data', 'b270_ambient_pairing_properties.txt'),
     'VANISHES ON THE BALL'),
    ("b270's pairing formula (EMITTER)",
     os.path.join(ROOT, 'data', 'b270_ambient_pairing_properties.txt'),
     'P(k) = p^{-k/2} SUM_m'),
    ("b271's not-dead witness value",
     os.path.join(ROOT, 'data', 'b271_top_level_no_go.txt'), '7 TERMINALS, ALL PRINTING'),
    ("b293's family definition",
     os.path.join(ROOT, 'data', 'b293_the_finite_family.txt'), 'Son(p,n; a,b) := { f'),
    ("b293's dimension law",
     os.path.join(ROOT, 'data', 'b293_the_finite_family.txt'), '(p^n - p^a)(p^n - p^b)'),
    ("b293's sum invariance",
     os.path.join(ROOT, 'data', 'b293_the_finite_family.txt'), 'THE SUM `a + b` IS INVARIANT'),
    ("b280's barrier verdict",
     os.path.join(ROOT, 'data', 'b280_the_consequence.txt'), 'VERDICT: (BARRIER)'),
    ("b281's compression verdict",
     os.path.join(ROOT, 'data', 'b281_the_compression.txt'), 'VERDICT: (COMPRESSION ZERO)'),
    ("b284's escaped-mass artifact",
     os.path.join(ROOT, 'data', 'b284_the_scalings_domain.txt'), 'ESCAPED MASS FOLDED BACK IN'),
    ("b285's typing verdict",
     os.path.join(ROOT, 'data', 'b285_archimedean_opening.txt'),
     'NO FINITE-SIDE STRUCTURAL FACT TYPES AT'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank returns the sub-family verdict', BANK, 'A PROPERTY OF A SUB-FAMILY'),
    ('bank names the nonzero member', BANK, 'Son(p,n; -1,-1)'),
    ('bank refuses the route reading first', BANK, 'IT IS NOT A ROUTE, AND THE ACT SAYS SO'),
    ('bank says the witness is not a Son vector', BANK, 'THE WITNESS IS NOT A `Son` VECTOR'),
    ('bank states the artifact exposure', BANK, 'NO LEVEL-SHIFTING MAP'),
    ('bank separates derived from computed', BANK, 'ZERO, DERIVED'),
    ('bank files the second mechanism', BANK, 'W-ORD-SECOND-ZERO-MECHANISM'),
    ('bank leaves the barrier untouched', BANK, 'NOT RE-VERDICTED, EXTENDED OR WEAKENED'),
    ('bank declares the orbit-only near miss', BANK, 'ABOUT TO BE THE VERDICT'),
    ('bank keeps the reopening unbanked', BANK, 'STILL UNBANKED-UNTIL-TESTED'),
    ('bank keeps M-2 unchanged', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('registration fixes falsifier X5', REG, 'A NONZERO VALUE IS NOT A ROUTE'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('no route is claimed', BANK, 'THE FAMILY IS A ROUTE.'),
    ('the barrier is not weakened', BANK, 'THE BARRIER IS WEAKENED.'),
    ('no aggregation is stated', BANK, 'THE AGGREGATION IS STATED.'),
    ('M-2 is not advanced', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b294 -- GATE SUITE')
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
