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


def registry():
    """PLACE-papers REGISTRY.md: its lines, its table rows by kind (a paper row: the first cell an id such as `1.5a-9` or d1-1), the rows
    whose text reads a tier (K, KC, C, N, E), and each section head with its paper-row count."""
    import re
    p = 'D:/MY-DOwnloads/PLACE-papers/REGISTRY.md'
    L = io.open(p, encoding='utf-8').read().replace('\r', '').split('\n')
    ID = re.compile(r'^\|\s*\**`?([0-9a-z][0-9a-z.]*-[0-9A-Za-z]+[a-z]?)`?\**\s*\|')
    rows = [(i + 1, ID.match(l).group(1)) for i, l in enumerate(L) if ID.match(l)]
    tier = [i for i, _id in rows if re.search(r'\btier (?:K|KC|C|N|E)\b|\bTier (?:K|KC|C|N|E)\b', L[i - 1])]
    print('### REGISTRY.md : %d lines ; paper rows %d (distinct ids %d) ; rows naming a tier %d' % (len(L), len(rows), len(set(x for _i, x in rows)), len(tier)))
    sec, n = None, 0
    for i, l in enumerate(L, 1):
        if l.startswith('## '):
            if sec:
                print('  %-70s rows %d' % (sec[:70], n))
            sec, n = '%d %s' % (i, l[3:]), 0
        elif ID.match(l):
            n += 1
    if sec:
        print('  %-70s rows %d' % (sec[:70], n))
    hdr = [(i + 1, l) for i, l in enumerate(L) if l.startswith('| ID') or l.startswith('| Id') or l.startswith('| #')]
    for i, l in hdr[:6]:
        print('  header :%d %s' % (i, l[:200]))


if __name__ == '__main__':
    if sys.argv[1:] == ['registry']:
        registry()
    elif sys.argv[1:] == ['surgery']:
        surgery()
    else:
        sys.exit('usage: b718_prices.py surgery | registry')
