# -*- coding: utf-8 -*-
"""b332_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTDISCHARGED`.** ### A reader who asks *what is the open
### clause* must be handed the statement WITH the words that it is not discharged, not weakened, not
### replaced, one face and not the compiled equivalence -- never a sentence that reads as a result. ###
### The ranking, the verdict and the row number are read from the run files at write time.
### ### **`the clause discharged` AND `the clause weakened` STAY UNKEYED.** ### The index is swept for
### stems after the write.
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

R = json.load(io.open(os.path.join(D, 'b332_statement_rows.json'), encoding='utf-8'))
CORR = io.open(os.path.join(D, 'b332_corr_run.txt'), encoding='utf-8').read()
ROWNUM = re.search(r'last row number is (\d+)', CORR).group(1)
RK = ', '.join('%s (%s)' % (k, g) for _o, k, _n, g, _re in R['ranking'])
TOP = R['ranking'][0]

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'clause-stated': ['the clause stated', 'clause stated', 'the open clause', 'the statement of the clause',\n"
    "                      'the positivity face', 'the fourth register realized', 'the E0 gate', 'the softest constituent',\n"
    "                      'the lawful class', 'the archimedean distribution', 'the compressed square', 'the aim-map',\n"
    "                      'what is the open clause', 'the constituents ranked'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE CLAUSE STATED (b332).\n"
    "    (\"clause-stated\", \"b332 (a statement act; no proof attempted)\",\n"
    "     \"(S) for every g in the source's class (Definition 3.1 with Proposition C.1's vanishing set; b328's seeds inside\"\n"
    "     \" it) the places sum of the explicit formula keeps the criterion's sign, SUM_v W_v(g conv g-bar^#) <= 0 -- the\"\n"
    "     \" positivity face's realized form, the deposit's refusal to compile the cross-register equivalences quoted\"\n"
    "     \" beside it. The places sum unfolded: the finite places' contribution (b310/b329), the prime sum (b306), the\"\n"
    "     \" archimedean distribution with its digamma witness (b315/b320), the compressed square plus the remainder that\"\n"
    "     \" is the margin (b318/b320/b321). THE E0 GATE HALTS AT K8, the quantifiers, UNOWNED. THE RANKING under the\"\n"
    "     \" sealed rule, softest first: " + RK + "\",\n"
    "     \"### NOT DISCHARGED, NOT WEAKENED, NOT REPLACED; ONE FACE AND NOT THE COMPILED EQUIVALENCE. ### Every grade its\"\n"
    "     \" owner's, none conferred. ### The navigator's registered expectation (the remainder softest): " + R['verdict'] + " --\"\n"
    "     \" the softest rank is " + TOP[1] + ", " + TOP[2] + ". ### The aim-map named as next, for the softest constituent;\"\n"
    "     \" neither it nor this act is the discharge. ### NO TERMINAL: analysis over an infinite class. ### M-2 UNCHANGED\",\n"
    "     \"D:/MY-DOwnloads/PLACE-papers/FINDINGS.md (anchor clause-stated); FACES_LEDGER.md row S1; the arc keystone's appended\"\n"
    "     \" line; data/b332_the_clause_stated.txt; data/b332_statement_rows.json; data/b332_registration_2026-09-06.txt\"\n"
    "     \" (sealed before any write); CORRESPONDENCE.md row " + ROWNUM + "\"),\n"
)

ALIASES = ('the clause stated', 'the open clause', 'the positivity face', 'the E0 gate', 'the softest constituent',
           'the aim-map', 'what is the open clause', 'the constituents ranked')
MUST_NOT_HIT = ('the clause discharged', 'the clause weakened')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b332 -- THE INDEX KEY. ### THE CLAUSE STATED.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'clause-stated'" in txt)
    have_row = ('"clause-stated"' in txt)
    print('  clause-stated    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('clause-stated')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : clause-stated returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'clause-stated' in o
        ok = ok and g
        print('    %-40s reaches the b332 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTDISCHARGED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'NOT DISCHARGED, NOT WEAKENED, NOT REPLACED' in out
    a2 = 'ONE FACE AND NOT THE COMPILED EQUIVALENCE' in out
    a3 = 'neither it nor this act is the discharge' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says not discharged, not weakened, not replaced : %s' % a1)
    print('    ### and one face, not the compiled equivalence               : %s' % a2)
    print('    ### and that neither next act is the discharge               : %s' % a3)
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
