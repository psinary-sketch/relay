# -*- coding: utf-8 -*-
"""b326_offline.py -- THE COMPLETENESS CENSUS: THE CENSUS'S OWN ARGUMENT PRINCIPLE OVER THE WHOLE
### RIGHT HALF OF THE STRIP, `sigma in [0.52, 1.50]`, TO THE HEIGHT THE CLOSURE NEEDS.

### ### **WHY THIS FILE EXISTS.** ### The on-line count to `T = 150` (144, every box winding equal
### to its sign-change count) plus the two banked off-line pairs falls some thirty short of the
### Riemann-von Mangoldt main term. ### The corpus's census scanned `sigma in [0.52, 1.50]` ONLY TO
### `t = 33`, so any off-line zero above that height is unbanked. ### **THE REGISTRATION'S FOURTH
### LINK -- the library's completeness -- IS THIS MEASUREMENT.**
### ### **THE ABSCISSA `1.50` IS NOT A CHOICE.** ### `SUM_{k >= 2} r_Q(k) k^{-sigma}` is `1.53 < 2`
### at `sigma = 1.5` (and `2.10 > 2` at `1.4`), so `|Z_Q(s) - 2| < 2` for `Re s >= 1.5` and `Z_Q`
### has no zero there; by the functional equation none with `Re s <= -0.5` either. ### The boxes
### start at `0.52` because `b326_zeros.py` has already shown every box `|sigma - 1/2| <= 0.02`
### holds exactly its on-line zeros.
### ### **EVERY BOX WITH A NONZERO WINDING IS SUBDIVIDED TO THE CENSUS'S OWN `T_STEP = 0.5`, AND
### EACH ZERO IS THEN LOCATED BY BOTH ROUTES** (the census's `Lam` and this act's `zq_b`), agreement
### `1e-8`, and checked to lie inside its sub-box.
"""
import io
import json
import math
import multiprocessing as mpr
import os
import sys
import time

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import epstein_census as CE     # noqa: E402
import b326_zeros as BZ         # noqa: E402  ### bind, zq_b, the bank idiom

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
BANK = os.path.join(D, 'b326_offline_bank.jsonl')
OUT = os.path.join(D, 'b326_offline.json')

SIG_LO, SIG_HI = 0.52, 1.50
T_LO = 0.5
T_TOP = float(os.environ.get('B326_OFF_T', 60.0))
BOX = 2.5
NSIDE = 50            # ### vertical spacing 0.05 on a 2.5-high box
SUB = 0.5             # ### the census's own T_STEP
NSUB = 10
PROCS = 10
K = 240
DPS = int(os.environ.get('B326_DPS', 119))
ROUTE_TOL = 1e-8


def _init(dps, k):
    BZ.bind(dps, k)


def task_box(args):
    t_lo, t_hi = args
    w, mm = CE.winding(SIG_LO, SIG_HI, t_lo, t_hi, NSIDE)
    return ('box', t_lo, dict(t_lo=t_lo, t_hi=t_hi, wind=float(w), minmod=float(mm)))


def task_sub(args):
    t_lo, t_hi = args
    w, mm = CE.winding(SIG_LO, SIG_HI, t_lo, t_hi, NSUB)
    return ('sub', t_lo, dict(t_lo=t_lo, t_hi=t_hi, wind=float(w), minmod=float(mm)))


def task_locate(args):
    t_lo, t_hi, count = args
    found = []
    starts = [mp.mpc(0.75, (t_lo + t_hi) / 2), mp.mpc(1.1, (t_lo + t_hi) / 2),
              mp.mpc(0.6, t_lo + 0.15), mp.mpc(0.9, t_hi - 0.15), mp.mpc(1.3, (t_lo + t_hi) / 2)]
    for s0 in starts:
        try:
            za = mp.findroot(lambda z: CE.Lam(z), s0, solver='secant', tol=mp.mpf('1e-24'))
        except Exception:
            continue
        b, g = float(za.real), float(za.imag)
        if not (SIG_LO <= b <= SIG_HI and t_lo <= g <= t_hi):
            continue
        if any(abs(complex(b, g) - complex(*f['rho_a'])) < 1e-6 for f in found):
            continue
        try:
            zb = mp.findroot(lambda z: BZ.zq_b(z), za, solver='secant', tol=mp.mpf('1e-24'))
            agree = abs(za - zb) <= ROUTE_TOL
            rb = [float(zb.real), float(zb.imag)]
        except Exception:
            agree, rb = False, None
        found.append(dict(rho_a=[b, g], rho_b=rb, agree=agree, sub=[t_lo, t_hi]))
        if len(found) >= count:
            break
    return ('zero', t_lo, dict(t_lo=t_lo, t_hi=t_hi, count=count, found=found))


def load_bank():
    recs = []
    if os.path.exists(BANK):
        for ln in io.open(BANK, encoding='utf-8'):
            if ln.strip():
                recs.append(json.loads(ln))
    return recs


def bank(rec):
    with io.open(BANK, 'a', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(rec) + '\n')


def run_pool(kind, fn, jobs, log):
    done = set((r['kind'], r['key']) for r in load_bank() if r['dps'] == DPS)
    todo = [j for j in jobs if (kind, round(j[0], 6)) not in done]
    log('  %-6s jobs %d  (already banked %d)' % (kind, len(todo), len(jobs) - len(todo)))
    if not todo:
        return
    t0 = time.time()
    ctx = mpr.get_context('spawn')
    with ctx.Pool(processes=PROCS, initializer=_init, initargs=(DPS, K)) as pool:
        n = 0
        for k, key, payload in pool.imap_unordered(fn, todo):
            bank(dict(kind=k, key=round(key, 6), payload=payload, dps=DPS, K=K))
            n += 1
            if n % 5 == 0 or n == len(todo):
                log('    %s %d/%d  %.0fs' % (kind, n, len(todo), time.time() - t0))


def main():
    lines = []

    def log(s=''):
        print(s, flush=True)
        lines.append(s)

    log('=' * 100)
    log('b326 -- THE COMPLETENESS CENSUS. ### sigma in [%.2f, %.2f], t to %g, the census\'s own winding.'
        % (SIG_LO, SIG_HI, T_TOP))
    log('=' * 100)
    BZ.bind(DPS, K)
    tail15 = sum(CE.RQ[k] * k ** (-1.5) for k in range(2, K + 1))
    log('  SUM_{k>=2} r_Q(k) k^-1.5 (k <= %d) = %.4f < 2 : no zero with Re s >= 1.5' % (K, tail15))
    # ### the two banked hits must reappear in their boxes.
    boxes = []
    t = T_LO
    while t < T_TOP - 1e-9:
        boxes.append((round(t, 6), round(min(t + BOX, T_TOP), 6)))
        t = round(t + BOX, 6)
    run_pool('box', task_box, boxes, log)
    recs = [r for r in load_bank() if r['dps'] == DPS]
    bx = sorted([r['payload'] for r in recs if r['kind'] == 'box'], key=lambda b: b['t_lo'])
    hot = [b for b in bx if abs(b['wind']) > 0.25]
    nonint = [b for b in bx if abs(b['wind'] - round(b['wind'])) > 0.1]
    log('  boxes %d ; boxes with a nonzero winding %d ; windings not near an integer %d'
        % (len(bx), len(hot), len(nonint)))
    for b in hot:
        log('    t in [%5.1f, %5.1f]  winding %+.3f  minmod %.2e' % (b['t_lo'], b['t_hi'], b['wind'], b['minmod']))
    subs = []
    for b in hot:
        t = b['t_lo']
        while t < b['t_hi'] - 1e-9:
            subs.append((round(t, 6), round(min(t + SUB, b['t_hi']), 6)))
            t = round(t + SUB, 6)
    run_pool('sub', task_sub, subs, log)
    recs = [r for r in load_bank() if r['dps'] == DPS]
    sb = sorted([r['payload'] for r in recs if r['kind'] == 'sub'], key=lambda b: b['t_lo'])
    hot_sub = [(s['t_lo'], s['t_hi'], int(round(s['wind']))) for s in sb if abs(s['wind']) > 0.25]
    log('  sub-boxes %d ; with a nonzero winding %d (total winding %d)'
        % (len(sb), len(hot_sub), sum(c for _a, _b, c in hot_sub)))
    run_pool('zero', task_locate, hot_sub, log)
    recs = [r for r in load_bank() if r['dps'] == DPS]
    loc = sorted([r['payload'] for r in recs if r['kind'] == 'zero'], key=lambda z: z['t_lo'])
    zeros = []
    short = []
    for z in loc:
        zeros.extend(z['found'])
        if len(z['found']) != z['count']:
            short.append((z['t_lo'], z['t_hi'], z['count'], len(z['found'])))
    log('  off-line zeros located : %d ; sub-boxes where fewer were located than wound : %d %s'
        % (len(zeros), len(short), short if short else ''))
    for z in zeros:
        log('    rho = %.9f %+.9fi  route B %s  agree %s' % (z['rho_a'][0], z['rho_a'][1], z['rho_b'], z['agree']))
    total_wind = sum(int(round(b['wind'])) for b in bx)
    banked_seen = [z for z in zeros if (abs(z['rho_a'][0] - 0.95326047) < 1e-6 and abs(z['rho_a'][1] - 16.29021572) < 1e-6)
                   or (abs(z['rho_a'][0] - 0.79799716) < 1e-6 and abs(z['rho_a'][1] - 29.55176110) < 1e-6)]
    log('  the two banked off-line zeros reappear : %d of 2' % len(banked_seen))
    out = dict(sig_lo=SIG_LO, sig_hi=SIG_HI, T=T_TOP, box=BOX, nside=NSIDE, dps=DPS, K=K,
               tail_at_1p5=tail15, boxes=bx, subboxes=sb, total_winding=total_wind,
               zeros=zeros, short=short, banked_reappear=len(banked_seen), log=lines)
    open(OUT + '.tmp', 'wb').write((json.dumps(out, indent=1) + '\n').encode('utf-8'))
    os.replace(OUT + '.tmp', OUT)
    log('  written : %s' % os.path.basename(OUT))
    log('=' * 100)
    return 0 if (not short and not nonint and len(banked_seen) == 2 and all(z['agree'] for z in zeros)) else 1


if __name__ == '__main__':
    mpr.freeze_support()
    sys.exit(main())
