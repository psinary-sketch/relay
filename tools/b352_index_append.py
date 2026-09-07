# -*- coding: utf-8 -*-
"""b352_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTMEASURED`.** ### A reader who asks *what the refit settled*
### must be handed: UNDER-RESOLVED AS A FIT; a model winning a selection score is not a floor existing; the three
### cells disagree and at five points the criterion is mostly counting parameters; and the smallest floor any arm
### could have seen is printed. ### **`the floor is established`, `the floor is refuted`, `b339 is corrected` AND
### `the side-reading is withdrawn` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b352_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
P = json.load(io.open(os.path.join(D, 'b352_fit.json'), encoding='utf-8'))
pc = P['per_cell']

Q = chr(34)
BS = chr(92)
APOS = BS + "'"

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'floor-fourth-candidate': ['the floor as a fit', 'the fourth candidate', 'the three models',\n"
    "                              'the model selection', 'a floor or a power law', 'the frame price',\n"
    "                              'the straddling gate', 'the spectral void'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")

ROW_NEW = (
    "    # ### THE FLOOR'S FOURTH CANDIDATE (b352).\n"
    "    (" + Q + "floor-fourth-candidate" + Q + ", " + Q + "b352 (a refit of banked figures; nothing recomputed)" + Q + ",\n"
    "     " + Q + "THE IDENTITY RESIDUAL REFITTED UNDER THREE MODELS SEALED BEFORE ANY FIT -- M1 = A X^-p (k=2), M2 = A X^-p + c (k=3), M3 = A X^-p + B X^-(p+1) (k=3) --" + Q + "\n"
    "     " + Q + " all by ONE criterion, least squares on log R, with M1 reproducing b322" + APOS + "s own fit_power at every cell to 1e-9 (the fitter IMPORTED) so that the" + Q + "\n"
    "     " + Q + " three scores are comparable. VERDICT: THE FLOOR IS UNDER-RESOLVED AS A FIT. The five frames DO separate a constant floor from a faster-decaying" + Q + "\n"
    "     " + Q + " correction -- M2 beats M3 at every cell -- but M2 against M1 is preferred at a = 1.3 by less than the bar, decisively at a = 1.35, and REJECTED at" + Q + "\n"
    "     " + Q + " a = 1.41 by 7.01. AND THE REASON IS THE CRITERION AND NOT THE DATA: at n = 5 a third parameter costs 20 AICc units against a bar of 2, so S must" + Q + "\n"
    "     " + Q + " fall by a factor of 54.6 to break even and the winner turns on the penalty. The fitted constant is POSITIVE at all three cells and passes the" + Q + "\n"
    "     " + Q + " second bar at all three, refuting the seat" + APOS + "s registered expectation. THE PRICE OF SETTLING IT IS ONE MORE FRAME: the binding cell needs 6 where" + Q + "\n"
    "     " + Q + " the record holds 5, the next rung is X = 256, N = 32768, AND THAT SITS INSIDE THE CEILING b339 SEALED AT X = 512 -- affordable where b339" + APOS + "s own" + Q + "\n"
    "     " + Q + " question was not. Component 3 filed the spectral void" + APOS + "s width as the MEASURED " + str(10.62) + " with b350 named, and minted the straddling-gate rule." + Q + ",\n"
    "     " + Q + "### A MODEL WINNING A SELECTION SCORE IS NOT A FLOOR EXISTING: a fit ranks descriptions of five numbers and measures nothing. ### WHAT THIS ACT" + Q + "\n"
    "     " + Q + " COULD NOT HAVE SEEN IS PRINTED PER CELL -- a true floor below the fit" + APOS + "s own scatter at the last rung would pass no arm here. ### NO ACT IS" + Q + "\n"
    "     " + Q + " RE-VERDICTED: b339" + APOS + "s UNAFFORDABLE STANDS, b346 stands, b350 stands, b351" + APOS + "s UNDECIDED stands. ### b339" + APOS + "S SIDE-READING IS RESTATED AS FIT-DEPENDENT" + Q + "\n"
    "     " + Q + " AND IS NOT WITHDRAWN -- its own act labelled it that seat" + APOS + "s reading. ### THE FRAME PRICE IS A PRICE AND NOT A PREDICTION, and the act does not" + Q + "\n"
    "     " + Q + " run it. ### NO CLASS IS DISCHARGED. ### THE CLAUSE HAS NOT MOVED. ### NO GRADE MOVED. ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b352_the_fourth_candidate.txt; data/b352_fit_run6.txt; data/b352_filings_run.txt;" + Q + "\n"
    "     " + Q + " data/b352_registration_2026-09-07.txt (sealed before one model was fitted);" + Q + "\n"
    "     " + Q + " PLACE-papers OPEN_TRAILS.md (the W-ORD-VOID-WIDTH block); TECHNE-Core STRADDLING_GATE.md (local-only);" + Q + "\n"
    "     " + Q + " tools/registration_gate.py (the straddle arm, appended); CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('the floor as a fit', 'the fourth candidate', 'the three models', 'the model selection',
           'a floor or a power law', 'the frame price', 'the straddling gate', 'the spectral void')
MUST_NOT_HIT = ('the floor is established', 'the floor is refuted',
                'b339 is corrected', 'the side-reading is withdrawn')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print("b352 -- THE INDEX KEY. ### THE FLOOR'S FOURTH CANDIDATE.")
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-44s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'floor-fourth-candidate'" in txt)
    have_row = ('"floor-fourth-candidate"' in txt)
    print('  floor-fourth-candidate key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('floor-fourth-candidate')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : floor-fourth-candidate returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'floor-fourth-candidate' in o
        ok = ok and g
        print('    %-44s reaches the b352 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTMEASURED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'NOT A FLOOR EXISTING' in out and 'measures nothing' in out
    a2 = 'UNDER-RESOLVED AS A FIT' in out and 'THE CRITERION AND NOT THE DATA' in out
    a3 = 'COULD NOT HAVE SEEN IS PRINTED PER CELL' in out
    a4 = 'IS NOT WITHDRAWN' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3 and a4
    print('    the answer says a score is not a floor, and a fit measures nothing : %s' % a1)
    print('    ### and under-resolved, for the criterion and not the data          : %s' % a2)
    print('    ### and what the act could not have seen is printed                 : %s' % a3)
    print("    ### and b339's side-reading is not withdrawn, and no grade moved    : %s" % a4)
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
