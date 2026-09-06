# -*- coding: utf-8 -*-
"""b346_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTEXPLAINED`.** ### A reader who asks *what did the rate settle*
### must be handed: a resolving power is a property of the INSTRUMENT; the separation of one full power is EXACT BY
### CONSTRUCTION and was not measured; NO CONVENTION IS DECLARED CORRECT and b313's clause governs; the floor is NOT
### explained, one of its three origins having been priced and the other two named; the two evaluators SHARE an
### engine; and one of this act's own sealed uncertainty arms COLLAPSED and is tabled. ### **`the convention is
### correct`, `the floor is explained`, `b313 is superseded` AND `the exponent is settled` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b346_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
R = json.load(io.open(os.path.join(D, 'b346_rate.json'), encoding='utf-8'))
K = R['rate']
P = R['premise']

Q = chr(34)
BS = chr(92)
APOS = BS + "'"

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'exponent-by-rate': ['the exponent by rate', 'the decay rate', 'the even sector', 'the convention',\n"
    "                         'the rate separates the conventions', 'which convention the banked values carry',\n"
    "                         'the resolving power in the rate', 'the floor is present'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")


def s(x):
    return str(x)


ROW_NEW = (
    "    # ### THE EXPONENT BY RATE (b346).\n"
    "    (" + Q + "exponent-by-rate" + Q + ", " + Q + "b346 (a premise tested, then a different axis measured)" + Q + ",\n"
    "     " + Q + "THE EXPONENT BY RATE: b339 priced the split between the exponent" + APOS + "s two candidates BY VALUE and banked it UNAFFORDABLE, with a side reading" + Q + "\n"
    "     " + Q + " that the residual descends to a FLOOR. b346 TESTED that premise rather than assuming it: b339" + APOS + "s own sealed limit arithmetic puts the fitted" + Q + "\n"
    "     " + Q + " limit ABOVE BOTH candidates at every covered cell, and b344" + APOS + "s ladder converges in NY with the whole remaining travel from the corpus" + APOS + "s own" + Q + "\n"
    "     " + Q + " NY = 512 equal to " + ('%.4f' % P['frac']) + " of b339" + APOS + "s floor there. A FLOOR IS PRESENT, SO NO DOMAIN RESOLVES THE EXPONENT BY VALUE. Then a different axis:" + Q + "\n"
    "     " + Q + " the even sector" + APOS + "s decay along the ARGUMENT, where b315 measured the rate moving a full power while along the cutoff it does not move at all." + Q + "\n"
    "     " + Q + " The two conventions came from b313" + APOS + "s copy-maker unedited, on the " + s(len(K['cells'])) + " cells b264" + APOS + "s own second axis marked converged; their ratio is the" + Q + "\n"
    "     " + Q + " argument itself at every cell, so THE SEPARATION IN THE EXPONENT IS EXACTLY 1.0 AND IS EXACT BY CONSTRUCTION, NOT MEASURED. What was measured is" + Q + "\n"
    "     " + Q + " the instrument" + APOS + "s uncertainty in the rate, " + ('%.6e' % R['uncertainty']) + ", a resolving power of " + ('%.1f' % R['resolving_power']) + ", the noise-floor gate RESOLVED at both conventions." + Q + "\n"
    "     " + Q + " VERDICT: RESOLVED ON THIS AXIS. The local slope at the top of the converged window is " + ('%.9f' % R['slope_top']) + ", sitting " + ('%.3e' % R['d_corpus']) + " from the corpus" + APOS + "s" + Q + "\n"
    "     " + Q + " asymptote and " + ('%.3e' % R['d_source']) + " from the source" + APOS + "s: THE BANKED VALUES CARRY THE CORPUS" + APOS + "S OWN r ** -0.5, read from the values and from nothing else." + Q + "\n"
    "     " + Q + " The standing clause of E-2026-09-03-1 therefore acquires a MECHANICAL TEST, appended to ERRATA.md under a b346 mark with the entry byte-identical." + Q + ",\n"
    "     " + Q + "### A RESOLVING POWER IS A PROPERTY OF THE INSTRUMENT: it says the axis can tell two objects apart, and nothing about which of them the mathematics" + Q + "\n"
    "     " + Q + " requires. ### NO CONVENTION IS DECLARED CORRECT. b312 decided which function the corpus" + APOS + "s remainder is BY UNFOLDING DEFINITIONS, and b313" + APOS + "s clause" + Q + "\n"
    "     " + Q + " governs: the exponent is fixed by the source" + APOS + "s own definition of the object the corpus imported, and a rate is not a vote on that any more than" + Q + "\n"
    "     " + Q + " a residue was. ### THE FLOOR IS NOT EXPLAINED: one of its three named origins has been priced and the cut" + APOS + "s tau and the taper are named, not moved." + Q + "\n"
    "     " + Q + " ### THE TWO EVALUATORS SHARE AN ENGINE -- the prolate layer and the node counts, which b313" + APOS + "s copy-maker declares deliberately -- so independence" + Q + "\n"
    "     " + Q + " of the prolate solver is NOT certified. ### AND ONE OF THIS ACT" + APOS + "S OWN SEALED UNCERTAINTY ARMS COLLAPSED: a two-point drift-zero is algebraically" + Q + "\n"
    "     " + Q + " the local slope of those two points, so the second estimator became the first and (u2) was structurally zero; TABLED AND NOT REPAIRED, the sealed" + Q + "\n"
    "     " + Q + " file unedited, the understatement bounded by a labelled whole-window diagnostic giving a resolving power of " + ('%.1f' % K['resolving_whole']) + ". ### NO GRADE MOVED." + Q + "\n"
    "     " + Q + " ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b346_the_exponent_by_rate.txt; data/b346_rate_run.txt; data/b346_filings_run.txt;" + Q + "\n"
    "     " + Q + " data/b346_registration_2026-09-06.txt (sealed before one slope was fitted and before the flipped copy was run once);" + Q + "\n"
    "     " + Q + " data/b346_ruling_2026-09-06.txt (this act" + APOS + "s number and the author" + APOS + "s framing note); PLACE-papers ERRATA.md (the b346 block against E-2026-09-03-1);" + Q + "\n"
    "     " + Q + " CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('the exponent by rate', 'the decay rate', 'the even sector', 'the convention',
           'the rate separates the conventions', 'which convention the banked values carry',
           'the resolving power in the rate', 'the floor is present')
MUST_NOT_HIT = ('the convention is correct', 'the floor is explained', 'b313 is superseded', 'the exponent is settled')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print("b346 -- THE INDEX KEY. ### THE EXPONENT BY RATE.")
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-38s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'exponent-by-rate'" in txt)
    have_row = ('"exponent-by-rate"' in txt)
    print('  exponent-by-rate key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('exponent-by-rate')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : exponent-by-rate returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'exponent-by-rate' in o
        ok = ok and g
        print('    %-44s reaches the b346 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTEXPLAINED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A RESOLVING POWER IS A PROPERTY OF THE INSTRUMENT' in out and 'NO CONVENTION IS DECLARED CORRECT' in out
    a2 = 'THE FLOOR IS NOT EXPLAINED' in out and 'THE TWO EVALUATORS SHARE AN ENGINE' in out
    a3 = 'SEALED UNCERTAINTY ARMS COLLAPSED' in out and 'TABLED AND NOT REPAIRED' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says a resolving power is the instrument\'s, and no convention is correct : %s' % a1)
    print('    ### and the floor is not explained, and the two evaluators share an engine          : %s' % a2)
    print('    ### and one of its own arms collapsed and is tabled                                 : %s' % a3)
    post = {}
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        post[q] = no_key(o)
        g = pre[q] and post[q]
        ok = ok and g
        print('    %-38s NO KEY after  : %s  %s' % (q, post[q], 'PASS' if g else '### FAIL ###'))
    print('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
