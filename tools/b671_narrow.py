# -*- coding: utf-8 -*-
"""b671_narrow.py -- Q0'S 163 POINTS NARROWED TO THE MAP'S INPUT WIDTH, under (R281)(3)-(5) on the author's word on the plan (relay
data/b671_narrow_plan.txt, relay data/b671_author_answers.txt).

### (M-on): each on-line point's t-interval on σ = ½, from b667's square [im ± 1e-12], certified by a sign change of the completed function
###   Λ_Q(½ + it) = (2π/√23)^{−s} Γ(s) Z_Q(s) -- real on the line (plan section 2) -- both endpoint balls excluding 0 with opposite signs, b667's
###   count 1 making it the square's one zero; then halved on the certified sign to half-width W (depth DEPTH). At every sign read the imaginary
###   part of the completed function's ball is printed and must contain 0 (the author's word on the plan): a ball excluding 0 there stops the
###   point at UNRESOLVED with the line kept. σ carried as the rational ½.
### (M-off): each off-line point's square, from b667's [re ± 1e-12] × [im ± 1e-12] at count 1, split at its centre into four quarters, each
###   quarter's count by b667's segment form; the quarter at count 1 kept, the three at 0 printed; to half-width W. A quarter whose count cannot
###   be read: the grid offset by an eighth of the half-width, printed, once; then UNRESOLVED-AT-DEPTH d.
### b667's square_count (tools/b667_epstein_certify.py :301-:315) holds SQ_SEG and DEPTH_SQ as module constants and is CARRIED here with both
###   lifted to this head (SEGS_PER_SIDE, DOUBLINGS_MAX); its segment (:258-:281) is CARRIED with one recording line (each halving's depth and
###   ends); edge_arg looks segment up in its own module, so the carried segment is set there by name (CERT.segment) and edge_arg, zq, _pt,
###   _accepted, _ball, logg_q, logg_z and the rungs are imported unedited. `python tools/b671_narrow.py diff` banks the carried code's diff.
### (C1) ζ's three lowest zeros by (M-on) on Λ(s) = π^{−s/2} Γ(s/2) ζ(s), the start intervals from acb.zeta_zero(n)'s balls widened to ± 1e-12
###   about their midpoints, the final interval printed containing the same call's ball. (C2) planted: ON idx 0 shifted by 10 · 1e-12 (NO SIGN
###   CHANGE), OFF idx 0 shifted by 1e-9 in σ (count 0).
### Usage: `run1` -- C1, C2, the 146 on-line points -> data/b671_narrow_run1.json, data/b671_narrow_run1.txt; `run2` -- the 17 off-line
### points on PROCS processes, each finished point appended to data/b671_narrow_run2_points.jsonl as it lands -> data/b671_narrow_run2.txt;
### `bank` -> data/b671_epstein_zeros_narrowed.json.gz, data/b671_epstein_zeros_narrowed_hashes.txt, data/b671_narrow_log.txt (.json).
### No lean; no kernel file read; b667's and b326's banks read and never written. Nothing here is about ζ but C1. Written by the Write tool at
### b671, read back whole before it runs.
"""
import difflib
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
import b667_epstein_certify as CERT   # noqa: E402  ### imported unedited; its main runs only under __main__

# ================================================================================ THE PLAN'S CONSTANTS (relay data/b671_narrow_plan.txt)
W = '1e-24'                        # ### the target half-width (plan section 1: 1e-18 / 6.1e3 = 1.6e-22, two decimal orders below)
H0 = '1e-12'                       # ### b667's squares' half-width, the start
DEPTH = 40                         # ### halvings from H0 to W (2^40 = 1.1e12)
PREC = CERT.PREC                   # ### 200 bits (b667's)
PREC_RUNG = CERT.PREC_RUNG         # ### the 400 rung (b667's); the Bessel factor's own 600-bit rung inside zq (CERT.PREC_BESSEL)
SEGS_PER_SIDE = 16                 # ### the starting segments per side of a quarter (the navigator's note, (2)); b667's SQ_SEG was 4
DOUBLINGS_MAX = 16                 # ### the printed ceiling of a segment's halvings (b667's DEPTH_SQ), then the 400 rung once, then UNRESOLVED
C2_ON_SHIFT = '1e-11'              # ### C2: ON idx 0's interval shifted by 10 · H0
C2_OFF_SHIFT = '1e-9'              # ### C2: OFF idx 0's square shifted in σ
C1_N = (1, 2, 3)                   # ### C1: ζ's lowest three zeros, by acb.zeta_zero(n)
PROCS = CERT.PROCS                 # ### 8 (b667's, under the 2560 MB hold)
BESSEL_BAR_EXP = -200              # ### the author's word on the Bessel bar: (3a)'s acceptance lifted from b667's -60 (certify :49). Its consumer: a
#                                  ### sign or a segment enclosure at half-width W, |Z_Q'|·W at the smallest |Z_Q'| b667's banks hold (3.895 at
#                                  ### 0.7 + 40.25i, data/b667_ball_obstruction.txt :3) = 3.9e-24; a term accepted below 2^-200 (6.2e-61), far beneath
#                                  ### two decimal orders under it. The ladder 200 -> 400 -> 600 bits unchanged. b667's certificates stand on their bar.
DIGITS = 45                        # ### decimal digits of a printed centre
Q0_CERT = 'b667_epstein_zeros_certified.json.gz'

D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
OUT = []


def say(s=''):
    OUT.append(s)
    print(s, flush=True)


def bs(x, n=15):
    """a ball printed as its midpoint and its radius (b671 defect (e): a 15-digit `[+/- r]` print hid a ball that excludes 0)."""
    return 'mid %s rad %s' % (x.mid().str(n, radius=False), x.rad().str(3, radius=False))


def exact(s):
    """an exact dyadic point at the working precision from a decimal string."""
    return arb(s).mid()


# ================================================================================ THE CARRIED COUNT (b667's square_count and segment)
def segment(F, za, zb, depth, maxd, cache, st):
    """the argument change of F along [za, zb] as an arb, or None (UNRESOLVED, its location in st['unresolved'])."""
    ctx.prec = PREC
    e = F(CERT._ball(za, zb), PREC)
    ctx.prec = PREC
    if not CERT._accepted(e):
        if depth < maxd:
            st.setdefault('doublings', []).append((depth + 1, za.mid().str(DIGITS, radius=False), zb.mid().str(DIGITS, radius=False)))   # ### b671: the record
            zm = (za + zb) / 2
            a = segment(F, za, zm, depth + 1, maxd, cache, st)
            if a is None:
                return None
            b = segment(F, zm, zb, depth + 1, maxd, cache, st)
            return None if b is None else a + b
        e = F(CERT._ball(za, zb), PREC_RUNG)
        ctx.prec = PREC
        st['rung_segments'] += 1
        if not CERT._accepted(e):
            st['unresolved'].append('[%s, %s]' % (za.mid().str(12, radius=False), zb.mid().str(12, radius=False)))
            return None
    st['segments'] += 1
    st['max_depth'] = max(st['max_depth'], depth)
    fa, fb = CERT._pt(F, za, cache), CERT._pt(F, zb, cache)
    ctx.prec = PREC
    return (fb / fa).arg()


CERT.segment = segment             # ### edge_arg reads `segment` from its own module: the carried one, set by name


def _bessel(m, nu, nu_mid, rad_nu, pre_mid, dsum_mid, prec, s):
    """(3a)-(3b): the factor K_ν(π√23 m) on the ball nu: K at the centre nu_mid at the lowest precision of the ladder at which the term's
    radius there is below 2^BESSEL_BAR_EXP (x formed at that precision), plus rad_nu · sup|∂_ν K|; every factor taken at 600 logged."""
    bar = arb(2) ** BESSEL_BAR_EXP
    ladder = sorted({prec} | {p for p in (CERT.PREC, CERT.PREC_RUNG, CERT.PREC_BESSEL) if p >= prec})
    used, km = ladder[-1], None
    for p in ladder:
        ctx.prec = p
        x = arb.pi() * arb(23).sqrt() * m
        km = acb(x).bessel_k(nu_mid)
        r = pre_mid * km.rad() * dsum_mid
        used = p
        if r.is_finite() and r < bar:
            break
    ctx.prec = used
    if rad_nu > 0:
        x = arb.pi() * arb(23).sqrt() * m
        e = (rad_nu * CERT.dK_bound(x, nu)).upper()
        km = km + acb(arb(0, e), arb(0, e))
    if used == CERT.PREC_BESSEL and prec < CERT.PREC_BESSEL:
        CERT.RUNGS.append((m, float(s.real.mid()), float(s.imag.mid()), used))
    ctx.prec = prec
    return km


CERT._bessel = _bessel             # ### zq reads `_bessel` from its own module: the carried one, its bar lifted, set by name (the author's word)


def square_count(F, re, im, h):
    """the count of zeros of F in the square [re ± h] × [im ± h]: (count or None, the count ball, stats)."""
    ctx.prec = PREC
    c = acb(re, im)
    hh = arb(h)
    cs = [c + acb(-hh, -hh), c + acb(hh, -hh), c + acb(hh, hh), c + acb(-hh, hh), c + acb(-hh, -hh)]
    st, cache, tot = CERT._stats(), {}, arb(0)
    for i in range(4):
        d = CERT.edge_arg(F, cs[i], cs[i + 1], SEGS_PER_SIDE, DOUBLINGS_MAX, st, cache)
        if d is None:
            return None, None, st
        tot += d
    cb = tot / (2 * arb.pi())
    n = cb.unique_fmpz()
    return (int(n) if n is not None and cb.rad() < 0.5 else None), cb, st


# ================================================================================ (M-on): THE SIGN OF THE COMPLETED FUNCTION ON THE LINE
def lam_q_at(t, prec):
    ctx.prec = prec
    s = acb(arb(1) / 2, t)
    return CERT.logg_q(s).exp() * CERT.zq(s, prec)


def lam_z_at(t, prec):
    ctx.prec = prec
    s = acb(arb(1) / 2, t)
    return CERT.logg_z(s).exp() * s.zeta()


def sign_at(lam, t):
    """the certified sign of the completed function at ½ + it: (sign or None, imaginary part contains 0, the printed line); 200 bits, then the
    400 rung where the real ball contains 0. A ball whose imaginary part excludes 0 is not a value on the line: its sign is not read."""
    for p in (PREC, PREC_RUNG):
        v = lam(t, p)
        im0 = v.imag.contains(0)
        line = 'Re %s ; Im %s ; Im contains 0 %s ; at %d bits' % (bs(v.real), bs(v.imag, 6), im0, p)
        if not im0:
            return None, False, line
        if v.real > 0:
            return 1, True, line
        if v.real < 0:
            return -1, True, line
    return None, True, line


def narrow_on(lam, name, t0, h0, lo=None, hi=None):
    """(M-on) from [t0 − h0, t0 + h0] -- or from a last certified interval [lo, hi] (the author's word on the Bessel bar: the 9 re-run from
    there, not from the start) -- to half-width W: returns the row's reading and the depth lines."""
    ctx.prec = PREC
    if lo is not None:
        a, bb = exact(lo), exact(hi)
    else:
        a, bb = exact(t0) - arb(h0), exact(t0) + arb(h0)
    a, bb = a.mid(), bb.mid()
    lines = []
    sa, ia, la = sign_at(lam, a)
    sb, ib, lb = sign_at(lam, bb)
    lines += ['  %s depth 0 : t_a %s : %s' % (name, a.str(DIGITS, radius=False), la), '  %s depth 0 : t_b %s : %s' % (name, bb.str(DIGITS, radius=False), lb)]
    if not (ia and ib):
        return dict(reading='UNRESOLVED-AT-DEPTH', depth=0, why='IMAGINARY PART EXCLUDES 0', signs=[sa, sb], lo=a, hi=bb), lines
    if sa is None or sb is None or sa == sb:
        return dict(reading='NO SIGN CHANGE' if (sa is not None and sb is not None) else 'UNRESOLVED-AT-DEPTH', depth=0, signs=[sa, sb],
                    lo=a, hi=bb, why='the endpoints'), lines
    w = arb(W)
    d = 0
    while d < DEPTH and not ((bb - a) / 2 <= w):
        m = ((a + bb) / 2).mid()
        sm, im_, lm = sign_at(lam, m)
        d += 1
        lines.append('  %s depth %d : t_m %s : %s' % (name, d, m.str(DIGITS, radius=False), lm))
        if not im_ or sm is None:
            return dict(reading='UNRESOLVED-AT-DEPTH', depth=d, signs=[sa, sb], lo=a, hi=bb,
                        why='IMAGINARY PART EXCLUDES 0' if not im_ else 'MIDPOINT SIGN UNREAD AT EVERY RUNG'), lines
        if sm == sa:
            a, sa = m, sm
        else:
            bb, sb = m, sm
    return dict(reading='NARROWED', depth=d, signs=[sa, sb], lo=a, hi=bb), lines


# ================================================================================ (M-off): THE QUARTERS BY THE COUNT
def narrow_off(name, re0, im0, h0):
    """(M-off) from the square [re0 ± h0] × [im0 ± h0] to half-width W: returns the reading and the depth lines."""
    ctx.prec = PREC
    cr, ci, h = exact(re0), exact(im0), arb(h0)
    w = arb(W)
    lines, d, offset_used = [], 0, False
    while d < DEPTH and not (h <= w):
        hq = (h / 2).mid()
        grid = [(cr - hq, ci - hq), (cr + hq, ci - hq), (cr - hq, ci + hq), (cr + hq, ci + hq)]
        got = []
        for gr, gi in grid:
            n, cb, st = square_count(CERT.zq, gr.mid().str(DIGITS, radius=False), gi.mid().str(DIGITS, radius=False), hq.str(DIGITS, radius=False))
            got.append((n, cb, st, gr, gi))
        d += 1
        counts = [x[0] for x in got]
        lines.append('  %s depth %d : half-width %s ; quarters %s ; segments %s ; doublings %s' % (
            name, d, hq.str(4, radius=False), counts, [x[2]['segments'] for x in got], [len(x[2].get('doublings') or []) for x in got]))
        for n, cb, st, gr, gi in got:
            for dd, za, zb in (st.get('doublings') or [])[:200]:
                lines.append('      doubling at depth %d : [%s, %s]' % (dd, za, zb))
        if None in counts or counts.count(1) != 1 or sum(counts) != 1:
            if offset_used:
                return dict(reading='UNRESOLVED-AT-DEPTH', depth=d, re=cr, im=ci, h=h, counts=counts), lines
            off = (h / 8).mid()
            lines.append('  %s depth %d : a quarter unread or the counts %s not one 1 and three 0 -- the grid offset by %s (an eighth of the '
                         'half-width), once' % (name, d, counts, off.str(4, radius=False)))
            offset_used = True
            cr, ci = (cr + off).mid(), (ci + off).mid()
            d -= 1
            continue
        k = counts.index(1)
        cr, ci, h = got[k][3].mid(), got[k][4].mid(), hq
    return dict(reading='NARROWED' if h <= w else 'UNRESOLVED-AT-DEPTH', depth=d, re=cr, im=ci, h=h, counts=[1]), lines


def task_off(r):
    t0 = time.time()
    res, lines = narrow_off('OFF %d' % r['idx'], r['re'], r['im'], r['h'])
    return dict(kind='OFF', idx=r['idx'], reading=res['reading'], depth=res['depth'], re=res['re'].str(DIGITS, radius=False),
                im=res['im'].str(DIGITS, radius=False), h=W if res['reading'] == 'NARROWED' else res['h'].str(DIGITS, radius=False),
                count=1, seconds=int(time.time() - t0), lines=lines, b667=dict(re=r['re'], im=r['im'], h=r['h']))


def rows667():
    return json.loads(gzip.decompress(open(os.path.join(D, Q0_CERT), 'rb').read()).decode('utf-8'))['rows']


def put(name, text):
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)


# ================================================================================ THE RUNS
def run1():
    t_start = time.time()
    say('b671 -- THE NARROWING, RUN 1: C1, C2 AND THE 146 ON-LINE POINTS (%s) ; W %s ; DEPTH %d ; %d / %d bits' % (
        time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), W, DEPTH, PREC, PREC_RUNG))
    say('### host free at start: %s MB' % CERT.free_mb())
    res = dict(c1=[], c2={}, on=[])
    say('== C1: ζ`s lowest three zeros by (M-on) on Λ(s) = π^{−s/2} Γ(s/2) ζ(s), the start from acb.zeta_zero(n)')
    for n in C1_N:
        ctx.prec = PREC
        z = acb.zeta_zero(n)
        t0 = z.imag.mid().str(DIGITS, radius=False)
        say('  C1 n = %d : acb.zeta_zero(%d) = %s ; the start [%s ± %s]' % (n, n, bs(z.imag, 30), t0, H0))
        r, lines = narrow_on(lam_z_at, 'C1 n=%d' % n, t0, H0)
        for l in lines:
            say(l)
        ctx.prec = PREC
        ref = acb.zeta_zero(n).imag
        inside = bool(r['lo'] <= ref.lower()) and bool(ref.upper() <= r['hi'])
        say('  C1 n = %d : %s at depth %d ; [%s, %s] ; the call`s ball inside it %s' % (n, r['reading'], r['depth'], r['lo'].str(DIGITS, radius=False),
                                                                                    r['hi'].str(DIGITS, radius=False), inside))
        res['c1'].append(dict(n=n, reading=r['reading'], depth=r['depth'], inside=inside))
    rows = rows667()
    on = sorted((r for r in rows if r['kind'] == 'ON'), key=lambda r: r['idx'])
    off = sorted((r for r in rows if r['kind'] == 'OFF'), key=lambda r: r['idx'])
    if len(on) != 146 or len(off) != 17:
        sys.exit('### b667`s ROWS ARE NOT 146 ON AND 17 OFF -- STOPPED')
    say('== C2: planted')
    r0 = on[0]
    ctx.prec = PREC
    t_shift = (exact(r0['im']) + arb(C2_ON_SHIFT)).mid().str(DIGITS, radius=False)
    r, lines = narrow_on(lam_q_at, 'C2 ON idx 0 shifted', t_shift, H0)
    for l in lines:
        say(l)
    say('  C2 ON idx 0 shifted by %s : %s' % (C2_ON_SHIFT, r['reading']))
    q0 = off[0]
    ctx.prec = PREC
    re_s = (exact(q0['re']) + arb(C2_OFF_SHIFT)).mid().str(DIGITS, radius=False)
    n, cb, st = square_count(CERT.zq, re_s, q0['im'], H0)
    say('  C2 OFF idx 0 shifted by %s in σ : count %s ; ball %s ; segments %d ; doublings %d' % (C2_OFF_SHIFT, n, bs(cb) if cb is not None else None,
                                                                                                st['segments'], len(st.get('doublings') or [])))
    res['c2'] = dict(on=r['reading'], off=n)
    say('== THE 146 ON-LINE POINTS, (M-on) on Λ_Q')
    low = None
    for r6 in on:
        t1 = time.time()
        r, lines = narrow_on(lam_q_at, 'ON %d' % r6['idx'], r6['im'], r6['h'])
        for l in lines:
            say(l)
        mid = ((r['lo'] + r['hi']) / 2).mid()
        row = dict(kind='ON', idx=r6['idx'], reading=r['reading'], depth=r['depth'], signs=r['signs'], re='0.5',
                   im=mid.str(DIGITS, radius=False) if r['reading'] == 'NARROWED' else r6['im'],
                   h=W if r['reading'] == 'NARROWED' else r6['h'], count=1, why=r.get('why'),
                   lo=r['lo'].str(DIGITS, radius=False), hi=r['hi'].str(DIGITS, radius=False), seconds=int(time.time() - t1))
        res['on'].append(row)
        say('  ON %d : %s at depth %d ; signs %s ; [%s, %s] ; %d s' % (r6['idx'], row['reading'], row['depth'], row['signs'], row['lo'], row['hi'],
                                                                         row['seconds']))
        if r6['idx'] % 10 == 0:
            f = CERT.free_mb()
            low = f if (low is None or (f is not None and f < low)) else low
    res['host_low_mb'] = low
    c = {}
    for x in res['on']:
        c[x['reading']] = c.get(x['reading'], 0) + 1
    say('### ### **RUN 1 : C1 %s ; C2 ON %s, OFF count %s ; ON POINTS %s ; HOST LOW %s MB ; %d s.**' % (
        [(x['n'], x['reading'], x['inside']) for x in res['c1']], res['c2']['on'], res['c2']['off'], c, low, time.time() - t_start))
    put('b671_narrow_run1.json', json.dumps(res, indent=1, ensure_ascii=False) + NL)
    put('b671_narrow_run1.txt', NL.join(OUT) + NL)
    say('  written: data/b671_narrow_run1.json, data/b671_narrow_run1.txt')


def run1b():
    """the author's word on the Bessel bar: C1 and C2 re-run under BESSEL_BAR_EXP and read as fixed before any Q0 point, then the on-line
    points run 1 left UNRESOLVED re-run from their last certified intervals."""
    t_start = time.time()
    say('b671 -- THE NARROWING, RUN 1b: C1, C2 AND RUN 1`S UNRESOLVED ON-LINE POINTS UNDER THE BAR 2^%d (%s) ; W %s ; DEPTH %d' % (
        BESSEL_BAR_EXP, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), W, DEPTH))
    r1 = json.load(io.open(os.path.join(D, 'b671_narrow_run1.json'), encoding='utf-8'))
    res = dict(bar=BESSEL_BAR_EXP, c1=[], c2={}, on=[])
    for n in C1_N:
        ctx.prec = PREC
        z = acb.zeta_zero(n)
        t0 = z.imag.mid().str(DIGITS, radius=False)
        r, lines = narrow_on(lam_z_at, 'C1 n=%d' % n, t0, H0)
        for l in lines:
            say(l)
        ctx.prec = PREC
        ref = acb.zeta_zero(n).imag
        inside = bool(r['lo'] <= ref.lower()) and bool(ref.upper() <= r['hi'])
        say('  C1 n = %d : %s at depth %d ; [%s, %s] ; the call`s ball inside it %s' % (n, r['reading'], r['depth'], r['lo'].str(DIGITS, radius=False),
                                                                                    r['hi'].str(DIGITS, radius=False), inside))
        res['c1'].append(dict(n=n, reading=r['reading'], depth=r['depth'], inside=inside))
    rows = rows667()
    on = dict((r['idx'], r) for r in rows if r['kind'] == 'ON')
    off = sorted((r for r in rows if r['kind'] == 'OFF'), key=lambda r: r['idx'])
    ctx.prec = PREC
    r0 = on[0]
    r, lines = narrow_on(lam_q_at, 'C2 ON idx 0 shifted', (exact(r0['im']) + arb(C2_ON_SHIFT)).mid().str(DIGITS, radius=False), H0)
    for l in lines:
        say(l)
    say('  C2 ON idx 0 shifted by %s : %s' % (C2_ON_SHIFT, r['reading']))
    q0 = off[0]
    ctx.prec = PREC
    n, cb, st = square_count(CERT.zq, (exact(q0['re']) + arb(C2_OFF_SHIFT)).mid().str(DIGITS, radius=False), q0['im'], H0)
    say('  C2 OFF idx 0 shifted by %s in σ : count %s ; ball %s ; segments %d ; doublings %d' % (C2_OFF_SHIFT, n, bs(cb) if cb is not None else None,
                                                                                                st['segments'], len(st.get('doublings') or [])))
    res['c2'] = dict(on=r['reading'], off=n)
    if not (all(x['inside'] and x['reading'] == 'NARROWED' for x in res['c1']) and res['c2'] == dict(on='NO SIGN CHANGE', off=0)):
        say('### C1 OR C2 NOT AS FIXED UNDER THE NEW BAR -- NO Q0 POINT RUN')
        put('b671_narrow_run1b.json', json.dumps(res, indent=1, ensure_ascii=False) + NL)
        put('b671_narrow_run1b.txt', NL.join(OUT) + NL)
        return
    for x in r1['on']:
        if x['reading'] == 'NARROWED':
            continue
        t1 = time.time()
        r, lines = narrow_on(lam_q_at, 'ON %d' % x['idx'], None, None, lo=x['lo'], hi=x['hi'])
        for l in lines:
            say(l)
        mid = ((r['lo'] + r['hi']) / 2).mid()
        row = dict(kind='ON', idx=x['idx'], reading=r['reading'], depth=x['depth'] + r['depth'], signs=r['signs'], re='0.5',
                   im=mid.str(DIGITS, radius=False), h=W if r['reading'] == 'NARROWED' else ((r['hi'] - r['lo']) / 2).upper().str(DIGITS, radius=False),
                   count=1, why=r.get('why'), lo=r['lo'].str(DIGITS, radius=False), hi=r['hi'].str(DIGITS, radius=False), seconds=int(time.time() - t1),
                   from_run1=dict(depth=x['depth'], lo=x['lo'], hi=x['hi']))
        res['on'].append(row)
        say('  ON %d : %s at depth %d (run 1 %d + run 1b %d) ; signs %s ; [%s, %s] ; %d s' % (
            x['idx'], row['reading'], row['depth'], x['depth'], r['depth'], row['signs'], row['lo'], row['hi'], row['seconds']))
    c = {}
    for x in res['on']:
        c[x['reading']] = c.get(x['reading'], 0) + 1
    say('### ### **RUN 1b : C1 %s ; C2 ON %s, OFF count %s ; THE %d RE-RUN %s ; %d s.**' % (
        [(x['n'], x['reading'], x['inside']) for x in res['c1']], res['c2']['on'], res['c2']['off'], len(res['on']), c, time.time() - t_start))
    put('b671_narrow_run1b.json', json.dumps(res, indent=1, ensure_ascii=False) + NL)
    put('b671_narrow_run1b.txt', NL.join(OUT) + NL)
    say('  written: data/b671_narrow_run1b.json, data/b671_narrow_run1b.txt')


def _init():
    ctx.prec = PREC


def run2():
    t_start = time.time()
    say('b671 -- THE NARROWING, RUN 2: THE 17 OFF-LINE POINTS ON %d PROCESSES (%s) ; W %s ; DEPTH %d ; SEGS_PER_SIDE %d ; DOUBLINGS_MAX %d' % (
        PROCS, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), W, DEPTH, SEGS_PER_SIDE, DOUBLINGS_MAX))
    f0 = CERT.free_mb()
    say('### host free at start: %s MB ; the hold %d MB' % (f0, CERT.HOLD_MB))
    off = sorted((r for r in rows667() if r['kind'] == 'OFF'), key=lambda r: r['idx'])
    pts = os.path.join(D, 'b671_narrow_run2_points.jsonl')
    done = set()
    if os.path.exists(pts):
        for l in io.open(pts, encoding='utf-8'):
            if l.strip():
                done.add(json.loads(l)['idx'])
    todo = [r for r in off if r['idx'] not in done]
    say('### points already banked: %s ; to run: %s' % (sorted(done), [r['idx'] for r in todo]))
    low = f0
    with mpr.Pool(PROCS, initializer=_init) as pool:
        for res in pool.imap_unordered(task_off, todo):
            with io.open(pts, 'a', encoding='utf-8', newline=NL) as fh:
                fh.write(json.dumps(res, ensure_ascii=False) + NL)
            f = CERT.free_mb()
            low = f if (low is None or (f is not None and f < low)) else low
            say('  OFF %d : %s at depth %d ; %d s ; host free %s MB' % (res['idx'], res['reading'], res['depth'], res['seconds'], f))
    say('### ### **RUN 2 : DONE ; HOST LOW %s MB ; %d s.**' % (low, time.time() - t_start))
    put('b671_narrow_run2.txt', NL.join(OUT) + NL)


def _last_interval(x):
    """an on-line row's ball: W about its interval's midpoint where NARROWED; where not, its last certified interval [lo, hi] -- the plan's
    "keeps its last certified interval" -- by its midpoint and the interval's half-width rounded up, never b667's square."""
    ctx.prec = PREC
    lo, hi = exact(x['lo']), exact(x['hi'])
    return ((lo + hi) / 2).mid().str(DIGITS, radius=False), (W if x['reading'] == 'NARROWED' else ((hi - lo) / 2).upper().str(DIGITS, radius=False))


def bank():
    r1 = json.load(io.open(os.path.join(D, 'b671_narrow_run1.json'), encoding='utf-8'))
    p1b = os.path.join(D, 'b671_narrow_run1b.json')
    if os.path.exists(p1b):           # ### the author's word on the Bessel bar: the re-run rows replace run 1's for their points
        r1b = json.load(io.open(p1b, encoding='utf-8'))
        rb = dict((x['idx'], x) for x in r1b.get('on') or [])
        r1['on'] = [rb.get(x['idx'], x) for x in r1['on']]
        r1['c1_run1b'], r1['c2_run1b'] = r1b.get('c1'), r1b.get('c2')
    for x in r1['on']:
        x['im'], x['h'] = _last_interval(x)
    off = [json.loads(l) for l in io.open(os.path.join(D, 'b671_narrow_run2_points.jsonl'), encoding='utf-8') if l.strip()]
    off = sorted(off, key=lambda r: r['idx'])
    rows = [dict(kind=r['kind'], idx=r['idx'], re=r['re'], im=r['im'], h=r['h'], count=1, reading=r['reading'], depth=r['depth'])
            for r in r1['on']] + [dict(kind='OFF', idx=r['idx'], re=r['re'], im=r['im'], h=r['h'], count=1, reading=r['reading'], depth=r['depth'])
                                  for r in off]
    js = (json.dumps(dict(w=W, h0=H0, depth=DEPTH, prec=PREC, source='data/b667_epstein_zeros_certified.json.gz', rows=rows), indent=1,
                     ensure_ascii=False) + NL).encode('utf-8')
    gz = gzip.compress(js, mtime=0)
    p = os.path.join(D, 'b671_epstein_zeros_narrowed.json.gz')
    open(p + '.tmp', 'wb').write(gz)
    os.replace(p + '.tmp', p)
    put('b671_epstein_zeros_narrowed_hashes.txt', 'b671 -- THE NARROWED LIST`S HASHES (rows are files): the JSON as written, then gzipped (mtime 0)%s'
        'data/b671_epstein_zeros_narrowed.json (inside the .gz) sha256 %s bytes %d%sdata/b671_epstein_zeros_narrowed.json.gz sha256 %s bytes %d%s' % (
            NL, hashlib.sha256(js).hexdigest(), len(js), NL, hashlib.sha256(gz).hexdigest(), len(gz), NL))
    log = [dict(kind='ON', idx=r['idx'], depth=r['depth'], reading=r['reading'] if r['reading'] in ('NARROWED', 'UNRESOLVED-AT-DEPTH') else
                'UNRESOLVED-AT-DEPTH', signs=r['signs'], why=r.get('why')) for r in r1['on']] + [
        dict(kind='OFF', idx=r['idx'], depth=r['depth'], reading=r['reading'], signs=None) for r in off]
    c = {}
    for x in log:
        c[(x['kind'], x['reading'])] = c.get((x['kind'], x['reading']), 0) + 1
    L = ['b671 -- THE NARROWING`S LOG (rows are points with their depth and reading; the depth-by-depth lines in data/b671_narrow_run1.txt and '
         'data/b671_narrow_run2_points.jsonl) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### C1: %s ; C2: ON %s, OFF count %s' % ([(x['n'], x['reading'], x['inside']) for x in r1['c1']], r1['c2']['on'], r1['c2']['off']), '']
    L += ['  %-3s %-4d depth %-3d %-20s signs %s%s' % (x['kind'], x['idx'], x['depth'], x['reading'], x['signs'], (' ; ' + x['why']) if x.get('why') else '')
          for x in log]
    on_n = sum(v for (k, r_), v in c.items() if k == 'ON' and r_ == 'NARROWED')
    off_n = sum(v for (k, r_), v in c.items() if k == 'OFF' and r_ == 'NARROWED')
    L += ['', '### ### **POINTS %d ; ON NARROWED %d OF %d ; OFF NARROWED %d OF %d ; UNRESOLVED %d ; HALF-WIDTH %s.**' % (
        len(log), on_n, len(r1['on']), off_n, len(off), len(log) - on_n - off_n, W)]
    put('b671_narrow_log.txt', NL.join(L) + NL)
    put('b671_narrow_log.json', json.dumps(dict(rows=log, c1=r1['c1'], c2=r1['c2'], w=W), indent=1, ensure_ascii=False) + NL)
    print(L[-1])


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    if mode == 'diff':
        # ### the carried code against b667's, banked: square_count and segment, each read from the two files' own source by its node
        src = io.open(os.path.join(ROOT, 'tools', 'b667_epstein_certify.py'), encoding='utf-8').read()
        import ast
        tree = ast.parse(src)
        lines = src.splitlines()
        out = ['b671 -- THE CARRIED COUNT AGAINST b667`s (tools/b667_epstein_certify.py): square_count and segment, unified diff', '']
        mine = io.open(os.path.abspath(__file__), encoding='utf-8').read().splitlines()
        mt = ast.parse(io.open(os.path.abspath(__file__), encoding='utf-8').read())
        for name in ('square_count', 'segment', '_bessel'):
            n0 = [x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name == name][0]
            n1 = [x for x in mt.body if isinstance(x, ast.FunctionDef) and x.name == name][0]
            a = lines[n0.lineno - 1:n0.end_lineno]
            bb = mine[n1.lineno - 1:n1.end_lineno]
            out += ['=== %s (b667 :%d-:%d ; b671 :%d-:%d)' % (name, n0.lineno, n0.end_lineno, n1.lineno, n1.end_lineno)] + list(
                difflib.unified_diff(a, bb, 'b667', 'b671', lineterm='')) + ['']
        put('b671_narrow_carry_diff.txt', NL.join(out) + NL)
        print(NL.join(out))
    elif mode == 'run1b':
        run1b()
    elif mode == 'run1':
        run1()
    elif mode == 'run2':
        run2()
    elif mode == 'bank':
        bank()
    else:
        print('usage: b671_narrow.py diff | run1 | run2 | bank')
        sys.exit(2)
