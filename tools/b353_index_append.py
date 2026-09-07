# -*- coding: utf-8 -*-
"""b353_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTCLOSED`.** ### A reader who asks *what the read settled*
### must be handed: a statement EXISTS and is pinned; it is an exhaustion at every width and NOT an exhaustion
### across widths; the width coordinate is NOT closed and the partition stays UNDECIDED; and the absence of a
### crossing statement is AN ABSENCE OF READING. ### **`the width is closed`, `the class is spanned`, `the
### partition is decided` AND `the literature carries no such statement` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b353_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
P = json.load(io.open(os.path.join(D, 'b353_read.json'), encoding='utf-8'))
SRC = P['source']

Q = chr(34)
BS = chr(92)
APOS = BS + "'"

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'width-missing-statement': ['the width coordinate', 'the missing statement', 'Boas-Kac',\n"
    "                               'the admissible class', 'the test function class', 'a density statement',\n"
    "                               'the spanning subfamily', 'exhaustion across widths'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")

ROW_NEW = (
    "    # ### THE WIDTH COORDINATE'S MISSING STATEMENT (b353).\n"
    "    (" + Q + "width-missing-statement" + Q + ", " + Q + "b353 (a read under the import bar and a pricing; it computes nothing)" + Q + ",\n"
    "     " + Q + "A STATEMENT EXISTS, AND IT DOES NOT CLOSE THE WIDTH COORDINATE. It is in the corpus" + APOS + "s OWN source -- arXiv " + SRC['arxiv'] + ", Connes-Consani, Weil" + Q + "\n"
    "     " + Q + " positivity and Trace formula the archimedean place, pinned at sha256 " + SRC['sha256'][:32] + "..., " + str(SRC['bytes']) + " bytes, graded" + Q + "\n"
    "     " + Q + " " + SRC['grade'] + ". ITS PROPOSITION 2, BOAS-KAC: for f in Cc^infty(R) supported in [-A, A], pointwise positivity of the Fourier transform is" + Q + "\n"
    "     " + Q + " EQUIVALENT to f = g conv g-star for some g supported in [-A/2, A/2]. THAT IS STRONGER THAN THE DENSITY STATEMENT THE ORDER ASKED FOR -- it" + Q + "\n"
    "     " + Q + " EXHAUSTS the admissible class rather than approximating it -- AND EVERY CONCLUSION IT GIVES IS AT THE SAME A IT WAS GIVEN, while the criterion" + Q + "\n"
    "     " + Q + " it serves quantifies over the union of ALL supports. SO AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS. The hypotheses" + Q + "\n"
    "     " + Q + " graded TWICE and never merged: against the source" + APOS + "s class all four are MET; against the corpus" + APOS + "s constructed objects H1 (smoothness) is" + Q + "\n"
    "     " + Q + " REFUTABLE -- the record" + APOS + "s own word for its test functions is PIECEWISE LINEAR -- H3 (pointwise positivity) is UNDECIDABLE FROM THE RECORD" + Q + "\n"
    "     " + Q + " because the corpus" + APOS + "s test is a scan and says so itself, and H4 (the vanishing conditions) is MET ONLY TO A MEASURED TOLERANCE. The missing" + Q + "\n"
    "     " + Q + " statement is typed and is UNPRICEABLE from banked figures, because the work it names is a proof and not a run." + Q + ",\n"
    "     " + Q + "### A LOCATED STATEMENT IS NOT A PROVED ONE, AND A CHECKED HYPOTHESIS IS NOT A DISCHARGED OBLIGATION. ### THE WIDTH COORDINATE IS NOT CLOSED BY" + Q + "\n"
    "     " + Q + " THIS ACT, no class is proved or spanned, and the partition b351 left UNDECIDED STAYS UNDECIDED. ### H1 BEING REFUTABLE AGAINST THE ARRAYS IS" + Q + "\n"
    "     " + Q + " NOT A FINDING THAT THE CORPUS" + APOS + "S RESULTS ARE WRONG: it is a finding that the record does not say what its arrays are meant to be, and that" + Q + "\n"
    "     " + Q + " question is routed and not answered. ### THE SEARCH IS NOT A SURVEY -- one source was read at content, and the absence of a crossing statement" + Q + "\n"
    "     " + Q + " is AN ABSENCE OF READING AND NOT AN ABSENCE OF LITERATURE. ### NO CLASS IS DISCHARGED. ### THE CLAUSE HAS NOT MOVED. ### NO GRADE MOVED. ###" + Q + "\n"
    "     " + Q + " NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b353_the_missing_statement.txt; data/b353_read_run.txt; data/b353_extract_notes.txt;" + Q + "\n"
    "     " + Q + " data/b353_source.json (the pin and the search); data/b353_registration_2026-09-07.txt" + Q + "\n"
    "     " + Q + " (sealed before one hypothesis was graded); CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('the width coordinate', 'the missing statement', 'Boas-Kac', 'the admissible class',
           'the test function class', 'a density statement', 'the spanning subfamily',
           'exhaustion across widths')
MUST_NOT_HIT = ('the width is closed', 'the class is spanned',
                'the partition is decided', 'the literature carries no such statement')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print("b353 -- THE INDEX KEY. ### THE WIDTH COORDINATE'S MISSING STATEMENT.")
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-44s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'width-missing-statement'" in txt)
    have_row = ('"width-missing-statement"' in txt)
    print('  width-missing-statement key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('width-missing-statement')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : width-missing-statement returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'width-missing-statement' in o
        ok = ok and g
        print('    %-44s reaches the b353 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTCLOSED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A LOCATED STATEMENT IS NOT A PROVED ONE' in out
    a2 = 'NOT AN EXHAUSTION ACROSS WIDTHS' in out
    a3 = 'THE WIDTH COORDINATE IS NOT CLOSED BY' in out and 'STAYS UNDECIDED' in out
    a4 = 'ABSENCE OF READING AND NOT AN ABSENCE OF LITERATURE' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3 and a4
    print('    the answer says a located statement is not a proved one       : %s' % a1)
    print('    ### and an exhaustion at every width is not one across widths  : %s' % a2)
    print('    ### and the width is NOT closed, the partition stays UNDECIDED : %s' % a3)
    print('    ### and the absence is an absence of READING, and no grade moved: %s' % a4)
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
