# W-LI FACE 2 — the run, with the novelty check settled at cite first.
#
# The channel: z = 1 - 1/rho (the Cayley map).  Re rho = 1/2  <=>  |z| = 1.  So the Cayley
# images of the zeros are the support of a measure on the unit circle exactly under RH, and
# c_n = sum z^n are its trigonometric moments; Toeplitz PSD of (c_n) is the moment condition.
#
# THIS SCRIPT MEASURES THREE THINGS, in this order:
#   B. whether the ZETA arm of the truncated-zero pipeline has any placement power at all
#      (a salt-check that must run BEFORE its verdict is read);
#   C. the witness arm's detection depth against the depth predicted in the power clause;
#   D. the instrument's delta-resolution at reachable depth (the re-price).
import os
import numpy as np

rng = np.random.default_rng(20260805)
T = os.environ.get("TEMP", ".")
with open(os.path.join(T, "k256_zeros.txt")) as f:
    gam = np.array([float(l.strip()[:60]) for l in f if l.strip()])[:1200]

BETA, GAM = 0.9533, 16.290          # the programme's located disc -23 off-line zero
DELTA = BETA - 0.5


def cayley(rho):
    return 1 - 1 / rho


def online_set(gammas):
    z = cayley(0.5 + 1j * np.asarray(gammas, dtype=float))
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


def toeplitz_min_eig(c, K):
    idx = np.abs(np.subtract.outer(np.arange(K), np.arange(K)))
    w = np.linalg.eigvalsh(c[idx])
    return w.min(), w.max()


# ----------------------------------------------------------------------------- A
print("=" * 78)
print("A.  THE POWER CLAUSE  (stated before any measurement below is read)")
print("=" * 78)
zq = quadruple(BETA, GAM)
mods = np.abs(zq)
out = mods.max()
log_out = np.log(out)
print(f"  witness   beta = {BETA}, gamma = {GAM},  delta = beta - 1/2 = {DELTA:.4f}")
print(f"  Cayley moduli of the quadruple: {np.round(mods, 8)}")
print(f"  the escaping modulus |z_out|          = {out:.10f}")
print(f"  growth exponent  log|z_out|           = {log_out:.10e}")
print(f"  asymptotic form  delta/gamma^2        = {DELTA/GAM**2:.10e}")
print(f"  FERRY'S DEPTH    n ~ gamma^2/delta    = {GAM**2/DELTA:.1f}   (the e-folding depth)")
print(f"  exact e-folding  1/log|z_out|         = {1/log_out:.1f}")
print("  NOTE: gamma^2/delta is the depth at which the signal is amplified by e, NOT the")
print("  depth at which it clears the on-line background.  The detection depth is")
print("  n_det = log(threshold * B) / log|z_out|, with B the background measured in B below.")

# ----------------------------------------------------------------------------- B
print()
print("=" * 78)
print("B.  DOES THE ZETA ARM HAVE ANY PLACEMENT POWER?  (salt-check, run first)")
print("=" * 78)
N = 5000
zA = online_set(gam)
cA = moments(zA, N)
B_bg = np.abs(cA).max()
print(f"  zeta arm: {len(gam)} banked zeros, conjugates included ({len(zA)} Cayley points)")
print(f"  background B = max |c_n| over n <= {N}:  {B_bg:.6g}")

print()
print("  Toeplitz min-eigenvalue, zeta arm vs TWO controls that share only ONE property")
print("  with it -- that their points lie on the critical line:")
print("    ctrl-1: 1200 RANDOM ordinates, uniform on [14, 2000]")
print("    ctrl-2: 1200 ordinates from an ARITHMETIC PROGRESSION (a maximally un-zeta-like")
print("            on-line set)")
g_rand = np.sort(rng.uniform(14.0, 2000.0, size=len(gam)))
g_arith = np.linspace(14.0, 2000.0, len(gam))
cR = moments(online_set(g_rand), N)
cP = moments(online_set(g_arith), N)
print()
print(f"{'K':>6} {'zeta min eig':>16} {'random min eig':>16} {'arith min eig':>16}")
for K in (10, 25, 50, 100, 200, 400):
    a, _ = toeplitz_min_eig(cA, K)
    r, _ = toeplitz_min_eig(cR, K)
    p, _ = toeplitz_min_eig(cP, K)
    print(f"{K:>6} {a:>16.6g} {r:>16.6g} {p:>16.6g}")
print()
print("  STRUCTURAL FACT behind the table: for unit-modulus points z_j, the Toeplitz matrix")
print("  T_ab = c_{a-b} = sum_j z_j^{a-b} = sum_j (v_j v_j^*)_ab  with v_j = (1, z_j, z_j^2,...),")
print("  so T is a sum of rank-one PSD matrices and is PSD FOR EVERY on-line set whatsoever.")
print("  The zeta arm's inputs are built as 0.5 + i*gamma: the real part is IMPOSED, not")
print("  measured.  Its PSD verdict is therefore a property of the construction.")

# ----------------------------------------------------------------------------- C
print()
print("=" * 78)
print("C.  THE WITNESS ARM  (known answer: an off-line quadruple is present by construction)")
print("=" * 78)
zB = np.concatenate([zA, zq])
cB = moments(zB, N)
thresh = 5 * B_bg
n_pred = np.log(2.5 * B_bg) / log_out
above = np.nonzero(np.abs(cB) > thresh)[0]
n_meas = int(above[0]) if above.size else None
print(f"  threshold = 5 x background = {thresh:.6g}")
print(f"  PREDICTED detection depth  n_det = log(2.5*B)/log|z_out| = {n_pred:.0f}")
print(f"  MEASURED  detection depth                                = {n_meas}")
print()
print(f"{'n':>7} {'|c_n| zeta':>14} {'|c_n| witness':>15} {'ratio':>12}")
for n in (0, 500, 1000, 2000, 3000, 4000, 5000):
    r = abs(cB[n]) / max(abs(cA[n]), 1e-300)
    print(f"{n:>7} {abs(cA[n]):>14.6g} {abs(cB[n]):>15.6g} {r:>12.6g}")
print()
print(f"{'K':>6} {'witness min eig':>18} {'zeta min eig':>16}")
for K in (10, 25, 50, 100, 200, 400):
    b, _ = toeplitz_min_eig(cB, K)
    a, _ = toeplitz_min_eig(cA, K)
    print(f"{K:>6} {b:>18.6g} {a:>16.6g}")

# ----------------------------------------------------------------------------- D
print()
print("=" * 78)
print("D.  RESOLUTION SWEEP  (the re-price: what delta is reachable at what depth)")
print("=" * 78)
print("  For gamma = 16.290 fixed, the smallest off-line displacement detectable by depth n:")
print()
print(f"{'depth n':>10} {'delta_min':>14} {'beta_min':>12}")
for n_max in (5000, 20000, 100000, 1_000_000):
    # n_max = log(2.5B)/log|z_out|  =>  log|z_out| = log(2.5B)/n_max
    lo = np.log(2.5 * B_bg) / n_max
    # |z_out|^2 = 1 + 2d/((0.5-d)^2 + gamma^2); solve for d
    target = np.exp(2 * lo) - 1.0
    d = target * GAM**2 / 2.0
    for _ in range(60):
        d = target * ((0.5 - d)**2 + GAM**2) / 2.0
    print(f"{n_max:>10} {d:>14.6g} {0.5+d:>12.8f}")
print()
print("  and the same sweep at the height of the FIRST zeta zero (gamma = 14.1347), which is")
print("  where a hypothetical counterexample would be cheapest to see:")
G1 = 14.134725
print(f"{'depth n':>10} {'delta_min':>14}")
for n_max in (5000, 100000):
    lo = np.log(2.5 * B_bg) / n_max
    target = np.exp(2 * lo) - 1.0
    d = target * G1**2 / 2.0
    for _ in range(60):
        d = target * ((0.5 - d)**2 + G1**2) / 2.0
    print(f"{n_max:>10} {d:>14.6g}")
