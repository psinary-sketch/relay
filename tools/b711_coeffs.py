# -*- coding: utf-8 -*-
"""b711_coeffs.py -- THE COEFFICIENT OBSERVATION, (R321)(5), AS data/b710_registrations.txt (iii) REGISTERED IT (:71-:80, committed at b710's step
zero before any number, unchanged): "Q0's log-derivative coefficients c(n) through n = e^{10.39} (about 32532, past the band's onset rung 32381),
computed exactly from the representation counts r_Q(n) of x^2 + xy + 6y^2 (the Dirichlet series of Z_Q and its log-derivative's coefficients by the
recursion over divisors, in exact rationals times log n where the coefficient carries one)". AN OBSERVATION, NO HYPOTHESIS.

### THE COMPUTATION: r_Q(n) by b694's count (tools/b694_witness_terms.py lambda_q :291-:317, IMPORTED unedited: its r), b_n = r_Q(n)/2 (b_1 = 1),
### c(n) = b_n log n - SUM_{d | n, 1 < d < n} c(d) b_{n/d} (b694's recursion, :309-:315) carried EXACTLY: each c(n) a vector of rationals over the
### primes p | n, c(n) = SUM_p q_p log p, log n = SUM_p v_p(n) log p. The logs of distinct primes are linearly independent over Q, so c(n) = 0 exactly
### where its vector is zero and otherwise its sign is read from the ball SUM_p q_p log p at 128 bits (refused where the ball meets zero).
### THE CUT: n <= floor(e^10.39) = 32532 (e^10.39 = 32532.7; data/b710_citation_check.txt's row for e^10.39).
### THE CONTROLS, computed and printed BEFORE any figure: (C1) the recursion with b_n = 1 for every n (zeta's series) returning von Mangoldt
### exactly -- log p at every prime power p^k <= the cut, the zero vector at every other n; (C2) the exact Q0 vector's ball at every n <= the cut
### overlapping b694's ball Lambda_Q(n) (lambda_q, the form's coefficients at b707-b709), and the zero vector exactly where b694's ball is the zero.
### THE READINGS (:75-:79): the least n with c(n) < 0 and its value, the navigator's expectation (n = 48, c(48) = -2 log 48, "from the navigator's
### exact computation") printed beside as an expectation and NOT checked; the count of negative coefficients through the cut; beside it the least
### height of a certified zero with Re rho > 1 in the list (tools/b709_pairs.py extended_rows over its banked units, b675's 180 representatives and
### the bands to 325), or "none in the list to 325" with the list's off-line search region read from its tool and its upper sigma printed.
### Routes: `run [dry]` -> the controls, then the readings, printed; without `dry` written to data/b711_coeffs.txt, data/b711_coeffs.json and
### data/b711_coeffs_hashes.txt. Written by the Write tool at b711; it writes only those three banks. Nothing here proves RH or GRH.
"""
import hashlib
import json
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

import b694_witness_terms as W    # noqa: E402  ### b694's r_Q and Lambda_Q, imported unedited

ACT = 'b711'
REG = 'data/b710_registrations.txt'
CUT = int(math.floor(math.exp(10.39)))     # ### 32532
EXPECT = (48, {2: fmpq(-8), 3: fmpq(-2)})  # ### the navigator's expectation c(48) = -2 log 48 = -8 log 2 - 2 log 3 (:75-:76), not checked
LIST_TOP = 325


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def spf_table(n):
    s = list(range(n + 1))
    for p in range(2, int(n ** 0.5) + 1):
        if s[p] == p:
            for m in range(p * p, n + 1, p):
                if s[m] == m:
                    s[m] = p
    return s


def factor(n, spf):
    out = {}
    while n > 1:
        p = spf[n]
        out[p] = out.get(p, 0) + 1
        n //= p
    return out


def recursion(b, N, spf):
    """c(n) exactly for n <= N: c(n) = b_n log n - SUM_{d | n, 1 < d < n} c(d) b_{n/d}, each c a dict {p: fmpq} (zero entries dropped)."""
    acc = [None] * (N + 1)
    c = [None] * (N + 1)
    for n in range(2, N + 1):
        v = dict(acc[n]) if acc[n] else {}
        if b[n] != 0:
            for p, e in factor(n, spf).items():
                v[p] = v.get(p, fmpq(0)) + b[n] * e
        v = dict((p, q) for p, q in v.items() if q != 0)
        c[n] = v
        if v:
            for e in range(2, N // n + 1):
                if b[e] != 0:
                    m = n * e
                    if acc[m] is None:
                        acc[m] = {}
                    am = acc[m]
                    for p, q in v.items():
                        am[p] = am.get(p, fmpq(0)) - q * b[e]
    return c


def value(v):
    tot = arb(0)
    for p, q in v.items():
        tot += arb(q) * arb(p).log()
    return tot


def show(v):
    return ' + '.join('(%s) log %d' % (q, p) for p, q in sorted(v.items())) or '0'


def controls(N, spf, lamq):
    # ### (C1) zeta's series
    one = [fmpq(0)] + [fmpq(1)] * N
    cz = recursion(one, N, spf)
    bad1 = []
    for n in range(2, N + 1):
        f = factor(n, spf)
        want = {next(iter(f)): fmpq(1)} if len(f) == 1 else {}
        if cz[n] != want:
            bad1.append(n)
    # ### (C2) Q0's exact vector against b694's balls
    return cz, bad1


def compute():
    t0 = time.time()
    N = CUT
    spf = spf_table(N)
    lamq, r = W.lambda_q(N)
    b = [fmpq(r[k], 2) for k in range(N + 1)]
    cz, bad1 = controls(N, spf, lamq)
    t1 = time.time()
    c = recursion(b, N, spf)
    bad2, zero_mismatch, overlap = [], [], 0
    vals = [None] * (N + 1)
    for n in range(2, N + 1):
        x = value(c[n]) if c[n] else arb(0)
        vals[n] = x
        if not c[n]:
            if not lamq[n].is_zero() and not lamq[n].contains(0):
                zero_mismatch.append(n)
        elif not x.overlaps(lamq[n]):
            bad2.append(n)
        else:
            overlap += 1
    neg, undecided = [], []
    for n in range(2, N + 1):
        if not c[n]:
            continue
        x = vals[n]
        if x < 0:
            neg.append(n)
        elif not x > 0:
            undecided.append(n)
    return dict(N=N, b1=b[1], c=c, vals=vals, bad1=bad1, bad2=bad2, zero_mismatch=zero_mismatch, overlap=overlap, neg=neg, undecided=undecided,
                nonzero=sum(1 for n in range(2, N + 1) if c[n]), r_nonzero=sum(1 for n in range(1, N + 1) if r[n]), seconds=int(time.time() - t0),
                control_seconds=int(t1 - t0))


def list_zeros():
    """the least height of a zero with Re rho > 1 in the list to 325 (b709's extended rows over its banked units), and the search region."""
    import b709_pairs as P9
    U = P9.units()
    top = P9._complete_to(P9._bands(U), U)
    rows, n_on, n_off = P9.extended_rows(U, top)
    over = sorted(((float(t.mid()), nm, s, t) for nm, s, t in rows if s > 1), key=lambda x: x[0])
    sig = dict(delta=P9.DELTA, lo='1/2 + %s' % P9.DELTA, upper_to_310='%.2f' % (0.55 + 0.05 * (P9.SIG_ROWS - 1)), upper_from_310='1.00')
    offs = [(nm, s, t) for nm, s, t in rows if nm.startswith('off')]
    smax = max(float(s.mid()) for _nm, s, _t in offs) if offs else None
    return dict(top=top, rows=len(rows), off_rows=len(offs), over=[(nm, s.str(12), t.str(12)) for _h, nm, s, t in over], sigma_max=smax, region=sig)


def lines(R, Z):
    N = R['N']
    L = ['%s -- COMPONENT 3, (R321)(5): THE COEFFICIENT OBSERVATION, AS %s (iii) REGISTERED IT (:71-:80) -- AN OBSERVATION, NO HYPOTHESIS (%s)' % (ACT, REG, utc()), '',
         '### rows are readings of c(n), Q0`s log-derivative coefficients (-Z_Q`/Z_Q = SUM c(n) n^-s), computed exactly for n <= %d = floor(e^10.39), each a' % N,
         '### vector of rationals over the primes of n (c(n) = SUM q_p log p); b_n = r_Q(n)/2 by b694`s count (b_1 = %s). THE CONTROLS FIRST, THEN THE READINGS.' % R['b1'], '']
    c1 = not R['bad1']
    c2 = not R['bad2'] and not R['zero_mismatch']
    L += ['### (C1) the recursion with b_n = 1 (zeta`s series) returns von Mangoldt exactly at every n <= %d: mismatches %d %s -- %s' % (
              N, len(R['bad1']), R['bad1'][:5], 'AS WANTED' if c1 else '### NOT AS WANTED'),
          '### (C2) the exact Q0 vector against b694`s ball Lambda_Q(n) (tools/b694_witness_terms.py lambda_q): %d nonzero vectors overlapping their balls, '
          '%d not overlapping %s, %d zero vectors against a ball excluding 0 %s -- %s' % (
              R['overlap'], len(R['bad2']), R['bad2'][:5], len(R['zero_mismatch']), R['zero_mismatch'][:5], 'AS WANTED' if c2 else '### NOT AS WANTED'),
          '### THE CONTROLS: C1 %s ; C2 %s' % (c1, c2), '']
    neg = R['neg']
    n0 = neg[0] if neg else None
    L += ['### THE READINGS:',
          '  the coefficients through %d: nonzero %d of %d (r_Q(n) nonzero at %d n <= %d) ; signs undecided %d' % (N, R['nonzero'], N - 1, R['r_nonzero'], N, len(R['undecided']))]
    if n0:
        L.append('  THE LEAST n WITH c(n) < 0: n = %d ; c(%d) = %s = %s' % (n0, n0, show(R['c'][n0]), R['vals'][n0].str(15)))
    else:
        L.append('  THE LEAST n WITH c(n) < 0: NONE through %d' % N)
    e_n, e_v = EXPECT
    L += ['  beside it, the navigator`s expectation (:75-:76), NOT checked: n = %d, c(%d) = -2 log 48 (= %s) ; the computed c(%d) = %s' % (
              e_n, e_n, show(e_v), e_n, show(R['c'][e_n]) if R['c'][e_n] else '0'),
          '  THE COUNT OF NEGATIVE COEFFICIENTS through %d: %d ; the first ten %s' % (N, len(neg), neg[:10])]
    if Z['over']:
        L.append('  THE LEAST HEIGHT OF A ZERO WITH Re rho > 1 IN THE LIST TO %s: %s at %s (sigma %s) ; %d such rows' % (Z['top'], Z['over'][0][0], Z['over'][0][2], Z['over'][0][1], len(Z['over'])))
    else:
        L.append('  THE LEAST HEIGHT OF A ZERO WITH Re rho > 1: NONE IN THE LIST TO %s (%d rows, %d off-line; the largest off-line real part %.6f)' % (
            Z['top'], Z['rows'], Z['off_rows'], Z['sigma_max'] if Z['sigma_max'] is not None else float('nan')))
    L += ['  the list`s off-line search region (tools/b709_pairs.py DELTA, SIG_ROWS, candidates): the right half-strip sigma >= %s, its candidate grid`s upper '
          'sigma %s for the bands to 310 and %s from 310 on' % (Z['region']['lo'], Z['region']['upper_to_310'], Z['region']['upper_from_310']), '']
    L += ['### ### **AN OBSERVATION ; c(n) NEGATIVE FROM n = %s (c = %s) ; NEGATIVE COEFFICIENTS %d THROUGH %d ; THE NAVIGATOR`S n = 48 PRINTED BESIDE, NOT CHECKED ; '
          'Re rho > 1 IN THE LIST TO %s: %s ; C1 %s ; C2 %s.**' % (
              n0, show(R['c'][n0]) if n0 else '-', len(neg), N, Z['top'], ('%s at %s' % (Z['over'][0][0], Z['over'][0][2])) if Z['over'] else 'NONE', c1, c2)]
    j = dict(at=utc(), registration=REG, cut=N, c1=c1, c2=c2, bad1=R['bad1'][:20], bad2=R['bad2'][:20], zero_mismatch=R['zero_mismatch'][:20],
             least_negative=n0, least_negative_value=show(R['c'][n0]) if n0 else None, least_negative_ball=R['vals'][n0].str(30) if n0 else None,
             negatives=len(neg), negative_list=neg, nonzero=R['nonzero'], undecided=R['undecided'], c48=show(R['c'][48]) if R['c'][48] else '0',
             expectation='n = 48, c(48) = -2 log 48 (not checked)', list=Z, seconds=R['seconds'])
    return L, j


def _membrane(p):
    """(R321)(2)(ii), standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    import b711_record as REC
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)


def _put(name, data):
    p = os.path.join(D, name)
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)
    return hashlib.sha256(data).hexdigest()


def run(*a):
    R = compute()
    print('  computed through %d in %d s (controls %d s)' % (R['N'], R['seconds'], R['control_seconds']), flush=True)
    Z = list_zeros()
    L, j = lines(R, Z)
    print(NL.join(L))
    if 'dry' in a:
        return
    h1 = _put('%s_coeffs.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    h2 = _put('%s_coeffs.json' % ACT, (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    H = ['%s -- THE COEFFICIENT OBSERVATION`S BANKS, THEIR sha256 (%s)' % (ACT, utc()), '', '  %s  data/%s_coeffs.txt' % (h1, ACT),
         '  %s  data/%s_coeffs.json' % (h2, ACT), '', '### ### **BANKS 2 HASHED.**']
    _put('%s_coeffs_hashes.txt' % ACT, (NL.join(H) + NL).encode('utf-8'))
    print(H[-1])


if __name__ == '__main__':
    if (sys.argv[1] if len(sys.argv) > 1 else '') != 'run':
        print('usage: b711_coeffs.py run [dry]')
        sys.exit(2)
    run(*sys.argv[2:])
