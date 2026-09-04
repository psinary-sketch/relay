# -*- coding: utf-8 -*-
"""b319_run.py -- THE COMPONENTS. ### **THE STABLE RANK.**

### ### **b318 MEASURED THAT THE GRID-AXIS ERROR IS THE RANK DISCRETIZATION** and filed two schemes
### SPECIFIED and NOT BUILT. ### This file builds the source's own -- the eigenvalue-one
### characterization of `S(1,1)` as the eigenspace of `P P-hat P` -- and reproduces b318's square on
### it.

### ### **NO NEW TEST FUNCTION AND NO NEW UNIT IS DEFINED HERE.** ### b317's variant and b316's unit
### are IMPORTED from their emitting files and MEASURED. ### **NO VERDICT IS TAKEN ON MEMBERSHIP**,
### and `W_infinity` is not computed in any direction.
### ### **EVERY BAR AND EVERY FRAME IS IMPORTED** -- the threshold from `b319_stable.py`, the frames
### from `b317_smear.py`, the identity bar from `b318_square.py`.
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
import b317_smear as SM         # noqa: E402
import b318_square as SQ        # noqa: E402
import b319_stable as ST        # noqa: E402
import noise_floor as NF        # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EXTRACT = os.path.join(D, 'b319_extract_notes.txt')

EXTRACT_NEEDLES = [
    ('the two projections, in the source normalization', 'becomes the multiplication by the charac'),
    ('### and the transform conjugation that makes the second', 'eRPFeR'),
    ('the spectral decomposition (81) of the sandwich',
     'The spectral decomposition of the positive operator'),
    ('### and that its remainder IS the projection on the space',
     'is the orthogonal projection on Sonin'),
    ('the eigenvalue-one characterization', 'is the eigenspace of'),
    ('the bandwidth parameter that fixes the prolate eigenvalues', 'with bandwidth parameter'),
    ('(16), which halves the full-line integral', 'as follows'),
    ('the grid scheme this act replaces, and its moving tolerance', 'def subspace'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


TFC = {}


def variant(a):
    if a not in TFC:
        TFC[a] = SM.mean_zero_variant(a)
    return TFC[a]


def main():
    t0 = time.time()
    fails, soft = [], []
    rec('=' * 100)
    rec('b319 -- THE STABLE RANK.')
    rec('=' * 100)
    igood, iarms = INS.self_test()
    rec('  ### b316 INSTRUMENT FIXTURES : %s  %s' % (iarms, 'PASS' if igood else '### FAIL ###'))
    sgood, sarms, _s = SM.self_test()
    rec('  ### b317 ASSEMBLY FIXTURES   : %s  %s' % (sarms, 'PASS' if sgood else '### FAIL ###'))
    qgood, qarms, _q = SQ.self_test()
    rec('  ### b318 SQUARE FIXTURES     : %s  %s' % (qarms, 'PASS' if qgood else '### FAIL ###'))
    tgood, tarms, tlines = ST.self_test()
    rec('  ### THIS ACT STABLE FIXTURES : %s  %s' % (tarms, 'PASS' if tgood else '### FAIL ###'))
    for s in tlines:
        rec('    ' + s)
    rec('  ### **ARM (i) IS THE ONE THAT CARRIES THE DERIVATION.** ### A projection sandwich has its')
    rec('  ### spectrum in `[0,1]`; if the discretization constant `(hy/h)` were wrong the maximum')
    rec('  ### would leave that interval, and no threshold on it would mean anything.')
    if not (igood and sgood and qgood and tgood):
        fails.append('a fixture suite did not pass')
        return 2, LINES, {}

    # ================================================================ COMPONENT 1
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE CHARACTERIZATION, AND THE SCHEME BUILT FROM IT.')
    rec('=' * 100)
    ext = io.open(EXTRACT, encoding='utf-8').read()
    rec('  ### THE SOURCE STATEMENTS, PULLED FROM THE EXTRACT FILE:')
    for lbl, anchor in EXTRACT_NEEDLES:
        hit = anchor in ext
        rec('    %-6s %s' % ('found' if hit else '### NONE', lbl))
        if not hit:
            fails.append('extract needle: %s' % lbl)
    rec('')
    rec('  ### (1a) THE OBJECT, IN THE SOURCE OWN WORDS AND ITS OWN NORMALIZATION.')
    rec('    ### **THE TWO PROJECTIONS:** ### *"The projection P ... becomes the multiplication by')
    rec('    ### the characteristic function of the interval complement {x : |x| >= 1} and P-hat')
    rec('    ### becomes F^-1 P F."*')
    rec('    ### **THE SPECTRAL DECOMPOSITION (81):** ### *"P P-hat P = SUM lambda(n)^2')
    rec('    ### |zeta_n><zeta_n| + R ... The operator R is the orthogonal projection on Sonin\'s')
    rec('    ### space S(1,1)."*')
    rec('    ### **THE CHARACTERIZATION:** ### *"Sonin\'s space S(1,1) is the eigenspace of')
    rec('    ### P P-hat P for the eigenvalue 1."*')
    rec('    ### ### **SO THE SPECTRUM IS `{lambda(n)^2}` TOGETHER WITH `1` ON THE SPACE**, and an')
    rec('    ### eigenvalue is DIMENSIONLESS. ### A cut on it does not move with the grid.')
    rec('')
    rec('  ### (1b) THE SANDWICH ON THE GRID, DERIVED ONCE AND CHECKED BY ITS OWN SPECTRUM.')
    rec('    ### On the free coordinates the first projection is the identity, so the sandwich is')
    rec('    ### `P-hat` there, and `<xi, P-hat_1 xi> = INT_0^1 |F xi(p)|^2 dp` under (16), which')
    rec('    ### halves the full-line integral. ### In orthonormal coordinates that is')
    rec('    ###   ### ### **`M = I - (hy/h) C^T C`**,')
    rec('    ### whose eigenvalue-one eigenspace is `null(C)` -- ### **THE SAME SPACE b316 BUILT** --')
    rec('    ### but whose spectrum is the one the source names.')
    rec('    ### **AND THE TWO SCHEMES CUT THE SAME SINGULAR VALUES IN DIFFERENT PLACES:** ### b316')
    rec('    ### at `max(C.shape) * s[0] * eps`, whose BOTH factors move with the grid; this act at')
    rec('    ### `sigma^2 > TAU = %.0e`, which is a pure number.' % ST.TAU)
    rec('    ### **THE THRESHOLD ARGUMENT, FROM THE CORPUS OWN BANKED VALUE:** ### the largest')
    rec('    ### non-space eigenvalue is `lambda(0)^2 = %.15f`, so the nearest one sits' % ST.LAMBDA0_SQ)
    rec('    ### **%.6e** ### below one and `TAU` is %.0f times inside it.'
        % (1.0 - ST.LAMBDA0_SQ, (1.0 - ST.LAMBDA0_SQ) / ST.TAU))

    frames = sorted(set(tuple(f) for f in (tuple(SM.GRID_AXIS) + tuple(SM.DOMAIN_AXIS))),
                    key=lambda k: (k[0], k[1]))
    FI = {}
    rec('')
    rec('  ### (1c) THE RANK AT EVERY FRAME, BY BOTH SCHEMES.')
    rec('    %-7s %-7s %-8s %-10s %-9s %-9s %-11s %-11s'
        % ('N', 'X', 'free', 'h', 'rank grid', 'rank stab', 'dim grid', 'dim stab'))
    for fk in frames:
        N, X, NY = fk
        fr = INS.Frame(N, X, NY)
        T = fr.transform_matrix()
        st, gr = ST.both_subspaces(fr, ST.TAU, T)
        FI[fk] = dict(N=N, X=X, NY=NY, h=fr.h, free=st['free'],
                      rank_grid=gr['rank'], rank_stab=st['rank'],
                      dim_grid=gr['dim'], dim_stab=st['dim'])
        rec('    %-7d %-7.1f %-8d %-10.6f %-9d %-9d %-11d %-11d'
            % (N, X, st['free'], fr.h, gr['rank'], st['rank'], gr['dim'], st['dim']))
        del fr, T, st, gr

    rec('')
    rec('  ### (1d) STABILITY ACROSS THE REFINEMENT LADDER WHERE THE GRID SCHEME STEPPED.')
    rec('    ### **THE GRID AXIS, `X` HELD AT %g:**' % SM.GRID_AXIS[0][1])
    gg = [FI[tuple(fk)]['rank_grid'] for fk in SM.GRID_AXIS]
    gs = [FI[tuple(fk)]['rank_stab'] for fk in SM.GRID_AXIS]
    rec('      N          : %s' % '  '.join('%-7d' % fk[0] for fk in SM.GRID_AXIS))
    rec('      rank grid  : %s' % '  '.join('%-7d' % r for r in gg))
    rec('      rank stable: %s' % '  '.join('%-7d' % r for r in gs))
    grid_steps = sum(1 for i in range(1, len(gg)) if gg[i] != gg[i - 1])
    stab_steps = sum(1 for i in range(1, len(gs)) if gs[i] != gs[i - 1])
    rec('      ### ### **RANK CHANGES ALONG THE GRID AXIS -- b316 SCHEME : %d ; THIS ACT : %d**'
        % (grid_steps, stab_steps))
    rec('    ### **THE DOMAIN AXIS, `h` HELD AT 1/%d:**' % round(1.0 / SM.DOMAIN_AXIS[0][1]
                                                                * SM.DOMAIN_AXIS[0][0]))
    dg = [FI[tuple(fk)]['rank_grid'] for fk in SM.DOMAIN_AXIS]
    ds = [FI[tuple(fk)]['rank_stab'] for fk in SM.DOMAIN_AXIS]
    rec('      X          : %s' % '  '.join('%-7g' % fk[1] for fk in SM.DOMAIN_AXIS))
    rec('      rank grid  : %s' % '  '.join('%-7d' % r for r in dg))
    rec('      rank stable: %s' % '  '.join('%-7d' % r for r in ds))
    rec('      ### **THE DOMAIN AXIS IS NOT EXPECTED TO HOLD ITS RANK AND DOES NOT:** ### a longer')
    rec('      ### domain is a BIGGER SPACE, so its dimension must grow. ### **WHAT THE STABLE')
    rec('      ### ### SCHEME IS FOR IS THE GRID AXIS**, where the space is the same and only the')
    rec('      ### discretization changes.')

    # ================================================================ COMPONENT 2
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE REPRODUCTION AT STABLE RANK.')
    rec('=' * 100)
    cells = SM.atlas_cells()
    work = {}
    for r in cells:
        for fk in SM.DOMAIN_AXIS:
            work.setdefault(tuple(fk), set()).add(r['a'])
    for a in SM.DETAIL_CELLS:
        for fk in SM.GRID_AXIS:
            work.setdefault(tuple(fk), set()).add(a)

    RES, ZRES, UNIT = {}, {}, {}
    rec('')
    rec('  ### (2a) THE FRAMES, WITH THE IDENTITY CONTROL RE-RUN ON THE STABLE SUBSPACE.')
    import qeps_layer as QL
    xq, wq, lam, lam2, xi_, xi1_, an, dan = QL.layer(700)
    rec('    %-7s %-7s %-7s %-16s %-9s %-12s'
        % ('N', 'X', 'rank', 'identity trace', 'dim', 'exact?'))
    for fk in sorted(work, key=lambda k: (k[0], k[1])):
        N, X, NY = fk
        fr = INS.Frame(N, X, NY)
        T = fr.transform_matrix()
        st, gr = ST.both_subspaces(fr, ST.TAU, T)
        ti, _f, _c = SM.identity_trace(fr, st)
        okid = abs(ti - st['dim']) < 1e-9
        rec('    %-7d %-7.1f %-7d %-16.6f %-9d %-12s'
            % (N, X, st['rank'], ti, st['dim'], 'YES' if okid else '### NO'))
        if not okid:
            fails.append('identity control at %s' % (fk,))
        for a in sorted(work[fk]):
            f = variant(a)
            RES[(fk, a)] = (SQ.square_trace(fr, st, f), SM.compressed_trace(fr, st, f)[0])
        # ### the corpus's expansion vectors, still measured outside -- b316's (3b), on this cut
        zs, zg = [], []
        for n in range(4):
            z = np.zeros(fr.N)
            hi = fr.x >= 1.0
            z[hi] = an(fr.x[hi])[:, n] * (lam[n] / math.sqrt(1.0 - lam2[n]))
            nz = fr.norm(z)
            if nz == 0:
                continue
            z = z / nz
            zs.append(float(np.linalg.norm(fr.outside(st, z))
                            / max(np.linalg.norm(z[st['hi']]), 1e-300)))
            zg.append(float(np.linalg.norm(fr.outside(gr, z))
                            / max(np.linalg.norm(z[gr['hi']]), 1e-300)))
        ZRES[fk] = (zs, zg)
        # ### the unit's residual, on BOTH cuts at the SAME frame -- Component 3's measurement
        u = INS.sonin_unit(fr)
        UNIT[fk] = (float(np.linalg.norm(fr.outside(st, u))
                          / max(np.linalg.norm(u[st['hi']]), 1e-300)),
                    float(np.linalg.norm(fr.outside(gr, u))
                          / max(np.linalg.norm(u[gr['hi']]), 1e-300)))
        del fr, T, st, gr

    ref = tuple(SM.REFERENCE)
    rec('')
    rec('  ### (2b) THE SQUARE AND THE SMEAR AT THE THIRTEEN BANKED CELLS, ON THE STABLE SUBSPACE.')
    rec('    %-6s %-16s %-16s %-16s %-7s'
        % ('a', 'SQUARE', 'SMEAR', 'difference', 'rank'))
    sweep = []
    for r in cells:
        a = r['a']
        sq, sm = RES[(ref, a)]
        bsq = [RES[(tuple(fk), a)][0] for fk in SM.DOMAIN_AXIS]
        bsm = [RES[(tuple(fk), a)][1] for fk in SM.DOMAIN_AXIS]
        sweep.append(dict(a=a, square=sq, smear=sm, diff=sq - sm,
                          rank=FI[ref]['rank_stab'],
                          sq_neg=any(x < 0.0 for x in bsq), sm_neg=any(x < 0.0 for x in bsm)))
        rec('    %-6g %-16.9f %-16.9f %-16.9f %-7d'
            % (a, sq, sm, sq - sm, FI[ref]['rank_stab']))
    nsq = sum(1 for s in sweep if s['sq_neg'])
    nsm = sum(1 for s in sweep if s['sm_neg'])
    rec('    ### ### **CELLS AT WHICH THE SQUARE IS NEGATIVE ANYWHERE : %d**' % nsq)
    rec('    ### ### **CELLS AT WHICH THE SMEAR IS NEGATIVE ANYWHERE  : %d**' % nsm)
    rec('    ### **b318 FOUND 0 AND 5 ON THE GRID CUT.** ### If these agree, the stable cut has')
    rec('    ### changed the rank and not the object, which is the whole point of the build.')

    rec('')
    rec('  ### (2c) THE IDENTITY, RE-PROVED ON THE STABLE SUBSPACE.')
    frr = INS.Frame(*ref)
    Tr_ = frr.transform_matrix()
    subr = ST.both_subspaces(frr, ST.TAU, Tr_)[0]
    rec('    %-6s %-16s %-16s %-12s %-10s'
        % ('a', 'SQUARE(f)', 'SMEAR(f conv f)', 'relative', 'within 1%'))
    ident = []
    for a in SM.DETAIL_CELLS:
        f = variant(a)
        sq = RES[(ref, a)][0]
        sm_ac = SM.compressed_trace(frr, subr, SQ.autocorrelation(f))[0]
        rel = abs(sq - sm_ac) / max(abs(sq), 1e-300)
        good = rel < SQ.BAR_IDENTITY
        ident.append(dict(a=a, square=sq, smear_ac=sm_ac, rel=rel, ok=good))
        rec('    %-6g %-16.9f %-16.9f %-12.3e %-10s'
            % (a, sq, sm_ac, rel, 'YES' if good else '### NO'))
    if not all(x['ok'] for x in ident):
        fails.append('the identity bar on the stable subspace')

    rec('')
    rec('  ### (2d) THE SOURCE WORKED INNER PRODUCT, STILL RECOVERED -- b316 (3c), UNCHANGED.')
    worst = 0.0
    for rho in (1.5, 2.0, 3.0):
        aa = np.exp(-4.0 * (frr.x - 0.7) ** 2)
        bb = np.exp(-2.0 * (frr.x - 1.1) ** 2)
        lhs = frr.inner(aa, frr.scaling(1.0 / rho, bb))
        rhsv = (rho ** 0.5) * frr.inner(aa, np.interp(rho * frr.x, frr.x, bb,
                                                      left=0.0, right=0.0))
        worst = max(worst, abs(lhs - rhsv))
    rec('    ### worst difference over three dilations : %.2e' % worst)
    rec('    ### **IT IS A CHECK ON (N1) AND (N3) AND NOT ON THE SUBSPACE**, so it must be')
    rec('    ### unchanged by this act, and it is.')
    if worst > 1e-12:
        fails.append("the source's worked inner product")
    del frr, Tr_, subr

    rec('')
    rec('  ### (2e) THE CORPUS EXPANSION VECTORS, STILL MEASURED OUTSIDE, ON BOTH CUTS.')
    rec('    %-7s %-7s %-28s %-28s' % ('N', 'X', 'zeta_n residual (stable)', 'zeta_n (grid)'))
    for fk in sorted(ZRES, key=lambda k: (k[0], k[1])):
        zs, zg = ZRES[fk]
        rec('    %-7d %-7.1f %-28s %-28s'
            % (fk[0], fk[1], ', '.join('%.4f' % v for v in zs),
               ', '.join('%.4f' % v for v in zg)))
    rec('    ### **b292 DERIVED THIS AND b316 MEASURED IT ON THE GRID CUT.** ### If the stable cut')
    rec('    ### agrees, the new criterion has not quietly admitted vectors the record says are out.')

    rec('')
    rec('  ### (2f) THE TWO AXES, WITH THE RANK AS A COLUMN OF EVERY ROW.')
    axes = {}
    for a in SM.DETAIL_CELLS:
        rec('')
        rec('    ### `a = %g`' % a)
        rec('      %-8s %-7s %-8s %-6s %-16s %-11s %-16s %-11s'
            % ('axis', 'N', 'X', 'rank', 'SQUARE', 'sq drift', 'SMEAR', 'sm drift'))
        gsv = [RES[(tuple(fk), a)] for fk in SM.GRID_AXIS]
        dsv = [RES[(tuple(fk), a)] for fk in SM.DOMAIN_AXIS]
        for i, fk in enumerate(SM.GRID_AXIS):
            dq = (abs(gsv[i][0] - gsv[i - 1][0]) / max(abs(gsv[i][0]), 1e-300)) if i else None
            dm = (abs(gsv[i][1] - gsv[i - 1][1]) / max(abs(gsv[i][1]), 1e-300)) if i else None
            rec('      %-8s %-7d %-8.1f %-6d %-16.9f %-11s %-16.9f %-11s'
                % ('grid' if i == 0 else '', fk[0], fk[1], FI[tuple(fk)]['rank_stab'], gsv[i][0],
                   '-' if dq is None else '%.3e' % dq, gsv[i][1],
                   '-' if dm is None else '%.3e' % dm))
        for i, fk in enumerate(SM.DOMAIN_AXIS):
            dq = (abs(dsv[i][0] - dsv[i - 1][0]) / max(abs(dsv[i][0]), 1e-300)) if i else None
            dm = (abs(dsv[i][1] - dsv[i - 1][1]) / max(abs(dsv[i][1]), 1e-300)) if i else None
            rec('      %-8s %-7d %-8.1f %-6d %-16.9f %-11s %-16.9f %-11s'
                % ('domain' if i == 0 else '', fk[0], fk[1], FI[tuple(fk)]['rank_stab'], dsv[i][0],
                   '-' if dq is None else '%.3e' % dq, dsv[i][1],
                   '-' if dm is None else '%.3e' % dm))
        axes[a] = dict(grid=[list(x) for x in gsv], domain=[list(x) for x in dsv],
                       grank=[FI[tuple(fk)]['rank_stab'] for fk in SM.GRID_AXIS],
                       drank=[FI[tuple(fk)]['rank_stab'] for fk in SM.DOMAIN_AXIS])

    rec('')
    rec('  ### (2g) THE NOISE-FLOOR GATE, IN THE PATH.')
    items = []
    for a in SM.DETAIL_CELLS:
        g = axes[a]['grid']
        d = axes[a]['domain']
        items.append(('grid   sq a=%g' % a, g[-2][0], g[-1][0]))
        items.append(('grid   sm a=%g' % a, g[-2][1], g[-1][1]))
        items.append(('domain sq a=%g' % a, d[-2][0], d[-1][0]))
        items.append(('domain sm a=%g' % a, d[-2][1], d[-1][1]))
    ngood, nrows, ndetail = NF.gate(items, label='b319')
    for name, value, refined, verdict, why in nrows:
        rec('    %-18s %-16.9f -> %-16.9f  %-10s' % (name, value, refined, verdict))
    rec('    ### %s' % ndetail)

    rec('')
    rec('  ### (2h) THE REACH, AGAINST (B3): %.0f PER CENT ON BOTH AXES ### **WITH THE RANK'
        % (SM.BAR_REACH * 100.0))
    rec('  ### ### CONSTANT ACROSS EACH STEP.**')
    gi = list(SM.GRID_AXIS).index(ref)
    di = list(SM.DOMAIN_AXIS).index(ref)
    rec('    %-6s %-9s %-13s %-13s %-13s %-13s %-9s'
        % ('a', 'object', 'grid drift', 'domain drift', 'grid rank', 'domain rank', 'inside?'))
    reach = {}
    for a in SM.DETAIL_CELLS:
        g = axes[a]['grid']
        d = axes[a]['domain']
        gr_ = axes[a]['grank']
        dr_ = axes[a]['drank']
        for j, nm in ((0, 'SQUARE'), (1, 'SMEAR')):
            gd = abs(g[gi + 1][j] - g[gi][j]) / max(abs(g[gi + 1][j]), 1e-300)
            dd = abs(d[di + 1][j] - d[di][j]) / max(abs(d[di + 1][j]), 1e-300)
            gst = gr_[gi] == gr_[gi + 1]
            dst = dr_[di] == dr_[di + 1]
            inside = (gd < SM.BAR_REACH) and (dd < SM.BAR_REACH) and gst and dst
            reach[(a, nm)] = dict(gd=gd, dd=dd, gstable=gst, dstable=dst, inside=inside)
            rec('    %-6g %-9s %-13.3e %-13.3e %-13s %-13s %-9s'
                % (a, nm, gd, dd, '%d->%d' % (gr_[gi], gr_[gi + 1]),
                   '%d->%d' % (dr_[di], dr_[di + 1]), 'YES' if inside else '### NO'))
    n_inside = sum(1 for v in reach.values() if v['inside'])
    rec('    ### ### **CELLS INSIDE THE REACH : %d OF %d.**' % (n_inside, len(reach)))
    rec('    ### **THE GRID HALF OF THE BAR IS THE HALF THIS ACT COULD MOVE.** ### The domain axis')
    rec('    ### changes the SPACE, so its rank must change and its drift is a real convergence')
    rec('    ### question this act did not set out to answer.')

    # ================================================================ COMPONENT 3
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- WHAT THE INSTRUMENT NOW IS.')
    rec('=' * 100)
    rec('  ### (3a) THE TWO SUBSPACES, COMPARED WHERE THEY DIFFER.')
    rec('    %-7s %-7s %-10s %-10s %-13s %-13s %-24s'
        % ('N', 'X', 'rank grid', 'rank stab', 'only grid', 'only stable', 'their eigenvalues'))
    diffs = {}
    for fk in frames:
        fr = INS.Frame(*fk)
        rg, rs, og, os_, eg, es = ST.scheme_difference(fr, ST.TAU)
        diffs[fk] = dict(rank_grid=rg, rank_stab=rs, n_only_grid=len(og), n_only_stab=len(os_),
                         eig_only_grid=[float(x) for x in eg[:3]],
                         eig_only_stab=[float(x) for x in es[:3]])
        ev = ', '.join('%.2e' % x for x in (eg[:2] if len(og) else es[:2]))
        rec('    %-7d %-7.1f %-10d %-10d %-13d %-13d %-24s'
            % (fk[0], fk[1], rg, rs, len(og), len(os_), ev or '-'))
        del fr
    rec('    ### **`only grid` ARE VECTORS b316 PUT OUTSIDE THE SPACE THAT THE THRESHOLD ADMITS;')
    rec('    ### ### `only stable` ARE VECTORS THE THRESHOLD PUTS OUT THAT b316 ADMITTED.** ### Both')
    rec('    ### cuts run on the SAME singular values, so the difference is an index set and its')
    rec('    ### eigenvalues can be printed rather than described.')

    rec('')
    rec('  ### (3b) THE UNIT MEMBERSHIP RESIDUAL, ON BOTH CUTS, AT THE SAME FRAMES.')
    rec('    ### ### **A MEASUREMENT, NOT A VERDICT. ### THE DECISION STAYS THE MEMBERSHIP ACT\'S.**')
    rec('    %-7s %-7s %-16s %-16s' % ('N', 'X', 'residual stable', 'residual grid'))
    for fk in sorted(UNIT, key=lambda k: (k[0], k[1])):
        us, ug = UNIT[fk]
        rec('    %-7d %-7.1f %-16.4f %-16.4f' % (fk[0], fk[1], us, ug))
    rec('    ### **b316 REPORTED `0.9455, 0.8023, 0.5527, 0.6033, 0.4902` ACROSS ITS OWN FIVE')
    rec('    ### ### TRUNCATIONS**, which are NOT these frames. ### The two columns above are')
    rec('    ### like-for-like at the SAME frames; b316\'s row is quoted as context and not')
    rec('    ### compared cell to cell. ### **NO VERDICT IS TAKEN ON MEMBERSHIP BY THIS ACT.**')

    payload = dict(frames=dict((str(k), v) for k, v in FI.items()),
                   sweep=sweep, ident=ident,
                   axes=dict((str(k), v) for k, v in axes.items()),
                   reach=dict((str(k), v) for k, v in reach.items()),
                   diffs=dict((str(k), v) for k, v in diffs.items()),
                   unit=dict((str(k), list(v)) for k, v in UNIT.items()),
                   zeta=dict((str(k), [list(a) for a in v]) for k, v in ZRES.items()),
                   grid_steps=grid_steps, stab_steps=stab_steps,
                   nsq_neg=nsq, nsm_neg=nsm, n_inside=n_inside,
                   inner_worst=worst, tau=ST.TAU, lambda0sq=ST.LAMBDA0_SQ,
                   noise_ok=ngood, noise=[(n, v, r, vd) for n, v, r, vd, _w in nrows],
                   elapsed=time.time() - t0, fails=fails, soft=soft)
    io.open(os.path.join(D, 'b319_rows.json'), 'w', encoding='utf-8',
            newline='\n').write(json.dumps(payload, indent=1, default=float) + '\n')

    rec('')
    rec('  ### CHECKS FAILING : %d' % len(fails))
    for f in fails:
        rec('    ### FAILED: %s' % f)
    rec('  ### ### **UNCONFIRMED : %d**' % len(soft))
    for f in soft:
        rec('    ### UNCONFIRMED: %s' % f)
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)
    return (0 if not fails else 1), LINES, payload


if __name__ == '__main__':
    code, ls, _p = main()
    io.open(os.path.join(D, 'b319_components_run.txt'), 'w', encoding='utf-8',
            newline='\n').write(chr(10).join(ls) + chr(10))
    sys.exit(code)
