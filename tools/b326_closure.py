# -*- coding: utf-8 -*-
"""b326_closure.py -- THE CORROBORATION: THE EXPLICIT FORMULA CLOSED AT EVERY CELL FOR BOTH
### FUNCTIONS WITH THEIR OWN ZERO LIBRARIES; THEN THE VERDICT, AT EXACTLY ITS SCOPE.

### ### **THE ZERO SIDE.** ### zeta: `2 SUM hhat(gamma)` over the atlas's ten thousand banked
### ordinates. ### Epstein: `2 SUM hhat(gamma)` over the on-line library of `b326_zeros.py`, PLUS
### the two banked off-line zeros as the FOUR complex terms they are -- `f~(rho)` at `beta + i
### gamma`, `beta - i gamma`, `1 - beta + i gamma`, `1 - beta - i gamma`, with `f~(rho) = INT w(v)
### e^{(rho - 1/2) v} dv` -- each printed, their sum printed beside the on-line sum.
### ### **TWO ROUTES SHARING NO CODE** for every transform: `b321_window.hhat_blocked` and this
### act's Simpson transform (`b326_windows.hhat_simpson`).
### ### **THE TRUNCATION BOUND, TWO ROUTES, THE LARGER USED:** ### `2 INT_T^inf |hhat| dN` against
### the function's own zero density, and the atlas's own `trunc_bound` form.
### ### **THE CLOSURE BAR, FROM THE SEALED REGISTRATION (section (5)):** ### a cell CLOSES when
### `|r| <= tail + 10 x drift + 1e-9`; a cell whose tail exceeds `1e-3 x max(|P|, |PR|, |A|, 1)`
### is BEYOND THE CEILING; a cell below the ceiling that misses the bar is a CLOSURE FAILURE, and
### the link is walked: the kernel normalization first (both kernels are closed side by side).
### ### **THE VERDICT BRANCHES ARE THE ORDER'S THREE, APPLIED TO THE ARC'S FAMILY;** ### the AIMED
### family (registration section (6)) is run with the same gate, closure and zeta control and is
### printed on its own line, never merged.
"""
import io
import json
import math
import multiprocessing as mpr
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import carto_atlas as AT        # noqa: E402
import b321_window as WI        # noqa: E402
import b326_windows as BW       # noqa: E402  ### the cells, the channels, the gate, the transform
import b317_smear as SM         # noqa: E402
import b318_square as SQ        # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
LIB = os.environ.get('B326_LIB', os.path.join(D, 'b326_epstein_zeros.json'))   # ### env: SMOKE only
WIN = os.path.join(D, 'b326_windows.json')
OUT_JSON = os.path.join(D, 'b326_closure.json')
OUT_TXT = os.path.join(D, 'b326_closure_run.txt')

DISC = 23
CEILING_REL = 1e-3
DRIFT_MULT = 10.0
BAR_ABS = 1e-9
AIMED_CELLS = (8.0, 16.0, 32.0, 64.0)


FINE_DV = 1e-4          # ### the autocorrelation's native grid (8193 points) aliases zeta's high ordinates:
                        # ### 2 pi / dv_native ~ 2300 at a = 16, and zeros near 2300 k land on hhat's main lobe.
                        # ### At dv = 1e-4 the alias period is 62800, six times the top ordinate.


def fine(v, w, dv=FINE_DV):
    """### resample (v, w) onto a uniform grid of spacing dv (the native grid interpolated)."""
    n = int(round((float(v[-1]) - float(v[0])) / dv)) + 1
    if n % 2 == 0:
        n += 1
    vv = np.linspace(float(v[0]), float(v[-1]), n)
    return vv, np.interp(vv, v, w, left=0.0, right=0.0)


def kernel_far(kind, U):
    from mpmath import mp, digamma, mpc, re as mre
    mp.dps = 15
    if kind == 'z':
        return np.array([float(mre(digamma(mpc(0.25, uu / 2.0)))) for uu in U]) - math.log(math.pi)
    k = 2.0 * np.array([float(mre(digamma(mpc(0.5, uu)))) for uu in U]) - 2.0 * math.log(2.0 * math.pi / math.sqrt(DISC))
    return k if kind == 'q' else 0.5 * k


def arch_tail(vf, wf, kind, umax=BW.UMAX, factor=20.0, n=4001):
    """### the archimedean channel's u-RANGE truncation: 2 INT_{|u| > UMAX} |hhat| |kernel| du / 2 pi,
    ### by two transform routes; the registration's list of truncations did not name this one and
    ### the act adds it -- a bound the seat omitted, measured rather than waved."""
    U = np.linspace(umax, factor * umax, n)
    k = np.abs(kernel_far(kind, U))
    # ### the two exact arrangements; a quadrature rule at `u dv ~ 1` is not a transform (the banked
    # ### rows of the first assembly carried a Simpson route reading 1.5 at a = 100 from exactly this).
    h1 = np.abs(hhat_exact(vf, wf, U))
    h2 = np.abs(hhat_exact2(vf, wf, U))
    r1 = 2.0 * float(np.trapezoid(h1 * k, U)) / (2.0 * math.pi)
    r2 = 2.0 * float(np.trapezoid(h2 * k, U)) / (2.0 * math.pi)
    return dict(route1=r1, route2=r2, used=max(r1, r2))


# ### ==============================================================================================
# ### THE EXACT TRANSFORM. ### `f`'s `w` is PIECEWISE LINEAR on a uniform grid (b318's autocorrelation
# ### is formed on one), so `INT w(v) e^{c v} dv` has a closed form: with `beta_j = (w_{j+1} - w_j)/dv`
# ### and `w` vanishing at both ends, it is `-(1/c^2) SUM_j beta_j (e^{c v_{j+1}} - e^{c v_j})`.
# ### ### **WHY QUADRATURE IS NOT USED FOR THE ZERO SIDE:** ### the first run of this tool summed
# ### `hhat` over zeta's ten thousand ordinates by the trapezoid rule on the native grid, whose
# ### alias period `2 pi / dv` (about 2300 at `a = 16`) folds ordinates near its multiples onto the
# ### main lobe -- the zero side read `7.40` where the places sum said `0.0034`. ### A fine grid at
# ### `dv = 1e-4` removes the aliasing and leaves the trapezoid and Simpson rules disagreeing at
# ### `1e-6` near `gamma = 10^4` (ten points per period). ### The closed form has neither defect;
# ### it is evaluated in TWO arrangements that share no code -- the product form in real cosines,
# ### and the telescoped complex-exponential form -- and the registered quadrature pair is kept as
# ### a check on the range where it is valid. ### **THIS IS A DECLARED CHANGE OF METHOD.**
# ### ==============================================================================================
def _segments(v, w):
    v = np.asarray(v, dtype=np.float64)
    w = np.asarray(w, dtype=np.float64)
    dv = float(v[1] - v[0])
    beta = (w[1:] - w[:-1]) / dv
    return v, dv, beta


def hhat_exact(v, w, G, block=128):
    """### ROUTE ONE (product form): hhat(g) = -(2 sin(g dv/2) / g^2) SUM_j beta_j sin(g (v_j + dv/2))."""
    v, dv, beta = _segments(v, w)
    mid = v[:-1] + dv / 2.0
    G = np.atleast_1d(np.asarray(G, dtype=np.float64))
    out = np.empty(G.size)
    for i in range(0, G.size, block):
        g = G[i:i + block]
        S = np.sin(np.outer(g, mid)) @ beta
        gs = np.where(np.abs(g) < 1e-9, 1.0, g)
        out[i:i + block] = -2.0 * np.sin(gs * dv / 2.0) / (gs * gs) * S
    # ### at g = 0 the closed form is 0/0; the limit is INT w dv, for which the trapezoid rule is EXACT on
    # ### a piecewise-linear w. ### The u-grids of this act contain u = 0.
    out[np.abs(G) < 1e-9] = float(np.trapezoid(np.asarray(w, dtype=np.float64), v))
    return out


def mellin_exact(v, w, C, block=128):
    """### ROUTE TWO (telescoped complex form): INT w e^{c v} dv = -(1/c^2) SUM_j beta_j (e^{c v_{j+1}} - e^{c v_j}),
    ### for complex `c`; `hhat(g)` is its real part at `c = i g`, and `f~(rho)` is its value at `c = rho - 1/2`."""
    v, dv, beta = _segments(v, w)
    C = np.atleast_1d(np.asarray(C, dtype=np.complex128))
    out = np.empty(C.size, dtype=np.complex128)
    for i in range(0, C.size, block):
        c = C[i:i + block]
        E = np.exp(np.outer(c, v))
        D = E[:, 1:] - E[:, :-1]
        out[i:i + block] = -(D @ beta.astype(np.complex128)) / (c * c)
    return out


def hhat_exact2(v, w, G, block=128):
    """### ROUTE TWO (difference of cosines): hhat(g) = (1/g^2) SUM_j beta_j (cos(g v_{j+1}) - cos(g v_j)),
    ### one cosine matrix per block, differenced along v -- the real part of `mellin_exact` at `c = i g`,
    ### written without the complex exponential."""
    v, dv, beta = _segments(v, w)
    G = np.atleast_1d(np.asarray(G, dtype=np.float64))
    out = np.empty(G.size)
    for i in range(0, G.size, block):
        g = G[i:i + block]
        Cm = np.cos(np.outer(g, v))
        gs = np.where(np.abs(g) < 1e-9, 1.0, g)
        out[i:i + block] = ((Cm[:, 1:] - Cm[:, :-1]) @ beta) / (gs * gs)
    out[np.abs(G) < 1e-9] = float(np.trapezoid(np.asarray(w, dtype=np.float64), v))
    return out


def density_zeta(g):
    return np.log(np.maximum(g, 2.0 * math.pi + 1e-9) / (2.0 * math.pi)) / (2.0 * math.pi)


def density_q(g):
    return np.log(np.maximum(g * math.sqrt(DISC) / (2.0 * math.pi), 1.0 + 1e-9)) / math.pi


def tail_bounds(v, w, T, dens, span=600.0, n=6001):
    """### two routes: the density integral, and the atlas's own max-times-span form."""
    G = np.linspace(T, T + span, n)
    h1 = hhat_exact(v, w, G)
    h2 = hhat_exact2(v, w, G)
    r1 = 2.0 * float(np.trapezoid(np.abs(h1) * dens(G), G))
    r1b = 2.0 * float(np.trapezoid(np.abs(h2) * dens(G), G))
    G2 = np.linspace(T, T + 200.0, 401)
    r2 = float(2.0 * np.max(np.abs(hhat_exact(v, w, G2))) * 200.0)
    return dict(density_route=r1, density_route2=r1b, atlas_form=r2, used=max(r1, r2))


def ftilde(v, w, rho):
    """### `f~(rho) = INT w(v) e^{(rho - 1/2) v} dv`, complex, by trapezoid and by Simpson."""
    c = complex(rho) - 0.5
    t2 = complex(mellin_exact(v, w, np.array([c]))[0])
    # ### route one for a complex exponent: the product form generalised, sinh in place of sin.
    vv, dv, beta = _segments(v, w)
    mid = vv[:-1] + dv / 2.0
    t1 = complex(-(2.0 * np.sinh(c * dv / 2.0) / (c * c)) * np.sum(beta * np.exp(c * mid)))
    return t1, t2


def zero_sides(f, lib, offline=None, check=False):
    v, w = f.v, f.w
    offline = lib['offline'] if offline is None else offline
    G = np.asarray(AT.GAM, dtype=np.float64)
    zz1 = 2.0 * float(np.sum(hhat_exact(v, w, G)))
    zz2 = 2.0 * float(np.sum(hhat_exact2(v, w, G)))
    # ### the registered quadrature pair, on the range where its grid resolves the oscillation:
    Glo = G[G <= 1000.0]
    if check:
        vf, wf = fine(v, w)
        q1 = 2.0 * float(np.sum(WI.hhat_blocked(vf, wf, Glo)))
        q2 = 2.0 * float(np.sum(BW.hhat_simpson(vf, wf, Glo, block=64)))
        e1 = 2.0 * float(np.sum(hhat_exact(v, w, Glo)))
    else:
        q1 = q2 = e1 = float('nan')
    gq = np.array([z['gamma_a'] for z in lib['zeros']], dtype=np.float64)
    gqb = np.array([z['gamma_b'] for z in lib['zeros']], dtype=np.float64)
    zq1 = 2.0 * float(np.sum(hhat_exact(v, w, gq))) if gq.size else 0.0
    zq2 = 2.0 * float(np.sum(hhat_exact2(v, w, gq))) if gq.size else 0.0
    zqb = 2.0 * float(np.sum(hhat_exact(v, w, gqb))) if gqb.size else 0.0
    off = []
    off_sum1 = 0.0 + 0.0j
    off_sum2 = 0.0 + 0.0j
    for o in offline:
        beta, gam = o['rho_a']
        for rho in (complex(beta, gam), complex(beta, -gam), complex(1 - beta, gam), complex(1 - beta, -gam)):
            t1, t2 = ftilde(v, w, rho)
            off.append(dict(rho=[rho.real, rho.imag], term=[t1.real, t1.imag], term_route2=[t2.real, t2.imag]))
            off_sum1 += t1
            off_sum2 += t2
    return dict(zero_z=zz1, zero_z_route2=zz2, zero_q_on=zq1, zero_q_on_route2=zq2, zero_q_on_gamma_b=zqb,
                quad_check=dict(trapezoid=q1, simpson=q2, exact=e1, up_to=1000.0),
                offline_terms=off, offline_sum=[off_sum1.real, off_sum1.imag],
                offline_sum_route2=[off_sum2.real, off_sum2.imag],
                zero_q=zq1 + off_sum1.real)


NV_FINE = 32769         # ### four times b318's default correlation grid (8193) -- see the note below


def channels_exact(v, w, lib, offline, refine=True):
    """### every channel of the explicit formula on the piecewise-linear (v, w), by the exact transform:
    ### the zero sides (zeta; Epstein on-line; the off-line four-term sums), the pole term, the three
    ### archimedean channels at two u-grids, and the two finite sides."""
    L = float(v[-1])
    zs = zero_sides_on(v, w, lib, offline)
    U1 = BW.ugrid(L, 1)
    h1 = hhat_exact(v, w, U1)
    Az = float(np.trapezoid(h1 * BW.kernel_zeta(U1), U1) / (2.0 * math.pi))
    Aq = float(np.trapezoid(h1 * BW.kernel_q_derived(U1), U1) / (2.0 * math.pi))
    Aq3 = float(np.trapezoid(h1 * BW.kernel_q_b325(U1), U1) / (2.0 * math.pi))
    if refine:
        U2 = BW.ugrid(L, 2)
        h2 = hhat_exact(v, w, U2)
        Az2 = float(np.trapezoid(h2 * BW.kernel_zeta(U2), U2) / (2.0 * math.pi))
        Aq2 = float(np.trapezoid(h2 * BW.kernel_q_derived(U2), U2) / (2.0 * math.pi))
        Aq32 = float(np.trapezoid(h2 * BW.kernel_q_b325(U2), U2) / (2.0 * math.pi))
    else:
        Az2, Aq2, Aq32 = Az, Aq, Aq3
    P = float(np.real(mellin_exact(v, w, np.array([0.5 + 0j]))[0] + mellin_exact(v, w, np.array([-0.5 + 0j]))[0]))
    PRz, _t = WI.prime_sum(v, w, 'corpus')
    PRq, _n = BW.epstein_finite(v, w, _LAMQ)
    return dict(L=L, dv=float(v[1] - v[0]), pole=P, arch_z=Az, arch_q=Aq, arch_q_b325=Aq3,
                udrift_z=abs(Az2 - Az), udrift_q=abs(Aq2 - Aq), udrift_q3=abs(Aq32 - Aq3),
                prime_z=PRz, finite_q=PRq, zero=zs)


def zero_sides_on(v, w, lib, offline, base=None):
    """### with `base` given (a zero_sides result on the same grid), only the off-line terms are re-formed."""
    if base is None:
        return zero_sides(SM.TestFunction('x', v, w, 'x'), lib, offline)
    off, s1, s2 = [], 0.0 + 0.0j, 0.0 + 0.0j
    for o in offline:
        beta, gam = o['rho_a']
        for rho in (complex(beta, gam), complex(beta, -gam), complex(1 - beta, gam), complex(1 - beta, -gam)):
            t1, t2 = ftilde(v, w, rho)
            off.append(dict(rho=[rho.real, rho.imag], term=[t1.real, t1.imag], term_route2=[t2.real, t2.imag]))
            s1 += t1
            s2 += t2
    out = dict(base)
    out.update(offline_terms=off, offline_sum=[s1.real, s1.imag], offline_sum_route2=[s2.real, s2.imag],
               zero_q=base['zero_q_on'] + s1.real)
    return out


_LAMQ = None


def closure_row(a, seed, ch_windows, lib, offl_all=None, deficit=0, sig_hi=1.5):
    """### ### **THE CLOSURE AT ONE CELL, ON ONE `f`, AT TWO CORRELATION GRIDS.**

    ### `f = autocorrelation(seed)` is piecewise linear on b318's uniform grid, and its transform has
    ### alias peaks at every multiple of `2 pi / dv` (about `8300` at `a = 22` on the default grid):
    ### exact copies of the main lobe scaled by `(gamma'/gamma)^2`. ### The peaks inside zeta's library
    ### are summed exactly; the ones beyond it are a real part of the zero side that no window of 600
    ### above the library's top can see -- the first run of the corrected tool measured `+1.3e-06` at
    ### `a = 22` from exactly this. ### **SO THE CLOSURE IS TAKEN ON THE SAME CONSTRUCTION AT FOUR TIMES
    ### ### THE CORRELATION GRID** (the first alias peak moves to `~33000` at `a = 22`), AND EVERY
    ### CHANNEL IS ALSO FORMED ON THE DEFAULT GRID, so that the `v`-grid drift enters the bar exactly
    ### as the `u`-grid drift does. ### The windows' channels (default grid, trapezoid transform) are
    ### reported beside both; the certified SIGNS are the windows', and they are not touched here."""
    global _LAMQ
    if _LAMQ is None:
        _LAMQ = BW.lambda_q_sieve(int(400.0 * 400.0) + 2)
    fc = SQ.autocorrelation(seed)
    ff = SQ.autocorrelation(seed, nv=NV_FINE)
    offl_two = lib['offline']
    cc = channels_exact(fc.v, fc.w, lib, offl_two, refine=False)
    cf = channels_exact(ff.v, ff.w, lib, offl_two)
    zs = cf['zero']
    zs_all = zero_sides_on(ff.v, ff.w, lib, offl_all, base=zs) if offl_all is not None else None
    zc_all = zero_sides_on(fc.v, fc.w, lib, offl_all, base=cc['zero']) if offl_all is not None else None
    v, w = ff.v, ff.w
    # ### the deficit bound (zero once the census reaches the library's top).
    G = np.linspace(60.0, float(lib['T']), 2001)
    hm = float(np.max(np.abs(hhat_exact(v, w, G))))
    deficit_bound = 4.0 * deficit * hm * math.cosh((sig_hi - 0.5) * float(v[-1]))
    Tz = float(AT.GAM[-1])
    Tq = float(lib['T'])
    tz = tail_bounds(v, w, Tz, density_zeta)
    tq = tail_bounds(v, w, Tq, density_q)
    at_z = arch_tail(v, w, 'z')
    at_q = arch_tail(v, w, 'q')
    at_q3 = arch_tail(v, w, 'q325')
    P, PRz, Az = cf['pole'], cf['prime_z'], cf['arch_z']
    PRq, Aq, Aq3 = cf['finite_q'], cf['arch_q'], cf['arch_q_b325']
    rz = zs['zero_z'] - (P - PRz + Az)
    rq = zs['zero_q'] - (P - PRq + Aq)
    rq3 = zs['zero_q'] - (P - PRq + Aq3)
    rq_all = (zs_all['zero_q'] - (P - PRq + Aq)) if zs_all is not None else None
    rq3_all = (zs_all['zero_q'] - (P - PRq + Aq3)) if zs_all is not None else None
    # ### the v-grid drift, channel by channel, between the default and the fine correlation grids.
    vd_z = abs(cf['zero']['zero_z'] - cc['zero']['zero_z']) + abs(PRz - cc['prime_z']) + abs(Az - cc['arch_z']) + abs(P - cc['pole'])
    zq_c = (zc_all['zero_q'] if zc_all is not None else cc['zero']['zero_q'])
    zq_f = (zs_all['zero_q'] if zs_all is not None else zs['zero_q'])
    vd_q = abs(zq_f - zq_c) + abs(PRq - cc['finite_q']) + abs(Aq - cc['arch_q']) + abs(P - cc['pole'])
    vd_q3 = abs(zq_f - zq_c) + abs(PRq - cc['finite_q']) + abs(Aq3 - cc['arch_q_b325']) + abs(P - cc['pole'])
    scale_z = max(abs(P), abs(PRz), abs(Az), 1.0)
    scale_q = max(abs(P), abs(PRq), abs(Aq), 1.0)
    ceil_z = (tz['used'] + at_z['used']) > CEILING_REL * scale_z
    ceil_q = (tq['used'] + at_q['used'] + deficit_bound) > CEILING_REL * scale_q
    bar_z = tz['used'] + at_z['used'] + DRIFT_MULT * (cf['udrift_z'] + vd_z) + BAR_ABS
    bar_q = tq['used'] + at_q['used'] + DRIFT_MULT * (cf['udrift_q'] + vd_q) + BAR_ABS + deficit_bound
    bar_q3 = tq['used'] + at_q3['used'] + DRIFT_MULT * (cf['udrift_q3'] + vd_q3) + BAR_ABS + deficit_bound

    def status(r, bar, ceil):
        if ceil:
            return 'BEYOND CEILING'
        return 'CLOSES' if abs(r) <= bar else 'FAILS'
    return dict(a=a, zero=zs, zero_all=zs_all, tail_z=tz, tail_q=tq, deficit_bound=deficit_bound,
                arch_tail_z=at_z, arch_tail_q=at_q, arch_tail_q_b325=at_q3,
                fine=dict(nv=NV_FINE, dv=cf['dv'], pole=P, arch_z=Az, arch_q=Aq, arch_q_b325=Aq3, prime_z=PRz, finite_q=PRq,
                          udrift_z=cf['udrift_z'], udrift_q=cf['udrift_q'], udrift_q3=cf['udrift_q3']),
                coarse=dict(nv=8193, dv=cc['dv'], pole=cc['pole'], arch_z=cc['arch_z'], arch_q=cc['arch_q'],
                            arch_q_b325=cc['arch_q_b325'], prime_z=cc['prime_z'], finite_q=cc['finite_q'],
                            zero_z=cc['zero']['zero_z'], zero_q=zq_c),
                vdrift=dict(z=vd_z, q=vd_q, q3=vd_q3),
                windows=(dict(pole=ch_windows['pole'], arch_z=ch_windows['arch_z'], arch_q=ch_windows['arch_q'],
                              arch_q_b325=ch_windows['arch_q_b325'], prime_z=ch_windows['prime_z'], finite_q=ch_windows['finite_q'])
                         if ch_windows is not None else None),
                residual_z=rz, residual_q=rq, residual_q_b325=rq3,
                residual_q_all=rq_all, residual_q_b325_all=rq3_all,
                status_q_all=(status(rq_all, bar_q, ceil_q) if rq_all is not None else None),
                status_q_b325_all=(status(rq3_all, bar_q3, ceil_q) if rq3_all is not None else None),
                bar_z=bar_z, bar_q=bar_q, bar_q_b325=bar_q3,
                status_z=status(rz, bar_z, ceil_z), status_q=status(rq, bar_q, ceil_q),
                status_q_b325=status(rq3, bar_q3, ceil_q),
                missing_half=rq3 - rq,
                offline_share=(zs['offline_sum'][0] / zs['zero_q']) if zs['zero_q'] else float('nan'))


def refresh_bars(rc, seed):
    """### recompute the arch u-tails with the corrected routes and re-derive every bar and status
    ### of a banked row; every other component is kept as banked."""
    ff = SQ.autocorrelation(seed, nv=NV_FINE)
    v, w = ff.v, ff.w
    rc['arch_tail_z'] = arch_tail(v, w, 'z')
    rc['arch_tail_q'] = arch_tail(v, w, 'q')
    rc['arch_tail_q_b325'] = arch_tail(v, w, 'q325')
    P, PRz, Az = rc['fine']['pole'], rc['fine']['prime_z'], rc['fine']['arch_z']
    PRq, Aq = rc['fine']['finite_q'], rc['fine']['arch_q']
    scale_z = max(abs(P), abs(PRz), abs(Az), 1.0)
    scale_q = max(abs(P), abs(PRq), abs(Aq), 1.0)
    tz, tq, dfb = rc['tail_z']['used'], rc['tail_q']['used'], rc['deficit_bound']
    ceil_z = (tz + rc['arch_tail_z']['used']) > CEILING_REL * scale_z
    ceil_q = (tq + rc['arch_tail_q']['used'] + dfb) > CEILING_REL * scale_q
    rc['bar_z'] = tz + rc['arch_tail_z']['used'] + DRIFT_MULT * (rc['fine']['udrift_z'] + rc['vdrift']['z']) + BAR_ABS
    rc['bar_q'] = tq + rc['arch_tail_q']['used'] + DRIFT_MULT * (rc['fine']['udrift_q'] + rc['vdrift']['q']) + BAR_ABS + dfb
    rc['bar_q_b325'] = tq + rc['arch_tail_q_b325']['used'] + DRIFT_MULT * (rc['fine']['udrift_q3'] + rc['vdrift']['q3']) + BAR_ABS + dfb

    def status(r, bar, ceil):
        if ceil:
            return 'BEYOND CEILING'
        return 'CLOSES' if abs(r) <= bar else 'FAILS'
    rc['status_z'] = status(rc['residual_z'], rc['bar_z'], ceil_z)
    rc['status_q'] = status(rc['residual_q'], rc['bar_q'], ceil_q)
    rc['status_q_b325'] = status(rc['residual_q_b325'], rc['bar_q_b325'], ceil_q)
    if rc.get('residual_q_all') is not None:
        rc['status_q_all'] = status(rc['residual_q_all'], rc['bar_q'], ceil_q)
        rc['status_q_b325_all'] = status(rc['residual_q_b325_all'], rc['bar_q_b325'], ceil_q)
    rc['bars_refreshed'] = True
    return rc


_W = {}


def _winit(lib, offl_all, deficit, sig_hi):
    _W.update(lib=lib, offl_all=offl_all, deficit=deficit, sig_hi=sig_hi)


def _wcell(args):
    a, kind, ch, omega = args
    seed = SM.mean_zero_variant(a) if kind == 'arc' else BW.aimed_variant(a, omega)
    rc = closure_row(a, seed, ch, _W['lib'], _W['offl_all'], _W['deficit'], _W['sig_hi'])
    return (a, kind, rc)


def verdict(rows_w, rows_c):
    """### the order's three branches, from certified signs and closures."""
    cert_pos = []
    for rw, rc in zip(rows_w, rows_c):
        if rw['gate_q']['certified'] and rw['gate_q']['sign'] == '+':
            cert_pos.append((rw['a'], rc))
    sees = [(a, rc) for a, rc in cert_pos
            if (rc['status_q_all'] or rc['status_q']) == 'CLOSES' and rc['status_z'] == 'CLOSES']
    if sees:
        a, rc = sees[0]
        rw = next(r for r in rows_w if r['a'] == a)
        zeta_ok = rw['gate_z']['certified'] and rw['gate_z']['sign'] == '-'
        if zeta_ok:
            return 'SEES IT', a, rc
        return 'PARTIAL', a, rc
    if cert_pos:
        return 'PARTIAL', cert_pos[0][0], cert_pos[0][1]
    return 'DOES NOT SEE IT', None, None


def main():
    lines = []

    def rec(s=''):
        lines.append(s)
        print(s, flush=True)

    rec('=' * 100)
    rec('b326 -- THE CORROBORATION. ### THE EXPLICIT FORMULA CLOSED FOR BOTH; THEN THE VERDICT.')
    rec('=' * 100)
    lib = json.load(io.open(LIB, encoding='utf-8'))
    win = json.load(io.open(WIN, encoding='utf-8'))
    OFF = os.path.join(D, 'b326_offline.json')
    off = json.load(io.open(OFF, encoding='utf-8')) if os.path.exists(OFF) else None
    offl_all, deficit, sig_hi = None, 0, 1.5
    if off is not None:
        offl_all = [dict(rho_a=z['rho_a']) for z in off['zeros']]
        sig_hi = off['sig_hi']
        nt = lib['rvm_main_term']
        n_exact = len(lib['zeros']) + 2 * int(round(off['total_winding']))
        if off['T'] >= lib['T'] - 1e-9:
            deficit = 0     # ### the census covers the whole strip to the library's top: nothing unlocated
            rec('  the census reaches the library top: N(%g) by the argument principle = %d on the line + 2 x %d off'
                ' = %d, against the main term %.1f (the difference is S(T) and the constant term, as it should be)'
                % (lib['T'], len(lib['zeros']), int(round(off['total_winding'])), n_exact, nt))
        else:
            deficit = max(0, int(round(nt - len(lib['zeros']) - 2 * len(offl_all))))
        rec('  completeness census : sigma in [%.2f, %.2f] to t = %g ; off-line zeros located %d (banked 2 reappear: %d of 2) ;'
            ' main term %.1f against on-line %d + 2 x %d off-line -> unlocated deficit taken as %d'
            % (off['sig_lo'], off['sig_hi'], off['T'], len(offl_all), off['banked_reappear'], nt, len(lib['zeros']),
               len(offl_all), deficit))
    rec('  Epstein library : T = %g, on-line zeros %d, off-line %d, dps %d, K %d, box mismatches %d'
        % (lib['T'], len(lib['zeros']), len(lib['offline']), lib['dps'], lib['K'], lib['box_mismatches']))
    rec('  zeta library    : %d ordinates, last %.4f' % (len(AT.GAM), float(AT.GAM[-1])))
    # ### fixture: the four-term off-line sum is REAL (the conjugate pairs cancel the imaginary part).
    f0 = BW.cell_function(3.0)
    zs0 = zero_sides(f0, lib, check=True)
    rec('  (i) the off-line four-term sum at a = 3 is real : imag %.3e (route 2 %.3e)'
        % (zs0['offline_sum'][1], zs0['offline_sum_route2'][1]))
    rec('  (ii) zero side, the two EXACT arrangements at a = 3 : zeta %.12f vs %.12f ; Epstein on-line %.12f vs %.12f'
        % (zs0['zero_z'], zs0['zero_z_route2'], zs0['zero_q_on'], zs0['zero_q_on_route2']))
    qc = zs0['quad_check']
    rec('  (iii) the registered quadrature pair against the exact form, zeta ordinates <= %g : trapezoid %.12f, Simpson %.12f, exact %.12f'
        % (qc['up_to'], qc['trapezoid'], qc['simpson'], qc['exact']))
    f16 = BW.cell_function(16.0)
    G16 = np.asarray(AT.GAM, dtype=np.float64)
    nat = 2.0 * float(np.sum(WI.hhat_blocked(f16.v, f16.w, G16)))
    exa = 2.0 * float(np.sum(hhat_exact(f16.v, f16.w, G16)))
    rec('  (iv) the aliasing the first run suffered, reproduced: zeta zero side at a = 16 on the native grid %.6f, exact %.9f'
        ' (places sum -0.003447230)' % (nat, exa))
    fx = (abs(zs0['offline_sum'][1]) < 1e-12 and abs(zs0['zero_z'] - zs0['zero_z_route2']) < 1e-9
          and abs(zs0['zero_q_on'] - zs0['zero_q_on_route2']) < 1e-9
          # ### the trapezoid rule on the fine grid sits at 1e-9 of the exact form; Simpson's alternating
          # ### fourth-order weights meet a kink at every node of a piecewise-linear w and sit at 5e-8.
          and abs(qc['trapezoid'] - qc['exact']) < 1e-8 and abs(qc['simpson'] - qc['exact']) < 1e-7
          and abs(nat) > 1.0 and abs(exa - 0.003447230) < 1e-5)
    rec('  ### FIXTURES : %s' % ('PASS' if fx else '### FAIL ###'))
    if not fx:
        return 2

    rows_c = []
    BANKC = os.path.join(D, 'b326_closure_bank.jsonl')
    got = {}
    if os.path.exists(BANKC):
        for ln in io.open(BANKC, encoding='utf-8'):
            if ln.strip():
                r = json.loads(ln)
                got[(r['kind'], r['a'])] = r['rc']
    jobs = [(rw['a'], 'arc', rw['coarse'], None) for rw in win['rows'] if ('arc', rw['a']) not in got]
    sel = os.environ.get('B326_CELLS')
    if sel:
        want = set(float(x) for x in sel.split(','))
        jobs = [j for j in jobs if j[0] in want]
    nproc = int(os.environ.get('B326_PROCS', 6))
    rec('  closure rows banked %d, to compute %d (a kill loses nothing: the bank resumes)' % (len(got), len(jobs)))
    ctx = mpr.get_context('spawn')
    if jobs:
        with ctx.Pool(processes=min(nproc, len(jobs)), initializer=_winit, initargs=(lib, offl_all, deficit, sig_hi)) as pool:
            for a, k, rc in pool.imap_unordered(_wcell, jobs):
                got[(k, a)] = rc
                with io.open(BANKC, 'a', encoding='utf-8', newline=chr(10)) as fh:
                    fh.write(json.dumps(dict(kind=k, a=a, rc=rc), default=float) + chr(10))
                print('    banked closure row a = %g' % a, flush=True)
    for (k, a), rc in list(got.items()):
        if not rc.get('bars_refreshed'):
            seed = SM.mean_zero_variant(a) if k == 'arc' else BW.aimed_variant(a, lib['offline'][0]['rho_a'][1])
            got[(k, a)] = refresh_bars(rc, seed)
    missing = [rw['a'] for rw in win['rows'] if ('arc', rw['a']) not in got]
    if missing:
        print('  arc cells still unbanked: %s -- nothing assembled this invocation' % missing, flush=True)
        return 3
    rec('')
    rec('  %-6s %-14s %-14s %-11s %-16s %-14s %-11s %-16s %-14s %-11s'
        % ('a', 'zeta zero', 'zeta resid', 'zeta bar', 'zeta status', 'Q zero', 'Q resid', 'Q bar',
           'Q status', 'Q resid(b325 k)'))
    for rw in win['rows']:
        a = rw['a']
        rc = got[('arc', a)]
        rows_c.append(rc)
        rec('  %-6g %-14.9f %-+14.3e %-11.2e %-16s %-14.9f %-+11.3e %-16.2e %-14s %-+11.3e %s'
            % (a, rc['zero']['zero_z'], rc['residual_z'], rc['bar_z'], rc['status_z'],
               rc['zero']['zero_q'], rc['residual_q'], rc['bar_q'], rc['status_q'],
               rc['residual_q_b325'], rc['status_q_b325']))
        rec('         bars: zeta zero-tail %.1e + arch u-tail %.1e + 10 x (u-drift %.1e + v-drift %.1e) ; Epstein zero-tail %.1e'
            ' + arch u-tail %.1e + 10 x (u-drift %.1e + v-drift %.1e) + deficit %.1e | fine minus windows: arch_z %+.1e arch_q %+.1e prime_z %+.1e finite_q %+.1e'
            % (rc['tail_z']['used'], rc['arch_tail_z']['used'], rc['fine']['udrift_z'], rc['vdrift']['z'], rc['tail_q']['used'],
               rc['arch_tail_q']['used'], rc['fine']['udrift_q'], rc['vdrift']['q'], rc['deficit_bound'],
               rc['fine']['arch_z'] - rc['windows']['arch_z'], rc['fine']['arch_q'] - rc['windows']['arch_q'],
               rc['fine']['prime_z'] - rc['windows']['prime_z'], rc['fine']['finite_q'] - rc['windows']['finite_q']))
        if rc['zero_all'] is not None:
            rec('         with EVERY located off-line zero : Q zero %.9f  resid %+.3e %s | b325 kernel resid %+.3e %s | deficit bound %.2e'
                % (rc['zero_all']['zero_q'], rc['residual_q_all'], rc['status_q_all'],
                   rc['residual_q_b325_all'], rc['status_q_b325_all'], rc['deficit_bound']))
    rec('')
    rec('  ### THE OFF-LINE TERMS, THE FOUR COMPLEX TERMS THEY ARE, AT THREE CELLS:')
    for rc in rows_c:
        if rc['a'] in (1.3, 3.0, 22.0):
            rec('    a = %g : on-line sum %.9f ; off-line sum %.9f %+.2ei (route 2 %.9f) ; off-line share of Z_Q %.3e'
                % (rc['a'], rc['zero']['zero_q_on'], rc['zero']['offline_sum'][0], rc['zero']['offline_sum'][1],
                   rc['zero']['offline_sum_route2'][0], rc['offline_share']))
            for t in rc['zero']['offline_terms']:
                rec('      rho = %.6f %+.6fi : f~(rho) = %+.9e %+.9ei' % (t['rho'][0], t['rho'][1], t['term'][0], t['term'][1]))
    st_z = [rc['status_z'] for rc in rows_c]
    st_q = [rc['status_q'] for rc in rows_c]
    st_q3 = [rc['status_q_b325'] for rc in rows_c]
    st_qa = [rc['status_q_all'] for rc in rows_c if rc['status_q_all'] is not None]
    st_q3a = [rc['status_q_b325_all'] for rc in rows_c if rc['status_q_b325_all'] is not None]
    rec('')
    rec('  ### CLOSURE TALLY  zeta : %d CLOSES / %d FAILS / %d BEYOND CEILING'
        % (st_z.count('CLOSES'), st_z.count('FAILS'), st_z.count('BEYOND CEILING')))
    rec('  ### CLOSURE TALLY  Epstein, DERIVED kernel : %d CLOSES / %d FAILS / %d BEYOND CEILING'
        % (st_q.count('CLOSES'), st_q.count('FAILS'), st_q.count('BEYOND CEILING')))
    rec('  ### CLOSURE TALLY  Epstein, b325 kernel    : %d CLOSES / %d FAILS / %d BEYOND CEILING'
        % (st_q3.count('CLOSES'), st_q3.count('FAILS'), st_q3.count('BEYOND CEILING')))
    if st_qa:
        rec('  ### CLOSURE TALLY  Epstein, DERIVED kernel, EVERY located off-line zero : %d CLOSES / %d FAILS / %d BEYOND CEILING'
            % (st_qa.count('CLOSES'), st_qa.count('FAILS'), st_qa.count('BEYOND CEILING')))
        rec('  ### CLOSURE TALLY  Epstein, b325 kernel,    EVERY located off-line zero : %d CLOSES / %d FAILS / %d BEYOND CEILING'
            % (st_q3a.count('CLOSES'), st_q3a.count('FAILS'), st_q3a.count('BEYOND CEILING')))
    below = [rc for rc in rows_c if rc['status_q'] != 'BEYOND CEILING']
    if below:
        ratio = [rc['residual_q_b325'] / (rc['zero']['zero_q'] - (rc['zero']['zero_q'] - rc['residual_q'] - 0.0) + 1e-300) for rc in below]
        mh = [(rc['a'], rc['missing_half'], rc['residual_q_b325_all'] if rc['residual_q_b325_all'] is not None else rc['residual_q_b325']) for rc in below]
        rec('  ### THE LINK WALKED: with b325\'s kernel the residual at each cell below the ceiling equals A_q - A_q(b325)'
            ' to within the bar : %s'
            % all(abs(r3 - m) <= rc['bar_q_b325'] for (a, m, r3), rc in zip(mh, below)))
        del ratio
    # ### the verdict on the arc's family.
    v, acell, rc_v = verdict(win['rows'], rows_c)
    rec('')
    rec('  ### ### ### **VERDICT, THE ARC\'S FAMILY : %s**' % v)
    if acell is not None:
        rec('    at a = %g : Epstein places %+.9f (certified), closure %s, zeta places %+.9f, zeta closure %s'
            % (acell, next(r for r in win['rows'] if r['a'] == acell)['coarse']['places_q'],
               rc_v['status_q'], next(r for r in win['rows'] if r['a'] == acell)['coarse']['places_z'],
               rc_v['status_z']))
    else:
        # ### the reason named from the numbers.
        dom = []
        for rw, rc in zip(win['rows'], rows_c):
            c = rw['coarse']
            dom.append((rw['a'], c['finite_q'], c['arch_q'], rc['zero']['offline_sum'][0], rc['zero']['zero_q_on']))
        rec('    reason, from the numbers -- at every cell the places sum is PR_Q - A_Q with:')
        for a, prq, aq, offs, on in dom:
            rec('      a = %-6g finite %.9f  arch %.9f  -> places %+.9f ; zero side: on-line %.9f, off-line %+.3e'
                % (a, prq, aq, prq - aq, on, offs))

    # ### the AIMED family, on its own line.
    rec('')
    rec('  ### ### **THE AIMED FAMILY (registration section (6)) -- SEPARATE, LABELLED, NEVER MERGED.**')
    omega = lib['offline'][0]['rho_a'][1] if lib['offline'] else None
    aimed = []
    if omega is not None:
        N = int(max(AIMED_CELLS) ** 2) + 2
        lam_z = BW.von_mangoldt_sieve(N)
        lam_q = BW.lambda_q_sieve(N)
        rec('    omega = %.9f (the refined banked off-line height); cells %s' % (omega, list(AIMED_CELLS)))
        jobs_a = [(a, 'aimed', None, omega) for a in AIMED_CELLS if ('aimed', a) not in got]
        if sel:
            jobs_a = [j for j in jobs_a if j[0] in want]
        if jobs_a:
            with ctx.Pool(processes=4, initializer=_winit, initargs=(lib, offl_all, deficit, sig_hi)) as pool:
                for a, k, rc in pool.imap_unordered(_wcell, jobs_a):
                    got[(k, a)] = rc
                    with io.open(BANKC, 'a', encoding='utf-8', newline=chr(10)) as fh:
                        fh.write(json.dumps(dict(kind=k, a=a, rc=rc), default=float) + chr(10))
        if any(('aimed', a) not in got for a in AIMED_CELLS):
            print('  aimed cells still unbanked -- nothing assembled this invocation', flush=True)
            return 3
        got_a = {a: got[('aimed', a)] for a in AIMED_CELLS}
        WB = os.path.join(D, 'b326_closure_aimed_windows.json')
        wb = json.load(io.open(WB, encoding='utf-8')) if os.path.exists(WB) else {}
        for a in AIMED_CELLS:
            key = '%g' % a
            if key not in wb:
                f = BW.cell_function(a, aimed_omega=omega)
                wb[key] = dict(c1=BW.channels(f, lam_z, lam_q, refine=1), c4=BW.channels(f, lam_z, lam_q, refine=4))
                open(WB + '.tmp', 'wb').write((json.dumps(wb, indent=1, default=float) + chr(10)).encode('utf-8'))
                os.replace(WB + '.tmp', WB)
            c1, c4 = wb[key]['c1'], wb[key]['c4']
            gz = BW.certify(c1['places_z'], c4['places_z'])
            gq = BW.certify(c1['places_q'], c4['places_q'])
            gq3 = BW.certify(c1['places_q_b325'], c4['places_q_b325'])
            rc = got_a[a]
            rc['windows'] = dict(pole=c1['pole'], arch_z=c1['arch_z'], arch_q=c1['arch_q'], arch_q_b325=c1['arch_q_b325'],
                                 prime_z=c1['prime_z'], finite_q=c1['finite_q'])
            aimed.append(dict(a=a, coarse=c1, refined=c4, gate_z=gz, gate_q=gq, gate_q_b325=gq3, closure=rc))
            rec('    a = %-4g pole %.2e | zeta places %+.9f %s %s | Epstein places %+.9f %s %s (closure %s, resid %+.2e, bar %.2e) |'
                ' off-line share %+.3f'
                % (a, c1['pole'], c1['places_z'], gz['verdict'], gz['sign'], c1['places_q'], gq['verdict'], gq['sign'],
                   rc['status_q'], rc['residual_q'], rc['bar_q'], rc['offline_share']))
        rows_wa = [dict(a=x['a'], gate_q=x['gate_q'], gate_z=x['gate_z']) for x in aimed]
        rows_ca = [x['closure'] for x in aimed]
        va, aa, _ = verdict(rows_wa, rows_ca)
        rec('    ### ### **AIMED : %s%s**' % (va, (' at a = %g' % aa) if aa is not None else ''))
    else:
        va, aa = 'NOT RUN', None
        rec('    no off-line zero in the library; the aimed family is not run.')

    # ### the ceiling, printed.
    beyond_z = [rc['a'] for rc in rows_c if rc['status_z'] == 'BEYOND CEILING']
    beyond_q = [rc['a'] for rc in rows_c if rc['status_q'] == 'BEYOND CEILING']
    rec('')
    rec('  ### THE CEILING : Epstein library height T = %g ; widest cell a = %g ; finite side n_max = %d ;'
        ' cells beyond the ceiling -- zeta %s, Epstein %s'
        % (lib['T'], max(r['a'] for r in win['rows']), win['n_finite'],
           beyond_z if beyond_z else 'NONE', beyond_q if beyond_q else 'NONE'))
    out = dict(verdict=v, verdict_cell=acell, aimed_verdict=va, aimed_cell=aa, omega=omega,
               deficit=deficit, offline_located=(len(offl_all) if offl_all is not None else None),
               tally_all=dict(q=st_qa, q_b325=st_q3a),
               rows=rows_c, aimed=aimed, tally=dict(zeta=st_z, q=st_q, q_b325=st_q3),
               beyond_z=beyond_z, beyond_q=beyond_q)
    open(OUT_JSON + '.tmp', 'wb').write((json.dumps(out, indent=1, default=float) + '\n').encode('utf-8'))
    os.replace(OUT_JSON + '.tmp', OUT_JSON)
    rec('  written : %s' % os.path.basename(OUT_JSON))
    rec('=' * 100)
    io.open(OUT_TXT, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    return 0


if __name__ == '__main__':
    mpr.freeze_support()
    sys.exit(main())
