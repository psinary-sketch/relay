# -*- coding: utf-8 -*-
"""b755, (R365)(6): AFTER BOTH VERDICTS, EXPLORATORY AND MARKED SO -- THE CENSUS FROM THE PRIMES AT -23, written by the seat from the
ruling's words alone (data/b755_ferry.txt :26) and committed before its run. No value of any Epstein zeta function is computed here: only
sums over primes, by tools/b755_zlist.py's functions as committed (prime_set, newton, match; its scan's arithmetic written again below with
the height's lower end a parameter, unchanged otherwise).

THE ORDER, quoted: "at -23 the route's roots with real part at least 0.85 to height 5,000, counted; and the least height at which the route
finds a root with real part above 1, at three prime bounds."
THE ROUTE: (5)(ii)'s, as tools/b755_zlist.py runs it -- the modulus of 1 + 2 exp(-3 T_P(s)) on sigma = 0.80..1.30 by 0.01 and t by 0.01 at
  P = 10^4, no tail; each local minimum under 0.3 (eight neighbours, the edges included) refined by Newton's method with the tail, the step
  capped at 0.05; a root kept where |f| < 1e-9; roots within 1e-6 of each other one root.
THE SEAT'S READINGS, fixed here before the run:
  "to height 5,000": the scan on [2, 5000] in five segments of height 1,000 (the route at -23 to height 200 took 60.1 s for its scan,
    data/b755_cand_h_scan_23.txt :6, so a segment prices near 300 s, one foreground call each under 600 s); a segment's edge column is in
    both segments it bounds, and a root found from both is one root (within 1e-6) at the bank.
  "counted": at the route's own Newton bound P = 3 x 10^5 ((5)(ii)), the roots with real part at least 0.85 and height in [2, 5000].
  "at three prime bounds": the Newton bound P in {10^5, 3 x 10^5, 10^6}, the route's own and one either side, each from the same scan's
    minima at P = 10^4; at each, the least height of a root with real part above 1, or none to 5000.
  THE CONTROL BESIDE IT, a used field and no test: the roots at P = 3 x 10^5 on [2, 445] against the 69 banked off-line zeros of
    data/b725_interference.txt (complete to 445) by match() in (5)(ii)'s words, printed ONE TO ONE or NOT ONE TO ONE; to height 200 the
    same route read ONE TO ONE (data/b755_cand_h_scan_23.txt :7).
  Nothing here is a registered prediction; nothing is read as HELD or REFUTED; no sentence says why.

### UNTRACKED WRITE: data/b755_census_units* -- data/b755_census_units_<lo>_<hi>.json, one file per segment (its minima and its roots at
### each bound), written as each segment lands; declared by prefix for the root route's exclusion list. The bank carries every root.

MODES
  segment <lo> <hi>   one segment of SEGMENTS: the scan, the minima, Newton at the three bounds; data/b755_census_units_<lo>_<hi>.json
  bank                every segment present: the count, the three least heights, the control; data/b755_census_from_primes.txt and .json
"""
import json
import math
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_, T_ = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T_)
import b755_zlist as Z   # noqa: E402  ### the route's functions as committed

ACT = 'b755'
FIELD = -23
H_TOP = 5000.0
SEGMENTS = [(2, 1000), (1000, 2000), (2000, 3000), (3000, 4000), (4000, 5000)]
BOUNDS = [10 ** 5, 3 * 10 ** 5, 10 ** 6]
P_COUNT = 3 * 10 ** 5
CTRL_TOP = 445.0


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _membrane(p):
    """standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path); the exclusion pattern
    the record tool's where it imports, none before it is carried (tools/b755_carry.py's form)."""
    import act_membrane as MEM
    try:
        import b755_record as REC
        ex = REC.R.ROOT_EXCLUDE
    except Exception:
        ex = None
    MEM.guard_path(ACT, p, ex)


def write(path, text):
    _membrane(path)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)
    os.replace(tmp, path)


def unit_path(lo, hi):
    return os.path.join(D_, '%s_census_units_%d_%d.json' % (ACT, lo, hi))


def seg_minima(lo, hi):
    """tools/b755_zlist.py scan()'s grid and minima, its arithmetic unchanged, on t = lo..hi by 0.01."""
    _, logp_s, _ = Z.prime_set(FIELD, Z.P_SCAN)
    nt = int(round((hi - lo) / 0.01)) + 1
    ts = lo + 0.01 * np.arange(nt)
    M = np.empty((len(Z.SIG), nt))
    for j, sg in enumerate(Z.SIG):
        a = np.exp(-sg * logp_s)
        for k0 in range(0, nt, 2000):
            tt = ts[k0:k0 + 2000]
            x = a[None, :] * np.exp(-1j * np.outer(tt, logp_s))
            T = np.sum(-np.log1p(-x) + np.log1p(-x ** 3) / 3, axis=1)
            M[j, k0:k0 + 2000] = np.abs(1 + 2 * np.exp(-3 * T))
    pad = np.pad(M, 1, constant_values=np.inf)
    core = pad[1:-1, 1:-1]
    ismin = np.ones_like(M, dtype=bool)
    for dj in (-1, 0, 1):
        for dk in (-1, 0, 1):
            if dj or dk:
                ismin &= core <= pad[1 + dj:1 + dj + M.shape[0], 1 + dk:1 + dk + M.shape[1]]
    ismin &= M < 0.3
    return [complex(Z.SIG[j], ts[k]) for j, k in zip(*np.nonzero(ismin))], len(logp_s), [len(Z.SIG), nt]


def refine(seeds, P):
    _, logp, w = Z.prime_set(FIELD, P)
    roots = []
    for s0 in seeds:
        r, res = Z.newton(FIELD, s0, logp, w, P, True)
        if res < 1e-9 and not any(abs(r - q) < 1e-6 for q in roots):
            roots.append(r)
    roots.sort(key=lambda z: z.imag)
    return roots, int(len(logp))


def dedup(rs):
    out = []
    for r in sorted(rs, key=lambda z: z.imag):
        if not any(abs(r - q) < 1e-6 for q in out):
            out.append(r)
    return out


def main(argv):
    if len(argv) == 3 and argv[0] == 'segment':
        lo, hi = int(argv[1]), int(argv[2])
        if (lo, hi) not in SEGMENTS:
            raise SystemExit('### the segment [%d, %d] is not one of %s -- REFUSED' % (lo, hi, SEGMENTS))
        t0 = time.time()
        seeds, nps, grid = seg_minima(lo, hi)
        t_scan = time.time() - t0
        out = {'at': utc(), 'field': FIELD, 'lo': lo, 'hi': hi, 'P_scan': Z.P_SCAN, 'primes_scan': nps, 'grid': grid, 'minima': len(seeds),
               'seeds': [[s.real, s.imag] for s in seeds], 'seconds_scan': round(t_scan, 1), 'bounds': {}}
        for P in BOUNDS:
            t1 = time.time()
            roots, npn = refine(seeds, P)
            out['bounds'][str(P)] = {'primes': npn, 'roots': [[r.real, r.imag] for r in roots], 'seconds': round(time.time() - t1, 1)}
            print('  [%d, %d] P = %d (%d primes): roots %d, with Re >= 0.85 %d, with Re > 1 %d ; %.1f s' % (
                lo, hi, P, npn, len(roots), sum(1 for r in roots if r.real >= 0.85), sum(1 for r in roots if r.real > 1),
                time.time() - t1), flush=True)
        write(unit_path(lo, hi), json.dumps(out, indent=1) + '\n')
        print('### SEGMENT [%d, %d]: grid %d x %d at P = %d (%d primes), minima %d ; scan %.1f s ; %.1f s in all' % (
            lo, hi, grid[0], grid[1], Z.P_SCAN, nps, len(seeds), t_scan, time.time() - t0))
        return 0
    if argv == ['bank']:
        miss = [s for s in SEGMENTS if not os.path.exists(unit_path(*s))]
        if miss:
            raise SystemExit('### segments not run: %s -- REFUSED' % miss)
        U = [json.load(open(unit_path(*s), encoding='utf-8')) for s in SEGMENTS]
        stamp = utc()
        rows, J = [], {'at': stamp, 'field': FIELD, 'H': H_TOP, 'segments': [], 'bounds': {}}
        for u in U:
            J['segments'].append({k: u[k] for k in ('lo', 'hi', 'grid', 'minima', 'seconds_scan', 'at')})
            rows.append('  segment [%d, %d]: grid %d x %d, minima %d ; scan %.1f s ; Newton %s' % (
                u['lo'], u['hi'], u['grid'][0], u['grid'][1], u['minima'], u['seconds_scan'],
                ', '.join('%s %.1f s' % (P, u['bounds'][str(P)]['seconds']) for P in BOUNDS)))
        least = {}
        for P in BOUNDS:
            rs = dedup([complex(*r) for u in U for r in u['bounds'][str(P)]['roots']])
            rs = [r for r in rs if 2 <= r.imag <= H_TOP]
            n85 = sum(1 for r in rs if r.real >= 0.85)
            over1 = [r for r in rs if r.real > 1]
            least[P] = over1[0] if over1 else None
            J['bounds'][str(P)] = {'roots': [[r.real, r.imag] for r in rs], 'roots_85': n85, 'over_1': len(over1),
                                   'least_over_1': [over1[0].real, over1[0].imag] if over1 else None,
                                   'max_re': max((r.real for r in rs), default=None)}
        c = J['bounds'][str(P_COUNT)]
        zs, top = Z.banked_list(FIELD)
        m = Z.match(zs, [complex(*r) for r in c['roots']], CTRL_TOP)
        J['control'] = m
        L = ['b755 -- (R365)(6): AFTER BOTH VERDICTS, EXPLORATORY AND MARKED SO -- THE CENSUS FROM THE PRIMES AT -23 TO HEIGHT 5,000 (%s)' % stamp, '',
             '### by tools/b755_census.py, committed before its run, over tools/b755_zlist.py\'s route as committed; EXPLORATORY: no registered',
             '### prediction, nothing read as HELD or REFUTED, no sentence says why. No value of an Epstein zeta function computed: sums over primes.',
             '### The order (data/b755_ferry.txt :26): "at -23 the route\'s roots with real part at least 0.85 to height 5,000, counted; and the',
             '### least height at which the route finds a root with real part above 1, at three prime bounds." The seat\'s readings are the',
             '### tool\'s head: the scan at P = 10^4 on [2, 5000] in five segments; the count at the route\'s Newton bound 3 x 10^5; the three',
             '### bounds 10^5, 3 x 10^5 and 10^6, each refining the same minima.', ''] + rows + ['']
        for P in BOUNDS:
            b = J['bounds'][str(P)]
            L.append('  P = %d: roots in [2, 5000] %d ; with Re >= 0.85 %d ; with Re > 1 %d ; the least height of a root with Re > 1: %s ; the largest real part %s' % (
                P, len(b['roots']), b['roots_85'], b['over_1'],
                ('%.6f (the root %.6f + %.6f i)' % (least[P].imag, least[P].real, least[P].imag)) if least[P] else 'none to 5000',
                ('%.6f' % b['max_re']) if b['max_re'] is not None else '-'))
        L += ['', '  THE CONTROL BESIDE IT (a used field, no test): the roots at P = %d on [2, %.0f] against the %d banked off-line zeros of' % (
            P_COUNT, CTRL_TOP, len(zs)),
              '  data/b725_interference.txt (complete to %.0f) by match() in (5)(ii)\'s words: zeros with Re >= 0.85 %d ; roots with Re >= 0.85 %d ;' % (
                  top, m['zeros_85'], m['roots_85']),
              '  pairs within 0.01 %d, the worst %s ; a zero without its partner %s ; a root without its partner %s: %s' % (
                  m['pairs'], ('%.5f' % m['worst']) if m['worst'] is not None else '-', m['zero_without_partner'] or 'none',
                  m['root_without_partner'] or 'none', 'ONE TO ONE' if m['held'] else 'NOT ONE TO ONE'), '']
        L += ['### THE ROOTS AT P = %d WITH Re >= 0.85, BY HEIGHT:' % P_COUNT]
        L += ['    root %.6f + %.6f i' % (r[0], r[1]) for r in c['roots'] if r[0] >= 0.85]
        L += ['', '### ### **(6), EXPLORATORY: AT -23 TO HEIGHT 5,000 THE ROUTE\'S ROOTS WITH Re >= 0.85 AT P = 3 x 10^5: %d ; THE LEAST HEIGHT OF A ROOT WITH Re > 1: %s ; THE CONTROL TO 445 %s.**' % (
            c['roots_85'], ' ; '.join('P = %d %s' % (P, ('%.2f' % least[P].imag) if least[P] else 'NONE TO 5000') for P in BOUNDS),
            'ONE TO ONE' if m['held'] else 'NOT ONE TO ONE')]
        text = '\n'.join(L) + '\n'
        print(text)
        write(os.path.join(D_, '%s_census_from_primes.txt' % ACT), text)
        write(os.path.join(D_, '%s_census_from_primes.json' % ACT), json.dumps(J, indent=1) + '\n')
        return 0
    sys.exit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
