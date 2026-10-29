# -*- coding: utf-8 -*-
"""b723_zetak.py -- H-ZETAK, (R333)(5)(i), AS data/b723_registrations.txt (ii) REGISTERED IT (:36-:50, committed alone at relay 9ad26421
before any figure): "on the two windows at which Q0's family form turns negative at its onset (rho0's family at a = 6.838396011, the band
zero's at a = 10.38532711), the same form with Q0's prime weights replaced by zeta_K's, P and A unchanged, is positive definite beyond its
certified ball at both." FALSIFIER: a least eigenvalue negative beyond its ball at either window.

### THE ROUTE: tools/b709_grid.py imported unedited -- its grid (the two points mid929_937 of rho0's family and rung32381 of the band zero's),
### its window per kind (C, N, CN), its prime sum with the exact ratios read from N (prime_sum709) and its terms (terms709); b707's gram and
### reading (tools/b707_onset.py, unedited). THE zeta_K FORM: S_K = P - PR_K + A, with P, A and k(0) Q0's own at the same window (Q(sqrt -23)
### shares Q0's gamma factor, conductor and pole), PR_K b709's prime sum on the weights Lambda_K(n) = Lambda(n)(1 + chi(n)), Lambda b694's
### lambda_z and chi = (-23 / n) the Kronecker symbol, computed here by the Jacobi route and checked against Euler's criterion mod 23 at
### every n to the window's nmax. Nothing is read from b709's banked units except to compare (C1).
### THE CONTROLS, printed before any zeta_K figure, and a zeta_K figure refused unless both read AS WANTED:
###   (C1) Q0's terms recomputed by terms709 at both windows, all three kinds, each S within the banked unit's ball (b709's units), and the
###        form's least eigenvalue against data/b709_grid.txt :441 (rho0: -0.0037191321) and :4501 (band: -3.5300862e-5);
###   (C2) Lambda_K(n) at n <= 50 printed beside chi(n) by both routes, Lambda(n) and Lambda_Q0(n); the split, inert and ramified primes named.
### (C3), FORCED AND NOT A TEST, printed at each window beside the zeta_K figures: S_Q0 - S_K = -PR_D, PR_D the same prime sum on the
### weights Lambda_Q0 - Lambda_K computed as a sum of its own, per kind; the two sides' balls must overlap.
### READ BESIDE IT, NOT A TEST: each least eigenvalue; at Q0's least eigenvector v (v^T M v = 1), v^T G_Q0 v, v^T G_K v, the difference
### v^T (G_Q0 - G_K) v, and the difference's share as the ratio (G_Q0 - G_K)(v) / |G_Q0(v)|.
### Routes: `run` (prints) ; `bank` (prints and writes data/b723_zetak.txt). Every value a ball (python-flint) at b696's precision.
### Written by the Write tool at b723; it writes that one bank and nothing else. Nothing here proves RH or GRH.
"""
import math
import os
import sys
import time

from flint import arb, fmpq

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b709_grid as G9            # noqa: E402  ### b709's grid, window, prime sum and terms: imported unedited
import b707_onset as O7           # noqa: E402  ### b707's gram and reading: imported unedited

W, WB = G9.W, G9.WB
bs, bl, fmt = WB.bs, WB.bl, WB.fmt
DQ = -23
POINTS = (('rho0', 'mid929_937', '6.838396011', '-0.0037191321', 'data/b709_grid.txt :441'),
          ('band', 'rung32381', '10.38532711', '-3.5300862e-5', 'data/b709_grid.txt :4501'))


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


# ================================================================================ THE CHARACTER AND THE WEIGHTS
def kronecker(a, n):
    """the Kronecker symbol (a / n), n >= 1, by the Jacobi route with the factor 2 by (a / 2) = 0, 1, -1 as a = 0, +-1, +-3 mod 8."""
    if n == 0:
        return 1 if abs(a) == 1 else 0
    res = 1
    while n % 2 == 0:
        n //= 2
        r = a % 8
        if r % 2 == 0:
            return 0
        if r in (3, 5):
            res = -res
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


def euler23(n):
    """(n / 23) by Euler's criterion: n^11 mod 23, read as 0, 1 or -1 -- the second route, since -23 = 1 mod 4 gives (-23 / n) = (n / 23)."""
    r = pow(n % 23, 11, 23)
    return 0 if n % 23 == 0 else (1 if r == 1 else -1)


def chi_table(nmax):
    c = [0] * (nmax + 1)
    bad = []
    for n in range(1, nmax + 1):
        c[n] = kronecker(DQ, n)
        if c[n] != euler23(n):
            bad.append(n)
    return c, bad


def weights(nmax):
    lz = W.lambda_z(nmax)
    lq = W.lambda_q(nmax)[0]
    chi, bad = chi_table(nmax)
    lk = [lz[n] * (1 + chi[n]) for n in range(nmax + 1)]
    ld = [lq[n] - lk[n] for n in range(nmax + 1)]
    return lz, lq, lk, ld, chi, bad


# ================================================================================ THE FORMS
def terms_obj(fam, pt, kind, lam, base):
    """S = P - PR + A at one window and kind on the weights `lam`, P, A and k(0) taken from `base` (Q0's terms at the same window)."""
    Wd = G9._window(fam, pt, kind)
    PR, nterms, _ = G9.prime_sum709(Wd, pt['N'], lam, math.isqrt(pt['N']))
    S = bl(base['P']) - PR + bl(base['A'])
    return dict(S=bs(S), PR=bs(PR), P=base['P'], A=base['A'], k0=base['k0'], prime_terms=nterms)


def quad(G, v):
    Scc, Snn, Scn = G
    return arb(v[0]) * arb(v[0]) * Scc + 2 * arb(v[0]) * arb(v[1]) * Scn + arb(v[1]) * arb(v[1]) * Snn


def least_vec(G, M):
    """Q0's least eigenvector from the midpoints, scaled so that v^T M v = 1 (as floats; the form's values at it in balls)."""
    Scc, Snn, Scn = [float(x.mid()) for x in G]
    Mcc, Mnn, Mcn = [float(x.mid()) for x in M]
    a_, b_, c_ = Mcc * Mnn - Mcn ** 2, Scc * Mnn + Snn * Mcc - 2 * Scn * Mcn, Scc * Snn - Scn ** 2
    lm = (b_ - math.sqrt(b_ * b_ - 4 * a_ * c_)) / (2 * a_)
    v1, v2 = -(Scn - lm * Mcn), Scc - lm * Mcc
    nrm = math.sqrt(v1 * v1 * Mcc + 2 * v1 * v2 * Mcn + v2 * v2 * Mnn)
    return (v1 / nrm, v2 / nrm), lm


def run(write):
    t_start = time.time()
    L = ['b723 -- COMPONENT 4 (i), (R333)(5)(i): H-ZETAK, THE DEDEKIND ZETA OF Q(sqrt -23) ON Q0`S TWO ONSET WINDOWS (%s)' % utc(), '',
         '### by tools/b723_zetak.py, on b709`s route imported unedited; the registration data/b723_registrations.txt (ii) :36-:50, committed alone',
         '### at relay 9ad26421 before any figure. The controls first; a zeta_K figure is refused unless (C1) and (C2) read AS WANTED.', '']

    def out(s=''):
        L.append(s)
        print(s, flush=True)

    U9 = G9.units()
    pts = {}
    for fam, name, a, lmin, src in POINTS:
        pts[fam] = [p for p in G9.grid(fam) if p['name'] == name][0]
    nmax = max(math.isqrt(p['N']) for p in pts.values())
    lz, lq, lk, ld, chi, bad = weights(nmax)

    # ---------------------------------------------------------------- (C1)
    out('## (C1) Q0`S TERMS RECOMPUTED BY terms709 AT BOTH WINDOWS, AGAINST b709`S BANKED UNITS AND LEAST EIGENVALUES')
    Q = {}
    c1 = True
    for fam, name, a, lmin, src in POINTS:
        pt = pts[fam]
        us = {}
        for kd in G9.KINDS:
            u = G9.terms709(fam, pt, kd, 'q0')
            b = U9[('terms', fam, kd, name, 'q0')]
            ok = bl(u['S']).overlaps(bl(b['S']))
            c1 &= ok
            us[kd] = u
            out('  %-4s %-11s %-2s | S %s | banked %s | %s s | %s' % (fam, name, kd, fmt(bl(u['S']), 14), fmt(bl(b['S']), 14), u['seconds'],
                                                               'AS WANTED' if ok else 'NOT AS WANTED'))
        G, M = O7.gram(us['C'], us['N'], us['CN'])
        rd = O7.reading(G, M)
        ok = abs(float(bl(rd['lmin']).mid()) - float(lmin)) <= 5e-11 + 1e-9 * abs(float(lmin)) and rd['reading'].startswith('NEGATIVE')
        c1 &= ok
        out('  %-4s %-11s FORM | a %s | lambda_min %s | banked %s (%s) | %s | %s' % (fam, name, fmt(bl(us['C']['a_radius']), 10), fmt(bl(rd['lmin']), 10),
                                                                         lmin, src, rd['reading'], 'AS WANTED' if ok else 'NOT AS WANTED'))
        Q[fam] = dict(us=us, G=G, M=M, rd=rd)
    out('  (C1) %s' % ('AS WANTED' if c1 else 'NOT AS WANTED'))
    out()

    # ---------------------------------------------------------------- (C2)
    out('## (C2) THE WEIGHTS AT n <= 50: chi(n) = (-23 / n) BY THE JACOBI ROUTE AND BY EULER`S CRITERION MOD 23, Lambda, Lambda_K = Lambda (1 + chi), Lambda_Q0')
    for n in range(2, 51):
        if lz[n].is_zero() and lq[n].is_zero():
            continue
        out('  n %2d | chi %2d (Euler %2d) | Lambda %s | Lambda_K %s | Lambda_Q0 %s' % (n, chi[n], euler23(n), fmt(lz[n], 10), fmt(lk[n], 10), fmt(lq[n], 10)))
    primes = [p for p in range(2, 51) if all(p % q for q in range(2, int(p ** 0.5) + 1))]
    out('  split (chi = 1): %s' % [p for p in primes if chi[p] == 1])
    out('  inert (chi = -1): %s' % [p for p in primes if chi[p] == -1])
    out('  ramified (chi = 0): %s' % [p for p in primes if chi[p] == 0])
    c2 = not bad and chi[23] == 0 and chi[2] == 1 and chi[5] == -1
    out('  the two routes agree at every n <= %d: %s (disagreements %d) ; chi(2) = 1 as -23 = 1 mod 8 ; chi(23) = 0 ; chi(5) = -1 (5 inert: -23 = 2 mod 5, a non-residue)' % (
        nmax, 'YES' if not bad else 'NO', len(bad)))
    out('  (C2) %s' % ('AS WANTED' if c2 else 'NOT AS WANTED'))
    out()
    if not (c1 and c2):
        out('### ### **REFUSED: A CONTROL NOT AS WANTED ; NO zeta_K FIGURE COMPUTED.**')
        _write(write, L)
        return 1

    # ---------------------------------------------------------------- THE zeta_K FORMS, (C3) BESIDE
    out('## THE zeta_K FORM AT EACH WINDOW (P, A, k(0) Q0`S; PR_K ON Lambda_K), (C3) BESIDE, FORCED AND NOT A TEST')
    verdicts = []
    c3 = True
    for fam, name, a, lmin, src in POINTS:
        pt = pts[fam]
        q = Q[fam]
        K, Dd = {}, {}
        for kd in G9.KINDS:
            K[kd] = terms_obj(fam, pt, kd, lk, q['us'][kd])
            Dd[kd] = terms_obj(fam, pt, kd, ld, q['us'][kd])
            lhs = bl(q['us'][kd]['S']) - bl(K[kd]['S'])
            rhs = -bl(Dd[kd]['PR'])
            ok = lhs.overlaps(rhs)
            c3 &= ok
            out('  %-4s %-2s | S_K %s | PR_K %s (%d terms) | (C3) S_Q0 - S_K %s ; -PR_D %s | %s' % (
                fam, kd, fmt(bl(K[kd]['S']), 14), fmt(bl(K[kd]['PR']), 12), K[kd]['prime_terms'], fmt(lhs, 12), fmt(rhs, 12), 'EQUAL WITHIN THE BALLS' if ok else 'NOT EQUAL'))
        G, M = O7.gram(K['C'], K['N'], K['CN'])
        rd = O7.reading(G, M)
        pos = rd['reading'].startswith('POSITIVE') and bl(rd['lmin']) > 0
        neg = bl(rd['lmin']) < 0
        verdicts.append((fam, pos, neg, rd))
        out('  %-4s FORM | a %s | lambda_min %s, lambda_max %s | det %s | %s' % (fam, a, fmt(bl(rd['lmin']), 10), fmt(bl(rd['lmax']), 6), fmt(bl(rd['det']), 6), rd['reading']))
        v, lm = least_vec(q['G'], q['M'])
        gq, gk = quad(q['G'], v), quad(G, v)
        out('  %-4s READ BESIDE, NOT A TEST: at Q0`s least eigenvector v = (%.10f, %.10f) (v^T M v = 1): G_Q0(v) %s ; G_K(v) %s ; (G_Q0 - G_K)(v) %s ; its ratio to |G_Q0(v)| %s' % (
            fam, v[0], v[1], fmt(gq, 10), fmt(gk, 10), fmt(gq - gk, 10), fmt((gq - gk) / abs(gq), 8)))
        out()
    out('  (C3) %s' % ('THE IDENTITY HOLDS WITHIN THE BALLS AT BOTH WINDOWS, ALL KINDS' if c3 else 'NOT AS FORCED: A DEFECT OF THE ROUTE'))
    out()
    held = all(p for _f, p, _n, _r in verdicts)
    fired = any(n for _f, _p, n, _r in verdicts)
    out('THE HYPOTHESIS (positive definite beyond its ball at both windows; (R333)(5): HELD, REFUTED or NOT SCORABLE): %s' % (
        'HELD' if held else ('REFUTED' if fired else 'NOT SCORABLE')))
    out('THE FALSIFIER (a least eigenvalue negative beyond its ball at either window): %s' % (
        'FIRED at %s' % [f for f, _p, n, _r in verdicts if n] if fired else 'NOT FIRED'))
    out()
    out('### ### **H-ZETAK: C1 %s ; C2 %s ; C3 %s ; rho0 %s ; band %s ; THE HYPOTHESIS %s ; %d s.**' % (
        'AS WANTED', 'AS WANTED', 'HOLDS' if c3 else 'DEFECT',
        verdicts[0][3]['reading'], verdicts[1][3]['reading'], 'HELD' if held else ('REFUTED' if fired else 'NOT SCORABLE'), int(time.time() - t_start)))
    _write(write, L)
    return 0


def _write(write, L):
    if not write:
        return
    p = os.path.join(D, 'b723_zetak.txt')
    with open(p + '.tmp', 'wb') as f:
        f.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print('written data/b723_zetak.txt')


if __name__ == '__main__':
    verb = sys.argv[1] if len(sys.argv) > 1 else ''
    if verb not in ('run', 'bank'):
        print('usage: b723_zetak.py run | bank')
        sys.exit(2)
    sys.exit(run(verb == 'bank'))
