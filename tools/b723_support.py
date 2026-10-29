# -*- coding: utf-8 -*-
"""b723_support.py -- H-SUPPORT'S ONSETS, (R333)(5)(ii), AS data/b723_registrations.txt (i) REGISTERED IT (:17-:34, committed alone at relay
9ad26421) ON THE ZEROS ITS RULE NAMED (data/b723_support_rule.txt, committed alone at relay 0e91c670 before any onset): "H-SUPPORT's onsets by
b707's route on b709's ladder, each zero's price read from b709's banked timings before it runs, stoppable between zeros".

### UNTRACKED WRITE: data/b723_support_units.jsonl (one unit per (route, fam, kind, point, obj), appended as each lands, resumable).
### THE ROUTE, PER ZERO (its family F_a(gamma0) = span{C, N} at the zero's ordinate gamma0, b707's template):
###   (1) b707's ladder (tools/b707_onset.py window and terms707, imported unedited): a = log 2, 2 log w at w = 32, 48, 64, 96, 128, 192; at
###       each rung the zeta form first (C1 of b707: POSITIVE DEFINITE, else no Q0 figure at that rung), then Q0's; the coarse bracket
###       (a+, a-] is the last rung read positive below the least rung read NEGATIVE DIRECTION;
###   (2) b709's fine grid in that bracket (tools/b709_grid.py grid, window, terms709, imported unedited; the family entered in its FREQS,
###       INTERVAL and ENDPOINT_RUNG under the zero's name, as b711 rebinds b709's module functions): the rungs log p^k and the midpoints, in
###       increasing a, the zeta form first at each point (b709's control before each Q0 figure) and Q0's after; THE ONSET a* is the least grid
###       point read NEGATIVE DIRECTION BEYOND ITS BOUND (a- itself where no interior point is). The run stops at the onset: every point below
###       it is read, none above it is needed for the least.
### THE CONTROL BEFORE ANY NAMED ZERO, (C1) of the registration: the same code path, with the banked families entered by name (rho0 at
### tools/b694_witness.py G0, band at data/b703_q0_band.txt :18's ordinate), reproduces b709's banked units at each banked onset point and the
### grid point just below it (both forms, three kinds, each S within the banked ball), the onset read NEGATIVE and the point below it not.
### THE PRICE, printed before each zero runs: b709's banked seconds per point (data/b709_grid_units*.jsonl: both forms, three kinds) times the
### points of the bracket the prediction falls in, and b707's seven rungs; the measured seconds printed beside after.
### THE GUARD: free memory read before each call and each batch (GlobalMemoryStatusEx); a call is refused beneath 2560 MB plus 250 MB per
### worker. Each call runs at most ~540 s of batches and resumes from its units.
### Routes: `c1` ; `price <zero>` ; `run <zero>` (call again until it prints THE ONSET or BEYOND REACH) ; `bank`.
### Written by the Write tool at b723; it writes its units file and data/b723_support.txt and nothing else. Every value a ball at 128 bits.
### Nothing here proves RH or GRH.
"""
import ctypes
import io
import json
import math
import os
import re
import sys
import time
from multiprocessing import Pool

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b709_grid as G9            # noqa: E402  ### b709's grid, window and terms: imported unedited
import b707_onset as O7           # noqa: E402  ### b707's ladder, window, terms, gram and reading: imported unedited

bs, bl, fmt = G9.WB.bs, G9.WB.bl, G9.WB.fmt
UNITS = os.path.join(D, 'b723_support_units.jsonl')
RULE_BANK = os.path.join(D, 'b723_support_rule.txt')
LADDER = [r for r, _w in O7.RUNGS]                     # ### log2, 32, 48, 64, 96, 128, 192
WIDTH = dict(O7.RUNGS)
HOLD_MB, PER_WORKER_MB = 2560, 250
WORKERS = 4
BATCH = 4                                              # ### grid points per batch (x 3 kinds per form)
BUDGET = 540
POS, NEG = 'POSITIVE DEFINITE BEYOND ITS BOUND', 'NEGATIVE DIRECTION BEYOND ITS BOUND'
BANKED = dict(rho0=dict(g0=O7.RHO0_IM, onset='mid929_937', a='6.838396011', lo='log2', hi='32'),
              band=dict(g0=O7.BAND_IM, onset='rung32381', a='10.38532711', lo='128', hi='192'))


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def free_mb():
    class MS(ctypes.Structure):
        _fields_ = [('dwLength', ctypes.c_ulong), ('dwMemoryLoad', ctypes.c_ulong), ('ullTotalPhys', ctypes.c_ulonglong),
                    ('ullAvailPhys', ctypes.c_ulonglong), ('ullTotalPageFile', ctypes.c_ulonglong), ('ullAvailPageFile', ctypes.c_ulonglong),
                    ('ullTotalVirtual', ctypes.c_ulonglong), ('ullAvailVirtual', ctypes.c_ulonglong), ('ullAvailExtendedVirtual', ctypes.c_ulonglong)]
    m = MS()
    m.dwLength = ctypes.sizeof(MS)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return int(m.ullAvailPhys // (1024 * 1024))


def guard(where):
    f = free_mb()
    need = HOLD_MB + PER_WORKER_MB * WORKERS
    print('  free MB %d at %s ; the call needs %d (hold %d + %d workers x %d) -- %s' % (f, where, need, HOLD_MB, WORKERS, PER_WORKER_MB,
                                                                                       'MET' if f >= need else 'REFUSED'), flush=True)
    if f < need:
        sys.exit('### FREE MEMORY BENEATH THE HOLD -- REFUSED (nothing computed after this line)')


# ================================================================================ UNITS
def units():
    U = {}
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[(u['route'], u['fam'], u['kind'], u['point'], u['obj'])] = u
    return U


def put_unit(u):
    u['at'] = utc()
    with open(UNITS, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


# ================================================================================ THE ZEROS AND THEIR FAMILIES
def zeros():
    """the rule's selection, read from its committed bank and checked against the list read afresh: {name: (beta, gamma0 string, a_pred)}."""
    import b723_support_rule as R
    txt = io.open(RULE_BANK, encoding='utf-8').read()
    sel = re.findall(r'\((\d)\) Q0 (off\d+) = ([0-9.]+) \+ ([0-9.]+)i ; beta - 1/2 = [0-9.]+ ; a\*_pred = ([0-9.]+)', txt)
    Z, _top, _n = R.zeros()
    full = dict((n, (b, g)) for n, b, g in Z)
    import b709_pairs as P9
    import b711_list as L11
    rows = P9.extended_rows(L11.units(), L11.top())[0]
    g_str = dict((n, t.mid().str(25, radius=False)) for n, s, t in rows if n.startswith('off'))
    out = {}
    for _i, name, b, g, ap in sel:
        fb, fg = full[name]
        assert abs(fb - float(b)) < 1e-9 and abs(fg - float(g)) < 1e-5, name
        out[name] = (fb, g_str[name], float(ap))
    return out


def register(fam, g0, lo, hi):
    """the family entered in b709's module dicts under its name: its frequency and its coarse bracket's two rungs."""
    G9.FREQS[fam] = g0
    G9.INTERVAL[fam] = (WIDTH[lo], WIDTH[hi])
    G9.ENDPOINT_RUNG[fam] = (lo, hi)


# ================================================================================ THE WORKERS
def _coarse_task(args):
    g0, rung, kind, obj = args
    u = O7.terms707(O7.window(kind, rung, g0), obj)
    return args, u


def _fine_task(args):
    fam, g0, lo, hi, pt, kind, obj = args
    register(fam, g0, lo, hi)
    u = G9.terms709(fam, pt, kind, obj)
    return args, u


def _form(us):
    G, M = O7.gram(us['C'], us['N'], us['CN'])
    return O7.reading(G, M), G


def _compute(pool, U, tasks, route, fam, pointname_of):
    """the tasks not yet banked, run in the pool, each unit banked as it lands."""
    todo = [t for t in tasks if (route, fam, t[-2], pointname_of(t), t[-1]) not in U]
    for args, u in pool.imap_unordered(_coarse_task if route == 'coarse' else _fine_task, todo):
        u.update(route=route, fam=fam, kind=args[-2], point=pointname_of(args), obj=args[-1])
        put_unit(u)
        U[(route, fam, u['kind'], u['point'], u['obj'])] = u


def _read(U, route, fam, point, obj):
    us = dict((k, U.get((route, fam, k, point, obj))) for k in G9.KINDS)
    if any(v is None for v in us.values()):
        return None
    return _form(us)[0]


# ================================================================================ (C1) THE BANKED ONSETS THROUGH THIS CODE PATH
def c1(*a):
    guard('c1')
    U = units()
    U9 = G9.units()
    ok_all = True
    with Pool(WORKERS) as pool:
        for fam, B in BANKED.items():
            name = 'c1_' + fam
            register(name, B['g0'], B['lo'], B['hi'])
            pts = G9.grid(name)
            i = [p['name'] for p in pts].index(B['onset'])
            two = [pts[i - 1], pts[i]]
            tasks = [(name, B['g0'], B['lo'], B['hi'], p, kd, obj) for p in two for obj in ('zeta', 'q0') for kd in G9.KINDS]
            _compute(pool, U, tasks, 'c1', name, lambda t: t[4]['name'])
            for p in two:
                for obj in ('zeta', 'q0'):
                    for kd in G9.KINDS:
                        u, b = U[('c1', name, kd, p['name'], obj)], U9[('terms', fam, kd, p['name'], obj)]
                        ok = bl(u['S']).overlaps(bl(b['S'])) and u['nmax'] == b['nmax']
                        ok_all &= ok
                        print('  C1 %-4s %-14s %-4s %-2s | S %s | b709 %s | %s' % (fam, p['name'], obj, kd, fmt(bl(u['S']), 12), fmt(bl(b['S']), 12),
                                                                              'AS WANTED' if ok else 'NOT AS WANTED'))
                    r = _read(U, 'c1', name, p['name'], obj)
                    want = POS if (obj == 'zeta' or p is two[0]) else NEG
                    ok = r['reading'] == want
                    ok_all &= ok
                    print('  C1 %-4s %-14s %-4s FORM | a %s | lambda_min %s | %s | wanted %s | %s' % (
                        fam, p['name'], obj, fmt(bl(U[('c1', name, 'C', p['name'], obj)]['a_radius']), 10), fmt(bl(r['lmin']), 10), r['reading'], want,
                        'AS WANTED' if ok else 'NOT AS WANTED'))
            a_on = float(bl(U[('c1', name, 'C', B['onset'], 'q0')]['a_radius']).mid())
            inside = 2 * math.log(float(O7.arb(WIDTH[B['lo']]).mid())) < a_on <= 2 * math.log(float(WIDTH[B['hi']]))
            ok_all &= inside and abs(a_on - float(B['a'])) < 1e-8
            print('  C1 %-4s the onset at a = %.9f (banked %s), inside the banked ladder interval (%s, %s]: %s' % (fam, a_on, B['a'], B['lo'], B['hi'],
                                                                                                                'AS WANTED' if inside else 'NOT AS WANTED'))
    put_unit(dict(route='c1verdict', fam='', kind='', point='', obj='', ok=bool(ok_all)))
    print('### C1 %s' % ('AS WANTED' if ok_all else 'NOT AS WANTED'))


def _c1_ok(U):
    v = U.get(('c1verdict', '', '', '', ''))
    return bool(v and v.get('ok'))


# ================================================================================ THE PRICE
def _secs709():
    U9 = G9.units()
    out = {}
    for fam in ('rho0', 'band'):
        s = [u['seconds'] for k, u in U9.items() if k[0] == 'terms' and k[1] == fam]
        out[fam] = 3 * sum(s) / len(s)          # ### per point and form: three kinds
    return out


def _bracket_of(a_pred):
    for lo, hi in zip(LADDER, LADDER[1:]):
        if a_pred <= 2 * math.log(float(O7.arb(WIDTH[hi]).mid())):
            return lo, hi
    return LADDER[-2], LADDER[-1]


def price(zero, *a):
    Z = zeros()
    beta, g0, ap = Z[zero]
    s = _secs709()
    lo, hi = _bracket_of(ap)
    register(zero, g0, lo, hi)
    n = len(G9.grid(zero))
    per = s['rho0'] if hi in ('32', '48', '64') else s['band']
    tot = 2 * per * (n + len(LADDER))
    print('PRICE %s: beta %.10f gamma0 %s a*_pred %.6f ; the bracket the prediction falls in (%s, %s], %d grid points ; b709`s seconds per point and form %.2f '
          '(rho0`s family) / %.2f (the band`s) ; both forms ; at most %d s (%.2f h) on one worker, about %d s with %d workers, less where the onset falls before '
          'the bracket`s top' % (zero, beta, g0, ap, lo, hi, n, s['rho0'], s['band'], tot, tot / 3600, tot / WORKERS, WORKERS))
    return tot


# ================================================================================ ONE ZERO
def run(zero, *a):
    U = units()
    if not _c1_ok(U):
        sys.exit('### C1 NOT READ AS WANTED -- NO ONSET AT A NAMED ZERO (the control before the figure)')
    guard('run ' + zero)
    Z = zeros()
    beta, g0, ap = Z[zero]
    t0 = time.time()
    with Pool(WORKERS) as pool:
        # ---- (1) b707's ladder, the zeta form first
        tasks = [(g0, r, kd, 'zeta') for r in LADDER for kd in G9.KINDS]
        _compute(pool, U, tasks, 'coarse', zero, lambda t: t[1])
        rz = dict((r, _read(U, 'coarse', zero, r, 'zeta')) for r in LADDER)
        bad = [r for r in LADDER if rz[r]['reading'] != POS]
        for r in LADDER:
            print('  %s coarse %-4s zeta lambda_min %s | %s' % (zero, r, fmt(bl(rz[r]['lmin']), 10), rz[r]['reading']), flush=True)
        if bad:
            sys.exit('### THE ZETA FORM NOT POSITIVE DEFINITE AT RUNG(S) %s -- NO Q0 FIGURE ON THE LADDER' % bad)
        tasks = [(g0, r, kd, 'q0') for r in LADDER for kd in G9.KINDS]
        _compute(pool, U, tasks, 'coarse', zero, lambda t: t[1])
        rq = dict((r, _read(U, 'coarse', zero, r, 'q0')) for r in LADDER)
        for r in LADDER:
            print('  %s coarse %-4s q0   lambda_min %s | %s' % (zero, r, fmt(bl(rq[r]['lmin']), 10), rq[r]['reading']), flush=True)
        negs = [r for r in LADDER if rq[r]['reading'] == NEG]
        if not negs:
            print('### %s: NO NEGATIVE DIRECTION ON b707`S LADDER TO 2 log 192 -- BEYOND REACH' % zero)
            put_unit(dict(route='onset', fam=zero, kind='', point='', obj='q0', beyond=True, seconds=int(time.time() - t0)))
            return
        hi = negs[0]
        if hi == LADDER[0]:
            print('### %s: NEGATIVE AT a = log 2, THE LADDER`S FOOT -- THE ONSET AT OR BELOW log 2' % zero)
            put_unit(dict(route='onset', fam=zero, kind='', point='log2', obj='q0', a=bs(2 * O7.arb(WIDTH['log2']).log()), foot=True, seconds=int(time.time() - t0)))
            return
        lo = LADDER[LADDER.index(hi) - 1]
        undec = [r for r in LADDER[:LADDER.index(hi)] if rq[r]['reading'] != POS]
        print('  %s THE COARSE BRACKET (%s, %s] ; rungs below it not POSITIVE: %s' % (zero, lo, hi, undec or 'none'), flush=True)
        # ---- (2) b709's fine grid in the bracket, in increasing a, the zeta form first per batch
        register(zero, g0, lo, hi)
        pts = G9.grid(zero)
        inner = pts[1:]                               # ### a+ is the coarse rung read positive above; a- is the last point
        for j in range(0, len(inner), BATCH):
            if time.time() - t0 > BUDGET:
                print('### THE CALL`S BUDGET REACHED BEFORE POINT %d of %d -- CALL AGAIN TO RESUME' % (inner[j]['i'], len(pts) - 1))
                return
            if j % (BATCH * 10) == 0:
                guard('%s point %d' % (zero, inner[j]['i']))
            batch = inner[j:j + BATCH]
            tasks = [(zero, g0, lo, hi, p, kd, 'zeta') for p in batch for kd in G9.KINDS]
            _compute(pool, U, tasks, 'fine', zero, lambda t: t[4]['name'])
            for p in batch:
                r = _read(U, 'fine', zero, p['name'], 'zeta')
                if r['reading'] != POS:
                    sys.exit('### THE ZETA FORM AT %s %s READS %s -- NO Q0 FIGURE AT THIS POINT' % (zero, p['name'], r['reading']))
            tasks = [(zero, g0, lo, hi, p, kd, 'q0') for p in batch for kd in G9.KINDS]
            _compute(pool, U, tasks, 'fine', zero, lambda t: t[4]['name'])
            for p in batch:
                r = _read(U, 'fine', zero, p['name'], 'q0')
                a_p = U[('fine', zero, 'C', p['name'], 'q0')]['a_radius']
                if p['i'] % 40 == 1 or r['reading'] != POS:
                    print('  %s %4d %-16s a %s | lambda_min %s | %s' % (zero, p['i'], p['name'], fmt(bl(a_p), 10), fmt(bl(r['lmin']), 10), r['reading']), flush=True)
                if r['reading'] == NEG:
                    a_on = float(bl(a_p).mid())
                    print('### %s: THE ONSET at %s, a = %s ; a*_pred %.6f ; a*/a*_pred - 1 = %+.5f ; %s' % (
                        zero, p['name'], fmt(bl(a_p), 10), ap, a_on / ap - 1, 'WITHIN 0.03' if abs(a_on / ap - 1) <= 0.03 else 'BEYOND 0.03: THE FALSIFIER FIRES'))
                    put_unit(dict(route='onset', fam=zero, kind='', point=p['name'], obj='q0', i=p['i'], a=a_p, lmin=r['lmin'], lo=lo, hi=hi,
                                  points=len(pts), seconds=int(time.time() - t0)))
                    return
        print('### %s: NO GRID POINT NEGATIVE IN (%s, %s] -- A DEFECT: the coarse rung %s read NEGATIVE' % (zero, lo, hi, hi))


# ================================================================================ THE BANK
def bank(*a):
    U = units()
    Z = zeros()
    s = _secs709()
    L = ['b723 -- COMPONENT 4 (ii), (R333)(5)(ii): H-SUPPORT`S ONSETS ON THE ZEROS ITS RULE NAMED, BY b707`S ROUTE ON b709`S LADDER (%s)' % utc(), '',
         '### by tools/b723_support.py (b707`s ladder and b709`s fine grid, both imported unedited); the registration data/b723_registrations.txt (i)',
         '### :17-:34 (relay 9ad26421) and the rule`s output data/b723_support_rule.txt (relay 0e91c670), both committed before any onset. THE ONSET:',
         '### the least fine-grid point in the coarse bracket read NEGATIVE DIRECTION BEYOND ITS BOUND, the zeta form read POSITIVE at every point first.',
         '### Units: data/b723_support_units.jsonl (untracked). b709`s seconds per point and form: rho0`s family %.2f, the band`s %.2f.' % (s['rho0'], s['band']), '']
    L.append('## (C1) THE BANKED ONSETS THROUGH THIS CODE PATH: %s' % ('AS WANTED' if _c1_ok(U) else 'NOT AS WANTED'))
    for fam, B in BANKED.items():
        u = U.get(('c1', 'c1_' + fam, 'C', B['onset'], 'q0'))
        L.append('  %-4s onset %s at a = %s (banked %s), its point below and both forms` S within b709`s balls' % (
            fam, B['onset'], fmt(bl(u['a_radius']), 10) if u else '### NOT RUN', B['a']))
    L.append('')
    L.append('## THE ZEROS, IN THE RULE`S ORDER')
    res = []
    for name, (beta, g0, ap) in Z.items():
        o = U.get(('onset', name, '', '', 'q0'))
        o = o or next((u for k, u in U.items() if k[0] == 'onset' and k[1] == name), None)
        cz = [(r, _read(U, 'coarse', name, r, 'q0')) for r in LADDER]
        L.append('  %s: beta %.10f ; gamma0 %s ; a*_pred %.6f' % (name, beta, g0, ap))
        L.append('    the ladder (q0): ' + ' ; '.join('%s %s' % (r, ('%s %s' % (fmt(bl(x['lmin']), 6), 'POS' if x['reading'] == POS else ('NEG' if x['reading'] == NEG else 'UND'))) if x else 'not run')
                                                    for r, x in cz))
        if o is None:
            L.append('    NOT RUN')
            res.append((name, None))
            continue
        if o.get('beyond') or o.get('foot'):
            top = 2 * math.log(192)
            L.append('    %s' % ('BEYOND REACH: no negative direction on the ladder to 2 log 192 = %.6f; no onset computed. Were the onset above it, '
                                 'a*/a*_pred - 1 > %+.5f' % (top, top / ap - 1) if o.get('beyond') else 'NEGATIVE AT THE LADDER`S FOOT'))
            res.append((name, 'beyond' if o.get('beyond') else 'foot'))
            continue
        a_on = float(bl(o['a']).mid())
        dev = a_on / ap - 1
        res.append((name, dev))
        nu = [u for k, u in U.items() if k[0] in ('coarse', 'fine') and k[1] == name]
        L.append('    THE ONSET: %s (grid point %d of %d in (%s, %s]) at a = %s, lambda_min %s ; a*/a*_pred - 1 = %+.5f -- %s ; units %d, their seconds summed %d' % (
            o['point'], o['i'], o['points'] - 1, o['lo'], o['hi'], fmt(bl(o['a']), 10), fmt(bl(o['lmin']), 10), dev,
            'WITHIN 0.03' if abs(dev) <= 0.03 else 'BEYOND 0.03', len(nu), sum(u.get('seconds', 0) for u in nu)))
    run_ = [d for _n, d in res if isinstance(d, float)]
    fired = [n for n, d in res if isinstance(d, float) and abs(d) > 0.03]
    beyond = [n for n, d in res if d == 'beyond']
    L.append('')
    L.append('THE FALSIFIER (a computed family onset with |a*/a*_pred - 1| > 0.03): %s' % ('FIRED at %s' % fired if fired else ('NOT FIRED on %d zeros' % len(run_))))
    L.append('BEYOND REACH, NO ONSET COMPUTED (the falsifier as worded reads computed onsets only): %s' % (beyond or 'none'))
    L.append('THE HYPOTHESIS ((R333)(5): HELD, REFUTED or NOT SCORABLE): %s' % ('REFUTED' if fired else ('HELD' if run_ else 'NOT SCORABLE')))
    L.append('')
    L.append('### ### **H-SUPPORT: C1 %s ; ZEROS %d ; ONSETS COMPUTED %d ; WITHIN 0.03 %d ; BEYOND REACH %d ; FALSIFIER %s ; THE HYPOTHESIS %s.**' % (
        'AS WANTED' if _c1_ok(U) else 'NOT AS WANTED', len(Z), len(run_), sum(1 for d in run_ if abs(d) <= 0.03), len(beyond),
        'FIRED' if fired else 'NOT FIRED', 'REFUTED' if fired else ('HELD' if run_ else 'NOT SCORABLE')))
    p = os.path.join(D, 'b723_support.txt')
    with open(p + '.tmp', 'wb') as f:
        f.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(NL.join(L))
    print('written data/b723_support.txt')


ROUTES = dict(c1=c1, price=price, run=run, bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b723_support.py c1 | price <zero> | run <zero> | bank')
        sys.exit(2)
    fn(*sys.argv[2:])
