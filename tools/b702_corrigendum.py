# -*- coding: utf-8 -*-
"""b702_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R312)(2): b701's two suite failures undeclared on its face (G-READ-RULE, G-ACTROOT-LAST),
its four un-lettered items lettered (h)-(k), and its trail's Resolved line's miscount corrected, answered by one generated FINDINGS entry in
b678's corrigendum form; b701's sealed face (relay data/b701_registration_2026-10-21.txt), its trail record (PLACE-papers OPEN_TRAILS :15412)
and every root-named bank unedited.

### Carried from tools/b700_corrigendum.py (itself b699's successor), its rows rewritten for b701's record. b678's tool
### (tools/b678_corrigendum.py) is IMPORTED and unchanged: its reader `rd`; its form -- one generated entry, each line it corrects quoted with
### its place, the corrected reading and its source, the figures read from their banks and checked before any write, `dry` then `land`.
### Every figure is read, none typed:
###   the failures: data/b701_checks.txt :11 and data/b701_checks_postpush.txt :11 (the combined verdict lines), the face's declaration line
###       ("BY NAME:** NONE."), the commits that declared them (relay 17e1b5c6, 2ab9ff3c, 613847d6, their subjects read from the log);
###   (h) the fourth whole read: data/b701_read_calls.txt :54 (the transcript line, the time, the file's lines);
###   (i) the diagnostic with a redirect and a pipe: this session's transcript, the one Bash call carrying it (its timestamp), after b701's
###       root (data/b701_act_root.json "at") and after b701's command bank's write at the root step (data/b701_commands.txt, REDIRECTS 1);
###   (j) the per-part seconds banks rewritten after the root: tools/b701_checks.py :1782-:1786 (no guard) against tools/b700_checks.py :1669
###       (`if PRERUN:`), the six banks' "at" against the root's, data/b701_checks_postpush.txt :107 (G-ACTROOT-LAST FAIL);
###   (k) the Resolved line: OPEN_TRAILS :15436 ("the three navigator misses and the seat's six defects") against data/b701_defects.txt's
###       owners read by tools/b702_record.py's reader (navigator 2, seat 5).
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b702_record's
### guarded landing, data/b702_corrigendum.txt (.json). Written by the Write tool at b702; it writes those two banks and the one FINDINGS entry.
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
import b702_worklist as K         # noqa: E402
import b702_record as REC         # noqa: E402  ### the repaired reader and the guarded landing

TITLE = ('## Corrigendum to b701’s face, trail and closing record (relay data/b701_registration_2026-10-21.txt, PLACE-papers OPEN_TRAILS '
         ':15412, relay data/b701_closing.txt): two suite failures undeclared, four items un-lettered, the trail’s Resolved line')
PP = K.PP
OT = os.path.join(PP, 'OPEN_TRAILS.md')
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
DIAG = 'git -C /d/relay log -1 --format=%s 2f0b3f5 2>&1 | head -c 0'


def at(path, pred, lo=0, hi=None):
    L = C78.rd(path).split(NL)
    return [(i + 1, l) for i, l in enumerate(L) if lo <= i < (hi if hi is not None else len(L)) and pred(l)]


def subject(h):
    return REC.g(ROOT, 'log', '-1', '--format=%s', h).strip()


def compose():
    ot = C78.rd(OT).split(NL)
    head = K.B701_TRAIL
    if not ot[head - 1].startswith('### b701 '):
        sys.exit('### OPEN_TRAILS :%d IS NOT b701`S TRAIL -- NOTHING WRITTEN' % head)
    end = next((i for i in range(head, len(ot)) if ot[i].startswith('### b')), len(ot))
    rl = [(i + 1, ot[i]) for i in range(head - 1, end) if ot[i].startswith('**Resolved by the seat')]
    dl = [(i + 1, ot[i]) for i in range(head - 1, end) if ot[i].startswith('**Defects** (relay data/b701_defects.txt):')]
    seven = REC._defect_short('b701')
    owners = [('NAVIGATOR' if "THE NAVIGATOR'S" in r else 'SEAT' if "THE SEAT'S" in r else '?') for r in seven]
    nav, seat = owners.count('NAVIGATOR'), owners.count('SEAT')
    mis = 'the three navigator misses and the seat’s six defects as lettered' in (rl[0][1] if rl else '')
    ck = at(os.path.join(D, 'b701_checks.txt'), lambda l: 'ARMS RUN : 123. ### LIVE PASSING : 122. ### LIVE FAILING : 1 [\'G-READ-RULE\']' in l)
    cp = at(os.path.join(D, 'b701_checks_postpush.txt'), lambda l: "ARMS RUN : 123. ### LIVE PASSING : 121. ### LIVE FAILING : 2 ['G-ACTROOT-LAST', 'G-READ-RULE']" in l)
    cpl = at(os.path.join(D, 'b701_checks_postpush.txt'), lambda l: l.startswith('  G-ACTROOT-LAST ') and '### FAILS' in l)
    fc = at(os.path.join(ROOT, *K.B701_FACE.split('/')), lambda l: 'DECLARED BEFORE THE LOCK, BY NAME:** NONE.' in l)
    rc = at(os.path.join(D, 'b701_read_calls.txt'), lambda l: '### AN OFFENCE' in l and 'audit_b701_reg_satisfiable.txt' in l)
    rm = re.match(r'^  (\d+) \| (\S+) \| (\d+) \| ### AN OFFENCE \| (.*)$', rc[0][1]) if len(rc) == 1 else None
    rcount = at(os.path.join(D, 'b701_read_calls.txt'), lambda l: 'WHOLE OF A FILE OF 200 LINES OR MORE 4' in l)
    cb = C78.rd(os.path.join(D, 'b701_commands.txt'))
    cmd_ok = 'REDIRECTS OF ANY STREAM 1' in cb and 'head -c 0' not in cb
    cb_at = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', cb.split(NL)[0] if cb else '')
    rj = json.loads(C78.rd(os.path.join(D, 'b701_act_root.json')))
    root_at = rj.get('at') or ''
    # ### (i) the diagnostic: the one assistant line of this session carrying it, read by its timestamp field
    diag = []
    needle = '"command":"' + DIAG   # ### the Bash call itself, not a later line that quotes the command (this tool's own write among them)
    for i, l in enumerate(C78.rd(SESSION).split(NL), 1):
        if needle in l and '"type":"assistant"' in l:
            m = re.search(r'"timestamp":"(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)\.\d+Z"', l)
            diag.append((i, m.group(1) + 'Z' if m else ''))
    c1 = C78.rd(os.path.join(T, 'b701_checks.py')).split(NL)
    c0 = C78.rd(os.path.join(T, 'b700_checks.py')).split(NL)
    guard_gone = 'b701_arm_seconds_%s.json' in c1[1781] and c1[1780].strip() != 'if PRERUN:'
    guard_was = c0[1668].strip() == 'if PRERUN:' and 'b700_arm_seconds_%s.json' in c0[1672]
    secs = []
    for p in K.PARTS:
        j = json.loads(C78.rd(os.path.join(D, 'b701_arm_seconds_%s.json' % p)) or '{}')
        secs.append((p, j.get('at') or ''))
    later = all(a > root_at for _p, a in secs)
    subs = dict((h, subject(h)) for h in ('17e1b5c6', '2ab9ff3c', '613847d6'))
    decl = ('G-READ-RULE reads the offence un-entered' in subs['17e1b5c6'] and 'REWROTE the six root-named banks' in subs['2ab9ff3c']
            and 'G-ACTROOT-LAST' in subs['613847d6'])
    tr = at(os.path.join(D, 'b701_tool_repairs.txt'), lambda l: 'REPAIRS 9 ;' in l)
    cg = at(os.path.join(D, 'b675_corrigenda.txt'), lambda l: l.startswith('  (16) '))
    cg17 = at(os.path.join(D, 'b675_corrigenda.txt'), lambda l: l.startswith('  (17) '))
    ok = (len(rl) == 1 and len(dl) == 1 and len(seven) == 7 and (nav, seat) == (2, 5) and mis and len(ck) == 1 and len(cp) == 1 and len(cpl) == 1
          and len(fc) == 1 and rm is not None and rm.group(3) == '219' and len(rcount) == 1 and cmd_ok and cb_at and cb_at.group(1) > root_at
          and len(diag) == 1 and diag[0][1] > cb_at.group(1) and guard_gone and guard_was and later and decl and len(tr) == 1 and len(cg) == 1)
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ (Resolved %d, Defects %d, rows %d, owners %s, miscount %s, checks %d/%d/%d, face %d, read %s, count %d, '
                 'commands %s at %s, root at %s, diag %s, guard gone %s was %s, seconds later %s, declared %s, repairs %d, corrigenda (16) %d) -- NOTHING WRITTEN' % (
                     len(rl), len(dl), len(seven), (nav, seat), mis, len(ck), len(cp), len(cpl), len(fc), rm and rm.groups(), len(rcount), cmd_ok,
                     cb_at and cb_at.group(1), root_at, diag, guard_gone, guard_was, later, decl, len(tr), len(cg)))
    return dict(head=head, rl=rl[0], dl=dl[0], seven=seven, nav=nav, seat=seat, ck=ck[0][0], cp=cp[0][0], cpl=cpl[0][0], fc=fc[0][0], rc=rc[0][0],
                rm=rm.groups(), rcount=rcount[0][0], cb_at=cb_at.group(1), root_at=root_at, diag=diag[0], secs=secs, subs=subs, tr=tr[0][0], cg=cg[0][0],
                cg17=bool(cg17))


def entry_text(s):
    L = ['', TITLE, '',
         'b701’s face, sealed before its suite ran, declares no carried failure (relay data/b701_registration_2026-10-21.txt :%d, “THE ARMS '
         'FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME: NONE”); its pre-push suite read 122 of 123 and its post-push suite '
         '121 of 123 (relay data/b701_checks.txt :%d; data/b701_checks_postpush.txt :%d), each failure declared in a commit’s subject alone (relay '
         '17e1b5c6, 2ab9ff3c, 613847d6). This entry declares them, letters the four items the act left un-lettered, and corrects the trail’s '
         'Resolved line; the face, the trail record and every root-named bank are not edited.' % (s['fc'], s['ck'], s['cp']), '',
         '**The two undeclared failures, each with its cause by line.** G-READ-RULE: one whole read of a file of two hundred lines or more after '
         'the defects bank was committed and before the lock -- relay data/audit_b701_reg_satisfiable.txt, 219 lines, read with a limit and no '
         'offset at transcript line %s (%s; data/b701_read_calls.txt :%d, the bank’s count :%d) -- entered by no lettered row, so the arm read it '
         'un-entered pre-push and post-push. G-ACTROOT-LAST: the sealed suite tool carried b700’s per-part seconds writer without its guard '
         '(tools/b701_checks.py :1782-:1786 against tools/b700_checks.py :1669, `if PRERUN:`), so the pre-push run rewrote the six root-named '
         'banks data/b701_arm_seconds_<part>.json after the root (the root at %s, relay data/b701_act_root.json; the banks at %s), and the '
         'post-push run read their write times after the root’s (data/b701_checks_postpush.txt :%d).' % (
             s['rm'][0], s['rm'][1], s['rc'], s['rcount'], s['root_at'], ', '.join('%s %s' % x for x in s['secs']), s['cpl']), '',
         '**The four items, lettered (h)-(k) in continuation of data/b701_defects.txt’s (a)-(g).** (h) THE SEAT’S: A FOURTH WHOLE READ OF A LONG '
         'FILE, NOT LETTERED -- the read above, at transcript line %s (data/b701_read_calls.txt :%d). (i) THE SEAT’S: A REDIRECT AND A PIPE INTO A '
         'SHELL FILTER IN ONE DIAGNOSTIC AFTER THE ROOT -- the command “%s” at transcript line %d (%s), after the root (%s) and after the '
         'command bank’s last write (data/b701_commands.txt, written %s at the root step: REDIRECTS OF ANY STREAM 1, the one of defect (c); this '
         'command is not in it and stands in b702’s capture of the previous act’s window). (j) THE SEAT’S: THE CARRIED SUITE’S PER-PART SECONDS WRITE WITHOUT b700’S '
         'GUARD, SIX ROOT-NAMED BANKS REWRITTEN AFTER THE ROOT -- the cause and the banks above; the guard restored at b702’s carry (relay '
         'data/b702_tool_repairs.txt, row (1)). (k) THE SEAT’S: THE TRAIL’S RESOLVED LINE MISCOUNTING THE DEFECTS -- below.' % (
             s['rm'][0], s['rc'], DIAG, s['diag'][0], s['diag'][1], s['root_at'], s['cb_at']), '',
         '**The Resolved line, corrected.** OPEN_TRAILS :%d reads at its (7) “the three navigator misses and the seat’s six defects as lettered”; '
         'the bank (data/b701_defects.txt, its rows read by b702’s record tool with the act passed at the call) letters seven: %s -- the '
         'navigator’s %d ((d), (e)), the seat’s %d. The line is not edited; the figures of record are two and five.' % (
             s['rl'][0], '; '.join(s['seven']), s['nav'], s['seat']), '',
         'The sealed face, the trail record and every root-named bank are not edited -- this entry is their correction. Nothing here proves RH '
         'or GRH.', '',
         '*Filed at b702 on the author’s ruling `(R312)`(2): generated by relay `tools/b702_corrigendum.py`, carried from '
         '`tools/b700_corrigendum.py`, in the corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), banked as '
         'relay `data/b702_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at rows (17) to (21); it answers b701’s two '
         'undeclared failures, its four un-lettered items and its trail’s Resolved line.*', '']
    return NL.join(L)


def bank_lines(s, landed_line=None):
    return ['b702 -- THE CORRIGENDUM, (R312)(2): b701`S TWO UNDECLARED SUITE FAILURES, ITS FOUR UN-LETTERED ITEMS (h)-(k) AND ITS TRAIL`S RESOLVED '
            'LINE, ANSWERED BY ONE GENERATED FINDINGS ENTRY IN b678`s FORM', '',
            '### rows are the corrected lines and the lines that correct them, each read from its bank by line; the face, the trail and the '
            'root-named banks are not rewritten.', '',
            '  THE FACE                relay %s :%d | DECLARED BEFORE THE LOCK, BY NAME: NONE' % (K.B701_FACE, s['fc']),
            '  THE SUITE               relay data/b701_checks.txt :%d (122 of 123, G-READ-RULE) ; data/b701_checks_postpush.txt :%d (121 of 123, G-ACTROOT-LAST, G-READ-RULE)' % (s['ck'], s['cp']),
            '  DECLARED IN COMMITS     relay 17e1b5c6 | %s' % s['subs']['17e1b5c6'][:120],
            '                          relay 2ab9ff3c | %s' % s['subs']['2ab9ff3c'][:120],
            '                          relay 613847d6 | %s' % s['subs']['613847d6'][:120],
            '  (h) THE WHOLE READ      relay data/b701_read_calls.txt :%d | transcript line %s at %s, %s lines, %s' % ((s['rc'],) + s['rm'][:4]),
            '  (i) THE DIAGNOSTIC      this session`s transcript line %d at %s | %s ; after the root at %s ; the command bank written %s (REDIRECTS OF ANY STREAM 1, not this one)' % (
                s['diag'][0], s['diag'][1], DIAG, s['root_at'], s['cb_at']),
            '  (j) THE GUARD           relay tools/b701_checks.py :1782-:1786 (the write, unguarded) ; tools/b700_checks.py :1669 (`if PRERUN:`) ; the banks` writes: %s ; '
            'data/b701_checks_postpush.txt :%d (G-ACTROOT-LAST FAIL) ; restored at b702 (data/b702_tool_repairs.txt row (1))' % (', '.join('%s %s' % x for x in s['secs']), s['cpl']),
            '  (k) THE RESOLVED LINE   PLACE-papers OPEN_TRAILS.md :%d | (7) "the three navigator misses and the seat`s six defects" ; the bank: navigator %d, seat %d' % (
                s['rl'][0], s['nav'], s['seat']),
            '  THE DEFECTS LINE        PLACE-papers OPEN_TRAILS.md :%d | equal to the bank`s seven rows (unchanged by this entry)' % s['dl'][0],
            '  THE REPAIRS BANK        relay data/b701_tool_repairs.txt :%d (REPAIRS 9)' % s['tr'],
            '  THE CORRIGENDA BANK     relay data/b675_corrigenda.txt :%d (row (16) the last before this act) ; rows (17)-(21) appended by this act' % s['cg'],
            '', '### ### **TWO FAILURES DECLARED HERE (G-READ-RULE, G-ACTROOT-LAST) ; FOUR ITEMS LETTERED (h)-(k) ; THE RESOLVED LINE`S COUNTS CORRECTED TO '
            '2 AND 5 ; THE FACE, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (landed_line or 'NOT YET WRITTEN')]


def main(route):
    s = compose()
    text = entry_text(s)
    if route == 'dry':
        REC.R.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b702_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b702_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b702_corrigendum.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, resolved_line=s['rl'][0], defects_line=s['dl'][0],
             failures=['G-READ-RULE', 'G-ACTROOT-LAST'], lettered=['h', 'i', 'j', 'k'], owners=dict(navigator=s['nav'], seat=s['seat']),
             diag=dict(line=s['diag'][0], at=s['diag'][1]), read=dict(line=s['rm'][0], at=s['rm'][1]), root_at=s['root_at'],
             seconds=[list(x) for x in s['secs']])
    p = os.path.join(D, 'b702_corrigendum.json')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b702_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
