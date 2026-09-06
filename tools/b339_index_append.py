# -*- coding: utf-8 -*-
"""b339_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOPREFERENCE`.** ### A reader who asks *was the exponent resolved* must be
### handed the price -- UNAFFORDABLE at the sealed ceiling at every covered cell, the price banked, no frame built --
### with the sentences that a price is not a prediction, that no candidate is preferred, and that the question stays
### UNDER-RESOLVED, NOT OPEN, by b322's rule. ### Every number is read from the price record at write time.
### ### **`the convention resolved` AND `the source's convention preferred` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b339_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
P = json.load(io.open(os.path.join(D, 'b339_price.json'), encoding='utf-8'))
c = P['cells']
PRICES = '; '.join('a = %s: X_req %.0f (ratio %.2f)' % (k, c[k]['x_req'], c[k]['x_req'] / 128.0) for k in sorted(c, key=float))

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'exponent-resolved': ['the exponent resolved', 'the exponent question', 'the exponent\\'s ratio', 'the exponent priced', 'the price of the exponent',\n"
    "                          'the resolving-power rule', 'the remainder\\'s convention', 'was the exponent resolved', 'unaffordable', 'the exponent unaffordable',\n"
    "                          'the two exponent candidates', 'the sealed ceiling', 'the price banked'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE EXPONENT PRICED (b339, leg 1 of the sortie b339-b343).\n"
    "    (\"exponent-resolved\", \"b339 (a pricing act under b322's sealed rule; no frame built)\",\n"
    "     \"THE EXPONENT PRICED: the domain the remainder instrument needs to split the two exponent candidates (rho ** +0.5, the source's; rho ** -0.5,\"\n"
    "     \" the corpus's) priced at every covered cell from b320's domain ladder and b321's separation -- the identity residual fitted by b322's fit_power,\"\n"
    "     \" the split criterion R <= s/2, the price X_req = 128 (R(128)/(s/2))^(1/p) -- against a ceiling X = 512 sealed before the price: " + PRICES + ".\"\n"
    "     \" UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL; THE PRICE BANKED; NO FRAME BUILT; NO REMAINDER EVALUATED AT A NEW DOMAIN. The side\"\n"
    "     \" reading on the same five frames puts the margin's limit above both candidates at every cell, so the price is an under-estimate and the floor is\"\n"
    "     \" what the next pricing must price.\",\n"
    "     \"### A PRICE IS NOT A PREDICTION. ### NO CANDIDATE PREFERRED. ### THE QUESTION STAYS UNDER-RESOLVED, NOT OPEN, BY b322's RULE. ### NO BAR MOVED.\"\n"
    "     \" ### THE ERRATUM E-2026-09-03-1 UNTOUCHED. ### NO TERMINAL. ### M-2 UNCHANGED\",\n"
    "     \"data/b339_the_exponent_resolved.txt; data/b339_price_run.txt; data/b339_price.json; data/b339_limit_run.txt; data/b339_registration_2026-09-06.txt\"\n"
    "     \" (sealed before the price); FACES_LEDGER.md (the b339 update, rows F2 and S1/K6); CORRESPONDENCE.md row " + R1 + "\"),\n"
)

ALIASES = ('the exponent resolved', 'the exponent question', "the exponent's ratio", 'the resolving-power rule', "the remainder's convention",
           'the price of the exponent', 'was the exponent resolved', 'the sealed ceiling', 'the price banked')
MUST_NOT_HIT = ('the convention resolved', "the source's convention preferred", 'the exponent measured')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b339 -- THE INDEX KEY. ### THE EXPONENT PRICED, UNAFFORDABLE AT THE SEALED CEILING.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'exponent-resolved'" in txt)
    have_row = ('"exponent-resolved"' in txt)
    print('  exponent-resolved    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('exponent-resolved')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : exponent-resolved returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'exponent-resolved' in o
        ok = ok and g
        print('    %-40s reaches the b339 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOPREFERENCE -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A PRICE IS NOT A PREDICTION' in out and 'NO CANDIDATE PREFERRED' in out
    a2 = 'UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL' in out and 'NO FRAME BUILT' in out
    a3 = "UNDER-RESOLVED, NOT OPEN, BY b322's RULE" in out and 'NO BAR MOVED' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says a price is not a prediction, no candidate preferred : %s' % a1)
    print('    ### and unaffordable at every covered cell, no frame built          : %s' % a2)
    print("    ### and under-resolved not open by b322's rule, no bar moved         : %s" % a3)
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        quiet = no_key(o)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s' % (q, quiet, pre[q], 'PASS' if good else '### FAIL ###'))
    import ferry_scan
    _c, sh = ferry_scan.scan_text(io.open(PATH, encoding='utf-8').read(), [], ferry_scan.stems())
    print('  ### THE INDEX SWEPT AFTER THE WRITE : %d stem hit(s)' % len(sh))
    ok = ok and not sh
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
