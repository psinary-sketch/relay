# -*- coding: utf-8 -*-
"""b328_family.py -- THE DISCRIMINATING FAMILY: THE CONDITION CHECKED, THE SEEDS BUILT, THE CONTROL RUN.

### ### **THE DERIVATION IS IN THE SEALED REGISTRATION, SECTION (2).** ### This tool measures its bars:
###   ### (B1) the four-term sum at a quadruple is `4 Re[G(c) G(-c)]` -- checked against b326's banked
###       four terms at the thirteen arc cells, the seed's transform formed here from the SEED alone;
###   ### (B2) for an even seed `G(-c) = G(c)`, so the sum is `4 |G|^2 cos(2 phi)`;
###   ### (B3) b326's own seeds have `|phi| < 45 deg` at the first off-line zero, as their positive
###       banked sums require;
###   ### (B4) two transform routes sharing no code -- the corpus's closed form `mellin_exact`
###       (imported) and this file's Simpson quadrature -- agree to 1e-10 relative;
###   ### (B5) the even seed reaches `|phi| > 45 deg` at a registered width or is reported NOT REACHED;
###       the odd seed has `|phi_o| < 45 deg`;
###   ### (B6) the two `Lambda_Q` routes agree to 1e-9; the two archimedean routes to 1e-9 relative;
###       the two prime routes to 1e-12 absolute.
### ### **THE PLACES SIDES ARE COMPUTED WITH NO ZERO** (`b326_windows.channels`, imported); the closure
### (`b326_closure.closure_row`, imported) corroborates from the libraries and reports the quadruples
### separately. ### **NOTHING HERE IS EDITED IN THE OWNER TOOLS.**

### ### **THE PHASES, EACH WRITING ITS OWN FILE ONCE:** ### `--derive` (B1-B3, the arc's seeds);
### `--build` (the two seeds at four widths: lawfulness, routes, phases, the quadruple's term);
### `--cell SEED a` (one control cell: channels at two u-grids, the gate, the closure);
### `--assemble` (the verdicts by the sealed branches, from the cell files).
"""
import io
import json
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import carto_atlas as AT        # noqa: E402
import b317_smear as SM         # noqa: E402
import b318_square as SQ        # noqa: E402
import b325_epstein as EP       # noqa: E402
import b326_windows as BW       # noqa: E402
import b326_closure as BC       # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LIB = json.load(io.open(os.path.join(D, 'b326_epstein_zeros.json'), encoding='utf-8'))
OFF = json.load(io.open(os.path.join(D, 'b326_offline.json'), encoding='utf-8'))
BETA1, GAMMA1 = LIB['offline'][0]['rho_a']          # ### quoted from the library, the registration's zero
DELTA = BETA1 - 0.5
C1 = complex(DELTA, GAMMA1)
WIDTHS = (20.0, 40.0, 81.0, 160.0)                   # ### the registration's, section (3)
NV = 32769                                           # ### the closure's fine grid
ARC_CELLS = (1.3, 1.35, 1.41, 1.5, 1.7, 1.9, 1.99, 2.0, 2.01, 2.1, 2.4, 2.8, 3.0)
THRESHOLD_DEG = 45.0
ROUTE_BAR = 1e-10
B1_BAR = 1e-9
LAWFUL_FLOOR = -1e-9                                 # ### b320's floor
POLE_BAR = 1e-9
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def _jd(o):
    """### numpy scalars into JSON -- the certification's `bool` is numpy's, and the first cell run died at its dump."""
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError('not serializable: %r' % type(o))


# ### ==============================================================================================
# ### THE TRANSFORM OF A SEED, TWO ROUTES SHARING NO CODE.
# ### ==============================================================================================
def G_closed(v, w, c):
    """### ROUTE A: the corpus's closed form (`b326_closure.mellin_exact`, imported) -- uniform grids."""
    return complex(BC.mellin_exact(v, w, np.array([c], dtype=np.complex128))[0])


def G_general(v, w, c):
    """### ROUTE A' for a NON-UNIFORM piecewise-linear grid (the arc's union grids): with `w` vanishing at
    ### both ends, `INT w e^{c v} dv = -(1/c^2) SUM_j beta_j (e^{c v_{j+1}} - e^{c v_j})`, `beta_j` the
    ### segment slopes -- the telescoped terms vanish because `w_0 = w_N = 0`. ### This file's own code."""
    v = np.asarray(v, dtype=np.float64)
    w = np.asarray(w, dtype=np.float64)
    beta = (w[1:] - w[:-1]) / (v[1:] - v[:-1])
    E = np.exp(c * v)
    return complex(-(np.sum(beta * (E[1:] - E[:-1]))) / (c * c))


def G_simpson(v, w, c, n=None):
    """### ROUTE B: Simpson's rule on a uniform resampling (this file's own code; no closed form)."""
    v = np.asarray(v, dtype=np.float64)
    w = np.asarray(w, dtype=np.float64)
    n = (v.size if n is None else n)
    if n % 2 == 0:
        n += 1
    vv = np.linspace(v[0], v[-1], n)
    ww = np.interp(vv, v, w, left=0.0, right=0.0)
    h = vv[1] - vv[0]
    coef = np.ones(n)
    coef[1:-1:2] = 4.0
    coef[2:-1:2] = 2.0
    return complex(np.sum(ww * np.exp(c * vv) * coef) * h / 3.0)


def quadruple_sum(Gc, Gmc):
    """### `S_4 = 4 Re[G(c) G(-c)]` -- the registration's (2)(b)."""
    return 4.0 * (Gc * Gmc).real


def even_reduction(Gc):
    """### `4 |G|^2 cos(2 phi)` -- the registration's (2)(c)."""
    return 4.0 * abs(Gc) ** 2 * math.cos(2.0 * math.atan2(Gc.imag, Gc.real))


def phase_deg(Gc):
    return math.degrees(math.atan2(Gc.imag, Gc.real))


def fixtures():
    """### BOTH POLARITIES ON THE CONDITION: a phase of 60 deg gives a negative sum, 30 deg a positive one;
    ### an odd seed's `-4 Re G_o^2` is negative at 30 deg and positive at 60 deg."""
    g60 = 2.0 * complex(math.cos(math.radians(60)), math.sin(math.radians(60)))
    g30 = 2.0 * complex(math.cos(math.radians(30)), math.sin(math.radians(30)))
    a = quadruple_sum(g60, g60) < 0 and abs(quadruple_sum(g60, g60) - even_reduction(g60)) < 1e-12
    b = quadruple_sum(g30, g30) > 0 and abs(quadruple_sum(g30, g30) - even_reduction(g30)) < 1e-12
    c = quadruple_sum(g30, -g30) < 0          # ### an odd seed: G(-c) = -G_o(c), phase 30 -> negative
    d = quadruple_sum(g60, -g60) > 0          # ### an odd seed at 60 deg -> positive
    return a, b, c, d


# ### ==============================================================================================
# ### THE SEEDS.
# ### ==============================================================================================
def _bump_on(V, a):
    v, w = AT.bump(a)
    return np.interp(V, v, w, left=0.0, right=0.0)


def seed_even(a):
    """### THE SINE-AIMED EVEN SEED: `env(v) sin(gamma_1 |v|)` on the corpus's bump, plus two even bump
    ### corrections solving the two moments as b317 solves them (`c_0 = 1`); scale `INT |w| = 1`."""
    L = math.log(a)
    V = np.linspace(-L, L, NV)
    phi0 = _bump_on(V, a) * np.sin(GAMMA1 * np.abs(V))
    phi1 = _bump_on(V, a ** 0.5)
    phi2 = _bump_on(V, a ** 0.25)
    phi = [phi0, phi1, phi2]
    I = np.array([np.trapezoid(p, V) for p in phi])
    M = np.array([np.trapezoid(p * np.cosh(V / 2.0), V) for p in phi])
    A2 = np.array([[I[1], I[2]], [M[1], M[2]]])
    c12 = np.linalg.solve(A2, np.array([-I[0], -M[0]]))
    w = phi0 + c12[0] * phi1 + c12[1] * phi2
    w = w / np.trapezoid(np.abs(w), V)
    tf = SM.TestFunction('sine-aimed even seed a=%g' % a, V, w, 'env(v) sin(gamma_1 |v|) on the corpus bump; two even corrections; b317 moments')
    tf.coeffs = (1.0, float(c12[0]), float(c12[1]))
    tf.kind = 'E'
    return tf


def seed_odd(a):
    """### THE COSINE-AIMED ODD SEED: `(v/L) env(v) cos(gamma_1 v)` (odd, continuous, zero at 0 and at the
    ### ends), plus one odd correction `(v/L) env_{a^{1/2}}(v)` solving the single pole condition
    ### `INT w sinh(v/2) dv = 0`; `INT w dv = 0` is automatic; scale `INT |w| = 1`."""
    L = math.log(a)
    V = np.linspace(-L, L, NV)
    phi0 = (V / L) * _bump_on(V, a) * np.cos(GAMMA1 * V)
    phi1 = (V / L) * _bump_on(V, a ** 0.5)
    m0 = np.trapezoid(phi0 * np.sinh(V / 2.0), V)
    m1 = np.trapezoid(phi1 * np.sinh(V / 2.0), V)
    c1 = -m0 / m1
    w = phi0 + c1 * phi1
    w = w / np.trapezoid(np.abs(w), V)
    tf = SM.TestFunction('cosine-aimed odd seed a=%g' % a, V, w, '(v/L) env(v) cos(gamma_1 v); one odd correction; the single pole condition')
    tf.coeffs = (1.0, float(c1))
    tf.kind = 'O'
    return tf


def make_seed(kind, a):
    return seed_even(a) if kind == 'E' else seed_odd(a)


def lawfulness(seed):
    """### (L1) Definition 3.1 on f = g conv g^#, by b318's scan; (L2) the pole conditions on the seed and P."""
    f = SQ.autocorrelation(seed, nv=NV)
    mn, tmin, h0, ok = SQ.positive_definite(f)
    v, w = seed.v, seed.w
    l1 = float(np.trapezoid(np.abs(w), v))
    g_half = G_closed(v, w, 0.5 + 0j)
    g_mhalf = G_closed(v, w, -0.5 + 0j)
    g_zero = float(np.trapezoid(w, v))
    P = 2.0 * (g_half * g_mhalf).real       # ### f~(0) + f~(1) = 2 G(1/2) G(-1/2)
    return dict(min_fhat=float(mn), t_at_min=float(tmin), fhat0=float(h0), def31=bool(mn >= LAWFUL_FLOOR),
                G_half=abs(g_half), G_mhalf=abs(g_mhalf), G_zero=abs(g_zero), l1=l1,
                poles_ok=bool(max(abs(g_half), abs(g_mhalf), abs(g_zero)) <= POLE_BAR * l1),
                P=float(P), P_ok=bool(abs(P) <= 1e-12),
                scan_reach=float(SQ.PD_TMAX_OVER_L / abs(float(f.v[-1]))))


def transform_at(seed, c):
    """### G(c) and G(-c) by both routes; the route disagreement; the phase; the quadruple's term."""
    v, w = seed.v, seed.w
    ga, gma = G_closed(v, w, c), G_closed(v, w, -c)
    gb, gmb = G_simpson(v, w, c), G_simpson(v, w, -c)
    dis = max(abs(ga - gb) / max(abs(ga), 1e-300), abs(gma - gmb) / max(abs(gma), 1e-300))
    return dict(G=[ga.real, ga.imag], G_minus=[gma.real, gma.imag], route_diff=float(dis), route_ok=bool(dis <= ROUTE_BAR),
                phase_deg=phase_deg(ga), phase_minus_deg=phase_deg(gma), S4=quadruple_sum(ga, gma),
                S4_route2=quadruple_sum(gb, gmb), even_reduction=even_reduction(ga),
                even_symmetry=float(abs(gma - ga) / max(abs(ga), 1e-300)))


def zero_side_pieces(seed):
    """### the zero side of `f = g conv g^#` FROM THE SEED: on-line `2 SUM_k |G(i gamma_k)|^2` over the
    ### Epstein library, the first quadruple, the other sixteen, and zeta's on-line sum -- corroboration
    ### numbers, formed by the closed form on the seed alone."""
    v, w = seed.v, seed.w
    gq = np.array([z['gamma_a'] for z in LIB['zeros']], dtype=np.float64)
    Gq = BC.mellin_exact(v, w, 1j * gq)
    Gqm = BC.mellin_exact(v, w, -1j * gq)
    on_q = 2.0 * float(np.sum((Gq * Gqm).real))
    quads = []
    for o in OFF['zeros']:
        b, g = o['rho_a']
        c = complex(b - 0.5, g)
        quads.append(quadruple_sum(G_closed(v, w, c), G_closed(v, w, -c)))
    Gz = BC.mellin_exact(v, w, 1j * np.asarray(AT.GAM, dtype=np.float64))
    Gzm = BC.mellin_exact(v, w, -1j * np.asarray(AT.GAM, dtype=np.float64))
    on_z = 2.0 * float(np.sum((Gz * Gzm).real))
    return dict(on_q=on_q, quad_first=quads[0], quads_other=float(sum(quads[1:])), quads=quads,
                zero_q=on_q + float(sum(quads)), on_z=on_z)


# ### ==============================================================================================
# ### THE PHASES.
# ### ==============================================================================================
def derive():
    rec('=' * 100)
    rec('b328 -- THE CONDITION, CHECKED. ### (B1) the quadruple sum, (B2) the even reduction, (B3) b326\'s seeds.')
    rec('=' * 100)
    fa, fb, fc, fd = fixtures()
    rec('  FIXTURES, both polarities : even 60 deg negative %s ; even 30 deg positive %s ; odd 30 deg negative %s ; odd 60 deg positive %s'
        % (fa, fb, fc, fd))
    if not (fa and fb and fc and fd):
        rec('  ### REFUSING TO PROCEED WITH A CONDITION THAT FAILS ITS OWN FIXTURES.')
        return 2
    rec('  the zero aimed at (library, both routes agree) : beta_1 = %.16f  gamma_1 = %.15f  delta = %.16f' % (BETA1, GAMMA1, DELTA))
    clo = json.load(io.open(os.path.join(D, 'b326_closure.json'), encoding='utf-8'))
    rows = {r['a']: r for r in clo['rows']}
    rec('')
    rec('  %6s %14s %14s %12s %12s %10s %10s %8s %8s' % ('a', 'S4 from seed', 'S4 banked', '|rel diff|', 'coarse-grid', 'phase deg', 'G(-c)=G(c)', 'sign ok', 'route'))
    worst_b1, worst_b1c, worst_sym, worst_route, phases = 0.0, 0.0, 0.0, 0.0, []
    b3_ok = True
    out = []
    for a in ARC_CELLS:
        seed = SM.mean_zero_variant(a)
        v, w = seed.v, seed.w
        ga, gma = G_general(v, w, C1), G_general(v, w, -C1)
        gb = G_simpson(v, w, C1, n=NV)
        route = abs(ga - gb) / abs(ga)
        s4 = quadruple_sum(ga, gma)
        r = rows[a]
        terms = r['zero']['offline_terms'][:4]           # ### the first quadruple, banked on the fine grid
        s4_banked = float(sum(t['term'][0] for t in terms))
        terms_c = r['zero_all']['offline_terms'][:4] if r.get('zero_all') else terms
        # ### the same four terms re-formed on the coarse (8193) autocorrelation grid, to show the grid term
        fc_ = SQ.autocorrelation(seed)
        s4_coarse = float(sum(BC.ftilde(fc_.v, fc_.w, complex(*t['rho']))[1].real for t in terms))
        rel = abs(s4 - s4_banked) / abs(s4_banked)
        relc = abs(s4 - s4_coarse) / abs(s4_coarse)
        sym = abs(gma - ga) / abs(ga)
        ph = phase_deg(ga)
        sign_ok = (math.copysign(1, even_reduction(ga)) == math.copysign(1, s4_banked))
        b3_ok = b3_ok and abs(ph) < THRESHOLD_DEG and sign_ok
        worst_b1, worst_b1c, worst_sym, worst_route = max(worst_b1, rel), max(worst_b1c, relc), max(worst_sym, sym), max(worst_route, route)
        phases.append(ph)
        rec('  %6.2f %14.6e %14.6e %12.3e %12.3e %10.3f %10.2e %8s %8.1e' % (a, s4, s4_banked, rel, relc, ph, sym, sign_ok, route))
        out.append(dict(a=a, S4_seed=s4, S4_banked=s4_banked, S4_coarse=s4_coarse, rel=rel, rel_coarse=relc, phase_deg=ph, sym=sym, route=route, sign_ok=sign_ok))
    rec('')
    b1 = worst_b1 <= B1_BAR
    rec('  (B1) worst |S4_seed - S4_banked| / |S4_banked| : %.3e   bar %.0e   %s' % (worst_b1, B1_BAR, 'HOLDS' if b1 else '### FAILS AS SEALED ###'))
    rec('       ### the banked terms are the transform of the DISCRETIZED autocorrelation (np.correlate on 32769 nodes) and the')
    rec('       ### seed-formed S4 is exact for the seed; their difference is the square\'s discretization, and against the 8193-grid')
    rec('       ### square it is %.3e -- the ratio of the two grid terms is %.2f (16 for a second-order term).' % (worst_b1c, worst_b1c / max(worst_b1, 1e-300)))
    b2 = worst_sym <= 1e-12
    rec('  (B2) worst |G(-c) - G(c)| / |G(c)| over the even arc seeds : %.3e   bar 1e-12   %s' % (worst_sym, 'HOLDS' if b2 else '### FAILS ###'))
    rec('  (B4) worst route disagreement on the arc seeds : %.3e   bar %.0e   %s' % (worst_route, ROUTE_BAR, 'HOLDS' if worst_route <= ROUTE_BAR else '### FAILS ###'))
    rec('  (B3) every arc phase below %g deg and every even-reduction sign the banked sign : %s   (phases %.2f .. %.2f deg)'
        % (THRESHOLD_DEG, 'HOLDS' if b3_ok else '### FAILS -- THE DERIVATION IS REFUTED ###', min(phases), max(phases)))
    rec('  ### (F1) the even-seed reduction : %s' % ('DERIVES AS ASSERTED' if (b2 and b3_ok) else 'NOT AS ASSERTED'))
    rec('=' * 100)
    rec_j = dict(beta1=BETA1, gamma1=GAMMA1, delta=DELTA, fixtures=[fa, fb, fc, fd], cells=out,
                 B1=dict(worst=worst_b1, bar=B1_BAR, holds=b1, worst_vs_coarse=worst_b1c),
                 B2=dict(worst=worst_sym, holds=b2), B3=dict(holds=b3_ok, phases=phases),
                 B4=dict(worst=worst_route, holds=bool(worst_route <= ROUTE_BAR)), F1=bool(b2 and b3_ok))
    io.open(os.path.join(D, 'b328_derive.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(rec_j, indent=1, default=_jd) + '\n')
    io.open(os.path.join(D, 'b328_derive_run.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    return 0


def build():
    rec('=' * 100)
    rec('b328 -- THE CONSTRUCTION. ### two seeds at four widths: lawfulness, two routes, the phase, the quadruple\'s term.')
    rec('=' * 100)
    out = []
    for kind in ('E', 'O'):
        for a in WIDTHS:
            seed = make_seed(kind, a)
            L = math.log(a)
            law = lawfulness(seed)
            tr = transform_at(seed, C1)
            zs = zero_side_pieces(seed)
            reach = (abs(tr['phase_deg']) > THRESHOLD_DEG) if kind == 'E' else (abs(tr['phase_deg']) < THRESHOLD_DEG)
            rec('')
            rec('  SEED %s  a = %g  L = %.4f  delta L = %.3f  coeffs %s' % (kind, a, L, DELTA * L, tuple(round(x, 6) for x in seed.coeffs)))
            rec('    (L1) Definition 3.1 scan : min f-hat %.3e at t = %.3f (f-hat(0) = %.3e, reach t <= %.1f)  %s'
                % (law['min_fhat'], law['t_at_min'], law['fhat0'], law['scan_reach'], 'LAWFUL' if law['def31'] else '### NOT POSITIVE DEFINITE ###'))
            rec('    (L2) |G(1/2)| %.2e  |G(-1/2)| %.2e  |G(0)| %.2e  (bar %.0e x L1 %.3f)  %s ; pole term P = %.3e  %s'
                % (law['G_half'], law['G_mhalf'], law['G_zero'], POLE_BAR, law['l1'], 'POLES VANISH' if law['poles_ok'] else '### POLE CONDITION FAILS ###', law['P'], 'ok' if law['P_ok'] else '### P NOT ZERO ###'))
            rec('    (B4) G(c_1) = %+.6e %+.6e i ; G(-c_1) = %+.6e %+.6e i ; route disagreement %.2e  %s'
                % (tr['G'][0], tr['G'][1], tr['G_minus'][0], tr['G_minus'][1], tr['route_diff'], 'HOLDS' if tr['route_ok'] else '### FAILS ###'))
            if kind == 'E':
                rec('    (B2) even symmetry |G(-c) - G(c)|/|G(c)| = %.2e' % tr['even_symmetry'])
            rec('    (B5) PHASE at rho_1 : %+.3f deg  (threshold %g deg)  %s' % (tr['phase_deg'], THRESHOLD_DEG, 'REACHED' if reach else '### NOT REACHED ###'))
            rec('    the quadruple\'s term S4 = %+.6e (route 2 %+.6e) ; on-line Epstein sum 2 SUM |G(i gamma_k)|^2 = %+.6e ; the other sixteen quadruples %+.6e'
                % (tr['S4'], tr['S4_route2'], zs['on_q'], zs['quads_other']))
            rec('    -> the Epstein zero side FROM THE SEED : %+.6e  (%s) ; zeta\'s on-line sum %+.6e' % (zs['zero_q'], 'NEGATIVE' if zs['zero_q'] < 0 else 'non-negative', zs['on_z']))
            out.append(dict(kind=kind, a=a, L=L, deltaL=DELTA * L, coeffs=list(seed.coeffs), law=law, transform=tr, zero=zs, reached=bool(reach)))
    e_reach = [x['a'] for x in out if x['kind'] == 'E' and x['reached']]
    o_reach = [x['a'] for x in out if x['kind'] == 'O' and x['reached']]
    rec('')
    rec('  ### (F2) an even seed reaches the threshold without an odd component : %s  (widths reached: %s)' % ('YES' if e_reach else 'NO -- REFUTED', e_reach))
    rec('  ### the odd seed below the threshold at widths : %s' % o_reach)
    rec('  ### lawful at every width : E %s  O %s' % (all(x['law']['def31'] and x['law']['poles_ok'] for x in out if x['kind'] == 'E'),
                                                    all(x['law']['def31'] and x['law']['poles_ok'] for x in out if x['kind'] == 'O')))
    rec('=' * 100)
    io.open(os.path.join(D, 'b328_build.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(out, indent=1, default=_jd) + '\n')
    io.open(os.path.join(D, 'b328_build_run.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    return 0


_LAM = {}


def finite_sides(N):
    if N not in _LAM:
        lam_z = BW.von_mangoldt_sieve(N)
        rq = EP.rep_counts(N)
        lam_q1 = BW.lambda_q_sieve(N, np.asarray(rq, dtype=np.int64))
        lam_q2 = np.asarray(EP.von_mangoldt_q(N, rq), dtype=np.float64)
        _LAM[N] = (lam_z, lam_q1, lam_q2, float(np.max(np.abs(lam_q1 - lam_q2))))
    return _LAM[N]


def cell(kind, a):
    rec('=' * 100)
    rec('b328 -- THE CONTROL CELL. ### seed %s at a = %g. ### the places sides with no zero; the gate; the closure.' % (kind, a))
    rec('=' * 100)
    seed = make_seed(kind, a)
    f = SQ.autocorrelation(seed)                        # ### b318's default grid, as the windows used
    N = int(a * a) + 2
    lam_z, lam_q, lam_q2, lamq_diff = finite_sides(N)
    rec('  finite sides to n = %d ; Lambda_Q by the divisor sieve against b325\'s inversion : worst %.3e  %s' % (N, lamq_diff, 'HOLDS' if lamq_diff <= 1e-9 else '### FAILS ###'))
    ch = BW.channels(f, lam_z, lam_q, refine=1)
    ch4 = BW.channels(f, lam_z, lam_q, refine=4)
    gz = BW.certify(ch['places_z'], ch4['places_z'])
    gq = BW.certify(ch['places_q'], ch4['places_q'])
    ra = max(abs(ch['arch_z'] - ch['arch_z_route2']) / max(abs(ch['arch_z']), 1e-300), abs(ch['arch_q'] - ch['arch_q_route2']) / max(abs(ch['arch_q']), 1e-300))
    rp = abs(ch['prime_z'] - ch['prime_z_route2'])
    rec('  (B6) archimedean routes %.2e rel (bar 1e-9) ; prime routes %.2e abs (bar 1e-12) ; transform routes %.2e' % (ra, rp, ch['hhat_route_diff']))
    rec('  pole P = %+.3e ; zeta: prime %+.9f  arch %+.9f  PLACES %+.9f  [%s %s drift %.1e] ; Epstein: finite %+.9f (%d terms)  arch %+.9f  PLACES %+.9f  [%s %s drift %.1e]'
        % (ch['pole'], ch['prime_z'], ch['arch_z'], ch['places_z'], gz['verdict'], gz['sign'], gz['drift'],
           ch['finite_q'], ch['finite_q_terms'], ch['arch_q'], ch['places_q'], gq['verdict'], gq['sign'], gq['drift']))
    # ### the closure, from the libraries, with every located off-line zero
    if BC._LAMQ is None:
        BC._LAMQ = lam_q if N >= 160002 else BW.lambda_q_sieve(int(400.0 * 400.0) + 2)
    rc = BC.closure_row(a, seed, ch, LIB, OFF['zeros'], deficit=0, sig_hi=1.5)
    zall = rc['zero_all']
    q1 = float(sum(t['term'][0] for t in zall['offline_terms'][:4]))
    qrest = float(sum(t['term'][0] for t in zall['offline_terms'][4:]))
    on_q = zall['zero_q_on']
    rec('  CLOSURE zeta : residual %+.3e  bar %.3e  %s' % (rc['residual_z'], rc['bar_z'], rc['status_z']))
    rec('  CLOSURE Epstein, every located zero : residual %+.3e  bar %.3e  %s' % (rc['residual_q_all'], rc['bar_q'], rc['status_q_all']))
    rec('  THE ZERO SIDE, SEPARATELY : on-line %+.6e ; first quadruple %+.6e ; other sixteen %+.6e ; total %+.6e'
        % (on_q, q1, qrest, zall['zero_q']))
    accounts = (q1 < 0) and (abs(q1) > on_q + qrest) if (on_q + qrest) >= 0 else (q1 < 0)
    rec('  the first quadruple accounts for the sign of the zero side : %s' % accounts)
    out = dict(kind=kind, a=a, N=N, lamq_diff=lamq_diff, channels=ch, channels_refined=ch4, gate_z=gz, gate_q=gq,
               route_arch=ra, route_prime=rp,
               closure=dict(residual_z=rc['residual_z'], bar_z=rc['bar_z'], status_z=rc['status_z'],
                            residual_q_all=rc['residual_q_all'], bar_q=rc['bar_q'], status_q_all=rc['status_q_all'],
                            residual_q_two=rc['residual_q'], status_q_two=rc['status_q'],
                            on_q=on_q, quad_first=q1, quads_other=qrest, zero_q=zall['zero_q'], zero_z=rc['zero']['zero_z'],
                            first_quadruple_terms=zall['offline_terms'][:4], accounts=bool(accounts),
                            tail_z=rc['tail_z']['used'], tail_q=rc['tail_q']['used'], arch_tail_z=rc['arch_tail_z']['used'], arch_tail_q=rc['arch_tail_q']['used']))
    name = 'b328_cell_%s_%g' % (kind, a)
    io.open(os.path.join(D, name + '.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(out, indent=1, default=_jd) + '\n')
    io.open(os.path.join(D, name + '_run.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    rec('=' * 100)
    return 0


def assemble():
    rec('=' * 100)
    rec('b328 -- THE VERDICTS, BY THE SEALED BRANCHES, FROM THE CELL FILES.')
    rec('=' * 100)
    cells = []
    for kind in ('E', 'O'):
        for a in WIDTHS:
            p = os.path.join(D, 'b328_cell_%s_%g.json' % (kind, a))
            if os.path.exists(p):
                cells.append(json.load(io.open(p, encoding='utf-8')))
    rec('  cell files present : %d of 8' % len(cells))
    rec('  %4s %6s %14s %8s %14s %8s %10s %10s %14s %14s %8s' % ('seed', 'a', 'Q places', 'sign', 'zeta places', 'sign', 'Q closes', 'z closes', 'quad 1', 'on-line Q', 'accounts'))
    flips, sees, partial = [], [], []
    for c in cells:
        gq, gz, cl = c['gate_q'], c['gate_z'], c['closure']
        rec('  %4s %6g %+14.6e %8s %+14.6e %8s %10s %10s %+14.6e %+14.6e %8s'
            % (c['kind'], c['a'], c['channels']['places_q'], gq['sign'], c['channels']['places_z'], gz['sign'],
               cl['status_q_all'], cl['status_z'], cl['quad_first'], cl['on_q'], cl['accounts']))
        if gz['certified'] and gz['sign'] == '+':
            flips.append(c)
        if gq['certified'] and gq['sign'] == '+':
            if cl['status_q_all'] == 'CLOSES' and cl['status_z'] == 'CLOSES' and cl['accounts'] and gz['certified'] and gz['sign'] == '-':
                sees.append(c)
            else:
                partial.append(c)
    rec('')
    if flips:
        verdict = 'ZETA FLIPS'
        rec('  ### ### **VERDICT : ZETA FLIPS AT %s -- A DEFECT IN THE CHAIN UNTIL PROVEN OTHERWISE; WALKED IN THE BANK.**' % [(c['kind'], c['a']) for c in flips])
    elif sees:
        verdict = 'SEES IT'
        rec('  ### ### **VERDICT : SEES IT** at %s -- the Epstein places side alone takes the forbidden sign, the cell closes for both,'
            % [(c['kind'], c['a']) for c in sees])
        rec('  ### the first quadruple accounts for it, and zeta keeps the permitted sign under the same seed.')
    elif partial:
        verdict = 'PARTIAL'
        rec('  ### ### **VERDICT : PARTIAL** at %s -- a certified positive Epstein sign whose corroboration is incomplete.' % [(c['kind'], c['a']) for c in partial])
    else:
        verdict = 'DOES NOT SEE IT'
        rec('  ### ### **VERDICT : DOES NOT SEE IT** -- no certified positive Epstein places side at any cell of either seed.')
    rec('  ### (F3) SEES IT with zeta holding : %s' % ('MET' if verdict == 'SEES IT' else 'NOT MET (%s)' % verdict))
    rec('=' * 100)
    out = dict(verdict=verdict, sees=[(c['kind'], c['a']) for c in sees], partial=[(c['kind'], c['a']) for c in partial],
               flips=[(c['kind'], c['a']) for c in flips], cells=cells)
    io.open(os.path.join(D, 'b328_family.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(out, indent=1, default=_jd) + '\n')
    io.open(os.path.join(D, 'b328_family_run.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    return 0


if __name__ == '__main__':
    args = sys.argv[1:]
    if args[:1] == ['--derive']:
        sys.exit(derive())
    if args[:1] == ['--build']:
        sys.exit(build())
    if args[:1] == ['--cell']:
        sys.exit(cell(args[1], float(args[2])))
    if args[:1] == ['--assemble']:
        sys.exit(assemble())
    print(__doc__)
    sys.exit(2)
