# b85 -- THE THETA-BRIDGE CONTINUATION's instrument (registration: data/b85_registration_2026-08-22.txt)
# Component 2's finite decidable checks. Exact cyclotomic coordinates only.
out = []

# (D1) the point-count identity at N = 9, 16: exponent fold == count-weighted assembly
def m9(e):
    b=[0]*6; e%=9
    if e<6: b[e]=1
    else: t=e-6; b[t]-=1; b[t+3]-=1
    return b
def m16(e):
    b=[0]*8; e%=16
    if e<8: b[e]=1
    else: b[e-8]=-1
    return b
for N, mono, dim in [(9, m9, 6), (16, m16, 8)]:
    direct=[0]*dim
    for m in range(N):
        for i,c in enumerate(mono((m*m)%N)): direct[i]+=c
    counts=[sum(1 for m in range(N) if (m*m)%N==r) for r in range(N)]
    weighted=[0]*dim
    for r in range(N):
        for i,c in enumerate(mono(r)): weighted[i]+=counts[r]*c
    ok = direct==weighted and sum(counts)==N
    out.append(f"  D1 N={N}: exponent fold == point-count assembly ({direct}); total counts = N: {'PASS' if ok else 'FAIL'} [DERIVED, decidable]")

# (D2) the cusp count c_N(0) = q at the eight banked cells
for (p,n) in [(2,1),(3,1),(2,2),(5,1),(2,3),(3,2),(2,4),(3,3)]:
    N=p**(2*n); q=p**n
    c0=sum(1 for m in range(N) if (m*m)%N==0)
    out.append(f"  D2 ({p},{n}) N={N}: c_N(0) = {c0} == q = {q}: {'PASS' if c0==q else 'FAIL'} [DERIVED, decidable]")

# (D3) the transformation law's finite shadow at N = 9: sum_m z^(m^2+2mk) = z^(-k^2) * G, G = 3
ok3=True
for k in range(9):
    lhs=[0]*6
    for m in range(9):
        for i,c in enumerate(m9((m*m+2*m*k)%9)): lhs[i]+=c
    rhs=[3*c for c in m9((9-(k*k)%9)%9)]
    if lhs!=rhs: ok3=False; out.append(f"  D3 k={k}: MISMATCH {lhs} vs {rhs}")
out.append(f"  D3 N=9, all k: sum_m z^(m^2+2mk) == z^(-k^2)*G (G = 3, banked): {'PASS' if ok3 else 'FAIL'} [DERIVED, decidable; the odd-cell functional-equation shadow]")
print("\n".join(out))
