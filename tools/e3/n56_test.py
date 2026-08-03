# W-LINK out-of-sample: the n=56 stratum (double-step kind, second member).
# Registered predictions (in the sitting report, before this run): deg N~ = 2;
# c0 = -(25/2) lead(H_ext56); r1 ~ 3.6e5 in [2.5e5, 4.7e5]; w ~ 1.0e-3 in [2e-4, 1.2e-3].

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

def build56():
    b1 = dl.poly_pow(W8, 7)
    b2 = dl.poly_mul(dl.poly_pow(W8, 4), dl.G24)
    b3 = dl.poly_mul(W8, dl.poly_mul(dl.G24, dl.G24))
    basis = [b1, b2, b3]
    M = [[basis[j][t] for j in range(3)] for t in (0, 4, 8)]
    sol, ok, rank = dl.solve_linear(M, [Fr(0), Fr(1), Fr(0)])
    assert ok and sol is not None
    B = [sum(sol[j] * basis[j][i] for j in range(3)) for i in range(57)]
    W_ext, d_ext = dl.extremal_type2_enumerator(56)
    assert d_ext == 12
    return W_ext, B

def floor3(W_ext, B, delta):
    W = [W_ext[i] + Fr(delta) * B[i] for i in range(57)]
    H = mech.H_of(W, 56, 4)
    m, L = mech.monic_moments(H, 7)
    D = mech.rdet([[m[i + j + 1] for j in range(3)] for i in range(3)])
    return D, L

def main():
    W_ext, B = build56()
    # window bisection
    lo, hi = Fr(1, 100000), Fr(1, 10)
    D_lo, _ = floor3(W_ext, B, lo); D_hi, _ = floor3(W_ext, B, hi)
    s_lo, s_hi = (D_lo > 0) - (D_lo < 0), (D_hi > 0) - (D_hi < 0)
    print(f"signs at {lo}, {hi}: {s_lo}, {s_hi}")
    if s_lo != s_hi:
        a, b = lo, hi
        for _ in range(20):
            mid = (a + b) / 2
            Dm, _ = floor3(W_ext, B, mid)
            if ((Dm > 0) - (Dm < 0)) == s_lo: a = mid
            else: b = mid
        w = float((a + b) / 2)
        print(f"w(56) in ({float(a):.7f}, {float(b):.7f}) ~ {w:.6f}")
        print(f"registered: primary 1.0e-3, bracket [2e-4, 1.2e-3] | within: {2e-4 <= w <= 1.2e-3}")
    # N~ interpolation (deg 2 expected -> few samples)
    xs = [Fr(j) for j in (1, 2, 3, 5, 7, -1, -2)] + [Fr(1, 2), Fr(3, 2), Fr(5, 2)]
    ys, Ls = [], []
    for d in xs:
        D, L = floor3(W_ext, B, d)
        ys.append(D * L ** 9); Ls.append(L)
    Lpoly = mech.interp(xs, Ls)
    N = mech.interp(xs, ys)
    N1, nL = mech.strip_factor(N, Lpoly)
    N2, ne = mech.strip_factor(N1, [Fr(0), Fr(1)])
    print(f"deg N~ = {len(N2)-1} (registered: 2) | L-stripped {nL} | eps-mult {ne}")
    c0 = N2[0]
    H_ext = mech.H_of(W_ext, 56, 12)
    dg = len(H_ext) - 1
    while H_ext[dg] == 0: dg -= 1
    lead = H_ext[dg]
    print(f"c0 = {c0}")
    print(f"lead(H_ext56) = {lead}")
    print(f"c0/lead = {c0/lead}  (registered: -25/2 -> {c0/lead == Fr(-25,2)})")
    if len(N2) > 1:
        r1 = N2[1] / c0
        print(f"r1 = {r1} ~ {float(r1):.2f}  (registered: [2.5e5, 4.7e5])")
    if len(N2) > 2:
        r2 = N2[2] / c0
        print(f"r2 = {r2} ~ {float(r2):.2f}")

if __name__ == "__main__":
    main()
