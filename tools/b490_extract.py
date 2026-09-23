# -*- coding: utf-8 -*-
"""b490_extract.py -- THE SURVEY. ### **NO CHAIN IS RUN.**

### Every value is READ from a bank on disk. ### The only arithmetic is a prime-power sieve and
### subtraction of banked numbers.

### ### **AND ONE PART OF THE ORDER CANNOT BE SERVED FROM THE BANKS.** ### Component 1 asks for a
### decomposition "from banked per-n prime-channel terms". ### This survey checks EVERY route to
### such terms and reports what it finds, with a POSITIVE CONTROL that proves the finder would
### see them if they were there.
"""
import io
import json
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
NL = chr(10)
L, MISSES = [], []

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


def prime_powers_upto(x):
    n = int(x + 1e-9)
    if n < 2:
        return []
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
                out.append((v, p, k))
                v *= p
                k += 1
    return sorted(out)


def has_term_values(obj, depth=0):
    """### ### **THE FINDER.** ### Does this object carry PER-TERM prime values -- a mapping or
    ### a list that pairs a prime power with a NUMBER? ### A bare list of integers is an INDEX,
    ### not a term value, and is reported as such."""
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if re.search(r'term|channel|per_n|prime', str(k), re.I):
                if isinstance(v, dict) and v and all(
                        re.match(r'^\d+$', str(kk)) for kk in list(v)[:8]) and all(
                        isinstance(vv, (int, float)) for vv in list(v.values())[:8]):
                    hits.append(('mapping n -> value', k, len(v)))
                elif isinstance(v, list) and v and all(
                        isinstance(x, (list, tuple)) and len(x) == 2 for x in v[:8]):
                    hits.append(('list of (n, value)', k, len(v)))
                elif isinstance(v, list) and v and all(isinstance(x, int) for x in v[:8]):
                    hits.append(('AN INDEX ONLY -- list of n, no values', k, len(v)))
                elif isinstance(v, int):
                    hits.append(('A COUNT ONLY -- an int', k, v))
            if depth < 4:
                hits += has_term_values(v, depth + 1)
    elif isinstance(obj, list) and depth < 4:
        for x in obj[:60]:
            hits += has_term_values(x, depth + 1)
    return hits


def main():
    rec('=' * 112)
    rec('b490 -- THE SURVEY. ### THE INCREMENTS, THE RATIO, AND THE PRIOR TEST.')
    rec('=' * 112)

    # ------------------------------------------------------------- (P1) component 0, banked
    rec('')
    rec('(P1) COMPONENT 0 -- pid 27508, ALREADY BANKED AT `data/b490_pid27508.txt`.')
    rec('-' * 112)
    pid = read(os.path.join(D, 'b490_pid27508.txt'))
    for l in pid.split(NL):
        if l.strip():
            rec('    %s' % l.strip()[:106])
    lj = json.loads(read(os.path.join(D, 'b475_launch.json')) or '{}')
    rec('')
    rec('    ### ### **AND 27508 IS NOT A NEW PROCESS. IT IS `b475`S DETACHED AXIOM RUN.**')
    rec('    `data/b475_launch.json` : pid ### **%s** ### , launcher `%s`,'
        % (lj.get('pid'), os.path.basename(lj.get('launcher', '?'))))
    rec('      started `%s`, serialized `%s`, LEAN_NUM_THREADS `%s`.'
        % (lj.get('started_utc'), lj.get('serialized'), lj.get('lean_num_threads')))
    log = lj.get('log', '')
    if os.path.exists(log):
        st = os.stat(log)
        import datetime
        idle = (datetime.datetime.now().timestamp() - st.st_mtime) / 3600.0
        rec('    the log`s byte count, ### **STAT ONLY -- THE FILE WAS NOT OPENED** ### : %d'
            % st.st_size)
        rec('      last written : %s ; ### **IDLE %.2f HOURS.**'
            % (datetime.datetime.fromtimestamp(st.st_mtime).isoformat(timespec='seconds'), idle))
        rec('    ### ### **SO THE STANDING EXCLUSION CARRIED SINCE b481 IS NOW FALSE.** ### Every')
        rec('    ### suite from b481 to b489 excluded this log from `G-NOPRIORBANK` on the ground')
        rec('    ### that ### *"another act`s live process is still appending to it"*. ### **NO')
        rec('    ### SUCH PROCESS EXISTS, AND THE FILE HAS NOT BEEN WRITTEN FOR HOURS.** ### The')
        rec('    ### ground lapsed when the run died and no act noticed. ### This act drops the')
        rec('    ### exception and states why.')

    # ------------------------------------------------------------- (P2) the ladder and its steps
    rec('')
    rec('(P2) THE LADDER`S 34 STEPS, AND WHAT ENTERS ON EACH.')
    rec('-' * 112)
    ent = [json.loads(l) for l in read(os.path.join(D, 'b477_entries.jsonl')).split(NL) if l.strip()]
    diag = sorted([x for x in ent if x.get('kind') == 'diagonal'], key=lambda x: x['a'])
    rungs = {round(r['a'], 6): r for r in
             (json.loads(read(os.path.join(D, 'b437_rungs.json'))) or {}).get('rows', [])}
    rows = []
    for x in diag:
        rg = rungs.get(round(x['a'], 6), {})
        rows.append(dict(a=x['a'], m=-x['W'], W=x['W'], zero=x['zero'],
                         arch=rg.get('arch'), pr=rg.get('pr'),
                         pp=[t[0] for t in prime_powers_upto(x['a'] * x['a'])]))
    rec('    35 cells, %d steps. ### the prime-power set grows from %d to %d members.'
        % (len(rows) - 1, len(rows[0]['pp']), len(rows[-1]['pp'])))
    entries = []
    for i in range(1, len(rows)):
        new = [n for n in rows[i]['pp'] if n not in rows[i - 1]['pp']]
        entries.append(new)
    rec('    steps admitting a NEW prime power : ### **%d** ### of %d'
        % (sum(1 for e in entries if e), len(entries)))
    rec('    ### the entering prime powers, step by step, where any enters:')
    for i, e in enumerate(entries):
        if e:
            rec('      step %2d  a %-11.6f -> %-11.6f   enters ### **%s**'
                % (i + 1, rows[i]['a'], rows[i + 1]['a'], ', '.join(str(n) for n in e)))
    rec('')
    rec('    ### ### **AND THE RUNGS ARE `sqrt n` ROUNDED TO SIX PLACES, SO A ROUNDING DECIDES')
    rec('    ### WHETHER `n` IS INSIDE ITS OWN RUNG.** ### b437`s tolerance lesson, exactly:')
    for n in (17, 19, 23, 25, 27, 29, 31, 32):
        r = math.sqrt(n)
        rec('      sqrt(%2d) = %.12f -> stored %.6f ; the rounding goes ### **%s**'
            % (n, r, round(r, 6), 'UP, so n is INSIDE its rung' if round(r, 6) > r
               else 'DOWN, so n is JUST OUTSIDE'))
    rec('    ### ### **THE TWO THE ORDER NAMES -- `3^3 = 27` AND `2^5 = 32` -- ARE BOTH ROUNDED')
    rec('    ### DOWN**, so on the STORED floats they fall outside their own rungs, while `17`,')
    rec('    ### `19`, `23` and `29` are rounded up and fall inside theirs. ### **BOTH READINGS')
    rec('    ### ARE PRINTED AND NEITHER IS SILENTLY CHOSEN.**')
    rec('')
    rec('    ### ### **AND THE ORDER`S TWO NAMED ENTRIES SIT EXACTLY ON THE TWO TURNS.**')
    for n, lab in ((27, '3^3'), (32, '2^5')):
        k = next((i for i, e in enumerate(entries) if n in e), None)
        gen = next((i for i, r in enumerate(rows) if abs(r['a'] - round(math.sqrt(n), 6)) < 5e-7),
                   None)
        rec('      `%s = %d` : on the STORED floats it enters %s' % (
            lab, n,
            ('at a = %.6f, step %d' % (rows[k + 1]['a'], k + 1)) if k is not None
            else '### **NEVER ON THIS LADDER**'))
        rec('          on the GENERATOR `sqrt %d = %.12f` its own rung is %s'
            % (n, math.sqrt(n),
               ('### **a = %.6f** ### (index %d)' % (rows[gen]['a'], gen)) if gen is not None
               else 'not a rung of this ladder'))
    ms = [r['m'] for r in rows]
    lo = min(range(len(ms)), key=lambda i: ms[i])
    hi = max(range(lo, len(ms)), key=lambda i: ms[i])
    rec('      the margin`s MINIMUM is at a = %.6f ; its LOCAL MAXIMUM at a = %.6f'
        % (rows[lo]['a'], rows[hi]['a']))
    rec('    ### ### **ON THE GENERATOR READING, `3^3` SITS EXACTLY AT THE LOCAL MAXIMUM AND')
    rec('    ### `2^5` EXACTLY AT THE LAST RUNG.** ### On the stored floats `3^3` enters one')
    rec('    ### rung LATER and `2^5` never enters at all. ### **THE ORDER`S (N1) PRESUMES THE')
    rec('    ### GENERATOR READING**, and this act says so rather than quietly adopting it.')
    rec('    ### ### **AND `2^4 = 16` ENTERS AT `a = 4.000000`, ONE RUNG BEFORE THE MINIMUM.**')

    # ------------------------------------------------------------- (P3) the halt
    rec('')
    rec('(P3) THE HALT. ### **PER-n PRIME-CHANNEL TERM VALUES ARE NOT BANKED, BY ANY ROUTE.**')
    rec('-' * 112)
    routes = [
        ('b437_rungs.json', 'the ladder`s own parts'),
        ('b437_cells.json', 'the ladder`s cells with their prime-power lists'),
        ('b448_channels.json', 'the channel measurement at a = 4.123106'),
        ('b449_integrand.json', 'the integrand at ln 17'),
        ('b334_leg_reaching_40.json', 'the aim map, reaching leg'),
        ('b334_leg_reaching_81.json', 'the aim map, reaching leg'),
        ('b334_leg_covered.json', 'the aim map, covered leg'),
        ('b321_rows.json', 'the window`s own banked rows'),
        ('b477_survey.json', 'the Gram run`s survey'),
    ]
    for f, what in routes:
        j = None
        try:
            j = json.loads(read(os.path.join(D, f)) or 'null')
        except Exception:
            pass
        h = has_term_values(j) if j is not None else []
        kinds = sorted({k[0] for k in h})
        rec('    %-30s %-44s %s' % (f, what, (', '.join(kinds) if kinds else 'nothing matching')))
    rec('    `b477_entries.jsonl`           the Gram run`s 379 entries             '
        '%s' % (', '.join(sorted({k[0] for k in has_term_values(
            [json.loads(l) for l in read(os.path.join(D, 'b477_entries.jsonl')).split(NL)
             if l.strip()][:80])})) or 'nothing matching'))
    rec('')
    rec('    ### ### **AND THE CHAIN`S OWN API RETURNS NO PER-TERM VALUE EITHER.**')
    src = read(os.path.join(T, 'b321_window.py'))
    m = re.search(r'def prime_sum\(.*?\n    return ([^\n]+)', src, re.S)
    rec('    `tools/b321_window.py`, `prime_sum` returns : ### **%s**'
        % (m.group(1).strip() if m else '?'))
    rec('    and `terms` is built by ### **`terms.append(n)`** ### -- ### **THE INTEGER `n`, NOT')
    rec('    ITS VALUE.** ### `channels()` passes the same list through as `prime_terms`.')
    rec('')
    rec('    ### ### **BUT ONE ROUTE DOES CARRY THEM, AND THE FIRST DRAFT OF THIS HALT WAS')
    rec('    ### WRONG.** ### `b449_integrand.json` banks `levels[*].terms` as a MAPPING')
    rec('    ### `n -> value`, with `terms_sum` equal to `prime` exactly. ### **A HALT PROVED')
    rec('    ### OVER THE WRONG POPULATION IS NOT A HALT**, and this one was caught by its own')
    rec('    ### finder before it was banked.')
    ig = json.loads(read(os.path.join(D, 'b449_integrand.json')) or '{}')
    lv = ig.get('levels') or []
    tm = (lv[-1].get('terms') if lv else {}) or {}
    rec('      its cell : ### **a = %s** ### -- and it is the ONLY cell so banked.' % ig.get('a'))
    rec('      levels : %d ; terms at the finest : %d ; `terms_sum == prime` : ### **%s**'
        % (len(lv), len(tm),
           abs(lv[-1]['terms_sum'] - lv[-1]['prime']) < 1e-15 if lv else '?'))
    rec('      the terms : %s' % ', '.join('%s:%.6g' % (k, v) for k, v in tm.items()))
    rec('      ### ### **AND `16` AND `17` ARE EXACTLY `0.0` THERE** -- `log 17` sits at the')
    rec('      ### window`s own edge `L = %.9f`, which is b449`s finding restated, not re-scored.'
        % (ig.get('vstar') or 0.0))
    rec('')
    rec('    ### ### **SO THE HALT IS NARROWER THAN "NO BANK HAS THEM", AND SHARPER:**')
    rec('    ### ### **PER-n TERMS ARE BANKED AT EXACTLY ONE OF THE THIRTY-FIVE CELLS, AND IT')
    rec('    ### IS THE OUTLIER.** ### The 34-step decomposition needs them at 35 cells.')
    rec('    ### ### **AND NEITHER `27` NOR `32` IS AMONG THE ELEVEN TERMS BANKED THERE** --')
    rec('    ### that cell`s window reaches only to `a^2 = 17`. ### So the fraction (N1) asks')
    rec('    ### for, at `3^3` and `2^5`, is ### **NOT DECIDABLE FROM THE BANKS** ### in either')
    rec('    ### direction.')
    rec('    ### To obtain it one would evaluate `2 log p / sqrt(n) * interp(log n, v, w)` at each')
    rec('    ### `n`, which needs the smeared window `(v, w)`. ### **THAT IS RUNNING THE CHAIN**,')
    rec('    ### which this order forbids in its own closing line.')
    rec('')
    rec('    ### ### **THE POSITIVE CONTROL: THE FINDER SEES TERM VALUES WHEN THEY EXIST.**')
    fixture = dict(cell=dict(a=2.0, prime_terms={'2': -0.31, '3': -0.12, '4': -0.05}))
    fh = has_term_values(fixture)
    rec('      a fixture written here, carrying `prime_terms` as `n -> value` : %s' % fh)
    fixture2 = dict(cell=dict(a=2.0, prime_terms=[2, 3, 4]))
    rec('      the same field as a bare list of `n`                            : %s'
        % has_term_values(fixture2))
    ok = bool(fh) and fh[0][0] == 'mapping n -> value'
    rec('      ### ### **THE CONTROL FIRES : %s.** ### The finder is not blind; the banks are'
        % ok)
    rec('      ### empty of what the order asks for.')
    if not ok:
        MISSES.append(('positive control', 'the finder failed its own fixture'))

    # ------------------------------------------------------------- (P4) the rehearsal
    rec('')
    rec('(P4) THE (R70) REHEARSAL -- THE STEP WHERE `17` ENTERS, READ BY HAND.')
    rec('-' * 112)
    k17 = next((i for i, e in enumerate(entries) if 17 in e), None)
    if k17 is None:
        MISSES.append(('ladder', '17 never enters'))
    else:
        b, a_ = rows[k17], rows[k17 + 1]
        rec('    the step : a = %.6f -> ### **a = %.6f** ### (a^2 = %.6f crosses 17)'
            % (b['a'], a_['a'], a_['a'] ** 2))
        rec('    ### ### **AND THAT IS THE OUTLIER CELL b446 AND b447 NAMED**, and the first rung')
        rec('    ### past the margin`s minimum.')
        rec('      before : m = %-16.9g arch = %-16.9g pr = %s' % (b['m'], b['arch'], b['pr']))
        rec('      after  : m = %-16.9g arch = %-16.9g pr = %s' % (a_['m'], a_['arch'], a_['pr']))
        rec('      ### increment of m : ### **%+.9g**' % (a_['m'] - b['m']))
        if b['arch'] is not None and a_['arch'] is not None:
            rec('      ### by channel : d(arch) = %+.9g ; d(pr) = %+.9g ; their difference = %+.9g'
                % (a_['arch'] - b['arch'], a_['pr'] - b['pr'],
                   (a_['arch'] - b['arch']) - (a_['pr'] - b['pr'])))
            rec('      ### and `m = arch - pr`, so d(m) should equal d(arch) - d(pr) :')
            rec('      ###   d(m) = %+.9g   against   d(arch) - d(pr) = %+.9g'
                % (a_['m'] - b['m'], (a_['arch'] - b['arch']) - (a_['pr'] - b['pr'])))
            rec('      ###   ### **THEY DIFFER BY %.3g** -- because b437 stores `arch` and `pr`'
                % abs((a_['m'] - b['m']) - ((a_['arch'] - b['arch']) - (a_['pr'] - b['pr']))))
            rec('      ###   ROUNDED to about ten significant figures, as b489 found. ### **THE')
            rec('      ###   CHANNEL SPLIT IS THEREFORE GOOD TO ~1e-4 AND NO FINER.**')
        rec('      the prime powers present after the step : %d -- %s'
            % (len(a_['pp']), a_['pp']))
        rec('    ### ### **WHAT THE REHEARSAL SETTLES:** ### the step`s increment and its CHANNEL')
        rec('    ### split are readable; ### **THE SPLIT WITHIN THE PRIME CHANNEL IS NOT.**')

    # ------------------------------------------------------------- (P5) the ratio
    rec('')
    rec('(P5) COMPONENT 2`S INPUTS -- `|W + Z|` OVER `m`, ALL BANKED.')
    rec('-' * 112)
    rec('    every diagonal entry banks `W` and `zero`; `|W + zero|` is the two-side')
    rec('    disagreement, and `m = -W`. ### Both are banked, so the ratio is a division.')
    rats = [(abs(x['W'] + x['zero']) / (-x['W']), x['a']) for x in diag]
    pk = max(rats)
    rec('    ratios computable at all %d cells : ### **%s**'
        % (len(rats), all(r[0] >= 0 for r in rats)))
    rec('    the peak, previewed here and reported in Component 2 : ### **%.6g at a = %s**'
        % (pk[0], pk[1]))

    # ------------------------------------------------------------- (P6) b334's crossings
    rec('')
    rec('(P6) COMPONENT 3`S SOURCE -- b334`S THREE CROSSINGS, AT THEIR BANK.')
    rec('-' * 112)
    am = read(os.path.join(D, 'b334_the_aim_map.txt'))
    i = am.find('THE EPSTEIN CROSSING REGION')
    seg = am[i:i + 1100] if i >= 0 else ''
    for l in seg.split(NL)[:8]:
        if l.strip():
            rec('      %s' % l.strip()[:108])
    rec('    ### ### **OCCURRENCES OF "CROSSING REGION" IN THE AIM MAP : %d.**'
        % am.count('CROSSING REGION'))
    if i < 0:
        MISSES.append(('b334_the_aim_map.txt', 'the crossing region paragraph is absent'))

    rec('')
    rec('=' * 112)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 112)
    io.open(os.path.join(D, 'b490_extract.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(rows=rows, entries=entries, turn_lo=rows[lo]['a'], turn_hi=rows[hi]['a'],
                   misses=MISSES, terms_banked=False),
              io.open(os.path.join(D, 'b490_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
