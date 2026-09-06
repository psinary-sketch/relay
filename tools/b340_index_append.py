# -*- coding: utf-8 -*-
"""b340_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTTHEOBJECT`.** ### A reader who asks *did the Li family control hold* must be
### handed the control at its archimedean constituent with the sentences that it certifies the instrument and not the object,
### that the Li family is not in the lawful class and the Sonin margin is not defined on it, and that the zero side and the
### finite side stay owed. ### Every number is read from the control record at write time.
### ### **`the li family lawful` AND `the sonin margin on the li family` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b340_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
J = json.load(io.open(os.path.join(D, 'b340_control.json'), encoding='utf-8'))
VERDICT = ('A FOURTH CONTROL AT ITS ARCHIMEDEAN CONSTITUENT: the bar holds at all %d tabulated indices with the pole constant carried' % len(J['indices'])) if J['holds_all'] \
    else ('THE DIFFERING CONSTITUENT: the bar fails at %d of %d tabulated indices' % (len(J['indices']) - J['n_hold'], len(J['indices'])))

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'li-family-control': ['the li family control', 'the fourth control', 'did the li family control hold', 'the li test functions',\n"
    "                          'the archimedean distribution on the li family', 'the archimedean channel of the li coefficient', 'the balance keystone',\n"
    "                          'the lagarias identification', 'finite-range positivity', 'the li family lawfulness', 'w-ord-li-family-control'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE LI FAMILY CONTROL (b340, leg 2 of the sortie b339-b343).\n"
    "    (\"li-family-control\", \"b340 (a control at one constituent, on a family outside the lawful class)\",\n"
    "     \"THE LI FAMILY CONTROL: the Li test functions built from the pinned source's (3.2) in the corpus's half-line normalization, NOT in the lawful\"\n"
    "     \" class (three of three of Theorem 1's conditions failing, the applicable and inapplicable certifications stated); the archimedean distribution on\"\n"
    "     \" them by the derived kernel, I(n) = (1/2pi) INT Re G_n(1/2+iu) h_+(u) du, two quadratures gated by the noise floor, at the balance keystone's\"\n"
    "     \" indices, against the deposit's channel lambda_A(n) by the bench's own definitions with the pole constant carried as its own column and b327's\"\n"
    "     \" identity lambda_A = S_inf + 1 as the bar; worst |I + 1 - lambda_A| = " + J['worst_miss'] + ", worst drift " + J['worst_drift'] + ". " + VERDICT + ".\"\n"
    "     \" The finite-range positivity restated at its scope beside the values (the certificate the deposit's, its premises open).\",\n"
    "     \"### A CONTROL CERTIFIES THE INSTRUMENT, NOT THE OBJECT. ### THE LI FAMILY IS NOT IN THE LAWFUL CLASS; THE SONIN MARGIN IS NOT DEFINED ON IT.\"\n"
    "     \" ### THE ZERO SIDE AND THE FINITE SIDE STAY OWED (W-ORD-LI-FAMILY-CONTROL). ### NO GRADE MOVED. ### NO TERMINAL. ### M-2 UNCHANGED\",\n"
    "     \"data/b340_the_li_family_control.txt; data/b340_control_run*.txt; data/b340_control.json; data/b340_registration_2026-09-06.txt (sealed before the\"\n"
    "     \" instrument); FACES_LEDGER.md (the b340 update, row L1 and the pair F1-L1); CORRESPONDENCE.md row " + R1 + "\"),\n"
)

ALIASES = ('the li family control', 'the fourth control', 'did the li family control hold', 'the li test functions', 'the balance keystone',
           'the lagarias identification', 'finite-range positivity', 'the archimedean channel of the li coefficient')
MUST_NOT_HIT = ('the li family lawful', 'the sonin margin on the li family', 'lambda_n positive for all n')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b340 -- THE INDEX KEY. ### THE LI FAMILY CONTROL.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'li-family-control'" in txt)
    have_row = ('"li-family-control"' in txt)
    print('  li-family-control    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('li-family-control')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : li-family-control returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'li-family-control' in o
        ok = ok and g
        print('    %-44s reaches the b340 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTTHEOBJECT -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A CONTROL CERTIFIES THE INSTRUMENT, NOT THE OBJECT' in out
    a2 = 'NOT IN THE LAWFUL CLASS; THE SONIN MARGIN IS NOT DEFINED ON IT' in out
    a3 = 'THE ZERO SIDE AND THE FINITE SIDE STAY OWED' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says a control certifies the instrument, not the object : %s' % a1)
    print('    ### and not in the lawful class, no Sonin margin on it                : %s' % a2)
    print('    ### and the zero side and the finite side stay owed, no grade moved   : %s' % a3)
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
