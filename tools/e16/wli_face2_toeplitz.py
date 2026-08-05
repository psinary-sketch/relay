# W-LI face 2, second stage: the Toeplitz detector's actual depth and delta-resolution.
#
# Stage 1 measured the MAGNITUDE detector (|c_n| crossing a multiple of the background) and
# found it needs n ~ 5100.  But the Toeplitz min-eigenvalue fired at K = 400, which uses only
# c_0..c_399.  This stage measures where the Toeplitz detector actually fires, and what
# off-line displacement it can resolve at a given order.
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
    w = np.linalg.eigvalsh(c[idx])
    return w.min()


NMAX = 1400
zA = online_set(gam)
cA = moments(zA, NMAX)

print("=" * 78)
print("E.  WHERE THE TOEPLITZ DETECTOR ACTUALLY FIRES")
print("=" * 78)
print("  Decision rule, fixed in advance: the witness arm is DETECTED at order K when its")
print("  Toeplitz min-eigenvalue is more negative than 100x the zeta arm's at the same K.")
print("  (The zeta arm is exactly PSD, so its min-eig IS the float64 noise floor at each K --")
print("  it is the correct scale to beat, and it is measured, not assumed.)")
print()
print(f"{'K':>6} {'zeta (noise)':>16} {'witness':>16} {'ratio':>12} {'detected':>10}")
cB = moments(np.concatenate([zA, quadruple(0.9533, GAM)]), NMAX)
fired = None
for K in (50, 100, 120, 140, 160, 180, 200, 250, 300, 400, 600, 800, 1000, 1200):
    a = min_eig(cA, K)
    b = min_eig(cB, K)
    r = b / a if a != 0 else float("inf")
    det = r > 100
    if det and fired is None:
        fired = K
    print(f"{K:>6} {a:>16.6g} {b:>16.6g} {r:>12.4g} {str(det):>10}")
print()
print(f"  FIRST ORDER AT WHICH THE WITNESS IS DETECTED: K = {fired}")
print(f"  moments consumed: c_0 .. c_{fired-1}   (depth n = {fired-1})")
print(f"  the MAGNITUDE detector needed n ~ 5101 for the same witness")
print(f"  --> the Toeplitz form is ~{5101/max(fired-1,1):.0f}x cheaper in depth")

print()
print("=" * 78)
print("F.  DELTA-RESOLUTION OF THE TOEPLITZ DETECTOR  (the re-price)")
print("=" * 78)
print("  gamma fixed at 16.290; beta = 1/2 + delta swept down.  For each delta, the smallest")
print("  order K at which the 100x rule fires.  'none' = not detected at K <= 1200.")
print()
print(f"{'delta':>12} {'beta':>12} {'|z_out|-1':>14} {'K_detect':>10} {'depth n':>9}")
Ks = (50, 100, 200, 300, 400, 600, 800, 1000, 1200)
noise = {K: min_eig(cA, K) for K in Ks}
for delta in (0.4533, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001):
    zq = quadruple(0.5 + delta, GAM)
    cD = moments(np.concatenate([zA, zq]), NMAX)
    hit = None
    for K in Ks:
        if noise[K] != 0 and min_eig(cD, K) / noise[K] > 100:
            hit = K
            break
    ex = np.abs(zq).max() - 1
    print(f"{delta:>12.4g} {0.5+delta:>12.6f} {ex:>14.6g} "
          f"{(str(hit) if hit else 'none'):>10} {(str(hit-1) if hit else '-'):>9}")

print()
print("  READ (corrected against the table above, which refuted the guess written here first):")
print("  the cost is NOT linear in 1/delta.  Dropping delta by 453x (0.4533 -> 0.001) costs")
print("  only 4x in order (K 200 -> 800).  The detector is therefore not relying on")
print("  exponential amplification of |z_out|^K -- at delta = 0.001, K*log|z_out| is 0.003,")
print("  no amplification at all -- but on the fact that a kernel r^|a-b| with r > 1 is not")
print("  a positive-definite kernel AT ANY r > 1.  Stage 3 measures where that breaks.")
