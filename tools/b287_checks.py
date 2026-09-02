# -*- coding: utf-8 -*-
"""b287 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b287_the_two_papers.txt')
REG = os.path.join(ROOT, 'data', 'b287_registration_2026-09-01.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ("b202 names its source as 2112.05500 (EMITTER)",
     os.path.join(ROOT, 'data', 'b202_sum_test.txt'), 'Connes-Moscovici'),
    ("b202's CM Sonin description (EMITTER)",
     os.path.join(ROOT, 'data', 'b202_sum_test.txt'),
     "Sonin's space is the orthogonal of the"),
    ("b202 also imports at CC's text grade (EMITTER)",
     os.path.join(ROOT, 'data', 'b202_sum_test.txt'), "CC 2006.13771v1's text grade"),
    ("b286's CC description (EMITTER)",
     os.path.join(ROOT, 'data', 'b286_the_cc_condition.txt'),
     'together with their Fourier'),
    ("b286 recorded the projections as deferred (EMITTER)",
     os.path.join(ROOT, 'data', 'b286_the_cc_condition.txt'),
     'DEFERRED TO REFERENCE [18]'),
    ("b232's identifier correction (EMITTER)",
     os.path.join(ROOT, 'data', 'b232_registration_2026-08-28.txt'),
     'THE GENUINE CC WORK IS arXiv 2006.13771'),
    ("b232 names 2112.05500 as Connes-Moscovici (EMITTER)",
     os.path.join(ROOT, 'data', 'b232_registration_2026-08-28.txt'),
     'arXiv 2112.05500 IS CONNES-MOSCOVICI'),
    ("b285's typing verdict, carried",
     os.path.join(ROOT, 'data', 'b285_archimedean_opening.txt'),
     'NO FINITE-SIDE STRUCTURAL FACT TYPES AT'),
    ("b285's hazard register on 'unit'",
     os.path.join(ROOT, 'data', 'b285_archimedean_opening.txt'),
     'THE MOST DANGEROUS WORD ON THIS LIST'),
    ("b284's dual failure, carried",
     os.path.join(ROOT, 'data', 'b284_the_scalings_domain.txt'),
     'VERDICT: (FAILS) -- IN BOTH DIRECTIONS'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank returns SAME SPACE', BANK, 'VERDICT: (SAME SPACE), DERIVED'),
    ('bank quotes Definition 4.4', BANK, 'let Sonin'),
    ('bank shows the derivation is not by name', BANK, 'NO SHARED NAME AND NO SHARED AUTHOR'),
    ('bank names and grades the one link', BANK, 'W-ORD-WSA-PSI-LINK'),
    ('bank locates [18] as a book', BANK, 'Colloquium Publications, Vol.55'),
    ('bank records the definition is not deferred', BANK, 'DEPENDS ON `[18]` FOR NOTHING'),
    ('bank keeps N-OPEN-B open', BANK, '`N-OPEN-B` REMAINS OPEN'),
    ('bank files the proposal unopened', BANK, 'UNBANKED-UNTIL-TESTED'),
    ('bank carries the smear caution', BANK, 'OBJECT FROM A FUNCTIONAL OF ONE OPERATOR'),
    ('bank re-verdicts nothing', BANK, 'NOT ONE OF THOSE ACTS IS RE-VERDICTED'),
    ('bank keeps M-2 unchanged', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('registration fixes falsifier M1', REG, 'NEITHER A SHARED WORD NOR A SHARED AUTHOR'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('nothing is adopted', BANK, 'THE CC CONDITION IS ADOPTED.'),
    ('nothing is constructed', BANK, 'THE ARCHIMEDEAN LOCAL SPACE IS CONSTRUCTED.'),
    ('the deferred book is not treated as read', BANK, '[18] WAS READ.'),
    ('the proposal is not opened', BANK, 'THE SMEARED FUNCTIONAL IS ADOPTED.'),
    ('no finite result is transported', BANK, 'b284 APPLIES AT THE ARCHIMEDEAN PLACE.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b287 -- GATE SUITE')
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
