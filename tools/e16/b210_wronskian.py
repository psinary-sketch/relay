# -*- coding: utf-8 -*-
"""b210 -- THE WRONSKIAN GATE. Tests the navigator-asserted relation

      alpha_k * beta'(mu_k)  =  s * INTEGRAL_1^inf psi_k^2 dx        (s independent of k)

   on the b205 instrument, UNCHANGED and imported rather than copied.

   ### THE RELATION IS TESTED, NEVER ASSUMED. ### NO DERIVATION IS PERFORMED HERE.
   ### EVERY RESOLUTION AXIS IS AN ARGUMENT AND IS QUOTED WITH EVERY NUMBER.

   The integral is assembled in three pieces, each with its own warrant:
     J1 = INT_1^x0    -- psi = alpha*y_I at an eigenvalue; the Frobenius series squared,
                         integrated term by term. Convergent: |t| <= x0-1 = 0.414 < 2.
     J2 = INT_x0^X    -- the instrument's OWN inward march, with the square of each step's
                         local Taylor polynomial integrated exactly on that step.
     J3 = INT_X^inf   -- the asymptotic series squared. The NON-OSCILLATORY part summed
                         exactly; the OSCILLATORY part by repeated integration by parts,
                         whose last retained term is quoted as the truncation bound.
   ### J3 IS NOT DROPPED. At X = 40, tau = 2pi it is ~1.2e-2 -- four orders above the
   ### residual being tested. A tail dropped here would fake a failure.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mpmath import mp, mpf, mpc, sqrt, pi, exp, sign, fabs
from b205_prolate import beta_alpha, yI_series, V_coeffs, psi_at


# ------------------------------------------------------------------ Taylor step, coefficients kept
def taylor_coeffs(mu, tau, x, y, dy, order):
    """The SAME recurrence as b205_prolate.step_taylor, but returning the coefficients
       so the square can be integrated exactly over the step."""
    T2 = tau * tau
    c = [y, dy]
    A = x * x - 1
    for n in range(0, order):
        acc = mp.zero
        if n + 1 < len(c):
            acc += 2 * x * (n + 1) * n * c[n + 1]
            acc += 2 * x * (n + 1) * c[n + 1]
        acc += n * (n - 1) * c[n]
        acc += 2 * n * c[n]
        acc += (T2 * x * x - mu) * c[n]
        if n >= 1: acc += 2 * T2 * x * c[n - 1]
        if n >= 2: acc += T2 * c[n - 2]
        c.append(-acc / (A * (n + 2) * (n + 1)))
    return c


def _poly_val_der(c, h):
    val = mp.zero; der = mp.zero; hp = mp.one
    for n, cn in enumerate(c):
        val += cn * hp
        if n >= 1: der += n * cn * hp / h
        hp *= h
    return val, der


def _sq_integral(c, h):
    """INT_0^h (sum c_n t^n)^2 dt, exactly from the coefficients."""
    m = len(c)
    conv = [mp.zero] * (2 * m - 1)
    for i, ci in enumerate(c):
        if ci == 0: continue
        for j, cj in enumerate(c):
            conv[i + j] += ci * cj
    tot = mp.zero; hp = h
    for k, bk in enumerate(conv):
        hp = h ** (k + 1)
        tot += bk * hp / (k + 1)
    return tot


def march_with_integral(mu, tau, x_from, x_to, y, dy, nsteps, order):
    """Inward march (as the instrument does) accumulating INT psi^2 along the way."""
    h = (x_to - x_from) / nsteps
    x = x_from; acc = mp.zero
    for _ in range(nsteps):
        c = taylor_coeffs(mu, tau, x, y, dy, order)
        acc += _sq_integral(c, h)
        y, dy = _poly_val_der(c, h)
        x += h
    return y, dy, acc


# ------------------------------------------------------------------------------- J1
def J1_series(mu, tau, alpha, x0, ncoef_int):
    """INT_1^x0 (alpha*y_I)^2 dx from the Frobenius coefficients."""
    a = yI_series(mu, tau, ncoef_int)
    T = x0 - 1
    m = len(a)
    conv = [mp.zero] * (2 * m - 1)
    for i, ai in enumerate(a):
        if ai == 0: continue
        for j, aj in enumerate(a):
            conv[i + j] += ai * aj
    tot = mp.zero
    for k, bk in enumerate(conv):
        tot += bk * T ** (k + 1) / (k + 1)
    return alpha * alpha * tot


# ------------------------------------------------------------------------------- J3
def _osc_tail(a, s, X, maxterms=60):
    """INT_X^inf e^{i a x} x^{-s} dx by repeated integration by parts.
       Returns (value, last_retained_term_magnitude)."""
    ia = mpc(0, 1) * a
    tot = mp.zero
    term = mp.one                      # (s)_k / (ia)^k  accumulator
    last = mp.zero
    for k in range(maxterms):
        contrib = term / ia * X ** (-s - k)
        if k > 0 and abs(contrib) > abs(last):
            break                      # asymptotic series turned; stop before it diverges
        tot += contrib
        last = contrib
        term = term * (s + k) / ia
    return -exp(ia * X) * tot, abs(last)


def J3_tail(mu, tau, X, N):
    """INT_X^inf psi^2 dx from the asymptotic series.
       psi = [e^{-i tau x} u^- - e^{+i tau x} u^+] / (2 i x)
       psi^2 = [ 2 u^-u^+ - e^{-2i tau x}(u^-)^2 - e^{+2i tau x}(u^+)^2 ] / (4 x^2)"""
    Vm = V_coeffs(mu, tau, N, -1)
    Vp = V_coeffs(mu, tau, N, +1)

    def conv(A, B):
        out = [mp.zero] * (len(A) + len(B) - 1)
        for i, ai in enumerate(A):
            if ai == 0: continue
            for j, bj in enumerate(B):
                out[i + j] += ai * bj
        return out

    p  = conv(Vm, Vp)
    qm = conv(Vm, Vm)
    qp = conv(Vp, Vp)

    # non-oscillatory: (1/2) sum_m p_m INT_X^inf x^{-2-m} dx
    nonosc = mp.zero
    for m, pm in enumerate(p):
        nonosc += pm * X ** (-1 - m) / (1 + m)
    nonosc = nonosc / 2

    osc = mp.zero; bound = mp.zero
    for m, qmm in enumerate(qm):
        v, b = _osc_tail(-2 * tau, 2 + m, X); osc += -qmm * v / 4; bound += abs(qmm) * b / 4
    for m, qpp in enumerate(qp):
        v, b = _osc_tail(+2 * tau, 2 + m, X); osc += -qpp * v / 4; bound += abs(qpp) * b / 4
    return nonosc + osc, bound, nonosc, osc


# -------------------------------------------------------------------------- the whole integral
def norm_integral(mu, tau, alpha, dps, N, xmax, nsteps, order, ncoef, ncoef_int=90):
    mp.dps = dps
    x0 = sqrt(mpf(2))
    p, dp = psi_at(mu, tau, xmax, N)
    _, _, acc = march_with_integral(mu, tau, xmax, x0, p, dp, nsteps, order)
    J2 = -acc                                   # march runs inward; flip to INT_x0^X
    J1 = J1_series(mu, tau, alpha, x0, ncoef_int)
    J3, bound, nonosc, osc = J3_tail(mu, tau, mpf(xmax), N)
    return (J1 + J2 + J3).real, J1.real, J2.real, J3.real, bound, nonosc.real, osc.real


# ------------------------------------------------------------------------------- beta'
def beta_prime(mu, tau, h, **ax):
    bp, _, _, _ = beta_alpha(mu + h, tau, **ax)
    bm, _, _, _ = beta_alpha(mu - h, tau, **ax)
    return ((bp - bm) / (2 * h)).real


def beta_real(mu, tau, **ax):
    b, a, p, v = beta_alpha(mu, tau, **ax)
    return b.real, a.real
