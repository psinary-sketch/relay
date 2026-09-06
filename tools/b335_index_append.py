# -*- coding: utf-8 -*-
"""b335_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-BINDS-NOTHING`.** ### A reader who asks *where are the standing
### clauses* or *what is the STOP format* must be handed the file, its version, its citation form, the scanner's
### check and the rule -- with the sentence that the file binds nothing by itself and the draft binds nothing.
### ### **`the draft binds` AND `a new rule` STAY UNKEYED.** ### The index is swept for stems after the write.
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

CORR = io.open(os.path.join(D, 'b335_corr_run.txt'), encoding='utf-8').read()
ROWNUM = re.search(r'last row number is (\d+)', CORR).group(1)
RUN = io.open(os.path.join(D, 'b335_standing_run.txt'), encoding='utf-8').read()
_m = re.search(r'clauses measured (\d+) ; STANDING \(>= (\d+) of (\d+)\) (\d+) ; FREQUENT, NOT STANDING (\d+)', RUN)
MEASURED, MAJ, N, STANDING, FREQ = _m.groups()

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'ferry-standing': ['the standing clauses', 'ferry standing', 'FERRY_STANDING', 'the standing file', 'where are the standing clauses',\n"
    "                       'the STOP format', 'the stop format', 'the draft ferry', 'DRAFT -- NAVIGATOR EDITS', 'the citation check',\n"
    "                       'a stale citation', 'what is the STOP format', 'Rule 6'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE STANDING CLAUSES, FILED (b335, leg 0 of the sortie b335-b338).\n"
    "    (\"ferry-standing\", \"b335 (filings only: a standing-clauses file, a scanner check by order, a rule of the executor's format)\",\n"
    "     \"THE STANDING CLAUSES OF THE RESEARCH SEAT'S FERRIES, in relay/tools/FERRY_STANDING.md VERSION 1: generated from the " + N + " banked ferries\"\n"
    "     \" b320-b334, " + MEASURED + " clauses measured, " + STANDING + " STANDING (carried by " + MAJ + " or more of " + N + "), " + FREQ + " FREQUENT, NOT STANDING, each with its count and\"\n"
    "     \" carriers, the wording b334's ferry's; cited by a ferry as FERRY_STANDING v1. THE FERRY SCAN (tools/ferry_scan.py) checks the citation\"\n"
    "     \" against the file's VERSION line and reports NONE / CURRENT / STALE / NO FILE, a STALE citation a hit (exit 1), fixtures of both\"\n"
    "     \" polarities built from the loaded version. RULE 6, THE STOP FORMAT (PLACE-papers/protocols/EXECUTOR_RULES.md, appended): the executor's\"\n"
    "     \" final message carries the closing summary, the pins, then a block headed DRAFT -- NAVIGATOR EDITS with a draft of the next ferry.\",\n"
    "     \"### THE FILE BINDS NOTHING BY ITSELF; A FERRY THAT CITES IT CARRIES ITS CLAUSES BY REFERENCE. ### THE DRAFT BINDS NOTHING: the next act runs\"\n"
    "     \" only on the navigator's paste. ### NO GRADE, NO CLAIM, NO TERMINAL. ### M-2 UNCHANGED\",\n"
    "     \"tools/FERRY_STANDING.md; data/b335_the_standing_clauses.txt; data/b335_standing_run.txt; data/b335_scan_selftest.txt; data/b335_scan_cite_stale.txt;\"\n"
    "     \" data/b335_rule6_run.txt; data/b335_registration_2026-09-06.txt (sealed before any write); PLACE-papers protocols/EXECUTOR_RULES.md Rule 6;\"\n"
    "     \" CORRESPONDENCE.md row " + ROWNUM + "\"),\n"
)

ALIASES = ('the standing clauses', 'ferry standing', 'FERRY_STANDING', 'the STOP format', 'the draft ferry', 'the citation check', 'Rule 6', 'where are the standing clauses')
MUST_NOT_HIT = ('the draft binds', 'a new rule', 'the cost census')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b335 -- THE INDEX KEY. ### THE STANDING CLAUSES, FILED.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'ferry-standing'" in txt)
    have_row = ('"ferry-standing"' in txt)
    print('  ferry-standing    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('ferry-standing')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : ferry-standing returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'ferry-standing' in o
        ok = ok and g
        print('    %-40s reaches the b335 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-BINDS-NOTHING -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'THE FILE BINDS NOTHING BY ITSELF' in out
    a2 = 'THE DRAFT BINDS NOTHING' in out
    a3 = 'NO GRADE, NO CLAIM, NO TERMINAL' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says the file binds nothing by itself   : %s' % a1)
    print('    ### and that the draft binds nothing               : %s' % a2)
    print('    ### and no grade, no claim, no terminal            : %s' % a3)
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
