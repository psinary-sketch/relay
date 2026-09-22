# -*- coding: utf-8 -*-
"""b477_gram.py -- THE GRAM RUN, UNDER THE b476 REGISTRATION AS AMENDED BY (R87).

### ### **THE CHAIN IS NOT EDITED.** ### `f_ab` is BUILT HERE and SUPPLIED to it, exactly as b321
### supplied `f`: for the diagonal by the chain's own `autocorrelation`, and off the diagonal by the
### cross-correlation of the two seeds on one grid.
### ### **ZETA'S ENTRY** is `b321_window.channels(f_ab)` -> `W = PR - A`, the places sum.
### ### **THE CONTROL'S ENTRY** is `b325_epstein.channels_q(f_ab)` -> `places = PR - A`, the EPSTEIN
### object's OWN finite and archimedean channels. ### **THAT CHAIN HAS NO ZERO SIDE, AND THE CONTROL'S
### VERDICT IS SCOPED TO THE PLACES SIDE.**
### The diagonal runs first at every cell, against b321's (and b437's) banked W, and a mismatch beyond
### the floor HALTS the run before any off-diagonal entry. ### Every entry is appended as it lands.
"""
import datetime
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
import carto_atlas as AT              # noqa: E402
import b317_smear as SM               # noqa: E402
import b318_square as SQ              # noqa: E402
import b321_window as WI              # noqa: E402
import b325_epstein as EP             # noqa: E402

FLOOR = 1.49e-08
ENTRIES = os.path.join(D, 'b477_entries.jsonl')
NL = chr(10)


def say(s):
    print('[%s] %s' % (datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M:%S'), s), flush=True)


def cross(ga, gb, nv=SQ.AUTOCORR_NV):
    """### `(g_a conv gbar_b^#)(v) = INT g_a(u + v) g_b(u) du`, built on ONE grid covering both seeds.

    ### ### **IT MIRRORS `b318_square.autocorrelation` LINE FOR LINE** -- same grid construction, same
    ### `np.correlate(..., 'full')`, same `du` weight, same support doubling -- and reduces to it when
    ### the two seeds are the same. ### **THE CHAIN IS NOT TOUCHED; ONLY ITS INPUT IS BUILT.**
    """
    L = max(abs(float(ga.v[-1])), abs(float(gb.v[-1])))
    u = np.linspace(-L, L, int(nv))
    du = u[1] - u[0]
    wa = np.interp(u, ga.v, ga.w, left=0.0, right=0.0)
    wb = np.interp(u, gb.v, gb.w, left=0.0, right=0.0)
    xc = np.correlate(wa, wb, mode='full') * du
    v = np.linspace(-2.0 * L, 2.0 * L, xc.size)
    return SM.TestFunction('cross of %s and %s' % (ga.name, gb.name), v, xc,
                           'np.correlate of two seeds on one grid, b318`s construction')


def main():
    say('b477 GRAM RUN START -- under b476 as amended by (R87)')
    S = json.loads(io.open(os.path.join(D, 'b476_survey.json'), encoding='utf-8').read())
    aim = list(S['cells'])
    lad = list(S['ladder'])
    banked = {r['a']: r['W'] for r in S['family']}
    rungs = json.loads(io.open(os.path.join(D, 'b437_rungs.json'), encoding='utf-8').read())
    for r in rungs.get('rows', []):
        if r.get('zero') is not None:
            banked[r['a']] = r['sum_v']
    say('aim-plane cells %d ; ladder cells %d ; banked W available for %d of %d'
        % (len(aim), len(lad), sum(1 for a in aim + lad if banked.get(a) is not None), len(aim) + len(lad)))

    out = io.open(ENTRIES, 'w', encoding='utf-8', newline=NL)

    def bank(rec):
        out.write(json.dumps(rec) + NL)
        out.flush()

    # ### ---------------------------------------------------------------- THE SEEDS, BUILT ONCE
    seeds = {}
    for a in aim + lad:
        t0 = time.time()
        seeds[a] = SM.mean_zero_variant(a)
        say('seed a=%g built in %.1f s' % (a, time.time() - t0))

    # ### ------------------------------------------------- THE DIAGONAL FIRST, AT EVERY CELL
    say('=== DIAGONAL CHECK AT EVERY CELL -- a mismatch beyond %.2e HALTS before any off-diagonal' % FLOOR)
    diag = {}
    for a in aim + lad:
        t0 = time.time()
        f = SQ.autocorrelation(seeds[a])
        ch = WI.channels(f.v, f.w)
        W = ch['prime'] - ch['arch']
        Z = ch['zero']
        tb = WI.trunc_bound(f.v, f.w)
        b = banked.get(a)
        d = None if b is None else abs(W - b)
        ok = (b is None) or (d < FLOOR)
        diag[a] = W
        say('DIAG a=%-9g W=%+.12f  banked=%s  |diff|=%s  Z=%+.9f  trunc_bound=%.3e  %s  (%.1f s)'
            % (a, W, ('%+.12f' % b) if b is not None else 'NONE', ('%.3e' % d) if d is not None else '-',
               Z, tb, 'OK' if ok else '### MISMATCH', time.time() - t0))
        bank(dict(kind='diagonal', a=a, W=W, banked=b, diff=d, zero=Z, trunc_bound=tb, ok=bool(ok)))
        if not ok:
            say('### HALT -- THE DIAGONAL CONTROL FAILED AT a=%g. NO OFF-DIAGONAL ENTRY IS COMPUTED.' % a)
            out.close()
            return 2
    say('=== DIAGONAL CHECK PASSED AT EVERY CELL')

    # ### ------------------------------------------------- THE OFF-DIAGONALS, AIM PLANE THEN LADDER
    for label, cells in (('AIM PLANE', aim), ('LADDER', lad)):
        n = len(cells)
        say('=== %s : %d cells, %d entries (%d off-diagonal)' % (label, n, n * (n + 1) // 2, n * (n - 1) // 2))
        for i in range(n):
            for j in range(i + 1, n):
                a, b = cells[i], cells[j]
                t0 = time.time()
                fab = cross(seeds[a], seeds[b])
                ch = WI.channels(fab.v, fab.w)
                W = ch['prime'] - ch['arch']
                cq = EP.channels_q(fab.v, fab.w)
                say('ENTRY %-9g %-9g  G=%+.12f  control=%+.12f  (%.1f s)'
                    % (a, b, W, cq['places'], time.time() - t0))
                bank(dict(kind='offdiagonal', family=label, a=a, b=b, W=W, zero=ch['zero'],
                          pole=ch['pole'], arch=ch['arch'], prime=ch['prime'],
                          control_places=cq['places'], control_arch=cq['arch'], control_finite=cq['finite'],
                          control_pole=cq['pole']))
        say('=== %s COMPLETE' % label)

    # ### the control's diagonal, on its own chain, for the control's own Gram
    say('=== THE CONTROL`S DIAGONAL, ON THE EPSTEIN CHAIN (places side only)')
    for a in aim + lad:
        t0 = time.time()
        f = SQ.autocorrelation(seeds[a])
        cq = EP.channels_q(f.v, f.w)
        say('CTRL-DIAG a=%-9g places=%+.12f  arch=%+.9f  finite=%+.9f  (%.1f s)'
            % (a, cq['places'], cq['arch'], cq['finite'], time.time() - t0))
        bank(dict(kind='control_diagonal', a=a, places=cq['places'], arch=cq['arch'],
                  finite=cq['finite'], pole=cq['pole']))
    out.close()
    say('RUN COMPLETE')
    return 0


if __name__ == '__main__':
    sys.exit(main())
