# W-LI face 2, third stage: where the Toeplitz detector's resolution ACTUALLY breaks.
#
# Stage 2's sweep contradicted the gloss written into it: dropping delta by 453x (0.4533 ->
# 0.001) cost only 4x in order (K 200 -> 800), which is not the linear-in-1/delta behaviour
# that exponential amplification would give.  This stage pushes delta down until the detector
# fails, and separates the two candidate limits: ARITHMETIC PRECISION (purchasable) versus
# something structural (not).
import os
import numpy as np

T = os.environ.get("TEMP", ".")
with open(os.path.join(T, "k256_zeros.txt")) as f:
    gam = np.array([float(l.strip()[:60]) for l in f if l.strip()])[:1200]

GAM = 16.290


def cayley(rho):
    return 1 - 1 / rho


def online_set(g):
    z = cayley(0.5 + 1j * np.asarray(g, dtype=float))
    return np.concatenate([z, np.conj(z)])


def quadruple(beta, gamma):
    q = np.array([beta + 1j*gamma, beta - 1j*gamma,
                  (1-beta) + 1j*gamma, (1-beta) - 1j*gamma])
    return cayley(q)


def moments(z, N):
    c = np.zeros(N + 1)
    p = np.ones_like(z)
    for n in range(N + 1):
        c[n] = p.sum().real
        p = p * z
    return c


def min_eig(c, K):
    idx = np.abs(np.subtract.outer(np.arange(K), np.arange(K)))
    return np.linalg.eigvalsh(c[idx]).min()


NMAX = 2400
zA = online_set(gam)
cA = moments(zA, NMAX)
Ks = (200, 400, 800, 1200, 1600, 2000)
noise = {K: min_eig(cA, K) for K in Ks}

print("=" * 78)
print("G.  RESOLUTION LIMIT: pushing delta down until the detector fails")
print("=" * 78)
print("  Same 100x-over-the-measured-noise rule.  Noise floor at each order (zeta arm, which")
print("  is exactly PSD, so this is pure float64 roundoff):")
for K in Ks:
    print(f"    K = {K:>5}:  {noise[K]:.4g}")
print()
print(f"{'delta':>12} {'|z_out|-1':>13} {'K_detect':>10} {'min-eig at K_det':>18} {'margin':>12}")
for delta in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9):
    zq = quadruple(0.5 + delta, GAM)
    cD = moments(np.concatenate([zA, zq]), NMAX)
    hit, val = None, None
    for K in Ks:
        m = min_eig(cD, K)
        if noise[K] != 0 and m / noise[K] > 100:
            hit, val = K, m
            break
    ex = np.abs(zq).max() - 1
    if hit:
        print(f"{delta:>12.3g} {ex:>13.4g} {hit:>10} {val:>18.6g} {val/noise[hit]:>12.4g}")
    else:
        print(f"{delta:>12.3g} {ex:>13.4g} {'none':>10} {'-':>18} {'-':>12}")

print()
print("=" * 78)
print("H.  WHICH LIMIT IS IT?  precision, or structure?")
print("=" * 78)
print("  If the limit is ARITHMETIC PRECISION, the detected min-eigenvalue at the failure")
print("  point should sit at the roundoff floor and scale with delta linearly above it.")
print("  Measuring the min-eig at fixed K = 1200 across delta:")
print()
print(f"{'delta':>12} {'min-eig (K=1200)':>20} {'ratio to noise':>16} {'min-eig/delta':>16}")
for delta in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8):
    cD = moments(np.concatenate([zA, quadruple(0.5 + delta, GAM)]), NMAX)
    m = min_eig(cD, 1200)
    print(f"{delta:>12.3g} {m:>20.6g} {m/noise[1200]:>16.4g} {m/delta:>16.6g}")
print()
print("  READ (corrected against the table above, which refuted the guess written here first):")
print("  the right-hand column is NOT constant -- it falls by a factor ~10 for each factor 10")
print("  in delta, so the signal scales as delta^2, not delta.  The failure at delta ~ 1e-6 is")
print("  therefore where a delta^2 signal meets the float64 roundoff floor, and the resolution")
print("  limit scales as sqrt(floor): it is bought with PRECISION, not with depth.  Nothing")
print("  structural stops the detector; only the arithmetic it is run in.")
