# -*- coding: utf-8 -*-
"""b321_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES TWO: ### `window-opened` AND `identity-control`.**

### ### ### **AND THE HARD PART OF THIS FILE IS NOT THE WRITING, IT IS WHAT THE ROWS MUST SAY WHEN
### ### QUERIED.** ### A reader who asks *did the window come out the right way* must be handed, in
### the same breath, that the sign it came out was ### **FORCED BY THE SHAPE OF THE COMPUTATION** ###
### -- the pole term vanishes for a lawful `f`, so the places sum IS minus the zero side, and the
### zero side is a sum of squares over an ordinate library holding only zeros ON the line.
### ### **A ROW THAT ANSWERED THAT QUESTION WITH `10 OF 10` AND STOPPED WOULD BE A TRUE SENTENCE
### ### ASSEMBLED TO GIVE A FALSE IMPRESSION**, and `G-FORCED` re-measures that it does not.

### ### **`the criterion` IS CLAIMED AND `the window class` IS NOT.** ### This act quotes the
### criterion verbatim and computes a finite instance of its left-hand side, so a reader asking about
### it should reach a row. ### **IT DECIDES NO CLASS**, so `the window class` stays unkeyed and
### `W-ORD-WINDOW-CLASS` stays open.
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
    "    'identity-control': ['the identity control', 'theorem four seven',\n"
    "                        'the remainder integral', 'did the equality hold',\n"
    "                        'is the exponent settled'],\n"
    "    'window-opened': ['window opened', 'the places sum', 'the criterion',\n"
    "                      'did the balance come out negative', 'the prime sum sign',\n"
    "                      'the explicit formula control'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE SECOND AND THIRD THEOREMS AS CONTROLS (b321).\n"
    "    (\"identity-control\", \"b321 (two further theorems as controls on the instrument)\",\n"
    "     \"the instrument tested against an EQUALITY and against the explicit formula. ###\"\n"
    "     \" **THEOREM 4.7 / (83) IS AN EQUALITY**, Tr(theta(f) S) = W_8(f) + INT f(rho^-1)\"\n"
    "     \" eps(rho) d*rho, so by cyclicity b320's margin must be exactly minus the remainder\"\n"
    "     \" integral. ### Computed with the b313 FLIPPED COPY -- the source's exponent, on b313's\"\n"
    "     \" reading of three sites and on no number -- it gives 0.158890, 0.186482, 0.221284 at the\"\n"
    "     \" three covered cells. ### **AND THE INSTRUMENT WALKS TOWARD EACH**: the residual along\"\n"
    "     \" the domain ladder at a = 1.3 falls 0.896557, 0.306328, 0.112555, 0.047182, 0.023224 --\"\n"
    "     \" by a factor of two to three at every step, at all three cells. ### **AND THE EXPLICIT\"\n"
    "     \" FORMULA (148) CLOSES AT ALL THIRTEEN CELLS**, residuals 2.2e-09 to 3.6e-05 against the\"\n"
    "     \" atlas's own sealed TOL = 1e-03, truncation bound never above 1.1e-11\",\n"
    "     \"### A CONTROL THAT HOLDS CERTIFIES THE INSTRUMENT, NOT THE OBJECT. ### **NO THEOREM IS\"\n"
    "     \" PROVED HERE** -- the source proved all three. ### **AND THE ORDER'S CONDITIONAL IS\"\n"
    "     \" REFUTED: it said this act closes the exponent question by measurement IF the identity\"\n"
    "     \" holds. ### IT HELD, AND IT DID NOT.** ### The corpus's own exponent copy passes every\"\n"
    "     \" one of the same arms at 3 of 3 cells; the two copies differ by 0.000981, 0.001937,\"\n"
    "     \" 0.003994 where the instrument's own distance from the equality is 0.023224, 0.020793,\"\n"
    "     \" 0.018808. ### **AN INSTRUMENT CANNOT DISCRIMINATE BETWEEN TWO CANDIDATES THAT LIE\"\n"
    "     \" CLOSER TOGETHER THAN ITS OWN DISTANCE FROM THE ANSWER.** ### b313's READING stands\"\n"
    "     \" alone, where b313 left it. ### **NO BAR WAS MOVED**: one quadrature pair missed the\"\n"
    "     \" sealed 1e-06 and the quadrature did more work rather than the bar less. ### NO ACT\"\n"
    "     \" RE-VERDICTED. ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b321_the_window_opened.txt; data/b321_components_run.txt;\"\n"
    "     \" tools/b321_window.py (the emitting file); tools/e16/b313f_qeps_layer.py;\"\n"
    "     \" CORRESPONDENCE.md row 154\"),\n"
    "    # ### THE WINDOW, AND WHY ITS SIGN IS NOT EVIDENCE (b321).\n"
    "    (\"window-opened\", \"b321 (the finite-instance balance on lawful objects)\",\n"
    "     \"the places sum of Proposition C.1 computed at the ten cells above a = 2^{1/2}, where the\"\n"
    "     \" lawful f = g conv g^# is supported past 2 and the primes enter. ### SUM_v W_v(f) =\"\n"
    "     \" PR - A, every sign quoted from an owner, comes out **NON-POSITIVE AT 10 OF 10 CELLS**.\"\n"
    "     \" ### ### **AND THAT COUNT IS FORCED BY THE SHAPE OF THE COMPUTATION AND IS NOT EVIDENCE\"\n"
    "     \" OF ANYTHING.** ### Two facts collapse it: **(i) THE POLE TERM VANISHES IDENTICALLY**\"\n"
    "     \" for a lawful f -- P = f-tilde(0) + f-tilde(1), and Theorem 1's own vanishing conditions\"\n"
    "     \" force both to zero, worst measured magnitude of order 1e-16 -- so (148) collapses to\"\n"
    "     \" SUM_v W_v = - Z; and **(ii) Z CANNOT BE NEGATIVE**, because f-hat is the squared\"\n"
    "     \" modulus of g-hat (b320 measured it, 13 of 13) and the ordinate library holds only zeros\"\n"
    "     \" ON the line. ### **SO THE TOTAL IS NON-POSITIVE BEFORE A SINGLE PRIME IS SUMMED**\",\n"
    "     \"### A COUNT THAT COULD NOT HAVE COME OUT THE OTHER WAY IS NOT A RESULT. ### **A FINITE\"\n"
    "     \" WINDOW AT A FINITE CUTOFF DECIDES NOTHING GLOBAL** -- 10000 ordinates, eleven primes,\"\n"
    "     \" thirteen cells of one family, against a criterion that quantifies over every lawful g.\"\n"
    "     \" ### A zero OFF the line is exactly what would break the sign and this library contains\"\n"
    "     \" none by construction. ### **ONE THING HERE IS A REAL MEASUREMENT: THE PRIME SUM CHANGES\"\n"
    "     \" SIGN TWICE ALONG THE LADDER** -- positive at 1.5 and 1.7, negative from 1.9 to 2.4,\"\n"
    "     \" positive again at 2.8 and 3.0 -- which is where log 2 falls in an oscillating test\"\n"
    "     \" function and nothing more. ### **THE PRIME SUM EXCEEDS THE MARGIN AT NO CELL.** ### THE\"\n"
    "     \" BALANCE IS INTERPRETED BY NOBODY IN THIS ACT. ### W-ORD-WINDOW-CLASS STAYS OPEN. ### NO\"\n"
    "     \" GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b321_the_window_opened.txt; data/b321_components_run.txt;\"\n"
    "     \" data/b321_registration_2026-09-04.txt (sealed); CORRESPONDENCE.md row 155\"),\n"
)

NEW_KEYS = ('identity-control', 'window-opened')
ALIASES = ('the identity control', 'theorem four seven', 'the remainder integral',
           'did the equality hold', 'is the exponent settled',
           'window opened', 'the places sum', 'the criterion',
           'did the balance come out negative', 'the prime sum sign',
           'the explicit formula control')
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
    print('b321 -- THE INDEX KEYS. ### THE IDENTITY CONTROL, AND THE WINDOW.')
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
        ok = ok and good
        print('    %-24s returns a row : %s  %s' % (k, good, 'PASS' if good else '### FAIL ###'))

    print('  ### THE ALIASES:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-42s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### ### **G-FORCED -- THE ARM THIS FILE EXISTS FOR.**')
    out, _rc = query('did the balance come out negative')
    forced = 'FORCED BY THE SHAPE OF THE COMPUTATION' in out
    nothing = 'DECIDES NOTHING GLOBAL' in out
    ok = ok and forced and nothing
    print('    the answer carries that the sign is FORCED     : %s' % forced)
    print('    ### and that a finite window decides nothing    : %s' % nothing)
    print('  ### **A ROW THAT ANSWERED *did the balance come out negative* WITH `10 OF 10` AND')
    print('  ### ### STOPPED WOULD BE A TRUE SENTENCE ASSEMBLED TO GIVE A FALSE IMPRESSION.**')

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the window class` STAYS UNKEYED: THIS ACT DECIDED NO CLASS.**')

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
