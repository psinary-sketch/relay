# -*- coding: utf-8 -*-
"""b731 -- THE PRICE BANK'S MEASURED ROWS, (R341)(2)(ii) AND (4): the three fields landed, each beside the estimate it answers, in I-10's form; the re-price of count and explicitFormula, printed for the
acts that take them. The rooted bank data/b729_count_price.txt is not edited. Lines are read from the tree of SIDE-explicit-formula at the commits named, runs by id, the controls printed first (N2).

  python -X utf8 -u tools/b731_price.py [--bank]
Written by the Write tool. Reads git, writes data/b731_price_measured.txt alone, and only with --bank.
"""
import io, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from standing import pricebank as P

EF = 'D:/SIDE-explicit-formula'
B730_TIP = '5688816e'
TIP = '23b006df'
Z = 'SIDEExplicitFormula/Schema/ZQ/%s.lean'
BANK = 'data/b731_price_measured.txt'
SRC = 'data/b729_count_price.txt'
ROWS = 'data/b731_dispatch_rows.json'

FIELDS = (('continuation', ('Lattice', 'Theta', 'FEPair', 'Continuation'), B730_TIP, (1500, 3000), (25, 50), SRC + ' :21', 'Mathlib`s even kernel route, b730',
           (41292290796, 41293161382, 41293638071, 41294254957, 41294932964, 41295546328)),
          ('logDeriv', ('Bound', 'LogDeriv'), TIP, (200, 400), (3, 8), SRC + ' :23', 'the LSeries route with the bound Z_Q(3/2) < 4, b731',
           (41316031450, 41316963968, 41317771708)),
          ('zeros', ('Zeros',), TIP, (300, 600), (5, 10), SRC + ' :22', 'zetaZeroConfig`s form over the completed function, b731',
           (41318856071,)))

TAKEN = (('count', (800, 2000), (15, 35), '20-45', SRC + ' :25'),
         ('explicitFormula', (3000, 5000), (40, 80), '60-120', SRC + ' :24'))


def lines(ref, names):
    n = 0
    for m in names:
        b = subprocess.run(['git', '-C', EF, 'show', '%s:%s' % (ref, Z % m)], capture_output=True, check=True).stdout
        n += b.count(b'\n')
    return n


def refuses(f):
    try:
        f()
    except ValueError:
        return True
    return False


def controls():
    R = P.measured('c', 'i', 835, list(range(6)))
    L = P.measured('l', 'i', 786, [1, 2, 3])
    cases = (('a measured row with no run',   refuses(lambda: P.measured('x', 'i', 10, [])), True),
             ('a measured row with no lines', refuses(lambda: P.measured('x', 'i', 0, [1])), True),
             ('b730`s ratio as v1.11.0 printed it', tuple(round(x, 3) for x in P.ratio(R, (1500, 3000), (25, 50))), (0.278, 0.557, 0.12, 0.24)),
             ('logDeriv by b730`s ratio, exact (plan 56-223)', P.reprice((200, 400), (3, 8), P.ratio(R, (1500, 3000), (25, 50))), (55, 223, 1, 2)),
             ('zeros by b730`s ratio, exact (plan 83-335)', P.reprice((300, 600), (5, 10), P.ratio(R, (1500, 3000), (25, 50))), (83, 334, 1, 3)),
             ('the zeros plan`s re-price by (3)`s ratio', P.reprice((300, 600), (5, 10), P.ratio(L, (200, 400), (3, 8))), (589, 2358, 1, 10)))
    out, ok = [], True
    for name, got, want in cases:
        good = got == want
        ok = ok and good
        out.append('  %-46s %-34s %s' % (name, got, 'AS WANTED' if good else 'NOT AS WANTED, WANTED %s' % (want,)))
    out.append('  CONTROLS %d OF %d AS WANTED' % (sum('NOT AS WANTED' not in x for x in out), len(cases)))
    return out, ok


def main():
    bank = '--bank' in sys.argv
    O = ['b731 -- THE PRICE BANK`S MEASURED ROWS AND THE RE-PRICE OF THE TWO FIELDS NOT TAKEN, (R341)(2)(ii), (4); NOTHING BUILT BY THIS BANK, NO LEAN PROCESS, NO DISPATCH', '',
         '### FORM: ' + P.FORM + '.', '### The rooted bank %s is not edited; the next field`s act reads these rows from here.' % SRC, '',
         '## THE CONTROLS FIRST']
    c, ok = controls()
    O += c
    if not ok:
        print('\n'.join(O))
        sys.exit('b731_price: a control missed')
    raw = io.open(os.path.join(ROOT, ROWS), encoding='utf-8').read()
    rows = []
    for name, mods, ref, el, ed, src, impl, runs in FIELDS:
        missing = [r for r in runs if name != 'continuation' and str(r) not in raw]
        if missing:
            sys.exit('b731_price: %s: run(s) %s not in %s' % (name, missing, ROWS))
        rows.append(dict(field=name, est_lines=el, est_disp=ed, source=src, row=P.measured(name, impl, lines(ref, mods), runs), mods=mods, ref=ref))
    O += ['', '## THE THREE MEASURED ROWS, EACH BESIDE ITS ESTIMATE'] + P.rows_text(rows) + ['', '## WHAT EACH ROW MEASURED']
    for x in rows:
        O.append('  %-14s %s ; modules %s at %s ; runs %s' % (x['field'], x['row']['implementation'], ', '.join(x['mods']), x['ref'], ', '.join(str(r) for r in x['row']['runs'])))
    O += ['', '## THE TWO FIELDS NOT TAKEN, RE-READ BY EACH MEASURED RATIO (NOT TOUCHED THIS ACT; PRINTED FOR THE ACTS THAT TAKE THEM; THE SEAT`S, NOT A BOUND)']
    for name, el, ed, hours, src in TAKEN:
        O.append('  %s: the bank`s %d-%d lines, %d-%d dispatches (%s)' % (name, el[0], el[1], ed[0], ed[1], src))
        lo, hi, dlo, dhi = [], [], [], []
        for x in rows:
            r = P.reprice(el, ed, P.ratio(x['row'], x['est_lines'], x['est_disp']))
            lo.append(r[0]); hi.append(r[1]); dlo.append(r[2]); dhi.append(r[3])
            O.append('    by %-14s %d-%d lines, %d-%d dispatches' % (x['field'] + '`s ratio', r[0], r[1], r[2], r[3]))
        O.append('    THE ENVELOPE OF THE THREE %d-%d lines, %d-%d dispatches. The bank`s %s foreground hours are not re-read: no hours were measured.' % (min(lo), max(hi), min(dlo), max(dhi), hours))
    O += ['', '## TWO FIGURES IN THE PLANS CORRECTED HERE, THE PLANS NOT EDITED',
          '  data/b731_logderiv_plan.txt :37 prints 56-223 lines and data/b731_zeros_plan.txt :37 prints 83-335. The exact readings are 55-223 and 83-334 (600 x 835/1500 = 334).',
          '  Both were worked by hand from the rounded ratios 0.278 and 0.557, not by pricebank.reprice; the first run of this tool`s controls found the second. Neither moved a decision: each plan priced its field from its lemmas.']
    O += ['', '## HOW FAR THE RATIOS GO',
          '  The three ratios do not agree, and the envelope is their spread, not a confidence interval: three fields, three kinds of proof, each estimate the seat`s.',
          '  Lines ran under the bank on continuation, over it on logDeriv, inside it on zeros. Dispatches ran under the bank on continuation and zeros and at its floor on logDeriv.',
          '  The zeros row is the cheapest in dispatches because the module had a compiled form to follow and was read through before its one dispatch; it is no promise for a field without one.',
          '  count: b729`s bank marks C3 and C4 ABSENT in Lean (:32, :33), and says ZQPremises.count names A0Q = 10 while the least route gives an unnamed A0 (:37). The dearer route is the author`s word on A0; no ratio here prices that choice.',
          '  explicitFormula: its neighbour is 12 modules, 3,742 lines (:24), and no field measured here is a contour chain. The ratios read the bank`s row and do not re-derive it.', '',
          '### ### **THE PRICE BANK: THREE ROWS MEASURED ; count AND explicitFormula RE-READ AND NOT TOUCHED ; THE RATIOS DISAGREE AND THE SPREAD IS PRINTED, NO ONE RATIO CHOSEN.**', '']
    t = '\n'.join(O)
    print(t)
    if bank:
        io.open(os.path.join(ROOT, BANK), 'w', encoding='utf-8', newline='\n').write(t)
        print('written ' + BANK)


if __name__ == '__main__':
    main()
