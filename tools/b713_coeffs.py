# -*- coding: utf-8 -*-
"""b713_coeffs.py -- THE COEFFICIENT OBSERVATION AT -15, (R323)(5)(iv), AS data/b712_registrations.txt (iii) REGISTERED IT (:54-:62, read unchanged
from 67a02388): "Q1's log-derivative coefficients c(n), computed exactly from the representation counts r_Q1(n) of x^2 + xy + 4y^2 ... through a cut
fixed in data/b712_price.txt" -- the cut n <= 32532 (data/b712_price.txt :53, b711's). AN OBSERVATION, NOT A PREDICTION (:60-:61).

### THE COMPUTATION, b711's form (tools/b711_coeffs.py, IMPORTED unedited: spf_table, factor, recursion, value, show): b_n = r_Q1(n)/2 (b_1 = 1),
### c(n) = b_n log n - SUM_{d | n, 1 < d < n} c(d) b_{n/d}, each c(n) exact as a vector of rationals over the primes of n; its sign read from the
### ball SUM q_p log p at flint's precision (refused where the ball meets zero). r_Q1(n) by direct enumeration (tools/b712_genus_control.py counts,
### IMPORTED unedited, the box its form's minimum bounds).
### THE CONTROLS, computed and printed BEFORE any figure: (C1) b711's: the recursion with b_n = 1 returns von Mangoldt exactly at every n <= the cut;
### (C2) registration (ii)'s (:50-:51): the input r_Q1(n) equal at every n <= the cut to the Dirichlet coefficients of zeta(s)L(s, chi_-15) +
### L(s, chi_-3)L(s, chi_5), i.e. SUM_{d|n} chi_-15(d) + SUM_{d|n} chi_-3(d) chi_5(n/d) (the half-sum of the genus identity's two rows; Kronecker
### symbols by b712's kronecker, imported unedited); and its NEG: Q2 = 2x^2 + xy + 2y^2's counts against the same right side, wanted UNEQUAL.
### THE READINGS (:58-:61): the least n with c(n) < 0 and its value in closed form (SUM q_p log p, exact rationals); the count of negative
### coefficients through the cut; beside it the least height of a certified zero of Q1 with Re rho > 1 in b713's list (data/b713_list.json), with the
### list's off-line search region read from its tool.
### Routes: `run [dry]` -> the controls, then the readings; without `dry` written to data/b713_coeffs.txt, data/b713_coeffs.json and
### data/b713_coeffs_hashes.txt. Written by the Write tool at b713; it writes only those three banks.
"""
import hashlib
import io
import json
import math
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from flint import arb, fmpq           # noqa: E402
import b711_coeffs as C11             # noqa: E402  ### b711's recursion, imported unedited
import b712_genus_control as G        # noqa: E402  ### b712's counts and kronecker, imported unedited

ACT = 'b713'
REG = 'data/b712_registrations.txt'
CUT = 32532                           # ### data/b712_price.txt :53 (b711's floor(e^10.39))


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def divisor_sums(N):
    """the two right sides through N: s1(n) = SUM_{d|n} chi_-15(d), s2(n) = SUM_{d|n} chi_-3(d) chi_5(n/d)."""
    k15 = [0] + [G.kronecker(-15, d) for d in range(1, N + 1)]
    k3 = [0] + [G.kronecker(-3, d) for d in range(1, N + 1)]
    k5 = [0] + [G.kronecker(5, d) for d in range(1, N + 1)]
    s1, s2 = [0] * (N + 1), [0] * (N + 1)
    for d in range(1, N + 1):
        for m in range(d, N + 1, d):
            s1[m] += k15[d]
            s2[m] += k3[d] * k5[m // d]
    return s1, s2


def compute():
    t0 = time.time()
    N = CUT
    spf = C11.spf_table(N)
    one = [fmpq(0)] + [fmpq(1)] * N
    cz = C11.recursion(one, N, spf)
    bad1 = []
    for n in range(2, N + 1):
        f = C11.factor(n, spf)
        want = {next(iter(f)): fmpq(1)} if len(f) == 1 else {}
        if cz[n] != want:
            bad1.append(n)
    r1 = G.counts(G.Q1, N)
    r2 = G.counts(G.Q2, N)
    s1, s2 = divisor_sums(N)
    bad2 = [n for n in range(1, N + 1) if r1[n] != s1[n] + s2[n]]
    neg2 = [n for n in range(1, N + 1) if r2[n] != s1[n] + s2[n]]
    t1 = time.time()
    b = [fmpq(0)] + [fmpq(r1[k], 2) for k in range(1, N + 1)]
    c = C11.recursion(b, N, spf)
    vals = [None] * (N + 1)
    neg, undecided = [], []
    for n in range(2, N + 1):
        if not c[n]:
            continue
        x = C11.value(c[n])
        vals[n] = x
        if x < 0:
            neg.append(n)
        elif not x > 0:
            undecided.append(n)
    return dict(N=N, b1=b[1], c=c, vals=vals, bad1=bad1, bad2=bad2, neg2=neg2, neg=neg, undecided=undecided,
                nonzero=sum(1 for n in range(2, N + 1) if c[n]), r_nonzero=sum(1 for n in range(1, N + 1) if r1[n]),
                seconds=int(time.time() - t0), control_seconds=int(t1 - t0))


def list_zeros():
    """the least height of a certified zero with Re rho > 1 in b713's list (data/b713_list.json), and the list's off-line search region."""
    import b713_list as LST
    P9 = LST.P9
    j = json.load(io.open(os.path.join(D, '%s_list.json' % ACT), encoding='utf-8'))
    offs = [(k, arb(z['re'], z['h_re']), arb(z['im'], z['h_im'])) for k, z in enumerate(j['offline'], 1)]
    over = sorted(((float(t.mid()), k, s, t) for k, s, t in offs if s > 1), key=lambda x: x[0])
    undecided = [k for k, s, t in offs if not s > 1 and not s < 1]
    region = dict(lo='1/2 + %s' % P9.DELTA, sig_rows=P9.SIG_ROWS, right_edge=LST.SIGMA_R)
    return dict(top=j['top'], online=len(j['online']), off_pairs=len(offs), over=[(k, s.str(12), t.str(12)) for _h, k, s, t in over],
                undecided=undecided, sigma_max=max(float(s.mid()) for _k, s, _t in offs) if offs else None, region=region)


def lines(R, Z):
    N = R['N']
    L = ['%s -- (R323)(5)(iv): THE COEFFICIENT OBSERVATION AT -15, AS %s (iii) REGISTERED IT (:54-:62) -- AN OBSERVATION, NOT A PREDICTION (%s)' % (ACT, REG, utc()), '',
         '### rows are readings of c(n), Q1`s log-derivative coefficients (-Z_Q1`/Z_Q1 = SUM c(n) n^-s), computed exactly for n <= %d (data/b712_price.txt :53),' % N,
         '### each a vector of rationals over the primes of n (c(n) = SUM q_p log p); b_n = r_Q1(n)/2, Q1 = x^2 + xy + 4y^2 (b_1 = %s). THE CONTROLS FIRST.' % R['b1'], '']
    c1 = not R['bad1']
    c2 = not R['bad2']
    cn = bool(R['neg2'])
    L += ['### (C1) the recursion with b_n = 1 (zeta`s series) returns von Mangoldt exactly at every n <= %d: mismatches %d %s -- %s' % (
              N, len(R['bad1']), R['bad1'][:5], 'AS WANTED' if c1 else '### NOT AS WANTED'),
          '### (C2) r_Q1(n) against the coefficients of zeta L(chi_-15) + L(chi_-3) L(chi_5) at every n <= %d: mismatches %d %s -- %s' % (
              N, len(R['bad2']), R['bad2'][:5], 'AS WANTED' if c2 else '### NOT AS WANTED'),
          '### (C2-NEG) r_Q2(n), Q2 = 2x^2 + xy + 2y^2, against the same right side: mismatches %d (the first %s) -- %s' % (
              len(R['neg2']), R['neg2'][:5], 'UNEQUAL AS WANTED' if cn else '### EQUAL, NOT AS WANTED'),
          '### THE CONTROLS: C1 %s ; C2 %s ; C2-NEG %s' % (c1, c2, cn), '']
    neg = R['neg']
    n0 = neg[0] if neg else None
    L += ['### THE READINGS:',
          '  the coefficients through %d: nonzero %d of %d (r_Q1(n) nonzero at %d n <= %d) ; signs undecided %d' % (N, R['nonzero'], N - 1, R['r_nonzero'], N, len(R['undecided']))]
    if n0:
        L.append('  THE LEAST n WITH c(n) < 0: n = %d ; c(%d) = %s = %s' % (n0, n0, C11.show(R['c'][n0]), R['vals'][n0].str(15)))
    else:
        L.append('  THE LEAST n WITH c(n) < 0: NONE through %d' % N)
    L.append('  THE COUNT OF NEGATIVE COEFFICIENTS through %d: %d ; the first ten %s' % (N, len(neg), neg[:10]))
    if Z['over']:
        k, s, t = Z['over'][0]
        L.append('  THE LEAST HEIGHT OF A CERTIFIED ZERO OF Q1 WITH Re rho > 1 IN b713`S LIST (complete to %s): pair %d, %s + %s i ; %d such pairs of %d ; undecided %d' % (
            Z['top'], k, s, t, len(Z['over']), Z['off_pairs'], len(Z['undecided'])))
    else:
        L.append('  THE LEAST HEIGHT OF A ZERO WITH Re rho > 1: NONE IN THE LIST TO %s (%d off-line pairs; the largest off-line real part %.6f)' % (
            Z['top'], Z['off_pairs'], Z['sigma_max'] if Z['sigma_max'] is not None else float('nan')))
    L += ['  the list`s off-line search region (tools/b713_list.py over tools/b709_pairs.py DELTA, SIG_ROWS): sigma >= %s, %s candidate rows, the right edge Re s = %s' % (
              Z['region']['lo'], Z['region']['sig_rows'], Z['region']['right_edge']), '']
    L += ['### ### **AN OBSERVATION ; c(n) NEGATIVE FROM n = %s (c = %s) ; NEGATIVE COEFFICIENTS %d THROUGH %d ; Re rho > 1 IN THE LIST TO %s: %s ; C1 %s ; C2 %s ; C2-NEG %s.**' % (
              n0, C11.show(R['c'][n0]) if n0 else '-', len(neg), N, Z['top'],
              ('pair %d at %s' % (Z['over'][0][0], Z['over'][0][2])) if Z['over'] else 'NONE', c1, c2, cn)]
    j = dict(at=utc(), registration=REG, cut=N, c1=c1, c2=c2, c2_neg=cn, bad1=R['bad1'][:20], bad2=R['bad2'][:20], neg2_first=R['neg2'][:20],
             least_negative=n0, least_negative_value=C11.show(R['c'][n0]) if n0 else None, least_negative_ball=R['vals'][n0].str(30) if n0 else None,
             negatives=len(neg), negative_list=neg, nonzero=R['nonzero'], undecided=R['undecided'], list=Z, seconds=R['seconds'])
    return L, j


def _membrane(p):
    import act_membrane as MEM
    import b713_record as REC
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)


def _put(name, data):
    p = os.path.join(D, name)
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)
    return hashlib.sha256(data).hexdigest()


def run(*a):
    import b713_list as LST
    LST._free('THE COEFFICIENTS THROUGH %d' % CUT)
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
        print('usage: b713_coeffs.py run [dry]')
        sys.exit(2)
    run(*sys.argv[2:])
