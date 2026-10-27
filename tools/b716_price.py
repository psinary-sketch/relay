# -*- coding: utf-8 -*-
"""b716_price.py -- (R326)(4)(iv): THE PRICE OF THE -39 COMPUTATION FOR b717, NOTHING OF -39 COMPUTED. Writes data/b716_price.txt.

Every figure is read from b713's banks of the -15 run (the run b712's price was read against) or computed from the main term; the
seat's estimates are marked THE SEAT'S. Read: b713's list bank (data/b713_list.json, its bands' N), its unit files
(data/b713_list_units_band_*.jsonl, each row's `seconds`, the rows `derived_from` another not counted, the control23 bands apart), its
onset units (data/b713_onsets_units.jsonl), its onsets bank (data/b713_onsets.txt, each pair's reach), its step bank (the act's wall
clock), and the coefficients' cut (data/b713_coeffs.json `cut`). Nothing at -39 is computed: no zero, no coefficient, no onset.

  python -X utf8 tools/b716_price.py          writes data/b716_price.txt and prints its foot
"""
import glob
import json
import math
import os
import re
import sys
import time
from datetime import datetime

RELAY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(RELAY, 'data')
NL = '\n'
DQ_PREV, DQ = 15, 39


def jl(name):
    with open(os.path.join(D, name), encoding='utf-8') as f:
        return json.load(f)


def rows(path):
    out = []
    for l in open(path, encoding='utf-8'):
        l = l.strip()
        if l:
            try:
                out.append(json.loads(l))
            except ValueError:
                pass
    return out


def main_term(T, d):
    """N(T) ~ (T/pi) log(T sqrt(d)/(2 pi e)) + 1, the main term b713's list bank reads beside its count (data/b713_list.txt :8)."""
    return (T / math.pi) * math.log(T * math.sqrt(d) / (2 * math.pi * math.e)) + 1 if T > 0 else 0.0


def band_zeros(lo, hi, d):
    return max(0.0, main_term(hi, d) - main_term(max(lo, 1.0), d))


def main():
    lst = jl('b713_list.json')
    bands = lst['bands']
    zeros_prev = sum(b['N'] for b in bands)
    files = [p for p in sorted(glob.glob(os.path.join(D, 'b713_list_units_band_*.jsonl'))) if 'control23' not in p]
    per_file, secs = [], 0
    for p in files:
        rs = rows(p)
        s = sum(int(r.get('seconds') or 0) for r in rs if not r.get('derived_from'))
        per_file.append((os.path.basename(p), len(rs), s))
        secs += s
    base_s = int((lst.get('base') or {}).get('seconds') or 0)
    on_rows = rows(os.path.join(D, 'b713_onsets_units.jsonl')) if os.path.isfile(os.path.join(D, 'b713_onsets_units.jsonl')) else []
    on_s = sum(int(r.get('seconds') or 0) for r in on_rows if not r.get('derived_from'))
    ons = open(os.path.join(D, 'b713_onsets.txt'), encoding='utf-8').read()
    held = re.findall(r'^  pair\s+(\d+) \| rho [\d.]+ \+ ([\d.]+) i \| n\* \d+', ons, re.M)
    beyond = [(int(a), float(b)) for a, b in re.findall(r'^  pair\s+(\d+) \| BEYOND REACH at T0` \d+ \(needs > ([\d.]+)\)', ons, re.M)]
    steps = jl('b713_steps.json')['rows']
    ats = [datetime.strptime(r['at'], '%Y-%m-%dT%H:%M:%SZ') for r in steps if r.get('at')]
    wall = (max(ats) - min(ats)).total_seconds() / 3600 if ats else None
    cut = jl('b713_coeffs.json').get('cut')
    # the base region's units are a fixed cost (no zero in it); the bands' seconds per unit height, measured, by the band file's edges
    base_file = [s for n, _r, s in per_file if n.endswith('_base.jsonl')]
    base_units = base_file[0] if base_file else 0
    dens = []
    for n, _r, s in per_file:
        m = re.match(r'b713_list_units_band_([\d.]+)_([\d.]+)\.jsonl$', n)
        if m:
            dens.append((float(m.group(1)), float(m.group(2)), s / (float(m.group(2)) - float(m.group(1)))))
    dens.sort()
    top_prev = max(h for _l, h, _d in dens)

    def measured(lo, hi):
        """-15's measured seconds over [lo, hi], by the bands' densities; above -15's top, the last band's density (an extrapolation)."""
        s = 0.0
        for a, b, d in dens:
            s += max(0.0, min(hi, b) - max(lo, a)) * d
        if hi > top_prev:
            s += (hi - max(lo, top_prev)) * dens[-1][2]
        return s
    band_secs = secs - base_units
    spz = band_secs / zeros_prev
    scale = math.sqrt(DQ_PREV / DQ)
    tiers = [('the first tier', [(0, 15), (15, 30), (30, 45), (45, 60), (60, 75), (75, 90), (90, 100)]),
             ('the second tier', [(100, 115), (115, 130), (130, 145), (145, 160), (160, 175), (175, 190), (190, 200)]),
             ('the third tier', [(200, 215), (215, 230), (230, 245), (245, 260), (260, 275), (275, 290), (290, 300)])]
    L = ['b716 -- (R326)(4)(iv): THE PRICE OF THE -39 COMPUTATION FOR b717; NOTHING OF -39 COMPUTED (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### rows are the price`s items: the tools named, the certified list`s tiers, the foreground hours per band, the coefficients` cut, the',
         '### act budget. Figures read from b713`s banks of the -15 run are cited by path; the seat`s estimates are marked THE SEAT`S. The',
         '### registrations this prices: relay data/b716_registrations.txt (committed alone at step zero, dc5e808f). Written by tools/b716_price.py.', '',
         '  (1) THE TOOLS NAMED FOR b717, each carried from its -15 form with the form a parameter and its control reproducing -15 first:',
         '      the certify engine and band route of b713 (tools/b713_epstein_certify.py, tools/b713_pairs.py, b667`s engine made sqrt(D) for the',
         '      form (1,1,c), D = 4c - 1) at c = 10, D = 39 = 4 . 10 - 1, Q1 = x^2 + xy + 10y^2; the coefficient route of b713 (tools/b713_coeffs.py)',
         '      over r_Q1(n), its input read equal to the three lines of registration (i) through the cut (data/b716_genus_control.txt); the onset',
         '      route of b713 for (iii). Each control first: -15`s band counts, -15`s eight pairs at b713`s ratios, -15`s least index 24 and Q0`s 48.',
         '',
         '  (2) THE MEASURED SECONDS AT -15 (b713`s run): the list`s %d unit files (control23 apart), every row`s `seconds` summed with the rows' % len(files),
         '      derived from another not counted -- %d s, of which the base region`s units %d s (a fixed cost, no zero in it; data/b713_list.json' % (
             secs, base_units),
         '      `base` records %d s for its own count) and the bands` %d s for %d zeros (the bands` N) -- %.2f s per zero on average, rising with' % (
             base_s, band_secs, zeros_prev, spz),
         '      height (per file below: the bands under 100 ran 70 to 303 s, the bands over 145 ran 598 to 1396 s).']
    L += ['        %-48s rows %4d ; seconds %5d' % f for f in per_file]
    L += ['      the onsets (data/b713_onsets_units.jsonl): rows %d, seconds %d, for %d pairs computed (data/b713_onsets.txt) ; the coefficients'
          ' to the cut %s: one foreground call, the bank at 01:21:09Z after the onsets` at 01:19:29Z (data/b713_coeffs.json, data/b713_onsets.txt :1).' % (
              len(on_rows), on_s, len(held), cut),
          '      b712`s price read b711`s Q0 seconds at 15.06 s per zero taken x 1.238 for -15 (data/b712_price.txt :21-:24): 18.6 s per zero;'
          ' the -15 run measured %.2f s per zero.' % spz, '']
    L += ['  (3) THE CERTIFIED LIST`S TIERS AND THE FOREGROUND HOURS PER BAND AT -39 (THE SEAT`S READING): zeros by the main term at D = 39; seconds',
          '      THE UPPER READING: -15`s measured seconds over the same heights (the band files` seconds per unit height) x the zeros` ratio',
          '      N39/N15 of the band; THE LOWER: that x sqrt(15/39) = %.3f (the engine`s Bessel truncation M as 1/sqrt(D),' % scale,
          '      tools/b667_epstein_certify.py :107, as b712 read it). Above -15`s top (%.1f) the last band`s density is carried, an' % top_prev,
          '      EXTRAPOLATION. A band over 600 s is split into calls under it; the base region once, %d s at -15 (fixed).' % base_units]
    tot = {}
    for name, bs in tiers:
        hu = hl = 0.0
        for lo, hi in bs:
            z = band_zeros(lo, hi, DQ)
            z15 = band_zeros(lo, hi, DQ_PREV)
            su = measured(lo, hi) * (z / z15 if z15 else 1.0)
            sl = su * scale
            hu, hl = hu + su, hl + sl
            L.append('      %-15s band [%6.1f, %6.1f] : zeros (main term, D = 39) %5.1f (D = 15: %5.1f) ; %5.0f s upper, %5.0f s lower%s' % (
                name, lo, hi, z, band_zeros(lo, hi, DQ_PREV), su, sl, ' ### OVER 600 s: SPLIT' if su > 600 else ''))
        tot[name] = (hu / 3600, hl / 3600)
    L.append('      %s' % ' ; '.join('%s %.2f h upper, %.2f h lower' % (n, u, l) for n, (u, l) in tot.items()))
    L += ['      THE CHECK of the main term at -15 against b713`s list: N(199.33082) at D = 15 reads %.1f ; the list holds %d (data/b713_list.txt :8).' % (
        main_term(199.33082, DQ_PREV), zeros_prev + 0), '',
          '  (4) THE REACH OF (iii)`s PAIRS: at -15 a list to T0` 199 reached %d of the %d pairs (heights %s), every pair above 65 asking more:' % (
              len(held), len(held) + len(beyond), ', '.join(h for _p, h in held)),
          '      the next asked %s. THE SEAT`S READING for -39: the first two tiers, [0, 200], reach the pairs whose requirement is below 200;' % (
              ', '.join('pair %d > %.1f' % b for b in sorted(beyond, key=lambda x: x[1])[:5])),
          '      the third tier, [200, 300], is priced for the author`s word, to be entered only where b717`s pair rows ask it. No -39 pair is',
          '      known at b716; their count and heights are b717`s first figures.', '',
          '  (5) THE COEFFICIENTS` CUT FOR (ii): n <= %s, b711`s and b713`s cut (data/b713_coeffs.json `cut`), so the least negative index at' % cut,
          '      -39 is read at the cut Q0`s 48 and -15`s 24 were read at; a least index above the cut is reported as none found to the cut.', '']
    hours_list = tot['the first tier'][0] + tot['the second tier'][0] + base_units / 3600
    L += ['  (5b) b713`s ACT, MEASURED: its step rows run %.1f h from its first to its last (data/b713_steps.json), the -15 list, predictions,' % (wall or 0),
          '      onsets and coefficients inside it.', '',
          '  (6) THE ACT BUDGET (THE SEAT`S ESTIMATE): the list`s base and first two tiers %.2f h (upper); the tools ported with their -15 controls 1.5 h;' % hours_list,
          '      the predictions and n* 1.0 h; the coefficients 0.25 h; the corrigendum, record lines, seal, suite in seven parts, root, mirror',
          '      and closing 2.5 h -- about %.1f foreground hours, inside one act where no pair asks above 200; the third tier adds %.2f h (upper)' % (
              hours_list + 5.25, tot['the third tier'][0]),
          '      where b717`s pair rows ask it.', '',
          '### ### **TIERS 3 ([0, 100], [100, 200], [200, 300] FOR THE AUTHOR) ; THE -15 BANDS` RATE %.2f s PER ZERO MEASURED, RISING WITH HEIGHT ;'
          ' BASE AND FIRST TWO TIERS %.2f h UPPER, %.2f h LOWER ; THE CUT %s ; THE SEAT`S ACT BUDGET ABOUT %.1f FOREGROUND HOURS ; NOTHING OF -39 COMPUTED.**' % (
              spz, hours_list, tot['the first tier'][1] + tot['the second tier'][1] + base_units / 3600, cut, hours_list + 5.25)]
    p = os.path.join(D, 'b716_price.txt')
    with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        f.write(NL.join(L) + NL)
    os.replace(p + '.tmp', p)
    print('bank', p)
    print(L[-1])
    return 0


if __name__ == '__main__':
    sys.exit(main())
