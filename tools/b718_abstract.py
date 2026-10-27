# -*- coding: utf-8 -*-
"""b718_abstract.py -- (R328)(4)(iii): the group-ring model of log(Z_Q1/2) on the bad-supported indices, abstract: no discriminant, no
prime -- a finite abelian group G, and a configuration of "bad" primes, each split with the class g != 0 of one prime ideal above it (the
other g^-1), or ramified with a class g of order 2; each with its exponent in n. a(e) for each divisor exponent vector e is the number of
ideals of that norm in the principal class; b(e) by the Omega derivation on the divisor lattice, exact. Imported by
tools/b718_derivation.py; writes nothing. Route `explore` prints the census of negative values by Omega and writes nothing.
"""
import itertools
import sys
from fractions import Fraction

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


class Group:
    def __init__(self, orders):
        self.orders = tuple(orders)
        self.elems = list(itertools.product(*[range(m) for m in orders]))
        self.zero = tuple(0 for _ in orders)

    def add(self, x, y):
        return tuple((a + b) % m for a, b, m in zip(x, y, self.orders))

    def mul(self, k, x):
        return tuple((k * a) % m for a, m in zip(x, self.orders))

    def neg(self, x):
        return self.mul(-1, x)

    def order(self, x):
        k = 1
        while self.mul(k, x) != self.zero:
            k += 1
        return k

    def name(self):
        return ' x '.join('C%d' % m for m in self.orders)


def local(G, prime, j):
    """{class: count} of the ideals of norm p^j: split (2i - j) g for i = 0..j; ramified j g."""
    t, g = prime
    if t == 'ram':
        return {G.mul(j, g): 1}
    out = {}
    for i in range(j + 1):
        c = G.mul(2 * i - j, g)
        out[c] = out.get(c, 0) + 1
    return out


def a_of(G, primes, e):
    dist = {G.zero: 1}
    for pr, j in zip(primes, e):
        if j == 0:
            continue
        loc = local(G, pr, j)
        new = {}
        for x, cx in dist.items():
            for y, cy in loc.items():
                z = G.add(x, y)
                new[z] = new.get(z, 0) + cx * cy
        dist = new
    return dist.get(G.zero, 0)


def lattice(k):
    return list(itertools.product(*[range(x + 1) for x in k]))


def b_lattice(G, primes, k):
    """{e: (a(e), b(e))} over the divisor lattice of exponent vector k, b by the Omega derivation."""
    L = sorted(lattice(k), key=sum)
    a = dict((e, a_of(G, primes, e)) for e in L)
    b = {}
    for e in L:
        Om = sum(e)
        if Om == 0:
            continue
        acc = Fraction(0)
        for f in L:
            if 0 < sum(f) < Om and all(x <= y for x, y in zip(f, e)):
                g = tuple(y - x for x, y in zip(f, e))
                if a[g] and b[f]:
                    acc += sum(f) * b[f] * a[g]
        b[e] = (Om * a[e] - acc) / Om
    return a, b


def pair_sum(a, e):
    tot = 0
    for f in a:
        if 0 < sum(f) < sum(e) and all(x <= y for x, y in zip(f, e)):
            tot += a[f] * a[tuple(y - x for x, y in zip(f, e))]
    return tot


def prime_types(G):
    """one representative of each prime kind up to g ~ -g: split with g != 0, ramified with g of order 2."""
    seen, out = set(), []
    for g in G.elems:
        if g == G.zero:
            continue
        key = min(g, G.neg(g))
        if key not in seen:
            seen.add(key)
            out.append(('split', key))
    for g in G.elems:
        if g != G.zero and G.order(g) == 2:
            out.append(('ram', g))
    return out


def configs(G, Om, rmin=2):
    """every multiset of r >= rmin distinct primes (kinds may repeat: two primes of one kind are two primes) with exponents summing to Om,
    up to the order of the primes."""
    kinds = prime_types(G)
    for r in range(rmin, Om + 1):
        for comp in _compositions(Om, r):
            for ks in itertools.combinations_with_replacement(range(len(kinds)), r):
                pairs = sorted(zip(ks, comp))
                if list(zip(ks, comp)) != pairs:
                    continue
                yield [kinds[x] for x in ks], tuple(comp)


def _compositions(n, r):
    if r == 1:
        if n >= 1:
            yield (n,)
        return
    for x in range(1, n - r + 2):
        for rest in _compositions(n - x, r - 1):
            yield (x,) + rest


GROUPS = [(2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), (12,), (2, 2), (2, 4), (3, 3), (2, 6), (2, 2, 2)]


def census(groups=GROUPS, oms=(4, 5, 6), verbose=True):
    """for each Omega: the negative configurations, their b values, and the minimal ones (no proper divisor with b < 0)."""
    out = {}
    for orders in groups:
        G = Group(orders)
        for Om in oms:
            seen = set()
            for primes, k in configs(G, Om):
                key = (tuple(primes), k)
                if key in seen:
                    continue
                seen.add(key)
                a, b = b_lattice(G, primes, k)
                if b[k] < 0:
                    minimal = not any(b[f] < 0 for f in b if f != k)
                    rec = out.setdefault(Om, dict(neg=0, minimal=0, values={}, minvalues={}, ap={}))
                    rec['neg'] += 1
                    rec['values'][str(b[k])] = rec['values'].get(str(b[k]), 0) + 1
                    if minimal:
                        rec['minimal'] += 1
                        rec['minvalues'][str(b[k])] = rec['minvalues'].get(str(b[k]), 0) + 1
                        apk = (a[k], pair_sum(a, k))
                        rec['ap'][str(apk)] = rec['ap'].get(str(apk), 0) + 1
        if verbose:
            print('  %-12s done' % G.name(), flush=True)
    return out


def describe(G, primes, k):
    return ' . '.join('%s%s^%d' % ('p' if t == 'split' else 'r', ''.join(str(x) for x in g), j) for (t, g), j in zip(primes, k))


def listing(orders, oms=(4, 5)):
    G = Group(orders)
    rows = []
    for Om in oms:
        for primes, k in configs(G, Om):
            a, b = b_lattice(G, primes, k)
            if b[k] < 0 and not any(b[f] < 0 for f in b if f != k):
                rows.append((Om, describe(G, primes, k), a[k], pair_sum(a, k), b[k]))
    return rows


if __name__ == '__main__':
    if sys.argv[1:2] == ['list']:
        for row in listing(tuple(int(x) for x in sys.argv[2].split(','))):
            print('  Omega %d  %-28s a %3d  pair %3d  b %s' % row)
        sys.exit(0)
    if sys.argv[1:2] != ['explore']:
        sys.exit('usage: b718_abstract.py explore [maxOmega] | list <orders, e.g. 4 or 2,2>')
    mo = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    gs = [tuple(int(x) for x in s.split(',')) for s in sys.argv[3].split(';')] if len(sys.argv) > 3 else GROUPS
    res = census(groups=gs, oms=tuple(range(4, mo + 1)))
    for Om in sorted(res):
        r = res[Om]
        print('Omega %d: negative %d, minimal %d ; values %s ; minimal values %s ; minimal (a, pair) %s' % (
            Om, r['neg'], r['minimal'], r['values'], r['minvalues'], r['ap']))
