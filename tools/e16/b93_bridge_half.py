# b93 -- THE BRIDGE-HALF ACT -- instrument: numeric cross-check of the four
# planned kernel terminals K1-K4 (BridgeShadow, row 62) BEFORE the Lean decide.
# K1/K2: the F -> F^3 image law (the conjugated completed square) at N = 9, 25.
# K3: the conjugated Gauss values equal the originals (+q at the odd cells).
# K4: the double-transform round trip at N = 9 (the |G|^2 = N shadow).
# Registration: data/b93_registration_2026-08-22.txt. Exact arithmetic lives in
# the kernel (decide); this is the cross-check at 1e-9.

import cmath

TOL = 1e-9
def z(N, e):
    return cmath.exp(2j * cmath.pi * (e % N) / N)

def close(a, b):
    return abs(a - b) < TOL

fails = []

# K1: N = 9, G = 3 -- for every k: sum_m zeta^{-(m^2+2mk)} = zeta^{+k^2} * 3
for k in range(9):
    lhs = sum(z(9, -(m*m + 2*m*k)) for m in range(9))
    rhs = 3 * z(9, k*k)
    if not close(lhs, rhs):
        fails.append(("K1", k, lhs, rhs))

# K2: N = 25, G = 5
for k in range(25):
    lhs = sum(z(25, -(m*m + 2*m*k)) for m in range(25))
    rhs = 5 * z(25, k*k)
    if not close(lhs, rhs):
        fails.append(("K2", k, lhs, rhs))

# K3: conjugated Gauss values: sum_m zeta^{-m^2} = q
for N, q in ((9, 3), (25, 5)):
    lhs = sum(z(N, -(m*m)) for m in range(N))
    if not close(lhs, q):
        fails.append(("K3", N, lhs, q))

# K4: round trip at N = 9: for every j, sum_k sum_m zeta^{m^2+2mk+2kj} = 9*zeta^{j^2}
for j in range(9):
    lhs = sum(z(9, m*m + 2*m*k + 2*k*j) for k in range(9) for m in range(9))
    rhs = 9 * z(9, j*j)
    if not close(lhs, rhs):
        fails.append(("K4", j, lhs, rhs))

if fails:
    print("FAIL:", len(fails))
    for f in fails:
        print(f)
else:
    print("K1 (mirror law N=9, all k): PASS")
    print("K2 (mirror law N=25, all k): PASS")
    print("K3 (mirror Gauss values = +q at 9, 25): PASS")
    print("K4 (round trip N=9, all j -- |G|^2 = N shadow): PASS")
    print("ALL FOUR CROSS-CHECKS PASS at 1e-9")
