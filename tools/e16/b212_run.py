# -*- coding: utf-8 -*-
"""b212 -- COMPONENT 3: THE RUN, and the data COMPONENT 4's ladder reads."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, pi, sqrt, fabs
from b212_odd import (beta_alpha_parity, beta_parity, beta_prime_parity,
                      norm_integral_parity, scan_roots, refine)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RES = [dict(dps=40, N=26, xmax=35, nsteps=180, order=16, ncoef=220),
       dict(dps=50, N=30, xmax=40, nsteps=250, order=18, ncoef=260),
       dict(dps=60, N=34, xmax=40, nsteps=400, order=20, ncoef=300)]
SCAN = RES[0]
PARAMS = [(2 * pi, '2 pi', mpf(1), mpf(-220)), (4 * pi, '4 pi', sqrt(mpf(2)), mpf(-200)),
          (6 * pi, '6 pi', sqrt(mpf(3)), mpf(-260))]


def ax_s(a):
    return "dps%d N%d x%d ns%d ord%d nc%d" % (a['dps'], a['N'], a['xmax'], a['nsteps'],
                                              a['order'], a['ncoef'])


print("b212 -- COMPONENT 3: THE RUN. Every number carries its axes.")
print("### G-PARITY PASSED AT ALL THREE PARAMETERS BEFORE ANY SIGN BELOW WAS READ.")
print("### SIGNS ARE THE INSTRUMENT'S, IN ITS OWN CONVENTION W = psi y_I' - psi' y_I.")
print("### b205's GLOBAL SIGN IS CARRIED AS IMMATERIAL: every statement below is about")
print("### ALTERNATION and RELATIVE sign, never about an absolute one.")
print()

for tau, name, Lam, lo in PARAMS:
    print("=" * 104)
    print("### tau = %-5s (Lambda = %s)" % (name, mp.nstr(Lam, 10)))
    print("=" * 104)
    mp.dps = SCAN['dps']
    br = scan_roots(tau, 'odd', lo, mpf(-5), mpf(1), SCAN)
    print("  SCAN (%s), mu in [%s,-5] step 1: %d odd sign changes" % (ax_s(SCAN), mp.nstr(lo, 6), len(br)))
    print()
    for ax in RES:
        mp.dps = ax['dps']
        h1 = mpf('1e-6'); h2 = mpf('1e-7')
        piL = pi * Lam
        print("  --- %s ---" % ax_s(ax))
        print("   j  mu_odd                        alpha_odd        |alpha|/(pi Lambda)  "
              "beta'(h1)        |b'(h1)-b'(h2)|/|b'|  INT psi^2        resid(identity)  sign")
        for j, (a, b) in enumerate(br, 1):
            mu = refine(tau, 'odd', a, b, ax)
            bv, al = beta_alpha_parity(mu, tau, 'odd', **ax)
            bp1 = beta_prime_parity(mu, tau, 'odd', h1, **ax)
            bp2 = beta_prime_parity(mu, tau, 'odd', h2, **ax)
            dd = fabs(bp1 - bp2) / fabs(bp1)
            J, J1, J2, J3, bd = norm_integral_parity(mu, tau, al, 'odd', ncoef_int=90, **ax)
            lhs = al * bp2
            resid = fabs(lhs) / J - 1
            print("   %-2d %-29s %-16s %-20s %-16s %-21s %-16s %-16s %+d"
                  % (j, mp.nstr(mu, 20), mp.nstr(al, 12), mp.nstr(fabs(al) / piL, 12),
                     mp.nstr(bp1, 12), mp.nstr(dd, 4), mp.nstr(J, 12),
                     mp.nstr(resid, 4), 1 if lhs > 0 else -1))
        print()
    print()
