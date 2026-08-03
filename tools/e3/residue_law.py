# E-3 re-aimed — THE RESIDUE LAW at the next strata (exact).
# (1) The lead law: along the n=32 pencil (W8^4 + c*W8G, defect delta = A_4 = 56+c) and the
#     n=40 pencil (W8^5 + c*W8^2*G24, delta = 70+c): is lead(H)(delta) = const * delta^2
#     exactly (the defect's double zero at every extremal point)?
# (2) The constant-term law at n=32's entry minor (floor k=3): does the reduced flip
#     polynomial's value at delta=0 equal a negative multiple of lead(H_extremal32)?
# (3) Bonus rung: extremal n=40 (d=8, g=13) — full certificate (RH exact?).

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
W84 = mech.W84
W8G = mech.W8G
W85 = dl.poly_mul(W84, W8)
W82G = dl.poly_mul(dl.poly_mul(W8, W8), dl.G24)

def pencil_H(base, second, n, delta, defect0):
    c = delta - defect0
    W = [base[i] + Fr(c) * second[i] for i in range(n + 1)]
    return mech.H_of(W, n, 4)

def lead(H):
    d = len(H) - 1
    while H[d] == 0: d -= 1
    return H[d], d

def lead_law(base, second, n, defect0, label):
    xs = [Fr(1), Fr(2), Fr(3), Fr(5), Fr(7), Fr(-1), Fr(11, 2)]
    ys = []
    for delta in xs:
        L, dg = lead(pencil_H(base, second, n, delta, defect0))
        ys.append(L)
    P = mech.interp(xs, ys)
    print(f"{label}: lead(H)(delta) = {mech.poly_str(P, 'd')}")
    dz = (len(P) > 2 and P[0] == 0 and P[1] == 0 and P[2] != 0
          and all(v == 0 for v in P[3:]))
    print(f"  DOUBLE ZERO at delta=0 (lead = const*delta^2 exactly): {dz}")
    return P

def main():
    print("=== (1) THE LEAD LAW ===")
    P32 = lead_law(W84, W8G, 32, 56, "n=32 pencil (g=13)")
    P40 = lead_law(W85, W82G, 40, 70, "n=40 pencil (g=17)")

    print("\n=== (2) the constant-term law at n=32 (entry minor: floor k=3) ===")
    xs = ([Fr(j) for j in range(1, 15)] + [Fr(-j) for j in range(1, 4)]
          + [Fr(2 * j + 1, 2) for j in range(1, 6)])
    ys = []
    Lpoly_samples = []
    for delta in xs:
        H = pencil_H(W84, W8G, 32, delta, 56)
        m, L = mech.monic_moments(H, 7)
        D = mech.rdet([[m[i + j + 1] for j in range(3)] for i in range(3)])
        ys.append(D * L ** 9)
        Lpoly_samples.append(L)
    Lpoly = mech.interp(xs, Lpoly_samples)
    N = mech.interp(xs, ys)
    if N is None:
        print("interpolation failed (need more samples)")
    else:
        N1, nL = mech.strip_factor(N, Lpoly)
        N2, ne = mech.strip_factor(N1, [Fr(0), Fr(1)])
        print(f"deg N = {len(N)-1} | L-factors stripped: {nL} | delta-multiplicity: {ne}")
        print(f"N~(0) = {N2[0]}")
        W32, d32 = dl.extremal_type2_enumerator(32)
        Hx = mech.H_of(W32, 32, 8)
        Lx, dgx = lead(Hx)
        print(f"lead(H_extremal32) = {Lx}")
        ratio = N2[0] / Lx
        print(f"N~(0) / lead(H_ext32) = {ratio}  (negative ratio = the residue law's "
              f"constant-term half, persisting)")
        roots = mech.isolate_roots(N2, Fr(0), Fr(60))
        print(f"real roots of N~ in (0,60): {[(str(a), str(b)) for a, b in roots]}")

    print("\n=== (3) bonus rung: extremal n=40 (d=8, g=13) full certificate ===")
    W40, d40 = dl.extremal_type2_enumerator(40)
    r = dl.analyze("extremal n=40", W40, 40, 8, False)
    print(f"n=40 d={d40} g={r['g']} | RH-EXACT: {r['RH_exact']} | P(1)={r['P1']} FE:{r['FE']}"
          f" | integral: {r['integral']} | curve-factor: {r['curve_factor']}")

if __name__ == "__main__":
    main()
