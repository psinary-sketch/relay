# -*- coding: utf-8 -*-
"""b308_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER SAYS EVERY RESULT KEYED, AND THIS ACT HAS TWO:** ### the instrument itself,
### and the retirement of the escaped-mass artifact FOR THAT INSTRUMENT.

### ### **THE MUST-NOT-HIT ARM IS b202's, MEASURED BEFORE AND AFTER: ### `exact` AND `reproduced`
### ### STAY UNKEYED BECAUSE THEY ARE PROPERTIES AND NOT OBJECTS.** ### An index that answered
### `exact` would be answering a question about a quality of a result, and the record's keys point
### at objects.
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
    "    'local-field-instrument': ['the local field', 'untied radii', 'the two radii',\n"
    "                              'the scaling part', 'the instrument build', 'the frame'],\n"
    "    'escaped-mass-artifact': ['escaped mass', 'the artifact', 'the fold count',\n"
    "                             'nothing to fold'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE LOCAL-FIELD INSTRUMENT, ACT ONE (b308).\n"
    "    (\"local-field-instrument\", \"b308 (an instrument build, act one of the priced item)\",\n"
    "     \"the finite model ties two radii to ONE level index -- b21's V_n is p^(-n)Z_p / p^n Z_p\"\n"
    "     \" = Z/p^(2n), one n governing both the SUPPORT radius and the CONSTANCY radius. ### This\"\n"
    "     \" act UNTIES them and changes nothing else: a frame is a pair (r,s) -- support in\"\n"
    "     \" p^{-r}Z_p, constant on cosets of p^s Z_p -- with b21's chart x = p^{-r} m and b21's\"\n"
    "     \" Haar giving each cell mass p^{-s}. ### **THE MODEL IS THE POINT r = s = n AND THE\"\n"
    "     \" INSTRUMENT IS THE PLANE.** ### The transform carries (r,s) to (s,r); the scaling part\"\n"
    "     \" of the multiplicative group acts as theta(p^k) : V(r,s) -> V(r-k, s+k), so BOTH radii\"\n"
    "     \" move, their SUM does not, and on chart indices the map is the IDENTITY. ### That is the\"\n"
    "     \" direction the model drops. ### Built with a positive control in both polarities on every\"\n"
    "     \" operation before it is used, exact Fraction/int/cyclotomic throughout\",\n"
    "     \"### AN INSTRUMENT BUILT AND CHECKED -- **NOT A RESULT**. ### The reproduction is the\"\n"
    "     \" GATE on the build: the family recovered as SET EQUALITY BOTH DIRECTIONS at every radius\"\n"
    "     \" pair in range at five cells (0 disagreeing); the dimension law and the keystone's own\"\n"
    "     \" (p^n-1)^2 at the diagonal (0 disagreeing); Tr(Pi) equal to the constrained dimension at\"\n"
    "     \" six cells; the compact-part smear zero at all six WITH its mechanism re-derived on the\"\n"
    "     \" instrument's own shells; the annihilation criterion at 80 members reached, 0\"\n"
    "     \" disagreeing, 50 forced zeros confirmed; b295's two registered witnesses re-valued at\"\n"
    "     \" their banked 4/3 and 4/7. ### **EVERY NUMBER IS A BANKED NUMBER RECOMPUTED OR A\"\n"
    "     \" CONTROL, AND TWO INSTRUMENTS AGREEING IS A CHECK ON THE INSTRUMENTS RATHER THAN A\"\n"
    "     \" PROMOTION OF ANY RESULT.** ### NO GRADE MOVES. ### NO NEW MATHEMATICS. ### **NO\"\n"
    "     \" FIRST-LEVEL VALUE AT ANY CELL OR MEMBER THE RECORD DOES NOT ALREADY CARRY** -- that is\"\n"
    "     \" a later act under its own registration, named in the bank and left uncomputed. ###\"\n"
    "     \" **UNTYING THE RADII REMOVES THE WRAPAROUND; IT DOES NOT REMOVE THE TRUNCATION.** ###\"\n"
    "     \" M-2 UNCHANGED\",\n"
    "     \"data/b308_the_local_field_instrument.txt; data/b308_instrument_run.txt;\"\n"
    "     \" tools/b308_local_field.py; tools/b308_reproduction.py; CORRESPONDENCE.md row 128\"),\n"
    "    # ### THE ESCAPED-MASS ARTIFACT, RETIRED FOR ONE INSTRUMENT (b308).\n"
    "    (\"escaped-mass-artifact\", \"b308 (a demonstration, and a retirement of one scope)\",\n"
    "     \"b21 named it -- U maps V_n INTO V_(n+1) and ESCAPES V_n, so THE MODEL'S mod-N WRAPAROUND\"\n"
    "     \" IS EXACTLY THIS ESCAPED MASS FOLDED BACK IN -- and b284 met it and wrote that the\"\n"
    "     \" derivation stands because it is on Q_p, where there is nothing to fold. ### **THIS ACT\"\n"
    "     \" MAKES THAT SENTENCE A COUNT.** ### The model must read theta(p^k) f back in the frame it\"\n"
    "     \" left, which on chart indices is m -> p^k m mod N; the instrument moves the frame\"\n"
    "     \" instead. ### **THE MODEL'S COLLIDED ORDERED PAIRS ARE N(p^k - 1), NONZERO AT EVERY CELL\"\n"
    "     \" AND EVERY DIRECTION TESTED, BY TWO ROUTES; THE INSTRUMENT'S ARE ZERO BY THE SAME TWO\"\n"
    "     \" ROUTES.** ### The escaped mass is exhibited on a vector of the object's own space: b21's\"\n"
    "     \" U sends it to V(n+1, n-1), its smallest containing ball is p^{-(n+1)}Z_p at every cell\"\n"
    "     \" (b21's own support law, recomputed), the escaped Haar mass is an exact nonzero rational,\"\n"
    "     \" and b21's `unitary on L^2(Q_p)` comes out as a normalizing scalar of exactly 1\",\n"
    "     \"### **RETIRED FOR THIS INSTRUMENT, AND FOR NOTHING ELSE.** ### **IT IS NOT RETIRED FOR\"\n"
    "     \" THE MODEL** -- the model's column is nonzero everywhere and any later act scaling on\"\n"
    "     \" Z/p^{2n} meets it again -- **NOR FOR b284**, whose exposure is declared, stands, and is\"\n"
    "     \" not re-verdicted. ### It retires neither W-ORD-FIBER-GENERAL, nor the barrier's scope\"\n"
    "     \" limit, nor the range law, nor the truncation. ### Exposure was decided BY CALL PATH: an\"\n"
    "     \" arm scans for a non-unit pushforward site, this act's own two files carry 5 and ALL are\"\n"
    "     \" declared carriers with 0 undeclared in the operational path, and the owners' sites are\"\n"
    "     \" ruled one by one. ### **AND THE ARM'S LIMIT IS PART OF THE RESULT: IT FINDS A SHAPE AND\"\n"
    "     \" CANNOT TELL A REGROUPING OF AN EXACT FINITE SUM FROM A REPRESENTATION OF A FUNCTION THAT\"\n"
    "     \" LEFT ITS LEVEL** -- that judgement is the seat's and no tool made it. ### M-2 UNCHANGED\",\n"
    "     \"data/b308_the_local_field_instrument.txt; data/b308_instrument_run.txt;\"\n"
    "     \" data/b21_2026-08-18.txt; data/b284_the_scalings_domain.txt; CORRESPONDENCE.md row 129\"),\n"
)

NEW_KEYS = ('local-field-instrument', 'escaped-mass-artifact')
ALIASES = ('the local field', 'untied radii', 'the two radii', 'the scaling part',
           'the instrument build', 'escaped mass', 'the artifact', 'nothing to fold')
MUST_NOT_HIT = ('exact', 'reproduced')


def no_key(out):
    """### TRUE IFF THE INDEX'S OWN VERDICT LINE SAYS `NO KEY`. ### **LINE-SCOPED** -- b302's D7."""
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
    print('b308 -- THE INDEX KEYS. ### THE INSTRUMENT, AND THE ARTIFACT RETIRED FOR IT.')
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

    print('  ### THE ALIASES, EACH OF WHICH RETURNED `NO KEY` BEFORE THIS ACT:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-26s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-22s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`exact` AND `reproduced` STAY UNKEYED BECAUSE THEY ARE PROPERTIES AND NOT')
    print('  ### OBJECTS** -- b202\'s own reason. ### **AND b164\'s LIMIT IS NOT RETIRED: KEYS CLOSE')
    print('  ### FALSE HITS, NOT FALSE MISSES.**')

    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import ferry_scan
    _c, sh = ferry_scan.scan_text(io.open(PATH, encoding='utf-8').read(), [], ferry_scan.stems())
    print('  ### THE INDEX SWEPT AFTER THE WRITE (b305\'s defect, not repeated) : %d stem hit(s)'
          % len(sh))
    for h in sh:
        print('      line %d  %s' % (h[1], h[3][:96]))
    ok = ok and not sh
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
