# -*- coding: utf-8 -*-
"""b341_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTAMEASUREMENT`.** ### A reader who asks *which emitter carries the defect*
### must be handed the verdict with the sentences that no bench measurement changes, that no deposited artifact is
### affected, that no owner file is edited, and that the dictionary's name is not its provenance. ### Every number is
### read from the records at write time. ### **`the bench's measurements wrong` AND `the keystone wrong` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b341_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
J = json.load(io.open(os.path.join(D, 'b341_coefficients.json'), encoding='utf-8'))
t3, t5 = J['table']['3'], J['table']['5']

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'two-coefficients': ['the two coefficients', 'the li bench', 'the keiper dict', 'the keiper dictionary', 'the bench\\'s literature dictionary',\n"
    "                         'the third coefficient', 'the fifth coefficient', 'the transcription defect', 'keiper', 'the literature values',\n"
    "                         'which emitter carries the defect', 'e-2026-09-06-1', 'the bench versus the keystone'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE TWO COEFFICIENTS (b341, leg 3 of the sortie b339-b343).\n"
    "    (\"two-coefficients\", \"b341 (a transcription filed: two routes, the literature under the import bar, an internal-record erratum)\",\n"
    "     \"THE TWO COEFFICIENTS: " + J['verdict'] + " -- the bench's KEIPER dictionary reads " + t3['bench'] + " and " + t5['bench'] + " at n = 3, 5 where two routes\"\n"
    "     \" sharing no quadrature (the bench's own definitions; the Li map of log xi by Taylor differentiation) give " + t3['A'][:16] + " and " + t5['A'][:16] + "\"\n"
    "     \" (off by " + t3['bench_off'] + " and " + t5['bench_off'] + "); the balance keystone's literature column agrees with the routes to its printed digits; Keiper 1992\"\n"
    "     \" LOCATED under the import bar at n = 3 and agreeing with the keystone (his lambda_n / n), readings beside the rule at n = 5 (Keiper's split mantissa;\"\n"
    "     \" Coffey's six decimals) agreeing too; no located source agrees with the dictionary. Filed as E-2026-09-06-1, INTERNAL RECORD, appended after the\"\n"
    "     \" partition block; the owner files untouched; the navigator's (L3) MET.\",\n"
    "     \"### NO BENCH MEASUREMENT CHANGES (the dictionary enters no computation). ### NO DEPOSITED ARTIFACT IS AFFECTED. ### NO OWNER FILE IS EDITED.\"\n"
    "     \" ### THE DICTIONARY'S NAME IS NOT ITS PROVENANCE. ### NO GRADE MOVED. ### NO TERMINAL. ### M-2 UNCHANGED\",\n"
    "     \"data/b341_the_two_coefficients.txt; data/b341_coefficients_run2.txt; data/b341_locate_run3.txt; data/b341_source_text_*.txt; data/b341_registration_2026-09-06.txt\"\n"
    "     \" (sealed before any fetch); ERRATA.md (E-2026-09-06-1); CORRESPONDENCE.md row " + R1 + "\"),\n"
)

ALIASES = ('the two coefficients', 'the li bench', 'the keiper dict', "the bench's literature dictionary", 'the third coefficient', 'the transcription defect',
           'keiper', 'the literature values', 'which emitter carries the defect')
MUST_NOT_HIT = ("the bench's measurements wrong", 'the keystone wrong', 'the deposit affected')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b341 -- THE INDEX KEY. ### THE TWO COEFFICIENTS.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'two-coefficients'" in txt)
    have_row = ('"two-coefficients"' in txt)
    print('  two-coefficients    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('two-coefficients')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : two-coefficients returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'two-coefficients' in o
        ok = ok and g
        print('    %-44s reaches the b341 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTAMEASUREMENT -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'NO BENCH MEASUREMENT CHANGES' in out and 'NO DEPOSITED ARTIFACT IS AFFECTED' in out
    a2 = 'NO OWNER FILE IS EDITED' in out
    a3 = "THE DICTIONARY'S NAME IS NOT ITS PROVENANCE" in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says no measurement changes, no deposited artifact affected : %s' % a1)
    print('    ### and no owner file edited                                              : %s' % a2)
    print("    ### and the dictionary's name is not its provenance, no grade moved       : %s" % a3)
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
