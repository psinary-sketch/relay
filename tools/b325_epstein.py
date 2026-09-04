# -*- coding: utf-8 -*-
"""b325_epstein.py -- THE EPSTEIN CHANNELS. ### **THE NEGATIVE CONTROL'S INSTRUMENT.**

### ### **WHAT TRANSFERS FROM THE ARC AND WHAT DOES NOT.**
### The arc's places sum for zeta is `SUM_v W_v(f) = PR - A`, with `PR` the prime channel and `A`
### the archimedean channel against the kernel `Re psi(1/4 + i u/2) - log pi`.
### ### **THAT KERNEL IS ZETA'S**, because it comes from zeta's archimedean factor
### `pi^{-s/2} Gamma(s/2)`, and the corpus's own `epstein_census.py` states the Epstein one in its
### METHOD header: ### **`Lambda(s) = (sqrt(23)/2pi)^s Gamma(s) Z_Q(s)`.**
### ### **SO THE ARCHIMEDEAN CHANNEL IS A BUILD, NOT A RE-RUN**, and it is built here by the SAME
### construction the atlas used, applied to the OTHER factor:
###   ### zeta      : `pi^{-s/2} Gamma(s/2)`  ->  kernel `Re psi(1/4 + i u/2) - log pi`
###   ### Epstein   : `(sqrt23/2pi)^s Gamma(s)` -> kernel `Re psi(1/2 + i u) - log(2 pi / sqrt 23)`
### ### **HALF-ARGUMENT AGAINST WHOLE, AND A DIFFERENT CONSTANT.** ### Two different functions.

### ### **AND THE FINITE SIDE IS A BUILD TOO, FOR A REASON WORTH STATING.** ### Zeta's prime channel
### uses `Lambda(n) = log p`, the coefficients of `-zeta'/zeta`. ### Epstein's Dirichlet
### coefficients are the REPRESENTATION NUMBERS `r_Q(k)` -- and ### **`r_Q` IS NOT THE ANALOGUE OF
### ### `Lambda`.** ### The explicit formula's finite side is the coefficient sequence of
### `-Z_Q'/Z_Q`, obtained from `r_Q` by Dirichlet inversion, and this file does that inversion and
### tests it against the series it inverts.

### ### ### **WHAT THE LAWFUL CLASS DOES: ### IT TRANSFERS, AND THAT IS A MEASURED FACT.** ###
### `Lambda_Q`'s poles sit at `s = 0` and `s = 1`, exactly where zeta's do -- the corpus's census
### header writes them as `- 1/s - 1/(1-s)`. ### So the arc's vanishing conditions kill the pole
### term here as well, and the arc's own lawful seeds are lawful for this function too.
"""
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
import b321_window as WI        # noqa: E402  ### the blocked transform and the channel shape

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE FORM, FROM THE CORPUS'S OWN CENSUS HEADER:** ### *"disc -23, principal form
# ### x^2 + xy + 6y^2, h(-23) = 3."*
DISC = 23
KMAX = 4096          # ### representation numbers formed to here; the cells need far fewer
_KERN_Q = None


def rep_counts(K=KMAX):
    """### ### **`r_Q(k)` FOR `x^2 + xy + 6y^2`, FORMED THE CORPUS'S OWN WAY.**

    ### The loop bounds are `epstein_li_v3.rep_counts`'s, and fixture (i) requires this to agree
    ### with that function value for value. ### **A RE-IMPLEMENTATION THAT CANNOT REPRODUCE ITS
    ### ### ORIGINAL IS AN OVERWRITE**, which is b321's rule and it applies here.
    """
    r = [0] * (K + 1)
    ymax = int(2 * math.sqrt(K / float(DISC))) + 1
    for y in range(-ymax, ymax + 1):
        for x in range(-int(math.sqrt(K)) - abs(y) - 1, int(math.sqrt(K)) + abs(y) + 2):
            k = x * x + x * y + 6 * y * y
            if 1 <= k <= K:
                r[k] += 1
    return r


RQ = rep_counts()


def von_mangoldt_q(K=None, rq=None):
    """### ### **THE FINITE SIDE: THE COEFFICIENTS OF `-Z_Q'/Z_Q`, BY DIRICHLET INVERSION.**

    ### `Z_Q(s) = SUM r_Q(k) k^{-s}` with `r_Q(1) = 2`, so write `B(s) = Z_Q(s)/2 = SUM b_k k^{-s}`
    ### with `b_1 = 1`. ### From `-B'/B = SUM Lambda_Q(n) n^{-s}` and `-B' = L B`:
    ###   ### **`b_n log n = SUM_{d | n} Lambda_Q(d) b_{n/d}`**,
    ### which inverts to `Lambda_Q(n) = b_n log n - SUM_{d | n, d < n} Lambda_Q(d) b_{n/d}`.
    ### ### **THE CONSTANT 2 CANCELS IN A LOG-DERIVATIVE**, which is why the normalization is free.
    ### ### **AND `Lambda_Q` IS NOT `r_Q`.** ### For zeta the Dirichlet coefficients are `1` and the
    ### von Mangoldt weights are `log p`; the two are different sequences there too, and the arc's
    ### prime channel uses the second. ### Using `r_Q` here would be the same error.
    """
    rq = RQ if rq is None else rq
    K = (len(rq) - 1) if K is None else K
    b = [0.0] * (K + 1)
    for k in range(1, K + 1):
        b[k] = rq[k] / 2.0
    lam = [0.0] * (K + 1)
    for n in range(2, K + 1):
        tot = b[n] * math.log(n)
        d = 1
        while d * d <= n:
            if n % d == 0:
                if d < n:
                    tot -= lam[d] * b[n // d]
                e = n // d
                if e != d and e < n:
                    tot -= lam[e] * b[d]
            d += 1
        lam[n] = tot
    return lam


LAMQ = von_mangoldt_q()


def kernel_q(U):
    """### ### **THE EPSTEIN ARCHIMEDEAN KERNEL, DERIVED FROM THE FACTOR THE CORPUS STATES.**

    ### The atlas builds zeta's from `pi^{-s/2} Gamma(s/2)`: at `s = 1/2 + i u` the archimedean
    ### log-derivative's real part is `(1/2)(Re psi(1/4 + i u/2) - log pi)`, and the atlas's kernel
    ### is that bracket. ### **THE SAME CONSTRUCTION ON `(sqrt23/2pi)^s Gamma(s)`** gives
    ### `Re psi(1/2 + i u) - log(2 pi / sqrt 23)`, and that is what this returns.
    ### ### **NOTHING HERE IS FITTED.** ### The factor is quoted; the kernel follows from it.
    """
    from mpmath import mp, digamma, mpc, re as mre
    mp.dps = 15
    c = math.log(2.0 * math.pi / math.sqrt(DISC))
    return (np.array([float(mre(digamma(mpc(0.5, uu)))) for uu in U]) - c)


def finite_channel(v, w, lam=None):
    """### `SUM_n 2 Lambda_Q(n) n^{-1/2} w(log n)` -- the atlas's prime line with `Lambda_Q`."""
    lam = LAMQ if lam is None else lam
    L = float(v[-1])
    total, terms = 0.0, []
    nmax = int(math.exp(L) + 1e-12)
    for n in range(2, min(nmax, len(lam) - 1) + 1):
        if lam[n] == 0.0:
            continue
        ln = math.log(n)
        if ln <= L:
            val = 2.0 * lam[n] / math.sqrt(n) * float(np.interp(ln, v, w))
            if val:
                total += val
                terms.append(n)
    return total, terms


def channels_q(v, w):
    """### ### **THE EPSTEIN PLACES SUM, IN THE ATLAS'S OWN ARRANGEMENT.**

    ### `SUM_v W_v(f) = PR - A`, the same shape b321 established for zeta -- with `PR` the finite
    ### channel above and `A` the archimedean channel against `kernel_q`.
    ### ### **THE POLE TERM IS RETURNED TOO, AND IS EXPECTED TO VANISH FOR A LAWFUL `f`**, because
    ### `Lambda_Q`'s poles sit at `s = 0` and `s = 1` exactly where zeta's do.
    """
    global _KERN_Q
    P = 2.0 * float(np.trapezoid(w * np.cosh(v / 2.0), v))
    U = np.linspace(-AT.UMAX, AT.UMAX, AT.NU)
    if _KERN_Q is None or _KERN_Q[0] != (AT.UMAX, AT.NU):
        _KERN_Q = ((AT.UMAX, AT.NU), kernel_q(U))
    A = float(np.trapezoid(WI.hhat_blocked(v, w, U) * _KERN_Q[1], U) / (2.0 * math.pi))
    PR, terms = finite_channel(v, w)
    return dict(pole=P, arch=A, finite=PR, places=PR - A, terms=terms)


def sieve(n):
    """### Primes to `n`. ### **THIS EXISTS BECAUSE b321's LIST STOPS AT 31.**"""
    if n < 2:
        return []
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i in range(2, n + 1) if s[i]]


def zeta_places_full(v, w):
    """### ### **THE POSITIVE CONTROL: ZETA THROUGH THE SAME CHANNELS, WITH EVERY PRIME.**

    ### b321 proved that for a lawful `f` the zeta places sum is `-Z` with `Z` a sum of squared
    ### moduli, so ### **IT CAN NEVER BE POSITIVE.** ### Running zeta through these channels is
    ### therefore a control whose correct answer is known in advance, and a positive value condemns
    ### the instrument rather than the object.

    ### ### ### **AND IT CONDEMNED IT ONCE, WHICH IS WHY THIS FUNCTION EXISTS.** ### `b321_window`
    ### carries `PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)`, copied from the atlas's own prime
    ### loop; b321's OWN header explains why it was left at eleven: *the largest cell in this arc has
    ### `f` supported below `9`, so the list is far longer than it needs to be*. ### **BEYOND THE
    ### ARC'S CELLS IT IS NOT.** ### At `a = 32` the
    ### support reaches `1024` and the list misses almost every prime in range, and the zeta places
    ### sum came out `+0.003489041` -- ### **A VALUE b321's OWN THEOREM FORBIDS.**
    ### ### **WITH EVERY PRIME IT IS `-0.000389214`, AND THE CONTROL PASSES.**
    ### ### **b321 IS NOT RE-VERDICTED BY THIS.** ### At the arc's own cells the two agree to every
    ### printed digit -- `-0.315810512` at `a = 3` from both -- because the list is sufficient there.
    ### **THE CONSTANT IS SCOPE-BOUND, THE SCOPE WAS NEVER WRITTEN DOWN, AND THIS IS WHERE IT BIT.**
    """
    L = float(v[-1])
    nmax = int(math.exp(L) + 1e-12)
    tot, terms = 0.0, 0
    for p in sieve(max(nmax, 2)):
        m = 1
        while p ** m <= nmax:
            n = p ** m
            ln = math.log(n)
            if ln <= L:
                tot += 2.0 * math.log(p) / math.sqrt(n) * float(np.interp(ln, v, w))
                terms += 1
            m += 1
    U = np.linspace(-AT.UMAX, AT.UMAX, AT.NU)
    # ### **A LATENT DEFECT IN THE OWNER, GUARDED HERE AND NOT REPAIRED THERE.** ### `AT.kernel`
    # ### memoises its result in `_KERN` WITHOUT KEYING ON THE GRID, so a caller that once asked
    # ### for nine points gets nine points forever. ### It never bit the atlas, whose every call
    # ### uses one grid. ### **THIS ACT'S FIXTURES CALL IT AT TWO SIZES AND IT BIT IMMEDIATELY.**
    # ### The owner is READ, never edited; the guard belongs in the caller.
    if getattr(AT, '_KERN', None) is not None and len(AT._KERN) != len(U):
        AT._KERN = None
    A = float(np.trapezoid(WI.hhat_blocked(v, w, U) * AT.kernel(U), U) / (2.0 * math.pi))
    return dict(finite=tot, arch=A, places=tot - A, terms=terms)


def self_test(verbose=False):
    ok, lines = [], []

    def note(s):
        lines.append(s)

    # ### (i) ### **THE REPRESENTATION NUMBERS REPRODUCE THE CORPUS'S OWN.**
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'e_v3_reps', os.path.join(ROOT, 'tools', 'e16', 'epstein_li_v3.py'))
    theirs = None
    try:
        src = open(os.path.join(ROOT, 'tools', 'e16', 'epstein_li_v3.py'),
                   encoding='utf-8').read()
        ns = {'math': math}
        i = src.index('def rep_counts(K):')
        j = src.index('RQ = rep_counts(KTERMS)')
        exec(compile(src[i:j], 'rep_counts', 'exec'), ns)
        theirs = ns['rep_counts'](40)
    except Exception as exc:                                    # noqa: BLE001
        note('(i)    ### COULD NOT LOAD THE CORPUS rep_counts : %s' % exc)
    same = theirs is not None and all(RQ[k] == theirs[k] for k in range(41))
    ok.append(bool(same))
    note('(i)    r_Q reproduces the corpus tool to k = 40 : %s ; r_Q(1..8) = %s'
         % (same, RQ[1:9]))

    # ### (ii) ### **AND IT MUST BE ABLE TO DISAGREE.** ### The WRONG form does.
    r2 = [0] * 41
    for y in range(-9, 10):
        for x in range(-9, 10):
            k = x * x + y * y                                   # ### the norm form, not this one
            if 1 <= k <= 40:
                r2[k] += 1
    ok.append(any(r2[k] != RQ[k] for k in range(1, 41)))
    note('(ii)   the sum-of-two-squares form gives a DIFFERENT sequence : %s' % r2[1:9])

    # ### (iii) ### **THE DIRICHLET INVERSION, CHECKED BY ITS OWN EXACT IDENTITY.**
    # ### The first version of this arm compared two TRUNCATED series and missed at `4.7e-06`.
    # ### **THAT WAS A TRUNCATION ARTEFACT AND NOT AN ERROR IN THE INVERSION**: a Dirichlet
    # ### convolution truncated at `K` is not the product of two series truncated at `K`.
    # ### **THE IDENTITY THE INVERSION SOLVES IS EXACT PER COEFFICIENT** -- `b_n log n =
    # ### SUM_{d|n} Lambda_Q(d) b_{n/d}` -- and that is what this arm now tests, at every `n`.
    b = [0.0] + [RQ[k] / 2.0 for k in range(1, 2001)]
    worst, worst_n = 0.0, 0
    for n in range(2, 2001):
        lhs = b[n] * math.log(n)
        rhs = 0.0
        d = 1
        while d * d <= n:
            if n % d == 0:
                rhs += LAMQ[d] * b[n // d]
                e = n // d
                if e != d:
                    rhs += LAMQ[e] * b[d]
            d += 1
        err = abs(lhs - rhs)
        if err > worst:
            worst, worst_n = err, n
    ok.append(worst < 1e-9)
    note('(iii)  the exact identity b_n log n = SUM_d Lambda_Q(d) b_(n/d), worst over n <= 2000 :'
         ' %.3e at n = %d' % (worst, worst_n))

    # ### (iii-b) ### **AND THE TRUNCATED SERIES AGREE TO THE ORDER THE TRUNCATION ALLOWS**,
    # ### which is reported rather than barred, because the bar would be a bar on the tail.
    s_ = 3.0
    K = 3000
    bb = [0.0] + [RQ[k] / 2.0 for k in range(1, K + 1)]
    B = sum(bb[k] * k ** -s_ for k in range(1, K + 1))
    Bp = -sum(bb[k] * math.log(k) * k ** -s_ for k in range(1, K + 1))
    direct = -Bp / B
    viaL = sum(LAMQ[n] * n ** -s_ for n in range(2, K + 1))
    rel = abs(direct - viaL) / max(abs(direct), 1e-300)
    ok.append(rel < 1e-3)
    note('(iii-b) the truncated series at s = 3 : direct %.12f ; via Lambda_Q %.12f ; rel %.3e'
         ' -- a TAIL, not an error' % (direct, viaL, rel))

    # ### (iv) ### **AND Lambda_Q IS NOT r_Q**, which is the whole reason the inversion exists.
    diff = max(abs(LAMQ[n] - RQ[n]) for n in range(2, 60))
    ok.append(diff > 1e-6)
    note('(iv)   max |Lambda_Q - r_Q| over n < 60 : %.6f -- they are different sequences' % diff)

    # ### (v) ### **THE KERNEL IS NOT ZETA'S.** ### If it were, nothing here would be a new test.
    U = np.linspace(-4.0, 4.0, 9)
    kq, kz = kernel_q(U), AT.kernel(U)
    ok.append(float(np.max(np.abs(kq - kz))) > 0.1)
    note('(v)    max |kernel_Q - kernel_zeta| on |u| <= 4 : %.6f -- different functions'
         % float(np.max(np.abs(kq - kz))))

    # ### (vi) ### **THE POLE TERM VANISHES ON A LAWFUL f**, so the lawful class transfers.
    g = SM.mean_zero_variant(SM.FIXTURE_A)
    f = SQ.autocorrelation(g)
    ch = channels_q(f.v, f.w)
    ok.append(abs(ch['pole']) < 1e-12)
    note('(vi)   the pole term on a lawful f : %.3e -- the arc\'s lawful class transfers'
         % ch['pole'])

    # ### (vii) the places sum is finite and its constituents are printed.
    ok.append(np.isfinite(ch['places']))
    note('(vii)  at a = %g : finite %.9f ; arch %.9f ; places %.9f ; terms %s'
         % (SM.FIXTURE_A, ch['finite'], ch['arch'], ch['places'], ch['terms']))

    # ### (viii) ### **THE POSITIVE CONTROL, AND THE DEFECT IT CAUGHT.**
    ga = SM.mean_zero_variant(3.0)
    fa = SQ.autocorrelation(ga)
    zc = zeta_places_full(fa.v, fa.w)
    old_ = WI.channels(fa.v, fa.w)
    same = abs(zc['places'] - (old_['prime'] - old_['arch'])) < 1e-9
    ok.append(same and zc['places'] < 0.0)
    note('(viii) zeta control at a = 3 : every prime %.9f ; b321 eleven-prime %.9f ; agree %s'
         % (zc['places'], old_['prime'] - old_['arch'], same))

    # ### (ix) ### **AND THE TWO DISAGREE WHERE THE LIST RUNS OUT, WHICH IS THE MEASUREMENT.**
    gb = SM.mean_zero_variant(32.0)
    fb = SQ.autocorrelation(gb)
    zb = zeta_places_full(fb.v, fb.w)
    ob = WI.channels(fb.v, fb.w)
    ok.append(zb['places'] < 0.0 < (ob['prime'] - ob['arch']))
    note('(ix)   at a = 32 : every prime %.9f (permitted) ; eleven primes %.9f (FORBIDDEN, and'
         ' b321 proved it cannot happen -- the list, not the object)'
         % (zb['places'], ob['prime'] - ob['arch']))

    if verbose:
        for s_ in lines:
            print('    ' + s_)
    return all(ok), ok, lines


if __name__ == '__main__':
    good, arms, ls = self_test(verbose=True)
    print('  ### FIXTURES : %s  %s' % (arms, 'PASS' if good else '### FAIL ###'))
    sys.exit(0 if good else 1)
