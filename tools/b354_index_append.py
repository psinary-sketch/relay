# -*- coding: utf-8 -*-
"""b354_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTSEPARATED`.** ### A reader who asks *what the sixth frame
### settled* must be handed: the residual is negative AND the rank saturated AT THE SAME RUNG, and the act
### separates them nowhere; the instrument's own controls hold exactly there; no six-frame score exists because
### the sealed criterion is undefined on a negative residual; and b339's side-reading is NOT withdrawn.
### ### **`the residual crosses zero`, `the floor is gone`, `the instrument failed` AND `the criterion was
### replaced` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b354_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
S = json.load(io.open(os.path.join(D, 'b354_sixth.json'), encoding='utf-8'))

Q = chr(34)
BS = chr(92)
APOS = BS + "'"

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'sixth-frame': ['the sixth frame', 'the sixth rung', 'the domain ladder', 'the rank saturation',\n"
    "                   'the negative residual', 'the last rung', 'the chosen ceiling',\n"
    "                   'the criterion domain'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")

ROW_NEW = (
    "    # ### THE SIXTH FRAME (b354).\n"
    "    (" + Q + "sixth-frame" + Q + ", " + Q + "b354 (one new rung, on the existing instrument, nothing re-tuned)" + Q + ",\n"
    "     " + Q + "THE SIXTH RUNG OF THE DOMAIN LADDER, WHICH b352 PRICED AND DID NOT RUN, RUN AT (N, X, NY) = (32768, 256, 512). THE ARM THAT LICENSED IT FIRST: the" + Q + "\n"
    "     " + Q + " FIFTH rung recomputed reproduces b320" + APOS + "s banked values to 0.000e+00 RELATIVE at all three cells, and the sixth frame" + APOS + "s identity control is" + Q + "\n"
    "     " + Q + " 0.000e+00 against a bar of 1e-9 whose floor is dim*eps = 7.1e-12 -- SO THE SIXTH RUNG IS NOT A BROKEN COMPUTATION. AND ITS RESIDUAL IS NEGATIVE AT" + Q + "\n"
    "     " + Q + " EVERY COVERED CELL (-2.76e-04, -2.21e-04, -1.69e-04), where the five banked rungs had fallen by ratios 0.34, 0.37, 0.42, 0.49 approaching one" + Q + "\n"
    "     " + Q + " half: THE RESIDUAL DID NOT SETTLE ONTO A FLOOR, IT CROSSED ZERO. AND THE SIXTH RUNG IS ALSO THE FIRST AT WHICH THE RANK IS LIMITED BY NY RATHER" + Q + "\n"
    "     " + Q + " THAN BY X -- the banked ranks 20, 37, 69, 133, 262 extrapolate to about 516 and the observed rank is 512, which is NY exactly, short by about" + Q + "\n"
    "     " + Q + " four dimensions out of five hundred. SO THE SIGN CHANGE AND THE INSTRUMENT" + APOS + "S BOUNDARY ARRIVE IN THE SAME STEP. THE SEALED CRITERION IS UNDEFINED" + Q + "\n"
    "     " + Q + " THERE (log of a negative residual), so NO SIX-FRAME SCORE EXISTS AND NONE IS REPORTED; refitting FIVE frames reproduces b352" + APOS + "s banked scores to" + Q + "\n"
    "     " + Q + " 3e-12, so b352 is EXTENDED and not re-verdicted. The chosen ceiling was " + ('%.0f' % S['wall_ceiling']) + " s and the run took " + ('%.1f' % S['wall']) + " s, the FIRST MEASURED WALL" + Q + "\n"
    "     " + Q + " THIS LADDER HAS. VERDICT by the letter of the sealed condition: FLOOR UNDER-RESOLVED STILL, for a reason the branch did not anticipate." + Q + ",\n"
    "     " + Q + "### THE SIGN CHANGE AND THE RANK SATURATION HAPPEN AT THE SAME RUNG AND THIS ACT SEPARATES THEM NOWHERE: nothing here decides whether the object" + Q + "\n"
    "     " + Q + " crosses zero or whether the instrument stopped being able to say. ### THE INSTRUMENT DID NOT FAIL -- its own controls hold EXACTLY at that rung." + Q + "\n"
    "     " + Q + " ### A CRITERION THAT RETURNED NOTHING IS NOT A CRITERION THAT SAID SOMETHING, and it is TABLED, NOT EDITED: a linear-space fit would fit these" + Q + "\n"
    "     " + Q + " six numbers and would be A SECOND CRITERION chosen after seeing the first fail. ### b339" + APOS + "S SIDE-READING IS NOT WITHDRAWN -- its own act labelled" + Q + "\n"
    "     " + Q + " it a reading, and the evidence against it arrives exactly at the instrument" + APOS + "s boundary. ### THE SEALED BRANCH RULE HAS NO SLOT FOR A FIT THAT" + Q + "\n"
    "     " + Q + " DOES NOT EXIST, and that absence is filed and TABLED. ### NO CLASS IS DISCHARGED. ### THE CLAUSE HAS NOT MOVED. ### NO GRADE MOVED. ### NO BAR" + Q + "\n"
    "     " + Q + " MOVED. ### NO TERMINAL. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b354_the_sixth_frame.txt; data/b354_sixth_run3.txt; data/b354_sixth.json;" + Q + "\n"
    "     " + Q + " data/b354_sixth_run_first_nan_scores.txt (the run banked as it stood);" + Q + "\n"
    "     " + Q + " data/b354_registration_2026-09-07.txt (sealed before the instrument ran);" + Q + "\n"
    "     " + Q + " tools/anchor_from_file.py (the sortie" + APOS + "s step zero); CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('the sixth frame', 'the sixth rung', 'the domain ladder', 'the rank saturation',
           'the negative residual', 'the last rung', 'the chosen ceiling', 'the criterion domain')
MUST_NOT_HIT = ('the residual crosses zero', 'the floor is gone',
                'the instrument failed', 'the criterion was replaced')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b354 -- THE INDEX KEY. ### THE SIXTH FRAME.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-44s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'sixth-frame'" in txt)
    have_row = ('"sixth-frame"' in txt)
    print('  sixth-frame key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('sixth-frame')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : sixth-frame returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'sixth-frame' in o
        ok = ok and g
        print('    %-44s reaches the b354 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTSEPARATED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'SEPARATES THEM NOWHERE' in out and 'whether the instrument stopped being able to say' in out
    a2 = 'THE INSTRUMENT DID NOT FAIL' in out
    a3 = 'TABLED, NOT EDITED' in out and 'A SECOND CRITERION' in out
    a4 = 'SIDE-READING IS NOT WITHDRAWN' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3 and a4
    print('    the answer says the two are not separated                        : %s' % a1)
    print('    ### and that the instrument did not fail                          : %s' % a2)
    print('    ### and that the criterion is tabled, not replaced                : %s' % a3)
    print("    ### and that b339's side-reading is not withdrawn, no grade moved : %s" % a4)
    post = {}
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        post[q] = no_key(o)
        g = pre[q] and post[q]
        ok = ok and g
        print('    %-44s NO KEY after  : %s  %s' % (q, post[q], 'PASS' if g else '### FAIL ###'))
    print('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
