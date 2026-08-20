#!/usr/bin/env python3
"""
b45 -- THE KNILL-LAFLAMME DISTANCE CHECK AT THE BANKED CELLS (Protection Act, Component B).
Exact Z[zeta_N] arithmetic; conjugation zeta -> zeta^{-1}; no floating point anywhere.
Registration: data/b45_registration_2026-08-20.txt (banked BEFORE this run).
Usage: python b45_kl_distance.py register | run
"""
import sys, os
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "..", "data", "b45_registration_2026-08-20.txt")

CELLS = [(3, 1), (2, 2), (5, 1), (2, 3), (3, 2)]
BANKED_D1 = {(3, 1): 1, (2, 2): 2, (5, 1): 4, (2, 3): 12, (3, 2): 16}

# ---- cyclotomic layer (b44's, plus conjugation) ----
def phi_reduce(d, p, N):
    Np = N // p
    out = [0] * (N - Np)
    for e, c0 in d.items():
        if c0 == 0: continue
        e %= N
        c, r = divmod(e, Np)
        if c <= p - 2: out[e] += c0
        else:
            for i in range(p - 1): out[i * Np + r] -= c0
    return out

def is_zero(d, p, N): return all(c == 0 for c in phi_reduce(d, p, N))
def cadd(a, b):
    out = dict(a)
    for e, c in b.items(): out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c != 0}
def cneg(a): return {e: -c for e, c in a.items()}
def cconj(a, N): return {(-e) % N: c for e, c in a.items()}
def cmul(a, b, N):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = (e1 + e2) % N
            out[e] = out.get(e, 0) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}

def find_ell_g(N):
    ell = N + 1
    while True:
        if ell % N == 1 and all(ell % r for r in range(2, int(ell ** 0.5) + 1)):
            for cand in range(2, ell):
                g = pow(cand, (ell - 1) // N, ell)
                if g != 1 and pow(g, N, ell) == 1:
                    if all(pow(g, N // f, ell) != 1 for f in set(
                            x for x in range(2, N + 1) if N % x == 0 and
                            all(x % y for y in range(2, int(x**0.5)+1)))):
                        return ell, g
        ell += N

def hom(d, ell, g, N): return sum(c * pow(g, e % N, ell) for e, c in d.items()) % ell

def units_and_basis(p, n):
    """b44's projector images + a mod-ell-certified independent subset of size d_1."""
    q = p ** n; N = q * q
    ell, g = find_ell_g(N)
    idx = [(i, j) for i in range(1, q) for j in range(1, q)]
    units = []
    for (i, j) in idx:
        f = {(i + q * j) % N: 1, i % N: -1}
        h = {}
        for m, c in f.items(): h[m] = h.get(m, 0) + c
        for m, c in list(f.items()): h[(-m) % N] = h.get((-m) % N, 0) + c
        u = [dict() for _ in range(N)]
        for m, c in h.items():
            if c == 0: continue
            u[m][0] = u[m].get(0, 0) + q * c
            for mp in range(N):
                e = (m * mp) % N
                u[mp][e] = u[mp].get(e, 0) + c
        units.append([{e: c for e, c in ent.items() if c != 0} for ent in u])
    # greedy independent subset mod ell
    basis, rows = [], []
    for u in units:
        row = [hom(x, ell, g, N) for x in u]
        cur = row[:]
        for r in rows:
            pos = next(k for k in range(N) if r[k])
            if cur[pos]:
                f = (cur[pos] * pow(r[pos], -1, ell)) % ell
                cur = [(a - f * b) % ell for a, b in zip(cur, r)]
        if any(cur):
            piv = next(k for k in range(N) if cur[k])
            inv = pow(cur[piv], -1, ell)
            rows.append([(x * inv) % ell for x in cur])
            basis.append(u)
        if len(basis) == BANKED_D1[(p, n)]: break
    return q, N, ell, g, basis

def run_cell(p, n, out):
    q = p ** n; N = q * q
    d1 = BANKED_D1[(p, n)]
    # chart bijectivity + factor dims (the (a,a) verification)
    chart = sorted((a + q * b) % N for a in range(q) for b in range(q))
    assert chart == list(range(N)), "chart not bijective"
    out.append(f"\nCELL ({p},{n})  N = {N}  q = {q}  d_1 = {d1}")
    out.append(f"  PASS chart bijective Z/{q} x Z/{q} -> Z/{N}; ambient factor dims ({q},{q}); "
               f"Sonin block ({q-1},{q-1}) (a=0 row zero) -- the (a,a) square reading verified")
    qq, NN, ell, g, B = units_and_basis(p, n)
    if len(B) != d1:
        out.append(f"  VOID: independent subset size {len(B)} != d_1")
        return None
    out.append(f"  basis: {d1} projector images, independence certified mod {ell}")

    def coeff(u, a, b): return u[(a + q * b) % N]
    # Gram
    G = [[None] * d1 for _ in range(d1)]
    for r in range(d1):
        for s in range(d1):
            acc = {}
            for m in range(N):
                acc = cadd(acc, cmul(cconj(B[r][m], N), B[s][m], N))
            G[r][s] = acc
    if is_zero(G[0][0], p, N):
        out.append("  VOID: G[0][0] = 0")
        return None
    out.append("  PASS G[0][0] != 0 (exact)")

    def kl_ok(X):
        """X = c G for some scalar c, decided by cross-multiplication in Z[zeta]."""
        for r in range(d1):
            for s in range(d1):
                lhs = cmul(X[r][s], G[0][0], N)
                rhs = cmul(G[r][s], X[0][0], N)
                if not is_zero(cadd(lhs, cneg(rhs)), p, N):
                    return (r, s)
        return None

    def X_of(factor, i, j):
        X = [[None] * d1 for _ in range(d1)]
        for r in range(d1):
            for s in range(d1):
                acc = {}
                for t in range(q):
                    if factor == 1:  # E_ij (x) 1 : (a,b)=(i,t)<- (j,t)
                        acc = cadd(acc, cmul(cconj(coeff(B[r], i, t), N),
                                             coeff(B[s], j, t), N))
                    else:            # 1 (x) E_ij : (a,b)=(t,i)<- (t,j)
                        acc = cadd(acc, cmul(cconj(coeff(B[r], t, i), N),
                                             coeff(B[s], t, j), N))
                X[r][s] = acc
        return X

    if d1 == 1:
        out.append("  TIER 1: VACUOUS PASS (d_1 = 1: any 1x1 X is proportional to G != 0; "
                   "a dim-1 code space carries no logical information -- counted for nothing, "
                   "per the registration's vacuity note)")
        return {"cell": (p, n), "tier1": "VACUOUS", "tier2": "VACUOUS"}

    # TIER 1: all weight-1 matrix units, both factors
    fails = []
    checked = 0
    for factor in (1, 2):
        for i in range(q):
            for j in range(q):
                X = X_of(factor, i, j)
                w = kl_ok(X)
                checked += 1
                if w is not None:
                    fails.append((factor, i, j, w))
    if not fails:
        out.append(f"  TIER 1: PASS -- all {checked} weight-1 basis operators satisfy "
                   f"P E P = c(E) G exactly (both factors, all matrix units): DISTANCE >= 2")
    else:
        f0 = fails[0]
        out.append(f"  TIER 1: FAIL at {len(fails)}/{checked} operators; first witness: "
                   f"E_{{{f0[1]},{f0[2]}}} on factor {f0[0]}, condition breaks at Gram "
                   f"entry ({f0[3][0]},{f0[3][1]}) -- exact nonzero discrepancy in Z[zeta_{N}]")
        for f in fails[1:6]:
            out.append(f"    also: E_{{{f[1]},{f[2]}}} factor {f[0]} at ({f[3][0]},{f[3][1]})")
        if len(fails) > 6:
            out.append(f"    ... {len(fails) - 6} more (bank holds the count per factor)")

    # TIER 2 as registered: same-factor pairs E+F -- run directly (content, not expectation)
    pair_fails = []
    pchecked = 0
    for factor in (1, 2):
        for (i, j) in [(i, j) for i in range(q) for j in range(q)]:
            for (k, l) in [(k, l) for k in range(q) for l in range(q)]:
                # E = E_ij, F = E_kl on the same factor: E+F = delta_ik E_jl
                pchecked += 1
                if i == k:
                    X = X_of(factor, j, l)
                    if kl_ok(X) is not None:
                        pair_fails.append((factor, (i, j), (k, l)))
                # i != k -> E+F = 0: condition holds with c = 0, nothing to check
        if pchecked and factor == 1 and q >= 8:
            pass  # full enumeration kept; loop is cheap since X_of reuses Tier-1 shapes
    if not pair_fails:
        out.append(f"  TIER 2 (as registered, same-factor pairs): PASS -- {pchecked} pairs; "
                   f"nonzero products reduce to the Tier-1 class (E_ij+ E_kl = delta_ik E_jl, "
                   f"verified structurally in the reduction used), zero products vacuous. "
                   f"AS REGISTERED, THIS IS IMPLIED BY TIER 1 -- stated, not smoothed.")
    else:
        out.append(f"  TIER 2: FAIL at {len(pair_fails)} pairs; first: {pair_fails[0]}")
    return {"cell": (p, n), "tier1": "PASS" if not fails else ("FAIL", fails),
            "tier2": "PASS" if not pair_fails else ("FAIL", pair_fails)}

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("register", "run"):
        print(__doc__); return
    if sys.argv[1] == "register":
        print(open(REG, encoding="utf-8", errors="replace").read()); return
    out = ["### REGISTRATION CLOSED (data/b45_registration_2026-08-20.txt, banked before this run).",
           "### MEASUREMENT BEGINS. Exact Z[zeta]; conjugation zeta -> zeta^{-1}; verdicts never mod-ell."]
    res = []
    for (p, n) in CELLS:
        r = run_cell(p, n, out)
        res.append(r)
    print("\n".join(out))
    return res

if __name__ == "__main__":
    main()
