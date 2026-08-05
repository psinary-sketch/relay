# W-CONTROL-AUDIT item 4 — pi_0 RE-POSED in unfolded coordinates.
# x_j := N(gamma_j) (the smooth counting function at the actual zero).  The
# position-matched control IS the integer lattice in these coordinates, so the statistic
# needs no separately-built control and is invariant under any constant offset:
#     Delta_unf(L) = sum_{i<j<=L} 2 log( |x_j - x_i| / (j - i) )
# DERIVED FIRST (E-25's computation, numerator half): Delta_unf(L) = L(gamma - 1) + O((log L)^2)
# under pair correlation.  Two normalizations:
#     harmonic (the old one): -> 0 like (gamma-1)/(log L + gamma - 1)   [degenerate]
#     per-point (the repair):  Delta_unf / L -> gamma - 1 = -0.42278    [non-vanishing]
# This script MEASURES both against the derivation, from banked atoms only.
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")
mp.mp.dps = 40

def N(g):
    return g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8

with open(os.path.join(T, "k256_zeros.txt")) as f:
    gz = [mp.mpf(l.strip()) for l in f if l.strip()]

x = [N(g) for g in gz]
gamma_c = mp.euler
print(f"derived ideal (per-point normalization): gamma - 1 = {mp.nstr(gamma_c - 1, 6)}")
print(f"derived ideal (harmonic normalization) at each L: (gamma-1)/(log L + gamma - 1)\n")
print(f"{'L':>6} {'Delta_unf':>14} {'per-point':>12} {'ideal/pt':>10} {'harmonic':>12} {'ideal/harm':>11}")
for L in (50, 100, 200, 400, 800, 1200):
    s = mp.mpf(0); h = mp.mpf(0)
    for i in range(L):
        for j in range(i + 1, L):
            s += 2 * mp.log(abs(x[j] - x[i]) / (j - i))
            h += mp.mpf(1) / (j - i)
    per = s / L
    har = s / h
    ideal_h = (gamma_c - 1) / (mp.log(L) + gamma_c - 1)
    print(f"{L:>6} {mp.nstr(s,7):>14} {mp.nstr(per,6):>12} {mp.nstr(gamma_c-1,5):>10} "
          f"{mp.nstr(har,6):>12} {mp.nstr(ideal_h,5):>11}")
