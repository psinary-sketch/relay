# -*- coding: utf-8 -*-
"""b667_epstein_certify.py -- Q0'S ZEROS BELOW HEIGHT 150 ISOLATED IN ARB BALLS BY AN ARGUMENT-PRINCIPLE COUNT, THE LIST'S COMPLETENESS
COUNTED BY THE SAME FORM, under (R277)(3)-(5) with (3a), (3b) and (3c) in force, on the author's word on the plan (relay
data/b667_epstein_plan.txt sections 13-15, relay data/b667_author_answers.txt).

### THE ROUTE (plan sections 2, 11, 14, 15): Z_Q(s) = T1 + T2 + T3 + T4 (Chowla-Selberg, Q0 = x² + xy + 6y²):
###   T1 = 2 ζ(2s); T2 = 2 √π Γ(s − ½) Γ(s)⁻¹ (√23/2)^{1−2s} ζ(2s − 1);
###   T3 = 8 π^s Γ(s)⁻¹ Σ_{m ≤ M} (−1)^m K_{s−½}(π√23 m) Σ_{k|m} k^{s−½} β_{m/k}^{½−s}, β_n = √23 n/2 (the sign (−1)^{kn} = (−1)^m, 11.1);
###   T4 the truncation, |T4| ≤ 8 |π^s Γ(s)⁻¹| C3(μ) (M+1)^{|μ|} e^{−c(M+1)} / (1 − 2^{|μ|} e^{−c}), c = π√23,
###   C3(μ) = 2 √(2/√23) e^{μ²/(2c)} (√23/2)^{|μ|}, μ = σ − ½, |μ| ≤ 2 (plan section 16, (R277)(3d)), added to the ball as its radius.
###   M = ⌈(π|t|/2 + (prec + 20) ln 2)/(π√23)⌉ + 1.
### (3b) EVERY BESSEL FACTOR is K_{ν_mid}(x) at the ball's centre, x = π√23 m formed at the call's own precision, plus |ν − ν_mid| times the
###   shifted-contour bound sup|∂_ν K| ≤ 2 e^{−|t||θ|} (|θ| K_{|μ|}(a) + e^{−1} K_{|μ|+1}(a)), a = x cos θ (plan 14(a)-(d)); Arb never
###   propagates a radius in ν or in x. Checked before any count against direct 800-bit evaluations at three grid points.
### (3a) THE PRECISION: 200 bits; the 400 rung for a point value wider than a relative 2^-40 and for a segment unresolved at the depth limit;
###   the Bessel factor alone climbs 200 -> 400 -> 600 bits while its term's radius at the centre is at or above 2^-60; every factor taken at
###   600 logged with its m, its point (σ, t) and its precision (relay data/b667_bessel_rungs.txt).
### THE COUNT (plan section 5): segment enclosures -- accepted when the enclosure excludes 0 with radius at most half its midpoint's modulus;
###   the argument change then the principal arg(F(z_b)/F(z_a)); otherwise bisected to depth 16 (squares) or 24 (paths), then the 400 rung
###   once, then UNRESOLVED printed and not refined further.
### (3c) R'S RIGHT EDGE σ = 3/2 (and C1's, σ = 2): the uniform tail bound printed below the leading coefficient (Z_Q(3/2) − 2 < 2;
###   ζ(2) − 1 < 1), so the function stays in the open right half-plane along the edge and the edge's argument change is the difference of
###   the principal arguments of its two end values.
### THE SQUARES: half-width h = 1e-12 about each banked double, the ball the square; one widening to 1e-9 printed WIDENED.
### THE REGIONS: R = [−0.5, 1.5] × [0.5, 150] and B = [−0.5, 1.5] × [−0.5, 0.5], each by its half path under Λ_Q(1 − conj s) = conj Λ_Q(s);
###   N(R) = (1/π) Δ_P arg Λ_Q ; zeros in B = (1/π) Δ_{P_B} arg Λ_Q + 2 (Λ_Q's poles at 0 and 1).
### THE ORDER: (3b)'s check; (3d)'s check; V1, V2, V3; C1; C2; R, then C3 on it; B; the Q0 squares; H1-H3 read.
### b326's banks are read and never written. No lean; no kernel file read. Nothing here is about ζ but C1.
### Usage: `python -X utf8 tools/b667_epstein_certify.py` -> data/b667_epstein_counts.txt, data/b667_epstein_zeros_certified.txt (.json),
### data/b667_bessel_rungs.txt. Written by the Write tool at b667 (rewritten whole under (3b)-(3c) before any run), read back whole before
### it runs.
"""
import io
import json
import math
import multiprocessing as mpr
import os
import subprocess
import sys
import time

from flint import arb, acb, ctx

# ================================================================================ THE PLAN'S CONSTANTS (relay data/b667_epstein_plan.txt §13-§15)
PREC = 200                         # ### Arb balls at 200 bits (relay data/b627_margin_inputs.txt :7)
PREC_RUNG = 400                    # ### the one rung of (R277)(3)
PREC_BESSEL = 600                  # ### (R277)(3a): the Bessel factor's own rung
PREC_CHECK = 800                   # ### (R277)(3b): the direct evaluation the remedy is checked against
BESSEL_BAR_EXP = -60               # ### (3a): a term's radius at or above 2^-60 climbs
REL_BAR_EXP = -40                  # ### plan §2: a point value wider than a relative 2^-40 is re-taken at the rung
CHECK_POINTS = (('0.5', '40.0'), ('0.5', '100.0'), ('0.5', '147.5'))    # ### (3b): three grid points of data/b667_bessel_obstruction.txt
#                                                                           ### on σ = ½ (plan §15, dated; defect (e))
CHECK_R = '1e-6'                   # ### (3b): the ball's radius at each
T4_CHECK_POINTS = (('1.5', '40.0'), ('1.5', '100.0'), ('-0.5', '147.5'))   # ### (3d): grid points on the σ-edges, the ball's |μ| in (1, 2]
H = '1e-12'                        # ### the squares' half-width (plan §3)
H_WIDE = '1e-9'                    # ### the one widening (plan §11, squares)
SIG_L, SIG_R = '-0.5', '1.5'       # ### R's and B's σ-range
T0, T_TOP = '0.5', '150'           # ### R's floor and top
B_HALF = '0.5'                     # ### B = [−0.5, 1.5] × [−B_HALF, B_HALF]
C1_SIG_R = '2'                     # ### (3c), reading (iii): C1's right edge, where ζ(σ) − 1 < 1
SQ_SEG = 4                         # ### initial segments per side of a square
P_SEG = (8, 8)                     # ### initial segments on P's bottom and top edges (its right edge by (3c))
PB_SEG = (8, 8, 8)                 # ### initial segments on P_B (all three edges by segments)
C1_SEG = (8, 8)                    # ### initial segments on C1's bottom and top edges (its right edge by (3c))
DEPTH_SQ, DEPTH_P = 16, 24         # ### bisection depths
C2_SHIFT = '1e-10'                 # ### C2: qE0 shifted in σ
V1_POINTS = (('0.8', '20'), ('0.3', '60'), ('1.2', '100'), ('0.5', '140'), ('-0.2', '149'))
LIST_SIZE_R = 146 + 2 * 17         # ### plan §1: 180 in R by orbit and pair
Q0_ON, Q0_OFF = 'b326_epstein_zeros.json', 'b326_offline.json'
PROCS = 8                          # ### plan §15: reduced from ten before the run (the 2560 MB hold)
HOLD_MB, PROC_MB = 2560, 25        # ### the hold; one process measured at 24.4 MB (plan §15)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RUNGS = []                         # ### (m, σ, t, precision) for every Bessel factor taken at 600 bits, per process


def say(s=''):
    print(s, flush=True)


def free_mb():
    r = subprocess.run(['powershell', '-NoProfile', '-Command', '[math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1024)'],
                       capture_output=True, text=True)
    try:
        return int(r.stdout.strip())
    except ValueError:
        return None


# ================================================================================ THE ROUTE
def _mu_abs(s):
    lo, hi = s.real.lower(), s.real.upper()
    h = arb(1) / 2
    return max(abs(lo - h).upper(), abs(hi - h).upper(), key=lambda a: a.upper())


def _tmax(s):
    return max(abs(float(s.imag.lower())), abs(float(s.imag.upper())))


def M_of(t, prec):
    return int(math.ceil((math.pi * abs(t) / 2 + (prec + 20) * math.log(2)) / (math.pi * math.sqrt(23)))) + 1


def dK_bound(x, nu):
    """(3b), plan 14(d): sup over the ball nu of |∂_ν K_ν(x)| ≤ 2 e^{−|t||θ|}(|θ| K_{|μ|}(a) + e^{−1} K_{|μ|+1}(a)), a = x cos θ, |t| the ball's
    least |Im ν|, |μ| its largest |Re ν|, θ = π/2 − 1/max(|t|, 1) (θ = 0 where the ball meets Im ν = 0)."""
    t_lo = min(abs(float(nu.imag.lower())), abs(float(nu.imag.upper())))
    mu = max(abs(nu.real.lower()).upper(), abs(nu.real.upper()).upper(), key=lambda a: a.upper())
    th = arb(0) if nu.imag.contains(0) else arb.pi() / 2 - 1 / arb(max(t_lo, 1.0))
    a = x * th.cos()
    k0 = acb(a).bessel_k(acb(mu)).real
    k1 = acb(a).bessel_k(acb(mu + 1)).real
    return 2 * (-arb(t_lo) * th).exp() * (th * k0 + (-arb(1)).exp() * k1)


def _bessel(m, nu, nu_mid, rad_nu, pre_mid, dsum_mid, prec, s):
    """(3a)-(3b): the factor K_ν(π√23 m) on the ball nu: K at the centre nu_mid at the lowest precision of the ladder at which the term's
    radius there is below 2^-60 (x formed at that precision), plus rad_nu · sup|∂_ν K|; every factor taken at 600 logged."""
    bar = arb(2) ** BESSEL_BAR_EXP
    ladder = sorted({prec} | {p for p in (PREC, PREC_RUNG, PREC_BESSEL) if p >= prec})
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
        e = (rad_nu * dK_bound(x, nu)).upper()
        km = km + acb(arb(0, e), arb(0, e))
    if used == PREC_BESSEL and prec < PREC_BESSEL:
        RUNGS.append((m, float(s.real.mid()), float(s.imag.mid()), used))
    ctx.prec = prec
    return km


def t4_bound(s, M):
    """T4 (plan 16 (d')-(j'), (R277)(3d)): |T4| ≤ 8 |π^s Γ(s)⁻¹| C3(μ) (M + 1)^{|μ|} e^{−c(M+1)} / (1 − 2^{|μ|} e^{−c}), C3(μ) = 2 √(2/√23)
    e^{μ²/(2c)} (√23/2)^{|μ|}, |μ| the ball's largest |σ − ½|, required ≤ 2; an arb upper bound."""
    pi, sq = arb.pi(), arb(23).sqrt()
    a = _mu_abs(s)
    if not (a <= 2):
        raise ValueError('|σ − ½| above 2: T4`s bound does not apply')
    c = pi * sq
    C3 = 2 * (2 / sq).sqrt() * (a * a / (2 * c)).exp() * (sq / 2) ** a
    t4 = 8 * abs(acb(pi) ** s * s.rgamma()).upper() * C3 * arb(M + 1) ** a * (-c * (M + 1)).exp() / (1 - arb(2) ** a * (-c).exp())
    return arb(t4.upper())


def zq(s, prec=PREC, M_force=None, with_t4=True):
    """Z_Q at s (a point or a ball), at the working precision prec, T4 in the radius. M_force and with_t4 serve (3d)'s check alone (the
    sum to a given length, without its tail bound); the route runs with their defaults."""
    ctx.prec = prec
    half = arb(1) / 2
    pi, sq = arb.pi(), arb(23).sqrt()
    s_mid = acb(s.mid())
    rad_nu = s.rad()
    T1 = 2 * (2 * s).zeta()
    T2 = 2 * pi.sqrt() * (s - half).gamma() * s.rgamma() * acb(sq / 2) ** (1 - 2 * s) * (2 * s - 1).zeta()
    nu, nu_mid = s - half, s_mid - half
    pre = 8 * acb(pi) ** s * s.rgamma()
    pre_mid = abs(8 * acb(pi) ** s_mid * s_mid.rgamma())
    M = M_force if M_force else M_of(_tmax(s), prec)
    S = acb(0)
    for m in range(1, M + 1):
        divs = [k for k in range(1, m + 1) if m % k == 0]
        dsum = sum((acb(k) ** nu * acb(sq * (m // k) / 2) ** (-nu) for k in divs), acb(0))
        dsum_mid = abs(sum((acb(k) ** nu_mid * acb(sq * (m // k) / 2) ** (-nu_mid) for k in divs), acb(0)))
        K = _bessel(m, nu, nu_mid, rad_nu, pre_mid, dsum_mid, prec, s)
        ctx.prec = prec
        S += (dsum * K) if m % 2 == 0 else -(dsum * K)
    T3 = pre * S
    if not with_t4:
        return T1 + T2 + T3
    # ### T4 (plan 16 (j'), (R277)(3d)): an upper bound, added as the radius
    r = t4_bound(s, M)
    return T1 + T2 + T3 + acb(arb(0, r), arb(0, r))


def tail_sum(s, prec, m_lo, m_hi):
    """(3d)'s instrument alone: T3's terms m = m_lo ... m_hi at the point s, summed directly at prec (the factor at the point, x formed at
    prec) -- the quantity T4 bounds, without the difference of two full sums."""
    ctx.prec = prec
    half = arb(1) / 2
    pi, sq = arb.pi(), arb(23).sqrt()
    nu = s - half
    S = acb(0)
    for m in range(m_lo, m_hi + 1):
        divs = [k for k in range(1, m + 1) if m % k == 0]
        dsum = sum((acb(k) ** nu * acb(sq * (m // k) / 2) ** (-nu) for k in divs), acb(0))
        K = acb(pi * sq * m).bessel_k(nu)
        S += (dsum * K) if m % 2 == 0 else -(dsum * K)
    return 8 * acb(pi) ** s * s.rgamma() * S


def zq_point(z):
    """a point value at 200 bits, re-taken at 400 when wider than a relative 2^-40."""
    v = zq(z, PREC)
    if v.contains(0) or not (v.rad() < abs(v.mid()) * arb(2) ** REL_BAR_EXP):
        return zq(z, PREC_RUNG)
    return v


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
            cache[k] = zq_point(z)
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
    return (fb / fa).arg()


def edge_arg(F, a, b, n, maxd, st, cache):
    """the argument change of F along the edge [a, b], split into n segments first."""
    tot = arb(0)
    for j in range(n):
        za = a + (b - a) * arb(j) / n
        zb = a + (b - a) * arb(j + 1) / n
        d = segment(F, za, zb, 0, maxd, cache, st)
        if d is None:
            return None
        tot += d
    return tot


def _stats():
    return dict(segments=0, rung_segments=0, max_depth=0, unresolved=[])


def square_count(F, re, im, h):
    """the count of zeros of F in the square [re ± h] × [im ± h]: (count or None, the count ball, stats)."""
    ctx.prec = PREC
    c = acb(re, im)
    hh = arb(h)
    cs = [c + acb(-hh, -hh), c + acb(hh, -hh), c + acb(hh, hh), c + acb(-hh, hh), c + acb(-hh, -hh)]
    st, cache, tot = _stats(), {}, arb(0)
    for i in range(4):
        d = edge_arg(F, cs[i], cs[i + 1], SQ_SEG, DEPTH_SQ, st, cache)
        if d is None:
            return None, None, st
        tot += d
    cb = tot / (2 * arb.pi())
    n = cb.unique_fmpz()
    return (int(n) if n is not None and cb.rad() < 0.5 else None), cb, st


def _count(cb):
    n = cb.unique_fmpz()
    return int(n) if n is not None and cb.rad() < 0.5 else None


def half_path_segments(F, logg, corners, nseg, poles=0):
    """(1/π)(Δ arg F + Δ Im log γ) + poles along the half path, every edge by segments: (count or None, the ball, stats)."""
    ctx.prec = PREC
    st, cache, tot = _stats(), {}, arb(0)
    for i in range(len(corners) - 1):
        d = edge_arg(F, corners[i], corners[i + 1], nseg[i], DEPTH_P, st, cache)
        if d is None:
            return None, None, st
        tot += d
    ctx.prec = PREC
    cb = (tot + (logg(corners[-1]) - logg(corners[0])).imag) / arb.pi() + poles
    return _count(cb), cb, st


def half_path_3c(F, logg, corners, nseg, lead, tail):
    """(3c): the half path A -> B -> C -> D with its right edge B -> C by the tail bound (|F − lead| ≤ tail < lead on the edge, so the edge's
    argument change is arg F(C) − arg F(B), principal values) and its other two edges by segments: (count or None, ball, stats, edge print)."""
    ctx.prec = PREC
    st, cache = _stats(), {}
    if not (tail < lead):
        return None, None, st, '### THE TAIL BOUND %s IS NOT BELOW %s -- THE EDGE NOT TAKEN' % (tail.str(10, radius=True), lead)
    A, B, C, Dd = corners
    d1 = edge_arg(F, A, B, nseg[0], DEPTH_P, st, cache)
    d3 = edge_arg(F, C, Dd, nseg[1], DEPTH_P, st, cache)
    fb, fc = _pt(F, B, cache), _pt(F, C, cache)
    ctx.prec = PREC
    ab, ac = fb.arg(), fc.arg()
    d2 = ac - ab
    pr = 'the right edge by (3c): tail %s < %s ; F(B) = %s (arg %s) ; F(C) = %s (arg %s) ; its argument change %s' % (
        tail.str(10, radius=True), lead, fb.str(10, radius=True), ab.str(10, radius=True), fc.str(10, radius=True), ac.str(10, radius=True),
        d2.str(10, radius=True))
    if d1 is None or d3 is None:
        return None, None, st, pr
    cb = (d1 + d2 + d3 + (logg(Dd) - logg(A)).imag) / arb.pi()
    return _count(cb), cb, st, pr


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
    try:
        n, cb, st = square_count(zq, re, im, H)
        widened = False
        if n == 0:
            n, cb, st = square_count(zq, re, im, H_WIDE)
            widened = True
    except Exception as ex:                       # ### one square's error is its own row, not the run's end
        return dict(kind=kind, idx=idx, re=re_s, im=im_s, h=H, widened=False, count=None, count_ball=None, segments=0, max_depth=0,
                    rung_segments=0, unresolved=['### ERROR %r' % ex], ball=None, rungs=list(RUNGS), seconds=round(time.time() - t0, 1))
    hb = H_WIDE if widened else H
    ball = acb(arb(re_s, hb), arb(im_s, hb))
    return dict(kind=kind, idx=idx, re=re_s, im=im_s, h=hb, widened=widened, count=n,
                count_ball=cb.str(10, radius=True) if cb is not None else None, segments=st['segments'], max_depth=st['max_depth'],
                rung_segments=st['rung_segments'], unresolved=st['unresolved'], ball=ball.str(25, radius=True),
                rungs=list(RUNGS), seconds=round(time.time() - t0, 1))


def _init():
    ctx.prec = PREC


# ================================================================================ MAIN
def main():
    T_START = time.time()
    ctx.prec = PREC
    OUT, ROWS = [], []
    log = lambda s='': (OUT.append(s), say(s))   # noqa: E731

    def put(name, text):
        p = os.path.join(D, name)
        open(p + '.tmp', 'wb').write(text.encode('utf-8'))
        os.replace(p + '.tmp', p)
    on, off, tail15 = q0_list()
    fm0 = free_mb()
    procs = PROCS
    while procs > 1 and fm0 is not None and fm0 - (procs + 1) * PROC_MB < HOLD_MB:
        procs -= 1
    lows = [fm0]
    log('b667 -- Q0`S ZEROS BELOW 150 IN BALLS: THE COUNTS (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    log('')
    log('### the plan relay data/b667_epstein_plan.txt sections 13-15 (the author`s word, (3a)-(3c)); python-flint 0.9.0; %d bits, rung %d, '
        'Bessel rung %d at 2^%d, the remedy`s check at %d; h %s, widening %s; R = [%s, %s] × [%s, %s], B = [%s, %s] × [−%s, %s]; depths '
        '%d / %d. Rows are rectangles and regions.' % (PREC, PREC_RUNG, PREC_BESSEL, BESSEL_BAR_EXP, PREC_CHECK, H, H_WIDE, SIG_L, SIG_R, T0,
                                                     T_TOP, SIG_L, SIG_R, B_HALF, B_HALF, DEPTH_SQ, DEPTH_P))
    log('### READINGS NAMED HERE ((R277)(3c), plan §15): (i) the departure from one form for every count is confined to R`s right edge '
        'σ = 3/2, taken by the tail bound from two point values, and C1`s right edge, which exercises it; (ii) R`s half path has no left '
        'edge -- σ = −½ is not traversed, the left half of R`s boundary being P`s reflection under s -> 1 − conj s; (iii) C1`s region is '
        '[−1, 2] × [0.5, T_c], its right edge σ = 2, since ζ(3/2) − 1 exceeds 1.')
    log('### the list: relay data/b326_epstein_zeros.json "zeros" %d ordinates ; relay data/b326_offline.json "zeros" %d off-line zeros ; '
        'R`s list size by orbit and pair %d' % (len(on), len(off), LIST_SIZE_R))
    log('### the processes: %d workers and the main process (plan §15: eight, reduced further only if the projection breaches the hold) ; '
        'free memory at the start %s MB ; projected low %s MB against the hold %d MB' % (
            procs, fm0, (fm0 - (procs + 1) * PROC_MB) if fm0 is not None else None, HOLD_MB))
    all_rungs = []

    # ### (3b): the remedy's check against direct 800-bit evaluations
    log('')
    log('== (3b) THE REMEDY`S CHECK: Z_Q on the ball of radius %s by the remedy at %d bits, against Z_Q at %d bits at its centre and at the '
        'offset point (σ + r/2, t + r/2)' % (CHECK_R, PREC, PREC_CHECK))
    ok3b = True
    for sg, tt in CHECK_POINTS:
        del RUNGS[:]
        ctx.prec = PREC
        zb = zq(acb(arb(sg, CHECK_R), arb(tt, CHECK_R)), PREC)
        all_rungs += RUNGS
        for label, (ps, pt) in (('centre', (arb(sg), arb(tt))), ('offset', (arb(sg) + arb(CHECK_R) / 2, arb(tt) + arb(CHECK_R) / 2))):
            ctx.prec = PREC_CHECK
            p = acb(arb(sg), arb(tt)) if label == 'centre' else acb(arb(sg) + arb(CHECK_R) / 2, arb(tt) + arb(CHECK_R) / 2)
            zd = zq(p, PREC_CHECK)
            ctx.prec = PREC
            ins = zb.contains(zd)
            ok3b = ok3b and ins
            log('  (σ, t) = (%s, %s) %s : the ball %s ; at %d bits %s ; INSIDE %s' % (sg, tt, label, zb.str(12, radius=True), PREC_CHECK,
                                                                                   zd.str(40, radius=True), ins))
    log('  (3b) %s' % ('HOLDS: every 800-bit value inside its ball' if ok3b else '### FAILS -- THE ACT STOPS HERE, THE COMPARISON BANKED'))
    if not ok3b:
        put('b667_epstein_counts.txt', NL.join(OUT) + NL)
        say('CERTIFY STOPPED AT (3b)')
        return

    # ### (3d): T4 restated for |μ| ≤ 2, its check against the sum taken to twice the length at 800 bits
    log('')
    log('== (3d) T4 RESTATED FOR |μ| ≤ 2 (plan section 16), ITS CHECK: Z_Q on the ball of radius %s by the route at %d bits (the sum to M, T4 in '
        'the radius) against the sum to 2M at %d bits at the ball`s centre; beside it the terms M + 1 ... 2M against T4`s bound' % (
            CHECK_R, PREC, PREC_CHECK))
    ok3d = True
    for sg, tt in T4_CHECK_POINTS:
        del RUNGS[:]
        ctx.prec = PREC
        bl = acb(arb(sg, CHECK_R), arb(tt, CHECK_R))
        zb = zq(bl, PREC)
        ctx.prec = PREC
        Mb = M_of(_tmax(bl), PREC)
        mu = _mu_abs(bl)
        tb = t4_bound(bl, Mb)
        all_rungs += RUNGS
        ctx.prec = PREC_CHECK
        p = acb(arb(sg), arb(tt))
        zl2 = zq(p, PREC_CHECK, M_force=2 * Mb, with_t4=False)
        tl = abs(tail_sum(p, PREC_CHECK, Mb + 1, 2 * Mb))
        ctx.prec = PREC
        ins = zb.contains(zl2)
        tstate = 'BELOW' if tl.upper() <= tb else ('ABOVE' if tl.lower() > tb else 'NOT DECIDED')
        ok3d = ok3d and ins and tstate != 'ABOVE'
        log('  (σ, t) = (%s, %s) : the ball`s largest |μ| %s ; M %d ; the ball %s ; the sum to 2M = %d at %d bits %s ; INSIDE %s ; the terms '
            'M + 1 ... 2M summed directly %s against T4`s bound %s : %s' % (
                sg, tt, mu.str(10, radius=False), Mb, zb.str(12, radius=True), 2 * Mb, PREC_CHECK, zl2.str(40, radius=True), ins,
                tl.str(5, radius=True), tb.str(5, radius=False), tstate))
    log('  (3d) %s' % ('HOLDS: every longer sum inside its ball (the ruled comparison); no tail above its bound' if ok3d else
                       '### FAILS -- THE ACT STOPS HERE, THE COMPARISON BANKED'))
    if not ok3d:
        put('b667_epstein_counts.txt', NL.join(OUT) + NL)
        say('CERTIFY STOPPED AT (3d)')
        return

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

    # ### V2: Z_Q(3/2) − 2, the uniform tail bound of (3c)
    del RUNGS[:]
    z15 = zq(acb(arb(SIG_R)), PREC)
    w = z15.real - 2
    v2_ok = bool(z15.imag.contains(0) and w > arb(tail15) and w < 2)
    all_rungs += RUNGS
    log('')
    log('== V2  Z_Q(3/2) = %s ; Σ_{n ≥ 2} r_Q(n) n^{−3/2} = Z_Q(3/2) − 2 = %s ; above b326`s truncated %r : %s ; below 2 : %s -> V2 %s' % (
        z15.str(15, radius=True), w.str(15, radius=True), tail15, w > arb(tail15), w < 2, 'HOLDS' if v2_ok else '### FAILS'))
    log('      a bound in σ alone: |Z_Q(s) − 2| ≤ Z_Q(3/2) − 2 < 2 for Re s ≥ 3/2, so no zero there and Z_Q in the open right half-plane on '
        'R`s right edge; σ ≤ −1/2 by the functional equation')

    # ### V3: the route sees qE0
    del RUNGS[:]
    s0, t0q = off[0]
    vb = zq(acb(arb(repr(s0), H), arb(repr(t0q), H)), PREC)
    vl = zq_point(acb(arb(1) / 2, arb(repr(t0q))))
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
    ctx.prec = PREC
    ztail = acb(arb(C1_SIG_R)).zeta().real - 1
    corners = [acb(arb(1) / 2, arb(T0)), acb(arb(C1_SIG_R), arb(T0)), acb(arb(C1_SIG_R), tc), acb(arb(1) / 2, tc)]
    kz, cbz, stz, prz = half_path_3c(zeta_f, logg_z, corners, list(C1_SEG), 1, ztail)
    c1_ok = c1_ok and kz == 3
    log('  region [−1, %s] × [%s, %s] by the half path: %s' % (C1_SIG_R, T0, tc.str(12, radius=False), prz))
    log('    count %s (ball %s ; segments %d, depth %d, unresolved %s)' % (
        kz, cbz.str(8, radius=True) if cbz is not None else '### UNRESOLVED', stz['segments'], stz['max_depth'], stz['unresolved'] or 'NONE'))
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

    # ### R: the half path, its right edge by (3c)
    del RUNGS[:]
    half = arb(1) / 2
    log('')
    log('== R   THE REGION [%s, %s] × [%s, %s] BY THE HALF PATH ½ + i%s -> %s + i%s -> %s + i%s -> ½ + i%s' % (
        SIG_L, SIG_R, T0, T_TOP, T0, SIG_R, T0, SIG_R, T_TOP, T_TOP))
    corners = [acb(half, arb(T0)), acb(arb(SIG_R), arb(T0)), acb(arb(SIG_R), arb(T_TOP)), acb(half, arb(T_TOP))]
    nR, cbR, stR, prR = half_path_3c(zq, logg_q, corners, list(P_SEG), 2, w)
    all_rungs += RUNGS
    lows.append(free_mb())
    log('  %s' % prR)
    log('  segments %d ; deepest %d ; at the rung %d ; unresolved %s' % (stR['segments'], stR['max_depth'], stR['rung_segments'],
                                                                        stR['unresolved'] or 'NONE'))
    log('  N(R) = %s (ball %s) ; the list in R %d' % (nR, cbR.str(10, radius=True) if cbR is not None else '### UNRESOLVED', LIST_SIZE_R))

    # ### C3: one on-line point removed
    c3 = (nR - (LIST_SIZE_R - 1)) if nR is not None else None
    c3_ok = c3 == 1
    log('')
    log('== C3  the list less on-line index 0 (%d points in R) against N(R) = %s : UNLISTED %s -> C3 %s' % (
        LIST_SIZE_R - 1, nR, c3, 'READS AS FIXED' if c3_ok else '### DOES NOT READ AS FIXED'))

    # ### B: the band, by segments
    del RUNGS[:]
    cB = [acb(half, -arb(B_HALF)), acb(arb(SIG_R), -arb(B_HALF)), acb(arb(SIG_R), arb(B_HALF)), acb(half, arb(B_HALF))]
    nB, cbB, stB = half_path_segments(zq, logg_q, cB, list(PB_SEG), poles=2)
    all_rungs += RUNGS
    log('')
    log('== B   THE BAND [%s, %s] × [−%s, %s] BY ITS HALF PATH, zeros = (1/π)Δ + 2 (Λ_Q`s poles at 0 and 1): %s (ball %s ; segments %d, '
        'depth %d, unresolved %s) ; the list in B 0' % (SIG_L, SIG_R, B_HALF, B_HALF, nB, cbB.str(10, radius=True) if cbB is not None else
                                                      '### UNRESOLVED', stB['segments'], stB['max_depth'], stB['unresolved'] or 'NONE'))

    # ### the Q0 squares
    jobs = [('ON', i, '0.5', repr(g)) for i, g in enumerate(on)] + [('OFF', i, repr(s), repr(t)) for i, (s, t) in enumerate(off)]
    jobs += [('PARTNER', i, (arb(1) - arb(repr(s))).mid().str(30, radius=False), repr(t)) for i, (s, t) in enumerate(off)]
    log('')
    log('== THE SQUARES: %d on-line, %d off-line, %d partners 1 − conj ρ ; h %s, one widening to %s ; %d workers' % (
        len(on), len(off), len(off), H, H_WIDE, procs))
    with mpr.Pool(procs, initializer=_init) as pool:
        ar = pool.map_async(task_square, jobs, chunksize=1)
        while not ar.ready():
            ar.wait(60)
            lows.append(free_mb())
        sq = ar.get()
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
    lv = [x for x in lows if x is not None]
    log('  the host`s free memory: at the start %s MB ; the low sampled during the run %s MB (%d samples) ; the hold %d MB' % (
        fm0, min(lv) if lv else None, len(lv), HOLD_MB))

    # ### H1-H3, V, C
    log('')
    log('== THE HYPOTHESES AND CHECKS, BY PRINTED LINE')
    H1 = h1[1] + h1[2] == h1[0] == 17
    H2 = h2[1] + h2[2] == h2[0] == 146
    H3 = nR == LIST_SIZE_R and nB == 0
    H5 = all((ok3b, ok3d, v1_ok, v2_ok, v3_ok, c1_ok, c2_ok, c3_ok))
    log('  (H1) off-line squares %d ; count 1 at h %d ; count 1 WIDENED %d ; not 1 %s ; each ball centred at its banked value -> %s' % (
        h1[0], h1[1], h1[2], h1[3] or 'NONE', 'HELD' if H1 else 'REFUTED'))
    log('  (H2) on-line squares %d (straddling σ = ½) ; count 1 at h %d ; count 1 WIDENED %d ; not 1 %s -> %s' % (
        h2[0], h2[1], h2[2], h2[3] or 'NONE', 'HELD' if H2 else 'REFUTED'))
    log('  (FE) partner squares %d ; count 1 at h %d ; WIDENED %d ; not 1 %s' % (hp[0], hp[1], hp[2], hp[3] or 'NONE'))
    log('  (H3) N(R) = %s against %d ; zeros in B = %s against 0%s -> %s' % (
        nR, LIST_SIZE_R, nB, (' ; UNLISTED %d' % (nR - LIST_SIZE_R)) if (nR is not None and nR > LIST_SIZE_R) else '', 'HELD' if H3 else 'REFUTED'))
    log('  (H5) (3b) %s ; (3d) %s ; V1 %s ; V2 %s ; V3 %s ; C1 %s ; C2 %s ; C3 %s -> %s' % (ok3b, ok3d, v1_ok, v2_ok, v3_ok, c1_ok, c2_ok,
                                                                                          c3_ok, 'HELD' if H5 else 'REFUTED'))
    log('  Bessel factors taken at %d bits: %d (relay data/b667_bessel_rungs.txt)' % (PREC_BESSEL, len(all_rungs)))
    log('')
    log('### ### **H1 %s ; H2 %s ; H3 %s ; H5 %s ; %.0f s.**' % ('HELD' if H1 else 'REFUTED', 'HELD' if H2 else 'REFUTED', 'HELD' if H3 else 'REFUTED',
                                                            'HELD' if H5 else 'REFUTED', time.time() - T_START))
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
                                                             H1=H1, H2=H2, H3=H3, H5=H5), indent=1, ensure_ascii=False) + NL)
    put('b667_bessel_rungs.txt', NL.join(['b667 -- EVERY BESSEL FACTOR TAKEN AT %d BITS ((R277)(3a)): rows are factors -- m, the evaluation`s '
                                          'point (σ, t) at its centre, the precision.' % PREC_BESSEL, ''] +
                                         ['  m %2d | σ %.15g | t %.15g | %d bits' % x for x in all_rungs] +
                                         ['', '### ### **FACTORS AT %d BITS: %d.**' % (PREC_BESSEL, len(all_rungs))]) + NL)
    say('CERTIFY DONE')


if __name__ == '__main__':
    main()
