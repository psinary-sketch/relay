# -*- coding: utf-8 -*-
"""b327_index_append.py -- TWO KEYS, THREE ROWS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOEQUIV`.** ### A reader who asks *is the Li margin the
### Sonin margin* or *are the faces equivalent* must be handed the ledger's refusal BY NAME -- a map of the
### premise, not a carrier of it -- with the bridge OWED and typed, never a row that reads as the
### equivalence the deposit withholds. ### And a reader who asks about the archimedean channel must be
### handed the constant that separates it from the archimedean place, not a `SAME`.
### ### **THE VERDICT WORDS ARE READ FROM `data/b327_bridge.json`.**
### ### **`the archimedean membership` AND `the window class` STAY UNKEYED.** ### The index is swept for
### stems after the write.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'tools', 'banked_index.py')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NL = chr(10)
B = json.load(io.open(os.path.join(D, 'b327_bridge.json'), encoding='utf-8'))
Q1, Q2 = B['q1'], B['q2']

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'faces-ledger': ['faces ledger', 'the faces ledger', 'the faces', 'the ledger of faces',\n"
    "                     'the register pentagon', 'the pentagon', 'the five faces', 'the cascades',\n"
    "                     'the owed bridges', 'the fixed-point silence', 'the sonin margin', 'the li margin'],\n"
    "    'li-weil-bridge': ['li-weil bridge', 'the li-weil bridge', 'the li-to-weil bridge', 'the bridge read',\n"
    "                       'the li coefficients as the weil functional', 'the archimedean channel',\n"
    "                       'the pole constant', 'one distribution on two families', 'the li test function',\n"
    "                       'the li family'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE FACES LEDGER (b327).\n"
    "    (\"faces-ledger\", \"b327 (a ledger build, author-authorized 2026-09-04)\",\n"
    "     \"PLACE-papers/FACES_LEDGER.md: thirteen rows -- the pentagon's five faces as the deposit states\"\n"
    "     \" them, the finite-instance identity, the Sonin margin, the Li margin, the spectral-realization\"\n"
    "     \" wall, the fixed-point silence, the two-radius family, the Epstein negative control at b326's\"\n"
    "     \" result, and the live row (the Li-to-Weil bridge) -- each with its claim quoted from its\"\n"
    "     \" emitting file, graded PROVED / MEASURED / IMPORTED / NAMED-ONLY, its correspondence rows, and\"\n"
    "     \" its owed bridges; a cascade section with one of STATED / OWED / NONE for all 78 pairs\",\n"
    "     \"### A MAP OF THE PREMISE, NOT A CARRIER OF IT. ### THE LEDGER CERTIFIES NOTHING AND COMPILES\"\n"
    "     \" NO EQUIVALENCE -- the deposit's refusal is quoted in its head and governs it; every row's\"\n"
    "     \" grade is its owning act's and no row is promoted by its neighbours. ### Rows enter only through\"\n"
    "     \" tools/b327_faces_row.py (duplicates refused, notation guarded, every quotation verified against\"\n"
    "     \" its emitter before writing, read back after every write). ### The owed bridges by ID:\"\n"
    "     \" W-ORD-LI-WEIL-BRIDGE, W-ORD-DISCRIMINATING-FAMILY, W-ORD-LI-FAMILY-CONTROL. ### NO GRADE MOVED\",\n"
    "     \"PLACE-papers/FACES_LEDGER.md; FINDINGS.md anchor faces-ledger; data/b327_the_faces_ledger.txt;\"\n"
    "     \" data/b327_registration_2026-09-05.txt (sealed before any instrument ran); CORRESPONDENCE.md row 166\"),\n"
    "    # ### THE LI-TO-WEIL BRIDGE READ (b327).\n"
    "    (\"li-weil-bridge\", \"b327 (a read under the import bar; a derived map with its corroboration)\",\n"
    "     \"the source: Lagarias, Li coefficients for automorphic L-functions, arXiv:math/0404394v4, pinned by\"\n"
    "     \" hash (restating Bombieri-Lagarias 1999): lambda_n = S_inf(n) - S_f(n) + 1 -- the archimedean place,\"\n"
    "     \" the finite places, the pole at s = 0 -- on the Li test family G_n(s) = 1 - (1 - 1/s)^n. ### THE MAP,\"\n"
    "     \" derived as a sealed bar and corroborated at n <= 30 to 1.3e-251 by two routes: the deposit's\"\n"
    "     \" archimedean channel is lambda_A(n) = S_inf(n) + 1. ### QUESTION ONE (the channel against the\"\n"
    "     \" archimedean place): " + Q1 + " -- the constant 1, the log s term of the deposit's own split, the\"\n"
    "     \" source's pole at s = 0. ### QUESTION TWO (the Li margin and the Sonin margin as one functional):\"\n"
    "     \" " + Q2 + " -- the Li margin's second term is the finite places; the Sonin margin's is the\"\n"
    "     \" compressed square, not a zero channel\",\n"
    "     \"### ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL: 2 Re(Gamma_R'/Gamma_R), the atlas's\"\n"
    "     \" kernel, is what both channels evaluate. ### THE BRIDGE STAYS OWED (W-ORD-LI-WEIL-BRIDGE), typed\"\n"
    "     \" more sharply: a relation between the compressed square on the Sonin family and the finite-place\"\n"
    "     \" channel on the Li family, or its impossibility. ### The order's if-SAME branch did not fire; the\"\n"
    "     \" finite-range certificate says nothing about the Sonin margin on the Li family (no compact support,\"\n"
    "     \" outside Theorem 1's class). ### The fourth control priced, not run (W-ORD-LI-FAMILY-CONTROL).\"\n"
    "     \" ### NO THEOREM PROVED. ### NO GRADE MOVED. ### THE EQUIVALENCE THE DEPOSIT WITHHOLDS IS NOT STATED\",\n"
    "     \"data/b327_bridge_run.txt; data/b327_bridge.json; data/b327_source.txt (the pin); tools/b327_bridge.py;\"\n"
    "     \" FACES_LEDGER.md row L1; CORRESPONDENCE.md row 167\"),\n"
    "    # ### THE TWO NOTES, FILED AS CONTACTS (b327).\n"
    "    (\"faces-ledger\", \"b327 (two contacts in the emerging-programmes ledger; not seeds)\",\n"
    "     \"EMERGING_RESEARCH_PROGRAMMES.md, Contacts filed 2026-09-05: the Curie reading of the\"\n"
    "     \" eigenvalue-one boundary (the remainder's weight diverging at the boundary as a susceptibility;\"\n"
    "     \" one consequence: sensitivity of the remainder to test-function perturbation near the boundary,\"\n"
    "     \" checkable on the instrument, not checked); the cubit reading of the 256 rules (each a function on\"\n"
    "     \" (Z/2)^3; rule 110's one-set a five-point Fano subset containing two lines, counted by\"\n"
    "     \" tools/b327_notes.py; the question which Fano subsets define universal rules, not answered)\",\n"
    "     \"### CONTACTS, NOT SEEDS: no promotion criterion, no claim, no grade. ### Provenance: the navigator's\"\n"
    "     \" conversation layer, 2026-09-04, ratified by the b327 ferry. ### Filed nowhere research-facing\",\n"
    "     \"PLACE-papers/EMERGING_RESEARCH_PROGRAMMES.md (the b327 contacts block); data/b327_notes_run.txt\"),\n"
)

NEW_KEYS = ('faces-ledger', 'li-weil-bridge')
ALIASES = ('the faces ledger', 'the pentagon', 'the five faces', 'the sonin margin', 'the li margin',
           'the fixed-point silence', 'the owed bridges', 'the li-weil bridge', 'the bridge read',
           'the archimedean channel', 'the pole constant', 'one distribution on two families', 'the li family')
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
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b327 -- THE INDEX KEYS. ### THE FACES LEDGER, AND THE LI-TO-WEIL BRIDGE.')
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
    print('  VERDICT FIXTURE : fires on the index\'s own NO KEY line : %s ; quiet on the phrase quoted inside a row : %s' % (rv, not qv))
    ok = rv and not qv
    print('  ### READ BACK BY QUERYING THE INDEX ITSELF:')
    need = {'faces-ledger': 2, 'li-weil-bridge': 1}
    for k in NEW_KEYS:
        out, rc = query(k)
        good = (not no_key(out)) and (k in out) and rc == 0
        n = out.count('act      :')
        enough = n >= need[k]
        ok = ok and good and enough
        print('    %-24s returns a row : %s ; returns %d row(s), %d required  %s' % (k, good, n, need[k], 'PASS' if (good and enough) else '### FAIL ###'))
    print('  ### THE ALIASES (each must reach one of THIS act\'s keys):')
    for q in ALIASES:
        out, _rc = query(q)
        good = (not no_key(out)) and any(k in out for k in NEW_KEYS)
        ok = ok and good
        print('    %-46s reaches a b327 key : %s  %s' % (q, good, 'PASS' if good else '### FAIL ###'))
    print('  ### ### **G-NOEQUIV -- THE ARM THIS FILE EXISTS FOR.**')
    out, _rc = query('the faces ledger')
    a1 = 'A MAP OF THE PREMISE, NOT A CARRIER OF IT' in out
    a2 = 'COMPILES NO EQUIVALENCE' in out
    a3 = 'W-ORD-LI-WEIL-BRIDGE' in out
    ok = ok and a1 and a2 and a3
    print('    the answer refuses the carrier reading BY NAME        : %s' % a1)
    print('    ### and says no equivalence is compiled               : %s' % a2)
    print('    ### and hands the bridge as OWED, by ID               : %s' % a3)
    out2, _rc2 = query('the archimedean channel')
    b1 = 'NOT ONE FUNCTIONAL' in out2
    b2 = 'THE BRIDGE STAYS OWED' in out2
    b3 = Q1 in out2
    ok = ok and b1 and b2 and b3
    print('  ### ### **THE SECOND ARM -- the channel is not handed back as SAME.**')
    print('    the answer says not one functional                    : %s' % b1)
    print('    ### and that the bridge stays owed                    : %s' % b2)
    print('    ### and carries the question-one verdict verbatim     : %s' % b3)
    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s' % (q, quiet, pre[q], 'PASS' if good else '### FAIL ###'))
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
