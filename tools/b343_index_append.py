# -*- coding: utf-8 -*-
"""b343_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTAPROOF`.** ### A reader who asks *does the room cross* must be handed
### the chart with the sentences that a finer chart is a finer chart, that the reaching widths are outside the square's
### and the remainder's reach, and that the frames establish only that the grid at fixed domain is not the floor's
### origin -- the floor's other candidates untouched. ### **`the room cannot cross` AND `the floor explained` STAY
### UNKEYED.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
PATH = os.path.join(ROOT, 'tools', 'banked_index.py')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CORR = io.open(os.path.join(D, 'b343_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
CJ = json.load(io.open(os.path.join(D, 'b343_crossing.json'), encoding='utf-8'))
FJ = json.load(io.open(os.path.join(D, 'b343_frames.json'), encoding='utf-8'))
FR = FJ['frames']
NAR = ' ; '.join('a = %s narrowest at gamma = %.2f, %+.9f' % (a, CJ['per_width'][a]['narrowest']['gamma'], CJ['per_width'][a]['narrowest']['room_z']) for a in sorted(CJ['per_width'], key=float))
FLOOR = ("the residual is unchanged across two doublings of N at fixed domain and rank, so THE GRID RESOLUTION AT FIXED DOMAIN IS NOT THE ORIGIN OF b339's FLOOR and the floor's other candidates are untouched"
         if FJ['unchanged'] else "the residual changed across the doublings and NOTHING is concluded about b339's floor")

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'map-next-reach': ['the map\\'s next reach', 'the finer grid', 'the finer chart', 'the narrowest room', 'the crossing', 'does the room cross',\n"
    "                       'the residual against the frame', 'the square\\'s rank', 'the identity residual', 'the grid axis', 'the floor\\'s origin'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE MAP'S NEXT REACH (b343, leg 5 of the sortie b339-b343).\n"
    "    (\"map-next-reach\", \"b343 (a chart at a finer grid, and a measurement of the instrument at three frames)\",\n"
    "     \"THE MAP'S NEXT REACH: the aim-map's quantities at thirteen heights from gamma = 2.0 to 8.0 in half-unit steps, at both reaching widths a = 40 and\"\n"
    "     \" a = 81, by b334's own code imported and not edited, the noise-floor gate on every sign -- " + CJ['verdict'] + " (" + NAR + ");\"\n"
    "     \" the two heights shared with b334's coarse grid reproduce its banked values to " + ('%.3e' % CJ['shared_worst']) + ". AND THE IDENTITY RESIDUAL AT ONE AIMED SEED\"\n"
    "     \" (a = 1.41, gamma = 33.650101) across the reference frame and the two larger grid-axis frames, N = " + str([r['frame'][0] for r in FR]) + " at fixed X = 32 and NY = 512,\"\n"
    "     \" the remainder under both conventions each named: the stable-cut rank " + (('constant at %d' % FR[0]['rank']) if FJ['rank_constant'] else 'moved') + ", and " + FLOOR + ".\",\n"
    "     \"### A FINER CHART IS A FINER CHART. ### THE REACHING WIDTHS ARE OUTSIDE THE SQUARE'S AND THE EPS EVALUATOR'S REACH, AND NEITHER WAS EVALUATED\"\n"
    "     \" THERE. ### THE DRAFT'S EXPECTATION THAT THE RESIDUAL GROWS WITH RANK CANNOT BE SCORED ON THE AXIS IT NAMES, WHICH HOLDS THE RANK FIXED.\"\n"
    "     \" ### NO GRADE MOVED; K6 STAYS MEASURED-AT-COVERED-CELLS. ### NO TERMINAL. ### M-2 UNCHANGED\",\n"
    "     \"data/b343_the_maps_next_reach.txt; data/b343_fine_40_run.txt; data/b343_fine_81_run.txt; data/b343_crossing_run.txt; data/b343_frames_run.txt;\"\n"
    "     \" data/b343_registration_2026-09-06.txt (sealed before any seed at a new height); FACES_LEDGER.md (the b343 update, row S1/K6);\"\n"
    "     \" CORRESPONDENCE.md row " + R1 + "\"),\n"
)

ALIASES = ("the map's next reach", 'the finer grid', 'the finer chart', 'the narrowest room', 'the crossing', 'does the room cross',
           'the residual against the frame', 'the identity residual', "the floor's origin")
MUST_NOT_HIT = ('the room cannot cross', 'the floor explained', 'the residual grows with rank')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print("b343 -- THE INDEX KEY. ### THE MAP'S NEXT REACH.")
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'map-next-reach'" in txt)
    have_row = ('"map-next-reach"' in txt)
    print('  map-next-reach    key/row already present : %s / %s' % (have_key, have_row))
    written = not (have_key and have_row)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file.')
        return 2
    if written:
        new = txt
        if not have_key:
            new = new.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW, 1)
        if not have_row:
            new = new.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW, 1)
        open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(PATH + '.tmp', PATH)
    else:
        print('  ### NOTHING WRITTEN. (idempotent) ### **THE READ-BACK ARMS STILL RUN.**')
    ok = True
    out, rc = query('map-next-reach')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : map-next-reach returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'map-next-reach' in o
        ok = ok and g
        print('    %-44s reaches the b343 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTAPROOF -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A FINER CHART IS A FINER CHART' in out
    a2 = "OUTSIDE THE SQUARE'S AND THE EPS EVALUATOR'S REACH" in out
    a3 = 'NO GRADE MOVED; K6 STAYS MEASURED-AT-COVERED-CELLS' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says a finer chart is a finer chart          : %s' % a1)
    print('    ### and the reaching widths are outside both reaches     : %s' % a2)
    print('    ### and no grade moved, K6 where it was                  : %s' % a3)
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        quiet = no_key(o)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s' % (q, quiet, pre[q], 'PASS' if good else '### FAIL ###'))
    import ferry_scan
    _c, sh = ferry_scan.scan_text(io.open(PATH, encoding='utf-8').read(), [], ferry_scan.stems())
    print('  ### THE INDEX SWEPT AFTER THE WRITE : %d stem hit(s)' % len(sh))
    ok = ok and not sh
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
