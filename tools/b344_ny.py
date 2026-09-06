# -*- coding: utf-8 -*-
"""b344_ny.py -- COMPONENT 1: THE FLOOR PRICED ON ONE AXIS. ### `NY` MOVED; `tau` AND THE TAPER HELD AND PRINTED.

### ### **THE REGISTRATION IS SEALED (`data/b344_registration_2026-09-06.txt`, section (C)); THIS TOOL MEASURES ITS BARS.**
### The axis is `NY`, chosen there with its reason before any value. ### The ladder is `128, 256, 512, 1024, 2048` at the
### reference frame's `N = 4096` and `X = 32`, both held; the object is `autocorrelation(mean_zero_variant(1.41))`, the one
### b320 measured and b339 priced, at the covered cell where b339's floor is narrowest.
### ### **AT EVERY RUNG THE TWO AXES NOT MOVED ARE PRINTED** (the ferry's ADDITION ONE), with the quantities a later act
### needs to price them without re-running this one: the cut's `tau` in force, how many of the sandwich's eigenvalues lie
### within a decade either side of it, and the distance between the smallest kept and the largest dropped; and the taper's
### `ALPHA` and `BETA`. ### **NEITHER IS MOVED HERE.**
### ### **THE REMAINDER IS CARRIED UNDER BOTH CONVENTIONS, EACH NAMED** (`E-2026-09-03-1`'s standing clause).
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
import b320_weil as WE          # noqa: E402
import b321_window as WI        # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### SEALED IN SECTION (C). ### NOT ADDED TO, NOT MOVED.
LADDER = (128, 256, 512, 1024, 2048)
N_FIXED, X_FIXED = 4096, 32.0
CELL = 1.41
SEPARATION = 0.003993528          # ### b321's `apart by` at this cell, quoted from its bank
FLOOR_IN_S = 1.6                  # ### b339: the limit above the source's copy at this cell, in separations
BAR_MOVES = 1e-3                  # ### b343's own threshold, carried so the two acts are comparable
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def held_axes(st):
    """### THE TWO AXES NOT MOVED, PRINTED SO A LATER ACT CAN PRICE THEM WITHOUT RE-RUNNING THIS ONE."""
    eig = np.sort(np.asarray(st['eig'], dtype=float))[::-1]
    tau = float(st['tau'])
    near = int(((eig > tau / 10.0) & (eig < tau * 10.0)).sum())
    kept = eig[eig > tau]
    dropped = eig[eig <= tau]
    lo_kept = float(kept[-1]) if kept.size else float('nan')
    hi_drop = float(dropped[0]) if dropped.size else float('nan')
    return dict(tau=tau, eig_within_decade=near, smallest_kept=lo_kept, largest_dropped=hi_drop,
                distance=lo_kept - hi_drop, alpha=float(INS.ALPHA), beta=float(INS.BETA))


def main():
    t0 = time.time()
    rec('=' * 100)
    rec('b344 -- COMPONENT 1, THE FLOOR PRICED ON ONE AXIS. ### NY moved ; tau and the taper held and printed at every rung.')
    rec('=' * 100)
    g = SM.mean_zero_variant(CELL)
    f = SQ.autocorrelation(g)
    rec('  the object, sealed : %s -> %s ; support %g against the frame X = %g : %s'
        % (g.name, f.name, f.support, X_FIXED, 'reached' if f.support <= X_FIXED else '### NOT REACHED'))
    wv, wreg, wsing, wp0 = WE.weil(f)
    rec("  W_infinity(f) by b320's own route, frame-independent : %+.12f" % wv)
    rem = {}
    for lbl, mod in (("the SOURCE convention rho^{+1/2} (b313f, EF)", WI.EF), ("the CORPUS convention rho^{-1/2} (b313r, ER)", WI.ER)):
        u = WI.remainder_integral(f, mod, 'uniform')
        c = WI.remainder_integral(f, mod, 'cheb')
        rem[lbl] = (u, c)
        rec('  INT f eps under %-46s : uniform %+.12f ; chebyshev %+.12f ; apart %.3e' % (lbl, u, c, abs(u - c)))
    kEF, kER = list(rem)
    rec('  ### the floor this act measures against, from b339 at this cell : %.1f separations x %.9f = %+.9f in the residual\'s units'
        % (FLOOR_IN_S, SEPARATION, FLOOR_IN_S * SEPARATION))
    rec('')
    rec('  %-6s %-8s %-8s %-8s %-13s %-16s %-16s %-16s' % ('NY', 'free', 'rank', 'dim', 'identity ctl', 'Tr (square)', 'R under EF', 'R under ER'))
    rows = []
    for ny in LADDER:
        tr0 = time.time()
        fr = INS.Frame(N_FIXED, X_FIXED, ny)
        st, _gr = ST.both_subspaces(fr, ST.TAU)
        ti, _f2, _c2 = SM.identity_trace(fr, st)
        tr = SQ.square_trace(fr, st, g)
        rEF = (wv - tr) - rem[kEF][0]
        rER = (wv - tr) - rem[kER][0]
        h = held_axes(st)
        rec('  %-6d %-8d %-8d %-8d %-13.3e %+16.9f %+16.9f %+16.9f   (%.0f s)'
            % (ny, st['free'], st['rank'], st['dim'], abs(ti - st['dim']), tr, rEF, rER, time.time() - tr0))
        rec('        ### HELD, NOT MOVED -- the cut : tau = %.1e ; eigenvalues within a decade either side : %d ; smallest kept %.6e ; largest dropped %.6e ; distance %.6e'
            % (h['tau'], h['eig_within_decade'], h['smallest_kept'], h['largest_dropped'], h['distance']))
        rec('        ### HELD, NOT MOVED -- the taper : ALPHA = %.6g ; BETA = %.6g' % (h['alpha'], h['beta']))
        rows.append(dict(NY=ny, free=st['free'], rank=st['rank'], dim=st['dim'], identity=abs(ti - st['dim']), Tr=tr, R_EF=rEF, R_ER=rER, held=h,
                         wall=time.time() - tr0))
        del fr, st
    # ### the verdict by the sealed rule of section (C)
    vEF = [r['R_EF'] for r in rows]
    vER = [r['R_ER'] for r in rows]
    absEF, absER = max(vEF) - min(vEF), max(vER) - min(vER)
    relEF = absEF / max(abs(vEF[LADDER.index(512)]), 1e-300)
    relER = absER / max(abs(vER[LADDER.index(512)]), 1e-300)
    floor = FLOOR_IN_S * SEPARATION
    moves = max(relEF, relER) > BAR_MOVES
    biggest = max(absEF, absER)
    if biggest >= floor / 2.0:
        size = 'OF THE SIZE THE FLOOR REQUIRES'
    elif biggest < floor / 10.0:
        size = 'NOT OF THAT SIZE'
    else:
        size = 'INCONCLUSIVE AT THIS LADDER'
    ranks = [r['rank'] for r in rows]
    rec('')
    rec('  ### THE RANK ALONG THE LADDER : %s ; %s' % (ranks, 'CONSTANT' if len(set(ranks)) == 1 else 'IT MOVES WITH NY'))
    rec('  ### THE RESIDUAL UNDER THE SOURCE\'S CONVENTION : %s' % ' '.join('%+.9f' % v for v in vEF))
    rec('  ### THE RESIDUAL UNDER THE CORPUS\'S CONVENTION : %s' % ' '.join('%+.9f' % v for v in vER))
    rec('  ### span across the ladder : %.6e (source) and %.6e (corpus) absolute ; %.3e and %.3e relative to the NY = 512 rung'
        % (absEF, absER, relEF, relER))
    rec('  ### ### **THE RESIDUAL %s WITH NY** (largest relative change %.3e against the sealed threshold %.0e).'
        % ('MOVES' if moves else 'DOES NOT MOVE', max(relEF, relER), BAR_MOVES))
    rec("  ### ### **AND THE MOVEMENT IS %s**: the largest absolute change is %.6e against b339's floor at this cell, %+.9f"
        % (size, biggest, floor))
    rec('  ###      (half the floor is %.6e ; a tenth of it is %.6e -- the two thresholds sealed in section (C)).' % (floor / 2.0, floor / 10.0))
    rec('  ### NOTHING IS CONCLUDED ABOUT THE TWO AXES HELD. ### ONE AXIS MOVED IS ONE AXIS MOVED.')
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)
    p, k = os.path.join(D, 'b344_ny_run.txt'), 1
    while os.path.exists(p):
        k += 1
        p = os.path.join(D, 'b344_ny_run%d.txt' % k)
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    io.open(os.path.join(D, 'b344_ny.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(ladder=list(LADDER), N=N_FIXED, X=X_FIXED, cell=CELL, object=f.name, weil=wv,
             remainder={k2: dict(uniform=v[0], cheb=v[1]) for k2, v in rem.items()}, rows=rows,
             span_abs_EF=absEF, span_abs_ER=absER, rel_EF=relEF, rel_ER=relER, floor=floor, separation=SEPARATION,
             moves=bool(moves), size=size, rank_constant=bool(len(set(ranks)) == 1), ranks=ranks, run_file=os.path.basename(p)), indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
