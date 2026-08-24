# -*- coding: utf-8 -*-
"""b140 -- the two bounds' KERNEL CONSTITUENTS, and the two registered checks.

### CIRCULARITY GATE. Everything computed here is a fact about Phi_K, hence
### about K = w*w, hence about the WINDOW ALONE. No Psi content enters. E1-E6
### appear nowhere. The two registered "where I could be wrong" checks are run
### at the end and are labelled.
"""
import functools, math, sys
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b121_instrument as B121

sg, K, Phi = B121.build_kernel()
L_LO, L_HI = math.log(math.sqrt(2)), math.log(math.sqrt(48))
UMAX = 2.0 * math.log(math.sqrt(48.001))

print("=" * 78)
print("b140 -- THE KERNEL CONSTITUENTS (window-only; no Psi content)")
print("=" * 78)

i0 = int(np.argmax(np.sign(Phi[:-1]) != np.sign(Phi[1:])))
s0 = float(sg[i0])
print("\n  crossing sigma_0 = %.6f   (b116 records 0.6215)" % s0)
print("  INT Phi_K over [0,2] = %.6e   (mean-zero)" % float(np.trapezoid(Phi, sg)))
P = float(np.trapezoid(Phi[:i0 + 1], sg[:i0 + 1]))
Nn = float(np.trapezoid(Phi[i0:], sg[i0:]))
print("  positive mass P = INT_0^s0 Phi_K      = %+.9f" % P)
print("  negative mass   = INT_s0^2 Phi_K      = %+.9f   (sums to %.2e)"
      % (Nn, P + Nn))
print("  ||Phi_K||_inf                          = %.9f" % float(np.abs(Phi).max()))
print("  ||Phi_K||_inf on [s0,2]                = %.9f" % float(np.abs(Phi[i0:]).max()))
print("  INT_0^2 |Phi_K|                        = %.9f" % float(np.trapezoid(np.abs(Phi), sg)))

print("\n--- P1's KERNEL CONSTITUENTS min(A,B) over interior splits ---")
print("%8s %8s %14s %14s %14s" % ("a", "b", "A", "B", "min(A,B)"))
best = (0.0, None, None)
for a in (0.10, 0.20, 0.30, 0.40, 0.50):
    for b in (0.80, 1.00, 1.20, 1.50):
        ia = int(np.searchsorted(sg, a)); ib = int(np.searchsorted(sg, b))
        A = float(np.trapezoid(Phi[:ia + 1], sg[:ia + 1]))
        B = abs(float(np.trapezoid(Phi[ib:], sg[ib:])))
        if min(A, B) > best[0]:
            best = (min(A, B), a, b)
        print("%8.2f %8.2f %14.9f %14.9f %14.9f" % (a, b, A, B, min(A, B)))
print("\n  ### best min(A,B) = %.9f at (a,b) = (%.2f, %.2f)" % best)
print("  ### SO THE DERIVED FORM IS |C_M(L)| >= %.6f * [M(%.2f L) - M(%.2f L)]"
      % (best[0], best[2], best[1]))
print("  ### and the bracket -- THE ENVELOPE'S RISE -- IS NOT DERIVED.")

print("\n--- P2's KERNEL CONSTITUENTS ---")
print("  the bound's form: |C_r(L)| <= ||Phi_K||_inf * (1/L) * ||r||_{L1[0,2L]}")
print("  ### the constant is DERIVED: ||Phi_K||_inf = %.9f" % float(np.abs(Phi).max()))
print("  sharpened on the negative region: %.9f" % float(np.abs(Phi[i0:]).max()))
print("  ### and ||r||_{L1} -- THE DEFICIT'S SIZE -- IS NOT DERIVED.")

# ---------------- the two registered checks ----------------
print("\n" + "=" * 78)
print("THE TWO REGISTERED 'WHERE I COULD BE WRONG' CHECKS")
print("=" * 78)

print("\n(i) DOES THE TOTAL-RISE ALTERNATE DEGENERATE?")
print("    it uses only M(2L) - M(0), which the endpoint anchor supplies;")
print("    it needs a split at a -> 0 and b -> 2, so its constant is")
print("%8s %8s %16s" % ("a", "b", "min(A,B)"))
for a, b in ((0.02, 1.98), (0.05, 1.95), (0.01, 1.99)):
    ia = int(np.searchsorted(sg, a)); ib = int(np.searchsorted(sg, b))
    A = float(np.trapezoid(Phi[:ia + 1], sg[:ia + 1]))
    B = abs(float(np.trapezoid(Phi[ib:], sg[ib:])))
    print("%8.2f %8.2f %16.9e" % (a, b, min(A, B)))
print("    ### the constant -> 0 as the split reaches the endpoints.")
print("    ### THE ALTERNATE DEGENERATES, AS REGISTERED. P1 does NOT derive")
print("    ### outright from the endpoint anchor.")

print("\n(ii) DOES THE LOCALIZATION DERIVE C_r's SIGN ACROSS THE RANGE?")
print("     the sign is derived where u*/L >= sigma_0, i.e. L <= u*/sigma_0.")
print("     u* is psi_coarse's first descent -- A MEASURED QUANTITY (E6), so")
print("     ### THE CONDITION IS STATED AS A CONDITION AND NOT EVALUATED HERE.")
print("     the licensed range is L in [%.5f, %.5f]." % (L_LO, L_HI))
print("     ### FOR THE SIGN TO BE DERIVED ACROSS THE WHOLE RANGE ONE NEEDS")
print("     ### u* >= sigma_0 * L_HI = %.6f * %.6f = %.6f," % (s0, L_HI, s0 * L_HI))
print("     ### i.e. psi_coarse MONOTONE ON [0, %.6f]. THAT IS A STATEMENT" % (s0 * L_HI))
print("     ### ABOUT Psi AND IS NOT DERIVED. The condition is banked as the")
print("     ### exact hypothesis that would buy C_r's sign, and no more.")
