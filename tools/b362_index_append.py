# -*- coding: utf-8 -*-
"""b362_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTADOPTED`.** ### A reader who asks *what b362 settled*
### must be handed: a register LOCATED AND PINNED AND NOT ADOPTED; **NO FACE PROMOTED**; **NO DISTANCE
### ### EVALUATED**; a criterion LOCATED and not PROVED; an unconditional finite side that **BUYS
### ### NOTHING**, because the criterion is a statement about a limit and an unconditional theorem bounds
### the finite side away from zero at every reach; and **NO BRIDGE TYPED** to any other instance.
### ### **`the register is adopted`, `a face is promoted`, `the distance is evaluated` AND `the criterion
### is proved` STAY UNKEYED**, each checked NO KEY before this file was written.
### ### **AND ONE ALIAS IS DELIBERATELY NOT CLAIMED:** ### `the criterion` already reaches `window-opened`.
### ### **AN ALIAS THAT COLLIDES WITH A BANKED KEY IS A FALSE HIT WAITING TO HAPPEN.**
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

CORR = io.open(os.path.join(D, 'b362_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
R = json.load(io.open(os.path.join(D, 'b362_read.json'), encoding='utf-8'))
E = json.load(io.open(os.path.join(D, 'b362_reads.json'), encoding='utf-8'))
L = json.load(io.open(os.path.join(D, 'b362_locate.json'), encoding='utf-8'))

Q = chr(34)
BS = chr(92)
APOS = BS + "'"


def s(x):
    return str(x)


KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'approximation-register': ['the approximation register', 'Nyman-Beurling', 'Baez-Duarte',\n"
    "                              'the closed span of dilations', 'the distance to the span',\n"
    "                              'the register read under a cap'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")

ROW_NEW = (
    "    # ### THE APPROXIMATION REGISTER, READ UNDER A CAP (b362).\n"
    "    (" + Q + "approximation-register" + Q + ", " + Q + "b362 (a read and a pricing; it computes nothing and adopts nothing)" + Q + ",\n"
    "     " + Q + "LOCATED BUT NOT WORTH OPENING at the reach this record can afford. The classical criterion and the variant restricting its family to the naturals were" + Q + "\n"
    "     " + Q + " located at pinned sources (" + s(L['attempted']) + " addresses attempted, " + s(L['fetched']) + " fetched, every one hashed) and quoted with their hypotheses unfolded one by one; the" + Q + "\n"
    "     " + Q + " navigator" + APOS + "s hint was treated as a SEARCH STRING AND NEVER AS A SOURCE and comes out CONFIRMED, WITH ONE CORRECTION -- the space, which the source" + Q + "\n"
    "     " + Q + " itself flags as a modified form of an original set elsewhere. THE STRUCTURAL FINDING: A FINITE INSTANCE HERE IS AN UNCONDITIONAL UPPER BOUND, since" + Q + "\n"
    "     " + Q + " the quantity" + APOS + "s definition mentions no zero and no hypothesis and an infimum over a subset is at least the infimum over the whole -- SO THIS REGISTER" + Q + "\n"
    "     " + Q + " DOES NOT CARRY THE SHORTFALL THE WINDOW ACT FOUND IN THE POSITIVITY REGISTER. THE SHORTFALL IT CARRIES INSTEAD IS THE RATE: the criterion is a" + Q + "\n"
    "     " + Q + " statement about a LIMIT and an UNCONDITIONAL theorem bounds the finite side away from zero at every reach, while the only UPPER bound located is" + Q + "\n"
    "     " + Q + " CIRCULAR AT (i), made under the hypothesis in its source" + APOS + "s own words. So what is unconditional here is the OBSTRUCTION and what would be progress" + Q + "\n"
    "     " + Q + " is CONDITIONAL. " + s(E['reads']) + " reads located, " + s(E['anchors_differing']) + " anchors differing from the hint that found them." + Q + ",\n"
    "     " + Q + "### THE REGISTER IS LOCATED AND PINNED AND IS NOT ADOPTED. ### NO FACE IS PROMOTED. ### NO GRADE IS CONFERRED BY A SEAT: the ledger row grades an" + Q + "\n"
    "     " + Q + " IMPORT at cite and says the corpus holds nothing here. ### NOTHING WAS COMPUTED AND NO DISTANCE WAS EVALUATED at any index, by any route, at any" + Q + "\n"
    "     " + Q + " precision. ### A LOCATED STATEMENT IS NOT A PROVED ONE, and a criterion located is not a criterion the corpus holds. ### AN UNCONDITIONAL FINITE" + Q + "\n"
    "     " + Q + " SIDE IS NOT A ROUTE: it is the one thing here better than the positivity register" + APOS + "s and it buys nothing, because the question was never about" + Q + "\n"
    "     " + Q + " any finite index. ### NOT WORTH OPENING IS A JUDGEMENT ABOUT WHAT THIS RECORD CAN AFFORD AND NOT ABOUT THE MATHEMATICS. ### THE PRICING WAS NOT" + Q + "\n"
    "     " + Q + " ATTEMPTED AND WAS THEN PRICED: the record holds no value, no control and no fixture here, the literature" + APOS + "s numbers are at a reference this act did" + Q + "\n"
    "     " + Q + " NOT fetch, and an instrument with no control is a number with no standing. ### THE SEARCH IS NOT A SURVEY and what was not located is AN ABSENCE OF" + Q + "\n"
    "     " + Q + " READING. ### NO BRIDGE IS TYPED to any other instance, in either direction. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE" + Q + "\n"
    "     " + Q + " CLAUSE HAS NOT MOVED. ### NO ACT IS RE-VERDICTED. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b362_the_approximation_register.txt; data/" + R['run_file'] + "; data/" + E['run_file'] + "; data/b362_locate_run.txt;" + Q + "\n"
    "     " + Q + " data/b362_registration_2026-09-07.txt (LOCKED before any read, search or fetch, on the audit" + APOS + "s own exit code);" + Q + "\n"
    "     " + Q + " the pinned renderings at data/b362_source_*.txt;" + Q + "\n"
    "     " + Q + " PLACE-papers FACES_LEDGER.md (row N1, a NEW row); CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('the approximation register', 'Nyman-Beurling', 'Baez-Duarte', 'the closed span of dilations',
           'the distance to the span', 'the register read under a cap')
MUST_NOT_HIT = ('the register is adopted', 'a face is promoted', 'the distance is evaluated',
                'the criterion is proved')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b362 -- THE INDEX KEY. ### THE APPROXIMATION REGISTER, READ AND NOT ADOPTED.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    coll, _rc = query('the criterion')
    print('    ### the alias NOT claimed, and why : `the criterion` already reaches a banked key : %s'
          % ('window-opened' in coll))
    have_key = ("'approximation-register'" in txt)
    have_row = ('"approximation-register"' in txt)
    print('  approximation-register key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('approximation-register')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : approximation-register returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'approximation-register' in o
        ok = ok and g
        print('    %-44s reaches the b362 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTADOPTED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'IS NOT ADOPTED' in out and 'NO FACE IS PROMOTED' in out
    a2 = 'NO DISTANCE WAS EVALUATED' in out and 'NOTHING WAS COMPUTED' in out
    a3 = 'A LOCATED STATEMENT IS NOT A PROVED ONE' in out
    a4 = 'AN UNCONDITIONAL FINITE' in out and 'it buys nothing' in out
    a5 = 'NO BRIDGE IS TYPED' in out and 'THE PARTITION STAYS UNDECIDED' in out
    ok = ok and a1 and a2 and a3 and a4 and a5
    print('    the register is not adopted and no face promoted          : %s' % a1)
    print('    ### nothing computed and no distance evaluated            : %s' % a2)
    print('    ### a located statement is not a proved one               : %s' % a3)
    print('    ### the unconditional finite side buys nothing            : %s' % a4)
    print('    ### no bridge typed, and the partition stays undecided     : %s' % a5)
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
