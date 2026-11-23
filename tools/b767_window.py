# -*- coding: utf-8 -*-
"""b767_window.py -- (R377)(6): THE WINDOW AT KNOTS GRADED BY OCTAVE, H-GRADED-WINDOW (relay data/b767_registration.txt, committed alone at
b9224ba6 before this tool's run), COMPUTED WITH NO DISPATCH AND BANKED AS DATA.

THE WINDOW: the knots t_0 < ... < t_160, 2^j (16 + i)/16 for j 0 .. 9 and i 0 .. 15, with 1024; the 157 cubic B-splines N_k on t_k ..
t_(k+4); c_k the value at the middle knot t_(k+2) of y^(-1/2) times the window at log y - log 32, rounded to 3 significant digits. Each
t_(k+2) is (j + 2)/16 for an integer j from 16 to 16380, a point of b765's uniform window at M 16 under the same rule, so c_k is read from
data/b765_window.json at that j (tools/b766_certificate.py window(): the bank through its digest at data/b765_window.txt :26) and not
computed again; the window's frequency is not read; nothing is computed at a zero and no bank of zeros is opened.
THE ROUTE, for any rational knots and coefficients:
  H in truncated powers: N_k(y) = (t_(k+4) - t_k) SUM_i w_(k,i) (y - t_(k+i))_+^3, w_(k,i) = 1 / PROD_(l != i) (t_(k+i) - t_(k+l)), so
  H(y) = SUM_m delta_m (y - t_m)_+^3, each delta_m exact; THE MOMENTS SUM_m delta_m t_m^r, r = 0 .. 3, are 0 (H vanishes past the last
  knot), checked; H's pieces p_a(y) = SUM_(m <= a) delta_m (y - t_m)^3 on [t_a, t_(a+1)], exact polynomials in y.
  BY EXACT PIECEWISE INTEGRATION IN y (tools/b765_window.py :33-:34): INT H; INT H / y; k(0) = INT H^2; L2 = INT H^2 log y; and K(n) =
  INT H(y) H(n y) dy over the common refinement of the knots and the knots over n, for n from 2 to 1023 at which cQ(n) is not 0. Beside
  them, from the truncated powers: INT H = SUM_m delta_m (T - t_m)^4 / 4 and INT H / y = SUM_m delta_m t_m^3 log t_m (T the last knot).
  THE ARCHIMEDEAN TERM, J = INT H(z) INT_0^z (H(z) - H(w)) / (z - w) dw dz (tools/b765_window.py :18-:19): for each knot t,
  INT_0^z ((z - t)_+^3 - (w - t)_+^3) / (z - w) dw = (z - t)_+^3 (log z - log(z - t) + 11/6), so J = (11/6) k(0) + L2 - X, X =
  INT H(z) SUM_m delta_m (z - t_m)_+^3 log(z - t_m) dz; written over the pairs of knots, each pair's upper limit cancels by the moments,
  and X = SUM_(m < m') delta_m delta_m' g^7 (log g / 140 - beta), g = t_m' - t_m, beta = INT_0^1 (v - 1)^3 v^3 log v dv; beside it
  k(0) = (1/140) SUM_(m < m') delta_m delta_m' g^7, a second route to k(0). The pairs grouped by their gap: over all pairs, or, where
  the knots are evenly spaced, by the autocorrelation of the delta (one integer polynomial product); the two equal at the test spline.
  A at Q0 = 2 k(0) (log(sqrt 23 / (2 pi)) - gamma) + 2 J (tools/b765_window.py :21); P = 2 INT H INT H / y; PR = 2 SUM cQ(n) K(n), cQ
  Lambda_Q exact in its primes (tools/b766_certificate.py lambda_q_exact, imported unedited). Every term an exact combination r_0 +
  r_gamma gamma + r_pi log pi + SUM_p r_p log p; the ball of S from it at PREC bits, read against 0 by the whole ball.
THE CONTROL, before any cell at graded knots (data/b767_registration.txt): (1) at b765's test spline (tools/b765_window.py :85) the route's
combination equals, exactly, that of b765's closed forms at uniform knots as b766 wrote them exactly (tools/b766_certificate.py), each K(n)
equal, its pairs and its autocorrelation group the gaps alike; and A PLANTED COEFFICIENT, one c moved by 1/7, READ AS A DIFFERENCE: the
comparison with b766's at the unmoved refused, the difference nonzero, and S(c + e) + S(c - e) - 2 S(c) = 2 S(e) exactly; (2) at the
uniform window M 16, d 3 (16,365 coefficients from data/b765_window.json) the route prints the banked value, -6.62468014575, to 10
digits, each K(n) equal to data/b766_certificate.json's and its combination equal to that bank's, exactly.
Nothing of a coefficient, a K(n) or a combination's r is printed: only sums and figures. The window's coefficients stand in the units file
(untracked) and in data/b767_window.json, the window banked as data.

  python -X utf8 -I -u tools/b767_window.py control   the control; one unit appended to data/b767_window_units.jsonl (UNTRACKED)
  python -X utf8 -I -u tools/b767_window.py cell      the cell at graded knots; refused until the control's unit stands AS WANTED
  python -X utf8 -I -u tools/b767_window.py bank      data/b767_window.txt and data/b767_window.json, with the reading
Each route refuses where this file or tools/b766_certificate.py differs from its blob at the relay's HEAD (committed before its run, N2).
Written by the Write tool.
"""
import bisect
import hashlib
import importlib.util
import json
import math
import os
import subprocess
import sys
import time

from flint import arb, ctx, fmpq, fmpq_poly, fmpz, fmpz_poly

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT = 'b767'
SELF = 'tools/b767_window.py'
CARRIED = 'tools/b766_certificate.py'
REG, REG_COMMIT = 'data/b767_registration.txt', 'b9224ba6'
CJSON = 'data/b766_certificate.json'
UNITS = os.path.join(ROOT, 'data', 'b767_window_units.jsonl')     # ### UNTRACKED WRITE: one unit a route, appended
BANK_TXT, BANK_JSON = 'data/b767_window.txt', 'data/b767_window.json'
PREC = 512
SREF = '-6.62468014575'     # ### data/b765_window.txt :19, the uniform window's cell, M 16, d 3
DIGITS = 10
YTOP = 1024
M_UNI = 16
TEST = dict(M=2, ytop=8, c=(3, -1, 4, 1, -5, 9, 2, -6, 5, 3, -5), den=7)   # ### tools/b765_window.py :85
PLANT = (5, 1)              # ### the test spline's sixth coefficient moved by 1 over its denominator
PRICE_UPPER_H = 1.80        # ### data/b767_price.txt :24
BETA = fmpq(1, 16) - fmpq(3, 25) + fmpq(3, 36) - fmpq(1, 49)   # ### INT_0^1 (v - 1)^3 v^3 log v dv, by INT_0^1 v^k log v dv = -1/(k + 1)^2

_spec = importlib.util.spec_from_file_location('b766_certificate', os.path.join(ROOT, *CARRIED.split('/')))
B6 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B6)
LAM = B6.lambda_q_exact(YTOP - 1, B6.factor_table(YTOP))[0]   # ### Lambda_Q(n), n <= 1023, each {p: the rational coefficient of log p}


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True)


def committed():
    out = []
    for rel in (SELF, CARRIED):
        here = open(os.path.join(ROOT, *rel.split('/')), 'rb').read().replace(b'\r', b'')
        r = _git('show', 'HEAD:' + rel)
        if r.returncode != 0 or r.stdout.replace(b'\r', b'') != here:
            sys.exit('### %s DIFFERS FROM ITS BLOB AT THE RELAY`S HEAD, OR IS NOT COMMITTED -- NOTHING RUN' % rel)
        out.append(hashlib.sha256(here).hexdigest())
    return _git('rev-parse', '--short=8', 'HEAD').stdout.decode().strip(), out[0]


def bs(x):
    x = arb(x)
    return [x.mid().str(45, radius=False), x.rad().str(5, radius=False)]


def bl(p):
    return arb(p[0], p[1])


def fmt(x, n=12):
    x = arb(x)
    return '%s +- %s' % (x.mid().str(n, radius=False), x.rad().str(3, radius=False))


# ================================================================================ THE KNOTS AND THE COEFFICIENTS
def graded_knots():
    return [fmpq(2 ** j * (16 + i), 16) for j in range(10) for i in range(16)] + [fmpq(YTOP)]


def uniform_knots(M, ytop):
    return [fmpq(k, M) for k in range(M, ytop * M + 1)]


def rat(me):
    m, e = me
    return fmpq(m) * fmpq(10) ** e if e >= 0 else fmpq(m, 10 ** -e)


def graded_coeffs(cm):
    """c_k at the middle knot t_(k+2) = (j + 2)/16, read from the uniform bank at that j; refused where a middle knot is not such a point."""
    t = graded_knots()
    out, js = [], []
    for k in range(len(t) - 4):
        j16 = t[k + 2] * 16 - 2
        if j16.q != 1 or not (16 <= int(j16.p) <= 16380) or int(j16.p) not in cm:
            sys.exit('### THE MIDDLE KNOT OF SPLINE %d IS NOT A POINT OF THE UNIFORM BANK -- NOTHING COMPUTED' % k)
        js.append(int(j16.p))
        out.append(rat(cm[int(j16.p)]))
    return t, out, js


# ================================================================================ THE ROUTE
def deltas(t, c):
    """delta_m, m = 0 .. N: SUM_k c_k N_k = SUM_m delta_m (y - t_m)_+^3."""
    d = [fmpq(0)] * len(t)
    for k, ck in enumerate(c):
        if ck == 0:
            continue
        span = t[k + 4] - t[k]
        for i in range(5):
            w = fmpq(1)
            for l in range(5):
                if l != i:
                    w *= t[k + i] - t[k + l]
            d[k + i] += ck * span / w
    return d


def pieces(t, d):
    P, acc = [], fmpq_poly([0])
    for a in range(len(t) - 1):
        if d[a] != 0:
            x = t[a]
            acc = acc + d[a] * fmpq_poly([-x ** 3, 3 * x ** 2, -3 * x, 1])
        P.append(acc)
    return P


class Form:
    """one + gamma * gamma + logpi * log pi + SUM_m L[m] log m (m >= 2), every coefficient an exact rational."""

    def __init__(self):
        self.one, self.gamma, self.logpi, self.L = fmpq(0), fmpq(0), fmpq(0), {}

    def log(self, x, c):
        """adds c log x, x a positive rational."""
        if c != 0:
            p, q = int(x.p), int(x.q)
            if p > 1:
                self.L[p] = self.L.get(p, fmpq(0)) + c
            if q > 1:
                self.L[q] = self.L.get(q, fmpq(0)) - c
        return self

    def add(self, o, c=1):
        c = fmpq(c)
        self.one += c * o.one
        self.gamma += c * o.gamma
        self.logpi += c * o.logpi
        for m, x in o.L.items():
            self.L[m] = self.L.get(m, fmpq(0)) + c * x
        return self


def reduce(F):
    """the form over the primes: (r_0, r_gamma, r_pi, {p: r_p}), zeros dropped."""
    rp = {}
    for m, x in F.L.items():
        if x != 0:
            for p, e in fmpz(m).factor():
                rp[int(p)] = rp.get(int(p), fmpq(0)) + int(e) * x
    return (F.one, F.gamma, F.logpi, dict((p, x) for p, x in rp.items() if x != 0))


def comb_lin(terms):
    r0, rg, rpi, rp = fmpq(0), fmpq(0), fmpq(0), {}
    for c, X in terms:
        c = fmpq(c)
        r0 += c * X[0]
        rg += c * X[1]
        rpi += c * X[2]
        for p, x in X[3].items():
            rp[p] = rp.get(p, fmpq(0)) + c * x
    return (r0, rg, rpi, dict((p, x) for p, x in rp.items() if x != 0))


def is_zero(X):
    return X[0] == 0 and X[1] == 0 and X[2] == 0 and not X[3]


def ball(X):
    return B6.ball(X, sorted(X[3]))


def gaps_pairs(t, d):
    """{gap key: (g, SUM delta_m delta_m')} over all pairs m < m'."""
    nz = [(t[m], d[m]) for m in range(len(t)) if d[m] != 0]
    R = {}
    for i in range(len(nz)):
        ti, di = nz[i]
        for j in range(i + 1, len(nz)):
            g = nz[j][0] - ti
            key = (int(g.p), int(g.q))
            old = R.get(key)
            R[key] = (g, (old[1] if old else fmpq(0)) + di * nz[j][1])
    return dict((k, v) for k, v in R.items() if v[1] != 0)


def gaps_ap(t, d):
    """the same, where the knots are evenly spaced, by the autocorrelation of the delta (one integer polynomial product); None otherwise."""
    h = t[1] - t[0]
    if any(t[m + 1] - t[m] != h for m in range(len(t) - 1)):
        return None
    Q = 1
    for x in d:
        q = int(x.q)
        Q = Q * q // math.gcd(Q, q)
    D = [int(x.p) * (Q // int(x.q)) for x in d]
    L = len(D)
    pc = (fmpz_poly(D) * fmpz_poly(D[::-1])).coeffs()
    R = {}
    for dd in range(1, L):
        idx = L - 1 + dd
        v = int(pc[idx]) if idx < len(pc) else 0
        if v:
            g = dd * h
            R[(int(g.p), int(g.q))] = (g, fmpq(v, Q * Q))
    return R


def kn(t, P, n):
    """K(n) = INT H(y) H(n y) dy, exact, over the common refinement of the knots and the knots over n."""
    top = t[-1] / n
    if top <= t[0]:
        return fmpq(0)
    y, a = t[0], 0
    b = bisect.bisect_right(t, n * y) - 1
    sc = fmpq_poly([0, n])
    qb, qbi = None, -1
    tot = fmpq(0)
    while y < top:
        na, nb = t[a + 1], t[b + 1] / n
        hi = na if na < nb else nb
        if qbi != b:
            qb, qbi = P[b](sc), b
        F = (P[a] * qb).integral()
        tot += F(hi) - F(y)
        if hi == na:
            a += 1
        if hi == nb:
            b += 1
        y = hi
    return tot


def route(t, c, nlist, gaps=None):
    """the terms at the spline SUM_k c_k N_k on the knots t by the route of the head; gaps 'pairs', 'ap' or None (ap where the knots are
    evenly spaced, pairs otherwise)."""
    t0 = time.time()
    N = len(t) - 1
    T = t[-1]
    d = deltas(t, c)
    mom = [sum((d[m] * t[m] ** r for m in range(N + 1) if d[m] != 0), fmpq(0)) for r in range(4)]
    P = pieces(t, d)
    intH_p, k0_p = fmpq(0), fmpq(0)
    hy_p, L2 = Form(), Form()
    for a in range(N):
        p = P[a]
        lo, hi = t[a], t[a + 1]
        Ip = p.integral()
        intH_p += Ip(hi) - Ip(lo)
        co = p.coeffs()
        if co:
            hy_p.log(hi, co[0]).log(lo, -co[0])
            for l in range(1, len(co)):
                hy_p.one += co[l] * (hi ** l - lo ** l) / l
        q = p * p
        Q = q.integral()
        Qh, Ql = Q(hi), Q(lo)
        k0_p += Qh - Ql
        L2.log(hi, Qh).log(lo, -Ql)
        cq = q.coeffs()
        if cq:
            R2 = fmpq_poly([0] + [cq[l] / (l + 1) ** 2 for l in range(len(cq))])
            L2.one -= R2(hi) - R2(lo)
    intH_c = sum((d[m] * (T - t[m]) ** 4 for m in range(N + 1) if d[m] != 0), fmpq(0)) / 4
    hy_c = Form()
    for m in range(N + 1):
        if d[m] != 0:
            hy_c.log(t[m], d[m] * t[m] ** 3)
    if gaps is None:
        R = gaps_ap(t, d)
        gaps = 'ap' if R is not None else 'pairs'
        if R is None:
            R = gaps_pairs(t, d)
    else:
        R = gaps_ap(t, d) if gaps == 'ap' else gaps_pairs(t, d)
    t_gap = time.time()
    s7, X = fmpq(0), Form()
    for _k, (g, r) in R.items():
        w = r * g ** 7
        s7 += w
        X.log(g, w / 140)
    X.one -= BETA * s7
    k0_g = s7 / 140
    J = Form()
    J.one += fmpq(11, 6) * k0_p
    J.add(L2).add(X, -1)
    A = Form()
    A.log(fmpq(23), k0_p).log(fmpq(2), -2 * k0_p)
    A.logpi -= 2 * k0_p
    A.gamma -= 2 * k0_p
    A.add(J, 2)
    Pf = Form().add(hy_p, 2 * intH_p)
    K = dict((n, kn(t, P, n)) for n in nlist)
    t_kn = time.time()
    PR = Form()
    products = 0
    for n in nlist:
        if n >= 2 and K[n] != 0 and LAM[n]:
            products += 1
            for p_, x in LAM[n].items():
                PR.L[p_] = PR.L.get(p_, fmpq(0)) + 2 * x * K[n]
    S = Form().add(Pf).add(PR, -1).add(A)
    hy_eq = reduce(hy_p) == reduce(hy_c)
    checks = dict(moments_zero=all(x == 0 for x in mom), intH_two_routes=intH_p == intH_c, intHy_two_routes=hy_eq,
                  k0_pieces_gaps=k0_p == k0_g)
    if 1 in K:
        checks['K1_equals_k0'] = K[1] == k0_p
    return dict(S=reduce(S), P=reduce(Pf), PR=reduce(PR), A=reduce(A), k0=k0_p, intH=intH_p, K=K, R=R, gaps=gaps, checks=checks,
                products=products, ncoef=len(c), nonzero=sum(1 for x in c if x != 0), knots=len(t),
                secs=dict(to_gaps=int(t_gap - t0), kn=int(t_kn - t_gap), all=int(time.time() - t0)))


# ================================================================================ b765'S CLOSED FORMS AS b766 WROTE THEM EXACTLY
def b766_comb(C, S, M, ytop, ns):
    """tools/b766_certificate.py compute() :406-:453 at the integer coefficients C over S, its closed forms called unedited."""
    jmax = ytop * M - 4
    S2M = fmpq(M * S * S)
    dmax = jmax - M
    mmax = max(jmax + 6, 24)
    spf = B6.factor_table(mmax)
    intH = fmpq(sum(C), M * S)
    A_ = fmpz_poly(C)
    pc = (A_ * fmpz_poly(list(reversed(C)))).coeffs()

    def cauto(x):
        idx = jmax + x
        return int(pc[idx]) if 0 <= x <= dmax and idx < len(pc) else 0
    k0 = (B6.BETA_D[0] * cauto(0) + 2 * sum((B6.BETA_D[dd] * cauto(dd) for dd in (1, 2, 3)), fmpq(0))) / S2M
    rho = B6.rho_comb(C, M, jmax, mmax)
    band = B6.band_comb(C, M, jmax, mmax)
    lam = B6.lam_comb(cauto, dmax, mmax)
    one = B6.Comb(mmax)
    one.one = fmpq(1)
    J = B6.lin(mmax, (fmpq(11, 6) * k0, one), (fmpq(1) / S2M, band), (fmpq(-1) / S2M, lam))
    arch = B6.Comb(mmax)
    arch.L[23], arch.L[2], arch.logpi, arch.gamma = fmpq(1, 2), fmpq(-1), fmpq(-1), fmpq(-1)
    A = B6.lin(mmax, (2 * k0, arch), (fmpq(2), J))
    P = B6.lin(mmax, (2 * intH / S, rho))
    Sc = B6.lin(mmax, (fmpq(1), P), (fmpq(1), A))
    rp = {}
    for m, x in enumerate(Sc.L):
        if m >= 2 and x != 0:
            for p, a in B6.factor(m, spf).items():
                rp[p] = rp.get(p, fmpq(0)) + a * x
    K = {}
    for n in ns:
        K[n] = B6.kn_scaled(C, M, jmax, n) / S2M
        if K[n] != 0:
            for p, x in LAM[n].items():
                rp[p] = rp.get(p, fmpq(0)) - 2 * x * K[n]
    return (Sc.one, Sc.gamma, Sc.logpi, dict((p, x) for p, x in rp.items() if x != 0)), K, k0


# ================================================================================ THE UNITS
def units():
    U = {}
    if os.path.exists(UNITS):
        for l in open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[u['key']] = u
    return U


def put_unit(u, commit, sha):
    u['at'] = utc()
    u['tool'] = dict(commit=commit, sha256=sha[:16])
    with open(UNITS, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


def agree(v):
    ok, mid = B6.agree(v, SREF)
    return bool(ok), str(mid)[:16]


# ================================================================================ THE CONTROL
def control(*a):
    commit, sha = committed()
    ctx.prec = PREC
    t0 = time.time()
    js, cm, _L, dig = B6.window()
    ck = {}
    # (1) the test spline
    M, ytop, den = TEST['M'], TEST['ytop'], TEST['den']
    t = uniform_knots(M, ytop)
    c = [fmpq(x, den) for x in TEST['c']]
    if len(c) != len(t) - 4:
        sys.exit('### THE TEST SPLINE`S COEFFICIENTS DO NOT FILL ITS KNOTS -- NOTHING COMPUTED')
    nl = [1] + [n for n in range(2, ytop) if LAM[n]]
    ap = route(t, c, nl, 'ap')
    pr = route(t, c, nl, 'pairs')
    C = [0] * M + list(TEST['c'])
    ref, refK, refk0 = b766_comb(C, den, M, ytop, [n for n in nl if n >= 2])
    ck['test: the route`s internal checks'] = all(ap['checks'].values()) and all(pr['checks'].values())
    ck['test: the pairs and the autocorrelation group the gaps alike'] = ap['R'] == pr['R'] and ap['S'] == pr['S']
    ck['test: the combination equals b766`s closed forms`, exactly'] = ap['S'] == ref
    ck['test: each K(n) and k(0) equal b766`s'] = all(ap['K'][n] == refK[n] for n in refK) and ap['k0'] == refk0
    k_, dv = PLANT
    cp, cmn, e = list(c), list(c), [fmpq(0)] * len(c)
    cp[k_] += fmpq(dv, den)
    cmn[k_] -= fmpq(dv, den)
    e[k_] = fmpq(dv, den)
    Sp, Sm, Se = (route(t, x, nl)['S'] for x in (cp, cmn, e))
    diff = comb_lin([(1, Sp), (-1, ref)])
    second = comb_lin([(1, Sp), (1, Sm), (-2, ap['S'])]) == comb_lin([(2, Se)])
    ck['PLANTED: c_%d moved by %d/%d, the comparison with b766`s at the unmoved refused, the difference nonzero, the second difference 2 S(e)' % (
        k_, dv, den)] = (Sp != ref) and not is_zero(diff) and second
    test_S = ball(ap['S'])
    # (2) the uniform window at M 16, d 3
    tu = uniform_knots(M_UNI, YTOP)
    cu = [rat(cm[M_UNI + k]) for k in range(len(tu) - 4)]
    nlu = [1] + [n for n in range(2, YTOP) if LAM[n]]
    ru = route(tu, cu, nlu)
    cj = json.load(open(os.path.join(ROOT, *CJSON.split('/')), encoding='utf-8'))
    rK = dict((int(n), B6.q_of(v)) for n, v in cj['K'].items())
    s_ = cj['S']
    rS = (B6.q_of(s_['r_0']), B6.q_of(s_['r_gamma']), B6.q_of(s_['r_pi']), dict((int(p), B6.q_of(v)) for p, v in s_['r_p'].items()))
    Su = ball(ru['S'])
    ok10, mid = agree(Su)
    ck['uniform M 16: the route`s internal checks'] = all(ru['checks'].values())
    ck['uniform M 16: S to 10 digits against %s' % SREF] = ok10
    ck['uniform M 16: each K(n) equal to data/b766_certificate.json`s'] = set(rK) == set(n for n in nlu if n >= 2) and all(ru['K'][n] == rK[n] for n in rK)
    ck['uniform M 16: the combination equal to data/b766_certificate.json`s, exactly'] = ru['S'] == rS
    wanted = all(ck.values())
    u = dict(key='control', route='control', checks=ck, wanted=wanted, test=dict(S=bs(test_S), checks=ap['checks'], gaps=ap['gaps']),
             uniform=dict(S=bs(Su), mid10=mid, P=bs(ball(ru['P'])), PR=bs(ball(ru['PR'])), A=bs(ball(ru['A'])), k0=bs(arb(ru['k0'])),
                          ncoef=ru['ncoef'], products=ru['products'], gaps=ru['gaps'], internal=ru['checks'], secs=ru['secs']),
             window_bank=dict(text_sha=dig['text_sha'][:16], coef_sha=dig['coef_sha']), prec=PREC, seconds=int(time.time() - t0))
    put_unit(u, commit, sha)
    print('  THE CONTROL (tools/b767_window.py at relay %s), before any cell at graded knots:' % commit)
    print('    the test spline M %d on [1, %d], %d coefficients over %d: S %s ; the gaps by %s' % (M, ytop, len(c), den, fmt(test_S), ap['gaps']))
    print('    the uniform window M %d, d 3, %d coefficients: S %s (to 10 digits %s) ; P %s ; PR %s ; A %s ; k(0) %s ; rational products %d ; '
          'the gaps by %s ; %s s' % (M_UNI, ru['ncoef'], fmt(Su), mid, fmt(ball(ru['P'])), fmt(ball(ru['PR'])), fmt(ball(ru['A'])),
                                    fmt(arb(ru['k0'])), ru['products'], ru['gaps'], ru['secs']))
    for k, v in ck.items():
        print('    %s: %s' % (k, 'AS WANTED' if v else '### NOT AS WANTED'))
    print('  ### ### **THE CONTROL %s: %d OF %d ; %d s.**' % ('AS WANTED' if wanted else 'NOT AS WANTED', sum(1 for v in ck.values() if v), len(ck),
                                                           u['seconds']))
    return 0 if wanted else 1


# ================================================================================ THE CELL
def budget(X, aS):
    """b766's rule (tools/b766_certificate.py :462-:480) over gamma, log pi and each log p."""
    cons = [('gamma', X[1]), ('log pi', X[2])] + [('log %d' % p, X[3][p]) for p in sorted(X[3])]
    cons = [(n, x) for n, x in cons if x != 0]
    N = len(cons)
    ln10 = arb(10).log()
    digits = []
    for n, x in cons:
        v = ((arb(abs(x)) * (2 * N)) / aS).log() / ln10
        digits.append(int(math.floor(float(v.mid()))) + 1)
    sabs = sum((abs(x) for _n, x in cons), fmpq(0))
    uv = ((arb(sabs) * 2) / aS).log() / ln10
    return dict(N=N, sabs=sabs, uniform=int(math.floor(float(uv.mid()))) + 1, dmax=max(digits or [0]), dmin=min(digits or [0]))


def reading_of(S):
    if S < 0:
        return 'HELD'
    if S >= 0:
        return 'REFUTED'
    return 'NOT SCORABLE'


def cell(*a):
    commit, sha = committed()
    U = units()
    cu = U.get('control')
    if cu is None or not cu['wanted']:
        sys.exit('### THE CONTROL`S UNIT %s -- NO CELL COMPUTED AT GRADED KNOTS' % ('MISSING' if cu is None else 'NOT AS WANTED'))
    ctx.prec = PREC
    t0 = time.time()
    js, cm, _L, dig = B6.window()
    t, c, jj = graded_coeffs(cm)
    nl = [1] + [n for n in range(2, YTOP) if LAM[n]]
    r = route(t, c, nl)
    Sv, Pv, PRv, Av = ball(r['S']), ball(r['P']), ball(r['PR']), ball(r['A'])
    reading = reading_of(Sv)
    B = budget(r['S'], abs(Sv)) if reading != 'NOT SCORABLE' else None
    u = dict(key='cell', route='cell', knots=[str(x) for x in t], coefficients=[[k, jj[k], str(t[k + 2]), str(c[k])] for k in range(len(c))],
             S=bs(Sv), P=bs(Pv), PR=bs(PRv), A=bs(Av), k0=bs(arb(r['k0'])), intH=str(r['intH']), ncoef=r['ncoef'], nonzero=r['nonzero'],
             products=r['products'], primes=len(r['S'][3]), gaps=r['gaps'], internal=r['checks'], reading=reading,
             budget=None if B is None else dict(constants=B['N'], sum_abs_r=str(B['sabs']), sum_abs_r_float='%.6g' % float(B['sabs']),
                                                uniform_digits=B['uniform'], digits_low=B['dmin'], digits_high=B['dmax']),
             window_bank=dict(text_sha=dig['text_sha'][:16], coef_sha=dig['coef_sha']), prec=PREC, secs=r['secs'],
             seconds=int(time.time() - t0), wanted=all(r['checks'].values()))
    put_unit(u, commit, sha)
    print('  THE CELL AT KNOTS GRADED BY OCTAVE (registration %s at %s): %d knots, %d coefficients (%d nonzero), each read at its middle knot '
          'from the uniform bank' % (REG, REG_COMMIT, len(t), r['ncoef'], r['nonzero']))
    print('    S %s ; P %s ; PR %s ; A %s ; k(0) %s ; rational products %d ; the gaps by %s ; %s s' % (
        fmt(Sv), fmt(Pv), fmt(PRv), fmt(Av), fmt(arb(r['k0'])), r['products'], r['gaps'], r['secs']))
    print('    the route`s internal checks: %s' % ' ; '.join('%s %s' % kv for kv in r['checks'].items()))
    if B is not None:
        print('    the combination: %d primes ; constants %d ; the sum of the |r| %s ; the budget`s one width %d digits (by constant %d to %d)' % (
            len(r['S'][3]), B['N'], u['budget']['sum_abs_r_float'], B['uniform'], B['dmin'], B['dmax']))
    print('  ### ### **H-GRADED-WINDOW: THE BALL %s ; %d s.**' % (reading, u['seconds']))
    return 0 if u['wanted'] else 1


# ================================================================================ THE BANK
def put_txt(rel, L):
    p = os.path.join(ROOT, *rel.split('/'))
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def reg_time():
    r = _git('log', '-1', '--format=%ct', REG_COMMIT)
    return int(r.stdout.decode().strip())


def price(u):
    return ('the DATA lemmas at %d coefficients: the coefficients` lemma %d lines generated (L2), the DATA parts 400-1,500 lines by hand and '
            '2-5 dispatches (data/b766_plan.txt :72, the K values` sums some 197 x %d products); the enclosures over %d primes: the table '
            '%d lines generated and 300-1,000 lines by hand, 1-3 dispatches, at %s digits (data/b767_plan.txt :67-:74, there 1,900 primes at '
            '22)' % (u['ncoef'], u['ncoef'] + 20, u['ncoef'], u['primes'], u['primes'],
                     u['budget']['uniform_digits'] if u['budget'] else '-'))


def bank(*a):
    commit, sha = committed()
    ctx.prec = PREC     # ### the units' balls read back at the precision they were written at
    U = units()
    cu, ce = U.get('control'), U.get('cell')
    hours = (time.time() - reg_time()) / 3600.0
    L = ['b767 -- THE WINDOW AT KNOTS GRADED BY OCTAVE, (R377)(6): H-GRADED-WINDOW (relay %s, committed alone at %s before this tool`s run), '
         'computed with no dispatch (%s)' % (REG, REG_COMMIT, utc()), '',
         '### the tool %s, sha256 %s, committed at relay %s before its run; tools/b766_certificate.py imported unedited; every value an exact'
         % (SELF, sha[:16], commit),
         '### rational or an exact combination of 1, gamma, log pi and the logarithms of primes, its ball at %d bits read against 0 by the' % PREC,
         '### whole ball. The coefficients read from data/b765_window.json at the middle knots (each a point (j + 2)/16 of the uniform window),',
         '### the bank through its digest; the window`s frequency not read; nothing computed at a zero; no bank of zeros opened; no coefficient,',
         '### no K(n) and no r printed here. The route: the head of the tool.', '', '## THE CONTROL, BEFORE ANY CELL']
    if cu is None:
        L.append('  NOT RUN')
    else:
        L.append('  the test spline (tools/b765_window.py :85): S %s ; the uniform window M 16, d 3: S %s (to 10 digits %s, against %s) ; P %s ; '
                 'PR %s ; A %s ; k(0) %s ; %d coefficients ; rational products %d ; %d s' % (
                     fmt(bl(cu['test']['S'])), fmt(bl(cu['uniform']['S'])), cu['uniform']['mid10'], SREF, fmt(bl(cu['uniform']['P'])),
                     fmt(bl(cu['uniform']['PR'])), fmt(bl(cu['uniform']['A'])), fmt(bl(cu['uniform']['k0'])), cu['uniform']['ncoef'],
                     cu['uniform']['products'], cu['seconds']))
        L += ['  %s: %s' % (k, 'AS WANTED' if v else '### NOT AS WANTED') for k, v in cu['checks'].items()]
        L.append('  THE CONTROL %s (unit at %s, tool %s)' % ('AS WANTED' if cu['wanted'] else 'NOT AS WANTED', cu['at'], cu['tool']['commit']))
    L += ['', '## THE CELL AT GRADED KNOTS']
    if ce is None:
        L.append('  NOT RUN')
    else:
        L.append('  %d knots, %d coefficients (%d nonzero) ; S %s ; P %s ; PR %s ; A %s ; k(0) %s ; rational products %d ; the gaps by %s ; '
                 'internal checks %s ; %d s (unit at %s, tool %s)' % (
                     len(ce['knots']), ce['ncoef'], ce['nonzero'], fmt(bl(ce['S'])), fmt(bl(ce['P'])), fmt(bl(ce['PR'])), fmt(bl(ce['A'])),
                     fmt(bl(ce['k0'])), ce['products'], ce['gaps'], 'ALL MET' if ce['wanted'] else '### NOT ALL MET', ce['seconds'], ce['at'],
                     ce['tool']['commit']))
        if ce['budget']:
            L.append('  REPORTED BESIDE IT, unregistered: %d coefficients ; rational products %d ; the combination`s primes %d, constants %d ; the '
                     'sum of the |r| %s ; the budget`s one width %d digits (by constant %d to %d)' % (
                         ce['ncoef'], ce['products'], ce['primes'], ce['budget']['constants'], ce['budget']['sum_abs_r_float'],
                         ce['budget']['uniform_digits'], ce['budget']['digits_low'], ce['budget']['digits_high']))
        L.append('  THE SEAT`S PRICE THERE: %s' % price(ce))
    if cu is None or not cu['wanted']:
        verdict, why = 'NOT SCORABLE', 'the control at the uniform window was not met'
    elif ce is None or not ce['wanted']:
        verdict, why = 'NOT SCORABLE', 'the cell not computed, or its internal checks not met'
    else:
        verdict, why = ce['reading'], ''
    if hours > PRICE_UPPER_H and verdict != 'NOT SCORABLE':
        L.append('  THE ROUTE`S HOURS %.2f from the registration`s commit, past the price`s upper %.2f h' % (hours, PRICE_UPPER_H))
    letter = {'HELD': '[G1]', 'REFUTED': '[G2]'}.get(verdict, '[G3]')
    L += ['', '## THE READING',
          '  H-GRADED-WINDOW: %s, %s%s ; %.2f h from the registration`s commit (%s) to this bank, the price`s upper %.2f h' % (
              verdict, letter, (' (%s)' % why) if why else '', hours, REG_COMMIT, PRICE_UPPER_H)]
    jsn = dict(act=ACT, ruling='(R377)(6)', registration=dict(path=REG, commit=REG_COMMIT), tool=dict(path=SELF, commit=commit, sha256=sha[:16]),
               h='h(v) = e^(v/2) H(e^v)', H='H(y) = SUM_k c_k N_k(y), N_k the cubic B-spline on the knots t_k .. t_(k+4)',
               knots_rule='2^j (16 + i)/16 for j 0 .. 9 and i 0 .. 15, with 1024', k='the autocorrelation of h', support=[1, YTOP],
               coefficient_rule='c_k = the value at the middle knot t_(k+2) of y^(-1/2) times the window at log y - log 32, rounded to 3 significant '
                                'digits (half to even), read from data/b765_window.json at j = 16 t_(k+2) - 2',
               reading=verdict, letter=letter, why=why, hours_from_registration=round(hours, 2))
    if ce is not None:
        jsn.update(knots=ce['knots'], coefficients=ce['coefficients'], S=ce['S'], P=ce['P'], PR=ce['PR'], A=ce['A'], k0=ce['k0'],
                   ncoef=ce['ncoef'], nonzero=ce['nonzero'], products=ce['products'], primes=ce['primes'], budget=ce['budget'],
                   window_bank=ce['window_bank'], prec=PREC)
    data = json.dumps(jsn, ensure_ascii=False, indent=1)
    put_txt(BANK_JSON, [data])
    L.append('  %s: written, %s coefficients as rationals, sha256 %s' % (BANK_JSON, ce['ncoef'] if ce else 0,
                                                                         hashlib.sha256((data + NL).encode('utf-8')).hexdigest()[:16]))
    put_txt(BANK_TXT, L)
    print(NL.join(L))
    return 0


ROUTES = {'control': control, 'cell': cell, 'bank': bank}

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ROUTES:
        sys.exit(__doc__)
    sys.exit(ROUTES[sys.argv[1]](*sys.argv[2:]))
