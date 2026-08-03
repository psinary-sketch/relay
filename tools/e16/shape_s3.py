# W-SHAPE stage 3: THE READ at K=64.
# (1) The resolved-pair window measured FIRST (node-vs-atom rel < 1%).
# (2) Unfolded resolved-gap statistics; THE DISCRIMINANT (stated in the report in advance):
#     D = Var(unfolded gaps)/0.180 (GUE nearest-neighbor variance at cite);
#     acceptance band for CONSISTENT at this window's power: D in [0.5, 2];
#     the control's D is the rigid null (~0).  Small-gap fraction as the second lens.
# (3) The E-24 rider: the relative resolved-band log-repulsion at K=64 vs K=16 (the
#     pi_0 limit's first depth datum) -- riding free, not the construct-or-refute.
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")
K = 64

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

def nodes_weights(al, beta, k):
    J = mp.matrix(k, k)
    for i in range(k): J[i, i] = al[i]
    for i in range(k - 1):
        off = mp.sqrt(beta[i + 1]); J[i, i + 1] = off; J[i + 1, i] = off
    E, V = mp.eigsy(J)
    lam = [E[i] for i in range(k)]
    mu = [beta[0] * V[0, i] ** 2 for i in range(k)]
    order = sorted(range(k), key=lambda i: -lam[i])
    return [lam[i] for i in order], [mu[i] for i in order]

def main():
    mp.mp.dps = 700
    out = {}
    for tag, apath, jpath in (("zeta", "shape_zeros.txt", "shape_jacobi_zeta.txt"),
                              ("ctrl", "shape_smooth.txt", "shape_jacobi_ctrl.txt")):
        gam = load_atoms(os.path.join(T, apath))
        betas = [1 / (2 * g) ** 2 for g in gam]
        al, beta = load_jacobi(os.path.join(T, jpath))
        lam, mu = nodes_weights(al, beta, K)
        resolved = 0
        for j in range(K):
            rel = abs(lam[j] - betas[j]) / betas[j]
            if rel < mp.mpf("0.01"):
                resolved = j + 1
            else:
                break
        # unfolded gaps on the resolved band, in gamma-coordinates
        g_nodes = [1 / (2 * mp.sqrt(l)) for l in lam[:resolved]]
        gaps = []
        for j in range(resolved - 1):
            raw = g_nodes[j + 1] - g_nodes[j]
            unf = raw * mp.log(g_nodes[j] / (2 * mp.pi)) / (2 * mp.pi)
            gaps.append(unf)
        n = len(gaps)
        mean = sum(gaps) / n
        var = sum((x / mean - 1) ** 2 for x in gaps) / (n - 1)
        small = sum(1 for x in gaps if x / mean < mp.mpf("0.5")) / mp.mpf(n)
        print(f"[{tag}] resolved pairs: {resolved} nodes -> {n} gaps | "
              f"unfolded mean {mp.nstr(mean, 5)} | Var(s/mean) = {mp.nstr(var, 4)} | "
              f"D = Var/0.180 = {mp.nstr(var / mp.mpf('0.180'), 4)} | "
              f"small-gap frac (<0.5 mean) = {mp.nstr(small, 3)}")
        out[tag] = (lam, mu, resolved)
    # E-24 rider: relative resolved-band log-repulsion, boundary-separated
    lamZ, muZ, resZ = out["zeta"]; lamC, muC, resC = out["ctrl"]
    nres = min(resZ, resC)
    def rep_band(lam, nres):
        b_bnd = mp.mpf(0); b_osc = mp.mpf(0)
        for i in range(nres):
            for j in range(i + 1, nres):
                t = 2 * mp.log(abs(lam[i] - lam[j]))
                if i < 2: b_bnd += t
                else: b_osc += t
        return b_bnd, b_osc
    bZ = rep_band(lamZ, nres); bC = rep_band(lamC, nres)
    print(f"\nE-24 rider (K=64, resolved band {nres}): Delta rep boundary = "
          f"{mp.nstr(bZ[0] - bC[0], 6)} | Delta rep oscillation = {mp.nstr(bZ[1] - bC[1], 6)}")
    print("(K=16 comparators: boundary 11.16, oscillation 5.03 -- the normalized-limit trend datum)")

if __name__ == "__main__":
    main()
