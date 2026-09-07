# -*- coding: utf-8 -*-
"""b347_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTEXPLAINED`.** ### A reader who asks *what did b347 settle* must
### be handed: a sharper instrument is NOT a result; the clock does NOT reach backwards; the audit's numerical limit
### is NAMED AND PRICED, NOT CLOSED; the gate MATCHES TEXT and cannot tell a floor from the words of one; NO PAST ACT
### IS RE-VERDICTED and no past copy of the flattener is edited; and this act's own registration fires on one of its
### own new arms and carries it. ### **`the audit is closed`, `the past acts are corrected`, `a sharper instrument is
### a result` AND `the clock dates the old runs` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b347_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
R = json.load(io.open(os.path.join(D, 'b347_repairs.json'), encoding='utf-8'))
C, Dd, E, F, G = R['C'], R['D'], R['E'], R['F'], R['G']

Q = chr(34)
BS = chr(92)
APOS = BS + "'"


def s(x):
    return str(x)


KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'bar-floor-rule': ['the bar-floor rule', 'the run file" + APOS + "s clock', 'the flattener', 'the two-routes rule',\n"
    "                      'the satisfiability audit" + APOS + "s limit', 'the standing clauses v2', 'the act-number clause',\n"
    "                      'a bar below its floor', 'arms that are one arm'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")

ROW_NEW = (
    "    # ### THE THREE REPAIRS AND THE TWO RULES (b347).\n"
    "    (" + Q + "bar-floor-rule" + Q + ", " + Q + "b347 (an instrument act; it decides nothing about the mathematics)" + Q + ",\n"
    "     " + Q + "THE BAR-FLOOR RULE, MINTED OVER BOTH SPECIES: a numerical bar is stated with the floor of the object it tests, and a bar below that floor is" + Q + "\n"
    "     " + Q + " UNINFORMATIVE RATHER THAN STRICT; and a bar with several arms is stated with what makes the arms independent, since arms that are algebraically one" + Q + "\n"
    "     " + Q + " arm are one arm. It is b322" + APOS + "s resolving-power rule one level down. Minted from two banked incidents: b345 sealed a fixture demanding 1e-25 of a" + Q + "\n"
    "     " + Q + " routine whose truncation left it a floor near 4.4e-18, so at its own threshold it rejected the correct copy too; b346 sealed an uncertainty whose" + Q + "\n"
    "     " + Q + " second estimator was algebraically its first, so one arm sat at machine level and another was structurally zero. Mechanized as two arms in" + Q + "\n"
    "     " + Q + " registration_gate.py beside the index-query arm, six fixtures in both polarities; the census over " + s(F['registrations']) + " registrations found " + s(F['would_fire']) + " that would fire and" + Q + "\n"
    "     " + Q + " " + s(F['clear']) + " clear, of which 276 carry nothing for the arms to look at. AND THE ACT DID NOT EXEMPT ITSELF: its own sealed registration fires on one arm and" + Q + "\n"
    "     " + Q + " carries it. THE OTHER TWO REPAIRS: run_clock.py gives a run file the instant it was written -- " + s(C['runs']) + " run files in the record carried none before it;" + Q + "\n"
    "     " + Q + " and gate_text.py repairs the flattener in one place, its reach measured statically at " + s(len(E['weakened'])) + " arm and reported as a LOWER BOUND. The satisfiability" + Q + "\n"
    "     " + Q + " audit" + APOS + "s numerical limit is named in its own output and PRICED at " + s(Dd['hand']) + " registrations of hand reading. FERRY_STANDING v2 written by its generator," + Q + "\n"
    "     " + Q + " counts re-measured live, the act-number clause in its own section marked AUTHOR-RULED, NOT MEASURED." + Q + ",\n"
    "     " + Q + "### A SHARPER INSTRUMENT IS NOT A RESULT, and nothing in this act decides anything about the mathematics: no frame built, no cell evaluated, no" + Q + "\n"
    "     " + Q + " object measured. ### THE CLOCK DOES NOT REACH BACKWARDS -- every run file written before it carries none and cannot be given one, and b345" + APOS + "s (E4)" + Q + "\n"
    "     " + Q + " stands exactly as b345 declared it. ### THE AUDIT" + APOS + "S NUMERICAL LIMIT IS NAMED AND PRICED, NOT CLOSED; no numerical checker is built. ### THE GATE" + Q + "\n"
    "     " + Q + " MATCHES TEXT and cannot tell a floor from the words of one -- a registration that writes UNPRICED beside every bar passes and has priced nothing." + Q + "\n"
    "     " + Q + " ### NO PAST ACT IS RE-VERDICTED, no past copy of the flattener is edited, and no registration the new arms would fire on is touched. ### THE SCAN" + Q + "\n"
    "     " + Q + " WAS NOT TAUGHT THE ACT-NUMBER CLAUSE, so it binds a reader and not a tool. ### THE MODULES ARE PRIVATE AND NOT PUSHED. ### NO GRADE MOVED." + Q + "\n"
    "     " + Q + " ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b347_the_three_repairs.txt; data/b347_repairs_run.txt (the first run file in the corpus carrying its own clock);" + Q + "\n"
    "     " + Q + " data/b347_registration_2026-09-06.txt (sealed before any tool was touched and before any module was written);" + Q + "\n"
    "     " + Q + " data/b347_order_2026-09-06.txt; tools/run_clock.py; tools/gate_text.py; tools/registration_gate.py (the two arms);" + Q + "\n"
    "     " + Q + " tools/FERRY_STANDING.md (v2); TECHNE-Core modules/2026-09/BAR_FLOOR_RULE.md and TWO_ROUTES.md (local, NOT PUSHED);" + Q + "\n"
    "     " + Q + " CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('the bar-floor rule', "the run file's clock", 'the flattener', 'the two-routes rule',
           "the satisfiability audit's limit", 'the standing clauses v2', 'the act-number clause',
           'a bar below its floor', 'arms that are one arm')
MUST_NOT_HIT = ('the audit is closed', 'the past acts are corrected', 'a sharper instrument is a result',
                'the clock dates the old runs')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print("b347 -- THE INDEX KEY. ### THE THREE REPAIRS AND THE TWO RULES.")
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'bar-floor-rule'" in txt)
    have_row = ('"bar-floor-rule"' in txt)
    print('  bar-floor-rule key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('bar-floor-rule')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : bar-floor-rule returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'bar-floor-rule' in o
        ok = ok and g
        print('    %-44s reaches the b347 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTEXPLAINED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A SHARPER INSTRUMENT IS NOT A RESULT' in out and 'THE CLOCK DOES NOT REACH BACKWARDS' in out
    a2 = 'NAMED AND PRICED, NOT CLOSED' in out and 'MATCHES TEXT' in out
    a3 = 'NO PAST ACT IS RE-VERDICTED' in out and 'NOT PUSHED' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says a sharper instrument is not a result, and the clock does not reach back : %s' % a1)
    print('    ### and the audit is not closed, and the gate only matches text                         : %s' % a2)
    print('    ### and no past act is re-verdicted, and the modules are not pushed                     : %s' % a3)
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
