# W-SUMRULE — the relative sum-rule deviation functionals of the zeta-string vs the
# smooth-density control (both purely atomic with identical density: the RELATIVE
# functionals isolate the arithmetic as a sum-rule quantity).
#   Z_K = sum_{k<=K} log(a_k^zeta / a_k^ctrl)          (Szego-flavor multiplicative deviation)
#   Q_K = sum_{k<=K} [ (alpha^z-alpha^c)^2 + (a^z-a^c)^2 ] / beta_k^2   (KS/P2-flavor, zero-scale normalized)
# a_k = sqrt(beta-recurrence).  Matched depth 10; zeta doubly-sourced at depth 5 (A vs B
# agreement recorded in E-20 face 1); control at the precision law.

import importlib.util, sys, pathlib
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "hb", str(pathlib.Path(__file__).with_name("hankel_bridge.py")))
hb = importlib.util.module_from_spec(spec); sys.modules["hb"] = hb; spec.loader.exec_module(hb)
spec2 = importlib.util.spec_from_file_location(
    "sc", str(pathlib.Path(__file__).with_name("string_construction.py")))
sc = importlib.util.module_from_spec(spec2); sys.modules["sc"] = sc; spec2.loader.exec_module(sc)
spec3 = importlib.util.spec_from_file_location(
    "cc", str(pathlib.Path(__file__).with_name("constant_control.py")))
cc = importlib.util.module_from_spec(spec3); sys.modules["cc"] = cc; spec3.loader.exec_module(cc)

def jacobi(s, depth):
    G = mp.matrix(depth + 1, depth + 1)
    for i in range(depth + 1):
        for j in range(depth + 1):
            G[i, j] = s[i + j + 1]
    R = mp.cholesky(G).T
    al, be = [], []
    for k in range(depth):
        t1 = R[k, k + 1] / R[k, k]
        t0 = R[k - 1, k] / R[k - 1, k - 1] if k >= 1 else mp.mpf(0)
        al.append(t1 - t0)
        if k >= 1:
            be.append((R[k, k] / R[k - 1, k - 1]) ** 2)
    return al, be

def main():
    depth = 10
    # zeta string (source A, dps 250)
    mp.mp.dps = 250
    sZ = hb.power_sums(mp.mpf(0), 2 * depth + 1)
    alZ, beZ = jacobi(sZ, depth)
    # control (smooth density; zeros dps 150, arithmetic dps 220)
    mp.mp.dps = 150
    J = 3000
    gam = [cc.smooth_zero(j) for j in range(1, J + 1)]
    betas_c = [1 / (2 * g) ** 2 for g in gam]
    gJ = gam[-1]
    sC = [None] * (2 * depth + 2)
    for k in range(1, 2 * depth + 2):
        base = sum(b ** k for b in betas_c)
        tail = mp.quad(lambda g: mp.log(g / (2 * mp.pi)) / (2 * mp.pi) * (2 * g) ** (-2 * k),
                       [gJ, 10 * gJ, mp.inf])
        sC[k] = base + tail
    mp.mp.dps = 220
    sC = [None] + [mp.mpf(x) for x in sC[1:]]
    alC, beC = jacobi(sC, depth)
    # actual zero scales for normalization
    mp.mp.dps = 30
    zs = [mp.zetazero(j).imag for j in range(1, depth + 2)]
    betaZ = [1 / (2 * g) ** 2 for g in zs]
    print("=== the Jacobi data, matched depth 10 (zeta vs control) ===")
    print(f"alpha (zeta): {[mp.nstr(a, 6) for a in alZ]}")
    print(f"alpha (ctrl): {[mp.nstr(a, 6) for a in alC]}")
    print(f"a=sqrt(be-rec) zeta: {[mp.nstr(mp.sqrt(b), 6) for b in beZ]}")
    print(f"a=sqrt(be-rec) ctrl: {[mp.nstr(mp.sqrt(b), 6) for b in beC]}")
    Z = mp.mpf(0); Q = mp.mpf(0)
    print("\n=== the relative sum-rule functionals (partial sums) ===")
    print(f"{'K':>3} {'Z_K (Szego-flavor)':>20} {'Q_K (KS-flavor)':>18}")
    for K in range(len(beZ)):
        Z += mp.log(mp.sqrt(beZ[K]) / mp.sqrt(beC[K]))
        dq = ((alZ[K + 1] - alC[K + 1]) ** 2 + (mp.sqrt(beZ[K]) - mp.sqrt(beC[K])) ** 2) / betaZ[K + 1] ** 2
        Q += dq
        print(f"{K+1:>3} {mp.nstr(Z, 6):>20} {mp.nstr(Q, 6):>18}")
    print(f"\ncontrol-noise scale for Z: ~1e-3 per term (the control's own stability);")
    print(f"|Z_9| and Q_9 vs that scale = the separation verdict.")

if __name__ == "__main__":
    main()
