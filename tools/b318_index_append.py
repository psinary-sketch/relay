# -*- coding: utf-8 -*-
"""b318_index_append.py -- ONE KEY. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES ONE: ### *forced-sign keyed*.** ### Two rows carry it -- the square, and
### the letter -- because a reader asking what the sign change was must be handed the definitional
### finding that dissolves it alongside the computation that exhibited it.

### ### **THE MUST-NOT-HIT ARM IS b202's, AND BOTH ENTRIES ARE THINGS THIS ACT DELIBERATELY DID NOT
### ### DO.** ### `the archimedean weil distribution` stays unkeyed -- ### **THIS ACT COMPUTES
### ### NEITHER SIDE OF THE SOURCE'S INEQUALITY**, and an index that answered it would be offering a
### trace-side number where a distribution was asked for. ### `the rank stable subspace` stays
### unkeyed -- ### **THE SCHEME IS SPECIFIED AND NOT BUILT**, and an index that answered it would be
### handing back a specification where a build was asked for.
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
    "    'forced-sign': ['the forced sign', 'the square form',\n"
    "                   'is the smear the source trace side', 'is the variant positive definite',\n"
    "                   'which letter is the corpus window',\n"
    "                   'why did the mean-zero column change sign'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE SQUARE (b318).\n"
    "    (\"forced-sign\", \"b318 (a computation on the instrument as certified)\",\n"
    "     \"the source's trace side in its square form, computed on the truncation. ### The paper\"\n"
    "     \" says where its positivity lives: the functional is positive definite BY CONSTRUCTION\"\n"
    "     \" only when evaluated at f = g conv g^, where it is Tr(theta(g) S theta(g)^) -- a\"\n"
    "     \" Hilbert-Schmidt norm squared. ### **CELLS AT WHICH THAT SQUARE IS NEGATIVE ANYWHERE:\"\n"
    "     \" 0. ### CELLS AT WHICH b317's SMEAR IS NEGATIVE ANYWHERE: 5.** ### **AND THE FIRST\"\n"
    "     \" DIFFERING CONSTITUENT IS PROVED, NOT ASSERTED**: theta(f)^theta(f) = theta(f^ conv f),\"\n"
    "     \" so the source's square form is the corpus's smear at the AUTOCORRELATION of the window\"\n"
    "     \" where the corpus evaluates it at the window -- two independent code paths agreeing to\"\n"
    "     \" 1.9e-06, 4.2e-06 and 3.4e-05 against a sealed bar of one per cent\",\n"
    "     \"### ONE STATEMENT HERE IS FINITE-DECIDABLE AND THE ACT SAYS WHICH. ### The square is a\"\n"
    "     \" Frobenius norm squared and **square_trace PERFORMS NO SUBTRACTION ANYWHERE**, so its\"\n"
    "     \" nonnegativity is arithmetic; **WHAT IS NOT DECIDABLE IS THAT THE SUM IS THE\"\n"
    "     \" OPERATOR-THEORETIC NORM**. ### **A POSITIVITY THAT HELD IS NOT A THEOREM CONFIRMED** --\"\n"
    "     \" the source proved it; this act checked the truncation does not destroy it. ### **THE\"\n"
    "     \" REACH IS EMPTY, 0 OF 6**, and the noise-floor gate REFUSES 6 pairs of 12, all on the\"\n"
    "     \" domain axis. ### **THE RANK IS THE GRID-AXIS ERROR, MEASURED**: steps that keep the\"\n"
    "     \" rank drift 2.7e-05 to 1.2e-04, the one that changes it (80 to 79) drifts 6.1e-03 to\"\n"
    "     \" 2.3e-02. ### W-ORD-RANK-STABLE-SUBSPACE filed; the scheme is SPECIFIED and NOT BUILT.\"\n"
    "     \" ### **NO UNIT USED. ### W_infinity NOT COMPUTED IN ANY DIRECTION.** ### NO GRADE MOVED.\"\n"
    "     \" ### M-2 UNCHANGED\",\n"
    "     \"data/b318_the_forced_sign.txt; data/b318_components_run.txt;\"\n"
    "     \" tools/b318_square.py (the emitting file); CORRESPONDENCE.md row 148\"),\n"
    "    # ### THE LETTER (b318), AND WHAT IT DOES TO b317's SIGN CHANGE.\n"
    "    (\"forced-sign\", \"b318 (the class of the window, decided)\",\n"
    "     \"the corpus's window is a candidate g and NOT a candidate f. ### Decided by the source's\"\n"
    "     \" own Definition 3.1 -- f is positive definite when its Fourier transform is pointwise\"\n"
    "     \" positive -- applied as a scan at every banked cell. ### **THE MEAN-ZERO VARIANT IS NOT\"\n"
    "     \" POSITIVE DEFINITE AT ANY CELL (min f-hat = -1.3119e-01), AND NEITHER IS THE CORPUS'S\"\n"
    "     \" INTEGRAL-ONE BUMP (-9.8392e-02): 0 OF 13 FOR BOTH.** ### But Theorem 1 puts its\"\n"
    "     \" conditions on g, not on f -- support in [2^-1/2, 2^1/2] and Fourier transform vanishing\"\n"
    "     \" at i/2 AND at 0 -- and **THE VARIANT SATISFIES BOTH VANISHING CONDITIONS AT 13 OF 13\"\n"
    "     \" AND THEOREM 1's SUPPORT INTERVAL AT 3 OF 13 (a = 1.3, 1.35, 1.41)**\",\n"
    "     \"### A DEFINITIONAL FINDING THAT DISSOLVES b317's ANOMALY RATHER THAN RESOLVING IT.\"\n"
    "     \" ### **THE SIGN CHANGE IS NOT A VIOLATION OF ANYTHING**: the source's positivity is\"\n"
    "     \" about Tr(theta(g) S theta(g)^), which stayed positive everywhere, and Tr(theta(f) S) at\"\n"
    "     \" an f outside the class carries no promise. ### **b317's NUMBERS ARE RE-LABELLED AND\"\n"
    "     \" b317 IS NOT RE-VERDICTED** -- correctly computed values of what it computed; its grade\"\n"
    "     \" does not move and its prediction score stands as it stated it. ### The class scan proves\"\n"
    "     \" the NEGATIVE only, and the act uses it in that direction alone. ###\"\n"
    "     \" W-ORD-WINDOW-CLASS UPDATED, not closed: the question is now WHICH LETTER, and what is\"\n"
    "     \" owed is the author's decision. ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b318_the_forced_sign.txt; data/b318_rows.json;\"\n"
    "     \" data/b318_extract_notes.txt (the source, located); CORRESPONDENCE.md row 149\"),\n"
)

NEW_KEYS = ('forced-sign',)
ALIASES = ('the forced sign', 'the square form', 'is the smear the source trace side',
           'is the variant positive definite', 'which letter is the corpus window',
           'why did the mean-zero column change sign')
MUST_NOT_HIT = ('the archimedean weil distribution', 'the rank stable subspace')


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
    print('b318 -- THE INDEX KEY. ### THE SQUARE, AND THE LETTER.')
    print('=' * 100)
    print('  ### MUST-NOT-HIT, MEASURED BEFORE THE WRITE:')
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))

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
    print('  ### **BOTH HALVES ARE REQUIRED.** ### An index that handed back the square without the')
    print('  ### letter would be answering *what was computed* and hiding *what it means for the')
    print('  ### act that asked*, which is the exact shape this record refuses.')

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
    print('  ### **BOTH ARE THINGS THIS ACT DELIBERATELY DID NOT DO**: neither side of the source\'s')
    print('  ### inequality was computed, and the rank-stable scheme is SPECIFIED and NOT BUILT.')

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
