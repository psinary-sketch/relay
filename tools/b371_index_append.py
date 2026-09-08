# -*- coding: utf-8 -*-
"""b371_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTCHECKED`.** ### A reader who asks *what `b371`
### settled* must be handed: ### that the count claim is ### **`STALE`, AND WAS EXACT WHEN WRITTEN**;
### that the rows are ### **LISTED AND NOT CHECKED**; ### that ### **A CLONE IS STILL NOT GUARDED**;
### that the kernel's `README` is ### **ROUTED, NOT REPAIRED**; ### and that the desk ### **CLOSED
### ### WITHOUT RE-VERDICTING THE THREE ACTS THAT WERE FORBIDDEN TO.**
### ### **`the rows are checked`, `the clone is guarded`, `the readme is repaired` AND `the federation
### is audited` STAY UNKEYED**, each checked NO KEY before this file was written.
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

CORR = io.open(os.path.join(D, 'b371_corr_run.txt'), encoding='utf-8', errors='replace').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
E = json.load(io.open(os.path.join(D, 'b371_reads.json'), encoding='utf-8'))
S = json.load(io.open(os.path.join(D, 'b371_settle.json'), encoding='utf-8'))
RP = json.load(io.open(os.path.join(D, 'b371_repair_desc.json'), encoding='utf-8'))
I = json.load(io.open(os.path.join(D, 'b371_inventory.json'), encoding='utf-8'))
H = json.load(io.open(os.path.join(D, 'b371_hookpath.json'), encoding='utf-8'))
Q = json.load(io.open(os.path.join(D, 'b371_desk.json'), encoding='utf-8'))
F = json.load(io.open(os.path.join(D, 'b371_filing.json'), encoding='utf-8'))


def s(x):
    return str(x)


KEY_ANCHOR = 'KEYS = {\n'
KEY_NEW = (
    "    'count-claim-stale': ['the count claim', 'the first target', 'the row inventory',\n"
    "                         'the desk closes', 'the hook made durable'],\n"
)

ROW_ANCHOR = ('INDEX = [\n'
              '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')

ROW_NEW = (
    '    # ### THE FIRST TARGET SETTLED, THE DESK CLOSED, THE GUARD MOVED (b371).\n'
    '    ("count-claim-stale", "b371 (one settling, one inventory listed and not checked, one guard moved to a tracked path; it opens no kernel for any row and runs no build)",\n'
    '     "THE ONE CONFIRMED LIVE CLAIM IS ' + s(S['verdict']) + ', AND IT WAS EXACT WHEN IT WAS WRITTEN. The construction kernel public description named a Core figure of ' + s(S['figure']) + '; the printed profile carried exactly"\n'
    '     " that at tag ' + s(S['tag']) + '; the repository is ' + s(S['head_ahead_of_tag']) + ' commits past that tag and its profile now carries ' + s(S['prints_at_head']) + '. THE TEST WAS FIXED BEFORE THE READ: SCOPE-DEPENDENT requires that the"\n'
    '     " two words count DIFFERENT THINGS, and STALE is what remains when they count THE SAME THING AT DIFFERENT REFS. They count the same thing -- the zero-axiom print count of Core -- so the verdict is"\n'
    '     " STALE and not scope-dependent. AND THE ARITHMETIC COINCIDENCE IS REPORTED AS A COINCIDENCE AND NOT PROMOTED TO A SCOPE: the record names summands that add to the figure, but they are the"\n'
    '     " composition of the tag own count, not a subset of a larger present one. THE DESCRIPTION CARRIED NO REF, TAG, VERSION OR DATE AT ALL, which is why the figure read as current. It is repaired, the"\n'
    '     " original preserved in the bank because a description has no history. THE DESK CLOSED FOR THE FIRST TIME under (R7): ' + s(Q['items']) + ' items swept, ' + s(Q['closed']) + ' closed, ' + s(Q['standing']) + ' standing, ' + s(Q['closures_refused']) + ' closures refused for want"\n'
    '     " of a killing file. SCAFFOLD-TERMINALS is CLOSED after b157, b367, b368 and b369. THE GUARD IS ' + s(H['outcome']) + ': .githooks/pre-push, TRACKED, in each of the ' + s(len(H['repos'])) + ' rostered repositories, exercised in both"\n'
    '     " polarities with ' + s(len(H['failing'])) + ' failing. THE ROW INVENTORY: ' + s(I['rows']) + ' rows name a kernel and a terminal, ' + s(I['with_pin']) + ' with a pin and ' + s(I['without_pin']) + ' with none, across ' + s(I['files']) + ' tracked markdown files.",\n'
    '     "### THE ROWS ARE LISTED AND NOT CHECKED: ROWS CHECKED ' + s(I['rows_checked']) + ', KERNELS OPENED ' + s(I['kernels_opened']) + ', and the sweep claims no completeness because a row whose pin is written in a shape the predicate does"\n'
    '     " not know is reported PINLESS. ### A ROW WITHOUT A PIN CANNOT BE CHECKED THE WAY (R6) SPECIFIES, which checks a row at the kernel and pin the row itself names -- a finding, not a hole in the"\n'
    '     " sweep. ### ' + s(I['flagged_count']) + ' rows name a declaration this record has already classified absent: a CROSS-REFERENCE against a banked finding and NOT A CHECK, and a row so flagged is not thereby wrong. ###"\n'
    '     " ONE OF THE ORDER THREE RANKING FACTORS CANNOT BE FILLED WITHOUT OPENING A KERNEL, so it is recorded NOT FILLED for every row. ### A CLONE IS NOT GUARDED: core.hooksPath is local config in an"\n'
    '     " untracked .git/config, so a clone carries the guard and still needs one command; MADE DURABLE is the order word for what was done, not a claim that it is done. THE OLD LOCATION IS LEFT INERT --"\n'
    '     " a safety net and a trap. ### THE KERNEL OWN README IS NOT REPAIRED: its headline says ' + s(S['readme_headline']) + ', its own breakdown sums to ' + s(S['readme_breakdown_sum']) + ', its ratio says ' + s(S['readme_ratio'][0]) + '/' + s(S['readme_ratio'][1]) + ', and the profile it ships"\n'
    '     " carries ' + s(S['prints_at_head']) + ' -- ROUTED, and it is the SHARPER half because the README travels with a clone and the description does not. ### THE GUARD OWN FRONT MATTER IS NOT REPAIRED EITHER: moving the guard"\n'
    '     " made its install line wrong, and an act auditing stale surfaces made one. ### NO ITEM CLOSED WITHOUT ITS KILLING FILE AND DATE, and one closure is flagged because its killing file is this act"\n'
    '     " own. ### NO ACT IS RE-VERDICTED: (R7) reverses a disposition b368, b369 and b370 each carried, and each obeyed the rule it was given -- the author changed the rule. ### NO LEAN FILE TOUCHED, NO"\n'
    '     " BUILD RUN, NO AXIOM PROFILE RECOMPUTED. ### NOTHING COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### M-2 UNCHANGED",\n'
    '     "data/b371_the_first_target.txt; data/' + E['run_file'] + '; data/' + S['run_file'] + '; data/' + RP['run_file'] + ';"\n'
    '     " data/' + I['run_file'] + '; data/' + H['run_file'] + '; data/' + Q['run_file'] + '; data/' + F['run_file'] + ';"\n'
    '     " data/b371_registration_2026-09-08.txt (LOCKED before any write of this act, on the audit own exit code);"\n'
    '     " tools/b371_settle.py (the two refs, the deciding equality and the coincidence refused); tools/b371_inventory.py (the declared predicate, the sweep and the price);"\n'
    '     " tools/b371_hookpath.py (the guard moved to a tracked path and exercised); tools/b371_desk.py ((R7), with every closure required to name a killing file);"\n'
    '     " SIDE-global-section public DESCRIPTION (repaired; original preserved in the bank) and .githooks/pre-push (NEW, TRACKED); tools/b304_hooks.py (the one licensed owner instrument, following the guard);"\n'
    '     " PLACE-papers OPEN_TRAILS.md (SCAFFOLD-TERMINALS CLOSED, an append-only block; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row ' + R1 + '"),\n'
)

ALIASES = ('the count claim', 'the first target', 'the row inventory', 'the desk closes',
           'the hook made durable')
MUST_NOT_HIT = ('the rows are checked', 'the clone is guarded', 'the readme is repaired',
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
    print('b371 -- THE INDEX KEY. ### THE COUNT CLAIM, STALE.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'count-claim-stale'" in txt)
    have_row = ('"count-claim-stale"' in txt)
    print('  count-claim-stale key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('count-claim-stale')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : count-claim-stale returns %d row(s), 1 required  %s'
          % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'count-claim-stale' in o
        ok = ok and g
        print('    %-44s reaches the b371 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTCHECKED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'IT WAS EXACT WHEN IT WAS WRITTEN' in out
    a2 = 'LISTED AND NOT CHECKED' in out
    a3 = 'A CLONE IS NOT GUARDED' in out
    a4 = 'README IS NOT REPAIRED' in out
    a5 = 'NO ACT IS RE-VERDICTED' in out
    a6 = 'NOT A CHECK' in out
    ok = ok and a1 and a2 and a3 and a4 and a5 and a6
    print('    the claim was exact when written                             : %s' % a1)
    print('    ### the rows are listed and not checked                      : %s' % a2)
    print('    ### a clone is not guarded                                   : %s' % a3)
    print('    ### the README is routed, not repaired                       : %s' % a4)
    print('    ### no act is re-verdicted by the new rule                   : %s' % a5)
    print('    ### the cross-reference is not a check                       : %s' % a6)
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
