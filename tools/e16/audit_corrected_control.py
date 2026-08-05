# W-CONTROL-AUDIT item 3 — the OFFSET-CORRECTED (position-matched) control.
# The old control solved N(gamma)=j (density-matched only).  The corrected control solves
# N(gamma) = j + a with a = mean_band(N(gamma_j) - j): its counting function agrees with
# zeta's POINTWISE on average, not merely asymptotically.  Built at J=1200, dps 2700, then
# factorized to K=256 (checkpointed) so every exposed row re-derives from one build.
import os, sys, importlib.util, pathlib
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "bc", str(pathlib.Path(__file__).with_name("blocked_cholesky.py")))
bc = importlib.util.module_from_spec(spec); sys.modules["bc"] = bc; spec.loader.exec_module(bc)

T = os.environ.get("TEMP", ".")
K, DPS, J = 256, 2700, 1200
APATH = os.path.join(T, "corr_atoms.txt")
MPATH = os.path.join(T, "corr_moments.txt")
JPATH = os.path.join(T, "corr_jacobi.txt")
CK = os.path.join(T, "corr_chol.ckpt")

def Nf(g):
    return g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8

def build():
    mp.mp.dps = DPS
    if os.path.exists(APATH): return
    with open(os.path.join(T, "k256_zeros.txt")) as f:
        gz = [mp.mpf(l.strip()) for l in f if l.strip()][:J]
    a = sum(Nf(g) - (i + 1) for i, g in enumerate(gz)) / J
    print(f"position-match offset a = {mp.nstr(a, 8)}")
    out = []
    for j in range(1, J + 1):
        target = mp.mpf(j) + a
        f = lambda g: Nf(g) - target
        g0 = gz[j - 1]
        out.append(mp.findroot(f, g0))
    with open(APATH, "w") as f:
        for x in out: f.write(mp.nstr(x, DPS) + "\n")
    print("corrected-control atoms banked")

def main():
    build()
    mp.mp.dps = DPS
    if os.path.exists(JPATH):
        print("corrected Jacobi already banked"); return
    if os.path.exists(MPATH):
        with open(MPATH) as f:
            s = [None] + [mp.mpf(l.strip()) for l in f if l.strip()]
    else:
        with open(APATH) as f:
            gam = [mp.mpf(l.strip()) for l in f if l.strip()][:J]
        betas = [1 / (2 * g) ** 2 for g in gam]
        s = [None] + [sum(b ** k for b in betas) for k in range(1, 2 * K + 2)]
        with open(MPATH, "w") as f:
            for x in s[1:]: f.write(mp.nstr(x, DPS) + "\n")
        print("corrected moments banked")
    Gf = lambda i, j: s[i + j + 1]
    R = bc.blocked_cholesky(Gf, K + 1, CK, block=16, max_blocks=5)
    if R is None:
        print("corrected Cholesky in progress — RERUN"); return
    al, beta = bc.jacobi_from_R(R, K, s[1])
    with open(JPATH, "w") as f:
        for x in al: f.write(mp.nstr(x, DPS) + "\n")
        f.write("BETA\n")
        for x in beta: f.write(mp.nstr(x, DPS) + "\n")
    os.remove(CK)
    print("corrected Jacobi K=256 banked — STAGE COMPLETE")

if __name__ == "__main__":
    main()
