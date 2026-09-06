# -*- coding: utf-8 -*-
"""b344_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTEXPLAINED`.** ### A reader who asks *what is the floor's origin* must
### be handed one axis moved, with the sentences that one axis moved is one axis moved, that nothing is concluded about
### the two held, that the repaired seal certifies nothing about acts sealed before it, and that a narrower room at a
### finer grid is a finer chart and not a trend. ### **`the floor explained`, `the taper exonerated` AND `the seal
### recovers b342` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b344_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
N = json.load(io.open(os.path.join(D, 'b344_ny.json'), encoding='utf-8'))
S = json.load(io.open(os.path.join(D, 'b344_seal_clock.json'), encoding='utf-8'))
M = json.load(io.open(os.path.join(D, 'b344_module.json'), encoding='utf-8'))
E = json.load(io.open(os.path.join(D, 'b344_edge.json'), encoding='utf-8'))

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'floor-priced': ['the floor priced', 'the floor\\'s origin', 'what is the floor\\'s origin', 'the NY axis', 'the ny ladder',\n"
    "                     'the seal\\'s clock', 'the seal\\'s own time', 'the seal carries its clock', 'the room\\'s edge', 'the bracketed minimum',\n"
    "                     'the cut\\'s tau', 'the taper', 'the axes held'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE FLOOR PRICED, THE SEAL'S OWN CLOCK, AND THE ROOM'S EDGE (b344).\n"
    "    (\"floor-priced\", \"b344 (one axis of three moved; a tool repair; a chart extended)\",\n"
    "     \"THE FLOOR PRICED ON ONE AXIS: of the three origins b339 named for the identity residual's floor -- the fixed NY, the cut's tau, the taper -- NY was\"\n"
    "     \" moved over the ladder " + str(N['ladder']) + " at the reference frame, the other two HELD AND PRINTED at every rung. The stable-cut rank is CONSTANT at\"\n"
    "     \" " + str(N['ranks'][0]) + " across the whole ladder, so NY does not move the rank. The residual MOVES with NY: the span across the ladder is " + ('%.3e' % N['span_abs_EF']) + " against\"\n"
    "     \" b339's floor of " + ('%+.9f' % N['floor']) + " at that cell, so by the sealed rule the movement is " + N['size'] + ". Beside the verdict and labelled: the increments fall\"\n"
    "     \" by a factor near four, so the residual converges in NY, and from the corpus's own NY = 512 the remaining travel is about a ninth of the floor.\"\n"
    "     \" THE SEAL'S OWN CLOCK: reg_seal.py repaired by the order's words to record the seal's UTC instant inside the block, additions-only, with all\"\n"
    "     \" " + str(S['sealed_before']) + " existing seals verifying identically before and after and none rewritten; filed as modules/2026-09/SEAL_CARRIES_ITS_CLOCK.md,\"\n"
    "     \" committed locally at " + str(M['committed']) + ", the remote unmoved, NOT PUSHED. THE ROOM'S EDGE: the grid extended below b343's edge at a = 81 only --\"\n"
    "     \" BRACKETED, the minimum interior at gamma = " + ('%.2f' % E['minimum']['gamma']) + ", room " + ('%+.9f' % E['minimum']['room_z']) + ", no crossing on the seventeen-height grid.\",\n"
    "     \"### ONE AXIS MOVED IS ONE AXIS MOVED: NOTHING IS CONCLUDED ABOUT THE TWO AXES HELD, AND THE FLOOR IS NOT EXPLAINED. ### A REPAIRED SEAL TOOL\"\n"
    "     \" CERTIFIES NOTHING ABOUT THE ACTS SEALED BEFORE IT, AND IT DOES NOT RECOVER b342's LOST TIMESTAMP. ### THE CLOCK IS OUTSIDE THE HASH AND SAYS SO.\"\n"
    "     \" ### A NARROWER ROOM AT A FINER GRID IS A FINER CHART AND NOT A TREND. ### NO GRADE MOVED. ### NO TERMINAL. ### M-2 UNCHANGED\",\n"
    "     \"data/b344_the_floor_priced.txt; data/b344_ny_run.txt; data/b344_edge_run.txt; data/b344_seal_after_run.txt; data/b344_module_run.txt;\"\n"
    "     \" data/b344_registration_2026-09-06.txt (sealed before any rung, before the tool was touched, and before any seed below the edge);\"\n"
    "     \" data/b344_ruling_2026-09-06.txt (this act's number); TECHNE-Core modules/2026-09/SEAL_CARRIES_ITS_CLOCK.md (local);\"\n"
    "     \" CORRESPONDENCE.md row " + R1 + "\"),\n"
)

ALIASES = ('the floor priced', "the floor's origin", "what is the floor's origin", 'the NY axis', "the seal's clock",
           'the seal carries its clock', "the room's edge", 'the axes held', 'the taper')
MUST_NOT_HIT = ('the floor explained', 'the taper exonerated', 'the seal recovers b342')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print("b344 -- THE INDEX KEY. ### THE FLOOR PRICED, THE SEAL'S OWN CLOCK, AND THE ROOM'S EDGE.")
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'floor-priced'" in txt)
    have_row = ('"floor-priced"' in txt)
    print('  floor-priced    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('floor-priced')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : floor-priced returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'floor-priced' in o
        ok = ok and g
        print('    %-44s reaches the b344 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTEXPLAINED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'ONE AXIS MOVED IS ONE AXIS MOVED' in out and 'THE FLOOR IS NOT EXPLAINED' in out
    a2 = "CERTIFIES NOTHING ABOUT THE ACTS SEALED BEFORE IT" in out and "DOES NOT RECOVER b342's LOST TIMESTAMP" in out
    a3 = 'A FINER CHART AND NOT A TREND' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says one axis moved, the floor not explained  : %s' % a1)
    print('    ### and the seal reaches nothing behind it                : %s' % a2)
    print('    ### and a finer chart is not a trend, no grade moved      : %s' % a3)
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
