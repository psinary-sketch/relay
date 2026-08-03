# W-LEHMER-TIE part A/B/C: scan low zeros for close pairs; table two-body collision times;
# quantify the depth-12 meter's spectral reach; run the targeted-enrichment MODEL at t=-0.1.
# MODEL GRADE throughout part C: the t<0 zero set is modeled by the two-body collision
# estimate (pair with x-gap r0 collides at t_c = -r0^2/8; past collision the pair is
# gamma_mid +/- i*delta with (2*delta)^2 = 8(|t|-|t_c|)); doubly-sourced by two windows.

import mpmath as mp

def main():
    mp.mp.dps = 25
    J = 1500
    zs = []
    for n in range(1, J + 1):
        zs.append(mp.zetazero(n).imag)
    print(f"scanned first {J} zeros; gamma_J = {mp.nstr(zs[-1], 10)}")
    # close pairs: gap thresholds
    pairs = []
    for i in range(J - 1):
        gap = zs[i + 1] - zs[i]
        tc = -(gap * gap) / 2  # x = 2*gamma: r0 = 2*gap, t_c = -r0^2/8 = -gap^2/2
        pairs.append((gap, i + 1, zs[i], zs[i + 1], tc))
    pairs.sort()
    print("\nten closest pairs in the first", J, "zeros (gap | index | heights | model t_c):")
    for gap, idx, a, b, tc in pairs[:10]:
        print(f"  gap {mp.nstr(gap, 6)} | n={idx} | {mp.nstr(a, 10)} .. {mp.nstr(b, 10)} "
              f"| t_c = {mp.nstr(tc, 4)}")
    collided_01 = [p for p in pairs if p[4] > -0.1]
    print(f"\npairs collided by t = -0.1 (model, |t_c| < 0.1): {len(collided_01)}")
    if collided_01:
        gap, idx, a, b, tc = min(collided_01, key=lambda p: p[2])
        print(f"  LOWEST collided pair: n={idx}, heights {mp.nstr(a, 10)} .. {mp.nstr(b, 10)}, "
              f"gap {mp.nstr(gap, 6)}, t_c = {mp.nstr(tc, 4)}")
        first_pair = (idx, a, b, gap, tc)
    else:
        # fall back to the classical Lehmer pair
        print("  none within first", J, "zeros; the classical Lehmer pair (n~6709, gamma~7005.06)")
        first_pair = None
    # meter reach: depth-12 window ~ the 12 largest beta = zeros gamma_1..gamma_12
    print(f"\nmeter reach: depth-12 band = gamma_1..gamma_12 = "
          f"[{mp.nstr(zs[0], 8)}, {mp.nstr(zs[11], 8)}]")
    if first_pair:
        idx, a, b, gap, tc = first_pair
        ratio = (a / zs[11]) ** 2
        print(f"first collided pair height / reach edge: gamma = {mp.nstr(a, 8)} vs "
              f"gamma_12 = {mp.nstr(zs[11], 8)} | beta-ratio (reach shortfall) = "
              f"{mp.nstr(ratio, 4)}x in beta^1; zeros above it in beta-order: {idx - 1}")
    # ---- PART C: the enrichment model at t = -0.1 ----
    if first_pair:
        mp.mp.dps = 40
        idx, a, b, gap, tc = first_pair
        gm = (a + b) / 2
        # model imaginary part: (2 delta)^2 = 8(|t| - |t_c|), t = -0.1
        delta = mp.sqrt(8 * (mp.mpf("0.1") - abs(tc))) / 2
        print(f"\nENRICHMENT MODEL at t = -0.1: pair -> {mp.nstr(gm, 10)} +/- "
              f"{mp.nstr(delta, 6)} i (model)")
        model = [mp.mpc(z, 0) for k, z in enumerate(zs) if k + 1 not in (idx, idx + 1)]
        model += [mp.mpc(gm, delta), mp.mpc(gm, -delta)]
        for name, sigma, wf in (("gauss sigma=3", 3, lambda l: mp.e ** (-l * l)),
                                ("gauss sigma=6", 6, lambda l: mp.e ** (-l * l)),
                                ("lorentz sigma=3", 3, lambda l: 1 / (1 + l * l) ** 3)):
            s = sigma
            def moments(zset):
                lam = [(z - gm) / s for z in zset]
                return [sum(wf(l) * l ** k for l in lam) for k in range(13)]
            mmod = moments(model)
            mreal = moments([mp.mpc(z, 0) for z in zs])  # t=0 control, same window
            def first_flip(m):
                for d in range(1, 7):
                    A = mp.matrix(d, d)
                    for i in range(d):
                        for j in range(d):
                            A[i, j] = m[i + j]
                    det = mp.det(A)
                    if mp.re(det) < 0:
                        return d
                return None
            fm, fr = first_flip(mmod), first_flip(mreal)
            print(f"  window {name}: model-pair flip at d = {fm} | t=0 control flip: "
                  f"{fr if fr else 'none (PSD, as it must be)'}")

if __name__ == "__main__":
    main()
