# -*- coding: utf-8 -*-
"""b310_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES BOTH: `smear-collapse` AND `fixed-point-silence`.**

### ### **THE MUST-NOT-HIT ARM IS b202's, MEASURED BEFORE AND AFTER: ### `the branch` AND
### ### `the mass` STAY UNKEYED.** ### Neither is this record's object: the first is a disjunction
### nobody has settled, the second a quantity whose ownership is exactly what is undecided.
### ### **AN INDEX THAT ANSWERED EITHER WOULD BE ANSWERING A QUESTION THE RECORD HAS NOT SETTLED**,
### which is worse than a miss -- b164's limit runs the other way here.
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
    "    'smear-collapse': ['the smear', 'the identity term', 'the assembled smear',\n"
    "                      'the source construction at a finite place'],\n"
    "    'fixed-point-silence': ['the fixed-point sentence', 'the signed count',\n"
    "                           'the finite side closure', 'off-ball fixed points'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE SMEAR COLLAPSES (b310).\n"
    "    (\"smear-collapse\", \"b310 (a computation and a derivation)\",\n"
    "     \"the source's own construction -- 'one can associate to a test function f the trace\"\n"
    "     \" Tr(theta(f) S)' -- assembled on the b308 instrument. ### **AT A FINITE PLACE THE\"\n"
    "     \" SCALING PART OF Q_p^x IS p^Z, WHICH IS DISCRETE**, so the source's integral over it is\"\n"
    "     \" a SUM over the powers of the prime with the test function evaluated at those powers:\"\n"
    "     \" T(w) = SUM over k of w_k Tr(theta(p^k) Pi). ### The weight is SYMBOLIC -- no bump is\"\n"
    "     \" chosen, so no class question arises and no price is paid -- and the sum is finite\"\n"
    "     \" because the source's test functions are compactly supported. ### **WITH b309's ZEROS AT\"\n"
    "     \" EVERY NONZERO POWER, EXACTLY ONE TERM SURVIVES: T(w) = w_0 (p^n - 1)^2.** ### Seven\"\n"
    "     \" cells, every carried power, 0 terms surviving away from the identity; the zeros are NOT\"\n"
    "     \" substituted in -- every term is formed and added\",\n"
    "     \"### A COMPUTATION AND A DERIVATION, general in p, n and the weight, with the seven-cell\"\n"
    "     \" table as the CHECK and not the proof. ### **THE SURVIVING TERM CONTAINS THE WEIGHT AT\"\n"
    "     \" THE IDENTITY AND THE CONSTRAINED DIMENSION, AND NOTHING ELSE: NO log p, NO SAMPLING AT\"\n"
    "     \" THE PRIME'S POWERS, NO DEPENDENCE ON THE WEIGHT AWAY FROM THE IDENTITY** -- measured\"\n"
    "     \" with a tail nonzero at every carried power, and with the discriminating arm beside it.\"\n"
    "     \" ### **SCOPE: this is what the construction returns AT A FINITE PLACE, ON THIS OBJECT,\"\n"
    "     \" IN THIS COMPRESSION. ### THE SOURCE WORKS AT THE ARCHIMEDEAN PLACE, WHERE THE GROUP IS\"\n"
    "     \" CONTINUOUS AND NONE OF THIS DERIVATION APPLIES** -- named, not derived; b285's boundary\"\n"
    "     \" stands. ### b309's zero is CARRIED, not re-derived. ### Two terminals, zero axioms,\"\n"
    "     \" certifying ARITHMETIC and NOT the collapse. ### NO AGGREGATION IS STATED. ### M-2\"\n"
    "     \" UNCHANGED\",\n"
    "     \"data/b310_the_smear_collapses.txt; data/b310_components_run.txt;\"\n"
    "     \" SIDE-global-section/Core/SmearCollapseShadow.lean; CORRESPONDENCE.md row 132\"),\n"
    "    # ### THE FIXED-POINT SENTENCE AND ITS BEARING (b310).\n"
    "    (\"fixed-point-silence\", \"b310 (a derivation, and a bearing that is never a decision)\",\n"
    "     \"b304 computed the COMPACT part of the local multiplicative group and found its smear\"\n"
    "     \" over the units zero; b309 computed the SCALING part and found it zero at every nonzero\"\n"
    "     \" power. ### **THOSE ARE ONE STATEMENT: Tr(theta(t) Pi) IS A SIGNED COUNT OF THE OFF-BALL\"\n"
    "     \" POINTS t FIXES, IN THE TWO CONGRUENCES THE OBJECT'S TWO CONDITIONS IMPOSE, WEIGHTED BY\"\n"
    "     \" THE EMBEDDING'S HAAR FACTOR.** ### At t = 1 every off-ball point is fixed and the count\"\n"
    "     \" is (p^n - 1)^2; at a nonzero power NOTHING off the ball is fixed, because p^k - 1 is a\"\n"
    "     \" unit, and the only point fixed is the one place the object must vanish. ### **AT A UNIT\"\n"
    "     \" OTHER THAN 1 THE COUNT IS GENERALLY NONZERO -- b304's zero is the SUM over the units,\"\n"
    "     \" not a per-unit vanishing, and the two halves are NOT the same kind of zero.** ###\"\n"
    "     \" Checked against b304's own trace_scaled at every unit and b309's reduced sum at every\"\n"
    "     \" carried power, 0 disagreeing\",\n"
    "     \"### A DERIVATION, AND A BEARING THAT IS NEVER A DECISION. ### At a finite place the\"\n"
    "     \" source's construction carries NO ARITHMETIC; the prime's contribution lives in the\"\n"
    "     \" local distribution the source integrates AGAINST -- eq. (149), read at content by b305\"\n"
    "     \" -- which carries the log p and samples at exactly the powers this trace does not read.\"\n"
    "     \" ### **THE BEARING: THE FINITE SIDE CANNOT SUPPLY THE FIRST-LEVEL MASS THROUGH THE\"\n"
    "     \" OBJECT**, the coefficient at p^1 being exactly zero. ### On b263's three properties,\"\n"
    "     \" for candidates of THIS CLASS: **(SPEC-1) CANNOT be met** -- the one place it demands\"\n"
    "     \" weight is exactly where the zero sits; **(SPEC-3) CAN be met**; **(SPEC-2) IS NOT\"\n"
    "     \" DECIDED BY THIS ACT.** ### **SCOPE: NOT A DECISION ON b262's BRANCH** (b262's own\"\n"
    "     \" sentence is a REQUIREMENT on the archimedean side and expressly not a claim that it\"\n"
    "     \" fails; the disjunction is b263's FORMULATION, not b262's wording); **NOT A VERDICT ON\"\n"
    "     \" M-2**, which stays (SPECIFIED-NOT-STATED) under b263's own 'these exclude; they do not\"\n"
    "     \" determine'; **NOT A CLAIM THAT THE FINITE SIDE CONTRIBUTES NOTHING** -- a distribution\"\n"
    "     \" is not a trace on a space; **AND NOT AN ARGUMENT FOR THE ARCHIMEDEAN BRANCH**, where\"\n"
    "     \" this act derives nothing. ### M-2 UNCHANGED\",\n"
    "     \"data/b310_the_smear_collapses.txt; data/b263_top_level_silence.txt (SPEC-1..3);\"\n"
    "     \" data/b262_junction_limit.txt (its own sentence); CORRESPONDENCE.md row 133\"),\n"
)

NEW_KEYS = ('smear-collapse', 'fixed-point-silence')
ALIASES = ('the smear', 'the identity term', 'the assembled smear',
           'the fixed-point sentence', 'the signed count', 'off-ball fixed points')
MUST_NOT_HIT = ('the branch', 'the mass')


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
    print('b310 -- THE INDEX KEYS. ### THE COLLAPSE, AND THE FIXED-POINT SENTENCE.')
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
        print('    %-30s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-22s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the branch` AND `the mass` STAY UNKEYED BECAUSE NEITHER IS THIS RECORD\'S')
    print('  ### OBJECT: one is a disjunction nobody has settled, the other a quantity whose')
    print('  ### ownership is exactly what is undecided.** ### An index answering either would be')
    print('  ### answering a question the record has not settled.')

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
