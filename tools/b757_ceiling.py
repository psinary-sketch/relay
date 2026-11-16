# -*- coding: utf-8 -*-
"""b757 -- (R367)(2): THE CEILING READ AGAIN AFTER COMPONENT 3.

Reads the price bank (data/b757_price.txt, written at step zero), the act's dispatch rows (data/b757_dispatch_rows.json) and the clock,
and prints: the hours spent from the ruling's delivery (transcript line 87853, 2026-11-16T04:32:48Z, the price bank :12) to the read;
the items of the table not yet done, at their lower figures, (7) at the navigator's figure and at the seat's beside it; the sum against
the ceiling of 24 hours, and what it carries in (R367)(2)'s order where it goes over -- (7); then the statement that rides with (6); then
(8)(iii); the dispatches used in each kernel against (R367)(10)'s caps, and what that leaves the wide direction. Every figure is read from
those banks or computed here. With --bank it writes data/b757_ceiling.txt and data/b757_ceiling.json; without, it prints alone.

usage: python -X utf8 -u tools/b757_ceiling.py [--bank]
"""
import datetime
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRICE = os.path.join(ROOT, 'data', 'b757_price.txt')
ROWS = os.path.join(ROOT, 'data', 'b757_dispatch_rows.json')
OUT_T = os.path.join(ROOT, 'data', 'b757_ceiling.txt')
OUT_J = os.path.join(ROOT, 'data', 'b757_ceiling.json')
DELIVERY = datetime.datetime(2026, 11, 16, 4, 32, 48, tzinfo=datetime.timezone.utc)
CEILING = 24.0
CAPS = {'SIDE-explicit-formula': 14, 'SIDE-dirichlet-mod-24': 4}
ROW = re.compile(r'^  (\(\d\)(?:\([ivx]+\))?|close)\s+(\S+)?.*\| dispatches [^|]+\| (\d+\.\d+)-(\d+\.\d+) h')
# the items the table prices that remain after Components 3 and 4 (the price bank's own keys): (7), (8)(i)-(v), (9), the close
REMAIN = ('(7) navigator', '(8)(i) the', '(8)(ii) the', '(8)(iii) N5`s', '(8)(iv) REGISTRY', '(8)(v) tools/b757_doors.py', '(9) the',
          'close Component')
SEAT7 = '(7) the'


def price_rows():
    rows = {}
    for i, l in enumerate(io.open(PRICE, encoding='utf-8').read().split('\n'), 1):
        m = ROW.match(l)
        if m:
            rows[(m.group(1) + ' ' + (m.group(2) or '')).strip()] = (i, float(m.group(3)), float(m.group(4)))
    return rows


def main(argv):
    bank = '--bank' in argv
    now = datetime.datetime.now(datetime.timezone.utc)
    rows = price_rows()
    missing = [k for k in REMAIN + (SEAT7,) if k not in rows]
    out = ['b757 -- (R367)(2): THE CEILING READ AGAIN AFTER COMPONENT 3 (%s, tools/b757_ceiling.py)' % now.strftime('%Y-%m-%dT%H:%M:%SZ'), '']
    if missing:
        out.append('### PRICE ROWS NOT FOUND: %s -- NOTHING READ' % missing)
        print('\n'.join(out))
        return 2
    R = json.load(io.open(ROWS, encoding='utf-8'))
    disp = [r for r in R if r.get('kind') == 'dispatch']
    reads = dict((int(r['run']), r) for r in R if r.get('kind') == 'read')
    used = dict((k, len([d for d in disp if d.get('kernel') == k])) for k in CAPS)
    t1 = [d for d in disp if d.get('item') == 'T1']
    t1_done = any(reads.get(int(d['run']), {}).get('build_exit') == '0' for d in t1)
    spent = (now - DELIVERY).total_seconds() / 3600.0
    rem = sum(rows[k][1] for k in REMAIN)
    t1_rest = 0.0 if t1_done else rows['(5) T1'][1] if '(5) T1' in rows else 0.0
    total = spent + rem + t1_rest
    seat = total - rows['(7) navigator'][1] + rows[SEAT7][1]
    left7 = CEILING - (spent + t1_rest + rem - rows['(7) navigator'][1])
    out.append('## THE READ')
    out.append('  SPENT from the ruling`s delivery (%s, transcript line 87853; data/b757_price.txt :12) to this read: %.2f h' % (
        DELIVERY.strftime('%Y-%m-%dT%H:%M:%SZ'), spent))
    out.append('  T1: %s (its dispatches %s)%s' % ('COMPILED, a read row with the exit file 0' if t1_done else 'NOT YET COMPILED',
                                                 ', '.join('%d run %s exit %s' % (d['n'], d['run'], reads.get(int(d['run']), {}).get('build_exit', 'NOT READ')) for d in t1),
                                                 '' if t1_done else '; its lower figure %.2f h counted as remaining' % t1_rest))
    for k in REMAIN:
        out.append('  REMAINING %-28s the price bank :%-3d lower %.2f h (upper %.2f h)' % (k, rows[k][0], rows[k][1], rows[k][2]))
    out.append('  THE SUM AT THE LOWER FIGURES: spent %.2f + T1 %.2f + remaining %.2f = %.2f h against the ceiling %.0f h -> %s' % (
        spent, t1_rest, rem, total, CEILING, 'NOTHING CARRIED' if total <= CEILING else 'OVER: CARRIED IN (R367)(2)`S ORDER -- (7), THEN THE STATEMENT THAT RIDES WITH (6), THEN (8)(iii)'))
    out.append('  THE OTHER READING, (7) at the seat`s lower figure (the price bank :%d, %.2f h for the navigator`s %.2f h): %.2f h -> %s' % (
        rows[SEAT7][0], rows[SEAT7][1], rows['(7) navigator'][1], seat, 'NOTHING CARRIED' if seat <= CEILING else 'OVER'))
    out.append('  WHAT REMAINS OF THE CEILING FOR (7), the other remaining items at their lower figures: %.2f h against (7)`s lower %.2f h '
               '(the navigator`s) or %.2f h (the seat`s)' % (left7, rows['(7) navigator'][1], rows[SEAT7][1]))
    out.append('')
    out.append('## THE DISPATCHES AGAINST (R367)(10)`S CAPS (data/b757_dispatch_rows.json)')
    for k, c in CAPS.items():
        out.append('  %s: used %d of %d ; left %d' % (k, used[k], c, c - used[k]))
    out.append('  THE WIDE DIRECTION`S PRICE: 4-8 dispatches (the navigator`s), 5-10 (the seat`s); left to it in SIDE-explicit-formula: %d' % (
        CAPS['SIDE-explicit-formula'] - used['SIDE-explicit-formula']))
    out.append('')
    verdict = 'NOTHING CARRIED' if total <= CEILING else 'CARRIED'
    out.append('### ### **THE CEILING AFTER COMPONENT 3: %.2f h AT THE LOWER FIGURES AGAINST 24 h, %s ; (7) LEFT %.2f h ; DISPATCHES %d OF 14 AND %d OF 4 USED.**' % (
        total, verdict, left7, used['SIDE-explicit-formula'], used['SIDE-dirichlet-mod-24']))
    text = '\n'.join(out) + '\n'
    print(text)
    if bank:
        io.open(OUT_T, 'w', encoding='utf-8', newline='\n').write(text)
        rec = dict(at=now.strftime('%Y-%m-%dT%H:%M:%SZ'), spent_h=round(spent, 2), t1_done=t1_done, t1_rest_h=t1_rest, remaining_h=round(rem, 2),
                   total_h=round(total, 2), seat_total_h=round(seat, 2), ceiling_h=CEILING, verdict=verdict, left_for_7_h=round(left7, 2),
                   used=used, caps=CAPS)
        io.open(OUT_J, 'w', encoding='utf-8', newline='\n').write(json.dumps(rec, indent=1) + '\n')
        print('BANKED: data/b757_ceiling.txt, data/b757_ceiling.json')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
