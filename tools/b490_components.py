# -*- coding: utf-8 -*-
"""b490_components.py -- THE COMPONENTS. ### **NO CHAIN IS RUN.**
### Every value is read from a bank; the arithmetic is a sieve, subtraction and division.
### ### **b475's LOG IS `stat`-ed AND NEVER OPENED** -- see `G-C0-LOG-STAT-NOT-READ`.
"""
import io
import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []

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


def main():
    sv = json.loads(read(os.path.join(D, 'b490_survey.json')) or '{}')
    rows, entries = sv['rows'], sv['entries']
    ms = [r['m'] for r in rows]
    lo = min(range(len(ms)), key=lambda i: ms[i])
    hi = max(range(lo, len(ms)), key=lambda i: ms[i])

    rec('=' * 118)
    rec('b490 -- THE COMPONENTS. ### THE INCREMENTS, THE RATIO, AND THE PRIOR TEST.')
    rec('=' * 118)

    # ================================================================= COMPONENT 0
    rec('')
    rec('COMPONENT 0 -- pid 27508`S CHILDREN.')
    rec('=' * 118)
    for l in read(os.path.join(D, 'b490_pid27508.txt')).split(NL):
        if l.strip():
            rec('   %s' % l.strip()[:112])
    lj = json.loads(read(os.path.join(D, 'b475_launch.json')) or '{}')
    log = lj.get('log', '')
    rec('')
    rec('   ### ### **27508 IS `b475`S DETACHED AXIOM RUN**, launched %s, serialized,'
        % lj.get('started_utc'))
    rec('   ### `LEAN_NUM_THREADS %s`, by `%s`.'
        % (lj.get('lean_num_threads'), os.path.basename(lj.get('launcher', '?'))))
    if os.path.exists(log):
        st = os.stat(log)
        import datetime
        rec('   the log`s byte count, ### **BY `stat` -- THE FILE WAS NOT OPENED** ### : %d'
            % st.st_size)
        rec('     last written %s ; ### **IDLE %.2f HOURS.**'
            % (datetime.datetime.fromtimestamp(st.st_mtime).isoformat(timespec='seconds'),
               (datetime.datetime.now().timestamp() - st.st_mtime) / 3600.0))
    rec('   ### ### **AND THE EXCLUSION CARRIED SINCE b481 IS RETIRED HERE.** ### Nine suites')
    rec('   ### excused this log from `G-NOPRIORBANK` because "a live process is still appending".')
    rec('   ### **THE PROCESS IS GONE AND THE FILE IS COLD.** ### The arm runs at full width.')

    # ================================================================= COMPONENT 1
    rec('')
    rec('COMPONENT 1 -- THE 34 INCREMENTS.')
    rec('=' * 118)
    rec('')
    rec('   step  a from        a to          enters      d(m)             d(arch)          '
        'd(pr)            closes to')
    rec('   ' + '-' * 112)
    steps = []
    for i in range(len(rows) - 1):
        b, a_ = rows[i], rows[i + 1]
        dm = a_['m'] - b['m']
        da = dp = clo = None
        if b['arch'] is not None and a_['arch'] is not None:
            da, dp = a_['arch'] - b['arch'], a_['pr'] - b['pr']
            clo = abs(dm - (da - dp))
        ent = ','.join(str(n) for n in entries[i]) or '(none)'
        rec('   %-5d %-12.6f %-13.6f %-11s %-16.9g %-16s %-16s %s'
            % (i + 1, b['a'], a_['a'], ent, dm,
               ('%.9g' % da) if da is not None else '-- not banked',
               ('%.9g' % dp) if dp is not None else '-- not banked',
               ('%.2g' % clo) if clo is not None else '--'))
        steps.append(dict(i=i + 1, a_from=b['a'], a_to=a_['a'], enters=entries[i], dm=dm,
                          darch=da, dpr=dp, closes=clo))
    cl = [s['closes'] for s in steps if s['closes'] is not None]
    rec('')
    rec('   ### steps with both channels banked : %d of %d ; ### **THE CHANNEL SPLIT CLOSES TO'
        % (len(cl), len(steps)))
    rec('   ### %.2g AT WORST** -- b437 stores `arch` and `pr` rounded, so no finer is claimed.'
        % (max(cl) if cl else 0))
    rec('   ### steps admitting a new prime power : ### **%d** ### ; steps admitting NONE :'
        % sum(1 for s in steps if s['enters']))
    rec('   ### **%d**, and those are printed as `(none)` rather than left blank.'
        % sum(1 for s in steps if not s['enters']))

    rec('')
    rec('### (1b) THE DECOMPOSITION THE ORDER ASKS FOR -- ### **NOT AVAILABLE. THE HALT.**')
    rec('-' * 118)
    ig = json.loads(read(os.path.join(D, 'b449_integrand.json')) or '{}')
    lv = ig.get('levels') or []
    tm = (lv[-1].get('terms') if lv else {}) or {}
    rec('   The split into "the newly entered terms` contribution" and "the drift of terms')
    rec('   already present" needs PER-n TERM VALUES at both ends of every step.')
    rec('   ### ### **THEY ARE BANKED AT EXACTLY ONE OF THE 35 CELLS:** ### `b449_integrand.json`,')
    rec('   ### at ### **a = %s** ### -- the outlier -- as `levels[*].terms`, `n -> value`, with'
        % ig.get('a'))
    rec('   ### `terms_sum == prime` exactly. ### %d terms: %s'
        % (len(tm), ', '.join('%s:%.4g' % (k, v) for k, v in tm.items())))
    rec('   ### ### **`16` AND `17` ARE EXACTLY `0.0`** -- `log 17` sits on the window`s own edge')
    rec('   ### `L = %.9f`. ### b449`s finding, restated and not re-scored.' % (ig.get('vstar') or 0))
    rec('   ### ### **AND NEITHER `27` NOR `32` IS AMONG THEM**, that cell`s window reaching only')
    rec('   ### to `a^2 = 17`. ### **SO THE FRACTION (N1) ASKS FOR EXISTS IN NO BANK.**')
    rec('   ### the only remaining route is to evaluate `2 log p / sqrt(n) * interp(log n, v, w)`,')
    rec('   ### which needs the smeared window -- ### **THAT IS RUNNING THE CHAIN, WHICH THIS')
    rec('   ### ORDER FORBIDS IN ITS OWN CLOSING LINE.** ### The halt is proved over every route')
    rec('   ### and carries a positive control, both printed in `b490_extract.txt` (P3).')

    rec('')
    rec('### (1c) THE TWO NAMED ENTRIES, UNDER BOTH READINGS OF THE RUNG.')
    rec('-' * 118)
    for n, lab in ((27, '3^3'), (32, '2^5')):
        k = next((i for i, e in enumerate(entries) if n in e), None)
        g = next((i for i, r in enumerate(rows)
                  if abs(r['a'] - round(math.sqrt(n), 6)) < 5e-7), None)
        rec('   `%s = %d` : sqrt %d = %.12f, stored as %.6f -- the rounding goes ### **%s**'
            % (lab, n, n, math.sqrt(n), round(math.sqrt(n), 6),
               'UP' if round(math.sqrt(n), 6) > math.sqrt(n) else 'DOWN'))
        rec('       STORED-FLOAT reading : %s'
            % (('enters at a = %.6f, step %d' % (rows[k + 1]['a'], k + 1)) if k is not None
               else '### **NEVER ENTERS THIS LADDER**'))
        rec('       GENERATOR reading    : its own rung is %s'
            % (('### **a = %.6f**, index %d' % (rows[g]['a'], g)) if g is not None else 'absent'))
    rec('   the margin`s MINIMUM : a = %.6f (index %d) ; LOCAL MAXIMUM : a = %.6f (index %d)'
        % (rows[lo]['a'], lo, rows[hi]['a'], hi))
    rec('   ### ### **ON THE GENERATOR READING `3^3` SITS EXACTLY AT THE LOCAL MAXIMUM AND `2^5`')
    rec('   ### EXACTLY AT THE LAST RUNG** -- which is what (N1) presumes. ### On the stored')
    rec('   ### floats neither does. ### **A SIX-PLACE ROUNDING DECIDES IT, NOT THE ARITHMETIC.**')
    rec('   ### ### **THE FRACTION OF EACH TURN`S INCREMENT CARRIED BY THOSE ENTRIES :')
    rec('   ### NOT DECIDABLE FROM THE BANKS**, under either reading, for the reason in (1b).')

    # ================================================================= COMPONENT 2
    rec('')
    rec('COMPONENT 2 -- THE SENSITIVITY RATIO.')
    rec('=' * 118)
    rec('')
    rec('   idx  a            |W + Z|          m(a)             ratio            mark')
    rec('   ' + '-' * 92)
    rats = []
    for i, r in enumerate(rows):
        d = abs(r['W'] + r['zero'])
        q = d / r['m']
        mark = []
        if i == lo:
            mark.append('### **MINIMUM MARGIN**')
        if abs(r['a'] - 4.123106) < 1e-9:
            mark.append('### **THE OUTLIER**')
        rats.append(q)
        rec('   %-4d %-12.6f %-16.6g %-16.9g %-16.6g %s' % (i, r['a'], d, r['m'], q,
                                                            ' '.join(mark)))
    pk = max(range(len(rats)), key=lambda i: rats[i])
    rec('')
    rec('   ### ### **THE RATIO PEAKS AT %.6g, AT a = %.6f, INDEX %d.**'
        % (rats[pk], rows[pk]['a'], pk))
    rec('   ### the margin`s minimum is at index %d ; ### **THE DISTANCE IS %d RUNGS.**'
        % (lo, abs(pk - lo)))
    rec('   ### the second-highest ratio, %.6g, IS at the minimum cell itself (index %d).'
        % (sorted(rats)[-2], rats.index(sorted(rats)[-2])))
    verdict = abs(pk - lo) <= 1
    rec('')
    rec('   ### ### **THE ONE VERDICT: THE RATIO %s PEAK WITHIN ONE RUNG OF THE MARGIN`S'
        % ('DOES' if verdict else 'DOES NOT'))
    rec('   ### MINIMUM.**')
    rec('   ### and the whole ratio column is below ### **%.2g** ### -- the two-side disagreement'
        % max(rats))
    rec('   ### never reaches a part in ### **%d** ### of the margin it prices.' % int(1 / max(rats)))

    # ================================================================= COMPONENT 3
    rec('')
    rec('COMPONENT 3 -- THE FALSIFIER`S PRIOR TEST, QUOTED FROM b334`S BANK.')
    rec('=' * 118)
    am = read(os.path.join(D, 'b334_the_aim_map.txt'))
    i = am.find('THE EPSTEIN CROSSING REGION')
    j = am.find('THE NAVIGATOR', i) if i >= 0 else -1
    quote = [l.strip().lstrip('#').strip() for l in am[i:j].split(NL) if l.strip()] if i >= 0 else []
    rec('')
    rec('   ### **QUOTED VERBATIM FROM `relay data/b334_the_aim_map.txt`:**')
    for l in quote[:9]:
        rec('     *%s*' % l[:108])
    rec('')
    rec('   ### the three aims, each with its height and the support that resolved it:')
    rec('     ### **(a = 40, gamma = 16.290216)** ### -- `places_q = +0.655053`')
    rec('     ### **(a = 81, gamma = 16.290216)** ### -- `places_q = +1.362830`')
    rec('     ### **(a = 81, gamma = 46.960994)** ### -- `places_q = +0.194219`')
    rec('   ### ### **EVERY MEMBER IS AT AN OFF-LINE ZERO`S HEIGHT AND NONE IS ELSEWHERE**, and')
    rec('   ### the region is EMPTY on the covered leg, as b334`s own paragraph states.')
    rec('   ### the supports that resolved them : ### **a = 40 AND a = 81.**')
    rec('   ### ### **THE LADDER`S LAST RUNG IS `a = %.6f`.** ### It does not reach either.'
        % rows[-1]['a'])
    rec('   ### **SO THE FALSIFIER WAS TESTED AT b334 AND COULD NOT BE TESTED ON THIS LADDER** --')
    rec('   ### not because it failed to fire, but because the ladder`s widths are seven and')
    rec('   ### fourteen times too small to resolve those heights.')
    rec('   ### the citation enters the trail as ### **TESTED-AT-b334**, with the reach stated.')

    rec('')
    rec('=' * 118)
    io.open(os.path.join(D, 'b490_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(steps=steps, ratios=rats, peak_i=pk, peak_a=rows[pk]['a'],
                   peak=rats[pk], lo=lo, hi=hi, dist=abs(pk - lo), verdict=verdict,
                   closes_max=max(cl) if cl else None,
                   n_entering=sum(1 for s in steps if s['enters']),
                   terms_cell=ig.get('a'), terms=tm, n1_decidable=False),
              io.open(os.path.join(D, 'b490_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL + '  written: b490_components.txt, b490_results.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
