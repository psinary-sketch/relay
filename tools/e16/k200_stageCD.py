# W-K200 Stages C+D: the five-point sequence (uniform object, nested blocks) +
# adjudication (i); the shape read at K=200 + adjudication (ii) per the pre-committed
# discriminant family.  Low-dps spectral read (the validated split).
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")
K = 200

def load_jacobi(path, dps):
    mp.mp.dps = dps
    al, beta, mode = [], [], "AL"
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            if line == "BETA": mode = "BETA"; continue
            (al if mode == "AL" else beta).append(mp.mpf(line))
    return al, beta

def load_atoms(path, n, dps):
    mp.mp.dps = dps
    with open(path) as f:
        v = [mp.mpf(line.strip()) for line in f if line.strip()]
    return v[:n]

def nodes(al, beta, k):
    J = mp.matrix(k, k)
    for i in range(k): J[i, i] = al[i]
    for i in range(k - 1):
        off = mp.sqrt(beta[i + 1]); J[i, i + 1] = off; J[i + 1, i] = off
    E = mp.eigsy(J, eigvals_only=True)
    return sorted([mp.mpf(E[i]) for i in range(k)], reverse=True)

def main():
    mp.mp.dps = 60
    alZ, beZ = load_jacobi(os.path.join(T, "k200_jacobi_zeta.txt"), 60)
    alC, beC = load_jacobi(os.path.join(T, "k200_jacobi_ctrl.txt"), 60)
    gamZ = load_atoms(os.path.join(T, "k200_zeros.txt"), 960, 60)
    gamC = load_atoms(os.path.join(T, "k200_smooth.txt"), 960, 60)
    aZ = [1 / (2 * g) ** 2 for g in gamZ]
    aC = [1 / (2 * g) ** 2 for g in gamC]
    cs = []
    lam200 = {}
    for k in (16, 32, 64, 128, 200):
        lamZ = nodes(alZ, beZ, k); lamC = nodes(alC, beC, k)
        def res(lam, atoms):
            r = 0
            for j in range(k):
                if abs(lam[j] - atoms[j]) / atoms[j] < mp.mpf("0.01"): r = j + 1
                else: break
            return r
        R = min(res(lamZ, aZ), res(lamC, aC))
        def osc(lam):
            v = mp.mpf(0)
            for i in range(2, R):
                for j in range(i + 1, R):
                    v += 2 * mp.log(abs(lam[i] - lam[j]))
            return v
        d = osc(lamZ) - osc(lamC)
        harm = sum(mp.mpf(1) / (j - i) for i in range(2, R) for j in range(i + 1, R))
        c = d / harm
        cs.append((k, R, c))
        if k == 200: lam200 = {"zeta": (lamZ, R), "ctrl": (lamC, R)}
        print(f"K={k}: R={R} | c = {mp.nstr(c, 6)}")
    # adjudication (i)
    vals = [c for _, _, c in cs]
    incs = [vals[i+1] - vals[i] for i in range(4)]
    ratios = [incs[i+1] / incs[i] for i in range(3)]
    print(f"increments: {[mp.nstr(x,4) for x in incs]}")
    print(f"ratios: {[mp.nstr(x,4) for x in ratios]}")
    r = ratios[-1]
    if r < 1:
        cinf = vals[-1] + incs[-1] * r / (1 - r)
        print(f"five-point geometric limit c_inf = {mp.nstr(cinf, 5)}")
        if mp.mpf("0.97") <= cinf <= mp.mpf("1.03"):
            print("ADJUDICATION (i): UNIT CONSTANT STANDS at five-point instrument grade")
        elif mp.mpf("0.85") <= cinf <= mp.mpf("1.05"):
            print("ADJUDICATION (i): certified-with-constant; the constant's value the datum")
        else:
            print("ADJUDICATION (i): RE-OPENS first-class")
    else:
        print("ADJUDICATION (i): no convergence — RE-OPENS first-class")
    # Stage D: the shape at K=200
    for tag in ("zeta", "ctrl"):
        lam, R = lam200[tag]
        g_nodes = [1 / (2 * mp.sqrt(l)) for l in lam[:R]]
        gaps = []
        for j in range(R - 1):
            raw = g_nodes[j + 1] - g_nodes[j]
            unf = raw * mp.log(g_nodes[j] / (2 * mp.pi)) / (2 * mp.pi)
            gaps.append(unf)
        n = len(gaps)
        mean = sum(gaps) / n
        sn = [x / mean for x in gaps]
        var = sum((x - 1) ** 2 for x in sn) / (n - 1)
        small = sum(1 for x in sn if x < mp.mpf("0.5")) / mp.mpf(n)
        # KS vs GUE Wigner surmise CDF: F(s) = 1 - exp(-4 s^2 / pi) * ... (unitary surmise)
        # P(s) = (32/pi^2) s^2 exp(-4 s^2/pi); F(s) = erf(2s/sqrt(pi)) - (4 s/pi) exp(-4 s^2/pi)
        def gue_cdf(s):
            return mp.erf(2 * s / mp.sqrt(mp.pi)) - (4 * s / mp.pi) * mp.e ** (-4 * s * s / mp.pi)
        ss = sorted(sn)
        ks = max(max(abs(gue_cdf(ss[i]) - mp.mpf(i) / n),
                     abs(gue_cdf(ss[i]) - mp.mpf(i + 1) / n)) for i in range(n))
        print(f"[{tag} K=200] gaps n={n} | Var = {mp.nstr(var, 4)} | D = "
              f"{mp.nstr(var / mp.mpf('0.180'), 4)} | small-gap = {mp.nstr(small, 3)} | "
              f"KS vs GUE = {mp.nstr(ks, 3)}")
    print("\n(adjudication (ii) against the pre-committed family: D in [0.65, 1.5]; "
          "small-gap in [0.02, 0.12]; KS <= 0.15)")

if __name__ == "__main__":
    main()
