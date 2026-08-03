# E-21 — THE ADDITIVE HUNT: the constant-term structure across n = 24, 32, 40 (exact).
# For each length: locate the entry minor (the shallowest flipping floor-layer minor near
# the stratum), interpolate N_k(delta) = D_k * L^{k^2} exactly, strip L- and delta-factors,
# and read the reduced constant N~(0).  Compare against lead(H_extremal) = p0(ext)^2:
# r_n = N~(0)/lead(H_ext).  Print exact values + factorizations for the recognition step.

from fractions import Fraction as Fr
import importlib.util, sys, pathlib

spec = importlib.util.spec_from_file_location(
    "dl", str(pathlib.Path(__file__).with_name("duursma_ladder.py")))
dl = importlib.util.module_from_spec(spec); sys.modules["dl"] = dl; spec.loader.exec_module(dl)
spec2 = importlib.util.spec_from_file_location(
    "gs", str(pathlib.Path(__file__).with_name("genus5.py")))
gs = importlib.util.module_from_spec(spec2); sys.modules["gs"] = gs; spec2.loader.exec_module(gs)
spec3 = importlib.util.spec_from_file_location(
    "mech", str(pathlib.Path(__file__).with_name("mechanism.py")))
mech = importlib.util.module_from_spec(spec3); sys.modules["mech"] = mech; spec3.loader.exec_module(mech)

W8 = dl.W8
G24 = dl.G24
PENCILS = {
    24: (dl.poly_mul(dl.poly_mul(W8, W8), W8), G24, 42),
    32: (mech.W84, mech.W8G, 56),
    40: (dl.poly_mul(mech.W84, W8), dl.poly_mul(dl.poly_mul(W8, W8), G24), 70),
}

def pencil_H(n, delta):
    base, second, defect0 = PENCILS[n]
    c = delta - defect0
    W = [base[i] + Fr(c) * second[i] for i in range(n + 1)]
    return mech.H_of(W, n, 4)

def floor_minor(H, k):
    m, L = mech.monic_moments(H, 2 * k + 1)
    D = mech.rdet([[m[i + j + 1] for j in range(k)] for i in range(k)])
    return D, L

def factorize(x):
    x = abs(int(x))
    if x == 0: return "0"
    out = []
    for p in range(2, 1000000):
        while x % p == 0:
            out.append(p); x //= p
        if x == 1: break
        if p * p > x:
            out.append(x); x = 1; break
    from collections import Counter
    cnt = Counter(out)
    return " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(cnt.items()))

def hunt(n, kmax_scan=6, nsamples=52):
    print(f"\n===== n = {n} =====")
    # entry scan at small delta
    Hs = pencil_H(n, Fr(1))
    entry = None
    for k in range(2, kmax_scan + 1):
        D, L = floor_minor(Hs, k)
        s = (D > 0) - (D < 0)
        print(f"  delta=1 floor k={k}: sign {s}")
        if s < 0 and entry is None:
            entry = k
    if entry is None:
        print("  no entry minor found within scan — null branch datum")
        return
    print(f"  ENTRY MINOR: floor k = {entry}")
    xs = ([Fr(j) for j in range(1, nsamples - 12)]
          + [Fr(-j) for j in range(1, 5)] + [Fr(2*j+1, 2) for j in range(1, 9)])
    ys, Ls = [], []
    for d in xs:
        H = pencil_H(n, d)
        D, L = floor_minor(H, entry)
        ys.append(D * L ** (entry * entry))
        Ls.append(L)
    Lpoly = mech.interp(xs, Ls)
    N = mech.interp(xs, ys)
    if N is None:
        print("  interpolation failed"); return
    N1, nL = mech.strip_factor(N, Lpoly)
    N2, ne = mech.strip_factor(N1, [Fr(0), Fr(1)])
    W_ext, d_ext = dl.extremal_type2_enumerator(n)
    H_ext = mech.H_of(W_ext, n, d_ext)
    dg = len(H_ext) - 1
    while H_ext[dg] == 0: dg -= 1
    lead_ext = H_ext[dg]
    c0 = N2[0]
    r = c0 / lead_ext
    print(f"  deg N = {len(N)-1}; L-stripped {nL}; delta-mult {ne}")
    print(f"  N~(0) = {c0}")
    print(f"  lead(H_ext) = {lead_ext}")
    print(f"  RATIO r = N~(0)/lead(H_ext) = {r}")
    print(f"    |r| num = {factorize(r.numerator)}")
    print(f"    |r| den = {factorize(r.denominator)}")
    # context data for recognition
    from math import comb
    print(f"  context: A_d(ext) = {W_ext[d_ext]}, C(n,4) = {comb(n,4)}, "
          f"C(n,{d_ext}) = {comb(n,d_ext)}, genus_pencil = {(n+2-8)//2}, "
          f"genus_ext = {(n+2-2*d_ext)//2}")
    roots = mech.isolate_roots(N2, Fr(0), Fr(80))
    print(f"  flip roots in (0,80): {[(str(a), str(b)) for a, b in roots]}")

def main():
    for n in (24, 32, 40):
        hunt(n)

if __name__ == "__main__":
    main()
