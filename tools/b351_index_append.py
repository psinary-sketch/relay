# -*- coding: utf-8 -*-
"""b351_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTSHAPED`.** ### A reader who asks *what the partition question
### settled* must be handed: UNDECIDED; a bound on the INSTRUMENT is not a bound on the COORDINATE; two closed
### coordinates are not half a classification; and the record contains neither a finite classification nor a proof
### that there is none. ### **`the plane has a shape`, `no finite partition exists`, `the height is bounded` AND
### `the classes are named` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b351_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
P = json.load(io.open(os.path.join(D, 'b351_read.json'), encoding='utf-8'))

Q = chr(34)
BS = chr(92)
APOS = BS + "'"

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'aim-plane-coordinates': ['the aim plane', 'the partition question', 'the abscissa', 'the height',\n"
    "                             'the phase window', 'the seed" + APOS + "s width', 'a finite classification',\n"
    "                             'a bound on the instrument'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")

ROW_NEW = (
    "    # ### THE PARTITION QUESTION (b351).\n"
    "    (" + Q + "aim-plane-coordinates" + Q + ", " + Q + "b351 (a read under a ceiling; it computes nothing)" + Q + ",\n"
    "     " + Q + "THE AIM PLANE" + APOS + "S COORDINATES READ FOR WHETHER THE RECORD CAN BOUND THEM, under the sealed distinction that A BOUND ON THE INSTRUMENT IS NOT A" + Q + "\n"
    "     " + Q + " BOUND ON THE COORDINATE. THE ABSCISSA: BOUNDED BY AN ARGUMENT -- b326" + APOS + "s summed bound SUM r_Q(k) k^(-3/2) = 1.38 < 2 confines every zero of" + Q + "\n"
    "     " + Q + " Lambda_Q to (-0.5, 1.5), a statement about ALL zeros, banked since the completeness census and never cited for the aim plane. THE SEED" + APOS + "S PHASE:" + Q + "\n"
    "     " + Q + " BOUNDED BY AN ARGUMENT and finitely cut -- for an EVEN seed the quadruple" + APOS + "s term is 4 G^2 cos(2 phi), the coordinate lives on a circle, and the" + Q + "\n"
    "     " + Q + " sign cuts it at exactly 45 and 135 degrees; ONE class survives, the vanishing transform, which the sign condition cannot see. THE HEIGHT: BOUNDED" + Q + "\n"
    "     " + Q + " ONLY BY A MEASUREMENT -- sixty boxes over t in [0.5, 150], the count closing at 180 against a main term of 178.6, and nothing claimed above it;" + Q + "\n"
    "     " + Q + " AND ITS ONLY METHOD PRODUCES INSTANCES WHOSE COUNT THE MAIN TERM SAYS NEVER RUN OUT, so the price of " + ('%.5f' % P['boxes_per_unit']) + " boxes per unit of height" + Q + "\n"
    "     " + Q + " (" + str(P['boxes_to_T300']) + " further boxes to T = 300, in boxes because the record printed no wall) BUYS INSTANCES WHILE THE MISSING STATEMENT NEEDS A CLASS. THE SEED" + APOS + "S" + Q + "\n"
    "     " + Q + " WIDTH: NOT BOUNDED, and worse off than the height -- the square and remainder are NOT REACHED at the charted widths, the remainder evaluator" + Q + "\n"
    "     " + Q + " changes sign past rho = 100, and for Z_Q the record" + APOS + "s own words are NOT AN INSTRUMENT THE RECORD HAS, so its missing statement is UNPRICEABLE" + Q + "\n"
    "     " + Q + " from banked figures and its pricing unpriceable too. VERDICT: UNDECIDED, both other branches SHOWN UNREACHABLE." + Q + ",\n"
    "     " + Q + "### UNDECIDED IS A STATEMENT ABOUT THE RECORD AND NOT ABOUT THE OBJECT: the aim plane may well admit a finite classification, and this act says" + Q + "\n"
    "     " + Q + " only that the record contains neither one nor a proof that there is none. ### NO PARTITION WAS CONSTRUCTED, NO CLASS PROVED SILENT, NO INSTRUMENT" + Q + "\n"
    "     " + Q + " WRITTEN, and nothing computed beyond one labelled division of two banked counts. ### A COORDINATE BEING BOUNDED IS NOT THE MARGIN BEING SAFE" + Q + "\n"
    "     " + Q + " THERE, and no margin was measured at any aim. ### TWO CLOSED COORDINATES ARE NOT HALF A CLASSIFICATION, because a classification of a product is" + Q + "\n"
    "     " + Q + " not two classifications of two factors. ### THE PHASE" + APOS + "S FINITE CUT IS STATED FOR AN EVEN SEED, the condition b328 states it under. ### NO CLASS" + Q + "\n"
    "     " + Q + " IS DISCHARGED. ### THE CLAUSE HAS NOT MOVED. ### NO GRADE MOVED. ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b351_the_partition_question.txt; data/b351_read_run.txt; data/b351_extract_notes2.txt;" + Q + "\n"
    "     " + Q + " data/b351_registration_2026-09-07.txt (sealed before one coordinate was judged);" + Q + "\n"
    "     " + Q + " CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('the aim plane', 'the partition question', 'the abscissa', 'the height',
           'the phase window', "the seed's width", 'a finite classification',
           'a bound on the instrument')
MUST_NOT_HIT = ('the plane has a shape', 'no finite partition exists',
                'the height is bounded', 'the classes are named')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b351 -- THE INDEX KEY. ### THE PARTITION QUESTION.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-44s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'aim-plane-coordinates'" in txt)
    have_row = ('"aim-plane-coordinates"' in txt)
    print('  aim-plane-coordinates key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('aim-plane-coordinates')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : aim-plane-coordinates returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'aim-plane-coordinates' in o
        ok = ok and g
        print('    %-44s reaches the b351 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTSHAPED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'UNDECIDED' in out and 'NOT ABOUT THE OBJECT' in out
    a2 = 'A BOUND ON THE INSTRUMENT IS NOT A' in out
    a3 = 'NOT HALF A CLASSIFICATION' in out
    a4 = 'NO PARTITION WAS CONSTRUCTED, NO CLASS PROVED SILENT' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3 and a4
    print('    the answer says UNDECIDED, and that it is about the record       : %s' % a1)
    print('    ### and that a bound on the instrument is not one on the coord   : %s' % a2)
    print('    ### and that two closed coordinates are not half a classification: %s' % a3)
    print('    ### and that nothing was constructed or silenced, no grade moved : %s' % a4)
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
