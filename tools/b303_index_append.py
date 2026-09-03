# -*- coding: utf-8 -*-
"""b303_index_append.py -- THREE KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER SAYS EVERY RESULT OF THIS ACT IS KEYED, INCLUDING ANY IT CLOSES**, and calls it
### *"the freshness shortfall's remedy applied to this act's own output"*. ### That is
### `W-ORD-DEBT-FRESHNESS` (b302) turned on the act that inherited it: ### **b268's RESULT WAS
### NEVER KEYED AND THE MISS COST b300 AND b301 A FALSE OPEN EACH.** ### So this act keys its own
### three results at the time it produces them rather than leaving a later act to find them.

### ### **THE THREE:**
###   ### `uniform-family` ....... the definition across places. ### **THE ORDER NAMES IT.**
###   ### `vn-definition-331` .... the source read that discharged b302's own stated exposure.
###   ### `object-conditions` .... the object's standing conditions, ### **WITH THE COUNT
###       CORRECTED** -- and this is the row that exists so the correction is FINDABLE, since a
###       correction filed only in a bank is exactly the shape that went missing before.

### ### **b164's LIMIT IS NOT RETIRED BY ANY OF THEM: ### KEYS CLOSE FALSE HITS, THEY DO NOT CLOSE
### ### FALSE MISSES.**
### ### **AND THE MUST-NOT-HIT ARM IS b202's: ### `uniform` AND `convergence` STAY UNKEYED BECAUSE
### ### THEY ARE PROPERTIES AND NOT OBJECTS.** ### Both returned `NO KEY` before this act and must
### still return it after, or the aliases have become a net.
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
    "    'uniform-family': ['the uniform family', 'the two-radius family',\n"
    "                      'the family across places', 'the uniform form',\n"
    "                      'the archimedean family', 'a pair of radii at every place'],\n"
    "    'vn-definition-331': ['definition 3.3.1', 'the c0-sequence definition',\n"
    "                         'the convergent unit sequence', 'von neumann definition 3.3.1'],\n"
    "    'object-conditions': ['the object conditions', 'object conditions',\n"
    "                         \"the object's standing conditions\",\n"
    "                         'the construction status'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE TWO-RADIUS FAMILY ACROSS PLACES (b303).\n"
    "    (\"uniform-family\", \"b303 (a definition, written across places)\",\n"
    "     \"a member is a choice, AT EVERY PLACE v, of a pair of radii (lambda_v, mu_v) -- one\"\n"
    "     \" bounding where the function vanishes, one where its transform does -- with\"\n"
    "     \" Son_v(lambda_v, mu_v) the functions in that place's own local space vanishing on\"\n"
    "     \" abs_v(x) <= lambda_v whose transform vanishes on abs_v(y) <= mu_v, the local space,\"\n"
    "     \" the absolute value and the transform each being THAT PLACE'S OWN. ### It restricts to\"\n"
    "     \" b293's Son(p,n;a,b) at finite p and to CC Definition 4.4's S(lambda,mu) at infinity.\"\n"
    "     \" ### **THE CORPUS'S OBJECT IS THE EVERYWHERE-(1,1) MEMBER**, which at every place is\"\n"
    "     \" the transform-fixed point of its own dilation orbit -- verified at content vector by\"\n"
    "     \" vector at five finite cells, and READ off CC's own identifying sentence at infinity.\"\n"
    "     \" ### The bridge is b21's chart x = p^(-n) m, THE CORPUS'S OWN, quoted by b293 inside\"\n"
    "     \" its own definition of B_e; under it the finite SUM invariant a+b is the archimedean\"\n"
    "     \" PRODUCT invariant lambda*mu, and the finite dilation is D_a at a = 1/p\",\n"
    "     \"### A DEFINITION, AND ITS GRADE IS A DIVISION: ### **UNIFORM AS A FORM, NOT AS AN\"\n"
    "     \" OBJECT.** ### One sentence covers all places because every term delegates to the\"\n"
    "     \" place; the instances are structurally different BY A THEOREM -- the sub-level set is a\"\n"
    "     \" compact open subgroup at p and provably not one at infinity (b198). ### **A LATER ACT\"\n"
    "     \" MAY QUOTE THE FORM AND MAY NOT QUANTIFY OVER THE OBJECTS AS THOUGH THEY WERE ONE KIND\"\n"
    "     \" OF THING.** ### W-ORD-UNIFORM-FORM's promotion criterion is met AS TO CONTENT and the\"\n"
    "     \" proposal stays UNBANKED-UNTIL-TESTED; PROMOTION IS THE AUTHOR'S. ### The annihilation\"\n"
    "     \" criterion remains a statement about members at the FINITE places. ### NO AGGREGATION\"\n"
    "     \" IS STATED. ### M-2 UNCHANGED (SPECIFIED-NOT-STATED)\",\n"
    "     \"data/b303_the_uniform_family.txt; data/b303_family_run.txt;\"\n"
    "     \" CORRESPONDENCE.md row 118\"),\n"
    "    # ### von NEUMANN'S DEFINITION 3.3.1, READ AT SOURCE (b303).\n"
    "    (\"vn-definition-331\", \"b303 (a read at content, in the source itself)\",\n"
    "     \"quoted whole from the page image: 'A sequence f_alpha, alpha in I, is a C0-sequence, if\"\n"
    "     \" and only if f_alpha in H_alpha for all alpha in I, and SUM_(alpha in I) of\"\n"
    "     \" abs(norm(f_alpha) - 1) converges.' ### **IT ASKS FOR MEMBERSHIP IN THE LOCAL HILBERT\"\n"
    "     \" SPACE AND A CONVERGENT NORM SUM AND FOR NOTHING MORE**, and it makes NO PARTITION OF\"\n"
    "     \" I -- no clause distinguishes an archimedean index from a finite one. ### The corpus's\"\n"
    "     \" own OCR extract stops dead at 'if and' and the next line is the page number, which is\"\n"
    "     \" why the clause had been held THROUGH A READER (b197) since b196\",\n"
    "     \"### AT CONTENT, b303's OWN READ, BY A ROUTE INDEPENDENT OF b197's -- and the two agree\"\n"
    "     \" WORD FOR WORD. ### **VERDICT: CONFIRMS.** ### b302's execution of RULE ARCH-UNIT\"\n"
    "     \" stands on the source's own words, and the conditional b302 wrote against itself is\"\n"
    "     \" DISCHARGED. ### **A CONFIRMATION REMOVES AN EXPOSURE; IT DOES NOT ADD A RESULT** --\"\n"
    "     \" Q4 stays WITHDRAWN, the sector clause stays DESCRIPTION, b214's c = +1 stays at BENCH.\"\n"
    "     \" ### SCOPE: ONE DEFINITION. Lemma 4.1.2, Def 4.1.1 and Def 3.3.2 were NOT re-read and\"\n"
    "     \" stand at b226's at-source grade. ### M-2 UNCHANGED\",\n"
    "     \"data/b303_the_uniform_family.txt; data/b303_source_read.txt;\"\n"
    "     \" CORRESPONDENCE.md row 119; artefact sha256\"\n"
    "     \" 571060b596af58af35f09f077984a2b747e7acbc52ab6d107ba8b45c761ad0a3, page index 21\"),\n"
    "    # ### THE OBJECT'S STANDING CONDITIONS, WITH THE COUNT CORRECTED (b303).\n"
    "    (\"object-conditions\", \"b301 and b302, count corrected at b303\",\n"
    "     \"the object (x)'_v (S-bar_v, u_v) is CONSTRUCTED CONDITIONALLY on FOUR standing\"\n"
    "     \" conditions, each typed: a PREMISE (the level limit, b198 I2); a RESULT\"\n"
    "     \" (W-ORD-PHI-MU-L2, phi_mu in L^2(R), stated by no owner); a RULING\"\n"
    "     \" (W-ORD-ARCH-NORM-READING, which inner product b226's archimedean normalization is);\"\n"
    "     \" and a CONSTRUCTION (C9 / N-OPEN-B, the real fiber's placement). ### **b302's SENTENCE\"\n"
    "     \" SAYS THREE AND b302's OWN LIST CARRIES FOUR; THE LIST IS RIGHT.** ### The root is\"\n"
    "     \" b301's headline, which counted ONE of its own THREE typed results\",\n"
    "     \"### AT b301's AND b302's OWN BANKED GRADES. ### **NO VERDICT MOVES AND NO CONDITION WAS\"\n"
    "     \" ADDED OR REMOVED -- ONLY THE COUNT IS CORRECTED**, and it is filed rather than edited\"\n"
    "     \" into either act (the append-only law). ### **WHAT SETTLES IT IS b303's SOURCE READ:**\"\n"
    "     \" Definition 3.3.1's FIRST conjunct is f_alpha in H_alpha, so W-ORD-PHI-MU-L2 is the\"\n"
    "     \" MEMBERSHIP HALF OF DEFINITION 3.3.1 AT INFINITY -- one of the two things the source\"\n"
    "     \" asks for, undischarged at one place -- and therefore a condition of the object and not\"\n"
    "     \" a debt of a lane. ### Q4 is NOT among the four: it was WITHDRAWN as a requirement.\"\n"
    "     \" ### M-2 UNCHANGED\",\n"
    "     \"data/b303_the_uniform_family.txt; data/b302_the_unit_requirement.txt;\"\n"
    "     \" data/b301_the_object_completed.txt\"),\n"
)

NEW_KEYS = ('uniform-family', 'vn-definition-331', 'object-conditions')
# ### THE ALIASES THAT RETURNED `NO KEY` BEFORE THIS ACT AND MUST NOW REACH A ROW.
ALIASES = ('the two-radius family', 'the uniform form', 'the family across places',
           'definition 3.3.1', 'the construction status')
# ### b202's ARM: PROPERTIES, NOT OBJECTS. ### **BOTH WERE `NO KEY` BEFORE AND MUST STAY SO.**
MUST_NOT_HIT = ('uniform', 'convergence')


def no_key(out):
    """### TRUE IFF THE INDEX'S OWN VERDICT LINE SAYS `NO KEY`. ### **LINE-SCOPED** -- b302's D7,
    where a checker read a row's own prose as the index's verdict. ### The fix is the scope."""
    for ln in (out or '').splitlines():
        if ln.strip().startswith('### NO KEY'):
            return True
    return False


def verdict_fixture():
    """### **BOTH POLARITIES ON THE LINE-SCOPING ITSELF.**"""
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
    print('b303 -- THE INDEX KEYS. ### THREE RESULTS, KEYED BY THE ACT THAT PRODUCED THEM.')
    print('=' * 100)

    have_key = {k: ("'%s'" % k) in txt for k in NEW_KEYS}
    have_row = {k: ('"%s"' % k) in txt for k in NEW_KEYS}
    for k in NEW_KEYS:
        print('  %-20s key/row already present : %s / %s' % (k, have_key[k], have_row[k]))
    written = not (all(have_key.values()) and all(have_row.values()))
    if not written:
        print('  ### NOTHING WRITTEN. (idempotent) ### **THE READ-BACK ARMS STILL RUN** -- a tool')
        print('  ### that reports nothing on its second run leaves no evidence of its first.')
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file. Refusing to write into a')
        print('  ### shape this tool cannot see.')
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
        print('    %-22s returns a row : %s  %s' % (k, good, 'PASS' if good else '### FAIL ###'))

    print('  ### THE ALIASES, EACH OF WHICH RETURNED `NO KEY` BEFORE THIS ACT:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-26s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### MUST-NOT-HIT (b202), so the aliases are keys and not a net:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        ok = ok and quiet
        print('    %-26s still returns NO KEY : %s  %s'
              % (q, quiet, 'PASS' if quiet else '### FAIL -- a nearest string became a hit'))
    print('  ### **`uniform` AND `convergence` STAY UNKEYED BECAUSE THEY ARE PROPERTIES AND NOT')
    print('  ### OBJECTS** -- b202\'s own reason, and it has not changed.')
    print('  ### **AND b164\'s LIMIT IS NOT RETIRED: KEYS CLOSE FALSE HITS, NOT FALSE MISSES.**')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
