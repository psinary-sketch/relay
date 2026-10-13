# -*- coding: utf-8 -*-
"""b662_map.py -- THE DETECTION-INDEX MAP AT Z₁, BOUND TO zeroSide_neg_at_rate_cfg (SIDE-explicit-formula v0.28, Schema/RateIndexCfg.lean
:135-:148), under (R271)(4)-(5) and the author's word (relay data/b661_author_answers.txt).

### Written whole by the Write tool at b661. The binding is relay data/b661_e1cfg_binding.txt; every quantity below names its kernel line.
### Per cell, every hypothesis of the theorem other than hrate is certified BY NAME AND ITS OWN BALL before any index prints; the readings
### are the three words of (R271)(4) and nothing else: `j₀ = <j>` (with any UNRESOLVED-AT-j beside it), `NONE ≤ J_max`, `HYP-UNVERIFIED(<name>)`.
### The rung (the author's word, set at b661, b627 having run at 200 bits throughout): a cell that does not certify a hypothesis, or meets an
### overlap of hrate's two balls, is re-read ONCE in full at PREC_RUNG; the 200-bit triggers are printed beside the cell; the re-read stands.
### The map states what the compiled theorem says of Z₁ and nothing of ζ: Z₁ is not ζ's configuration.
### Usage: `python tools/b662_map.py` -- banks data/b662_detection_map_40.txt and .json. No lean; no kernel file read but by citation.
### b662, (R272)(3) and the author's word (relay data/b662_author_answers.txt): tools/b661_map.py carried by the Write tool unchanged but for
### the constant J_EXTRA (8 -> 40), the bank's name and the act in its title line and in this docstring; the difference printed and banked.
"""
import io
import json
import os
import sys
import time

from flint import arb, acb, arb_series, ctx

# ================================================================================ THE CONSTANTS, AT THE HEAD ((R271)(4), the ferry)
GRID_SIGMA = ('0.55', '0.6', '0.7', '0.8', '0.9')          # ### (R266)(4), carried by (R271)(4)
GRID_T = ('14.1', '29.6', '50.0', '100.0')
T_HEIGHT = 1000                                            # ### Z₁'s height, b656's binding (relay data/b656_e1_binding.txt :27)
PREC = 200                                                 # ### Arb balls at 200 bits (relay data/b627_margin_inputs.txt :7)
PREC_RUNG = 400                                            # ### the one rung, 200 -> 400 bits, re-read once (the author's word at b661)
J_EXTRA = 40                                               # ### J_max = D + 40 per cell ((R272)(3) and the author's word at b662)
H3_CELL = ('0.8', '29.6')                                  # ### (R271)(5) H3
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


# ================================================================================ THE ZERO LIST (Z₁'s on-line part, its definition)
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


# ================================================================================ hA: THE LOCAL COUNT AT Z₁, A FINITE MAXIMUM
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


def cell(sig, tt, prec, zl, i4, rung_note=None, jcap=J_EXTRA):
    ctx.prec = prec
    rec = dict(sigma=sig, t=tt, prec=prec, certs=[], hrate=[], unresolved=[], reading=None, triggers=[])
    sg, t = arb(sig), arb(tt)
    dl = sg - arb(1) / 2
    rho1 = acb(sg, t)
    z1 = acb(t, -dl)                                     # gammaOf ρ₁ = (ρ₁ - 1/2)/I (Defs.lean :121)
    ell = 1 / (4 * (abs(z1) + 1))                        # baseWidth ρ₁ (Detector.lean :33)
    say('== CELL (σ, t) = (%s, %s) -- %d bits%s' % (sig, tt, prec, (' -- ' + rung_note) if rung_note else ''))
    say('  ℓ = baseWidth ρ₁ (Schema/Detector.lean :33) = 1/(4(‖γ(ρ₁)‖ + 1)) = %s ; L = ℓ (Detector.lean :113)' % b(ell))

    def fail(name, why):
        rec['certs'].append((name, 'NOT CERTIFIED', why))
        say('  %-9s NOT CERTIFIED -- %s' % (name, why))
        rec['reading'] = 'HYP-UNVERIFIED(%s)' % name
        return rec

    def ok(name, why):
        rec['certs'].append((name, 'CERTIFIED', why))
        say('  %-9s CERTIFIED -- %s' % (name, why))

    # ### the setup H : PWSetup C.toZeroConfig g0 L M (PowerLimit.lean :245-:251)
    ok('H.hev', 'plateau_even (TwoPropertyWindow.lean :69), the term Detector.lean :114 passes; COMPILED')
    ok('H.hsm', 'plateau_contDiff (TwoPropertyWindow.lean :60), as Detector.lean :114; COMPILED')
    ok('H.hs', 'plateau_support_Icc, as Detector.lean :107-:108; COMPILED')
    ok('H.hL', 'baseWidth_pos (Detector.lean :35); 0 ≤ ℓ; COMPILED')
    orbit = [('ρ₁', z1), ('1 − conj ρ₁', acb(t, dl)), ('conj ρ₁', acb(-t, -dl)), ('1 − ρ₁', acb(-t, dl))]
    gh = [(nm, z, ghat(z, ell, prec)) for nm, z in orbit]
    M = abs(gh[0][2])                                    # offScore g0 ρ₁ (PowerWindow.lean :328)
    rec['M'] = b(M)
    if not M.is_finite():
        return fail('H.hM', 'M = %s OVERFLOW' % b(M))
    if not M > 0:
        return fail('H.hM', 'M = %s, the ball meets 0 (UNDERFLOW)' % b(M))
    ok('H.hM', 'M = offScore g0 ρ₁ = |ĝ0(γ(ρ₁))| = %s > 0' % b(M))
    sc = [abs(g) for _nm, _z, g in gh]
    if not all(x.overlaps(M) for x in sc):
        return fail('H.hdom', 'an orbit score does not meet M: %s' % ' '.join(b(x, 8) for x in sc))
    ok('H.hdom', 'the off-line points of Z₁ are the orbit alone (the zero list on the line); the four scores %s each meet M, equal by '
       'offScore_reflect (PowerLimit.lean :219) and paperFT_conj_of_real (:36)' % ' ; '.join('%s %s' % (nm, b(x, 8)) for (nm, _z, _g), x in zip(gh, sc)))
    v = (dl + acb(0, 1) * t) ** 2                       # vOf ρ₁ (PowerLimit.lean :146)
    if not (v.imag > 0 or v.imag < 0):
        return fail('tieSet', 'Im v = %s meets 0' % b(v.imag))
    ok('tieSet', 'tieSet C g0 M (PowerWindow.lean :398) = the orbit, 4 points, mult 1; VF = {v, conj v} (:280), Im v = %s ≠ 0' % b(v.imag))
    # ### the kill set and θ, by the zeros in order of |γ|, the decay screen offScore ≤ Aw/(1 + ‖γ‖⁴) (PowerLimit.lean :825)
    aw = (arb(3) / 2 * ell + 16 * i4 / ell ** 3) * (ell / 2).exp()     # Aw (PowerLimit.lean :800) = (∫g0 + ∫|g0''''|) e^{L/2}
    rec['Aw'] = b(aw)
    killed, straddle, theta, targ, nread, nscreen = [], [], arb(0), None, 0, 0
    for k, gm in enumerate(zl):
        sb = aw.upper() / (1 + gm.lower() ** 4)
        if sb < M.lower() and (sb / M.lower()).upper() <= theta.upper() and theta > 0:
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
    xr = [-(gm ** 2) for gm in killed]                    # Xr (PowerLimit.lean :268), one per |γ|
    ok('killSet', 'killSet C g0 M (PowerWindow.lean :401): zeros read %d, killed %d%s, screened by the decay bound %d, straddling 0; '
       'card Xr = %d' % (nread, len(killed), (' (γ ≤ %s)' % b(killed[-1], 10)) if killed else '', nscreen, len(xr)))
    # ### hA
    ords = [x for gm in zl for x in (gm, -gm)] + [t, t, -t, -t]
    a0, sarg, scnt = a0_upper(ords)
    ok('hA', 'HCount C.toZeroConfig A₀ (RestBound.lean :44-:45): A₀ = %s (an exact upper value; the steps of N(s, s+1] read at their '
       'points nearest 0, the largest ratio at s = %s, count %d; 1 ≤ A₀)' % (a0.str(15, radius=False), b(sarg, 10) if sarg is not None else '-', scnt))
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
    ok('hθ', 'every on-line point outside the kill set read or screened: offScore/M ≤ θ%s' % (
        (' (the largest at γ = %s)' % b(targ, 10)) if targ is not None else ' (none read outside the kill set)'))
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
    # ### H3's control at its cell
    if (sig, tt) == H3_CELL and j0 is not None:
        rec['H3'] = h3(j0, Qs[j0], kp, F, gh, M, zl, killed, nread, aw, ell, prec)
    rec['_ctx'] = dict(Qs=Qs)
    return rec


def _prod(xs):
    p = arb(1) if not xs or isinstance(xs[0], arb) else acb(1)
    for x in xs:
        p = p * x
    return p


def h3(j0, Q, kp, F, gh, M, zl, killed, nread, aw, ell, prec):
    """(R271)(5) H3: (zeroSide_cfg Z₁ (kWindow (coeffList (Pof H (Q j₀))) g0 j₀)).re, each term by term_eq (PowerLimit.lean :736),
    (Q j₀)(vOf ρ)² · Xval H j₀ ρ, divided by M^(2^(j₀+1)) (the sign unchanged): the four orbit terms from their own balls; a killed zero's
    term 0 (its vOf a root of Kp by the definition of Xr, kill_term_zero :756); a read zero's term in balls; a screened zero's term in
    [0, its decay bound's term] (every on-line term is a square times a positive real)."""
    aq, bq = Q
    n = 2 ** (j0 + 1)
    tot = acb(0)
    for _nm, z, g in gh:
        vv = (acb(0, 1) * z) ** 2                         # vOf ρ = (ρ - 1/2)² = (i γ(ρ))²
        q = acb(aq) + bq * vv
        rr = g / M
        p = rr
        for _ in range(j0 + 1):
            p = p * p
        tot += q ** 2 * F(vv) * p
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
    zs = tot.real + on
    held = bool(zs < 0)
    say('  H3 at (%s, %s), j₀ = %d: (zeroSide_cfg Z₁ (kWindow …) g0 j₀).re / M^(2^(j₀+1)) = %s -- the orbit %s, the on-line terms %s ; '
        'the ball %s 0' % (H3_CELL[0], H3_CELL[1], j0, b(zs, 15), b(tot.real, 15), b(on, 15), 'BELOW' if held else 'NOT BELOW'))
    return dict(j0=j0, zero_side=b(zs, 20), orbit=b(tot.real, 20), online=b(on, 20), held=held)


# ================================================================================ THE MAP
def main():
    t0 = time.time()
    say('b662 -- THE DETECTION-INDEX MAP AT Z₁ BOUND TO zeroSide_neg_at_rate_cfg, AT J_max = D + 40, UNDER (R271)(4)-(5) AND (R272)(3) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    say('')
    say('### the kernel: SIDE-explicit-formula v0.28 = main ffbc617, Schema/RateIndexCfg.lean :135-:148; the binding relay data/b661_e1cfg_binding.txt;')
    say('### the author`s word relay data/b661_author_answers.txt. Rows are cells (σ, t); per cell the hypotheses by name, then hrate by j, then')
    say('### the reading. python-flint %s ; Arb balls at %d bits, the rung %d ; T = %d ; J_max = D + %d.' % (__import__('flint').__version__, PREC, PREC_RUNG, T_HEIGHT, J_EXTRA))
    say('### The map states what the compiled theorem says of Z₁ and nothing of ζ: Z₁ is not ζ`s configuration.')
    say('')
    zls, i4s, recs = {}, {}, []
    for prec in (PREC,):
        ctx.prec = prec
        n, zl, okz, last, nxt = zero_list()
        say('### THE ZERO LIST at %d bits: N(%d) = %d by arb.zeta_nzeros ; acb.zeta_zeros(1, %d), every real part 1/2 ; the %d-th %s < T < the next %s ; %s' % (
            prec, T_HEIGHT, n, n, n, b(last, 12), b(nxt, 12), 'MATCHED' if okz else 'NOT MATCHED -- THE MAP STOPS'))
        if not okz:
            sys.exit(2)
        zls[prec] = zl
        lo, hi = i4_ball()
        i4s[prec] = span(lo, hi)
        say("### ∫_0^1 |s''''| at %d bits (Aw`s fourth-derivative part, PowerLimit.lean :800, = 16 I4 / ℓ³ over both ramps): I4 = %s" % (prec, b(i4s[prec], 20)))
    say('')
    for tt in GRID_T:
        for sig in GRID_SIGMA:
            r = cell(sig, tt, PREC, zls[PREC], i4s[PREC])
            trig = []
            if r['reading'].startswith('HYP-UNVERIFIED'):
                trig.append(r['reading'])
            if r['unresolved']:
                trig.append('hrate overlap at j = %s' % r['unresolved'])
            trig += r['triggers']
            if trig:
                if PREC_RUNG not in zls:
                    ctx.prec = PREC_RUNG
                    n2, zl2, ok2, _l, _n = zero_list()
                    if not ok2 or n2 != len(zls[PREC]):
                        sys.exit('### THE ZERO LIST AT %d BITS DOES NOT MATCH -- THE MAP STOPS' % PREC_RUNG)
                    zls[PREC_RUNG] = zl2
                    lo, hi = i4_ball()
                    i4s[PREC_RUNG] = span(lo, hi)
                    say('### the rung: the zero list re-read at %d bits, N(T) = %d MATCHED ; I4 = %s' % (PREC_RUNG, n2, b(i4s[PREC_RUNG], 20)))
                say('  ### the 200-bit reading %s ; triggers: %s -- RE-READ ONCE AT %d BITS:' % (r['reading'], '; '.join(trig), PREC_RUNG))
                r2 = cell(sig, tt, PREC_RUNG, zls[PREC_RUNG], i4s[PREC_RUNG], rung_note='the rung, re-read once')
                r2['first'] = dict(reading=r['reading'], triggers=trig)
                r = r2
            if r['reading'].startswith('j₀') and r['unresolved']:
                r['reading'] += ' (UNRESOLVED-AT-j %s beside it: the true j₀ may be lower)' % ', '.join(str(j) for j in r['unresolved'])
            elif r['unresolved']:
                r['reading_beside'] = 'UNRESOLVED-AT-j %s' % ', '.join(str(j) for j in r['unresolved'])
            say('  READING (%s, %s): %s%s%s' % (sig, tt, r['reading'], ('  ### ' + r['sides']) if not r['reading'].startswith('HYP') else '',
                                              ('  ### ' + r['reading_beside']) if r.get('reading_beside') else ''))
            say('')
            r.pop('_ctx', None)
            recs.append(r)
    score(recs)
    say('### elapsed %d s' % int(time.time() - t0))
    put(recs)


def score(recs):
    forms = [r['reading'].split(' ')[0] for r in recs]
    one = all(r['reading'].startswith(('j₀ = ', 'NONE ≤ J_max', 'HYP-UNVERIFIED(')) for r in recs)
    c = len(recs)
    ni = sum(1 for r in recs if r['reading'].startswith('j₀'))
    nn = sum(1 for r in recs if r['reading'].startswith('NONE'))
    nu = sum(1 for r in recs if r['reading'].startswith('HYP'))
    say('### ### **CELLS %d: %d WITH AN INDEX, %d NONE ≤ J_max, %d HYP-UNVERIFIED.**' % (c, ni, nn, nu))
    say('  H1 %s -- every cell prints exactly one of j₀, NONE ≤ J_max, HYP-UNVERIFIED(<name>): %d of %d' % (
        'HELD' if one else 'REFUTED', sum(1 for r in recs if r['reading'].startswith(('j₀ = ', 'NONE ≤ J_max', 'HYP-UNVERIFIED('))), c))
    bad, pairs = [], 0
    for tt in GRID_T:
        row = [(arb(r['sigma']), r['j0']) for r in recs if r['t'] == tt and 'j0' in r]
        row.sort(key=lambda x: x[0].mid())
        for (s1, j1), (s2, j2) in zip(row, row[1:]):
            pairs += 1
            if j1 < j2:
                bad.append('t = %s: j₀ %d at σ = %s below j₀ %d at σ = %s' % (tt, j1, s1.str(3, radius=False), j2, s2.str(3, radius=False)))
    say('  H2 %s -- at fixed t among cells with j₀, j₀ non-decreasing as σ decreases toward 1/2: %d adjacent pair(s) read%s%s' % (
        'REFUTED' if bad else ('HELD' if pairs else 'VACUOUS (HELD, no pair of cells with an index at one t)'), pairs,
        (' ; refuting: ' + '; '.join(bad)) if bad else '', ''))
    h3c = [r for r in recs if (r['sigma'], r['t']) == H3_CELL][0]
    if 'H3' in h3c:
        say('  H3 %s -- at (%s, %s), j₀ = %d, the zero side`s ball %s' % ('HELD' if h3c['H3']['held'] else 'REFUTED', H3_CELL[0], H3_CELL[1],
                                                                         h3c['H3']['j0'], h3c['H3']['zero_side']))
    else:
        say('  H3 NOT SCORABLE -- the cell (%s, %s) reads %s, no j₀ to read the zero side at' % (H3_CELL[0], H3_CELL[1], h3c['reading']))
    hA = [r for r in recs if r['reading'] == 'HYP-UNVERIFIED(hA)']
    say('  H4 %s -- cells printing HYP-UNVERIFIED(hA): %d of %d' % ('REFUTED' if hA else 'HELD', len(hA), c))
    return forms


def put(recs, name='b662_detection_map_40'):
    tx = (NL.join(OUT) + NL).encode('utf-8')
    p = os.path.join(D_DIR, name + '.txt')
    open(p + '.tmp', 'wb').write(tx)
    os.replace(p + '.tmp', p)
    js = (json.dumps(dict(cells=recs), indent=1, ensure_ascii=False, default=str) + NL).encode('utf-8')
    p = os.path.join(D_DIR, name + '.json')
    open(p + '.tmp', 'wb').write(js)
    os.replace(p + '.tmp', p)


# ================================================================================ THE CONTROL, NOT A READING
CONTROL_CAP = 40                                           # ### the control's index range: j in [D, D + 40], not the map's J_max


def control():
    """`python tools/b661_map.py control`: every cell of the map read NONE ≤ J_max, so no index was there to check the computation's binding
    to the kernel's objects by. A positive control, NOT a reading of the map: at H3's cell the same certifications, then hrate read past
    J_max up to D + 40 until it holds, and the zero side read at that j as H3 reads it. H3 stays NOT SCORABLE (its cell prints no j₀);
    this bank (data/b661_map_control.txt) says whether the machinery binds where an index exists."""
    t0 = time.time()
    say('b661 -- THE CONTROL BESIDE THE MAP, NOT A READING OF IT (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    say('')
    say('### every cell of relay data/b661_detection_map.txt read NONE ≤ J_max; H3 is NOT SCORABLE there. This control reads H3`s cell')
    say('### (%s, %s) with the same certifications and hrate past J_max (j ≤ D + %d), and the zero side at the first j where hrate holds:' % (
        H3_CELL[0], H3_CELL[1], CONTROL_CAP))
    say('### it tests the computation`s binding to the kernel`s objects, and scores nothing. Arb balls at %d bits.' % PREC)
    say('')
    ctx.prec = PREC
    n, zl, okz, last, nxt = zero_list()
    say('### THE ZERO LIST at %d bits: N(%d) = %d ; %s' % (PREC, T_HEIGHT, n, 'MATCHED' if okz else 'NOT MATCHED -- THE CONTROL STOPS'))
    if not okz:
        sys.exit(2)
    lo, hi = i4_ball()
    i4 = span(lo, hi)
    say("### ∫_0^1 |s''''| = %s" % b(i4, 20))
    say('')
    r = cell(H3_CELL[0], H3_CELL[1], PREC, zl, i4, rung_note='THE CONTROL, j ≤ D + %d' % CONTROL_CAP, jcap=CONTROL_CAP)
    say('  CONTROL (%s, %s): hrate first holds at %s ; %s' % (H3_CELL[0], H3_CELL[1], ('j = %d' % r['j0']) if 'j0' in r else 'no j ≤ D + %d' % CONTROL_CAP,
                                                         ('the zero side BELOW 0' if r['H3']['held'] else 'the zero side NOT BELOW 0') if 'H3' in r else 'no zero side read'))
    say('### elapsed %d s' % int(time.time() - t0))
    r.pop('_ctx', None)
    put([r], name='b661_map_control')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'control':
        sys.exit('### b662: the control route is b661`s and writes b661`s bank -- NOT RUN FROM THIS COPY')
    else:
        main()
