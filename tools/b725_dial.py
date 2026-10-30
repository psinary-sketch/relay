# -*- coding: utf-8 -*-
"""b725_dial.py -- H-DIAL AT c = 0.6, 0.8, 1.0, (R335)(4)(ii) WITH (R335)(8)'s BUDGET, AS data/b725_registrations.txt (ii) REGISTERED IT
(relay 22210d4b) AND THE SEAT'S READING OF ITS BUILD (relay 2531aad5, committed alone before any figure at F_c).

### UNTRACKED WRITE: data/b725_dial_units.jsonl (one unit per (route, c, kind, point), appended as each lands, resumable).
### G_c(s) = zeta(s + c/2) zeta(s - c/2) on b707's template at zeta's lowest ordinate; S = P - PR + A on span{C, N}:
###   P   = SUM of k^ at z = -+ i(1/2 + c/2), -+ i(1/2 - c/2) (the four poles, with multiplicity);
###   PR  = b694's prime_sum / b709's prime_sum709 (imported unedited) with Lambda_G(n) = Lambda(n)(n^(c/2) + n^(-c/2));
###   A   = (1/pi) INT_0^4000 k^(r) B_c(r) dr + the tail ball, B_c = SUM_{delta = +-c/2} [(psi(u+1+iz/2) + psi(u+1-iz/2))/2 - u/(u^2 + z^2/4)
###         - log pi], u = 1/4 + delta/2; the tail ball b696's closed form with alpha = 2, beta = 2 log(pi/2) + 2/R + (43/3)/R^2.
### The form and its reading: tools/b707_onset.py gram and reading (imported unedited). The ladder b707's; the fine grid b709's.
### Routes (each its own foreground call):
###   tails               the two tail balls at the control window, each c, with their derivations' constants
###   c0                  (c0): at c = 0 every term twice b707's zeta unit (rho0's window, rung 32, C, N, CN)
###   identity            (id): at c = 0.6, 0.8, 1.0, window C of rung 32 at zeta's lowest ordinate, the prime side against the zero side
###   price               b723's dial price beside this act's measured seconds per term
###   run <c> [--workers n] [--budget s]   the onset at c (call again until THE ONSET or BEYOND REACH)
###   bank                data/b725_dial.txt
### Written by the Write tool at b725; it writes its units file and data/b725_dial.txt and nothing else. Every value a ball at 128 bits.
### Nothing here proves RH or GRH.
"""
import io
import json
import math
import os
import sys
import time
from multiprocessing import Pool

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b709_grid as G9            # noqa: E402  ### b709's grid, window and prime_sum709: imported unedited
import b707_onset as O7           # noqa: E402  ### b707's ladder, window, nmax_of, gram and reading: imported unedited
from flint import acb, arb, ctx, fmpq   # noqa: E402

W, WB = O7.W, O7.WB
bs, bl, fmt = WB.bs, WB.bl, WB.fmt
ctx.prec = O7.PREC
UNITS = os.path.join(D, 'b725_dial_units.jsonl')
BANK = os.path.join(D, 'b725_dial.txt')
CS = ('0.6', '0.8', '1.0')
R_INT = O7.R_INT
T0 = '151.59'                     # ### b696's T0 (tools/b696_witness_balls.py :46)
LADDER = [r for r, _w in O7.RUNGS]
WIDTH = dict(O7.RUNGS)
TOP = 2 * math.log(192)
HOLD_MB, PER_WORKER_MB = 2560, 250
POS, NEG = 'POSITIVE DEFINITE BEYOND ITS BOUND', 'NEGATIVE DIRECTION BEYOND ITS BOUND'
SPREAD = 0.10


def _g1():
    ctx.prec = O7.PREC
    return acb.zeta_zero(1).imag.mid().str(30, radius=False)


G1 = _g1()                        # ### zeta's lowest ordinate, the template's frequency


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def free_mb():
    import ctypes

    class MS(ctypes.Structure):
        _fields_ = [('dwLength', ctypes.c_ulong), ('dwMemoryLoad', ctypes.c_ulong), ('ullTotalPhys', ctypes.c_ulonglong),
                    ('ullAvailPhys', ctypes.c_ulonglong), ('ullTotalPageFile', ctypes.c_ulonglong), ('ullAvailPageFile', ctypes.c_ulonglong),
                    ('ullTotalVirtual', ctypes.c_ulonglong), ('ullAvailVirtual', ctypes.c_ulonglong), ('ullAvailExtendedVirtual', ctypes.c_ulonglong)]
    m = MS()
    m.dwLength = ctypes.sizeof(MS)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return int(m.ullAvailPhys // (1024 * 1024))


def guard(where, workers):
    f = free_mb()
    need = HOLD_MB + PER_WORKER_MB * workers
    print('  free MB %d at %s ; the call needs %d (hold %d + %d workers x %d) -- %s' % (f, where, need, HOLD_MB, workers, PER_WORKER_MB,
                                                                                       'MET' if f >= need else 'REFUSED'), flush=True)
    if f < need:
        sys.exit('### FREE MEMORY BENEATH THE HOLD -- REFUSED (nothing computed after this line)')


def units():
    U = {}
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[(u['route'], u['c'], u['kind'], u['point'])] = u
    return U


def put_unit(u):
    u['at'] = utc()
    with open(UNITS, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


# ================================================================================ THE TERMS OF G_c
_LAM = {}


def lam_g(c, top):
    key = (c, top)
    if key not in _LAM:
        lz = W.lambda_z(top)
        h = arb(c) / 2
        _LAM[key] = [x if x.is_zero() else x * (arb(n) ** h + arb(n) ** (-h)) for n, x in enumerate(lz)]
    return _LAM[key]


def bracket_g(z, c):
    z = acb(z)
    I = acb(0, 1)
    tot = acb(0)
    for sg in (1, -1):
        u = arb(1) / 4 + sg * arb(c) / 4
        t = ((acb(u + 1) + I * z / 2).digamma() + (acb(u + 1) - I * z / 2).digamma()) / 2 - arb.pi().log()
        if not u.is_zero():
            t = t - acb(u) / (acb(u) * u + z * z / 4)
        tot += t
    return tot


def a_int_g(Wd, c, lo, hi):
    f = lambda z, an: Wd.khat(z) * bracket_g(z, c)   # noqa: E731
    tot = acb(0)
    for e in range(lo, hi, W.CHUNK):
        tot += acb.integral(f, e, e + W.CHUNK, rel_tol=arb(2) ** -110, abs_tol=arb(2) ** -110)
    return 2 * tot.real / (2 * arb.pi())


def arch_tail_g(Wd, R):
    """the seat's tail ball (registration (ii), the build's first): b696's closed form (:90-:107) with alpha = 2,
    beta = 2 log(pi/2) + 2/R + (43/3)/R^2."""
    R = arb(R)
    s, g0 = Wd.s, Wd.g0
    assert R > 2 * g0
    theta = 1 - g0 / R
    p = 8 if Wd.fam == 'N' else 12
    Kc = (2 / (theta * s)) ** 12
    alpha = arb(2)
    beta = 2 * (arb.pi() / 2).log() + 2 / R + (arb(43) / 3) / (R * R)
    q = arb(p - 1)
    return Kc * R ** (1 - p) * (alpha * (R.log() / q + 1 / (q * q)) + beta / q) / arb.pi()


def poles(Wd, c):
    h = arb(c) / 2
    tot = acb(0)
    for y in (arb(1) / 2 + h, arb(1) / 2 - h):
        tot += Wd.khat(acb(0, y)) + Wd.khat(acb(0, -y))
    return tot.real


def terms_g(Wd, c, PR, nmax, nterms, extra=None):
    t0 = time.time()
    P = poles(Wd, c)
    Ai = a_int_g(Wd, c, 0, R_INT)
    if (arb(1) / 4 - arb(c) / 4).is_zero():
        # ### registration (ii)'s amendment at c = 1.0: the Poisson kernel's limit, -k^(0) (the double pole on the line counted once)
        Ai = Ai - Wd.khat(acb(0)).real
    tl = arch_tail_g(Wd, R_INT)
    A = Ai + WB.unit_ball(tl)
    S = P - PR + A
    k0 = Wd.kval(arb(0), fmpq(0))
    u = dict(P=bs(P), PR=bs(PR), Aint=bs(Ai), tail=bs(tl), A=bs(A), S=bs(S), k0=bs(k0), nmax=nmax, prime_terms=nterms, R=R_INT,
             L=bs(Wd.L), a_radius=bs(2 * Wd.L), seconds=round(time.time() - t0, 1))
    u.update(extra or {})
    return u


def coarse_terms(c, rung, kind, g0=None):
    t0 = time.time()
    Wd = O7.window(kind, rung, g0 or G1)
    nmax = O7.nmax_of(Wd)
    if nmax >= 2:
        PR, nt, _ = W.prime_sum(Wd, lam_g(c, max(nmax, 2)), nmax)
    else:
        PR, nt = arb(0), 0
    u = terms_g(Wd, c, PR, nmax, nt)
    u['seconds'] = round(time.time() - t0, 1)
    return u


def register(fam, lo, hi):
    G9.FREQS[fam] = G1
    G9.INTERVAL[fam] = (WIDTH[lo], WIDTH[hi])
    G9.ENDPOINT_RUNG[fam] = (lo, hi)


def fine_terms(c, lo, hi, pt, kind):
    t0 = time.time()
    fam = 'dial' + c
    register(fam, lo, hi)
    Wd = G9._window(fam, pt, kind)
    N = pt['N']
    if N is None:
        N, nmax = 4, 1
    else:
        nmax = math.isqrt(N)
    if nmax >= 2:
        PR, nt, _ = G9.prime_sum709(Wd, N, lam_g(c, int(WIDTH[hi]) ** 2 if WIDTH[hi].isdigit() else nmax), nmax)
    else:
        PR, nt = arb(0), 0
    u = terms_g(Wd, c, PR, nmax, nt, dict(N=N, width=pt['width'][:24]))
    u['seconds'] = round(time.time() - t0, 1)
    return u


# ================================================================================ THE CONTROLS
def tails(*a):
    L = ['  THE ARCHIMEDEAN TAIL (the build`s first): alpha 2 ; beta 2 log(pi/2) + 2/R + (43/3)/R^2 = %s at R = %d' % (
        fmt(2 * (arb.pi() / 2).log() + 2 / arb(R_INT) + (arb(43) / 3) / (arb(R_INT) ** 2), 12), R_INT)]
    for kind in ('C', 'N'):
        Wd = O7.window(kind, '32', G1)
        L.append('  the ball at window %s, rung 32, gamma_0 %s: %s (b696`s zeta ball at the same window %s)' % (
            kind, G1[:12], fmt(arch_tail_g(Wd, R_INT), 6), fmt(WB.arch_tail(Wd, 'zeta', R_INT), 6)))
    Wd = O7.window('C', '32', G1)
    zt = WB.zero_tail(Wd, 'zeta', T0)[0]
    L.append('  THE ZERO-SIDE TAIL (the build`s second): 2 x b696`s zero_tail(window C rung 32, zeta, T0 = %s) = %s (|delta| <= 1/2 covers c/2)' % (T0, fmt(2 * zt, 6)))
    for l in L:
        print(l)
    put_unit(dict(route='tails', c='', kind='', point='', lines=L))


def c0(*a):
    guard('c0', 0)
    U7 = O7.units()
    ok_all = True
    L = []
    for kind in O7.KINDS:
        ref = next((u for (rt, fq, kd, rg, ob), u in U7.items() if fq == 'rho0' and kd == kind and rg == '32' and ob == 'zeta' and 'S' in u), None)
        if ref is None:
            ok_all = False
            L.append('  (c0) %s: NO b707 zeta unit at rho0 rung 32 -- NOT AS WANTED' % kind)
            continue
        u = coarse_terms('0', '32', kind, g0=O7.RHO0_IM)
        oks = []
        for k in ('P', 'PR', 'A', 'S'):
            oks.append(bl(u[k]).overlaps(2 * bl(ref[k])))
        ok = all(oks)
        ok_all &= ok
        L.append('  (c0) %-2s rho0 rung 32: S %s against 2 x b707`s %s ; P, PR, A, S each overlapping %s ; %.1f s -- %s' % (
            kind, fmt(bl(u['S']), 14), fmt(2 * bl(ref['S']), 14), oks, u['seconds'], 'AS WANTED' if ok else 'NOT AS WANTED'))
    L.append('### (c0) %s' % ('AS WANTED' if ok_all else 'NOT AS WANTED'))
    for l in L:
        print(l, flush=True)
    put_unit(dict(route='c0', c='0', kind='', point='', ok=bool(ok_all), lines=L))


def zeta_zeros_below(T0s):
    zs, n = [], 1
    T = arb(T0s)
    while True:
        g = acb.zeta_zero(n).imag
        if not (g < T):
            assert g > T, 'a zero ordinate meets T0'
            break
        zs.append(g)
        n += 1
    return zs


def identity(*a):
    guard('identity', 0)
    zs = zeta_zeros_below(T0)
    ok_all = True
    L = ['  (id) zeta`s ordinates below T0 = %s: %d (acb.zeta_zero(1..%d)), the last %s' % (T0, len(zs), len(zs), zs[-1].str(12))]
    for c in CS:
        u = coarse_terms(c, '32', 'C')
        Wd = O7.window('C', '32', G1)
        h = arb(c) / 2
        Z = acb(0)
        for g in zs:
            for gg in (g, -g):
                Z += Wd.khat(acb(gg, -h)) + Wd.khat(acb(gg, h))
        zt = WB.zero_tail(Wd, 'zeta', T0)[0]
        Zr = Z.real + WB.unit_ball(2 * zt)
        S = bl(u['S'])
        ok = S.overlaps(Zr) and Zr.rad() < abs(S.mid()) * arb('1e-6') and S.rad() < abs(S.mid()) * arb('1e-6')
        ok_all &= ok
        L.append('  (id) c = %s, window C rung 32 at %s: S (prime side) %s ; the zero side %s (its imaginary part %s ; tail %s) ; P %s, PR %s, A %s ; %.1f s -- %s' % (
            c, G1[:10], fmt(S, 14), fmt(Zr, 14), fmt(Z.imag, 3), fmt(2 * zt, 3), fmt(bl(u['P']), 8), fmt(bl(u['PR']), 8), fmt(bl(u['A']), 8),
            u['seconds'], 'AS WANTED' if ok else 'NOT AS WANTED'))
    L.append('### (id) %s' % ('AS WANTED' if ok_all else 'NOT AS WANTED'))
    for l in L:
        print(l, flush=True)
    put_unit(dict(route='identity', c='', kind='', point='', ok=bool(ok_all), lines=L))


def price(*a):
    print('PRICE: b723`s (data/b723_dial_price.txt :22-:25): up to about 1.7 h per c with four workers, 15-30 min where the onset falls low in its '
          'bracket; this act`s terms (the controls` lines carry their seconds) beside it.')


# ================================================================================ ONE c
def _coarse_task(args):
    c, rung, kind = args
    return args, coarse_terms(c, rung, kind)


def _fine_task(args):
    c, lo, hi, pt, kind = args
    return args, fine_terms(c, lo, hi, pt, kind)


def _form(U, route, c, point):
    us = dict((k, U.get((route, c, k, point))) for k in O7.KINDS)
    if any(v is None for v in us.values()):
        return None
    G, M = O7.gram(us['C'], us['N'], us['CN'])
    return O7.reading(G, M)


def run(c, *a):
    a = list(a)
    workers = int(a[a.index('--workers') + 1]) if '--workers' in a else 3
    budget = int(a[a.index('--budget') + 1]) if '--budget' in a else 540
    U = units()
    ok = [U.get(('c0', '0', '', '')), U.get(('identity', '', '', ''))]
    if not all(x and x.get('ok') for x in ok):
        sys.exit('### (c0) AND (id) NOT READ AS WANTED -- NO ONSET (the control before the figure)')
    guard('run c = %s' % c, workers)
    t0 = time.time()
    with Pool(workers) as pool:
        todo = [(c, r, k) for r in LADDER for k in O7.KINDS if ('coarse', c, k, r) not in U]
        for args, u in pool.imap_unordered(_coarse_task, todo):
            u.update(route='coarse', c=c, kind=args[2], point=args[1])
            put_unit(u)
            U[('coarse', c, args[2], args[1])] = u
        rq = dict((r, _form(U, 'coarse', c, r)) for r in LADDER)
        for r in LADDER:
            print('  c = %s coarse %-4s lambda_min %s | %s' % (c, r, fmt(bl(rq[r]['lmin']), 10), rq[r]['reading']), flush=True)
        negs = [r for r in LADDER if rq[r]['reading'] == NEG]
        if not negs:
            print('### c = %s: NO NEGATIVE DIRECTION ON b707`S LADDER TO 2 log 192 -- BEYOND REACH' % c)
            put_unit(dict(route='onset', c=c, kind='', point='', beyond=True, seconds=int(time.time() - t0)))
            return
        hi = negs[0]
        if hi == LADDER[0]:
            print('### c = %s: NEGATIVE AT a = log 2, THE LADDER`S FOOT' % c)
            put_unit(dict(route='onset', c=c, kind='', point='log2', foot=True, seconds=int(time.time() - t0)))
            return
        lo = LADDER[LADDER.index(hi) - 1]
        undec = [r for r in LADDER[:LADDER.index(hi)] if rq[r]['reading'] != POS]
        print('  c = %s THE COARSE BRACKET (%s, %s] ; rungs below it not POSITIVE: %s' % (c, lo, hi, undec or 'none'), flush=True)
        fam = 'dial' + c
        register(fam, lo, hi)
        pts = G9.grid(fam)
        inner = pts[1:]
        B = 4
        for j in range(0, len(inner), B):
            if time.time() - t0 > budget:
                print('### THE CALL`S BUDGET REACHED BEFORE POINT %d of %d -- CALL AGAIN TO RESUME' % (inner[j]['i'], len(pts) - 1))
                return
            if j % (B * 10) == 0:
                guard('c = %s point %d' % (c, inner[j]['i']), workers)
            batch = inner[j:j + B]
            todo = [(c, lo, hi, p, k) for p in batch for k in O7.KINDS if ('fine', c, k, p['name']) not in U]
            for args, u in pool.imap_unordered(_fine_task, todo):
                u.update(route='fine', c=c, kind=args[4], point=args[3]['name'], i=args[3]['i'])
                put_unit(u)
                U[('fine', c, args[4], args[3]['name'])] = u
            for p in batch:
                r = _form(U, 'fine', c, p['name'])
                a_p = U[('fine', c, 'C', p['name'])]['a_radius']
                if p['i'] % 40 == 1 or r['reading'] != POS:
                    print('  c = %s %4d %-16s a %s | lambda_min %s | %s' % (c, p['i'], p['name'], fmt(bl(a_p), 10), fmt(bl(r['lmin']), 10), r['reading']), flush=True)
                if r['reading'] == NEG:
                    print('### c = %s: THE ONSET at %s, a = %s ; (c/2) a* = %.6f' % (c, p['name'], fmt(bl(a_p), 10), float(c) / 2 * float(bl(a_p).mid())))
                    put_unit(dict(route='onset', c=c, kind='', point=p['name'], i=p['i'], a=a_p, lmin=r['lmin'], lo=lo, hi=hi, points=len(pts),
                                  seconds=int(time.time() - t0)))
                    return
        print('### c = %s: NO GRID POINT NEGATIVE IN (%s, %s] -- A DEFECT: the coarse rung %s read NEGATIVE' % (c, lo, hi, hi))


# ================================================================================ THE BANK
def bank(*a):
    U = units()
    L = ['b725 -- (R335)(4)(ii): H-DIAL AT c = 0.6, 0.8, 1.0 ON b707`S TEMPLATE AT ZETA`S LOWEST ORDINATE (%s)' % utc(), '',
         '### by tools/b725_dial.py; the registration data/b725_registrations.txt (ii) (relay 22210d4b) and the seat`s reading of the build (relay',
         '### 2531aad5), both committed before any figure at F_c. The frame G_c(s) = zeta(s + c/2) zeta(s - c/2); gamma_0 = %s.' % G1,
         '### Units: data/b725_dial_units.jsonl (untracked).', '']
    for key, title in ((('tails', '', '', ''), 'THE TWO TAIL BALLS'), (('c0', '0', '', ''), '(c0)'), (('identity', '', '', ''), '(id)')):
        runs = [json.loads(l) for l in io.open(UNITS, encoding='utf-8') if l.strip() and ('"route": "%s"' % key[0]) in l] if os.path.exists(UNITS) else []
        L.append('## %s' % title)
        if not runs:
            L.append('  NOT RUN')
        for i, r in enumerate(runs, 1):
            if len(runs) > 1:
                L.append('  ## RUN %d of %d at %s%s' % (i, len(runs), r.get('at'), ' (BEFORE THE AMENDMENT at c = 1.0; not the run read)' if i < len(runs) else ' (THE RUN READ)'))
            L += r.get('lines', [])
    L.append('')
    L.append('## THE ONSETS')
    prods, notrun, beyond = [], [], []
    for c in CS:
        o = next((u for k, u in U.items() if k[0] == 'onset' and k[1] == c), None)
        cz = [(r, _form(U, 'coarse', c, r)) for r in LADDER]
        L.append('  c = %s, the ladder: %s' % (c, ' ; '.join('%s %s' % (r, ('%s %s' % (fmt(bl(x['lmin']), 6), 'POS' if x['reading'] == POS else ('NEG' if x['reading'] == NEG else 'UND'))) if x else 'not run')
                                                    for r, x in cz)))
        if o is None:
            notrun.append(c)
            L.append('    NOT RUN')
            continue
        if o.get('beyond') or o.get('foot'):
            beyond.append(c)
            L.append('    %s' % ('BEYOND REACH: positive to 2 log 192 = %.6f; (c/2) a* > %.6f' % (TOP, float(c) / 2 * TOP) if o.get('beyond') else 'NEGATIVE AT THE LADDER`S FOOT'))
            continue
        a_on = float(bl(o['a']).mid())
        nu = [u for k, u in U.items() if k[0] in ('coarse', 'fine') and k[1] == c]
        prods.append((c, a_on, float(c) / 2 * a_on))
        L.append('    THE ONSET: %s (grid point %d of %d in (%s, %s]) at a = %s, lambda_min %s ; (c/2) a* = %.6f ; units %d, seconds summed %d' % (
            o['point'], o['i'], o['points'] - 1, o['lo'], o['hi'], fmt(bl(o['a']), 10), fmt(bl(o['lmin']), 10), float(c) / 2 * a_on, len(nu),
            sum(u.get('seconds', 0) for u in nu)))
    L.append('')
    if len(prods) == 3:
        m = sum(p for *_, p in prods) / 3
        spread = (max(p for *_, p in prods) - min(p for *_, p in prods)) / m
        verdict = 'REFUTED' if spread > SPREAD else 'HELD'
        L.append('THE PRODUCTS %s ; mean %.6f ; spread (max - min)/mean %.4f against 0.10 -- %s' % (['%.6f' % p for *_, p in prods], m, spread,
                                                                                                    'THE FALSIFIER FIRES' if spread > SPREAD else 'WITHIN'))
    else:
        verdict = 'NOT SCORABLE'
        L.append('FEWER THAN THREE PRODUCTS (%d): the spread is not read (the registration`s NOT SCORABLE) ; beyond reach %s ; not run %s' % (len(prods), beyond, notrun))
    L.append('THE HYPOTHESIS (HELD, REFUTED or NOT SCORABLE): %s' % verdict)
    L.append('')
    L.append('### ### **H-DIAL: (c0) %s ; (id) %s ; ONSETS %d OF 3 ; THE HYPOTHESIS %s.**' % (
        'AS WANTED' if (U.get(('c0', '0', '', '')) or {}).get('ok') else 'NOT AS WANTED',
        'AS WANTED' if (U.get(('identity', '', '', '')) or {}).get('ok') else 'NOT AS WANTED', len(prods), verdict))
    with open(BANK + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(BANK + '.tmp', BANK)
    for l in L[-8:]:
        print(l)
    print('written data/b725_dial.txt')


ROUTES = dict(tails=tails, c0=c0, identity=identity, price=price, run=run, bank=bank)

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ROUTES:
        print('usage: b725_dial.py ' + ' | '.join(ROUTES))
        sys.exit(2)
    ROUTES[sys.argv[1]](*sys.argv[2:])
