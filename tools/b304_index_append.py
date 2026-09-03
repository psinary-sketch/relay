# -*- coding: utf-8 -*-
"""b304_index_append.py -- THREE KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER SAYS EVERY RESULT IS KEYED, AND `demands-shape` BY NAME.** ### The freshness
### remedy (b302's `W-ORD-DEBT-FRESHNESS`, applied by b303 to its own output) is applied here too:
### this act keys its results at the time it produces them, so a later act asking whether
### `W-ORD-PHI-MU-L2` is still owed finds the discharge rather than the filing.

### ### **THE THREE:**
###   ### `demands-shape` ...... whether the per-index first-level demand is downstream of the
###       termwise requirement, and what the index set's shape does about it.
###   ### `phi-mu-l2` .......... the archimedean unit's square-integrability. ### **THIS ROW EXISTS
###       BECAUSE ITS ABSENCE IS EXACTLY THE SHAPE THAT COST b300 AND b301 A FALSE OPEN EACH.**
###   ### `smearing-compression` the finite analogue of the source's move, its reach verdict, and
###       what was refused rather than computed.

### ### **THE MUST-NOT-HIT ARM IS b202's: ### `positivity` AND `the trace` STAY UNKEYED BECAUSE
### ### THEY ARE PROPERTIES AND NOT OBJECTS.** ### Both must be checked as `NO KEY` BEFORE the
### write and again after, or the aliases have become a net.
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
    "    'demands-shape': ['the demand shape', \"the demand's shape\",\n"
    "                     'the per-index demand', 'per-index demand',\n"
    "                     'termwise agreement', 'the first-level demand'],\n"
    "    'phi-mu-l2': ['phi mu in l2', 'the archimedean unit membership',\n"
    "                 'square-integrability of the archimedean unit',\n"
    "                 'the fourth condition'],\n"
    "    'smearing-compression': ['the smearing compression', 'smearing over the group',\n"
    "                            'the finite scaling trace', 'the sonin trace',\n"
    "                            'the finite analogue of the source move'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE DEMAND'S SHAPE (b304).\n"
    "    (\"demands-shape\", \"b304 (a derivation from the specification's own text)\",\n"
    "     \"is the per-index first-level demand (SPEC-1) downstream of requiring TERMWISE\"\n"
    "     \" agreement with the quotient channel below the top (SPEC-2)? ### **NO.** ### Two\"\n"
    "     \" reasons, both in b263's text: (i) SPEC-1's stated ground is S1 + S2 and NAMES SPEC-2\"\n"
    "     \" NOWHERE; (ii) at the primes SPEC-1 is about, SPEC-2's range 1 <= k <= n-1 reads\"\n"
    "     \" 1 <= k <= 0 and is EMPTY, so there is nothing there for a loosening to loosen.\"\n"
    "     \" ### Loosening termwise to aggregate DISSOLVES the demand at primes with n_p >= 2 and\"\n"
    "     \" DISSOLVES NOTHING at n_p = 1 -- which by S2 carry 73.96% rising to 99.95% of the\"\n"
    "     \" separation. ### **THE DEMAND IS DOWNSTREAM OF THE INDEX SET BEING A SINGLE POINT,\"\n"
    "     \" NOT OF A CHOICE ABOUT AGREEMENT**, and b262 states that shape outright: the n_p = 1\"\n"
    "     \" family are the primes 'whose only level IS the top level'\",\n"
    "     \"### DERIVED FROM THE OWNERS' TEXT, NOT ARGUED. ### **NO SPECIFICATION IS LOOSENED BY\"\n"
    "     \" THIS ACT -- ONLY THE AUTHOR MAY DO THAT** -- and the two options are assembled as a\"\n"
    "     \" DECISION CARD with NO recommendation. ### The barrier still reaches the n_p = 1\"\n"
    "     \" places under either option, because the demand there is still a value at the top.\"\n"
    "     \" ### NO AGGREGATION IS STATED. ### M-2 UNCHANGED (SPECIFIED-NOT-STATED)\",\n"
    "     \"data/b304_the_demands_shape.txt; data/b263_top_level_silence.txt (SPEC-1..3, S1, S2);\"\n"
    "     \" data/b262_junction_limit.txt (the T_top partition)\"),\n"
    "    # ### THE ARCHIMEDEAN UNIT'S SQUARE-INTEGRABILITY (b304).\n"
    "    (\"phi-mu-l2\", \"b304 (a read at content, in both sources)\",\n"
    "     \"the corpus's u_inf is phi_mu at the first even negative eigenvalue, normalized, and\"\n"
    "     \" **IT LIES IN L^2(R)**, by two independent routes. ### ROUTE A: phi_mu is an\"\n"
    "     \" eigenvector of Wsa; CM defines Wsa as the restriction of Wmax to a subspace with an\"\n"
    "     \" explicit Dom Wsa, the ambient space being L^2(R) in CM's own words; and an\"\n"
    "     \" eigenvector lies in its operator's domain BY THE DEFINITION OF EIGENVECTOR --\"\n"
    "     \" **SO MEMBERSHIP IS DEFINITIONAL AND NOT A DECAY STATEMENT**. ### ROUTE B: CM\"\n"
    "     \" Corollary 3.2 puts phi_mu in the Sonin space, and CC defines that space as a subspace\"\n"
    "     \" of the Hilbert space L^2(R)_ev. ### The hypothesis was CHECKED and not carried on the\"\n"
    "     \" corollary's name: Corollary 3.2 needs mu negative, and b214's printed mu is\"\n"
    "     \" -20.48057322913694697\",\n"
    "     \"### AT CONTENT, b304's OWN READ OF BOTH SOURCES (arXiv:2112.05500v1 sha256 426114ae...;\"\n"
    "     \" arXiv:2006.13771 sha256 b8e0b54a...). ### **W-ORD-PHI-MU-L2 IS DISCHARGED** -- filed\"\n"
    "     \" at b300 as 'stated by no owner', and an owner does state it, twice; what was missing\"\n"
    "     \" was the READ and not the mathematics. ### **SCOPE: THE OBJECT STILL STANDS ON THREE\"\n"
    "     \" CONDITIONS** -- the level-limit premise, W-ORD-ARCH-NORM-READING, and C9/N-OPEN-B --\"\n"
    "     \" and A CONDITION DISCHARGED IS NOT THE OBJECT CONSTRUCTED. ### It does NOT put u_inf\"\n"
    "     \" in the sector (b201's BRANCH (NO EXHIBIT) stands) and does NOT decide which inner\"\n"
    "     \" product the normalization is. ### M-2 UNCHANGED\",\n"
    "     \"data/b304_the_demands_shape.txt; CORRESPONDENCE.md row 120;\"\n"
    "     \" data/b300_the_archimedean_leg.txt (where it was filed)\"),\n"
    "    # ### THE FINITE ANALOGUE OF THE SOURCE'S MOVE, COMPRESSED (b304).\n"
    "    (\"smearing-compression\", \"b304 (a decision by definitions, then a computation)\",\n"
    "     \"the finite analogue of CC's Tr(theta(f) S) is T(f) = Tr(theta(f) Pi) on Z/N,\"\n"
    "     \" N = p^{2n}, with Pi the projection onto Son(p,n). ### **THE BARRIER DOES NOT REACH\"\n"
    "     \" IT**: the barrier's operator is a functional of the unit's restriction TO the ball,\"\n"
    "     \" where every element of S-bar_p vanishes, while the smeared operator's matrix elements\"\n"
    "     \" are supported OFF the ball, where S-bar_p lives. ### The compression was therefore\"\n"
    "     \" computed, exact rationals, no float: at (2,1) (2,2) (3,1) (3,2) (5,1) (7,1) the\"\n"
    "     \" smeared value against the constant test function on the units is **EXACTLY ZERO AT\"\n"
    "     \" ALL SIX, including every one-level place** -- and the zero is DERIVED, not only\"\n"
    "     \" measured: SUM_t theta(t) is |U| times the projection onto the unit-invariants, which\"\n"
    "     \" are spanned by valuation shells, and every Son vector is orthogonal to every shell\",\n"
    "     \"### A COMPUTATION ON THE PART OF THE GROUP THE MODEL CAN CARRY. ### **Q_p^x = p^Z x\"\n"
    "     \" Z_p^x, AND ONLY THE Z_p^x PART WAS COMPUTED** -- it acts by permutations, verified at\"\n"
    "     \" every t used. ### **THE p^Z PART WAS REFUSED**: it is b21's escaped-mass artifact, met\"\n"
    "     \" at b284, and the model would return the genuine object with its escaped mass folded\"\n"
    "     \" back onto the ball. ### **AND THE REFUSED PART IS THE PART WITH AN ARCHIMEDEAN\"\n"
    "     \" COUNTERPART**, so this zero is NOT 'the finite analogue's value'. ### **IT IS NOT A\"\n"
    "     \" BARRIER AND NOT A ROUTE** -- for a general test function the value is SUM_t f(t)\"\n"
    "     \" Tr(theta(t) Pi) and those traces are not all zero. ### The barrier is not weakened:\"\n"
    "     \" an operator it does not reach is not a counterexample to it. ### M-2 UNCHANGED\",\n"
    "     \"data/b304_the_demands_shape.txt; data/b304_smearing_run.txt;\"\n"
    "     \" CORRESPONDENCE.md row 121\"),\n"
)

NEW_KEYS = ('demands-shape', 'phi-mu-l2', 'smearing-compression')
ALIASES = ("the demand's shape", 'per-index demand', 'the fourth condition',
           'smearing over the group', 'the sonin trace')
MUST_NOT_HIT = ('positivity', 'the trace')


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
    print('b304 -- THE INDEX KEYS. ### THREE RESULTS, KEYED BY THE ACT THAT PRODUCED THEM.')
    print('=' * 100)

    # ### THE MUST-NOT-HIT ARM, RUN ### BEFORE ### THE WRITE TOO, so "still NO KEY" means
    # ### something. ### **A CONTROL THAT WAS NEVER CLEAN BEFOREHAND PROVES NOTHING AFTERWARDS.**
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
        print('    %-24s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`positivity` AND `the trace` STAY UNKEYED BECAUSE THEY ARE PROPERTIES AND NOT')
    print('  ### OBJECTS** -- b202\'s own reason. ### **AND b164\'s LIMIT IS NOT RETIRED.**')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
