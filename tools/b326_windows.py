# -*- coding: utf-8 -*-
"""b326_windows.py -- THE TWO WINDOWS, SIDE BY SIDE, FROM THE ARC'S CELLS THROUGH THE CROSSING
### REGION AND PAST IT. ### EVERY PRIME; EVERY REPRESENTATION NUMBER; BOTH KERNEL NORMALIZATIONS.

### ### **WHAT IS COMPUTED AT EVERY CELL `a`**, on the arc's own test function
### `f = autocorrelation(mean_zero_variant(a))` (b317's seed, b318's square, unchanged):
###   ### `P`      -- the pole term `2 INT w cosh(v/2)`, expected to vanish for a lawful `f`;
###   ### `PR_z`   -- zeta's finite side with EVERY prime power `p^k <= e^L`, by TWO routes sharing
###                   no code: `b321_window.prime_sum` (after the ordered edit) and a von Mangoldt
###                   sieve in this file;
###   ### `PR_q`   -- the Epstein finite side with EVERY representation number: `Lambda_Q(n)` to
###                   `n = a^2` by a divisor-sieve Dirichlet inversion in this file, fixtured against
###                   b325's inversion on its own range and against the per-coefficient identity;
###   ### `A_z`    -- zeta's archimedean channel against the atlas's kernel;
###   ### `A_q`    -- the Epstein archimedean channel against the DERIVED kernel
###                   `2 Re psi(1/2 + i u) - 2 log(2 pi / sqrt23)` (registration section (1));
###   ### `A_q325` -- the same against b325's kernel, HALF of the derived one -- the link walked,
###                   not a channel this act uses;
###   ### the places sums `PR - A` for both, each at TWO `u`-grid resolutions, passed to the
###   noise-floor gate as the SAME cell refined; the sign read only from a RESOLVED value whose
###   size exceeds ten times its drift.
### ### **THE TRANSFORM IS COMPUTED BY TWO ROUTES SHARING NO CODE** -- `b321_window.hhat_blocked`
### and a Simpson-rule transform in this file -- and the archimedean channel is reported from both.
### ### **THE `u`-GRID IS SET BY THE CELL, NOT BY THE ATLAS'S CONSTANT:** ### `hhat` of a test function
### of half-width `L` has lobes of width `~ 1/L`, and the atlas's `du = 0.1` is coarse for `L = 12`.
### ### `du = min(0.1, 0.2 / L)`, refined by four for the gate.
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
import carto_atlas as AT        # noqa: E402  ### the settled chain, IMPORTED never edited
import b317_smear as SM         # noqa: E402
import b318_square as SQ        # noqa: E402
import b321_window as WI        # noqa: E402  ### edited THIS ACT by order: the prime set
import b325_epstein as EP       # noqa: E402  ### last act's finite side and kernel, READ
import noise_floor as NF        # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
OUT_JSON = os.path.join(D, 'b326_windows.json')
OUT_TXT = os.path.join(D, 'b326_windows_run.txt')

DISC = 23
PRICED = (8.0, 12.0, 16.0, 20.0, 22.0, 24.0, 28.0, 32.0, 50.0)      # ### b325's nine
PAST = (64.0, 100.0, 200.0, 400.0)                                   # ### past the crossing region
UMAX = AT.UMAX                                                       # ### 600, the atlas's own
SIGN_MARGIN = 10.0                                                   # ### |value| > 10 x drift


# ### ==============================================================================================
# ### THE TEST FUNCTION AT A CELL, AND ITS TRANSFORM BY TWO ROUTES.
# ### ==============================================================================================
def cell_function(a, aimed_omega=None):
    """### the arc's own `f`; or, for the AIMED family, the same construction on modulated bumps."""
    if aimed_omega is None:
        g = SM.mean_zero_variant(a)
    else:
        g = aimed_variant(a, aimed_omega)
    return SQ.autocorrelation(g)


def aimed_variant(a, omega):
    """### b317's `mean_zero_variant`, with each of the three atlas bumps multiplied by `cos(omega v)`
    ### BEFORE the two vanishing moments are solved -- the same two equations, the same `c_0 = 1`,
    ### the same union grid, the same `INT |f| dv = 1` scale. ### `omega` is the one quoted number."""
    grids = []
    for e in SM.MZ_EXPONENTS:
        v, w = AT.bump(a ** e)
        grids.append((v, w * np.cos(omega * v)))
    V = grids[0][0]
    for v, _w in grids[1:]:
        V = np.union1d(V, v)
    phi = [np.interp(V, v, w, left=0.0, right=0.0) for v, w in grids]
    I = np.array([np.trapezoid(p, V) for p in phi])
    M = np.array([np.trapezoid(p * np.cosh(V / 2.0), V) for p in phi])
    A2 = np.array([[I[1], I[2]], [M[1], M[2]]])
    b2 = np.array([-I[0], -M[0]])
    c12 = np.linalg.solve(A2, b2)
    w = phi[0] + c12[0] * phi[1] + c12[1] * phi[2]
    w = w / np.trapezoid(np.abs(w), V)
    return SM.TestFunction('aimed variant at a=%g, omega=%.6f' % (a, omega), V, w,
                           'b317 mean_zero_variant construction on cos(omega v)-modulated bumps')


def hhat_simpson(v, w, U, block=2048):
    """### ROUTE TWO for the transform: Simpson on the `v`-grid, per `u`, blocked over `u`.
    ### `hhat(u) = INT w(v) cos(u v) dv`. ### Shares nothing with `b321_window.hhat_blocked`."""
    v = np.asarray(v, dtype=np.float64)
    w = np.asarray(w, dtype=np.float64)
    # ### Simpson needs an odd number of nodes on a uniform grid; resample onto one if needed.
    n = v.size
    if n % 2 == 0:
        n += 1
    vv = np.linspace(v[0], v[-1], n)
    ww = np.interp(vv, v, w, left=0.0, right=0.0)
    h = vv[1] - vv[0]
    coef = np.ones(n)
    coef[1:-1:2] = 4.0
    coef[2:-1:2] = 2.0
    coef *= h / 3.0
    out = np.empty(U.size)
    for i in range(0, U.size, block):
        u = U[i:i + block]
        out[i:i + block] = np.cos(np.outer(u, vv)) @ (ww * coef)
    return out


# ### ==============================================================================================
# ### THE FINITE SIDES.
# ### ==============================================================================================
def von_mangoldt_sieve(N):
    """### zeta's `Lambda(n)` for `n <= N` by a smallest-prime-factor sieve. ### ROUTE TWO."""
    spf = np.zeros(N + 1, dtype=np.int64)
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        p = spf[n]
        m = n
        while m % p == 0:
            m //= p
        if m == 1:
            lam[n] = math.log(p)
    return lam


def zeta_finite_route2(v, w, lam):
    L = float(v[-1])
    nmax = int(math.exp(L) + 1e-12)
    total = 0.0
    for n in range(2, min(nmax, lam.size - 1) + 1):
        if lam[n] == 0.0:
            continue
        ln = math.log(n)
        if ln <= L:
            total += 2.0 * lam[n] / math.sqrt(n) * float(np.interp(ln, v, w))
    return total


def rep_counts_b(K):
    """### `r_Q(k)`, `k <= K`, for `x^2 + x y + 6 y^2`, by the y-outer enumeration (b326_zeros's)."""
    r = np.zeros(K + 1, dtype=np.int64)
    ymax = int(math.isqrt(4 * K // 23)) + 2
    for y in range(-ymax, ymax + 1):
        disc = y * y - 4 * (6 * y * y - K)
        if disc < 0:
            continue
        span = int(math.isqrt(disc)) + 2
        xs = np.arange((-y - span) // 2 - 1, (-y + span) // 2 + 2)
        ks = xs * xs + xs * y + 6 * y * y
        ks = ks[(ks >= 1) & (ks <= K)]
        np.add.at(r, ks, 1)
    return r


def lambda_q_sieve(K, rq=None):
    """### `Lambda_Q(n)` to `K` by DIVISOR-SIEVE Dirichlet inversion of `b_k = r_Q(k)/2`:
    ### `SUM_{d | n} Lambda_Q(d) b_{n/d} = b_n log n`. ### ROUTE TWO, `O(K log K)`; shares no code
    ### with b325's per-`n` divisor walk."""
    rq = rep_counts_b(K) if rq is None else rq
    b = rq.astype(np.float64) / 2.0
    lam = np.zeros(K + 1)
    rhs = np.zeros(K + 1)
    for n in range(1, K + 1):
        rhs[n] = b[n] * math.log(n)
    # ### accumulate SUM_{d < n, d | n} Lambda_Q(d) b_{n/d} as each Lambda_Q(d) becomes known.
    acc = np.zeros(K + 1)
    for d in range(1, K + 1):
        lam[d] = rhs[d] - acc[d]
        if lam[d] != 0.0:
            m = np.arange(2 * d, K + 1, d)
            acc[m] += lam[d] * b[m // d]
    return lam


def epstein_finite(v, w, lam):
    L = float(v[-1])
    nmax = int(math.exp(L) + 1e-12)
    total, terms = 0.0, 0
    for n in range(2, min(nmax, lam.size - 1) + 1):
        if lam[n] == 0.0:
            continue
        ln = math.log(n)
        if ln <= L:
            val = 2.0 * lam[n] / math.sqrt(n) * float(np.interp(ln, v, w))
            if val:
                total += val
                terms += 1
    return total, terms


# ### ==============================================================================================
# ### THE KERNELS.
# ### ==============================================================================================
_KCACHE = {}


def kernel_zeta(U):
    """### the atlas's kernel, on THIS grid (the atlas caches on its own grid; b325 found that)."""
    key = ('z', U.size, float(U[0]), float(U[-1]))
    if key not in _KCACHE:
        from mpmath import mp, digamma, mpc, re as mre
        mp.dps = 15
        _KCACHE[key] = (np.array([float(mre(digamma(mpc(0.25, uu / 2.0)))) for uu in U])
                        - math.log(math.pi))
    return _KCACHE[key]


def kernel_q_derived(U):
    """### `2 Re psi(1/2 + i u) - 2 log(2 pi / sqrt23)` -- registration section (1), this act's own
    ### code: `2 Re(gamma_Q'/gamma_Q)` on the line."""
    key = ('q', U.size, float(U[0]), float(U[-1]))
    if key not in _KCACHE:
        from mpmath import mp, digamma, mpc, re as mre
        mp.dps = 15
        _KCACHE[key] = (2.0 * np.array([float(mre(digamma(mpc(0.5, uu)))) for uu in U])
                        - 2.0 * math.log(2.0 * math.pi / math.sqrt(DISC)))
    return _KCACHE[key]


def kernel_q_b325(U):
    """### b325's `kernel_q`, IMPORTED -- the link walked."""
    key = ('q325', U.size, float(U[0]), float(U[-1]))
    if key not in _KCACHE:
        _KCACHE[key] = EP.kernel_q(U)
    return _KCACHE[key]


# ### ==============================================================================================
# ### THE CHANNELS AT A CELL.
# ### ==============================================================================================
def ugrid(L, refine=1):
    du = min(0.1, 0.2 / max(L, 1e-9)) / refine
    n = int(round(2 * UMAX / du)) + 1
    return np.linspace(-UMAX, UMAX, n)


def channels(f, lam_z, lam_q, refine=1):
    v, w = f.v, f.w
    L = float(v[-1])
    U = ugrid(L, refine)
    P = 2.0 * float(np.trapezoid(w * np.cosh(v / 2.0), v))
    h1 = WI.hhat_blocked(v, w, U)
    h2 = hhat_simpson(v, w, U)
    kz = kernel_zeta(U)
    kq = kernel_q_derived(U)
    k3 = kernel_q_b325(U)
    Az1 = float(np.trapezoid(h1 * kz, U) / (2.0 * math.pi))
    Az2 = float(np.trapezoid(h2 * kz, U) / (2.0 * math.pi))
    Aq1 = float(np.trapezoid(h1 * kq, U) / (2.0 * math.pi))
    Aq2 = float(np.trapezoid(h2 * kq, U) / (2.0 * math.pi))
    Aq325 = float(np.trapezoid(h1 * k3, U) / (2.0 * math.pi))
    PRz1, terms_z = WI.prime_sum(v, w, 'corpus')
    PRz2 = zeta_finite_route2(v, w, lam_z)
    PRq, terms_q = epstein_finite(v, w, lam_q)
    return dict(L=L, du=float(U[1] - U[0]), nu=int(U.size), pole=P,
                arch_z=Az1, arch_z_route2=Az2, arch_q=Aq1, arch_q_route2=Aq2, arch_q_b325=Aq325,
                prime_z=PRz1, prime_z_route2=PRz2, prime_z_terms=len(terms_z),
                finite_q=PRq, finite_q_terms=terms_q,
                places_z=PRz1 - Az1, places_q=PRq - Aq1, places_q_b325=PRq - Aq325,
                hhat_route_diff=float(np.max(np.abs(h1 - h2))))


def certify(value, refined):
    """### the gate, then the sign: RESOLVED and |value| > SIGN_MARGIN x drift."""
    verdict, why = NF.classify(value, refined)
    drift = abs(refined - value)
    certified = (verdict == NF.RESOLVED) and abs(value) > SIGN_MARGIN * drift
    sign = ('+' if value > 0 else '-') if certified else '?'
    return dict(verdict=verdict, why=why, drift=drift, certified=certified, sign=sign)


# ### ==============================================================================================
# ### THE FIXTURES.
# ### ==============================================================================================
def self_test(lines):
    ok = []
    # (i) Lambda_Q by the sieve against b325's inversion on b325's own range.
    lq = lambda_q_sieve(EP.KMAX)
    d = float(np.max(np.abs(lq - np.asarray(EP.LAMQ[:EP.KMAX + 1]))))
    ok.append(d < 1e-9)
    lines.append('  (i)    Lambda_Q by the divisor sieve against b325\'s inversion, n <= %d : worst %.3e  %s'
                 % (EP.KMAX, d, 'PASS' if ok[-1] else 'FAIL'))
    # (ii) the per-coefficient Dirichlet identity on a range beyond b325's.
    K = 20000
    rq = rep_counts_b(K)
    lq = lambda_q_sieve(K, rq)
    b = rq / 2.0
    worst = 0.0
    for n in range(2, K + 1, 97):
        s = 0.0
        for dd in range(1, n + 1):
            if n % dd == 0:
                s += lq[dd] * b[n // dd]
        worst = max(worst, abs(s - b[n] * math.log(n)))
    ok.append(worst < 1e-9)
    lines.append('  (ii)   SUM_{d|n} Lambda_Q(d) b_{n/d} = b_n log n, sampled to n = %d : worst %.3e  %s'
                 % (K, worst, 'PASS' if ok[-1] else 'FAIL'))
    # (iii) representation counts against the census's own, k <= 4096.
    same = (rep_counts_b(4096).tolist() == EP.rep_counts(4096)[:4097]) if hasattr(EP, 'rep_counts') else None
    ok.append(bool(same))
    lines.append('  (iii)  r_Q by this file against b325\'s, k <= 4096 : %s' % same)
    # (iv) the derived kernel is exactly twice b325's at seven points.
    U = np.array([-100.0, -7.5, -1.0, 0.0, 1.0, 7.5, 100.0])
    r = float(np.max(np.abs(kernel_q_derived(U) - 2.0 * kernel_q_b325(U))))
    ok.append(r < 1e-12)
    lines.append('  (iv)   derived kernel against 2 x b325\'s kernel at seven points : worst %.3e  %s'
                 % (r, 'PASS' if ok[-1] else 'FAIL'))
    # (v) the zeta kernel here against the atlas's own on the atlas's own grid.
    Ua = np.linspace(-AT.UMAX, AT.UMAX, AT.NU)
    r2 = float(np.max(np.abs(kernel_zeta(Ua) - AT.kernel(Ua))))
    ok.append(r2 < 1e-12)
    lines.append('  (v)    zeta kernel here against carto_atlas.kernel on its own grid : worst %.3e  %s'
                 % (r2, 'PASS' if ok[-1] else 'FAIL'))
    # (vi) the two transform routes on the atlas's bump.
    v, w = AT.bump(2.0)
    Ut = np.linspace(-50, 50, 2001)
    r3 = float(np.max(np.abs(WI.hhat_blocked(v, w, Ut) - hhat_simpson(v, w, Ut))))
    ok.append(r3 < 1e-8)
    lines.append('  (vi)   hhat by b321\'s blocked route and by Simpson, atlas bump a = 2 : worst %.3e  %s'
                 % (r3, 'PASS' if ok[-1] else 'FAIL'))
    # (vii) zeta finite side: the sieve route against b321's prime_sum on a wide function.
    f = cell_function(50.0)
    lam_z = von_mangoldt_sieve(2600)
    a1, _t = WI.prime_sum(f.v, f.w, 'corpus')
    a2 = zeta_finite_route2(f.v, f.w, lam_z)
    ok.append(abs(a1 - a2) < 1e-12)
    lines.append('  (vii)  zeta finite side at a = 50 by b321\'s prime_sum and by the sieve : %.12f vs %.12f  %s'
                 % (a1, a2, 'PASS' if ok[-1] else 'FAIL'))
    # (viii) the eleven-prime tuple is NOT what prime_sum reads any more: at a = 50 the sieve
    #        route and b321's route agree, and both differ from an eleven-prime sum.
    tot11 = 0.0
    L = float(f.v[-1])
    for p in WI.PRIMES_ATLAS:
        k = 1
        while p ** k <= math.exp(L) + 1e-12:
            n = p ** k
            tot11 += 2.0 * math.log(p) / math.sqrt(n) * float(np.interp(math.log(n), f.v, f.w))
            k += 1
    ok.append(abs(tot11 - a1) > 1e-6)
    lines.append('  (viii) the eleven-prime sum at a = 50 : %.9f -- differs from the full set, as it must  %s'
                 % (tot11, 'PASS' if ok[-1] else 'FAIL'))
    # (ix) the noise gate can REFUSE: a drifting pair is refused, a stable pair certified.
    c1 = certify(1e-2, 1e-2 * 1.5)
    c2 = certify(1e-2, 1e-2 * (1 + 1e-6))
    ok.append((not c1['certified']) and c2['certified'] and c2['sign'] == '+')
    lines.append('  (ix)   the gate refuses a drifting pair (%s) and certifies a stable one (%s, sign %s)  %s'
                 % (c1['verdict'], c2['verdict'], c2['sign'], 'PASS' if ok[-1] else 'FAIL'))
    return all(ok), ok


# ### ==============================================================================================
# ### MAIN.
# ### ==============================================================================================
def main():
    lines = []

    def rec(s=''):
        lines.append(s)
        print(s, flush=True)

    rec('=' * 100)
    rec('b326 -- THE TWO WINDOWS. ### EVERY PRIME, EVERY REPRESENTATION NUMBER, BOTH KERNELS.')
    rec('=' * 100)
    good, arms = self_test(lines)
    for ln in lines[3:]:
        print(ln, flush=True)
    rec('  ### FIXTURES : %s  %s' % (arms, 'PASS' if good else '### FAIL ###'))
    if not good:
        io.open(OUT_TXT, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return 2

    cells = [r['a'] for r in SM.atlas_cells()] + list(PRICED) + list(PAST)
    amax = max(cells)
    N = int(amax * amax) + 2
    rec('  finite sides prepared to n = %d (a_max^2): zeta by the sieve, Epstein by the divisor sieve'
        % N)
    lam_z = von_mangoldt_sieve(N)
    lam_q = lambda_q_sieve(N)
    rows = []
    rec('')
    rec('  %-6s %-9s %-14s %-14s %-14s %-14s %-14s %-14s %-9s %-9s'
        % ('a', 'L', 'pole', 'zeta finite', 'zeta arch', 'ZETA places', 'Q finite', 'Q arch',
           'Q places', 'Q places(b325 kernel)'))
    for a in cells:
        f = cell_function(a)
        c1 = channels(f, lam_z, lam_q, refine=1)
        c4 = channels(f, lam_z, lam_q, refine=4)
        gz = certify(c1['places_z'], c4['places_z'])
        gq = certify(c1['places_q'], c4['places_q'])
        gq3 = certify(c1['places_q_b325'], c4['places_q_b325'])
        row = dict(a=a, coarse=c1, refined=c4, gate_z=gz, gate_q=gq, gate_q_b325=gq3)
        rows.append(row)
        rec('  %-6g %-9.4f %-14.3e %-14.9f %-14.9f %-14.9f %-14.9f %-14.9f %-9s %-9s'
            % (a, c1['L'], c1['pole'], c1['prime_z'], c1['arch_z'], c1['places_z'],
               c1['finite_q'], c1['arch_q'], ('%+.9f %s' % (c1['places_q'], gq['sign'])),
               ('%+.9f %s' % (c1['places_q_b325'], gq3['sign']))))
    rec('')
    rec('  ### THE GATE, SAME CELL AT du AND du/4 (RESOLVED and |value| > %g x drift certifies a sign):'
        % SIGN_MARGIN)
    for r in rows:
        rec('    a = %-6g zeta %-9s drift %.2e  sign %s | Epstein %-9s drift %.2e  sign %s | (b325 kernel) %-9s sign %s'
            % (r['a'], r['gate_z']['verdict'], r['gate_z']['drift'], r['gate_z']['sign'],
               r['gate_q']['verdict'], r['gate_q']['drift'], r['gate_q']['sign'],
               r['gate_q_b325']['verdict'], r['gate_q_b325']['sign']))
    # ### the routes' agreement, cell by cell.
    worst_h = max(r['coarse']['hhat_route_diff'] for r in rows)
    worst_az = max(abs(r['coarse']['arch_z'] - r['coarse']['arch_z_route2']) for r in rows)
    worst_aq = max(abs(r['coarse']['arch_q'] - r['coarse']['arch_q_route2']) for r in rows)
    worst_pz = max(abs(r['coarse']['prime_z'] - r['coarse']['prime_z_route2']) for r in rows)
    rec('')
    rec('  ### TWO ROUTES, WORST DISAGREEMENT OVER ALL CELLS: hhat %.3e ; zeta arch %.3e ; Epstein arch %.3e ;'
        ' zeta finite %.3e' % (worst_h, worst_az, worst_aq, worst_pz))
    # ### the zeta control and the crossing.
    zbad = [r['a'] for r in rows if r['gate_z']['certified'] and r['gate_z']['sign'] == '+']
    zunc = [r['a'] for r in rows if not r['gate_z']['certified']]
    rec('  ### THE ZETA CONTROL : cells with a CERTIFIED positive zeta places sum : %s ; cells not certified : %s'
        % (zbad if zbad else 'NONE', zunc if zunc else 'NONE'))
    qpos = [r['a'] for r in rows if r['gate_q']['certified'] and r['gate_q']['sign'] == '+']
    qunc = [r['a'] for r in rows if not r['gate_q']['certified']]
    q3pos = [r['a'] for r in rows if r['gate_q_b325']['certified'] and r['gate_q_b325']['sign'] == '+']
    rec('  ### THE EPSTEIN SIGN, DERIVED KERNEL : certified POSITIVE at %s ; not certified at %s'
        % (qpos if qpos else 'NONE', qunc if qunc else 'NONE'))
    rec('  ### THE EPSTEIN SIGN, b325 KERNEL   : certified POSITIVE at %s' % (q3pos if q3pos else 'NONE'))
    crossing = qpos[0] if qpos else None
    rec('  ### ### **THE CROSSING CELL, FROM THE NUMBERS (derived kernel) : %s**'
        % (('a = %g' % crossing) if crossing is not None else 'NO CROSSING AT THIS REACH'))
    out = dict(cells=cells, n_finite=N, umax=UMAX, sign_margin=SIGN_MARGIN, rows=rows,
               zeta_control_positive=zbad, zeta_uncertified=zunc,
               epstein_positive=qpos, epstein_uncertified=qunc,
               epstein_positive_b325_kernel=q3pos, crossing=crossing,
               worst_routes=dict(hhat=worst_h, arch_z=worst_az, arch_q=worst_aq, prime_z=worst_pz),
               fixtures=arms)
    open(OUT_JSON + '.tmp', 'wb').write((json.dumps(out, indent=1, default=float) + '\n').encode('utf-8'))
    os.replace(OUT_JSON + '.tmp', OUT_JSON)
    rec('  written : %s' % os.path.basename(OUT_JSON))
    rec('=' * 100)
    io.open(OUT_TXT, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    return 0 if not zbad else 1


if __name__ == '__main__':
    sys.exit(main())
