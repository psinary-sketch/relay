# -*- coding: utf-8 -*-
"""b342_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-BINDSNOTHING`.** ### A reader who asks *where do the two rules live* must be
### handed the modules with the sentences that they are private, local, not pushed, that they state the grade their owning
### acts carry and confer none, and that the fold's lines are untouched. ### **`the modules published` AND `the rule has
### force` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b342_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
J = json.load(io.open(os.path.join(D, 'b342_modules.json'), encoding='utf-8'))

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'two-rules-modules': ['the two rules as modules', 'the like-for-like rule', 'the like-for-like module', 'the sign rule', 'the sign rule module',\n"
    "                          'the threshold rule', 'the phase rule', 'the phase refinement', 'where do the two rules live', 'the techne modules',\n"
    "                          'like_for_like.md', 'sign_rule.md', 'the lore re-typed'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE TWO RULES AS MODULES (b342, leg 4 of the sortie b339-b343).\n"
    "    (\"two-rules-modules\", \"b342 (a filings act: two method modules, private, local, NOT PUSHED; a re-typing block)\",\n"
    "     \"THE TWO RULES AS TECHNE MODULES, as the executor's draft states them: LIKE_FOR_LIKE.md (a comparator is named with the function it was\"\n"
    "     \" computed for; a bar sealed against a banked table names the table's function; a mismatch is refused -- b333's incident, b334's comparator)\"\n"
    "     \" and SIGN_RULE.md (a threshold rule is stated with its sign condition; a phase past the threshold is not a negative term -- b334's hundred\"\n"
    "     \" positive-term aims), the sign-rule module carrying the b328 refinement (S_4 negative exactly between 45 and 135 degrees; b336's addendum);\"\n"
    "     \" the index appended by one block; every existing module byte-identical; committed locally at " + str(J['committed']) + ", the remote at " + str(J['remote_after']) + " before and\"\n"
    "     \" after, NOT PUSHED. FINDINGS gains one appended block re-typing the two lore lines from TOOL to MODULE, the fold's lines untouched.\",\n"
    "     \"### THE MODULES BIND NOTHING; THEY STATE THE GRADE THEIR OWNING ACTS CARRY AND CONFER NONE. ### PRIVATE, LOCAL, NOT PUSHED. ### THE FOLD'S\"\n"
    "     \" LINES UNTOUCHED. ### NO GRADE MOVED. ### NO TERMINAL. ### M-2 UNCHANGED\",\n"
    "     \"data/b342_the_two_rules_as_modules.txt; data/b342_modules_run.txt; data/b342_lore_run.txt; data/b342_executor_draft_2026-09-06.txt;\"\n"
    "     \" data/b342_registration_2026-09-06.txt (sealed before any write, with its post-seal marking); TECHNE-Core modules/2026-09/LIKE_FOR_LIKE.md,\"\n"
    "     \" SIGN_RULE.md, modules/INDEX.md (local); FINDINGS.md (the b342 addendum); CORRESPONDENCE.md row " + R1 + "\"),\n"
)

ALIASES = ('the two rules as modules', 'the like-for-like rule', 'the sign rule', 'the threshold rule', 'the phase rule', 'the techne modules',
           'where do the two rules live', 'the lore re-typed')
MUST_NOT_HIT = ('the modules published', 'the rule has force', 'techne pushed')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b342 -- THE INDEX KEY. ### THE TWO RULES AS MODULES.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'two-rules-modules'" in txt)
    have_row = ('"two-rules-modules"' in txt)
    print('  two-rules-modules    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('two-rules-modules')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : two-rules-modules returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'two-rules-modules' in o
        ok = ok and g
        print('    %-44s reaches the b342 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-BINDSNOTHING -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'THE MODULES BIND NOTHING' in out and 'CONFER NONE' in out
    a2 = 'PRIVATE, LOCAL, NOT PUSHED' in out
    a3 = "THE FOLD'S LINES UNTOUCHED" in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says the modules bind nothing, confer none : %s' % a1)
    print('    ### and private, local, not pushed                     : %s' % a2)
    print("    ### and the fold's lines untouched, no grade moved      : %s" % a3)
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
