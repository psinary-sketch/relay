# -*- coding: utf-8 -*-
"""b372_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTCHECKED`.** ### A reader who asks *what `b372`
### settled* must be handed: ### that ### **NO ROW WAS REPAIRED AND NO PIN WAS ADDED**; ### that a
### pinless row was ### **CHECKED AT A HEAD AND THAT IS WEAKER**; ### that the README's three figures
### ### **COUNT ONE QUANTITY AT THREE REFS AND NONE NAMES ITS REF**; ### that the attribute fixes
### ### **WHAT THE NEXT CHECKOUT PRODUCES AND NOT THIS DISK**; ### and that the order's LABEL and its
### DESCRIPTION named different files.
### ### **`the rows are repaired`, `the pins are added`, `the disk is normalised` AND `the federation is
### ### audited` STAY UNKEYED**, each checked NO KEY before this file was written.
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

CORR = io.open(os.path.join(D, 'b372_corr_run.txt'), encoding='utf-8', errors='replace').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, A, RM, B, Q, F = (J('b372_reads'), J('b372_eol'), J('b372_readme'), J('b372_batch'),
                     J('b372_desk'), J('b372_filing'))
T = RM['table']
T0, T1, TH = T[0], T[1], T[-1]
TV = B['terminal_tally']
NPIN = len([r for r in B['rows'] if r['mode'] == 'AT-PIN'])
NHEAD = len([r for r in B['rows'] if r['mode'] == 'CHECKED-AT-HEAD'])
BADB = [k for k, v in A['before'].items() if not v['fresh_equals_blob']]


def s(x):
    return str(x)


KEY_ANCHOR = 'KEYS = {\n'
KEY_NEW = (
    "    'pin-is-a-date': ['the eol pin', 'the readme figures', 'the first batch',\n"
    "                     'checked at head', 'the row classification'],\n"
)

ROW_ANCHOR = ('INDEX = [\n'
              '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')

ROW_NEW = (
    '    # ### THE EOL PIN, THE README FIGURES, THE FIRST BATCH OF ROW CHECKS (b372).\n'
    '    ("pin-is-a-date", "b372 (one attribute written in two repositories, one README repaired, twelve rows classified and none repaired; it opens no kernel for a build and adds no pin)",\n'
    '     "A PIN IS A DATE THAT SURVIVES. The same three declarations -- no_conspiracy_twins, no_conspiracy_goldbach, no_conspiracy_sg -- are PRESENT at the pin a row names and RETIRED at the head, and the"\n'
    '     " rows citing them without a pin cannot say which they meant. Of the twelve flagged rows, ' + s(NPIN) + ' were opened AT A PIN and ' + s(NHEAD) + ' at the kernel live head under ruling (R8) and are marked"\n'
    '     " CHECKED-AT-HEAD, which is weaker than a pinned row check and the record says why. Across them ' + s(TV.get('RETIRED', 0)) + ' named terminals classify RETIRED, ' + s(TV.get('PRESENT', 0)) + ' PRESENT and ' + s(TV.get('ABSENT', 0)) + ' ABSENT; every RETIRED verdict"\n'
    '     " quotes the kernel own retirement ledger and none is an inference from absence. THE THREE README FIGURES DO NOT COUNT THREE DIFFERENT SCOPES: they count ONE QUANTITY -- Core zero-axiom terminals,"\n'
    '     " one per printed line -- AT THREE DIFFERENT REFS, and each was exact when it was written. At ' + s(T0['ref'][:7]) + ' the headline, the breakdown, the ratio and the shipped profile all read ' + s(T0['total']) + '; at"\n'
    '     " ' + s(T1['ref'][:7]) + ' all of them moved to ' + s(T1['total']) + ' except the headline, which was left behind; at the head the profile carries ' + s(TH['prints']) + '. AND NONE OF THE THREE NAMES THE REF IT HOLDS AT. THE"\n'
    '     " END-OF-LINE ATTRIBUTE IS NOW TRACKED IN ALL ' + s(len(A['after'])) + ' ROSTERED REPOSITORIES and a fresh checkout of the tracked guard equals its blob in every one; before this act it was ' + s(len(A['before']) - len(BADB)) + ' of ' + s(len(A['before'])) + ', and the two"\n'
    '     " that failed were exactly the two without the attribute.",\n'
    '     "### NO ROW WAS REPAIRED AND NO PIN WAS ADDED TO ANY ROW: (R8) makes the addition of pins a SEPARATE RULING, PRICED AND NOT ATTEMPTED, and the classification is the product. ### NO HEAD WAS"\n'
    '     " WRITTEN INTO A ROW; every head read is recorded in the act own bank and dated. ### A CHECK AT A HEAD IS WEAKER THAN A CHECK AT A PIN: a pinned check is reproducible by anyone who resolves the"\n'
    '     " pin, and a check at a head is true of a moving target and only as good as the date beside it. ### THE ORDER PRESENT TEST CANNOT BE FULLY SATISFIED IN EITHER KERNEL READ, BECAUSE NEITHER SHIPS A"\n'
    '     " PRINTED AXIOM PROFILE: a declaration found alive is recorded PRESENT with its profile NOT LOCATED and is not silently upgraded. ### THE ORDER LABEL AND ITS DESCRIPTION NAMED DIFFERENT FILES: the"\n'
    '     " label said the exclusion kernel README, which has one count line, no breakdown and ships no profile at all; the object was identified BY THE DESCRIPTION, because a description is checkable"\n'
    '     " against a file and a label is not, and NOTHING IN THE EXCLUSION KERNEL README WAS REPAIRED. ### THE FIGURE WAS REMOVED RATHER THAN RESTATED, and the layer census was PRESERVED VERBATIM AND"\n'
    '     " DATED to the ref it holds at; re-deriving that census at the head rewrites a claim and not a number and is ROUTED. ### THE ATTRIBUTE FIXES WHAT THE NEXT CHECKOUT PRODUCES AND NOT THIS DISK: no"\n'
    '     " repository was renormalised, no working file was deleted to force a checkout and no branch was created or reset. ### ' + s(len(BADB)) + ' rows the previous act counted as pinned carry something that LOOKS"\n'
    '     " LIKE A PIN AND IS NOT. ### NO LEAN FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED. ### NOTHING COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS"\n'
    '     " UNDECIDED. ### M-2 UNCHANGED",\n'
    '     "data/b372_the_first_batch.txt; data/' + E['run_file'] + '; data/' + A['run_file'] + '; data/' + RM['run_file'] + ';"\n'
    '     " data/' + B['run_file'] + '; data/' + Q['run_file'] + '; data/' + F['run_file'] + ';"\n'
    '     " data/b372_registration_2026-09-08.txt (LOCKED before any write of this act, on the audit own exit code);"\n'
    '     " tools/b372_eol.py (the attribute, asked of git and verified by a fresh checkout into a scratch directory, both polarities);"\n'
    '     " tools/b372_readme.py (what each figure counts, measured at the ref that introduced it); tools/b372_batch.py (the twelve rows, re-anchored by content and opened at pin or head);"\n'
    '     " tools/b372_desk.py ((R7), with every closure required to name a killing file resolved by its recorded clock);"\n'
    '     " relay/.gitattributes and SIDE-effects/.gitattributes (WRITTEN, the pre-existing path-scoped line PRESERVED); SIDE-global-section/README.md (REPAIRED, original in the bank);"\n'
    '     " PLACE-papers OPEN_TRAILS.md (an append-only block; NO ROW IN ANY PAPER EDITED; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row ' + R1 + '"),\n'
)

ALIASES = ('the eol pin', 'the readme figures', 'the first batch', 'checked at head',
           'the row classification')
MUST_NOT_HIT = ('the rows are repaired', 'the pins are added', 'the disk is normalised',
                'the federation is audited')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b372 -- THE INDEX KEY. ### A PIN IS A DATE THAT SURVIVES.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'pin-is-a-date'" in txt)
    have_row = ('"pin-is-a-date"' in txt)
    print('  pin-is-a-date key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('pin-is-a-date')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : pin-is-a-date returns %d row(s), 1 required  %s'
          % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'pin-is-a-date' in o
        ok = ok and g
        print('    %-44s reaches the b372 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTCHECKED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'NO ROW WAS REPAIRED AND NO PIN WAS ADDED' in out
    a2 = 'A CHECK AT A HEAD IS WEAKER THAN A CHECK AT A PIN' in out
    a3 = 'NONE OF THE THREE NAMES THE REF IT HOLDS AT' in out
    a4 = 'WHAT THE NEXT CHECKOUT PRODUCES AND NOT THIS DISK' in out
    a5 = 'NAMED DIFFERENT FILES' in out
    a6 = 'NEITHER SHIPS A' in out
    ok = ok and a1 and a2 and a3 and a4 and a5 and a6
    print('    no row repaired and no pin added                             : %s' % a1)
    print('    ### a check at a head is weaker, and why                     : %s' % a2)
    print('    ### none of the three figures names its ref                  : %s' % a3)
    print('    ### the attribute fixes the next checkout, not this disk     : %s' % a4)
    print('    ### the label and the description named different files      : %s' % a5)
    print('    ### neither kernel ships a printed profile                   : %s' % a6)
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
