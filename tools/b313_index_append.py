# -*- coding: utf-8 -*-
"""b313_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES ONE -- `the-exponent` -- AND SAYS EVERY RESULT KEYED.** ### The act has
### two: the residue's verdict, and what the convention does account for.

### ### **THE MUST-NOT-HIT ARM IS b202's: ### `the convention` AND `the archimedean term` STAY
### ### UNKEYED.** ### The first is the word this act's whole finding turns on and is exactly the
### query most likely to be typed by someone wanting a verdict the act did not give; the second is
### a TERM OF AN IDENTITY that other acts own at their own grades, and ### **AN INDEX THAT ANSWERED
### ### EITHER WOULD BE OFFERING A MEASUREMENT OF ONE TERM AS THOUGH IT WERE A STATEMENT ABOUT THE
### ### WHOLE.**
### ### **AND TWO QUERIES ARE DELIBERATELY NOT IN THAT ARM, BECAUSE THEY ALREADY HIT SOMETHING
### ### ELSE AND THIS ACT DID NOT PUT IT THERE:** ### `the residue` reaches `w-union` and
### `the identity` reaches an earlier act's row. ### **PUTTING AN ALREADY-HIT QUERY IN A
### ### MUST-NOT-HIT ARM WOULD MAKE THE ARM FAIL FOR SOMEBODY ELSE'S REASON**, which is a control
### that reports the wrong act.
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
    "    'the-exponent': ['the flip', 'the remainder under the source normalization',\n"
    "                    'did the residue collapse', 'the exponent check'],\n"
    "    'convention-share-of-the-residue': ['what the convention accounts for',\n"
    "                    'the decay under the flip', 'the one-power shift'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE RESIDUE IS NOT THE EXPONENT (b313).\n"
    "    (\"the-exponent\", \"b313 (a computation, and a negative one)\",\n"
    "     \"b312 identified the corpus's archimedean remainder as differing from the source's by a\"\n"
    "     \" factor of rho; **THIS ACT RAN THE CHECK b312 FILED AND THE RESIDUE DID NOT COLLAPSE.**\"\n"
    "     \" ### In a COPY of the instrument -- the owner files untouched -- the remainder side was\"\n"
    "     \" recomputed under the source's exponent, everything else byte-identical.\"\n"
    "     \" ### **resid = Tr - A - E2 FELL FROM (4.0486, 3.3740, 3.0478, 2.5208, 2.4540, 2.3134)\"\n"
    "     \" TO (3.7150, 2.9792, 2.6347, 2.0917, 2.0242, 1.8834)** at a^2 = 2, 3, 4, 8, 9, 12 --\"\n"
    "     \" ratios 0.9176 to 0.8141, a shrinkage of 8%% to 19%% with the order of magnitude kept at\"\n"
    "     \" every cell. ### **A AND Tr DO NOT MOVE AT ALL**, measured and not asserted\",\n"
    "     \"### A MEASUREMENT, AND A NEGATIVE ONE. ### **IT DOES NOT MEAN THE FLIP WAS WRONG: the\"\n"
    "     \" exponent is fixed by the source's own definition and by NOTHING the residue does, and\"\n"
    "     \" b312 decided which function the remainder IS by unfolding definitions.** ### **NO\"\n"
    "     \" BANKED NUMBER IS CALLED WRONG, NO ACT IS RE-VERDICTED, NO GRADE MOVED, NO TARGET WAS\"\n"
    "     \" NAMED AND NO FIT WAS PERFORMED.** ### Controls: the transcribed loop reproduces b38's\"\n"
    "     \" month-old banked table to 4.98e-05 (its own display rounding); the copy with the\"\n"
    "     \" exponent RESTORED reproduces the owner 78/78 BITWISE; the flip is a pointwise rho\"\n"
    "     \" factor to 5.55e-16. ### The third and fourth face-offs are NOT re-read. ### M-2\"\n"
    "     \" UNCHANGED\",\n"
    "     \"data/b313_the_exponent.txt; data/b313_components_run.txt; data/b313_flip_run.txt;\"\n"
    "     \" CORRESPONDENCE.md row 138\"),\n"
    "    # ### WHAT THE CONVENTION DOES ACCOUNT FOR (b313).\n"
    "    (\"convention-share-of-the-residue\", \"b313 (a measurement at six cells)\",\n"
    "     \"the flip is **EXACTLY MULTIPLICATION BY rho**, measured to 5.55e-16 across all 240 grid\"\n"
    "     \" points, so every consequence is a one-power shift. ### b264's ladder, re-run under the\"\n"
    "     \" flip at its own reach with the noise-floor gate in the path (NRES = 7; even floor modes\"\n"
    "     \" 8 and 10, and what excluding them removes PRINTED at 1e-11 to 1e-15): **the even\"\n"
    "     \" sector's decay moves from rho^(-3/2) to rho^(-1/2) and b264's measured leading constant\"\n"
    "     \" does not move at all** -- the two scaled columns agree to 1.09e-11 at every cell. ###\"\n"
    "     \" **AND THE BANKED CROSS-CHECK IS SHOWN INSENSITIVE, AS b312 DERIVED**: eps'(1+) is\"\n"
    "     \" BITWISE identical under both conventions\",\n"
    "     \"### AN INSTRUMENT FINDING, ROUTED AND NOT FILED. ### **SCOPE: the convention mismatch\"\n"
    "     \" accounts for BETWEEN 8%% AND 19%% OF THE RESIDUE AT SIX CELLS. ### IT DOES NOT ACCOUNT\"\n"
    "     \" FOR THE REST, AND NOTHING HERE SAYS WHAT DOES.** ### Routed to the author as an\"\n"
    "     \" ERRATA-class candidate on the E1 precedent (E-2026-08-31-1): the owner files untouched,\"\n"
    "     \" the correction of record in the bank, because THE RECORD DOES NOT SILENTLY OVERWRITE\"\n"
    "     \" ITSELF. ### **WHAT IT WOULD AFFECT IF FILED: every banked number through those three\"\n"
    "     \" call paths is a computation of the corpus's own function rather than the source's -- A\"\n"
    "     \" STATEMENT ABOUT WHAT THE NUMBERS ARE COMPUTATIONS OF, NOT A CLAIM THAT ANY IS WRONG.**\"\n"
    "     \" ### W-ORD-A-PLUS-E2 and W-ORD-CONVENTION-SWEEP filed. ### M-2 UNCHANGED\",\n"
    "     \"data/b313_the_exponent.txt; data/b313_rows.json; data/b264_rows.json (the reference\"\n"
    "     \" ladder); CORRESPONDENCE.md row 139\"),\n"
)

NEW_KEYS = ('the-exponent', 'convention-share-of-the-residue')
ALIASES = ('the flip', 'the remainder under the source normalization',
           'did the residue collapse', 'the exponent check',
           'what the convention accounts for', 'the one-power shift')
MUST_NOT_HIT = ('the convention', 'the archimedean term')


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
    print('b313 -- THE INDEX KEYS. ### THE MEASUREMENT, AND THE CONVENTION\'S SHARE.')
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
        print('  %-34s key/row already present : %s / %s' % (k, have_key[k], have_row[k]))
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
        print('    %-34s returns a row : %s  %s' % (k, good, 'PASS' if good else '### FAIL ###'))

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
        print('    %-24s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the convention` AND `the archimedean term` STAY UNKEYED.** ### This act')
    print('  ### measured ONE TERM of an identity under two conventions and said nothing about the')
    print('  ### identity itself; an index answering either query would be offering that')
    print('  ### measurement as a statement about the whole, which is the reading the act refuses.')
    print('  ### **AND TWO OBVIOUS CANDIDATES ARE DELIBERATELY NOT IN THIS ARM:** ### `the residue`')
    print('  ### already reaches `w-union` and `the identity` already reaches an earlier act, and')
    print('  ### NEITHER was put there by this act. ### **A MUST-NOT-HIT ARM OVER AN ALREADY-HIT')
    print("  ### QUERY FAILS FOR SOMEBODY ELSE'S REASON, WHICH IS A CONTROL THAT REPORTS THE")
    print('  ### WRONG ACT.** ### They are recorded here instead, where a reader can act on them.')

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
