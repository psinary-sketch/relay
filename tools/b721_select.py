# -*- coding: utf-8 -*-
"""b721_select.py -- (R331)(3)(i): THE RULE APPLIED. Prints the rule from data/b721_registrations.txt section (1) before its first
discriminant, then walks the negative fundamental discriminants with class number 2 and two units in increasing |D|, prints the used set
read from the earlier coefficient banks, and at each unused D the C2 table's reading from decomposition types alone -- the types and
classes of the primes, the bad primes, and the table's n0, shape and b(n0) by tools/b720_predict.py predict (imported unedited, over
tools/b718_classgroup.py and tools/b718_abstract.py, unedited). Stops at the second D whose b(n0) is neither -2 nor -1/2. No
representation count is read; no coefficient of b711's route. Writes no file: its print is entered into the registration by the Write tool.

THE CONTROLS FIRST: (S1) the table at the seven banked discriminants returns their banked n0 and b (-23: 48, -2 ; -15: 24, -2 ; -39: 120,
-2 ; -20: 36, -2 ; -47: 168, -2 ; -35: 135, -2 ; -40: 100, -1/2); (S2) a planted class -- the class above 2 at -40 set to the identity --
moves -40's off 100; (S3) the fundamental test on the known list of h = 2 discriminants below 100 (-15, -20, -24, -35, -40, -51, -52, -88,
-91), and the rejection of -60 (not fundamental) and -84 (C2 x C2, not class number 2).

  python -X utf8 -u tools/b721_select.py          prints; writes nothing
"""
import os
import re
import sys
import time
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_ = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b718_classgroup as CG   # noqa: E402  ### b718's, unedited
import b720_predict as PR      # noqa: E402  ### b720's, unedited: setup, predict

USED_BANKS = ('b711_coeffs.txt', 'b713_coeffs.txt', 'b717_coeffs.txt', 'b719_coeffs.txt', 'b720_coeffs.txt')
SKIP_VALUES = (Fraction(-2), Fraction(-1, 2))
LIMIT = 1000


def rd(name):
    with open(os.path.join(D_, name), encoding='utf-8') as fh:
        return fh.read().replace(chr(13), '')


def squarefree(m):
    m = abs(m)
    p = 2
    while p * p <= m:
        if m % (p * p) == 0:
            return False
        p += 1
    return True


def fundamental(D):
    if D % 4 == 1 or D % 4 == -3:
        return squarefree(D)
    if D % 4 == 0:
        m = D // 4
        return m % 4 in (2, 3) and squarefree(m)
    return False


def h_of(D):
    return len(CG.reduced_forms(D))


def cyclic(D):
    F, e, T, _ok = CG.group(D)
    return any(CG.order(x, e, T) == len(F) for x in F)


def used_set():
    out = {}
    for b in USED_BANKS:
        t = rd(b)
        for m in re.finditer(r'(?:\bD = |n0\()(-\d+)', t):
            out.setdefault(int(m.group(1)), set()).add(b)
    return out


def rule_text():
    t = rd('b721_registrations.txt').split(NL)
    i = t.index('## (1) THE RULE, printed before any discriminant is named ((R331)(3)(i))')
    out = []
    for l in t[i:]:
        if out and l.startswith('## '):
            break
        out.append(l)
    return [l for l in out if l.strip()]


def run():
    t0 = time.time()
    L = ['b721 -- (R331)(3)(i): THE RULE APPLIED BY tools/b721_select.py (%s); THE RULE FIRST, AS THE REGISTRATION CARRIES IT:' % (
        time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))] + ['  | ' + l for l in rule_text()] + ['']
    ok_all = True
    want = {-23: (48, -2), -15: (24, -2), -39: (120, -2), -20: (36, -2), -47: (168, -2), -35: (135, -2), -40: (100, Fraction(-1, 2))}
    for D, (nw, bw) in want.items():
        r = PR.predict(PR.setup(D))
        good = r['n'] == nw and r['b'] == bw
        ok_all &= good
        L.append('(S1) D = %d: the table`s n0 %s, b %s (banked %d, %s) -- %s' % (D, r['n'], r['b'], nw, bw, 'AS WANTED' if good else 'NOT AS WANTED'))
    S40 = PR.setup(-40)
    pl = PR.predict(S40, override={2: (0,)})
    ok_all &= pl['n'] != 100
    L.append('(S2) PLANT: at -40 the class above 2 set to the identity: n0 %s (not 100) -- %s' % (pl['n'], 'FAILS AS WANTED' if pl['n'] != 100 else 'DOES NOT FAIL'))
    known = [-15, -20, -24, -35, -40, -51, -52, -88, -91]
    got = [D for D in range(-5, -100, -1) if fundamental(D) and h_of(D) == 2]
    s3 = got == known and not fundamental(-60) and h_of(-84) == 4 and not cyclic(-84)
    ok_all &= s3
    L += ['(S3) the h = 2 fundamental discriminants below 100: %s (wanted %s) ; -60 fundamental %s ; -84 h %d, cyclic %s -- %s' % (
        got, known, fundamental(-60), h_of(-84), cyclic(-84), 'AS WANTED' if s3 else 'NOT AS WANTED'),
          '### THE CONTROLS: %s' % ('ALL AS WANTED' if ok_all else 'NOT AS WANTED -- NO DISCRIMINANT BELOW IS READ'), '']
    if not ok_all:
        return L, None
    used = used_set()
    L.append('## THE USED SET (the coefficient banks` `D = ` and `n0(` readings): ' + ' ; '.join(
        '%d (%s)' % (D, ', '.join(sorted(b))) for D, b in sorted(used.items(), key=lambda x: -x[0])))
    L.append('## THE WALK, h = 2, two units, fundamental, in increasing |D|:')
    out = []
    for D in range(-5, -LIMIT, -1):
        if not fundamental(D) or h_of(D) != 2:
            continue
        if D in used:
            L.append('  D = %d: USED -- passed over' % D)
            continue
        S = PR.setup(D)
        types = ' ; '.join('%d %s' % (p, CG.prime_class(D, p)[0] if CG.prime_class(D, p)[0] == 'inert' else
                                      '%s %s' % (CG.prime_class(D, p)[0], 'BAD' if S['log'][CG.prime_class(D, p)[1]] else 'good'))
                           for p in (2, 3, 5, 7, 11, 13))
        r = PR.predict(S)
        if r['n'] is None:
            L.append('  D = %d: types %s ; the table yields no n0 through the cut (bad primes %d) -- passed over' % (D, types, r['nbad']))
            continue
        fs = ' . '.join('%d^%d' % (p, k) for p, k, _t, _c in r['factors'])
        pick = r['b'] not in SKIP_VALUES
        L.append('  D = %d: types %s ; the table`s n0 = %d = %s, b(n0) = %s, a(n0) %d, the pair sum %s, the shape %s ; bad primes %d -- %s' % (
            D, types, r['n'], fs, r['b'], r['a'], r['pair'], r['shape'], r['nbad'],
            'TAKEN (value neither -2 nor -1/2)' if pick else 'passed over (value %s)' % r['b']))
        if pick:
            F = CG.reduced_forms(D)
            L.append('      the reduced forms %s ; the principal form %s ; its primes: %s' % (
                F, CG.principal(D), ' ; '.join('%d %s, class generator^%d' % (p, t, c[0]) for p, _k, t, c in r['factors'])))
            out.append((D, r))
            if len(out) == 2:
                break
    L += ['', '### ### **THE CONTROLS AS WANTED ; THE OUTPUT %s ; %d s.**' % (
        ' AND '.join('%d (n0 %d, b %s)' % (D, r['n'], r['b']) for D, r in out), int(time.time() - t0))]
    return L, out


if __name__ == '__main__':
    L, _out = run()
    print(NL.join(L))
