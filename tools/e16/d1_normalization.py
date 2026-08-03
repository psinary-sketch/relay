# D-1 entry face: the normalization sub-problem.  All three points (K = 16, 32, 64) from
# the SAME truncated-object caches (the Jacobi coefficients nest); per K: resolved count,
# boundary-separated relative pair-energy bands, the four candidate normalizations'
# constants; the stability adjudication (max/min <= 1.25, stated in the report in advance).
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")

def load_atoms(path):
    with open(path) as f:
        return [mp.mpf(line.strip()) for line in f if line.strip()]

def load_jacobi(path):
    al, beta, mode = [], [], "AL"
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            if line == "BETA": mode = "BETA"; continue
            (al if mode == "AL" else beta).append(mp.mpf(line))
    return al, beta

def nodes(al, beta, k):
    J = mp.matrix(k, k)
    for i in range(k): J[i, i] = al[i]
    for i in range(k - 1):
        off = mp.sqrt(beta[i + 1]); J[i, i + 1] = off; J[i + 1, i] = off
    E = mp.eigsy(J, eigvals_only=True)
    return sorted([mp.mpf(E[i]) for i in range(k)], reverse=True)

def main():
    mp.mp.dps = 700
    gamZ = load_atoms(os.path.join(T, "shape_zeros.txt"))
    gamC = load_atoms(os.path.join(T, "shape_smooth.txt"))
    bZ = [1 / (2 * g) ** 2 for g in gamZ]
    bC = [1 / (2 * g) ** 2 for g in gamC]
    alZ, beZ = load_jacobi(os.path.join(T, "shape_jacobi_zeta.txt"))
    alC, beC = load_jacobi(os.path.join(T, "shape_jacobi_ctrl.txt"))
    rows = []
    for K in (16, 32, 64):
        lamZ = nodes(alZ, beZ, K); lamC = nodes(alC, beC, K)
        def resolved(lam, atoms):
            r = 0
            for j in range(K):
                if abs(lam[j] - atoms[j]) / atoms[j] < mp.mpf("0.01"): r = j + 1
                else: break
            return r
        R = min(resolved(lamZ, bZ), resolved(lamC, bC))
        def bands(lam):
            bnd = mp.mpf(0); osc = mp.mpf(0)
            for i in range(R):
                for j in range(i + 1, R):
                    t = 2 * mp.log(abs(lam[i] - lam[j]))
                    if i < 2: bnd += t
                    else: osc += t
            return bnd, osc
        bndZ, oscZ = bands(lamZ); bndC, oscC = bands(lamC)
        d_osc = oscZ - oscC
        n_osc_nodes = R - 2
        n_pairs = n_osc_nodes * (n_osc_nodes - 1) // 2
        harm = sum(mp.mpf(1) / (j - i) for i in range(2, R) for j in range(i + 1, R))
        rows.append((K, R, d_osc, bndZ - bndC, n_pairs, n_osc_nodes, harm))
        print(f"K={K}: R={R} | D-osc = {mp.nstr(d_osc, 6)} | D-bnd = {mp.nstr(bndZ - bndC, 6)}")
    print(f"\nraw exponent fit (D-osc ~ A * R^p) over the three points:")
    import math
    (K1, R1, d1, *_), (K2, R2, d2, *_), (K3, R3, d3, *_) = rows
    p12 = mp.log(d2 / d1) / mp.log(mp.mpf(R2 - 2) / (R1 - 2))
    p23 = mp.log(d3 / d2) / mp.log(mp.mpf(R3 - 2) / (R2 - 2))
    print(f"  p(16->32) = {mp.nstr(p12, 4)} | p(32->64) = {mp.nstr(p23, 4)}")
    print(f"\n{'form':>28} {'c(16)':>12} {'c(32)':>12} {'c(64)':>12} {'max/min':>9} {'STABLE?':>8}")
    forms = [("(a) per-pair C(R-2,2)", lambda r: r[4]),
             ("(b) per-gap R-2", lambda r: r[5]),
             ("(c) per log-window", lambda r: mp.log(r[5])),
             ("(d) harmonic pair-weight", lambda r: r[6])]
    for name, f in forms:
        cs = [r[2] / f(r) for r in rows]
        ratio = max(cs) / min(cs)
        print(f"{name:>28} {mp.nstr(cs[0], 5):>12} {mp.nstr(cs[1], 5):>12} "
              f"{mp.nstr(cs[2], 5):>12} {mp.nstr(ratio, 4):>9} "
              f"{'YES' if ratio <= mp.mpf('1.25') else 'no':>8}")

if __name__ == "__main__":
    main()
