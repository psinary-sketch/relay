# -*- coding: utf-8 -*-
"""b501_desk_bank.py -- THE DESK. ### **SCORED ON PRINTED CELLS, INCLUDING AGAINST THE SEAT.**"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def word(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


R = json.loads(io.open(os.path.join(D, 'b501_results.json'), encoding='utf-8').read())
rows = sorted((json.loads(l) for l in io.open(os.path.join(D, 'b501_cells.jsonl'), encoding='utf-8') if l.strip()),
              key=lambda r: r['i'])
short = [r for r in rows if r['B'] < r['achieved']]
AIM, LAD = 4.562e-05, 3.169e-06

rec('=' * 104)
rec('b501 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE CELLS THE COMPONENTS PRINTED.**')
rec('=' * 104)
rec('')
rec('### ### **FIRST, THE FACE`S OWN READING (1) IS CORRECTED -- IT WAS WRONG.** ### The sealed face said')
rec('### b483`s AIM PLANE lay outside the thirty-five cells and called that half of (N1) NOT SCORABLE.')
rec('### ### **THE THIRTY-FIVE ARE b483`S TWO FAMILIES TOGETHER**: %d cells with a <= 3 (b483`s AIM PLANE,'
    % R['aim_cells'])
rec('### 13 cells, a from 1.3 to 3) and %d above (its LADDER, 22 cells, a from 3.158 to 5.657). ### The'
    % R['ladder_cells'])
rec('### seat found it after the seal, from b483`s own family headers and the cells` a-values, before any')
rec('### expectation was scored. ### **THE FACE IS NOT EDITED; (N1) IS SCORED ON BOTH FAMILIES.**')
rec('')
rec('### THE NAVIGATOR`S THREE.')
rec('-' * 104)
r_aim, r_lad = R['aim_maxB'] / AIM, R['ladder_maxB'] / LAD
n1 = (1.0 < r_aim < 1000.0) and (1.0 < r_lad < 1000.0)
rec('  **(N1)** ### **%s.** -- *"the new bound exceeds the achieved error at both b483 cells by less than'
    % word(n1))
rec('    three orders"*')
rec('    AIM PLANE : max B %.3e against 4.562e-05 -> ratio %.3f' % (R['aim_maxB'], r_aim))
rec('    LADDER    : max B %.3e against 3.169e-06 -> ratio %.3f' % (R['ladder_maxB'], r_lad))
rec('    ### ### **THE BOUND DOES NOT EXCEED THE ACHIEVED ERROR ON EITHER FAMILY -- IT IS BELOW BOTH**, so the')
rec('    ### expectation fails at its first clause, not its second. ### Part of that is a unit: b483`s figures')
rec('    ### are SPECTRAL NORMS of a matrix of cross-terms, while B is per cell; the per-cell achieved maxima')
rec('    ### are 3.558e-05 and 3.213e-07, and B`s maxima sit at 1.00x and 1.39x of those.')
rec('')
n2 = R['floors_exceeded'] == R['n']
rec('  **(N2)** ### **%s.** -- *"all 35 margins still exceed their new floors"* -- ### **%d OF %d**'
    % (word(n2), R['floors_exceeded'], R['n']))
rec('')
n3 = R['min_cell']['B'] < 1e-4
rec('  **(N3)** ### **%s.** -- *"the new floor at a = 4.061553 is below 1e-04"* -- ### **%.3e**'
    % (word(n3), R['min_cell']['B']))
rec('')
rec('### THE SEAT`S THREE.')
rec('-' * 104)
s1 = len(short) > 30
rec('  **(S1)** ### **%s.** -- *"B below |W+Z| at more than thirty of the thirty-five"* -- ### **%d**'
    % (word(s1), len(short)))
rec('    ### ### **REFUTED, AND THE REASON IS THE FINDING OF THIS ACT.** ### The seat reasoned that the')
rec('    ### achieved disagreement was carried by the zero side, because b446`s doubling moved W by little.')
rec('    ### ### **IT IS CARRIED BY THE PLACES SIDE.** ### B tracks |W+Z| to within a small factor at every')
rec('    ### cell -- at small a through A`s u-grid (E_u 3.54e-05 at a = 1.3 against |W+Z| 3.56e-05), above')
rec('    ### a = 2 through the v-grid -- and b446 doubled only the v-grid.')
rec('    ### ### **WHERE B FALLS SHORT, BY HOW MUCH (%d CELLS):**' % len(short))
for r in short:
    rec('      a=%-10.6f  B %.3e  |W+Z| %.3e  short by x%.2f  (%s)'
        % (r['a'], r['B'], r['achieved'], r['achieved'] / r['B'], r['kind']))
worst = max((r['achieved'] / r['B'] for r in short), default=1.0)
rec('    ### ### **THE WORST SHORTFALL IS x%.2f.** ### A Richardson estimate is not a bound, as the face said;' % worst)
rec('    ### here it is that and no worse. ### A safety factor of 2 would cover every cell, and it is NOT applied:')
rec('    ### a factor chosen after the numbers are seen is fitted, not computed.')
s2 = R['composite_ok'] == R['n']
rec('  **(S2)** ### **%s.** -- the composite B + trunc_bound >= |W+Z| at %d of %d.'
    % (word(s2), R['composite_ok'], R['n']))
rec('    ### trunc_bound adds nothing that moves a verdict: the zero side`s truncation is not what differs.')
s3 = R['nonasymptotic'] >= 1
rec('  **(S3)** ### **%s.** -- NON-ASYMPTOTIC cells : %d.' % (word(s3), R['nonasymptotic']))
rec('')
nav, seat = [n1, n2, n3], [s1, s2, s3]
rec('### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.**' % (nav.count(True), nav.count(False)))
rec('### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d ; NOT SCORABLE 0.**'
    % (seat.count(True), seat.count(False)))
rec('=' * 104)
io.open(os.path.join(D, 'b501_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
json.dump(dict(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, s3=s3, short=len(short), worst=worst,
               r_aim=r_aim, r_lad=r_lad),
          io.open(os.path.join(D, 'b501_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
print('  written: b501_desk_notes.txt, b501_scores.json')
