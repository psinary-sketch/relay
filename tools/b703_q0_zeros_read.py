# -*- coding: utf-8 -*-
"""b703_q0_zeros_read.py -- (R313)(6)(i), W-ORD-Q0-BAND-CONTROL: THE NAMED READER OF b681'S CERTIFIED ZEROS OF Q0.

### The compressed bank relay data/b681_epstein_zeros_narrowed.json.gz is read by this reader alone (the ferry's read clause). Before it
### opens the bank it checks the gz's sha256 against relay data/b681_epstein_zeros_narrowed_hashes.txt :3 and, once decompressed in memory,
### the JSON's sha256 against :2; either unequal, it reads nothing and writes nothing. Its writes go to relay data/b703_q0_band.txt alone.
### Registered before it was written (relay data/b703_registrations.txt, committed alone at relay b8a36309): the hypothesis -- the bank
### holds a certified off-line zero of Q0 with 1/2 < Re ρ <= 7/8; the falsifier -- none in the bank, its height range then printed and the
### strip-locate instrument I-1 named for the range beyond it; the control -- the row count equals the stated 163 (relay
### data/b681_findings.json :2) and the row for ρ₀ reads Re 0.95326047479466068625 to the bank's digits. No witness and no Li coefficient
### is computed: the reader counts.
### Routes: `keys` -- the bank's keys and the first row's field names printed, no value read, nothing written; `count` -- the count,
### data/b703_q0_band.txt. Written by the Write tool at b703 after the registrations' commit.
"""
import decimal
import gzip
import hashlib
import io
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
BANK = os.path.join(D, 'b681_epstein_zeros_narrowed.json.gz')
HASHES = os.path.join(D, 'b681_epstein_zeros_narrowed_hashes.txt')
OUT = os.path.join(D, 'b703_q0_band.txt')
STATED_ROWS = 163
RHO0_RE = '0.95326047479466068625'
BINS = (('(1/2, 0.6]', decimal.Decimal('0.5'), decimal.Decimal('0.6'), True), ('(0.6, 0.75]', decimal.Decimal('0.6'), decimal.Decimal('0.75'), True),
        ('(0.75, 7/8]', decimal.Decimal('0.75'), decimal.Decimal('0.875'), True), ('(7/8, 1)', decimal.Decimal('0.875'), decimal.Decimal('1'), False))
RE_KEYS = ('re', 'real', 'sigma', 'beta', 'x', 're_mid', 'sigma_mid')
IM_KEYS = ('im', 'imag', 't', 'gamma', 'y', 'im_mid', 't_mid')
KIND_KEYS = ('kind', 'form', 'line', 'where', 'on_line', 'online')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
decimal.getcontext().prec = 80


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _pinned():
    """the two sha256 the hashes bank pins: (json at :2, gz at :3)."""
    L = io.open(HASHES, encoding='utf-8').read().replace(chr(13), '').split(NL)
    j = re.search(r'sha256 ([0-9a-f]{64})', L[1])
    z = re.search(r'sha256 ([0-9a-f]{64})', L[2])
    if not (L[1].startswith('data/b681_epstein_zeros_narrowed.json (inside the .gz) sha256') and L[2].startswith('data/b681_epstein_zeros_narrowed.json.gz sha256')
            and j and z):
        sys.exit('### THE HASHES BANK :2-:3 IS NOT AS READ -- NOTHING READ, NOTHING WRITTEN')
    return j.group(1), z.group(1)


def _open():
    pj, pz = _pinned()
    raw = open(BANK, 'rb').read()
    hz = hashlib.sha256(raw).hexdigest()
    if hz != pz:
        sys.exit('### THE .gz`S sha256 %s IS NOT THE PINNED %s -- NOTHING READ, NOTHING WRITTEN' % (hz, pz))
    js = gzip.decompress(raw)
    hj = hashlib.sha256(js).hexdigest()
    if hj != pj:
        sys.exit('### THE JSON`S sha256 %s IS NOT THE PINNED %s -- NOTHING READ, NOTHING WRITTEN' % (hj, pj))
    return json.loads(js.decode('utf-8'), parse_float=decimal.Decimal), hz, hj


def _rows(obj):
    """the bank's list of zero records: the top-level list, or the one list of dicts under a top-level key."""
    if isinstance(obj, list):
        return None, obj
    lists = [(k, v) for k, v in obj.items() if isinstance(v, list) and v and all(isinstance(x, dict) for x in v)]
    if len(lists) != 1:
        return None, None
    return lists[0]


def _field(row, names):
    hit = [k for k in row if k.lower() in names]
    return hit[0] if len(hit) == 1 else None


def _num(v):
    if isinstance(v, (int, decimal.Decimal)):
        return decimal.Decimal(v)
    if isinstance(v, str):
        m = re.match(r'^\s*\[?\s*([-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)', v)
        if m:
            return decimal.Decimal(m.group(1))
    if isinstance(v, list) and v:
        return _num(v[0])
    if isinstance(v, dict):
        for k in ('mid', 'center', 'value', 'mid_str'):
            if k in v:
                return _num(v[k])
    return None


def keys(*a):
    obj, hz, hj = _open()
    print('  the bank: relay data/b681_epstein_zeros_narrowed.json.gz ; gz sha256 %s ; JSON sha256 %s -- each equal to the hashes bank :3, :2' % (hz, hj))
    print('  its top-level %s ; keys %s' % (type(obj).__name__, sorted(obj) if isinstance(obj, dict) else '-'))
    rk, rows = _rows(obj)
    print('  the list of rows under %r: %s rows ; the first row`s field names %s' % (rk, len(rows) if rows is not None else '### NOT FOUND',
                                                                              sorted(rows[0]) if rows else '-'))
    print('  (no value read; nothing written)')


def count(*a):
    obj, hz, hj = _open()
    rk, rows = _rows(obj)
    if rows is None:
        sys.exit('### NO SINGLE LIST OF ROWS IN THE BANK -- NOTHING WRITTEN')
    fre, fim, fkind = _field(rows[0], RE_KEYS), _field(rows[0], IM_KEYS), _field(rows[0], KIND_KEYS)
    if not fre or not fim:
        sys.exit('### THE REAL-PART OR HEIGHT FIELD IS NOT ONE OF %s / %s (the row`s fields %s) -- NOTHING WRITTEN' % (RE_KEYS, IM_KEYS, sorted(rows[0])))
    pts = []
    for r in rows:
        re_, im_ = _num(r.get(fre)), _num(r.get(fim))
        pts.append(dict(re=re_, im=im_, kind=r.get(fkind) if fkind else None, raw_re=r.get(fre)))
    half = decimal.Decimal('0.5')
    tol = decimal.Decimal('1e-20')
    off = [p for p in pts if p['re'] is not None and abs(p['re'] - half) > tol]
    on = [p for p in pts if p['re'] is not None and abs(p['re'] - half) <= tol]
    unread = [p for p in pts if p['re'] is None or p['im'] is None]
    bins = []
    for name, lo, hi, closed in BINS:
        bins.append((name, [p for p in off if p['re'] > lo and (p['re'] <= hi if closed else p['re'] < hi)]))
    beyond = [p for p in off if p['re'] < half or p['re'] >= 1]
    band = [p for p in off if half < p['re'] <= decimal.Decimal('0.875')]
    lowest = min(band, key=lambda p: abs(p['im'])) if band else None
    hmin = min((p['im'] for p in pts if p['im'] is not None), default=None)
    hmax = max((p['im'] for p in pts if p['im'] is not None), default=None)
    r0 = [p for p in off if str(p['raw_re']).startswith(RHO0_RE) or (p['re'] is not None and abs(p['re'] - decimal.Decimal(RHO0_RE)) < decimal.Decimal('1e-20'))]
    c_rows = len(rows) == STATED_ROWS
    c_rho0 = len(r0) >= 1
    L = ['b703 -- (R313)(6)(i), W-ORD-Q0-BAND-CONTROL: b681`S CERTIFIED ZEROS OF Q0 COUNTED BY REAL PART, BY THE NAMED READER (%s)' % utc(), '',
         '### the reader: relay tools/b703_q0_zeros_read.py, registered before it was written (relay data/b703_registrations.txt, committed alone at',
         '### relay b8a36309); the bank opened after its gz sha256 %s and its JSON sha256 %s each equalled relay' % (hz, hj),
         '### data/b681_epstein_zeros_narrowed_hashes.txt :3 and :2. No witness and no Li coefficient computed: the reader counts. Rows are bins.', '',
         '  the bank`s top-level keys: %s ; the rows under %r ; the fields read: real part %r, height %r, kind %r' % (
             sorted(obj) if isinstance(obj, dict) else '-', rk, fre, fim, fkind),
         '  rows %d ; off the line %d ; on the line %d (|Re ρ - 1/2| <= 1e-20) ; values unread %d' % (len(rows), len(off), len(on), len(unread)),
         '  the heights: from %s to %s' % (hmin, hmax), '',
         '### THE OFF-LINE ROWS BY REAL PART (rows are bins: the bin | the count | each row`s Re ρ and Im ρ to 12 places):']
    for name, ps in bins:
        L.append('  %-12s %3d | %s' % (name, len(ps), '; '.join('%.12f + %.12f i' % (p['re'], p['im']) for p in sorted(ps, key=lambda p: abs(p['im']))) or '-'))
    L.append('  outside (1/2, 1): %d | %s' % (len(beyond), '; '.join('%.12f + %.12f i' % (p['re'], p['im']) for p in beyond) or '-'))
    L += ['', '### THE HYPOTHESIS: a certified off-line zero with 1/2 < Re ρ <= 7/8 -- %s' % (
        'MET: %d in the band, the lowest-height %.20f + %.20f i' % (len(band), lowest['re'], lowest['im']) if lowest else
        'FALSIFIED: none in the band; the bank`s heights run %s to %s, and beyond them the strip-locate instrument I-1 is the instrument named '
        'for the range above the list`s height (its price for b705`s ruling)' % (hmin, hmax)),
          '### THE CONTROL: the row count %d against the stated %d: %s ; the row for ρ₀ at Re %s to the bank`s digits: %s (%s)' % (
              len(rows), STATED_ROWS, c_rows, RHO0_RE, c_rho0, '; '.join('%s + %s i' % (p['raw_re'], p['im']) for p in r0) or 'NOT FOUND'),
          '', '### ### **ROWS %d (THE CONTROL %s) ; OFF THE LINE %d, ON IT %d ; IN (1/2, 7/8] %d ; ρ₀ READ %s ; NO WITNESS COMPUTED.**' % (
              len(rows), 'AGREES' if c_rows and c_rho0 else '### FAILS', len(off), len(on), len(band), c_rho0)]
    if not (c_rows and c_rho0):
        print(NL.join(L))
        sys.exit('### THE CONTROL FAILS -- NOTHING WRITTEN')
    with open(OUT + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(OUT + '.tmp', OUT)
    print(NL.join(L))


if __name__ == '__main__':
    fn = dict(keys=keys, count=count).get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b703_q0_zeros_read.py keys | count')
        sys.exit(2)
    fn(*sys.argv[2:])
