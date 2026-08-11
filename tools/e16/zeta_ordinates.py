# -*- coding: utf-8 -*-
"""Bulk zeta ordinates for W-ORD-SLOPE.

The base of every family point is the first M ordinates of zeta (recovered and
verified exactly against the family run's ten measured indices, 4/4).  Reaching
four decades of B = 2M needs M up to 10000, which mpmath's per-index zetazero
cannot supply in reasonable time.

Strategy:
  * exact mpmath zetazero for k <= NEXACT.  The base's sensitivity to an ordinate
    error eps is ~ n*eps/gamma^2, so the SMALL ordinates are the only ones that
    can move a measured index; those are computed exactly.
  * Riemann-Siegel Z(t) in vectorised float64 above that, with the C0 remainder
    term, scanning for sign changes and bisecting.
  * verification: zero COUNT against Riemann-von Mangoldt N(T), and a random
    sample of computed ordinates cross-checked against exact zetazero.
"""
import math, os, sys, json
import numpy as np

NEXACT = 300
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zeta_ordinates.npy")

def theta_rs(t):
    """Riemann-Siegel theta, asymptotic series."""
    return (t / 2.0) * np.log(t / (2.0 * math.pi)) - t / 2.0 - math.pi / 8.0 \
           + 1.0 / (48.0 * t) + 7.0 / (5760.0 * t ** 3)

def Z(t):
    """Hardy Z(t), Riemann-Siegel with the C0 remainder. Vectorised over t."""
    t = np.asarray(t, dtype=np.float64)
    tau = np.sqrt(t / (2.0 * math.pi))
    K = np.floor(tau).astype(np.int64)
    th = theta_rs(t)
    Kmax = int(K.max())
    ks = np.arange(1, Kmax + 1, dtype=np.float64)
    # main sum: 2 * sum_{k<=K} k^-1/2 cos(theta - t log k)
    ang = th[:, None] - t[:, None] * np.log(ks)[None, :]
    mask = (ks[None, :] <= K[:, None])
    s = 2.0 * np.sum(np.where(mask, np.cos(ang) / np.sqrt(ks)[None, :], 0.0), axis=1)
    # C0 remainder.  Psi(p) = cos(2pi(p^2-p-1/16))/cos(2pi p) has only REMOVABLE
    # singularities (at p = +-1/4 the numerator vanishes too), so Psi is entire and
    # the quotient must NOT be evaluated directly in floating point -- it blows up
    # near p = +-1/4 and manufactures spurious sign changes.  Use its Taylor series.
    p = tau - K                     # fractional part in [0,1) -- the standard argument
    C0 = np.polyval(_PSI_COEF, p)
    s = s + ((-1.0) ** (K - 1)) * tau ** (-0.5) * C0
    return s

def _psi_taylor(order=60):
    """Taylor coefficients of Psi at 0, highest power first (for np.polyval)."""
    from mpmath import mp, cos, pi, taylor
    mp.dps = 60
    f = lambda z: cos(2 * pi * (z * z - z - mp.mpf(1) / 16)) / cos(2 * pi * z)
    c = taylor(f, 0, order)
    return np.array([float(x) for x in c][::-1])

_PSI_COEF = _psi_taylor()

def N_rvm(T):
    return T / (2.0 * math.pi) * math.log(T / (2.0 * math.pi * math.e)) + 7.0 / 8.0

def bisect(a, b, za, zb, tol=1e-10):
    for _ in range(200):
        if b - a < tol:
            break
        m = 0.5 * (a + b)
        zm = float(Z(np.array([m]))[0])
        if (za > 0) == (zm > 0):
            a, za = m, zm
        else:
            b, zb = m, zm
    return 0.5 * (a + b)

def build(M, step=0.01, verbose=True):
    from mpmath import mp, zetazero
    mp.dps = 20
    ne = min(NEXACT, M)
    if verbose: print("  exact zetazero for k = 1..%d ..." % ne, flush=True)
    g = [float(zetazero(k).imag) for k in range(1, ne + 1)]
    if M <= NEXACT:
        return np.array(g)
    t = g[-1] + 1e-6
    Tmax = 1.0
    while N_rvm(Tmax) < M + 30:
        Tmax *= 1.05
    if verbose: print("  Riemann-Siegel scan to T=%.0f (need %d zeros) ..." % (Tmax, M), flush=True)
    CH = 200000
    while len(g) < M and t < Tmax:
        hi = min(t + CH * step, Tmax)
        grid = np.arange(t, hi, step)
        if grid.size < 2: break
        z = Z(grid)
        sgn = np.signbit(z)
        idx = np.nonzero(sgn[:-1] != sgn[1:])[0]
        for i in idx:
            if len(g) >= M: break
            g.append(bisect(grid[i], grid[i + 1], float(z[i]), float(z[i + 1])))
        t = hi
        if verbose: print("    t=%.0f  zeros=%d" % (t, len(g)), flush=True)
    return np.array(g[:M])

def get(M):
    if os.path.exists(CACHE):
        a = np.load(CACHE)
        if len(a) >= M:
            return a[:M]
    a = build(max(M, 10000))
    np.save(CACHE, a)
    return a[:M]

if __name__ == "__main__":
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    a = build(M)
    np.save(CACHE, a)
    print("\nbuilt %d ordinates, last = %.6f" % (len(a), a[-1]))
    print("count check: N_rvm(last) = %.1f  vs  index %d" % (N_rvm(a[-1]), len(a)))
    print("\n--- verification against exact zetazero ---")
    from mpmath import mp, zetazero
    mp.dps = 20
    bad = 0
    for k in (301, 500, 1000, 2500, 5000, 7500, 9999):
        if k > len(a): continue
        ex = float(zetazero(k).imag)
        err = abs(ex - a[k - 1])
        flag = "OK" if err < 1e-3 else "INDEX SHIFT"
        if err >= 1e-3: bad += 1
        print("  k=%-6d exact %.9f   got %.9f   err %.2e  %s" % (k, ex, a[k - 1], err, flag))
    print("  --> %s" % ("ALL OK" if bad == 0 else "%d MISMATCHES" % bad))
