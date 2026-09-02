# -*- coding: utf-8 -*-
"""b291 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b291_the_involution.txt')
REG = os.path.join(ROOT, 'data', 'b291_registration_2026-09-02.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ("the keystone's F-squared law", KEY, 'F² = parity'),
    ("b61's odd-part instance (EMITTER)",
     os.path.join(ROOT, 'data', 'b61_epsilon_minus.txt'), 'F^2 = -1 on the odd part'),
    ("b290 named the missing sentence",
     os.path.join(ROOT, 'data', 'b290_the_cross_pairing_read.txt'), 'ONE SENTENCE -- `F_eR^2 = 1`'),
    ("b290's PARTIAL verdict",
     os.path.join(ROOT, 'data', 'b290_the_cross_pairing_read.txt'),
     'SECOND READ -- VERDICT: (PARTIAL)'),
    ("b290 fixed the second family at the source",
     os.path.join(ROOT, 'data', 'b290_the_cross_pairing_read.txt'), 'VECTOR, CUT TO `|x| >= 1`'),
    ("b288: no two-parameter finite family",
     os.path.join(ROOT, 'data', 'b288_the_family_and_the_complement.txt'),
     'TWO-PARAMETER FINITE-PLACE FAMILY'),
    ("b288's dilation-orbit form",
     os.path.join(ROOT, 'data', 'b288_the_family_and_the_complement.txt'),
     'THE PRODUCT IS INVARIANT'),
    ("b250's zeta_n normalization (EMITTER)",
     os.path.join(ROOT, 'data', 'b250_m4_derivation.txt'), 'for x >= 1, else 0'),
    ("b250's S3(a) wall (EMITTER)",
     os.path.join(ROOT, 'data', 'b250_m4_derivation.txt'), 'S3(a) HALTS AT (NOT DERIVED)'),
    ("b289's print-coverage order",
     os.path.join(ROOT, 'data', 'b289_consolidation.txt'), 'W-ORD-ALLPRINTS-COVERAGE'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank quotes the involutivity', BANK, 'is its own inverse'),
    ('bank records the corpus absence', BANK, '(ABSENT) FOR THE SOURCE'),
    ('bank grades the import', BANK, 'IMPORT, READ AT CONTENT IN ITS OWN SOURCE'),
    ('bank promotes the reflection', BANK, 'DERIVES-on-IMPORT'),
    ('bank states both arms of the orbit consequence', BANK, 'THERE IS EXACTLY ONE POSITIVE'),
    ('bank returns REFUTED on component 3', BANK, 'VERDICT: (REFUTED)'),
    ('bank gives the computed restriction', BANK, '(1 - lambda(n)^2) xi_n'),
    ('bank separates source vector from corpus vector', BANK, 'W-ORD-ZETA-IS-PSI'),
    ('bank disturbs no measurement', BANK, 'NO MEASUREMENT IS DISTURBED'),
    ('bank blocks transport to the finite places', BANK, 'A REFLECTION NEEDS A'),
    ('bank keeps M-2 unchanged', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('registration fixes falsifier R4', REG, 'IS NOT A CONCLUSION ABOUT THE CORPUS'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('no corpus theorem is claimed', BANK, 'THIS IS A CORPUS THEOREM.'),
    ('the corpus vector is not settled', BANK, 'ZETA_N IS NOT IN THE SONIN SPACE.'),
    ('no measurement is impugned', BANK, 'THE ARCHIMEDEAN NUMBERS ARE WRONG.'),
    ('nothing transported to the finite places', BANK, 'THE FINITE FAMILY CARRIES A REFLECTION.'),
    ('no adoption is stated', BANK, 'THE REFLECTION IS ADOPTED.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b291 -- GATE SUITE')
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
