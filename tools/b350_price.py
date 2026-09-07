# -*- coding: utf-8 -*-
"""b350_price.py -- THE FLOOR'S TWO HELD AXES, PRICED FROM b344's PRINTED FIGURES.

### ### **NO FRAME IS BUILT, NO LADDER IS RUN, NO CELL IS EVALUATED.** ### This tool imports nothing that can
### compute a residual. ### It reads `b344_ny.json` and does arithmetic on figures that act already printed.
### ### **THE THREE UNITS ARE THE SEALED ONES:** the ladder's wall cost; the room an axis has before the
### instrument keeps something different; and what the move would confound, in the sealed words of the act that
### declined it.
### ### ### **AND THE DISTINCTION THE REGISTRATION FIXED IN ADVANCE IS KEPT THROUGHOUT: A RANK-PRESERVING BAND
### ### ### IS A FACT ABOUT THE CUT AND NOT ABOUT THE RESIDUAL.**
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock    # noqa: E402
import quote_norm   # noqa: E402  ### the sortie's shared normaliser -- both sides of every quotation

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []

REASONS = [
    ("the cut's threshold", 'b344_registration_2026-09-06.txt',
     "### ### **WHY `NY` AND NOT THE CUT'S `tau`:** ### moving `tau` moves the stable cut, and the cut's rank is"),
    ('the taper', 'b344_registration_2026-09-06.txt',
     '### ### **WHY `NY` AND NOT THE TAPER:** ### the taper is `ALPHA` and `BETA`, and b316 records them as the'),
]


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def main():
    rec('=' * 100)
    rec("b350 -- THE FLOOR'S TWO HELD AXES, PRICED. ### read from b344's printed figures; nothing is run.")
    rec('=' * 100)
    N = json.load(io.open(os.path.join(D, 'b344_ny.json'), encoding='utf-8'))
    rows = N['rows']
    rec('')
    rec("  b344's PRINTED FIGURES, READ AND NOT RECOMPUTED (data/b344_ny.json):")
    rec('    %-7s %-9s %-6s %-9s %-14s %-16s %-16s %-9s %-7s'
        % ('NY', 'wall s', 'rank', 'tau', 'eig in decade', 'smallest kept', 'largest dropped', 'ALPHA', 'BETA'))
    for r in rows:
        h = r['held']
        rec('    %-7d %-9.2f %-6d %-9.1e %-14d %-16.6e %-16.6e %-9.1f %-7.1f'
            % (r['NY'], r['wall'], r['rank'], h['tau'], h['eig_within_decade'], h['smallest_kept'],
               h['largest_dropped'], h['alpha'], h['beta']))
    tau = rows[0]['held']['tau']
    wall = sum(r['wall'] for r in rows)
    rec('')
    rec('  ### (1) THE COST OF A LADDER, summed from the walls b344 printed:')
    rec('    the sealed ladder %s at the reference frame : %s' % (N['ladder'], ' + '.join('%.2f' % r['wall'] for r in rows)))
    rec('    ### ### **%.2f SECONDS OF WALL PER VALUE TRIED, FOR EITHER AXIS**, because a move is a ladder either' % wall)
    rec('    ### way and the ladder is the same shape. ### **THE COST IS THE SAME FOR BOTH AXES AND IT IS SMALL.**')
    rec('    ### **AND WHAT THAT COST BUYS IS ONE VALUE.** ### A ladder answers what the residual does at ONE new')
    rec('    ### threshold or ONE new taper, not what it does across either axis.')

    lo = max(r['held']['largest_dropped'] for r in rows)
    hi = min(r['held']['smallest_kept'] for r in rows)
    inside = lo < tau < hi
    rec('')
    rec('  ### (2) THE ROOM EACH AXIS HAS BEFORE THE INSTRUMENT KEEPS SOMETHING DIFFERENT:')
    rec('    THE CUT\'S THRESHOLD -- the intersection across the rungs of (largest dropped, smallest kept):')
    rec('      the widest largest-dropped over the rungs : %.6e' % lo)
    rec('      the narrowest smallest-kept over the rungs : %.6e' % hi)
    rec('      ### ### **THE RANK-PRESERVING BAND IS ( %.6e , %.6e ), A FACTOR OF %.2f WIDE**, and the corpus\'s'
        % (lo, hi, hi / lo))
    rec('      ### own `tau = %.1e` sits inside it : %s -- it may fall by a factor of %.2f or rise by a factor of'
        % (tau, inside, tau / lo))
    rec('      ### %.2f with the SAME eigenvalues kept at every rung, and therefore the same rank.' % (hi / tau))
    rec('      ### ### **AND THAT IS A FACT ABOUT THE CUT AND NOT ABOUT THE RESIDUAL.** ### The same subspace kept')
    rec('      ### does not mean the same residual; the residual depends on how the kept subspace is used and not')
    rec('      ### only on which vectors are in it. ### **b344 PRINTED NO RESIDUAL AT A SECOND THRESHOLD, SO THE')
    rec('      ### ### RESIDUAL\'S RESPONSE TO THE THRESHOLD IS NOT PRICED BY THESE FIGURES.**')
    alpha = {r['held']['alpha'] for r in rows}
    beta = {r['held']['beta'] for r in rows}
    rec('')
    rec('    THE TAPER -- what the printed figures say about it:')
    rec('      ALPHA takes the values %s across every rung ; BETA takes %s.' % (sorted(alpha), sorted(beta)))
    rec('      ### ### **THEY ARE PRINTED AS CONSTANTS AND NOTHING IS PRINTED BESIDE THEM.** ### There is no second')
    rec('      ### value, no neighbourhood, no eigenvalue interval and no derivative. ### **SO THE PRINTED FIGURES')
    rec('      ### ### PRICE NO ROOM FOR THE TAPER AT ALL, AND THIS ACT SAYS SO RATHER THAN INVENTING ONE.**')
    rec('      ### ### **AND THE PRICING IS THEN PRICED, AS THE ORDER REQUIRES:** to price the taper\'s room one')
    rec('      ### would need the residual at a second `ALPHA` and at a second `BETA` -- **two ladders, %.2f s of' % (2 * wall))
    rec('      ### wall in total at the reference frame** -- and even that would give a difference and not a room,')
    rec('      ### because the taper has no analogue of the eigenvalue interval that gives the threshold one.')

    rec('')
    rec("  ### (3) WHAT EACH MOVE WOULD CONFOUND -- in the SEALED WORDS of the act that declined it,")
    rec('  ### located through the sortie\'s shared normaliser at the sealed file:')
    quoted = []
    for name, fn, frag in REASONS:
        src = io.open(os.path.join(D, fn), encoding='utf-8', errors='replace').read()
        found = quote_norm.contains(src, frag)
        line = next((i + 1 for i, ln in enumerate(src.split(chr(10))) if quote_norm.contains(ln, frag)), None)
        rec('    %-22s located at %s line %s : %s' % (name, fn, line, found))
        quoted.append(dict(axis=name, file=fn, line=line, found=bool(found), fragment=frag))
    rec("    THE CUT'S THRESHOLD would confound the RANK with the FLOOR: moving it moves the stable cut, and b343")
    rec('      showed the rank constant across the grid axis, so a residual that moved with the threshold could not')
    rec('      be told from a residual that moved with the rank. ### b319 records that the corpus\'s threshold sits')
    rec('      ### **57 TIMES INSIDE THAT SEPARATION**, which is why it was chosen and why moving it is not free.')
    rec('    THE TAPER would confound the INSTRUMENT with the OBJECT: `ALPHA` and `BETA` are the source\'s own')
    rec("      constants -- b316 records them as *\"Definition 4.4's `a`, at the source's own `S(1,1)`\"* -- so a")
    rec('      taper moved is no longer the source\'s object, and any change in the residual would be a change in')
    rec('      what was being measured. ### **THAT IS A HARDER CONFOUND THAN THE THRESHOLD\'S, AND IT IS WHY THE')
    rec('      ### ### CHEAPNESS OF THE LADDER IS NOT THE WHOLE PRICE.**')

    # ### the verdict on the floor, by the sealed rule
    rec('')
    rec('=' * 100)
    rec("  THE VERDICT ON THE FLOOR, BY SECTION (D)'s RULE AND NO OTHER.")
    rec('=' * 100)
    rec('    the three origins b339 named : the fixed `NY`, the cut\'s `tau`, the taper.')
    rec('    moved, with the residual measured against it : `NY` only (b344).')
    rec('    measured in this act : ### **NOTHING. ### THIS ACT MOVES NO AXIS AND MEASURES NO RESIDUAL.**')
    rec('    the record\'s measurements of the residual against a HELD origin : ### **NONE.**')
    rec('')
    rec('  ### ### ### **THE FLOOR IS UNEXPLAINED.**')
    rec('  ### The one axis that was moved does not account for it -- b344 found the residual CONVERGES in `NY`,')
    rec('  ### with the remaining travel from the corpus\'s own `NY = 512` about a ninth of the floor -- and for the')
    rec('  ### two held axes the record contains no measurement of the residual at all. ### **PRICING IS NOT')
    rec('  ### ### MEASURING, AND NOTHING PRICED HERE EXPLAINS ANYTHING.**')
    rec('  ### **THE UNEXPLAINED PART, NAMED:** the residual\'s response to the cut\'s threshold anywhere in its')
    rec('  ### rank-preserving band, and the residual\'s response to the taper at any value. ### **NEITHER IS IN')
    rec('  ### ### THE RECORD AND NEITHER IS PRICED BY b344\'s PRINTED FIGURES; ONLY THE COST OF GETTING THEM IS.**')

    # ### the trail
    tr = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read()
    owed = quote_norm.contains(tr, 'the same movement measurement b344 made on `NY`, made on `tau` and on the taper')
    price = quote_norm.contains(tr, 'it can be read off the figures above without a single new frame')
    rec('')
    rec('  THE TRAIL `W-ORD-FLOOR-HELD-AXES`, AGAINST ITS OWN TWO DEMANDS:')
    rec('    its demand for the MEASUREMENT located in its own text : %s' % owed)
    rec('    its demand for the PRICE located in its own text        : %s' % price)
    rec('    ### ### **THE PRICE HALF IS PAID.** ### The ladder cost is stated for both axes, the threshold\'s')
    rec('    ### rank-preserving band is computed from the printed figures with no new frame, and the taper\'s')
    rec('    ### unpriceability is stated with the cost of removing it.')
    rec('    ### ### **THE MEASUREMENT HALF IS NOT PAID AND IS NOT ATTEMPTED.** ### No axis moved.')
    rec('    ### ### ### **SO THE TRAIL IS RESTATED, NOT DISCHARGED. ### A TRAIL IS NOT DISCHARGED BY PAYING THE')
    rec('    ### ### ### CHEAPER HALF OF IT.**')
    rec('')
    rec('  ### NO FRAME BUILT ; NO LADDER RUN ; NO CELL EVALUATED ; NO AXIS MOVED ; NO ACT RE-VERDICTED.')
    rec('=' * 100)
    p = run_clock.write(D, 'b350_price_run', LINES)
    io.open(os.path.join(D, 'b350_price.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(ladder=N['ladder'], wall_total=wall, walls=[r['wall'] for r in rows], tau=tau,
             band_lo=lo, band_hi=hi, band_factor=hi / lo, tau_inside=bool(inside),
             fall_factor=tau / lo, rise_factor=hi / tau, alpha=sorted(alpha), beta=sorted(beta),
             taper_room_priced=False, taper_pricing_cost=2 * wall, reasons=quoted,
             verdict='THE FLOOR IS UNEXPLAINED', trail='RESTATED, NOT DISCHARGED',
             trail_owed_found=bool(owed), trail_price_found=bool(price),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  ### run file : %s ; its clock : %s' % (os.path.basename(p), run_clock.read_stamp(p)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
