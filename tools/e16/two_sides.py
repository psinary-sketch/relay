# W-TWOSIDES instrument: the finite relative identity, both halves, zeta-string and
# smooth-density control, depths 12 and 16.
#   COEFFICIENT side: log D_K = sum_{j=0}^{K-1} (K-j) log beta_j   (beta_0 = m_0 = s_1)
#   SPECTRAL side:    log D_K = sum_i log mu_i + 2 sum_{i<j} log|lambda_i - lambda_j|
# Balance = the double-source (Cholesky route vs eigen route).  Attribution: boundary
# (nodes 1-2) / oscillation (resolved 3..8) / residual (tail clusters), on the relative
# log-repulsion and log-weight terms.  Precision law: dps 450 arithmetic; control zeros
# at dps 250.

import importlib.util, sys, pathlib
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "hb", str(pathlib.Path(__file__).with_name("hankel_bridge.py")))
hb = importlib.util.module_from_spec(spec); sys.modules["hb"] = hb; spec.loader.exec_module(hb)
spec3 = importlib.util.spec_from_file_location(
    "cc", str(pathlib.Path(__file__).with_name("constant_control.py")))
cc = importlib.util.module_from_spec(spec3); sys.modules["cc"] = cc; spec3.loader.exec_module(cc)

def jacobi_full(s, depth):
    G = mp.matrix(depth + 1, depth + 1)
    for i in range(depth + 1):
        for j in range(depth + 1):
            G[i, j] = s[i + j + 1]
    R = mp.cholesky(G).T
    al, beta = [], [s[1]]          # beta_0 = m_0 = s_1
    for k in range(depth):
        t1 = R[k, k + 1] / R[k, k]
        t0 = R[k - 1, k] / R[k - 1, k - 1] if k >= 1 else mp.mpf(0)
        al.append(t1 - t0)
        if k >= 1:
            beta.append((R[k, k] / R[k - 1, k - 1]) ** 2)
    return al, beta

def sides(al, beta, K):
    # coefficient side
    coeff = sum((K - j) * mp.log(beta[j]) for j in range(K))
    # spectral side via eigen decomposition of the K x K Jacobi matrix
    J = mp.matrix(K, K)
    for i in range(K):
        J[i, i] = al[i]
    for i in range(K - 1):
        off = mp.sqrt(beta[i + 1])
        J[i, i + 1] = off; J[i + 1, i] = off
    E, V = mp.eigsy(J)
    lam = [E[i] for i in range(K)]
    mu = [beta[0] * V[0, i] ** 2 for i in range(K)]
    order = sorted(range(K), key=lambda i: -lam[i])
    lam = [lam[i] for i in order]; mu = [mu[i] for i in order]
    ent = sum(mp.log(m) for m in mu)
    rep = 2 * sum(mp.log(abs(lam[i] - lam[j])) for i in range(K) for j in range(i + 1, K))
    return coeff, ent + rep, lam, mu, ent, rep

def main():
    depths = (12, 16)
    mp.mp.dps = 450
    sZ = hb.power_sums(mp.mpf(0), 2 * max(depths) + 1)
    mp.mp.dps = 250
    J = 3000
    gam = [cc.smooth_zero(j) for j in range(1, J + 1)]
    betas_c = [1 / (2 * g) ** 2 for g in gam]
    gJ = gam[-1]
    sC = [None] * (2 * max(depths) + 2)
    for k in range(1, 2 * max(depths) + 2):
        base = sum(b ** k for b in betas_c)
        tail = mp.quad(lambda g: mp.log(g / (2 * mp.pi)) / (2 * mp.pi) * (2 * g) ** (-2 * k),
                       [gJ, 10 * gJ, mp.inf])
        sC[k] = base + tail
    mp.mp.dps = 450
    sC = [None] + [mp.mpf(x) for x in sC[1:]]
    alZ, betaZ = jacobi_full(sZ, max(depths))
    alC, betaC = jacobi_full(sC, max(depths))
    results = {}
    for K in depths:
        for name, al, be in (("zeta", alZ, betaZ), ("ctrl", alC, betaC)):
            c, sspec, lam, mu, ent, rep = sides(al, be, K)
            results[(name, K)] = (c, sspec, lam, mu, ent, rep)
            bal = c - sspec
            print(f"[{name} K={K}] coeff side = {mp.nstr(c, 12)}")
            print(f"{'':12} spec side  = {mp.nstr(sspec, 12)}  (entropy {mp.nstr(ent, 8)}, "
                  f"repulsion {mp.nstr(rep, 8)})")
            print(f"{'':12} BALANCE (coeff - spec) = {mp.nstr(bal, 4)}")
    print("\n=== THE RELATIVE DECOMPOSITION (zeta - control), per depth ===")
    mp.mp.dps = 40
    zs = [mp.zetazero(j).imag for j in range(1, 20)]
    for K in depths:
        cZ, sZs, lamZ, muZ, entZ, repZ = results[("zeta", K)]
        cC, sCs, lamC, muC, entC, repC = results[("ctrl", K)]
        print(f"\nK = {K}: Delta coeff = {mp.nstr(cZ - cC, 8)} | Delta entropy = "
              f"{mp.nstr(entZ - entC, 8)} | Delta repulsion = {mp.nstr(repZ - repC, 8)}")
        # attribution on the repulsion term: pair contributions by band
        def rep_bands(lam, nres):
            b_bnd = mp.mpf(0); b_osc = mp.mpf(0); b_res = mp.mpf(0)
            K = len(lam)
            for i in range(K):
                for j in range(i + 1, K):
                    t = 2 * mp.log(abs(lam[i] - lam[j]))
                    if i < 2 and j < nres:
                        b_bnd += t
                    elif i < nres and j < nres:
                        b_osc += t
                    else:
                        b_res += t
            return b_bnd, b_osc, b_res
        nres = 6 if K == 12 else 8
        bZ = rep_bands(lamZ, nres); bC = rep_bands(lamC, nres)
        print(f"  Delta repulsion by band: boundary(1-2 x resolved) = {mp.nstr(bZ[0]-bC[0], 6)}"
              f" | oscillation(3..{nres} pairs) = {mp.nstr(bZ[1]-bC[1], 6)}"
              f" | residual(tail) = {mp.nstr(bZ[2]-bC[2], 6)}")
    # shape first look: per-adjacent-pair log-gap deviation in the resolved band, K=16
    print("\n=== shape first look (K=16, resolved band adjacent log-gaps, zeta - ctrl) ===")
    cZ, sZs, lamZ, muZ, entZ, repZ = results[("zeta", 16)]
    cC, sCs, lamC, muC, entC, repC = results[("ctrl", 16)]
    for i in range(7):
        dz = mp.log(lamZ[i] - lamZ[i + 1])
        dc = mp.log(lamC[i] - lamC[i + 1])
        print(f"  pair ({i+1},{i+2}): delta log-gap = {mp.nstr(dz - dc, 5)}")

if __name__ == "__main__":
    main()
