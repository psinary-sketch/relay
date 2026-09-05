# -*- coding: utf-8 -*-
"""b326_index_append.py -- TWO KEYS, THREE ROWS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTMETHOD`.** ### A reader who asks *does the
### instrument see a failing hypothesis* must be handed ### **NOT ON THE ARC'S FAMILY, TO a = 400**
### ### -- with the reason (the off-line terms come out positive on `g conv g^#` for this seed), the
### aimed family's separate line, and the priced family that could. ### A row that handed back
### `DOES NOT SEE IT` as a verdict on the method would be a true sentence assembled to mislead.

### ### **AND THE SECOND ARM IS `G-NOTIMPEACHED`.** ### A reader who asks about b325's crossing must
### be handed that it was the halved kernel's artefact, that the closure decided it, AND that b325's
### verdict stands and is stronger -- a withdrawn PRICE is not a re-verdicted act.

### ### **`the archimedean membership` AND `the window class` STAY UNKEYED.**
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
    "    'the-reach': ['the reach', 'the crossing region', 'both windows extended',\n"
    "                  'the closure for both', 'the halved kernel', 'the missing half',\n"
    "                  'the withdrawn crossing', 'a test this family cannot fail',\n"
    "                  'the aimed family'],\n"
    "    'epstein-zeros': ['epstein zeros', 'the epstein zeros', 'the on-line epstein zeros',\n"
    "                      'the completeness census', 'the off-line zeros located',\n"
    "                      'the epstein library', 'zeros on the line'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE REACH -- THE VERDICT (b326).\n"
    "    (\"the-reach\", \"b326 (a computation on the explicit-formula instrument; the verdict)\",\n"
    "     \"both windows extended with every prime and every representation number to a = 400,\"\n"
    "     \" twenty-six cells: **ZETA KEEPS THE PERMITTED SIGN AT EVERY CELL; SO DOES THE EPSTEIN\"\n"
    "     \" FUNCTION** -- no crossing at this reach. ### The explicit formula closes for zeta at 26\"\n"
    "     \" of 26 and for the Epstein function, with every located off-line zero, at 21 of 21 below\"\n"
    "     \" the library's ceiling. ### **VERDICT: DOES NOT SEE IT AT THE ARC'S FAMILY TO a = 400,\"\n"
    "     \" AND AT A DECLARED AIMED FAMILY** (cos(omega v) on every bump, omega = 16.290216, the\"\n"
    "     \" banked off-line height). ### The navigator's expectation REFUTED in its first half (the\"\n"
    "     \" priced crossing was an artefact) and MET in its second (zeta negative throughout)\",\n"
    "     \"### A FAMILY VERDICT IS NOT A METHOD VERDICT. ### The reason from the numbers: on\"\n"
    "     \" f = g conv g^# the off-line four-term sums come out POSITIVE for a seed whose transform\"\n"
    "     \" keeps its sign across the off-line real part (+1.29 of 25.4 at a = 1.3; aimed, 92 to 98\"\n"
    "     \" per cent of the zero side and still positive), so the failing function's places sum is\"\n"
    "     \" minus a sum of squares plus a positive correction -- the permitted sign for the same\"\n"
    "     \" reason zeta's is. ### **THE FAMILY THAT COULD SEE IT NEEDS A SIGN CHANGE ACROSS beta AND\"\n"
    "     \" 1 - beta**, priced at one act, not built. ### **THE ENTAILMENT AT EXACTLY ITS SCOPE: the\"\n"
    "     \" zeta window at this reach is not a passed test but a test this family cannot fail**; the\"\n"
    "     \" arc's *could not have come out otherwise* is true of the library at the arc's cells and,\"\n"
    "     \" on this family, of the method to a = 400. ### NOTHING ABOUT h2 OR THE ROSTER. ### NO\"\n"
    "     \" GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b326_the_reach.txt; data/b326_windows_run.txt; data/b326_closure_run.txt;\"\n"
    "     \" data/b326_registration_2026-09-04.txt (sealed before any run); CORRESPONDENCE.md row 164\"),\n"
    "    # ### THE REACH -- THE KERNEL THE CLOSURE DECIDED (b326).\n"
    "    (\"the-reach\", \"b326 (the closure, and the prior act's kernel)\",\n"
    "     \"a derivation written into the registration BEFORE any run: the Epstein archimedean\"\n"
    "     \" kernel is 2 Re(gamma_Q'/gamma_Q) = 2 Re psi(1/2 + iu) - 2 log(2pi/sqrt23), exactly as\"\n"
    "     \" zeta's atlas kernel is 2 Re(gamma_R'/gamma_R); b325's kernel_q was named as one half of\"\n"
    "     \" it. ### **THE CLOSURE DECIDED IT**: derived kernel closes at 21 of 21 cells below the\"\n"
    "     \" ceiling; b325's fails at 21 of 21, and at every one the residual equals the missing half\"\n"
    "     \" to within the bar (+2.2495 against 2.249540 at a = 3). ### **b325's PRICED CROSSING AT\"\n"
    "     \" a ~ 22 WAS THE HALVED CHANNEL'S ARTEFACT AND IS WITHDRAWN**: the true places sum there is\"\n"
    "     \" -0.374; the +0.017 reappears under b325's kernel and nowhere else\",\n"
    "     \"### **b325 IS NOT RE-VERDICTED.** ### Its DOES NOT SEE IT at the arc's cells stands and\"\n"
    "     \" is stronger (the true places sums are twice as negative); what is withdrawn is a PRICE,\"\n"
    "     \" by the measurement b325 reported as blocked. ### Its sealed registration is not edited;\"\n"
    "     \" the defect is filed as a sealed-bar-found-defective row for the next fold; the internal\"\n"
    "     \" confinement keystone gains an appended correcting line with b325's block visible above\"\n"
    "     \" it. ### **THE LIBRARY THE ORDER NAMED (two banked off-line zeros) FAILED AT 15 CELLS**\"\n"
    "     \" and the fourth link -- completeness -- was walked to fifteen unbanked zeros. ### The\"\n"
    "     \" corpus's census is not called wrong: it banked what lay below t = 33. ### NO GRADE MOVED.\"\n"
    "     \" ### NO ACT RE-VERDICTED. ### M-2 UNCHANGED\",\n"
    "     \"data/b326_the_reach.txt; data/b326_closure_run.txt (the link walked); tools/b326_windows.py\"\n"
    "     \" (kernel_q_derived, fixture (iv)); data/b326_closure_run_first_defective.txt (kept);\"\n"
    "     \" CORRESPONDENCE.md row 165\"),\n"
    "    # ### THE EPSTEIN ZEROS (b326).\n"
    "    (\"epstein-zeros\", \"b326 (the zero library, two routes, every box)\",\n"
    "     \"the Epstein function's zeros on the line to T = 150 by the corpus's own argument-principle\"\n"
    "     \" census run at Re s = 1/2, its constants rebound for the height (K = 240, dps = 119 -- the\"\n"
    "     \" registered dps 60 FAILED ITS OWN GATE, the cancellation being against the pole term,\"\n"
    "     \" e^{pi t/2}/t^2): **146 ZEROS, EVERY ONE AGREED BY AN INDEPENDENT SECOND ROUTE** (Z_Q by\"\n"
    "     \" regularized incomplete gammas, mpmath.findroot), 299 of 299 boxes holding exactly their\"\n"
    "     \" sign-change count (one close pair 0.015 apart resolved by a finer scan). ### The\"\n"
    "     \" completeness census over sigma in [0.52, 1.50] to t = 150: **SEVENTEEN OFF-LINE ZEROS,\"\n"
    "     \" FIFTEEN UNBANKED**, each by both routes; 146 + 2 x 17 = 180 against a main term of 178.6\",\n"
    "     \"### THE CENSUS'S CAVEAT ANSWERED, NOT WAVED: a line scan counts what lies ON the line, the\"\n"
    "     \" box windings say what lies within 0.02 of it, and the completeness census says what lies\"\n"
    "     \" off it -- the abscissa 1.50 is where SUM r_Q(k) k^{-3/2} = 1.38 < 2 makes a zero impossible.\"\n"
    "     \" ### The two banked off-line zeros refine to 0.953260 + 16.290216i and 0.797997 +\"\n"
    "     \" 29.551761i inside their rectangles and reappear in the completeness census. ### **THE\"\n"
    "     \" CORPUS'S CENSUS IS NOT CALLED WRONG**: it banked what lay below t = 33 and was right; the\"\n"
    "     \" confinement keystone's finding is strengthened from two instances to seventeen. ### The\"\n"
    "     \" library is COMPLETE TO T = 150 AND NO HIGHER, a cap set by price. ### NO GRADE MOVED\",\n"
    "     \"data/b326_epstein_zeros.json; data/b326_zeros_run.txt; data/b326_offline.json;\"\n"
    "     \" data/b326_offline_run_150.txt; tools/b326_zeros.py; tools/b326_offline.py;\"\n"
    "     \" tools/e16/epstein_census.py (the evaluator, rebound not edited)\"),\n"
)

NEW_KEYS = ('the-reach', 'epstein-zeros')
ALIASES = ('the reach', 'the crossing region', 'the halved kernel', 'the missing half',
           'the withdrawn crossing', 'a test this family cannot fail', 'the aimed family',
           'epstein zeros', 'the completeness census', 'the epstein library', 'zeros on the line')
MUST_NOT_HIT = ('the archimedean membership', 'the window class')


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
    print('b326 -- THE INDEX KEYS. ### THE REACH, AND THE EPSTEIN ZEROS.')
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
    need = {'the-reach': 2, 'epstein-zeros': 1}
    for k in NEW_KEYS:
        out, rc = query(k)
        good = (not no_key(out)) and (k in out) and rc == 0
        n = out.count('act      :')
        enough = n >= need[k]
        ok = ok and good and enough
        print('    %-24s returns a row : %s ; returns %d row(s), %d required  %s'
              % (k, good, n, need[k], 'PASS' if (good and enough) else '### FAIL ###'))

    print('  ### THE ALIASES (each must reach one of THIS act\'s keys):')
    for q in ALIASES:
        out, _rc = query(q)
        good = (not no_key(out)) and any(k in out for k in NEW_KEYS)
        ok = ok and good
        print('    %-46s reaches a b326 key : %s  %s' % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### ### **G-NOTMETHOD -- THE ARM THIS FILE EXISTS FOR.**')
    out, _rc = query('the reach')
    a1 = 'A FAMILY VERDICT IS NOT A METHOD VERDICT' in out
    a2 = 'SIGN CHANGE ACROSS beta AND' in out
    a3 = 'a test this family cannot fail' in out
    ok = ok and a1 and a2 and a3
    print('    the answer refuses the method reading BY NAME       : %s' % a1)
    print('    ### and names the family that could see it          : %s' % a2)
    print('    ### and carries the entailment at its scope         : %s' % a3)
    print('  ### ### **G-NOTIMPEACHED -- THE SECOND ARM.**')
    out2, _rc2 = query('the halved kernel')
    b1 = 'b325 IS NOT RE-VERDICTED' in out2
    b2 = 'MISSING HALF' in out2.upper()
    b3 = 'WITHDRAWN' in out2
    ok = ok and b1 and b2 and b3
    print('    the answer says b325 is NOT re-verdicted            : %s' % b1)
    print('    ### and carries the missing half                    : %s' % b2)
    print('    ### and the withdrawn price                         : %s' % b3)
    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))

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
