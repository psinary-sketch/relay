# W-LEHMER-TIE part C refinement: window-scale sweep. The model pair at gamma ~ 415.237
# +/- 0.0977 i sits among real zeros with local gap ~ 1.5; the flip needs the form to
# resolve the pair's faintness (delta / local gap ~ 0.065). Sweep sigma and depth to
# locate the visibility threshold. Doubly-sourced: gaussian vs lorentzian windows.

import mpmath as mp

def main():
    mp.mp.dps = 50
    J = 1500
    zs = [mp.zetazero(n).imag for n in range(1, J + 1)]
    idx = 212
    a, b = zs[idx - 1], zs[idx]
    gm = (a + b) / 2
    tc = -((b - a) ** 2) / 2
    delta = mp.sqrt(8 * (mp.mpf("0.1") - abs(tc))) / 2
    print(f"model pair: {mp.nstr(gm, 10)} +/- {mp.nstr(delta, 6)} i  (t = -0.1)")
    model = [mp.mpc(z, 0) for k, z in enumerate(zs) if k + 1 not in (idx, idx + 1)]
    model += [mp.mpc(gm, delta), mp.mpc(gm, -delta)]
    real_set = [mp.mpc(z, 0) for z in zs]
    windows = [("gauss", lambda l: mp.e ** (-l * l)),
               ("lorentz", lambda l: 1 / (1 + l * l) ** 4)]
    print(f"{'sigma':>6} | {'window':>8} | model flip d | t=0 control")
    for sigma in (mp.mpf("0.3"), mp.mpf("0.5"), 1, 2, 3):
        for wname, wf in windows:
            def flip(zset):
                lam = [(z - gm) / sigma for z in zset]
                m = [sum(wf(l) * l ** k for l in lam) for k in range(29)]
                for d in range(1, 15):
                    A = mp.matrix(d, d)
                    for i in range(d):
                        for j in range(d):
                            A[i, j] = m[i + j]
                    if mp.re(mp.det(A)) < 0:
                        return d
                return None
            fm, fr = flip(model), flip(real_set)
            print(f"{mp.nstr(sigma,3):>6} | {wname:>8} | {str(fm):>12} | "
                  f"{str(fr) if fr else 'PSD (must be)'}")

if __name__ == "__main__":
    main()
