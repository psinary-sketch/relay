#!/usr/bin/env python3
"""
b50 -- THE PLANCHEREL-BY-THE-TOWER UNIT, the exact computations (component 2).
Gates re-verified (rule b); the P1 constant measured on the E1 bases at both levels;
the P2/composite exponents (p^3 on transform-pairings, p^5 on their traces) checked
exactly at both live pairs. Registration: data/b50_registration_2026-08-20.txt
(banked BEFORE this run). Usage: python b50_plancherel_tower.py register | run
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b45_kl_distance import (units_and_basis, cadd, cneg, cconj, cmul, is_zero,
                             BANKED_D1)
from b49_tower_check import emb, scal, galois_sum

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "..", "data", "b50_registration_2026-08-20.txt")

PAIRS = [((2, 2), (2, 3)), ((3, 1), (3, 2))]

def gates(p, n, out):
    q = p ** n; N = q * q
    for t in range(1, N):
        s = {}
        for m in range(N):
            e = (m * t) % N
            s[e] = s.get(e, 0) + 1
        if not is_zero(s, p, N):
            out.append(f"  VOID G1 at N={N}, t={t}"); return False
    out.append(f"  PASS G1  geometric sums = N*delta at N = {N} (t = 1..{N-1}, exact)")
    assert all((-(-m % N)) % N == m for m in range(N))
    out.append(f"  PASS G2  Pi involutive at N = {N} (S^2 = q^2 Pi rides G1, the b44 derivation)")
    return True

def iota_vec(u, p, q, N, qP, NP):
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

def S_apply(v, N):
    Sv = [dict() for _ in range(N)]
    for m in range(N):
        for e, c in v[m].items():
            for mp in range(N):
                ee = (e + m * mp) % N
                Sv[mp][ee] = Sv[mp].get(ee, 0) + c
    return Sv

def pairing(x, y, N):
    acc = {}
    for m in range(N):
        acc = cadd(acc, cmul(cconj(x[m], N), y[m], N))
    return acc

def run_pair(lo, hi, out):
    (p, n), (_, n2) = lo, hi
    q = p ** n; N = q * q; qP = p ** n2; NP = qP * qP
    d1 = BANKED_D1[lo]
    out.append(f"\nPAIR ({p},{n}) -> ({p},{n2})   q = {q} -> {qP}   d_1(level) = {d1}")
    if not (gates(p, n, out) and gates(p, n2, out)):
        return None
    _, _, ell, g, B = units_and_basis(p, n)
    I = [iota_vec(u, p, q, N, qP, NP) for u in B]
    SB = [S_apply(u, N) for u in B]
    SI = [S_apply(v, NP) for v in I]
    # G3: Su = qu level; S+ iota(u) = q+ iota(u) host
    for k in range(d1):
        okl = all(is_zero(cadd(SB[k][m], cneg(scal(B[k][m], q))), p, N) for m in range(N))
        okh = all(is_zero(cadd(SI[k][m], cneg(scal(I[k][m], qP))), p, NP) for m in range(NP))
        out.append(f"  {'PASS' if okl and okh else 'VOID'} G3  Su = qu (level) and "
                   f"S+iota(u) = q+iota(u) (host), u_{k}, exact")
        if not (okl and okh): return None
    # P1 on the E1 bases, both levels: <Su_r, Su_s> = q^2 <u_r, u_s>, exact
    okP1l = okP1h = True
    Glev = [[pairing(B[r], B[s], N) for s in range(d1)] for r in range(d1)]
    Ghost = [[pairing(I[r], I[s], NP) for s in range(d1)] for r in range(d1)]
    for r in range(d1):
        for s in range(d1):
            if not is_zero(cadd(pairing(SB[r], SB[s], N),
                                cneg(scal(Glev[r][s], q * q))), p, N):
                okP1l = False
            if not is_zero(cadd(pairing(SI[r], SI[s], NP),
                                cneg(scal(Ghost[r][s], qP * qP))), p, NP):
                okP1h = False
    out.append(f"  P1 level: <Su_r,Su_s> = q^2 G[r][s] {'EXACT' if okP1l else 'FAILS'} "
               f"(constant q^2 = {q*q})")
    out.append(f"  P1 host:  <S+v_r,S+v_s> = q+^2 G''[r][s] {'EXACT' if okP1h else 'FAILS'} "
               f"(constant q+^2 = {qP*qP})")
    # composite exponents: transform-pairing host = p^3 emb(level); trace = p^5
    ok3 = ok5 = True
    for r in range(d1):
        for s in range(d1):
            TPl = pairing(SB[r], SB[s], N)
            TPh = pairing(SI[r], SI[s], NP)
            if not is_zero(cadd(TPh, cneg(scal(emb(TPl, p), p ** 3))), p, NP):
                ok3 = False
            tr = galois_sum(TPh, p, N, NP)
            if not is_zero(cadd(tr, cneg(scal(emb(TPl, p), p ** 5))), p, NP):
                ok5 = False
    out.append(f"  P2 composite: transform-pairings host = p^3 * emb(level) "
               f"{'EXACT (p^3 = ' + str(p**3) + ')' if ok3 else 'FAILS -- witness banked'}")
    out.append(f"  P2 composite: Tr(transform-pairings) = p^5 * emb(level) "
               f"{'EXACT (p^5 = ' + str(p**5) + ')' if ok5 else 'FAILS -- witness banked'}")
    return {"pair": (lo, hi), "P1": okP1l and okP1h, "p3": ok3, "p5": ok5}

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("register", "run"):
        print(__doc__); return
    if sys.argv[1] == "register":
        print(open(REG, encoding="utf-8", errors="replace").read()); return
    out = ["### REGISTRATION CLOSED (data/b50_registration_2026-08-20.txt, banked before this run).",
           "### MEASUREMENT BEGINS. Exact Z[zeta]; gates re-verified before dependence;",
           "### composite exponents (p^3, p^5) pre-derived in the registration, never fitted.",
           "### The (2,1)->(2,2) step stays VACUOUS (d_1(2,1) = 0) -- recorded."]
    res = [run_pair(lo, hi, out) for lo, hi in PAIRS]
    print("\n".join(out))
    return res

if __name__ == "__main__":
    main()
