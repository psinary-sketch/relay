# -*- coding: utf-8 -*-
"""b693_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R303)(2): b692's two post-seal figures, answered by one generated FINDINGS entry in
b678's corrigendum form, b692's sealed entry (FINDINGS :9462) unedited, the two lettered as b692's defect (m).

### b678's tool (tools/b678_corrigendum.py) is IMPORTED and unchanged: its reader `rd`; its form -- one generated entry, each line it corrects
### quoted with its place, the corrected reading and its source, the figures read from their banks and checked before any write, `dry` then
### `land` -- is carried, as b689, b690 and b692 carried it. Every figure is read, none typed:
###   the two entry lines: PLACE-papers FINDINGS.md, the lines of b692's entry carrying "LOAD led by ." and "1.53. --";
###   LOAD: relay data/b692_circuit_SIDE-explicit-formula_v0.34.1.txt, its verdict line, read by a needle that passes a dotted name (the
###         three highest up to the line's closing ".**");
###   the factor: relay data/b692_suite_load.txt, its verdict line, the number before the line's closing ".**";
###   the cause: tools/b692_record.py :1349 and :1352 (the sealed needles) and data/b692_defects.txt (m), which carries both figures.
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b693_record's
### guarded landing, data/b693_corrigendum.txt (.json). Written by the Write tool at b693; it writes those two banks and the one FINDINGS entry.
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
PP = 'D:/MY-DOwnloads/PLACE-papers'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b678_corrigendum as C78   # noqa: E402  ### b678's tool, imported unchanged: rd
from b652_record import conv     # noqa: E402  ### the one conversion

ENTRY = 9462                     # ### b692's entry head, FINDINGS
READING = 'b692_circuit_SIDE-explicit-formula_v0.34.1.txt'
LOAD_NEEDLE = re.compile(r'LOAD`S THREE HIGHEST (.+?)\.\*\*\s*$')          # ### passes the dots of a name; stops at the line's ".**"
FACTOR_NEEDLE = re.compile(r'THE FACTOR (\d+(?:\.\d+)?)\.\*\*\s*$')         # ### the number alone, the closing period left out
SEALED_LOAD, SEALED_FACTOR = 1349, 1352
TITLE = ('## Corrigendum to b692’s entry (FINDINGS :9462): LOAD’s three highest and the SUITE-LOAD factor, two figures the sealed record '
         'tool mis-read')


def at(path, needle):
    """[(line, text)] of the file's lines carrying the needle."""
    return [(i + 1, l) for i, l in enumerate(C78.rd(path).split(NL)) if needle in l]


def compose():
    F = os.path.join(PP, 'FINDINGS.md')
    head = at(F, '## The dependency-circuit reading at SIDE-explicit-formula v0.34.1')
    lo = [x for x in at(F, 'LOAD led by .') if x[0] > ENTRY]
    fa = [x for x in at(F, 'the factor 1.53. --') if x[0] > ENTRY]
    rb = [(i, l) for i, l in enumerate(C78.rd(os.path.join(D, READING)).split(NL), 1) if LOAD_NEEDLE.search(l)]
    sb = [(i, l) for i, l in enumerate(C78.rd(os.path.join(D, 'b692_suite_load.txt')).split(NL), 1) if FACTOR_NEEDLE.search(l)]
    rec = C78.rd(os.path.join(T, 'b692_record.py')).split(NL)
    nl_, nf_ = rec[SEALED_LOAD - 1], rec[SEALED_FACTOR - 1]
    dm = C78.rd(os.path.join(D, 'b692_defects.txt'))
    mrow = re.search(r'(?ms)^    \(m\) .*?(?=^    \([a-z]\) |\Z)', dm)
    load = LOAD_NEEDLE.search(rb[0][1]).group(1) if len(rb) == 1 else None
    factor = FACTOR_NEEDLE.search(sb[0][1]).group(1) if len(sb) == 1 else None
    mtext = ' '.join(mrow.group(0).split()) if mrow else ''
    ok = (len(head) == 1 and head[0][0] == ENTRY and len(lo) == 1 and len(fa) == 1 and load and factor
          and r"LOAD`S THREE HIGHEST ([^.]*)\.\*\*" in nl_ and r"THE FACTOR ([\d.]+)" in nf_
          and load in mtext and ('the factor %s' % factor) in mtext)
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ (head %s, load line %d, factor line %d, reading %d, suite load %d, needles %s/%s, (m) carries '
                 'both %s) -- NOTHING WRITTEN' % ([h[0] for h in head], len(lo), len(fa), len(rb), len(sb), r"([^.]*)\.\*\*" in nl_,
                                                 r"([\d.]+)" in nf_, bool(load and factor and load in mtext)))
    return dict(head=head[0], lo=lo[0], fa=fa[0], rb=rb[0], sb=sb[0], load=load, factor=factor, nl=nl_.strip(), nf=nf_.strip(),
                m_line=dm[:mrow.start()].count(NL) + 1)


def entry_text(s):
    L = ['', TITLE, '',
         'b692’s entry, sealed, prints two figures its banks do not carry. (1) FINDINGS.md :%d, its readings paragraph, reads “LOAD led by .” -- '
         'the figure absent. The reading bank’s LOAD line carries the three highest as “%s” (relay data/%s :%d): LOAD is led by %s. (2) '
         'FINDINGS.md :%d, its SUITE-LOAD paragraph, reads “the factor 1.53. --”, a doubled period. The bank carries “THE FACTOR %s.**” (relay '
         'data/b692_suite_load.txt :%d): the factor is %s, the period the bank’s own. The cause by line: the sealed record tool’s two needles, '
         'relay tools/b692_record.py :%d, whose LOAD group `%s` stops at the first dot of a dotted name and so found nothing, and :%d, whose '
         'factor group `%s` takes the bank’s closing period. Found in b692’s entry dry run after the seal, the tool sealed, so the entry landed '
         'as composed; lettered b692’s defect (m), the seat’s (relay data/b692_defects.txt :%d). The entry, sealed, is not edited -- this entry '
         'is its correction; the figures stand as the banks give them. Nothing here proves RH or GRH.' % (
             s['lo'][0], s['load'], READING, s['rb'][0], s['load'], s['fa'][0], s['factor'], s['sb'][0], s['factor'], SEALED_LOAD,
             r'([^.]*)\.\*\*', SEALED_FACTOR, r'([\d.]+)', s['m_line']), '',
         '*Filed at b693 on the author’s ruling `(R303)`(2): generated by relay `tools/b693_corrigendum.py` in the corrigendum form of relay '
         '`tools/b678_corrigendum.py` (its reader imported unchanged), banked as relay `data/b693_corrigendum.txt`, the corrigenda bank '
         '`data/b675_corrigenda.txt` appended at row (7); it answers b692’s defect (m).*', '']
    return NL.join(L)


def bank_lines(s, landed_line=None):
    L = ['b693 -- THE CORRIGENDUM, (R303)(2): b692`S TWO POST-SEAL FIGURES, ITS DEFECT (m), ANSWERED BY ONE GENERATED FINDINGS ENTRY IN b678`s FORM',
         '', '### rows are the corrected line and the lines that correct it, each read from its bank by line; the sealed entry is not rewritten.', '',
         '  THE ENTRY                PLACE-papers FINDINGS.md :%d | %s' % (s['head'][0], s['head'][1].strip()[:120]),
         '  (1) AS PRINTED           FINDINGS.md :%d | ... LOAD led by . ...' % s['lo'][0],
         '  (1) THE BANK             relay data/%s :%d | LOAD`S THREE HIGHEST %s' % (READING, s['rb'][0], s['load']),
         '  (2) AS PRINTED           FINDINGS.md :%d | ... the factor 1.53. -- ...' % s['fa'][0],
         '  (2) THE BANK             relay data/b692_suite_load.txt :%d | THE FACTOR %s.**' % (s['sb'][0], s['factor']),
         '  THE SEALED NEEDLES       relay tools/b692_record.py :%d | %s' % (SEALED_LOAD, s['nl']),
         '                           relay tools/b692_record.py :%d | %s' % (SEALED_FACTOR, s['nf']),
         '  THE DEFECT               relay data/b692_defects.txt :%d | (m)' % s['m_line'],
         '', '### ### **LOAD LED BY %s ; THE FACTOR %s ; THE SEALED ENTRY UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
             s['load'], s['factor'], landed_line or 'NOT YET WRITTEN')]
    return L


def main(route):
    s = compose()
    text = entry_text(s)
    import b693_record as REC
    if route == 'dry':
        REC.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(bank_lines(s)[-1])
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b693_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b693_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b693_corrigendum.txt')
    open(p + '.tmp', 'wb').write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, load=s['load'], factor=s['factor'],
             printed=dict(load=s['lo'][0], factor=s['fa'][0]), banks=dict(reading=[READING, s['rb'][0]], suite_load=['b692_suite_load.txt', s['sb'][0]]),
             needles=dict(load=[SEALED_LOAD, s['nl']], factor=[SEALED_FACTOR, s['nf']]))
    p = os.path.join(D, 'b693_corrigendum.json')
    open(p + '.tmp', 'wb').write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b693_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
