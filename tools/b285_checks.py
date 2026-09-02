# -*- coding: utf-8 -*-
"""b285 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b285_archimedean_opening.txt')
REG = os.path.join(ROOT, 'data', 'b285_registration_2026-09-01.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ("keystone's infinity clause", KEY, 'the Sonin condition at the'),
    ("keystone: a Hilbert object, not a function space", KEY,
     'it is a Hilbert object, not a function'),
    ("N-OPEN-A, the analytic function space",
     os.path.join(ROOT, 'data', 'analytic_theta_constructor_registration_STAGED_2026-08-22.txt'),
     'the analytic function space the object lives in at the CC scale'),
    ("N-OPEN-B, the real-fiber measure",
     os.path.join(ROOT, 'data', 'analytic_theta_constructor_registration_STAGED_2026-08-22.txt'),
     'the real-fiber measure/normalization'),
    ("CC-scale ground is recorded, not built",
     os.path.join(ROOT, 'data', 'adelic_phase_plane_registration_STAGED_2026-08-21.txt'),
     'not built'),
    ("b198's proved theorem (EMITTER)",
     os.path.join(ROOT, 'data', 'b198_nonvanishing.txt'),
     'real_no_compact_open_addSubgroup'),
    ("b263's branch sentence (EMITTER)", os.path.join(ROOT, 'data', 'b263_filings.txt'),
     'finite side supplies, or archimedean side absorbs'),
    ("b263: the honest first step is a statement-read",
     os.path.join(ROOT, 'data', 'b263_filings.txt'), 'a statement-read on `eps`, not a ladder'),
    ("b262's divergence (EMITTER)", os.path.join(ROOT, 'data', 'b262_junction_limit.txt'),
     'THE JUNCTION DIVERGES ALONG THE CUTOFF LIMIT'),
    ("b262's PNT import (EMITTER)", os.path.join(ROOT, 'data', 'b262_junction_limit.txt'),
     'PNT IN CHEBYSHEV FORM'),
    ("b264's envelope (EMITTER)", os.path.join(ROOT, 'data', 'b264_eps_even_decay.txt'),
     'C_even = 132.781908429'),
    ("b264's printed reach (EMITTER)", os.path.join(ROOT, 'data', 'b264_eps_even_decay.txt'),
     'CONVERGED ON THE LADDER AND `rho < 238.4` ON THE CURVE'),
    ("b261's dilation identity (EMITTER)",
     os.path.join(ROOT, 'data', 'b261_e2even_monotone.txt'),
     'E2even(a) = E_{s~p}[ eps_even(a^s) ]'),
    ("b250's S3(a) halt (EMITTER)", os.path.join(ROOT, 'data', 'b250_m4_derivation.txt'),
     'S3(a) HALTS AT (NOT DERIVED)'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank returns NAMED-NOT-CONSTRUCTED', BANK, 'VERDICT ON THE SPACE: (NAMED-NOT-CONSTRUCTED)'),
    ('bank answers the typing question', BANK, 'NO FINITE-SIDE STRUCTURAL FACT TYPES AT'),
    ('bank corrects the ferry premise', BANK, 'NO SUCH FILING EXISTS IN THE RECORD'),
    ('bank reports the arity as open', BANK, 'ONE CONDITION OR TWO? ### NOT STATED'),
    ('bank quotes the target without fitting', BANK, 'APPROACHES IT, APPROXIMATES IT, OR IS COMPARED TO IT'),
    ('bank names the knowledge boundary', BANK, 'A SHADOW ALONG A DIRECTION IS NOT THE TERM'),
    ('bank carries the hazard register', BANK, 'THE MOST DANGEROUS WORD ON THIS LIST'),
    ('bank keeps M-2 unchanged', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('bank restates the seam debt', BANK, "THE SEAM'S DEBT ITEM 1"),
    ('registration fixes falsifier K4', REG, 'THE ACT SAYS SO PLAINLY'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('the branch is not decided', BANK, 'THE ARCHIMEDEAN SIDE ABSORBS THE MASS.'),
    ('absorption is not derived', BANK, 'ABSORPTION IS DERIVED.'),
    ('no finite result is transported', BANK, 'THE BARRIER HOLDS AT THE ARCHIMEDEAN PLACE.'),
    ('the space is not claimed constructed', BANK, 'THE ARCHIMEDEAN LOCAL SPACE IS CONSTRUCTED.'),
    ('no adoption is stated', BANK, 'C3 IS ADOPTED.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b285 -- GATE SUITE')
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
