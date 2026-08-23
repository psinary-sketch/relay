# -*- coding: utf-8 -*-
"""b110 -- THE CROSSING ACT -- the in-domain SUBSTITUTE for P3.

P3 asked for b109's reduction identity verified AT NEW CELLS. There are no new
cells: b38's grid stops at a^2 = 12 because its epsilon layer does (the rho-grid
is hard-stopped at 12.001 and np.interp clamps silently past it), and no grid
rule exists to continue. See the b110 registration's refusal.

THIS SCRIPT DOES THE REACHABLE THING INSTEAD: it verifies b109's identity at
b38's OWN SIX CELLS, in-domain, using b38's OWN functions (imported, not
re-implemented). This is not a re-run of a recorded verdict -- b38 never checked
this identity; its bank prints W+, W-, f_cell and E2even but not the raw-trace
sums the identity needs. So the components are recomputed to test something new.

THE IDENTITY (b109, derived from b38's definition by exact algebra):
    W+  -  sigma_even * A
      =  [ sum_even tr_n_raw  -  sigma_even * Tr_raw_N ]
       -  [ sum_even E2_n     -  sigma_even * E2_N     ]
Registration: data/b110_registration_2026-08-22.txt.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import qeps_layer as Q

CELLS = B38.CELLS
S4 = B38.S4
NQ, NMODE = B38.TRIPLE[1]          # the headline triple middle, as banked
EPS_NQ, EPS_NG, EPS_NRHO = B38.EPS_NQ, B38.EPS_NG, B38.EPS_NRHO

print("b110 reduction check -- b109's identity at b38's own six cells")
print("instrument: b38_act10 functions, imported; triple (NQ,NMODE) = (%d,%d)" % (NQ, NMODE))
print()

x, w, lam, lam2, xi, xi1, an, dan = Q.layer(EPS_NQ)
t_n = lam2 / (1 - lam2) * xi1 ** 2

rr = np.exp(np.linspace(1e-4, math.log(12.001), EPS_NRHO))
ee_modes = B38.per_mode_eps_grids(rr)

print("%-5s %12s %12s %12s %12s" % ("a^2", "LHS", "RHS", "|LHS-RHS|", "sigma_even"))
worst = 0.0
rows = []
for a, alab in CELLS:
    v, w2, corr, vc, L = B38.family(a)
    A, P, PR = B38.left_side(a, S4, v, w2, corr, vc, L)
    tr = B38.trace_modes(a, corr, vc, L, NQ, NMODE)
    N = len(tr)
    E2n = np.array([B38.e2_of_grid(a, corr, vc, L, rr, ee_modes[n]) for n in range(N)])
    E2N = float(E2n.sum())
    TrN = float(tr.sum())
    resid = TrN - A - E2N
    s = t_n[:N] / float(t_n[:N].sum())
    wmode = tr - E2n - s * resid
    Wp = float(wmode[0::2].sum())
    sigma_even = float(s[0::2].sum())

    lhs = Wp - sigma_even * A
    rhs = (float(tr[0::2].sum()) - sigma_even * TrN) - (float(E2n[0::2].sum()) - sigma_even * E2N)
    d = abs(lhs - rhs)
    worst = max(worst, d)
    rows.append((alab, sigma_even, float(Wp / A)))
    print("%-5s %12.6e %12.6e %12.3e %12.6f" % (alab, lhs, rhs, d, sigma_even))

print()
print("worst |LHS - RHS| across the six cells: %.3e" % worst)
print("VERDICT:", "IDENTITY HOLDS at machine precision" if worst < 1e-9
      else "IDENTITY FAILS -- report as found, do not adjust")
print()
print("sigma_even per cell (the t-mass even share, as the instrument computes it):")
for alab, se, f in rows:
    print("  a^2=%-3s sigma_even=%.6f  f_cell=%.6f  f-sigma=%+.6f" % (alab, se, f, f - se))
