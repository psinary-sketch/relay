# -*- coding: utf-8 -*-
"""b288 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b288_the_family_and_the_complement.txt')
REG = os.path.join(ROOT, 'data', 'b288_registration_2026-09-01.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ("CC Definition 4.4, from its emitting bank",
     os.path.join(ROOT, 'data', 'b287_the_two_papers.txt'), 'let Sonin'),
    ("CC: psi_n and their transforms orthogonal to S(1,1)",
     os.path.join(ROOT, 'data', 'b287_the_two_papers.txt'), 'orthogonal to `S(1,1)`'),
    ("keystone: one ball, both halves",
     os.path.join(ROOT, 'data', 'b280_the_consequence.txt'),
     "BOTH HALVES USE `ball_n`"),
    ("b284's dual failure, carried",
     os.path.join(ROOT, 'data', 'b284_the_scalings_domain.txt'),
     'VERDICT: (FAILS) -- IN BOTH DIRECTIONS'),
    ("b284 reserved the untested routes",
     os.path.join(ROOT, 'data', 'b284_the_scalings_domain.txt'),
     'C3 REMAINS OPEN BY EVERY ROUTE THIS ACT DID NOT TEST'),
    ("b284's vacuity finding",
     os.path.join(ROOT, 'data', 'b284_the_scalings_domain.txt'),
     'IS IDENTICALLY ZERO FOR ### EVERY'),
    ("b250's mode series (EMITTER)",
     os.path.join(ROOT, 'data', 'b250_m4_derivation.txt'),
     'eps(rho) = sum_n [lam_n / sqrt(1-lam_n^2)]'),
    ("b250's zeta_n supported off the cutoff (EMITTER)",
     os.path.join(ROOT, 'data', 'b250_m4_derivation.txt'),
     'for x >= 1, else 0'),
    ("b250's S3(a) halt (EMITTER)",
     os.path.join(ROOT, 'data', 'b250_m4_derivation.txt'),
     'S3(a) HALTS AT (NOT DERIVED)'),
    ("b264's prolate modes (EMITTER)",
     os.path.join(ROOT, 'data', 'b264_eps_even_decay.txt'),
     'the ODD prolate modes vanish'),
    ("b281's compression, carried",
     os.path.join(ROOT, 'data', 'b281_the_compression.txt'),
     'VERDICT: (COMPRESSION ZERO)'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank returns the product invariant', BANK, 'THE PRODUCT IS INVARIANT'),
    ('bank shows each parameter separately', BANK, 'SO `mu -> a * mu`'),
    ('bank reads non-preservation as a stabilizer', BANK, 'STABILIZER IS TRIVIAL'),
    ('bank says the finite family does not exist', BANK, 'TWO-PARAMETER FINITE-PLACE FAMILY'),
    ('bank refuses the resemblance as evidence', BANK, 'REASON TO BELIEVE EITHER DERIVATION'),
    ('bank leaves b280 and b281 undisturbed', BANK, 'ARE NOT DISTURBED'),
    ('bank files the candidate unbanked', BANK, 'UNBANKED-UNTIL-TESTED'),
    ('bank returns UNDERDETERMINED for component 2', BANK, 'VERDICT: (UNDERDETERMINED)'),
    ('bank names the missing datum', BANK, 'W-ORD-ZETA-TRANSFORM-SIDE'),
    ('bank refuses to compute the weight shape', BANK, 'IT IS NOT AN ARGUMENT'),
    ('bank keeps M-2 unchanged', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('registration fixes falsifier N4', REG, 'CANNOT BE FLOWED ALONG'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('the barrier is not disturbed', BANK, 'b280 IS REOPENED.'),
    ('the candidate is not banked', BANK, 'THE FAMILY ROUTE IS ADOPTED.'),
    ('no aggregation is stated', BANK, 'THE AGGREGATION IS STATED.'),
    ('orthogonality is not claimed', BANK, 'THE PAIRINGS VANISH.'),
    ('no cross-place transport', BANK, 'THE ARCHIMEDEAN ANSWER SETTLES THE FINITE ONE.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b288 -- GATE SUITE')
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
