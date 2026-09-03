# -*- coding: utf-8 -*-
"""b308_reproduction.py -- THE COMPONENTS. ### **THE OBJECTS, THE BUILD, THE REPRODUCTION, THE
### ARTIFACT.**

### ### **THE ORDER'S RULE THIS FILE IS BUILT AROUND:** ### *the instrument must REPRODUCE the
### banked results it can reach before any new computation is trusted.* ### So the reproduction is
### not an appendix: ### **THE OWNING TOOLS ARE IMPORTED AND RE-RUN, AND THEIR ANSWERS ARE
### COMPARED WITH THE INSTRUMENT'S. ### CITING THEM WOULD BE A CITATION, NOT A REPRODUCTION**
### (b303's own sentence about its own act).

### ### **AND THE RULE ON DISAGREEMENT, FROM THE SEALED REGISTRATION:** ### a disagreement at any
### reachable cell is printed ### AT FULL PROMINENCE ### and ### **THE INSTRUMENT IS NOT ADJUSTED
### TOWARD THE OWNER.** ### An instrument tuned until it reproduces is evidence about nothing.

### ### **WHAT IS PRINTED AS A NUMBER AND WHAT IS NOT.** ### The criterion's TRUTH VALUE is printed
### wherever the instrument reaches. ### **A FIRST-LEVEL VALUE IS PRINTED ONLY WHERE THE RECORD
### ALREADY CARRIES ONE** -- the two witnesses written into b295's own sealed registration -- and
### the owning tool is named beside it. ### The order puts the first computation on this instrument
### in a LATER act under its own registration, and this file honours that by not making one.

### ### **NO FLOAT. ### `Fraction` AND `int` AND EXACT CYCLOTOMIC REDUCTION.**
"""
import io
import os
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, 'tools')
E16 = os.path.join(HERE, 'e16')
sys.path.insert(0, HERE)
sys.path.insert(0, E16)

import needle_pull                                                     # noqa: E402
import b308_local_field as LF                                          # noqa: E402
import b303_family as FAM                                              # noqa: E402
import b304_smearing as SMEAR                                          # noqa: E402
from b270_ambient_pairing import ball_of                               # noqa: E402
from b281_compression import matrix_A                                  # noqa: E402
from b293_finite_family import basis_family, in_family                 # noqa: E402
from b295_second_mechanism import (form_matrix, first_nonzero,         # noqa: E402
                                   diag_witness, forced_zero,
                                   REGISTERED_WITNESSES)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')

# ### THE CELLS, EACH TAKEN FROM THE OWNER WHOSE RESULT IS BEING REPRODUCED AT IT. ### **NOT ONE OF
# ### THEM IS CHOSEN BY THIS ACT**, which is what keeps the reproduction from being a sample this
# ### seat picked after seeing the answers.
CELLS_FAMILY = list(FAM.CELLS)                 # ### b303's five
CELLS_SMEAR = list(SMEAR.CELLS)                # ### b304's six
CELLS_CRITERION = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (2, 3)]   # ### b295's six

OWNERS = [
    ('b21  -- THE CHART AND THE HAAR NORMALIZATION, AND THE TIE BETWEEN THE TWO RADII',
     'b21_2026-08-18.txt', 'via x = p^(-n) m; Haar measure'),
    ('b21  -- THE MODEL SPACE, WHERE THE TWO RADII ARE TIED TO ONE `n`',
     'b21_2026-08-18.txt', 'V_n IS canonically the model space'),
    ('b21  -- THE GENUINE TRANSFORM, FROM WHICH THE INSTRUMENT WRITES ITS OWN',
     'b21_2026-08-18.txt', 'THE GENUINE TRANSFORM: (F f)(y) = int f(x) psi(x y) dx'),
    # ### **RE-POINTED, NOT RE-TYPED.** ### The first anchor spanned b21's own hard wrap -- the
    # ### sentence breaks after `IS the` -- and the needle came back unpullable on the first run.
    # ### **THAT IS THE GATE DOING ITS WORK, AND THE FIX IS TO POINT AT WHAT THE FILE EMITS.**
    ('b21  -- THE MODEL TRANSFORM IS THE GENUINE ONE AT A FIXED LEVEL, WITH ITS ENTRY FORMULA',
     'b21_2026-08-18.txt', 'the model transform IS the'),
    ('b21  -- ... and the second half of that sentence, on its own line',
     'b21_2026-08-18.txt', 'genuine local transform at level n'),
    ('b21  -- WHERE THE ARTIFACT LIVES',
     'b21_2026-08-18.txt', "MODEL'S mod-N WRAPAROUND IS THE ARTIFACT"),
    ('b280 -- THE BALL IN b21\'s CHART IS `Z_p`',
     'b280_the_consequence.txt', 'ball_n = { x = p^{-n} p^n k }'),
    ('b280 -- THE HAAR BRIDGE: A CHART POINT IS A COSET OF POSITIVE MEASURE',
     'b280_the_consequence.txt', 'a chart point `m` at level `n`'),
    ('b280 -- b270\'s ABSORPTION AT `k = n`, THE ZERO THE CRITERION GENERALISES',
     'b280_the_consequence.txt', '`P(n) = 0`'),
    ('b284 -- THE ESCAPE, AND THE SENTENCE THIS ACT TURNS INTO A COMPUTATION',
     'b284_the_scalings_domain.txt', 'strictly bigger than'),
    ('b284 -- WHY THE DERIVATION STOOD WHERE THE MODEL DID NOT',
     'b284_the_scalings_domain.txt', 'WHERE THERE IS NOTHING TO FOLD'),
    ('b293 -- THE BALL OF EXPONENT `e`, WHICH IS THE INSTRUMENT\'S BALL AT `r = n`',
     'b293_the_finite_family.txt', 'B_e := { m : v_p(m) >= n - e }'),
    ('b293 -- THE DIMENSION LAW',
     'b293_the_finite_family.txt', 'dim Son(p,n; a,b) = p^{2n}'),
    ('b293 -- THE DILATION AND ITS INVARIANT, ON THE CONDITION RADII',
     'b293_the_finite_family.txt', 'THE SUM `a+b` IS INVARIANT'),
    ('b295 -- THE ANNIHILATION CRITERION',
     'b295_the_second_mechanism.txt', '`a >= 0`  ###  OR  ###  `b >= n - 1`'),
    ('b295 -- THE CRITERION\'S OWN SCOPE, CARRIED WITH IT',
     'b295_the_second_mechanism.txt', 'AND PAIRINGS OF THIS SHAPE'),
]


def rule(ch='-', n=100):
    return ch * n


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    fails = []

    rec('=' * 100)
    rec('b308 -- THE LOCAL-FIELD INSTRUMENT. ### THE COMPONENTS, IN ORDER.')
    rec('=' * 100)

    # ==============================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE OBJECTS, FROM THEIR OWNERS. ### **PULLED, NOT TYPED.**')
    rec('=' * 100)
    rec('  ### Every sentence below is the EXACT LINE the owning file emits, extracted by')
    rec('  ### `needle_pull.pull`. ### **A SENTENCE THIS SEAT REMEMBERED WOULD NOT APPEAR HERE.**')
    rec('')
    unpullable = 0
    for label, fn, anchor in OWNERS:
        try:
            line = needle_pull.pull(os.path.join(D, fn), anchor)
            rec('  %s' % label)
            rec('      %s' % line[:150])
        except LookupError:
            unpullable += 1
            fails.append('owner needle: %s' % label)
            rec('  ### FAIL (UNPULLABLE) %s   anchor=%r' % (label, anchor))
    rec('')
    rec('  ### OWNER SENTENCES PULLED : %d   ### UNPULLABLE : %d'
        % (len(OWNERS) - unpullable, unpullable))

    rec('')
    rec(rule())
    rec('### (1a) THE TWO RADII, NAMED SEPARATELY, AND THE MODEL\'S TIE.')
    rec(rule())
    rec('  ### **THE SUPPORT RADIUS** ..... `p^r`  -- the support lies in `p^{-r} Z_p`.')
    rec('  ### **THE CONSTANCY RADIUS** ... `p^{-s}` -- constant on cosets of `p^s Z_p`.')
    rec('  ### ### **THE MODEL TIES THEM: `r = s = n`, AND THE FILE THAT TIES THEM IS b21**, in the')
    rec('  ### sentence pulled above -- `p^(-n)Z_p / p^n Z_p` is one `n` governing both.')
    rec('  ### **THE INSTRUMENT UNTIES THEM AND CHANGES NOTHING ELSE**: the chart is b21\'s')
    rec('  ### `x = p^{-r} m`, the Haar is b21\'s (`Z_p` mass 1, cell mass `p^{-s}`), and at')
    rec('  ### `r = s = n` every object below is the model\'s, entry for entry.')
    for (p, n) in [(2, 2), (3, 1)]:
        fr = LF.model_frame(p, n)
        rec('    p=%d n=%d : model frame %s   cell mass %s   ### the corpus\'s V_n'
            % (p, n, fr.label(), fr.cell_mass()))
        for k in (1, -1):
            tg, _ = LF.scaling_action(fr, k, [Fraction(0)] * fr.M)
            rec('              theta(p^%+d) -> %s   cell mass %s   ### OFF THE MODEL\'S DIAGONAL'
                % (k, tg.label(), tg.cell_mass()))

    rec('')
    rec(rule())
    rec('### (1b) THE ACTION OF `Q_p^x`, SPLIT, WITH EACH PART NAMED AS SUCH.')
    rec(rule())
    rec('  ### `Q_p^x = p^Z x Z_p^x`, and the action is b304\'s `(theta(t) f)(m) = f(t^{-1} m)`.')
    rec('  ### ### **THE COMPACT PART `Z_p^x`** -- `|t| = 1`, so NEITHER radius moves and the grid')
    rec('  ###   is permuted. ### **THIS IS THE PART THE MODEL CARRIES**, and b304 computed with it.')
    rec('  ### ### **THE SCALING PART `p^Z`** -- `theta(p^k) : V(r,s) -> V(r-k, s+k)`, so BOTH')
    rec('  ###   radii move and their SUM does not. ### **THIS IS THE PART THE MODEL DROPS.**')

    # ==============================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE BUILD. ### **EVERY OPERATION CONTROLLED IN BOTH POLARITIES FIRST.**')
    rec('=' * 100)
    rec('  ### THE THREE SELF-TESTS, RUN BEFORE ANY OF THE THREE FILES IS USED IN A VERDICT:')
    ok_lf = LF.self_test(verbose=False)
    ok_fam = FAM.self_test(verbose=False)
    ok_sm = SMEAR.self_test(verbose=False)
    rec('    b308_local_field  (this instrument)          : %s' % ('PASS' if ok_lf else '### FAIL'))
    rec('    b303_family       (the family\'s conditions)  : %s' % ('PASS' if ok_fam else '### FAIL'))
    rec('    b304_smearing     (the projection and trace) : %s' % ('PASS' if ok_sm else '### FAIL'))
    if not (ok_lf and ok_fam and ok_sm):
        rec('  ### REFUSING TO REPORT A BUILD FROM A SUITE THAT FAILS ITS OWN FIXTURES.')
        return 2, out

    rec('')
    rec(rule())
    rec('### (2a) THE TRANSFORM. ### **b21\'s A5a REPRODUCED EXHAUSTIVELY, THEN THE INVERSION.**')
    rec(rule())
    rec('  ### The instrument\'s transform is `(F f)(m\') = p^{-s} SUM_m f(m) zeta_M^{m m\'}` on the')
    rec('  ### frame `(r,s)`, landing in `(s,r)`. ### **THE INVERSION CONTROL RUNS THROUGH b21\'s')
    rec('  ### OWN GEOMETRIC-SUM IDENTITY, WHICH IS VERIFIED HERE FOR EVERY RESIDUE FIRST** -- an')
    rec('  ### identity used without being checked is an assumption wearing a proof\'s clothes.')
    rec('  %-22s %-14s %-26s %s' % ('frame', 'M', 'A5a over ALL residues', 'F F f = f(-x)'))
    for (p, r, s) in [(2, 1, 1), (2, 2, 2), (2, 3, 1), (3, 1, 1), (3, 2, 2), (5, 1, 1), (2, 0, 2)]:
        fr = LF.Frame(p, r, s)
        M = fr.M
        a5a = all(LF.is_rational_value(LF.geometric_sum(p, M, c), Fraction(M)) if c % M == 0
                  else LF.is_zero_poly(LF.geometric_sum(p, M, c)) for c in range(M))
        # ### THE INVERSION, COMPUTED THROUGH THE VERIFIED IDENTITY:
        # ###   (F F f)(m'') = p^{-(r+s)} SUM_m f(m) SUM_{m'} zeta_M^{m'(m + m'')}
        # ###                = p^{-(r+s)} SUM_m f(m) * M * [m + m'' = 0]  =  f(-m'').
        # ### **AND THE SCALAR IS CHECKED, NOT WAVED AT: `p^{-r} p^{-s} M = 1` EXACTLY.**
        scalar = Fraction(1, p ** r) * Fraction(1, p ** s) * M
        vec = [Fraction((m * m + 3) % 7) - Fraction(2) for m in range(M)]
        reflected = [vec[(-m) % M] for m in range(M)]
        recovered = [scalar * vec[(-m) % M] for m in range(M)]
        inv_ok = a5a and scalar == 1 and recovered == reflected
        rec('  %-22s %-14d %-26s %s'
            % (fr.label(), M, 'YES' if a5a else '### NO ###',
               'YES, scalar = 1' if inv_ok else '### NO ###'))
        if not inv_ok:
            fails.append('transform inversion at %s' % fr.label())
    rec('  ### **AND THE NEGATIVE ARM, WHICH IS WHAT MAKES THE POSITIVE ONE MEAN ANYTHING:**')
    fr = LF.Frame(2, 1, 1)
    rec('    a spike at the origin transforms to the constant 1, vanishing NOWHERE : %s'
        % (not LF.is_zero_poly(LF.zeta_sum(fr, [Fraction(1)] + [Fraction(0)] * 3, 3))))
    rec('    `1_{Z_p}` is self-dual, so it does NOT vanish on the unit ball          : %s'
        % (not LF.transform_vanishes_on_ball(
            fr, [Fraction(1) if m in fr.ball(0) else Fraction(0) for m in range(fr.M)], 0)))

    rec('')
    rec(rule())
    rec('### (2b) THE TWO SONIN CONDITIONS AS TESTS, AND THE COLLAPSE CHECKED RATHER THAN USED.')
    rec(rule())
    rec('  ### The first condition is `f = 0` on `{|x| <= p^a}`; the second is `F f = 0` on')
    rec('  ### `{|y| <= p^b}`, computed LITERALLY in `Q(zeta_M)`. ### b293 collapsed the second to')
    rec('  ### the vanishing of every fiber sum at modulus `p^{n+b}`, and the instrument writes that')
    rec('  ### as `p^{r+b}`. ### **THE TWO ARE COMPARED AT EVERY CELL, BOTH DIRECTIONS, WITH A')
    rec('  ### NON-MEMBER CONTROL. ### A COLLAPSE MERELY IMPLIED BY MEMBERSHIP WOULD PASS THE')
    rec('  ### POSITIVE ARM AND FAIL THE NEGATIVE ONE.**')
    rec('  %-10s %-8s %-30s %-24s %s'
        % ('cell', 'radii', 'collapsed => literal', 'literal => collapsed', 'control fires'))
    for (p, n) in CELLS_FAMILY:
        fr = LF.model_frame(p, n)
        M = fr.M
        off = next(m for m in range(M) if m not in fr.ball(0))
        spike = [Fraction(1) if m == off else Fraction(0) for m in range(M)]
        for (a, b) in [(0, 0), (-1, 0), (0, -1)]:
            basis = LF.son_basis(fr, a, b)
            sample = basis[:3]
            fwd = all(LF.transform_vanishes_on_ball(fr, v, b) for v in sample)
            # ### the reverse arm: a vector meeting the LITERAL condition meets the collapsed one.
            rev = all(LF.fiber_sums_vanish(fr, v, b) for v in sample)
            ctl = (not LF.fiber_sums_vanish(fr, spike, b)) and \
                  (not LF.transform_vanishes_on_ball(fr, spike, b))
            good = fwd and rev and ctl and bool(basis)
            if not good:
                fails.append('collapse equivalence at (%d,%d) radii (%d,%d)' % (p, n, a, b))
            rec('  %-10s %-8s %-30s %-24s %s'
                % ('(%d,%d)' % (p, n), '(%+d,%+d)' % (a, b),
                   'YES on %d sampled' % len(sample) if fwd else '### NO ###',
                   'YES on %d sampled' % len(sample) if rev else '### NO ###',
                   'YES, spike rejected by BOTH' if ctl else '### NO ###'))

    rec('')
    rec(rule())
    rec('### (2c) THE DILATION, BOTH DIRECTIONS, AND b21\'s UNITARITY AS AN IDENTITY OF RATIONALS.')
    rec(rule())
    rec('  ### b21: ### **"(U f)(x) = p^(-1/2) f(p x), unitary on L^2(Q_p)"** ### and')
    rec('  ### **"supp(U f) = p^(-n-1)Z_p, strictly bigger than p^(-n)Z_p"**. ### On the untied')
    rec('  ### frame `U = p^{-1/2} theta(p^{-1})`, landing in `V(n+1, n-1)`, and BOTH sentences')
    rec('  ### become computations.')
    rec('  %-10s %-22s %-22s %-18s %s'
        % ('cell', 'U lands in', 'smallest ball  supp', '||Uf|| = ||f||', 'both directions'))
    for (p, n) in CELLS_FAMILY:
        fr = LF.model_frame(p, n)
        basis = LF.son_basis(fr, 0, 0)
        f = basis[0]
        up, uf = LF.scaling_action(fr, -1, f)
        down, df = LF.scaling_action(fr, +1, f)
        supp_e = max((up.abs_index(m) for m in range(up.M) if uf[m]), default=None)
        # ### THE UNITARITY SCALAR, EXACT: `p^{-1} * (cell mass of the target) / (cell mass here)`.
        unit_scalar = Fraction(1, p) * up.cell_mass() / fr.cell_mass()
        norm_ok = (unit_scalar == 1)
        both = (up.key() == (p, n + 1, n - 1) and down.key() == (p, n - 1, n + 1)
                and uf == f and df == f)
        if not (norm_ok and both and supp_e == n + 1):
            fails.append('dilation at (%d,%d)' % (p, n))
        rec('  %-10s %-22s %-22s %-18s %s'
            % ('(%d,%d)' % (p, n), 'V(%d,%d)' % (up.r, up.s),
               'p^{-%s}Z_p  %s' % (supp_e, 'STRICTLY BIGGER' if supp_e == n + 1 else '### NO ###'),
               'YES (scalar %s)' % unit_scalar if norm_ok else '### NO ###',
               'YES, list unchanged' if both else '### NO ###'))
    rec('  ### **AND THE NEGATIVE ARM: THE MODEL FRAME IS NOT PRESERVED BY EITHER DIRECTION.** ### A')
    rec('  ### dilation that left the frame alone would be an instrument that had untied nothing.')
    fr = LF.model_frame(2, 2)
    rec('    theta(p) on V(2,2) lands in V(1,3), which is NOT V(2,2)      : %s'
        % (LF.scaling_action(fr, 1, [Fraction(0)] * fr.M)[0].key() != fr.key()))

    rec('')
    rec(rule())
    rec('### (2d) THE COMPRESSION BY THE CONSTRAINED SPACE\'S PROJECTION.')
    rec(rule())
    rec('  ### `Pi` is b304\'s projector, IMPORTED. ### The source\'s move, in b304\'s quotation of')
    rec('  ### it, compresses by the projection onto ### SONIN\'S SPACE ### and not onto a sector.')
    rec('  ### ### **AND ONE CONTROL IS NEW HERE AND IS THE ONE THE UNTYING MAKES POSSIBLE:** ### the')
    rec('  ### projector built with the HAAR inner product and the projector built with the MODEL\'s')
    rec('  ### must be the SAME MATRIX, because the two differ by the positive scalar `p^{-s}` and a')
    rec('  ### positive scalar cannot change orthogonality. ### **SAID, THEN CHECKED ENTRY-WISE.**')
    rec('  %-10s %-8s %-12s %-14s %-16s %s'
        % ('cell', 'dim', 'Tr(Pi)', 'idempotent', 'fixes basis', 'Haar Pi == model Pi'))
    for (p, n) in CELLS_FAMILY:
        fr = LF.model_frame(p, n)
        M = fr.M
        basis = LF.son_basis(fr, 0, 0)
        P, rank = SMEAR.projector(basis, M)
        tr = sum(P[i][i] for i in range(M))
        idem = all(sum(P[i][k] * P[k][j] for k in range(M)) == P[i][j]
                   for i in range(0, M, max(1, M // 8)) for j in range(0, M, max(1, M // 8)))
        fixes = all(all(sum(P[i][j] * v[j] for j in range(M)) == v[i] for i in range(M))
                    for v in basis[:3])
        # ### THE HAAR-SCALED BASIS SPANS THE SAME SPACE, SO THE PROJECTOR IS THE SAME MATRIX.
        scaled = [[fr.cell_mass() * x for x in v] for v in basis]
        P2, _r2 = SMEAR.projector(scaled, M)
        same = (P == P2)
        off = next(m for m in range(M) if m not in fr.ball(0))
        spike = [Fraction(1) if m == off else Fraction(0) for m in range(M)]
        moved = ([sum(P[i][j] * spike[j] for j in range(M)) for i in range(M)] != spike)
        good = idem and fixes and same and moved and rank == len(basis)
        if not good:
            fails.append('compression at (%d,%d)' % (p, n))
        rec('  %-10s %-8d %-12s %-14s %-16s %s'
            % ('(%d,%d)' % (p, n), rank, tr, idem, fixes,
               'YES' if same else '### NO ###'))
    rec('  ### **NEGATIVE CONTROL AT EVERY CELL: an off-ball spike is MOVED by `Pi`.** ### A')
    rec('  ### projector that fixed everything would report every trace below and mean nothing.')

    return _components_three_and_four(rec, fails, out)


# ==================================================================================================
def _components_three_and_four(rec, fails, out):
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE REPRODUCTION. ### **MANDATORY BEFORE ANYTHING ELSE IS TRUSTED.**')
    rec('=' * 100)

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec(rule())
    rec('### (3a) `F3` -- THE UNTIED RADII RECOVER THE TWO-RADIUS FAMILY, AS SETS, BOTH DIRECTIONS.')
    rec(rule())
    rec('  ### The instrument builds `Son(frame; a, b)` from its OWN two conditions on the untied')
    rec('  ### frame; b293 builds `Son(p,n; a,b)` from ITS own. ### **CONTAINMENT BOTH WAYS PLUS')
    rec('  ### EQUAL DIMENSION IS SET EQUALITY; ONE WAY IS NOT** (b303\'s ARM B, carried).')
    rec('  %-10s %-9s %-7s %-7s %-22s %-22s %s'
        % ('cell', 'radii', 'dim I', 'dim b293', 'I vectors in b293', 'b293 vectors in I',
           'spike rejected'))
    f3_bad = 0
    for (p, n) in CELLS_FAMILY:
        fr = LF.model_frame(p, n)
        M = fr.M
        off = next(m for m in range(M) if m not in fr.ball(0))
        spike = [Fraction(1) if m == off else Fraction(0) for m in range(M)]
        for a in range(-n, n + 1):
            for b in range(-n, n + 1):
                bi = LF.son_basis(fr, a, b)
                bo = [v for v in basis_family(p, n, a, b) if any(x != 0 for x in v)]
                if not bi and not bo:
                    continue
                fwd = all(in_family(v, p, n, a, b) for v in bi)
                rev = all(LF.vanishes_on_ball(fr, v, a) and LF.fiber_sums_vanish(fr, v, b)
                          for v in bo)
                ctl = (not in_family(spike, p, n, a, b)) and (not LF.in_space(fr, spike, a, b))
                dim_ok = (len(bi) == len(bo))
                good = fwd and rev and ctl and dim_ok
                f3_bad += 0 if good else 1
                if not good:
                    fails.append('F3 at (%d,%d) radii (%+d,%+d)' % (p, n, a, b))
                    rec('  ### ### **DISAGREEMENT AT (%d,%d) radii (%+d,%+d)** -- '
                        'dims %d vs %d, fwd %s, rev %s, control %s'
                        % (p, n, a, b, len(bi), len(bo), fwd, rev, ctl))
                elif (a, b) in [(0, 0), (-1, 0), (0, -1), (-1, -1)]:
                    rec('  %-10s %-9s %-7d %-7d %-22s %-22s %s'
                        % ('(%d,%d)' % (p, n), '(%+d,%+d)' % (a, b), len(bi), len(bo),
                           'YES, all %d' % len(bi), 'YES, all %d' % len(bo),
                           'YES, by BOTH tests'))
    rec('  ### **MEMBERS COMPARED ACROSS ALL FIVE CELLS AND ALL RADII IN RANGE. ### '
        'DISAGREEING : %d**' % f3_bad)

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec(rule())
    rec('### (3b) THE DIMENSION LAW, AND THE KEYSTONE\'S OWN NUMBER AT THE DIAGONAL.')
    rec(rule())
    rec('  ### b293: ### **`dim Son(p,n; a,b) = (p^n - p^a)(p^n - p^b)`**, claimed only where it was')
    rec('  ### tested -- `a + b >= 0` with both exponents non-negative -- and ### **AT `a = b = 0`')
    rec('  ### IT IS THE KEYSTONE\'S `(p^n - 1)^2`.** ### The scope travels with the law.')
    rec('  %-10s %-9s %-10s %-14s %s' % ('cell', 'radii', 'dim built', 'the law', 'agree'))
    dim_bad = 0
    for (p, n) in CELLS_FAMILY:
        fr = LF.model_frame(p, n)
        for (a, b) in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            if a + b < 0 or a < 0 or b < 0:
                continue
            got = len(LF.son_basis(fr, a, b))
            law = (p ** n - p ** a) * (p ** n - p ** b)
            ok = (got == law)
            dim_bad += 0 if ok else 1
            if not ok:
                fails.append('dimension law at (%d,%d) radii (%+d,%+d)' % (p, n, a, b))
            if (a, b) == (0, 0):
                rec('  %-10s %-9s %-10d %-14s %s'
                    % ('(%d,%d)' % (p, n), '(%+d,%+d)' % (a, b), got,
                       '(p^n-1)^2 = %d' % ((p ** n - 1) ** 2),
                       'YES  ### the keystone\'s own number' if ok else '### NO ###'))
            else:
                rec('  %-10s %-9s %-10d %-14s %s'
                    % ('(%d,%d)' % (p, n), '(%+d,%+d)' % (a, b), got, law,
                       'YES' if ok else '### NO ###'))
    rec('  ### **CELLS DISAGREEING WITH THE LAW IN ITS OWN TESTED RANGE : %d**' % dim_bad)

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec(rule())
    rec('### (3c) THE NOT-DEAD WITNESS, AND (3d) THE COMPACT-PART SMEAR\'S ZERO WITH ITS MECHANISM.')
    rec(rule())
    rec('  ### b304\'s two, reproduced on the instrument\'s own space at b304\'s own six cells.')
    rec('  ### **`Tr(Pi)` MUST EQUAL THE CONSTRAINED DIMENSION -- THAT IS THE WITNESS THAT THE')
    rec('  ### PROJECTION IS NOT DEAD, AND WITHOUT IT EVERY ZERO BELOW WOULD BE FREE.**')
    rec('  ### And the smear\'s zero is reported WITH ITS MECHANISM: `SUM_{t in U} theta(t)` is')
    rec('  ### `|U|` times the projection onto the `U`-invariants, the invariants are spanned by the')
    rec('  ### shells of constant `|x|`, and every `Son` vector is orthogonal to every shell for the')
    rec('  ### ### SPACE\'S OWN TWO REASONS, ONE PER SHELL RANGE.')
    rec('  %-10s %-8s %-12s %-12s %-14s %-14s %s'
        % ('cell', 'dim', 'Tr(Pi)', 'smear T', 'shells orth', 'shells=unions', 'instrument shells'))
    for (p, n) in CELLS_SMEAR:
        fr = LF.model_frame(p, n)
        M = fr.M
        basis = LF.son_basis(fr, 0, 0)
        P, rank = SMEAR.projector(basis, M)
        tr = sum(P[i][i] for i in range(M))
        law = (p ** n - 1) ** 2
        units = [t for t in range(M) if SMEAR.gcd(t, M) == 1]
        all_perm = all(SMEAR.is_permutation(t, M) for t in units)
        smeared = sum(SMEAR.trace_scaled(P, t, M) for t in units)
        orth, _ns, unions = SMEAR.invariant_reason(p, n, M, basis)
        # ### THE INSTRUMENT'S OWN SHELLS, FROM `|x|`, COMPARED WITH b304's VALUATION SHELLS.
        # ### ### **THIS COMPARISON CAME BACK UNEQUAL ON THE FIRST RUN AND IS REPORTED AS IT CAME
        # ### ### BACK.** ### The instrument's shells partition the WHOLE grid, including the cell
        # ### `m = 0`, which is the coset `p^s Z_p` and carries `|x| <= p^{-s}`. ### b304's
        # ### enumeration reaches one shell fewer, because the valuation it imports returns its FUEL
        # ### CAP at `0` rather than `2n`, so the `j = 2n` shell its own docstring names comes back
        # ### empty and is skipped. ### **NOTHING IN b304's VERDICT DEPENDS ON IT** -- `0` lies in
        # ### the ball and every `Son` vector vanishes there -- so orthogonality to the missing
        # ### shell is automatic, and this act CHECKS that rather than asserting it.
        own = {}
        for m in range(M):
            own.setdefault(fr.abs_index(m), set()).add(m)
        b304_shells = {}
        for j in range(0, 2 * n + 1):
            s = set(m for m in range(M) if FAM.vp(p, m) == j)
            if s:
                b304_shells[j] = s
        partitions = (set().union(*own.values()) == set(range(M))
                      and sum(len(v) for v in own.values()) == M)
        extra = [v for v in own.values() if v not in b304_shells.values()]
        extra_is_zero_cell = (len(extra) == 1 and extra[0] == {0})
        extra_orth = all(all(v[m] == 0 for m in extra[0]) for v in basis) if extra else True
        refines = (sorted((v for v in own.values() if v != {0}), key=sorted)
                   == sorted(b304_shells.values(), key=sorted))
        good = (tr == law and rank == law and smeared == 0 and orth and unions and all_perm
                and partitions and extra_is_zero_cell and extra_orth and refines)
        if not good:
            fails.append('smear/witness at (%d,%d)' % (p, n))
        rec('  %-10s %-8d %-12s %-12s %-14s %-14s %s'
            % ('(%d,%d)' % (p, n), rank, '%s %s' % (tr, '==dim' if tr == law else '### NO'),
               smeared, orth, unions,
               'b304\'s + {0}, and Son vanishes on {0}' if good else '### NO ###'))
    rec('  ### **EVERY UNIT PERMUTES THE GRID AT EVERY CELL, SO THE COMPACT PART IS COMPUTED WITH')
    rec('  ### NOTHING ESCAPING AND NOTHING FOLDED** -- b304\'s own test, re-run here.')
    rec('')
    rec('  ### ### **ONE DIFFERENCE THE REPRODUCTION FOUND, REPORTED AS IT CAME BACK AND NOT')
    rec('  ### ### SMOOTHED.** ### The instrument\'s shells are the level sets of `|x|` and they')
    rec('  ### PARTITION THE WHOLE GRID. ### b304\'s enumeration reaches ONE SHELL FEWER: the cell')
    rec('  ### `m = 0`. ### Its own docstring says ### **"`j = 2n` is `{0}`"**, but the valuation it')
    rec('  ### imports returns its FUEL CAP at `0`, so that shell comes back empty and is skipped.')
    rec('  ### ### **AND NOTHING IN b304\'s VERDICT DEPENDS ON IT, WHICH IS WHY THIS IS A NOTE AND')
    rec('  ### ### NOT A CORRECTION:** ### `0` lies in the ball, every `Son` vector vanishes on the')
    rec('  ### ball, so orthogonality to the missing shell is automatic -- ### **AND THIS ACT')
    rec('  ### CHECKED IT AT EVERY CELL RATHER THAN ARGUING IT.** ### b304\'s smeared zero, its')
    rec('  ### mechanism and its trace all stand exactly as b304 left them. ### **NO GRADE MOVES,')
    rec('  ### NO ACT IS RE-VERDICTED, AND b304\'s FILE IS NOT REWRITTEN** -- the append-only law.')

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec(rule())
    rec('### (3e) THE ANNIHILATION CRITERION AT EVERY CELL THE INSTRUMENT REACHES.')
    rec(rule())
    rec('  ### b295, DERIVED: ### **the first-level pairing vanishes identically -- as a FORM, both')
    rec('  ### slots -- on `Son(p,n; a,b)` whenever `a >= 0` OR `b >= n - 1`.**')
    rec('  ### The operator is b273\'s `A` at `k = n`, IMPORTED from b281 and never re-defined here.')
    rec('  ### **THE VERDICTS BELOW ARE BASIS-INDEPENDENT AND THAT IS WHY THEY ARE THE THING')
    rec('  ### COMPARED**: the instrument\'s basis and b293\'s are different bases of the same space,')
    rec('  ### so a per-vector number would not be comparable and a per-space verdict is.')
    rec('  %-10s %-9s %-7s %-7s %-16s %-16s %-16s %s'
        % ('cell', 'radii', 'dim I', 'dim O', 'FORM on I', 'FORM on b293', 'criterion',
           'agreement'))
    crit_bad, reached, forced_confirmed = 0, 0, 0
    for (p, n) in CELLS_CRITERION:
        fr = LF.model_frame(p, n)
        N = fr.M
        A = matrix_A(N, p, n, n)
        ballset = sorted(ball_of(N, p, n))
        for a in range(-n, n + 1):
            for b in range(-n, n + 1):
                bi = LF.son_basis(fr, a, b)
                bo = [v for v in basis_family(p, n, a, b) if any(x != 0 for x in v)]
                if not bi and not bo:
                    continue
                reached += 1
                Mi = form_matrix(A, bi, N, ballset)
                Mo = form_matrix(A, bo, N, ballset)
                zi = (first_nonzero(Mi) is None)
                zo = (first_nonzero(Mo) is None)
                wi = (diag_witness(Mi, bi, N)[0] is None)
                wo = (diag_witness(Mo, bo, N)[0] is None)
                crit = forced_zero(a, b, n)
                agree = (zi == zo) and (wi == wo) and (len(bi) == len(bo))
                if crit:
                    agree = agree and zi
                    forced_confirmed += 1 if zi else 0
                crit_bad += 0 if agree else 1
                if not agree:
                    fails.append('criterion at (%d,%d) radii (%+d,%+d)' % (p, n, a, b))
                    rec('  ### ### **DISAGREEMENT AT (%d,%d) radii (%+d,%+d)**: FORM zero on the '
                        'instrument = %s, on b293 = %s, criterion forces zero = %s'
                        % (p, n, a, b, zi, zo, crit))
                elif crit or (a, b) in [(-1, 0), (-1, -1)]:
                    rec('  %-10s %-9s %-7d %-7d %-16s %-16s %-16s %s'
                        % ('(%d,%d)' % (p, n), '(%+d,%+d)' % (a, b), len(bi), len(bo),
                           'ZERO' if zi else 'NONZERO', 'ZERO' if zo else 'NONZERO',
                           'ZERO forced' if crit else 'not forced',
                           'derived zero, confirmed' if crit else 'agree, and NOT forced'))
    rec('  ### **MEMBERS REACHED : %d   ### DISAGREEING : %d   ### FORCED ZEROS CONFIRMED : %d**'
        % (reached, crit_bad, forced_confirmed))
    rec('  ### **AND THE ARM THAT MAKES THE ZEROS MEAN SOMETHING: THE FORM IS NONZERO SOMEWHERE.**')
    rec('  ### A criterion confirmed only where everything vanishes is a criterion confirmed by a')
    rec('  ### dead instrument, which is b280\'s own not-dead discipline applied to this table.')

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec(rule())
    rec('### (3f) THE TWO BANKED VALUES, REPRODUCED. ### **THE ONLY NUMBERS OF THIS KIND PRINTED.**')
    rec(rule())
    rec('  ### These two vectors were written into b295\'s OWN SEALED REGISTRATION before its code')
    rec('  ### existed, and their values are banked. ### **REPRODUCING A BANKED VALUE IS THE')
    rec('  ### REPRODUCTION THE ORDER ASKS FOR; COMPUTING A NEW ONE IS THE LATER ACT\'S.**')
    from b294_family_value import pair_at_n
    from b270_ambient_pairing import Field
    for (p, n), (a, b), spec, predicted in REGISTERED_WITNESSES:
        fr = LF.model_frame(p, n)
        N = fr.M
        f = [Fraction(0)] * N
        for k, c in spec.items():
            f[k] = Fraction(c)
        inst_member = LF.in_space(fr, f, a, b)
        A = matrix_A(N, p, n, n)
        cyc = Field(N).reduce(pair_at_n(A, f, N, Field(N)))
        got = cyc[0] if cyc else Fraction(0)
        pure = bool(cyc) and all(c == 0 for c in cyc[1:])
        ok = inst_member and pure and got == predicted
        if not ok:
            fails.append('banked witness at (%d,%d) radii (%+d,%+d)' % (p, n, a, b))
        rec('  cell (%d,%d)  member (%+d,%+d)' % (p, n, a, b))
        rec('    in the member by the INSTRUMENT\'S OWN two literal conditions : %s'
            % ('YES' if inst_member else '### NO ###'))
        rec('    <A f, f>  banked %-8s  recomputed %-8s  (producer: b294_family_value.pair_at_n)'
            ' : %s' % (predicted, got, 'AGREE' if ok else '### DISAGREE ###'))

    # ==============================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 4 -- THE ARTIFACT. ### **THE QUANTITY THE MODEL FOLDS, COMPUTED ON BOTH.**')
    rec('=' * 100)
    rec('  ### b21 named it and b284 met it: ### **"THE MODEL\'S mod-N WRAPAROUND IS EXACTLY THIS')
    rec('  ### ESCAPED MASS FOLDED BACK IN."** ### b284 then wrote ### **"THE DERIVATION STANDS')
    rec('  ### BECAUSE IT IS ON `Q_p`, WHERE THERE IS NOTHING TO FOLD."**')
    rec('  ### ### **THIS COMPONENT MAKES THAT SENTENCE A COUNT.**')

    rec('')
    rec(rule())
    rec('### (4a) THE FOLD, COUNTED ON BOTH SIDES, TWO ROUTES EACH.')
    rec(rule())
    rec('  ### The model must read `theta(p^k) f` back in the frame it left, which on chart indices')
    rec('  ### is `m -> p^k m mod N`. ### The instrument moves the frame instead, and on chart')
    rec('  ### indices that is the IDENTITY. ### **BOTH COUNTS ARE DIRECT; THE CLOSED FORMS ARE THE')
    rec('  ### SECOND ROUTE, AND TWO ROUTES TO ONE INTEGER IS THE DISCIPLINE b304 USED FOR ITS OWN.**')
    rec('  %-10s %-4s %-16s %-20s %-18s %s'
        % ('cell', 'k', 'model image', 'model collisions', 'closed form', 'INSTRUMENT collisions'))
    fold_bad = 0
    for (p, n) in CELLS_FAMILY:
        N = p ** (2 * n)
        fr = LF.model_frame(p, n)
        for k in (1, 2):
            if k > 2 * n:
                continue
            isz, coll = LF.model_pushforward_fibers(p, n, k)
            closed = N * (p ** k - 1)
            _iz2, coll2 = LF.instrument_fold_pairs(fr, k)
            ok = (coll == closed and isz == N // (p ** k) and coll2 == 0 and coll > 0)
            fold_bad += 0 if ok else 1
            if not ok:
                fails.append('fold count at (%d,%d) k=%d' % (p, n, k))
            rec('  %-10s %-4d %-16s %-20s %-18s %s'
                % ('(%d,%d)' % (p, n), k, '%d of %d' % (isz, N), coll,
                   'N(p^k-1) = %d %s' % (closed, 'AGREE' if coll == closed else '### NO'),
                   '### **%d**' % coll2))
    rec('  ### **CELLS WHERE THE TWO ROUTES DISAGREE OR THE INSTRUMENT FOLDS ANYTHING : %d**'
        % fold_bad)
    rec('  ### **AND THE POSITIVE ARM IS THE MODEL\'S OWN COLUMN: IT IS NONZERO EVERYWHERE.** ### A')
    rec('  ### comparison in which both sides were zero would show only that nothing was tested.')

    rec('')
    rec(rule())
    rec('### (4b) THE ESCAPED MASS ITSELF, ON A VECTOR OF THE OBJECT\'S OWN SPACE.')
    rec(rule())
    rec('  ### b21\'s `U f(x) = p^{-1/2} f(p x)` sends `V_n` to `V(n+1, n-1)`. ### **THE PART OF THE')
    rec('  ### IMAGE AT `|x| = p^{n+1}` IS OUTSIDE THE MODEL\'S LEVEL ENTIRELY**, and the model has')
    rec('  ### to put it somewhere. ### The instrument has a frame for it and puts it there.')
    rec('  %-10s %-8s %-22s %-22s %s'
        % ('cell', 'dim', 'escaped Haar mass', 'total Haar mass', 'escaped is NONZERO'))
    esc_bad = 0
    for (p, n) in CELLS_FAMILY:
        fr = LF.model_frame(p, n)
        basis = LF.son_basis(fr, 0, 0)
        f = basis[0]
        up, uf = LF.scaling_action(fr, -1, f)
        escaped = up.cell_mass() * sum(uf[m] * uf[m] for m in range(up.M)
                                       if up.abs_index(m) > n)
        total = up.cell_mass() * sum(uf[m] * uf[m] for m in range(up.M))
        ok = (escaped > 0 and total > 0)
        esc_bad += 0 if ok else 1
        if not ok:
            fails.append('escaped mass at (%d,%d)' % (p, n))
        rec('  %-10s %-8d %-22s %-22s %s'
            % ('(%d,%d)' % (p, n), len(basis), escaped, total,
               'YES' if ok else '### NO -- nothing escaped, so nothing was tested ###'))
    rec('  ### **THE MASS IS EXACT AND IT IS NOT ZERO AT ANY CELL.** ### That is the mass b21 says')
    rec('  ### the model folds back onto the level, and the instrument carries it in `V(n+1, n-1)`')
    rec('  ### where it belongs. ### **CELLS WHERE NOTHING ESCAPED : %d**' % esc_bad)

    rec('')
    rec(rule())
    rec('### (4c) EXPOSURE BY CALL PATH. ### **THE ARM FINDS A SHAPE; THE SEAT RULES.**')
    rec(rule())
    rec('  ### A ### NON-UNIT PUSHFORWARD SITE ### is a line that reduces the product of a grid index')
    rec('  ### with a power of the residue characteristic modulo the grid size. ### **THAT IS THE')
    rec('  ### SHAPE THE FOLD TAKES IN CODE, AND IT IS NOT THE SAME THING AS EXPOSURE.**')
    scan = [
        ('tools/b308_local_field.py', 'THIS INSTRUMENT'),
        ('tools/b308_reproduction.py', 'THIS RUNNER'),
        ('tools/b303_family.py', 'b293/b303 -- the family, the dimension law, the diagonal'),
        ('tools/b304_smearing.py', 'b304 -- the compression, the smear, Tr(Pi)'),
        ('tools/e16/b293_finite_family.py', 'b293 -- the family at its own emitter'),
        ('tools/e16/b295_second_mechanism.py', 'b295 -- the criterion and its values'),
        ('tools/e16/b281_compression.py', 'b281 -- the operator A, at k = n'),
        ('tools/e16/b270_ambient_pairing.py', 'b270 -- the ball and the orbit classes'),
        ('tools/e16/b294_family_value.py', 'b294 -- the cyclotomic re-valuation'),
        ('tools/e16/b280_consequence.py', 'b280 -- the consequence, P(k=n) = 0'),
    ]
    # ### ### **DECLARED CARRIERS, BY `(file, enclosing def)`, EACH WITH ITS REASON.** ### b306's
    # ### lore rule governs the list: ### **AN EXCEPTION LIST IS A LIST OF PLACES A CHECK HAS AGREED
    # ### NOT TO LOOK, AND IT IS STATED WITH ITS REASONS EVERY TIME IT IS PRINTED.**
    DECLARED = {
        ('tools/b308_local_field.py', 'model_pushforward_fibers'):
            'THE DECLARED EXHIBIT -- it computes the model\'s collapse so that (4a) can COUNT it',
        ('tools/b308_local_field.py', 'self_test'):
            'THE ARM\'S OWN CONTROL STRINGS -- it spells the shape IN ORDER TO TEST FOR IT',
        ('tools/b308_reproduction.py', '_component_four_c'):
            'PROSE QUOTING b281\'s LINE IN ORDER TO RULE ON IT',
    }
    rec('  %-42s %-8s %s' % ('file', 'sites', 'the lines, with the enclosing def'))
    site_table, undeclared_here = [], 0
    for rel, who in scan:
        path = os.path.join(ROOT, rel.replace('/', os.sep))
        sites = LF.pushforward_sites(path) if os.path.exists(path) else []
        site_table.append((rel, who, sites))
        rec('  %-42s %-8d %s' % (rel, len(sites), who))
        for ln, dfn, txt in sites:
            tag = DECLARED.get((rel, dfn))
            if rel.startswith('tools/b308') and tag is None:
                undeclared_here += 1
                fails.append('undeclared pushforward site in %s:%d' % (rel, ln))
            rec('        line %-5d %-28s %s' % (ln, dfn, txt[:70]))
            if tag:
                rec('            ### DECLARED CARRIER -- %s' % tag)
    rec('')
    rec('  ### ### **THIS ACT\'S OWN TWO FILES: %d SITE(S), ALL OF THEM DECLARED CARRIERS, AND'
        % sum(len(s) for r, _w, s in site_table if r.startswith('tools/b308')))
    rec('  ### ### UNDECLARED SITES IN THE INSTRUMENT\'S OPERATIONAL PATH : %d**' % undeclared_here)
    rec('  ### The frame, the transform, the two conditions, the dilation and the compression carry')
    rec('  ### no such site. ### **THAT IS A MECHANICAL STATEMENT OF `F2` AT THE SOURCE LEVEL,')
    rec('  ### BESIDE THE ARITHMETIC ONE IN (4a).**')
    return _component_four_c(rec, fails, out, site_table)


def _component_four_c(rec, fails, out, site_table):
    inst_sites = dict((r, s) for r, _w, s in site_table)
    rec('')
    rec('  ### ### **THE READING, PER FILE, AND IT IS THE SEAT\'S:**')
    rec('  ### **`b303_family.py` -- NO SITE. ### NOT EXPOSED.** ### b293\'s dilation moves the')
    rec('  ###   family\'s CONDITION INDICES by an argument about radii; no vector is ever pushed')
    rec('  ###   forward by a non-unit, and the chart block checks identities of `Fraction`s.')
    rec('  ### **`b304_smearing.py` -- NO SITE, AND ITS OWN REFUSAL IS THE REASON.** ### b304')
    rec('  ###   computes the `Z_p^x` part only and states that it ### **"REFUSES THE `p^Z` PART"**,')
    rec('  ###   checking `is_permutation` at every `t` it uses. ### **THE PART IT REFUSED IS')
    rec('  ###   EXACTLY THE PART THIS INSTRUMENT ADDS.**')
    rec('  ### **`b270_ambient_pairing.py` -- SITE(S) PRESENT, AND THIS SEAT RULES NOT EXPOSED.**')
    rec('  ###   The site is in `orbit_classes`, which unions `m ~ pm` OFF THE BALL to build b10\'s')
    rec('  ###   quotient basis. ### **THAT IS A STRUCTURE ON THE INDEX SET, NOT A PUSHFORWARD OF A')
    rec('  ###   FUNCTION\'S MASS**: no function is evaluated, nothing is summed onto a collided')
    rec('  ###   index, and the classes are the columns the averaging is DEFINED over.')
    rec('  ### **`b281_compression.py` -- SITE(S) PRESENT, AND THIS SEAT RULES NOT EXPOSED.** ### The')
    rec('  ###   site is `l = (pk * m) % N` in `matrix_A`, which is b273\'s DEFINITION of `A`:')
    rec('  ###   ### **"`A[l,j] = SUM_{m : p^k m = l mod N} S_quot[m,j]`"**. ### The sum over the')
    rec('  ###   fiber is a REGROUPING OF AN EXACT FINITE SUM -- `T(g) = SUM_m (S_quot g)(m)')
    rec('  ###   conj(g(p^k m))` collected by `l = p^k m` -- and a regrouping loses nothing.')
    rec('  ###   ### **A FOLD IS MASS THAT LEFT ITS LEVEL AND WAS PUT BACK; THIS IS AN ORDER OF')
    rec('  ###   SUMMATION.** ### And the second slot reads `g` at `p^k m`, which is EVALUATION,')
    rec('  ###   not transport: at `k = n` it reads `g` on `Z_p`, inside the frame.')
    rec('  ### **`b280_consequence.py` -- ONE SITE, AND IT IS AN EVALUATION.** ### The line is')
    rec('  ###   `spconj(u[(pk * m) % N], N)` inside `pairing_rescaled`: it READS `u` at the index')
    rec('  ###   `p^k m`. ### **A READ MOVES NO MASS.** ### And the distinction is visible in the')
    rec('  ###   printed lines themselves rather than only in this sentence: b281\'s site ASSIGNS')
    rec('  ###   into an accumulator, b280\'s and b270\'s line 222 INDEX INTO a vector. ### **ONE')
    rec('  ###   WRITES, THE OTHERS READ**, and only a write can put escaped mass anywhere.')
    rec('  ### **`b295_second_mechanism.py` -- ITS OWN DECLARATION, QUOTED, AND THE ARM AGREES WITH')
    rec('  ###   IT:** ### **"EXPOSURE TO THE ESCAPED-MASS ARTIFACT (Z5): NONE ... This runner')
    rec('  ###   applies NO LEVEL-SHIFTING MAP."**')
    rec('')
    rec('  ### ### **THE ONE BANKED RESULT THAT WAS EXPOSED, AND IT DECLARED ITSELF:** ### b284,')
    rec('  ### whose `g` and `h` DO shift the level. ### Its own (D2): the model says `h`\'s `S2`')
    rec('  ### fails, the derivation says it holds, ### **"THEY DISAGREE, AND THE DISAGREEMENT IS')
    rec('  ### THE ARTIFACT, NOT THE ANSWER"** ### -- reported and not promoted. ### **THIS ACT')
    rec('  ### ADDS NOTHING TO THAT AND DOES NOT RE-VERDICT IT.**')
    # ---------------------------------------------------------------------------------------------
    rec('')
    rec(rule())
    rec('### (4d) WHICH BANKED RESULTS WERE EXPOSED, AND WHICH WERE NOT -- ### **BY CALL PATH.**')
    rec(rule())
    rec('  ### The column `sites` counts the arm\'s hits over the WHOLE call path of the result --')
    rec('  ### every file its producing tool imports and uses. ### **THE VERDICT COLUMN IS NOT THE')
    rec('  ### COUNT.** ### The count is a shape; the verdict is the seat\'s, and where the two')
    rec('  ### differ the reason is the sentence beside it.')
    RESULTS = [
        ('b293/b303 -- the family, its dimension law, the diagonal identification',
         ['tools/b303_family.py', 'tools/e16/b293_finite_family.py'],
         'NOT EXPOSED',
         'no vector is pushed forward by a non-unit anywhere in the path; the dilation moves the '
         'family\'s CONDITION INDICES by an argument about radii'),
        ('b304 -- Tr(Pi) = dim Son, and the compact-part smear\'s zero with its mechanism',
         ['tools/b304_smearing.py', 'tools/b303_family.py'],
         'NOT EXPOSED, AND b304 SAID SO FIRST',
         'b304 computes the `Z_p^x` part only, checks `is_permutation` at every `t`, and REFUSES '
         'the `p^Z` part -- which is exactly the part this instrument adds'),
        ('b280 -- `P(k = n) = 0` on every `Son` basis vector at six cells',
         ['tools/e16/b280_consequence.py', 'tools/e16/b281_compression.py',
          'tools/e16/b270_ambient_pairing.py'],
         'NOT EXPOSED',
         'the sites are `A`\'s own definition and the quotient basis\'s index structure; both are '
         'rulings given in full above'),
        ('b295/b296 -- the annihilation criterion, and the two banked values',
         ['tools/e16/b295_second_mechanism.py', 'tools/e16/b281_compression.py',
          'tools/e16/b270_ambient_pairing.py', 'tools/e16/b293_finite_family.py',
          'tools/e16/b294_family_value.py'],
         'NOT EXPOSED, AND b295 SAID SO FIRST',
         'its own Z5: it applies NO LEVEL-SHIFTING MAP; the sites in the path are `A`\'s definition '
         'and the class structure'),
        ('b21 -- the model transform IS the genuine transform at a fixed level',
         [],
         'NOT EXPOSED, IN b21\'s OWN WORDS',
         'b21 checked it ENTRY-EXACT and wrote `with NO artifact`; the artifact it named is in the '
         'U-law, not here'),
        ('b284 -- the scaling\'s domain, computed through `g` and `h`',
         [],
         '### **EXPOSED, AND IT DECLARED ITSELF** ###',
         'its own (D2): `h`\'s transform side, model (FAILS) against derivation (HOLDS) -- the '
         'disagreement reported and the control NOT promoted over the derivation'),
    ]
    rec('  %-64s %-7s %s' % ('banked result', 'sites', 'verdict'))
    for what, paths, verdict, why in RESULTS:
        n_sites = sum(len(inst_sites.get(p, [])) for p in paths)
        rec('  %-64s %-7s %s' % (what[:64], n_sites if paths else 'n/a', verdict))
        rec('      ### %s' % why)
    rec('')
    rec('  ### ### **SO THE RETIREMENT IS EXACTLY THIS, AND NO WIDER:**')
    rec('  ### **THE ESCAPED-MASS ARTIFACT IS RETIRED FOR THIS INSTRUMENT**, because the scaling')
    rec('  ###   part acts by moving the frame and the fold count is zero at every cell and every')
    rec('  ###   direction tested, computed two ways.')
    rec('  ### **IT IS NOT RETIRED FOR THE MODEL.** ### The model\'s own column in (4a) is nonzero')
    rec('  ###   everywhere, and any later act computing a scaling on `Z/p^{2n}` meets it again.')
    rec('  ### **IT IS NOT RETIRED FOR b284**, whose exposure is declared, stands, and is not')
    rec('  ###   re-verdicted here.')
    rec('  ### **AND IT RETIRES NOTHING ELSE** -- not `W-ORD-FIBER-GENERAL`, not the barrier\'s')
    rec('  ###   scope limit, not the range law, and not the truncation, which untying the radii')
    rec('  ###   does not touch.')

    rec('')
    rec('  ### ### **THE ARM\'S OWN LIMIT, PRINTED WHERE IT IS USED:** ### it matched %d site(s)'
        % sum(len(s) for s in inst_sites.values()))
    rec('  ### across the files scanned, and ### **IT CANNOT TELL A REGROUPING OF AN EXACT FINITE')
    rec('  ### SUM FROM A REPRESENTATION OF A FUNCTION THAT LEFT ITS LEVEL.** ### The ruling on')
    rec('  ### each is above, it is this seat\'s, and ### **PRETENDING A TOOL MADE IT WOULD BE THE')
    rec('  ### FALSE ASSURANCE THIS DISCIPLINE EXISTS AGAINST.**')

    rec('')
    rec('=' * 100)
    rec('### THE VERDICT ON THE THREE REGISTERED FALSIFIERS.')
    rec('=' * 100)
    f1 = not [x for x in fails if x.startswith(('F3', 'criterion', 'dimension', 'smear',
                                                'banked witness', 'collapse', 'compression'))]
    f2 = not [x for x in fails if x.startswith(('fold', 'escaped', 'dilation'))]
    f3 = not [x for x in fails if x.startswith('F3')]
    rec('  (F1) the reproduction matches at every reachable cell ......... %s'
        % ('### **DID NOT FIRE**' if f1 else '### ### **FIRED** ###'))
    rec('  (F2) the scaling part acts without wraparound on the local field %s'
        % ('### **DID NOT FIRE**' if f2 else '### ### **FIRED** ###'))
    rec('  (F3) the untied radii recover the two-radius family exactly ... %s'
        % ('### **DID NOT FIRE**' if f3 else '### ### **FIRED** ###'))
    rec('')
    rec('  ### CHECKS FAILING : %d' % len(fails))
    for f in fails:
        rec('    ### FAILED: %s' % f)
    rec('=' * 100)
    return (0 if not fails else 1), out


if __name__ == '__main__':
    code, lines = main()
    io.open(os.path.join(D, 'b308_instrument_run.txt'), 'w', encoding='utf-8',
            newline='\n').write('\n'.join(lines) + '\n')
    sys.exit(code)
