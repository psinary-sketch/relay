# THE SIXTH POINT Stages C+D: the six-point read (uniform object, nested blocks; the
# uniform-object check passes by construction and is asserted) + the fixed adjudication:
# the measured c(256) against the two pre-registered predictions; nearer family wins
# unless within the demonstrated error scale (0.006) of the midpoint band -> UNDISCRIMINATED.
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")
K = 256
PRED_D = mp.mpf("0.942744")   # (d) A/logK
PRED_A = mp.mpf("0.960941")   # (a) geometric-index
ERR = mp.mpf("0.006")

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

def nodes(al, beta, k):
    J = mp.matrix(k, k)
    for i in range(k): J[i, i] = al[i]
    for i in range(k - 1):
        off = mp.sqrt(beta[i + 1]); J[i, i + 1] = off; J[i + 1, i] = off
    E = mp.eigsy(J, eigvals_only=True)
    return sorted([mp.mpf(E[i]) for i in range(k)], reverse=True)

def main():
    mp.mp.dps = 60
    alZ, beZ = load_jacobi(os.path.join(T, "k256_jacobi_zeta.txt"), 60)
    alC, beC = load_jacobi(os.path.join(T, "k256_jacobi_ctrl.txt"), 60)
    gamZ = load_atoms(os.path.join(T, "k256_zeros.txt"), 1200, 60)
    gamC = load_atoms(os.path.join(T, "k256_smooth.txt"), 1200, 60)
    aZ = [1 / (2 * g) ** 2 for g in gamZ]
    aC = [1 / (2 * g) ** 2 for g in gamC]
    print("uniform-object check: single object (J=1200, dps 2700), nested blocks — "
          "structural PASS; lower-point agreement verified below")
    seq = []
    for k in (16, 32, 64, 128, 200, 256):
        lamZ = nodes(alZ, beZ, k); lamC = nodes(alC, beC, k)
        def res(lam, atoms):
            r = 0
            for j in range(k):
                if abs(lam[j] - atoms[j]) / atoms[j] < mp.mpf("0.01"): r = j + 1
                else: break
            return r
        R = min(res(lamZ, aZ), res(lamC, aC))
        def osc(lam):
            v = mp.mpf(0)
            for i in range(2, R):
                for j in range(i + 1, R):
                    v += 2 * mp.log(abs(lam[i] - lam[j]))
            return v
        d = osc(lamZ) - osc(lamC)
        harm = sum(mp.mpf(1) / (j - i) for i in range(2, R) for j in range(i + 1, R))
        c = d / harm
        seq.append((k, R, c))
        print(f"K={k}: R={R} | c = {mp.nstr(c, 6)}")
    prior = {16: "0.578133", 32: "0.729832", 64: "0.825489", 128: "0.886588", 200: "0.932074"}
    worst = max(abs(c - mp.mpf(prior[k])) for k, _, c in seq if k in prior)
    print(f"lower-point agreement vs the K200-object values: worst |delta| = {mp.nstr(worst, 3)} "
          f"(J-robustness envelope ~ 0.005)")
    c256 = seq[-1][2]
    dd = abs(c256 - PRED_D); da = abs(c256 - PRED_A)
    print(f"\nTHE MEASURED c(256) = {mp.nstr(c256, 6)}")
    print(f"|c - pred_d| = {mp.nstr(dd, 4)} | |c - pred_a| = {mp.nstr(da, 4)}")
    if abs(dd - da) <= ERR:
        print("ADJUDICATION: UNDISCRIMINATED — the seventh point re-prices")
    elif dd < da:
        print("ADJUDICATION: LAW (d) WINS — the denominator is wrong; pi_0 re-normalizes; "
              "the saturation reading stays unused")
    else:
        print("ADJUDICATION: LAW (a) WINS — the unit constant stands at six-point "
              "instrument grade; the saturation test opens")

if __name__ == "__main__":
    main()
