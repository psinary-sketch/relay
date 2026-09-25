# -*- coding: utf-8 -*-
"""b522_reach.py -- VARIANT (B) AT p = 7, THE REACH READ PER WIDTH. ### `python tools/b522_reach.py run`

### (R131)(2): a width is WITHIN REACH iff E_tail <= B' = E_u + E_k + E_round AT THAT WIDTH (and a^2 within Q0`s LAMQ);
### widths outside are banked as their error terms and NOT READ. ### (R131)(3): variant (B) at p = 7 on a = 15..60, every
### width computed, no stop. ### The cell is b521`s `cell_q(a, 7)`, IMPORTED, not copied -- the closed-form tail, the
### completed bank, the exact transform.
"""
import io
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T_ = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T_)
import b521_tail as B21   # noqa: E402

NL = chr(10)
P = 7
GRID = [float(a) for a in range(15, 61)]
ERR = ('a', 'p', 'Etail', 'tail_on', 'tail_off', 'Bprime', 'Eu', 'Ek', 'Eround', 'shortfall')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def run():
    out = os.path.join(D, 'b522_cells.jsonl')
    if os.path.exists(out):
        os.remove(out)
    table = []
    t0 = time.time()
    for a in GRID:
        c = B21.cell_q(a, P)
        lamq_ok = a * a <= B21.LAMQ_TOP
        inside = c['Etail'] <= c['Bprime'] and lamq_ok
        row = {k: c[k] for k in ERR}
        row.update(lamq_ok=lamq_ok, tail_over_Bprime=c['Etail'] / c['Bprime'], within=inside)
        table.append(row)
        if inside:
            c['tail_share'] = c['Etail'] / c['B']
            with io.open(out, 'a', encoding='utf-8', newline=NL) as fh:
                fh.write(json.dumps(c) + NL)
        print('[%s] a=%-4.0f E_tail %.3e ; B` %.3e ; %s ; elapsed %.0f s'
              % (time.strftime('%H:%M:%S'), a, c['Etail'], c['Bprime'], 'IN' if inside else 'OUT', time.time() - t0), flush=True)
    res = dict(p=P, grid=[GRID[0], GRID[-1]], lamq_top=B21.LAMQ_TOP, within=[r['a'] for r in table if r['within']],
               outside=[r['a'] for r in table if not r['within']], table=table)
    io.open(os.path.join(D, 'b522_reach.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print('### WITHIN REACH : %d of %d ; outside : %s' % (len(res['within']), len(GRID), res['outside']))
    return 0


if __name__ == '__main__':
    sys.exit({'run': run}[sys.argv[1]]())
