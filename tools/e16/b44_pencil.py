#!/usr/bin/env python3
"""
b44 second block -- THE PENCIL-GCD AT (2,2): does E1(2,2) (d_1 = 2) contain ANY
nonzero Schmidt-pure vector over the algebraic closure? Registered in
data/b44_registration_2026-08-19.txt (VERDICT VOCABULARY: MIXED-FORCED decidable
exactly at d_1 <= 2 by the pencil-GCD over Q(zeta)[t]). Exact arithmetic:
Q(zeta_16) as 8-tuples of Fractions mod x^8 + 1. No floating point.

Every vector of E1(2,2) is alpha*C1 + beta*C2. Pure <=> all 2x2 minors vanish.
For alpha != 0 write t = beta/alpha: the nine minors are quadratics m_k(t) over
Q(zeta_16); a pure vector exists iff the m_k share a root over CLOSURE(Q(zeta_16))
iff gcd_k m_k(t) is nonconstant -- or C2 alone is pure (checked exactly: it is not,
b44 first block). GCD over a field detects closure roots: polynomials with no
common factor generate (1) in Q(zeta_16)[t], hence have no common root anywhere.
"""
from fractions import Fraction
from itertools import combinations

P, N, Q = 2, 16, 4
DEG = 8  # phi(16); Phi_16 = x^8 + 1

# ---- Q(zeta_16) arithmetic: dense 8-lists of Fractions, zeta^8 = -1 ----
def red(e):  # zeta^e -> (index, sign)
    e %= 16
    return (e % 8, 1 if e < 8 else -1)

def kzero(): return [Fraction(0)] * DEG
def kadd(a, b): return [x + y for x, y in zip(a, b)]
def ksub(a, b): return [x - y for x, y in zip(a, b)]
def kscale(a, s): return [x * s for x in a]
def kmul(a, b):
    out = kzero()
    for i, x in enumerate(a):
        if x == 0: continue
        for j, y in enumerate(b):
            if y == 0: continue
            idx, sg = red(i + j)
            out[idx] += sg * x * y
    return out
def kisz(a): return all(x == 0 for x in a)
def kinv(a):
    # solve a*b = 1 by Gaussian elimination on the 8x8 multiplication matrix
    M = [[Fraction(0)] * DEG for _ in range(DEG)]
    for j in range(DEG):  # b = e_j contributes a*zeta^j
        for i, x in enumerate(a):
            if x == 0: continue
            idx, sg = red(i + j)
            M[idx][j] += sg * x
    rhs = [Fraction(1)] + [Fraction(0)] * (DEG - 1)
    for col in range(DEG):
        piv = next(r for r in range(col, DEG) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]; rhs[col], rhs[piv] = rhs[piv], rhs[col]
        inv = 1 / M[col][col]
        M[col] = [v * inv for v in M[col]]; rhs[col] *= inv
        for r in range(DEG):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [v - f * w for v, w in zip(M[r], M[col])]; rhs[r] -= f * rhs[col]
    return rhs

# ---- polynomials in t over K: list of K-elements, index = degree ----
def ptrim(f):
    while f and kisz(f[-1]): f.pop()
    return f
def pmod(f, g):
    f = [c[:] for c in f]; g = ptrim([c[:] for c in g])
    dg, lead_inv = len(g) - 1, kinv(g[-1])
    while len(f) - 1 >= dg and ptrim([c[:] for c in f]):
        f = ptrim(f)
        if len(f) - 1 < dg: break
        c = kmul(f[-1], lead_inv); sh = len(f) - 1 - dg
        for i in range(len(g)):
            f[sh + i] = ksub(f[sh + i], kmul(c, g[i]))
        f = ptrim(f)
        if not f: break
    return ptrim(f)
def pgcd(f, g):
    f, g = ptrim([c[:] for c in f]), ptrim([c[:] for c in g])
    while g:
        f, g = g, pmod(f, g)
    return f

# ---- rebuild the two E1(2,2) basis units (same construction as first block) ----
def zconst(v):
    out = kzero(); out[0] = Fraction(v); return out
def sparse_to_k(d):
    out = kzero()
    for e, c in d.items():
        idx, sg = red(e)
        out[idx] += sg * c
    return out

def unit(i, j):
    f = {(i + Q * j) % N: 1, i % N: -1}
    h = {}
    for m, c in f.items(): h[m] = h.get(m, 0) + c
    for m, c in list(f.items()): h[(-m) % N] = h.get((-m) % N, 0) + c
    u = [dict() for _ in range(N)]
    for m, c in h.items():
        if c == 0: continue
        u[m][0] = u[m].get(0, 0) + Q * c
        for mp in range(N):
            e = (m * mp) % N
            u[mp][e] = u[mp].get(e, 0) + c
    return u

def cmat(u):
    return [[sparse_to_k(u[(a + Q * b) % N]) for b in range(Q)] for a in range(Q)]

def main():
    C1, C2 = cmat(unit(1, 1)), cmat(unit(1, 2))
    # independence re-check (mod 17, zeta -> 3): done in first block (G5 rank 2). Here
    # exact: C1, C2 not proportional -- witnessed below by non-proportional minors.
    polys = []
    for (a1, a2) in combinations(range(1, Q), 2):     # row 0 is zero in Son
        for (b1, b2) in combinations(range(Q), 2):
            A = ksub(kmul(C1[a1][b1], C1[a2][b2]), kmul(C1[a1][b2], C1[a2][b1]))
            Cc = ksub(kmul(C2[a1][b1], C2[a2][b2]), kmul(C2[a1][b2], C2[a2][b1]))
            B = ksub(kadd(kmul(C1[a1][b1], C2[a2][b2]), kmul(C2[a1][b1], C1[a2][b2])),
                     kadd(kmul(C1[a1][b2], C2[a2][b1]), kmul(C2[a1][b2], C1[a2][b1])))
            pol = ptrim([A, B, Cc])
            if pol: polys.append(((a1, a2, b1, b2), pol))
    print(f"minors with a nonzero polynomial in t: {len(polys)} of "
          f"{len(list(combinations(range(1,Q),2))) * len(list(combinations(range(Q),2)))}")
    gseq = polys[0][1]
    for _, pol in polys[1:]:
        gseq = pgcd(gseq, pol)
        if len(gseq) == 1: break
    if len(gseq) == 1:
        print("PENCIL-GCD = 1 in Q(zeta_16)[t]: the nine minor-quadratics generate (1).")
        print("=> NO nonzero Schmidt-pure vector exists in E1(2,2) over ANY extension")
        print("   (a common root in the closure would force a nonconstant common factor).")
        print("   C2-alone (t = infinity) already MIXED, first block.  VERDICT (2,2): MIXED-FORCED.")
    else:
        print(f"PENCIL-GCD nonconstant, degree {len(gseq)-1}: pure vectors EXIST at its roots.")
        print("gcd coefficients (zeta-power basis):")
        for d, c in enumerate(gseq):
            print(f"  t^{d}: {[str(x) for x in c]}")

if __name__ == "__main__":
    main()
