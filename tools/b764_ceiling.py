# -*- coding: utf-8 -*-
"""tools/b764_ceiling.py -- (R374)(3): THE CEILING, 24 HOURS AGAINST THE PRICE TABLE'S LOWER FIGURES, READ AFTER COMPONENT 2 (the step-zero
reading stands in data/b764_price.txt). "THE CEILING: 24 hours against the table's lower figures, read at step zero and after Component 2;
over it, carried by name in this order, each with its price: the orders of (8), the last priced leaving soonest; then the trial of (7);
then the reading of (6); then (9)(b); then the keys of (5) in the order of repair read from its end" (data/b764_ferry.txt :13).
Carried from tools/b763_ceiling.py by tools/standing/carry.py (data/b764_carry_ceiling.txt, its two moved cites printed there) and
rewritten for (R374)(3) by the Write tool before its first run; committed before it runs. Its writes: data/b764_ceiling.txt and
data/b764_ceiling.json, each reading appended to the readings the json holds and the text rendered whole from it; a second reading at a
point the json holds is refused, nothing written.

THE RATE ((R374)(5) [K14]): each dispatching row of the table is read at its build's kind by tools/standing/dispatchrate.py, a row priced
below its kind's floor read at the floor and printed so; the rows whose dispatches run together named in WAITS with their row's words.

THE READING: the hours spent from the delivery (transcript line 213526, 2026-11-20T16:52:08Z) to the read; the table's summed rows that
remain at the point, at their lower figures read at their kind; the sum against 24 h, and what it carries in (R374)(3)'s order where it
goes over; then the orders of (8) in ascending order of the table's upper hours, each built where what the ceiling leaves after every other
remaining row at its lower figure holds its upper figure ((R374)(8)), that upper then taken from what is left. The dispatches used, from
data/b764_dispatch_rows.json, against the worklist's MAX_DISPATCHES.

  read c2    one reading after Component 2, with its controls; appended and banked
  control    the controls alone, printed; writes nothing
"""
import ast
import io
import json
import os
import sys
from datetime import datetime, timezone

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import figbank as FB   # noqa: E402
import dispatchrate as DR   # noqa: E402

NL = '\n'
ACT = 'b764'
PRICE_J = os.path.join(D, 'b764_price.json')
PRICE_B763 = os.path.join(D, 'b763_price.json')   # ### [K14]'s record instance: a flat 0.325 h a dispatch (data/b763_misses.txt (11))
ROWS = os.path.join(D, 'b764_dispatch_rows.json')
WORKLIST = os.path.join(T, 'b764_worklist.py')
BANK_T = os.path.join(D, 'b764_ceiling.txt')
BANK_J = os.path.join(D, 'b764_ceiling.json')
DELIVERY = '2026-11-20T16:52:08Z'   # ### the delivery, one part (transcript line 213526, 16:52:08.852Z), to the second
CEILING = 24.0
POINTS = ('c2',)
# ### the summed rows that remain after Component 2, by the price bank's keys: (7)'s trial but its route (tools/standing/commit.py's
# ### change, made in Component 2), the orders of (8), (9) and the close
TRIAL_7 = ('(7) workflow', '(7) reference+save', '(7) restore', '(7) main')
REMAIN = {'c2': TRIAL_7}
TAIL = ('(9)(a)', '(9)(b)', '(9)(c)', '(9)(d)', 'close')
CARRY_9B = '(9)(b)'
# ### the rows whose dispatches run together, each with its row's words: (lo, hi) waits
WAITS = {'(7) reference+save': (1, 1)}
WAITS_WHY = {'(7) reference+save': 'data/b764_price.txt :38, "TWO DISPATCHES of the branch tip sent together ... the waits of both read as one"'}


def _t(s):
    return datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)


def _now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def price(path=PRICE_J, given=None, waits=WAITS):
    """(the json, {key: row} with each dispatching row read at its kind, the (8) keys in table order, the rate's lines, ok)."""
    j = json.load(io.open(path, encoding='utf-8'))
    rows, L, ok = DR.rows_at_kind(j, given, waits)
    return j, dict((r['key'], r) for r in rows), [r['key'] for r in rows if r['key'].startswith('(8)')], L, ok


def cap():
    for n in ast.parse(io.open(WORKLIST, encoding='utf-8').read()).body:
        if isinstance(n, ast.Assign) and any(getattr(x, 'id', '') == 'MAX_DISPATCHES' for x in n.targets):
            return ast.literal_eval(n.value)
    sys.exit('### MAX_DISPATCHES NOT FOUND IN tools/b764_worklist.py -- NOTHING READ')


def used():
    R = json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []
    return sum(1 for r in R if r.get('kind') == 'dispatch'), os.path.exists(ROWS)


def units(remain, k8):
    """(R374)(3)'s order over the ceiling, among the rows that remain: each order of (8), the last priced first; then (7)'s trial whole;
    then (9)(b). (6) and the keys of (5) are Component 2's and remain at no reading of this tool."""
    out = [(k,) for k in reversed(k8) if k in remain]
    t7 = tuple(k for k in TRIAL_7 if k in remain)
    return out + ([t7] if t7 else []) + ([(CARRY_9B,)] if CARRY_9B in remain else [])


def carry(spent, remain, rows, k8):
    """(the total at the lower figures, the carried keys in order, the total after them)."""
    total = spent + sum(rows[k]['lo_h'] for k in remain)
    run, out = total, []
    for u in units(remain, k8):
        if run <= CEILING:
            break
        out += list(u)
        run -= sum(rows[k]['lo_h'] for k in u)
    return total, out, run


def plan8(left, rows, k8, carried=()):
    """(8) in ascending order of upper hours: each built where what is left holds its upper figure, the upper then taken from it; an order
    the carry took named carried."""
    out = []
    for k in sorted(k8, key=lambda k: rows[k]['hi_h']):
        hi = rows[k]['hi_h']
        if k in carried:
            out.append((k, 'CARRIED BY THE CEILING', hi, left))
        elif hi <= left:
            out.append((k, 'BUILT WHERE IT FITS', hi, left))
            left -= hi
        else:
            out.append((k, 'CARRIED BY NAME', hi, left))
    return out


def left_for_8(spent, remain, rows, carried):
    return CEILING - (spent + sum(rows[k]['lo_h'] for k in remain if not k.startswith('(8)') and k not in carried))


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    j, rows, k8, rl, rok = price()
    summed = [k for k, r in rows.items() if r['summed']]
    bound = 0.005 * (len(summed) + 1)
    sp = (_t(j['at']) - _t(DELIVERY)).total_seconds() / 3600.0
    c('the delivery reproduces the price bank`s spent_h at its own time (%s)' % j['at'], ('%.4f' % sp, j['spent_h']), abs(sp - j['spent_h']) <= 0.005)
    tot, car, run = carry(j['spent_h'], summed, rows, k8)
    c('the step-zero sum from the json`s rows read at their kind against the bank`s, within the rounding of %d rows and the spent figure (%.3f h)' % (
        len(summed), bound), ('%.2f' % tot, j['lower_sum_h']), abs(tot - j['lower_sum_h']) <= bound)
    c('the step-zero carry against the bank`s carried list and its sum after', (car, '%.2f' % run, j['after_carry_h']),
      car == j['carried'] and abs(run - j['after_carry_h']) <= bound)
    # ### [K14]: the rate by the kind of build
    o4, _l4, k4 = DR.read(json.load(io.open(PRICE_B763, encoding='utf-8')), (j['whole_min'][0], j['whole_min'][1], j['closure_min']))
    st = o4.get('(7) statements') or {}
    c('THE RATE, the record instance: b763`s table (a flat 0.325 h a dispatch) read at the kinds b764`s table names: every dispatching row BELOW '
      'ITS KIND, (7)`s statement (priced 0.33 h, a dispatch that built the kernel whole) read at a whole build',
      (len(o4), sum(1 for x in o4.values() if x['below']), st.get('priced'), st.get('read')),
      k4 and len(o4) == 15 and all(x['below'] for x in o4.values()) and (st.get('read') or [0])[0] >= j['whole_min'][0] / 60.0 - 0.005)
    o5, _l5, _k5 = DR.read(j, None, WAITS)
    o5n, _l5n, _k5n = DR.read(j, None, None)
    c('THE RATE over b764`s table: each dispatching row AT ITS KIND with the waits of WAITS (%s); without them the reference and the saving run, '
      'sent together, read BELOW, the waits read' % '; '.join(WAITS_WHY.values()),
      ([(k, x['verdict']) for k, x in sorted(o5.items())], o5n.get('(7) reference+save', {}).get('verdict')),
      len(o5) == 2 and not any(x['below'] for x in o5.values()) and o5n.get('(7) reference+save', {}).get('below') is True)
    pr = DR.read_row(dict(key='planted', dispatches=[1, 1], lo_h=0.33, hi_h=0.33), DR.timings(j)[0])
    c('planted: a dispatching row that names no kind is read as a whole build', (pr['kind'], pr['kind_from'], pr['read']),
      pr['kind'] == 'whole' and pr['below'] and pr['read'][0] >= j['whole_min'][0] / 60.0 - 0.005)
    _o7, _l7, k7 = DR.read(dict(rows=[dict(key='planted', dispatches=[1, 1], lo_h=0.33, hi_h=0.33)], h_per_dispatch=0.325))
    c('planted: a table naming no build`s minutes, none passed, is refused', k7, k7 is False)
    rem2 = list(REMAIN['c2']) + k8 + list(TAIL)
    s0 = CEILING - sum(rows[k]['lo_h'] for k in rem2)
    _t0, c_at, _r0 = carry(s0, rem2, rows, k8)
    _t1, c_ov1, _r1 = carry(s0 + 0.01, rem2, rows, k8)
    _t2, c_ov, _r2 = carry(CEILING, rem2, rows, k8)
    c('planted at c2: the sum exactly at 24 h carries nothing; 0.01 h over carries the last priced order of (8) alone; spent 24 h carries every '
      'order of (8), the last priced first, then (7)`s trial whole, then (9)(b)', (c_at, c_ov1, c_ov),
      c_at == [] and c_ov1 == [k8[-1]] and c_ov == list(reversed(k8)) + list(TRIAL_7) + [CARRY_9B])
    p = plan8(1.0, rows, k8)
    c('planted with 1 h left for (8): ascending upper order, each built where its upper fits, its upper then taken',
      [(k[4:], w) for k, w, _h, _l in p], [k for k, _w, _h, _l in p] == sorted(k8, key=lambda k: rows[k]['hi_h'])
      and [w for _k, w, _h, _l in p][:3] == ['BUILT WHERE IT FITS', 'BUILT WHERE IT FITS', 'CARRIED BY NAME'])
    want = list(TRIAL_7) + list(TAIL)
    c('the price bank`s rows for each key this tool reads, five orders of (8) among them', ([k for k in want if k not in rows], len(k8)),
      all(k in rows for k in want) and len(k8) == 5)
    return L, ok, rl


def render(readings, L):
    out = ['%s -- (R374)(3): THE CEILING, 24 HOURS AGAINST THE PRICE TABLE`S LOWER FIGURES, READ AFTER COMPONENT 2 (tools/b764_ceiling.py; the '
           'step-zero reading in data/b764_price.txt)' % ACT, '', '## THE CONTROLS'] + L + ['']
    for r in readings:
        out += ['## THE READING AFTER COMPONENT 2, AT %s' % r['at']] + r['lines'] + ['']
    last = readings[-1]
    out.append('### ### **THE CEILING: READINGS %d ; THE LAST AFTER COMPONENT 2 AT %s, %.2f h AT THE LOWER FIGURES AGAINST 24 h, %s ; %s ; DISPATCHES %d OF %s.**' % (
        len(readings), last['at'], last['total_h'], 'CARRIED ' + ', '.join(last['carried']) if last['carried'] else 'NOTHING CARRIED', last['verdict'],
        last['used'], last['cap']))
    return NL.join(out)


def cmd_read(point):
    L, ok, rl = controls()
    if not all(ok):
        print(NL.join(L))
        sys.exit('### THE CONTROLS NOT AS WANTED -- NOTHING WRITTEN')
    held = json.load(io.open(BANK_J, encoding='utf-8'))['readings'] if os.path.exists(BANK_J) else []
    if any(r['point'] == point for r in held):
        sys.exit('### A READING AFTER %s IS HELD (data/b764_ceiling.json) -- NOTHING WRITTEN' % point)
    j, rows, k8, rl, rok = price()
    if not rok:
        print(NL.join(rl))
        sys.exit('### THE RATE REFUSED -- NOTHING WRITTEN')
    now = _now()
    spent = (_t(now) - _t(DELIVERY)).total_seconds() / 3600.0
    remain = [k for k in list(REMAIN[point]) + k8 + list(TAIL) if rows[k]['summed']]
    total, car, run = carry(spent, remain, rows, k8)
    n_used, have_rows = used()
    cp = cap()
    lines = list(rl) + ['  SPENT from the delivery (%s, transcript line 213526) to this read: %.2f h' % (DELIVERY, spent)]
    for k in remain:
        lines.append('  REMAINING %-32s lower %.2f h (upper %.2f h)' % (k, rows[k]['lo_h'], rows[k]['hi_h']))
    lines.append('  THE SUM AT THE LOWER FIGURES: %.2f h against %.0f h -> %s' % (
        total, CEILING, 'NOTHING CARRIED' if not car else 'OVER: CARRIED IN (R374)(3)`S ORDER, ' + ', '.join(
            '%s (%.2f-%.2f h)' % (k, rows[k]['lo_h'], rows[k]['hi_h']) for k in car) + '; %.2f h after' % run))
    left = left_for_8(spent, remain, rows, car)
    p = plan8(left, rows, k8, car)
    lines.append('  WHAT THE CEILING LEAVES FOR (8), every other remaining row not carried at its lower figure: %.2f h' % left)
    for k, w, hi, lf in p:
        lines.append('  (8) %-30s upper %.2f h against %.2f h left -> %s' % (k[4:], hi, lf, w))
    verdict = 'BUILT WHERE IT FITS: ' + (', '.join(k[4:] for k, w, _h, _l in p if w == 'BUILT WHERE IT FITS') or 'none') + (
        ' ; (7) %s' % ('CARRIED' if TRIAL_7[0] in car else 'TRIED WHERE THE CEILING LEAVES IT'))
    lines.append('  THE DISPATCHES (data/b764_dispatch_rows.json%s): used %d against the worklist`s MAX_DISPATCHES %s' % (
        '' if have_rows else ', absent: none sent', n_used, cp))
    rec = dict(point=point, at=now, spent_h=round(spent, 2), total_h=round(total, 2), carried=car, after_carry_h=round(run, 2), used=n_used, cap=cp,
               dispatch_rows=have_rows, left_for_8_h=round(left, 2), plan=[dict(key=k, word=w, hi_h=hi, left_h=round(lf, 2)) for k, w, hi, lf in p],
               verdict=verdict, lines=lines)
    held.append(rec)
    text = render(held, L)
    FB.write(BANK_T, text)
    r = FB.write(BANK_J, json.dumps(dict(readings=held), indent=1))
    print(text)
    print('written data/b764_ceiling.txt, data/b764_ceiling.json ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        L, ok, rl = controls()
        print(NL.join(rl + [''] + L))
        print('### CONTROLS %d OF %d AS WANTED' % (sum(ok), len(ok)))
    elif a[:1] == ['read'] and len(a) == 2 and a[1] in POINTS:
        cmd_read(a[1])
    else:
        sys.exit(__doc__)
