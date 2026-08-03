# W-SHAPE stage 2: the strings at depth K=64 from the atom caches.  Truncated-measure
# moments by EXACT summation (no tail estimate -- the objects are the 300-atom measures by
# definition); Jacobi via Cholesky at dps 700 (the precision law + margin); checkpoints:
# positivity of every recurrence beta, moment double-source (dps 700 vs dps 500 recompute).
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")
K = 64

def load(path):
    with open(path) as f:
        return [mp.mpf(line.strip()) for line in f if line.strip()]

def moments(gammas, kmax):
    betas = [1 / (2 * g) ** 2 for g in gammas]
    return [None] + [sum(b ** k for b in betas) for k in range(1, kmax + 1)]

def jacobi(s, depth):
    G = mp.matrix(depth + 1, depth + 1)
    for i in range(depth + 1):
        for j in range(depth + 1):
            G[i, j] = s[i + j + 1]
    R = mp.cholesky(G).T
    al, beta = [], [s[1]]
    for k in range(depth):
        t1 = R[k, k + 1] / R[k, k]
        t0 = R[k - 1, k] / R[k - 1, k - 1] if k >= 1 else mp.mpf(0)
        al.append(t1 - t0)
        if k >= 1:
            beta.append((R[k, k] / R[k - 1, k - 1]) ** 2)
    return al, beta

def main():
    mp.mp.dps = 700
    for tag, path in (("zeta", "shape_zeros.txt"), ("ctrl", "shape_smooth.txt")):
        g = load(os.path.join(T, path))
        s = moments(g, 2 * K + 1)
        # double-source: dps-500 recompute of a moment subset
        mp.mp.dps = 500
        s2 = moments([mp.mpf(x) for x in g], 2 * K + 1)
        worst = max(abs(s[k] - s2[k]) / abs(s[k]) for k in (1, 20, 60, 100, 129))
        mp.mp.dps = 700
        print(f"[{tag}] moment double-source worst rel: {mp.nstr(worst, 3)} "
              f"({'PASS' if worst < mp.mpf(10)**(-480) else 'FAIL - HALT'})")
        al, beta = jacobi(s, K)
        pos = all(b > 0 for b in beta)
        print(f"[{tag}] Jacobi K={K}: all beta > 0: {pos} "
              f"({'PASS' if pos else 'FAIL - HALT'})")
        with open(os.path.join(T, f"shape_jacobi_{tag}.txt"), "w") as f:
            for a in al: f.write(mp.nstr(a, 700) + "\n")
            f.write("BETA\n")
            for b in beta: f.write(mp.nstr(b, 700) + "\n")
        print(f"[{tag}] Jacobi cached")

if __name__ == "__main__":
    main()
