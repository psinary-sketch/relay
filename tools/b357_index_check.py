# -*- coding: utf-8 -*-
"""b357_index_check.py -- ONE KEY, ONE ROW. ### READ BACK, AND THE OVERREADINGS PROBED.

### ### **WHAT THIS FILE IS, SAID PLAINLY:** ### the key and its aliases were appended to
### `tools/banked_index.py` BY EDIT, not by a generator, so this tool ### **WRITES NOTHING** ### and its
### whole job is the read-back and the arms below. ### `b356` used a generator; this act did not, and says
### so rather than shipping a generator that would only ever run in its no-op branch.
### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTSETTLED`.** ### A reader who asks *what the ledger read
### settled* must be handed: SOME ROWS SAY IT; the wider sentence is not necessarily false; the membership
### question is b355's `H1` and is still ROUTED; twelve hand-picked passages are not a census; and the
### correction is DRAFTED, not made.
### ### **`the ledgers are wrong`, `the class is settled`, `the checks are demoted` AND `the errata is
### filed` STAY UNKEYED.**
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

KEY = 'what-the-ledgers-certify'
ALIASES = ('what the ledgers say the checks certify', 'the wider sentence', 'the narrower sentence',
           'the attribution fault', 'what the checks certify', 'the ledger read', 'the errata draft',
           'the construction-confirming scan')
MUST_NOT_HIT = ('the ledgers are wrong', 'the class is settled',
                'the checks are demoted', 'the errata is filed')

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
    C = json.load(io.open(os.path.join(D, 'b357_read.json'), encoding='utf-8'))
    # ### **THE ROW NUMBER IS READ FROM THE TABLE, NOT FROM A RUN FILE**: the writing run was not
    # ### captured, and a number derived from the artefact itself is better evidence than one quoted
    # ### from a log. ### The marker is b357's own, so the match is unique or this tool fails.
    tbl = io.open(os.path.join(r'D:\SIDE-global-section', 'CORRESPONDENCE.md'), encoding='utf-8').read()
    hits = re.findall(r'^\| (\d+) \| THE LEDGERS DO SAY MORE THAN THE CHECKS ESTABLISHED',
                      tbl, re.M)
    if len(hits) != 1:
        print('  ### HARD FAILURE -- b357 row found %d times, 1 required.' % len(hits))
        return 2
    rownum = hits[0]
    rec('=' * 100)
    rec('b357 -- THE INDEX KEY. ### WHAT THE LEDGERS SAY THE CHECKS CERTIFY.')
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
        rec('    %-44s reaches the b357 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    rec('  ### ### **G-NOTSETTLED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'THE WIDER SENTENCE IS NOT NECESSARILY FALSE' in out
    a2 = 'THE MEMBERSHIP QUESTION IS NOT DECIDED' in out and 'ROUTED' in out
    a3 = 'ARE NOT A CENSUS' in out
    a4 = 'THE CORRECTION IS DRAFTED, NOT MADE' in out and 'NO CHECK IS DEMOTED' in out
    a5 = 'NO ROW IS EDITED' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3 and a4 and a5
    rec('    the answer says the wider sentence is not necessarily false      : %s' % a1)
    rec('    ### and that the membership question is undecided and routed     : %s' % a2)
    rec('    ### and that twelve hand-picked passages are not a census        : %s' % a3)
    rec('    ### and that the correction is drafted and nothing is demoted    : %s' % a4)
    rec('    ### and that no row is edited and no grade moved                 : %s' % a5)
    rec('  ### ### **AND THE FIGURES IN THE KEY ARE THE READING\'S OWN:**')
    f1 = ('%d WIDER / %d NARROWER / %d SILENT' % (C['n_wider'], C['n_narrower'], C['n_silent'])) in out
    f2 = ('THE ATTRIBUTION FAULT, %d rows' % len(C['attribution_fault'])) in out
    f3 = ('NO WARRANT NAMED, %d rows' % len(C['membership_only'])) in out
    f4 = ('CORRESPONDENCE.md row %s' % rownum) in out
    ok = ok and f1 and f2 and f3 and f4
    rec('    the 5/6/1 split : %s ; the 3 and the 2 : %s / %s ; row %s : %s' % (f1, f2, f3, rownum, f4))
    post = {}
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        post[q] = no_key(o)
        g = pre[q] and post[q]
        ok = ok and g
        rec('    %-44s NO KEY after  : %s  %s' % (q, post[q], 'PASS' if g else '### FAIL ###'))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    rec('=' * 100)
    p = run_clock.write(D, 'b357_index_run', LINES)
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
