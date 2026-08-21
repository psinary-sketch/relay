#!/usr/bin/env python3
"""
b57 -- THE DEPTH ACT, ROW 31. P1/P2 verified from the BANK-READ dims before anything is
built; the Component-3 dim-law targets checked against the banks; the P3 iota-chain run
through (2,2), (2,3), (2,4) with the (2,3) instance NEW. Registration:
data/b57_registration_2026-08-21.txt (banked BEFORE this run).
Usage: python b57_row31_depth.py register | run
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b45_kl_distance import cadd, cneg, is_zero as zzero

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "..", "data")
REG = os.path.join(DATA, "b57_registration_2026-08-21.txt")

def read_banked_dims():
    """The dims are READ FROM THE BANKS (b53 bank text; b55 bank text), never hardcoded."""
    dims = {}
    t53 = open(os.path.join(DATA, "b53_twisted_bases.txt"), encoding="utf-8", errors="replace").read()
    for m in re.finditer(r"\((\d),(\d)\)=\((\d+),\s*(\d+),\s*(\d+),\s*(\d+)\)", t53):
        p, n = int(m.group(1)), int(m.group(2))
        dims[(p, n)] = tuple(int(m.group(k)) for k in range(3, 7))
    t55 = open(os.path.join(DATA, "b55_tower_extension.txt"), encoding="utf-8", errors="replace").read()
    for m in re.finditer(r"\((\d),(\d)\)\s+q\s*=\s*\d+.*?dims \((\d+), (\d+), (\d+), (\d+)\)", t55, re.S):
        p, n = int(m.group(1)), int(m.group(2))
        if (p, n) not in dims:
            dims[(p, n)] = tuple(int(m.group(k)) for k in range(3, 7))
    return dims

def p1_p2(dims, out):
    okP1 = okP2 = True
    for (p, n), (d1, dm1, di, dmi) in sorted(dims.items()):
        q = p ** n
        t1 = (d1 - dm1, di - dmi)          # Re, Im
        t3 = (d1 - dm1, -(di - dmi))
        t2 = d1 + dm1 - di - dmi
        conj_ok = (t3 == (t1[0], -t1[1]))
        out.append(f"  ({p},{n}) dims {(d1,dm1,di,dmi)}: t1 = {t1}, t2 = {t2}, "
                   f"t3 = {t3} -- t3 = conj(t1): {'OK' if conj_ok else 'FAIL'}; t2 real by form")
        if not conj_ok: okP1 = False
        if p == 2:
            if not (t1 == (0, 1) and t2 == -1 and d1 == dm1 == dmi and di == dmi + 1): okP2 = False
        else:
            if not (t1 == (0, 0) and t2 == 0 and d1 == dm1 == di == dmi): okP2 = False
    out.append(f"  P1 {'VERIFIED' if okP1 else 'FAILED'}: t3 = conj(t1) and t2 real at every banked cell (from bank-read dims)")
    out.append(f"  P2 {'VERIFIED' if okP2 else 'FAILED'}: odd cells exactly flat; place-2 twisted trace exactly i, excess one, others equal")
    return okP1 and okP2

def dim_law_targets(dims, out):
    ok = True
    for (p, n), t in sorted(dims.items()):
        q = p ** n
        if p == 2:
            d = q * (q - 2) // 4
            law = (d, d, d + 1, d)
        else:
            d = (q - 1) ** 2 // 4
            law = (d, d, d, d)
        hit = (law == t)
        out.append(f"  ({p},{n}): law tuple {law} vs banked {t}: {'EXACT' if hit else 'MISMATCH'}")
        if not hit: ok = False
    out.append(f"  COMPONENT-3 DIM LAW: {'EXACT AT ALL EIGHT BANKED CELLS' if ok else 'MISMATCH -- branch (b) evidence'}")
    return ok

def S_apply(v, NN):
    Sv = [dict() for _ in range(NN)]
    for m in range(NN):
        for e, c in v[m].items():
            for mp in range(NN):
                ee = (e + m * mp) % NN
                Sv[mp][ee] = Sv[mp].get(ee, 0) + c
    return Sv

def iota(u, p, nlo):
    q = p ** nlo; N = q * q; qP = p ** (nlo + 1); NP = qP * qP
    v = [dict() for _ in range(NP)]
    for a in range(q):
        for b in range(q):
            val = u[(a + q * b) % N]
            if not val: continue
            ev = {(e * p * p) % NP: c for e, c in val.items()}
            for j in range(p):
                m2 = (p * a + qP * ((b + q * j) % qP)) % NP
                v[m2] = cadd(v[m2], ev)
    return v

def chain_check(u, p, n, out):
    q = p ** n; N = q * q
    supp = [m for m in range(N) if u[m] and not zzero(dict(u[m]), p, N)]
    rows = sorted({m % q for m in supp})
    nonzero = len(supp) > 0
    Sv = S_apply(u, N)
    # target: i * q * u  with i = zeta^(N/4): exponent shift by N/4, scale q
    ok_eig = True
    for m in range(N):
        targ = {(e + N // 4) % N: q * c for e, c in u[m].items()}
        if not zzero(cadd(Sv[m], cneg(targ)), p, N): ok_eig = False
    out.append(f"  (2,{n}): nonzero {'YES' if nonzero else 'NO'}; support rows {rows} "
               f"(single row: {'YES' if len(rows) == 1 else 'NO'}); S u = i q u exact: "
               f"{'PASS' if ok_eig else 'FAIL'} (=> in E_i; single-row => rank-1 => PURE)")
    return nonzero and len(rows) == 1 and ok_eig and rows[0] == 2 ** (n - 1)

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("register", "run"):
        print(__doc__); return
    if sys.argv[1] == "register":
        print(open(REG, encoding="utf-8", errors="replace").read()); return
    out = ["### REGISTRATION CLOSED (data/b57_registration_2026-08-21.txt, banked before this run).",
           "### P1/P2 FROM THE BANK-READ DIMS (before any mechanization):"]
    dims = read_banked_dims()
    out.append(f"  bank-read cells: {sorted(dims.keys())}")
    ok12 = p1_p2(dims, out)
    out.append("\n### COMPONENT-3 DIM-LAW TARGETS vs THE BANKS (the longhand law's endpoints):")
    okL = dim_law_targets(dims, out)
    out.append("\n### P3 -- THE SEED CHAIN (u = delta_1 - delta_3 at (2,1); Su = 2i u longhand):")
    # the (2,1) seed: N = 4, u[1] = {0: 1}, u[3] = {0: -1}
    u = [dict() for _ in range(4)]; u[1] = {0: 1}; u[3] = {0: -1}
    ok0 = chain_check(u, 2, 1, out)  # row 1 at the boundary
    okP3 = True
    for lvl in (2, 3, 4):
        u = iota(u, 2, lvl - 1)
        new = " [THE NEW INSTANCE]" if lvl == 3 else " [re-verified against its bank]"
        okc = chain_check(u, 2, lvl, out)
        out[-1] += new
        okP3 = okP3 and okc
    out.append(f"\nP3 {'VERIFIED' if okP3 else 'FAILED'}: the iota-chain is a nonzero exact i-eigenvector with "
               f"single-row support (rows 2 -> 4 -> 8) at (2,2), (2,3), (2,4); the excess count "
               f"d_i - d_-i = 1 matches the ONE imported seed line at every place-2 cell (P2), and by the "
               f"purity-locus law the seed line is the canonical representative of the excess.")
    out.append(f"\nGATE FOR THE MECHANIZATION: P1/P2 {'CLEAR' if ok12 else 'BLOCKED'}; dim law {'EXACT' if okL else 'OPEN'}.")
    print("\n".join(out))

if __name__ == "__main__":
    main()
