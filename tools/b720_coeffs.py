# -*- coding: utf-8 -*-
"""b720_coeffs.py -- THE COEFFICIENTS AT -35 AND -40, (R330)(3): "the coefficients through the cut 32532 by b711's route, controls C1-C3
before any figure. Print n0, b(n0), its prime factors with classes, and its decomposition into a(n0) and the ordered pair sum. Every row
reads HELD/REFUTED, with the FORCED parts apart." Written whole at b720 by the Write tool, after tools/b719_coeffs.py (read through the Read
tool :1-:325; the carried copy, data/b720_carry_coeffs.txt, composed b719's rows and was replaced whole).

### THE ROUTE, b711's: tools/b711_coeffs.py's recursion IMPORTED unedited (spf_table, factor, recursion, value, show) -- b_n = r_Q1(n)/2
### (b_1 = 1), c(n) = b_n log n - SUM_{d | n, 1 < d < n} c(d) b_{n/d}, each c(n) exact as a vector of rationals over the primes of n, its sign
### read from the ball SUM q_p log p; r_Q(n) by direct enumeration (tools/b716_genus_control.py counts, IMPORTED unedited, its box set by the
### module's DISC, set to the form's discriminant and restored, as b717's and b719's wrappers did).
### THE CONTROLS (`controls`, banked in data/b720_coeffs_controls.json before any figure):
### (C1) the recursion with b_n = 1 returns von Mangoldt exactly at every n <= the cut (b711's (C1));
### (C2) at each of -35 and -40: the trivial line SUM over the reduced forms of r_f(n) = 2 SUM_{d | n} chi_D(d); r_Q1(n)/2 equal to the
###      number of principal ideals of norm n read from the primes' classes (tools/b718_classgroup.py ideal_classes, the second way); the
###      genus line r_Q1 - r_Q2 = 2 SUM chi_d1(d) chi_d2(n/d) (-35 = -7 . 5, -40 = -8 . 5); NEG: r_Q2 in Q1's place, wanted UNEQUAL;
### (C3) the route reproducing the five banked least indices through the same cut, their closed forms and negative counts: -23's 48,
###      -15's 24, -39's 120, -20's 36, -47's 168 (data/b711_coeffs.txt :12, :14 ; data/b713_coeffs.txt :13, :14 ; data/b717_coeffs.txt :16,
###      :25 ; data/b719_coeffs.txt :16, :21, :24, :29).
### THE READINGS at each discriminant: n0, its closed form, b(n0) = c(n0)/log n0 exactly and by the Omega derivation (tools/b718_classgroup.py
### log_coeffs) -- the two equal; a(n0), the ordered pair sum, the k >= 3 factorizations, a - pair/2; the proper divisors with a != 0; each
### prime of n0, its kind, the class of a prime ideal above it and the forms representing it. Then the rows of data/b720_registrations.txt,
### each HELD or REFUTED: THE LAW (clause 1, clause 2, clause 2's strong form) at each; PRED-35, PRED-40; H-DECOMP T1-T4 and overall, F1
### and F2 printed apart as FORCED and counted for nothing; H-RR at -40 and -35, labelled NOT BLIND.
### Routes: `controls [dry]` ; `run [dry]` (refused before the controls are banked as wanted) -> data/b720_coeffs.txt, data/b720_coeffs.json.
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

ACT = 'b720'
CUT = 32532
HOLD_MB = 2560
DISCS = {-35: dict(Q1=(1, 1, 9), forms=[(1, 1, 9), (3, 1, 3)], genus=(-7, 5)),
         -40: dict(Q1=(1, 0, 10), forms=[(1, 0, 10), (2, 0, 5)], genus=(-8, 5))}
C3_WANT = [('-23 (1, 1, 6)', (1, 1, 6), -23, 48, '(-8) log 2 + (-2) log 3', 1066, 'data/b711_coeffs.txt :12, :14'),
           ('-15 (1, 1, 4)', (1, 1, 4), -15, 24, '(-6) log 2 + (-2) log 3', 756, 'data/b713_coeffs.txt :13, :14'),
           ('-39 (1, 1, 10)', (1, 1, 10), -39, 120, '(-6) log 2 + (-2) log 3 + (-2) log 5', 571, 'data/b717_coeffs.txt :16, :25'),
           ('-20 (1, 0, 5)', (1, 0, 5), -20, 36, '(-4) log 2 + (-4) log 3', 478, 'data/b719_coeffs.txt :16, :21'),
           ('-47 (1, 1, 12)', (1, 1, 12), -47, 168, '(-6) log 2 + (-2) log 3 + (-2) log 7', 759, 'data/b719_coeffs.txt :24, :29')]
PRED = {-35: (135, '-2'), -40: (100, '-1/2')}         # ### data/b720_registrations.txt, PRED-35 and PRED-40 (54fc03d9)
INERT = {-35: 2, -40: 3}                               # ### the inert prime of each, F1 and F2
HDECOMP = {-35: {2: 0, 3: 3}, -40: {2: 2, 3: 0}}       # ### T1-T4
HRR = {-40: 100, -35: 1225}                            # ### H-RR: b(q1^2 q2^2) = -1/2, NOT BLIND
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


def b_of(c, n, spf):
    """b(n) = c(n)/log n exactly, when c(n) is (b . e_p) log p over n's primes p^e_p; '0' when c(n) is zero; None otherwise."""
    fac = C11.factor(n, spf)
    v = c[n]
    if not v:
        return '0'
    ratios = set(v.get(p, fmpq(0)) / e for p, e in fac.items())
    return str(list(ratios)[0]) if len(ratios) == 1 and set(v) <= set(fac) else None


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
            sys.exit('### THE REDUCED FORMS OF %d ARE %s, NOT THE REGISTRATION`S -- NOTHING RUN' % (D_, CG.reduced_forms(D_)))
        rs = dict((f, counts(f, D_, N)) for f in spec['forms'])
        s1 = sieve_line(lambda d, D_=D_: G.kronecker(D_, d), lambda e: 1, N)
        triv = [n for n in range(1, N + 1) if sum(r[n] for r in rs.values()) != 2 * s1[n]]
        acl, ok = class_count(D_, N, P)
        q1 = rs[spec['Q1']]
        cls = [n for n in range(1, N + 1) if q1[n] % 2 or q1[n] // 2 != acl[n]]
        q2 = rs[spec['forms'][1]]
        neg = [n for n in range(1, N + 1) if q2[n] % 2 or q2[n] // 2 != acl[n]]
        d1, d2 = spec['genus']
        s2 = sieve_line(lambda d, d1=d1: G.kronecker(d1, d), lambda e, d2=d2: G.kronecker(d2, e), N)
        gen = [n for n in range(1, N + 1) if q1[n] - q2[n] != 2 * s2[n]]
        c2[D_] = dict(triv=len(triv), triv_first=triv[:5], cls=len(cls), cls_first=cls[:5], neg=len(neg), neg_first=neg[:5],
                      genus=len(gen), genus_first=gen[:5], genus_chars=[d1, d2], axioms=all(ok.values()),
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
                 'primes` classes misses %d %s (the group`s axioms %s) ; the genus line r_Q1 - r_Q2 = 2 SUM chi_%d(d) chi_%d(n/d) misses %d %s ; '
                 'NEG r_Q2/2 in Q1`s place misses %d (the first %s) -- %s' % (
                     D_, N, v['triv'], v['triv_first'], v['cls'], v['cls_first'], 'ALL HOLD' if v['axioms'] else 'NOT ALL',
                     v['genus_chars'][0], v['genus_chars'][1], v['genus'], v['genus_first'],
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
    out['hrr'] = dict(n=HRR[D_], b=b_of(c, HRR[D_], spf), closed=C11.show(c[HRR[D_]]) if c[HRR[D_]] else '0')
    n0 = neg[0] if neg else None
    out['n0'] = n0
    if not n0:
        return out
    fac = C11.factor(n0, spf)
    v = c[n0]
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
    out.update(fac=sorted(fac.items()), closed=C11.show(v), ball=vals[n0].str(15), b=b_of(c, n0, spf),
               b_omega=str(bo[n0]), a=a_int[n0], pair=pair, k3=k3, a_half=str(Fraction(a_int[n0]) - Fraction(pair, 2)), divs=divs,
               reps=dict((p, dict(kind=x['kind'], cls=form_s(x['cls']) if x['cls'] else None, order=x['order'],
                                  forms=[form_s(f) for f in x['forms']], by_q1=x['by_q1'])) for p, x in reps.items()))
    return out


def _exp(n, p):
    k = 0
    while n % p == 0:
        n, k = n // p, k + 1
    return k


def rows_of(R):
    """every row of data/b720_registrations.txt, HELD or REFUTED on its own clauses (NOT SCORABLE where n0 is absent through the cut);
    the FORCED parts returned apart."""
    rows, forced = [], []
    for D_ in (-35, -40):
        r = R[D_]
        if not r['n0']:
            for name in ('THE LAW clause 1', 'THE LAW clause 2', 'THE LAW clause 2 (strong)', 'PRED%d' % D_):
                rows.append((name, D_, 'NOT SCORABLE', 'no n <= %d with b(n) < 0' % CUT))
            for p in (2, 3):
                rows.append(('H-DECOMP T(%d, %d)' % (D_, p), D_, 'NOT SCORABLE', 'no n0 through the cut'))
            forced.append(('H-DECOMP F(%d, %d)' % (D_, INERT[D_]), D_, 'NOT SCORABLE', 'no n0 through the cut'))
            continue
        bn = r['b']
        unrep = [p for p, x in r['reps'].items() if not x['by_q1']]
        rows.append(('THE LAW clause 1', D_, 'HELD' if bn == '-2' else 'REFUTED', 'b(%d) = %s' % (r['n0'], bn)))
        rows.append(('THE LAW clause 2', D_, 'HELD' if unrep else 'REFUTED', 'primes unrepresented by Q1: %s' % (unrep or 'NONE')))
        rows.append(('THE LAW clause 2 (strong)', D_, 'HELD' if len(unrep) == len(r['reps']) else 'REFUTED',
                     'every prime of n0 unrepresented by Q1: %s of %s' % (len(unrep), len(r['reps']))))
        pn, pb = PRED[D_]
        rows.append(('PRED%d' % D_, D_, 'HELD' if (r['n0'] == pn and bn == pb) else 'REFUTED',
                     'computed n0 %d, b %s ; predicted %d, %s' % (r['n0'], bn, pn, pb)))
        for p in (2, 3):
            got, want = _exp(r['n0'], p), HDECOMP[D_][p]
            rows.append(('H-DECOMP T(%d, %d)' % (D_, p), D_, 'HELD' if got == want else 'REFUTED',
                         'the exponent of %d in n0 = %d is %d ; registered %d' % (p, r['n0'], got, want)))
        q = INERT[D_]
        forced.append(('H-DECOMP F(%d, %d)' % (D_, q), D_, 'FORCED, %s' % ('AS FORCED' if _exp(r['n0'], q) % 2 == 0 else 'NOT AS FORCED'),
                       'the exponent of the inert prime %d in n0 = %d is %d, even: %s' % (q, r['n0'], _exp(r['n0'], q), _exp(r['n0'], q) % 2 == 0)))
    ts = [x for x in rows if x[0].startswith('H-DECOMP T')]
    rows.append(('H-DECOMP (overall)', None, 'NOT SCORABLE' if any(x[2] == 'NOT SCORABLE' for x in ts) else
                 ('HELD' if all(x[2] == 'HELD' for x in ts) else 'REFUTED'), ' ; '.join('%s %s' % (x[0], x[2]) for x in ts)))
    for D_ in (-40, -35):
        h = R[D_]['hrr']
        rows.append(('H-RR at %d (NOT BLIND)' % D_, D_, 'HELD' if h['b'] == '-1/2' else 'REFUTED',
                     'b(%d) = %s (c = %s) ; registered -1/2' % (h['n'], h['b'], h['closed'])))
    return rows, forced


def run(*a):
    ctl = json.load(io.open(os.path.join(D, CTL), encoding='utf-8')) if os.path.exists(os.path.join(D, CTL)) else {}
    if not ctl.get('ok'):
        sys.exit('### THE CONTROLS ARE NOT BANKED AS WANTED (data/%s) -- NOTHING RUN' % CTL)
    free_or_exit('THE COEFFICIENTS THROUGH %d' % CUT)
    t0 = time.time()
    N = CUT
    spf = C11.spf_table(N)
    P = CG.primes_upto(N)
    R = dict((D_, reading(D_, spec, N, spf, P)) for D_, spec in DISCS.items())
    L = ['%s -- (R330)(3): THE COEFFICIENTS AT -35 AND -40 THROUGH %d BY b711`S ROUTE, EVERY ROW READ HELD OR REFUTED, THE FORCED PARTS APART (%s)' % (ACT, N, utc()), '',
         '### rows are readings of c(n), Q1`s log-derivative coefficients (-Z_Q1`/Z_Q1 = SUM c(n) n^-s), exact for n <= %d, each a vector of rationals' % N,
         '### over the primes of n (c(n) = SUM q_p log p); b_n = r_Q1(n)/2 (b_1 = 1); b(n) = c(n)/log n, the coefficient of log(Z_Q1/2). The registrations',
         '### committed before: data/b720_registrations.txt at f5353ca9 (the rule, H-DECOMP, THE LAW, H-RR) and 54fc03d9 (PRED-35, PRED-40). THE CONTROLS FIRST',
         '### (data/%s, %s).' % (CTL, ctl['at']), '']
    L += control_lines(ctl) + ['']
    for D_ in (-35, -40):
        r = R[D_]
        L += ['## D = %d, Q1 = %s: nonzero c(n) %d of %d (r_Q1(n) nonzero at %d n <= %d) ; signs undecided %d' % (
            D_, form_s(DISCS[D_]['Q1']), r['nonzero'], N - 1, r['rnz'], N, r['undecided'])]
        if not r['n0']:
            L += ['  NO n <= %d WITH c(n) < 0' % N]
        else:
            L += ['  THE LEAST n WITH c(n) < 0: n0 = %d = %s ; c(n0) = %s = %s' % (
                      r['n0'], ' . '.join(('%d^%d' % (p, k)) if k > 1 else '%d' % p for p, k in r['fac']), r['closed'], r['ball']),
                  '  b(n0) = c(n0)/log n0 = %s ; by the Omega derivation %s ; EQUAL %s' % (r['b'], r['b_omega'], r['b'] == r['b_omega']),
                  '  the decomposition: a(n0) %d ; the ordered pair sum %d ; k >= 3 factorizations %d ; a - pair/2 = %s' % (r['a'], r['pair'], r['k3'], r['a_half']),
                  '  the proper divisors with nonzero a: ' + ', '.join('%d (%d)' % dv for dv in r['divs']),
                  '  each prime of n0: ' + ' ; '.join('%d %s, a prime ideal above it in the class of %s (order %s), represented by %s, by Q1: %s' % (
                      p, x['kind'], x['cls'], x['order'], ', '.join(x['forms']) or 'NO FORM', x['by_q1']) for p, x in sorted(r['reps'].items(), key=lambda kv: int(kv[0]))),
                  '  THE COUNT OF NEGATIVE COEFFICIENTS through %d: %d ; the first ten %s' % (N, r['negatives'], r['first'])]
        L += ['  H-RR`s index (NOT BLIND): b(%d) = %s, c = %s' % (r['hrr']['n'], r['hrr']['b'], r['hrr']['closed']), '']
    rows, forced = rows_of(R)
    L += ['### THE ROWS, EACH ON ITS OWN CLAUSES (data/b720_registrations.txt (i)-(iii), H-RR):']
    L += ['  %-28s %-6s %-12s %s' % (n, '' if d is None else d, v, why) for n, d, v, why in rows]
    L += ['', '### THE FORCED PARTS, APART AND COUNTED FOR NOTHING (data/b720_registrations.txt (ii) F1, F2):']
    L += ['  %-28s %-6s %-18s %s' % (n, '' if d is None else d, v, why) for n, d, v, why in forced]
    held = sum(1 for x in rows if x[2] == 'HELD')
    ref = sum(1 for x in rows if x[2] == 'REFUTED')
    word = lambda name: [x for x in rows if x[0] == name][0][2]  # noqa: E731
    law = 'HELD' if all(x[2] == 'HELD' for x in rows if x[0].startswith('THE LAW')) else 'REFUTED'
    L += ['', '### ### **n0(-35) = %s, b = %s ; n0(-40) = %s, b = %s ; ROWS %d: HELD %d, REFUTED %d, NOT SCORABLE %d ; THE LAW %s ; H-DECOMP %s ; '
          'PRED-35 %s, PRED-40 %s ; FORCED %d APART ; %d s.**' % (
              R[-35]['n0'], R[-35].get('b'), R[-40]['n0'], R[-40].get('b'), len(rows), held, ref, len(rows) - held - ref, law,
              word('H-DECOMP (overall)'), word('PRED-35'), word('PRED-40'), len(forced), int(time.time() - t0))]
    print(NL.join(L))
    if 'dry' in a:
        return
    _put('%s_coeffs.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    _put('%s_coeffs.json' % ACT, (json.dumps(dict(at=utc(), cut=N, controls_at=ctl['at'], readings=dict((str(k), v) for k, v in R.items()),
                                                  rows=[dict(row=n, D=d, verdict=v, why=w) for n, d, v, w in rows],
                                                  forced=[dict(row=n, D=d, verdict=v, why=w) for n, d, v, w in forced]),
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
        sys.exit('usage: b720_coeffs.py controls [dry] | run [dry]')
    fn(*sys.argv[2:])
