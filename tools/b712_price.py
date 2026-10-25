# -*- coding: utf-8 -*-
"""b712_price.py -- (R322)(6): THE PRICE OF THE -15 CONTROL FOR b713, data/b712_price.txt (.json). NOTHING OF THE -15 ZEROS IS COMPUTED HERE.

### Written whole by the Write tool at b712. Every figure is read from a bank or computed from one, none typed:
###   b711's band seconds: data/b711_list.json, each route entry carrying `seconds`, the derived copies (`derived_from`) not counted twice;
###   b711's band counts: data/b711_list.json `bands` (N per band, 325 to 445);
###   the zero-count main term N(T) = (T/pi) log(T sqrt(D) / (2 pi e)), checked against Q0's banked counts (D = 23) before it is used at D = 15;
###   the engine's Bessel truncation M proportional to 1/sqrt(D) (tools/b667_epstein_certify.py :107), so the seconds per zero at -15 are
###   scaled by sqrt(23/15) and not reduced for the lower heights (an upper reading, not a fit);
###   the cut for (iii): data/b711_coeffs.txt :11, read by its line.
### The heights proposed, the tools named, the act budget and the source pin are the seat's, each printed as such. Route: `bank` (writes the
### two banks through the membrane), `dry` (prints, writes nothing).
"""
import json
import math
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BAND = 15.0                       # ### b711's band width (data/b711_list.txt :7-:14, 15 height units, two of them cut between two zeros)
TIERS = ((0.0, 100.0, 'the first tier: the record`s three off-line zeros at -15 (two pinned at 12.04 and 15.50, archive :2971) and the route`s rest set'),
         (100.0, 200.0, 'the second tier: the rest set`s reach, entered only where b713`s pair rows ask a height above 100'))
TOLERANCE = 0.03                  # ### the main term's check against Q0's banked counts: within 3 per cent over 325-445


def rd(p):
    with open(p, encoding='utf-8', errors='replace') as fh:
        return fh.read()


def n_main(t, disc):
    return (t / math.pi) * math.log(t * math.sqrt(disc) / (2 * math.pi * math.e)) if t > 0 else 0.0


def _walk(o, out):
    if isinstance(o, dict):
        if 'route' in o and 'seconds' in o:
            out.append(o)
        for v in o.values():
            _walk(v, out)
    elif isinstance(o, list):
        for v in o:
            _walk(v, out)


def compose():
    j = json.load(open(os.path.join(D, 'b711_list.json'), encoding='utf-8'))
    ents = []
    _walk(j, ents)
    seen, comp = set(), []
    for e in ents:
        k = (e['route'], e.get('key'))
        if e.get('derived_from') or k in seen:
            continue
        seen.add(k)
        comp.append(e)
    by = {}
    for e in comp:
        by[e['route']] = by.get(e['route'], 0) + int(e['seconds'])
    secs = sum(by.values())
    bands = j.get('bands') or []
    n_banked = sum(int(b['N']) for b in bands)
    t_lo, t_hi = float(j['base']), float(j['top'])
    n_pred = n_main(t_hi, 23) - n_main(t_lo, 23)
    check = abs(n_pred - n_banked) / n_banked
    per_zero = secs / n_banked
    scale = math.sqrt(23.0 / 15.0)
    rows = []
    for a, b, why in TIERS:
        lo = a
        while lo < b:
            hi = min(b, lo + BAND)
            nz = n_main(hi, 15) - n_main(lo, 15)
            rows.append(dict(tier=why.split(':')[0], lo=lo, hi=hi, zeros=nz, seconds=nz * per_zero * scale))
            lo = hi
    cl = rd(os.path.join(D, 'b711_coeffs.txt')).split(NL)
    m = re.search(r'the coefficients through (\d+):', cl[10] if len(cl) > 10 else '')
    cut = int(m.group(1)) if m else None
    s = dict(by=by, secs=secs, n_banked=n_banked, t_lo=t_lo, t_hi=t_hi, n_pred=n_pred, check=check, per_zero=per_zero, scale=scale, rows=rows,
             cut=cut, n_entries=len(comp))
    bad = [x for x, v in (('the main term within tolerance at Q0', check <= TOLERANCE), ('b711`s band seconds read', secs > 0),
                          ('the cut read at data/b711_coeffs.txt :11', cut)) if not v]
    if bad:
        sys.exit('### NOT AS READ: %s -- NOTHING COMPOSED (%r)' % (bad, {k: v for k, v in s.items() if k != 'rows'}))
    return s


def lines(s):
    tier_h = {}
    for r in s['rows']:
        tier_h[r['tier']] = tier_h.get(r['tier'], 0.0) + r['seconds'] / 3600.0
    t1, t2 = tier_h.get('the first tier', 0.0), tier_h.get('the second tier', 0.0)
    tools_h = 1.5
    pairs_h = 1.0
    coeff_h = 0.25
    pin_h = 0.5
    seal_h = 2.5
    budget = t1 + t2 + tools_h + pairs_h + coeff_h + pin_h + seal_h
    L = ['b712 -- (R322)(6): THE PRICE OF THE CLASS-NUMBER-2 CONTROL AT DISCRIMINANT -15 FOR b713; NOTHING COMPUTED OF ITS ZEROS (%s)' % (
        time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### rows are the price`s items: the tools named, the heights proposed, the foreground hours per band, the act budget, the source pin, the',
         '### cut for (iii). Figures read from b711`s banks are cited by path and line; the seat`s estimates are marked THE SEAT`S. The registrations',
         '### this prices: relay data/b712_registrations.txt (committed alone at step zero, 67a02388).', '',
         '  (1) THE TOOLS NAMED FOR b713, each carried from its Q0 form with the form a parameter and its control reproducing Q0 first:',
         '      tools/b713_epstein_certify.py -- b667`s engine (tools/b667_epstein_certify.py), its sqrt(23) of the (1,1,6) expansion (:7-:11, :107,',
         '          :130, :150, :220) made sqrt(D) for the form (1,1,c), D = 4c - 1; Q1 = (1,1,4) at D = 15; the control: Q0 at D = 23 reproducing b711`s',
         '          band counts (data/b711_list.json `bands`) at one band before any -15 band.',
         '      tools/b713_pairs.py -- b709`s band, count, online, candidates, offline and pairs routes (tools/b709_pairs.py :366-:949) over the',
         '          parametrized engine; b675`s representatives (tools/b675_li_bench.py) and b705`s configuration (tools/b705_detection.py) carried.',
         '      tools/b713_coeffs.py -- b711`s coefficient observation in its form over r_Q1(n); its input read equal to the Dirichlet coefficients of',
         '          zeta(s)L(s,chi_-15) + L(s,chi_-3)L(s,chi_5) through the cut (registration (ii) control (C2), tools/b712_genus_control.py`s identity).',
         '',
         '  (2) THE CERTIFIED-LIST HEIGHTS PROPOSED (THE SEAT`S): %s; %s. The route`s height requirement per pair (b709`s T0`, tools/b709_pairs.py' % (
             '[%g, %g] %s' % TIERS[0], '[%g, %g] %s' % TIERS[1]),
         '      _pair_unit :870) is read at b713 from the pair rows before the second tier is entered; at Q0 pair 11 asked T0` > 405.4 and pair 15',
         '      T0` > 442.3 (data/b711_list.txt :17), so a requirement above 200 at -15 is a further act, not this budget.',
         '',
         '  (3) THE FOREGROUND HOURS PER BAND. THE READING: b711`s computed seconds over 325-445 (data/b711_list.json, %d route entries, the derived' % s['n_entries'],
         '      copies not counted): %s ; total %d s for %d zeros, %.2f s per zero. THE CHECK of the main term N(T) = (T/pi) log(T sqrt(D)/(2 pi e))' % (
             ', '.join('%s %d s' % (k, v) for k, v in sorted(s['by'].items())), s['secs'], s['n_banked'], s['per_zero']),
         '      at Q0 (D = 23): N(445) - N(325) = %.1f against the banked %d, off by %.1f per cent (tolerance %d per cent). THE SCALING: the engine`s' % (
             s['n_pred'], s['n_banked'], 100 * s['check'], int(100 * TOLERANCE)),
         '      Bessel truncation M goes as 1/sqrt(D) (tools/b667_epstein_certify.py :107), so the seconds per zero at -15 are taken x %.3f = sqrt(23/15),' % s['scale'],
         '      and not reduced for the lower heights (an upper reading). The bands at -15, 15 height units each:']
    for r in s['rows']:
        L.append('      %-15s band [%6.1f, %6.1f] : zeros (main term, D = 15) %5.1f ; %6.0f s ; %.2f foreground hours' % (
            r['tier'], r['lo'], r['hi'], r['zeros'], r['seconds'], r['seconds'] / 3600.0))
    L += ['      the first tier %.2f hours ; the second tier %.2f hours.' % (t1, t2), '',
          '  (4) THE ACT BUDGET (THE SEAT`S ESTIMATE): the list %.2f + %.2f h (the two tiers); the tools ported with their Q0 controls %.1f h; the pairs`' % (t1, t2, tools_h),
          '      predictions and n* %.1f h; the coefficient observation %.2f h; the source pin %.1f h; the corrigendum, record lines, seal, suite in seven' % (pairs_h, coeff_h, pin_h),
          '      parts, root, mirror and closing %.1f h (b711`s order) -- about %.1f foreground hours, for the author`s reading against one act`s' % (seal_h, budget),
          '      budget ((R322)(11)); it holds where the route asks no height above 200, and where it asks more the list beyond 200 is priced at the',
          '      act that reads the requirement. The list`s hours are an upper reading from b711`s seconds; the other items are the seat`s.', '',
          '  (5) THE SOURCE PIN FOR b713 (THE SEAT`S; NO SEARCH THIS ACT, the author`s word at prompt 1): one text stating the genus decomposition of',
          '      registration (i) for the forms of discriminant -15 -- Z_Q1 + Z_Q2 = 2 zeta L(chi_-15) and Z_Q1 - Z_Q2 = 2 L(chi_-3) L(chi_5) -- fetched',
          '      once, its sha256 and size banked, the statement quoted with its page or line, read against (i) before any -15 band; a statement not',
          '      found is banked as ABSENT with its control (a second query shape), and (i) stands on the author`s word with its control as',
          '      data/b712_genus_control.txt banks it. Priced at %.1f h, inside (4).' % pin_h, '',
          '  (6) THE CUT FOR (iii): n <= %d, b711`s cut (data/b711_coeffs.txt :11, e^{10.39} as data/b710_registrations.txt :72 fixed it), so' % s['cut'],
          '      the -15 observation stands at the same cut as Q0`s; the onset rung of b710`s reading is a Q0 object and is not carried.', '',
          '### ### **TIERS 2 ([0, 100], [100, 200]) ; FIRST TIER %.2f h, SECOND %.2f h ; THE SEAT`S ACT BUDGET ABOUT %.1f FOREGROUND HOURS WHERE NO PAIR' % (t1, t2, budget),
          '### ASKS ABOVE 200 ; THE MAIN TERM CHECKED AT Q0 (%.1f PER CENT) ; THE CUT %d ; NOTHING OF THE -15 ZEROS COMPUTED.**' % (100 * s['check'], s['cut'])]
    return L, dict(t1=t1, t2=t2, budget=budget)


def main(route):
    s = compose()
    L, tot = lines(s)
    if route == 'dry':
        print(NL.join(L))
        return
    import act_membrane as MEM
    import b712_record as REC
    for name, data in (('b712_price.txt', NL.join(L) + NL),
                       ('b712_price.json', json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), by=s['by'], seconds=s['secs'],
                                                           zeros_banked=s['n_banked'], main_term=s['n_pred'], check=s['check'], per_zero=s['per_zero'],
                                                           scale=s['scale'], rows=s['rows'], cut=s['cut'], **tot), indent=1) + NL)):
        p = os.path.join(D, name)
        MEM.guard_path('b712', p, REC.R.ROOT_EXCLUDE)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(data.encode('utf-8'))
        os.replace(p + '.tmp', p)
    print(L[-2])
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'bank'):
        print('usage: b712_price.py dry | bank')
        sys.exit(2)
    main(r)
