# -*- coding: utf-8 -*-
"""b361_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTDECIDED`.** ### A reader who asks *what b361 settled*
### must be handed: an index condition, and nothing else. ### **THE TAIL IS NOT CLOSED** -- it is closed by
### the ZERO channel, which has no unconditional bound at all. ### **THE CIRCULARITY FINDING IS
### ### UNTOUCHED.** ### **THE VALUE IS NOT QUOTED FROM THE SOURCE** but identified from two of the
### source's own displayed formulae. ### **`H-CUSP` IS INHERITED AND NOT DECIDED.** ### **NO GRADE IS
### ### CONFERRED BY A SEAT.**
### ### **`the tail is closed`, `the circularity is removed`, `the value is quoted from the source` AND
### `H-CUSP is decided` STAY UNKEYED**, and each was checked NO KEY before this file was written.
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

CORR = io.open(os.path.join(D, 'b361_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
R = json.load(io.open(os.path.join(D, 'b361_read.json'), encoding='utf-8'))
E = json.load(io.open(os.path.join(D, 'b361_reads.json'), encoding='utf-8'))

Q = chr(34)
BS = chr(92)
APOS = BS + "'"


def s(x):
    return str(x)


KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'index-condition-decided': ['H-NGEK', 'the held item', 'the index condition',\n"
    "                               'the archimedean index condition', 'the absolute constant',\n"
    "                               'the vacuous condition'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")

ROW_NEW = (
    "    # ### THE HELD ITEM, QUOTED THEN BRANCHED (b361).\n"
    "    (" + Q + "index-condition-decided" + Q + ", " + Q + "b361 (a read and one square of zero; it proves nothing and confers no grade)" + Q + ",\n"
    "     " + Q + "THE INDEX CONDITION ON THE ARCHIMEDEAN CHANNEL IS VACUOUS FOR THE CORPUS" + APOS + "S OBJECT: K(pi_triv) = " + s(R['K']) + ", so Lagarias" + APOS + "s Theorem 5.1," + Q + "\n"
    "     " + Q + " whose implied constant is ABSOLUTE, holds at every index the corpus computes and its error term O(N(K(pi)+1)) collapses to O(1). b358 left" + Q + "\n"
    "     " + Q + " it UNDECIDABLE-FROM-THE-RECORD under its own cap -- DETERMINED IS NOT COMPUTED -- and named one evaluation as what would decide it. THE" + Q + "\n"
    "     " + Q + " BRANCH WAS FIXED BY THE ORDER BEFORE THE QUOTATION WAS SEEN and the registration was LOCKED BEFORE ANY READ, with the locked face declaring" + Q + "\n"
    "     " + Q + " that this seat had read the item" + APOS + "s bank one act earlier and that RECOLLECTION IS NEVER A SOURCE FOR A VALUE. The definition is located AT" + Q + "\n"
    "     " + Q + " CONTENT in the pinned source ((2.1), (2.2), (2.3), (5.3)); the source states its own completed L-function for the trivial representation and" + Q + "\n"
    "     " + Q + " states its conductor; at N = 1 these force the archimedean parameter to zero, and (5.3) gives the constant. " + s(E['reads']) + " reads, " + s(E['without_anchor']) + " without an anchor," + Q + "\n"
    "     " + Q + " " + s(E['anchors_differing']) + " anchors differing from the hint that found them. AND THE THING NO SEAT WROTE DOWN: the source" + APOS + "s own introduction already gives the same" + Q + "\n"
    "     " + Q + " asymptotic for all n >= 1 at (1.12), but with an implied constant that DEPENDS ON pi -- so the index condition was always the price of the" + Q + "\n"
    "     " + Q + " ABSOLUTE constant, and nobody had put the two statements side by side, including b358, which quoted (5.1) and not (1.12)." + Q + ",\n"
    "     " + Q + "### AN INDEX CONDITION DECIDED IS NOT A BOUND PROVED, AND IT IS NOT A CLOSED TAIL: the tail is closed by the ZERO channel, which has NO" + Q + "\n"
    "     " + Q + " UNCONDITIONAL BOUND AT ALL. ### THE CIRCULARITY FINDING IS UNTOUCHED -- the tail bound asserts the hypothesis, and no decision here changes" + Q + "\n"
    "     " + Q + " that. ### THE VALUE IS NOT QUOTED FROM THE SOURCE: it is an IDENTIFICATION of two of the source" + APOS + "s own displayed formulae, and the source" + Q + "\n"
    "     " + Q + " writes neither the parameter nor the constant for this representation anywhere. ### H-CUSP IS INHERITED AND NOT DECIDED: Theorem 5.1 is" + Q + "\n"
    "     " + Q + " stated for an irreducible CUSPIDAL representation and the corpus" + APOS + "s object is the one the source marks as its exception; b358 graded that" + Q + "\n"
    "     " + Q + " question and this act stands on that grade. ### A VACUOUS CONDITION IS NOT AN OBSTRUCTION REMOVED -- a condition that costs nothing to" + Q + "\n"
    "     " + Q + " satisfy was never the obstruction. ### NO GRADE IS CONFERRED BY A SEAT; the row grade NAMED-ONLY stands. ### NO ACT IS RE-VERDICTED. ### NO" + Q + "\n"
    "     " + Q + " COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b361_the_held_item.txt; data/" + R['run_file'] + "; data/" + E['run_file'] + ";" + Q + "\n"
    "     " + Q + " data/b361_registration_2026-09-07.txt (LOCKED before any read, on the audit" + APOS + "s own exit code);" + Q + "\n"
    "     " + Q + " the source pinned at b358, data/b358_source_lagarias0404394.txt;" + Q + "\n"
    "     " + Q + " PLACE-papers FACES_LEDGER.md (row U1, an appended UPDATE BLOCK); CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('H-NGEK', 'the held item', 'the index condition', 'the archimedean index condition',
           'the absolute constant', 'the vacuous condition')
MUST_NOT_HIT = ('the tail is closed', 'the circularity is removed',
                'the value is quoted from the source', 'H-CUSP is decided')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b361 -- THE INDEX KEY. ### THE HELD ITEM, DECIDED.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'index-condition-decided'" in txt)
    have_row = ('"index-condition-decided"' in txt)
    print('  index-condition-decided key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('index-condition-decided')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : index-condition-decided returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'index-condition-decided' in o
        ok = ok and g
        print('    %-44s reaches the b361 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTDECIDED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'IS NOT A CLOSED TAIL' in out and 'NO' in out and 'UNCONDITIONAL BOUND AT ALL' in out
    a2 = 'THE CIRCULARITY FINDING IS UNTOUCHED' in out
    a3 = 'THE VALUE IS NOT QUOTED FROM THE SOURCE' in out and 'IDENTIFICATION' in out
    a4 = 'H-CUSP IS INHERITED AND NOT DECIDED' in out
    a5 = 'NO GRADE IS CONFERRED BY A SEAT' in out and 'A VACUOUS CONDITION IS NOT AN OBSTRUCTION REMOVED' in out
    ok = ok and a1 and a2 and a3 and a4 and a5
    print('    an index condition is not a closed tail                   : %s' % a1)
    print('    ### the circularity finding is untouched                  : %s' % a2)
    print('    ### the value is identified, not quoted                   : %s' % a3)
    print('    ### H-CUSP is inherited and not decided                   : %s' % a4)
    print('    ### no grade conferred, and a vacuous condition is not one: %s' % a5)
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
