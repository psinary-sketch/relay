# -*- coding: utf-8 -*-
"""b316_index_append.py -- ONE KEY. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES ONE: ### *archimedean-instrument keyed*.** ### Two rows carry it -- the
### build, and the reproduction arm -- because they are one act's two halves and a reader asking
### about the instrument must be handed the half that DID NOT CONFIRM alongside the half that did.

### ### **THE MUST-NOT-HIT ARM IS b202's: ### `the trace on the space` AND `the sonin space` STAY
### ### UNKEYED.** ### The first is act two's number and ### **THIS ACT DID NOT COMPUTE IT** -- an
### index that answered it would be offering a build where a number was asked for. ### The second is
### the SOURCE's object; this act owns a TRUNCATION of it, and ### **b285's BOUNDARY IS THAT A WORD
### ### SURVIVING IS NOT THE OBJECT SURVIVING.**
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
    "    'archimedean-instrument': ['the truncated space', 'is u_inf in the space',\n"
    "                   'does the scaling restrict', 'sonin space instrument',\n"
    "                   'the archimedean instrument', 'which condition breaks'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE INSTRUMENT (b316, act one of two).\n"
    "    (\"archimedean-instrument\", \"b316 (an instrument build, with its own fixtures)\",\n"
    "     \"a computable truncation of the source's own archimedean space. ### **S(1,1) BUILT FROM\"\n"
    "     \" DEFINITION 4.4 AND NOTHING ELSE** -- even functions on [0, X] at N midpoints, with the\"\n"
    "     \" source's inner product (eq. 16), transform normalization (eq. 24), scaling exponent\"\n"
    "     \" (eq. 61) and two vanishing conditions (eq. 72) as linear constraints. ### **THE FIRST\"\n"
    "     \" ARCHIMEDEAN INSTRUMENT THE CORPUS HAS WHOSE VECTORS ARE INSIDE THE OBJECT'S OWN\"\n"
    "     \" SPACE.** ### Dimension 914, 1904, 3888, 3887, 5870 at five truncations and GROWING\"\n"
    "     \" WITHOUT BOUND, which is the source's *infinite dimensional Sonin's space* appearing as\"\n"
    "     \" a measurement. ### **AND THE SOURCE'S SECOND SENTENCE SHARPENED**: the paper says the\"\n"
    "     \" scaling action does not restrict; the instrument says WHICH condition breaks --\"\n"
    "     \" condition one survives EXACTLY at every dilation, and the whole failure is in the\"\n"
    "     \" transform condition, leaking 0.1352 at lambda 1.25 up to 0.4253 at lambda 4\",\n"
    "     \"### AN INSTRUMENT BUILD, AND ITS LIMITS BELONG IN ITS OWN ENTRY. ### **IT CAN decide\"\n"
    "     \" exactly that a vector supported in the unit interval is orthogonal to the space, and\"\n"
    "     \" that condition one survives any dilation at or above one; measure how far a vector\"\n"
    "     \" lies outside, with a discrimination arm that FIRES; measure the scaling leakage; apply\"\n"
    "     \" the compression; accept either test function.** ### **IT CANNOT DECIDE MEMBERSHIP**\"\n"
    "     \" (the next entry), converge to a fixed finite answer under refinement, separate a\"\n"
    "     \" truncation effect from a construction effect, or say anything about the p-adic places\"\n"
    "     \" -- b285's boundary stands and b309's zero does not travel. ### **NO TRACE COMPUTED AND\"\n"
    "     \" NO SMEAR ASSEMBLED**: that is act two, under its own registration. ### NO GRADE MOVED.\"\n"
    "     \" ### M-2 UNCHANGED\",\n"
    "     \"data/b316_the_archimedean_instrument.txt; data/b316_components_run.txt;\"\n"
    "     \" tools/b316_instrument.py (the emitting file); CORRESPONDENCE.md row 144\"),\n"
    "    # ### THE REPRODUCTION ARM, AND THE ONE THAT DID NOT CONFIRM (b316).\n"
    "    (\"archimedean-instrument\", \"b316 (the mandatory reproduction arm)\",\n"
    "     \"what the instrument reproduces of what the record already owns. ### **b292 CONFIRMED BY\"\n"
    "     \" A SECOND AND INDEPENDENT ROUTE**: the corpus's expansion vectors zeta_n pass condition\"\n"
    "     \" one and fail condition two with residual 1.0000 at n = 0,1,2,3 and at every\"\n"
    "     \" truncation, where b292 derived the same failure from the source's statement about\"\n"
    "     \" psi_n. ### The source's own worked inner product RECOVERED to 0.00e+00. ### **AND\"\n"
    "     \" b300's MEMBERSHIP IS *NOT* CONFIRMED**: the derived archimedean unit, built on this\"\n"
    "     \" grid by the corpus's own solver, has residual 0.9455, 0.8023, 0.5527, 0.6033, 0.4902\"\n"
    "     \" across five truncations -- falling with the domain and nowhere near zero. ### The hard-\"\n"
    "     \" cutoff explanation was TESTED AND REFUSED (a smooth taper moves 0.8023 to 0.8020)\",\n"
    "     \"### A REPRODUCTION ARM, AND ONE OF ITS FOUR DID NOT CONFIRM. ### **b300 IS NOT\"\n"
    "     \" RE-VERDICTED AND IS NOT CALLED WRONG** -- b300's derivation is on the WHOLE LINE and\"\n"
    "     \" this is a truncation, and b15's law governs: a finite-place-set object at a finite\"\n"
    "     \" cutoff decides nothing global. ### **AND THE CONTROL THAT WOULD HAVE SETTLED THE\"\n"
    "     \" CONSTRUCTION COULD NOT FIRE**: the asymptotic check confirms the decay and frequency\"\n"
    "     \" but returns 1.1435 and 1.1558 at two NON-eigenvalues against the eigenvalue's 1.1323,\"\n"
    "     \" so by b308's law it is reported as NOT-A-CHECK. ### **THREE CAUSES REMAIN AND THIS ACT\"\n"
    "     \" CHOOSES NONE.** ### **THE INSTRUMENT IS DECLARED NOT YET CERTIFIED FOR MEMBERSHIP AND\"\n"
    "     \" ACT TWO MAY NOT USE IT FOR ONE**; W-ORD-ARCH-MEMBERSHIP filed. ### NO GRADE MOVED. ###\"\n"
    "     \" M-2 UNCHANGED\",\n"
    "     \"data/b316_the_archimedean_instrument.txt; data/b316_rows.json;\"\n"
    "     \" data/b300_the_archimedean_leg.txt (b300's own bank); CORRESPONDENCE.md row 145\"),\n"
)

NEW_KEYS = ('archimedean-instrument',)
ALIASES = ('the truncated space', 'is u_inf in the space', 'does the scaling restrict',
           'sonin space instrument', 'the archimedean instrument', 'which condition breaks')
MUST_NOT_HIT = ('the trace on the space', 'the sonin space')


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
    print('b316 -- THE INDEX KEY. ### THE INSTRUMENT, AND WHAT IT FAILED TO REPRODUCE.')
    print('=' * 100)
    print('  ### MUST-NOT-HIT, MEASURED BEFORE THE WRITE:')
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-24s NO KEY before : %s' % (q, pre[q]))

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
    print('  ### **BOTH HALVES ARE REQUIRED.** ### An index that handed back the build without the')
    print('  ### reproduction arm would be answering *what was built* and hiding *what it could not')
    print('  ### do*, which is the exact shape this record refuses.')

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
        print('    %-24s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the trace on the space` STAYS UNKEYED BECAUSE THIS ACT DID NOT COMPUTE IT**, and')
    print('  ### an index that answered it would hand back a build where a number was asked for.')
    print('  ### **`the sonin space` STAYS UNKEYED BECAUSE THIS ACT OWNS A TRUNCATION OF IT AND NOT')
    print('  ### ### IT** -- b285\'s boundary, applied to this act\'s own product.')

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
