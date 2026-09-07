# -*- coding: utf-8 -*-
"""b356_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTCONVERGED`.** ### A reader who asks *what the raised axis
### settled* must be handed: THE BOUNDARY; two points on an axis are NOT a convergence; b354 is not
### re-verdicted and named its own ambiguity; the raised frame is comparable to b354's sixth rung and to
### nothing else; and a sign that returns under one raise is not a sign that is safe.
### ### **`the residual is positive`, `the floor is confirmed`, `b354 was wrong` AND `the ladder continues`
### STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b356_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
R = json.load(io.open(os.path.join(D, 'b356_raised.json'), encoding='utf-8'))

Q = chr(34)
BS = chr(92)
APOS = BS + "'"

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'object-or-boundary': ['the object or the boundary', 'the raised axis', 'the quadrature bound',\n"
    "                          'the instrument edge', 'the sixth rung again', 'six dimensions',\n"
    "                          'the rank at the bound', 'the control at the raised axis'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")

ROW_NEW = (
    "    # ### THE OBJECT OR THE BOUNDARY (b356).\n"
    "    (" + Q + "object-or-boundary" + Q + ", " + Q + "b356 (one frame, one parameter re-tuned, deliberately)" + Q + ",\n"
    "     " + Q + "THE BOUNDARY. b354 found the sixth rung" + APOS + "s residual negative AND the rank saturated at the quadrature bound IN THE SAME STEP, and separated" + Q + "\n"
    "     " + Q + " them nowhere. b356 raises NY from 512 to 1024 -- a value the record had already used, being a rung of b344" + APOS + "s own ladder -- with nothing else" + Q + "\n"
    "     " + Q + " moved. THE CONTROL RAN FIRST AND LICENSED EVERYTHING ELSE: the FIFTH rung under the raised axis has rank 262 EXACTLY as banked and its trace" + Q + "\n"
    "     " + Q + " reproduces b320 to 4.895e-04 worst against a bar of 1e-3 whose floor is b344" + APOS + "s own measured 9.753e-05 move of THIS axis over EXACTLY this step" + Q + "\n"
    "     " + Q + " -- the observed move being 5.02 times that floor, so a bar set AT the floor would have failed on a correct computation. THE RANK AT THE RAISED" + Q + "\n"
    "     " + Q + " AXIS IS 518 AGAINST A BOUND OF 1024, where b354 measured 512 against 512 and extrapolated to about 516: THE EXTRAPOLATION WAS ACCURATE TO TWO." + Q + "\n"
    "     " + Q + " AND THE RESIDUAL RETURNS POSITIVE AT EVERY COVERED CELL: -2.760e-04 becomes +1.085e-02, -2.215e-04 becomes +9.723e-03, -1.686e-04 becomes" + Q + "\n"
    "     " + Q + " +8.801e-03. SO b354" + APOS + "S SIXTH RUNG WAS THE INSTRUMENT" + APOS + "S EDGE, AND THE FIVE-FRAME PICTURE STANDS WITH ITS EDGE NOW LOCATED AT X = 256 WITH" + Q + "\n"
    "     " + Q + " NY = 512. AND SIX DIMENSIONS DECIDED THE SIGN: the cut needs 518 and at NY = 512 it got 512, and the six it could not have turned +1.08e-02" + Q + "\n"
    "     " + Q + " into -2.76e-04 -- a change larger than the residual itself, from ONE PART IN EIGHTY-SIX of the cut. The run took " + ('%.1f' % R['wall']) + " s against a chosen" + Q + "\n"
    "     " + Q + " ceiling of " + ('%.0f' % R['wall_ceiling']) + " s." + Q + ",\n"
    "     " + Q + "### TWO POINTS ON AN AXIS ARE NOT A CONVERGENCE, AND THIS ACT HAS TWO: nothing here says the residual is positive in the limit, and b344" + APOS + "s own" + Q + "\n"
    "     " + Q + " ladder shows the trace still moving at NY = 2048. ### A SIGN THAT RETURNS UNDER ONE RAISE IS NOT A SIGN THAT IS SAFE. ### b354 IS NOT" + Q + "\n"
    "     " + Q + " RE-VERDICTED -- it named its own ambiguity, could not have resolved it, and its figures stand exactly as banked and are used here. ### THE" + Q + "\n"
    "     " + Q + " RAISED FRAME IS COMPARABLE TO b354" + APOS + "S SIXTH RUNG AND TO NOTHING ELSE: comparing it to the banked fifth-rung residual moves TWO parameters at" + Q + "\n"
    "     " + Q + " once, and the act refuses that comparison by name. ### b339" + APOS + "S SIDE-READING IS NOT WITHDRAWN -- b354" + APOS + "s evidence against it is removed here, so" + Q + "\n"
    "     " + Q + " it returns to where b339 left it, a reading its own act labelled, neither confirmed nor refuted. ### THE FLOOR QUESTION IS EXACTLY WHERE b352" + Q + "\n"
    "     " + Q + " LEFT IT: no fit was ordered and NO SCORE IS REPORTED. ### NO CLASS IS DISCHARGED. ### THE CLAUSE HAS NOT MOVED. ### NO GRADE MOVED. ### NO BAR" + Q + "\n"
    "     " + Q + " MOVED. ### NO TERMINAL. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b356_the_boundary.txt; data/b356_raised_run2.txt; data/b356_raised.json;" + Q + "\n"
    "     " + Q + " data/b356_axis.json (b344" + APOS + "s ladder, read for the bar" + APOS + "s floor);" + Q + "\n"
    "     " + Q + " data/b356_registration_2026-09-07.txt (sealed on the audit" + APOS + "s own exit code, before the instrument ran);" + Q + "\n"
    "     " + Q + " CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('the object or the boundary', 'the raised axis', 'the quadrature bound',
           'the instrument edge', 'the sixth rung again', 'six dimensions',
           'the rank at the bound', 'the control at the raised axis')
MUST_NOT_HIT = ('the residual is positive', 'the floor is confirmed',
                'b354 was wrong', 'the ladder continues')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b356 -- THE INDEX KEY. ### THE OBJECT OR THE BOUNDARY.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-44s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'object-or-boundary'" in txt)
    have_row = ('"object-or-boundary"' in txt)
    print('  object-or-boundary key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('object-or-boundary')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : object-or-boundary returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'object-or-boundary' in o
        ok = ok and g
        print('    %-44s reaches the b356 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTCONVERGED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'TWO POINTS ON AN AXIS ARE NOT A CONVERGENCE' in out and 'still moving at NY = 2048' in out
    a2 = 'NOT A SIGN THAT IS SAFE' in out
    a3 = 'b354 IS NOT' in out and 'RE-VERDICTED' in out and 'named its own ambiguity' in out
    a4 = 'AND TO NOTHING ELSE' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3 and a4
    print('    the answer says two points are not a convergence                : %s' % a1)
    print('    ### and that a sign returning once is not a sign that is safe    : %s' % a2)
    print('    ### and that b354 is not re-verdicted and named its own ambiguity: %s' % a3)
    print('    ### and that only one comparison is licensed, and no grade moved : %s' % a4)
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
