# -*- coding: utf-8 -*-
"""b333_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTCONFERRED`.** ### A reader who asks *is the archimedean
### term derived* must be handed the derivation tool's verdict AS PRINTED, its diagnosis, the grade's owner
### (the derivation's own, on named imports) and the sentence that routes agreeing certify the routes and not
### the size -- never a sentence that reads as the sealed bar met, a measurement grade conferred or the
### clause moved. ### The verdict, the diagnostic's worst values, the ranking and the row number are read from
### the run files at write time.
### ### **`the size certified` AND `the clause moved` STAY UNKEYED.** ### The index is swept for stems after
### the write.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
PATH = os.path.join(ROOT, 'tools', 'banked_index.py')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def load(n):
    return json.load(io.open(os.path.join(D, n), encoding='utf-8'))


R = load('b333_derive.json')
G = load('b333_diagnose.json')
K = load('b333_rerank.json')
CORR = io.open(os.path.join(D, 'b333_corr_run.txt'), encoding='utf-8').read()
ROWNUM = re.search(r'last row number is (\d+)', CORR).group(1)
RK = ', '.join('%s (%s)' % (k, g) for _o, k, _n, g, _re in K['ranking'])
SOFT = ' and '.join(K['softest'])

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'archimedean-term-derived': ['the archimedean term derived', 'archimedean term derived', 'the archimedean term',\n"
    "                                 'the digamma kernel', 'the classical term', 'the principal value', 'the third route',\n"
    "                                 'the re-rank', 'the factor of two', 'the Gamma factor', 'is the archimedean term derived',\n"
    "                                 'the new softest constituent', 'the mismatch diagnosed'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE ARCHIMEDEAN TERM DERIVED (b333).\n"
    "    (\"archimedean-term-derived\", \"b333 (a derivation under the import bar; a third route; the re-rank; a sealed bar not met, diagnosed)\",\n"
    "     \"THE DERIVATION TOOL'S VERDICT, AS PRINTED, FIRST: " + R['verdict'].replace('"', '') + ". ### Diagnosed: the act's sealed bar paired the third\"\n"
    "     \" route, run on the atlas's bump, with b320's table, which b320 computed for its own function autocorrelation(mean_zero_variant(a));\"\n"
    "     \" THE RECORD'S ARCHIMEDEAN NUMBERS ARE NOT TOUCHED -- the third route ((150) on the real side, mpmath, no corpus code) agrees with the\"\n"
    "     \" atlas's own banked channel for the bump at all thirteen cells (worst " + ('%.3e' % G['A_worst']['atlas']) + ") and with b320's two routes applied to the\"\n"
    "     \" bump (worst " + ('%.3e' % G['A_worst']['dig']) + " / " + ('%.3e' % G['A_worst']['w38']) + "); (150) on b320's own function agrees with b320's table (worst " + ('%.3e' % G['B_worst']['dig']) + " / " + ('%.3e' % G['B_worst']['w38']) + ").\"\n"
    "     \" The sealed bar, as sealed, NOT MET and not rewritten. ### THE CHAIN, its own verdict DERIVES-ON-IMPORT: the stated clause's constituent K5,\"\n"
    "     \" the archimedean distribution, derived from the classical term as the pinned source states it (Appendix B: (150) the principal value,\"\n"
    "     \" (151) the Gamma factor with its power of pi and its logarithmic derivative against the transform, (152)-(153) the digamma kernel,\"\n"
    "     \" W_inf = -W_R) under the corpus's conventions to the atlas's A = (1/2pi) INT hhat [Re psi(1/4 + iu/2) - log pi] du: THE CORPUS'S A IS\"\n"
    "     \" THE SOURCE'S W_inf = -W_R, entering (148) as pole + W_inf - PRIME; the factor-of-two hazard of b325 checked from one identity.\"\n"
    "     \" ### The re-rank under b332's sealed rule: " + RK + " -- the new softest: " + SOFT + "\",\n"
    "     \"### NO GRADE CONFERRED BEYOND THE DERIVATION'S OWN: DERIVES-ON-IMPORTS, the imports named; MEASURED-ON-FAMILIES NOT CONFERRED (the sealed\"\n"
    "     \" bar not met). ### ROUTES AGREEING CERTIFY THAT THE ROUTES AGREE, NOT THE SIZE OF THE TERM. ### THE CLAUSE HAS NOT MOVED; K8 STAYS\"\n"
    "     \" UNOWNED. ### The aim-map named as next, its target the new softest; neither it nor this act is the discharge. ### NO TERMINAL. ### M-2 UNCHANGED\",\n"
    "     \"data/b333_the_archimedean_term_derived.txt; data/b333_derive_run.txt; data/b333_diagnose_run.txt; data/b333_rerank_run.txt; data/b333_source.txt;\"\n"
    "     \" data/b333_registration_2026-09-06.txt (sealed before any value); FINDINGS.md (the b333 addendum after\"\n"
    "     \" clause-stated); FACES_LEDGER.md (the b333 update, row S1 / K5); CORRESPONDENCE.md row " + ROWNUM + "\"),\n"
)

ALIASES = ('the archimedean term derived', 'the archimedean term', 'the digamma kernel', 'the classical term',
           'the third route', 'the re-rank', 'is the archimedean term derived', 'the new softest constituent', 'the mismatch diagnosed')
MUST_NOT_HIT = ('the size certified', 'the clause moved', 'the sealed bar met')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b333 -- THE INDEX KEY. ### THE ARCHIMEDEAN TERM DERIVED.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'archimedean-term-derived'" in txt)
    have_row = ('"archimedean-term-derived"' in txt)
    print('  archimedean-term-derived    key/row already present : %s / %s' % (have_key, have_row))
    written = not (have_key and have_row)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file.')
        return 2
    if written:
        new = txt
        if not have_key:
            new = new.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW, 1)
        if not have_row:
            new = new.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW, 1)
        open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(PATH + '.tmp', PATH)
    else:
        print('  ### NOTHING WRITTEN. (idempotent) ### **THE READ-BACK ARMS STILL RUN.**')
    ok = True
    out, rc = query('archimedean-term-derived')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : archimedean-term-derived returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'archimedean-term-derived' in o
        ok = ok and g
        print('    %-40s reaches the b333 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTCONFERRED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = "NO GRADE CONFERRED BEYOND THE DERIVATION'S OWN" in out
    a2 = 'ROUTES AGREEING CERTIFY THAT THE ROUTES AGREE' in out
    a3 = 'THE CLAUSE HAS NOT MOVED; K8 STAYS' in out
    a4 = 'VERDICT, AS PRINTED, FIRST' in out and 'NOT MET and not rewritten' in out
    ok = ok and a1 and a2 and a3 and a4
    print('    the answer says no grade conferred beyond the derivation\'s own      : %s' % a1)
    print('    ### and that agreement certifies the routes, not the size           : %s' % a2)
    print('    ### and that the clause has not moved, K8 unowned                   : %s' % a3)
    print('    ### and carries the verdict as printed first, the sealed bar not met : %s' % a4)
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        quiet = no_key(o)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s' % (q, quiet, pre[q], 'PASS' if good else '### FAIL ###'))
    import ferry_scan
    _c, sh = ferry_scan.scan_text(io.open(PATH, encoding='utf-8').read(), [], ferry_scan.stems())
    print('  ### THE INDEX SWEPT AFTER THE WRITE : %d stem hit(s)' % len(sh))
    ok = ok and not sh
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
