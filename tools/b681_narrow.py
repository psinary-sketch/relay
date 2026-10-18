# -*- coding: utf-8 -*-
"""b681_narrow.py -- Q0'S 163 POINTS NARROWED FROM b671'S HALF-WIDTH 1e-24 TO THE MEASURED WIDTH'S TARGET, IN RESUMABLE FOREGROUND PARTS,
under (R291)(5)-(7) on the author's word on the plan (relay data/b681_narrow_plan.txt).

### The certification forms are b671's, IMPORTED from tools/b671_narrow.py and unchanged (its carried segment and Bessel factor set into
### b667's certify by name at its import): (M-on) the certified sign change of Λ_Q(½ + it) on the line, the interval halved on the certified
### sign (b671 :180 sign_at, :196 narrow_on's loop, re-written here for the new width and start); (M-off) the square split at its centre into
### four quarters, each quarter's count by the argument principle over 4 sides × SEGS_PER_SIDE segments (b667 :284 edge_arg, b671 :90
### segment, :148 square_count), the quarter at count 1 kept, and at a depth whose quarter cannot be read the split lines offset by a third
### of that depth's half-width in the coordinate whose line meets the zero, one offset per depth (b671 :275 OFFSET_4A, :279 _line_meeting,
### :291 narrow_off_4a). Re-written here in RESUMABLE form: a depth's squares are a GRID; each segment of each side of each square is a UNIT,
### computed by a worker of a process pool and appended to data/b681_narrow_units.jsonl as it lands; a square's count is assembled from its
### 64 units (the sum of their argument balls over 2π) exactly as square_count sums edge_arg's, so the count read is b671's count. A part
### runs the pool until its deadline, terminates and joins it (no process left behind), assembles every complete grid, writes each
### point's state to the additive progress bank data/b681_narrow_progress.txt, and exits; the next part resumes from the two banks.
### The Bessel factor: b671's _bessel (:120) CARRIED here with one counting line -- an evaluation whose term radius stays at or above the bar
### 2^BESSEL_BAR_EXP at the ladder's top is counted (H6) -- and set into b667's certify by name.
### (C1) ζ's zeros n = 1..10 by (M-on) on Λ(s) = π^{−s/2} Γ(s/2) ζ(s), each start [γ ± 1e-24] about acb.zeta_zero(n)'s midpoint, narrowed to
### W by the same loop, the final interval printed containing the same call's ball. (C2) planted: the midpoint between Q0's adjacent on-line
### zeros ON 0 and ON 1, [m ± 1e-24], which the sign change must refuse (NO SIGN CHANGE).
### Routes, each one foreground run under 540 s: `verify` (the hash chain from b671's bank, printed, nothing written); `online` (C1, C2 and
### the 146 on-line points); `part` (one part of the off-line points); `status` (the state, nothing written); `bank` (data/b681_narrow.txt,
### data/b681_narrow_controls.txt, data/b681_epstein_zeros_narrowed.json.gz and its hashes bank chaining from b671's, the units file gzipped
### under its own name with its LF hashes in data/b681_large_banks.txt). No lean; no kernel file read; b667's and b671's banks read and never
### written. Written by the Write tool at b681, committed alone before any run.
"""
import gzip
import hashlib
import io
import json
import multiprocessing as mpr
import os
import sys
import time

from flint import arb, acb, ctx

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b671_narrow as N               # noqa: E402  ### imported unedited: the carried segment and Bessel factor, the sign, the (4a) rule
CERT = N.CERT

# ================================================================================ THE PLAN'S CONSTANTS (relay data/b681_narrow_plan.txt)
W = '1e-30'                        # ### the target half-width (plan == 1: h_tol(64) 3.162e-28, two decimal orders below, to the power of ten)
H_START = '1e-24'                  # ### b671's half-width, the start (its bank's h)
HALVINGS = 20                      # ### 1e-24 / 2^20 = 9.54e-31 <= 1e-30
PREC = N.PREC                      # ### 200 bits (b667's, b671's)
SEGS = N.SEGS_PER_SIDE             # ### 16 (b671's)
DOUBLINGS_MAX = N.DOUBLINGS_MAX    # ### 16 (b671's)
PROCS = 8                          # ### b667's and b671's, under the 2560 MB hold
HOLD_MB = CERT.HOLD_MB
BUDGET = 470                       # ### a part's pool deadline in seconds; the part's whole run under 540 s (plan == 4)
BESSEL_BAR_EXP = N.BESSEL_BAR_EXP  # ### 2^-200, kept (plan == 2)
DIGITS = 45
C1_N = tuple(range(1, 11))         # ### C1: ζ's lowest ten zeros
IN_GZ = 'b671_epstein_zeros_narrowed.json.gz'
IN_HASHES = ('51d9e6322510b738ba1332b1945bde75363a339f9fd567ea099bb675abd6f804', 'cd3a8ea1dcc7660c66a3b73a08d7c471ee6980e62e5bc4330e92e0c1b40e415b')
PROGRESS = 'b681_narrow_progress.txt'
UNITS = 'b681_narrow_units.jsonl'

D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BAR_MISS = [0]


def say(s=''):
    print(s, flush=True)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


# ================================================================================ THE CARRIED BESSEL FACTOR (b671 :120-:142, one counting line)
def _bessel(m, nu, nu_mid, rad_nu, pre_mid, dsum_mid, prec, s):
    bar = arb(2) ** BESSEL_BAR_EXP
    ladder = sorted({prec} | {p for p in (CERT.PREC, CERT.PREC_RUNG, CERT.PREC_BESSEL) if p >= prec})
    used, km, met = ladder[-1], None, False
    for p in ladder:
        ctx.prec = p
        x = arb.pi() * arb(23).sqrt() * m
        km = acb(x).bessel_k(nu_mid)
        r = pre_mid * km.rad() * dsum_mid
        used = p
        if r.is_finite() and r < bar:
            met = True
            break
    if not met:
        BAR_MISS[0] += 1           # ### b681: the count of H6
    ctx.prec = used
    if rad_nu > 0:
        x = arb.pi() * arb(23).sqrt() * m
        e = (rad_nu * CERT.dK_bound(x, nu)).upper()
        km = km + acb(arb(0, e), arb(0, e))
    if used == CERT.PREC_BESSEL and prec < CERT.PREC_BESSEL:
        CERT.RUNGS.append((m, float(s.real.mid()), float(s.imag.mid()), used))
    ctx.prec = prec
    return km


CERT._bessel = _bessel


# ================================================================================ THE HASH CHAIN AND THE INPUT
def chain():
    """(R291)(6)(v): b671's bank verified against its hashes bank before any point is read: (ok, gz sha256, json sha256, rows)."""
    raw = open(os.path.join(D, IN_GZ), 'rb').read()
    inner = gzip.decompress(raw)
    hg, hj = hashlib.sha256(raw).hexdigest(), hashlib.sha256(inner).hexdigest()
    hb = io.open(os.path.join(D, 'b671_epstein_zeros_narrowed_hashes.txt'), encoding='utf-8').read()
    ok = hg == IN_HASHES[0] and hj == IN_HASHES[1] and IN_HASHES[0] in hb and IN_HASHES[1] in hb
    return ok, hg, hj, json.loads(inner.decode('utf-8'))['rows']


def _append(name, lines):
    with io.open(os.path.join(D, name), 'a', encoding='utf-8', newline=NL) as fh:
        for l in lines:
            fh.write(l + NL)


def _rows(name, tag):
    p = os.path.join(D, name)
    out = []
    if os.path.exists(p):
        for l in io.open(p, encoding='utf-8'):
            if l.startswith(tag + ' '):
                out.append(json.loads(l[len(tag) + 1:]))
    return out


def _part_no():
    return len(_rows(PROGRESS, 'PART')) + 1


# ================================================================================ (M-on), THE LOOP AT THE NEW WIDTH (b671 :196-:228's)
def on_narrow(lam, name, lo, hi):
    ctx.prec = PREC
    a, bb = N.exact(lo).mid(), N.exact(hi).mid()
    sa, ia, la = N.sign_at(lam, a)
    sb, ib, lb = N.sign_at(lam, bb)
    lines = ['  %s depth 0 : t_a %s : %s' % (name, a.str(DIGITS, radius=False), la), '  %s depth 0 : t_b %s : %s' % (name, bb.str(DIGITS, radius=False), lb)]
    if not (ia and ib):
        return dict(reading='UNRESOLVED-AT-DEPTH', depth=0, why='IMAGINARY PART EXCLUDES 0', signs=[sa, sb], lo=a, hi=bb), lines
    if sa is None or sb is None or sa == sb:
        return dict(reading='NO SIGN CHANGE' if (sa is not None and sb is not None) else 'UNRESOLVED-AT-DEPTH', depth=0, signs=[sa, sb],
                    lo=a, hi=bb, why='the endpoints'), lines
    w = arb(W)
    d = 0
    while d < HALVINGS and not ((bb - a) / 2 <= w):
        m = ((a + bb) / 2).mid()
        sm, im_, lm = N.sign_at(lam, m)
        d += 1
        lines.append('  %s depth %d : t_m %s : %s' % (name, d, m.str(DIGITS, radius=False), lm))
        if not im_ or sm is None:
            return dict(reading='UNRESOLVED-AT-DEPTH', depth=d, signs=[sa, sb], lo=a, hi=bb,
                        why='IMAGINARY PART EXCLUDES 0' if not im_ else 'MIDPOINT SIGN UNREAD AT EVERY RUNG'), lines
        if sm == sa:
            a, sa = m, sm
        else:
            bb, sb = m, sm
    return dict(reading='NARROWED' if (bb - a) / 2 <= w else 'UNRESOLVED-AT-DEPTH', depth=d, signs=[sa, sb], lo=a, hi=bb), lines


def online(*a):
    t0 = time.time()
    ok, hg, hj, rows = chain()
    say('b681 -- THE NARROWING, THE ON-LINE PART: C1, C2 AND THE 146 ON-LINE POINTS (%s) ; W %s ; HALVINGS %d ; %d bits' % (utc(), W, HALVINGS, PREC))
    say('### the chain: b671`s bank gz sha256 %s, json %s : %s' % (hg[:16], hj[:16], 'EQUAL TO ITS HASHES BANK' if ok else '### DIFFERS -- NOTHING READ'))
    if not ok:
        return 3
    if _rows(PROGRESS, 'CONTROL') or [r for r in _rows(PROGRESS, 'POINT') if r['kind'] == 'ON']:
        say('### THE ON-LINE PART IS BANKED ALREADY -- NOTHING RUN TWICE')
        return 3
    f0 = CERT.free_mb()
    part = _part_no()
    out = []
    w = arb(W)
    for n in C1_N:
        ctx.prec = PREC
        z = acb.zeta_zero(n)
        g = z.imag
        lo, hi = (g.mid() - arb(H_START)).mid().str(DIGITS + 10, radius=False), (g.mid() + arb(H_START)).mid().str(DIGITS + 10, radius=False)
        res, lines = on_narrow(N.lam_z_at, 'C1 zeta %d' % n, lo, hi)
        inside = bool(res['lo'] <= g.lower() and g.upper() <= res['hi'])
        row = dict(part=part, control='C1', n=n, reading=res['reading'], depth=res['depth'], lo=res['lo'].str(DIGITS + 10, radius=False),
                   hi=res['hi'].str(DIGITS + 10, radius=False), at_width=bool((res['hi'] - res['lo']) / 2 <= w), inside=inside, at=utc())
        out.append('CONTROL ' + json.dumps(row, ensure_ascii=False))
        say('  C1 ζ zero %d : %s at depth %d ; half-width at or below W %s ; contains acb.zeta_zero(%d) %s' % (n, row['reading'], row['depth'],
                                                                                                            row['at_width'], n, inside))
    on = sorted((r for r in rows if r['kind'] == 'ON'), key=lambda r: int(r['idx']))
    ctx.prec = PREC
    m = (N.exact(on[0]['im']) + N.exact(on[1]['im'])) / 2
    res, lines = on_narrow(N.lam_q_at, 'C2 planted', (m - arb(H_START)).mid().str(DIGITS, radius=False), (m + arb(H_START)).mid().str(DIGITS, radius=False))
    row = dict(part=part, control='C2', reading=res['reading'], depth=res['depth'], signs=res['signs'], t=m.mid().str(DIGITS, radius=False),
               lines=lines, refused=res['reading'] == 'NO SIGN CHANGE', at=utc())
    out.append('CONTROL ' + json.dumps(row, ensure_ascii=False))
    say('  C2 planted at the midpoint of ON 0 and ON 1 (t %s) : %s ; signs %s ; REFUSED %s' % (row['t'][:30], row['reading'], row['signs'], row['refused']))
    for l in lines:
        say('    ' + l)
    BAR_MISS[0] = 0
    for r in on:
        ctx.prec = PREC
        t = N.exact(r['im'])
        res, lines = on_narrow(N.lam_q_at, 'ON %s' % r['idx'], (t - arb(r['h'])).mid().str(DIGITS, radius=False), (t + arb(r['h'])).mid().str(DIGITS, radius=False))
        mid = ((res['lo'] + res['hi']) / 2).mid()
        row = dict(part=part, kind='ON', idx=int(r['idx']), form='M-on', reading=res['reading'], depth=res['depth'], signs=res['signs'],
                   re='0.5', im=mid.str(DIGITS, radius=False), lo=res['lo'].str(DIGITS, radius=False), hi=res['hi'].str(DIGITS, radius=False),
                   h=W if res['reading'] == 'NARROWED' else ((res['hi'] - res['lo']) / 2).str(6, radius=False), b671_h=r['h'], at=utc())
        out.append('POINT ' + json.dumps(row, ensure_ascii=False))
    ons = [json.loads(x[6:]) for x in out if x.startswith('POINT ')]
    secs = int(time.time() - t0)
    f1 = CERT.free_mb()
    summ = dict(part=part, route='online', seconds=secs, free_start=f0, free_end=f1, mem_low=min(x for x in (f0, f1) if x is not None) if (f0 or f1) else None,
                bar_misses=BAR_MISS[0], at=utc(), on=dict((k, sum(1 for x in ons if x['reading'] == k)) for k in set(x['reading'] for x in ons)))
    out.append('PART ' + json.dumps(summ, ensure_ascii=False))
    _append(PROGRESS, out)
    say('### PART %d LINE : points touched ON 0-145 (%d) and the controls ; their half-widths now %s ; %d s ; memory low %s MB' % (
        part, len(ons), sorted(set(x['h'] for x in ons)), secs, summ['mem_low']))
    ctl = [json.loads(x[8:]) for x in out if x.startswith('CONTROL ')]
    c1 = sum(1 for c in ctl if c['control'] == 'C1' and c['reading'] == 'NARROWED' and c['inside'] and c['at_width'])
    c2 = [c for c in ctl if c['control'] == 'C2'][0]['refused']
    say('### ### **ON-LINE PART %d : ON %s ; C1 NARROWED, AT W AND INSIDE %d OF %d ; C2 REFUSED %s ; BESSEL BAR MISSES %d ; %d s ; MEMORY LOW %s MB.**' % (
        part, summ['on'], c1, len(C1_N), c2, BAR_MISS[0], secs, summ['mem_low']))
    return 0


# ================================================================================ (M-off), RESUMABLE: GRIDS OF SQUARES, UNITS OF SEGMENTS
def _corners(re, im, h):
    ctx.prec = PREC
    c = acb(re, im)
    hh = arb(h)
    return [c + acb(-hh, -hh), c + acb(hh, -hh), c + acb(hh, hh), c + acb(-hh, hh), c + acb(-hh, -hh)]


def _init():
    ctx.prec = PREC


def task_unit(u):
    """one segment of one side of one square: its argument change by b671's carried segment (b667's edge_arg splitting, b671 :90)."""
    t0 = time.time()
    ctx.prec = PREC
    cs = _corners(u['re'], u['im'], u['h'])
    a, b = cs[u['side']], cs[u['side'] + 1]
    za = a + (b - a) * arb(u['seg']) / SEGS
    zb = a + (b - a) * arb(u['seg'] + 1) / SEGS
    st, cache = CERT._stats(), {}
    BAR_MISS[0] = 0
    v = N.segment(CERT.zq, za, zb, 0, DOUBLINGS_MAX, cache, st)
    ctx.prec = PREC
    return dict(idx=u['idx'], step=u['step'], sq=u['sq'], side=u['side'], seg=u['seg'], arg=None if v is None else v.str(60, radius=True),
                segments=st['segments'], doublings=len(st.get('doublings') or []), rung=st['rung_segments'], unresolved=st['unresolved'][:4],
                bar_misses=BAR_MISS[0], seconds=round(time.time() - t0, 2))


def _state(rows):
    """each off-line point's latest state: from its last POINT row, else b671's row as depth 0 awaiting its start square's count."""
    last = {}
    for r in _rows(PROGRESS, 'POINT'):
        if r['kind'] == 'OFF':
            last[r['idx']] = r
    st = {}
    for r in rows:
        if r['kind'] != 'OFF':
            continue
        i = int(r['idx'])
        st[i] = last.get(i) or dict(kind='OFF', idx=i, form='M-off', reading='START', depth=0, re=r['re'], im=r['im'], h=r['h'], offset=None,
                                    step=-1, b671_h=r['h'])
    return st


def _grids():
    g = {}
    for r in _rows(UNITS, 'GRID'):
        g[(r['idx'], r['step'])] = r
    return g


def _units():
    u = {}
    for r in _rows(UNITS, 'UNIT'):
        k = (r['idx'], r['step'], r['sq'], r['side'], r['seg'])
        if k not in u:
            u[k] = r
    return u


def _next_grid(s):
    """the grid a point's state asks for next: its start square (step 0), or its four quarters, offset where the state carries one."""
    ctx.prec = PREC
    if s['reading'] == 'START':
        return dict(idx=s['idx'], step=0, kind='start', depth=0, squares=[[s['re'], s['im'], s['h']]], offset=None)
    cr, ci, h = N.exact(s['re']), N.exact(s['im']), N.exact(s['h'])
    hq = (h / 2).mid()
    sr, si = cr, ci
    if s.get('offset'):
        sr, si = sr + N.exact(s['offset'][0]), si + N.exact(s['offset'][1])
    grid = [(sr - hq, si - hq), (sr + hq, si - hq), (sr - hq, si + hq), (sr + hq, si + hq)]
    return dict(idx=s['idx'], step=s['step'] + 1, kind='quarters', depth=s['depth'] + 1, offset=s.get('offset'),
                squares=[[gr.mid().str(DIGITS, radius=False), gi.mid().str(DIGITS, radius=False), hq.str(DIGITS, radius=False)] for gr, gi in grid])


def _count(grid, units, j):
    """square j's count from its 64 units, as square_count sums edge_arg's: (count or None, the count ball's print, the units' stats)."""
    ctx.prec = PREC
    tot, segs, dbl, miss = arb(0), 0, 0, 0
    for side in range(4):
        for k in range(SEGS):
            u = units[(grid['idx'], grid['step'], j, side, k)]
            segs += u['segments']
            dbl += u['doublings']
            miss += u['bar_misses']
            if u['arg'] is None:
                return None, 'UNRESOLVED (%s)' % '; '.join(u['unresolved'][:2]), (segs, dbl, miss)
            tot += arb(u['arg'])
    cb = tot / (2 * arb.pi())
    n = cb.unique_fmpz()
    return (int(n) if n is not None and cb.rad() < 0.5 else None), cb.str(8, radius=True), (segs, dbl, miss)


def _advance(s, grid, units, part):
    """a complete grid read into the point's next state, by b671's rules (narrow_off_4a :298-:333), as a POINT row."""
    ctx.prec = PREC
    res = [_count(grid, units, j) for j in range(len(grid['squares']))]
    counts = [c for c, _b, _s in res]
    stats = [s_ for _c, _b, s_ in res]
    row = dict(part=part, kind='OFF', idx=s['idx'], form='M-off', step=grid['step'], counts=counts, balls=[b for _c, b, _s in res],
               segments=sum(x[0] for x in stats), doublings=sum(x[1] for x in stats), bar_misses=sum(x[2] for x in stats), b671_h=s['b671_h'], at=utc())
    if grid['kind'] == 'start':
        ok = counts == [1]
        row.update(reading='READY' if ok else 'UNRESOLVED-AT-DEPTH', depth=0, re=s['re'], im=s['im'], h=s['h'], offset=None,
                   why=None if ok else 'the start square`s count %s, not 1' % counts)
        return row
    if None in counts or counts.count(1) != 1 or sum(counts) != 1:
        if grid.get('offset'):
            row.update(reading='UNRESOLVED-AT-DEPTH', depth=s['depth'], re=s['re'], im=s['im'], h=s['h'], offset=grid['offset'],
                       why='depth %d unread again after its offset, quarters %s' % (grid['depth'], counts))
            return row
        co = N._line_meeting(counts)
        hq = N.exact(grid['squares'][0][2])
        off = (hq / N.OFFSET_4A).mid()
        offs = [off.str(DIGITS, radius=False) if 're' in co else '0', off.str(DIGITS, radius=False) if 'im' in co else '0']
        row.update(reading='NARROWING', depth=s['depth'], re=s['re'], im=s['im'], h=s['h'], offset=offs,
                   why='(4a) at depth %d: quarters %s, the split lines offset by %s in %s' % (grid['depth'], counts, off.str(4, radius=False),
                                                                                         ' and '.join({'re': 'σ', 'im': 't'}[c] for c in co)))
        return row
    k = counts.index(1)
    re_, im_, hq = grid['squares'][k]
    done = N.exact(hq) <= arb(W)
    row.update(reading='NARROWED' if done else 'NARROWING', depth=grid['depth'], re=re_, im=im_, h=W if done else hq, offset=None, quarter=k,
               h_reached=hq)
    return row


def part(*a):
    t0 = time.time()
    ok, hg, hj, rows = chain()
    pn = _part_no()
    say('b681 -- THE NARROWING, OFF-LINE PART %d (%s) ; W %s ; PROCS %d ; THE POOL`S DEADLINE %d s' % (pn, utc(), W, PROCS, BUDGET))
    say('### the chain: b671`s bank gz sha256 %s, json %s : %s' % (hg[:16], hj[:16], 'EQUAL TO ITS HASHES BANK' if ok else '### DIFFERS -- NOTHING READ'))
    if not ok:
        return 3
    f0 = CERT.free_mb()
    say('### host free at start: %s MB ; the hold %d MB' % (f0, HOLD_MB))
    if f0 is None or f0 < HOLD_MB:
        say('### FREE MEMORY BENEATH THE HOLD -- NOTHING RUN')
        return 3
    st, grids, units = _state(rows), _grids(), _units()
    live = [s for s in st.values() if s['reading'] in ('START', 'READY', 'NARROWING')]
    new_grids, tasks = [], []
    for s in sorted(live, key=lambda s: s['idx']):
        g = _next_grid(s)
        if (g['idx'], g['step']) not in grids:
            new_grids.append('GRID ' + json.dumps(g, ensure_ascii=False))
            grids[(g['idx'], g['step'])] = g
        for j, (re_, im_, h_) in enumerate(g['squares']):
            for side in range(4):
                for k in range(SEGS):
                    if (g['idx'], g['step'], j, side, k) not in units:
                        tasks.append(dict(idx=g['idx'], step=g['step'], sq=j, side=side, seg=k, re=re_, im=im_, h=h_))
    if new_grids:
        _append(UNITS, new_grids)
    say('### points live %d %s ; finished or stopped %d ; units to run %d' % (len(live), sorted(s['idx'] for s in live), len(st) - len(live), len(tasks)))
    landed, low, stop_why, touched = 0, f0, 'all units landed', set()
    if tasks:
        pool = mpr.Pool(PROCS, initializer=_init)
        try:
            buf = []
            it = pool.imap_unordered(task_unit, tasks)
            while True:
                left = BUDGET - (time.time() - t0)
                if left <= 0:
                    stop_why = 'the deadline'
                    break
                try:
                    r = it.next(timeout=left)
                except StopIteration:
                    break
                except mpr.TimeoutError:
                    stop_why = 'the deadline'
                    break
                r['part'] = pn
                touched.add(r['idx'])
                buf.append('UNIT ' + json.dumps(r, ensure_ascii=False))
                landed += 1
                units[(r['idx'], r['step'], r['sq'], r['side'], r['seg'])] = r
                if len(buf) >= 32:
                    _append(UNITS, buf)
                    buf = []
                if landed % 128 == 0:
                    f = CERT.free_mb()
                    low = f if (f is not None and (low is None or f < low)) else low
                    if f is not None and f < HOLD_MB:
                        stop_why = 'free memory beneath the hold (%s MB)' % f
                        break
            _append(UNITS, buf)
        finally:
            pool.terminate()
            pool.join()
    out = []
    for s in sorted(live, key=lambda s: s['idx']):
        g = grids[(s['idx'], s['step'] + 1)] if s['reading'] != 'START' else grids[(s['idx'], 0)]
        need = [(g['idx'], g['step'], j, side, k) for j in range(len(g['squares'])) for side in range(4) for k in range(SEGS)]
        if all(x in units for x in need):
            row = _advance(s, g, units, pn)
            out.append('POINT ' + json.dumps(row, ensure_ascii=False))
            say('  OFF %d : %s at depth %d ; counts %s ; h %s%s' % (row['idx'], row['reading'], row['depth'], row['counts'], row['h'][:10],
                                                                 (' ; ' + row['why']) if row.get('why') else ''))
        else:
            say('  OFF %d : grid step %d (depth %d) %d of %d units landed' % (s['idx'], g['step'], g['depth'], sum(1 for x in need if x in units), len(need)))
    f1 = CERT.free_mb()
    low = min(x for x in (low, f1) if x is not None) if (low is not None or f1 is not None) else None
    secs = int(time.time() - t0)
    out.append('PART ' + json.dumps(dict(part=pn, route='part', seconds=secs, units_landed=landed, units_asked=len(tasks), stop=stop_why,
                                         free_start=f0, free_end=f1, mem_low=low, at=utc()), ensure_ascii=False))
    _append(PROGRESS, out)
    stt = _state(rows)
    # ### the navigator's answer on the plan: each part's line -- the part, the points it touched, their current half-widths, the seconds
    # ### and the memory low -- so the run's progress reads from the chat or the progress bank at any time
    say('### PART %d LINE : points touched %s ; their half-widths now %s ; %d s ; memory low %s MB' % (
        pn, sorted(touched), ', '.join('OFF %d %s' % (i, stt[i]['h'][:9]) for i in sorted(touched)) or 'NONE', secs, low))
    say('### ### **OFF-LINE PART %d : UNITS LANDED %d OF %d (%s) ; POINTS NARROWED %d ; LIVE %d ; STOPPED %d ; %d s ; MEMORY LOW %s MB.**' % (
        pn, landed, len(tasks), stop_why, sum(1 for s in stt.values() if s['reading'] == 'NARROWED'),
        sum(1 for s in stt.values() if s['reading'] in ('START', 'READY', 'NARROWING')),
        sum(1 for s in stt.values() if s['reading'] == 'UNRESOLVED-AT-DEPTH'), secs, low))
    return 0


def status(*a):
    ok, hg, hj, rows = chain()
    st = _state(rows)
    parts = _rows(PROGRESS, 'PART')
    say('### parts %d, seconds summed %d ; the longest %s s' % (len(parts), sum(p['seconds'] for p in parts), max([p['seconds'] for p in parts] or [0])))
    for s in sorted(st.values(), key=lambda s: s['idx']):
        say('  OFF %d : %s depth %d h %s' % (s['idx'], s['reading'], s['depth'], s['h'][:12]))
    on = [r for r in _rows(PROGRESS, 'POINT') if r['kind'] == 'ON']
    say('  ON points banked %d' % len(on))


# ================================================================================ THE BANKS (R291)(6)(v), (7)
def _put(name, b):
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def bank(*a):
    """data/b681_narrow.txt (rows are points: final half-width, form, reading, the parts that touched them), data/b681_narrow_controls.txt,
    data/b681_epstein_zeros_narrowed.json.gz with data/b681_epstein_zeros_narrowed_hashes.txt chaining from b671's, and the units file
    gzipped under its own name with its hashes in data/b681_large_banks.txt (the .jsonl left untracked, as b671's run banks were)."""
    ok, hg, hj, rows = chain()
    if not ok:
        say('### THE CHAIN FROM b671`S BANK DOES NOT VERIFY -- NOTHING WRITTEN')
        return 3
    pts = _rows(PROGRESS, 'POINT')
    parts = _rows(PROGRESS, 'PART')
    ctl = _rows(PROGRESS, 'CONTROL')
    touch = {}
    for r in pts:
        touch.setdefault((r['kind'], r['idx']), set()).add(r['part'])
    for u in _rows(UNITS, 'UNIT'):
        touch.setdefault(('OFF', u['idx']), set()).add(u.get('part'))
    last = {}
    for r in pts:
        last[(r['kind'], r['idx'])] = r
    out_rows, L = [], []
    for r in sorted(rows, key=lambda r: (r['kind'], int(r['idx']))):
        k = (r['kind'], int(r['idx']))
        x = last.get(k)
        if x is None:
            L.append('  %-3s %-3d ### NO ROW -- NOT RUN' % k)
            continue
        form = 'M-on' if r['kind'] == 'ON' else 'M-off'
        L.append('  %-3s %-3d form %-5s (b671 %s) ; %-19s ; half-width %s ; depth %d ; parts %s' % (
            k[0], k[1], x['form'], form, x['reading'], x['h'], x['depth'], sorted(p for p in touch.get(k, ()) if p is not None)))
        out_rows.append(dict(kind=r['kind'], idx=r['idx'], re=x['re'], im=x['im'], h=x['h'], count=1, reading=x['reading'], depth=x['depth'],
                             form=x['form'], b671_h=r['h']))
    nar = sum(1 for o in out_rows if o['reading'] == 'NARROWED')
    same = all(o['form'] == ('M-on' if o['kind'] == 'ON' else 'M-off') for o in out_rows)
    secs = [p['seconds'] for p in parts]
    miss = sum(p.get('bar_misses', 0) for p in parts) + sum(u.get('bar_misses', 0) for u in _rows(UNITS, 'UNIT'))
    head = ['b681 -- THE NARROWING, BANKED (%s): rows are points -- kind, index, the certification form (b671`s beside it), the reading, the final '
            'half-width, the depth from 1e-24, the parts that touched it' % utc(), '',
            '### the chain: b671`s bank gz sha256 %s and json %s, EQUAL to data/b671_epstein_zeros_narrowed_hashes.txt :2-:3, read before any point.' % (hg, hj), '']
    tail = ['', '### the parts: %d ; seconds %s ; summed %d ; the longest %d ; above 600 s %d.' % (len(parts), secs, sum(secs), max(secs or [0]),
                                                                                                  sum(1 for s in secs if s > 600)),
            '### ### **POINTS %d ; NARROWED TO %s %d OF 163 ; FORMS AS b671`S %s ; PARTS %d, %d s ; THE LONGEST PART %d s ; BESSEL BAR MISSES %d.**' % (
                len(out_rows), W, nar, same, len(parts), sum(secs), max(secs or [0]), miss)]
    _put('b681_narrow.txt', (NL.join(head + L + tail) + NL).encode('utf-8'))
    C = ['b681 -- THE CONTROLS, (R291)(6)(vi) (%s): rows are control points with their reading' % utc(), '']
    for c in ctl:
        if c['control'] == 'C1':
            C.append('  C1 ζ zero %d : %s at depth %d ; half-width at or below %s %s ; [%s, %s] contains acb.zeta_zero(%d) %s' % (
                c['n'], c['reading'], c['depth'], W, c['at_width'], c['lo'][:40], c['hi'][:40], c['n'], c['inside']))
        else:
            C.append('  C2 planted at t %s (the midpoint of ON 0 and ON 1) : %s ; signs %s ; REFUSED %s' % (c['t'][:40], c['reading'], c['signs'], c['refused']))
            C += ['      ' + l for l in c['lines']]
    c1 = sum(1 for c in ctl if c['control'] == 'C1' and c['reading'] == 'NARROWED' and c['inside'] and c['at_width'])
    c2 = any(c['control'] == 'C2' and c['refused'] for c in ctl)
    C += ['', '### ### **C1 %d OF %d NARROWED TO %s AND INSIDE ; C2 REFUSED %s.**' % (c1, len(C1_N), W, c2)]
    _put('b681_narrow_controls.txt', (NL.join(C) + NL).encode('utf-8'))
    js = (json.dumps(dict(w=W, h0=H_START, halvings=HALVINGS, prec=PREC, source='data/%s (b671), narrowed by tools/b681_narrow.py' % IN_GZ,
                          rows=out_rows), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    buf = io.BytesIO()
    with gzip.GzipFile(filename='', mode='wb', fileobj=buf, mtime=0) as gz:
        gz.write(js)
    gzb = buf.getvalue()
    _put('b681_epstein_zeros_narrowed.json.gz', gzb)
    H = ['b681 -- THE NARROWED LIST`S HASHES (rows are files): the JSON as written, then gzipped (mtime 0); the chain from b671`s',
         'data/b681_epstein_zeros_narrowed.json (inside the .gz) sha256 %s bytes %d' % (hashlib.sha256(js).hexdigest(), len(js)),
         'data/b681_epstein_zeros_narrowed.json.gz sha256 %s bytes %d ; CR LF pairs in the .gz %d' % (hashlib.sha256(gzb).hexdigest(), len(gzb), gzb.count(b'\r\n')),
         'chains from: data/b671_epstein_zeros_narrowed.json.gz sha256 %s, its JSON %s (data/b671_epstein_zeros_narrowed_hashes.txt :2-:3)' % (hg, hj)]
    _put('b681_epstein_zeros_narrowed_hashes.txt', (NL.join(H) + NL).encode('utf-8'))
    up = os.path.join(D, UNITS)
    ub = open(up, 'rb').read() if os.path.exists(up) else b''
    buf = io.BytesIO()
    with gzip.GzipFile(filename='', mode='wb', fileobj=buf, mtime=0) as gz:
        gz.write(ub)
    ugz = buf.getvalue()
    _put(UNITS + '.gz', ugz)
    LB = ['b681 -- THE RUN`S LARGE BANKS, GZIPPED UNDER THEIR OWN NAMES (%s): rows are banks -- the uncompressed bytes and sha256, the gz bytes and sha256' % utc(),
          '', '  data/%s.gz | uncompressed %d bytes, sha256 %s | gz %d bytes, sha256 %s | CR LF pairs in the .gz %d' % (
              UNITS, len(ub), hashlib.sha256(ub).hexdigest(), len(ugz), hashlib.sha256(ugz).hexdigest(), ugz.count(b'\r\n')),
          '  data/b681_epstein_zeros_narrowed.json.gz | uncompressed %d bytes, sha256 %s | gz %d bytes, sha256 %s | CR LF pairs in the .gz %d' % (
              len(js), hashlib.sha256(js).hexdigest(), len(gzb), hashlib.sha256(gzb).hexdigest(), gzb.count(b'\r\n')),
          '', '### the .jsonl stays untracked on disk; the root names this LF bank and the hashes bank, not the .gz files (data/b680_rules.txt row (1)).']
    _put('b681_large_banks.txt', (NL.join(LB) + NL).encode('utf-8'))
    say(tail[-1])
    say(C[-1])
    return 0


if __name__ == '__main__':
    fn = {'verify': lambda *a: say('### the chain: %s' % (chain()[:3],)), 'online': online, 'part': part, 'status': status,
          'bank': bank}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b681_narrow.py verify | online | part | status | bank')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
