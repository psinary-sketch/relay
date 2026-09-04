# -*- coding: utf-8 -*-
"""b315_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES BOTH: ### *calibration, rate-corrected keyed*.**

### ### **THE MUST-NOT-HIT ARM IS b202's: ### `the sign` AND `the envelope` STAY UNKEYED.** ### The
### first is what the calibration fixes and is the query most likely to be typed by someone wanting
### a verdict about the archimedean sign itself, which this act did not give; the second is an
### object whose banked form belongs to b264, and ### **AN INDEX THAT ANSWERED `the envelope` WOULD
### ### BE OFFERING A CONSTANT BOUND UNDER ONE CONVENTION AS THOUGH IT WERE THE ENVELOPE.**
### ### **THE INDEX IS SWEPT FOR STEMS AFTER THE WRITE** (b305's defect, caught at b306).
"""
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'tools', 'banked_index.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NL = chr(10)

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'calibration': ['what the calibration fixes', 'is A independently defined',\n"
    "                   'the E2 in the bracket', 'the sign only'],\n"
    "    'rate-corrected': ['the even sector under the source convention',\n"
    "                   'the envelope becomes a constant', 'the cutoff order',\n"
    "                   'the rate re-derived'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE CALIBRATION READ (b315).\n"
    "    (\"calibration\", \"b315 (a read at content, at the operation)\",\n"
    "     \"the atlas's calibration read AT THE OPERATION, not at the comment. ### **A IS COMPUTED\"\n"
    "     \" AT carto_atlas.py:66 AS AN EXPLICIT INTEGRAL OF THE DIGAMMA KERNEL AGAINST THE TEST\"\n"
    "     \" FUNCTION, DIVIDED BY 2 pi -- no free constant, no fitted factor, and nothing from any\"\n"
    "     \" remainder in it**; the calibration settles the ORIENTATION with which that term enters\"\n"
    "     \" the explicit formula, tested at line 117 by abs(residual) <= TOL on Z - (P - PR + A).\"\n"
    "     \" ### **AND THAT RESIDUAL CONTAINS NO REMAINDER AT ALL: the E2 in the bracket is the\"\n"
    "     \" name of a REGISTERED CLAIM (E1-E4), NOT the archimedean remainder E2 of b38's\"\n"
    "     \" identity.** ### **SO THE NEAR-CANCELLATION A + E2 ~ 0 UNDER THE SOURCE'S CONVENTION IS\"\n"
    "     \" NOT PRODUCED BY THE CALIBRATION: IT SURVIVES**, worst modulus 0.022509, 1.13%% of the\"\n"
    "     \" largest modulus of A in the table\",\n"
    "     \"### A READ, AND A CORRECTION TO A REASON. ### **b312's SENTENCE AND b313's CAUTION\"\n"
    "     \" RESTED ON ONE NAME FOR TWO OBJECTS -- the double-name species b200 named and b219\"\n"
    "     \" realised -- AND NEITHER ACT IS RE-VERDICTED.** ### Their numbers stand; b313's REFUSAL\"\n"
    "     \" to interpret the column ALSO STANDS, on a stronger ground: not *it might be the\"\n"
    "     \" calibration* but **no definition has been stated that would make it mean anything**.\"\n"
    "     \" ### **A CORRECTION THAT REMOVES A CAUTION IS NOT A LICENCE TO INTERPRET**, and A + E2\"\n"
    "     \" is promoted to nothing. ### The independence check runs over the ENCLOSING FUNCTION and\"\n"
    "     \" is shown able to find a dependence when one is there. ### NO GRADE MOVED. ### M-2\"\n"
    "     \" UNCHANGED\",\n"
    "     \"data/b315_the_calibration_and_the_rate.txt; data/b315_components_run.txt;\"\n"
    "     \" tools/e16/carto_atlas.py (the emitting file); CORRESPONDENCE.md row 142\"),\n"
    "    # ### THE RATE UNDER THE SOURCE'S EXPONENT (b315).\n"
    "    (\"rate-corrected\", \"b315 (a derivation, with the bench as its check)\",\n"
    "     \"b264's Cauchy-Schwarz-and-Plancherel route re-run with the corrected exponent. ###\"\n"
    "     \" **EVERY STEP SURVIVES BUT THE PREFACTOR**: Cauchy-Schwarz bounds the INTEGRAL and the\"\n"
    "     \" exponent multiplies it. ### **SO THE MODULUS OF eps_even^src(rho) IS AT MOST C_even =\"\n"
    "     \" 132.781908429 -- THE SAME CONSTANT, WITH NO POWER OF rho AT ALL.** ### The sharp rate\"\n"
    "     \" keeps its constant and loses one power: **rho^(1/2) eps_even^src -> K_even =\"\n"
    "     \" 1.568231065**. ### And along the CUTOFF, by b264's own dilation route (cited, not\"\n"
    "     \" re-claimed): **THE EVEN SECTOR STILL VANISHES AT THE SAME LEADING ORDER 1/log a, AND\"\n"
    "     \" ONLY THE CONSTANT CHANGES**, because the measure drho/rho absorbs exactly the one power\"\n"
    "     \" the flip introduces\",\n"
    "     \"### A DERIVATION, AND WHAT IT REPORTS IS A LOSS. ### **THE NEW ENVELOPE IS NOT MERELY\"\n"
    "     \" LOOSE, IT IS VACUOUS IN THE LIMIT** -- about 168x above the value at its tightest\"\n"
    "     \" converged cell, and getting looser without bound. ### b264 used the old envelope to\"\n"
    "     \" CARRY THE TAIL; **a constant is not integrable against drho/rho, so the cutoff constant\"\n"
    "     \" has a measured body and NO RIGOROUS TAIL BOUND from this route.** ### The ORDER is\"\n"
    "     \" derived and unchanged; the CONSTANT is not certified. W-ORD-SOURCE-TAIL filed. ###\"\n"
    "     \" Convergence decided by b264's OWN TWO-AXIS TEST, not a ceiling number. ### **THE\"\n"
    "     \" BEARING ON b262's BRANCH IS A BEARING ONLY** -- one archimedean OBJECT is not the\"\n"
    "     \" archimedean SIDE, and b242's law governs: a measured rate is not a tail bound. ### M-2\"\n"
    "     \" UNCHANGED\",\n"
    "     \"data/b315_the_calibration_and_the_rate.txt; data/b315_rows.json;\"\n"
    "     \" data/b264_eps_even_decay.txt (the route's owner); CORRESPONDENCE.md row 143\"),\n"
)

NEW_KEYS = ('calibration', 'rate-corrected')
ALIASES = ('what the calibration fixes', 'is A independently defined',
           'the E2 in the bracket', 'the sign only',
           'the even sector under the source convention',
           'the envelope becomes a constant', 'the cutoff order', 'the rate re-derived')
MUST_NOT_HIT = ('the sign', 'the envelope')


def no_key(out):
    for ln in (out or '').splitlines():
        if ln.strip().startswith('### NO KEY'):
            return True
    return False


def verdict_fixture():
    real = no_key('=====' + NL + '  ### NO KEY.' + NL + '  ### matched no DECLARED key')
    quoted = no_key('    grade    : ... every query that would have found b268 returned NO KEY.')
    return real, quoted


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b315 -- THE INDEX KEYS. ### THE CALIBRATION, AND THE RATE.')
    print('=' * 100)
    print('  ### MUST-NOT-HIT, MEASURED BEFORE THE WRITE:')
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-18s NO KEY before : %s' % (q, pre[q]))

    have_key = {k: ("'%s'" % k) in txt for k in NEW_KEYS}
    have_row = {k: ('"%s"' % k) in txt for k in NEW_KEYS}
    for k in NEW_KEYS:
        print('  %-18s key/row already present : %s / %s' % (k, have_key[k], have_row[k]))
    written = not (all(have_key.values()) and all(have_row.values()))
    if not written:
        print('  ### NOTHING WRITTEN. (idempotent) ### **THE READ-BACK ARMS STILL RUN.**')
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file.')
        return 2

    if written:
        new = txt
        if not all(have_key.values()):
            new = new.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW, 1)
        if not all(have_row.values()):
            new = new.replace(ROW_ANCHOR, ROW_ANCHOR + (ROW_NEW % ()), 1)
        open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(PATH + '.tmp', PATH)

    rv, qv = verdict_fixture()
    print('  VERDICT FIXTURE : fires on the index\'s own NO KEY line : %s ;'
          ' quiet on the phrase quoted inside a row : %s' % (rv, not qv))
    ok = rv and not qv

    print('  ### READ BACK BY QUERYING THE INDEX ITSELF:')
    for k in NEW_KEYS:
        out, rc = query(k)
        good = (not no_key(out)) and (k in out) and rc == 0
        ok = ok and good
        print('    %-18s returns a row : %s  %s' % (k, good, 'PASS' if good else '### FAIL ###'))

    print('  ### THE ALIASES, EACH OF WHICH RETURNED `NO KEY` BEFORE THIS ACT:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-42s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-18s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the sign` AND `the envelope` STAY UNKEYED.** ### The first is what the')
    print('  ### calibration fixes and is the query most likely to be typed by someone wanting a')
    print('  ### verdict about the archimedean sign itself, which this act did not give; the second')
    print('  ### is b264\'s object, and an index answering it would offer a CONSTANT bound under one')
    print('  ### convention as though it were the envelope.')

    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import ferry_scan
    _c, sh = ferry_scan.scan_text(io.open(PATH, encoding='utf-8').read(), [], ferry_scan.stems())
    print('  ### THE INDEX SWEPT AFTER THE WRITE : %d stem hit(s)' % len(sh))
    for h in sh:
        print('      line %d  %s' % (h[1], h[3][:96]))
    ok = ok and not sh
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
