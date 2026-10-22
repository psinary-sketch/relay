# -*- coding: utf-8 -*-
"""b704_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R314)(2): b703's unlettered read after its closing lettered (m) in continuation of
data/b703_defects.txt's (a)-(l) -- the project-state memory file read whole after the closing, while it was updated -- answered by one
generated FINDINGS entry in b678's corrigendum form, the read rule's sort pointed to where it is banked (data/b704_read_sort.txt); b703's
sealed face (relay data/b703_registration_2026-10-21.txt), its trail record (PLACE-papers OPEN_TRAILS :15508) and every root-named bank unedited.

### Carried from tools/b703_corrigendum.py, its rows rewritten for b703's record. b678's tool (tools/b678_corrigendum.py) is IMPORTED and
### unchanged: its reader `rd`; its form -- one generated entry, each line it corrects quoted with its place, the corrected reading and its source,
### the figures read from their banks and checked before any write, `dry` then `land`. Every figure is read, none typed:
###   (m) the read: b703's session transcript (K.PREV_SESSION) -- the Read call on the memory file after the closing push's capture (its time
###       from data/b703_closing_push_out.txt :1), its offset and limit, and the file's length then from the call's own result (its last numbered
###       line); the read bank's stamp (data/b703_read_calls.txt :1) before it; b703's defects bank lettering (a)-(l).
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b704_record's
### guarded landing, data/b704_corrigendum.txt (.json). Written by the Write tool at b704; it writes those two banks and the one FINDINGS entry.
"""
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b678_corrigendum as C78   # noqa: E402  ### b678's tool, imported unchanged: rd
from b652_record import conv     # noqa: E402  ### the one conversion
import b704_worklist as K         # noqa: E402
import b704_record as REC         # noqa: E402  ### the guarded landing

TITLE = ('## Corrigendum to b703’s record after its closing (relay data/b703_closing_push_out.txt, data/b703_read_calls.txt): the '
         'project-state memory file read whole')
MEMORY = 'project_state_cp4_cp5_b559_b576.md'


def _memory_read():
    """the Read call on the memory file after the closing in b703's session, with the last numbered line of its own result."""
    po = C78.rd(os.path.join(D, 'b703_closing_push_out.txt')).split(NL)
    m = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', po[0])
    closing = m.group(1) if m else ''
    calls, results = [], {}
    for i, raw in enumerate(open(REC.PREV_SESSION_PATH, encoding='utf-8', errors='replace'), 1):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        cs = (o.get('message') or {}).get('content')
        for c in (cs if isinstance(cs, list) else []):
            if not isinstance(c, dict):
                continue
            if c.get('type') == 'tool_use' and c.get('name') == 'Read' and MEMORY in (c.get('input') or {}).get('file_path', '') \
                    and (o.get('timestamp') or '') > closing.replace('Z', ''):
                calls.append((i, o.get('timestamp'), c['input'].get('file_path'), c['input'].get('offset'), c['input'].get('limit'), c.get('id')))
            if c.get('type') == 'tool_result':
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t if isinstance(x, dict)) if isinstance(t, list) else (t or '')
                nums = [int(x) for x in re.findall(r'^\s*(\d+)\t', t, re.M)]
                results[c.get('tool_use_id')] = (max(nums) if nums else None, len(nums), len(t), ' '.join(t[-240:].split()))
    return closing, [(c[0], c[1], c[2], c[3], c[4]) + tuple(results.get(c[5]) or (None, 0, 0)) for c in calls]


def compose():
    closing, calls = _memory_read()
    rb = C78.rd(os.path.join(D, 'b703_read_calls.txt')).split(NL)
    rs = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', rb[0])
    df = C78.rd(os.path.join(D, 'b703_defects.txt')).split(NL)
    letters = re.findall(r"^    \(([a-z])\) THE ", NL.join(df), re.M)
    whole = [c for c in calls if not (c[3] and c[4])]
    sort = C78.rd(os.path.join(D, 'b704_read_sort.txt')).split(NL)
    sv = [l for l in sort if l.startswith('### ### **BREACHES')]
    now = len(C78.rd(whole[0][2]).replace(chr(13), '').rstrip(NL).split(NL)) if whole else 0
    ok = closing and len(whole) == 1 and now >= 200 and rs and rs.group(1) < closing and letters == list('abcdefghijkl') and sv
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ (closing %r, the whole reads %s, the file now %d lines, the read bank`s stamp %s, letters %s, the sort %s) '
                 '-- NOTHING WRITTEN' % (closing, whole, now, rs and rs.group(1), letters, sv))
    w = whole[0]
    return dict(closing=closing, line=w[0], at=w[1], path=w[2], lines=now, shown=w[6], chars=w[7], rb_at=rs.group(1),
                sort=sv[0].strip('#* ').rstrip('.*'), others=[c for c in calls if c is not w])


def entry_text(s):
    L = ['', TITLE, '',
         'b703’s closing push was captured at %s (relay data/b703_closing_push_out.txt :1), after every bank of the act was written; one read of '
         'the act’s session after it is in no bank the root names and in no lettered row of its defects bank (relay data/b703_defects.txt, (a)-(l)). '
         'This entry letters it (m) in continuation, with its cause by line; the face, the trail record and every root-named bank are not '
         'edited.' % s['closing'], '',
         '**(m) THE SEAT’S: THE PROJECT-STATE MEMORY FILE READ WHOLE AFTER THE CLOSING, WHILE IT WAS UPDATED.** At %s, b703’s session '
         '(%s, transcript line %d) read the project-state memory file (%s; %d lines now, 514 as b703’s seat reported it, the call’s stored '
         'result carrying its first %d lines) with neither an offset nor a limit, to update it -- where the read '
         'rule (relay data/b698_rules.txt row (2)) reads a file of two hundred lines or more by offset and limit, memory files included. The '
         'act’s read bank (relay data/b703_read_calls.txt) was stamped at %s, before the closing, so no bank carries the call.' % (
             s['at'], K.PREV_SESSION[:8], s['line'], s['path'].replace('\\', '/').split('/')[-1], s['lines'], s['shown'], s['rb_at']), '',
         '**The sort.** The read rule’s breaches at b703 -- (k) thirteen calls, (l) the one read before the lock and lettered after the seal '
         '(relay data/b703_defects.txt :70-:73), and (m) -- sorted by trace under the author’s word of 2026-10-18 (relay data/b704_read_sort.txt: '
         '%s): (k) and (l) traceable as rows of the read bank, (m) in none; the arm for the traceable class written on the author’s word at '
         'b704, (m)’s kind kept as prose and entered by hand when it occurs.' % s['sort'], '',
         'The sealed face, the trail record and every root-named bank are not edited -- this entry is their correction. Nothing here proves RH '
         'or GRH.', '',
         '*Filed at b704 on the author’s ruling `(R314)`(2): generated by relay `tools/b704_corrigendum.py`, carried from '
         '`tools/b703_corrigendum.py`, in the corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), banked as '
         'relay `data/b704_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (24); it answers b703’s one read '
         'after its closing.*', '']
    return NL.join(L)


def bank_lines(s, landed_line=None):
    return ['b704 -- THE CORRIGENDUM, (R314)(2): b703`S UNLETTERED READ AFTER ITS CLOSING, LETTERED (m), ANSWERED BY ONE GENERATED FINDINGS ENTRY '
            'IN b678`s FORM', '',
            '### rows are the corrected lines and the lines that correct them, each read from its source by line; the face, the trail and the '
            'root-named banks are not rewritten.', '',
            '  (m) THE READ            b703`s session %s, transcript line %d, %s | %s | offset none, limit none | %d lines now (514 as b703`s seat '
            'reported it) ; the stored result %d numbered lines, %d characters' % (K.PREV_SESSION[:8], s['line'], s['at'], s['path'], s['lines'], s['shown'], s['chars']),
            '                          the closing`s capture at %s (data/b703_closing_push_out.txt :1) ; the read bank stamped at %s (data/b703_read_calls.txt :1)' % (
                s['closing'], s['rb_at']),
            '                          the other reads of the file after the closing, each with both an offset and a limit: %s' % (
                '; '.join('line %d offset %s limit %s' % (c[0], c[3], c[4]) for c in s['others']) or 'NONE'),
            '  THE SORT                relay data/b704_read_sort.txt | %s' % s['sort'],
            '  THE CORRIGENDA BANK     relay data/b675_corrigenda.txt, row (24) appended by this act',
            '', '### ### **ONE ITEM LETTERED (m) ; THE FACE, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
                landed_line or 'NOT YET WRITTEN')]


def main(route):
    s = compose()
    text = entry_text(s)
    if route == 'dry':
        REC.R.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b704_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b704_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b704_corrigendum.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, lettered=['m'], closing=s['closing'],
             read=[s['line'], s['at'], s['path'], s['lines']], read_bank_at=s['rb_at'], sort=s['sort'])
    p = os.path.join(D, 'b704_corrigendum.json')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b704_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
