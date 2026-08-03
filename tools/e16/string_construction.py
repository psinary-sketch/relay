# E-20 — THE STRING CONSTRUCTION.
# The Krein-string/Jacobi data of the zero-moment measure nu = sum_j beta_j delta_{beta_j},
# beta_j = 1/(2 gamma_j)^2, computed from the moments m_k = s_{k+1} (pairing <x^i,x^j> =
# s_{i+j+1}) at increasing Hankel truncation.  Monic-OP recurrence (alpha_k, beta_k) via
# Cholesky of the moment Gram.  DOUBLY-SOURCED: (A) the integral route (H_0 Taylor moments,
# dps 150 — E-16's machinery) vs (B) explicit zero-sums over 500 zeros + smooth-density tail
# correction.  Determinacy is FREE (bounded support).  Output: the Jacobi table at depths
# 5/6/7, source agreement, and the audit cells vs xi's constraints.

import importlib.util, sys, pathlib
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "hb", str(pathlib.Path(__file__).with_name("hankel_bridge.py")))
hb = importlib.util.module_from_spec(spec); sys.modules["hb"] = hb; spec.loader.exec_module(hb)

def zero_route(kmax, J=500):
    mp.mp.dps = 40
    zs = [mp.zetazero(j).imag for j in range(1, J + 1)]
    s = [None] * (kmax + 1)
    gJ = zs[-1]
    for k in range(1, kmax + 1):
        base = sum((2 * g) ** (-2 * k) for g in zs)
        # smooth-density tail: integral_{gJ}^inf rho(g) (2g)^{-2k} dg, rho = log(g/2pi)/2pi
        tail = mp.quad(lambda g: mp.log(g / (2 * mp.pi)) / (2 * mp.pi) * (2 * g) ** (-2 * k),
                       [gJ, 10 * gJ, mp.inf])
        s[k] = base + tail
    return s

def jacobi_from_moments(s, depth):
    """Monic OP recurrence for the measure with Gram G_{ij} = s[i+j+1], via Cholesky."""
    G = mp.matrix(depth + 1, depth + 1)
    for i in range(depth + 1):
        for j in range(depth + 1):
            G[i, j] = s[i + j + 1]
    R = mp.cholesky(G).T          # upper triangular, G = R^T R
    alpha, beta = [], []
    for k in range(depth):
        t1 = R[k, k + 1] / R[k, k] if k + 1 <= depth else mp.mpf(0)
        t0 = R[k - 1, k] / R[k - 1, k - 1] if k >= 1 else mp.mpf(0)
        alpha.append(t1 - t0)
        if k >= 1:
            beta.append((R[k, k] / R[k - 1, k - 1]) ** 2)
    return alpha, beta

def main():
    kmax = 15
    mp.mp.dps = 150
    sA = hb.power_sums(mp.mpf(0), kmax)
    sB = zero_route(kmax)
    mp.mp.dps = 40
    print("=== moment agreement (integral route vs zeros+tail) ===")
    for k in (1, 2, 3, 5, 8):
        rel = abs(sA[k] - sB[k]) / abs(sA[k])
        print(f"  s_{k}: A = {mp.nstr(sA[k], 10)}  B = {mp.nstr(sB[k], 10)}  rel = {mp.nstr(rel, 3)}")
    print(f"\nmass cell: s_1 (A) = {mp.nstr(sA[1], 10)}; 4*s_1 = {mp.nstr(4*sA[1], 10)} "
          f"(the classical Sum 1/gamma^2)")
    print(f"spectral edge: beta_1 = 1/(2 gamma_1)^2 = {mp.nstr(1/(2*mp.zetazero(1).imag)**2, 10)}")
    print("\n=== the Jacobi/string table (monic recurrence), by source and depth ===")
    for name, s in (("A(integral)", sA), ("B(zeros+tail)", sB)):
        for depth in (5, 6, 7):
            try:
                al, be = jacobi_from_moments([None] + [mp.mpf(x) for x in s[1:]], depth)
                print(f"[{name} d={depth}] alpha = {[mp.nstr(a, 8) for a in al[:5]]}")
                print(f"{'':14}  beta  = {[mp.nstr(b, 8) for b in be[:4]]}")
            except Exception as ex:
                print(f"[{name} d={depth}] Cholesky failed: {ex}")
    print("\n(alpha_k should sit inside (0, beta_1]; beta_k > 0 = the string's positivity)")

if __name__ == "__main__":
    main()
