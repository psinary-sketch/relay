# -*- coding: utf-8 -*-
"""b699_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R309)(2): b698's undeclared failure G-NOTHING-RAN-AHEAD (b698's defect (c)), its
post-root rewrite of the answers bank (defect (d)) and the ONE-COPY figure (defect (a)), answered by one generated FINDINGS entry in b678's
corrigendum form; b698's sealed face (relay data/b698_registration_2026-10-21.txt) and every root-named bank unedited.

### Carried from tools/b695_corrigendum.py, the last successor that ran, on the author's answer to b699's citation miss 2 (b698 ran no
### corrigendum tool; data/b699_author_answers.txt). b678's tool (tools/b678_corrigendum.py) is IMPORTED and unchanged: its reader `rd`; its
### form -- one generated entry, each line it corrects quoted with its place, the corrected reading and its source, the figures read from
### their banks and checked before any write, `dry` then `land` -- carried as b689-b695 carried it. Every figure is read, none typed:
###   the face: relay data/b698_registration_2026-10-21.txt, section (0)'s head, the Component 5 line naming the late commits in words, the
###             line declaring the arms failing on real state, and the lock time the arm reads;
###   (c): the counts in data/b698_checks.txt and data/b698_checks_postpush.txt; the arm's line in the two standing-a banks; the arm's test at
###        tools/b698_checks.py; the arm's reading RECOMPUTED here as it reads -- every relay and PLACE-papers commit from the act's start to the
###        pre-push HEAD, timed at or before the lock, whose first seven characters the face does not carry; data/b698_defects.txt (c);
###   (d): the root bank's row for data/b698_author_answers.json (data/b698_act_root.json, its sha256 and its time), the file's sha256 now and
###        its blob's at HEAD, its write time; data/act_roots.txt's b698 line; data/b698_defects.txt (d);
###   (a): the one-table roster's stored field (data/b698_roster_simplicity.json) and the counting route's bank (data/b698_onecopy.txt :61);
###        data/b698_defects.txt (a).
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b699_record's
### guarded landing, data/b699_corrigendum.txt (.json). Written by the Write tool at b699; it writes those two banks and the one FINDINGS entry.
"""
import calendar
import hashlib
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
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b678_corrigendum as C78   # noqa: E402  ### b678's tool, imported unchanged: rd
from b652_record import conv     # noqa: E402  ### the one conversion
import b699_worklist as K         # noqa: E402

TITLE = ('## Corrigendum to b698’s face and closing record (relay data/b698_registration_2026-10-21.txt, data/b698_closing.txt): '
         'G-NOTHING-RAN-AHEAD failing undeclared; the answers bank rewritten after the root; the ONE-COPY figure')
PP = K.PP
PRE = dict(relay='dcce6eed', pp='f5a4a6e')            # ### b698's starting mains (tools/b698_worklist.py :16-:17)
PREPUSH = dict(relay='f19eccc4', pp='1a8d8d1')        # ### the HEADs the pre-push suite read (data/b698_closing.txt :1)
ANS = 'data/b698_author_answers.json'


def at(path, pred):
    return [(i + 1, l) for i, l in enumerate(C78.rd(path).split(NL)) if pred(l)]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def iso(e):
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(e))


def compose():
    face = os.path.join(ROOT, *K.B698_FACE.split('/'))
    ft = C78.rd(face)
    f0 = at(face, lambda l: 'WHAT RAN AHEAD OF THIS SEAL, DECLARED' in l)
    f5 = at(face, lambda l: 'COMPONENT 5 BEFORE THIS SEAL:** relay 50986eb' in l)
    fd = at(face, lambda l: 'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:** NONE.' in l)
    lk = re.search(r'locked at \(UTC\)[^0-9]*(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', ft)
    lock = calendar.timegm(time.strptime(lk.group(1), '%Y-%m-%dT%H:%M:%SZ')) if lk else None
    want = "ARMS RUN : 123. ### LIVE PASSING : 122. ### LIVE FAILING : 1 ['G-NOTHING-RAN-AHEAD']"
    cpre = at(os.path.join(D, 'b698_checks.txt'), lambda l: want in l)
    cpost = at(os.path.join(D, 'b698_checks_postpush.txt'), lambda l: want in l)
    apre = at(os.path.join(D, 'b698_checks_standing-a.txt'), lambda l: l.startswith('  G-NOTHING-RAN-AHEAD') and 'FAIL' in l)
    apost = at(os.path.join(D, 'b698_checks_postpush_standing-a.txt'), lambda l: l.startswith('  G-NOTHING-RAN-AHEAD') and 'FAIL' in l)
    test = at(os.path.join(T, 'b698_checks.py'), lambda l: "all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch'])" in l)
    miss, seen = [], 0
    for repo, k in ((ROOT, 'relay'), (PP, 'pp')):
        for l in git(repo, 'log', '--reverse', '--format=%H %ct %s', '%s..%s' % (PRE[k], PREPUSH[k])).split(NL):
            if not l.strip():
                continue
            h, ct, s = l.split(' ', 2)
            if lock is not None and int(ct) <= lock:
                seen += 1
                if h[:7] not in ft:
                    miss.append(dict(repo=k, hash=h, time=iso(int(ct)), subject=s))
    dc = at(os.path.join(D, 'b698_defects.txt'), lambda l: l.startswith("    (c) THE SEAT'S"))
    dd = at(os.path.join(D, 'b698_defects.txt'), lambda l: l.startswith("    (d) THE SEAT'S"))
    da = at(os.path.join(D, 'b698_defects.txt'), lambda l: l.startswith("    (a) THE SEAT'S"))
    rj = json.loads(C78.rd(os.path.join(D, 'b698_act_root.json')))
    rrow = at(os.path.join(D, 'b698_act_root.json'), lambda l: l.strip().startswith('"%s ' % ANS))
    rsha = rrow[0][1].strip().strip('",').split(' ')[1] if len(rrow) == 1 else None
    now = hashlib.sha256(open(os.path.join(ROOT, *ANS.split('/')), 'rb').read()).hexdigest()
    blob = hashlib.sha256(subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:' + ANS], capture_output=True).stdout).hexdigest()
    last = git(ROOT, 'log', '-1', '--format=%h %cI', '--', ANS).strip()
    mtime = iso(int(os.path.getmtime(os.path.join(ROOT, *ANS.split('/')))))
    rline = at(os.path.join(D, 'act_roots.txt'), lambda l: l.startswith('b698 '))
    roster = at(os.path.join(D, 'b698_roster_simplicity.json'), lambda l: '"partner_lines_differing": 6' in l)
    oc = at(os.path.join(D, 'b698_onecopy.txt'), lambda l: 'THE TWO TABLES DIFFER IN 18 LINES (the generator`s reading: 6)' in l)
    ok = all(len(x) == 1 for x in (f0, f5, fd, cpre, cpost, apre, apost, test, dc, dd, da, rrow, rline, roster, oc)) and lock is not None \
        and [m['hash'][:7] for m in miss] == ['2d19edd', '069778f'] and rsha == now == blob and rj.get('root', '').startswith('1db80825') \
        and rline[0][1].split()[1] == rj['root'] and mtime > rj.get('at', '')
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ (face %d/%d/%d, lock %s, counts %d/%d, arm %d/%d, test %d, missing %s, defects %d/%d/%d, root row %d, '
                 'sha root %s now %s blob %s, mtime %s root at %s, roster %d, onecopy %d) -- NOTHING WRITTEN' % (
                     len(f0), len(f5), len(fd), lk and lk.group(1), len(cpre), len(cpost), len(apre), len(apost), len(test),
                     [m['hash'][:7] for m in miss], len(dc), len(dd), len(da), len(rrow), (rsha or '')[:12], now[:12], blob[:12], mtime,
                     rj.get('at'), len(roster), len(oc)))
    return dict(f0=f0[0][0], f5=f5[0][0], fd=fd[0], lock=lk.group(1), seen=seen, cpre=cpre[0][0], cpost=cpost[0][0], apre=apre[0][0],
                apost=apost[0][0], test=test[0][0], miss=miss, dc=dc[0][0], dd=dd[0][0], da=da[0][0], rrow=rrow[0][0], sha=now, last=last,
                mtime=mtime, root=rj['root'], root_at=rj['at'], rline=rline[0][0], roster=roster[0][0], oc=oc[0][0])


def entry_text(s):
    m1, m2 = s['miss']
    L = ['', TITLE, '',
         'b698’s face, sealed before any of this, declares at its line :%d no arm failing on real state (“BY NAME:** NONE”). One arm failed after '
         'the seal, undeclared: the pre-push suite and the post-push suite each read 122 of 123, G-NOTHING-RAN-AHEAD failing (relay '
         'data/b698_checks.txt :%d, data/b698_checks_postpush.txt :%d; the arm’s line in data/b698_checks_standing-a.txt :%d and '
         'data/b698_checks_postpush_standing-a.txt :%d), the count b698’s closing record carries at its line :1 (“suite 122 of 123”).' % (
             s['fd'][0], s['cpre'], s['cpost'], s['apre'], s['apost']), '',
         '**G-NOTHING-RAN-AHEAD** (b698’s defect (c), relay data/b698_defects.txt :%d). The arm reads every relay and PLACE-papers commit of the '
         'act timed at or before the lock (%s, the face’s own line) and wants its hash’s first seven characters on the face (relay '
         'tools/b698_checks.py :%d). Read as the arm reads them, %d commits stand before the lock and two are not on the face by hash: relay `%s` '
         '(%s, “%s”) and relay `%s` (%s, “%s”). Section (0) (the face’s :%d) names them in words alone, its Component 5 line (:%d) listing the '
         'suite, the gate, the spec, the closing and the face, then the pre-run’s six parts, with no hash beside either: the face was written '
         'before either commit and not re-read for their hashes before the lock.' % (
             s['dc'], s['lock'], s['test'], s['seen'], m1['hash'][:8], m1['time'], m1['subject'].split(';')[0], m2['hash'][:8], m2['time'],
             m2['subject'].split(';')[0], s['f0'], s['f5']), '',
         '**The answers bank after the root** (b698’s defect (d), relay data/b698_defects.txt :%d), an event against the rule that no named bank is '
         'written after the root. The record tool’s answers route, re-run after the post-push suite, rewrote data/b698_author_answers.json’s '
         'timestamp line; the line was restored by the Edit tool. Its bytes now are its committed bytes: sha256 %s, equal to the blob at HEAD '
         '(last written by relay %s) and to the row the root bank carries for it (relay data/b698_act_root.json :%d). The root is unchanged '
         '-- %s (data/act_roots.txt :%d), computed at %s; the file’s write time, %s, stands after the root’s.' % (
             s['dd'], s['sha'][:16], s['last'].split()[0], s['rrow'], s['root'][:16], s['rline'], s['root_at'], s['mtime']), '',
         '**The ONE-COPY figure** (b698’s defect (a), relay data/b698_defects.txt :%d). b698’s stale-cell prompt and its generator’s print carried '
         '6 lines differing between SIMPLICITY_OF_RIEMANN_ZEROS.md and its partner copy -- the roster field partner_lines_differing stored at b672 '
         '(relay data/b698_roster_simplicity.json :%d), not a count. Counted line by line by the generator’s own table finder: 18 '
         '(data/b698_onecopy.txt :%d), the figure entered beneath W-ORD-ONE-COPY (OPEN_TRAILS :%d).' % (
             s['da'], s['roster'], s['oc'], K.B698_ONECOPY_LINE), '',
         'The sealed face and every root-named bank are not edited -- this entry is their correction. Nothing here proves RH or GRH.', '',
         '*Filed at b699 on the author’s ruling `(R309)`(2): generated by relay `tools/b699_corrigendum.py`, carried from '
         '`tools/b695_corrigendum.py` on the author’s answer, in the corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported '
         'unchanged), banked as relay `data/b699_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at rows (11) to (13); '
         'it answers b698’s defects (c), (d) and (a).*', '']
    return NL.join(L)


def bank_lines(s, landed_line=None):
    m1, m2 = s['miss']
    return ['b699 -- THE CORRIGENDUM, (R309)(2): b698`S UNDECLARED FAILURE, ITS POST-ROOT REWRITE AND THE ONE-COPY FIGURE, ITS DEFECTS (c), (d) AND (a), '
            'ANSWERED BY ONE GENERATED FINDINGS ENTRY IN b678`s FORM', '',
            '### rows are the corrected lines and the lines that correct them, each read from its bank by line; the face and the root-named banks '
            'are not rewritten.', '',
            '  THE FACE                relay %s :%d | %s' % (K.B698_FACE, s['fd'][0], s['fd'][1].strip()),
            '  SECTION (0)             relay %s :%d (its head), :%d (Component 5, the late commits in words) ; locked at (UTC) %s' % (
                K.B698_FACE, s['f0'], s['f5'], s['lock']),
            '  THE COUNTS              relay data/b698_checks.txt :%d ; data/b698_checks_postpush.txt :%d | 122 of 123 ; 122 of 123' % (s['cpre'], s['cpost']),
            '  (c) THE ARM             relay data/b698_checks_standing-a.txt :%d ; data/b698_checks_postpush_standing-a.txt :%d' % (s['apre'], s['apost']),
            '  (c) THE TEST            relay tools/b698_checks.py :%d | every commit at or before the lock by its hash`s first seven characters' % s['test'],
            '  (c) AS THE ARM READS    %d commits before the lock ; on the face by hash %d ; not %d' % (s['seen'], s['seen'] - 2, 2),
            '  (c) NOT BY HASH 1       relay %s | %s | %s' % (m1['hash'], m1['time'], m1['subject']),
            '  (c) NOT BY HASH 2       relay %s | %s | %s' % (m2['hash'], m2['time'], m2['subject']),
            '  (c) THE DEFECT          relay data/b698_defects.txt :%d' % s['dc'],
            '  (d) THE BANK            relay data/b698_author_answers.json | sha256 now %s ; at HEAD equal ; last written by relay %s' % (s['sha'], s['last']),
            '  (d) THE ROOT`S ROW      relay data/b698_act_root.json :%d | the same sha256' % s['rrow'],
            '  (d) THE ROOT            relay data/act_roots.txt :%d | %s, computed at %s ; UNCHANGED' % (s['rline'], s['root'], s['root_at']),
            '  (d) THE WRITE TIME      %s, after the root`s' % s['mtime'],
            '  (d) THE DEFECT          relay data/b698_defects.txt :%d' % s['dd'],
            '  (a) AS STORED           relay data/b698_roster_simplicity.json :%d | partner_lines_differing 6 (b672`s field)' % s['roster'],
            '  (a) AS COUNTED          relay data/b698_onecopy.txt :%d | 18 lines' % s['oc'],
            '  (a) THE DEFECT          relay data/b698_defects.txt :%d' % s['da'],
            '', '### ### **ONE ARM FAILING AFTER b698`S SEAL, UNDECLARED, BY ITS TWO COMMITS ; THE ANSWERS BANK`S BYTES EQUAL TO THE ROOT`S ROW, THE '
            'ROOT UNCHANGED ; THE ONE-COPY FIGURE 6 AS STORED, 18 AS COUNTED ; THE FACE AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS '
            ':%s.**' % (landed_line or 'NOT YET WRITTEN')]


def main(route):
    s = compose()
    text = entry_text(s)
    import b699_record as REC
    if route == 'dry':
        REC.R.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b699_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b699_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b699_corrigendum.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, lock=s['lock'], missing=s['miss'],
             answers=dict(sha256=s['sha'], last=s['last'], mtime=s['mtime'], root=s['root'], root_at=s['root_at']), onecopy=dict(stored=6, counted=18))
    p = os.path.join(D, 'b699_corrigendum.json')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b699_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
