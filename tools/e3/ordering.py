# Genus-9 face 2 — THE ORDERING CHECK: along the Gleason pencil, which Hankel layer flips
# at shallower depth: reality (Hamburger, [m_{i+j}]), floor (Stieltjes, [m_{i+j+1}], u >= 0),
# or ceiling (Hausdorff top, [4 m_{i+j} - m_{i+j+1}], u <= 4)?  Exact over Q throughout:
# power sums m_k of H(u)'s roots by Newton from H(u) in Q[u]; determinants by exact
# fraction Gaussian elimination.  Compared against the zeta-meter's found texture.

from fractions import Fraction as Fr
import importlib.util, sys, pathlib

spec = importlib.util.spec_from_file_location(
    "dl", str(pathlib.Path(__file__).with_name("duursma_ladder.py")))
dl = importlib.util.module_from_spec(spec); sys.modules["dl"] = dl; spec.loader.exec_module(dl)
spec2 = importlib.util.spec_from_file_location(
    "gs", str(pathlib.Path(__file__).with_name("genus5.py")))
gs = importlib.util.module_from_spec(spec2); sys.modules["gs"] = gs; spec2.loader.exec_module(gs)

def newton_rational(H):
    d = len(H) - 1
    while H[d] == 0: d -= 1
    A = [Fr(0)] * (2 * d + 1)
    for i in range(1, d + 1):
        A[i] = H[d - i] / H[d]
    m = [Fr(d)] + [Fr(0)] * (2 * d)
    for k in range(1, 2 * d + 1):
        acc = -Fr(k) * (A[k] if k <= d else Fr(0))
        for i in range(1, min(k, d + 1)):
            acc -= A[i] * m[k - i]
        m[k] = acc
    return m, d

def rdet(M):
    n = len(M)
    A = [row[:] for row in M]
    det = Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            A[c], A[p] = A[p], A[c]; det = -det
        det *= A[c][c]
        inv = A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / inv
            A[r] = [A[r][j] - f * A[c][j] for j in range(n)]
    return det

def first_flip(m, entry, dmax):
    for d in range(1, dmax + 1):
        M = [[entry(m, i, j) for j in range(d)] for i in range(d)]
        if rdet(M) < 0:
            return d
    return None

def layers(W, n, dd, label):
    r = dl.analyze(label, W, n, dd, False)
    h = gs.build_h(r["p"], r["g"])
    H = gs.rational_certificate(h)
    m, deg = newton_rational(H)
    dmax = deg
    f_real = first_flip(m, lambda m, i, j: m[i + j], dmax)
    f_floor = first_flip(m, lambda m, i, j: m[i + j + 1], dmax)
    f_ceil = first_flip(m, lambda m, i, j: 4 * m[i + j] - m[i + j + 1], dmax)
    fmt = lambda f: f if f else "-"
    print(f"{label:28s} | RH={str(r['RH_exact']):5s} | reality:{fmt(f_real)}  "
          f"floor(u>=0):{fmt(f_floor)}  ceiling(u<=4):{fmt(f_ceil)}")
    return f_real, f_floor, f_ceil

def main():
    print("first-negative-minor depth per layer ('-' = PSD through full depth):\n")
    W32, _ = dl.extremal_type2_enumerator(32)
    layers(W32, 32, 8, "extremal n=32 (confining)")
    W8 = dl.W8
    W83 = dl.poly_mul(dl.poly_mul(W8, W8), W8)
    for c in (Fr(0), Fr(-10), Fr(-21), Fr(-30), Fr(-35), Fr(-41), Fr(-419, 10), Fr(-43), Fr(-50)):
        Wc = [W83[i] + c * dl.G24[i] for i in range(25)]
        layers(Wc, 24, 4, f"pencil c={c}")

if __name__ == "__main__":
    main()
