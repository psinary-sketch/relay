# -*- coding: utf-8 -*-
"""b720_predict.py -- (R330)(3)(i), the order data/b720_registrations.txt (i) fixes: the primes' classes at -35 and -40 from the reduced
forms, and the shape rule's prediction of n0 and b(n0) at each, before any coefficient is computed. Carried from tools/b719_predict.py by
tools/b720_carry.py (data/b720_carry_predict.txt) and repaired at the carry: the substitution named tools/b719_classgroup.py and
tools/b719_abstract.py, which do not exist -- b718's two are imported unedited, as at b719; the controls P1 read the five banked cases; the
discriminants -35 and -40 (the repair diff data/b720_repairdiff_predict.txt).

THE RULE (data/b718_derivation.txt step 7 and its grade :121-:127): n0 is the least n instantiating, over D's bad primes with their
classes, a minimal negative shape of Cl(K). Read operationally: over the n <= 32532 supported on bad primes (a prime is bad when it is
split or ramified and the classes of the prime ideals above it are not the identity; an inert prime is never bad), in increasing order,
b(n) is computed by the group-ring model of tools/b718_abstract.py (the divisor lattice of n's exponent vector, each prime its kind and
class, a(e) the number of principal ideals of that norm, b by the Omega derivation, exact); the first n with b(n) < 0 is the prediction. No
r_Q1 is enumerated and no coefficient of b711's route is read: the prediction stands on the classes alone.

THE CONTROLS FIRST: (P1) the rule at the five banked discriminants returns their n0 and b (-23: 48, -15: 24, -39: 120, -20: 36, -47: 168;
-2 each; data/b718_decomp.txt :9, :21, :33 and data/b719_coeffs.txt :45); (P2) a planted error -- the class of the prime ideal above 2 at
-39 set to the identity -- moves the -39 prediction off 120, failing as wanted; (P3) each group's axioms (tools/b718_classgroup.py group).
Then -35 and -40. Writes data/b720_prediction.txt (route `bank`); `dry` prints and writes nothing.
"""
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_ = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b718_classgroup as CG   # noqa: E402  ### b718's, imported unedited
import b718_abstract as AB     # noqa: E402  ### b718's, imported unedited

CUT = 32532
P = CG.primes_upto(CUT)
TARGETS = (-35, -40)


def setup(D):
    F, e, T, ok = CG.group(D)
    h = len(F)
    gen = [x for x in F if CG.order(x, e, T) == h]
    if not gen:
        sys.exit('### Cl(%d) NOT CYCLIC -- THE MODEL`S LOG TABLE NEEDS A CYCLIC GROUP' % D)
    g = gen[0]
    log, y = {e: 0}, e
    for k in range(1, h):
        y = T[(y, g)]
        log[y] = k
    G = AB.Group((h,))
    kinds = {}
    for p in P:
        t, f = CG.prime_class(D, p)
        if t == 'inert':
            continue
        kinds[p] = (t, (log[f],), f)
    return dict(D=D, F=F, e=e, T=T, ok=ok, h=h, gen=g, log=log, G=G, kinds=kinds)


def bad_primes(S, override=None):
    out = []
    for p, (t, c, f) in sorted(S['kinds'].items()):
        if override and p in override:
            c = override[p]
        if c != (0,):
            out.append((p, t, c))
    return out


def bad_supported(bad, N):
    """every n <= N supported on the bad primes, with its exponent vector over its own primes, in increasing n."""
    out = []

    def rec(i, n, fac):
        if fac:
            out.append((n, tuple(fac)))
        for j in range(i, len(bad)):
            p = bad[j][0]
            if n * p > N:
                break
            m, k = n, 0
            while m * p <= N:
                m, k = m * p, k + 1
                rec(j + 1, m, fac + [(j, k)])
    rec(0, 1, [])
    return sorted(out)


def predict(S, override=None):
    bad = bad_primes(S, override)
    G = S['G']
    for n, fac in bad_supported(bad, CUT):
        primes = [('split' if bad[j][1] == 'split' else 'ram', bad[j][2]) for j, _k in fac]
        k = tuple(x for _j, x in fac)
        a, b = AB.b_lattice(G, primes, k)
        if b[k] < 0:
            return dict(n=n, b=b[k], a=a[k], pair=AB.pair_sum(a, k), shape=AB.describe(G, primes, k),
                        factors=[(bad[j][0], x, bad[j][1], bad[j][2]) for j, x in fac], nbad=len(bad))
    return dict(n=None, nbad=len(bad))


def form_s(f):
    a, b, c = f
    return '%dx^2 %s %dxy + %dy^2' % (a, '+' if b >= 0 else '-', abs(b), c) if b else '%dx^2 + %dy^2' % (a, c)


def run():
    L, t0 = [], time.time()
    L += ['b720 -- (R330)(3)(i): THE PRIMES` CLASSES AT -35 AND -40 AND THE SHAPE RULE`S PREDICTION OF n0 AND b(n0), BEFORE ANY COEFFICIENT (%s)' % (
        time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
          '### the rule: data/b718_derivation.txt step 7 (:109-:118) and its grade (:121-:127), read operationally as this tool`s docstring states;',
          '### b(n) by tools/b718_abstract.py`s group-ring model over the classes alone (no r_Q1, no coefficient of b711`s route). THE CONTROLS FIRST.', '']
    want = {-23: (48, -2), -15: (24, -2), -39: (120, -2), -20: (36, -2), -47: (168, -2)}
    ok_all = True
    for D, (n_w, b_w) in want.items():
        S = setup(D)
        r = predict(S)
        good = (r['n'] == n_w and r['b'] == b_w and all(S['ok'].values()))
        ok_all &= good
        L += ['### (P1) D = %d: Cl C%d, axioms %s ; bad primes <= %d: %d ; the rule`s n0 %s, b %s, shape %s (wanted %d, %d) -- %s' % (
            D, S['h'], 'ALL HOLD' if all(S['ok'].values()) else S['ok'], CUT, r['nbad'], r['n'], r['b'], r.get('shape'), n_w, b_w,
            'AS WANTED' if good else 'NOT AS WANTED')]
    S39 = setup(-39)
    pl = predict(S39, override={2: (0,)})
    pl_ok = pl['n'] != 120
    ok_all &= pl_ok
    L += ['### (P2) PLANT: at -39 the class above 2 set to the identity: the rule`s n0 %s, b %s (not 120) -- %s' % (
        pl['n'], pl.get('b'), 'FAILS AS WANTED' if pl_ok else 'DOES NOT FAIL'),
          '### THE CONTROLS: %s' % ('ALL AS WANTED' if ok_all else 'NOT AS WANTED -- NO FIGURE BELOW IS READ'), '']
    res = {}
    for D in TARGETS:
        S = setup(D)
        L += ['## D = %d: h = %d ; Cl(K) cyclic of order %d, generator %s ; the group`s axioms %s' % (
            D, S['h'], S['h'], form_s(S['gen']), 'ALL HOLD' if all(S['ok'].values()) else S['ok'])]
        for p in (2, 3, 5, 7, 11, 13):
            t, f = CG.prime_class(D, p)
            if t == 'inert':
                L += ['  p = %d: inert (the ideal (p) principal, of norm p^2; never bad)' % p]
            else:
                c = S['log'][f]
                L += ['  p = %d: %s ; a prime ideal above it in the class of %s (generator^%d) ; its order %d ; %s' % (
                    p, t, form_s(f), c, CG.order(f, S['e'], S['T']), 'GOOD (principal)' if c == 0 else 'BAD')]
        r = predict(S)
        res[D] = r
        if r['n'] is None:
            L += ['  THE RULE`S PREDICTION: NO bad-supported n <= %d with b(n) < 0 (bad primes %d) -- the rule yields none; n0 predicted NOT SCORABLE through the cut' % (CUT, r['nbad']), '']
            continue
        fs = ' . '.join('%d^%d' % (p, k) for p, k, _t, _c in r['factors'])
        L += ['  THE RULE`S PREDICTION: n0 = %d = %s ; b(n0) = %s ; a(n0) %d, the pair sum %s ; the shape %s ; bad primes <= %d: %d' % (
            r['n'], fs, r['b'], r['a'], r['pair'], r['shape'], CUT, r['nbad']),
              '  its primes: ' + ' ; '.join('%d %s, class generator^%d' % (p, t, c[0]) for p, _k, t, c in r['factors']), '']
    L += ['### ### **THE CONTROLS %s ; PREDICTED n0(-35) = %s, b = %s ; PREDICTED n0(-40) = %s, b = %s ; %d s.**' % (
        'AS WANTED' if ok_all else 'NOT AS WANTED', res[-35]['n'], res[-35].get('b'), res[-40]['n'], res[-40].get('b'), int(time.time() - t0))]
    return L, ok_all


if __name__ == '__main__':
    route = sys.argv[1] if len(sys.argv) > 1 else 'dry'
    L, ok = run()
    print(NL.join(L))
    if route == 'bank':
        if not ok:
            sys.exit('### THE CONTROLS NOT AS WANTED -- NOTHING WRITTEN')
        p = os.path.join(D_, 'b720_prediction.txt')
        with open(p + '.tmp', 'wb') as fh:
            fh.write((NL.join(L) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/b720_prediction.txt')
