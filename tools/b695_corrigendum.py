# -*- coding: utf-8 -*-
"""b695_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R305)(2): b694's two post-seal suite failures, undeclared on its face --
G-RULE-BINARY-HASHES (b694's defect (k)) and G-RULE-ONE-GIT-WRITE (b694's defect (l)) -- answered by one generated FINDINGS entry in b678's
corrigendum form; b694's sealed face (relay data/b694_registration_2026-10-20.txt) and the root-named hashes bank unedited.

### b678's tool (tools/b678_corrigendum.py) is IMPORTED and unchanged: its reader `rd`; its form -- one generated entry, each line it corrects
### quoted with its place, the corrected reading and its source, the figures read from their banks and checked before any write, `dry` then
### `land` -- is carried, as b689-b694 carried it. Every figure is read, none typed:
###   the face: relay data/b694_registration_2026-10-20.txt, the line declaring the arms failing on real state;
###   the counts: data/b694_checks.txt and data/b694_checks_postpush.txt, the ARMS RUN line;
###   (k): the arm's line in data/b694_checks_standing-a.txt and data/b694_checks_postpush_standing-a.txt; the hashes bank's path row
###        (relay data/b694_circuit_SIDE-lv-conservation_v0.13.0_png_hashes.txt); the PNG's own path and sha256 read from the file; the arm's
###        test at tools/rule_arms.py (`carried_by=`); data/b694_defects.txt (k);
###   (l): the arm's line in data/b694_checks_postpush_standing-a.txt; the message it names, read from the session transcript (its tool uses,
###        their commands and the timestamps of their lines); the read-backs in data/b694_relay_push_out.txt and data/b694_pp_push_out.txt;
###        data/b694_defects.txt (l); data/b692_rules.txt row (1).
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b695_record's
### guarded landing, data/b695_corrigendum.txt (.json). Written by the Write tool at b695; it writes those two banks and the one FINDINGS entry.
"""
import hashlib
import io
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
import b695_worklist as K         # noqa: E402

TITLE = ('## Corrigendum to b694’s face and closing record (relay data/b694_registration_2026-10-20.txt, data/b694_closing.txt): two arms '
         'failing after the seal, undeclared -- G-RULE-BINARY-HASHES and G-RULE-ONE-GIT-WRITE')
HB = 'b694_circuit_SIDE-lv-conservation_v0.13.0_png_hashes.txt'
PNG = 'data/b694_circuit_SIDE-lv-conservation_v0.13.0.png'
READBACK = re.compile(r'^push_gated: main read back at the remote: ([0-9a-f]{40})$')
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID


def at(path, pred):
    return [(i + 1, l) for i, l in enumerate(C78.rd(path).split(NL)) if pred(l)]


def _message(ts):
    """the assistant message whose first line carries the timestamp the arm names: its id, and every tool use under that id with the command
    and the timestamp of its own transcript line."""
    rows = []
    mid = None
    for i, raw in enumerate(io.open(SESSION, encoding='utf-8', errors='replace'), 1):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        m = o.get('message') or {}
        if o.get('type') != 'assistant':
            continue
        if mid is None and o.get('timestamp') == ts:
            mid = m.get('id')
        if mid is not None and m.get('id') == mid:
            for c in m.get('content') or []:
                if isinstance(c, dict) and c.get('type') == 'tool_use':
                    rows.append((i, o.get('timestamp'), (c.get('input') or {}).get('command', '')))
    return mid, rows


def compose():
    face = at(os.path.join(D, 'b694_registration_2026-10-20.txt'), lambda l: 'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED' in l)
    cpre = at(os.path.join(D, 'b694_checks.txt'), lambda l: 'ARMS RUN : 124.' in l)
    cpost = at(os.path.join(D, 'b694_checks_postpush.txt'), lambda l: 'ARMS RUN : 124.' in l)
    kpre = at(os.path.join(D, 'b694_checks_standing-a.txt'), lambda l: l.startswith('  ###   G-RULE-BINARY-HASHES') and 'FAIL' in l)
    kpost = at(os.path.join(D, 'b694_checks_postpush_standing-a.txt'), lambda l: l.startswith('  ###   G-RULE-BINARY-HASHES') and 'FAIL' in l)
    lpost = at(os.path.join(D, 'b694_checks_postpush_standing-a.txt'), lambda l: l.startswith('  ###   G-RULE-ONE-GIT-WRITE') and 'FAIL' in l)
    hrow = at(os.path.join(D, HB), lambda l: l.strip().startswith('data/') and '.png |' in l)
    sha = hashlib.sha256(open(os.path.join(ROOT, *PNG.split('/')), 'rb').read()).hexdigest()
    test = at(os.path.join(T, 'rule_arms.py'), lambda l: 'carried_by=[b for b, t in texts if p in t and sha and sha in t]' in l)
    dk = at(os.path.join(D, 'b694_defects.txt'), lambda l: l.startswith("    (k) THE SEAT'S"))
    dl = at(os.path.join(D, 'b694_defects.txt'), lambda l: l.startswith("    (l) THE SEAT'S"))
    rule = at(os.path.join(D, 'b692_rules.txt'), lambda l: l.startswith('  (1) A COMMIT MADE AFTER THE SEAL THAT FAILS AN ARM IS LEFT AS IT STANDS'))
    rr = at(os.path.join(D, 'b694_relay_push_out.txt'), lambda l: bool(READBACK.match(l)))
    pr = at(os.path.join(D, 'b694_pp_push_out.txt'), lambda l: bool(READBACK.match(l)))
    ts = re.search(r"with more than one \['([^']+)'\]", lpost[0][1]).group(1) if len(lpost) == 1 else None
    mid, uses = _message(ts) if ts else (None, [])
    hpath = hrow[0][1].strip().split(' | ')[0] if len(hrow) == 1 else None
    hsha = hrow[0][1].strip().split(' | ')[1] if len(hrow) == 1 else None
    ok = all(len(x) == 1 for x in (face, cpre, cpost, kpre, kpost, lpost, hrow, test, dk, dl, rule, rr, pr)) and len(uses) == 3 \
        and hsha == sha and hpath != PNG and 'NONE' in face[0][1]
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ (face %d, pre %d, post %d, k %d/%d, l %d, hashes row %d, test %d, (k) %d, (l) %d, rule %d, '
                 'read-backs %d/%d, uses %d, sha equal %s, path %s) -- NOTHING WRITTEN' % (
                     len(face), len(cpre), len(cpost), len(kpre), len(kpost), len(lpost), len(hrow), len(test), len(dk), len(dl), len(rule),
                     len(rr), len(pr), len(uses), hsha == sha, hpath))
    return dict(face=face[0], cpre=cpre[0], cpost=cpost[0], kpre=kpre[0][0], kpost=kpost[0][0], lpost=lpost[0][0], hrow=hrow[0][0],
                hpath=hpath, sha=sha, test=test[0][0], dk=dk[0][0], dl=dl[0][0], rule=rule[0][0], rr=(rr[0][0], READBACK.match(rr[0][1]).group(1)),
                pr=(pr[0][0], READBACK.match(pr[0][1]).group(1)), ts=ts, mid=mid, uses=uses)


def _cmd(c):
    m = re.match(r'^PUSH_GATED_LOG=/d/relay/(data/\S+) bash /d/relay/tools/push_gated\.sh (\S+) (\S+)$', c.strip())
    return 'push_gated.sh %s %s (capture %s)' % (m.group(2), m.group(3), m.group(1)) if m else c.strip()


def entry_text(s):
    u = s['uses']
    L = ['', TITLE, '',
         'b694’s face, sealed before any of this, declares at its line :%d no arm failing on real state (“BY NAME:** NONE”). Two arms failed after '
         'the seal, neither declared: the pre-push suite read 123 of 124 and the post-push suite 122 of 124 (relay data/b694_checks.txt :%d, '
         'data/b694_checks_postpush.txt :%d), the count b694’s closing record carries at its line :1 (“suite 122 of 124”).' % (
             s['face'][0], s['cpre'][0], s['cpost'][0]), '',
         '**G-RULE-BINARY-HASHES** (b694’s defect (k), relay data/b694_defects.txt :%d), failing before and after the push (data/b694_checks_standing-a.txt '
         ':%d, data/b694_checks_postpush_standing-a.txt :%d). The circuit figure’s hashes bank, a root-named text bank, names the PNG at its line :%d '
         'as `%s`; the file stands as `%s`, sha256 %s, the same sha256 the row carries. The arm reads a binary bank as carried only where a text bank '
         'of its act names the file’s own path beside its sha256 (relay tools/rule_arms.py :%d); the path as written is b692’s, so the arm finds no '
         'carrier. The cause: the record tool’s wrapper over relay tools/circuit_read.py renamed the reader’s banks to b694’s and not the paths the '
         'reader writes inside a row. The row as it should read: `%s | %s`.' % (
             s['dk'], s['kpre'], s['kpost'], s['hrow'], s['hpath'], PNG, s['sha'], s['test'], PNG, s['sha']), '',
         '**G-RULE-ONE-GIT-WRITE** (b694’s defect (l), relay data/b694_defects.txt :%d), failing after the push (data/b694_checks_postpush_standing-a.txt '
         ':%d), the message at %s named. Three git writes went as three parallel calls in that one message: %s at %s; %s at %s; %s at %s. All three '
         'landed and were read back -- relay main %s (data/b694_relay_push_out.txt :%d), PLACE-papers main %s (data/b694_pp_push_out.txt :%d) -- and '
         'no commit was amended, rebased or rewritten; every later git write went alone in its own message. As relay data/b692_rules.txt :%d orders '
         'for a commit made after the seal that fails an arm, the commits were left as they stand and the failure entered: this entry is the rule’s '
         'test, read for the record.' % (
             s['dl'], s['lpost'], s['ts'], '`%s`' % _cmd(u[0][2]), u[0][1], '`%s`' % _cmd(u[1][2]), u[1][1], '`%s`' % _cmd(u[2][2]), u[2][1],
             s['rr'][1][:8], s['rr'][0], s['pr'][1][:7], s['pr'][0], s['rule']), '',
         'The sealed face and the root-named hashes bank are not edited -- this entry is their correction. Nothing here proves RH or GRH.', '',
         '*Filed at b695 on the author’s ruling `(R305)`(2): generated by relay `tools/b695_corrigendum.py` in the corrigendum form of relay '
         '`tools/b678_corrigendum.py` (its reader imported unchanged), banked as relay `data/b695_corrigendum.txt`, the corrigenda bank '
         '`data/b675_corrigenda.txt` appended at rows (9) and (10); it answers b694’s defects (k) and (l).*', '']
    return NL.join(L)


def bank_lines(s, landed_line=None):
    u = s['uses']
    return (['b695 -- THE CORRIGENDUM, (R305)(2): b694`S TWO POST-SEAL FAILURES, ITS DEFECTS (k) AND (l), ANSWERED BY ONE GENERATED FINDINGS ENTRY IN '
            'b678`s FORM', '', '### rows are the corrected lines and the lines that correct them, each read from its bank by line; the face and the '
            'hashes bank are not rewritten.', '',
            '  THE FACE                relay data/b694_registration_2026-10-20.txt :%d | %s' % (s['face'][0], s['face'][1].strip()),
            '  THE COUNTS              relay data/b694_checks.txt :%d ; data/b694_checks_postpush.txt :%d | 123 of 124 ; 122 of 124' % (s['cpre'][0], s['cpost'][0]),
            '  (k) THE ARM             relay data/b694_checks_standing-a.txt :%d ; data/b694_checks_postpush_standing-a.txt :%d' % (s['kpre'], s['kpost']),
            '  (k) AS WRITTEN          relay data/%s :%d | %s' % (HB, s['hrow'], s['hpath']),
            '  (k) AS IT SHOULD READ   %s | sha256 %s (read from the file)' % (PNG, s['sha']),
            '  (k) THE TEST            relay tools/rule_arms.py :%d | carried_by: the path and the sha256 both in a text bank of the act' % s['test'],
            '  (k) THE DEFECT          relay data/b694_defects.txt :%d' % s['dk'],
            '  (l) THE ARM             relay data/b694_checks_postpush_standing-a.txt :%d | the message at %s (id %s)' % (s['lpost'], s['ts'], s['mid'])]
            + ['  (l) WRITE %d             transcript line %d at %s | %s' % (k, i, t, _cmd(c)) for k, (i, t, c) in enumerate(u, 1)] + [
            '  (l) READ-BACKS          relay data/b694_relay_push_out.txt :%d main %s ; data/b694_pp_push_out.txt :%d main %s' % (
                s['rr'][0], s['rr'][1], s['pr'][0], s['pr'][1]),
            '  (l) THE RULE            relay data/b692_rules.txt :%d | left as they stand, the failure entered' % s['rule'],
            '  (l) THE DEFECT          relay data/b694_defects.txt :%d' % s['dl'],
            '', '### ### **TWO ARMS FAILING AFTER b694`S SEAL, UNDECLARED, EACH BY ITS CAUSE ; THE FACE AND THE HASHES BANK UNEDITED ; THE ENTRY AT '
            'FINDINGS :%s.**' % (landed_line or 'NOT YET WRITTEN')])


def main(route):
    s = compose()
    text = entry_text(s)
    import b695_record as REC
    if route == 'dry':
        REC.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b695_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b695_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b695_corrigendum.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, png=PNG, png_sha256=s['sha'], as_written=s['hpath'],
             message=dict(ts=s['ts'], id=s['mid'], uses=[dict(line=i, ts=t, command=c) for i, t, c in s['uses']]),
             readbacks=dict(relay=s['rr'][1], pp=s['pr'][1]))
    p = os.path.join(D, 'b695_corrigendum.json')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b695_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
