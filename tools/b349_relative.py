# -*- coding: utf-8 -*-
"""b349_relative.py -- PART (a): THE ROOM, MEASURED RELATIVE TO THE TERMS IT SITS BETWEEN.

### ### **NO SEED IS BUILT HERE AND NO BANKED FIGURE IS RECOMPUTED.** ### Every row is READ from the record
### that charted it: b334's two reaching legs, b343's two finer grids, b344's extension below the edge.
### ### **THE RATIO IS THE SEALED ONE AND NOTHING ELSE:** `R_rel = |places| / max(|arch|, |prime|)`, the same
### denominator at every aim, at both widths, on both sides.
### ### **AND THE FLOOR IS THE SEALED ONE:** a row whose noise-floor gate does not return `RESOLVED` on its
### `places` value is EXCLUDED from every minimum and is reported as excluded. ### A room below the gate's floor
### is not a small room; it is no measurement.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402
import noise_floor as NF  # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []

SOURCES = [
    ('b334', 'b334_leg_reaching_40.json'),
    ('b334', 'b334_leg_reaching_81.json'),
    ('b343', 'b343_fine_40.json'),
    ('b343', 'b343_fine_81.json'),
    ('b344', 'b344_edge.json'),
]


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def load(n):
    return json.load(io.open(os.path.join(D, n), encoding='utf-8'))


def rel(row, side):
    """### THE SEALED RATIO. ### `side` is 'z' or 'q'."""
    pl = abs(float(row['places_' + side]))
    den = max(abs(float(row['arch_' + side])), abs(float(row['prime_z' if side == 'z' else 'finite_q'])))
    return (pl / den) if den else float('nan'), pl, den


def main():
    rec('=' * 100)
    rec('b349 -- PART (a): THE ROOM, RELATIVE. ### the sealed ratio, on the aims already charted, no new seed.')
    rec('=' * 100)
    rows, seen = [], {}
    dupes = []
    for act, fn in SOURCES:
        try:
            J = load(fn)
        except OSError:
            rec('  ### %s NOT PRESENT -- skipped' % fn)
            continue
        for r in J.get('rows', []):
            key = (float(r['a']), float(r['gamma']))
            if key in seen:
                dupes.append((key, seen[key], act, r['places_z'], rows[seen[key]][ 'places_z']))
                continue
            seen[key] = len(rows)
            rr = dict(r)
            rr['_act'] = act
            rr['_src'] = fn
            rows.append(rr)
    rec('  rows read : %d ; duplicate aims (same width AND height) skipped : %d' % (len(rows), len(dupes)))
    for k, i, act, a_, b_ in dupes:
        rec('    ### DUPLICATE a=%g gamma=%g : first from %s (places_z %s) ; also in %s (places_z %s) -- counted once'
            % (k[0], k[1], rows[i]['_act'], b_, act, a_))
    rec('')
    rec('  THE SEALED RATIO : R_rel = |places| / max(|arch|, |prime|) ; the gate floor : %.16e' % NF.DEFAULT_FLOOR)
    rec('')
    rec('  %-5s %-8s %-6s %-14s %-14s %-13s %-11s %-14s %-13s %-11s'
        % ('a', 'gamma', 'act', '|places_z|', 'den_z', 'R_rel_z', 'gate_z', '|places_q|', 'R_rel_q', 'gate_q'))
    table, excluded = [], []
    for r in rows:
        rz, plz, dz = rel(r, 'z')
        rq, plq, dq = rel(r, 'q')
        gz = (r.get('gate') or {}).get('places_z', {}).get('verdict', '?')
        gq = (r.get('gate') or {}).get('places_q', {}).get('verdict', '?')
        ok_z, ok_q = (gz == NF.RESOLVED), (gq == NF.RESOLVED)
        if not ok_z:
            excluded.append((r['a'], r['gamma'], 'z', gz))
        if not ok_q:
            excluded.append((r['a'], r['gamma'], 'q', gq))
        rec('  %-5g %-8g %-6s %-14.6e %-14.6e %-13.6e %-11s %-14.6e %-13.6e %-11s'
            % (r['a'], r['gamma'], r['_act'], plz, dz, rz, gz, plq, rq, gq))
        table.append(dict(a=float(r['a']), gamma=float(r['gamma']), act=r['_act'], src=r['_src'],
                          places_z=plz, den_z=dz, rel_z=rz, gate_z=gz, ok_z=bool(ok_z),
                          places_q=plq, den_q=dq, rel_q=rq, gate_q=gq, ok_q=bool(ok_q),
                          arch_z=float(r['arch_z']), prime_z=float(r['prime_z']),
                          arch_z_route2=float(r.get('arch_z_route2', r['arch_z'])),
                          places_z_refined=float(r.get('places_z_refined', r['places_z']))))
    rec('    ### rows EXCLUDED by the sealed floor rule (gate not RESOLVED) : %d %s'
        % (len(excluded), excluded if excluded else ''))
    # ### the second route, carried as a printed spread and NOT as an arm (the registration says so)
    sp_arch = max(abs(t['arch_z'] - t['arch_z_route2']) for t in table)
    sp_pl = max(abs(t['places_z'] - abs(t['places_z_refined'])) for t in table)
    rec('    ### the acts\' OWN second route, carried as a printed spread and not as an arm of this act :')
    rec('    ###   worst |arch_z - arch_z_route2| = %.3e ; worst |places_z - places_z_refined| = %.3e' % (sp_arch, sp_pl))

    rec('')
    rec('  THE MINIMA, BY THE SEALED READING RULE, AT EACH WIDTH:')
    verdicts = {}
    for width in sorted({t['a'] for t in table}):
        at = [t for t in table if t['a'] == width and t['ok_z']]
        if not at:
            rec('    a = %-5g ### no gate-RESOLVED row -- no minimum' % width)
            continue
        amin = min(at, key=lambda x: x['places_z'])
        rmin = min(at, key=lambda x: x['rel_z'])
        same = (amin['gamma'] == rmin['gamma'])
        verdicts[width] = dict(abs_gamma=amin['gamma'], abs_val=amin['places_z'],
                               rel_gamma=rmin['gamma'], rel_val=rmin['rel_z'], same=bool(same),
                               n=len(at))
        rec('    a = %-5g rows %-3d ; ABSOLUTE minimum at gamma = %-7g (|places_z| %.6e) ; RELATIVE minimum at gamma = %-7g (R_rel %.6e) ; SAME AIM : %s'
            % (width, len(at), amin['gamma'], amin['places_z'], rmin['gamma'], rmin['rel_z'], same))
    rec('')
    rec('  THE FLATNESS, REPORTED WHETHER OR NOT THE MINIMUM MOVES (the sealed largest-to-smallest test):')
    flat = {}
    for width in sorted({t['a'] for t in table}):
        at = [t for t in table if t['a'] == width and t['ok_z']]
        if len(at) < 2:
            continue
        av = [x['places_z'] for x in at]
        rv = [x['rel_z'] for x in at]
        fa, fr = max(av) / min(av), max(rv) / min(rv)
        flat[width] = dict(absolute=fa, relative=fr, relative_flatter=bool(fr < fa))
        rec('    a = %-5g absolute largest/smallest = %-12.4f ; relative = %-12.4f ; ### the RELATIVE measure is %s'
            % (width, fa, fr, 'FLATTER' if fr < fa else ('NOT flatter' if fr > fa else 'EQUALLY flat')))

    # ### the desk's item lives at the width b344 extended: a = 81
    desk_w = 81.0
    v = verdicts.get(desk_w)
    rec('')
    rec('=' * 100)
    rec("  THE READING, BY THE SEALED RULE OF SECTION (D) AND NO OTHER.")
    rec('=' * 100)
    if v is None:
        rec('  ### ### **NO GATE-RESOLVED ROW AT THE DESK\'S WIDTH. ### NOTHING IS READ.**')
        survives = None
    else:
        survives = v['same']
        rec('    at the width the desk\'s item lives at (a = %g): the absolute minimum sits at gamma = %g and the'
            % (desk_w, v['abs_gamma']))
        rec('    relative minimum at gamma = %g.' % v['rel_gamma'])
        if survives:
            rec('')
            rec('  ### ### **THE MINIMUM SURVIVES THE RELATIVE MEASURE.** ### The located point of maximum tension')
            rec('  ### sits where it sat, in a measure that divides out the size of the terms the room is a')
            rec('  ### difference of. ### **THAT IS ONE MEASURE AGREEING WITH ANOTHER, WHICH IS WEAKER THAN EITHER')
            rec('  ### BEING RIGHT**, and the registration said so before the figures existed.')
            rec('  ### ### **SO PART (b) RUNS.**')
        else:
            rec('')
            rec('  ### ### ### **THE MINIMUM MOVES.**')
            rec('  ### ### ### **THE LOCATED POINT OF MAXIMUM TENSION WAS AN ARTIFACT OF ABSOLUTE MEASUREMENT.**')
            rec('  ### ### **SO PART (b) IS NOT RUN, AND THE DESK ITEM IS RESTATED RATHER THAN EXTENDED.**')
    rec('')
    rec('  ### NO SEED BUILT ; NO BANKED FIGURE RECOMPUTED ; NO AIM ADDED, REMOVED OR RE-ORDERED ; NO CROSSING CLAIMED.')
    rec('=' * 100)
    p = run_clock.write(D, 'b349_relative_run', LINES)
    io.open(os.path.join(D, 'b349_relative.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(table=table, verdicts={str(k): v for k, v in verdicts.items()},
             flatness={str(k): v for k, v in flat.items()}, excluded=excluded, duplicates=len(dupes),
             desk_width=desk_w, survives=survives, spread_arch=sp_arch, spread_places=sp_pl,
             floor=NF.DEFAULT_FLOOR, run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  ### run file : %s ; its clock : %s' % (os.path.basename(p), run_clock.read_stamp(p)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
