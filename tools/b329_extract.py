# -*- coding: utf-8 -*-
"""b329_extract.py -- THE EXTRACT STEP FOR THE FINITE-SIDE SEAL. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### The fixed-point sentence as b309 and b310 wrote it (the
### module's docstring quotes it from its emitting act); b304's derivation of the compact part's zero
### (orthogonality to the valuation shells) and its own refusal (the traces are not all zero); the two
### shadow modules whose definitions this module restates (`gridN`, `ballQ`, `offBallFixed`) and whose
### headers say the general law is uncompiled; b270's polarity idiom; the certification file's last
### import and last print; the correspondence rows and the ledger row this act bears on; the lore's
### anchors. ### b283's law: every quotation located at its emitting file and its line before it is
### written anywhere else; the gate suite pulls its needles from THIS file.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b329_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def s(n):
    return os.path.join(SIDE, n)


WANTED = [
    # ### ---- b309: the scaling part's mechanism, the sentence the exhaustiveness theorem's docstring quotes
    ('b309 -- the mechanism in one sentence, first half', d('b309_the_scaling_trace.txt'), 'THE SCALING MAP HAS NO FIXED POINT OFF THE BALL,'),
    ('### its second half: p^j - 1 invertible', d('b309_the_scaling_trace.txt'), 'BECAUSE `p^j - 1` IS INVERTIBLE'),
    ('### its third half: the only fixed point is where the object vanishes', d('b309_the_scaling_trace.txt'), 'IS THE ONE PLACE THE OBJECT IS REQUIRED TO VANISH.'),
    # ### ---- b310: the fixed-point sentence, the signed count, the identity value
    ('b310 -- the fixed-point sentence, first line', d('b310_the_smear_collapses.txt'), 'IS A SIGNED COUNT OF THE OFF-BALL POINTS `t` FIXES, IN THE TWO'),
    ('### its second line, with the Haar factor', d('b310_the_smear_collapses.txt'), "CONGRUENCES THE OBJECT'S TWO CONDITIONS IMPOSE, WEIGHTED BY THE EMBEDDING'S HAAR FACTOR."),
    ('### b304 and b309 are one statement', d('b310_the_smear_collapses.txt'), 'THOSE ARE ONE STATEMENT, AND THIS IS IT:'),
    ('### the identity value', d('b310_the_smear_collapses.txt'), 'at `t = 1` every off-ball point is fixed and the count is `(p^n - 1)^2`;'),
    # ### ---- b304: the compact part's zero, derived by orthogonality to the shells; and its own refusal
    ('b304 -- the smeared object unfolded', d('b304_the_demands_shape.txt'), 'Tr(theta(f) Pi) = SUM_t f(t) Tr(theta(t) Pi)'),
    ('### the averaged sum is the projection onto the invariants', d('b304_the_demands_shape.txt'), 'SUM_{t in U} theta(t) = |U| * Q'),
    ('### the orbits are the valuation shells', d('b304_the_demands_shape.txt'), 'VALUATION SHELLS'),
    ('### a shell at or above the level lies in the ball', d('b304_the_demands_shape.txt'), 'WHERE EVERY `Son` VECTOR VANISHES'),
    ('### a shell below the level is a union of fibers', d('b304_the_demands_shape.txt'), 'each zero by the transform condition.'),
    ('### both limbs checked at every cell', d('b304_the_demands_shape.txt'), 'BOTH LIMBS CHECKED AT EVERY CELL'),
    ('### the zero at all six cells', d('b304_the_demands_shape.txt'), 'THE SMEARED VALUE EXACTLY 0 AT ALL SIX'),
    ("### b304's own refusal: the traces are not all zero", d('b304_the_demands_shape.txt'), 'AND THOSE TRACES ARE NOT ALL ZERO'),
    # ### ---- the two shadow modules whose definitions this module restates, and their own refusal
    ('B309 module -- the cells', s('Core/ScalingTraceShadow.lean'), 'def cells : List (Nat × Nat) := [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1), (2, 3)]'),
    ('### the grid', s('Core/ScalingTraceShadow.lean'), 'def gridN (p n : Nat) : Nat := p ^ (2 * n)'),
    ('### the ball', s('Core/ScalingTraceShadow.lean'), 'def ballQ (p n : Nat) : Nat := p ^ n'),
    ('### the per-cell theorem it decides', s('Core/ScalingTraceShadow.lean'), 'theorem no_offball_fixed_point_of_scaling'),
    ('### its header: the general law uncompiled', s('Core/ScalingTraceShadow.lean'), "general law is the bank's derivation and is uncompiled"),
    ('B310 module -- the signed count', s('Core/SmearCollapseShadow.lean'), 'def offBallFixed (p n t m : Nat) : Nat :='),
    ('### the identity theorem', s('Core/SmearCollapseShadow.lean'), 'theorem signed_count_at_the_identity_is_the_dimension'),
    ('### the collapse theorem', s('Core/SmearCollapseShadow.lean'), 'theorem identity_term_survives_alone'),
    ('B270 module -- the polarity idiom', s('Core/BallAbsorptionShadow.lean'), 'def hasLiveStep (p n k : Nat) : Bool :='),
    ('### and why it exists: a dead operator', s('Core/BallAbsorptionShadow.lean'), 'THIS PART, PART (1) WOULD BE COMPATIBLE WITH A DEAD OPERATOR'),
    # ### ---- the certification file and the build's own declared procedure
    ('AllPrints.lean -- the last import', s('AllPrints.lean'), 'import TopLevelSilenceShadow'),
    ('### the last print', s('AllPrints.lean'), '#print axioms TopLevelSilenceShadow.only_the_candidate_count_is_zero'),
    ('the toolchain pin', s('lean-toolchain'), 'v4.29.1'),
    ("the repo's build sentence", s('README.md'), 'compiles each module standalone'),
    ('b315 -- the coverage gate is supposed to fail', t('b315_coverage_gate.py'), 'IT IS SUPPOSED TO FAIL'),
    ('b310 registration -- the refusal that travels with a build', d('b310_registration_2026-09-03.txt'), 'IT CERTIFIES ARITHMETIC AND NOT'),
    # ### ---- the rows and the ledger row this act bears on
    ('CORRESPONDENCE row 130', s('CORRESPONDENCE.md'), '| 130 | THE SCALING TRACE, COMPUTED (b309)'),
    ('### row 131', s('CORRESPONDENCE.md'), '| 131 | THE MECHANISM: NO OFF-BALL FIXED POINT (b309)'),
    ('### row 132', s('CORRESPONDENCE.md'), '| 132 | THE SMEAR COLLAPSES (b310)'),
    ('### row 133', s('CORRESPONDENCE.md'), '| 133 | THE FIXED-POINT SENTENCE, AND ITS BEARING (b310)'),
    ('### the last row before this act', s('CORRESPONDENCE.md'), '| 169 | THE NEGATIVE CONTROL UNDER THE DISCRIMINATING FAMILY'),
    ("the faces ledger's fixed-point-silence row", os.path.join(PP, 'FACES_LEDGER.md'), '| F5 | F5 -- the fixed-point silence'),
    # ### ---- the lore's anchors, and the order naming this act next
    ("lore_rules -- the last mechanized entry's close", t('lore_rules.py'), "discharged='b328'),"),
    ("### the fixture list's last line", t('lore_rules.py'), "('phase condition (b326/b328)', _fixture_phase_condition)]:"),
    ('b328 named this act next', d('b328_the_discriminating_family.txt'), 'THE FINITE-SIDE SEALING MODULE IS NAMED NEXT BY THE ORDER'),
    ('b327 named it too', d('b327_the_faces_ledger.txt'), 'THEN THE FINITE-SIDE SEALING MODULE'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b329_extract.py -- THE FINITE-SIDE SEAL. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
    rec('=' * 100)
    missing, paths_missing = 0, 0
    for lbl, path, frag in WANTED:
        rec('### ==== %s' % lbl)
        if not os.path.exists(path):
            paths_missing += 1
            rec('###      %s | ### **FILE NOT PRESENT**' % path)
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        hits = [(i + 1, ln) for i, ln in enumerate(body) if frag in ln]
        short = path.replace(PP, '<papers>').replace(SIDE, '<side>').replace(ROOT, '<relay>').replace(chr(92), '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    print('\n'.join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
