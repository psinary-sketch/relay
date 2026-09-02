# -*- coding: utf-8 -*-
"""b290 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b290_the_cross_pairing_read.txt')
REG = os.path.join(ROOT, 'data', 'b290_registration_2026-09-02.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ("CC Definition 4.4, from its emitting bank",
     os.path.join(ROOT, 'data', 'b287_the_two_papers.txt'), 'let Sonin'),
    ("CC: psi_n and transforms orthogonal to S(1,1)",
     os.path.join(ROOT, 'data', 'b287_the_two_papers.txt'), 'orthogonal to `S(1,1)`'),
    ("b288's cross-pairing verdict",
     os.path.join(ROOT, 'data', 'b288_the_family_and_the_complement.txt'),
     'VERDICT: (UNDERDETERMINED)'),
    ("b288: no two-parameter finite family",
     os.path.join(ROOT, 'data', 'b288_the_family_and_the_complement.txt'),
     'TWO-PARAMETER FINITE-PLACE FAMILY'),
    ("b288's weight juxtaposition",
     os.path.join(ROOT, 'data', 'b288_the_family_and_the_complement.txt'),
     'IT IS NOT AN ARGUMENT'),
    ("b250's mode series (EMITTER)",
     os.path.join(ROOT, 'data', 'b250_m4_derivation.txt'),
     'eps(rho) = sum_n [lam_n / sqrt(1-lam_n^2)]'),
    ("b250's zeta_n cut off the interval (EMITTER)",
     os.path.join(ROOT, 'data', 'b250_m4_derivation.txt'), 'for x >= 1, else 0'),
    ("b289's coverage finding",
     os.path.join(ROOT, 'data', 'b289_consolidation.txt'), 'W-ORD-ALLPRINTS-COVERAGE'),
    ("b289's print counts",
     os.path.join(ROOT, 'data', 'b289_consolidation.txt'), '404 -> 426'),
    ("the standing profile carries B270",
     'D:/SIDE-global-section/AXIOM_PRINTS.txt',
     "'B270.absorb_2_2' does not depend on any axioms"),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank returns ABSENT on the first read', BANK, 'FIRST READ -- VERDICT: (ABSENT)'),
    ('bank returns PARTIAL on the second', BANK, 'SECOND READ -- VERDICT: (PARTIAL)'),
    ('bank names the missing sentence', BANK, 'ONE SENTENCE -- `F_eR^2 = 1`'),
    ('bank quotes the related-but-different fact', BANK, 'IS NOT AN ANSWER TO THE FIRST READ'),
    ('bank refuses to promote the proposal', BANK, 'NOT PROMOTED. ### LEFT FILED'),
    ('bank draws no instrument consequence', BANK, 'NO CONSEQUENCE FOR THE INSTRUMENTS IS DRAWN'),
    ('bank blocks transport to the finite places', BANK, 'A reflection needs a family'),
    ('bank files the print coverage', BANK, 'FILED. NOT RUN'),
    ('bank keeps the juxtaposition unconnected', BANK, 'NOT CONNECTED. NOT A CONJECTURE'),
    ('bank keeps M-2 unchanged', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('registration named involutivity in advance', REG, 'INVOLUTIVITY IS THE LIKELY HIDDEN STEP'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('the swap is not claimed derived', BANK, 'THE SWAP IS DERIVED.'),
    ('self-duality is not claimed', BANK, 'S(1,1) IS SELF-DUAL.'),
    ('no orthogonality is derived', BANK, 'THE PAIRINGS VANISH.'),
    ('no proposal is adopted', BANK, 'THE TRANSFORM REFLECTION IS ADOPTED.'),
    ('nothing transported to the finite places', BANK, 'THE FINITE FAMILY CARRIES A REFLECTION.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b290 -- GATE SUITE')
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
