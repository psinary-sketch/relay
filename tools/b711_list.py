# -*- coding: utf-8 -*-
"""b711_list.py -- THE CERTIFIED LIST TOWARD 443, (R321)(7), W-ORD-Q0-ZEROS-443 (OPEN_TRAILS :15764): "the bands from 325 in fifteens in b709's
foreground form, each band closed by its count before the next ... On the author's word to stop, or where the act's remaining budget calls for
it, the reached height banked".

### UNTRACKED WRITE: data/b711_list_units* -- data/b711_list_units_band_<lo>_<hi>.jsonl, one file per band (b709's SEG form), appended as each unit
### lands, resumable; declared by prefix for the root route's exclusion list.

### THE ROUTE: tools/b709_pairs.py IMPORTED UNEDITED -- its band route (the on-line scan to one past the asked top and the top set clear of a zero
### on the line, the count by b667's half path in twelve pieces per edge in the foreground, the on-line zeros by the certified sign of Lambda_Q
### halved to 1e-8, the off-line zeros by its Newton candidates on the grid from 310 on, each band COMPLETE where N = on + 2 off) and its chain
### (_bands, _chain, _complete_to, extended_rows). Two of its module functions are rebound here and nothing else: `units` reads b709's banked
### units (the list complete to 325, data/b709_pairs.txt :36) and this act's band files beside them; `put_unit` writes this act's band file
### through the membrane (tools/act_membrane.py guard_path, standing clauses v2 row (53)). b709's arithmetic and grids are its own; one budget
### is lowered: the count's per-call budget from 420 s to 300 s (half_path_pieces wrapped, its other arguments unchanged), since a piece next to
### the line runs about 270 s at these heights and 420 + 270 passes the 590 s guard (band [355, 369.75]'s fourth call ran 577 s).
### THE BANDS: from the chain's top in fifteens on the nominal grid 325, 340, ..., 445 -- `next` runs the band from the top the chain has reached
### to the next nominal height above it (b709's band sets the band's own top clear of a zero on the line, so a band's ends may move by < 0.1).
### Routes: `next` (one foreground call of the next band; call again until the band prints COMPLETE) ; `band <lo> <hi>` ; `status` ;
### `bank [dry]` -> data/b711_list.txt, data/b711_list.json, data/b711_list_hashes.txt. Written by the Write tool at b711; it writes only its band
### files and those banks. Nothing here proves RH or GRH; the list certifies zeros of Z_Q in the bands it closes and states nothing beyond them.
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
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b709_pairs as P9            # noqa: E402  ### b709's band route and chain, imported unedited

ACT = 'b711'
PFX = '%s_list_units_band_' % ACT
GRID = [325 + 15 * k for k in range(9)]   # ### 325, 340, ..., 445
TARGET = 443
NEEDED = dict((i, P9.NEEDED[i]) for i in (11, 15))   # ### 405.4, 442.3 (data/b707_registrations.txt :25-:36 as b709 carries them)
_P9_UNITS = P9.units


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _membrane(p):
    import act_membrane as MEM
    import b711_record as REC
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)


def units():
    """b709's units (its own reader, unedited) and this act's band files beside them; a later unit of the same key wins."""
    U = _P9_UNITS()
    for f in sorted(f for f in os.listdir(D) if f.startswith(PFX) and f.endswith('.jsonl')):
        for l in io.open(os.path.join(D, f), encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[(u['route'], u['key'])] = u
    return U


def put_unit(u):
    u['at'] = utc()
    path = os.path.join(D, '%s%s.jsonl' % (PFX, P9.SEG or 'misc'))
    _membrane(path)
    with open(path, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


P9.units, P9.put_unit = units, put_unit
_P9_PIECES = P9.half_path_pieces
COUNT_BUDGET = 300


def half_path_pieces(U, key, t_lo, t_hi, parts=12, budget=COUNT_BUDGET):
    return _P9_PIECES(U, key, t_lo, t_hi, parts, budget)


P9.half_path_pieces = half_path_pieces


def top():
    return P9._complete_to(P9._bands(units()), units())


def nxt(*a):
    t = top()
    if t >= TARGET:
        print('  the list is complete to %s, at or above %s: no band to run' % (t, TARGET))
        return
    hi = [g for g in GRID if g > t + 1.0][0]
    print('  the chain`s top %s ; the band [%s, %s]' % (t, t, hi), flush=True)
    P9.band(str(t), str(hi))


def band(lo, hi, *a):
    P9.band(lo, hi)


def _rows():
    U = units()
    bands = [b for b in P9._bands(U) if b['t_hi'] > 325.0 + 1e-9]
    t = top()
    rows, n_on, n_off = P9.extended_rows(U, t)
    return U, bands, t, rows, n_on, n_off


def status(*a):
    U, bands, t, rows, n_on, n_off = _rows()
    for b in bands:
        print('  band [%s, %s]: N %s ; on-line %s ; off-line %s ; %s' % (b['t_lo'], b['t_hi'], b['N'], b['on'], b['off'], 'COMPLETE' if b['complete'] else 'INCOMPLETE'))
    print('### THE LIST COMPLETE TO %s ; rows %d (on-line above 150 %d, off-line pairs above 150 %d) ; pair 11 needs > %s: %s ; pair 15 needs > %s: %s' % (
        t, len(rows), n_on, n_off, NEEDED[11], t > NEEDED[11], NEEDED[15], t > NEEDED[15]))


def _put(name, data):
    p = os.path.join(D, name)
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)
    return hashlib.sha256(data).hexdigest()


def bank(*a):
    U, bands, t, rows, n_on, n_off = _rows()
    chain, _t = P9._chain(U)
    new = [(b, f) for b, f in chain if b['t_hi'] > 325.0 + 1e-9]
    L = ['%s -- COMPONENT 4, (R321)(7): THE CERTIFIED LIST TOWARD %d, W-ORD-Q0-ZEROS-443, IN b709`S FOREGROUND FORM (%s)' % (ACT, TARGET, utc()), '',
         '### rows are bands above b709`s 325 (data/b709_pairs.txt :35-:36), each by tools/b709_pairs.py`s band route imported unedited: N(band) by b667`s half path,',
         '### the on-line zeros by the certified sign of Lambda_Q halved to %s, the off-line zeros by its Newton candidates (point values and the band`s count, b709`s' % P9.W_ON,
         '### RECT_CERTIFY %s), COMPLETE where N = on + 2 off. THE LIST`S BASE: b709`s chain complete to 325.' % P9.RECT_CERTIFY, '']
    for b in bands:
        on = U.get(('online', b['key']))
        offz = U.get(('offline', b['key']))
        L.append('  band [%s, %s] | N %s | on-line %s | off-line %s %s | %s' % (
            b['t_lo'], b['t_hi'], b['N'], b['on'], b['off'], [(z['re'][:10], z['im'][:12]) for z in (offz['zeros'] if offz else [])] or '',
            'COMPLETE' if b['complete'] else '### INCOMPLETE'))
    L += ['', '### THE CHAIN ABOVE 325: %d bands chained ; THE LIST COMPLETE TO %s ; rows %d (b675`s 180 representatives and the zeros above 150: on-line %d, '
          'off-line pairs %d)' % (len(new), t, len(rows), n_on, n_off),
          '### THE PAIRS` HEIGHTS: pair 11 needs T0` > %s -- %s ; pair 15 needs T0` > %s -- %s' % (
              NEEDED[11], 'PASSED' if t > NEEDED[11] else 'NOT REACHED', NEEDED[15], 'PASSED' if t > NEEDED[15] else 'NOT REACHED'), '',
          '### ### **THE LIST COMPLETE TO %s ; BANDS ABOVE 325 %d (COMPLETE %d) ; PAIR 11 %s ; PAIR 15 %s.**' % (
              t, len(bands), sum(1 for b in bands if b['complete']), 'REACHED' if t > NEEDED[11] else 'BEYOND REACH AT %s' % t,
              'REACHED' if t > NEEDED[15] else 'BEYOND REACH AT %s' % t)]
    j = dict(at=utc(), base=325.0, top=t, bands=bands, chained=[dict(b, t_from=f) for b, f in new], rows=len(rows), new_on=n_on, new_off=n_off,
             needed=NEEDED, reached=dict((k, t > v) for k, v in NEEDED.items()),
             units=dict(('%s|%s' % k, v) for k, v in U.items() if k[0] in ('count', 'online', 'offline') and float(v.get('t_hi') or 0) > 325.0 + 1e-9))
    print(NL.join(L))
    if 'dry' in a:
        return
    h1 = _put('%s_list.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    h2 = _put('%s_list.json' % ACT, (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    H = ['%s -- THE LIST`S BANKS, THEIR sha256 (%s)' % (ACT, utc()), '', '  %s  data/%s_list.txt' % (h1, ACT), '  %s  data/%s_list.json' % (h2, ACT)]
    for f in sorted(f for f in os.listdir(D) if f.startswith(PFX) and f.endswith('.jsonl')):
        H.append('  %s  data/%s (untracked, its units)' % (hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest(), f))
    H += ['', '### ### **BANKS 2 HASHED, THE BAND FILES BESIDE.**']
    _put('%s_list_hashes.txt' % ACT, (NL.join(H) + NL).encode('utf-8'))
    print(H[-1])


ROUTES = dict(next=nxt, band=band, status=status, bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b711_list.py next | band <lo> <hi> | status | bank [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
