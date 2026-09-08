# -*- coding: utf-8 -*-
"""b373_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTCHECKED`.** ### A reader who asks *what `b373`
### settled* must be handed: ### that ### **NO PIN WAS WRITTEN**; ### that the reason is
### ### **THE PAPERS ARE OLDER THAN THE INSTRUMENTS** ### and not a seat declining; ### that
### ### **NO GRADE WAS MOVED**; ### that ### **NO DEPOSITED OR ARCHIVED SURFACE WAS EDITED**; ### and
### that the graded-against-absent defect is ### **BOUNDED INSIDE THE TWELVE `b372` ALREADY FOUND.**
### ### **`the pins are added`, `the grades are corrected`, `the rows are checked` AND `the archive is
### ### updated` STAY UNKEYED**, each checked NO KEY before this file was written.
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

CORR = io.open(os.path.join(D, 'b373_corr_run.txt'), encoding='utf-8', errors='replace').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, P, S, Q, F = J('b373_reads'), J('b373_pins'), J('b373_status'), J('b373_desk'), J('b373_filing')
PCT = int(round(100.0 * P['located_act'] / max(1, P['rows'])))
NOACT = P['reasons'].get('WRITING ACT NOT NAMED', 0)


def s(x):
    return str(x)


KEY_ANCHOR = 'KEYS = {\n'
KEY_NEW = (
    "    'rule-outruns-record': ['the pins ruling', 'the sourcing rule', 'the status column',\n"
    "                           'cites at an unknown ref', 'the writing act'],\n"
)

ROW_ANCHOR = ('INDEX = [\n'
              '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')

ROW_NEW = (
    '    # ### THE PINS SOURCED FROM THE WRITING ACT, AND THE STATUS COLUMN LISTED (b373).\n'
    '    ("rule-outruns-record", "b373 (one ruling executed to exhaustion and writing nothing, one status sweep listed and routed, one licensed instrument corrected; it opens no kernel and moves no grade)",\n'
    '     "A RULE CAN OUTRUN THE RECORD IT REACHES INTO. Ruling (R9) says a citing row names a pin, sourced ONLY from the act that wrote the row and located in that act own bank, never from the current"\n'
    '     " head. It was executed over all ' + s(P['rows']) + ' pinless rows at ' + ('%.1f' % P['per_row']) + ' seconds a row, and IT WROTE NO PIN. Not because the price did not fit and not because the seat declined:"\n'
    '     " BECAUSE THE CHAIN THE RULING REQUIRES DOES NOT CLOSE. ' + s(P['located_act']) + ' of ' + s(P['rows']) + ' rows have a locatable writing act (' + s(PCT) + ' percent); ' + s(NOACT) + ' were introduced by commits whose subject names no"\n'
    '     " act at all; and the pins instrument that banks a kernel ref begins at b300, later than most rows that need one. THE PAPERS ARE OLDER THAN THE INSTRUMENTS. ' + s(P['pinnable']) + ' rows were PINNABLE and every"\n'
    '     " one of them sits on a deposited companion, an archived snapshot or an append-only ledger entry, which this seat will not rewrite on a citation-hygiene ruling. THE STATUS COLUMN: ' + s(S['defect']) + ' rows in"\n'
    '     " two documents assert a grade against a declaration this record has classified retired or absent, and EVERY ONE IS INSIDE THE TWELVE b372 ALREADY FLAGGED -- the sweep of ' + s(S['rows_scanned']) + ' table rows across"\n'
    '     " ' + s(S['files']) + ' files found no instance outside that set.",\n'
    '     "### NO PIN WAS WRITTEN TO ANY ROW AND NO PIN WAS TAKEN FROM ANY CURRENT HEAD. ### NO ROW WAS CHECKED AT ANY PIN: adding a pin dates a claim, it does not verify one, and no kernel was opened."\n'
    '     " ### NO GRADE WAS MOVED BY THIS SEAT; a seat that regrades is a seat that decided what was verified, and the author faces three named choices per row without one being chosen. ### NO DEPOSITED"\n'
    '     " FILE, NO ARCHIVED FILE AND NO APPEND-ONLY LEDGER ENTRY WAS EDITED -- a deposited companion edited here no longer matches what was deposited, an archive that changes is not an archive, and a"\n'
    '     " ledger row is a historical statement already dated by the act that wrote it; whether those surfaces should carry pins is ROUTED. ### A ROW NOBODY CAN DATE AND A ROW WHOSE KERNEL WAS NEVER"\n'
    '     " ROSTERED ARE NOT THE SAME PROBLEM and the reasons are kept apart. ### AN ARM THAT TESTS THE VALUE CANNOT TEST THE SOURCE: ' + s(P['equals_a_head']) + ' correctly-sourced pins equal a current head because their kernel"\n'
    '     " has not moved, and the locked bar forbids writing them; the bar was obeyed and the tension filed. ### THE THREE-WAY SPLIT IN THE STATUS SWEEP DECIDED ROWS: ' + s(S['corrected']) + ' state their own retirement and"\n'
    '     " ' + s(S['live_graded']) + ' grades a declaration b372 found ALIVE, and neither is the defect. ### NO KERNEL RE-CLASSIFIED. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### LEG 2 NOT BEGUN. ### NOTHING COMPUTED ABOUT THE"\n'
    '     " OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### M-2 UNCHANGED",\n'
    '     "data/b373_the_pins_and_the_status_column.txt; data/' + E['run_file'] + '; data/' + P['run_file'] + '; data/' + S['run_file'] + ';"\n'
    '     " data/' + Q['run_file'] + '; data/' + F['run_file'] + ';"\n'
    '     " data/b373_registration_2026-09-08.txt (LOCKED before any write of this act, on the audit own exit code);"\n'
    '     " tools/b373_pins.py (the sourcing chain, declared before it was run, with every link failure keeping its own name);"\n'
    '     " tools/b373_status.py (the grade sweep, with the three-way split drawn before the sweep ran); tools/b373_desk.py ((R7));"\n'
    '     " tools/b304_hooks.py (THE ONE LICENSED OWNER INSTRUMENT, corrected: the sentence b372 made false, with its caveat kept);"\n'
    '     " PLACE-papers OPEN_TRAILS.md (an append-only block; NO ROW IN ANY PAPER EDITED; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row ' + R1 + '"),\n'
)

ALIASES = ('the pins ruling', 'the sourcing rule', 'the status column', 'cites at an unknown ref',
           'the writing act')
MUST_NOT_HIT = ('the pins are added', 'the grades are corrected', 'the rows are checked',
                'the archive is updated')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b373 -- THE INDEX KEY. ### A RULE CAN OUTRUN THE RECORD IT REACHES INTO.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'rule-outruns-record'" in txt)
    have_row = ('"rule-outruns-record"' in txt)
    print('  rule-outruns-record key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('rule-outruns-record')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : rule-outruns-record returns %d row(s), 1 required  %s'
          % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'rule-outruns-record' in o
        ok = ok and g
        print('    %-44s reaches the b373 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTCHECKED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'IT WROTE NO PIN' in out
    a2 = 'THE PAPERS ARE OLDER THAN THE INSTRUMENTS' in out
    a3 = 'NO GRADE WAS MOVED BY THIS SEAT' in out
    a4 = 'NO DEPOSITED' in out and 'NO ARCHIVED FILE' in out
    a5 = 'INSIDE THE TWELVE b372 ALREADY FLAGGED' in out
    a6 = 'AN ARM THAT TESTS THE VALUE CANNOT TEST THE SOURCE' in out
    ok = ok and a1 and a2 and a3 and a4 and a5 and a6
    print('    no pin was written                                          : %s' % a1)
    print('    ### and the reason is the record, not a seat declining       : %s' % a2)
    print('    ### no grade was moved                                       : %s' % a3)
    print('    ### no deposited or archived surface was edited              : %s' % a4)
    print('    ### the graded-against-absent defect is bounded              : %s' % a5)
    print('    ### the bar tests the value, the ruling forbids the source   : %s' % a6)
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
