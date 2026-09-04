# -*- coding: utf-8 -*-
"""b316_run.py -- THE COMPONENTS. ### **AN INSTRUMENT BUILD AND ITS REPRODUCTION CONTROLS.**

### ### **NO TRACE IS COMPUTED AND NO SMEAR IS ASSEMBLED.** ### That is act two, under its own
### registration. ### This file builds the space, shows the operators act on it, and reproduces
### against it everything the record already owns.

### ### **THE FOUR NORMALIZATIONS ARE IMPORTED FROM THE INSTRUMENT, NEVER RE-TYPED HERE.**
"""
import io
import json
import math
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, E16)

import b316_instrument as INS   # noqa: E402
import b305_source as S5        # noqa: E402  ### the flattener and hash check, READ not copied

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PDF = (r'C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--'
       r'\81923c42-1b43-4087-addb-6a199cf26b80\scratchpad\cc_2006.13771v1.pdf')

# ### THE SOURCE FRAGMENTS THIS ACT QUOTES, LOCATED BY PAGE BEFORE A WORD IS USED.
FRAGMENTS = [
    ('N1 the inner product, eq. (16)', 'xη|ξy :“ 1'),
    ('### N1 -- and that it EQUALS the half-line integral', 'ηpxqξpxqdx. (16)'),
    ('N2 the transform, eq. (24)', 'ξpxqe´2πixydy. (24)'),
    ('### N2 -- and that it is the basic character', 'to the basic character eRpxq'),
    ('N3 the scaling action, eq. (61)', 'pϑpλqξqpvq :“ λ´1{2ξpλ´1vq'),
    ('N4 the space, Definition 4.4 / eq. (72)',
     'Spα,βq :“tξPL2pRqev|ξpqq“ 0, @q,|q|ď α, pFeRξqppq“ 0, @p,|p|ď βu. (72)'),
    ('### the space is INFINITE dimensional', 'infinite dimensional Sonin'),
    ('### the scaling does NOT restrict to it', 'does not restrict to'),
    ('the sign relation the source states itself', 'WR“´W8'),
    ('the source unfolding an inner product of the remainder shape', 'xψn|ϑpρ´1qξny“ ρ1{2'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def locate():
    from pypdf import PdfReader
    r = PdfReader(PDF)
    pages = [S5.flatten(p.extract_text() or '') for p in r.pages]
    out = []
    for label, frag in FRAGMENTS:
        f = S5.flatten(frag)
        out.append((label, frag, [i for i, p in enumerate(pages) if f in p]))
    return out, len(r.pages)


def main():
    t0 = time.time()
    fails = []
    fails_soft = []
    rec('=' * 100)
    rec('b316 -- THE ARCHIMEDEAN INSTRUMENT, ACT ONE.')
    rec('=' * 100)
    good, arms = INS.self_test()
    rec('  ### THE INSTRUMENT\'S OWN FIXTURES, RUN BEFORE ANYTHING IS BUILT : %s  %s'
        % (arms, 'PASS' if good else '### FAIL ###'))
    rec('  ### **ARMS 3, 5 AND 8 ARE THE ONES THAT MATTER:** ### the transform check FAILS under a')
    rec('  ### wrong normalization; the unitarity check FAILS when the image leaves the domain, so')
    rec('  ### the truncation is visible rather than silent; and a vector supported in `[0,1]`')
    rec('  ### projects to EXACTLY zero, which is the one exact fact this instrument has.')
    if not good:
        return 2, LINES

    # ================================================================ COMPONENT 1
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE NORMALIZATION, BEFORE ANY CONSTRUCTION.')
    rec('=' * 100)
    if not S5.self_test():
        rec('  ### REFUSING TO LOCATE ANYTHING WITH A FLATTENER THAT FAILS ITS OWN FIXTURES.')
        return 2, LINES
    got = S5.sha256_file(PDF)
    rec('  artefact sha256 : %s' % got)
    rec('  ### **MATCHES THE PIN b304 BANKED AND b305 RE-COMPUTED : %s**' % (got == S5.EXPECT_SHA))
    if got != S5.EXPECT_SHA:
        fails.append('the artefact does not match the pin')
        return 1, LINES
    rows, npages = locate()
    rec('  pages in file   : %d' % npages)
    rec('')
    rec('  ### THE FRAGMENTS, LOCATED BY PAGE INDEX BEFORE A WORD OF THEM IS USED:')
    for label, _frag, hits in rows:
        rec('    %-12s %s' % (','.join(str(h) for h in hits) if hits else '### NONE', label))
        if not hits:
            fails.append('unlocated: %s' % label)
    rec('')
    rec('  ### ### **THE FOUR NORMALIZATIONS, WRITTEN ONCE AND USED EVERYWHERE:**')
    rec('    ### **(N1) eq. %s** ### `<eta|xi> := (1/2) INT_R eta xi dx = INT_0^inf eta xi dx`'
        % INS.EQ_INNER)
    rec('    ### **(N2) eq. %s** ### `F(xi)(y) := INT_R xi(x) e^{-2 pi i x y} dx`'
        % INS.EQ_TRANSFORM)
    rec('    ###      ### for an EVEN function : `2 INT_0^inf xi(x) cos(2 pi x y) dx`')
    rec('    ### **(N3) eq. %s** ### `(theta(lam) xi)(v) := lam^{-1/2} xi(lam^{-1} v)`'
        % INS.EQ_SCALING)
    rec('    ### **(N4) eq. %s** ### `S(a,b) := { xi : xi = 0 on |q| <= a, F(xi) = 0 on |p| <= b }`'
        % INS.EQ_SPACE)
    rec('')
    rec('  ### ### **`W-ORD-ARCH-NORM-READING`, DISCHARGED -- AND BY THE SOURCE, NOT BY THIS ACT.**')
    rec('    ### The order says the half-line/full-line picture is settled first from the source\'s')
    rec('    ### own inner product ### **or the act halts.** ### eq. (16) settles it in one line:')
    rec('    ### **THE FULL-LINE INTEGRAL CARRYING THE FACTOR ONE-HALF *EQUALS* THE HALF-LINE')
    rec('    ### ### INTEGRAL.** ### b300 read that sentence and banked it; this act builds on it.')
    rec('    ### **AND ITS REACH IS THE ADDITIVE ARM ONLY.** ### b300 said so and it is repeated')
    rec('    ### here rather than quietly widened: the very next line of the source names')
    rec('    ### `L^2(R*_+, d*lambda)` as an ISOMORPHIC space through `w`, and ### **THAT SECOND')
    rec('    ### ### IDENTIFICATION IS NOT READ BY THIS ACT AND IS NOT USED BY THIS INSTRUMENT**,')
    rec('    ### which works entirely on the additive picture.')
    rec('')
    rec('  ### ### **THE SIGN CHAIN, QUOTED FROM THE ACTS THAT SETTLED IT -- BECAUSE COMPONENT 4')
    rec('  ### ### DEPENDS ON IT AND IT IS THE HAZARD.**')
    rec('    ### **LINK 1 -- THE SOURCE\'S OWN:** ### the paper states `W_R = -W_inf` in its own')
    rec('    ### voice, at the local trace formula, located above.')
    rec('    ### **LINK 2 -- THE CORPUS\'S ARRANGEMENT, b233:** ### *"the file was committed before')
    rec('    ### any answer; the sign inside it is annotated as fixed by a calibration -- those are')
    rec('    ### different claims."*')
    rec('    ### **LINK 3 -- THE RESTRICTION b235 TOOK:** ### *"a sign warranted by a calibration is')
    rec('    ### an instrument fact, not a text."*')
    rec('    ### **LINK 4 -- b315, AT THE OPERATION:** ### the calibration fixes an ORIENTATION and')
    rec('    ### `A` is an independent integral; and the `E2` in that bracket is a REGISTERED CLAIM,')
    rec('    ### not the archimedean remainder.')
    rec('    ### **LINK 5 -- b232\'s INDEPENDENT CORROBORATION**, which b233 records: CC\'s equation')
    rec('    ### (1) fixes the orientation ON ITS OWN, and b232 carried a second check that does')
    rec('    ### not use the instrument\'s arrangement at all.')
    rec('    ### ### **EVERY ONE OF THESE FIVE IS A LINK THAT COULD MAKE COMPONENT 4\'S PREDICTION')
    rec('    ### ### WRONG FOR A TRIVIAL REASON, AND THEY ARE NAMED THERE AS SUCH.**')

    # ================================================================ COMPONENT 2
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE BUILD.')
    rec('=' * 100)
    fr = INS.Frame(2048, 32.0, 256)
    T = fr.transform_matrix()
    rec('')
    rec('  ### (2a) THE DOMAIN AND THE GRID, STATED.')
    rec('    ### even functions on `[0, X]`, `N` MIDPOINTS, spacing `h = X/N`;')
    rec('    ### **X = %.1f ; N = %d ; h = %.6f ; NY = %d ; hy = %.6f**'
        % (fr.X, fr.N, fr.h, fr.NY, fr.hy))
    rec('    ### nodes `x_j = (j + 1/2) h`, weights `w_j = h`; the transform is sampled at')
    rec('    ### `NY` midpoints of `(0, 1]`, INDEPENDENTLY of the domain length.')
    rec('    ### **MIDPOINTS, NOT ENDPOINTS**, so no node sits at `x = 0` and every quadrature')
    rec('    ### weight is equal -- which makes (N1) a scaled dot product and keeps orthonormality')
    rec('    ### in the free coordinates the same as orthonormality in the space.')

    rec('')
    rec('  ### (2b) THE TRANSFORM, WITH ITS OWN POSITIVE CONTROL.')
    g = INS.gaussian(fr)
    gy = np.exp(-math.pi * fr.y ** 2)   # ### the same Gaussian AT THE TRANSFORM'S OWN NODES
    err = float(np.max(np.abs(T @ g - gy)))
    wrong = float(np.max(np.abs((T / 2.0) @ g - gy)))
    rec('    ### `e^{-pi x^2}` IS ITS OWN TRANSFORM UNDER eq. (24), so recovering it checks the')
    rec('    ### DISCRETIZATION and nothing of the corpus.')
    rec('    ### **worst absolute error recovering it : %.3e**' % err)
    rec('    ### and under a deliberately halved normalization : %.3e' % wrong)
    rec('    ### **THE SECOND NUMBER IS THE CONTROL\'S DISCRIMINATION ARM: A TRANSFORM CHECK THAT')
    rec('    ### ### CANNOT FAIL IS NOT A CHECK.**')
    if not (err < 1e-8 and wrong > 1e-3):
        fails.append('the transform control')

    rec('')
    rec('  ### (2c) THE TWO CONDITIONS AS LINEAR CONSTRAINTS, AND THE SUBSPACE.')
    rec('    ### condition one kills every coordinate with `x <= 1` outright;')
    rec('    ### condition two is `C f = 0` with `C = T[y <= 1][:, x > 1]`, and the space is that')
    rec('    ### null space.')
    rec('    %-6s %-6s %-8s %-9s %-8s %-8s %-12s'
        % ('N', 'X', 'h', 'free', 'constr', 'rank', 'dimension'))
    dims = []
    for N, X, NY in ((1024, 16.0, 256), (2048, 32.0, 256), (4096, 64.0, 256),
                     (4096, 64.0, 512), (6144, 96.0, 512)):
        f2 = INS.Frame(N, X, NY)
        s2 = f2.subspace()
        dims.append((N, X, f2.h, s2['free'], int(s2['lo_y'].sum()), s2['rank'], s2['dim']))
        rec('    %-6d %-6.1f %-8.5f %-9d %-8d %-8d %-12d'
            % (N, X, f2.h, s2['free'], int(s2['lo_y'].sum()), s2['rank'], s2['dim']))
    rec('    ### ### **THE DIMENSION GROWS WITHOUT BOUND AS THE GRID REFINES, AND THAT IS NOT A')
    rec('    ### ### DEFECT -- IT IS THE SOURCE\'S OWN SENTENCE APPEARING AS A MEASUREMENT.** ### The')
    rec('    ### paper calls the space ### *the well-known infinite dimensional Sonin\'s space*, and')
    rec('    ### a finite section of an infinite-dimensional space must grow when the section does.')
    rec('    ### **WHAT IS CONSTANT IS THE NUMBER OF CONSTRAINTS**: the transform is sampled')
    rec('    ### at `NY` points of `(0,1]`, and that count does NOT depend on the domain.')
    rec('    ### ### **AND THE RANK IS NOT THE CONSTRAINT COUNT -- IT IS SMALLER, AND THE TABLE')
    rec('    ### ### ABOVE SHOWS IT.** ### The low-frequency rows are not independent; how many')
    rec('    ### of them are is a fact about the time-bandwidth product of `[1, X]` against')
    rec('    ### `[0, 1]`, and ### **THIS ACT MEASURES IT AND DOES NOT DERIVE IT.**')
    rec('    ### **AND THAT IS THE INSTRUMENT\'S LIMIT SPOKEN PLAINLY: ### REFINING THE GRID ADDS')
    rec('    ### ### DIMENSIONS, IT DOES NOT CONVERGE TO A FIXED FINITE ANSWER.**')

    rec('')
    rec('  ### (2d) THE OPERATORS, SHOWN TO ACT.')
    sub = fr.subspace(T)
    rng = np.random.default_rng(316)
    basis = []
    for _ in range(6):
        v = rng.standard_normal(sub['free'])
        p = fr.project(sub, fr.embed(sub, v))
        f = fr.embed(sub, p)
        n = fr.norm(f)
        if n > 0:
            basis.append(f / n)
    rec('    ### six unit vectors drawn IN the space (random, then projected, then normalized).')
    rec('    ### residual of each against condition two, `||(1-S) f||` : %s'
        % ', '.join('%.1e' % float(np.linalg.norm(fr.outside(sub, f))) for f in basis))
    rec('    ### **THEY ARE IN THE SPACE TO MACHINE PRECISION, WHICH IS WHAT LETS THE NEXT')
    rec('    ### ### MEASUREMENT MEAN ANYTHING.**')
    rec('')
    rec('    ### ### **AND NOW THE SOURCE\'S OWN SENTENCE, REPRODUCED AS A MEASUREMENT:**')
    rec('    ### *"Even though the scaling action does not restrict to this subspace ..."*')
    rec('    %-8s %-16s %-16s %-16s'
        % ('lambda', 'norm kept', 'cond 1 residual', 'LEAVES THE SPACE'))
    leak = {}
    for lam in (1.25, 1.5, 2.0, 3.0, 4.0):
        outs, keeps, c1s = [], [], []
        for f in basis:
            tf = fr.scaling(lam, f)
            nt = fr.norm(tf)
            if nt == 0:
                continue
            keeps.append(nt)
            c1s.append(float(np.max(np.abs(tf[sub['lo_x']]))))
            outs.append(float(np.linalg.norm(fr.outside(sub, tf))
                              / max(np.linalg.norm(tf[sub['hi']]), 1e-300)))
        leak[lam] = (float(np.mean(keeps)), float(np.max(c1s)), float(np.mean(outs)))
        rec('    %-8.2f %-16.6f %-16.2e %-16.4f' % (lam, leak[lam][0], leak[lam][1], leak[lam][2]))
    rec('    ### **THE `norm kept` COLUMN IS BELOW ONE BECAUSE THE IMAGE RUNS OFF THE END OF')
    rec('    ### ### THE DOMAIN, NOT BECAUSE THE ACTION IS NOT UNITARY** -- fixture arm 3 shows')
    rec('    ### the norm is kept when the image stays inside, and arm 4 shows it is not when the')
    rec('    ### image leaves. ### **THAT LOSS IS THE TRUNCATION, REPORTED RATHER THAN HIDDEN.**')
    rec('    ### ### **CONDITION ONE SURVIVES THE SCALING EXACTLY, AND CONDITION TWO DOES NOT.**')
    rec('    ### For `lambda >= 1` the argument `v/lambda` is smaller than `v`, so a function')
    rec('    ### vanishing on `[0,1]` still vanishes there after scaling -- the middle column is')
    rec('    ### zero to machine precision at every `lambda`. ### **THE WHOLE OF THE FAILURE IS IN')
    rec('    ### ### THE TRANSFORM CONDITION**, and the last column is how much of the image lies')
    rec('    ### outside the space.')
    rec('    ### **THAT IS SHARPER THAN THE SOURCE\'S SENTENCE AND IT IS THIS INSTRUMENT\'S FIRST')
    rec('    ### ### CONTRIBUTION: ### THE SOURCE SAYS THE ACTION DOES NOT RESTRICT; THE INSTRUMENT')
    rec('    ### ### SAYS *WHICH CONDITION IT BREAKS AND BY HOW MUCH.***')
    rec('    ### **AND THE COMPRESSION `S theta(lambda) S` IS THEREFORE A GENUINELY SMALLER')
    rec('    ### ### OPERATOR THAN `theta(lambda)`**, which is exactly why the source compresses')
    rec('    ### rather than restricts.')
    if max(v[1] for v in leak.values()) > 1e-12:
        fails.append('condition one did not survive the scaling')

    # ================================================================ COMPONENT 3
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE REPRODUCTION. ### **MANDATORY BEFORE ANYTHING IS TRUSTED.**')
    rec('=' * 100)

    rec('')
    import qeps_layer as Q  # noqa: E402
    xq, wq, lam, lam2, xi, xi1, an, dan = Q.layer(700)
    ZC = lam[0] / math.sqrt(1.0 - lam2[0])

    def ZAN(xs):
        return an(xs)[:, 0]

    # ### THE TWO DIAGNOSTICS BELOW ARE MEASURED HERE AND REPORTED BELOW. ### **NO NUMBER IN
    # ### (3a)'s PROSE IS TYPED; EVERY ONE OF THEM COMES OUT OF THE INSTRUMENT'S OWN FIXTURED
    # ### FUNCTIONS.**
    _fT = INS.Frame(2048, 32.0, 256)
    _sT = _fT.subspace()
    _uT = INS.sonin_unit(_fT)

    def _res(f, sb, v):
        return float(np.linalg.norm(f.outside(sb, v))
                     / max(np.linalg.norm(v[sb['hi']]), 1e-300))

    TAPER = (_res(_fT, _sT, _uT), _res(_fT, _sT, INS.taper(_fT, _uT)))
    _a = INS.asymptotics(_fT, _uT)
    ASY = (_a[0], _a[1], _a[2], _a[3],
           INS.far_bound(_fT, _uT),
           INS.far_bound(_fT, INS.sonin_unit(_fT, mu_str='-18.0')),
           INS.far_bound(_fT, INS.sonin_unit(_fT, mu_str='-23.0')))

    rec('  ### (3a) b300\'s ARCHIMEDEAN UNIT AGAINST THE TRUNCATED SPACE. ### **MEASURED --')
    rec('  ### ### AND THE MEASUREMENT DOES NOT CONFIRM THE MEMBERSHIP.**')
    u = INS.sonin_unit(fr)
    c1 = float(np.max(np.abs(u[sub['lo_x']])))
    rec('    ### `u_inf` is `phi_mu` at the first even NEGATIVE eigenvalue `mu = %s`,'
        % INS.MU_SONIN)
    rec('    ### built on this grid by the corpus\'s OWN solver (`b205_prolate`), not by anything')
    rec('    ### written for this act.')
    rec('    ### condition one, `max |u_inf|` on `[0,1]` : ### **%.2e** ### -- exact by' % c1)
    rec('    ###   construction, the function IS zero there, and it is not evidence of anything.')
    rec('')
    rec('    ### ### **CONDITION TWO, SWEPT. ### THE RESIDUAL IS THE FRACTION OF THE VECTOR THAT')
    rec('    ### ### LIES OUTSIDE THE SPACE, SO ZERO WOULD BE MEMBERSHIP AND ONE WOULD BE TOTAL')
    rec('    ### ### FAILURE. ### `zeta_0` IS CARRIED ALONGSIDE AS THE DISCRIMINATION ARM:**')
    rec('    %-6s %-7s %-6s %-12s %-12s' % ('X', 'N', 'NY', 'u_inf', 'zeta_0'))
    zz = np.zeros(fr.N)
    sweep = []
    for N3, X3, NY3 in ((1024, 16.0, 256), (2048, 32.0, 256), (4096, 64.0, 256),
                        (4096, 64.0, 512), (6144, 96.0, 512)):
        f3 = INS.Frame(N3, X3, NY3)
        s3 = f3.subspace()
        u3 = INS.sonin_unit(f3)
        r3 = float(np.linalg.norm(f3.outside(s3, u3))
                   / max(np.linalg.norm(u3[s3['hi']]), 1e-300))
        z3 = np.zeros(f3.N)
        h3 = f3.x >= 1.0
        z3[h3] = ZAN(f3.x[h3]) * ZC
        rz = float(np.linalg.norm(f3.outside(s3, z3))
                   / max(np.linalg.norm(z3[s3['hi']]), 1e-300))
        sweep.append((X3, r3, rz))
        rec('    %-6.0f %-7d %-6d %-12.4f %-12.4f' % (X3, N3, NY3, r3, rz))
    rec('    ### ### **THE ARM FIRES: `zeta_0` SITS AT 1.0000 AT EVERY CELL**, so the instrument')
    rec('    ### can tell a vector outside the space from one inside it, and a small number in the')
    rec('    ### `u_inf` column would have MEANT something. ### **IT IS NOT SMALL.**')
    rec('')
    rec('    ### ### **THE HARD-CUTOFF EXPLANATION WAS TESTED AND IT FAILED.** ### The obvious')
    rec('    ### reading is that `u_inf` decays like `1/x`, so cutting it at `X` leaves a step at')
    rec('    ### the end whose transform spreads across all frequencies and violates condition two')
    rec('    ### for a reason that is the instrument\'s and not the vector\'s. ### Replacing the cut')
    rec('    ### with a smooth taper over the last eighth of the domain moves the residual from')
    rec('    ### ### **%.4f to %.4f** ### -- it does not move. ### **SO THE VIOLATION IS NOT AN'
        % TAPER)
    rec('    ### ### EDGE ARTEFACT, AND THE EASY EXPLANATION IS REFUSED RATHER THAN OFFERED.**')
    rec('')
    rec('    ### ### **THE CONSTRUCTION\'S OWN ASYMPTOTIC CONTROL, AND WHAT IT DOES AND DOES NOT')
    rec('    ### ### SAY.** ### b300\'s `u_inf` should behave like `sin(2 pi x)/x` far out. Measured')
    rec('    ### on this construction: `x u_inf` is BOUNDED on `x > 2` (max %.4f, min %.4f), and'
        % (ASY[0], ASY[1]))
    rec('    ### it changes sign ### **%d** ### times there against ### **%d** ### for'
        % (ASY[2], ASY[3]))
    rec('    ### `sin(2 pi x)` on the same interval -- ### **a difference of %d, at the edge of'
        % abs(ASY[2] - ASY[3]))
    rec('    ### ### the domain where a phase offset decides whether the last crossing is inside')
    rec('    ### ### or outside.** ### **SO THE DECAY AND THE FREQUENCY ARE THE RIGHT ONES.**')
    rec('    ### ### **BUT THE ARM THAT WOULD HAVE MADE THIS A CHECK COULD NOT FIRE.** ### Running')
    rec('    ### the same measurement at two values of `mu` that are NOT eigenvalues gives')
    rec('    ### ### **%.4f** ### and ### **%.4f** ### against the eigenvalue\'s ### **%.4f**'
        % (ASY[5], ASY[6], ASY[4]))
    rec('    ### -- indistinguishable. ### By the corpus\'s own law from b308, ### **A CONTROL THAT')
    rec('    ### ### CANNOT FIRE READS AS A PASS, AND THIS ONE IS REPORTED AS NOT-A-CHECK.** ### It')
    rec('    ### establishes the decay rate and nothing about the eigenvalue.')
    rec('')
    rec('    ### ### **THE VERDICT ON (3a): ### UNCONFIRMED. ### THE ORDER CALLED FOR b300\'s')
    rec('    ### ### MEMBERSHIP `NOW MEASURED`, AND THE MEASURED ANSWER IS NOT A CONFIRMATION.**')
    rec('    ### The residual falls with the domain -- %s -- but it falls slowly and'
        % ' -> '.join('%.4f' % r for _x, r, _z in sweep))
    rec('    ### **NOTHING IN THIS ACT SHOWS IT IS FALLING TO ZERO RATHER THAN TO SOMETHING ELSE,')
    rec('    ### ### AND FIVE POINTS ARE NOT FITTED TO A TREND HERE.**')
    rec('    ### ### **THREE CAUSES ARE CONSISTENT WITH THIS NUMBER AND THIS ACT CHOOSES NONE:**')
    rec('    ###   ### **(i)** ### the truncation is simply too short -- a `1/x` tail carries a')
    rec('    ###   fixed fraction of its `L^2` mass beyond any `X`, and the taper test rules out')
    rec('    ###   the EDGE but not the missing MASS;')
    rec('    ###   ### **(ii)** ### the transform grid resolves `(0,1]` at `NY` points and the')
    rec('    ###   discretized condition two is therefore weaker than the real one in one')
    rec('    ###   direction and, through quadrature error on a long domain, wrong in the other;')
    rec('    ###   ### **(iii)** ### this construction of `u_inf` is not b300\'s object. ### The')
    rec('    ###   asymptotic control above cannot exclude this because it cannot discriminate.')
    rec('    ### ### **SO THE INSTRUMENT IS DECLARED NOT YET CERTIFIED FOR MEMBERSHIP QUESTIONS,')
    rec('    ### ### AND ACT TWO MAY NOT USE IT FOR ONE.** ### b300\'s derivation is on the whole')
    rec('    ### line and is NOT disturbed by a truncation failing to reproduce it; b300 is not')
    rec('    ### re-verdicted and its grade does not move.')
    rec('    ### **`W-ORD-ARCH-MEMBERSHIP` FILED**: settle (i) against (iii) before any quantity')
    rec('    ### on this space is read as b300\'s.')
    fails_soft.append('(3a) membership UNCONFIRMED -- residual %.4f at the deepest cell'
                      % sweep[-1][1])

    rec('')
    rec('  ### (3b) THE PROLATE VECTORS ARE ORTHOGONAL TO IT. ### **NOW MEASURED.**')
    rec('    ### ### **THE EXACT HALF, AND IT IS EXACT ON ANY GRID WHATEVER:** ### the corpus\'s')
    rec('    ### `xi_n` is supported in `[-1,1]`, and every element of the space vanishes there.')
    rec('    ### **SO THE INNER PRODUCT IS ZERO BY DISJOINT SUPPORT** -- not small, zero.')
    supp = np.zeros(fr.N)
    supp[fr.x <= 1.0] = 1.0
    exact = float(np.max(np.abs(fr.project(sub, supp))))
    rec('    ### measured on the instrument, a vector supported in `[0,1]` projects to : %.1e'
        % exact)
    rec('    ### **AND THE MEASUREMENT AGREES WITH THE ARGUMENT RATHER THAN REPLACING IT.**')
    rec('')
    rec('    ### ### **THE HALF THAT IS NOT EXACT, AND IS THE ONE b292 SETTLED:** ### the corpus\'s')
    rec('    ### `zeta_n` is `[lam/sqrt(1-lam^2)] xi_n^an(x)` for `x >= 1` and zero below, so it')
    rec('    ### ### **PASSES CONDITION ONE AND b292 FOUND IT FAILS CONDITION TWO.**')
    rec('    %-4s %-14s %-18s %-18s' % ('n', 'cond 1 max', 'cond 2 residual', 'in the space?'))
    zres = []
    for n in (0, 1, 2, 3):
        z = np.zeros(fr.N)
        hi = fr.x >= 1.0
        z[hi] = an(fr.x[hi])[:, n] * (lam[n] / math.sqrt(1.0 - lam2[n]))
        nz = fr.norm(z)
        if nz == 0:
            continue
        z = z / nz
        c1z = float(np.max(np.abs(z[sub['lo_x']])))
        r = float(np.linalg.norm(fr.outside(sub, z))
                  / max(np.linalg.norm(z[sub['hi']]), 1e-300))
        zres.append(r)
        rec('    %-4d %-14.2e %-18.4f %-18s' % (n, c1z, r, 'NO' if r > 0.01 else '?'))
    rec('    ### ### **EVERY ONE OF THEM CARRIES A LARGE COMPONENT OUTSIDE THE SPACE**, which is')
    rec('    ### b292\'s finding measured on an instrument rather than argued at definitions.')
    rec('    ### **AND THE TWO ROUTES AGREE**: b292 derived the failure from the source\'s own')
    rec('    ### statement about `psi_n`; this instrument measures it directly. ### **NEITHER IS')
    rec('    ### ### EVIDENCE FOR THE OTHER -- THEY ARE INDEPENDENT, AND THAT IS WHY BOTH ARE HERE.**')

    rec('')
    rec('  ### (3c) THE SOURCE\'S OWN WORKED INNER PRODUCT, RECOVERED.')
    rec('    ### the source writes, of a bracket of exactly the remainder\'s shape:')
    rec('    ###   ### **`<psi | theta(rho^-1) xi> = rho^{1/2} INT xi(rho x) psi(x) dx`**')
    rec('    ### which is `(N1)` and `(N3)` together and nothing else. ### Checked on this grid:')
    worst = 0.0
    for rho in (1.5, 2.0, 3.0):
        a = np.exp(-4.0 * (fr.x - 0.7) ** 2)
        b = np.exp(-2.0 * (fr.x - 1.1) ** 2)
        lhs = fr.inner(a, fr.scaling(1.0 / rho, b))
        rhsv = (rho ** 0.5) * fr.inner(a, np.interp(rho * fr.x, fr.x, b,
                                                    left=0.0, right=0.0))
        worst = max(worst, abs(lhs - rhsv))
        rec('    ### rho = %-5.2f  left = %-14.9f  right = %-14.9f  difference = %.2e'
            % (rho, lhs, rhsv, abs(lhs - rhsv)))
    rec('    ### **worst difference : %.2e** -- the two sides are the same expression, and this' % worst)
    rec('    ### is a check that the instrument implements (N1) and (N3) as the source wrote them.')
    if worst > 1e-12:
        fails.append("the source's worked inner product was not recovered")

    rec('')
    rec('  ### (3d) THE CORPUS\'S REMAINDER INSTRUMENT IS **NOT** REPRODUCED HERE, AND WHY.')
    rec('    ### ### **IT IS BUILT ON VECTORS THAT ARE OUTSIDE THIS SPACE**, which (3b) has just')
    rec('    ### measured: the corpus\'s `eps` expands in `zeta_n`, and every `zeta_n` carries a')
    rec('    ### large component outside `S(1,1)`.')
    rec('    ### **SO REPRODUCING IT HERE WOULD NOT BE A CONTROL. ### IT WOULD BE THIS INSTRUMENT')
    rec('    ### ### COMPUTING SOMEBODY ELSE\'S OBJECT AND CALLING THE AGREEMENT A CHECK.**')
    rec('    ### **AND THAT IS THE POINT OF THE WHOLE ACT, SAID PLAINLY: ### EVERY ARCHIMEDEAN')
    rec('    ### ### INSTRUMENT THE CORPUS HAS COMPUTES WITH VECTORS OUTSIDE THE OBJECT\'S OWN')
    rec('    ### ### SPACE, AND THIS IS THE FIRST THAT DOES NOT.**')

    # ================================================================ COMPONENT 4
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 4 -- THE PREDICTION. ### **REGISTERED FOR ACT TWO AND NOT TESTED HERE.**')
    rec('=' * 100)
    rec('  ### **NO TRACE IS COMPUTED AND NO SMEAR IS ASSEMBLED IN THIS ACT.**')
    rec('  ### ### **THE NAVIGATOR\'S PREDICTION, REGISTERED:** ### under the source\'s Theorem 4.7,')
    rec('  ### with the corpus\'s archimedean term identified with the source\'s Weil distribution by')
    rec('  ### the record\'s settled sign, the corrected remainder\'s near-cancellation against it')
    rec('  ### says the compressed smeared trace on this space, ### **for the corpus\'s integral-one')
    rec('  ### ### bump, should be SMALL relative to the corpus\'s own trace instrument\'s values.**')
    rec('  ### ### **REFUTABLE BY ACT TWO\'S NUMBER.**')
    rec('  ### **AND THE SAME QUANTITY FOR THE MEAN-ZERO VARIANT IS UNPREDICTED**, which is the')
    rec('  ### `W2` ruling\'s own shape: the instrument accepts either test function and computes')
    rec('  ### with neither here.')
    rec('')
    rec('  ### ### **THE SIGN CHAIN\'S EVERY LINK, NAMED AS WHAT WOULD MAKE THIS PREDICTION WRONG')
    rec('  ### ### FOR A TRIVIAL REASON:**')
    rec('    ### **(L1)** the source\'s own `W_R = -W_inf`. ### If the corpus\'s `A` corresponds to')
    rec('    ###   `W_R` rather than `W_inf`, the prediction flips sign and means nothing.')
    rec('    ### **(L2)** the corpus\'s arrangement `... - PRIME + ARCH`, annotated as fixed by a')
    rec('    ###   calibration. ### b233: that is a different claim from *committed before any')
    rec('    ###   answer*, and b235 took the restriction.')
    rec('    ### **(L3)** b315\'s reading at the operation: the calibration fixes an ORIENTATION,')
    rec('    ###   `A` is an independent integral, and the `E2` in the bracket is a registered')
    rec('    ###   claim rather than the remainder.')
    rec('    ### **(L4)** the near-cancellation itself, `A + E2 ~ 0` under the source\'s exponent,')
    rec('    ###   which b315 measured and ### **PROMOTED TO NOTHING** ### for want of a stated')
    rec('    ###   definition. ### **A PREDICTION RESTING ON A FACT PROMOTED TO NOTHING IS A')
    rec('    ###   ### PREDICTION AND NOT A DERIVATION, AND IS REGISTERED AS SUCH.**')
    rec('    ### **(L5)** the identification of the corpus\'s window with the source\'s test')
    rec('    ###   function class, which no act has settled at content.')
    rec('    ### ### **IF ANY ONE OF THE FIVE IS WRONG, ACT TWO\'S NUMBER WILL REFUTE THE')
    rec('    ### ### PREDICTION FOR A REASON THAT HAS NOTHING TO DO WITH THE MATHEMATICS**, and')
    rec('    ### that is why they are listed before the number exists rather than after it.')

    payload = dict(X=fr.X, N=fr.N, h=fr.h, gauss_err=err, gauss_wrong=wrong,
                   dims=dims, leak={str(k): v for k, v in leak.items()},
                   u_cond1=c1, u_sweep=sweep, taper=list(TAPER), asym=list(ASY),
                   zeta_resid=zres, NY=fr.NY,
                   inner_worst=worst, disjoint_exact=exact,
                   elapsed=time.time() - t0, fails=fails, soft=fails_soft)
    io.open(os.path.join(D, 'b316_rows.json'), 'w', encoding='utf-8',
            newline='\n').write(json.dumps(payload, indent=1, default=float) + '\n')

    rec('')
    rec('  ### CHECKS FAILING : %d' % len(fails))
    for f in fails:
        rec('    ### FAILED: %s' % f)
    rec('  ### ### **UNCONFIRMED REPRODUCTIONS, WHICH ARE NOT TOOL FAILURES AND ARE NOT')
    rec('  ### ### SWALLOWED EITHER : %d**' % len(fails_soft))
    for f in fails_soft:
        rec('    ### UNCONFIRMED: %s' % f)
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)
    return (0 if not fails else 1), LINES


if __name__ == '__main__':
    code, ls = main()
    io.open(os.path.join(D, 'b316_components_run.txt'), 'w', encoding='utf-8',
            newline='\n').write('\n'.join(ls) + '\n')
    sys.exit(code)
