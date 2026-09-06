# -*- coding: utf-8 -*-
"""b340_diagnose.py -- THE DIAGNOSTIC OF THE SEALED REFINEMENT ROUTE. ### A READING BESIDE THE VERDICT, NOT A VERDICT.

### ### **WHAT THE RUN SHOWED.** ### The theta route (tanh-sinh on `4n + 4` panels) gives `I(n) + 1 = lambda_A(n)` to
### the working precision at every tabulated index, while the sealed refinement -- the `u` variable on panels at the
### phase multiples and the tail `[u_{n-1}, inf]` by Gauss-Legendre -- drifts from it by `1e-5` to `1e-3`, so the sealed
### gate (drift below the bar) refuses and the sealed verdict is THE DIFFERING CONSTITUENT, a quadrature failure.
### ### **WHAT THIS FILE ASKS:** where does the drift live? ### (i) the tail panel `[u_{n-1}, inf]` alone, by Gauss-Legendre
### as sealed and by tanh-sinh; (ii) the finite panels alone, by both rules; (iii) the whole `u` route by tanh-sinh (the
### same substitution, the other rule) against the theta route. ### If the drift is the tail panel's under the
### Gauss-Legendre rule and the `u` route by tanh-sinh meets the bar, the sealed refinement and not the identity is
### what failed. ### **THE BAR IS NOT MOVED; THE VERDICT AS SEALED STANDS; THIS IS A READING.**
"""
import io
import json
import os
import sys
import time

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b340_li_control as LC   # noqa: E402  ### the instrument's own functions, IMPORTED

D = os.path.join(ROOT, 'data')
RUN = os.path.join(D, 'b340_diagnose_run.txt')
OUT = os.path.join(D, 'b340_diagnose.json')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

INDICES_DIAG = (1, 6, 20, 60, 130)   # ### a spread of the keystone's indices; the whole run is the instrument's


def parts(n, method):
    with mp.workdps(LC.DPS_U):
        pts = [mp.tan(mp.pi * m / (2 * n)) / 2 for m in range(n)]
        f = lambda u: LC.reG_closed(n, u) * LC.h_plus(u)
        fin = mp.quad(f, pts, method=method) if n > 1 else mp.mpf(0)
        tail = mp.quad(f, [pts[-1], mp.inf], method=method)
        return fin / mp.pi, tail / mp.pi


def main():
    t0 = time.time()
    J = json.load(io.open(os.path.join(D, 'b340_control.json'), encoding='utf-8'))
    byn = {t['n']: t for t in J['table']}
    L = []

    def rec(s=''):
        L.append(s)
        print(s, flush=True)
    rec('=' * 100)
    rec('b340 -- THE DIAGNOSTIC OF THE SEALED REFINEMENT ROUTE. ### where the drift lives. ### A READING, NOT A VERDICT.')
    rec('=' * 100)
    rec('  %-4s %-14s %-14s %-14s %-14s %-12s %-12s %-12s' % ('n', 'finite (GL)', 'finite (TS)', 'tail (GL)', 'tail (TS)', 'u-TS vs theta', 'u-GL vs theta', 'bar'))
    out = {}
    ok_all = True
    for n in INDICES_DIAG:
        tn = time.time()
        fg, tg = parts(n, 'gauss-legendre')
        ft, tt = parts(n, 'tanh-sinh')
        with mp.workdps(40):
            ith = mp.mpf(byn[n]['I_theta'])
            bar = mp.mpf(byn[n]['bar'])
            d_ts = abs(ft + tt - ith)
            d_gl = abs(fg + tg - ith)
            tail_diff = abs(tg - tt)
            fin_diff = abs(fg - ft)
            meets = d_ts <= bar
            ok_all = ok_all and meets
            rec('  %-4d %-14s %-14s %-14s %-14s %-12.3e %-12.3e %-12.3e   tail GL-TS %.3e ; finite GL-TS %.3e ; u by tanh-sinh meets the bar : %s  (%.0f s)'
                % (n, mp.nstr(fg, 12), mp.nstr(ft, 12), mp.nstr(tg, 12), mp.nstr(tt, 12), d_ts, d_gl, bar, tail_diff, fin_diff, 'YES' if meets else 'NO', time.time() - tn))
            out[str(n)] = dict(finite_gl=mp.nstr(fg, 25), finite_ts=mp.nstr(ft, 25), tail_gl=mp.nstr(tg, 25), tail_ts=mp.nstr(tt, 25), u_ts_vs_theta=mp.nstr(d_ts, 3),
                               u_gl_vs_theta=mp.nstr(d_gl, 3), tail_gl_minus_ts=mp.nstr(tail_diff, 3), finite_gl_minus_ts=mp.nstr(fin_diff, 3), bar=mp.nstr(bar, 3), meets=bool(meets))
    tail_carries = all(mp.mpf(o['tail_gl_minus_ts']) > 10 * mp.mpf(o['finite_gl_minus_ts']) for o in out.values())
    rec('')
    rec('  ### THE DRIFT LIVES IN THE TAIL PANEL UNDER THE GAUSS-LEGENDRE RULE at every diagnosed index : %s' % tail_carries)
    rec('  ### THE u ROUTE BY TANH-SINH (the same substitution, the other rule) MEETS THE SEALED BAR AGAINST THE THETA ROUTE at every diagnosed index : %s' % ok_all)
    rec('  ### READING: %s' % ('the sealed refinement route (Gauss-Legendre on an infinite panel with a logarithmic tail) is what failed, and not the identity; the bar as sealed is NOT MET and is not rewritten.'
                              if (tail_carries and ok_all) else 'the drift is not confined to the tail panel, or the tanh-sinh u route does not meet the bar; the reading is withheld.'))
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)
    io.open(RUN, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(dict(indices=list(INDICES_DIAG), parts=out, tail_carries=bool(tail_carries), u_ts_meets_bar=bool(ok_all)), indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
