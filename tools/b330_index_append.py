# -*- coding: utf-8 -*-
"""b330_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-METHODONLY`.** ### A reader who asks *what did the
### extraction put into TECHNE* must be handed METHOD, NOT PUSHED, and the private-until-filed rule --
### never a sentence that reads as a result having moved. ### The row's numbers (the module count, the
### local hash, the remote tip, the correspondence row number) are read from the run files at write time.
### ### **`a result in TECHNE` AND `the techne push` STAY UNKEYED.** ### The index is swept for stems
### after the write.
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
import b330_correspondence as R  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REC = R.read_records()
CORR = io.open(os.path.join(D, 'b330_corr_run.txt'), encoding='utf-8').read()
ROWNUM = re.search(r'last row number is (\d+)', CORR).group(1)

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'techne-extraction': ['techne extraction', 'the techne extraction', 'the september extraction', 'techne modules',\n"
    "                          'the method modules', 'claim-shaped modules', 'the module families', 'modules/2026-09',\n"
    "                          'the patent note', 'line-ending hygiene', 'the vacuity taxonomy', 'the negative-control protocol'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE TECHNE EXTRACTION -- METHOD ONLY, NOT PUSHED (b330).\n"
    "    (\"techne-extraction\", \"b330 (filings of method into a private core; a hygiene fix at step zero)\",\n"
    "     \"" + str(REC['n']) + " claim-shaped method modules under modules/2026-09/ in the canonical local TECHNE clone (WHAT IT DOES,\"\n"
    "     \" WHEN IT APPLIES, WHAT IT REFUSES, PROVENANCE pulled from the emitting files), a top-level modules/INDEX.md\"\n"
    "     \" mapping each to a family (the August three, or VACUITY / REGISTRATION / READING / CERTIFICATION /\"\n"
    "     \" NEGATIVE_CONTROL named once) and cross-referencing the August module it extends or supersedes; the August\"\n"
    "     \" files untouched and still untracked; the local commit " + REC['head'] + " NOT PUSHED, the remote tip " + REC['remote'] + "\"\n"
    "     \" unchanged, the second clone " + REC['second'] + " untouched. ### At step zero: .gitattributes in the kernel repository\"\n"
    "     \" (SIDE 3cbe47c), the profile equal to its blob on raw bytes after the re-checkout\",\n"
    "     \"### METHOD, NOT A RESULT -- NOTHING ABOUT THE PROGRAMME'S OBJECTS ENTERS TECHNE (research-vocabulary sweep 0\"\n"
    "     \" hits). ### NOT PUSHED; TECHNE-Core PRIVATE UNTIL ITS PROVISIONALS ARE FILED. ### The patent note lives in the\"\n"
    "     \" bank and makes no legal claim. ### The two-clone divergence read, not resolved. ### NO GRADE MOVED; NO GRADE\"\n"
    "     \" CONFERRED. ### M-2 UNCHANGED\",\n"
    "     \"D:/MY-DOwnloads/TECHNE-Core/modules/2026-09/ (local); data/b330_the_techne_extraction.txt; data/b330_modules_check_run3.txt;\"\n"
    "     \" data/b330_techne_verify.txt; data/b330_eol_after.txt; data/b330_registration_2026-09-06.txt (sealed before any\"\n"
    "     \" write); CORRESPONDENCE.md row " + ROWNUM + "\"),\n"
)

ALIASES = ('the techne extraction', 'the september extraction', 'the method modules', 'the module families',
           'the patent note', 'line-ending hygiene', 'the vacuity taxonomy', 'the negative-control protocol')
MUST_NOT_HIT = ('a result in TECHNE', 'the techne push')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b330 -- THE INDEX KEY. ### THE TECHNE EXTRACTION.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'techne-extraction'" in txt)
    have_row = ('"techne-extraction"' in txt)
    print('  techne-extraction    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('techne-extraction')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : techne-extraction returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'techne-extraction' in o
        ok = ok and g
        print('    %-40s reaches the b330 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-METHODONLY -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'METHOD, NOT A RESULT' in out
    a2 = 'NOT PUSHED' in out and 'PRIVATE UNTIL ITS PROVISIONALS ARE FILED' in out
    a3 = 'makes no legal claim' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says METHOD, NOT A RESULT              : %s' % a1)
    print('    ### and NOT PUSHED, private until filed            : %s' % a2)
    print('    ### and that the patent note makes no legal claim  : %s' % a3)
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
