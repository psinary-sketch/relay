# -*- coding: utf-8 -*-
"""b717_predict.py -- THE PREDICTIONS AT -39, (R327)(4)(ii): "each reachable off-line pair's prediction computed from the registered law alone,
by the form b714 (7) read, written as data/b717_predictions.txt and committed alone before any onset at -39 is computed". The law as
data/b716_registrations.txt (iii) carries it unchanged from dc5e808f (:60-:79): for each off-line pair of Q1 = x^2 + xy + 10y^2 the list
certifies, n*_pred is the fixed point of n = (4 log(4C) + 8 log(n + 1)) / r(rho) (:63, :72), r(rho) = log |1 - 1/rho'| (rho' its reflection,
b705's r_of), C = 2(2 + 2(1 + s)^2) K with s = (1 + 3R)/4 and K the rest set's sum over the certified list with its tail (:64-:65), C read on
Q1's own certified list at -39 before the pair's n* is computed; the first-order form with C per pair (:67-:69); the window [0.99, 1.01] (:74).

### CARRIED FROM tools/b713_predict.py (read through the Read tool :1-:137) by the Write tool, the act's names and the law's bank moved:
### b713 -> b717, the list tool tools/b717_list.py (the engine at sqrt(39), Q1's units of -39), the registration b716's (iii). THE ROUTE FOR C
### UNCHANGED: tools/b709_pairs.py's constants_for709 imported unedited, called with the onset cap 1 so that its onset loop runs no n; the
### configuration b709's -- every on-line zero of the list complete to T0' and the one pair (off<k>, ref<k>), dom = ref<k>; T0' = the floor of
### the list's top. K's tail under T-COUNT with b675's A0 = 10, an ASSUMPTION at Q1 of -39 carried as b675 carries it at Q0, not certified
### for Q1. A pair whose rest moduli or uncertified bound reach r is entered "beyond reach at <T0'>" ((R327)(4)(v)) with the height its rule
### needs, sqrt(2/(r_rule^2 - 1)), and no prediction is scored for it.
### Routes: `bank [dry]` -> data/b717_predictions.txt, data/b717_predictions.json. Writes only those banks; no onset is computed here.
"""
import hashlib
import json
import math
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b717_list as LST            # noqa: E402  ### the engine at sqrt(39), Q1's units, b709's module through it
from flint import arb, ctx         # noqa: E402

P9 = LST.P9
B, P5 = P9.B, P9.P5
ACT = 'b717'
WINDOW = ('0.99', '1.01')          # ### data/b716_registrations.txt :74


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def list_rows():
    """the list as data/b717_list.json banks it: (T0', on rows, the pairs [(k, off row, ref row)])."""
    j = json.load(open(os.path.join(D, '%s_list.json' % ACT), encoding='utf-8'))
    T0p = int(math.floor(j['top']))
    ctx.prec = B.PREC
    on = [('on%d' % (i + 1), arb('0.5'), arb(z['t'], z['h'])) for i, z in enumerate(j['online'])]
    pairs = []
    for k, z in enumerate(j['offline'], 1):
        sg, tt = arb(z['re'], z['h_re']), arb(z['im'], z['h_im'])
        pairs.append((k, ('off%d' % k, sg, tt), ('ref%d' % k, 1 - sg, tt)))
    return T0p, on, pairs, j


def law(C, r):
    """the fixed point of n = (4 log(4C) + 8 log(n + 1)) / r, iterated from 4 log(4C)/r in arb at the bench's precision."""
    ctx.prec = B.PREC
    a = 4 * (4 * C).log()
    n = a / r
    for _ in range(200):
        n2 = (a + 8 * (n + 1).log()) / r
        if abs(n2 - n) < arb('1e-30'):
            n = n2
            break
        n = n2
    return n


def predictions():
    T0p, on, pairs, j = list_rows()
    rows = []
    for k, off, ref in pairs:
        cfg = on + [off, ref]
        c = P9.constants_for709(B.terms(cfg), 'ref%d' % k, T0p, 1)
        ctx.prec = B.PREC
        r = P5.r_of(off[1], off[2])
        rr = P9._arb(c['r'])
        need = math.sqrt(2.0 / (float(rr.mid()) ** 2 - 1.0)) if float(rr.mid()) > 1 else None
        row = dict(k=k, re=off[1].str(20, radius=True), im=off[2].str(20, radius=True), r=r.str(25, radius=True), r_rule=c['r'], R=c['R'],
                   T0=T0p, needs_T0_above=need, reach=c.get('reach'))
        if not c.get('reach'):
            C = P9._arb(c['C'])
            n = law(C, r)
            cap = int(math.ceil(1.25 * float(n.mid())))
            row.update(s=c['s'], K_cert=c['K_cert'], K_tail=c['K_tail'], K=c['K'], C=c['C'], A='1/256', n_pred=n.str(20, radius=True),
                       n_pred_float=float(n.mid()), window=[float(arb(WINDOW[0]) * n.mid()), float(arb(WINDOW[1]) * n.mid())], cap=cap)
        rows.append(row)
    return T0p, rows, j


def bank(*a):
    t0 = time.time()
    T0p, rows, j = predictions()
    live = [r for r in rows if not r['reach']]
    L = ['%s -- (R327)(4)(ii): THE PREDICTIONS AT -39, n*_pred FROM THE REGISTERED LAW, COMMITTED ALONE BEFORE ANY ONSET (%s)' % (ACT, utc()), '',
         '### the law: data/b716_registrations.txt (iii) :60-:79, read unchanged from dc5e808f; the first-order form with C per pair (:67-:69); n*_pred',
         '### the fixed point of n = (4 log(4C) + 8 log(n + 1)) / r(rho), M(n) = (C (n + 1)^2)^4, A = (1/4)^4 = 1/256; C by b709`s constants_for709',
         '### (onset cap 1, no n computed) on Q1`s list at -39 (data/b717_list.txt, the counts certified and the off-line points located, complete',
         '### to %s, T0` = %d): every on-line zero (%d) and the one pair, dom = ref<k>.' % (j['top'], T0p, len(j['online'])),
         '### K`s tail under T-COUNT with b675`s A0 = 10 (Q0`s P3 A0Q), an ASSUMPTION at Q1 of -39 carried as at Q0, not certified for Q1.',
         '### the window [0.99, 1.01] of n*_pred (:74); the falsifier a computed pair outside it (:75); each pair`s onset cap 1.25 x n*_pred.',
         '### a pair the rule cannot reach at T0` (b709`s modulus rule) is entered "beyond reach at T0`" with the height it needs, scored for nothing.', '']

    def m(s, d=12):
        return ('%.' + str(d) + 'g') % float(P9._arb(s).mid())
    for r in rows:
        if r['reach']:
            L.append('  pair %2d | rho %s + %s i | r %s | beyond reach at %d: the rule needs T0` > %.1f' % (
                r['k'], m(r['re'], 10), m(r['im'], 12), m(r['r'], 8), T0p, r['needs_T0_above'] or float('nan')))
        else:
            L.append('  pair %2d | rho %s + %s i | r %s | R %s | s %s | K %s (cert %s, tail %s) | C %s | A 1/256 | n*_pred %.1f | window [%.1f, %.1f] | cap %d' % (
                r['k'], m(r['re'], 10), m(r['im'], 12), m(r['r'], 10), m(r['R'], 12), m(r['s'], 12), m(r['K'], 10), m(r['K_cert'], 10), m(r['K_tail'], 10),
                m(r['C'], 10), r['n_pred_float'], r['window'][0], r['window'][1], r['cap']))
    L += ['', '### ### **PAIRS %d ; PREDICTED %d (pairs %s) ; BEYOND REACH AT T0` %d: %d ; NO ONSET COMPUTED ; %d s.**' % (
        len(rows), len(live), [r['k'] for r in live], T0p, len(rows) - len(live), int(time.time() - t0))]
    print(NL.join(L))
    if 'dry' in a:
        return
    for name, data in (('%s_predictions.txt' % ACT, (NL.join(L) + NL).encode('utf-8')),
                       ('%s_predictions.json' % ACT, (json.dumps(dict(at=utc(), T0=T0p, top=j['top'], window=WINDOW, A0=B.A0, rows=rows), indent=1) + NL).encode('utf-8'))):
        p = os.path.join(D, name)
        LST._membrane(p)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(p + '.tmp', p)
        print('  %s  data/%s' % (hashlib.sha256(data).hexdigest(), name))


ROUTES = dict(bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b717_predict.py bank [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
