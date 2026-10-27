# -*- coding: utf-8 -*-
"""b718_derivation.py -- (R328)(4)(iii): THE ARGUMENT, written as data/b718_derivation.txt, the coefficient law of data/b716_registrations.txt
(ii) read through the class group. Each step's check runs at -23, -15 and -39 (data/b711_coeffs.json, data/b713_coeffs.json,
data/b717_coeffs.json) through their cuts and is printed BEFORE the step's text, with a planted error in the check failing as wanted; the
direct b(n) is first checked against each bank's negative list (as tools/b718_decomp.py). The abstract census of minimal negative shapes
(tools/b718_abstract.py) is read for the three groups C2, C3, C4 at Omega 4-6. The grade at the end. Footing WRITTEN PROOF where it closes;
nothing compiled. Writes data/b718_derivation.txt and .json through the membrane. Route: `run`.
"""
import json
import os
import sys
import time
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_, T_ = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T_)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b718_classgroup as CG   # noqa: E402
import b718_abstract as AB     # noqa: E402

CASES = [(-23, 'b711_coeffs'), (-15, 'b713_coeffs'), (-39, 'b717_coeffs')]


class Disc:
    def __init__(self, D, bank):
        self.D, self.bank = D, bank
        with open(os.path.join(D_, bank + '.json'), encoding='utf-8') as fh:
            self.j = json.load(fh)
        self.N = int(self.j['cut'])
        self.P = CG.primes_upto(self.N)
        self.F, self.e, self.T, self.ok = CG.group(D)
        self.h = len(self.F)
        r = CG.r_form(CG.principal(D), self.N)
        self.a = [x // 2 for x in r]
        self.a[1] = 1
        self.b, self.Om = CG.log_coeffs(self.a, self.N, self.P)
        self.pc = dict((p, CG.prime_class(D, p)) for p in self.P)
        self.bad = set(p for p, (t, g) in self.pc.items() if t != 'inert' and g != self.e)
        self.fac = [None, {}] + [CG.factor(n, self.P) for n in range(2, self.N + 1)]

    def kind(self, n):
        ps = set(self.fac[n])
        nb = len(ps & self.bad)
        return 'bad' if nb == len(ps) else ('good' if nb == 0 else 'mixed')


def _cyclic_map(d):
    """the forms' class group onto Z/h by a generator's discrete log (the three groups cyclic: C3, C2, C4)."""
    gen = [x for x in d.F if CG.order(x, d.e, d.T) == d.h][0]
    log, y = {d.e: 0}, d.e
    for k in range(1, d.h):
        y = d.T[(y, gen)]
        log[y] = k
    return log


# ---------------------------------------------------------------- the checks, each (ok, figure) and its planted error
def check0(d, plant=False):
    """the direct b(n) against the bank's negative list through the cut."""
    b = d.b
    if plant:
        a2 = list(d.a)
        a2[d.j['least_negative'] // 2] += 1
        b, _ = CG.log_coeffs(a2, d.N, d.P)
    neg = [n for n in range(2, d.N + 1) if b[n] < 0]
    return neg == list(d.j['negative_list']), 'negatives %d against the bank`s %d, the lists %s' % (
        len(neg), len(d.j['negative_list']), 'EQUAL' if neg == list(d.j['negative_list']) else 'UNEQUAL')


def check1(d, plant=False):
    """a(n) through the class group, every n <= cut: the ideals of norm n counted in the principal class, and the character sum."""
    pc = dict(d.pc)
    if plant:
        p = min(d.bad)
        pc[p] = (pc[p][0], d.e)
    bad_ideal = bad_char = 0
    for n in range(2, d.N + 1):
        dist = CG.ideal_classes(d.D, n, d.P, d.T, d.e, pc)
        x = dist.get(d.e, 0)
        if x != d.a[n]:
            bad_ideal += 1
        if n <= 2000 and dist and CG.a_by_characters(dist, d.F, d.e, d.T) != d.a[n]:
            bad_char += 1
    return bad_ideal == 0 and bad_char == 0, 'mismatches by the ideals %d (n <= %d), by the characters %d (n <= 2000)' % (bad_ideal, d.N, bad_char)


def check2(d, plant=False):
    """b(n) = 0 at every mixed n; at good-supported n, b the log of zeta_K's Euler factors: 2/k (split), 1/k (ramified), 1/j at p^2j
    (inert) at a prime power, 0 at two or more primes."""
    bad = set(d.bad)
    if plant:
        bad.discard(min(bad))
    mixed_nz = good_off = nm = ng = 0
    for n in range(2, d.N + 1):
        ps = set(d.fac[n])
        nb = len(ps & bad)
        if 0 < nb < len(ps):
            nm += 1
            mixed_nz += d.b[n] != 0
        elif nb == 0:
            ng += 1
            if len(ps) > 1:
                want = Fraction(0)
            else:
                (p, k), = d.fac[n].items()
                t = d.pc[p][0]
                want = Fraction(2, k) if t == 'split' else Fraction(1, k) if t == 'ram' else (Fraction(2, k) if k % 2 == 0 else Fraction(0))
            good_off += d.b[n] != want
    return mixed_nz == 0 and good_off == 0, 'mixed n %d, b != 0 at %d ; good-supported n %d, off the Euler-factor value at %d' % (nm, mixed_nz, ng, good_off)


def _single(t, m, N, drop=False):
    if t == 'ram':
        return Fraction(2, N) if N % 2 == 0 else Fraction(0)
    v = (Fraction(2, N) if N % 2 == 0 else 0) + (Fraction(2 * m, N) if N % m == 0 else 0)
    if not drop:
        v -= Fraction(2 * m, N) if N % (2 * m) == 0 else 0
    return Fraction(v)


def check3(d, plant=False):
    """b(p^N) at every bad prime power <= cut against the closed form: split with class order m, [2|N] 2/N + [m|N] 2m/N - [2m|N] 2m/N;
    ramified, [2|N] 2/N. Every value >= 0."""
    n_pp = off = negs = 0
    for p in sorted(d.bad):
        t, g = d.pc[p]
        m = CG.order(g, d.e, d.T)
        q, N = p, 1
        while q <= d.N:
            n_pp += 1
            off += d.b[q] != _single(t, m, N, drop=plant)
            negs += d.b[q] < 0
            q, N = q * p, N + 1
    return off == 0 and negs == 0, 'bad prime powers %d, off the closed form at %d, negative at %d' % (n_pp, off, negs)


def check4(d, plant=False):
    """at every bad-supported n <= cut: no divisor d with a(d) != 0 has Omega(d) < 2; b(n) = a(n) - P(n)/2 where Omega(n) <= 5, b(n) = a(n)
    where Omega(n) <= 3."""
    low = sum(1 for p in d.bad if p <= d.N and d.a[p])
    n4 = off = n3 = off3 = 0
    for n in range(2, d.N + 1):
        if d.kind(n) != 'bad':
            continue
        Om = d.Om[n]
        if Om <= 3:
            n3 += 1
            off3 += d.b[n] != d.a[n]
        elif Om <= 5:
            n4 += 1
            pr = CG.pair_sum(d.a, n)
            off += d.b[n] != d.a[n] - Fraction(pr, 1 if plant else 2)
    return low == 0 and off == 0 and off3 == 0, 'bad primes with a(p) != 0: %d ; Omega <= 3: %d n, b != a at %d ; Omega 4-5: %d n, b != a - P/2 at %d' % (low, n3, off3, n4, off)


def check5(d, plant=False):
    """the abstract model (tools/b718_abstract.py: the group and the classes of n's primes, nothing else) against the direct b(n) at every
    bad-supported n <= cut."""
    log = _cyclic_map(d)
    G = AB.Group((d.h,))
    nb = off = 0
    pmin = min(d.bad)
    for n in range(2, d.N + 1):
        if d.kind(n) != 'bad' or d.b[n] == 0 and d.Om[n] == 1:
            continue
        items = sorted(d.fac[n].items())
        primes = []
        for p, _k in items:
            t, g = d.pc[p]
            x = (log[g] + (1 if (plant and p == pmin and d.h > 2) else 0)) % d.h
            if plant and p == pmin and d.h == 2:
                t = 'ram' if t == 'split' else 'split'
            primes.append((t, (x,)))
        k = tuple(kk for _p, kk in items)
        _a, b = AB.b_lattice(G, primes, k)
        nb += 1
        off += b[k] != d.b[n]
    return off == 0, 'bad-supported n %d, the model off the direct b at %d' % (nb, off)


def check6(d, plant=False):
    """the least negative n: every prime bad (unrepresented by Q1), at least two distinct."""
    n0 = min(n for n in range(2, d.N + 1) if d.b[n] < 0)
    bad = set(d.bad)
    if plant:
        bad.discard(max(d.fac[n0]))
    ps = sorted(d.fac[n0])
    ok = all(p in bad for p in ps) and len(ps) >= 2 and all(d.a[p] == 0 for p in ps)
    return ok, 'n0 = %d, primes %s, each bad %s, each with a(p) = 0 %s, distinct %d' % (
        n0, ps, all(p in bad for p in ps), all(d.a[p] == 0 for p in ps), len(ps))


CHECKS = [('(0) THE DIRECT b AGAINST THE BANKS', check0), ('(1) a(n) THROUGH THE CLASS GROUP', check1),
          ('(2) DECOUPLING; THE GOOD-SUPPORTED VALUES', check2), ('(3) ONE BAD PRIME', check3),
          ('(4) THE k >= 3 TERMS; THE CLOSED FORM AT OMEGA <= 5', check4), ('(5) THE ABSTRACT MODEL', check5),
          ('(6) THE PRIMES OF THE LEAST NEGATIVE INDEX', check6)]

STEPS = {
    0: ['The direct route: a(n) = r_Q1(n)/2 by enumeration and b(n) by the Omega derivation, Omega(n) b(n) = SUM_{d|n} Omega(d) b(d) a(n/d)',
        '(Omega additive, so f -> Omega f is a derivation of Dirichlet convolution and Omega(log f) = (Omega f) * f^-1). The banks` c(n) are',
        'b(n) log n, so the negative lists must agree; they do (above). Every later check reads this b.'],
    1: ['STEP 1 (the object through the class group). K = Q(sqrt D), w = 2, Cl(K) of order h. The ideals of norm n are the products of',
        'prime ideals: for p split, p = P Pbar, the choices P^i Pbar^(k-i), i = 0..k, of class g^(2i-k) where g = [P]; for p ramified, p = P^2,',
        'the one ideal P^k of class [P]^k; for p inert, (p)^(k/2) of the principal class, k even. Each class of norm-p ideals is read from the',
        'reduced form (p, b, (b^2 - D)/4p), b^2 = D mod 4p. A principal ideal of norm n is a pair (x, y) up to the two units, so',
        'a(n) = #{A : N A = n, [A] = 1} = (1/h) SUM_chi SUM_{N A = n} chi(A), by orthogonality of the characters of Cl(K). Hence',
        'Z_Q1/2 = eps(F), F = PRODUCT_p F_p, F_p = SUM_A [class of A] N(A)^-s in Q[Cl(K)][[p^-s]], eps the coefficient of the identity.'],
    2: ['STEP 2 (decoupling). Call p GOOD when every ideal of p-power norm is principal (p inert, or split or ramified with a principal prime',
        'ideal) and BAD otherwise (split or ramified with [P] != 1). For good p, F_p is a scalar multiple of [1]; so F = F_good F_bad with F_good',
        'scalar, eps(F) = F_good eps(F_bad), and log(Z_Q1/2) = log F_good + log eps(F_bad). The first is supported on good-supported n, the',
        'second on bad-supported n; so b(n) = 0 at every n with both a good and a bad prime. log F_good = SUM_{good p} log F_p, each F_p an',
        'Euler factor of zeta_K: b(p^k) = 2/k (split), 1/k (ramified), 1/j at k = 2j (inert), and b = 0 at good n with two or more primes. All',
        'these values are >= 0: A NEGATIVE b(n) OCCURS ONLY AT A BAD-SUPPORTED n.'],
    3: ['STEP 3 (one bad prime). For p split with g = [P] of order m >= 2, eps(F_p) = SUM over (i, j) with m | i - j of x^(i+j) (x = p^-s), which',
        'is (1 - x^(2m)) / ((1 - x^2)(1 - x^m)^2); its log gives b(p^N) = [2|N] 2/N + [m|N] 2m/N - [2m|N] 2m/N >= 0 (where 2m | N the',
        'second term cancels the third and the first stays). For p ramified with [P] of order 2, eps(F_p) = 1/(1 - x^2), b(p^N) = [2|N] 2/N.',
        'So b >= 0 on every bad prime power: A NEGATIVE b(n) NEEDS AT LEAST TWO DISTINCT BAD PRIMES.'],
    4: ['STEP 4 (part (b): the k >= 3 terms). For a bad prime p, a(p) = 0: no prime ideal above p is principal. Every divisor d of a',
        'bad-supported n is bad-supported, so a(d) != 0 forces Omega(d) >= 2. A product a(d_1)...a(d_k) != 0 over an ordered factorization of',
        'n then needs Omega(n) >= 2k. Hence for Omega(n) <= 5 only k = 1, 2 survive: b(n) = a(n) - P(n)/2 with P(n) = SUM_{de = n; d, e >= 2}',
        'a(d) a(e) = (a*a)(n) - 2a(n), that is b(n) = 2a(n) - (a*a)(n)/2; and for Omega(n) <= 3, P(n) = 0 and b(n) = a(n) >= 0. A NEGATIVE',
        'b(n) NEEDS Omega(n) >= 4; AT Omega(n) = 4, 5 ITS VALUE IS 2a(n) - (a*a)(n)/2, BOTH COUNTS OF IDEALS IN THE PRINCIPAL CLASS.'],
    5: ['STEP 5 (the model). By steps 1-4, b(n) at a bad-supported n is a function of Cl(K) and the list (type, class, exponent) of n`s',
        'primes alone -- not of the primes` sizes. tools/b718_abstract.py computes it from that list (above: equal to the direct b at every',
        'bad-supported n through each cut).'],
    6: ['STEP 6 (part (d): the primes of the least negative index). Let n0 be the least n with b(n) < 0. By step 2, n0 is bad-supported:',
        'EVERY prime of n0 is bad, so has a(p) = 0, so is represented by no form of the principal class (r_Q1(p) = 0). By step 3, n0 has at',
        'least two distinct primes; by step 4, Omega(n0) >= 4. Clause 2 of the law follows, in the stronger form "every prime of n0".'],
}

STEP7 = [
    'STEP 7 (part (c): the value at the least negative index). n0 has no proper divisor with b < 0 (each is smaller), so its shape is a',
    'MINIMAL negative shape of Cl(K): a list (type, class, exponent) with b < 0 and b >= 0 at every proper sub-list. The census of',
    'tools/b718_abstract.py over C2, C3, C4 (above) lists every minimal negative shape at Omega 4, 5 and 6 with its value, the shapes',
    'abstract (a shape with more ramified primes than a discriminant of that group has is listed too). At the three banks:',
    '-15 (C2): n0 = 24 = 2^3 . 3, the shape (split g)^3 (ramified g)^1: all four ideals P^i Pbar^(3-i) Q have class (2i - 2)g = 1, so a = 4;',
    'the divisors with a != 0 are p^2 (a = 3) and pq (a = 2: P Q, Pbar Q, class 2g = 1), so P = 2 . 3 . 2 = 12 and b = 4 - 6 = -2.',
    '-23 (C3): n0 = 48 = 2^4 . 3, the shape (split g)^4 (split g)^1: a = 4 and P = 12 by the same count over C3 (data/b718_decomp.txt).',
    '-39 (C4): n0 = 120 = 2^3 . 3 . 5, (split c)^3 (ramified c^2) (split c): a = 4, P = 12 (data/b718_decomp.txt).',
    'WHAT REPLACES a = 4, P = 12 IN GENERAL: at Omega(n0) = 4, 5 the value 2a(n0) - (a*a)(n0)/2 of the minimal shape n0 instantiates; the',
    'census shows those values are not all -2 in any of the three groups.',
]


def census_lines():
    L = []
    rows_all = {}
    for orders in ((2,), (3,), (4,)):
        rows = AB.listing(orders, oms=(4, 5, 6))
        rows_all[str(orders)] = [(Om, s, a, p, str(b)) for Om, s, a, p, b in rows]
        vals = {}
        for Om, _s, _a, _p, b in rows:
            vals.setdefault(Om, {})
            vals[Om][str(b)] = vals[Om].get(str(b), 0) + 1
        m2 = [(Om, s) for Om, s, a, p, b in rows if b == -2]
        L += ['  C%d: minimal negative shapes %d ; values by Omega %s' % (orders[0], len(rows), dict((k, vals[k]) for k in sorted(vals))),
              '      the shapes of value -2: %s' % '; '.join('Omega %d %s' % x for x in m2)]
    return L, rows_all


def main():
    t0 = time.time()
    ds = [Disc(D, bank) for D, bank in CASES]
    L = ['b718 -- (R328)(4)(iii): THE COEFFICIENT LAW READ THROUGH THE CLASS GROUP, THE ARGUMENT WITH ITS CHECKS (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### THE OBJECT ((R328)(4)(i)): D < 0 fundamental, h >= 2, two units; a(n) = r_Q1(n)/2; log(Z_Q1/2) = SUM_{n>=2} b(n) n^-s. The law of',
         '### data/b716_registrations.txt (ii): the least n with b(n) < 0 has (1) b(n) = -2 and (2) a prime the principal form does not represent.',
         '### Each step: its CHECK at -23, -15, -39 through the banks` cuts, then its PLANT (an error put into the check), printed BEFORE the step.',
         '### The class groups by the forms` composition, each axiom checked: %s.' % ' ; '.join('%d: h %d, %s' % (d.D, d.h, 'ALL TRUE' if all(d.ok.values()) else d.ok) for d in ds), '']
    J = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), checks=[])
    good = True
    for i, (title, fn) in enumerate(CHECKS):
        L += ['## %s' % title]
        for d in ds:
            ok, fig = fn(d)
            pok, pfig = fn(d, plant=True)
            good &= ok and not pok
            L += ['  CHECK %d (data/%s.json, cut %d): %s -- %s' % (d.D, d.bank, d.N, fig, 'AS WANTED' if ok else '### NOT AS WANTED'),
                  '  PLANT %d: %s -- %s' % (d.D, pfig, 'FAILS AS WANTED' if not pok else '### PASSES, NOT AS WANTED')]
            J['checks'].append(dict(step=i, D=d.D, ok=ok, figure=fig, plant_fails=not pok, plant=pfig))
        L += [''] + ['  ' + x for x in STEPS[i]] + ['']
        print('  %s done %.0f s' % (title, time.time() - t0), flush=True)
    cl, rows = census_lines()
    L += ['## (7) THE MINIMAL NEGATIVE SHAPES (the census, tools/b718_abstract.py, C2, C3, C4 at Omega 4-6)'] + cl + [''] + ['  ' + x for x in STEP7] + ['']
    J['census'] = rows
    L += ['## THE GRADE',
          '  THEOREM (footing WRITTEN PROOF; nothing compiled). Let D < 0 be a fundamental discriminant with h(D) >= 2 and w = 2, Q1 its',
          '  principal form, a(n) = r_Q1(n)/2 and log(Z_Q1/2) = SUM b(n) n^-s. Then (i) b(n) = 0 at every n carrying both a good and a bad prime,',
          '  and b(n) >= 0 at every good-supported n and at every power of one bad prime; (ii) at a bad-supported n, a(d) = 0 for every divisor',
          '  d with Omega(d) <= 1, so the k-fold terms vanish for 2k > Omega(n), and b(n) = 2a(n) - (a*a)(n)/2 when Omega(n) <= 5; (iii) if some',
          '  b(n) < 0, the least such n0 is bad-supported with at least two distinct primes and Omega(n0) >= 4, so every prime dividing n0 is',
          '  represented by no form of the principal class -- CLAUSE 2 OF THE LAW, DERIVED, in the stronger form; (iv) b(n0) is the value of a',
          '  minimal negative shape of Cl(K), and at Omega(n0) <= 5 equals 2a(n0) - (a*a)(n0)/2.',
          '  CLAUSE 1 (b(n0) = -2) IS NOT DERIVED. THE STEP THAT REMAINS, NAMED EXACTLY: that the least n, over the bad primes of D with their',
          '  classes, instantiating a minimal negative shape of Cl(K) instantiates one of value -2. The value is not a function of the group:',
          '  minimal negative shapes of value other than -2 exist in C2 at Omega 4, in C3 at Omega 4 and 5, and in C4 at Omega 4, 5 and 6 (the',
          '  census above, read at Omega 4-6 only); which shape is least is set by the sizes of the least bad primes in each class, which the',
          '  class group does not fix. Nor does the argument bound Omega(n0): C4 has minimal negative shapes at Omega 6 (census), where the',
          '  k = 3 terms enter; the census does not read Omega 7 or more. The law`s clause 1 stands REGISTERED,',
          '  HELD at -23, -15, -39, and carried with its falsifier; clause 2 stands as a written proof.', '']
    L += ['### ### **CHECKS 7 STEPS x 3 DISCRIMINANTS: %s ; PLANTS: %s ; THE GRADE: CLAUSE 2 A THEOREM (WRITTEN PROOF) ; CLAUSE 1 NOT DERIVED, ITS STEP NAMED ; %.0f s.**' % (
        'ALL AS WANTED' if good else 'NOT ALL AS WANTED', 'ALL FAIL AS WANTED' if good else 'SEE ABOVE', time.time() - t0)]
    J.update(all_as_wanted=good, seconds=round(time.time() - t0, 1), grade='clause 2 theorem (written proof); clause 1 not derived')
    import act_membrane as MEM
    import b718_record as REC
    for name, data in (('b718_derivation.txt', NL.join(L) + NL), ('b718_derivation.json', json.dumps(J, indent=1) + NL)):
        p = os.path.join(D_, name)
        MEM.guard_path('b718', p, REC.R.ROOT_EXCLUDE)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(data.encode('utf-8'))
        os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    if sys.argv[1:] != ['run']:
        sys.exit('usage: b718_derivation.py run')
    main()
