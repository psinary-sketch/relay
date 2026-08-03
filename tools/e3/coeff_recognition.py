# E-21 face 2 — THE HIGHER-COEFFICIENT RECOGNITION.
# Full reduced flip polynomials N~ at the k=3 floor minor for n = 24, 32, 40 (exact
# interpolation); the coefficient ratios c_j/c_0 computed exactly; the epsilon^1 ratio
# tested for a cross-n law in the recognition basis (genus-linear families / C(n,k) /
# A_d / p-coefficients); factorizations printed for the recognition step.

from fractions import Fraction as Fr
import importlib.util, sys, pathlib
from math import comb

spec = importlib.util.spec_from_file_location(
    "dl", str(pathlib.Path(__file__).with_name("duursma_ladder.py")))
dl = importlib.util.module_from_spec(spec); sys.modules["dl"] = dl; spec.loader.exec_module(dl)
spec2 = importlib.util.spec_from_file_location(
    "gs", str(pathlib.Path(__file__).with_name("genus5.py")))
gs = importlib.util.module_from_spec(spec2); sys.modules["gs"] = gs; spec2.loader.exec_module(gs)
spec3 = importlib.util.spec_from_file_location(
    "ah", str(pathlib.Path(__file__).with_name("additive_hunt.py")))
ah = importlib.util.module_from_spec(spec3); sys.modules["ah"] = ah; spec3.loader.exec_module(ah)
mech = ah.mech

def reduced_poly(n, k=3):
    xs = ([Fr(j) for j in range(1, 34)] + [Fr(-j) for j in range(1, 5)]
          + [Fr(2*j+1, 2) for j in range(1, 8)])
    ys, Ls = [], []
    for d in xs:
        H = ah.pencil_H(n, d)
        D, L = ah.floor_minor(H, k)
        ys.append(D * L ** (k * k)); Ls.append(L)
    Lpoly = mech.interp(xs, Ls)
    N = mech.interp(xs, ys)
    N1, _ = mech.strip_factor(N, Lpoly)
    N2, _ = mech.strip_factor(N1, [Fr(0), Fr(1)])
    return N2

def main():
    data = {}
    for n in (24, 32, 40):
        N2 = reduced_poly(n)
        data[n] = N2
        print(f"n={n}: reduced N~ degree {len(N2)-1}")
        c0 = N2[0]
        for j, c in enumerate(N2):
            if j == 0:
                print(f"  c_0 = {c}")
            else:
                r = c / c0
                print(f"  c_{j}/c_0 = {r}  | num {ah.factorize(r.numerator)} | "
                      f"den {ah.factorize(r.denominator)}")
        print(f"  context: C(n,4) = {comb(n,4)}, genus_pencil = {(n-6)//2 + 0 if False else (n+2-8)//2}")
    # cross-n law test on the eps^1 ratio: is c1/c0 * C(n,4) (or similar) genus-linear?
    print("\n=== cross-n tests on r1 = c_1/c_0 ===")
    r1 = {n: data[n][1] / data[n][0] for n in (24, 32, 40)}
    for n in (24, 32, 40):
        print(f"  n={n}: r1 = {r1[n]} ~ {float(r1[n]):.6f}")
    for name, scale in (("r1 * C(n,4)", lambda n: comb(n, 4)),
                        ("r1 * (n+16)", lambda n: n + 16),
                        ("r1 * n", lambda n: n),
                        ("r1 * genus", lambda n: (n + 2 - 8) // 2)):
        vals = [r1[n] * scale(n) for n in (24, 32, 40)]
        d1 = vals[1] - vals[0]; d2 = vals[2] - vals[1]
        lin = (d2 == d1)
        print(f"  {name}: {[str(v) for v in vals]} | linear in n(step8): {lin}")
        fv = [float(v) for v in vals]
        print(f"    floats: {fv} | diffs {fv[1]-fv[0]:.6f}, {fv[2]-fv[1]:.6f}")

if __name__ == "__main__":
    main()
