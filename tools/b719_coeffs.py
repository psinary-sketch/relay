# -*- coding: utf-8 -*-
"""b719_coeffs.py -- THE COEFFICIENTS AT -20 AND -47, (R329)(6)(ii): "computed exactly through the cut 32532 at each discriminant by
b711's route, its controls C1-C3 printed before any figure: the least index with b(n) < 0, its value in closed form, b(n), its prime factors
with the class representing each, and the decomposition of b(n) into its log-series terms, a(n) and the ordered pair sum among them, as
data/b718_decomp.txt read the three. Every row of data/b718_registrations.txt and then H-24 and H-47 read HELD or REFUTED on its own
clauses." Written whole at b719 by the Write tool, after tools/b717_coeffs.py (read through the Read tool :1-:200).

### THE ROUTE, b711's: tools/b711_coeffs.py's recursion IMPORTED unedited (spf_table, factor, recursion, value, show) -- b_n = r_Q1(n)/2
### (b_1 = 1), c(n) = b_n log n - SUM_{d | n, 1 < d < n} c(d) b_{n/d}, each c(n) exact as a vector of rationals over the primes of n, its sign
### read from the ball SUM q_p log p; r_Q(n) by direct enumeration (tools/b716_genus_control.py counts, IMPORTED unedited, its box set by the
### module's DISC, set to the form's discriminant and restored, as b717's wrapper did).
### THE CONTROLS (`controls`, banked in data/b719_coeffs_controls.json before any figure):
### (C1) the recursion with b_n = 1 returns von Mangoldt exactly at every n <= the cut (b711's (C1));
### (C2) at each of -20 and -47: the trivial line SUM over the reduced forms of r_f(n) = 2 SUM_{d | n} chi_D(d); and r_Q1(n)/2 equal to the
###      number of principal ideals of norm n read from the primes' classes (tools/b718_classgroup.py ideal_classes, the second way); at -20
###      the genus line r_Q1 - r_Q2 = 2 SUM chi_-4(d) chi_5(n/d); NEG: r_Q2 in Q1's place in the class count, wanted UNEQUAL;
### (C3) the route reproducing -23's 48 (data/b711_coeffs.txt :12, :14), -15's 24 (data/b713_coeffs.txt :13, :14) and -39's 120
###      (data/b717_coeffs.txt :16, :25) through the same cut, their closed forms and negative counts.
### THE READINGS at each discriminant, as data/b718_decomp.txt read the three: n0, its closed form, b(n0) = c(n0)/log n0 exactly, and beside
### it b(n0) by the Omega derivation (tools/b718_classgroup.py log_coeffs, exact) -- the two equal; a(n0), the ordered pair sum, the k >= 3
### factorizations, a - pair/2; the proper divisors with a != 0; each prime of n0, its kind, the class of a prime ideal above it and the
### reduced forms representing it. Then the rows, each HELD or REFUTED: b718's law (clause 1, clause 2, and clause 2's strong form, every
### prime of n0 unrepresented by Q1) at each; the prediction PRED-20, PRED-47; H-24 at each and on the pair; H-47.
### Routes: `controls [dry]` ; `run [dry]` (refused before the controls are banked as wanted) -> data/b719_coeffs.txt, data/b719_coeffs.json.
"""
import ctypes
import io
import json
import os
import sys
import time
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from flint import fmpq                # noqa: E402
import b711_coeffs as C11             # noqa: E402  ### b711's recursion, imported unedited
import b716_genus_control as G        # noqa: E402  ### b716's counts and kronecker, imported unedited
import b718_classgroup as CG          # noqa: E402  ### b718's class group, imported unedited

ACT = 'b719'
CUT = 32532
HOLD_MB = 2560
DISCS = {-20: dict(Q1=(1, 0, 5), forms=[(1, 0, 5), (2, 2, 3)]),
         -47: dict(Q1=(1, 1, 12), forms=[(1, 1, 12), (2, -1, 6), (2, 1, 6), (3, -1, 4), (3, 1, 4)])}
C3_WANT = [('-23 (1, 1, 6)', (1, 1, 6), -23, 48, '(-8) log 2 + (-2) log 3', 1066, 'data/b711_coeffs.txt :12, :14'),
           ('-15 (1, 1, 4)', (1, 1, 4), -15, 24, '(-6) log 2 + (-2) log 3', 756, 'data/b713_coeffs.txt :13, :14'),
           ('-39 (1, 1, 10)', (1, 1, 10), -39, 120, '(-6) log 2 + (-2) log 3 + (-2) log 5', 571, 'data/b717_coeffs.txt :16, :25')]
PRED = {-20: 36, -47: 168}
CTL = '%s_coeffs_controls.json' % ACT


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


class _MS(ctypes.Structure):
    _fields_ = [('dwLength', ctypes.c_ulong), ('dwMemoryLoad', ctypes.c_ulong), ('ullTotalPhys', ctypes.c_ulonglong),
                ('ullAvailPhys', ctypes.c_ulonglong), ('ullTotalPageFile', ctypes.c_ulonglong), ('ullAvailPageFile', ctypes.c_ulonglong),
                ('ullTotalVirtual', ctypes.c_ulonglong), ('ullAvailVirtual', ctypes.c_ulonglong), ('ullAvailExtendedVirtual', ctypes.c_ulonglong)]


def free_or_exit(what):
    m = _MS()
    m.dwLength = ctypes.sizeof(_MS)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    mb = m.ullAvailPhys // 2 ** 20
    print('### FREE MEMORY BEFORE %s: %d MB (the hold %d MB) -- %s' % (what, mb, HOLD_MB, 'MET' if mb >= HOLD_MB else 'NOT MET, NOTHING RUN'))
    if mb < HOLD_MB:
        sys.exit(1)


def counts(f, disc, n_max):
    """b716's counts with its box set by the form's own discriminant (b716's DISC restored after)."""
    keep = G.DISC
    G.DISC = disc
    try:
        return G.counts(f, n_max)
    finally:
        G.DISC = keep


def sieve_line(chi_d, chi_nd, n_max):
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


def class_count(D_, N, P):
    """the number of principal ideals of norm n, n <= N, from the primes' classes (b718's ideal_classes)."""
    F, e, Tb, ok = CG.group(D_)
    pc = dict((p, CG.prime_class(D_, p)) for p in P if p <= N)
    a = [0] * (N + 1)
    a[1] = 1
    for n in range(2, N + 1):
        a[n] = CG.ideal_classes(D_, n, P, Tb, e, pc).get(e, 0)
    return a, ok


def controls(*a):
    free_or_exit('THE COEFFICIENT CONTROLS THROUGH %d' % CUT)
    t0 = time.time()
    N = CUT
    spf = C11.spf_table(N)
    P = CG.primes_upto(N)
    one = [fmpq(0)] + [fmpq(1)] * N
    cz = C11.recursion(one, N, spf)
    bad1 = []
    for n in range(2, N + 1):
        f = C11.factor(n, spf)
        if cz[n] != ({next(iter(f)): fmpq(1)} if len(f) == 1 else {}):
            bad1.append(n)
    c2 = {}
    for D_, spec in DISCS.items():
        if sorted(CG.reduced_forms(D_)) != sorted(spec['forms']):
            sys.exit('### THE REDUCED FORMS OF %d ARE %s, NOT b718`S -- NOTHING RUN' % (D_, CG.reduced_forms(D_)))
        rs = dict((f, counts(f, D_, N)) for f in spec['forms'])
        s1 = sieve_line(lambda d, D_=D_: G.kronecker(D_, d), lambda e: 1, N)
        triv = [n for n in range(1, N + 1) if sum(r[n] for r in rs.values()) != 2 * s1[n]]
        acl, ok = class_count(D_, N, P)
        q1 = rs[spec['Q1']]
        cls = [n for n in range(1, N + 1) if q1[n] % 2 or q1[n] // 2 != acl[n]]
        q2 = rs[spec['forms'][1]]
        neg = [n for n in range(1, N + 1) if q2[n] % 2 or q2[n] // 2 != acl[n]]
        gen = []
        if D_ == -20:
            s2 = sieve_line(lambda d: G.kronecker(-4, d), lambda e: G.kronecker(5, e), N)
            gen = [n for n in range(1, N + 1) if q1[n] - q2[n] != 2 * s2[n]]
        c2[D_] = dict(triv=len(triv), triv_first=triv[:5], cls=len(cls), cls_first=cls[:5], neg=len(neg), neg_first=neg[:5],
                      genus=(len(gen) if D_ == -20 else None), axioms=all(ok.values()),
                      ok=(not triv and not cls and not gen and bool(neg) and all(ok.values())))
    c3 = []
    for name, f, disc, n_want, v_want, cnt_want, src in C3_WANT:
        _b, c, negl, und, _v = coeffs(counts(f, disc, N), N, spf)
        n0 = negl[0] if negl else None
        c3.append(dict(name=name, n=n0, value=C11.show(c[n0]) if n0 else None, count=len(negl), undecided=len(und), n_want=n_want,
                       v_want=v_want, count_want=cnt_want, src=src, ok=(n0 == n_want and C11.show(c[n0]) == v_want and len(negl) == cnt_want)))
    j = dict(at=utc(), cut=N, c1=not bad1, bad1=bad1[:20], c2=dict((str(k), v) for k, v in c2.items()), c3=c3, seconds=int(time.time() - t0))
    j['ok'] = j['c1'] and all(v['ok'] for v in c2.values()) and all(x['ok'] for x in c3)
    for l in control_lines(j):
        print(l)
    if 'dry' in a:
        return
    _put(CTL, (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    print('written data/%s' % CTL)


def control_lines(j):
    N = j['cut']
    L = ['### (C1) the recursion with b_n = 1 (zeta`s series) returns von Mangoldt exactly at every n <= %d: mismatches %d %s -- %s' % (
        N, len(j['bad1']), j['bad1'][:5], 'AS WANTED' if j['c1'] else '### NOT AS WANTED')]
    for D_, v in sorted(j['c2'].items(), key=lambda kv: -int(kv[0])):
        L.append('### (C2) D = %s through %d: the trivial line SUM_f r_f = 2 SUM chi_D(d) misses %d %s ; r_Q1/2 against the principal ideals by the '
                 'primes` classes misses %d %s (the group`s axioms %s)%s ; NEG r_Q2/2 in Q1`s place misses %d (the first %s) -- %s' % (
                     D_, N, v['triv'], v['triv_first'], v['cls'], v['cls_first'], 'ALL HOLD' if v['axioms'] else 'NOT ALL',
                     (' ; the genus line r_Q1 - r_Q2 = 2 SUM chi_-4(d) chi_5(n/d) misses %d' % v['genus']) if v['genus'] is not None else '',
                     v['neg'], v['neg_first'], 'AS WANTED' if v['ok'] else '### NOT AS WANTED'))
    for x in j['c3']:
        L.append('### (C3) %s through %d: the least negative n = %s, c = %s, negatives %d (wanted %d, %s, %d ; %s) -- %s' % (
            x['name'], N, x['n'], x['value'], x['count'], x['n_want'], x['v_want'], x['count_want'], x['src'],
            'REPRODUCED' if x['ok'] else '### NOT REPRODUCED'))
    L.append('### THE CONTROLS: C1 %s ; C2 %s ; C3 %s ; %d s' % (j['c1'], all(v['ok'] for v in j['c2'].values()), all(x['ok'] for x in j['c3']), j['seconds']))
    return L


def form_s(f):
    a, b, c = f
    return '%dx^2 %s %dxy + %dy^2' % (a, '+' if b >= 0 else '-', abs(b), c) if b else '%dx^2 + %dy^2' % (a, c)


def reading(D_, spec, N, spf, P):
    q1 = spec['Q1']
    r1 = counts(q1, D_, N)
    b, c, neg, undecided, vals = coeffs(r1, N, spf)
    out = dict(D=D_, negatives=len(neg), first=neg[:10], undecided=len(undecided), nonzero=sum(1 for n in range(2, N + 1) if c[n]),
               rnz=sum(1 for n in range(1, N + 1) if r1[n]))
    n0 = neg[0] if neg else None
    out['n0'] = n0
    if not n0:
        return out
    fac = C11.factor(n0, spf)
    v = c[n0]
    ratios = set(v.get(p, fmpq(0)) / e for p, e in fac.items())
    bn = list(ratios)[0] if len(ratios) == 1 and set(v) <= set(fac) else None
    a_int = [0] + [r1[k] // 2 for k in range(1, N + 1)]
    a_int[1] = 1
    bo, _Om = CG.log_coeffs(a_int, n0, P)
    F, e, Tb, _ok = CG.group(D_)
    reps = {}
    for p in fac:
        rp = [f for f in spec['forms'] if counts(f, D_, p)[p]]
        t, g = CG.prime_class(D_, p)
        reps[p] = dict(kind=t, cls=g, order=CG.order(g, e, Tb) if g else None, forms=rp, by_q1=(q1 in rp))
    pair = CG.pair_sum(a_int, n0)
    k3 = CG.ordered_factorizations(a_int, n0)
    divs = [(d, a_int[d]) for d in range(2, n0) if n0 % d == 0 and a_int[d]]
    out.update(fac=sorted(fac.items()), closed=C11.show(v), ball=vals[n0].str(15), b=(str(bn) if bn is not None else None),
               b_omega=str(bo[n0]), a=a_int[n0], pair=pair, k3=k3, a_half=str(Fraction(a_int[n0]) - Fraction(pair, 2)), divs=divs,
               reps=dict((p, dict(kind=x['kind'], cls=form_s(x['cls']) if x['cls'] else None, order=x['order'],
                                  forms=[form_s(f) for f in x['forms']], by_q1=x['by_q1'])) for p, x in reps.items()))
    return out


def rows_of(R):
    """every row, HELD or REFUTED on its own clauses (NOT SCORABLE where n0 is absent through the cut)."""
    rows = []
    for D_ in (-20, -47):
        r = R[D_]
        if not r['n0']:
            for name in ('b718 law clause 1', 'b718 law clause 2', 'b718 law clause 2 (strong)', 'PRED%d' % D_, 'H-24 at %d' % D_):
                rows.append((name, D_, 'NOT SCORABLE', 'no n <= %d with b(n) < 0' % CUT))
            continue
        bn = r['b']
        unrep = [p for p, x in r['reps'].items() if not x['by_q1']]
        rows.append(('b718 law clause 1', D_, 'HELD' if bn == '-2' else 'REFUTED', 'b(%d) = %s' % (r['n0'], bn)))
        rows.append(('b718 law clause 2', D_, 'HELD' if unrep else 'REFUTED', 'primes unrepresented by Q1: %s' % (unrep or 'NONE')))
        rows.append(('b718 law clause 2 (strong)', D_, 'HELD' if len(unrep) == len(r['reps']) else 'REFUTED',
                     'every prime of n0 unrepresented by Q1: %s of %s' % (len(unrep), len(r['reps']))))
        rows.append(('PRED%d' % D_, D_, 'HELD' if (r['n0'] == PRED[D_] and bn == '-2') else 'REFUTED',
                     'computed n0 %d, b %s ; predicted %d, -2' % (r['n0'], bn, PRED[D_])))
        rows.append(('H-24 at %d' % D_, D_, 'HELD' if r['n0'] % 24 == 0 else 'REFUTED', '%d mod 24 = %d' % (r['n0'], r['n0'] % 24)))
    sc = [x for x in rows if x[0].startswith('H-24 at')]
    rows.append(('H-24 (the pair)', None, 'NOT SCORABLE' if any(x[2] == 'NOT SCORABLE' for x in sc) else
                 ('HELD' if all(x[2] == 'HELD' for x in sc) else 'REFUTED'), ' ; '.join('%s %s' % (x[0], x[2]) for x in sc)))
    r = R[-47]
    rows.append(('H-47', -47, 'NOT SCORABLE' if not r['n0'] else ('HELD' if r['n0'] % 24 else 'REFUTED'),
                 ('n0(-47) %s, 24 divides it: %s ; the premise, the orders above 2 and 3: %s' % (
                     r['n0'], (r['n0'] % 24 == 0) if r['n0'] else '-', H47_PREMISE.get('text')))))
    return rows


H47_PREMISE = {}


def run(*a):
    ctl = json.load(io.open(os.path.join(D, CTL), encoding='utf-8')) if os.path.exists(os.path.join(D, CTL)) else {}
    if not ctl.get('ok'):
        sys.exit('### THE CONTROLS ARE NOT BANKED AS WANTED (data/%s) -- NOTHING RUN' % CTL)
    free_or_exit('THE COEFFICIENTS THROUGH %d' % CUT)
    t0 = time.time()
    N = CUT
    spf = C11.spf_table(N)
    P = CG.primes_upto(N)
    F, e, Tb, _ok = CG.group(-47)
    H47_PREMISE['text'] = ', '.join('%d: %s of order %s' % (p, CG.prime_class(-47, p)[0], CG.order(CG.prime_class(-47, p)[1], e, Tb)
                                                         if CG.prime_class(-47, p)[1] else '-') for p in (2, 3))
    R = dict((D_, reading(D_, spec, N, spf, P)) for D_, spec in DISCS.items())
    L = ['%s -- (R329)(6)(ii): THE COEFFICIENTS AT -20 AND -47 THROUGH %d BY b711`S ROUTE, EVERY ROW READ HELD OR REFUTED (%s)' % (ACT, N, utc()), '',
         '### rows are readings of c(n), Q1`s log-derivative coefficients (-Z_Q1`/Z_Q1 = SUM c(n) n^-s), exact for n <= %d, each a vector of rationals' % N,
         '### over the primes of n (c(n) = SUM q_p log p); b_n = r_Q1(n)/2 (b_1 = 1); b(n) = c(n)/log n, the coefficient of log(Z_Q1/2). The registrations',
         '### committed before: data/b719_registrations.txt at ac88ffb1 (H-24, H-47) and 7e743b4d (PRED-20, PRED-47). THE CONTROLS FIRST (data/%s, %s).' % (CTL, ctl['at']), '']
    L += control_lines(ctl) + ['']
    for D_ in (-20, -47):
        r = R[D_]
        L += ['## D = %d, Q1 = %s: nonzero c(n) %d of %d (r_Q1(n) nonzero at %d n <= %d) ; signs undecided %d' % (
            D_, form_s(DISCS[D_]['Q1']), r['nonzero'], N - 1, r['rnz'], N, r['undecided'])]
        if not r['n0']:
            L += ['  NO n <= %d WITH c(n) < 0' % N, '']
            continue
        L += ['  THE LEAST n WITH c(n) < 0: n0 = %d = %s ; c(n0) = %s = %s' % (
                  r['n0'], ' . '.join(('%d^%d' % (p, k)) if k > 1 else '%d' % p for p, k in r['fac']), r['closed'], r['ball']),
              '  b(n0) = c(n0)/log n0 = %s ; by the Omega derivation %s ; EQUAL %s' % (r['b'], r['b_omega'], r['b'] == r['b_omega']),
              '  the decomposition: a(n0) %d ; the ordered pair sum %d ; k >= 3 factorizations %d ; a - pair/2 = %s' % (r['a'], r['pair'], r['k3'], r['a_half']),
              '  the proper divisors with nonzero a: ' + ', '.join('%d (%d)' % dv for dv in r['divs']),
              '  each prime of n0: ' + ' ; '.join('%d %s, a prime ideal above it in the class of %s (order %s), represented by %s, by Q1: %s' % (
                  p, x['kind'], x['cls'], x['order'], ', '.join(x['forms']) or 'NO FORM', x['by_q1']) for p, x in sorted(r['reps'].items(), key=lambda kv: int(kv[0]))),
              '  THE COUNT OF NEGATIVE COEFFICIENTS through %d: %d ; the first ten %s' % (N, r['negatives'], r['first']), '']
    rows = rows_of(R)
    L += ['### THE ROWS, EACH ON ITS OWN CLAUSES (data/b718_registrations.txt (4) :28-:33; data/b719_registrations.txt):']
    L += ['  %-28s %-6s %-12s %s' % (n, '' if d is None else d, v, why) for n, d, v, why in rows]
    held = sum(1 for x in rows if x[2] == 'HELD')
    ref = sum(1 for x in rows if x[2] == 'REFUTED')
    L += ['', '### ### **n0(-20) = %s, b = %s ; n0(-47) = %s, b = %s ; ROWS %d: HELD %d, REFUTED %d, NOT SCORABLE %d ; H-24 %s ; H-47 %s ; %d s.**' % (
        R[-20]['n0'], R[-20].get('b'), R[-47]['n0'], R[-47].get('b'), len(rows), held, ref, len(rows) - held - ref,
        [x for x in rows if x[0] == 'H-24 (the pair)'][0][2], [x for x in rows if x[0] == 'H-47'][0][2], int(time.time() - t0))]
    print(NL.join(L))
    if 'dry' in a:
        return
    _put('%s_coeffs.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    _put('%s_coeffs.json' % ACT, (json.dumps(dict(at=utc(), cut=N, controls_at=ctl['at'], readings=dict((str(k), v) for k, v in R.items()),
                                                  rows=[dict(row=n, D=d, verdict=v, why=w) for n, d, v, w in rows]),
                                             indent=1, ensure_ascii=False, default=str) + NL).encode('utf-8'))
    print('written data/%s_coeffs.txt, .json' % ACT)


def _put(name, data):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)


if __name__ == '__main__':
    route = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = dict(controls=controls, run=run).get(route)
    if fn is None:
        sys.exit('usage: b719_coeffs.py controls [dry] | run [dry]')
    fn(*sys.argv[2:])
