# THE ONE BUILD, Stage C3 — the read + Stage D's adjudication.
# Nesting check (the K=128 Jacobi's top block vs the certified K=64 cache, within the
# certified floor); low-dps spectral read (the precision-split, validated at Stage B);
# the boundary-separated relative pair-energy at K=128; the four-point harmonic-form
# adjudication per the pre-registered criterion (deceleration <= 0.75; geometric limit
# in [0.85, 1.05]).
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")
K = 128

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

def main():
    # nesting check at dps 700-level
    alZ128, beZ128 = load_jacobi(os.path.join(T, "build_jacobi_zeta.txt"), 700)
    alZ64, beZ64 = load_jacobi(os.path.join(T, "shape_jacobi_zeta.txt"), 700)
    worst = max(max(abs(alZ128[k] - alZ64[k]) / abs(alZ64[k]) for k in range(64)),
                max(abs(beZ128[k] - beZ64[k]) / abs(beZ64[k]) for k in range(1, 64)))
    print(f"nesting check (K=128 top block vs certified K=64): worst rel {mp.nstr(worst, 3)} "
          f"({'PASS' if worst < mp.mpf(10) ** (-140) else 'FAIL - HALT'})")
    # low-dps read
    mp.mp.dps = 60
    out = {}
    for tag, jpath, apath in (("zeta", "build_jacobi_zeta.txt", "build_zeros_1300.txt"),
                              ("ctrl", "build_jacobi_ctrl.txt", "build_smooth_1300.txt")):
        al, beta = load_jacobi(os.path.join(T, jpath), 60)
        gam = load_atoms(os.path.join(T, apath), 600, 60)
        atoms = [1 / (2 * g) ** 2 for g in gam]
        J = mp.matrix(K, K)
        for i in range(K): J[i, i] = al[i]
        for i in range(K - 1):
            off = mp.sqrt(beta[i + 1]); J[i, i + 1] = off; J[i + 1, i] = off
        E = mp.eigsy(J, eigvals_only=True)
        lam = sorted([mp.mpf(E[i]) for i in range(K)], reverse=True)
        r = 0
        for j in range(K):
            if abs(lam[j] - atoms[j]) / atoms[j] < mp.mpf("0.01"): r = j + 1
            else: break
        out[tag] = (lam, r)
        print(f"[{tag}] resolved: {r}")
    lamZ, rZ = out["zeta"]; lamC, rC = out["ctrl"]
    R = min(rZ, rC)
    def bands(lam):
        bnd = mp.mpf(0); osc = mp.mpf(0)
        for i in range(R):
            for j in range(i + 1, R):
                t = 2 * mp.log(abs(lam[i] - lam[j]))
                if i < 2: bnd += t
                else: osc += t
        return bnd, osc
    bZ = bands(lamZ); bC = bands(lamC)
    d_osc = bZ[1] - bC[1]
    harm = sum(mp.mpf(1) / (j - i) for i in range(2, R) for j in range(i + 1, R))
    c5 = d_osc / harm
    print(f"\nK=128: R = {R} | D-osc = {mp.nstr(d_osc, 6)} | D-bnd = {mp.nstr(bZ[0]-bC[0], 6)}")
    print(f"harmonic constant c(128) = {mp.nstr(c5, 6)}")
    c3, c4 = mp.mpf("0.72985"), mp.mpf("0.82072")
    dec = (c5 - c4) / (c4 - c3)
    print(f"deceleration ratio (c5-c4)/(c4-c3) = {mp.nstr(dec, 4)}  (criterion: <= 0.75)")
    if dec < 1:
        cinf = c5 + (c5 - c4) * dec / (1 - dec)
        print(f"geometric extrapolated limit c_inf = {mp.nstr(cinf, 5)}  (band: [0.85, 1.05])")
        verdict = "CERTIFIES-at-four-points" if (dec <= mp.mpf("0.75")
                  and mp.mpf("0.85") <= cinf <= mp.mpf("1.05")) else "RETIRES"
    else:
        print("no convergent extrapolation (ratio >= 1)")
        verdict = "RETIRES"
    print(f"\nSTAGE D VERDICT: the harmonic pair-weight {verdict}")

if __name__ == "__main__":
    main()
