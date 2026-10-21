# -*- coding: utf-8 -*-
"""b700_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R310)(2): b699's trail Defects line (b699's defect (d)), its head line's two counts and
the navigator's root-named claim, answered by one generated FINDINGS entry in b678's corrigendum form; b699's sealed face (relay
data/b699_registration_2026-10-21.txt), its trail record (PLACE-papers OPEN_TRAILS :15336) and every root-named bank unedited.

### Carried from tools/b699_corrigendum.py (itself b695's successor), its rows rewritten for b699's record. b678's tool
### (tools/b678_corrigendum.py) is IMPORTED and unchanged: its reader `rd`; its form -- one generated entry, each line it corrects quoted with
### its place, the corrected reading and its source, the figures read from their banks and checked before any write, `dry` then `land`.
### Every figure is read, none typed:
###   (d) the trail: OPEN_TRAILS's b699 record (:15336) and its Defects line; b699's four defects read by tools/b700_record.py's repaired
###       reader -- data/b699_defects.txt (a)-(c) with the act passed at the call, and (d) from data/b699_closing.txt's (g) line, on the
###       author's answer at b700 (Option 1); b698's four read the same way from data/b698_defects.txt, to show which act's the line carries;
###   the head line: data/b699_closing.txt :1; the answers bank's prompts (data/b699_author_answers.txt "### PROMPT" rows) and the root-prompt
###       answer's (R278)(4) check, printed to the defects bank after the root (data/b699_defects.txt); the root's time (data/b699_act_root.json);
###       the trail's prompts line;
###   (e) the navigator's claim (the ruling's own account, relay data/b700_ferry.txt :5): the root's named banks as the root tool lists them
###       (data/b699_act_root.json items), the exclusion that keeps the defects bank out (tools/b699_record.py ROOT_EXCLUDE).
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b700_record's
### guarded landing, data/b700_corrigendum.txt (.json). Written by the Write tool at b700; it writes those two banks and the one FINDINGS entry.
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
import b700_worklist as K         # noqa: E402
import b700_record as REC         # noqa: E402  ### the repaired reader and the guarded landing

TITLE = ('## Corrigendum to b699’s trail and closing record (PLACE-papers OPEN_TRAILS :15336, relay data/b699_closing.txt): '
         'the trail’s Defects line, the head line’s two counts, the root-named claim')
PP = K.PP
OT = os.path.join(PP, 'OPEN_TRAILS.md')


def at(path, pred, lo=0, hi=None):
    L = C78.rd(path).split(NL)
    return [(i + 1, l) for i, l in enumerate(L) if lo <= i < (hi if hi is not None else len(L)) and pred(l)]


def compose():
    ot = C78.rd(OT).split(NL)
    head = K.B699_TRAIL
    if not ot[head - 1].startswith('### b699 '):
        sys.exit('### OPEN_TRAILS :%d IS NOT b699`S TRAIL -- NOTHING WRITTEN' % head)
    end = next((i for i in range(head, len(ot)) if ot[i].startswith('### b')), len(ot))
    dl = [(i + 1, ot[i]) for i in range(head - 1, end) if ot[i].startswith('**Defects** (relay data/b699_defects.txt):')]
    pl = [(i + 1, ot[i]) for i in range(head - 1, end) if ot[i].startswith('**Prompts to the author:**')]
    four99 = [(s, 'data/b699_defects.txt') for s in REC._defect_short('b699')] + REC.closing_defects('b699')
    four98 = REC._defect_short('b698')
    landed = re.findall(r'\(([a-z])\) ([^;]+?)(?:;|\.$)', dl[0][1].split(':', 1)[1].strip()) if len(dl) == 1 else []
    carries98 = [('(%s) %s' % (k, v.strip())) for k, v in landed] == four98
    cl = C78.rd(os.path.join(D, 'b699_closing.txt')).split(NL)
    hl = cl[0]
    hm = re.search(r'; (\d+) prompts? answered; (\d+) defects?$', hl)
    gl = [(i + 1, l) for i, l in enumerate(cl) if l.startswith('    (g) The defects (a)')]
    prompts = at(os.path.join(D, 'b699_author_answers.txt'), lambda l: l.startswith('### PROMPT '))
    calls = len(json.loads(C78.rd(os.path.join(D, 'b699_author_answers.json')) or '{}').get('calls') or [])
    chk = at(os.path.join(D, 'b699_defects.txt'), lambda l: l.startswith('### (R278)(4) THE MID-ACT CHECK (') and 'land as composed' in l)
    ckt = re.search(r'CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', chk[0][1]).group(1) if len(chk) == 1 else ''
    dfl = at(os.path.join(D, 'b699_defects.txt'), lambda l: re.match(r"^    \([a-z]\) ", l) is not None)
    rj = json.loads(C78.rd(os.path.join(D, 'b699_act_root.json')))
    items = [it.split()[0] for it in rj.get('items') or [] if it.startswith('data/')]
    named = dict((b, b in items) for b in ('data/b699_author_answers.txt', 'data/b699_author_answers.json', 'data/b699_citation_check.txt',
                                          'data/b699_citation_check.json', 'data/b699_defects.txt', 'data/b699_defects.json'))
    rx = at(os.path.join(T, 'b699_record.py'), lambda l: l.startswith("R.ROOT_EXCLUDE = re.compile(r'^b699_(defects|"))
    rl = at(os.path.join(D, 'act_roots.txt'), lambda l: l.startswith('b699 '))
    fy = at(os.path.join(D, 'b700_ferry.txt'), lambda l: "the navigator’s claim that the defects bank is root-named read as wrong" in l)
    ok = (len(dl) == 1 and len(pl) == 1 and carries98 and len(four99) == 4 and hm and (int(hm.group(1)), int(hm.group(2))) == (4, 3)
          and len(gl) == 1 and len(prompts) == 4 and len(chk) == 1 and ckt > rj.get('at', '') and len(dfl) == 3
          and named['data/b699_author_answers.txt'] and named['data/b699_citation_check.txt'] and not named['data/b699_defects.txt']
          and len(rx) == 1 and len(rl) == 1 and rl[0][1].split()[1] == rj.get('root') and len(fy) == 1)
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ (defects line %d, prompts line %d, carries b698`s %s, b699`s four %d, head %s, (g) %d, prompts %d, '
                 'check %d at %s against the root at %s, bank rows %d, named %s, exclusion %d, root row %d, ferry %d) -- NOTHING WRITTEN' % (
                     len(dl), len(pl), carries98, len(four99), hm and hm.groups(), len(gl), len(prompts), len(chk), ckt, rj.get('at'), len(dfl),
                     named, len(rx), len(rl), len(fy)))
    return dict(head=head, dl=dl[0], pl=pl[0], four99=four99, four98=four98, hl=hl, gl=gl[0][0], prompts=len(prompts), calls=calls,
                chk=chk[0][0], ckt=ckt, root=rj['root'], root_at=rj['at'], items=len(items), named=named, rx=rx[0][0], rl=rl[0][0], fy=fy[0][0])


def entry_text(s):
    d99 = '; '.join(r for r, _src in s['four99'])
    L = ['', TITLE, '',
         'b699’s trail record (OPEN_TRAILS :%d), sealed and landed before any of this, carries at its line :%d a Defects line that lists b698’s '
         'four defects in the place of b699’s: “%s”. The sealed record tool composed it from b698_record._defect_short, whose act was bound '
         'at import (relay tools/b698_record.py :367, `act=ACT`, ‘b698’) and carried by reference into the sealed tools/b699_record.py; b699 '
         'landed it as composed, on the author’s word, and entered the defect in its closing’s (g) line (relay data/b699_closing.txt :%d) and '
         'not in its defects bank.' % (s['head'], s['dl'][0], s['dl'][1].split(':', 1)[1].strip().rstrip('.'), s['gl']), '',
         '**The Defects line, corrected** (b699’s defect (d)). b699’s four, as the defects bank and the closing line give them, read by b700’s '
         'record tool with its act passed at the call: %s. (a)-(c) from relay data/b699_defects.txt; (d) from data/b699_closing.txt :%d.' % (
             d99, s['gl']), '',
         '**The head line’s two counts.** data/b699_closing.txt :1 reads “%s”. PROMPTS: 4 as printed, 5 as put -- the answers bank holds 4 '
         'prompts in %d calls (relay data/b699_author_answers.txt) and was written once, before the root; the fifth, the trail’s prompt at the '
         'root, was put after it, its answer checked at %s (data/b699_defects.txt :%d) against the root computed at %s, so no count the closing '
         'reads carries it. The trail’s own line (OPEN_TRAILS :%d, “%s”) undercounts it the same way. DEFECTS: 3 as printed, 4 as entered -- '
         'the head line counts the defects bank’s lettered rows, (a)-(c); (d) stands in the closing’s (g) line alone, on the author’s word.' % (
             s['hl'], s['calls'], s['ckt'], s['chk'], s['root_at'], s['pl'][0], s['pl'][1].strip()), '',
         '**The root-named claim** (lettered the navigator’s (e)). The answer at the trail’s prompt, the navigator’s, read the defects bank as '
         'root-named, so that (d) could not be written there after the root (the ruling’s account, relay data/b700_ferry.txt :%d). As the root tool lists '
         'them, b699’s root names %d banks (relay data/b699_act_root.json; data/act_roots.txt :%d, %s): the answers bank (.txt and .json) and the '
         'citation bank (.txt and .json) among them, the defects bank not -- tools/b699_record.py :%d excludes `defects` by name. The seat '
         'followed the word, and its (R278)(4) check on it was VACUOUS (no path, line or commit named); the claim is corrected here, the bank '
         'left as it stands.' % (s['fy'], s['items'], s['rl'], s['root'][:16], s['rx']), '',
         'The sealed face, the trail record and every root-named bank are not edited -- this entry is their correction. Nothing here proves RH '
         'or GRH.', '',
         '*Filed at b700 on the author’s ruling `(R310)`(2): generated by relay `tools/b700_corrigendum.py`, carried from '
         '`tools/b699_corrigendum.py`, in the corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), banked as '
         'relay `data/b700_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at rows (14) to (16); it answers b699’s '
         'defect (d), its head line’s counts and the navigator’s (e).*', '']
    return NL.join(L)


def bank_lines(s, landed_line=None):
    return ['b700 -- THE CORRIGENDUM, (R310)(2): b699`S TRAIL DEFECTS LINE, ITS HEAD LINE`S TWO COUNTS AND THE NAVIGATOR`S ROOT-NAMED CLAIM, '
            'ANSWERED BY ONE GENERATED FINDINGS ENTRY IN b678`s FORM', '',
            '### rows are the corrected lines and the lines that correct them, each read from its bank by line; the face, the trail and the '
            'root-named banks are not rewritten.', '',
            '  THE TRAIL               PLACE-papers OPEN_TRAILS.md :%d (b699`s record) ; its Defects line :%d' % (s['head'], s['dl'][0]),
            '  (d) AS LANDED           b698`s four: %s' % ' ; '.join(s['four98']),
            '  (d) AS ENTERED          b699`s four: %s' % ' ; '.join('%s [%s]' % rs for rs in s['four99']),
            '  (d) THE CAUSE           relay tools/b698_record.py :367 `def _defect_short(act=ACT):`, carried at tools/b699_record.py :786',
            '  (d) THE ENTRY           relay data/b699_closing.txt :%d ((g)), on the author`s word' % s['gl'],
            '  THE HEAD LINE           relay data/b699_closing.txt :1 | %s' % s['hl'],
            '  PROMPTS                 4 as printed ; 5 as put -- the answers bank 4 prompts in %d calls ; the fifth at the trail, its check at %s '
            '(data/b699_defects.txt :%d), the root at %s' % (s['calls'], s['ckt'], s['chk'], s['root_at']),
            '  PROMPTS ON THE TRAIL    OPEN_TRAILS.md :%d | %s' % (s['pl'][0], s['pl'][1].strip()),
            '  DEFECTS                 3 as printed (the bank`s lettered rows) ; 4 as entered ((d) in the closing`s (g) line)',
            '  (e) THE CLAIM           relay data/b700_ferry.txt :%d (the ruling`s account of the author`s word at the trail`s prompt)' % s['fy'],
            '  (e) THE ROOT`S BANKS    relay data/b699_act_root.json | %d banks ; %s' % (
                s['items'], ' ; '.join('%s %s' % (b, 'NAMED' if v else 'NOT NAMED') for b, v in s['named'].items())),
            '  (e) THE EXCLUSION       relay tools/b699_record.py :%d (ROOT_EXCLUDE, `defects` by name)' % s['rx'],
            '  (e) THE ROOT            relay data/act_roots.txt :%d | %s, computed at %s ; UNCHANGED' % (s['rl'], s['root'], s['root_at']),
            '', '### ### **b699`S TRAIL LINE CARRYING b698`S FOUR, b699`S FOUR ENTERED ; PROMPTS 4 AS PRINTED, 5 AS PUT ; DEFECTS 3 AS PRINTED, 4 AS '
            'ENTERED ; THE DEFECTS BANK NOT ROOT-NAMED (THE NAVIGATOR`S (e)) ; THE FACE, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT '
            'FINDINGS :%s.**' % (landed_line or 'NOT YET WRITTEN')]


def main(route):
    s = compose()
    text = entry_text(s)
    if route == 'dry':
        REC.R.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b700_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b700_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b700_corrigendum.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, trail_line=s['dl'][0],
             landed=s['four98'], entered=[dict(row=r, source=src) for r, src in s['four99']], prompts=dict(printed=4, put=5),
             defects=dict(printed=3, entered=4), root_banks=s['items'], named=s['named'])
    p = os.path.join(D, 'b700_corrigendum.json')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b700_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
