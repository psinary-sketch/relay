# b101 -- THE MONOTONICITY ACT -- instrument: the four decidable checks K1-K4
# cross-checked numerically before the Lean decides, at the banked truncation
# pairs. Registration: data/b101_registration_2026-08-22.txt (the chain fixed
# there BEFORE this ran). Also: a DIRECT end-to-end test of the inclusion on an
# explicit spanning set at the smallest pair, as an independent confirmation
# that the index chain models the real Sonin condition and not a caricature.

import cmath, itertools

PAIRS = [(2, 1), (2, 2), (3, 1)]   # (p, n): the pair is level n -> level n+1
TOL = 1e-9
fails = []

for p, n in PAIRS:
    Nn = p ** (2 * n)
    Nn1 = p ** (2 * n + 2)
    bn = p ** n           # ball modulus at level n
    bn1 = p ** (n + 1)    # ball modulus at level n+1
    step = p ** (2 * n + 1)

    # K1 support side: (p*m + step*j) % bn1 == 0  <->  m % bn == 0
    for m in range(Nn):
        for j in range(p):
            idx = (p * m + step * j) % Nn1
            lhs = (idx % bn1 == 0)
            rhs = (m % bn == 0)
            if lhs != rhs:
                fails.append(("K1", p, n, m, j, lhs, rhs))

    # K2 inner-sum rule: for r in B_{n+1}, r*step % Nn1 == 0 (every j-term is 1)
    for r in range(0, Nn1, bn1):
        if (r * step) % Nn1 != 0:
            fails.append(("K2", p, n, r))

    # K3 transform index shift: (r*p*m) % Nn1 == p**2 * (((r//p)*m) % Nn)
    # (the scale factor is p**2, not p: r*p*m / Nn1 == (r/p)*m / Nn as fractions,
    #  and Nn1 = p**2 * Nn -- the b101 registration's "i.e." line said p and was
    #  CORRECTED here by this instrument before any Lean was written.)
    for r in range(0, Nn1, bn1):
        for m in range(Nn):
            lhs = (r * p * m) % Nn1
            rhs = (p ** 2) * (((r // p) * m) % Nn)
            if lhs != rhs:
                fails.append(("K3", p, n, r, m, lhs, rhs))

    # K4 quotient in ball: for r in B_{n+1}, (r//p) % bn == 0
    for r in range(0, Nn1, bn1):
        if (r // p) % bn != 0:
            fails.append(("K4", p, n, r))

# --- the independent end-to-end test at the smallest pair (2,1) -> (2,2) ---
# Son(2,1): v on Z/4 vanishing on B_1 = {0,2}, with (F v)(r) = 0 for r in {0,2}.
# Then check iota(v) satisfies the level-2 conditions on Z/16 with B_2 = {0,4,8,12}.
def son_basis(p, n):
    N = p ** (2 * n)
    ball = [m for m in range(N) if m % (p ** n) == 0]
    z = cmath.exp(2j * cmath.pi / N)
    # brute-force a spanning set over the "support-allowed" coordinates:
    # v is supported off the ball; impose (F v)(r) = 0 for r in ball.
    free = [m for m in range(N) if m % (p ** n) != 0]
    # the transform conditions are |ball| linear equations on |free| unknowns;
    # solve by taking the nullspace numerically over the complex field.
    import numpy as np
    A = np.array([[z ** (r * m) for m in free] for r in ball], dtype=complex)
    u, s, vh = np.linalg.svd(A)
    rank = int((s > 1e-9).sum())
    ns = vh[rank:].conj().T          # nullspace basis, columns
    vecs = []
    for k in range(ns.shape[1]):
        v = [0j] * N
        for i, m in enumerate(free):
            v[m] = ns[i, k]
        vecs.append(v)
    return vecs, ball, N

def transform(v, N):
    z = cmath.exp(2j * cmath.pi / N)
    return [sum(v[m] * z ** (r * m) for m in range(N)) for r in range(N)]

try:
    import numpy as np
    p, n = 2, 1
    vecs, ball1, N1 = son_basis(p, n)
    N2 = p ** (2 * n + 2)
    ball2 = [r for r in range(N2) if r % (p ** (n + 1)) == 0]
    step = p ** (2 * n + 1)
    dim_expected = (p ** n - 1) ** 2
    if len(vecs) != dim_expected:
        fails.append(("DIM", p, n, len(vecs), dim_expected))
    for v in vecs:
        iv = [0j] * N2
        for m in range(N1):
            for j in range(p):
                iv[(p * m + step * j) % N2] += v[m]
        for r in ball2:
            if abs(iv[r]) > TOL:
                fails.append(("E2E-support", r))
        Fiv = transform(iv, N2)
        for r in ball2:
            if abs(Fiv[r]) > TOL:
                fails.append(("E2E-transform", r, Fiv[r]))
    e2e = f"end-to-end at (2,1)->(2,2): {len(vecs)} basis vector(s) (dim {dim_expected}), all conditions hold"
except ImportError:
    e2e = "end-to-end test SKIPPED (numpy unavailable) -- K1-K4 stand alone"

if fails:
    print("FAIL:", len(fails))
    for f in fails[:20]:
        print(f)
else:
    print("K1 (support side: image index in the ball iff m in the ball): PASS")
    print("K2 (inner-sum rule: every j-term is 1 on ball rows): PASS")
    print("K3 (transform index shift under the scale map): PASS")
    print("K4 (r/p lands in the level-n ball): PASS")
    print(e2e)
    print("ALL CHECKS PASS -- THE INCLUSION HOLDS at the banked pairs")
