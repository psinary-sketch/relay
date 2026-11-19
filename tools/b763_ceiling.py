# -*- coding: utf-8 -*-
"""tools/b763_ceiling.py -- (R373)(3): THE CEILING, 24 HOURS AGAINST THE PRICE TABLE'S LOWER FIGURES, READ AFTER COMPONENT 2 AND AFTER
COMPONENT 3 (the step-zero reading stands in data/b763_price.txt). "THE CEILING: 24 hours against the table's lower figures, read at step
zero, after Component 2 and after Component 3; over it, carried by name in this order, each with its price: the items of (8), last priced
leaving soonest; then the proof of (7), its statement staying committed; then statements (S4) and (S5) of (6)" (data/b763_ferry.txt :13).
Carried from tools/b757_ceiling.py (its price-based form: the price bank, the dispatch rows and the clock) by the Write tool at b763's
Component 1 and committed before it runs. Its writes: data/b763_ceiling.txt and data/b763_ceiling.json, each reading appended to the
readings the json holds and the text rendered whole from it; a second reading at a point the json holds is refused, nothing written.

THE READING: the hours spent from the delivery (transcript line 191165, 2026-11-19T18:35:12Z; data/b763_price.json spent_h) to the read;
the table's summed rows that remain at the point, at their lower figures; the sum against 24 h, and what it carries in (R373)(3)'s order
where it goes over. After Component 2: what the ceiling leaves for (7)'s proof, every other remaining summed row but (8) at its lower
figure, and the form it decides by (7): FORM B where its upper fits, else FORM A where its upper fits, else no proof ([X2]). After
Component 3: (8) in ascending order of upper hours, each built where what is left holds its upper figure, the upper then taken from what is
left; the two orders (12) bars (data/b763_misses.txt (4)) named as barred whatever the ceiling leaves. The dispatches used, from
data/b763_dispatch_rows.json, against the worklist's MAX_DISPATCHES.

  read <c2|c3>   one reading at that point, with its controls; appended and banked
  control        the controls alone, printed; writes nothing
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

NL = '\n'
ACT = 'b763'
PRICE_J = os.path.join(D, 'b763_price.json')
ROWS = os.path.join(D, 'b763_dispatch_rows.json')
WORKLIST = os.path.join(T, 'b763_worklist.py')
BANK_T = os.path.join(D, 'b763_ceiling.txt')
BANK_J = os.path.join(D, 'b763_ceiling.json')
DELIVERY = '2026-11-19T18:35:12Z'   # ### the delivery, one part (transcript line 191165, 18:35:12.961Z), to the second
CEILING = 24.0
POINTS = ('c2', 'c3')
# ### the summed rows that remain at each point, by the price bank's keys: after Component 2, (7)'s statements and proof, (8), (9) and the
# ### close; after Component 3, (8), (9) and the close
REMAIN = {'c2': ('(7) statements', '(7) B'), 'c3': ()}
TAIL = ('(9)', 'close')
PROOF_B, PROOF_A = '(7) B', '(7) A'
BARRED_12 = ('(8) BESSEL-BOUND-TIGHTEN', '(8) E2-SEPARATION')   # ### data/b763_misses.txt (4): each computes at zeros, which (12) forbids


def _t(s):
    return datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)


def _now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def price():
    j = json.load(io.open(PRICE_J, encoding='utf-8'))
    rows = dict((r['key'], r) for r in j['rows'])
    k8 = [r['key'] for r in j['rows'] if r['key'].startswith('(8)')]
    return j, rows, k8


def cap():
    for n in ast.parse(io.open(WORKLIST, encoding='utf-8').read()).body:
        if isinstance(n, ast.Assign) and any(getattr(x, 'id', '') == 'MAX_DISPATCHES' for x in n.targets):
            return ast.literal_eval(n.value)
    sys.exit('### MAX_DISPATCHES NOT FOUND IN tools/b763_worklist.py -- NOTHING READ')


def used():
    R = json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []
    return sum(1 for r in R if r.get('kind') == 'dispatch'), os.path.exists(ROWS)


def carry(spent, remain, rows, k8, proof_in):
    """(R373)(3)'s order over the ceiling: the (8) rows that remain, the last priced first; then (7)'s proof where it remains. Returns the
    total at the lower figures, the carried keys in order, and the total after them."""
    total = spent + sum(rows[k]['lo_h'] for k in remain)
    run, out = total, []
    for k in [k for k in reversed(k8) if k in remain] + ([PROOF_B] if proof_in and PROOF_B in remain else []):
        if run <= CEILING:
            break
        out.append(k)
        run -= rows[k]['lo_h']
    return total, out, run


def proof_left(spent, remain, rows):
    return CEILING - (spent + sum(rows[k]['lo_h'] for k in remain if k != PROOF_B and not k.startswith('(8)')))


def decide(left, rows):
    if rows[PROOF_B]['hi_h'] <= left:
        return 'FORM B'
    if rows[PROOF_A]['hi_h'] <= left:
        return 'FORM A'
    return 'NO PROOF SENT: [X2]'


def plan8(left, rows, k8):
    """(8) in ascending order of upper hours: each built where what is left holds its upper figure, the upper then taken from it; the two
    orders (12) bars named as barred."""
    out = []
    for k in sorted(k8, key=lambda k: rows[k]['hi_h']):
        hi = rows[k]['hi_h']
        if k in BARRED_12:
            out.append((k, 'BARRED BY (12)', hi, left))
        elif hi <= left:
            out.append((k, 'BUILT WHERE IT FITS', hi, left))
            left -= hi
        else:
            out.append((k, 'CARRIED BY NAME', hi, left))
    return out


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    j, rows, k8 = price()
    summed = [k for k, r in rows.items() if r['summed']]
    bound = 0.005 * (len(summed) + 1)
    sp = (_t(j['at']) - _t(DELIVERY)).total_seconds() / 3600.0
    c('the delivery reproduces the price bank`s spent_h at its own time (%s)' % j['at'], ('%.4f' % sp, j['spent_h']), abs(sp - j['spent_h']) <= 0.005)
    tot, car, run = carry(j['spent_h'], summed, rows, k8, True)
    c('the step-zero sum from the json`s rounded rows against the bank`s, within the rounding of %d rows and the spent figure (%.3f h)' % (len(summed), bound),
      ('%.2f' % tot, j['lower_sum_h']), abs(tot - j['lower_sum_h']) <= bound)
    c('the step-zero carry, the last priced first, against the bank`s carried list and its sum after', (car, '%.2f' % run, j['after_carry_h']),
      car == j['carried'] and abs(run - j['after_carry_h']) <= bound)
    pl = proof_left(j['spent_h'], summed, rows)
    c('what the step zero left for (7)`s proof against the bank`s, and the decision', ('%.2f' % pl, j['proof_left_h'], decide(pl, rows)),
      abs(pl - j['proof_left_h']) <= bound and decide(pl, rows).startswith('NO PROOF'))
    c('planted: FORM B where its upper fits, FORM A where only its own would (none can: its upper is above B`s), no proof below B`s upper',
      (decide(rows[PROOF_B]['hi_h'], rows), decide(rows[PROOF_A]['hi_h'], rows), decide(rows[PROOF_B]['hi_h'] - 0.01, rows)),
      decide(rows[PROOF_B]['hi_h'], rows) == 'FORM B' and decide(rows[PROOF_B]['hi_h'] - 0.01, rows).startswith('NO PROOF'))
    # ### b763 defect (e): the first form planted "spent 0 carries nothing", a plant that does not meet its premise (c2's remaining rows sum
    # ### to 26.95 h at their lower figures, over 24 h with nothing spent); planted now at the boundary, the remaining sum exactly at the ceiling
    rem2 = list(REMAIN['c2']) + k8 + list(TAIL)
    s0 = CEILING - sum(rows[k]['lo_h'] for k in rem2)
    _t0, c_at, _r0 = carry(s0, rem2, rows, k8, True)
    _t1, c_ov1, _r1 = carry(s0 + 0.01, rem2, rows, k8, True)
    _t2, c_ov, _r2 = carry(CEILING, rem2, rows, k8, True)
    c('planted at c2: the sum exactly at 24 h carries nothing; 0.01 h over carries the last priced alone; spent 24 h carries every (8) row, '
      'the last priced first, then (7)`s proof', (c_at, c_ov1, c_ov),
      c_at == [] and c_ov1 == [k8[-1]] and c_ov == list(reversed(k8)) + [PROOF_B])
    p = plan8(5.0, rows, k8)
    c('planted at c3 with 5 h left: (8) in ascending upper order, the barred two named barred whatever is left',
      [(k[4:], w) for k, w, _h, _l in p], [k for k, _w, _h, _l in p] == sorted(k8, key=lambda k: rows[k]['hi_h'])
      and all(w == 'BARRED BY (12)' for k, w, _h, _l in p if k in BARRED_12) and p[0][1] == 'BUILT WHERE IT FITS')
    c('the price bank`s rows for each key this tool reads', [k for k in REMAIN['c2'] + TAIL + (PROOF_A,) + BARRED_12 if k not in rows],
      all(k in rows for k in REMAIN['c2'] + TAIL + (PROOF_A,) + BARRED_12))
    return L, ok


def render(readings, L):
    out = ['%s -- (R373)(3): THE CEILING, 24 HOURS AGAINST THE PRICE TABLE`S LOWER FIGURES, READ AFTER COMPONENT 2 AND AFTER COMPONENT 3 '
           '(tools/b763_ceiling.py; the step-zero reading in data/b763_price.txt)' % ACT, '', '## THE CONTROLS'] + L + ['']
    for r in readings:
        out += ['## THE READING AFTER %s, AT %s' % ({'c2': 'COMPONENT 2', 'c3': 'COMPONENT 3'}[r['point']], r['at'])] + r['lines'] + ['']
    last = readings[-1]
    out.append('### ### **THE CEILING: READINGS %d ; THE LAST AFTER %s AT %s, %.2f h AT THE LOWER FIGURES AGAINST 24 h, %s ; %s ; DISPATCHES %d OF %s.**' % (
        len(readings), {'c2': 'COMPONENT 2', 'c3': 'COMPONENT 3'}[last['point']], last['at'], last['total_h'],
        'CARRIED ' + ', '.join(last['carried']) if last['carried'] else 'NOTHING CARRIED', last['verdict'], last['used'], last['cap']))
    return NL.join(out)


def cmd_read(point):
    L, ok = controls()
    if not all(ok):
        print(NL.join(L))
        sys.exit('### THE CONTROLS NOT AS WANTED -- NOTHING WRITTEN')
    held = json.load(io.open(BANK_J, encoding='utf-8'))['readings'] if os.path.exists(BANK_J) else []
    if any(r['point'] == point for r in held):
        sys.exit('### A READING AFTER %s IS HELD (data/b763_ceiling.json) -- NOTHING WRITTEN' % point)
    j, rows, k8 = price()
    now = _now()
    spent = (_t(now) - _t(DELIVERY)).total_seconds() / 3600.0
    remain = [k for k in list(REMAIN[point]) + k8 + list(TAIL) if rows[k]['summed']]
    total, car, run = carry(spent, remain, rows, k8, point == 'c2')
    n_used, have_rows = used()
    cp = cap()
    lines = ['  SPENT from the delivery (%s, transcript line 191165) to this read: %.2f h' % (DELIVERY, spent)]
    for k in remain:
        lines.append('  REMAINING %-28s lower %.2f h (upper %.2f h)' % (k, rows[k]['lo_h'], rows[k]['hi_h']))
    lines.append('  THE SUM AT THE LOWER FIGURES: %.2f h against %.0f h -> %s' % (
        total, CEILING, 'NOTHING CARRIED' if not car else 'OVER: CARRIED IN (R373)(3)`S ORDER, ' + ', '.join(
            '%s (%.2f-%.2f h)' % (k, rows[k]['lo_h'], rows[k]['hi_h']) for k in car) + '; %.2f h after' % run))
    rec = dict(point=point, at=now, spent_h=round(spent, 2), total_h=round(total, 2), carried=car, after_carry_h=round(run, 2), used=n_used,
               cap=cp, dispatch_rows=have_rows)
    if point == 'c2':
        left = proof_left(spent, remain, rows)
        verdict = decide(left, rows) if PROOF_B not in car else 'NO PROOF SENT: [X2], THE PROOF CARRIED'
        lines.append('  WHAT THE CEILING LEAVES FOR (7)`S PROOF, every other remaining summed row but (8) at its lower figure: %.2f h ; FORM B`s '
                     'upper %.2f h %s ; FORM A`s upper %.2f h %s -> %s' % (
                         left, rows[PROOF_B]['hi_h'], 'FITS' if rows[PROOF_B]['hi_h'] <= left else 'DOES NOT FIT', rows[PROOF_A]['hi_h'],
                         'FITS' if rows[PROOF_A]['hi_h'] <= left else 'DOES NOT FIT', verdict))
        rec.update(proof_left_h=round(left, 2), verdict=verdict)
    else:
        left = CEILING - (spent + sum(rows[k]['lo_h'] for k in TAIL))
        p = plan8(left, rows, k8)
        lines.append('  WHAT THE CEILING LEAVES FOR (8), (9) and the close at their lower figures: %.2f h' % left)
        for k, w, hi, lf in p:
            lines.append('  (8) %-24s upper %.2f h against %.2f h left -> %s' % (k[4:], hi, lf, w))
        verdict = 'BUILT WHERE IT FITS: ' + (', '.join(k[4:] for k, w, _h, _l in p if w == 'BUILT WHERE IT FITS') or 'none')
        rec.update(left_for_8_h=round(left, 2), plan=[dict(key=k, word=w, hi_h=hi, left_h=round(lf, 2)) for k, w, hi, lf in p], verdict=verdict)
    lines.append('  THE DISPATCHES (data/b763_dispatch_rows.json%s): used %d against the worklist`s MAX_DISPATCHES %s' % (
        '' if have_rows else ', absent: none sent', n_used, cp))
    rec['lines'] = lines
    held.append(rec)
    text = render(held, L)
    FB.write(BANK_T, text)
    r = FB.write(BANK_J, json.dumps(dict(readings=held), indent=1))
    print(text)
    print('written data/b763_ceiling.txt, data/b763_ceiling.json ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        L, ok = controls()
        print(NL.join(L))
        print('### CONTROLS %d OF %d AS WANTED' % (sum(ok), len(ok)))
    elif a[:1] == ['read'] and len(a) == 2 and a[1] in POINTS:
        cmd_read(a[1])
    else:
        sys.exit(__doc__)
