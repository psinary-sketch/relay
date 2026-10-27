# -*- coding: utf-8 -*-
"""b718_decomp.py -- (R328)(4)(ii): THE NAVIGATOR'S READING REPRODUCED by the seat's own tool, at the three discriminants already banked and
at no other: -23 (Q0 = x^2 + xy + 6y^2), -15 (x^2 + xy + 4y^2), -39 (Q1 = x^2 + xy + 10y^2). For n = 48, 24, 120: a(n) = r_Q1(n)/2, the
ordered pair sum SUM_{de = n, d, e >= 2} a(d) a(e), the number of ordered factorizations into three or more parts with every a(d_i)
nonzero, b(n) from the full log series and from a(n) - pair/2, and the proper divisors carrying a nonzero a. Each figure beside the
navigator's ((R328)(4)(ii), data/b718_ferry.txt :15); a figure that differs is printed DIFFERS and the seat's stands.
### THE CHECK FIRST: b(n) by the Omega derivation (tools/b718_classgroup.py) against each coefficient bank through its cut -- the least
### negative n, its b, the count of negatives and the negative list where the bank carries it; then a PLANTED ERROR (a(n) at the least
### negative's largest proper divisor with nonzero a raised by one) must move the comparison (FAILS AS WANTED).
### Writes data/b718_decomp.txt and .json through the membrane; nothing else. Route: `run`.
"""
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_, T_ = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T_)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b718_classgroup as CG   # noqa: E402

CASES = [  # (D, the bank, the navigator's n, the navigator's divisors {d: a(d)})
    (-23, 'b711_coeffs', 48, {4: 1, 6: 2, 8: 2, 12: 2, 16: 1, 24: 2}),
    (-15, 'b713_coeffs', 24, {4: 3, 6: 2}),
    (-39, 'b717_coeffs', 120, {4: 1, 10: 2, 12: 2, 30: 2, 40: 4}),
]
NAV = dict(a=4, pair=12, k3=0, b=-2)


def _bank(name):
    p = os.path.join(D_, name + '.json')
    with open(p, encoding='utf-8') as fh:
        return json.load(fh)


def compare(D, j, a, P, N):
    b, _Om = CG.log_coeffs(a, N, P)
    neg = [n for n in range(2, N + 1) if b[n] < 0]
    out = dict(cut=N, least=neg[0] if neg else None, b_least=str(b[neg[0]]) if neg else None, negatives=len(neg))
    rows = []
    if 'least_negative' in j:
        rows.append(('least negative', j['least_negative'], out['least']))
    if 'b' in j:
        rows.append(('b at the least', str(j['b']), out['b_least']))
    if 'negatives' in j:
        rows.append(('negatives', j['negatives'], out['negatives']))
    if 'negative_list' in j:
        rows.append(('the negative list', 'banked %d' % len(j['negative_list']), 'EQUAL' if list(j['negative_list']) == neg else 'UNEQUAL'))
    ok = all((str(w) == str(h)) if k != 'the negative list' else h == 'EQUAL' for k, w, h in rows)
    return ok, rows, b, neg


def main():
    t0 = time.time()
    L = ['b718 -- (R328)(4)(ii): THE NAVIGATOR`S READING REPRODUCED AT -23, -15 AND -39, THE BANKS` DISCRIMINANTS AND NO OTHER (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### a(n) = r_Q1(n)/2 by enumeration; b(n) by the Omega derivation of tools/b718_classgroup.py, exact; the banks` c(n) = b(n) log n.',
         '### THE CHECK FIRST, against each bank through its cut, then its planted error; the reading after.', '']
    J = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), cases=[])
    allok, plants = True, True
    for D, bank, n0, nav_div in CASES:
        j = _bank(bank)
        N = int(j.get('cut', 32532))
        P = CG.primes_upto(N)
        f = CG.principal(D)
        r = CG.r_form(f, N)
        a = [x // 2 for x in r]
        a[1] = 1
        ok, rows, b, neg = compare(D, j, a, P, N)
        allok &= ok
        L += ['### (CHECK) D = %d, Q1 = %r, data/%s.json through its cut %d: %s -- %s' % (
            D, f, bank, N, ' ; '.join('%s banked %s, here %s' % r_ for r_ in rows), 'AGREES' if ok else '### DIFFERS')]
        # the planted error
        divs = [d for d in range(2, n0) if n0 % d == 0 and a[d]]
        dp = max(divs)
        a2 = list(a)
        a2[dp] += 1
        ok2, rows2, _b2, _n2 = compare(D, j, a2, P, N)
        plants &= not ok2
        L += ['###   (PLANT) a(%d) raised by one: %s -- %s' % (dp, ' ; '.join('%s here %s' % (k, h) for k, _w, h in rows2),
                                                          'FAILS AS WANTED' if not ok2 else '### PASSES, NOT AS WANTED')]
        # the reading
        fig = dict(a=a[n0], pair=CG.pair_sum(a, n0), k3=CG.ordered_factorizations(a, n0, 3), b=b[n0])
        bal = fig['a'] - fig['pair'] / 2
        div = dict((d, a[d]) for d in divs)
        J['cases'].append(dict(D=D, n=n0, a=fig['a'], pair=fig['pair'], k3=fig['k3'], b=str(fig['b']), divisors=div,
                               least_negative=neg[0] if neg else None, check=ok, plant_fails=not ok2))
        rd = []
        for k in ('a', 'pair', 'k3', 'b'):
            rd.append('%s %s (the navigator`s %s) %s' % ({'a': 'a(n)', 'pair': 'the pair sum', 'k3': 'k >= 3 factorizations', 'b': 'b(n)'}[k],
                                                        fig[k], NAV[k], 'AGREES' if str(fig[k]) == str(NAV[k]) else '### DIFFERS'))
        L += ['', '  D = %d, n = %d = %s, the least negative here %s:' % (D, n0, ' . '.join('%d^%d' % kv for kv in sorted(CG.factor(n0, P).items())), neg[0] if neg else None)]
        L += ['    ' + x for x in rd]
        L += ['    a(n) - pair/2 = %s ; the full series %s ; EQUAL %s' % (bal, fig['b'], bal == fig['b'])]
        L += ['    the proper divisors with nonzero a: %s ; the navigator`s %s ; %s' % (
            ', '.join('%d (%d)' % kv for kv in sorted(div.items())), ', '.join('%d (%d)' % kv for kv in sorted(nav_div.items())),
            'AGREES' if div == nav_div else '### DIFFERS')]
        L += ['    each prime of n: %s' % ' ; '.join('%d %s %s, represented by Q1: %s' % (
            p, CG.prime_class(D, p)[0], CG.prime_class(D, p)[1], bool(a[p])) for p in sorted(CG.factor(n0, P)))]
        L += ['']
    nd = sum(1 for c in J['cases'] for k in ('a', 'pair', 'k3', 'b') if str(c[k]) != str(NAV[k])) + sum(1 for c, x in zip(J['cases'], CASES) if c['divisors'] != x[3])
    J.update(checks=allok, plants=plants, differs=nd, seconds=round(time.time() - t0, 1))
    L += ['### ### **THE CHECKS %s ; THE PLANTS %s ; THE NAVIGATOR`S FIGURES: %d OF 15 AGREE, %d DIFFER ; %.0f s.**' % (
        'AGREE 3 OF 3' if allok else 'NOT ALL AGREE', 'FAIL AS WANTED 3 OF 3' if plants else 'NOT AS WANTED', 15 - nd, nd, time.time() - t0)]
    import act_membrane as MEM
    import b718_record as REC
    for name, data in (('b718_decomp.txt', NL.join(L) + NL), ('b718_decomp.json', json.dumps(J, indent=1) + NL)):
        p = os.path.join(D_, name)
        MEM.guard_path('b718', p, REC.R.ROOT_EXCLUDE)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(data.encode('utf-8'))
        os.replace(p + '.tmp', p)
    print(NL.join(L))


if __name__ == '__main__':
    if sys.argv[1:] != ['run']:
        sys.exit('usage: b718_decomp.py run')
    main()
