# -*- coding: utf-8 -*-
"""b703_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R313)(2): b702's two items after its root lettered (j) and (k) in continuation of
data/b702_defects.txt's (a)-(i) -- the mirror bank's span line naming b697's export, and the closing push's opening call given the repository's
name -- answered by one generated FINDINGS entry in b678's corrigendum form, the between-acts read pointed to where it is lettered (b703's
(a)); b702's sealed face (relay data/b702_registration_2026-10-21.txt), its trail record (PLACE-papers OPEN_TRAILS :15458) and every root-named
bank unedited.

### Carried from tools/b702_corrigendum.py, its rows rewritten for b702's record. b678's tool (tools/b678_corrigendum.py) is IMPORTED and
### unchanged: its reader `rd`; its form -- one generated entry, each line it corrects quoted with its place, the corrected reading and its source,
### the figures read from their banks and checked before any write, `dry` then `land`. Every figure is read, none typed:
###   (j) the span line: data/b702_mirror.txt (the line carrying "### THE SPAN:"), the literal at tools/b698_record.py (the line carrying it), the
###       mirror bank chain (data/b701_mirror.json's zip, the last export before b702's), b702's root time (data/b702_act_root.json "at") before
###       the mirror bank's own stamp (its head line);
###   (k) the closing push: data/b702_closing_push_out.txt (the two "capture on" lines, the git error between them, the second call's read-back),
###       committed at this act's step zero (its commit read from the log).
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b703_record's
### guarded landing, data/b703_corrigendum.txt (.json). Written by the Write tool at b703; it writes those two banks and the one FINDINGS entry.
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
import b703_worklist as K         # noqa: E402
import b703_record as REC         # noqa: E402  ### the guarded landing and the mirror chain

TITLE = ('## Corrigendum to b702’s record after its root (relay data/b702_mirror.txt, data/b702_closing_push_out.txt): the mirror bank’s span '
         'line and the closing push’s opening call')


def at(path, pred):
    L = C78.rd(path).split(NL)
    return [(i + 1, l) for i, l in enumerate(L) if pred(l)]


def compose():
    mi = at(os.path.join(D, 'b702_mirror.txt'), lambda l: l.startswith('### THE SPAN:'))
    mh = C78.rd(os.path.join(D, 'b702_mirror.txt')).split(NL)[0]
    m_at = re.search(r'banked (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', mh)
    lit = at(os.path.join(T, 'b698_record.py'), lambda l: '### THE SPAN: every roster and ledger change of b698 (the last export b697`s' in l)
    last, z = REC._last_export('b702')
    rj = json.loads(C78.rd(os.path.join(D, 'b702_act_root.json')) or '{}')
    root_at = rj.get('at') or ''
    po = C78.rd(os.path.join(D, 'b702_closing_push_out.txt')).split(NL)
    caps = [(i + 1, l) for i, l in enumerate(po) if l.startswith('push_gated: capture on')]
    err = [(i + 1, l) for i, l in enumerate(po) if l.startswith('fatal: cannot change to ')]
    back = [(i + 1, l) for i, l in enumerate(po) if l.startswith('push_gated: main read back at the remote: 8773acc9')]
    pc = [x for x in REC.g(ROOT, 'log', '--format=%h %s', '--', 'data/b702_closing_push_out.txt').split(NL) if x.strip()]
    ok = (len(mi) == 1 and 'the last export b697`s' in mi[0][1] and len(lit) == 1 and last == 'b701' and z and m_at and m_at.group(1) > root_at
          and len(caps) == 2 and len(err) == 1 and caps[0][0] < err[0][0] < caps[1][0] and len(back) == 1 and len(pc) == 1 and pc[0].startswith('4937f61'))
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ (span %s, literal %s, chain %s %s, mirror at %s root at %s, captures %s, error %s, read back %s, commits %s) '
                 '-- NOTHING WRITTEN' % (mi, lit, last, z, m_at and m_at.group(1), root_at, caps, err, back, pc))
    return dict(mi=mi[0], lit=lit[0], last=last, zip=z, m_at=m_at.group(1), root_at=root_at, caps=caps, err=err[0], back=back[0], commit=pc[0].split()[0])


def entry_text(s):
    L = ['', TITLE, '',
         'b702’s root was computed before its mirror and its closing push, as the act’s order has it, so two of its records after the root are '
         'in no bank the root names and in no lettered row of its defects bank (relay data/b702_defects.txt, (a)-(i)). This entry letters them (j) '
         'and (k) in continuation, each with its cause by line; the face, the trail record and every root-named bank are not edited.', '',
         '**(j) THE SEAT’S: THE MIRROR BANK’S SPAN LINE NAMES b697’S EXPORT.** relay data/b702_mirror.txt :%d reads “%s”; the last export before '
         'b702’s was %s’s (%s, named by data/%s_mirror.json), the line carried as wording from b698’s record tool (tools/b698_record.py :%d), '
         'which b702’s record tool imports. The mirror bank was written at %s, after the root at %s. The repair, at b703’s carry: the span line '
         'read from the mirror bank chain and not carried as wording (relay tools/b703_record.py, `span` and `mbank`; data/b703_tool_repairs.txt), '
         'its dry run printing b702 as the last export before b703’s.' % (
             s['mi'][0], s['mi'][1], s['last'], s['zip'], s['last'], s['lit'][0], s['m_at'], s['root_at']), '',
         '**(k) THE SEAT’S: THE CLOSING PUSH’S OPENING CALL GIVEN THE REPOSITORY’S NAME FOR ITS PATH.** relay data/b702_closing_push_out.txt :%d '
         'opens the first call and :%d carries its stop, “%s” -- the push tool given `relay` where it takes the repository by its path; exit 128, '
         'nothing pushed. The second call (:%d) took `/d/relay` and read main back at the remote (:%d). Both calls stand in the capture, committed at '
         'b703’s step zero (relay %s).' % (s['caps'][0][0], s['err'][0], s['err'][1], s['caps'][1][0], s['back'][0], s['commit']), '',
         '**The between-acts read.** The seat’s read of relay data/b681_narrow.txt :5-:40 between b702 and b703 (rows of the narrowing bank, no '
         'ordinate and no real part among them, nothing computed from them) is lettered (a) in relay data/b703_defects.txt, the act whose ruling '
         'it precedes; the registration of b703 is unaffected.', '',
         'The sealed face, the trail record and every root-named bank are not edited -- this entry is their correction. Nothing here proves RH '
         'or GRH.', '',
         '*Filed at b703 on the author’s ruling `(R313)`(2): generated by relay `tools/b703_corrigendum.py`, carried from '
         '`tools/b702_corrigendum.py`, in the corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), banked as '
         'relay `data/b703_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at rows (22) and (23); it answers b702’s two '
         'items after its root.*', '']
    return NL.join(L)


def bank_lines(s, landed_line=None):
    return ['b703 -- THE CORRIGENDUM, (R313)(2): b702`S TWO ITEMS AFTER ITS ROOT, LETTERED (j) AND (k), ANSWERED BY ONE GENERATED FINDINGS ENTRY '
            'IN b678`s FORM', '',
            '### rows are the corrected lines and the lines that correct them, each read from its bank by line; the face, the trail and the '
            'root-named banks are not rewritten.', '',
            '  (j) THE SPAN LINE       relay data/b702_mirror.txt :%d | %s' % (s['mi'][0], s['mi'][1][:140]),
            '                          the literal: relay tools/b698_record.py :%d ; the chain: data/%s_mirror.json names %s (the last export before b702`s)' % (
                s['lit'][0], s['last'], s['zip']),
            '                          the mirror bank at %s, the root at %s (the bank after the root, named by no root)' % (s['m_at'], s['root_at']),
            '  (k) THE CLOSING PUSH    relay data/b702_closing_push_out.txt :%d (the first call) ; :%d %s ; :%d (the second) ; :%d (main read back at '
            '8773acc9) ; committed at relay %s' % (s['caps'][0][0], s['err'][0], s['err'][1], s['caps'][1][0], s['back'][0], s['commit']),
            '  THE BETWEEN-ACTS READ   relay data/b703_defects.txt (a) | data/b681_narrow.txt :5-:40, lettered in b703`s bank',
            '  THE CORRIGENDA BANK     relay data/b675_corrigenda.txt, rows (22) and (23) appended by this act',
            '', '### ### **TWO ITEMS LETTERED (j) AND (k) ; THE FACE, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
                landed_line or 'NOT YET WRITTEN')]


def main(route):
    s = compose()
    text = entry_text(s)
    if route == 'dry':
        REC.R.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b703_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b703_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b703_corrigendum.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, lettered=['j', 'k'], span=list(s['mi']),
             literal=list(s['lit']), last_export=[s['last'], s['zip']], mirror_at=s['m_at'], root_at=s['root_at'],
             captures=[list(x) for x in s['caps']], error=list(s['err']), read_back=list(s['back']), commit=s['commit'])
    p = os.path.join(D, 'b703_corrigendum.json')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b703_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
