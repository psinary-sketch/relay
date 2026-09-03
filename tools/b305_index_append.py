# -*- coding: utf-8 -*-
"""b305_index_append.py -- THREE KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES `arithmetics-entry` AND SAYS EVERY RESULT IS KEYED.** ### The freshness
### remedy is applied as b303 and b304 applied it: this act keys its results at the time it
### produces them, so a later act asking where the source's arithmetic enters finds the answer
### rather than the question.

### ### **THE THREE:**
###   ### `arithmetics-entry` .. where the source's arithmetic enters, and which of the three
###       candidates carries the primes.
###   ### `prime-sum-is-weil` ... the species comparison, and the term-for-term identification.
###   ### `instrument-q-p` ...... the priced instrument, its price, what it must reproduce, and the
###       artifact it retires.

### ### **THE MUST-NOT-HIT ARM IS b202's, MEASURED BOTH BEFORE AND AFTER THE WRITE** (b304's
### addition): ### **`arithmetic` AND `positivity` STAY UNKEYED BECAUSE THEY ARE PROPERTIES AND NOT
### OBJECTS.**
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
    "    'arithmetics-entry': ['where the arithmetic enters', 'the arithmetic entry',\n"
    "                         'the weil distribution', 'the local weil distribution',\n"
    "                         'the explicit formula'],\n"
    "    'prime-sum-is-weil': ['the prime sum', 'the adopted prime sum',\n"
    "                         'the corpus prime side', 'PR summand'],\n"
    "    'instrument-q-p': ['the instrument', 'the priced instrument',\n"
    "                      'the q_p instrument', 'the scaling instrument'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### WHERE THE SOURCE'S ARITHMETIC ENTERS (b305).\n"
    "    (\"arithmetics-entry\", \"b305 (a read at content, in the source)\",\n"
    "     \"in CC (arXiv:2006.13771v1) the primes are carried by the LOCAL WEIL DISTRIBUTION\"\n"
    "     \" W_p(f) = (log p) SUM_{m>=1} ( f(p^m) + f#(p^m) ), eq. (149) of Appendix B.\"\n"
    "     \" ### **SO THE ARITHMETIC ENTERS THROUGH NEITHER THE TEST FUNCTION NOR THE OPERATOR BUT\"\n"
    "     \" THROUGH THE DISTRIBUTION THEY ARE PAIRED AGAINST.** ### The operator theta(g) S\"\n"
    "     \" theta(g)* contains no prime -- theta is the scaling action, S the Sonin projection, g\"\n"
    "     \" a bump -- and its positivity is the A*A shape with A = S theta(g)*. ### The test\"\n"
    "     \" function contributes a SUPPORT, which gates WHICH primes appear: the source takes\"\n"
    "     \" supp in (1/2,2)'so that rational primes are not involved (see (149))'\",\n"
    "     \"### AT CONTENT, b305's OWN READ; artefact sha256 b8e0b54a..., text layer measured\"\n"
    "     \" INTACT (0 truncated pages), 11 of 11 quoted fragments located by page index.\"\n"
    "     \" ### **THIS IS A READ OF A SOURCE AND IS NOT A RESULT OF THE CORPUS.** ### It REFUTES\"\n"
    "     \" the registered falsifier (F1) in its first half -- the arithmetic does NOT enter\"\n"
    "     \" through the test function -- and confirms its second. ### It settles\"\n"
    "     \" W-ORD-FORCED-POSITIVITY: the source never asks its positivity to carry arithmetic;\"\n"
    "     \" Theorem 1 is an INEQUALITY between an arithmetic distribution and a forced-positive\"\n"
    "     \" trace, and the content is in the difference. ### M-2 UNCHANGED\",\n"
    "     \"data/b305_the_arithmetics_entry.txt; data/b305_source_read.txt;\"\n"
    "     \" CORRESPONDENCE.md row 122\"),\n"
    "    # ### THE CORPUS'S PRIME SUM IS THE LOCAL WEIL DISTRIBUTION (b305).\n"
    "    (\"prime-sum-is-weil\", \"b305 (a comparison by definitions)\",\n"
    "     \"the corpus's adopted summand w_{p,k} = 2 log p * p^{-k/2} * corr(log p^k) (b260,\"\n"
    "     \" adopted b229) IS the k-th term of CC's local Weil distribution W_p under CC's OWN\"\n"
    "     \" normalization W_v(f) := W_v(Delta^{-1/2} f): that term is (log p) p^{-k/2} ( f(p^k) +\"\n"
    "     \" f(p^{-k}) ), and **the corpus's factor 2 is CC's f + f# collapsed under evenness**.\"\n"
    "     \" ### Same log p, same p^{-k/2} from the same normalization, same finite index set.\"\n"
    "     \" ### **AND NOT THE SAME SPECIES AS THE QUOTIENT CHANNEL**: the orbit ratio\"\n"
    "     \" (p^n - p^k)/(p^n - 1) is dimensionless, carries neither factor, is silent at the top\"\n"
    "     \" level by its own range, and is a WEIGHT applied to a prime term\",\n"
    "     \"### DECIDED BY DEFINITIONS, FACTOR BY FACTOR. ### **(F2) HOLDS, MORE STRONGLY THAN IT\"\n"
    "     \" WAS REGISTERED -- the same OBJECT, not merely the same species.** ### **SCOPE: HAVING\"\n"
    "     \" THE OBJECT IS NOT DOING WITH IT WHAT THE SOURCE DOES.** ### The source pairs W_v\"\n"
    "     \" against a compressed trace and proves an inequality; the corpus pairs PR against an\"\n"
    "     \" orbit-count channel and measures a separation. ### The quotient channel is NOT demoted\"\n"
    "     \" by being a different species -- a weight is not a lesser object than a distribution.\"\n"
    "     \" ### The match rests on an evenness the corpus records by its factor 2 rather than by a\"\n"
    "     \" sentence, and that reading is NAMED. ### NO AGGREGATION IS STATED. ### M-2 UNCHANGED\",\n"
    "     \"data/b305_the_arithmetics_entry.txt; data/b260_junction_sign.txt (the PR summand);\"\n"
    "     \" data/b220_aggregation_freedom.txt (act 9's range); CORRESPONDENCE.md row 123\"),\n"
    "    # ### THE INSTRUMENT ON Q_p, PRICED AND NOT BUILT (b305).\n"
    "    (\"instrument-q-p\", \"b305 (a pricing, not a build)\",\n"
    "     \"an instrument carrying the SCALING part p^Z of Q_p^x, which the truncated model drops.\"\n"
    "     \" ### It would compute on locally constant functions of compact support on Q_p -- and\"\n"
    "     \" **the corpus's own chart and Haar normalization ALREADY DEFINE THEM**: b280's V_n is\"\n"
    "     \" supported in p^{-n}Z_p and constant on cosets of p^n Z_p, a chart point being 'a COSET\"\n"
    "     \" OF MEASURE p^{-n} > 0' on which f is constant. ### **THE ONE STRUCTURAL CHANGE IS TO\"\n"
    "     \" UNTIE TWO RADII THE MODEL TIES TOGETHER** -- support radius and constancy radius, both\"\n"
    "     \" n in V_n -- and the corpus already has b303's two-radius family for the untied pair\"\n"
    "     \" and b293's dilation for how scaling moves it. ### Exact arithmetic: mostly Q, since\"\n"
    "     \" b293's collapse makes the conditions rational; cyclotomic only for transform values\",\n"
    "     \"### A PRICE, AND THIS SEAT'S ESTIMATE: **THREE ACTS FOR THE CORE, FIVE FOR THE\"\n"
    "     \" COMPARISON**. ### **IT IS NOT A COMMITMENT, NOT A MEASUREMENT, AND NOT A\"\n"
    "     \" RECOMMENDATION TO BUILD.** ### It must reproduce: (1) b293's two conditions, dimension\"\n"
    "     \" law and diagonal identification; (2) b304's compact-part zero WITH its mechanism, not\"\n"
    "     \" only its value; (3) b297's annihilation criterion and b280's P(k=n)=0 at reachable\"\n"
    "     \" cells; and (4) b304's Tr(Pi) = dim Son, so it is shown alive. ### **IT RETIRES THE\"\n"
    "     \" ESCAPED-MASS ARTIFACT** (b21, met b284): on Q_p there is no modulus and nothing to\"\n"
    "     \" fold. ### It does NOT retire W-ORD-FIBER-GENERAL, the barrier's scope limit, or the\"\n"
    "     \" range law. ### M-2 UNCHANGED\",\n"
    "     \"data/b305_the_arithmetics_entry.txt; data/b280_the_consequence.txt (the chart and\"\n"
    "     \" Haar sentences); data/b284_the_scalings_domain.txt (nothing to fold on Q_p)\"),\n"
)

NEW_KEYS = ('arithmetics-entry', 'prime-sum-is-weil', 'instrument-q-p')
ALIASES = ('where the arithmetic enters', 'the weil distribution', 'the prime sum',
           'the explicit formula', 'the instrument')
MUST_NOT_HIT = ('arithmetic', 'positivity')


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
    print('b305 -- THE INDEX KEYS. ### THREE RESULTS, KEYED BY THE ACT THAT PRODUCED THEM.')
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
        print('  %-22s key/row already present : %s / %s' % (k, have_key[k], have_row[k]))
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
        print('    %-22s returns a row : %s  %s' % (k, good, 'PASS' if good else '### FAIL ###'))

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
    print('  ### **`arithmetic` AND `positivity` STAY UNKEYED BECAUSE THEY ARE PROPERTIES AND NOT')
    print('  ### OBJECTS** -- b202\'s own reason. ### **AND b164\'s LIMIT IS NOT RETIRED.**')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
