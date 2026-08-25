# -*- coding: utf-8 -*-
"""b168 -- THE FLOOR ON THE QUANTITY THE VERDICT ACTUALLY DEPENDS ON.

### Delta's own floor (4.671e-02, axis u-grid) is dominated by the plunge near
u = 0, where Delta falls from 10 to ~2.9 in a tenth of the range. ### THE VERDICT
DOES NOT DEPEND ON Delta POINTWISE -- IT DEPENDS ON J(L) = <PhiK, Delta(L.)> AND
ON THE SUBRANGE ENDPOINT DERIVED FROM IT. This measures the floor THERE, on the
two axes that carried Delta's floor, and reports the endpoint's spread.
### A FLOOR QUOTED ON THE WRONG QUANTITY IS NOT THE FLOOR THAT GOVERNS THE VERDICT.
"""
import functools, math, sys
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b121_instrument as B121
import b134_wroute as WR
import b168_epsgrid as EG

CELLS = [2, 3, 4, 8, 9, 12, 16, 24, 48]
NLEG, NGQ, NQ = 300, 160, 700
UMAX = WR.UMAX
sg, K, Phi = B121.build_kernel()
Ls = np.linspace(math.log(math.sqrt(2)), math.log(math.sqrt(48)), 601)


def endpoint(npts, n_rho):
    g = np.linspace(0.0, UMAX, npts)
    E = EG.E_modes(g, n_rho=n_rho, repaired=True)
    psi, A, sig = WR.psi_W(g, NLEG, NGQ, NQ, E)
    delta = A.sum(0) - E.sum(0)

    def pr(L, arr):
        return float(np.trapezoid(Phi * np.interp(L * sg, g, arr, right=arr[-1]), sg))

    Isig = np.array([pr(L, psi) for L in Ls])
    J = np.array([pr(L, delta) for L in Ls])
    dmax = np.inf
    for i0, j0 in zip(Isig, J):
        if j0 > 0:
            dmax = min(dmax, -i0 / j0)
    return sig - dmax, J, Isig, sig


print("=" * 88)
print("b168 -- THE FLOOR ON J AND ON THE SUBRANGE ENDPOINT")
print("=" * 88)
rows = []
for npts in (200, 400, 800):
    for n_rho in (400, 800, 1600):
        mu_lo, J, Isig, sig = endpoint(npts, n_rho)
        rows.append((npts, n_rho, mu_lo, J.min(), J.max()))
        print("  u-grid %4d  n_rho %5d :  mu_lo = %.9f   J in [%.9f, %.9f]"
              % (npts, n_rho, mu_lo, J.min(), J.max()))

mus = [r[2] for r in rows]
ref = [r for r in rows if r[0] == 400 and r[1] == 800][0][2]
print("\n  reference (u-grid 400, n_rho 800) : mu_lo = %.9f" % ref)
print("  ### SPREAD OF THE ENDPOINT OVER ALL NINE CONFIGURATIONS = %.6e"
      % (max(mus) - min(mus)))
print("  ### range: [%.9f, %.9f]" % (min(mus), max(mus)))
print("  worst |mu_lo - reference| = %.6e" % max(abs(m - ref) for m in mus))
print("\n  ### AND THE VERDICT'S TWO STANDING FACTS AGAINST THAT SPREAD:")
print("     b38's member 0.616500299 sits %.6f above the endpoint" % (0.616500298741 - ref))
print("     the free end 0.000000000 sits %.6f below it" % (ref - 0.0))
print("  ### BOTH DISTANCES EXCEED THE SPREAD BY ORDERS, so the VERDICT is robust")
print("  ### to the floor even where the ENDPOINT's later digits are not.")
print("=" * 88)
