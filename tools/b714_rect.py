# -*- coding: utf-8 -*-
"""b714_rect.py -- (R324)(9), PAIR 7'S RECTANGLE: an argument-principle count of the zeros of Z_Q1 (Q1 = x^2 + xy + 4y^2, discriminant -15)
in a rectangle about 1.025973 + 61.422798 i (data/b713_list.txt :40) lying wholly in Re s > 1, by b667's interval method -- edge_arg on the
four edges (tools/b667_epstein_certify.py :284), as tools/b709_pairs.py's rect_pieces / rect_assemble (:470-:515) run it, imported unedited
over b713's carried engine (tools/b713_list.py, sqrt(23) -> sqrt(15) at import, its controls data/b713_list_controls.txt). CERTIFIED where
the count reads 1; priced and carried where the run passes one hour.

### THE CONTROLS FIRST: (K0) the carry in a worker process (Windows spawn re-runs this module, which imports b713_list, so each worker
### compiles the carried engine): the worker's zq names b713's carried source and DQ 15; (K1) POS, a rectangle about -15 pair 1
### (0.800011 + 12.038599 i, data/b713_list.txt :34; its band [1, 15] COMPLETE, N 6 = 4 + 2 x 1, :18) counts 1; (K2) a rectangle in Re s > 1
### at t in [61.00, 61.02], below the least height of a zero with Re > 1 (61.4228, :72) inside the COMPLETE band [59.881486, 75.0] (:22),
### counts 0. THE UNITS: data/b714_rect_units.jsonl (this tool's; b709's and b713's units files are never written: b713_list's rebinding of
### b709's units/put_unit is replaced here before any piece runs). Each `run` call runs at most PROCS pieces (a pool joined before the
### return) and banks them; `bank [dry]` assembles and writes data/b714_rect.txt. Run as `python -X utf8` (it imports its siblings).
### UNTRACKED WRITE: data/b714_rect_units.jsonl (the units file, left untracked as b709's and b713's are; declared at Component 5 for the root)
"""
import hashlib
import io
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
ACT = 'b714'
OUT = os.path.join(D, 'b714_rect.txt')
UNITS = os.path.join(D, 'b714_rect_units.jsonl')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b713_list as LST            # noqa: E402  ### the engine carried to sqrt(15) at import (also in each spawned worker)
from flint import arb, ctx         # noqa: E402

P9, CERT = LST.P9, LST.CERT
PARTS, NSEG, PROCS = 2, 2, 6
CAP_S = 3600                       # ### (R324)(9): priced and carried where the run passes one hour
RECTS = [  # (name, re_lo, re_hi, im_lo, im_hi, the count wanted, what it is)
    ('K1', '0.790010988', '0.810010988', '12.028598629', '12.048598629', 1, 'POS: about -15 pair 1 (data/b713_list.txt :34, band :18 COMPLETE)'),
    ('K2', '1.015972616', '1.035972616', '61.000000000', '61.020000000', 0, 'ZERO: Re s > 1 below the least height 61.4228 (:72), band :22 COMPLETE'),
    ('P7', '1.015972616', '1.035972616', '61.412798309', '61.432798309', 1, 'PAIR 7: about 1.025972616 + 61.422798309 i (:40), wholly in Re s > 1'),
]


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def units():
    U = {}
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[(u['route'], u['key'])] = u
    return U


def put_unit(u):
    u['at'] = utc()
    with open(UNITS, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


P9.units, P9.put_unit = units, put_unit     # ### this tool's units file alone (b713_list had bound b713's)


def _carry_task(_x):
    """in a worker: what the engine there is."""
    return dict(pid=os.getpid(), dq=getattr(CERT, 'DQ', None), zq_src=CERT.zq.__code__.co_filename, m_src=CERT.M_of.__code__.co_filename)


def k0(*a):
    import multiprocessing as mpr
    LST._free('K0')
    pool = mpr.Pool(2)
    try:
        res = pool.map(_carry_task, [0, 1])
    finally:
        pool.close()
        pool.join()
    ok = all(r['dq'] == 15 and r['zq_src'].startswith('<b713 carried') and r['m_src'].startswith('<b713 carried') for r in res)
    u = dict(route='k0', key='k0', workers=res, ok=ok, main_dq=CERT.DQ, main_zq_src=CERT.zq.__code__.co_filename)
    put_unit(u)
    print('  (K0) the carry in %d workers: %s -- %s' % (len(res), res, 'AS WANTED' if ok else 'NOT AS WANTED'))


def _rect(name):
    return [r for r in RECTS if r[0] == name][0]


def run(name, *a):
    U = units()
    if not (U.get(('k0', 'k0')) or {}).get('ok'):
        sys.exit('### (K0) NOT YET AS WANTED -- NO RECTANGLE RUN')
    if name == 'P7':
        for c in ('K1', 'K2'):
            res = [U.get(('rectpiece', '%s_%d_%d' % (c, i, j))) for i in range(4) for j in range(PARTS)]
            if not all(res) or P9.rect_assemble(res)[0] != _rect(c)[5]:
                sys.exit('### CONTROL %s NOT YET ASSEMBLED AS WANTED -- PAIR 7 NOT RUN (controls before figures)' % c)
    LST._free('RECT %s' % name)
    _n, lo, hi, ilo, ihi, want, what = _rect(name)
    t0 = time.time()
    ctx.prec = P9.CPREC
    res, rem = P9.rect_pieces(U, name, arb(lo), arb(hi), arb(ilo), arb(ihi), nseg=NSEG, procs=PROCS, parts=PARTS)
    took = time.time() - t0
    secs = sum(r.get('seconds', 0) for r in {(r['i'], r['j']): r for r in res}.values())
    print('  %s [%s, %s] x [%s, %s]: pieces banked %d of %d, remaining %d ; this call %d s' % (name, lo, hi, ilo, ihi, len(res), 4 * PARTS, rem, int(took)))
    if rem == 0:
        n, cb, st = P9.rect_assemble(res)
        print('  %s count %s (ball %s) ; wanted %d ; segments %d, max depth %d, unresolved %s' % (
            name, n, cb.str(15, radius=True) if cb is not None else None, want, st['segments'], st['max_depth'], st['unresolved'][:4] or 'NONE'))


def bank(*a):
    U = units()
    k = U.get(('k0', 'k0'))
    L = ['%s -- (R324)(9): PAIR 7`S RECTANGLE, AN ARGUMENT-PRINCIPLE COUNT IN Re s > 1 BY b667`S INTERVAL METHOD (%s)' % (ACT, utc()), '',
         '### the method: b667`s edge_arg on the four edges (tools/b667_epstein_certify.py :284), each edge in %d pieces of %d segments, as' % (PARTS, NSEG),
         '### tools/b709_pairs.py rect_pieces / rect_assemble (:470-:515) run it, imported unedited over b713`s carried engine (tools/b713_list.py,',
         '### sqrt(23) -> sqrt(15) at import; data/b713_list_controls.txt). The count the unique integer in (sum of the edges` arguments)/(2 pi) when',
         '### that ball`s radius is below 1/2, else UNREAD. Units data/b714_rect_units.jsonl. The cap one hour (%d s) of piece time.' % CAP_S, '',
         '## I. THE CONTROLS, BEFORE PAIR 7',
         '  (K0) the carry in the workers: %s -- %s' % ((k or {}).get('workers'), 'AS WANTED' if (k or {}).get('ok') else 'NOT AS WANTED OR NOT RUN')]
    ok = [bool((k or {}).get('ok'))]
    total = 0
    verdict = None
    for name, lo, hi, ilo, ihi, want, what in RECTS:
        res = [U[('rectpiece', '%s_%d_%d' % (name, i, j))] for i in range(4) for j in range(PARTS) if ('rectpiece', '%s_%d_%d' % (name, i, j)) in U]
        seq = [json.loads(l) for l in io.open(UNITS, encoding='utf-8') if l.strip()]
        seq = [u for u in seq if u.get('route') == 'rectpiece' and u['key'].startswith(name + '_')]
        batches = [seq[i:i + PROCS] for i in range(0, len(seq), PROCS)]     # ### one call banks at most PROCS pieces, in file order
        csecs = sum(b[0].get('seconds', 0) for b in batches)
        total += csecs
        if name == 'P7':
            L += ['', '## II. PAIR 7']
        if len(res) < 4 * PARTS:
            L.append('  (%s) %s: [%s, %s] x [%s, %s] -- pieces %d of %d banked, NOT ASSEMBLED ; piece time so far %d s' % (
                name, what, lo, hi, ilo, ihi, len(res), 4 * PARTS, csecs))
            ok.append(False)
            if name == 'P7':
                verdict = 'PRICED AND CARRIED' if total > CAP_S else 'NOT COMPLETE'
            continue
        n, cb, st = P9.rect_assemble(res)
        good = n == want
        L.append('  (%s) %s: [%s, %s] x [%s, %s] -- count %s (ball %s), wanted %d ; segments %d, max depth %d, unresolved %s ; piece time %d s -- %s' % (
            name, what, lo, hi, ilo, ihi, n, cb.str(15, radius=True) if cb is not None else 'UNREAD', want, st['segments'], st['max_depth'],
            st['unresolved'][:4] or 'NONE', csecs, ('AS WANTED' if good else 'NOT AS WANTED') if name != 'P7' else ('CERTIFIED' if good else 'NOT CERTIFIED')))
        if name == 'P7':
            verdict = 'CERTIFIED' if (good and all(ok)) else ('NOT CERTIFIED' if n is not None else 'UNREAD')
        else:
            ok.append(good)
    L += ['', '### ### **CONTROLS %d OF %d AS WANTED ; PAIR 7`S RECTANGLE [1.015972616, 1.035972616] x [61.412798309, 61.432798309], WHOLLY IN Re s > 1 : %s ;'
          ' PIECE TIME %d s AGAINST THE CAP %d s.**' % (sum(ok), len(ok), verdict, total, CAP_S)]
    out = NL.join(L) + NL
    print(out)
    if 'dry' in a:
        return
    data = out.encode('utf-8')
    with open(OUT + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(OUT + '.tmp', OUT)
    print('  %s  data/b714_rect.txt' % hashlib.sha256(data).hexdigest())


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r == 'k0':
        k0()
    elif r == 'run' and len(sys.argv) > 2 and sys.argv[2] in [x[0] for x in RECTS]:
        run(sys.argv[2], *sys.argv[3:])
    elif r == 'bank':
        bank(*sys.argv[2:])
    else:
        print('usage: b714_rect.py k0 | run <K1|K2|P7> | bank [dry]')
        sys.exit(2)
