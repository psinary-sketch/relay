# E-3 sitting 1, pencil sweep — n=24 Gleason pencil W_c = W8^3 + c*g24, c in [-42, 0].
# c=-42 = Golay (extremal, d=8); c=0 = e8+e8+e8 (d=4, RH-violating witness).
# Exact RH certificate per c; bisection to a width-<=1/64 rational bracket on each flip.
# Also: m=3 witness root moduli (numeric quote) and the k=1 Gegenbauer non-match check.

from fractions import Fraction as Fr
import importlib.util, sys, pathlib
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "dl", str(pathlib.Path(__file__).with_name("duursma_ladder.py")))
dl = importlib.util.module_from_spec(spec)
sys.modules["dl"] = dl
spec.loader.exec_module(dl)

W8, G24 = dl.W8, dl.G24
W83 = dl.poly_mul(dl.poly_mul(W8, W8), W8)

def pencil(c):
    return [W83[i] + Fr(c) * G24[i] for i in range(25)]

def rh_at(c):
    W = pencil(c)
    d = 8 if W[4] == 0 else 4
    r = dl.analyze(f"pencil c={c}", W, 24, d, False)
    assert r["P1"] == 1 and r["FE"]
    return r["RH_exact"], r

def main():
    print("=== n=24 pencil sweep (coarse) ===")
    coarse = {}
    for c in [Fr(x) for x in range(-42, 1, 3)]:
        ok, _ = rh_at(c)
        coarse[c] = ok
        print(f"c={str(c):>6} d={'8' if c == -42 else '4'} RH_exact={ok}")
    # locate flips and bisect
    cs = sorted(coarse)
    print("\n=== flip bisection (width <= 1/64) ===")
    for i in range(len(cs) - 1):
        a, b = cs[i], cs[i + 1]
        if coarse[a] != coarse[b]:
            fa = coarse[a]
            while b - a > Fr(1, 64):
                mid = (a + b) / 2
                ok, _ = rh_at(mid)
                if ok == fa:
                    a = mid
                else:
                    b = mid
            print(f"flip bracket: RH={coarse[cs[i]]} at {a}  <->  RH={coarse[cs[i+1]]} at {b}"
                  f"   (width {b - a})")
    print("\n=== W8^3 witness roots (numeric quote; certificate is the exact Sturm) ===")
    _, r3 = rh_at(0)
    mp.mp.dps = 40
    norm = r3["norm"]
    roots = mp.polyroots([mp.mpf(v.numerator) / mp.mpf(v.denominator) for v in reversed(norm)],
                         maxsteps=400, extraprec=200)
    tgt = 1 / mp.sqrt(2)
    off = sorted([abs(rr) for rr in roots], key=lambda z: abs(z - tgt), reverse=True)[:4]
    print("worst |T| values vs 1/sqrt2 =", mp.nstr(tgt, 12), ":", [mp.nstr(v, 12) for v in off])

    print("\n=== Gegenbauer non-match check at the extremal k=1 rung (g=5) ===")
    W24, d24 = dl.extremal_type2_enumerator(24)
    rG = dl.analyze("golay", W24, 24, d24, False)
    p = rG["p"]
    g = rG["g"]
    def ptilde(i):
        base = Fr(p[i], 2 ** (i // 2))
        return dl.F2(base, 0) if i % 2 == 0 else dl.F2(0, base / 2)
    v_prev = [dl.F2(2)]; v_curr = [dl.F2(0), dl.F2(1)]
    h = [ptilde(g)]
    def padd(a, b):
        m = max(len(a), len(b))
        z = dl.F2(0)
        return [(a[i] if i < len(a) else z) + (b[i] if i < len(b) else z) for i in range(m)]
    for j in range(1, g + 1):
        if j == 1:
            vj = v_curr
        else:
            vj = padd([dl.F2(0)] + v_curr, [x * dl.F2(-1) for x in v_prev])
            v_prev, v_curr = v_curr, vj
        h = padd(h, [x * ptilde(g + j) for x in vj])
    h = dl.f2p_trim(h)
    print("h(s) coefficients (a + b*sqrt2), ascending:")
    for i, cf in enumerate(h):
        print(f"  s^{i}: {cf.a} + {cf.b}*sqrt2")
    # Gegenbauer C_5^lam(x) on x = s/2: proportional match requires
    # h ~ K * C_5^lam(s/2) for some lam, K. C_5^lam odd polynomial (only odd powers)
    # -> h must have zero even-degree coefficients to match; report the comparison.
    evens_zero = all(h[i].is_zero() for i in range(0, len(h), 2))
    print("h has only odd powers (necessary for any ultraspherical C_5 match):", evens_zero)

if __name__ == "__main__":
    main()
