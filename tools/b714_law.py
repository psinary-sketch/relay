# -*- coding: utf-8 -*-
"""b714_law.py -- (R324)(7), THE LAW'S IDENTITY, read before any other computation of this act: the formula data/b713_predictions.txt was
computed by, printed from its tool by path and line, beside the words of data/b710_registrations.txt (i); the source of each constant; Q0's
pairs 11 and 15 under the -15 tool's evaluation (b713's (C1), data/b713_onsets.json :81-:115) beside b710's committed F2 predictions; the
difference named a constant, an approximation or a form; the reading ONE LAW, TWO EVALUATIONS or TWO FORMS, and the form each test used.

### NOTHING ON THE ROUTE IS RECOMPUTED: C and r are read from the banks (b713_predictions.json, b713_onsets.json c1, b709_pairs.txt), and the
### two fixed points are iterated in floats from them (the reading needs the fixed points only). Controls first, then the figures.
### Routes: `bank [dry]` -> data/b714_law.txt. Written by the Write tool at b714; it writes that bank alone. Run as `python -I -X utf8`.
"""
import ctypes
import hashlib
import json
import math
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
NL = chr(10)
ACT = 'b714'
OUT = os.path.join(D, 'b714_law.txt')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

F2 = (19.065093, 7.997097)          # ### data/b710_registrations.txt :26 (data/b710_fit.txt :21)
F2_PRED = {11: 12294837.0, 15: 14776939.6}   # ### data/b711_pairs.txt :12, :13 (b710_registrations :34, :36 to the unit)
R_Q0 = {11: 1.216894664e-5, 15: 1.022443029e-5}  # ### data/b709_pairs.txt :52, :56 (b710_registrations :34, :36)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def free_mb():
    class M(ctypes.Structure):
        _fields_ = [('l', ctypes.c_ulong), ('load', ctypes.c_ulong), ('tot', ctypes.c_ulonglong), ('avail', ctypes.c_ulonglong),
                    ('tp', ctypes.c_ulonglong), ('ap', ctypes.c_ulonglong), ('tv', ctypes.c_ulonglong), ('av', ctypes.c_ulonglong),
                    ('ae', ctypes.c_ulonglong)]
    m = M()
    m.l = ctypes.sizeof(M)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return m.avail // (1 << 20), m.tot // (1 << 20)


def mid(s):
    """the midpoint of a banked ball string '[mid +/- rad]' or a plain number."""
    if isinstance(s, (int, float)):
        return float(s)
    return float(s.strip().strip('[]').split('+/-')[0])


def rad(s):
    """the ball's radius plus half a unit in the last printed digit of its midpoint: the width the banked digits carry."""
    if isinstance(s, (int, float)):
        return 0.0
    body = s.strip().strip('[]')
    m = body.split('+/-')[0].strip()
    r = float(body.split('+/-')[1]) if '+/-' in body else 0.0
    mant, _, ex = m.lower().partition('e')
    dec = len(mant.split('.')[1]) if '.' in mant else 0
    return r + 0.5 * 10.0 ** (-dec + (int(ex) if ex else 0))


def between(f, lo_args, hi_args, want):
    """f is monotone in each argument; (lo, hi, inside) for the banked figure want."""
    a, b = f(*lo_args), f(*hi_args)
    lo, hi = min(a, b), max(a, b)
    return lo, hi, lo <= want <= hi


def lines(rel, *ns):
    t = open(os.path.join(ROOT, rel), encoding='utf-8').read().split(NL)
    return ['    %s :%d  %s' % (rel, n, t[n - 1].rstrip()) for n in ns]


def fixed(a, b, r, n0=None):
    """the fixed point of n = (a + b log(n + 1)) / r, iterated in floats from a/r to a change below 1e-9."""
    n = a / r if n0 is None else n0
    for _ in range(500):
        n2 = (a + b * math.log(n + 1)) / r
        if abs(n2 - n) < 1e-9:
            return n2
        n = n2
    return n


def first_order(C, r):
    return fixed(4 * math.log(4 * C), 8.0, r)


def bank(*a):
    fm, tm = free_mb()
    L = ['%s -- (R324)(7): THE LAW`S IDENTITY, READ BEFORE ANY OTHER COMPUTATION OF THIS ACT (%s)' % (ACT, utc()), '',
         '### free memory %d MB of %d MB before the run (the hold 2560 MB, (R324)(11)). No route recomputed: C and r read from the banks.' % (fm, tm), '',
         '## I. THE FORMULA data/b713_predictions.txt WAS COMPUTED BY, FROM ITS TOOL BY PATH AND LINE']
    L += lines('tools/b713_predict.py', 57, 58, 60, 61, 63, 76, 78, 84, 85)
    L += ['  ### the constant C: tools/b709_pairs.py constants_for709 (b675`s constants_for line for line), called with onset cap 1 (b713_predict :76):']
    L += lines('tools/b709_pairs.py', 170, 179, 180, 181, 187, 188)
    L += ['  ### the rate r: b705`s r_of (b713_predict :78), r(rho) = log |1 - 1/rho`| (b713_predict :5); the exponent 8 and the 4 in 4 log(4C) fixed in law() (:60, :63).',
          '', '## II. THE WORDS OF data/b710_registrations.txt (i)']
    L += lines('data/b710_registrations.txt', 20, 21, 22, 25, 26, 27, 28, 29, 34, 36, 43)

    # ---------------------------------------------------------------- controls
    P = json.load(open(os.path.join(D, 'b713_predictions.json'), encoding='utf-8'))
    O = json.load(open(os.path.join(D, 'b713_onsets.json'), encoding='utf-8'))
    L += ['', '## III. THE CONTROLS, BEFORE THE FIGURES']
    ok = []
    l1 = []
    for row in P['rows']:
        if row.get('reach'):
            continue
        C, dC, r, dr = mid(row['C']), rad(row['C']), mid(row['r']), rad(row['r'])
        lo, hi, ins = between(first_order, (C - dC, r + dr), (C + dC, r - dr), row['n_pred_float'])
        l1.append((row['k'], lo, hi, row['n_pred_float'], ins))
    p1 = len(l1) == 8 and all(x[4] for x in l1)
    ok.append(p1)
    L += ['  (L1) POS: the first-order form r n = 4 log(4C) + 8 log(n + 1), over b713_predictions.json`s own C and r with the width their banked',
          '       digits carry (each ball`s radius plus half a unit in its midpoint`s last printed digit; the -15 zeros certified to ~1e-6, so r',
          '       is banked to five or six figures), holds the bank`s n_pred_float at each of the eight -15 pairs: ' +
          ' ; '.join('%d [%.1f, %.1f] holds %.4f %s' % (k, lo, hi, b, 'IN' if i else 'OUT') for k, lo, hi, b, i in l1) +
          ' -- the widest interval %.1f, beside the window`s half-width 0.01 n (%.0f at pair 1) -- %s' % (
              max(x[2] - x[1] for x in l1), 0.01 * l1[0][3], 'AS WANTED' if p1 else 'NOT AS WANTED')]
    pn1 = all(not (lo <= 1.001 * b <= hi) for _k, lo, hi, b, _i in l1)
    ok.append(pn1)
    L += ['  (NEG1) the same intervals do NOT hold each n_pred moved by 0.1%% (x 1.001), so (L1) can fail: %s -- %s' % (
        ' ; '.join('%d %s' % (k, 'OUT' if not (lo <= 1.001 * b <= hi) else 'IN') for k, lo, hi, b, _i in l1), 'FAILS AS WANTED' if pn1 else 'NOT AS WANTED')]
    c1 = {u['idx']: u for u in O['c1']}
    l3 = [(k, first_order(mid(c1[k]['C']), mid(c1[k]['r'])), mid(c1[k]['n_pred'])) for k in (11, 15)]
    p3 = all(abs(n - b) < 0.05 for _k, n, b in l3)
    ok.append(p3)
    L += ['  (L2) POS: the same form, from b713_onsets.json c1`s C and r at Q0 (:91-:92, :108-:109), reproduces c1`s n_pred (:95, :112): ' +
          ' ; '.join('%d %.4f/%.6f' % x for x in l3) + ' -- %s' % ('AS WANTED' if p3 else 'NOT AS WANTED')]
    h = 0.5e-6                       # ### alpha and beta banked to six decimals (b710_fit.txt :21)
    R_RAD = {11: 4.96e-15 + 0.5e-14, 15: 4.59e-15 + 0.5e-14}   # ### b709_pairs :52, :56: the radius plus half a unit of the printed r
    f2 = lambda a_, b_, r_: fixed(a_, b_, r_)
    l2 = [(k,) + between(f2, (F2[0] - h, F2[1] - h, R_Q0[k] + R_RAD[k]), (F2[0] + h, F2[1] + h, R_Q0[k] - R_RAD[k]), F2_PRED[k]) + (F2_PRED[k],)
          for k in (11, 15)]
    p2 = all(x[3] for x in l2)
    ok.append(p2)
    L += ['  (L3) POS: F2, r n = alpha + beta log(n + 1) with alpha 19.065093, beta 7.997097 (six decimals, b710_fit :21) and b709`s r (:52, :56),',
          '       over the width those digits carry, holds b710`s committed predictions (b710_fit :38-:39, b711_pairs :12-:13): ' +
          ' ; '.join('%d [%.1f, %.1f] holds %.1f %s' % (k, lo, hi, w, 'IN' if i else 'OUT') for k, lo, hi, i, w in l2) +
          ' -- %s' % ('AS WANTED' if p2 else 'NOT AS WANTED')]
    neg = [(k, fixed(F2[0], F2[1], mid(c1[k]['r'])), mid(c1[k]['n_pred'])) for k in (11, 15)]
    pn = all(abs(n - b) > 1000 for _k, n, b in neg)
    ok.append(pn)
    L += ['  (NEG) F2 put in the place of the first-order form at c1`s own r does NOT give c1`s n_pred (the difference over 1000): ' +
          ' ; '.join('%d %.1f vs %.1f' % x for x in neg) + ' -- %s' % ('FAILS AS WANTED' if pn else 'NOT AS WANTED')]

    # ---------------------------------------------------------------- figures
    L += ['', '## IV. THE FIGURES: Q0`S PAIRS 11 AND 15, THE TWO COMPUTATIONS']
    rows = []
    for k in (11, 15):
        C, r = mid(c1[k]['C']), mid(c1[k]['r'])
        n1, n2 = mid(c1[k]['n_pred']), F2_PRED[k]
        a1 = 4 * math.log(4 * C)
        lg = math.log(n2 + 1)
        a2eff = F2[0] + (F2[1] - 8.0) * lg
        CF2 = math.exp(F2[0] / 4) / 4
        rows.append((k, n1, n2))
        L += ['  pair %d | the -15 tool`s evaluation (b713 c1, T0` %d): alpha = 4 log(4C) = %.6f from C %.10f (this pair`s, b709`s route), beta 8 ; n %.6f' % (
                  k, c1[k]['T0'], a1, C, n1),
              '          | b710`s F2: alpha %.6f, beta %.6f, fitted once over the ten pairs (b710_registrations :24-:26), the same for every pair ; n %.1f' % (
                  F2[0], F2[1], n2),
              '          | F2 written as alpha_eff + 8 log(n + 1) at n: alpha_eff %.6f, the C it reads exp(alpha/4)/4 = %.6f (b710_registrations :29: "near 29")' % (a2eff, CF2),
              '          | F2 - the -15 tool: %.1f in n (%.4f%%) ; alpha_eff - 4 log(4C) = %.6f ; r x (F2 - the -15 tool) = %.6f' % (
                  n2 - n1, 100 * (n2 - n1) / n1, a2eff - a1, r * (n2 - n1))]
    L += ['', '## V. THE DIFFERENCE NAMED, AND THE READING',
          '  ### the rule of the reading: ONE LAW where the two computations use one formula with one definition of each constant (they differ in',
          '  ### digits only); TWO EVALUATIONS where the formula and the definitions agree and an input differs (a list, a height, a precision);',
          '  ### TWO FORMS where a constant is defined differently in the two.',
          '  the difference: A CONSTANT, DEFINED TWO WAYS. Both computations solve r n = alpha + beta log(n + 1). In the -15 tool`s (b713_predict',
          '  law() :57-:68, b713`s (C1) and its -15 test) alpha is 4 log(4C) with C the pair`s own constant from b709`s route and beta is the',
          '  route`s 8 -- the route`s onset equation read to first order (b710_registrations :20-:23). In b710`s F2 (:25-:26) alpha and beta are',
          '  two numbers fitted once by least squares to the ten ONSETS of Q0`s pairs 5-10, 12-14, 16 at T0` 325 and used for every pair. Not',
          '  an approximation of one by the other: F2 reads no C; the first-order form reads no onset.',
          '  ### ### **THE READING: TWO FORMS.**',
          '  the form each test used:',
          '    b710`s fit control and b711`s (C1) (the ten re-computed at 415 and 445) and b711`s test of pairs 11 and 15 (data/b711_pairs.txt',
          '      :4, :8-:15): F2, the window [0.9, 1.1] -- pairs 11, 15 WITHIN at n*/F2 0.998460, 0.998079.',
          '    b713`s (C1) at Q0 (data/b713_onsets.txt :8-:9) and b713`s -15 test (:12-:19, the window [0.99, 1.01], data/b712_registrations.txt',
          '      :46): the first-order form, C per pair -- Q0 11, 15 at ratio 1.000005, 1.000004; the eight -15 pairs HELD.',
          '    b713`s NEG (4 log 4C struck): the first-order form less its constant term, OUTSIDE as wanted (data/b713_onsets.txt :8-:9).',
          '  the -15 result stands as the test of its own form, the first-order form with C per pair; it is not a test of F2, and b711`s is not',
          '  a test of the first-order form.']
    allok = all(ok)
    L += ['', '### ### **CONTROLS %d OF %d AS WANTED ; THE DIFFERENCE A CONSTANT DEFINED TWO WAYS (alpha fitted vs 4 log 4C per pair, beta 7.997097 vs 8) ;'
          ' F2 - THE -15 TOOL %.1f AND %.1f IN n ; THE READING TWO FORMS.**' % (sum(ok), len(ok), rows[0][2] - rows[0][1], rows[1][2] - rows[1][1])]
    out = NL.join(L) + NL
    print(out)
    if 'dry' in a or not allok:
        if not allok:
            print('### A CONTROL NOT AS WANTED -- NOTHING WRITTEN')
        return
    data = out.encode('utf-8')
    with open(OUT + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(OUT + '.tmp', OUT)
    print('  %s  data/b714_law.txt' % hashlib.sha256(data).hexdigest())


if __name__ == '__main__':
    if (sys.argv[1] if len(sys.argv) > 1 else '') != 'bank':
        print('usage: b714_law.py bank [dry]')
        sys.exit(2)
    bank(*sys.argv[2:])
