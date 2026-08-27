# -*- coding: utf-8 -*-
"""b210 -- G-NORM. The integral's truncation tail, BOUNDED AND QUOTED, and the total
   required to agree at TWO values of X, as the registration demands."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, pi, fabs
from b210_wronskian import norm_integral, beta_real
import b210_run as R

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

mp.dps = 60
print("b210 -- G-NORM: THE TAIL, BOUNDED AND QUOTED; THE TOTAL AT TWO VALUES OF X.")
print("### THE TAIL IS NOT NEGLIGIBLE AND IS NOT DROPPED: at X = 40 it is ~1.2e-2,")
print("### i.e. THIRTEEN ORDERS ABOVE the residual being tested. Dropping it would have")
print("### produced a clean-looking FAILURE.")
print()

CASES = [(2 * pi, '2 pi', mpf(-21), mpf(-20)),
         (2 * pi, '2 pi', mpf(-50.5), mpf(-49.5)),
         (4 * pi, '4 pi', mpf(-40), mpf(-39))]

for tau, name, lo, hi in CASES:
    ax40 = dict(dps=60, N=34, xmax=40, nsteps=400, order=20, ncoef=300)
    mu = R.refine(tau, lo, hi, ax40)
    _, al = beta_real(mu, tau, **ax40)
    print("=" * 96)
    print("tau = %-6s mu = %s   alpha = %s" % (name, mp.nstr(mu, 20), mp.nstr(al, 12)))
    rows = []
    for X, ns in ((40, 400), (60, 600)):
        ax = dict(dps=60, N=34, xmax=X, nsteps=ns, order=20, ncoef=300)
        J, J1, J2, J3, bd, no, osc = norm_integral(mu, tau, al, ncoef_int=90, **ax)
        rows.append((X, ns, J, J1, J2, J3, bd, no, osc))
        print("  X = %-3d ns=%-4d  J1(1..x0) = %s   J2(x0..X) = %s   J3(X..inf) = %s"
              % (X, ns, mp.nstr(J1, 16), mp.nstr(J2, 16), mp.nstr(J3, 12)))
        print("            tail split: non-oscillatory %s   oscillatory %s"
              % (mp.nstr(no, 12), mp.nstr(osc, 8)))
        print("            ### IBP TRUNCATION BOUND ON THE OSCILLATORY TAIL: %s" % mp.nstr(bd, 6))
        print("            TOTAL J = %s" % mp.nstr(J, 20))
    d = fabs(rows[0][2] - rows[1][2]) / fabs(rows[0][2])
    print("  ### G-NORM, TWO VALUES OF X: |J(40) - J(60)| / J = %s" % mp.nstr(d, 6))
    print("  ### VERDICT: %s" % ("PASS" if d < mpf('1e-12') else "### FAIL -- THE TOTAL MOVES WITH X"))
    print()
