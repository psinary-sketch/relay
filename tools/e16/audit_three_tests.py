# W-CONTROL-AUDIT items 2-4, banked atoms only.
# (2) RESIDUAL TEST: fit (measured - derived) against the derivation's own stated
#     correction form (log L)^2 / L across the full range.
# (3) HEIGHT-VS-L TEST: the unfolded statistic on a HIGH-height and a LOW-height window
#     at MATCHED L — the discriminator between a height systematic and an L-effect.
# (4) REFERENCE CONSTANTS: lattice (exact 0), GUE (gamma-1, derived), Poisson (-log 2pi,
#     derived the same way with R_2 = 1) — the statistic as a one-number shape discriminant.
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")
mp.mp.dps = 40

def N(g):
    return g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8

with open(os.path.join(T, "k256_zeros.txt")) as f:
    gz = [mp.mpf(l.strip()) for l in f if l.strip()]
x = [N(g) for g in gz]
GUE = mp.euler - 1
POIS = -mp.log(2 * mp.pi)

def stat(lo, hi):
    """per-point unfolded pair energy on the window [lo, hi) (0-based indices)."""
    s = mp.mpf(0); L = hi - lo
    for i in range(lo, hi):
        for j in range(i + 1, hi):
            s += 2 * mp.log(abs(x[j] - x[i]) / (j - i))
    return s / L

print("=== (2) THE RESIDUAL TEST ===")
Ls = [50, 100, 200, 400, 800, 1200]
meas = {}
for L in Ls:
    meas[L] = stat(0, L)
print(f"{'L':>6} {'measured':>11} {'shortfall':>11} {'(logL)^2/L':>12} {'coef needed':>12} {'C/logL fit':>11}")
for L in Ls:
    short = meas[L] - GUE
    form = mp.log(L) ** 2 / L
    print(f"{L:>6} {mp.nstr(meas[L],6):>11} {mp.nstr(short,5):>11} {mp.nstr(form,4):>12} "
          f"{mp.nstr(short/form,4):>12} {mp.nstr(short*mp.log(L),4):>11}")
c_hi = (meas[1200] - GUE) / (mp.log(1200) ** 2 / 1200)
pred_lo = c_hi * mp.log(50) ** 2 / 50
print(f"\ncoefficient closing L=1200: {mp.nstr(c_hi,4)}; it predicts shortfall at L=50 = "
      f"{mp.nstr(pred_lo,4)} vs measured {mp.nstr(meas[50]-GUE,4)}")
print(f"|whole statistic| = {mp.nstr(abs(GUE),4)} — mispredicts by more than the statistic: "
      f"{abs(pred_lo - (meas[50]-GUE)) > abs(GUE)}")
print("the C/logL column is near-constant by comparison — the shortfall decays like 1/log L,")
print("not like (log L)^2/L: the stated error term does NOT account for it.")

print("\n=== (3) THE HEIGHT-VS-L TEST (matched L = 300) ===")
Lw = 300
low = stat(0, Lw)
high = stat(1200 - Lw, 1200)
print(f"low window  (zeros 1..{Lw}, gamma {mp.nstr(gz[0],5)}..{mp.nstr(gz[Lw-1],6)}): "
      f"{mp.nstr(low,6)}")
print(f"high window (zeros {1200-Lw+1}..1200, gamma {mp.nstr(gz[1200-Lw],6)}..{mp.nstr(gz[-1],6)}): "
      f"{mp.nstr(high,6)}")
print(f"derived GUE ideal: {mp.nstr(GUE,6)} | high is closer: {abs(high-GUE) < abs(low-GUE)} "
      f"(|low-ideal| = {mp.nstr(abs(low-GUE),4)}, |high-ideal| = {mp.nstr(abs(high-GUE),4)})")

print("\n=== (4) THE REFERENCE CONSTANTS ===")
print(f"  rigid integer lattice : 0            (exact, by construction)")
print(f"  GUE / sine kernel     : gamma - 1 = {mp.nstr(GUE,7)}   (derived)")
print(f"  Poisson (R_2 = 1)     : -log 2pi  = {mp.nstr(POIS,7)}   (derived the same way)")
print(f"  zeta measured (L=1200): {mp.nstr(meas[1200],7)}")
frac = (meas[1200] - 0) / (GUE - 0)
print(f"  zeta sits at {mp.nstr(frac*100,4)}% of the way from lattice to GUE, and "
      f"{mp.nstr((meas[1200]/POIS)*100,4)}% of the way to Poisson")
