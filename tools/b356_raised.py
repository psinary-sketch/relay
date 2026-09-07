# -*- coding: utf-8 -*-
"""b356_raised.py -- THE SIXTH RUNG WITH THE QUADRATURE AXIS RAISED. ### ONE PARAMETER MOVED, DELIBERATELY.

### ### **THE INSTRUMENT IS IMPORTED AND ONE PARAMETER IS RE-TUNED:** ### `NY` from `512` to `1024`, and
### **NOTHING ELSE.** ### `b316_instrument.Frame`, `b319_stable.both_subspaces`, `b317_smear.identity_trace`,
### `b318_square.square_trace` -- the same calls `b320_run.py` and `b354_sixth.py` make.
### ### **THE CONTROL RUNS FIRST AND IT TESTS THE RAISE, NOT THE OBJECT:** ### the FIFTH rung under the
### raised axis, where `b354` measured the rank at `262` against a bound of `512` -- NOT at the bound. ###
### **IF IT FAILS, THE ACT STOPS AND REPORTS THAT INSTEAD.**
### ### **AND THE RAISED FRAME IS COMPARED TO `b354`'s OWN SIXTH RUNG AND TO NOTHING ELSE.**
"""
import io
import json
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import b316_instrument as INS   # noqa: E402
import b317_smear as SM         # noqa: E402
import b318_square as SQ        # noqa: E402
import b319_stable as ST        # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### SEALED IN THE REGISTRATION. ### THE CEILING IS CHOSEN, NOT READ.
WALL_CEILING = 1800.0
BYTES_CEILING = 8 * 1024 ** 3
RAISED = 1024
SIXTH_RAISED = (32768, 256.0, RAISED)
FIFTH_RAISED = (16384, 128.0, RAISED)
BAR_RANK = 262            # ### (D) bar 1 -- an EQUALITY on an integer, no floor needed
BAR_TRACE = 1e-3          # ### (D) bar 2 ; floor 9.753e-05, b344's measured move of THIS axis
BAR_TRACE_FLOOR = 9.753e-05
BAR_IDENTITY = 1e-9       # ### (D) bar 3 ; floor ~ dim*eps ~ 7e-12

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def seed(a):
    return SM.mean_zero_variant(a)


def main():
    t0 = time.time()
    P = json.load(io.open(os.path.join(D, 'b339_price.json'), encoding='utf-8'))
    B320 = json.load(io.open(os.path.join(D, 'b320_rows.json'), encoding='utf-8'))
    B354 = json.load(io.open(os.path.join(D, 'b354_sixth.json'), encoding='utf-8'))
    AX = json.load(io.open(os.path.join(D, 'b356_axis.json'), encoding='utf-8'))
    cells = sorted(P['cells'], key=float)

    rec('=' * 100)
    rec('b356 -- THE OBJECT OR THE BOUNDARY. ### THE AXIS RAISED, ONE PARAMETER, DELIBERATELY.')
    rec('=' * 100)
    rec('  ### the axis, as every act since b316 held it : NY = %d' % SM.NY_FIXED)
    rec('  ### the axis, raised here                     : NY = %d   ### **RE-TUNING, AND SAID TO BE**' % RAISED)
    rec('  ### the frame                                 : N=%d X=%g' % (SIXTH_RAISED[0], SIXTH_RAISED[1]))
    rec('  ### THE CHOSEN CEILING (registration (E))     : %.0f s ; %.0f GB'
        % (WALL_CEILING, BYTES_CEILING / 1024.0 ** 3))
    rec('  ### ### **A CHOSEN CEILING IS NOT A READ ONE.** ### b354 measured 212.1 s for its component, of')
    rec('  ### ### which the cells dominated, and how a cell scales with a larger rank is NOT in the record.')
    rec('  ### ### **SO THIS ACT CANNOT PRICE ITS OWN FRAME, AND SAYS SO.**')

    def over(where):
        el = time.time() - t0
        if el > WALL_CEILING:
            rec('')
            rec('  ### ### ### **THE RUN OVERRAN THE CHOSEN CEILING AT %s : %.1f s > %.0f s.**'
                % (where, el, WALL_CEILING))
            rec('  ### ### **ABANDONED. ### THE OVERRUN IS THE FINDING. ### NO BAR MOVES, NO PARTIAL VALUE')
            rec('  ### ### IS TAKEN, AND THIS OUTPUT IS BANKED AS IT STANDS.** ### The verdict is STILL')
            rec('  ### ### CONFOUNDED, by the third branch\'s own third clause.')
            return True
        return False

    # ================================================================ THE CONTROL.
    rec('')
    rec('-' * 100)
    rec('  ### THE CONTROL. ### **THE FIFTH RUNG UNDER THE RAISED AXIS. ### IT TESTS THE RAISE.**')
    rec('-' * 100)
    rec('    ### the precedent, from the only act that moved this axis: b344 found the rank CONSTANT at %d'
        % AX['b344_frame']['rank'])
    rec('    ### across NY = 128..2048 at N=%s X=%s, and the trace moving by %.3e relative over the step'
        % (AX['b344_frame']['N'], AX['b344_frame']['X'], AX['step_512_to_1024']))
    rec('    ### this act takes. ### **THAT IS THE FLOOR OF BAR 2, AND IT IS A MEASUREMENT OF THIS AXIS.**')
    rec('    ### **AND IT IS NOT A MEASUREMENT OF THIS RUNG:** b344 sat at rank %d against a bound of %d,'
        % (AX['b344_frame']['rank'], SM.NY_FIXED))
    rec('    ### far from it; the fifth rung sits at %d against the same bound, closer.' % BAR_RANK)
    t5 = time.time()
    fr5 = INS.Frame(*FIFTH_RAISED)
    st5, _g5 = ST.both_subspaces(fr5, ST.TAU)
    ti5, _f5, _c5 = SM.identity_trace(fr5, st5)
    id5 = abs(ti5 - st5['dim'])
    rec('')
    rec('    N=%-6d X=%-6.1f NY=%-5d  free=%-6d rank=%-4d dim=%-6d   (decomposition %.1f s)'
        % (FIFTH_RAISED[0], FIFTH_RAISED[1], RAISED, st5['free'], st5['rank'], st5['dim'], time.time() - t5))
    rank_ok = (int(st5['rank']) == BAR_RANK)
    rec('    ### **BAR 1 -- THE RANK, AN EQUALITY:** ### banked %d ; here %d ; %s'
        % (BAR_RANK, st5['rank'], 'HOLDS' if rank_ok else '### FAILS ###'))
    rec('    ### **BAR 3 -- THE IDENTITY CONTROL:** ### |Tr - dim| = %.3e  bar %.0e  floor ~ %.1e  %s'
        % (id5, BAR_IDENTITY, st5['dim'] * np.finfo(float).eps, 'HOLDS' if id5 <= BAR_IDENTITY else '### FAILS ###'))
    ctrl = []
    rec('    %-8s %-20s %-20s %-13s %s' % ('a', 'Tr at the raised axis', "b320's banked Tr", '|rel diff|', 'bar 1e-3'))
    for k in cells:
        tr = SQ.square_trace(fr5, st5, seed(float(k)))
        banked = B320['axes'][k]['domain'][-1]
        rd = abs(tr - banked) / max(abs(banked), 1e-300)
        ctrl.append(dict(a=k, here=float(tr), banked=float(banked), rel=float(rd), ok=bool(rd <= BAR_TRACE)))
        rec('    %-8s %-20.12f %-20.12f %-13.3e %s'
            % (k, tr, banked, rd, 'HOLDS' if rd <= BAR_TRACE else '### FAILS ###'))
        if over('the control, cell a=%s' % k):
            run_clock.write(D, 'b356_raised_run', LINES)
            return 1
    trace_ok = all(c['ok'] for c in ctrl)
    worst = max(c['rel'] for c in ctrl)
    rec('    ### **BAR 2 -- THE TRACE:** ### worst %.3e against a bar of %.0e whose floor is %.3e : %s'
        % (worst, BAR_TRACE, BAR_TRACE_FLOOR, 'HOLDS' if trace_ok else '### FAILS ###'))
    rec('    ### and the worst move is %.2f times b344\'s measured move of this axis over the same step.'
        % (worst / BAR_TRACE_FLOOR))
    control_ok = rank_ok and trace_ok and id5 <= BAR_IDENTITY
    rec('    ### ### **THE CONTROL : %s**' % ('HOLDS' if control_ok else '### FAILS ###'))
    if not control_ok:
        rec('    ### ### **THE RAISE MOVED A RUNG WHERE THE BOUND WAS NOT BINDING.** ### The order says the')
        rec('    ### ### act STOPS AND REPORTS THAT INSTEAD, and it does. ### **NO VERDICT ABOUT THE SIXTH')
        rec('    ### ### RUNG IS TAKEN**, and the branch is STILL CONFOUNDED with the control named as the')
        rec('    ### ### reason.')
        p = run_clock.write(D, 'b356_raised_run', LINES)
        io.open(os.path.join(D, 'b356_raised.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
            dict(verdict='STILL CONFOUNDED', reason='the control failed', control=ctrl,
                 control_ok=False, rank5=int(st5['rank']), rank_ok=bool(rank_ok), trace_ok=bool(trace_ok),
                 identity5=float(id5), raised=RAISED, wall=float(time.time() - t0),
                 wall_ceiling=WALL_CEILING, overran=False,
                 run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
        return 1
    rec('    ### **AND THAT LICENSES THE RAISED SIXTH RUNG**: the raise behaves as a quadrature refinement')
    rec('    ### at a rung where the bound was not binding.')
    if over('the control'):
        run_clock.write(D, 'b356_raised_run', LINES)
        return 1

    # ================================================================ THE RAISED SIXTH RUNG.
    rec('')
    rec('-' * 100)
    rec('  ### THE SIXTH RUNG, WITH THE AXIS RAISED.')
    rec('-' * 100)
    t6 = time.time()
    fr6 = INS.Frame(*SIXTH_RAISED)
    st6, _g6 = ST.both_subspaces(fr6, ST.TAU)
    t_svd = time.time() - t6
    ti6, _f6, _c6 = SM.identity_trace(fr6, st6)
    id6 = abs(ti6 - st6['dim'])
    rank6 = int(st6['rank'])
    old = B354['frame6']
    rec('    ### **b354, AT THE ORIGINAL AXIS** : free=%d rank=%d dim=%d   (rank AT the bound of %d)'
        % (old['free'], old['rank'], old['dim'], SM.NY_FIXED))
    rec('    ### **HERE, AT THE RAISED AXIS**   : free=%d rank=%d dim=%d   (bound now %d)'
        % (st6['free'], rank6, st6['dim'], RAISED))
    rec('    ### the decomposition alone : %.1f s (b354 measured %.1f s at the original axis)'
        % (t_svd, B354['svd_wall']))
    cleared = rank6 < RAISED
    rec('')
    rec('    ### ### **IS THE RANK STILL AT ITS BOUND? ### %s**'
        % ('NO -- %d against a bound of %d, with %d to spare' % (rank6, RAISED, RAISED - rank6) if cleared
           else 'YES -- %d against a bound of %d' % (rank6, RAISED)))
    rec('    ### the banked ranks extrapolated to about %.0f ; b354 observed %d at the old bound ; here %d'
        % (B354['rank_extrapolated'], old['rank'], rank6))
    rec('    ### **BAR 3 -- THE IDENTITY CONTROL:** ### |Tr - dim| = %.3e  bar %.0e  floor ~ %.1e  %s'
        % (id6, BAR_IDENTITY, st6['dim'] * np.finfo(float).eps, 'HOLDS' if id6 <= BAR_IDENTITY else '### FAILS ###'))
    if id6 > BAR_IDENTITY:
        rec('    ### ### **BAR 3 FAILS AT THE RAISED FRAME. ### THE ACT STOPS AND SAYS SO.**')
        run_clock.write(D, 'b356_raised_run', LINES)
        return 1
    if over('the raised sixth frame'):
        run_clock.write(D, 'b356_raised_run', LINES)
        return 1

    rows = {}
    rec('')
    rec('    %-8s %-16s %-16s %-16s %-18s %s'
        % ('a', 'W_inf', 'Tr(256, raised)', 'margin W - Tr', 'R = margin - INT_EF', 'wall'))
    for k in cells:
        tc = time.time()
        tr6 = SQ.square_trace(fr6, st6, seed(float(k)))
        c = P['cells'][k]
        margin = c['weil'] - tr6
        R6 = margin - c['int_ef']
        rows[k] = dict(tr=float(tr6), margin=float(margin), R=float(R6), wall=time.time() - tc)
        rec('    %-8s %-16.9f %-16.9f %-16.9f %-18.9f %.1f s' % (k, c['weil'], tr6, margin, R6, rows[k]['wall']))
        if over('cell a=%s' % k):
            run_clock.write(D, 'b356_raised_run', LINES)
            return 1
    wall = time.time() - t0
    rec('')
    rec('    ### ### **THE RAISED SIXTH RUNG LANDED. ### WALL : %.1f s AGAINST A CHOSEN CEILING OF %.0f s.**'
        % (wall, WALL_CEILING))

    # ================================================================ THE ONE COMPARISON LICENSED.
    rec('')
    rec('-' * 100)
    rec('  ### THE ONE COMPARISON THIS ACT LICENSES. ### **b354\'s OWN SIXTH RUNG, AND NOTHING ELSE.**')
    rec('-' * 100)
    rec('    ### The two frames differ in ONE parameter and agree in every other. ### **NO COMPARISON TO THE')
    rec('    ### FIFTH RUNG\'S RESIDUAL, TO b320\'s TABLE, OR TO ANY OTHER BANKED FIGURE IS TAKEN HERE.**')
    rec('    %-8s %-20s %-20s %-14s %s' % ('a', 'R at NY=512 (b354)', 'R at NY=1024 (here)', 'sign changed?', 'ratio'))
    signs = {}
    for k in cells:
        old_r = B354['per_cell'][k]['R_sixth']
        new_r = rows[k]['R']
        flipped = (old_r < 0) != (new_r < 0)
        signs[k] = dict(old=float(old_r), new=float(new_r), flipped=bool(flipped),
                        ratio=float(new_r / old_r) if old_r else None)
        rec('    %-8s %-+20.9e %-+20.9e %-14s %s'
            % (k, old_r, new_r, 'YES' if flipped else 'no',
               ('%.4f' % (new_r / old_r)) if old_r else '--'))
    all_neg = all(rows[k]['R'] < 0 for k in cells)
    all_pos = all(rows[k]['R'] > 0 for k in cells)

    # ================================================================ THE VERDICT.
    rec('')
    rec('-' * 100)
    rec("  ### THE VERDICT, BY THE SEALED BRANCH RULE OF SECTION (F).")
    rec('-' * 100)
    rec('    ### **(THE OBJECT)** demands TWO conditions together: the residual NEGATIVE at the raised axis')
    rec('      AND the rank no longer at the bound.')
    rec('      residual negative at every cell : %s ; rank clear of the bound : %s' % (all_neg, cleared))
    rec('    ### **(THE BOUNDARY)** demands the residual POSITIVE once the bound is lifted.')
    rec('      residual positive at every cell : %s' % all_pos)
    rec('    ### **(STILL CONFOUNDED)** -- the raise did not clear the bound, or the run overran, or the')
    rec('      control failed. ### control held : %s ; overran : %s ; bound cleared : %s'
        % (control_ok, False, cleared))
    if all_neg and cleared:
        verdict = 'THE OBJECT'
    elif all_pos and cleared:
        verdict = 'THE BOUNDARY'
    else:
        verdict = 'STILL CONFOUNDED'
    rec('    ### ### ### **VERDICT : %s**' % verdict)
    rec('')
    rec('    ### ### **AND THE READING THIS ACT MUST NOT MAKE, FIXED IN THE REGISTRATION BEFORE ANY VALUE:**')
    rec('    ### ### **A SIGN THAT SURVIVES ONE RAISE IS NOT A SIGN THAT SURVIVES THE LIMIT.** ### This act')
    rec('    ### ### has TWO points on the quadrature axis at this frame. ### **TWO POINTS ARE NOT A')
    rec('    ### ### CONVERGENCE**, and nothing here says what a third would show.')
    rec('    ### **AND THE CRITERION:** ### b352\'s stays and is not replaced. ### The residual is %s at the'
        % ('negative' if all_neg else ('positive' if all_pos else 'mixed in sign')))
    rec('    ### raised axis, so the sealed criterion is %s and %s.'
        % ('still undefined' if not all_pos else 'defined again',
           'NO SCORE IS REPORTED' if not all_pos else 'a score would be possible but is not ordered here'))
    rec('    ### **b354 IS NOT RE-VERDICTED** -- its own act said it could not tell the object from the')
    rec('    ### boundary, and this act tells it or does not. ### **b339\'s SIDE-READING IS HANDLED BY THE')
    rec('    ### ### BRANCH TAKEN AND IS NOT WITHDRAWN HERE.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b356_raised_run', LINES)
    io.open(os.path.join(D, 'b356_raised.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(verdict=verdict, raised=RAISED, sixth=list(SIXTH_RAISED), fifth=list(FIFTH_RAISED),
             cells=cells, rows=rows, signs=signs, control=ctrl, control_ok=bool(control_ok),
             rank5=int(st5['rank']), rank_ok=bool(rank_ok), trace_ok=bool(trace_ok),
             worst_control_rel=float(worst), bar_trace=BAR_TRACE, bar_trace_floor=BAR_TRACE_FLOOR,
             identity5=float(id5), identity6=float(id6), rank6=rank6, cleared=bool(cleared),
             frame6=dict(free=int(st6['free']), rank=rank6, dim=int(st6['dim'])),
             b354_frame6=old, all_neg=bool(all_neg), all_pos=bool(all_pos),
             wall=float(wall), svd_wall=float(t_svd), wall_ceiling=WALL_CEILING, overran=False,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
