# E-24: the power analysis and the class check, BEFORE any Epstein computation.
# (1) Derive pi_0's ideal for a general translation-invariant R_2 = 1 - K(r):
#        pi_0 = -log 2pi - 2 * integral_0^inf K(r) log r dr
#     GUE (K = sinc^2)  -> gamma - 1;  Poisson (K = 0) -> -log 2pi;
#     m-fold superposition (K = (1/m) sinc^2(r/m)) -> gamma - 1 - log m.
# (2) VALIDATE that formula numerically on a synthetic 2-fold superposition built from the
#     banked zeros (two interleaved half-density copies), through the identical pipeline.
# (3) State the power numbers: uncertainty at accessible windows vs the separations.
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")
mp.mp.dps = 30

def N(g):
    return g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8

with open(os.path.join(T, "k256_zeros.txt")) as f:
    gz = [mp.mpf(l.strip()) for l in f if l.strip()]
x_zeta = [N(g) for g in gz]

def pi0(x, L):
    s = mp.mpf(0)
    for i in range(L):
        for j in range(i + 1, L):
            s += 2 * mp.log(abs(x[j] - x[i]) / (j - i))
    return s / L

GUE = mp.euler - 1
print("=== (1) THE DERIVED FAMILY ===")
for m in (1, 2, 3):
    print(f"  m = {m}-fold superposition: pi_0 = gamma - 1 - log {m} = "
          f"{mp.nstr(GUE - mp.log(m), 7)}")
print(f"  Poisson (K = 0): -log 2pi = {mp.nstr(-mp.log(2*mp.pi), 7)}")

print("\n=== (2) VALIDATION on a synthetic 2-fold superposition ===")
# CORRECTED construction (the first attempt halved the unfolded positions, which doubled
# the merged density and produced a density artifact, not a superposition):
# two INDEPENDENT density-1/2 spectra, each a disjoint stretch of zeta's zeros decimated
# by 2 (spacing ~2 = density 1/2), translated onto a common range, then merged -> density 1.
NH = 280
A = [x_zeta[2 * i] - x_zeta[0] for i in range(NH)]
B = [x_zeta[600 + 2 * i] - x_zeta[600] + mp.mpf("1.0") for i in range(NH)]
merged = sorted(A + B)
print(f"  merged points: {len(merged)} | derived target: gamma - 1 - log 2 = "
      f"{mp.nstr(GUE - mp.log(2), 7)}")
for L in (200, 400, 600):
    print(f"    L = {L}: pi_0(superposition) = {mp.nstr(pi0(merged, L), 6)} | "
          f"pi_0(zeta) = {mp.nstr(pi0(x_zeta, L), 6)}")

print("\n=== (3) THE POWER NUMBERS ===")
lo = pi0(x_zeta[:300] if False else x_zeta, 300)
print(f"  zeta pi_0 at L = 300 (low window): {mp.nstr(lo, 6)}")
print(f"  measured uncertainty at accessible windows: ~0.04-0.06")
print(f"     (height drift at matched L = 300: 0.037; L-drift across 50..1200: ~0.06)")
print(f"  expected separation, CORRELATION structure (m = 1 vs 2): "
      f"{mp.nstr(mp.log(2), 4)}  -> ample power")
print(f"  expected separation, PLACEMENT at fixed R_2: 0 exactly")
print("     pi_0 is a functional of the IMAGINARY PARTS ONLY (x_j = N(gamma_j));")
print("     the real parts never enter its definition -> zero power for placement,")
print("     by construction, not by insufficient data.")
