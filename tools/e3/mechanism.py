# Genus-9 face 3 — THE MECHANISM EXTRACTION.
# Structure: the zeta defining system's matrix is c-independent => p(c) AFFINE in c;
# h affine; H(u) = h h^sigma QUADRATIC in c.  With eps = c + 42 (the extremality defect,
# = A_4 of the pencil member), the monic-moment Hankel minors are D_k(eps) = N_k(eps)/L(eps)^{k^2}
# with L = lead(H) and N_k a POLYNOMIAL — exactly reconstructible by interpolation from
# exact samples.  Deliverable: N_k for the shallow flipping minors (floor k=2, reality k=3),
# their eps-structure (multiplicity at 0, L-factors stripped, rational roots, the boundary
# root isolated exactly), coefficient signs — the candidate distinguishing datum.
# Control: the n=32 pencil (defect delta = 56 + c) — is the boundary defect-structured?

from fractions import Fraction as Fr
import importlib.util, sys, pathlib

spec = importlib.util.spec_from_file_location(
    "dl", str(pathlib.Path(__file__).with_name("duursma_ladder.py")))
dl = importlib.util.module_from_spec(spec); sys.modules["dl"] = dl; spec.loader.exec_module(dl)
spec2 = importlib.util.spec_from_file_location(
    "gs", str(pathlib.Path(__file__).with_name("genus5.py")))
gs = importlib.util.module_from_spec(spec2); sys.modules["gs"] = gs; spec2.loader.exec_module(gs)

W8 = dl.W8
W83 = dl.poly_mul(dl.poly_mul(W8, W8), W8)
W84 = dl.poly_mul(W83, W8)
W8G = dl.poly_mul(W8, dl.G24)   # length-32 Gleason second basis element

def H_of(W, n, d):
    p, rep = dl.zeta_from_enumerator(W, n, d, False)
    assert p is not None and rep["failed"] == 0
    g = (n + 2 - 2 * d) // 2
    h = gs.build_h(p, g)
    return gs.rational_certificate(h)   # H(u) in Q[u], ascending

def monic_moments(H, kmax):
    dg = len(H) - 1
    while H[dg] == 0: dg -= 1
    L = H[dg]
    A = [Fr(0)] * (kmax + 1)
    for i in range(1, min(dg, kmax) + 1):
        A[i] = H[dg - i] / L
    m = [Fr(dg)] + [Fr(0)] * kmax
    for k in range(1, kmax + 1):
        acc = -Fr(k) * (A[k] if k <= dg else Fr(0))
        for i in range(1, min(k, dg + 1)):
            acc -= A[i] * m[k - i]
        m[k] = acc
    return m, L

def rdet(M):
    n = len(M); A = [r[:] for r in M]; det = Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None: return Fr(0)
        if p != c: A[c], A[p] = A[p], A[c]; det = -det
        det *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            A[r] = [A[r][j] - f * A[c][j] for j in range(n)]
    return det

def sample(eps):
    c = eps - 42
    W = [W83[i] + Fr(c) * dl.G24[i] for i in range(25)]
    H = H_of(W, 24, 4)
    m, L = monic_moments(H, 19)
    return m, L

def interp(xs, ys):
    """Exact min-degree polynomial through (xs, ys); verified on all points."""
    for deg in range(1, len(xs)):
        M = [[Fr(x) ** j for j in range(deg + 1)] for x in xs[:deg + 1]]
        sol, ok, rank = dl.solve_linear(M, ys[:deg + 1])
        if not ok or sol is None: continue
        if all(sum(sol[j] * Fr(x) ** j for j in range(deg + 1)) == y
               for x, y in zip(xs, ys)):
            return sol
    return None

def poly_str(P, var="e"):
    terms = []
    for j, c in enumerate(P):
        if c != 0:
            terms.append(f"({c}){var}^{j}")
    return " + ".join(terms) if terms else "0"

def strip_factor(P, F):
    """Divide P by F as many times as exact; return (reduced, count)."""
    from fractions import Fraction
    cnt = 0
    while True:
        q, r = divmod_poly(P, F)
        if r is not None and all(v == 0 for v in r) and any(q):
            P = q; cnt += 1
        else:
            return P, cnt

def divmod_poly(a, b):
    a = list(a); db = len(b) - 1
    while db >= 0 and b[db] == 0: db -= 1
    if db < 0: return None, None
    da = len(a) - 1
    while da >= 0 and a[da] == 0: da -= 1
    if da < db: return [Fr(0)], a
    q = [Fr(0)] * (da - db + 1)
    while da >= db:
        f = a[da] / b[db]
        q[da - db] = f
        for i in range(db + 1):
            a[da - db + i] -= f * b[i]
        while da >= 0 and a[da] == 0: da -= 1
    return q, a

def eval_poly(P, x):
    acc = Fr(0)
    for c in reversed(P): acc = acc * Fr(x) + c
    return acc

def isolate_roots(P, lo, hi, steps=200):
    """Sign-change bracketing of real roots of P in (lo, hi)."""
    out = []
    prev_x, prev_s = None, None
    for i in range(steps + 1):
        x = Fr(lo) + (Fr(hi) - Fr(lo)) * i / steps
        v = eval_poly(P, x)
        s = (v > 0) - (v < 0)
        if prev_s is not None and s != 0 and prev_s != 0 and s != prev_s:
            a, b = prev_x, x
            for _ in range(30):
                mid = (a + b) / 2
                vm = eval_poly(P, mid)
                sm = (vm > 0) - (vm < 0)
                if sm == prev_s: a = mid
                else: b = mid
            out.append((a, b))
        if s != 0:
            prev_x, prev_s = x, s
    return out

def main():
    print("=== sampling the n=24 pencil exactly (eps = c + 42 = A_4, the defect) ===")
    eps_list = ([Fr(j) for j in range(1, 31)] + [Fr(-j) for j in range(1, 9)]
                + [Fr(17, 2), Fr(19, 2), Fr(35, 2), Fr(51, 2), Fr(61, 2), Fr(65, 2),
                   Fr(43, 2), Fr(27, 2)])
    data = {}
    for e in eps_list:
        m, L = sample(e)
        data[e] = (m, L)
    print(f"samples: {len(eps_list)}")
    # L(eps): quadratic — interpolate
    xs = eps_list
    Lpoly = interp(xs, [data[e][1] for e in xs])
    print(f"L(eps) = lead(H) = {poly_str(Lpoly)}")
    # N_k = D_k * L^{k^2} for floor k=2 (shift 1... floor layer = [m_{i+j+1}]) and reality k=3 ([m_{i+j}])
    targets = [("floor k=2", 1, 2), ("floor k=3", 1, 3), ("reality k=3", 0, 3), ("reality k=4", 0, 4)]
    for name, shift, k in targets:
        ys = []
        for e in xs:
            m, L = data[e]
            D = rdet([[m[i + j + shift] for j in range(k)] for i in range(k)])
            ys.append(D * L ** (k * k))
        N = interp(xs, ys)
        if N is None:
            print(f"{name}: interpolation failed (degree > {len(xs)-1})"); continue
        # strip L factors and eps factors
        N1, nL = strip_factor(N, Lpoly)
        N2, ne = strip_factor(N1, [Fr(0), Fr(1)])
        print(f"\n{name}: deg N = {len(N)-1} | L-factors stripped: {nL} | eps-multiplicity: {ne}")
        print(f"  reduced N~ (deg {len(N2)-1}): {poly_str(N2)}")
        roots = isolate_roots(N2, Fr(0), Fr(45))
        print(f"  real roots of N~ in (0, 45): {[(str(a), str(b)) for a, b in roots]}")
        rneg = isolate_roots(N2, Fr(-10), Fr(0))
        print(f"  real roots of N~ in (-10, 0): {[(str(a), str(b)) for a, b in rneg]}")
    print("\n=== control: the n=32 pencil (defect delta = 56 + c; extremal at c = -56) ===")
    # flip boundary for floor k=2 by bisection on delta
    def floor2_sign(delta):
        c = delta - 56
        W = [W84[i] + Fr(c) * W8G[i] for i in range(33)]
        H = H_of(W, 32, 4)
        m, L = monic_moments(H, 7)
        D = rdet([[m[i + j + 1] for j in range(2)] for i in range(2)])
        return (D > 0) - (D < 0)
    lo, hi = Fr(1), Fr(56)  # expect + near extremal? sample ends
    s_lo, s_hi = floor2_sign(lo), floor2_sign(hi)
    print(f"floor k=2 sign at delta=1: {s_lo}; at delta=56 (c=0): {s_hi}")
    if s_lo != s_hi:
        a, b = lo, hi
        for _ in range(20):
            mid = (a + b) / 2
            if floor2_sign(mid) == s_lo: a = mid
            else: b = mid
        print(f"n=32 floor-k=2 flip at delta* in ({a}, {b}) = ({float(a):.3f}, {float(b):.3f});"
              f" fraction of full defect: {float((a+b)/2)/56:.3f}")
    print("n=24 comparison: eps* (floor k=2 flip) as fraction of 42: see roots above")

if __name__ == "__main__":
    main()
