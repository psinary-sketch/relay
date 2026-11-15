# -*- coding: utf-8 -*-
"""tools/b756_faults_placed.py -- b756, (R366)(6): WHERE EACH FAULT OF TWO ACTS OR MORE WENT, read against the banks and the commits.
The rows and their places are read from data/b756_faults.txt (relay 21b0c76e), the count's own bank; a row whose place there reads
"none: ..." is NO CODE (the seat's manner or the words of a ruling) and is so read from the bank, not typed here. A row LANDED names
its version, its commit, the file the change stands in and the control that tests it; each is checked: the commit stands in
data/b756_steps.json, its file list carries the file and the version's controls bank, and that bank carries the control and closes
ALL AS WANTED. A row CARRIED gives its reason here, in the seat's words. The four hours of (6) read from the count's own stamp to the
last landed commit's time.
  python -X utf8 -u tools/b756_faults_placed.py [--bank]
"""
import io
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT = 'b756'
ROWLINE = re.compile(r"^  ((?:carried \(\d+\))|(?:b755 \([a-z]+\)))\s+(\d+)\s")
PLACELINE = re.compile(r"^      the place: (.*)$")

# ### each landed row: (version, commit, the file the change stands in, the controls bank, the control's name in it)
LANDED = {
    'carried (8)': ('v1.35.1', '7fae9822', 'tools/standing/postseal.py', 'data/b756_standing_v1351.txt', 'postseal'),
    'b755 (n)': ('v1.35.1', '7fae9822', 'tools/standing/carry.py', 'data/b756_standing_v1351.txt', 'carry'),
    'carried (6)': ('v1.35.1', '7fae9822', 'tools/standing/fold/record.tpl', 'data/b756_standing_v1351.txt', 'defectrow'),
    'carried (11)': ('v1.35.2', '520777a8', 'tools/standing/fold/checks.tpl', 'data/b756_standing_v1352.txt', 'editroute'),
    'carried (10)': ('v1.35.2', '520777a8', 'tools/standing/ranahead.py', 'data/b756_standing_v1352.txt', 'ranahead'),
    'carried (9)': ('v1.35.2', '520777a8', 'tools/standing/deletefree.py', 'data/b756_standing_v1352.txt', 'deletefree'),
    'b755 (o)': ('v1.35.2', '520777a8', 'tools/standing/commit.py', 'data/b756_standing_v1352.txt', 'shared'),
    'b755 (b)': ('v1.35.2', '520777a8', 'tools/standing/subject.py', 'data/b756_standing_v1352.txt', 'subject'),
    'b755 (e)': ('v1.35.2', '520777a8', 'tools/b756_address_scan.py', 'data/b756_standing_v1352.txt', 'scanheading'),
    'carried (1)': ('v1.35.2', '520777a8', 'tools/standing/gitwrite.py', 'data/b756_standing_v1352.txt', 'gitwrite'),
    'carried (2)': ('v1.35.2', '520777a8', 'tools/standing/gitwrite.py', 'data/b756_standing_v1352.txt', 'gitwrite'),
}
# ### each carried row, its reason (the seat's words)
CARRIED = {
    'b755 (d)': ('the (W) bank`s four paths wider than the ruling come from rules every act`s bank is built by (the kinds` next-act '
                 'rows, the amendment and face clauses` writes, the by-design list), not from this act`s; narrowing them is a change to '
                 'the kinds, read by every act, beyond a fault`s repair; the wider list refuses nothing it should admit, the seat writes '
                 'none of the four, and the bank is regenerated before the lock as (R366)(7) orders'),
}


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def rows_of(text):
    out, cur = [], None
    for l in text.split(NL):
        m = ROWLINE.match(l)
        if m:
            cur = dict(src=m.group(1), count=int(m.group(2)), place='')
            out.append(cur)
            continue
        p = PLACELINE.match(l)
        if p and cur is not None and not cur['place']:
            cur['place'] = p.group(1).strip()
    return out


def check_landed(src, steps, files_of, bank_text):
    ver, c, f, bank, ctl = LANDED[src]
    st = any(s.get('commit', '').startswith(c) for s in steps)
    fl = files_of(c)
    bt = bank_text(bank)
    ok = (st and f in fl and bank in fl and ('### (%s):' % ctl) in bt and bool(re.search(r'\*\*%s: CONTROLS .* ALL AS WANTED\.\*\*' % re.escape(ver), bt)))
    return ok, 'step row %s ; the file in the commit %s ; the controls bank in the commit %s ; the control (%s) in it %s ; %s ALL AS WANTED %s' % (
        st, f in fl, bank in fl, ctl, ('### (%s):' % ctl) in bt, ver, bool(re.search(r'\*\*%s: CONTROLS .* ALL AS WANTED\.\*\*' % re.escape(ver), bt)))


def main(argv):
    fb = rd(os.path.join(D, 'b756_faults.txt'))
    rows = [r for r in rows_of(fb) if r['count'] >= 2]
    steps = json.loads(rd(os.path.join(D, 'b756_steps.json')) or '[]')
    if isinstance(steps, dict):
        steps = steps.get('rows') or []
    cache = {}

    def files_of(c):
        if c not in cache:
            cache[c] = [x for x in git('show', '--name-only', '--format=', c).split(NL) if x.strip()]
        return cache[c]

    def bank_text(b):
        p = os.path.join(ROOT, b)
        return rd(p) if os.path.isfile(p) else ''

    out = ['%s -- (R366)(6): WHERE EACH FAULT OF TWO ACTS OR MORE WENT (%s)' % (ACT, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
           '### the rows and their places read from data/b756_faults.txt; each landed row checked against its commit, its step row and its',
           '### version`s controls bank; a place reading "none: ..." in the count`s bank is NO CODE; the carried row`s reason the seat`s words', '']
    # controls
    out.append('## THE CONTROLS, BEFORE ANY PLACING')
    c1 = len(rows) == 16 and rows[0]['src'] == 'carried (8)' and rows[0]['count'] == 23
    out.append('  (rows) the count`s bank read: rows of two acts or more %d ; the first %s at %d -> %s' % (
        len(rows), rows[0]['src'] if rows else None, rows[0]['count'] if rows else 0, 'AS WANTED' if c1 else 'NOT AS WANTED'))
    saved = LANDED.get('carried (8)')
    pk0, _w = check_landed('carried (8)', steps, files_of, bank_text)
    LANDED['carried (8)'] = (saved[0], 'deadbee1', saved[2], saved[3], saved[4])
    pk1, _w = check_landed('carried (8)', steps, files_of, bank_text)
    LANDED['carried (8)'] = (saved[0], saved[1], 'tools/standing/nosuchfile.py', saved[3], saved[4])
    pk2, _w = check_landed('carried (8)', steps, files_of, bank_text)
    LANDED['carried (8)'] = (saved[0], saved[1], saved[2], saved[3], 'nosuchcontrol')
    pk3, _w = check_landed('carried (8)', steps, files_of, bank_text)
    LANDED['carried (8)'] = saved
    c2 = pk0 and not pk1 and not pk2 and not pk3
    out.append('  (planted) the row carried (8) as it stands %s ; with a commit no step row holds %s ; with a file its commit does not carry %s ; '
               'with a control its bank does not name %s -> %s' % ('passed' if pk0 else 'REFUSED', 'refused' if not pk1 else 'PASSED',
                                                                 'refused' if not pk2 else 'PASSED', 'refused' if not pk3 else 'PASSED',
                                                                 'AS WANTED' if c2 else 'NOT AS WANTED'))
    nc = 2
    ng = int(c1) + int(c2)
    out.append('### THE CONTROLS : %d OF %d AS WANTED' % (ng, nc))
    out.append('')
    out.append('## THE PLACING, IN THE COUNT`S ORDER')
    tally = dict(LANDED=0, CARRIED=0, NOCODE=0, UNPLACED=0)
    bad = []
    for r in rows:
        s = r['src']
        if s in LANDED:
            ok, why = check_landed(s, steps, files_of, bank_text)
            ver, c, f, bank, ctl = LANDED[s]
            out.append('  %-14s %2d  LANDED %s, relay %s, %s ; control (%s) in %s' % (s, r['count'], ver, c, f, ctl, bank))
            out.append('      checked: %s -> %s' % (why, 'AS WANTED' if ok else 'NOT AS WANTED'))
            tally['LANDED'] += 1
            if not ok:
                bad.append(s)
        elif s in CARRIED:
            out.append('  %-14s %2d  CARRIED: %s' % (s, r['count'], CARRIED[s]))
            out.append('      the count`s place: %s' % r['place'])
            tally['CARRIED'] += 1
        elif r['place'].startswith('none:'):
            out.append('  %-14s %2d  NO CODE: %s (the count`s bank)' % (s, r['count'], r['place'][len('none:'):].strip()))
            tally['NOCODE'] += 1
        else:
            out.append('  %-14s %2d  UNPLACED: %s' % (s, r['count'], r['place']))
            tally['UNPLACED'] += 1
            bad.append(s)
    out.append('')
    m = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', fb.split(NL)[0])
    t0 = datetime.strptime(m.group(1), '%Y-%m-%dT%H:%M:%SZ') if m else None
    at = dict((s.get('commit', '')[:8], s.get('at')) for s in steps)
    last = max((LANDED[s][1] for s in LANDED), key=lambda c: at.get(c) or '')
    t1 = datetime.strptime(at[last], '%Y-%m-%dT%H:%M:%SZ')   # ### the step row's own time
    hrs = (t1 - t0).total_seconds() / 3600.0 if t0 else None
    u2 = at.get('2c3acfca')   # ### [U2]'s commit, v1.35.0: the change before the faults, so the earliest the faults' work began
    t2 = datetime.strptime(u2, '%Y-%m-%dT%H:%M:%SZ') if u2 else None
    h2 = (t1 - t2).total_seconds() / 3600.0 if t2 else None
    out.append('## THE FOUR HOURS ((R366)(6), "to four hours and no further"): to the last landed commit relay %s at %sZ, from [U2]`s commit relay '
               '2c3acfca at %s (v1.35.0, the change before the faults) %s h, from the count`s stamp %s %s h%s' % (
                   last, t1.strftime('%Y-%m-%dT%H:%M:%S'), u2, '%.2f' % h2 if h2 is not None else '?', m.group(1) if m else None,
                   '%.2f' % hrs if hrs is not None else '?',
                   ' ; within the four hours by either, and no row of two acts or more is left that a tool change answers' if h2 is not None and h2 <= 4 and not tally['UNPLACED'] else ''))
    out.append('### ### **THE FAULTS OF TWO ACTS OR MORE: %d ; LANDED %d (v1.35.1 and v1.35.2) ; CARRIED %d ; NO CODE %d ; UNPLACED %d ; THE CONTROLS %d OF %d ; %s.**' % (
        len(rows), tally['LANDED'], tally['CARRIED'], tally['NOCODE'], tally['UNPLACED'], ng, nc,
        'EACH LANDED ROW CHECKED AS WANTED' if not bad and ng == nc else 'NOT AS WANTED: %s' % bad))
    text = NL.join(out)
    print(text)
    if '--bank' in argv:
        if bad or ng != nc:
            sys.exit('NOT BANKED: a check or a control is not as wanted')
        with io.open(os.path.join(D, 'b756_faults_placed.txt'), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(text + NL)
        print('written data/b756_faults_placed.txt')


if __name__ == '__main__':
    main(sys.argv[1:])
