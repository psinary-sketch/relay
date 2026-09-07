# -*- coding: utf-8 -*-
"""b360_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTFOLDED`.** ### A reader who asks *what the fold settles*
### must be handed: a fold PROVES NOTHING and moves no grade; the three rhyming obstructions are THREE
### obstructions with NO BRIDGE TYPED; an EDGE LOCATED IS NOT A FLOOR EXPLAINED and the floor is still
### unexplained; the partition STAYS UNDECIDED and the clause has not moved; the roster row is a CARRYING
### DECISION that says nothing about whether the ledger is true and is NOT retroactive; and the span's
### closing sentence is a statement about this board, not a claim that no move exists.
### ### **`the fold proves it`, `the obstructions are equivalent`, `the quantifier is closed` AND `the roster
### change repairs the archive` STAY UNKEYED.**
### ### **AND ONE ALIAS IS DELIBERATELY NOT CLAIMED:** ### `the arc as one statement` already reaches
### `priced-and-resolved-fold` (b348). ### **AN ALIAS THAT COLLIDES WITH A BANKED KEY IS A FALSE HIT WAITING
### ### TO HAPPEN**, and the collision was checked before this file was written, not after.
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

CORR = io.open(os.path.join(D, 'b360_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
F = json.load(io.open(os.path.join(D, 'b360_fold.json'), encoding='utf-8'))
E = json.load(io.open(os.path.join(D, 'b360_reads.json'), encoding='utf-8'))
RS = json.load(io.open(os.path.join(D, 'b360_roster.json'), encoding='utf-8'))

Q = chr(34)
BS = chr(92)
APOS = BS + "'"


def s(x):
    return str(x)


KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'uniformity-fold': ['the fold b349', 'the uniformity arc', 'the three that rhyme',\n"
    "                       'what the checks certify', 'the instrument edge', 'the mirror roster addition',\n"
    "                       'the span b349', 'the fourth instance'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")

ROW_NEW = (
    "    # ### THE UNIFORMITY ARC, b349-b359 -- THE FOLD (b360).\n"
    "    (" + Q + "uniformity-fold" + Q + ", " + Q + "b360 (a filings act; it proves nothing and moves no grade)" + Q + ",\n"
    "     " + Q + "THE FOLD OF b349-b359: " + s(F['n_span']) + " acts filed as one section of the findings document, PURELY ADDITIVE, " + s(F['lines_added']) + " lines added and nothing above them" + Q + "\n"
    "     " + Q + " edited. THE SPAN IS COUNTED, NOT TYPED: the emitter reads the last fold section" + APOS + "s own filing line off FINDINGS.md and finds each act" + APOS + "s bank on disk," + Q + "\n"
    "     " + Q + " and refuses to emit if the counted span and the result table disagree. F-QUOTE " + s(F['quotes_failing']) + " failing; F-NOGRADE " + s(F['grades_failing']) + " failing, the no-grade-moved claim" + Q + "\n"
    "     " + Q + " mechanical as b348 built it. The extract located " + s(E['reads']) + " of " + s(E['reads']) + " reads, " + s(E['anchors_differing']) + " anchors differing from the hint that found them." + Q + "\n"
    "     " + Q + " THE ARC AS ONE STATEMENT, at the grade the acts support: the archimedean instrument" + APOS + "s EDGE is located at the quadrature bound and the floor is still" + Q + "\n"
    "     " + Q + " unexplained; the exponent resolved on the rate axis; the partition UNDECIDED with its coordinates failing in different ways and the abscissa closed" + Q + "\n"
    "     " + Q + " by a sum already in the record; the width statement an equivalence at each fixed support and not across supports; the Li tail circular; the" + Q + "\n"
    "     " + Q + " lawfulness checks confirming the construction rather than testing the class; and THE CLAUSE HAS NOT MOVED. THE THREE THAT RHYME -- the clause" + APOS + "s" + Q + "\n"
    "     " + Q + " quantifier (b332), the height coordinate" + APOS + "s enumeration (b351), the width coordinate" + APOS + "s union (b353) -- with b358" + APOS + "s localization as a FOURTH ENTRY OF THE" + Q + "\n"
    "     " + Q + " SAME KIND and NOT a fifth obstruction. AND THE AUTHOR" + APOS + "S RULING EXECUTED: FACES_LEDGER.md added to the mirror roster, " + s(RS['before']) + " rows to " + s(RS['after']) + ", appended at" + Q + "\n"
    "     " + Q + " the END so no existing slot changes." + Q + ",\n"
    "     " + Q + "### A FOLD IS A SUMMARY OF ITS ACTS AT THEIR OWN GRADES: it proves nothing, discharges nothing, and MOVES NO GRADE -- checked, not asserted." + Q + "\n"
    "     " + Q + " ### THREE OBSTRUCTIONS THAT RHYME ARE THREE OBSTRUCTIONS, AND NO BRIDGE IS TYPED between them in either direction; the deposit" + APOS + "s own refusal to" + Q + "\n"
    "     " + Q + " compile cross-register equivalence is quoted at the deposited file. ### AN EDGE LOCATED IS NOT A FLOOR EXPLAINED: b350" + APOS + "s THE FLOOR IS" + Q + "\n"
    "     " + Q + " UNEXPLAINED stands and b352" + APOS + "s UNDER-RESOLVED AS A FIT stands. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS" + Q + "\n"
    "     " + Q + " NOT MOVED. ### THE ROSTER ROW IS A CARRYING DECISION AND NOTHING ELSE: carrying a ledger in an archive says nothing about whether what the" + Q + "\n"
    "     " + Q + " ledger says is true, and the addition reaches the archive from this rebuild forward and does NOT place it in any prior mirror. ### THE SPAN" + APOS + "S" + Q + "\n"
    "     " + Q + " CLOSING SENTENCE IS A STATEMENT ABOUT THIS BOARD AND NOT A CLAIM THAT NO MOVE EXISTS, and it opens nothing. ### NO GRADE MOVED. ### NO BAR" + Q + "\n"
    "     " + Q + " MOVED. ### NO ACT RE-VERDICTED. ### NO TERMINAL. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b360_the_fold.txt; data/" + F['run_file'] + "; data/b360_fold_emitted.md; data/" + E['run_file'] + ";" + Q + "\n"
    "     " + Q + " data/b360_registration_2026-09-07.txt (LOCKED before any write, on the audit" + APOS + "s own exit code);" + Q + "\n"
    "     " + Q + " PLACE-papers FINDINGS.md (the appended section); relay tools/mirror_roster.json (the author" + APOS + "s ruling executed);" + Q + "\n"
    "     " + Q + " CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('the fold b349', 'the uniformity arc', 'the three that rhyme', 'what the checks certify',
           'the instrument edge', 'the mirror roster addition', 'the span b349', 'the fourth instance')
MUST_NOT_HIT = ('the fold proves it', 'the obstructions are equivalent', 'the quantifier is closed',
                'the roster change repairs the archive')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print("b360 -- THE INDEX KEY. ### THE UNIFORMITY ARC, FOLDED.")
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    coll, _rc = query('the arc as one statement')
    print('    ### the alias NOT claimed, and why : `the arc as one statement` already reaches a banked key : %s'
          % ('priced-and-resolved-fold' in coll))
    have_key = ("'uniformity-fold'" in txt)
    have_row = ('"uniformity-fold"' in txt)
    print('  uniformity-fold key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('uniformity-fold')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : uniformity-fold returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'uniformity-fold' in o
        ok = ok and g
        print('    %-44s reaches the b360 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTFOLDED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A FOLD IS A SUMMARY OF ITS ACTS AT THEIR OWN GRADES' in out and 'MOVES NO GRADE' in out
    a2 = 'THREE OBSTRUCTIONS THAT RHYME ARE THREE OBSTRUCTIONS, AND NO BRIDGE IS TYPED' in out
    a3 = 'AN EDGE LOCATED IS NOT A FLOOR EXPLAINED' in out and 'THE PARTITION STAYS UNDECIDED' in out
    a4 = 'CARRYING A DECISION' not in out and 'says nothing about whether what the' in out and 'does NOT place it in any prior mirror' in out
    a5 = 'NOT A CLAIM THAT NO MOVE EXISTS' in out and 'THE CLAUSE HAS' in out
    ok = ok and a1 and a2 and a3 and a4 and a5
    print('    a fold moves no grade                                     : %s' % a1)
    print('    ### three that rhyme are three, and no bridge is typed    : %s' % a2)
    print('    ### an edge is not a floor, and the partition is undecided: %s' % a3)
    print('    ### the roster row carries and does not certify           : %s' % a4)
    print('    ### the closing sentence is not a claim that none exists  : %s' % a5)
    post = {}
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        post[q] = no_key(o)
        g = pre[q] and post[q]
        ok = ok and g
        print('    %-40s NO KEY after  : %s  %s' % (q, post[q], 'PASS' if g else '### FAIL ###'))
    print('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
