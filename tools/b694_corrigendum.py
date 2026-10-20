# -*- coding: utf-8 -*-
"""b694_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R304)(2): b693's closing row for relay push-b693-root, printed ABSENT where the branch
stood at 59de04e1, answered by one generated FINDINGS entry in b678's corrigendum form, b693's closing record (relay data/b693_closing.txt)
unedited, the row lettered as b693's defect (h).

### b678's tool (tools/b678_corrigendum.py) is IMPORTED and unchanged: its reader `rd`; its form -- one generated entry, each line it corrects
### quoted with its place, the corrected reading and its source, the figures read from their banks and checked before any write, `dry` then
### `land` -- is carried, as b689, b690, b692 and b693 carried it. Every figure is read, none typed:
###   the row as printed: relay data/b693_closing.txt, the line carrying "relay push-b693-root" and "ABSENT";
###   the branch: relay data/b693_root_branch_push_out.txt, the read-back line ("push_gated: branch push-b693-root read back at the remote: <sha>");
###   the cause: tools/b693_closing.py, the look-up (`def remote_refs`, its return line) and the row's call (`remote_refs(ROOT)`), and the
###              store's key (`paths = ['D:/' + r for r in REPOS]`); data/b693_defects.txt (h);
###   the repair: data/b694_tool_repairs.txt row (1) and data/b694_lookup_control.txt's verdict line.
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b694_record's
### guarded landing, data/b694_corrigendum.txt (.json). Written by the Write tool at b694; it writes those two banks and the one FINDINGS entry.
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

TITLE = ('## Corrigendum to b693’s closing record (relay data/b693_closing.txt): the push-b693-root row printed ABSENT where the branch stood '
         'at 59de04e1')
READBACK = re.compile(r'^push_gated: branch push-b693-root read back at the remote: ([0-9a-f]{40})$')


def at(path, pred):
    return [(i + 1, l) for i, l in enumerate(C78.rd(path).split(NL)) if pred(l)]


def compose():
    cl = at(os.path.join(D, 'b693_closing.txt'), lambda l: l.startswith('      relay push-b693-root') and 'ABSENT' in l)
    rb = at(os.path.join(D, 'b693_root_branch_push_out.txt'), lambda l: bool(READBACK.match(l)))
    src = os.path.join(T, 'b693_closing.py')
    look = at(src, lambda l: l.strip() == 'return _REMOTE.get(p, {})')
    call = at(src, lambda l: "remote_refs(ROOT).get('refs/heads/push-b693-root'" in l)
    store = at(src, lambda l: "paths = ['D:/' + r for r in REPOS]" in l)
    rootl = at(src, lambda l: l.startswith('ROOT = os.path.dirname'))
    dh = at(os.path.join(D, 'b693_defects.txt'), lambda l: l.startswith("    (h) THE SEAT'S"))
    ctl = re.findall(r'(?m)^### ### \*\*(.*)\*\*$', C78.rd(os.path.join(D, 'b694_lookup_control.txt')))
    rep = at(os.path.join(D, 'b694_tool_repairs.txt'), lambda l: l.startswith('  (1) tools/b694_closing.py'))
    ok = all(len(x) == 1 for x in (cl, rb, look, call, store, rootl, dh, rep)) and ctl and 'THE CONTROL AS WANTED True' in ctl[-1]
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ (closing %d, read-back %d, look-up %d, call %d, store %d, root %d, (h) %d, repair %d, control %s)'
                 ' -- NOTHING WRITTEN' % (len(cl), len(rb), len(look), len(call), len(store), len(rootl), len(dh), len(rep), bool(ctl)))
    return dict(cl=cl[0], sha=READBACK.match(rb[0][1]).group(1), rb=rb[0][0], look=look[0][0], call=call[0][0], store=store[0][0],
                root=rootl[0][0], h=dh[0][0], ctl=ctl[-1].rstrip('.'), rep=rep[0][0])


def entry_text(s):
    L = ['', TITLE, '',
         'b693’s closing record, pushed at relay 48ca2540, prints at its line :%d “relay push-b693-root remote ABSENT ; ### ABSENT”. The branch '
         'stood: pushed alone by push_gated’s branch mode and read back at %s (relay data/b693_root_branch_push_out.txt :%d), and read directly '
         'after the closing. The cause by line: the sealed closing tool stored its remote reads under the key %s (relay tools/b693_closing.py :%d) '
         'and looked them up by the path as passed (:%d); the row asked under its ROOT, built by os.path as D:\\relay (:%d, :%d), and found no '
         'read. Lettered b693’s defect (h), the seat’s (relay data/b693_defects.txt :%d). The repair at b694’s carry: one key for every read, '
         'stored and looked up alike, so D:\\relay, D:/relay and /d/relay resolve to the same reads (relay data/b694_tool_repairs.txt :%d); its '
         'control over a read store seeded from b693’s banked read-back -- the branch deleted at b694’s step zero under `(R304)`(5) -- prints “%s” '
         '(relay data/b694_lookup_control.txt). The closing record is not edited -- this entry is its correction: push-b693-root stood at %s at '
         'b693’s close. Nothing here proves RH or GRH.' % (
             s['cl'][0], s['sha'][:8], s['rb'], "'D:/' + the repository name", s['store'], s['look'], s['root'], s['call'], s['h'], s['rep'],
             s['ctl'], s['sha'][:8]), '',
         '*Filed at b694 on the author’s ruling `(R304)`(2): generated by relay `tools/b694_corrigendum.py` in the corrigendum form of relay '
         '`tools/b678_corrigendum.py` (its reader imported unchanged), banked as relay `data/b694_corrigendum.txt`, the corrigenda bank '
         '`data/b675_corrigenda.txt` appended at row (8); it answers b693’s defect (h).*', '']
    return NL.join(L)


def bank_lines(s, landed_line=None):
    return ['b694 -- THE CORRIGENDUM, (R304)(2): b693`S CLOSING ROW FOR push-b693-root, ITS DEFECT (h), ANSWERED BY ONE GENERATED FINDINGS ENTRY IN '
            'b678`s FORM', '', '### rows are the corrected line and the lines that correct it, each read from its bank by line; the closing record is not '
            'rewritten.', '',
            '  AS PRINTED              relay data/b693_closing.txt :%d | %s' % (s['cl'][0], s['cl'][1].strip()),
            '  THE BRANCH              relay data/b693_root_branch_push_out.txt :%d | read back at the remote: %s' % (s['rb'], s['sha']),
            '  THE STORE`S KEY         relay tools/b693_closing.py :%d | the reads stored under \'D:/\' + the repository name' % s['store'],
            '  THE LOOK-UP             relay tools/b693_closing.py :%d | the dict get by the path as passed' % s['look'],
            '  THE ROW`S CALL          relay tools/b693_closing.py :%d, ROOT at :%d | remote_refs(ROOT), ROOT D:\\relay' % (s['call'], s['root']),
            '  THE DEFECT              relay data/b693_defects.txt :%d | (h)' % s['h'],
            '  THE REPAIR              relay data/b694_tool_repairs.txt :%d | one key, repo_key(), at the store and at every look-up' % s['rep'],
            '  THE CONTROL             relay data/b694_lookup_control.txt | %s' % s['ctl'],
            '', '### ### **push-b693-root STOOD AT %s AT b693`S CLOSE ; THE CLOSING RECORD UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
                s['sha'][:8], landed_line or 'NOT YET WRITTEN')]


def main(route):
    s = compose()
    text = entry_text(s)
    import b694_record as REC
    if route == 'dry':
        REC.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(bank_lines(s)[-1])
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b694_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b694_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b694_corrigendum.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, branch_sha=s['sha'],
             printed=dict(closing_line=s['cl'][0]), cause=dict(store=s['store'], lookup=s['look'], call=s['call'], root=s['root']), control=s['ctl'])
    p = os.path.join(D, 'b694_corrigendum.json')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b694_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
