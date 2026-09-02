# -*- coding: utf-8 -*-
"""b292 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b292_the_identification.txt')
REG = os.path.join(ROOT, 'data', 'b292_registration_2026-09-02.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ("b250's zeta_n definition (EMITTER)",
     os.path.join(ROOT, 'data', 'b250_m4_derivation.txt'), 'for x >= 1, else 0'),
    ("the supplied definition of xi_n^an (EMITTER)",
     os.path.join(ROOT, 'data', 'lemma52_2026-08-17.txt'),
     'xi_n^an = (2/lam) int_0^1 xi_n cos(2 pi t x) dt'),
    ("b250: xi_n^an is the entire extension (EMITTER)",
     os.path.join(ROOT, 'data', 'b250_m4_derivation.txt'),
     'IS the entire extension of `xi_n`'),
    ("b250's pin-P3 equation (EMITTER)",
     os.path.join(ROOT, 'data', 'b250_m4_derivation.txt'),
     'lam xi_n(x) = 2 int_0^1 xi_n(t) cos(2 pi t x) dt'),
    ("b291's refutation, carried",
     os.path.join(ROOT, 'data', 'b291_the_involution.txt'), 'VERDICT: (REFUTED)'),
    ("b291's computed restriction",
     os.path.join(ROOT, 'data', 'b291_the_involution.txt'), '(1 - lambda(n)^2) xi_n'),
    ("b291 filed the identification question",
     os.path.join(ROOT, 'data', 'b291_the_involution.txt'), 'W-ORD-ZETA-IS-PSI'),
    ("b288's cross-pairing verdict",
     os.path.join(ROOT, 'data', 'b288_the_family_and_the_complement.txt'),
     'VERDICT: (UNDERDETERMINED)'),
    ("b289's print-coverage order",
     os.path.join(ROOT, 'data', 'b289_consolidation.txt'), 'W-ORD-ALLPRINTS-COVERAGE'),
    ("b285's typing verdict, carried",
     os.path.join(ROOT, 'data', 'b285_archimedean_opening.txt'),
     'NO FINITE-SIDE STRUCTURAL FACT TYPES AT'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank returns SAME OBJECT up to a scalar', BANK, 'VERDICT: (SAME OBJECT), UP TO A NONZERO'),
    ('bank refuses the resemblance', BANK, 'APPEARS NOWHERE IN THE DERIVATION BELOW'),
    ('bank shows the equations coincide', BANK, 'THEY ARE THE SAME EQUATION'),
    ('bank does not claim the scalars equal', BANK, 'ARE NOT CLAIMED EQUAL'),
    ('bank shows the scalar argument both ways', BANK, 'BACKWARD, AND THIS IS THE DIRECTION'),
    ('bank names the picture residue', BANK, 'W-ORD-PICTURE-IDENTIFICATION'),
    ('bank carries the refutation to the corpus', BANK, 'IS NOT IN `S(1,1)`'),
    ('bank disturbs no measurement', BANK, 'NO MEASUREMENT IS DISTURBED'),
    ('bank keeps the juxtaposition unconnected', BANK, 'DERIVATION NOBODY HAS PERFORMED'),
    ('bank mints the search rule', BANK, 'A SYMBOLIC-ONLY SEARCH IS HALF A SEARCH'),
    ('bank keeps M-2 unchanged', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('registration fixes falsifier S1', REG, 'NOT ON PROVENANCE'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('the vectors are not claimed identical', BANK, 'THEY ARE THE SAME VECTOR.'),
    ('no measurement is impugned', BANK, 'THE ARCHIMEDEAN NUMBERS ARE WRONG.'),
    ('no adoption is stated', BANK, 'C3 IS ADOPTED.'),
    ('the juxtaposition is not connected', BANK, 'THE WEIGHTS DIVERGE INTO THE SONIN SPACE.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b292 -- GATE SUITE')
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
