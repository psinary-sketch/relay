# b76 -- THE RADIALIZATION ACT's instrument (registration: data/b76_registration_2026-08-21.txt)
from math import gcd
out = []

# (P1) shell partitions + seed addresses (gcd = p^v law)
for (p, n) in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2)]:
    N = p**(2*n)
    shells = {}
    for m in range(N): shells.setdefault(gcd(m, N), 0); shells[gcd(m, N)] += 1
    sizes = [shells[p**v] for v in range(2*n)] + [1]
    out.append(f"  P1 ({p},{n}) N={N}: shell count {len(sizes)} == {2*n+1}; sizes {sizes}: "
               f"{'PASS' if len(sizes) == 2*n+1 and sum(sizes) == N else 'FAIL'}")
for n in range(1, 5):
    q = 2**n; seed = q // 2 if n > 1 else 1
    ok = gcd(seed, q) == 2**(n-1)
    out.append(f"  P1 seed address level {n}: gcd({seed},{q}) = {gcd(seed,q)} == 2^{n-1}: {'PASS' if ok else 'FAIL'}")
# boundary-index from R's side: image of doubling misses primitives, fixes zero
for N in [4, 16, 64]:
    miss = all(((2*m) % N) % 2 == 0 for m in range(N))
    out.append(f"  P1 boundary index at N={N}: primitive shell off the doubling image AND zero terminal: "
               f"{'PASS' if miss and (2*0) % N == 0 else 'FAIL'}")

# (P2) the gcd intertwining law, full ranges
for N in [4, 16, 64, 256]:
    ok = all(gcd((2*m) % N, N) == min(2*gcd(m, N), N) for m in range(N))
    out.append(f"  P2 intertwining gcd law at N={N} (full range): {'PASS' if ok else 'FAIL'}")
# the ball-boundary transition = the deficient/seed shell
for n in [1, 2, 3]:
    N = 4**n; ball = 2**n
    trans = sorted(set(gcd(m, N) for m in range(N) if gcd(m, N) < ball and (gcd((2*m) % N, N) >= ball or (2*m) % N == 0)))
    ok = trans == [2**(n-1)]
    out.append(f"  P2 ball-boundary transition at level {n}: shells {trans} == [2^{n-1}]: {'PASS' if ok else 'FAIL'}")

# (P3) theta by shells at (2,1), (3,1), (2,2) -- exact cyclotomic coordinates
def theta_shells(p, n):
    N = p**(2*n); acc = {}
    for m in range(N):
        v = 0; mm = m
        if m == 0: v = 2*n
        else:
            while mm % p == 0: mm //= p; v += 1
        acc.setdefault(v, []).append((m*m) % N)
    return acc
# (2,1): Z[i] pairs
P = {0:(1,0),1:(0,1),2:(-1,0),3:(0,-1)}
sh = theta_shells(2,1); tot=(0,0); rep=[]
for v in sorted(sh):
    s=(0,0)
    for e in sh[v]: s=(s[0]+P[e%4][0], s[1]+P[e%4][1])
    rep.append((v,s)); tot=(tot[0]+s[0], tot[1]+s[1])
out.append(f"  P3 (2,1) shells {rep} total {tot} == (2,2)=q(1+i): {'PASS' if tot==(2,2) else 'FAIL'}")
# (3,1): mono9 six-coords
def m9(e):
    b=[0]*6; e%=9
    if e<6: b[e]=1
    else: t=e-6; b[t]-=1; b[t+3]-=1
    return b
sh = theta_shells(3,1); tot=[0]*6; rep=[]
for v in sorted(sh):
    s=[0]*6
    for e in sh[v]:
        for i2,c in enumerate(m9(e)): s[i2]+=c
    rep.append((v,tuple(s)))
    for i2 in range(6): tot[i2]+=s[i2]
ok = tot==[3,0,0,0,0,0] and rep[0][1]==(0,)*6
out.append(f"  P3 (3,1) primitive shell silent, total {tuple(tot)} == 3=q: {'PASS' if ok else 'FAIL'}")
# (2,2): mono16 eight-coords (x^8 = -1)
def m16(e):
    b=[0]*8; e%=16
    if e<8: b[e]=1
    else: b[e-8]=-1
    return b
sh = theta_shells(2,2); tot=[0]*8; rep=[]
for v in sorted(sh):
    s=[0]*8
    for e in sh[v]:
        for i2,c in enumerate(m16(e)): s[i2]+=c
    rep.append((v,tuple(s)))
    for i2 in range(8): tot[i2]+=s[i2]
ok = tot==[4,0,0,0,4,0,0,0] and rep[0][1]==(0,)*8
out.append(f"  P3 (2,2) primitive shell silent, shells-by-v {[(v,s) for v,s in rep]}, total {tuple(tot)} == 4+4i=q(1+i): {'PASS' if ok else 'FAIL'}")

# (P4) the factorization: gcd multiplicativity across the place split
for (D, q1, q2) in [(36, 4, 9), (100, 4, 25)]:
    ok = all(gcd(j, D) == gcd(j % q1, q1)*gcd(j % q2, q2) for j in range(D))
    out.append(f"  P4 radial coordinate factors through the place split at D={D}: {'PASS' if ok else 'FAIL'}")
print("\n".join(out))
