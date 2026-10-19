# -*- coding: utf-8 -*-
"""b689_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R299)(2): b688's defect (f) answered by one generated FINDINGS entry in b678's corrigendum
form, the sealed entry itself unedited.

### b678's tool (tools/b678_corrigendum.py) is IMPORTED and unchanged: its `_quote` gives the sentence verbatim from the ledger (through a code
### span's closing backtick where a cut leaves one open), its form -- one generated entry, each corrected sentence quoted with its line, the
### corrected reading and its source, the counts diffed before any write, `dry` then `land` -- is carried. Its compose reads b676's Q0 rows
### and its HAND_COUNT 36, which are not this defect's; here the one row is (f)'s, read from the banks:
###   the sentence: FINDINGS :9320, the citation sentence of b688's entry (:9314), "the two commit cites ... tested directly";
###   the figure the citation bank gives: relay data/b688_citation_check.txt, its rows `MISS | commit | <sha>` each with a "tested directly by the
###     seat" note beneath, COUNTED here (b688's lesson: a figure is composed from its bank, never typed) -- three, at :96, :107, :116;
###   the correct source: b688's trail record's defects line, OPEN_TRAILS :14946, its (f).
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through
### b689_record's guarded landing, data/b689_corrigendum.txt (.json). Written by the Write tool at b689; it writes those two banks and the one
### FINDINGS entry.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b678_corrigendum as C78   # noqa: E402  ### b678's tool, imported unchanged: _quote, rd
from b652_record import conv     # noqa: E402  ### the one conversion

ENTRY, SENTENCE_LINE, TRAIL_LINE = 9314, 9320, 14946
SENTENCE = 'the two commit cites outside the route’s repositories tested directly'
WRITTEN_FIGURE = 'two'
CIT_BANK = 'b688_citation_check.txt'
WORDS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
TITLE = '## Corrigendum to b688’s entry (FINDINGS :9314): the commit cites tested directly were three, not two'


def tested_rows():
    """the citation bank's commit-cite rows with a direct test beneath: [(line, sha, the repository the note names)]."""
    L = C78.rd(os.path.join(D, CIT_BANK)).split(NL)
    out = []
    for i, l in enumerate(L):
        m = re.match(r'^  MISS \| commit \| ([0-9a-f]{7,40})$', l)
        if not m:
            continue
        note = next((L[j] for j in range(i + 1, min(i + 4, len(L))) if L[j].startswith('### the miss tested directly by the seat')), None)
        if note:
            k = re.search(r'is a commit of (SIDE-[\w-]+)', note + ' ' + (L[L.index(note) + 1] if L.index(note) + 1 < len(L) else ''))
            out.append((i + 1, m.group(1), k.group(1) if k else '?'))
    return out


def compose():
    led = C78.rd(os.path.join(PP, 'FINDINGS.md')).split(NL)
    if not led[ENTRY - 1].startswith('## SIDE-li-map re-cut'):
        sys.exit('### FINDINGS :%d IS NOT b688`s ENTRY -- NOTHING WRITTEN' % ENTRY)
    q, ext = C78._quote('FINDINGS.md', SENTENCE_LINE, SENTENCE)
    if q is None or q not in led[SENTENCE_LINE - 1]:
        sys.exit('### FINDINGS :%d DOES NOT CARRY THE SENTENCE -- NOTHING WRITTEN' % SENTENCE_LINE)
    tr = C78.rd(os.path.join(PP, 'OPEN_TRAILS.md')).split(NL)[TRAIL_LINE - 1]
    m = re.search(r"\(f\) THE SEAT'S: THE ENTRY SAYS TWO COMMIT CITES WERE TESTED DIRECTLY, THE CITATION BANK TESTS (\w+)\.", tr)
    if not tr.startswith('**Defects** (relay data/b688_defects.txt)') or not m:
        sys.exit('### OPEN_TRAILS :%d IS NOT b688`s DEFECTS LINE WITH ITS (f) -- NOTHING WRITTEN' % TRAIL_LINE)
    rows = tested_rows()
    return q, ext, rows, m.group(1).lower(), m.group(0)


def entry_text(q, ext, rows, trail_word, trail_clause):
    fig = WORDS.get(len(rows), str(len(rows)))
    cites = '; '.join('%s of %s (relay data/b688_citation_check.txt :%d)' % (sha, repo, ln) for ln, sha, repo in rows)
    L = ['', TITLE, '',
         'b688’s entry (FINDINGS :%d) says, in its citation sentence at :%d, “%s”; the citation bank it cites tests %s such cites directly, '
         'each a commit of a kernel outside the answer route’s repositories, noted beneath its mid-act check: %s. The figure as written, %s; the '
         'figure the bank gives, %s. The correct source is b688’s trail record’s defects line (OPEN_TRAILS :%d), whose (f) reads “%s” -- the '
         'figure three, as the bank gives it. The sealed entry stands as written and is pinned to nothing; this entry is its correction. Nothing '
         'here proves RH or GRH.' % (ENTRY, SENTENCE_LINE, q, fig, cites, WRITTEN_FIGURE, fig, TRAIL_LINE, trail_clause), '',
         '*Filed at b689 on the author’s ruling `(R299)`(2): generated by relay `tools/b689_corrigendum.py` in the corrigendum form of relay '
         '`tools/b678_corrigendum.py` (its quoting helper imported unchanged), banked as relay `data/b689_corrigendum.txt`, the corrigenda bank '
         '`data/b675_corrigenda.txt` appended; it answers b688’s defect (f) (relay `data/b688_defects.txt` :34).*', '']
    return NL.join(L)


def bank_lines(q, ext, rows, trail_word, landed_line=None):
    fig = WORDS.get(len(rows), str(len(rows)))
    L = ['b689 -- THE CORRIGENDUM, (R299)(2): b688`s DEFECT (f) ANSWERED BY ONE GENERATED FINDINGS ENTRY IN b678`s FORM',
         '', '### rows are the corrected sentence and the rows that correct it: the sentence (file :line, quoted verbatim) | the figure as written |',
         '### the bank`s rows that give the figure, each by line | the correct source. The ledger line is not rewritten and receives no pin.', '',
         '  THE SENTENCE   FINDINGS.md :%d (the citation sentence of b688`s entry at :%d) | "%s" | %s' % (SENTENCE_LINE, ENTRY, q, ext or 'the sentence verbatim'),
         '  AS WRITTEN     %s' % WRITTEN_FIGURE]
    L += ['  THE BANK`S ROW  relay data/b688_citation_check.txt :%d | MISS | commit | %s | tested directly by the seat beneath: a commit of %s' % (ln, sha, repo)
          for ln, sha, repo in rows]
    L += ['  THE SOURCE     OPEN_TRAILS.md :%d, b688`s trail record`s defects line, its (f): the figure %s' % (TRAIL_LINE, trail_word),
          '', '### THE COUNT: the bank`s directly tested commit cites %d (%s) ; the figure as written %s ; the trail line`s figure %s ; %s' % (
              len(rows), fig, WRITTEN_FIGURE, trail_word, 'THE BANK AND THE TRAIL AGREE' if trail_word == fig else '### THE BANK AND THE TRAIL DIFFER'),
          '', '### ### **THE SENTENCE AT FINDINGS :%d ; AS WRITTEN %s ; THE BANK %s (ROWS %s) ; THE TRAIL %s ; THE ENTRY AT FINDINGS :%s.**' % (
              SENTENCE_LINE, WRITTEN_FIGURE.upper(), fig.upper(), ', '.join(':%d' % r[0] for r in rows), trail_word.upper(), landed_line or 'NOT YET WRITTEN')]
    return L


def main(route):
    q, ext, rows, trail_word, trail_clause = compose()
    fig = WORDS.get(len(rows), str(len(rows)))
    if fig != trail_word or fig == WRITTEN_FIGURE:
        sys.exit('### THE BANK GIVES %s, THE TRAIL %s, THE ENTRY %s -- NOTHING WRITTEN' % (fig, trail_word, WRITTEN_FIGURE))
    text = entry_text(q, ext, rows, trail_word, trail_clause)
    import b689_record as REC
    if route == 'dry':
        REC.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text)[:2400])
        print(NL.join(bank_lines(q, ext, rows, trail_word)[-3:]))
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b689_corrigendum_landing.json', 'corrigendum', entry=ENTRY,
             check=[('FINDINGS.md', ENTRY, '## SIDE-li-map re-cut'), ('FINDINGS.md', SENTENCE_LINE, SENTENCE)], dry=False)
    ln = (REC.jl('b689_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(q, ext, rows, trail_word, ln)
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b689_corrigendum.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    j = (json.dumps(dict(entry_line=ln, title=TITLE, sentence=dict(file='FINDINGS.md', line=SENTENCE_LINE, quote=q), written=WRITTEN_FIGURE,
                         bank_rows=[dict(line=r[0], sha=r[1], repo=r[2]) for r in rows], trail=dict(line=TRAIL_LINE, figure=trail_word)),
                    indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, 'b689_corrigendum.json')
    open(p + '.tmp', 'wb').write(j)
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b689_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
