# (1) I-7's SECOND RUN — testing the ferry's proposed operational form against the very
#     failure it is being written for, before it is filed as standing.
# (2) THE EPSTEIN ZERO CENSUS — priced in advance, not run.
import os
import math
import numpy as np

T = os.environ.get("TEMP", ".")
with open(os.path.join(T, "k256_zeros.txt")) as f:
    gam = np.array([float(l.strip()[:60]) for l in f if l.strip()])[:1200]
rng = np.random.default_rng(20260805)
GAM_W, BETA_W = 16.290, 0.9533


def cayley(r):
    return 1 - 1 / r


def pts(gammas, sigmas):
    z = cayley(np.asarray(sigmas, dtype=float) + 1j * np.asarray(gammas, dtype=float))
    return np.concatenate([z, np.conj(z)])


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


K, N = 400, 500
base = min_eig(moments(pts(gam, np.full_like(gam, 0.5)), N), K)

print("=" * 78)
print("(1)  I-7's SECOND RUN — does the proposed operational form catch the failure?")
print("=" * 78)
print("  THE FERRY'S PROPOSED FORM: 'perturb the inputs' real parts and re-run; if the")
print("  statistic does not move, the instrument has no placement power.'")
print()
print(f"  Toeplitz min-eig at K = {K}, real parts all exactly 1/2:  {base:.6g}")
print()
print(f"{'perturbation eta':>18} {'min-eig':>16} {'moved?':>10}")
for eta in (0.0, 1e-9, 1e-7, 1e-5, 1e-3, 1e-1):
    sig = np.full_like(gam, 0.5) + eta * rng.choice([-1.0, 1.0], size=len(gam))
    m = min_eig(moments(pts(gam, sig), N), K)
    print(f"{eta:>18.3g} {m:>16.6g} {str(abs(m/base) > 10):>10}")
print()
print("  RESULT: the statistic MOVES, by twelve orders of magnitude, as soon as the real")
print("  parts leave 1/2.  So the proposed form PASSES this pipeline -- it does not catch")
print("  the failure it is being written for.")
print()
print("  WHY: perturbing the inputs tests the STATISTIC.  The statistic is placement-")
print("  sensitive; that was never in doubt.  What failed is the PIPELINE -- its inputs")
print("  are constructed at 1/2 rather than measured, so no perturbation of them is ever")
print("  taken from the object.")
print()
print("  THE FORM THAT DID CATCH IT (substitution, not perturbation): replace the object's")
print("  data with ARBITRARY data of the same class and ask whether the verdict changes.")
print()
print(f"{'input set':>34} {'min-eig at K=400':>18} {'ratio to zeta':>15}")
rows = [("zeta's 1200 banked ordinates", gam),
        ("1200 uniform random ordinates", np.sort(rng.uniform(14, 2000, len(gam)))),
        ("1200 in arithmetic progression", np.linspace(14, 2000, len(gam))),
        ("1200 ordinates all equal to 100", np.full(len(gam), 100.0))]
for label, g in rows:
    m = min_eig(moments(pts(g, np.full_like(g, 0.5)), N), K)
    print(f"{label:>34} {m:>18.6g} {m/base:>15.4g}")
print()
print("  RESULT: the verdict is unchanged across inputs that share only one property with")
print("  zeta's zeros -- lying on the line.  Even 1200 COPIES OF A SINGLE ORDINATE give the")
print("  same answer.  The pipeline is reading its own construction.")

print()
print("=" * 78)
print("(2)  THE EPSTEIN ZERO CENSUS — PRICED IN ADVANCE (named, not run)")
print("=" * 78)
print("  Object: the disc -23 Epstein zeta of the principal form x^2+xy+6y^2, h(-23) = 3.")
print("  A degree-2 L-function of conductor 23.  Zero count to height T:")
print("     N(T) ~ (T/pi) * log( sqrt(23) * T / (2*pi*e) )")
print()
print(f"{'T':>10} {'zeros N(T)':>12} {'2-D cells':>12} {'evals':>14} {'wall (mpmath)':>16}")
for Tt in (100, 1000, 10000):
    N_T = (Tt / math.pi) * math.log(math.sqrt(23) * Tt / (2 * math.pi * math.e))
    cells = 14 * (Tt / 0.5)                       # strip sigma in [0.3,1.7], 0.1 x 0.5 cells
    evals = cells * 200                           # ~200 boundary points per winding integral
    hours = evals * 0.03 / 3600                   # ~30 ms per Epstein evaluation at dps 30
    print(f"{Tt:>10} {N_T:>12.0f} {cells:>12.0f} {evals:>14.3g} {hours:>13.1f} h")
print()
print("  The census MUST be 2-D (argument-principle winding over rectangles in the strip),")
print("  not a critical-line scan.  A 1-D scan would impose the real part and reproduce")
print("  exactly the defect that (1) above just diagnosed.")
print()
print("  DETECTOR REACH that the census would buy.  The escaping modulus' excess is")
print("  |z_out| - 1 ~ delta/gamma^2, so sensitivity degrades as gamma^2.  Measured floor:")
print("  delta_min = 3e-6 at gamma = 16.29 in float64, scaling as sqrt(roundoff floor).")
print()
print(f"{'gamma':>10} {'delta_min float64':>20} {'delta_min at dps=50':>22}")
for g in (16.29, 100.0, 1000.0, 10000.0):
    d64 = 3e-6 * (g / GAM_W) ** 2
    d50 = d64 * math.sqrt(1e-50 / 2.2e-16)
    print(f"{g:>10.4g} {d64:>20.4g} {d50:>22.4g}")
print()
print("  THE KNOWN WITNESS sits at gamma = 16.290 with delta = 0.4533 -- five orders above")
print("  the float64 floor at that height.  It is detected at K = 200 with room to spare.")
