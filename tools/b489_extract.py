# -*- coding: utf-8 -*-
"""b489_extract.py -- THE SURVEY. ### **NOTHING IS RUN AND NO CHAIN IS CALLED.**

### Every number is READ from a bank already on disk:
###   the ladder      -- `data/b477_entries.jsonl`, `kind == "diagonal"` (35 cells, W banked)
###   the control     -- the same file, `kind == "control_diagonal"` (the same 35 cells)
###   the ladder's parts -- `data/b437_rungs.json` (arch, pr, rung, bound, resid)
###   the aim map     -- `data/b334_leg_reaching_40.json`, `_81`, `data/b334_leg_covered.json`
### ### **THE ONLY ARITHMETIC THIS TOOL DOES ITSELF IS THE PRIME POWERS IN `[a^-2, a^2]`**,
### which is a sieve over integers and not a chain.

### ### **ORIENTATION, PER (R87):** ### `W = PR - A`, so the margin is ### **m(a) = -W(f_a) =
### A - PR**, the places side's own difference. ### The zero side's independent value is banked
### beside it, and the two-side residual is printed, never assumed.
"""
import io
import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
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


def jload(name):
    try:
        return json.loads(read(os.path.join(D, name)) or 'null')
    except Exception:
        MISSES.append((name, 'unreadable'))
        return None


def prime_powers_upto(x):
    """### every prime power p^k <= x, as (p, k, value). ### A SIEVE, NOT A CHAIN."""
    n = int(x)
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    out = []
    for p in range(2, n + 1):
        if sieve[p]:
            v, k = p, 1
            while v <= n:
                out.append((p, k, v))
                v *= p
                k += 1
    return sorted(out, key=lambda t: t[2])


def main():
    rec('=' * 110)
    rec('b489 -- THE SURVEY. ### THE MARGIN OVER SUPPORT, READ FROM THE BANKS.')
    rec('=' * 110)

    # ---------------------------------------------------------------- (P1) the ladder
    rec('')
    rec('(P1) THE LADDER -- 35 CELLS, `W` BANKED AT b477.')
    rec('-' * 110)
    ent = [json.loads(l) for l in read(os.path.join(D, 'b477_entries.jsonl')).split(NL) if l.strip()]
    diag = [x for x in ent if x.get('kind') == 'diagonal']
    ctrl = [x for x in ent if x.get('kind') == 'control_diagonal']
    rungs = (jload('b437_rungs.json') or {}).get('rows') or []
    rec('    `b477_entries.jsonl` : %d entries -- diagonal %d, control_diagonal %d, offdiagonal %d'
        % (len(ent), len(diag), len(ctrl),
           len([x for x in ent if x.get('kind') == 'offdiagonal'])))
    rec('    `b437_rungs.json`    : %d rows' % len(rungs))
    if len(diag) != 35 or len(ctrl) != 35:
        MISSES.append(('b477_entries.jsonl', 'expected 35 diagonal and 35 control'))
    aw = {round(x['a'], 6) for x in diag}
    if aw != {round(x['a'], 6) for x in ctrl}:
        MISSES.append(('b477_entries.jsonl', 'ladder and control are not over the same cells'))
    rec('    ### ### **THE CONTROL IS OVER THE SAME 35 SUPPORT WIDTHS : %s.**'
        % (aw == {round(x['a'], 6) for x in ctrl}))
    rr = {round(x['a'], 6): x for x in rungs}
    rec('    ### every ladder cell has a `b437` row : ### **%s**'
        % all(round(x['a'], 6) in rr for x in diag))

    # ---------------------------------------------------------------- (P2) the rehearsal
    rec('')
    rec('(P2) THE (R70) REHEARSAL -- ONE LADDER CELL AND ONE AIM-MAP CELL, READ BY HAND.')
    rec('-' * 110)
    rec('    ### ### **LADDER CELL -- the last rung, `a = 5.656854`.**')
    lc = [x for x in diag if abs(x['a'] - 5.656854) < 1e-9][0]
    rg = rr[round(5.656854, 6)]
    rec('      b437 row : arch = %.15g ; pr = %.15g' % (rg['arch'], rg['pr']))
    rec('      ### the orientation`s own arithmetic : W = PR - A = %.15g' % (rg['pr'] - rg['arch']))
    rec('      b477 banks W = %.15g' % lc['W'])
    agree = abs((rg['pr'] - rg['arch']) - lc['W']) < 1e-12
    rec('      ### ### **THE TWO BANKS AGREE ON W TO 1e-12 : %s.**' % agree)
    rec('      so the margin m(a) = -W = A - PR = ### **%.15g**' % (-lc['W']))
    rec('      the ZERO SIDE, banked independently : %.15g' % lc['zero'])
    rec('      the two-side residual : %.6g ; the run`s own `trunc_bound` : %.6g'
        % (abs(lc['zero'] + lc['W']), lc['trunc_bound']))
    resid2 = abs(lc['zero'] + lc['W'])
    rec('      ### ### **THE TWO-SIDE RESIDUAL EXCEEDS THE RUN`S OWN `trunc_bound` BY %.1f ORDERS**'
        % math.log10(resid2 / lc['trunc_bound']))
    rec('      ### -- b484`s quadrature finding, visible again at this cell. ### It does NOT')
    rec('      ### threaten the margin HERE: the residual sits %.1f orders BELOW the margin itself,'
        % math.log10(-lc['W'] / resid2))
    rec('      ### so `m` is resolved at this rung. ### **THE BOUND IS WRONG; THE MARGIN IS NOT.**')
    if not agree:
        MISSES.append(('b437/b477', 'the two banks disagree on W'))

    rec('')
    rec('    ### ### **AIM-MAP CELL -- the reaching leg, `a = 40`, `gamma = 4`.**')
    r40 = jload('b334_leg_reaching_40.json') or {}
    row = next((x for x in (r40.get('rows') or []) if abs(x['gamma'] - 4.0) < 1e-9), None)
    if row is None:
        MISSES.append(('b334_leg_reaching_40.json', 'gamma = 4 row absent'))
    else:
        rec('      seed : %s' % row['name'])
        rec('      arch_z   = %.15g' % row['arch_z'])
        rec('      places_z = %.15g' % row['places_z'])
        rec('      prime_z  = %.15g' % row['prime_z'])
        rec('      ### ### **AND THE REHEARSAL`S FIRST READING WAS WRONG, WHICH IS WHY IT RAN.**')
        rec('      ### It took `places_z` for the PRIME SUM and computed `arch_z - places_z`,')
        rec('      ### getting ### **%.9g** ### -- a NEGATIVE number where the aim map prints a'
            % (row['arch_z'] - row['places_z']))
        rec('      ### positive room. ### **`places_z` IS ALREADY THE SIGNED PLACES SUM**, i.e.')
        rec('      ### this family`s `W`; the prime slot is ### **`prime_z`**.')
        rec('      ### the orientation, done on the right fields : A - PR = %.15g'
            % (row['arch_z'] - row['prime_z']))
        rec('      ### and, independently, -W = -places_z = %.15g' % (-row['places_z']))
        rec('      the bank`s own `room_z` : %.15g' % row['room_z'])
        ok = (abs((row['arch_z'] - row['prime_z']) - row['room_z']) < 1e-9
              and abs(-row['places_z'] - row['room_z']) < 1e-12)
        rec('      ### ### **`room_z` IS THE MARGIN, BY BOTH ROUTES, AGREEING : %s.**' % ok)
        rec('      ### and the aim map prints this cell as the NARROWEST point of the room:')
        rec('      ### *"A_z - PR_z = +0.000577751 at a = 40"* -- read here as %.9g'
            % row['room_z'])
        if not ok:
            MISSES.append(('b334', 'room_z is not A - PR'))

    rec('')
    rec('    ### ### **WHAT THE REHEARSAL SETTLED BEFORE ANY TABLE WAS BUILT:**')
    rec('    ### (i) the margin is ### **`A - PR`** ### in BOTH families, by the same orientation;')
    rec('    ### (ii) the ladder`s margin is a function of ### **`a` ALONE**, while the aim map`s')
    rec('    ###      is a function of ### **`(a, gamma)`** -- ### **THEY ARE NOT THE SAME')
    rec('    ###      VARIABLE**, and a fit over the second is not a second reading of the first;')
    rec('    ### (iii) the ladder`s zero-side value is banked, so its margin has a CHECK; the aim')
    rec('    ###      map`s `room_z` is a places-side difference with no independent zero side')
    rec('    ###      banked beside it. ### **THE CHECK EXISTS ON ONE FAMILY ONLY.**')

    # ---------------------------------------------------------------- (P3) the aim map
    rec('')
    rec('(P3) THE AIM MAP -- ITS CELLS, AND WHAT VARIES ACROSS THEM.')
    rec('-' * 110)
    legs = []
    for nm, f in (('reaching a=40', 'b334_leg_reaching_40.json'),
                  ('reaching a=81', 'b334_leg_reaching_81.json'),
                  ('covered', 'b334_leg_covered.json')):
        j = jload(f) or {}
        rows = j.get('rows') or []
        legs.append((nm, f, rows))
        widths = sorted({round(x['a'], 4) for x in rows})
        gammas = sorted({round(x['gamma'], 6) for x in rows})
        rec('    %-14s %-32s rows %2d ; widths %s ; gammas %d'
            % (nm, f, len(rows), widths, len(gammas)))
    total = sum(len(r) for _, _, r in legs)
    rec('    ### ### **AIM-MAP CELLS IN ALL : %d.**' % total)
    if total != 56:
        MISSES.append(('b334', 'expected 56 aim-map cells, got %d' % total))

    # ---------------------------------------------------------------- (P4) the control
    rec('')
    rec('(P4) THE CONTROL`S MARGIN -- THE SAME ORIENTATION, THE SAME CELLS.')
    rec('-' * 110)
    c0 = ctrl[0]
    rec('    the control`s banked fields : %s' % ', '.join(sorted(c0.keys())))
    rec('    ### ### **IT BANKS NO `W`.** ### It banks `places`, `arch`, `finite`, `pole`, and')
    rec('    ### `places = finite - arch` at every cell -- checked below. ### So the control`s')
    rec('    ### own W is `places`, and its margin is ### **m_Q = -places = arch - finite**, the')
    rec('    ### same `A - PR` with the Epstein function`s finite sum in the prime slot.')
    bad = [x['a'] for x in ctrl if abs(x['places'] - (x['finite'] - x['arch'])) > 1e-9]
    rec('    cells where `places != finite - arch` : ### **%d** ### of %d' % (len(bad), len(ctrl)))
    if bad:
        MISSES.append(('b477 control', 'places != finite - arch at %d cells' % len(bad)))
    rec('    ### ### **AND THE IDENTIFICATION IS THIS SEAT`S, NOT THE BANK`S.** ### b477 never')
    rec('    ### writes the word `margin` for the control. ### It is read here by the orientation')
    rec('    ### (R87) fixes, and the arithmetic that licenses it is printed above.')

    # ---------------------------------------------------------------- (P5) the falsifier's height
    rec('')
    rec('(P5) THE FALSIFIER`S HEIGHT, `t = 16.29`, AT ITS OWN ADDRESS.')
    rec('-' * 110)
    am = read(os.path.join(D, 'b334_the_aim_map.txt'))
    hits = [l.strip() for l in am.split(NL) if '16.290216' in l]
    for h in hits[:6]:
        rec('      %s' % h[:118])
    rec('    ### ### **OCCURRENCES IN THE AIM MAP`S OWN TEXT : %d.**' % len(hits))
    if not hits:
        MISSES.append(('b334_the_aim_map.txt', 'the height 16.290216 is not in it'))
    rec('    ### ### **AND IT IS A HEIGHT, NOT A SUPPORT WIDTH.** ### The aim map`s crossing')
    rec('    ### region is three AIMS `(a, gamma)`, each at `gamma = 16.290216` or `46.960994`,')
    rec('    ### on the REACHING leg at `a = 40` and `a = 81`. ### The ladder runs to')
    rec('    ### `a = 5.656854`. ### **THE FALSIFIER NAMES A HEIGHT THE LADDER`S WIDTHS DO NOT')
    rec('    ### REACH**, and this survey says so before any fit is made.')

    # ---------------------------------------------------------------- (P6) prime powers
    rec('')
    rec('(P6) THE PRIME POWERS IN `[a^-2, a^2]` -- A SIEVE, SPOT-CHECKED.')
    rec('-' * 110)
    for a in (1.3, 1.41, 1.5, 2.0, 5.656854):
        pp = prime_powers_upto(a * a)
        rec('      a = %-10s a^2 = %-12.6f prime powers <= a^2 : %d  %s'
            % (a, a * a, len(pp), [t[2] for t in pp][:12]))
    rec('    ### ### **`[a^-2, a^2]` IS SYMMETRIC IN `log`, SO EACH `p^k <= a^2` CONTRIBUTES')
    rec('    ### TWICE** -- at `+log p^k` and at `-log p^k`. ### The count below is of DISTINCT')
    rec('    ### prime powers `p^k <= a^2`, and the doubling is stated, not silently folded in.')
    rec('    ### the first prime power is `2`, so a cell has NO prime power until `a >= sqrt 2`')
    rec('    ### = 1.41421356. ### That is why the first three rungs bank `pr = 0`.')

    rec('')
    rec('=' * 110)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 110)
    io.open(os.path.join(D, 'b489_extract.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(n_diag=len(diag), n_ctrl=len(ctrl), n_rungs=len(rungs),
                   aim_cells=total, misses=MISSES),
              io.open(os.path.join(D, 'b489_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
