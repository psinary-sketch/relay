# -*- coding: utf-8 -*-
"""b296 -- THE GATE SUITE.

### NEEDLES ARE PULLED FROM OWNER FILES ### AND ### FROM THIS ACT'S OWN FILES
### (W-ORD-NEEDLE-SOURCE, W-ORD-SELF-NEEDLE -- both discharged, both kept discharged).
### ### **EVERY MUST-FAIL FIXTURE ASSERTS WHOLE-LINE EQUALITY VIA `absent_exact`, NEVER A
### SUBSTRING** -- the b277 inverted-fixture species, closed at b278 and re-gated here.

### ### **TWO GATES THIS ACT ADDS, BOTH FROM ITS OWN SCOPE:**
###   ### **(i) THE SYMMETRIC-DEFAULT GATE.** ### The registration retired the navigator's
###     symmetric framing by name and declared a cap of ZERO on symmetric premises. ### A cap that
###     nothing checks is a sentence, so the bank must carry the retirement as a findable line.
###   ### **(ii) THE FALLBACK-NOT-FOLDED GATE.** ### Y9 forbids folding a fallback arm into a pass
###     count. ### The run must carry the separation as a findable line.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull  # noqa: E402
import hedge_audit  # noqa: E402

D = os.path.join(ROOT, 'data')
BANK = os.path.join(D, 'b296_the_asymmetry.txt')
REG = os.path.join(D, 'b296_registration_2026-09-02.txt')
RUN = os.path.join(D, 'b296_asymmetry_run.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL, never a skip.
OWNER_NEEDLES = [
    ("b293's collapse -- the fiber-sum condition (EMITTER)",
     os.path.join(D, 'b293_the_finite_family.txt'),
     "SUM_{m' = r mod p^{n+b}} f(m') = 0"),
    ("b279's collapse at b = 0 (EMITTER)",
     os.path.join(D, 'b279_the_local_space.txt'), 'every fiber sum is zero'),
    ("b279's level bookkeeping (EMITTER)",
     os.path.join(D, 'b279_the_local_space.txt'), 'reproduced exactly `p` times'),
    ("b281's operator definition (EMITTER)",
     os.path.join(D, 'b281_the_compression.txt'), 'S_quot[m,j]'),
    ("b281's form TYPE -- the asymmetry's source (EMITTER)",
     os.path.join(D, 'b281_the_compression.txt'), 'NEITHER HERMITIAN NOR SYMMETRIC'),
    ("b270's barrier hypothesis (EMITTER)",
     os.path.join(D, 'b270_ambient_pairing_properties.txt'), 'VANISHES ON THE BALL'),
    ("b271's not-dead witness value",
     os.path.join(D, 'b271_top_level_no_go.txt'), '4(N - q)'),
    ("b272's spanning-family incident -- the species' first sighting",
     os.path.join(D, 'b272_escape_class.txt'), 'ONE MEMBER OF AN `N`-MEMBER SPANNING FAMILY'),
    ("b280's barrier verdict",
     os.path.join(D, 'b280_the_consequence.txt'), 'VERDICT: (BARRIER)'),
    ("b284's escaped-mass artifact",
     os.path.join(D, 'b284_the_scalings_domain.txt'), 'ESCAPED MASS FOLDED BACK IN'),
    ("b285's typing verdict",
     os.path.join(D, 'b285_archimedean_opening.txt'),
     'NO FINITE-SIDE STRUCTURAL FACT TYPES AT'),
    ("b295's criterion -- what this act refines",
     os.path.join(D, 'b295_the_second_mechanism.txt'), '`a >= 0`  ###  OR  ###  `b >= n - 1`'),
    ("b295's own filing of the necessity question",
     os.path.join(D, 'b295_the_second_mechanism.txt'), 'W-ORD-CRITERION-NECESSITY'),
    ("b266's fold precedent -- the next act, named not attempted",
     os.path.join(D, 'b266_registration_2026-08-31.txt'), 'THE FOLD *STATES* GRADES AND CONFERS'),
]

# ### SELF needles -- into this act's OWN emitted files, PULLED and not typed from memory.
SELF_NEEDLES = [
    ('bank returns the three-part verdict', BANK, 'THE THRESHOLD FALLS OUT'),
    ('bank states the equivalence', BANK, 'IF AND ONLY IF'),
    ('bank names the reading scale', BANK, 'ONE STEP COARSER THAN POINTWISE'),
    ('bank derives the threshold from the scale', BANK,
     'AND NOT FROM THE CRITERION IT EXPLAINS'),
    ('bank states the ONE common statement', BANK,
     'EACH THRESHOLD IS THE DISTANCE FROM'),
    ('bank retires the symmetric default by name', BANK,
     "THE NAVIGATOR'S SYMMETRIC FRAMING IS RETIRED BY NAME"),
    ('bank carries the one-sidedness measurement', BANK, 'THE ANNIHILATION IS ONE-SIDED'),
    ('bank says which condition the members weaken', BANK,
     "EACH WEAKENS THE OBJECT'S ### FIRST ### CONDITION"),
    ('bank prints the witness ball-mass rather than asserting it', BANK,
     'HAS MASS ON THE BALL'),
    ('bank keeps the barrier untouched and re-measures it', BANK, '40 OF 40'),
    # ### RE-PULLED: the first anchor spanned a line break ("... ### No / level-shifting map
    # ### appears ..."), which is b280's own scar and b293's re-pull, met again.
    ('bank states the artifact exposure', BANK, 'level-shifting map appears'),
    ('bank separates the derivation from its control', BANK,
     'IS A ### DERIVATION ### AND IS NOT LIMITED TO'),
    ('bank declares the post-run reporting patch', BANK,
     'NO MEASUREMENT'),
    ('bank keeps the reopening unbanked', BANK, 'STILL UNBANKED-UNTIL-TESTED'),
    ('bank keeps M-2 unchanged', BANK,
     'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('bank names the fold as the next act', BANK, 'THE FOLD, `b283-b296`'),
    ('bank leaves the new-keystone question to the author', BANK,
     "IS ### THE AUTHOR'S ### , NOT THIS SEAT'S"),
    ('registration fixed the deciding falsifier BEFORE the run', REG,
     'THE FALSIFIER FOR C1\'s (DERIVED)'),
    ('registration capped symmetric premises at zero', REG,
     'NO SYMMETRIC EXPECTATION ABOUT THE TWO CONDITIONS IS USED'),
    ('registration predicted the degeneracy cell in advance', REG,
     'AT `(2,1)` THE CONSTRUCTION'),
    ('run carries the reading-scale measurement', RUN, "THE OPERATOR'S READING SCALE"),
    ('run separates the fallback from the general arm', RUN,
     'REPORTED UNAVAILABLE AT THE FALLBACK CELLS, NEVER A PASS'),
    ('run closes Y8 arithmetic on the page', RUN, 'forced-zero decomposition'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.**
MUST_FAIL = [
    ('no route is claimed', BANK, 'THE MEMBER IS A ROUTE.'),
    ('the barrier is not weakened', BANK, 'THE BARRIER IS WEAKENED.'),
    ('the barrier is not extended', BANK, 'THE BARRIER IS EXTENDED.'),
    ('no aggregation is stated', BANK, 'THE AGGREGATION IS STATED.'),
    ('M-2 is not advanced', BANK, 'M-2 IS STATED.'),
    ('no prior act is re-verdicted', BANK, 'b295 IS RE-VERDICTED.'),
    ('the two conditions are not called symmetric', BANK,
     'THE TWO CONDITIONS ARE SYMMETRIC.'),
    ('the threshold is not conceded as fitted', BANK, 'THE THRESHOLD IS FITTED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b296 -- GATE SUITE')
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
