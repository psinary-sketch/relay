# b75 -- THE ADELIC CONSTRUCTION ACT's instrument (registration: data/b75_registration_2026-08-21.txt)
# The staged plane's finite part run at decidable core: gluing, H-COH-fin, the three D2
# candidates, Q-triviality. Integer and Z[i] arithmetic only.

def rec36(a): return (9*(a % 4) + 4*((7*a) % 9)) % 36
def rec100(a): return (25*(a % 4) + 4*((19*a) % 25)) % 100
out = []

# (C/G1) the gluing: negation respects the place split (the quarter-turn's only nontrivial part)
g = all(((36 - j) % 36) % 4 == (4 - j % 4) % 4 and ((36 - j) % 36) % 9 == (9 - j % 9) % 9 for j in range(36)) \
    and all(((100 - j) % 100) % 4 == (4 - j % 4) % 4 and ((100 - j) % 100) % 25 == (25 - j % 25) % 25 for j in range(100))
out.append(f"  C/G1 negation respects the place split (D = 36, 100): {'PASS' if g else 'FAIL'}")

# (D1) H-COH-fin: character additivity on the glued grid + level-extension transport
add36 = all((rec36(a) + rec36(b)) % 36 == (a + b) % 36 for a in range(36) for b in range(36))
ext = all(((4*a) % 16)*4 % 64 == (16*a) % 64 for a in range(4)) and all(((2*a) % 4)*4 % 16 == (8*a) % 16 for a in range(2))
out.append(f"  D1 character additivity over the full 36x36 square: {'PASS' if add36 else 'FAIL'}")
out.append(f"  D1 level-extension exponent transport (place-2 ladder): {'PASS' if ext else 'FAIL'}")

# (D2-leading) the stationary dimensions: Z[i] pairs; Son trace tuples per cell
def cmul(u, v): return (u[0]*v[0] - u[1]*v[1], u[0]*v[1] + u[1]*v[0])
def tup(q, p2):  # (tr M^0, tr M, tr Pi, tr M^3) on Son
    return [( (q-1)**2, 0), (0, 1) if p2 else (0, 0), (-1, 0) if p2 else (0, 0), (0, -1) if p2 else (0, 0)]
cells = {(2,1): tup(2, True), (3,1): tup(3, False), (2,2): tup(4, True), (5,1): tup(5, False),
         (2,3): tup(8, True), (3,2): tup(9, False), (2,4): tup(16, True), (3,3): tup(27, False)}
rosters = {"R1": ([(2,1),(3,1),(5,1)], 16), "R2": ([(2,2),(3,2)], 144), "R3": ([(2,2),(3,2),(5,1)], 2304),
           "R4": ([(2,3),(3,2),(5,1)], 12544), "R5": ([(2,1),(3,1)], 1)}
for name, (ros, banked) in rosters.items():
    tot = (0, 0)
    for k in range(4):
        prod = (1, 0)
        for c in ros: prod = cmul(prod, cells[c][k])
        tot = (tot[0] + prod[0], tot[1] + prod[1])
    ok = tot == (4*banked, 0)
    out.append(f"  D2-leading {name} {ros}: sum_k prod_v tr = {tot} == 4*{banked}: {'PASS' if ok else 'FAIL'}")

# (D2-alternate, AM-1) the visibility mechanism at the eight banked q
qs = [2, 3, 4, 5, 8, 9, 16, 27]
for q in qs:
    locus = [j for j in range(q) if (2*j) % q == 0]
    want = [0] if q % 2 == 1 else [0, q // 2]
    inv = (q % 2 == 0) or (((q + 1)//2)*2 % q == 1)
    out.append(f"  D2-alt q = {q}: diagonal 2-torsion {locus} == {want} and half-integrality law: "
               f"{'PASS' if locus == want and inv else 'FAIL'}")

# (D2-third, AM-2) global-minus-local at the six banked deficits (subtraction-free)
d1 = {(2,1): 0, (3,1): 1, (2,2): 2, (5,1): 4, (2,3): 12, (3,2): 16, (2,4): 56, (3,3): 169}
qq = {(2,1): 2, (3,1): 3, (2,2): 4, (5,1): 5, (2,3): 8, (3,2): 9, (2,4): 16, (3,3): 27}
defs = [([(2,1),(3,1)], 0), ([(2,1),(3,1),(5,1)], 11), ([(2,2),(3,2)], 126),
        ([(2,2),(3,2),(5,1)], 2282), ([(2,3),(3,2),(5,1)], 12512), ([(2,4),(3,3)], 37800)]
for ros, dv in defs:
    T0 = 1
    for c in ros: T0 *= (qq[c]-1)**2
    s = sum(d1[c] for c in ros)
    ok = T0 == 4*(s + dv)
    out.append(f"  D2-third {ros}: T0 = {T0} == 4*({s} + {dv}): {'PASS' if ok else 'FAIL'}")

# (D3) Q-triviality in action: finite product exponent + formal real exponent == 0 mod D
t36 = all((rec36(a) + (36 - a % 36)) % 36 == 0 for a in range(36))
t100 = all((rec100(a) + (100 - a % 100)) % 100 == 0 for a in range(100))
out.append(f"  D3 Q-triviality located (D = 36, 100, full ranges): {'PASS' if t36 and t100 else 'FAIL'}")
print("\n".join(out))
