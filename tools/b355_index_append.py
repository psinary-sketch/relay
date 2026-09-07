# -*- coding: utf-8 -*-
"""b355_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTDEMOTED`.** ### A reader who asks *what the reading of the
### arrays settled* must be handed: the record STATES it, at the line where it makes them, with its reason; the
### consequence is A RELABELLING AND NOT A DEMOTION; every banked number stands and every check that passed
### still passed; and NO VERDICT IS MOVED. ### **`a measurement is wrong`, `the arrays are in the class`, `the
### corpus chose badly` AND `the verdicts are withdrawn` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b355_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)

Q = chr(34)
BS = chr(92)
APOS = BS + "'"

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'what-the-arrays-are': ['what the arrays are', 'the test functions', 'the piecewise-linear object',\n"
    "                           'the lawfulness checks', 'what the scan certifies', 'the three layers',\n"
    "                           'the relabelling', 'the smooth bump'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")

ROW_NEW = (
    "    # ### WHAT THE ARRAYS ARE (b355).\n"
    "    (" + Q + "what-the-arrays-are" + Q + ", " + Q + "b355 (a read and a filing; it computes nothing and moves nothing)" + Q + ",\n"
    "     " + Q + "THE RECORD DOES STATE WHAT ITS ARRAYS ARE, AT THE LINE WHERE IT MAKES THEM, WITH ITS REASON -- and b353, which graded the smoothness hypothesis" + Q + "\n"
    "     " + Q + " REFUTABLE and said the record did not settle it, did not look at that line. THREE LAYERS, EACH AT AN EMITTING LINE: the GENERATING FORMULA at" + Q + "\n"
    "     " + Q + " carto_atlas.py:49 is exp(-1/(1-t^2)) on the unit interval, the textbook Cc-infinity bump, so the formula the code writes down IS in the class;" + Q + "\n"
    "     " + Q + " the SAMPLED ARRAY at :45 and :50 is that formula at NV nodes divided by its own TRAPEZOID integral; and the OBJECT INTEGRATED at" + Q + "\n"
    "     " + Q + " b317_smear.py:136 is np.interp between nodes and zero outside, stated in words at :126 and given its reason at :128 -- the function this act" + Q + "\n"
    "     " + Q + " integrates is the function the corpus" + APOS + "s number was formed from. SO THE CHOICE WAS MADE FOR INTERNAL CONSISTENCY WITH BANKED NUMBERS AND NOT FOR" + Q + "\n"
    "     " + Q + " MEMBERSHIP IN THE SOURCE" + APOS + "S CLASS. H1 and H3 are answered SEPARATELY: H1 fails on what the object IS, H3 is undecided on how far the looking" + Q + "\n"
    "     " + Q + " went, and H3" + APOS + "s grade stands undisturbed. AND THE DISTINCTION FIXED BEFORE ANY CHECK WAS LOOKED AT: for a true autocorrelation the transform is" + Q + "\n"
    "     " + Q + " the squared modulus and positivity is AUTOMATIC, so A SCAN APPLIED TO AN OBJECT BUILT AS AN AUTOCORRELATION IS NOT AN INDEPENDENT TEST OF CLASS" + Q + "\n"
    "     " + Q + " MEMBERSHIP. The checks one by one: b320" + APOS + "s 13 of 13 USED BOTH; b320" + APOS + "s Theorem 1 conditions and covered-cell naming USED NEITHER; b328" + APOS + "s" + Q + "\n"
    "     " + Q + " lawfulness and every aimed seed at b334, b343, b344 and b349 USED BOTH. NO ACT IN THE FAMILY EVER TESTED CLASS MEMBERSHIP INDEPENDENTLY OF THE" + Q + "\n"
    "     " + Q + " CONSTRUCTION. VERDICT: THE RECORD STATES IT." + Q + ",\n"
    "     " + Q + "### A RELABELLING IS NOT A DEMOTION: every banked number stands exactly as banked, nothing here recomputes one or contradicts one, and every" + Q + "\n"
    "     " + Q + " check that passed still passed -- what changes is the sentence describing what passing established. ### THE OLD READING was that the seeds are" + Q + "\n"
    "     " + Q + " in the source" + APOS + "s class; THE READING THIS ACT SUPPORTS is that they are built as autocorrelations of a piecewise-linear interpolant of a sampled" + Q + "\n"
    "     " + Q + " smooth bump, and the scan confirms the discrete construction behaves like a continuous one within its reach. THE SECOND IS NARROWER AND IT IS" + Q + "\n"
    "     " + Q + " TRUE; THE FIRST WAS NEVER MEASURED. ### NOT that the two objects give different numbers -- NO ACT HAS MEASURED THE DIFFERENCE. ### NOT that the" + Q + "\n"
    "     " + Q + " corpus chose badly: it chose for a stated reason. ### NO VERDICT IS MOVED BY THIS ACT; whether any turns on the difference is a reading, and the" + Q + "\n"
    "     " + Q + " author moves rows. ### b353" + APOS + "s width sentence is CONFIRMED AND NOT STRENGTHENED and the partition stays UNDECIDED. ### NO CLASS IS DISCHARGED." + Q + "\n"
    "     " + Q + " ### THE CLAUSE HAS NOT MOVED. ### NO GRADE MOVED. ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b355_what_the_arrays_are.txt; data/b355_read_run2.txt; data/b355_extract_notes3.txt;" + Q + "\n"
    "     " + Q + " data/b355_registration_2026-09-07.txt (sealed before the reading was turned into a verdict);" + Q + "\n"
    "     " + Q + " tools/e16/carto_atlas.py:45,49,50; tools/b317_smear.py:126,128,136; CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('what the arrays are', 'the test functions', 'the piecewise-linear object',
           'the lawfulness checks', 'what the scan certifies', 'the three layers',
           'the relabelling', 'the smooth bump')
MUST_NOT_HIT = ('a measurement is wrong', 'the arrays are in the class',
                'the corpus chose badly', 'the verdicts are withdrawn')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b355 -- THE INDEX KEY. ### WHAT THE ARRAYS ARE.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-44s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'what-the-arrays-are'" in txt)
    have_row = ('"what-the-arrays-are"' in txt)
    print('  what-the-arrays-are key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('what-the-arrays-are')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : what-the-arrays-are returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'what-the-arrays-are' in o
        ok = ok and g
        print('    %-44s reaches the b355 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTDEMOTED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A RELABELLING IS NOT A DEMOTION' in out and 'every banked number stands' in out
    a2 = 'THE FIRST WAS NEVER MEASURED' in out
    a3 = 'NO VERDICT IS MOVED BY THIS ACT' in out and 'the author moves rows' in out
    a4 = 'NOT that the corpus chose badly' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3 and a4
    print('    the answer says a relabelling is not a demotion, and numbers stand : %s' % a1)
    print('    ### and that the wider sentence was never measured                  : %s' % a2)
    print('    ### and that no verdict is moved and the author moves rows          : %s' % a3)
    print('    ### and that the corpus did not choose badly, and no grade moved    : %s' % a4)
    post = {}
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        post[q] = no_key(o)
        g = pre[q] and post[q]
        ok = ok and g
        print('    %-44s NO KEY after  : %s  %s' % (q, post[q], 'PASS' if g else '### FAIL ###'))
    print('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
