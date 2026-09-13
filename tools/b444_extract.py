# -*- coding: utf-8 -*-
"""b444_extract.py -- THE SURVEY. ### **WRITTEN BEFORE THE FACE. IT READS; IT COMPUTES NO CORRELATION AND NO
### RESIDUAL.** ### It prints the shapes of the banked tables and the floor's text, never their values."""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OUT = os.path.join(D, 'b444_extract.txt')
NL = chr(10)
SPAN = ['b433', 'b434', 'b435', 'b436', 'b437', 'b438', 'b439', 'b440', 'b441', 'b442', 'b443']

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
L, MISS, READS = [], [], [0]


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13) + NL, NL)
    except Exception:
        return ''


def quote(path, needle, clip=300):
    READS[0] += 1
    for i, ln in enumerate(read(path).splitlines()):
        if needle in ln:
            rec('      %s:%d  | %s' % (os.path.basename(path), i + 1, ln.strip()[:clip]))
            return i + 1
    MISS.append('%s : %r' % (os.path.basename(path), needle[:50]))
    rec('      ### **NOT LOCATED** : %s' % needle[:60])


def main():
    rec('=' * 100)
    rec('b444 -- THE FOLD, AND THE CHANNELS DECORRELATED. ### THE SURVEY.')
    rec('=' * 100)
    rec('')
    rec('### (1) THE SPAN RULE AND THE FOLD HEADINGS')
    quote(os.path.join(T, 'b363_span.py'), "heads = [m.start() for m in re.finditer(r'^## .*")
    quote(os.path.join(T, 'b363_span.py'), 'start = fold_act + 1')
    heads = [ln for ln in read(os.path.join(PP, 'FINDINGS.md')).splitlines() if ln.startswith('## ')
             and ('THE FOLD' in ln or 'folded at' in ln)]
    for h in heads[-4:]:
        rec('      heading | %s' % h[:120])
    rec('      headings matching the tool`s pattern (`— THE FOLD` at line end): %d of %d'
        % (len([h for h in heads if re.search(r'— THE FOLD\s*$', h)]), len(heads)))
    quote(os.path.join(PP, 'FINDINGS.md'), 'because a fold’s span has always ended before its filing act')
    rec('')
    rec('### (2) THE CLOSING BANKS IN THE ORDERED SPAN')
    for a in SPAN:
        f = os.path.join(D, ('b443r' if a == 'b443' else a) + '_closing.txt')
        rec('      %-6s %-22s lines %s' % (a, os.path.basename(f), len(read(f).splitlines()) or 'MISSING'))
    rec('')
    rec('### (3) WHICH OF THE ORDER`S ONE-STATEMENT CLAUSES LIE OUTSIDE THE SPAN')
    fnd = read(os.path.join(PP, 'FINDINGS.md'))
    for needle in ('| **b429** |', '| **b430** |', '| **b431** |'):
        quote(os.path.join(PP, 'FINDINGS.md'), needle, clip=200)
    rec('')
    rec('### (4) THE BANKED TABLES -- SHAPES ONLY')
    rungs = json.loads(read(os.path.join(D, 'b437_rungs.json')))
    rows = rungs['rows']
    full = [r for r in rows if r.get('zero') is not None]
    rec('      b437_rungs.json rows %d ; rows carrying zero/arch/pr/pole/resid %d ; fields %s'
        % (len(rows), len(full), sorted(full[0].keys())))
    chart = json.loads(read(os.path.join(D, 'b334_chart.json')))
    blk = chart['block']
    rec('      b334_chart.json block %d cells ; fields %s' % (len(blk), sorted(blk[0].keys())))
    rec('      b334 radii %s ; ladder full-cell radii overlap with them : %s'
        % (sorted(set(r['a'] for r in blk)), sorted(set(r['a'] for r in blk) & set(r['a'] for r in full))))
    rec('')
    rec('### (5) THE FLOOR AS b437 PRICED AND RESOLVED IT')
    quote(os.path.join(D, 'b437_closing.txt'), 'All three are far above the `1.49e-08` floor')
    quote(os.path.join(D, 'b437_closing.txt'), 'a = 5.385165   ratio 1.077773894')
    rec('')
    rec('### (6) THE ORIENTATION DIGEST')
    dig = read(os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md'))
    rec('      last refresh markers : %s' % re.findall(r'<!-- (b4\d\d) orientation refresh', dig))
    rec('')
    rec('=' * 100)
    rec('  ### READS ATTEMPTED : %d' % READS[0])
    rec('  ### MISSES          : %d %s' % (len(MISS), MISS or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)


if __name__ == '__main__':
    main()
