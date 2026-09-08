# -*- coding: utf-8 -*-
"""b364_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOREPAIR`.** ### A reader who asks *what b364 settled*
### must be handed: the branch **REAL**; **THE COPY WAS INNOCENT**; the arm **DATED, NOT WRONG**; the half
### that still holds and the half that cannot; ### **NO VERDICT WITHDRAWN, NO ACT RE-VERDICTED, NO ARM
### ### REPAIRED, NO SUITE EDITED**; and **NO CURE PROPOSED**.
### ### **`the arm is repaired`, `the banked verdict is withdrawn`, `b357 is re-verdicted` AND `the copy
### was at fault` STAY UNKEYED**, each checked NO KEY before this file was written.
### ### **AND ONE ALIAS IS DELIBERATELY NOT CLAIMED:** ### `the wrong arm` already reaches `b363`'s key,
### and a dated arm is NOT a wrong arm. ### **AN ALIAS THAT COLLIDES WITH A BANKED KEY IS A FALSE HIT
### ### WAITING TO HAPPEN, AND ONE THAT COLLAPSES TWO SPECIES IS WORSE.**
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

CORR = io.open(os.path.join(D, 'b364_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
E = json.load(io.open(os.path.join(D, 'b364_reads.json'), encoding='utf-8'))
J = json.load(io.open(os.path.join(D, 'b364_diagnose.json'), encoding='utf-8'))
F = json.load(io.open(os.path.join(D, 'b364_filing.json'), encoding='utf-8'))
MOVED = '; '.join('%s %d to %d' % (a, b, c) for a, b, c in F['moved'])
LOC = re.search(r'rows re-located at their ledgers : \d+ of \d+ ; unclassified : \d+',
                J['home_section']).group(0)


def s(x):
    return str(x)


KEY_ANCHOR = 'KEYS = {\n'
KEY_NEW = (
    "    'dated-arm': ['the dated arm', 'a dated arm', 'the copy that did not reproduce',\n"
    "                  'G-LOCATED', 'the arm that no longer holds'],\n"
)

ROW_ANCHOR = ('INDEX = [\n'
              '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')

ROW_NEW = (
    '    # ### THE COPY THAT DID NOT REPRODUCE, DIAGNOSED AND NOT REPAIRED (b364).\n'
    '    ("dated-arm", "b364 (a diagnosis; it repairs nothing and decides nothing that is the author own)",\n'
    '     "THE COPY WAS INNOCENT AND THE BRANCH IS ' + s(J['branch']) + '. b363 found b357 copy reporting a failing gate where b357 banked none. b364 ran the BANKED SUITE tools/b357_checks.py AT ITS OWN"\n'
    '     " LOCATION, UNEDITED, and it reports the same GATES FAILING : ' + s(J['home_failing']) + ' ' + s(J['home_names']) + ' -- the same arm and the same four rows. THE FAILURE HAS NOTHING TO DO WITH COPYING, PATHS OR A"\n'
    '     " WORKING DIRECTORY. THE PREDICATE IS QUOTED FROM ITS OWN SUITE AND NOT PARAPHRASED (' + s(E['predicate_lines']) + ' lines located by the anchor tool). THE ARM CERTIFIES TWO THINGS AND ONLY ONE HAS"\n'
    '     " FAILED: (a) that every row b357 classified is still findable at its own ledger NOW, located by the row OWN TEXT -- ' + LOC + '; and (b) that any row whose LINE NUMBER moved is"\n'
    '     " declared in b357 own bank with both numbers -- and THAT HALF CANNOT HOLD AND CANNOT BE MADE TO, because it compares a number computed now against a literal in a bank written once, in an"\n'
    '     " append-only file that may never be edited. ' + s(len(F['moved'])) + ' rows have moved: ' + MOVED + '. b357 declared two of them itself, the ones its own index append caused, and could not"\n'
    '     " declare the rest. THE SPECIES IS NAMED: A DATED ARM -- an arm whose pass condition is a literal in a frozen file, compared against a quantity recomputed at every run, is dated by"\n'
    '     " construction; it does not become wrong, it becomes old. ' + s(E['reads']) + ' reads located, ' + s(E['anchors_differing']) + ' anchors differing from the hint that found them.",\n'
    '     "### A DIAGNOSIS IS NOT A CURE. ### NO VERDICT IS WITHDRAWN AND NO ACT IS RE-VERDICTED: b357 verdict was true when it was banked, and what is recorded is that RE-RUNNING that suite today"\n'
    '     " no longer reproduces it, and why. ### NO ARM IS REPAIRED AND NO SUITE, BANK, INDEX OR RUN FILE IS EDITED -- diagnose, do not repair-to-pass, and every file read is proved byte-identical to"\n'
    '     " its committed blob at both ends. ### b357 FINDING IS UNTOUCHED: which passages say what, and the 5 wider / 6 narrower / 1 silent split, rest on the half that still holds at every row."\n'
    '     " ### A DATED ARM IS NOT A WRONG ARM: a wrong arm was wrong the day it was written and a dated arm was right the day it was written, and they need different cures. ### NO CURE IS PROPOSED:"\n'
    '     " the filing names the author choices and prefers none. ### THE OTHER FIVE SUITES WERE NOT AUDITED for arms of this shape and are not claimed clean. ### THE ABSOLUTE-PATH WORK-ORDER IS NOT"\n'
    '     " RESTATED, because this is not its incident. ### NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NO GRADE IS CONFERRED BY A SEAT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED."\n'
    '     " ### THE CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",\n'
    '     "data/b364_the_copy_that_did_not_reproduce.txt; data/' + J['run_file'] + '; data/' + F['run_file'] + '; data/' + E['run_file'] + ';"\n'
    '     " data/b364_registration_2026-09-07.txt (LOCKED before any read of the suite and before any run of it, on the audit own exit code);"\n'
    '     " tools/b364_diagnose.py (the predicate, both runs and the unchanged bar); tools/b364_filing.py (the filing);"\n'
    '     " PLACE-papers OPEN_TRAILS.md (' + F['entry'] + ', an append-only block; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row ' + R1 + '"),\n'
)

ALIASES = ('the dated arm', 'a dated arm', 'the copy that did not reproduce', 'G-LOCATED',
           'the arm that no longer holds')
MUST_NOT_HIT = ('the arm is repaired', 'the banked verdict is withdrawn', 'b357 is re-verdicted',
                'the copy was at fault')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b364 -- THE INDEX KEY. ### THE COPY THAT DID NOT REPRODUCE, DIAGNOSED AND NOT REPAIRED.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    coll, _rc = query('the wrong arm')
    print('    ### the alias NOT claimed, and why : `the wrong arm` reaches b363 key and is a DIFFERENT')
    print('    ### species : %s' % ('anchored-gate-arms' in coll))
    have_key = ("'dated-arm'" in txt)
    have_row = ('"dated-arm"' in txt)
    print('  dated-arm key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('dated-arm')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : dated-arm returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'dated-arm' in o
        ok = ok and g
        print('    %-44s reaches the b364 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOREPAIR -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'THE COPY WAS INNOCENT' in out and 'AT ITS OWN' in out
    a2 = 'NO VERDICT IS WITHDRAWN AND NO ACT IS RE-VERDICTED' in out
    a3 = 'NO ARM IS REPAIRED' in out and 'IS EDITED' in out
    a4 = 'A DATED ARM IS NOT A WRONG ARM' in out
    a5 = 'NO CURE IS PROPOSED' in out and 'WERE NOT AUDITED' in out
    ok = ok and a1 and a2 and a3 and a4 and a5
    print('    the copy was innocent, and the suite was run where it lives  : %s' % a1)
    print('    ### no verdict withdrawn and no act re-verdicted              : %s' % a2)
    print('    ### no arm repaired and nothing edited                        : %s' % a3)
    print('    ### a dated arm is not a wrong arm                            : %s' % a4)
    print('    ### no cure proposed, and the other suites not audited        : %s' % a5)
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
