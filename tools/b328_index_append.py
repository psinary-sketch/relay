# -*- coding: utf-8 -*-
"""b328_index_append.py -- ONE KEY, TWO ROWS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTGENERAL`.** ### A reader who asks *does the instrument
### see a counterexample* must be handed the verdict WITH its scope -- this family, this instrument,
### this reach -- and b326's verdict on the arc's family unmoved; never a `SEES IT` as a sentence about
### the method or about zeta. ### The verdict words are read from `data/b328_family.json`.
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
FAM = json.load(io.open(os.path.join(D, 'b328_family.json'), encoding='utf-8'))
V = FAM['verdict']
WHERE = str(FAM['sees'] if V == 'SEES IT' else (FAM['flips'] if V == 'ZETA FLIPS' else FAM['partial']))

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'discriminating-family': ['discriminating family', 'the discriminating family', 'the phase condition',\n"
    "                              'the four-term sum', 'the off-line quadruple', 'the sine-aimed seed',\n"
    "                              'the odd seed', 'the quadruple sum', 'forty-five degrees', 'the phase threshold',\n"
    "                              'the negative control under the family', 'sees it'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE DISCRIMINATING FAMILY -- THE CONDITION AND THE SEEDS (b328).\n"
    "    (\"discriminating-family\", \"b328 (a derivation from the pinned source; a construction)\",\n"
    "     \"for f = g * g^7 the four-term sum at an off-line quadruple {rho, conj rho, 1 - rho, 1 - conj rho} is\"\n"
    "     \" 4 Re[G(c) G(-c)], c = rho - 1/2, G the seed's transform; for an EVEN seed 4 |G|^2 cos(2 phi),\"\n"
    "     \" NEGATIVE EXACTLY PAST FORTY-FIVE DEGREES OF PHASE; an odd component contributes -4 Re G_o^2, negative\"\n"
    "     \" only below it. ### Checked against b326's banked four terms at the thirteen arc cells (phases -5.3\"\n"
    "     \" to 24.1 degrees, all below the threshold; the arc's sums positive for exactly that reason). ### Two\"\n"
    "     \" seeds built on the corpus's bump and aimed at the first off-line Epstein zero: the sine-aimed even\"\n"
    "     \" seed at 89 degrees, the cosine-aimed odd seed at 0, widths a = 20, 40, 81, 160, each lawful\"\n"
    "     \" (Definition 3.1; the pole conditions g~(0) = g~(1) = 0 measured)\",\n"
    "     \"### THE PHASE COMES FROM sinh(delta v): zero on the line, small at narrow widths, set by a sine aimed\"\n"
    "     \" at the ordinate. ### (F1) DERIVES; (F2) MET. ### Two sealed bars found defective by running them,\"\n"
    "     \" neither edited: (B1) at 1e-9 fails on the square's discretization (1.1e-7, second order in the\"\n"
    "     \" correlation grid); (B4) at 1e-10 fails because Simpson straddles a kink in every triple on the native\"\n"
    "     \" nodes (exact at 2x; a Gauss-Legendre route meets the bar). ### The lore gains the rule with its gate.\"\n"
    "     \" ### NO GRADE MOVED\",\n"
    "     \"data/b328_the_discriminating_family.txt; data/b328_derive_run.txt; data/b328_build_run.txt;\"\n"
    "     \" data/b328_routes_run.txt; tools/b328_family.py; data/b328_registration_2026-09-05.txt (sealed before\"\n"
    "     \" any run); CORRESPONDENCE.md row 168\"),\n"
    "    # ### THE DISCRIMINATING FAMILY -- THE CONTROL'S VERDICT (b328).\n"
    "    (\"discriminating-family\", \"b328 (a computation on the explicit-formula instrument; the verdict)\",\n"
    "     \"the negative control under the two seeds at four widths, the places sides computed with NO ZERO and\"\n"
    "     \" every sign through the noise-floor gate, the closure with every located zero as corroboration:\"\n"
    "     \" **VERDICT: " + V + "** at " + WHERE.replace('"', '') + ". ### THE ZETA CONTROL under the same seeds: see the\"\n"
    "     \" bank's cell table -- a flip, had one occurred, is the act's first finding\",\n"
    "     \"### A VERDICT ON THIS FAMILY, ON THIS INSTRUMENT, AT THIS REACH -- NOT ON THE METHOD AND NOT ON ZETA.\"\n"
    "     \" ### b326's DOES NOT SEE IT on the arc's family STANDS; what changed is the family. ### The entailment,\"\n"
    "     \" if SEES IT: the finite-instance places sum computed without any zero distinguishes a holding\"\n"
    "     \" hypothesis from a failing one on this family, and the zeta window is a passed test FOR THIS FAMILY.\"\n"
    "     \" ### NOTHING ABOUT TOTALITY, h2 OR THE ROSTER. ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b328_family_run.txt; data/b328_family.json; data/b328_cell_*_run.txt; FACES_LEDGER.md (the b328\"\n"
    "     \" update); OPEN_TRAILS.md (W-ORD-DISCRIMINATING-FAMILY, updated); CORRESPONDENCE.md row 169\"),\n"
)

NEW_KEYS = ('discriminating-family',)
ALIASES = ('the discriminating family', 'the phase condition', 'the four-term sum', 'the off-line quadruple',
           'the sine-aimed seed', 'the odd seed', 'forty-five degrees', 'sees it')
MUST_NOT_HIT = ('the archimedean membership', 'the window class')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b328 -- THE INDEX KEY. ### THE DISCRIMINATING FAMILY.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'discriminating-family'" in txt)
    have_row = ('"discriminating-family"' in txt)
    print('  discriminating-family    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('discriminating-family')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 2
    ok = ok and good
    print('  READ BACK : discriminating-family returns %d row(s), 2 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'discriminating-family' in o
        ok = ok and g
        print('    %-40s reaches the b328 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTGENERAL -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'NOT ON THE METHOD AND NOT ON ZETA' in out
    a2 = "b326's DOES NOT SEE IT on the arc's family STANDS" in out
    a3 = ('VERDICT: %s' % V) in out
    ok = ok and a1 and a2 and a3
    print('    the answer scopes the verdict to the family BY NAME        : %s' % a1)
    print("    ### and keeps b326's verdict on the arc's family           : %s" % a2)
    print('    ### and carries the verdict word verbatim                  : %s' % a3)
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        quiet = no_key(o)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s' % (q, quiet, pre[q], 'PASS' if good else '### FAIL ###'))
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import ferry_scan
    _c, sh = ferry_scan.scan_text(io.open(PATH, encoding='utf-8').read(), [], ferry_scan.stems())
    print('  ### THE INDEX SWEPT AFTER THE WRITE : %d stem hit(s)' % len(sh))
    ok = ok and not sh
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
