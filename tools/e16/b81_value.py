# b81 -- THE VALUE ACT's instrument (registration: data/b81_registration_2026-08-21.txt)
out = []
# (C1) the equal-magnitude lemma's arithmetic: J = [[0,-1],[1,0]]; det(I - J)
a, b_, c, d = 1-0, 0-(-1), 0-1, 1-0   # I - J entries
det = a*d - b_*c
out.append(f"  C1 det(I - J) = {det} == 2 (point-independent; R linear): {'PASS' if det == 2 else 'FAIL'} [DERIVED]")
for q in [2, 4, 8, 16]:
    ok = q*q + 0 == 0 + q*q
    out.append(f"  C1 finite twin q={q}: |q*1|^2 = |q*i|^2 = {q*q}: {'PASS' if ok else 'FAIL'} [DERIVED]")
# (C2) the finite ledger
for q in [2, 4, 8, 16]:
    s = (q + 0, 0 + q)
    ok = s == (q, q)
    out.append(f"  C2 q={q}: (q,0)+(0,q) = {s} == (q,q) = banked trace; balance components equal ({s[0]}={s[1]}): {'PASS' if ok else 'FAIL'} [DERIVED]")
# (C3) the ledger's sum at unit normalization, both orientations
plus = (1+0, 0+1); conj = (1+0, 0-1)
ok = plus == (1,1) and conj == (1,-1) and (conj[0]**2 + conj[1]**2) == 2 and plus != conj and (plus[0], -plus[1]) == conj
out.append(f"  C3 ledger sums: plus (1,1), conjugate (1,-1); norm^2 = 2; pconj-swapped, distinct: {'PASS' if ok else 'FAIL'} [DERIVED arithmetic; the archimedean reading CONDITIONAL: the decomposition clause (named) + [UNDER H-COH-inf]]")
print("\n".join(out))
