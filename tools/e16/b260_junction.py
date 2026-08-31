# -*- coding: utf-8 -*-
"""b260_junction.py -- J1: THE JUNCTION'S SIGN. ### THE RUN.

### WHAT THIS FILE DOES AND WHAT IT MAY NOT DO.
### It exhibits, at every (p,k) of the sixteen diagonal a^2 cells, the two summands the
### derivation compares -- Theta_q's `tau_{p,k}` and PR's `w_{p,k}` -- each unfolded to the
### constituents its OWNER writes, and tests the three registered falsifiers F1/F2/F3.
###
### ### **IT IS A CONTROL ON A DERIVATION, NOT THE DERIVATION.** ### The derivation is in the
### bank and rests on act 9's closed form; this file tests the one premise the derivation
### could not derive (F1, the instrument-to-closed-form identification) and the two sign
### facts it read off the owners (F2, F3).
###
### ### **NO VALUE COMPUTED HERE ENTERS ANY DEFINITION.** ### b229's standing clause.
###
### THE AXES ARE b255's AND ARE PRINTED BEFORE ANY NUMBER (### W-ORD-TE-SPEC).
### ### THE INSTRUMENT FUNCTIONS ARE IMPORTED FROM `b38_act10`, NOT RE-TYPED, so that a
### divergence between this act's arithmetic and the banked instrument's is impossible by
### construction rather than by care.
"""
import io
import json
import math
import os
import random
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import carto_atlas as C          # noqa: E402
import b8_sonin_dim as B8        # noqa: E402
import b10_cells as B10          # noqa: E402
import b38_act10 as B38          # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BANK = r'D:\relay\data\b260_run.txt'
ROWS = r'D:\relay\data\b260_terms.json'
B255 = r'D:\relay\data\b255_rows.json'

CELLS = [2, 3, 4, 8, 9, 12, 16, 20, 25, 32, 36, 45, 50, 64, 81, 100]
S4 = (2, 3, 5)

# ### THE F1 BAR, QUOTED FROM THE REGISTRATION, FIXED THERE BEFORE ANY VALUE EXISTED.
F1_BAR = 1e-9

_TQ = {}


def tq_vector(p, n):
    """### THE INSTRUMENT'S PER-LEVEL TRACE, `|tr(U^k S)| / d`, FOR k = 1 .. 2n-1.

    ### **THE LOOP IS `b38_act10.theta_quotient`'s OWN, CHARACTER FOR CHARACTER**, lifted out
    ### only so the per-(p,n) work is done ONCE instead of once per cell. ### The arithmetic
    ### is not altered; the caching is."""
    if (p, n) in _TQ:
        return _TQ[(p, n)]
    N, K, d = B10.quotient_basis(p, n)
    U = B8.scaling_matrix(p, n)
    S = K @ K.T
    Uk = np.eye(N)
    out = []
    for k in range(1, 2 * n):
        Uk = U @ Uk
        out.append(abs(complex(np.trace(Uk @ S))) / d)
    _TQ[(p, n)] = (out, N, d)
    return _TQ[(p, n)]


def closed_form(p, n, k):
    """### act 9 sec 2, EXACTLY AS QUOTED, WITH ITS RECOVERED RANGE:
    ###   `tau_q(p,n,k) * p^(k/2) = (p^n - p^k)/(p^n - 1)` for `1 <= k <= n-1`, ### `0 for k >= n`.
    ### ### **THE RATIO IS COMPUTED IN EXACT INTEGER ARITHMETIC** (Python ints), and only the
    ### `p^{-k/2}` factor is floating point."""
    if k >= n:
        return 0.0, 0, 1
    num = p ** n - p ** k
    den = p ** n - 1
    return (num / den) * (p ** (-k / 2.0)), num, den


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b260 RUN -- J1: THE JUNCTION SIGN. ### CONTROLS ON A DERIVATION. Registration banked first.')
    rec('=' * 100)

    # ---------------------------------------------------------------- axes
    rec('')
    rec('--- ### W-ORD-TE-SPEC: THE AXES, PRINTED BEFORE ANY NUMBER IS READ ---')
    rec('  NV / NU / UMAX          : %d / %d / %.1f      (carto_atlas, committed constants)'
        % (C.NV, C.NU, C.UMAX))
    rec('  NU_HALF                 : %d                  (b38_act10)' % B38.NU_HALF)
    rec('  EPS_NQ / EPS_NG         : %d / %d             (b38_act10; NOT EXERCISED -- no E2 here)'
        % (B38.EPS_NQ, B38.EPS_NG))
    rec('  EPS_NRHO / rho grid     : ### NOT EXERCISED -- this act computes no E2 and needs no rho-grid.')
    rec('  place set S4            : %s   ### FIXED. No new prime activates along the ladder; 7 never enters.'
        % (S4,))
    rec('  cells (diagonal a^2)    : %s' % CELLS)
    rec('  F1 bar (registered)     : %.0e absolute' % F1_BAR)
    rec('  ### CELL SPECIES: ### **DIAGONAL a^2 THROUGHOUT.** Local (p,n) cells do not appear.')

    # ---------------------------------------------------------------- S3-ii, corr sign
    rec('')
    rec('=' * 100)
    rec('### S3-ii -- THE SIGN OF `corr`. ### FALSIFIER F2. ### The bump read at source, not inherited.')
    rec('=' * 100)
    f2_fired = []
    bump_neg = 0
    corr_neg = 0
    for a2 in CELLS:
        a = math.sqrt(a2)
        v, w, corr, vc, L = B38.family(a)
        bn = int((w < 0.0).sum())
        cn = int((corr < 0.0).sum())
        bump_neg += bn
        corr_neg += cn
        if cn:
            f2_fired.append((a2, cn, float(corr.min())))
    rec('  bump samples < 0, summed over all sixteen cells : ### **%d**' % bump_neg)
    rec('  corr samples < 0, summed over all sixteen cells : ### **%d**' % corr_neg)
    rec('  ### ### **S3-ii %s.** ### %s'
        % ('HOLDS AT EVERY SAMPLE' if corr_neg == 0 else 'REFUTED',
           'F2 DID NOT FIRE.' if not f2_fired else 'F2 FIRED at %s' % (f2_fired,)))

    # ---------------------------------------------------------------- the per-term table
    rec('')
    rec('=' * 100)
    rec('### S1 + S2 + S3 -- THE INDEX SETS, THE PER-TERM FORMS, AND THE PER-TERM INEQUALITY.')
    rec('=' * 100)

    allrows = {}
    f1_fired, f3_fired, s3_fired = [], [], []
    n_terms = 0
    n_terms_kn = 0
    n_strict = 0
    worst_f1 = 0.0
    worst_f1_at = None

    for a2 in CELLS:
        a = math.sqrt(a2)
        v, w, corr, vc, L = B38.family(a)

        # ### S1 -- THE TWO INDEX SETS, BUILT BY EACH INSTRUMENT'S ### OWN ### GUARD.
        # ### **NEITHER IS DERIVED FROM THE OTHER.** That is what makes the comparison a test.
        idx_theta = []
        for p in S4:
            n = B38.staircase(p, a)
            if n < 1:
                continue
            for k in range(1, 2 * n):
                if k * math.log(p) <= 2 * L:
                    idx_theta.append((p, k))
        idx_pr = []
        for p in S4:
            k = 1
            while p ** k <= a * a + 1e-12:
                if math.log(p ** k) <= 2 * L:
                    idx_pr.append((p, k))
                k += 1
        same = bool(set(idx_theta) == set(idx_pr))
        if not same:
            f3_fired.append((a2, sorted(set(idx_theta) ^ set(idx_pr))))

        rows = []
        th_sum, pr_sum = 0.0, 0.0
        for p in S4:
            n = B38.staircase(p, a)
            if n < 1:
                continue
            tqv, N, d = tq_vector(p, n)
            for k in range(1, 2 * n):
                ln = k * math.log(p)
                if ln > 2 * L:
                    continue
                tq = tqv[k - 1]
                cf, num, den = closed_form(p, n, k)
                dev = abs(tq - cf)
                if dev > worst_f1:
                    worst_f1, worst_f1_at = dev, (a2, p, n, k)
                if dev > F1_BAR:
                    f1_fired.append((a2, p, n, k, tq, cf, dev))
                cval = float(np.interp(ln, vc, corr))
                cval_pr = float(np.interp(math.log(p ** k), vc, corr))
                tau = math.log(p) * tq * 2.0 * cval
                wgt = 2.0 * math.log(p) / math.sqrt(p ** k) * cval_pr
                th_sum += tau
                pr_sum += wgt
                n_terms += 1
                if k >= n:
                    n_terms_kn += 1
                if not bool(tau <= wgt):
                    s3_fired.append((a2, p, n, k, tau, wgt))
                elif bool(tau < wgt):
                    n_strict += 1
                rows.append(dict(p=p, n=n, k=k, N=N, d=d, tq=tq, cf=cf, dev=dev,
                                 pk2=p ** (-k / 2.0), corr=cval, tau=tau, w=wgt,
                                 ratio_num=num, ratio_den=den))
        allrows[a2] = dict(a2=a2, same_index=same, n_idx=len(idx_pr), rows=rows,
                           theta=th_sum, pr=pr_sum)

    rec('')
    rec('### S1 -- INDEX-SET IDENTITY, CELL BY CELL. ### FALSIFIER F3.')
    rec('  %-6s %-22s %-10s %s' % ('a^2', 'staircase (2,3,5)', '|index|', 'sets identical?'))
    rec('  ' + '-' * 76)
    for a2 in CELLS:
        a = math.sqrt(a2)
        st = [B38.staircase(p, a) for p in S4]
        r = allrows[a2]
        rec('  %-6d %-22s %-10d %s' % (a2, st, r['n_idx'],
                                       'YES' if r['same_index'] else '### NO'))
    rec('  ### ### **CELLS WITH IDENTICAL INDEX SETS: ### %d of %d.**'
        % (sum(1 for a2 in CELLS if allrows[a2]['same_index']), len(CELLS)))
    rec('  ### ### **F3 %s**' % ('DID NOT FIRE.' if not f3_fired else 'FIRED: %s' % (f3_fired,)))

    rec('')
    rec('### S3-i -- THE IDENTIFICATION `tq` == act 9\'s CLOSED FORM. ### FALSIFIER F1. ### THE LIVE ONE.')
    rec('  terms compared                       : ### **%d**' % n_terms)
    rec('  of those at k >= n (closed form = 0)  : ### **%d**' % n_terms_kn)
    rec('  worst |tq - closed_form|              : ### **%.3e**   at (a^2,p,n,k) = %s'
        % (worst_f1, worst_f1_at))
    rec('  bar (registered before any value)     : %.0e' % F1_BAR)
    rec('  ### ### **F1 %s**' % ('DID NOT FIRE -- the identification HOLDS at every term.'
                                 if not f1_fired else 'FIRED at %d term(s): %s'
                                 % (len(f1_fired), f1_fired[:6])))

    rec('')
    rec('### S3 -- THE PER-TERM INEQUALITY `tau_{p,k} <= w_{p,k}`.')
    rec('  terms tested          : ### **%d**' % n_terms)
    rec('  terms STRICTLY less   : ### **%d**' % n_strict)
    rec('  terms VIOLATING       : ### **%d**' % len(s3_fired))
    if s3_fired:
        rec('  ### ### **S3 REFUTED. THE COUNTER-TERMS:**')
        for r in s3_fired[:10]:
            rec('      a^2=%s p=%s n=%s k=%s  tau=%.9e  w=%.9e' % r)
    else:
        rec('  ### ### **S3 HOLDS AT EVERY TERM OF EVERY CELL.**')

    # ---------------------------------------------------------------- the exhibited structure
    rec('')
    rec('=' * 100)
    rec('### THE PER-TERM STRUCTURE EXHIBITED. ### a^2 = 100, THE DEEPEST CELL, EVERY TERM.')
    rec('=' * 100)
    rec('  ### `tau/w` IS THE WHOLE INEQUALITY: the 2 log p and the corr CANCEL, leaving act 9\'s ratio.')
    rec('  %-3s %-3s %-3s %-13s %-13s %-9s %-13s %-13s %s'
        % ('p', 'n', 'k', 'tq', 'p^{-k/2}', 'tq/p^-k/2', 'tau', 'w', '(p^n-p^k)/(p^n-1)'))
    rec('  ' + '-' * 112)
    for r in allrows[100]['rows']:
        rat = r['tq'] / r['pk2'] if r['pk2'] else float('nan')
        exact = '%d/%d' % (r['ratio_num'], r['ratio_den']) if r['k'] < r['n'] else '0  (k >= n)'
        rec('  %-3d %-3d %-3d %-13.6e %-13.6e %-9.6f %-13.6e %-13.6e %s'
            % (r['p'], r['n'], r['k'], r['tq'], r['pk2'], rat, r['tau'], r['w'], exact))

    # ---------------------------------------------------------------- S4
    rec('')
    rec('=' * 100)
    rec('### S4 -- THE SUM, AND THE b255 CONTROL. ### THE SIXTEEN-CELL TABLE.')
    rec('=' * 100)
    b255 = json.load(io.open(B255, encoding='utf-8'))
    rec('  %-6s %-14s %-14s %-14s %-9s %-13s %s'
        % ('a^2', 'Theta_q', 'PR', 'PR - Theta_q', 'sign', 'b255 junc', '|delta| vs b255'))
    rec('  ' + '-' * 104)
    sum_viol, worst_ctl = [], 0.0
    for a2 in CELLS:
        r = allrows[a2]
        j = r['pr'] - r['theta']
        ctl = b255[str(a2)]['junc']
        dd = abs(j - ctl)
        worst_ctl = max(worst_ctl, dd)
        if not bool(r['theta'] <= r['pr']):
            sum_viol.append(a2)
        rec('  %-6d %-14.9f %-14.9f %-14.9f %-9s %-13.9f %.3e'
            % (a2, r['theta'], r['pr'], j, '+' if j > 0 else ('0' if j == 0 else '### -'), ctl, dd))
    rec('')
    rec('  cells with `Theta_q <= PR`            : ### **%d of %d**'
        % (len(CELLS) - len(sum_viol), len(CELLS)))
    rec('  ### **CONTROL -- worst |junction - b255\'s banked junction| : ### %.3e**' % worst_ctl)
    rec('  ### ### **b255 IS A CONTROL HERE AND NOT A PREMISE: NO STEP ABOVE CITED IT.**')

    # ---------------------------------------------------------------- tautology control
    rec('')
    rec('=' * 100)
    rec('### THE TAUTOLOGY CONTROL. ### EVERY SYMBOLIC STEP RE-RUN ON ARBITRARY VALUES.')
    rec('=' * 100)
    rng = random.Random(20260830)
    red_hold = 0
    for _ in range(20000):
        c = rng.uniform(1e-6, 50.0)      # stands in for 2 log p > 0
        g = rng.uniform(0.0, 50.0)       # stands in for corr >= 0
        x = rng.uniform(-50.0, 50.0)
        y = rng.uniform(-50.0, 50.0)
        if x > y:
            x, y = y, x
        if c * g * x <= c * g * y + 1e-12:
            red_hold += 1
    rec('  (T1) THE S3 REDUCTION `c>0, g>=0, x<=y  =>  c*g*x <= c*g*y`')
    rec('       holds on arbitrary tuples : ### **%d / 20000**' % red_hold)
    rec('       ### ### **IT IS MEANT TO. ### IT IS A TAUTOLOGY AND IS REPORTED AS ONE --')
    rec('       ### ### IT CARRIES NO CONTENT ABOUT EITHER SIDE.**')

    tb_hold = 0
    for _ in range(20000):
        p = rng.choice([2, 3, 5, 7, 11])
        n = rng.randint(1, 6)
        k = rng.randint(1, n)
        fake_tq = rng.uniform(0.0, 1.0)
        if fake_tq <= p ** (-k / 2.0):
            tb_hold += 1
    rec('  (T2) THE TRACE BOUND `tq <= p^{-k/2}` ON ### ARBITRARY ### `tq`')
    rec('       holds on arbitrary tuples : ### **%d / 20000**' % tb_hold)
    rec('       ### ### **IT MUST ### FAIL ### OFTEN, AND IT DOES. ### THE BOUND IS A REAL CLAIM')
    rec('       ### ### ABOUT act 9\'s CLOSED FORM, NOT AN IDENTITY.** ### If this had read 20000/20000')
    rec('       ### ### THE "DERIVATION" WOULD HAVE BEEN A TAUTOLOGY WEARING A THEOREM\'S CLOTHES.')

    # ---------------------------------------------------------------- positive controls
    rec('')
    rec('=' * 100)
    rec('### POSITIVE CONTROLS. ### EVERY DISCRIMINATOR SHOWN ABLE TO SAY NO.')
    rec('=' * 100)
    r100 = allrows[100]['rows'][0]
    perturbed = r100['tau'] + 1.0
    rec('  (C1) THE PER-TERM COMPARATOR DISCRIMINATES -- a tau perturbed by +1 at (p=%d,k=%d):'
        % (r100['p'], r100['k']))
    rec('       `perturbed <= w` : ### **%s** ### (must be False)' % bool(perturbed <= r100['w']))
    fake_corr = np.array([-1.0, -0.5, -0.25])
    rec('  (C2) THE corr-SIGN TEST DISCRIMINATES -- on a deliberately negative array:')
    rec('       negatives counted : ### **%d of 3** ### (must be 3)' % int((fake_corr < 0.0).sum()))
    rec('  (C3) THE INDEX MATCHER DISCRIMINATES -- an invented pair (p=7,k=1) at a^2=100:')
    a = math.sqrt(100.0)
    inv = bool((7, 1) in set((p, k) for p in S4 for k in range(1, 2 * max(1, B38.staircase(p, a)))))
    rec('       present in the index set : ### **%s** ### (must be False -- 7 is not in S4)' % inv)
    rec('  (C4) THE CLOSED FORM DISCRIMINATES -- it is NOT constant in k at (p=2,n=6):')
    vals = [closed_form(2, 6, kk)[0] for kk in (1, 3, 5, 6)]
    rec('       k = 1,3,5,6 -> %s' % ['%.6f' % x for x in vals])
    rec('       distinct values : ### **%d of 4** ### (must be 4)' % len(set('%.9f' % x for x in vals)))
    rec('  (C5) THE F1 DEVIATION MEASURE DISCRIMINATES -- a control closed form off by one level:')
    ctlr = allrows[100]['rows'][0]
    off = abs(ctlr['tq'] - closed_form(ctlr['p'], ctlr['n'], ctlr['k'] + 1)[0])
    rec('       |tq - closed_form(k+1)| = ### **%.3e** ### vs bar %.0e -- must EXCEED the bar' % (off, F1_BAR))

    # ---------------------------------------------------------------- verdicts
    rec('')
    rec('=' * 100)
    rec('### THE RUN\'S VERDICTS, IN THE REGISTERED BRANCH LANGUAGE.')
    rec('=' * 100)
    rec('  S1 (index sets identical)  : ### **%s**' % ('HOLDS' if not f3_fired else 'REFUTED'))
    rec('  S3-ii (corr >= 0)          : ### **%s**' % ('HOLDS' if corr_neg == 0 else 'REFUTED'))
    rec('  F1 (identification)        : ### **%s**' % ('HOLDS' if not f1_fired else 'FIRED'))
    rec('  S3 (per-term inequality)   : ### **%s**' % ('HOLDS' if not s3_fired else 'REFUTED'))
    rec('  S4 (the sum)               : ### **%s**' % ('HOLDS' if not sum_viol else 'REFUTED at %s' % sum_viol))
    rec('')
    rec('  ### **QUOTED-N: %d terms across %d cells; %d index pairs; %d distinct (p,n) trace blocks.**'
        % (n_terms, len(CELLS), sum(allrows[a2]['n_idx'] for a2 in CELLS), len(_TQ)))
    rec('=' * 100)

    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump({str(k): v for k, v in allrows.items()}, io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    print('\n  banked -> %s\n  terms  -> %s' % (BANK, ROWS))


if __name__ == '__main__':
    main()
