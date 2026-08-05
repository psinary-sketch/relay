# W-CONTROL-AUDIT item 1 — re-derive the three EXPOSED rows against the position-matched
# (offset-corrected) control, through the identical pipeline, from banked caches.
#   (a) the two-sides attribution: Delta-coeff = Delta-entropy + Delta-repulsion, and the
#       repulsion share (the original 97% at K=16, J=300/600 objects; re-derived here at
#       the same depths on the J=1200 object, old control vs corrected control)
#   (b) the sum-rule separation Z_K, Q_K (original Z_9 = 1.62, Q_9 = 0.78)
#   (c) the c-sequence at the ladder (original 0.578/0.730/0.826/0.882/0.930/0.950)
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")

def load_j(p, dps):
    mp.mp.dps = dps
    al, be, mode = [], [], "AL"
    with open(p) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            if line == "BETA": mode = "BETA"; continue
            (al if mode == "AL" else be).append(mp.mpf(line))
    return al, be

def load_a(p, n, dps):
    mp.mp.dps = dps
    with open(p) as f:
        return [mp.mpf(l.strip()) for l in f if l.strip()][:n]

def nodes_weights(al, be, k):
    J = mp.matrix(k, k)
    for i in range(k): J[i, i] = al[i]
    for i in range(k - 1):
        off = mp.sqrt(be[i + 1]); J[i, i + 1] = off; J[i + 1, i] = off
    E, V = mp.eigsy(J)
    lam = [E[i] for i in range(k)]
    mu = [be[0] * V[0, i] ** 2 for i in range(k)]
    o = sorted(range(k), key=lambda i: -lam[i])
    return [lam[i] for i in o], [mu[i] for i in o]

mp.mp.dps = 60
alZ, beZ = load_j(os.path.join(T, "k256_jacobi_zeta.txt"), 60)
alO, beO = load_j(os.path.join(T, "k256_jacobi_ctrl.txt"), 60)     # old (density-matched)
alC, beC = load_j(os.path.join(T, "corr_jacobi.txt"), 60)          # corrected (position-matched)
aZ = [1/(2*g)**2 for g in load_a(os.path.join(T, "k256_zeros.txt"), 1200, 60)]
aO = [1/(2*g)**2 for g in load_a(os.path.join(T, "k256_smooth.txt"), 1200, 60)]
aC = [1/(2*g)**2 for g in load_a(os.path.join(T, "corr_atoms.txt"), 1200, 60)]

print("=== (a) THE TWO-SIDES ATTRIBUTION, re-derived ===")
print(f"{'K':>4} {'control':>10} {'D-coeff':>12} {'D-entropy':>12} {'D-repulsion':>13} {'rep share':>10}")
for K in (12, 16):
    for tag, al, be in (("old", alO, beO), ("corrected", alC, beC)):
        cZ = sum((K - j) * mp.log(beZ[j]) for j in range(K))
        cX = sum((K - j) * mp.log(be[j]) for j in range(K))
        lamZ, muZ = nodes_weights(alZ, beZ, K)
        lamX, muX = nodes_weights(al, be, K)
        entZ = sum(mp.log(m) for m in muZ); entX = sum(mp.log(m) for m in muX)
        repZ = 2*sum(mp.log(abs(lamZ[i]-lamZ[j])) for i in range(K) for j in range(i+1,K))
        repX = 2*sum(mp.log(abs(lamX[i]-lamX[j])) for i in range(K) for j in range(i+1,K))
        dc, de, dr = cZ-cX, entZ-entX, repZ-repX
        print(f"{K:>4} {tag:>10} {mp.nstr(dc,7):>12} {mp.nstr(de,6):>12} {mp.nstr(dr,7):>13} "
              f"{mp.nstr(100*dr/dc,4):>9}%")

print("\n=== (b) THE SUM-RULE SEPARATION, re-derived ===")
for tag, al, be in (("old", alO, beO), ("corrected", alC, beC)):
    Z = mp.mpf(0); Q = mp.mpf(0)
    for k in range(1, 10):
        Z += mp.log(mp.sqrt(beZ[k]) / mp.sqrt(be[k]))
        Q += ((alZ[k]-al[k])**2 + (mp.sqrt(beZ[k])-mp.sqrt(be[k]))**2) / aZ[k]**2
    print(f"  {tag:>10}: Z_9 = {mp.nstr(Z,6):>10} | Q_9 = {mp.nstr(Q,6):>10}")

print("\n=== (c) THE c-SEQUENCE, re-derived ===")
print(f"{'K':>5} {'R':>5} {'c (old ctrl)':>14} {'c (corrected)':>15} {'shift':>10}")
for K in (16, 32, 64, 128, 200, 256):
    out = {}
    for tag, al, be, at in (("old", alO, beO, aO), ("corrected", alC, beC, aC)):
        lamZ, _ = nodes_weights(alZ, beZ, K)
        lamX, _ = nodes_weights(al, be, K)
        def res(lam, atoms):
            r = 0
            for j in range(K):
                if abs(lam[j]-atoms[j])/atoms[j] < mp.mpf("0.01"): r = j+1
                else: break
            return r
        R = min(res(lamZ, aZ), res(lamX, at))
        def osc(lam):
            v = mp.mpf(0)
            for i in range(2, R):
                for j in range(i+1, R):
                    v += 2*mp.log(abs(lam[i]-lam[j]))
            return v
        harm = sum(mp.mpf(1)/(j-i) for i in range(2,R) for j in range(i+1,R))
        out[tag] = ((osc(lamZ)-osc(lamX))/harm, R)
    co, Ro = out["old"]; cc, Rc = out["corrected"]
    print(f"{K:>5} {Ro:>5} {mp.nstr(co,6):>14} {mp.nstr(cc,6):>15} {mp.nstr(cc-co,4):>10}")
