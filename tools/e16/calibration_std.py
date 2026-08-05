# ITEM 4 — THE CALIBRATION STANDARD.
# Object CAL = the smooth control with ONE atom displaced by a known amount (atom #60,
# +0.30 x its local gap).  In the resolved band the Gauss nodes equal the atoms to <1%,
# so the pair-energy change is ANALYTICALLY KNOWN from the atom positions:
#   Delta_osc_exact(R) = sum_{j in band, j != m} 2[ log|b'_m - b_j| - log|b_m - b_j| ]
# (restricted to the band's pair set, i.e. indices 2..R-1, the same set the statistic uses).
# The pipeline (moments -> blocked Cholesky at dps 2700 -> eigen -> band -> statistic) is
# run on CAL vs the smooth control and its measured Delta_osc compared to the exact value.
# The gap between them IS the pipeline's bias on this statistic, at each ladder point.
# SCOPE (stated): this calibrates the measurement chain against an exact answer for a known
# displacement; it does not calibrate sensitivity to global fluctuation structure.
import os, sys, importlib.util, pathlib
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "bc", str(pathlib.Path(__file__).with_name("blocked_cholesky.py")))
bc = importlib.util.module_from_spec(spec); sys.modules["bc"] = bc; spec.loader.exec_module(bc)

T = os.environ.get("TEMP", ".")
K, DPS, J = 256, 2700, 1200
M = 59                       # 0-based index of the displaced atom (rank 60)
FRAC = mp.mpf("0.30")        # displacement as a fraction of the local gap
APATH = os.path.join(T, "cal_atoms.txt")
MPATH = os.path.join(T, "cal_moments.txt")
JPATH = os.path.join(T, "cal_jacobi.txt")
CK = os.path.join(T, "cal_chol.ckpt")

def load_a(p, n):
    with open(p) as f:
        return [mp.mpf(l.strip()) for l in f if l.strip()][:n]

def build():
    mp.mp.dps = DPS
    if os.path.exists(APATH): return
    g = load_a(os.path.join(T, "k256_smooth.txt"), J)
    gap = g[M + 1] - g[M]
    g2 = list(g)
    g2[M] = g[M] + FRAC * gap
    with open(APATH, "w") as f:
        for x in g2: f.write(mp.nstr(x, DPS) + "\n")
    print(f"cal atoms banked (atom {M+1} moved +{mp.nstr(FRAC,3)} local gap)")

def moments():
    mp.mp.dps = DPS
    if os.path.exists(MPATH):
        with open(MPATH) as f:
            return [None] + [mp.mpf(l.strip()) for l in f if l.strip()]
    gam = load_a(APATH, J)
    betas = [1 / (2 * x) ** 2 for x in gam]
    s = [sum(b ** k for b in betas) for k in range(1, 2 * K + 2)]
    with open(MPATH, "w") as f:
        for x in s: f.write(mp.nstr(x, DPS) + "\n")
    print("cal moments banked")
    return [None] + s

def load_j(p):
    al, be, mode = [], [], "AL"
    with open(p) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            if line == "BETA": mode = "BETA"; continue
            (al if mode == "AL" else be).append(mp.mpf(line))
    return al, be

def main():
    build()
    mp.mp.dps = DPS
    if not os.path.exists(JPATH):
        s = moments()
        Gf = lambda i, j: s[i + j + 1]
        R = bc.blocked_cholesky(Gf, K + 1, CK, block=16, max_blocks=5)
        if R is None:
            print("cal Cholesky in progress — RERUN"); return
        al, beta = bc.jacobi_from_R(R, K, s[1])
        with open(JPATH, "w") as f:
            for a in al: f.write(mp.nstr(a, DPS) + "\n")
            f.write("BETA\n")
            for b in beta: f.write(mp.nstr(b, DPS) + "\n")
        os.remove(CK)
        print("cal Jacobi banked")
    mp.mp.dps = 60
    alA, beA = load_j(JPATH)
    alC, beC = load_j(os.path.join(T, "k256_jacobi_ctrl.txt"))
    bA = [1 / (2 * g) ** 2 for g in load_a(APATH, J)]
    bC = [1 / (2 * g) ** 2 for g in load_a(os.path.join(T, "k256_smooth.txt"), J)]
    def nodes(al, be, k):
        Jm = mp.matrix(k, k)
        for i in range(k): Jm[i, i] = al[i]
        for i in range(k - 1):
            off = mp.sqrt(be[i + 1]); Jm[i, i + 1] = off; Jm[i + 1, i] = off
        E = mp.eigsy(Jm, eigvals_only=True)
        return sorted([mp.mpf(E[i]) for i in range(k)], reverse=True)
    print(f"\n{'K':>5} {'R':>5} {'measured':>14} {'exact':>14} {'bias':>12} {'bias/0.0182':>12}")
    for k in (64, 128, 200, 256):
        lamA = nodes(alA, beA, k); lamC = nodes(alC, beC, k)
        def res(lam, atoms):
            r = 0
            for j in range(k):
                if abs(lam[j] - atoms[j]) / atoms[j] < mp.mpf("0.01"): r = j + 1
                else: break
            return r
        R = min(res(lamA, bA), res(lamC, bC))
        def osc(lam):
            v = mp.mpf(0)
            for i in range(2, R):
                for j in range(i + 1, R):
                    v += 2 * mp.log(abs(lam[i] - lam[j]))
            return v
        meas = osc(lamA) - osc(lamC)
        exact = mp.mpf(0)
        if 2 <= M < R:
            for j in range(2, R):
                if j == M: continue
                exact += 2 * (mp.log(abs(bA[M] - bC[j])) - mp.log(abs(bC[M] - bC[j])))
        harm = sum(mp.mpf(1) / (j - i) for i in range(2, R) for j in range(i + 1, R))
        bias_c = (meas - exact) / harm
        print(f"{k:>5} {R:>5} {mp.nstr(meas,8):>14} {mp.nstr(exact,8):>14} "
              f"{mp.nstr(bias_c,3):>12} {mp.nstr(abs(bias_c)/mp.mpf('0.0182'),3):>12}")
    print("\n(bias reported in c-units — directly comparable to the 0.0182 prediction separation)")

if __name__ == "__main__":
    main()
