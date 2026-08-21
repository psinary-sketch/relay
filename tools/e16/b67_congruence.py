#!/usr/bin/env python3
"""
b67 -- THE CONGRUENCE ACT, component 1. The Lefschetz family decided at every banked
cell: each power's direct trace vs its fixed-locus phase sum; the swapped pair; the
dims-from-the-center endpoint vs the banked tuples. Registration:
data/b67_registration_2026-08-21.txt (banked BEFORE this run).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b45_kl_distance import cadd, cneg, is_zero as zzero

CELLS = [(2,1),(3,1),(2,2),(5,1),(2,3),(3,2),(2,4),(3,3)]
DIMS = {(2,1):(0,0,1,0),(3,1):(1,1,1,1),(2,2):(2,2,3,2),(5,1):(4,4,4,4),
        (2,3):(12,12,13,12),(3,2):(16,16,16,16),(2,4):(56,56,57,56),(3,3):(169,169,169,169)}

out = []
allpass = True
for (p, n) in CELLS:
    q = p ** n; N = q * q
    # direct power-traces of the permutation-with-phase m -> ... : use matrix-free sums:
    # tr M^0 = N; tr S = sum zeta^{m^2}; tr S^2 = q^2 * #fix(Pi); tr S^3 via S^3 = q^2 Pi S
    tr1 = {}
    for m in range(N): tr1[(m*m) % N] = tr1.get((m*m) % N, 0) + 1     # tr S
    trPi = sum(1 for m in range(N) if (2*m) % N == 0)                  # tr Pi (direct count)
    # tr(Pi S) = sum_m (Pi S)(m,m) = sum_m S(-m, m)-entry = sum zeta^{-m^2}
    tr3 = {}
    for m in range(N): tr3[(-(m*m)) % N] = tr3.get((-(m*m)) % N, 0) + 1  # tr Pi S = tr S^3 / q^2
    # fixed-phase sums (normalized M-level): M: origin 1 (+ center i at p=2)
    fpM = {0: 1}
    if p == 2: fpM[N // 4] = fpM.get(N // 4, 0) + 1
    fpM3 = {0: 1}
    if p == 2: fpM3[(N - N // 4) % N] = fpM3.get((N - N // 4) % N, 0) + 1
    fpPi = 1 if p != 2 else 2
    # compare: tr S = q * fpM ; tr Pi = fpPi ; tr(PiS) = q * fpM3
    okM = zzero(cadd(dict(tr1), cneg({e: q * c for e, c in fpM.items()})), p, N)
    okPi = (trPi == fpPi)
    okM3 = zzero(cadd(dict(tr3), cneg({e: q * c for e, c in fpM3.items()})), p, N)
    ok0 = True  # tr 1 = N = whole grid count q^2 trivially
    # dims from the center (D5)
    if p == 2:
        d_other = ((q-1)**2 - 1) // 4; d_i = ((q-1)**2 + 3) // 4
        dims = (d_other, d_other, d_i, d_other)
    else:
        d = (q-1)**2 // 4; dims = (d, d, d, d)
    okD = (dims == DIMS[(p, n)])
    ok = okM and okPi and okM3 and ok0 and okD
    allpass = allpass and ok
    out.append(f"  ({p},{n}) q={q}: M {'PASS' if okM else 'FAIL'}; Pi {'PASS' if okPi else 'FAIL'} "
               f"(direct {trPi} = phase sum {fpPi}); M^3 {'PASS' if okM3 else 'FAIL'}; "
               f"dims-from-center {dims} vs banked {DIMS[(p,n)]}: {'PASS' if okD else 'FAIL'}")
# P2: the swapped pair at p = 2 cells
for q in (2, 4, 8, 16):
    a, b = (q // 2, 0), (0, q // 2)
    sig = lambda v: ((q - v[1]) % q, v[0])
    ok2 = (sig(a) == b and sig(b) == a and sig(sig(a)) == a and sig(a) != a)
    allpass = allpass and ok2
    out.append(f"  P2 q={q}: ({q//2},0) <-> (0,{q//2}) a sigma-2-cycle, sigma^2-fixed, not sigma-fixed: "
               f"{'PASS' if ok2 else 'FAIL'}")
out.append(f"\nVERDICT: {'ALL PASS -- the character-average law is a fixed-point theorem in full at every banked cell' if allpass else 'A FAILURE ABOVE'}")
print("\n".join(out))
