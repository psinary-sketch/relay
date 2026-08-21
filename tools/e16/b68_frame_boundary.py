#!/usr/bin/env python3
"""
b68 -- THE FRAME-BOUNDARY EXTENSIONS. The nativity arithmetic; the u-line refusal
witnesses at the smallest cell of each parity; the limit-frame exponent arithmetic.
Registration: data/b68_registration_2026-08-21.txt (banked BEFORE this run).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b45_kl_distance import cadd, cneg, is_zero as zzero

out = []
# D1: nativity arithmetic
nat = (16 % 8 == 0 and 64 % 8 == 0 and 256 % 8 == 0 and 4 % 8 != 0
       and all((4 * q * q) % 8 == 4 for q in (3, 5, 9, 27)))
out.append(f"  D1 nativity: 8 | N at place-2 depth >= 2; 8 !| 4; 4q^2 == 4 mod 8 at odd q: {'PASS' if nat else 'FAIL'}")
# D3: u-line witnesses
for (p, n) in ((2, 1), (3, 1)):
    q = p ** n; N = q * q
    u = [({0: 1} if m % q == 0 else {}) for m in range(N)]
    Su = [dict() for _ in range(N)]
    for m in range(N):
        for e, c in u[m].items():
            for mp in range(N):
                Su[mp][(e + m * mp) % N] = Su[mp].get((e + m * mp) % N, 0) + c
    okS = all(zzero(cadd(dict(Su[m]), cneg({e: q * c for e, c in u[m].items()})), p, N) for m in range(N))
    okPi = all(u[(N - m) % N] == u[m] for m in range(N))
    okNe = any(u[m] for m in range(N))
    out.append(f"  D3 ({p},{n}): S u = q u exact: {'PASS' if okS else 'FAIL'}; Pi u = u: "
               f"{'PASS' if okPi else 'FAIL'}; u nonzero (u /= -u): {'PASS' if okNe else 'FAIL'}")
# D2: limit-frame exponent arithmetic
lim = ((16//8)*4 == 64//8 and (64//8)*4 == 256//8 and
       (16//8)*2 == 16//4 and (64//8)*2 == 64//4 and (256//8)*2 == 256//4)
out.append(f"  D2 limit frame: N/8 -> p^2 N/8 = N+/8 and (N/8)*2 = N/4 (zeta_8^2 = i in exponents): {'PASS' if lim else 'FAIL'}")
print("\n".join(out))
