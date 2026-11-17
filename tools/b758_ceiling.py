# -*- coding: utf-8 -*-
"""tools/b758_ceiling.py -- (R368)(2): THE CEILING, READ AGAINST THE CLOCK. "THE CEILING: 16 hours, this act being smaller than b757; over it,
carried in this order: (7), then (6)(ii)" (data/b758_ferry.txt :11); step zero: "16 hours from the delivery, 2026-11-16T23:21:58Z, to
2026-11-17T15:21:58Z. ... Read again after Component 3 and before Component 5" (data/b758_stepzero.txt :88-:89). Written whole by the Write tool
at b758's Component 5, committed before it runs; its one write data/b758_ceiling.txt, each reading appended to the readings the bank holds and
the bank written whole.

  read "<when>"   one reading: the hours since the delivery against 16, the hours left, the carry it orders (NOTHING CARRIED within the
                  ceiling; (7) THEN (6)(ii) CARRIED over it), the dispatches used of 4 by the dispatch rows; appended and banked
  control         the tool's controls, printed
"""
import io
import json
import os
import re
import sys
import time
from datetime import datetime, timezone

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import figbank as FB   # noqa: E402

NL = '\n'
ACT = 'b758'
DELIVERY = '2026-11-16T23:21:58Z'
CEILING_H = 16
CAP = 4
BANK = os.path.join(D, 'b758_ceiling.txt')
ROWS = os.path.join(D, 'b758_dispatch_rows.json')
ROW = re.compile(r'^  reading (\d+) at (\S+) \((.*)\): ([\d.]+) h of (\d+), ([\d.-]+) h left ; (NOTHING CARRIED|\(7\) THEN \(6\)\(ii\) CARRIED) ; dispatches (\d+) of (\d+)$')


def _t(s):
    return datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)


def reading(now, when, used):
    h = (_t(now) - _t(DELIVERY)).total_seconds() / 3600.0
    word = 'NOTHING CARRIED' if h <= CEILING_H else '(7) THEN (6)(ii) CARRIED'
    return h, word, '(%s): %.2f h of %d, %.2f h left ; %s ; dispatches %d of %d' % (when, h, CEILING_H, CEILING_H - h, word, used, CAP)


def rows_held():
    t = io.open(BANK, encoding='utf-8').read().replace('\r', '') if os.path.exists(BANK) else ''
    return [l for l in t.split(NL) if ROW.match(l)]


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    a = reading('2026-11-17T15:21:58Z', 'planted at the ceiling', 2)
    b = reading('2026-11-17T15:21:59Z', 'planted one second over', 2)
    c('a planted reading at the ceiling carries nothing; one second over carries (7) then (6)(ii)', (a[1], b[1]),
      a[1] == 'NOTHING CARRIED' and b[1] == '(7) THEN (6)(ii) CARRIED')
    r = '  reading 1 at 2026-11-17T02:40:00Z %s' % reading('2026-11-17T02:40:00Z', 'planted', 1)[2]
    c('a planted row read back by the bank`s own pattern', bool(ROW.match(r)), bool(ROW.match(r)))
    s = io.open(os.path.join(D, 'b758_stepzero.txt'), encoding='utf-8').read()
    c('the delivery and the ceiling as step zero banks them', (DELIVERY, CEILING_H),
      '16 hours from the delivery, 2026-11-16T23:21:58Z, to' in s and '2026-11-17T15:21:58Z' in s)
    return L, ok


def cmd_read(when):
    L, ok = controls()
    if not all(ok) or not when.strip() or ')' in when or '(' in when:
        print(NL.join(L))
        sys.exit('### THE CONTROLS NOT AS WANTED, OR THE READING`S NAME EMPTY OR CARRYING A PARENTHESIS -- nothing written')
    now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    R = json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []
    used = sum(1 for r in R if r.get('kind') == 'dispatch')
    held = rows_held()
    h, word, txt = reading(now, when, used)
    held.append('  reading %d at %s %s' % (len(held) + 1, now, txt))
    out = ['%s -- (R368)(2): THE CEILING, READ AGAINST THE CLOCK, FROM THE DELIVERY %s, %d HOURS (tools/b758_ceiling.py)' % (ACT, DELIVERY, CEILING_H),
           '', '## THE CONTROLS'] + L + ['', '## THE READINGS, EACH APPENDED WHEN TAKEN'] + held + [
           '', '### ### **THE CEILING: READINGS %d ; THE LAST AT %s, %.2f h OF %d ; %s ; DISPATCHES %d OF %d.**' % (len(held), now, h, CEILING_H, word, used, CAP)]
    r = FB.write(BANK, NL.join(out))
    print(NL.join(out))
    print('written data/b758_ceiling.txt ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        print(NL.join(controls()[0]))
    elif a[:1] == ['read'] and len(a) == 2:
        cmd_read(a[1])
    else:
        sys.exit(__doc__)
