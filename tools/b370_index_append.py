# -*- coding: utf-8 -*-
"""b370_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTMOVED`.** ### A reader who asks *what `b370`
### settled* must be handed: ### that a fold ### **MOVES NO GRADE AND SETTLES NOTHING**; ### that the
### span ### **PRODUCED NO NEW MATHEMATICS**; ### that ### **SEVEN OF THE NINE ACTS PRODUCED NO RESULT
### ### ABOUT THE OBJECT AT ALL**; ### that the span counter ### **NOW READS WITHOUT WRITING**; and that
### the next arc is ### **NAMED, PRICED AND NOT OPENED.**
### ### **`the clause moved`, `the fold proves`, `the federation is audited` AND `the hook is durable`
### STAY UNKEYED**, each checked NO KEY before this file was written.
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

CORR = io.open(os.path.join(D, 'b370_corr_run.txt'), encoding='utf-8', errors='replace').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
E = json.load(io.open(os.path.join(D, 'b370_reads.json'), encoding='utf-8'))
S = json.load(io.open(os.path.join(D, 'b370_span.json'), encoding='utf-8'))
F = json.load(io.open(os.path.join(D, 'b370_fold.json'), encoding='utf-8'))
L = json.load(io.open(os.path.join(D, 'b370_lore.json'), encoding='utf-8'))
Q = json.load(io.open(os.path.join(D, 'b370_desk.json'), encoding='utf-8'))


def s(x):
    return str(x)


KEY_ANCHOR = 'KEYS = {\n'
KEY_NEW = (
    "    'apparatus-arc-fold': ['the apparatus arc', 'the fold b361', 'the span counted',\n"
    "                          'the three mints', 'the durability split'],\n"
)

ROW_ANCHOR = ('INDEX = [\n'
              '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')

ROW_NEW = (
    '    # ### THE APPARATUS ARC, b361-b369 -- THE FOLD (b370).\n'
    '    ("apparatus-arc-fold", "b370 (a fold; it proves nothing, discharges nothing and moves no grade -- plus one owner instrument repaired and three lore modules minted)",\n'
    '     "THE FOLD, b' + s(S['span_starts_at']) + ' THROUGH b' + s(S['this_act']) + ' -- ' + s(S['current_span']) + ' ACTS, THE SPAN COUNTED AND NOT TYPED. The counter reads the last fold section own filing line off FINDINGS.md and counts"\n'
    '     " forward, and the section is written ONLY because the count agreed with the range it names. F-NOGRADE HELD: ' + s(F['grade_misses']) + ' grade strings were not found verbatim in their own act bank."\n'
    '     " AND THE ATTRIBUTION WAS THE HARD HALF, NOT THE PRESENCE: the grade word SUPPORTED-BY-THE-SOURCE APPLICATION is b366 RULING and not b365 FINDING, and b365 row carries what b365 own bank says."\n'
    '     " ' + s(F['obstacles']) + ' obstacles are quoted, each located in the bank of the act that ORIGINATED it. THE ARC AS ONE STATEMENT: this span produced NO NEW MATHEMATICS about the clause; it produced two results about the"\n'
    '     " clause SHAPE -- the approximation register located and closed with its obstruction a RATE (b362), and the Li localization archimedean half supported at zeta with a stated constant (b361, b365) --"\n'
    '     " and its main product was NEITHER: it was making the record checkable by a reader who trusts none of it. SEVEN OF THE NINE ACTS PRODUCED NO RESULT ABOUT THE OBJECT AT ALL. THE THREE MINTS: one"\n'
    '     " incident does not show you a partition; a predicate that knows one shape finds one shape; and THE DURABILITY SPLIT -- a repair to a tracked file travels with a clone and a repair to an untracked"\n'
    '     " one does not, so the guards that have caught the most are the ones a fresh clone starts without. ' + s(E['reads']) + ' reads, ' + s(E['without_anchor']) + ' without an anchor.",\n'
    '     "### A FOLD MOVES NO GRADE AND SETTLES NOTHING. ### NO ACT IN THE SPAN IS RE-VERDICTED: every grade is its own act, checked verbatim against that act bank, and the two shape results are left at"\n'
    '     " the grades their own acts gave them and are NOT PROMOTED. ### THE CLAUSE HAS NOT MOVED AND NO ACT IN THE SPAN CLAIMS OTHERWISE. ### A FOLD THAT LET THE SEVEN APPARATUS ACTS READ AS PROGRESS ON"\n'
    '     " THE CLAUSE WOULD BE THE EXACT DEFECT THIS SPAN SPENT ITSELF FINDING ELSEWHERE. ### THE FOLD IS PURELY ADDITIVE: ' + s(F['sections_edited']) + ' existing sections edited, FINDINGS.md before a true prefix of after and"\n'
    '     " of its committed blob, read BEFORE THE PUSH. ### STEP ZERO: tools/b363_span.py wrote a run file and a JSON under b363 own stem on every run, whoever ran it -- filed twice, fixed never, a revert"\n'
    '     " both times. IT NOW READS AND DOES NOT WRITE; --emit writes under the CALLER own stem; its act number is read from the record; and A FIXTURE PROVES IT IN BOTH POLARITIES, because an arm that"\n'
    '     " cannot fail is not an arm. ### THE THREE MINTS EACH STATE THEIR MECHANIZABLE HALF APART: the first has NONE and says so first; the second is caught by re-derivation and NOT by any arm, because"\n'
    '     " the gate would have been written by the same hand with the same predicate; the third is mechanizable as a DURABLE / NOT DURABLE column and NOT mechanizable as a ranking by what a guard has"\n'
    '     " caught. ### THE DESK: ' + s(Q['confirmed']) + ' of ' + s(Q['items']) + ' CONFIRMED-BY-FILE, ' + s(Q['items_closed']) + ' CLOSED -- the THIRD act running to report that number with that caveat, and A MEASUREMENT WHOSE RESULT AND WHOSE"\n'
    '     " CAVEAT BOTH NEVER MOVE IS A MEASUREMENT NOBODY IS USING. ### TWO ITEMS NAMED AS STILL OWED: the count claim above the repaired list, so THE FRONT DOCUMENT IS NOT NOW CORRECT; and the hook non-"\n'
    '     " durability, PRICED AND NOT BUILT. ### COMPONENT 5 IS NAMED, PRICED AND NOT OPENED: no repository audited, no surface read for correctness, and THE PROFILE THAT WOULD SETTLE ITS FIRST TARGET IS"\n'
    '     " NOT OPENED. ### NO LEAN FILE TOUCHED, NO BUILD RUN, NO TECHNE MODULE PUSHED. ### NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### M-2"\n'
    '     " UNCHANGED",\n'
    '     "data/b370_the_fold.txt; data/' + E['run_file'] + '; data/' + S['run_file'] + '; data/' + F['run_file'] + ';"\n'
    '     " data/' + L['run_file'] + '; data/' + Q['run_file'] + ';"\n'
    '     " data/b370_registration_2026-09-08.txt (LOCKED before any write of this act, on the audit own exit code);"\n'
    '     " tools/b370_fold.py (F-NOGRADE, the obstacles and the additive bar); tools/b370_lore.py (the three mints); tools/b363_span.py (REPAIRED: reads, does not write, with a two-polarity fixture);"\n'
    '     " PLACE-papers FINDINGS.md (one fold section, purely additive, ' + s(F['grew']) + ' bytes; FACES_LEDGER.md NOT written, no row moved);"\n'
    '     " TECHNE-Core modules/2026-09 (' + s(L['minted']) + ' minted, local commit ' + L['techne_head'] + ', NOT PUSHED); CORRESPONDENCE.md row ' + R1 + '"),\n'
)

ALIASES = ('the apparatus arc', 'the fold b361', 'the span counted', 'the three mints',
           'the durability split')
MUST_NOT_HIT = ('the clause moved', 'the fold proves', 'the federation is audited',
                'the hook is durable')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b370 -- THE INDEX KEY. ### THE APPARATUS ARC, FOLDED.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'apparatus-arc-fold'" in txt)
    have_row = ('"apparatus-arc-fold"' in txt)
    print('  apparatus-arc-fold key/row already present : %s / %s' % (have_key, have_row))
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file.')
        return 2
    if not (have_key and have_row):
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
    out, rc = query('apparatus-arc-fold')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : apparatus-arc-fold returns %d row(s), 1 required  %s'
          % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'apparatus-arc-fold' in o
        ok = ok and g
        print('    %-44s reaches the b370 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTMOVED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A FOLD MOVES NO GRADE AND SETTLES NOTHING' in out
    a2 = 'NO NEW MATHEMATICS about the clause' in out
    a3 = 'SEVEN OF THE NINE ACTS PRODUCED NO RESULT ABOUT THE OBJECT AT ALL' in out
    a4 = 'IT NOW READS AND DOES NOT WRITE' in out
    a5 = 'NAMED, PRICED AND NOT OPENED' in out
    a6 = 'THE CLAUSE HAS NOT MOVED' in out
    ok = ok and a1 and a2 and a3 and a4 and a5 and a6
    print('    a fold moves no grade and settles nothing                    : %s' % a1)
    print('    ### no new mathematics about the clause                      : %s' % a2)
    print('    ### seven of the nine produced no result about the object    : %s' % a3)
    print('    ### the span counter now reads without writing               : %s' % a4)
    print('    ### the next arc named, priced and not opened                : %s' % a5)
    print('    ### the clause has not moved                                 : %s' % a6)
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        g = pre[q] and no_key(o)
        ok = ok and g
        print('    %-40s NO KEY after  : %s  %s' % (q, no_key(o), 'PASS' if g else '### FAIL ###'))
    print('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
