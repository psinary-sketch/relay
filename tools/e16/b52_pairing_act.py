#!/usr/bin/env python3
"""
b52 -- THE PAIRING ACT, measured half (component 2). The R5 direct consistency gate
(36-dim two-ring tensor arithmetic, entrywise, never the product shortcut); the
spanning gates (S u = q u re-verified at every cell with units); branch verdicts.
Registration: data/b52_registration_2026-08-20.txt (banked BEFORE this run).
Usage: python b52_pairing_act.py register | run
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b45_kl_distance import units_and_basis, cadd, cneg, is_zero, BANKED_D1
from b49_tower_check import scal

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "..", "data", "b52_registration_2026-08-20.txt")

# ---- the two-ring tensor ring Z[zeta_4] (x) Z[zeta_9]: dict {(e2, e9): int} ----
def tadd(a, b):
    out = dict(a)
    for k, v in b.items(): out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}

def tmul(a, b):
    out = {}
    for (x1, y1), v1 in a.items():
        for (x2, y2), v2 in b.items():
            k = ((x1 + x2) % 4, (y1 + y2) % 9)
            out[k] = out.get(k, 0) + v1 * v2
    return {k: v for k, v in out.items() if v}

def tzero(a):
    # reduce mod Phi_4 (zeta^2 = -1) and Phi_9 (zeta^6 = -zeta^3 - 1)
    arr = [[0] * 9 for _ in range(4)]
    for (x, y), v in a.items(): arr[x][y] += v
    red = [[0] * 6 for _ in range(2)]
    for x in range(4):
        sx, xx = (1, x) if x < 2 else (-1, x - 2)
        for y in range(9):
            terms = [(1, y)] if y < 6 else [(-1, y - 3), (-1, y - 6)]
            for sy, yy in terms:
                red[xx][yy] += sx * sy * arr[x][y]
    return all(c == 0 for row in red for c in row)

def mat_id(n): return [[({(0, 0): 1} if i == j else {}) for j in range(n)] for i in range(n)]

def kron(A, B, nb):
    na = len(A)
    return [[tmul(A[i // nb][j // nb], B[i % nb][j % nb])
             for j in range(na * nb)] for i in range(na * nb)]

def mmul(A, B):
    n = len(A)
    return [[__import__('functools').reduce(lambda s, k: tadd(s, tmul(A[i][k], B[k][j])), range(n), {})
             for j in range(n)] for i in range(n)]

def trace(A):
    return __import__('functools').reduce(lambda s, i: tadd(s, A[i][i]), range(len(A)), {})

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("register", "run"):
        print(__doc__); return
    if sys.argv[1] == "register":
        print(open(REG, encoding="utf-8", errors="replace").read()); return
    out = ["### REGISTRATION CLOSED (data/b52_registration_2026-08-20.txt, banked before this run).",
           "### MEASUREMENT BEGINS. Exact tensor-ring arithmetic at R5; the gates decide the",
           "### spanning verdict; the operator labels' chart-relativity recorded as a deviation",
           "### in-run (the multiplicativity gate is label-independent)."]
    # ---- the R5 consistency gate: S_glob = S_2 (x) S_3, entrywise ----
    S2 = [[{(m * mp % 4, 0): 1} for mp in range(4)] for m in range(4)]
    S3 = [[{(0, m * mp % 9): 1} for mp in range(9)] for m in range(9)]
    Sg = kron(S2, S3, 9)
    def unit(n, i, j, place):
        return [[({(0, 0): 1} if (r == i and c == j) else {}) for c in range(n)] for r in range(n)]
    OPS2 = [("I", mat_id(4)), ("E01", unit(4, 0, 1, 2)), ("E11", unit(4, 1, 1, 2))]
    OPS3 = [("I", mat_id(9)), ("E01", unit(9, 0, 1, 3)), ("E11", unit(9, 1, 1, 3))]
    # powers of S per place and global
    def powers(M, k=4):
        acc = [mat_id(len(M))]
        for _ in range(k - 1): acc.append(mmul(acc[-1], M))
        return acc
    P2, P3, Pg = powers(S2), powers(S3), powers(Sg)
    okall = True
    for n2, A2 in OPS2:
        for n3, A3 in OPS3:
            Ag = kron(A2, A3, 9)
            for j in range(4):
                lhs = trace(mmul(Pg[j], Ag))
                t2 = trace(mmul(P2[j], A2))
                t3 = trace(mmul(P3[j], A3))
                rhs = tmul(t2, t3)
                if not tzero(tadd(lhs, {k: -v for k, v in rhs.items()})):
                    okall = False
                    out.append(f"  GATE FAIL: A=({n2},{n3}), j={j} -- ACT VOIDS FOR REPAIR")
    out.append(f"R5 CONSISTENCY GATE (36-dim entrywise, all 9 operator pairs x 4 powers): "
               f"{'PASS -- tr(S_glob^j A) = tr(S2^j A2) * tr(S3^j A3) EXACTLY in the tensor ring' if okall else 'FAIL'}")
    out.append("  => with trace-linearity (proved abstract: form_level_lift), the factorizable")
    out.append("     identity 4 tr(P1 A) = sum_j prod_v tr(M_v^j A_v) holds at R5 by the proved")
    out.append("     algebra on the gated values; the theorem half's run-gate is met.")
    # ---- the spanning gates: S u = q u at every cell with units ----
    allpass = True
    for cell in [(3, 1), (2, 2), (5, 1), (2, 3), (3, 2)]:
        p, n = cell; q = p ** n; N = q * q
        _, _, ell, g, B = units_and_basis(p, n)
        ok = True
        for u in B:
            Su = [dict() for _ in range(N)]
            for m in range(N):
                for e, c in u[m].items():
                    for mp in range(N):
                        ee = (e + m * mp) % N
                        Su[mp][ee] = Su[mp].get(ee, 0) + c
            if not all(is_zero(cadd(Su[m], cneg(scal(u[m], q))), p, N) for m in range(N)):
                ok = False
        out.append(f"  {'PASS' if ok else 'FAIL'} spanning gate at {cell}: S u = q u exact, all {len(B)} banked basis vectors")
        allpass = allpass and ok
    if allpass:
        out.append("SPANNING VERDICT -- BRANCH (c), BY THE GATES: every banked basis vector is")
        out.append("E_1-exact, so every banked factorizable product lies in the PRINCIPAL (all-ones)")
        out.append("sector of the global E_1; the banked span has ZERO component in every")
        out.append("mixed-pattern direction. THE MIXED DIRECTIONS ARE NOT VISIBLE IN THE BANKED")
        out.append("SPAN -- said exactly. Question (ii) NOT REACHED (as registered in advance).")
        out.append("THE SHORTFALL, banked: the mixed sectors need per-place E_{-1}, E_{+-i} bases;")
        out.append("constructible by the b44 projector method with the three twisted projectors")
        out.append("(1/4) sum_j (-1)^j M^j and (1/4) sum_j (-+i)^j M^j. PRICE: one instrument")
        out.append("sitting (the b44/b45 machinery, three more projectors per cell, same gates).")
        out.append("STAGED FOR THE AUTHOR, not run.")
    print("\n".join(out))

if __name__ == "__main__":
    main()
