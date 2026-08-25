# -*- coding: utf-8 -*-
"""b167 -- THE GATE FAILURE, DIAGNOSED RATHER THAN ASSERTED.
### The act has HALTED. Nothing below reads a new quantity for the banking; this
locates the cause of G4's failure and quantifies what a repair would require."""
import functools, math, sys
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38

RHO_MAX = 48.001
print("=" * 88)
print("b167 -- G4's FAILURE, LOCATED")
print("=" * 88)

for n_rho in (400, 800, 1600, 3200):
    rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), n_rho))
    ee = B38.per_mode_eps_grids(rr)
    s0 = float(ee[:10, 0].sum())
    # what np.interp returns at rho = 1 (BELOW the grid's first point)
    clamp = float(sum(np.interp(1.0, rr, ee[n]) for n in range(10)))
    print("  n_rho %5d : rr[0] = %.10f   sum_n e_n(rr[0]) = %.9e   np.interp at rho=1 -> %.9e"
          % (n_rho, rr[0], s0, clamp))

print("\n  ### THE GRID'S LEFT ENDPOINT IS exp(1e-4) = %.10f, NOT 1." % math.exp(1e-4))
print("  ### np.interp CLAMPS BELOW IT, so e_n(u=0) returns e_n(rr[0]), not e_n(1) = 0.")
print("  ### THE DEFICIT IS THEREFORE sum_n e_n(rr[0]), AND IT DOES NOT SHRINK WITH n_rho")
print("  ### BECAUSE THE LEFT ENDPOINT IS FIXED AT exp(1e-4) AT EVERY RESOLUTION.")

print("\n--- WHY Psi DID NOT SEE THIS AND Delta DOES ---")
rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), 800))
ee = B38.per_mode_eps_grids(rr)
tot = float(ee[:10, 0].sum())
even = float(ee[0:10:2, 0].sum())
sig = 0.616500298741
print("  sum_n e_n(rr[0])            = %.9e" % tot)
print("  sum_even e_n(rr[0])         = %.9e" % even)
print("  sigma_even * sum_n          = %.9e" % (sig * tot))
print("  phi_e(0) = even - sigma*tot = %.9e   ### b115 banked -1.42e-11" % (even - sig * tot))
print("  even share of the total     = %.9f   ### sigma_even = %.9f" % (even / tot, sig))
print("\n  ### Psi's epsilon half is a t-PROPORTIONAL DIFFERENCE and the clamp cancels")
print("  ### out of it almost exactly. ### DELTA IS A RAW SUM AND SEES THE CLAMP WHOLE.")
print("  ### THE CANCELLATION THAT PROTECTS Psi AT u = 0 DOES NOT PROTECT Delta.")

print("\n--- HOW FAR THE DEFECT REACHES ---")
u_bad = 1e-4
print("  clamping affects u < %.1e only (rho < rr[0]); above it np.interp interpolates." % u_bad)
for u in (0.0, 1e-5, 1e-4, 1e-3, 1e-2):
    rho = math.exp(u)
    v = float(sum(np.interp(rho, rr, ee[n]) for n in range(10)))
    print("     u = %-8.1e rho = %.8f : sum_n e_n = %.9e %s"
          % (u, rho, v, "  <-- CLAMPED" if rho < rr[0] else ""))
print("=" * 88)
