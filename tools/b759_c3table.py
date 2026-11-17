# -*- coding: utf-8 -*-
"""tools/b759_c3table.py -- (R369)(6): THE TABLE OF APPENDIX A REPRODUCED, WITH A PLANTED ERROR. A reproduction and no registered prediction
(the navigator computed the table in its workspace before the ruling). Committed before its run; its one write data/b759_c3table.txt
(through standing.figbank). Reads no network and runs no lean process; imports tools/b718_abstract.py and tools/b750_cq_sign.py unchanged.

ROUTE ONE, the group-ring model of INSTRUMENTS I-105 (tools/b718_abstract.py): the cyclic group of order 3, each prime split with a class of
order 3; at each of the nine patterns (1,1), (2,1), (3,1), (2,2), (1,1,1), (4,1), (3,2), (2,1,1), (1,1,1,1): alpha by a_of, alpha*alpha as
pair_sum plus twice alpha, beta by b_lattice.
ROUTE TWO, the form's own count at discriminant -23, by the recursion of tools/b750_cq_sign.py (INSTRUMENTS :766): the primes below 30 that
split and that x^2 + xy + 6y^2 does not represent, read by the tool and wanted 2, 3, 13, 29; b(n) = c(n)/log n exactly at n = 6, 12, 24, 36,
78, 48, 72, 156, 2262, one instance of each pattern in the table's order. alpha(n) = rQ(n)/2 (the two units), alpha*alpha(n) the sum over
the divisors d of n of alpha(d) alpha(n/d); c(n) the tool's exact value (a sum of q_p log p, q_p rational), b(n) = c(n)/log n exactly where
q_p = b v_p(n) at each prime and no other prime enters.
ROUTE THREE, the proof's general steps over a range: (a) for one prime, beta(e) for e from 1 to 24 against the closed form of Step 4, 2/e
where e is even plus 6/e where e is an odd multiple of 3; (b) over each pattern of at most 8 prime factors counted with multiplicity: the
patterns containing none of (4,1), (3,2), (2,1,1), (1,1,1,1) are the one-part patterns and (1,1), (2,1), (3,1), (2,2), (1,1,1), and beta is
negative at none of them.
WANTED: alpha 2, 2, 2, 3, 2, 4, 4, 4, 6; alpha*alpha 4, 4, 8, 12, 4, 20, 24, 20, 36; beta 2, 2, 0, 0, 2, -2, -4, -2, -6, by routes one and
two alike. THE PLANT, printed before any use of the result: the wanted table with beta at (3,2) read -2 is reported unequal by each route,
the cell named.

  bank     the plant, the three routes and the verdict, written to data/b759_c3table.txt
  print    the same, printed and not written
"""
import os
import sys
import time
from fractions import Fraction

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b718_abstract as AB      # noqa: E402  ### INSTRUMENTS I-105, imported and not changed
import b750_cq_sign as CQ       # noqa: E402  ### INSTRUMENTS :766, imported and not changed (its tables at N = 3000 built at import)
import figbank as FB            # noqa: E402

NL = '\n'
ACT = 'b759'
BANK = os.path.join(D, 'b759_c3table.txt')
PATTERNS = ((1, 1), (2, 1), (3, 1), (2, 2), (1, 1, 1), (4, 1), (3, 2), (2, 1, 1), (1, 1, 1, 1))
INSTANCES = (6, 12, 24, 36, 78, 48, 72, 156, 2262)
WANTED_PRIMES = [2, 3, 13, 29]
WANTED = dict(alpha=(2, 2, 2, 3, 2, 4, 4, 4, 6), alpha2=(4, 4, 8, 12, 4, 20, 24, 20, 36), beta=(2, 2, 0, 0, 2, -2, -4, -2, -6))
FOUR = ((4, 1), (3, 2), (2, 1, 1), (1, 1, 1, 1))
ALLOWED = ((1, 1), (2, 1), (3, 1), (2, 2), (1, 1, 1))
G3 = AB.Group((3,))
G = (1,)   # ### a class of order 3


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def fr(x):
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else '%d/%d' % (x.numerator, x.denominator)


# ---------------------------------------------------------------- route one
def route_one():
    """{pattern: (alpha, alpha*alpha, beta)} by the group-ring model."""
    out = {}
    for pat in PATTERNS:
        primes = [('split', G)] * len(pat)
        alpha = AB.a_of(G3, primes, pat)
        a, b = AB.b_lattice(G3, primes, pat)
        out[pat] = (Fraction(alpha), Fraction(AB.pair_sum(a, pat) + 2 * a[pat]), Fraction(b[pat]))
    return out


# ---------------------------------------------------------------- route two
def split_unrepresented(bound=30):
    rq0 = CQ.form_counts(1, 1, 6, bound)
    return [p for p in CQ.primes_upto(bound - 1) if CQ.kronecker(CQ.D, p) == 1 and rq0[p] == 0]


def n_of(pat, primes):
    n = 1
    for e, p in zip(pat, primes):
        n *= p ** e
    return n


def exact_b(cd, n):
    """b where c(n) = b log n exactly (q_p = b v_p(n) at each prime of n, no other prime), else None."""
    fa = CQ.FAC[n]
    if any(p not in fa for p in cd):
        return None
    bs = set(Fraction(cd.get(p, 0)) / e for p, e in fa.items())
    return bs.pop() if len(bs) == 1 else None


def route_two():
    """(the primes read, {pattern: (n, alpha, alpha*alpha, beta or None)})."""
    primes = split_unrepresented()
    rq0 = CQ.form_counts(1, 1, 6, CQ.N)
    c = CQ.recursion(rq0)
    al = [Fraction(0)] + [Fraction(rq0[n], 2) for n in range(1, CQ.N + 1)]
    out = {}
    for pat, n0 in zip(PATTERNS, INSTANCES):
        n = n_of(pat, primes)
        a2 = sum(al[d] * al[n // d] for d in CQ.DIVS[n])
        out[pat] = (n, al[n], a2, exact_b(c[n], n))
    return primes, out


# ---------------------------------------------------------------- route three
def closed_form(e):
    return (Fraction(2, e) if e % 2 == 0 else Fraction(0)) + (Fraction(6, e) if e % 2 == 1 and e % 3 == 0 else Fraction(0))


def route_three_a(top=24):
    _a, b = AB.b_lattice(G3, [('split', G)], (top,))
    return [(e, Fraction(b[(e,)]), closed_form(e)) for e in range(1, top + 1)]


def partitions(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def contains(P, Q):
    """the pattern P contains Q: Q's parts matched to P's, each at most its match (both read in descending order)."""
    p, q = sorted(P, reverse=True), sorted(Q, reverse=True)
    return len(q) <= len(p) and all(x <= y for x, y in zip(q, p))


def route_three_b(top=8):
    rows = []
    for om in range(1, top + 1):
        for pat in partitions(om):
            primes = [('split', G)] * len(pat)
            _a, b = AB.b_lattice(G3, primes, pat)
            rows.append((pat, Fraction(b[pat]), [Q for Q in FOUR if contains(pat, Q)]))
    return rows


# ---------------------------------------------------------------- the comparison
def compare(table, wanted):
    """[(cell name, got, wanted)] for each cell that differs; table {pattern: (alpha, alpha2, beta)}."""
    bad = []
    for i, pat in enumerate(PATTERNS):
        got = table.get(pat)
        for j, key in enumerate(('alpha', 'alpha2', 'beta')):
            g = got[j] if got else None
            if g is None or Fraction(g) != Fraction(wanted[key][i]):
                bad.append(('%s at %s' % ({'alpha2': 'alpha*alpha'}.get(key, key), str(pat).replace(' ', '')), g, wanted[key][i]))
    return bad


def planted():
    w = dict((k, list(v)) for k, v in WANTED.items())
    w['beta'][PATTERNS.index((3, 2))] = -2
    return w


def run():
    L = ['%s -- (R369)(6): THE TABLE OF APPENDIX A REPRODUCED, WITH A PLANTED ERROR (%s, tools/b759_c3table.py)' % (ACT, _now()), '',
         '### a reproduction and no registered prediction: the navigator computed the table in its workspace before (R369). Route one the',
         '### group-ring model (tools/b718_abstract.py, INSTRUMENTS I-105); route two the form`s own count at -23 by the recursion of',
         '### tools/b750_cq_sign.py (INSTRUMENTS :766); route three the proof`s general steps over a range. Both tools imported unchanged.', '']
    r1 = route_one()
    primes, r2full = route_two()
    r2 = dict((p, v[1:]) for p, v in r2full.items())
    # ### THE PLANT FIRST
    pw = planted()
    p1, p2 = compare(r1, pw), compare(r2, pw)
    plant_ok = [c for c, _g, _w in p1] == ['beta at (3,2)'] and [c for c, _g, _w in p2] == ['beta at (3,2)']
    L += ['## THE PLANT, PRINTED BEFORE ANY USE OF THE RESULT: the wanted table with beta at (3,2) read -2',
          '  route one reports: %s' % ('; '.join('%s got %s, the plant %s' % (c, fr(g), w) for c, g, w in p1) or 'EQUAL'),
          '  route two reports: %s' % ('; '.join('%s got %s, the plant %s' % (c, fr(g) if g is not None else 'NOT EXACT', w) for c, g, w in p2) or 'EQUAL'),
          '  ### THE PLANT %s' % ('FAILS AS WANTED: each route reports it unequal, the cell named, beta at (3,2), and no other cell' if plant_ok
                                  else 'DOES NOT FAIL AS WANTED'), '']
    # ### ROUTE ONE
    L.append('## ROUTE ONE, THE GROUP-RING MODEL: C3, each prime split with the class of order 3 (alpha by a_of, alpha*alpha as pair_sum + 2 alpha, beta by b_lattice)')
    L.append('  %-12s %8s %12s %8s' % ('pattern', 'alpha', 'alpha*alpha', 'beta'))
    for pat in PATTERNS:
        a, a2, b = r1[pat]
        L.append('  %-12s %8s %12s %8s' % (str(pat).replace(' ', ''), fr(a), fr(a2), fr(b)))
    d1 = compare(r1, WANTED)
    L += ['  against the wanted table: %s' % ('EACH CELL AGREES, 27 of 27' if not d1 else 'DIFFERS at %s' % '; '.join('%s got %s, wanted %s' % (c, fr(g), w) for c, g, w in d1)), '']
    # ### ROUTE TWO
    L.append('## ROUTE TWO, THE FORM`S OWN COUNT AT -23 (x^2 + xy + 6y^2; the recursion of tools/b750_cq_sign.py, c(n) exact as a sum of q_p log p)')
    L.append('  the primes below 30 that split (the Kronecker symbol (-23/p) = 1) and that the form does not represent: %s ; wanted %s -> %s' % (
        primes, WANTED_PRIMES, 'AS WANTED' if primes == WANTED_PRIMES else 'NOT AS WANTED'))
    L.append('  %-12s %6s %8s %12s %8s' % ('pattern', 'n', 'alpha', 'alpha*alpha', 'beta'))
    inst_ok = True
    for pat, n0 in zip(PATTERNS, INSTANCES):
        n, a, a2, b = r2full[pat]
        inst_ok = inst_ok and n == n0
        L.append('  %-12s %6d %8s %12s %8s%s' % (str(pat).replace(' ', ''), n, fr(a), fr(a2), fr(b) if b is not None else 'NOT EXACT',
                                                '' if n == n0 else '  (the ruling`s instance %d)' % n0))
    d2 = compare(r2, WANTED)
    L += ['  the instances against the ruling`s 6, 12, 24, 36, 78, 48, 72, 156, 2262: %s' % ('EQUAL' if inst_ok else 'UNEQUAL'),
          '  against the wanted table: %s' % ('EACH CELL AGREES, 27 of 27' if not d2 else 'DIFFERS at %s' % '; '.join(
              '%s got %s, wanted %s' % (c, fr(g) if g is not None else 'NOT EXACT', w) for c, g, w in d2)), '']
    # ### ROUTE THREE
    ra = route_three_a()
    bad_a = [(e, b, c) for e, b, c in ra if b != c]
    L.append('## ROUTE THREE (a): ONE PRIME, beta(e) FOR e = 1..24 AGAINST THE CLOSED FORM OF STEP 4 (2/e where e is even, plus 6/e where e is an odd multiple of 3)')
    L.append('  ' + ' ; '.join('%d: %s%s' % (e, fr(b), '' if b == c else ' (closed form %s)' % fr(c)) for e, b, c in ra))
    L += ['  ### (a) %s' % ('HOLDS: 24 of 24 equal' if not bad_a else 'FAILS at e = %s' % [e for e, _b, _c in bad_a]), '']
    rb = route_three_b()
    avoid = [pat for pat, _b, cont in rb if not cont]
    want_avoid = sorted([(k,) for k in range(1, 9)] + list(ALLOWED))
    neg_avoid = [(pat, b) for pat, b, cont in rb if not cont and b < 0]
    set_ok = sorted(avoid) == want_avoid
    L.append('## ROUTE THREE (b): EVERY PATTERN OF AT MOST 8 PRIME FACTORS COUNTED WITH MULTIPLICITY (%d patterns), beta at the pattern by b_lattice' % len(rb))
    for pat, b, cont in rb:
        L.append('  %-20s beta %-8s %s' % (str(pat).replace(' ', ''), fr(b), 'contains %s' % ', '.join(str(q).replace(' ', '') for q in cont) if cont else 'contains none of the four'))
    L += ['  the patterns containing none of (4,1), (3,2), (2,1,1), (1,1,1,1): %d, %s the one-part patterns (1) to (8) and (1,1), (2,1), (3,1), (2,2), '
          '(1,1,1)' % (len(avoid), 'EQUAL TO' if set_ok else 'NOT EQUAL TO'),
          '  beta negative among them: %d %s' % (len(neg_avoid), [(str(p).replace(' ', ''), fr(b)) for p, b in neg_avoid]),
          '  ### (b) %s' % ('HOLDS' if set_ok and not neg_avoid else 'FAILS'), '']
    agree = not d1 and not d2 and primes == WANTED_PRIMES and inst_ok
    holds = not bad_a and set_ok and not neg_avoid
    if agree and holds and plant_ok:
        verdict = 'EACH CELL AGREES BY ROUTES ONE AND TWO ; (a) AND (b) HOLD ; THE PLANT FAILS AS WANTED: the law enters as a theorem by written proof'
        outcome = 'REPRODUCED'
    else:
        first = (d1 or d2)[0][0] if (d1 or d2) else ('route two`s primes' if primes != WANTED_PRIMES else 'route two`s instances' if not inst_ok
                                                     else '(a)' if bad_a else '(b)' if not (set_ok and not neg_avoid) else 'the plant')
        verdict = 'NOT REPRODUCED at %s: the law enters as observed' % first
        outcome = 'NOT REPRODUCED at %s' % first
    L.append('### ### **THE TABLE OF APPENDIX A: %s ; ROUTE ONE %s ; ROUTE TWO %s ; (a) %s ; (b) %s ; THE PLANT %s.**' % (
        outcome, 'AGREES 27 OF 27' if not d1 else 'DIFFERS %d' % len(d1), 'AGREES 27 OF 27' if not d2 else 'DIFFERS %d' % len(d2),
        'HOLDS' if not bad_a else 'FAILS', 'HOLDS' if set_ok and not neg_avoid else 'FAILS', 'FAILS AS WANTED' if plant_ok else 'NOT AS WANTED'))
    L.append('### %s' % verdict)
    return L


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['bank']:
        L_ = run()
        r_ = FB.write(BANK, NL.join(L_))
        print(NL.join(L_))
        print('written data/b759_c3table.txt ; figbank: %s' % r_['why'])
    elif a[:1] == ['print']:
        print(NL.join(run()))
    else:
        sys.exit(__doc__)
