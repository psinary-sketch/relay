# -*- coding: utf-8 -*-
"""b344_edge.py -- COMPONENT 2b: THE ROOM'S EDGE. ### the grid extended downward past b343's edge, at ONE width only.

### ### **THE REGISTRATION IS SEALED (section (E)); THIS TOOL MEASURES ITS BARS.** ### b343's minimum at `a = 81` sat at
### its sealed lower edge of `gamma = 2.0`, so that interval did not bracket it. ### This tool extends the grid by one
### unit below that edge at quarter-unit steps -- `gamma = 1.00, 1.25, 1.50, 1.75` -- ### **AT `a = 81` ONLY**; `a = 40`'s
### minimum was interior and is not extended. ### Every quantity is b334's own code, IMPORTED and not edited, called
### exactly as b343 called it: the archimedean distribution on two transforms with the (150) witness, the prime sum by
### two routes, the noise-floor gate on every sign.
### ### **THE VERDICT** by the sealed rule: BRACKETED (an interior minimum), STILL AT THE EDGE (the minimum at the new
### lower boundary), or A CROSSING, LOCATED (b343's own rule, reported before anything else).
### ### **A NARROWER ROOM AT A FINER GRID IS A FINER CHART AND NOT A TREND, AND NOTHING ABOUT TOTALITY FOLLOWS.**
"""
import io
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import b334_aimmap as AM        # noqa: E402  ### the seed, the quantities, the gate, the comparator -- IMPORTED
import b328_family as FA        # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### SEALED IN SECTION (E). ### NOT ADDED TO, NOT MOVED.
EXTEND = (1.00, 1.25, 1.50, 1.75)
WIDTH = 81.0
OLD_EDGE = 2.0
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def main():
    t0 = time.time()
    rec('=' * 100)
    rec("b344 -- COMPONENT 2b, THE ROOM'S EDGE. ### the grid extended one unit below b343's edge, at a = %g only." % WIDTH)
    rec('=' * 100)
    if not AM.fixture_like():
        rec('  ### the like-for-like fixture FAILS ; refusing to proceed.')
        return 2
    rec("  the like-for-like comparator's fixture fires (b334's, imported) ; the sealed extension is %s below b343's edge of %g" % (EXTEND, OLD_EDGE))
    prior = json.load(io.open(os.path.join(D, 'b343_fine_%g.json' % WIDTH), encoding='utf-8'))
    prior_rows = sorted(prior['rows'], key=lambda r: r['gamma'])
    rec("  b343's own rows at this width, read from its record : %d heights from %g to %g ; its minimum room %+.9f at gamma = %.6f"
        % (len(prior_rows), prior_rows[0]['gamma'], prior_rows[-1]['gamma'],
           min(r['room_z'] for r in prior_rows), min(prior_rows, key=lambda r: r['room_z'])['gamma']))
    N = int(WIDTH * WIDTH) + 2
    lam_z, lam_q, _lq2, lamq_diff = FA.finite_sides(N)
    rec('  finite sides to n = %d ; Lambda_Q by the divisor sieve against b325\'s inversion : worst %.3e %s' % (N, lamq_diff, 'HOLDS' if lamq_diff <= AM.BAR_LAMQ else '### EXCEEDS ###'))
    rec("  THE SQUARE'S REACH, MEASURED : the frame's X = %g against a^2 = %g : NOT REACHED -- the square and the remainder are NOT evaluated here" % (AM.FRAME_REF[1], WIDTH * WIDTH))
    out = []
    for g in EXTEND:
        s = AM.seed_aimed(g, WIDTH)
        rec('')
        rec('  gamma = %.6f  width %g  seed %s  cond %.2e' % (g, WIDTH, s.name, s.cond))
        _f, r = AM.quantities(s, lam_z, lam_q, lamq_diff)
        r.update(gamma=g, a=WIDTH, seed=s.name, square='NOT REACHED', remainder='NOT REACHED')
        AM.print_quantities(r)
        out.append(r)
    # ### the extended grid, this act's rows and b343's together
    joint = sorted(out + prior_rows, key=lambda r: r['gamma'])
    rec('')
    rec('  ### THE EXTENDED GRID AT a = %g -- this act\'s heights and b343\'s together:' % WIDTH)
    rec('  %-10s %-8s %18s %18s %18s %10s %8s' % ('gamma', 'from', 'A_z', 'PR_z', 'room_z', 'gate', 'sign'))
    for r in joint:
        rec('  %-10.6f %-8s %+18.9f %+18.9f %+18.9f %10s %8s'
            % (r['gamma'], 'b344' if r['gamma'] < OLD_EDGE else 'b343', r['arch_z'], r['prime_z'], r['room_z'], r['gate']['places_z']['verdict'], r['gate']['places_z']['sign']))
    signs = [(r['gamma'], r['gate']['places_z']['sign'], r['room_z']) for r in joint if r['gate']['places_z']['sign'] in ('+', '-')]
    refused = [r['gamma'] for r in joint if r['gate']['places_z']['sign'] not in ('+', '-')]
    pairs = [(signs[i][0], signs[i + 1][0]) for i in range(len(signs) - 1) if signs[i][1] != signs[i + 1][1]]
    negative = [g for g, sg, v in signs if v < 0]
    lo = min(joint, key=lambda r: r['room_z'])
    idx = [r['gamma'] for r in joint].index(lo['gamma'])
    interior = 0 < idx < len(joint) - 1
    rec('')
    if pairs or negative:
        rec('  ### ### **A CROSSING, LOCATED at a = %g : adjacent pairs %s ; heights with a negative room %s**' % (WIDTH, pairs, negative))
        verdict = 'A CROSSING, LOCATED at a = %g' % WIDTH
    elif refused:
        rec('  ### ### **REFUSED : the gate declines a sign at %s ; the question is left open there**' % refused)
        verdict = 'REFUSED at a = %g' % WIDTH
    elif interior:
        rec("  ### ### **BRACKETED: the room's minimum over the extended grid is INTERIOR, at gamma = %.6f, room %+.9f**" % (lo['gamma'], lo['room_z']))
        rec('  ###      its neighbours are %+.9f at gamma = %.2f and %+.9f at gamma = %.2f, both larger.'
            % (joint[idx - 1]['room_z'], joint[idx - 1]['gamma'], joint[idx + 1]['room_z'], joint[idx + 1]['gamma']))
        verdict = "BRACKETED at a = %g, the minimum interior at gamma = %.6f" % (WIDTH, lo['gamma'])
    else:
        rec("  ### ### **STILL AT THE EDGE: the room's minimum sits at gamma = %.6f, the extended grid's own boundary; THIS INTERVAL DOES NOT BRACKET IT EITHER**" % lo['gamma'])
        verdict = 'STILL AT THE EDGE at a = %g, the minimum at gamma = %.6f' % (WIDTH, lo['gamma'])
    prior_min = min(r['room_z'] for r in prior_rows)
    rec('')
    rec("  ### THE NARROWING, AS MEASURED: b343's minimum on its own grid was %+.9f ; the extended grid's is %+.9f ; the ratio is %.2f."
        % (prior_min, lo['room_z'], prior_min / lo['room_z'] if lo['room_z'] else float('nan')))
    rec('  ### ### **A NARROWER ROOM AT A FINER GRID IS A FINER CHART AND NOT A TREND, AND NOTHING ABOUT TOTALITY FOLLOWS.**')
    rec('  ### The square and the remainder are NOT REACHED at this width and were not evaluated.')
    rec('  ### wall %.1f s' % (time.time() - t0))
    rec('=' * 100)
    p, k = os.path.join(D, 'b344_edge_run.txt'), 1
    while os.path.exists(p):
        k += 1
        p = os.path.join(D, 'b344_edge_run%d.txt' % k)
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    io.open(os.path.join(D, 'b344_edge.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(width=WIDTH, extension=list(EXTEND), old_edge=OLD_EDGE, rows=out,
             joint=[dict(gamma=r['gamma'], arch_z=r['arch_z'], prime_z=r['prime_z'], room_z=r['room_z'],
                         verdict=r['gate']['places_z']['verdict'], sign=r['gate']['places_z']['sign'],
                         source='b344' if r['gamma'] < OLD_EDGE else 'b343') for r in joint],
             minimum=dict(gamma=lo['gamma'], room_z=lo['room_z'], interior=bool(interior)),
             prior_minimum=prior_min, ratio=prior_min / lo['room_z'] if lo['room_z'] else None,
             verdict=verdict, refused=refused, pairs=pairs, negative=negative, run_file=os.path.basename(p)), indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
