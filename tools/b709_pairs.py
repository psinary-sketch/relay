# -*- coding: utf-8 -*-
"""b709_pairs.py -- THE DETECTION LAW OVER THE TWELVE HIGHER PAIRS, (R319)(5), AS data/b707_registrations.txt (i) REGISTERED IT (:10-:77,
committed alone at relay 6e8ece87 before any number, unchanged): "the twelve off-line pairs beyond b675's modulus rule by the route the
registration priced, at the working precision it names, each pair's n* and its ratio to the predicted value printed, the falsifier read (any
pair outside [0.67, 1.5]) and printed HELD or REFUTED, the controls printed before the figures (b675's figure at rho_0 and b705's five pairs
reproduced); a pair beyond the route's reach entered as 'beyond reach at n = <bound>' with the bound, not estimated".

### UNTRACKED WRITE: data/b709_pairs_units* -- data/b709_pairs_units.jsonl and the band files data/b709_pairs_units_band_<lo>_<hi>.jsonl (one unit per
### (route, key), appended as it lands; resumable); declared by prefix for the root route's exclusion list (the line read to its first space by
### tools/b709_record.py, a carry-time repair banked in data/b709_tool_repairs.txt).

### THE ROUTE (the registration :39-:43): b675's arithmetic unchanged -- for each pair, constants_for (tools/b675_li_bench.py :163-:194) on the ON
### rows and that pair alone with dom = ref<idx> (b705's configuration, tools/b705_detection.py pair_rows), the tail under T-COUNT (A0 = 10,
### KMAX 20000), n* the onset of 2 - R^n/4 + C (n + 1)^2 s^n below 0 (onset :153-:160) -- run under a certified list extended to a height
### T0' at which the uncertified modulus bound sqrt(1 + 2/T0'^2) falls below the pair's r = (1 + R)/2, and the onset's cap raised from
### 2,000,000 to 1.5 x the predicted n*. constants_for709 below is :163-:194 with two parameters where b675 has module constants: the certified
### height T0 (b675's 150, here the height the extended list is complete to) and the onset cap; its arithmetic is otherwise b675's line for
### line; (C1) and (C2) run it at T0 = 150 and cap 2,000,000 and must reproduce b675's and b705's figures exactly.
### THE EXTENSION (the registration :49-:53, "a NEW CERTIFICATION of Q0's zeros above 149.72"): the engine is b667's (tools/b667_epstein_certify.py,
### IMPORTED unedited: zq with T4 in the radius, logg_q, edge_arg, half_path_3c) with b671's carried segment and Bessel bar (tools/b671_narrow.py,
### imported unedited, which sets them into b667's module by name as b681 did). Per height band [T_lo, T_hi]:
###   `count`   N(band) = the zeros of Z_Q in [-1/2, 3/2] x [T_lo, T_hi] by b667's half path 1/2 + iT_lo -> 3/2 + iT_lo -> 3/2 + iT_hi -> 1/2 + iT_hi,
###             the right edge by (3c) (|Z_Q - 2| <= Z_Q(3/2) - 2 < 2 there), the count (1/pi)(Delta arg Z_Q + Delta Im log gamma_Q) -- b667's R
###             form (its reading (ii): the left half of the boundary is the half path's reflection under s -> 1 - conj s). A band's ends on the
###             line must not be zeros: a band whose count is unread is split at its midpoint and the two halves counted.
###   `online`  the zeros ON the line in the band: the certified sign of Lambda_Q(1/2 + it) (b671's sign_at: real on the line, the imaginary ball
###             containing 0, 200 then 400 bits) scanned at a step, each sign change halved to the half-width W_ON -- a zero of odd order in each
###             interval; the band's N against the on-line count read beneath.
###   `offline` the zeros OFF the line in the band, where N(band) exceeds the on-line count: the right half-strip [1/2 + DELTA, 3/2] x [T_lo, T_hi]
###             counted in rectangles by b667's edge_arg (Z_Q analytic there, no pole above t = 1/2), each rectangle at count 1 halved on its
###             longer side to half-widths W_OFF, each at count 1 a located zero, its partner 1 - conj rho the reflection; N(band) must equal
###             the on-line count plus twice the off-line count, or the band stands INCOMPLETE and reaches no pair.
### THE READING per pair: the extended list complete to T0' (every band below T0' counted and placed); the pair reached where
### sqrt(1 + 2/T0'^2) < r; n* by constants_for709; n*/predicted against [0.67, 1.5]; a pair whose r stays below the bound at the height
### reached is "beyond reach: the certified list ends at T0' = <reached>, the rule needs T0' > <needed>" (the registration's table :25-:36),
### and a pair whose onset is not found below its cap is "beyond reach at n = <cap>" -- the bound, not estimated.
### THE CONTROLS, printed before any figure: (C1) n*(rho_0) by the route at T0 = 150 over the whole 180-representative configuration with
### dom = ref0, against b675's 63676 (data/b675_li_bench.txt :6; data/b705_detection_controls.txt :6); (C2) b705's five pairs idx 0-4 at
### T0 = 150 and cap 2,000,000, against 63651, 358522, 897059, 798682, 1020476 (data/b705_detection.txt :10-:14); (C3) the five pairs under the
### extended list (T0' the height reached), their n* beside b705's and their ratios still within the range, before any pair of the twelve.
### Routes (each its own foreground call under the 590 s guard, resumable):
###   controls                       C1 and C2                       count <T_lo> <T_hi>          N(band)
###   online <T_lo> <T_hi> [step]    the on-line zeros of the band    offline <T_lo> <T_hi>        the off-line zeros of the band
###   extstatus                      the bands, their counts, the height the list is complete to
###   c3                             the five pairs under the extended list
###   pairs <i> <j>                  the pairs idx i..j (5-16), each resumable by its own unit
###   bank                           data/b709_pairs.txt, data/b709_pairs.json.gz beside data/b709_pairs_hashes.txt (data/b680_rules.txt row (1))
### Written by the Write tool at b709; it writes only the banks it names and its units file. 256 bits for the route (b675's PREC), 200/400 for
### the certification (b667's); every value a ball.
"""
import gzip
import hashlib
import io
import json
import math
import os
import sys
import time

from flint import acb, arb, ctx

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b675_li_bench as B          # noqa: E402  ### b675's route, imported unedited (reps, terms, onset, constants_for, T0, KMAX, A0, PREC)
import b705_detection as P5        # noqa: E402  ### b705's configuration and readings: pair_rows, r_of, leading, RANGE, B675_NSTAR
import b667_epstein_certify as CERT   # noqa: E402  ### the engine: zq, logg_q, edge_arg, half_path_3c, _stats, _pt
import b671_narrow as N            # noqa: E402  ### the carried segment and Bessel bar set into CERT by name at import; sign_at, lam_q_at

ACT = 'b709'
UNITS = os.path.join(D, '%s_pairs_units.jsonl' % ACT)
BESSEL_RUNG = 2000                 # ### the Bessel factor's top rung, b667's 600 raised: K_nu(pi sqrt23 m) with |Im nu| = t cancels like e^(pi t), about
CERT.PREC_BESSEL = BESSEL_RUNG     # ### 4.5 t bits, so b667's ladder 200 -> 400 -> 600 returns a ball of radius 1e9..1e158 above t = 185 (the probe route
#                                  # ### banked in data/b709_pairs.txt); at 2000 the value at 443 has radius 4e-12 in 0.1 s. Set into b667's module by name as
#                                  # ### b681 set the bar (b671's _bessel reads CERT.PREC_BESSEL at each call); nothing else of the engine changed.
RANGE = P5.RANGE                   # ### [0.67, 1.5]
B705_FIVE = (63651, 358522, 897059, 798682, 1020476)   # ### data/b705_detection.txt :10-:14
T_BASE = '150'                     # ### the certified list as held: complete to 150 (b667's R, data/b667_epstein_counts.txt :52), T0 = 150 (b675 :36)
NEEDED = {5: 157.0, 6: 154.1, 7: 229.7, 8: 207.0, 9: 263.7, 10: 233.4, 11: 405.4, 12: 226.0, 13: 274.2, 14: 302.9, 15: 442.3, 16: 318.7}   # ### :25-:36 (DERIVED there)
CPREC, CRUNG = CERT.PREC, CERT.PREC_RUNG     # ### 200, 400
W_ON = '1e-8'                      # ### the on-line interval's half-width after the halvings
W_OFF = '1e-6'                     # ### the off-line rectangle's half-width
DELTA = '0.02'                     # ### the right half-strip's left edge sigma = 1/2 + DELTA (the off-line real parts of the 17 lie in [0.605, 0.954])
SCAN_STEP = '0.05'                 # ### the on-line scan's step (the zeros' mean spacing about 0.6 at these heights)
PAIR_BUDGET = 500                  # ### seconds per call of the onset loop before the unit is banked as partial
T_CALL = []                        # ### the band call's start, read by `offline` for its budget
SIG_ROWS = 19                      # ### the candidate grid's sigma rows from 0.55 step 0.05: 19 to 1.45 for the bands to 310; 10 (to 1.00) from 310 on -- the 32
#                                  # ### off-line real parts read so far lie in [0.56, 0.96], and a zero the grid misses shows as N(band) > on + 2 x located
RECT_CERTIFY = False               # ### the off-line candidates' rectangles (count 1 by b667's edge_arg) were run for the bands to 250 (100 s to 1000 s each,
#                                  # ### the segments as b667's squares); for the bands above, the located zero stands by its point values and the band's
#                                  # ### count -- the off-line zeros' positions never enter the pairs' route (b705's configuration removes every other
#                                  # ### orbit), only their NUMBER does, read from N(band) - on-line; the bank names which zeros carry a rectangle
DIGITS = 30


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def s_(x, d=20):
    return x.str(d, radius=True)


def put_txt(name, L):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


SEG = ''   # ### a band's own units file data/b709_pairs_units_band_<lo>_<hi>.jsonl (UNTRACKED WRITE) when the `band` route runs it, so that
#          # ### several bands run as separate foreground processes at once, none appending to another's file


def units():
    U = {}
    files = [UNITS] + sorted(os.path.join(D, f) for f in os.listdir(D) if f.startswith('%s_pairs_units_band_' % ACT) and f.endswith('.jsonl'))
    for path in files:
        if os.path.exists(path):
            for l in io.open(path, encoding='utf-8'):
                if l.strip():
                    u = json.loads(l)
                    U[(u['route'], u['key'])] = u
    return U


def put_unit(u):
    u['at'] = utc()
    path = os.path.join(D, '%s_pairs_units_band_%s.jsonl' % (ACT, SEG)) if SEG else UNITS
    with open(path, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


def _arb(s):
    """a ball from its banked string 'mid +/- rad' or '[mid +/- rad]'."""
    s = s.strip().strip('[]')
    if '+/-' in s:
        m, r = s.split('+/-')
        return arb(m.strip(), r.strip())
    return arb(s)


# ================================================================================ THE ROUTE WITH ITS TWO PARAMETERS (b675 :153-:194, line for line)
def onset709(Dm, R, c, Cc, s, cap, n_start=1, budget=None):
    """b675's onset (:153-:160) with the cap a parameter and the loop resumable: (n or None, the expression's ball, the last n read, done)."""
    lR, ls = R.log(), s.log()
    t0 = time.time()
    n = n_start
    while n < cap:
        e = Dm - c * (lR * n).exp() + Cc * (n + 1) ** 2 * (ls * n).exp()
        if e < 0:
            return n, e, n, True
        if budget is not None and (n & 1023) == 0 and time.time() - t0 > budget:
            return None, None, n, False
        n += 1
    return None, None, cap, True


def constants_for709(Tm, dom, T0p, cap, removed=(), n_start=1, budget=None):
    """b675's constants_for (:163-:194) with T0 and the onset cap as parameters; the arithmetic b675's line for line."""
    ctx.prec = B.PREC
    rest = [x for x in Tm if x[0] not in removed and x[0] != dom]
    d = [x for x in Tm if x[0] == dom][0]
    z = (1 - 1 / acb(d[2], d[3]))
    R, th = abs(z), z.arg()
    r = (1 + R) / 2
    mods = [(x[0], abs(1 - 1 / acb(x[2], x[3]))) for x in rest]
    nxt = max(mods, key=lambda m: m[1].mid())
    unc = (1 + arb(2) / (T0p * T0p)).sqrt()
    below_r = all(bool(m[1] < r) for m in mods) and bool(unc < r)
    if not below_r:
        return dict(dom=dom, reach='the rule`s modulus condition fails: every rest modulus below r %s, the uncertified bound %s' % (
            all(bool(m[1] < r) for m in mods), s_(unc, 15)), R=s_(R, 25), r=s_(r, 25), uncertified_modulus_bound=s_(unc, 15), T0=T0p,
            next_modulus=[nxt[0], s_(nxt[1], 25)], every_rest_modulus_below_r=below_r, n_star=None, done=True)
    s1 = r
    s = (s1 + R) / 2
    Kc = 2 * sum((1 / (1 + x[3] * x[3] + (x[2] - arb('0.5')) ** 2) for x in rest), arb(0))
    Kt = arb(0)
    for k in range(T0p - 1, B.KMAX + 1):
        kp = arb(max(k, T0p))
        Kt += 2 * B.A0 * arb(k + 4).log() / (1 + kp * kp)
    Kt += 2 * B.A0 * B._tailint()
    Kk = Kc + Kt
    Cc = 2 * (2 + 2 * (1 + s) ** 2) * Kk
    n_, e, n_last, done = onset709(arb(2), R, arb(1) / 4, Cc, s, cap, n_start, budget)
    return dict(dom=dom, removed=list(removed), R=s_(R, 25), theta=s_(th, 25), r=s_(r, 25), next_modulus=[nxt[0], s_(nxt[1], 25)],
                uncertified_modulus_bound=s_(unc, 15), every_rest_modulus_below_r=below_r, s1=s_(s1, 25), s=s_(s, 25),
                ln_R_over_s=s_((R / s).log(), 15), K_cert=s_(Kc, 20), K_tail=s_(Kt, 20), K=s_(Kk, 20), C=s_(Cc, 20), T0=T0p, cap=cap,
                n_star=n_, expr_at_n_star=s_(e, 15) if e is not None else None, rest_points=2 * len(rest), n_last=n_last, done=done, reach=None)


# ================================================================================ C1 AND C2
def controls(*a):
    U = units()
    R0 = B.reps()
    T0m = B.terms(R0)
    out = []
    key = ('controls', 'C1')
    if key not in U:
        t0 = time.time()
        c = constants_for709(T0m, 'ref0', B.T0, 2000000)
        off0 = [x for x in R0 if x[0] == 'off0'][0]
        r0 = P5.r_of(off0[1], off0[2])
        put_unit(dict(route='controls', key='C1', n_star=c['n_star'], b675=P5.B675_NSTAR, equal=c['n_star'] == P5.B675_NSTAR, R=c['R'], s=c['s'],
                      r0=s_(r0, 30), L0=s_(r0 * c['n_star'], 30) if c['n_star'] else None, seconds=int(time.time() - t0)))
        U = units()
    u = U[key]
    print('  C1 | n*(rho_0) by the route at T0 = 150 over the 180 representatives, dom = ref0: %s ; b675`s %d ; EQUAL %s ; L0 = r(rho_0) x n* = %s ; %d s' % (
        u['n_star'], u['b675'], u['equal'], u['L0'], u['seconds']), flush=True)
    out.append(u['equal'])
    t_call = time.time()
    for idx in range(5):
        key = ('controls', 'C2-%d' % idx)
        if key not in U:
            if time.time() - t_call > 420:
                print('### THE CALL`S BUDGET REACHED BEFORE C2 PAIR %d -- CALL AGAIN TO RESUME' % idx)
                return
            t0 = time.time()
            off = [x for x in R0 if x[0] == 'off%d' % idx][0]
            rows = P5.pair_rows(R0, idx)
            c = constants_for709(B.terms(rows), 'ref%d' % idx, B.T0, 2000000)
            put_unit(dict(route='controls', key='C2-%d' % idx, idx=idx, n_star=c['n_star'], b705=B705_FIVE[idx], equal=c['n_star'] == B705_FIVE[idx],
                          r=s_(P5.r_of(off[1], off[2]), 30), R=c['R'], seconds=int(time.time() - t0)))
            U = units()
        u = U[key]
        print('  C2 | pair %d at T0 = 150, cap 2,000,000: n* %s ; b705`s %d ; EQUAL %s ; %d s' % (idx, u['n_star'], u['b705'], u['equal'], u['seconds']), flush=True)
        out.append(u['equal'])
    put_unit(dict(route='controls', key='verdict', ok=all(out), rows=len(out)))
    print('### C1 AND C2 AS WANTED %s' % all(out))


def _controls_ok(U):
    v = U.get(('controls', 'verdict'))
    return bool(v) and bool(v.get('ok'))


# ================================================================================ THE EXTENSION: THE BAND COUNT
def _w_tail():
    ctx.prec = CPREC
    z15 = CERT.zq(acb(arb('1.5')), CPREC)
    return z15.real - 2


def _hp_task(args):
    """one piece of a horizontal edge of the half path, in a worker process: the argument change along it (b667's edge_arg, depth DEPTH_P)."""
    t_lo, t_hi, which, j, parts, nseg = args
    ctx.prec = CPREC
    CERT.PREC_BESSEL = BESSEL_RUNG
    half = arb(1) / 2
    A, Bc, C, Dd = acb(half, arb(t_lo)), acb(arb('1.5'), arb(t_lo)), acb(arb('1.5'), arb(t_hi)), acb(half, arb(t_hi))
    a, b_ = (A, Bc) if which == 0 else (C, Dd)
    za = a + (b_ - a) * arb(j) / parts
    zb = a + (b_ - a) * arb(j + 1) / parts
    st, cache = CERT._stats(), {}
    d = CERT.edge_arg(CERT.zq, za, zb, nseg, CERT.DEPTH_P, st, cache)
    return dict(which=which, j=j, arg=d.str(60, radius=True) if d is not None else None, segments=st['segments'], max_depth=st['max_depth'],
                rung_segments=st['rung_segments'], unresolved=st['unresolved'][:4])


def half_path_parallel(t_lo, t_hi, parts=3, procs=6):
    """b667's half_path_3c (:337-:357) for the band [t_lo, t_hi]: the two horizontal edges in `parts` pieces each as worker processes (joined
    before the return), the right edge by (3c) from two point values, the count (1/pi)(d1 + d2 + d3 + Delta Im log gamma_Q)."""
    import multiprocessing as mpr
    ctx.prec = CPREC
    half = arb(1) / 2
    A, Bc, C, Dd = acb(half, arb(t_lo)), acb(arb('1.5'), arb(t_lo)), acb(arb('1.5'), arb(t_hi)), acb(half, arb(t_hi))
    w = _w_tail()
    lead = 2
    st = CERT._stats()
    if not (w < lead):
        return None, None, st, '### THE TAIL BOUND %s IS NOT BELOW %s -- THE EDGE NOT TAKEN' % (w.str(10, radius=True), lead)
    args = [(t_lo, t_hi, which, j, parts, 3) for which in (0, 1) for j in range(parts)]
    pool = mpr.Pool(procs)
    try:
        res = pool.map(_hp_task, args)
    finally:
        pool.close()
        pool.join()
    ctx.prec = CPREC
    d1, d3 = arb(0), arb(0)
    for r in sorted(res, key=lambda r: (r['which'], r['j'])):
        st['segments'] += r['segments']
        st['max_depth'] = max(st['max_depth'], r['max_depth'])
        st['rung_segments'] += r['rung_segments']
        st['unresolved'] += r['unresolved']
        if r['arg'] is None:
            return None, None, st, 'an edge piece unresolved'
        if r['which'] == 0:
            d1 += _arb(r['arg'])
        else:
            d3 += _arb(r['arg'])
    cache = {}
    fb, fc = CERT._pt(CERT.zq, Bc, cache), CERT._pt(CERT.zq, C, cache)
    ctx.prec = CPREC
    ab, ac = fb.arg(), fc.arg()
    d2 = ac - ab
    pr = 'the right edge by (3c): tail %s < %s ; F(B) = %s (arg %s) ; F(C) = %s (arg %s) ; its argument change %s' % (
        w.str(10, radius=True), lead, fb.str(10, radius=True), ab.str(10, radius=True), fc.str(10, radius=True), ac.str(10, radius=True), d2.str(10, radius=True))
    cb = (d1 + d2 + d3 + (CERT.logg_q(Dd) - CERT.logg_q(A)).imag) / arb.pi()
    return CERT._count(cb), cb, st, pr


def half_path_pieces(U, key, t_lo, t_hi, parts=12, budget=420):
    """the half path's horizontal edges in `parts` pieces each, run IN THE FOREGROUND one after another (no pool, the author's word of
    2026-10-24), each banked as it lands ('hppiece', '<key>_p<parts>_<which>_<j>'); a call stops after the piece that passes `budget` seconds
    and the next call runs the pieces still missing; returns (count, ball, stats, the (3c) print, remaining). The two bands whose pieces were
    banked at parts 6 by the pooled form (289.836447-299.827256, 299.827256-310) assemble from those."""
    ctx.prec = CPREC
    pfx = '%s_p%d_' % (key, parts) if parts != 6 else '%s_' % key
    want = [(which, j) for which in (0, 1) for j in range(parts)]
    have = {}
    for which, j in want:
        u = U.get(('hppiece', '%s%d_%d' % (pfx, which, j)))
        if u:
            have[(which, j)] = u
    t_call = time.time()
    for which, j in want:
        if (which, j) in have:
            continue
        if time.time() - t_call > budget:
            break
        t0 = time.time()
        r = _hp_task((t_lo, t_hi, which, j, parts, 2))
        r.update(route='hppiece', key='%s%d_%d' % (pfx, which, j), seconds=int(time.time() - t0))
        put_unit(r)
        have[(which, j)] = r
        print('    count piece edge %d part %d banked: segments %d, depth %d, %s ; %d s' % (which, j, r['segments'], r['max_depth'], 'read' if r['arg'] else '### UNRESOLVED', r['seconds']), flush=True)
    remaining = len([1 for wj in want if wj not in have])
    if remaining:
        return None, None, CERT._stats(), '', remaining
    ctx.prec = CPREC
    half = arb(1) / 2
    A, Bc, C, Dd = acb(half, arb(t_lo)), acb(arb('1.5'), arb(t_lo)), acb(arb('1.5'), arb(t_hi)), acb(half, arb(t_hi))
    w = _w_tail()
    lead = 2
    st = CERT._stats()
    if not (w < lead):
        return None, None, st, '### THE TAIL BOUND %s IS NOT BELOW %s -- THE EDGE NOT TAKEN' % (w.str(10, radius=True), lead), 0
    d1, d3 = arb(0), arb(0)
    for (which, j), r in sorted(have.items()):
        st['segments'] += r['segments']
        st['max_depth'] = max(st['max_depth'], r['max_depth'])
        st['rung_segments'] += r['rung_segments']
        st['unresolved'] += r['unresolved']
        if r['arg'] is None:
            return None, None, st, 'an edge piece unresolved', 0
        if which == 0:
            d1 += _arb(r['arg'])
        else:
            d3 += _arb(r['arg'])
    cache = {}
    fb, fc = CERT._pt(CERT.zq, Bc, cache), CERT._pt(CERT.zq, C, cache)
    ctx.prec = CPREC
    ab, ac = fb.arg(), fc.arg()
    d2 = ac - ab
    pr = 'the right edge by (3c): tail %s < %s ; F(B) = %s (arg %s) ; F(C) = %s (arg %s) ; its argument change %s' % (
        w.str(10, radius=True), lead, fb.str(10, radius=True), ab.str(10, radius=True), fc.str(10, radius=True), ac.str(10, radius=True), d2.str(10, radius=True))
    cb = (d1 + d2 + d3 + (CERT.logg_q(Dd) - CERT.logg_q(A)).imag) / arb.pi()
    return CERT._count(cb), cb, st, pr, 0


def count(t_lo, t_hi, *a):
    """N([-1/2, 3/2] x [t_lo, t_hi]) by b667's half path with (3c) on the right edge; banked per band."""
    U = units()
    key = ('count', '%s_%s' % (t_lo, t_hi))
    if key in U and U[key].get('count') is not None:
        u = U[key]
        print('  band [%s, %s]: N = %s (banked; ball %s)' % (t_lo, t_hi, u['count'], u['ball']))
        return
    ctx.prec = CPREC
    t0 = time.time()
    n, cb, st, pr, remaining = half_path_pieces(U, key[1], t_lo, t_hi)
    if remaining:
        print('  band [%s, %s]: %d edge pieces of the count still to run -- call again ; %d s' % (t_lo, t_hi, remaining, int(time.time() - t0)))
        return
    u = dict(route='count', key=key[1], t_lo=t_lo, t_hi=t_hi, count=n, ball=cb.str(12, radius=True) if cb is not None else None, segments=st['segments'],
             max_depth=st['max_depth'], rung_segments=st['rung_segments'], unresolved=st['unresolved'][:8], edge3c=pr[:300], seconds=int(time.time() - t0))
    put_unit(u)
    print('  band [%s, %s]: N = %s (ball %s ; segments %d ; depth %d ; unresolved %s) ; %d s' % (t_lo, t_hi, n, u['ball'], st['segments'], st['max_depth'],
                                                                                                 st['unresolved'][:3] or 'NONE', u['seconds']), flush=True)


# ================================================================================ THE EXTENSION: THE ON-LINE ZEROS
def _sign(t):
    s, im0, line = N.sign_at(N.lam_q_at, t)
    return s


def online(t_lo, t_hi, step=SCAN_STEP, *a):
    """the on-line zeros of the band by the certified sign of Lambda_Q on the line at the step, each change halved to W_ON; banked per band
    (resumable at the scan point)."""
    U = units()
    key = ('online', '%s_%s' % (t_lo, t_hi) if str(step) == SCAN_STEP else '%s_%s@%s' % (t_lo, t_hi, step))   # ### a finer re-scan keyed by its step
    u = U.get(key) or dict(route='online', key=key[1], t_lo=t_lo, t_hi=t_hi, step=step, scanned_to=None, zeros=[], unread=[], done=False, seconds=0)
    if u.get('done'):
        print('  band [%s, %s]: on-line zeros %d (banked)' % (t_lo, t_hi, len(u['zeros'])))
        return
    ctx.prec = CPREC
    t0 = time.time()
    h = arb(step)
    w = arb(W_ON)
    t = arb(u['scanned_to']) if u['scanned_to'] else arb(t_lo)
    s_prev = _sign(t)
    if s_prev is None:
        u['unread'].append(t.str(20, radius=False))
    while t < arb(t_hi):
        t2 = t + h
        if t2 > arb(t_hi):
            t2 = arb(t_hi)
        s2 = _sign(t2)
        if s2 is None:
            u['unread'].append(t2.str(20, radius=False))
        elif s_prev is not None and s2 != s_prev:
            a_, b_, sa, sb = t, t2, s_prev, s2
            d = 0
            ok = True
            while (b_ - a_) / 2 > w:
                m = ((a_ + b_) / 2).mid()
                sm = _sign(m)
                d += 1
                if sm is None:
                    ok = False
                    u['unread'].append('halving at %s' % m.str(20, radius=False))
                    break
                if sm == sa:
                    a_ = m
                else:
                    b_ = m
            if ok:
                mid = ((a_ + b_) / 2).mid()
                hw = ((b_ - a_) / 2).upper()
                u['zeros'].append(dict(t=mid.str(DIGITS, radius=False), h=hw.str(5, radius=False), lo=a_.str(DIGITS, radius=False), hi=b_.str(DIGITS, radius=False), depth=d, signs=[sa, sb]))
                print('    on-line zero at t = %s +/- %s (signs %d -> %d, %d halvings)' % (mid.str(16, radius=False), hw.str(3, radius=False), sa, sb, d), flush=True)
        if s2 is not None:
            s_prev = s2
        t = t2
        u['scanned_to'] = t.str(DIGITS, radius=False)
        if time.time() - t0 > 500:
            u['seconds'] += int(time.time() - t0)
            put_unit(u)
            print('### THE CALL`S BUDGET REACHED AT t = %s -- CALL AGAIN TO RESUME (%d zeros so far)' % (u['scanned_to'], len(u['zeros'])))
            return
    u['done'] = True
    u['seconds'] += int(time.time() - t0)
    put_unit(u)
    print('  band [%s, %s]: on-line zeros %d ; sign unread at %s ; %d s' % (t_lo, t_hi, len(u['zeros']), u['unread'][:4] or 'NONE', u['seconds']))


# ================================================================================ THE EXTENSION: THE OFF-LINE ZEROS
def _edge_task(args):
    """one edge of a rectangle, in a worker process (b667's pool form): the argument change as a string ball, or None, with its stats."""
    import multiprocessing as _m   # noqa: F401
    re_lo, re_hi, im_lo, im_hi, i, j, parts, nseg = args
    ctx.prec = CPREC
    CERT.PREC_BESSEL = BESSEL_RUNG
    a, b_, c, d_ = arb(re_lo), arb(re_hi), arb(im_lo), arb(im_hi)
    cs = [acb(a, c), acb(b_, c), acb(b_, d_), acb(a, d_), acb(a, c)]
    za = cs[i] + (cs[i + 1] - cs[i]) * arb(j) / parts          # ### the j-th of `parts` pieces of edge i
    zb = cs[i] + (cs[i + 1] - cs[i]) * arb(j + 1) / parts
    st, cache = CERT._stats(), {}
    d = CERT.edge_arg(CERT.zq, za, zb, nseg, CERT.DEPTH_SQ, st, cache)
    return dict(i=i, j=j, arg=d.str(60, radius=True) if d is not None else None, segments=st['segments'], max_depth=st['max_depth'],
                rung_segments=st['rung_segments'], unresolved=st['unresolved'][:4])


def rect_pieces(U, key, re_lo, re_hi, im_lo, im_hi, nseg=2, procs=6, parts=3):
    """the rectangle's 4 x `parts` edge pieces, each a banked unit ('rectpiece', '<key>_<i>_<j>'); a call runs at most `procs` of the pieces
    not yet banked, as a pool joined before the return; returns (the banked pieces, the number still remaining)."""
    import multiprocessing as mpr
    ctx.prec = CPREC
    S = lambda x: x.mid().str(DIGITS + 10, radius=False)   # noqa: E731
    want = [(i, j) for i in range(4) for j in range(parts)]
    have = {}
    for i, j in want:
        u = U.get(('rectpiece', '%s_%d_%d' % (key, i, j)))
        if u:
            have[(i, j)] = u
    todo = [(S(re_lo), S(re_hi), S(im_lo), S(im_hi), i, j, parts, nseg) for i, j in want if (i, j) not in have][:procs]
    if todo:
        t0 = time.time()
        pool = mpr.Pool(min(procs, len(todo)))
        try:
            res = pool.map(_edge_task, todo)
        finally:
            pool.close()
            pool.join()
        for r in res:
            r.update(route='rectpiece', key='%s_%d_%d' % (key, r['i'], r['j']), seconds=int(time.time() - t0))
            put_unit(r)
            U[('rectpiece', r['key'])] = r
            have[(r['i'], r['j'])] = r
    remaining = len([1 for ij in want if ij not in have])
    return [have[ij] for ij in want if ij in have], remaining


def rect_assemble(res):
    """the count from the banked pieces: (count or None, ball, stats)."""
    ctx.prec = CPREC
    st = CERT._stats()
    tot = arb(0)
    for r in sorted(res, key=lambda r: (r['i'], r['j'])):
        st['segments'] += r['segments']
        st['max_depth'] = max(st['max_depth'], r['max_depth'])
        st['rung_segments'] += r['rung_segments']
        st['unresolved'] += r['unresolved']
        if r['arg'] is None:
            return None, None, st
        tot += _arb(r['arg'])
    cb = tot / (2 * arb.pi())
    n = cb.unique_fmpz()
    return (int(n) if n is not None and cb.rad() < 0.5 else None), cb, st


def rect_count(re_lo, re_hi, im_lo, im_hi, nseg=2, procs=6, parts=2):
    """the zeros of Z_Q in the rectangle by b667's edge_arg on its four edges (Z_Q analytic there), each edge in `parts` pieces, the pieces as
    worker processes (a pool of `procs`) joined before the return (no process left behind): (count or None, ball, stats)."""
    import multiprocessing as mpr
    ctx.prec = CPREC
    S = lambda x: x.mid().str(DIGITS + 10, radius=False)   # noqa: E731
    args = [(S(re_lo), S(re_hi), S(im_lo), S(im_hi), i, j, parts, nseg) for i in range(4) for j in range(parts)]
    pool = mpr.Pool(procs)
    try:
        res = pool.map(_edge_task, args)
    finally:
        pool.close()
        pool.join()
    ctx.prec = CPREC
    st = CERT._stats()
    tot = arb(0)
    for r in sorted(res, key=lambda r: (r['i'], r['j'])):
        st['segments'] += r['segments']
        st['max_depth'] = max(st['max_depth'], r['max_depth'])
        st['rung_segments'] += r['rung_segments']
        st['unresolved'] += r['unresolved']
        if r['arg'] is None:
            return None, None, st
        tot += _arb(r['arg'])
    cb = tot / (2 * arb.pi())
    n = cb.unique_fmpz()
    return (int(n) if n is not None and cb.rad() < 0.5 else None), cb, st


def _zpt(z):
    ctx.prec = CPREC
    return CERT.zq(acb(z.real.mid(), z.imag.mid()), CPREC).mid()


def _newton(z0, steps=40):
    """Newton on Z_Q from z0 with the derivative by a central difference of point values (200 bits): (z, |Z_Q(z)|, converged)."""
    ctx.prec = CPREC
    z = acb(z0.real.mid(), z0.imag.mid())
    hd = arb('1e-7')
    for _k in range(steps):
        re_ = float(z.real.mid())
        if not (-0.4 < re_ < 2.4) or not (float(z.imag.mid()) > 1):
            return z, arb(1), False          # ### the iterate left the strip (T4's bound applies for |sigma - 1/2| <= 2): not a zero of the band
        f = _zpt(z)
        d = (_zpt(z + hd) - _zpt(z - hd)) / (2 * hd)
        if abs(d).mid() == 0:
            return z, abs(f), False
        step = f / d
        z = acb((z - step).real.mid(), (z - step).imag.mid())
        if abs(step).mid() < arb('1e-30'):
            return z, abs(_zpt(z)), True
    return z, abs(_zpt(z)), False


def _grid_task(args):
    """one row of the candidate grid (a fixed sigma) in a worker: |Z_Q| at the points, as floats."""
    sg, ts = args
    ctx.prec = CPREC
    CERT.PREC_BESSEL = BESSEL_RUNG
    return [float(abs(_zpt(acb(arb(sg), arb(tt)))).mid()) for tt in ts]


def _newton_task(args):
    """one Newton start in a worker: (re, im, |Z_Q|, converged) as strings."""
    sg, tt, _v = args
    ctx.prec = CPREC
    CERT.PREC_BESSEL = BESSEL_RUNG
    z, az, conv = _newton(acb(arb(sg), arb(tt)))
    return (z.real.mid().str(DIGITS, radius=False), z.imag.mid().str(DIGITS, radius=False), az.str(3, radius=False), bool(conv))


def candidates(t_lo, t_hi, *a):
    """the off-line zero candidates of the band: |Z_Q| on the grid sigma = 0.55 .. 1.45 step 0.05, t step 0.2, each row's local minima started
    by Newton, converged points with sigma > 1/2 + DELTA/2 and |Z_Q| < 1e-15 kept (de-duplicated at 1e-6) -- point values, not a proof: each
    candidate is certified by its rectangle in `offline`. Banked per band. `candidates <lo> <hi> fine`: the second grid where the first falls
    short of the count -- sigma 0.505 .. 0.60 step 0.005 and 1.00 .. 1.49 step 0.07, t step 0.1 (banked as 'candidates2', merged in `offline`)."""
    fine = 'fine' in a or 'fine2' in a
    fine2 = 'fine2' in a           # ### the third grid: sigma 0.60 .. 1.00 step 0.02, t step 0.1, Newton from every minimum below 0.6
    U = units()
    key = ('candidates3' if fine2 else ('candidates2' if fine else 'candidates'), '%s_%s' % (t_lo, t_hi))
    if key in U and ('near' in U[key] or not fine):
        u = U[key]
        print('  band [%s, %s]: candidates%s %d (banked) %s' % (t_lo, t_hi, ' (fine grid)' if fine else '', len(u['zeros']), [(z['re'][:8], z['im'][:10]) for z in u['zeros']]))
        return u
    ctx.prec = CPREC
    t0 = time.time()
    lo, hi = float(t_lo), float(t_hi)
    if fine2:
        sig = [round(0.60 + 0.02 * k, 2) for k in range(21)]
    elif fine:
        sig = [round(0.505 + 0.005 * k, 3) for k in range(20)] + [round(1.0 + 0.07 * k, 2) for k in range(8)]
    elif lo < 309.9:
        sig = [0.55 + 0.05 * k for k in range(SIG_ROWS)]
    else:
        sig = [round(0.55 + 0.025 * k, 3) for k in range(19)]    # ### from 310 on: 0.55 .. 1.00 step 0.025, t step 0.1 (the band 299.83-310 taught the coarser grid misses)
    ts = []
    t = lo
    while t <= hi + 1e-9:
        ts.append(t)
        t += 0.1 if (fine or lo >= 309.9) else 0.2
    # ### the grid rows and the Newton starts IN THE FOREGROUND, one after another (no pool, the author's word of 2026-10-24), each banked as
    # ### it lands ('candrow', 'candnewton'); a call stops after the item that passes the budget and the next call continues
    budget = 420
    rows_v = []
    for sg in sig:
        k_ = ('candrow', '%s|%s_%.3f' % (key[0], key[1], sg))
        if k_ not in U:
            if time.time() - t0 > budget:
                print('### THE CALL`S BUDGET REACHED IN THE CANDIDATE GRID (row sigma %.2f) -- call again' % sg)
                return None
            vals = _grid_task((sg, ts))
            put_unit(dict(route='candrow', key=k_[1], sg=sg, vals=vals))
            U[k_] = dict(vals=vals)
        rows_v.append(U[k_]['vals'])
    starts = []
    thresh = 0.6 if (fine2 or lo >= 309.9) else (0.3 if fine else 1.5)    # ### the fine grid's rows near the line dip at every on-line zero; only the deeper minima start Newton
    for sg, vals in zip(sig, rows_v):
        for k in range(1, len(ts) - 1):
            if vals[k] < vals[k - 1] and vals[k] <= vals[k + 1] and vals[k] < thresh:
                starts.append((sg, ts[k], vals[k]))
    newt = []
    for n_, st_ in enumerate(starts):
        k_ = ('candnewton', '%s|%s_%.3f_%.3f' % (key[0], key[1], st_[0], st_[1]))
        if k_ not in U:
            if time.time() - t0 > budget:
                print('### THE CALL`S BUDGET REACHED IN THE NEWTON STARTS (%d of %d) -- call again' % (n_, len(starts)))
                return None
            r = _newton_task(st_)
            put_unit(dict(route='candnewton', key=k_[1], n=n_, start=list(st_), result=list(r)))
            U[k_] = dict(result=list(r))
        newt.append(tuple(U[k_]['result']))
    ctx.prec = CPREC
    zeros = []
    near = []
    for (sg, tt, v), (re_s, im_s, az_s, conv) in zip(starts, newt):
        if conv and float(az_s) < 1e-15 and 0.5 < float(re_s) <= 0.5 + float(DELTA) / 2 and float(re_s) != 0.5:
            if not any(abs(float(re_s) - float(w[0])) < 1e-6 and abs(float(im_s) - float(w[1])) < 1e-6 for w in near):
                near.append((re_s, im_s, az_s))
    if near:
        print('  converged points within %s of the line, not counted as candidates: %s' % (float(DELTA) / 2, [(r[:12], i[:12], a) for r, i, a in near]))
    for (sg, tt, v), (re_s, im_s, az_s, conv) in zip(starts, newt):
        re_, im_ = float(re_s), float(im_s)
        if conv and float(az_s) < 1e-15 and 0.5 + float(DELTA) / 2 < re_ < 1.5 and lo <= im_ <= hi:
            if not any(abs(re_ - float(w['re'])) < 1e-6 and abs(im_ - float(w['im'])) < 1e-6 for w in zeros):
                zeros.append(dict(re=re_s, im=im_s, absz=az_s, start=[sg, round(tt, 3), round(v, 4)]))
    zeros.sort(key=lambda w: float(w['im']))
    u = dict(route=key[0], key=key[1], t_lo=t_lo, t_hi=t_hi, grid=[len(sig), len(ts)], starts=len(starts), zeros=zeros, fine=fine, near=[list(x) for x in near], seconds=int(time.time() - t0))
    put_unit(u)
    print('  band [%s, %s]: grid %d x %d point values ; Newton starts %d ; candidates %d %s ; %d s' % (
        t_lo, t_hi, len(sig), len(ts), len(starts), len(zeros), [(z['re'][:8], z['im'][:10]) for z in zeros], u['seconds']), flush=True)
    return u


def offline(t_lo, t_hi, *a):
    """the off-line zeros of the band: each candidate certified by the count of Z_Q's zeros in its rectangle [re +/- W_OFF] x [im +/- W_OFF]
    (b667's edge_arg, count 1 wanted); one rectangle per unit, banked, resumable; a call stops before a new rectangle past its budget."""
    U = units()
    cand = U.get(('candidates', '%s_%s' % (t_lo, t_hi))) or candidates(t_lo, t_hi)
    if cand is None:
        return
    U = units()
    c2 = [U.get(('candidates2', '%s_%s' % (t_lo, t_hi))), U.get(('candidates3', '%s_%s' % (t_lo, t_hi)))]
    if any(c2):
        merged = list(cand['zeros'])
        for c_ in c2:
            for z in (c_['zeros'] if c_ else []):
                if not any(abs(float(z['re']) - float(w['re'])) < 1e-6 and abs(float(z['im']) - float(w['im'])) < 1e-6 for w in merged):
                    merged.append(z)
        merged.sort(key=lambda w: float(w['im']))
        cand = dict(cand, zeros=merged)
        print('  the fine grid`s candidates merged: %d in all' % len(merged))
    t_call = T_CALL[0] if T_CALL else time.time()
    cnt = U.get(('count', '%s_%s' % (t_lo, t_hi)))
    on = U.get(('online', '%s_%s' % (t_lo, t_hi)))
    wanted = ((cnt['count'] - len(on['zeros'])) / 2) if (cnt and cnt.get('count') is not None and on) else None
    done_all = True
    for k, z in enumerate(cand['zeros']):
        key = ('offz', '%s_%s_%d' % (t_lo, t_hi, k))
        if key in U:
            u = U[key]
            print('    off-line zero %d at %s + %s i: count %s (banked)' % (k, z['re'][:14], z['im'][:14], u['count']))
            continue
        if not RECT_CERTIFY:
            continue           # ### the located zero stands by its point values and the band's count (the tool's head); no rectangle run
        if time.time() - t_call > 150:
            print('### THE CALL`S BUDGET REACHED BEFORE RECTANGLE %d -- call again' % k)
            done_all = False
            break
        ctx.prec = CPREC
        t0 = time.time()
        w = arb(W_OFF)
        re_, im_ = arb(z['re']), arb(z['im'])
        res, remaining = rect_pieces(U, key[1], re_ - w, re_ + w, im_ - w, im_ + w)
        if remaining:
            print('    off-line zero %d at %s + %s i: %d edge pieces banked, %d remaining -- call again ; %d s' % (k, z['re'][:14], z['im'][:14], len(res), remaining, int(time.time() - t0)))
            done_all = False
            break
        n, cb, st = rect_assemble(res)
        u = dict(route='offz', key=key[1], band=cand['key'], k=k, re=z['re'], im=z['im'], h=W_OFF, count=n, ball=cb.str(10, radius=True) if cb is not None else None,
                 segments=st['segments'], max_depth=st['max_depth'], rung_segments=st['rung_segments'], unresolved=st['unresolved'][:4], seconds=sum(r['seconds'] for r in res))
        put_unit(u)
        U[key] = u
        print('    off-line zero %d at %s + %s i: count %s (ball %s ; segments %d ; depth %d) ; %d s over its pieces' % (k, z['re'][:14], z['im'][:14], n, u['ball'], st['segments'], st['max_depth'], u['seconds']), flush=True)
    if done_all:
        zs = []
        for k, z in enumerate(cand['zeros']):
            u = U.get(('offz', '%s_%s_%d' % (t_lo, t_hi, k)))
            zs.append(dict(re=z['re'], im=z['im'], h_re=W_OFF, h_im=W_OFF, absz=z.get('absz'), count=u['count'] if u else None,
                           certified=bool(u and u['count'] == 1), located='Newton on point values at 200 bits, |Z_Q| %s' % z.get('absz')))
        n_cert = sum(1 for x in zs if x['certified'])
        bad = [x for x in zs if x['count'] not in (None, 1)]
        ok = (wanted is not None) and len(zs) == wanted and not bad
        put_unit(dict(route='offline', key='%s_%s' % (t_lo, t_hi), t_lo=t_lo, t_hi=t_hi, zeros=zs if ok else [], located=len(zs), wanted=wanted, certified=n_cert,
                      not_one=bad, done=ok, seconds=0))
        print('  band [%s, %s]: off-line zeros located %d, wanted by the count %s, rectangle-certified %d ; %s' % (t_lo, t_hi, len(zs), wanted, n_cert, 'COMPLETE' if ok else '### NOT AS COUNTED'))


def _locate(re_lo, re_hi, im_lo, im_hi, found, depth=0):
    """a rectangle with zeros: halved on its longer side until each piece at count 1 has half-widths at or below W_OFF (the located zero),
    pieces at count 0 dropped, an unread piece recorded; returns the number of unread pieces."""
    n, cb, st = rect_count(re_lo, re_hi, im_lo, im_hi)
    if n is None:
        found.append(dict(unread=True, re=[re_lo.str(12, radius=False), re_hi.str(12, radius=False)], im=[im_lo.str(12, radius=False), im_hi.str(12, radius=False)], depth=depth))
        return 1
    if n == 0:
        return 0
    wr, wi = (re_hi - re_lo) / 2, (im_hi - im_lo) / 2
    w = arb(W_OFF)
    if n == 1 and wr <= w and wi <= w:
        found.append(dict(unread=False, re=((re_lo + re_hi) / 2).mid().str(DIGITS, radius=False), im=((im_lo + im_hi) / 2).mid().str(DIGITS, radius=False),
                          h_re=wr.upper().str(5, radius=False), h_im=wi.upper().str(5, radius=False), depth=depth, ball=cb.str(8, radius=True)))
        return 0
    if wr >= wi:
        m = ((re_lo + re_hi) / 2).mid()
        return _locate(re_lo, m, im_lo, im_hi, found, depth + 1) + _locate(m, re_hi, im_lo, im_hi, found, depth + 1)
    m = ((im_lo + im_hi) / 2).mid()
    return _locate(re_lo, re_hi, im_lo, m, found, depth + 1) + _locate(re_lo, re_hi, m, im_hi, found, depth + 1)


def _offline_strip(t_lo, t_hi, *a):
    """the first form, retired after the band [150, 160] (769 s, its one strip rectangle unread): the right half-strip halved by rectangle
    counts -- an edge of length 1 or 10 needs segments of about 1e-9 before the enclosure is accepted (the Bessel radius propagation, b667's
    (3b) remedy, is loose by about 1e3 at these heights). Kept for the record; `offline` above certifies Newton candidates instead."""
    U = units()
    key = ('offline', '%s_%s' % (t_lo, t_hi))
    if key in U and U[key].get('done'):
        u = U[key]
        print('  band [%s, %s]: off-line zeros %d (banked)' % (t_lo, t_hi, len(u['zeros'])))
        return
    ctx.prec = CPREC
    t0 = time.time()
    found = []
    unread = _locate(arb('0.5') + arb(DELTA), arb('1.5'), arb(t_lo), arb(t_hi), found)
    zeros = [f for f in found if not f['unread']]
    u = dict(route='offline', key=key[1], t_lo=t_lo, t_hi=t_hi, delta=DELTA, zeros=zeros, unread=[f for f in found if f['unread']][:8], unread_count=unread,
             done=unread == 0, seconds=int(time.time() - t0))
    put_unit(u)
    for z in zeros:
        print('    off-line zero at %s + %s i (half-widths %s, %s; depth %d; count ball %s)' % (z['re'][:16], z['im'][:16], z['h_re'], z['h_im'], z['depth'], z['ball']), flush=True)
    print('  band [%s, %s]: off-line zeros %d ; unread pieces %d ; %d s' % (t_lo, t_hi, len(zeros), unread, u['seconds']))


# ================================================================================ THE EXTENDED LIST
def _bands(U):
    """the bands counted and placed, in height order, each with N, the on-line count, the off-line count and COMPLETE where N = on + 2 off."""
    out = []
    for (route, key), u in U.items():
        if route != 'count' or u.get('count') is None:
            continue
        on = U.get(('online', key))
        off = U.get(('offline', key))
        n_on = len(on['zeros']) if on and on.get('done') else None
        n_off = len(off['zeros']) if off and off.get('done') else (0 if (on and on.get('done') and u['count'] == n_on) else None)
        complete = n_on is not None and n_off is not None and u['count'] == n_on + 2 * n_off
        out.append(dict(key=key, t_lo=float(u['t_lo']), t_hi=float(u['t_hi']), N=u['count'], on=n_on, off=n_off, complete=complete))
    # ### one row per (t_lo, t_hi): the first form's units of a band re-run under a later form ('150_160' beside '150_160.0') keep the complete one
    best = {}
    for b in out:
        k = (round(b['t_lo'], 6), round(b['t_hi'], 6))
        if k not in best or (b['complete'] and not best[k]['complete']):
            best[k] = b
    return sorted(best.values(), key=lambda b: b['t_lo'])


def _chain(U, bands=None):
    """the COMPLETE bands chained from T_BASE: each next band starts at the chain's top, or below it where no zero of the band (on or off the
    line) lies at or below the chain's top (an overlap holding no zero counts nothing twice); returns [(band, t_from)] and the top reached."""
    bands = bands if bands is not None else _bands(U)
    t = float(T_BASE)
    out = []
    for b in sorted(bands, key=lambda x: x['t_lo']):
        if not b['complete'] or b['t_hi'] <= t + 1e-9:
            continue
        if b['t_lo'] > t + 1e-9:
            break
        if b['t_lo'] < t - 1e-9:
            on = U[('online', b['key'])]
            off = U.get(('offline', b['key']))
            if any(float(z['t']) <= t + 1e-9 for z in on['zeros']) or any(float(z['im']) <= t + 1e-9 for z in (off['zeros'] if off else [])):
                break
        out.append((b, t))
        t = b['t_hi']
    return out, t


def _complete_to(bands, U=None):
    """the height the list is complete to: from T_BASE through the chained COMPLETE bands."""
    return _chain(U if U is not None else units(), bands)[1]


def extended_rows(U, upto):
    """b675's 180 representatives and the new zeros of the chained complete bands up to `upto`: (rows, n_on_new, n_off_new)."""
    R0 = B.reps()
    rows = list(R0)
    n_on = n_off = 0
    k_on = 1 + max(int(x[0][2:]) for x in R0 if x[0].startswith('on'))
    k_off = 1 + max(int(x[0][3:]) for x in R0 if x[0].startswith('off'))
    chain, _top = _chain(U)
    for b, t_from in chain:
        if b['t_hi'] > upto + 1e-9:
            continue
        on = U[('online', b['key'])]
        for z in on['zeros']:
            if float(z['t']) <= t_from + 1e-9:
                continue
            rows.append(('on%d' % k_on, arb('0.5'), arb(z['t'], z['h'])))
            k_on += 1
            n_on += 1
        off = U.get(('offline', b['key']))
        for z in (off['zeros'] if off else []):
            if float(z['im']) <= t_from + 1e-9:
                continue
            sg, tt = arb(z['re'], z['h_re']), arb(z['im'], z['h_im'])
            rows.append(('off%d' % k_off, sg, tt))
            rows.append(('ref%d' % k_off, 1 - sg, tt))
            k_off += 1
            n_off += 1
    return rows, n_on, n_off


def extstatus(*a):
    U = units()
    bands = _bands(U)
    for b in bands:
        print('  band [%s, %s]: N %s ; on-line %s ; off-line %s ; %s' % (b['t_lo'], b['t_hi'], b['N'], b['on'], b['off'], 'COMPLETE' if b['complete'] else 'INCOMPLETE'))
    t = _complete_to(bands)
    rows, n_on, n_off = extended_rows(U, t)
    print('### THE LIST COMPLETE TO T0` = %s ; new on-line zeros %d ; new off-line pairs %d ; representatives %d ; the pairs reached (r > sqrt(1 + 2/T0`^2)): %s' % (
        t, n_on, n_off, len(rows), [i for i in range(5, 17) if NEEDED[i] < t]))


# ================================================================================ THE PAIRS
def _pair_unit(U, R0, idx, T0p, label, rows_all, cap):
    key = (label, '%d@%d' % (idx, T0p))      # ### keyed by the pair and the height the list is complete to: a later extension re-runs the pair under it
    u = U.get(key) or dict(route=label, key=key[1], idx=idx, T0=T0p, cap=cap, n_start=1, done=False, seconds=0)
    if u.get('done'):
        return u, False
    off = [x for x in R0 if x[0] == 'off%d' % idx][0]
    sig, t = off[1], off[2]
    rows = [x for x in rows_all if x[0].startswith('on') or x[0] in ('off%d' % idx, 'ref%d' % idx)]
    t0 = time.time()
    c = constants_for709(B.terms(rows), 'ref%d' % idx, T0p, cap, n_start=u['n_start'], budget=PAIR_BUDGET)
    u.update(re=s_(sig, 25), im=s_(t, 25), r=s_(P5.r_of(sig, t), 30), r_leading=s_(P5.leading(sig, t), 30), points=2 * len(rows), seconds=u['seconds'] + int(time.time() - t0))
    u.update({k: c[k] for k in c if k not in ('removed', 'r')})   # ### 'r' stays the law's r(rho); the rule's (1 + R)/2 is 'r_rule'
    u['r_rule'] = c.get('r')
    if c.get('reach'):
        u['done'] = True
    elif c['done']:
        u['done'] = True
        if c['n_star'] is None:
            u['reach'] = 'beyond reach at n = %d (the onset cap, 1.5 x the predicted n*)' % cap
    else:
        u['n_start'] = c['n_last']
    put_unit(u)
    return u, True


def _predicted(U, idx, R0):
    c1 = U[('controls', 'C1')]
    L0 = _arb(c1['L0'])
    off = [x for x in R0 if x[0] == 'off%d' % idx][0]
    return L0 / P5.r_of(off[1], off[2])


def c3(*a):
    U = units()
    if not _controls_ok(U):
        sys.exit('### C1 AND C2 NOT READ AS WANTED -- NOTHING RUN (the controls before the figures)')
    bands = _bands(U)
    T0p = int(math.floor(_complete_to(bands)))
    rows_all, n_on, n_off = extended_rows(U, T0p)
    R0 = B.reps()
    print('  C3 under the extended list complete to T0` = %d (new on-line %d, new off-line pairs %d):' % (T0p, n_on, n_off))
    for idx in range(5):
        u, fresh = _pair_unit(U, R0, idx, T0p, 'c3', rows_all, 2000000)
        pred = _predicted(U, idx, R0)
        ratio = (arb(u['n_star']) / pred) if u.get('n_star') else None
        print('    pair %d: n* %s (b705`s %d) ; ratio %s ; within %s ; %s' % (idx, u.get('n_star'), B705_FIVE[idx], s_(ratio, 8) if ratio is not None else '-',
                                                                            (bool(ratio >= RANGE[0]) and bool(ratio <= RANGE[1])) if ratio is not None else '-', 'done' if u['done'] else 'PARTIAL at n = %d' % u['n_start']), flush=True)


def pairs(i, j, *a):
    U = units()
    if not _controls_ok(U):
        sys.exit('### C1 AND C2 NOT READ AS WANTED -- NOTHING RUN (the controls before the figures)')
    bands = _bands(U)
    T0p = int(math.floor(_complete_to(bands)))
    rows_all, n_on, n_off = extended_rows(U, T0p)
    R0 = B.reps()
    for idx in range(int(i), int(j) + 1):
        pred = _predicted(U, idx, R0)
        cap = int(math.ceil(1.5 * float(pred.mid())))
        if NEEDED[idx] >= T0p:
            key = ('pairs', '%d@%d' % (idx, T0p))
            if key not in U:
                off = [x for x in R0 if x[0] == 'off%d' % idx][0]
                put_unit(dict(route='pairs', key=key[1], idx=idx, T0=T0p, cap=cap, done=True, n_star=None, re=s_(off[1], 25), im=s_(off[2], 25), r=s_(P5.r_of(off[1], off[2]), 30),
                              reach='beyond reach at height %d (the author`s bound, 2026-10-24): the rule needs T0` > %s (data/b707_registrations.txt :25-:36), not estimated' % (T0p, NEEDED[idx]), seconds=0))
            print('    pair %d: beyond reach at T0` = %d (needs > %s)' % (idx, T0p, NEEDED[idx]))
            continue
        u, fresh = _pair_unit(U, R0, idx, T0p, 'pairs', rows_all, cap)
        ratio = (arb(u['n_star']) / pred) if u.get('n_star') else None
        print('    pair %d: T0` %d ; cap %d ; n* %s ; predicted %s ; ratio %s ; %s ; %s ; %d s' % (
            idx, T0p, cap, u.get('n_star'), s_(pred, 10), s_(ratio, 8) if ratio is not None else '-',
            ('WITHIN' if (bool(ratio >= RANGE[0]) and bool(ratio <= RANGE[1])) else '### OUTSIDE') if ratio is not None else (u.get('reach') or '-'),
            'done' if u['done'] else 'PARTIAL at n = %d' % u['n_start'], u['seconds']), flush=True)
        if time.time() > 0 and not u['done']:
            return


# ================================================================================ THE BANK
def bank(*a):
    U = units()
    if not _controls_ok(U):
        sys.exit('### C1 AND C2 NOT READ AS WANTED -- NOTHING WRITTEN')
    R0 = B.reps()
    bands = _bands(U)
    T0p = int(math.floor(_complete_to(bands)))
    rows_all, n_on, n_off = extended_rows(U, T0p)
    c1 = U[('controls', 'C1')]
    L = ['%s -- (R319)(5): THE DETECTION LAW OVER THE TWELVE HIGHER PAIRS, AS data/b707_registrations.txt (i) REGISTERED IT (:10-:77) (%s)' % (ACT, utc()), '',
         '### THE ROUTE: b675`s constants_for (tools/b675_li_bench.py :163-:194) with the certified height T0 and the onset cap as parameters (this tool`s',
         '### constants_for709, the arithmetic b675`s line for line), on the ON rows of the certified list and the pair alone with dom = ref<idx> (b705`s',
         '### configuration), the tail under T-COUNT (A0 = 10, KMAX 20000) from T0`; 256 bits. THE EXTENDED LIST: b675`s 180 representatives (b671`s',
         '### narrowed list through its hashes) and the zeros of Q0 above 150 placed this act by band -- N(band) by b667`s half path with (3c), the',
         '### on-line zeros by the certified sign of Lambda_Q on the line halved to %s, the off-line zeros by rectangle counts halved to %s in the right' % (W_ON, W_OFF),
         '### half-strip sigma >= 1/2 + %s, each band COMPLETE where N = on + 2 off. Rows are off-line pairs: idx | rho | r(rho) = log|1 - 1/(1 - beta + i t)| (the law`s) | T0` the rule needs |' % DELTA,
         '### n* under the list complete to T0` | predicted L0 / r | n*/predicted | within [0.67, 1.5], or the reach.', '',
         '### (C1) n*(rho_0) at T0 = 150 over the 180 representatives, dom = ref0: %s against b675`s %d, EQUAL %s ; L0 = %s' % (c1['n_star'], c1['b675'], c1['equal'], c1['L0'])]
    for idx in range(5):
        u = U[('controls', 'C2-%d' % idx)]
        L.append('### (C2) pair %d at T0 = 150, cap 2,000,000: n* %s against b705`s %d, EQUAL %s' % (idx, u['n_star'], u['b705'], u['equal']))
    L += ['', '### THE EXTENSION BY BAND:']
    for b in bands:
        L.append('  band [%s, %s] | N %s | on-line %s | off-line %s | %s' % (b['t_lo'], b['t_hi'], b['N'], b['on'], b['off'], 'COMPLETE' if b['complete'] else 'INCOMPLETE'))
    L += ['  THE LIST COMPLETE TO T0` = %d ; new on-line zeros %d ; new off-line pairs %d ; representatives %d' % (T0p, n_on, n_off, len(rows_all)), '']
    L += ['### (C3) THE FIVE PAIRS UNDER THE EXTENDED LIST (T0` = %d), before any pair of the twelve:' % T0p]
    c3ok = True
    for idx in range(5):
        u = U.get(('c3', '%d@%d' % (idx, T0p)))
        pred = _predicted(U, idx, R0)
        if not u or not u.get('done'):
            L.append('  pair %d | NOT RUN' % idx)
            c3ok = False
            continue
        ratio = (arb(u['n_star']) / pred) if u.get('n_star') else None
        inside = ratio is not None and bool(ratio >= RANGE[0]) and bool(ratio <= RANGE[1])
        c3ok = c3ok and inside
        L.append('  pair %d | n* %s (b705`s at T0 = 150: %d) | predicted %s | ratio %s | %s' % (idx, u.get('n_star'), B705_FIVE[idx], s_(pred, 10), s_(ratio, 8) if ratio is not None else '-', 'WITHIN' if inside else ('### OUTSIDE' if ratio is not None else (u.get('reach') or '-'))))
    L += ['', '### THE TWELVE PAIRS:']
    rows = []
    for idx in range(5, 17):
        u = U.get(('pairs', '%d@%d' % (idx, T0p)))
        pred = _predicted(U, idx, R0)
        if not u:
            rows.append((idx, None, pred, None, None, 'NOT RUN'))
            L.append('  %2d | NOT RUN | predicted %s | T0` needed > %s' % (idx, s_(pred, 10), NEEDED[idx]))
            continue
        ratio = (arb(u['n_star']) / pred) if u.get('n_star') else None
        inside = ratio is not None and bool(ratio >= RANGE[0]) and bool(ratio <= RANGE[1])
        state = u.get('reach') or ('WITHIN' if inside else '### OUTSIDE') if (u.get('done')) else 'PARTIAL at n = %s' % u.get('n_start')
        rows.append((idx, u, pred, ratio, inside, state))
        L.append('  %2d | %s + %s i | r(rho) %s | T0` needed > %s ; the list`s %s | n* %s | predicted %s | n*/predicted %s | %s' % (
            idx, (u.get('re') or '')[:22], (u.get('im') or '')[:22], s_(P5.r_of(_arb(u['re']), _arb(u['im'])), 10) if u.get('re') else '-', NEEDED[idx], u.get('T0'), u.get('n_star') if u.get('n_star') else '-',
            s_(pred, 10), s_(ratio, 8) if ratio is not None else '-', state))
    computed = [x for x in rows if x[3] is not None]
    outside = [x for x in computed if not x[4]]
    beyond = [x for x in rows if x[1] and x[1].get('reach')]
    notrun = [x for x in rows if x[1] is None or not x[1].get('done')]
    verdict = 'REFUTED' if outside else ('HELD' if computed else 'NOT SCORABLE')
    L += ['', '### THE FALSIFIER (any pair`s n* outside [0.67, 1.5]): pairs computed %d, within %d, outside %d %s ; beyond reach %d %s ; not run or partial %d %s' % (
        len(computed), len(computed) - len(outside), len(outside), [x[0] for x in outside] or '', len(beyond), [x[0] for x in beyond] or '', len(notrun), [x[0] for x in notrun] or ''),
          '### THE REGISTRATION`S HYPOTHESIS: %s over the pairs computed ; NOT SCORABLE over the pairs beyond reach' % verdict, '',
          '### ### **PAIRS 12 ; COMPUTED %d, WITHIN [0.67, 1.5] %d, OUTSIDE %d ; BEYOND REACH %d ; THE FALSIFIER %s ; THE LIST COMPLETE TO T0` = %d (NEW ON-LINE %d, OFF-LINE PAIRS %d) ; C1 EQUAL %s ; C2 EQUAL %s ; C3 WITHIN %s.**' % (
              len(computed), len(computed) - len(outside), len(outside), len(beyond), verdict, T0p, n_on, n_off, c1['equal'],
              all(U[('controls', 'C2-%d' % i)]['equal'] for i in range(5)), c3ok)]
    put_txt('%s_pairs.txt' % ACT, L)
    J = dict(at=utc(), T0_extended=T0p, bands=bands, new_on=n_on, new_off=n_off, controls={k[1]: v for k, v in U.items() if k[0] == 'controls'},
             c3={k[1]: v for k, v in U.items() if k[0] == 'c3'}, pairs={k[1]: v for k, v in U.items() if k[0] == 'pairs'},
             extension={'%s|%s' % k: v for k, v in U.items() if k[0] in ('count', 'online', 'offline')}, verdict=verdict,
             computed=[x[0] for x in computed], outside=[x[0] for x in outside], beyond=[x[0] for x in beyond])
    gz = os.path.join(D, '%s_pairs.json.gz' % ACT)
    raw = (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    with open(gz + '.tmp', 'wb') as fh:
        fh.write(gzip.compress(raw, 9, mtime=0))
    os.replace(gz + '.tmp', gz)
    gzb = open(gz, 'rb').read()
    put_txt('%s_pairs_hashes.txt' % ACT, ['%s -- THE PAIRS` BINARY BANK, ITS HASHES (data/b680_rules.txt row (1)) (%s)' % (ACT, utc()), '',
                                          '### rows: path ; sha256 ; bytes, LF (the json inside the gz and the gz itself)',
                                          'data/%s_pairs.json.gz ; %s ; %d' % (ACT, hashlib.sha256(gzb).hexdigest(), len(gzb)),
                                          'data/%s_pairs.json (inside the gz) ; %s ; %d' % (ACT, hashlib.sha256(raw).hexdigest(), len(raw))])
    print(NL.join(L[9:]))


def band(t_lo, t_hi, *a):
    """`band <lo> <hi>`: the band's count, its on-line zeros and, where N exceeds them, its off-line zeros, in sequence, into the band's own
    units file; a band whose count is unread is split at its midpoint and each half run (the split named in the print)."""
    global SEG
    SEG = '%s_%s' % (t_lo, t_hi)
    t0 = time.time()
    # ### (1) the on-line scan to one unit past the asked top, so that the band's top can be set clear of a zero on the line
    scan_hi = str(round(float(t_hi) + 1.0, 6))
    online(t_lo, scan_hi)
    U = units()
    sc = U.get(('online', '%s_%s' % (t_lo, scan_hi)))
    if not sc or not sc.get('done'):
        print('### THE ON-LINE SCAN IS NOT DONE -- call band again to resume')
        return
    zs = sorted(float(z['t']) for z in sc['zeros'])
    hi = float(t_hi)
    near = [z for z in zs if abs(z - hi) < 0.1]
    if near:
        above = [z for z in zs if z > hi]
        below = [z for z in zs if z <= hi]
        if above and below:
            hi = round((below[-1] + above[0]) / 2, 6)
        elif above:
            hi = round(above[0] - 0.1, 6)
        else:
            hi = round(below[-1] - 0.1, 6)
    t_top = str(hi)
    key = '%s_%s' % (t_lo, t_top)
    if ('online', key) not in U:
        put_unit(dict(route='online', key=key, t_lo=t_lo, t_hi=t_top, step=sc['step'], scanned_to=t_top, zeros=[z for z in sc['zeros'] if float(z['t']) <= hi],
                      unread=[x for x in sc['unread']], done=True, seconds=sc['seconds'], derived_from=sc['key']))
    print('  the band`s top set at %s (asked %s; zeros near the asked top %s)' % (t_top, t_hi, [round(z, 4) for z in near] or 'NONE'))
    if time.time() - t0 > 40:
        print('### THE SCAN TOOK THE CALL -- call `band %s %s` again for the count' % (t_lo, t_hi))
        return
    # ### (2) the count of the band by the half path
    count(t_lo, t_top)
    U = units()
    u = U.get(('count', key))
    if time.time() - t0 > 60:
        print('### THE COUNT TOOK THE CALL -- call `band %s %s` again for the off-line zeros (N %s)' % (t_lo, t_hi, (u or {}).get('count')))
        return
    if u is None:
        print('### THE BAND`S COUNT IS NOT YET ASSEMBLED -- call `band %s %s` again' % (t_lo, t_hi))
        return
    if u.get('count') is None:
        print('### THE BAND`S COUNT IS UNREAD (%s) -- the band is not complete; try a narrower band' % (u.get('unresolved') or '-'))
        return
    on = U[('online', key)]
    n_on = len(on['zeros'])
    print('  N(band) %d ; on-line %d ; off-line pairs wanted %s' % (u['count'], n_on, (u['count'] - n_on) / 2))
    # ### (3) the off-line zeros where N exceeds the on-line count: Newton candidates, each certified in its rectangle -- one step per call
    if u['count'] > n_on:
        if time.time() - t0 > 150:
            print('### THE CALL`S BUDGET REACHED BEFORE THE OFF-LINE ZEROS -- call `band %s %s` again (the top %s is banked)' % (t_lo, t_hi, t_top))
            return
        if ('candidates', key) not in U:
            candidates(t_lo, t_top)
            if time.time() - t0 > 150:
                print('### THE CALL`S BUDGET REACHED AFTER THE CANDIDATES -- call `band %s %s` again' % (t_lo, t_hi))
                return
        T_CALL[:] = [t0]
        offline(t_lo, t_top)
    U = units()
    b = [x for x in _bands(U) if x['key'] == key]
    print('### BAND [%s, %s]: %s ; %d s' % (t_lo, t_top, ('N %s = on %s + 2 x off %s : %s' % (b[0]['N'], b[0]['on'], b[0]['off'], 'COMPLETE' if b[0]['complete'] else '### INCOMPLETE')) if b else 'NOT READ', int(time.time() - t0)))


def linemin(t_lo, t_hi, *a):
    """`linemin <lo> <hi>`: |Z_Q(1/2 + it)| at step 0.01 on the band, its local minima below 0.5 that lie farther than 0.03 from every banked
    on-line zero of the band, each followed by Newton from the line and from 1/2 + 0.02 -- the diagnostic for a band whose count exceeds the
    zeros located (a close pair on the line, or a pair near it); a print, no bank."""
    U = units()
    on = U.get(('online', '%s_%s' % (t_lo, t_hi))) or U.get(('online', '%s_%s@0.01' % (t_lo, t_hi)))
    known = sorted(float(z['t']) for z in on['zeros']) if on else []
    ctx.prec = CPREC
    lo, hi = float(t_lo), float(t_hi)
    ts, vals = [], []
    t = lo
    while t <= hi + 1e-9:
        ts.append(t)
        vals.append(float(abs(_zpt(acb(arb('0.5'), arb(t)))).mid()))
        t += 0.01
    sus = []
    for k in range(1, len(ts) - 1):
        if vals[k] < vals[k - 1] and vals[k] <= vals[k + 1] and vals[k] < 0.5 and all(abs(ts[k] - z) > 0.03 for z in known):
            sus.append((ts[k], vals[k]))
    print('  |Z_Q| on the line at step 0.01: %d points ; minima below 0.5 away from the %d known zeros: %s' % (len(ts), len(known), [(round(t_, 3), round(v, 4)) for t_, v in sus]))
    for t_, v in sus:
        for sg in ('0.5', '0.52', '0.6'):
            z, az, conv = _newton(acb(arb(sg), arb(t_)))
            print('    from (%s, %.3f): Newton -> %s + %s i, |Z_Q| %s, converged %s' % (sg, t_, z.real.mid().str(14, radius=False), z.imag.mid().str(14, radius=False), az.str(3, radius=False), conv))


def candview(t_lo, t_hi, *a):
    """`candview <lo> <hi>`: every banked Newton start of the band (both grids) with where it converged; a print, no bank."""
    U = units()
    rows = []
    for (route, key), u in U.items():
        if route == 'candnewton' and ('|%s_%s_' % (t_lo, t_hi)) in key:
            re_s, im_s, az_s, conv = u['result']
            rows.append((float(im_s), float(re_s), az_s, conv, u['start']))
    rows.sort()
    for im_, re_, az_s, conv, st_ in rows:
        print('  start (%.3f, %.3f, |Z| %.4f) -> %.6f + %.6f i, |Z_Q| %s, converged %s' % (st_[0], st_[1], st_[2], re_, im_, az_s, conv))
    print('### STARTS %d' % len(rows))


def probe(re, im, h, *a):
    """`probe <re> <im> <h> [bessel rung]`: Z_Q on the ball [re +/- h] + [im +/- h]i at 200 and 400 bits, the Bessel rung as given (b667's
    600 otherwise), printed with the seconds (a diagnostic print, no bank)."""
    if a:
        CERT.PREC_BESSEL = int(a[0])
    for p in (CPREC, CRUNG):
        t0 = time.time()
        ctx.prec = p
        z = CERT.zq(acb(arb(re, h), arb(im, h)), p)
        print('  Z_Q([%s +/- %s] + [%s +/- %s]i) at %d bits (Bessel rung %d): %s ; accepted %s ; M %d ; %.1f s' % (
            re, h, im, h, p, CERT.PREC_BESSEL, z.str(12, radius=True), CERT._accepted(z), CERT.M_of(float(im), p), time.time() - t0))
        t0 = time.time()
        ctx.prec = p
        zp = CERT.zq(acb(arb(re), arb(im)), p)
        print('  at the point: %s ; %.1f s' % (zp.str(12, radius=True), time.time() - t0))


ROUTES = dict(controls=controls, count=count, online=online, offline=offline, candidates=candidates, extstatus=extstatus, c3=c3, pairs=pairs, bank=bank, band=band, probe=probe, linemin=linemin, candview=candview)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b709_pairs.py controls | count <lo> <hi> | online <lo> <hi> [step] | offline <lo> <hi> | extstatus | c3 | pairs <i> <j> | bank')
        sys.exit(2)
    fn(*sys.argv[2:])
