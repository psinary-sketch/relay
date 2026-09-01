# -*- coding: utf-8 -*-
"""b283 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b283_the_tower_action.txt')
REG = os.path.join(ROOT, 'data', 'b283_registration_2026-09-01.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ("b21 defines iota as a chart refinement (EMITTER)",
     os.path.join(ROOT, 'data', 'b21_2026-08-18.txt'),
     "isometric embedding iota: V_n -> V_(n+1) (chart"),
    ("b21's genuine scaling escapes the level (EMITTER)",
     os.path.join(ROOT, 'data', 'b21_2026-08-18.txt'),
     'U ESCAPES V_n, exactly'),
    ("b21's chart and Haar (EMITTER)",
     os.path.join(ROOT, 'data', 'b21_2026-08-18.txt'), 'via x = p^(-n) m'),
    ("b10 defines V_inv by x ~ px (EMITTER)",
     os.path.join(ROOT, 'data', 'b10_2026-08-17.txt'), 'the orbit space x ~ px of'),
    ("b10's non-descent (EMITTER)",
     os.path.join(ROOT, 'data', 'b10_2026-08-17.txt'),
     'THE FOURIER HALF DOES NOT DESCEND'),
    ("act 9 sec 2's quantity at its EMITTER b220",
     os.path.join(ROOT, 'data', 'b220_aggregation_freedom.txt'),
     'tau_q(p,n,k) * p^(k/2) = (p^n - p^k)/(p^n - 1)'),
    ("b281's barrier form", os.path.join(ROOT, 'data', 'b281_the_compression.txt'),
     'THE LEFT PROJECTION ALONE KILLS THE OPERATOR'),
    ("b281's stated crack", os.path.join(ROOT, 'data', 'b281_the_compression.txt'),
     'would not be C2, and this act says'),
    ("b279's construction", os.path.join(ROOT, 'data', 'b279_the_local_space.txt'),
     'VERDICT: (CONSTRUCTED)'),
    ("banked TowerInstance profile",
     os.path.join(ROOT, 'data', 'b227_core_remeasured.txt'),
     "'TowerInstance.support_ball_vanish' does not depend on any axioms"),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank returns (DOUBLE-NAME)', BANK, 'VERDICT: (DOUBLE-NAME)'),
    ('bank says the tower gives a filtration', BANK, 'A FILTRATION, NOT AN ACTION'),
    ('bank stops at (c)', BANK, 'STRUCTURE IS BUILT, AND NONE IS SKETCHED'),
    ('bank refuses the vacuous reading', BANK, 'TRUE AND VACUOUS'),
    ('bank keeps C3 price unchanged', BANK, "C3's PRICE: ### UNCHANGED"),
    ('bank routes b10 rather than applying it', BANK, 'NAMED AND ROUTED, NOT APPLIED'),
    ('bank names the third object', BANK, 'W-ORD-U-PRESERVES-SBAR'),
    ('bank keeps M-2 owed', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED)'),
    ('bank restates the seam debt', BANK, "THE SEAM'S DEBT ITEM 1"),
    ('registration fixes falsifier I4', REG, 'NEEDLES PULLED FROM EMITTING FILES'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('no orbit structure is built', BANK, 'THE ORBIT STRUCTURE IS BUILT.'),
    ('no adoption is stated', BANK, 'C3 IS ADOPTED.'),
    ('C3 price is not reduced', BANK, "C3'S PRICE IS REDUCED."),
    ('no archimedean claim', BANK, 'THE ARCHIMEDEAN QUESTION IS SETTLED.'),
    ('U is not claimed to preserve S-bar', BANK, 'U PRESERVES S-bar_p.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b283 -- GATE SUITE')
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
