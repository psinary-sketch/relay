"""b750, (R360)(2)[E]: THE SIGN OF cQ(n) OVER n <= 3000, from the recursion as SIDE-explicit-formula's
SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean :63-:65 defines cQ at the tag v0.38 (peel 14ca5725):

    cQ n = 0 for n <= 1 ;  2 cQ n = rQ n * log n - sum over d in properDivisors n of cQ d * rQ (n / d)   (n >= 2)

with rQ (Schema/EpsteinZQ.lean :59 at 14ca5725) the number of (m, k) in the box |m| <= 2n, |k| <= n with m^2 + m k + 6 k^2 = n
(rQ 0 = 0, rQ 1 = 2). The 2 dividing is rQ 1.

THE ROUTE. Every value is held exactly: cQ n is a finite sum of q_p * log p over primes p with rational q_p (the recursion is
linear over Q in the logs, and log n = sum v_p(n) log p). The logs of distinct primes are linearly independent over Q, so cQ n = 0
exactly when every q_p is 0; otherwise its sign is read from the sum evaluated in decimal arithmetic at PREC digits, with the
smallest |value| met printed against the evaluation's error. rQ is counted by enumerating every lattice point with
m^2 + m k + 6 k^2 <= N (4 Q = (2m + k)^2 + 23 k^2, so |k| <= sqrt(4N/23) and |2m + k| <= 2 sqrt N); the Lean box is checked against it.

THE CONTROLS, printed before the figure:
  (K1) the same recursion with r == 1 (the coefficients of zeta, r(1) = 1 dividing) returns von Mangoldt's Lambda(n) at every
       n <= N, exactly (log p at n = p^k, 0 elsewhere), and is nonnegative throughout;
  (K2) the same recursion on zeta_K's coefficients for K = Q(sqrt -23), a(n) = sum over d | n of the Kronecker symbol (-23/d)
       (relay data/b725_interference.txt :8, :11, the ideal count) is nonnegative throughout; a(n) matches b725's first twelve;
  (K3) the independent route: c = (r * log) Dirichlet-convolved with the Dirichlet inverse of r (the inverse by its own recursion,
       exact rationals), evaluated in decimals, agrees with the recursion's value at every n <= N;
  (K4) rQ by the enumeration equals the Lean box count at every n <= BOXCHECK, and equals b725's first twelve r_Q0
       (data/b725_interference.txt :11); r_Q0 + 2 r_Q1 = 2 a(n) at every n <= N (b725's (C1) identity, :8).

THE FIGURE: the count of n <= N with cQ(n) < 0, the smallest such n and its value, the largest |cQ(n)| and its n; or "none negative".
By the author's clause at the sitting's [E]: any cQ(n) whose 60-digit value lies within 1e-40 of zero (exact zeros among them) is printed
with its n and counted neither negative nor nonnegative, the count of such n printed. The figure says what was computed and no more.

Usage: python -X utf8 -u tools/b750_cq_sign.py [--controls | --bank]   (--controls: the controls alone, no figure; no flag: prints only;
       --bank: writes data/b750_cq_sign.txt once, LF)
Reads nothing external; no network; no lean or lake process.
"""
import os
import sys
import time
from decimal import Decimal, getcontext
from fractions import Fraction

N = 3000
BOXCHECK = 300
PREC = 60
NEAR = Decimal('1e-40')   # ### the author's clause at the sitting's [E]: a value within 1e-40 of zero printed with its n and counted neither way
D = -23
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK = os.path.join(ROOT, 'data', 'b750_cq_sign.txt')
B725_FIRST = {1: (2, 0, 1), 2: (0, 2, 2), 3: (0, 2, 2), 4: (2, 2, 3), 5: (0, 0, 0), 6: (4, 2, 4), 7: (0, 0, 0), 8: (4, 2, 4),
              9: (2, 2, 3), 10: (0, 0, 0), 11: (0, 0, 0), 12: (4, 4, 6)}   # ### n: r_Q0, r_Q1, ideal count (data/b725_interference.txt :11)

getcontext().prec = PREC


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b'\x00\x00'
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


PR = primes_upto(N)


def factor(n):
    out = {}
    for p in PR:
        if p * p > n:
            break
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


FAC = [None, {}] + [factor(n) for n in range(2, N + 1)]
DIVS = [[] for _ in range(N + 1)]
for d_ in range(1, N + 1):
    for m_ in range(d_, N + 1, d_):
        DIVS[m_].append(d_)


def form_counts(a, b, c, n):
    """the number of integer (x, y) with a x^2 + b x y + c y^2 = k, for every 1 <= k <= n (positive definite forms)."""
    disc = 4 * a * c - b * b
    out = [0] * (n + 1)
    ymax = int((4 * a * n / disc) ** 0.5) + 2
    for y in range(-ymax, ymax + 1):
        xmax = int((n / a) ** 0.5 + abs(b * y) / (2 * a)) + 2
        for x in range(-xmax, xmax + 1):
            v = a * x * x + b * x * y + c * y * y
            if 1 <= v <= n:
                out[v] += 1
    return out


def rq_box(k):
    """the Lean definition at EpsteinZQ.lean :59, literally: the box |m| <= 2k, |n| <= k."""
    if k == 0:
        return 0
    return sum(1 for m in range(-2 * k, 2 * k + 1) for n in range(-k, k + 1) if m * m + m * n + 6 * n * n == k)


def kronecker(a, n):
    """the Kronecker symbol (a/n), n >= 1."""
    if n == 1:
        return 1
    res = 1
    while n % 2 == 0:
        n //= 2
        if a % 2 == 0:
            return 0
        res *= 1 if a % 8 in (1, 7) else -1
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


def recursion(r):
    """cQ by the recursion of LogDeriv.lean :63-:65, generalised to r(1) dividing: c(n) = (r(n) log n - sum_{d | n, d < n} c(d) r(n/d)) / r(1),
    c(n) = 0 for n <= 1. Each c(n) exact: {p: Fraction} meaning sum q_p log p."""
    r1 = Fraction(r[1])
    c = [dict(), dict()]
    for n in range(2, N + 1):
        acc = {}
        if r[n]:
            for p, e in FAC[n].items():
                acc[p] = acc.get(p, Fraction(0)) + r[n] * e
        for d in DIVS[n][:-1]:
            if r[n // d] and c[d]:
                w = r[n // d]
                for p, q in c[d].items():
                    acc[p] = acc.get(p, Fraction(0)) - q * w
        c.append(dict((p, q / r1) for p, q in acc.items() if q != 0))
    return c


LOG = dict((p, Decimal(p).ln()) for p in PR)


def value(cd):
    return sum((Decimal(q.numerator) / Decimal(q.denominator)) * LOG[p] for p, q in cd.items()) if cd else Decimal(0)


def inverse_route(r):
    """the independent route: rinv the Dirichlet inverse of r (exact), then c = (r log) * rinv, evaluated in decimals."""
    r1 = Fraction(r[1])
    inv = [Fraction(0)] * (N + 1)
    inv[1] = 1 / r1
    for n in range(2, N + 1):
        s = Fraction(0)
        for d in DIVS[n][1:]:
            if r[d] and inv[n // d]:
                s += r[d] * inv[n // d]
        inv[n] = -s / r1
    rlog = [Decimal(0)] * (N + 1)
    for n in range(2, N + 1):
        if r[n]:
            rlog[n] = r[n] * sum(e * LOG[p] for p, e in FAC[n].items())
    out = [Decimal(0)] * (N + 1)
    for n in range(2, N + 1):
        s = Decimal(0)
        for d in DIVS[n]:
            q = inv[n // d]
            if rlog[d] and q:
                s += rlog[d] * (Decimal(q.numerator) / Decimal(q.denominator))
        out[n] = s
    return out


def main():
    t0 = time.time()
    bank = '--bank' in sys.argv[1:]
    L = ['b750 -- (R360)(2)[E]: THE SIGN OF cQ(n) OVER n <= %d, FROM THE RECURSION AT SIDE-explicit-formula v0.38 (14ca5725) (%s)' % (N, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### by relay tools/b750_cq_sign.py, committed before its run; the recursion as Schema/ZQ/LogDeriv.lean :63-:65 defines cQ at 14ca5725:',
         '###   cQ n = 0 for n <= 1 ; 2 cQ n = rQ n * log n - sum over proper divisors d of cQ d * rQ (n / d) ; rQ (EpsteinZQ.lean :59) the lattice count of m^2 + m k + 6 k^2 = n.',
         '### Each value exact as sum q_p log p (q_p rational); zero exactly when every q_p is 0; the sign of a nonzero value read at %d decimal digits.' % PREC, '']
    rq0 = form_counts(1, 1, 6, N)
    rq1 = form_counts(2, 1, 3, N)
    a = [0] + [sum(kronecker(D, d) for d in DIVS[n]) for n in range(1, N + 1)]
    # ### (K4)
    box_bad = [k for k in range(1, BOXCHECK + 1) if rq_box(k) != rq0[k]]
    first_bad = [n for n, (x0, x1, ia) in B725_FIRST.items() if (rq0[n], rq1[n], a[n]) != (x0, x1, ia)]
    c1_bad = [n for n in range(1, N + 1) if rq0[n] + 2 * rq1[n] != 2 * a[n]]
    k4 = not box_bad and not first_bad and not c1_bad and rq0[1] == 2
    L += ['## (K4) rQ: THE ENUMERATION AGAINST THE LEAN BOX AND b725`S BANK',
          '  the Lean box count (EpsteinZQ.lean :59, literally) against the enumeration, n = 1..%d: mismatches %d %s' % (BOXCHECK, len(box_bad), box_bad[:10]),
          '  rQ(1) = %d (LogDeriv.lean :56, rQ_one: 2)' % rq0[1],
          '  b725`s first twelve (n: r_Q0, r_Q1, ideal count; data/b725_interference.txt :11): mismatches %d %s' % (len(first_bad), first_bad),
          '  r_Q0 + 2 r_Q1 = 2 a(n), n = 1..%d (b725`s (C1) identity, data/b725_interference.txt :8): mismatches %d %s' % (N, len(c1_bad), c1_bad[:10]),
          '  ### (K4) %s' % ('AS WANTED' if k4 else 'NOT AS WANTED'), '']
    # ### (K1)
    one = [0] + [1] * N
    cz = recursion(one)
    lam_bad = [n for n in range(2, N + 1) if cz[n] != ({next(iter(FAC[n])): Fraction(1)} if len(FAC[n]) == 1 else {})]
    z_neg = [n for n in range(2, N + 1) if cz[n] and value(cz[n]) < 0]
    k1 = not lam_bad and not z_neg
    L += ['## (K1) THE SAME RECURSION ON zeta (r == 1, r(1) = 1 dividing) RETURNS VON MANGOLDT`S LAMBDA',
          '  exactly log p at n = p^k and 0 elsewhere, n = 2..%d: mismatches %d %s' % (N, len(lam_bad), lam_bad[:10]),
          '  negative values: %d %s ; the values at n = 2..12: %s' % (len(z_neg), z_neg[:10], ', '.join('%d: %s' % (n, ('%.6f' % float(value(cz[n])))) for n in range(2, 13))),
          '  ### (K1) %s' % ('AS WANTED' if k1 else 'NOT AS WANTED'), '']
    # ### (K2)
    ck = recursion(a)
    k_neg = [n for n in range(2, N + 1) if ck[n] and value(ck[n]) < 0]
    k_neg_coef = [n for n in range(2, N + 1) if any(q < 0 for q in ck[n].values())]
    k2 = not k_neg and a[1] == 1
    L += ['## (K2) THE SAME RECURSION ON zeta_K, K = Q(sqrt -23): a(n) = sum over d | n of (-23/d) (data/b725_interference.txt :8, :11), a(1) = %d' % a[1],
          '  negative values, n = 2..%d: %d %s ; rows with a negative log-coefficient: %d %s' % (N, len(k_neg), k_neg[:10], len(k_neg_coef), k_neg_coef[:10]),
          '  the values at n = 2..12: %s' % ', '.join('%d: %.6f' % (n, float(value(ck[n]))) for n in range(2, 13)),
          '  ### (K2) %s' % ('AS WANTED' if k2 else 'NOT AS WANTED'), '']
    # ### the figure's values, and (K3)
    cq = recursion(rq0)
    vals = [Decimal(0), Decimal(0)] + [value(cq[n]) for n in range(2, N + 1)]
    inv = inverse_route(rq0)
    tol = Decimal(10) ** (-(PREC - 15))
    k3_bad = [n for n in range(2, N + 1) if abs(inv[n] - vals[n]) > tol * (1 + abs(vals[n]))]
    k3_max = max(abs(inv[n] - vals[n]) for n in range(2, N + 1))
    k3 = not k3_bad
    L += ['## (K3) THE INDEPENDENT ROUTE: c = (rQ log) CONVOLVED WITH THE DIRICHLET INVERSE OF rQ (EXACT RATIONALS), AGAINST THE RECURSION',
          '  n = 2..%d: disagreements beyond %s relative: %d %s ; the largest difference %s' % (N, '1e-%d' % (PREC - 15), len(k3_bad), k3_bad[:10], '%.3e' % float(k3_max)),
          '  ### (K3) %s' % ('AS WANTED' if k3 else 'NOT AS WANTED'), '']
    ctl = k1 and k2 and k3 and k4
    L += ['### THE CONTROLS: (K1) %s ; (K2) %s ; (K3) %s ; (K4) %s ; %s' % tuple(['AS WANTED' if x else 'NOT AS WANTED' for x in (k1, k2, k3, k4)] + ['ALL AS WANTED' if ctl else 'NOT ALL AS WANTED']), '']
    if not ctl:
        L += ['### ### **THE CONTROLS NOT ALL AS WANTED: NO FIGURE READ.**']
    elif '--controls' in sys.argv[1:]:
        L += ['### ### **--controls: THE CONTROLS ALONE, NO FIGURE COMPUTED OR PRINTED ; %.1f s.**' % (time.time() - t0)]
        bank = False
    else:
        zero = [n for n in range(2, N + 1) if not cq[n]]
        band = [n for n in range(2, N + 1) if abs(vals[n]) <= NEAR]   # ### the author's clause at [E]: within 1e-40 of zero, exact zeros included
        bset = set(band)
        neg = [n for n in range(2, N + 1) if n not in bset and vals[n] < 0]
        pos = [n for n in range(2, N + 1) if n not in bset and vals[n] > 0]
        out = [n for n in range(2, N + 1) if n not in bset]
        small = min(out, key=lambda n: abs(vals[n]))
        big = max(out, key=lambda n: abs(vals[n]))
        L += ['## THE FIGURE: cQ(n), n = 1..%d' % N,
              '  cQ(1) = 0 by definition ; n = 2..%d: WITHIN 1e-40 OF ZERO %d (of them exactly zero %d, nonzero %d), counted neither negative nor nonnegative ; '
              'outside that band: negative %d, nonnegative %d' % (N, len(band), len(zero), len(band) - len(zero), len(neg), len(pos)),
              '  the n within 1e-40 of zero, each with its value (exact: every log-coefficient 0): %s' % (
                  ', '.join('%d: %s' % (n, 'exact 0' if not cq[n] else '%.6e' % float(vals[n])) for n in band) or 'none'),
              '  the smallest |cQ(n)| outside the band: n = %d, %s (the evaluation at %d digits; its error below 1e-%d)' % (small, '%.6e' % float(vals[small]), PREC, PREC - 15),
              '  the largest |cQ(n)|: n = %d, cQ = %s' % (big, '%.12f' % float(vals[big])),
              '  the first values (n: rQ, cQ): %s' % ' ; '.join('%d: %d %.9f' % (n, rq0[n], float(vals[n])) for n in range(1, 13))]
        if neg:
            n0 = neg[0]
            L += ['  the negative n, first twenty: %s' % ', '.join(str(n) for n in neg[:20]),
                  '  the smallest n with cQ(n) < 0: n = %d = %s, cQ(n) = %s, exactly %s' % (
                      n0, ' . '.join('%d^%d' % (p, e) for p, e in sorted(FAC[n0].items())), '%.12f' % float(vals[n0]),
                      ' + '.join('(%s) log %d' % (q, p) for p, q in sorted(cq[n0].items())))]
        L += ['', '### ### **cQ(n), n = 2..%d, FROM THE RECURSION AT v0.38: NEGATIVE %d%s ; WITHIN 1e-40 OF ZERO %d (EXACTLY ZERO %d), COUNTED NEITHER WAY ; NONNEGATIVE %d ; THE LARGEST |cQ| %s AT n = %d ; CONTROLS (K1)-(K4) ALL AS WANTED ; %.1f s.**' % (
            N, len(neg), (' ; THE SMALLEST NEGATIVE n = %d, cQ = %s' % (neg[0], '%.12f' % float(vals[neg[0]]))) if neg else ' ; NONE NEGATIVE',
            len(band), len(zero), len(pos), '%.9f' % float(vals[big]), big, time.time() - t0)]
    text = '\n'.join(L) + '\n'
    print(text, end='')
    if bank:
        if os.path.exists(BANK):
            sys.exit('### %s EXISTS: THE BANK IS WRITTEN ONCE -- NOTHING WRITTEN' % BANK)
        with open(BANK, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(text)
        print('  banked: data/b750_cq_sign.txt')


if __name__ == '__main__':
    main()
