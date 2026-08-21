#!/usr/bin/env python3
"""
b48 -- THE ARRIVAL-DEPTH ALIGNMENT CHECK (Consolidated Triggers Act, component 1).
Re-runs b45's weight-1 KL class with per-operator resolution (the registered deviation),
then tests the registered statistics S1/S2/S3 and sub-question (i), exactly.
Registration: data/b48_registration_2026-08-20.txt (banked BEFORE this run).
Usage: python b48_depth_alignment.py register | run
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b45_kl_distance import (units_and_basis, cadd, cneg, cconj, cmul, is_zero,
                             phi_reduce, BANKED_D1)

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "..", "data", "b48_registration_2026-08-20.txt")

CELLS = [(2, 2), (5, 1), (2, 3), (3, 2)]
B45_TOTALS = {(2, 2): 25, (5, 1): 41, (2, 3): 113, (3, 2): 145}

def vp(a, p):
    if a == 0:
        return 10**9  # the ball class: depth-maximal
    v = 0
    while a % p == 0:
        a //= p; v += 1
    return v

def run_cell(p, n, out):
    q = p ** n; N = q * q; d1 = BANKED_D1[(p, n)]
    qq, NN, ell, g, B = units_and_basis(p, n)
    assert len(B) == d1
    def coeff(u, a, b): return u[(a + q * b) % N]
    G = [[None] * d1 for _ in range(d1)]
    for r in range(d1):
        for s in range(d1):
            acc = {}
            for m in range(N):
                acc = cadd(acc, cmul(cconj(B[r][m], N), B[s][m], N))
            G[r][s] = acc
    def kl_pass(X):
        for r in range(d1):
            for s in range(d1):
                lhs = cmul(X[r][s], G[0][0], N)
                rhs = cmul(G[r][s], X[0][0], N)
                if not is_zero(cadd(lhs, cneg(rhs)), p, N):
                    return False
        return True
    def X_of(factor, i, j):
        X = [[None] * d1 for _ in range(d1)]
        for r in range(d1):
            for s in range(d1):
                acc = {}
                for t in range(q):
                    if factor == 1:
                        acc = cadd(acc, cmul(cconj(coeff(B[r], i, t), N),
                                             coeff(B[s], j, t), N))
                    else:
                        acc = cadd(acc, cmul(cconj(coeff(B[r], t, i), N),
                                             coeff(B[s], t, j), N))
                X[r][s] = acc
        return X

    table = {1: {}, 2: {}}
    for factor in (1, 2):
        for i in range(q):
            for j in range(q):
                table[factor][(i, j)] = kl_pass(X_of(factor, i, j))
    f1_fail = sum(1 for v in table[1].values() if not v)
    f2_fail = sum(1 for v in table[2].values() if not v)
    total = f1_fail + f2_fail
    out.append(f"\nCELL ({p},{n})  q = {q}  d_1 = {d1}")
    out.append(f"  re-run totals: factor-1 fails {f1_fail}, factor-2 fails {f2_fail}, "
               f"total {total}  (b45 banked total {B45_TOTALS[(p,n)]})"
               + ("  REPRODUCED" if total == B45_TOTALS[(p, n)] else "  VOID: MISMATCH"))
    if total != B45_TOTALS[(p, n)]:
        return None
    # S1: position passes exactly {i=0 or j=0}; frequency passes none
    s1_pos = all(table[1][(i, j)] == (i == 0 or j == 0)
                 for i in range(q) for j in range(q))
    s1_frq = all(not v for v in table[2].values())
    out.append(f"  S1 position half (pass iff i=0 or j=0): {'HOLDS EXACTLY' if s1_pos else 'FAILS'}"
               f"  -> fails (q-1)^2 = {(q-1)**2}")
    out.append(f"  S1 frequency half (no passes): {'HOLDS EXACTLY' if s1_frq else 'FAILS'}"
               f"  -> fails q^2 = {q**2}")
    # sub-question (i): the first-fail witness in canonical order, and its shell
    first = next(((f, i, j) for f in (1, 2) for i in range(q) for j in range(q)
                  if not table[f][(i, j)]))
    out.append(f"  (i) first witness in canonical order: E_{{{first[1]},{first[2]}}} on factor "
               f"{first[0]}; index a = {first[1]}: v_p = {vp(first[1], p)} "
               f"({'DEPTH-MINIMAL (unit shell)' if vp(first[1], p) == 0 else 'not minimal'}); "
               f"off-ball: {first[1] != 0}")
    # S3: any shell distinction among off-ball position passes? (S1 says none exist)
    offball_passes = [(i, j) for i in range(1, q) for j in range(1, q) if table[1][(i, j)]]
    out.append(f"  S3 off-ball position passes: {len(offball_passes)} "
               f"(S1 predicts 0; shell refinement {'ABSENT as predicted' if not offball_passes else 'PRESENT: ' + str(offball_passes[:6])})")
    return {"cell": (p, n), "s1": s1_pos and s1_frq, "first": first,
            "f1_fail": f1_fail, "f2_fail": f2_fail}

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("register", "run"):
        print(__doc__); return
    if sys.argv[1] == "register":
        print(open(REG, encoding="utf-8", errors="replace").read()); return
    out = ["### REGISTRATION CLOSED (data/b48_registration_2026-08-20.txt, banked before this run).",
           "### MEASUREMENT BEGINS. Exact Z[zeta]; the registered deviation: the weight-1 class",
           "### re-run with per-operator resolution; totals must reproduce b45's bank or VOID."]
    res = [run_cell(p, n, out) for (p, n) in CELLS]
    # S2: failure totals vs d_1 across cells (affine fit test, exact integers)
    if all(res):
        cells = [(r["f1_fail"] + r["f2_fail"], BANKED_D1[r["cell"]]) for r in res]
        # test: is total affine in d_1? solve on two cells, test the rest
        (t1, d1a), (t2, d2a) = cells[0], cells[1]
        s2 = None
        if d2a != d1a:
            num, den = (t2 - t1), (d2a - d1a)
            s2 = all((t - t1) * den == num * (d - d1a) for (t, d) in cells)
        out.append(f"\nS2 (failure total affine in d_1 across the four cells): "
                   f"{'HOLDS (unexpectedly)' if s2 else 'FAILS -- as registered/expected; totals are (q-1)^2 + q^2, a q-statistic not a d_1-statistic'}")
    print("\n".join(out))
    return res

if __name__ == "__main__":
    main()
