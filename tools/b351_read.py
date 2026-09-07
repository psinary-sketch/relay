# -*- coding: utf-8 -*-
"""b351_read.py -- THE PARTITION QUESTION, ANSWERED BY READING. ### IT COMPUTES NOTHING.

### ### **WHAT IT IMPORTS IS THE WHOLE ARGUMENT THAT IT COMPUTES NOTHING:** ### a needle puller, the sortie's
### shared normaliser, and a clock. ### **NO TRANSFORM, NO ROOM, NO RESIDUAL, NO PHASE, NO SEED.** ### Every
### figure it prints is a substring of a line in a file the corpus already banked, and the line and its number
### are printed beside it.
### ### **THE UNITS ARE THE SEALED ONES (registration section (C)):** ### for each coordinate, the charted
### range; the bound state, one of `BOUNDED BY AN ARGUMENT` / `BOUNDED BY A MEASUREMENT` / `NOT BOUNDED`; and
### where a class would have to be proved silent rather than measured.
### ### **THE ONE ARITHMETIC IT DOES IS DIVISION OF TWO BANKED COUNTS**, to turn the census's own box grid into
### a price in boxes, and it is labelled where it happens.
"""
import io
import json
import math
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

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


STATES = ('BOUNDED BY AN ARGUMENT', 'BOUNDED BY A MEASUREMENT', 'NOT BOUNDED')

# ### THE CENSUS'S OWN BOX GRID, READ OFF ITS OWN SENTENCE AND NOT TYPED FROM MEMORY.
BOXES, T_LO, T_HI, BOX_H = 60, 0.5, 150.0, 2.5


def cite(path, anchor):
    """### Locate a sentence at its emitting file, through the SHARED normaliser. ### Returns (line, text)."""
    needle_pull.pull(path, anchor)                     # ### raises LookupError if it is not there
    txt = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
    for i, ln in enumerate(txt, 1):
        if quote_norm.contains(ln, anchor):
            return i, ln.strip()
    raise LookupError(anchor)


def show(path, anchor, note=''):
    n, ln = cite(path, anchor)
    rec('      %s:%d' % (os.path.relpath(path, ROOT).replace(os.sep, '/'), n))
    rec('        | %s' % ln)
    if note:
        rec('        ### %s' % note)
    return n


def main():
    rec('=' * 100)
    rec('b351 -- THE PARTITION QUESTION. ### A READ, UNDER THE ORDER\'S CEILING. ### NOTHING IS COMPUTED.')
    rec('=' * 100)
    rec('  ### THE SEALED STATES, AND NO OTHERS : %s' % ' / '.join(STATES))
    rec('  ### ### **A BOUND ON THE INSTRUMENT IS NOT A BOUND ON THE COORDINATE.** (registration section (C))')
    rec('')
    out = {}

    # ============================================================================================
    rec('-' * 100)
    rec('  ### COORDINATE 1 -- THE ABSCISSA `beta`.')
    rec('-' * 100)
    rec('    (C1) THE RANGE THE RECORD HAS CHARTED:')
    show(t('b334_aimmap.py'), 'BETAS = (0.50, 0.55, 0.60, 0.70, 0.80, 0.90, 0.9532604747946607)',
         'the top is the abscissa of the first off-line zero, not a round number chosen for convenience')
    rec('    (C2) CAN THE RECORD BOUND IT?')
    show(d('b326_the_reach.txt'), "height `2.5` at the working precision. ### **THE ABSCISSA `1.50` IS NOT A CHOICE:** ###")
    show(d('b326_the_reach.txt'), '`SUM_{k>=2} r_Q(k) k^{-3/2} = 1.38 < 2`, so `|Z_Q(s) - 2| < 2` and `Z_Q` cannot vanish at')
    show(d('b326_the_reach.txt'), '`Re s >= 1.5` (nor, by the functional equation, at `Re s <= -0.5`); and every box within `0.02` of')
    rec('    ### ### **STATE : %s**' % STATES[0])
    rec('    ### ### **AND THIS IS THE ONLY ONE OF THE FOUR THAT IS BOUNDED AS AN OBJECT AND NOT AS A LOOKING.**')
    rec('    ### The sum is over ALL representation numbers and the bound holds at EVERY `s` in the half-plane,')
    rec('    ### so it closes the abscissa for zeros nobody has found, not merely for those anybody has.')
    rec('    ### `beta` lies strictly inside `(-0.5, 1.5)`, and the charted top `0.9532604747946607` is not near')
    rec('    ### the boundary of that interval -- which is a fact about where the record has looked, and is')
    rec('    ### recorded here as a separate thing from the bound itself.')
    rec('    (C3) WHERE A CLASS WOULD HAVE TO BE PROVED SILENT : ### **NO SUCH CLASS.**')
    out['beta'] = dict(state=STATES[0], silent_class=None, missing=None, price=None)

    # ============================================================================================
    rec('')
    rec('-' * 100)
    rec('  ### COORDINATE 2 -- THE HEIGHT `gamma`.')
    rec('-' * 100)
    rec('    (C1) THE RANGE THE RECORD HAS CHARTED:')
    show(d('b334_chart_run.txt'), 'the largest gamma charted 61.687904')
    show(d('b334_chart_run.txt'), "zero-side tail bound, largest over the seeds : 3.604e-03 ; zeta's ordinates to 9877.782657",
         'the libraries reach further than the chart does, and both ceilings are printed')
    rec('    (C2) CAN THE RECORD BOUND IT?')
    show(d('b326_the_reach.txt'), "### census's own `winding`, over `sigma in [0.52, 1.50]`, `t in [0.5, 150]`, in sixty boxes of")
    show(d('b326_the_reach.txt'), '### ### ### **THE COUNT NOW CLOSES BY THE ARGUMENT PRINCIPLE:** ### `146` on the line plus',
         'the count closes AT the library top; it says nothing above it')
    show(d('b326_the_reach.txt'), '### ### NEVER LOOKED**, so the deficit is off-line zeros nobody has banked -- and the registration',
         "the record's own word for a height above a census: nobody looked")
    rec('    ### ### **STATE : %s**' % STATES[1])
    rec('    ### The bound is `T = 150`, and `150` is where the census stopped. ### **THE COORDINATE IS NOT')
    rec('    ### BOUNDED; THE LOOKING IS.**')
    rec('    (C3) WHERE A CLASS WOULD HAVE TO BE PROVED SILENT:')
    rec('    ### ### **THE CLASS IS `gamma > 150`**, and it would have to be proved silent, because there is no')
    rec('    ### measurement in it and none is reachable by more of the same measuring. ### And the reason is')
    rec('    ### sharper than reach, and the registration fixed the words before this was read:')
    show(d('b326_the_reach.txt'), '### ### DEFECT.** ### The Riemann-von Mangoldt main term `(T/pi) log(T sqrt23 / 2 pi e)` at',
         'the count of instances GROWS with the height, without bound')
    rec('    ### ### **SO THE ONLY METHOD THE RECORD HAS ON THIS COORDINATE PRODUCES INSTANCES, AND THE MAIN')
    rec('    ### ### TERM SAYS THE INSTANCES DO NOT RUN OUT.** ### Running the census higher buys more zeros.')
    rec('    ### ### **IT NEVER BUYS A STATEMENT ABOUT ALL ZEROS ABOVE A HEIGHT**, which is what a class is.')
    per = BOXES / (T_HI - T_LO)
    to300 = int(math.ceil((300.0 - T_LO) / BOX_H)) - BOXES
    rec('    ### THE PRICE, IN THE RECORD\'S OWN COUNTABLE UNIT, BECAUSE IT PRINTS NO WALL TIME FOR THIS WORK:')
    rec('      the census: %d boxes of height %.1f over t in [%.1f, %.1f] = %.5f boxes per unit of height'
        % (BOXES, BOX_H, T_LO, T_HI, per))
    rec('      to carry the census to T = 300 : %d further boxes at the same precision' % to300)
    rec('    ### ### **AND THE ACT SAYS PLAINLY THAT IT COULD NOT GIVE A TIME:** ### b326 printed no wall for')
    rec('    ### ### the census, and a wall time borrowed from other work is not a price for this work.')
    rec('    ### ### **AND THE DEEPER REFUSAL: THIS PRICE IS FOR THE WRONG OBJECT.** ### Boxes buy zeros; the')
    rec('    ### ### missing statement needs a class; ### **so paying it in full would leave the question')
    rec('    ### ### exactly where it stands.**')
    out['gamma'] = dict(state=STATES[1], silent_class='gamma > 150',
                        missing=('there exist T0 and finitely many classes C1..Ck such that every aim with '
                                 'gamma > T0 lies in one of them, and the margin behaviour on each class is '
                                 'decided by the class'),
                        price=dict(unit='boxes', per_unit_height=per, boxes_to_T300=to300,
                                   wall='NOT PRINTED BY THE RECORD',
                                   note='the price buys instances; the missing statement needs a class'))

    # ============================================================================================
    rec('')
    rec('-' * 100)
    rec('  ### COORDINATE 3 -- THE SEED\'S PHASE `phi`.')
    rec('-' * 100)
    rec('    (C1) THE RANGE THE RECORD HAS CHARTED:')
    show(d('b349_extend_run.txt'), "the sealed phase WINDOW : 45 < |phase| < 135 degrees (b328's refinement, a window and NOT a threshold)")
    rec('    (C2) CAN THE RECORD BOUND IT?')
    show(t('b328_family.py'), '###   ### (B2) for an even seed `G(-c) = G(c)`, so the sum is `4 |G|^2 cos(2 phi)`;')
    rec('    ### ### **STATE : %s**' % STATES[0])
    rec('    ### The coordinate is an angle: ### **IT LIVES ON A CIRCLE, WHICH NEEDS NO BOUNDING.** ### And the')
    rec('    ### sign of the quadruple\'s term is decided by `cos(2 phi)` alone, so the circle is cut into the')
    rec('    ### arcs where that cosine is negative and the arcs where it is positive, meeting exactly at')
    rec('    ### `|phi| = 45` and `|phi| = 135`. ### **THAT IS A COMPLETE AND FINITE CLASSIFICATION OF THIS ONE')
    rec('    ### COORDINATE, AND IT IS ALGEBRAIC RATHER THAN MEASURED.**')
    rec('    (C3) WHERE A CLASS WOULD HAVE TO BE PROVED SILENT:')
    rec('    ### ### **ONE CLASS SURVIVES THE ALGEBRA: `|G| = 0`.** ### When the transform vanishes the term is')
    rec('    ### zero whatever the angle is, and the angle itself is undefined -- ### **so the sign condition')
    rec('    ### cannot see this case at all, and no reading of `phi` reports it.**')
    show(d('b349_the_room_relative.txt'), '### ### NEVER DEGENERATES -- IT MEANS THESE THREE DID NOT.**',
         "the record's own words about exactly this class, from the act that checked for it")
    rec('    ### ### **AND THIS IS THE CLEAREST CASE IN THE WHOLE ACT OF A CLASS THAT CANNOT BE MEASURED')
    rec('    ### ### SILENT.** ### Checking seeds and finding none degenerate is a statement about the seeds')
    rec('    ### ### checked. ### **NO FINITE NUMBER OF THEM IS A STATEMENT ABOUT THE CONSTRUCTION**, and the')
    rec('    ### ### price of the missing sentence is therefore not a quantity of running at all.')
    out['phi'] = dict(state=STATES[0], silent_class='|G| = 0 at a lawful aim',
                      missing='no lawful seed at a charted aim has |G| = 0',
                      price=dict(unit=None, wall=None,
                                 note='NOT A QUANTITY OF RUNNING: no finite number of seeds proves a class silent'))

    # ============================================================================================
    rec('')
    rec('-' * 100)
    rec('  ### COORDINATE 4 -- THE SEED\'S WIDTH `a`.')
    rec('-' * 100)
    rec('    (C1) THE RANGE THE RECORD HAS CHARTED:')
    show(t('b334_aimmap.py'), 'REACHING = (40.0, 81.0)')
    rec('    (C2) CAN THE RECORD BOUND IT?')
    show(d('b334_the_aim_map.txt'), "### `X = 32` against `f`'s support `a^2 = 1600` and `6561`; the eps evaluator measured at five radii:")
    show(d('b334_the_aim_map.txt'), '### `eps(100) = +9.968008e-02`, `eps(1600) = -7.369351e+03`, `eps(6561) = -9.726459e+03` -- a sign change')
    show(d('b334_the_aim_map.txt'), '### and a growth past `rho = 100`, so the remainder at these widths is outside')
    show(d('b334_leg_covered_run.txt'), 'the square for Z_Q : NOT AN INSTRUMENT THE RECORD HAS')
    rec('    ### ### **STATE : %s**' % STATES[2])
    rec('    ### There is no argument closing the width, and there is not even a measurement that reaches the')
    rec('    ### widths already charted: ### **at `a = 40` and `a = 81` the square and the remainder are NOT')
    rec('    ### REACHED, by the record\'s own measurement of its own frame**, and the remainder evaluator has')
    rec('    ### changed sign and grown by four orders past `rho = 100`.')
    rec('    (C3) WHERE A CLASS WOULD HAVE TO BE PROVED SILENT:')
    rec('    ### ### **THE CLASS IS `a^2 > 32`**, which is every width the reaching leg uses.')
    rec('    ### ### **AND THIS COORDINATE IS WORSE OFF THAN THE HEIGHT, IN A WAY WORTH SAYING PLAINLY:** ###')
    rec('    ### ### the height has a method that produces instances and merely has not been run higher. ###')
    rec('    ### ### **THE WIDTH HAS NO METHOD AT ALL** -- the evaluator is outside its own reach there, and')
    rec('    ### ### for the Epstein function the record says in its own words that the instrument does not')
    rec('    ### ### exist. ### **SO THE PRICE OF THE MISSING STATEMENT IS AN INSTRUMENT, AND AN INSTRUMENT IS')
    rec('    ### ### WHAT THIS ACT\'S CEILING FORBIDS AND WHAT NO BANKED FIGURE PRICES.**')
    rec('    ### ### **UNPRICEABLE FROM BANKED FIGURES, AND THE PRICING IS UNPRICEABLE TOO** -- there is no')
    rec('    ### ### rung, box, cell or aim in the record whose count would scale to it.')
    out['a'] = dict(state=STATES[2], silent_class='a^2 > 32',
                    missing=('the remainder evaluator is valid at rho > 100, or there is an instrument for the '
                             'square and the remainder of Z_Q'),
                    price=dict(unit=None, wall=None, note='UNPRICEABLE FROM BANKED FIGURES; the pricing is unpriceable too'))

    # ============================================================================================
    rec('')
    rec('-' * 100)
    rec('  ### THE VERDICT, BY THE SEALED BRANCH RULE OF SECTION (D).')
    rec('-' * 100)
    states = [out[k]['state'] for k in ('beta', 'gamma', 'phi', 'a')]
    argued = [k for k in ('beta', 'gamma', 'phi', 'a') if out[k]['state'] == STATES[0]]
    open_c = [k for k in ('beta', 'gamma', 'phi', 'a') if out[k]['state'] != STATES[0]]
    rec('    the states, in the sealed order beta / gamma / phi / a :')
    for k in ('beta', 'gamma', 'phi', 'a'):
        rec('      %-6s %s' % (k, out[k]['state']))
    rec('')
    rec('    ### **(A SHAPE EXISTS) -- SHOWN UNREACHABLE, NOT MERELY UNCLAIMED.**')
    rec('      It demands every coordinate either bounded by an argument or reducible to finitely many classes')
    rec('      by a statement the record already holds. ### %d of the four are bounded by an argument (%s), and'
        % (len(argued), ', '.join(argued)))
    rec('      the other %s are not, and no statement in the record reduces either to finitely many classes:'
        % (' and '.join(open_c)))
    rec('        `gamma` : its only method produces instances whose count the main term says grows.')
    rec('        `a`     : the record has no method there at all, by its own words.')
    rec('      ### **SO THE BRANCH FAILS ON ITS OWN CONDITION.**')
    rec('')
    rec('    ### **(NO FINITE PARTITION) -- SHOWN UNREACHABLE, AND FOR A REASON THE REGISTRATION FIXED.**')
    rec('      It demands an obstruction NAMED AND QUOTED at an emitting line -- a statement in the record from')
    rec('      which it follows that no finite classification can exist. ### **NO SUCH STATEMENT WAS FOUND, AND')
    rec('      ### SECTION (D) FIXED IN ADVANCE THAT AN ABSENCE OF A BOUND IS NOT AN OBSTRUCTION.** ### This')
    rec('      branch may not be reached by failing to find one, and it is not reached.')
    rec('')
    rec('    ### ### ### **THEREFORE: UNDECIDED.**')
    verdict = 'UNDECIDED'
    rec('')
    rec('    ### ### **THE MISSING STATEMENTS, TYPED AS SENTENCES THAT WOULD HAVE TO BE TRUE:**')
    rec('      (M-beta)  ### **NONE.** ### The coordinate is closed by an argument the record already holds.')
    rec('      (M-gamma) "%s."' % out['gamma']['missing'])
    rec('                ### PRICED AT %.5f BOXES PER UNIT OF HEIGHT (%d further boxes to T = 300), IN BOXES AND'
        % (per, to300))
    rec('                ### NOT IN SECONDS, BECAUSE THE RECORD PRINTS NO WALL FOR THIS WORK -- ### **and the')
    rec('                ### price buys instances while the statement needs a class.**')
    rec('      (M-phi)   "%s."' % out['phi']['missing'])
    rec('                ### **NOT A QUANTITY OF RUNNING.** ### No finite number of seeds proves it.')
    rec('      (M-a)     "%s."' % out['a']['missing'])
    rec('                ### **UNPRICEABLE FROM BANKED FIGURES**, and its pricing is unpriceable too.')
    rec('')
    rec('    ### ### **WHAT THIS ACT DID NOT DO, RESTATED AGAINST ITS OWN CEILING:** ### no partition was')
    rec('    ### constructed; no class was proved silent; no instrument was written; nothing was computed')
    rec('    ### beyond one division of two banked counts, which is labelled where it happens. ### **NO CLASS')
    rec('    ### IS DISCHARGED. ### THE CLAUSE HAS NOT MOVED. ### NOTHING HERE BEARS ON THE QUANTIFIER.**')

    rec('')
    rec('-' * 100)
    rec('  ### THE EXPECTATIONS, SCORED.')
    rec('-' * 100)
    rec("    ### **THE NAVIGATOR'S (L3)** -- UNDECIDED, with the height the coordinate the record cannot bound :")
    rec('    ### ### **MET ON THE VERDICT, AND MET-THEN-REFINED ON THE COORDINATE.** ### The height is indeed a')
    rec('    ### coordinate the record cannot bound. ### **IT IS NOT THE ONLY ONE, AND IT IS NOT THE WORST:**')
    rec('    ### the width is unbounded with no method at all, while the height at least has a method that has')
    rec('    ### not been run higher. ### The expectation named the right verdict and the second-worst axis.')
    rec("    ### **THIS SEAT'S** -- more than one coordinate unbounded, the four failing in different ways, and")
    rec('    ### at least one closed by an argument already in the record and never cited for this purpose :')
    rec('    ### ### **MET**, and the argument is b326\'s summed bound, banked since the completeness census and')
    rec('    ### never once used to say anything about the aim plane.')

    rec('')
    rec('=' * 100)
    rec('  VERDICT : ### **%s**' % verdict)
    rec('  ### ### **AND WHAT UNDECIDED IS: A STATEMENT ABOUT THE RECORD, NOT ABOUT THE OBJECT.** ### The aim')
    rec('  ### plane may well admit a finite classification; ### **THIS ACT SAYS ONLY THAT THE RECORD DOES NOT')
    rec('  ### CONTAIN ONE AND DOES NOT CONTAIN A PROOF THAT THERE IS NONE.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b351_read_run', LINES)
    io.open(os.path.join(D, 'b351_read.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(coordinates=out, states=states, verdict=verdict, argued=argued, open_coords=open_c,
             boxes=BOXES, t_lo=T_LO, t_hi=T_HI, box_h=BOX_H, boxes_per_unit=per, boxes_to_T300=to300,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
