# -*- coding: utf-8 -*-
"""b336_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTAGRADE`.** ### A reader who asks *what would it cost to move a
### face* must be handed the census -- the types, the priced rows, the sorted view -- with the sentence that a cost
### is not a grade, not a plan, not a prediction, and that no grade moved. ### The row count and the row number
### are read from the run files at write time. ### **`a grade moved` AND `the price predicts` STAY UNKEYED.**
"""
import io
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

CORR = io.open(os.path.join(D, 'b336_corr_run.txt'), encoding='utf-8').read()
ROWNUM = re.search(r'last row number is (\d+)', CORR).group(1)
RUN = io.open(os.path.join(D, 'b336_cost_run.txt'), encoding='utf-8').read()
NROWS = re.search(r'rows typed (\d+)', RUN).group(1)
PRICED = re.search(r'rows the record prices : \[(.*?)\]', RUN).group(1).replace("'", '')

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'cost-census': ['the cost census', 'cost census', 'the cost column', 'the typed cost column', 'what moving it one grade would take',\n"
    "                    'what would it cost to move a face', 'the sorted view', 'the pole-constant relation', 'the pole-constant row', 'row L2',\n"
    "                    'the phase rule refined', '45 to 135 degrees', 'the addendum to b328'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE COST CENSUS (b336, leg 1 of the sortie b335-b338).\n"
    "    (\"cost-census\", \"b336 (a census on the faces ledger, typed; no grade moved)\",\n"
    "     \"THE COST CENSUS: for each of the faces ledger's rows, what moving it ONE grade would take, typed as READ / IMPORT / MEASUREMENT /\"\n"
    "     \" DERIVATION / CONSTRUCTION (cheapest kind first) with the record's price quoted at its emitter where the record prices the step -- " + NROWS + " rows\"\n"
    "     \" typed, the rows the record prices " + PRICED + " (the unit's domain factor 3.104e+02 at b322; the exponent's ratio, a twenty-fourth to a fifth, at b321;\"\n"
    "     \" the instrument's six acts at b321_run; the crossing widths at b328 and b334), every other row 'no price in the record'; filed as an append-only\"\n"
    "     \" block keyed to the row ids through the writer, the sorted view at relay data/b336_cost_sorted.txt. ROW L2, the pole-constant relation between the\"\n"
    "     \" Li and positivity faces: the deposit's archimedean channel on the Li family is the archimedean distribution plus the pole constant 1, the two\"\n"
    "     \" margins two evaluations of one distribution and not one functional (FINDINGS), separated by the pole constant (b331) -- STATED, cost zero. THE ADDENDUM TO b328's BLOCK: the quadruple's term\"\n"
    "     \" 4 |G|^2 cos 2 phi is negative only between 45 and 135 degrees, b334's chart sign column cited.\",\n"
    "     \"### NO GRADE MOVED; every existing row byte-identical. ### A COST IS NOT A GRADE, NOT A PLAN, NOT A PREDICTION. ### NO TERMINAL. ### M-2 UNCHANGED\",\n"
    "     \"data/b336_the_cost_census.txt; data/b336_cost_run.txt; data/b336_cost_sorted.txt; data/b336_registration_2026-09-06.txt (sealed before any write);\"\n"
    "     \" FACES_LEDGER.md (the b336 cost census block; row L2; the b336 addendum to b328); CORRESPONDENCE.md row " + ROWNUM + "\"),\n"
)

ALIASES = ('the cost census', 'cost census', 'the cost column', 'what moving it one grade would take', 'what would it cost to move a face',
           'the pole-constant relation', 'row L2', 'the phase rule refined', 'the addendum to b328')
MUST_NOT_HIT = ('a grade moved', 'the price predicts', 'the housekeeping')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b336 -- THE INDEX KEY. ### THE COST CENSUS.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'cost-census'" in txt)
    have_row = ('"cost-census"' in txt)
    print('  cost-census    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('cost-census')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : cost-census returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'cost-census' in o
        ok = ok and g
        print('    %-40s reaches the b336 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTAGRADE -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'NO GRADE MOVED' in out
    a2 = 'A COST IS NOT A GRADE, NOT A PLAN, NOT A PREDICTION' in out
    a3 = 'STATED, cost zero' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says no grade moved                       : %s' % a1)
    print('    ### and that a cost is not a grade, plan or prediction : %s' % a2)
    print('    ### and that L2 is STATED, cost zero                   : %s' % a3)
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
