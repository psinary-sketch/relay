# -*- coding: utf-8 -*-
"""b492_run.py -- THE RUN. ### **THE CHAIN AT ALL 35 LADDER CELLS, UNDER (R101).**

### The recipe and the floor are b477's, quoted from `b477_gram.py`; the per-n term expression is
### b449's, quoted from `b449_components.py`. ### **THIS ACT CHOOSES NO GRID AND NO THRESHOLD.**
### ### **THE DIAGONAL `W` IS CHECKED AT EVERY CELL BEFORE ANYTHING ELSE IS READ**, and a cell
### outside the floor HALTS the run before a single term is banked.
"""
import io
import json
import math
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
NL = chr(10)
FLOOR = 1.49e-08

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def main():
    import numpy as np
    import b317_smear as SM
    import b318_square as SQ
    import b321_window as WI
    sv = json.loads(read(os.path.join(D, 'b492_survey.json')))
    cells = sv['cells']
    out = io.open(os.path.join(D, 'b492_run.log'), 'w', encoding='utf-8', newline=NL)

    def say(s):
        print(s, flush=True)
        out.write(s + NL)
        out.flush()

    say('=' * 104)
    say('b492 -- THE RUN. ### 35 CELLS, b477`S RECIPE AND GRID, b477`S FLOOR %.2e.' % FLOOR)
    say('=' * 104)
    say('### PHASE 1 -- THE DIAGONAL CHECK AT EVERY CELL. ### A MISMATCH HALTS BEFORE ANY TERM.')
    say('')
    t00 = time.time()
    rows = []
    for i, c in enumerate(cells):
        a = c['a']
        t0 = time.time()
        g = SM.mean_zero_variant(a)
        f = SQ.autocorrelation(g)
        ch = WI.channels(f.v, f.w)
        W = ch['prime'] - ch['arch']
        d = abs(W - c['W_banked'])
        ok = d < FLOOR
        Lv = float(f.v[-1])
        terms = {}
        for p in WI.primes_to(math.exp(Lv) + WI.PRIME_TOL):
            k = 1
            while p ** k <= math.exp(Lv) + WI.PRIME_TOL:
                n = p ** k
                ln = math.log(n)
                if ln <= Lv:
                    terms[n] = 2.0 * math.log(p) / math.sqrt(n) * float(np.interp(ln, f.v, f.w))
                k += 1
        say('  %2d  a=%-11.6f  W=%+.15f  banked=%+.15f  |diff|=%-9.2e  %s   terms=%-3d  %.1fs'
            % (i, a, W, c['W_banked'], d, 'OK' if ok else '### MISMATCH', len(terms),
               time.time() - t0))
        if not ok:
            say('')
            say('### ### **HALT -- THE DIAGONAL CHECK FAILED AT a=%g. NOTHING FURTHER IS READ.**' % a)
            out.close()
            return 2
        rows.append(dict(i=i, a=a, exact=c['exact'], kind=c['kind'], n0=c['n0'],
                         W=W, W_banked=c['W_banked'], dW=d, m=-W,
                         zero=ch['zero'], arch=ch['arch'], prime=ch['prime'],
                         pole=ch['pole'], residual=ch['residual'], L=Lv,
                         terms={str(n): x for n, x in sorted(terms.items())},
                         terms_sum=sum(terms.values()),
                         seconds=round(time.time() - t0, 1)))
    say('')
    say('### ### **THE DIAGONAL CHECK PASSED AT ALL %d CELLS.**' % len(rows))
    say('    worst |W - banked| : ### **%.3e** ### against the floor %.2e'
        % (max(r['dW'] for r in rows), FLOOR))
    say('    cells reproducing EXACTLY (|diff| = 0) : ### **%d of %d**'
        % (sum(1 for r in rows if r['dW'] == 0.0), len(rows)))
    say('    worst |sum(terms) - PR| : ### **%.3e**'
        % max(abs(r['terms_sum'] - r['prime']) for r in rows))
    say('    total : %.1f s' % (time.time() - t00))
    json.dump(dict(floor=FLOOR, rows=rows, seconds=round(time.time() - t00, 1)),
              io.open(os.path.join(D, 'b492_cells.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    say('')
    say('  written: b492_cells.json')
    out.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
