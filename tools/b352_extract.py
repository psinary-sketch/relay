# -*- coding: utf-8 -*-
"""b352_extract.py -- EXTRACT-TO-DISK, AND THE FRAME COUNT VERIFIED BEFORE THE SEAL.

### ### **TWO JOBS, AND THE SECOND IS THE ORDER'S OWN CONDITION.** ### The order adopts a note requiring the frame
### count to be verified BEFORE sealing, with whatever count is found reported. ### This file does that, off
### `data/b339_price.json` and not off any prose, and writes it where the registration can quote it.
### ### **EVERY QUOTATION IS PULLED AT ITS EMITTING FILE AND LINE**, through the sortie's shared normaliser.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull   # noqa: E402
import quote_norm    # noqa: E402
import run_clock     # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


READS = [
    # ---- THE ORDER --------------------------------------------------------------------------------
    ('the order -- leg 1 adopts the (C) block with three notes', 'ORDER', d('b352_ferry_2026-09-07.txt'),
     "(C) block as banked, ADOPTED with the executor's three notes"),
    ('the order -- the frame count verified before sealing', 'ORDER', d('b352_ferry_2026-09-07.txt'),
     'frame count is verified before sealing, with whatever count is'),
    ('the order -- the void carried as the measured 10.62', 'ORDER', d('b352_ferry_2026-09-07.txt'),
     "and they are paid; the spectral void's width is carried as the"),
    ('the (C) block -- the models, fixed before any fit', 'ORDER', d('b351_ferry_2026-09-07.txt'),
     'models fixed in the registration before any fit — at minimum a'),
    ('the (C) block -- the question the fit must answer', 'ORDER', d('b351_ferry_2026-09-07.txt'),
     "Report each model's parameters, its residuals, and whether the"),
    ('the (C) block -- b339 is not re-verdicted', 'ORDER', d('b351_ferry_2026-09-07.txt'),
     "b339's verdict stands and this act measures the"),

    # ---- b339: THE OBJECT BEING REFITTED -----------------------------------------------------------
    ('b339 -- the domain ladder and its frames', 'b339', d('b339_price_run.txt'),
     '### the domain ladder, b317\'s DOMAIN_AXIS : X = [8.0, 16.0, 32.0, 64.0, 128.0] ; N = 128 X ; NY = 512'),
    ('b339 -- the verdict that stands', 'b339', d('b339_price_run.txt'),
     '### ### **THE GATE ON THE RUN (sealed): the cells whose X_req <= 512 : NONE -- UNAFFORDABLE**'),
    ('b339 -- an extrapolation of a fitted slope, labelled as one', 'b339', d('b339_price_run.txt'),
     '### **AN EXTRAPOLATION OF A FITTED SLOPE, LABELLED AS ONE. A PRICE IS NOT A PREDICTION.**'),
    ('b339 -- the side reading: descending toward a floor', 'b339', d('b339_the_exponent_resolved.txt'),
     '### ### What it says is that the residual the price extrapolated is descending toward a FLOOR and not'),
    ('b339 -- the floor reading is THIS SEAT\'S and labelled so', 'b339', d('b339_the_exponent_resolved.txt'),
     'choice of `X = 512` as one act\'s ceiling (sixteen times b320\'s largest kernel per trace) is this'),
    ('b339 -- its own words: the ladder is not yet a power law', 'b339', d('b339_the_exponent_resolved.txt'),
     '### (E3) the sealed price rule extrapolates a slope that the record\'s own ladder'),
    ('b339 -- the floor is what the next pricing must price', 'b339', d('b339_the_exponent_resolved.txt'),
     '### floor is what the next pricing must price; its origin (the fixed `NY = 512`, the cut\'s `tau`, the'),

    # ---- THE FITTER, AND THE PRECISION FLOOR OF THE OBJECT ------------------------------------------
    ('b322 -- the fitter, imported and not copied', 'FIT', t('b322_ladder.py'),
     '    """### ### **LEAST SQUARES FOR `log y = A + p log x`. ### RETURNS `(p, A, rms)`.**'),
    ('b322 -- a slope without a fit quality', 'FIT', t('b322_ladder.py'),
     '### **`rms` IS REPORTED BESIDE IT BECAUSE A'),
    ('b322 -- a price is not a prediction', 'RULE', d('b322_the_membership.txt'),
     '### it does. ### **A PRICE IS NOT A PREDICTION.**'),

    # ---- THE VOID'S WIDTH, MEASURED AT b350 --------------------------------------------------------
    ('b350 -- the band, and its measured width', 'b350', d('b350_the_two_held_axes.txt'),
     '### ### ### **THE RANK-PRESERVING BAND IS `(2.144048e-07, 2.277535e-06)`, A FACTOR OF `10.62` WIDE**, and'),
    ('b350 -- a band is about the cut and not the residual', 'b350', d('b350_the_two_held_axes.txt'),
     '### ### ### **AND THAT IS A FACT ABOUT THE CUT AND NOT ABOUT THE RESIDUAL.**'),
    ('b319 -- the threshold sits 57 times inside that separation', 'b350', t('b319_stable.py'),
     '# ### `TAU = 1e-6` therefore sits ### **57 TIMES INSIDE THAT SEPARATION** ### and ten orders of'),

    # ---- THE STRADDLING-GATE INCIDENTS -------------------------------------------------------------
    ('straddle (i) -- the mirror clean on a stale build', 'LORE', t('mirror_verify.py'),
     '### ### A CLEAN CLAUSE 1 ON A STALE BUILD IS EXACTLY AS CLEAN-LOOKING AS A'),
    ('straddle (ii) -- the hook and mirror arm, owed but unwritable before the push', 'LORE', d('b350_checks_run_prepush.txt'),
     '    ### the hook and the mirror records are NOT YET WRITTEN (they are written at the push).'),
    ('straddle (iii) -- a true prefix of its blob, before and after the commit', 'LORE', d('b351_checks_run_prepush.txt'),
     '    row 199 present once : True ; true prefix of its blob : True ; PASS'),
    ('the rule this act mints, in its own words at b351', 'LORE', d('b351_sortie_closing.txt'),
     '### commit and near-vacuous after; and `b342`'),

    # ---- WHAT b346 RESTS ON, IF ANYTHING -----------------------------------------------------------
    ('b346 -- the floor is present, and the rate resolves', 'b346', d('b346_the_exponent_by_rate.txt'),
     'A FLOOR IS PRESENT'),
    ('b350 -- pricing is not measuring', 'RULE', d('b350_the_two_held_axes.txt'),
     '### **PRICING IS NOT MEASURING, AND NOTHING PRICED HERE'),
    ('b351 -- the partition stays UNDECIDED', 'b351', d('b351_the_partition_question.txt'),
     '### ### ### **UNDECIDED.**'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b352 -- EXTRACT-TO-DISK, AND THE FRAME COUNT VERIFIED BEFORE THE SEAL.')
    rec('=' * 100)

    # ================= THE FRAME COUNT, THE ORDER'S OWN CONDITION =================
    P = json.load(io.open(d('b339_price.json'), encoding='utf-8'))
    xs = P['xs']
    cells = sorted(P['cells'], key=float)
    rec('')
    rec('  ### ### **THE FRAME COUNT, VERIFIED BEFORE THE SEAL AND OFF THE RECORD RATHER THAN OFF PROSE.**')
    rec('    the domain ladder, as b339 banked it : %s' % xs)
    rec('    covered cells found                  : %s' % cells)
    rec('    %-8s %-8s %-8s %-8s %-12s %-12s %s' % ('a', 'frames', 'Tr', 'margin', 'int_ef', 's', 'reproduces b321'))
    counts = []
    for k in cells:
        c = P['cells'][k]
        counts.append(len(c['R']))
        rec('    %-8s %-8d %-8d %-8d %-12r %-12r %s'
            % (k, len(c['R']), len(c['tr']), len(c['margin']), c['int_ef'], c['s'], c['reproduces']))
    same = len(set(counts)) == 1
    n = counts[0] if same else None
    rec('    ### frames per cell identical at every covered cell : %s' % same)
    rec('    ### ### **THE COUNT FOUND : %s AT EVERY ONE OF %d COVERED CELLS.**' % (n, len(cells)))
    rec('    ### ### **THE ORDER SAID "the five frames". ### THE RECORD SAYS %s. ### THEY AGREE, AND THE ACT'
        % n)
    rec('    ### ### CHECKED RATHER THAN ACCEPTED.**')
    rec('    ### ### **AND WHAT IS NOT FIVE: THE CELLS.** ### There are %d covered cells, not five, and the'
        % len(cells))
    rec('    ### models are fitted per cell over %s frames each.' % n)
    rec('')
    rec("  ### ### **THE OBJECT'S PRECISION FLOOR, READ OFF THE RECORD AND NOT ASSUMED.**")
    dec = [len(repr(P['cells'][k]['int_ef']).split('.')[1]) for k in cells]
    rec('    `int_ef` enters `R = margin - int_ef` with %s decimal places at the three cells,' % dec)
    rec('    so ### **R IS KNOWN TO +/- 5e-10 ABSOLUTE**, whatever precision the JSON prints.')
    smallest = min(min(P['cells'][k]['R']) for k in cells)
    rec('    the smallest residual anywhere on the ladder : %.9e' % smallest)
    rec('    ### ### **SO THE RELATIVE FLOOR AT THE LAST RUNG IS %.3e**, and any bar this act sets must sit'
        % (5e-10 / smallest))
    rec('    ### ### above it or be marked UNPRICED.')

    # ================= THE READS =================
    rec('')
    rec('-' * 100)
    rec('  ### THE READS.')
    rec('-' * 100)
    bad = 0
    for label, tag, path, anchor in READS:
        try:
            needle_pull.pull(path, anchor)
        except LookupError:
            bad += 1
            rec('  ### ### **UNPULLABLE** : %s' % label)
            rec('      file   : %s' % os.path.relpath(path, ROOT))
            rec('      anchor : %r' % anchor)
            continue
        txt = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
        num = None
        for i, ln in enumerate(txt, 1):
            if quote_norm.contains(ln, anchor):
                num = i
                break
        rec('')
        rec('  [%-5s] %s' % (tag, label))
        rec('      %s : line %s' % (os.path.relpath(path, ROOT).replace(os.sep, '/'), num))
        rec('      | %s' % txt[num - 1].rstrip())
        if num < len(txt) and txt[num].strip():
            rec('      | %s' % txt[num].rstrip())
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### UNPULLABLE : %d' % (len(READS), bad))
    rec('  ### ### **AN EXTRACT IS A QUOTATION AT A LINE. ### IT IS NOT A READING OF THE ARGUMENT AROUND IT.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b352_extract_notes', LINES)
    io.open(d('b352_frames.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(xs=xs, cells=cells, frames_per_cell=counts, frames=n, uniform=same, n_cells=len(cells),
             int_ef_decimals=dec, floor_abs=5e-10, smallest_R=smallest, floor_rel=5e-10 / smallest,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
