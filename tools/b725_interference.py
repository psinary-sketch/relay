# -*- coding: utf-8 -*-
"""b725_interference.py -- H-INTERFERENCE, (R335)(9), AS data/b725_registrations.txt (v) REGISTERED IT (committed alone at relay 390b7894
before any figure at it): "at every certified off-line zero rho of Z_Q0 in data/b711_list.json (to height 445), Z_Q1(rho) is nonzero beyond
its certified ball".

### UNTRACKED WRITE: data/b725_interference_units.jsonl (one unit per control and per zero, appended as each lands, resumable).
### THE ROUTE FOR Z_Q1 (the registration's, the seat's: the ruling's cited route a MISS, data/b725_addendum_citation.txt): the general
### Chowla-Selberg expansion of Z_Q, Q = a x^2 + b xy + c y^2, |D| = 4ac - b^2,
###   Z_Q(s) = 2 a^(-s) zeta(2s) + 2 a^(-1/2) sqrt(pi) Gamma(s - 1/2)/Gamma(s) (|D|/(4a))^(1/2 - s) zeta(2s - 1)
###            + 8 pi^s / (Gamma(s) sqrt a) SUM_{m <= M} cos(pi m b / a) K_{s-1/2}(pi m sqrt|D| / a) SUM_{k|m} (2k / (sqrt|D| (m/k)))^(s - 1/2) + T4,
### T4 the registration's bound added as the radius; Q1: a = 2, b = 1, |D| = 23. Z_Q0 by tools/b667_epstein_certify.py zq_point, imported
### unedited. Each value on the zero's ball at 200 bits, re-taken at 400, then 800, where the ball contains 0 or is wider than 2^-40 of
### its midpoint's modulus.
### Routes (each its own foreground call):
###   c1                  (C1): the two identities on the Dirichlet coefficients to n = 3000, exact
###   controls            (C2)-(C4): zeta's first zero, zeta_K against zeta L(chi_-23), the route against b667 at a = 1
###   price               the measured seconds per evaluation times the zeros
###   run [--budget s]    the 69 zeros in decreasing beta - 1/2, resumable
###   bank                data/b725_interference.txt
### Written by the Write tool at b725; it writes its units file and data/b725_interference.txt and nothing else. Nothing here proves RH or GRH.
"""
import io
import json
import math
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from flint import acb, arb, ctx, dirichlet_char    # noqa: E402
import b667_epstein_certify as CERT               # noqa: E402  ### b667's Z_Q0 (zq_point), imported unedited

UNITS = os.path.join(D, 'b725_interference_units.jsonl')
BANK = os.path.join(D, 'b725_interference.txt')
HOLD_MB = 2560
LADDER = (200, 400, 800)
REL_BAR = -40
N_C1 = 3000
Q1 = (2, 1, 23)
Q0 = (1, 1, 23)
BUDGET = 540


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


def guard(where):
    f = free_mb()
    print('  free MB %d at %s ; one process ; hold %d -- %s' % (f, where, HOLD_MB, 'MET' if f >= HOLD_MB else 'REFUSED'), flush=True)
    if f < HOLD_MB:
        sys.exit('### FREE MEMORY BENEATH THE HOLD -- REFUSED (nothing computed after this line)')


def units():
    U = {}
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[(u['route'], u['name'])] = u
    return U


def put_unit(u):
    u['at'] = utc()
    with open(UNITS, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


def bs(x):
    return [x.mid().str(30, radius=False), x.rad().str(5, radius=False)] if isinstance(x, arb) else \
        [x.real.mid().str(30, radius=False), x.real.rad().str(5, radius=False), x.imag.mid().str(30, radius=False), x.imag.rad().str(5, radius=False)]


def fmt(z, d=12):
    if isinstance(z, arb):
        return z.str(d, radius=True)
    return '(%s) + (%s)i' % (z.real.str(d, radius=True), z.imag.str(d, radius=True))


# ================================================================================ THE ROUTE
def _cos_exact(m, a, b):
    """cos(pi m b / a): exact where m b / a is a multiple of 1/2, a ball otherwise."""
    r = (2 * m * b) % (4 * a)                     # ### cos(pi x) with x = m b / a, 2x mod 4 = r / a
    if r % a == 0:
        return (arb(1), arb(0), arb(-1), arb(0))[r // a]
    return (arb.pi() * arb(m * b) / a).cos()


BESSEL_CAP = 4096
BESSEL_REL = -60


def _bessel_c(m, a, Dabs, nu, nu_mid, rad_nu, prec):
    """the amendment's Bessel factor (b667's (3b)): K_{nu_mid}(x) at the ball's centre, x = pi m sqrt|D| / a formed at each precision, the
    precision doubling from prec until the relative radius is below 2^-60 (at most 4096 bits), plus |nu - nu_mid| sup|d_nu K| by b667's
    dK_bound (imported unedited), returned at prec."""
    p = prec
    while True:
        ctx.prec = p
        x = arb.pi() * arb(Dabs).sqrt() * m / a
        K = acb(x).bessel_k(nu_mid)
        if (K.is_finite() and K.rad() <= abs(K.mid()) * arb(2) ** BESSEL_REL) or p >= BESSEL_CAP:
            break
        p *= 2
    ctx.prec = prec
    if rad_nu > 0:
        x = arb.pi() * arb(Dabs).sqrt() * m / a
        e = (rad_nu * CERT.dK_bound(x, nu)).upper()
        ctx.prec = prec
        K = K + acb(arb(0, e), arb(0, e))
    return K


def zq_form(s, a, b, Dabs, prec):
    """the registration's general Chowla-Selberg expansion at s (a point or a ball), at prec bits, T4 in the radius."""
    ctx.prec = prec
    s = acb(s)
    half = arb(1) / 2
    pi, sD, A = arb.pi(), arb(Dabs).sqrt(), arb(a)
    nu = s - half
    T1 = 2 * acb(A) ** (-s) * (2 * s).zeta()
    T2 = 2 * A ** (-half) * pi.sqrt() * (s - half).gamma() * s.rgamma() * acb(arb(Dabs) / (4 * A)) ** (half - s) * (2 * s - 1).zeta()
    c = pi * sD / A
    cf = float(c.mid())
    t = max(abs(float(s.imag.lower())), abs(float(s.imag.upper())))
    M = int(math.ceil((math.pi * t / 2 + (prec + 20) * math.log(2) + cf) / cf))
    pre = 8 * acb(pi) ** s * s.rgamma() * A ** (-half)
    nu_mid = acb(s.mid()) - half
    rad_nu = (s.real.rad() ** 2 + s.imag.rad() ** 2).sqrt()
    S = acb(0)
    for m in range(1, M + 1):
        cs = _cos_exact(m, a, b)
        if cs == 0:
            continue
        K = _bessel_c(m, a, Dabs, nu, nu_mid, rad_nu, prec)
        ctx.prec = prec
        ds = acb(0)
        for k in range(1, m + 1):
            if m % k == 0:
                ds += acb(2 * arb(k) / (sD * (m // k))) ** nu
        S += cs * K * ds
    T3 = pre * S
    mu = CERT._mu_abs(s)
    Kmu = acb(c * (M + 1)).bessel_k(acb(mu)).real
    rho = (arb(M + 2) / (M + 1)) ** (1 + mu) * (-c).exp()
    t4 = 8 * abs(acb(pi) ** s * s.rgamma()).upper() * A ** (-half) * (sD / 2) ** mu * Kmu * arb(M + 1) ** (1 + mu) / (1 - rho)
    r = arb(t4.upper())
    return T1 + T2 + T3 + acb(arb(0, r), arb(0, r)), M


def _good(v):
    return v.is_finite() and not v.contains(0) and v.rad() < abs(v.mid()) * arb(2) ** REL_BAR


def zq1_ladder(s):
    """Z_Q1 on the ball s by the ladder: (value, precision, M, seconds)."""
    t0 = time.time()
    v, M, p = None, None, None
    for p in LADDER:
        v, M = zq_form(s, Q1[0], Q1[1], Q1[2], p)
        if _good(v):
            break
    ctx.prec = LADDER[0]
    return v, p, M, round(time.time() - t0, 1)


def zq0(s):
    t0 = time.time()
    v = CERT.zq_point(acb(s))
    ctx.prec = LADDER[0]
    return v, round(time.time() - t0, 1)


# ================================================================================ (C1)
def r_counts(a, b, c, N):
    r = [0] * (N + 1)
    ymax = int(math.isqrt(4 * a * N // (4 * a * c - b * b))) + 2
    for y in range(-ymax, ymax + 1):
        xmax = int(math.isqrt(N // a + abs(b * y))) + abs(b * y) + 2
        for x in range(-xmax, xmax + 1):
            q = a * x * x + b * x * y + c * y * y
            if 0 < q <= N:
                r[q] += 1
    return r


def eta_eta23(N):
    """coefficients of eta(z) eta(23z) = q PROD (1 - q^k)(1 - q^23k) to q^N, exact (Euler's pentagonal series)."""
    e = [0] * (N + 1)
    J = int(math.isqrt(2 * N)) + 2
    for j in range(-J, J + 1):
        k = j * (3 * j - 1) // 2
        if 0 <= k <= N:
            e[k] += -1 if j % 2 else 1
    out = [0] * (N + 1)
    for i in range(N + 1):
        if e[i] == 0:
            continue
        for jj in range(0, (N - 1 - i) // 23 + 1):
            if e[jj] and i + 23 * jj + 1 <= N:
                out[i + 23 * jj + 1] += e[i] * e[jj]
    return out


def chi23(d):
    d %= 23
    return 0 if d == 0 else (1 if pow(d, 11, 23) == 1 else -1)


def c1(*a):
    N = N_C1
    t0 = time.time()
    r0, r1 = r_counts(1, 1, 6, N), r_counts(2, 1, 3, N)
    ideal = [0] + [sum(chi23(d) for d in range(1, n + 1) if n % d == 0) for n in range(1, N + 1)]
    bad_k = [n for n in range(1, N + 1) if r0[n] + 2 * r1[n] != 2 * ideal[n]]
    ee = eta_eta23(N)
    lc = [0] * (N + 1)
    odd = []
    for n in range(1, N + 1):
        if (r0[n] - r1[n]) % 2:
            odd.append(n)
        lc[n] = (r0[n] - r1[n]) // 2
    bad_l = [n for n in range(1, N + 1) if lc[n] != ee[n]]
    bad_m = [(m, n) for m in range(2, N + 1) for n in range(m + 1, N // m + 1) if math.gcd(m, n) == 1 and lc[m * n] != lc[m] * lc[n]]
    pairs = sum(1 for m in range(2, N + 1) for n in range(m + 1, N // m + 1) if math.gcd(m, n) == 1)
    # ### a non-vacuity count: the coefficients the check met that are not zero
    nz = sum(1 for n in range(1, N + 1) if lc[n])
    ok = not bad_k and not bad_l and not bad_m and not odd
    L = ['  (C1) n = 1..%d, exact: r_Q0 + 2 r_Q1 = 2 SUM_{d|n} (-23/d): mismatches %d %s' % (N, len(bad_k), bad_k[:5]),
         '  (C1) (r_Q0 - r_Q1)/2 integral at every n: odd differences %d ; equal to eta(z) eta(23z)`s q^n coefficient: mismatches %d %s ; nonzero coefficients met %d' % (
             len(odd), len(bad_l), bad_l[:5], nz),
         '  (C1) multiplicative on coprime pairs m < n, m n <= %d: pairs %d, mismatches %d %s' % (N, pairs, len(bad_m), bad_m[:5]),
         '  (C1) the first coefficients (n: r_Q0, r_Q1, ideal count, L`s): ' + ' ; '.join('%d: %d %d %d %d' % (n, r0[n], r1[n], ideal[n], lc[n]) for n in range(1, 13)),
         '### (C1) %s ; %.1f s' % ('AS WANTED' if ok else 'NOT AS WANTED', time.time() - t0)]
    for l in L:
        print(l)
    put_unit(dict(route='c1', name='', ok=ok, lines=L))


# ================================================================================ (C2)-(C4)
def chi_minus23():
    for j in range(1, 23):
        ch = dirichlet_char(23, j)
        if ch.is_real() and not ch.is_principal():
            return ch
    raise RuntimeError('no real character mod 23')


def controls(*a):
    guard('controls')
    U = units()
    ok_all = True
    L = []
    # ---- (C2)
    ctx.prec = LADDER[0]
    r1 = acb.zeta_zero(1)
    g = r1.imag
    zeta_ch = dirichlet_char(1, 1)
    zl, zr = zeta_ch.hardy_z(acb(g.mid() - arb('1e-6'))), zeta_ch.hardy_z(acb(g.mid() + arb('1e-6')))
    sign_change = bool((zl.real < 0 and zr.real > 0) or (zl.real > 0 and zr.real < 0))
    v1, p1, M1, s1 = zq1_ladder(r1)
    v0, s0 = zq0(r1)
    ctx.prec = LADDER[0]
    zk = v0 + 2 * v1
    ok = sign_change and zk.contains(0) and zk.rad() < arb('1e-20') and not v1.contains(0)
    ok_all &= ok
    L += ['  (C2) rho_1 = %s (acb.zeta_zero(1)) ; Hardy`s Z at gamma -/+ 1e-6: %s / %s, a sign change %s' % (fmt(r1, 20), fmt(zl.real, 6), fmt(zr.real, 6), sign_change),
          '  (C2) Z_Q1(rho_1) = %s (%d bits, M %d, %.1f s) ; Z_Q0(rho_1) = %s (%.1f s)' % (fmt(v1), p1, M1, s1, fmt(v0), s0),
          '  (C2) Z_Q0 + 2 Z_Q1 = %s ; contains 0 %s ; radius below 1e-20 %s ; Z_Q1 nonzero %s -- %s' % (
              fmt(zk, 6), zk.contains(0), zk.rad() < arb('1e-20'), not v1.contains(0), 'AS WANTED' if ok else 'NOT AS WANTED')]
    secs = [s1]
    # ---- (C3)
    chi = chi_minus23()
    for sv in (acb(2, 3), acb(arb('0.7'), 50)):
        v1, p1, M1, s1 = zq1_ladder(sv)
        v0, _ = zq0(sv)
        ctx.prec = LADDER[0]
        zk = (v0 + 2 * v1) / 2
        ref = sv.zeta() * acb.dirichlet_l(sv, chi)
        ok = zk.overlaps(ref) and zk.rad() < arb('1e-20') and ref.rad() < arb('1e-20')
        ok_all &= ok
        secs.append(s1)
        L.append('  (C3) s = %s: (Z_Q0 + 2 Z_Q1)/2 = %s ; zeta L(chi_-23) = %s (chi index %d) ; %s' % (
            fmt(sv, 4), fmt(zk, 14), fmt(ref, 14), chi.index(), 'AS WANTED' if ok else 'NOT AS WANTED'))
    # ---- (C4)
    sv = acb(arb('0.7'), 50)
    vf, Mf = zq_form(sv, Q0[0], Q0[1], Q0[2], LADDER[0])
    vb, _ = zq0(sv)
    ctx.prec = LADDER[0]
    ok = vf.overlaps(vb) and vf.rad() < arb('1e-20')
    ok_all &= ok
    L.append('  (C4) the route at a = b = 1, |D| = 23, s = 0.7 + 50i: %s (M %d) ; b667`s zq %s ; %s' % (fmt(vf, 14), Mf, fmt(vb, 14), 'AS WANTED' if ok else 'NOT AS WANTED'))
    L.append('### (C2)-(C4) %s ; Z_Q1`s seconds per evaluation at the controls %s' % ('AS WANTED' if ok_all else 'NOT AS WANTED', secs))
    for l in L:
        print(l, flush=True)
    put_unit(dict(route='controls', name='', ok=bool(ok_all), lines=L, secs=secs))


# ================================================================================ THE ZEROS
def zeros():
    import b709_pairs as P9
    import b711_list as L11
    top = L11.top()
    rows = P9.extended_rows(L11.units(), top)[0]
    off = [(n, sg, tt) for n, sg, tt in rows if n.startswith('off') and float(sg.mid()) > 0.5]
    return sorted(off, key=lambda z: -float(z[1].mid())), top


def price(*a):
    U = units()
    c = U.get(('controls', ''))
    if not c:
        sys.exit('### THE CONTROLS NOT RUN -- NO PRICE')
    Z, _top = zeros()
    per = max(c['secs'])
    print('PRICE: %d zeros ; the controls` seconds per Z_Q1 evaluation %s (the largest %.1f, at t = 50) ; Z_Q0 beside each ; at most about %d s '
          '(%.2f h) on one process, more where the ladder climbs or t is higher' % (len(Z), c['secs'], per, 2 * per * len(Z), 2 * per * len(Z) / 3600))


def run(*a):
    global BUDGET
    a = list(a)
    if '--budget' in a:
        BUDGET = int(a[a.index('--budget') + 1])
    U = units()
    c1u, cu = U.get(('c1', '')), U.get(('controls', ''))
    if not (c1u and c1u.get('ok') and cu and cu.get('ok')):
        sys.exit('### (C1)-(C4) NOT READ AS WANTED -- NO FIGURE AT AN OFF-LINE ZERO')
    guard('run')
    Z, _top = zeros()
    t0 = time.time()
    for i, (name, sg, tt) in enumerate(Z, 1):
        if ('zero', name) in U:
            continue
        if time.time() - t0 > BUDGET:
            print('### THE CALL`S BUDGET REACHED BEFORE %s (%d of %d) -- CALL AGAIN TO RESUME' % (name, i, len(Z)))
            return
        if i % 10 == 0:
            guard('zero %d' % i)
        s = acb(sg, tt)
        v1, p1, M1, s1 = zq1_ladder(s)
        v0, s0 = zq0(s)
        ctx.prec = LADDER[0]
        u = dict(route='zero', name=name, beta=bs(sg), t=bs(tt), z1=bs(v1), abs1=bs(abs(v1)), prec=p1, M=M1, excl=bool(not v1.contains(0)),
                 z0=bs(v0), z0_contains0=bool(v0.contains(0)), secs1=s1, secs0=s0)
        put_unit(u)
        U[('zero', name)] = u
        print('  %2d %-6s beta %.10f gamma %11.6f | |Z_Q1| %s (%d bits, M %d, %.0f s) %s | Z_Q0 contains 0 %s' % (
            i, name, float(sg.mid()), float(tt.mid()), fmt(abs(v1), 8), p1, M1, s1, 'EXCLUDES 0' if u['excl'] else 'CONTAINS 0', u['z0_contains0']), flush=True)
    print('### ALL %d ZEROS READ' % len(Z))


def bank(*a):
    U = units()
    Z, top = zeros()
    c1u, cu = U.get(('c1', '')), U.get(('controls', ''))
    L = ['b725 -- (R335)(9): H-INTERFERENCE, Z_Q1 AT Q0`S CERTIFIED OFF-LINE ZEROS (%s)' % utc(), '',
         '### by tools/b725_interference.py; the registration data/b725_registrations.txt (v) (relay 390b7894), committed alone before any figure;',
         '### the route for Z_Q1 the seat`s general Chowla-Selberg expansion (the ruling`s cited route a MISS, data/b725_addendum_citation.txt);',
         '### Z_Q0 by b667`s zq_point, imported unedited. Units: data/b725_interference_units.jsonl (untracked). Every value a ball.', '']
    L.append('## THE CONTROLS: (C1) %s ; (C2)-(C4) %s' % ('AS WANTED' if (c1u and c1u['ok']) else 'NOT AS WANTED', 'AS WANTED' if (cu and cu['ok']) else 'NOT AS WANTED'))
    runs = [json.loads(l) for l in io.open(UNITS, encoding='utf-8') if l.strip() and '"route": "controls"' in l] if os.path.exists(UNITS) else []
    L += (c1u or {}).get('lines', [])
    for i, r in enumerate(runs, 1):
        L.append('  ## (C2)-(C4), RUN %d of %d at %s%s' % (i, len(runs), r.get('at'), ' (BEFORE THE AMENDMENT of registration (v); not the run read)'
                                                          if i < len(runs) else ' (THE RUN READ)'))
        L += r.get('lines', [])
    L.append('')
    L.append('## THE ZEROS (list complete to %s ; off-line rows with beta > 1/2: %d), IN DECREASING beta - 1/2 -- the table READ BESIDE, not a test' % (top, len(Z)))
    L.append('  name    beta - 1/2     gamma         |Z_Q1(rho)|                    bits  Z_Q1 ball   Z_Q0 ball   zeta_K(rho) = Z_Q1(rho) = -2 L(rho, psi) (FORCED)')
    read, fired, notrun = 0, [], []
    for name, sg, tt in Z:
        u = U.get(('zero', name))
        if not u:
            notrun.append(name)
            L.append('  %-6s %.10f %12.6f  NOT RUN' % (name, float(sg.mid()) - 0.5, float(tt.mid())))
            continue
        read += 1
        if not u['excl']:
            fired.append(name)
        L.append('  %-6s %.10f %12.6f  %-30s %4d  %-11s %-11s %s' % (
            name, float(sg.mid()) - 0.5, float(tt.mid()), '%s +- %s' % (u['abs1'][0][:16], u['abs1'][1]), u['prec'],
            'EXCLUDES 0' if u['excl'] else 'CONTAINS 0', 'contains 0' if u['z0_contains0'] else 'EXCLUDES 0',
            'Z_Q1 = (%s) + (%s)i' % (u['z1'][0][:14], u['z1'][2][:14])))
    L.append('')
    verdict = 'REFUTED' if fired else ('NOT SCORABLE' if notrun else 'HELD')
    L.append('THE FALSIFIER (one off-line rho at which Z_Q1`s ball contains 0): %s' % ('FIRED at %s' % fired if fired else 'NOT FIRED on %d zeros' % read))
    L.append('NOT RUN (carried with its price): %s' % (notrun or 'none'))
    L.append('THE HYPOTHESIS (HELD, REFUTED or NOT SCORABLE): %s' % verdict)
    L.append('')
    L.append('### ### **H-INTERFERENCE: (C1) %s ; (C2)-(C4) %s ; ZEROS %d ; READ %d ; Z_Q1 EXCLUDES 0 AT %d ; THE HYPOTHESIS %s.**' % (
        'AS WANTED' if (c1u and c1u['ok']) else 'NOT AS WANTED', 'AS WANTED' if (cu and cu['ok']) else 'NOT AS WANTED', len(Z), read, read - len(fired), verdict))
    with open(BANK + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(BANK + '.tmp', BANK)
    for l in L[-6:]:
        print(l)
    print('written data/b725_interference.txt')


ROUTES = dict(c1=c1, controls=controls, price=price, run=run, bank=bank)

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ROUTES:
        print('usage: b725_interference.py ' + ' | '.join(ROUTES))
        sys.exit(2)
    ROUTES[sys.argv[1]](*sys.argv[2:])
