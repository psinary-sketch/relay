# b97 -- THE COMPLEX-EXTENSION BUILD ACT -- instrument. Registration:
# data/b97_registration_2026-08-22.txt (the probe point z0 = 1 + i/2 and the
# derived interval FIXED there before this ran). Checks: the probe sum against
# the derived interval [e^-pi, e^-pi + 2 e^-9pi] for -Im; Schwarz covariance at
# the probe; the phase pattern; K1-K4 numeric cross-checks before the Lean
# decides. N-EXT-2 honored: no boundary point touched (Re z = 1 throughout).

import cmath, math

TOL = 1e-12
fails = []

# the probe (P1): psi(z) = sum_{n>=1} e^{-pi n^2 z}, truncated with rigorous tail
z0 = 1 + 0.5j
N_TRUNC = 40  # tail < e^{-pi*1600}, far below any tolerance
psi_z0 = sum(cmath.exp(-cmath.pi * n * n * z0) for n in range(1, N_TRUNC + 1))
im = psi_z0.imag
lo = math.exp(-math.pi)                      # derived lower endpoint for -Im
hi = math.exp(-math.pi) + 2 * math.exp(-9 * math.pi)  # derived upper endpoint
if not (lo - TOL <= -im <= hi + TOL):
    fails.append(("P1-interval", im, lo, hi))

# Schwarz covariance at the probe: psi(conj z0) == conj(psi(z0))
psi_zbar = sum(cmath.exp(-cmath.pi * n * n * z0.conjugate()) for n in range(1, N_TRUNC + 1))
if abs(psi_zbar - psi_z0.conjugate()) > TOL:
    fails.append(("P1-schwarz", psi_zbar, psi_z0.conjugate()))

# the phase pattern: term phase at z0 is exactly -i for n odd, real for n even
for n in range(1, 64):
    ph = cmath.exp(-1j * cmath.pi * n * n / 2)
    if n % 2 == 1 and abs(ph - (-1j)) > TOL:
        fails.append(("phase-odd", n, ph))
    if n % 2 == 0 and abs(ph.imag) > TOL:
        fails.append(("phase-even", n, ph))

# K1: n odd => n^2 % 8 = 1; n even => n^2 % 4 = 0 (range 256)
for n in range(256):
    if n % 2 == 1 and (n * n) % 8 != 1:
        fails.append(("K1-odd", n))
    if n % 2 == 0 and (n * n) % 4 != 0:
        fails.append(("K1-even", n))

# K2: witness exponents {2,6}; conj e -> (16-e)%16; doubling swaps {4,12}; 4th powers at 8
k2 = ((16 - 2) % 16 == 14 and (16 - 6) % 16 == 10
      and (2 * 2) % 16 == 4 and (2 * 6) % 16 == 12
      and (2 * 14) % 16 == 12 and (2 * 10) % 16 == 4
      and all((4 * e) % 16 == 8 for e in (2, 6, 14, 10)))
if not k2:
    fails.append(("K2",))

# K3: product-1 mirror relation; the zeta_8 anchor exponent
k3 = ((2 + 14) % 16 == 0 and (6 + 10) % 16 == 0 and 16 // 8 == 2)
if not k3:
    fails.append(("K3",))

# K4: level-16 gaussian fold and its conjugate, in C (numeric mirror of the
# exact Z[zeta_16] kernel statement): fold = 4(1+i), conj fold = 4(1-i)
zeta16 = cmath.exp(2j * cmath.pi / 16)
fold = sum(zeta16 ** ((m * m) % 16) for m in range(16))
cfold = sum(zeta16 ** ((16 - (m * m) % 16) % 16) for m in range(16))
if abs(fold - (4 + 4j)) > TOL or abs(cfold - (4 - 4j)) > TOL:
    fails.append(("K4", fold, cfold))

if fails:
    print("FAIL:", len(fails))
    for f in fails:
        print(f)
else:
    print(f"P1 probe: Im psi(1+i/2) = {im:.12f} inside the derived interval")
    print(f"          [-{hi:.12f}, -{lo:.12f}] -- NONZERO, sign minus, as derived")
    print("P1 Schwarz covariance at the probe: PASS at 1e-12")
    print("phase pattern (odd -> -i exactly; even -> real): PASS")
    print("K1 (mod-8/mod-4 square pattern, n < 256): PASS")
    print("K2 (conjugation swaps the witness square-classes; 4th powers at -1): PASS")
    print("K3 (product-1 mirror relation; the zeta_8 anchor exponent): PASS")
    print(f"K4 (level-16 fold 4(1+i) vs conjugate 4(1-i)): PASS")
    print("ALL CHECKS PASS")
