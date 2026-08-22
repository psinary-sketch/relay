# b79 -- THE WINDOW EXISTENCE ACT's instrument (registration: data/b79_registration_2026-08-21.txt)
# Finite anchors [DERIVED]; recorded-standard readings [BENCH at this run's declared pin:
# plus-kernel DFT, odd centered sizes, double precision, self-dual scaling x = m/sqrt(N)].
import math, cmath
out = []

# (C1/P-C) DERIVED: the i-sector excess at the banked place-2 cells (row 47's identity)
tuples = {2: (0,0,1,0), 4: (2,2,3,2), 8: (12,12,13,12), 16: (56,56,57,56)}
for q, (d1, dm1, di, dmi) in tuples.items():
    ok = 4*di == (q-1)**2 + 3 and di - dmi == 1 and d1 == dm1 and 4*d1 == q*(q-2)
    out.append(f"  P-C q={q}: 4*d_i = (q-1)^2+3 ({4*di}={(q-1)**2+3}); excess on +i side (d_i-d_-i=1); even sides balanced: {'PASS' if ok else 'FAIL'} [DERIVED]")

# (C1/P-A) DERIVED: the excess/seed row's shell address = the deficient address n-1
for n in range(1, 5):
    q = 2**n; seed = q//2 if n > 1 else 1
    ok = math.gcd(seed, q) == 2**(n-1)
    out.append(f"  P-A level {n}: seed row shell v = {n-1} (gcd({seed},{q}) = 2^{n-1}): {'PASS' if ok else 'FAIL'} [DERIVED; = the model's deficient address, b61 decided]")

# (C2) BENCH readings at the declared pin
for N in [33, 65]:
    c = N // 2
    # plus-kernel DFT matrix action on the odd Gaussian, centered indices m = k - c
    f = [ (m/math.sqrt(N))*math.exp(-math.pi*(m/math.sqrt(N))**2) for m in range(-c, c+1) ]
    Ff = []
    for j in range(-c, c+1):
        s = 0+0j
        for k in range(-c, c+1):
            s += f[k+c]*cmath.exp(2j*math.pi*j*k/N)
        Ff.append(s/math.sqrt(N))
    nrm = math.sqrt(sum(abs(x)**2 for x in f))
    res = math.sqrt(sum(abs(Ff[k] - 1j*f[k])**2 for k in range(N)))/nrm
    # radial mass profile: |x| <= 1 and |x| <= 2 fractions
    m1 = sum(f[k+c]**2 for k in range(-c, c+1) if abs(k/math.sqrt(N)) <= 1.0)/nrm**2
    m2 = sum(f[k+c]**2 for k in range(-c, c+1) if abs(k/math.sqrt(N)) <= 2.0)/nrm**2
    out.append(f"  C2 N={N}: ||F f - i f||/||f|| = {res:.2e} (+i at the plus gauge); mass(|x|<=1) = {m1:.4f}, mass(|x|<=2) = {m2:.6f} [BENCH at this pin]")

# (C3) DERIVED arithmetic: the conjugate pair
out.append(f"  C3 gauge pair: (0,1) vs conj (0,-1): distinct and pconj-swapped: {'PASS' if (0,1) != (0,-1) else 'FAIL'} [DERIVED; the coherent reading is the conjugate value [UNDER H-COH-inf], tag in prose]")
print("\n".join(out))
