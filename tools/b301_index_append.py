# -*- coding: utf-8 -*-
"""b301_index_append.py -- FILE THE INDEX KEY. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **`object-completed` WAS QUERIED BEFORE ANY STEP AND RETURNED `NO KEY`.** ### This is the
### other half of the b160 convention: the object is keyed so the next act's query is not another
### `NO KEY`.

### ### **b164's LIMIT TRAVELS WITH THE KEY AND IS NOT RETIRED BY IT: ### KEYS CLOSE FALSE HITS,
### ### THEY DO NOT CLOSE FALSE MISSES.**
### ### **AND b202's ALIAS RULE IS OBEYED: ### THE BARE WORDS "the object" AND "the product" ARE
### ### NOT ADDED.** ### "the object" is what the whole programme calls its subject and would
### collide with half the record; ### **"the product" IS AMBIGUOUS ACROSS THE TWO CONSTRUCTIONS
### THIS VERY ACT HAD TO SEPARATE** -- the restricted tensor product and von Neumann's incomplete
### direct product. ### **A NEAREST STRING IS HOW A MISS BECOMES A FALSE HIT.**
"""
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'tools', 'banked_index.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'object-completed': ['the object completed', 'the incomplete direct product',\n"
    "                        'the stated choice across places', 'the constituents table',\n"
    "                        'the c0 condition', 'term 3 object'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE OBJECT COMPLETED (b301).\n"
    "    (\"object-completed\", \"b301 (construction restatement and its checks)\",\n"
    "     \"the object (x)'_v (S-bar_v, u_v) restated with every constituent in one table:\"\n"
    "     \" AT FINITE p, S-bar_p is the L^2(Q_p)-closure of the Son tower (b279, CONSTRUCTED),\"\n"
    "     \" with u_p = 4q P_1 f_(1,1) at level ell(p) = 2 if p = 2 else 1 -- the exceptional\"\n"
    "     \" place being the law's own zero d_1(2,1) = 0; AT INFINITY, S(1,1) from CC Definition\"\n"
    "     \" 4.4 with the inner product of CC eq (16), and u_inf = phi_mu at the first even\"\n"
    "     \" NEGATIVE eigenvalue, IN that space (b300). ### **OF THE PRODUCT'S EIGHT REQUIREMENTS:\"\n"
    "     \" 4 MET (a Hilbert space at every index; a norm-one vector EXISTS at every index; the\"\n"
    "     \" C0 condition; the level-limit premise), 3 OPEN (the STATED finite unit's nonvanishing\"\n"
    "     \" at the generic odd place; the archimedean unit's SECTOR membership; choice-dependence)\"\n"
    "     \" and 1 NOT ASKED -- purity, which belongs to the RESTRICTED TENSOR PRODUCT and not to\"\n"
    "     \" von Neumann's incomplete direct product the author's b225 ruling re-scoped term 3 to.**\"\n"
    "     \" ### The C0 condition was RE-CHECKED in exact rationals under CC eq (16): it holds\"\n"
    "     \" under every reading of the archimedean normalization, and **the corpus's own\"\n"
    "     \" half-line picture is the reading that agrees with the source exactly**, keeping\"\n"
    "     \" b226's sum at EXACTLY 0; under the plain-INT_R reading the deviation is 1 - 1/sqrt(2)\"\n"
    "     \" and Lemma 4.1.2's hypothesis wants a renormalization this act NAMES and does not make\",\n"
    "     \"### CONSTRUCTED CONDITIONALLY -- on the level-limit premise (b226, at b198 I2's grade),\"\n"
    "     \" on ONE RESULT (b226's OWED generic odd place), on ONE RULING (which inner product the\"\n"
    "     \" archimedean normalization is -- W-ORD-ARCH-NORM-READING) and on ONE CONSTRUCTION (the\"\n"
    "     \" real fiber's placement, N-OPEN-B). ### **NO GRADE MOVES: every cell carries its owning\"\n"
    "     \" act's grade, pulled from that act's file.** ### **NOT A ROUTE. ### NO AGGREGATION IS\"\n"
    "     \" STATED. ### THE IDENTITY CHAIN'S TERM-3 ROW DOES NOT MOVE BY THIS ACT** -- it names\"\n"
    "     \" the restricted tensor product, three requirements are open, and a row is not moved by\"\n"
    "     \" an executor (W-ORD-TERM3-ROW). ### M-2 UNCHANGED (SPECIFIED-NOT-STATED)\",\n"
    "     \"data/b301_the_object_completed.txt; data/b301_object_gate.txt;\"\n"
    "     \" CORRESPONDENCE.md row 116\"),\n"
)


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b301 -- THE INDEX KEY. ### `object-completed` RETURNED NO KEY BEFORE ANY STEP.')
    print('=' * 100)

    have_key = "'object-completed'" in txt
    have_row = '"object-completed"' in txt
    print('  key already declared : %s   row already present : %s' % (have_key, have_row))
    if have_key and have_row:
        print('  ### NOTHING WRITTEN. (idempotent)')
        print('=' * 100)
        return 0
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file. Refusing to write into a')
        print('  ### shape this tool cannot see.')
        return 2

    new = txt
    if not have_key:
        new = new.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW, 1)
    if not have_row:
        new = new.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW, 1)
    open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(PATH + '.tmp', PATH)

    # ### READ BACK BY RUNNING THE INDEX, NOT BY GREPPING THE SOURCE.
    q = subprocess.run([sys.executable, PATH, '--query', 'object-completed'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = q.stdout or ''
    ok = ('NO KEY' not in out) and ('object-completed' in out) and q.returncode == 0
    print('  ### READ BACK BY QUERYING THE INDEX ITSELF:')
    for line in out.splitlines()[:8]:
        print('    %s' % line)
    print('  query returns a row : %s  %s' % (ok, 'PASS' if ok else '### FAIL ###'))

    # ### THE MUST-NOT-HIT ARM (b202's precedent): the ambiguous bare words stay unkeyed.
    quiet = True
    for probe in ('the product', 'the object'):
        q2 = subprocess.run([sys.executable, PATH, '--query', probe],
                            capture_output=True, text=True, encoding='utf-8', errors='replace')
        hit = 'NO KEY' not in (q2.stdout or '')
        quiet = quiet and not hit
        print('  MUST-NOT-HIT: %-14r still returns NO KEY : %s' % (probe, not hit))
    print('  ### **"the product" IS AMBIGUOUS ACROSS THE TWO CONSTRUCTIONS THIS ACT SEPARATED,')
    print('  ### AND THAT IS EXACTLY WHY IT IS NOT AN ALIAS.**')
    print('  ### b164\'s limit stands: keys close false hits, not false misses.')
    print('=' * 100)
    return 0 if (ok and quiet) else 1


if __name__ == '__main__':
    sys.exit(main())
