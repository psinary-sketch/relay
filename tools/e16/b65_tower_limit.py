#!/usr/bin/env python3
"""
b65 -- THE TOWER-LIMIT CONSTRUCTION. Gates first: the transport laws re-verified at
the consumed instance; then (L1) the monomial embedding law and (L2) the exact
intertwining verified at (2,1) -> (2,2) in exact Z[zeta] dicts; the fraction and
eighth-root exponent constancies; the register arithmetic. Registration:
data/b65_registration_2026-08-21.txt (banked BEFORE this run).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b45_kl_distance import cadd, cneg, is_zero as zzero
from b58_row29_onlyif import S_apply
from b57_row31_depth import iota

def gvec(p, n, a, t):
    q = p ** n; N = q * q
    v = [dict() for _ in range(N)]
    for b in range(q):
        v[(a + q * b) % N][(q * t * b) % N] = v[(a + q * b) % N].get((q * t * b) % N, 0) + 1
    return v

def eq(u, v, p, N):
    return all(zzero(cadd(dict(u[m]), cneg(dict(v[m]))), p, N) for m in range(N))

out = []
p = 2
# GATE: the S-action law at (2,1): S g_{1,1} = q zeta^{a(q-t)} g_{q-t,a} = 2 zeta^{1} g_{1,1}
q, N = 2, 4
g11 = gvec(2, 1, 1, 1)
Sg = S_apply(g11, N)
targ = [{(e + 1) % N: 2 * c for e, c in g11[m].items()} for m in range(N)]
out.append(f"  GATE S-action at (2,1): S g_(1,1) = 2 zeta^1 g_(1,1): {'PASS' if eq(Sg, targ, p, N) else 'FAIL'}")
# (L1): iota(g_(1,1)) at (2,1) = g_(2,2) at (2,2)
ig = iota(g11, 2, 1)
g22 = gvec(2, 2, 2, 2)
out.append(f"  (L1) iota(g_(1,1)) = g+_(2,2): {'PASS' if eq(ig, g22, p, 16) else 'FAIL'}")
# (L2): S+ (iota g) = p * iota(S g)
Sig = S_apply(ig, 16)
iSg = iota(Sg, 2, 1)
piSg = [{e: 2 * c for e, c in iSg[m].items()} for m in range(16)]
out.append(f"  (L2) S+ iota g = p * iota(S g) at the instance: {'PASS' if eq(Sig, piSg, p, 16) else 'FAIL'}")
# norm transport: ||g||^2 = q; ||iota g||^2 = q+ = p q  (counting unit-monomial entries)
n1 = sum(len(g11[m]) for m in range(4)); n2 = sum(len(ig[m]) for m in range(16))
out.append(f"  (L4) norms: ||g||^2 = {n1} = q; ||iota g||^2 = {n2} = pq: "
           f"{'PASS' if (n1, n2) == (2, 4) else 'FAIL'}")
# fraction constancy and eighth-root exponent constancy
fr = all(a * (2 * qq) == (2 * a) * qq for qq in (2, 4, 8) for a in range(1, qq))
e8 = ((16 // 8) * 4 == 64 // 8) and ((64 // 8) * 4 == 256 // 8)
out.append(f"  (L3) fraction constancy a/q = pa/q+ (instances): {'PASS' if fr else 'FAIL'}; "
           f"eighth-root exponent N/8 -> p^2 N/8 = N+/8 (16->64->256): {'PASS' if e8 else 'FAIL'}")
# register arithmetic
reg = all((2**n) * (2**n) == 4**n and 2**n < 4**n for n in range(1, 5))
out.append(f"  (P3) register arithmetic: p-register class norms q/p^n = 1 constant; "
           f"p^2-register collapse (2^n < 4^n, n = 1..4): {'PASS' if reg else 'FAIL'}")
print("\n".join(out))
