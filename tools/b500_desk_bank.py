# -*- coding: utf-8 -*-
"""b500_desk_bank.py -- THE DESK. ### **SCORED ON PRINTED CELLS, INCLUDING AGAINST THE SEAT.**"""
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


R = json.loads(io.open(os.path.join(D, 'b500_results.json'), encoding='utf-8').read())
F = json.loads(io.open(os.path.join(D, 'b500_results_first.json'), encoding='utf-8').read())
n1 = R['nonzero_exits'] == 0
n2 = R['all_standard_three']
n3 = len(R['built_lines']) < 70
s1 = n1 and len(R['ends']) == 2
s2 = R['built_mathlib'] == 0
s3 = R['r82'] == 'HOLDS'
rec('=' * 104)
rec('b500 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE CELLS THE LOG PRINTED.**')
rec('=' * 104)
rec('')
rec('### THE NAVIGATOR`S THREE.')
rec('-' * 104)
rec('  **(N1)** ### **%s.** -- *"0 non-zero exits"* -- `END` lines %d, ### **NON-ZERO %d**'
    % (word(n1), len(R['ends']), R['nonzero_exits']))
rec('  **(N2)** ### **%s.** -- *"all three profiles the standard three"* -- %s'
    % (word(n2), {k: v['verdict'] for k, v in R['profiles'].items()}))
rec('    ### ### **AND THE FIRST READING SAID ABSENT FOR ALL THREE.** ### b497`s axiom matcher was')
rec('    ### anchored at the start of a line, and the launcher stamps an instant at the start of every')
rec('    ### line, so it could not match a real run. ### First run: %s.'
    % {k: v['verdict'] for k, v in F['profiles'].items()})
rec('  **(N3)** ### **%s.** -- *"fewer than seventy modules in all"* -- ### **`Built` LINES : %d**'
    % (word(n3), len(R['built_lines'])))
rec('')
rec('### THE SEAT`S THREE.')
rec('-' * 104)
rec('  **(S1)** ### **%s.** -- both `END` lines exit 0.' % word(s1))
rec('  **(S2)** ### **%s.** -- `Mathlib.*` modules built : %d ; `Zeta23.*` : %d.'
    % (word(s2), R['built_mathlib'], R['built_zeta']))
rec('  **(S3)** ### **%s.** -- (R82) : %s.' % (word(s3), R['r82']))
rec('')
nav, seat = [n1, n2, n3], [s1, s2, s3]
rec('### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.**' % (nav.count(True), nav.count(False)))
rec('### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d ; NOT SCORABLE 0.**'
    % (seat.count(True), seat.count(False)))
rec('=' * 104)
io.open(os.path.join(D, 'b500_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
json.dump(dict(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, s3=s3), io.open(
    os.path.join(D, 'b500_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
print('  written: b500_desk_notes.txt, b500_scores.json')
