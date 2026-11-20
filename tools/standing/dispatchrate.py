# -*- coding: utf-8 -*-
"""tools/standing/dispatchrate.py -- v1.38.13, (R374)(5) [K14]: THE PRICE'S RATE, A DISPATCH'S HOURS TAKEN FROM THE KIND OF BUILD IT IS.

b763's table priced every dispatch at zq-b730's 0.325 h (data/b763_price.json h_per_dispatch, from data/b757_price.txt :8), where b763's
seven runs took 0.25 to 1.73 h of wall time each, the completed ones 67.7 to 103.9 min, the runner rebuilding the kernel's modules from
source at each (data/b763_misses.txt (11)); its ceiling read the rows as priced and counted a dispatch at about a fifth of what it took.
This reader takes each dispatching row's hours from its build's kind and the timings the table names; a ceiling sums what it returns.

  THE KIND: 'whole', a build of the kernel whole, every module from source; 'closure', one module's import closure, its upper a whole
    build (a closure dispatch rebuilds what the runner does not hold). Read from the row's `kind` field ('dispatch-whole',
    'dispatch-closure', 'beside-whole', 'beside-closure'); a dispatching row that names no kind is read as 'whole', the dear kind, so printed.
  THE TIMINGS: the table's `whole_min` [lo, hi] and `closure_min`; a table holding none (a flat `h_per_dispatch`) is read at the timings
    the caller passes, its flat rate set aside and printed, or REFUSED where none is passed.
  THE WAITS: the dispatches a row waits on one after another, its dispatches by default; the caller names the rows whose dispatches run
    together, each with its row's words.
  THE FLOOR: the lower waits at the kind's lower minutes to the upper waits at a whole build's upper minutes; a row priced below its floor
    is read AT ITS FLOOR and printed BELOW ITS KIND; one at or above it is read as priced, AT ITS KIND.

  python -X utf8 -u tools/standing/dispatchrate.py <price json> [<whole lo> <whole hi> <closure>]    a print; writes nothing
"""
import json
import sys

KIND_OF = {'dispatch-whole': 'whole', 'dispatch-closure': 'closure', 'beside-whole': 'whole', 'beside-closure': 'closure'}
TOL = 0.005   # ### the table's hours are rounded to the hundredth
NL = chr(10)


def timings(price, given=None):
    """({'whole': (lo, hi), 'closure': (lo, hi)} in minutes or None, its source in words)."""
    w, c = price.get('whole_min'), price.get('closure_min')
    flat = (', its flat rate of %s h a dispatch set aside' % price['h_per_dispatch']) if 'h_per_dispatch' in price else ''
    if w and c is not None:
        return dict(whole=(float(w[0]), float(w[1])), closure=(float(c), float(w[1]))), 'the table`s whole_min and closure_min'
    if given:
        return dict(whole=(float(given[0]), float(given[1])), closure=(float(given[2]), float(given[1]))), 'the caller`s timings, the table naming none%s' % flat
    return None, 'NO TIMINGS: the table names no build`s minutes%s, and the caller passed none' % flat


def read_row(row, t, waits=None):
    """the row read at its kind, or None for a row that dispatches nothing."""
    d = list(row.get('dispatches') or [0, 0])
    if max(d) <= 0:
        return None
    k = KIND_OF.get(row.get('kind'))
    src = 'its kind %s' % row.get('kind') if k else 'NO KIND NAMED, read as a whole build'
    k = k or 'whole'
    w = list(waits) if waits else d
    flo, fhi = w[0] * t[k][0] / 60.0, w[1] * t[k][1] / 60.0
    below = row['lo_h'] < flo - TOL or row['hi_h'] < fhi - TOL
    return dict(key=row['key'], kind=k, kind_from=src, dispatches=d, waits=w, floor=[round(flo, 2), round(fhi, 2)], priced=[row['lo_h'], row['hi_h']],
                read=[round(max(row['lo_h'], flo), 2), round(max(row['hi_h'], fhi), 2)], below=below,
                verdict='BELOW ITS KIND, READ AT ITS FLOOR' if below else 'AT ITS KIND')


def read(price, given=None, waits=None, rows_key='rows'):
    """({key: the row read}, lines, ok): every dispatching row of price[rows_key] read at its kind; ok False where no timings stand.
    `waits` maps a row's key to (lo, hi) waits, the rows whose dispatches run together."""
    t, src = timings(price, given)
    L = ['## THE PRICE`S RATE BY THE KIND OF BUILD (tools/standing/dispatchrate.py, v1.38.13, (R374)(5) [K14]), the rows of `%s`: %s' % (rows_key, src)]
    if t is None:
        return {}, L + ['  ### REFUSED: no dispatching row is read at a rate that names no build'], False
    L.append('  a build of the kernel whole %.1f-%.1f min ; a module`s closure %.1f min, its upper a whole build' % (t['whole'][0], t['whole'][1], t['closure'][0]))
    out = {}
    for r in price.get(rows_key) or []:
        x = read_row(r, t, (waits or {}).get(r['key']))
        if x:
            out[r['key']] = x
            L.append('  %-30s %s (%s) ; dispatches %d-%d, waits %d-%d ; floor %.2f-%.2f h ; priced %.2f-%.2f h -> %s%s' % (
                x['key'], x['kind'], x['kind_from'], x['dispatches'][0], x['dispatches'][1], x['waits'][0], x['waits'][1], x['floor'][0], x['floor'][1],
                x['priced'][0], x['priced'][1], x['verdict'], (' %.2f-%.2f h' % tuple(x['read'])) if x['below'] else ''))
    L.append('  dispatching rows read %d ; BELOW ITS KIND %d' % (len(out), sum(1 for x in out.values() if x['below'])))
    return out, L, True


def rows_at_kind(price, given=None, waits=None):
    """(the table's rows with each dispatching row's lo_h and hi_h read at its kind, lines, ok): what a ceiling sums."""
    out, L, ok = read(price, given, waits)
    rows = []
    for r in price.get('rows') or []:
        r2 = dict(r)
        if r['key'] in out:
            r2['lo_h'], r2['hi_h'] = out[r['key']]['read']
        rows.append(r2)
    return rows, L, ok


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) not in (1, 4):
        sys.exit(__doc__)
    p = json.load(open(a[0], encoding='utf-8'))
    _o, L, ok = read(p, tuple(float(x) for x in a[1:]) if len(a) == 4 else None)
    print(NL.join(L))
    sys.exit(0 if ok else 3)
