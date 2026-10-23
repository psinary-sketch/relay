# -*- coding: utf-8 -*-
"""b709_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R319)(2): b708's item found after its seal -- G-CLOSING-DRY-STEP failing in the pre-push
and post-push runs on its own needle (the string "### NO VERDICT LINE" the closing's dry run prints for the prints bank, which carries no verdict
line by its form; data/b708_defects.txt, the unlettered event) -- and, beside it, the kind b708 read for C7OrderBounds.lean :380 ("a renamed
Mathlib declaration" where the error names the kernel's own _half theorem failing at :277; this act's (a), found at the citation check) --
answered by one generated FINDINGS entry in b678's corrigendum form, in the banks' words; b708's sealed face (relay
data/b708_registration_2026-10-23.txt), its trail record (PLACE-papers OPEN_TRAILS :15724) and every root-named bank unedited.

### Carried from tools/b708_corrigendum.py by tools/b709_carry.py (data/b709_carry_corrigendum.txt), then written whole by the Write tool with
### its rows rewritten for b708's record (b708 wrote its own the same way for b707's). b678's tool (tools/b678_corrigendum.py) is IMPORTED and
### unchanged: its reader `rd`; its form -- one generated entry, each line it corrects quoted with its place, the corrected reading and its source,
### the figures read from their banks and checked before any write, `dry` then `land`. Every figure is read, none typed:
###   the event: the rows of data/b708_defects.txt beneath EVENTS, UNLETTERED, by line (its own heading line to the blank line);
###   the failing two: data/b708_checks_postpush.txt's LIVE FAILING list; the one declared on the face: the face's declaration line;
###   the trail's Defects line: PLACE-papers OPEN_TRAILS from the trail head at :15724, its letters read; the trail's own line number;
###   the string: data/b708_reg_gate.txt's line for the prints bank; the old needle: tools/b708_checks.py's closing_dry_ok (its last clause);
###   the repair: tools/b709_checks.py no_verdict_line_ok and NO_VERDICT_EXEMPT, its controls data/b709_repair_controls.txt (AS WANTED True);
###   the kind: data/b708_port_lines.txt's :380 row and b708's entry line at FINDINGS :10154; the module at port-b707 (:264 the _half theorem,
###   :383 its use) and this act's (a) in data/b709_defects.txt; the correction named by path.
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b709_record's
### guarded landing, data/b709_corrigendum.txt (.json). The corrigenda bank's row (29) is appended by the seat through the Edit tool from the
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
import b709_worklist as K         # noqa: E402
import b709_record as REC         # noqa: E402  ### the guarded landing and the repaired defects reader

TITLE = ('## Corrigendum to b708’s record after its seal (relay data/b708_defects.txt, data/b708_checks_postpush.txt, data/b708_port_lines.txt): '
         'G-CLOSING-DRY-STEP’s needle on the prints bank, and the kind read for C7OrderBounds.lean :380')
EVENT_HEAD = '    G-CLOSING-DRY-STEP FAILING AFTER THE SEAL, IN THE PRE-PUSH RUN.'
POST_SEAL_ARM = 'G-CLOSING-DRY-STEP'
DECLARED_ARM = 'G-READ-RULE-STANDING'
THM_HALF = 'exists_norm_completedRiemannZeta₀_le_exp_half'


def _event(L):
    s = next((i + 1 for i, l in enumerate(L) if l.startswith(EVENT_HEAD)), 0)
    if not s:
        return 0, 0, ''
    e = next((i for i in range(s, len(L)) if not L[i].strip()), len(L))
    return s, e, ' '.join(x.strip() for x in L[s - 1:e])


def _row(L, letter):
    s = next((i + 1 for i, l in enumerate(L) if l.startswith('    (%s) ' % letter)), 0)
    if not s:
        return 0, 0, ''
    e = next((i for i in range(s, len(L)) if re.match(r'^    \([a-z]\) ', L[i]) or L[i].startswith('###')), len(L))
    return s, e, ' '.join(x.strip() for x in L[s - 1:e])


def compose():
    df = C78.rd(os.path.join(D, 'b708_defects.txt')).split(NL)
    ev = _event(df)
    ck = C78.rd(os.path.join(D, 'b708_checks_postpush.txt'))
    m8 = re.search(r'LIVE FAILING : (\d+) \[(.*?)\]', ck)
    fails = [x.strip().strip("'") for x in (m8.group(2) if m8 else '').split(',') if x.strip()]
    face = C78.rd(os.path.join(ROOT, *K.B708_FACE.split('/')))
    md = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', ' '.join(face.split()))
    declared = sorted(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', md.group(1)))) if md else []
    ot = C78.rd(os.path.join(K.PP, 'OPEN_TRAILS.md')).split(NL)
    th = next((i + 1 for i, l in enumerate(ot) if l.startswith('### b708 — lane two, act one hundred and thirty-five')), 0)
    dl = next((i + 1 for i in range(th, len(ot)) if ot[i].startswith('**Defects** (relay data/b708_defects.txt)')), 0) if th else 0
    rl = next((i + 1 for i in range(th, len(ot)) if ot[i].startswith('**Resolved by the seat')), 0) if th else 0
    letters = re.findall(r'\(([a-z])\) THE (?:SEAT|NAVIGATOR)', ot[dl - 1]) if dl else []
    short = REC._defect_short('b708')
    bank_letters = [re.match(r'^\(([a-z])\)', x).group(1) for x in short]
    gate = C78.rd(os.path.join(D, 'b708_reg_gate.txt')).split(NL)
    gl = next((i + 1 for i, l in enumerate(gate) if 'data/b708_prints_v0.17.txt): ### NO VERDICT LINE' in l), 0)
    old = C78.rd(os.path.join(T, 'b708_checks.py')).split(NL)
    ol = next((i + 1 for i, l in enumerate(old) if l.startswith('def closing_dry_ok(S):')), 0)
    ocl = next((i + 1 for i in range(ol, min(ol + 6, len(old))) if "'### NO VERDICT LINE' not in g" in old[i]), 0) if ol else 0
    new = C78.rd(os.path.join(T, 'b709_checks.py'))
    ctl = C78.rd(os.path.join(D, 'b709_repair_controls.txt'))
    mc = re.search(r'CASES (\d+) ; AS WANTED (True|False)', ctl)
    pl = C78.rd(os.path.join(D, 'b708_port_lines.txt')).split(NL)
    pll = next((i + 1 for i, l in enumerate(pl) if l.startswith('  C7OrderBounds.lean :380:8') and 'a renamed Mathlib declaration' in l), 0)
    fi = C78.rd(os.path.join(K.PP, 'FINDINGS.md')).split(NL)
    el = K.B708_ENTRY + 2
    mod = C78.rd(os.path.join(K.LV_DIR, *K.PORT_FILE.split('/'))).split(NL)
    d9 = C78.rd(os.path.join(D, 'b709_defects.txt')).split(NL)
    a9 = _row(d9, 'a')
    rules = C78.rd(os.path.join(D, 'b709_rules.txt'))
    post_seal = [a for a in fails if a not in declared]
    ok = (ev[0] and 'the arm`s defect, found after the seal' in ev[2].replace("'", '`') and len(fails) == 2 and declared == [DECLARED_ARM]
          and post_seal == [POST_SEAL_ARM] and th == K.B708_TRAIL and dl and rl and letters == list('abcdefg') and bank_letters == list('abcdefg')
          and gl and ol and ocl and 'def no_verdict_line_ok(g):' in new and "NO_VERDICT_EXEMPT = ('data/b708_prints_v0.17.txt',)" in new
          and mc and mc.group(2) == 'True' and pll and len(fi) >= el and '380:8 a renamed Mathlib declaration' in fi[el - 1]
          and len(mod) >= 383 and mod[263].startswith('theorem ' + THM_HALF) and THM_HALF in mod[382]
          and a9[0] and 'CASCADE OF :277' in a9[2] and '(1) THE CARRY IS READ BY DIFF' in rules)
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ (event %s, failing %s, declared %s, trail :%s, Defects :%s letters %s, bank %s, gate :%s, old :%s/:%s, '
                 'controls %s, port_lines :%s, entry :%s, module %s/%s, (a) :%s) -- NOTHING WRITTEN' % (
                     ev[0], fails, declared, th, dl, ''.join(letters), ''.join(bank_letters), gl, ol, ocl, mc.group(0) if mc else None, pll, el,
                     mod[263][:40] if len(mod) > 263 else '-', THM_HALF in mod[382] if len(mod) > 382 else '-', a9[0]))
    return dict(event=(ev[0], ev[1]), fails=fails, declared=declared, post_seal=post_seal, trail=th, defects_line=dl, resolved_line=rl,
                letters=''.join(letters), bank_letters=''.join(bank_letters), gate_line=gl, old_def=ol, old_clause=ocl, cases=int(mc.group(1)),
                port_line=pll, entry_line=el, a_row=(a9[0], a9[1] - 1 if a9[1] > a9[0] else a9[0]))


def entry_text(s):
    return NL + NL.join(_entry_lines(s))   # ### the leading newline the guarded landing expects (the title two lines past the ledger's last)


def _entry_lines(s):
    return [TITLE, '',
            'b708’s face was locked after Components 1-4 (relay data/b708_registration_2026-10-23.txt) with one failure declared on it by name '
            '(%s); its pre-push and post-push suites found one more, %s, not editable in a sealed tool, entered in its defects bank as an '
            'unlettered event and in its closing’s defects line; and its reading of the port’s second line (C7OrderBounds.lean :380) was found at '
            'this act’s citation check to be a misreading of the kernel’s own declaration. This entry answers the two in the banks’ words, each '
            'with its cause by line; the face, the trail record (PLACE-papers OPEN_TRAILS :%d, its Defects line :%d reading (%s) equal to the bank’s '
            '(%s)) and every root-named bank are not edited.' % (
                ', '.join(s['declared']), ', '.join(s['post_seal']), s['trail'], s['defects_line'], ')-('.join(s['letters'][0::6]), ')-('.join(s['bank_letters'][0::6])), '',
            '**THE POST-SEAL ITEM: G-CLOSING-DRY-STEP FAILING AFTER THE SEAL** (relay data/b708_defects.txt :%d-:%d). The sealed arm '
            '(tools/b708_checks.py closing_dry_ok :%d, its needle the last clause of :%d) forbids the string “### NO VERDICT LINE” anywhere in the '
            'gate’s record; the closing’s dry run prints that string for data/b708_prints_v0.17.txt (data/b708_reg_gate.txt :%d), whose form -- '
            'b706’s prints bank, the probe step’s print banked whole -- carries no verdict line, so the arm read the closing’s honest line as a '
            'failure, the closing’s dry run CLEAN and the gate CLEAR beside it. THE CORRECTION: under (R319)(2) the needle is repaired at this act’s '
            'carry -- tools/b709_checks.py no_verdict_line_ok excludes the prints bank by name (NO_VERDICT_EXEMPT) and fails on the string anywhere '
            'else -- its diff in relay data/b709_tool_repairs.txt and its controls in data/b709_repair_controls.txt (%d cases as wanted: b708’s own '
            'gate record passing the repaired needle and failing the old; the NEG control, the string moved onto a verdict-bearing bank’s line, '
            'failing both); no sealed tool of b708 is edited.' % (s['event'][0], s['event'][1], s['old_def'], s['old_clause'], s['gate_line'], s['cases']), '',
            '**THE KIND OF C7OrderBounds.lean :380** (relay data/b708_port_lines.txt :%d; b708’s entry FINDINGS :%d “380:8 a renamed Mathlib '
            'declaration”; data/b708_closing.txt’s port line the same). The error at :380:8 names SIDELvConservation.%s, the kernel’s own theorem '
            'declared at :264 of the module on port-b707, whose body fails at :277 (the WeakFEPair.hasMellin call, the first line’s kind) and which '
            ':383 applies -- the “unknown constant” is that theorem not elaborating, a cascade of :277, and no Mathlib name is renamed. THE '
            'CORRECTION: the kind is “a cascade of :277”; the one edit at :277 under (R319)(4) answers both lines, :380 read again after it '
            '(relay data/b709_defects.txt (a) :%d-:%d, the seat’s, found at the citation check and entered by the fact clause; data/b709_port.txt); '
            'b708’s bank and entry stand as written.' % (s['port_line'], s['entry_line'], THM_HALF, s['a_row'][0], s['a_row'][1]), '',
            'The sealed face, the trail record and every root-named bank are not edited -- this entry is their correction. Nothing here proves RH or GRH.', '',
            '*Filed at b709 on the author’s ruling `(R319)`(2): generated by relay `tools/b709_corrigendum.py`, carried from '
            '`tools/b708_corrigendum.py`, in the corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), banked as '
            'relay `data/b709_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (29); it answers b708’s post-seal item '
            'and the kind of :380.*']


ROW = ('  (29) b708\'s suite after its seal (relay data/b708_checks_postpush.txt, LIVE FAILING 2, one beyond the face): G-CLOSING-DRY-STEP on the\n'
       '      string "### NO VERDICT LINE" the closing\'s dry run prints for the prints bank data/b708_prints_v0.17.txt, which carries no verdict\n'
       '      line by its form (the unlettered event; THE ARM\'S OWN NEEDLE); and the kind b708 read for C7OrderBounds.lean :380, "a renamed\n'
       '      Mathlib declaration", where the error names the kernel\'s own _half theorem failing at :277 (b709\'s (a), THE SEAT\'S). THE\n'
       '      CORRECTION: the needle repaired at b709\'s carry under (R319)(2) (relay data/b709_tool_repairs.txt, its controls\n'
       '      data/b709_repair_controls.txt); the kind read as a cascade of :277, the one edit at :277 under (R319)(4). The generated corrigendum\n'
       '      entry stands at FINDINGS.md :%s.')


def bank_lines(s, landed_line=None):
    return ['b709 -- THE CORRIGENDUM, (R319)(2): b708`S POST-SEAL ITEM (G-CLOSING-DRY-STEP`S NEEDLE) AND THE KIND OF C7OrderBounds.lean :380, ANSWERED BY ONE GENERATED '
            'FINDINGS ENTRY IN b678`s FORM', '',
            '### rows are the corrected lines and the lines that correct them, each read from its source by line; the face, the trail and the root-named banks are not rewritten.', '',
            '  THE POST-SEAL ITEM       relay data/b708_defects.txt :%d-:%d (the unlettered event) | G-CLOSING-DRY-STEP, tools/b708_checks.py closing_dry_ok :%d, the needle at :%d ; the string at data/b708_reg_gate.txt :%d | '
            'tools/b709_checks.py no_verdict_line_ok, NO_VERDICT_EXEMPT ((R319)(2)); controls data/b709_repair_controls.txt, %d cases as wanted' % (
                s['event'][0], s['event'][1], s['old_def'], s['old_clause'], s['gate_line'], s['cases']),
            '  THE KIND OF :380         relay data/b708_port_lines.txt :%d ; FINDINGS :%d | "a renamed Mathlib declaration" where the error names the kernel`s own %s (:264, applied at :383) | '
            'a cascade of :277; the one edit at :277 ((R319)(4)); data/b709_defects.txt (a) :%d-:%d' % (s['port_line'], s['entry_line'], THM_HALF, s['a_row'][0], s['a_row'][1]),
            '  THE FAILING TWO          relay data/b708_checks_postpush.txt | %s | declared on the face %s ; found after the seal %s' % (
                ', '.join(s['fails']), ', '.join(s['declared']), ', '.join(s['post_seal'])),
            '  THE TRAIL                OPEN_TRAILS :%d, its Defects line :%d (%s) and Resolved line :%d against the bank (%s) | equal; no trail arm fails at b708' % (
                s['trail'], s['defects_line'], s['letters'], s['resolved_line'], s['bank_letters']),
            '  THE CORRIGENDA BANK     relay data/b675_corrigenda.txt, row (29) appended by this act through the Edit tool',
            '', '### ### **TWO ITEMS ANSWERED (THE POST-SEAL NEEDLE, THE KIND OF :380) ; THE FACE, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
                landed_line or 'NOT YET WRITTEN')]


def main(route):
    s = compose()
    text = entry_text(s)
    if route == 'dry':
        REC.R.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        print(ROW % 'NOT YET WRITTEN')
        return
    if route == 'bank':
        # ### the entry already landed (the first `land` call wrote the entry and stopped before its banks: the text lacked its leading newline,
        # ### the title read one line early; the blank line inserted by the Edit tool, the event in data/b709_defects.txt); the landed line read
        # ### from the ledger itself, the title found once, and the banks written for it.
        fi = C78.rd(os.path.join(K.PP, 'FINDINGS.md')).split(NL)
        at = [i + 1 for i, l in enumerate(fi) if l == TITLE]
        if len(at) != 1 or fi[at[0] - 2].strip() or fi[at[0]].strip():
            sys.exit('### THE TITLE STANDS AT %s, NOT ONCE WITH A BLANK LINE EACH SIDE -- NOTHING WRITTEN' % at)
        ln = at[0]
        p = os.path.join(D, 'b709_corrigendum_landing.json')
        with open(p + '.tmp', 'wb') as fh:
            fh.write((json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), lines=[dict(file='FINDINGS.md', line=ln, title=TITLE)],
                                      route='bank (the entry landed by the first land call; see data/b709_defects.txt)'), indent=1, ensure_ascii=False) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
    else:
        REC.land([('FINDINGS.md', TITLE, text)], 'b709_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
        ln = (REC.jl('b709_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b709_corrigendum.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, lettered=[], event=POST_SEAL_ARM,
             second_item='the kind of C7OrderBounds.lean :380', trail_arms=[], failing=s['fails'], declared=s['declared'], post_seal=s['post_seal'],
             trail=s['trail'], defects_line=s['defects_line'], row=29)
    p = os.path.join(D, 'b709_corrigendum.json')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])
    print(ROW % ln)


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land', 'bank'):
        print('usage: b709_corrigendum.py dry | land | bank')
        sys.exit(2)
    main(r)
