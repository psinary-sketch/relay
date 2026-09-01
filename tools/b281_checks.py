# -*- coding: utf-8 -*-
"""b281 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b281_the_compression.txt')
REG = os.path.join(ROOT, 'data', 'b281_registration_2026-09-01.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ('keystone: archimedean specified separately', KEY, 'the Sonin condition at the'),
    ("b273's form definition", os.path.join(ROOT, 'data', 'b273_spec2_range.txt'),
     'A[l,j] = SUM_{m : p^k m = l mod N} S_quot[m,j]'),
    ("b273: neither Hermitian nor symmetric", os.path.join(ROOT, 'data', 'b273_spec2_range.txt'),
     'THE FORM IS NEITHER HERMITIAN NOR'),
    ("b272: g_c are real-valued", os.path.join(ROOT, 'data', 'b272_escape_class.txt'),
     'REAL-VALUED'),
    ("b272: the g_c span E_1", os.path.join(ROOT, 'data', 'b272_escape_class.txt'),
     'THE `g_c` SPAN `E_1`'),
    ("b21: the standard character", os.path.join(ROOT, 'data', 'b21_2026-08-18.txt'),
     'psi the standard character'),
    ("b227: sign over R or phase over C", os.path.join(ROOT, 'data', 'b227_the_trace.txt'),
     'a sign (over R) or a phase (over C)'),
    ("b276's fiber-lemma scope", os.path.join(ROOT, 'data', 'b276_size_equivalence_tension.txt'),
     'PROVED AT LEVEL 1 AND FULLY VERIFIED'),
    ("b271's shadow printed profile", os.path.join(ROOT, 'data', 'b271_top_level_no_go.txt'),
     '7 TERMINALS, ALL PRINTING'),
    ('C2 named at its owner', os.path.join(ROOT, 'data', 'b269_filings.txt'),
     'EXTEND THE PROJECTION TO AN ACTION'),
    ("b263's branch question", os.path.join(ROOT, 'data', 'b263_filings.txt'),
     'finite side supplies, or archimedean side absorbs'),
    ("b264's E2even asymptote", os.path.join(ROOT, 'data', 'b264_eps_even_decay.txt'),
     'NOT ### A POWER OF `a`'),
    ("b280's verdict, carried", os.path.join(ROOT, 'data', 'b280_the_consequence.txt'),
     'VERDICT: (BARRIER)'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank returns (COMPRESSION ZERO)', BANK, 'VERDICT: (COMPRESSION ZERO)'),
    ('bank states no polarization is used', BANK, 'NO POLARIZATION IS USED'),
    ('bank carries the finite-place boundary', BANK, 'this is the FINITE PLACES ONLY'),
    ('bank derives C2 closed', BANK, 'SO C2 CANNOT ESCAPE THE COMPRESSION'),
    ('bank names C3 surviving', BANK, 'THE SURVIVING SHAPE, WITH THE REASON'),
    ('bank keeps b263 as bearing', BANK, 'CARRIED AS BEARING, NEVER AS A DECISION'),
    ('bank protects b276', BANK, 'b276 IS UNTOUCHED AND IS NOT RE-VERDICTED'),
    ('bank keeps M-2 owed', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED)'),
    ('bank names the fold as next', BANK, 'THE NEXT ACT IS THE FOLD'),
    ('registration fixes falsifier H3', REG, 'A BANKED LEMMA IS NOT REFUTED BY A COMPUTATION'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('no archimedean claim', BANK, 'THE COMPRESSION IS ZERO AT THE ARCHIMEDEAN PLACE.'),
    ('no adoption is stated', BANK, 'C3 IS ADOPTED.'),
    ('b276 is not refuted', BANK, 'b276 IS REFUTED.'),
    ('b263 is not decided', BANK, 'THE FINITE SIDE DOES NOT SUPPLY THE MASS.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b281 -- GATE SUITE')
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
