# -*- coding: utf-8 -*-
"""b723_support_rule.py -- H-SUPPORT'S RULE AND ITS OUTPUT, (R333)(4)(i), Component 3 (data/b723_registrations.txt :22-:26, committed alone at
relay 9ad26421 before any zero was named): the rule printed first, then Q0's off-line zeros read, the two banked zeros excluded by name, the
selection and each a*_pred = K / (beta - 1/2) against the reach of b707's ladder (its top, 2 log 192).

### THE LIST: Q0's list complete to 445 as b711 banked it -- b675's representatives (the list to 150) and the zeros of the chained complete
### bands above it, read by tools/b711_list.py's `units` and tools/b709_pairs.py's `extended_rows`, both imported unedited (b711's band files
### beside b709's units; no band is run). The off-line zeros are b709's Newton candidates in bands closed by their count (N = on + 2 off;
### RECT_CERTIFY False), as data/b711_list.txt :3-:5 states. Only the zeros with beta > 1/2 are read; each one's reflection is its twin.
### K is the registration's 3.097 (:18-:19), the mean of the two banked products printed beside it unrounded; FORCED, not a test.
### Routes: `show` prints the rule and its output ; `bank` writes data/b723_support_rule.txt as well. Written by the Write tool at b723;
### it writes that one bank and nothing else, and computes no onset. Nothing here proves RH or GRH.
"""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

K = 3.097                                          # ### data/b723_registrations.txt :19, "their mean K = 3.097"
BANKED = (('rho0', '0.9532604748', '16.29021', '6.838396011'),       # ### FINDINGS :5667 ; data/b709_grid.txt :441
          ('band', '0.79800', '29.5518', '10.38532711'))             # ### archive-2 :2982 ; data/b709_grid.txt :4501
REACH = 2 * math.log(192)                          # ### b707's ladder top, data/b723_registrations.txt :23
MOST, LEAST = 3, 2
RULE = [
    'THE RULE (data/b723_registrations.txt :22-:26), printed before any zero is named:',
    "  Q0's certified off-line zeros (data/b711_list.json, to height 445) other than the two banked, in decreasing beta - 1/2, those whose",
    "  a*_pred lies within the reach of b707's ladder (its top, 2 log 192), at most three; where fewer than two qualify, the rule continues",
    "  into -15's and -39's certified lists (data/b713_list.json, data/b717_list.json) with each field's own gamma factor and conductor in",
    "  the same template, its price printed before any figure; the rule's output and each a*_pred added by a commit of their own before any onset.",
]


def zeros():
    """Q0's off-line zeros with beta > 1/2 to the list's top: (name, beta, gamma) as strings at 12 places, and the top."""
    import b711_list as L11
    import b709_pairs as P9
    U = L11.units()
    top = L11.top()
    rows, _on, _off = P9.extended_rows(U, top)
    out = []
    for name, sg, tt in rows:
        if name.startswith('off'):
            out.append((name, float(sg.mid()), float(tt.mid())))
    return out, top, len(rows)


def run(write):
    L = ['b723 -- COMPONENT 3, (R333)(4)(i): H-SUPPORT`S RULE AND ITS OUTPUT, EACH a*_pred, BY A COMMIT OF THEIR OWN BEFORE ANY ONSET (2026-10-29)', '',
         '### by tools/b723_support_rule.py; the rule printed first, from the registration committed alone at relay 9ad26421. No onset computed.', '']
    L += RULE + ['']
    for l in L:
        print(l, flush=True)
    Z, top, nrows = zeros()
    M = []
    prods = [(n, float(b) - 0.5, float(a), (float(b) - 0.5) * float(a)) for n, b, g, a in BANKED]
    M.append('THE CONSTANT, FORCED: ' + ' ; '.join('%s (%.10f) x %s = %.6f' % (n, x, a, p) for n, x, a, p in prods)
             + ' ; mean %.6f ; K as registered %s' % (sum(p for *_, p in prods) / 2, K))
    M.append('THE REACH: 2 log 192 = %.6f ; a*_pred within it where beta - 1/2 >= K / reach = %.6f' % (REACH, K / REACH))
    M.append("THE LIST READ: complete to %s ; rows %d ; off-line zeros with beta > 1/2: %d" % (top, nrows, len(Z)))
    M.append('')
    M.append('THE TWO BANKED, EXCLUDED BY NAME:')
    excl = set()
    for n, b, g, a in BANKED:
        hit = [z for z in Z if abs(z[1] - float(b)) < 5e-5 and abs(z[2] - float(g)) < 5e-3]
        M.append('  %-5s beta %s gamma %s -> %s' % (n, b, g, ', '.join('%s (%.10f + %.6fi)' % h for h in hit) if len(hit) == 1
                                                   else 'NOT FOUND ONCE (%d hits)' % len(hit)))
        excl.update(h[0] for h in hit)
    M.append('  EXCLUDED %d of 2 -- %s' % (len(excl), 'AS WANTED' if len(excl) == 2 else 'NOT AS WANTED'))
    M.append('')
    rest = sorted((z for z in Z if z[0] not in excl), key=lambda z: -z[1])
    M.append('THE ZEROS IN DECREASING beta - 1/2, a*_pred = K / (beta - 1/2), until a*_pred passes the reach:')
    sel, printed = [], 0
    for name, b, g in rest:
        printed += 1
        ap = K / (b - 0.5)
        ok = ap <= REACH
        M.append('  %-6s beta %.10f gamma %11.6f  beta-1/2 %.10f  a*_pred %9.6f  %s' % (
            name, b, g, b - 0.5, ap, ('SELECTED' if len(sel) < MOST else 'WITHIN REACH, PAST THE THREE') if ok else 'BEYOND REACH'))
        if ok and len(sel) < MOST:
            sel.append((name, b, g, ap))
        if not ok:
            break
    within = sum(1 for z in rest if K / (z[1] - 0.5) <= REACH)
    M.append('  printed %d of %d (the rest have smaller beta - 1/2 and larger a*_pred) ; within reach %d ; selected %d' % (
        printed, len(rest), within, len(sel)))
    M.append('')
    if len(sel) < LEAST:
        M.append('FEWER THAN TWO QUALIFY: the rule continues into -15 and -39 (its price printed before any figure).')
    M.append('THE SELECTION, EACH a*_pred:')
    for i, (name, b, g, ap) in enumerate(sel, 1):
        M.append('  (%d) Q0 %s = %.10f + %.6fi ; beta - 1/2 = %.10f ; a*_pred = %.6f ; falsified where |a*/a*_pred - 1| > 0.03, i.e. a* outside [%.6f, %.6f]' % (
            i, name, b, g, b - 0.5, ap, 0.97 * ap, 1.03 * ap))
    M.append('')
    M.append('### ### **H-SUPPORT`S RULE: ZEROS READ %d ; BANKED EXCLUDED %d OF 2 ; WITHIN REACH %d ; SELECTED %d ; CONTINUES INTO -15/-39 %s ; ONSETS COMPUTED 0.**' % (
        len(Z), len(excl), within, len(sel), 'YES' if len(sel) < LEAST else 'NO'))
    for l in M:
        print(l)
    if write:
        p = os.path.join(D, 'b723_support_rule.txt')
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(L + M) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/b723_support_rule.txt')
    return 0 if len(excl) == 2 else 1


if __name__ == '__main__':
    verb = sys.argv[1] if len(sys.argv) > 1 else ''
    if verb not in ('show', 'bank'):
        print('usage: b723_support_rule.py show | bank')
        sys.exit(2)
    sys.exit(run(verb == 'bank'))
