# -*- coding: utf-8 -*-
"""b306_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES `the-difference` AND SAYS EVERY RESULT IS KEYED.** ### This act has two:
### the definitional decision, and the closure of the sweep-scope hole.

### ### **AND ONE OF THEM EXISTS BECAUSE THE INDEX ITSELF CARRIED A DEFECT.** ### b305's row in
### `banked_index.py` held a banned stem -- that act fixed its generator and not its artefact --
### and the extended sweep caught it. ### **A KEY FOR THE SWEEP IS THEREFORE A KEY FOR THE REASON
### THE INDEX IS NOW CLEANER THAN IT WAS**, which is worth finding later.

### ### **THE MUST-NOT-HIT ARM IS b202's, MEASURED BOTH BEFORE AND AFTER THE WRITE:** ###
### **`different` AND `the sign` STAY UNKEYED BECAUSE THEY ARE PROPERTIES AND NOT OBJECTS.**
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
    "    'the-difference': ['the difference', 'the corpus difference',\n"
    "                      'the imbalance', 'the cell-level imbalance',\n"
    "                      'the fourth face-off difference'],\n"
    "    'sweep-scope': ['the sweep scope', 'the shared-target sweep',\n"
    "                   'the correspondence sweep', 'the stem sweep scope'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE CORPUS'S DIFFERENCE IS NOT THE SOURCE'S (b306).\n"
    "    (\"the-difference\", \"b306 (a decision by definitions)\",\n"
    "     \"is the corpus's cell-level imbalance the same object as CC's\"\n"
    "     \" arithmetic-minus-trace difference? ### **NO. ### DIFFERENT.** ### CC's is Theorem 1's\"\n"
    "     \" inequality W_inf(g*g*) >= Tr(theta(g) S theta(g)*), a SINGLE-PLACE statement whose\"\n"
    "     \" finite places enter through eq. (149) and are ZEROED -- not excluded -- by the support\"\n"
    "     \" condition ('so that rational primes are not involved'). ### The corpus's is\"\n"
    "     \" L - R = -(E2even + junction) at cells a^2 in {2,3,4,8,9,12}, verified against b254's\"\n"
    "     \" and b248's own tables. ### **THE FIRST DIFFERING CONSTITUENT IS THE ARCHIMEDEAN SIDE**,\"\n"
    "     \" and b291 is the quotation: 'SO NEITHER PAIRED FAMILY LIES IN THE OBJECT'S ARCHIMEDEAN\"\n"
    "     \" SPACE.' ### A trace compressed ONTO Sonin's space sums over vectors IN it; the corpus's\"\n"
    "     \" sums over vectors provably OUTSIDE it. ### **THE PRIME SIDE DOES MATCH (b305, carried),\"\n"
    "     \" cutoff included -- and a difference of two things is the same object only if both\"\n"
    "     \" are.** ### Four constituents have NO COUNTERPART at all: the smeared operator, the\"\n"
    "     \" compression, W_inf, and the places summed over\",\n"
    "     \"### DECIDED BY DEFINITIONS, CONSTITUENT BY CONSTITUENT. ### All three registered\"\n"
    "     \" falsifiers HOLD. ### **SCOPE: NO MEASUREMENT IS DISTURBED AND NO GRADE MOVES.** ###\"\n"
    "     \" E2even being a different functional says nothing about whether it was measured\"\n"
    "     \" correctly; the junction stays DERIVES, E2even stays at bench, b254's (IMBALANCED)\"\n"
    "     \" stands, b291's finding stands as its own. ### The source is not criticised: its theorem\"\n"
    "     \" is about its own objects at its own window, and **the corpus's window is the\"\n"
    "     \" COMPLEMENTARY choice of the same knob -- the source picks its window so no prime\"\n"
    "     \" enters, the corpus so every prime up to a^2 does.** ### The corpus's test function is\"\n"
    "     \" also outside Theorem 1's class (its bump is normalized to integral 1, so ghat(0) is not\"\n"
    "     \" 0), and the source prices exactly that at -c|ghat(0)|^2 with 13 < c < 17 (Thm 6.11).\"\n"
    "     \" ### W-ORD-SOURCE-METHOD-APPLICABILITY filed. ### NO AGGREGATION IS STATED. ### M-2\"\n"
    "     \" UNCHANGED (SPECIFIED-NOT-STATED)\",\n"
    "     \"data/b306_the_difference.txt; data/b306_difference_run.txt;\"\n"
    "     \" CORRESPONDENCE.md row 124\"),\n"
    "    # ### THE SHARED-TARGET STEM SWEEP (b306).\n"
    "    (\"sweep-scope\", \"b306 (a scope repair, closing a hole b305 named)\",\n"
    "     \"the stem sweep now covers the files EVERY act appends to and NO act swept --\"\n"
    "     \" CORRESPONDENCE.md and banked_index.py. ### b305's own words are the specification:\"\n"
    "     \" 'the sweep runs over this act's files and not over CORRESPONDENCE.md, so the row was\"\n"
    "     \" caught by the bank's hit and not by its own.' ### **THE TOOL REPORTS PER ROW AND DOES\"\n"
    "     \" NOT REFUSE**, because a hit in a shared file may be OLDER than the act running, and the\"\n"
    "     \" row number is the attribution. ### Three hits on the first run, all one stem:\"\n"
    "     \" banked_index.py line 400 (**b305's -- this seat's own, where the fix touched the\"\n"
    "     \" generator and not the generated artefact; REPAIRED**); CORRESPONDENCE.md row 101\"\n"
    "     \" (b284's, a defect when written since the stem entered the list at b142, which the old\"\n"
    "     \" sweep could not see; NOT REWRITTEN); row 2 (predates b142, so not a defect -- a ban is\"\n"
    "     \" not retroactive)\",\n"
    "     \"### A SCOPE REPAIR, NOT A RESULT. ### **THE BOUNDARY THIS ACT DREW: REPAIR WHAT THIS\"\n"
    "     \" SEAT WROTE AND MIS-FIXED; FILE WHAT ANOTHER ACT OWNS** -- the append-only law governs\"\n"
    "     \" the difference between CANNOT and WILL NOT. ### The stems are READ from\"\n"
    "     \" ferry_scan.stems() and never copied, so a stem added or retired moves the sweep with\"\n"
    "     \" it. ### Fixtures on both polarities AND on the row-attribution arm, because a sweep\"\n"
    "     \" that found a hit but could not name its row would leave an act unable to tell its own\"\n"
    "     \" row from an ancestor's. ### W-ORD-ANCESTOR-ROW-b284 filed as a POINTER, not a repair.\"\n"
    "     \" ### NO GRADE MOVES. ### M-2 UNCHANGED\",\n"
    "     \"data/b306_the_difference.txt; data/b306_stem_scope.txt;\"\n"
    "     \" CORRESPONDENCE.md row 125\"),\n"
)

NEW_KEYS = ('the-difference', 'sweep-scope')
ALIASES = ('the difference', 'the imbalance', 'the shared-target sweep',
           'the correspondence sweep')
MUST_NOT_HIT = ('different', 'the sign')


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
    print('b306 -- THE INDEX KEYS. ### TWO RESULTS, KEYED BY THE ACT THAT PRODUCED THEM.')
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
        print('  %-20s key/row already present : %s / %s' % (k, have_key[k], have_row[k]))
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
        print('    %-20s returns a row : %s  %s' % (k, good, 'PASS' if good else '### FAIL ###'))

    print('  ### THE ALIASES, EACH OF WHICH RETURNED `NO KEY` BEFORE THIS ACT:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-28s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-24s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`different` AND `the sign` STAY UNKEYED BECAUSE THEY ARE PROPERTIES AND NOT')
    print('  ### OBJECTS** -- b202\'s own reason. ### **AND b164\'s LIMIT IS NOT RETIRED.**')

    # ### AND THE ARM THIS ACT OWES ITSELF: ### **THE INDEX MUST BE STEM-CLEAN AFTER THE WRITE.**
    # ### b305 wrote a row carrying a banned stem and its own sweep could not see it.
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
