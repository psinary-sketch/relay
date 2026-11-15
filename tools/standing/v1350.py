# -*- coding: utf-8 -*-
"""standing/v1350.py -- THE CONTROLS OF v1.35.0, (R366)(6)[U2]: THE LEDGERS CARRY FINDINGS (relay data/b754_rules.txt (11)), in force from
b757, in v1348.py's form. BEFORE is the record and the suite as BASE left them (relay be3fc2b3, v1.34.9's own commit): the trail's Defects
line every row's head, its sealed tools and open orders by name, the corrigendum's entry the act's own c1 route alone. AFTER is
tools/standing/ledgers.py, the wrapper at record.tpl's foot, the record's dry check and the suite's two trail arms reading the line through
it, and orders.py's roll reader. THE COMPILE CONTROL RUNS FIRST; the free memory is printed before each control. Nothing is written but this
bank; no ledger is read but PLACE-papers OPEN_TRAILS through git at HEAD for the roll reader, and no line of it is printed. Written at b756 by
the Write tool; no identifier of the author is read into any string here.

  (trail)    over a composed trail carrying b756's own defect rows (relay data/b756_defects.txt), four sealed tools and three open orders:
             at b756 the text unchanged; read as if b756 were in force, the three lines by count, their counts the rows', every other line
             (the Next in full among them) unchanged, the rows they leave held for the trail bank, the backticks paired.
  (readers)  the one reading of the Defects line: before b757 the heads joined and KIND's owner count, as the dry check and the two arms read
             them at BASE; from b757 the counts printed, a planted miscount read as a mismatch; the record's dry check and the suite's two
             arms reading through it; every line-keyed region of the two templates the same length as at BASE.
  (orders)   orders.py's last roll line: at PLACE-papers HEAD the same line as BASE reads; a planted roll line by count read past.
  (entry)    the corrigendum's entry composed from b755's banks: its counts by bank equal to b756's landed corrigendum (relay
             data/b756_corrigendum.json), its head line first, the CLAIM items none, the repairs with their controls, the CLOSE items by count.
  (version)  tools/standing/VERSION moved to v1.35.0.

  python -X utf8 -u tools/standing/v1350.py control [trail|readers|orders|entry|version ...] [--bank]
"""
import io
import json
import os
import re
import sys
import time
import types

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = 'be3fc2b3'   # ### v1.34.9's own commit (b756 component 5): the record and the suite before this change
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)
import act_close as AC          # noqa: E402
from standing import ledgers as LDG   # noqa: E402
from standing import orders as ORD    # noqa: E402

KIND0 = re.compile(r"\(([a-z])\) THE (NAVIGATOR|SEAT)[’']S")   # ### b703_checks.py :989, the suite's KIND at BASE


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.9): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.35.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def both(L, cls, what, at_base, on_disk, holds_base, holds_disk):
    ok = bool(holds_base) and bool(holds_disk)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.9): %s -> (alike at both is wanted)' % at_base,
          '      AFTER  (v1.35.0): %s -> %s' % (on_disk, 'PASSES' if ok else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


class _Forced(object):
    def __enter__(self):
        self.was = LDG.FROM_ACT
        LDG.FROM_ACT = 756
        return self

    def __exit__(self, *a):
        LDG.FROM_ACT = self.was


def heads():
    """b756's defect rows as heads, `(x) THE <OWNER>'S [TAG ; ...]: ...`, the form the trail's letters carry."""
    return [r[4][:160] for r in LDG.bank_rows(os.path.join(D, 'b756_defects.txt'))]


def composed(rows):
    return NL.join(['', '### b757 — a composed trail for the control', '',
                    '**The orders by the tool:** 3 of 40 open.', '',
                    LDG.ROLL + ' `W-ORD-STORMER-CLASH`; `W-ORD-B518-FLOAT`; `W-ORD-ROOT-BINARY-BANK`.', '',
                    '**The sealed tools at the record:** b757_lockgate.py agree, b757_orders.py agree, b757_moves.py differ, b757_ceiling.py agree.', '',
                    '**Defects** (relay data/b756_defects.txt): %s.' % ('; '.join(rows) or 'none'), '',
                    '**Next:** as the author answers at the root (the answers bank).', ''])


# ================================================================================ (trail)
def control_trail():
    L, g, n = ['### (trail): THE TRAIL`S THREE LONG LINES BY COUNT, FROM b757'], 0, 0
    rows = heads()
    text = composed(rows)
    same = LDG.trail('b756', text, rows)
    n += 1
    g += both(L, 'trail', 'NOT IN FORCE: at b756 the composed trail unchanged (FROM_ACT %d)' % LDG.FROM_ACT, 'the act`s composition',
              'unchanged %s ; rows held %s' % (same == text, LDG.rows('b756')), True, same == text and LDG.rows('b756') == {})
    with _Forced():
        out = LDG.trail('b756', text, rows)
        held = LDG.rows('b756')
        nav, seat = AC.defect_owners(rows)['NAVIGATOR'], AC.defect_owners(rows)['SEAT']
        tg = LDG.tags(rows)
    o, t = out.split(NL), text.split(NL)
    dl = next((l for l in o if l.startswith('**Defects**')), '')
    sl = next((l for l in o if l.startswith('**The sealed tools')), '')
    rl = next((l for l in o if l.startswith(LDG.ROLL)), '')
    want_d = '%d lettered; CLAIM %d; CLOSE %d; the navigator’s %d, the seat’s %d' % (
        len(rows), sum(1 for _x, k in tg if k == 'CLAIM'), sum(1 for _x, k in tg if k == 'CLOSE'), nav, seat)
    n += 1
    g += case(L, 'trail', 'the Defects line over b756`s %d rows (relay data/b756_defects.txt)' % len(rows), 'every row`s head, %d characters' % len(
        next(l for l in t if l.startswith('**Defects**'))), dl[:200], True, want_d in dl and 'relay data/b756_defects.txt' in dl)
    n += 1
    g += case(L, 'trail', 'the sealed tools` line, four tools, one differing', 'each tool by name', sl, True,
              '4, 3 of them agreeing' in sl and 'relay data/b756_seal_hashes.json' in sl and held.get('sealed') and len(held['sealed']) == 4)
    n += 1
    g += case(L, 'trail', 'the open orders` roll line, three named', 'each order by name', '%s ; the trail bank`s rows %s' % (rl, held.get('open_orders')), True,
              rl.startswith(LDG.ROLL + ' 3 open') and not ORD.NAME.search(rl) and held.get('open_orders') == ['W-ORD-STORMER-CLASH', 'W-ORD-B518-FLOAT', 'W-ORD-ROOT-BINARY-BANK'])
    others = [(a, b) for a, b in zip(t, o) if not (a.startswith('**Defects**') or a.startswith('**The sealed tools') or a.startswith(LDG.ROLL))]
    n += 1
    g += both(L, 'trail', 'every other line as composed, the Next in full among them; the backticks of each line paired',
              '%d lines' % len(t), 'lines %d of %d ; unchanged %s ; odd-backtick lines %s' % (len(o), len(t), all(a == b for a, b in others),
                                                                                         [l for l in o if l.count('`') % 2]),
              True, len(o) == len(t) and all(a == b for a, b in others) and not [l for l in o if l.count('`') % 2]
              and '**Next:** as the author answers at the root (the answers bank).' in o)
    return L, g, n


# ================================================================================ (readers)
def control_readers():
    L, g, n = ['### (readers): THE ONE READING OF THE DEFECTS LINE'], 0, 0
    rows = heads()
    old_body = '; '.join(rows) or 'none'
    k0 = KIND0.findall(old_body)
    n += 1
    g += both(L, 'readers', 'before b757: the body the heads joined, the owners as KIND counts them', 'body %d chars ; owners %s' % (
        len(old_body), (sum(1 for _x, o in k0 if o == 'NAVIGATOR'), sum(1 for _x, o in k0 if o == 'SEAT'))),
              'body equal %s ; owners %s' % (LDG.defects_body('b756', rows) == old_body, LDG.owners_of('b756', old_body)), True,
              LDG.defects_body('b756', rows) == old_body and LDG.owners_of('b756', old_body) == (sum(1 for _x, o in k0 if o == 'NAVIGATOR'),
                                                                                                 sum(1 for _x, o in k0 if o == 'SEAT')))
    with _Forced():
        body = LDG.defects_body('b756', rows)
        got = LDG.owners_of('b756', body)
        planted = body.replace('the seat’s %d' % AC.defect_owners(rows)['SEAT'], 'the seat’s %d' % (AC.defect_owners(rows)['SEAT'] + 1))
        gotp = LDG.owners_of('b756', planted)
    want = (AC.defect_owners(rows)['NAVIGATOR'], AC.defect_owners(rows)['SEAT'])
    n += 1
    g += case(L, 'readers', 'from b757: the owners read from the counts the line prints, against the one counter (tools/act_close.py defect_owners)',
              'KIND over the count form reads %s' % (len(KIND0.findall(body)),), 'owners %s ; the counter %s' % (got, want), not KIND0.findall(body), got == want)
    n += 1
    g += both(L, 'readers', 'PLANTED: the seat`s count raised by one in the line', 'a mismatch', 'owners %s against %s' % (gotp, want), True, gotp != want)
    rec_t = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    chk_t = io.open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
    rec_b = V.show(BASE, 'tools/standing/fold/record.tpl') or ''
    chk_b = V.show(BASE, 'tools/standing/fold/checks.tpl') or ''
    n += 1
    g += case(L, 'readers', 'the record`s dry check and the suite`s two trail arms reading the line through tools/standing/ledgers.py',
              'ledgers named %d and %d times' % (rec_b.count('LDG.'), chk_b.count('standing.ledgers')),
              'the dry check %s ; trail_defects_ok %s ; trail_lines_equal_defects %s' % (
                  'want = LDG.defects_body(ACT, _letters_now())' in rec_t, ".defects_body(ACTN, seal))" in chk_t, ".owners_of(ACTN, dm.group(1))" in chk_t),
              rec_b.count('LDG.') == 0 and chk_b.count('standing.ledgers') == 0,
              'want = LDG.defects_body(ACT, _letters_now())' in rec_t and ".defects_body(ACTN, seal))" in chk_t and ".owners_of(ACTN, dm.group(1))" in chk_t)

    def upto(t, needle):
        return next((i for i, l in enumerate(t.split(NL)) if l.startswith(needle)), None)
    marks = ((rec_b, rec_t, 'MIRROR_FOLDER_ROLE = ', 'record.tpl, to the foot`s first binding'), (chk_b, chk_t, 'def main():', 'checks.tpl, to the part route`s main'))
    res = [(w, upto(b, nd), upto(t, nd)) for b, t, nd, w in marks]
    n += 1
    g += both(L, 'readers', 'the line-keyed regions (the acts before b735 key their overrides by line) the same length as at BASE',
              '; '.join('%s :%s' % (w, a) for w, a, _b in res), '; '.join('%s :%s' % (w, b) for w, _a, b in res), all(a for _w, a, _b in res),
              all(a is not None and a == b for _w, a, b in res))
    return L, g, n


# ================================================================================ (orders)
def old_orders():
    src = V.show(BASE, 'tools/standing/orders.py')
    m = types.ModuleType('orders_base')
    m.__file__ = os.path.join(S, 'orders.py')
    exec(compile(src, 'BASE:orders.py', 'exec'), m.__dict__)   # noqa: S102
    return m


def control_orders():
    L, g, n = ['### (orders): orders.py`s LAST ROLL LINE'], 0, 0
    OO = old_orders()
    lines = ORD.trail('HEAD')
    a, b = OO.last_roll(lines), ORD.last_roll(lines)
    n += 1
    g += both(L, 'orders', 'OPEN_TRAILS at PLACE-papers HEAD (%d lines): the last roll line read (its number and its names` count; no line printed)' % len(lines),
              ':%s, %d names' % (a[0], len(ORD.NAME.findall(a[1]))), ':%s, %d names' % (b[0], len(ORD.NAME.findall(b[1]))), bool(a[0]), a == b)
    planted = lines + ['', LDG.ROLL + ' 31 open at PLACE-papers main with this trail’s lines, each by name in relay data/b757_trail.json.']
    a2, b2 = OO.last_roll(planted), ORD.last_roll(planted)
    n += 1
    g += case(L, 'orders', 'PLANTED: a roll line by count after the last', ':%s, %d names' % (a2[0], len(ORD.NAME.findall(a2[1]))),
              ':%s, %d names' % (b2[0], len(ORD.NAME.findall(b2[1]))), len(ORD.NAME.findall(a2[1])) == 0, b2 == b)
    return L, g, n


# ================================================================================ (entry)
def control_entry():
    L, g, n = ['### (entry): THE CORRIGENDUM`S ENTRY, COMPOSED FROM b755`S BANKS'], 0, 0
    cj = json.load(io.open(os.path.join(D, 'b756_corrigendum.json'), encoding='utf-8'))
    title = '## Corrigendum to b755’s record, composed for the control'
    vb = io.open(os.path.join(D, 'b756_standing_v1347.txt'), encoding='utf-8').read()
    mv = re.search(r'CASES (\d+) ; AS WANTED (\d+)', vb)
    if not mv:
        raise SystemExit('relay data/b756_standing_v1347.txt carries no CASES line')
    vn, vg = int(mv.group(1)), int(mv.group(2))
    lines, tl = LDG.corrigendum('b755', D, title, [('tools/standing/ v1.34.7, (R366)(1)(i) and (ii)', 'dc8319ea', vg, vn, 'b756_standing_v1347.txt')])
    by = dict((k, dict(claim=v['claim'], close=v['close'], total=v['rows'])) for k, v in tl['tally'].items())
    landed = dict((k, dict(claim=v['claim'], close=v['close'], total=v['total'])) for k, v in cj['by_bank'].items())
    n += 1
    g += case(L, 'entry', 'the counts by bank against b756`s landed corrigendum (relay data/b756_corrigendum.json)', 'no composer: the act`s c1 alone',
              'composed %s ; landed %s' % (by, landed), True, by == landed)
    close_line = next((l for l in lines if l.startswith('**The CLOSE items')), '')
    n += 1
    g += case(L, 'entry', 'the entry`s parts in the rule`s order', 'no composer',
              'head first %s ; CLAIM %s ; repairs %s ; CLOSE %s' % (lines[0] == title, next((l for l in lines if l.startswith('**The CLAIM')), ''),
                                                                 next((l for l in lines if l.startswith('- tools/standing/')), ''), close_line), True,
              lines[0] == title and '**The CLAIM items, in full:** none.' in lines and '%d, every row in full in relay data/b755_defects.txt and relay data/b755_events.txt' % cj['close'] in close_line
              and any('its controls %d of %d as wanted (relay data/b756_standing_v1347.txt)' % (vg, vn) in l for l in lines))
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.34.9', ver == 'v1.35.0' == LDG.VERSION)
    return L, g, n


CONTROLS = dict(trail=control_trail, readers=control_readers, orders=control_orders, entry=control_entry, version=control_version)
ORDER = ('trail', 'readers', 'orders', 'entry', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.35.0, (R366)(6)[U2]: THE LEDGERS CARRY FINDINGS, IN FORCE FROM b757 (%s)' % (
               act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'written through tools/standing/figbank.py; no ledger line printed', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before and after, the tools before read from %s' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(V.free_line())
        try:
            L, g, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
        per.append('(%s) %d of %d' % (k, g, c))
    out.append('### per change: %s' % ' ; '.join(per))
    out.append('### ### **v1.35.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1350.txt' % act), NL.join(out))
        print('written data/%s_standing_v1350.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
