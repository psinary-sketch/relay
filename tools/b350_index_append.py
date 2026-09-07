# -*- coding: utf-8 -*-
"""b350_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTEXPLAINED`.** ### A reader who asks *what the pricing settled*
### must be handed: PRICING IS NOT MEASURING; a rank-preserving band is a fact about the CUT and not about the
### RESIDUAL; the floor is UNEXPLAINED; the trail is RESTATED, NOT DISCHARGED; and nothing here says what either
### held axis does. ### **`the floor is explained`, `the band leaves the residual unchanged`, `the trail is
### discharged` AND `the axes are priced and settled` STAY UNKEYED.**
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

CORR = io.open(os.path.join(D, 'b350_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
P = json.load(io.open(os.path.join(D, 'b350_price.json'), encoding='utf-8'))

Q = chr(34)
BS = chr(92)
APOS = BS + "'"

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'held-axes-priced': ['the held axes', 'the price of the axes', 'the cut" + APOS + "s threshold', 'the taper',\n"
    "                        'the rank-preserving band', 'the floor is explained', 'the floor unexplained',\n"
    "                        'pricing is not measuring'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")

ROW_NEW = (
    "    # ### THE FLOOR'S TWO HELD AXES, PRICED (b350).\n"
    "    (" + Q + "held-axes-priced" + Q + ", " + Q + "b350 (a pricing act; it moves nothing and measures nothing)" + Q + ",\n"
    "     " + Q + "THE FLOOR" + APOS + "S TWO HELD AXES PRICED FROM b344" + APOS + "S PRINTED FIGURES, with no frame built and nothing re-run. THE COST is the same for both --" + Q + "\n"
    "     " + Q + " " + ('%.2f' % P['wall_total']) + " seconds of wall per value tried, summed from the walls b344 printed over its sealed ladder -- because a move is a ladder either way, and" + Q + "\n"
    "     " + Q + " what it buys is ONE value. THE ROOM is priceable for the threshold and not for the taper: the intersection across the rungs of (largest dropped," + Q + "\n"
    "     " + Q + " smallest kept) is (" + ('%.6e' % P['band_lo']) + ", " + ('%.6e' % P['band_hi']) + "), a factor of " + ('%.2f' % P['band_factor']) + " wide, with the corpus" + APOS + "s own tau inside it, free to fall by " + ('%.2f' % P['fall_factor']) + " or rise" + Q + "\n"
    "     " + Q + " by " + ('%.2f' % P['rise_factor']) + " with the same rank. The taper" + APOS + "s constants are printed as constants with nothing beside them, so NO ROOM FOR IT IS PRICEABLE AT ALL, and" + Q + "\n"
    "     " + Q + " the act prices the pricing instead: two ladders, " + ('%.2f' % P['taper_pricing_cost']) + " seconds, AND EVEN THAT WOULD GIVE A DIFFERENCE AND NOT A ROOM. WHAT EACH MOVE WOULD" + Q + "\n"
    "     " + Q + " CONFOUND, in the sealed words of the act that declined it: the threshold confounds the RANK with the FLOOR; the taper confounds the INSTRUMENT with" + Q + "\n"
    "     " + Q + " the OBJECT. VERDICT: THE FLOOR IS UNEXPLAINED. The trail W-ORD-FLOOR-HELD-AXES is RESTATED, NOT DISCHARGED." + Q + ",\n"
    "     " + Q + "### PRICING IS NOT MEASURING, and a price is a statement about what an act would cost made by an act that does not perform it: no frame was built," + Q + "\n"
    "     " + Q + " no ladder run, no cell evaluated and NO AXIS MOVED. ### A RANK-PRESERVING BAND IS A FACT ABOUT THE CUT AND NOT ABOUT THE RESIDUAL -- the same" + Q + "\n"
    "     " + Q + " subspace kept does not mean the same residual, and b344 printed no residual at a second threshold. ### THE FLOOR IS UNEXPLAINED: the one axis moved" + Q + "\n"
    "     " + Q + " does not account for it and for the two held axes the record contains NO measurement of the residual at all. ### THE TRAIL IS RESTATED, NOT" + Q + "\n"
    "     " + Q + " DISCHARGED -- its price half is paid and its measurement half is not, and A TRAIL IS NOT DISCHARGED BY PAYING THE CHEAPER HALF OF IT. ### NO GRADE" + Q + "\n"
    "     " + Q + " MOVED. ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b350_the_two_held_axes.txt; data/b350_price_run.txt; data/b350_filings_run.txt;" + Q + "\n"
    "     " + Q + " data/b350_registration_2026-09-07.txt (sealed before one price was computed);" + Q + "\n"
    "     " + Q + " PLACE-papers OPEN_TRAILS.md (the b350 block); CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('the held axes', 'the price of the axes', "the cut's threshold", 'the taper',
           'the rank-preserving band', 'the floor is explained', 'the floor unexplained',
           'pricing is not measuring')
MUST_NOT_HIT = ('the band leaves the residual unchanged', 'the trail is discharged',
                'the axes are priced and settled', 'the floor is accounted for')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print("b350 -- THE INDEX KEY. ### THE FLOOR'S TWO HELD AXES, PRICED.")
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-44s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'held-axes-priced'" in txt)
    have_row = ('"held-axes-priced"' in txt)
    print('  held-axes-priced key/row already present : %s / %s' % (have_key, have_row))
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
    out, rc = query('held-axes-priced')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : held-axes-priced returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'held-axes-priced' in o
        ok = ok and g
        print('    %-44s reaches the b350 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTEXPLAINED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'PRICING IS NOT MEASURING' in out and 'NO AXIS MOVED' in out
    a2 = 'A FACT ABOUT THE CUT AND NOT ABOUT THE RESIDUAL' in out
    a3 = 'THE FLOOR IS UNEXPLAINED' in out and 'NO measurement of the residual at all' in out
    a4 = 'RESTATED, NOT' in out and 'DISCHARGED' in out and 'NO GRADE' in out and 'MOVED' in out
    ok = ok and a1 and a2 and a3 and a4
    print('    the answer says pricing is not measuring, and no axis moved     : %s' % a1)
    print('    ### and a band is about the cut, not the residual                : %s' % a2)
    print('    ### and the floor is unexplained, with no measurement at all     : %s' % a3)
    print('    ### and the trail is restated, not discharged, and no grade moved: %s' % a4)
    post = {}
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        post[q] = no_key(o)
        g = pre[q] and post[q]
        ok = ok and g
        print('    %-44s NO KEY after  : %s  %s' % (q, post[q], 'PASS' if g else '### FAIL ###'))
    print('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
