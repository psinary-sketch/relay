# -*- coding: utf-8 -*-
"""b337_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NODEPOSIT`.** ### A reader who asks *what did the housekeeping do* must
### be handed the fetch's agreement, the one drift and its appended repair, the partition, the local TECHNE commit
### and the receipts' statement -- with the sentences that nothing deposited, nothing was pushed, no entry moved, and
### nothing is concluded about the reply. ### The row number and the states are read from the run files at write time.
### ### **`the deposit moved`, `TECHNE pushed` AND `the reply filed` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b337_corr_run.txt'), encoding='utf-8').read()
ROWNUM = re.search(r'last row number is (\d+)', CORR).group(1)
F = json.load(io.open(os.path.join(D, 'b337_fetch.json'), encoding='utf-8'))
GOT = F['got']
HEAD = re.search(r'HEAD now (\w+)', io.open(os.path.join(D, 'b337_techne_run.txt'), encoding='utf-8').read()).group(1)

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'housekeeping': ['the housekeeping', 'the wave\\'s housekeeping', 'housekeeping', 'the errata partition', 'the partition of errata',\n"
    "                     'the deposit fetch', 'the read-only fetch', 'the three ledgers reconciled', 'the ledgers reconciled', 'the August TECHNE files',\n"
    "                     'the TECHNE commit', 'the patent receipts checked', 'what did the housekeeping do', 'the currency note'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE WAVE'S HOUSEKEEPING (b337, leg 2 of the sortie b335-b338).\n"
    "    (\"housekeeping\", \"b337 (housekeeping: filings and checks; no claim, no grade, no deposit action)\",\n"
    "     \"THE THREE LEDGERS (ERRATA.md, VERIFICATION_LOOM.md, OPEN_TRAILS.md) RECONCILED TO REGISTRY AGAINST ONE READ-ONLY FETCH of the public record\"\n"
    "     \" (" + GOT['version'] + ", published " + GOT['date'] + ", DOI " + GOT['doi'] + ", " + str(GOT['nfiles']) + " files): REGISTRY's d1-1 row agrees on every field, the local canonical copy matches the\"\n"
    "     \" published MD5s at " + str(F['local_match']) + " of " + str(F['local_total']) + "; the loom and the trails CURRENT; ERRATA's head (v1.1.1 as current) DRIFT, repaired by an APPENDED currency\"\n"
    "     \" note, the head not edited. THE ERRATA PARTITION per the author's ruling ratified by the sortie paste: one appended block, five entries\"\n"
    "     \" DEPOSIT-FACING and five INTERNAL-RECORD by their own words, entries unmoved. THE NINE AUGUST TECHNE MODULE FILES committed at " + HEAD + " in the\"\n"
    "     \" canonical local clone by explicit list, the remote unchanged, NOT PUSHED. THE PATENT RECEIPTS: ABSENT ON THE MOUNTED VOLUMES (C, D) for\"\n"
    "     \" both applications; F: not mounted this session; the four office notices and the 2026-08-30 response packages present; the repo of record\"\n"
    "     \" has no remote.\",\n"
    "     \"### NO DEPOSIT ACTION; NOTHING WAS WRITTEN AT ZENODO. ### NO ENTRY MOVED OR EDITED. ### TECHNE NOT PUSHED. ### NOTHING IS CONCLUDED ABOUT WHETHER\"\n"
    "     \" A REPLY WAS FILED. ### NO GRADE, NO CLAIM, NO TERMINAL. ### M-2 UNCHANGED\",\n"
    "     \"data/b337_the_housekeeping.txt; data/b337_fetch_run.txt; data/b337_record.json; data/b337_errata_run.txt; data/b337_techne_run.txt;\"\n"
    "     \" data/b337_receipts_run.txt; data/b337_registration_2026-09-06.txt (sealed before any tool); PLACE-papers ERRATA.md (the b337 partition block);\"\n"
    "     \" TECHNE-Core local commit " + HEAD + "; CORRESPONDENCE.md row " + ROWNUM + "\"),\n"
)

ALIASES = ('the housekeeping', 'the errata partition', 'the deposit fetch', 'the three ledgers reconciled', 'the August TECHNE files', 'the patent receipts checked',
           'what did the housekeeping do', 'the currency note')
MUST_NOT_HIT = ('the deposit moved', 'TECHNE pushed', 'the reply filed', 'the fold b331 to b334')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print("b337 -- THE INDEX KEY. ### THE WAVE'S HOUSEKEEPING.")
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'housekeeping'" in txt)
    have_row = ('"housekeeping"' in txt)
    print('  housekeeping    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('housekeeping')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : housekeeping returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'housekeeping' in o
        ok = ok and g
        print('    %-40s reaches the b337 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NODEPOSIT -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'NO DEPOSIT ACTION; NOTHING WAS WRITTEN AT ZENODO' in out
    a2 = 'TECHNE NOT PUSHED' in out
    a3 = 'NOTHING IS CONCLUDED ABOUT WHETHER' in out
    a4 = 'NO ENTRY MOVED OR EDITED' in out
    ok = ok and a1 and a2 and a3 and a4
    print('    the answer says no deposit action, nothing written at Zenodo : %s' % a1)
    print('    ### and TECHNE not pushed                                   : %s' % a2)
    print('    ### and nothing concluded about the reply                    : %s' % a3)
    print('    ### and no entry moved or edited                             : %s' % a4)
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
