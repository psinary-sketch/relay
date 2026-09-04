# -*- coding: utf-8 -*-
"""b321_window.py -- THE REMAINDER INTEGRAL, AND THE PLACES SUM, ON A LAWFUL TEST FUNCTION.

### ### **WHAT THIS FILE ADDS, AND WHY IT COULD NOT BE TAKEN OFF THE SHELF.**
### The corpus already computes a zero side, a pole term, an archimedean channel and a prime sum.
### ### **IT COMPUTES THEM FOR ITS OWN BUMP AND FOR NOTHING ELSE**: `carto_atlas.channels(a)` builds
### `bump(a)` inside itself and caps the prime loop at `log a`. ### The lawful function of this arc
### is `f = g conv g^#`, whose support in `v` is ### **TWICE** ### the seed's, and no argument to
### `channels` produces it.
### ### **SO THE CHANNELS ARE RE-FORMED HERE ON AN ARBITRARY TEST FUNCTION, AND THAT IS A
### ### RE-IMPLEMENTATION, WHICH IS A THING THAT NEEDS A FIXTURE AND NOT A PROMISE.** ### Fixture
### (i) feeds this file the atlas's OWN bump and requires ### **EVERY CHANNEL TO COME BACK
### ### BIT-FOR-BIT EQUAL TO `carto_atlas.channels(a)`.** ### If it does not, nothing else here is
### worth reading.

### ### **THE SIGNS ARE NOT THIS FILE'S TO CHOOSE.** ### Every one is quoted:
###   ### the atlas's own header -- ### *"sum_gamma hhat(gamma) = hhat(i/2) + hhat(-i/2) - PRIME +
###     ARCH [sign fixed BY the E2 calibration]"* -- which is the corpus's settled chain;
###   ### the source's (148) -- ### `SUM_rho f-tilde(rho) = INT f + INT f^# - SUM_v W_v(f)`;
###   ### the source's (149) -- ### `W_p(f) = (log p) SUM_m ( f(p^m) + f^#(p^m) )`;
###   ### and the source's page 49 -- ### *"a positivity result for the distribution W_8 = - W_R"*,
###     which is the ONLY reason this file may write `A = W_infinity` rather than `A = -W_infinity`.
### ### **THE NAVIGATOR SUPPLIED NONE OF THEM.**

### ### **AND THE REMAINDER IS THE b313 FLIPPED COPY, ON b313's READING AND ON NO NUMBER.** ### The
### two copies differ in one character. ### This file imports BOTH and reports both, because an act
### that used one and never showed the other would be asking to be believed.
"""
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))

import carto_atlas as AT            # noqa: E402  ### the settled chain, IMPORTED never edited
import b313f_qeps_layer as EF       # noqa: E402  ### the SOURCE exponent  (rho ** +0.5)
import b313r_qeps_layer as ER       # noqa: E402  ### the corpus's banked exponent (rho ** -0.5)
import b317_smear as SM             # noqa: E402
import b318_square as SQ            # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE PRIMES THE ATLAS SWEEPS, TAKEN FROM THE ATLAS AND NOT CHOSEN HERE.** ### The largest
# ### cell in this arc has `f` supported below `9`, so the list is far longer than it needs to be;
# ### it is copied in full so that the fixture against `carto_atlas.channels` is exact.
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
UBLOCK = 512          # ### the transform is blocked over `u`; the matrix is never formed whole
NEPS_UNIFORM = 4001   # ### route A: eps at this many EQUALLY SPACED nodes on [0, V]
NEPS_CHEB = 129       # ### route B: eps at this many CHEBYSHEV-LOBATTO nodes on [0, V]
PRIME_TOL = 1e-12     # ### the atlas's own `p ** k <= a + 1e-12`


# ### ==============================================================================================
# ### THE FOUR CHANNELS, RE-FORMED ON AN ARBITRARY TEST FUNCTION.
# ### ==============================================================================================
def hhat_blocked(v, w, u, block=UBLOCK):
    """### `INT w(v) cos(u v) dv`, ### **BY THE ATLAS'S OWN `hhat`**, blocked over `u`.

    ### The atlas forms `cos(outer(u, v)) @ (w dv)` in one matrix. ### For the lawful `f` that matrix
    ### is `12001 x 16385` and would be 1.6 GB, so the CALL is chunked -- ### **THE FORMULA IS NOT
    ### ### TOUCHED**, each chunk goes through `carto_atlas.hhat` verbatim.
    """
    u = np.atleast_1d(np.asarray(u, dtype=np.float64))
    out = np.empty(u.size)
    for s in range(0, u.size, block):
        e = min(s + block, u.size)
        out[s:e] = AT.hhat(v, w, u[s:e])
    return out


def prime_sum(v, w, route='corpus'):
    """### `SUM_p W_p(f)`, by two expressions of the source's (149).

    ### **ROUTE `corpus`** ### -- the atlas's own line, verbatim:
    ###   `val = 2 log p / sqrt(n) * interp(log n, v, w)`.
    ### **ROUTE `s149`** ### -- the source's (149) written out with no evenness assumed:
    ###   `W_p = log p * SUM_m ( f(p^m) + f^#(p^m) )`, with the corpus's half-line normalization
    ###   `f(x) = x^{-1/2} w(log x)` and therefore `f^#(x) = x^{-1} f(1/x) = x^{-1/2} w(-log x)`.
    ### ### **THEY ARE THE SAME NUMBER ONLY IF `w` IS EVEN**, which the lawful `f` is by
    ### construction and which route `s149` does not assume. ### That is the whole point of it.
    """
    L = float(v[-1])
    total, terms = 0.0, []
    for p in PRIMES:
        k = 1
        while p ** k <= math.exp(L) + PRIME_TOL:
            n = p ** k
            ln = math.log(n)
            if ln <= L:
                if route == 'corpus':
                    val = 2.0 * math.log(p) / math.sqrt(n) * float(np.interp(ln, v, w))
                else:
                    fx = float(np.interp(ln, v, w, left=0.0, right=0.0)) / math.sqrt(n)
                    fs = float(np.interp(-ln, v, w, left=0.0, right=0.0)) / math.sqrt(n)
                    val = math.log(p) * (fx + fs)
                if val:
                    total += val
                    terms.append(n)
            k += 1
    return total, terms


def channels(v, w):
    """### ### **THE FOUR CHANNELS OF THE EXPLICIT FORMULA, ON ANY `(v, w)`.**

    ### `Z` the zero side, `P` the pole term, `A` the archimedean channel, `PR` the prime sum, and
    ### the residual the source's (148) requires to vanish: ### **`Z - (P - PR + A)`**.
    ### **THE ARRANGEMENT IS THE ATLAS'S AND THE SIGNS ARE ITS HEADER'S**, quoted in this file's own
    ### docstring; this function chose none of them.
    """
    Z = 2.0 * float(np.sum(hhat_blocked(v, w, AT.GAM)))
    P = 2.0 * float(np.trapezoid(w * np.cosh(v / 2.0), v))
    U = np.linspace(-AT.UMAX, AT.UMAX, AT.NU)
    A = float(np.trapezoid(hhat_blocked(v, w, U) * AT.kernel(U), U) / (2.0 * math.pi))
    PR, terms = prime_sum(v, w, 'corpus')
    return dict(zero=Z, pole=P, arch=A, prime=PR,
                residual=Z - (P - PR + A), prime_terms=terms)


def trunc_bound(v, w):
    """### The atlas's own zero-side truncation bound, on an arbitrary `(v, w)`."""
    T = float(AT.GAM[-1])
    tail = hhat_blocked(v, w, np.linspace(T, T + 200.0, 401))
    return float(2.0 * np.max(np.abs(tail)) * 200.0)


# ### ==============================================================================================
# ### THE REMAINDER INTEGRAL OF THEOREM 4.7.
# ### ==============================================================================================
def _cheb_nodes(V, n):
    """### Chebyshev-Lobatto nodes on `[0, V]`, ascending, with their barycentric weights."""
    k = np.arange(n + 1)
    x = 0.5 * V * (1.0 + np.cos(math.pi * k / n))[::-1]
    bw = np.ones(n + 1)
    bw[0] = bw[-1] = 0.5
    bw = bw * ((-1.0) ** k)
    return x, bw[::-1]


def _bary(xq, x, y, bw):
    """### Barycentric interpolation at `xq`, exact at the nodes."""
    out = np.empty(xq.size)
    for i, q in enumerate(xq):
        d = q - x
        hit = np.where(np.abs(d) < 1e-15)[0]
        if hit.size:
            out[i] = y[hit[0]]
            continue
        t = bw / d
        out[i] = float(np.dot(t, y) / np.sum(t))
    return out


def remainder_integral(f, mod=EF, route='uniform', n=None):
    """### ### **`INT f(rho^-1) eps(rho) d*rho`, THE RIGHT-HAND CORRECTION OF (83).**

    ### On `R*_+` with `d*rho = drho/rho`, and `v = log rho`, this is `INT w(-v) eps(e^|v|) dv`.
    ### ### **`eps` IS EVEN BY (84)'s OWN STATEMENT** ### -- the source writes `eps(rho^-1) =
    ### eps(rho)` in the theorem itself -- and `eps(1) = 0`, so the integrand has a CORNER at the
    ### origin and both routes split there rather than integrating across it.
    ### ### **`w(-v)` IS EVALUATED AND NOT ASSUMED EQUAL TO `w(v)`.**

    ### ### **BOTH ROUTES INTEGRATE ON THE TEST FUNCTION'S OWN GRID, AND THAT IS NOT A DETAIL.** ###
    ### `w` is PIECEWISE LINEAR on `f.v` (spacing `6.4e-05` for the lawful `f`). ### A first pair of
    ### quadratures sampled it at `4.4e-04` and `1.6e-03` and ### **AGREED ONLY TO `1.6e-05`, WHICH
    ### ### MISSED THE SEALED `1e-06` BAR** -- neither route resolved the kinks of the function it
    ### was integrating. ### **THE BAR WAS NOT MOVED.** ### Integrating on `f.v` makes `w` exact by
    ### construction and leaves `eps` as the only approximation, which is what the two routes then
    ### differ in:
    ### **ROUTE `uniform`** ### -- `eps` at equally spaced nodes, piecewise-linear in between.
    ### **ROUTE `cheb`** ### -- `eps` at Chebyshev-Lobatto nodes, barycentric in between.
    ### ### **THEY SHARE THE `eps` EVALUATOR, WHICH IS DECLARED IN (B1d) AND IS NOT TWO ROUTES.**
    ### There is exactly one implementation of (84) in this corpus. ### What these two arms buy is a
    ### quadrature limit, and the registration says so before the value.
    """
    V = float(f.v[-1])
    s = f.v[f.v >= 0.0]
    if route == 'uniform':
        nodes = np.linspace(0.0, V, int(n or NEPS_UNIFORM))
        ev = np.asarray(mod.eps(np.exp(nodes)), dtype=float)
        e = np.interp(s, nodes, ev)
    else:
        nodes, bw = _cheb_nodes(V, int(n or NEPS_CHEB))
        ev = np.asarray(mod.eps(np.exp(nodes)), dtype=float)
        e = _bary(s, nodes, ev, bw)
    tot = 0.0
    for sgn in (+1.0, -1.0):
        wv = np.interp(sgn * -s, f.v, f.w, left=0.0, right=0.0)
        tot += float(np.trapezoid(wv * e, s))
    return tot


# ### ==============================================================================================
# ### THE FIXTURES. ### **(i) IS THE ONE THAT MATTERS.**
# ### ==============================================================================================
def self_test(verbose=False):
    ok, lines = [], []

    def note(s):
        lines.append(s)

    # ### (i) ### **THE RE-IMPLEMENTATION REPRODUCES THE ATLAS, ON THE ATLAS'S OWN BUMP.**
    a = 2.4
    v, w = AT.bump(a)
    mine = channels(v, w)
    theirs = AT.channels(a)
    same = [abs(mine[k] - theirs[k]) for k in ('zero', 'pole', 'arch', 'prime', 'residual')]
    ok.append(max(same) < 1e-12 and mine['prime_terms'] == theirs['prime_terms'])
    note('(i)    on the atlas OWN bump at a = %g, worst channel difference : %.3e ; '
         'prime terms %s vs %s' % (a, max(same), mine['prime_terms'], theirs['prime_terms']))

    # ### (ii) ### **AND IT MUST BE ABLE TO DISAGREE** -- a deliberately broken prime cap does.
    bad, _ = prime_sum(v, w * 0.5, 'corpus')
    ok.append(abs(bad - theirs['prime']) > 1e-9)
    note('(ii)   the same prime sum on a halved test function : %.9f vs %.9f -- differs, as it must'
         % (bad, theirs['prime']))

    # ### (iii) the two expressions of (149) agree on an even `w`.
    p1, t1 = prime_sum(v, w, 'corpus')
    p2, t2 = prime_sum(v, w, 's149')
    ok.append(abs(p1 - p2) <= 1e-12 * max(abs(p1), 1.0) and t1 == t2)
    note('(iii)  (149) by the atlas line %.12f and written out %.12f ; difference %.3e'
         % (p1, p2, abs(p1 - p2)))

    # ### (iv) ### **THE TWO REMAINDER COPIES DO NOT AGREE.** ### If they did, the exponent question
    # ### would be empty and this act would be choosing between identical things.
    g = SM.mean_zero_variant(SM.FIXTURE_A)
    f = SQ.autocorrelation(g)
    rf = remainder_integral(f, EF, 'uniform')
    rr = remainder_integral(f, ER, 'uniform')
    ok.append(abs(rf - rr) > 1e-6 * max(abs(rf), 1.0))
    note('(iv)   remainder integral, source exponent %.9f ; corpus exponent %.9f ; they DIFFER'
         % (rf, rr))

    # ### (v) the two quadratures agree.
    rg = remainder_integral(f, EF, 'cheb')
    ok.append(abs(rf - rg) < 1e-6 * max(abs(rf), 1.0))
    note('(v)    quadrature limit: uniform %.9f ; chebyshev %.9f ; relative %.3e'
         % (rf, rg, abs(rf - rg) / max(abs(rf), 1e-300)))

    # ### (vi) ### **AND THE INTEGRAL IS LINEAR IN `eps`** -- a halved remainder halves it. ### An
    # ### arm that could not detect a scaled kernel would not be checking the kernel.
    class Half(object):
        @staticmethod
        def eps(rho):
            return 0.5 * np.asarray(EF.eps(rho), dtype=float)
    rh = remainder_integral(f, Half, 'uniform')
    ok.append(abs(rh - 0.5 * rf) < 1e-9 * max(abs(rf), 1.0))
    note('(vi)   with eps halved : %.9f, against half of %.9f = %.9f'
         % (rh, rf, 0.5 * rf))

    # ### (vii) `eps(1) = 0`, which (84) requires and which makes the corner integrable.
    ok.append(abs(float(EF.eps(1.0))) < 1e-14)
    note('(vii)  eps(1) = %.3e, as (84) requires' % abs(float(EF.eps(1.0))))

    # ### (viii) the truncation bound is finite and positive at the widest cell used here.
    tb = trunc_bound(f.v, f.w)
    ok.append(np.isfinite(tb) and tb >= 0.0)
    note('(viii) the zero-side truncation bound at a = %g : %.3e' % (SM.FIXTURE_A, tb))

    if verbose:
        for s in lines:
            print('    ' + s)
    return all(ok), ok, lines


if __name__ == '__main__':
    good, arms, ls = self_test(verbose=True)
    print('  ### FIXTURES : %s  %s' % (arms, 'PASS' if good else '### FAIL ###'))
    sys.exit(0 if good else 1)
