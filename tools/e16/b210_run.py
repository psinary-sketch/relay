# -*- coding: utf-8 -*-
"""b210 -- THE RUN. Every number carries its axes."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, pi, sqrt, fabs
from b205_prolate import beta_alpha
from b210_wronskian import beta_real, beta_prime, norm_integral

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RES = [dict(dps=40, N=26, xmax=35, nsteps=180, order=16, ncoef=220),
       dict(dps=50, N=30, xmax=40, nsteps=250, order=18, ncoef=260),
       dict(dps=60, N=34, xmax=40, nsteps=400, order=20, ncoef=300)]
SCAN = dict(dps=40, N=26, xmax=35, nsteps=180, order=16, ncoef=220)


def axes(ax):
    return "dps%d N%d x%d ns%d ord%d nc%d" % (ax['dps'], ax['N'], ax['xmax'],
                                              ax['nsteps'], ax['order'], ax['ncoef'])


def scan(tau, lo, hi, step):
    """### THE SWEEP IS RUN IN THIS ACT, NOT CITED. Brackets from sign changes of beta."""
    mp.dps = SCAN['dps']
    br = []
    mu = mpf(hi); prev = None
    while mu > lo:
        b, _ = beta_real(mu, tau, **SCAN)
        if prev is not None and (prev[1] > 0) != (b > 0):
            br.append((mu, prev[0]))
        prev = (mu, b)
        mu -= step
    return br


def refine(tau, a, b, ax):
    """### SECANT on beta, at the axes given -- superlinear, so the root costs a handful of
       evaluations rather than the ~80 a bisection to this precision would need.
       The bracket is kept and the result CHECKED to lie inside it: a secant that leaves its
       bracket has found something other than the root it was sent for."""
    mp.dps = ax['dps']
    lo, hi = mpf(min(a, b)), mpf(max(a, b))
    x0, x1 = lo, hi
    f0, _ = beta_real(x0, tau, **ax)
    f1, _ = beta_real(x1, tau, **ax)
    tol = mpf(10) ** (-(ax['dps'] - 12))
    for _ in range(60):
        if f1 == f0:
            break
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        if not (lo <= x2 <= hi):                 # fall back to the bracket's midpoint
            x2 = (lo + hi) / 2
        f2, _ = beta_real(x2, tau, **ax)
        x0, f0, x1, f1 = x1, f1, x2, f2
        if fabs(x1 - x0) < tol or f1 == 0:
            break
    return x1


def run_tau(tau, name, lo, hi):
    print("=" * 100)
    print("### tau = %s   (%s)" % (name, mp.nstr(tau, 12)))
    print("=" * 100)
    t0 = time.time()
    br = scan(tau, lo, hi, mpf(1))
    print("  SCAN (%s), mu in [%s, %s] step 1: %d sign changes"
          % (axes(SCAN), lo, hi, len(br)))
    print()

    for ax in RES:
        print("  --- %s ---" % axes(ax))
        print("   k  mu                              alpha            beta'(h1)         beta'(h2)"
              "        |b'(h1)-b'(h2)|/|b'|   INT psi^2         residual        s_k")
        mp.dps = ax['dps']
        h1 = mpf('1e-6'); h2 = mpf('1e-7')
        for k, (a, b) in enumerate(br, 1):
            mu = refine(tau, a, b, ax)
            bv, al = beta_real(mu, tau, **ax)
            bp1 = beta_prime(mu, tau, h1, **ax)
            bp2 = beta_prime(mu, tau, h2, **ax)
            dd = fabs(bp1 - bp2) / fabs(bp1)
            J, J1, J2, J3, bd, no, osc = norm_integral(mu, tau, al, ncoef_int=90, **ax)
            lhs = al * bp2
            resid = fabs(lhs) / J - 1
            s = 1 if lhs > 0 else -1
            print("   %-2d %-31s %-16s %-17s %-16s %-21s %-17s %-15s %+d"
                  % (k, mp.nstr(mu, 20), mp.nstr(al, 12), mp.nstr(bp1, 12),
                     mp.nstr(bp2, 12), mp.nstr(dd, 4), mp.nstr(J, 12),
                     mp.nstr(resid, 4), s))
        print()
    print("  elapsed %.1fs" % (time.time() - t0))
    print()


def tail_report(tau, mu, ax):
    J, J1, J2, J3, bd, no, osc = norm_integral(mu, tau, mpf(1), ncoef_int=90, **ax)
    return J1, J2, J3, bd, no, osc


if __name__ == '__main__':
    mp.dps = 60
    two = 2 * pi
    print("b210 -- THE WRONSKIAN GATE -- THE RAW RUN.")
    print("INSTRUMENT: relay tools/e16/b205_prolate.py (banked b205, UNCHANGED, imported).")
    print("### THE RELATION UNDER TEST IS THE NAVIGATOR'S AND IS TESTED, NEVER ASSUMED.")
    print("### NO ABSOLUTE SIGN CLAIM IS MADE. s_k IS sign(alpha_k * beta'(mu_k)) IN THIS")
    print("### INSTRUMENT'S CONVENTION W = psi*y_I' - psi'*y_I, AND NOWHERE ELSE.")
    print()
    run_tau(2 * pi, "2 pi  (Lambda = 1)", mpf(-220), mpf(-5))
    run_tau(4 * pi, "4 pi  (Lambda = sqrt 2)", mpf(-200), mpf(-5))
    run_tau(6 * pi, "6 pi  (Lambda = sqrt 3)", mpf(-260), mpf(-5))
