# Closing a work-order the formula-provenance sweep raised against THIS WEEK's own filing.
#
# INSTRUMENTS records: "the limit is arithmetic precision, purchasable as sqrt(floor) -- at 50
# digits the same order reaches delta ~ 2e-23."  The 2e-23 was EXTRAPOLATED from a scaling law
# that was never itself checked.  This checks the law.
#
# The law's two claims:
#   (i)  the Toeplitz noise floor is proportional to machine epsilon;
#   (ii) since the signal scales as delta^2, the resolvable delta scales as sqrt(floor).
# Both are testable cheaply by changing precision by a KNOWN factor: float32 vs float64.
#   eps32/eps64 = 1.192e-7 / 2.220e-16 = 5.37e8  ->  floor ratio should be ~5.4e8
#                                              ->  delta_min ratio should be ~sqrt = 2.3e4
import os
import numpy as np

T = os.environ.get("TEMP", ".")
with open(os.path.join(T, "k256_zeros.txt")) as f:
    gam = np.array([float(l.strip()[:60]) for l in f if l.strip()])[:1200]
GAM = 16.290


def run(dtype_c, dtype_r, K, N, delta=None):
    z = 1 - 1 / (0.5 + 1j * gam)
    z = np.concatenate([z, np.conj(z)])
    if delta is not None:
        b = 0.5 + delta
        q = np.array([b + 1j*GAM, b - 1j*GAM, (1-b) + 1j*GAM, (1-b) - 1j*GAM])
        z = np.concatenate([z, 1 - 1/q])
    z = z.astype(dtype_c)
    c = np.zeros(N + 1, dtype=dtype_r)
    p = np.ones_like(z)
    for n in range(N + 1):
        c[n] = p.sum().real
        p = p * z
    idx = np.abs(np.subtract.outer(np.arange(K), np.arange(K)))
    return np.linalg.eigvalsh(c[idx].astype(dtype_r)).min()


K, N = 400, 500
eps64, eps32 = np.finfo(np.float64).eps, np.finfo(np.float32).eps
print("=" * 78)
print("CLAIM (i): the Toeplitz noise floor is proportional to machine epsilon")
print("=" * 78)
f64 = run(np.complex128, np.float64, K, N)
f32 = run(np.complex64, np.float32, K, N)
print(f"  eps64 = {eps64:.4g}   eps32 = {eps32:.4g}   eps32/eps64 = {eps32/eps64:.4g}")
print(f"  floor at K={K}, float64: {f64:.6g}")
print(f"  floor at K={K}, float32: {f32:.6g}")
print(f"  measured floor ratio  : {f32/f64:.4g}")
print(f"  predicted (eps ratio) : {eps32/eps64:.4g}")
p_floor = np.log(abs(f32/f64)) / np.log(eps32/eps64)
print(f"  MEASURED EXPONENT: floor ~ eps^p with p = {p_floor:.3f}")
print("  (p = 1 was the filed assumption; the measurement is reported as the exponent")
print("   rather than as a pass/fail against an arbitrary tolerance band.)")

print()
print("=" * 78)
print("CLAIM (ii): resolvable delta scales as sqrt(floor)")
print("=" * 78)
print("  smallest delta detected at the 100x-over-floor rule, in each precision:")
GRID = [0.45, 0.3, 0.2, 0.15, 0.1, 0.07, 0.05, 0.03, 0.02, 0.01, 3e-3, 1e-3]
res = {}
for name, dc, dr, floor in (("float64", np.complex128, np.float64, f64),
                            ("float32", np.complex64, np.float32, f32)):
    hit = None
    for d in GRID:
        m = run(dc, dr, K, N, delta=d)
        if abs(m) > 100 * abs(floor):
            hit = d
        else:
            break
    res[name] = hit
    print(f"    {name}: delta_min = {hit if hit else '> ' + str(GRID[0])}")
if res["float64"] and res["float32"]:
    r_meas = res["float32"] / res["float64"]
    q = np.log(r_meas) / np.log(abs(f32 / f64))
    print(f"  measured delta_min ratio        : {r_meas:.4g}")
    print(f"  predicted sqrt(floor ratio)     : {np.sqrt(abs(f32/f64)):.4g}")
    print(f"  MEASURED EXPONENT: delta_min ~ floor^q with q = {q:.3f}  (0.5 was the filed")
    print("   assumption, and follows from the measured delta^2 signal law)")
else:
    q = float("nan")
    print("  delta_min not bracketed in one of the precisions; exponent not measured")

print()
print("=" * 78)
print("VERDICT ON THE FILED EXTRAPOLATION (delta ~ 2e-23 at 50 digits)")
print("=" * 78)
if np.isfinite(q):
    comb = p_floor * q
    print(f"  composed law: delta_min ~ eps^(p*q) = eps^{comb:.3f}")
    print(f"  the FILED figure assumed p*q = 1 * 0.5 = 0.500")
    eps50 = 1e-50
    filed = 3e-6 * np.sqrt(eps50 / eps64)
    remeas = 3e-6 * (eps50 / eps64) ** comb
    print(f"  delta_min at 50 digits, AS FILED     : {filed:.3g}")
    print(f"  delta_min at 50 digits, RE-DERIVED   : {remeas:.3g}")
    print(f"  the filed figure is optimistic by a factor {remeas/filed:.4g}")
print("  Either way the 50-digit number is an EXTRAPOLATION -- a law measured across a")
print("  5.4e8 precision change, applied far outside that range -- and must be recorded")
print("  as an extrapolation, never as a measurement.")
