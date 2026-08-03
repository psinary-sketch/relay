# E-20 face 3 — THE CONTINUUM-LIMIT AUDIT: the string at depth 16 (dps 400, precision law),
# its growth/spacing structure vs the zero-density constraint.
# Computable continuum cells: (a) the resolved-node count trend (~d/2); (b) THE TRACKING LAW:
# alpha_k vs beta_k = 1/(2 gamma_k)^2 — the string's diagonal following the zero scale is the
# discrete shadow of the Hamiltonian-growth <-> density relation; (c) the tail-cluster edge
# vs the density integral.  Source A (integral route) at dps 400.

import importlib.util, sys, pathlib
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "hb", str(pathlib.Path(__file__).with_name("hankel_bridge.py")))
hb = importlib.util.module_from_spec(spec); sys.modules["hb"] = hb; spec.loader.exec_module(hb)
spec2 = importlib.util.spec_from_file_location(
    "sc", str(pathlib.Path(__file__).with_name("string_construction.py")))
sc = importlib.util.module_from_spec(spec2); sys.modules["sc"] = sc; spec2.loader.exec_module(sc)

def main():
    depth = 16
    mp.mp.dps = 400
    sA = hb.power_sums(mp.mpf(0), 2 * depth + 1)
    al, be = sc.jacobi_from_moments(sA, depth)
    mp.mp.dps = 40
    zs = [mp.zetazero(j).imag for j in range(1, depth + 5)]
    betas = [1 / (2 * g) ** 2 for g in zs]
    print(f"=== depth-{depth} string (dps 400) ===")
    print(f"alpha_k: {[mp.nstr(a, 6) for a in al]}")
    print(f"beta_k : {[mp.nstr(b, 6) for b in be]}")
    print("\n=== THE TRACKING LAW: alpha_k vs beta_k (the zero scale at rank k) ===")
    print(f"{'k':>3} {'alpha_k':>14} {'beta_k(zero)':>14} {'ratio':>8}")
    for k in range(depth):
        r = al[k] / betas[k]
        print(f"{k+1:>3} {mp.nstr(al[k], 8):>14} {mp.nstr(betas[k], 8):>14} {mp.nstr(r, 5):>8}")
    # node test at depth 16
    def nodes(alpha, beta):
        d = len(alpha)
        J = mp.matrix(d, d)
        for i in range(d): J[i, i] = alpha[i]
        for i in range(d - 1):
            off = mp.sqrt(beta[i]); J[i, i+1] = off; J[i+1, i] = off
        E = mp.eigsy(J, eigvals_only=True)
        return sorted([mp.mpf(x) for x in E], reverse=True)
    nd = nodes(al, be)
    print("\n=== node test at depth 16 (resolved range) ===")
    resolved = 0
    for j in range(depth):
        rel = abs(nd[j] - betas[j]) / betas[j]
        mark = "RESOLVED" if rel < mp.mpf("0.01") else "tail-cluster"
        if rel < mp.mpf("0.01"): resolved += 1
        print(f"  node {j+1}: rel diff {mp.nstr(rel, 3)}  [{mark}]")
    print(f"\nresolved-node count at depth 16: {resolved} (depth 12 gave 6; trend ~ d/2)")

if __name__ == "__main__":
    main()
