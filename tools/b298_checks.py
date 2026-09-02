# -*- coding: utf-8 -*-
"""b298 -- THE GATE SUITE.

### NEEDLES ARE PULLED FROM EMITTING FILES AND FROM THIS ACT'S OWN FILES.
### ### **EVERY MUST-FAIL FIXTURE ASSERTS WHOLE-LINE EQUALITY VIA `absent_exact`, NEVER A
### SUBSTRING** -- the b277 inverted-fixture species, closed at b278 and re-gated here.

### ### **AND THE GATES THIS ACT ADDS ARE THE ONES A KERNEL BUILD NEEDS, EACH READ FROM THE
### ### PRINTED PROFILE RATHER THAN FROM A COMPILE'S EXIT CODE (b227's standard):**
###   ### **P-PROFILE** ### -- every `B298.*` declaration reports no axiom dependence, counted
###     with a DISCRIMINATION ARM so a counter that calls everything clean is caught.
###   ### **P-SCOPE** ### -- the terminal's own statement carries the cell and the radii, and the
###     companion conjunct decides the object's own space rejects the witness.
###   ### **P-VANILLA / P-NOFLOAT** ### -- checked CASE-SENSITIVELY over CODE LINES ONLY, because
###     this act's first pass matched `Float` inside the word FLOATING in the module's own sentence
###     saying there is no floating point (declared at the bank's (D2)).
###   ### **P-NOARTIFACT** ### -- the module's index maps are ENUMERATED, not regexed for absence,
###     because a regex for `/ p` cannot tell a level-shifting map from the integer descent inside
###     a valuation, and on the first pass it did not.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull  # noqa: E402
import hedge_audit  # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
BANK = os.path.join(D, 'b298_the_boundary_terminal.txt')
REG = os.path.join(D, 'b298_registration_2026-09-02.txt')
MODULE = os.path.join(SIDE, 'Core', 'BoundaryValueShadow.lean')
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')
ALLPRINTS = os.path.join(SIDE, 'AllPrints.lean')

DECLS = [
    'ball_agrees_with_b270_2_2', 'witness_not_in_object_2_2',
    'witness_has_mass_on_ball_2_2', 'witness_leaves_member_at_b_eq_1_2_2',
    'refuse_value_five_2_2', 'not_dead_2_2', 'not_dead_matches_banked_2_2',
    'class_size_2_2', 'classes_uniform_2_2',
    'boundary_value_at_cell_2_2_on_member_radii_neg1_0',
    'ctor_distinct_2_2', 'ctor_degenerate_2_1',
]

OWNER_NEEDLES = [
    ("b295's existence fact -- the value (EMITTER)",
     os.path.join(D, 'b295_the_second_mechanism.txt'), '4/3'),
    ("b295's witness, by its indices (EMITTER)",
     os.path.join(D, 'b295_the_second_mechanism.txt'), 'e_2 - e_6 + e_4 - e_12'),
    ("b296's general construction (EMITTER)",
     os.path.join(D, 'b296_the_asymmetry.txt'), 'e_{p^{n-1}} - e_{p^{n-1} + p^{2n-2}}'),
    ("b296's degeneracy at (2,1) (EMITTER)",
     os.path.join(D, 'b296_the_asymmetry.txt'), 'UNAVAILABLE'),
    ("b297's kernel plan -- the candidate that passed (EMITTER)",
     os.path.join(D, 'b297_the_fold.txt'), 'NAMES THE MEMBER IN ITS OWN STATEMENT'),
    ("b297's refusal of the other candidates (EMITTER)",
     os.path.join(D, 'b297_the_fold.txt'), 'EVERYTHING ANALYSIS-BOUND'),
    ("b270's absorption law -- the function side (EMITTER)",
     os.path.join(D, 'b270_ambient_pairing_properties.txt'), 'VANISHES ON THE BALL'),
    ("b271's not-dead witness value (EMITTER)",
     os.path.join(D, 'b271_top_level_no_go.txt'), '4(N - q)'),
    ("b289's scar -- imported in the same commit (EMITTER)",
     os.path.join(D, 'b289_consolidation.txt'), 'NEITHER WAS IMPORTED BY'),
    ("b284's escaped-mass artifact (EMITTER)",
     os.path.join(D, 'b284_the_scalings_domain.txt'), 'ESCAPED MASS FOLDED BACK IN'),
    ("the built module's own terminal statement",
     MODULE, 'inMember 2 2 (-1) 0 w = true'),
    ("the built module's scope conjunct",
     MODULE, 'inMember 2 2 0 0 w = false'),
]

SELF_NEEDLES = [
    ('bank reports from the profile, not the compile', BANK,
     'A COMPILE IS NOT A VERIFICATION'),
    ('bank states the pair and its cell', BANK, 'BOTH SIDES OF THE BOUNDARY AT ONE CELL'),
    ('bank refuses to overstate the pair', BANK, 'NOT THE EQUIVALENCE IN GENERAL'),
    ('bank quotes the Lean statement', BANK, 'boundary_value_at_cell_2_2_on_member_radii_neg1_0'),
    ('bank answers the scope question plainly', BANK, 'DOES IT CARRY ITS OWN SCOPE? ### YES'),
    ('bank shows the artifact by enumeration', BANK, 'NOT EXPOSED, AND SHOWN BY ENUMERATION'),
    ('bank restates the refusal list', BANK, 'STILL REFUSED'),
    ('bank restates print coverage with its count', BANK, '25 STILL OUTSIDE'),
    ('bank declares the terminal-count miss', BANK, '10 PREDICTED vs 12 BUILT'),
    ('bank declares the ad-hoc check misfires', BANK, 'FLOATING'),
    ('bank declares the temporary-build hazard', BANK, 'a copy is not a regeneration'),
    ('bank keeps M-2 unchanged', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('bank leaves the keystone question to the author', BANK, 'IS ### THE AUTHOR'),
    ('registration fixed the profile falsifier before the build', REG, 'P-PROFILE'),
    ('registration required the scope in the statement', REG,
     'THE TERMINAL MUST CARRY ITS OWN SCOPE IN ITS OWN STATEMENT'),
]

MUST_FAIL = [
    ('no route is claimed', BANK, 'THE MEMBER IS A ROUTE.'),
    ('the equivalence is not claimed compiled', BANK, 'THE EQUIVALENCE IS CERTIFIED.'),
    ('no aggregation is stated', BANK, 'THE AGGREGATION IS STATED.'),
    ('M-2 is not advanced', BANK, 'M-2 IS STATED.'),
    ('no act is re-verdicted', BANK, 'b294 IS RE-VERDICTED.'),
    ('the refused candidates are not reopened', BANK, 'THE REFUSED CANDIDATES ARE BUILT.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the module claims nothing about the object', MODULE,
     'This is a statement about Son(2,2).'),
]


def code_lines(path):
    """### CODE ONLY -- the block comment and doc comments dropped, so a check cannot match
    ### the prose that DENIES the thing it looks for. ### That is (D2)'s whole lesson."""
    out, in_block = [], False
    for line in io.open(path, encoding='utf-8').read().splitlines():
        s = line.strip()
        if s.startswith('/-'):
            in_block = True
        if in_block:
            if s.endswith('-/'):
                in_block = False
            continue
        if s.startswith('--'):
            continue
        out.append(line)
    return out


def main():
    fails = []
    print('=' * 100)
    print('b298 -- GATE SUITE')
    print('=' * 100)

    print('\n  OWNER NEEDLES (pulled from emitting files):')
    unpullable = 0
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s' % lbl)

    print('\n  SELF NEEDLES:')
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

    # ### P-PROFILE, WITH ITS DISCRIMINATION ARM.
    prof = io.open(PROFILE, encoding='utf-8').read().splitlines()
    clean = [l for l in prof if 'does not depend on any axioms' in l]
    dirty = [l for l in prof if 'depends on axioms' in l]
    b298 = [l for l in prof if "'B298." in l]
    print('\n  P-PROFILE (read from the printed profile, not the compile):')
    print('    total prints %d   zero-axiom %d   axiom-dependent %d   B298 rows %d'
          % (len(prof), len(clean), len(dirty), len(b298)))
    missing = [d for d in DECLS if not any(("'B298.%s'" % d) in l for l in clean)]
    print('    every B298 declaration clean : %s'
          % ('YES' if not missing else '### NO ### %s' % missing))
    if missing or len(dirty) or len(b298) != len(DECLS):
        fails.append('profile')
    synth = ["'F.a' does not depend on any axioms", "'F.b' depends on axioms: [propext]"]
    zc = len([l for l in synth if 'does not depend on any axioms' in l])
    print('    DISCRIMINATION ARM: 2 synthetic lines, counted zero-axiom = %d (must be 1)  %s'
          % (zc, 'PASS' if zc == 1 else '### FAIL ###'))
    if zc != 1:
        fails.append('profile discrimination')

    # ### P-SCOPE.
    src = io.open(MODULE, encoding='utf-8').read()
    scope_ok = ('inMember 2 2 (-1) 0 w = true' in src
                and 'inMember 2 2 0 0 w = false' in src
                and 'classSize 2 2 = 3' in src
                and 'pairTimesClass 2 2 w = 4' in src)
    print('\n  P-SCOPE : the terminal names cell and radii, and decides the object rejects the'
          ' witness : %s' % ('PASS' if scope_ok else '### FAIL ###'))
    if not scope_ok:
        fails.append('scope')

    # ### P-VANILLA / P-NOFLOAT -- CODE LINES ONLY, CASE-SENSITIVE.
    code = code_lines(MODULE)
    imports = [l for l in code if l.startswith('import ')]
    floats = [l for l in code if re.search(r'\d\.\d', l) or re.search(r'\bFloat\b', l)]
    native = [l for l in code if 'native_decide' in l]
    tactics = re.findall(r':=\s*by\s+(\w+)', '\n'.join(code))
    nondecide = sorted({t for t in tactics if t != 'decide'})
    print('  P-VANILLA: imports %d   native_decide %d   tactics other than decide %s'
          % (len(imports), len(native), nondecide if nondecide else 'none'))
    print('  P-NOFLOAT: float literals / Float tokens in CODE lines : %d' % len(floats))
    if imports or native or nondecide or floats:
        fails.append('vanilla/float')

    # ### P-NOARTIFACT -- ENUMERATE, do not regex for absence.
    maps = [l.strip() for l in code if '% N p n' in l]
    shifts = [l for l in code if 'scale_g' in l or 'scale_h' in l]
    print('  P-NOARTIFACT: index maps enumerated %d   b284 level-shifting maps present %d'
          % (len(maps), len(shifts)))
    for m in maps:
        print('      %s' % m[:96])
    if shifts:
        fails.append('artifact')

    # ### THE IMPORT, IN THE SAME COMMIT.
    ap = io.open(ALLPRINTS, encoding='utf-8').read()
    imported = 'import BoundaryValueShadow' in ap
    printed = sum(1 for d in DECLS if ('#print axioms B298.%s' % d) in ap)
    print('  P-IMPORT : module imported by AllPrints.lean : %s   print lines for it : %d/%d'
          % (imported, printed, len(DECLS)))
    if not imported or printed != len(DECLS):
        fails.append('import')

    n, gh, ua = hedge_audit.audit(BANK)
    print('\n  HEDGE AUDIT on own bank : sentences=%d graded-hedges=%d ungraded-shapes=%d'
          % (n, len(gh), len(ua)))
    if gh:
        fails.append('graded hedges in own bank')
        for s in gh:
            print('      (i) a graded sentence also hedges: %d characters, described not quoted'
                  % len(s))

    print('\n' + '=' * 100)
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 6 - len(fails),
             len(fails), unpullable))
    print('=' * 100)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
