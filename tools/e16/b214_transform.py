# -*- coding: utf-8 -*-
"""b214 -- THE ORIENTATION BITS. F phi / phi computed DIRECTLY.

   ### THE TRANSFORM CONVENTION, ADOPTED FOR THIS ACT AND STATED ONCE:
   ###     (F f)(y) = INTEGRAL f(x) e^{+2 pi i x y} dx
   ### the continuum limit of b19's centered DFT (exp(+2 pi i m_j m_k / N)/sqrt N, self-dual
   ### spacing). ### THE KEYSTONE'S "F^2 = parity, F^4 = 1" DOES NOT PICK THE SIGN -- both signs
   ### satisfy it -- so the sign is ADOPTED here, not derived.

   phi(x) = y_I(x; mu) for x >= 1, 0 for |x| < 1, extended EVEN or ODD.
     EVEN: (F phi)(y) = 2  * INT_1^inf y_I(x) cos(2 pi x y) dx      -- REAL
     ODD : (F phi)(y) = 2i * INT_1^inf y_I(x) sin(2 pi x y) dx      -- PURELY IMAGINARY
   ### AN ODD RATIO WITH A REAL PART IS A DEFECT, NOT A SIGN.

   INT_1^X by quadrature; INT_X^inf ANALYTICALLY from the asymptotic form, by the same
   integration-by-parts tail b210 built, with its truncation term quoted.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, mpc, sqrt, pi, cos, sin, exp, fabs, factorial
from b205_prolate import yI_series, yI_eval, V_coeffs
from b210_wronskian import taylor_coeffs, _poly_val_der, _osc_tail
from b212_odd import beta_alpha_parity, refine, scan_roots

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

XS = mpf('2.5')          # Frobenius series used on [1, XS]; ODE march beyond


# ------------------------------------------------------------------ y_I, dense
def series_eval(a, x):
    """### THE FROBENIUS SERIES EVALUATED FROM PRECOMPUTED COEFFICIENTS.
       yI_eval recomputes the whole recurrence on every call, which made the
       [1, XS] quadrature the run's bottleneck. ### THE COEFFICIENTS DO NOT
       DEPEND ON x, SO THEY ARE COMPUTED ONCE."""
    t = x - 1
    val = mp.zero; tp = mp.one
    for an in a:
        val += an * tp
        tp *= t
    return val


def yI_blocks(mu, tau, X, nsteps, order, ncoef):
    """March y_I outward from XS to X, keeping each step's Taylor coefficients."""
    y, dy = yI_eval(mu, tau, XS, ncoef)
    h = (X - XS) / nsteps
    blocks = []
    x = XS
    for _ in range(nsteps):
        c = taylor_coeffs(mu, tau, x, y, dy, order)
        blocks.append((x, c))
        y, dy = _poly_val_der(c, h)
        x += h
    return blocks, h


def yI_at(mu, tau, x, blocks, h, ncoef):
    if x <= XS:
        return yI_eval(mu, tau, x, ncoef)[0]
    k = int((x - XS) / h)
    if k >= len(blocks):
        k = len(blocks) - 1
    x0, c = blocks[k]
    t = x - x0
    val = mp.zero; tp = mp.one
    for cn in c:
        val += cn * tp
        tp *= t
    return val


# ------------------------------------------------- exact product integral on one step
def _trig_taylor(A, B, h, M, which):
    """Taylor coefficients d_m of cos/sin(A + B t) about t = 0."""
    d = []
    Bp = mp.one
    for m in range(M + 1):
        ph = A + m * pi / 2
        d.append(Bp * (cos(ph) if which == 'cos' else sin(ph)) / factorial(m))
        Bp *= B
    return d


def _prod_integral(c, d, h):
    """INT_0^h (sum c_n t^n)(sum d_m t^m) dt, exactly from the coefficients."""
    tot = mp.zero
    for n, cn in enumerate(c):
        if cn == 0:
            continue
        for m, dm in enumerate(d):
            tot += cn * dm * h ** (n + m + 1) / (n + m + 1)
    return tot


# ------------------------------------------------------------------ the tail
def _tail(mu, tau, X, N, y, alpha, parity):
    """INT_X^inf y_I(x) * (e^{2 pi i x y} -+ e^{-2 pi i x y}) dx, assembled from the
       asymptotic form of psi. Returns (value, truncation bound)."""
    Vm = V_coeffs(mu, tau, N, -1)
    Vp = V_coeffs(mu, tau, N, +1)
    tp = tau          # ### THE FREQUENCY IS tau, NOT 2 pi. At Lambda = 1 they coincide;
                      # ### at Lambda != 1 they do not, and G-SONIN caught the difference.
    a1, a2, a3, a4 = tp * (y - 1), tp * (y + 1), -tp * (y + 1), -tp * (y - 1)
    tot = mp.zero
    bd = mp.zero
    for n in range(len(Vm)):
        s = n + 1
        T1, b1 = _osc_tail(a1, s, X)
        T2, b2 = _osc_tail(a2, s, X)
        T3, b3 = _osc_tail(a3, s, X)
        T4, b4 = _osc_tail(a4, s, X)
        if parity == 'even':
            # psi = (1/2i) sum [ Vm e^{-2pi i x} - Vp e^{+2pi i x} ] x^{-n-1}
            # contribution to  INT psi (e^{+..} + e^{-..})
            term = (Vm[n] * T1 - Vp[n] * T2 + Vm[n] * T3 - Vp[n] * T4) / mpc(0, 2)
            bnd = (abs(Vm[n]) * (b1 + b3) + abs(Vp[n]) * (b2 + b4)) / 2
        else:
            # psi_odd = -(1/2) sum [ Vm e^{-2pi i x} + Vp e^{+2pi i x} ] x^{-n-1}
            # contribution to  INT psi_odd (e^{+..} - e^{-..})
            term = -(Vm[n] * T1 + Vp[n] * T2 - Vm[n] * T3 - Vp[n] * T4) / 2
            bnd = (abs(Vm[n]) * (b1 + b3) + abs(Vp[n]) * (b2 + b4)) / 2
        tot += term
        bd += bnd
    return tot / alpha, bd / abs(alpha)


# ------------------------------------------------------------------ F phi
def Fphi(mu, tau, y, parity, alpha, blocks, h, X, N, ncoef, order, M=36, nsub=64, Lam=None):
    """(F phi)(y) under the adopted convention. Returns (value, tail, tail bound)."""
    which = 'cos' if parity == 'even' else 'sin'
    tp = tau                       # ### frequency tau (= 2 pi Lambda^2)
    if Lam is None:
        Lam = sqrt(tau / (2 * pi))  # ### the physical transform carries a factor Lambda

    # --- [1, XS] : Frobenius series, subdivided, Gauss-Legendre via mp.quad
    seg = (XS - 1) / nsub
    accA = mp.zero
    ser = yI_series(mu, tau, ncoef)          # ### COMPUTED ONCE, NOT PER NODE
    for i in range(nsub):
        a = 1 + i * seg
        accA += mp.quad(lambda t: series_eval(ser, t) *
                        (cos(tp * t * y) if which == 'cos' else sin(tp * t * y)),
                        [a, a + seg])

    # --- [XS, X] : per-step exact product of two Taylor series
    accB = mp.zero
    for (x0, c) in blocks:
        d = _trig_taylor(tp * y * x0, tp * y, h, M, which)
        accB += _prod_integral(c, d, h)

    tail, bd = _tail(mu, tau, X, N, y, alpha, parity)

    if parity == 'even':
        return Lam * (2 * (accA + accB) + tail), tail, bd
    return Lam * (mpc(0, 2) * (accA + accB) + tail), tail, bd
