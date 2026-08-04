# THE SIXTH POINT Stage B: moments (exact summation, dps 2700) + blocked K=256
# factorizations, both objects, checkpointed; run repeatedly until STAGE B COMPLETE.
import os, sys, importlib.util, pathlib, time
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "bc", str(pathlib.Path(__file__).with_name("blocked_cholesky.py")))
bc = importlib.util.module_from_spec(spec); sys.modules["bc"] = bc; spec.loader.exec_module(bc)

T = os.environ.get("TEMP", ".")
K = 256
DPS = 2700
J = 1200

def load_atoms(path):
    with open(path) as f:
        v = [mp.mpf(line.strip()) for line in f if line.strip()]
    assert len(v) >= J, f"{path}: {len(v)} < {J}"
    return v[:J]

def get_moments(tag, apath):
    mpath = os.path.join(T, f"k256_moments_{tag}.txt")
    if os.path.exists(mpath):
        with open(mpath) as f:
            return [None] + [mp.mpf(line.strip()) for line in f if line.strip()]
    gam = load_atoms(os.path.join(T, apath))
    betas = [1 / (2 * g) ** 2 for g in gam]
    s = [sum(b ** k for b in betas) for k in range(1, 2 * K + 2)]
    with open(mpath, "w") as f:
        for x in s: f.write(mp.nstr(x, DPS) + "\n")
    print(f"[{tag}] moments banked")
    return [None] + s

def main():
    mp.mp.dps = DPS
    t0 = time.time()
    for tag, apath in (("zeta", "k256_zeros.txt"), ("ctrl", "k256_smooth.txt")):
        jpath = os.path.join(T, f"k256_jacobi_{tag}.txt")
        if os.path.exists(jpath):
            print(f"[{tag}] already banked"); continue
        s = get_moments(tag, apath)
        Gf = lambda i, j: s[i + j + 1]
        ck = os.path.join(T, f"k256_chol_{tag}.ckpt")
        R = bc.blocked_cholesky(Gf, K + 1, ck, block=16, max_blocks=5)
        if R is None:
            print(f"[{tag}] Cholesky in progress — RERUN ({time.time()-t0:.0f} s)"); return
        al, beta = bc.jacobi_from_R(R, K, s[1])
        with open(jpath, "w") as f:
            for a in al: f.write(mp.nstr(a, DPS) + "\n")
            f.write("BETA\n")
            for b in beta: f.write(mp.nstr(b, DPS) + "\n")
        os.remove(ck)
        print(f"[{tag}] Jacobi K=256 banked ({time.time()-t0:.0f} s)")
    print("STAGE B COMPLETE")

if __name__ == "__main__":
    main()
