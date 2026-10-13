# -*- coding: utf-8 -*-
"""b667_bessel_probe.py -- THE ROUTE'S TERM T3 AT THE RULED PRECISION, MEASURED OVER THE REGION'S HEIGHTS BEFORE ANY ZERO IS COUNTED.

### (R277)(3) fixes Arb balls at 200 bits with the 400-bit rung; the plan (relay data/b667_epstein_plan.txt section 2) takes T3's Bessel
### factors K_{s−½}(π√23 m), m ≤ M(t), from acb.bessel_k. A scratch probe after the author's word found acb.bessel_k's ball useless at order
### ν ≈ 0.2 + 149.3i for x ≈ 105-272 at 200 bits and x ≈ 211-272 at 400 bits, tight at 800. This tool measures it over the region's heights:
### for each t on a grid of [0, 150] and σ ∈ {−0.5, 0.5, 1.5} (the region's edges and the line), each m ≤ M(t) (the plan's M), the absolute
### radius T3's term m carries -- |8 π^s Γ(s)⁻¹| · rad(K_ν(π√23 m)) · Σ_{k|m} |k^ν β_{m/k}^{−ν}| -- at 200, 400, 600 and 800 bits, and the
### precision at which every term's radius is below 2^{−60} (Z_Q is of order one on the region; the plan's rung bar is a relative 2^{−40}).
### No banked zero is read and no value of Z_Q is computed or printed: radii, counts of terms and seconds only.
### Usage: `python -X utf8 tools/b667_bessel_probe.py` -> data/b667_bessel_obstruction.txt (.json). Written by the Write tool at b667.
"""
import io
import json
import math
import os
import sys
import time

from flint import arb, acb, ctx

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PRECS = (200, 400, 600, 800)
SIGMAS = ('-0.5', '0.5', '1.5')
T_GRID = [0.5 * i for i in range(0, 301, 5)]       # ### t = 0, 2.5, ..., 150
BAR = arb(2) ** -60


def M_of(t, prec):
    """the plan's M (section 2): ⌈(π|t|/2 + (prec + 20) ln 2) / (π√23)⌉ + 1."""
    return int(math.ceil((math.pi * abs(t) / 2 + (prec + 20) * math.log(2)) / (math.pi * math.sqrt(23)))) + 1


def worst(sig, t, prec):
    ctx.prec = prec
    s = acb(arb(sig), arb(t))
    nu = s - arb(1) / 2
    pre = abs(8 * acb(arb.pi()) ** s * s.rgamma())
    sq = arb(23).sqrt()
    bad, mx = [], arb(0)
    for m in range(1, M_of(t, 200) + 1):            # ### the terms the 200-bit evaluation needs
        k_ = acb(arb.pi() * sq * m).bessel_k(nu)
        dsum = sum((abs(acb(k) ** nu * acb(sq * (m // k) / 2) ** (-nu)) for k in range(1, m + 1) if m % k == 0), arb(0))
        r = pre * k_.rad() * dsum
        if not (r < BAR):
            bad.append(m)
        mx = max(mx, arb(r.upper()), key=lambda a: a.upper()) if r.is_finite() else arb('inf')
    return bad, mx


def main():
    t0 = time.time()
    rows, L = [], []
    for sig in SIGMAS:
        for t in T_GRID:
            rec = dict(sigma=sig, t=t, M200=M_of(t, 200), by_prec={})
            for p in PRECS:
                bad, mx = worst(sig, t, p)
                rec['by_prec'][p] = dict(bad_m=bad, max_rad=mx.str(3, radius=False))
            rec['first_clean'] = next((p for p in PRECS if not rec['by_prec'][p]['bad_m']), None)
            rows.append(rec)
    ctx.prec = 200
    hdr = ['b667 -- THE ROUTE`S TERM T3 AT THE RULED PRECISION, OVER THE REGION`S HEIGHTS (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
           '',
           '### rows are (σ, t) grid points; each prints M (the plan`s, at 200 bits), the m whose T3 term carries an absolute radius at or above',
           '### 2^-60 at 200 / 400 / 600 / 800 bits, and the first precision at which none does. acb.bessel_k (python-flint 0.9.0); no zero read,',
           '### no value of Z_Q computed.', '']
    for r in rows:
        L.append('  σ %4s  t %5.1f  M %2d | 200: %-28s | 400: %-22s | 600: %-14s | 800: %-10s | first clean %s' % (
            r['sigma'], r['t'], r['M200'], r['by_prec'][200]['bad_m'] or 'clean', r['by_prec'][400]['bad_m'] or 'clean',
            r['by_prec'][600]['bad_m'] or 'clean', r['by_prec'][800]['bad_m'] or 'clean', r['first_clean'] or '### ABOVE 800'))
    def lowest(p):
        ts = [r['t'] for r in rows if r['by_prec'][p]['bad_m']]
        return min(ts) if ts else None
    S = ['', '### THE LOWEST HEIGHT ON THE GRID WHERE A TERM IS NOT ENCLOSED BELOW 2^-60: at 200 bits %s ; at 400 bits %s ; at 600 bits %s ; '
         'at 800 bits %s.' % (lowest(200), lowest(400), lowest(600), lowest(800)),
         '### ### **GRID POINTS %d ; CLEAN AT 400 BITS %d ; CLEAN ONLY ABOVE 400 %d ; NOT CLEAN AT 800 %d ; %.0f s.**' % (
             len(rows), sum(1 for r in rows if r['first_clean'] in (200, 400)), sum(1 for r in rows if r['first_clean'] in (600, 800)),
             sum(1 for r in rows if r['first_clean'] is None), time.time() - t0)]
    out = hdr + L + S
    p = os.path.join(D, 'b667_bessel_obstruction.txt')
    open(p + '.tmp', 'wb').write((NL.join(out) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    q = os.path.join(D, 'b667_bessel_obstruction.json')
    open(q + '.tmp', 'wb').write((json.dumps(dict(rows=rows), indent=1) + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    print(NL.join(S))


def readings600():
    """(R277)(3a): the readings at all grid points at 600 bits, appended beneath data/b667_bessel_obstruction.txt from its own .json
    (the measurement of main(), not re-run); additive -- the bank's earlier lines are not touched."""
    p = os.path.join(D, 'b667_bessel_obstruction.txt')
    old = io.open(p, encoding='utf-8').read()
    if 'THE READINGS AT 600 BITS' in old:
        sys.exit('### THE 600-BIT READINGS ARE ALREADY BENEATH THE BANK -- NOTHING WRITTEN')
    rows = json.load(io.open(os.path.join(D, 'b667_bessel_obstruction.json'), encoding='utf-8'))['rows']
    L = ['', '### DATED, 2026-10-13, under (R277)(3a) (the author`s word on the Bessel prompt, relay data/b667_author_answers.txt): THE READINGS AT '
         '600 BITS AT ALL %d GRID POINTS, from this bank`s .json (the same measurement): rows are (σ, t); the m not enclosed below 2^-60 and the '
         'largest absolute radius any term m ≤ M carries.' % len(rows)]
    for r in rows:
        x = r['by_prec']['600']
        L.append('  σ %4s  t %5.1f  M %2d | 600: %-6s | largest radius %s' % (r['sigma'], r['t'], r['M200'], x['bad_m'] or 'clean', x['max_rad']))
    n_clean = sum(1 for r in rows if not r['by_prec']['600']['bad_m'])
    L.append('### ### **AT 600 BITS: GRID POINTS %d ; ENCLOSED BELOW 2^-60 AT EVERY TERM %d ; NOT %d.**' % (len(rows), n_clean, len(rows) - n_clean))
    b = (old.rstrip(NL) + NL + NL.join(L) + NL).encode('utf-8')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'readings600':
        readings600()
    else:
        main()
