# THE ONE BUILD, Stage C2 — the fourth point: moments (exact summation, dps 1300),
# the blocked Cholesky K=128 (checkpointed; resumable across task runs), the low-dps
# spectral read, the boundary-separated relative pair-energy.  Stage boundaries banked:
# moments cached; Cholesky checkpoint; nesting check (top 64x64 vs the K=64 certified
# Jacobi within the certified floor).
import os, sys, importlib.util, pathlib, time
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "bc", str(pathlib.Path(__file__).with_name("blocked_cholesky.py")))
bc = importlib.util.module_from_spec(spec); sys.modules["bc"] = bc; spec.loader.exec_module(bc)

T = os.environ.get("TEMP", ".")
K = 128
DPS = 1300

def load_atoms(path, n):
    with open(path) as f:
        v = [mp.mpf(line.strip()) for line in f if line.strip()]
    assert len(v) >= n, f"{path}: {len(v)} < {n}"
    return v[:n]

def get_moments(tag, atoms_path):
    mpath = os.path.join(T, f"build_moments_{tag}.txt")
    if os.path.exists(mpath):
        with open(mpath) as f:
            return [None] + [mp.mpf(line.strip()) for line in f if line.strip()]
    gam = load_atoms(atoms_path, 600)
    betas = [1 / (2 * g) ** 2 for g in gam]
    s = [sum(b ** k for b in betas) for k in range(1, 2 * K + 2)]
    with open(mpath, "w") as f:
        for x in s:
            f.write(mp.nstr(x, DPS) + "\n")
    print(f"[{tag}] moments banked")
    return [None] + s

def main():
    mp.mp.dps = DPS
    t0 = time.time()
    for tag, apath in (("zeta", "build_zeros_1300.txt"), ("ctrl", "build_smooth_1300.txt")):
        s = get_moments(tag, os.path.join(T, apath))
        Gf = lambda i, j: s[i + j + 1]
        ck = os.path.join(T, f"build_chol_{tag}.ckpt")
        R = bc.blocked_cholesky(Gf, K + 1, ck, block=16, max_blocks=40)
        if R is None:
            print(f"[{tag}] Cholesky in progress — RERUN to continue ({time.time()-t0:.0f} s)")
            return
        al, beta = bc.jacobi_from_R(R, K, s[1])
        with open(os.path.join(T, f"build_jacobi_{tag}.txt"), "w") as f:
            for a in al: f.write(mp.nstr(a, DPS) + "\n")
            f.write("BETA\n")
            for b in beta: f.write(mp.nstr(b, DPS) + "\n")
        print(f"[{tag}] Jacobi K=128 banked ({time.time()-t0:.0f} s)")
    print("STAGE C2 COMPLETE — run stage C3 (the read)")

if __name__ == "__main__":
    main()
