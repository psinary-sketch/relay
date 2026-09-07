# -*- coding: utf-8 -*-
"""b358_index_check.py -- ONE KEY, ONE ROW. ### READ BACK, AND THE OVERREADINGS PROBED.

### ### **WHAT THIS FILE IS, SAID PLAINLY:** ### the key and its aliases were appended to
### `tools/banked_index.py` BY EDIT, not by a generator, so this tool ### **WRITES NOTHING** ### and its
### whole job is the read-back and the arms below. ### `b356` used a generator; this act did not, and says
### so rather than shipping a generator that would only ever run in its no-op branch.
### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTCLOSED`.** ### A reader who asks *what the ledger read
### settled* must be handed: EXISTS BUT CIRCULAR; a located statement is not an applied one; five addresses
### are not a search of the literature; the five UNDECIDABLE grades are not permanent; and no coordinate is
### closed.
### ### **`the tail is closed`, `the asymptotic is unconditional`, `RH is proved` AND `the coordinate is
### closed` STAY UNKEYED.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

PATH = os.path.join(ROOT, 'tools', 'banked_index.py')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KEY = 'li-asymptotics-circular'
ALIASES = ('the li asymptotics', 'the li tail', 'the li coefficients asymptotic',
           'what would close the tail', 'the detection threshold', 'the finite range',
           'the circularity check', 'the two channels')
MUST_NOT_HIT = ('the tail is closed', 'the asymptotic is unconditional',
                'RH is proved', 'the coordinate is closed')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    C = json.load(io.open(os.path.join(D, 'b358_read.json'), encoding='utf-8'))
    # ### **THE ROW NUMBER IS READ FROM THE TABLE, NOT FROM A RUN FILE**: the writing run was not
    # ### captured, and a number derived from the artefact itself is better evidence than one quoted
    # ### from a log. ### The marker is b358's own, so the match is unique or this tool fails.
    tbl = io.open(os.path.join(r'D:\SIDE-global-section', 'CORRESPONDENCE.md'), encoding='utf-8').read()
    hits = re.findall(r'^\| (\d+) \| THE LITERATURE DOES CARRY AN ASYMPTOTIC', tbl, re.M)
    corr = re.findall(r'^\| (\d+) \| A CORRECTION ROW, BY THE AUTHOR', tbl, re.M)
    if len(hits) != 1 or len(corr) != 1:
        print('  ### HARD FAILURE -- act row %d time(s), R1 correction row %d time(s); 1 each required.'
              % (len(hits), len(corr)))
        return 2
    rownum, rowr1 = hits[0], corr[0]
    rec('=' * 100)
    rec('b358 -- THE INDEX KEY. ### WHAT THE LEDGERS SAY THE CHECKS CERTIFY.')
    rec('### ### **THIS TOOL WRITES NOTHING.** ### The key was appended by edit; this is the read-back.')
    rec('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        rec('    %-44s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'%s'" % KEY) in txt
    have_row = ('"%s"' % KEY) in txt
    rec('  %s key/row present : %s / %s' % (KEY, have_key, have_row))
    ok = have_key and have_row
    rec('  ### NOTHING WRITTEN. ### **THE READ-BACK ARMS STILL RUN.**')
    out, rc = query(KEY)
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n == 1
    ok = ok and good
    rec('  READ BACK : %s returns %d row(s), 1 required  %s' % (KEY, n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and KEY in o
        ok = ok and g
        rec('    %-44s reaches the b358 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    rec('  ### ### **G-NOTCLOSED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A STATEMENT LOCATED IS NOT A STATEMENT APPLIED' in out
    a2 = 'AN ABSENCE OF READING IS NOT AN ABSENCE OF LITERATURE' in out
    a3 = 'NOT A DISCOVERY ABOUT THE LITERATURE' in out
    a4 = 'NOT THAT THE FIVE UNDECIDABLE GRADES ARE PERMANENT' in out
    a5 = 'NO COORDINATE IS CLOSED' in out and 'THE PARTITION STAYS UNDECIDED' in out
    ok = ok and a1 and a2 and a3 and a4 and a5
    rec('    the answer says a located statement is not an applied one       : %s' % a1)
    rec('    ### and that an absence of reading is not one of literature      : %s' % a2)
    rec('    ### and that it is not a discovery about the literature          : %s' % a3)
    rec('    ### and that the five UNDECIDABLE grades are not permanent       : %s' % a4)
    rec('    ### and that no coordinate is closed, the partition undecided    : %s' % a5)
    rec('  ### ### **AND THE FIGURES IN THE KEY ARE THE READING\'S OWN:**')
    f1 = ('%d of %d statements are circular' % (len(C['circular']), len(C['statements']))) in out
    f2 = ('%d MET and %d UNDECIDABLE-FROM-THE-RECORD' % (
        sum(1 for h in C['hypotheses'].values() if h['axis2'] == 'MET'), C['n_undecidable_axis2'])) in out
    f3 = ('%.2e' % C['price_ratio']) in out
    f4 = ('rows %s and %s' % (rownum, rowr1)) in out
    ok = ok and f1 and f2 and f3 and f4
    rec('    4-of-7 circular : %s ; the 3 and the 5 on axis 2 : %s ; the ratio : %s ; rows %s and %s : %s'
        % (f1, f2, f3, rownum, rowr1, f4))
    post = {}
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        post[q] = no_key(o)
        g = pre[q] and post[q]
        ok = ok and g
        rec('    %-44s NO KEY after  : %s  %s' % (q, post[q], 'PASS' if g else '### FAIL ###'))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    rec('=' * 100)
    p = run_clock.write(D, 'b358_index_run', LINES)
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
