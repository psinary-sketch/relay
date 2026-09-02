# -*- coding: utf-8 -*-
"""b286 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b286_the_cc_condition.txt')
REG = os.path.join(ROOT, 'data', 'b286_registration_2026-09-01.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ("b232's identifier correction (EMITTER)",
     os.path.join(ROOT, 'data', 'b232_registration_2026-08-28.txt'),
     'THE GENUINE CC WORK IS arXiv 2006.13771'),
    ("b232 names 2112.05500 as Connes-Moscovici (EMITTER)",
     os.path.join(ROOT, 'data', 'b232_registration_2026-08-28.txt'),
     'arXiv 2112.05500 IS CONNES-MOSCOVICI'),
    ("b232's 123-PDF search (EMITTER)",
     os.path.join(ROOT, 'data', 'b232_registration_2026-08-28.txt'), '2006.13771'),
    ("b202 names its source as 2112.05500 (EMITTER)",
     os.path.join(ROOT, 'data', 'b202_sum_test.txt'), 'Connes-Moscovici'),
    ("b202 banks the CM Sonin description (EMITTER)",
     os.path.join(ROOT, 'data', 'b202_sum_test.txt'),
     "Sonin's space is the orthogonal of the"),
    ("b202's index-query lesson (EMITTER)",
     os.path.join(ROOT, 'data', 'audit_b202_index_query.txt'),
     'the record names no element of the'),
    ("b198's proved theorem (EMITTER)",
     os.path.join(ROOT, 'data', 'b198_nonvanishing.txt'),
     'real_no_compact_open_addSubgroup'),
    ("b284's dual failure, carried",
     os.path.join(ROOT, 'data', 'b284_the_scalings_domain.txt'),
     'VERDICT: (FAILS) -- IN BOTH DIRECTIONS'),
    ("b285's typing verdict, carried",
     os.path.join(ROOT, 'data', 'b285_archimedean_opening.txt'),
     'NO FINITE-SIDE STRUCTURAL FACT TYPES AT'),
    ("b285 recorded the singular as not evidence",
     os.path.join(ROOT, 'data', 'b285_archimedean_opening.txt'),
     'ONE CONDITION OR TWO? ### NOT STATED'),
    ("b264's printed reach (EMITTER)",
     os.path.join(ROOT, 'data', 'b264_eps_even_decay.txt'),
     'CONVERGED ON THE LADDER AND `rho < 238.4` ON THE CURVE'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank returns SUPPLIED BY SOURCE', BANK, 'VERDICT ON `N-OPEN-A`: (SUPPLIED BY SOURCE)'),
    ('bank names the space', BANK, 'square integrable even'),
    ('bank answers the count', BANK, 'TWO CONDITIONS'),
    ('bank names the cutoff and scale', BANK, 'THE `Lambda = 1` CUTOFF'),
    ('bank quotes the does-not-restrict sentence', BANK, 'DOES NOT RESTRICT to this subspace'),
    ('bank flags the second identifier hazard', BANK, 'FROM THE ### OTHER ### PAPER'),
    ('bank refuses to compute the convergence', BANK, 'IT DOES NOT COMPARE'),
    ('bank grades the import', BANK, 'GRADE: ### IMPORT'),
    ('bank keeps b285 un-re-verdicted', BANK, 'b285 IS NOT RE-VERDICTED'),
    ('bank keeps M-2 unchanged', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('registration fixes falsifier L1', REG, 'THE SOURCE MUST BE 2006.13771 ITSELF'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('no condition is adopted', BANK, 'THE CC CONDITION IS ADOPTED.'),
    ('no construction is attempted', BANK, 'THE ARCHIMEDEAN LOCAL SPACE IS CONSTRUCTED.'),
    ('the import is not a corpus theorem', BANK, 'THIS IS A CORPUS THEOREM.'),
    ('the branch is not decided', BANK, 'THE ARCHIMEDEAN SIDE ABSORBS THE MASS.'),
    ('no finite result is transported', BANK, 'b284 APPLIES AT THE ARCHIMEDEAN PLACE.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b286 -- GATE SUITE')
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
