#!/usr/bin/env python3
"""
b224 -- THE SEGRE QUESTION AT THE THREE OPEN CELLS.
### EXACT ARITHMETIC IN Q(zeta_N) THROUGHOUT (N = p^{2n}, a prime power). ### NO FLOATS ANYWHERE.
Registration: data/b224_registration_2026-08-28.txt (banked BEFORE this runs).

### THE QUESTION, in the purity report's own words: "the pencil method generalizes to a QUADRIC
### SYSTEM ON P^{d1-1}" -- does ANY nonzero Schmidt-pure vector hide in E1?

### THE METHOD, and why it is linear algebra rather than a Groebner basis.
### Pure <=> rank 1 <=> every 2x2 minor vanishes. With E1 spanned by C_1..C_d, the general element
### is SUM alpha_k C_k and each minor is a QUADRATIC FORM q_r(alpha). The pure vectors are the
### projective variety V(q_1..q_M) in P^{d-1}.
### ### V IS EMPTY  <=>  the ideal I = (q_1..q_M) contains m^D for some D
### ###              <=>  the multiplication map  (S_{D-2})^M --> S_D,  (f_r) |-> SUM f_r q_r,
### ###                   IS SURJECTIVE for some D.
### ### SO EMPTINESS IS CERTIFIED BY A **RANK** OVER Q(zeta_N), which is exact and needs no
### ### Groebner engine. ### THE CERTIFICATE IS ONE-DIRECTIONAL AND THE CODE SAYS SO:
### ###   surjective at some D  ==>  (NONE), certified.
### ###   not surjective at the D reached  ==>  (UNDECIDED). ### IT DOES **NOT** MEAN NONEMPTY.

### G-EXACT: a reduction mod ell is used ONLY as a non-binding pre-screen for picking a basis of
### E1, never for a verdict. ### A system with no common zero mod ell may still have one in
### characteristic zero, and one with a zero mod ell need not lift.
"""
import itertools
import os
from fractions import Fraction

# ---------------- Q(zeta_N), N = p^a : dense Fraction vectors of length phi(N) ----------------


class Cyc:
    """Q(zeta_N) for N a power of p. Basis {zeta^e : e < phi(N)}; Phi_N = sum_{t<p} x^{t N/p}."""

    def __init__(self, p, N):
        self.p, self.N = p, N
        self.Np = N // p
        self.deg = N - self.Np              # phi(N)

    def zero(self):
        return [Fraction(0)] * self.deg

    def from_exp(self, e, c=1):
        """zeta^e * c, reduced into the power basis."""
        v = self.zero()
        self.add_exp(v, e, Fraction(c))
        return v

    def add_exp(self, v, e, c):
        e %= self.N
        k, r = divmod(e, self.Np)
        if k <= self.p - 2:
            v[k * self.Np + r] += c
        else:
            for t in range(self.p - 1):
                v[t * self.Np + r] -= c

    def add(self, a, b):
        return [x + y for x, y in zip(a, b)]

    def sub(self, a, b):
        return [x - y for x, y in zip(a, b)]

    def scale(self, a, s):
        return [x * s for x in a]

    def mul(self, a, b):
        # multiply as polynomials in zeta then reduce
        out = self.zero()
        for i, x in enumerate(a):
            if not x:
                continue
            for j, y in enumerate(b):
                if not y:
                    continue
                self.add_exp(out, i + j, x * y)
        return out

    def is_zero(self, a):
        return all(x == 0 for x in a)

    def inv(self, a):
        """### EXACT inverse by extended Euclid on Q[x] modulo Phi_N."""
        if self.is_zero(a):
            raise ZeroDivisionError("inverse of 0 in Q(zeta_N)")
        phi = [Fraction(0)] * (self.deg + 1)
        for t in range(self.p):
            phi[t * self.Np] = Fraction(1)
        r0, r1 = phi[:], _trim(a[:] + [Fraction(0)])
        s0, s1 = [Fraction(0)], [Fraction(1)]
        while _deg(r1) >= 0:
            qy, rr = _divmod_poly(r0, r1)
            r0, r1 = r1, rr
            s0, s1 = s1, _sub_poly(s0, _mul_poly(qy, s1))
        c = r0[_deg(r0)]
        s0 = [x / c for x in s0]
        out = self.zero()
        for i, x in enumerate(s0):
            if x:
                self.add_exp(out, i, x)
        return out


def _trim(f):
    while f and f[-1] == 0:
        f.pop()
    return f


def _deg(f):
    return len(_trim(f[:])) - 1


def _mul_poly(a, b):
    if not a or not b:
        return []
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return _trim(out)


def _sub_poly(a, b):
    n = max(len(a), len(b))
    out = [Fraction(0)] * n
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] -= x
    return _trim(out)


def _divmod_poly(a, b):
    a = _trim(a[:])
    b = _trim(b[:])
    if not b:
        raise ZeroDivisionError
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a:
        d = len(a) - len(b)
        c = a[-1] / b[-1]
        q[d] += c
        for i, y in enumerate(b):
            a[i + d] -= c * y
        _trim(a)
    return _trim(q), a


# ---------------- the E1 units and their Schmidt matrices ----------------

def unit_entries(K, p, n, i, j):
    """u = q(1+Pi)f + S(1+Pi)f for f = e_{i+qj} - e_i, as N cyclotomic entries."""
    q = p ** n
    N = q * q
    f = {}
    f[(i + q * j) % N] = f.get((i + q * j) % N, 0) + 1
    f[i % N] = f.get(i % N, 0) - 1
    h = dict(f)
    for m, c in f.items():
        h[(-m) % N] = h.get((-m) % N, 0) + c
    h = {m: c for m, c in h.items() if c}
    u = [K.zero() for _ in range(N)]
    for m, c in h.items():
        K.add_exp(u[m], 0, Fraction(q * c))
        for mp in range(N):
            K.add_exp(u[mp], (m * mp) % N, Fraction(c))
    return u


def schmidt_matrix(K, u, p, n):
    """C[a][b] = u[(a + q b) mod N] -- the bipartition matrix the minor test uses."""
    q = p ** n
    N = q * q
    return [[u[(a + q * b) % N] for b in range(q)] for a in range(q)]


def e1_basis(K, p, n, d1, ell, g):
    """Pick d1 independent units by a mod-ell rank screen.
    ### THE SCREEN IS NON-BINDING (G-EXACT): it only CHOOSES a spanning set; every verdict
    ### afterwards is computed exactly in Q(zeta_N)."""
    q = p ** n
    N = q * q
    chosen, rows = [], []
    for i in range(1, q):
        for j in range(1, q):
            u = unit_entries(K, p, n, i, j)
            r = [_hom(K, ent, ell, g) for ent in u]
            if all(x == 0 for x in r):
                continue
            test = rows + [r]
            if _rank_mod(test, ell) > len(rows):
                rows = test
                chosen.append((i, j, u))
                if len(chosen) == d1:
                    return chosen
    return chosen


def _hom(K, vec, ell, g):
    s = 0
    gp = 1
    for c in vec:
        if c:
            num, den = c.numerator % ell, c.denominator % ell
            s = (s + num * pow(den, ell - 2, ell) * gp) % ell
        gp = (gp * g) % ell
    return s


def _rank_mod(rows, ell):
    m = [r[:] for r in rows]
    R = 0
    ncols = len(m[0]) if m else 0
    for c in range(ncols):
        piv = None
        for r in range(R, len(m)):
            if m[r][c] % ell:
                piv = r
                break
        if piv is None:
            continue
        m[R], m[piv] = m[piv], m[R]
        inv = pow(m[R][c], ell - 2, ell)
        m[R] = [(x * inv) % ell for x in m[R]]
        for r in range(len(m)):
            if r != R and m[r][c] % ell:
                f = m[r][c]
                m[r] = [(x - f * y) % ell for x, y in zip(m[r], m[R])]
        R += 1
        if R == len(m):
            break
    return R


def find_ell_g(N, start=1000):
    ell = start
    while True:
        ell += 1
        if all(ell % t for t in range(2, int(ell ** 0.5) + 1)) and (ell - 1) % N == 0:
            for g in range(2, ell):
                if pow(g, N, ell) == 1 and all(pow(g, N // t, ell) != 1
                                               for t in _prime_factors(N)):
                    return ell, g


def _prime_factors(n):
    fs, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            fs.add(d)
            n //= d
        d += 1
    if n > 1:
        fs.add(n)
    return fs


# ---------------- the quadric system and the degree-D emptiness certificate ----------------

def monomials(d, deg):
    """exponent tuples of total degree `deg` in d variables."""
    if d == 1:
        return [(deg,)]
    out = []
    for e in range(deg + 1):
        for rest in monomials(d - 1, deg - e):
            out.append((e,) + rest)
    return out


def quadrics(K, mats, q):
    """The 2x2 minors of SUM alpha_k C_k as quadratic forms.
    Returns list of dicts {(k,l) with k<=l : coefficient in Q(zeta_N)}."""
    d = len(mats)
    out = []
    for a1, a2 in itertools.combinations(range(1, q), 2):    # row 0 is zero in Son
        for b1, b2 in itertools.combinations(range(q), 2):
            form = {}
            for k in range(d):
                for l in range(d):
                    t = K.sub(K.mul(mats[k][a1][b1], mats[l][a2][b2]),
                              K.mul(mats[k][a1][b2], mats[l][a2][b1]))
                    if K.is_zero(t):
                        continue
                    key = (k, l) if k <= l else (l, k)
                    form[key] = K.add(form.get(key, K.zero()), t)
            form = {kk: v for kk, v in form.items() if not K.is_zero(v)}
            if form:
                out.append(form)
    return out


def surjective_in_degree(K, forms, d, D, cap_rows=None):
    """### THE CERTIFICATE. Is (S_{D-2})^M --> S_D surjective?
    If YES the projective variety is EMPTY and the verdict is (NONE), certified exactly."""
    tgt = monomials(d, D)
    tix = {m: i for i, m in enumerate(tgt)}
    src = monomials(d, D - 2)
    rows = []
    for f in forms:
        for s in src:
            row = [None] * len(tgt)
            for (k, l), c in f.items():
                e = list(s)
                e[k] += 1
                e[l] += 1
                i = tix[tuple(e)]
                row[i] = c if row[i] is None else K.add(row[i], c)
            rows.append([K.zero() if x is None else x for x in row])
            if cap_rows and len(rows) >= cap_rows:
                break
        if cap_rows and len(rows) >= cap_rows:
            break
    r = rank_exact(K, rows, len(tgt))
    return r, len(tgt), len(rows)


def rank_exact(K, rows, ncols):
    """### EXACT Gaussian elimination over Q(zeta_N). No floats."""
    m = [r[:] for r in rows]
    R = 0
    for c in range(ncols):
        piv = None
        for r in range(R, len(m)):
            if not K.is_zero(m[r][c]):
                piv = r
                break
        if piv is None:
            continue
        m[R], m[piv] = m[piv], m[R]
        inv = K.inv(m[R][c])
        m[R] = [K.mul(x, inv) for x in m[R]]
        for r in range(len(m)):
            if r != R and not K.is_zero(m[r][c]):
                f = m[r][c]
                m[r] = [K.sub(x, K.mul(f, y)) for x, y in zip(m[r], m[R])]
        R += 1
        if R == ncols or R == len(m):
            break
    return R


def single_rank_one(K, mats, q):
    """Cheap pre-screen: is any basis matrix C_k itself rank 1 (i.e. already pure)?"""
    hits = []
    for k, C in enumerate(mats):
        pure = True
        for a1, a2 in itertools.combinations(range(1, q), 2):
            for b1, b2 in itertools.combinations(range(q), 2):
                t = K.sub(K.mul(C[a1][b1], C[a2][b2]), K.mul(C[a1][b2], C[a2][b1]))
                if not K.is_zero(t):
                    pure = False
                    break
            if not pure:
                break
        if pure:
            hits.append(k)
    return hits


def rank_incremental(K, row_iter, ncols, target=None, log=None):
    """### EXACT rank, row at a time, stopping the moment full rank is reached.
    rank_exact() sweeps every row for every column and is wasteful when the rank is
    attained early; this reduces each row against the pivots found so far.
    ### STILL FULLY EXACT -- no floats, no mod-ell shortcut."""
    piv_rows = []          # (pivot_col, normalised row)
    seen = 0
    for row in row_iter:
        seen += 1
        r = row[:]
        for pc, pr in piv_rows:
            if not K.is_zero(r[pc]):
                f = r[pc]
                r = [K.sub(x, K.mul(f, y)) for x, y in zip(r, pr)]
        pc = None
        for c in range(ncols):
            if not K.is_zero(r[c]):
                pc = c
                break
        if pc is None:
            continue
        inv = K.inv(r[pc])
        r = [K.mul(x, inv) for x in r]
        piv_rows.append((pc, r))
        if log and len(piv_rows) % 10 == 0:
            log(len(piv_rows), seen)
        if target and len(piv_rows) >= target:
            break
    return len(piv_rows), seen


def quadric_rows(K, forms, d, D):
    """Yield the rows of the multiplication map (S_{D-2})^M -> S_D, lazily."""
    tgt = monomials(d, D)
    tix = {m: i for i, m in enumerate(tgt)}
    src = monomials(d, D - 2)
    for f in forms:
        for s in src:
            row = [None] * len(tgt)
            for (k, l), c in f.items():
                e = list(s)
                e[k] += 1
                e[l] += 1
                i = tix[tuple(e)]
                row[i] = c if row[i] is None else K.add(row[i], c)
            yield [K.zero() if x is None else x for x in row]
