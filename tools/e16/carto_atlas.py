# -*- coding: utf-8 -*-
"""W-ORD-CARTOGRAPHY act 1 — the atlas's first sheet.

Registered at PLACE-papers 0de616d BEFORE any computation.
DISCLAIMED REGISTER: a computation maps and cannot prove. No sign claim is made.

Weil explicit formula, even test function h on R with Fourier transform hhat:
    sum_gamma hhat(gamma)  =  ARCH + POLE - PRIME
where, writing g for the multiplicative-side bump supported in [1/a, a],
we use the standard pair
    h(u) = int g(e^v) e^{iuv} dv        (Fourier transform of the additive-side bump)
The three channels are computed SEPARATELY, which is the point of the sheet.

E2 is the calibration: for a < sqrt(2) the prime channel is EMPTY (no prime power
n with 1/a <= n <= a when a < 2), so the identity must close on ARCH + POLE alone.
If it does not close, the instrument is wrong and the act says so.
"""
import math, os, sys
import numpy as np

ORD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zeta_ordinates.npy")
GAM = np.load(ORD)                      # 10000 verified ordinates


def bump(a, n=200001):
    """Smooth even (in v = log x) bump, support v in [-L, L], L = log a.
    Returns (v, g) with g a C^inf bump normalised to unit mass in v."""
    L = math.log(a)
    v = np.linspace(-L, L, n)
    t = v / L
    w = np.zeros_like(t)
    m = np.abs(t) < 1.0
    w[m] = np.exp(-1.0 / (1.0 - t[m] ** 2))
    w /= np.trapezoid(w, v)
    return v, w


def hhat(v, w, u):
    """h(u) = int w(v) e^{i u v} dv ; w even => real, even in u."""
    u = np.atleast_1d(np.asarray(u, dtype=np.float64))
    return np.array([np.trapezoid(w * np.cos(uu * v), v) for uu in u])


def zero_side(v, w, gam):
    """sum over gamma (and -gamma) of h(gamma)."""
    return 2.0 * np.sum(hhat(v, w, gam))


def pole_side(v, w):
    """h(i/2) + h(-i/2) = 2 * int w(v) cosh(v/2) dv."""
    return 2.0 * np.trapezoid(w * np.cosh(v / 2.0), v)


def prime_side(a, v, w):
    """sum over prime powers n=p^k in [1/a, a] of 2*Lambda(n)/sqrt(n) * w(log n).
    (w is even in v, so n and 1/n contribute together.)"""
    tot, terms = 0.0, []
    L = math.log(a)
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        k = 1
        while True:
            n = p ** k
            ln = math.log(n)
            if ln > L:
                break
            val = 2.0 * math.log(p) / math.sqrt(n) * float(np.interp(ln, v, w))
            if val != 0.0:
                tot += val
                terms.append((n, val))
            k += 1
    return tot, terms


def arch_side(v, w):
    """The archimedean/Weil W_infty term:
       int w(v) * [ psi_re(1/4 + i u /2) ... ] -- computed in the u-domain as
       (1/2pi) int h(u) * Re psi(1/4 + iu/2) du  minus the log(pi) mass.
       We use the standard form  W_inf(h) = (1/2pi) int h(u) (Re psi(1/4+iu/2) - log pi) du."""
    from mpmath import mp, digamma, mpf, mpc, re as mre
    mp.dps = 20
    U = np.linspace(-400.0, 400.0, 8001)
    H = hhat(v, w, U)
    kern = np.array([float(mre(digamma(mpc(0.25, uu / 2.0)))) - math.log(math.pi) for uu in U])
    return float(np.trapezoid(H * kern, U) / (2.0 * math.pi))


if __name__ == "__main__":
    print("ordinates: %d, last = %.4f" % (len(GAM), GAM[-1]))
    print("%-6s %14s %14s %14s %14s %12s" % ("a", "zero-side", "pole", "arch", "prime", "residual"))
    rows = []
    for a in (1.30, 1.40, 1.41, 1.60, 1.90, 1.99, 2.00, 2.05, 2.20, 2.50, 3.00):
        v, w = bump(a)
        Z = zero_side(v, w, GAM)
        P = pole_side(v, w)
        A = arch_side(v, w)
        PR, terms = prime_side(a, v, w)
        # explicit formula:  Z = P - PR - A     (residual should vanish)
        res = Z - (P - PR - A)
        rows.append((a, Z, P, A, PR, res, terms))
        print("%-6.2f %14.6f %14.6f %14.6f %14.6f %12.4f  %s"
              % (a, Z, P, A, PR, res, "" if not terms else "n=" + ",".join(str(t[0]) for t in terms)))
    print("\n--- E2 CALIBRATION (a < sqrt(2) = 1.4142: prime channel MUST be empty) ---")
    for r in rows:
        if r[0] < math.sqrt(2.0):
            print("  a=%.2f  prime terms: %d  residual: %.4f" % (r[0], len(r[6]), r[5]))
    print("\n--- E3 ONSET ---")
    for r in rows:
        print("  a=%.2f  prime share of |total|: %.4f" % (r[0], abs(r[4]) / max(abs(r[1]), 1e-30)))
