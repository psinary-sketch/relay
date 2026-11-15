# -*- coding: utf-8 -*-
"""b756, (R366)(7): THE CEILING READ AGAIN AFTER COMPONENT 4 ("THE CEILING: 24 hours against the table's lower figures, read at step zero
and again after Component 4; over it, carried in this order: (6) from its end backward; then (5)(i)'s HERE work", data/b756_ferry.txt :32).
The price table is step zero's, read from its bank at relay HEAD (data/b756_stepzero.txt, the section "## THE PRICE TABLE"), each row parsed
and placed: DONE (a row of Component 0 to 4, its work landed), REMAINING (Component 5 and 6), or BESIDE (a row the table printed beside and
did not sum). The spent time is the clock from the ruling's delivery (transcript line 69885, 2026-11-15T12:27:47Z, as step zero read it) to
this run, in place of the DONE rows' figures; the read is the spent time with the REMAINING rows' lower figures, against 24 hours, the upper
figures printed beside. Its control: step zero's own sum recomputed from the parsed rows equals the bank's THE SUM line.
MODES  dry | bank      BANK data/b756_ceiling_c4.txt
"""
import calendar
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
NL = '\n'
SZ = 'data/b756_stepzero.txt'
BANK = os.path.join(RELAY, 'data', 'b756_ceiling_c4.txt')
DELIVERY = '2026-11-15T12:27:47Z'
CEILING = 24.0
DONE = ('(1) weight', '(1) corrigendum', '(1)(i)+(ii)', '(1)(i) line', '(2)', '(4)(i) carry', '(4)(ii)', '(4)(iii)', '(3)(vi)', '(5)(i) read',
        '(5) put', '(5)(i) HERE', '(1) lock gate', '(3)(i)-(v)', '(4)(i) run')
REMAINING = ('(6)[U1]', '(6)[U2]', '(6) faults', '(6)[H1]', '(6) README', 'C6 act module', 'gate', 'lock', 'seal', 'pre-root', 'root', 'record', 'closing')
CARRY_ORDER = ('(6) README', '(6)[H1]', '(6) faults', '(6)[U2]', '(6)[U1]')   # ### (6) from its end backward; (5)(i)'s HERE work landed
ROW = re.compile(r'^  (\S.*?)\s{2,}(\S.*?) \| (.*)$')
FIG = re.compile(r'^(\d+(?:\.\d+)?)(?:-(\d+(?:\.\d+)?))? h (\(estimate\)|READ)(, BESIDE)?$')


def relay_head(path):
    r = subprocess.run(['git', '-C', RELAY, 'show', 'HEAD:%s' % path], capture_output=True)
    if r.returncode:
        raise SystemExit('### %s NOT READ AT RELAY HEAD -- NOTHING DONE' % path)
    return r.stdout.decode('utf-8').replace('\r', '').split(NL)


def epoch(s):
    return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))


def parse(L):
    a = next(i for i, l in enumerate(L) if l.startswith('## THE PRICE TABLE'))
    b = next(i for i, l in enumerate(L) if l.startswith('## THE CEILING'))
    rows, spent0, total = [], None, None
    for k in range(a, b):
        l = L[k]
        m0 = re.match(r'^  STEP ZERO, SPENT\s+(\d+\.\d+) h', l)
        if m0:
            spent0 = float(m0.group(1))
            continue
        if l.startswith('  THE SUM'):
            total = (k + 1, l.strip())
            continue
        m = ROW.match(l)
        if not m:
            continue
        label, desc, fig = m.group(1).strip(), m.group(2), m.group(3).strip()
        f = FIG.match(fig)
        if f:
            lo = float(f.group(1))
            hi = float(f.group(2)) if f.group(2) else lo
            kind = 'BESIDE' if f.group(4) else ('estimate' if f.group(3).startswith('(') else 'READ')
        elif fig == 'NOT PRICED, NO BANK':
            lo = hi = None
            kind = 'UNPRICED'
        else:
            raise SystemExit('### THE ROW AT %s :%d NOT READ (%r) -- NOTHING DONE' % (SZ, k + 1, fig))
        rows.append(dict(line=k + 1, label=label, lo=lo, hi=hi, kind=kind))
    return rows, spent0, total


def place(r):
    if r['kind'] == 'BESIDE':
        return 'BESIDE'
    if r['label'] in DONE:
        return 'DONE'
    if r['label'] in REMAINING:
        return 'REMAINING'
    return None


def compose():
    L = relay_head(SZ)
    rows, spent0, total = parse(L)
    out = []
    unplaced = [r for r in rows if place(r) is None]
    summed = [r for r in rows if r['kind'] in ('estimate', 'READ')]
    lo0 = spent0 + sum(r['lo'] for r in summed)
    hi0 = spent0 + sum(r['hi'] for r in summed)
    want = 'THE SUM' in total[1] and ('= %.2f-%.2f h' % (lo0, hi0)) in total[1]
    out.append(('every row of the table parsed and placed (%d rows ; unplaced %s)' % (len(rows), [r['label'] for r in unplaced] or 'none'), not unplaced, True))
    out.append(('step zero`s sum recomputed from the parsed rows, %.2f-%.2f h, equal to %s :%d' % (lo0, hi0, SZ, total[0]), want, True))
    out.append(('each REMAINING label read once in the table', all(sum(1 for r in rows if r['label'] == x and r['kind'] != 'BESIDE') == 1 for x in REMAINING), True))
    try:
        place(dict(label='(9) planted', kind='estimate')) or (_ for _ in ()).throw(SystemExit('unplaced'))
        refused = False
    except SystemExit:
        refused = True
    out.append(('a planted row of no place left unplaced, and so refused by the first control', refused, True))
    now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    spent = (epoch(now) - epoch(DELIVERY)) / 3600.0
    rem = [r for r in rows if place(r) == 'REMAINING']
    lo, hi = spent + sum(r['lo'] for r in rem), spent + sum(r['hi'] for r in rem)
    carry, run = [], lo
    for c in CARRY_ORDER:
        if run <= CEILING:
            break
        r = next(x for x in rem if x['label'] == c)
        run -= r['lo']
        carry.append((c, r['lo'], run))
    return L, rows, out, dict(now=now, spent=spent, lo=lo, hi=hi, carry=carry, lo0=lo0, hi0=hi0, total=total)


def main(argv):
    step = argv[0] if argv else ''
    if step not in ('dry', 'bank'):
        sys.exit(__doc__)
    L, rows, out, R = compose()
    for n, a, b in out:
        print('  CONTROL %s: %s (wanted %s)' % (n, a, b))
    good = sum(1 for _, a, b in out if a == b)
    print('### CONTROLS %d OF %d AS WANTED' % (good, len(out)))
    if good != len(out):
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    B = ['b756 -- (R366)(7): THE CEILING READ AGAIN AFTER COMPONENT 4 (%s)' % R['now'], '',
         '### by tools/b756_ceiling.py, committed before its run. The table is step zero`s (relay %s, its section "## THE PRICE TABLE"), each row' % SZ,
         '### parsed and placed DONE, REMAINING or BESIDE; the spent time is the clock from the ruling`s delivery (%s) to this run, in place of' % DELIVERY,
         '### the DONE rows; the read is the spent time with the REMAINING rows` lower figures against %d hours, the upper beside.' % CEILING,
         '### CONTROLS %d OF %d AS WANTED: step zero`s sum recomputed, %.2f-%.2f h, equal to its THE SUM line (:%d).' % (good, len(out), R['lo0'], R['hi0'], R['total'][0]), '',
         '## THE ROWS']
    for p in ('DONE', 'REMAINING', 'BESIDE'):
        for r in rows:
            if place(r) == p:
                fig = 'not priced' if r['lo'] is None else ('%.2f-%.2f h' % (r['lo'], r['hi']))
                B.append('  %-9s %-16s %-16s (%s :%d, %s)' % (p, r['label'], fig, SZ, r['line'], r['kind']))
    rem = [r for r in rows if place(r) == 'REMAINING']
    B += ['', '## THE READ',
          '  SPENT, the ruling`s delivery to this run: %.2f h' % R['spent'],
          '  REMAINING, lower %.2f h ; upper %.2f h (%d rows: (6) %.2f-%.2f h ; Component 6 %.2f-%.2f h)' % (
              sum(r['lo'] for r in rem), sum(r['hi'] for r in rem), len(rem),
              sum(r['lo'] for r in rem if r['label'].startswith('(6)')), sum(r['hi'] for r in rem if r['label'].startswith('(6)')),
              sum(r['lo'] for r in rem if not r['label'].startswith('(6)')), sum(r['hi'] for r in rem if not r['label'].startswith('(6)'))),
          '  THE LOWER READ %.2f h %s %d h: %s' % (R['lo'], '<=' if R['lo'] <= CEILING else '>', CEILING,
                                                 'NOTHING CARRIED' if not R['carry'] else 'CARRIED ' + ' ; '.join('%s (%.2f h, the lower read after %.2f h)' % c for c in R['carry'])),
          '  BESIDE IT, NOT THE READ: the upper %.2f h %s %d h' % (R['hi'], '<=' if R['hi'] <= CEILING else '>', CEILING),
          '  NOT CARRIED BY THE RULING`S WORDS: (1), (2), (3), (4), (5)(ii); (5)(i)`s HERE work landed (relay 5b7aa91e)', '',
          '### ### **THE CEILING AFTER COMPONENT 4: SPENT %.2f h + REMAINING LOWER %.2f h = %.2f h AGAINST %d h ; %s ; THE UPPER %.2f h BESIDE.**' % (
              R['spent'], sum(r['lo'] for r in rem), R['lo'], CEILING, 'NOTHING CARRIED' if not R['carry'] else '%d CARRIED' % len(R['carry']), R['hi'])]
    print(NL.join(B))
    if step == 'bank':
        if os.path.exists(BANK):
            raise SystemExit('### %s STANDS ALREADY -- NOTHING WRITTEN' % os.path.relpath(BANK, RELAY))
        with open(BANK + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(NL.join(B) + NL)
        os.replace(BANK + '.tmp', BANK)
        print('### BANKED %s' % os.path.relpath(BANK, RELAY))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
