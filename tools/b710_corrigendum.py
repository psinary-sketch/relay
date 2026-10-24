# -*- coding: utf-8 -*-
"""b710_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R320)(3): b709's two items found after its seal -- G-REPORT-UNSEALED and G-AXIS-REGISTERED
failing in the pre-push and post-push runs on their own needles (the report's key RATIO wanted in capitals where the unsealed report printed "the
twelve ratios"; the ranking's quotation needled as one string where the registrations bank wraps it across its lines 12-13; data/b709_defects.txt,
the unlettered event) -- answered by one generated FINDINGS entry in b678's corrigendum form, in the banks' words; b709's sealed face (relay
data/b709_registration_2026-10-23.txt), its trail record (PLACE-papers OPEN_TRAILS :15766) and every root-named bank unedited.

### Carried from tools/b709_corrigendum.py by tools/b710_carry.py (data/b710_carry_corrigendum.txt; its head :1-:65 and its landing :178-:226 read
### by offset and limit), then written whole by the Write tool with its items rewritten for b709's record (b708 and b709 wrote theirs the same
### way; the item sections :66-:177 not read). b678's reader `rd` IMPORTED unchanged; its form -- one generated entry, each line it corrects
### quoted with its place, the corrected reading and its source, the figures read from their banks and checked before any write, `dry` then
### `land`. Every figure is read, none typed:
###   the event: the row of data/b709_defects.txt beneath EVENTS, UNLETTERED that opens TWO ARMS FAILING AFTER THE SEAL, by line;
###   the failing three: data/b709_checks_postpush.txt's LIVE FAILING list; the one declared on the face: the face's declaration line;
###   the trail's Defects line: PLACE-papers OPEN_TRAILS from the trail head at :15766, its letters read; the trail's own line number;
###   the needles: tools/b709_checks.py report_unsealed_ok and axis_registered_ok, their needle lines; the report's wording: data/b709_report.txt;
###   the wrap: data/b709_registrations.txt :12-:13; the repairs: tools/b710_checks.py keys_ci and joined, their controls
###   data/b710_repair_controls.txt (AS WANTED True).
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b710_record's
### guarded landing, data/b710_corrigendum.txt (.json). The corrigenda bank's row (30) is appended by the seat through the Edit tool from the
### bank line this tool prints (ROW). It writes those two banks and the one FINDINGS entry.
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
import b710_worklist as K         # noqa: E402
import b710_record as REC         # noqa: E402  ### the guarded landing and the repaired defects reader

TITLE = ('## Corrigendum to b709’s record after its seal (relay data/b709_defects.txt, data/b709_checks_postpush.txt): G-REPORT-UNSEALED’s '
         'key in capitals and G-AXIS-REGISTERED’s quotation through a wrapped line')
EVENT_HEAD = '    TWO ARMS FAILING AFTER THE SEAL ON THEIR OWN NEEDLES'
POST_SEAL_ARMS = ['G-AXIS-REGISTERED', 'G-REPORT-UNSEALED']
DECLARED_ARM = 'G-READ-RULE-STANDING'
QUOTE = '(e) representation coordinates (the operator / Toeplitz form) -- 4'
ROW = ('  (30) b709\'s suite after its seal (relay data/b709_checks_postpush.txt, LIVE FAILING 3, two beyond the face): G-REPORT-UNSEALED on its\n'
       '      key RATIO wanted in capitals where the unsealed report printed "the twelve ratios" (data/b709_report.txt), and G-AXIS-REGISTERED on\n'
       '      the ranking\'s quotation needled as one string where data/b709_registrations.txt wraps it across :12-:13 (the unlettered event; THE\n'
       '      ARMS\' OWN NEEDLES). THE CORRECTION: the keys read case-insensitively and the bank read after joining its wrapped lines, repaired at\n'
       '      b710\'s carry under (R320)(3) (relay data/b710_tool_repairs.txt rows (1)-(2), their controls data/b710_repair_controls.txt). The\n'
       '      generated corrigendum entry stands at FINDINGS.md :%s.')


def _event(L):
    s = next((i + 1 for i, l in enumerate(L) if l.startswith(EVENT_HEAD)), 0)
    if not s:
        return 0, 0, ''
    e = next((i for i in range(s, len(L)) if not L[i].strip()), len(L))
    return s, e, ' '.join(x.strip() for x in L[s - 1:e])


def _line_of(L, needle, start=1):
    return next((i + 1 for i, l in enumerate(L) if i + 1 >= start and needle in l), 0)


def compose():
    dl = C78.rd(os.path.join(D, 'b709_defects.txt')).split(NL)
    es, ee, et = _event(dl)
    m = re.search(r'LIVE FAILING : (\d+) \[(.*?)\]', C78.rd(os.path.join(D, 'b709_checks_postpush.txt')))
    fails = sorted(x.strip().strip("'") for x in (m.group(2) if m else '').split(',') if x.strip())
    face = ' '.join(C78.rd(os.path.join(ROOT, *K.B709_FACE.split('/'))).split())
    md = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', face)
    declared = sorted(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', md.group(1)))) if md else []
    post = sorted(a for a in fails if a not in declared)
    ot = C78.rd(os.path.join(K.PP, 'OPEN_TRAILS.md')).split(NL)
    trail = K.B709_TRAIL if ot[K.B709_TRAIL - 1].startswith('### b709') else 0
    dline = next((i + 1 for i in range(trail, min(trail + 60, len(ot))) if ot[i].startswith('**Defects**')), 0) if trail else 0
    letters = re.findall(r'\(([a-h])\) THE SEAT', ot[dline - 1]) if dline else []
    ck = C78.rd(os.path.join(T, 'b709_checks.py')).split(NL)
    ru, ax = _line_of(ck, 'def report_unsealed_ok'), _line_of(ck, 'def axis_registered_ok')
    ru_n = _line_of(ck, "('ONSET', 'ZETA', 'RATIO', 'MODULES', 'FIGURES')", ru)
    ax_n = _line_of(ck, "q = '%s'" % QUOTE, ax)
    rep = C78.rd(os.path.join(D, 'b709_report.txt'))
    rep_ratio = 'the twelve ratios' in rep and 'RATIO' not in rep
    rg = C78.rd(os.path.join(D, 'b709_registrations.txt')).split(NL)
    wrap = rg[11].rstrip().endswith('"(e) representation') and rg[12].strip().startswith('coordinates (the operator / Toeplitz form) -- 4"')
    ctl = REC.jl('b710_repair_controls.json')
    ok_ctl = ctl.get('as_wanted') is True and sum(1 for c in ctl.get('cases') or [] if c['case'][:3] in ('(1)', '(2)')) == 8
    s = dict(event=(es, ee), event_text=et, fails=fails, declared=declared, post_seal=post, trail=trail, defects_line=dline, letters=letters,
             ru=ru, ru_n=ru_n, ax=ax, ax_n=ax_n, rep_ratio=rep_ratio, wrap=wrap, ctl=ok_ctl)
    bad = [k for k, v in (('the event row', es), ('the failing three', fails == sorted(POST_SEAL_ARMS + [DECLARED_ARM])), ('the declared arm', declared == [DECLARED_ARM]),
                          ('the post-seal pair', post == POST_SEAL_ARMS), ('the trail head', trail), ('the Defects line', letters == list('abcdefgh')),
                          ('the report needle', ru and ru_n), ('the axis needle', ax and ax_n), ('the report wording', rep_ratio), ('the wrap', wrap),
                          ('the controls', ok_ctl)) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (%r)' % (bad, s))
    return s


def entry_text(s):
    return NL + NL.join(_entry_lines(s)) + NL


def _entry_lines(s):
    return [
        TITLE, '',
        ('b709’s face was locked after Components 1-4 (relay %s) with one failure declared on it by name (%s); its pre-push and post-push suites '
         'found two more, %s and %s, not editable in a sealed tool, entered in its defects bank as an unlettered event (relay data/b709_defects.txt '
         ':%d-:%d) and in its closing’s defects line. This entry answers the two in the banks’ words, each with its cause by line; the face, the '
         'trail record (PLACE-papers OPEN_TRAILS :%d, its Defects line :%d reading (a)-(h) equal to the bank’s (a)-(h)) and every root-named bank '
         'are not edited.' % (K.B709_FACE, DECLARED_ARM, POST_SEAL_ARMS[1], POST_SEAL_ARMS[0], s['event'][0], s['event'][1], s['trail'], s['defects_line'])), '',
        ('**THE FIRST ITEM: G-REPORT-UNSEALED FAILING AFTER THE SEAL** (relay data/b709_defects.txt :%d). The sealed arm (tools/b709_checks.py '
         'report_unsealed_ok :%d, its needle at :%d) wants the five keys ONSET, ZETA, RATIO, MODULES and FIGURES in the report bank, each read '
         'case-sensitively; the unsealed report tool, written after the author’s word at the root, printed “the twelve ratios” in lower case and no '
         'RATIO in its verdict line (relay data/b709_report.txt :18, :23), so the needle found nothing there, every other clause of the arm met (the '
         'stamp after the lock and before the root, six lines, the tool unsealed). THE CORRECTION: under (R320)(3) the key is read case-insensitively '
         'at this act’s carry -- tools/b710_checks.py keys_ci, the arm reading its keys through it -- its diff in relay data/b710_tool_repairs.txt row '
         '(1) and its controls in data/b710_repair_controls.txt (b709’s report failing the old needle and passing the repaired; the NEG copy with '
         'every “ratio” removed failing the repaired); no sealed tool of b709 is edited.' % (s['event'][0], s['ru'], s['ru_n'])), '',
        ('**THE SECOND ITEM: G-AXIS-REGISTERED FAILING AFTER THE SEAL** (relay data/b709_defects.txt :%d). The sealed arm (tools/b709_checks.py '
         'axis_registered_ok :%d, its needle at :%d) needles the ranking’s second row as one string, “%s”, in the registrations bank and in '
         'data/b705_i6_ranking.txt :58; the registrations bank, written at b709’s step zero by the Write tool, wraps that quotation across its lines '
         '12-13 (“(e) representation” / “coordinates (the operator / Toeplitz form) -- 4”), so the needle found nothing there, the pre-run having '
         'read the arm failing on the entry not yet landed and so masked the needle. THE CORRECTION: under (R320)(3) the bank is read after joining '
         'its wrapped lines at this act’s carry -- tools/b710_checks.py joined, every run of white space read as one space -- its diff in relay '
         'data/b710_tool_repairs.txt row (2) and its controls in data/b710_repair_controls.txt (b709’s bank failing the old needle and passing the '
         'repaired, the ranking’s :58 passing, the NEG copy with “Toeplitz” changed failing, the arm’s other needles passing on the joined bank); '
         'no sealed tool of b709 is edited.' % (s['event'][0], s['ax'], s['ax_n'], QUOTE)), '',
        'The sealed face, the trail record and every root-named bank are not edited -- this entry is their correction. Nothing here proves RH or GRH.', '',
        ('*Filed at b710 on the author’s ruling `(R320)`(3): generated by relay `tools/b710_corrigendum.py`, carried from `tools/b709_corrigendum.py`, '
         'in the corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), banked as relay `data/b710_corrigendum.txt`, '
         'the corrigenda bank `data/b675_corrigenda.txt` appended at row (30); it answers b709’s two post-seal needles.*')]


def bank_lines(s, landed_line=None):
    L = ['b710 -- THE CORRIGENDUM ENTRY FOR b709`S TWO POST-SEAL NEEDLES, (R320)(3) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the figures read before the write: the event data/b709_defects.txt :%d-:%d ; failing %s ; declared %s ; beyond the face %s ; the trail' % (
             s['event'][0], s['event'][1], s['fails'], s['declared'], s['post_seal']),
         '### OPEN_TRAILS :%d, its Defects line :%d letters %s ; the needles tools/b709_checks.py :%d/:%d and :%d/:%d ; the report`s wording %s ; the wrap %s ;' % (
             s['trail'], s['defects_line'], ''.join(s['letters']), s['ru'], s['ru_n'], s['ax'], s['ax_n'], s['rep_ratio'], s['wrap']),
         '### the controls data/b710_repair_controls.txt AS WANTED %s.' % s['ctl'], '']
    L += ['  ' + l for l in _entry_lines(s)]
    L += ['', '### ### **TWO ITEMS ANSWERED (G-REPORT-UNSEALED`S KEY, G-AXIS-REGISTERED`S WRAP) ; THE FACE, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
        landed_line if landed_line else 'NOT YET WRITTEN')]
    return L


def main(route):
    s = compose()
    text = entry_text(s)
    if route == 'dry':
        REC.R.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        print(ROW % 'NOT YET WRITTEN')
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b710_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b710_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b710_corrigendum.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, lettered=[], events=POST_SEAL_ARMS, trail_arms=[],
             failing=s['fails'], declared=s['declared'], post_seal=s['post_seal'], trail=s['trail'], defects_line=s['defects_line'], row=30)
    p = os.path.join(D, 'b710_corrigendum.json')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])
    print(ROW % ln)


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b710_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
