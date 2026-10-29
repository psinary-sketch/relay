# -*- coding: utf-8 -*-
"""b723_c2_check.py -- THE C2 CLOSED FORM CHECKED, (R333)(6), Component 5: the derivation data/b723_c2_closed_form.txt read against every
coefficient bank of b711-b722 at class number 2, EACH ROW LABELLED POST HOC because the banks predate the closed form.

THE CLOSED FORM: for an imaginary quadratic field of class number 2 with principal form Q, log(Z_Q / 2) = log zeta_K - S + log cosh S,
S = SUM over bad primes of e_p artanh(p^-s); a prime bad when it splits or ramifies into non-principal prime ideals (chi_D(p) != -1 and
Q does not represent p), e_p = 2 split and 1 ramified. b(n) is the coefficient of n^-s in log(Z_Q / 2): here computed FROM THE CLOSED
FORM ALONE -- log zeta_K's coefficient at a prime power (e_p / k at a bad p^k; the good prime powers carry a positive one and are not
read) plus the coefficient of -S + log cosh S (log cosh x = SUM 2^(2m-1)(2^(2m)-1) B_2m x^(2m) / (m (2m)!), B_2m exact), every value a
rational, over the bad-smooth n to the banks' cut 32532 (a coefficient off them is 0 or a good prime power's, never negative).

### THE CONTROLS, printed before any bank is read:
###   (C0) the closed form against the direct series log(Z_Q / 2) = SUM_k (-1)^(k+1) F_k / k from r_Q (b722's C2 statement's route,
###        data/b722_c2_statement.txt :38-:49), fresh, at every n <= 3000, at D = -15 and D = -20;
###   (C1) a planted e_p: at D = -15 the split bad prime 2 given e_2 = 1 in place of 2 -- the check FAILS to reproduce, as wanted.
### THE ROWS, each POST HOC: per field, the bank's n0 and b(n0) against the closed form's; the bank's count of negatives through 32532
### against the closed form's (beside, as the banks print it); every n the bank prints as negative (its list), each with no good prime
### (the closed form's zero at every n of two or more distinct primes with a good one); the n0's Omega and its terms -S^4/12 and S^2/2.
### Routes: `run` (prints) ; `bank` (prints and writes data/b723_c2_check.txt). Written by the Write tool at b723; it writes that one bank.
### Nothing here is compiled; nothing proves RH or GRH.
"""
import json
import math
import os
import sys
import time
from fractions import Fraction as Fr

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CUT = 32532
# ### the class-number-2 fields of b711-b722's coefficient banks: (D, bank, how its reading is found)
BANKS = [(-15, 'b713_coeffs.json', 'b713'), (-20, 'b719_coeffs.json', 'readings'), (-35, 'b720_coeffs.json', 'readings'),
         (-40, 'b720_coeffs.json', 'readings')] + [(d, 'b722_walk.json', 'readings') for d in
                                                    (-15, -24, -51, -52, -88, -91, -115, -123, -148, -187, -232, -235, -267, -403, -427)]


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def kronecker(a, n):
    """(a / n) by the Jacobi route, the factor 2 by (a / 2) = 0, 1, -1 as a = 0, +-1, +-3 mod 8 (tools/b723_zetak.py's, copied to keep
    this check free of b709's import chain)."""
    res = 1
    while n % 2 == 0:
        n //= 2
        r = a % 8
        if r % 2 == 0:
            return 0
        if r in (3, 5):
            res = -res
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


def pform(D):
    return (1, 0, -D // 4) if D % 4 == 0 else (1, 1, (1 - D) // 4)


def represents(D, m):
    a, b, c = pform(D)
    ymax = math.isqrt(4 * m // abs(D)) + 1
    for y in range(0, ymax + 1):
        disc = b * b * y * y - 4 * (c * y * y - m)
        if disc < 0:
            continue
        r = math.isqrt(disc)
        if r * r == disc and ((-b * y + r) % 2 == 0 or (-b * y - r) % 2 == 0):
            return True
    return False


def primes_to(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b'\x00\x00'
    for p in range(2, math.isqrt(n) + 1):
        if s[p]:
            s[p * p::p] = bytearray(len(s[p * p::p]))
    return [p for p in range(n + 1) if s[p]]


def bad_primes(D, cut=CUT):
    """{p: e_p} -- p splits (chi = 1, e 2) or ramifies (chi = 0, e 1) and Q does not represent p."""
    out = {}
    for p in primes_to(cut):
        ch = kronecker(D, p)
        if ch != -1 and not represents(D, p):
            out[p] = 2 if ch == 1 else 1
    return out


def bernoulli(m):
    B = [Fr(0)] * (m + 1)
    B[0] = Fr(1)
    for n in range(1, m + 1):
        B[n] = -sum(Fr(math.comb(n + 1, k)) * B[k] for k in range(n)) / (n + 1)
    return B


_B = bernoulli(40)


def logcosh_coef(m):
    """the coefficient of x^(2m) in log cosh x."""
    return Fr(2 ** (2 * m - 1) * (2 ** (2 * m) - 1)) * _B[2 * m] / (m * math.factorial(2 * m))


def conv(A, B, cut):
    out = {}
    for a, x in A.items():
        for b, y in B.items():
            if a * b > cut:
                continue
            out[a * b] = out.get(a * b, 0) + x * y
    return out


def closed_b(bad, cut=CUT):
    """b(n) from the closed form at every bad-smooth n <= cut (n >= 2), with the terms by power of S: {n: (b, {power: term}, zk)}."""
    S = {}
    for p, e in bad.items():
        q, k = p, 1
        while q <= cut:
            if k % 2:
                S[q] = Fr(e, k)
            q *= p
            k += 1
    terms = {1: {n: -x for n, x in S.items()}}
    P, j = S, 1
    while P:
        P = conv(P, S, cut)
        j += 1
        if j % 2 == 0 and P:
            c = logcosh_coef(j // 2)
            terms[j] = {n: c * x for n, x in P.items()}
    out = {}
    for j, tm in terms.items():
        for n, x in tm.items():
            out.setdefault(n, [Fr(0), {}, Fr(0)])
            out[n][0] += x
            out[n][1][j] = x
    for p, e in bad.items():
        q, k = p, 1
        while q <= cut:
            out.setdefault(q, [Fr(0), {}, Fr(0)])
            out[q][0] += Fr(e, k)
            out[q][2] = Fr(e, k)
            q *= p
            k += 1
    return out


def factor(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


# ================================================================================ (C0) THE DIRECT SERIES
def direct_b(D, cut):
    """b(n) for 2 <= n <= cut from r_Q directly: a(n) = r_Q(n)/2, log(1 + A) = SUM_k (-1)^(k+1) A^k / k, A = SUM_{n>=2} a(n) n^-s."""
    a, b_, c = pform(D)
    r = [0] * (cut + 1)
    lim = math.isqrt(4 * cut) + 2
    for y in range(-lim, lim + 1):
        for x in range(-lim - abs(y), lim + abs(y) + 1):
            v = a * x * x + b_ * x * y + c * y * y
            if 1 <= v <= cut:
                r[v] += 1
    A = {n: Fr(r[n], 2) for n in range(2, cut + 1) if r[n]}
    out, P, k = {}, A, 1
    while P:
        for n, x in P.items():
            out[n] = out.get(n, 0) + (Fr(1, k) if k % 2 else Fr(-1, k)) * x
        P = conv(P, A, cut)
        k += 1
    return out


def c0(D, cut=3000):
    dr = direct_b(D, cut)
    cl = closed_b(bad_primes(D, cut), cut)
    bad = bad_primes(D, cut)
    miss = []
    for n in range(2, cut + 1):
        f = factor(n)
        want = dr.get(n, Fr(0))
        if n in cl:
            got = cl[n][0]
        elif len(f) == 1 and list(f)[0] not in bad:
            # ### a good prime power: log zeta_K's coefficient alone -- split 2/k, ramified 1/k, inert 2/k at even k and 0 at odd k
            p, k = list(f.items())[0]
            ch = kronecker(D, p)
            got = Fr(2, k) if ch == 1 else (Fr(1, k) if ch == 0 else (Fr(2, k) if k % 2 == 0 else Fr(0)))
        else:
            got = Fr(0)
        if got != want:
            miss.append((n, str(want), str(got)))
    return miss


# ================================================================================ THE BANKS
def reading(D, bank, how):
    j = json.load(open(os.path.join(D_, bank), encoding='utf-8'))
    if how == 'b713':
        return dict(n0=j['least_negative'], b=None, closed=j['least_negative_value'], negatives=j['negatives'], listed=j['negative_list'],
                    listed_what='the full list of negatives')
    r = j['readings'][str(D)]
    return dict(n0=r['n0'], b=r['b'], closed=r.get('closed'), negatives=r['negatives'], listed=r['first'], listed_what='the first ten negatives')


def run(write):
    t0 = time.time()
    L = ['b723 -- COMPONENT 5, (R333)(6): THE C2 CLOSED FORM CHECKED AGAINST THE COEFFICIENT BANKS OF b711-b722 AT CLASS NUMBER 2 -- EVERY ROW POST HOC (%s)' % utc(), '',
         '### by tools/b723_c2_check.py; the derivation data/b723_c2_closed_form.txt. b(n), the coefficient of log(Z_Q/2), computed from the closed form',
         '### alone (log zeta_K at the bad prime powers, -S + log cosh S exact in rationals) to the banks` cut %d; the banks read as committed.' % CUT,
         '### EVERY ROW IS POST HOC: the banks predate the closed form, which was written knowing them; nothing here is a prediction or compiled.', '']

    def out(s=''):
        L.append(s)
        print(s, flush=True)

    out('## (C0) THE CLOSED FORM AGAINST THE DIRECT SERIES FROM r_Q, FRESH, EVERY n <= 3000 (POST HOC LIKE THE REST: the form was written knowing such series)')
    c0ok = True
    for D in (-15, -20):
        miss = c0(D)
        c0ok &= not miss
        out('  D = %d: n <= 3000 compared 2999 ; mismatches %d %s -- %s' % (D, len(miss), miss[:4], 'AS WANTED' if not miss else 'NOT AS WANTED'))
    out('## (C1) THE PLANTED e_p: D = -15, the split bad prime 2 given e_2 = 1 in place of 2')
    bad = bad_primes(-15)
    pl = dict(bad)
    pl[2] = 1
    cl_pl = closed_b(pl)
    neg_pl = sorted(n for n, v in cl_pl.items() if v[0] < 0)
    rd = reading(-15, 'b713_coeffs.json', 'b713')
    c1fail = not (neg_pl and neg_pl[0] == rd['n0'] and len(neg_pl) == rd['negatives'])
    out('  planted: n0 %s, negatives %d ; the bank: n0 %s, negatives %d -- %s' % (
        neg_pl[0] if neg_pl else None, len(neg_pl), rd['n0'], rd['negatives'], 'FAILS TO REPRODUCE, AS WANTED' if c1fail else 'REPRODUCES: NOT AS WANTED'))
    out()
    if not (c0ok and c1fail):
        out('### ### **REFUSED: A CONTROL NOT AS WANTED ; NO BANK READ.**')
        _write(write, L)
        return 1

    out('## THE ROWS, EACH POST HOC (field ; bad primes to 50 with e_p ; the bank`s n0, b(n0), negatives ; the closed form`s ; the printed negatives with a good prime)')
    rows_ok, nrows = 0, 0
    seen = []
    for D, bank, how in BANKS:
        bad = bad_primes(D)
        cl = closed_b(bad)
        neg = sorted(n for n, v in cl.items() if v[0] < 0)
        rd = reading(D, bank, how)
        n0, b0 = neg[0], cl[neg[0]][0]
        bank_b = Fr(rd['b']) if rd['b'] is not None else None
        good_in_list = [n for n in rd['listed'] + [rd['n0']] if any(p not in bad for p in factor(n))]
        ok_n0 = n0 == rd['n0']
        ok_b = bank_b is None or b0 == bank_b
        ok_cnt = len(neg) == rd['negatives']
        ok_list = all(x in set(neg) for x in rd['listed']) and (how != 'b713' or rd['listed'] == neg)
        ok = ok_n0 and ok_b and ok_cnt and ok_list and not good_in_list
        nrows += 1
        rows_ok += ok
        f0 = factor(n0)
        om = sum(f0.values())
        tm = cl[n0][1]
        ram = sorted(p for p, e in bad.items() if e == 1)
        out('  POST HOC  D %5d (%s) | bad to 50 %s ; ramified bad %s | bank n0 %s, b(n0) %s, negatives %d | closed n0 %d = %s, b(n0) %s, negatives %d ; '
            'Omega(n0) %d, its terms: S^2/2 %s, -S^4/12 %s, log zeta_K %s | %s listed (%d): all negative in the closed form %s, with a good prime %d | %s' % (
                D, bank, {p: e for p, e in bad.items() if p <= 50}, ram, rd['n0'], rd['b'] if rd['b'] is not None else '(not printed; ' + rd['closed'] + ')',
                rd['negatives'], n0, '.'.join('%d^%d' % (p, k) if k > 1 else str(p) for p, k in sorted(f0.items())), b0, len(neg), om,
                tm.get(2, 0), tm.get(4, 0), cl[n0][2], rd['listed_what'], len(rd['listed']), ok_list, len(good_in_list),
                'REPRODUCED' if ok else 'NOT REPRODUCED: n0 %s b %s count %s list %s' % (ok_n0, ok_b, ok_cnt, ok_list)))
        seen.append(D)
    # ### the consequences, read over every field and every bad-smooth n to the cut, from the closed form
    out()
    out('## THE CONSEQUENCES READ FROM THE CLOSED FORM OVER THE EIGHTEEN FIELDS TO %d' % CUT)
    low_neg, every_ram = 0, True
    for D in sorted(set(seen), reverse=True):
        bad = bad_primes(D)
        cl = closed_b(bad)
        low_neg += sum(1 for n, v in cl.items() if v[0] < 0 and sum(factor(n).values()) <= 3)
        every_ram &= any(e == 1 for e in bad.values())
    out('  negative b(n) at Omega(n) <= 3: %d (the derivation: none) ; a bad ramified prime at every field: %s (the derivation: genus theory)' % (
        low_neg, every_ram))
    out()
    out('### ### **THE C2 CLOSED FORM, POST HOC: C0 %s ; C1 (PLANTED e_p) %s ; ROWS %d, REPRODUCED %d ; FIELDS %d ; NEGATIVE AT OMEGA <= 3: %d ; '
        'A BAD RAMIFIED PRIME AT EVERY FIELD %s ; %d s.**' % ('AS WANTED' if c0ok else 'NOT AS WANTED', 'FAILS, AS WANTED' if c1fail else 'NOT AS WANTED',
                                                             nrows, rows_ok, len(set(seen)), low_neg, every_ram, int(time.time() - t0)))
    _write(write, L)
    return 0 if rows_ok == nrows else 1


def _write(write, L):
    if not write:
        return
    p = os.path.join(D_, 'b723_c2_check.txt')
    with open(p + '.tmp', 'wb') as f:
        f.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print('written data/b723_c2_check.txt')


if __name__ == '__main__':
    verb = sys.argv[1] if len(sys.argv) > 1 else ''
    if verb not in ('run', 'bank'):
        print('usage: b723_c2_check.py run | bank')
        sys.exit(2)
    sys.exit(run(verb == 'bank'))
