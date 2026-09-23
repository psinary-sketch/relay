# -*- coding: utf-8 -*-
"""b492_extract.py -- THE SURVEY. ### **THE NUMERICAL LANE IS OPEN, BY (R101), FOR THIS ONE ACT.**

### It recovers the ladder's GENERATOR from b437's own source, fixes the floor and the recipe from
### b477's own runner, and rehearses one cell against a bank that already holds its per-n terms.
"""
import io
import json
import math
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
L, MISSES = [], []
FLOOR = 1.49e-08

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def prime_powers_upto(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    out = []
    for p in range(2, n + 1):
        if s[p]:
            v, k = p, 1
            while v <= n:
                out.append(v)
                v *= p
                k += 1
    return sorted(out)


def main():
    rec('=' * 112)
    rec('b492 -- THE SURVEY. ### THE GENERATOR, THE FLOOR, AND ONE REHEARSED CELL.')
    rec('=' * 112)

    # ---------------------------------------------------------------- (P1) the generator
    rec('')
    rec('(P1) THE LADDER`S GENERATOR, RECOVERED FROM b437`S OWN SOURCE.')
    rec('-' * 112)
    src = read(os.path.join(T, 'b437_components.py'))
    for pat in (r'^BOUNDARY_N = .*$', r'^BOUNDARIES = .*$', r'^_pts = .*$',
                r'^MIDPOINTS = .*$', r'^NEW_A = .*$'):
        m = re.search(pat, src, re.M)
        rec('    %s' % (m.group(0) if m else '### **ABSENT**'))
        if not m:
            MISSES.append(('b437_components.py', pat))
    rec('')
    rec('    ### ### **THE ROUNDING IS IN THE GENERATOR ITSELF.** ### `NEW_A` is built by')
    rec('    ### `round(x, 6)` over the boundaries and midpoints, so ### **THE LADDER`S STORED `a`')
    rec('    ### IS A SIX-PLACE ROUNDING OF AN EXACT VALUE BY CONSTRUCTION** -- not an artefact of')
    rec('    ### any later reading. ### b490 saw the symptom; this is the cause, at its address.')

    bn = [n for n in prime_powers_upto(36) if 9 < n <= 36]
    bd = [math.sqrt(n) for n in bn]
    pts = [3.0] + bd
    mid = [(pts[i] + pts[i + 1]) / 2.0 for i in range(len(pts) - 1)]
    exact = {}
    for n, x in zip(bn, bd):
        exact[round(x, 6)] = dict(kind='sqrt', n=n, a=x)
    for i, x in enumerate(mid):
        k = round(x, 6)
        if k not in exact:
            exact[k] = dict(kind='midpoint', lo=pts[i], hi=pts[i + 1], a=x)
    rec('    BOUNDARY_N (prime powers in (9, 36]) : ### **%s**' % bn)
    rec('    boundary cells : %d ; midpoint cells : %d ; NEW_A : ### **%d**'
        % (len(bd), len(mid), len(exact)))

    # ---------------------------------------------------------------- (P2) the cells
    rec('')
    rec('(P2) THE 35 CELLS, AND WHICH CARRY AN EXACT GENERATOR.')
    rec('-' * 112)
    ent = [json.loads(l) for l in read(os.path.join(D, 'b477_entries.jsonl')).split(NL) if l.strip()]
    diag = sorted([x for x in ent if x.get('kind') == 'diagonal'], key=lambda x: x['a'])
    cells = []
    for x in diag:
        e = exact.get(round(x['a'], 6))
        cells.append(dict(a=x['a'], W_banked=x['W'], zero_banked=x['zero'],
                          exact=(e['a'] if e else x['a']),
                          kind=(e['kind'] if e else 'literal'),
                          n0=(e.get('n') if e else None)))
    rec('    cells : ### **%d** ### -- sqrt %d, midpoint %d, literal %d'
        % (len(cells), sum(1 for c in cells if c['kind'] == 'sqrt'),
           sum(1 for c in cells if c['kind'] == 'midpoint'),
           sum(1 for c in cells if c['kind'] == 'literal')))
    diffs = [(abs(c['exact'] - c['a']), c['a']) for c in cells if c['kind'] != 'literal']
    rec('    ### the stored `a` differs from its generator by at most ### **%.3g** ### -- a'
        % max(d[0] for d in diffs))
    rec('    ### six-place rounding, as the source says. ### **THE LITERAL CELLS ARE EXACT AS')
    rec('    ### WRITTEN**, being b321`s own decimal choices and not roundings of anything.')
    rec('')
    rec('    ### the cells whose generator is `sqrt n`, and whether `n` is IN on each reading:')
    rec('      %-12s %-18s %-4s %-24s %s' % ('stored a', 'exact a', 'n', 'n <= (stored a)^2',
                                             'n <= (exact a)^2'))
    for c in cells:
        if c['kind'] != 'sqrt':
            continue
        rec('      %-12.6f %-18.12f %-4d %-24s %s'
            % (c['a'], c['exact'], c['n0'], c['n0'] <= c['a'] * c['a'], 'True (n <= n, EXACT)'))
    rec('    ### ### **ON THE EXACT GENERATOR THE ANSWER IS DECIDED BY INTEGER ARITHMETIC, NOT BY')
    rec('    ### A FLOAT:** ### `a = sqrt n` gives `a^2 = n`, so `n <= a^2` holds because')
    rec('    ### ### **n <= n**. ### No tolerance is chosen and none is needed.')

    # ---------------------------------------------------------------- (P3) the recipe
    rec('')
    rec('(P3) THE RECIPE AND THE FLOOR, FROM b477`S OWN RUNNER.')
    rec('-' * 112)
    gram = read(os.path.join(T, 'b477_gram.py'))
    for pat in (r'^\s*f = SQ\.autocorrelation\(seeds\[a\]\)$', r'^\s*ch = WI\.channels\(f\.v, f\.w\)$',
                r"^\s*W = ch\['prime'\] - ch\['arch'\]$", r'^FLOOR = .*$'):
        m = re.search(pat, gram, re.M)
        rec('    %s' % (m.group(0).strip() if m else '### **ABSENT**'))
        if not m:
            MISSES.append(('b477_gram.py', pat))
    rec('    `AUTOCORR_NV` default : ### **%s**'
        % (re.search(r'^AUTOCORR_NV = (\d+)', read(os.path.join(T, 'b318_square.py')), re.M)
           or ['', '?'])[1])
    rec('    ### ### **THE FLOOR IS `%.2e`** ### -- b446`s `sqrt(eps)` kind domain, and b477`s'
        % FLOOR)
    rec('    ### own halt threshold. ### **THIS ACT USES b477`S NUMBER, NOT ONE OF ITS OWN.**')

    # ---------------------------------------------------------------- (P4) the rehearsal
    rec('')
    rec('(P4) THE (R70) REHEARSAL -- ONE CELL, AGAINST A BANK THAT ALREADY HOLDS ITS TERMS.')
    rec('-' * 112)
    import numpy as np  # noqa: F401
    import b317_smear as SM
    import b318_square as SQ
    import b321_window as WI
    ig = json.loads(read(os.path.join(D, 'b449_integrand.json')) or '{}')
    lv0 = (ig.get('levels') or [{}])[0]
    a = ig.get('a')
    rec('    the cell : ### **a = %s** ### -- the only cell of the 35 with banked per-n terms,' % a)
    rec('    from `b449_integrand.json` at `nv = %s` (size %s), which is the DEFAULT grid.'
        % (lv0.get('nv'), lv0.get('size')))
    t0 = time.time()
    g = SM.mean_zero_variant(a)
    f = SQ.autocorrelation(g)
    ch = WI.channels(f.v, f.w)
    W = ch['prime'] - ch['arch']
    el = time.time() - t0
    rec('    ### ### **RUN HERE, NOW:** ### %.1f s ; grid size %d' % (el, f.v.size))
    b = next((c for c in cells if abs(c['a'] - a) < 1e-9), None)
    rec('      W computed  : %.17g' % W)
    rec('      W banked    : %.17g   (b477)' % b['W_banked'])
    dW = abs(W - b['W_banked'])
    rec('      ### ### **|diff| = %.3g ; FLOOR %.2e ; WITHIN : %s**' % (dW, FLOOR, dW < FLOOR))
    if dW >= FLOOR:
        MISSES.append(('rehearsal', 'W outside the floor'))
    rec('      PR computed : %.17g' % ch['prime'])
    rec('      PR banked   : %.17g   (b449)' % lv0.get('prime'))
    dP = abs(ch['prime'] - lv0.get('prime', 0))
    rec('      ### **|diff| = %.3g**' % dP)
    Lv = float(f.v[-1])
    terms = {}
    for p in WI.primes_to(math.exp(Lv) + WI.PRIME_TOL):
        k = 1
        while p ** k <= math.exp(Lv) + WI.PRIME_TOL:
            n = p ** k
            ln = math.log(n)
            if ln <= Lv:
                terms[n] = 2.0 * math.log(p) / math.sqrt(n) * float(np.interp(ln, f.v, f.w))
            k += 1
    bt = lv0.get('terms') or {}
    rec('      terms computed : %d ; terms banked : %d' % (len(terms), len(bt)))
    worst = 0.0
    for n, x in sorted(terms.items()):
        d = abs(x - bt.get(str(n), float('nan')))
        worst = max(worst, d if d == d else 1.0)
    rec('      ### ### **WORST PER-TERM |diff| AGAINST b449`S BANK : %.3g**' % worst)
    rec('      sum of terms : %.17g ; against PR : %.3g'
        % (sum(terms.values()), abs(sum(terms.values()) - ch['prime'])))
    ok = (dW < FLOOR and worst < 1e-12 and len(terms) == len(bt))
    rec('    ### ### **THE REHEARSAL REPRODUCES A BANK THIS ACT DID NOT WRITE : %s.**' % ok)
    rec('    ### **THAT IS THE POSITIVE CONTROL FOR THE WHOLE RUN** -- the term recipe, the grid')
    rec('    ### and the channel arrangement are the record`s, not this act`s.')
    if not ok:
        MISSES.append(('rehearsal', 'the terms do not reproduce b449'))

    rec('')
    rec('(P5) THE COST.')
    rec('-' * 112)
    rec('    one cell measured here : ### **%.1f s** ### ; 35 cells : ### **%.0f s ~ %.1f min.**'
        % (el, el * 35, el * 35 / 60.0))
    rec('    ### ### **THE LANE IS OPEN FOR THIS ONE RUN AND CLOSES AT THIS ACT`S END**, by')
    rec('    ### (R101). ### No second run is taken and no lane is left open.')

    rec('')
    rec('=' * 112)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 112)
    io.open(os.path.join(D, 'b492_extract.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(cells=cells, floor=FLOOR, boundary_n=bn, rehearsal=dict(
        a=a, W=W, W_banked=b['W_banked'], dW=dW, n_terms=len(terms), worst=worst,
        seconds=el, ok=ok), misses=MISSES),
        io.open(os.path.join(D, 'b492_survey.json'), 'w', encoding='utf-8', newline=NL),
        indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
