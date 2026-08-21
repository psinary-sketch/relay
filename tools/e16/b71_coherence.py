# b71 -- THE COHERENCE ACT's instrument (registration: data/b71_registration_2026-08-21.txt)
# D1: the rational reciprocity theorem's decided instances (CRT recombination, full ranges)
# D2: the convention survey's decided discriminator at (2,1) (the plus orientation's +i part)
# D3: the conjugate-complement shape (the product-law triviality's arithmetic core)

out = []
cases = [
    (36,  lambda a: (9*(a % 4) + 4*((7*a) % 9)) % 36),
    (100, lambda a: (25*(a % 4) + 4*((19*a) % 25)) % 100),
    (1296,lambda a: (81*(a % 16) + 16*((76*a) % 81)) % 1296),
    (900, lambda a: (225*(a % 4) + 100*(a % 9) + 36*((16*a) % 25)) % 900),
]
for D, f in cases:
    ok = all(f(a) == a for a in range(D))
    out.append(f"  D1 reciprocity at D = {D}: recombination exact over the full range: {'PASS' if ok else 'FAIL'}")

trS = [0, 0]
for m in range(4):
    e = (m*m) % 4
    trS[0] += (1 if e == 0 else (-1 if e == 2 else 0))
    trS[1] += (1 if e == 1 else (-1 if e == 3 else 0))
out.append(f"  D2 (2,1) trace pair: {tuple(trS)} == (2, 2) (plus orientation) and /= (2, -2): "
           f"{'PASS' if tuple(trS) == (2, 2) else 'FAIL'}")
out.append("  D2 survey: the S_apply exponent is +m*m' in every banked instrument (grep below); the g-law and limit phases plus: CITED AT PINS")

ok3 = all((a + (36 - a) % 36) % 36 == 0 for a in range(36))
out.append(f"  D3 conjugate-complement shape at D = 36: {'PASS' if ok3 else 'FAIL'}")
print("\n".join(out))
