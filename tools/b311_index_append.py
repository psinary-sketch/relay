# -*- coding: utf-8 -*-
"""b311_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES ONE -- `identity-neighbourhood` -- AND SAYS EVERY RESULT KEYED.** ### The
### act has two: where the source's trace-side content sits, and the decision that the finite
### side's mechanism does not type at infinity.

### ### **THE MUST-NOT-HIT ARM IS b202's: ### `the proof` AND `infinity` STAY UNKEYED.** ### The
### first is a generic object this record holds many of; the second is a PLACE, not a result, and
### ### **AN INDEX THAT ANSWERED `infinity` WOULD BE OFFERING THIS ACT'S REFUSAL AS THOUGH IT WERE
### ### THE CORPUS'S ARCHIMEDEAN MATHEMATICS.**
### ### **AND THE INDEX IS SWEPT FOR STEMS AFTER THE WRITE** (b305's defect, caught at b306).
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
    "    'identity-neighbourhood': ['the trace remainder', 'the local weight',\n"
    "                              'where the content sits', 'the source proof read'],\n"
    "    'arch-mechanism-untyped': ['trace class', 'the count and the jacobian',\n"
    "                              'does not type', 'the archimedean instrument price'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE SOURCE'S PROOF READ (b311).\n"
    "    (\"identity-neighbourhood\", \"b311 (a read at content, under the import bar)\",\n"
    "     \"CC 2006.13771v1 read at content, artefact pinned by sha256 b8e0b54a... BEFORE a word of\"\n"
    "     \" it was read. ### **THE SOURCE DOES NOT EVALUATE THE COMPRESSED TRACE AT INDIVIDUAL\"\n"
    "     \" SCALINGS**: it gives the single-scaling trace FORMALLY (Prop 1.5(ii)) and recovers\"\n"
    "     \" trace class ONLY after smearing (Prop 1.5(iv)); it isolates a trace-remainder delta\"\n"
    "     \" (Def 2.1) and notes that, unlike tau which 'is not a function because of the divergency\"\n"
    "     \" at rho = 1', delta IS a function with a JUMP IN ITS FIRST DERIVATIVE at rho = 1; and it\"\n"
    "     \" turns that jump into Theorem 3.6's -2 Id + K_I with K_I compact. ### **AND THEOREM 4.7\"\n"
    "     \" PINS THE TRACE SIDE TO THE DISTRIBUTION: Tr(theta(f)S) = W_inf(f) + INT f(rho^-1)\"\n"
    "     \" eps(rho) d*rho with eps a FUNCTION** -- so the only part of the trace side that is not\"\n"
    "     \" an integral against a function is the part at the identity\",\n"
    "     \"### AN IMPORT, READ AT CONTENT, AT THE IMPORT BAR. ### **THIS ACT READ STATEMENTS AND\"\n"
    "     \" THEIR STATED ROLES; IT VERIFIED NO PROOF OF THE SOURCE'S, AND NOTHING HERE IS EVIDENCE\"\n"
    "     \" THAT ANY OF THEM IS CORRECT.** ### 20 fragments located by tools/b311_source.py, 0\"\n"
    "     \" unlocated, across pages 1, 2, 8, 10, 11, 12, 13, 18, 26, 27, 47; the tool LOCATES and\"\n"
    "     \" does not read. ### **WHAT DOES NOT FOLLOW: that the source's result is ABOUT THE\"\n"
    "     \" IDENTITY ALONE** -- eps is not nothing and Theorem 3.6 is about a quadratic form on an\"\n"
    "     \" INTERVAL. ### **NO ARCHIMEDEAN NUMBER IS COMPUTED.** ### M-2 UNCHANGED\",\n"
    "     \"data/b311_the_identitys_neighbourhood.txt; data/b311_components_run.txt;\"\n"
    "     \" data/b311_source_pin.txt; CORRESPONDENCE.md row 134\"),\n"
    "    # ### THE MECHANISM DOES NOT TYPE AT INFINITY (b311).\n"
    "    (\"arch-mechanism-untyped\", \"b311 (a decision at definitions, and a price)\",\n"
    "     \"b310 closed the finite side with one sentence -- Tr(theta(t)Pi) is a SIGNED COUNT of the\"\n"
    "     \" off-ball points t fixes. ### **THIS ACT DECIDES, BY DEFINITIONS, THAT IT DOES NOT TYPE\"\n"
    "     \" AT THE ARCHIMEDEAN PLACE, AND THE STEP AT WHICH IT PARTS IS THE DIMENSION OF THE\"\n"
    "     \" OBJECT'S SPACE**: finite-dimensional at a finite place (a truncation, so theta(t)Pi is\"\n"
    "     \" finite rank and the trace is an integer count the first condition kills), and INFINITE\"\n"
    "     \" at infinity in CC's own words -- so the single-scaling compression is not trace class\"\n"
    "     \" and THERE IS NO COUNT TO TAKE. ### In both cases the map fixes only the origin and the\"\n"
    "     \" origin lies in the excluded region, but **the finite local term is an EVALUATION and\"\n"
    "     \" the continuous one is a JACOBIAN, and a vanishing condition acts on the first and not\"\n"
    "     \" on the second**\",\n"
    "     \"### A REFUSAL, NOT A NEGATIVE RESULT. ### **A STATEMENT ABOUT TYPES -- that a question\"\n"
    "     \" answered on one side does not parse on the other -- AND THE CORPUS HAS DONE NO\"\n"
    "     \" MATHEMATICS AT INFINITY HERE.** ### The navigator's second expectation is REFUTED in\"\n"
    "     \" its first half (the compression has NO trace, and where its formal value is a function\"\n"
    "     \" it is nonzero) and CONFIRMED in its diagnosis (the difference lives at the identity).\"\n"
    "     \" ### **THE RESEMBLANCE BETWEEN A DISCRETE COUNT AND A CONTINUOUS WEIGHT IS NAMED AND\"\n"
    "     \" REFUSED AS EVIDENCE; no bridging definition is exhibited or claimed** -- b285's hazard\"\n"
    "     \" register named the species: THE WORD SURVIVES; THE OBJECT DOES NOT. ### The price of an\"\n"
    "     \" archimedean instrument is typed and estimated at three acts for the truncation and two\"\n"
    "     \" for the compression, ONLY IF W-ORD-ARCH-NORM-READING is settled first -- an estimate,\"\n"
    "     \" not a commitment. ### The author's W2 window ruling is RECORDED AND NOT APPLIED. ### NO\"\n"
    "     \" BRANCH DECIDED. ### M-2 UNCHANGED under its cap\",\n"
    "     \"data/b311_the_identitys_neighbourhood.txt; data/b285_archimedean_opening.txt (the hazard\"\n"
    "     \" register); data/b310_the_smear_collapses.txt; CORRESPONDENCE.md row 135\"),\n"
)

NEW_KEYS = ('identity-neighbourhood', 'arch-mechanism-untyped')
ALIASES = ('the trace remainder', 'the local weight', 'the source proof read',
           'trace class', 'does not type', 'the archimedean instrument price')
MUST_NOT_HIT = ('the proof', 'infinity')


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
    print('b311 -- THE INDEX KEYS. ### THE READ, AND THE REFUSAL.')
    print('=' * 100)
    print('  ### MUST-NOT-HIT, MEASURED BEFORE THE WRITE:')
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-22s NO KEY before : %s' % (q, pre[q]))

    have_key = {k: ("'%s'" % k) in txt for k in NEW_KEYS}
    have_row = {k: ('"%s"' % k) in txt for k in NEW_KEYS}
    for k in NEW_KEYS:
        print('  %-26s key/row already present : %s / %s' % (k, have_key[k], have_row[k]))
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
            new = new.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW, 1)
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
        print('    %-26s returns a row : %s  %s' % (k, good, 'PASS' if good else '### FAIL ###'))

    print('  ### THE ALIASES, EACH OF WHICH RETURNED `NO KEY` BEFORE THIS ACT:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-32s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-22s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the proof` AND `infinity` STAY UNKEYED: the first is a generic object this')
    print('  ### record holds many of, and the second is a PLACE and not a result.** ### An index')
    print('  ### answering `infinity` would be offering this act\'s REFUSAL as though it were the')
    print('  ### corpus\'s archimedean mathematics.')

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
