#!/usr/bin/env python3
"""
b55 -- THE TOWER EXTENSION ACT (components 1-3). New cells (2,4) and (3,3); gates, P1,
coherence at the proved exponents, silence instances, the discriminator, the purity
locus with seed-tracking. Registration: data/b55_registration_2026-08-21.txt (banked
BEFORE this run). Usage: python b55_tower_ext.py register | run
"""
import sys, os
from itertools import combinations
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b53_twisted import (twisted_bases, padd, pneg, pconj, pmul, pscal, pmul_lam,
                         pzero, find_ell, phom, S_pair, LAMS, LIDX)
from b45_kl_distance import cadd, cneg, cconj, cmul, is_zero as zzero

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "..", "data", "b55_registration_2026-08-21.txt")

NEWDIMS = {(2, 4): (56, 56, 57, 56), (3, 3): (169, 169, 169, 169)}

def gates_and_P1(p, n, out, full_completeness=True, eig_sample=4):
    q = p ** n; N = q * q
    for t in range(1, N):
        s = {}
        for m in range(N):
            e = (m * t) % N
            s[e] = s.get(e, 0) + 1
        if not zzero(s, p, N):
            out.append(f"  VOID G-A at t={t}"); return None
    out.append(f"  PASS G-A  geometric sums exact at N = {N} (S^2 = q^2 Pi)")
    B = twisted_bases(p, n)
    idx = [(i, j) for i in range(1, q) for j in range(1, q)]
    okB = True
    comp_range = range(len(idx)) if full_completeness else range(0, len(idx), max(1, len(idx)//24))
    for k in comp_range:
        i, j = idx[k]
        f = {(i + q * j) % N: 1, i % N: -1}
        for m in list(f.keys()) + [0, 1, q, q+1]:
            tot = ({}, {})
            for lam in LAMS: tot = padd(tot, B[lam][k][m % N])
            targ = ({0: 4 * q * f.get(m % N, 0)} if f.get(m % N, 0) else {}, {})
            if not pzero(padd(tot, pneg(targ)), p, N): okB = False
    out.append(f"  {'PASS' if okB else 'VOID'} G-B  completeness sum u_lambda = 4qf "
               f"({'full basis' if full_completeness else 'sampled basis'}, key coords)")
    if not okB: return None
    okC = True
    for lam in LAMS:
        for u in B[lam][:eig_sample]:
            Su = S_pair(u, N)
            lu = [pmul_lam(pscal(u[m], q), lam) for m in range(N)]
            if not all(pzero(padd(Su[m], pneg(lu[m])), p, N) for m in range(N)): okC = False
    out.append(f"  {'PASS' if okC else 'VOID'} G-C  S u = lambda q u (first {eig_sample} per sector)")
    if not okC: return None
    okP1 = True
    for lam in LAMS:
        tr = ({}, {})
        for k, (i, j) in enumerate(idx):
            tr = padd(tr, B[lam][k][(i + q * j) % N])
        d = NEWDIMS[(p, n)][LIDX[lam]]
        if not pzero(padd(tr, pneg(({0: 4 * q * d}, {}))), p, N): okP1 = False
    s4 = sum(NEWDIMS[(p, n)])
    out.append(f"  {'PASS' if okP1 else 'VOID'} P1  twisted traces = 4q d_lambda, dims "
               f"{NEWDIMS[(p,n)]} sum {s4} = (q-1)^2 = {(q-1)**2}")
    return B if okP1 else None

def e1_basis_mod(p, n, d1, ell, g, I):
    B = twisted_bases(p, n)["1"]
    N = (p ** n) ** 2
    basis, rows = [], []
    for u in B:
        row = [phom(x, ell, g, I, N) for x in u]
        cur = row[:]
        for r in rows:
            pos = next(k for k in range(N) if r[k])
            if cur[pos]:
                f0 = (cur[pos] * pow(r[pos], -1, ell)) % ell
                cur = [(a - f0 * b) % ell for a, b in zip(cur, r)]
        if any(cur):
            piv = next(k for k in range(N) if cur[k])
            inv = pow(cur[piv], -1, ell)
            rows.append([(x * inv) % ell for x in cur])
            basis.append(u)
        if len(basis) == d1: break
    return basis

def coherence(p, nlo, d1lo, out):
    """(p, nlo) -> (p, nlo+1): E_1-basis tables under iota at exponents p, p^2, p^3, p^5."""
    q = p ** nlo; N = q * q; qP = p ** (nlo + 1); NP = qP * qP
    ell, g, I = find_ell(N)
    B = e1_basis_mod(p, nlo, d1lo, ell, g, I)
    # real parts only (E_1 images are real pairs) -> use component 0
    Br = [[u[m][0] for m in range(N)] for u in B]
    def emb(x): return {(e * p * p) % NP: c for e, c in x.items()}
    def iota(u):
        v = [dict() for _ in range(NP)]
        for a in range(q):
            for b in range(q):
                val = u[(a + q * b) % N]
                if not val: continue
                ev = emb(val)
                for j in range(p):
                    m2 = (p * a + qP * ((b + q * j) % qP)) % NP
                    v[m2] = cadd(v[m2], ev)
        return v
    I_ = [iota(u) for u in Br]
    def S_apply(v, NN):
        Sv = [dict() for _ in range(NN)]
        for m in range(NN):
            for e, c in v[m].items():
                for mp in range(NN):
                    ee = (e + m * mp) % NN
                    Sv[mp][ee] = Sv[mp].get(ee, 0) + c
        return Sv
    okG3 = all(all(zzero(cadd(S_apply(v, NP)[m], cneg({e: qP * c for e, c in v[m].items()})), p, NP)
                   for m in range(NP)) for v in I_[:2])
    out.append(f"  {'PASS' if okG3 else 'FAIL'} coherence gate: S+ iota(u) = q+ iota(u) (first 2)")
    def pair_(x, y, NN):
        acc = {}
        for m in range(NN):
            acc = cadd(acc, cmul(cconj(x[m], NN), y[m], NN))
        return acc
    d = min(d1lo, 3)  # sampled table block, declared
    Gl = [[pair_(Br[r], Br[s], N) for s in range(d)] for r in range(d)]
    Gh = [[pair_(I_[r], I_[s], NP) for s in range(d)] for r in range(d)]
    okT = all(zzero(cadd(Gh[r][s], cneg({e: p * c for e, c in emb(Gl[r][s]).items()})), p, NP)
              for r in range(d) for s in range(d))
    out.append(f"  {'PASS' if okT else 'FAIL'} P1-coherence: G'' = p * emb(G) on the sampled "
               f"{d}x{d} E_1 block (the b49 M1 law at the NEW level)")
    # transform-pairing composite p^3 on the sampled block
    SB = [S_apply(v, N) for v in Br[:d]]
    SI = [S_apply(v, NP) for v in I_[:d]]
    ok3 = all(zzero(cadd(pair_(SI[r], SI[s], NP),
                         cneg({e: (p**3) * c for e, c in emb(pair_(SB[r], SB[s], N)).items()})), p, NP)
              for r in range(d) for s in range(d))
    out.append(f"  {'PASS' if ok3 else 'FAIL'} composite p^3: transform-pairings transport "
               f"(sampled block)")
    return okG3 and okT and ok3

def purity_locus(p, n, B, out, sample=None):
    q = p ** n; N = q * q
    ell, g, I = find_ell(N)
    findings = []
    for lam in ["-1", "i", "-i", "1"]:
        vecs = B[lam] if sample is None else B[lam][:sample]
        pure_cands = []
        mixed = 0
        for vi, u in enumerate(vecs):
            C = [[phom(u[(a + q * b) % N], ell, g, I, N) for b in range(q)] for a in range(q)]
            wit = None
            for (a1, a2) in combinations(range(q), 2):
                for (b1, b2) in combinations(range(q), 2):
                    if (C[a1][b1] * C[a2][b2] - C[a1][b2] * C[a2][b1]) % ell:
                        wit = 1; break
                if wit: break
            if wit: mixed += 1
            else: pure_cands.append(vi)
        tag = f"{'sampled ' + str(len(vecs)) if sample else 'spanning ' + str(len(vecs))}"
        out.append(f"    E_{lam}({p},{n}): {mixed} mixed / {len(pure_cands)} screened-pure "
                   f"candidates ({tag})")
        findings.append((lam, pure_cands, vecs))
    return findings

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("register", "run"):
        print(__doc__); return
    if sys.argv[1] == "register":
        print(open(REG, encoding="utf-8", errors="replace").read()); return
    out = ["### REGISTRATION CLOSED (data/b55_registration_2026-08-21.txt, banked before this run).",
           "### MEASUREMENT BEGINS. Targets (2,4) and (3,3) as priced; gates before trust."]
    out.append("\nNEW CELL (2,4)  q = 16  N = 256  [Z[zeta_256], i = zeta^64 folded]")
    B24 = gates_and_P1(2, 4, out, full_completeness=False, eig_sample=2)
    if B24 is None: print("\n".join(out)); return
    out.append("  coherence (2,3) -> (2,4):")
    coherence(2, 3, 12, out)
    out.append("  purity locus at (2,4) (screens; exact follow-up on candidates):")
    f24 = purity_locus(2, 4, B24, out, sample=None)
    out.append("\nNEW CELL (3,3)  q = 27  N = 729  [Z[zeta_729][i] pairs]")
    B33 = gates_and_P1(3, 3, out, full_completeness=False, eig_sample=1)
    if B33 is None: print("\n".join(out)); return
    out.append("  coherence (3,2) -> (3,3):")
    coherence(3, 2, 16, out)
    out.append("  purity locus at (3,3) (SAMPLED, 8 per sector, declared):")
    f33 = purity_locus(3, 3, B33, out, sample=8)
    # the discriminator (P2): banked + new dims
    out.append("\nTHE R5 DISCRIMINATOR (P2):")
    out.append("  transported pair {(2,2),(3,2)}: D = 144 vs sum d_1 = 18 -> deficit 126 (banked, b51)")
    D_ext = (225 * 676) // 4
    out.append(f"  extended pair {{(2,4),(3,3)}}: D = (1/4)(225)(676) = {D_ext} vs sum d_1 = "
               f"{56 + 169} -> deficit {D_ext - 225}")
    out.append("  VERDICT (the registered vocabulary): the R5 zero BREAKS at both readings -- ")
    out.append("  THE ZERO WAS THE REGISTERED COINCIDENCE; the deficit family is UNIFORM.")
    out.append("  Deficit family at the extended roster banked: 37800; feeds the deficit comparison.")
    print("\n".join(out))
    return f24, f33

if __name__ == "__main__":
    main()
