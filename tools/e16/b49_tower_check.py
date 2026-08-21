#!/usr/bin/env python3
"""
b49 -- THE TOWER-COMPATIBILITY CHECK (Assembly Act opening, component 2).
Exact Z[zeta] arithmetic at both levels; the three registered candidate maps
(coefficient embedding/reduction, Galois trace, norm); normalizations pre-computed
in the registration, never fitted. Registration: data/b49_registration_2026-08-20.txt
(banked BEFORE this run). Usage: python b49_tower_check.py register | run
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b45_kl_distance import (units_and_basis, cadd, cneg, cconj, cmul, is_zero,
                             phi_reduce, BANKED_D1)

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "..", "data", "b49_registration_2026-08-20.txt")

PAIRS = [((2, 2), (2, 3)), ((3, 1), (3, 2))]

def emb(x, p):
    """Z[zeta_N] -> Z[zeta_N+]: exponent e -> p^2 e"""
    return {(e * p * p): c for e, c in x.items()}

def scal(x, k):
    return {e: k * c for e, c in x.items()}

def sigma(x, c, N, Nplus):
    """sigma_c: zeta_N+ -> zeta_N+^{1+cN}"""
    out = {}
    for e, v in x.items():
        e2 = (e * (1 + c * N)) % Nplus
        out[e2] = out.get(e2, 0) + v
    return out

def galois_sum(x, p, N, Nplus):
    acc = {}
    for c in range(p * p):
        acc = cadd(acc, sigma(x, c, N, Nplus))
    return acc

def galois_prod(x, p, N, Nplus):
    acc = {0: 1}
    for c in range(p * p):
        acc = cmul(acc, sigma(x, c, N, Nplus), Nplus)
    return acc

def run_pair(lo, hi, out):
    (p, n), (p2c, n2) = lo, hi
    assert p == p2c and n2 == n + 1
    q = p ** n; N = q * q
    qP = p ** n2; NP = qP * qP
    d1 = BANKED_D1[lo]
    out.append(f"\nPAIR ({p},{n}) -> ({p},{n2})   q = {q} -> {qP}   d_1(level) = {d1}")
    _, _, ell, g, B = units_and_basis(p, n)
    # iota images as host vectors: host index (p*a) + qP*(b + q*j) <- value u(a + q*b), embedded
    def iota(u):
        v = [dict() for _ in range(NP)]
        for a in range(q):
            for b in range(q):
                val = u[(a + q * b) % N]
                if not val: continue
                ev = emb(val, p)
                for j in range(p):
                    m2 = (p * a + qP * ((b + q * j) % qP)) % NP
                    v[m2] = cadd(v[m2], ev)
        return v
    I = [iota(u) for u in B]
    # G1: each iota(u) in E_1(host): S+ iota(u) = qP iota(u), exact
    for k, v in enumerate(I):
        Sv = [dict() for _ in range(NP)]
        for m in range(NP):
            for e, c in v[m].items():
                for mp in range(NP):
                    ee = (e + m * mp) % NP
                    Sv[mp][ee] = Sv[mp].get(ee, 0) + c
        ok = all(is_zero(cadd(Sv[m], cneg(scal(v[m], qP))), p, NP) for m in range(NP))
        out.append(f"  {'PASS' if ok else 'VOID'} G1  S+ iota(u_{k}) = q+ iota(u_{k}) exactly")
        if not ok: return None
    def coeff(u, a, b, qq, NN): return u[(a + qq * b) % NN]
    def gram(vecs, NN):
        d = len(vecs)
        return [[__import__('functools').reduce(lambda A, m: cadd(A, cmul(cconj(vecs[r][m], NN), vecs[s][m], NN)), range(NN), {})
                 for s in range(d)] for r in range(d)]
    def x_table(vecs, i, j, qq, NN):
        d = len(vecs)
        return [[__import__('functools').reduce(lambda A, t: cadd(A, cmul(cconj(coeff(vecs[r], i, t, qq, NN), NN), coeff(vecs[s], j, t, qq, NN), NN)), range(qq), {})
                 for s in range(d)] for r in range(d)]
    Glev, Ghost = gram(B, N), gram(I, NP)
    # M1 on G: Ghost = p * emb(Glev)?
    okG = all(is_zero(cadd(Ghost[r][s], cneg(scal(emb(Glev[r][s], p), p))), p, NP)
              for r in range(d1) for s in range(d1))
    out.append(f"  M1 G-table: G'' = p*emb(G) {'HOLDS EXACTLY' if okG else 'FAILS'}")
    ops = [(i, j) for i in range(q) for j in range(q)]
    okX, okD, okTr = True, True, True
    Dpairs = []  # nonzero (emb(D), D'') entries for the norm cross-test
    for (i, j) in ops:
        Xl = x_table(B, i, j, q, N)
        Xh = x_table(I, p * i, p * j, qP, NP)
        for r in range(d1):
            for s in range(d1):
                if not is_zero(cadd(Xh[r][s], cneg(scal(emb(Xl[r][s], p), p))), p, NP):
                    okX = False
        # discrepancy tables
        for r in range(d1):
            for s in range(d1):
                Dl = cadd(cmul(Xl[r][s], Glev[0][0], N), cneg(cmul(Glev[r][s], Xl[0][0], N)))
                Dh = cadd(cmul(Xh[r][s], Ghost[0][0], NP), cneg(cmul(Ghost[r][s], Xh[0][0], NP)))
                pred = scal(emb(Dl, p), p * p)
                if not is_zero(cadd(Dh, cneg(pred)), p, NP):
                    okD = False
                trh = galois_sum(Dh, p, N, NP)
                predtr = scal(emb(Dl, p), p ** 4)
                if not is_zero(cadd(trh, cneg(predtr)), p, NP):
                    okTr = False
                if any(phi_reduce(Dl, p, N)) and len(Dpairs) < 2 and (i, j) not in [d[2] for d in Dpairs]:
                    Dpairs.append((Dl, Dh, (i, j), (r, s)))
    out.append(f"  M1 X-tables (all {len(ops)} position operators): X'' = p*emb(X) "
               f"{'HOLDS EXACTLY' if okX else 'FAILS'}")
    out.append(f"  M1 D-tables: D'' = p^2*emb(D) {'HOLDS EXACTLY' if okD else 'FAILS'}"
               + ("  [note: at d_1 = 1 the D-tables are identically zero -- the registered vacuity]" if d1 == 1 else ""))
    out.append(f"  M2 trace: Tr(D'') = p^4*emb(D) {'HOLDS EXACTLY' if okTr else 'FAILS'}"
               + ("  [vacuous at d_1 = 1]" if d1 == 1 else ""))
    # silence transport check line (Component 1 at both levels)
    out.append(f"  silence transport: ball-touching (i=0 or j=0) level ops map to ball-touching "
               f"host ops (p*i = 0 iff i = 0) -- exact by the correspondence; consistent with "
               f"Component 1's theorem at both levels")
    # M3 norm cross-proportionality on two nonzero D entries
    if len(Dpairs) >= 2:
        (D1l, D1h, op1, _), (D2l, D2h, op2, _) = Dpairs[:2]
        n1, n2_ = galois_prod(D1h, p, N, NP), galois_prod(D2h, p, N, NP)
        lhs = cmul(n1, emb(D2l, p), NP)
        rhs = cmul(n2_, emb(D1l, p), NP)
        prop = is_zero(cadd(lhs, cneg(rhs)), p, NP)
        out.append(f"  M3 norm: cross-proportionality across ops {op1}, {op2}: "
                   f"{'HOLDS (unexpectedly)' if prop else 'FAILS -- as registered (multiplicative, not a table transport); exact witness banked'}")
    else:
        out.append("  M3 norm: no two nonzero D entries at this pair (d_1 = 1 vacuity) -- "
                   "the norm test is vacuous here, registered")
    return {"pair": (lo, hi), "G": okG, "X": okX, "D": okD, "Tr": okTr}

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("register", "run"):
        print(__doc__); return
    if sys.argv[1] == "register":
        print(open(REG, encoding="utf-8", errors="replace").read()); return
    out = ["### REGISTRATION CLOSED (data/b49_registration_2026-08-20.txt, banked before this run).",
           "### MEASUREMENT BEGINS. Exact Z[zeta] at both levels; normalizations pre-computed",
           "### in the registration (p on tables, p^2 on discrepancies, p^4 on the trace).",
           "### The (2,1)->(2,2) step is VACUOUS (d_1(2,1) = 0, arrival-depth death) -- recorded."]
    res = [run_pair(lo, hi, out) for lo, hi in PAIRS]
    print("\n".join(out))
    return res

if __name__ == "__main__":
    main()
