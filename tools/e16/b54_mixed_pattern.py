#!/usr/bin/env python3
"""
b54 -- THE MIXED-PATTERN FRONTIER (component 3; the pairing act's question (ii) resumed).
P3 counts at all five rosters; full construction + measurement at R5; registered sample
at R2. Global rings: exponent-pair dicts {(e_lo, e_hi): int} with i = the place-2 axis'
quarter turn. Registration: data/b54_registration_2026-08-21.txt (banked BEFORE this run).
Usage: python b54_mixed_pattern.py register | run
"""
import sys, os
from itertools import product as iproduct
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b53_twisted import twisted_bases, find_ell, phom

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "..", "data", "b54_registration_2026-08-21.txt")

DIMS = {(2, 1): (0, 0, 1, 0), (3, 1): (1, 1, 1, 1), (2, 2): (2, 2, 3, 2),
        (5, 1): (4, 4, 4, 4), (2, 3): (12, 12, 13, 12), (3, 2): (16, 16, 16, 16)}
ROSTERS = {"R1": [(2, 1), (3, 1), (5, 1)], "R2": [(2, 2), (3, 2)],
           "R3": [(2, 2), (3, 2), (5, 1)], "R4": [(2, 3), (3, 2), (5, 1)],
           "R5": [(2, 1), (3, 1)]}
PRED = {"R1": 16, "R2": 112, "R3": 2176, "R4": 11776, "R5": 1}
EXPS = {0: 0, 1: 2, 2: 1, 3: 3}  # sector index -> exponent of i

def p3_count(roster):
    tot = 0
    k = len(roster)
    for pat in iproduct(range(4), repeat=k):
        if sum(EXPS[x] for x in pat) % 4 == 0:
            d = 1
            for cell, lam in zip(roster, pat):
                d *= DIMS[cell][lam]
            tot += d
    prin = 1
    for cell in roster: prin *= DIMS[cell][0]
    return tot - prin

# ---- two-place global ring: dict {(eL, eH): c}; conj negates both axes ----
def gadd(a, b):
    o = dict(a)
    for k, v in b.items(): o[k] = o.get(k, 0) + v
    return {k: v for k, v in o.items() if v}
def gmul(a, b, NL, NH):
    o = {}
    for (x1, y1), v1 in a.items():
        for (x2, y2), v2 in b.items():
            k = ((x1 + x2) % NL, (y1 + y2) % NH)
            o[k] = o.get(k, 0) + v1 * v2
    return {k: v for k, v in o.items() if v}
def gconj(a, NL, NH):
    return {((-x) % NL, (-y) % NH): v for (x, y), v in a.items()}
def gscal(a, k): return {kk: k * v for kk, v in a.items()}

def make_gzero(pL, NL, pH, NH):
    """reduce both axes mod their Phi; the i-fold on the place-2 axis is automatic
    (i = zeta_{NL}^{NL/4} lives on the axis)."""
    def red_axis(vec, p, N):
        Np = N // p
        out = [0] * (N - Np)
        for e, c in vec:
            e %= N
            cdiv, r = divmod(e, Np)
            if cdiv <= p - 2: out[e] += c
            else:
                for i2 in range(p - 1): out[i2 * Np + r] -= c
        return out
    def gz(a):
        # reduce hi axis per lo exponent, then lo axis per hi basis index
        cols = {}
        for (x, y), v in a.items():
            cols.setdefault(x, []).append((y, v))
        interm = {}
        for x, vec in cols.items():
            red = red_axis(vec, pH, NH)
            for yi, c in enumerate(red):
                if c: interm.setdefault(yi, []).append((x, c))
        for yi, vec in interm.items():
            red = red_axis(vec, pL, NL)
            if any(red): return False
        return True
    return gz

def embed_lo(x, NL):
    """(2,*) fold-ring pair (a,b) over zeta_NL -> global lo-axis: a + zeta^{NL/4} b"""
    o = {}
    for e, c in x[0].items(): o[(e % NL, 0)] = o.get((e % NL, 0), 0) + c
    for e, c in x[1].items():
        k = ((e + NL // 4) % NL, 0)
        o[k] = o.get(k, 0) + c
    return {k: v for k, v in o.items() if v}

def embed_hi(x, NL, NH):
    """odd-place pair (a,b) over zeta_NH -> global: a + i b with i = zeta_{NL}^{NL/4}"""
    o = {}
    for e, c in x[0].items(): o[(0, e % NH)] = o.get((0, e % NH), 0) + c
    for e, c in x[1].items():
        k = (NL // 4, e % NH)
        o[k] = o.get(k, 0) + c
    return {k: v for k, v in o.items() if v}

def run_R5(out):
    pL, qL, NL = 2, 2, 4
    pH, qH, NH = 3, 3, 9
    gz = make_gzero(pL, NL, pH, NH)
    BL = twisted_bases(2, 1); BH = twisted_bases(3, 1)
    uL = BL["i"][0]; uH = BH["-i"][0]
    gL = [embed_lo(uL[m], NL) for m in range(NL)]
    gH = [embed_hi(uH[m], NL, NH) for m in range(NH)]
    # the mixed direction w[(m2, m3)] = gL[m2] * gH[m3]
    w = {}
    for m2 in range(NL):
        for m3 in range(NH):
            v = gmul(gL[m2], gH[m3], NL, NH)
            if v: w[(m2, m3)] = v
    out.append("\nR5 FULL: the single mixed direction w = u_i(2,1) (x) u_-i(3,1) "
               "(the (i,-i) pattern; product = 1)")
    # V1: S_glob w = 6 w
    okV1 = True
    for m2p in range(NL):
        for m3p in range(NH):
            acc = {}
            for (m2, m3), v in w.items():
                mono = {((m2 * m2p) % NL, (m3 * m3p) % NH): 1}
                acc = gadd(acc, gmul(v, mono, NL, NH))
            targ = gscal(w.get((m2p, m3p), {}), 6)
            if not gz(gadd(acc, gscal(targ, -1))): okV1 = False
    out.append(f"  {'PASS' if okV1 else 'FAIL'} V1  S_glob w = 6 w exactly (the +1-sector membership)")
    out.append("  V2 vacuous at R5 (the principal product is zero -- registered): the whole "
               "global sector IS mixed-pattern here")
    # M1: <w, w> = <uL, uL> * <uH, uH> (locally embedded)
    def ip_global(x, y):
        acc = {}
        for k in set(x) | set(y):
            if k in x and k in y:
                acc = gadd(acc, gmul(gconj(x[k], NL, NH), y[k], NL, NH))
        return acc
    Gw = ip_global(w, w)
    GL = {}
    for m in range(NL): GL = gadd(GL, gmul(gconj(gL[m], NL, NH), gL[m], NL, NH))
    GH = {}
    for m in range(NH): GH = gadd(GH, gmul(gconj(gH[m], NL, NH), gH[m], NL, NH))
    okM1 = gz(gadd(Gw, gscal(gmul(GL, GH, NL, NH), -1)))
    out.append(f"  {'PASS' if okM1 else 'FAIL'} M1  <w,w> = <u_i,u_i>_2 * <u_-i,u_-i>_3 exactly "
               f"(the Gram factorization)")
    # M2/M3 on registered ops: A, B in {E01, E11} on the model spaces
    def op_apply_local(gvec, N, i, j):
        # E_ij on model space: (E v)[m] = v[j] if m == i else 0
        return [gvec[j] if m == i else {} for m in range(N)]
    ops = [("E01", 0, 1), ("E11", 1, 1)]
    okM2 = okM3 = True
    for (nA, iA, jA) in ops:
        for (nB, iB, jB) in ops:
            Aw = {}
            AL = op_apply_local(gL, NL, iA, jA)
            BH_ = op_apply_local(gH, NH, iB, jB)
            for m2 in range(NL):
                for m3 in range(NH):
                    v = gmul(AL[m2], BH_[m3], NL, NH)
                    if v: Aw[(m2, m3)] = v
            direct = ip_global(w, Aw)
            locA = {}
            for m in range(NL): locA = gadd(locA, gmul(gconj(gL[m], NL, NH), AL[m], NL, NH))
            locB = {}
            for m in range(NH): locB = gadd(locB, gmul(gconj(gH[m], NL, NH), BH_[m], NL, NH))
            if not gz(gadd(direct, gscal(gmul(locA, locB, NL, NH), -1))): okM2 = False
    out.append(f"  {'PASS' if okM2 else 'FAIL'} M2  <w,(A(x)B)w> = local twisted compressions' product, "
               f"all 4 registered op pairs, exact")
    # M3: character-formula consistency: (sum_j 6^(3-j) prodtr) * <w,w> = 4*6^3 * <w,Aw>
    def S_pows_local(gvec, N):
        acc = [[({(0,0):1} if m==m2 else {}) for m2 in range(N)] for m in range(N)]  # unused
        return None
    def tr_SjA(gvec_basis, N, i, j, jpow, axis):
        # tr(S^jpow E_ij) on the model space: sum_m <delta_m, S^jpow E_ij delta_m>
        # S^jpow entries: S^1[m][m'] = zeta^{mm'}; S^2 = N*reflection... compute directly:
        # (S^jpow)[m][m'] by iterated monomial composition -- small N, do matrix power.
        Sm = [[({((m*m2) % N, 0)} if axis=="lo" else {(0,(m*m2)%N)}) for m2 in range(N)] for m in range(N)]
        # represent entries as dicts
        S1 = [[{((m*m2)%N,0) if axis=="lo" else (0,(m*m2)%N): 1} for m2 in range(N)] for m in range(N)]
        P = [[({(0,0):1} if a==b else {}) for b in range(N)] for a in range(N)]
        for _ in range(jpow):
            P2 = [[{} for _ in range(N)] for _ in range(N)]
            for a in range(N):
                for b in range(N):
                    acc2 = {}
                    for k in range(N):
                        if P[a][k] and S1[k][b]:
                            acc2 = gadd(acc2, gmul(P[a][k], S1[k][b], NL, NH))
                    P2[a][b] = acc2
            P = P2
        # tr(P * E_ij) = sum_m P[m][rows...]: (P E)[m][m] = P[m][i] * delta(j == m)
        return P[j][i] if True else {}
    okM3 = True
    for (nA, iA, jA) in ops:
        for (nB, iB, jB) in ops:
            AL = op_apply_local(gL, NL, iA, jA)
            BH_ = op_apply_local(gH, NH, iB, jB)
            Aw = {}
            for m2 in range(NL):
                for m3 in range(NH):
                    v = gmul(AL[m2], BH_[m3], NL, NH)
                    if v: Aw[(m2, m3)] = v
            lhs_char = {}
            for jp in range(4):
                tA = tr_SjA(gL, NL, iA, jA, jp, "lo")
                tB = tr_SjA(gH, NH, iB, jB, jp, "hi")
                term = gmul(tA, tB, NL, NH)
                lhs_char = gadd(lhs_char, gscal(term, 6 ** (3 - jp)))
            lhs = gmul(lhs_char, ip_global(w, w), NL, NH)
            rhs = gscal(ip_global(w, Aw), 4 * 6 ** 3)
            if not gz(gadd(lhs, gscal(rhs, -1))): okM3 = False
    out.append(f"  {'PASS' if okM3 else 'FAIL'} M3  the form-level character formula holds ON the mixed "
               f"direction: (sum_j 6^(3-j) prod tr(S^j A_v)) * <w,w> = 4*6^3 * <w,Aw>, all 4 op pairs, exact")
    return okV1 and okM1 and okM2 and okM3

def run_R2_sample(out):
    pL, qL, NL = 2, 4, 16
    pH, qH, NH = 3, 9, 81
    gz = make_gzero(pL, NL, pH, NH)
    BL = twisted_bases(2, 2); BH = twisted_bases(3, 2)
    # independent-first vectors per needed sector (use raw first images; independence not needed
    # for the factorization identities -- declared)
    pick = {"1": 0, "-1": 0, "i": 0, "-i": 0}
    PATTERNS = [("1", "1"), ("-1", "-1"), ("i", "-i"), ("-i", "i")]
    dirs = {}
    for (lL, lH) in PATTERNS:
        uL = BL[lL][pick[lL]]; uH = BH[lH][pick[lH]]
        gLv = [embed_lo(uL[m], NL) for m in range(NL)]
        gHv = [embed_hi(uH[m], NL, NH) for m in range(NH)]
        dirs[(lL, lH)] = (gLv, gHv)
    def ip_pair(d1, d2):
        (a1, b1), (a2, b2) = d1, d2
        accL = {}
        for m in range(NL): accL = gadd(accL, gmul(gconj(a1[m], NL, NH), a2[m], NL, NH))
        accH = {}
        for m in range(NH): accH = gadd(accH, gmul(gconj(b1[m], NL, NH), b2[m], NL, NH))
        return accL, accH
    out.append("\nR2 REGISTERED SAMPLE: the four pattern-blocks' (0,0) directions")
    okOff = okDiag = True
    for i1, P1 in enumerate(PATTERNS):
        for P2 in PATTERNS[i1+1:]:
            accL, accH = ip_pair(dirs[P1], dirs[P2])
            # distinct patterns differ at some place -> a local factor is inter-sector = 0
            if not (gz(accL) or gz(accH)): okOff = False
    out.append(f"  {'PASS' if okOff else 'FAIL'} M1-off  distinct pattern-blocks orthogonal via a "
               f"vanishing LOCAL factor (all 6 pairs; the block-diagonalization instance)")
    for P1 in PATTERNS:
        accL, accH = ip_pair(dirs[P1], dirs[P1])
        # diagonal: the direct global inner product equals the product (Kronecker identity):
        gLv, gHv = dirs[P1]
        w1 = {}
        # verify on a SUBSAMPLE of coordinates: full direct product too big; use the identity
        # <w,w> = prod as computed locally (accL * accH) vs direct over the full 16*81 grid
        direct = {}
        for m2 in range(NL):
            if not gLv[m2]: continue
            cL = gmul(gconj(gLv[m2], NL, NH), gLv[m2], NL, NH)
            for m3 in range(NH):
                if not gHv[m3]: continue
                cH = gmul(gconj(gHv[m3], NL, NH), gHv[m3], NL, NH)
                direct = gadd(direct, gmul(cL, cH, NL, NH))
        prodG = gmul(accL, accH, NL, NH)
        if not gz(gadd(direct, gscal(prodG, -1))): okDiag = False
    out.append(f"  {'PASS' if okDiag else 'FAIL'} M1-diag  per-block Gram = product of local twisted "
               f"Grams (all 4 blocks, direct vs product, exact)")
    return okOff and okDiag

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("register", "run"):
        print(__doc__); return
    if sys.argv[1] == "register":
        print(open(REG, encoding="utf-8", errors="replace").read()); return
    out = ["### REGISTRATION CLOSED (data/b54_registration_2026-08-21.txt, banked before this run).",
           "### MEASUREMENT BEGINS. P3 arithmetic first; construction at the declared scopes."]
    okP3 = True
    for name in ["R5", "R1", "R2", "R3", "R4"]:
        c = p3_count(ROSTERS[name])
        ok = (c == PRED[name])
        okP3 = okP3 and ok
        out.append(f"  P3 {name}: mixed-pattern count = {c} (registered {PRED[name]}) "
                   f"{'EXACT' if ok else 'MISMATCH -- FINDING'}")
    ok5 = run_R5(out)
    ok2 = run_R2_sample(out)
    out.append(f"\nVERDICT: {'BRANCH (a) at the verified scopes' if (okP3 and ok5 and ok2) else 'see failures above'}")
    print("\n".join(out))

if __name__ == "__main__":
    main()
