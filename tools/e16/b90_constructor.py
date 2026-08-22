# b90 -- THE CONSTRUCTOR ACT's instrument (registration: data/b90_registration_2026-08-22.txt)
from math import gcd
out = []

# Z[zeta_25] twenty-coordinates: Phi_25 = x^20 + x^15 + x^10 + x^5 + 1
def m25(e):
    e %= 25; b = [0]*20
    if e < 20: b[e] = 1
    else:
        k = e - 20  # x^(20+k) = -(x^(15+k) + x^(10+k) + x^(5+k) + x^k)
        for off in (15, 10, 5, 0): b[off + k] -= 1
    return b
def vadd(u, v): return [a + b for a, b in zip(u, v)]

# AG-1 extension at (5,1): point-count identity + total = 5 = q
direct = [0]*20
for m in range(25): direct = vadd(direct, m25((m*m) % 25))
counts = [sum(1 for m in range(25) if (m*m) % 25 == r) for r in range(25)]
weighted = [0]*20
for r in range(25):
    for i, c in enumerate(m25(r)): weighted[i] += counts[r]*c
tot_ok = direct == weighted and direct == [5] + [0]*19 and sum(counts) == 25
out.append(f"  AG-1 (5,1): exponent fold == count-weighted; total = 5*e0 = q: {'PASS' if tot_ok else 'FAIL'} [DERIVED, decidable] {direct[:6]}...")

# AG-3 extension at N = 25: sum_m z^(m^2+2mk) = z^(-k^2) * G, G = 5*e0
ok3 = True
for k in range(25):
    lhs = [0]*20
    for m in range(25): lhs = vadd(lhs, m25((m*m + 2*m*k) % 25))
    rhs = [5*c for c in m25((25 - (k*k) % 25) % 25)]
    if lhs != rhs: ok3 = False; out.append(f"    k={k} MISMATCH")
out.append(f"  AG-3 N=25, every k: completed-square law: {'PASS' if ok3 else 'FAIL'} [DERIVED, decidable]")

# AG-6: the silhouette exam -- six rosters, q's from the cusp table
cusp = {(2,1):2,(3,1):3,(2,2):4,(5,1):5,(2,3):8,(3,2):9,(2,4):16,(3,3):27}
d1 = {(2,1):0,(3,1):1,(2,2):2,(5,1):4,(2,3):12,(3,2):16,(2,4):56,(3,3):169}
rosters = [([(2,1),(3,1)],0), ([(2,1),(3,1),(5,1)],11), ([(2,2),(3,2)],126),
           ([(2,2),(3,2),(5,1)],2282), ([(2,3),(3,2),(5,1)],12512), ([(2,4),(3,3)],37800)]
for ros, dv in rosters:
    T0 = 1
    for c in ros: T0 *= (cusp[c]-1)**2
    s = sum(d1[c] for c in ros)
    ok = T0 == 4*(s + dv)
    out.append(f"  AG-6 {ros}: prod(cusp-1)^2 = {T0} == 4*({s}+{dv}): {'PASS' if ok else 'FAIL'} [the object's boundary data feeding the exam; DERIVED, decidable]")

# Strikeable 4: N5's vector identity at (2,2) and (2,1) -- positions + gcd shells
def Vvec(coeffs, N):  # V doubles positions
    outv = [0]*N
    for m, c in enumerate(coeffs): outv[(2*m) % N] += c
    return outv
def Rvec(coeffs, N, top):  # shell sums by gcd exponent
    sh = [0]*(top+1)
    for m, c in enumerate(coeffs):
        if m == 0: sh[top] += c
        else:
            g = gcd(m, N); v = 0
            while g % 2 == 0: g //= 2; v += 1
            sh[v] += c
    return sh
# (2,2): N=16, shells v=0..4 (top=4)
g20 = [0]*16
for b in range(4): g20[(2+4*b) % 16] += 1
g22 = [0]*16
for b in range(4): g22[(2+4*b) % 16] += (1 if b % 2 == 0 else -1)  # i^{2b} = (-1)^b
v20 = Vvec(g20, 16); v22 = Vvec(g22, 16)
r20 = Rvec(v20, 16, 4); r22 = Rvec(v22, 16, 4)
ok4a = v22 == [0,0,0,0,2,0,0,0,0,0,0,0,-2,0,0,0] and r20 == [0,0,4,0,0] and r22 == [0,0,0,0,0]
out.append(f"  N5 (2,2): V g22 = 2d4 - 2d12 (the b66 banked value) {v22[4]},{v22[12]}; R(V g20) = 4 e2 = q*e_n {r20}; R(V g22) = 0 {r22}: {'PASS' if ok4a else 'FAIL'} [DERIVED, decidable]")
# (2,1): N=4, shells v=0..2
g10 = [0]*4
for b in range(2): g10[(1+2*b) % 4] += 1
g11 = [0]*4
for b in range(2): g11[(1+2*b) % 4] += (1 if b == 0 else -1)  # i^{2b}? omega = zeta_4^... at q=2: omega = -1: (-1)^b
v10 = Vvec(g10, 4); v11 = Vvec(g11, 4)
r10 = Rvec(v10, 4, 2)
ok4b = v10 == [0,0,2,0] and r10 == [0,2,0] and v11 == [0,0,0,0]
out.append(f"  N5 (2,1): V g10 = 2d2, R = 2 e1 = q*e_n {r10}; V g11 = 0 (the primitive kill) {v11}: {'PASS' if ok4b else 'FAIL'} [DERIVED, decidable]")
print("\n".join(out))
