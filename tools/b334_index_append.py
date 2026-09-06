# -*- coding: utf-8 -*-
"""b334_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOPROOF`.** ### A reader who asks *what does the aim-map say*
### must be handed a chart -- the narrowest points, the crossing region, the softness of the pair, the three
### expectations scored -- with the sentence that a chart is not a proof and that the quantifier stays unowned;
### never a sentence that reads as a result about the clause. ### The verdicts and the row numbers are read
### from the run files at write time.
### ### **`the chart is a proof`, `the quantifier owned` AND `the cost census` STAY UNKEYED** -- the last is the
### next act's. ### The index is swept for stems after the write.
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


CH = load('b334_chart.json')
CORR = io.open(os.path.join(D, 'b334_corr_run.txt'), encoding='utf-8').read()
_m = re.search(r'rows to append : (\d+) and (\d+)', CORR)
ROWS = '%s and %s' % (_m.group(1), _m.group(2))
NAV = CH['navigator']
NARROW = '; '.join('%s at gamma %.6f' % (k, v['gamma']) for k, v in sorted(CH['narrowest'].items()) if not k.endswith('_margin'))
CROSS = '; '.join('a = %g at gamma %.6f' % (a, gm) for (_l, a, gm, _p) in CH['crossing']) or 'EMPTY'

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'aim-map': ['the aim-map', 'aim map', 'the aim map', 'the room the arithmetic leaves', 'the chart', 'the chart over aims',\n"
    "                'the narrowest points', 'the crossing region over aims', 'the softest pair over aims', 'K5 and K6 over aims',\n"
    "                'soften together', 'what does the aim-map say', 'the reaching leg', 'the covered leg'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE AIM-MAP (b334).\n"
    "    (\"aim-map\", \"b334 (a computation on the certified instruments; a finite-reach chart over aims; interpreted by nobody)\",\n"
    "     \"THE ROOM THE ARITHMETIC LEAVES, CHARTED OVER AIMS: b328's sine-aimed even seed at every height of the sealed grid, for zeta and for the\"\n"
    "     \" Epstein function side by side, at the reaching widths a = 40, 81 (the phase past 45 degrees at every off-line aim) and the covered widths\"\n"
    "     \" a = 1.3, 1.41 (where the square on the stable cut and the remainder are instruments the record certifies). Per aim, like for like by name:\"\n"
    "     \" the archimedean distribution by the derived kernel on two transforms and by the principal-value witness (150); the square at two frames;\"\n"
    "     \" the margin as A_z - Tr and as minus the remainder by two quadratures, the identity residual printed; the prime sum by two routes; the\"\n"
    "     \" places side gated. THE NARROWEST POINTS: " + NARROW + ". THE CROSSING REGION for Z_Q: " + CROSS + ". (F1) the prime sum inside the margin\"\n"
    "     \" at every aim at this reach: " + NAV['F1'] + " -- A PASSED TEST OVER A GRID AT THIS REACH AND NOTHING MORE. (F2) the crossing region contains the banked\"\n"
    "     \" off-line zeros' aims: " + NAV['F2'] + " -- THE NEGATIVE CONTROL CHARTED. (F3) K5 and K6 soften together over aims: " + NAV['F3'] + " (Spearman " + ('%+.4f' % CH['spearman_s5_s6']) + ").\",\n"
    "     \"### A CHART IS NOT A PROOF. ### THE QUANTIFIER K8 STAYS UNOWNED. ### NO GRADE: THE SOFTEST PAIR GAINS A BEHAVIOUR OVER AIMS, FILED AS THE\"\n"
    "     \" CLAUSE'S FIRST CHART. ### Signs certified by the gate; sizes at named resolutions. ### The cost census named as next. ### NO TERMINAL.\"\n"
    "     \" ### M-2 UNCHANGED\",\n"
    "     \"data/b334_the_aim_map.txt; data/b334_chart_run.txt; data/b334_grid_run.txt; data/b334_leg_reaching_40_run.txt; data/b334_leg_reaching_81_run.txt;\"\n"
    "     \" data/b334_leg_covered_run.txt; data/b334_registration_2026-09-06.txt (sealed before any seed); FACES_LEDGER.md (the b334 update: S1 / K5, K6;\"\n"
    "     \" F7; b328's block); CORRESPONDENCE.md rows " + ROWS + "\"),\n"
)

ALIASES = ('the aim-map', 'aim map', 'the room the arithmetic leaves', 'the chart', 'the narrowest points', 'the crossing region over aims',
           'the softest pair over aims', 'K5 and K6 over aims', 'what does the aim-map say')
MUST_NOT_HIT = ('the chart is a proof', 'the quantifier owned', 'the cost census')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b334 -- THE INDEX KEY. ### THE AIM-MAP.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'aim-map'" in txt)
    have_row = ('"aim-map"' in txt)
    print('  aim-map    key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('aim-map')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : aim-map returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'aim-map' in o
        ok = ok and g
        print('    %-40s reaches the b334 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOPROOF -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A CHART IS NOT A PROOF' in out
    a2 = 'THE QUANTIFIER K8 STAYS UNOWNED' in out
    a3 = 'A PASSED TEST OVER A GRID AT THIS REACH AND NOTHING MORE' in out
    a4 = 'THE SOFTEST PAIR GAINS A BEHAVIOUR OVER AIMS' in out
    ok = ok and a1 and a2 and a3 and a4
    print('    the answer says a chart is not a proof                         : %s' % a1)
    print('    ### and that the quantifier stays unowned                       : %s' % a2)
    print('    ### and that (F1) is a passed test at this reach, nothing more  : %s' % a3)
    print('    ### and that the pair gains a behaviour, not a grade            : %s' % a4)
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
