# -*- coding: utf-8 -*-
"""b317_index_append.py -- ONE KEY. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES ONE: ### *trace-on-the-object keyed*.** ### Two rows carry it -- the
### number, and the link the number broke -- because a reader asking what this act computed must be
### handed the measurement that undercuts the chain alongside the measurement that landed on it.

### ### **AND IT TAKES OVER AN ALIAS b316 DELIBERATELY LEFT UNKEYED.** ### b316's own index entry
### says `the trace on the space` STAYS UNKEYED ### *because this act did not compute it*. ### **THIS
### ### ACT COMPUTED IT**, so the alias is claimed here, which is the only honest way for that
### sentence of b316's to age.

### ### **THE MUST-NOT-HIT ARM IS b202's.** ### `the sonin space` stays unkeyed -- this act owns a
### TRUNCATION of it and b285's boundary is that a word surviving is not the object surviving. ###
### `the archimedean weil distribution` stays unkeyed -- ### **IT IS THE OTHER SIDE OF THE SOURCE'S
### ### INEQUALITY AND THIS ACT DID NOT COMPUTE IT IN ANY DIRECTION**, and an index that answered it
### would be offering one side where both were asked for.
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
    "    'trace-on-the-object': ['the trace on the space', 'the compressed smeared trace',\n"
    "                   'is the corpus window in the source class', 'the mean-zero column',\n"
    "                   'was the prediction small', 'the trace on the object'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE NUMBER (b317, act two of two).\n"
    "    (\"trace-on-the-object\", \"b317 (a computation on the instrument as certified)\",\n"
    "     \"the source's compressed smeared trace, computed on the object's own space. ###\"\n"
    "     \" **Tr(theta(f) S) OF THEOREM 4.7, ASSEMBLED FROM eq. (61) AND DEFINITION 4.4 ALONE** --\"\n"
    "     \" the scaling action integrated in d*lambda, which by u = x/lambda is the kernel\"\n"
    "     \" K(x,u) = f(x/u)/sqrt(xu), compressed by b316's projector and traced. ### Thirteen\"\n"
    "     \" banked cells, both test functions, the whole registered cutoff. ### **AGAINST A BAR\"\n"
    "     \" SEALED BEFORE ANY VALUE AT ANY BANKED CELL EXISTED (|T| <= |A|/10, scored on the\"\n"
    "     \" largest |T| the whole domain sweep produces), THE REGISTERED PREDICTION SCORES AS SMALL\"\n"
    "     \" AT 13 CELLS OF 13** -- ratios 0.09318 down to 0.00019, with the narrowest cell at 93\"\n"
    "     \" per cent of the bar. ### **AND THE CANCELLATION IS THE BUMP'S OWN, NOT THE\"\n"
    "     \" COMPRESSION'S**: the same compression removes 98.6 per cent of the bump's uncompressed\"\n"
    "     \" trace and only 55 per cent of the mean-zero variant's\",\n"
    "     \"### A NUMBER ON A TRUNCATION, AND ITS LIMITS BELONG IN ITS OWN ENTRY. ### **THE REACH IS\"\n"
    "     \" EMPTY** -- no cell meets the joint 5 per cent bar fixed before the run -- ### **AND THE\"\n"
    "     \" NOISE-FLOOR GATE REFUSES 8 PAIRS OF 12**, so no point verdict is taken from either\"\n"
    "     \" axis and the scoring is a BAND statement. ### The grid-axis drift spike is a RANK STEP\"\n"
    "     \" (80 to 79), not a quadrature error. ### **NO UNIT IS USED ANYWHERE IN THE ACT** and the\"\n"
    "     \" number MAY NOT BE READ AS b300's -- W-ORD-ARCH-MEMBERSHIP is open. ### NO ACT\"\n"
    "     \" RE-VERDICTED. ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b317_the_trace_on_the_object.txt; data/b317_components_run.txt;\"\n"
    "     \" tools/b317_smear.py (the emitting file); CORRESPONDENCE.md row 146\"),\n"
    "    # ### THE LINK THE NUMBER BROKE (b317).\n"
    "    (\"trace-on-the-object\", \"b317 (the sign chain's fifth link, measured)\",\n"
    "     \"the corpus's window is NOT the source's test-function class. ### b316 registered its\"\n"
    "     \" prediction on a chain of five and named each as a way for it to be wrong for a reason\"\n"
    "     \" that has nothing to do with the mathematics. ### Four this act cannot touch. ###\"\n"
    "     \" **THE FIFTH IT MEASURED, AND THE FIFTH IS FALSE**: the source's eq. (54) requires the\"\n"
    "     \" moment INT f(rho) rho^{+-1/2} d*rho to vanish, and the corpus's integral-one bump has\"\n"
    "     \" it at 1.003, 1.010 and 1.024 at a = 1.5, 2, 3. ### **AND FIVE OF THE THIRTEEN CELLS\"\n"
    "     \" ALSO LEAVE eq. (53)'s SUPPORT CONDITION [1/2, 2].** ### A mean-zero variant built from\"\n"
    "     \" three of the corpus's own bumps DOES satisfy both moments, to 2.8e-17\",\n"
    "     \"### A MEASUREMENT ABOUT A WINDOW, NOT A VERDICT ON AN ACT. ### **A PREDICTION WHOSE\"\n"
    "     \" NUMBER LANDS WHILE A LINK IT RESTS ON IS MEASURED WRONG HAS NOT BEEN CONFIRMED BY THE\"\n"
    "     \" LANDING** -- so the prediction SCORED and is NOT CONFIRMED, and the entailment is\"\n"
    "     \" bounded: the correspondence may not be read as identifying the corpus's window with the\"\n"
    "     \" source's class, because that is the thing this act refused. ### **NO ACT IS\"\n"
    "     \" RE-VERDICTED AND NO BANKED MEASUREMENT IS CALLED WRONG** -- naming two quantities\"\n"
    "     \" different is a statement about what they are. ### W-ORD-WINDOW-CLASS filed. ### NO\"\n"
    "     \" GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b317_the_trace_on_the_object.txt; data/b317_rows.json;\"\n"
    "     \" data/b316_the_archimedean_instrument.txt (the chain's own bank);\"\n"
    "     \" CORRESPONDENCE.md row 147\"),\n"
)

NEW_KEYS = ('trace-on-the-object',)
ALIASES = ('the trace on the space', 'the compressed smeared trace',
           'is the corpus window in the source class', 'the mean-zero column',
           'was the prediction small', 'the trace on the object')
MUST_NOT_HIT = ('the sonin space', 'the archimedean weil distribution')


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
    print('b317 -- THE INDEX KEY. ### THE NUMBER, AND THE LINK IT BROKE.')
    print('=' * 100)
    print('  ### MUST-NOT-HIT, MEASURED BEFORE THE WRITE:')
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))

    print('  ### AND THE ALIAS b316 LEFT UNKEYED, MEASURED BEFORE THIS ACT CLAIMS IT:')
    out, _rc = query('the trace on the space')
    was_unkeyed = no_key(out)
    print('    %-36s NO KEY before : %s' % ('the trace on the space', was_unkeyed))
    print('    ### **b316 LEFT IT UNKEYED BECAUSE b316 HAD NOT COMPUTED IT. ### THIS ACT HAS.**')

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
        both = out.count('act      :') >= 2
        ok = ok and good and both
        print('    %-24s returns a row : %s ; returns BOTH halves : %s  %s'
              % (k, good, both, 'PASS' if (good and both) else '### FAIL ###'))
    print('  ### **BOTH HALVES ARE REQUIRED.** ### An index that handed back the number without the')
    print('  ### broken link would be answering *what was computed* and hiding *what it cost the')
    print('  ### chain*, which is the exact shape this record refuses.')

    print('  ### THE ALIASES:')
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
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the sonin space` STAYS UNKEYED BECAUSE THIS ACT OWNS A TRUNCATION OF IT AND NOT')
    print('  ### ### IT** -- b285\'s boundary, applied to this act\'s own product.')
    print('  ### **`the archimedean weil distribution` STAYS UNKEYED BECAUSE IT IS THE OTHER SIDE OF')
    print('  ### ### THE INEQUALITY AND THIS ACT DID NOT COMPUTE IT IN ANY DIRECTION.**')

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
