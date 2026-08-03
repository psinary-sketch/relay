# E-20 face 2 — THE ASYMPTOTIC AUDIT.
# The string pushed to depth 12 (dps 250, source A = integral route) and depth 6 (source B =
# zeros+tail); the sharpest test: the Gauss/Jacobi NODES of the truncated string against the
# actual beta_j = 1/(2 gamma_j)^2 — the determinate reconstruction's convergence audited;
# trend cells (alpha_k, beta_k -> 0 with the accumulation) reported.

import importlib.util, sys, pathlib
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "hb", str(pathlib.Path(__file__).with_name("hankel_bridge.py")))
hb = importlib.util.module_from_spec(spec); sys.modules["hb"] = hb; spec.loader.exec_module(hb)
spec2 = importlib.util.spec_from_file_location(
    "sc", str(pathlib.Path(__file__).with_name("string_construction.py")))
sc = importlib.util.module_from_spec(spec2); sys.modules["sc"] = sc; spec2.loader.exec_module(sc)

def nodes_from_jacobi(alpha, beta):
    d = len(alpha)
    J = mp.matrix(d, d)
    for i in range(d):
        J[i, i] = alpha[i]
    for i in range(d - 1):
        off = mp.sqrt(beta[i])
        J[i, i + 1] = off
        J[i + 1, i] = off
    E = mp.eigsy(J, eigvals_only=True)
    return sorted([mp.mpf(x) for x in E], reverse=True)

def main():
    mp.mp.dps = 250
    depth = 12
    sA = hb.power_sums(mp.mpf(0), 2 * depth + 1)
    al, be = sc.jacobi_from_moments(sA, depth)
    mp.mp.dps = 40
    print(f"=== source A (integral, dps 250), depth {depth} ===")
    print(f"alpha_k: {[mp.nstr(a, 6) for a in al]}")
    print(f"beta_k : {[mp.nstr(b, 6) for b in be]}")
    print(f"alpha monotone->0 beyond k=2: {all(al[i] > al[i+1] > 0 for i in range(2, len(al)-1))}")
    print(f"beta all positive, decreasing: {all(be[i] > be[i+1] > 0 for i in range(len(be)-1))}")
    nodesA = nodes_from_jacobi(al, be)
    zs = [mp.zetazero(j).imag for j in range(1, depth + 3)]
    betas = [1 / (2 * g) ** 2 for g in zs]
    print("\n=== THE NODE TEST: Gauss nodes of the depth-12 string vs the actual zeros ===")
    print(f"{'j':>3} {'node_j':>16} {'beta_j (zero)':>16} {'rel diff':>12}")
    for j in range(depth):
        rel = abs(nodesA[j] - betas[j]) / betas[j]
        print(f"{j+1:>3} {mp.nstr(nodesA[j], 10):>16} {mp.nstr(betas[j], 10):>16} "
              f"{mp.nstr(rel, 3):>12}")
    print("\n=== source B (zeros+tail, depth 6) cross-check on the top nodes ===")
    sB = sc.zero_route(13)
    alB, beB = sc.jacobi_from_moments([None] + [mp.mpf(x) for x in sB[1:]], 6)
    nodesB = nodes_from_jacobi(alB, beB)
    for j in range(4):
        rel = abs(nodesB[j] - betas[j]) / betas[j]
        print(f"  node {j+1}: {mp.nstr(nodesB[j], 10)} vs {mp.nstr(betas[j], 10)} "
              f"| rel {mp.nstr(rel, 3)}")

if __name__ == "__main__":
    main()
