# E-3 sitting 1 instrument — the extremal Type II 24k ladder (exact arithmetic throughout).
#
# Pipeline per rung:
#   1. Extremal Type II weight enumerator via Gleason basis (W8, g24), exact solve.
#   2. Duursma zeta polynomial P(T) solved from the defining coefficient identity
#      (two independent square subsystems solved and compared; full overdetermined
#      system then verified equation-by-equation).
#   3. Structural checks NOT imposed by the solve: P(1) = 1; the self-dual functional
#      equation p_{2g-i} = q^{g-i} p_i.
#   4. Duursma-RH certified EXACTLY: h(s) in Q(sqrt2)[s] with Q(tau) = tau^g h(tau+1/tau),
#      all roots of h real in [-2,2] via Sturm chains over Q(sqrt2) (recursive on gcd for
#      multiplicities).  RH <=> that containment.
#   5. Integrality test P/p0 in Z[T]; curve-partner factor test (1+2T+2T^2) | P.
#   6. mpmath high-precision root display (display only; the certificate is item 4).
#
# Validation rungs pin the convention and cross-check prior sittings' independent
# computations: [8,4,4] -> P=(1+2T+2T^2)/5 ; length-16 -> (1+2T+2T^2)(1-4T^4+16T^8)/P0 ;
# Golay [24,12,8] -> non-integral.

from fractions import Fraction as Fr
from math import comb
import mpmath as mp

Q = 2  # field size

# ---------- homogeneous (x,y) polynomials of degree n: list indexed by y-degree ----------

def poly_mul(a, b):
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    out[i + j] += ai * bj
    return out

def poly_pow(a, e):
    r = [Fr(1)]
    for _ in range(e):
        r = poly_mul(r, a)
    return r

# Gleason generators, as y-degree coefficient lists (homogeneous, x-degree implicit).
W8 = [Fr(0)] * 9
W8[0], W8[4], W8[8] = Fr(1), Fr(14), Fr(1)          # x^8 + 14 x^4 y^4 + y^8
# g24 = x^4 y^4 (x^4 - y^4)^4
_t = [Fr(0)] * 17
for j in range(5):
    _t[4 * j] = Fr(comb(4, j) * (-1) ** j)           # (x^4 - y^4)^4 over y-degree
G24 = [Fr(0)] * 25
for j in range(17):
    G24[j + 4] = _t[j]                               # shift by y^4 (x^4 implicit by homogeneity)

def solve_linear(M, rhs):
    """Exact Gaussian elimination; returns (solution_or_None, consistent, rank)."""
    rows = len(M); cols = len(M[0])
    A = [list(M[i]) + [rhs[i]] for i in range(rows)]
    piv_cols = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = Fr(1) / A[r][c]
        A[r] = [v * inv for v in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(cols + 1)]
        piv_cols.append(c)
        r += 1
        if r == rows:
            break
    for i in range(r, rows):
        if A[i][cols] != 0:
            return None, False, r
    if r < cols:
        return None, True, r  # underdetermined
    x = [Fr(0)] * cols
    for i, c in enumerate(piv_cols):
        x[c] = A[i][cols]
    return x, True, r

def extremal_type2_enumerator(n):
    """Unique extremal Type II enumerator: A_0 = 1, A_i = 0 for 0 < i < 4*floor(n/24)+4."""
    assert n % 8 == 0
    m = n // 8
    jmax = m // 3
    basis = [poly_mul(poly_pow(W8, m - 3 * j), poly_pow(G24, j)) for j in range(jmax + 1)]
    # conditions: y^0 coeff = 1; y^(4t) coeff = 0 for t = 1..jmax
    M = [[basis[j][4 * t] for j in range(jmax + 1)] for t in range(jmax + 1)]
    rhs = [Fr(1)] + [Fr(0)] * jmax
    c, ok, rank = solve_linear(M, rhs)
    assert ok and c is not None, "Gleason solve failed"
    W = [Fr(0)] * (n + 1)
    for j, cj in enumerate(c):
        for i, v in enumerate(basis[j]):
            W[i] += cj * v
    d = 4 * (n // 24) + 4
    assert W[0] == 1
    for i in range(1, d):
        assert W[i] == 0, (n, i, W[i])
    assert W[d] != 0
    assert all(W[i] == W[n - i] for i in range(n + 1)), "x<->y symmetry fails"
    return W, d

# ---------- Duursma zeta from the defining identity ----------

def zeta_from_enumerator(W, n, d, swap):
    """Solve P from: [T^(n-d)] ( (uT + v(1-T))^n * P(T) / ((1-T)(1-qT)) ) = (W - x^n)/(q-1).
    swap=False: (u,v)=(x,y);  swap=True: (u,v)=(y,x).
    Returns (p, report) with p the coefficient list of P, plus verification data."""
    g2 = n + 2 - 2 * d          # deg P = 2g for self-dual (d = dperp)
    tmax = n - d
    # B_s(x,y) = [T^s] (uT+v(1-T))^n  as y-degree lists
    B = []
    for s in range(tmax + 1):
        row = [Fr(0)] * (n + 1)
        for a in range(0, s + 1):
            cf = Fr(comb(n, a) * comb(n - a, s - a) * (-1) ** (s - a))
            if cf == 0:
                continue
            ydeg = a if swap else n - a   # u carries T; u=y if swap else x
            row[ydeg] += cf
        B.append(row)
    e = [Fr(Q ** (j + 1) - 1, Q - 1) for j in range(tmax + 1)]
    # G_t = sum_{s<=t} B_s * e_{t-s}
    Gg = []
    for t in range(tmax + 1):
        row = [Fr(0)] * (n + 1)
        for s in range(t + 1):
            ee = e[t - s]
            Bs = B[s]
            for i in range(n + 1):
                if Bs[i]:
                    row[i] += Bs[i] * ee
        Gg.append(row)
    # equations: sum_i p_i * G_{n-d-i}[mono] = RHS[mono]
    ncols = g2 + 1
    M = [[(Gg[tmax - i][mono] if tmax - i >= 0 else Fr(0)) for i in range(ncols)]
         for mono in range(n + 1)]
    rhs = [Fr(0)] * (n + 1)
    for i in range(1, n + 1):
        rhs[i] = Fr(W[i], Q - 1)
    rhs[0] = Fr(W[0] - 1, Q - 1)  # subtract x^n

    # route A: first rows; route B: last rows (independent subsystems)
    ordA = list(range(n + 1))
    ordB = list(reversed(range(n + 1)))
    def take_square(order):
        rowsM, rowsR = [], []
        for mono in order:
            rowsM.append(M[mono]); rowsR.append(rhs[mono])
            if len(rowsM) >= ncols:
                sol, ok, rank = solve_linear(rowsM, rowsR)
                if ok and sol is not None:
                    return sol
        return None
    pA = take_square(ordA)
    pB = take_square(ordB)
    if pA is None or pB is None or pA != pB:
        return None, {"routes_agree": False}
    p = pA
    # full overdetermined verification, every monomial equation
    bad = 0
    for mono in range(n + 1):
        lhs = sum(p[i] * M[mono][i] for i in range(ncols))
        if lhs != rhs[mono]:
            bad += 1
    return p, {"routes_agree": True, "equations": n + 1, "failed": bad}

# ---------- Q(sqrt2) exact arithmetic ----------

class F2:
    __slots__ = ("a", "b")
    def __init__(self, a, b=Fr(0)):
        self.a, self.b = Fr(a), Fr(b)
    def __add__(s, o): return F2(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return F2(s.a - o.a, s.b - o.b)
    def __neg__(s):    return F2(-s.a, -s.b)
    def __mul__(s, o): return F2(s.a * o.a + 2 * s.b * o.b, s.a * o.b + s.b * o.a)
    def inv(s):
        den = s.a * s.a - 2 * s.b * s.b
        assert den != 0
        return F2(s.a / den, -s.b / den)
    def __truediv__(s, o): return s * o.inv()
    def is_zero(s): return s.a == 0 and s.b == 0
    def sign(s):
        if s.b == 0: return (s.a > 0) - (s.a < 0)
        if s.a == 0: return (s.b > 0) - (s.b < 0)
        if s.a > 0 and s.b > 0: return 1
        if s.a < 0 and s.b < 0: return -1
        d = s.a * s.a - 2 * s.b * s.b   # sign(a + b sqrt2) with mixed signs
        return ((d > 0) - (d < 0)) * ((s.a > 0) - (s.a < 0))
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def __repr__(s): return f"({s.a}+{s.b}√2)"

def f2p_deg(p):
    d = len(p) - 1
    while d >= 0 and p[d].is_zero():
        d -= 1
    return d

def f2p_trim(p):
    return p[:f2p_deg(p) + 1] if f2p_deg(p) >= 0 else [F2(0)]

def f2p_eval(p, s):   # s is F2
    acc = F2(0)
    for c in reversed(p):
        acc = acc * s + c
    return acc

def f2p_deriv(p):
    return f2p_trim([p[i] * F2(i) for i in range(1, len(p))]) if len(p) > 1 else [F2(0)]

def f2p_divmod(a, b):
    a = list(a); db, db_ = f2p_deg(b), None
    assert db >= 0
    inv = b[db].inv()
    q = [F2(0)] * max(1, len(a) - db)
    while f2p_deg(a) >= db:
        da = f2p_deg(a)
        c = a[da] * inv
        q[da - db] = c
        for i in range(db + 1):
            a[i + da - db] = a[i + da - db] - c * b[i]
        a[da] = F2(0)  # force exact cancellation
    return f2p_trim(q), f2p_trim(a)

def f2p_gcd(a, b):
    a, b = f2p_trim(a), f2p_trim(b)
    while f2p_deg(b) >= 0 and not (f2p_deg(b) == 0 and b[0].is_zero()):
        _, r = f2p_divmod(a, b)
        a, b = b, r
        if f2p_deg(b) < 0 or (f2p_deg(b) == 0 and b[0].is_zero()):
            break
    # normalize monic
    d = f2p_deg(a)
    inv = a[d].inv()
    return [c * inv for c in a]

def sturm_count_open(p, lo, hi):
    """# distinct real roots of squarefree p in open interval (lo, hi); lo,hi rational F2."""
    chain = [f2p_trim(p), f2p_deriv(p)]
    while f2p_deg(chain[-1]) > 0:
        _, r = f2p_divmod(chain[-2], chain[-1])
        if f2p_deg(r) < 0 or (f2p_deg(r) == 0 and r[0].is_zero()):
            break
        chain.append([F2(-c.a, -c.b) for c in r])
    def var(x):
        signs = [f2p_eval(c, x).sign() for c in chain]
        signs = [s for s in signs if s != 0]
        return sum(1 for i in range(len(signs) - 1) if signs[i] * signs[i + 1] < 0)
    return var(lo) - var(hi)

def all_roots_real_in_pm2(h):
    """True iff every root of h (with multiplicity) is real and lies in [-2, 2]."""
    h = f2p_trim(h)
    if f2p_deg(h) <= 0:
        return True
    hp = f2p_deriv(h)
    gg = f2p_gcd(h, hp)
    hsf, rem = f2p_divmod(h, gg)
    assert f2p_deg(rem) < 0 or (f2p_deg(rem) == 0 and rem[0].is_zero())
    hsf = f2p_trim(hsf)
    # endpoint roots
    ends = 0
    for pt in (F2(-2), F2(2)):
        if f2p_eval(hsf, pt).is_zero():
            hsf, r0 = f2p_divmod(hsf, [F2(0) - pt, F2(1)])  # divide by (s - pt)
            assert f2p_deg(r0) < 0 or r0[0].is_zero()
            ends += 1
    inner = sturm_count_open(hsf, F2(-2), F2(2)) if f2p_deg(hsf) > 0 else 0
    if ends + inner != f2p_deg(hsf) + ends:  # all distinct roots of hsf accounted for
        return False
    return all_roots_real_in_pm2(gg)

# ---------- per-rung analysis ----------

def analyze(name, W, n, d, swap_convention):
    p, rep = zeta_from_enumerator(W, n, d, swap_convention)
    assert p is not None and rep["routes_agree"] and rep["failed"] == 0, (name, rep)
    g2 = n + 2 - 2 * d
    g = g2 // 2
    # structural checks not imposed by the solve
    P1 = sum(p)
    fe_ok = all(p[g2 - i] == Fr(Q) ** (g - i) * p[i] for i in range(g2 + 1))
    # h(s): Q(tau)=sum p_i tau^i / 2^{i/2}; h = ptilde_g + sum_{j>=1} ptilde_{g+j} v_j(s)
    # ptilde_{g+j} = p_{g+j} / 2^{(g+j)/2} : rational when g+j even, (rational)*sqrt2/2.. handle in F2
    def ptilde(i):
        # p_i / sqrt2^i  = p_i / 2^{i//2} * (1/sqrt2 if i odd)
        base = Fr(p[i], 2 ** (i // 2))
        return F2(base, 0) if i % 2 == 0 else F2(0, base / 2)  # 1/sqrt2 = sqrt2/2
    # v_j(s): v0=2, v1=s, v_j = s v_{j-1} - v_{j-2}
    v_prev = [F2(2)]          # v0
    v_curr = [F2(0), F2(1)]   # v1
    h = [ptilde(g)]
    def padd(a, b):
        m = max(len(a), len(b))
        return [ (a[i] if i < len(a) else F2(0)) + (b[i] if i < len(b) else F2(0)) for i in range(m) ]
    def pscale(a, c):
        return [x * c for x in a]
    def pmuls(a):  # multiply by s
        return [F2(0)] + a
    for j in range(1, g + 1):
        vj = v_curr if j == 1 else None
        if j == 1:
            vj = v_curr
        else:
            vj = padd(pmuls(v_curr), pscale(v_prev, F2(-1)))
            v_prev, v_curr = v_curr, vj
        h = padd(h, pscale(vj, ptilde(g + j)))
    h = f2p_trim(h)
    assert f2p_deg(h) == g, (f2p_deg(h), g)
    rh_exact = all_roots_real_in_pm2(h)
    # integrality & normalization
    p0 = p[0]
    norm = [pi / p0 for pi in p]
    integral = all(v.denominator == 1 for v in norm)
    # curve-partner factor (1 + 2T + 2T^2) | P ?
    def qdivmod(a, b):
        a = [Fr(v) for v in a]; db = len(b) - 1
        qq = [Fr(0)] * max(1, len(a) - db)
        while len(a) - 1 >= db and any(a):
            da = max(i for i, v in enumerate(a) if v != 0) if any(a) else -1
            if da < db: break
            c = a[da] / b[db]
            qq[da - db] = c
            for i in range(db + 1):
                a[i + da - db] -= c * b[i]
        return qq, a
    _, remf = qdivmod(p, [Fr(1), Fr(2), Fr(2)])
    factor_divides = all(v == 0 for v in remf)
    # numeric roots (display only)
    max_dev = None
    try:
        mp.mp.dps = 60
        roots = mp.polyroots([mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in reversed(norm)],
                             maxsteps=400, extraprec=300)
        max_dev = max(abs(abs(r) - 1 / mp.sqrt(2)) for r in roots)
    except Exception as ex:
        max_dev = f"numeric-display-failed: {ex}"
    return {
        "name": name, "n": n, "d": d, "g": g, "deg": g2,
        "P1": P1, "FE": fe_ok, "RH_exact": rh_exact,
        "eqs": rep["equations"], "p": p, "norm": norm,
        "integral": integral, "curve_factor": factor_divides,
        "max_dev": max_dev,
    }

def wt_dist_head(W, upto=3):
    out = []
    cnt = 0
    for i, v in enumerate(W):
        if v != 0 and i > 0:
            out.append((i, v)); cnt += 1
            if cnt >= upto: break
    return out

def main():
    # ---- convention pin on [8,4,4] ----
    W8_844 = [Fr(0)] * 9
    W8_844[0], W8_844[4], W8_844[8] = Fr(1), Fr(14), Fr(1)
    target = [Fr(1, 5), Fr(2, 5), Fr(2, 5)]
    pinned = None
    for swap in (False, True):
        p, rep = zeta_from_enumerator(W8_844, 8, 4, swap)
        if p is not None and rep["failed"] == 0 and p == target:
            pinned = swap
            print(f"[convention] pinned: swap={swap} reproduces P=(1+2T+2T^2)/5 on [8,4,4]")
    assert pinned is not None, "convention pin failed"

    # ---- validation rungs ----
    print("\n=== VALIDATION RUNGS ===")
    res844 = analyze("[8,4,4] e8-code", W8_844, 8, 4, pinned)
    print(res844["name"], "P =", res844["p"], "| P(1)=", res844["P1"], "| FE:", res844["FE"],
          "| RH exact:", res844["RH_exact"], "| integral:", res844["integral"])
    W16 = poly_mul(W8_844, W8_844)  # E8+E8 / d16+ shared enumerator
    res16 = analyze("length-16 (e8+e8 / d16+)", W16, 16, 4, pinned)
    print(res16["name"], "| P(1)=", res16["P1"], "| FE:", res16["FE"],
          "| RH exact:", res16["RH_exact"], "| integral:", res16["integral"],
          "| (1+2T+2T^2) divides:", res16["curve_factor"])
    print("  P/P(0) =", [str(v) for v in res16["norm"]])

    # ---- the ladder k = 1..5 ----
    print("\n=== THE EXTREMAL 24k LADDER ===")
    known_heads = {24: (8, 759), 48: (12, 17296), 72: (16, 249849)}
    results = []
    for k in range(1, 6):
        n = 24 * k
        W, d = extremal_type2_enumerator(n)
        if n in known_heads:
            dd, Ad = known_heads[n]
            assert d == dd and W[d] == Ad, (n, d, W[d])
            print(f"[cross-check] n={n}: A_{d} = {W[d]} matches the literature value")
        r = analyze(f"extremal n={n} (d={d}, g={r0g(n,d)})", W, n, d, pinned)
        results.append(r)
        print(f"n={n} d={d} g={r['g']} degP={r['deg']} | eqs verified: {r['eqs']} "
              f"| P(1)={r['P1']} | FE:{r['FE']} | RH-EXACT:{r['RH_exact']} "
              f"| integral:{r['integral']} | curve-factor:{r['curve_factor']} "
              f"| max | |T|-1/sqrt2 | = {r['max_dev']}")
        print(f"    p_i all positive: {all(v > 0 for v in r['p'])}"
              f" | p (first 6): {[str(v) for v in r['p'][:6]]}")
    print("\n=== SUMMARY TABLE ===")
    for r in results:
        print(f"n={r['n']:4d} d={r['d']:3d} g={r['g']:3d} RH_exact={r['RH_exact']} "
              f"integral={r['integral']} curve_factor={r['curve_factor']}")

def r0g(n, d):
    return (n + 2 - 2 * d) // 2

if __name__ == "__main__":
    main()
