#!/usr/bin/env python3
"""
b46 -- THE SEGRE-INTERSECTION DECISION AT THE d_1 > 2 CELLS (Protection Act, Component C;
work-order W-ORD-SEGRE-D1-GT-2, trigger fired). Exact arithmetic: the quadric system's
Z[zeta_N] coefficients reduced by the ring hom zeta -> g into F_ell; emptiness over
closure(F_ell) certified by Macaulay saturation; emptiness over closure(Q) follows by the
registered specialization/properness argument. Integer arithmetic only.
Registration: data/b46_registration_2026-08-20.txt (banked BEFORE this run).
Usage: python b46_segre.py register | run
"""
import sys, os
from itertools import combinations, combinations_with_replacement

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "..", "data", "b46_registration_2026-08-20.txt")

CELLS = [(5, 1), (2, 3), (3, 2)]
BANKED_D1 = {(5, 1): 4, (2, 3): 12, (3, 2): 16}

def find_ell_g(N, skip=0):
    ell = N + 1; found = 0
    while True:
        if ell % N == 1 and all(ell % r for r in range(2, int(ell ** 0.5) + 1)):
            for cand in range(2, ell):
                g = pow(cand, (ell - 1) // N, ell)
                if g != 1 and pow(g, N, ell) == 1:
                    primes = [x for x in range(2, N + 1) if N % x == 0 and
                              all(x % y for y in range(2, int(x ** 0.5) + 1))]
                    if all(pow(g, N // f, ell) != 1 for f in primes):
                        if found == skip: return ell, g
                        found += 1
                        break
        ell += N

def basis_mod_ell(p, n, ell, g):
    """d_1 independent projector images, reduced to F_ell vectors of length N."""
    q = p ** n; N = q * q
    d1 = BANKED_D1[(p, n)]
    basis, rows = [], []
    for i in range(1, q):
        for j in range(1, q):
            f = {(i + q * j) % N: 1, i % N: -1}
            h = {}
            for m, c in f.items(): h[m] = h.get(m, 0) + c
            for m, c in list(f.items()): h[(-m) % N] = h.get((-m) % N, 0) + c
            u = [0] * N
            for m, c in h.items():
                if c == 0: continue
                u[m] = (u[m] + q * c) % ell
                for mp in range(N):
                    u[mp] = (u[mp] + c * pow(g, (m * mp) % N, ell)) % ell
            cur = u[:]
            for r in rows:
                pos = next(k for k in range(N) if r[k])
                if cur[pos]:
                    fac = (cur[pos] * pow(r[pos], -1, ell)) % ell
                    cur = [(a - fac * b) % ell for a, b in zip(cur, r)]
            if any(cur):
                piv = next(k for k in range(N) if cur[k])
                inv = pow(cur[piv], -1, ell)
                rows.append([(x * inv) % ell for x in cur])
                basis.append(u)
            if len(basis) == d1: return basis
    return basis

def run_cell(p, n, out, skip_ell=0, max_deg=4):
    q = p ** n; N = q * q; d1 = BANKED_D1[(p, n)]
    ell, g = find_ell_g(N, skip=skip_ell)
    B = basis_mod_ell(p, n, ell, g)
    if len(B) != d1:
        out.append(f"  VOID ({p},{n}): basis size {len(B)} != d_1"); return None
    out.append(f"\nCELL ({p},{n})  q = {q}  d_1 = {d1}  [ell = {ell}, g = {g}]  "
               f"codimension bound (q-2)^2 = {(q-2)**2}, margin {(q-2)**2 - d1}")
    # coefficient matrices C_k[a][b] = u_k(a + q b) in F_ell; a in 1..q-1 (row 0 zero)
    C = [[[B[k][(a + q * b) % N] for b in range(q)] for a in range(q)] for k in range(d1)]
    # quadrics: for each minor (rows a1<a2 in 1..q-1, cols b1<b2), coefficients on t_k t_l
    quads = []
    pairs = list(combinations_with_replacement(range(d1), 2))
    for (a1, a2) in combinations(range(1, q), 2):
        for (b1, b2) in combinations(range(q), 2):
            coefs = {}
            for k in range(d1):
                for l in range(d1):
                    v = (C[k][a1][b1] * C[l][a2][b2] - C[k][a1][b2] * C[l][a2][b1]) % ell
                    if v:
                        key = (k, l) if k <= l else (l, k)
                        coefs[key] = (coefs.get(key, 0) + v) % ell
            coefs = {kk: v for kk, v in coefs.items() if v}
            if coefs: quads.append(coefs)
    out.append(f"  quadrics: {len(quads)} nonzero minors of "
               f"{len(list(combinations(range(1,q),2))) * len(list(combinations(range(q),2)))}")
    # Macaulay saturation at degree D = 3 (escalate to 4 if needed)
    for D in range(3, max_deg + 1):
        monsD = list(combinations_with_replacement(range(d1), D))
        midx = {m: i for i, m in enumerate(monsD)}
        pivots = {}   # leading-column -> reduced sparse row (dict col->val, lead normalized 1)
        target = len(monsD)
        rank = 0
        done = False
        mults = list(combinations_with_replacement(range(d1), D - 2))
        for mu in mults:
            for qd in quads:
                row = {}
                for (k, l), v in qd.items():
                    mon = tuple(sorted(mu + (k, l)))
                    c0 = midx[mon]
                    row[c0] = (row.get(c0, 0) + v) % ell
                row = {c: v for c, v in row.items() if v}
                while row:
                    lead = min(row)
                    if lead in pivots:
                        piv = pivots[lead]
                        f0 = row[lead]
                        for c, v in piv.items():
                            row[c] = (row.get(c, 0) - f0 * v) % ell
                        row = {c: v for c, v in row.items() if v}
                    else:
                        inv = pow(row[lead], -1, ell)
                        pivots[lead] = {c: (v * inv) % ell for c, v in row.items()}
                        rank += 1
                        row = None
                if rank == target:
                    done = True; break
            if done: break
        out.append(f"  degree {D}: Macaulay rank {rank} / {target} monomials"
                   + ("  -> SATURATED" if rank == target else "  -> not saturated"))
        if rank == target:
            out.append(f"  VERDICT ({p},{n}): EMPTY -- the degree-{D} piece of the ideal is the "
                       f"full space over F_{ell}; the projective variety is empty over "
                       f"closure(F_{ell}); by the registered specialization argument, EMPTY over "
                       f"closure(Q): E_1({p},{n}) contains NO nonzero Schmidt-pure vector over "
                       f"any field extension. MIXED-FORCED.")
            return {"cell": (p, n), "verdict": "EMPTY", "degree": D, "ell": ell}
    out.append(f"  VERDICT ({p},{n}): INCONCLUSIVE at degrees <= {max_deg} with ell = {ell} "
               f"-- escalation per registration required")
    return {"cell": (p, n), "verdict": "INCONCLUSIVE", "ell": ell}

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("register", "run"):
        print(__doc__); return
    if sys.argv[1] == "register":
        print(open(REG, encoding="utf-8", errors="replace").read()); return
    out = ["### REGISTRATION CLOSED (data/b46_registration_2026-08-20.txt, banked before this run).",
           "### MEASUREMENT BEGINS. F_ell arithmetic in the certificate direction only;",
           "### the emptiness verdict transfers to characteristic 0 by the registered",
           "### specialization/properness argument (stated longhand in the registration)."]
    res = []
    for (p, n) in CELLS:
        res.append(run_cell(p, n, out))
    print("\n".join(out))
    return res

if __name__ == "__main__":
    main()
