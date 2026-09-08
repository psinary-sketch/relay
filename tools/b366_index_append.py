# -*- coding: utf-8 -*-
"""b366_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTREPAIRED`.** ### A reader who asks *what b366 settled*
### must be handed: the counts; that the classification is ### **DECLARED, NOT INFERRED**; that the
### detector is ### **A NET OF THREE NAMED SHAPES AND NOT A DECISION PROCEDURE**; that ### **NO SUITE WAS
### ### EDITED AND NO DATED ARM WAS CURED**; that ### **NO RULING WAS MADE BY THIS SEAT**; and that the
### grade word is the author's, ### **APPLIED AND NOT CONFERRED.**
### ### **`the suites are repaired`, `the dated arms are cured`, `this seat ruled the threshold` AND `the
### detector decides` STAY UNKEYED**, each checked NO KEY before this file was written.
### ### **AND ONE ALIAS IS DELIBERATELY NOT CLAIMED:** ### `the dated arm` alone already reaches `b364`'s
### `dated-arm` key, and the two are the DIAGNOSIS and the SWEEP. ### **AN ALIAS THAT COLLAPSED THEM WOULD
### ### HAND A READER ONE ACT WHEN THEY ASKED FOR THE OTHER.**
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

CORR = io.open(os.path.join(D, 'b366_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
E = json.load(io.open(os.path.join(D, 'b366_reads.json'), encoding='utf-8'))
S = json.load(io.open(os.path.join(D, 'b366_sweep.json'), encoding='utf-8'))
F = json.load(io.open(os.path.join(D, 'b366_faces_row.json'), encoding='utf-8'))
M = json.load(io.open(os.path.join(D, 'b366_mint.json'), encoding='utf-8'))


def s(x):
    return str(x)


KEY_ANCHOR = 'KEYS = {\n'
KEY_NEW = (
    "    'dated-arm-sweep': ['the dated-arm sweep', 'the rewrite rule', 'gate_content',\n"
    "                       'the standing check', 'address predicate'],\n"
)

ROW_ANCHOR = ('INDEX = [\n'
              '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')

ROW_NEW = (
    '    # ### THE DATED-ARM SWEEP (b366).\n'
    '    ("dated-arm-sweep", "b366 (a classification and a rule; it repairs nothing and rules nothing)",\n'
    '     "' + s(S['dated']) + ' DATED ARMS IN THE WHOLE RECORD, OUT OF ' + s(S['arms']) + ' ARMS ACROSS ' + s(S['suites']) + ' GATE SUITES, and ' + s(S['one_substitution']) + ' of the ' + s(S['dated']) + ' are ONE SUBSTITUTION FROM STANDING. The third is not harder to"\n'
    '     " write -- IT IS MISSING ITS CONTENT: its act banked a line number and not the text found there, so there is nothing to look the content up BY. THE SPECIES IS REAL, IT IS CONFIRMED, AND IT IS"\n'
    '     " NOT A CLASS THIS RECORD IS RIDDLED WITH. The classification is by the author ruling (R2): an arm on the act own artifacts is STANDING and must reproduce; an arm on the living record is a"\n'
    '     " MOMENT CERTIFICATE unless written by CONTENT rather than by ADDRESS. THE COUNT IS MECHANICAL AND THE CLASSIFICATION IS DECLARED, arm by arm with the code line printed beside it, because a"\n'
    '     " detector cannot decide whether the file being indexed is the act own artifact or the living record -- that is a question about what a computed path names. ' + s(S['flagged']) + ' lines flagged: ' + s(S['dated']) + ' DATED,"\n'
    '     " ' + s(S['standing']) + ' ADDRESS-SHAPED BUT STANDING (an act indexing its own frozen extraction -- the case that shows the classification cannot be left to a detector), and ' + s(S['not_address']) + ' not address predicates at all."\n'
    '     " THE DETECTOR FOUND THE ONE CONFIRMED INSTANCE THE RECORD HOLDS, b357 G-LOCATED diagnosed at b364. AND THE REWRITE RULE FELL ON THE HELPER SIDE OF THE ORDER OWN TEST: the substitution is one"\n'
    '     " call, tools/gate_content.py, with six fixtures in both polarities. ' + s(E['reads']) + ' reads located, ' + s(E['anchors_differing']) + ' anchors differing from the hint that found them.",\n'
    '     "### A CLASSIFICATION IS NOT A CURE. ### NO SUITE IS EDITED AND NO DATED ARM IS CURED BY THIS ACT -- a rewrite RULE is a thing a later act applies, and suite files differing from their"\n'
    '     " committed blobs: 0. ### NO PAST VERDICT IS WITHDRAWN AND NO ACT IS RE-VERDICTED: b363 control is RELABELLED as having measured drift on its dated arms and correctness on its standing ones,"\n'
    '     " which is not the same thing. ### NO RULING IS MADE BY THIS SEAT: R1, R2 and R3 are the author own and this act executes them. ### THE DETECTOR IS A NET OF THREE NAMED SHAPES AND IS NOT A"\n'
    '     " DECISION PROCEDURE -- an address predicate written in a shape it does not name would not be found. ### THE COUNT IS OF ARMS THE SUITES REGISTER UNDER A NAME, and ' + s(S['unattributed']) + ' registrations whose"\n'
    '     " name is not a literal are reported as UNATTRIBUTED rather than folded in. ### NO GRADE IS CONFERRED BY A SEAT: (R3) word is the author own, APPLIED and not conferred, and it grades the"\n'
    '     " ARCHIMEDEAN half and nothing else. ### NO PROOF IS VERIFIED. ### b358 CIRCULARITY FINDING IS UNTOUCHED. ### NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NO FACE IS PROMOTED. ### NO COORDINATE"\n'
    '     " IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",\n'
    '     "data/b366_the_dated_arm_sweep.txt; data/' + S['run_file'] + '; data/' + E['run_file'] + '; data/' + F['run_file'] + '; data/' + M['run_file'] + ';"\n'
    '     " data/b366_registration_2026-09-07.txt (LOCKED before any write, on the audit own exit code, with the pre-lock survey declared on its face);"\n'
    '     " tools/b366_sweep.py (the count, the detector and the declared classification); tools/gate_content.py (the rewrite rule, six fixtures, both polarities);"\n'
    '     " TECHNE-Core ' + M['module'] + ' (local-only at ' + M['techne_head'] + ', NOT pushed; kept BESIDE modules/2026-09/WRONG_ARM.md and not inside it);"\n'
    '     " PLACE-papers FACES_LEDGER.md (row ' + F['row'] + ', an UPDATE BLOCK through the ledger own writer, applying (R3)); CORRESPONDENCE.md row ' + R1 + '"),\n'
)

ALIASES = ('the dated-arm sweep', 'the rewrite rule', 'gate_content', 'the standing check',
           'address predicate')
MUST_NOT_HIT = ('the suites are repaired', 'the dated arms are cured', 'this seat ruled the threshold',
                'the detector decides')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b366 -- THE INDEX KEY. ### THE DATED-ARM SWEEP.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    coll, _rc = query('the dated arm')
    print('    ### the alias NOT claimed, and why : `the dated arm` reaches b364 DIAGNOSIS key, and this')
    print('    ### act is the SWEEP : %s' % ('dated-arm' in coll))
    have_key = ("'dated-arm-sweep'" in txt)
    have_row = ('"dated-arm-sweep"' in txt)
    print('  dated-arm-sweep key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('dated-arm-sweep')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : dated-arm-sweep returns %d row(s), 1 required  %s'
          % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'dated-arm-sweep' in o
        ok = ok and g
        print('    %-44s reaches the b366 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTREPAIRED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'NO SUITE IS EDITED AND NO DATED ARM IS CURED' in out and 'blobs: 0' in out
    a2 = 'NO RULING IS MADE BY THIS SEAT' in out
    a3 = 'NOT A' in out and 'DECISION PROCEDURE' in out
    a4 = 'APPLIED and not conferred' in out and 'NO GRADE IS CONFERRED BY A SEAT' in out
    a5 = 'RELABELLED' in out and 'NO PROOF IS VERIFIED' in out
    ok = ok and a1 and a2 and a3 and a4 and a5
    print('    no suite edited and no dated arm cured                      : %s' % a1)
    print('    ### no ruling made by this seat                             : %s' % a2)
    print('    ### the detector is not a decision procedure                : %s' % a3)
    print('    ### the grade applied and not conferred                     : %s' % a4)
    print('    ### the relabelling, and no proof verified                  : %s' % a5)
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
