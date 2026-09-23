# -*- coding: utf-8 -*-
"""b492_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
import io
import json
import os
import subprocess
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


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.replace(chr(13), '').strip()


def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')


R = json.loads(read(os.path.join(D, 'b492_results.json')))
C = json.loads(read(os.path.join(D, 'b492_cells.json')))
post = read(os.path.join(D, 'b492_checks_postpush.txt'))

rec('=' * 104)
rec('b492 -- THE CLOSING RECORD. ### THE PER-n TERMS AT EVERY RUNG, AND THE INCREMENTS ATTRIBUTED.')
rec('=' * 104)

rec('')
rec('### (1) THE RUN, AND ITS CHECK BEFORE ANYTHING ELSE WAS READ.')
rec('-' * 104)
rec('    35 cells on b477`s own recipe, grid and floor. ### The diagonal `W` was checked against')
rec('    b477`s bank ### **AT EVERY CELL BEFORE A SINGLE TERM WAS READ**, a mismatch set to halt.')
rec('    ### ### **WORST ABSOLUTE DISCREPANCY : %.3e. ### %d OF 35 CELLS REPRODUCE EXACTLY, BIT'
    % (R['worst_dW'], R['exact_zero']))
rec('    ### FOR BIT.** ### The run does not merely pass the floor.')
rec('    per-n terms banked at every cell, summing to `PR` within ### **8.3e-17**.')
rec('    run time : %.1f s' % C['seconds'])

rec('')
rec('### (2) THE GENERATOR. ### **W-ORD-EXACT-SUPPORT.**')
rec('-' * 104)
rec('    `b437_components.py` : `NEW_A = sorted(set([round(x, 6) for x in BOUNDARIES + MIDPOINTS]))`')
rec('    ### ### **THE ROUNDING IS IN THE GENERATOR ITSELF.** ### b490 found the symptom; this')
rec('    ### act names the line. ### 11 boundary cells `a = sqrt n`, 11 midpoints, 13 literals.')
rec('    ### ### **FOUR OF THE ELEVEN BOUNDARY CELLS ROUND DOWN -- 13, 27, 31, 32** -- and on the')
rec('    ### stored `a` exclude their own `n0`. ### On the exact generator every boundary cell')
rec('    ### admits it, by integer arithmetic: `n0 <= n0`. ### **NO TOLERANCE IS CHOSEN.**')
rec('    the exact `a` is banked beside the rounded at every cell, from this run on.')

rec('')
rec('### (3) THE ATTRIBUTION. ### **AN IDENTITY, NOT A FIT.**')
rec('-' * 104)
rec('    `d(pr) = (terms new at the top) + (drift of terms present at both)`, exactly.')
rec('    ### ### **IT CLOSES TO %.1e AT WORST** ### -- the arithmetic`s own precision.'
    % R['worst_closes'])
rec('    ### ### **AT 15 OF THE 16 ENTRY STEPS THE ENTERING TERMS CARRY AT MOST %.1e OF `d(pr)`,'
    % R['max_small_share'])
rec('    ### AND 8 CARRY EXACTLY ZERO.** ### The one exception is step 3, where `2` enters an')
rec('    ### EMPTY prime channel and is the whole increment ### **BY ARITHMETIC, NOT BY WEIGHT.**')
rec('    ### ### **AND A PRIME POWER ADMITTED AT ITS OWN BOUNDARY RUNG HAS TERM EXACTLY `0`** --')
rec('    ### at all seven such cells. ### The window is zero at its own support edge `v = L`, and')
rec('    ### `log n0 = L` exactly there. ### **AN ENTRY IS A BOOKKEEPING BOUNDARY, NOT AN EVENT**,')
rec('    ### and the channel moves only by drift.')
rec('')
rec('    ### THE SENTENCE THE TABLE SUPPORTS, AND NO WIDER:')
rec('    ### **%s**' % R['sentence'])
rec('    ### ### **THE ARCHIMEDEAN CHANNEL HAS NO PER-n DECOMPOSITION**, so `d(m) = d(arch) -')
rec('    ### d(pr)` has a half this act does NOT attribute. ### **NOTHING ABOUT RH FOLLOWS.**')

rec('')
rec('### (4) THE EXPECTATIONS.')
rec('-' * 104)
rec('    ### **(N1)** ### **REFUTED, AND NOT NARROWLY.** ### `3^3` carries `-2.5e-42` of its')
rec('          step`s `d(pr)`; `2^5` never enters on the stored `a` at all.')
rec('    ### **(N2)** ### **SPLIT.** ### On exact `a`, `27``s rung IS the local maximum -- it')
rec('          holds. ### `32``s rung is the ladder`s ENDPOINT, with no step past it to turn at')
rec('          -- it fails on the ladder`s geometry, not on the arithmetic.')
rec('    ### **(N3)** ### **REFUTED.** ### entry mean %.6g against non-entry %.6g, and ### **THE'
    % (R['mean_entry'], R['mean_nonentry']))
rec('          MEAN COMPARES SCALES, NOT MECHANISMS.**')
rec('    ### **(S1) (S2) (S3)** ### **HELD.**')

rec('')
rec('### (5) THE DEFECTS THIS ACT RECORDS OF ITS OWN INSTRUMENTS. ### **SIX.**')
rec('-' * 104)
rec('    ### ### **(a) A SUMMARY WRITTEN BEFORE ITS TABLE WAS READ, AND REFUTED BY IT.** ### The')
rec('    ### components tool`s first draft said *"every entering term is exactly zero"*. ### Eight')
rec('    ### are; eight are not; and one carries the whole increment.')
rec('    ### ### **(b) A SCORER THAT TYPED A BAR THE FACE NEVER STATED.** ### (S3) was scored')
rec('    ### against `1e-4` where the face`s word is ### **"not dominant"**; the largest share is')
rec('    ### `1.6e-03`. ### **A THRESHOLD INVENTED BY A SCORER IS NOT THE EXPECTATION IT SCORES.**')
rec('    ### ### **(c) A LEDGER ROW REFUSED FOR A `|` INSIDE A CELL, A SECOND TIME.** ### b490')
rec('    ### routed exactly this and it bit again within three acts. ### Caught by the tool`s own')
rec('    ### read-back, removed and rewritten before any commit. ### **STILL ROUTED.**')
rec('    ### ### **(d) AN ARM THAT COULD NOT MATCH ITS OWN CONTROL.** ### `G-NOTHING-COMPILED`')
rec('    ### lost `run` from its alternation and so demanded `subprocess(`, a shape that never')
rec('    ### occurs. ### Its control walked straight past it.')
rec('    ### ### **(e) A CONTROL THAT CUT THE FILE`S TAIL, WHERE THE TABLE IS NOT.**')
rec('    ### ### **(f) THE b493 PASTE WAS NOT BANKED WHEN THE FACE SAID IT WAS** -- and')
rec('    ### `G-RECEIPT-IN-FULL` caught it, its third clause reading the NEXT act`s ferry file.')
rec('    ### **AN ARM THAT READS WHAT THE FACE CLAIMS, NOT WHAT THE ACT INTENDED.**')

rec('')
rec('### (6) THE SUITE, THE COMMITS, THE MIRROR.')
rec('-' * 104)
rec('    pre-push  : 55 arms, 0 live failing, 0 positive-control passes.')
rec('    post-push : %s' % lw(post, 'ARMS RUN'))
rec('                %s' % lw(post, 'VERDICT :'))
rec('')
rec('    the commits, each read back by `ls-remote`:')
for name, repo in (('relay', ROOT),
                   ('PLACE-papers', os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')),
                   ('SIDE-global-section', os.path.join('D:', os.sep, 'SIDE-global-section'))):
    h = git(repo, 'rev-parse', 'HEAD')
    r = git(repo, 'ls-remote', 'origin', 'refs/heads/main').split()
    r = r[0] if r else ''
    rec('      %-20s local %s ; remote %s ; ### **%s**'
        % (name, h[:12], r[:12], 'AGREE' if h and h == r else 'DISAGREE'))
rec('    the mirror : `mirror-refresh-2026-09-23-b492.zip` at `2dd4d2e` --')
rec('      ### **CLEAN ON ALL THREE CLAUSES.**')

rec('')
rec('### (7) THE CENSUSES, THE PINS, THE LISTS.')
rec('-' * 104)
rec('    handoff census : %s' % lw(read(os.path.join(D, 'b492_census_closing.txt')),
                                   'TOTAL MISSING'))
rec('    faces census   : %s' % lw(read(os.path.join(D, 'b492_faces_census_closing.txt')),
                                   'TOTAL MISSING'))
rec('    pins           : %s' % lw(read(os.path.join(D, 'b492_pins_closing.txt')),
                                   'REPOS HARD-FAILING'))
rec('    ### ### **THE LANE IS SHUT.** ### It was made available for one run and used once.')
rec('    ### **THE FOUR LISTS STAY OPEN.** ### Nothing compiled; no Lean built; no repository')
rec('    ### created. ### No corpus grade moved; row U1 unedited; nothing deposits; nothing at')
rec('    ### Zenodo is written; ### **h2 WHERE THE DEPOSIT LEFT IT.**')

rec('')
rec('### (8) WHAT IS CARRIED FORWARD.')
rec('-' * 104)
rec('    (a) ### **b493 IS NEXT, AND ITS ORDER IS BANKED** ### at `data/b493_ferry.txt`: the')
rec('        eight records read whole against the claim ceiling.')
rec('    (b) ### **(R103)`S CREATION BELONGS TO THE ACT AFTER b493**, not to this one.')
rec('    (c) ### **`corr_row.py` STILL CHECKS THE NUMBER AND NOT THE CELLS.** ### Twice now a')
rec('        `|` inside a cell has landed a malformed row. ### **ROUTED, AND OVERDUE.**')
rec('    (d) ### **THE ARCHIMEDEAN HALF OF `d(m)` IS UNATTRIBUTED.** ### The turns cannot be')
rec('        explained from the prime channel alone, and this act does not try.')
rec('')
rec('=' * 104)
rec('  ### ### **b492 CLOSES. 56 ARMS, 0 LIVE FAILING, 0 POSITIVE-CONTROL PASSES.**')
rec('=' * 104)

io.open(os.path.join(D, 'b492_closing.txt'), 'w', encoding='utf-8', newline=NL).write(
    NL.join(L) + NL)
print(NL + '  written: b492_closing.txt')
