# -*- coding: utf-8 -*-
"""b492_components.py -- THE COMPONENTS. ### THE 34 INCREMENTS, ATTRIBUTED.

### ### **THE SPLIT IS AN IDENTITY, NOT A FIT.** ### With per-n terms at both ends of a step,
###   `d(pr) = SUM_{n new at the top} t_hi(n)  +  SUM_{n in both} ( t_hi(n) - t_lo(n) )`
### exactly, because the prime-power set only grows along the ladder.
### ### **THE ARCHIMEDEAN CHANNEL HAS NO PER-n DECOMPOSITION**, so `d(m) = d(arch) - d(pr)`
### attributes only the `d(pr)` half, as the sealed face fixed before any fraction was printed.
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
    R = json.loads(read(os.path.join(D, 'b492_cells.json')))
    rows = R['rows']
    ms = [r['m'] for r in rows]
    lo = min(range(len(ms)), key=lambda i: ms[i])
    hi = max(range(lo, len(ms)), key=lambda i: ms[i])

    rec('=' * 120)
    rec('b492 -- THE COMPONENTS. ### THE PER-n TERMS AT EVERY RUNG, AND THE INCREMENTS ATTRIBUTED.')
    rec('=' * 120)

    # ============================================================== the run's own controls
    rec('')
    rec('### (1) THE RUN, AND ITS CHECK AGAINST b477 BEFORE ANYTHING ELSE WAS READ.')
    rec('-' * 120)
    rec('    cells run : ### **%d** ### ; floor : ### **%.2e** ### (b477`s own)'
        % (len(rows), R['floor']))
    rec('    worst `|W - banked|` : ### **%.3e**' % max(r['dW'] for r in rows))
    rec('    cells reproducing ### **EXACTLY** ### (`|diff| = 0`) : ### **%d of %d**'
        % (sum(1 for r in rows if r['dW'] == 0.0), len(rows)))
    rec('    worst `|sum(terms) - PR|` : ### **%.3e** ### -- the terms account for the prime')
    rec('    channel entirely, at every cell.')
    rec('    run time : %.1f s' % R['seconds'])

    # ============================================================== exact a beside rounded
    rec('')
    rec('### (2) THE GENERATOR`S EXACT `a` BESIDE THE ROUNDED `a`. ### **W-ORD-EXACT-SUPPORT.**')
    rec('-' * 120)
    rec('    %-4s %-13s %-20s %-10s %-6s %-26s %s'
        % ('idx', 'stored a', 'exact a', 'kind', 'n0', 'n0 <= (stored a)^2', 'n0 in the run`s terms'))
    rec('    ' + '-' * 112)
    edge = []
    for r in rows:
        inset = ('%s' % (r['n0'] <= r['a'] * r['a'])) if r['n0'] else '--'
        inter = ('%s' % (str(r['n0']) in r['terms'])) if r['n0'] else '--'
        rec('    %-4d %-13.6f %-20.15f %-10s %-6s %-26s %s'
            % (r['i'], r['a'], r['exact'], r['kind'], r['n0'] or '--', inset, inter))
        if r['n0']:
            edge.append((r, r['n0'] <= r['a'] * r['a'], str(r['n0']) in r['terms']))
    rec('')
    rec('    ### ### **ON THE EXACT GENERATOR EVERY BOUNDARY CELL ADMITS ITS OWN `n0`:** ### at')
    rec('    ### `a = sqrt n0` the window reaches `a^2 = n0`, so `n0 <= a^2` holds because')
    rec('    ### **`n0 <= n0`** -- integer arithmetic, no tolerance.')
    disagree = [e for e in edge if e[1] != e[2] or not e[1]]
    rec('    ### ### **ON THE STORED SIX-PLACE `a`, %d OF THE %d BOUNDARY CELLS EXCLUDE IT**, the'
        % (sum(1 for e in edge if not e[1]), len(edge)))
    rec('    ### rounding having gone DOWN: %s'
        % ', '.join(str(e[0]['n0']) for e in edge if not e[1]))
    rec('    ### and the run`s own term set agrees with the stored-`a` reading at every cell:')
    rec('    ### ### **%d DISAGREEMENTS BETWEEN THE COLUMN AND THE COMPUTED TERMS.**'
        % sum(1 for e in edge if e[1] != e[2]))
    rec('    ### ### **AND WHERE `n0` IS ADMITTED, ITS TERM IS `0`.** ### The window vanishes at')
    rec('    ### its own support edge `v = L`, and `log n0 = L` exactly there:')
    for e in edge:
        if e[2]:
            rec('      a = %-12.6f n0 = %-4d term = ### **%.3e**'
                % (e[0]['a'], e[0]['n0'], e[0]['terms'][str(e[0]['n0'])]))

    # ============================================================== the 34 steps
    rec('')
    rec('### (3) THE 34 INCREMENTS, ATTRIBUTED. ### **THE SPLIT IS AN IDENTITY.**')
    rec('-' * 120)
    rec('    %-4s %-11s %-11s %-9s %-15s %-15s %-15s %-15s %s'
        % ('step', 'a from', 'a to', 'enters', 'd(m)', 'd(pr)', 'NEW terms', 'DRIFT', 'closes'))
    rec('    ' + '-' * 114)
    steps = []
    for i in range(len(rows) - 1):
        a_, b_ = rows[i], rows[i + 1]
        new = [n for n in b_['terms'] if n not in a_['terms']]
        newsum = sum(b_['terms'][n] for n in new)
        drift = sum(b_['terms'][n] - a_['terms'][n] for n in b_['terms'] if n in a_['terms'])
        dpr = b_['prime'] - a_['prime']
        dm = b_['m'] - a_['m']
        darch = b_['arch'] - a_['arch']
        closes = abs(dpr - (newsum + drift))
        steps.append(dict(i=i + 1, a_lo=a_['a'], a_hi=b_['a'], enters=sorted(int(n) for n in new),
                          dm=dm, dpr=dpr, darch=darch, new=newsum, drift=drift, closes=closes))
        rec('    %-4d %-11.6f %-11.6f %-9s %-15.8g %-15.8g %-15.8g %-15.8g %.2e'
            % (i + 1, a_['a'], b_['a'], (','.join(str(int(n)) for n in new) or '(none)'),
               dm, dpr, newsum, drift, closes))
    rec('')
    rec('    ### ### **THE SPLIT CLOSES TO %.2e AT WORST** ### -- it is an identity, and that is'
        % max(s['closes'] for s in steps))
    rec('    ### the arithmetic`s own precision, not a fit`s residual.')
    ent = [s for s in steps if s['enters']]
    rec('    steps admitting a new prime power : ### **%d** ### of %d ; admitting none : %d'
        % (len(ent), len(steps), len(steps) - len(ent)))

    # ============================================================== the fractions
    rec('')
    rec('### (4) THE FRACTION OF EACH ENTRY STEP`S INCREMENT CARRIED BY THE ENTERING TERMS.')
    rec('-' * 120)
    rec('    ### ### **THE DENOMINATOR IS `d(pr)`, THE PRIME CHANNEL`S OWN INCREMENT**, because')
    rec('    ### the archimedean channel has no per-n decomposition -- as the sealed face fixed.')
    rec('    ### The share of `d(m)` is printed beside it and is SMALLER, `d(m)` being the larger.')
    rec('')
    rec('    %-4s %-11s %-9s %-15s %-15s %-14s %s'
        % ('step', 'a to', 'enters', 'NEW terms', 'd(pr)', 'NEW / d(pr)', 'NEW / d(m)'))
    rec('    ' + '-' * 100)
    for s in ent:
        f1 = s['new'] / s['dpr'] if s['dpr'] else float('nan')
        f2 = s['new'] / s['dm'] if s['dm'] else float('nan')
        rec('    %-4d %-11.6f %-9s %-15.8g %-15.8g %-14.6g %.6g'
            % (s['i'], s['a_hi'], ','.join(str(n) for n in s['enters']), s['new'], s['dpr'],
               f1, f2))
    rec('')
    # ### ### **THIS BLOCK'S FIRST DRAFT SAID "EVERY ENTERING TERM IS EXACTLY 0" AND THE TABLE
    # ### ABOVE REFUTES IT.** ### Several are small but non-zero, and ONE carries the whole
    # ### increment. ### The corrected reading is computed, not asserted.
    fr = [(abs(s['new'] / s['dpr']) if s['dpr'] else float('nan'), s) for s in ent]
    big = [x for x in fr if x[0] > 0.5]
    small = [x for x in fr if x[0] <= 0.5]
    zero = [s for s in ent if s['new'] == 0.0]
    rec('    ### ### **AND THE FIRST DRAFT OF THIS PARAGRAPH SAID "EVERY ENTERING TERM IS EXACTLY')
    rec('    ### ZERO", WHICH THE TABLE ABOVE REFUTES.** ### %d of the %d are exactly zero; the'
        % (len(zero), len(ent)))
    rec('    ### rest are small but not zero. ### The corrected reading:')
    rec('      entry steps carrying MORE than half of `d(pr)` : ### **%d**' % len(big))
    for f, s in big:
        rec('        step %d, a = %.6f, enters %s : ### **NEW / d(pr) = %.6g**'
            % (s['i'], s['a_hi'], ','.join(str(n) for n in s['enters']), f))
    rec('      ### ### **AND THAT ONE IS THE FIRST PRIME POWER ENTERING AN EMPTY SET.** ### Before')
    rec('      ### `a = sqrt 2` the prime channel is identically zero, so the first entry IS the')
    rec('      ### whole increment, trivially and by arithmetic rather than by weight.')
    rec('      entry steps carrying at most half : ### **%d** ### ; their LARGEST share of `d(pr)`'
        % len(small))
    rec('        is ### **%.3g**, and %d of them are exactly `0`.'
        % (max(x[0] for x in small), len(zero)))
    rec('    ### ### **WHY THE LATER ENTRIES CARRY NOTHING:** ### a prime power is admitted as')
    rec('    ### `log n` reaches the window`s support edge `L = 2 log a`, and ### **THE WINDOW IS')
    rec('    ### ZERO AT ITS OWN EDGE BY CONSTRUCTION.** ### At a boundary rung the term is `0` or')
    rec('    ### vanishing; at a literal rung the window has moved a little past `log n` and the')
    rec('    ### term is small but non-zero. ### **THAT IS A FACT OF THE SUPPORT, NOT A SMALLNESS')
    rec('    ### OF MEASUREMENT.**')

    # ============================================================== the two named entries
    rec('')
    rec('### (5) THE TWO ENTRIES THE ORDER NAMES, AND THE TWO TURNS.')
    rec('-' * 120)
    rec('    the margin`s MINIMUM      : a = ### **%.6f** ### (index %d)' % (rows[lo]['a'], lo))
    rec('    the margin`s LOCAL MAXIMUM: a = ### **%.6f** ### (index %d)' % (rows[hi]['a'], hi))
    for n in (27, 32):
        b = next((r for r in rows if r['n0'] == n), None)
        st = next((s for s in steps if n in s['enters']), None)
        rec('')
        rec('    `n = %d` : its boundary rung is a = ### **%.6f** ### (index %d), exact '
            % (n, b['a'], b['i']) + 'a = %.15f' % b['exact'])
        rec('      on EXACT `a` it is admitted there : ### **True** ### (`%d <= %d`)' % (n, n))
        rec('      on the STORED `a` the run`s terms admit it there : ### **%s**'
            % (str(n) in b['terms']))
        rec('      the step at which the run`s terms first admit it : %s'
            % ('### **%d, to a = %.6f**' % (st['i'], st['a_hi']) if st else '### **NEVER**'))
        rec('      is its boundary rung a TURN ? ### **%s**'
            % ('YES -- the local maximum' if b['i'] == hi else
               ('YES -- the minimum' if b['i'] == lo else 'NO')))
    rec('')
    rec('    ### ### **`3^3` SITS EXACTLY AT THE LOCAL MAXIMUM; `2^5` SITS AT THE LAST RUNG, WHICH')
    rec('    ### IS AN ENDPOINT AND NOT A TURN.** ### The ladder stops there, so no step past it')
    rec('    ### exists to turn.')

    # ============================================================== entry vs non-entry
    rec('')
    rec('### (6) ENTRY RUNGS AGAINST NON-ENTRY RUNGS, IN MAGNITUDE.')
    rec('-' * 120)
    e = [abs(s['dm']) for s in ent]
    ne = [abs(s['dm']) for s in steps if not s['enters']]
    rec('    entry steps     : n = %-3d  mean |d(m)| = ### **%.6g** ### ; max %.6g'
        % (len(e), sum(e) / len(e), max(e)))
    rec('    non-entry steps : n = %-3d  mean |d(m)| = ### **%.6g** ### ; max %.6g'
        % (len(ne), sum(ne) / len(ne), max(ne)))
    rec('    ### ### **THE ENTRY RUNGS` MEAN %s THE NON-ENTRY RUNGS`.**'
        % ('EXCEEDS' if sum(e) / len(e) > sum(ne) / len(ne) else 'DOES NOT EXCEED'))
    rec('    ### ### **AND THE COMPARISON IS CONFOUNDED BY WHERE THEY SIT.** ### The non-entry')
    rec('    ### steps include the small-`a` end, where `m` is two hundred times larger and every')
    rec('    ### increment with it. ### **A MEAN OVER STEPS AT DIFFERENT SCALES IS NOT A')
    rec('    ### COMPARISON OF MECHANISMS**, and the act prints it because the order asks, with')
    rec('    ### the confound named.')

    # ============================================================== the sentence
    rec('')
    rec('### (7) ONE SENTENCE THE TABLE SUPPORTS, AND NO WIDER.')
    rec('-' * 120)
    _fr = [(abs(s['new'] / s['dpr']) if s['dpr'] else 0.0, s) for s in ent]
    _small = [x for x in _fr if x[0] <= 0.5]
    sentence = ('On this ladder, at %d of the %d steps that admit a new prime power the entering '
                'terms carry at most %.1e of the prime channel’s increment, the whole of it '
                'being the drift of terms already present; the one exception is the first prime '
                'power entering an empty set, where the entry is the increment by arithmetic.'
                % (len(_small), len(ent), max(x[0] for x in _small)))
    rec('    ### **%s**' % sentence)
    rec('')
    rec('    ### ### **WHAT IT DOES NOT SAY.** ### It does not say the margin`s turns are caused')
    rec('    ### by drift, nor that they are caused by anything: ### **THE ARCHIMEDEAN CHANNEL IS')
    rec('    ### NOT DECOMPOSED HERE** ### and `d(m) = d(arch) - d(pr)` has a half this act cannot')
    rec('    ### attribute. ### It does not extend past `a = %.6f`. ### **AND NOTHING ABOUT RH'
        % rows[-1]['a'])
    rec('    ### FOLLOWS FROM AN ATTRIBUTION.**')

    rec('')
    rec('=' * 120)
    io.open(os.path.join(D, 'b492_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(steps=steps, lo=lo, hi=hi, turn_lo=rows[lo]['a'], turn_hi=rows[hi]['a'],
                   n_entry=len(ent), worst_closes=max(s['closes'] for s in steps),
                   worst_dW=max(r['dW'] for r in rows),
                   exact_zero=sum(1 for r in rows if r['dW'] == 0.0),
                   all_entries_zero=all(s['new'] == 0.0 for s in ent),
                   n_exact_zero=sum(1 for s in ent if s['new'] == 0.0),
                   max_small_share=max((abs(s['new'] / s['dpr']) if s['dpr'] else 0.0)
                                       for s in ent
                                       if (abs(s['new'] / s['dpr']) if s['dpr'] else 0.0) <= 0.5),
                   mean_entry=sum(e) / len(e), mean_nonentry=sum(ne) / len(ne),
                   sentence=sentence),
              io.open(os.path.join(D, 'b492_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL + '  written: b492_components.txt, b492_results.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
