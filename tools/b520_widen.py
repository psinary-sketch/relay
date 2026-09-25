# -*- coding: utf-8 -*-
"""b520_widen.py -- VARIANT (B) WIDENED PAST THE LADDER. ### `python tools/b520_widen.py run`

### READING (1): the window is b519's variant (B) exactly -- `b519_window.cell(a, 'B')` IMPORTED, not copied -- on the width grid
### a = 15, 16, ..., 60. ### READING (2), THE REACH: one pass in increasing width; at each width and object the tail bound
### E_tail is compared with the rest of the cell's bound B' = E_u + E_k + E_round, and with the prime channel's table
### (Q0's LAMQ to n = 4096, the channel needing n <= a^2). ### The first width where E_tail > B' (or a^2 > 4096 for Q0) ENDS
### that object's reach: its quantities there and beyond are NOT BANKED -- only the error terms that decided the stop.
"""
import io
import json
import math
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b519_window as B19   # noqa: E402
import b325_epstein as EP   # noqa: E402

NL = chr(10)
GRID = [float(a) for a in range(15, 61)]
OUT = os.path.join(D, 'b520_cells.jsonl')
REACH = os.path.join(D, 'b520_reach.json')
NAMED = (20.0, 30.0, 45.0, 60.0)
LAMQ_TOP = len(EP.LAMQ) - 1
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def errors(x):
    bprime = x['Eu'] + x['Ek'] + x['Eround']
    return dict(Etail=x['Etail'], Bprime=bprime, Eu=x['Eu'], Ek=x['Ek'], Eround=x['Eround'], shortfall=x['shortfall'],
                tail_over_Bprime=x['Etail'] / bprime if bprime > 0 else float('inf'))


def run():
    open_ = dict(q=True, xi=True)
    reach = dict(q=None, xi=None)
    stop = dict(q=None, xi=None)
    scan = []
    t0 = time.time()
    if os.path.exists(OUT):
        os.remove(OUT)
    for a in GRID:
        if not (open_['q'] or open_['xi']):
            break
        c = B19.cell(a, 'B')
        row = dict(a=a, nv=None, nv_note='closed-form transform: no v-grid -- (R114)`s rule has no object, as b511-b519 read it')
        srow = dict(a=a)
        for o in ('q', 'xi'):
            if not open_[o]:
                continue
            e = errors(c[o])
            lamq_ok = (o != 'q') or (a * a <= LAMQ_TOP)
            e['lamq_ok'] = lamq_ok
            srow[o] = e
            if e['Etail'] > e['Bprime'] or not lamq_ok:
                open_[o] = False
                stop[o] = dict(a=a, why=('E_tail > B`' if e['Etail'] > e['Bprime'] else 'a^2 beyond LAMQ'), **e)
                continue
            reach[o] = a
            row[o] = c[o]
        scan.append(srow)
        if 'q' in row or 'xi' in row:
            with io.open(OUT, 'a', encoding='utf-8', newline=NL) as fh:
                fh.write(json.dumps(row) + NL)
        print('[%s] a=%.0f ; open q %s xi %s ; tail/B` q %s xi %s ; elapsed %.0f s'
              % (time.strftime('%H:%M:%S'), a, open_['q'], open_['xi'],
                 ('%.2e' % srow['q']['tail_over_Bprime']) if 'q' in srow else '-',
                 ('%.2e' % srow['xi']['tail_over_Bprime']) if 'xi' in srow else '-', time.time() - t0), flush=True)
    named = {str(int(a)): {o: s.get(o) for o in ('q', 'xi')} for s in scan for a in NAMED if s['a'] == a}
    res = dict(grid=[GRID[0], GRID[-1]], lamq_top=LAMQ_TOP, reach=reach, stop=stop, named=named, scan=scan)
    io.open(REACH, 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print('### REACH : Q0 %s (stop %s) ; xi %s (stop %s)' % (reach['q'], stop['q'], reach['xi'], stop['xi']))
    for a in NAMED:
        n = named.get(str(int(a)))
        if n is None:
            print('  a=%.0f : NOT REACHED BY THE SCAN' % a)
            continue
        for o in ('q', 'xi'):
            if n.get(o):
                print('  a=%.0f %-3s E_tail %.3e against B` %.3e (%s)' % (a, o, n[o]['Etail'], n[o]['Bprime'],
                                                                         'within' if n[o]['Etail'] <= n[o]['Bprime'] else 'BEYOND'))
    return 0


if __name__ == '__main__':
    sys.exit({'run': run}[sys.argv[1]]())
