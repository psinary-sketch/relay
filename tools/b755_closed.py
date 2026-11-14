# -*- coding: utf-8 -*-
"""b755 Component 3, (R365)(4)(a): THE CLOSED FORM AT CLASS NUMBER 3, written by the seat from the statement alone (data/b753_registrations.txt
:67-:69, (a) as (R363)(4) words it) and committed before its run ((S3), data/b754_rules.txt (3)).

THE STATEMENT: at class number 3, log(Z_Q0/2) = log zeta_K + log((1 + 2 exp(-3T))/3), T the sum of p^(-ks)/k over the non-principal primes p
and the k not divisible by 3, expanding as log zeta_K - 2T + T^2 + T^3/3 - T^4/4 - ...; against the direct b(n) at -23 for n <= 3000,
mismatches 0, after the direct route reproduced data/b750_cq_sign.txt :39. (R365)(4)(a) adds -31 and the plant: the k divisible by 3 kept.

THE ROUTES, every value an exact rational (fractions.Fraction), n <= N = 3000:
  DIRECT: a(n) = r_Q0(n)/2 by enumeration of x^2 + xy + c y^2 = n; b = log of the Dirichlet series 1 + SUM a(n) n^-s by the Omega derivation,
          Omega(n) b(n) = Omega(n) a(n) - SUM_{d | n, 1 < d < n} Omega(d) b(d) a(n/d) (data/b718_derivation.txt :16's route, written again here).
  CLOSED: log zeta_K from the primes' kinds (the Kronecker symbol): a split p gives 2/m at p^m, a ramified p 1/m at p^m, an inert p 2/m at
          p^m for m even; T from the split primes the principal form does not represent (r_Q0(p) = 0), 1/k at p^k for k not divisible by 3;
          E = exp(-3T) by the same derivation (Omega(n) E(n) = SUM_{d | n, d > 1} Omega(d) G(d) E(n/d), G = -3T); then
          log((1 + 2E)/3) by the log route; the closed b the sum of the two logs.
  PLANT ('plant'): T with every k, the k divisible by 3 kept; the agreement must break.
CONTROLS, printed before any row: (K1) the direct route at -23 reproduces data/b750_cq_sign.txt :39 (negative 102, least negative n 48,
  exactly zero 2498, positive 399, the largest |cQ| = |b(n)| log n 190.565466363 at n = 2808); (K2) the statement's expansion, the Taylor
  coefficients of log((1 + 2 exp(-3T))/3) in T, read as -2, 1, 1/3, -1/4; (K3) the principal form's class number 3 by its reduced forms.
Usage: python -X utf8 -u tools/b755_closed.py run | plant      (run writes data/b755_cand_a.txt and .json; plant writes data/b755_cand_a_plant.txt)
"""
import json
import math
import os
import sys
import time
from fractions import Fraction as Fr

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N = 3000
FIELDS = ((-23, 6), (-31, 8))  # (D, c) for the principal form x^2 + xy + c y^2, c = (1 - D)/4
K1_WANT = {'negative': 102, 'least': 48, 'zero': 2498, 'positive': 399, 'max_n': 2808, 'max_abs': 190.565466363}
K2_WANT = [Fr(-2), Fr(1), Fr(1, 3), Fr(-1, 4)]


def omega_table(n):
    om = [0] * (n + 1)
    rest = list(range(n + 1))
    for p in range(2, n + 1):
        if rest[p] == p and om[p] == 0 and all(p % q for q in range(2, int(p ** 0.5) + 1)):
            pk = p
            while pk <= n:
                for m in range(pk, n + 1, pk):
                    om[m] += 1
                pk *= p
    return om


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def divisors_table(n):
    dv = [[] for _ in range(n + 1)]
    for d in range(1, n + 1):
        for m in range(d, n + 1, d):
            dv[m].append(d)
    return dv


def reps(c, n):
    r = [0] * (n + 1)
    X = math.isqrt(4 * n) + 2
    for y in range(-X, X + 1):
        for x in range(-X, X + 1):
            v = x * x + x * y + c * y * y
            if 1 <= v <= n:
                r[v] += 1
    return r


def reduced_forms(D):
    out = []
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a) == 0:
                c = (b * b - D) // (4 * a)
                if c >= a and not (b < 0 and (a == c)) and math.gcd(math.gcd(a, abs(b)), c) == 1:
                    out.append((a, b, c))
        a += 1
    return out


def kron(D, p):
    if p == 2:
        return 0 if D % 2 == 0 else (1 if D % 8 in (1, 7) else -1)
    t = pow(D % p, (p - 1) // 2, p)
    return 0 if D % p == 0 else (1 if t == 1 else -1)


def dlog(F, om, dv):
    """log of the Dirichlet series F (F[1] = 1) by the Omega derivation."""
    b = [Fr(0)] * (N + 1)
    for n in range(2, N + 1):
        s = Fr(om[n]) * F[n]
        for d in dv[n][1:-1]:
            if b[d] and F[n // d]:
                s -= om[d] * b[d] * F[n // d]
        b[n] = s / om[n]
    return b


def dexp(G, om, dv):
    """exp of the Dirichlet series G (G[1] = 0) by the Omega derivation."""
    E = [Fr(0)] * (N + 1)
    E[1] = Fr(1)
    for n in range(2, N + 1):
        s = Fr(0)
        for d in dv[n][1:]:
            if G[d] and E[n // d]:
                s += om[d] * G[d] * E[n // d]
        E[n] = s / om[n]
    return E


def closed_b(D, r, om, dv, P, plant):
    lz = [Fr(0)] * (N + 1)
    T = [Fr(0)] * (N + 1)
    npr = []
    for p in P:
        k = kron(D, p)
        pk, m = p, 1
        while pk <= N:
            if k == 1:
                lz[pk] += Fr(2, m)
            elif k == 0:
                lz[pk] += Fr(1, m)
            elif m % 2 == 0:
                lz[pk] += Fr(2, m)
            pk *= p
            m += 1
        if k == 1 and r[p] == 0:
            npr.append(p)
            pk, m = p, 1
            while pk <= N:
                if plant or m % 3:
                    T[pk] += Fr(1, m)
                pk *= p
                m += 1
    G = [-3 * t for t in T]
    E = dexp(G, om, dv)
    F2 = [Fr(0)] * (N + 1)
    F2[1] = Fr(1)
    for n in range(2, N + 1):
        F2[n] = 2 * E[n] / 3
    L2 = dlog(F2, om, dv)
    return [lz[n] + L2[n] for n in range(N + 1)], npr


def taylor_k2():
    # log((1 + 2 exp(-3T))/3) as a power series in T to T^6, exact
    M = 7
    e = [Fr((-3) ** k, math.factorial(k)) for k in range(M)]
    y = [Fr(0)] + [2 * e[k] / 3 for k in range(1, M)]  # (1 + 2e)/3 - 1
    out = [Fr(0)] * M
    pw = [Fr(1)] + [Fr(0)] * (M - 1)
    for j in range(1, M):
        nxt = [Fr(0)] * M
        for i in range(M):
            if pw[i]:
                for k in range(1, M - i):
                    nxt[i + k] += pw[i] * y[k]
        pw = nxt
        for i in range(M):
            out[i] += Fr((-1) ** (j + 1), j) * pw[i]
    return out[1:5]


def write(path, text):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)
    os.replace(tmp, path)


def main(mode):
    t0 = time.time()
    plant = mode == 'plant'
    om = omega_table(N)
    dv = divisors_table(N)
    P = primes_upto(N)
    L = []
    J = {'mode': mode, 'N': N, 'fields': {}}
    # CONTROLS
    r23 = reps(6, N)
    a23 = [Fr(0), Fr(1)] + [Fr(r23[n], 2) for n in range(2, N + 1)]
    b23 = dlog(a23, om, dv)
    neg = [n for n in range(2, N + 1) if b23[n] < 0]
    zer = [n for n in range(2, N + 1) if b23[n] == 0]
    pos = [n for n in range(2, N + 1) if b23[n] > 0]
    cq = [(abs(float(b23[n])) * math.log(n), n) for n in range(2, N + 1)]
    mx = max(cq)
    k1 = {'negative': len(neg), 'least': neg[0] if neg else None, 'b_least': str(b23[neg[0]]) if neg else None, 'zero': len(zer),
          'positive': len(pos), 'max_n': mx[1], 'max_abs': round(mx[0], 9)}
    k1_ok = (k1['negative'] == K1_WANT['negative'] and k1['least'] == K1_WANT['least'] and k1['zero'] == K1_WANT['zero']
             and k1['positive'] == K1_WANT['positive'] and k1['max_n'] == K1_WANT['max_n'] and abs(k1['max_abs'] - K1_WANT['max_abs']) < 5e-9)
    k2 = taylor_k2()
    k2_ok = k2 == K2_WANT
    k3 = {D: reduced_forms(D) for D, c in FIELDS}
    k3_ok = all(len(v) == 3 for v in k3.values()) and all((1, 1, c) in k3[D] for D, c in FIELDS)
    J['controls'] = {'K1': k1, 'K1_ok': k1_ok, 'K2': [str(x) for x in k2], 'K2_ok': k2_ok, 'K3': {str(D): v for D, v in k3.items()}, 'K3_ok': k3_ok}
    L.append('## THE CONTROLS, BEFORE ANY ROW')
    L.append('  (K1) the direct route at -23, n = 2..%d, against data/b750_cq_sign.txt :39: negative %d (want 102), least negative n %s with b = %s (want 48),'
             ' exactly zero %d (want 2498), positive %d (want 399), the largest |b(n)| log n %.9f at n = %d (want 190.565466363 at 2808): %s'
             % (N, k1['negative'], k1['least'], k1['b_least'], k1['zero'], k1['positive'], k1['max_abs'], k1['max_n'], 'AS WANTED' if k1_ok else 'NOT AS WANTED'))
    L.append('  (K2) the Taylor coefficients of log((1 + 2 exp(-3T))/3) at T^1..T^4, exact: %s (the statement: -2, 1, 1/3, -1/4): %s'
             % (', '.join(str(x) for x in k2), 'AS WANTED' if k2_ok else 'NOT AS WANTED'))
    L.append('  (K3) the reduced forms: %s: %s' % (' ; '.join('%d: %s' % (D, ', '.join('(%d,%d,%d)' % f for f in v)) for D, v in k3.items()),
                                                 'AS WANTED (three each, the principal form among them)' if k3_ok else 'NOT AS WANTED'))
    ok_controls = k1_ok and k2_ok and k3_ok
    L.append('### THE CONTROLS: %s' % ('ALL AS WANTED' if ok_controls else 'NOT ALL AS WANTED -- NO ROW IS READ'))
    rows_ok = True
    if ok_controls:
        L.append('')
        L.append('## THE ROWS%s' % (' -- THE PLANT: THE k DIVISIBLE BY 3 KEPT IN T' if plant else ''))
        for D, c in FIELDS:
            r = r23 if D == -23 else reps(c, N)
            a = [Fr(0), Fr(1)] + [Fr(r[n], 2) for n in range(2, N + 1)]
            bd = b23 if D == -23 else dlog(a, om, dv)
            bc, npr = closed_b(D, r, om, dv, P, plant)
            mism = [n for n in range(2, N + 1) if bd[n] != bc[n]]
            nonzero = sum(1 for n in range(2, N + 1) if bd[n] != 0)
            J['fields'][str(D)] = {'c': c, 'nonprincipal_split_first': npr[:8], 'nonprincipal_split_count': len(npr), 'nonzero_direct': nonzero,
                                   'mismatches': len(mism), 'first_mismatches': mism[:10]}
            L.append('  D = %d, x^2 + xy + %dy^2: the non-principal split primes <= %d: %d, the first %s ; direct b(n) nonzero at %d of n = 2..%d ;'
                     ' closed against direct: MISMATCHES %d%s' % (D, c, N, len(npr), npr[:8], nonzero, N, len(mism),
                                                                (' (first %s)' % mism[:10]) if mism else ''))
            if plant:
                rows_ok = rows_ok and len(mism) > 0
            else:
                rows_ok = rows_ok and len(mism) == 0
    secs = time.time() - t0
    J['rows_ok'] = rows_ok
    J['seconds'] = round(secs, 1)
    if plant:
        verdict = 'THE PLANT BREAKS THE AGREEMENT AT BOTH FIELDS: AS WANTED' if (ok_controls and rows_ok) else 'THE PLANT: NOT AS WANTED'
    else:
        verdict = 'MISMATCHES 0 AT BOTH FIELDS: REPRODUCED' if (ok_controls and rows_ok) else 'NOT REPRODUCED'
    head = ('b755 -- (R365)(4)(a): THE CLOSED FORM AT CLASS NUMBER 3 AGAINST THE DIRECT COEFFICIENTS AT -23 AND -31, n <= %d%s (%s)\n\n'
            '### by tools/b755_closed.py (%s), written from the statement alone (data/b753_registrations.txt :67-:69) and committed before its run;\n'
            '### every value an exact rational. The navigator\'s h3check.py (sha256 opening fd6ce1ec81cc0e97) printed to the screen and kept no output:\n'
            '### its "mismatches 0" stands in no bank ((R365)(4)(a)), and no figure of it is printed here as a banked figure.\n\n'
            % (N, ' -- THE PLANT' if plant else '', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), mode))
    text = head + '\n'.join(L) + '\n\n### ### **THE CLOSED FORM (a)%s: %s ; CONTROLS %s ; %.1f s.**\n' % (
        ' WITH ITS PLANT' if plant else '', verdict, 'ALL AS WANTED' if ok_controls else 'NOT ALL AS WANTED', secs)
    print(text)
    base = os.path.join(ROOT, 'data', 'b755_cand_a_plant' if plant else 'b755_cand_a')
    write(base + '.txt', text)
    if not plant:
        write(base + '.json', json.dumps(J, indent=1, sort_keys=True) + '\n')
    return 0 if (ok_controls and rows_ok) else 1


if __name__ == '__main__':
    if sys.argv[1:2] not in (['run'], ['plant']):
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
