# -*- coding: utf-8 -*-
"""b320_run.py -- THE COMPONENTS. ### **THE LAWFUL FUNCTION AND THE CONTROL.**

### ### **THE ACT MAY NOT WIDEN, TUNE OR RE-BAR ANYTHING TO MAKE THE CONTROL PASS.** ### Every bar
### is imported from a tool that carries the sealed value; a failure names the link at (B6)'s order.

### ### **NO UNIT IS USED. ### NO WINDOW IS OPENED.** ### The uncovered cells are computed and
### REPORTED AS DATA.
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
import b320_weil as WE          # noqa: E402
import noise_floor as NF        # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EXTRACT = os.path.join(D, 'b320_extract_notes.txt')

EXTRACT_NEEDLES = [
    ('Theorem 1 -- the three conditions on g', 'have support in the interval'),
    ('### and the inequality it asserts', 'Then one has'),
    ('Definition 3.1 -- positive definite', 'is pointwise positive'),
    ('the involution of the convolution algebra', 'which replaces the involution'),
    ('(53) -- W_infinity', 'weinvestigatethefunctional'.replace('weinvestigatethefunctional',
                                                                'we investigate the functional')),
    ('(38) -- the principal value', 'With this de'),
    ('### (39) -- the kernel tau', 'gives the Weil distribution'),
    ('the square form, in the source own voice', 'when evaluated on'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


SEED, AUTO = {}, {}


def seed(a):
    if a not in SEED:
        SEED[a] = SM.mean_zero_variant(a)
    return SEED[a]


def auto(a):
    if a not in AUTO:
        AUTO[a] = SQ.autocorrelation(seed(a))
    return AUTO[a]


def main():
    t0 = time.time()
    fails, soft = [], []
    rec('=' * 100)
    rec('b320 -- THE LAWFUL FUNCTION AND THE CONTROL.')
    rec('=' * 100)
    for nm, fn in (('b316 INSTRUMENT', INS.self_test), ('b317 ASSEMBLY', SM.self_test),
                   ('b318 SQUARE', SQ.self_test), ('b319 STABLE', ST.self_test),
                   ('THIS ACT WEIL', WE.self_test)):
        r = fn()
        good, arms = r[0], r[1]
        rec('  ### %-18s FIXTURES : %s  %s' % (nm, arms, 'PASS' if good else '### FAIL ###'))
        if not good:
            fails.append('%s fixtures' % nm)
    if fails:
        return 2, LINES, {}
    _g, _a, wl = WE.self_test()
    for s in wl:
        rec('    ' + s)
    rec('  ### **THE PRINCIPAL VALUE\'S CONSTANT IS MEASURED FROM (38), NOT REMEMBERED:**')
    rec('  ### **C_R = %.12f** at split radius R = %g, from two Gaussian widths agreeing to %.1e.'
        % (WE.C_R, WE.RSPLIT, WE.C_SPREAD))
    rec('  ### ### **AND IT LANDS ON `gamma + log(2 pi)` = %.12f, WHICH THIS ACT DID NOT PUT IN.**'
        % (0.5772156649015329 + math.log(2.0 * math.pi)))
    rec('  ### That agreement is CORROBORATION and not the definition: the definition is (38).')

    # ================================================================ COMPONENT 1
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE SQUARE OF THE SEED.')
    rec('=' * 100)
    ext = io.open(EXTRACT, encoding='utf-8').read()
    rec('  ### THE SOURCE STATEMENTS, PULLED FROM THE EXTRACT FILE:')
    for lbl, anchor in EXTRACT_NEEDLES:
        hit = anchor in ext
        rec('    %-6s %s' % ('found' if hit else '### NONE', lbl))
        if not hit:
            fails.append('extract needle: %s' % lbl)

    rec('')
    rec('  ### (1a) THE ADJOINT, WRITTEN ONCE FROM THE SOURCE\'S DEFINITION.')
    rec('    ### The source replaces `f -> f-bar^#` by ### **THE INVOLUTION OF THE CONVOLUTION')
    rec('    ### ### C*-ALGEBRA**, which on `R*_+` with the multiplicative measure `d*rho` is')
    rec('    ###   ### **`g^#(rho) = conj( g(rho^{-1}) )`**,')
    rec('    ### so that ### **`(g conv g^#)(lambda) = INT g(mu) g^#(mu^{-1} lambda) d*mu`**. ### In')
    rec('    ### the source\'s own variable `v = log rho` the measure is `dv` and, for a REAL seed')
    rec('    ### EVEN in `v`, `g^# = g` and the product is the AUTOCORRELATION')
    rec('    ###   ### **`f(v) = INT g(u) g(u - v) du`**, whose transform is `|g-hat|^2`.')
    rec('    ### **THE MEASURE FACTOR IS THE WHOLE OF WHAT MAKES THIS THE SOURCE\'S PRODUCT**: it is')
    rec('    ### `d*mu` and not `dmu`, which is why the convolution is additive in `v` and not in')
    rec('    ### `rho`, and b318 formed it that way.')

    rec('')
    rec('  ### (1b) DEFINITION 3.1 ON `f = g conv g^#`, AT EVERY CELL, WITH A FAILING ARM BESIDE IT.')
    cells = SM.atlas_cells()
    rec('    %-6s %-15s %-15s %-11s %-9s'
        % ('a', 'min f-hat', 'max f-hat', 'floor', 'pos.def.'))
    c1 = []
    for r in cells:
        a = r['a']
        f = auto(a)
        mn, tm, h0, pd = SQ.positive_definite(f)
        mx = float(np.max(SQ.fhat(f, np.linspace(0.0, 1.0, 3))))
        okpd = mn >= -WE.PD_FLOOR * max(abs(mx), 1.0)
        c1.append(dict(a=a, minf=mn, maxf=mx, pd=okpd))
        rec('    %-6g %-15.4e %-15.4e %-11.1e %-9s'
            % (a, mn, mx, -WE.PD_FLOOR * max(abs(mx), 1.0), 'YES' if okpd else '### NO'))
    npd = sum(1 for x in c1 if x['pd'])
    rec('    ### ### **POSITIVE DEFINITE IN DEFINITION 3.1\'s SENSE : %d OF %d.**' % (npd, len(c1)))
    rec('    ### **AND THE TEST CAN FAIL**: b318\'s fixture (ii) runs a wide bump minus a narrow one')
    rec('    ### -- a function known NOT to be a square by an argument about widths -- and the same')
    rec('    ### scan returns `min f-hat = -5.85e-01`. ### **A CLASS TEST EVERYTHING PASSES IS NOT')
    rec('    ### ### ONE**, and this one is the same code path that rejects that function.')

    rec('')
    rec('  ### (1c) THEOREM 1\'s THREE CONDITIONS ON THE SEED `g`, PER CELL.')
    rec('    %-6s %-13s %-13s %-13s %-11s'
        % ('a', 'supp <= 2^1/2', 'g-hat(0)', 'g-hat(i/2)', 'COVERED'))
    covered = []
    c1b = []
    for r in cells:
        a = r['a']
        g = seed(a)
        s_ok = g.support <= SQ.SUPPORT_G_HI
        h0 = g.at_zero()
        m54 = g.vanishing_54()[0]
        z_ok = abs(h0) <= WE.THM1_TOL
        h_ok = abs(m54) <= WE.THM1_TOL
        cov = bool(s_ok and z_ok and h_ok)
        if cov:
            covered.append(a)
        c1b.append(dict(a=a, supp=s_ok, h0=h0, m54=m54, covered=cov))
        rec('    %-6g %-13s %-13.3e %-13.3e %-11s'
            % (a, 'YES' if s_ok else 'no', h0, m54, 'YES' if cov else 'no'))
    rec('    ### ### **THE COVERED CELLS, NAMED FROM THE CHECK : %s**'
        % (', '.join('%g' % a for a in covered) if covered else 'NONE'))
    rec('    ### The support interval is the source\'s own `[2^-1/2, 2^1/2]`, i.e. `a <= %.9f`.'
        % SQ.SUPPORT_G_HI)
    rec('    ### **THE TWO VANISHING CONDITIONS ARE TESTED AT `%.0e` ABSOLUTE**, the sealed (B2)'
        % WE.THM1_TOL)
    rec('    ### floor, because they are quadratures and a strict equality would bar rounding.')

    # ================================================================ COMPONENT 2
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE TWO SIDES.')
    rec('=' * 100)
    work = {}
    for r in cells:
        for fk in SM.DOMAIN_AXIS:
            work.setdefault(tuple(fk), set()).add(r['a'])
    for a in covered:
        for fk in tuple(SM.GRID_AXIS) + tuple(SM.DOMAIN_AXIS):
            work.setdefault(tuple(fk), set()).add(a)

    RES, FI = {}, {}
    rec('')
    rec('  ### (2a) THE FRAMES, ON b319\'s STABLE CUT, WITH THE RANK PRINTED.')
    rec('    %-7s %-7s %-8s %-7s %-9s' % ('N', 'X', 'free', 'rank', 'dim'))
    for fk in sorted(work, key=lambda k: (k[0], k[1])):
        fr = INS.Frame(*fk)
        st, _gr = ST.both_subspaces(fr, ST.TAU)
        FI[fk] = dict(N=fk[0], X=fk[1], free=st['free'], rank=st['rank'], dim=st['dim'])
        rec('    %-7d %-7.1f %-8d %-7d %-9d' % (fk[0], fk[1], st['free'], st['rank'], st['dim']))
        ti, _f, _c = SM.identity_trace(fr, st)
        if abs(ti - st['dim']) > 1e-9:
            fails.append('identity control at %s' % (fk,))
        for a in sorted(work[fk]):
            RES[(fk, a)] = SQ.square_trace(fr, st, seed(a))
        del fr, st

    rec('')
    rec('  ### (2b) THE TWO SIDES AT EVERY CELL. ### **REFERENCE FRAME `N=%d, X=%g`, RANK %d.**'
        % (SM.REFERENCE[0], SM.REFERENCE[1], FI[tuple(SM.REFERENCE)]['rank']))
    rec('    ### LEFT  : `W_infinity(g conv g^#)` from (53) and (38).')
    rec('    ### RIGHT : `Tr(theta(g) S theta(g)^)`, the square on the stable cut.')
    rec('    %-6s %-9s %-16s %-16s %-16s %-9s'
        % ('a', 'covered', 'W_inf (LEFT)', 'SQUARE (RIGHT)', 'margin L-R', 'L >= R'))
    ref = tuple(SM.REFERENCE)
    rows = []
    for r in cells:
        a = r['a']
        wv, wreg, wsing, wp0 = WE.weil(auto(a))
        sq = RES[(ref, a)]
        cov = a in covered
        rows.append(dict(a=a, weil=wv, wreg=wreg, wsing=wsing, square=sq,
                         margin=wv - sq, holds=bool(wv >= sq), covered=cov,
                         prime=r['prime'], arch=r['arch'], zero=r['zero'], pole=r['pole']))
        rec('    %-6g %-9s %-16.9f %-16.9f %-16.9f %-9s'
            % (a, 'YES' if cov else 'no', wv, sq, wv - sq, 'YES' if wv >= sq else '### NO'))

    rec('')
    rec('  ### (2c) THE CORPUS\'S DIGAMMA INTEGRAL, AS CORROBORATION ONLY.')
    rec('    ### ### **IT IS NOT THE SOURCE\'S `W_infinity` AND IS NOT READ AS IT.** ### The corpus')
    rec('    ### forms `A = INT h-hat(u) [Re psi(1/4 + iu/2) - log pi] du / (2 pi)` in its own')
    rec('    ### emitting file, against its own bump -- a DIFFERENT test function from the seed\'s')
    rec('    ### autocorrelation -- and through the sign chain b316 quoted:')
    rec('    ###   ### **(L1)** the source\'s own `W_R = -W_inf`;')
    rec('    ###   ### **(L2)** b233: the corpus\'s arrangement is annotated as fixed by a')
    rec('    ###     calibration, which is a different claim from *committed before any answer*;')
    rec('    ###   ### **(L3)** b235: a sign warranted by a calibration is an instrument fact;')
    rec('    ###   ### **(L4)** b315: the calibration fixes an ORIENTATION and `A` is an')
    rec('    ###     independent integral;')
    rec('    ###   ### **(L5)** b318 MEASURED the fifth link FALSE -- the corpus\'s window is not in')
    rec('    ###     the source\'s class at all. ### **SO THE CHAIN IS BROKEN AND THE COMPARISON')
    rec('    ###     ### BELOW CARRIES NO INFERENCE IN EITHER DIRECTION.**')
    rec('    %-6s %-16s %-16s %-16s' % ('a', 'W_inf (this act)', 'corpus A (banked)', 'ratio'))
    for w in rows:
        rec('    %-6g %-16.9f %-16.9f %-16.6f'
            % (w['a'], w['weil'], w['arch'],
               w['weil'] / w['arch'] if abs(w['arch']) > 0 else float('nan')))
    rec('    ### **REPORTED, NOT CONCLUDED.** ### They are two different functionals at two')
    rec('    ### different test functions, and (L5) says the corpus\'s is outside the class where')
    rec('    ### the source\'s theorem speaks.')

    # ---- the two axes at the covered cells, for the reach
    rec('')
    rec('  ### (2d) THE TWO AXES AT THE COVERED CELLS, WITH RANK BESIDE EVERY ROW.')
    axes = {}
    for a in covered:
        rec('')
        rec('    ### `a = %g`' % a)
        rec('      %-8s %-7s %-8s %-6s %-16s %-12s' % ('axis', 'N', 'X', 'rank', 'SQUARE', 'drift'))
        gv = [RES[(tuple(fk), a)] for fk in SM.GRID_AXIS]
        dv = [RES[(tuple(fk), a)] for fk in SM.DOMAIN_AXIS]
        for i, fk in enumerate(SM.GRID_AXIS):
            dr = (abs(gv[i] - gv[i - 1]) / max(abs(gv[i]), 1e-300)) if i else None
            rec('      %-8s %-7d %-8.1f %-6d %-16.9f %-12s'
                % ('grid' if i == 0 else '', fk[0], fk[1], FI[tuple(fk)]['rank'], gv[i],
                   '-' if dr is None else '%.3e' % dr))
        for i, fk in enumerate(SM.DOMAIN_AXIS):
            dr = (abs(dv[i] - dv[i - 1]) / max(abs(dv[i]), 1e-300)) if i else None
            rec('      %-8s %-7d %-8.1f %-6d %-16.9f %-12s'
                % ('domain' if i == 0 else '', fk[0], fk[1], FI[tuple(fk)]['rank'], dv[i],
                   '-' if dr is None else '%.3e' % dr))
        axes[a] = dict(grid=gv, domain=dv,
                       grank=[FI[tuple(fk)]['rank'] for fk in SM.GRID_AXIS],
                       drank=[FI[tuple(fk)]['rank'] for fk in SM.DOMAIN_AXIS])

    rec('')
    rec('  ### (2e) THE REACH, AGAINST THE CORRECTED BAR (B3).')
    rec('    ### **GRID: rank CONSTANT and drift below %.0f per cent.**' % (SM.BAR_REACH * 100.0))
    rec('    ### **DOMAIN: drift below %.0f per cent; the rank MAY GROW and need only be MONOTONE.**'
        % (SM.BAR_REACH * 100.0))
    rec('    ### b319 sealed a bar requiring the rank constant on BOTH axes and its own Component 4')
    rec('    ### showed that unsatisfiable. ### **THE CORRECTION WAS MADE IN THIS ACT\'S')
    rec('    ### ### REGISTRATION, BEFORE ANY VALUE**, and not after seeing one.')
    gi = list(SM.GRID_AXIS).index(ref)
    di = list(SM.DOMAIN_AXIS).index(ref)
    rec('    %-6s %-13s %-13s %-13s %-13s %-9s'
        % ('a', 'grid drift', 'domain drift', 'grid rank', 'domain rank', 'inside?'))
    reach = {}
    for a in covered:
        gv, dv = axes[a]['grid'], axes[a]['domain']
        gr, dr_ = axes[a]['grank'], axes[a]['drank']
        gd = abs(gv[gi + 1] - gv[gi]) / max(abs(gv[gi + 1]), 1e-300)
        dd = abs(dv[di + 1] - dv[di]) / max(abs(dv[di + 1]), 1e-300)
        gstable = gr[gi] == gr[gi + 1]
        dmono = dr_[di + 1] >= dr_[di]
        inside = (gd < SM.BAR_REACH) and gstable and (dd < SM.BAR_REACH) and dmono
        reach[a] = dict(gd=gd, dd=dd, gstable=gstable, dmono=dmono, inside=inside)
        rec('    %-6g %-13.3e %-13.3e %-13s %-13s %-9s'
            % (a, gd, dd, '%d->%d' % (gr[gi], gr[gi + 1]), '%d->%d' % (dr_[di], dr_[di + 1]),
               'YES' if inside else '### NO'))
    n_in = sum(1 for v in reach.values() if v['inside'])
    rec('    ### ### **COVERED CELLS INSIDE THE REACH : %d OF %d.**' % (n_in, len(covered)))

    rec('')
    rec('  ### (2f) THE NOISE-FLOOR GATE, IN THE PATH.')
    items = []
    for a in covered:
        gv, dv = axes[a]['grid'], axes[a]['domain']
        items.append(('grid   a=%g' % a, gv[-2], gv[-1]))
        items.append(('domain a=%g' % a, dv[-2], dv[-1]))
    ngood, nrows, ndetail = NF.gate(items, label='b320') if items else (True, [], 'no pairs')
    for name, value, refined, verdict, why in nrows:
        rec('    %-16s %-16.9f -> %-16.9f  %-10s' % (name, value, refined, verdict))
    rec('    ### %s' % ndetail)

    # ================================================================ COMPONENT 3
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE CONTROL.')
    rec('=' * 100)
    testable = [a for a in covered if reach[a]['inside']]
    rec('  ### **THE INEQUALITY: ### `W_infinity(g conv g^#) >= Tr(theta(g) S theta(g)^)`.**')
    if not covered:
        rec('  ### ### **NO CELL IS COVERED. ### THE CONTROL IS UNTESTABLE.**')
        verdict = 'UNTESTABLE'
    elif not testable:
        verdict = 'UNTESTABLE'
        rec('  ### ### **NO COVERED CELL LIES INSIDE THE REACH. ### THE CONTROL IS UNTESTABLE**, the')
        rec('  ### band statement stands, and the cell nearest the reach is reported:')
        best = min(covered, key=lambda a: max(reach[a]['gd'], reach[a]['dd']))
        rec('    ### nearest: `a = %g`, grid drift %.3e, domain drift %.3e against a bar of %.3e'
            % (best, reach[best]['gd'], reach[best]['dd'], SM.BAR_REACH))
    else:
        rec('    %-6s %-16s %-16s %-16s %-10s'
            % ('a', 'LEFT W_inf', 'RIGHT square', 'margin', 'holds?'))
        bad = []
        for a in testable:
            w = [x for x in rows if x['a'] == a][0]
            rec('    %-6g %-16.9f %-16.9f %-16.9f %-10s'
                % (a, w['weil'], w['square'], w['margin'], 'YES' if w['holds'] else '### NO'))
            if not w['holds']:
                bad.append(a)
        if bad:
            verdict = 'FAILS'
            rec('  ### ### **THE CONTROL FAILS AT %s.**' % (', '.join('%g' % a for a in bad)))
            rec('  ### **THE LINK ORDER FIXED AT (B6) IS FOLLOWED AND NOTHING IS WIDENED:**')
            rec('  ###   ### (1) the normalizations (N1)-(N4); (2) the adjoint factor and the')
            rec('  ###   multiplicative measure; (3) the transform convention; (4) the principal')
            rec('  ###   value and its constant; (5) the sign chain; (6) the rank.')
        else:
            verdict = 'HOLDS'
            rec('  ### ### **THE CONTROL HOLDS AT EVERY COVERED CELL INSIDE THE REACH.**')
            rec('  ### **AND WHAT THAT CERTIFIES IS THE INSTRUMENT, AT EXACTLY THAT SCOPE:** ### the')
            rec('  ### source proved this theorem; this act checked that the instrument, on the')
            rec('  ### object\'s own space and with both sides computed from the paper\'s own')
            rec('  ### displays, does not contradict it. ### **NO THEOREM IS PROVED HERE.**')
    rec('  ### ### **VERDICT : %s**' % verdict)

    # ================================================================ COMPONENT 4
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 4 -- THE UNCOVERED CELLS, AS DATA.')
    rec('=' * 100)
    rec('  ### ### **REPORTED AND NOT INTERPRETED. ### THE WINDOW ACT OWNS THEIR MEANING.**')
    rec('  ### The corpus\'s prime sum is quoted beside them from `tools/e16/carto_atlas.py`, whose')
    rec('  ### `channels()` forms it as `2 log p / sqrt(n)` over the prime powers inside the cell.')
    rec('')
    rec('  ### CHART-READY BLOCK -- columns: a, W_inf, SQUARE, margin, prime, arch')
    for w in rows:
        if w['covered']:
            continue
        rec('  ###DATA %g %.9f %.9f %.9f %.9f %.9f'
            % (w['a'], w['weil'], w['square'], w['margin'], w['prime'], w['arch']))
    rec('')
    rec('    %-6s %-16s %-16s %-16s %-14s'
        % ('a', 'W_inf', 'SQUARE', 'margin', 'corpus prime'))
    for w in rows:
        if w['covered']:
            continue
        rec('    %-6g %-16.9f %-16.9f %-16.9f %-14.9f'
            % (w['a'], w['weil'], w['square'], w['margin'], w['prime']))
    rec('  ### **THE THEOREM DOES NOT COVER THESE CELLS AND NEITHER DOES THIS ACT.** ### No claim is')
    rec('  ### attached to any number above, in either direction.')

    payload = dict(class_f=c1, thm1=c1b, covered=covered, rows=rows,
                   frames=dict((str(k), v) for k, v in FI.items()),
                   axes=dict((str(k), v) for k, v in axes.items()),
                   reach=dict((str(k), v) for k, v in reach.items()),
                   verdict=verdict, n_inside=n_in if covered else 0,
                   C_R=WE.C_R, C_spread=WE.C_SPREAD,
                   noise_ok=ngood, noise=[(n, v, r, vd) for n, v, r, vd, _w in nrows],
                   elapsed=time.time() - t0, fails=fails, soft=soft)
    io.open(os.path.join(D, 'b320_rows.json'), 'w', encoding='utf-8',
            newline='\n').write(json.dumps(payload, indent=1, default=float) + '\n')

    rec('')
    rec('  ### CHECKS FAILING : %d' % len(fails))
    for f in fails:
        rec('    ### FAILED: %s' % f)
    rec('  ### ### **UNCONFIRMED : %d**' % len(soft))
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)
    return (0 if not fails else 1), LINES, payload


if __name__ == '__main__':
    code, ls, _p = main()
    io.open(os.path.join(D, 'b320_components_run.txt'), 'w', encoding='utf-8',
            newline='\n').write(chr(10).join(ls) + chr(10))
    sys.exit(code)
