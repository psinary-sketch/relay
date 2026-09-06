# -*- coding: utf-8 -*-
"""b331_index_append.py -- ONE KEY, TWO ROWS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTVERDICT`.** ### A reader who asks *what did the arc
### establish* must be handed the six clauses WITH their scope and the sentence that the clause has not
### moved -- never a fold read as a verdict on the arc. ### The numbers (lines added, F-QUOTE tally, the
### row numbers) are read from the run files at write time.
### ### **`the clause moved` AND `the arc proved` STAY UNKEYED.** ### The index is swept for stems after
### the write.
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
import b331_correspondence as R  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

K = R.read_records()
CORR = io.open(os.path.join(D, 'b331_corr_run.txt'), encoding='utf-8').read()
RN = re.search(r'last 2 row number\(s\) are \[(\d+), (\d+)\]', CORR)
ROW1, ROW2 = RN.group(1), RN.group(2)

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'discriminating-arc-fold': ['the discriminating arc fold', 'the discriminating-family arc', 'b323-b330',\n"
    "                                'the eight acts', 'fold b323', 'the negative-control arc', 'what did the arc establish',\n"
    "                                'the arc as one statement', 'the desk', 'the instrument can say no',\n"
    "                                'the reconciliation wave', 'the patent receipts'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE DISCRIMINATING-FAMILY ARC, b323-b330 -- THE FOLD (b331).\n"
    "    (\"discriminating-arc-fold\", \"b331 (a filings act)\",\n"
    "     \"FINDINGS.md gains the section '" + K['section'].replace('\u2013', '-').replace('\u2014', '--') + "', " + ('%+d' % K['added']) + " lines\"\n"
    "     \" (" + str(K['before']) + " -> " + str(K['after']) + "): the eight acts each with its grade as its own act left it, its own quotation, its scope and its\"\n"
    "     \" obstacle quoted; the corrections table; the sealed-bars-found-defective table continued; the seats' declared\"\n"
    "     \" defects as their own table; the lore with a TECHNE module beside each mechanized rule; the suite; the desk.\"\n"
    "     \" ### F-QUOTE " + str(K['fq_n']) + " quotations, " + str(K['fq_bad']) + " unfindable, the discrimination arm firing; F-COUNT the arc exactly;\"\n"
    "     \" PURELY ADDITIVE measured on the working file and on the blob\",\n"
    "     \"### A FILING, AT THE GRADE OF THE ACTS IT FOLDS AND NO HIGHER. ### NO GRADE MOVED; NO ACT RE-VERDICTED; NO NEW\"\n"
    "     \" MATHEMATICS. ### The judgement that each quoted sentence is its act's own voice is the seat's, declared.\"\n"
    "     \" ### M-2 UNCHANGED\",\n"
    "     \"D:/MY-DOwnloads/PLACE-papers/FINDINGS.md (the section); data/b331_fold_emitted.md; data/b331_fold_run.txt;\"\n"
    "     \" data/b331_fold_rows.json; data/b331_the_fold.txt; data/b331_registration_2026-09-06.txt (sealed before any\"\n"
    "     \" write); CORRESPONDENCE.md row " + ROW1 + "\"),\n"
    "    # ### THE ARC AS ONE STATEMENT, WITH ITS SCOPE (b331).\n"
    "    (\"discriminating-arc-fold\", \"b331 (the arc's six clauses, each an act's own verdict at its own grade)\",\n"
    "     \"the instrument can say no (b325, b326, b328); the zeta window is a passed test for the discriminating family\"\n"
    "     \" at this reach, and for the arc's family b326's verdict stands (b328); the finite side is compiled, general\"\n"
    "     \" where the header says general and per cell where it says per cell (b329); the two margins are two\"\n"
    "     \" evaluations of one distribution separated by the pole constant (b324, b327); the object's archimedean unit\"\n"
    "     \" is in its space by derivation and priced at bench (b300, b322, unchanged); THE CLAUSE HAS NOT MOVED and no\"\n"
    "     \" act in the arc claims otherwise\",\n"
    "     \"### A SUMMARY AND NOT A VERDICT. ### The no is a verdict on one family, one instrument, one reach -- nothing\"\n"
    "     \" about the method or about zeta; the compiled finite side certifies the model's arithmetic and the counting\"\n"
    "     \" form, not the identification with the source's trace and not the compact part beyond the cells; the\"\n"
    "     \" margins' relation is a reading under an import bar with the bridge owed. ### NOTHING ABOUT THE IDENTITY,\"\n"
    "     \" h2, OR THE ROSTER. ### M-2 UNCHANGED\",\n"
    "     \"D:/MY-DOwnloads/PLACE-papers/FINDINGS.md (the section's 'The arc as one statement' and its scope paragraph);\"\n"
    "     \" data/b331_the_fold.txt; CORRESPONDENCE.md row " + ROW2 + "\"),\n"
)

ALIASES = ('the discriminating arc fold', 'the eight acts', 'fold b323', 'the negative-control arc', 'what did the arc establish',
           'the instrument can say no', 'the reconciliation wave', 'the patent receipts')
MUST_NOT_HIT = ('the clause moved', 'the arc proved')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b331 -- THE INDEX KEY. ### THE DISCRIMINATING-FAMILY ARC, FOLDED.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'discriminating-arc-fold'" in txt)
    have_row = ('"discriminating-arc-fold"' in txt)
    print('  discriminating-arc-fold    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('discriminating-arc-fold')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 2
    ok = ok and good
    print('  READ BACK : discriminating-arc-fold returns %d row(s), 2 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'discriminating-arc-fold' in o
        ok = ok and g
        print('    %-40s reaches the b331 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTVERDICT -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A FILING, AT THE GRADE OF THE ACTS IT FOLDS AND NO HIGHER' in out
    a2 = 'THE CLAUSE HAS NOT MOVED' in out
    a3 = 'A SUMMARY AND NOT A VERDICT' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says a filing at the acts\' grade and no higher : %s' % a1)
    print('    ### and that the clause has not moved                       : %s' % a2)
    print('    ### and that the statement is a summary, not a verdict      : %s' % a3)
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
