# -*- coding: utf-8 -*-
"""b692_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R302)(2): b691's two items after the root, answered by one generated FINDINGS entry in
b678's corrigendum form, b691's sealed face unedited, the two lettered as b691's defects (l) and (m).

### b678's tool (tools/b678_corrigendum.py) is IMPORTED and unchanged: its reader `rd`; its form -- one generated entry, each line it corrects
### quoted with its place, the corrected reading and its source, the figures read from their banks and checked before any write, `dry` then
### `land` -- is carried, as b689 and b690 carried it (tools/b689_corrigendum.py, tools/b690_corrigendum.py). Every figure is read, none typed:
###   (l) the face: relay data/b691_registration_2026-10-19.txt, its declaration line naming G-RULE-ONE-GIT-WRITE alone and its lock line; the
###       suites' verdict lines (data/b691_checks.txt, data/b691_checks_postpush.txt) naming G-RULE-SUITE-PARTS failing beside it; the arm's
###       own rows (data/b691_checks_standing-a.txt, data/b691_checks_postpush_standing-a.txt); its pattern at tools/rule_arms.py :268 and the
###       parts the pre-run bank carries (data/b691_arms_prerun.txt);
###   (m) the two PLACE-papers commits, cb6b7ef and 9a0dc76, their subjects and trees read by git; relay f5318624's message, which names the
###       amend and the arm that read the first subject (the first standing-a bank was rewritten by its re-run, so the commit is the record).
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b692_record's
### guarded landing, data/b692_corrigendum.txt (.json). Written by the Write tool at b692; it writes those two banks and the one FINDINGS entry.
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b678_corrigendum as C78   # noqa: E402  ### b678's tool, imported unchanged: rd
from b652_record import conv     # noqa: E402  ### the one conversion

FACE = 'b691_registration_2026-10-19.txt'
DECL = 'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:** `G-RULE-ONE-GIT-WRITE`.'
VERDICT = "ARMS RUN : 121. ### LIVE PASSING : 119. ### LIVE FAILING : 2 ['G-RULE-ONE-GIT-WRITE', 'G-RULE-SUITE-PARTS']"
ARM_ROW = '###   G-RULE-SUITE-PARTS           FAIL read '
PATTERN_LINE = 268
OLD, NEW, TREE = 'cb6b7ef', '9a0dc76', '26892785'
CLOSING_COMMIT = 'f5318624'
TITLE = ('## Corrigendum to b691’s face (relay data/b691_registration_2026-10-19.txt): G-RULE-SUITE-PARTS failed after the seal, undeclared; '
         'the trail commit’s subject amended before its push')


def at(name, needle):
    """[(line, text)] of the bank lines carrying the needle."""
    return [(i + 1, l) for i, l in enumerate(C78.rd(os.path.join(D, name)).split(NL)) if needle in l]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def compose():
    decl, lock = at(FACE, DECL), at(FACE, 'locked at (UTC)')
    pre, post = at('b691_checks.txt', VERDICT), at('b691_checks_postpush.txt', VERDICT)
    apre, apost = at('b691_checks_standing-a.txt', ARM_ROW), at('b691_checks_postpush_standing-a.txt', ARM_ROW)
    pat = (C78.rd(os.path.join(T, 'rule_arms.py')).split(NL) + [''] * PATTERN_LINE)[PATTERN_LINE - 1]
    parts = re.findall(r'(?m)^  ### PART ([\w-]+) : ARMS \d+ ; \d+ s$', C78.rd(os.path.join(D, 'b691_arms_prerun.txt')))
    head = C78.rd(os.path.join(D, 'b691_closing.txt')).split(NL)[0]
    cnt = re.search(r'suite (\d+) of (\d+)', head)
    so, sn = git(PP, 'log', '-1', '--format=%s', OLD), git(PP, 'log', '-1', '--format=%s', NEW)
    to, tn = git(PP, 'rev-parse', OLD + '^{tree}'), git(PP, 'rev-parse', NEW + '^{tree}')
    po, pn = git(PP, 'rev-parse', OLD + '^'), git(PP, 'rev-parse', NEW + '^')
    cm = git(ROOT, 'log', '-1', '--format=%B', CLOSING_COMMIT)
    mf = re.search(r'G-RULE-SUITE-PARTS\s+FAIL read (\d+) ; failing (\d+)', apre[0][1]) if apre else None
    mp = re.search(r'G-RULE-SUITE-PARTS\s+FAIL read (\d+) ; failing (\d+)', apost[0][1]) if apost else None
    ok = (len(decl) == 1 and len(lock) == 1 and pre and post and mf and mp and r'\bstanding-[a-z]\b' in pat
          and parts == ['standing-a', 'standing-c', 'standing-b1', 'standing-b2', 'act'] and cnt
          and so.startswith('b691 trail') and sn.startswith('b691 record') and to == tn and to.startswith(TREE) and po == pn
          and 'amended before its push' in cm and 'G-SEALED-AFTER-COMPONENTS' in cm)
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ (decl %d, lock %d, pre %d, post %d, arm %s/%s, pattern %s, parts %s, count %s, subjects %r/%r, '
                 'trees %s, parents %s, closing message %s) -- NOTHING WRITTEN' % (
                     len(decl), len(lock), len(pre), len(post), bool(mf), bool(mp), r'\bstanding-[a-z]\b' in pat, parts, bool(cnt), so[:30],
                     sn[:30], to == tn, po == pn, 'amended before its push' in cm))
    lock_at = re.search(r'locked at \(UTC\) : (\S+)', lock[0][1]).group(1)
    return dict(decl=decl[0], lock=lock[0], lock_at=lock_at, pre=pre[0], post=post[0], apre=apre[0], apost=apost[0], arm_pre=mf.groups(),
                arm_post=mp.groups(), pat=pat.strip(), parts=parts, count=(int(cnt.group(1)), int(cnt.group(2))), head=head, so=so, sn=sn,
                tree=to, parent=po)


def entry_text(s):
    L = ['', TITLE, '',
         'b691’s face, locked at %s, declares at its :%d one arm failing on real state, G-RULE-ONE-GIT-WRITE. Two items followed the root. '
         '(l) G-RULE-SUITE-PARTS FAILS pre-push and post-push, undeclared: the suites read “%s” (relay data/b691_checks.txt :%d, '
         'data/b691_checks_postpush.txt :%d), the arm’s own rows “read %s ; failing %s” pre-push and “read %s ; failing %s” post-push '
         '(data/b691_checks_standing-a.txt :%d, data/b691_checks_postpush_standing-a.txt :%d). Its cause by line: the arm reads each act’s '
         'governing parts from the rules banks with the pattern at relay tools/rule_arms.py :%d, “%s”, which reads standing-b1 and standing-b2 '
         '-- the names the five-part split under `(R301)`(8) gave the pre-run, “%s” (data/b691_arms_prerun.txt) -- as no part, so b691’s own run '
         'banks match no governing list; the pre-run passed because its combined bank did not yet exist when the arm ran. Lettered b691’s '
         'defect (l), shared: the navigator’s (the split named parts the arm could not read) and the seat’s (the arm not run against the new '
         'names before the seal). (m) The PLACE-papers trail commit’s subject amended before its push: %s “%s” became %s “%s”, the tree %s and '
         'the parent %s unchanged, after G-SEALED-AFTER-COMPONENTS read the first subject as a component commit after the lock; done without a '
         'prompt because none is allowed after the seal, and named in relay %s’s message. Lettered b691’s defect (m), the seat’s; relay '
         'data/b692_rules.txt row (1) binds from b692: a commit made after the seal that fails an arm is left as it stands. The count as it '
         'stands is the suites’ %d of %d (data/b691_closing.txt :1); the face, sealed, is not edited -- this entry is its correction. Nothing '
         'here proves RH or GRH.' % (
             s['lock_at'], s['decl'][0], VERDICT.replace(' ### ', ' ; '), s['pre'][0], s['post'][0], s['arm_pre'][0], s['arm_pre'][1],
             s['arm_post'][0], s['arm_post'][1], s['apre'][0], s['apost'][0], PATTERN_LINE, s['pat'], ', '.join(s['parts']), OLD, s['so'], NEW,
             s['sn'], s['tree'][:8], s['parent'][:7], CLOSING_COMMIT, s['count'][0], s['count'][1]), '',
         '*Filed at b692 on the author’s ruling `(R302)`(2): generated by relay `tools/b692_corrigendum.py` in the corrigendum form of relay '
         '`tools/b678_corrigendum.py` (its reader imported unchanged), banked as relay `data/b692_corrigendum.txt`, the corrigenda bank '
         '`data/b675_corrigenda.txt` appended at rows (5) and (6); it answers b691’s two items after the root, lettered (l) and (m).*', '']
    return NL.join(L)


def bank_lines(s, landed_line=None):
    L = ['b692 -- THE CORRIGENDUM, (R302)(2): b691`S TWO ITEMS AFTER THE ROOT, LETTERED (l) AND (m), ANSWERED BY ONE GENERATED FINDINGS ENTRY IN b678`s FORM',
         '', '### rows are the corrected line and the lines that correct it, each read from its bank by line; the sealed face is not rewritten.', '',
         '  THE FACE`S DECLARATION   relay data/%s :%d | %s' % (FACE, s['decl'][0], s['decl'][1].strip()),
         '  THE LOCK                 relay data/%s :%d | %s' % (FACE, s['lock'][0], s['lock'][1].strip()),
         '  (l) PRE-PUSH             relay data/b691_checks.txt :%d | %s' % (s['pre'][0], s['pre'][1].strip()),
         '  (l) POST-PUSH            relay data/b691_checks_postpush.txt :%d | %s' % (s['post'][0], s['post'][1].strip()),
         '  (l) THE ARM, PRE-PUSH    relay data/b691_checks_standing-a.txt :%d | read %s ; failing %s' % ((s['apre'][0],) + tuple(s['arm_pre'])),
         '  (l) THE ARM, POST-PUSH   relay data/b691_checks_postpush_standing-a.txt :%d | read %s ; failing %s' % ((s['apost'][0],) + tuple(s['arm_post'])),
         '  (l) THE PATTERN          relay tools/rule_arms.py :%d | %s' % (PATTERN_LINE, s['pat']),
         '  (l) THE PARTS            relay data/b691_arms_prerun.txt | %s' % ', '.join(s['parts']),
         '  (m) THE FIRST SUBJECT    PLACE-papers %s | %s' % (OLD, s['so']),
         '  (m) THE PUSHED SUBJECT   PLACE-papers %s | %s' % (NEW, s['sn']),
         '  (m) THE TREE, THE PARENT %s (both), %s (both)' % (s['tree'], s['parent']),
         '  THE COUNT AS IT STANDS   relay data/b691_closing.txt :1 | %s' % s['head'],
         '', '### ### **THE FACE DECLARES G-RULE-ONE-GIT-WRITE ALONE ; (l) G-RULE-SUITE-PARTS FAILS PRE-PUSH AND POST-PUSH, ITS PATTERN AT rule_arms.py :%d ; '
             '(m) %s -> %s, THE TREE UNCHANGED ; THE COUNT %d OF %d ; THE ENTRY AT FINDINGS :%s.**' % (
                 PATTERN_LINE, OLD, NEW, s['count'][0], s['count'][1], landed_line or 'NOT YET WRITTEN')]
    return L


def main(route):
    s = compose()
    text = entry_text(s)
    import b692_record as REC
    if route == 'dry':
        REC.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(bank_lines(s)[-1])
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b692_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b692_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b692_corrigendum.txt')
    open(p + '.tmp', 'wb').write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, decl=s['decl'], lock=s['lock'], pre=s['pre'],
             post=s['post'], arm=dict(pre=s['apre'], post=s['apost']), pattern=s['pat'], parts=s['parts'],
             amend=dict(old=OLD, new=NEW, tree=s['tree'], parent=s['parent']), count=s['count'])
    p = os.path.join(D, 'b692_corrigendum.json')
    open(p + '.tmp', 'wb').write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b692_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
