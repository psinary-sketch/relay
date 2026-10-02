# -*- coding: utf-8 -*-
"""b590_bench.py -- COMPONENT 4: THE KERNEL'S WITNESS WINDOW AGAINST THE BENCH, UNDER (R200)(4)(c). ### A READING.

### ### `python tools/b590_bench.py witness` -> data/b590_witness_vs_bench.txt / .json.
### The detector theorem (SIDE-explicit-formula Schema/Detector.lean, branch epstein-b590) names the window's base: the
### kernel's plateau at ramp fraction 1/2 and half-width w = baseWidth(rhoE) = 1 / (4 (|gammaOf rhoE| + 1)). Its power j and
### coefficient list a are existential; j = max J D in the converse (Converse.lean :172-:174), D from coeffs_exist
### (PowerLimit.lean :688): D = 2|VF| + 2 DK + DE, DK = natDegree Kp + 1 = |Xr| + 1, DE = natDegree Ep + 1 = 2.
### This bench computes, on the bench's zero list for Z_Q (Q0 = x^2 + xy + 6y^2, disc -23):
###   (1) the plateau's transform at gammaOf of every zero (mpmath quadrature), the scores, the dominant off-line orbit M,
###       the tie set T, the kill set K, VF, Xr, D;
###   (2) the witness's support half-width, at least 2^D w before the pairing (2^(D+1) w after it), against b522's plateau
###       half-width ln 33.194255 (relay data/b554_sign_pattern.txt :79, the left end of Q0's first negative run);
###   (3) the zero side's sign at the witness by the converse's own inequality: Re zeroSide <= -M^N (SUM_T Nf) + SUM_rest
###       B^2 (1 + |w(x)|)^(2D) s_x^N, N = 2^(j+1) (tie_term_neg, kill_term_zero, rest_term_small), B = |VF| max(CV,0) BK BE
###       (coeffs_exist :686), CV the Lagrange coefficient sum (real_even_interpolant :432), BK and BE fixed_poly_bound's;
###       the least certifying j >= D printed, with the floor; zeros above 150 bounded through the count field, its constant
###       printed as the premise it is.
### Nothing here is a statement about the zeros of any Epstein zeta function beyond the bench's own numbers.
"""
import io
import json
import math
import os
import sys

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_ = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

mp.mp.dps = 40
F = mp.mpf(1) / 2
RHO_E = (mp.mpf('0.7979971571786801'), mp.mpf('29.551761098629115'))
A_BENCH = mp.mpf('33.194255')
T_LIST = 150


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D_, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D_, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def zeros():
    """### the bench's list: b326's on-line ordinates (complete below 150, b506) and b506's off-line zeros (column R, sigma > 1/2)."""
    lib = json.load(io.open(os.path.join(D_, 'b326_epstein_zeros.json'), encoding='utf-8'))
    on = sorted(mp.mpf(repr(z['gamma_a'])) for z in lib['zeros'])
    c2 = json.load(io.open(os.path.join(D_, 'b506_c2_results.json'), encoding='utf-8'))
    off = [(mp.mpf(repr(z['rho'][0])), mp.mpf(repr(z['rho'][1]))) for z in c2['found'] if z.get('rho') and z['col'] == 'R']
    return on, off


def gamma_of(beta, gam):
    """### gammaOf rho = (rho - 1/2) / i = gam - i (beta - 1/2)."""
    return mp.mpc(gam, -(beta - mp.mpf(1) / 2))


def st(x):
    """### Real.smoothTransition: e(x) / (e(x) + e(1 - x)), e(x) = exp(-1/x) for x > 0, else 0."""
    e = lambda y: mp.exp(-1 / y) if y > 0 else mp.mpf(0)
    a, b = e(x), e(1 - x)
    return a / (a + b)


def ghat(z, L):
    """### paperFT (phiC (plateau 1/2 L)) z = INT phi(u) e^(i z u) du = 2 L INT_0^1 phi1(t) cos(z L t) dt; phi1 = 1 on [0, 1/2],
    ### st(2 (1 - t)) on [1/2, 1] (the second factor st(2 (1 + t)) is 1 there)."""
    zl = z * L
    flat = mp.sin(zl / 2) / zl if zl != 0 else mp.mpf(1) / 2
    ramp, err = mp.quad(lambda t: st(2 * (1 - t)) * mp.cos(zl * t), [mp.mpf(1) / 2, mp.mpf(3) / 4, 1], error=True)
    return 2 * L * (flat + ramp), 2 * L * err


def d4_integral(L):
    """### INT |phi''''| du = 2 L^-3 INT_{1/2}^1 |phi1''''(t)| dt, the decay constant of paperFT_decay (PowerWindow), numerically."""
    f = lambda t: abs(mp.diff(lambda s: st(2 * (1 - s)), t, 4))
    return 2 * L ** -3 * mp.quad(f, mp.linspace(mp.mpf(1) / 2, 1, 9))


def witness():
    on, off = zeros()
    zE = gamma_of(*RHO_E)
    w = 1 / (4 * (abs(zE) + 1))
    # ### (1) the scores: on-line at +-gamma (one score), off-line per orbit (the four images share it: even, real window)
    sc_on, err_on = [], []
    for gam in on:
        v, e = ghat(mp.mpc(gam, 0), w)
        sc_on.append(abs(v))
        err_on.append(e)
    sc_off, err_off = [], []
    for b, gam in off:
        v, e = ghat(gamma_of(b, gam), w)
        sc_off.append(abs(v))
        err_off.append(e)
    k = max(range(len(off)), key=lambda i: sc_off[i])
    M = sc_off[k]
    ties = [i for i in range(len(off)) if abs(sc_off[i] - M) <= 10 * (err_off[i] + err_off[k]) + mp.mpf(10) ** -30]
    b_s, g_s = off[k]
    delta = b_s - mp.mpf(1) / 2
    v_s = mp.mpc(delta, g_s) ** 2                                   # vOf rho = (rho - 1/2)^2
    VF = [v_s, mp.conj(v_s)]
    kill = [i for i in range(len(on)) if sc_on[i] >= M]
    Xr = sorted(set(-on[i] ** 2 for i in kill))                     # (vOf rho).re = -gamma^2 on the line, +-gamma one value
    DK = len(Xr) + 1
    DE = 2
    Dp = 2 * len(VF) + 2 * DK + DE
    # ### (2) the support
    half_pre = mp.mpf(2) ** Dp * w
    half_post = mp.mpf(2) ** (Dp + 1) * w
    lnA = mp.log(A_BENCH)
    ratio = half_pre / lnA
    # ### (3) the sign by the converse's inequality, in logarithms
    if len(ties) != 1:
        sys.exit('### THE TIE SET SPANS %d ORBITS -- this bench handles one; NOTHING WRITTEN' % len(ties))
    nT = 4 * len(ties)                                               # cE = 1 + SUM_{rho in TF} 1/|re - 1/2|, TF the orbit's images
    cE = 1 + nT / abs(delta)
    Kp = lambda x: mp.fprod([x - c for c in Xr]) if Xr else mp.mpf(1)
    Nf = [abs(Kp(v) ** 2 * (1 - cE ** 2 * v)) for v in (v_s, v_s, mp.conj(v_s), mp.conj(v_s))] * len(ties)
    tie_mass = mp.fsum(Nf)
    CV = (1 + abs(v_s)) / abs(mp.im(v_s))                            # Lagrange basis on {v, conj v}: |c1| + |c0| per node, two nodes
    BK = DK * mp.fprod([1 + abs(c) for c in Xr]) if Xr else mp.mpf(1)
    BE = 2 * (1 + cE)
    B = len(VF) * max(CV, 0) * BK * BE
    rest = []                                                        # (score ratio, |w|, multiplicity count) for zeros outside T and K
    for i, gam in enumerate(on):
        if i not in kill:
            rest.append((sc_on[i] / M, abs(gam), 2, err_on[i]))
    for i, (b, gam) in enumerate(off):
        if i not in ties:
            rest.append((sc_off[i] / M, abs(gamma_of(b, gam)), 4, err_off[i]))
    rmax = max(r[0] for r in rest)
    floor_rel = max(r[3] for r in rest) / M + max(err_off) / M         # relative floor on a score ratio
    # ### the tail above T_LIST: scores bounded by the sampled sup on [150, T0] and by paperFT_decay beyond T0
    A4 = d4_integral(w) * mp.exp(w / 2)
    T0 = mp.mpf(T_LIST)
    while A4 / (M * T0 ** 4) > mp.mpf(1) / 2:
        T0 += 50
    # ### the sup of the score on [150, T0] x |Im z| <= 1/2, sampled at unit steps in t and quarter steps in Im z, each sample
    # ### raised by the Lipschitz margin |d ghat| <= INT |u| phi(u) e^(|u|/2) du <= 2 L^2 e^(L/2) over half a step each way
    lip = 2 * w ** 2 * mp.exp(w / 2)
    mp.mp.dps = 25
    grid = [mp.mpf(T_LIST) + i for i in range(0, int(T0) - T_LIST + 1)]
    sup = max(max(abs(ghat(mp.mpc(t, -dl), w)[0]) for dl in (0, mp.mpf(1) / 4, mp.mpf(1) / 2)) for t in grid)
    mp.mp.dps = 40
    sup = sup + lip * (mp.mpf(1) / 2 + mp.mpf(1) / 8)
    sup_ratio = sup / M
    # ### the count premise: A0 from the list (max over unit windows of N / log(t + 3)), doubled, as the premise it is
    ords = sorted([g for g in on] + [g for _, g in off for _ in (0, 1)])
    a0_list = max((sum(1 for x in ords if t < x <= t + 1) / mp.log(t + 3)) for t in [mp.mpf(i) / 4 for i in range(0, 4 * T_LIST)])
    A0 = 2 * a0_list
    log10 = lambda x: mp.log10(x) if x > 0 else -mp.inf

    def certify(j):
        N = mp.mpf(2) ** (j + 1)
        terms = [mult * B ** 2 * (1 + wa) ** (2 * Dp) * (min(1, r * (1 + floor_rel))) ** N for r, wa, mult, _ in rest]
        lr = log10(mp.fsum(terms)) if terms else -mp.inf
        # tail [150, T0]: count <= 2 A0 log(t + 3) per unit, weight <= B^2 (1 + T0 + 1)^(2D), score ratio <= sup_ratio (floored)
        tail1 = 2 * A0 * mp.log(T0 + 3) * (T0 - T_LIST) * B ** 2 * (2 + T0) ** (2 * Dp) * min(1, sup_ratio * (1 + floor_rel)) ** N
        # tail beyond T0: SUM_t 2 A0 log(t + 3) B^2 (2 + t)^(2D) (A4 / (M t^4))^N <= its integral bound at T0 (N >> 2D)
        tail2 = 4 * A0 * mp.log(T0 + 3) * B ** 2 * (2 + T0) ** (2 * Dp + 1) * (A4 / (M * T0 ** 4)) ** N
        lt = log10(mp.fsum([mp.mpf(10) ** lr if lr > -mp.inf else 0, tail1, tail2]))
        return dict(j=j, log10_tie_mass=float(log10(tie_mass)), log10_rest_list=float(lr), log10_tail1=float(log10(tail1)),
                    log10_tail2=float(log10(tail2)), log10_rest_total=float(lt), certified=bool(log10(tie_mass) > lt))
    cert = []
    j = Dp
    while True:
        c = certify(j)
        cert.append(c)
        if c['certified'] or j > Dp + 64:
            break
        j += 1
    jstar = cert[-1]['j'] if cert[-1]['certified'] else None
    half_j = mp.mpf(2) ** jstar * w if jstar is not None else None
    h31c = 'HOLDS' if (mp.mpf(1) / 10 <= ratio <= 10) else 'REFUTED'
    res = dict(rhoE=[str(RHO_E[0]), str(RHO_E[1])], gammaOf_rhoE=[str(mp.re(zE)), str(mp.im(zE))], abs_gammaOf=str(abs(zE)),
               w=str(w), on_count=len(on), off_count=len(off), dominant=[str(b_s), str(g_s)], M=str(M), ties=len(ties),
               tie_orbits=[[str(off[i][0]), str(off[i][1])] for i in ties],
               rhoE_score=str(sc_off[[i for i, (b, gg) in enumerate(off) if abs(gg - RHO_E[1]) < 1e-6][0]]),
               kill=len(kill), kill_ordinates=[str(on[i]) for i in kill], VF=len(VF), Xr=len(Xr), DK=DK, DE=DE, D=Dp,
               half_pre=str(half_pre), half_post=str(half_post), ln_a=str(lnA), ratio=str(ratio), H31c=h31c,
               cE=str(cE), CV=str(CV), BK=str(BK), BE=str(BE), B=str(B), tie_mass=str(tie_mass), rest_count=len(rest),
               rmax=str(rmax), floor_rel=str(floor_rel), A4=str(A4), T0=str(T0), sup_ratio=str(sup_ratio), A0_list=str(a0_list), A0=str(A0),
               cert=cert, jstar=jstar, half_at_jstar=str(half_j) if half_j is not None else None,
               ratio_at_jstar=str(half_j / lnA) if half_j is not None else None,
               scores_on=[[str(on[i]), str(sc_on[i] / M)] for i in range(len(on))],
               scores_off=[[str(off[i][0]), str(off[i][1]), str(sc_off[i] / M)] for i in range(len(off))])
    nz = lambda x: mp.nstr(x, 12)
    L = ['b590 -- COMPONENT 4: THE KERNEL`S WITNESS WINDOW AGAINST THE BENCH, (R200)(4)(c). ### A READING.', '',
         '### the zero list: on-line ordinates %d (relay data/b326_epstein_zeros.json, complete below %d by b506), each with its '
         'conjugate; off-line zeros %d with sigma > 1/2 (data/b506_c2_results.json column R), each with its reflection and their '
         'conjugates.' % (len(on), T_LIST, len(off)),
         '### rhoE = %s + %s i ; gammaOf rhoE = %s ; |gammaOf rhoE| = %s' % (nz(RHO_E[0]), nz(RHO_E[1]), nz(zE), nz(abs(zE))),
         '### THE BASE (named by the kernel): plateau, ramp fraction 1/2, half-width w = baseWidth(rhoE) = 1/(4(|gammaOf rhoE|+1)) = %s' % nz(w),
         '',
         '### (1) THE SCORES AT THE BASE: the dominant off-line orbit %s + %s i, M = %s (rhoE`s orbit: score/M = %s) ; tie orbits %d' % (
             nz(b_s), nz(g_s), mp.nstr(M, 15), mp.nstr(res and mp.mpf(res['rhoE_score']) / M, 12), len(ties)),
         '###   the kill set: on-line ordinates with score >= M: %d %s' % (len(kill), [mp.nstr(on[i], 8) for i in kill]),
         '###   |VF| = %d ; |Xr| = %d ; DK = |Xr| + 1 = %d ; DE = %d ; ### **D = 2|VF| + 2 DK + DE = %d**' % (len(VF), len(Xr), DK, DE, Dp),
         '###   the largest score ratio outside T and K: %s ; the quadrature floor on a ratio: %s' % (mp.nstr(rmax, 15), mp.nstr(floor_rel, 3)),
         '',
         '### (2) THE SUPPORT: the witness`s pre-pairing half-width 2^j w with j = max J D >= D, so at least 2^D w = %s ; paired, at least '
         '2^(D+1) w = %s.' % (nz(half_pre), nz(half_post)),
         '###   b522`s plateau half-width ln 33.194255 = %s (relay data/b554_sign_pattern.txt :79) ; ### **THE RATIO, AT LEAST: %s**' % (
             nz(lnA), mp.nstr(ratio, 8)),
         '###   (the support`s hull equals the bound: Titchmarsh`s convolution theorem for the powers and the pairing, a page reading; the '
         'kernel states the inclusion, pwWindow_support)',
         '### ### **H31c %s: the half-width lies %s a factor of ten of ln 33.19 (ratio at least %s).**' % (
             h31c, 'within' if h31c == 'HOLDS' else 'beyond', mp.nstr(ratio, 6)),
         '',
         '### (3) THE SIGN AT THE WITNESS, by the converse`s own inequality (log10, the tie mass against the rest`s dominant):',
         '###   cE = %s ; CV = %s ; BK = %s ; BE = %s ; B = %s ; SUM_T Nf = %s' % (mp.nstr(cE, 8), mp.nstr(CV, 8), mp.nstr(BK, 8), mp.nstr(BE, 8),
                                                                              mp.nstr(B, 8), mp.nstr(tie_mass, 8)),
         '###   the tail above %d: the sampled sup of the score ratio on [%d, T0 = %s] (unit steps, Im z in {0, -1/4, -1/2}, each '
         'raised by the Lipschitz margin) = %s ; beyond T0 paperFT_decay`s constant A4 = %s with A4/(M T0^4) = %s ; ### THE COUNT '
         'PREMISE: A0 = %s (twice the list`s own %s)' % (
             T_LIST, T_LIST, mp.nstr(T0, 6), mp.nstr(sup_ratio, 8), mp.nstr(A4, 6), mp.nstr(A4 / (M * T0 ** 4), 4),
             mp.nstr(A0, 6), mp.nstr(a0_list, 6))]
    for c in cert:
        L.append('    j %-4d tie %.3f ; rest(list) %.3f ; tail [150,T0] %.4g ; tail beyond %.4g ; rest total %.3f ; %s' % (
            c['j'], c['log10_tie_mass'], c['log10_rest_list'], c['log10_tail1'], c['log10_tail2'], c['log10_rest_total'],
            'CERTIFIED NEGATIVE' if c['certified'] else 'not certified'))
    L += ['### ### **THE LEAST CERTIFYING POWER j* = %s ; the half-width there 2^j* w = %s, %s times ln 33.19.**' % (
        jstar, mp.nstr(half_j, 10) if half_j is not None else None, mp.nstr(half_j / lnA, 8) if half_j is not None else None),
          '### A READING: the bench`s zero list and the count premise; nothing about any zero of Z_Q is asserted beyond these numbers.']
    put_txt('b590_witness_vs_bench.txt', L)
    put_json('b590_witness_vs_bench.json', res)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd != 'witness':
        print('usage: b590_bench.py witness')
        sys.exit(2)
    witness()
