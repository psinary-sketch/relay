# -*- coding: utf-8 -*-
"""b341_coefficients.py -- THE TWO COEFFICIENTS BY TWO ROUTES, THE LOCATED LITERATURE BESIDE THEM, AND THE DECISION BY
### THE SEALED RULE (registration (C), (D)).

### ### **ROUTE (A)** the bench's own definitions executed from its file through b327's loader (imported): `lambda_n =
### lambda_A(n) + lambda_Z(n)` at the bench's two radii, `M = 512`, the bench's `dps 260`. ### **ROUTE (B)** the Li map
### applied to `log xi(s)` by mpmath's Taylor differentiation at `s = 1` (`mp.taylor`), `dps 60` -- no quadrature shared
### with (A). ### **THE RULE:** at `n = 3, 5`, the emitter whose value differs from the two agreeing routes by more than
### `1e-9` carries a transcription defect; the located literature is the third witness. ### The bench's dictionary and
### the keystone's column are read from their files at their lines, never retyped.
"""
import io
import json
import os
import re
import sys
import time
from math import comb

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_bridge as BR   # noqa: E402  ### load_bench_definitions -- IMPORTED, never edited

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
KEY = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
BENCH = os.path.join(PP, 'internal', 'bench', 'li_bench.py')
RUN = os.path.join(D, 'b341_coefficients_run.txt')
OUT = os.path.join(D, 'b341_coefficients.json')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BAR_ROUTES = mp.mpf('1e-12')
BAR_DEFECT = mp.mpf('1e-9')
NMAX = 5
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def read_bench_dict():
    src = io.open(BENCH, encoding='utf-8').read().splitlines()
    for i, ln in enumerate(src):
        m = re.match(r'^KEIPER = (\{.*\})\s*$', ln)
        if m:
            return eval(m.group(1)), i + 1
    raise RuntimeError('the bench carries no KEIPER dictionary line')


def read_keystone_table():
    txt = io.open(KEY, encoding='utf-8').read().splitlines()
    head = '| n | computed \u03bb_n | literature | absdiff |'
    i = txt.index(head)
    rows = {}
    for k, ln in enumerate(txt[i + 2:]):
        if not ln.startswith('|'):
            break
        c = [x.strip() for x in ln.strip().strip('|').split('|')]
        rows[int(c[0])] = dict(computed=c[1], literature=c[2], absdiff=c[3], line=i + 3 + k)
    return rows, i + 1


def route_b(nmax):
    """### the Li map of log xi at s = 1 by Taylor differentiation: eta_j = the j-th Taylor coefficient; lambda_n = n SUM C(n-1,j-1) eta_j."""
    with mp.workdps(60):
        def logxi(s):
            # ### (s - 1) zeta(s) -> 1 at s = 1 (a removable point); mp.taylor's stencil evaluates AT s = 1, where mp.zeta raises
            # ### on the pole -- the first run stopped there. The value at the point is exact, log 1 = 0, and the function is analytic.
            fz = mp.mpf(0) if s == 1 else mp.log((s - 1) * mp.zeta(s))
            return mp.log(s) + mp.loggamma(s / 2) - (s / 2) * mp.log(mp.pi) + fz
        eta = mp.taylor(logxi, 1, nmax)          # ### eta[0] the constant, eta[j] the coefficient of (s-1)^j
        lam = {}
        for n in range(1, nmax + 1):
            lam[n] = n * sum(comb(n - 1, j - 1) * eta[j] for j in range(1, n + 1))
        return lam


def main():
    t0 = time.time()
    rec('=' * 100)
    rec('b341 -- THE TWO COEFFICIENTS BY TWO ROUTES, THE LITERATURE BESIDE THEM, THE DECISION BY THE SEALED RULE.')
    rec('=' * 100)
    dct, dline = read_bench_dict()
    krows, khead = read_keystone_table()
    rec('  the bench\'s dictionary, read from %s line %d : %s' % (os.path.basename(BENCH), dline, dct))
    rec('  the keystone\'s validation table, read from its line %d : %s' % (khead, {n: r['literature'] for n, r in krows.items()}))
    rec('')
    rec('  ROUTE (A) -- the bench\'s definitions from its file (b327_bridge.load_bench_definitions), two radii, M = 512:')
    ns, nhead, _k = BR.load_bench_definitions()
    tA = time.time()
    lamA, lamZ = {}, {}
    for r in BR.RADII:
        lamA[r] = ns['lambdas'](ns['taylor_coeffs'](ns['f_A'], r, 512, NMAX), NMAX)
        lamZ[r] = ns['lambdas'](ns['taylor_coeffs'](ns['f_Z'], r, 512, NMAX), NMAX)
    r0, r1 = BR.RADII
    A = {n: lamA[r0][n] + lamZ[r0][n] for n in range(1, NMAX + 1)}
    A1 = {n: lamA[r1][n] + lamZ[r1][n] for n in range(1, NMAX + 1)}
    rec('    dps %d ; %.0f s ; the two radii agree to %s' % (mp.mp.dps, time.time() - tA, mp.nstr(max(abs(A[n] - A1[n]) for n in A), 3)))
    rec('  ROUTE (B) -- mp.taylor of log xi at s = 1, dps 60:')
    tB = time.time()
    B = route_b(NMAX)
    rec('    %.0f s' % (time.time() - tB))
    rec('')
    rec('    %-3s %-24s %-24s %-10s %-20s %-18s %-12s' % ('n', 'route A', 'route B', '|A - B|', "the bench's dict", "the keystone's lit.", 'agree?'))
    table = {}
    routes_ok = True
    with mp.workdps(40):
        for n in range(1, NMAX + 1):
            dAB = abs(A[n] - B[n])
            routes_ok = routes_ok and dAB <= BAR_ROUTES
            bd = mp.mpf(dct[n]) if n in dct else None
            kl = mp.mpf(krows[n]['literature']) if n in krows else None
            d_b = abs(bd - A[n]) if bd is not None else None
            d_k = abs(kl - A[n]) if kl is not None else None
            table[n] = dict(A=mp.nstr(A[n], 22), B=mp.nstr(B[n], 22), dAB=mp.nstr(dAB, 3), bench=dct.get(n), keystone=krows.get(n, {}).get('literature'),
                            bench_off=mp.nstr(d_b, 3) if d_b is not None else None, keystone_off=mp.nstr(d_k, 3) if d_k is not None else None,
                            bench_defect=bool(d_b is not None and d_b > BAR_DEFECT), keystone_defect=bool(d_k is not None and d_k > BAR_DEFECT))
            rec('    %-3d %-24s %-24s %-10s %-20s %-18s %-12s' % (n, mp.nstr(A[n], 20), mp.nstr(B[n], 20), mp.nstr(dAB, 3), dct.get(n), krows.get(n, {}).get('literature'), 'YES' if dAB <= BAR_ROUTES else '### NO'))
    rec('    the two routes agree at n = 1..%d within %s : %s' % (NMAX, mp.nstr(BAR_ROUTES, 2), routes_ok))
    rec('')
    rec("  THE TWO EMITTERS AGAINST THE ROUTES (bar %s):" % mp.nstr(BAR_DEFECT, 2))
    for n in (3, 5):
        t = table[n]
        rec("    n = %d : the bench's %-16s off by %-10s -> %s ; the keystone's %-18s off by %-10s -> %s"
            % (n, t['bench'], t['bench_off'], 'DEFECT' if t['bench_defect'] else 'agrees', t['keystone'], t['keystone_off'], 'DEFECT' if t['keystone_defect'] else 'agrees'))
    # ### the literature, from the locate record
    L = json.load(io.open(os.path.join(D, 'b341_locate.json'), encoding='utf-8'))
    rec('')
    rec('  THE LOCATED LITERATURE (from b341_locate.json), the third witness:')
    lit = {}
    for n in (3, 5):
        found = []
        for sid, s in L['sources'].items():
            if not s.get('read'):
                rec('    n = %d : %s NOT READ (%s)' % (n, sid, s.get('reason', 'no PDF')))
                continue
            hs = s['hits'].get(str(n), [])
            if not hs:
                rec('    n = %d : %s read, NOT LOCATED (no string matches either candidate)' % (n, sid))
            for h in hs:
                found.append((sid, h['agrees_with'], h['string'], h['line'], s['sha256']))
                rec("    n = %d : %s LOCATED at line %d, %r under %s -- agrees with the %s's value" % (n, sid, h['line'], h['string'], h['normalization'], h['agrees_with']))
        lit[n] = found
    rec('')
    rec('  READINGS BESIDE THE RULE (labelled; NOT LOCATED under the sealed eight-digit decimal-string rule):')
    beside = {3: [], 5: []}
    for sid, s in L['sources'].items():
        for n in (3, 5):
            for b in (s.get('beside') or {}).get(str(n), []):
                beside[n].append(dict(source=sid, **b))
                rec("    n = %d : %s line %d, %s -- agrees with the %s's value ; %s" % (n, sid, b['line'], b['kind'], b['agrees_with'], b['context'][:90]))
    # ### the decision by the sealed rule
    rec('')
    verdict, carrier = None, {}
    if not routes_ok:
        verdict = 'WITHHELD -- the two routes disagree'
    else:
        lit_dis = any(who == 'bench' and table[n]['bench_defect'] or who == 'keystone' and table[n]['keystone_defect'] for n in (3, 5) for (_s, who, _v, _l, _h) in lit[n])
        if lit_dis:
            verdict = 'WITHHELD -- a located source disagrees with the routes'
        else:
            for n in (3, 5):
                if table[n]['bench_defect'] and not table[n]['keystone_defect']:
                    carrier.setdefault('bench', []).append(n)
                elif table[n]['keystone_defect'] and not table[n]['bench_defect']:
                    carrier.setdefault('keystone', []).append(n)
                elif table[n]['bench_defect'] and table[n]['keystone_defect']:
                    carrier.setdefault('both', []).append(n)
            if list(carrier) == ['bench']:
                verdict = 'THE BENCH CARRIES THE DEFECT at n = %s' % carrier['bench']
            elif list(carrier) == ['keystone']:
                verdict = 'THE KEYSTONE CARRIES THE DEFECT at n = %s' % carrier['keystone']
            elif not carrier:
                verdict = 'WITHHELD -- neither emitter differs from the routes beyond the bar'
            else:
                verdict = 'BOTH -- %s' % carrier
    lit_agree = {n: [(s, who) for (s, who, _v, _l, _h) in lit[n]] for n in (3, 5)}
    lit_status = {n: ('LOCATED, AGREES' if lit[n] and all(who == 'keystone' for (_s, who, _v, _l, _h) in lit[n]) and not table[n]['keystone_defect'] else ('LOCATED, DISAGREES' if lit[n] else 'NOT READ')) for n in (3, 5)}
    rec('  ### ### **VERDICT BY THE SEALED RULE : %s.** ### the literature: n = 3 %s ; n = 5 %s' % (verdict, lit_status[3], lit_status[5]))
    rec('  ### NO OWNER FILE EDITED ; the dictionary enters no computation ; no grade moved.')
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)
    run_path, k = RUN, 1
    while os.path.exists(run_path):
        k += 1
        run_path = RUN.replace('_run.txt', '_run%d.txt' % k)
    io.open(run_path, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(dict(table={str(k): v for k, v in table.items()}, routes_ok=bool(routes_ok), verdict=verdict, carrier=carrier, beside={str(k): v for k, v in beside.items()}, run_file=os.path.basename(run_path),
                                                                              lit_status={str(k): v for k, v in lit_status.items()}, lit={str(k): v for k, v in lit.items()},
                                                                              bench_line=dline, keystone_head_line=khead, keystone_rows={str(k): v for k, v in krows.items()},
                                                                              radii_worst=mp.nstr(max(abs(A[n] - A1[n]) for n in A), 3), names_carrier=bool(verdict and not verdict.startswith('WITHHELD') and not verdict.startswith('BOTH'))), indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
