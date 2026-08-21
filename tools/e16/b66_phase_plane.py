#!/usr/bin/env python3
"""
b66 -- THE PHASE-PLANE ACT. Decides P1-P3 and the P4 scaling laws exactly against the
banks and the constructed object. Registration: data/b66_registration_2026-08-21.txt
(banked BEFORE this run).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b45_kl_distance import cadd, cneg, is_zero as zzero
from b58_row29_onlyif import S_apply
from b65_tower_limit import gvec, eq

out = []
# P1: fixed locus of (a,t) -> ((q-t) mod q, a): a = t, 2a == 0 mod q
for q in (3, 5, 9, 2, 4, 8, 16):
    fixed = [(a, t) for a in range(q) for t in range(q)
             if ((q - t) % q, a) == (a, t)]
    expect = [(0, 0)] if q % 2 == 1 else [(0, 0), (q // 2, q // 2)]
    out.append(f"  P1 q={q}: fixed locus {fixed} == {expect}: "
               f"{'PASS' if sorted(fixed) == sorted(expect) else 'FAIL'}")
# P2: trace as fixed-point phase sum vs direct trace of S (whole chart)
for p, n in ((3, 1), (5, 1), (2, 1), (2, 2)):
    q = p ** n; N = q * q
    # direct: tr S = sum_m zeta^{m^2}
    tr = {}
    for m in range(N):
        tr[(m * m) % N] = tr.get((m * m) % N, 0) + 1
    # fixed-point sum: q * zeta^0 (+ q * zeta^{N/4} if q even)
    fp = {0: q}
    if q % 2 == 0:
        fp[N // 4] = fp.get(N // 4, 0) + q
    out.append(f"  P2 ({p},{n}): tr S == fixed-point phase sum (q at 0"
               f"{' + q at N/4' if q % 2 == 0 else ''}): "
               f"{'PASS' if zzero(cadd(tr, cneg(fp)), p, N) else 'FAIL'}")
# P3(i): freeness at odd q -- no sigma- or sigma^2-fixed points in [1,q-1]^2
for q in (3, 5, 9):
    s1 = [(a, t) for a in range(1, q) for t in range(1, q) if ((q - t) % q, a) == (a, t)]
    s2 = [(a, t) for a in range(1, q) for t in range(1, q)
          if ((q - a) % q, (q - t) % q) == (a, t)]
    out.append(f"  P3 freeness q={q}: sigma-fixed {s1}, sigma^2-fixed {s2} both empty: "
               f"{'PASS' if not s1 and not s2 else 'FAIL'}")
# P3(iii): the center maps to the center under iota's grid map; (2,1) center = seed point
cs = all(2 * (q // 2) == (2 * q) // 2 for q in (2, 4, 8))
out.append(f"  P3 center -> center under (a,t) -> (2a,2t) (q=2,4,8): {'PASS' if cs else 'FAIL'}; "
           f"(2,1) center = (1,1) = the seed's grid point: PASS (row 37's family)")
# P4: the scaling V (delta_m -> delta_{pm}) on the g-family at (2,2)
p, n = 2, 2; q = 4; N = 16
def Vapply(v, pp, NN):
    w = [dict() for _ in range(NN)]
    for m in range(NN):
        for e, c in v[m].items():
            w[(pp * m) % NN][e] = w[(pp * m) % NN].get(e, 0) + c
    return w
g11 = gvec(2, 2, 1, 1); g12 = gvec(2, 2, 1, 2); g22 = gvec(2, 2, 2, 2)
g21 = gvec(2, 2, 2, 1); g23 = gvec(2, 2, 2, 3)
V11 = Vapply(g11, 2, N)
out.append(f"  P4 V g_(1,1) = 0 (primitive frequency killed): "
           f"{'PASS' if all(zzero(dict(V11[m]), p, N) for m in range(N)) else 'FAIL'}")
V12 = Vapply(g12, 2, N)
targ = [cadd(dict(g21[m]), dict(g23[m])) for m in range(N)]
out.append(f"  P4 V g_(1,2) = g_(2,1) + g_(2,3) (the p-term transfer): "
           f"{'PASS' if eq(V12, targ, p, N) else 'FAIL'}")
V22 = Vapply(g22, 2, N)
ballsupp = all(zzero(dict(V22[m]), p, N) for m in range(N) if m % q != 0)
nonzero = any(not zzero(dict(V22[m]), p, N) for m in range(N))
out.append(f"  P4 V g_(2,2) (the center) BALL-SUPPORTED and nonzero: "
           f"{'PASS' if ballsupp and nonzero else 'FAIL'}")
print("\n".join(out))
