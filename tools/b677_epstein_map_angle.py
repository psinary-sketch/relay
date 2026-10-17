# -*- coding: utf-8 -*-
"""b677_epstein_map_angle.py -- THE DETECTION MAP IN THE ANGLE FORM OVER THE NARROWED BALLS: THE RATE INDEX AND THE ZERO SIDE AT THE Q0
CONFIGURATION, BOUND TO zeroSide_neg_at_rate_cfg (SIDE-explicit-formula, Schema/RateIndexCfg.lean :135-:148) AT q0Config, under (R287)(4)
and the navigator's answer on the run (option 2).

### Written whole by the Write tool from tools/b667_epstein_map_balls.py (left as it is): its computation lines kept, and every power taken
### in the angle form, zⁿ = exp(n·log z) with log z once per ball about an exact point at its midpoint (relay data/b677_map_plan.txt
### section 3) -- the phase at j is exp(2^(j+1)·log us) in place of us squared j+1 times, and the zero side's (ĝ/M)^(2^(j₀+1)) likewise.
### The diff against the b667 map is banked (relay data/b677_map_diff.txt, `diff`).
### Added, each named in the plan: the per-tie row (section 5); the plants P1 width, P2 shift, P3 confirmation (section 7); and, on the
### navigator's answer, the labelled reading -- hrate and the zero side computed past the tie controls with hQtie taken from coeffs_exist
### (PowerLimit.lean :686-:704) and the orbit identity (plan section 4), banked as an instrument-side row, not an object finding.
### The balls: relay data/b671_epstein_zeros_narrowed.json.gz (h = 1e-24). Routes, each one foreground part under 600 s:
###   part1 -> data/b677_map.txt (.json) and data/b677_map_run.txt ; part2 -> data/b677_tolerance_p1.json ; part3 -> data/b677_tolerance.txt
###   (.json) ; hyp -> data/b677_map_h.txt (.json) ; diff -> data/b677_map_diff.txt. No lean; no kernel file read.
### Nothing here is about ζ: Z₁ is not ζ's configuration, and the Q0 configuration is Z_Q's only under its premises.
"""
import difflib
import gzip
import hashlib
import io
import json
import math
import os
import re
import sys
import time

from flint import arb, acb, arb_series, ctx

# ================================================================================ THE CONSTANTS, AT THE HEAD
T_HEIGHT = 1000                                            # ### Z₁'s height, b656's binding (relay data/b656_e1_binding.txt :27) -- the control
PREC = 200                                                 # ### Arb balls at 200 bits (relay data/b627_margin_inputs.txt :7)
PREC_RUNG = 400                                            # ### the one rung, 200 -> 400 bits, re-read once (the author's word at b661)
J_EXTRA = 40                                               # ### J_max = D + 40 ((R273)(4), the b662 script's rule)
Z1_CELL = ('0.8', '29.6')                                  # ### the control: b661's Z₁ at its H3 cell
Q0_ON, Q0_OFF = 'b326_epstein_zeros.json', 'b326_offline.json'   # ### the bench's list (on the author's word, b326's)
Q0_CERT = 'b671_epstein_zeros_narrowed.json'               # ### the narrowed balls (b671), read with '.gz' appended, as b671's wrapper read them
Q0_T = 150                                                 # ### the height cut, the banks' own T
Q0_BASE = 0                                                # ### qE0 = the off-line list's index 0, the dominant (data/b663_dominance.txt)
Q0_A0 = 10                                                 # ### A0Q, P3's constant (Schema/EpsteinQ0.lean; data/b663_a0_list.txt)
I4_DELTA0, I4_PIECES, I4_MINW_EXP = 300, 400, 120         # ### ∫|s''''|: the cut [0, 1/300] by a Cauchy bound; 400 pieces; bisection to 2^-120
BAR_EXP = -20                                              # ### the control's bar 2^-20 (the b667 map :349)
WIDTHS = ['1e-%d' % k for k in range(16, 35)]              # ### P1: the planted half-widths 1e-16 ... 1e-24 (as banked) ... 1e-34 (plan section 7;
                                                           # ### the grid widened above 1e-24 after part 2's first run, which could not read h_tol(38))
SHIFT = '1e-12'                                            # ### P2: the shift of one tie point's phase angle (plan section 7)
SHIFT_AT = 1                                               # ### P2: the tie point shifted, 1 − conj ρ
H4_J0, B667_TOL = 38, 1e-18                                # ### H4's j₀ (data/b667_epstein_plan.txt :125) ; b667's estimate (data/b667_h4_reading.txt :14)
PRICE = dict(upper=dict(c=2.092e-21, rad64=7.720e-02, last_pass=47, h_need=1.24e-29),
             lower=dict(c=3.606e-24, rad64=1.330e-04, last_pass=56, h_need=7.17e-27))   # ### the plan's price (data/b677_map_plan.txt section 6)
B671_WIDTH = (('(ii) FROM THE AMPLIFICATION', '8.5e-30, with two decimal orders about 1e-31'),
              ('(i) LINEAR ESTIMATE', '1.5e-38, with two decimal orders 1.5e-40'))   # ### OPEN_TRAILS :14396, left beside the measurement

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_DIR = os.path.join(ROOT, 'data')
B667_MAP = os.path.join(ROOT, 'tools', 'b667_epstein_map_balls.py')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
OUT = []
TALLY = dict(angle=0, square_by_product=0)


def say(s=''):
    OUT.append(s)
    print(s, flush=True)


def b(x, n=12):
    return x.str(n, radius=True)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


# ================================================================================ THE ANGLE FORM (plan section 3)
def lg(z):
    """log z once per ball, about the exact point at its midpoint: log z̃ + log(z/z̃), so the ball of the logarithm sits away from the cut."""
    zt = acb(z.mid()) if isinstance(z, acb) else arb(z.mid())
    return zt.log() + (z / zt).log()


def pw(z, n):
    """zⁿ = exp(n·log z), never repeated multiplication. A square of a ball that holds 0 (where no logarithm is taken) is the one product
    z·z, counted in TALLY and printed; any other power of a ball holding 0 stops the map."""
    if n == 0:
        return acb(1) if isinstance(z, acb) else arb(1)
    if z.contains(0):
        if n == 2:
            TALLY['square_by_product'] += 1
            return z * z
        sys.exit('### A POWER %d OF A BALL HOLDING 0 -- THE MAP STOPS (%s)' % (n, b(z)))
    TALLY['angle'] += 1
    return (n * lg(z)).exp()


# ================================================================================ THE BASE: s, ĝ0, ∫|s''''| (the b667 map :55-:129)
def s_acb(x):
    """Mathlib's smoothTransition, e(x)/(e(x)+e(1-x)), e(x) = exp(-1/x) (TwoPropertyWindow.lean :55), on (0, 1)."""
    e1 = (-1 / x).exp()
    e2 = (-1 / (1 - x)).exp()
    return e1 / (e1 + e2)


def eps_for(prec):
    """the end cut of the ramp integral: exp(1/(1-ε) - 1/ε) below 2^-(prec+10)."""
    return arb(1) / int((prec + 16) * 0.7 + 1)


def ramp_R(w, prec):
    """R(w) = ∫_0^1 s(x) cos(w (1 - x/2)) dx, a ball: acb.integral on [ε, 1-ε]; on [1-ε, 1] the cosine's closed form less ∫(1-s)cos;
    the two end pieces bounded by ε · exp(1/(1-ε) - 1/ε) · cosh|Im w| each (s(x) ≤ e(x)/e(1-x) on [0, ε]; 1 - s(x) = s(1-x))."""
    ep = eps_for(prec)
    mid = acb.integral(lambda x, analytic: s_acb(x) * (w * (1 - x / 2)).cos(), acb(ep), acb(1 - ep))
    a = acb(1 - ep)
    endc = (2 / w) * ((w * (1 - a / 2)).sin() - (w / 2).sin())
    bnd = (2 * ep * (1 / (1 - ep) - 1 / ep).exp() * arb(abs(w.imag)).cosh()).upper()
    tot = mid + endc
    return acb(arb(tot.real.mid(), tot.real.rad() + bnd), arb(tot.imag.mid(), tot.imag.rad() + bnd))


def ghat(z, ell, prec):
    """paperFT (phiC g0) z = ∫ g0(u) e^{izu} du (Zeta23/Defs.lean :60) for g0 = detectorBase ρ₁ = plateau (1/2) ℓ (Detector.lean :40;
    TwoPropertyWindow.lean :56-:57): = ℓ (2 sin(w/2)/w + R(w)), w = zℓ."""
    w = z * ell
    return ell * (2 * (w / 2).sin() / w + ramp_R(w, prec))


def s_series(x, n):
    X = arb_series([x, 1], prec=n)
    e1 = (-1 / X).exp()
    e2 = (-1 / (1 - X)).exp()
    return e1 / (e1 + e2)


def sder(x, k):
    f = 1
    for i in range(2, k + 1):
        f *= i
    return s_series(x, k + 1)[k] * f


def i4_ball():
    """I4 = ∫_0^1 |s''''| = 2 ∫_0^{1/2} |s''''| (the b667 map :102-:124); the Cauchy bound's x⁴ in the angle form."""
    x = arb(1) / I4_DELTA0
    cb = x * 24 * 16 / pw(x, 4) * (-(arb(2) / (3 * x))).exp() / ((-1 / (1 - arb(1.5) * x)).exp() - (-(arb(2) / (3 * x))).exp())
    lo, hi = arb(0), arb(cb.upper())
    a0, b0 = x, arb(1) / 2
    h = (b0 - a0) / I4_PIECES
    stack = [(a0 + i * h, a0 + (i + 1) * h) for i in range(I4_PIECES)]
    minw = arb(2) ** -I4_MINW_EXP
    while stack:
        a, bb = stack.pop()
        v = sder(arb((a + bb) / 2, ((bb - a) / 2).upper()), 4)
        if v > 0 or v < 0:
            p = abs(sder(a, 3) - sder(bb, 3))
            lo, hi = lo + p.lower(), hi + p.upper()
        elif (bb - a) < minw:
            hi = hi + ((bb - a) * abs(v).upper()).upper()
        else:
            m = (a + bb) / 2
            stack += [(a, m), (m, bb)]
    return 2 * arb(lo.lower()), 2 * arb(hi.upper())


def span(lo, hi):
    return arb((lo + hi) / 2, ((hi - lo) / 2).upper())


# ================================================================================ THE ZERO LISTS (the b667 map :132-:155; the width plant P1 added)
def zero_list():
    n = arb.zeta_nzeros(arb(T_HEIGHT))
    if not n.is_exact():
        sys.exit('### N(T) IS NOT EXACT AT T = %d -- THE MAP STOPS' % T_HEIGHT)
    n = int(n.unique_fmpz())
    zs = acb.zeta_zeros(1, n)
    nxt = acb.zeta_zero(n + 1)
    ok = all(z.real == arb(1) / 2 for z in zs) and zs[-1].imag < T_HEIGHT and nxt.imag > T_HEIGHT and len(zs) == n
    return n, [z.imag for z in zs], ok, zs[-1].imag, nxt.imag


def q0_list(width=None):
    """the narrowed balls (relay data/b671_epstein_zeros_narrowed.json.gz): the on-line ordinates as arb(γ, h) and the off-line zeros as
    the ball strings '[σ +/- h]', '[t +/- h]'; with width (P1) every half-width set to that planted value about the banked centre -- a
    planted width, not a certified ball."""
    rows = json.loads(gzip.decompress(open(os.path.join(D_DIR, Q0_CERT + '.gz'), 'rb').read()).decode('utf-8'))['rows']
    on = sorted((r for r in rows if r['kind'] == 'ON'), key=lambda r: r['idx'])
    off = sorted((r for r in rows if r['kind'] == 'OFF'), key=lambda r: r['idx'])
    if not all(r['count'] == 1 for r in on + off) or len(on) != 146 or len(off) != 17:
        sys.exit('### A ROW WITHOUT A CERTIFIED BALL (count not 1) -- THE MAP STOPS')
    h = (lambda r: width) if width is not None else (lambda r: r['h'])
    return [arb(r['im'], h(r)) for r in on], [('[%s +/- %s]' % (r['re'], h(r)), '[%s +/- %s]' % (r['im'], h(r))) for r in off]


# ================================================================================ hA (the b667 map :159-:180, unchanged)
def a0_upper(ords):
    ev = []
    for y in ords:
        lo, hi = y.lower() - 1, y.upper()
        ev.append((lo, 1))
        ev.append((hi, -1))
    ev.sort(key=lambda e: (e[0], -e[1]))
    best, arg, cnt, c = arb(1), None, 0, 0
    for i, (p, dlt) in enumerate(ev):
        c += dlt
        if c <= 0 or i + 1 >= len(ev):
            continue
        a, bb = p, ev[i + 1][0]
        s = arb(0) if (a <= 0 and bb >= 0) else (a if a > 0 else bb)
        r = arb(c) / (abs(s) + 3).log()
        if r.upper() > best.upper():
            best, arg, cnt = arb(r.upper()), s, c
    return best, arg, cnt


# ================================================================================ ONE CELL (the b667 map :184-:409)
def unit(x):
    return x / abs(x)


def orbit_of(sg, t):
    """the four points ρ, 1 − conj ρ, conj ρ, 1 − ρ of an off-line zero σ + it, as gammaOf ρ = (ρ - 1/2)/I (Defs.lean :121)."""
    dl = sg - arb(1) / 2
    return [('ρ', acb(t, -dl)), ('1 − conj ρ', acb(t, dl)), ('conj ρ', acb(-t, -dl)), ('1 − ρ', acb(-t, dl))]


def word(mids, rads, zin, bar):
    """the b671 diagnostic's rule (tools/b671_tie_diagnostic.py :101-:107, the navigator's answer on the two readings at b671)."""
    passed = all(zin) and max(rads) < bar
    obj = all(mm + rr < bar for mm, rr in zip(mids, rads))
    ins = all(zin) and max(rads) >= bar
    return passed, 'PASS' if passed else 'OBJECT' if obj else 'INSTRUMENT' if ins else 'NEITHER'


def cell(name, base, online, offline, prec, i4, above=None, a0_premise=None, rung_note=None, jcap=J_EXTRA, tie_only=False, past=False,
         shift=None):
    ctx.prec = prec
    rec = dict(name=name, base=list(base), prec=prec, certs=[], hrate=[], unresolved=[], reading=None, triggers=[], ties=[])
    sb, tb = arb(base[0]), arb(base[1])
    zb = acb(tb, -(sb - arb(1) / 2))
    ell = 1 / (4 * (abs(zb) + 1))                        # baseWidth ρb (Detector.lean :33)
    say('== CELL %s -- base %s + %s i -- %d bits%s' % (name, base[0], base[1], prec, (' -- ' + rung_note) if rung_note else ''))
    say('  ℓ = baseWidth ρb (Schema/Detector.lean :33) = 1/(4(‖γ(ρb)‖ + 1)) = %s ; L = ℓ (Detector.lean :113)' % b(ell))

    def put_cert(tgt, nm, st, why):
        tgt['certs'].append((nm, st, why))
        say('  %s%-9s %s -- %s' % ('[LABELLED] ' if tgt is not rec else '', nm, st, why))

    def fail(nm, why, tgt=None):
        tgt = rec if tgt is None else tgt
        put_cert(tgt, nm, 'NOT CERTIFIED', why)
        tgt['reading'] = 'HYP-UNVERIFIED(%s)' % nm
        return rec

    def ok(nm, why, tgt=None):
        put_cert(rec if tgt is None else tgt, nm, 'CERTIFIED', why)

    ok('H.hev', 'plateau_even (TwoPropertyWindow.lean :69), the term Detector.lean :114 passes; COMPILED')
    ok('H.hsm', 'plateau_contDiff (TwoPropertyWindow.lean :60), as Detector.lean :114; COMPILED')
    ok('H.hs', 'plateau_support_Icc, as Detector.lean :107-:108; COMPILED')
    ok('H.hL', 'baseWidth_pos (Detector.lean :35); 0 ≤ ℓ; COMPILED')
    orbs = []
    for k, (ss, ts) in enumerate(offline):
        o = orbit_of(arb(ss), arb(ts))
        orbs.append((k, ss, ts, [(nm, z, ghat(z, ell, prec)) for nm, z in o]))
    top = max(orbs, key=lambda x: abs(x[3][0][2]).mid())
    M = abs(top[3][0][2])
    rec['M'] = b(M)
    rec['dominant'] = [top[1], top[2]]
    if not M.is_finite():
        return fail('H.hM', 'M = %s OVERFLOW' % b(M))
    if not M > 0:
        return fail('H.hM', 'M = %s, the ball meets 0 (UNDERFLOW)' % b(M))
    ok('H.hM', 'M = offScore g0 ρ* = |ĝ0(γ(ρ*))| = %s > 0, ρ* = %s + %s i the largest of %d off-line orbit(s)' % (b(M), top[1], top[2], len(orbs)))
    gh = top[3]
    sc = [abs(g) for _nm, _z, g in gh]
    if not all(x.overlaps(M) for x in sc):
        return fail('H.hdom', 'an orbit score of the dominant does not meet M: %s' % ' '.join(b(x, 8) for x in sc))
    others = [o for o in orbs if o[0] != top[0]]
    over = [(o[1], o[2], b(abs(g), 8)) for o in others for _nm, _z, g in o[3] if not abs(g).upper() < M.lower()]
    if over:
        return fail('H.hdom', 'THE GUARD: an off-line point of another orbit does not lie below M: %s -- THE CELL STOPS' % over[:4])
    ok('H.hdom', 'the dominant`s four scores %s each meet M, equal by offScore_reflect (PowerLimit.lean :219) and paperFT_conj_of_real (:36); '
       'the other %d orbit(s), %d point(s), every score below M in balls%s' % (
           ' ; '.join('%s %s' % (nm, b(x, 8)) for (nm, _z, _g), x in zip(gh, sc)), len(others), 4 * len(others),
           '' if above is None else '; above T = %d by B1 (below)' % above))
    sd, tt = arb(top[1]), arb(top[2])
    dl = sd - arb(1) / 2
    t = tt
    v = pw(dl + acb(0, 1) * t, 2)                        # vOf ρ* (PowerLimit.lean :146), the square in the angle form
    if not (v.imag > 0 or v.imag < 0):
        return fail('tieSet', 'Im v = %s meets 0' % b(v.imag))
    ok('tieSet', 'tieSet C g0 M (PowerWindow.lean :398) = the dominant`s orbit, 4 points, mult 1; VF = {v, conj v} (:280), Im v = %s ≠ 0' % b(v.imag))
    aw = (arb(3) / 2 * ell + 16 * i4 / pw(ell, 3)) * (ell / 2).exp()     # Aw (PowerLimit.lean :800)
    rec['Aw'] = b(aw)
    zl = online
    killed, straddle, theta, targ, nread, nscreen = [], [], arb(0), None, 0, 0
    for k, gm in enumerate(zl):
        sb_ = aw.upper() / (1 + pw(gm.lower(), 4))
        if sb_ < M.lower() and (sb_ / M.lower()).upper() <= theta.upper() and theta > 0:
            nscreen = len(zl) - k
            break
        nread += 1
        g = abs(ghat(acb(gm), ell, prec))
        if g.lower() >= M.upper():
            killed.append(gm)
        elif g.upper() < M.lower():
            r = arb((g.upper() / M.lower()).upper())
            if r.upper() > theta.upper():
                theta, targ = r, gm
        else:
            straddle.append((gm, g))
    if straddle:
        return fail('hθ', 'the kill set not decided: %d zero(s) whose score ball straddles M, first at γ = %s, score %s' % (
            len(straddle), b(straddle[0][0], 10), b(straddle[0][1], 10)))
    for o in others:
        for _nm, _z, g in o[3]:
            r = arb((abs(g).upper() / M.lower()).upper())
            if r.upper() > theta.upper():
                theta, targ = r, 'off-line %s + %s i' % (o[1][:10], o[2][:10])
    b1 = None
    if above is not None:
        b1 = arb((2 * (ell / 2).exp() / (arb(above) * M.lower())).upper())
        if b1.upper() > theta.upper():
            theta, targ = b1, 'B1 at |Im ρ| = %d' % above
        rec['B1'] = b(b1)
        say('  B1        the points of Z with |Im ρ| ≥ %d: offScore g0 ρ / M ≤ 2 e^{ℓ/2}/(%d M) = %s ; certified on B1 (READ)' % (above, above, b(b1, 10)))
    rec['theta_at'] = str(targ)
    xr = [-pw(gm, 2) for gm in killed]                   # Xr (PowerLimit.lean :268), one per |γ|
    ok('killSet', 'killSet C g0 M (PowerWindow.lean :401): zeros read %d, killed %d, screened by the decay bound %d, straddling 0; '
       'off-line points killed 0 (the guard); card Xr = %d' % (nread, len(killed), nscreen, len(xr)))
    ords = [x for gm in zl for x in (gm, -gm)] + [x for o in orbs for x in (arb(o[2]), arb(o[2]), -arb(o[2]), -arb(o[2]))]
    a0l, sarg, scnt = a0_upper(ords)
    if a0_premise is None:
        a0 = a0l
        ok('hA', 'HCount C.toZeroConfig A₀ (RestBound.lean :44-:45): A₀ = %s' % a0.str(15, radius=False))
    else:
        a0 = arb(a0_premise)
        if not a0l.upper() <= a0.lower():
            return fail('hA', 'the listed points` own A₀ %s exceeds P3`s A0Q = %s' % (a0l.str(15, radius=False), a0_premise))
        ok('hA', 'HCount C.toZeroConfig A0Q BY P3 (Q0Count, a named premise, stated, not proved; open), A0Q = %s; the listed points` own '
           'A₀ = %s ≤ A0Q' % (a0_premise, a0l.str(15, radius=False)))
    D = 2 * len(xr) + 8
    jmax = D + jcap
    cE = 1 + 4 / abs(dl)                                 # cE (PowerLimit.lean :274)
    cv = 2 * (abs(v) + 1) / abs(v - v.conjugate())       # CV (PowerWindow.lean :432)
    bk = (len(xr) + 1) * _prod([1 + pw(gm, 2) for gm in killed])
    be = 2 * (1 + cE)
    B = 2 * cv * bk * be
    say('  D = 2·card Xr + 8 = %d ; J_max = D + %d = %d ; cE = %s ; CV = %s ; BK = %s ; BE = %s ; B = %s' % (
        D, jcap, jmax, b(cE, 10), b(cv, 10), b(bk, 10), b(be, 10), b(B, 10)))
    rec.update(D=D, J_max=jmax, card_Xr=len(xr), A0=a0.str(15, radius=False), B=b(B), theta=b(theta))
    cE2 = pw(cE, 2)

    def kp(w):
        return _prod([w - x for x in xr]) if xr else acb(1)

    def F(w):
        return pw(kp(w), 2) * (1 - cE2 * w)

    # ### THE TIE TEST IN THE ANGLE FORM (the b667 map :331-:356): the phase at j is exp(2^(j+1)·log us), log us once per tie point
    us = [unit(g) for _nm, _z, g in gh]
    lus = [lg(u) for u in us]
    if shift is not None:                                # ### P2: one tie point's angle shifted (plan section 7)
        dlt = arb(lus[SHIFT_AT].imag.rad()) / 4 if shift == 'quarter' else arb(shift)
        lus[SHIFT_AT] = lus[SHIFT_AT] + acb(0, dlt)
        rec['shift'] = dict(at=gh[SHIFT_AT][0], delta=b(dlt, 6))
        say('  ### P2 THE SHIFT PLANT: the angle at %s shifted by %s' % (gh[SHIFT_AT][0], b(dlt, 6)))
    rec['angle_rad'] = [float(l.imag.rad()) for l in lus]
    nodes = [v, v.conjugate(), v.conjugate(), v]
    bar = arb(2) ** BAR_EXP
    Qs, nt, nb = {}, 0, 0
    for j in range(D, jmax + 1):
        e = 2 ** (j + 1)
        pwj = [(e * l).exp() for l in lus]
        TALLY['angle'] += len(lus)
        ph = [unit(F(nd)) * p for nd, p in zip(nodes, pwj)]
        yv = -ph[0].conjugate()
        r1, r2 = yv.sqrt(), acb(0, 1) * (-yv).sqrt()
        r = r1 if r1.rad() <= r2.rad() else r2
        bq = r.imag / v.imag
        aq = r.real - bq * v.real
        Qs[j] = (aq, bq)
        res = [pw(acb(aq) + bq * nd, 2) * p + 1 for nd, p in zip(nodes, ph)]
        mids = [float(abs(x.mid())) for x in res]
        rads = [float(x.rad()) for x in res]
        zin = [bool(x.real.contains(0) and x.imag.contains(0)) for x in res]
        passed, wd = word(mids, rads, zin, float(bar))
        if all(x.real.contains(0) and x.imag.contains(0) and x.rad() < bar for x in res):
            nt += 1
        if abs(aq).upper() <= cv.lower() and abs(bq).upper() <= cv.lower():
            nb += 1
        arad = max(float((e * l).imag.rad()) for l in lus)
        rec['ties'].append(dict(j=j, mids=mids, rads=rads, zin=zin, angle_rad=arad, word=wd))
        say('  TIE %s %d j %d : angle rad %.3e ; ' % (name, prec, j, arad) + ' | '.join(
            '|mid| %.3e ; rad %.3e ; 0 in %s' % (mm, rr, zz) for mm, rr, zz in zip(mids, rads, zin)) + ' ; %s' % wd)
    k = jmax - D + 1
    rec['hqtie'] = [nt, k]
    if tie_only:
        rec['reading'] = 'TIE ONLY (a plant)'
        return rec
    tgt = rec
    if nt < k:
        fail('hQtie', 'by coeffs_exist, inputs certified; controls %d of %d -- a tie residual ball not resolved at 0' % (nt, k))
        if not past:
            return rec
        tgt = rec['labelled'] = dict(note='hQtie taken from coeffs_exist (PowerLimit.lean :686-:704) and the orbit identity (relay '
                                          'data/b677_map_plan.txt section 4), not from balls -- an instrument-side reading row, not an '
                                          'object finding (the navigator`s answer on the run)', certs=[], hrate=[], unresolved=[],
                                     triggers=[], reading=None)
        say('  ### [LABELLED] THE READING PAST THE TIE CONTROLS: %s' % tgt['note'])
    else:
        ok('hQtie', 'by coeffs_exist (PowerLimit.lean :686-:704), inputs certified; controls %d of %d' % (nt, k))
    if nb < k:
        fail('hQb', 'by coeffs_exist, inputs certified; controls %d of %d -- |a_j| or |b_j| not below CV' % (nb, k), tgt)
        return rec
    ok('hQb', 'by coeffs_exist (PowerLimit.lean :705-:731), inputs certified; controls %d of %d' % (nb, k), tgt)
    ok('hθ0', 'θ = %s ≥ 0' % theta.str(15, radius=False), tgt)
    ok('hθ', 'every point outside the tie and kill sets read or screened: offScore/M ≤ θ%s' % (
        '' if above is None else '; the points above T certified on B1 (READ), not a kernel lemma'), tgt)
    z3 = 2 * arb(3).zeta() - 1
    rhs = sum((abs(F(nd)) for nd in nodes), arb(0))
    if not rhs > 0:
        fail('hrate', 'the right side %s meets 0 (UNDERFLOW)' % b(rhs), tgt)
        return rec
    lr = rhs.log()
    base = (3 * a0 * z3 * 128).log() + D * arb(8).log() + 2 * B.log() + arb(2) ** (D + 1) * (aw / M).log()
    j0 = None
    for j in range(D, jmax + 1):
        ex = 2 ** (j + 1) - 2 ** (D + 1)
        if ex == 0:
            ll = base
        elif theta == 0:
            ll = None
        else:
            ll = base + ex * theta.log()
        if ll is None:
            st, sides = 'HOLDS', 'left 0 (θ = 0) ; right %s' % b(rhs, 10)
        else:
            if not ll.is_finite():
                tgt['triggers'].append('hrate OVERFLOW at j = %d' % j)
                st = 'OVERLAP'
            elif ll.upper() < lr.lower():
                st = 'HOLDS'
            elif ll.lower() > lr.upper():
                st = 'FAILS'
            else:
                st = 'OVERLAP'
            sides = 'left exp(%s) ; right exp(%s) = %s' % (b(ll, 15), b(lr, 15), b(rhs, 10))
        tgt['hrate'].append((j, st, sides))
        say('    %shrate j = %-3d %-7s %s' % ('[LABELLED] ' if tgt is not rec else '', j, st, sides))
        if st == 'OVERLAP':
            tgt['unresolved'].append(j)
        if st == 'HOLDS' and j0 is None:
            j0 = j
            break
    tgt['reading'] = ('j₀ = %d' % j0) if j0 is not None else 'NONE ≤ J_max'
    if j0 is not None:
        tgt['j0'] = j0
    tgt['sides'] = tgt['hrate'][-1][2]
    if j0 is not None:
        tgt['zero_side'] = zero_side(j0, Qs[j0], kp, F, gh, others, M, zl, killed, nread, aw, ell, prec, cE, a0, above, b1,
                                     '[LABELLED] ' if tgt is not rec else '')
    return rec


def _prod(xs):
    p = arb(1) if not xs or isinstance(xs[0], arb) else acb(1)
    for x in xs:
        p = p * x
    return p


def _rpow(rr, E):
    """a ratio ball rr ≥ 0 raised to E: in the angle form where rr is held off 0, else as the ball [0, ub^E] (the power increasing)."""
    if rr.contains(0) or not rr > 0:
        u = pw(arb(rr.upper()), E).upper()
        return arb(u / 2, u / 2)
    return pw(rr, E)


def zero_side(j0, Q, kp, F, gh, others, M, zl, killed, nread, aw, ell, prec, cE, a0, above, b1, tag=''):
    """the b667 map :419-:475, every power in the angle form: (ĝ/M)^(2^(j₀+1)) = exp(2^(j₀+1)·log(ĝ/M))."""
    aq, bq = Q
    E = 2 ** (j0 + 1)
    tot = acb(0)
    for _nm, z, g in gh:
        vv = pw(acb(0, 1) * z, 2)
        q = acb(aq) + bq * vv
        tot += pw(q, 2) * F(vv) * pw(g / M, E)
    oth = acb(0)
    for o in others:
        for _nm, z, g in o[3]:
            vv = pw(acb(0, 1) * z, 2)
            q = acb(aq) + bq * vv
            oth += pw(q, 2) * F(vv) * pw(g / M, E)
    on = arb(0)
    kset = set(id(x) for x in killed)
    for k, gm in enumerate(zl):
        if id(gm) in kset:
            continue
        vv = acb(-pw(gm, 2))
        q = acb(aq) + bq * vv
        fac = (pw(q, 2) * F(vv)).real
        if k < nread:
            rr = abs(ghat(acb(gm), ell, prec)) / M
        else:
            rr = arb(0, (aw.upper() / (1 + pw(gm.lower(), 4)) / M.lower()).upper())
        p = _rpow(rr, E)
        term = 2 * fac * p
        on = on + (term if k < nread else arb(term.upper() / 2, term.upper() / 2))
    tail = arb(0)
    if above is not None:
        K = 7 + 4 * len(killed)
        c0 = 2 * arb(a0) * pw(abs(acb(aq)) + abs(bq), 2) * _prod([pw(1 + pw(gm, 2), 2) for gm in killed]) * (1 + pw(cE, 2)) * pw(arb('1.0201'), 3 + 2 * len(killed))
        bnd = c0 * pw(arb(above), K) * (E * b1.log()).exp() * (2 + arb(above) / (E - K - 1))
        tail = arb(0, bnd.upper())
        say('  %sthe points above T = %d: |Σ terms| ≤ %s, on B1 (READ) and P3 (A0Q = %s) -- K = %d, E = 2^(j₀+1) = 2^%d' % (
            tag, above, b(arb(bnd.upper()), 6), a0.str(5, radius=False), K, j0 + 1))
    zs = tot.real + oth.real + on + tail
    held = bool(zs < 0)
    say('  %sTHE ZERO SIDE at j₀ = %d: %s -- the dominant`s orbit %s, the other off-line orbits %s, the on-line terms %s, the points above T '
        '%s ; the ball %s 0' % (tag, j0, b(zs, 15), b(tot.real, 15), b(oth.real, 15), b(on, 15), b(tail, 6), 'BELOW' if held else 'NOT BELOW'))
    return dict(j0=j0, zero_side=b(zs, 20), orbit=b(tot.real, 20), others=b(oth.real, 20), online=b(on, 20), above=b(tail, 8), held=held)


# ================================================================================ THE CELLS AND THE RUNG (the b667 map :479-:501)
def run_cell(name, base, online, offline, i4s, zls_rung, above=None, a0_premise=None, past=False):
    r = cell(name, base, online, offline, PREC, i4s[PREC], above=above, a0_premise=a0_premise, past=past)
    trig = []
    if r['reading'].startswith('HYP-UNVERIFIED'):
        trig.append(r['reading'])
    if r['unresolved']:
        trig.append('hrate overlap at j = %s' % r['unresolved'])
    trig += r['triggers']
    if trig:
        ctx.prec = PREC_RUNG
        if PREC_RUNG not in i4s:
            lo, hi = i4_ball()
            i4s[PREC_RUNG] = span(lo, hi)
        online2 = zls_rung() if zls_rung else online
        say('  ### the 200-bit reading %s ; triggers: %s -- RE-READ ONCE AT %d BITS:' % (r['reading'], '; '.join(trig), PREC_RUNG))
        r2 = cell(name, base, online2, offline, PREC_RUNG, i4s[PREC_RUNG], above=above, a0_premise=a0_premise, rung_note='the rung, re-read once',
                  past=past)
        r2['first'] = dict(reading=r['reading'], triggers=trig, ties=r['ties'], labelled=r.get('labelled'), hqtie=r.get('hqtie'))
        r = r2
    if r['reading'].startswith('j₀') and r['unresolved']:
        r['reading'] += ' (UNRESOLVED-AT-j %s beside it: the true j₀ may be lower)' % ', '.join(str(j) for j in r['unresolved'])
    say('  READING %s: %s' % (name, r['reading']))
    if r.get('labelled'):
        say('  [LABELLED] READING %s past the tie controls: %s' % (name, r['labelled']['reading']))
    say('')
    return r


def _i4():
    ctx.prec = PREC
    lo, hi = i4_ball()
    return {PREC: span(lo, hi)}


def _put(name, text):
    p = os.path.join(D_DIR, name)
    open(p + '.tmp', 'wb').write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)


def _putj(name, obj):
    _put(name, json.dumps(obj, indent=1, ensure_ascii=False, default=str) + NL)


def _b671_words():
    """the b671 diagnostic's word per (cell, bits, j), read from its bank's rows (data/b671_tie_diagnostic.txt :7-:129)."""
    t = io.open(os.path.join(D_DIR, 'b671_tie_diagnostic.txt'), encoding='utf-8').read()
    out = {}
    for i, l in enumerate(t.split(NL), 1):
        m = re.match(r'^  (THE CONTROL Z₁\(0\.8, 29\.6\)|Q0 AT qE0)\s+(\d+) j (\d+) : .* ; (PASS|INSTRUMENT|OBJECT|NEITHER)$', l)
        if m:
            out[(m.group(1), int(m.group(2)), int(m.group(3)))] = (m.group(4), i)
    return out


# ================================================================================ PART 1: THE CONTROL AND Q0, THE 123 ROWS (plan section 9)
def part1(*a):
    t0 = time.time()
    s0 = sha(B667_MAP)
    say('b677 -- PART 1: THE DETECTION MAP IN THE ANGLE FORM, THE CONTROL Z₁ AND Q0 AT qE0 ON THE NARROWED BALLS, UNDER (R287)(4) (%s)' % utc())
    say('### the b667 map tools/b667_epstein_map_balls.py sha256 %s before the part ; python-flint %s ; %d bits, the rung %d ; J_max = D + %d.'
        % (s0, __import__('flint').__version__, PREC, PREC_RUNG, J_EXTRA))
    say('')
    i4s = _i4()
    say("### ∫_0^1 |s''''| at %d bits: I4 = %s" % (PREC, b(i4s[PREC], 20)))
    n, zl, okz, _l, _n = zero_list()
    say('### THE CONTROL`S ZERO LIST at %d bits: N(%d) = %d ; %s' % (PREC, T_HEIGHT, n, 'MATCHED' if okz else 'NOT MATCHED -- THE CONTROL STOPS'))
    if not okz:
        sys.exit(2)

    def zl_rung():
        ctx.prec = PREC_RUNG
        n2, z2, ok2, _a, _b = zero_list()
        if not ok2 or n2 != n:
            sys.exit('### THE ZERO LIST AT %d BITS DOES NOT MATCH -- THE MAP STOPS' % PREC_RUNG)
        return z2
    say('')
    rc = run_cell('THE CONTROL Z₁(%s, %s)' % Z1_CELL, Z1_CELL, zl, [Z1_CELL], i4s, zl_rung)
    zc = rc.get('zero_side')
    c_ok = rc.get('j0') == 31 and zc is not None and zc['held']
    say('  ### THE CONTROL %s -- expected j₀ = 31 and the zero side below 0; read j₀ = %s' % ('REPRODUCED' if c_ok else 'NOT REPRODUCED', rc.get('j0')))
    say('')
    if not c_ok:
        _put('b677_map_run.txt', NL.join(OUT) + NL)
        sys.exit('### THE CONTROL NOT REPRODUCED IN THE ANGLE FORM -- THE ACT STOPS BEFORE ANY Q0 ROW (plan section 10)')
    ctx.prec = PREC
    on, off = q0_list()
    say('### THE Q0 LIST: relay data/%s.gz, %d ordinates, %d off-line zeros; the base qE0 = %s + %s i ; T = %d ; A0Q = %d' % (
        Q0_CERT, len(on), len(off), off[Q0_BASE][0], off[Q0_BASE][1], Q0_T, Q0_A0))
    say('')
    rq = run_cell('Q0 AT qE0', off[Q0_BASE], on, off, i4s, None, above=Q0_T, a0_premise=Q0_A0, past=True)
    s1 = sha(B667_MAP)
    say('### the b667 map sha256 %s after the part (%s) ; powers in the angle form %d ; squares by one product of a ball holding 0 %d ; '
        'elapsed %d s' % (s1, 'EQUAL' if s1 == s0 else 'CHANGED', TALLY['angle'], TALLY['square_by_product'], int(time.time() - t0)))
    _put('b677_map_run.txt', NL.join(OUT) + NL)
    bank_map(rc, rq, c_ok, s0, s1, int(time.time() - t0))


def bank_map(rc, rq, c_ok, s0, s1, secs):
    W = _b671_words()
    bar = 2.0 ** BAR_EXP
    groups = [('THE CONTROL Z₁(0.8, 29.6)', PREC, rc['ties'] if 'first' not in rc else rc['first']['ties'])]
    if 'first' in rq:
        groups += [('Q0 AT qE0', PREC, rq['first']['ties']), ('Q0 AT qE0', PREC_RUNG, rq['ties'])]
    else:
        groups += [('Q0 AT qE0', PREC, rq['ties'])]
    rows = []
    for cellname, bits, ties in groups:
        for x in ties:
            w671 = W.get((cellname, bits, x['j']), (None, None))
            rows.append(dict(cell=cellname, bits=bits, j=x['j'], mids=x['mids'], rads=x['rads'], zin=x['zin'], angle_rad=x['angle_rad'],
                             rad=max(x['rads']), word=x['word'], b671=w671[0], b671_row=w671[1]))
    L = ['b677 -- THE MAP IN THE ANGLE FORM (data/b677_map.txt), UNDER (R287)(4) (%s): rows are ties -- the cell, the precision, j; the phase '
         'angle`s radius at j (the largest of the four, exp(2^(j+1)·log us)); at each of the four tie points the residual`s |mid| and radius; '
         'the largest radius and its ratio to the bar 2^-20 = %.6e; the word by the b671 diagnostic`s rule (INSTRUMENT, OBJECT, PASS or '
         'NEITHER); the b671 word from its cited row.' % (utc(), bar), '',
         '### the tool tools/b677_epstein_map_angle.py sha256 %s ; the b667 map sha256 %s before and %s after (%s) ; the balls relay '
         'data/%s.gz ; part 1 %d s.' % (sha(os.path.abspath(__file__)), s0, s1, 'EQUAL' if s0 == s1 else 'CHANGED', Q0_CERT, secs),
         '### the control Z₁ %s (j₀ = %s, the zero side %s).' % ('REPRODUCED' if c_ok else 'NOT REPRODUCED', rc.get('j0'),
                                                                ('BELOW 0' if rc.get('zero_side', {}).get('held') else 'NOT BELOW 0')), '']
    for x in rows:
        L.append('  %-26s %3d j %2d : angle rad %.3e ; ' % (x['cell'], x['bits'], x['j'], x['angle_rad']) + ' | '.join(
            '|mid| %.3e rad %.3e' % (mm, rr) for mm, rr in zip(x['mids'], x['rads'])) + ' ; rad max %.3e ; rad/bar %.3e ; %-10s ; b671 %s (:%s)' % (
            x['rad'], x['rad'] / bar, x['word'], x['b671'], x['b671_row']))
    L.append('')
    for cellname, bits, _t in groups:
        g = [x for x in rows if (x['cell'], x['bits']) == (cellname, bits)]
        ps = [x['j'] for x in g if x['word'] == 'PASS']
        fl = [x for x in g if x['word'] != 'PASS']
        was = [x for x in g if x['b671'] == 'INSTRUMENT']
        L.append('### ### **%s at %d bits : CONTROLS %d ; PASS %d (j %s) ; INSTRUMENT %d ; OBJECT %d ; NEITHER %d ; of b671`s INSTRUMENT %d now PASS %d ; '
                 'the first failing j %s ; the radius at j = 64 %s.**' % (
                     cellname, bits, len(g), len(ps), ('%d-%d' % (min(ps), max(ps))) if ps else '-', sum(x['word'] == 'INSTRUMENT' for x in fl),
                     sum(x['word'] == 'OBJECT' for x in fl), sum(x['word'] == 'NEITHER' for x in fl), len(was),
                     sum(x['word'] == 'PASS' for x in was), min((x['j'] for x in fl), default='-'),
                     next(('%.3e' % x['rad'] for x in g if x['j'] == 64), '-')))
    L.append('### ### **ROWS %d (the b671 list: 41 + 41 + 41) ; NONE DROPPED %s.**' % (len(rows), len(rows) == 123))
    _put('b677_map.txt', NL.join(L) + NL)
    _putj('b677_map.json', dict(at=utc(), rows=rows, control=dict(reproduced=c_ok, j0=rc.get('j0'), zero_side=rc.get('zero_side')),
                                q0=dict(reading=rq['reading'], hqtie=rq.get('hqtie'), first=dict((k, v) for k, v in rq.get('first', {}).items() if k != 'ties'),
                                        certs=rq['certs'], labelled=rq.get('labelled'), zero_side=rq.get('zero_side'), D=rq.get('D'),
                                        J_max=rq.get('J_max'), angle_rad=rq.get('angle_rad')),
                                tally=TALLY, secs=secs))
    print(NL.join(L[-5:]))


# ================================================================================ PART 2: P1 THE WIDTH PLANT (plan section 7)
def _tie_cell(width=None, shift=None, prec=PREC):
    on, off = q0_list(width)
    i4s = _i4() if prec == PREC else None
    if i4s is None:
        ctx.prec = prec
        lo, hi = i4_ball()
        i4s = {prec: span(lo, hi)}
    return cell('Q0 AT qE0', off[Q0_BASE], on, off, prec, i4s[prec], above=Q0_T, a0_premise=Q0_A0, tie_only=True, shift=shift,
                rung_note='a plant: width %s%s' % (width or 'as banked', '' if shift is None else ', shift %s' % shift))


def part2(*a):
    t0 = time.time()
    s0 = sha(B667_MAP)
    res = {}
    for h in WIDTHS:
        t1 = time.time()
        r = _tie_cell(width=h)
        res[h] = dict(secs=int(time.time() - t1), passing=[x['j'] for x in r['ties'] if x['word'] == 'PASS'],
                      rows=[dict(j=x['j'], word=x['word'], rad=max(x['rads']), angle_rad=x['angle_rad']) for x in r['ties']],
                      angle_rad=r['angle_rad'])
        print('  P1 h = %s : PASS j %s ; %d s' % (h, _runs(res[h]['passing']), res[h]['secs']), flush=True)
    tol = _tolerance(res)
    bis = {}
    for j in (H4_J0, 64):
        lo_h, hi_h = tol[j]['passing_h'], tol[j]['failing_h']
        if lo_h is not None and hi_h is not None:
            hm = '%.3e' % math.sqrt(float(lo_h) * float(hi_h))
            r = _tie_cell(width=hm)
            row = next(x for x in r['ties'] if x['j'] == j)
            bis[j] = dict(h=hm, word=row['word'], rad=max(row['rads']))
            print('  P1 bisection at j = %d : h = %s %s' % (j, hm, row['word']), flush=True)
    _putj('b677_tolerance_p1.json', dict(at=utc(), widths=res, tolerance=tol, bisection=bis, sha_b667=[s0, sha(B667_MAP)],
                                         secs=int(time.time() - t0)))
    print('### P1 banked (data/b677_tolerance_p1.json) ; %d s' % int(time.time() - t0))


def _runs(js):
    if not js:
        return '-'
    out, s, p = [], js[0], js[0]
    for j in js[1:] + [None]:
        if j is not None and j == p + 1:
            p = j
            continue
        out.append('%d-%d' % (s, p) if s != p else '%d' % s)
        if j is not None:
            s = p = j
    return ', '.join(out)


def _tolerance(res):
    """h_tol(j): the largest planted width on the grid at which the control at j passes, with the next width up that fails."""
    hs = sorted(res, key=lambda h: float(h))
    tol = {}
    for j in range(24, 65):
        ps = [h for h in hs if j in res[h]['passing']]
        best = max(ps, key=float) if ps else None
        up = [h for h in hs if best is not None and float(h) > float(best)]
        tol[j] = dict(passing_h=best, failing_h=min(up, key=float) if up else None)
    return tol


# ================================================================================ PART 3: P2 THE SHIFT CONTROL, P3 THE CONFIRMATION
def part3(*a):
    t0 = time.time()
    p1 = json.load(io.open(os.path.join(D_DIR, 'b677_tolerance_p1.json'), encoding='utf-8'))
    tol = dict((int(k), v) for k, v in p1['tolerance'].items())
    p2 = {}
    for nm, sh in (('P2 shift 1e-12', SHIFT), ('P2 shift a quarter of the angle`s radius', 'quarter')):
        r = _tie_cell(shift=sh)
        p2[nm] = dict(shift=r.get('shift'), rows=[dict(j=x['j'], word=x['word'], zin=x['zin'], rad=max(x['rads']), mid=max(x['mids'])) for x in r['ties']])
        print('  %s : words %s' % (nm, sorted(set(x['word'] for x in p2[nm]['rows']))), flush=True)
    p3 = {}
    for j in (H4_J0, 64):
        ht = _best_tol(p1, j)
        if ht is None:
            p3[j] = dict(h_tol=None, note='no passing width on the grid')
            continue
        out = {}
        for nm, f in (('at h_tol/3 (expected PASS)', 1 / 3), ('at 3·h_tol (expected FAIL)', 3)):
            hh = '%.3e' % (ht * f)
            r = _tie_cell(width=hh)
            row = next(x for x in r['ties'] if x['j'] == j)
            out[nm] = dict(h=hh, word=row['word'], rad=max(row['rads']))
            print('  P3 j = %d %s : h = %s %s' % (j, nm, hh, row['word']), flush=True)
        p3[j] = dict(h_tol=ht, rows=out)
    bank_tolerance(p1, tol, p2, p3, int(time.time() - t0))


def _best_tol(p1, j):
    """the measured tolerance at j: the bisection's width where it passed, else the grid's passing width."""
    bj = p1.get('bisection', {}).get(str(j))
    t = p1['tolerance'][str(j)]
    if bj and bj['word'] == 'PASS':
        return float(bj['h'])
    return float(t['passing_h']) if t['passing_h'] is not None else None


def bank_tolerance(p1, tol, p2, p3, secs):
    bar = 2.0 ** BAR_EXP
    ar = p1['widths']['1e-24']['angle_rad']
    transfer = max(ar) / 1e-24
    L = ['b677 -- THE CONSUMER`S TOLERANCE, MEASURED ON THE CONSUMER (data/b677_tolerance.txt), UNDER (R287)(4) H2 AND H5 (%s): rows are the '
         'perturbation, the consumer`s response and the tolerance read. The consumer: the tie check of the map (data/b667_h4_reading.txt :9-:14; '
         'every residual ball holding 0 with radius below 2^-20 = %.6e).' % (utc(), bar), '',
         '### P1 THE WIDTH PLANT: every input ball`s half-width set to h about the banked centres (a planted width, not a certified ball); the '
         'Q0 cell`s tie test in the angle form at %d bits; per width the passing j and the part`s seconds.' % PREC]
    for h in sorted(p1['widths'], key=float, reverse=True):
        w = p1['widths'][h]
        L.append('  P1 h = %-6s : PASS j %-10s ; the phase angle`s input radius (largest of four) %.3e ; %d s' % (h, _runs(w['passing']), max(w['angle_rad']), w['secs']))
    L += ['', '### THE TRANSFER: the input width to the phase angle`s radius at qE0, at h = 1e-24: %.3e / 1e-24 = %.3e (b671`s "6.1·10³" '
          'beside it, OPEN_TRAILS :14396).' % (max(ar), transfer), '',
          '### h_tol(j), THE LARGEST PASSING WIDTH ON THE GRID AND THE NEXT ONE UP THAT FAILS (rows are j):']
    for j in range(24, 65):
        t = tol[j]
        L.append('  j %2d : h_tol %-7s ; fails at %s' % (j, t['passing_h'] or 'NONE', t['failing_h'] or '-'))
    L += ['', '### THE BISECTION (one half-decade step between the grid`s last pass and first fail):']
    for j, x in sorted(p1.get('bisection', {}).items(), key=lambda kv: int(kv[0])):
        L.append('  j %s : h = %s %s (rad %.3e)' % (j, x['h'], x['word'], x['rad']))
    L += ['', '### P2 THE SHIFT PLANT, A POSITIVE CONTROL (one tie point`s phase angle shifted, the symmetry of plan section 4 broken):']
    for nm, x in p2.items():
        ws = [r['word'] for r in x['rows']]
        L.append('  %s (at %s, δ = %s) : %s' % (nm, x['shift']['at'], x['shift']['delta'], ' '.join('j%d %s' % (r['j'], r['word']) for r in x['rows'])))
        L.append('    words: %s' % ', '.join('%s %d' % (w, ws.count(w)) for w in sorted(set(ws))))
    L += ['', '### P3 THE CONFIRMATION (H5): at j = 38 and j = 64, P1 re-run at h_tol/3 and 3·h_tol:']
    for j, x in p3.items():
        if x.get('rows') is None:
            L.append('  j %d : %s' % (j, x['note']))
            continue
        for nm, r in x['rows'].items():
            L.append('  j %d : h_tol %.3e ; %s : h = %s %s' % (j, x['h_tol'], nm, r['h'], r['word']))
    t38, t64 = _best_tol(p1, H4_J0), _best_tol(p1, 64)
    L += ['', '### THE TOLERANCE READ:',
          '  at j = 38 (b667`s sizing): h_tol %s ; b667`s estimate %.0e (data/b667_h4_reading.txt :13-:14) ; ratio measured / estimate %s' % (
              ('%.3e' % t38) if t38 else 'NONE', B667_TOL, ('%.3e' % (t38 / B667_TOL)) if t38 else '-'),
          '  at j = 64 (J_max): h_tol %s ; the banked width 1e-24 %s it' % (('%.3e' % t64) if t64 else 'NONE ON THE GRID',
                                                                           'within' if (t64 and 1e-24 <= t64) else 'ABOVE'),
          '  the plan`s price (data/b677_map_plan.txt section 6) beside it: the width carrying every control to j = 64, %.2e (upper) to %.2e '
          '(lower); b671`s figures left beside with their labels: %s.' % (
              PRICE['upper']['h_need'], PRICE['lower']['h_need'], '; '.join('%s %s' % kv for kv in B671_WIDTH)), '',
          '### ### **P1 WIDTHS %d ; h_tol(38) %s ; h_tol(64) %s ; P2 SHIFT 1e-12 FIRES %s ; P2 QUARTER-RADIUS SHIFT AS UNPLANTED %s ; P3 %s ; %d s.**' % (
              len(p1['widths']), ('%.3e' % t38) if t38 else 'NONE', ('%.3e' % t64) if t64 else 'NONE',
              all(r['word'] != 'PASS' for r in p2['P2 shift 1e-12']['rows']),
              [r['j'] for r in p2['P2 shift a quarter of the angle`s radius']['rows'] if r['word'] == 'PASS'] ==
              [r['j'] for r in p1['widths']['1e-24']['rows'] if r['word'] == 'PASS'],
              'AS PLANTED' if all(x.get('rows') and list(x['rows'].values())[0]['word'] == 'PASS' and list(x['rows'].values())[1]['word'] != 'PASS'
                                  for x in p3.values()) else 'NOT AS PLANTED', secs)]
    _put('b677_tolerance.txt', NL.join(L) + NL)
    _putj('b677_tolerance.json', dict(at=utc(), transfer=transfer, tolerance=tol, p2=p2, p3=p3, h_tol38=t38, h_tol64=t64, secs=secs))
    print(NL.join(L[-8:]))


# ================================================================================ THE HYPOTHESES (data/b677_map_h.txt)
def hyp(*a):
    m = json.load(io.open(os.path.join(D_DIR, 'b677_map.json'), encoding='utf-8'))
    tj = json.load(io.open(os.path.join(D_DIR, 'b677_tolerance.json'), encoding='utf-8'))
    rows = m['rows']
    bar = 2.0 ** BAR_EXP
    was = [x for x in rows if x['b671'] == 'INSTRUMENT']
    still = [x for x in was if x['word'] != 'PASS']
    h1 = not still
    q64 = [x for x in rows if x['cell'] == 'Q0 AT qE0' and x['j'] == 64]
    h2 = all(x['rad'] < bar for x in q64) and tj['h_tol64'] is not None and 1e-24 <= tj['h_tol64']
    q = m['q0']
    h3 = q['reading'].startswith('j₀')
    zs = q.get('zero_side')
    p3 = tj['p3']
    h5 = all(x.get('rows') and list(x['rows'].values())[0]['word'] == 'PASS' and list(x['rows'].values())[1]['word'] != 'PASS' for x in p3.values())
    lab = q.get('labelled') or {}
    first_fail = min((x['j'] for x in rows if x['cell'] == 'Q0 AT qE0' and x['word'] != 'PASS'), default=None)
    L = ['b677 -- THE HYPOTHESES OF (R287)(4), READ ON THE RUN (data/b677_map_h.txt) (%s): rows are the hypotheses with their reading and the '
         'rows that decide them.' % utc(), '',
         '  H1 %s -- of the %d controls b671 read INSTRUMENT (data/b671_tie_diagnostic.txt :66-:88, :107-:129), %d read PASS in the angle form '
         'and %d do not (%s); each still failing read by the b671 rule: %s (data/b677_map.txt).' % (
             'HELD' if h1 else 'REFUTED', len(was), len(was) - len(still), len(still),
             ', '.join('%d bits j %d' % (x['bits'], x['j']) for x in still[:3]) + (' ...' if len(still) > 3 else ''),
             ', '.join('%s %d' % (w, sum(x['word'] == w for x in still)) for w in ('INSTRUMENT', 'OBJECT', 'NEITHER'))),
         '  H2 %s -- the residual radius at j = 64: %s against the bar %.3e; h_tol(64) %s against the banked width 1e-24 '
         '(data/b677_tolerance.txt).' % ('HELD' if h2 else 'REFUTED', ', '.join('%d bits %.3e' % (x['bits'], x['rad']) for x in q64), bar,
                                         ('%.3e' % tj['h_tol64']) if tj['h_tol64'] else 'NONE ON THE GRID'),
         '  H3 %s -- as data/b663_epstein_plan.txt :131 states it: the map reads %s; hQtie controls %s of %s%s (data/b677_map_run.txt).' % (
             'HELD' if h3 else 'REFUTED', q['reading'], (q.get('hqtie') or ['-', '-'])[0], (q.get('hqtie') or ['-', '-'])[1],
             '' if h1 else ' -- ON A FAILING INSTRUMENT: no object reading taken ((R287)(5))'),
         '  H4 %s -- as data/b667_epstein_plan.txt :124-:125 states it: %s' % (
             ('SCORABLE: ' + ('HELD' if zs['held'] and zs['j0'] == H4_J0 else 'REFUTED')) if zs else 'NOT SCORABLE',
             ('j₀ = %d, the zero side %s' % (zs['j0'], zs['zero_side'])) if zs else 'no j₀ read by the map (hQtie %s of %s), the plan`s own criterion' % tuple(q.get('hqtie') or ['-', '-'])),
         '  H5 %s -- P3 at j = 38 and 64 reads PASS at h_tol/3 and FAIL at 3·h_tol: %s; h_tol(38) %s beside b667`s %.0e, ratio %s '
         '(data/b677_tolerance.txt).' % ('HELD' if h5 else 'REFUTED', '; '.join(
             'j %s %s' % (j, ' / '.join(r['word'] for r in x['rows'].values()) if x.get('rows') else x.get('note')) for j, x in p3.items()),
             ('%.3e' % tj['h_tol38']) if tj['h_tol38'] else 'NONE', B667_TOL, ('%.3e' % (tj['h_tol38'] / B667_TOL)) if tj['h_tol38'] else '-'),
         '',
         '  THE LABELLED READING (the navigator`s answer on the run; an instrument-side row, not an object finding): %s -- %s%s' % (
             lab.get('note', 'not computed'), lab.get('reading'), ('; the zero side at j₀ = %d %s, %s' % (lab['zero_side']['j0'], lab['zero_side']['zero_side'],
                                                                                                       'BELOW 0' if lab['zero_side']['held'] else 'NOT BELOW 0'))
             if lab.get('zero_side') else ''),
         '  THE LOCATED FAILURE: the first failing j at Q0 %s; the price (plan section 6) the last passing j 47 (upper) to 56 (lower) and the '
         'radius at j = 64 %.1e to %.1e.' % (first_fail, PRICE['upper']['rad64'], PRICE['lower']['rad64']), '',
         '### ### **H1 %s ; H2 %s ; H3 %s ; H4 %s ; H5 %s.**' % ('HELD' if h1 else 'REFUTED', 'HELD' if h2 else 'REFUTED', 'HELD' if h3 else 'REFUTED',
                                                              ('SCORABLE' if zs else 'NOT SCORABLE'), 'HELD' if h5 else 'REFUTED')]
    _put('b677_map_h.txt', NL.join(L) + NL)
    _putj('b677_map_h.json', dict(at=utc(), H1=h1, H2=h2, H3=h3, H4=('SCORABLE' if zs else 'NOT SCORABLE'), H5=h5, first_fail=first_fail,
                                  still=[(x['bits'], x['j'], x['word']) for x in still], labelled=lab))
    print(NL.join(L))


# ================================================================================ THE DIFF AGAINST THE b667 MAP (N3 read on the text)
def diff(*a):
    old = io.open(B667_MAP, encoding='utf-8').read().split(NL)
    me = io.open(os.path.abspath(__file__), encoding='utf-8').read().split(NL)
    d = list(difflib.unified_diff(old, me, 'tools/b667_epstein_map_balls.py', 'tools/b677_epstein_map_angle.py', lineterm='', n=0))
    stars = [(i, l.strip()) for i, l in enumerate(me, 1) if '**' in l and not l.strip().startswith('#') and '"""' not in l and "'**" not in l]
    loops = [(i, l.strip()) for i, l in enumerate(me, 1) if re.search(r'\bp = p \* p\b|\[p \* p for', l) and 'repeated-squaring loops' not in l]
    L = ['b677 -- THE NEW TOOL`S DIFF AGAINST THE b667 MAP (data/b677_map_diff.txt) (%s): tools/b667_epstein_map_balls.py sha256 %s (left as it '
         'is) ; tools/b677_epstein_map_angle.py sha256 %s ; added %d, removed %d lines.' % (
             utc(), sha(B667_MAP), sha(os.path.abspath(__file__)), sum(1 for l in d if l.startswith('+') and not l.startswith('+++')),
             sum(1 for l in d if l.startswith('-') and not l.startswith('---'))), '',
         '### N3 READ ON THE TEXT: every `**` left in the new tool, each hand-read (exact integers and exact powers of two only):']
    L += ['  :%d %s' % (i, l[:150]) for i, l in stars] or ['  NONE']
    L += ['### the repeated-squaring loops (`p = p * p`, `[p * p for`) left: %s' % (loops or 'NONE'), '', '### THE DIFF, WHOLE:'] + d
    _put('b677_map_diff.txt', NL.join(L) + NL)
    print(NL.join(L[:len(stars) + 6]))


if __name__ == '__main__':
    fn = {'part1': part1, 'part2': part2, 'part3': part3, 'hyp': hyp, 'diff': diff}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b677_epstein_map_angle.py part1 | part2 | part3 | hyp | diff')
        sys.exit(2)
    fn(*sys.argv[2:])
