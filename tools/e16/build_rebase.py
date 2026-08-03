# THE ONE BUILD — halt-and-diagnose: the nesting check compared DIFFERENT objects
# (J=300 vs J=600 truncations) — invalid as specified.  The repair: (a) the corrected
# cross-check (low-k coefficients agree across J where both truncations resolve the same
# physics); (b) ALL FOUR points rebased on the uniform J=600 object (nested blocks of the
# banked K=128 Jacobi); (c) the Stage-D adjudication re-run on the uniform sequence.
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")

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
    # (a) corrected cross-check: low-k agreement across J
    al128, be128 = load_jacobi(os.path.join(T, "build_jacobi_zeta.txt"), 200)
    al64, be64 = load_jacobi(os.path.join(T, "shape_jacobi_zeta.txt"), 200)
    for kmax, label in ((20, "k<=20"), (40, "k<=40"), (64, "k<=64")):
        w = max(max(abs(al128[k] - al64[k]) / abs(al64[k]) for k in range(kmax)),
                max(abs(be128[k] - be64[k]) / abs(be64[k]) for k in range(1, kmax)))
        print(f"cross-J agreement {label}: worst rel {mp.nstr(w, 3)}")
    print("(the divergence at deep k = the 300-vs-600 tail difference, structural not error)")
    # (b)+(c): the uniform J=600 sequence
    mp.mp.dps = 60
    alZ, beZ = load_jacobi(os.path.join(T, "build_jacobi_zeta.txt"), 60)
    alC, beC = load_jacobi(os.path.join(T, "build_jacobi_ctrl.txt"), 60)
    gamZ = load_atoms(os.path.join(T, "build_zeros_1300.txt"), 600, 60)
    gamC = load_atoms(os.path.join(T, "build_smooth_1300.txt"), 600, 60)
    aZ = [1 / (2 * g) ** 2 for g in gamZ]
    aC = [1 / (2 * g) ** 2 for g in gamC]
    def nodes(al, beta, k):
        J = mp.matrix(k, k)
        for i in range(k): J[i, i] = al[i]
        for i in range(k - 1):
            off = mp.sqrt(beta[i + 1]); J[i, i + 1] = off; J[i + 1, i] = off
        E = mp.eigsy(J, eigvals_only=True)
        return sorted([mp.mpf(E[i]) for i in range(k)], reverse=True)
    seq = []
    for k in (16, 32, 64, 128):
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
        seq.append((k, R, d, c))
        print(f"K={k}: R={R} | D-osc={mp.nstr(d, 6)} | c={mp.nstr(c, 6)}")
    cs = [x[3] for x in seq]
    print(f"\nuniform-object c-sequence: {[mp.nstr(c, 5) for c in cs]}")
    d1 = cs[1] - cs[0]; d2 = cs[2] - cs[1]; d3 = cs[3] - cs[2]
    r12 = d2 / d1; r23 = d3 / d2
    print(f"increments: {mp.nstr(d1,4)}, {mp.nstr(d2,4)}, {mp.nstr(d3,4)} | "
          f"ratios: {mp.nstr(r12,4)}, {mp.nstr(r23,4)}")
    if r23 < 1:
        cinf = cs[3] + d3 * r23 / (1 - r23)
        print(f"geometric limit (last ratio): c_inf = {mp.nstr(cinf, 5)}")
        verdict = ("CERTIFIES-at-four-points" if (r23 <= mp.mpf("0.75")
                   and mp.mpf("0.85") <= cinf <= mp.mpf("1.05")) else "RETIRES")
    else:
        verdict = "RETIRES (no convergence)"
    print(f"\nSTAGE D VERDICT (uniform object, pre-registered criteria): "
          f"the harmonic pair-weight {verdict}")

if __name__ == "__main__":
    main()
