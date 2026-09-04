# -*- coding: utf-8 -*-
"""b320_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES TWO: ### `lawful-function` AND `source-control`.**

### ### **AND THE CLAIM THIS ACT TAKES IS ONE NO PRIOR ACT COULD: ### *the archimedean weil
### ### distribution*.** ### b317, b318 and b319 each left it unkeyed and each was right to --
### none of them computed the functional on the LEFT of the source's inequality. ### This act does,
### from the source's (53) and (38) directly, so it claims the alias. ### **THE MEASUREMENT BEFORE
### ### THE WRITE IS PRINTED SO THE TRANSITION IS VISIBLE**, exactly as b319 did when it claimed
### `the rank stable subspace` from b318.

### ### **`the nonempty reach` IS ALSO CLAIMED, AND WITH A QUALIFICATION IN THE ROW ITSELF.** ###
### b319 left it unkeyed because its own sealed bar was unsatisfiable. ### **THE REACH IS NON-EMPTY
### ### HERE UNDER A BAR THIS ACT ITSELF CORRECTED**, and a row that said `3 of 3` without saying
### that would be handing back an achievement where a bar change belongs.

### ### **THE MUST-NOT-HIT ARMS ARE THINGS THIS ACT DID NOT DO.** ### `the window class` stays
### unkeyed -- ### **NO WINDOW WAS OPENED HERE** ### and the ten uncovered cells are data with no
### claim. ### `the archimedean membership` stays unkeyed -- nothing here decides it.
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
    "    'lawful-function': ['the lawful function', 'the square of the seed',\n"
    "                        'is the corpus window a g or an f', 'the sonin class membership test',\n"
    "                        'which cells does theorem one cover'],\n"
    "    'source-control': ['the source control', 'both sides of the inequality',\n"
    "                       'the archimedean weil distribution', 'the nonempty reach',\n"
    "                       'the control that failed first', 'did the control hold'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE SQUARE OF THE SEED, AND THE CELLS THE THEOREM COVERS (b320).\n"
    "    (\"lawful-function\", \"b320 (a construction, and the class test the source defines)\",\n"
    "     \"the corpus's seed squared in the source's own convention and tested against the\"\n"
    "     \" source's own class definition. ### The adjoint is written once from the involution of\"\n"
    "     \" the convolution C*-algebra, g#(rho) = conj(g(rho^-1)) against the MULTIPLICATIVE\"\n"
    "     \" measure d*mu, which in v = log rho makes the product the autocorrelation with\"\n"
    "     \" transform |g-hat|^2. ### By Definition 3.1 -- positive definite iff f-hat >= 0\"\n"
    "     \" pointwise -- **f = g conv g# IS POSITIVE DEFINITE AT 13 OF 13 CELLS**, minima -4.6e-17\"\n"
    "     \" to +5.9e-18 against a sealed -1e-09 floor. ### **AND THIS SETTLES b318's READING BY\"\n"
    "     \" MEASUREMENT**: b318 found NEITHER test function positive definite, 0 of 13, and read\"\n"
    "     \" the corpus's window as a candidate g and not a candidate f. ### The window passes at NO\"\n"
    "     \" cell; its square passes at every one. ### **THEOREM 1's COVERED CELLS, NAMED FROM THE\"\n"
    "     \" CHECK: 1.3, 1.35, 1.41** -- the support condition is the only one that bites, and the\"\n"
    "     \" two vanishing conditions hold at EVERY cell to 1.4e-17..5.7e-16\",\n"
    "     \"### A SQUARE LANDING IN THE CLASS OF SQUARES IS NOT A DISCOVERY. ### **SCOPE: this\"\n"
    "     \" fixes WHICH CELLS the source's theorem speaks at, and nothing else.** ### **AND THE\"\n"
    "     \" CLASS TEST CAN FAIL, WHICH IS THE ONLY REASON ITS PASSING IS WORTH PRINTING**: the same\"\n"
    "     \" code path returns min f-hat = -5.85e-01 on b318's wide-minus-narrow fixture. ### **NO\"\n"
    "     \" WINDOW IS OPENED** -- the ten uncovered cells are computed and printed as data with no\"\n"
    "     \" claim, and the inequality holding there is evidence for nothing, because outside the\"\n"
    "     \" hypotheses there is no conclusion to be evidence for. ### **NO UNIT IS USED.** ### NO\"\n"
    "     \" ACT RE-VERDICTED. ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b320_the_lawful_function.txt; data/b320_components_run.txt;\"\n"
    "     \" tools/b320_weil.py and tools/b318_square.py (the emitting files);\"\n"
    "     \" CORRESPONDENCE.md row 152\"),\n"
    "    # ### BOTH SIDES, AND THE CONTROL THAT FAILED BEFORE IT HELD (b320).\n"
    "    (\"source-control\", \"b320 (a computation, and the source's own theorem as its control)\",\n"
    "     \"both sides of the source's inequality computed on the stable-rank instrument and checked\"\n"
    "     \" where Theorem 1 covers. ### The left side is built from (53) and (38) with its\"\n"
    "     \" principal-value constant MEASURED and not remembered -- C_R = 2.415093331442 from two\"\n"
    "     \" Gaussian widths agreeing to 4.7e-10, landing on gamma + log(2 pi) = 2.415092731311,\"\n"
    "     \" which this act did not put in. ### **THIS ACT'S FIRST REPORTED VERDICT WAS FAILS.** ###\"\n"
    "     \" The registration's (B6) fixed a link order before any value existed and the failure\"\n"
    "     \" named a constituent: links (1)-(3) clean, **LINK (4), THIS ACT'S OWN IMPLEMENTATION OF\"\n"
    "     \" (38), NAMED**. ### After the repair: **W_inf >= SQUARE at all three covered cells,\"\n"
    "     \" margins +0.2714, +0.2855, +0.3098, and at 27 of 27 instrument frames.** ### A second\"\n"
    "     \" defect in the same function survived the first repair and printed 1.9e9; two new\"\n"
    "     \" fixtures fail without each repair, and a SECOND AND INDEPENDENT ROUTE was built\",\n"
    "     \"### A CONTROL THAT HOLDS CERTIFIES THE INSTRUMENT, NOT THE OBJECT. ### **NO THEOREM IS\"\n"
    "     \" PROVED HERE** -- the source proved Theorem 1 and this act checked that the instrument\"\n"
    "     \" does not contradict it where it speaks. ### **NO BAR WAS MOVED, NO CELL DROPPED, NO\"\n"
    "     \" TOLERANCE LOOSENED, AND THE REGISTRATION WAS NOT RE-SEALED** -- hash 6f1c1e13...\"\n"
    "     \" verifies intact. ### **THE REACH IS NON-EMPTY FOR THE FIRST TIME IN THIS ARC, 3 OF 3,\"\n"
    "     \" UNDER A BAR THIS ACT ITSELF CORRECTED** in its registration before any value, per\"\n"
    "     \" b319's own proposal. ### **SCOPE: the SIGN of every margin is certified at every frame;\"\n"
    "     \" the SIZE at none** -- the noise gate REFUSES 3 of 6 and all three are domain frames.\"\n"
    "     \" ### **AND THE REGISTERED EXPECTATION IS HALF REFUTED**: the margin was expected to\"\n"
    "     \" SHRINK toward the boundary cell and it GROWS. ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b320_the_lawful_function.txt; data/b320_corroboration.txt;\"\n"
    "     \" data/b320_registration_2026-09-04.txt (sealed); CORRESPONDENCE.md row 153\"),\n"
)

NEW_KEYS = ('lawful-function', 'source-control')
ALIASES = ('the lawful function', 'the square of the seed', 'is the corpus window a g or an f',
           'the sonin class membership test', 'which cells does theorem one cover',
           'the source control', 'both sides of the inequality',
           'the control that failed first', 'did the control hold')
# ### **CLAIMED HERE, AND UNKEYED BEFORE NOW.** ### The transition is measured, not asserted.
CLAIMED_FROM_UNKEYED = ('the archimedean weil distribution', 'the nonempty reach')
MUST_NOT_HIT = ('the window class', 'the archimedean membership')


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
    print('b320 -- THE INDEX KEYS. ### THE LAWFUL FUNCTION, AND THE CONTROL.')
    print('=' * 100)
    print('  ### MUST-NOT-HIT, MEASURED BEFORE THE WRITE:')
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))

    print('  ### AND THE TWO ALIASES THIS ACT CLAIMS, MEASURED BEFORE IT CLAIMS THEM:')
    preclaim = {}
    for q in CLAIMED_FROM_UNKEYED:
        out, _rc = query(q)
        preclaim[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, preclaim[q]))
    print('    ### **b317, b318 AND b319 EACH LEFT `the archimedean weil distribution` UNKEYED AND')
    print('    ### ### EACH WAS RIGHT TO** -- none of them computed the left-hand side. ### This')
    print('    ### act computes it from (53) and (38) and therefore claims it.')
    print('    ### **`the nonempty reach` IS CLAIMED WITH ITS QUALIFICATION IN THE ROW**: the reach')
    print('    ### is non-empty under a bar THIS ACT ITSELF CORRECTED, and the row says so.')

    have_key = {k: ("'%s'" % k) in txt for k in NEW_KEYS}
    have_row = {k: ('"%s"' % k) in txt for k in NEW_KEYS}
    for k in NEW_KEYS:
        print('  %-24s key/row already present : %s / %s' % (k, have_key[k], have_row[k]))
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
        print('    %-24s returns a row : %s  %s'
              % (k, good, 'PASS' if good else '### FAIL ###'))

    print('  ### THE ALIASES:')
    for q in ALIASES + CLAIMED_FROM_UNKEYED:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-42s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### AND THE CONTROL ROW MUST HAND BACK THE FAILURE AND NOT ONLY THE HOLDING:')
    out, _rc = query('did the control hold')
    both = ('FIRST REPORTED VERDICT WAS FAILS' in out) and ('27 of 27' in out.replace('27 OF 27',
                                                                                      '27 of 27'))
    ok = ok and both
    print('    the answer carries BOTH the FAILS and the HOLDS : %s  %s'
          % (both, 'PASS' if both else '### FAIL ###'))
    print('  ### **A ROW THAT ANSWERED *did the control hold* WITH ONLY THE SECOND RUN WOULD BE A')
    print('  ### ### TRUE SENTENCE ASSEMBLED TO GIVE A FALSE IMPRESSION**, which is the exact shape')
    print('  ### this record refuses.')

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the window class` STAYS UNKEYED BECAUSE NO WINDOW WAS OPENED HERE.**')

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
