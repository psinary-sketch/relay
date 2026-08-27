# -*- coding: utf-8 -*-
"""b212 -- THE ODD FAMILY. The cosine solution, on the b205 instrument.

   ### NOTHING IS INHERITED FROM THE EVEN FAMILY THAT THE COSINE SOLUTION DOES NOT RE-EARN.
   ### EVERY RESOLUTION AXIS IS AN ARGUMENT AND IS QUOTED WITH EVERY NUMBER.

   psi_even ~ -sin(tau x)/x   =  (e^{-i tau x} u^-  -  e^{+i tau x} u^+) / (2 i x)
   psi_odd  ~ -cos(tau x)/x   = -(e^{-i tau x} u^-  +  e^{+i tau x} u^+) / (2 x)

   ### THE ODD D_tau NORMALIZATION IS NOT QUOTED FROM THE PAPER. RRT sec 4.2.2 states the
   ### D_tau EVEN psi directly; for the odd case the paper says "There is a variant of the
   ### above proposition, replacing W_Lambda by D_tau. It is only a change of notations. WE
   ### LEAVE IT TO THE READER." ### SO THIS NORMALIZATION IS AN EXECUTOR INFERENCE FROM A
   ### DELEGATED VARIANT, AND G-REPRO-ODD BELOW TESTS IT RATHER THAN TRUSTING IT.

   psi_odd^2 = [ 2 u^-u^+ + e^{-2i tau x}(u^-)^2 + e^{+2i tau x}(u^+)^2 ] / (4 x^2)
   ### THE OSCILLATORY PART CARRIES **+** WHERE THE EVEN FAMILY CARRIES **-**; the
   ### non-oscillatory part is the same. That one sign is the whole parity dependence of the
   ### tail, and it is derived here rather than copied.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, mpc, sqrt, pi, exp, cos, sin, fabs
from b205_prolate import V_coeffs, yI_eval, integrate_in
from b210_wronskian import taylor_coeffs, _poly_val_der, _sq_integral, J1_series, _osc_tail

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def psi_parity_at(mu, tau, xm, N, parity):
    out = []
    for sgn in (-1, +1):
        V = V_coeffs(mu, tau, N, sgn)
        s = mpc(0, 1) * sgn * tau
        u = mp.zero; du = mp.zero
        for n, Vn in enumerate(V):
            u += Vn / (xm ** n)
            du += -n * Vn / (xm ** (n + 1))
        g = u / xm
        dg = du / xm - u / (xm ** 2)
        out.append((exp(s * xm) * g, exp(s * xm) * (s * g + dg)))
    (fm, dfm), (fp, dfp) = out
    if parity == 'even':
        return (fm - fp) / mpc(0, 2), (dfm - dfp) / mpc(0, 2)
    return -(fm + fp) / 2, -(dfm + dfp) / 2


def beta_alpha_parity(mu, tau, parity, dps=50, N=30, xmax=40, nsteps=250, order=18, ncoef=260):
    mp.dps = dps
    tau = mpf(tau); mu = mpf(mu)
    x0 = sqrt(mpf(2))
    p, dp = psi_parity_at(mu, tau, mpf(xmax), N, parity)
    p, dp = integrate_in(mu, tau, mpf(xmax), x0, p, dp, nsteps, order)
    v, dv = yI_eval(mu, tau, x0, ncoef)
    beta = ((x0 * x0 - 1) * (p * dv - dp * v)).real
    alpha = (p / v).real
    return beta, alpha


def beta_parity(mu, tau, parity, **ax):
    return beta_alpha_parity(mu, tau, parity, **ax)[0]


# ------------------------------------------------------------------ the tail, per parity
def J3_tail_parity(mu, tau, X, N, parity):
    Vm = V_coeffs(mu, tau, N, -1)
    Vp = V_coeffs(mu, tau, N, +1)

    def conv(A, B):
        out = [mp.zero] * (len(A) + len(B) - 1)
        for i, ai in enumerate(A):
            if ai == 0: continue
            for j, bj in enumerate(B):
                out[i + j] += ai * bj
        return out

    p_, qm, qp = conv(Vm, Vp), conv(Vm, Vm), conv(Vp, Vp)
    nonosc = mp.zero
    for m, pm in enumerate(p_):
        nonosc += pm * X ** (-1 - m) / (1 + m)
    nonosc = nonosc / 2
    # ### THE ONE PARITY-DEPENDENT SIGN, AND IT IS DERIVED IN THE DOCSTRING, NOT COPIED.
    sgn = mp.one if parity == 'odd' else -mp.one
    osc = mp.zero; bound = mp.zero
    for m, qmm in enumerate(qm):
        v, b = _osc_tail(-2 * tau, 2 + m, X); osc += sgn * qmm * v / 4; bound += abs(qmm) * b / 4
    for m, qpp in enumerate(qp):
        v, b = _osc_tail(+2 * tau, 2 + m, X); osc += sgn * qpp * v / 4; bound += abs(qpp) * b / 4
    return nonosc + osc, bound


def norm_integral_parity(mu, tau, alpha, parity, dps, N, xmax, nsteps, order, ncoef, ncoef_int=90):
    mp.dps = dps
    x0 = sqrt(mpf(2))
    p, dp = psi_parity_at(mu, tau, mpf(xmax), N, parity)
    h = (x0 - mpf(xmax)) / nsteps
    x = mpf(xmax); acc = mp.zero; y, dy = p, dp
    for _ in range(nsteps):
        c = taylor_coeffs(mu, tau, x, y, dy, order)
        acc += _sq_integral(c, h)
        y, dy = _poly_val_der(c, h)
        x += h
    J2 = -acc
    J1 = J1_series(mu, tau, alpha, x0, ncoef_int)
    J3, bound = J3_tail_parity(mu, tau, mpf(xmax), N, parity)
    return (J1 + J2 + J3).real, J1.real, J2.real, J3.real, bound


def beta_prime_parity(mu, tau, parity, h, **ax):
    return ((beta_parity(mu + h, tau, parity, **ax)
             - beta_parity(mu - h, tau, parity, **ax)) / (2 * h))


# ------------------------------------------------------------------ roots
def scan_roots(tau, parity, lo, hi, step, ax):
    mp.dps = ax['dps']
    br = []; mu = mpf(hi); prev = None
    while mu > lo:
        b = beta_parity(mu, tau, parity, **ax)
        if prev is not None and (prev[1] > 0) != (b > 0):
            br.append((prev[0], mu))
        prev = (mu, b)
        mu -= step
    return br


def refine(tau, parity, a, b, ax):
    mp.dps = ax['dps']
    lo, hi = mpf(min(a, b)), mpf(max(a, b))
    x0, x1 = lo, hi
    f0 = beta_parity(x0, tau, parity, **ax)
    f1 = beta_parity(x1, tau, parity, **ax)
    tol = mpf(10) ** (-(ax['dps'] - 12))
    for _ in range(60):
        if f1 == f0: break
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        if not (lo <= x2 <= hi): x2 = (lo + hi) / 2
        f2 = beta_parity(x2, tau, parity, **ax)
        x0, f0, x1, f1 = x1, f1, x2, f2
        if fabs(x1 - x0) < tol or f1 == 0: break
    return x1
