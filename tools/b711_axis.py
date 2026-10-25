# -*- coding: utf-8 -*-
"""b711_axis.py -- THE AXIS (e), REPRESENTATION COORDINATES, (R321)(6), AS data/b709_registrations.txt (i) REGISTERED IT (:10-:58, committed at
b709's step zero before any number, unchanged): "S is the quadratic form of a self-adjoint operator T_a on the whole even window space W_a of
support radius a; on an orthonormal basis e_1..e_N of a truncation W_a^N (the Legendre polynomials scaled to [-a, a] and made even, or the source's
prolate basis where it is computable in balls) its matrix S_ij = S(e_i, e_j) is an N x N Hermitian matrix in balls, and ITS LEAST EIGENVALUE
lambda_min(a, N) IS THE SIGN" (:24-:27); the quantity :34-:37, the hypothesis :38-:40, the falsifier :41-:44, the controls :45-:52.

### UNTRACKED WRITE: data/b711_axis_units* -- data/b711_axis_units.jsonl, one unit per (route, width, obj), appended, resumable (b707's form);
### declared for the root route's exclusion list.

### THE RADII: b707's coarse ladder (tools/b707_onset.py RUNGS: the widths sqrt 2, 32, 48, 64, 96, 128, 192), each width w the window's as b694
### gives it -- L = log w, the window supported on [-L, L] in u = log x, k = h * h on [-2L, 2L], a = 2L the radius b707-b709 print.
### THE BASIS (the seat's reading, for the author's strike): G_k(v) = C_2k^(17/2)(v) (1 - v^2)^4, k = 0..15, v = u/L -- the span of the even
### Legendre polynomials P_2k scaled to [-L, L], each carried by the weight (1 - v^2)^4 so that its transform decays as r^-5 and the archimedean
### tail beyond R carries b696's form of bound (a bare polynomial's transform decays as r^-1, its tail at R = 4000 of the order 1e-3 x the
### entries' size, larger than the readings); the Gegenbauer polynomials make the weighted basis orthogonal in L2 (M diagonal, the eigenvalues
### of each truncation unchanged: the same span, nested). The first run took P_2k (1 - v^2)^4 itself; its Gram near 1e-22 at N = 16 left the
### pivots inside their balls (the unit UNDECIDED, superseded by this basis's unit; both in the units file). The form is read in the L2 metric,
### b707's: the generalized eigenproblem S v = lambda M v, M_ij = INT g_i g_j = k_ij(0). The N = 2, 4, 8 matrices are the leading blocks of N = 16.
### THE ENTRIES, each a ball (python-flint) at 192 bits: k_ij(x) = INT g_i(t) g_j(x - t) dt = L SUM_{a,b} g_ia g_jb C_ab(x/L) EXACTLY, C_ab(y) =
### INT_{y-1}^{1} s^a (y - s)^b ds a rational polynomial; PR_ij = SUM_n c(n) n^-1/2 2 k_ij(log n) = 2L SUM_{a,b} g_ia g_jb SUM_m C_ab,m mu_m with
### the moments mu_m = SUM_{n <= w^2} c(n) n^-1/2 (log n / L)^m (c = Lambda_Q by b694's lambda_q at Q0, von Mangoldt at zeta); P_ij =
### 2 ghat_i(i/2) ghat_j(i/2); A_ij = (1/pi) INT_0^R ghat_i ghat_j bracket dr (b694's bracket, acb.integral per chunk of 2 as b696's a_int) with the
### tail beyond R = 4000 bounded by B_i B_j r^-10 (B_k from the boundary sum, b696's alpha and beta) and added to the radius. ghat_k(z) = L J_k(zL),
### J_k(w) = INT_{-1}^{1} G_k(v) e^(i w v) dv: its Taylor series in w (exact moments, the remainder bounded and added) where |w| <= 40, the
### integration-by-parts sum SUM_m (-1)^m [G^(m) e^(iwv)]_{-1}^{1} / (iw)^(m+1) (exact, finite) beyond -- one entire function, two enclosures.
### THE READING per (width, obj, N): POSITIVE DEFINITE beyond its bound where S's Cholesky pivots in balls are all positive; NEGATIVE DIRECTION where a
### rational witness v has v^T S v < 0 in balls; UNDECIDED otherwise; lambda_min enclosed between a certified lower bound (S - l M positive definite
### by its pivots) and the witness's Rayleigh quotient. At a negative reading, the least eigenvector's frequency profile |e^(t)| over t in [0, 40]
### (step 0.01, midpoints), its peak t_peak and the half-width at half maximum.
### THE CONTROLS, printed BEFORE any figure: (C1) the family in the operator's coordinates -- b707's 2 x 2 at its four coarse points (band 128 and
### 192, rho_0 log 2 and 32) recomputed through b707's own windows and reading (tools/b707_onset.py terms707, gram, reading; C and N lie in W_a,
### not in the polynomial truncation) against data/b707_onset.txt :17-:20 as the registration quotes them; beside it the basis's own checks: the
### two enclosures of J_k agreeing where both apply (w = 41, 45), k_00 against acb.integral's convolution at x = L/2 and L, ghat_0(i/2) against
### acb.integral; (C2) the zeta form on W_a^N POSITIVE DEFINITE beyond its bound at every radius read, its tail beside lambda_min; (C3) at a = log 2
### (the width sqrt 2) no prime term enters at Q0 (Lambda_Q(2) = 0) and lambda_min(log 2, N) POSITIVE DEFINITE beyond its bound at every N read.
### Routes: `controls` -> the C1 units and the basis checks; `radius <width> <obj>` -> one radius's 16 x 16 S and M (a unit); `status`;
### `bank [dry]` -> data/b711_axis.txt, data/b711_axis.json, data/b711_axis_hashes.txt. Written by the Write tool at b711; it writes only its units
### file and those banks. Nothing here proves RH or GRH or locates any zero.
"""
import hashlib
import io
import json
import math
import os
import sys
import time

from flint import acb, arb, ctx, fmpq, fmpq_poly

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b707_onset as O7           # noqa: E402  ### b707's windows, terms, gram, reading, ladder: imported unedited
W, WB = O7.W, O7.WB

ACT = 'b711'
REG = 'data/b709_registrations.txt'
PREC = 192
PR_PREC = 512                            # ### the prime side's moments and the k_ij polynomials evaluated there
UNITS = os.path.join(D, '%s_axis_units.jsonl' % ACT)
LADDER = O7.RUNGS                        # ### (('log2', SQRT2), ('32', '32'), ..., ('192', '192'))
NB = 16
NS = (2, 4, 8, 16)
WEIGHT = 4                               # ### (1 - v^2)^4
R_INT = 4000
CHUNK = 2
W1 = 40                                  # ### the Taylor enclosure where |w| <= 40
MJ = 110                                 # ### its terms: w^(2j), j <= 110
OFFLINE = (('rho_0', O7.RHO0_IM), ('the band zero', O7.BAND_IM))
B707 = (('band', '128', '0.88175528'), ('band', '192', '-0.18015272'), ('rho0', 'log2', '3.7190621'), ('rho0', '32', '-0.14004491'))   # ### :46-:47
GRID_NEG = ('32', '192')                 # ### b707's coarse widths where b709's grid families read NEGATIVE DIRECTION (rho_0 at 32, the band at 192)
FAMILY_ONSET_A = (('rho_0', '6.838396011'), ('the band zero', '10.38532711'))   # ### data/b709_report.txt :16
ASTAR = 'a6.838396011'                   # ### the earlier family onset read as a point off the ladder (the hypothesis's second clause, :40)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def bs(x):
    x = arb(x)
    return [x.mid().str(60, radius=False), x.rad().str(5, radius=False)]


def bl(p):
    return arb(p[0], p[1])


def fmt(x, n=10):
    x = arb(x)
    return '%s +- %s' % (x.mid().str(n, radius=False), x.rad().str(3, radius=False))


# ================================================================================ THE BASIS
def gegenbauer(n, lam):
    """C_n^(lam)(v), exact: C_0 = 1, C_1 = 2 lam v, n C_n = 2 v (n + lam - 1) C_{n-1} - (n + 2 lam - 2) C_{n-2}."""
    v = fmpq_poly([0, 1])
    c = [fmpq_poly([1]), fmpq_poly([0, 2 * lam])]
    for m in range(2, n + 1):
        c.append((v * fmpq_poly([2 * (m + lam - 1)]) * c[m - 1] - fmpq_poly([m + 2 * lam - 2]) * c[m - 2]) * fmpq_poly([fmpq(1, m)]))
    return c[n]


def basis():
    """G_k = C_2k^(17/2)(v) (1 - v^2)^4: the even polynomials of degree <= 2k times the weight, orthogonal in L2 on [-1, 1] (Gegenbauer's weight
    (1 - v^2)^(lam - 1/2) = (1 - v^2)^8, the square of the window's weight), so that M is diagonal -- the span of P_2k(v) (1 - v^2)^4 over
    k <= 15 (the first run's basis, whose Gram reached near 1e-22 at N = 16 and left the Cholesky pivots inside their balls)."""
    v = fmpq_poly([0, 1])
    w = (1 - v * v) ** WEIGHT
    return [gegenbauer(2 * k, fmpq(2 * WEIGHT + 1, 2)) * w for k in range(NB)]


GB = basis()
GC = [list(g.coeffs()) for g in GB]
DEG = max(g.degree() for g in GB)


def _ders_at_one(g):
    out, d = [], g
    for _m in range(g.degree() + 1):
        out.append(d(fmpq(1)))
        d = d.derivative()
    return out


GD = [_ders_at_one(g) for g in GB]


def pval(g, z):
    """g(z) at an acb ball, by Horner over the exact coefficients."""
    cs = g.coeffs()
    acc = acb(0)
    for c in reversed(cs):
        acc = acc * z + acb(arb(c))
    return acc


def moment(g, m):
    """INT_{-1}^{1} g(v) v^m dv, exact."""
    tot = fmpq(0)
    for a, c in enumerate(g.coeffs()):
        if c != 0 and (a + m) % 2 == 0:
            tot += c * fmpq(2, a + m + 1)
    return tot


def _series_coeffs():
    out = []
    for g in GB:
        cs = []
        f = fmpq(1)
        for j in range(MJ + 1):
            if j:
                f = f / ((2 * j - 1) * (2 * j))
            cs.append(((-1) ** j) * moment(g, 2 * j) * f)
        out.append(cs)
    return out


SC = None


def jvec(w):
    """J_k(w) for every k, an enclosure of the entire function at the acb ball w."""
    global SC
    w = acb(w)
    up = w.abs_upper()
    if up <= W1:
        if SC is None:
            SC = [[arb(c) for c in cs] for cs in _series_coeffs()]
        u = w * w
        err = 2 * arb(up) ** (2 * MJ + 2) / arb(2 * MJ + 2).fac() * arb(up).exp()
        eb = acb(arb(0, err.mid() + err.rad()), arb(0, err.mid() + err.rad()))
        out = []
        for cs in SC:
            acc = acb(cs[-1])
            for c in reversed(cs[:-1]):
                acc = acc * u + c
            out.append(acc + eb)
        return out
    I = acb(0, 1)
    E, Em = (I * w).exp(), (-I * w).exp()
    iw = 1 / (I * w)
    t = []
    p = iw
    for m in range(DEG + 1):
        t.append(((-1) ** m) * (E - ((-1) ** m) * Em) * p)
        p = p * iw
    out = []
    for dk in GD:
        acc = acb(0)
        for m, dv in enumerate(dk):
            if dv != 0:
                acc += t[m] * arb(dv)
        out.append(acc)
    return out


def ghat(z, L):
    return [acb(L) * j for j in jvec(acb(z) * acb(L))]


def jvec_both(w):
    """the two enclosures at a real w beside each other, for the basis check."""
    global SC
    if SC is None:
        SC = [[arb(c) for c in cs] for cs in _series_coeffs()]
    w = acb(w)
    u = w * w
    ser = []
    for cs in SC:
        acc = acb(cs[-1])
        for c in reversed(cs[:-1]):
            acc = acc * u + c
        ser.append(acc)
    I = acb(0, 1)
    E, Em, iw = (I * w).exp(), (-I * w).exp(), 1 / (I * w)
    bnd = []
    for dk in GD:
        acc, p = acb(0), iw
        for m, dv in enumerate(dk):
            acc += ((-1) ** m) * (E - ((-1) ** m) * Em) * p * arb(dv)
            p = p * iw
        bnd.append(acc)
    return ser, bnd


# ================================================================================ THE CONVOLUTION POLYNOMIALS C_ab(y)
_CAB = {}


def cab(a, b):
    """C_ab(y) = INT_{y-1}^{1} s^a (y - s)^b ds as an fmpq_poly in y."""
    if (a, b) in _CAB:
        return _CAB[(a, b)]
    y = fmpq_poly([0, 1])
    tot = fmpq_poly([0])
    for c in range(b + 1):
        e = a + c + 1
        tot += fmpq_poly([math.comb(b, c) * (-1) ** c]) * y ** (b - c) * (1 - (y - 1) ** e) * fmpq_poly([fmpq(1, e)])
    _CAB[(a, b)] = tot
    return tot


def kpoly(i, j):
    """K_ij(y) with k_ij(L y) = L K_ij(y), exact."""
    tot = fmpq_poly([0])
    for a, ca in enumerate(GC[i]):
        if ca == 0:
            continue
        for b, cb in enumerate(GC[j]):
            if cb == 0:
                continue
            tot += cab(a, b) * fmpq_poly([ca * cb])
    return tot


# ================================================================================ ONE RADIUS
def _tail_consts(obj, R):
    R = arb(R)
    r2 = arb(2).sqrt()
    if obj == 'q0':
        return arb(2), 2 * abs((2 * arb.pi() / arb(23).sqrt()).log()) + 1 / R + (arb(1) / 4 + r2 / 3) / (R * R)
    return arb(1), (arb.pi() / 2).log() + 1 / R + (arb(1) / 8 + 2 * r2 / 3) / (R * R)


def radius_unit(width, obj):
    ctx.prec = PREC
    t0 = time.time()
    L = arb(width).log()
    nmax = int(math.floor(math.exp(2 * float(L.mid())) + 1e-9))
    # ### the moments, at PR_PREC: K_ij's monomial coefficients cancel against y^m (y <= 2, m <= 77) by some 1e40, so the prime side is
    # ### carried at 512 bits and returned to PREC after (the first run of width sqrt 2 at 192 bits left the N = 16 entries with radii near 1e-15)
    ctx.prec = PR_PREC
    L = arb(width).log()
    lam = W.lambda_q(max(nmax, 2))[0] if obj == 'q0' else W.lambda_z(max(nmax, 2))
    mdeg = 2 * DEG + 1
    mu = [arb(0)] * (mdeg + 1)
    nterms = 0
    for n in range(2, nmax + 1):
        if lam[n].is_zero():
            continue
        nterms += 1
        y = arb(n).log() / L
        base = lam[n] / arb(n).sqrt()
        p = arb(1)
        for m in range(mdeg + 1):
            mu[m] += base * p
            p = p * y
    K = {}
    for i in range(NB):
        for j in range(i, NB):
            K[(i, j)] = kpoly(i, j)
    M, PR = {}, {}
    for (i, j), kp in K.items():
        cs = kp.coeffs()
        M[(i, j)] = L * arb(kp(fmpq(0)))
        tot = arb(0)
        for m, c in enumerate(cs):
            if c != 0:
                tot += arb(c) * mu[m]
        PR[(i, j)] = 2 * L * tot
    ctx.prec = PREC
    L = arb(width).log()
    gp = ghat(acb(0, 0.5), L)
    P = dict(((i, j), (2 * gp[i] * gp[j]).real) for (i, j) in K)
    # ### the archimedean integral, every entry per chunk, the transforms memoised per evaluation point
    memo = {}

    def gv(z):
        key = (z.real.mid().str(40), z.real.rad().str(5), z.imag.mid().str(40), z.imag.rad().str(5))
        v = memo.get(key)
        if v is None:
            v = (ghat(z, L), W.bracket(obj, z))
            memo[key] = v
        return v
    A0 = dict(((i, j), acb(0)) for (i, j) in K)
    for e in range(0, R_INT, CHUNK):
        memo.clear()
        for (i, j) in K:
            f = lambda z, an, i=i, j=j: (lambda g: g[0][i] * g[0][j] * g[1])(gv(z))   # noqa: E731
            A0[(i, j)] += acb.integral(f, e, e + CHUNK, rel_tol=arb(2) ** -110, abs_tol=arb(2) ** -110)
    # ### the tail beyond R: |ghat_k(r)| <= B_k r^-5, B_k = 2 L^-4 SUM_m |G^(m)(1)| (R L)^-(m-4)
    RL = arb(R_INT) * L
    B = []
    for dk in GD:
        tot = arb(0)
        for m, dv in enumerate(dk):
            if m >= 4 and dv != 0:
                tot += abs(arb(dv)) / RL ** (m - 4)
        assert all(dk[m] == 0 for m in range(4))
        B.append(2 * tot / L ** 4)
    al, be = _tail_consts(obj, R_INT)
    q = arb(9)
    Rr = arb(R_INT)
    tailf = Rr ** (-9) * (al * (Rr.log() / q + 1 / (q * q)) + be / q) / arb.pi()
    S, A, TL = {}, {}, {}
    for (i, j) in K:
        tl = B[i] * B[j] * tailf
        A[(i, j)] = A0[(i, j)].real / arb.pi() + WB.unit_ball(tl)
        TL[(i, j)] = tl
        S[(i, j)] = P[(i, j)] - PR[(i, j)] + A[(i, j)]
    key = lambda d: dict(('%d,%d' % ij, bs(v)) for ij, v in d.items())   # noqa: E731
    return dict(route='radius', width=width, obj=obj, L=bs(L), a=bs(2 * L), nmax=nmax, prime_terms=nterms, S=key(S), M=key(M), P=key(P), PR=key(PR),
                A=key(A), tail=key(TL), tail_max=bs(max(TL.values(), key=lambda x: float(x.mid()))), B=[bs(b) for b in B], R=R_INT, prec=PREC,
                seconds=int(time.time() - t0))


# ================================================================================ THE READING
def _mat(u, part, n):
    return [[bl(u[part]['%d,%d' % (min(i, j), max(i, j))]) for j in range(n)] for i in range(n)]


def _cholesky_pd(A):
    """True where every pivot of A's Cholesky in balls is certified positive; the pivots' least lower bound."""
    n = len(A)
    Lm = [[arb(0)] * n for _ in range(n)]
    lo = None
    for j in range(n):
        s = A[j][j] - sum((Lm[j][k] * Lm[j][k] for k in range(j)), arb(0))
        if not s > 0:
            return False, s
        lo = s if lo is None or float(s.mid()) < float(lo.mid()) else lo
        Lm[j][j] = s.sqrt()
        for i in range(j + 1, n):
            Lm[i][j] = (A[i][j] - sum((Lm[i][k] * Lm[j][k] for k in range(j)), arb(0))) / Lm[j][j]
    return True, lo


def read(u, n):
    import mpmath
    mpmath.mp.dps = 50
    S, M = _mat(u, 'S', n), _mat(u, 'M', n)
    Sm = mpmath.matrix([[mpmath.mpf(S[i][j].mid().str(55, radius=False)) for j in range(n)] for i in range(n)])
    Mm = mpmath.matrix([[mpmath.mpf(M[i][j].mid().str(55, radius=False)) for j in range(n)] for i in range(n)])
    Lc = mpmath.cholesky(Mm)
    Li = mpmath.inverse(Lc)
    C = Li * Sm * Li.T
    C = (C + C.T) / 2
    ev, Q = mpmath.eigsy(C)
    k0 = min(range(n), key=lambda k: ev[k])
    lam = ev[k0]
    vec = Li.T * Q[:, k0]
    sc = max(abs(vec[i]) for i in range(n))
    r = [fmpq(int(mpmath.nint(vec[i] / sc * mpmath.mpf(2) ** 60)), 2 ** 60) for i in range(n)]
    vs = sum((arb(r[i]) * arb(r[j]) * S[i][j] for i in range(n) for j in range(n)), arb(0))
    vm = sum((arb(r[i]) * arb(r[j]) * M[i][j] for i in range(n) for j in range(n)), arb(0))
    rq = vs / vm
    pd, _piv = _cholesky_pd(S)
    if pd:
        rd = 'POSITIVE DEFINITE BEYOND ITS BOUND'
    elif vs < 0:
        rd = 'NEGATIVE DIRECTION BEYOND ITS BOUND'
    else:
        rd = 'UNDECIDED'
    # ### the certified lower bound: S - l M positive definite
    lower = None
    eps = abs(float(lam)) * 1e-12 + 1e-40
    for _t in range(40):
        l = arb(mpmath.nstr(lam - eps, 40))
        ok, _p = _cholesky_pd([[S[i][j] - l * M[i][j] for j in range(n)] for i in range(n)])
        if ok:
            lower = l
            break
        eps *= 10
    return dict(n=n, reading=rd, lmin_est=mpmath.nstr(lam, 25), lower=bs(lower) if lower is not None else None, rayleigh=bs(rq), witness_S=bs(vs),
                vec=[float(vec[i] / sc) for i in range(n)], ev=[mpmath.nstr(x, 12) for x in ev])


def profile(u, vec):
    """|e^(t)| over [0, 40], step 0.01, from midpoints: the peak and its half-width at half maximum."""
    ctx.prec = 128
    L = bl(u['L'])
    ts = [k / 100.0 for k in range(4001)]
    vals = []
    for t in ts:
        g = ghat(acb(t), L)
        e = sum(vec[k] * float(g[k].real.mid()) for k in range(len(vec)))
        vals.append(abs(e))
    k0 = max(range(len(vals)), key=lambda k: vals[k])
    half = vals[k0] / 2
    lft = next((k for k in range(k0, -1, -1) if vals[k] <= half), None)
    rgt = next((k for k in range(k0, len(vals)) if vals[k] <= half), None)
    hw = ((ts[rgt] if rgt is not None else ts[-1]) - (ts[lft] if lft is not None else 0.0)) / 2
    return dict(t_peak=ts[k0], peak=vals[k0], half_width=hw, left=ts[lft] if lft is not None else None, right=ts[rgt] if rgt is not None else None)


def spectral(u, vec, n):
    """THE SEAT'S CHECK, NOT REGISTERED: the zero side of the explicit formula for the witness g = SUM v_k G_k -- S(g) = SUM_rho ghat(t_rho)^2,
    t_rho = -i (rho - 1/2) -- over tools/b709_pairs.py's certified list to 325 (extended_rows: 'on' rows 2 ghat(gamma)^2 for rho, conj rho; 'off' rows
    4 Re ghat(t)^2 for the quartet; 'ref' rows, the partners 1 - rho of the 'off' rows, not counted again), against v^T S v; the off-line rows'
    largest contributions. The list's tail beyond 325 is not bounded here: the ratio is a reading, not a ball."""
    import b709_pairs as P9
    U9 = P9.units()
    top = P9._complete_to(P9._bands(U9), U9)
    rows, _n_on, _n_off = P9.extended_rows(U9, top)
    ctx.prec = 128
    L = bl(u['L'])
    S = _mat(u, 'S', n)
    vs = sum((arb(vec[i]) * arb(vec[j]) * S[i][j] for i in range(n) for j in range(n)), arb(0))
    on, off, per = arb(0), arb(0), []
    kinds = set()
    for nm, s, t in rows:
        kind = nm.rstrip('0123456789')
        kinds.add(kind)
        if kind == 'ref':
            continue
        g = ghat(acb(t, -(s - arb(1) / 2)), L)
        e = sum((acb(vec[k]) * g[k] for k in range(n)), acb(0))
        if kind == 'off':
            c = 4 * (e * e).real
            off += c
            per.append((float(c.mid()), nm, s.str(8), t.str(8)))
        else:
            assert kind == 'on', kind
            on += 2 * (e * e).real
    per.sort()
    return dict(top=top, kinds=sorted(kinds), vSv=bs(vs), on=bs(on), off=bs(off), ratio=bs((on + off) / vs), largest=per[:3])


# ================================================================================ THE UNITS
def units():
    U = {}
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                x = json.loads(l)
                U[(x['route'], x.get('width', ''), x.get('obj', ''))] = x
    return U


def _membrane(p):
    """(R321)(2)(ii), standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    import b711_record as REC
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)


def put_unit(x):
    x['at'] = utc()
    _membrane(UNITS)
    with open(UNITS, 'ab') as fh:
        fh.write((json.dumps(x, ensure_ascii=False) + NL).encode('utf-8'))


def controls(*a):
    U = units()
    if ('controls', '', '') in U and 'again' not in a:
        print('  the controls are banked (%s)' % U[('controls', '', '')]['at'])
        return
    ctx.prec = 128
    t0 = time.time()
    c1 = []
    for fam, rung, want in B707:
        g0 = dict(O7.FREQS)[fam]
        us = [O7.terms707(O7.window(kd, rung, g0), 'q0') for kd in O7.KINDS]
        Gm, Mm = O7.gram(*us)
        r = O7.reading(Gm, Mm)
        lm = bl(r['lmin'])
        dig = len(want.lstrip('-').replace('.', '').lstrip('0'))
        printed = ('%.' + str(dig - 1) + 'e') % float(lm.mid())
        c1.append(dict(fam=fam, rung=rung, lmin=r['lmin'], reading=r['reading'], registered=want, equal=printed == ('%.' + str(dig - 1) + 'e') % float(want)))
        print('  C1 %s %s lambda_min %s against %s %s' % (fam, rung, fmt(lm), want, c1[-1]['equal']), flush=True)
    ctx.prec = PREC
    ov = []
    for w in (41, 45):
        ser, bnd = jvec_both(arb(w))
        ov.append(dict(w=w, agree=all(s.overlaps(b) for s, b in zip(ser, bnd)), worst=max(float(abs(s - b).mid()) for s, b in zip(ser, bnd))))
    L = arb('32').log()
    kp = kpoly(0, 0)
    kc = []
    g0 = GB[0]
    for xf in (fmpq(1, 2), fmpq(1)):
        x = arb(xf) * L
        f = lambda t, an, x=x: pval(g0, acb(t) / acb(L)) * pval(g0, (acb(x) - acb(t)) / acb(L))   # noqa: E731
        num = acb.integral(f, acb(x - L), acb(L), rel_tol=arb(2) ** -150, abs_tol=arb(2) ** -150).real
        ex = L * arb(kp(xf))
        kc.append(dict(x='%s L' % xf, exact=bs(ex), integral=bs(num), agree=ex.overlaps(num)))
    gp = ghat(acb(0, 0.5), L)[0].real
    fi = lambda t, an: pval(g0, acb(t) / acb(L)) * (-acb(t) / 2).exp()   # noqa: E731
    gi = acb.integral(fi, acb(-L), acb(L), rel_tol=arb(2) ** -150, abs_tol=arb(2) ** -150).real
    pc = dict(series=bs(gp), integral=bs(gi), agree=gp.overlaps(gi))
    x = dict(route='controls', c1=c1, overlap=ov, kconv=kc, ghat_i2=pc, seconds=int(time.time() - t0))
    put_unit(x)
    print('  basis checks: enclosures agree %s ; k_00 %s ; ghat_0(i/2) %s ; %d s' % ([o['agree'] for o in ov], [k['agree'] for k in kc], pc['agree'], x['seconds']))


def radius(width, obj, *a):
    U = units()
    if ('radius', width, obj) in U and 'again' not in a:
        print('  banked: %s %s (%d s)' % (width, obj, U[('radius', width, obj)]['seconds']))
        return
    w = dict(LADDER).get(width, width)
    if width.startswith('a'):
        # ### a point off the ladder named by its radius a (b709's family onset): the width exp(a/2) carried as a 150-digit string
        ctx.prec = PR_PREC
        w = (arb(width[1:]) / 2).exp().mid().str(150, radius=False)
    x = radius_unit(w, obj)
    x['width'] = width
    put_unit(x)
    print('  %s %s: nmax %d, prime terms %d, tail max %s, %d s' % (width, obj, x['nmax'], x['prime_terms'], fmt(bl(x['tail_max']), 3), x['seconds']), flush=True)
    for n in NS:
        r = read(x, n)
        print('    N %2d: %s ; lambda_min ~ %s ; lower %s ; Rayleigh %s' % (n, r['reading'], r['lmin_est'][:14], fmt(bl(r['lower']), 6) if r['lower'] else 'NONE',
                                                                         fmt(bl(r['rayleigh']), 6)), flush=True)


def diag(width, obj, *a):
    """the largest ball radius per part of one radius's unit, and its entry; writes nothing."""
    x = units()[('radius', width, obj)]
    for part in ('P', 'PR', 'A', 'tail', 'M', 'S'):
        d = x[part]
        k = max(d, key=lambda e: float(d[e][1]))
        kk = max(d, key=lambda e: abs(float(d[e][0])))
        print('  %-4s largest radius %s at %s ; largest |mid| %s at %s' % (part, d[k][1], k, d[kk][0][:12], kk))


def status(*a):
    U = units()
    for k, x in sorted(U.items()):
        print('  %s %s %s %s s' % (k[0], k[1], k[2], x.get('seconds')))


def _put(name, data):
    p = os.path.join(D, name)
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)
    return hashlib.sha256(data).hexdigest()


def bank(*a):
    U = units()
    C = U.get(('controls', '', ''))
    if not C:
        sys.exit('### THE CONTROLS ARE NOT BANKED -- NOTHING WRITTEN')
    widths = [w for w, _v in LADDER]
    read_w = [w for w in widths if ('radius', w, 'q0') in U and ('radius', w, 'zeta') in U]
    Lines = ['%s -- COMPONENT 3, (R321)(6): THE AXIS (e), REPRESENTATION COORDINATES, AS %s (i) REGISTERED IT (:10-:58) (%s)' % (ACT, REG, utc()), '',
             '### rows are readings per radius of b707`s coarse ladder: the Weil form on W_a^N, N = 2, 4, 8, 16 (the basis C_2k^(17/2)(v) (1 - v^2)^4, the seat`s',
             '### reading for the author`s strike, tools/b711_axis.py head), its least eigenvalue in the L2 metric in balls. THE CONTROLS FIRST, THEN THE FIGURES.', '']
    c1 = C['c1']
    bc = all(o['agree'] for o in C['overlap']) and all(k['agree'] for k in C['kconv']) and C['ghat_i2']['agree']
    Lines += ['### (C1) THE FAMILY IN THE OPERATOR`S COORDINATES -- b707`s 2 x 2 at its coarse points through b707`s windows and reading (C and N lie in W_a, not in',
              '### the polynomial truncation W_a^N), against data/b707_onset.txt :17-:20 as the registration quotes them (:46-:47):']
    for c in c1:
        Lines.append('  %-5s %-5s | lambda_min %s (%s) | registered %s | equal at its digits %s' % (c['fam'], c['rung'], fmt(bl(c['lmin'])), c['reading'], c['registered'], c['equal']))
    Lines += ['  the basis`s own checks: the two enclosures of J_k agree at w = 41, 45 %s (largest gap %s) ; k_00 against acb.integral`s convolution at x = L/2, L (w = 32) %s ;'
              ' ghat_0(i/2) against acb.integral %s' % ([o['agree'] for o in C['overlap']], ['%.1e' % o['worst'] for o in C['overlap']], [k['agree'] for k in C['kconv']], C['ghat_i2']['agree'])]
    c1ok = all(c['equal'] for c in c1) and bc
    R = {}
    astar = ('radius', ASTAR, 'q0') in U and ('radius', ASTAR, 'zeta') in U
    for w in read_w + ([ASTAR] if astar else []):
        for obj in ('zeta', 'q0'):
            R[(w, obj)] = [read(U[('radius', w, obj)], n) for n in NS]
    Lines += ['', '### (C2) THE ZETA FORM ON W_a^N AT EVERY RADIUS READ (wanted POSITIVE DEFINITE beyond its bound), its tail beside:']
    c2ok = True
    c2under = []
    for w in read_w + ([ASTAR] if astar else []):
        for r in R[(w, 'zeta')]:
            if not r['reading'].startswith('POSITIVE') and abs(float(bl(r['rayleigh']).mid())) < float(bl(U[('radius', w, 'zeta')]['tail_max']).mid()):
                c2under.append('%s N%d' % (w, r['n']))
    for w in read_w + ([ASTAR] if astar else []):
        u = U[('radius', w, 'zeta')]
        rs = R[(w, 'zeta')]
        ok = all(r['reading'].startswith('POSITIVE') for r in rs)
        c2ok = c2ok and ok
        Lines.append('  width %-5s a = %s | %s | lambda_min(16) ~ %s | the tail ball, largest entry %s | %s' % (
            w, fmt(bl(u['a']), 8), ' / '.join('N%d %s' % (r['n'], r['reading'].split()[0]) for r in rs), rs[-1]['lmin_est'][:12], fmt(bl(u['tail_max']), 3),
            'AS WANTED' if ok else '### NOT AS WANTED'))
    if c2under:
        Lines.append('  ### the zeta readings not POSITIVE whose witness Rayleigh quotient lies below the largest entry`s tail ball (the form`s least eigenvalue under the '
                     'resolution of the archimedean tail beyond R = %d, not a sign): %d of them -- %s' % (R_INT, len(c2under), ', '.join(c2under)))
    c3 = None
    if 'log2' in read_w:
        u = U[('radius', 'log2', 'q0')]
        rs = R[('log2', 'q0')]
        lq2 = W.lambda_q(2)[0][2]
        c3 = u['prime_terms'] == 0 and lq2.is_zero() and all(r['reading'].startswith('POSITIVE') for r in rs)
        Lines += ['', '### (C3) THE PROVEN RANGE AT a = log 2: Lambda_Q(2) = %s, prime terms %d ; lambda_min(log 2, N) %s -- %s' % (
            lq2.str(5), u['prime_terms'], ' / '.join('N%d %s %s' % (r['n'], r['reading'].split()[0], r['lmin_est'][:10]) for r in rs), 'AS WANTED' if c3 else '### NOT AS WANTED')]
    Lines += ['### THE CONTROLS: C1 %s ; C2 %s ; C3 %s' % (c1ok, c2ok, c3), '', '### THE FIGURES: the Q0 form on W_a^N per radius (the convergence in N read across the row):']
    onset = None
    for w in read_w:
        u = U[('radius', w, 'q0')]
        rs = R[(w, 'q0')]
        Lines.append('  width %-5s a = %s | prime terms %d | %s' % (w, fmt(bl(u['a']), 8), u['prime_terms'],
                                                                   ' | '.join('N%d %s %s' % (r['n'], r['reading'].split()[0], r['lmin_est'][:11]) for r in rs)))
        Lines.append('        N 16: lambda_min in [%s, %s] (the certified lower bound, the witness`s Rayleigh quotient) ; %s' % (
            fmt(bl(rs[-1]['lower']), 8) if rs[-1]['lower'] else 'NONE', fmt(bl(rs[-1]['rayleigh']), 8), rs[-1]['reading']))
        if onset is None and rs[-1]['reading'].startswith('NEGATIVE'):
            onset = w
    ast_rd = None
    if astar:
        rs = R[(ASTAR, 'q0')]
        ast_rd = rs[-1]['reading']
        Lines += ['  ### the point off the ladder at the earlier family onset a = %s (rho_0`s, data/b709_report.txt :16), read for the hypothesis`s second clause:' % ASTAR[1:],
                  '  a = %s | prime terms %d | %s' % (fmt(bl(U[('radius', ASTAR, 'q0')]['a']), 10), U[('radius', ASTAR, 'q0')]['prime_terms'],
                                                     ' | '.join('N%d %s %s' % (r['n'], r['reading'].split()[0], r['lmin_est'][:11]) for r in rs)),
                  '        N 16: lambda_min in [%s, %s] ; %s' % (fmt(bl(rs[-1]['lower']), 8) if rs[-1]['lower'] else 'NONE', fmt(bl(rs[-1]['rayleigh']), 8), ast_rd)]
    prof = chk = cal = None
    if onset:
        prof = profile(U[('radius', onset, 'q0')], R[(onset, 'q0')][-1]['vec'])
        near = [(nm, float(g)) for nm, g in OFFLINE if abs(prof['t_peak'] - float(g)) <= prof['half_width']]
        Lines += ['', '### THE LEAST RADIUS ON THE LADDER WITH lambda_min(a, 16) NEGATIVE: width %s (a = %s) ; the least eigenvector`s |e^(t)| on [0, 40]: t_peak %.2f, '
                  'half-width %.2f ; the off-line ordinates within one half-width: %s' % (onset, fmt(bl(U[('radius', onset, 'q0')]['a']), 8), prof['t_peak'], prof['half_width'], near or 'NONE')]
        hyp1 = bool(near)
        a_on = float(bl(U[('radius', onset, 'q0')]['a']).mid())
        # ### the ladder bounds the onset on W_a^16 above by its least negative radius; at or below a* where that radius is, or where the point at a*
        # ### itself reads NEGATIVE DIRECTION (a* not read, or read otherwise: not settled by these readings)
        hyp2 = True if (a_on <= min(float(x) for _n, x in FAMILY_ONSET_A) or (ast_rd or '').startswith('NEGATIVE')) else None
        Lines.append('### THE ONSET ON W_a^16: below the ladder`s least negative radius a = %.6f%s' % (
            a_on, (' and at or below a* = %s (the point reads %s)' % (ASTAR[1:], ast_rd)) if astar else ''))
        chk = []
        for nm, w in (('the onset radius', onset),) + ((('the point a*', ASTAR),) if astar else ()):
            sp = spectral(U[('radius', w, 'q0')], R[(w, 'q0')][-1]['vec'], NS[-1])
            chk.append(dict(at=nm, width=w, **sp))
        cal = spectral(U[('radius', onset, 'q0')], R[(onset, 'q0')][0]['vec'], NS[0])
        Lines += ['', '### THE SEAT`S CHECK, NOT REGISTERED: the zero side of the explicit formula for each witness, S(g) = SUM_rho ghat(t_rho)^2 over tools/b709_pairs.py`s',
                  '### certified list to %s (row kinds %s; the list`s tail beyond it unbounded here, so a ratio and not a ball) against v^T S v:' % (cal['top'], cal['kinds']),
                  '  calibration, width %s N %d: v^T S v %s ; on-line %s ; off-line %s ; ratio %s' % (onset, NS[0], fmt(bl(cal['vSv']), 8), fmt(bl(cal['on']), 8),
                                                                                                   fmt(bl(cal['off']), 8), fmt(bl(cal['ratio']), 8))]
        for c in chk:
            Lines.append('  %s, width %s N %d: v^T S v %s ; on-line %s ; off-line %s ; ratio %s ; the largest off-line terms %s' % (
                c['at'], c['width'], NS[-1], fmt(bl(c['vSv']), 8), fmt(bl(c['on']), 8), fmt(bl(c['off']), 8), fmt(bl(c['ratio']), 8),
                '; '.join('%s (sigma %s, t %s) %.4g' % (x[1], x[2], x[3], x[0]) for x in c['largest'])))
    else:
        hyp1 = hyp2 = None
        Lines += ['', '### THE LEAST RADIUS ON THE LADDER WITH lambda_min(a, 16) NEGATIVE: NONE among the radii read (%s)' % ', '.join(read_w)]
    tool_f = [w for w in GRID_NEG if w in read_w and R[(w, 'q0')][-1]['reading'].startswith('POSITIVE')]
    if onset:
        verdict = 'HELD' if (hyp1 and hyp2) else 'REFUTED' if not hyp1 else 'NOT HELD'
    else:
        verdict = 'REFUTED' if tool_f else 'NOT SCORABLE'
    Lines += ['### THE HYPOTHESIS (:38-:40): the peak within one half-width of an off-line ordinate %s ; the operator`s onset at or below the earlier family onset '
              '(a = 6.838396011) %s' % (hyp1, hyp2),
              '### THE FALSIFIER (:41-:44): the peak near no off-line ordinate %s ; lambda_min(a, 16) POSITIVE DEFINITE where b709`s grid reads a family NEGATIVE '
              '(widths %s): %s -- the tool`s falsifier beside the axis`s' % (('FIRED' if hyp1 is False else 'NOT FIRED' if hyp1 else 'NOT READ (no negative radius)'),
                                                                               ', '.join(GRID_NEG), ('FIRED at %s' % tool_f) if tool_f else 'NOT FIRED'), '']
    if chk:
        top0 = chk[0]['largest'][0]
        share = top0[0] / float(bl(chk[0]['vSv']).mid())
        tre = float(top0[3].strip('[').split()[0])
        Lines += ['### THE SEAT`S READING BESIDE THE VERDICT, NOT CHANGING IT (the check above is not registered): at the onset radius the largest zero-side term is %s'
                  ' (sigma %s, t %s), %.4f of v^T S v ; the real-axis peak t_peak %.2f lies %.2f from its ordinate against the half-width %.2f -- the registered profile'
                  ' reads |e^(t)| on the real line, the term sits at the complex point t - i (sigma - 1/2)' % (top0[1], top0[2], top0[3], share, prof['t_peak'],
                                                                                                             abs(prof['t_peak'] - tre), prof['half_width']), '']
    Lines += ['### ### **THE AXIS (e) %s ; RADII READ %d OF %d ; THE ONSET ON W_a^16 %s ; THE TOOL`S FALSIFIER %s ; C1 %s ; C2 %s ; C3 %s.**' % (
        verdict, len(read_w), len(widths), ('width %s, t_peak %.2f, half-width %.2f' % (onset, prof['t_peak'], prof['half_width'])) if onset else 'NONE',
        ('FIRED at %s' % ', '.join(tool_f)) if tool_f else 'NOT FIRED', c1ok, c2ok, c3)]
    j = dict(at=utc(), registration=REG, read=read_w, controls=dict(c1=c1, basis=bc, c2=c2ok, c3=c3),
             readings=dict(('%s/%s' % k, [dict((kk, r[kk]) for kk in ('n', 'reading', 'lmin_est', 'lower', 'rayleigh')) for r in v]) for k, v in R.items()),
             onset=onset, astar=dict(point=ASTAR, reading=ast_rd) if astar else None, profile=prof, hypothesis=[hyp1, hyp2], tool_falsifier=tool_f,
             verdict=verdict, seat_check=dict(calibration=cal, witnesses=chk) if chk else None, c2_under_tail=c2under)
    print(NL.join(Lines))
    if 'dry' in a:
        return
    h1 = _put('%s_axis.txt' % ACT, (NL.join(Lines) + NL).encode('utf-8'))
    h2 = _put('%s_axis.json' % ACT, (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    hu = hashlib.sha256(open(UNITS, 'rb').read()).hexdigest()
    H = ['%s -- THE AXIS`S BANKS, THEIR sha256 (%s)' % (ACT, utc()), '', '  %s  data/%s_axis.txt' % (h1, ACT), '  %s  data/%s_axis.json' % (h2, ACT),
         '  %s  data/%s_axis_units.jsonl (untracked, its units)' % (hu, ACT), '', '### ### **BANKS 2 HASHED, THE UNITS FILE BESIDE.**']
    _put('%s_axis_hashes.txt' % ACT, (NL.join(H) + NL).encode('utf-8'))
    print(H[-1])


ROUTES = dict(controls=controls, radius=radius, status=status, bank=bank, diag=diag)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b711_axis.py controls | radius <width> <obj> | status | bank [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
