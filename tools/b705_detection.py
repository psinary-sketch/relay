# -*- coding: utf-8 -*-
"""b705_detection.py -- THE DETECTION LAW OVER THE SEVENTEEN OFF-LINE PAIRS, (R315)(7)(i), AS data/b703_registrations.txt (ii) REGISTERED IT
(:21-:31, committed alone at relay b8a36309, unchanged): nothing added to the registration after its commit.

### THE QUANTITY: for an off-line zero rho = beta + i t with beta > 1/2, r(rho) = log |1 - 1/(1 - beta + i t)| -- the log-modulus of the
### reflected point's z = 1 - 1/rho', rho' = 1 - conj rho, the dominant modulus R of the pair -- which is (2 beta - 1)/(2 t^2) to leading order.
### For each off-line pair, n*(rho) by b675's route (tools/b675_li_bench.py constants_for :163, onset :153, IMPORTED unedited) on the
### configuration of Q0's certified on-line zeros (the 146 ON rows, each a conjugate pair of weight 2) with P3's tail (K_tail under T-COUNT,
### A0 = 10, b675's KMAX) and THAT PAIR ALONE (rho and its reflection 1 - conj rho; the sixteen other orbits removed): n* the least n at which
### the v0.32 bound's expression SUM_D m - c R^n + C (n + 1)^2 s^n is certified below 0 -- the least n at which the coefficient is negative
### under the bound, b675's n*.
### THE PREDICTION (the registration's hypothesis): n*(rho) = L0 / r(rho) within the factor range [0.67, 1.5], L0 calibrated at rho0 as
### r(rho0) x n*(rho0). THE FALSIFIER: any pair's n* outside the range -- any pair with n*/predicted outside [0.67, 1.5].
### THE CONTROLS, printed BEFORE the figures: (C1) the configuration at rho0 computed by b675's route -- b675's own call, constants_for over
### the whole 180-representative configuration with dom = ref0 -- reproducing b675's figure n* = 63676 (data/b675_li_constants.json bench,
### data/b675_li_bench.txt :6); (C2) zeta's coefficients nonnegative through the largest predicted n*: P_n over zeta's first 146 zeros (acb
### zeta_zero, on the line) read at the grid 1, 10, ..., and at every predicted n*, NONNEGATIVE -- by algebra, 2(1 - cos n theta) >= 0 for a
### point on the line, so this control reads the INSTRUMENT'S sign where no off-line zero stands, not the object: VACUOUS as a test of the
### law, a control of the reader.
### THE REACH: b675's rule (the plan's section 2 (i)) needs every rest modulus below r = (1 + R)/2, the uncertified points' bound
### sqrt(1 + 2/T0^2) among them; a pair whose R stands at or below that bound is BEYOND the route's reach and entered "beyond reach: the
### rule's modulus condition fails (unc >= r)"; a pair whose onset is not found below b675's cap (onset :153, cap 2,000,000) is entered
### "beyond reach at n = 2000000", the bound, not estimated.
### THE TAIL'S CONTOUR: P3's count law over N_Q's strip -1/2 < Re rho < 3/2 (data/b705_contour.txt, both ranges enclosing every zero of
### Lambda_Q); the tail enters n* through K_tail as b675's route has it (T-COUNT, A0 = 10).
### Routes (each its own foreground call): `controls` -> data/b705_detection_controls.txt ; `pairs <i> <j>` -> the pairs i..j computed, one
### unit per pair appended to data/b705_detection_units.jsonl (untracked, resumable) ; `bank` -> data/b705_detection.txt, data/b705_detection.json.gz
### beside data/b705_detection_hashes.txt (data/b680_rules.txt row (1)). Written by the Write tool at b705; it writes only the banks it names.
"""
import gzip
import hashlib
import io
import json
import math
import os
import sys
import time

from flint import acb, arb, ctx

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b675_li_bench as B   # noqa: E402  ### b675's route, imported unedited (reps, terms, constants_for, onset, P)

ACT = 'b705'
ctx.prec = B.PREC
UNITS = os.path.join(D, '%s_detection_units.jsonl' % ACT)
RANGE = (arb('0.67'), arb('1.5'))     # ### data/b703_registrations.txt :25
B675_NSTAR = 63676                    # ### data/b675_li_bench.txt :6 ; data/b675_li_constants.json bench.n_star
ZETA_ZEROS = 146                      # ### zeta's control configuration: as many zeros as Q0's on-line rows


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def s_(x, d=20):
    return x.str(d, radius=True)


def put_txt(name, L):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def units():
    U = {}
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[u['idx']] = u
    return U


def put_unit(u):
    with open(UNITS, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


def rows_all():
    """b675's representatives: the 146 ON rows and, per off-line row, (off<idx>, ref<idx>) -- 180 in all, read through b671's hashes."""
    return B.reps()


def pair_rows(R0, idx):
    """the configuration of (R315)(7)(i): every ON row and the one pair off<idx>, ref<idx>."""
    return [x for x in R0 if x[0].startswith('on') or x[0] in ('off%d' % idx, 'ref%d' % idx)]


def r_of(sig, t):
    """r(rho) = log |1 - 1/(1 - beta + i t)|: the reflected point's log-modulus."""
    rho_ref = acb(1 - sig, t)
    return abs(1 - 1 / rho_ref).log()


def leading(sig, t):
    return (2 * sig - 1) / (2 * t * t)


def controls(*a):
    t0 = time.time()
    R0 = rows_all()
    T0 = B.terms(R0)
    c0 = B.constants_for(T0, 'ref0')
    n0 = c0['n_star']
    t1 = time.time()
    # ### C2: zeta's P_n over its first 146 zeros, on the line, at the grid and at the largest predicted n* (filled at `bank` from the units; here the grid)
    Z = [('z%d' % k, arb('0.5'), acb.zeta_zero(k).imag) for k in range(1, ZETA_ZEROS + 1)]
    TZ = B.terms(Z)
    grid = [1, 10, 100, 1000, 10000, 63676, 100000, 1000000, 2000000]
    zs = [(n, B.P(TZ, n)) for n in grid]
    neg = [n for n, p in zs if p < 0]
    t2 = time.time()
    L = ['%s -- (R315)(7)(i): THE DETECTION LAW`S CONTROLS, PRINTED BEFORE ANY PAIR`S FIGURE (%s)' % (ACT, utc()), '',
         '### (C1) the configuration at rho0 by b675`s route: tools/b675_li_bench.py constants_for (:163) over the whole configuration (180',
         '### representatives, the 146 ON rows and the seventeen off-line orbits` pairs, read through b671`s hashes) with dom = ref0, as b675`s part1',
         '### called it; its n* against b675`s figure (data/b675_li_bench.txt :6 ; data/b675_li_constants.json bench.n_star = %d).' % B675_NSTAR,
         '  n* %s ; b675`s %d ; EQUAL %s ; R %s ; s %s ; ln(R/s) %s ; %d s' % (n0, B675_NSTAR, n0 == B675_NSTAR, c0['R'], c0['s'], c0['ln_R_over_s'], int(t1 - t0)),
         '  r(rho0) = log|1 - 1/(1 - beta0 + i t0)| = %s (the leading term (2 beta0 - 1)/(2 t0^2) = %s) ; L0 = r(rho0) x n*(rho0) = %s' % (
             s_(r_of(R0[0][1] if R0[0][0] == 'off0' else [x for x in R0 if x[0] == 'off0'][0][1], [x for x in R0 if x[0] == 'off0'][0][2])),
             s_(leading([x for x in R0 if x[0] == 'off0'][0][1], [x for x in R0 if x[0] == 'off0'][0][2])),
             s_(r_of([x for x in R0 if x[0] == 'off0'][0][1], [x for x in R0 if x[0] == 'off0'][0][2]) * n0)), '',
         '### (C2) zeta`s coefficients nonnegative: P_n over zeta`s first %d zeros (acb.zeta_zero, each on the line, weight 2) at the grid; the' % ZETA_ZEROS,
         '### largest predicted n* read at `bank` from the pairs. By algebra 2(1 - cos n theta) >= 0 for a point on the line, so a NONNEGATIVE reading',
         '### is VACUOUS as a test of the law: it reads the instrument`s sign where no off-line zero stands. Rows are n | P_n | the sign.']
    L += ['  %8d  %-44s %s' % (n, s_(p, 15), 'NEG' if p < 0 else 'NONNEG') for n, p in zs]
    L += ['  %d s' % int(t2 - t1), '',
          '### ### **C1: n*(rho0) BY b675`S ROUTE %s AGAINST b675`S %d, EQUAL %s ; C2: ZETA P_n NONNEGATIVE AT EVERY GRID n %s (VACUOUS BY ALGEBRA, THE INSTRUMENT`S SIGN).**' % (
              n0, B675_NSTAR, n0 == B675_NSTAR, not neg)]
    put_txt('%s_detection_controls.txt' % ACT, L)
    put_unit(dict(idx='C1', n_star=n0, b675=B675_NSTAR, equal=n0 == B675_NSTAR, R=c0['R'], s=c0['s'], ln_R_over_s=c0['ln_R_over_s'],
                  r0=s_(r_of([x for x in R0 if x[0] == 'off0'][0][1], [x for x in R0 if x[0] == 'off0'][0][2]), 30),
                  L0=s_(r_of([x for x in R0 if x[0] == 'off0'][0][1], [x for x in R0 if x[0] == 'off0'][0][2]) * n0, 30), seconds=int(t1 - t0)))
    put_unit(dict(idx='C2', grid=[(n, s_(p, 15), 'NEG' if p < 0 else 'NONNEG') for n, p in zs], seconds=int(t2 - t1)))
    print(NL.join(L[3:6] + L[-1:]))


def pairs(*a):
    """`pairs <i> <j>`: the pairs idx i..j (0-16), each one unit: r(rho), the configuration on<all> + the pair, constants_for with dom = ref<idx>
    (the rest the ON rows alone), n* or the reach it exceeds."""
    i, j = int(a[0]), int(a[1])
    R0 = rows_all()
    U = units()
    for idx in range(i, j + 1):
        if idx in U:
            print('  pair %d: banked already' % idx)
            continue
        t0 = time.time()
        off = [x for x in R0 if x[0] == 'off%d' % idx][0]
        sig, t = off[1], off[2]
        r = r_of(sig, t)
        rows = pair_rows(R0, idx)
        T = B.terms(rows)
        u = dict(idx=idx, re=s_(sig, 25), im=s_(t, 25), r=s_(r, 30), r_leading=s_(leading(sig, t), 30), points=2 * len(rows), n_star=None, reach=None)
        try:
            c = B.constants_for(T, 'ref%d' % idx)
            u.update(n_star=c['n_star'], R=c['R'], s=c['s'], ln_R_over_s=c['ln_R_over_s'], K=c['K'], C=c['C'], next_modulus=c['next_modulus'],
                     below_r=c['every_rest_modulus_below_r'])
            if c['n_star'] is None:
                u['reach'] = 'beyond reach at n = 2000000 (b675`s onset cap, tools/b675_li_bench.py :153)'
        except SystemExit as e:
            z = (1 - 1 / acb(1 - sig, t))
            R_ = abs(z)
            rr = (1 + R_) / 2
            unc = (1 + arb(2) / (B.T0 * B.T0)).sqrt()
            u.update(R=s_(R_, 25), r_rule=s_(rr, 25), unc=s_(unc, 15),
                     reach='beyond reach: b675`s rule (every rest modulus below r = (1 + R)/2) fails at this pair -- the uncertified modulus bound %s >= r %s (%s)' % (
                         s_(unc, 12), s_(rr, 12), str(e)[:80]))
        u['seconds'] = int(time.time() - t0)
        put_unit(u)
        print('  pair %2d  rho = %s + %s i  r %s  n* %s  %s  %d s' % (idx, u['re'][:14], u['im'][:14], u['r'][:16], u['n_star'], (u['reach'] or '')[:70], u['seconds']))


def bank(*a):
    U = units()
    c1 = U.get('C1')
    if not c1 or not all(k in U for k in range(17)):
        sys.exit('### THE CONTROLS OR A PAIR IS NOT BANKED -- NOTHING WRITTEN (have %s)' % sorted(U))
    L0 = arb(c1['L0'].strip('[]').split(' +/-')[0])
    rows = []
    for idx in range(17):
        u = U[idx]
        r = arb(u['r'].strip('[]').split(' +/-')[0])
        pred = L0 / r
        ratio = (arb(u['n_star']) / pred) if u['n_star'] else None
        inside = (ratio is not None) and bool(ratio >= RANGE[0]) and bool(ratio <= RANGE[1])
        rows.append((idx, u, pred, ratio, inside))
    computed = [x for x in rows if x[3] is not None]
    beyond = [x for x in rows if x[3] is None]
    refuted = [x for x in computed if not x[4]]
    largest_pred = max(float(x[2].mid()) for x in rows)
    # ### C2 at the largest predicted n*: zeta`s P_n there (and the grid, from the control unit)
    Z = [('z%d' % k, arb('0.5'), acb.zeta_zero(k).imag) for k in range(1, ZETA_ZEROS + 1)]
    TZ = B.terms(Z)
    nmax = int(math.ceil(largest_pred))
    pz = B.P(TZ, nmax)
    c2 = U.get('C2') or {}
    c2_ok = all(s == 'NONNEG' for _n, _p, s in (c2.get('grid') or [])) and not (pz < 0)
    L = ['%s -- (R315)(7)(i): THE DETECTION LAW OVER THE SEVENTEEN OFF-LINE PAIRS, AS data/b703_registrations.txt (ii) REGISTERED IT (%s)' % (ACT, utc()), '',
         '### rows are off-line pairs (b681`s certified off-line zeros, idx 0-16, through b671`s hashes): idx | rho | r(rho) = log|1 - 1/(1 - beta + i t)|',
         '### (its leading term beside) | n*(rho) by b675`s route on the ON rows with that pair alone and P3`s tail (T-COUNT, A0 = 10) | the',
         '### prediction L0 / r(rho), L0 = r(rho0) x n*(rho0) = %s (C1) | n*/predicted | within [0.67, 1.5]. A pair beyond the route`s reach carries' % c1['L0'][:30],
         '### its reach and no estimate. The tail`s contour: P3`s count law over N_Q`s strip -1/2 < Re rho < 3/2 (data/b705_contour.txt).',
         '### The controls (data/b705_detection_controls.txt): C1 n*(rho0) = %s against b675`s %d, equal %s ; C2 zeta nonnegative through the largest' % (c1['n_star'], c1['b675'], c1['equal']),
         '### predicted n* (%d): P_%d = %s %s (VACUOUS by algebra, the instrument`s sign).' % (nmax, nmax, s_(pz, 12), 'NONNEG' if not (pz < 0) else '### NEG'), '']
    for idx, u, pred, ratio, inside in rows:
        L.append('  %2d | %s + %s i | r %s (leading %s) | n* %s | predicted %s | n*/predicted %s | %s' % (
            idx, u['re'][:22], u['im'][:22], u['r'][:18], u['r_leading'][:14], u['n_star'] if u['n_star'] else '-', s_(pred, 10),
            s_(ratio, 8) if ratio is not None else '-', ('WITHIN' if inside else '### OUTSIDE') if ratio is not None else u['reach']))
    L += ['', '### THE FALSIFIER (any pair`s n* outside [0.67, 1.5]): pairs computed %d, within %d, outside %d %s ; beyond reach %d %s' % (
        len(computed), len(computed) - len(refuted), len(refuted), [x[0] for x in refuted] or '', len(beyond), [x[0] for x in beyond] or ''),
          '### THE REGISTRATION`S HYPOTHESIS: %s over the pairs computed ; NOT SCORABLE over the pairs beyond reach' % ('HELD' if computed and not refuted else ('REFUTED' if refuted else 'NOT SCORABLE')),
          '', '### ### **PAIRS 17 ; COMPUTED %d, WITHIN [0.67, 1.5] %d, OUTSIDE %d ; BEYOND REACH %d ; THE FALSIFIER %s ; C1 EQUAL %s ; C2 NONNEGATIVE %s (VACUOUS).**' % (
              len(computed), len(computed) - len(refuted), len(refuted), len(beyond), 'REFUTED' if refuted else ('HELD' if computed else 'NOT SCORABLE'), c1['equal'], c2_ok)]
    put_txt('%s_detection.txt' % ACT, L)
    J = dict(at=utc(), L0=c1['L0'], range=['0.67', '1.5'], controls=dict(C1=c1, C2=dict(c2, at_largest=[nmax, s_(pz, 15), 'NONNEG' if not (pz < 0) else 'NEG'])),
             rows=[dict(idx=i_, re=u['re'], im=u['im'], r=u['r'], n_star=u['n_star'], predicted=s_(p, 30), ratio=s_(q, 30) if q is not None else None, within=w, reach=u['reach'])
                   for i_, u, p, q, w in rows],
             verdict='REFUTED' if refuted else ('HELD' if computed else 'NOT SCORABLE'), computed=len(computed), outside=[x[0] for x in refuted], beyond=[x[0] for x in beyond])
    gz = os.path.join(D, '%s_detection.json.gz' % ACT)
    raw = (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    with open(gz + '.tmp', 'wb') as fh:
        fh.write(gzip.compress(raw, 9, mtime=0))
    os.replace(gz + '.tmp', gz)
    gzb = open(gz, 'rb').read()
    put_txt('%s_detection_hashes.txt' % ACT, ['%s -- THE DETECTION LAW`S BINARY BANK, ITS HASHES (data/b680_rules.txt row (1)) (%s)' % (ACT, utc()), '',
                                               '### rows: path ; sha256 ; bytes, LF (the json inside the gz and the gz itself)',
                                               'data/%s_detection.json.gz ; %s ; %d' % (ACT, hashlib.sha256(gzb).hexdigest(), len(gzb)),
                                               'data/%s_detection.json (inside the gz) ; %s ; %d' % (ACT, hashlib.sha256(raw).hexdigest(), len(raw))])
    print(NL.join(L[7:]))


ROUTES = dict(controls=controls, pairs=pairs, bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b705_detection.py controls | pairs <i> <j> | bank')
        sys.exit(2)
    fn(*sys.argv[2:])
