# -*- coding: utf-8 -*-
"""b365_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTMOVED`.** ### A reader who asks *what b365 settled*
### must be handed: the convention **LOCATED**; the source **WORKING THE EXCEPTIONAL CASE ITSELF**; the
### localization **SUPPORTED AT ζ, WITH A STATED CONSTANT**; and, in the same breath, ### **THAT THE
### ### SUPPORT IS BY THE PAPER'S OWN APPLICATION AND NOT BY ITS OWN QUANTIFIER**, that ### **NO GRADE
### ### MOVES**, that ### **NO PROOF IS VERIFIED**, that the threshold is **PROPOSED AND NOT RULED**, and
### that the mint **SHIPS NO ARM**.
### ### **`the grade is moved`, `the theorem is corrected`, `the hypothesis covers zeta` AND `the
### threshold is ruled` STAY UNKEYED**, each checked NO KEY before this file was written.
### ### **AND ONE ALIAS IS DELIBERATELY NOT CLAIMED:** ### `the convention` alone is left free -- it is a
### word this record uses in several unrelated senses, and an alias that broad is a false hit waiting to
### happen.
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

CORR = io.open(os.path.join(D, 'b365_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
E = json.load(io.open(os.path.join(D, 'b365_reads.json'), encoding='utf-8'))
R = json.load(io.open(os.path.join(D, 'b365_read.json'), encoding='utf-8'))
M = json.load(io.open(os.path.join(D, 'b365_mint.json'), encoding='utf-8'))
F = json.load(io.open(os.path.join(D, 'b365_filing.json'), encoding='utf-8'))
ROWS = ', '.join(R['faces_rows']) or 'none'


def s(x):
    return str(x)


KEY_ANCHOR = 'KEYS = {\n'
KEY_NEW = (
    "    'cuspidality-convention': ['the cuspidality convention', 'the convention is located',\n"
    "                              'the exceptional case', 'W-ORD-LI-CUSP', 'the owed read'],\n"
)

ROW_ANCHOR = ('INDEX = [\n'
              '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')

ROW_NEW = (
    '    # ### THE OWED READ, PAID (b365).\n'
    '    ("cuspidality-convention", "b365 (a read; it computes nothing, verifies no proof and moves no grade)",\n'
    '     "THE CONVENTION IS ' + s(R['convention']) + ' AND THE SOURCE WORKS THE EXCEPTIONAL CASE ITSELF. Lagarias math/0404394v4 states results for irreducible cuspidal representations and the corpus object"\n'
    '     " is the trivial representation of GL(1), which the same paper marks as its own exception. THE PAPER NAMES A CONVENTION FOR IT AND SAYS WHY IT IS FORCED -- it removes the poles at s = 0 and"\n'
    '     " s = 1 for that case and concludes that its completed function is entire IN ALL CASES. AND IT CARRIES THE EXCEPTION THROUGH ITS OWN CUSPIDAL-HYPOTHESIS RESULTS, which a hypothesis line alone"\n'
    '     " would have hidden: Lemma 4.3 is stated for a cuspidal representation and applied to the exception by a Remark printed beneath it, and Lemma 4.2 hypothesis says cuspidal while its own"\n'
    '     " conclusion defines a term that is 1 exactly when the representation is the trivial one. THE CONSTANT AND THE ERROR TERM ARE DERIVED INDEPENDENTLY OF CUSPIDALITY: C1 depends on N and the"\n'
    '     " conductor alone, the implied constant is ABSOLUTE in the paper own word, AND THE PAPER PRINTS C1 FOR THE EXCEPTION AS A NUMBER in the paragraph after Theorem 5.1. A PAPER THAT COMPUTES A"\n'
    '     " THEOREM OWN CONSTANT FOR A CASE IS APPLYING THE THEOREM TO THAT CASE. SO THE LOCALIZATION IS ' + s(R['localization']) + '. AND WHAT IN THIS RECORD RESTS ON IT IS A NEGATIVE ANSWER: a bounded"\n'
    '     " pass found ' + s(len(R['faces_blocks'])) + ' of the ledger ' + s(R['faces_headings']) + ' blocks citing b358 or b361, every one an update to row ' + ROWS + ', and NO BANKED NUMBER OF THIS RECORD IS COMPUTED FROM THEOREM 5.1 CONSTANT."\n'
    '     " ' + s(E['reads']) + ' reads located, ' + s(E['anchors_differing']) + ' anchors differing from the hint that found them, ' + s(E['source_lines']) + ' source lines located at the pinned rendering.",\n'
    '     "### NO GRADE MOVES IN EITHER DIRECTION: H-CUSP stands where b358 left it and b361 decision stands where b361 left it, and A READ THAT SUPPORTS A GRADE DOES NOT RAISE IT. ### THE SUPPORT IS"\n'
    '     " BY THE PAPER OWN APPLICATION AND NOT BY ITS OWN QUANTIFIER: the theorem hypothesis line still says irreducible cuspidal and the paper never re-states it to admit the exception; what it does"\n'
    '     " instead is APPLY it, which is weaker and is what the quotations support. ### NO PROOF IS VERIFIED -- this act read what the paper states, checked no derivation, and could not; A LOCATED"\n'
    '     " STATEMENT IS NOT A PROVED ONE. ### b358 CIRCULARITY FINDING IS UNTOUCHED and nothing here bears on the zero channel. ### NO SOURCE WAS FETCHED and the rendering seam stands. ### THE"\n'
    '     " THRESHOLD IS PROPOSED AT ' + s(M['threshold_proposed']) + ' ACTS AND NOT RULED, with the spread ' + s(M['shortest']) + ' to ' + s(M['longest']) + ' printed beside it. ### THE MINT SHIPS NO ARM and claims no audit. ### NOTHING WAS COMPUTED"\n'
    '     " ABOUT THE OBJECT. ### NO ACT IS RE-VERDICTED. ### NO FACE IS PROMOTED. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",\n'
    '     "data/b365_the_owed_read_paid.txt; data/' + R['run_file'] + '; data/' + E['run_file'] + '; data/' + M['run_file'] + '; data/' + F['run_file'] + ';"\n'
    '     " data/b365_registration_2026-09-07.txt (LOCKED before the read, on the audit own exit code, with the pre-lock search declared on its face);"\n'
    '     " the pinned rendering at data/b358_source_lagarias0404394.txt (pinned b327, re-verified b358, NOT re-fetched here);"\n'
    '     " TECHNE-Core ' + M['module'] + ' (local-only at ' + M['techne_head'] + ', NOT pushed);"\n'
    '     " PLACE-papers OPEN_TRAILS.md (' + F['entry'] + ' marked ' + F['status'] + '; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row ' + R1 + '"),\n'
)

ALIASES = ('the cuspidality convention', 'the convention is located', 'the exceptional case',
           'W-ORD-LI-CUSP', 'the owed read')
MUST_NOT_HIT = ('the grade is moved', 'the theorem is corrected', 'the hypothesis covers zeta',
                'the threshold is ruled')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b365 -- THE INDEX KEY. ### THE OWED READ, PAID.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'cuspidality-convention'" in txt)
    have_row = ('"cuspidality-convention"' in txt)
    print('  cuspidality-convention key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('cuspidality-convention')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : cuspidality-convention returns %d row(s), 1 required  %s'
          % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'cuspidality-convention' in o
        ok = ok and g
        print('    %-44s reaches the b365 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTMOVED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'NO GRADE MOVES IN EITHER DIRECTION' in out and 'DOES NOT RAISE IT' in out
    a2 = 'NOT BY ITS OWN QUANTIFIER' in out
    a3 = 'NO PROOF IS VERIFIED' in out and 'NOT A PROVED ONE' in out
    a4 = 'AND NOT RULED' in out and 'SHIPS NO ARM' in out
    a5 = 'CIRCULARITY FINDING IS UNTOUCHED' in out and 'NO SOURCE WAS FETCHED' in out
    ok = ok and a1 and a2 and a3 and a4 and a5
    print('    no grade moves, and a supporting read does not raise one : %s' % a1)
    print('    ### the support is by application and not by quantifier    : %s' % a2)
    print('    ### no proof verified, and a located statement is not proved: %s' % a3)
    print('    ### the threshold not ruled, and the mint ships no arm     : %s' % a4)
    print('    ### the circularity finding untouched, and nothing fetched : %s' % a5)
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
