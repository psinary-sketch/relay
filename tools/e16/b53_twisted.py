#!/usr/bin/env python3
"""
b53 -- THE TWISTED-PROJECTOR EXTENSION (components 1-2). Exact arithmetic in the
declared per-cell rings (p = 2: Z[zeta_N] with i = zeta^{N/4} folded at the test;
odd p: the composite Z[zeta_N][i] as pairs, componentwise tests). Registration:
data/b53_registration_2026-08-21.txt (banked BEFORE this run).
Usage: python b53_twisted.py register | run
"""
import sys, os
from itertools import combinations
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b45_kl_distance import cadd, cneg, cconj, cmul, is_zero as zzero, BANKED_D1

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "..", "data", "b53_registration_2026-08-21.txt")

CELLS = [(2, 1), (3, 1), (2, 2), (5, 1), (2, 3), (3, 2)]
DIMS = {(2, 1): (0, 0, 1, 0), (3, 1): (1, 1, 1, 1), (2, 2): (2, 2, 3, 2),
        (5, 1): (4, 4, 4, 4), (2, 3): (12, 12, 13, 12), (3, 2): (16, 16, 16, 16)}
LAMS = ["1", "-1", "i", "-i"]
LIDX = {"1": 0, "-1": 1, "i": 2, "-i": 3}

# ---- pair ring: (a, b) ~ a + i b, a/b sparse Z[zeta_N] dicts ----
def padd(x, y): return (cadd(x[0], y[0]), cadd(x[1], y[1]))
def pneg(x): return (cneg(x[0]), cneg(x[1]))
def pconj(x, N): return (cconj(x[0], N), cneg(cconj(x[1], N)))
def pmul(x, y, N):
    a, b = x; c, d = y
    return (cadd(cmul(a, c, N), cneg(cmul(b, d, N))),
            cadd(cmul(a, d, N), cmul(b, c, N)))
def pscal(x, k): return ({e: k * c for e, c in x[0].items()},
                         {e: k * c for e, c in x[1].items()})
def pmul_i(x): return (cneg(x[1]), x[0])          # i*(a+ib) = -b + ia
def pmul_lam(x, lam):
    if lam == "1": return x
    if lam == "-1": return pneg(x)
    if lam == "i": return pmul_i(x)
    return pneg(pmul_i(x))
def shift(d, k, N): return {(e + k) % N: c for e, c in d.items()}
def pzero(x, p, N):
    if p == 2:  # fold i = zeta^{N/4}
        return zzero(cadd(x[0], shift(x[1], N // 4, N)), p, N)
    return zzero(x[0], p, N) and zzero(x[1], p, N)

def find_ell(N):
    L = 4 * N if N % 2 else N  # need 1 mod 4 and mod N
    ell = L + 1
    while True:
        if ell % 4 == 1 and ell % N == 1 and all(ell % r for r in range(2, int(ell**0.5) + 1)):
            for c in range(2, ell):
                g = pow(c, (ell - 1) // N, ell)
                primes = [x for x in range(2, N + 1) if N % x == 0 and all(x % y for y in range(2, int(x**0.5) + 1))]
                if g != 1 and pow(g, N, ell) == 1 and all(pow(g, N // f, ell) != 1 for f in primes):
                    I = pow(c, (ell - 1) // 4, ell)
                    if (I * I) % ell == ell - 1:
                        return ell, g, I
        ell += L

def phom(x, ell, g, I, N):
    v = sum(c * pow(g, e % N, ell) for e, c in x[0].items())
    v += I * sum(c * pow(g, e % N, ell) for e, c in x[1].items())
    return v % ell

def twisted_bases(p, n):
    """all four sectors' projector images per Sonin basis vector, pair-ring entries"""
    q = p ** n; N = q * q
    out = {lam: [] for lam in LAMS}
    for i in range(1, q):
        for j in range(1, q):
            f = {(i + q * j) % N: 1, i % N: -1}
            pif = {(-m) % N: c for m, c in f.items()}
            hplus = cadd(f, pif); hminus = cadd(f, cneg(pif))
            def S_of(h):
                Sv = [dict() for _ in range(N)]
                for m, c in h.items():
                    if c == 0: continue
                    for mp in range(N):
                        e = (m * mp) % N
                        Sv[mp][e] = Sv[mp].get(e, 0) + c
                return Sv
            Sp_, Sm_ = S_of(hplus), S_of(hminus)
            qh_p = [{0: q * hplus.get(m, 0)} if hplus.get(m, 0) else {} for m in range(N)]
            qh_m = [{0: q * hminus.get(m, 0)} if hminus.get(m, 0) else {} for m in range(N)]
            u1  = [(cadd(qh_p[m], Sp_[m]), {}) for m in range(N)]
            um1 = [(cadd(qh_p[m], cneg(Sp_[m])), {}) for m in range(N)]
            ui  = [(qh_m[m], cneg(Sm_[m])) for m in range(N)]
            umi = [(qh_m[m], Sm_[m]) for m in range(N)]
            for lam, u in zip(LAMS, [u1, um1, ui, umi]):
                out[lam].append(u)
    return out

def S_pair(v, N):
    Sv = [({}, {}) for _ in range(N)]
    for m in range(N):
        for comp in (0, 1):
            for e, c in v[m][comp].items():
                for mp in range(N):
                    ee = (e + m * mp) % N
                    d = Sv[mp][comp]
                    d[ee] = d.get(ee, 0) + c
    return Sv

def run_cell(p, n, out):
    q = p ** n; N = q * q
    ell, g, I = find_ell(N)
    out.append(f"\nCELL ({p},{n})  q = {q}  ring: " +
               ("Z[zeta_N], i = zeta^(N/4) folded" if p == 2 else "Z[zeta_N][i] pairs") +
               f"  [ell = {ell}]")
    # G-A
    for t in range(1, N):
        s = {}
        for m in range(N):
            e = (m * t) % N
            s[e] = s.get(e, 0) + 1
        if not zzero(s, p, N):
            out.append("  VOID G-A"); return None
    out.append(f"  PASS G-A  geometric sums exact (S^2 = q^2 Pi)")
    B = twisted_bases(p, n)
    idx = [(i, j) for i in range(1, q) for j in range(1, q)]
    # G-B completeness: sum_lambda u_lambda = 4q f
    okB = True
    for k, (i, j) in enumerate(idx):
        f = {(i + q * j) % N: 1, i % N: -1}
        for m in range(N):
            tot = ({}, {})
            for lam in LAMS: tot = padd(tot, B[lam][k][m])
            targ = ({0: 4 * q * f.get(m, 0)} if f.get(m, 0) else {}, {})
            if not pzero(padd(tot, pneg(targ)), p, N): okB = False
    out.append(f"  {'PASS' if okB else 'VOID'} G-B  completeness: sum_lambda u_lambda = 4q f, every basis vector")
    if not okB: return None
    # G-C eigenvector per image (sampled fully for small, first 4 per sector for big)
    okC = True
    for lam in LAMS:
        sample = B[lam] if len(B[lam]) <= 9 else B[lam][:4]
        for u in sample:
            Su = S_pair(u, N)
            lu = [pmul_lam(pscal(u[m], q), lam) for m in range(N)]
            if not all(pzero(padd(Su[m], pneg(lu[m])), p, N) for m in range(N)):
                okC = False
    out.append(f"  {'PASS' if okC else 'VOID'} G-C  S u = lambda q u per twisted image (full/sampled, declared)")
    if not okC: return None
    # P1 traces
    okP1 = True
    for lam in LAMS:
        tr = ({}, {})
        for k, (i, j) in enumerate(idx):
            tr = padd(tr, B[lam][k][(i + q * j) % N])
        d = DIMS[(p, n)][LIDX[lam]]
        targ = ({0: 4 * q * d}, {})
        if not pzero(padd(tr, pneg(targ)), p, N): okP1 = False
    s4 = sum(DIMS[(p, n)])
    out.append(f"  {'PASS' if okP1 else 'VOID'} P1  tr(4q P_lambda) = 4q d_lambda at every lambda; "
               f"dims {DIMS[(p,n)]} sum {s4} = (q-1)^2 = {(q-1)**2}")
    if not okP1: return None
    # G-C' inter-sector orthogonality (full small cells, sampled big)
    okO = True
    pairs_checked = 0
    for l1, l2 in combinations(LAMS, 2):
        s1 = B[l1] if len(B[l1]) <= 4 else B[l1][:2]
        s2 = B[l2] if len(B[l2]) <= 4 else B[l2][:2]
        for u in s1:
            for v in s2:
                acc = ({}, {})
                for m in range(N):
                    acc = padd(acc, pmul(pconj(u[m], N), v[m], N))
                pairs_checked += 1
                if not pzero(acc, p, N): okO = False
    out.append(f"  {'PASS' if okO else 'VOID'} G-C'  inter-sector orthogonality <u_l, u_m> = 0 "
               f"({pairs_checked} pairs, full/sampled declared)")
    # Son membership incl. ball rows (twisted ball-silence precondition)
    okS = True
    for lam in LAMS:
        for u in (B[lam] if len(B[lam]) <= 9 else B[lam][:4]):
            for b in range(q):
                if not pzero(u[(q * b) % N], p, N): okS = False
    out.append(f"  {'PASS' if okS else 'VOID'} P2'  ball rows vanish in every twisted sector "
               f"(=> the ball-silence law transfers verbatim: X_E = 0, c = 0, same longhand)")
    # P2 minors per twisted sector: mod-ell screen; independent subset per sector first
    res = {}
    for lam in LAMS:
        d = DIMS[(p, n)][LIDX[lam]]
        if d == 0:
            res[lam] = "empty sector (d = 0)"; continue
        if q == 2:
            res[lam] = "PURE BY SHAPE (1x1 block; registered exception)"; continue
        # greedy independent subset mod ell
        basis, rows = [], []
        for u in B[lam]:
            row = [phom(x, ell, g, I, N) for x in u]
            cur = row[:]
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
            if len(basis) == d: break
        if len(basis) != d:
            res[lam] = f"VOID: independent subset {len(basis)} != d = {d}"; continue
        mixed = 0
        for u in basis:
            C = [[phom(u[(a + q * b) % N], ell, g, I, N) for b in range(q)] for a in range(q)]
            wit = None
            for (a1, a2) in combinations(range(q), 2):
                for (b1, b2) in combinations(range(q), 2):
                    if (C[a1][b1] * C[a2][b2] - C[a1][b2] * C[a2][b1]) % ell:
                        wit = (a1, a2, b1, b2); break
                if wit: break
            if wit: mixed += 1
        res[lam] = f"MIXED {mixed}/{d} basis vectors (mod-{ell} witnesses, exact certificates)"
    for lam in LAMS:
        out.append(f"    E_{lam}: {res[lam]}")
    return {"cell": (p, n), "res": res}

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("register", "run"):
        print(__doc__); return
    if sys.argv[1] == "register":
        print(open(REG, encoding="utf-8", errors="replace").read()); return
    out = ["### REGISTRATION CLOSED (data/b53_registration_2026-08-21.txt, banked before this run).",
           "### MEASUREMENT BEGINS. Per-cell rings as declared; mod-ell certificate direction only."]
    for (p, n) in CELLS:
        if run_cell(p, n, out) is None:
            out.append(f"  CELL ({p},{n}) VOID -- stop per registration"); break
    print("\n".join(out))

if __name__ == "__main__":
    main()
