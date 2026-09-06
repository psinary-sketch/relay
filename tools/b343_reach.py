# -*- coding: utf-8 -*-
"""b343_reach.py -- THE MAP'S NEXT REACH (registration sealed first, `data/b343_registration_2026-09-06.txt`).

###   `--fine a`     COMPONENT 1: the aim-map's four quantities at the thirteen sealed heights between 2 and 8, at the
###                  reaching width `a` (40 or 81), by b334's own code IMPORTED and not edited -- the archimedean
###                  distribution on two transforms and the (150) witness, the prime sum by two routes, the Epstein
###                  pair, the noise-floor gate on every sign; the room `A_z - PR_z` per height, the crossing looked
###                  for by the sealed rule, and the two heights shared with b334's coarse grid compared to its bank.
###   `--frames`     COMPONENT 2: the identity residual at one aimed seed (a = 1.41, gamma = 33.650101) at the
###                  reference frame and the two larger grid-axis frames -- the stable cut's rank and free dimension
###                  at each, the identity control, the square, the archimedean side, the remainder under BOTH
###                  conventions each NAMED (the erratum's standing clause) by both quadratures, and the residual;
###                  read against b339's floor by the sealed reading rule and no wider.
### ### **EVERY INSTRUMENT IS IMPORTED, NEVER EDITED.** ### Each mode writes its own run file once; a repeat writing
### run is numbered. ### **A FINER CHART IS A FINER CHART.**
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
import b334_aimmap as AM        # noqa: E402  ### the grid, the seed, the quantities, the gate, the comparator -- IMPORTED
import b316_instrument as INS   # noqa: E402
import b317_smear as SM         # noqa: E402
import b318_square as SQ        # noqa: E402
import b319_stable as ST        # noqa: E402
import b321_window as WI        # noqa: E402
import b326_windows as BW       # noqa: E402
import b328_family as FA        # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE GRID, AS SEALED IN SECTION (C). ### NOT ADDED TO, NOT MOVED.
FINE = (2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0)
WIDTHS = (40.0, 81.0)
SHARED = (4.0, 8.0)                    # ### the heights this grid shares with b334's coarse one
SEED_A, SEED_G = 1.41, 33.650101       # ### section (D): the aimed seed, sealed
FRAMES = (tuple(SM.REFERENCE), tuple(SM.GRID_AXIS[2]), tuple(SM.GRID_AXIS[3]))
BAR_SHARED = 1e-12                     # ### (F3), relative
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def runfile(base):
    p = os.path.join(D, base + '_run.txt')
    k = 1
    while os.path.exists(p):
        k += 1
        p = os.path.join(D, base + '_run%d.txt' % k)
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    return os.path.basename(p)


def dump(base, obj):
    io.open(os.path.join(D, base + '.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(obj, indent=1))


# ### ==============================================================================================
# ### COMPONENT 1 -- the finer grid at one reaching width
# ### ==============================================================================================
def fine(a):
    t0 = time.time()
    rec('=' * 100)
    rec("b343 -- COMPONENT 1, THE FINER GRID, a = %g. ### thirteen heights between 2 and 8, b334's own quantities, the gate on every sign." % a)
    rec('=' * 100)
    if not AM.fixture_like():
        rec('  ### the like-for-like fixture FAILS ; refusing to proceed.')
        return 2
    rec("  the like-for-like comparator's fixture fires (b334's, imported) : the sealed grid is %s" % (FINE,))
    N = int(a * a) + 2
    lam_z, lam_q, _lq2, lamq_diff = FA.finite_sides(N)
    rec('  finite sides to n = %d ; Lambda_Q by the divisor sieve against b325\'s inversion : worst %.3e %s' % (N, lamq_diff, 'HOLDS' if lamq_diff <= AM.BAR_LAMQ else '### EXCEEDS ###'))
    rec("  THE SQUARE'S REACH, MEASURED : the frame's X = %g against f's support a^2 = %g : %s" % (AM.FRAME_REF[1], a * a, 'NOT REACHED' if a * a > AM.FRAME_REF[1] else 'reached'))
    eps_vals, eps_bad, _ok = AM.eps_reach()
    rec("  THE REMAINDER'S REACH : %s" % ('NOT REACHED at this width (rho to %g)' % (a * a) if eps_bad else 'reached'))
    rec('  ### both are b334\'s findings, re-measured here; the square and the remainder are NOT evaluated on this leg.')
    out = []
    for g in FINE:
        s = AM.seed_aimed(g, a)
        rec('')
        rec('  gamma = %.6f  width %g  seed %s  cond %.2e' % (g, a, s.name, s.cond))
        f, r = AM.quantities(s, lam_z, lam_q, lamq_diff)
        r.update(gamma=g, a=a, seed=s.name, square='NOT REACHED', remainder='NOT REACHED')
        AM.print_quantities(r)
        out.append(r)
    rec('')
    rec('  %-10s %16s %16s %16s %7s %16s %16s %16s %7s' % ('gamma', 'A_z', 'PR_z', 'room_z', 'sign', 'A_Q', 'finite_Q', 'room_Q', 'sign'))
    for r in out:
        rec('  %-10.6f %+16.9f %+16.9f %+16.9f %7s %+16.9f %+16.9f %+16.9f %7s'
            % (r['gamma'], r['arch_z'], r['prime_z'], r['room_z'], r['gate']['places_z']['sign'], r['arch_q'], r['finite_q'], r['room_q'], r['gate']['places_q']['sign']))
    rec('  wall %.1f s' % (time.time() - t0))
    rec('=' * 100)
    dump('b343_fine_%g' % a, dict(a=a, N=N, grid=list(FINE), lamq_diff=lamq_diff,
                                  eps_reach=dict(radii=AM.EPS_RADII, values=eps_vals, outside_at=eps_bad),
                                  square_reach=dict(X=AM.FRAME_REF[1], support=a * a), rows=out))
    runfile('b343_fine_%g' % a)
    return 0


# ### ==============================================================================================
# ### COMPONENT 2 -- the residual against the frame, at one aimed seed
# ### ==============================================================================================
def frames():
    t0 = time.time()
    rec('=' * 100)
    rec('b343 -- COMPONENT 2, THE RESIDUAL AGAINST THE FRAME. ### one aimed seed, three grid-axis frames; a measurement of the instrument.')
    rec('=' * 100)
    s = AM.seed_aimed(SEED_G, SEED_A)
    rec('  the sealed seed : a = %g, gamma = %.6f, %s ; cond %.2e' % (SEED_A, SEED_G, s.name, s.cond))
    # ### `seed_aimed` returns b317's TestFunction itself; the squared object is b318's autocorrelation of it,
    # ### exactly as b334's covered leg forms it.
    g = s
    f = SQ.autocorrelation(g)
    rec('  the object squared : %s ; support %g against the frame X = %g : %s' % (f.name, f.support, FRAMES[0][1], 'reached' if f.support <= FRAMES[0][1] else '### NOT REACHED'))
    # ### the archimedean side, frame-independent: computed ONCE and printed at every frame so the reader sees it does not move
    lam_z, lam_q = BW.von_mangoldt_sieve(2600), BW.lambda_q_sieve(2600)
    ch = BW.channels(f, lam_z, lam_q, refine=1)
    A_z = ch['arch_z']
    rec('  A_z on the squared seed by the derived kernel (b326 channels, refine 1) : %+.12f   ### frame-independent by construction' % A_z)
    # ### the remainder under BOTH conventions, each NAMED (E-2026-09-03-1's standing clause)
    rem = {}
    for lbl, mod in (("the SOURCE convention rho^{+1/2} (b313f, EF)", WI.EF), ("the CORPUS convention rho^{-1/2} (b313r, ER)", WI.ER)):
        u = WI.remainder_integral(f, mod, 'uniform')
        c = WI.remainder_integral(f, mod, 'cheb')
        rem[lbl] = (u, c)
        rec('  INT f eps under %-46s : uniform %+.12f ; chebyshev %+.12f ; apart %.3e' % (lbl, u, c, abs(u - c)))
    rec('')
    rec('  %-22s %8s %8s %8s %14s %18s %18s %18s' % ('frame (N, X, NY)', 'free', 'rank', 'dim', 'identity ctl', 'Tr (square)', 'R under EF', 'R under ER'))
    rows = []
    for fk in FRAMES:
        fr = INS.Frame(*fk)
        st, _gr = ST.both_subspaces(fr, ST.TAU)
        ti, _ff, _cc = SM.identity_trace(fr, st)
        tr = SQ.square_trace(fr, st, g)
        rEF = (A_z - tr) - rem[list(rem)[0]][0]
        rER = (A_z - tr) - rem[list(rem)[1]][0]
        rec('  %-22s %8d %8d %8d %14.3e %+18.9f %+18.9f %+18.9f' % ('(%d, %g, %d)' % fk, st['free'], st['rank'], st['dim'], abs(ti - st['dim']), tr, rEF, rER))
        rows.append(dict(frame=list(fk), free=st['free'], rank=st['rank'], dim=st['dim'], identity=abs(ti - st['dim']), Tr=tr, R_EF=rEF, R_ER=rER))
        del fr, st
    ranks = set(r['rank'] for r in rows)
    rec('')
    rec('  ### WHAT MOVED AND WHAT DID NOT: N %s ; X %s ; NY %s ; ### **THE STABLE-CUT RANK : %s**'
        % ([r['frame'][0] for r in rows], sorted(set(r['frame'][1] for r in rows)), sorted(set(r['frame'][2] for r in rows)),
           'CONSTANT at %d' % rows[0]['rank'] if len(ranks) == 1 else 'MOVED: %s' % sorted(ranks)))
    for key, lbl in (('R_EF', "the source's convention"), ('R_ER', "the corpus's convention")):
        v = [r[key] for r in rows]
        d1, d2 = v[1] - v[0], v[2] - v[1]
        rel = max(abs(d1), abs(d2)) / max(abs(v[0]), 1e-300)
        rec('  ### the residual under %-26s : %s ; step differences %+.3e and %+.3e ; largest relative change %.3e'
            % (lbl, ' '.join('%+.9f' % x for x in v), d1, d2, rel))
    relEF = max(abs(rows[1]['R_EF'] - rows[0]['R_EF']), abs(rows[2]['R_EF'] - rows[1]['R_EF'])) / max(abs(rows[0]['R_EF']), 1e-300)
    relER = max(abs(rows[1]['R_ER'] - rows[0]['R_ER']), abs(rows[2]['R_ER'] - rows[1]['R_ER'])) / max(abs(rows[0]['R_ER']), 1e-300)
    unchanged = relEF < 1e-3 and relER < 1e-3
    rec('')
    rec('  ### ### **THE READING, BY THE SEALED RULE OF SECTION (D), AND NO WIDER:**')
    if len(ranks) == 1:
        rec("  ### the axis the draft names holds the rank CONSTANT at %d while N doubles twice, so it varies the GRID and not the RANK;" % rows[0]['rank'])
        rec("  ### **THE DRAFT'S (F2) -- *the residual grows with rank* -- CANNOT BE SCORED ON THIS AXIS, AND IS SCORED NOT APPLICABLE.**")
    else:
        rec('  ### the rank MOVED on this axis (%s), against the axis definition; the draft\'s (F2) is scored on the values above.' % sorted(ranks))
    if unchanged:
        rec('  ### the residual is unchanged across two doublings of N at fixed X, NY and rank (largest relative change %.3e under the' % max(relEF, relER))
        rec("  ### source's convention and %.3e under the corpus's), so ### **THE GRID RESOLUTION AT FIXED DOMAIN IS NOT THE ORIGIN OF" % relER)
        rec("  ### b339's FLOOR.** ### The floor's other candidates -- the fixed NY, the cut's tau, the taper -- are UNTOUCHED by this.")
    else:
        rec('  ### the residual CHANGED across the doublings (largest relative change %.3e) ; the size is reported and NOTHING is concluded' % max(relEF, relER))
        rec("  ### about b339's floor.")
    rec('  wall %.1f s' % (time.time() - t0))
    rec('=' * 100)
    dump('b343_frames', dict(seed=dict(a=SEED_A, gamma=SEED_G, name=s.name, cond=s.cond), object=f.name, support=f.support, A_z=A_z,
                             remainder={k: dict(uniform=v[0], cheb=v[1]) for k, v in rem.items()}, frames=rows,
                             rank_constant=bool(len(ranks) == 1), rel_EF=relEF, rel_ER=relER, unchanged=bool(unchanged)))
    runfile('b343_frames')
    return 0


def main(argv):
    if argv and argv[0] == '--fine' and len(argv) > 1:
        return fine(float(argv[1]))
    if argv and argv[0] == '--frames':
        return frames()
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
