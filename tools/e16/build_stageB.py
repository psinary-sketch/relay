# THE ONE BUILD, Stage B — VALIDATION FIRST (the mandatory gate).
# (1) The new blocked engine rebuilds the K=64 Jacobi data from the existing 300-atom
#     caches at dps 700; compared against the certified shape_jacobi_{zeta,ctrl}.txt.
# (2) The precision-split validated: the low-dps (60) spectral read reproduces the
#     certified D-osc triple (5.0374 / 25.3793 / 87.012) to 1e-4.
# A mismatch halts and files.
import os, sys, importlib.util, pathlib
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "bc", str(pathlib.Path(__file__).with_name("blocked_cholesky.py")))
bc = importlib.util.module_from_spec(spec); sys.modules["bc"] = bc; spec.loader.exec_module(bc)

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

def main():
    mp.mp.dps = 700
    K = 64
    results = {}
    for tag, apath, jpath in (("zeta", "shape_zeros.txt", "shape_jacobi_zeta.txt"),
                              ("ctrl", "shape_smooth.txt", "shape_jacobi_ctrl.txt")):
        gam = load_atoms(os.path.join(T, apath))
        betas = [1 / (2 * g) ** 2 for g in gam]
        s = [None] + [sum(b ** k * 1 for b in (betas)) if False else None for k in range(1)]
        s = [None] + [sum(b ** k for b in betas) for k in range(1, 2 * K + 2)]
        # measure has weight beta at point beta: moments m_k = sum beta^{k+1} = s_{k+1}
        Gf = lambda i, j: s[i + j + 1]
        ck = os.path.join(T, f"build_B_{tag}.ckpt")
        if os.path.exists(ck): os.remove(ck)
        R = bc.blocked_cholesky(Gf, K + 1, ck, block=16)
        al, beta = bc.jacobi_from_R(R, K, s[1])
        alC, betaC = load_jacobi(os.path.join(T, jpath))
        worst = max(max(abs(al[k] - alC[k]) / abs(alC[k]) for k in range(K)),
                    max(abs(beta[k] - betaC[k]) / abs(betaC[k]) for k in range(1, K)))
        print(f"[{tag}] new engine vs certified cache: worst rel {mp.nstr(worst, 3)} "
              f"({'PASS' if worst < mp.mpf(10) ** (-500) else 'FAIL - HALT'})")
        results[tag] = (al, beta)
        os.remove(ck)
    # precision-split validation: low-dps spectral read reproduces the D-osc triple
    alZ, beZ = results["zeta"]; alC2, beC2 = results["ctrl"]
    gamZ = load_atoms(os.path.join(T, "shape_zeros.txt"))
    gamC = load_atoms(os.path.join(T, "shape_smooth.txt"))
    bZ = [1 / (2 * g) ** 2 for g in gamZ]; bC = [1 / (2 * g) ** 2 for g in gamC]
    mp.mp.dps = 60
    alZ = [mp.mpf(x) for x in alZ]; beZ = [mp.mpf(x) for x in beZ]
    alC2 = [mp.mpf(x) for x in alC2]; beC2 = [mp.mpf(x) for x in beC2]
    bZ = [mp.mpf(x) for x in bZ]; bC = [mp.mpf(x) for x in bC]
    certified = {16: mp.mpf("5.0374"), 32: mp.mpf("25.3793"), 64: mp.mpf("87.012")}
    def nodes(al, beta, k):
        J = mp.matrix(k, k)
        for i in range(k): J[i, i] = al[i]
        for i in range(k - 1):
            off = mp.sqrt(beta[i + 1]); J[i, i + 1] = off; J[i + 1, i] = off
        E = mp.eigsy(J, eigvals_only=True)
        return sorted([mp.mpf(E[i]) for i in range(k)], reverse=True)
    ok_all = True
    for k in (16, 32, 64):
        lamZ = nodes(alZ, beZ, k); lamC = nodes(alC2, beC2, k)
        def res(lam, atoms):
            r = 0
            for j in range(k):
                if abs(lam[j] - atoms[j]) / atoms[j] < mp.mpf("0.01"): r = j + 1
                else: break
            return r
        Rr = min(res(lamZ, bZ), res(lamC, bC))
        def osc(lam):
            v = mp.mpf(0)
            for i in range(2, Rr):
                for j in range(i + 1, Rr):
                    v += 2 * mp.log(abs(lam[i] - lam[j]))
            return v
        d = osc(lamZ) - osc(lamC)
        rel = abs(d - certified[k]) / certified[k]
        ok = rel < mp.mpf("1e-4")
        ok_all = ok_all and ok
        print(f"[split k={k}] D-osc(low-dps read) = {mp.nstr(d, 6)} vs certified "
              f"{certified[k]} | rel {mp.nstr(rel, 3)} ({'PASS' if ok else 'FAIL - HALT'})")
    print(f"\nSTAGE B GATE: {'PASS - the engine earns production use' if ok_all else 'FAIL'}")

if __name__ == "__main__":
    main()
