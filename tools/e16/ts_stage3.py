# W-TWOSIDES stage 3: the identity assembled from cached moments (fast).
# Coefficient side vs spectral side, zeta and control, depths 12 and 16; balance;
# relative decomposition; attribution bands; shape first look.
import os
import mpmath as mp

def load(path, dps):
    mp.mp.dps = dps
    with open(path) as f:
        vals = [mp.mpf(line.strip()) for line in f if line.strip()]
    return [None] + vals

def jacobi_full(s, depth):
    G = mp.matrix(depth + 1, depth + 1)
    for i in range(depth + 1):
        for j in range(depth + 1):
            G[i, j] = s[i + j + 1]
    R = mp.cholesky(G).T
    al, beta = [], [s[1]]
    for k in range(depth):
        t1 = R[k, k + 1] / R[k, k]
        t0 = R[k - 1, k] / R[k - 1, k - 1] if k >= 1 else mp.mpf(0)
        al.append(t1 - t0)
        if k >= 1:
            beta.append((R[k, k] / R[k - 1, k - 1]) ** 2)
    return al, beta

def sides(al, beta, K):
    coeff = sum((K - j) * mp.log(beta[j]) for j in range(K))
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
    mp.mp.dps = 400
    T = os.environ.get("TEMP", ".")
    sZ = load(os.path.join(T, "ts_zeta_moments.txt"), 400)
    sC = load(os.path.join(T, "ts_ctrl_moments.txt"), 400)
    alZ, betaZ = jacobi_full(sZ, 16)
    alC, betaC = jacobi_full(sC, 16)
    results = {}
    for K in (12, 16):
        for name, al, be in (("zeta", alZ, betaZ), ("ctrl", alC, betaC)):
            c, sspec, lam, mu, ent, rep = sides(al, be, K)
            results[(name, K)] = (c, sspec, lam, mu, ent, rep)
            print(f"[{name} K={K}] coeff = {mp.nstr(c, 12)} | spec = {mp.nstr(sspec, 12)} "
                  f"| BALANCE = {mp.nstr(c - sspec, 4)} | ent {mp.nstr(ent, 8)} rep {mp.nstr(rep, 8)}")
    print("\n=== RELATIVE (zeta - ctrl) ===")
    for K in (12, 16):
        cZ, _, lamZ, muZ, entZ, repZ = results[("zeta", K)]
        cC, _, lamC, muC, entC, repC = results[("ctrl", K)]
        print(f"K={K}: D-coeff = {mp.nstr(cZ - cC, 8)} | D-entropy = {mp.nstr(entZ - entC, 8)} "
              f"| D-repulsion = {mp.nstr(repZ - repC, 8)}")
        def rep_bands(lam, nres):
            b = [mp.mpf(0)] * 3
            n = len(lam)
            for i in range(n):
                for j in range(i + 1, n):
                    t = 2 * mp.log(abs(lam[i] - lam[j]))
                    if i < 2 and j < nres: b[0] += t
                    elif i < nres and j < nres: b[1] += t
                    else: b[2] += t
            return b
        nres = 6 if K == 12 else 8
        bZ = rep_bands(lamZ, nres); bC = rep_bands(lamC, nres)
        print(f"   D-rep bands: boundary = {mp.nstr(bZ[0] - bC[0], 6)} | "
              f"oscillation = {mp.nstr(bZ[1] - bC[1], 6)} | residual = {mp.nstr(bZ[2] - bC[2], 6)}")
        def ent_bands(mu, nres):
            return (sum(mp.log(m) for m in mu[:2]),
                    sum(mp.log(m) for m in mu[2:nres]),
                    sum(mp.log(m) for m in mu[nres:]))
        eZ = ent_bands(muZ, nres); eC = ent_bands(muC, nres)
        print(f"   D-ent bands: boundary = {mp.nstr(eZ[0] - eC[0], 6)} | "
              f"oscillation = {mp.nstr(eZ[1] - eC[1], 6)} | residual = {mp.nstr(eZ[2] - eC[2], 6)}")
    print("\n=== shape first look (K=16 adjacent log-gaps, zeta - ctrl) ===")
    _, _, lamZ, _, _, _ = results[("zeta", 16)]
    _, _, lamC, _, _, _ = results[("ctrl", 16)]
    for i in range(7):
        d = mp.log(lamZ[i] - lamZ[i + 1]) - mp.log(lamC[i] - lamC[i + 1])
        print(f"  pair ({i+1},{i+2}): delta log-gap = {mp.nstr(d, 5)}")

if __name__ == "__main__":
    main()
