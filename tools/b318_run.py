# -*- coding: utf-8 -*-
"""b318_run.py -- THE COMPONENTS. ### **THE FORCED SIGN.**

### ### **b317 COMPUTED A NUMBER THAT CHANGED SIGN AND DID NOT KNOW WHAT THE SIGN CHANGE WAS.**
### This file tests the instrument against the one thing the source guarantees without any argument
### about truncations -- that its trace side, in its square form, is a Hilbert-Schmidt norm -- and
### decides the class of the mean-zero variant by the source's own Definition 3.1.

### ### **NO UNIT IS USED ANYWHERE IN THIS FILE.** ### `INS.sonin_unit` is never called.
### ### **AND `W_infinity` IS NOT COMPUTED IN ANY DIRECTION.** ### Both objects here are trace-side.
### ### **EVERY BAR AND EVERY FRAME IS IMPORTED** -- the frames from `b317_smear.py`, because the
### order says *same cells, same frames, same quadrature as b317*, and the bars from
### `b318_square.py`, which is where the sealed (5) lives.
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
import b318_square as SQ        # noqa: E402
import noise_floor as NF        # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EXTRACT = os.path.join(D, 'b318_extract_notes.txt')

# ### THE SOURCE STATEMENTS THIS ACT USES, ### **PULLED FROM THE EXTRACT FILE AND NOT FROM THE PDF.**
# ### The order says *needles from the extract file*: the read already happened, under its own pin,
# ### and re-opening the artefact here would be a second read nobody re-runs.
EXTRACT_NEEDLES = [
    ('the square form, in the source own voice', 'when evaluated on f'),
    ('### and that it is the trace of a positive operator', 'of a positive operator'),
    ('Definition 3.1 -- the class test', 'positive de'),
    ('### and that it is pointwise on the transform', 'is pointwise positive'),
    ('Theorem 1 -- the interval the source own g must live in', 'have support in the interval'),
    ('### and the two vanishing conditions it puts on g', 'vanishing at i'),
    ('the quadratic form Q_W and its vector space V', 'the positivity of the quadratic form'),
    ('the autocorrelation form, in the introduction', 'gpxyqgpyqdy'),
    ('### f-hat = |g-hat|^2, the link Boas-Kac supplies', 'shows that f is positive'),
    ('### the source own counterexample: (54) holds and W_infinity is negative', 'but for which'),
    ('the eigenvalue-one characterization of S(1,1)', 'is the eigenspace of'),
    ('(53) and its support condition', 'whose support is in the interval'),
    ('(61) the scaling action', 'its action is given by'),
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


BPC = {}


def bump(a):
    if a not in BPC:
        BPC[a] = SM.corpus_bump(a)
    return BPC[a]


def main():
    t0 = time.time()
    fails, soft = [], []
    rec('=' * 100)
    rec('b318 -- THE FORCED SIGN.')
    rec('=' * 100)

    igood, iarms = INS.self_test()
    rec('  ### b316 INSTRUMENT FIXTURES : %s  %s' % (iarms, 'PASS' if igood else '### FAIL ###'))
    sgood, sarms, _sl = SM.self_test()
    rec('  ### b317 ASSEMBLY FIXTURES   : %s  %s' % (sarms, 'PASS' if sgood else '### FAIL ###'))
    qgood, qarms, qlines = SQ.self_test()
    rec('  ### THIS ACT SQUARE FIXTURES : %s  %s' % (qarms, 'PASS' if qgood else '### FAIL ###'))
    for s in qlines:
        rec('    ' + s)
    rec('  ### **ARMS (i) AND (ii) ARE THE CLASS TEST BOTH WAYS**: it says YES on a genuine square')
    rec('  ### and NO on a function known not to be one by an argument about widths, not by a')
    rec('  ### measurement. ### **ARMS (vi) AND (vii) ARE THE IDENTITY BOTH WAYS**: the square')
    rec('  ### equals the smear at the AUTOCORRELATION and differs from the smear at the WINDOW.')
    rec('  ### **THE FIXTURES RUN AT `a = %g`, WHICH IS NOT ONE OF THE ATLAS CELLS.**' % SQ.FIXTURE_A)
    if not (igood and sgood and qgood):
        fails.append('a fixture suite did not pass')
        return 2, LINES, {}

    # ================================================================ COMPONENT 1
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE CLASS OF THE VARIANT, READ OFF DIRECTLY.')
    rec('=' * 100)
    rec('  ### ### **THE SOURCE STATEMENTS, PULLED FROM THE EXTRACT FILE.** ### The read happened')
    rec('  ### under its own pin at the extract step; ### **RE-OPENING THE ARTEFACT HERE WOULD BE A')
    rec('  ### ### SECOND READ NOBODY RE-RUNS.**')
    ext = io.open(EXTRACT, encoding='utf-8').read()
    for lbl, anchor in EXTRACT_NEEDLES:
        hit = anchor in ext
        rec('    %-6s %s' % ('found' if hit else '### NONE', lbl))
        if not hit:
            fails.append('extract needle: %s' % lbl)
    rec('')
    rec('  ### ### **WHAT THE SOURCE REQUIRES, AND OF WHICH LETTER.** ### This is the whole of')
    rec('  ### Component 1 and it turns on a distinction the corpus has not been making:')
    rec('    ### **eq. (53)** puts `supp f` inside `[1/2, 2]` and defines `W_infinity` there;')
    rec('    ### **eq. (54)** puts `INT f(rho) rho^{+-1/2} d*rho = 0`;')
    rec('    ### **DEFINITION 3.1** says `f` is POSITIVE DEFINITE when `f-hat(t) >= 0` pointwise;')
    rec('    ### ### **THEOREM 1 PUTS ITS CONDITIONS ON `g`, NOT ON `f`**: ### *"Let g have support')
    rec('    ### ### in the interval [2^-1/2, 2^1/2] and Fourier transform vanishing at i/2 and 0"*,')
    rec('    ### and the object it then bounds is `W_infinity(g conv g^) >= Tr(theta(g) S theta(g)^)`.')

    rec('')
    rec('  ### (1a) THE VARIANT AT EVERY CELL, AGAINST ALL FOUR CONDITIONS.')
    rec('    %-6s %-13s %-13s %-9s %-9s %-13s %-11s %-9s'
        % ('a', 'f-hat(0)', 'eq.(54)', 'supp<=2', 'supp<=r2', 'min f-hat', 't at min', 'pos.def.'))
    cells = SM.atlas_cells()
    c1 = []
    for r in cells:
        a = r['a']
        f = variant(a)
        m54 = f.vanishing_54()[0]
        mn, tm, h0, pd = SQ.positive_definite(f)
        okf = f.support <= SQ.SUPPORT_F_HI
        okg = f.support <= SQ.SUPPORT_G_HI
        c1.append(dict(a=a, h0=h0, m54=m54, supp_f=okf, supp_g=okg, minf=mn, tmin=tm, pd=pd))
        rec('    %-6g %-13.3e %-13.3e %-9s %-9s %-13.4e %-11.3f %-9s'
            % (a, h0, m54, 'YES' if okf else 'no', 'YES' if okg else 'no', mn, tm,
               'YES' if pd else '### NO'))
    rec('')
    rec('  ### (1b) THE CORPUS INTEGRAL-ONE BUMP AT EVERY CELL, THE SAME FOUR CONDITIONS.')
    rec('    %-6s %-13s %-13s %-9s %-9s %-13s %-11s %-9s'
        % ('a', 'f-hat(0)', 'eq.(54)', 'supp<=2', 'supp<=r2', 'min f-hat', 't at min', 'pos.def.'))
    c1b = []
    for r in cells:
        a = r['a']
        f = bump(a)
        m54 = f.vanishing_54()[0]
        mn, tm, h0, pd = SQ.positive_definite(f)
        okf = f.support <= SQ.SUPPORT_F_HI
        okg = f.support <= SQ.SUPPORT_G_HI
        c1b.append(dict(a=a, h0=h0, m54=m54, supp_f=okf, supp_g=okg, minf=mn, tmin=tm, pd=pd))
        rec('    %-6g %-13.3e %-13.3e %-9s %-9s %-13.4e %-11.3f %-9s'
            % (a, h0, m54, 'YES' if okf else 'no', 'YES' if okg else 'no', mn, tm,
               'YES' if pd else '### NO'))

    n_pd = sum(1 for x in c1 if x['pd'])
    n_54 = sum(1 for x in c1 if abs(x['m54']) < 1e-9)
    n_h0 = sum(1 for x in c1 if abs(x['h0']) < 1e-9)
    n_sf = sum(1 for x in c1 if x['supp_f'])
    n_sg = sum(1 for x in c1 if x['supp_g'])
    rec('')
    rec('  ### (1c) VERDICTS PER CONDITION, FOR THE VARIANT, OVER %d CELLS:' % len(c1))
    rec('    ### transform vanishing at 0 (Theorem 1 first condition)   : %d / %d'
        % (n_h0, len(c1)))
    rec('    ### eq. (54), transform vanishing at +-i/2 (Theorem 1 second) : %d / %d'
        % (n_54, len(c1)))
    rec('    ### support inside eq. (53) window [1/2, 2]                : %d / %d'
        % (n_sf, len(c1)))
    rec('    ### support inside Theorem 1 g-window [2^-1/2, 2^1/2]      : %d / %d'
        % (n_sg, len(c1)))
    rec('    ### ### **POSITIVE DEFINITE IN DEFINITION 3.1 SENSE        : %d / %d**'
        % (n_pd, len(c1)))
    rec('    ### the scan runs `t` in `[0, %g/L]` at %d points, `L` the cell own half-width.'
        % (SQ.PD_TMAX_OVER_L, SQ.PD_NT))
    rec('    ### **A NEGATIVE VALUE PROVES THE FUNCTION IS NOT POSITIVE DEFINITE; A NONNEGATIVE SCAN')
    rec('    ### ### DOES NOT PROVE THAT IT IS**, beyond the interval scanned. ### (B1) says so.')

    # ================================================================ COMPONENT 2
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE SQUARE, COMPUTED.')
    rec('=' * 100)

    work = {}

    def need(fk, a):
        work.setdefault(tuple(fk), set()).add(a)

    for r in cells:
        for fk in SM.DOMAIN_AXIS:
            need(fk, r['a'])
    for a in SM.DETAIL_CELLS:
        for fk in SM.GRID_AXIS:
            need(fk, a)

    RES, FI = {}, {}
    rec('')
    rec('  ### (2a) THE FRAMES, BUILT ONCE EACH, WITH THE RANK PRINTED AS ITS OWN COLUMN.')
    rec('    %-7s %-7s %-6s %-10s %-8s %-7s %-8s %-9s'
        % ('N', 'X', 'NY', 'h', 'free', 'rank', 'dim', 'NY/X'))
    for fk in sorted(work, key=lambda k: (k[0], k[1])):
        N, X, NY = fk
        fr = INS.Frame(N, X, NY)
        sub = fr.subspace()
        FI[fk] = dict(N=N, X=X, NY=NY, h=fr.h, free=sub['free'], rank=sub['rank'],
                      dim=sub['dim'], ny_over_x=float(NY) / X)
        rec('    %-7d %-7.1f %-6d %-10.6f %-8d %-7d %-8d %-9.2f'
            % (N, X, NY, fr.h, sub['free'], sub['rank'], sub['dim'], float(NY) / X))
        ti, _f, _c = SM.identity_trace(fr, sub)
        if abs(ti - sub['dim']) > 1e-9:
            fails.append('identity control at %s' % (fk,))
        for a in sorted(work[fk]):
            f = variant(a)
            RES[(fk, a)] = (SQ.square_trace(fr, sub, f), SM.compressed_trace(fr, sub, f)[0])
        del fr, sub
    rec('    ### **THE IDENTITY CONTROL WAS RE-RUN AT EVERY FRAME** and returned the dimension.')

    rec('')
    rec('  ### (2b) THE ARITHMETIC NONNEGATIVITY, AT A FRAME SMALL ENOUGH TO DECIDE EXACTLY.')
    frs = INS.Frame(256, 8.0, 64)
    subs = frs.subspace()
    fv = variant(SM.DETAIL_CELLS[0])
    sq_small = SQ.square_trace(frs, subs, fv)
    rec('    ### `theta(f) S` has matrix `A[:,H] P`. ### `|| . ||_F^2` is the sum of the squares of')
    rec('    ### that matrix entries, and ### **`square_trace` PERFORMS NO SUBTRACTION ANYWHERE**.')
    rec('    ### N=%d, X=%g, NY=%d, rank=%d : ### **square = %.12f ; nonnegative : %s**'
        % (frs.N, frs.X, frs.NY, subs['rank'], sq_small, sq_small >= 0.0))
    rec('    ### ### **THIS IS THE ONE FINITE-DECIDABLE STATEMENT IN THE ACT, AND ITS SCOPE IS')
    rec('    ### ### EXACTLY THIS:** ### every summand is a square of a machine float, hence')
    rec('    ### nonnegative, and a running sum of nonnegatives cannot go below zero. ### **WHAT IS')
    rec('    ### ### NOT DECIDABLE IS THAT THIS SUM IS THE OPERATOR-THEORETIC NORM** -- that rests')
    rec('    ### on the quadrature, the numerical rank and the truncation.')
    if sq_small < 0.0:
        fails.append('the arithmetic nonnegativity control')
    x0, npts = SQ.first_contributing_row(frs, fv)
    rec('    ### and the rows the square reaches: the smallest contributing `x` is %.5f, whose'
        % x0)
    rec('    ### `u`-window holds ### **%.2f point(s)** ### -- so b317 first-node defect, which sat'
        % npts)
    rec('    ### at `x = h/2` with less than one point, ### **IS NOT REACHED BY THIS OBJECT EITHER.**')
    if npts <= 1.0:
        fails.append('the square reaches an under-resolved row')

    rec('')
    rec('  ### (2c) THE IDENTITY THAT NAMES THE DIFFERENCE, CHECKED BY TWO CODE PATHS.')
    rec('    ### `theta(f)^ theta(f) = theta(f^ conv f)`, so ### **`SQUARE(f) = SMEAR(f^ conv f)`**.')
    ref = tuple(SM.REFERENCE)
    frr = INS.Frame(*ref)
    subr = frr.subspace()
    rec('    %-6s %-16s %-16s %-12s %-10s'
        % ('a', 'SQUARE(f)', 'SMEAR(f conv f)', 'relative', 'within 1%'))
    ident = []
    for a in SM.DETAIL_CELLS:
        f = variant(a)
        sq = RES[(ref, a)][0]
        ac = SQ.autocorrelation(f)
        sm_ac = SM.compressed_trace(frr, subr, ac)[0]
        rel = abs(sq - sm_ac) / max(abs(sq), 1e-300)
        good = rel < SQ.BAR_IDENTITY
        ident.append(dict(a=a, square=sq, smear_ac=sm_ac, rel=rel, ok=good))
        rec('    %-6g %-16.9f %-16.9f %-12.3e %-10s'
            % (a, sq, sm_ac, rel, 'YES' if good else '### NO'))
    rec('    ### ### **THE TWO ARE THE SAME OBJECT.** ### The source square form is the corpus')
    rec('    ### smear evaluated at the AUTOCORRELATION of the window, not at the window.')
    rec('    ### **AND THAT IS THE FIRST DIFFERING CONSTITUENT, LOCATED RATHER THAN ASSERTED.**')
    if not all(x['ok'] for x in ident):
        soft.append('the identity bar (B2) was not met at every detail cell')
    del frr, subr

    rec('')
    rec('  ### (2d) PER CELL AT THE REFERENCE FRAME `N=%d, X=%g`, WITH THE RANK BESIDE IT.'
        % (ref[0], ref[1]))
    rec('    %-6s %-16s %-16s %-16s %-7s %-9s'
        % ('a', 'SQUARE', 'SMEAR', 'difference', 'rank', 'smear<0'))
    sweep = []
    for r in cells:
        a = r['a']
        sq, sm = RES[(ref, a)]
        band_sq = [RES[(tuple(fk), a)][0] for fk in SM.DOMAIN_AXIS]
        band_sm = [RES[(tuple(fk), a)][1] for fk in SM.DOMAIN_AXIS]
        sweep.append(dict(a=a, square=sq, smear=sm, diff=sq - sm, rank=FI[ref]['rank'],
                          band_sq_lo=min(band_sq), band_sq_hi=max(band_sq),
                          band_sm_lo=min(band_sm), band_sm_hi=max(band_sm),
                          sq_neg_any=any(x < 0.0 for x in band_sq),
                          sm_neg_any=any(x < 0.0 for x in band_sm)))
        rec('    %-6g %-16.9f %-16.9f %-16.9f %-7d %-9s'
            % (a, sq, sm, sq - sm, FI[ref]['rank'], 'YES' if sm < 0.0 else 'no'))
    nsq_neg = sum(1 for s in sweep if s['sq_neg_any'])
    nsm_neg = sum(1 for s in sweep if s['sm_neg_any'])
    rec('    ### ### **OVER THE WHOLE DOMAIN SWEEP AND ALL %d CELLS:**' % len(sweep))
    rec('    ### ### **CELLS AT WHICH THE SQUARE IS NEGATIVE ANYWHERE : %d**' % nsq_neg)
    rec('    ### ### **CELLS AT WHICH THE SMEAR IS NEGATIVE ANYWHERE  : %d**' % nsm_neg)

    rec('')
    rec('  ### (2e) THE TWO AXES, WITH THE RANK AS A COLUMN OF EVERY ROW.')
    axes = {}
    for a in SM.DETAIL_CELLS:
        rec('')
        rec('    ### `a = %g`, the mean-zero variant' % a)
        rec('      %-8s %-7s %-8s %-6s %-16s %-11s %-16s %-11s'
            % ('axis', 'N', 'X', 'rank', 'SQUARE', 'sq drift', 'SMEAR', 'sm drift'))
        gs = [RES[(tuple(fk), a)] for fk in SM.GRID_AXIS]
        ds = [RES[(tuple(fk), a)] for fk in SM.DOMAIN_AXIS]
        for i, fk in enumerate(SM.GRID_AXIS):
            dq = (abs(gs[i][0] - gs[i - 1][0]) / max(abs(gs[i][0]), 1e-300)) if i else None
            dm = (abs(gs[i][1] - gs[i - 1][1]) / max(abs(gs[i][1]), 1e-300)) if i else None
            rec('      %-8s %-7d %-8.1f %-6d %-16.9f %-11s %-16.9f %-11s'
                % ('grid' if i == 0 else '', fk[0], fk[1], FI[tuple(fk)]['rank'], gs[i][0],
                   '-' if dq is None else '%.3e' % dq, gs[i][1],
                   '-' if dm is None else '%.3e' % dm))
        for i, fk in enumerate(SM.DOMAIN_AXIS):
            dq = (abs(ds[i][0] - ds[i - 1][0]) / max(abs(ds[i][0]), 1e-300)) if i else None
            dm = (abs(ds[i][1] - ds[i - 1][1]) / max(abs(ds[i][1]), 1e-300)) if i else None
            rec('      %-8s %-7d %-8.1f %-6d %-16.9f %-11s %-16.9f %-11s'
                % ('domain' if i == 0 else '', fk[0], fk[1], FI[tuple(fk)]['rank'], ds[i][0],
                   '-' if dq is None else '%.3e' % dq, ds[i][1],
                   '-' if dm is None else '%.3e' % dm))
        axes[a] = dict(grid=[list(x) for x in gs], domain=[list(x) for x in ds],
                       grank=[FI[tuple(fk)]['rank'] for fk in SM.GRID_AXIS],
                       drank=[FI[tuple(fk)]['rank'] for fk in SM.DOMAIN_AXIS])

    rec('')
    rec('  ### (2f) THE NOISE-FLOOR GATE, IN THE PATH.')
    items = []
    for a in SM.DETAIL_CELLS:
        g = axes[a]['grid']
        d = axes[a]['domain']
        items.append(('grid   sq a=%g' % a, g[-2][0], g[-1][0]))
        items.append(('domain sq a=%g' % a, d[-2][0], d[-1][0]))
        items.append(('grid   sm a=%g' % a, g[-2][1], g[-1][1]))
        items.append(('domain sm a=%g' % a, d[-2][1], d[-1][1]))
    ngood, nrows, ndetail = NF.gate(items, label='b318')
    for name, value, refined, verdict, why in nrows:
        rec('    %-18s %-16.9f -> %-16.9f  %-10s' % (name, value, refined, verdict))
    rec('    ### %s' % ndetail)

    # ================================================================ COMPONENT 3
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE DECISION.')
    rec('=' * 100)
    sq_ever_neg = nsq_neg > 0
    sm_ever_neg = nsm_neg > 0
    form_fails = (n_pd == 0)
    rec('  ### THE THREE BRANCHES THE ORDER PROVIDES, AND WHICH ONE THE NUMBERS SELECT:')
    rec('    ### **(i) the square is nonnegative everywhere and the smear is not** : %s'
        % ((not sq_ever_neg) and sm_ever_neg))
    rec('    ### **(ii) the square itself goes negative**                          : %s'
        % sq_ever_neg)
    rec('    ### **(iii) the variant fails the form condition**                    : %s'
        % form_fails)
    payload = dict(class_variant=c1, class_bump=c1b, sweep=sweep, ident=ident,
                   axes=dict((str(k), v) for k, v in axes.items()),
                   frames=dict((str(k), v) for k, v in FI.items()),
                   noise_ok=ngood, noise=[(n, v, r, vd) for n, v, r, vd, _w in nrows],
                   sq_small=sq_small, first_row=[x0, npts],
                   n_pd=n_pd, n_54=n_54, n_h0=n_h0, n_sf=n_sf, n_sg=n_sg,
                   nsq_neg=nsq_neg, nsm_neg=nsm_neg,
                   bar_identity=SQ.BAR_IDENTITY, bar_reach=SM.BAR_REACH,
                   elapsed=time.time() - t0, fails=fails, soft=soft)
    io.open(os.path.join(D, 'b318_rows.json'), 'w', encoding='utf-8',
            newline='\n').write(json.dumps(payload, indent=1, default=float) + '\n')

    # ================================================================ COMPONENT 4
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 4 -- THE REACH, HONESTLY.')
    rec('=' * 100)
    rec('  ### (B3): a cell is inside the reach when the value moves by less than %.0f per cent'
        % (SM.BAR_REACH * 100.0))
    rec('  ### under BOTH refinements ### **AND THE MEASURED RANK IS IDENTICAL AT BOTH FRAMES OF')
    rec('  ### ### EACH STEP.** ### b317 found its grid drift dominated by a rank step and could')
    rec('  ### not separate the two effects; here rank stability is a CONDITION of the reach.')
    gi = list(SM.GRID_AXIS).index(ref)
    di = list(SM.DOMAIN_AXIS).index(ref)
    rec('    %-6s %-9s %-13s %-13s %-13s %-13s %-9s'
        % ('a', 'object', 'grid drift', 'domain drift', 'grid rank', 'domain rank', 'inside?'))
    reach = {}
    for a in SM.DETAIL_CELLS:
        g = axes[a]['grid']
        d = axes[a]['domain']
        gr = axes[a]['grank']
        dr = axes[a]['drank']
        for j, nm in ((0, 'SQUARE'), (1, 'SMEAR')):
            gd = abs(g[gi + 1][j] - g[gi][j]) / max(abs(g[gi + 1][j]), 1e-300)
            dd = abs(d[di + 1][j] - d[di][j]) / max(abs(d[di + 1][j]), 1e-300)
            gstable = gr[gi] == gr[gi + 1]
            dstable = dr[di] == dr[di + 1]
            inside = (gd < SM.BAR_REACH) and (dd < SM.BAR_REACH) and gstable and dstable
            reach[(a, nm)] = dict(gd=gd, dd=dd, gstable=gstable, dstable=dstable, inside=inside)
            rec('    %-6g %-9s %-13.3e %-13.3e %-13s %-13s %-9s'
                % (a, nm, gd, dd, '%d->%d' % (gr[gi], gr[gi + 1]),
                   '%d->%d' % (dr[di], dr[di + 1]), 'YES' if inside else '### NO'))
    n_inside = sum(1 for v in reach.values() if v['inside'])
    rec('    ### ### **CELLS INSIDE THE REACH : %d OF %d.**' % (n_inside, len(reach)))
    payload['reach'] = dict((str(k), v) for k, v in reach.items())
    payload['n_inside'] = n_inside
    io.open(os.path.join(D, 'b318_rows.json'), 'w', encoding='utf-8',
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
    io.open(os.path.join(D, 'b318_components_run.txt'), 'w', encoding='utf-8',
            newline='\n').write(chr(10).join(ls) + chr(10))
    sys.exit(code)
