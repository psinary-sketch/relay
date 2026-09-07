# -*- coding: utf-8 -*-
"""b349_extend.py -- PART (b): THE HEIGHT GRID EXTENDED BELOW THE BRACKETED MINIMUM.

### ### **IT RUNS ONLY BECAUSE PART (a) LEFT THE LOW-HEIGHT MINIMUM STANDING IN THE RELATIVE MEASURE**, and it
### refuses to run if `b349_relative.json` does not say so.
### ### **THE SPAN IS THE SEALED ONE AND NOTHING ELSE:** `gamma = 0.75, 0.50, 0.25` at `a = 81` only.
### ### ### **AND EVERY SEED IS CHECKED BEFORE IT IS CHARTED, ON BOTH SEALED CONDITIONS:**
###   ### (1) LAWFULNESS by the source's own definition, through `b328_family.lawfulness`, IMPORTED.
###   ### (2) THE PHASE AT THE AIM, as a ### **WINDOW** ### and not a threshold -- b328's refinement as b334
###     carries it: the sign condition holds exactly when `45 < |phase| < 135` degrees.
### ### **A SEED FAILING EITHER IS REPORTED AS DEGENERATE AND IS NOT CHARTED.** ### It contributes no room and
### enters no minimum. ### **THE CONSTRUCTION MAY DEGENERATE AS THE HEIGHT FALLS, AND THAT IS A FINDING.**
"""
import io
import json
import math
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock            # noqa: E402
import b334_aimmap as AM    # noqa: E402  ### the seed, the quantities, the gate -- IMPORTED
import b328_family as FA    # noqa: E402  ### lawfulness and the transform -- IMPORTED

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EXTEND = (0.75, 0.50, 0.25)      # ### sealed, section (E)
WIDTH = 81.0                     # ### sealed, section (E)
LO, HI = 45.0, 135.0             # ### sealed, section (E): the WINDOW, not a threshold
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def main():
    t0 = time.time()
    rec('=' * 100)
    rec("b349 -- PART (b): THE HEIGHT GRID EXTENDED BELOW THE BRACKETED MINIMUM, at a = %g only." % WIDTH)
    rec('=' * 100)
    R = json.load(io.open(os.path.join(D, 'b349_relative.json'), encoding='utf-8'))
    if not R.get('survives'):
        rec('  ### ### **PART (a) DID NOT LEAVE THE MINIMUM STANDING. ### PART (b) DOES NOT RUN.**')
        return 3
    rec('  part (a) left the minimum standing in the relative measure at a = %g, so this part runs.' % R['desk_width'])
    if not AM.fixture_like():
        rec('  ### the like-for-like fixture FAILS ; refusing to proceed.')
        return 2
    fa, fb, fc, fd = FA.fixtures()
    rec('  FIXTURES : like-for-like refuses a name mismatch True ; the condition both polarities %s' % all((fa, fb, fc, fd)))
    rec('  the sealed extension %s, below b344\'s lowest charted height of 1.00 and below its bracketed minimum at 1.25' % (EXTEND,))
    rec('  the sealed phase WINDOW : %g < |phase| < %g degrees (b328\'s refinement, a window and NOT a threshold)' % (LO, HI))
    prior = json.load(io.open(os.path.join(D, 'b344_edge.json'), encoding='utf-8'))
    prior_rows = sorted(prior['rows'], key=lambda r: r['gamma'])
    rec("  b344's own rows at this width, read from its record : %d heights from %g to %g ; its minimum room %+.9f at gamma = %.2f"
        % (len(prior_rows), prior_rows[0]['gamma'], prior_rows[-1]['gamma'],
           min(r['room_z'] for r in prior_rows), min(prior_rows, key=lambda r: r['room_z'])['gamma']))

    # ### ### **THE SEEDS ARE CHECKED BEFORE ANY FINITE SIDE IS COMPUTED.** ### A degenerate seed costs nothing.
    rec('')
    rec('  THE SEEDS, CHECKED ON BOTH SEALED CONDITIONS BEFORE ANY IS CHARTED:')
    rec('    %-8s %-12s %-9s %-11s %-11s %-11s %-11s %-9s %s'
        % ('gamma', 'cond', 'def 3.1', 'poles ok', 'min f-hat', 'phase deg', 'in window', 'LAWFUL', 'verdict'))
    seeds, charted, degenerate = [], [], []
    for g in EXTEND:
        s = AM.seed_aimed(g, WIDTH)
        law = FA.lawfulness(s)
        lawful = bool(law['def31'] and law['poles_ok'])
        # ### the phase at the aim: the aim's own beta, from b334's own list, at this height
        ph = []
        for b in AM.BETAS:
            tr = FA.transform_at(s, complex(b - 0.5, g))
            ph.append((b, tr['phase_deg'], tr['S4'], tr['route_diff'], tr['route_ok']))
        best = max(ph, key=lambda x: (LO < abs(x[1]) < HI, abs(x[1])))
        in_win = bool(LO < abs(best[1]) < HI)
        ok = lawful and in_win
        rec('    %-8.2f %-12.3e %-9s %-11s %-11.2e %-11.3f %-11s %-9s %s'
            % (g, s.cond, law['def31'], law['poles_ok'], law['min_fhat'], best[1], in_win, lawful,
               'CHARTED' if ok else '### DEGENERATE'))
        e = dict(gamma=g, cond=float(s.cond), def31=bool(law['def31']), poles_ok=bool(law['poles_ok']),
                 min_fhat=float(law['min_fhat']), lawful=lawful, beta=float(best[0]), phase_deg=float(best[1]),
                 S4=float(best[2]), route_diff=float(best[3]), in_window=in_win, charted=bool(ok),
                 phases=[[float(b), float(p)] for b, p, _s, _d, _o in ph])
        seeds.append(e)
        (charted if ok else degenerate).append((g, s, e))
    rec('    ### seeds built %d ; CHARTED %d ; ### **DEGENERATE %d** -- reported and NOT charted'
        % (len(seeds), len(charted), len(degenerate)))
    for g, _s, e in degenerate:
        why = []
        if not e['def31']:
            why.append("the source's Definition 3.1 fails")
        if not e['poles_ok']:
            why.append('the pole conditions fail')
        if not e['in_window']:
            why.append('the phase %.3f deg is outside the window' % e['phase_deg'])
        rec('    ### DEGENERATE at gamma = %.2f : %s' % (g, ' ; '.join(why)))

    out = []
    if charted:
        N = int(WIDTH * WIDTH) + 2
        lam_z, lam_q, _lq2, lamq_diff = FA.finite_sides(N)
        rec('')
        rec('  finite sides to n = %d ; Lambda_Q against b325\'s inversion : worst %.3e %s'
            % (N, lamq_diff, 'HOLDS' if lamq_diff <= AM.BAR_LAMQ else '### EXCEEDS ###'))
        rec("  THE SQUARE'S REACH, MEASURED : the frame's X = %g against a^2 = %g : NOT REACHED -- the square and the remainder are NOT evaluated here"
            % (AM.FRAME_REF[1], WIDTH * WIDTH))
        for g, s, _e in charted:
            rec('')
            rec('  gamma = %.6f  width %g  seed %s  cond %.2e' % (g, WIDTH, s.name, s.cond))
            _f, r = AM.quantities(s, lam_z, lam_q, lamq_diff)
            r.update(gamma=g, a=WIDTH, seed=s.name, square='NOT REACHED', remainder='NOT REACHED')
            AM.print_quantities(r)
            out.append(r)
    else:
        rec('')
        rec('  ### ### **NO SEED SURVIVED BOTH CONDITIONS. ### NO HEIGHT IS CHARTED AND NO ROOM IS REPORTED.**')

    def relof(r):
        den = max(abs(float(r['arch_z'])), abs(float(r['prime_z'])))
        return abs(float(r['places_z'])) / den if den else float('nan')

    joint = sorted(out + prior_rows, key=lambda r: r['gamma'])
    rec('')
    rec('  ### THE EXTENDED GRID AT a = %g -- this act\'s charted heights and b344\'s together, ABSOLUTE AND RELATIVE:' % WIDTH)
    rec('  %-9s %-7s %17s %17s %15s %14s %9s %6s' % ('gamma', 'from', 'A_z', 'PR_z', 'room_z', 'R_rel', 'gate', 'sign'))
    for r in joint:
        rec('  %-9.4f %-7s %+17.9f %+17.9f %+15.9f %14.6e %9s %6s'
            % (r['gamma'], 'b349' if r['gamma'] < 1.0 else 'b344', r['arch_z'], r['prime_z'], r['room_z'],
               relof(r), r['gate']['places_z']['verdict'], r['gate']['places_z']['sign']))
    signs = [(r['gamma'], r['gate']['places_z']['sign'], r['room_z']) for r in joint if r['gate']['places_z']['sign'] in ('+', '-')]
    refused = [r['gamma'] for r in joint if r['gate']['places_z']['sign'] not in ('+', '-')]
    pairs = [(signs[i][0], signs[i + 1][0]) for i in range(len(signs) - 1) if signs[i][1] != signs[i + 1][1]]
    negative = [g for g, sg, v in signs if v < 0]
    lo_abs = min(joint, key=lambda r: r['room_z'])
    lo_rel = min(joint, key=relof)
    ia = [r['gamma'] for r in joint].index(lo_abs['gamma'])
    ir = [r['gamma'] for r in joint].index(lo_rel['gamma'])
    int_a, int_r = 0 < ia < len(joint) - 1, 0 < ir < len(joint) - 1
    rec('')
    if pairs or negative:
        verdict = 'A CROSSING, LOCATED at a = %g' % WIDTH
        rec('  ### ### **A CROSSING, LOCATED at a = %g : adjacent pairs %s ; heights with a negative room %s**' % (WIDTH, pairs, negative))
    elif refused:
        verdict = 'REFUSED at a = %g' % WIDTH
        rec('  ### ### **REFUSED : the gate declines a sign at %s ; the question is left open there**' % refused)
    else:
        verdict = ('MINIMUM INTERIOR IN BOTH MEASURES' if (int_a and int_r) else
                   ('MINIMUM AT AN EDGE IN AT LEAST ONE MEASURE'))
        rec('  ### ### **NO CROSSING ON THE EXTENDED GRID. ### THE MINIMA:**')
        rec('  ###   ABSOLUTE : gamma = %.4f, room %+.9f -- %s' % (lo_abs['gamma'], lo_abs['room_z'], 'INTERIOR' if int_a else '### AT AN EDGE'))
        rec('  ###   RELATIVE : gamma = %.4f, R_rel %.6e -- %s' % (lo_rel['gamma'], relof(lo_rel), 'INTERIOR' if int_r else '### AT AN EDGE'))
        if int_a:
            rec('  ###   the absolute minimum\'s neighbours : %+.9f at gamma = %.4f and %+.9f at gamma = %.4f, both larger'
                % (joint[ia - 1]['room_z'], joint[ia - 1]['gamma'], joint[ia + 1]['room_z'], joint[ia + 1]['gamma']))
    rec('')
    rec('  ### **AND WHAT IS NOT CLAIMED: NO CROSSING IS CLAIMED AT ANY HEIGHT, AND A NARROWER ROOM AT A LOWER')
    rec('  ### HEIGHT IS A LOWER HEIGHT AND NOT A TREND.** ### The square and the remainder are NOT reached at')
    rec('  ### this width, and nothing here bears on totality.')
    rec('  ### wall %.0f s' % (time.time() - t0))
    rec('=' * 100)
    p = run_clock.write(D, 'b349_extend_run', LINES)
    io.open(os.path.join(D, 'b349_extend.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(width=WIDTH, extension=list(EXTEND), window=[LO, HI], seeds=seeds,
             charted=[g for g, _s, _e in charted], degenerate=[g for g, _s, _e in degenerate],
             rows=out, verdict=verdict, min_abs=dict(gamma=lo_abs['gamma'], room=lo_abs['room_z'], interior=bool(int_a)),
             min_rel=dict(gamma=lo_rel['gamma'], rel=relof(lo_rel), interior=bool(int_r)),
             crossing_pairs=pairs, negative=negative, refused=refused,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  ### run file : %s ; its clock : %s' % (os.path.basename(p), run_clock.read_stamp(p)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
