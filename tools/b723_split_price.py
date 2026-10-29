# -*- coding: utf-8 -*-
"""b723_split_price.py -- (R333)(8): THE LEDGER SPLIT'S BUDGET PRINTED BEFORE ANY CUT. Written whole at b723 by the Write tool.

The author's word (5): the split lands "where the seat's printed budget holds both its controls and the act's close, else carried whole
to b724 with its price". Read-only: FINDINGS.md and OPEN_TRAILS.md at PLACE-papers HEAD (line counts); every `FINDINGS :NNNN` occurrence
by git grep at HEAD in relay data/ and tools/ and PLACE-papers *.md, classed by the cut :456-:6949 (ARCHIVED inside it, SHIFTED below
it by 6494 lines, STAYS above it), the act's own b723_ files counted apart; b722's close timed from its step rows (data/b722_steps.json);
b680's price (data/b680_split_price.txt) printed beside. Nothing cut, nothing written but the bank.

  bank   -> data/b723_split_price.txt
"""
import io
import json
import os
import re
import subprocess
import sys
import time

NL = chr(10)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_ = os.path.join(ROOT, 'data')
PP = 'D:/MY-DOwnloads/PLACE-papers'
OUT = os.path.join(D_, 'b723_split_price.txt')
A, B = 456, 6949
PAT = r'FINDINGS[^:\n]{0,3}:[0-9]{2,5}'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True).stdout.decode('utf-8', 'replace')


def sites():
    cnt, own = {}, {}
    for repo, paths, kind in ((ROOT, ['data/', 'tools/'], 'relay'), (PP, ['*.md'], 'PLACE-papers')):
        for l in g(repo, 'grep', '-o', '-E', PAT, 'HEAD', '--', *paths).split(NL):
            if not l.strip():
                continue
            _rev, path, hit = l.split(':', 2)
            n = int(re.search(r':([0-9]+)$', hit).group(1))
            cls = 'ARCHIVED' if A <= n <= B else ('SHIFTED' if n > B else 'STAYS')
            sub = 'ledger' if path in ('FINDINGS.md', 'OPEN_TRAILS.md') else ('tool' if path.startswith('tools/') else
                                                                             ('bank' if kind == 'relay' else 'paper'))
            cnt[(kind, sub, cls)] = cnt.get((kind, sub, cls), 0) + 1
            if os.path.basename(path).startswith('b723_'):
                own[cls] = own.get(cls, 0) + 1
    return cnt, own


def close_time():
    st = json.load(io.open(os.path.join(D_, 'b722_steps.json'), encoding='utf-8'))
    rows = st['rows'] if isinstance(st, dict) else st
    c8 = [r['at'] for r in rows if r.get('phase') == 'component 8']
    cl = [r['at'] for r in rows if r.get('phase') == 'closing']
    t = lambda s: time.mktime(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))   # noqa: E731
    return c8[0], cl[-1], (t(cl[-1]) - t(c8[0])) / 3600.0


def bank():
    cnt, own = sites()
    fl = g(PP, 'show', 'HEAD:FINDINGS.md').count(NL)
    ol = g(PP, 'show', 'HEAD:OPEN_TRAILS.md').count(NL)
    c0, c1, hrs = close_time()
    b680 = [l for l in io.open(os.path.join(D_, 'b680_split_price.txt'), encoding='utf-8').read().split(NL) if l.startswith('### ### **')]
    tot = {}
    for (_k, _s, cls), v in cnt.items():
        tot[cls] = tot.get(cls, 0) + v
    tools_moved = sum(v for (k, s, c), v in cnt.items() if s == 'tool' and c != 'STAYS')
    moved = tot.get('ARCHIVED', 0) + tot.get('SHIFTED', 0)
    out = ['b723 -- (R333)(8): THE LEDGER SPLIT`S BUDGET, PRINTED BEFORE ANY CUT (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
           '### Written by tools/b723_split_price.py bank. Read-only: the ledgers at PLACE-papers HEAD %s; `FINDINGS :NNNN` occurrences by git grep at' % g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
           '### HEAD (relay data/ and tools/, PLACE-papers *.md), each occurrence counted (b680 counted once per FINDINGS line per site, its own rule,',
           '### so the two figures differ in rule as well as date). ARCHIVED: the cited line inside :456-:6949; SHIFTED: below it, up by 6494 lines;',
           '### STAYS: above it. Nothing cut; no bank, ledger or paper rewritten.', '',
           '## THE LEDGERS AT HEAD', '  FINDINGS.md %d lines (b680 read 9077) ; OPEN_TRAILS.md %d lines' % (fl, ol), '',
           '## THE CITATION OCCURRENCES (repo ; kind ; class ; count)']
    for k in sorted(cnt):
        out.append('  %-13s %-7s %-9s %6d' % (k + (cnt[k],)))
    out += ['  TOTAL: ARCHIVED %d ; SHIFTED %d ; STAYS %d ; MOVED %d ; in live tools MOVED %d ; in b723`s own files ARCHIVED %d, SHIFTED %d' % (
               tot.get('ARCHIVED', 0), tot.get('SHIFTED', 0), tot.get('STAYS', 0), moved, tools_moved, own.get('ARCHIVED', 0), own.get('SHIFTED', 0)),
            '  b680 beside: ' + (b680[0] if b680 else 'NOT READ'), '',
            '## THE WORK (R333)(8) NAMES, AS PRICED BY THE SEAT',
            '  (a) the cut tool: archive-3 sliced byte-exact from FINDINGS :456-:6949 and from OPEN_TRAILS`s record stream filed before b600 (the',
            '      active sections kept), reassembly verified, one offset-table row per cut -- tools/ledger_split.py moves by anchors and re-pins',
            '      no line citation (b680 :3-:6), so the line-offset form is new work: about 1-1.5 h with its reassembly control;',
            '  (b) the resolver in three tools (rowgen, the citation check, the Correspondence generator), each mapping a `FINDINGS :NNNN` read at',
            '      the citing act`s own date through the offset table -- the citation`s date is not in the citation, so each tool needs the citing',
            '      file`s act read from its path or its commit: about 2-3 h with a control per tool;',
            '  (c) the controls before the cut lands: a sample drawn by a printed rule from banks, ledgers and papers resolving to the same text',
            '      before and after, a planted wrong offset failing, the reassembly equal; the pointer headers in each live file: about 1 h;',
            '  SPLIT, SEAT`S ESTIMATE: about 4-5.5 h, before the close.',
            '## THE CLOSE, TIMED FROM b722`s ROWS: its last component`s first step %s to its closing %s -- %.1f h; b723`s close runs the same' % (c0, c1, hrs),
            '  toolset at v1.3.0, whose citation check and record composer read `FINDINGS :NNNN` lines (%d occurrences in live tools moved by the cut).' % tools_moved,
            '',
            '## THE READING',
            '  The cut moves %d citation occurrences, %d of them in the live tools the close runs and %d in this act`s own banks; landed before the' % (
                moved, tools_moved, own.get('ARCHIVED', 0) + own.get('SHIFTED', 0)),
            '  close, every one of the close`s citation and record arms reads FINDINGS through a resolver built and controlled in the same act,',
            '  never run under a close. No clock bounds the act; the seat`s budget is the close as b722 timed it (%.1f h) with its arms on tested' % hrs,
            '  tools. The split adds about 4-5.5 h ahead of it and puts those arms on the untried resolver: the seat reads that as the budget not',
            '  holding both, a reading, printed for the author`s strike.', '',
            '### ### **THE LEDGER SPLIT: CARRIED WHOLE TO b724 WITH ITS PRICE -- %d CITATION OCCURRENCES MOVED (%d IN LIVE TOOLS), THE SPLIT ABOUT 4-5.5 H BEFORE A CLOSE OF %.1f H ; NOTHING CUT.**' % (
                moved, tools_moved, hrs)]
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline='\n').write(NL.join(out) + NL)
    os.replace(OUT + '.tmp', OUT)
    print(NL.join(out))
    print('written data/b723_split_price.txt')


if __name__ == '__main__':
    if sys.argv[1:2] == ['bank']:
        bank()
    else:
        print(__doc__)
