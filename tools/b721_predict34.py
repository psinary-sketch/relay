# -*- coding: utf-8 -*-
"""b721_predict34.py -- (R331)(4): THE PREDICTIONS AT ONE NEW DISCRIMINANT OF CLASS NUMBER 3 AND ONE OF CLASS NUMBER 4 (CYCLIC), BY THE RULE
OF data/b721_registrations.txt section (4), printed before either is named. Writes no file: its print is entered into the registration by
the Write tool and committed by a commit of its own. No representation count is read: the classes of the primes from their reduced forms
(tools/b720_predict.py setup, unedited), the table of data/b721_derivation.txt (tools/b721_derivation.py, its table and least_instance),
and beside it the group-ring model's least negative index over every Omega (tools/b720_predict.py predict, unedited).

  python -X utf8 -u tools/b721_predict34.py        prints; writes nothing
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

import b718_classgroup as CG     # noqa: E402  ### b718's, unedited
import b720_predict as PR        # noqa: E402  ### b720's, unedited
import b721_derivation as DV     # noqa: E402  ### this act's (4) tool: the table, canon, least_instance
import b721_select as SE         # noqa: E402  ### this act's: fundamental, used_set, rd

BANKED = {3: -23, 4: -39}


def rule_text():
    t = SE.rd('b721_registrations.txt').split(NL)
    head = [i for i, l in enumerate(t) if l.startswith("## (4) THE RULE FOR (R331)(4)'S PREDICTIONS")]
    if len(head) != 1:
        sys.exit('### THE RULE`S SECTION (4) NOT FOUND ONCE IN THE REGISTRATION -- NOTHING NAMED')
    out = []
    for l in t[head[0]:]:
        if out and l.startswith('## '):
            break
        out.append(l)
    return [l for l in out if l.strip()]


def run():
    t0 = time.time()
    L = ['b721 -- (R331)(4): THE RULE APPLIED BY tools/b721_predict34.py (%s); THE RULE FIRST, AS THE REGISTRATION CARRIES IT (at 5febd903):' % (
        time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))] + ['  | ' + l for l in rule_text()] + ['']
    used = SE.used_set()
    out = {}
    for h in (3, 4):
        tab = DV.table(h)
        neg = dict((r['key'], r) for r in tab if r['neg'])
        L.append('## h = %d: the walk, fundamental, cyclic of order %d, two units, in increasing |D|:' % (h, h))
        for D in range(-5, -2000, -1):
            if not SE.fundamental(D) or SE.h_of(D) != h or not SE.cyclic(D):
                continue
            if D in used or D == BANKED[h]:
                L.append('  D = %d: %s -- passed over' % (D, 'the banked case' if D == BANKED[h] else 'USED'))
                continue
            li = DV.least_instance(D, neg, h)
            pr = PR.predict(PR.setup(D))
            row = neg.get(li.get('key'))
            same = li.get('n') == pr['n'] and not li.get('outside')
            fs = ' . '.join('%d^%d' % (p, x) for p, x, _t, _c in li.get('factors', []))
            L += ['  D = %d: TAKEN. the reduced forms %s ; the principal form %s' % (D, CG.reduced_forms(D), CG.principal(D)),
                  '      its primes 2-13: ' + ' ; '.join('%d %s' % (p, CG.prime_class(D, p)[0]) for p in (2, 3, 5, 7, 11, 13)),
                  '      (a) THE TABLE`S PREDICTION: n0 = %s = %s (%s) ; the row %s, Omega %s: a %s, the pair sum %s, b(n0) = %s' % (
                      li.get('n'), fs, ', '.join('%d %s class %d' % (p, t, c) for p, _x, t, c in li.get('factors', [])),
                      DV.key_name(li['key']) if li.get('key') else '-', li.get('Om'), row and row['a'], row and row['P'], row and row['b']),
                  '          below it, of Omega above the table`s and read by the model: %s' % (
                      ', '.join('%d (Omega %d, b %s)' % x for x in li.get('outside_read', [])) or 'none'),
                  '      (b) THE MODEL`S OWN LEAST NEGATIVE INDEX (every Omega to the cut): n0 = %s, b = %s, shape %s -- %s' % (
                      pr['n'], pr.get('b'), pr.get('shape'), 'THE SAME n0' if same else '### NOT FROM THE TABLE ALONE'),
                  '      (c) THE PRIME CLAUSE AS THE TABLE READS IT: every prime of n0 bad (a prime ideal above it non-principal), so none is '
                  'represented by the principal form']
            out[h] = (D, li, pr, row, same)
            break
    L += ['', '### ### **THE PREDICTIONS: %s ; %d s.**' % (' ; '.join(
        'h = %d: D = %d, n0 %s, b %s%s' % (h, D, li.get('n'), row and row['b'], '' if same else ' (NOT FROM THE TABLE ALONE)')
        for h, (D, li, pr, row, same) in sorted(out.items())), int(time.time() - t0))]
    return L, out


if __name__ == '__main__':
    L, _o = run()
    print(NL.join(L))
