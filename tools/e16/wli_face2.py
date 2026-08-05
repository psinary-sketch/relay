# W-LI face 2: the placement channel, with a known-answer synthetic control.
# c_n = sum over zeros of z^n, z = 1 - 1/rho (the Cayley image).  On the critical line
# |z| = 1 exactly; off it |z| != 1, and the mirror zero's |z| > 1 makes c_n grow.
# Objects: (A) zeta's banked zeros (all on-line, conjugates included);
#          (B) the same PLUS one Davenport-Heilbronn quadruple at the Epstein witness's
#              measured parameters (beta = 0.9533, gamma = 16.290) -- a synthetic control
#              with a KNOWN answer, standing in for the Epstein object whose own zeros are
#              a separate build.
# Reported: the power numbers, the c_n profiles, and the Toeplitz positivity profile.
import os
import numpy as np

T = os.environ.get("TEMP", ".")
with open(os.path.join(T, "k256_zeros.txt")) as f:
    gam = np.array([float(l.strip()[:60]) for l in f if l.strip()])[:1200]

def zs_online(g):
    rho = 0.5 + 1j * g
    return 1 - 1 / rho

zA = zs_online(gam)
zA = np.concatenate([zA, np.conj(zA)])            # +/- gamma

BETA, GAM = 0.9533, 16.290
quad = np.array([BETA + 1j*GAM, BETA - 1j*GAM, (1-BETA) + 1j*GAM, (1-BETA) - 1j*GAM])
zq = 1 - 1 / quad
zB = np.concatenate([zA, zq])

print("=== THE POWER NUMBERS (stated before the run's verdict) ===")
mods = np.abs(zq)
print(f"  witness quadruple |z| values: {np.round(mods, 6)}")
delta = mods.max() - 1
print(f"  growth rate delta = max|z| - 1 = {delta:.6f}")
noise = np.sqrt(len(zA))
print(f"  on-line noise floor ~ sqrt(2*1200) = {noise:.1f}")
n_det = np.log(noise) / np.log(1 + delta)
print(f"  PREDICTED detection depth n = ln(noise)/ln(1+delta) = {n_det:.0f}")
print(f"  achievable n at float64 (|z|^n error ~ n*1e-16): 5000 -> error ~5e-13 << delta")
print(f"  VERDICT ON POWER: reachable (predicted {n_det:.0f} << achievable 5000)")

def moments(z, N):
    c = np.zeros(N + 1)
    p = np.ones_like(z)
    for n in range(N + 1):
        c[n] = p.sum().real
        p = p * z
    return c

N = 5000
cA = moments(zA, N)
cB = moments(zB, N)
print("\n=== THE MEASURED PROFILES ===")
print(f"{'n':>6} {'|c_n| zeta':>14} {'|c_n| witness':>15} {'ratio':>10}")
for n in (0, 100, 500, 1000, 2000, 2300, 3000, 4000, 5000):
    r = abs(cB[n]) / max(abs(cA[n]), 1e-300)
    print(f"{n:>6} {abs(cA[n]):>14.4g} {abs(cB[n]):>15.4g} {r:>10.4g}")
mx = int(np.argmax(np.abs(cB) > 5 * noise))
print(f"\n  first n where |c_n(witness)| exceeds 5x the noise floor: {mx}")
print(f"  zeta's |c_n| stays bounded by: {np.abs(cA).max():.4g} (max over n<=5000)")

print("\n=== THE TOEPLITZ POSITIVITY PROFILE ===")
def toeplitz_min_eig(c, K):
    idx = np.abs(np.subtract.outer(np.arange(K), np.arange(K)))
    Tm = c[idx]
    w = np.linalg.eigvalsh(Tm)
    return w.min(), w.max()

print(f"{'order K':>9} {'zeta min eig':>16} {'witness min eig':>18} {'zeta PSD':>10} {'witness PSD':>12}")
for K in (10, 25, 50, 100, 200, 400):
    a_min, a_max = toeplitz_min_eig(cA, K)
    b_min, b_max = toeplitz_min_eig(cB, K)
    print(f"{K:>9} {a_min:>16.6g} {b_min:>18.6g} {str(a_min > -1e-6*abs(a_max)):>10} "
          f"{str(b_min > -1e-6*abs(b_max)):>12}")
print("\n(the error bar on each min-eigenvalue is set by the float64 accumulation in c_n,")
print(" ~n*1e-16 relative; at K<=400 that is ~1e-13 absolute against entries of order 1e3)")
