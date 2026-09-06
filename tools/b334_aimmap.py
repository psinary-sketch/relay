# -*- coding: utf-8 -*-
"""b334_aimmap.py -- THE AIM-MAP: THE GRID, THE FOUR QUANTITIES PER AIM ON TWO LEGS, THE CHART.

### ### **THE REGISTRATION IS SEALED (`data/b334_registration_2026-09-06.txt`); THIS TOOL MEASURES ITS BARS.**
###   `--grid`            the seeds at every (height, width) of section (D): lawfulness, the moment system's
###                       condition number, the phase at every aim (beta, gamma) by two transform routes, the
###                       threshold verdict, the quadruple's term; the zero-side tail bound per seed.
###   `--leg reaching a`  the four quantities for zeta and for the Epstein function on `f = E conv E^#` at
###                       width `a` (40 or 81): the archimedean distribution by the derived kernel on two
###                       transforms and by the principal-value witness (150); the prime sum by two routes; the
###                       Epstein kernel on two transforms, its finite side by two Lambda_Q routes; the gate on
###                       each; the square and the remainder NOT REACHED, with the measurements that say so.
###   `--leg covered`     the same at widths 1.3 and 1.41, PLUS the square on the stable cut at two frames and
###                       the remainder integral by two quadratures, the identity residual printed.
###   `--chart`           the chart-ready block, the narrowest points, the crossing region against the off-line
###                       zeros' heights, the softness of K5 and K6 over aims, both seats' expectations scored.
### ### **THE LIKE-FOR-LIKE RULE, ENFORCED BY NAME:** every quantity is a `Q(name, value)`; `compare` raises on
### a name mismatch; the fixture proves it raises. ### **EVERY INSTRUMENT IS IMPORTED, NEVER EDITED.** ###
### Each mode writes its own run file once; a repeat writing run is numbered.
"""
import io
import json
import math
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import carto_atlas as AT        # noqa: E402
import b316_instrument as INS   # noqa: E402
import b317_smear as SM         # noqa: E402
import b318_square as SQ        # noqa: E402
import b319_stable as ST        # noqa: E402
import b321_window as WI        # noqa: E402
import b313f_qeps_layer as EF   # noqa: E402
import b326_windows as BW       # noqa: E402
import b328_family as FA        # noqa: E402
import noise_floor as NF        # noqa: E402
import b333_diagnose as DG      # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE GRID, AS SEALED IN SECTION (D).
BETAS = (0.50, 0.55, 0.60, 0.70, 0.80, 0.90, 0.9532604747946607)
GAMMAS = (4.0, 8.0, 12.0, 14.134725, 16.290215720390393, 20.0, 25.0, 29.551761098629115, 33.650101, 40.0,
          43.858664, 46.960994, 55.0, 61.687904)
REACHING = (40.0, 81.0)
COVERED = (1.3, 1.41)
OFFLINE_HEIGHTS = (16.290215720390393, 29.551761098629115, 33.650101, 43.858664, 46.960994, 61.687904)
NV = FA.NV
THRESHOLD_DEG = FA.THRESHOLD_DEG
BAR_TRANSFORM = 1e-7        # ### (Q1), (Q1'): the two transforms, relative
BAR_WITNESS = 5e-4          # ### (Q1): the (150) witness against the derived kernel, relative
BAR_PRIME = 1e-12           # ### (Q4): absolute
BAR_LAMQ = 1e-9             # ### (Q4')
BAR_ROUTE_G = FA.ROUTE_BAR  # ### the transform at the aim, 1e-10 relative
BAR_REMAINDER = 1e-6        # ### b321's two-quadrature limit
FRAME_REF = tuple(SM.REFERENCE)
FRAME_GRID = tuple(SM.GRID_AXIS[2])   # ### (8192, 32, NY): rank constant against the reference
EPS_RADII = (2.0, 10.0, 100.0, 1600.0, 6561.0)
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def runfile(base):
    k, name = 1, os.path.join(D, base + '_run.txt')
    while os.path.exists(name):
        k += 1
        name = os.path.join(D, '%s_run%d.txt' % (base, k))
    io.open(name, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    return name


def dump(base, obj):
    p = os.path.join(D, base + '.json')
    open(p + '.tmp', 'wb').write((json.dumps(obj, indent=1, default=FA._jd) + chr(10)).encode('utf-8'))
    os.replace(p + '.tmp', p)
    return p


# ### ==============================================================================================
# ### THE LIKE-FOR-LIKE RULE.
# ### ==============================================================================================
class Q(object):
    """### a quantity that carries the name of the function it was computed on."""
    __slots__ = ('name', 'value')

    def __init__(self, name, value):
        self.name, self.value = name, float(value)


def compare(a, b, rel=True):
    """### the only comparison in this file; it raises when the two sides name different functions."""
    if a.name != b.name:
        raise ValueError('LIKE-FOR-LIKE REFUSED: %r against %r' % (a.name, b.name))
    d = abs(a.value - b.value)
    return d / max(abs(a.value), 1e-300) if rel else d


def fixture_like():
    try:
        compare(Q('E(gamma=16.290216, a=40)', 1.0), Q('E(gamma=16.290216, a=81)', 1.0))
        return False
    except ValueError:
        return compare(Q('x', 2.0), Q('x', 2.0)) == 0.0


def ename(gamma, a):
    return 'E(gamma=%.6f, a=%g)' % (gamma, a)


def fname(gamma, a):
    return 'f = E conv E^# (gamma=%.6f, a=%g)' % (gamma, a)


# ### ==============================================================================================
# ### THE SEED: b328's SINE-AIMED EVEN CONSTRUCTION WITH `gamma` IN PLACE OF `gamma_1`.
# ### ==============================================================================================
def seed_aimed(gamma, a):
    L = math.log(a)
    V = np.linspace(-L, L, NV)
    phi0 = FA._bump_on(V, a) * np.sin(gamma * np.abs(V))
    phi1 = FA._bump_on(V, a ** 0.5)
    phi2 = FA._bump_on(V, a ** 0.25)
    phi = [phi0, phi1, phi2]
    I = np.array([np.trapezoid(p, V) for p in phi])
    M = np.array([np.trapezoid(p * np.cosh(V / 2.0), V) for p in phi])
    A2 = np.array([[I[1], I[2]], [M[1], M[2]]])
    c12 = np.linalg.solve(A2, np.array([-I[0], -M[0]]))
    w = phi0 + c12[0] * phi1 + c12[1] * phi2
    w = w / np.trapezoid(np.abs(w), V)
    tf = SM.TestFunction(ename(gamma, a), V, w, "b328's sine-aimed even construction, gamma in place of gamma_1; two even corrections; b317 moments")
    tf.coeffs = (1.0, float(c12[0]), float(c12[1]))
    tf.cond = float(np.linalg.cond(A2))
    tf.gamma, tf.a = gamma, a
    return tf


# ### ==============================================================================================
# ### --grid
# ### ==============================================================================================
def grid():
    t0 = time.time()
    rec('=' * 100)
    rec('b334 -- THE GRID. ### the seeds at every (height, width); lawfulness; the phase at every aim; the tail bound.')
    rec('=' * 100)
    fl = fixture_like()
    fa, fb, fc, fd = FA.fixtures()
    rec('  FIXTURES : like-for-like refuses a name mismatch %s ; the condition both polarities %s' % (fl, all((fa, fb, fc, fd))))
    if not (fl and fa and fb and fc and fd):
        rec('  ### REFUSING TO PROCEED.')
        return 2
    rec('  aims beta   : %s' % (BETAS,))
    rec('  aims gamma  : %s' % (GAMMAS,))
    rec('  widths      : reaching %s ; covered %s' % (REACHING, COVERED))
    rec('  threshold   : %g deg ; transform-route bar %.0e relative' % (THRESHOLD_DEG, BAR_ROUTE_G))
    out = []
    for leg, widths in (('covered', COVERED), ('reaching', REACHING)):
        for a in widths:
            for g in GAMMAS:
                s = seed_aimed(g, a)
                law = FA.lawfulness(s)
                tb = WI.trunc_bound(s.v, s.w)
                aims = []
                for b in BETAS:
                    c = complex(b - 0.5, g)
                    tr = FA.transform_at(s, c)
                    reached = abs(tr['phase_deg']) > THRESHOLD_DEG
                    aims.append(dict(beta=b, gamma=g, phase_deg=tr['phase_deg'], S4=tr['S4'], route_diff=tr['route_diff'],
                                     route_ok=tr['route_ok'], even_symmetry=tr['even_symmetry'], reached=bool(reached)))
                lawful = bool(law['def31'] and law['poles_ok'])
                rec('')
                rec('  %-9s %s  L = %.4f  cond %.3e  coeffs %s  LAWFUL %s (min f-hat %.2e ; poles %.1e %.1e %.1e ; P %.1e)  tail bound %.2e'
                    % (leg, s.name, math.log(a), s.cond, tuple(round(x, 5) for x in s.coeffs), lawful, law['min_fhat'], law['G_half'], law['G_mhalf'], law['G_zero'], law['P'], tb))
                rec('    %-8s %10s %14s %10s %8s' % ('beta', 'phase deg', 'S4', 'route', 'reached'))
                for q in aims:
                    rec('    %-8.4f %+10.3f %+14.6e %10.2e %8s' % (q['beta'], q['phase_deg'], q['S4'], q['route_diff'], 'REACHED' if q['reached'] else 'no'))
                out.append(dict(leg=leg, a=a, gamma=g, name=s.name, L=math.log(a), cond=s.cond, coeffs=list(s.coeffs), law=law, lawful=lawful,
                                tail_bound=tb, aims=aims))
    n_reached = sum(1 for r in out for q in r['aims'] if q['reached'])
    n_aims = sum(len(r['aims']) for r in out)
    worst_route = max(q['route_diff'] for r in out for q in r['aims'])
    rec('')
    rec('  seeds built %d ; lawful %d ; aims reached %d of %d ; worst transform-route disagreement %.2e (bar %.0e) %s'
        % (len(out), sum(1 for r in out if r['lawful']), n_reached, n_aims, worst_route, BAR_ROUTE_G, 'HOLDS' if worst_route <= BAR_ROUTE_G else '### EXCEEDED, AS MEASURED ###'))
    for leg in ('covered', 'reaching'):
        rs = [r for r in out if r['leg'] == leg]
        rec('  %-9s reached %d of %d aims ; lawful seeds %d of %d' % (leg, sum(1 for r in rs for q in r['aims'] if q['reached']), sum(len(r['aims']) for r in rs),
                                                                       sum(1 for r in rs if r['lawful']), len(rs)))
    rec('  wall %.1f s' % (time.time() - t0))
    rec('=' * 100)
    dump('b334_grid', dict(betas=BETAS, gammas=GAMMAS, reaching=REACHING, covered=COVERED, threshold=THRESHOLD_DEG, seeds=out,
                           fixtures=dict(like=fl, condition=[fa, fb, fc, fd]), worst_route=worst_route))
    return 0


# ### ==============================================================================================
# ### THE FOUR QUANTITIES ON ONE `f`.
# ### ==============================================================================================
def gate(name, v1, v4):
    q1, q4 = Q(name, v1), Q(name, v4)
    compare(q1, q4)
    return BW.certify(q1.value, q4.value)


def quantities(s, lam_z, lam_q, lamq_diff):
    """### zeta's and the Epstein function's channels on `f = E conv E^#`, two routes each, the gate on each."""
    f = SQ.autocorrelation(s)
    fn = fname(s.gamma, s.a)
    ch1 = BW.channels(f, lam_z, lam_q, refine=1)
    ch4 = BW.channels(f, lam_z, lam_q, refine=4)
    a150 = -DG.w150_in_v(f.v, f.w)
    r = dict(name=fn, L_f=ch1['L'], du=ch1['du'], nu=ch1['nu'], pole=ch1['pole'],
             arch_z=ch1['arch_z'], arch_z_route2=ch1['arch_z_route2'], arch_z_refined=ch4['arch_z'], arch_z_150=a150,
             arch_q=ch1['arch_q'], arch_q_route2=ch1['arch_q_route2'], arch_q_refined=ch4['arch_q'], arch_q_b325=ch1['arch_q_b325'],
             prime_z=ch1['prime_z'], prime_z_route2=ch1['prime_z_route2'], prime_z_terms=ch1['prime_z_terms'],
             finite_q=ch1['finite_q'], finite_q_terms=ch1['finite_q_terms'], lamq_diff=lamq_diff,
             places_z=ch1['places_z'], places_z_refined=ch4['places_z'], places_q=ch1['places_q'], places_q_refined=ch4['places_q'],
             hhat_route_diff=ch1['hhat_route_diff'])
    r['d_transform_z'] = compare(Q(fn, ch1['arch_z']), Q(fn, ch1['arch_z_route2']))
    r['d_transform_q'] = compare(Q(fn, ch1['arch_q']), Q(fn, ch1['arch_q_route2']))
    r['d_witness_z'] = compare(Q(fn, ch1['arch_z']), Q(fn, a150))
    r['d_prime'] = compare(Q(fn, ch1['prime_z']), Q(fn, ch1['prime_z_route2']), rel=False)
    r['gate'] = dict(places_z=gate(fn, ch1['places_z'], ch4['places_z']), places_q=gate(fn, ch1['places_q'], ch4['places_q']),
                     arch_z=gate(fn, ch1['arch_z'], ch4['arch_z']), arch_q=gate(fn, ch1['arch_q'], ch4['arch_q']),
                     prime_z=gate(fn, ch1['prime_z'], ch1['prime_z_route2']), finite_q=gate(fn, ch1['finite_q'], ch1['finite_q']))
    r['s5'] = max(compare(Q(fn, ch1['arch_z']), Q(fn, ch4['arch_z'])), r['d_witness_z'])
    r['room_z'] = ch1['arch_z'] - ch1['prime_z']
    r['room_q'] = ch1['arch_q'] - ch1['finite_q']
    return f, r


def print_quantities(r):
    g = r['gate']
    rec('    %s' % r['name'])
    rec('    zeta    : A_z %+.9f (transform 2 %+.9f, d %.2e %s ; witness (150) %+.9f, d %.2e %s ; refined %+.9f) [%s %s drift %.1e]'
        % (r['arch_z'], r['arch_z_route2'], r['d_transform_z'], 'ok' if r['d_transform_z'] <= BAR_TRANSFORM else 'EXCEEDS %.0e' % BAR_TRANSFORM,
           r['arch_z_150'], r['d_witness_z'], 'ok' if r['d_witness_z'] <= BAR_WITNESS else 'EXCEEDS %.0e' % BAR_WITNESS, r['arch_z_refined'],
           g['arch_z']['verdict'], g['arch_z']['sign'], g['arch_z']['drift']))
    rec('              PR_z %+.9f (sieve %+.9f, d %.1e %s ; %d prime powers) ; ROOM A_z - PR_z %+.9f ; places_z %+.9f [%s %s drift %.1e]'
        % (r['prime_z'], r['prime_z_route2'], r['d_prime'], 'ok' if r['d_prime'] <= BAR_PRIME else 'EXCEEDS', r['prime_z_terms'], r['room_z'],
           r['places_z'], g['places_z']['verdict'], g['places_z']['sign'], g['places_z']['drift']))
    rec('    Epstein : A_Q %+.9f (transform 2 %+.9f, d %.2e %s ; b325 halved %+.9f beside, unused ; refined %+.9f) [%s %s drift %.1e]'
        % (r['arch_q'], r['arch_q_route2'], r['d_transform_q'], 'ok' if r['d_transform_q'] <= BAR_TRANSFORM else 'EXCEEDS %.0e' % BAR_TRANSFORM,
           r['arch_q_b325'], r['arch_q_refined'], g['arch_q']['verdict'], g['arch_q']['sign'], g['arch_q']['drift']))
    rec('              finite_Q %+.9f (%d terms ; Lambda_Q sieve vs inversion %.1e %s) ; ROOM A_Q - finite_Q %+.9f ; places_q %+.9f [%s %s drift %.1e]'
        % (r['finite_q'], r['finite_q_terms'], r['lamq_diff'], 'ok' if r['lamq_diff'] <= BAR_LAMQ else 'EXCEEDS', r['room_q'],
           r['places_q'], g['places_q']['verdict'], g['places_q']['sign'], g['places_q']['drift']))
    rec('              the square for Z_Q : NOT AN INSTRUMENT THE RECORD HAS ; the remainder for Z_Q : NOT AN INSTRUMENT THE RECORD HAS')
    rec('    K5 per-aim convergence s5 = %.3e' % r['s5'])


def eps_reach():
    vals = EF.eps(np.array(EPS_RADII, dtype=float))
    rec('  THE EPS EVALUATOR\'S REACH, MEASURED : ' + ' ; '.join('eps(%g) = %+.6e' % (r, v) for r, v in zip(EPS_RADII, vals)))
    ok100 = vals[2] > 0 and vals[2] < vals[1]
    bad = [float(r) for r, v in zip(EPS_RADII, vals) if r > 100.0 and (v < 0 or abs(v) > abs(vals[2]))]
    rec('  ### the value past rho = 100 changes sign or grows at rho = %s : the reaching leg is OUTSIDE its reach' % bad if bad else '  ### no sign change or growth past rho = 100')
    return [float(v) for v in vals], bad, bool(ok100)


# ### ==============================================================================================
# ### --leg reaching a
# ### ==============================================================================================
def leg_reaching(a):
    t0 = time.time()
    rec('=' * 100)
    rec('b334 -- THE REACHING LEG, a = %g. ### the four quantities per aim on f = E conv E^#, two routes each, the gate on each.' % a)
    rec('=' * 100)
    if not fixture_like():
        rec('  ### the like-for-like fixture FAILS ; refusing to proceed.')
        return 2
    N = int(a * a) + 2
    lam_z, lam_q, _lam_q2, lamq_diff = FA.finite_sides(N)
    rec('  finite sides to n = %d ; Lambda_Q by the divisor sieve against b325\'s inversion : worst %.3e %s' % (N, lamq_diff, 'HOLDS' if lamq_diff <= BAR_LAMQ else '### EXCEEDS ###'))
    rec("  THE SQUARE'S REACH, MEASURED : the frame's X = %g against f's support a^2 = %g : %s" % (FRAME_REF[1], a * a, 'NOT REACHED' if a * a > FRAME_REF[1] else 'reached'))
    eps_vals, eps_bad, _ok = eps_reach()
    rec("  THE REMAINDER'S REACH : %s" % ('NOT REACHED at this width (rho to %g)' % (a * a) if eps_bad else 'reached'))
    out = []
    for g in GAMMAS:
        s = seed_aimed(g, a)
        rec('')
        rec('  gamma = %.6f  width %g  seed %s  cond %.2e' % (g, a, s.name, s.cond))
        f, r = quantities(s, lam_z, lam_q, lamq_diff)
        r.update(gamma=g, a=a, seed=s.name, square='NOT REACHED', remainder='NOT REACHED')
        print_quantities(r)
        out.append(r)
    rec('')
    rec('  %-10s %14s %14s %14s %6s %14s %14s %14s %6s' % ('gamma', 'A_z', 'PR_z', 'room_z', 'sign', 'A_Q', 'finite_Q', 'room_Q', 'sign'))
    for r in out:
        rec('  %-10.6f %+14.9f %+14.9f %+14.9f %6s %+14.9f %+14.9f %+14.9f %6s'
            % (r['gamma'], r['arch_z'], r['prime_z'], r['room_z'], r['gate']['places_z']['sign'], r['arch_q'], r['finite_q'], r['room_q'], r['gate']['places_q']['sign']))
    rec('  wall %.1f s' % (time.time() - t0))
    rec('=' * 100)
    dump('b334_leg_reaching_%g' % a, dict(a=a, N=N, lamq_diff=lamq_diff, eps_reach=dict(radii=EPS_RADII, values=eps_vals, outside_at=eps_bad),
                                          square_reach=dict(X=FRAME_REF[1], support=a * a), rows=out))
    return 0


# ### ==============================================================================================
# ### --leg covered
# ### ==============================================================================================
def leg_covered():
    t0 = time.time()
    rec('=' * 100)
    rec('b334 -- THE COVERED LEG, a in %s. ### the four quantities, the square on the stable cut at two frames, the remainder by two quadratures, the identity residual.' % (COVERED,))
    rec('=' * 100)
    if not fixture_like():
        rec('  ### the like-for-like fixture FAILS ; refusing to proceed.')
        return 2
    eps_vals, eps_bad, ok100 = eps_reach()
    rec("  THE REMAINDER'S REACH at the covered widths (rho to %g) : %s" % (COVERED[-1] ** 2, 'reached' if ok100 else '### NOT REACHED ###'))
    frames = {}
    for fk in (FRAME_REF, FRAME_GRID):
        fr = INS.Frame(*fk)
        st, _gr = ST.both_subspaces(fr, ST.TAU)
        ti, _f, _c = SM.identity_trace(fr, st)
        frames[fk] = (fr, st)
        rec('  frame N=%d X=%g : free %d rank %d dim %d ; identity control %.3e' % (fk[0], fk[1], st['free'], st['rank'], st['dim'], abs(ti - st['dim'])))
    rec("  THE SQUARE'S REACH : the frame's X = %g against f's support a^2 = %g : reached" % (FRAME_REF[1], COVERED[-1] ** 2))
    N = int(COVERED[-1] ** 2) + 2
    lam_z, lam_q, _l2, lamq_diff = FA.finite_sides(max(N, 64))
    out = []
    for a in COVERED:
        for g in GAMMAS:
            s = seed_aimed(g, a)
            rec('')
            rec('  gamma = %.6f  width %g  seed %s  cond %.2e' % (g, a, s.name, s.cond))
            f, r = quantities(s, lam_z, lam_q, lamq_diff)
            fn = r['name']
            tr_ref = SQ.square_trace(frames[FRAME_REF][0], frames[FRAME_REF][1], f)
            tr_grid = SQ.square_trace(frames[FRAME_GRID][0], frames[FRAME_GRID][1], f)
            d_sq = compare(Q(fn, tr_ref), Q(fn, tr_grid))
            ru = WI.remainder_integral(f, EF, 'uniform')
            rc = WI.remainder_integral(f, EF, 'cheb')
            d_rem = compare(Q(fn, ru), Q(fn, rc))
            margin = r['arch_z'] - tr_ref
            resid = margin - (-ru)
            s6 = max(d_sq, d_rem)
            r.update(gamma=g, a=a, seed=s.name, square=tr_ref, square_grid=tr_grid, d_square=d_sq, remainder_uniform=ru, remainder_cheb=rc, d_remainder=d_rem,
                     margin=margin, margin_by_remainder=-ru, residual=resid, s6=s6, room_margin=margin - r['prime_z'])
            print_quantities(r)
            rec('    square  : Tr at (%d, %g) %+.9f ; at (%d, %g) %+.9f ; grid drift %.2e (rank constant %d) ; Tr >= 0 %s'
                % (FRAME_REF[0], FRAME_REF[1], tr_ref, FRAME_GRID[0], FRAME_GRID[1], tr_grid, d_sq, frames[FRAME_REF][1]['rank'], tr_ref >= 0))
            rec('    margin  : A_z - Tr %+.9f ; - INT f eps (uniform) %+.9f (cheb %+.9f, rel %.2e %s) ; IDENTITY RESIDUAL %+.9f (printed, not barred) ; ROOM margin - PR_z %+.9f'
                % (margin, -ru, -rc, d_rem, 'ok' if d_rem <= BAR_REMAINDER else 'EXCEEDS %.0e' % BAR_REMAINDER, resid, margin - r['prime_z']))
            rec('    K6 per-aim convergence s6 = %.3e' % s6)
            out.append(r)
    rec('')
    rec('  %-6s %-10s %14s %14s %14s %14s %14s %14s %6s %14s %14s %6s' % ('a', 'gamma', 'A_z', 'Tr', 'margin', '-INT f eps', 'residual', 'PR_z', 'sign', 'A_Q', 'finite_Q', 'sign'))
    for r in out:
        rec('  %-6g %-10.6f %+14.9f %+14.9f %+14.9f %+14.9f %+14.9f %+14.9f %6s %+14.9f %+14.9f %6s'
            % (r['a'], r['gamma'], r['arch_z'], r['square'], r['margin'], r['margin_by_remainder'], r['residual'], r['prime_z'], r['gate']['places_z']['sign'],
               r['arch_q'], r['finite_q'], r['gate']['places_q']['sign']))
    rec('  wall %.1f s' % (time.time() - t0))
    rec('=' * 100)
    dump('b334_leg_covered', dict(widths=COVERED, frames=dict((str(k), dict(N=k[0], X=k[1], rank=v[1]['rank'], dim=v[1]['dim'])) for k, v in frames.items()),
                                  eps_reach=dict(radii=EPS_RADII, values=eps_vals, outside_at=eps_bad), lamq_diff=lamq_diff, rows=out))
    return 0


# ### ==============================================================================================
# ### --chart
# ### ==============================================================================================
def spearman(x, y):
    def ranks(v):
        v = np.asarray(v, dtype=float)
        order = np.argsort(v)
        r = np.empty(v.size)
        r[order] = np.arange(1, v.size + 1)
        for val in np.unique(v):
            m = v == val
            if m.sum() > 1:
                r[m] = r[m].mean()
        return r
    rx, ry = ranks(x), ranks(y)
    if rx.std() == 0 or ry.std() == 0:
        return float('nan')
    return float(np.corrcoef(rx, ry)[0, 1])


def chart():
    rec('=' * 100)
    rec('b334 -- THE CHART. ### the block, the narrowest points, the crossing region, the softness of K5 and K6 over aims, the expectations scored.')
    rec('=' * 100)
    G = json.load(io.open(os.path.join(D, 'b334_grid.json'), encoding='utf-8'))
    legs = {}
    for a in REACHING:
        legs[('reaching', a)] = json.load(io.open(os.path.join(D, 'b334_leg_reaching_%g.json' % a), encoding='utf-8'))
    C = json.load(io.open(os.path.join(D, 'b334_leg_covered.json'), encoding='utf-8'))
    for a in COVERED:
        legs[('covered', a)] = dict(rows=[r for r in C['rows'] if r['a'] == a], eps_reach=C['eps_reach'])
    seeds = {(r['leg'], r['a'], r['gamma']): r for r in G['seeds']}
    rec('')
    rec('  ### (F-a) THE CHART-READY BLOCK -- one line per (leg, width, gamma); every value on f = E conv E^# at that (gamma, a).')
    rec('  %-9s %-5s %-10s %14s %14s %14s %5s %14s %14s %14s %5s %14s %14s %14s %8s %s'
        % ('leg', 'a', 'gamma', 'A_z', 'PR_z', 'A_z-PR_z', 'sgn', 'A_Q', 'finite_Q', 'A_Q-fin_Q', 'sgn', 'Tr', 'A_z-Tr', '-INT f eps', 'lawful', 'phase at beta grid (deg) / reached'))
    block = []
    for (leg, a), L in sorted(legs.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        for r in L['rows']:
            sd = seeds[(leg, a, r['gamma'])]
            # ### the quadruple's sign beside the threshold verdict: past 135 degrees the term is positive again
            ph = ' '.join('%+.1f%s%s' % (q['phase_deg'], '*' if q['reached'] else '', '-' if q['S4'] < 0 else '+') for q in sd['aims'])
            tr = r.get('square', 'NOT REACHED')
            line = dict(leg=leg, a=a, gamma=r['gamma'], A_z=r['arch_z'], PR_z=r['prime_z'], room_z=r['room_z'], sign_z=r['gate']['places_z']['sign'],
                        A_Q=r['arch_q'], finite_Q=r['finite_q'], room_q=r['room_q'], sign_q=r['gate']['places_q']['sign'],
                        Tr=(tr if isinstance(tr, float) else None), margin=r.get('margin'), rem=r.get('margin_by_remainder'), lawful=sd['lawful'],
                        reached=[q['reached'] for q in sd['aims']], phases=[q['phase_deg'] for q in sd['aims']], s5=r['s5'], s6=r.get('s6'))
            block.append(line)
            rec('  %-9s %-5g %-10.6f %+14.9f %+14.9f %+14.9f %5s %+14.9f %+14.9f %+14.9f %5s %14s %14s %14s %8s %s'
                % (leg, a, r['gamma'], r['arch_z'], r['prime_z'], r['room_z'], r['gate']['places_z']['sign'], r['arch_q'], r['finite_q'], r['room_q'], r['gate']['places_q']['sign'],
                   ('%+.9f' % tr) if isinstance(tr, float) else 'NOT REACHED', ('%+.9f' % r['margin']) if 'margin' in r else '-', ('%+.9f' % r['margin_by_remainder']) if 'margin_by_remainder' in r else '-',
                   sd['lawful'], ph))
    rec('  (* = the phase exceeds %g deg at that beta: REACHED ; the trailing sign is the quadruple\'s term S_4 = 4 |G|^2 cos 2 phi, negative only between 45 and 135 degrees)' % THRESHOLD_DEG)
    n_reached = sum(1 for r in G['seeds'] for q in r['aims'] if q['reached'])
    n_disc = sum(1 for r in G['seeds'] for q in r['aims'] if q['reached'] and q['S4'] < 0)
    n_wrap = sum(1 for r in G['seeds'] for q in r['aims'] if q['reached'] and q['S4'] >= 0)
    rec('  aims REACHED by the sealed rule %d ; of these with a NEGATIVE quadruple term (discriminating) %d ; REACHED with a POSITIVE term (the phase past 135 deg) %d' % (n_reached, n_disc, n_wrap))

    rec('')
    rec('  ### (F-b) THE NARROWEST POINTS -- the height at which the prime sum comes closest to the room, per leg and width.')
    narrow = {}
    for (leg, a), L in sorted(legs.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        rows = [r for r in L['rows'] if seeds[(leg, a, r['gamma'])]['lawful']]
        r = min(rows, key=lambda r: r['room_z'])
        narrow['%s_%g' % (leg, a)] = dict(gamma=r['gamma'], room=r['room_z'], sign=r['gate']['places_z']['sign'])
        rec('  %-9s a = %-5g : A_z - PR_z smallest at gamma = %.6f : %+.9f [%s]' % (leg, a, r['gamma'], r['room_z'], r['gate']['places_z']['sign']))
        if leg == 'covered':
            rm = min(rows, key=lambda r: r['room_margin'])
            narrow['%s_%g_margin' % (leg, a)] = dict(gamma=rm['gamma'], room=rm['room_margin'])
            rec('  %-9s a = %-5g : margin - PR_z smallest at gamma = %.6f : %+.9f' % (leg, a, rm['gamma'], rm['room_margin']))

    rec('')
    rec("  ### (F-c) THE CROSSING REGION -- (width, gamma) at which places_q is CERTIFIED positive, against the off-line zeros' heights on the grid.")
    crossing = []
    for (leg, a), L in sorted(legs.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        for r in L['rows']:
            gq = r['gate']['places_q']
            if gq['certified'] and gq['sign'] == '+':
                crossing.append((leg, a, r['gamma'], r['places_q']))
    rec('  members : %s' % (['%s a=%g gamma=%.6f places_q=%+.6f' % c for c in crossing] if crossing else 'EMPTY'))
    banked = OFFLINE_HEIGHTS[:2]
    on_grid = OFFLINE_HEIGHTS
    contains_banked = {h: [(leg, a) for (leg, a, g, _p) in crossing if abs(g - h) < 1e-9] for h in banked}
    contains_all = {h: [(leg, a) for (leg, a, g, _p) in crossing if abs(g - h) < 1e-9] for h in on_grid}
    for h in on_grid:
        rec('  off-line height %.6f : in the crossing region at %s' % (h, contains_all[h] if contains_all[h] else 'NONE'))
    elsewhere = [c for c in crossing if not any(abs(c[2] - h) < 1e-9 for h in on_grid)]
    rec('  crossing members at heights that are not off-line zeros : %s' % (elsewhere if elsewhere else 'NONE'))
    f2_reaching = all(any(leg == 'reaching' and a == w for (leg, a) in contains_banked[h]) for h in banked for w in REACHING)
    f2_covered_empty = not any(leg == 'covered' for (leg, _a, _g, _p) in crossing)

    rec('')
    rec('  ### (F-d) THE SOFTNESS OF K5 AND K6 OVER AIMS.')
    cov = [r for r in C['rows']]
    s5 = [r['s5'] for r in cov]
    s6 = [r['s6'] for r in cov]
    rho = spearman(s5, s6)
    rec('  covered leg, %d aims (both widths) : Spearman(s5, s6) = %+.4f' % (len(cov), rho))
    rec('  %-6s %-10s %12s %12s' % ('a', 'gamma', 's5 (K5)', 's6 (K6)'))
    for r in cov:
        rec('  %-6g %-10.6f %12.3e %12.3e' % (r['a'], r['gamma'], r['s5'], r['s6']))
    s5_reach = {a: [r['s5'] for r in legs[('reaching', a)]['rows']] for a in REACHING}
    s5_cov = {a: [r['s5'] for r in legs[('covered', a)]['rows']] for a in COVERED}
    order_agree = {}
    for ar in REACHING:
        for ac in COVERED:
            order_agree['%g_vs_%g' % (ar, ac)] = spearman(s5_reach[ar], s5_cov[ac])
    rec('  the aim ordering by s5, reaching against covered (Spearman over gamma) : %s' % {k: round(v, 4) for k, v in order_agree.items()})
    rec('  reaching leg s5 by gamma : ' + ' ; '.join('a=%g: %s' % (a, ['%.1e' % x for x in s5_reach[a]]) for a in REACHING))

    rec('')
    rec('  ### THE CEILING, PRINTED.')
    tb = max(r['tail_bound'] for r in G['seeds'])
    rec("  zero-side tail bound, largest over the seeds : %.3e ; zeta's ordinates to %.6f (%d) ; the Epstein library on-line to 149.72, off-line census to T = 150" % (tb, float(AT.GAM[-1]), len(AT.GAM)))
    rec("  the frame's X = %g against a^2 = %s ; the eps evaluator past rho = 100 : %s ; the largest gamma charted %.6f" % (FRAME_REF[1], [a * a for a in REACHING + COVERED], legs[('reaching', REACHING[0])]['eps_reach']['outside_at'], max(GAMMAS)))

    rec('')
    rec('  ### THE EXPECTATIONS, SCORED AGAINST PRINTED VALUES.')
    lawful_reach = [r for (leg, a), L in legs.items() if leg == 'reaching' for r in L['rows'] if seeds[(leg, a, r['gamma'])]['lawful']]
    f1_reach_ok = all(r['gate']['places_z']['certified'] and r['gate']['places_z']['sign'] == '-' for r in lawful_reach)
    f1_reach_n = sum(1 for r in lawful_reach if r['gate']['places_z']['certified'] and r['gate']['places_z']['sign'] == '-')
    f1_cov_ok = all(r['room_margin'] > 0 for r in cov)
    f1 = f1_reach_ok and f1_cov_ok
    rec('  (F1) the prime sum inside the margin at every aim : reaching leg places_z certified negative at %d of %d lawful aims ; covered leg margin - PR_z > 0 at %d of %d : %s'
        % (f1_reach_n, len(lawful_reach), sum(1 for r in cov if r['room_margin'] > 0), len(cov), 'MET' if f1 else 'NOT MET'))
    f2 = f2_reaching
    rec("  (F2) the crossing region contains the banked off-line zeros' aims (%s at both reaching widths) : %s ; empty on the covered leg : %s"
        % (['%.6f' % h for h in banked], 'MET' if f2 else 'NOT MET', f2_covered_empty))
    f3 = (rho > 0) if rho == rho else False
    rec('  (F3) K5 and K6 soften together over aims : Spearman(s5, s6) over the covered leg = %+.4f : %s' % (rho, 'MET' if f3 else 'NOT MET'))
    seat = dict(F1='MET' if f1 else 'NOT MET', F2='MET' if (f2 and f2_covered_empty) else 'NOT MET', F3='MET' if f3 else 'NOT MET')
    rec("  THIS SEAT'S : F1 %s ; F2 (met at both banked heights at both reaching widths, empty on the covered leg) %s ; F3 (positive correlation) %s" % (seat['F1'], seat['F2'], seat['F3']))
    cov_reached = any(q['reached'] for r in G['seeds'] if r['leg'] == 'covered' for q in r['aims'])
    az_signs = dict(reaching_all_negative=all(r['arch_z'] < 0 for r in lawful_reach), covered_all_positive=all(r['arch_z'] > 0 for r in cov))
    rec("  and : the covered leg's phases stay below the threshold at every aim : %s ; A_z negative at every reaching aim %s, positive at every covered aim %s"
        % (not cov_reached, az_signs['reaching_all_negative'], az_signs['covered_all_positive']))
    rec('=' * 100)
    dump('b334_chart', dict(block=block, narrowest=narrow, crossing=crossing, contains=dict((str(k), v) for k, v in contains_all.items()), elsewhere=elsewhere,
                            spearman_s5_s6=rho, order_agree=order_agree, s5_reaching=s5_reach, s5_covered=s5_cov,
                            navigator=dict(F1='MET' if f1 else 'NOT MET', F2='MET' if f2 else 'NOT MET', F3='MET' if f3 else 'NOT MET'), seat=seat,
                            covered_reached=cov_reached, az_signs=az_signs, tail_bound=tb,
                            aims_reached=n_reached, aims_discriminating=n_disc, aims_reached_positive_term=n_wrap))
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == '--grid':
        code, base = grid(), 'b334_grid'
    elif argv[0] == '--leg' and argv[1] == 'reaching':
        a = float(argv[2])
        code, base = leg_reaching(a), 'b334_leg_reaching_%g' % a
    elif argv[0] == '--leg' and argv[1] == 'covered':
        code, base = leg_covered(), 'b334_leg_covered'
    elif argv[0] == '--chart':
        code, base = chart(), 'b334_chart'
    else:
        print(__doc__)
        return 2
    print('  run file : %s' % runfile(base))
    return code


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
