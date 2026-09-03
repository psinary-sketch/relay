# -*- coding: utf-8 -*-
"""b300_index_append.py -- FILE THE INDEX KEY. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **`archimedean-leg` WAS QUERIED BEFORE ANY STEP AND RETURNED `NO KEY`.** ### The b160
### convention and the b185 gate: an object marked open, navigator-asserted or requiring a
### construction is queried first and the query's result is recorded. ### **THIS IS THE OTHER
### HALF -- THE OBJECT IS KEYED SO THE NEXT ACT'S QUERY IS NOT ANOTHER `NO KEY`.**

### ### **b164's LIMIT TRAVELS WITH THE KEY AND IS NOT RETIRED BY IT: ### KEYS CLOSE FALSE HITS,
### ### THEY DO NOT CLOSE FALSE MISSES.** ### And b202's rule is obeyed at the alias list: ### the
### bare word "prolate" is ### **NOT** ### added, because it is ambiguous across two families this
### very act had to separate -- ### **A NEAREST STRING IS HOW A MISS BECOMES A FALSE HIT.**
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
    "    'archimedean-leg': ['the archimedean leg', 'the archimedean unit',\n"
    "                       'u_inf', 'the chosen archimedean unit',\n"
    "                       'the archimedean local space', 'the sonin sector'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE ARCHIMEDEAN LEG (b300).\n"
    "    (\"archimedean-leg\", \"b300 (construction from a graded import, and a derivation)\",\n"
    "     \"the object's archimedean local space is BUILT from the source's own Definition 4.4 as\"\n"
    "     \" S(1,1) = {xi in L^2(R)_ev : xi = 0 on |q|<=1, F_eR xi = 0 on |p|<=1}, with the inner\"\n"
    "     \" product and its normalization read at content at CC 2006.13771 eq (16) --\"\n"
    "     \" <eta|xi> := (1/2) INT_R eta conj(xi) dx = INT_0^inf eta conj(xi) dx -- and it is a\"\n"
    "     \" Hilbert space because CC's R is the ORTHOGONAL PROJECTION onto it, which is the only\"\n"
    "     \" thing von Neumann 4.1.1 asks of a local space. ### **AND THE CORPUS'S CHOSEN\"\n"
    "     \" ARCHIMEDEAN UNIT u_inf -- phi_mu at the first even NEGATIVE eigenvalue, normalized in\"\n"
    "     \" L^2 (b226, from b214's rank-2 measurement) -- IS IN THAT SPACE**, tested against BOTH\"\n"
    "     \" conditions: condition one is CM Lemma 3.1's 'zero on [-1,1]' quoted, and condition two\"\n"
    "     \" follows from b211's derived eigenrelation F phi_mu = c phi_mu with c = +-1, so\"\n"
    "     \" (F_eR phi_mu)(p) = c*0 = 0 there. ### **THE SIGN OF c IS NEVER USED, SO NO BENCH NUMBER\"\n"
    "     \" IS LOAD-BEARING.** ### Separately: the 'Sonin sector' (b206's +1 eigenspace of F on the\"\n"
    "     \" space) is a PROPER subspace of S(1,1), so sector and space are DIFFERENT objects; and\"\n"
    "     \" u_inf is NOT the instrument vector b291/b292 placed OUTSIDE the space -- two\"\n"
    "     \" derivations, one from scalar-invariance and one from CC's own orthogonality sentence\",\n"
    "     \"### DERIVES-on-IMPORTS, AND THE GRADE NAMES ITS INPUTS -- CM Lemma 3.1; b211's (C3)\"\n"
    "     \" chain on I8+I6+I10 at b211's own banked grade. ### **THE CONSTRUCTION IS CONDITIONAL**:\"\n"
    "     \" the real fiber's placement in the corpus's adelic object (N-OPEN-B as b287 read it) is\"\n"
    "     \" STILL OPEN, and phi_mu in L^2(R) is stated by NO OWNER (W-ORD-PHI-MU-L2) -- b226's own\"\n"
    "     \" choice presupposes it. ### **NOT A ROUTE. ### IT UNBLOCKS NOTHING: b221 records the\"\n"
    "     \" halt is at the FINITE places, and b226's G-SECTOR at the generic odd place is STILL\"\n"
    "     \" OWED.** ### Whether u_inf is in the SECTOR is NOT derived (that needs c = +1 at rank 2,\"\n"
    "     \" which stands at BENCH), and which space the factor is remains the b212 ruling's,\"\n"
    "     \" provenance the conversation layer. ### M-2 UNCHANGED (SPECIFIED-NOT-STATED)\",\n"
    "     \"data/b300_the_archimedean_leg.txt; data/b300_source_read.txt; data/b300_e0_gate.txt;\"\n"
    "     \" CORRESPONDENCE.md row 115\"),\n"
)


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b300 -- THE INDEX KEY. ### `archimedean-leg` RETURNED NO KEY BEFORE ANY STEP.')
    print('=' * 100)

    have_key = "'archimedean-leg'" in txt
    have_row = '"archimedean-leg"' in txt
    print('  key already declared : %s   row already present : %s' % (have_key, have_row))
    if have_key and have_row:
        print('  ### NOTHING WRITTEN. (idempotent)')
        print('=' * 100)
        return 0
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file. Refusing to write into')
        print('  ### a shape this tool cannot see.')
        return 2

    new = txt
    if not have_key:
        new = new.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW, 1)
    if not have_row:
        new = new.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW, 1)
    data = new.encode('utf-8')
    open(PATH + '.tmp', 'wb').write(data)
    os.replace(PATH + '.tmp', PATH)

    # ### READ BACK BY RUNNING THE INDEX, NOT BY GREPPING THE SOURCE. ### **A KEY THAT PARSES AND
    # ### A KEY THAT ANSWERS ARE DIFFERENT FACTS, AND ONLY THE SECOND IS THE ONE THAT MATTERS.**
    q = subprocess.run([sys.executable, PATH, '--query', 'archimedean-leg'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = q.stdout or ''
    ok = ('NO KEY' not in out) and ('archimedean-leg' in out) and q.returncode == 0
    print('  ### READ BACK BY QUERYING THE INDEX ITSELF:')
    for line in out.splitlines()[:12]:
        print('    %s' % line)
    print('  query returns a row : %s  %s' % (ok, 'PASS' if ok else '### FAIL ###'))

    # ### THE MUST-NOT-HIT ARM (b202's precedent): the bare word stays unkeyed on purpose.
    q2 = subprocess.run([sys.executable, PATH, '--query', 'prolate'],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    quiet = 'NO KEY' in (q2.stdout or '')
    print('  MUST-NOT-HIT: the bare word "prolate" still returns NO KEY : %s  %s'
          % (quiet, 'PASS' if quiet else '### FAIL -- a nearest string became a false hit'))
    print('  ### **THE HALF THAT CARRIES INFORMATION IS THE SECOND, BECAUSE I WROTE THE ALIASES')
    print('  ### THE FIRST HALF MATCHES.** ### b164\'s limit is not retired: keys close false')
    print('  ### hits, they do not close false misses.')
    print('=' * 100)
    return 0 if (ok and quiet) else 1


if __name__ == '__main__':
    sys.exit(main())
