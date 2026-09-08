# -*- coding: utf-8 -*-
"""b367_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTREPAIRED`.** ### A reader who asks *what b367 settled*
### must be handed: ### **NOT LOCATED**; that the terminals are ### **RETIRED AND GONE** ### and the
### kernel says so itself; that ### **THE THREE ROUTES WERE NOT PRICED, CHOSEN OR RECOMMENDED**; that
### ### **NO LEAN FILE WAS WRITTEN AND NO BUILD WAS RUN**; and that the live defect found is ### **A STALE
### ### FRONT DOCUMENT, NOT A SCAFFOLD TERMINAL.**
### ### **`the terminals are replaced`, `a route is chosen`, `the scaffold is repaired` AND `the kernel
### was written` STAY UNKEYED**, each checked NO KEY before this file was written.
### ### **AND TWO ALIASES ARE DELIBERATELY NOT CLAIMED:** ### `not located` alone is too broad to be
### anything but a false hit, and `the exclusion kernel` names a repository rather than a finding.
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

CORR = io.open(os.path.join(D, 'b367_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
E = json.load(io.open(os.path.join(D, 'b367_reads.json'), encoding='utf-8'))
J = json.load(io.open(os.path.join(D, 'b367_locate.json'), encoding='utf-8'))
F = json.load(io.open(os.path.join(D, 'b367_filing.json'), encoding='utf-8'))
K = J['refs']['SIDE-effects']
G2 = J['refs'].get('SIDE-grh-transfer') or {}


def s(x):
    return str(x)


KEY_ANCHOR = 'KEYS = {\n'
KEY_NEW = (
    "    'scaffold-not-located': ['the scaffold terminals', 'grh_exclusion', 'no_ls_zero',\n"
    "                            'twist_cancels', 'the scaffold repair'],\n"
)

ROW_ANCHOR = ('INDEX = [\n'
              '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')

ROW_NEW = (
    '    # ### THE SCAFFOLD REPAIR, NOT LOCATED (b367).\n'
    '    ("scaffold-not-located", "b367 (a location and a read; it prices nothing, writes no Lean and runs no build)",\n'
    '     "' + s(J['verdict']) + '. The scaffold terminals do not exist. Searching the kernel own six .lean files at SIDE-effects ref ' + K['branch'] + ' = ' + K['head'] + ' for the names the ledger carries"\n'
    '     " -- grh_exclusion, twist_cancels, no_ls_zero -- gives ' + s(J['live_declarations']) + ' LIVE DECLARATIONS. There are ' + s(J['mentions']) + ' mentions and EVERY ONE IS INSIDE A COMMENT: Structural.lean own RETIREMENT LEDGER,"\n'
    '     " recording that they were removed and why. SIDE-grh-transfer at ref ' + G2.get('head', '?') + ' carries ' + s(J['grh_transfer_hits']) + ' occurrences. THE HINT WAS SCORED AGAINST WHAT WAS FOUND: the kernel and the"\n'
    '     " structural module CONFIRMED and the two subjects CONFIRMED as the ledger own headings, but THE BRANCH CLAUSE IS CORRECTED (the working head is main and is ahead of both feature branches, with"\n'
    '     " 0 branches carrying work the read ref lacks), THE COUNT IS CORRECTED (the ledger retires NINE framework consequences; the two subjects carry THREE named declarations), and THE"\n'
    '     " CHARACTERISATION trivially true IS CORRECTED BY THE KERNEL OWN DISTINCTION -- the audit separates True-valued stubs from opaque-Prop templates and files these two as opaque-Prop. THE HINT"\n'
    '     " NAMED THE RIGHT TERMINALS AND THE WRONG DEFECT. AND THE RECORD ALREADY FOUND THIS ON 2026-08-25 (b157). THE LIVE DEFECT IS NOT THE SCAFFOLD: the front document AGENTS.md exports ' + s(J['front_exported']) + ' named"\n'
    '     " theorems at Layer 1 of which ' + s(len(J['front_absent'])) + ' are ABSENT from the source, exactly b157 figure, unmoved. ' + s(E['reads']) + ' reads located, ' + s(E['anchors_differing']) + ' anchors differing from the hint that found them.",\n'
    '     "### NOT LOCATED IS A FULL VERDICT AND NOT A FAILURE OF THE SEARCH. ### THE THREE ROUTES ARE NOT PRICED, CHOSEN OR RECOMMENDED -- all three take the terminal as their input and there is no"\n'
    '     " terminal; the cap says NOT LOCATED stops the act. ### AND ROUTE (c) IS ALREADY WHAT HAPPENED: the kernel did not price deletion, it deleted, and the retirement ledger IS that route executed."\n'
    '     " ### NO LEAN FILE IS WRITTEN, NO TERMINAL REPLACED, NO STATEMENT PROVED, NO BUILD RUN, and not one byte of either kernel changed. ### NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF EITHER"\n'
    '     " SUBJECT: no statement was read, because the kernel holds none. ### THE RETIREMENT IS REPORTED, NOT ENDORSED. ### THE 18-OF-20 FIGURE IS A COUNT AGAINST THE KERNEL OWN SIX .lean FILES AND IS"\n'
    '     " NOT A CLAIM THAT THE KERNEL IS EMPTY. ### WHAT THE RECORD SANCTIONS IS REPORTED AND NOT RECOMMENDED: of INTERFACES it says this is a legitimate architecture, not a defect, and it uses it at"\n'
    '     " Route 3 own terminal; and ENCODES-CONCLUSION / SHELL is already classified a work-order, not a citation, so the ban on these two was never a special rule. ### NO ACT IS RE-VERDICTED: b157"\n'
    '     " finding is CONFIRMED AS STILL LIVE. ### NO GRADE IS CONFERRED BY A SEAT. ### NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE"\n'
    '     " CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",\n'
    '     "data/b367_the_scaffold_repair.txt; data/' + J['run_file'] + '; data/' + E['run_file'] + '; data/' + F['run_file'] + ';"\n'
    '     " data/b367_registration_2026-09-07.txt (LOCKED before any read of the kernel, on the audit own exit code);"\n'
    '     " tools/b367_locate.py (the refs, the live-vs-mention split, the front-document count and the bounded sweep);"\n'
    '     " SIDE-effects at ' + K['branch'] + ' = ' + K['head'] + ' and SIDE-grh-transfer at ' + G2.get('branch', '?') + ' = ' + G2.get('head', '?') + ', both READ and neither written;"\n'
    '     " PLACE-papers OPEN_TRAILS.md (' + F['entry'] + ' marked ' + F['status'] + ', an append-only block; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row ' + R1 + '"),\n'
)

ALIASES = ('the scaffold terminals', 'grh_exclusion', 'no_ls_zero', 'twist_cancels',
           'the scaffold repair')
MUST_NOT_HIT = ('the terminals are replaced', 'a route is chosen', 'the scaffold is repaired',
                'the kernel was written')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b367 -- THE INDEX KEY. ### THE SCAFFOLD REPAIR, NOT LOCATED.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'scaffold-not-located'" in txt)
    have_row = ('"scaffold-not-located"' in txt)
    print('  scaffold-not-located key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('scaffold-not-located')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : scaffold-not-located returns %d row(s), 1 required  %s'
          % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'scaffold-not-located' in o
        ok = ok and g
        print('    %-44s reaches the b367 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTREPAIRED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'NOT LOCATED IS A FULL VERDICT' in out
    a2 = 'NOT PRICED, CHOSEN OR RECOMMENDED' in out
    a3 = 'NO LEAN FILE IS WRITTEN' in out and 'not one byte of either kernel changed' in out
    a4 = 'NOTHING IS CLAIMED ABOUT THE MATHEMATICS' in out
    a5 = 'REPORTED AND NOT RECOMMENDED' in out and 'CONFIRMED AS STILL LIVE' in out
    ok = ok and a1 and a2 and a3 and a4 and a5
    print('    not located is a full verdict                                : %s' % a1)
    print('    ### no route priced, chosen or recommended                   : %s' % a2)
    print('    ### no Lean written and no byte of either kernel changed     : %s' % a3)
    print('    ### nothing claimed about the mathematics                    : %s' % a4)
    print('    ### the sanction reported not recommended, b157 still live   : %s' % a5)
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
