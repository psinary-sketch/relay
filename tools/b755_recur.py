# -*- coding: utf-8 -*-
"""b755, (R365)(5)(iii): H-RECURRENCE's GENERATOR AND ITS NULL, committed with the rule and its seed before the certified list at -59 exists.

THE RULE (data/b755_registrations.txt (3), in the ruling's words, data/b755_ferry.txt :24): with p1 = 3 and p2 = 5, the row's two least
primes (data/b753_registrations.txt :32), and the heights of the located off-line zeros, one height for each pair, S is the count of pairs of
heights whose difference, times log p1 / 2 pi and times log p2 / 2 pi, lies within 1/18 of a whole number in both. THE NULL: 4,000 draws of
as many heights uniform on [2, H], numpy's default generator with SEED below. HELD where S is above the largest draw; REFUTED otherwise; NOT
DECIDED where the list holds fewer than 15 heights.
THE SEAT'S READING, fixed here: the heights are those of the certified list's off-line zeros with beta > 1/2 (one of each pair rho,
1 - conj(rho)) at heights in [2, H], read from the band rows of data/b755_list_59.txt in the form of data/b717_list.txt
("  band [lo, hi] | N n | on-line k | off-line m [('beta', 'gamma'), ...] | COMPLETE"); every band must read COMPLETE and the bands must
reach H, else no verdict is printed. "Within 1/18": the distance to the nearest whole number at most 1/18. The count is the same function as
(4)(l)'s (tools/b755_cands.py S_count, written again here unchanged in its arithmetic).
MODES
  control   (4)(l) as this rule's control, one field (-23), a used one: the 69 heights of data/b725_interference.txt with log 2 and log 3,
            S wanted equal to data/b755_cand_l.txt's 168; the null on [2, 445] with SEED; bank data/b755_recur_control.txt
  test      the rule at -59 on data/b755_list_59.txt with H = 200; bank data/b755_recur_59.txt and .json
"""
import json
import math
import os
import re
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = 59
DRAWS = 4000
H = 200.0
P1, P2 = 3, 5
BAND = re.compile(r"^  band \[([0-9.]+), ([0-9.]+)\] \| N (\d+) \| on-line (\d+) \| off-line (\d+)\s*(\[.*\])?\s*\| (\S+)")


def write(path, text):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)
    os.replace(tmp, path)


def S_count(h, l1, l2):
    i, j = np.triu_indices(len(h), 1)
    d = np.abs(h[i] - h[j])
    v1, v2 = d * l1 / (2 * math.pi), d * l2 / (2 * math.pi)
    return int(np.sum((np.abs(v1 - np.round(v1)) <= 1 / 18) & (np.abs(v2 - np.round(v2)) <= 1 / 18))), len(d)


def null(n, lo, hi, l1, l2):
    rng = np.random.default_rng(SEED)
    return np.array([S_count(rng.uniform(lo, hi, n), l1, l2)[0] for _ in range(DRAWS)])


def read_list(path):
    bands, zs = [], []
    for line in open(path, encoding='utf-8'):
        m = BAND.match(line)
        if not m:
            continue
        lo, hi, N, on, off, pairs, status = m.groups()
        got = re.findall(r"\('([0-9.]+)', '([0-9.]+)'\)", pairs or '')
        if len(got) != int(off):
            raise SystemExit('### band [%s, %s]: %s off-line read, %d listed -- REFUSED' % (lo, hi, off, len(got)))
        bands.append((float(lo), float(hi), int(N), int(on), int(off), status))
        zs += [(float(b), float(g)) for b, g in got]
    return bands, zs


def main(argv):
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    t0 = time.time()
    if argv == ['control']:
        hs = []
        for line in open(os.path.join(ROOT, 'data', 'b725_interference.txt'), encoding='utf-8'):
            m = re.match(r'^\s+off(\d+)\s+([0-9.]+)\s+([0-9.]+)\s', line)
            if m:
                hs.append(float(m.group(3)))
        h = np.array(sorted(hs))
        S, npairs = S_count(h, math.log(2), math.log(3))
        dr = null(len(h), 2.0, 445.0, math.log(2), math.log(3))
        ok = len(h) == 69 and S == 168
        text = ('b755 -- (R365)(5)(iii): H-RECURRENCE\'S CONTROL, (4)(l) AT ONE FIELD (-23), A USED ONE (%s)\n\n'
                '### by tools/b755_recur.py control, committed with the rule and its seed before the certified list at -59 exists.\n\n'
                '  the 69 heights of data/b725_interference.txt with log 2 and log 3: S = %d of %d pairs ; data/b755_cand_l.txt\'s S 168: %s\n'
                '  the null, %d draws of %d heights uniform on [2, 445], seed %d: mean %.2f, largest %d ; S %s the largest draw\n\n'
                '### ### **H-RECURRENCE\'S CONTROL: S = %d, %s ; THE NULL\'S LARGEST %d ; %.1f s.**\n') % (
            stamp, S, npairs, 'EQUAL, AS WANTED' if ok else 'NOT EQUAL, NOT AS WANTED', DRAWS, len(h), SEED, dr.mean(), dr.max(),
            'ABOVE' if S > dr.max() else 'NOT ABOVE', S, 'AS WANTED' if ok else 'NOT AS WANTED', dr.max(), time.time() - t0)
        print(text)
        write(os.path.join(ROOT, 'data', 'b755_recur_control.txt'), text)
        return 0 if ok else 1
    if argv == ['test']:
        path = os.path.join(ROOT, 'data', 'b755_list_59.txt')
        bands, zs = read_list(path)
        complete = bool(bands) and all(b[5] == 'COMPLETE' for b in bands) and max(b[1] for b in bands) >= H - 1e-9
        hs = np.array(sorted(g for b, g in zs if 2.0 <= g <= H))
        L = ['  the certified list data/b755_list_59.txt: bands %d, every band COMPLETE and reaching %.0f: %s ; off-line zeros with beta > 1/2 %d,'
             ' at heights in [2, %.0f] %d' % (len(bands), H, complete, len(zs), H, len(hs))]
        out = {'stamp': stamp, 'bands': len(bands), 'complete': complete, 'offline': len(zs), 'heights': hs.tolist(), 'seed': SEED,
               'p1': P1, 'p2': P2, 'H': H}
        if not complete:
            verdict = 'NO VERDICT: THE LIST IS NOT COMPLETE TO H'
        elif len(hs) < 15:
            verdict = 'NOT DECIDED: %d HEIGHTS, FEWER THAN 15' % len(hs)
        else:
            S, npairs = S_count(hs, math.log(P1), math.log(P2))
            dr = null(len(hs), 2.0, H, math.log(P1), math.log(P2))
            held = S > dr.max()
            out.update({'S': S, 'pairs': npairs, 'null_mean': float(dr.mean()), 'null_max': int(dr.max()), 'held': bool(held)})
            L.append('  S = %d of %d pairs with log %d and log %d ; the null, %d draws of %d heights uniform on [2, %.0f], seed %d: mean %.2f,'
                     ' largest %d' % (S, npairs, P1, P2, DRAWS, len(hs), H, SEED, dr.mean(), dr.max()))
            verdict = '%s: S = %d AGAINST THE LARGEST DRAW %d' % ('HELD' if held else 'REFUTED', S, dr.max())
        out['verdict'] = verdict
        text = ('b755 -- (R365)(5)(iii): H-RECURRENCE AT -59, ON THE CERTIFIED LIST (%s)\n\n'
                '### by tools/b755_recur.py test, committed with the rule and its seed before the certified list existed; read against the\n'
                '### rule of data/b755_registrations.txt (3) and nothing written after it; no sentence says why.\n\n'
                % stamp) + '\n'.join(L) + '\n\n### ### **H-RECURRENCE AT -59: %s ; %.1f s.**\n' % (verdict, time.time() - t0)
        print(text)
        write(os.path.join(ROOT, 'data', 'b755_recur_59.txt'), text)
        write(os.path.join(ROOT, 'data', 'b755_recur_59.json'), json.dumps(out, indent=1) + '\n')
        return 0
    sys.exit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
