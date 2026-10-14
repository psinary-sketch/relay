# -*- coding: utf-8 -*-
"""b667_epstein_certify.py -- Q0'S ZEROS BELOW HEIGHT 150 ISOLATED IN ARB BALLS BY AN ARGUMENT-PRINCIPLE COUNT, THE LIST'S COMPLETENESS
COUNTED BY THE SAME FORM, under (R277)(3)-(5) with (3a) in force, on the author's word on the plan (relay data/b667_epstein_plan.txt at
4c972bb1, relay data/b667_author_answers.txt).

### THE ROUTE (plan sections 2 and 11): Z_Q(s) = T1 + T2 + T3 + T4 (Chowla-Selberg, Q0 = x² + xy + 6y²):
###   T1 = 2 ζ(2s); T2 = 2 √π Γ(s − ½) Γ(s)⁻¹ (√23/2)^{1−2s} ζ(2s − 1);
###   T3 = 8 π^s Γ(s)⁻¹ Σ_{m ≤ M} (−1)^m K_{s−½}(π√23 m) Σ_{k|m} k^{s−½} β_{m/k}^{½−s}, β_n = √23 n/2 (the sign (−1)^{kn} = (−1)^m, 11.1);
###   T4 the truncation, |T4| ≤ 8 |π^s Γ(s)⁻¹| C3 (M+1)^{|μ|} e^{−c(M+1)} / (1 − 2e^{−c}), c = π√23, C3 = 2 √(2/√23) e^{1/(2c)} (√23/2)^{|μ|},
###   μ = σ − ½ (11.2), added to the ball as its radius. M = ⌈(π|t|/2 + (prec + 20) ln 2)/(π√23)⌉ + 1.
### THE PRECISION: 200 bits; the 400 rung for a point value wider than a relative 2^-40 and for a segment unresolved at the depth limit;
### (3a) the Bessel factor alone climbs 200 -> 400 -> 600 bits while its term's radius, read at the evaluation's midpoint, is at or above
### 2^-60; every factor taken at 600 is logged with its m, its point (σ, t) and its precision (relay data/b667_bessel_rungs.txt).
### THE COUNT (plan section 5): segment enclosures -- a segment's ball enclosure of F accepted when it excludes 0 with radius at most half its
### midpoint's modulus; then its argument change is the principal arg(F(z_b)/F(z_a)) from the endpoint values; otherwise bisected to depth 16
### (squares) or 24 (paths), then the 400 rung once, then UNRESOLVED printed and not refined further.
### THE SQUARES (plan section 3, 11): half-width h = 1e-12 about each banked double, the ball the square; one widening to 1e-9 printed WIDENED.
### THE REGIONS (plan sections 4, 11): R = [−0.5, 1.5] × [0.5, 150] and B = [−0.5, 1.5] × [−0.5, 0.5], each by its half path under
### Λ_Q(1 − conj s) = conj Λ_Q(s): N(R) = (1/π) Δ_P arg Λ_Q ; zeros in B = (1/π) Δ_{P_B} arg Λ_Q + 2 (Λ_Q's poles at 0 and 1).
### THE ORDER (plan section 13): V1, V2, V3; C1; C2; R, then C3 on it; B; the Q0 squares; H1-H3 read.
### b326's banks are read and never written. No lean; no kernel file read. Nothing here is about ζ but C1.
### Usage: `python -X utf8 tools/b667_epstein_certify.py` -> data/b667_epstein_counts.txt, data/b667_epstein_zeros_certified.txt (.json),
### data/b667_bessel_rungs.txt. Written by the Write tool at b667, read back whole before it runs.
"""
import io
import json
import math
import multiprocessing as mpr
import os
import sys
import time

from flint import arb, acb, ctx

# ================================================================================ THE PLAN'S CONSTANTS (relay data/b667_epstein_plan.txt §13)
PREC = 200                         # ### Arb balls at 200 bits (relay data/b627_margin_inputs.txt :7)
PREC_RUNG = 400                    # ### the one rung of (R277)(3)
PREC_BESSEL = 600                  # ### (R277)(3a): the Bessel factor's own rung
BESSEL_BAR_EXP = -60               # ### (3a): a term's radius at or above 2^-60 climbs
REL_BAR_EXP = -40                  # ### plan §2: a point value wider than a relative 2^-40 is re-taken at the rung
H = '1e-12'                        # ### the squares' half-width (plan §3)
H_WIDE = '1e-9'                    # ### the one widening (plan §11, squares)
SIG_L, SIG_R = '-0.5', '1.5'       # ### R's and B's σ-range
T0, T_TOP = '0.5', '150'           # ### R's floor and top
B_HALF = '0.5'                     # ### B = [−0.5, 1.5] × [−B_HALF, B_HALF]
SQ_SEG = 4                         # ### initial segments per side of a square
P_SEG = (8, 299, 8)                # ### initial segments on P: bottom, right, top
PB_SEG = (8, 8, 8)                 # ### initial segments on P_B
C1_SEG = (8, 40, 8)                # ### initial segments on C1's half path (ζ, to the midpoint of its third and fourth ordinates)
DEPTH_SQ, DEPTH_P = 16, 24         # ### bisection depths
C2_SHIFT = '1e-10'                 # ### C2: qE0 shifted in σ
V1_POINTS = (('0.8', '20'), ('0.3', '60'), ('1.2', '100'), ('0.5', '140'), ('-0.2', '149'))
LIST_SIZE_R = 146 + 2 * 17         # ### plan §1: 180 in R by orbit and pair
Q0_ON, Q0_OFF = 'b326_epstein_zeros.json', 'b326_offline.json'
PROCS = 10

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RUNGS = []                         # ### (m, σ, t, precision) for every Bessel factor taken at 600 bits, per process


def say(s=''):
    print(s, flush=True)


# ================================================================================ THE ROUTE
def _mu_abs(s):
    lo, hi = s.real.lower(), s.real.upper()
    h = arb(1) / 2
    return max(abs(lo - h).upper(), abs(hi - h).upper(), key=lambda a: a.upper())


def _tmax(s):
    return max(abs(float(s.imag.lower())), abs(float(s.imag.upper())))


def M_of(t, prec):
    return int(math.ceil((math.pi * abs(t) / 2 + (prec + 20) * math.log(2)) / (math.pi * math.sqrt(23)))) + 1


def _bessel(m, x, nu, nu_mid, pre_mid, dsum_mid, prec, s):
    """(3a): the factor K_nu(x) at the lowest of prec, 400, 600 at which the term's radius at the midpoint is below 2^-60; the ball value at
    that precision (nu a ball, or a point); every factor taken at 600 logged."""
    bar = arb(2) ** BESSEL_BAR_EXP
    ladder = [p for p in (PREC, PREC_RUNG, PREC_BESSEL) if p >= prec]
    used = ladder[-1]
    for p in ladder:
        ctx.prec = p
        km = acb(x).bessel_k(nu_mid)
        r = pre_mid * km.rad() * dsum_mid
        if r.is_finite() and r < bar:
            used = p
            break
    ctx.prec = used
    k = acb(x).bessel_k(nu) if nu.rad() > 0 else acb(x).bessel_k(nu_mid)
    if used == PREC_BESSEL:
        RUNGS.append((m, float(s.real.mid()), float(s.imag.mid()), used))
    ctx.prec = prec
    return k


def zq(s, prec=PREC):
    """Z_Q at s (a point or a ball), at the working precision prec, T4 in the radius."""
    ctx.prec = prec
    half = arb(1) / 2
    pi, sq = arb.pi(), arb(23).sqrt()
    s_mid = acb(s.mid())
    T1 = 2 * (2 * s).zeta()
    T2 = 2 * pi.sqrt() * (s - half).gamma() * s.rgamma() * acb(sq / 2) ** (1 - 2 * s) * (2 * s - 1).zeta()
    nu, nu_mid = s - half, s_mid - half
    pre = 8 * acb(pi) ** s * s.rgamma()
    pre_mid = abs(8 * acb(pi) ** s_mid * s_mid.rgamma())
    M = M_of(_tmax(s), prec)
    S = acb(0)
    for m in range(1, M + 1):
        divs = [k for k in range(1, m + 1) if m % k == 0]
        dsum = sum((acb(k) ** nu * acb(sq * (m // k) / 2) ** (-nu) for k in divs), acb(0))
        dsum_mid = abs(sum((acb(k) ** nu_mid * acb(sq * (m // k) / 2) ** (-nu_mid) for k in divs), acb(0)))
        K = _bessel(m, pi * sq * m, nu, nu_mid, pre_mid, dsum_mid, prec, s)
        ctx.prec = prec
        S += (dsum * K) if m % 2 == 0 else -(dsum * K)
    T3 = pre * S
    # ### T4 (plan 11.2 (j)): an upper bound, added as the radius
    a = _mu_abs(s)
    if not (a <= 1):
        raise ValueError('|σ − ½| above 1: T4`s bound does not apply')
    c = pi * sq
    C3 = 2 * (2 / sq).sqrt() * (1 / (2 * c)).exp() * (sq / 2) ** a
    t4 = 8 * abs(acb(pi) ** s * s.rgamma()).upper() * C3 * arb(M + 1) ** a * (-c * (M + 1)).exp() / (1 - 2 * (-c).exp())
    r = arb(t4.upper())
    return T1 + T2 + T3 + acb(arb(0, r), arb(0, r))


def zq_point(z):
    """a point value at 200 bits, re-taken at 400 when wider than a relative 2^-40; returns (value, precision)."""
    v = zq(z, PREC)
    if v.contains(0) or not (v.rad() < abs(v.mid()) * arb(2) ** REL_BAR_EXP):
        return zq(z, PREC_RUNG), PREC_RUNG
    return v, PREC


def zeta_f(s, prec=PREC):
    ctx.prec = prec
    return s.zeta()


def logg_q(s):
    return -s * (2 * arb.pi() / arb(23).sqrt()).log() + s.lgamma()


def logg_z(s):
    return -(s / 2) * arb.pi().log() + (s / 2).lgamma()


def lam_q(s):
    ctx.prec = PREC
    return (logg_q(s)).exp() * zq(s, PREC)


# ================================================================================ THE COUNT: SEGMENT ENCLOSURES (plan §5)
def _ball(za, zb):
    mid = (za + zb) / 2
    d = zb - za
    rr, ri = abs(d.real).upper() / 2, abs(d.imag).upper() / 2
    return mid + acb(arb(0, rr), arb(0, ri))


def _accepted(e):
    return e.is_finite() and not e.contains(0) and e.rad() <= abs(e.mid()) / 2


def _pt(F, z, cache):
    k = (z.real.mid().str(40), z.imag.mid().str(40))
    if k not in cache:
        if F is zq:
            cache[k] = zq_point(z)[0]
        else:
            v = F(z, PREC)
            if v.contains(0) or not (v.rad() < abs(v.mid()) * arb(2) ** REL_BAR_EXP):
                v = F(z, PREC_RUNG)
            cache[k] = v
        ctx.prec = PREC
    return cache[k]


def segment(F, za, zb, depth, maxd, cache, st):
    """the argument change of F along [za, zb] as an arb, or None (UNRESOLVED, its location in st['unresolved'])."""
    ctx.prec = PREC
    e = F(_ball(za, zb), PREC)
    ctx.prec = PREC
    if not _accepted(e):
        if depth < maxd:
            zm = (za + zb) / 2
            a = segment(F, za, zm, depth + 1, maxd, cache, st)
            if a is None:
                return None
            b = segment(F, zm, zb, depth + 1, maxd, cache, st)
            return None if b is None else a + b
        e = F(_ball(za, zb), PREC_RUNG)
        ctx.prec = PREC
        st['rung_segments'] += 1
        if not _accepted(e):
            st['unresolved'].append('[%s, %s]' % (za.mid().str(12, radius=False), zb.mid().str(12, radius=False)))
            return None
    st['segments'] += 1
    st['max_depth'] = max(st['max_depth'], depth)
    fa, fb = _pt(F, za, cache), _pt(F, zb, cache)
    ctx.prec = PREC
    d = (fb / fa).arg()
    return d


def path_arg(F, corners, nseg, maxd, st):
    """the argument change of F along the polygon through the corners, each edge split into nseg[i] segments first."""
    cache, tot = {}, arb(0)
    for i in range(len(corners) - 1):
        a, b = corners[i], corners[i + 1]
        for j in range(nseg[i]):
            za = a + (b - a) * arb(j) / nseg[i]
            zb = a + (b - a) * arb(j + 1) / nseg[i]
            d = segment(F, za, zb, 0, maxd, cache, st)
            if d is None:
                return None
            tot += d
    return tot


def _stats():
    return dict(segments=0, rung_segments=0, max_depth=0, unresolved=[])


def square_count(F, re, im, h):
    """the count of zeros of F in the square [re ± h] × [im ± h] (re, im, h arbs): (count or None, the count ball, stats)."""
    ctx.prec = PREC
    c = acb(re, im)
    hh = arb(h)
    corners = [c + acb(-hh, -hh), c + acb(hh, -hh), c + acb(hh, hh), c + acb(-hh, hh), c + acb(-hh, -hh)]
    st = _stats()
    a = path_arg(F, corners, [SQ_SEG] * 4, DEPTH_SQ, st)
    if a is None:
        return None, None, st
    cb = a / (2 * arb.pi())
    n = cb.unique_fmpz()
    return (int(n) if n is not None and cb.rad() < 0.5 else None), cb, st


def half_path_count(F, logg, corners, nseg, poles=0):
    """(1/π)(Δ arg F + Δ Im log γ) along the half path + poles: (count or None, the ball, stats)."""
    ctx.prec = PREC
    st = _stats()
    a = path_arg(F, corners, nseg, DEPTH_P, st)
    if a is None:
        return None, None, st
    ctx.prec = PREC
    dl = (logg(corners[-1]) - logg(corners[0])).imag
    cb = (a + dl) / arb.pi() + poles
    n = cb.unique_fmpz()
    return (int(n) if n is not None and cb.rad() < 0.5 else None), cb, st


# ================================================================================ THE LIST (b326's banks, read only)
def q0_list():
    on = json.load(io.open(os.path.join(D, Q0_ON), encoding='utf-8'))['zeros']
    off = json.load(io.open(os.path.join(D, Q0_OFF), encoding='utf-8'))['zeros']
    if not all(z['agree'] and z['gamma_a'] == z['gamma_b'] for z in on) or not all(z['agree'] and z['rho_a'] == z['rho_b'] for z in off):
        sys.exit('### A BANKED ZERO WHOSE TWO ROUTES DISAGREE -- NOTHING COUNTED')
    tail15 = json.load(io.open(os.path.join(D, Q0_OFF), encoding='utf-8'))['tail_at_1p5']
    return [z['gamma_a'] for z in on], [tuple(z['rho_a']) for z in off], tail15


# ================================================================================ ONE SQUARE (a pool task)
def task_square(args):
    kind, idx, re_s, im_s = args
    ctx.prec = PREC
    del RUNGS[:]
    t0 = time.time()
    re, im = arb(re_s), arb(im_s)
    n, cb, st = square_count(zq, re, im, H)
    widened = False
    if n == 0:
        n, cb, st = square_count(zq, re, im, H_WIDE)
        widened = True
    hb = H_WIDE if widened else H
    ball = acb(arb(re_s, hb), arb(im_s, hb))
    return dict(kind=kind, idx=idx, re=re_s, im=im_s, h=hb, widened=widened, count=n,
                count_ball=cb.str(10, radius=True) if cb is not None else None, segments=st['segments'], max_depth=st['max_depth'],
                rung_segments=st['rung_segments'], unresolved=st['unresolved'], ball=ball.str(25, radius=True),
                rungs=list(RUNGS), seconds=round(time.time() - t0, 1))


def task_path(args):
    """a run of the half path's right edge, for the pool: the argument change of Z_Q along [za, zb] split into n segments."""
    za_s, zb_s, n = args
    ctx.prec = PREC
    del RUNGS[:]
    za, zb = acb(arb(za_s[0]), arb(za_s[1])), acb(arb(zb_s[0]), arb(zb_s[1]))
    st = _stats()
    a = path_arg(zq, [za, zb], [n], DEPTH_P, st)
    return dict(za=za_s, zb=zb_s, arg=(a.str(30, radius=True) if a is not None else None), segments=st['segments'], max_depth=st['max_depth'],
                rung_segments=st['rung_segments'], unresolved=st['unresolved'], rungs=list(RUNGS))


def _init():
    ctx.prec = PREC


# ================================================================================ MAIN
def main():
    T_START = time.time()
    ctx.prec = PREC
    OUT, ROWS = [], []
    log = lambda s='': (OUT.append(s), say(s))   # noqa: E731
    on, off, tail15 = q0_list()
    log('b667 -- Q0`S ZEROS BELOW 150 IN BALLS: THE COUNTS (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    log('')
    log('### the plan relay data/b667_epstein_plan.txt at 4c972bb1 (the author`s word); python-flint 0.9.0; %d bits, rung %d, Bessel rung %d at '
        '2^%d; h %s, widening %s; R = [%s, %s] × [%s, %s], B = [%s, %s] × [−%s, %s]; depths %d / %d. Rows are rectangles and regions.' % (
            PREC, PREC_RUNG, PREC_BESSEL, BESSEL_BAR_EXP, H, H_WIDE, SIG_L, SIG_R, T0, T_TOP, SIG_L, SIG_R, B_HALF, B_HALF, DEPTH_SQ, DEPTH_P))
    log('### the list: relay data/b326_epstein_zeros.json "zeros" %d ordinates ; relay data/b326_offline.json "zeros" %d off-line zeros ; '
        'R`s list size by orbit and pair %d' % (len(on), len(off), LIST_SIZE_R))
    all_rungs = []

    # ### V1: the functional equation, each side a ball
    log('')
    log('== V1  THE FUNCTIONAL EQUATION Λ_Q(s) = Λ_Q(1 − s), each side`s ball')
    v1_ok = True
    for sg, tt in V1_POINTS:
        del RUNGS[:]
        s = acb(arb(sg), arb(tt))
        a, b = lam_q(s), lam_q(1 - s)
        ov = a.overlaps(b)
        v1_ok = v1_ok and ov
        all_rungs += RUNGS
        log('  s = %s + %si : Λ_Q(s) %s ; Λ_Q(1 − s) %s ; OVERLAP %s' % (sg, tt, a.str(12, radius=True), b.str(12, radius=True), ov))
    log('  V1 %s' % ('HOLDS (5 of 5 overlap)' if v1_ok else '### FAILS'))

    # ### V2: Z_Q(1.5) − 2 in [the bank's truncated 1.38, 2)
    del RUNGS[:]
    z15 = zq(acb(arb(SIG_R)), PREC)
    w = z15.real - 2
    v2_ok = bool(z15.imag.contains(0) and w > arb(tail15) and w < 2)
    all_rungs += RUNGS
    log('')
    log('== V2  Z_Q(1.5) = %s ; Z_Q(1.5) − 2 = %s ; above b326`s truncated %r : %s ; below 2 : %s -> V2 %s' % (
        z15.str(15, radius=True), w.str(15, radius=True), tail15, w > arb(tail15), w < 2, 'HOLDS' if v2_ok else '### FAILS'))
    log('      so for σ ≥ 1.5, |Z_Q(s) − 2| ≤ Z_Q(1.5) − 2 < 2 and Z_Q has no zero there; σ ≤ −0.5 by the functional equation')

    # ### V3: the route sees qE0
    del RUNGS[:]
    s0, t0q = off[0]
    vb = zq(acb(arb(repr(s0), H), arb(repr(t0q), H)), PREC)
    vl = zq_point(acb(arb(1) / 2, arb(repr(t0q))))[0]
    v3_ok = vb.contains(0) and not vl.contains(0)
    all_rungs += RUNGS
    log('')
    log('== V3  Z_Q on the h-ball about qE0 = %r + %r i : %s, CONTAINS 0 %s ; at ½ + %r i : %s, CONTAINS 0 %s -> V3 %s' % (
        s0, t0q, vb.str(10, radius=True), vb.contains(0), t0q, vl.str(10, radius=True), vl.contains(0), 'HOLDS' if v3_ok else '### FAILS'))

    # ### C1: ζ
    log('')
    log('== C1  THE SAME ENGINE POINTED AT ζ (acb.zeta; log γ_ζ(s) = −(s/2) log π + lgamma(s/2))')
    c1_ok = True
    zz = [acb.zeta_zero(n) for n in (1, 2, 3, 4)]
    for n in (1, 2, 3):
        z = zz[n - 1]
        k, cb, st = square_count(zeta_f, z.real.mid(), z.imag.mid(), H)
        c1_ok = c1_ok and k == 1
        log('  square about acb.zeta_zero(%d) = %s : count %s (ball %s ; segments %d, depth %d, unresolved %s)' % (
            n, z.str(20, radius=False), k, cb.str(8, radius=True) if cb is not None else '### UNRESOLVED', st['segments'], st['max_depth'],
            st['unresolved'] or 'NONE'))
    tc = ((zz[2].imag + zz[3].imag) / 2).mid()
    corners = [acb(arb(1) / 2, arb(T0)), acb(arb(SIG_R), arb(T0)), acb(arb(SIG_R), tc), acb(arb(1) / 2, tc)]
    kz, cbz, stz = half_path_count(zeta_f, logg_z, corners, list(C1_SEG))
    c1_ok = c1_ok and kz == 3
    log('  region [%s, %s] × [%s, %s] by the half path: count %s (ball %s ; segments %d, depth %d, unresolved %s)' % (
        SIG_L, SIG_R, T0, tc.str(12, radius=False), kz, cbz.str(8, radius=True) if cbz is not None else '### UNRESOLVED', stz['segments'],
        stz['max_depth'], stz['unresolved'] or 'NONE'))
    log('  C1 %s' % ('READS AS FIXED (1, 1, 1 and 3)' if c1_ok else '### DOES NOT READ AS FIXED'))

    # ### C2: qE0 shifted
    del RUNGS[:]
    sh = arb(repr(s0)) + arb(C2_SHIFT)
    k2, cb2, st2 = square_count(zq, sh, arb(repr(t0q)), H)
    c2_ok = cb2 is not None and not cb2.contains(1)
    all_rungs += RUNGS
    log('')
    log('== C2  qE0 shifted by %s in σ, the square h = %s about the shifted point: count %s, ball %s ; CONTAINS 1 %s -> C2 %s' % (
        C2_SHIFT, H, k2, cb2.str(8, radius=True) if cb2 is not None else '### UNRESOLVED', cb2.contains(1) if cb2 is not None else None,
        'READS AS FIXED' if c2_ok else '### DOES NOT READ AS FIXED'))

    # ### R: the half path, its right edge in parallel runs
    log('')
    log('== R   THE REGION [%s, %s] × [%s, %s] BY THE HALF PATH ½ + i%s -> %s + i%s -> %s + i%s -> ½ + i%s' % (
        SIG_L, SIG_R, T0, T_TOP, T0, SIG_R, T0, SIG_R, T_TOP, T_TOP))
    half = arb(1) / 2
    pts = [(str(SIG_R), repr(0.5 + 0.5 * j)) for j in range(P_SEG[1] + 1)]
    jobs = [(('0.5', T0), (SIG_R, T0), P_SEG[0])] + [(pts[j], pts[j + 1], 1) for j in range(P_SEG[1])] + [((SIG_R, T_TOP), ('0.5', T_TOP), P_SEG[2])]
    with mpr.Pool(PROCS, initializer=_init) as pool:
        res = pool.map(task_path, jobs)
    ctx.prec = PREC
    unres = sum((r['unresolved'] for r in res), [])
    for r in res:
        all_rungs += r['rungs']
    if unres or any(r['arg'] is None for r in res):
        nR, cbR = None, None
    else:
        a = sum((arb(r['arg']) for r in res), arb(0))
        dl = (logg_q(acb(half, arb(T_TOP))) - logg_q(acb(half, arb(T0)))).imag
        cbR = (a + dl) / arb.pi()
        u = cbR.unique_fmpz()
        nR = int(u) if u is not None and cbR.rad() < 0.5 else None
    log('  segments %d ; deepest %d ; at the rung %d ; unresolved %s' % (sum(r['segments'] for r in res), max(r['max_depth'] for r in res),
                                                                        sum(r['rung_segments'] for r in res), unres or 'NONE'))
    log('  N(R) = %s (ball %s) ; the list in R %d' % (nR, cbR.str(10, radius=True) if cbR is not None else '### UNRESOLVED', LIST_SIZE_R))

    # ### C3: one on-line point removed
    c3 = (nR - (LIST_SIZE_R - 1)) if nR is not None else None
    c3_ok = c3 == 1
    log('')
    log('== C3  the list less on-line index 0 (%d points in R) against N(R) = %s : UNLISTED %s -> C3 %s' % (
        LIST_SIZE_R - 1, nR, c3, 'READS AS FIXED' if c3_ok else '### DOES NOT READ AS FIXED'))

    # ### B: the band
    del RUNGS[:]
    cB = [acb(half, -arb(B_HALF)), acb(arb(SIG_R), -arb(B_HALF)), acb(arb(SIG_R), arb(B_HALF)), acb(half, arb(B_HALF))]
    nB, cbB, stB = half_path_count(zq, logg_q, cB, list(PB_SEG), poles=2)
    all_rungs += RUNGS
    log('')
    log('== B   THE BAND [%s, %s] × [−%s, %s] BY ITS HALF PATH, zeros = (1/π)Δ + 2 (Λ_Q`s poles at 0 and 1): %s (ball %s ; segments %d, '
        'depth %d, unresolved %s) ; the list in B 0' % (SIG_L, SIG_R, B_HALF, B_HALF, nB, cbB.str(10, radius=True) if cbB is not None else
                                                      '### UNRESOLVED', stB['segments'], stB['max_depth'], stB['unresolved'] or 'NONE'))

    # ### the Q0 squares
    jobs = [('ON', i, '0.5', repr(g)) for i, g in enumerate(on)] + [('OFF', i, repr(s), repr(t)) for i, (s, t) in enumerate(off)]
    jobs += [('PARTNER', i, (arb(1) - arb(repr(s))).mid().str(30, radius=False), repr(t)) for i, (s, t) in enumerate(off)]
    log('')
    log('== THE SQUARES: %d on-line, %d off-line, %d partners 1 − conj ρ ; h %s, one widening to %s' % (len(on), len(off), len(off), H, H_WIDE))
    with mpr.Pool(PROCS, initializer=_init) as pool:
        sq = pool.map(task_square, jobs)
    ctx.prec = PREC
    for r in sq:
        all_rungs += r['rungs']
        ROWS.append(r)
        log('  %-7s %3d  centre %s + %s i : count %s%s ; ball %s ; segments %d, depth %d, rung %d%s ; %.1f s' % (
            r['kind'], r['idx'], r['re'], r['im'], r['count'], ' WIDENED' if r['widened'] else '', r['ball'], r['segments'], r['max_depth'],
            r['rung_segments'], (' ; UNRESOLVED ' + ', '.join(r['unresolved'])) if r['unresolved'] else '', r['seconds']))
    ctx.prec = PREC
    cen = [acb(arb(r['re']), arb(r['im'])) for r in sq]
    sep = min((abs(cen[i] - cen[j]).lower() for i in range(len(cen)) for j in range(i + 1, len(cen))), key=lambda a: float(a))

    def line_of(kind):
        rs = [r for r in sq if r['kind'] == kind]
        return (len(rs), sum(1 for r in rs if r['count'] == 1 and not r['widened']), sum(1 for r in rs if r['count'] == 1 and r['widened']),
                [r['idx'] for r in rs if r['count'] != 1])
    h1, h2, hp = line_of('OFF'), line_of('ON'), line_of('PARTNER')
    log('  the minimum separation of the squares` centres %s (2h = %s)' % (sep.str(6, radius=False), 2 * float(H)))

    # ### H1-H3, V, C
    log('')
    log('== THE HYPOTHESES AND CHECKS, BY PRINTED LINE')
    H1 = h1[1] + h1[2] == h1[0] == 17
    H2 = h2[1] + h2[2] == h2[0] == 146
    H3 = nR == LIST_SIZE_R and nB == 0
    log('  (H1) off-line squares %d ; count 1 at h %d ; count 1 WIDENED %d ; not 1 %s ; each ball centred at its banked value -> %s' % (
        h1[0], h1[1], h1[2], h1[3] or 'NONE', 'HELD' if H1 else 'REFUTED'))
    log('  (H2) on-line squares %d (straddling σ = ½) ; count 1 at h %d ; count 1 WIDENED %d ; not 1 %s -> %s' % (
        h2[0], h2[1], h2[2], h2[3] or 'NONE', 'HELD' if H2 else 'REFUTED'))
    log('  (FE) partner squares %d ; count 1 at h %d ; WIDENED %d ; not 1 %s' % (hp[0], hp[1], hp[2], hp[3] or 'NONE'))
    log('  (H3) N(R) = %s against %d ; zeros in B = %s against 0%s -> %s' % (
        nR, LIST_SIZE_R, nB, (' ; UNLISTED %d' % (nR - LIST_SIZE_R)) if (nR is not None and nR > LIST_SIZE_R) else '', 'HELD' if H3 else 'REFUTED'))
    log('  (H5) V1 %s ; V2 %s ; V3 %s ; C1 %s ; C2 %s ; C3 %s -> %s' % (v1_ok, v2_ok, v3_ok, c1_ok, c2_ok, c3_ok,
                                                                      'HELD' if all((v1_ok, v2_ok, v3_ok, c1_ok, c2_ok, c3_ok)) else 'REFUTED'))
    log('  Bessel factors taken at %d bits: %d (relay data/b667_bessel_rungs.txt)' % (PREC_BESSEL, len(all_rungs)))
    log('')
    log('### ### **H1 %s ; H2 %s ; H3 %s ; H5 %s ; %.0f s.**' % ('HELD' if H1 else 'REFUTED', 'HELD' if H2 else 'REFUTED', 'HELD' if H3 else 'REFUTED',
                                                            'HELD' if all((v1_ok, v2_ok, v3_ok, c1_ok, c2_ok, c3_ok)) else 'REFUTED',
                                                            time.time() - T_START))

    def put(name, text):
        p = os.path.join(D, name)
        open(p + '.tmp', 'wb').write(text.encode('utf-8'))
        os.replace(p + '.tmp', p)
    put('b667_epstein_counts.txt', NL.join(OUT) + NL)
    Z = ['b667 -- Q0`S ZEROS BELOW 150, CERTIFIED IN BALLS (%s): rows are zeros with balls -- kind (ON, OFF, PARTNER), the bank index, the '
         'centre (the banked double), the ball (the square), the count, WIDENED where so; relay data/b667_epstein_counts.txt the counts.'
         % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '']
    for r in ROWS:
        Z.append('  %-7s %3d | %s + %s i | %s | count %s%s' % (r['kind'], r['idx'], r['re'], r['im'], r['ball'], r['count'],
                                                             ' WIDENED (h %s)' % r['h'] if r['widened'] else ''))
    put('b667_epstein_zeros_certified.txt', NL.join(Z) + NL)
    put('b667_epstein_zeros_certified.json', json.dumps(dict(h=H, h_wide=H_WIDE, prec=PREC, rows=ROWS, N_R=nR, N_B=nB,
                                                             N_R_ball=cbR.str(20, radius=True) if cbR is not None else None,
                                                             H1=H1, H2=H2, H3=H3), indent=1, ensure_ascii=False) + NL)
    put('b667_bessel_rungs.txt', NL.join(['b667 -- EVERY BESSEL FACTOR TAKEN AT %d BITS ((R277)(3a)): rows are factors -- m, the evaluation`s '
                                          'point (σ, t) at its midpoint, the precision.' % PREC_BESSEL, ''] +
                                         ['  m %2d | σ %.15g | t %.15g | %d bits' % x for x in all_rungs] +
                                         ['', '### ### **FACTORS AT %d BITS: %d.**' % (PREC_BESSEL, len(all_rungs))]) + NL)
    say('CERTIFY DONE')


if __name__ == '__main__':
    main()
