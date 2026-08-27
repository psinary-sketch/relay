# -*- coding: utf-8 -*-
"""b205 -- the beta-dichotomy of RRT 2025, implemented from the ODE.

  D_tau - mu :   (x^2 - 1) f'' + 2 x f' + (tau^2 x^2 - mu) f = 0

  psi   : the solution asymptotic to -sin(tau x)/x at +infinity
  y_I   : the analytic local solution at x = 1 with y_I(1) = 1
  beta  : (x^2 - 1) * W(psi, y_I) at x_0 = sqrt(2);  its zeros are the eigenvalues
  alpha : at an eigenvalue beta = 0, so psi = alpha * y_I and alpha = psi(x_0)/y_I(x_0)

  EVERY RESOLUTION AXIS IS AN ARGUMENT AND IS QUOTED WITH EVERY NUMBER.
"""
import sys
from mpmath import mp, mpf, mpc, sin, cos, exp, sqrt, pi, matrix

# ----------------------------------------------------------------- y_I at x = 1
def yI_series(mu, tau, ncoef):
    """Frobenius series for the analytic solution at x = 1, y_I(1) = 1.
       t = x - 1;  (t^2+2t) f'' + (2t+2) f' + (tau^2 (t+1)^2 - mu) f = 0.
       Coefficients a_n of f = sum a_n t^n, a_0 = 1."""
    T2 = tau * tau
    a = [mp.one] + [mp.zero] * (ncoef + 4)
    # (t^2+2t)f'' -> sum a_n [ n(n-1) t^n + 2(n+1)n t^n ]
    # (2t+2)f'    -> sum a_n [ 2 n t^n + 2 (n+1) t^n ]
    # (T2(t^2+2t+1) - mu) f -> T2 a_{n-2} + 2 T2 a_{n-1} + (T2 - mu) a_n
    # collect coefficient of t^n:
    #   n(n-1)a_n + 2(n+1)n a_{n+1} + 2 n a_n + 2(n+1)a_{n+1} + T2 a_{n-2} + 2T2 a_{n-1} + (T2-mu)a_n = 0
    #   => 2(n+1)^2 a_{n+1} = -[ (n(n-1) + 2n + T2 - mu) a_n + 2 T2 a_{n-1} + T2 a_{n-2} ]
    for n in range(0, ncoef + 2):
        an   = a[n]
        anm1 = a[n - 1] if n >= 1 else mp.zero
        anm2 = a[n - 2] if n >= 2 else mp.zero
        rhs = -((n * (n - 1) + 2 * n + T2 - mu) * an + 2 * T2 * anm1 + T2 * anm2)
        a[n + 1] = rhs / (2 * (n + 1) ** 2)
    return a[:ncoef + 1]


def yI_eval(mu, tau, x, ncoef):
    a = yI_series(mu, tau, ncoef)
    t = x - 1
    val = mp.zero; der = mp.zero; tp = mp.one
    for n, an in enumerate(a):
        val += an * tp
        if n >= 1:
            der += n * an * (tp / t) if t != 0 else (an if n == 1 else mp.zero)
        tp *= t
    return val, der


# ------------------------------------------------- the divergent series at infinity
def V_coeffs(mu, tau, N, sgn):
    """V_n for  y = e^{sgn*i*tau*x} * x^{-1} * sum V_n x^{-n},  V_0 = 1.
       Substituting into (x^2-1)f'' + 2x f' + (tau^2 x^2 - mu) f = 0 and
       collecting powers of x gives a two-term recurrence; derived here."""
    s = mpc(0, 1) * sgn * tau            # f = e^{s x} x^{-1} u(x),  u = sum V_n x^{-n}
    V = [mp.one] + [mp.zero] * N
    # With f = e^{sx} g, g = x^{-1} u:
    #   (x^2-1)(g'' + 2 s g' + s^2 g) + 2x (g' + s g) + (tau^2 x^2 - mu) g = 0
    #   s^2 = -tau^2  =>  (x^2-1)s^2 + tau^2 x^2 = -s^2*(-1) ... collect:
    #   (x^2-1)g'' + 2s(x^2-1)g' + s^2 x^2 g - s^2 g + 2x g' + 2 s x g + tau^2 x^2 g - mu g = 0
    #   s^2 x^2 + tau^2 x^2 = 0, so:
    #   (x^2-1)g'' + [2s(x^2-1) + 2x] g' + [2 s x - s^2 - mu] g = 0
    # g = sum V_n x^{-n-1}:  g' = sum -(n+1)V_n x^{-n-2}; g'' = sum (n+1)(n+2)V_n x^{-n-3}
    # term A: (x^2-1)g''  -> (n+1)(n+2)V_n x^{-n-1} - (n+1)(n+2)V_n x^{-n-3}
    # term B: 2s x^2 g'   -> -2s(n+1)V_n x^{-n}
    # term C: -2s g'      -> +2s(n+1)V_n x^{-n-2}
    # term D: 2x g'       -> -2(n+1)V_n x^{-n-1}
    # term E: 2s x g      -> 2s V_n x^{-n}
    # term F: -(s^2+mu) g -> -(s^2+mu) V_n x^{-n-1}
    # coefficient of x^{-m}:  from B,E at n=m: -2s(m+1)V_m + 2s V_m = -2 s m V_m
    #   from A,D,F at n=m-1: [ m(m+1) - 2m - (s^2+mu) ] V_{m-1}
    #   from C at n=m-2: 2 s (m-1) V_{m-2}
    #   from A(second) at n=m-3: -(m-2)(m-1) V_{m-3}
    for m in range(1, N + 1):
        acc = mp.zero
        if m - 1 >= 0:
            acc += (m * (m + 1) - 2 * m - (s * s + mu)) * V[m - 1]
        if m - 2 >= 0:
            acc += 2 * s * (m - 1) * V[m - 2]
        if m - 3 >= 0:
            acc += -((m - 2) * (m - 1)) * V[m - 3]
        V[m] = acc / (2 * s * m)
    return V


def psi_at(mu, tau, xm, N):
    """psi and psi' at x = xm from the truncated asymptotic series.
       psi ~ [e^{-i tau x} v^-(x) - e^{+i tau x} v^+(x)] / (2 i x)  ->  -sin(tau x)/x."""
    out = []
    for sgn in (-1, +1):
        V = V_coeffs(mu, tau, N, sgn)
        s = mpc(0, 1) * sgn * tau
        u = mp.zero; du = mp.zero; xp = mp.one
        for n, Vn in enumerate(V):
            u += Vn / (xm ** n)
            du += -n * Vn / (xm ** (n + 1))
        g = u / xm
        dg = du / xm - u / (xm ** 2)
        f = exp(s * xm) * g
        df = exp(s * xm) * (s * g + dg)
        out.append((f, df))
    (fm, dfm), (fp, dfp) = out
    two_i = mpc(0, 2)
    return (fm - fp) / two_i, (dfm - dfp) / two_i


# ---------------------------------------------------- inward Taylor integration
def step_taylor(mu, tau, x, y, dy, h, order):
    """One Taylor step of the ODE (x^2-1)f'' + 2x f' + (tau^2 x^2 - mu) f = 0."""
    T2 = tau * tau
    c = [y, dy]
    A = x * x - 1
    for n in range(0, order):
        # (x^2-1) f'' + 2x f' + (tau^2 x^2 - mu) f = 0 in local variable t (x -> x+t)
        # coefficients are polynomials in t; expand about t=0:
        # A(t) = (x+t)^2-1 = A + 2x t + t^2 ;  B(t) = 2(x+t) = 2x + 2t
        # C(t) = tau^2 (x+t)^2 - mu = (T2 x^2 - mu) + 2 T2 x t + T2 t^2
        s = mp.zero
        if n >= 1:
            s += 2 * x * (n) * (n + 1) * c[n + 1] if False else mp.zero
        # coefficient of t^n in A f'' :
        #   A*(n+2)(n+1)c_{n+2} + 2x*(n+1)n*c_{n+1} + 1*n(n-1)c_n
        # in B f' : 2x*(n+1)c_{n+1} + 2*n*c_n
        # in C f  : (T2 x^2 - mu)c_n + 2 T2 x c_{n-1} + T2 c_{n-2}
        acc = mp.zero
        acc += 2 * x * (n + 1) * n * c[n + 1] if n + 1 < len(c) else mp.zero
        acc += n * (n - 1) * c[n]
        acc += 2 * x * (n + 1) * c[n + 1] if n + 1 < len(c) else mp.zero
        acc += 2 * n * c[n]
        acc += (T2 * x * x - mu) * c[n]
        if n >= 1: acc += 2 * T2 * x * c[n - 1]
        if n >= 2: acc += T2 * c[n - 2]
        c.append(-acc / (A * (n + 2) * (n + 1)))
    val = mp.zero; der = mp.zero; hp = mp.one
    for n, cn in enumerate(c):
        val += cn * hp
        if n >= 1: der += n * cn * hp / h
        hp *= h
    return val, der


def integrate_in(mu, tau, x_from, x_to, y, dy, nsteps, order):
    h = (x_to - x_from) / nsteps
    x = x_from
    for _ in range(nsteps):
        y, dy = step_taylor(mu, tau, x, y, dy, h, order)
        x += h
    return y, dy


# ------------------------------------------------------------------- beta, alpha
def beta_alpha(mu, tau, dps=60, N=None, xmax=None, nsteps=400, order=18, ncoef=260):
    mp.dps = dps
    tau = mpf(tau); mu = mpf(mu)
    if xmax is None: xmax = mpf(40)
    if N is None:    N = 30
    x0 = sqrt(mpf(2))
    p, dp = psi_at(mu, tau, xmax, N)
    p, dp = integrate_in(mu, tau, xmax, x0, p, dp, nsteps, order)
    v, dv = yI_eval(mu, tau, x0, ncoef)
    W = p * dv - dp * v
    beta = (x0 * x0 - 1) * W
    alpha = p / v
    return beta, alpha, p, v
