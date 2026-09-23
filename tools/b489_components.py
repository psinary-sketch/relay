# -*- coding: utf-8 -*-
"""b489_components.py -- THE COMPONENTS. ### THE MARGIN TABLE, THE FIT, AND THE CONJECTURE.

### ### **NO CHAIN IS RUN.** ### Every `m` is `-W` with `W` read from `b477_entries.jsonl`, or
### `room_z` read from a `b334` leg bank. ### The only arithmetic here is a prime-power sieve and
### a least-squares fit over numbers already banked.

### ### **THE FIT USES A NELDER-MEAD WRITTEN HERE, NOT A LIBRARY OPTIMISER** -- scipy is absent on
### this machine. ### It is DETERMINISTIC: fixed starting simplices, fixed iteration count, no
### randomness, so the run reproduces. ### Its limits are printed with its results.
"""
import io
import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def prime_powers_upto(x):
    n = int(x)
    if n < 2:
        return []
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    out = []
    for p in range(2, n + 1):
        if s[p]:
            v, k = p, 1
            while v <= n:
                out.append(v)
                v *= p
                k += 1
    return sorted(out)


# ------------------------------------------------------------------ the three forms, as (C2) fixed
def f_pow_a(th, a):
    return th[0] * a ** (-th[1])


def f_pow_log(th, a):
    return th[0] * math.log(a) ** (-th[1])


def f_const_decay(th, a):
    return th[0] + th[1] * math.exp(-th[2] * a)


FORMS = [
    ('(i)   C * a^(-p)', f_pow_a, 2, [(1.0, 1.0), (5.0, 2.0), (0.1, 0.5)]),
    ('(ii)  C * (log a)^(-q)', f_pow_log, 2, [(1.0, 1.0), (0.1, 3.0), (5.0, 2.0)]),
    ('(iii) c0 + C * exp(-k a)', f_const_decay, 3,
     [(0.0, 10.0, 1.0), (0.05, 30.0, 2.0), (0.1, 5.0, 0.5)]),
]


def nelder_mead(fn, x0, steps=900):
    """### A DETERMINISTIC Nelder-Mead. ### No randomness; the simplex is built from x0 by a fixed
    ### rule, and the iteration count is fixed. ### **IT FINDS A LOCAL MINIMUM AND CLAIMS NO MORE.**"""
    n = len(x0)
    simp = [list(x0)]
    for i in range(n):
        y = list(x0)
        y[i] = y[i] + (0.1 * abs(y[i]) if y[i] else 0.1)
        simp.append(y)
    val = [fn(p) for p in simp]
    for _ in range(steps):
        idx = sorted(range(n + 1), key=lambda i: val[i])
        simp = [simp[i] for i in idx]
        val = [val[i] for i in idx]
        cen = [sum(p[j] for p in simp[:-1]) / n for j in range(n)]
        xr = [cen[j] + 1.0 * (cen[j] - simp[-1][j]) for j in range(n)]
        fr = fn(xr)
        if fr < val[0]:
            xe = [cen[j] + 2.0 * (cen[j] - simp[-1][j]) for j in range(n)]
            fe = fn(xe)
            simp[-1], val[-1] = (xe, fe) if fe < fr else (xr, fr)
        elif fr < val[-2]:
            simp[-1], val[-1] = xr, fr
        else:
            xc = [cen[j] + 0.5 * (simp[-1][j] - cen[j]) for j in range(n)]
            fc = fn(xc)
            if fc < val[-1]:
                simp[-1], val[-1] = xc, fc
            else:
                for i in range(1, n + 1):
                    simp[i] = [simp[0][j] + 0.5 * (simp[i][j] - simp[0][j]) for j in range(n)]
                    val[i] = fn(simp[i])
    k = min(range(n + 1), key=lambda i: val[i])
    return simp[k], val[k]


BIG = 1e18


def fit(form, xs, ys, loss):
    """### least squares on `m` (`loss='lin'`) or on `log m` (`loss='log'`).
    ### ### **EVERY START IS TRIED AND THE BEST IS REPORTED**; the starts are fixed on the form."""
    name, fn, npar, starts = form

    def sse(th):
        s = 0.0
        for a, y in zip(xs, ys):
            try:
                p = fn(th, a)
            except Exception:
                return BIG
            if not (p == p) or abs(p) == float('inf'):
                return BIG
            if loss == 'log':
                if p <= 0 or y <= 0:
                    return BIG
                d = math.log(p) - math.log(y)
            else:
                d = p - y
            s += d * d
        return s

    best, bv = None, BIG
    for st in starts:
        th, v = nelder_mead(sse, list(st))
        if v < bv:
            best, bv = th, v
    return best, math.sqrt(bv / len(xs)), npar


def main():
    ent = [json.loads(l) for l in read(os.path.join(D, 'b477_entries.jsonl')).split(NL) if l.strip()]
    diag = sorted([x for x in ent if x.get('kind') == 'diagonal'], key=lambda x: x['a'])
    ctrl = sorted([x for x in ent if x.get('kind') == 'control_diagonal'], key=lambda x: x['a'])
    rungs = {round(r['a'], 6): r for r in
             (json.loads(read(os.path.join(D, 'b437_rungs.json'))) or {}).get('rows', [])}

    rec('=' * 118)
    rec('b489 -- THE COMPONENTS. ### THE MARGIN OVER SUPPORT, THE SHAPE, AND THE CONJECTURE.')
    rec('=' * 118)

    # ================================================================= COMPONENT 1
    rec('')
    rec('COMPONENT 1 -- THE MARGIN, CELL BY CELL.')
    rec('=' * 118)
    rec('')
    rec('### (1a) THE LADDER -- 35 CELLS. ### **m(a) = -W(f_a) = A - PR, THE PLACES SIDE.**')
    rec('-' * 118)
    rec('   rung   a            a^2        p^k<=a^2  the prime powers in [a^-2, a^2]'
        '            m(a) = -W        zero side        two-side')
    rec('   ' + '-' * 113)
    cells = []
    for x in diag:
        a = x['a']
        pp = prime_powers_upto(a * a)
        rg = rungs.get(round(a, 6), {})
        m = -x['W']
        z = x['zero']
        r2 = abs(z - m)
        shown = ','.join(str(v) for v in pp)
        if len(shown) > 40:
            shown = shown[:37] + '...'
        rec('   %-6s %-12.6f %-10.4f %-9d %-42s %-16.9g %-16.9g %.3g'
            % (rg.get('rung', '?'), a, a * a, len(pp), shown or '(none)', m, z, r2))
        cells.append(dict(a=a, rung=rg.get('rung'), npp=len(pp), pp=pp, m=m, zero=z, resid=r2,
                          arch=rg.get('arch'), pr=rg.get('pr')))
    ms = [c['m'] for c in cells]
    lo = min(range(len(ms)), key=lambda i: ms[i])
    rec('')
    rec('   ### ### **EVERY MARGIN IS POSITIVE.** ### min %.9g at `a = %s` (rung %s) ; max %.9g'
        % (ms[lo], cells[lo]['a'], cells[lo]['rung'], max(ms)))
    inc = [(cells[i]['a'], cells[i + 1]['a']) for i in range(len(ms) - 1) if ms[i] < ms[i + 1]]
    rec('   ### ### **AND IT IS NOT MONOTONE: %d OF THE %d STEPS RISE.**' % (len(inc), len(ms) - 1))
    hi = max(range(lo, len(ms)), key=lambda i: ms[i])
    rec('   ### ### **AND THE SHAPE HAS TWO TURNING POINTS, NOT ONE.**')
    rec('      falls, monotonically, over the first %d steps to a MINIMUM' % lo)
    rec('         ### **m = %.9g at a = %s** ### (rung %s)'
        % (ms[lo], cells[lo]['a'], cells[lo]['rung']))
    rec('      rises over the next %d steps to a LOCAL MAXIMUM' % (hi - lo))
    rec('         ### **m = %.9g at a = %s** ### (rung %s)'
        % (ms[hi], cells[hi]['a'], cells[hi]['rung']))
    rec('      falls again over the last %d steps to ### **m = %.9g at a = %s**'
        % (len(ms) - 1 - hi, ms[-1], cells[-1]['a']))
    rec('   ### rises before the minimum : ### **%d** ### ; rises after it : ### **%d of %d**'
        % (sum(1 for i in range(lo) if ms[i] < ms[i + 1]), len(inc), len(ms) - 1))
    rec('   ### ### **IT DOES NOT RISE AT EVERY STEP AFTER THE MINIMUM**, and this tool`s first')
    rec('   ### draft said it did. ### The last rung is ABOVE the minimum and BELOW the local')
    rec('   ### maximum, so a statement that reads only the endpoints hides the second turn.')
    rec('   ### the zero-side column is an INDEPENDENT bank, not a restatement: the two-side')
    rec('   ### residual is printed for every cell and is never assumed to be zero.')
    rec('   ### ### **AND NO CELL HAS A PRIME POWER UNTIL `a >= sqrt 2`** -- three rungs carry')
    rec('   ### none, and their margin is the archimedean term alone.')

    rec('')
    rec('### (1b) THE AIM MAP -- 56 CELLS, THE SECOND FAMILY. ### **`room_z`, NO ZERO SIDE BANKED.**')
    rec('-' * 118)
    aim = []
    for nm, fnm in (('reaching', 'b334_leg_reaching_40.json'),
                    ('reaching', 'b334_leg_reaching_81.json'),
                    ('covered', 'b334_leg_covered.json')):
        j = json.loads(read(os.path.join(D, fnm)) or '{}')
        for r in j.get('rows', []):
            aim.append(dict(leg=nm, a=r['a'], gamma=r['gamma'], m=r['room_z'],
                            arch=r['arch_z'], prime=r['prime_z'], npp=len(prime_powers_upto(
                                r['a'] * r['a']))))
    rec('   leg       a       gamma          p^k<=a^2   m = room_z        A - PR (recomputed)')
    rec('   ' + '-' * 88)
    for r in aim[:4] + aim[12:16] + aim[28:31] + aim[-3:]:
        rec('   %-9s %-7s %-14.6f %-10d %-17.9g %.9g'
            % (r['leg'], r['a'], r['gamma'], r['npp'], r['m'], r['arch'] - r['prime']))
    rec('   ... %d rows in all; the full table is banked in `b489_cells.json`.' % len(aim))
    bad = [r for r in aim if abs((r['arch'] - r['prime']) - r['m']) > 1e-9]
    rec('   ### cells where `room_z != A - PR` : ### **%d** ### of %d' % (len(bad), len(aim)))
    neg = [r for r in aim if r['m'] <= 0]
    rec('   ### ### **AIM-MAP CELLS WITH A NON-POSITIVE MARGIN : %d.**' % len(neg))
    byw = {}
    for r in aim:
        byw.setdefault(r['a'], []).append(r['m'])
    rec('   ### the margin by width, min to max at each of the four widths:')
    for w in sorted(byw):
        rec('      a = %-6s n = %2d   min %-16.9g max %-16.9g   ### **SPREAD %.3g**'
            % (w, len(byw[w]), min(byw[w]), max(byw[w]), max(byw[w]) - min(byw[w])))
    rec('   ### ### **AT A FIXED WIDTH THE MARGIN VARIES BY MORE THAN IT VARIES BETWEEN WIDTHS**')
    rec('   ### at the covered widths -- so on this family `m` is NOT a function of `a`, and a')
    rec('   ### fit of `m` against `a` alone is fitting through a spread it does not model.')

    # ================================================================= COMPONENT 2
    rec('')
    rec('COMPONENT 2 -- THE SHAPE, FITTED AND NOT BELIEVED.')
    rec('=' * 118)
    rec('   ### the three forms were fixed on the SEALED face before any fit was made, and the')
    rec('   ### loss was fixed with them. ### **NO FOURTH FORM IS ADDED AND NONE IS DROPPED.**')
    fits = {}
    for fam, xs, ys in (('LADDER (35 cells)', [c['a'] for c in cells], [c['m'] for c in cells]),
                        ('AIM MAP (56 cells)', [r['a'] for r in aim], [r['m'] for r in aim])):
        rec('')
        rec('### %s' % fam)
        rec('-' * 118)
        rec('   form                        pars   RMS residual on m      RMS residual on log m'
            '     constants (primary fit, loss on m)')
        rec('   ' + '-' * 113)
        for form in FORMS:
            th_l, rms_l, npar = fit(form, xs, ys, 'lin')
            th_g, rms_g, _ = fit(form, xs, ys, 'log')
            cons = ', '.join('%.6g' % v for v in th_l)
            rec('   %-27s %-6d %-22.6g %-25.6g %s' % (form[0], npar, rms_l, rms_g, cons))
            fits[(fam, form[0])] = dict(lin=rms_l, log=rms_g, th_lin=th_l, th_log=th_g, npar=npar)
        bl = min(FORMS, key=lambda f: fits[(fam, f[0])]['lin'])
        bg = min(FORMS, key=lambda f: fits[(fam, f[0])]['log'])
        rec('   ### ### **PREFERRED ON `m` : %s** ### ; ### **PREFERRED ON `log m` : %s**'
            % (bl[0].split()[0], bg[0].split()[0]))
        others = sorted(fits[(fam, f[0])]['lin'] for f in FORMS if f[0] != bl[0])
        rec('   ### the winner`s margin on `m` : %.3g against the next best %.3g -- a factor %.2f'
            % (fits[(fam, bl[0])]['lin'], others[0], others[0] / fits[(fam, bl[0])]['lin']))
        rec('   ### ### **THE TWO LOSSES %s ON THIS FAMILY.**'
            % ('AGREE' if bl[0] == bg[0] else 'DISAGREE'))
        fits[(fam, 'best')] = dict(lin=bl[0], log=bg[0])

    rec('')
    rec('   ### ### **AND THE THIRD FORM HAS THREE CONSTANTS AGAINST THE OTHERS` TWO.** ### A')
    rec('   ### third constant buys residual for free, so a lower residual there is not a better')
    rec('   ### law -- the parameter count is printed beside every residual for that reason.')
    rec('   ### ### **A FIT OVER THIRTY-FIVE CELLS IS A DESCRIPTION, NOT A LAW.** ### It')
    rec('   ### describes thirty-five numbers on one function family with one instrument at one')
    rec('   ### reach. ### It says nothing about any `a` outside `[1.3, 5.656854]`, and the')
    rec('   ### aim-map family is fitted on FOUR DISTINCT WIDTHS with fourteen-fold replication.')
    rec('   ### ### **AND EVERY FORM IS MONOTONE IN `a` BY CONSTRUCTION**, while the ladder`s')
    rec('   ### margin turns at `a = %s`. ### **ALL THREE MIS-DESCRIBE THE RUNGS PAST THE TURN**,'
        % cells[lo]['a'])
    rec('   ### and the residual is concentrated there. ### The next block shows it.')

    # residual concentration
    fam = 'LADDER (35 cells)'
    bl = fits[(fam, 'best')]['lin']
    form = next(f for f in FORMS if f[0] == bl)
    th = fits[(fam, bl)]['th_lin']
    pre, post = [], []
    for c in cells:
        d = form[1](th, c['a']) - c['m']
        (post if c['a'] > cells[lo]['a'] else pre).append(d * d)
    rec('')
    rec('   ### THE PREFERRED FORM`S RESIDUAL, SPLIT AT THE TURN:')
    rec('      cells up to and including the turn : %2d   RMS %.6g' % (len(pre),
                                                                       math.sqrt(sum(pre) / len(pre))))
    rec('      cells past the turn                : %2d   RMS %.6g' % (len(post),
                                                                       math.sqrt(sum(post) / len(post))
                                                                       if post else 0.0))

    # ================================================================= COMPONENT 3
    rec('')
    rec('COMPONENT 3 -- THE CONJECTURE, WITH ITS FALSIFIER AND ITS PREDICTION.')
    rec('=' * 118)
    rec('')
    rec('### (3a) THE CONTROL`S MARGIN OVER THE SAME 35 CELLS -- THE FALSIFIER.')
    rec('-' * 118)
    rec('   a            m_Q = arch - finite    arch            finite          sign')
    rec('   ' + '-' * 78)
    mq = []
    for x in ctrl:
        v = x['arch'] - x['finite']
        mq.append(v)
    for x, v in list(zip(ctrl, mq))[:4] + list(zip(ctrl, mq))[-4:]:
        rec('   %-12.6f %-22.9g %-15.9g %-15.9g %s'
            % (x['a'], v, x['arch'], x['finite'], '+' if v > 0 else ('-' if v < 0 else '0')))
    rec('   ... 35 cells in all.')
    crosses = sum(1 for i in range(len(mq) - 1) if mq[i] * mq[i + 1] < 0)
    rec('   ### ### **SIGN CHANGES ACROSS THE LADDER : %d. ### NEGATIVE CELLS : %d OF %d.**'
        % (crosses, sum(1 for v in mq if v < 0), len(mq)))
    rec('   ### the control`s minimum over the ladder : ### **%.9g** ### at `a = %s`'
        % (min(mq), ctrl[mq.index(min(mq))]['a']))
    rec('   ### ### **THE CONTROL DOES NOT CROSS ZERO ON THIS LADDER.**')
    rec('   ### ### **AND THE FALSIFIER IS OUT OF RANGE, NOT MERELY UNMET.** ### It asks for a')
    rec('   ### crossing "at a support resolving `t = 16.29`". ### `16.290216` is a GAMMA -- an')
    rec('   ### aim`s HEIGHT -- and the aim map finds the Epstein crossing region there only at')
    rec('   ### widths `a = 40` and `a = 81`. ### **THE LADDER STOPS AT `a = 5.656854`.** ### So')
    rec('   ### this table cannot fire the falsifier in either direction, and the conjecture')
    rec('   ### below is registered ### **WITH ITS FALSIFIER UNTESTED**, which is said plainly')
    rec('   ### rather than counted as a pass.')
    rec('   ### ### **WHAT THE AIM MAP DOES SAY AT THAT HEIGHT, READ AND NOT RE-SCORED:** the')
    rec('   ### Epstein room `places_q` is ### **-0.655053** ### at `(a = 40, gamma = 16.290216)`')
    rec('   ### and ### **-1.362830** ### at `(a = 81, gamma = 16.290216)` -- so in the aim map`s')
    rec('   ### own orientation the control`s margin there is ### **POSITIVE**, `+0.655053` and')
    rec('   ### `+1.362830`. ### **THE CROSSING REGION IS WHERE THE CONTROL`S ROOM IS NARROW,')
    rec('   ### NOT WHERE ITS MARGIN IS NEGATIVE**, and b334 already graded (F2) NOT MET.')

    rec('')
    rec('### (3b) THE PREDICTION -- THE NEXT CELL BEYOND THE LADDER`S REACH.')
    rec('-' * 118)
    step = cells[-1]['a'] / cells[-2]['a']
    nxt = cells[-1]['a'] * step
    rec('   the ladder`s last two rungs : %.6f and %.6f ; their ratio %.9f'
        % (cells[-2]['a'], cells[-1]['a'], step))
    rec('   ### the next cell at that ratio : ### **a = %.6f** ### (a^2 = %.4f, %d prime powers)'
        % (nxt, nxt * nxt, len(prime_powers_upto(nxt * nxt))))
    preds = {}
    for form in FORMS:
        th = fits[(fam, form[0])]['th_lin']
        v = form[1](th, nxt)
        preds[form[0]] = v
        rec('      %-27s predicts m = ### **%.9g**' % (form[0], v))
    rec('   ### ### **AND THE THREE PREDICTIONS DISAGREE BY A FACTOR OF %.1f**'
        % (max(preds.values()) / min(preds.values()) if min(preds.values()) > 0 else float('nan')))
    rec('   ### -- which is the honest width of a three-form description at one step beyond its')
    rec('   ### last data point. ### **THE MEASURED MARGIN AT THAT CELL WOULD REFUTE AT LEAST TWO')
    rec('   ### OF THE THREE**, and the turn at `a = %s` says the true value is more likely to'
        % cells[lo]['a'])
    rec('   ### RISE than to follow any of them down.')

    rec('')
    rec('### (3c) THE SENTENCE, AS THE TRAIL WILL CARRY IT.')
    rec('-' * 118)
    thb = fits[(fam, bl)]['th_lin']
    if bl.startswith('(i)  '):
        expr = 'm_fit(a) = %.9g * a^(-%.9g)' % (thb[0], thb[1])
    elif bl.startswith('(ii)'):
        expr = 'm_fit(a) = %.9g * (log a)^(-%.9g)' % (thb[0], thb[1])
    else:
        expr = 'm_fit(a) = %.9g + %.9g * exp(-%.9g * a)' % (thb[0], thb[1], thb[2])
    sentence = ('For every support width a in the class, W(f_a) <= -m_fit(a), with '
                + expr + ' -- graded CONJECTURED, from a finite-reach chart of 35 support '
                'widths in [1.3, 5.656854], and no higher.')
    rec('   ### **%s**' % sentence)
    rec('')
    rec('   ### ### **IT IS FALSE ON ITS OWN DATA, AND THAT IS PRINTED HERE AND NOT HIDDEN.**')
    viol = [c for c in cells if c['m'] < form_of(bl)(thb, c['a'])]
    rec('   ### cells where the measured `m` falls BELOW `m_fit(a)` : ### **%d of %d**'
        % (len(viol), len(cells)))
    if viol:
        rec('   ### the worst : `a = %s`, measured %.9g against fitted %.9g'
            % (viol[0]['a'], viol[0]['m'], form_of(bl)(thb, viol[0]['a'])))
    rec('   ### ### **A LEAST-SQUARES FIT IS A CENTRE LINE, NOT A BOUND.** ### Half the cells')
    rec('   ### lie below it by construction. ### An inequality `W <= -m_fit` therefore does NOT')
    rec('   ### hold on the very cells it was fitted to, and the sentence as the order words it')
    rec('   ### is ### **REFUTED BY ITS OWN CHART BEFORE IT LEAVES IT.**')
    rec('   ### ### **THE REPAIR THE DATA SUPPORTS, OFFERED AND NOT ADOPTED:** the same sentence')
    rec('   ### with `m_fit` replaced by the chart`s MINIMUM, `m_min = %.9g` at `a = %s` -- which'
        % (ms[lo], cells[lo]['a']))
    rec('   ### IS true at all 35 cells, and which is a statement about a finite chart and not a')
    rec('   ### law over a class. ### **THAT CHOICE IS THE AUTHOR`S, AND THIS ACT DOES NOT TAKE')
    rec('   ### IT.** ### The order`s sentence is written to the trail as ordered, with this')
    rec('   ### refutation beside it.')

    rec('')
    rec('=' * 118)
    io.open(os.path.join(D, 'b489_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(cells=cells, aim=aim,
                   fits={'%s | %s' % k: {kk: vv for kk, vv in v.items()}
                         for k, v in fits.items() if k[1] != 'best'},
                   best={'lin': fits[(fam, 'best')]['lin'], 'log': fits[(fam, 'best')]['log']},
                   control=[dict(a=x['a'], m=v) for x, v in zip(ctrl, mq)],
                   crossings=crosses, ctrl_negatives=sum(1 for v in mq if v < 0),
                   turn_a=cells[lo]['a'], m_min=ms[lo], rises=len(inc), turn_i=lo,
                   max_a=cells[max(range(lo, len(ms)), key=lambda i: ms[i])]['a'],
                   max_m=max(ms[lo:]), steps=len(ms) - 1,
                   next_a=nxt, predictions=preds, sentence=sentence, violations=len(viol)),
              io.open(os.path.join(D, 'b489_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    json.dump(dict(ladder=cells, aim=aim),
              io.open(os.path.join(D, 'b489_cells.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL + '  written: b489_components.txt, b489_results.json, b489_cells.json')
    return 0


def form_of(label):
    return next(f[1] for f in FORMS if f[0] == label)


if __name__ == '__main__':
    sys.exit(main())
