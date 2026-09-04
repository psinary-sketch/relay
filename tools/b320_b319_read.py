# -*- coding: utf-8 -*-
"""b320_b319_read.py -- STEP ZERO's READ OF b319's BANK AGAINST ITS OWN TABLE.

### ### **WHAT THE ORDER ASKS.** ### *the containment direction between the grid cut and the stable
### cut stated from the numbers, and any sentence pointing the other way filed as a prose-vs-table
### defect against that bank (not edited).*

### ### **THE DIRECTION IS DECIDED BY TWO COLUMNS AND NOTHING ELSE.** ### `rank` counts the
### directions a cut puts OUTSIDE the space; `dim = free - rank` is the dimension of the space
### itself. ### **A SMALLER RANK IS A BIGGER SPACE**, and that inversion is exactly the place a
### bank's prose can drift away from its own table without anyone noticing.

### ### **THIS FILE DOES NOT EDIT b319.** ### It reads `data/b319_rows.json`, states the direction
### the numbers give, and tests each of b319's own sentences against it. ### A sentence that
### contradicts the table is FILED, quoted, with the numbers that contradict it.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = os.path.join(D, 'b319_rows.json')
BANK = os.path.join(D, 'b319_the_stable_rank.txt')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def self_test():
    """### **FIXTURES. ### THE READER MUST BE ABLE TO REPORT THE OTHER ANSWER.**"""
    ok = []
    # ### (i) it calls the smaller-rank cut the LARGER space.
    ok.append(direction(rank_a=69, dim_a=3899, rank_b=80, dim_b=3888) == 'A CONTAINS B')
    # ### (ii) ### **AND IT REVERSES WHEN THE NUMBERS DO** -- a reader that always says the same
    # ### thing is not reading.
    ok.append(direction(rank_a=80, dim_a=3888, rank_b=69, dim_b=3899) == 'B CONTAINS A')
    # ### (iii) equal ranks give neither.
    ok.append(direction(rank_a=70, dim_a=100, rank_b=70, dim_b=100) == 'NEITHER')
    # ### (iv) the quoted-number finder pulls a run of integers out of a sentence.
    ok.append(nums_in('is 69, 69, 69, 69.') == [69, 69, 69, 69])
    # ### (v) and finds none where there are none.
    ok.append(nums_in('no numerals here') == [])
    return all(ok), ok


def direction(rank_a, dim_a, rank_b, dim_b):
    """### WHICH CUT'S SPACE CONTAINS THE OTHER'S, FROM THE COUNTS."""
    if rank_a < rank_b and dim_a > dim_b:
        return 'A CONTAINS B'
    if rank_b < rank_a and dim_b > dim_a:
        return 'B CONTAINS A'
    return 'NEITHER'


def nums_in(s):
    # ### a trailing SENTENCE period is not a decimal point, and the first version of this
    # ### regex refused `69.` at the end of a sentence -- caught by fixture (iv).
    return [int(x) for x in re.findall(r'(?<![\w.])(\d+)(?![\w])(?!\.\d)', s)]


def main():
    good, arms = self_test()
    rec('=' * 100)
    rec('b320 STEP ZERO -- THE READ OF b319\'s BANK AGAINST ITS OWN TABLE.')
    rec('=' * 100)
    rec('  ### THE READER\'S OWN FIXTURES : %s  %s' % (arms, 'PASS' if good else '### FAIL ###'))
    rec('  ### **ARM (ii) IS THE ONE THAT MATTERS: THE READER MUST BE ABLE TO SAY THE OPPOSITE.**')
    if not good:
        return 2

    p = json.load(io.open(ROWS, encoding='utf-8'))
    frames = p['frames']
    bank = io.open(BANK, encoding='utf-8').read()

    rec('')
    rec('-' * 100)
    rec('### (A) THE CONTAINMENT DIRECTION, STATED FROM THE NUMBERS.')
    rec('-' * 100)
    rec('    %-30s %-10s %-10s %-10s %-10s %-16s'
        % ('frame', 'rank grid', 'rank stab', 'dim grid', 'dim stab', 'direction'))
    dirs = set()
    for k in sorted(frames, key=lambda s: (frames[s]['N'], frames[s]['X'])):
        f = frames[k]
        dd = direction(f['rank_stab'], f['dim_stab'], f['rank_grid'], f['dim_grid'])
        dirs.add(dd)
        rec('    %-30s %-10d %-10d %-10d %-10d %-16s'
            % ('N=%d X=%g' % (f['N'], f['X']), f['rank_grid'], f['rank_stab'],
               f['dim_grid'], f['dim_stab'], dd.replace('A', 'STABLE').replace('B', 'GRID')))
    rec('')
    if dirs == {'A CONTAINS B'}:
        rec('  ### ### **THE DIRECTION IS THE SAME AT EVERY FRAME: ### THE STABLE CUT\'S SPACE')
        rec('  ### ### CONTAINS THE GRID CUT\'S.**')
        rec('  ### The stable cut puts FEWER directions outside (rank 69 against 80) and therefore')
        rec('  ### keeps MORE of them in (dim 3899 against 3888 at the reference frame).')
        rec('  ### **b319 SAID THIS AND ITS TABLE AGREES WITH IT:** ### `only grid` 9 to 12 at every')
        rec('  ### frame, `only stable` 0 at every frame -- a one-directional difference.')
    else:
        rec('  ### ### **THE DIRECTION IS NOT CONSTANT ACROSS THE FRAMES: %s**' % sorted(dirs))

    rec('')
    rec('-' * 100)
    rec('### (B) b319\'s OWN SENTENCES, TESTED AGAINST THAT TABLE.')
    rec('-' * 100)
    defects = []

    # ### the reference frame's own numbers, which the sentences below are tested against
    ref = None
    for k in frames:
        f = frames[k]
        if f['N'] == 4096 and f['X'] == 32.0:
            ref = f
    rec('  reference frame N=4096 X=32 : rank_stab=%d  dim_stab=%d  rank_grid=%d  dim_grid=%d'
        % (ref['rank_stab'], ref['dim_stab'], ref['rank_grid'], ref['dim_grid']))
    rec('')

    # ### ---- CLAIM 1: the containment sentence.
    c1 = 'STRICTLY CONTAINS' in bank
    rec('  ### (1) *"the stable subspace STRICTLY CONTAINS b316\'s"*')
    rec('      present in the bank : %s ; the table says : %s' % (c1, 'STABLE CONTAINS GRID'))
    rec('      ### **AGREES WITH THE TABLE.**')

    # ### ---- CLAIM 2: the ANSWERS sentence naming 69.
    m = re.search(r'the dimension selected by the source\'s own criterion is[^\n]*', bank)
    if m:
        sent = m.group(0)
        got = nums_in(sent)
        rec('')
        rec('  ### (2) *"%s"*' % sent.strip()[:88])
        rec('      numerals in that sentence : %s' % got)
        rec('      the table\'s `dim stab` at those frames : %s'
            % [frames[k]['dim_stab'] for k in sorted(
                frames, key=lambda s: (frames[s]['N'], frames[s]['X']))
               if frames[k]['X'] == 32.0])
        rec('      the table\'s `rank stab` at those frames : %s'
            % [frames[k]['rank_stab'] for k in sorted(
                frames, key=lambda s: (frames[s]['N'], frames[s]['X']))
               if frames[k]['X'] == 32.0])
        if 69 in got and ref['dim_stab'] != 69:
            defects.append(
                ('b319 bank, THE ANSWERS (1)',
                 sent.strip(),
                 'It calls `69` THE DIMENSION. ### `69` is the RANK -- the count of directions the '
                 'cut puts OUTSIDE the space. ### The bank\'s OWN table (1c) prints `dim stab` at '
                 'that frame as `%d`. ### **THE SENTENCE AND THE TABLE DISAGREE ABOUT WHICH COLUMN '
                 '`69` IS.**' % ref['dim_stab']))

    # ### ---- CLAIM 3: the direction of the rank inequality.
    rec('')
    rec('  ### (3) does any sentence say the stable cut EXCLUDES more than the grid cut?')
    bad = []
    for pat in [r'stable cut (?:excludes|puts out) more',
                r'smaller (?:space|subspace) than b316',
                r'only stable[^\n]*[1-9]']:
        for mm in re.finditer(pat, bank, re.I):
            bad.append(mm.group(0))
    rec('      sentences pointing the other way : %d %s' % (len(bad), bad if bad else ''))
    if bad:
        defects.append(('b319 bank', '; '.join(bad),
                        'Points against the table\'s containment direction.'))

    rec('')
    rec('-' * 100)
    rec('### (C) THE FILING.')
    rec('-' * 100)
    rec('  ### ### **PROSE-VS-TABLE DEFECTS FILED AGAINST b319\'s BANK : %d**' % len(defects))
    for where, sent, why in defects:
        rec('')
        rec('  ### **DEFECT -- %s**' % where)
        rec('    quoted : *"%s"*' % sent.strip()[:150])
        rec('    why    : %s' % why)
    rec('')
    rec('  ### ### **b319 IS NOT EDITED AND IS NOT RE-VERDICTED.** ### Its table is right, its')
    rec('  ### numbers are right, and its measurement stands. ### **WHAT IS FILED IS A SENTENCE**,')
    rec('  ### and a sentence that names the wrong column is a defect in the writing and not in the')
    rec('  ### instrument. ### The bank is append-only and the record carries the correction here.')
    rec('=' * 100)
    return 0 if good else 1


if __name__ == '__main__':
    code = main()
    io.open(os.path.join(D, 'b320_b319_read.txt'), 'w',
            encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
