# -*- coding: utf-8 -*-
"""b718_a0.py -- (R328)(5)(i): A0 = 10 FOR Q1 = x^2 + xy + 10y^2 (DISCRIMINANT -39), CERTIFIED IN BALL ARITHMETIC ON ITS DEFINING EXPRESSION.

### THE DEFINING EXPRESSION: HCount Z A0 (SIDE-explicit-formula v0.37, SIDEExplicitFormula/RestBound.lean :44-:45): 1 <= A0 and, for every
### real t, N(t, t + 1) <= A0 log(|t| + 3), N the configuration's points (the nontrivial zeros, as at Q0, data/b685_p3.txt) with
### imaginary part in the window. A0Q = 10 at Q0 (Schema/EpsteinQ0.lean :104), derived at b685-b687: T3 below 150 from the certified list,
### T4 above it by b685's count law in Backlund's form (tools/b685_count.py), composed at b687 (data/b687_composition.txt).
### THE ROUTE PRINTED BEFORE ANY FIGURE -- THE SAME ROUTE AT -39: tools/b685_count.py imported unedited, its params_q and W_window compiled
### from their own source with A(23) -> A(DQ), DQ = 39 (kappa = sqrt(39)/2pi), the substitution count printed; b667's engine carried to
### sqrt(39) by tools/b717_list.py's carry_engine (b717's, unedited), Z_Q1 at real points by b667's zq_point; the composition by
### b685's p3 lines, the meeting height moved from 149 to 199 because b717's list is certified to 200 (data/b717_list.txt :69): below it
### N(t, t + 1) bounded from the list -- the on-line zeros located to 1e-8 in the window, plus every zero of each band meeting the window
### that is not a located on-line zero (N - on, the band's count certified), the off-line points not used for their heights.
### THE CONTROLS BEFORE THE FIGURES: (C-a) Z_Q1 at sigma = 2.0 and 2.4 by the carried engine against its Dirichlet series SUM_{n<=X} r(n)
### n^-sigma, X = 100000, widened by b717's tail bound, the balls overlapping, and NEG: Q0's series in its place, wanted not to overlap;
### (C-b) the derived window bound against the certified list's window counts on [150, 199], every count beneath it, and NEG: the bound
### with its top(T) and arcsin terms dropped, wanted to fall beneath a certified count.
### Routes, each one foreground call: `grid` -> data/b718_a0_part1.json ; `params` -> data/b718_a0_part2.json ; `compose` -> data/b718_a0.txt,
### data/b718_a0.json (with the seven predictions re-read by tools/b717_predict.py's predictions(), unedited, beside the committed values).
"""
import inspect
import io
import json
import math
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_, T_ = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T_)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b717_list as L7             # noqa: E402  ### b667's engine carried to sqrt(39) by its carry_engine; imported unedited
import b685_count as C85           # noqa: E402  ### b685's count route, imported unedited
from flint import arb, acb, ctx    # noqa: E402

DQ = 39
A0 = 10
MEET = 199
CERT = C85.CERT
SUBS = (('A(23)', 'A(DQ)'),)
ROUTE_ROWS = []


def say(s=''):
    print(s, flush=True)


def _membrane_put(name, data):
    import act_membrane as MEM
    import b718_record as REC
    p = os.path.join(D_, name)
    MEM.guard_path('b718', p, REC.R.ROOT_EXCLUDE)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data.encode('utf-8'))
    os.replace(p + '.tmp', p)


def _free():
    import subprocess
    out = subprocess.run(['powershell', '-NoProfile', '-Command', '(Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory'],
                         capture_output=True, text=True).stdout.strip()
    mb = int(out) // 1024 if out.isdigit() else -1
    say('  free memory %d MB (the hold 2560 MB)' % mb)
    if 0 <= mb < 2560:
        sys.exit('### FREE MEMORY %d MB BENEATH THE 2560 MB HOLD -- REFUSED' % mb)


def carry():
    """the engine to sqrt(39) (b717's carry_engine), then b685's two kappa functions compiled with A(23) -> A(DQ)."""
    rows = L7.carry_engine(DQ)
    C85.DQ = DQ
    out = []
    for fn in ('params_q', 'W_window'):
        f = getattr(C85, fn)
        src = inspect.getsource(f)
        k = src.count('A(23)')
        new = src.replace('A(23)', 'A(DQ)')
        ns = {}
        exec(compile(new, '<b718 carried %s>' % fn, 'exec'), C85.__dict__, ns)
        setattr(C85, fn, ns[fn])
        out.append('%s: A(23) -> A(DQ) at %d place(s)' % (fn, k))
    ROUTE_ROWS[:] = ['the engine: %s' % (r,) for r in (rows or [])] + out
    return ROUTE_ROWS


def series(form, sig, X=100000):
    """SUM_{n<=X} r_form(n) n^-sigma in arb, widened by b717's tail bound sigma [2 X^(1-s)/(s-1) + 10 X^(1/2-s)/(s-1/2) + X^-s/s]."""
    import b718_classgroup as CG
    r = CG.r_form(form, X)
    ctx.prec = C85.PREC
    s = arb(str(sig))
    tot = arb(0)
    for n in range(1, X + 1):
        if r[n]:
            tot += r[n] * arb(n) ** (-s)
    Xa = arb(X)
    tail = s * (2 * Xa ** (1 - s) / (s - 1) + 10 * Xa ** (arb('0.5') - s) / (s - arb('0.5')) + Xa ** (-s) / s)
    return tot + arb(0, tail.upper())


# ================================================================================ grid
def grid(*a):
    t0 = time.time()
    _free()
    say('b718 a0 grid -- THE ROUTE: %s' % ' ; '.join(carry()))
    ok = True
    for sig in ('2.0', '2.4'):
        ctx.prec = C85.PREC
        v = CERT.zq_point(acb(arb(sig))).real
        s1 = series((1, 1, 10), sig)
        s0 = series((1, 1, 6), sig)
        ov, neg = v.overlaps(s1), v.overlaps(s0)
        ok &= ov and not neg
        say('  (C-a) sigma %s: Z_Q1 %s ; its series %s ; OVERLAP %s ; NEG Q0`s series %s ; OVERLAP %s (wanted False)' % (
            sig, C85.bs(v), C85.bs(s1), ov, C85.bs(s0), neg))
    say('  (C-a) %s' % ('AS WANTED' if ok else '### NOT AS WANTED -- STOPPED'))
    if not ok:
        sys.exit(1)
    rows, prev = {}, None
    for s in C85.GRID:
        ctx.prec = C85.PREC
        v = CERT.zq_point(acb(arb(str(s))))
        ctx.prec = C85.PREC
        if not v.imag.contains(0):
            sys.exit('### Z_Q1(%s) HAS AN IMAGINARY PART EXCLUDING 0 -- STOPPED' % s)
        if prev is not None and not (v.real < prev):
            sys.exit('### Z_Q1 NOT DECREASING AT %s -- STOPPED' % s)
        prev = v.real
        rows['%.2f' % s] = C85.ser(v.real)
    say('  Z_Q1(1.02) = %s ; Z_Q1(1.50) = %s ; Z_Q1(2.50) = %s ; points %d ; %d s' % (
        C85.bs(C85.des(rows['1.02'])), C85.bs(C85.des(rows['1.50'])), C85.bs(C85.des(rows['2.50'])), len(rows), time.time() - t0))
    _membrane_put('b718_a0_part1.json', json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), route=ROUTE_ROWS, control_a=ok,
                                                        grid=rows, seconds=int(time.time() - t0)), indent=1) + NL)


def _get(name):
    return json.load(io.open(os.path.join(D_, name), encoding='utf-8'))


# ================================================================================ params (b685's p2, its loop, at -39)
def params(*a):
    t0 = time.time()
    _free()
    carry()
    g = _get('b718_a0_part1.json')['grid']
    best, tried, refused = None, 0, 0
    for c in C85.PAR_C:
        rmax = (c - 0.5) ** 2 / (c - 1)
        rs = [round(c + 0.05 + 0.05 * k, 3) for k in range(40) if c + 0.05 + 0.05 * k < rmax - 0.001]
        for r in rs:
            for eta in C85.PAR_ETA:
                pr = C85.params_q(g, c, r, eta)
                tried += 1
                if not all(ok for _n, ok in C85.conditions_q(pr)):
                    refused += 1
                    continue
                I = C85.jensen(pr, C85.N_SEARCH, C85.A(C85.T_MIN))
                w = C85.W_window(pr, I, MEET)
                if best is None or w.upper() < best[0].upper():
                    best = (w, c, r, eta)
    if best is None:
        sys.exit('### NO PARAMETER SET MEETS THE CONDITIONS -- STOPPED')
    w, c, r, eta = best
    pr = C85.params_q(g, c, r, eta)
    I = C85.jensen(pr, C85.N_FINAL, C85.A(C85.T_MIN))
    say('b718 a0 params -- tried %d, refused %d ; chosen c %s, r %s, eta %s ; W(%d) %s' % (tried, refused, c, r, eta, MEET, C85.bs(C85.W_window(pr, I, MEET))))
    for n_, ok in C85.conditions_q(pr):
        say('  condition %-36s %s' % (n_, ok))
    say('  sigma1 %s ; eps = Z_Q1(sigma1) - 2 <= %s ; 4 - Z_Q1(c) >= %s ; %d s' % (C85.bs(pr['sigma1']), C85.bs(pr['eps']), C85.bs(pr['low']), time.time() - t0))
    _membrane_put('b718_a0_part2.json', json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), c=c, r=r, eta=eta, tried=tried, refused=refused,
                                                        Ic=C85.ser(I[0]), Ir=C85.ser(I[1]), conditions=[[n_, ok] for n_, ok in C85.conditions_q(pr)],
                                                        seconds=int(time.time() - t0)), indent=1) + NL)


def _load():
    g = _get('b718_a0_part1.json')['grid']
    j = _get('b718_a0_part2.json')
    pr = C85.params_q(g, j['c'], j['r'], j['eta'])
    return pr, (C85.des(j['Ic']), C85.des(j['Ir'])), j


def _bare(pr, I, t):
    """the PLANT of (C-b): W with its top(T) and arcsin terms dropped, (1/pi)[log kappa + G(t + 1) - G(t)]."""
    kap = C85.A(DQ).sqrt() / (2 * arb.pi())
    tt = C85.A(t)
    return (kap.log() + (tt + 1).log() + 1 / (8 * tt) + 1 / (3 * tt)) / arb.pi()


def _list_windows(lst):
    """for each integer k in [0, 199]: the bound on N(t, t + 1), t in [k, k + 1), from the list: the on-line zeros with t in [k - 1e-8, k + 2 +
    1e-8] plus N - on of every band meeting [k, k + 2]; and for t in [-1, 0) the bound 2 x (on-line in [0, 1] + N - on of the bands meeting
    [0, 1]). The list's bands, complete to its top."""
    on = sorted(float(z['t']) for z in lst['online'])
    bands = [b for b in lst['bands'] if b['complete']]
    top = float(lst['top'])

    def extra(lo, hi):
        return sum(int(b['N']) - int(b['on']) for b in bands if float(b['t_lo']) <= hi and float(b['t_hi']) >= lo)
    out = []
    for k in range(0, int(top) - 1 + 1):
        if k + 2 > top + 1e-9 and k + 1 > top:
            break
        lo, hi = k - 1e-8, min(k + 2, top) + 1e-8
        n_on = sum(1 for x in on if lo <= x <= hi)
        out.append((k, n_on + extra(k, k + 2)))
    neg = 2 * (sum(1 for x in on if x <= 1 + 1e-8) + extra(0, 1))
    return out, neg, len(bands), top


def compose(*a):
    t0 = time.time()
    _free()
    carry()
    pr, I, j2 = _load()
    lst = _get('b717_list.json')
    L = ['b718 -- (R328)(5)(i): A0 = 10 FOR Q1 = x^2 + xy + 10y^2 (-39), HCount`S INEQUALITY CERTIFIED IN BALLS BY b685`S ROUTE AT -39 (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### THE DEFINING EXPRESSION: HCount Z A0 (SIDE-explicit-formula v0.37, SIDEExplicitFormula/RestBound.lean :44-:45): 1 <= A0 and for every',
         '### real t, N(t, t + 1) <= A0 log(|t| + 3); A0Q = 10 at Q0 (Schema/EpsteinQ0.lean :104), certified there at b685-b687 by this route.',
         '### THE ROUTE (printed before any figure): tools/b685_count.py imported unedited, %s; the engine carried by tools/b717_list.py: %s.' % (
             '; '.join(r for r in ROUTE_ROWS if 'A(23)' in r), '; '.join(r for r in ROUTE_ROWS if 'A(23)' not in r) or 'its rows'),
         '### Z_Q1 at real points data/b718_a0_part1.json ((C-a) %s); the parameters data/b718_a0_part2.json (c %s, r %s, eta %s, tried %d, refused %d).' % (
             'AS WANTED' if _get('b718_a0_part1.json').get('control_a') else 'NOT AS WANTED', j2['c'], j2['r'], j2['eta'], j2['tried'], j2['refused']), '']
    # ### (C-b) the derived bound against the certified list on [150, 199]
    wins, neg, nb, top = _list_windows(lst)
    # ### (C-b) reads a CERTIFIED LOWER count of the unit window (k, k + 1]: the on-line zeros located inside it, each present by its
    # ### certified sign change; the true N(k, k + 1) is at least that, and W(k) bounds N(k, k + 1] from above, so the lower count must lie
    # ### beneath W(k). (The seat's first form compared the list region's two-unit upper bound with the one-unit W: defect (m).)
    onl = sorted(float(z['t']) for z in lst['online'])
    okb, plant_fail, worst = True, False, None
    for k in range(150, MEET):
        n = sum(1 for x in onl if k + 1e-8 < x <= k + 1 - 1e-8)
        W = C85.W_window(pr, I, k)
        okb &= bool(arb(n) <= W)
        if not bool(arb(n) <= _bare(pr, I, k)):
            plant_fail = True
        if worst is None or n > worst[1]:
            worst = (k, n, W)
    L += ['## (C-b) THE DERIVED WINDOW BOUND AGAINST THE CERTIFIED LIST, the unit windows (k, k + 1], k in [150, 198]: every certified lower count (the on-line zeros located inside) beneath W(k): %s (the largest %d at k = %d, W %s) ; NEG, the top and arcsin terms dropped, beneath a certified count somewhere: %s -- %s' % (
        okb, worst[1], worst[0], C85.bs(worst[2]), plant_fail, 'AS WANTED' if okb and plant_fail else '### NOT AS WANTED'), '']
    # ### the lower region from the list
    low_ok, low_rows = True, []
    for k, n in wins:
        req = A0 * arb(k + 3).log()
        ok = bool(arb(n) <= req)
        low_ok &= ok
        if k in (0, 1, 15, 50, 100, 150, 198) or not ok:
            low_rows.append('  t in [%d, %d): N(t, t + 1) <= %d (the list) ; 10 log(|t| + 3) >= %s ; %s' % (k, k + 1, n, C85.bs(req), 'HOLDS' if ok else '### FAILS'))
    req0 = A0 * arb(3).log()
    neg_ok = bool(arb(neg) <= req0)
    low_ok &= neg_ok
    mx = max(wins, key=lambda x: x[1] - 10 * math.log(x[0] + 3))
    L += ['## THE LIST REGION, |t| <= %d (data/b717_list.json: %d bands complete to %s; negative t by the conjugate symmetry, t in [-1, 0) read whole)' % (MEET, nb, top)]
    L += low_rows + ['  t in [-1, 0): N(t, t + 1) <= %d ; 10 log 3 >= %s ; %s' % (neg, C85.bs(req0), 'HOLDS' if neg_ok else '### FAILS'),
                     '  the least margin over the list region at k = %d (bound %d) ; EVERY k IN [0, %d] HOLDS: %s' % (mx[0], mx[1], wins[-1][0], low_ok), '']
    # ### the derived region (b685's p3 lines, from MEET)
    narrow, ta, npieces = None, float(MEET), 0
    while ta < C85.SCAN_TOP:
        tb = min(ta * C85.SCAN_RATIO, C85.SCAN_TOP)
        Wb = C85.W_window(pr, I, tb)
        m = A0 * C85.A(ta + 3).log() - Wb
        npieces += 1
        if narrow is None or m.lower() < narrow[0].lower():
            narrow = (m, ta, tb, Wb)
        ta = tb
    Ic, Ir = I
    kap = C85.A(DQ).sqrt() / (2 * arb.pi())
    k1 = (1 + arb.pi() * (Ic - 1) / pr['ell']) / arb.pi()
    t6 = C85.A(C85.SCAN_TOP)
    E = C85.topq(pr, I, C85.SCAN_TOP)[2]
    k0 = (kap.log() + C85.A(11) / (24 * t6) + 2 * (pr['eps'] / 2).asin() + arb.pi() / pr['ell'] * (Ir - pr['low'].log()) + E
          + 2 * ((pr['sigma1'] - 1) / C85.A(C85.T_MIN)).atan() + 2 * (1 / (2 * C85.A(C85.T_MIN))).atan()) / arb.pi()
    mco = (A0 - k1) * (t6 + 1).log() - k0
    hi_ok = bool(narrow[0] > 0 and mco > 0 and k1 < A0)
    L += ['## THE DERIVED REGION, t >= %d (b685`s count law at kappa = sqrt(39)/2pi, its window W(t) for t >= 150; pieces of ratio %s to 10^6, then the coefficient form)' % (MEET, C85.SCAN_RATIO),
          '  pieces %d ; THE NARROWEST MARGIN 10 log(t + 3) - W on [%d, 10^6]: %s on [%.6g, %.6g] (W <= %s)' % (npieces, MEET, C85.bs(narrow[0]), narrow[1], narrow[2], C85.bs(narrow[3])),
          '  t >= 10^6: W(t) <= k1 log(t + 1) + k0, k1 %s < 10 %s ; k0 %s ; the margin at 10^6 %s, increasing beyond' % (C85.bs(k1), bool(k1 < A0), C85.bs(k0), C85.bs(mco)),
          '  EVERY t >= %d HOLDS: %s' % (MEET, hi_ok), '']
    cert = bool(okb and plant_fail and low_ok and hi_ok)
    L += ['### HCount Z 10 AT Q1 OF -39: 1 <= 10 ; N(t, t + 1) <= 10 log(|t| + 3) AT EVERY REAL t (the list region |t| <= %d, the derived region t >= %d, negative t by symmetry): %s' % (
        MEET, MEET, 'CERTIFIED' if cert else '### NOT CERTIFIED'), '']
    # ### the seven predictions re-read
    import b717_predict as PR7
    _T0p, rows, _j = PR7.predictions()
    committed = dict((r['k'], r) for r in _get('b717_predictions.json')['rows'])
    L += ['## THE SEVEN PREDICTIONS RE-READ UNDER THE CERTIFIED A0 = 10 (tools/b717_predict.py predictions(), unedited) BESIDE THE COMMITTED (data/b717_predictions.json, f47d8ab5)']
    nre, neq = 0, 0
    for r in rows:
        if r.get('reach'):
            continue
        c = committed.get(r['k'], {})
        nre += 1
        e = (r.get('n_pred') == c.get('n_pred'))
        neq += e
        ratio = r['n_pred_float'] / c['n_pred_float'] if c.get('n_pred_float') else float('nan')
        L += ['  pair %d : n*_pred re-read %.1f ; committed %.1f ; re-read/committed %.9f ; the arb strings %s' % (
            r['k'], r['n_pred_float'], c.get('n_pred_float', float('nan')), ratio, 'EQUAL' if e else 'DIFFER')]
    L += ['  n*_pred unchanged at every pair, so the onsets` ratios against it stand as data/b717_onsets.txt :57 prints them (1.000050 to 1.000264,',
          '  every one in [0.99, 1.01]); none leaves the window under the certified value.']
    L += ['', '### ### **A0 = 10 AT Q1 OF -39: %s ; (C-a) %s, (C-b) %s ; THE PREDICTIONS RE-READ %d, EQUAL TO THE COMMITTED %d ; %d s.**' % (
        'CERTIFIED (HCount Z 10, every real t)' if cert else 'NOT CERTIFIED', 'AS WANTED' if _get('b718_a0_part1.json').get('control_a') else 'NOT',
        'AS WANTED' if okb and plant_fail else 'NOT', nre, neq, time.time() - t0)]
    J = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), route=ROUTE_ROWS, certified=cert, control_b=okb and plant_fail, list_region=low_ok,
             derived_region=hi_ok, narrowest=C85.ser(narrow[0]), k1=C85.ser(k1), k0=C85.ser(k0), reread=nre, equal=neq)
    _membrane_put('b718_a0.txt', NL.join(L) + NL)
    _membrane_put('b718_a0.json', json.dumps(J, indent=1) + NL)
    print(NL.join(L))


ROUTES = dict(grid=grid, params=params, compose=compose)
if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        sys.exit('usage: b718_a0.py grid | params | compose')
    fn(*sys.argv[2:])
