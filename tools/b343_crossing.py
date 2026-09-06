# -*- coding: utf-8 -*-
"""b343_crossing.py -- THE CROSSING, BY THE SEALED RULE, AND THE TWO HEIGHTS SHARED WITH b334's COARSE GRID.

### ### **THE RULE, FROM THE SEALED REGISTRATION, SECTION (C):** a crossing is a pair of adjacent heights on this grid
### at one width whose certified `A_z - PR_z` signs differ, or a single height whose certified sign is positive. ### The
### verdict is ### **NO CROSSING ON THIS GRID** (with the narrowest height and value named), ### **A CROSSING, LOCATED**,
### or ### **REFUSED** (the gate declines a sign at a height, and the question is left open there). ### **(F3):** at
### `gamma = 4` and `gamma = 8`, both widths, this act's values are set against b334's banked values with the
### difference printed; a difference above `1e-12` relative is reported at full prominence.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

WIDTHS = (40.0, 81.0)
SHARED = (4.0, 8.0)
BAR_SHARED = 1e-12
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def main():
    rec('=' * 100)
    rec("b343 -- THE CROSSING, BY THE SEALED RULE; AND THE TWO HEIGHTS SHARED WITH b334's COARSE GRID.")
    rec('=' * 100)
    fine = {a: json.load(io.open(os.path.join(D, 'b343_fine_%g.json' % a), encoding='utf-8')) for a in WIDTHS}
    b334 = {a: json.load(io.open(os.path.join(D, 'b334_leg_reaching_%g.json' % a), encoding='utf-8')) for a in WIDTHS}
    out = {}
    verdicts, refused_any, crossings = [], [], []
    for a in WIDTHS:
        rows = sorted(fine[a]['rows'], key=lambda r: r['gamma'])
        rec('')
        rec('  ### a = %g : %d heights, %s' % (a, len(rows), [r['gamma'] for r in rows]))
        rec('  %-10s %18s %18s %18s %10s %10s' % ('gamma', 'A_z', 'PR_z', 'room_z = A_z - PR_z', 'gate', 'sign'))
        signs, refused = [], []
        for r in rows:
            gz = r['gate']['places_z']
            rec('  %-10.6f %+18.9f %+18.9f %+18.9f %10s %10s' % (r['gamma'], r['arch_z'], r['prime_z'], r['room_z'], gz['verdict'], gz['sign']))
            if gz['sign'] in ('+', '-'):
                signs.append((r['gamma'], gz['sign'], r['room_z']))
            else:
                refused.append(r['gamma'])
        # ### the sealed rule: adjacent certified signs differing, or a certified POSITIVE room (b334 prints the room's
        # ### sign as the places side's, so a POSITIVE VALUE of A_z - PR_z carries the sign '-'; a crossing is a change).
        pairs = [(signs[i][0], signs[i + 1][0]) for i in range(len(signs) - 1) if signs[i][1] != signs[i + 1][1]]
        pos = [g for g, s, v in signs if v < 0]
        narrow = min(((r['room_z'], r['gamma']) for r in rows), key=lambda x: x[0])
        rec('  ### the narrowest room at a = %g : gamma = %.6f, A_z - PR_z = %+.9f' % (a, narrow[1], narrow[0]))
        rec('  ### certified signs at %d of %d heights ; the gate refused at %s' % (len(signs), len(rows), refused if refused else 'no height'))
        if pairs or pos:
            rec('  ### ### **A CROSSING, LOCATED at a = %g : adjacent pairs %s ; heights with a negative room %s**' % (a, pairs, pos))
            crossings.append((a, pairs, pos))
            verdicts.append('A CROSSING, LOCATED at a = %g' % a)
        elif refused:
            rec('  ### ### **REFUSED at a = %g : the gate declines a sign at %s ; the crossing question is left open there**' % (a, refused))
            refused_any.append((a, refused))
            verdicts.append('REFUSED at a = %g' % a)
        else:
            rec('  ### ### **NO CROSSING ON THIS GRID at a = %g** ; every height certified, the room positive in value at all %d' % (a, len(rows)))
            verdicts.append('NO CROSSING at a = %g' % a)
        out[str(a)] = dict(rows=[dict(gamma=r['gamma'], arch_z=r['arch_z'], prime_z=r['prime_z'], room_z=r['room_z'],
                                      verdict=r['gate']['places_z']['verdict'], sign=r['gate']['places_z']['sign']) for r in rows],
                           narrowest=dict(gamma=narrow[1], room_z=narrow[0]), refused=refused, pairs=pairs, negative_rooms=pos)
    # ### (F3) the shared heights against b334's bank
    rec('')
    rec("  ### (F3) THE TWO HEIGHTS SHARED WITH b334's COARSE GRID -- this act's values against its banked ones:")
    rec('  %-6s %-10s %20s %20s %12s' % ('a', 'gamma', 'this act A_z - PR_z', "b334's A_z - PR_z", 'relative'))
    worst = 0.0
    shared = []
    for a in WIDTHS:
        by = {round(r['gamma'], 6): r for r in fine[a]['rows']}
        old = {round(r['gamma'], 6): r for r in b334[a]['rows']}
        for g in SHARED:
            n, o = by.get(round(g, 6)), old.get(round(g, 6))
            if not n or not o:
                rec('  %-6g %-10.6f  ### ONE SIDE ABSENT' % (a, g))
                continue
            rel = abs(n['room_z'] - o['room_z']) / max(abs(o['room_z']), 1e-300)
            worst = max(worst, rel)
            rec('  %-6g %-10.6f %+20.9f %+20.9f %12.3e%s' % (a, g, n['room_z'], o['room_z'], rel, '   ### **ABOVE THE BAR**' if rel > BAR_SHARED else ''))
            shared.append(dict(a=a, gamma=g, mine=n['room_z'], b334=o['room_z'], rel=rel))
    rec('  ### worst relative difference at the shared heights : %.3e (bar %.0e) : %s' % (worst, BAR_SHARED, 'AGREE' if worst <= BAR_SHARED else '### DIFFER ###'))
    verdict = ' ; '.join(verdicts)
    rec('')
    rec('  ### ### **THE VERDICT ON THE FINER GRID : %s.**' % verdict)
    rec('  ### A FINER CHART IS A FINER CHART. ### The square and the remainder are NOT REACHED at these widths and were not evaluated.')
    rec('=' * 100)
    p, k = os.path.join(D, 'b343_crossing_run.txt'), 1
    while os.path.exists(p):
        k += 1
        p = os.path.join(D, 'b343_crossing_run%d.txt' % k)
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    io.open(os.path.join(D, 'b343_crossing.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(widths=list(WIDTHS), grid=fine[WIDTHS[0]]['grid'], per_width=out, shared=shared, shared_worst=worst,
                        verdict=verdict, any_crossing=bool(crossings), any_refused=bool(refused_any), run_file=os.path.basename(p)), indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
