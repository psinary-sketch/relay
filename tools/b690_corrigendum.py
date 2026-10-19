# -*- coding: utf-8 -*-
"""b690_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R300)(2): b689's defect (e), the undeclared post-seal failure, answered by one generated
FINDINGS entry in b678's corrigendum form, b689's sealed face unedited.

### b678's tool (tools/b678_corrigendum.py) is IMPORTED and unchanged: its reader `rd`; its form -- one generated entry, each line it corrects
### quoted with its place, the corrected reading and its source, the figures read from their banks and checked before any write, `dry` then
### `land` -- is carried, as b689 carried it (tools/b689_corrigendum.py). Every figure here is read from a bank by line, none typed:
###   the face: relay data/b689_registration_2026-10-19.txt, its declaration line "THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE
###     LOCK, BY NAME:** NONE." and its lock block's "locked at (UTC)" line;
###   the arm's reading: relay data/b689_checks.txt and data/b689_checks_postpush.txt, each one's verdict line naming G-EDIT-ROUTE failing;
###   the command: relay data/b689_commands.txt :238 (#177 in the every-command list) and its offence row (:7);
###   the count as it stands: relay data/b689_closing.txt :1, "suite 115 of 116".
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b690_record's
### guarded landing, data/b690_corrigendum.txt (.json). Written by the Write tool at b690; it writes those two banks and the one FINDINGS entry.
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

FACE = 'b689_registration_2026-10-19.txt'
DECL = 'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:** NONE.'
VERDICT = "ARMS RUN : 116. ### LIVE PASSING : 115. ### LIVE FAILING : 1 ['G-EDIT-ROUTE']"
CMD_LINE, OFF_LINE = 238, 7
TITLE = '## Corrigendum to b689’s face (relay data/b689_registration_2026-10-19.txt): G-EDIT-ROUTE failed after the seal, undeclared'


def at(name, needle):
    """[(line, text)] of the bank lines carrying the needle."""
    return [(i + 1, l) for i, l in enumerate(C78.rd(os.path.join(D, name)).split(NL)) if needle in l]


def compose():
    decl = at(FACE, DECL)
    lock = at(FACE, 'locked at (UTC)')
    pre, post = at('b689_checks.txt', VERDICT), at('b689_checks_postpush.txt', VERDICT)
    cl = C78.rd(os.path.join(D, 'b689_commands.txt')).split(NL)
    cmd = cl[CMD_LINE - 1] if len(cl) >= CMD_LINE else ''
    off = cl[OFF_LINE - 1] if len(cl) >= OFF_LINE else ''
    head = C78.rd(os.path.join(D, 'b689_closing.txt')).split(NL)[0]
    m = re.match(r'^  #177 \| (\S+) \| seat \| Bash \| (.*)$', cmd)
    cnt = re.search(r'suite (\d+) of (\d+)', head)
    ok = len(decl) == 1 and len(lock) == 1 and pre and post and m and 'R sed in any form' in off and '#177' in off and cnt
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ (decl %d, lock %d, pre %d, post %d, cmd %s, off %s, count %s) -- NOTHING WRITTEN' % (
            len(decl), len(lock), len(pre), len(post), bool(m), '#177' in off, bool(cnt)))
    lock_at = re.search(r'locked at \(UTC\) : (\S+)', lock[0][1]).group(1)
    return dict(decl=decl[0], lock=lock[0], lock_at=lock_at, pre=pre[0], post=post[0], ts=m.group(1), cmd=m.group(2).strip(), off=off.strip(),
                count=(int(cnt.group(1)), int(cnt.group(2))), head=head)


def entry_text(s):
    L = ['', TITLE, '',
         'b689’s face, locked at %s, declares at its :%d “%s” -- no arm failing on real state; at %s, after the lock, the seat read the dry '
         'entry’s title by the shell command the command bank prints at relay data/b689_commands.txt :%d, “%s”, a sed read with a redirect onto '
         '/dev/null (its offence row :%d, “%s”). The arm G-EDIT-ROUTE reads the act’s whole capture, so from that command on it FAILS on real '
         'state: pre-push “%s” (relay data/b689_checks.txt :%d) and post-push the same (data/b689_checks_postpush.txt :%d). The count as it '
         'stands is the suites’ %d of %d (data/b689_closing.txt :1); the face’s declaration reads NONE where one arm failed, and the face, '
         'sealed, is not edited -- this entry is its correction. The locus: b688’s defect (f) and b689’s (e) both arose after the seal, in the '
         'window where the entry and the dry entry are read by shell; relay data/b690_rules.txt row (1) closes that window. Nothing here proves '
         'RH or GRH.' % (s['lock_at'], s['decl'][0], DECL.replace('** ', ' ').replace('**', ''), s['ts'], CMD_LINE, s['cmd'], OFF_LINE, s['off'],
                        VERDICT.replace(' ### ', ' ; '), s['pre'][0], s['post'][0], s['count'][0], s['count'][1]), '',
         '*Filed at b690 on the author’s ruling `(R300)`(2): generated by relay `tools/b690_corrigendum.py` in the corrigendum form of relay '
         '`tools/b678_corrigendum.py` (its reader imported unchanged), banked as relay `data/b690_corrigendum.txt`, the corrigenda bank '
         '`data/b675_corrigenda.txt` appended at row (4); it answers b689’s defect (e) (relay `data/b689_defects.txt` :38).*', '']
    return NL.join(L)


def bank_lines(s, landed_line=None):
    L = ['b690 -- THE CORRIGENDUM, (R300)(2): b689`s DEFECT (e), THE UNDECLARED POST-SEAL FAILURE, ANSWERED BY ONE GENERATED FINDINGS ENTRY IN b678`s FORM',
         '', '### rows are the corrected line and the lines that correct it, each read from its bank by line; the sealed face is not rewritten.', '',
         '  THE FACE`S DECLARATION   relay data/%s :%d | %s' % (FACE, s['decl'][0], s['decl'][1].strip()),
         '  THE LOCK                 relay data/%s :%d | %s' % (FACE, s['lock'][0], s['lock'][1].strip()),
         '  THE COMMAND              relay data/b689_commands.txt :%d | %s | %s' % (CMD_LINE, s['ts'], s['cmd']),
         '  ITS OFFENCE ROW          relay data/b689_commands.txt :%d | %s' % (OFF_LINE, s['off']),
         '  PRE-PUSH                 relay data/b689_checks.txt :%d | %s' % (s['pre'][0], s['pre'][1].strip()),
         '  POST-PUSH                relay data/b689_checks_postpush.txt :%d | %s' % (s['post'][0], s['post'][1].strip()),
         '  THE COUNT AS IT STANDS   relay data/b689_closing.txt :1 | %s' % s['head'],
         '', '### ### **THE FACE DECLARES NONE ; G-EDIT-ROUTE FAILS PRE-PUSH AND POST-PUSH ; THE COMMAND AT data/b689_commands.txt :%d (%s) ; THE COUNT %d OF %d ; '
             'THE ENTRY AT FINDINGS :%s.**' % (CMD_LINE, s['ts'], s['count'][0], s['count'][1], landed_line or 'NOT YET WRITTEN')]
    return L


def main(route):
    s = compose()
    text = entry_text(s)
    import b690_record as REC
    if route == 'dry':
        REC.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(bank_lines(s)[-1])
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b690_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b690_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b690_corrigendum.txt')
    open(p + '.tmp', 'wb').write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, decl=s['decl'], lock=s['lock'], command=dict(
        line=CMD_LINE, ts=s['ts'], text=s['cmd']), pre=s['pre'], post=s['post'], count=s['count'])
    p = os.path.join(D, 'b690_corrigendum.json')
    open(p + '.tmp', 'wb').write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b690_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
