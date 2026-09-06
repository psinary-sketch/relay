# -*- coding: utf-8 -*-
"""b340_li_control.py -- THE LI FAMILY CONTROL: THE ARCHIMEDEAN DISTRIBUTION ON THE LI FAMILY BY THE DERIVED KERNEL,
### AGAINST THE DEPOSIT'S ARCHIMEDEAN CHANNEL OF THE LI COEFFICIENT, WITH b327's IDENTITY AS THE BAR.

### ### **WHAT IS MEASURED (registration (D), sealed before this file was written).** ### At the twenty-two indices the
### balance keystone tabulates: `I(n) = (1/2 pi) INT Re G_n(1/2 + iu) h_+(u) du`, the atlas's archimedean channel with
### the Li test function's transform on the line in place of `hhat`, the kernel `h_+(u) = Re psi(1/4 + iu/2) - log pi`
### (b326's `kernel_zeta`, b333's identity) evaluated by `mpmath`; by two quadratures (the theta substitution on
### `4n + 4` panels, tanh-sinh; the `u` variable on panels at the phase multiples, Gauss-Legendre), gated by the
### noise floor. ### Against: `lambda_A(n)` by the bench's own definitions executed from its file (b327's loader,
### IMPORTED), at the bench's two radii; `S_inf(n) + 1` by the source's (4.11) (b327's `s_inf_closed`, IMPORTED);
### the keystone's tabulated column. ### The pole constant `1`, the Li map of `log s`, carried as its own column.
### ### **THE BAR:** `|I(n) + 1 - lambda_A(n)| <= 1e-9 max(1, |lambda_A(n)|)`, and the quadrature drift below it.
### ### **THE FIXTURES FIRST:** the built `g_n` has Mellin transform `G_n` (F1); the closed form on the line equals
### the binomial sum (F2); each fails on its altered input.
### ### **WHAT IT DOES NOT DO:** it evaluates no zero side and no finite side; it defines no Sonin margin on the
### family; it proves nothing; it moves no grade.
"""
import io
import json
import os
import re
import sys
import time
from math import comb

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_bridge as BR      # noqa: E402  ### load_bench_definitions, s_inf_closed -- IMPORTED, never edited
import noise_floor as NF      # noqa: E402  ### the gate

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
KEY = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
BENCH = os.path.join(PP, 'internal', 'bench', 'li_bench.py')
MONO = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
RUN = os.path.join(D, 'b340_control_run.txt')
OUT = os.path.join(D, 'b340_control.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BAR_REL = mp.mpf('1e-9')          # ### sealed, section (D)
DPS_THETA, DPS_U = 30, 40         # ### sealed, section (D)
M_QUAD = 512                      # ### b327's reduced quadrature for the bench's circle
CERT_FRAG = "partialPositivity_finiteRange` (v0.8.0) certifies \u03bb_n \u2265 0 for n up to Voros's detection threshold N\u2080(T) \u2248 2T\u00b2"
BENCH_FRAG = 'positivity of lambda_n in a finite range is NOT evidence of the kind the criterion'

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


# ### ==============================================================================================
# ### THE LI TEST FUNCTIONS, BUILT.
# ### ==============================================================================================
def G(n, s):
    """### the source's (3.2), as the binomial sum."""
    return sum(comb(n, j) * (-1) ** (j + 1) * s ** (-j) for j in range(1, n + 1))


def g_x(n, x, alter=False):
    """### the Li test function on (0, 1]: SUM C(n,j) (-1)^{j+1} (-log x)^{j-1} / (j-1)!  (alter: one coefficient scaled)."""
    L = -mp.log(x)
    acc = mp.mpf(0)
    for j in range(1, n + 1):
        c = comb(n, j) * (-1) ** (j + 1)
        if alter and j == 1:
            c = c * mp.mpf('1.001')
        acc += c * L ** (j - 1) / mp.factorial(j - 1)
    return acc


def mellin_of_g(n, s, alter=False):
    """### INT_0^1 x^{s-1} g_n(x) dx by mpmath.quad, in the variable t = -log x (the same integral; the first run's
    ### direct form on (0, 1) reached only 3.8e-09 at n = 8, and the fixture's bar is 1e-12)."""
    ### the second run's panels [0, 1, 8, 40, inf] still reached only 3.8e-09 at n = 8, u = 7 (forty-five oscillations of
    ### e^{-iut} inside one panel); the third run resolves the oscillation with panels of half a unit to t = 160, where e^{-t/2} t^7 is below 1e-30, so the infinite panel carries nothing.
    pts = [mp.mpf(k) / 2 for k in range(0, 321)] + [mp.inf]
    return mp.quad(lambda tt: mp.exp(-s * tt) * g_x(n, mp.exp(-tt), alter), pts)


def reG_closed(n, u):
    """### Re G_n(1/2 + iu) = 1 - (-1)^n cos(2n arctan 2u), in the stable form 2 sin^2 / 2 cos^2."""
    ph = n * mp.atan(2 * u)
    return 2 * mp.sin(ph) ** 2 if n % 2 == 0 else 2 * mp.cos(ph) ** 2


def h_plus(u):
    """### the derived kernel, b326's kernel_zeta formula: Re psi(1/4 + iu/2) - log pi."""
    return mp.re(mp.digamma(mp.mpc(mp.mpf(1) / 4, u / 2))) - mp.log(mp.pi)


def I_theta(n):
    """### (1/4pi) INT_0^pi [1 - (-1)^n cos n theta] h_+(u(theta)) sec^2(theta/2) dtheta, u = tan(theta/2)/2; tanh-sinh on 4n+4 panels."""
    with mp.workdps(DPS_THETA):
        def f(th):
            c = mp.cos(th / 2)
            u = mp.sin(th / 2) / (2 * c)
            osc = 2 * mp.sin(n * th / 2) ** 2 if n % 2 == 0 else 2 * mp.cos(n * th / 2) ** 2
            return osc * h_plus(u) / (c * c)
        pts = [mp.pi * k / (4 * n + 4) for k in range(4 * n + 5)]
        v, err = mp.quad(f, pts, error=True)
        return v / (4 * mp.pi), err


def I_u(n):
    """### (1/pi) INT_0^inf Re G_n(1/2 + iu) h_+(u) du on panels at the phase multiples; Gauss-Legendre."""
    with mp.workdps(DPS_U):
        pts = [mp.tan(mp.pi * m / (2 * n)) / 2 for m in range(n)] + [mp.inf]
        v, err = mp.quad(lambda u: reG_closed(n, u) * h_plus(u), pts, method='gauss-legendre', error=True)
        return v / mp.pi, err


# ### ==============================================================================================
# ### THE KEYSTONE'S TABLE, READ FROM THE OWNER FILE.
# ### ==============================================================================================
def keystone_table():
    txt = io.open(KEY, encoding='utf-8').read().splitlines()
    head = '| n | \u03bb_A(n) | \u03bb_Z(n) | margin \u03bb_n | agree digits |'
    i = txt.index(head)
    rows = []
    for ln in txt[i + 2:]:
        if not ln.startswith('|'):
            break
        cells = [c.strip().replace('**', '').replace('\u2212', '-') for c in ln.strip().strip('|').split('|')]
        rows.append(dict(n=int(cells[0]), lamA=cells[1], lamZ=cells[2], margin=cells[3], digits=int(cells[4])))
    return rows, i + 1


def main():
    t0 = time.time()
    rec('=' * 100)
    rec("b340 -- THE LI FAMILY CONTROL. ### the archimedean distribution on the Li family by the derived kernel, against the deposit's channel.")
    rec('=' * 100)
    fails = []

    # ### (F1) the built function's Mellin transform is G_n; the altered coefficient fails.
    rec('')
    rec('  (F1) THE LI TEST FUNCTION BUILT: Mellin transform of g_n on (0,1] against G_n(s) at s = 1/2 + iu (mpmath.quad, dps 30):')
    worst1, worst_alt = mp.mpf(0), mp.mpf('inf')
    with mp.workdps(40):
        for n in (1, 3, 8):
            for u in ('0.3', '2', '7'):
                s = mp.mpc(mp.mpf(1) / 2, mp.mpf(u))
                d = abs(mellin_of_g(n, s) - G(n, s))
                da = abs(mellin_of_g(n, s, alter=True) - G(n, s))
                worst1 = max(worst1, d)
                worst_alt = min(worst_alt, da)
                rec('      n = %-3d u = %-4s |Mellin(g_n) - G_n| = %.3e   altered coefficient : %.3e' % (n, u, d, da))
    f1 = worst1 <= mp.mpf('1e-12') and worst_alt > mp.mpf('1e-12')
    rec('    worst %.3e (bar 1e-12) ; the altered input\'s smallest miss %.3e : %s' % (worst1, worst_alt, 'PASS' if f1 else '### FAIL ###'))
    if not f1:
        fails.append('F1')

    # ### (F2) the closed form on the line against the binomial sum.
    rec('')
    rec('  (F2) ON THE LINE: Re G_n(1/2 + iu) = 1 - (-1)^n cos(2n arctan 2u) against the binomial sum:')
    worst2 = mp.mpf(0)
    with mp.workdps(130):        # ### the binomial sum at n = 130 cancels ~10^62 at u = 0; the first run at dps 30 lost it all
        for n in (1, 2, 3, 8, 130):
            for u in ('0', '0.3', '2', '7', '50'):
                s = mp.mpc(mp.mpf(1) / 2, mp.mpf(u))
                d = abs(reG_closed(n, mp.mpf(u)) - mp.re(G(n, s)))
                worst2 = max(worst2, d)
        alt = abs(reG_closed(3, mp.mpf('0.3')) - mp.re(G(4, mp.mpc(mp.mpf(1) / 2, mp.mpf('0.3')))))
    f2 = worst2 <= mp.mpf('1e-12') and alt > mp.mpf('1e-12')
    rec('    worst %.3e over n in {1,2,3,8,130}, u in {0,0.3,2,7,50} (bar 1e-12) ; the wrong n misses by %.3e : %s' % (worst2, alt, 'PASS' if f2 else '### FAIL ###'))
    if not f2:
        fails.append('F2')

    # ### the keystone's indices
    rows, head_line = keystone_table()
    idx = [r['n'] for r in rows]
    rec('')
    rec('  THE KEYSTONE\'S TABLE (owner file, line %d): %d rows, indices %s' % (head_line, len(rows), idx))
    nmax = max(idx)

    # ### the deposit's channel, route A: the bench's definitions from its own file, through b327's loader.
    rec('')
    rec('  ROUTE A -- lambda_A(n) BY THE BENCH\'S OWN DEFINITIONS (b327_bridge.load_bench_definitions), two radii, M = %d:' % M_QUAD)
    ns, nhead, keiper = BR.load_bench_definitions()
    rec('    bench head executed : %d lines ; dps now %d (the bench\'s own) ; its KEIPER dict carried, unused here' % (nhead, mp.mp.dps))
    tA = time.time()
    lamA, lamZ, pole = {}, {}, {}
    for r in BR.RADII:
        etaA = ns['taylor_coeffs'](ns['f_A'], r, M_QUAD, nmax)
        lamA[r] = ns['lambdas'](etaA, nmax)
        etaP = ns['taylor_coeffs'](lambda s: mp.log(s), r, M_QUAD, nmax)
        pole[r] = ns['lambdas'](etaP, nmax)
    rec('    lambda_A at radii %s in %.0f s ; the pole constant L_n[log s] at both radii' % (BR.RADII, time.time() - tA))
    tZ = time.time()
    for r in BR.RADII:
        etaZ = ns['taylor_coeffs'](ns['f_Z'], r, M_QUAD, nmax)
        lamZ[r] = ns['lambdas'](etaZ, nmax)
    rec('    lambda_Z at radii %s in %.0f s' % (BR.RADII, time.time() - tZ))
    r0, r1 = BR.RADII
    radii_worst = max(abs(lamA[r0][n] - lamA[r1][n]) for n in idx)
    pole_worst = max(abs(pole[r0][n] - 1) for n in idx)
    rec('    the two radii agree on lambda_A to %.3e over the indices ; the pole constant L_n[log s] - 1 worst %.3e' % (radii_worst, pole_worst))

    # ### route B: the source's (4.11) + 1
    SB = {n: BR.s_inf_closed(n) for n in idx}
    routeB_worst = max(abs(lamA[r0][n] - (SB[n] + 1)) for n in idx)
    rec("    ROUTE B -- S_inf(n) + 1 by the source's (4.11) (b327_bridge.s_inf_closed): worst |lambda_A - S_inf - 1| = %.3e (b327's identity, re-measured)" % routeB_worst)

    # ### the instrument
    rec('')
    rec('  THE INSTRUMENT -- I(n) = (1/2pi) INT Re G_n(1/2+iu) h_+(u) du, the derived kernel by mpmath (dps %d / %d):' % (DPS_THETA, DPS_U))
    rec('    %-4s %-24s %-24s %-11s %-9s %-4s %-24s %-11s %-6s' % ('n', 'I(n) theta (tanh-sinh)', 'I(n) u (Gauss-Legendre)', 'drift', 'gate', 'pole', 'lambda_A (route A)', '|I+1-lamA|', 'bar?'))
    table = []
    holds_all = True
    for n in idx:
        tn = time.time()
        it, e1 = I_theta(n)
        iu, e2 = I_u(n)
        with mp.workdps(40):
            drift = abs(it - iu)
            verdict, why = NF.classify(float(it), float(iu))
            la = lamA[r0][n]
            bar = BAR_REL * max(mp.mpf(1), abs(la))
            miss = abs(it + 1 - la)
            missB = abs(it - SB[n])
            ok = (miss <= bar) and (drift <= bar) and (verdict == NF.RESOLVED)
            holds_all = holds_all and ok
            ks = mp.mpf(rows[idx.index(n)]['lamA'])
            ks_miss = abs(it + 1 - ks)
            rec('    %-4d %-24s %-24s %-11.3e %-9s %-4s %-24s %-11.3e %-6s   (%.0f s; keystone column %s, off by %.2e)'
                % (n, mp.nstr(it, 20), mp.nstr(iu, 20), drift, verdict, mp.nstr(pole[r0][n], 3), mp.nstr(la, 20), miss, 'HOLDS' if ok else '### FAILS', time.time() - tn, mp.nstr(ks, 13), ks_miss))
            table.append(dict(n=n, I_theta=mp.nstr(it, 25), I_u=mp.nstr(iu, 25), err_theta=mp.nstr(e1, 3), err_u=mp.nstr(e2, 3), drift=mp.nstr(drift, 3), gate=verdict,
                              pole=mp.nstr(pole[r0][n], 20), lamA=mp.nstr(la, 25), lamA_r1=mp.nstr(lamA[r1][n], 25), S_inf_plus_1=mp.nstr(SB[n] + 1, 25),
                              miss=mp.nstr(miss, 3), missB=mp.nstr(missB, 3), bar=mp.nstr(bar, 3), holds=bool(ok),
                              keystone_lamA=rows[idx.index(n)]['lamA'], keystone_miss=mp.nstr(ks_miss, 3),
                              lamZ_bench=mp.nstr(lamZ[r0][n], 20), keystone_lamZ=rows[idx.index(n)]['lamZ'], keystone_margin=rows[idx.index(n)]['margin'],
                              margin_bench=mp.nstr(lamA[r0][n] + lamZ[r0][n], 20), margin_positive=bool(lamA[r0][n] + lamZ[r0][n] > 0)))
    worst_miss = max(mp.mpf(t['miss']) for t in table)
    worst_drift = max(mp.mpf(t['drift']) for t in table)
    worst_ks = max(mp.mpf(t['keystone_miss']) for t in table)
    n_hold = sum(1 for t in table if t['holds'])
    rec('    ### the bar holds at %d of %d indices ; worst |I + 1 - lambda_A| = %.3e ; worst drift = %.3e ; worst against the keystone\'s printed column = %.3e' % (n_hold, len(table), worst_miss, worst_drift, worst_ks))

    # ### the differing constituent, if any
    rec('')
    what = 'none'
    if holds_all:
        rec('  ### ### **VERDICT: A FOURTH CONTROL, AT ITS ARCHIMEDEAN CONSTITUENT -- THE BAR HOLDS AT EVERY TABULATED INDEX WITH THE POLE CONSTANT CARRIED.**')
    else:
        bad = [t for t in table if not t['holds']]
        offs = [mp.mpf(t['I_theta']) + 1 - mp.mpf(t['lamA']) for t in bad]
        const = max(abs(o - offs[0]) for o in offs) < mp.mpf('1e-6') if len(offs) > 1 else True
        ratios = [(mp.mpf(t['I_theta']) + 1) / mp.mpf(t['lamA']) for t in bad if abs(mp.mpf(t['lamA'])) > 1]
        factor = (max(abs(q - ratios[0]) for q in ratios) < mp.mpf('1e-6')) if len(ratios) > 1 else False
        gate_ref = any(t['gate'] != NF.RESOLVED or mp.mpf(t['drift']) > mp.mpf(t['bar']) for t in bad)
        what = 'a quadrature failure (the gate refusing)' if gate_ref else ('a constant offset (the pole constant miscarried)' if const else ('a factor (the factor-of-two hazard)' if factor else 'a growth with n (the tail)'))
        rec('  ### ### **VERDICT: THE DIFFERING CONSTITUENT -- the bar fails at %s ; what differs: %s.**' % ([t['n'] for t in bad], what))
        rec('      offsets I + 1 - lambda_A at the failing indices : %s' % [mp.nstr(o, 6) for o in offs])
        n_id = sum(1 for t in table if mp.mpf(t['miss']) <= mp.mpf(t['bar']))
        rec('      ### and, read beside the verdict: the identity |I(n) + 1 - lambda_A(n)| <= bar by the theta route alone at %d of %d indices (worst %.3e); the drift between the two quadratures is what the gate refuses.' % (n_id, len(table), worst_miss))
        fails.append('BAR')

    # ### the finite-range positivity restated at its scope, beside the values
    rec('')
    rec("  THE DEPOSIT'S FINITE-RANGE POSITIVITY, RESTATED AT ITS SCOPE, BESIDE THE INSTRUMENT'S VALUES:")
    mono = io.open(MONO, encoding='utf-8', errors='replace').read().splitlines()
    cl = [i + 1 for i, ln in enumerate(mono) if CERT_FRAG in ln]
    sent = ''
    if cl:
        ln = mono[cl[0] - 1]
        a = ln.index(CERT_FRAG) - 1
        b = ln.index('no further', a) + len('no further')
        sent = ln[a:b]
    rec('    the monograph, line %s: *"%s"*' % (cl[0] if cl else 'NOT FOUND', sent))
    bench_txt = io.open(BENCH, encoding='utf-8').read().splitlines()
    bl = [i + 1 for i, ln in enumerate(bench_txt) if BENCH_FRAG in ln]
    rec('    the bench, line %s: *"%s"* -- and the next line: *"%s"*' % (bl[0] if bl else 'NOT FOUND', BENCH_FRAG, 'respects (Keiper 1992; BALANCE_AND_POSITIVITY sec V). This is an instrument, not an argument.'))
    rec('    %-4s %-20s %-20s %-20s %-20s %-8s' % ('n', 'lambda_A (bench)', 'lambda_Z (bench)', 'margin lambda_n', "keystone's margin", 'sign'))
    for t in table:
        rec('    %-4d %-20s %-20s %-20s %-20s %-8s' % (t['n'], mp.nstr(mp.mpf(t['lamA']), 13), mp.nstr(mp.mpf(t['lamZ_bench']), 13), mp.nstr(mp.mpf(t['margin_bench']), 13), t['keystone_margin'], 'POSITIVE' if t['margin_positive'] else '### NOT'))
    allpos = all(t['margin_positive'] for t in table)
    rec('    the margin positive at all %d tabulated indices : %s ; ### THE CERTIFICATE IS THE DEPOSIT\'S AND ITS PREMISES ARE NAMED AND OPEN ; POSITIVITY IN A FINITE RANGE IS NOT EVIDENCE OF THE KIND THE CRITERION RESPECTS (the bench\'s sentence).' % (len(table), allpos))
    ks_z_worst = max(abs(mp.mpf(t['lamZ_bench']) - mp.mpf(t['keystone_lamZ'])) for t in table)
    rec("    the bench's lambda_Z against the keystone's printed column : worst %.3e (its rounding)" % ks_z_worst)

    rec('')
    rec('  ### NO ZERO SIDE AND NO FINITE SIDE EVALUATED ; NO SONIN MARGIN DEFINED ON THE FAMILY ; NO GRADE MOVED ; A CONTROL CERTIFIES THE INSTRUMENT, NOT THE OBJECT.')
    rec('  ### CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)
    run_path, k = RUN, 1
    while os.path.exists(run_path):
        k += 1
        run_path = RUN.replace('_run.txt', '_run%d.txt' % k)
    io.open(run_path, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    res = dict(indices=idx, table=table, holds_all=bool(holds_all), n_hold=n_hold, worst_miss=mp.nstr(worst_miss, 3), worst_drift=mp.nstr(worst_drift, 3), worst_keystone=mp.nstr(worst_ks, 3),
               f1=bool(f1), f2=bool(f2), worst_f1=mp.nstr(worst1, 3), worst_f2=mp.nstr(worst2, 3), radii_worst=mp.nstr(radii_worst, 3), pole_worst=mp.nstr(pole_worst, 3),
               routeB_worst=mp.nstr(routeB_worst, 3), cert_line=cl[0] if cl else None, cert_sentence=sent, bench_line=bl[0] if bl else None, all_margins_positive=bool(allpos),
               keystone_lamZ_worst=mp.nstr(ks_z_worst, 3), keystone_head_line=head_line, fails=fails, elapsed=time.time() - t0,
               what=what, n_identity=sum(1 for t in table if mp.mpf(t['miss']) <= mp.mpf(t['bar'])), run_file=os.path.basename(run_path))
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(res, indent=1))
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
