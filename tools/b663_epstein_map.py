# -*- coding: utf-8 -*-
"""b663_epstein_map.py -- THE RATE INDEX AND THE ZERO SIDE AT THE Q0 CONFIGURATION, BOUND TO zeroSide_neg_at_rate_cfg (SIDE-explicit-formula
v0.28, Schema/RateIndexCfg.lean :135-:148) AT q0Config (branch epstein-b663, Schema/EpsteinQ0.lean), under (R273)(4) and the author's word on
b663's plan (relay data/b663_epstein_plan.txt, section 8; data/b663_author_answers.txt).

### Carried by the Write tool from tools/b662_map.py; the changes confined to the plan's section 6: the configuration (the bench's list in
### place of ζ's, one cell at the base qE0 in place of the grid), M and hdom over all seventeen off-line orbits (M := the dominant's score),
### θ and the kill set over the other sixteen orbits and the points above T (on B1), hA's ordinates and A₀ (P3's A0Q), and the zero side
### (the other orbits' terms and the tail above T on B1 and P3). ghat, ramp_R, i4_ball, a0_upper, zero_list, the controls of hQtie and
### hQb, hrate and the rung are b662's lines unchanged; the diff is banked (relay data/b663_map_diff.txt).
### Every zero of Q0 is BANKED, NOT BALL-CERTIFIED (two agreeing routes in mpmath at 119 digits): each enters as its decimal literal, exact,
### the configuration's own point. B1 is a named READ premise of this computation, not a kernel lemma (the plan, section 8).
### THE CONTROL (the author's word on Q3): the same cell routine run first on b661's Z₁(0.8, 29.6) -- the orbit of 0.8 + 29.6 i and ζ's zeros
### to 1000 from Arb --, expected to reproduce j₀ = 31 and the zero side below 0 (relay data/b661_map_control.txt); printed beside the Q0 cell.
### Usage: `python tools/b663_epstein_map.py` -- banks data/b663_epstein_control.txt and .json. No lean; no kernel file read but by citation.
### Nothing here is about ζ: Z₁ is not ζ's configuration, and the Q0 configuration is Z_Q's only under its premises.
"""
import io
import json
import os
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
Q0_T = 150                                                 # ### the height cut, the banks' own T
Q0_BASE = 0                                                # ### qE0 = the off-line list's index 0, the dominant (data/b663_dominance.txt)
Q0_A0 = 10                                                 # ### A0Q, P3's constant (Schema/EpsteinQ0.lean; data/b663_a0_list.txt)
I4_DELTA0, I4_PIECES, I4_MINW_EXP = 300, 400, 120         # ### ∫|s''''|: the cut [0, 1/300] by a Cauchy bound; 400 pieces; bisection to 2^-120

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_DIR = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
OUT = []


def say(s=''):
    OUT.append(s)
    print(s, flush=True)


def b(x, n=12):
    return x.str(n, radius=True)


# ================================================================================ THE BASE: s, ĝ0, ∫|s''''|
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
    TwoPropertyWindow.lean :56-:57): g0 even, 1 on [-ℓ/2, ℓ/2], s(2(ℓ-|u|)/ℓ) on the ramps; = 2∫_0^ℓ g0 cos(zu) du = ℓ (2 sin(w/2)/w + R(w)),
    w = zℓ."""
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
    """I4 = ∫_0^1 |s''''| = 2 ∫_0^{1/2} |s''''| (s''''(1-x) = -s''''(x)). On [0, δ0] a Cauchy bound (radius x/2; increasing in x there);
    on [δ0, 1/2] pieces where s'''' keeps its sign contribute |s'''(b) - s'''(a)| exactly, pieces bisected to 2^-120 where it does not
    contribute at most their width times the ball's sup. Returns (lower, upper) of I4."""
    x = arb(1) / I4_DELTA0
    cb = x * 24 * 16 / x ** 4 * (-(arb(2) / (3 * x))).exp() / ((-1 / (1 - arb(1.5) * x)).exp() - (-(arb(2) / (3 * x))).exp())
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
    """the ball [lo, hi]."""
    return arb((lo + hi) / 2, ((hi - lo) / 2).upper())


# ================================================================================ THE ZERO LISTS: Z₁'s on-line part (the control), Q0's
def zero_list():
    """arb.zeta_nzeros(T) and acb.zeta_zeros(1, N(T)) (Platt's isolation with Turing's method): every zero a ball with real part 1/2; the
    N(T)-th below T and the next above it, or the map stops."""
    n = arb.zeta_nzeros(arb(T_HEIGHT))
    if not n.is_exact():
        sys.exit('### N(T) IS NOT EXACT AT T = %d -- THE MAP STOPS' % T_HEIGHT)
    n = int(n.unique_fmpz())
    zs = acb.zeta_zeros(1, n)
    nxt = acb.zeta_zero(n + 1)
    ok = all(z.real == arb(1) / 2 for z in zs) and zs[-1].imag < T_HEIGHT and nxt.imag > T_HEIGHT and len(zs) == n
    return n, [z.imag for z in zs], ok, zs[-1].imag, nxt.imag


def q0_list():
    """the bench's list (relay data/b326_epstein_zeros.json, data/b326_offline.json, key "zeros"): the ordinates gamma_a (= gamma_b) and
    the off-line zeros rho_a (= rho_b), each by index, each as its decimal literal (an exact arb of the double the bank holds); a row whose
    two routes disagree stops the map."""
    on = json.load(io.open(os.path.join(D_DIR, Q0_ON), encoding='utf-8'))['zeros']
    off = json.load(io.open(os.path.join(D_DIR, Q0_OFF), encoding='utf-8'))['zeros']
    if not all(z['agree'] and z['gamma_a'] == z['gamma_b'] for z in on) or not all(z['agree'] and z['rho_a'] == z['rho_b'] for z in off):
        sys.exit('### A BANKED ZERO WHOSE TWO ROUTES DISAGREE -- THE MAP STOPS')
    return [arb(repr(z['gamma_a'])) for z in on], [(repr(z['rho_a'][0]), repr(z['rho_a'][1])) for z in off]


# ================================================================================ hA: THE LOCAL COUNT, A FINITE MAXIMUM
def a0_upper(ords):
    """HCount (RestBound.lean :44-:45): 1 ≤ A₀ and Z.N s (s+1) ≤ A₀ log(|s| + 3) for every real s; Z.N s (s+1) counts Im in (s, s+1]
    (Defs.lean :162). N(s) ≤ N⁺(s) = #{y : y_lo - 1 ≤ s < y_hi} (an ordinate whose ball meets an edge counted on both sides); N⁺ is a step
    function between the sorted exact endpoints, and on each step 1/log(|s|+3) is largest at the step's point nearest 0. Returns
    (A₀ an exact upper value, the arg max s, the count there)."""
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


# ================================================================================ ONE CELL
def unit(x):
    return x / abs(x)


def orbit_of(sg, t):
    """the four points ρ, 1 − conj ρ, conj ρ, 1 − ρ of an off-line zero σ + it, as gammaOf ρ = (ρ - 1/2)/I (Defs.lean :121)."""
    dl = sg - arb(1) / 2
    return [('ρ', acb(t, -dl)), ('1 − conj ρ', acb(t, dl)), ('conj ρ', acb(-t, -dl)), ('1 − ρ', acb(-t, dl))]


def cell(name, base, online, offline, prec, i4, above=None, a0_premise=None, rung_note=None, jcap=J_EXTRA):
    """one configuration at one base: base = (σ, t) strings of the off-line zero whose detectorBase is g0; online = the ordinates (arb,
    positive); offline = the off-line zeros as (σ, t) strings; above = None (a finite configuration) or Q0_T (the points above it read on
    B1 and P3); a0_premise = None (A₀ from the list) or P3's constant."""
    ctx.prec = prec
    rec = dict(name=name, base=list(base), prec=prec, certs=[], hrate=[], unresolved=[], reading=None, triggers=[])
    sb, tb = arb(base[0]), arb(base[1])
    zb = acb(tb, -(sb - arb(1) / 2))
    ell = 1 / (4 * (abs(zb) + 1))                        # baseWidth ρb (Detector.lean :33)
    say('== CELL %s -- base %s + %s i -- %d bits%s' % (name, base[0], base[1], prec, (' -- ' + rung_note) if rung_note else ''))
    say('  ℓ = baseWidth ρb (Schema/Detector.lean :33) = 1/(4(‖γ(ρb)‖ + 1)) = %s ; L = ℓ (Detector.lean :113)' % b(ell))

    def fail(nm, why):
        rec['certs'].append((nm, 'NOT CERTIFIED', why))
        say('  %-9s NOT CERTIFIED -- %s' % (nm, why))
        rec['reading'] = 'HYP-UNVERIFIED(%s)' % nm
        return rec

    def ok(nm, why):
        rec['certs'].append((nm, 'CERTIFIED', why))
        say('  %-9s CERTIFIED -- %s' % (nm, why))

    # ### the setup H : PWSetup C.toZeroConfig g0 L M (PowerLimit.lean :245-:251)
    ok('H.hev', 'plateau_even (TwoPropertyWindow.lean :69), the term Detector.lean :114 passes; COMPILED')
    ok('H.hsm', 'plateau_contDiff (TwoPropertyWindow.lean :60), as Detector.lean :114; COMPILED')
    ok('H.hs', 'plateau_support_Icc, as Detector.lean :107-:108; COMPILED')
    ok('H.hL', 'baseWidth_pos (Detector.lean :35); 0 ≤ ℓ; COMPILED')
    # ### M := the dominant's score over every off-line orbit (the plan, section 6: :197-:210 changed)
    orbs = []
    for k, (ss, ts) in enumerate(offline):
        o = orbit_of(arb(ss), arb(ts))
        orbs.append((k, ss, ts, [(nm, z, ghat(z, ell, prec)) for nm, z in o]))
    top = max(orbs, key=lambda x: abs(x[3][0][2]).mid())
    M = abs(top[3][0][2])                                # offScore g0 ρ* (PowerWindow.lean :328), ρ* the dominant
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
        return fail('H.hdom', 'THE GUARD: an off-line point of another orbit does not lie below M (dominance not decided, or the point '
                    'killed): %s -- THE CELL STOPS' % over[:4])
    ok('H.hdom', 'the dominant`s four scores %s each meet M, equal by offScore_reflect (PowerLimit.lean :219) and paperFT_conj_of_real (:36); '
       'the other %d orbit(s), %d point(s), every score below M in balls (the largest %s)%s' % (
           ' ; '.join('%s %s' % (nm, b(x, 8)) for (nm, _z, _g), x in zip(gh, sc)), len(others), 4 * len(others),
           b(max((abs(g) for o in others for _n, _z, g in o[3]), key=lambda x: x.mid()), 8) if others else '-',
           '' if above is None else '; above T = %d by B1 (below)' % above))
    sd, tt = arb(top[1]), arb(top[2])
    dl = sd - arb(1) / 2
    t = tt
    v = (dl + acb(0, 1) * t) ** 2                       # vOf ρ* (PowerLimit.lean :146)
    if not (v.imag > 0 or v.imag < 0):
        return fail('tieSet', 'Im v = %s meets 0' % b(v.imag))
    ok('tieSet', 'tieSet C g0 M (PowerWindow.lean :398) = the dominant`s orbit, 4 points, mult 1; VF = {v, conj v} (:280), Im v = %s ≠ 0' % b(v.imag))
    # ### the kill set and θ, by the zeros in order of |γ|, the decay screen offScore ≤ Aw/(1 + ‖γ‖⁴) (PowerLimit.lean :825)
    aw = (arb(3) / 2 * ell + 16 * i4 / ell ** 3) * (ell / 2).exp()     # Aw (PowerLimit.lean :800) = (∫g0 + ∫|g0''''|) e^{L/2}
    rec['Aw'] = b(aw)
    zl = online
    killed, straddle, theta, targ, nread, nscreen = [], [], arb(0), None, 0, 0
    for k, gm in enumerate(zl):
        sb_ = aw.upper() / (1 + gm.lower() ** 4)
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
    # ### θ over the other off-line orbits (the plan, section 6: :219-:236 changed)
    for o in others:
        for _nm, _z, g in o[3]:
            r = arb((abs(g).upper() / M.lower()).upper())
            if r.upper() > theta.upper():
                theta, targ = r, 'off-line %s + %s i' % (o[1][:10], o[2][:10])
    # ### the points above T (Q0): B1, a named READ premise (the plan, section 8)
    b1 = None
    if above is not None:
        b1 = arb((2 * (ell / 2).exp() / (arb(above) * M.lower())).upper())
        h4 = ((aw / (theta * M) - 1).log() / 4).exp() if theta > 0 else None
        if b1.upper() > theta.upper():
            theta, targ = b1, 'B1 at |Im ρ| = %d' % above
        rec['B1'] = b(b1)
        say('  B1        the points of Z with |Im ρ| ≥ %d (unlisted; P2 lists every point below it): offScore g0 ρ / M ≤ 2 e^{ℓ/2}/(%d M) = %s ; '
            'certified on B1 (READ), not a kernel lemma -- the kernel`s fourth-order bound (zero_weight`s hsA, PowerLimit.lean :825) clears '
            'only above %s, the banks reach %d' % (above, above, b(b1, 10), b(h4, 8) if h4 is not None else '-', above))
    rec['theta_at'] = str(targ)
    xr = [-(gm ** 2) for gm in killed]                    # Xr (PowerLimit.lean :268), one per |γ|
    ok('killSet', 'killSet C g0 M (PowerWindow.lean :401): zeros read %d, killed %d%s, screened by the decay bound %d, straddling 0; '
       'off-line points killed 0 (the guard); card Xr = %d' % (nread, len(killed), (' (γ ≤ %s)' % b(killed[-1], 10)) if killed else '', nscreen, len(xr)))
    # ### hA (the plan, section 6: :241 changed -- every listed ordinate; A₀ from P3 where it is given)
    ords = [x for gm in zl for x in (gm, -gm)] + [x for o in orbs for x in (arb(o[2]), arb(o[2]), -arb(o[2]), -arb(o[2]))]
    a0l, sarg, scnt = a0_upper(ords)
    if a0_premise is None:
        a0 = a0l
        ok('hA', 'HCount C.toZeroConfig A₀ (RestBound.lean :44-:45): A₀ = %s (an exact upper value; the steps of N(s, s+1] read at their '
           'points nearest 0, the largest ratio at s = %s, count %d; 1 ≤ A₀)' % (a0.str(15, radius=False), b(sarg, 10) if sarg is not None else '-', scnt))
    else:
        a0 = arb(a0_premise)
        if not a0l.upper() <= a0.lower():
            return fail('hA', 'the listed points` own A₀ %s exceeds P3`s A0Q = %s' % (a0l.str(15, radius=False), a0_premise))
        ok('hA', 'HCount C.toZeroConfig A0Q BY P3 (Q0Count, a named premise, stated, not proved; open), A0Q = %s; the listed points` own '
           'A₀ = %s ≤ A0Q (relay data/b663_a0_list.txt)' % (a0_premise, a0l.str(15, radius=False)))
    # ### D, B, CV (coeffs_exist's witness, PowerLimit.lean :683)
    D = 2 * len(xr) + 8
    jmax = D + jcap
    cE = 1 + 4 / abs(dl)                                 # cE (PowerLimit.lean :274)
    cv = 2 * (abs(v) + 1) / abs(v - v.conjugate())       # CV (PowerWindow.lean :432) at the two nodes
    bk = (len(xr) + 1) * _prod([1 + gm ** 2 for gm in killed])   # BK = (natDegree Kp + 1) Σ|coeff Kp| (:667), Kp = ∏(X + γ²)
    be = 2 * (1 + cE)                                    # BE = (natDegree Ep + 1) Σ|coeff Ep|, Ep = 1 + cE X (:277)
    B = 2 * cv * bk * be                                 # B = card VF · max CV 0 · BK · BE
    say('  D = 2 card VF + 2 DK + DE = 2·card Xr + 8 = %d ; J_max = D + %d = %d ; cE = %s ; CV = %s ; BK = %s ; BE = %s ; B = %s' % (
        D, jcap, jmax, b(cE, 10), b(cv, 10), b(bk, 10), b(be, 10), b(B, 10)))
    rec.update(D=D, J_max=jmax, card_Xr=len(xr), A0=a0.str(15, radius=False), B=b(B), theta=b(theta))

    def kp(w):
        return _prod([w - x for x in xr]) if xr else acb(1)

    def F(w):
        return kp(w) ** 2 * (1 - cE ** 2 * w)

    # ### the controls of hQtie and hQb at j in [D, J_max]: Q j = a + b X interpolating rT H j on {v, conj v}
    us = [unit(g) for _nm, _z, g in gh]
    nodes = [v, v.conjugate(), v.conjugate(), v]               # vOf at ρ₁, 1 − conj ρ₁, conj ρ₁, 1 − ρ₁
    pw = list(us)
    for _ in range(D + 1):
        pw = [p * p for p in pw]
    Qs, nt, nb = {}, 0, 0
    for j in range(D, jmax + 1):
        if j > D:
            pw = [p * p for p in pw]
        ph = [unit(F(nd)) * p for nd, p in zip(nodes, pw)]        # Xval/|Xval| at each tie point (PowerLimit.lean :437-:439)
        yv = -ph[0].conjugate()                                     # Yv (:560)
        r1, r2 = yv.sqrt(), acb(0, 1) * (-yv).sqrt()
        r = r1 if r1.rad() <= r2.rad() else r2                       # rT (:591-:592) up to sign; Q² and the window unchanged
        bq = r.imag / v.imag
        aq = r.real - bq * v.real
        Qs[j] = (aq, bq)
        res = [(acb(aq) + bq * nd) ** 2 * p + 1 for nd, p in zip(nodes, ph)]
        if all(x.real.contains(0) and x.imag.contains(0) and x.rad() < arb(2) ** -20 for x in res):
            nt += 1
        if abs(aq).upper() <= cv.lower() and abs(bq).upper() <= cv.lower():
            nb += 1
    k = jmax - D + 1
    if nt < k:
        return fail('hQtie', 'by coeffs_exist, inputs certified; controls %d of %d -- a tie residual ball not resolved at 0' % (nt, k))
    ok('hQtie', 'by coeffs_exist (PowerLimit.lean :686-:704), inputs certified; controls %d of %d' % (nt, k))
    if nb < k:
        return fail('hQb', 'by coeffs_exist, inputs certified; controls %d of %d -- |a_j| or |b_j| not below CV' % (nb, k))
    ok('hQb', 'by coeffs_exist (PowerLimit.lean :705-:731), inputs certified; controls %d of %d' % (nb, k))
    ok('hθ0', 'θ = %s ≥ 0' % theta.str(15, radius=False))
    ok('hθ', 'every point outside the tie and kill sets read or screened: offScore/M ≤ θ%s%s' % (
        (' (the largest at %s)' % (b(targ, 10) if isinstance(targ, arb) else targ)) if targ is not None else ' (none read outside the kill set)',
        '' if above is None else '; the points above T certified on B1 (READ), not a kernel lemma'))
    # ### hrate (RateIndexCfg.lean :145-:147), both sides on a logarithmic scale
    z3 = 2 * arb(3).zeta() - 1                           # zeta3Sum (RestBound.lean :51)
    rhs = sum((abs(F(nd)) for nd in nodes), arb(0))      # Σ_{x ∈ sT_cfg H} mult x · Nf H x (Nf :445)
    if not rhs > 0:
        return fail('hrate', 'the right side %s meets 0 (UNDERFLOW)' % b(rhs))
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
                rec['triggers'].append('hrate OVERFLOW at j = %d' % j)
                st = 'OVERLAP'
            elif ll.upper() < lr.lower():
                st = 'HOLDS'
            elif ll.lower() > lr.upper():
                st = 'FAILS'
            else:
                st = 'OVERLAP'
            sides = 'left exp(%s) ; right exp(%s) = %s' % (b(ll, 15), b(lr, 15), b(rhs, 10))
        rec['hrate'].append((j, st, sides))
        say('    hrate j = %-3d %-7s %s' % (j, st, sides))
        if st == 'OVERLAP':
            rec['unresolved'].append(j)
        if st == 'HOLDS' and j0 is None:
            j0 = j
            break
    if j0 is not None:
        rec['reading'] = 'j₀ = %d' % j0
        rec['j0'] = j0
    else:
        rec['reading'] = 'NONE ≤ J_max'
    rec['sides'] = rec['hrate'][-1][2]
    # ### the zero side at j₀ (the plan, section 6: :351-:388 changed -- the other orbits' terms; the tail above T on B1 and P3)
    if j0 is not None:
        rec['zero_side'] = zero_side(j0, Qs[j0], kp, F, gh, others, M, zl, killed, nread, aw, ell, prec, cE, a0, above, b1)
    return rec


def _prod(xs):
    p = arb(1) if not xs or isinstance(xs[0], arb) else acb(1)
    for x in xs:
        p = p * x
    return p


def zero_side(j0, Q, kp, F, gh, others, M, zl, killed, nread, aw, ell, prec, cE, a0, above, b1):
    """(zeroSide_cfg C (kWindow (coeffList (Pof H (Q j₀))) g0 j₀)).re, each term by term_eq (PowerLimit.lean :736), (Q j₀)(vOf ρ)² ·
    Xval H j₀ ρ, divided by M^(2^(j₀+1)) (the sign unchanged): the dominant's four orbit terms and every other off-line orbit's four from
    their own balls; a killed zero's term 0 (kill_term_zero :756); a read zero's term in balls; a screened zero's term in [0, its decay
    bound's term]; and, above T (Q0), every unlisted point's term bounded on B1 and P3: |term| ≤ |Q(v)|² |F(v)| B1^(2^(j₀+1)) with
    |v| ≤ (|Im ρ| + 1/2)², the points in (n, n+1] at most A0Q log(n + 4) on each side by P3, summed for n ≥ 149 (the n = 149 window holds
    only points at |Im ρ| = 150) through Σ_{n ≥ 150} n^(K - E) ≤ 150^(K - E) (1 + 150/(E - K - 1))."""
    aq, bq = Q
    E = 2 ** (j0 + 1)
    tot = acb(0)
    for _nm, z, g in gh:
        vv = (acb(0, 1) * z) ** 2                         # vOf ρ = (ρ - 1/2)² = (i γ(ρ))²
        q = acb(aq) + bq * vv
        p = g / M
        for _ in range(j0 + 1):
            p = p * p
        tot += q ** 2 * F(vv) * p
    oth = acb(0)
    for o in others:
        for _nm, z, g in o[3]:
            vv = (acb(0, 1) * z) ** 2
            q = acb(aq) + bq * vv
            p = g / M
            for _ in range(j0 + 1):
                p = p * p
            oth += q ** 2 * F(vv) * p
    on = arb(0)
    kset = set(id(x) for x in killed)
    for k, gm in enumerate(zl):
        if id(gm) in kset:
            continue
        vv = acb(-(gm ** 2))
        q = acb(aq) + bq * vv
        fac = (q ** 2 * F(vv)).real
        if k < nread:
            rr = abs(ghat(acb(gm), ell, prec)) / M
        else:
            rr = arb(0, (aw.upper() / (1 + gm.lower() ** 4) / M.lower()).upper())
        p = rr
        for _ in range(j0 + 1):
            p = p * p
        term = 2 * fac * p                                 # ±γ
        on = on + (term if k < nread else arb(term.upper() / 2, term.upper() / 2))
    tail = arb(0)
    if above is not None:
        K = 7 + 4 * len(killed)
        c0 = 2 * arb(a0) * (abs(acb(aq)) + abs(bq)) ** 2 * _prod([(1 + gm ** 2) ** 2 for gm in killed]) * (1 + cE ** 2) * arb('1.0201') ** (3 + 2 * len(killed))
        bnd =c0 * (arb(above) ** K) * (E * b1.log()).exp() * (2 + arb(above) / (E - K - 1))
        tail = arb(0, bnd.upper())
        say('  the points above T = %d: |Σ terms| ≤ %s, on B1 (READ) and P3 (A0Q = %s) -- K = %d, B1 = %s, E = 2^(j₀+1) = 2^%d' % (
            above, b(arb(bnd.upper()), 6), a0.str(5, radius=False), K, b(b1, 8), j0 + 1))
    zs = tot.real + oth.real + on + tail
    held = bool(zs < 0)
    say('  THE ZERO SIDE at j₀ = %d: (zeroSide_cfg C (kWindow …) g0 j₀).re / M^(2^(j₀+1)) = %s -- the dominant`s orbit %s, the other off-line '
        'orbits %s, the on-line terms %s, the points above T %s ; the ball %s 0' % (j0, b(zs, 15), b(tot.real, 15), b(oth.real, 15), b(on, 15),
                                                                           b(tail, 6), 'BELOW' if held else 'NOT BELOW'))
    return dict(j0=j0, zero_side=b(zs, 20), orbit=b(tot.real, 20), others=b(oth.real, 20), online=b(on, 20), above=b(tail, 8), held=held)


# ================================================================================ THE CONTROL AND THE Q0 CELL
def run_cell(name, base, online, offline, i4s, zls_rung, above=None, a0_premise=None):
    r = cell(name, base, online, offline, PREC, i4s[PREC], above=above, a0_premise=a0_premise)
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
        r2 = cell(name, base, online2, offline, PREC_RUNG, i4s[PREC_RUNG], above=above, a0_premise=a0_premise, rung_note='the rung, re-read once')
        r2['first'] = dict(reading=r['reading'], triggers=trig)
        r = r2
    if r['reading'].startswith('j₀') and r['unresolved']:
        r['reading'] += ' (UNRESOLVED-AT-j %s beside it: the true j₀ may be lower)' % ', '.join(str(j) for j in r['unresolved'])
    say('  READING %s: %s%s' % (name, r['reading'], ('  ### ' + r['sides']) if not r['reading'].startswith('HYP') else ''))
    say('')
    return r


def main():
    t0 = time.time()
    say('b663 -- THE RATE INDEX AND THE ZERO SIDE AT THE Q0 CONFIGURATION, BOUND TO zeroSide_neg_at_rate_cfg AT q0Config, UNDER (R273)(4) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    say('')
    say('### the kernel: SIDE-explicit-formula v0.28 = main ffbc617, Schema/RateIndexCfg.lean :135-:148; the instance on branch epstein-b663,')
    say('### Schema/EpsteinQ0.lean (q0Config, q0_rate, q0_hA); the plan relay data/b663_epstein_plan.txt (section 8, the author`s word). Rows are')
    say('### cells: the control Z₁(%s, %s) first, then Q0 at the base qE0. python-flint %s ; Arb balls at %d bits, the rung %d ; J_max = D + %d.' % (
        Z1_CELL[0], Z1_CELL[1], __import__('flint').__version__, PREC, PREC_RUNG, J_EXTRA))
    say('### Q0`s zeros BANKED, NOT BALL-CERTIFIED; B1 a named READ premise, not a kernel lemma; A₀ by P3. Nothing here is about ζ.')
    say('')
    ctx.prec = PREC
    lo, hi = i4_ball()
    i4s = {PREC: span(lo, hi)}
    say("### ∫_0^1 |s''''| at %d bits (Aw`s fourth-derivative part, PowerLimit.lean :800): I4 = %s" % (PREC, b(i4s[PREC], 20)))
    # ### THE CONTROL: b661's Z₁(0.8, 29.6)
    n, zl, okz, last, nxt = zero_list()
    say('### THE CONTROL`S ZERO LIST at %d bits: N(%d) = %d by arb.zeta_nzeros ; acb.zeta_zeros(1, %d), every real part 1/2 ; %s' % (
        PREC, T_HEIGHT, n, n, 'MATCHED' if okz else 'NOT MATCHED -- THE CONTROL STOPS'))
    if not okz:
        sys.exit(2)

    def zl_rung():
        ctx.prec = PREC_RUNG
        n2, z2, ok2, _l, _n = zero_list()
        if not ok2 or n2 != n:
            sys.exit('### THE ZERO LIST AT %d BITS DOES NOT MATCH -- THE MAP STOPS' % PREC_RUNG)
        return z2
    say('')
    rc = run_cell('THE CONTROL Z₁(%s, %s)' % Z1_CELL, Z1_CELL, zl, [Z1_CELL], i4s, zl_rung)
    zc = rc.get('zero_side')
    c_ok = rc.get('j0') == 31 and zc is not None and zc['held']
    say('  ### THE CONTROL %s -- expected j₀ = 31 and the zero side below 0 (relay data/b661_map_control.txt); read j₀ = %s, the zero side %s' % (
        'REPRODUCED' if c_ok else 'NOT REPRODUCED', rc.get('j0'), ('BELOW 0' if zc['held'] else 'NOT BELOW 0') if zc else 'not read'))
    say('')
    # ### Q0
    ctx.prec = PREC
    on, off = q0_list()
    say('### THE Q0 LIST: relay data/%s, %d ordinates (index 0-%d); relay data/%s, %d off-line zeros (index 0-%d); the base qE0 = index %d = %s + %s i ; '
        'T = %d ; A0Q = %d' % (Q0_ON, len(on), len(on) - 1, Q0_OFF, len(off), len(off) - 1, Q0_BASE, off[Q0_BASE][0], off[Q0_BASE][1], Q0_T, Q0_A0))
    say('')
    rq = run_cell('Q0 AT qE0', off[Q0_BASE], on, off, i4s, None, above=Q0_T, a0_premise=Q0_A0)
    score(rc, c_ok, rq)
    say('### elapsed %d s' % int(time.time() - t0))
    put([rc, rq])


def score(rc, c_ok, rq):
    """H3 and H4 by printed line; H1 and H2 read from the instance bank (relay data/b663_epstein_instance.txt) where it stands."""
    ib = os.path.join(D_DIR, 'b663_epstein_instance.txt')
    inst = io.open(ib, encoding='utf-8').read() if os.path.exists(ib) else ''
    say('### ### **THE HYPOTHESES OF (R273)(4):**')
    for h in ('H1', 'H2'):
        ln = [l for l in inst.split(NL) if l.startswith('  %s ' % h)]
        say('  %s %s' % (h, ln[0][5:] if ln else 'read at Component 3 from relay data/b663_epstein_instance.txt (not in this bank)'))
    certs = [c[0] for c in rq['certs'] if c[1] == 'CERTIFIED']
    h3 = rq['reading'].startswith('j₀') and 'j0' in rq and rq['j0'] <= rq['J_max']
    say('  H3 %s -- at Q0 every hypothesis of zeroSide_neg_at_rate_cfg certified by name (%s)%s and hrate %s' % (
        'HELD ON B1' if h3 else 'REFUTED', ', '.join(certs), '; hθ above T on B1 (READ)', ('holds at j₀ = %d ≤ D + %d = %d' % (rq['j0'], J_EXTRA, rq['J_max']))
        if h3 else 'reads %s' % rq['reading']))
    zs = rq.get('zero_side')
    if zs is None:
        say('  H4 NOT SCORABLE -- no j₀ at Q0')
    else:
        say('  H4 %s -- the zero side at j₀ = %d: %s' % ('HELD ON B1' if zs['held'] else ('REFUTED, H3 HELD -- THE ACT`S FINDING' if h3 else 'REFUTED'),
                                                    zs['j0'], zs['zero_side']))
    say('  THE CONTROL %s' % ('REPRODUCED (j₀ = 31, the zero side below 0)' if c_ok else 'NOT REPRODUCED'))


def put(recs, name='b663_epstein_control'):
    tx = (NL.join(OUT) + NL).encode('utf-8')
    p = os.path.join(D_DIR, name + '.txt')
    open(p + '.tmp', 'wb').write(tx)
    os.replace(p + '.tmp', p)
    js = (json.dumps(dict(cells=recs), indent=1, ensure_ascii=False, default=str) + NL).encode('utf-8')
    p = os.path.join(D_DIR, name + '.json')
    open(p + '.tmp', 'wb').write(js)
    os.replace(p + '.tmp', p)


if __name__ == '__main__':
    main()
