# -*- coding: utf-8 -*-
"""b363_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTCURED`.** ### A reader who asks *what b363 settled*
### must be handed: a helper BUILT and found NARROWER than the rule it was proposed under; **7 OF 11, NOT
### ### NINE OR TEN**; a population of **ELEVEN AND NOT THIRTEEN**, counted from the banks; **TWO WRONG
### ### ARMS THE HELPER DOES NOT REACH** and **TWO ARMS THAT WERE RIGHT AND MUST NOT BE QUIETENED**;
### **NO ARM ACTUALLY RETIRED AND NO BANKED SUITE EDITED**; and a trail entry **FILED, NOT PAID**.
### ### **`the gate is cured`, `every arm is retired`, `a sharper instrument is a result` AND `a banked
### suite was edited` STAY UNKEYED**, each checked NO KEY before this file was written.
### ### **AND ONE ALIAS IS DELIBERATELY NOT CLAIMED:** ### `the needle` is left alone, because the needle
### species already has banked language of its own and an alias that collides with a banked key is a false
### hit waiting to happen.
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

CORR = io.open(os.path.join(D, 'b363_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
E = json.load(io.open(os.path.join(D, 'b363_reads.json'), encoding='utf-8'))
N = json.load(io.open(os.path.join(D, 'b363_census.json'), encoding='utf-8'))
T = json.load(io.open(os.path.join(D, 'b363_trail.json'), encoding='utf-8'))


def s(x):
    return str(x)


KEY_ANCHOR = 'KEYS = {\n'
KEY_NEW = (
    "    'anchored-gate-arms': ['the anchored gate arms', 'gate_needle', 'the anchored-arm helper',\n"
    "                           'the needle helper', 'the wrong arm', 'the gate arms counted'],\n"
)

ROW_ANCHOR = ('INDEX = [\n'
              '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')

ROW_NEW = (
    '    # ### THE ANCHORED GATE ARMS, COUNTED AND NOT ASSERTED (b363).\n'
    '    ("anchored-gate-arms", "b363 (a tool, a count and a filing; it computes nothing about the object)",\n'
    '     "BUILT AND FOUND NARROWER THAN THE RULE IT WAS PROPOSED UNDER. tools/gate_needle.py takes a typed hint, returns the FILE OWN LINE, and compares under a"\n'
    '     " normaliser both sides pass through, stripping marker runs WHEREVER THEY OCCUR and not only at line start -- seven fixtures, both polarities, including an"\n'
    '     " arm that SHOULD fire and still does. THE POPULATION IS COUNTED AND NOT TAKEN FROM THE DRAFT: the three acts own headline figures, located by the anchor"\n'
    '     " tool at their own banks, are FOUR, TWO and FIVE, summing to ' + s(N['headline_sum']) + '; ' + s(N['enumerated']) + ' arms were enumerated one by one, each pinned to the bank line that"\n'
    '     " describes it; AND THE TOOL REFUSES TO EMIT IF THE TWO DISAGREE. The draft claimed ' + s(N['draft_population']) + ' and was wrong about its own banks. THE HELPER WOULD HAVE REACHED"\n'
    '     " ' + s(N['retired']) + ' OF ' + s(N['enumerated']) + ', against the draft estimate of ' + s(N['draft_retirement']) + '. THE FOUR IT DOES NOT REACH SPLIT INTO TWO KINDS: TWO ARE WRONG ARMS (A3, A10), whose predicates test"\n'
    '     " something other than what their labels name, and TWO ARE MISSING SENTENCES (A6, A9), arms that were RIGHT. THE CONTROL IS THE BANKED SUITES, UNEDITED:"\n'
    '     " six copied, run, deleted in a finally, ' + s(N['copies_reproducing']) + ' OF ' + s(N['copies']) + ' reproducing their own act verdict, the exception (b357, G-LOCATED) reported at full prominence."\n'
    '     " THE HELPER WAS EXERCISED OVER ' + s(N['needles_declared']) + ' DECLARED NEEDLES: ' + s(N['needles_built']) + ' BUILT, ' + s(N['needles_refused']) + ' REFUSED. ' + s(E['reads']) + ' reads located, ' + s(E['anchors_differing']) + ' anchors differing from the hint that found them.",\n'
    '     "### A SHARPER INSTRUMENT IS NOT A RESULT. ### NO ARM WAS ACTUALLY RETIRED: the census says what the helper WOULD HAVE reached had it existed, and the"\n'
    '     " banked suites are byte-identical to what their acts left. ### NO BANKED SUITE WAS EDITED. ### 7 OF 11 IS NOT A RATE AND NOT A FORECAST -- it is a count"\n'
    '     " over eleven named arms in three named acts. ### THE HELPER DOES NOT REACH THE WRONG-ARM SPECIES, and the act says so rather than letting a fraction imply"\n'
    '     " it: A NEEDLE BUILT FROM A FILE IS STILL A NEEDLE FOR THE WRONG QUESTION. ### AND IT MUST NOT REACH A MISSING SENTENCE: a helper that quietened A6 or A9"\n'
    '     " would be a defect and not a cure. ### THE CLASSIFICATION IS DECLARED DATA AND NOT INFERRED FROM PROSE. ### THE TRAIL ENTRY IS FILED AND NOT PAID, AND"\n'
    '     " NAMING A READ IS NOT PERFORMING ONE. ### NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED. ### NO ACT IS RE-VERDICTED. ### NOTHING WAS COMPUTED"\n'
    '     " ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",\n'
    '     "data/b363_the_anchored_gate_arms.txt; data/' + T['run_file'] + '; data/' + N['run_file'] + '; data/' + E['run_file'] + ';"\n'
    '     " data/b363_registration_2026-09-07.txt (LOCKED before any write, on the audit own exit code);"\n'
    '     " tools/gate_needle.py (the shared helper); tools/b363_census.py (the count, the classification and the control);"\n'
    '     " PLACE-papers OPEN_TRAILS.md (' + T['entry'] + ', an append-only block; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row ' + R1 + '"),\n'
)

ALIASES = ('the anchored gate arms', 'gate_needle', 'the anchored-arm helper', 'the needle helper',
           'the wrong arm', 'the gate arms counted')
MUST_NOT_HIT = ('the gate is cured', 'every arm is retired', 'a sharper instrument is a result',
                'a banked suite was edited')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b363 -- THE INDEX KEY. ### THE ANCHORED GATE ARMS, COUNTED AND NOT ASSERTED.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'anchored-gate-arms'" in txt)
    have_row = ('"anchored-gate-arms"' in txt)
    print('  anchored-gate-arms key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('anchored-gate-arms')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : anchored-gate-arms returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'anchored-gate-arms' in o
        ok = ok and g
        print('    %-44s reaches the b363 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTCURED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'NARROWER THAN THE RULE IT WAS PROPOSED UNDER' in out and 'A SHARPER INSTRUMENT IS NOT A RESULT' in out
    a2 = 'NO ARM WAS ACTUALLY RETIRED' in out and 'NO BANKED SUITE WAS EDITED' in out
    a3 = 'TWO ARE WRONG ARMS' in out and 'STILL A NEEDLE FOR THE WRONG QUESTION' in out
    a4 = 'TWO ARE MISSING SENTENCES' in out and 'would be a defect and not a cure' in out
    a5 = 'FILED AND NOT PAID' in out and 'REFUSES TO EMIT IF THE TWO DISAGREE' in out
    ok = ok and a1 and a2 and a3 and a4 and a5
    print('    built and narrower, and a sharper instrument is not a result : %s' % a1)
    print('    ### no arm actually retired and no banked suite edited        : %s' % a2)
    print('    ### the wrong arms, and the limit that keeps them            : %s' % a3)
    print('    ### the missing sentences, and why quietening them is a defect: %s' % a4)
    print('    ### the trail filed not paid, and the census own refusal      : %s' % a5)
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
