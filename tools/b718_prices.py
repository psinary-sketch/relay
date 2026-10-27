# -*- coding: utf-8 -*-
"""b718_prices.py -- the figures the act's prices stand on, read from the banks and printed; writes nothing (the price banks are written by
the Write tool from these prints). Route `surgery`: b709's grid units (data/b709_grid_units*.jsonl) -- the points, their kinds, their seconds
summed -- and b711's surgery bank (data/b711_surgery.json) -- its seconds where it carries them -- for (R328)(5)(iv)'s price.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_ = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def surgery():
    files = sorted(f for f in os.listdir(D_) if f.startswith('b709_grid_units') and f.endswith('.jsonl'))
    tot_units, tot_s, kinds, keys = 0, 0.0, {}, set()
    for f in files:
        n, s = 0, 0.0
        for line in io.open(os.path.join(D_, f), encoding='utf-8'):
            line = line.strip()
            if not line:
                continue
            try:
                u = json.loads(line)
            except ValueError:
                continue
            n += 1
            s += float(u.get('seconds', 0) or 0)
            k = u.get('kind') or u.get('route') or '?'
            kinds[k] = kinds.get(k, 0) + 1
            keys.add(str(u.get('key', u.get('point', ''))))
        tot_units += n
        tot_s += s
        print('  %-44s units %6d ; seconds %10.1f' % (f, n, s))
    print('### b709 GRID UNITS: files %d ; units %d ; distinct keys %d ; seconds summed %.1f (%.2f h) ; kinds %s' % (
        len(files), tot_units, len(keys), tot_s, tot_s / 3600, dict(sorted(kinds.items()))))
    j = json.load(io.open(os.path.join(D_, 'b711_surgery.json'), encoding='utf-8'))
    print('### b711 SURGERY BANK: keys %s ; seconds %s' % (sorted(j)[:20], j.get('seconds')))


if __name__ == '__main__':
    if sys.argv[1:] != ['surgery']:
        sys.exit('usage: b718_prices.py surgery')
    surgery()
