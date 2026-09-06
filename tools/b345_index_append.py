# -*- coding: utf-8 -*-
"""b345_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTEXPLAINED`.** ### A reader who asks *what did the Li control
### re-run settle* must be handed: a control certifies the instrument and not the object; the Li family is NOT in the
### lawful class; b340's bar is NOT rewritten and its verdict NOT re-verdicted; the zero side and the finite side are
### NOT evaluated, so the trail stays owed; the deposit's finite-range positivity is the DEPOSIT'S; and one sealed
### fixture FAILED at its own threshold and is tabled rather than repaired into passing. ### **`b340 corrected`, `the
### li family is lawful`, `the trail is paid` AND `the formula closed on the li family` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b345_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
K = json.load(io.open(os.path.join(D, 'b345_control.json'), encoding='utf-8'))
F = json.load(io.open(os.path.join(D, 'b345_filings.json'), encoding='utf-8'))
KD = K['kernel_diagnostic'] or {}

Q = chr(34)
BS = chr(92)
APOS = BS + "'"

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'li-control-rerun': ['the li control re-run', 'the li control rerun', 'the tail panel', 'the two routes',\n"
    "                         'the fourth control', 'the kernel fixture', 'the hand-rolled kernel', 'the work-order for the axes',\n"
    "                         'the floor" + APOS + "s two axes', 'one distribution on two families'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")


def s(x):
    return str(x)


ROW_NEW = (
    "    # ### THE LI CONTROL, RE-RUN (b345).\n"
    "    (" + Q + "li-control-rerun" + Q + ", " + Q + "b345 (a control re-run under a new bar with the tail rule fixed first)" + Q + ",\n"
    "     " + Q + "THE LI CONTROL RE-RUN: b340 asked two things of every index -- the identity, and the drift between two sealed quadratures. The identity held;" + Q + "\n"
    "     " + Q + " the drift did not, because the sealed refinement route put Gauss-Legendre on an infinite panel with a logarithmic tail. b345 registered ITS OWN" + Q + "\n"
    "     " + Q + " bar with the tail rule FIXED BEFORE ANY VALUE as TANH-SINH -- the rule b340" + APOS + "s own diagnosis named -- and required its two routes to share no" + Q + "\n"
    "     " + Q + " code: route A is b340" + APOS + "s theta route imported unedited, route B is fresh in the u variable with the transform factor as the complex power" + Q + "\n"
    "     " + Q + " Re[1 - ((s-1)/s)^n] and a HAND-ROLLED digamma. VERDICT, BY THE SEALED RULE: " + s(K['verdict']) + " at " + s(K['n_hold']) + " of " + s(len(K['indices'])) + " tabulated indices --" + Q + "\n"
    "     " + Q + " worst identity miss " + s(K['worst_miss']) + " against 1e-9 max(1, |lambda_A|), worst drift between routes " + s(K['worst_drift']) + ", every index RESOLVED," + Q + "\n"
    "     " + Q + " the pole constant L_n[log s] its own column and equal to 1 to " + s(K['pole_worst']) + ". AND ONE SEALED FIXTURE FAILED AT ITS OWN THRESHOLD: section (C)" + Q + "\n"
    "     " + Q + " sealed a recurrence to |w| >= " + s(K['recur_to']) + " with Stirling through B_" + s(2 * K['n_bern']) + " AND a fixture threshold of " + s(K['fix_bar']) + " in the same paragraph; the" + Q + "\n"
    "     " + Q + " truncation" + APOS + "s first dropped term leaves a floor near " + s(K['kernel_worst']) + ", so at " + s(K['fix_bar']) + " the fixture rejects the CORRECT copy too and separates" + Q + "\n"
    "     " + Q + " nothing. Carrying only the recurrence to |w| >= " + s(KD.get('recur')) + " brings the same routine to " + s(KD.get('worst')) + ", which locates the defect in one named half." + Q + ",\n"
    "     " + Q + "### A CONTROL CERTIFIES THE INSTRUMENT, NOT THE OBJECT. ### THE LI FAMILY IS NOT IN THE LAWFUL CLASS -- three of three of Theorem 1" + APOS + "s" + Q + "\n"
    "     " + Q + " conditions fail -- so Theorem 1" + APOS + "s inequality and the Sonin margin DO NOT APPLY, and the Sonin margin is not defined on this family at all." + Q + "\n"
    "     " + Q + " ### b340" + APOS + "s BAR IS NOT REWRITTEN AND ITS VERDICT IS NOT RE-VERDICTED: a re-run under a new bar is a new measurement, not a correction." + Q + "\n"
    "     " + Q + " ### THE ZERO SIDE AND THE FINITE SIDE ARE NOT EVALUATED, SO W-ORD-LI-FAMILY-CONTROL STAYS OWED and is paid at its archimedean constituent" + Q + "\n"
    "     " + Q + " only. ### THE DEPOSIT" + APOS + "S FINITE-RANGE POSITIVITY IS THE DEPOSIT" + APOS + "S, restated at its scope; positivity in a finite range is not evidence of the" + Q + "\n"
    "     " + Q + " kind the criterion respects. ### THE FAILED FIXTURE IS TABLED, NOT REPAIRED INTO PASSING, AND CONFERS NOTHING. ### NO GRADE MOVED." + Q + "\n"
    "     " + Q + " ### NO TERMINAL. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b345_the_li_control_rerun.txt; data/b345_control_run.txt; data/b345_filings_run.txt;" + Q + "\n"
    "     " + Q + " data/b345_registration_2026-09-06.txt (sealed before the tail panel was integrated once and before the second route was written);" + Q + "\n"
    "     " + Q + " data/b345_control_draft_unsealed_params_stopped.txt (a draft at parameters this act did not seal, stopped, no value used);" + Q + "\n"
    "     " + Q + " PLACE-papers FACES_LEDGER.md (row L1 update block) and OPEN_TRAILS.md (" + s(F['trail_id']) + ");" + Q + "\n"
    "     " + Q + " CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('the li control re-run', 'the tail panel', 'the two routes', 'the kernel fixture', 'the hand-rolled kernel',
           'the work-order for the axes', "the floor's two axes", 'one distribution on two families')
MUST_NOT_HIT = ('b340 corrected', 'the li family is lawful', 'the trail is paid', 'the formula closed on the li family')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print("b345 -- THE INDEX KEY. ### THE LI CONTROL, RE-RUN.")
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'li-control-rerun'" in txt)
    have_row = ('"li-control-rerun"' in txt)
    print('  li-control-rerun key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('li-control-rerun')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : li-control-rerun returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'li-control-rerun' in o
        ok = ok and g
        print('    %-44s reaches the b345 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTEXPLAINED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A CONTROL CERTIFIES THE INSTRUMENT, NOT THE OBJECT' in out and 'NOT IN THE LAWFUL CLASS' in out
    a2 = 'IS NOT REWRITTEN AND ITS VERDICT IS NOT RE-VERDICTED' in out and 'STAYS OWED' in out
    a3 = 'FINITE-RANGE POSITIVITY IS THE DEPOSIT' in out and 'TABLED, NOT REPAIRED INTO PASSING' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3
    print('    the answer says a control certifies the instrument, and the family is not lawful : %s' % a1)
    print("    ### and b340 is not corrected, and the trail stays owed                          : %s" % a2)
    print('    ### and the positivity is the deposit\'s, and the failed fixture confers nothing  : %s' % a3)
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
