# -*- coding: utf-8 -*-
"""b302_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE SECOND KEY IS THE REMEDY, NOT AN EXTRA.** ### `unit-requirement` is this act's own
### object and the order names it. ### **`generator-nonvanishing` IS b268's RESULT, WHICH WAS NEVER
### KEYED -- AND THAT IS WHY b300 AND b301 BOTH CARRIED A DEBT b268 HAD PAID TWO DAYS EARLIER.**
### Before this act ran, `generator-nonvanishing`, `nonvanishing`, `support` and `the generator`
### all returned `NO KEY`, and that was recorded in the sealed registration BEFORE the component
### that diagnosed it.
### ### **b164's LIMIT IS NOT RETIRED BY EITHER KEY: ### KEYS CLOSE FALSE HITS, THEY DO NOT CLOSE
### ### FALSE MISSES.** ### What this closes is one specific miss that has already cost two acts.
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
    "    'unit-requirement': ['the unit requirement', 'rule arch-unit', 'arch-unit',\n"
    "                        'space membership suffices', 'what the product asks of a vector'],\n"
    "    'generator-nonvanishing': ['the generator nonvanishing', 'the canonical generator',\n"
    "                              'the generic odd place', 'support of u_p',\n"
    "                              'b226 owed step'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE UNIT REQUIREMENT (b302).\n"
    "    (\"unit-requirement\", \"b302 (a ruling executed against quoted text)\",\n"
    "     \"what von Neumann's incomplete direct product asks of a CHOSEN VECTOR at each place,\"\n"
    "     \" quoted: Definition 3.3.1's `f_alpha in H_alpha for all alpha in I` (at b197's\"\n"
    "     \" at-content grade, the corpus's OCR extract being defective exactly there), its norm\"\n"
    "     \" clause `SUM_v | ||f_v|| - 1 | CONVERGE`, and Lemma 4.1.2's `||f_a|| = 1`.\"\n"
    "     \" ### **THAT IS ALL IT ASKS: MEMBERSHIP IN THE LOCAL HILBERT SPACE AND UNIT NORM.**\"\n"
    "     \" ### No clause mentions an eigenspace, an operator, a sector or a transform, and\"\n"
    "     \" **THE INDEX SET IS NOT PARTITIONED ANYWHERE -- there is no clause distinguishing an\"\n"
    "     \" archimedean index from a finite one.** ### So the author's RULE ARCH-UNIT ('A --\"\n"
    "     \" space membership suffices'), which executes only if the quoted text supports it,\"\n"
    "     \" EXECUTES; the HALT branch was tested and not taken\",\n"
    "     \"### THE AUTHOR'S RULING, EXECUTED AGAINST QUOTED TEXT AND STRIKEABLE. ### **WHAT IT\"\n"
    "     \" DOES IS NARROW THE ORIGINAL WORDING RATHER THAN FULFIL IT**: the b225 ruling asked\"\n"
    "     \" for 'the archimedean unit from the Sonin sector', and that requirement is WITHDRAWN,\"\n"
    "     \" the sector clause retained as DESCRIPTION whose establishment is not required by the\"\n"
    "     \" construction and is NOT CLAIMED. ### b214's c = +1 at rank 2 stands at BENCH and is\"\n"
    "     \" NOT promoted. ### The ruling is named ARCH-UNIT and is NOT applied to the finite\"\n"
    "     \" units, where it would have no bite: b226's u_p is a projector image, in E_1 BY\"\n"
    "     \" CONSTRUCTION. ### M-2 UNCHANGED (SPECIFIED-NOT-STATED)\",\n"
    "     \"data/b302_the_unit_requirement.txt; CORRESPONDENCE.md row 117\"),\n"
    "    # ### THE GENERATOR'S NONVANISHING (b268), KEYED AT b302 BECAUSE IT NEVER WAS.\n"
    "    (\"generator-nonvanishing\", \"b268 (2026-08-31), keyed at b302\",\n"
    "     \"4q P_1 f_(1,1) != 0 AT EVERY ODD PRIME p AT LEVEL 1 -- b226's owed step, PAID.\"\n"
    "     \" ### The route is one line of congruence arithmetic once the owners' objects are\"\n"
    "     \" unfolded, and it delivers more than the nonvanishing: **support(u_p) = N - q\"\n"
    "     \" EXACTLY**, which b226 had recorded as OBSERVED at six cells and explicitly did NOT\"\n"
    "     \" assert as a theorem. ### The hinge is that for ODD q, gcd(q+2, q^2) = 1, so the zero\"\n"
    "     \" set is exactly the q multiples of q. ### Controlled exactly in Z[zeta_N] at eight\"\n"
    "     \" places -- b226's six plus p = 17 and p = 19 -- with 1039 values reduced modulo Phi_N\"\n"
    "     \" and NO floating point deciding anything\",\n"
    "     \"### DERIVES-on-IMP, the imports being the owners' own definitions and the BANKED\"\n"
    "     \" purity identity, and NO NEW IMPORT -- as b268 graded it. ### **THIS ROW EXISTS\"\n"
    "     \" BECAUSE ITS ABSENCE COST TWO ACTS A FALSE OPEN**: b300 and b301 both restated b226's\"\n"
    "     \" step as OWED, pulling it from the act that INCURRED it and never asking whether a\"\n"
    "     \" later act had PAID it, and every query that would have found b268 returned NO KEY.\"\n"
    "     \" ### b164's limit stands: keys close false hits, not false misses.\"\n"
    "     \" ### It pays b226's step and does NOT touch (SPEC-1) -- a support is not a\"\n"
    "     \" contribution. ### M-2 UNCHANGED\",\n"
    "     \"data/b268_generator_nonvanishing.txt; data/b268_run.txt;\"\n"
    "     \" data/b302_the_unit_requirement.txt (the staleness diagnosis)\"),\n"
)


def no_key(out):
    """### TRUE IFF THE INDEX'S OWN VERDICT LINE SAYS `NO KEY`. ### **LINE-SCOPED, AND THAT IS THE
    ### WHOLE OF THE FIX.**

    ### ### **DEFECT FOUND ON THIS TOOL'S FIRST LIVE RUN.** ### The first version tested
    ### `'NO KEY' in out` over the whole output, and ### **THE `generator-nonvanishing` ROW'S OWN
    ### GRADE CELL CONTAINS THE PHRASE "returned NO KEY"** -- because the row records the very miss
    ### it exists to close. ### So the checker read the row's prose as the index's verdict and
    ### reported the key ABSENT while the index was printing it.
    ### ### ### **THAT IS b163's SPECIES AND `W-ORD-ADHOC-CHECK-FIXTURES`'s: ### A CHECK THAT
    ### ### ### CANNOT DISTINGUISH ITS TARGET FROM THE PROSE DESCRIBING IT.** ### The repair is the
    ### scope, not the row -- ### **DELETING THE PHRASE FROM THE ROW WOULD HAVE SILENCED THE CHECK
    ### BY EDITING THE EVIDENCE.**
    """
    for ln in (out or '').splitlines():
        if ln.strip().startswith('### NO KEY'):
            return True
    return False


def verdict_fixture():
    """### **BOTH POLARITIES ON THE LINE-SCOPING ITSELF.**"""
    real = no_key('=====' + NL + '  ### NO KEY.' + NL + '  ### matched no DECLARED key')
    quoted = no_key('    grade    : ... would have found b268 returned NO KEY.')
    return real, quoted


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b302 -- THE INDEX KEYS. ### ONE FOR THIS ACT, ONE AS THE REMEDY FOR A MISS.')
    print('=' * 100)

    have = ["'unit-requirement'" in txt, '"unit-requirement"' in txt,
            "'generator-nonvanishing'" in txt, '"generator-nonvanishing"' in txt]
    print('  unit-requirement   key/row already present : %s / %s' % (have[0], have[1]))
    print('  generator-nonvanishing key/row already present : %s / %s' % (have[2], have[3]))
    written = not all(have)
    if not written:
        print('  ### NOTHING WRITTEN. (idempotent) ### **THE READ-BACK ARMS STILL RUN** -- a tool')
        print('  ### that reports nothing on its second run leaves no evidence of its first.')
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file. Refusing to write into a')
        print('  ### shape this tool cannot see.')
        return 2

    new = txt
    if written and not have[0]:
        new = new.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW, 1)
    if written and not have[1]:
        new = new.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW, 1)
    if written:
        open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(PATH + '.tmp', PATH)

    rv, qv = verdict_fixture()
    print('  VERDICT FIXTURE : fires on the index own NO KEY line : %s ; quiet on'
          ' phrase quoted inside a row : %s' % (rv, not qv))
    ok = rv and not qv
    print('  ### READ BACK BY QUERYING THE INDEX ITSELF:')
    for q in ('unit-requirement', 'generator-nonvanishing'):
        r = subprocess.run([sys.executable, PATH, '--query', q],
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        out = r.stdout or ''
        good = (not no_key(out)) and (q in out) and r.returncode == 0
        ok = ok and good
        print('    %-26s returns a row : %s  %s' % (q, good, 'PASS' if good else '### FAIL ###'))

    # ### THE ARM THAT MATTERS MOST: the aliases that returned NO KEY before this act must now
    # ### REACH b268's result. ### **THAT IS THE MISS THIS KEY EXISTS TO CLOSE.**
    print('  ### THE MISS, RE-QUERIED THROUGH THE ALIASES THAT FAILED BEFORE THIS ACT:')
    for q in ('the generic odd place', 'b226 owed step', 'the canonical generator'):
        r = subprocess.run([sys.executable, PATH, '--query', q],
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        good = not no_key(r.stdout)
        ok = ok and good
        print('    %-26s now reaches b268 : %s  %s' % (q, good, 'PASS' if good else '### FAIL ###'))

    # ### AND THE MUST-NOT-HIT ARM (b202's precedent), so the aliases did not become a net.
    print('  ### MUST-NOT-HIT, so the aliases are a key and not a net:')
    for q in ('nonvanishing', 'the sector'):
        r = subprocess.run([sys.executable, PATH, '--query', q],
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        quiet = no_key(r.stdout)
        ok = ok and quiet
        print('    %-26s still returns NO KEY : %s  %s'
              % (q, quiet, 'PASS' if quiet else '### FAIL -- a nearest string became a hit'))
    print('  ### **`nonvanishing` STAYS UNKEYED BECAUSE IT IS A PROPERTY AND NOT AN OBJECT** --')
    print('  ### b202\'s own reason for refusing it, and it has not changed.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
