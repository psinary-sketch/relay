# -*- coding: utf-8 -*-
"""b476_extract.py -- THE SURVEY FOR THE COMPRESSION REGISTRATION.

### ### **NO GRAM ENTRY IS COMPUTED HERE.** ### What this tool does: reads the two families from their
### own banks; prints each cell's `a`, its support and the prime powers the support carries; runs the
### (R70) REHEARSAL -- the family reader and the DIAGONAL CONTROL on ONE cell, `G(a,a)` recomputed by
### b321's own chain and set against b321's banked `W` -- and times it, which is the chain's cost per
### run; reads the truncation from the atlas; reads the CONTROL's own census; and prices the resolving
### family size and the total run.
"""
import io
import json
import math
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'e16'))

import numpy as np                    # noqa: E402
import carto_atlas as AT              # noqa: E402  ### the settled chain, IMPORTED never edited
import b317_smear as SM               # noqa: E402
import b318_square as SQ              # noqa: E402
import b321_window as WI              # noqa: E402

NL = chr(10)
L, MISSES = [], []
REHEARSAL_CELL = 1.5                  # ### fixed here, before the rehearsal runs
FLOOR = 1.49e-08                      # ### b446: sqrt(eps), the chain's own floor

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read()
    except Exception:
        return ''


def prime_powers_upto(x):
    """### Every prime power `p^k <= x`, by trial division -- the same objects b321's prime sum walks."""
    out = []
    n = 2
    while n <= x + 1e-12:
        m, p = n, None
        for q in range(2, int(n ** 0.5) + 1):
            if n % q == 0:
                p = q
                break
        if p is None:
            p = n
        k, r = 0, n
        while r % p == 0:
            r //= p
            k += 1
        if r == 1:
            out.append(n)
        n += 1
    return out


def main():
    rec('=' * 104)
    rec('b476 -- THE SURVEY. ### NOTHING BUT THE (R70) REHEARSAL IS COMPUTED.')
    rec('=' * 104)

    # ----------------------------------------------------------------------------- (P1) the family
    rec('')
    rec('(P1) THE AIM-PLANE FAMILY, AS b321`S CHAIN DEFINES IT, AT THE CELLS THE RECORD HOLDS.')
    rec('-' * 104)
    rows = json.loads(read(os.path.join(D, 'b321_rows.json')) or '{}')
    cells = sorted(float(a) for a in rows.get('c2', {}))
    above = sorted(float(a) for a in rows.get('above', []))
    totals = {float(k): v for k, v in rows.get('totals', {}).items()}
    rec('    the chain, quoted from b321_run.py:139-141 and :242-245 --')
    rec('      g = SM.mean_zero_variant(a) ; f = SQ.autocorrelation(g) ; ch = WI.channels(f.v, f.w)')
    rec('    ### the seed`s support is [a^-1, a] ; ### **THE FORM f = g conv gbar^# HAS TWICE THE SEED`S')
    rec('    ### SUPPORT IN v, SO ITS OWN SUPPORT IS [a^-2, a^2]** -- b321_window.py:8 says so in its head.')
    rec('')
    rec('    %-8s %-10s %-16s %-7s %-34s %s' % ('a', 'above?', 'W = PR - A', 'p^k<=a', 'p^k <= a^2 (the form`s own)', 'count'))
    fam = []
    for a in cells:
        seed_pp = prime_powers_upto(a)
        form_pp = prime_powers_upto(a * a)
        w = totals.get(a)
        fam.append(dict(a=a, above=a in above, W=w, seed_primes=seed_pp, form_primes=form_pp))
        rec('    %-8g %-10s %-16s %-7s %-34s %d'
            % (a, 'YES' if a in above else 'no', ('%.9f' % w) if w is not None else 'NOT BANKED',
               ','.join(str(x) for x in seed_pp) or '-', ','.join(str(x) for x in form_pp) or '-',
               len(form_pp)))
    rec('    ### ### **CELLS %d ; WITH A BANKED W %d.**' % (len(cells), len(totals)))

    # -------------------------------------------------------------------------- (P2) the ladder
    rec('')
    rec('(P2) THE RADIUS LADDER`S CELLS, AND WHETHER THEIR `g` DIFFERS.')
    rec('-' * 104)
    rungs = json.loads(read(os.path.join(D, 'b437_rungs.json')) or '{}')
    lrows = [r for r in rungs.get('rows', []) if r.get('zero') is not None]
    lad = sorted(r['a'] for r in lrows)
    rec('    ladder cells carrying every channel : %d ; radii %g to %g' % (len(lad), lad[0], lad[-1]))
    rec('    b437`s own window, from its components record : the same `mean_zero_variant` seed, and the')
    rec('    same autocorrelation -- b437_checks.py:426 tests that its own record says `mean_zero_variant`')
    rec('    ### ### **SO THE LADDER`S `g` DOES NOT DIFFER FROM THE AIM PLANE`S: ONE CONSTRUCTION, TWO')
    rec('    ### SETS OF RADII.** ### What differs is the RADIUS SET and the fact that the ladder`s cells')
    rec('    ### carry a zero channel of their own.')
    overlap = sorted(set(lad) & set(cells))
    rec('    radii shared with the aim-plane cells : %s' % (overlap or 'NONE'))
    rec('    ladder radii : %s' % ', '.join('%g' % x for x in lad))

    # ------------------------------------------------------------------- (P3) the rehearsal (R70)
    rec('')
    rec('(P3) THE REHEARSAL UNDER (R70): THE FAMILY READER AND THE DIAGONAL CONTROL, ON ONE CELL.')
    rec('-' * 104)
    a0 = REHEARSAL_CELL
    rec('    the cell, fixed in this tool`s head before the run : a = %g' % a0)
    t0 = time.time()
    g = SM.mean_zero_variant(a0)
    f = SQ.autocorrelation(g)
    ch = WI.channels(f.v, f.w)
    dt = time.time() - t0
    diag = ch['prime'] - ch['arch']
    banked = totals.get(a0)
    delta = None if banked is None else abs(diag - banked)
    rec('    the family reader returns : seed support %g, form support %g, v in [%.6f, %.6f], %d samples'
        % (g.support, f.support, f.v[0], f.v[-1], len(f.v)))
    rec('    the four channels at a = %g : zero %.9f ; pole %.3e ; arch %.9f ; prime %.9f'
        % (a0, ch['zero'], ch['pole'], ch['arch'], ch['prime']))
    rec('    ### ### **G(a,a) = PR - A = %.12f**' % diag)
    rec('    ### ### **b321`S BANKED W AT THIS CELL = %.12f**' % banked if banked is not None else
        '    ### banked W : NOT BANKED')
    rec('    ### ### **|DIFFERENCE| = %.3e ; THE CHAIN`S OWN FLOOR = %.3e ; WITHIN THE FLOOR : %s**'
        % (delta, FLOOR, delta < FLOOR) if delta is not None else '    no comparison possible')
    if delta is None or delta >= FLOOR:
        MISSES.append(('diagonal control', 'a=%g delta=%s' % (a0, delta)))
    rec('    ### ### **THE CHAIN`S COST PER RUN, TIMED HERE : %.2f s** -- one seed, one' % dt)
    rec('    ### autocorrelation, one four-channel evaluation, this machine, foreground.')

    # ------------------------------------------------------------------ (P4) the truncation
    rec('')
    rec('(P4) THE TRUNCATION, AS THE INSTRUMENT`S OWN.')
    rec('-' * 104)
    Tz = float(AT.GAM[-1])
    rec('    the zero channel sums BANKED ordinates : %d of them, from %.6f to ### **T = %.6f**'
        % (len(AT.GAM), float(AT.GAM[0]), Tz))
    tb = WI.trunc_bound(f.v, f.w)
    rec('    the atlas`s own truncation bound at the rehearsal cell : %s' % (tb,))
    rec('    ### ### **EACH OMITTED ON-LINE ZERO CONTRIBUTES hhat(gamma) >= 0 TO THE ZERO SIDE UNDER RH,')
    rec('    ### SO THE TRUNCATED GRAM IS AT MOST THE TRUE GRAM IN THE LOEWNER ORDER** -- the order`s own')
    rec('    ### statement, registered as the instrument`s and not proved here.')

    # ------------------------------------------------------------------ (P5) the control
    rec('')
    rec('(P5) THE CONTROL: THE RECORD`S OWN EPSTEIN CENSUS, AND THE ORDER`S HEIGHT CHECKED AGAINST IT.')
    rec('-' * 104)
    off = json.loads(read(os.path.join(D, 'b326_offline.json')) or '{}')
    found = []

    def walk(o):
        if isinstance(o, dict):
            if 'rho_a' in o:
                found.append(tuple(o['rho_a']))
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(off)
    hs = sorted(set(round(h, 6) for _, h in found))
    rec('    the census box : sigma in [%s, %s], t up to ### **T = %s** ; located off-line zeros : %d'
        % (off.get('sig_lo'), off.get('sig_hi'), off.get('T'), len(hs)))
    rec('    their heights : %s' % ', '.join('%g' % h for h in hs))
    rec('    ### ### **THE ORDER NAMES "t about 176.70". ### THE RECORD`S CENSUS HOLDS NO ZERO THERE, AND')
    rec('    ### 176.70 IS ABOVE THE CENSUS`S OWN CEILING T = %s.**' % off.get('T'))
    rec('    ### ### **THE LOWEST LOCATED OFF-LINE ZERO IS t = %g**, and it is the one this' % hs[0])
    rec('    ### registration names for the control -- lower is cheaper to resolve, and it is in the bank.')

    # ------------------------------------------------------- the resolving size, PRICED not assumed
    rec('')
    rec('    THE RESOLVING FAMILY SIZE, PRICED BY THE CHAIN`S OWN TRANSFORM (no Gram entry computed):')
    rec('      the rule, fixed here: a family RESOLVES a zero at height t when some window`s own')
    rec('      transform carries weight there above the chain`s floor -- |hhat_a(t)| > %.2e.' % FLOOR)
    price = []
    for a in cells + [x for x in lad if x not in cells]:
        gg = SM.mean_zero_variant(a)
        ff = SQ.autocorrelation(gg)
        val = float(abs(AT.hhat(ff.v, ff.w, np.array([hs[0]]))[0]))
        price.append(dict(a=a, hhat=val, resolves=val > FLOOR))
        rec('      a = %-9g |hhat(%g)| = %.3e   %s' % (a, hs[0], val, 'RESOLVES' if val > FLOOR else 'below the floor'))
    first_res = next((p['a'] for p in sorted(price, key=lambda x: x['a']) if p['resolves']), None)
    n_res = sum(1 for p in price if p['resolves'])
    rec('      ### ### **CELLS THAT RESOLVE IT : %d OF %d ; THE SMALLEST SUCH RADIUS : %s**'
        % (n_res, len(price), first_res))

    # ------------------------------------------------------------------ (P6) the price of the run
    rec('')
    rec('(P6) THE PRICE OF THE RUN, FROM THE COST TIMED ABOVE.')
    rec('-' * 104)
    for label, n in (('the aim-plane cells', len(cells)), ('the ladder cells', len(lad)),
                     ('both families together', len(cells) + len(lad))):
        e = n * (n + 1) // 2
        rec('    %-24s n = %-4d entries n(n+1)/2 = %-6d at %.2f s = %.0f s (%.1f min)'
            % (label, n, e, dt, e * dt, e * dt / 60.0))
    rec('    ### ### **AND THE CONTROL COSTS THE SAME PER ENTRY**, on its own family to the resolving size.')
    rec('    ### The numerical instrument lane is not opened by this registration.')

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b476_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(family=fam, cells=cells, above=above, ladder=lad, overlap=overlap,
                   rehearsal=dict(a=a0, diag=diag, banked=banked, delta=delta, seconds=dt,
                                  floor=FLOOR, within=bool(delta is not None and delta < FLOOR)),
                   truncation=dict(T=Tz, ordinates=len(AT.GAM)),
                   control=dict(census_T=off.get('T'), sig=[off.get('sig_lo'), off.get('sig_hi')],
                                heights=hs, lowest=hs[0], order_height=176.70,
                                order_height_in_bank=any(abs(h - 176.70) < 0.5 for h in hs)),
                   resolution=dict(rule='|hhat_a(t)| > %.2e' % FLOOR, t=hs[0], rows=price,
                                   resolving=n_res, smallest=first_res),
                   price=dict(seconds_per_run=dt,
                              aim=len(cells) * (len(cells) + 1) // 2,
                              ladder=len(lad) * (len(lad) + 1) // 2,
                              both=(len(cells) + len(lad)) * (len(cells) + len(lad) + 1) // 2),
                   misses=MISSES),
              io.open(os.path.join(D, 'b476_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
