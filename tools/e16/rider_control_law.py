# THE REGISTERED FREE RIDER — the control's convergence law.
# The rider object (construction fixed in advance, relay 015c501): the HEIGHT-MATCHED
# SURMISE control — positions from the banked smooth atoms' density with unfolded gaps
# sampled from the GUE Wigner surmise, mean-normalized, deterministic seed 20260804,
# atoms by cumulative sums (no zero-finding).  Its RELATIVE c-sequence against the smooth
# control (= pair structure WITHOUT arithmetic) at the same K-ladder, fitted against the
# same pre-committed family set under the same criterion.
# Stages: atoms -> moments -> checkpointed factorization -> read -> fit.  Re-runnable.
import os, sys, importlib.util, pathlib, math, random
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "bc", str(pathlib.Path(__file__).with_name("blocked_cholesky.py")))
bc = importlib.util.module_from_spec(spec); sys.modules["bc"] = bc; spec.loader.exec_module(bc)

T = os.environ.get("TEMP", ".")
K = 256
DPS = 2700
J = 1200
APATH = os.path.join(T, "rider_surmise.txt")
MPATH = os.path.join(T, "rider_moments.txt")
JPATH = os.path.join(T, "rider_jacobi.txt")
CK = os.path.join(T, "rider_chol.ckpt")

def gue_sample(rng):
    """Wigner surmise (unitary) sample, mean 1: inverse CDF by bisection."""
    u = rng.random()
    F = lambda s: math.erf(2 * s / math.sqrt(math.pi)) - (4 * s / math.pi) * math.exp(-4 * s * s / math.pi)
    lo, hi = 0.0, 6.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if F(mid) < u: lo = mid
        else: hi = mid
    return (lo + hi) / 2

def build_atoms():
    if os.path.exists(APATH):
        return
    rng = random.Random(20260804)
    with open(os.path.join(T, "k256_smooth.txt")) as f:
        first = float(f.readline().strip())
    g = first
    out = [g]
    while len(out) < J:
        dens = math.log(g / (2 * math.pi)) / (2 * math.pi)   # mean density at height g
        g = g + gue_sample(rng) / dens
        out.append(g)
    mp.mp.dps = DPS
    with open(APATH, "w") as f:
        for x in out:
            f.write(mp.nstr(mp.mpf(repr(x)), 30) + "\n")   # the object is EXACTLY these values
    print("rider atoms banked")

def get_moments():
    mp.mp.dps = DPS
    if os.path.exists(MPATH):
        with open(MPATH) as f:
            return [None] + [mp.mpf(l.strip()) for l in f if l.strip()]
    with open(APATH) as f:
        gam = [mp.mpf(l.strip()) for l in f if l.strip()][:J]
    betas = [1 / (2 * g) ** 2 for g in gam]
    s = [sum(b ** k for b in betas) for k in range(1, 2 * K + 2)]
    with open(MPATH, "w") as f:
        for x in s: f.write(mp.nstr(x, DPS) + "\n")
    print("rider moments banked")
    return [None] + s

def main():
    build_atoms()
    mp.mp.dps = DPS
    if not os.path.exists(JPATH):
        s = get_moments()
        Gf = lambda i, j: s[i + j + 1]
        R = bc.blocked_cholesky(Gf, K + 1, CK, block=16, max_blocks=5)
        if R is None:
            print("rider Cholesky in progress — RERUN"); return
        al, beta = bc.jacobi_from_R(R, K, s[1])
        with open(JPATH, "w") as f:
            for a in al: f.write(mp.nstr(a, DPS) + "\n")
            f.write("BETA\n")
            for b in beta: f.write(mp.nstr(b, DPS) + "\n")
        os.remove(CK)
        print("rider Jacobi banked")
    # the read: rider vs smooth control, same ladder
    mp.mp.dps = 60
    def load_j(p):
        al, be, mode = [], [], "AL"
        with open(p) as f:
            for line in f:
                line = line.strip()
                if not line: continue
                if line == "BETA": mode = "BETA"; continue
                (al if mode == "AL" else be).append(mp.mpf(line))
        return al, be
    alR, beR = load_j(JPATH)
    alC, beC = load_j(os.path.join(T, "k256_jacobi_ctrl.txt"))
    def load_a(p):
        with open(p) as f:
            return [mp.mpf(l.strip()) for l in f if l.strip()][:J]
    aR = [1 / (2 * g) ** 2 for g in load_a(APATH)]
    aC = [1 / (2 * g) ** 2 for g in load_a(os.path.join(T, "k256_smooth.txt"))]
    def nodes(al, be, k):
        Jm = mp.matrix(k, k)
        for i in range(k): Jm[i, i] = al[i]
        for i in range(k - 1):
            off = mp.sqrt(be[i + 1]); Jm[i, i + 1] = off; Jm[i + 1, i] = off
        E = mp.eigsy(Jm, eigvals_only=True)
        return sorted([mp.mpf(E[i]) for i in range(k)], reverse=True)
    cs = []
    for k in (16, 32, 64, 128, 200, 256):
        lamR = nodes(alR, beR, k); lamC = nodes(alC, beC, k)
        def res(lam, atoms):
            r = 0
            for j in range(k):
                if abs(lam[j] - atoms[j]) / atoms[j] < mp.mpf("0.01"): r = j + 1
                else: break
            return r
        R_ = min(res(lamR, aR), res(lamC, aC))
        def osc(lam):
            v = mp.mpf(0)
            for i in range(2, R_):
                for j in range(i + 1, R_):
                    v += 2 * mp.log(abs(lam[i] - lam[j]))
            return v
        d = osc(lamR) - osc(lamC)
        harm = sum(mp.mpf(1) / (j - i) for i in range(2, R_) for j in range(i + 1, R_))
        c = d / harm
        cs.append((k, R_, c))
        print(f"RIDER K={k}: R={R_} | c = {mp.nstr(c, 6)}")
    # the fit: same families, same criterion (LOO on the last point)
    K_ = [x[0] for x in cs]; C_ = [x[2] for x in cs]
    def lsq(xs, ys):
        n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
        b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
        return my - b * mx, b
    print("\nRIDER FIT (families on the first five, LOO predicting the sixth):")
    inc = [C_[i+1] - C_[i] for i in range(4)]
    rho = sum(inc[i+1] / inc[i] for i in range(3)) / 3
    pred_g = C_[4] + inc[3] * rho
    cinf_g = C_[4] + inc[3] * rho / (1 - rho) if rho < 1 else mp.mpf('nan')
    print(f"  (a) geometric: LOO pred {mp.nstr(pred_g,6)} | err {mp.nstr(pred_g - C_[5],3)} "
          f"| c_inf {mp.nstr(cinf_g,5)}")
    for name, fx in (("(c) A logK/K", lambda k: mp.log(k) / k), ("(d) A/logK", lambda k: 1 / mp.log(k))):
        xs = [fx(k) for k in K_[:5]]
        a, b = lsq(xs, C_[:5])
        pred = a + b * fx(256)
        print(f"  {name}: LOO pred {mp.nstr(pred,6)} | err {mp.nstr(pred - C_[5],3)} "
              f"| c_inf {mp.nstr(a,5)}")

if __name__ == "__main__":
    main()
