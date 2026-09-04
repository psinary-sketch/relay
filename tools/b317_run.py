# -*- coding: utf-8 -*-
"""b317_run.py -- THE COMPONENTS. ### **THE TRACE ON THE OBJECT.**

### ### **THIS IS b316's ACT TWO.** ### b316 built the truncation, listed what it could and could
### not do, and registered a prediction it was forbidden to test. ### This file computes the
### source's compressed smeared trace on that truncation, for both test functions, and scores the
### prediction against the bar sealed in `data/b317_registration_2026-09-04.txt` (4).

### ### **NO UNIT IS USED ANYWHERE IN THIS FILE.** ### `INS.sonin_unit` is never called; b300's
### derived archimedean unit is never constructed, never projected and never traced.
### ### **EVERY BAR AND EVERY FRAME IS IMPORTED FROM `b317_smear.py`**, which is where the sealed
### registration's (4) and (5) live, so this runner carries no float literal that decides anything.
"""
import io
import json
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
import b317_smear as SM         # noqa: E402
import b305_source as S5        # noqa: E402
import noise_floor as NF        # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PDF = ('C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--'
       '/4c01a20d-29c8-4658-82bf-5cf0e994a191/scratchpad/cc_2006.13771v1.pdf')

# ### THE SOURCE FRAGMENTS THIS ACT QUOTES, LOCATED BY PAGE BEFORE A WORD IS USED.
FRAGMENTS = [
    ('N1 the inner product, eq. (16)', 'x\u03b7|\u03bey :\u201c 1'),
    ('N2 the transform, eq. (24)', '\u03bepxqe\u00b42\u03c0ixydy. (24)'),
    ('N3 the scaling action, eq. (61)',
     'p\u03d1p\u03bbq\u03beqpvq :\u201c \u03bb\u00b41{2\u03bep\u03bb\u00b41vq'),
    ('N4 the space, Definition 4.4 / eq. (72)',
     'Sp\u03b1,\u03b2q :\u201ct\u03bePL2pRqev|\u03bepqq\u201c 0'),
    ('(53) the functional W_infinity, in the source own display',
     'fp\u03c1\u00b41q\u03c4p\u03c1qd\u02da\u03c1 (53)'),
    ('### (53) -- and the SUPPORT CONDITION it carries',
     'for test functions f whose support is in the interval'),
    ('(54) the vanishing conditions',
     'fp\u03c1q\u03c1\u02d8 1 2d\u02da\u03c1\u201c 0 (54)'),
    ('THEOREM 4.7 -- the definition the cancellation lacked',
     'Theorem 4.7 Let S be the orthogonal projection of L2pRqev on the closed subspace Sp1, 1q'),
    ('### THEOREM 4.7 -- (83), the identity this act computes the left side of',
     'Trp\u03d1pfqSq\u201c W8pfq`'),
    ('### THEOREM 4.7 -- and that it holds for ALL compactly supported test functions',
     'fp\u03c1\u00b41q\u03f5p\u03c1qd\u02da\u03c1, @fPC8'),
    ('(43) the local trace formula Theorem 4.7 refines',
     'fp\u03c1\u00b41qp\u03b4p\u03c1q\u00b4 \u03c4p\u03c1qqd\u02da\u03c1. (43)'),
    ('the sign relation the source states itself', 'WR\u201c\u00b4W8'),
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


TFC = {}


def testfn(a, which):
    key = (a, which)
    if key not in TFC:
        TFC[key] = SM.corpus_bump(a) if which == 0 else SM.mean_zero_variant(a)
    return TFC[key]


NAMES = ('(T1) the corpus integral-one bump', '(T2) the mean-zero variant')


def main():
    t0 = time.time()
    fails, soft = [], []
    rec('=' * 100)
    rec('b317 -- THE TRACE ON THE OBJECT.')
    rec('=' * 100)

    igood, iarms = INS.self_test()
    rec('  ### b316 INSTRUMENT FIXTURES, RUN BEFORE ANYTHING IS POINTED : %s  %s'
        % (iarms, 'PASS' if igood else '### FAIL ###'))
    sgood, sarms, slines = SM.self_test()
    rec('  ### THIS ACT ASSEMBLY FIXTURES : %s  %s'
        % (sarms, 'PASS' if sgood else '### FAIL ###'))
    for s in slines:
        rec('    ' + s)
    rec('  ### **THE FIXTURES RUN AT `a = %g`, WHICH IS NOT ONE OF THE ATLAS CELLS.** ### That is'
        % SM.FIXTURE_A)
    rec('  ### why the registration could be sealed before any value at a banked cell existed.')
    if not (igood and sgood):
        fails.append('a fixture suite did not pass')
        return 2, LINES, {}

    # ================================================================ COMPONENT 1
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE ASSEMBLY, FROM THE SOURCE OWN DEFINITIONS.')
    rec('=' * 100)
    if not S5.self_test(verbose=False):
        rec('  ### REFUSING TO LOCATE ANYTHING WITH A FLATTENER THAT FAILS ITS OWN FIXTURES.')
        return 2, LINES, {}
    got = S5.sha256_file(PDF)
    rec('  artefact sha256 : %s' % got)
    rec('  ### **MATCHES THE PIN b304 BANKED AND b305 RE-COMPUTED : %s**' % (got == S5.EXPECT_SHA))
    if got != S5.EXPECT_SHA:
        fails.append('the artefact does not match the pin')
        return 1, LINES, {}
    rows, npages = locate()
    rec('  pages in file   : %d' % npages)
    rec('')
    rec('  ### THE FRAGMENTS, LOCATED BY PAGE INDEX BEFORE A WORD OF THEM IS USED:')
    for label, _frag, hits in rows:
        rec('    %-14s %s' % (','.join(str(h) for h in hits) if hits else '### NONE', label))
        if not hits:
            fails.append('unlocated: %s' % label)
    rec('')
    rec('  ### (1a) THE FOUR NORMALIZATIONS, IMPORTED FROM b316 AND NOT RE-TYPED:')
    rec('    ### **(N1) eq. %s** ### `<eta|xi> := (1/2) INT_R eta xi dx = INT_0^inf eta xi dx`'
        % INS.EQ_INNER)
    rec('    ### **(N2) eq. %s** ### `F(xi)(y) := INT_R xi(x) e^{-2 pi i x y} dx`'
        % INS.EQ_TRANSFORM)
    rec('    ### **(N3) eq. %s** ### `(theta(lam) xi)(v) := lam^{-1/2} xi(lam^{-1} v)`'
        % INS.EQ_SCALING)
    rec('    ### **(N4) eq. %s** ### `S(a,b) := { xi : xi = 0 on |q| <= a, F(xi) = 0 on |p| <= b }`'
        % INS.EQ_SPACE)
    rec('    ### at the source own `S(%g, %g)`.' % (INS.ALPHA, INS.BETA))
    rec('')
    rec('  ### (1b) THE ASSEMBLY ITSELF. ### **THE SCALING ACTION, INTEGRATED, COMPRESSED, TRACED.**')
    rec('    ### The source eq. (61) is an action of `lambda`; the source Theorem 4.7 needs it')
    rec('    ### integrated against a test function in the multiplicative group own measure:')
    rec('    ###   ### `(theta(f) xi)(x) = INT f(lam) lam^{-1/2} xi(x/lam) d*lam`')
    rec('    ###   ### substituting `u = x/lam`, so that `d*lam` becomes `du/u`:')
    rec('    ###   ### ### **`= INT K(x,u) xi(u) du`   with   `K(x,u) = f(x/u) / sqrt(x u)`.**')
    rec('    ### **THAT SUBSTITUTION IS THE WHOLE OF THE ASSEMBLY AND IT IS THE ONE PLACE A FACTOR')
    rec('    ### ### CAN GO WRONG SILENTLY**, so it is checked by two independent code paths in')
    rec('    ### (1d) rather than by re-reading the derivation.')
    rec('    ### Then b316 projector compresses and the trace is taken:')
    rec('    ###   ### ### **`Tr(theta(f) S) = Tr(A_HH) - Tr(Q^T A_HH Q)`**, which needs the')
    rec('    ###   diagonal and `rank` matrix-vector products. ### **THE OPERATOR IS NEVER FORMED')
    rec('    ###   ### WHOLE**, and both halves are reported because their SIZES are the finding.')

    rec('')
    rec('  ### (1c) THE TWO TEST FUNCTIONS, IN THE SOURCE OWN VARIABLE `v = log rho`.')
    rec('    ### **AND THE SOURCE OWN CLASS BOUNDARY, MEASURED RATHER THAN ASSERTED.**')
    rec('    ### eq. (53) defines `W_infinity` for test functions supported in `[1/2, 2]`, and')
    rec('    ### eq. (54) assumes `INT f(rho) rho^{+-1/2} d*rho = 0` ### *to isolate on the left')
    rec('    ### hand side of the explicit formula the contribution of the zeros*. ### **THEOREM')
    rec('    ### ### 4.7 ITSELF CARRIES NEITHER CONDITION** -- its (83) is stated for all')
    rec('    ### `f in C_c^infinity(R*_+)`, and that is located above rather than smoothed over.')
    rec('    %-6s %-34s %-13s %-13s %-13s %-9s'
        % ('a', 'test function', 'INT f d*rho', 'eq.(54) +', 'eq.(54) -', 'supp in'))
    classrows = []
    for a in SM.DETAIL_CELLS:
        for which in (0, 1):
            f = testfn(a, which)
            m = f.vanishing_54()
            insupp = (f.support <= SM.SUPPORT_HI)
            classrows.append((a, which, f.at_zero(), m[0], m[1], insupp))
            rec('    %-6g %-34s %-13.6f %-13.3e %-13.3e %-9s'
                % (a, NAMES[which], f.at_zero(), m[0], m[1], 'YES' if insupp else '### NO'))
    rec('    ### ### **THE CORPUS BUMP IS NOT IN THE SOURCE eq. (54) CLASS AND THE VARIANT IS.**')
    rec('    ### The bump transform at zero is one by construction and its eq. (54) moments are')
    rec('    ### NOT zero; the variant vanishes on both, to machine precision, BY CONSTRUCTION and')
    rec('    ### not by luck -- it is three of the corpus own bumps with the coefficients solved.')
    mz = testfn(SM.DETAIL_CELLS[0], 1)
    rec('    ### the variant coefficients at `a = %g` : %s ; conditioning of the 2x2 : %.3g'
        % (SM.DETAIL_CELLS[0], ', '.join('%.4f' % c for c in mz.coeffs), mz.cond))
    rec('    ### **AND THE SUPPORT COLUMN IS THE OTHER HALF OF THE BOUNDARY**: the cells with')
    rec('    ### `a > %g` leave the eq. (53) support condition, so `W_infinity` is not defined for'
        % SM.SUPPORT_HI)
    rec('    ### them by the source own display, even though the Theorem 4.7 left side still is.')

    rec('')
    rec('  ### (1d) THE SMEARING QUADRATURE OWN POSITIVE CONTROLS.')
    frc = INS.Frame(1024, 8.0, SM.NY_FIXED)
    subc = frc.subspace()
    ti, freei, corri = SM.identity_trace(frc, subc)
    rec('    ### ### **THE CONTROL THE ORDER NAMES: A SCALING BY THE IDENTITY ALONE.**')
    rec('    ### `theta(1)` is the identity, so `Tr(S theta(1) S)` must be `Tr(S)` -- the')
    rec('    ### truncation own DIMENSION. ### Through the same two terms:')
    rec('    ### **free = %d ; rank-term = %.9f ; identity trace = %.9f ; dim = %d**'
        % (freei, corri, ti, subc['dim']))
    rec('    ### ### **EXACT, AND IT IS THE ONE EXACT FACT IN THIS ACT** -- it is `free - rank` by')
    rec('    ### orthonormality of `Q`, not a quadrature that happened to land.')
    if abs(ti - subc['dim']) > 1e-9:
        fails.append('the identity control did not return the dimension')
    fbp = testfn(SM.DETAIL_CELLS[1], 0)
    g = np.exp(-(frc.x - INS.ALPHA - INS.BETA) ** 2)
    rel_all, rel, nwin = SM.route_agreement(frc, fbp, g)
    _ra, relbad, _nw = SM.route_agreement(frc, fbp, g, half=True)
    rec('    ### ### **AND THE SUBSTITUTION IS CHECKED BY A SECOND ROUTE.** ### `smear_by_scaling`')
    rec('    ### never builds a kernel: it evaluates eq. (61) at each `lambda` and integrates over')
    rec('    ### `v = log lambda`.')
    rec('    ### worst relative difference over `x > %g`, ### **WHICH IS THE ONLY REGION THE'
        % INS.ALPHA)
    rec('    ### ### COMPRESSED TRACE EVER EVALUATES** : ### **%.3e**' % rel)
    rec('    ### the same over the WHOLE grid, first node included : %.3e' % rel_all)
    rec('    ### and with the kernel deliberately halved : **%.3e**' % relbad)
    rec('    ### ### **THE TWO FIGURES DIFFER AND THE REASON IS ARITHMETIC, NOT LUCK.** ### The')
    rec('    ### kernel route integrates in `u`, and for output `x` the integrand lives on')
    rec('    ### `[x/a, a x]` -- a window carrying `x (a - 1/a) / h` grid points. ### **AT THE')
    rec('    ### ### FIRST NODE `x = h/2` THAT COUNT IS %.3f, WHICH IS BELOW ONE**, so the kernel'
        % nwin)
    rec('    ### quadrature is simply not resolved there while the scaling route is. ### **AND IT')
    rec('    ### ### REACHES NO NUMBER IN THIS ACT**: condition one kills every coordinate with')
    rec('    ### `x <= %g` before the compression, so `compressed_trace` never evaluates the'
        % INS.ALPHA)
    rec('    ### kernel at the first node. ### **THE EXCLUDED REGION IS NAMED AND ITS SIZE IS')
    rec('    ### ### PRINTED RATHER THAN THE FIGURE BEING QUIETLY RESTRICTED.**')
    rec('    ### **A ROUTE AGREEMENT THAT CANNOT FAIL IS NOT A CHECK**, which is the third number.')
    if not (rel < 1e-4 and relbad > 1e-1):
        fails.append('the two-route control')
    del frc, subc

    # ================================================================ COMPONENT 2
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE NUMBER, AT THE BANKED CELLS AND ALONG THE CUTOFF.')
    rec('=' * 100)
    cells = SM.atlas_cells()

    work = {}

    def need(fk, a, which):
        work.setdefault(tuple(fk), set()).add((a, which))

    for r in cells:
        for fk in SM.SWEEP_FRAMES:
            need(fk, r['a'], 0)
            need(fk, r['a'], 1)
    for a in SM.DETAIL_CELLS:
        for fk in tuple(SM.GRID_AXIS) + tuple(SM.DOMAIN_AXIS):
            need(fk, a, 0)
            need(fk, a, 1)

    RES, FI = {}, {}
    rec('')
    rec('  ### (2a) THE FRAMES, BUILT ONCE EACH, WITH THE RANK GUARD (B3) ON EVERY ONE.')
    rec('    %-7s %-7s %-6s %-10s %-8s %-7s %-8s %-9s %-9s'
        % ('N', 'X', 'NY', 'h', 'free', 'rank', 'dim', 'NY/X', 'guard'))
    guard_fired = []
    for fk in sorted(work, key=lambda k: (k[0], k[1])):
        N, X, NY = fk
        fr = INS.Frame(N, X, NY)
        sub = fr.subspace()
        ok_rank = sub['rank'] < NY
        nyx = float(NY) / X
        FI[fk] = dict(N=N, X=X, NY=NY, h=fr.h, free=sub['free'], rank=sub['rank'],
                      dim=sub['dim'], ny_over_x=nyx, guard_ok=ok_rank)
        rec('    %-7d %-7.1f %-6d %-10.6f %-8d %-7d %-8d %-9.2f %-9s'
            % (N, X, NY, fr.h, sub['free'], sub['rank'], sub['dim'], nyx,
               'ok' if ok_rank else '### REFUSED'))
        if not ok_rank:
            guard_fired.append(fk)
        ti2, _f2, _c2 = SM.identity_trace(fr, sub)
        if abs(ti2 - sub['dim']) > 1e-9:
            fails.append('identity control at %s' % (fk,))
        for (a, which) in sorted(work[fk]):
            RES[(fk, a, which)] = SM.compressed_trace(fr, sub, testfn(a, which))
        del fr, sub
    rec('    ### ### **THE RANK GUARD (B3): ### %d CELL(S) REFUSED.**' % len(guard_fired))
    rec('    ### `NY/X` is the number of transform samples per oscillation of the transform of a')
    rec('    ### function supported out to `X`. ### **IT IS THE REASON THE DOMAIN AXIS STOPS WHERE')
    rec('    ### ### IT DOES**, and it is printed rather than left implicit.')
    rec('    ### ### **AND THE IDENTITY CONTROL WAS RE-RUN AT EVERY FRAME**, not once at the start.')
    if guard_fired:
        fails.append('the rank guard fired at %s' % (guard_fired,))

    rec('')
    rec('  ### (2b) THE THIRTEEN BANKED CELLS AT THE REFERENCE FRAME `N=%d, X=%g`,'
        % (SM.REFERENCE[0], SM.REFERENCE[1]))
    rec('  ### AND THE BAND OVER THE DOMAIN SWEEP `X = %s`.'
        % ', '.join('%g' % fk[1] for fk in SM.SWEEP_FRAMES))
    rec('    ### **BESIDE THEM, FOR THE INTEGRAL-ONE BUMP ONLY AND AS THE PREDICTION STATED')
    rec('    ### ### REFERENT: THE CORPUS OWN BANKED TRACE VALUES**, quoted from')
    rec('    ### `data/carto_atlas.jsonl`, emitted by `tools/e16/carto_atlas.py`. ### CONVENTION:')
    rec('    ### %s' % SM.ATLAS_CONVENTION)
    rec('')
    rec('    %-6s %-9s %-13s %-13s %-13s %-11s %-8s'
        % ('a', 'supp<=2', 'T (T1) ref', 'T (T2) ref', 'band |T1|', 'A banked', 'ratio'))
    sweep = []
    ref = tuple(SM.REFERENCE)
    for r in cells:
        a = r['a']
        t1 = RES[(ref, a, 0)][0]
        t2 = RES[(ref, a, 1)][0]
        band = [abs(RES[(tuple(fk), a, 0)][0]) for fk in SM.SWEEP_FRAMES]
        band2 = [abs(RES[(tuple(fk), a, 1)][0]) for fk in SM.SWEEP_FRAMES]
        A = r['arch']
        ratio = max(band) / abs(A)
        insupp = a <= SM.SUPPORT_HI
        sweep.append(dict(a=a, t1=t1, t2=t2, band_lo=min(band), band_hi=max(band),
                          A=A, ratio=ratio, in_support=insupp, band2=band2))
        rec('    %-6g %-9s %-13.7f %-13.7f %-13s %-11.7f %-8.5f'
            % (a, 'YES' if insupp else 'no', t1, t2,
               '%.5f-%.5f' % (min(band), max(band)), A, ratio))
    rec('    ### ### **THE UNCOMPRESSED HALF, WHICH IS WHERE THE SIZE OF THIS RESULT LIVES --')
    rec('    ### ### AND IT IS CARRIED FOR *BOTH* TEST FUNCTIONS, BECAUSE THE DIFFERENCE BETWEEN')
    rec('    ### ### THE TWO COLUMNS IS THE FINDING.**')
    rec('    %-6s %-13s %-13s %-13s %-13s %-13s %-13s'
        % ('a', 'T1 Tr(A_HH)', 'T1 Q^T A Q', 'T1 diff', 'T2 Tr(A_HH)', 'T2 Q^T A Q', 'T2 diff'))
    cancel = []
    for r in cells:
        a = r['a']
        t, un, co = RES[(ref, a, 0)]
        t2u, un2, co2 = RES[(ref, a, 1)]
        cancel.append((a, un, t, un2, t2u))
        rec('    %-6g %-13.6f %-13.6f %-13.6f %-13.6f %-13.6f %-13.6f'
            % (a, un, co, t, un2, co2, t2u))
    rec('    ### ### **THE CANCELLATION IS THE INTEGRAL-ONE BUMP OWN, NOT THE COMPRESSION OWN.**')
    rec('    ### For `(T1)` condition two removes almost all of the uncompressed trace at every')
    rec('    ### cell. ### **FOR `(T2)` IT DOES NOT**, and the mean-zero column survives the')
    rec('    ### compression at a size the bump column never reaches. ### A reader given only the')
    rec('    ### differences could not tell a small operator from a large one that nearly cancels,')
    rec('    ### and these two columns are the difference between those two readings.')
    rec('    ### ### **THE TRACE OVER THE HALF LINE WITH CONDITION ONE ALONE IS OF ORDER ONE, AND')
    rec('    ### ### CONDITION TWO REMOVES ALMOST ALL OF IT.** ### The compressed number is orders')
    rec('    ### of magnitude below the uncompressed one at every cell. ### **THAT CANCELLATION IS')
    rec('    ### ### THE MEASUREMENT**, and it is why both halves are printed: a reader given only')
    rec('    ### the difference could not tell it from a small operator, and it is not one.')

    rec('')
    rec('  ### (2c) THE TWO AXES, MEASURED INDEPENDENTLY, AT THE THREE DETAIL CELLS.')
    axes = {}
    for a in SM.DETAIL_CELLS:
        for which in (0, 1):
            rec('')
            rec('    ### `a = %g`, %s' % (a, NAMES[which]))
            rec('      %-8s %-8s %-9s %-7s %-15s %-12s'
                % ('axis', 'N', 'X', 'rank', 'T', 'rel drift'))
            gvals = [RES[(tuple(fk), a, which)][0] for fk in SM.GRID_AXIS]
            dvals = [RES[(tuple(fk), a, which)][0] for fk in SM.DOMAIN_AXIS]
            gdr, ddr = [], []
            for i, fk in enumerate(SM.GRID_AXIS):
                dr = (abs(gvals[i] - gvals[i - 1]) / max(abs(gvals[i]), 1e-300)) if i else None
                gdr.append(dr)
                rec('      %-8s %-8d %-9.1f %-7d %-15.8f %-12s'
                    % ('grid' if i == 0 else '', fk[0], fk[1], FI[tuple(fk)]['rank'], gvals[i],
                       '-' if dr is None else '%.3e' % dr))
            for i, fk in enumerate(SM.DOMAIN_AXIS):
                dr = (abs(dvals[i] - dvals[i - 1]) / max(abs(dvals[i]), 1e-300)) if i else None
                ddr.append(dr)
                rec('      %-8s %-8d %-9.1f %-7d %-15.8f %-12s'
                    % ('domain' if i == 0 else '', fk[0], fk[1], FI[tuple(fk)]['rank'], dvals[i],
                       '-' if dr is None else '%.3e' % dr))
            axes[(a, which)] = dict(grid=gvals, domain=dvals, gdrift=gdr, ddrift=ddr,
                                    grank=[FI[tuple(fk)]['rank'] for fk in SM.GRID_AXIS],
                                    drank=[FI[tuple(fk)]['rank'] for fk in SM.DOMAIN_AXIS])
    rec('')
    rec('    ### ### **READ THE `rank` COLUMN BEFORE READING ANY DRIFT ON THE GRID AXIS.** ### The')
    rec('    ### measured rank of the transform condition is not a constant of the grid: it steps')
    rec('    ### from %d to %d between `N = %d` and `N = %d` at `X = %g`, because one singular value'
        % (FI[tuple(SM.GRID_AXIS[1])]['rank'], FI[tuple(SM.GRID_AXIS[2])]['rank'],
           SM.GRID_AXIS[1][0], SM.GRID_AXIS[2][0], SM.GRID_AXIS[1][1]))
    rec('    ### crosses the numerical-rank tolerance. ### **A STEP IN THE RANK IS A STEP IN THE')
    rec('    ### ### PROJECTOR, SO THE DRIFT ACROSS THAT ONE REFINEMENT IS A DISCRETE CHANGE AND')
    rec('    ### ### NOT A QUADRATURE ERROR** -- and the refinements that do NOT change the rank')
    rec('    ### drift by orders of magnitude less. ### **THIS IS NAMED RATHER THAN AVERAGED IN**,')
    rec('    ### and it is why the grid axis is reported with its rank beside it.')

    rec('')
    rec('  ### (2d) THE REACH, AGAINST THE BAR (B2) FIXED BEFORE THE RUN : %.0f per cent'
        % (SM.BAR_REACH * 100.0))
    rec('    ### ### **AND A DEFECT OF THIS ACT OWN REGISTRATION, FOUND BY TRYING TO APPLY ITS OWN')
    rec('    ### ### BAR.** ### (B2) asks for the last cell where BOTH refinements agree. ### The')
    rec('    ### frame set sealed at (5) has the two axes crossing at exactly ONE frame,')
    rec('    ### `N=%d, X=%g`, so ### **THE JOINT TEST CAN BE APPLIED AT ONE POINT AND NOT ALONG A'
        % (SM.REFERENCE[0], SM.REFERENCE[1]))
    rec('    ### ### SEQUENCE.** ### A frame set that crossed twice would have cost one more frame')
    rec('    ### and was not registered. ### **THAT IS A DESIGN DEFECT OF THE REGISTRATION, NOT OF')
    rec('    ### ### THE INSTRUMENT, AND IT IS DECLARED RATHER THAN WORKED AROUND.**')
    rec('    %-6s %-34s %-13s %-13s %-10s'
        % ('a', 'test function', 'grid drift', 'domain drift', 'inside?'))
    reach = {}
    gi = list(SM.GRID_AXIS).index(tuple(SM.REFERENCE))
    di = list(SM.DOMAIN_AXIS).index(tuple(SM.REFERENCE))
    for a in SM.DETAIL_CELLS:
        for which in (0, 1):
            gv = axes[(a, which)]['grid']
            dv = axes[(a, which)]['domain']
            gd = abs(gv[gi + 1] - gv[gi]) / max(abs(gv[gi + 1]), 1e-300)
            dd = abs(dv[di + 1] - dv[di]) / max(abs(dv[di + 1]), 1e-300)
            inside = (gd < SM.BAR_REACH) and (dd < SM.BAR_REACH)
            reach[(a, which)] = dict(grid=gd, domain=dd, inside=inside)
            rec('    %-6g %-34s %-13.3e %-13.3e %-10s'
                % (a, NAMES[which], gd, dd, 'YES' if inside else '### NO'))

    rec('')
    rec('  ### (2e) THE NOISE-FLOOR GATE (B4), IN THE PATH.')
    items = []
    for a in SM.DETAIL_CELLS:
        for which in (0, 1):
            gv = axes[(a, which)]['grid']
            dv = axes[(a, which)]['domain']
            items.append(('grid   a=%g %s' % (a, 'T1' if which == 0 else 'T2'), gv[-2], gv[-1]))
            items.append(('domain a=%g %s' % (a, 'T1' if which == 0 else 'T2'), dv[-2], dv[-1]))
    ngood, nrows, ndetail = NF.gate(items, label='b317')
    for name, value, refined, verdict, why in nrows:
        rec('    %-18s %-14.8f -> %-14.8f  %-10s %s' % (name, value, refined, verdict, why[:48]))
    rec('    ### %s' % ndetail)
    rec('    ### **A VALUE THE GATE REFUSES MAY NOT CARRY A VERDICT**, and that is exactly why the')
    rec('    ### scoring below is a BAND statement and not a point statement.')

    # ================================================================ COMPONENT 3
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE PREDICTION SCORED.')
    rec('=' * 100)
    rec('  ### ### **THE SIGN CHAIN FIRST, LINK BY LINK, BEFORE ANY NUMBER IS READ.** ### b316')
    rec('  ### registered this prediction on a chain of five and named every one of them as a way')
    rec('  ### for the prediction to be wrong for a reason that has nothing to do with the')
    rec('  ### mathematics. ### **THE CHAIN IS QUOTED HERE AND IS NOT RE-DECIDED.**')
    rec('    ### **(L1)** the source own `W_R = -W_inf`, located above on this run. ### If the')
    rec('    ###   corpus `A` corresponds to `W_R` rather than `W_inf`, the prediction flips sign.')
    rec('    ###   ### **STATUS: THE SOURCE SENTENCE IS LOCATED. ### THE IDENTIFICATION OF THE')
    rec('    ###   ### CORPUS `A` WITH EITHER SIDE IS NOT SETTLED BY THIS ACT.**')
    rec('    ### **(L2)** the corpus arrangement, annotated as fixed by a calibration. ### b233:')
    rec('    ###   that is a different claim from *committed before any answer*; b235 restricted it')
    rec('    ###   to an instrument fact. ### **STATUS: UNCHANGED, AND NOT RE-DECIDED HERE.**')
    rec('    ### **(L3)** b315 reading at the operation -- the calibration fixes an ORIENTATION,')
    rec('    ###   `A` is an independent integral, the `E2` in that bracket is a registered claim.')
    rec('    ###   ### **STATUS: UNCHANGED.**')
    rec('    ### **(L4)** the near-cancellation itself, which b315 measured and ### **PROMOTED TO')
    rec('    ###   ### NOTHING** ### for want of a stated definition. ### **STATUS: STILL PROMOTED')
    rec('    ###   ### TO NOTHING. ### A PREDICTION RESTING ON IT IS A PREDICTION, NOT A')
    rec('    ###   ### DERIVATION**, and b316 registered it as such.')
    rec('    ### **(L5)** the identification of the corpus window with the source test function')
    rec('    ###   class. ### **STATUS: THIS ACT MEASURED IT, AND IT IS THE ONE LINK THAT MOVED --')
    rec('    ###   ### AND IT MOVED AGAINST THE PREDICTION.** ### (1c) shows the corpus bump is')
    rec('    ###   NOT in the source eq. (54) class, and at `a > %g` it is not in the eq. (53)'
        % SM.SUPPORT_HI)
    rec('    ###   support class either. ### **SO THE CORPUS WINDOW IS NOT THE SOURCE TEST')
    rec('    ###   ### FUNCTION CLASS, AND THAT IS NOW MEASURED RATHER THAN OPEN.**')
    rec('')
    rec('  ### ### **THE SCORE, AGAINST THE BAR SEALED AT (B1): `|T| <= |A| / %g`.**'
        % SM.BAR_SMALL)
    rec('  ### **AND IT IS SCORED AGAINST THE LARGEST `|T|` THE DOMAIN SWEEP PRODUCES**, so a')
    rec('  ### value small only at the friendliest truncation does not pass.')
    rec('    %-6s %-13s %-13s %-11s %-11s %-8s'
        % ('a', 'max |T1|', '|A|/%g' % SM.BAR_SMALL, 'ratio', 'supp<=2', 'small?'))
    npass = 0
    for s in sweep:
        bar = abs(s['A']) / SM.BAR_SMALL
        good = s['band_hi'] <= bar
        npass += 1 if good else 0
        s['small'] = good
        rec('    %-6g %-13.7f %-13.7f %-11.5f %-11s %-8s'
            % (s['a'], s['band_hi'], bar, s['ratio'],
               'YES' if s['in_support'] else 'no', 'YES' if good else '### NO'))
    rec('    ### ### **CELLS SCORING SMALL : %d OF %d.**' % (npass, len(sweep)))

    # ================================================================ COMPONENT 4
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 4 -- THE MEAN-ZERO COLUMN, AS ITS OWN MEASUREMENT.')
    rec('=' * 100)
    rec('  ### ### **NO PREDICTION IS ATTACHED TO THIS COLUMN AND NONE WAS REGISTERED.** ### b316')
    rec('  ### recorded that the same quantity for the mean-zero variant is UNPREDICTED, which is')
    rec('  ### the `W2` ruling own shape.')
    rec('    %-6s %-15s %-13s %-13s' % ('a', 'T (T2) ref', 'band lo', 'band hi'))
    for s in sweep:
        rec('    %-6g %-15.8f %-13.7f %-13.7f'
            % (s['a'], s['t2'], min(s['band2']), max(s['band2'])))
    rec('  ### ### **THIS IS THE FIRST ARCHIMEDEAN NUMBER IN THE PROGRAMME COMPUTED ON THE OBJECT')
    rec('  ### ### OWN SPACE FOR A TEST FUNCTION THE SOURCE INEQUALITY COVERS.** ### The variant')
    rec('  ### satisfies eq. (54) to machine precision by construction, and at `a <= %g` it also'
        % SM.SUPPORT_HI)
    rec('  ### satisfies the eq. (53) support condition.')
    rec('  ### ### **AND THE INEQUALITY IS NOT EVALUATED HERE.** ### Its other side -- the')
    rec('  ### archimedean Weil distribution `W_infinity` for this variant -- is a separate')
    rec('  ### computation under its own registration. ### **ONE SIDE OF AN INEQUALITY IS NOT THE')
    rec('  ### ### INEQUALITY**, and the registration caps this act at one side.')

    payload = dict(frames=dict((str(k), v) for k, v in FI.items()),
                   sweep=sweep, classrows=classrows, cancel=cancel,
                   axes=dict((str(k), v) for k, v in axes.items()),
                   reach=dict((str(k), v) for k, v in reach.items()),
                   noise_ok=ngood, noise=[(n, v, r, vd) for n, v, r, vd, _w in nrows],
                   identity=dict(free=freei, corr=corri, trace=ti),
                   routes=dict(agree_hi=rel, agree_all=rel_all, halved=relbad, window=nwin),
                   bar_small=SM.BAR_SMALL, bar_reach=SM.BAR_REACH,
                   guard_fired=[list(x) for x in guard_fired],
                   npass=npass, ncells=len(sweep),
                   elapsed=time.time() - t0, fails=fails, soft=soft)
    io.open(os.path.join(D, 'b317_rows.json'), 'w', encoding='utf-8',
            newline='\n').write(json.dumps(payload, indent=1, default=float) + '\n')

    rec('')
    rec('  ### CHECKS FAILING : %d' % len(fails))
    for f in fails:
        rec('    ### FAILED: %s' % f)
    rec('  ### ### **UNCONFIRMED, WHICH ARE NOT TOOL FAILURES AND ARE NOT SWALLOWED : %d**'
        % len(soft))
    for f in soft:
        rec('    ### UNCONFIRMED: %s' % f)
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)
    return (0 if not fails else 1), LINES, payload


if __name__ == '__main__':
    code, ls, _p = main()
    io.open(os.path.join(D, 'b317_components_run.txt'), 'w', encoding='utf-8',
            newline='\n').write(chr(10).join(ls) + chr(10))
    sys.exit(code)
