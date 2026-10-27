# -*- coding: utf-8 -*-
"""b718_classgroup.py -- the class group of a negative fundamental discriminant and the coefficients of log(Z_Q1/2), for (R328)(4).
Imported by tools/b718_decomp.py, tools/b718_derivation.py and tools/b718_registrations.py; writes nothing.

### reduced forms (a, b, c), b^2 - 4ac = D, by the standard reduction; composition by the united-form formula (Arndt's, as in Cohen
### 5.4.6), validated by the group's own axioms in `group`; a prime's class read from the forms (p, b, c) with b^2 = D mod 4p, reduced.
### a(n) = the number of principal ideals of norm n, read two ways: by the forms (r_Q1(n)/2, enumerated) and by the class group (the
### ideals of norm n as products of prime ideals, each with its class, counted where the product is the identity -- the character sum
### (1/h) SUM_chi SUM_{N A = n} chi(A) by orthogonality, the characters computed for a cyclic group in `a_by_characters`).
### b(n), the coefficients of log(1 + SUM_{n>=2} a(n) n^-s), by the Omega derivation: Omega(mn) = Omega(m) + Omega(n), so f -> Omega f is a
### derivation of Dirichlet convolution and Omega(n) b(n) = SUM_{d | n} Omega(d) b(d) a(n/d), exact in rationals. The banks' c(n) are
### b(n) log n (c(n) = -(d/ds) of the log's coefficient), so the two routes meet in b(n) = c(n)/log n.
"""
import cmath
import math
from fractions import Fraction


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def reduce_form(f):
    a, b, c = f
    while True:
        if not (-a < b <= a):
            k = (a - b) // (2 * a)
            b, c = b + 2 * a * k, a * k * k + b * k + c
            continue
        if c < a:
            a, b, c = c, -b, a
            continue
        if a == c and b < 0:
            b = -b
        return (a, b, c)


def disc(f):
    return f[1] * f[1] - 4 * f[0] * f[2]


def reduced_forms(D):
    out = []
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b - D) % 2:
                continue
            num = b * b - D
            if num % (4 * a):
                continue
            c = num // (4 * a)
            if c < a or (c == a and b < 0):
                continue
            if math.gcd(math.gcd(a, abs(b)), c) != 1:
                continue
            out.append((a, b, c))
        a += 1
    return sorted(out)


def compose(f1, f2, D):
    a1, b1, c1 = f1
    a2, b2, c2 = f2
    m = (b1 + b2) // 2
    g1, u1, v1 = xgcd(a1, a2)
    g, x, w = xgcd(g1, m)
    u, v = x * u1, x * v1                      # u a1 + v a2 + w m = g
    a3 = a1 * a2 // (g * g)
    num = u * a1 * b2 + v * a2 * b1 + w * (b1 * b2 + D) // 2
    if num % g:
        raise ArithmeticError('composition: %r %r not integral' % (f1, f2))
    b3 = (num // g) % (2 * a3)
    if (b3 * b3 - D) % (4 * a3):
        raise ArithmeticError('composition: %r %r gives no form' % (f1, f2))
    return reduce_form((a3, b3, (b3 * b3 - D) // (4 * a3)))


def principal(D):
    return reduce_form((1, D % 2, (D % 2 - D) // 4))


def inverse(f):
    return reduce_form((f[0], -f[1], f[2]))


def group(D):
    """the class group: the reduced forms, the identity, the multiplication table; its axioms checked (closure, identity, inverses,
    associativity over every triple, commutativity), each a boolean returned with the table."""
    F = reduced_forms(D)
    e = principal(D)
    T = dict(((x, y), compose(x, y, D)) for x in F for y in F)
    ok = dict(
        closure=all(v in F for v in T.values()),
        discriminant=all(disc(v) == D for v in T.values()),
        identity=all(T[(e, x)] == x for x in F),
        inverses=all(T[(x, inverse(x))] == e for x in F),
        commutative=all(T[(x, y)] == T[(y, x)] for x in F for y in F),
        associative=all(T[(T[(x, y)], z)] == T[(x, T[(y, z)])] for x in F for y in F for z in F))
    return F, e, T, ok


def order(x, e, T):
    k, y = 1, x
    while y != e:
        y, k = T[(y, x)], k + 1
    return k


def kron(D, p):
    """the Kronecker symbol (D/p) for a prime p: 0 ramified, 1 split, -1 inert."""
    if D % p == 0:
        return 0
    if p == 2:
        return 1 if D % 8 == 1 or D % 8 == -7 else -1
    t = pow(D % p, (p - 1) // 2, p)
    return 1 if t == 1 else -1


def prime_class(D, p):
    """(type, class of one prime ideal above p): 'inert' with None, or 'split'/'ram' with the reduced form of (p, b, c)."""
    k = kron(D, p)
    if k == -1:
        return ('inert', None)
    for b in range(0, 2 * p):
        if (b * b - D) % (4 * p) == 0:
            return ('split' if k == 1 else 'ram', reduce_form((p, b, (b * b - D) // (4 * p))))
    raise ArithmeticError('no root of D mod 4p at p = %d' % p)


def primes_upto(N):
    s = bytearray([1]) * (N + 1)
    s[0:2] = b'\x00\x00'
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(N + 1) if s[i]]


def factor(n, P):
    out = {}
    for p in P:
        if p * p > n:
            break
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def r_form(f, N):
    """r_f(n) for n <= N by enumeration of (x, y) with f(x, y) = n."""
    a, b, c = f
    r = [0] * (N + 1)
    D = b * b - 4 * a * c
    ymax = int(math.isqrt(4 * a * N // (-D))) + 1
    for y in range(-ymax, ymax + 1):
        # a x^2 + b x y + c y^2 <= N
        disc_ = b * b * y * y - 4 * a * (c * y * y - N)
        if disc_ < 0:
            continue
        s = math.isqrt(disc_)
        lo = (-b * y - s) // (2 * a) - 1
        hi = (-b * y + s) // (2 * a) + 1
        for x in range(lo, hi + 1):
            v = a * x * x + b * x * y + c * y * y
            if 0 < v <= N:
                r[v] += 1
    return r


def ideal_classes(D, n, P, T, e, pc):
    """the distribution over classes of the ideals of norm n: {class: count}, from each prime's class (pc[p] = prime_class(D, p))."""
    dist = {e: 1}
    for p, k in factor(n, P).items():
        t, g = pc[p]
        if t == 'inert':
            if k % 2:
                return {}
            local = {e: 1}
        elif t == 'ram':
            y = e
            for _ in range(k):
                y = T[(y, g)]
            local = {y: 1}
        else:
            gi = inverse(g)
            local = {}
            for i in range(k + 1):
                y = e
                for _ in range(i):
                    y = T[(y, g)]
                for _ in range(k - i):
                    y = T[(y, gi)]
                local[y] = local.get(y, 0) + 1
        new = {}
        for x, cx in dist.items():
            for y, cy in local.items():
                z = T[(x, y)]
                new[z] = new.get(z, 0) + cx * cy
        dist = new
    return dist


def a_by_characters(dist, F, e, T):
    """(1/h) SUM_chi SUM_A chi(A) for a cyclic class group: a generator found, chi_j(gen^k) = exp(2 pi i j k / h); the sum rounded
    after its imaginary part is checked below 1e-9. Returns None where the group is not cyclic."""
    h = len(F)
    gen = [x for x in F if order(x, e, T) == h]
    if not gen:
        return None
    g = gen[0]
    log = {e: 0}
    y = e
    for k in range(1, h):
        y = T[(y, g)]
        log[y] = k
    s = 0j
    for j in range(h):
        for x, cx in dist.items():
            s += cx * cmath.exp(2j * math.pi * j * log[x] / h)
    s /= h
    if abs(s.imag) > 1e-9 or abs(s.real - round(s.real)) > 1e-9:
        raise ArithmeticError('character sum not an integer: %r' % s)
    return int(round(s.real))


def omega(n, P):
    return sum(factor(n, P).values())


def log_coeffs(a, N, P):
    """b(n), n <= N, of log(1 + SUM_{n>=2} a(n) n^-s), exact (Fractions), by the Omega derivation."""
    Om = [0] * (N + 1)
    for p in P:
        if p > N:
            break
        q = p
        while q <= N:
            for m in range(q, N + 1, q):
                Om[m] += 1
            q *= p
    nz = [k for k in range(2, N + 1) if a[k]]
    acc = [Fraction(0)] * (N + 1)
    b = [Fraction(0)] * (N + 1)
    for n in range(2, N + 1):
        b[n] = (Om[n] * a[n] - acc[n]) / Om[n]
        if b[n]:
            w = Om[n] * b[n]
            for k in nz:
                m = n * k
                if m > N:
                    break
                acc[m] += a[k] * w
    return b, Om


def pair_sum(a, n):
    return sum(a[d] * a[n // d] for d in range(2, n) if n % d == 0)


def ordered_factorizations(a, n, kmin=3):
    """the number of ordered factorizations n = d_1 ... d_k, k >= kmin, each d_i >= 2 with a(d_i) != 0."""
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def F(m, k):
        # ordered factorizations of m into exactly k parts, each with a != 0
        if k == 1:
            return 1 if (m >= 2 and a[m]) else 0
        return sum(F(m // d, k - 1) for d in range(2, m + 1) if m % d == 0 and a[d])
    return sum(F(n, k) for k in range(kmin, int(math.log2(n)) + 2))
