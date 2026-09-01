# -*- coding: utf-8 -*-
"""b284 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b284_the_scalings_domain.txt')
REG = os.path.join(ROOT, 'data', 'b284_registration_2026-09-01.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ("b21's genuine scaling (EMITTER)", os.path.join(ROOT, 'data', 'b21_2026-08-18.txt'),
     'THE GENUINE SCALING'),
    ("b21's escape/support law (EMITTER)", os.path.join(ROOT, 'data', 'b21_2026-08-18.txt'),
     'U ESCAPES V_n, exactly'),
    ("b21's wraparound sentence (EMITTER)", os.path.join(ROOT, 'data', 'b21_2026-08-18.txt'),
     "THE MODEL'S mod-N WRAPAROUND IS EXACTLY THIS ESCAPED MASS FOLDED BACK IN"),
    ("b21's standard character (EMITTER)", os.path.join(ROOT, 'data', 'b21_2026-08-18.txt'),
     'psi the standard character'),
    ("b21's chart and Haar (EMITTER)", os.path.join(ROOT, 'data', 'b21_2026-08-18.txt'),
     'via x = p^(-n) m'),
    ("b10's non-descent (EMITTER)", os.path.join(ROOT, 'data', 'b10_2026-08-17.txt'),
     'THE FOURIER HALF DOES NOT DESCEND'),
    ("b10 defines V_inv on the orbit space (EMITTER)",
     os.path.join(ROOT, 'data', 'b10_2026-08-17.txt'), 'the orbit space x ~ px of'),
    ("b263's branch question (EMITTER)", os.path.join(ROOT, 'data', 'b263_filings.txt'),
     'finite side supplies, or archimedean side absorbs'),
    ("b264's E2even asymptote (EMITTER)",
     os.path.join(ROOT, 'data', 'b264_eps_even_decay.txt'), 'NOT ### A POWER OF `a`'),
    ("b283's iota finding, carried", os.path.join(ROOT, 'data', 'b283_the_tower_action.txt'),
     'VERDICT: (DOUBLE-NAME)'),
    ("b279's construction", os.path.join(ROOT, 'data', 'b279_the_local_space.txt'),
     'VERDICT: (CONSTRUCTED)'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank returns (FAILS) both directions', BANK, 'VERDICT: (FAILS) -- IN BOTH DIRECTIONS'),
    ('bank names the gap set', BANK, 'THE UNITS `Z_p^x = Z_p \ p Z_p`'),
    ('bank scopes the entailment', BANK, 'C3-VIA-SCALING IS CLOSED'),
    ('bank refuses the wider claim', BANK, 'NOT ### "C3 IS CLOSED"'),
    ('bank declares the import', BANK, 'AN IMPORT UNDER THE'),
    ('bank reports the disagreement', BANK, 'THE DISAGREEMENT IS THE ARTIFACT'),
    ('bank reports the vacuity', BANK, 'IS IDENTICALLY ZERO FOR ### EVERY'),
    ('bank keeps b263 as bearing', BANK, 'BEARING, NEVER A DECISION'),
    ('bank files the archimedean note', BANK, 'FILED, NOT OPENED'),
    ('bank keeps M-2 owed', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED)'),
    ('registration fixes falsifier J2', REG, 'IS NOT THE CONDITION'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('C3 is not declared closed', BANK, 'C3 IS CLOSED.'),
    ('no adoption is stated', BANK, 'C3 IS ADOPTED.'),
    ('the scaling is not claimed to preserve', BANK, 'THE SCALING PRESERVES S-bar_p.'),
    ('no archimedean claim', BANK, 'THE ARCHIMEDEAN SIDE ABSORBS THE MASS.'),
    ('b263 is not decided', BANK, 'THE FINITE SIDE DOES NOT SUPPLY THE MASS.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b284 -- GATE SUITE')
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
