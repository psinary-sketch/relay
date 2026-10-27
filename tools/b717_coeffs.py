# -*- coding: utf-8 -*-
"""b717_coeffs.py -- THE COEFFICIENTS AT -39, (R327)(4)(iv): "the log-derivative coefficients through the cut 32532: the least negative index,
its closed form, b(n), the prime factors of n with the classes representing them; registration (ii) read HELD or REFUTED on both clauses", as
data/b716_registrations.txt (ii) registered it (:39-:57, read unchanged from dc5e808f).

### CARRIED FROM tools/b713_coeffs.py (read through the Read tool :1-:189) by the Write tool: the act's names b713 -> b717, the form
### Q1 = x^2 + xy + 10y^2, the registration b716's (ii). THE COMPUTATION UNCHANGED: b711's recursion (tools/b711_coeffs.py, IMPORTED unedited:
### spf_table, factor, recursion, value, show), b_n = r_Q1(n)/2 (b_1 = 1), c(n) = b_n log n - SUM_{d | n, 1 < d < n} c(d) b_{n/d}, each c(n)
### exact as a vector of rationals over the primes of n, its sign read from the ball SUM q_p log p (refused where the ball meets zero); r_Q(n)
### by direct enumeration (tools/b716_genus_control.py counts, IMPORTED unedited, its box set by the module's DISC, which this tool sets to the
### discriminant of the form it counts and restores).
### THE CONTROLS, registration (ii)'s (:54-:57), computed and printed BEFORE any -39 figure (`controls`, banked in data/b717_coeffs_controls.json):
### (C1) the recursion with b_n = 1 returns von Mangoldt exactly at every n <= the cut;
### (C2) r_Q1(n) against the coefficients of (1/2)[zeta L(chi_-39) + L(chi_-3) L(chi_13)] + L_K(psi) through the cut -- the three lines of (i)
###      re-read at the cut: r_Q1 + r_Q3 + 2 r_Q2 = 2 SUM chi_-39(d), r_Q1 + r_Q3 - 2 r_Q2 = 2 SUM chi_-3(d) chi_13(n/d), r_Q2 = r_Q2', and the
###      quartic pair's a(n) = (r_Q1 - r_Q3)/2 on the Hecke laws (b716's hecke_laws), so r_Q1 = (s1 + s2)/2 + a at every n; NEG: Q3's counts
###      in Q1's place in the trivial line, wanted UNEQUAL;
### (C3) the route reproducing Q0's least index 48 (c(48) = (-8) log 2 + (-2) log 3, data/b711_coeffs.txt :12, 1066 negatives :14) and
###      -15's 24 (c(24) = (-6) log 2 + (-2) log 3, data/b713_coeffs.txt :13, 756 negatives :14) through the same cut, unchanged.
### THE READINGS: the least n with c(n) < 0, its closed form SUM q_p log p, b(n) = c(n)/log n exactly (the logs of distinct primes independent
### over Q: b(n) is a rational where the vector is proportional to n's exponents, and "not a rational multiple" otherwise), the primes of n
### and, for each, the reduced forms of -39 representing it (Q(x, y) = p by enumeration); THE LAW (:51-:53): clause 1 b(n) = -2; clause 2 a
### prime of n represented by no form of the principal class (Q1(x, y) = p with no integer solution); HELD where both hold, REFUTED otherwise.
### Beside it the count of negatives through the cut and the least height of a zero with Re rho > 1 in b717's list.
### Routes: `controls` ; `run [dry]` (refused before the controls are banked as wanted) -> data/b717_coeffs.txt, data/b717_coeffs.json,
### data/b717_coeffs_hashes.txt. Written by the Write tool at b717; it writes only those banks.
"""
import hashlib
import io
import json
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
import b716_genus_control as G        # noqa: E402  ### b716's counts, kronecker, reduced_forms, hecke_laws, imported unedited

ACT = 'b717'
REG = 'data/b716_registrations.txt'
CUT = 32532                           # ### (R327)(4)(iv)
Q1, Q2, Q2I, Q3 = (1, 1, 10), (2, 1, 5), (2, -1, 5), (3, 3, 4)
C3_WANT = {'Q0 (1, 1, 6), -23': ((1, 1, 6), -23, 48, '(-8) log 2 + (-2) log 3', 1066, 'data/b711_coeffs.txt :12, :14'),
           '-15 (1, 1, 4)': ((1, 1, 4), -15, 24, '(-6) log 2 + (-2) log 3', 756, 'data/b713_coeffs.txt :13, :14')}
CTL = '%s_coeffs_controls.json' % ACT


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def counts(f, disc, n_max):
    """b716's counts with its box set by the form's own discriminant (b716's DISC restored after)."""
    keep = G.DISC
    G.DISC = disc
    try:
        return G.counts(f, n_max)
    finally:
        G.DISC = keep


def sieve_line(chi_d, chi_nd, n_max):
    """SUM_{d | n} chi_d(d) chi_nd(n/d) for 1 <= n <= n_max by a sieve over d."""
    s = [0] * (n_max + 1)
    cd = [0] + [chi_d(d) for d in range(1, n_max + 1)]
    cn = [0] + [chi_nd(e) for e in range(1, n_max + 1)]
    for d in range(1, n_max + 1):
        if cd[d]:
            for e in range(1, n_max // d + 1):
                s[d * e] += cd[d] * cn[e]
    return s


def coeffs(r, N, spf):
    b = [fmpq(0)] + [fmpq(r[k], 2) for k in range(1, N + 1)]
    c = C11.recursion(b, N, spf)
    neg, undecided, vals = [], [], {}
    for n in range(2, N + 1):
        if not c[n]:
            continue
        x = C11.value(c[n])
        if x < 0:
            neg.append(n)
            vals[n] = x
        elif not x > 0:
            undecided.append(n)
    return b, c, neg, undecided, vals


def controls(*a):
    import b717_list as LST
    LST._free('THE COEFFICIENT CONTROLS THROUGH %d' % CUT)
    t0 = time.time()
    N = CUT
    spf = C11.spf_table(N)
    one = [fmpq(0)] + [fmpq(1)] * N
    cz = C11.recursion(one, N, spf)
    bad1 = []
    for n in range(2, N + 1):
        f = C11.factor(n, spf)
        if cz[n] != ({next(iter(f)): fmpq(1)} if len(f) == 1 else {}):
            bad1.append(n)
    r1, r2, r2i, r3 = (counts(f, -39, N) for f in (Q1, Q2, Q2I, Q3))
    s1 = sieve_line(lambda d: G.kronecker(-39, d), lambda e: 1, N)
    s2 = sieve_line(lambda d: G.kronecker(-3, d), lambda e: G.kronecker(13, e), N)
    aq = [0] + [(r1[n] - r3[n]) // 2 for n in range(1, N + 1)]
    bm, br = G.hecke_laws(aq, N)
    bad2 = [n for n in range(1, N + 1) if r1[n] + r3[n] + 2 * r2[n] != 2 * s1[n] or r1[n] + r3[n] - 2 * r2[n] != 2 * s2[n] or r2[n] != r2i[n]
            or (r1[n] - r3[n]) % 2 or 2 * r1[n] != s1[n] + s2[n] + 2 * aq[n]]
    neg2 = [n for n in range(1, N + 1) if r3[n] + r3[n] + 2 * r2[n] != 2 * s1[n]]
    c3 = []
    for name, (f, disc, n_want, v_want, cnt_want, src) in C3_WANT.items():
        _b, c, neg, und, _v = coeffs(counts(f, disc, N), N, spf)
        n0 = neg[0] if neg else None
        c3.append(dict(name=name, n=n0, value=C11.show(c[n0]) if n0 else None, count=len(neg), undecided=len(und), n_want=n_want, v_want=v_want,
                       count_want=cnt_want, src=src, ok=(n0 == n_want and C11.show(c[n0]) == v_want and len(neg) == cnt_want)))
    j = dict(at=utc(), cut=N, c1=not bad1, bad1=bad1[:20], c2=not bad2 and not bm and not br, bad2=bad2[:20], hecke_mult_off=len(bm),
             hecke_rec_off=len(br), c2_neg=bool(neg2), neg2_count=len(neg2), neg2_first=neg2[:5], c3=c3, seconds=int(time.time() - t0))
    j['ok'] = j['c1'] and j['c2'] and j['c2_neg'] and all(x['ok'] for x in c3)
    for l in control_lines(j):
        print(l)
    if 'dry' in a:
        return
    _put(CTL, (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def control_lines(j):
    N = j['cut']
    L = ['### (C1) the recursion with b_n = 1 (zeta`s series) returns von Mangoldt exactly at every n <= %d: mismatches %d %s -- %s' % (
             N, len(j['bad1']), j['bad1'][:5], 'AS WANTED' if j['c1'] else '### NOT AS WANTED'),
         '### (C2) r_Q1(n) against the coefficients of (1/2)[zeta L(chi_-39) + L(chi_-3) L(chi_13)] + L_K(psi) at every n <= %d (the trivial and genus lines,' % N,
         '###      r_Q2 = r_Q2`, a(n) = (r_Q1 - r_Q3)/2 on the Hecke laws): mismatches %d %s ; Hecke laws off %d coprime, %d prime powers -- %s' % (
             len(j['bad2']), j['bad2'][:5], j['hecke_mult_off'], j['hecke_rec_off'], 'AS WANTED' if j['c2'] else '### NOT AS WANTED'),
         '### (C2-NEG) r_Q3(n) in Q1`s place in the trivial line: mismatches %d (the first %s) -- %s' % (
             j['neg2_count'], j['neg2_first'], 'UNEQUAL AS WANTED' if j['c2_neg'] else '### EQUAL, NOT AS WANTED')]
    for x in j['c3']:
        L.append('### (C3) %s through %d: the least negative n = %s, c = %s, negatives %d (wanted %d, %s, %d ; %s) -- %s' % (
            x['name'], N, x['n'], x['value'], x['count'], x['n_want'], x['v_want'], x['count_want'], x['src'], 'REPRODUCED' if x['ok'] else '### NOT REPRODUCED'))
    L.append('### THE CONTROLS: C1 %s ; C2 %s ; C2-NEG %s ; C3 %s ; %d s' % (j['c1'], j['c2'], j['c2_neg'], all(x['ok'] for x in j['c3']), j['seconds']))
    return L


def represented_by(p):
    """the reduced forms of -39 with Q(x, y) = p for some integers x, y (enumeration over the box the form's minimum bounds)."""
    out = []
    for f in (Q1, Q2, Q2I, Q3):
        if counts(f, -39, p)[p]:
            out.append(f)
    return out


def list_zeros():
    j = json.load(io.open(os.path.join(D, '%s_list.json' % ACT), encoding='utf-8'))
    over = [(k, z) for k, z in enumerate(j['offline'], 1) if float(z['re']) > 1.0]
    return dict(top=j['top'], off_pairs=len(j['offline']), over=[(k, z['re'][:12], z['im'][:12]) for k, z in over],
                sigma_max=max(float(z['re']) for z in j['offline']) if j['offline'] else None)


def run(*a):
    ctl = json.load(io.open(os.path.join(D, CTL), encoding='utf-8')) if os.path.exists(os.path.join(D, CTL)) else {}
    if not ctl.get('ok'):
        sys.exit('### THE CONTROLS ARE NOT BANKED AS WANTED (data/%s) -- NOTHING RUN' % CTL)
    import b717_list as LST
    LST._free('THE COEFFICIENTS THROUGH %d' % CUT)
    t0 = time.time()
    N = CUT
    spf = C11.spf_table(N)
    r1 = counts(Q1, -39, N)
    b, c, neg, undecided, vals = coeffs(r1, N, spf)
    n0 = neg[0] if neg else None
    L = ['%s -- (R327)(4)(iv): THE COEFFICIENTS AT -39 THROUGH %d, AS %s (ii) REGISTERED THEM (:39-:57), READ HELD OR REFUTED (%s)' % (ACT, N, REG, utc()), '',
         '### rows are readings of c(n), Q1`s log-derivative coefficients (-Z_Q1`/Z_Q1 = SUM c(n) n^-s), computed exactly for n <= %d, each a vector of' % N,
         '### rationals over the primes of n (c(n) = SUM q_p log p); b_n = r_Q1(n)/2, Q1 = x^2 + xy + 10y^2 (b_1 = %s). THE CONTROLS FIRST (data/%s, %s).' % (b[1], CTL, ctl['at']), '']
    L += control_lines(ctl) + ['', '### THE READINGS:',
                               '  the coefficients through %d: nonzero %d of %d (r_Q1(n) nonzero at %d n <= %d) ; signs undecided %d' % (
                                   N, sum(1 for n in range(2, N + 1) if c[n]), N - 1, sum(1 for n in range(1, N + 1) if r1[n]), N, len(undecided))]
    j = dict(at=utc(), registration=REG, cut=N, controls_at=ctl['at'], negatives=len(neg), negative_list=neg, undecided=undecided)
    if n0:
        fac = C11.factor(n0, spf)
        v = c[n0]
        ratios = set(v.get(p, fmpq(0)) / e for p, e in fac.items()) | set(fmpq(1) for p in v if p not in fac)
        bn = list(ratios)[0] if len(ratios) == 1 and set(v) <= set(fac) else None
        reps = dict((p, represented_by(p)) for p in fac)
        cl1 = bn == fmpq(-2)
        cl2 = any(Q1 not in reps[p] for p in fac)
        L += ['  THE LEAST n WITH c(n) < 0: n = %d = %s ; c(%d) = %s = %s' % (n0, ' . '.join('%d^%d' % (p, e) if e > 1 else '%d' % p for p, e in sorted(fac.items())),
                                                                              n0, C11.show(v), vals[n0].str(15)),
              '  b(n) = c(n)/log n = %s%s' % (bn if bn is not None else 'NOT A RATIONAL', ' (c(n) = %s log %d)' % (bn, n0) if bn is not None else ''),
              '  the primes of n and the reduced forms of -39 representing each: ' + ' ; '.join(
                  '%d by %s' % (p, ', '.join('%dx^2 %s %dxy + %dy^2' % (f[0], '+' if f[1] >= 0 else '-', abs(f[1]), f[2]) for f in reps[p]) or 'NO FORM')
                  for p in sorted(fac)),
              '', '### THE LAW (%s :51-:53):' % REG,
              '  clause 1, b(n) = -2: b(%d) = %s -- %s' % (n0, bn, 'HELD' if cl1 else 'REFUTED'),
              '  clause 2, n divisible by a prime represented by no form of the principal class (Q1(x, y) = p unsolved): %s -- %s' % (
                  ', '.join('%d %s' % (p, 'unrepresented by Q1' if Q1 not in reps[p] else 'represented by Q1') for p in sorted(fac)), 'HELD' if cl2 else 'REFUTED'),
              '  REGISTRATION (ii): %s' % ('HELD' if cl1 and cl2 else 'REFUTED')]
        j.update(least_negative=n0, factors=dict((str(p), e) for p, e in fac.items()), value=C11.show(v), ball=vals[n0].str(30), b=str(bn),
                 represented=dict((str(p), [list(f) for f in reps[p]]) for p in fac), clause1=cl1, clause2=cl2, verdict='HELD' if cl1 and cl2 else 'REFUTED')
    else:
        L.append('  THE LEAST n WITH c(n) < 0: NONE through %d -- the law has no index to read: REFUTED (its object absent)' % N)
        j.update(least_negative=None, verdict='REFUTED')
    Z = list_zeros()
    L += ['', '  THE COUNT OF NEGATIVE COEFFICIENTS through %d: %d ; the first ten %s' % (N, len(neg), neg[:10]),
          '  THE LEAST HEIGHT OF A ZERO WITH Re rho > 1 IN b717`S LIST (complete to %s, the counts certified and the off-line points located): %s' % (
              Z['top'], ('pair %d at %s + %s i' % Z['over'][0]) if Z['over'] else 'NONE (%d off-line pairs; the largest off-line real part %.6f)' % (Z['off_pairs'], Z['sigma_max'])),
          '', '### ### **c(n) NEGATIVE FROM n = %s (c = %s, b(n) = %s) ; NEGATIVE COEFFICIENTS %d THROUGH %d ; REGISTRATION (ii) %s ; %d s.**' % (
              n0, j.get('value'), j.get('b'), len(neg), N, j['verdict'], int(time.time() - t0))]
    j['list'] = Z
    print(NL.join(L))
    if 'dry' in a:
        return
    h1 = _put('%s_coeffs.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    h2 = _put('%s_coeffs.json' % ACT, (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    h3 = hashlib.sha256(open(os.path.join(D, CTL), 'rb').read()).hexdigest()
    H = ['%s -- THE COEFFICIENTS` BANKS, THEIR sha256 (%s)' % (ACT, utc()), '', '  %s  data/%s_coeffs.txt' % (h1, ACT),
         '  %s  data/%s_coeffs.json' % (h2, ACT), '  %s  data/%s' % (h3, CTL), '', '### ### **BANKS 3 HASHED.**']
    _put('%s_coeffs_hashes.txt' % ACT, (NL.join(H) + NL).encode('utf-8'))
    print(H[-1])


def _membrane(p):
    import act_membrane as MEM
    import b717_record as REC
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)


def _put(name, data):
    p = os.path.join(D, name)
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)
    return hashlib.sha256(data).hexdigest()


ROUTES = dict(controls=controls, run=run)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b717_coeffs.py controls [dry] | run [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
