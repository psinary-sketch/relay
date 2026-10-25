# -*- coding: utf-8 -*-
"""b711_pairs.py -- PAIRS 11 AND 15 AGAINST THE REFINED DETECTION LAW, (R321)(7), AS data/b710_registrations.txt (i) REGISTERED IT (:10-:49,
committed at b710's step zero before any number, unchanged): "each of pairs 11 and 15, computed by b709's route on the certified list extended to
T0' above its need, has n* within [0.9, 1.1] of its F2 prediction"; the falsifier "either computed n* outside [0.9, 1.1] of its F2 prediction".

### UNTRACKED WRITE: data/b711_pairs_units* -- data/b711_pairs_units.jsonl, one unit per (route, key), appended, resumable (b709's form).

### THE ROUTE: tools/b709_pairs.py IMPORTED UNEDITED through tools/b711_list.py (its units: b709's bands and this act's) -- _pair_unit, which is
### b709's constants_for709 (b675's constants_for :163-:194 line for line, T0 and the cap its two parameters) on the ON rows of the list complete to
### T0' and the pair alone with dom = ref<idx>, the onset resumable per call. One module value is rebound: PAIR_BUDGET 500 -> 400 s (the call's
### onset budget, so that a call stays inside the 590 s guard with the configuration's set-up beside it); its arithmetic unchanged.
### THE PREDICTIONS, read from the banks unchanged: F2 for pairs 11 and 15 from data/b710_fit.txt :38-:39 (12294837.0, 14776939.6; the
### registration's :34, :36 print them rounded) and the window [0.9, 1.1] of each; the caps from the registration :40 (1.25 x F2: 15368546,
### 18471175); F2's alpha and beta from data/b710_fit.txt :21 for (C1)'s ten, each prediction b710's fixed point (tools/b710_fit.py solve,
### imported, iterated from L0 / r with b709's L0, data/b709_pairs.txt :11).
### THE CONTROLS, printed before either pair: (C1) the ten pairs b709 computed (5-10, 12-14, 16) RE-COMPUTED by the route on the list complete to
### the T0' the pair is read at, each n* against its F2 prediction within [0.9, 1.1] (b709's cap, 1.5 x L0/r); (C2) b709's controls by the route
### at T0 = 150, cap 2,000,000: n*(rho_0) over the 180 representatives against 63676, and b705's five pairs against 63651, 358522, 897059,
### 798682, 1020476, EQUAL.
### Routes: `c2` ; `c1 <T0'>` (resumable, one pair per call portion) ; `pair <idx>` (11 or 15, at the list's T0', refused below its need) ;
### `status` ; `bank [dry]` -> data/b711_pairs.txt, data/b711_pairs.json, data/b711_pairs_hashes.txt. Written by the Write tool at b711; it writes
### only its units file and those banks. Nothing here proves RH or GRH or locates any zero.
"""
import hashlib
import io
import json
import math
import os
import re
import sys
import time

from flint import arb

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b711_list as LST            # noqa: E402  ### the list's units (b709's bands and this act's) and b709's module through it
import b710_fit as FIT             # noqa: E402  ### b710's rows (r(rho) from data/b709_pairs.txt) and its fixed point solve, imported unedited

P9 = LST.P9
B, P5 = P9.B, P9.P5
ACT = 'b711'
REG = 'data/b710_registrations.txt'
UNITS = os.path.join(D, '%s_pairs_units.jsonl' % ACT)
P9.PAIR_BUDGET = 400
TEN = (5, 6, 7, 8, 9, 10, 12, 13, 14, 16)
WINDOW = (0.9, 1.1)
CAPS = {11: 15368546, 15: 18471175}      # ### data/b710_registrations.txt :40
L0 = 108.573953341369431556137           # ### data/b709_pairs.txt :11 (as tools/b710_fit.py :62 carries it)
B705_FIVE = P9.B705_FIVE


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def fit_bank():
    """F2's alpha, beta (:21) and the F2 predictions for 11 and 15 (:38-:39), read from data/b710_fit.txt as printed."""
    L = io.open(os.path.join(D, 'b710_fit.txt'), encoding='utf-8').read().split(NL)
    m = re.search(r'alpha (\S+) ; beta (\S+)', L[20])
    assert L[20].lstrip().startswith('(F2)') and m, L[20]
    F2 = {}
    for ln in (38, 39):
        g = re.match(r'^\s+(\d+) \| :\d+ \| .* \| F2 (\S+) \| F1 ', L[ln - 1])
        assert g, L[ln - 1]
        F2[int(g.group(1))] = float(g.group(2))
    return float(m.group(1)), float(m.group(2)), F2


ALPHA, BETA, F2 = fit_bank()


def _membrane(p):
    LST._membrane(p)


def units():
    U = LST.units()
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[(u['route'], u['key'])] = u
    return U


def put_unit(u):
    u['at'] = utc()
    _membrane(UNITS)
    with open(UNITS, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


P9.units, P9.put_unit = units, put_unit


def r_of(idx):
    return [x for x in FIT.rows() if x['idx'] == idx][0]['r']


def predict(idx):
    if idx in F2:
        return F2[idx]
    r = r_of(idx)
    return FIT.solve(ALPHA, BETA, r, L0 / r)


def T0p():
    return int(math.floor(LST.top()))


def c2(*a):
    U = units()
    R0 = B.reps()
    out = []
    t_call = time.time()
    for key, dom, rows, want in [('rho0', 'ref0', R0, P5.B675_NSTAR)] + [('pair%d' % i, 'ref%d' % i, P5.pair_rows(R0, i), B705_FIVE[i]) for i in range(5)]:
        k = ('b711c2', key)
        if k not in U:
            if time.time() - t_call > 360:
                print('### THE CALL`S BUDGET REACHED BEFORE %s -- call again' % key)
                return
            t0 = time.time()
            c = P9.constants_for709(B.terms(rows), dom, B.T0, 2000000)
            put_unit(dict(route='b711c2', key=key, n_star=c['n_star'], want=want, equal=c['n_star'] == want, seconds=int(time.time() - t0)))
            U = units()
        u = U[k]
        out.append(u['equal'])
        print('  C2 %-6s at T0 = 150, cap 2,000,000: n* %s ; banked %d ; EQUAL %s ; %d s' % (key, u['n_star'], u['want'], u['equal'], u['seconds']), flush=True)
    print('### C2 EQUAL %s (%d of %d)' % (all(out), sum(out), len(out)))


def _run(idx, T0, label, cap):
    U = units()
    rows_all, _n_on, _n_off = P9.extended_rows(U, T0)
    R0 = B.reps()
    u, fresh = P9._pair_unit(U, R0, idx, T0, label, rows_all, cap)
    return u


def _ratio(u, idx):
    return (u['n_star'] / predict(idx)) if u.get('n_star') else None


def c1(T0=None, *a):
    T0 = int(T0) if T0 else T0p()
    t_call = time.time()
    for idx in TEN:
        U = units()
        k = ('b711c1', '%d@%d' % (idx, T0))
        if k in U and U[k].get('done'):
            u = U[k]
        else:
            if time.time() - t_call > 60:
                print('### THE CALL`S BUDGET REACHED BEFORE PAIR %d -- call again' % idx)
                return
            r = r_of(idx)
            u = _run(idx, T0, 'b711c1', int(math.ceil(1.5 * L0 / r)))
            if not u.get('done'):
                print('    C1 pair %2d at T0` %d: PARTIAL at n = %s ; %d s -- call again' % (idx, T0, u.get('n_start'), u['seconds']), flush=True)
                return
        q = _ratio(u, idx)
        print('    C1 pair %2d at T0` %d: n* %s ; F2 %.1f ; ratio %s ; %s ; %d s' % (idx, T0, u.get('n_star'), predict(idx), '%.6f' % q if q else '-',
                                                                          ('WITHIN' if WINDOW[0] <= q <= WINDOW[1] else '### OUTSIDE') if q else u.get('reach'), u['seconds']), flush=True)
    print('### C1 AT T0` %d: the ten re-computed' % T0)


def pair(idx, *a):
    idx = int(idx)
    T0 = T0p()
    need = P9.NEEDED[idx]
    if not T0 > need:
        sys.exit('### PAIR %d NOT REACHED: the list is complete to %s, the rule needs T0` > %s -- nothing run' % (idx, LST.top(), need))
    U = units()
    if not all(U.get(('b711c1', '%d@%d' % (i, T0)), {}).get('done') for i in TEN) or not all(U.get(('b711c2', k)) for k in ['rho0'] + ['pair%d' % i for i in range(5)]):
        sys.exit('### THE CONTROLS ARE NOT READ AT T0` %d -- run c2 and c1 first (the controls before the figures)' % T0)
    u = _run(idx, T0, 'b711pair', CAPS[idx])
    q = _ratio(u, idx)
    print('  pair %d at T0` %d: cap %d ; n* %s ; F2 %.1f ; window [%.1f, %.1f] ; ratio %s ; %s ; %s ; %d s' % (
        idx, T0, CAPS[idx], u.get('n_star'), F2[idx], WINDOW[0] * F2[idx], WINDOW[1] * F2[idx], '%.6f' % q if q else '-',
        ('WITHIN' if WINDOW[0] <= q <= WINDOW[1] else '### OUTSIDE') if q else (u.get('reach') or '-'),
        'done' if u.get('done') else 'PARTIAL at n = %s' % u.get('n_start'), u['seconds']), flush=True)


def status(*a):
    U = units()
    for k, u in sorted(U.items()):
        if k[0] in ('b711c1', 'b711c2', 'b711pair'):
            print('  %s %s n* %s done %s %s s' % (k[0], k[1], u.get('n_star'), u.get('done', True), u.get('seconds')))
    print('  the list complete to %s ; T0` %d' % (LST.top(), T0p()))


def _put(name, data):
    p = os.path.join(D, name)
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)
    return hashlib.sha256(data).hexdigest()


def bank(*a):
    U = units()
    top = LST.top()
    T0 = T0p()
    L = ['%s -- COMPONENT 4, (R321)(7): PAIRS 11 AND 15 AGAINST THE REFINED DETECTION LAW, AS %s (i) REGISTERED IT (:10-:49) (%s)' % (ACT, REG, utc()), '',
         '### rows are pairs: idx | the list`s T0` | n* by b709`s route (tools/b709_pairs.py _pair_unit, imported unedited) | the F2 prediction | n*/F2 | the',
         '### window [0.9, 1.1]. F2 alpha %s, beta %s and the predictions read from data/b710_fit.txt :21, :38-:39; the caps from the registration :40.' % (ALPHA, BETA),
         '### THE CONTROLS FIRST, THEN THE FIGURES. The list complete to %s (data/b711_list.txt).' % top, '']
    c2u = [U.get(('b711c2', k)) for k in ['rho0'] + ['pair%d' % i for i in range(5)]]
    c2ok = all(c2u) and all(u['equal'] for u in c2u)
    L.append('### (C2) b709`s controls by the route at T0 = 150, cap 2,000,000: %s -- %s' % (
        ' ; '.join('%s n* %s (want %s)' % (u['key'], u['n_star'], u['want']) for u in c2u if u) or 'NOT RUN', 'EQUAL' if c2ok else '### NOT AS WANTED'))
    T0s = sorted(set(int(k[1].split('@')[1]) for k in U if k[0] == 'b711pair'))
    c1ok = {}
    for t in T0s or [T0]:
        rows = [U.get(('b711c1', '%d@%d' % (i, t))) for i in TEN]
        qs = [(_ratio(u, i) if u and u.get('done') else None) for u, i in zip(rows, TEN)]
        ok = all(q is not None and WINDOW[0] <= q <= WINDOW[1] for q in qs)
        c1ok[t] = ok
        L.append('### (C1) the ten re-computed at T0` %d against F2 (window [0.9, 1.1]): %s -- %s' % (
            t, ' ; '.join('%d %s/%.0f %s' % (i, u.get('n_star') if u else '-', predict(i), ('%.6f' % q) if q else '-') for u, i, q in zip(rows, TEN, qs)),
            'WITHIN 10 OF 10' if ok else '### NOT AS WANTED (%d of 10 within)' % sum(1 for q in qs if q and WINDOW[0] <= q <= WINDOW[1])))
    L += ['', '### THE PAIRS:']
    res = {}
    for idx in (11, 15):
        us = [U[k] for k in U if k[0] == 'b711pair' and k[1].startswith('%d@' % idx)]
        u = max(us, key=lambda x: x['T0']) if us else None
        if u is None:
            res[idx] = ('beyond reach at %s' % top) if not top > P9.NEEDED[idx] else 'NOT RUN'
            L.append('  %2d | the list complete to %s ; the rule needs T0` > %s | %s' % (idx, top, P9.NEEDED[idx], res[idx].upper()))
            continue
        q = _ratio(u, idx)
        st = ('WITHIN' if WINDOW[0] <= q <= WINDOW[1] else 'OUTSIDE') if (q and u.get('done')) else (u.get('reach') or 'PARTIAL at n = %s' % u.get('n_start'))
        res[idx] = st
        L.append('  %2d | T0` %d | n* %s | F2 %.1f | n*/F2 %s | window [%.1f, %.1f] | cap %d | %s' % (
            idx, u['T0'], u.get('n_star') or '-', F2[idx], ('%.6f' % q) if q else '-', WINDOW[0] * F2[idx], WINDOW[1] * F2[idx], CAPS[idx], st))
    comp = [i for i in res if res[i] in ('WITHIN', 'OUTSIDE')]
    out = [i for i in comp if res[i] == 'OUTSIDE']
    verdict = 'REFUTED' if out else ('HELD' if comp else 'NOT SCORABLE')
    L += ['', '### THE FALSIFIER (either computed n* outside [0.9, 1.1] of its F2 prediction): pairs computed %d %s, outside %d %s ; %s' % (
        len(comp), comp or '', len(out), out or '', ' ; '.join('pair %d %s' % (i, res[i]) for i in (11, 15))),
          '### THE REGISTRATION`S HYPOTHESIS: %s over the pairs computed' % verdict, '',
          '### ### **PAIRS 11 AND 15: %s ; THE LAW %s ; THE LIST COMPLETE TO %s ; C1 %s ; C2 %s.**' % (
              ' ; '.join('pair %d %s' % (i, res[i].upper()) for i in (11, 15)), verdict, top, c1ok, c2ok)]
    j = dict(at=utc(), registration=REG, top=top, alpha=ALPHA, beta=BETA, F2=F2, caps=CAPS, c1=c1ok, c2=c2ok, results=res, verdict=verdict,
             units=dict(('%s|%s' % k, v) for k, v in U.items() if k[0] in ('b711c1', 'b711c2', 'b711pair')))
    print(NL.join(L))
    if 'dry' in a:
        return
    h1 = _put('%s_pairs.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    h2 = _put('%s_pairs.json' % ACT, (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    hu = hashlib.sha256(open(UNITS, 'rb').read()).hexdigest() if os.path.exists(UNITS) else '-'
    H = ['%s -- THE PAIRS` BANKS, THEIR sha256 (%s)' % (ACT, utc()), '', '  %s  data/%s_pairs.txt' % (h1, ACT), '  %s  data/%s_pairs.json' % (h2, ACT),
         '  %s  data/%s_pairs_units.jsonl (untracked, its units)' % (hu, ACT), '', '### ### **BANKS 2 HASHED, THE UNITS FILE BESIDE.**']
    _put('%s_pairs_hashes.txt' % ACT, (NL.join(H) + NL).encode('utf-8'))
    print(H[-1])


ROUTES = dict(c1=c1, c2=c2, pair=pair, status=status, bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b711_pairs.py c2 | c1 [T0`] | pair <11|15> | status | bank [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
