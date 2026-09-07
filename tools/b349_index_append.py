# -*- coding: utf-8 -*-
"""b349_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTEXPLAINED`.** ### A reader who asks *what the relative room
### settles* must be handed: one measure agreeing with another is WEAKER than either being right; NO CROSSING is
### claimed at any height; a narrower room at a lower height is a lower height and NOT A TREND; three lawful seeds
### mean these three did not degenerate and NOT that the construction never does; and the square and the remainder
### are NOT REACHED at this width. ### **`the room closes`, `a crossing is near`, `the construction never
### degenerates` AND `the relative measure is the right one` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b349_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
R = json.load(io.open(os.path.join(D, 'b349_relative.json'), encoding='utf-8'))
E = json.load(io.open(os.path.join(D, 'b349_extend.json'), encoding='utf-8'))
F40, F81 = R['flatness']['40.0'], R['flatness']['81.0']

Q = chr(34)
BS = chr(92)
APOS = BS + "'"


def s(x):
    return str(x)


KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'room-relative': ['the room', 'the relative room', 'the room relative', 'the point of maximum tension',\n"
    "                      'the shared normaliser', 'the extended height grid', 'the phase window',\n"
    "                      'a degenerate seed'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")

ROW_NEW = (
    "    # ### THE ROOM, RELATIVE BEFORE EXTENDED (b349).\n"
    "    (" + Q + "room-relative" + Q + ", " + Q + "b349 (a second measure of banked figures, then three new heights)" + Q + ",\n"
    "     " + Q + "THE ROOM MEASURED RELATIVE TO THE TERMS IT SITS BETWEEN, the denominator fixed before any value as the LARGER of the two terms so the ratio cannot be" + Q + "\n"
    "     " + Q + " inflated by a small one. On the " + s(len(R['table'])) + " aims already charted, reading and running no seed: THE MINIMUM SURVIVES AT BOTH WIDTHS -- absolute and relative" + Q + "\n"
    "     " + Q + " minima both at gamma = 2.5 at a = 40, and both at gamma = 1.25 at a = 81 -- SO THE LOCATED POINT OF MAXIMUM TENSION IS NOT AN ARTIFACT OF ABSOLUTE" + Q + "\n"
    "     " + Q + " MEASUREMENT. And the relative measure IS FLATTER at both widths (" + ('%.0f' % F40['absolute']) + " against " + ('%.0f' % F40['relative']) + " at a = 40; " + ('%.0f' % F81['absolute']) + " against " + ('%.0f' % F81['relative']) + " at a = 81)," + Q + "\n"
    "     " + Q + " so the navigator" + APOS + "s expectation is half met and half refuted and the halves point opposite ways. PART (b) THEREFORE RAN: three sealed heights at" + Q + "\n"
    "     " + Q + " a = 81, every seed checked for lawfulness by the source" + APOS + "s Definition 3.1 AND for its phase inside b328" + APOS + "s WINDOW of 45 to 135 degrees --" + Q + "\n"
    "     " + Q + " ALL THREE LAWFUL, ALL THREE IN THE WINDOW, NONE DEGENERATE. NO CROSSING on the extended grid, and the minimum stays at gamma = 1.25, INTERIOR IN" + Q + "\n"
    "     " + Q + " BOTH MEASURES. The sortie" + APOS + "s step zero also built tools/quote_norm.py, one normaliser imported by both sides of every quotation comparison, over" + Q + "\n"
    "     " + Q + " the species banked at b298, b309 and b348." + Q + ",\n"
    "     " + Q + "### ONE MEASURE AGREEING WITH ANOTHER IS WEAKER THAN EITHER BEING RIGHT, and the relative measure is a DIFFERENT measure and not a better one." + Q + "\n"
    "     " + Q + " ### NO CROSSING IS CLAIMED AT ANY HEIGHT. ### A NARROWER ROOM AT A LOWER HEIGHT IS A LOWER HEIGHT AND NOT A TREND: below gamma = 1 the room moves" + Q + "\n"
    "     " + Q + " very little across three heights while the dip at 1.25 sits an order of magnitude under all of them, a local feature and not a descent. ### THREE" + Q + "\n"
    "     " + Q + " LAWFUL SEEDS MEAN THESE THREE DID NOT DEGENERATE; THEY DO NOT MEAN THE CONSTRUCTION NEVER DOES. ### THE SQUARE AND THE REMAINDER ARE NOT REACHED" + Q + "\n"
    "     " + Q + " AT THIS WIDTH. ### THE ORDER NAMED A b305 INCIDENT THIS SEAT COULD NOT LOCATE AND NONE WAS MANUFACTURED. ### NO GRADE MOVED. ### NO BAR MOVED." + Q + "\n"
    "     " + Q + " ### NO TERMINAL. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b349_the_room_relative.txt; data/b349_relative_run.txt; data/b349_extend_run.txt;" + Q + "\n"
    "     " + Q + " data/b349_registration_2026-09-07.txt (sealed before one relative value was computed and before any new seed);" + Q + "\n"
    "     " + Q + " tools/quote_norm.py (the sortie" + APOS + "s shared normaliser); CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('the room', 'the relative room', 'the room relative', 'the point of maximum tension',
           'the shared normaliser', 'the extended height grid', 'the phase window', 'a degenerate seed')
MUST_NOT_HIT = ('the room closes', 'a crossing is near', 'the construction never degenerates',
                'the relative measure is the right one')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print("b349 -- THE INDEX KEY. ### THE ROOM, RELATIVE BEFORE EXTENDED.")
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'room-relative'" in txt)
    have_row = ('"room-relative"' in txt)
    print('  room-relative key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('room-relative')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : room-relative returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'room-relative' in o
        ok = ok and g
        print('    %-44s reaches the b349 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTEXPLAINED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'WEAKER THAN EITHER BEING RIGHT' in out and 'NO CROSSING IS CLAIMED AT ANY HEIGHT' in out
    a2 = 'NOT A TREND' in out and 'a local feature and not a descent' in out
    a3 = 'THEY DO NOT MEAN THE CONSTRUCTION NEVER DOES' in out and 'NOT REACHED' in out
    a4 = 'NONE WAS MANUFACTURED' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3 and a4
    print('    the answer says one measure agreeing is weaker, and no crossing is claimed : %s' % a1)
    print('    ### and a lower room at a lower height is not a trend                       : %s' % a2)
    print('    ### and three lawful seeds do not settle the construction                   : %s' % a3)
    print('    ### and nothing was manufactured, and no grade moved                        : %s' % a4)
    post = {}
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        post[q] = no_key(o)
        g = pre[q] and post[q]
        ok = ok and g
        print('    %-40s NO KEY after  : %s  %s' % (q, post[q], 'PASS' if g else '### FAIL ###'))
    print('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
