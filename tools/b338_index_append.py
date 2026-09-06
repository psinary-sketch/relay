# -*- coding: utf-8 -*-
"""b338_index_append.py -- ONE KEY, TWO ROWS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTAVERDICT`.** ### A reader who asks *what did the stated-clause arc
### find* must be handed the fold -- four acts at their own grades, the desk with the wave's candidate list restated
### and the housekeeping's state beside it -- with the sentences that a fold is a filing and not a result, the arc's
### one statement a summary and not a verdict, and the wave the author's. ### The section's numbers and the row
### numbers are read from the run files at write time. ### **`the arc's verdict` AND `the wave recommended` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b338_corr_run.txt'), encoding='utf-8').read()
_m = re.search(r'rows to append : (\d+) and (\d+)', CORR)
R1, R2 = _m.group(1), _m.group(2)
J = json.load(io.open(os.path.join(D, 'b338_fold_rows.json'), encoding='utf-8'))

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'stated-clause-arc-fold': ['the fold b331 to b334', 'the fold of b331', 'the sortie fold', 'the stated-clause arc', 'the stated clause arc',\n"
    "                               'what did the stated-clause arc find', 'the wave\\'s candidate list', 'the candidate list', 'the candidate list restated',\n"
    "                               'the housekeeping\\'s state', 'the desk after b337', 'the fold of the sortie'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE STATED-CLAUSE ARC, b331-b334 -- THE FOLD (b338, leg 3 of the sortie b335-b338).\n"
    "    (\"stated-clause-arc-fold\", \"b338 (a filings act: the fold of four acts, purely additive)\",\n"
    "     \"THE FOLD, b331 THROUGH b334: one section appended to FINDINGS.md (+" + str(J['lines_added']) + " lines, " + str(J['lines_before']) + " -> " + str(J['lines_after']) + ") by a committed generator --\"\n"
    "     \" F-QUOTE at every quotation against the originating act, F-COUNT the arc exactly, F-MODULES every rule by module or by tool on disk, the\"\n"
    "     \" working file and the blob true prefixes of the result; four results at their own grades (b331 FILED; b332 STATED; b333 DERIVES-ON-IMPORTS\"\n"
    "     \" for K5, MEASURED-ON-FAMILIES not conferred; b334 MEASURED on a grid at this reach), four obstacles, four corrections, three sealed bars\"\n"
    "     \" found defective and tabled, the lore typed MODULE / TOOL / JUDGEMENT, the suite this arc added; THE DESK'S FIRST ITEM the wave's\"\n"
    "     \" candidate list restated (b324's six, b331's addition, this arc's typed candidates) with the housekeeping's state as b337 stated it\"\n"
    "     \" beside it. THE ARC AS ONE STATEMENT: the clause stated whole and not discharged; its softest constituent derived under the import bar;\"\n"
    "     \" the room charted over aims; the clause not moved.\",\n"
    "     \"### A FILING, NOT A RESULT; THE ONE STATEMENT A SUMMARY AND NOT A VERDICT. ### THE WAVE IS THE AUTHOR'S; THE LIST IS TYPED, NOT RANKED.\"\n"
    "     \" ### NO GRADE MOVED. ### A CHART IS NOT A PROOF. ### NO TERMINAL. ### M-2 UNCHANGED\",\n"
    "     \"data/b338_the_fold.txt; data/b338_fold_run.txt; data/b338_fold_emitted.md; data/b338_fold_rows.json; data/b338_registration_2026-09-06.txt\"\n"
    "     \" (sealed before the generator); FINDINGS.md (THE STATED-CLAUSE ARC, b331-b334 -- THE FOLD); CORRESPONDENCE.md rows " + R1 + " and " + R2 + "\"),\n"
)

ALIASES = ('the fold b331 to b334', 'the sortie fold', 'the stated-clause arc', "the wave's candidate list", 'the candidate list', "the housekeeping's state",
           'what did the stated-clause arc find', 'the fold of the sortie')
MUST_NOT_HIT = ("the arc's verdict", 'the wave recommended', 'the clause discharged')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b338 -- THE INDEX KEY. ### THE STATED-CLAUSE ARC, b331-b334 -- THE FOLD.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'stated-clause-arc-fold'" in txt)
    have_row = ('"stated-clause-arc-fold"' in txt)
    print('  stated-clause-arc-fold    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('stated-clause-arc-fold')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : stated-clause-arc-fold returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'stated-clause-arc-fold' in o
        ok = ok and g
        print('    %-40s reaches the b338 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTAVERDICT -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A FILING, NOT A RESULT; THE ONE STATEMENT A SUMMARY AND NOT A VERDICT' in out
    a2 = "THE WAVE IS THE AUTHOR'S; THE LIST IS TYPED, NOT RANKED" in out
    a3 = 'NO GRADE MOVED' in out and 'A CHART IS NOT A PROOF' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says a filing, not a result; a summary, not a verdict : %s' % a1)
    print("    ### and that the wave is the author's, the list typed not ranked : %s" % a2)
    print('    ### and no grade moved, a chart not a proof                       : %s' % a3)
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
