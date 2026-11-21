# -*- coding: utf-8 -*-
"""b765_window.py -- THE SPLINE WINDOW, COMPUTED AND BANKED AS DATA: (R375)(5)(c), [G2] PART TWO, H-SPLINE-WINDOW (relay
data/b765_registration.txt, committed alone at 7907161c before any dispatch and before this tool's run).

### Carried from tools/b667_epstein_certify.py: every value a ball (python-flint arb/acb) at a stated precision, every constant a ball
### (pi, Euler's gamma, log 23, the logarithms of rationals), the result a ball read against 0 by the whole ball. Nothing of b667's zeros
### is carried: nothing here is computed at a zero, and no bank of zeros is opened.
### THE WINDOW. The kernel's witnessH stands on push-b763-arith alone (data/b765_misses.txt (5)); the tool takes the window that
### data/b709_grid.txt was computed at: b709's N window (tools/b709_grid.py _window, imported unedited) at width 32, its support
### [-log 32, log 32], its frequency the grid's own, read by name and never printed. Its control: the banked S_NN at :426 and :439.
### THE OBJECT ([G2] PART TWO): S = P - PR + A at k the autocorrelation of h(v) = e^(v/2) H(e^v), H(y) = SUM_{j=M}^{1024M-4} c_j B(M y - j),
### B the cubic B-spline on [0, 4] with integer knots, c_j the window's value at log y - log 32 times y^(-1/2), y = (j + 2)/M, rounded to d
### significant digits (half to even; refused where the value's ball rounds two ways).
### THE THREE TERMS IN y. With K(x) = INT H(y) H(x y) dy: k(t) = e^(t/2) K(e^t), so n^(-1/2) k(log n) = K(n) and k(0) = K(1) = INT H^2.
###   P  = k^(i/2) + k^(-i/2) = 2 (INT H dy) (INT H(y) dy / y)                           (the kernel's poleTerm, b694's P)
###   PR = SUM_{n=2}^{1023} c(n) n^(-1/2) 2 k(log n) = 2 SUM c(n) K(n), each K(n) an exact rational  (c = Lambda_Q at Q0, Lambda at zeta)
###   A  = (1/2 pi) INT k^(r) bracket(r) dr (b694's bracket), by Gauss's integral for psi, the reading of (R375)(5)(b):
###        J  = INT_0^inf (e^-t k(0) - e^(-t/2) k(t)) / (1 - e^-t) dt = INT_1^inf (k(0) - x K(x)) / (x (x - 1)) dx
###           = INT H(z) INT_0^z (H(z) - H(w)) / (z - w) dw dz
###        Hk = INT_1^inf K(x) / (x + 1) dx = (1/2) INT INT H(y) H(z) / (y + z) dy dz
###        at Q0:   A = 2 k(0) (log(sqrt 23 / (2 pi)) - gamma) + 2 J
###        at zeta: A = J - Hk - (gamma + log(2 pi)) k(0)
### IN THE B-SPLINE BASIS, the knots uniform, so that each pair term reads the indices' difference or sum alone save one banded term:
###   INT H = (1/M) SUM c_j ; INT H/y = SUM c_j rho(j), rho(j) = INT_0^4 B(u) / (u + j) du ; k(0) = (1/M) SUM_d beta(d) C(d)
###   K(n) = (1/M) SUM_e kappa_n(e) Gamma_n(e), kappa_n(e) = INT_0^4 B(u) B(n u - e) du, Gamma_n(e) = SUM_i c_i c_(n i + e)
###   J  = (11/6) k(0) + (1/M) SUM_i SUM_(|d| <= 3) c_i c_(i-d) Lg(i, d) - (1/M) SUM_d lam(d) C(|d|),
###        Lg(i, d) = INT_0^4 B(u) B(u + d) log(u + i) du, lam(d) = INT_0^4 B(u) l(u + d) du,
###        l(v) = (1/6) SUM_(i=0..4) (-1)^i C(4, i) (v - i)_+^3 log(v - i), C(d) = SUM_i c_i c_(i-d)
###   Hk = (1/(2M)) SUM_s nu(s) (c * c)(s), nu(s) = INT_0^8 N_8(v) / (v + s) dv, N_8 = B * B
### Each a sum over unit pieces of a polynomial against log(c + s) or 1/(c + s), in closed form by G_l(c) = INT_0^1 s^l / (c + s) ds
### (G_0 = log((c + 1)/c), G_l = 1/l - c G_(l-1)) and F_l(c) = INT_0^1 s^l log(c + s) ds = (log(1 + c) - G_(l+1)(c)) / (l + 1),
### F_l(0) = -1/(l + 1)^2, at SPREC bits.
### THE TOOL'S OWN CONTROL, beside the registration's two: at a test spline (M = 2 on [1, 8]) every closed form above against a second route
### written apart: K(n), INT H and INT H/y by exact piecewise integration in y; the Mellin transform h^ = M^3 SUM_m D_m a_m^(s+3) /
### (s (s+1) (s+2) (s+3)) at s = 1/2 + i r (D_m the fourth differences of the c_j, a_m = m/M) against INT H at s = 1 and INT H/y at s = 0;
### and A at Q0 and at zeta by the kernel's own definition, (1/pi) INT_0^R h^(r) h^(-r) bracket(r) dr, the tail beyond R bounded.
### Routes, each writing one unit to data/b765_window_units.jsonl (UNTRACKED, appended):
###   control-kernel <rung983 | mid1021_1024>   b709's terms at its N window at that point, at b709's precision, against the banked S_NN
###   control-spline                            the tool's own control above
###   zeta <M> <d>                              the registration's second control: Lambda and zeta's terms; wanted, not below 0
###   cell <M> <d>                              the arithmetic side at Q0 at the window (M, d); refused until the controls stand AS WANTED
###   bank                                      data/b765_window.txt; data/b765_window.json where PART TWO reads HELD and not otherwise
### Each route refuses where this file differs from its blob at the relay's HEAD: committed before its run ((R375)(5)(c), N2).
### Written by the Write tool at b765; it writes only the files it names.
"""
import hashlib
import io
import json
import math
import os
import re
import subprocess
import sys
import time
from decimal import Decimal, ROUND_HALF_EVEN, getcontext
from operator import mul

from flint import acb, arb, ctx, fmpq, fmpz_poly

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b694_witness_terms as W    # noqa: E402  ### Lambda_Q, Lambda and the bracket: imported unedited
import b696_witness_balls as WB   # noqa: E402  ### the precision b709 ran at: imported unedited
import b709_grid as G             # noqa: E402  ### the grid's points, its window and its terms (terms709): imported unedited

ACT = 'b765'
SELF = 'tools/b765_window.py'
UNITS = os.path.join(D, 'b765_window_units.jsonl')     # ### UNTRACKED WRITE: one unit a route, appended
BANK = 'data/b765_window.txt'
JSON_BANK = 'data/b765_window.json'
REG, REG_COMMIT = 'data/b765_registration.txt', '7907161c'
GRID = 'data/b709_grid.txt'
GRID_ROWS = {'rung983': (426, 379), 'mid1021_1024': (439, 392)}   # ### [G2] :50: the two rows read, and no other
KPREC = WB.PREC          # ### 128 bits, b709's
SPREC = 512
YTOP = 1024
SHIFT = 32               # ### log y - log 32: the window's support [-log 32, log 32] onto y in [1, 1024]
REGISTERED = (16, 3)
REPORTED = ((8, 3), (32, 3))
TEST = dict(M=2, ytop=8, c=(3, -1, 4, 1, -5, 9, 2, -6, 5, 3, -5), den=7)   # ### the tool's own control: 11 coefficients, j = 2 .. 12
TEST_R = 1000
CONTROLS = ('control-kernel/rung983', 'control-kernel/mid1021_1024', 'control-spline', 'zeta/16/3')
getcontext().prec = 90


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def bs(x):
    x = arb(x)
    return [x.mid().str(45, radius=False), x.rad().str(5, radius=False)]


def bl(p):
    return arb(p[0], p[1])


def fmt(x, n=12):
    x = arb(x)
    return '%s +- %s' % (x.mid().str(n, radius=False), x.rad().str(3, radius=False))


# ================================================================================ COMMITTED BEFORE ITS RUN
def _git(*a):
    r = subprocess.run(('git', '-C', ROOT) + a, capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').strip()


def self_commit():
    """the commit holding this file as it stands; exits where the working file differs from its blob at HEAD, or HEAD holds none."""
    rc1, blob = _git('rev-parse', 'HEAD:' + SELF)
    rc2, work = _git('hash-object', SELF)
    rc3, st = _git('status', '--porcelain', '--', SELF)
    if rc1 or rc2 or rc3 or blob != work or st:
        sys.exit('### %s DIFFERS FROM ITS BLOB AT THE RELAY`S HEAD, OR HEAD HOLDS NONE -- NOTHING RUN (committed before its run, N2)' % SELF)
    return _git('log', '-1', '--format=%H', '--', SELF)[1][:8]


def self_sha():
    return hashlib.sha256(open(os.path.join(ROOT, SELF), 'rb').read()).hexdigest()[:16]


# ================================================================================ THE UNITS FILE
def units():
    U = {}
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[u['key']] = u
    return U


def put_unit(u, commit):
    u['at'] = utc()
    u['tool'] = dict(commit=commit, sha256=self_sha())
    line = (json.dumps(u, ensure_ascii=False) + NL).encode('utf-8')
    with open(UNITS, 'ab') as fh:
        fh.write(line)


# ================================================================================ EXACT POLYNOMIALS (ascending coefficient lists of fmpq)
def padd(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else fmpq(0)) + (b[i] if i < len(b) else fmpq(0)) for i in range(n)]


def pmul(a, b):
    out = [fmpq(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x != 0:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def pscale(a, c):
    return [x * c for x in a]


def plin(c0, c1, k):
    """(c0 + c1 s)^k."""
    out = [fmpq(1)]
    for _ in range(k):
        out = pmul(out, [fmpq(c0), fmpq(c1)])
    return out


def pcomp(a, c0, c1):
    """a(c0 + c1 y) as a polynomial in y (Horner)."""
    res = [fmpq(0)]
    for x in reversed(a):
        res = padd(pmul(res, [fmpq(c0), fmpq(c1)]), [x])
    return res


def pint(a, lo, hi):
    """INT_lo^hi a(y) dy, exact."""
    lo, hi = fmpq(lo), fmpq(hi)
    tot = fmpq(0)
    for l, x in enumerate(a):
        if x != 0:
            tot += x * (hi ** (l + 1) - lo ** (l + 1)) / (l + 1)
    return tot


# ================================================================================ THE B-SPLINES
def cardinal(m):
    """the cardinal B-spline N_m on [p, p + 1], p = 0 .. m - 1, in the local variable s = u - p: (1/(m-1)!) SUM_(i<=p) (-1)^i C(m, i) (s + p - i)^(m-1)."""
    out = []
    for p in range(m):
        acc = [fmpq(0)] * m
        for i in range(p + 1):
            acc = padd(acc, pscale(plin(p - i, 1, m - 1), fmpq((-1) ** i * math.comb(m, i), math.factorial(m - 1))))
        out.append(acc)
    return out


BETA = cardinal(4)      # ### B, the cubic B-spline on [0, 4]: BETA[q] on [q, q + 1]
N8 = cardinal(8)        # ### N_8 = B * B on [0, 8]
BETA_D = {d: sum((pint(pmul(BETA[q], BETA[q + d]), 0, 1) for q in range(4) if 0 <= q + d <= 3), fmpq(0)) for d in range(-3, 4)}
MU = [[sum((BETA[q][a] / (a + l + 1) for a in range(4)), fmpq(0)) for l in range(4)] for q in range(4)]   # ### INT_0^1 beta_q(s) s^l ds


def pieces_check():
    """the pieces' exact facts, printed before any value: B's local pieces, INT B = 1, INT N_8 = 1, SUM_d beta(d) = 1, beta symmetric."""
    want0 = [fmpq(0), fmpq(0), fmpq(0), fmpq(1, 6)]
    want3 = [fmpq(1, 6), fmpq(-1, 2), fmpq(1, 2), fmpq(-1, 6)]
    ok = dict(b0=BETA[0] == want0, b3=BETA[3] == want3,
              intB=sum((pint(BETA[q], 0, 1) for q in range(4)), fmpq(0)) == 1,
              intN8=sum((pint(N8[p], 0, 1) for p in range(8)), fmpq(0)) == 1,
              beta_sum=sum(BETA_D.values(), fmpq(0)) == 1,
              beta_sym=all(BETA_D[d] == BETA_D[-d] for d in range(4)))
    print('  THE PIECES: %s ; beta(0..3) = %s' % (' ; '.join('%s %s' % kv for kv in ok.items()), [str(BETA_D[d]) for d in range(4)]), flush=True)
    if not all(ok.values()):
        sys.exit('### THE PIECES NOT AS WANTED -- NOTHING COMPUTED')


# ================================================================================ THE WINDOW'S COEFFICIENTS
def round_sig(x, d):
    """x a real ball, rounded to d significant digits (half to even), as a Decimal; None where the ball's two ends round apart."""
    m, r = x.mid(), x.rad()
    lo = Decimal((m - r).str(70, radius=False))
    hi = Decimal((m + r).str(70, radius=False))

    def rd(v):
        if v == 0:
            return v
        return v.quantize(Decimal(1).scaleb(v.adjusted() - d + 1), rounding=ROUND_HALF_EVEN)
    a, b = rd(lo), rd(hi)
    return a if a == b else None


def dec_me(v):
    """a Decimal as (m, e), v = m 10^e."""
    sign, digits, exp = v.as_tuple()
    m = int(''.join(str(x) for x in digits)) if digits else 0
    return (-m if sign else m), int(exp)


def coefficients(M, d, ytop=YTOP):
    """c_j, j = M .. ytop M - 4, as (m, e) with c_j = m 10^e: the window's value at log y - log 32 times y^(-1/2), y = (j + 2)/M, rounded."""
    Wd = G._window('rho0', dict(width=str(SHIFT)), 'N')
    Lf, sf = float(Wd.L.mid()), float(Wd.s.mid())
    out, refused = {}, []
    for j in range(M, ytop * M - 3):
        y = fmpq(j + 2, M)
        u = arb(y / SHIFT).log()
        piece = min(5, max(0, int(math.floor((float(u.mid()) + Lf) / sf))))
        v = Wd.hder(piece, u, 0) / arb(y).sqrt()
        r = round_sig(v, d)
        if r is None:
            refused.append(j)
        else:
            out[j] = dec_me(r)
    return out, refused


def scaled(cm, M, jmax):
    """the coefficients as integers C_j over one power of ten S: c_j = C_j / S."""
    E = max([0] + [-e for (m, e) in cm.values() if m != 0])
    C = [0] * (jmax + 1)
    for j, (m, e) in cm.items():
        C[j] = m * 10 ** (e + E)
    return C, 10 ** E


def coef_hash(cm):
    return hashlib.sha256(json.dumps(sorted([j, m, e] for j, (m, e) in cm.items())).encode('utf-8')).hexdigest()[:16]


# ================================================================================ THE CLOSED FORMS' TABLES
class Tabs:
    """G_l(c), l = 0 .. 8, and F_l(c), l = 0 .. 6, for c = 0 .. cmax at the current precision (G at c = 0 not used)."""

    def __init__(self, cmax):
        self.G = [None] * (cmax + 1)
        self.F = [None] * (cmax + 1)
        self.F[0] = [arb(fmpq(-1, (l + 1) ** 2)) for l in range(7)]
        for c in range(1, cmax + 1):
            g = [arb(fmpq(c + 1, c)).log()]
            for l in range(1, 9):
                g.append(arb(fmpq(1, l)) - c * g[-1])
            lg = arb(c + 1).log()
            self.G[c] = g
            self.F[c] = [(lg - g[l + 1]) / (l + 1) for l in range(7)]


def rho_sum(C, M, jmax, tb):
    """SUM_j C_j rho(j), rho(j) = INT_0^4 B(u) / (u + j) du = SUM_q SUM_l BETA[q][l] G_l(j + q)."""
    BA = [[arb(x) for x in BETA[q]] for q in range(4)]
    tot = arb(0)
    for j in range(M, jmax + 1):
        if C[j]:
            r = arb(0)
            for q in range(4):
                g = tb.G[j + q]
                for l in range(4):
                    if BETA[q][l] != 0:
                        r += BA[q][l] * g[l]
            tot += C[j] * r
    return tot


def band_sum(C, M, jmax, tb):
    """SUM_i SUM_(|d|<=3) C_i C_(i-d) Lg(i, d), Lg(i, d) = SUM_q INT_0^1 beta_q(s) beta_(q+d)(s) log(i + q + s) ds."""
    PI = {}
    for d in range(-3, 4):
        for q in range(4):
            if 0 <= q + d <= 3:
                PI[(d, q)] = [arb(x) for x in pmul(BETA[q], BETA[q + d])]
    tot = arb(0)
    for i in range(M, jmax + 1):
        if not C[i]:
            continue
        for d in range(-3, 4):
            j = i - d
            if j < M or j > jmax or not C[j]:
                continue
            lg = arb(0)
            for q in range(4):
                pi = PI.get((d, q))
                if pi is not None:
                    f = tb.F[i + q]
                    for l in range(7):
                        lg += pi[l] * f[l]
            tot += (C[i] * C[j]) * lg
    return tot


def lam_table(dmax, tb):
    """lam(d), d = -3 .. dmax: (1/6) SUM_i (-1)^i C(4, i) E(d - i), E(e) = INT_0^4 B(u) (u + e)_+^3 log(u + e) du = SUM_q INT_0^1 beta_q(s)
    (s + c)^3 log(s + c) ds over c = q + e >= 0."""
    E = {}
    for e in range(-7, dmax + 1):
        tot = arb(0)
        for q in range(4):
            c = q + e
            if c < 0:
                continue
            f = tb.F[c]
            cq = fmpq(c)
            for l, x in enumerate(pmul(BETA[q], [cq ** 3, 3 * cq ** 2, 3 * cq, fmpq(1)])):
                if x != 0:
                    tot += arb(x) * f[l]
        E[e] = tot
    return {d: sum((E[d - i] * ((-1) ** i * math.comb(4, i)) for i in range(5)), arb(0)) / 6 for d in range(-3, dmax + 1)}


def nu_sum(cc, smin, smax, tb):
    """SUM_s cc(s) nu(s), nu(s) = SUM_p SUM_l N8[p][l] G_l(s + p)."""
    NA = [[arb(x) for x in N8[p]] for p in range(8)]
    tot = arb(0)
    for s_ in range(smin, smax + 1):
        v = cc[s_]
        if not v:
            continue
        g_s = arb(0)
        for p in range(8):
            g = tb.G[s_ + p]
            for l in range(8):
                if N8[p][l] != 0:
                    g_s += NA[p][l] * g[l]
        tot += v * g_s
    return tot


def kn_scaled(C, M, jmax, n):
    """M S^2 K(n) = SUM_e kappa_n(e) Gamma_n(e), exact. Gamma_n(e) = SUM_i C_i C_(n i + e), e = -3 .. 4n - 1; kappa_n(e) = (1/n) SUM_q
    V(q, m, g) over t = q + e = m n + g in [0, 4n), V(q, m, g) = INT_0^1 beta_q(s) beta_m((g + s)/n) ds = SUM_k A(q, m, k) g^k."""
    gam = []
    for e in range(-3, 4 * n):
        i0 = max(M, -((e - M) // n))
        i1 = min(jmax, (jmax - e) // n)
        gam.append(sum(map(mul, C[i0:i1 + 1], C[n * i0 + e:n * i1 + e + 1:n])) if i1 >= i0 else 0)
    gp = [[g ** k for g in range(n)] for k in range(4)]
    nq = fmpq(n)
    tot = fmpq(0)
    for q in range(4):
        for m in range(4):
            A = [sum((BETA[m][j] * math.comb(j, k) * MU[q][j - k] / nq ** j for j in range(k, 4)), fmpq(0)) for k in range(4)]
            base = m * n - q + 3
            sl = gam[base:base + n]
            for k in range(4):
                if A[k] != 0:
                    sk = sum(map(mul, gp[k], sl))
                    if sk:
                        tot += A[k] * sk
    return tot / n


# ================================================================================ THE THREE TERMS AT A SPLINE
def spline_terms(C, S, M, ytop, obj, nlist=None):
    """P, PR and A at the spline H = SUM_j (C_j / S) B(M y - j), j = M .. ytop M - 4, at the current precision."""
    t0 = time.time()
    jmax = ytop * M - 4
    S2M = fmpq(M * S * S)
    dmax = jmax - M
    tb = Tabs(max(jmax + 4, dmax + 4, (2 * jmax + 8) if obj == 'zeta' else 0))
    intH = fmpq(sum(C), M * S)
    intHy = rho_sum(C, M, jmax, tb) / S
    P = 2 * arb(intH) * intHy
    A_ = fmpz_poly(C)
    pc = (A_ * fmpz_poly(list(reversed(C)))).coeffs()

    def cauto(x):
        idx = jmax + x
        return int(pc[idx]) if 0 <= x <= dmax and idx < len(pc) else 0
    k0 = (BETA_D[0] * cauto(0) + 2 * sum((BETA_D[d] * cauto(d) for d in (1, 2, 3)), fmpq(0))) / S2M
    band = band_sum(C, M, jmax, tb)
    lam = lam_table(dmax, tb)
    lamsum = sum((lam[d] * cauto(abs(d)) for d in range(-3, dmax + 1)), arb(0))
    J = arb(fmpq(11, 6) * k0) + (band - lamsum) / arb(S2M)
    eg, pi = arb.const_euler(), arb.pi()
    Hk = None
    if obj == 'q0':
        A = 2 * arb(k0) * ((arb(23).sqrt() / (2 * pi)).log() - eg) + 2 * J
    else:
        cc = [int(x) for x in (A_ * A_).coeffs()]
        Hk = nu_sum(cc, 2 * M, min(2 * jmax, len(cc) - 1), tb) / (2 * arb(S2M))
        A = J - Hk - (eg + (2 * pi).log()) * arb(k0)
    nmax = ytop - 1
    lamn = W.lambda_q(nmax)[0] if obj == 'q0' else W.lambda_z(nmax)
    PR, products, kn = arb(0), 0, {}
    for n in (nlist or range(2, nmax + 1)):
        if nlist is None and lamn[n].is_zero():
            continue
        ks = kn_scaled(C, M, jmax, n)
        kn[n] = ks / S2M
        if n >= 2 and ks != 0 and not lamn[n].is_zero():
            PR += lamn[n] * arb(kn[n])
            products += 1
    PR = 2 * PR
    return dict(P=P, PR=PR, A=A, S=P - PR + A, k0=k0, J=J, Hk=Hk, intH=intH, intHy=intHy, kn=kn, products=products,
                nonzero=sum(1 for j in range(M, jmax + 1) if C[j]), ncoef=jmax - M + 1, seconds=int(time.time() - t0))


# ================================================================================ THE TOOL'S OWN CONTROL: A SECOND ROUTE, WRITTEN APART
def direct(C, S, M, ytop):
    """INT H, INT H/y and K(n), n = 1 .. ytop - 1, by H's pieces in y, each product integrated exactly over the common refinement."""
    jmax = ytop * M - 4
    cs = {j: fmpq(C[j], S) for j in range(M, jmax + 1) if C[j]}
    P = {}
    for k in range(M, jmax + 4):
        acc = [fmpq(0)]
        for r in range(4):
            if (k - r) in cs:
                acc = padd(acc, pscale(pcomp(BETA[r], -k, M), cs[k - r]))
        P[k] = acc
    intH = sum((pint(P[k], fmpq(k, M), fmpq(k + 1, M)) for k in P), fmpq(0))
    intHy = arb(0)
    for k, p in P.items():
        lo, hi = fmpq(k, M), fmpq(k + 1, M)
        tot = fmpq(0)
        for l in range(1, len(p)):
            tot += p[l] * (hi ** l - lo ** l) / l
        intHy += arb(tot) + arb(p[0]) * arb(hi / lo).log()
    K = {}
    for n in range(1, ytop):
        top = fmpq(ytop, n)
        bp = {fmpq(1), top}
        for k in range(M, ytop * M + 1):
            if fmpq(k, M) <= top:
                bp.add(fmpq(k, M))
        for k in range(n * M, ytop * M + 1):
            if fmpq(k, n * M) <= top:
                bp.add(fmpq(k, n * M))
        pts = sorted(b for b in bp if 1 <= b <= top)
        tot = fmpq(0)
        for lo, hi in zip(pts, pts[1:]):
            mid = (lo + hi) / 2
            k1 = int((mid.p * M) // mid.q)
            k2 = int((mid.p * n * M) // mid.q)
            if k1 in P and k2 in P:
                tot += pint(pmul(P[k1], pcomp(P[k2], 0, n)), lo, hi)
        K[n] = tot
    return dict(intH=intH, intHy=intHy, K=K)


def mellin(C, S, M, ytop):
    """h^ by the fourth differences D_m: h^(z) = M^3 SUM_m D_m a_m^(s+3) / (s (s+1) (s+2) (s+3)), s = 1/2 + i z; the four moments
    SUM_m D_m a_m^k (k = 0..3, wanted 0), h^ at s = 1 (INT H), the limit at s = 0 (INT H/y), and the bound |h^| <= Cb / |z|^4."""
    jmax = ytop * M - 4
    cs = [fmpq(C[j], S) if M <= j <= jmax else fmpq(0) for j in range(jmax + 5)]
    Dm = {}
    for m in range(M, jmax + 5):
        v = sum((fmpq((-1) ** i * math.comb(4, i)) * cs[m - i] for i in range(5) if 0 <= m - i <= jmax), fmpq(0))
        if v != 0:
            Dm[m] = v
    moments = [sum((v * fmpq(m, M) ** k for m, v in Dm.items()), fmpq(0)) for k in range(4)]
    M3q = fmpq(M) ** 3
    h_s1 = M3q * sum((v * fmpq(m, M) ** 4 for m, v in Dm.items()), fmpq(0)) / 24
    logs = {m: arb(fmpq(m, M)).log() for m in Dm}
    h_s0 = arb(M3q) * sum((arb(v) * arb(fmpq(m, M)) ** 3 * logs[m] for m, v in Dm.items()), arb(0)) / 6
    Da = {m: arb(v) for m, v in Dm.items()}
    M3 = arb(M3q)
    I = acb(0, 1)

    def hhat(z):
        s_ = acb(0.5) + I * acb(z)
        tot = acb(0)
        for m in Dm:
            tot += Da[m] * ((s_ + 3) * logs[m]).exp()
        return M3 * tot / (s_ * (s_ + 1) * (s_ + 2) * (s_ + 3))
    Cb = M3 * sum((abs(Da[m]) * (arb(7) / 2 * logs[m]).exp() for m in Dm), arb(0))
    return hhat, moments, h_s1, h_s0, Cb


def arch_def(hhat, obj, R, Cb):
    """(1/pi) INT_0^R h^(r) h^(-r) bracket(r) dr by acb.integral per chunk of 4, b694's bracket; the tail beyond R bounded by
    (1/pi) INT_R^inf Cb^2 r^-8 (2 log r + 6) dr (|bracket(r)| <= 2 log r + 6 for r >= 1000, b694's own bound at :269 widened)."""
    f = lambda z, an: hhat(z) * hhat(-z) * W.bracket(obj, z)   # noqa: E731
    tot = acb(0)
    for e in range(0, R, 4):
        tot += acb.integral(f, e, e + 4, rel_tol=arb(2) ** -100, abs_tol=arb(2) ** -100)
    Rr = arb(R)
    tail = Cb * Cb / arb.pi() * (2 * (Rr.log() / (7 * Rr ** 7) + 1 / (49 * Rr ** 7)) + 6 / (7 * Rr ** 7))
    return tot.real / arb.pi() + arb(0, 1) * tail, tail


def control_spline(*a):
    commit = self_commit()
    pieces_check()
    t0 = time.time()
    M, ytop, S = TEST['M'], TEST['ytop'], TEST['den']
    jmax = ytop * M - 4
    C = [0] * (jmax + 1)
    for i, v in enumerate(TEST['c']):
        C[M + i] = v
    if M + len(TEST['c']) - 1 != jmax:
        sys.exit('### THE TEST SPLINE`S COEFFICIENTS DO NOT FILL j = M .. ytop M - 4 -- NOTHING COMPUTED')
    ctx.prec = SPREC
    dr = direct(C, S, M, ytop)
    cl = {obj: spline_terms(C, S, M, ytop, obj, nlist=range(1, ytop)) for obj in ('q0', 'zeta')}
    q = cl['q0']
    k_equal = all(q['kn'][n] == dr['K'][n] for n in range(1, ytop))
    k0_equal = q['k0'] == dr['K'][1]
    inth_equal = q['intH'] == dr['intH']
    inthy_agree = (q['intHy'] - dr['intHy']).contains(0)
    ctx.prec = KPREC
    hhat, moments, h_s1, h_s0, Cb = mellin(C, S, M, ytop)
    moments_zero = all(x == 0 for x in moments)
    s1_equal = h_s1 == dr['intH']
    s0_agree = (h_s0 - dr['intHy']).contains(0)
    rows = {}
    for obj in ('q0', 'zeta'):
        A_def, tail = arch_def(hhat, obj, TEST_R, Cb)
        lamn = W.lambda_q(ytop - 1)[0] if obj == 'q0' else W.lambda_z(ytop - 1)
        PR_def = 2 * sum((lamn[n] * arb(dr['K'][n]) for n in range(2, ytop)), arb(0))
        S_def = 2 * arb(dr['intH']) * dr['intHy'] - PR_def + A_def
        c = cl[obj]
        rows[obj] = dict(A_closed=bs(c['A']), A_def=bs(A_def), tail=bs(tail), A_diff=fmt(c['A'] - A_def, 4),
                         A_agree=bool((c['A'] - A_def).contains(0)), S_closed=bs(c['S']), S_def=bs(S_def),
                         S_agree=bool((c['S'] - S_def).contains(0)))
    checks = dict(K_n_equal=k_equal, k0_equal=k0_equal, intH_equal=inth_equal, intHy_agree=bool(inthy_agree), moments_zero=moments_zero,
                  mellin_s1_equal=s1_equal, mellin_s0_agree=bool(s0_agree), A_q0_agree=rows['q0']['A_agree'], A_zeta_agree=rows['zeta']['A_agree'],
                  S_q0_agree=rows['q0']['S_agree'], S_zeta_agree=rows['zeta']['S_agree'])
    wanted = all(checks.values())
    u = dict(key='control-spline', route='control-spline', M=M, ytop=ytop, c=list(TEST['c']), den=S, R=TEST_R, checks=checks, rows=rows,
             K=[str(dr['K'][n]) for n in range(1, ytop)], wanted=wanted, prec=[SPREC, KPREC], seconds=int(time.time() - t0))
    put_unit(u, commit)
    print('  THE TOOL`S OWN CONTROL, the test spline M %d on [1, %d], %d coefficients over %d: %s' % (M, ytop, len(TEST['c']), S,
          ' ; '.join('%s %s' % kv for kv in checks.items())), flush=True)
    for obj, r in rows.items():
        print('    %-4s A closed %s ; A by the bracket %s (tail %s) ; difference %s ; S closed %s ; S by the second route %s' % (
            obj, fmt(bl(r['A_closed'])), fmt(bl(r['A_def'])), fmt(bl(r['tail']), 3), r['A_diff'], fmt(bl(r['S_closed'])),
            fmt(bl(r['S_def']))), flush=True)
    print('  %s ; %d s' % ('AS WANTED' if wanted else 'NOT AS WANTED', u['seconds']), flush=True)


# ================================================================================ THE REGISTRATION'S FIRST CONTROL: THE KERNEL'S OWN WINDOW
def grid_row(point):
    """data/b709_grid.txt at the point's row, read by its line and no other; its needle and its S_NN."""
    line, idx = GRID_ROWS[point]
    row = None
    with io.open(os.path.join(ROOT, GRID), encoding='utf-8') as fh:
        for i, l in enumerate(fh, 1):
            if i == line:
                row = l.rstrip(chr(13) + NL)
                break
    needle = '  rho0 | %4d | %s ' % (idx, point)
    m = re.search(r'\| S_NN (\S+) \+- (\S+) \|', row or '')
    if row is None or not row.startswith(needle) or m is None:
        sys.exit('### %s :%d DOES NOT OPEN WITH %r OR HOLDS NO S_NN -- NOTHING COMPUTED' % (GRID, line, needle))
    return m.group(1), m.group(2)


def control_kernel(point=None, *a):
    if point not in GRID_ROWS:
        sys.exit('usage: control-kernel <%s>' % ' | '.join(GRID_ROWS))
    commit = self_commit()
    ctx.prec = KPREC
    bmid, brad = grid_row(point)
    banked = arb(bmid, brad)
    pts = {p['name']: p for p in G.grid('rho0')}
    pt = pts[point]
    if pt['i'] != GRID_ROWS[point][1]:
        sys.exit('### THE GRID`S POINT %s HAS INDEX %d, THE BANK`S ROW %d -- NOTHING COMPUTED' % (point, pt['i'], GRID_ROWS[point][1]))
    t0 = time.time()
    r = G.terms709('rho0', pt, 'N', 'q0')
    S = bl(r['S'])
    e6 = int(math.floor(math.log10(abs(float(bmid))))) - 5
    tol = arb(fmpq(1, 2)) * arb(10) ** e6
    agree = bool(abs(S - banked) < tol)
    sign = bool(S > 0) if point == 'rung983' else None
    wanted = agree and sign is not False
    u = dict(key='control-kernel/' + point, route='control-kernel', point=point, line=GRID_ROWS[point][0], index=pt['i'],
             banked=[bmid, brad], P=r['P'], PR=r['PR'], A=r['A'], S=r['S'], k0=r['k0'], prime_terms=r['prime_terms'], nmax=r['nmax'],
             diff=fmt(S - banked, 4), tol='0.5e%d' % e6, agree6=agree, sign_above_0=sign, wanted=wanted, prec=KPREC,
             seconds=int(time.time() - t0))
    put_unit(u, commit)
    print('  THE KERNEL`S OWN WINDOW at %s (%s :%d, index %d): S_NN %s ; banked %s +- %s ; difference %s ; to 6 digits (half a unit of the '
          'sixth, %s) %s%s ; P %s ; PR %s ; A %s ; %s ; %d s' % (
              point, GRID, GRID_ROWS[point][0], pt['i'], fmt(S), bmid, brad, u['diff'], u['tol'], agree,
              (' ; above 0 %s' % sign) if sign is not None else '', fmt(bl(r['P'])), fmt(bl(r['PR'])), fmt(bl(r['A'])),
              'AS WANTED' if wanted else 'NOT AS WANTED', u['seconds']), flush=True)


# ================================================================================ THE SECOND CONTROL AND THE CELLS
def _window_unit(route, M, d, obj):
    commit = self_commit()
    pieces_check()
    ctx.prec = SPREC
    t0 = time.time()
    cm, refused = coefficients(M, d)
    if refused:
        sys.exit('### c_j ROUNDS TWO WAYS AT j = %s -- NOTHING COMPUTED' % refused[:10])
    jmax = YTOP * M - 4
    C, S = scaled(cm, M, jmax)
    r = spline_terms(C, S, M, YTOP, obj)
    u = dict(route=route, M=M, d=d, obj=obj, P=bs(r['P']), PR=bs(r['PR']), A=bs(r['A']), S=bs(r['S']), k0=bs(r['k0']), J=bs(r['J']),
             Hk=bs(r['Hk']) if r['Hk'] is not None else None, intH=str(r['intH']), intHy=bs(r['intHy']), nonzero=r['nonzero'],
             ncoef=r['ncoef'], products=r['products'], scale_exp=len(str(S)) - 1, coef_sha=coef_hash(cm), prec=SPREC,
             seconds=int(time.time() - t0))
    return u, r, commit


def zeta(M=None, d=None, *a):
    M, d = int(M), int(d)
    u, r, commit = _window_unit('zeta', M, d, 'zeta')
    u['key'] = 'zeta/%d/%d' % (M, d)
    u['not_below_0'] = not bool(r['S'] < 0)
    u['wanted'] = u['not_below_0']
    put_unit(u, commit)
    print('  ZETA`S TERMS AT THE WINDOW M %d d %d (Lambda in place of cQ, zeta`s pole and archimedean terms): S %s ; P %s ; PR %s ; A %s ; '
          'k(0) %s ; nonzero c_j %d of %d ; rational products %d ; not below 0 %s ; %s ; %d s' % (
              M, d, fmt(r['S']), fmt(r['P']), fmt(r['PR']), fmt(r['A']), fmt(arb(r['k0'])), r['nonzero'], r['ncoef'], r['products'],
              u['not_below_0'], 'AS WANTED' if u['wanted'] else 'NOT AS WANTED', u['seconds']), flush=True)


def reading_of(S):
    if S < 0:
        return 'HELD'
    if S >= 0:
        return 'REFUTED'
    return 'NOT SCORABLE'


def cell(M=None, d=None, *a):
    M, d = int(M), int(d)
    if (M, d) != REGISTERED and (M, d) not in REPORTED:
        sys.exit('### THE CELLS ARE M %d d %d (registered) AND %s (reported) -- NOTHING COMPUTED' % (REGISTERED + (REPORTED,)))
    U = units()
    missing = [k for k in CONTROLS if k not in U]
    bad = [k for k in CONTROLS if k in U and not U[k]['wanted']]
    if missing or bad:
        sys.exit('### THE CONTROLS BEFORE ANY CELL: MISSING %s ; NOT AS WANTED %s -- NO CELL COMPUTED' % (missing, bad))
    u, r, commit = _window_unit('cell', M, d, 'q0')
    u['key'] = 'cell/%d/%d' % (M, d)
    u['registered'] = (M, d) == REGISTERED
    u['reading'] = reading_of(r['S'])
    u['wanted'] = True
    put_unit(u, commit)
    print('  THE CELL M %d d %d (%s): S %s ; P %s ; PR %s ; A %s ; k(0) %s ; nonzero c_j %d of %d ; rational products %d ; the ball %s ; %d s' % (
        M, d, 'REGISTERED' if u['registered'] else 'REPORTED, unregistered', fmt(r['S']), fmt(r['P']), fmt(r['PR']), fmt(r['A']),
        fmt(arb(r['k0'])), r['nonzero'], r['ncoef'], r['products'], u['reading'], u['seconds']), flush=True)


# ================================================================================ THE BANK
def put_txt(path, L):
    data = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(ROOT, path)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)


def bank(*a):
    commit = self_commit()
    U = units()
    cells = ['cell/%d/%d' % REGISTERED] + ['cell/%d/%d' % x for x in REPORTED]
    missing = [k for k in CONTROLS + tuple(cells) if k not in U]
    bad = [k for k in CONTROLS if k in U and not U[k]['wanted']]
    if missing and not bad:
        sys.exit('### UNITS MISSING %s -- NOTHING BANKED' % missing)
    ctx.prec = SPREC
    L = ['b765 -- THE SPLINE WINDOW COMPUTED AND BANKED AS DATA, (R375)(5)(c): [G2] PART TWO, H-SPLINE-WINDOW (relay %s, committed alone at %s '
         'before any dispatch and before this tool`s run) (%s)' % (REG, REG_COMMIT, utc()), '',
         '### the tool %s, sha256 %s, committed at relay %s before its run (each route refuses where the file differs from its blob at HEAD);'
         % (SELF, self_sha(), commit),
         '### every value a ball (python-flint arb), the cells at %d bits, the kernel`s window at b709`s %d; the result read against 0 by the whole'
         % (SPREC, KPREC),
         '### ball. The window: b709`s N window at width 32 (tools/b709_grid.py _window, imported unedited), the kernel`s witnessH standing on',
         '### push-b763-arith alone (data/b765_misses.txt (5)); its frequency read by name and not printed. Nothing computed at a zero; no bank',
         '### of zeros opened; data/b709_grid.txt read at :426 and :439 alone. The archimedean term by Gauss`s integral for psi (the reading',
         '### of (R375)(5)(b)), in the closed forms of the tool`s head; the tool`s own control checks each against a second route.', '',
         '## THE CONTROLS, BEFORE ANY CELL']
    for pt in GRID_ROWS:
        u = U.get('control-kernel/' + pt)
        if u is None:
            L.append('  the kernel`s own window at %s: NOT RUN' % pt)
            continue
        L.append('  the kernel`s own window at %s (%s :%d, index %d), b709`s terms709: S_NN %s ; banked %s +- %s ; difference %s ; to 6 digits %s%s ; '
                 'P %s ; PR %s ; A %s ; %s ; %d s' % (pt, GRID, u['line'], u['index'], fmt(bl(u['S'])), u['banked'][0], u['banked'][1], u['diff'],
                                                       u['agree6'], (' ; above 0 %s' % u['sign_above_0']) if u['sign_above_0'] is not None else '',
                                                       fmt(bl(u['P'])), fmt(bl(u['PR'])), fmt(bl(u['A'])),
                                                       'AS WANTED' if u['wanted'] else 'NOT AS WANTED', u['seconds']))
    u = U.get('zeta/16/3')
    if u is None:
        L.append('  zeta`s terms at M 16 d 3: NOT RUN')
    else:
        L.append('  zeta`s terms at the window M 16 d 3 (Lambda in place of cQ, zeta`s pole and archimedean terms): S %s ; P %s ; PR %s ; A %s ; '
                 'not below 0 %s ; %s ; %d s' % (fmt(bl(u['S'])), fmt(bl(u['P'])), fmt(bl(u['PR'])), fmt(bl(u['A'])), u['not_below_0'],
                                                 'AS WANTED' if u['wanted'] else 'NOT AS WANTED', u['seconds']))
    u = U.get('control-spline')
    if u is None:
        L.append('  the tool`s own control: NOT RUN')
    else:
        L.append('  the tool`s own control, the test spline M %d on [1, %d], c = %s / %d: %s ; %s ; %d s' % (
            u['M'], u['ytop'], u['c'], u['den'], ' ; '.join('%s %s' % kv for kv in u['checks'].items()),
            'AS WANTED' if u['wanted'] else 'NOT AS WANTED', u['seconds']))
        for obj, r in u['rows'].items():
            L.append('    %-4s A closed %s ; A by the bracket to R %d %s (tail %s) ; difference %s' % (
                obj, fmt(bl(r['A_closed'])), u['R'], fmt(bl(r['A_def'])), fmt(bl(r['tail']), 3), r['A_diff']))
    L += ['', '## THE CELLS']
    for k in cells:
        u = U.get(k)
        if u is None:
            L.append('  %s: NOT RUN' % k)
            continue
        L.append('  M %d d %d (%s): S %s ; P %s ; PR %s ; A %s ; k(0) %s ; nonzero c_j %d of %d ; rational products %d ; the coefficients` sha256 '
                 '%s ; the ball %s ; %d s' % (u['M'], u['d'], 'REGISTERED' if u['registered'] else 'REPORTED, unregistered', fmt(bl(u['S'])),
                                               fmt(bl(u['P'])), fmt(bl(u['PR'])), fmt(bl(u['A'])), fmt(bl(u['k0'])), u['nonzero'], u['ncoef'],
                                               u['products'], u['coef_sha'], u['reading'], u['seconds']))
    reg = U.get(cells[0])
    if bad:
        verdict, ball = 'NOT SCORABLE', None
        sentence = 'NO CELL: the controls not as wanted (%s); [W2] with that reason' % ', '.join(bad)
    else:
        ball = bl(reg['S'])
        verdict = reading_of(ball)
        if verdict == 'HELD':
            sentence = ('At the cubic spline window with knots at the multiples of 1/16 on [1, 1024] and coefficients of 3 digits, the control`s '
                        'arithmetic side is below 0: %s; the window is banked with %d coefficients.' % (fmt(ball), reg['ncoef']))
        elif verdict == 'REFUTED':
            sentence = 'At that window the control`s arithmetic side is not below 0: %s.' % fmt(ball)
        else:
            sentence = 'At that window the ball holds 0 at the tool`s precision: %s.' % fmt(ball)
    L += ['', '## THE READING', '  H-SPLINE-WINDOW: %s' % verdict, '  THE SENTENCE: %s' % sentence]
    if verdict == 'HELD':
        cm, refused = coefficients(*REGISTERED)
        if refused or coef_hash(cm) != reg['coef_sha']:
            sys.exit('### THE COEFFICIENTS RECOMPUTED DIFFER FROM THE CELL`S (sha256 %s, refused %s) -- NOTHING BANKED' % (coef_hash(cm), refused[:5]))
        M = REGISTERED[0]
        js = dict(act=ACT, registration='relay %s (%s), PART TWO, H-SPLINE-WINDOW' % (REG, REG_COMMIT), tool=dict(path=SELF, commit=commit, sha256=self_sha()),
                  h='h(v) = e^(v/2) H(e^v)', H='H(y) = SUM_{j=%d}^{%d} c_j B(%d y - j)' % (M, YTOP * M - 4, M),
                  B='the cubic B-spline on [0, 4] with integer knots', k='the autocorrelation of h', M=M, d=REGISTERED[1], support=[1, YTOP],
                  window='c_j = the value at y = (j + 2)/%d of y^(-1/2) times b709`s N window at width 32 at log y - log 32, rounded to %d significant digits '
                         '(half to even)' % (M, REGISTERED[1]),
                  S=reg['S'], P=reg['P'], PR=reg['PR'], A=reg['A'], k0=reg['k0'], prec=SPREC, ncoef=len(cm), nonzero=reg['nonzero'],
                  coef_sha=reg['coef_sha'],
                  coefficients=[[j, '%de%d' % (m, e), str(fmpq(m) * fmpq(10) ** e if e >= 0 else fmpq(m, 10 ** -e))] for j, (m, e) in sorted(cm.items())])
        data = json.dumps(js, ensure_ascii=False, indent=1)
        L.append('  %s: written, %d coefficients as rationals, sha256 %s' % (JSON_BANK, len(cm), hashlib.sha256(data.encode('utf-8')).hexdigest()[:16]))
        put_txt(JSON_BANK, [data])
    else:
        L.append('  %s: not written (PART TWO reads %s)' % (JSON_BANK, verdict))
    put_txt(BANK, L)
    print(NL.join(L), flush=True)


ROUTES = {'control-kernel': control_kernel, 'control-spline': control_spline, 'zeta': zeta, 'cell': cell, 'bank': bank}

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ROUTES:
        sys.exit('usage: b765_window.py <%s> [args]' % ' | '.join(ROUTES))
    ROUTES[sys.argv[1]](*sys.argv[2:])
