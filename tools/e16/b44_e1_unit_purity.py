#!/usr/bin/env python3
"""
b44 -- THE PURITY CHECK AT THE BANKED CELLS (ferry 2026-08-19).
Exact Z[zeta_N] arithmetic throughout; no floating point anywhere.
Registration: data/b44_registration_2026-08-19.txt (banked BEFORE this run).
Usage: python b44_e1_unit_purity.py register | run
"""
import sys, os
from fractions import Fraction
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "..", "data", "b44_registration_2026-08-19.txt")

CELLS = [(2, 1), (3, 1), (2, 2), (5, 1), (2, 3), (3, 2)]
BANKED_D1 = {(2, 1): 0, (3, 1): 1, (2, 2): 2, (5, 1): 4, (2, 3): 12, (3, 2): 16}

# ---------- cyclotomic layer: Z[zeta_N], N = p^(2n), elements as sparse dicts e->c ----------

def phi_reduce(d, p, N):
    """reduce a sparse Z[x]/(x^N-1) element mod Phi_N (N = p^k) to the power basis
    x^e, e = c*(N/p)+r with c in 0..p-2: returns dense list length N - N/p."""
    Np = N // p
    out = [0] * (N - Np)
    for e, c0 in d.items():
        if c0 == 0:
            continue
        e %= N
        c, r = divmod(e, Np)
        if c <= p - 2:
            out[e] += c0
        else:  # c == p-1: x^e = -sum_{i=0}^{p-2} x^{i*Np + r}
            for i in range(p - 1):
                out[i * Np + r] -= c0
    return out

def is_zero(d, p, N):
    return all(c == 0 for c in phi_reduce(d, p, N))

def cadd(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c != 0}

def cneg(a):
    return {e: -c for e, c in a.items()}

def cscale(a, k):
    return {e: k * c for e, c in a.items()} if k != 0 else {}

def cmul(a, b, N):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = (e1 + e2) % N
            out[e] = out.get(e, 0) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}

def minor2(C, a1, a2, b1, b2, N):
    """C[a][b] sparse cyclotomic entries; the 2x2 minor as a sparse element."""
    t1 = cmul(C[a1][b1], C[a2][b2], N)
    t2 = cmul(C[a1][b2], C[a2][b1], N)
    return cadd(t1, cneg(t2))

# ---------- hom to F_ell: zeta -> g of exact order N (mixedness certificates) ----------

def find_ell_g(N):
    ell = N + 1
    while True:
        if ell % N == 1 and all(ell % r for r in range(2, int(ell ** 0.5) + 1)):
            for cand in range(2, ell):
                g = pow(cand, (ell - 1) // N, ell)
                ok = g != 1
                if ok:
                    # exact order N check (N = p^(2n): enough to rule out order N/p)
                    if pow(g, N, ell) == 1 and pow(g, N // min(
                            f for f in range(2, N + 1) if N % f == 0), ell) != 1:
                        return ell, g
        ell += N

def hom(d, ell, g, N):
    return sum(c * pow(g, e % N, ell) for e, c in d.items()) % ell

def rank_mod(rows, ell):
    rows = [r[:] for r in rows]
    rank, ncols = 0, (len(rows[0]) if rows else 0)
    for col in range(ncols):
        piv = next((i for i in range(rank, len(rows)) if rows[i][col] % ell), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = pow(rows[rank][col], -1, ell)
        rows[rank] = [(x * inv) % ell for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col] % ell:
                f = rows[i][col]
                rows[i] = [(x - f * y) % ell for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank

# ---------- the model at a cell ----------

def run_cell(p, n, out):
    q = p ** n
    N = q * q
    ell, g = find_ell_g(N)
    out.append(f"\nCELL ({p},{n})  N = {N}  q = {q}  dim Son = {(q-1)**2}  "
               f"banked d_1 = {BANKED_D1[(p,n)]}  [ell = {ell}, g = {g}]")

    # G1: geometric-sum identity => S^2 = q^2 Pi exactly on the whole space
    for t in range(1, N):
        s = {}
        for m in range(N):
            e = (m * t) % N
            s[e] = s.get(e, 0) + 1
        if not is_zero(s, p, N):
            out.append(f"  VOID G1: geometric sum nonzero at t = {t}")
            return None
    out.append(f"  PASS G1  sum_m zeta^(mt) = 0 for t = 1..{N-1} exactly (=> S^2 = q^2 Pi; M^2 = Pi)")
    # G2: Pi involution (permutation m -> -m)
    assert all((-(-m % N)) % N == m for m in range(N))
    out.append("  PASS G2  Pi is the involutive permutation m -> -m (no sign)")

    # Son basis f_{i,j} = e_i (x) (e_j - e_0), i,j in 1..q-1, as integer dicts m -> c
    idx = [(i, j) for i in range(1, q) for j in range(1, q)]
    def f_vec(i, j):
        v = {}
        v[(i + q * j) % N] = v.get((i + q * j) % N, 0) + 1
        v[i % N] = v.get(i % N, 0) - 1
        return v

    def pi_vec(v):
        return {(-m) % N: c for m, c in v.items()}

    # u = q(1+Pi)f + S(1+Pi)f : list of N sparse cyclotomic entries
    units = {}
    for (i, j) in idx:
        f = f_vec(i, j)
        h = cadd(f, pi_vec(f))          # integer dict
        u = [dict() for _ in range(N)]
        for m, c in h.items():
            u[m][0] = u[m].get(0, 0) + q * c          # q*(1+Pi)f, constant coeff
            for mp in range(N):
                e = (m * mp) % N
                u[mp][e] = u[mp].get(e, 0) + c        # S(1+Pi)f
        units[(i, j)] = [{e: c for e, c in ent.items() if c != 0} for ent in u]

    # G3: Son membership of every u: ball rows zero and row sums zero
    for (i, j), u in units.items():
        for b in range(q):
            if not is_zero(u[(q * b) % N], p, N):
                out.append(f"  VOID G3: u_({i},{j}) nonzero on ball at b = {b}")
                return None
        for a in range(1, q):
            rs = {}
            for b in range(q):
                rs = cadd(rs, u[(a + q * b) % N])
            if not is_zero(rs, p, N):
                out.append(f"  VOID G3: u_({i},{j}) row {a} sum nonzero")
                return None
    out.append("  PASS G3  every u vanishes on the ball and has zero row sums (Son membership)")
    # G3 spot-check: S u = q u directly on the first nonzero u
    for (i, j), u in units.items():
        if any(u):
            Su = [dict() for _ in range(N)]
            for m in range(N):
                for e, c in u[m].items():
                    for mp in range(N):
                        ee = (e + m * mp) % N
                        Su[mp][ee] = Su[mp].get(ee, 0) + c
            ok = all(is_zero(cadd(Su[m], cscale(u[m], -q)), p, N) for m in range(N))
            out.append(f"  {'PASS' if ok else 'VOID'} G3' spot-check S u = q u at u_({i},{j})")
            if not ok:
                return None
            break

    # G4: projector trace = 4 q d_1 exactly
    tr = {}
    for (i, j) in idx:
        tr = cadd(tr, units[(i, j)][(i + q * j) % N])
    target = {0: 4 * q * BANKED_D1[(p, n)]}
    if not is_zero(cadd(tr, cneg(target)), p, N):
        out.append(f"  VOID G4: tr(4q P1) != 4 q d_1;  reduced tr = {phi_reduce(tr, p, N)}")
        return None
    out.append(f"  PASS G4  tr(4q P1) = {4*q*BANKED_D1[(p,n)]} = 4 q d_1 exactly -- banked d_1 re-derived")

    # G5: span rank mod ell = d_1
    rows = [[hom(u[m], ell, g, N) for m in range(N)] for u in units.values()]
    r = rank_mod(rows, ell)
    if r != BANKED_D1[(p, n)]:
        out.append(f"  VOID G5: span rank mod {ell} = {r} != banked d_1")
        return None
    out.append(f"  PASS G5  span rank mod {ell} = {r} = d_1  (with G4: span = E1 exactly)")

    if BANKED_D1[(p, n)] == 0:
        # (2,1): no unit; the ferry's no-weight minor test on the Sonin generator
        f = f_vec(1, 1) if (p, n) == (2, 1) else None
        C = [[{q * 0: 0} for _ in range(q)] for _ in range(q)]
        pure = True
        for (a1, a2) in combinations(range(q), 2):
            for (b1, b2) in combinations(range(q), 2):
                fm = lambda a, b: {0: f.get((a + q * b) % N, 0)}
                mnr = cadd(cmul(fm(a1, b1), fm(a2, b2), N),
                           cneg(cmul(fm(a1, b2), fm(a2, b1), N)))
                if not is_zero(mnr, p, N):
                    pure = False
        out.append(f"  VERDICT ({p},{n}): NO-UNIT (d_1 = 0, exact: (1+Pi)f = 0 -> projector image 0)."
                   f"  Sonin-generator minor test: {'all 2x2 minors vanish (rank 1, pure by shape)' if pure else 'MIXED'}"
                   f" -- registered no-weight.")
        return {"cell": (p, n), "verdict": "NO-UNIT", "detail": "pure-by-shape, no-weight"}

    # purity per spanning unit
    def coeff_matrix(u):
        return [[u[(a + q * b) % N] for b in range(q)] for a in range(q)]

    results = {}
    pure_units, mixed_units = [], []
    for (i, j), u in units.items():
        if not any(u):
            continue
        C = coeff_matrix(u)
        Cl = [[hom(C[a][b], ell, g, N) for b in range(q)] for a in range(q)]
        witness = None
        for (a1, a2) in combinations(range(q), 2):
            for (b1, b2) in combinations(range(q), 2):
                if (Cl[a1][b1] * Cl[a2][b2] - Cl[a1][b2] * Cl[a2][b1]) % ell:
                    witness = (a1, a2, b1, b2)
                    break
            if witness:
                break
        if witness:
            a1, a2, b1, b2 = witness
            mnr = minor2(C, a1, a2, b1, b2, N)
            red = phi_reduce(mnr, p, N)
            assert any(red), "hom-nonzero but exact zero: impossible"
            mixed_units.append((i, j))
            results[(i, j)] = ("MIXED", witness, red)
        else:
            # exact full check
            allzero, nz = True, None
            for (a1, a2) in combinations(range(q), 2):
                for (b1, b2) in combinations(range(q), 2):
                    mnr = minor2(C, a1, a2, b1, b2, N)
                    if not is_zero(mnr, p, N):
                        allzero, nz = False, (a1, a2, b1, b2, phi_reduce(mnr, p, N))
                        break
                if not allzero:
                    break
            if allzero:
                pure_units.append((i, j))
                results[(i, j)] = ("PURE", None, None)
            else:
                mixed_units.append((i, j))
                results[(i, j)] = ("MIXED", nz[:4], nz[4])
    nP, nM = len(pure_units), len(mixed_units)
    out.append(f"  spanning set: {nP + nM} nonzero projector images; PURE {nP}, MIXED {nM}")
    for key in sorted(results):
        v = results[key]
        if v[0] == "MIXED":
            out.append(f"    u_{key}: MIXED  witness minor rows {v[1][0]},{v[1][1]} cols {v[1][2]},{v[1][3]}"
                       f"  reduced != 0 (nonzero coeffs: {sum(1 for c in v[2] if c)})")
        else:
            out.append(f"    u_{key}: PURE  (all {len(list(combinations(range(q),2)))**2} 2x2 minors vanish in Z[zeta])")
    return {"cell": (p, n), "results": results, "units": units, "idx": idx,
            "q": q, "N": N, "ell": ell, "g": g, "d1": BANKED_D1[(p, n)],
            "pure": pure_units, "mixed": mixed_units, "out": out}

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("register", "run"):
        print(__doc__)
        return
    if sys.argv[1] == "register":
        print(open(REG, encoding="utf-8", errors="replace").read())
        return
    out = ["### REGISTRATION CLOSED (data/b44_registration_2026-08-19.txt, banked before this run).",
           "### MEASUREMENT BEGINS. Exact Z[zeta] arithmetic; mod-ell used only as a",
           "### nonzero-certificate direction (ring hom), never for vanishing."]
    summaries = []
    for (p, n) in CELLS:
        res = run_cell(p, n, out)
        if res is None:
            out.append(f"  CELL ({p},{n}): VOID -- gate failure; run stops per registration.")
            break
        summaries.append(res)
    print("\n".join(out))
    return summaries

if __name__ == "__main__":
    main()
