#!/usr/bin/env python3
"""b768, (R378)(4)(d), L11d (window_arith_neg): the data and the generated chunks of the inequality, from the kernel's own files.

The real part of the arithmetic side at the window, by arith_eq_comb (L11c, ArithComb.lean), is a constant in k(0), log 23, log 2,
log pi and Euler's constant, a coefficient of each log m (m < 16390) with the constant archC0, and the prime-power side's terms at
2 <= n < 1024. ArithFrame.lean (written by hand) reads each part's bound:
  * the m side, as the integer walk arWalk over the five lists (the band's and the far sum's coefficients, coeffPad, the two
    constants' terms), each place m >= 2 taking log m at the end of its interval of L10 (logNat_bounds) that its coefficient's sign
    gives (arSelU), over dc * 2^100 with dc = 48 * 10^(2 coeffScale) * bandDEN * farDEN;
  * the prime side, at each n the lower end of 2 cQ(n) K(n) / (80640 n^4 10^34) through cQ_eq_comb, each log p at the end its
    coefficient's sign gives (arSelL), floored to an integer over 80640 * 10^34 * 2^100 (the table arTqTab, each place checked
    against its bound by the kernel);
  * the constants, each at the end of its interval of L10 that its coefficient's sign gives (k(0) > 0).
This tool computes the three exactly as the kernel will (integers and fractions), prints the inequality's sign and its slack, and
writes ArithData.lean, ArithA0-4.lean, ArithB.lean and ArithJoin.lean. It prints no window coefficient, no K(n), no r, no k(0)'s
or the integral's numerator, no chunk's value and no entry of the table: counts, truth values, digests, the sign, the slack and the
widths alone.

  control   the planted checks
  dry       the data, the checks, the budget and the texts; nothing written
  write     the same, then the files written in the kernel's working tree and read back, print_targets.txt given the names
"""
import hashlib
import math
import os
import re
import sys
from fractions import Fraction

T = os.path.dirname(os.path.abspath(__file__))
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
import b768_packed_data as PD     # noqa: E402  (read_coeffs, text_checks, the kernel's folder, git)
import b768_far_data as FD        # noqa: E402  (build: farNumL and farGL)
import b768_band_data as BD       # noqa: E402  (build: bandNumL and bandGL)

NL = '\n'
KPATH = PD.KPATH
DIR = 'SIDEExplicitFormula/Window/'
N_M = 16390          # ### m < 16390: arith_eq_comb's sum
CH_A = 128           # ### places of the walk a declaration: the far sum's chunks compiled at 128 (data/b768_defects.txt (l))
PER_FILE = 26        # ### chunks a file: 129 chunks in five files
CHAINS = 2           # ### ArithA files free to build at once: dispatch 11 (run 45510384327) stopped under the hold with four building
                     # ### together, so ArithA<i> imports ArithA<i-2> (A0 -> A2 -> A4, A1 -> A3)
N_LO, N_HI = 2, 1023 # ### the prime side's n
CH_B = 128           # ### the prime side's chunks: cq_ok's (CQValues.lean :198-:212)
D = 2 ** 100         # ### lpD (LogBounds.lean :29)
BW = [1, -4, 6, -4, 1]
ANCHOR = 'SIDEExplicitFormula.Window.arith_eq_comb'
FRAME = DIR + 'ArithFrame.lean'
NEG = DIR + 'ArithNeg.lean'
FRAME_USED = ['ar_walk_chunk', 'ar_sum_chunk']          # ### the frame's theorems the generated joins name
NEG_THMS = ['window_arith_neg', 'controlFailureExists']   # ### (R378)(4)(d) and (e)
THM = re.compile(r'^theorem ([A-Za-z_][A-Za-z_0-9]*)', re.M)


def rd(rel):
    return open(os.path.join(KPATH, rel), 'rb').read().decode('utf-8').replace('\r\n', '\n')


def one(pat, text, what):
    m = re.findall(pat, text, re.S)
    if len(m) != 1:
        sys.exit('### %s: %d matches, wanted 1' % (what, len(m)))
    return m[0]


def blob_equal(rel):
    """the working tree's bytes equal to HEAD's blob (digests compared, nothing printed of the file)."""
    p = os.path.join(KPATH, rel)
    return PD.git('hash-object', p) == PD.git('rev-parse', 'HEAD:%s' % rel)


def sieve(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def factor(m, primes):
    out = []
    for p in primes:
        if p * p > m:
            break
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            out.append((p, e))
    if m > 1:
        out.append((m, 1))
    return out


def sel_u(c, lo, hi):
    return c * hi if c >= 0 else c * lo


def sel_l(c, lo, hi):
    return c * lo if c >= 0 else c * hi


def read_sources():
    src = {}
    rep = {}
    for rel in ('ArchData.lean', 'PoleData.lean', 'Coeffs.lean', 'BandPoly.lean', 'FarPoly.lean', 'LogData.lean', 'KData.lean',
                'CQData.lean', 'LogConst.lean'):
        src[rel] = rd(DIR + rel)
        rep[rel] = blob_equal(DIR + rel)
    d = {}
    d['k0'] = int(one(r'def k0Num : ℤ :=\s*(-?\d+)', src['ArchData.lean'], 'k0Num'))
    d['intH'] = int(one(r'def intHNum : ℤ :=\s*(-?\d+)', src['PoleData.lean'], 'intHNum'))
    d['cs'] = int(one(r'def coeffScale : ℕ :=\s*(\d+)', src['Coeffs.lean'], 'coeffScale'))
    d['bden'] = int(one(r'def bandDEN : ℕ :=\s*(\d+)', src['BandPoly.lean'], 'bandDEN'))
    d['fden'] = int(one(r'def farDEN : ℕ :=\s*(\d+)', src['FarPoly.lean'], 'farDEN'))
    ents = re.findall(r'⟨(\d+), (\d+), (\d+), (\d+), \[', src['LogData.lean'])
    d['lp'] = {int(p): (int(lo), int(hi)) for p, lo, hi, _k in ents}
    d['lp_n'] = len(ents)
    kts = re.findall(r'\((\d+), (-?\d+)\)', src['KData.lean'])
    d['kt'] = {int(n): int(v) for n, v in kts}
    d['kt_n'] = len(kts)
    pl = one(r'def primeList : List ℕ :=\s*\[(.*?)\]', src['CQData.lean'], 'primeList')
    d['primeList'] = [int(x) for x in re.findall(r'\d+', pl)]
    d['pLo'] = Fraction(*map(int, one(r'def pLo : ℚ := (\d+) / (\d+)', src['LogConst.lean'], 'pLo')))
    d['gLo'] = Fraction(*map(int, one(r'def gLo : ℚ := (\d+) / (\d+)', src['LogConst.lean'], 'gLo')))
    return d, rep


def cq_reps(k):
    """r_Q(k): the pairs (a, b) of integers with a^2 + a b + 6 b^2 = k (4 Q = (2a + b)^2 + 23 b^2)."""
    c = 0
    bmax = int(math.isqrt(4 * k // 23)) + 1
    for b in range(-bmax, bmax + 1):
        rest = 4 * k - 23 * b * b
        if rest < 0:
            continue
        s = math.isqrt(rest)
        for t in {s, -s}:
            if t * t == rest and (t - b) % 2 == 0:
                c += 1
    return c


def ev(p, n):
    e = 0
    while n > 0 and n % p == 0:
        n //= p
        e += 1
    return e


def cq_z(primes):
    """z(n, p) for 2 <= n <= 1023 and p | n, by the recursion cq_holds reads (CQValues.lean :231): 2 z(n, p) = r(n) e_p(n) -
    sum over proper divisors d of z(d, p) r(n / d); z(1, p) = 0 and z(n, p) = 0 where p does not divide n."""
    r = [0] + [cq_reps(k) for k in range(1, N_HI + 1)]
    z = {}
    odd = 0
    for n in range(2, N_HI + 1):
        divs = [d for d in range(1, n) if n % d == 0]
        for p in primes:
            if n % p:
                continue
            s = r[n] * ev(p, n) - sum(z.get((d, p), 0) * r[n // d] for d in divs)
            if s % 2:
                odd += 1
            z[(n, p)] = s // 2
    return z, r, odd


def compute(verbose=True):
    d, rep = read_sources()
    lists, crep = PD.read_coeffs()
    flat = [x for l in lists for x in l]
    b = BD.build(verbose=False)
    f = FD.build(verbose=False)
    bnum, bgam, fnum, fgam = b['num'], b['gam'], f['num'], f['gam']
    out = dict(d=d)
    chk = {}
    chk['sources equal at HEAD'] = all(rep.values()) and crep['equal']
    chk['numerators 16365'] = len(flat) == 16365
    chk['band and far lengths 16385 16384 16370 16369'] = (len(bnum), len(bgam), len(fnum), len(fgam)) == (16385, 16384, 16370, 16369)
    chk['band and far denominators as the kernel holds'] = b['den'] == d['bden'] and f['den'] == d['fden']
    chk['lpTree entries 1900, keys distinct'] = d['lp_n'] == 1900 and len(d['lp']) == 1900
    chk['ktTable entries 197, keys distinct'] = d['kt_n'] == 197 and len(d['kt']) == 197
    primes_all = sieve(N_M)
    chk['every prime to 16389 a key of lpTree'] = all(p in d['lp'] for p in primes_all)
    plist = d['primeList']
    chk['primeList the 172 primes below 1024'] = sorted(plist) == sieve(1023) and len(plist) == 172
    chk['k(0) positive'] = d['k0'] > 0
    pad = [0] * 20 + flat

    def padg(i):
        return pad[i] if 0 <= i < len(pad) else 0

    def coeff_int(j):
        return flat[j - 16] if 16 <= j <= 16380 else 0

    def pnum(m):
        return m ** 3 * (BW[0] * padg(m + 4) + BW[1] * padg(m + 3) + BW[2] * padg(m + 2) + BW[3] * padg(m + 1) + BW[4] * padg(m))

    def polenum(m):
        return m ** 3 * sum(BW[k] * coeff_int(m - k if m >= k else 0) for k in range(5))

    def g(l, i):
        return l[i] if i < len(l) else 0

    bd, fd = d['bden'], d['fden']
    cA = d['intH'] * bd * fd

    def c_i(m, bn=bnum):
        return cA * pnum(m) + 6 * fd * g(bn, m) - bd * g(fnum, m)

    def g_i(m):
        return 6 * fd * g(bgam, m) - bd * g(fgam, m)

    lpd = d['lp']
    facs = {m: factor(m, primes_all) for m in range(2, N_M)}

    def f_lo(m):
        return sum(e * lpd[p][0] for p, e in facs[m])

    def f_hi(m):
        return sum(e * lpd[p][1] for p, e in facs[m])

    def a_p(m, bn=bnum):
        return (0 if m <= 1 else sel_u(c_i(m, bn), f_lo(m), f_hi(m))) + g_i(m) * D

    chk['pNum at the window equals poleNum at every m'] = all(pnum(m) == polenum(m) for m in range(N_M))
    S = []
    starts = list(range(0, N_M, CH_A))
    for a in starts:
        k = min(CH_A, N_M - a)
        S.append(sum(a_p(m) for m in range(a, a + k)))
    SA = sum(S)
    P = [0] * len(S)
    acc = 0
    for j in range(len(S) - 1, -1, -1):
        acc += S[j]
        P[j] = acc
    out.update(S=S, P=P, SA=SA, starts=starts)
    # the prime side
    z, r, odd = cq_z(plist)
    chk['the recursion even at every n and p'] = odd == 0
    chk['r(1) = 2'] = r[1] == 2
    kt = d['kt']
    cov = all(all(z.get((n, p), 0) == 0 for p in plist) or n in kt for n in range(N_LO, N_HI + 1))
    chk['each n with a nonzero coefficient in ktTable (arKtCov)'] = cov

    def g_b(n, p):
        zz = z.get((n, p), 0)
        if zz == 0:
            return 0
        return sel_l(2 * zz * kt.get(n, 0), lpd[p][0], lpd[p][1])

    bB = {n: sum(g_b(n, p) for p in plist) for n in range(N_LO, N_HI + 1)}
    Tq = [bB[n] // n ** 4 for n in range(N_LO, N_HI + 1)]
    chk['each table entry a floor of its bound'] = all(Tq[n - 2] * n ** 4 <= bB[n] < (Tq[n - 2] + 1) * n ** 4
                                                       for n in range(N_LO, N_HI + 1))
    TB = []
    bstarts = list(range(N_LO, N_HI + 1, CH_B))
    for a in bstarts:
        k = min(CH_B, N_HI + 1 - a)
        TB.append(sum(Tq[n - 2] for n in range(a, a + k)))
    SB = sum(TB)
    QB = [0] * len(TB)
    acc = 0
    for j in range(len(TB) - 1, -1, -1):
        acc += TB[j]
        QB[j] = acc
    out.update(Tq=Tq, TB=TB, QB=QB, SB=SB, bstarts=bstarts, H23=lpd[23][1], L2=lpd[2][0])
    # the constants and the inequality
    kap = Fraction(d['k0'], 80640 * 10 ** 34)
    E = kap * (Fraction(11, 3) + Fraction(lpd[23][1], D) - 2 * Fraction(lpd[2][0], D) - 2 * d['pLo'] - 2 * d['gLo'])
    dc = 48 * 10 ** (2 * d['cs']) * bd * fd
    FB = 80640 * 10 ** 34 * D
    U = E + Fraction(SA, dc * D) - Fraction(SB, FB)
    out.update(U=U)
    # the widths, floats (read, not entered)
    wA = sum(abs(c_i(m)) * (f_hi(m) - f_lo(m)) for m in range(2, N_M)) / (dc * D)
    wB = 0.0
    for n in range(N_LO, N_HI + 1):
        for p in plist:
            zz = z.get((n, p), 0)
            if zz:
                wB += abs(2 * zz * kt.get(n, 0)) * (lpd[p][1] - lpd[p][0]) / D / (80640 * n ** 4 * 10 ** 34)
    kf = float(kap)
    gam = 0.5772156649015329
    wC = dict(log23=kf * (lpd[23][1] / D - math.log(23)), log2=2 * kf * (math.log(2) - lpd[2][0] / D),
              logpi=2 * kf * (math.log(math.pi) - float(d['pLo'])), gamma=2 * kf * (gam - float(d['gLo'])))
    floor_loss = (N_HI - N_LO + 1) / FB
    out.update(widths=dict(m_side=wA, prime_side=wB, floor=floor_loss, **wC))
    # a planted change: one band coefficient moved by 1 at m = 1000 moves that chunk's sum
    bn2 = list(bnum)
    bn2[1000] += 1
    chk['a planted coefficient moved by 1 moves its chunk (control)'] = sum(a_p(m, bn2) for m in range(768, 1024)) != S[3]
    out['checks'] = chk
    if verbose:
        for k_, v in chk.items():
            print('  CHECK %-62s %s' % (k_, v))
    return out


def par(x):
    return str(x) if x >= 0 else '(%d)' % x


HEAD_DOC = 'Written by relay tools/b768_arith_data.py from the kernel`s own files; edited by no hand.'


def texts(o):
    tx = {}
    # the table
    rows = []
    Tq = o['Tq']
    for i in range(0, len(Tq), 4):
        rows.append('  ' + ', '.join(str(x) for x in Tq[i:i + 4]))
    tx[DIR + 'ArithData.lean'] = NL.join([
        'import Mathlib.Data.Int.Notation', '',
        '/-!', '# L11d`s table: the prime-power side`s lower ends at the window, floored', '', HEAD_DOC, '-/', '',
        'namespace SIDEExplicitFormula', 'namespace Window', '',
        '/-- At `n = 2 + i`, `i < 1022`: an integer at most the lower end `arBB n / n ^ 4` (ArithFrame.lean), checked there. -/',
        'def arTqTab : List ℤ := [', (',' + NL).join(rows), ']', '',
        'end Window', 'end SIDEExplicitFormula', ''])
    # the walk's chunks
    S, starts = o['S'], o['starts']
    nfile = (len(S) + PER_FILE - 1) // PER_FILE
    for fi in range(nfile):
        body = []
        for j in range(fi * PER_FILE, min(len(S), (fi + 1) * PER_FILE)):
            a = starts[j]
            k = min(CH_A, N_M - a)
            body += ['set_option maxHeartbeats 0 in',
                     '/-- The walk over `m` from %d, %d places. -/' % (a, k),
                     'theorem arithA_c%02d : arWalk %d %d (arX0.dr %d) = %d := by decide +kernel' % (j, k, a, a, S[j]), '']
        tx[DIR + 'ArithA%d.lean' % fi] = NL.join([
            'import SIDEExplicitFormula.Window.' + ('ArithFrame' if fi < CHAINS else 'ArithA%d' % (fi - CHAINS)), '',
            '/-!', '# L11d: the walk over `m`, chunks %d to %d' % (fi * PER_FILE, min(len(S), (fi + 1) * PER_FILE) - 1), '',
            HEAD_DOC, '-/', '', 'namespace SIDEExplicitFormula', 'namespace Window', ''] + body +
            ['end Window', 'end SIDEExplicitFormula', ''])
    # the prime side's checks and sums
    TB, bstarts = o['TB'], o['bstarts']
    body = ['set_option maxHeartbeats 0 in',
            '/-- Each `n` whose coefficients are not all `0` has its entry in ktTable. -/',
            'theorem ar_kt_cov : allDC arKtCov 2 1022 10 = true := by decide +kernel', '',
            'set_option maxHeartbeats 0 in',
            '/-- Each prime below 1024 a key of the table of L10a. -/',
            'theorem ar_p_find : ∀ p ∈ primeList, (lpTree.find p).isSome = true := by decide +kernel', '',
            '/-- The upper end`s numerator at 23. -/',
            'theorem ar_e23 : arHi 23 = %d := by decide +kernel' % o['H23'], '',
            '/-- The lower end`s numerator at 2. -/',
            'theorem ar_e2 : arLo 2 = %d := by decide +kernel' % o['L2'], '']
    for j, a in enumerate(bstarts):
        k = min(CH_B, N_HI + 1 - a)
        body += ['set_option maxHeartbeats 0 in', '/-- The table`s entries checked from %d, %d places. -/' % (a, k),
                 'theorem ar_tq_ok_%d : allDC arTqOK %d %d 7 = true := by decide +kernel' % (j, a, k), '']
    for j, a in enumerate(bstarts):
        k = min(CH_B, N_HI + 1 - a)
        body += ['/-- The table`s entries summed from %d, %d places. -/' % (a, k),
                 'theorem ar_tq_sum_%d : arSum arTq %d %d = %d := by decide +kernel' % (j, a, k, TB[j]), '']
    tx[DIR + 'ArithB.lean'] = NL.join([
        'import SIDEExplicitFormula.Window.ArithFrame', '',
        '/-!', '# L11d: the prime-power side`s checks and sums, the two constants` numerators', '', HEAD_DOC, '-/', '',
        'namespace SIDEExplicitFormula', 'namespace Window', ''] + body + ['end Window', 'end SIDEExplicitFormula', ''])
    # the join
    P, QB = o['P'], o['QB']
    j_lines = ['set_option maxHeartbeats 0 in',
               '/-- The walk over `m < 16390`, its chunks joined. -/',
               'theorem arithA_all : arWalk 16390 0 (arX0.dr 0) = %d := by' % P[0]]
    for j in range(len(S) - 1):
        a = starts[j]
        rest = N_M - a - CH_A
        j_lines.append('  refine ar_walk_chunk arX0 %d %d %d %d %s %s %s (by norm_num) arithA_c%02d ?_ (by norm_num)'
                       % (CH_A, rest, a, a + CH_A, par(S[j]), par(P[j + 1]), par(P[j]), j))
    j_lines += ['  exact arithA_c%02d' % (len(S) - 1), '']
    j_lines += ['set_option maxHeartbeats 0 in',
                '/-- The table summed over `2 ≤ n ≤ 1023`, its chunks joined. -/',
                'theorem arithB_all : arSum arTq 2 1022 = %d := by' % QB[0]]
    for j in range(len(TB) - 1):
        a = bstarts[j]
        rest = (N_HI + 1) - a - CH_B
        j_lines.append('  refine ar_sum_chunk arTq %d %d %d %d %s %s %s (by norm_num) ar_tq_sum_%d ?_ (by norm_num)'
                       % (CH_B, rest, a, a + CH_B, par(TB[j]), par(QB[j + 1]), par(QB[j]), j))
    j_lines += ['  exact ar_tq_sum_%d' % (len(TB) - 1), '']
    j_lines += ['set_option maxHeartbeats 0 in',
                '/-- Each entry of the table at most its bound, `2 ≤ n ≤ 1023`. -/',
                'theorem ar_tq_all : ∀ n, 2 ≤ n → n ≤ 1023 → arTqOK n = true := by', '  intro n h2 hn']
    for j, a in enumerate(bstarts):
        hi_ = a + CH_B
        if j == 0:
            j_lines += ['  by_cases c0 : n < %d' % hi_, '  · exact allDC_at (by norm_num) ar_tq_ok_0 h2 (by omega)']
        elif j < len(bstarts) - 1:
            j_lines += ['  by_cases c%d : n < %d' % (j, hi_),
                        '  · exact allDC_at (by norm_num) ar_tq_ok_%d (by omega) (by omega)' % j]
        else:
            j_lines += ['  · exact allDC_at (by norm_num) ar_tq_ok_%d (by omega) (by omega)' % j]
    j_lines += ['',
                '/-- Each `n`, `2 ≤ n ≤ 1023`, covered by ktTable where its coefficients are not all `0`. -/',
                'theorem ar_cov_all : ∀ n, 2 ≤ n → n ≤ 1023 → arKtCov n = true :=',
                '  fun n h2 hn => allDC_at (by norm_num) ar_kt_cov h2 (by omega)', '',
                'set_option maxHeartbeats 0 in',
                '/-- The three bounds` sum, evaluated: below `0`. -/',
                'theorem arith_num : arithE + arithA - arithB < 0 := by',
                '  unfold arithE arithA arithB',
                '  rw [arithA_all, arithB_all, ar_e23, ar_e2]',
                '  unfold kap0 arDc',
                '  norm_num [k0Num, coeffScale, bandDEN, farDEN, lpD, pLo, gLo]', '']
    tx[DIR + 'ArithJoin.lean'] = NL.join(
        ['import SIDEExplicitFormula.Window.ArithA%d' % i for i in range(nfile)] +
        ['import SIDEExplicitFormula.Window.ArithB', '',
         '/-!', '# L11d: the chunks joined and the three bounds` sum evaluated', '', HEAD_DOC, '-/', '',
         'namespace SIDEExplicitFormula', 'namespace Window', ''] + j_lines + ['end Window', 'end SIDEExplicitFormula', ''])
    names = (['arithA_c%02d' % j for j in range(len(S))] +
             ['ar_kt_cov', 'ar_p_find', 'ar_e23', 'ar_e2'] + ['ar_tq_ok_%d' % j for j in range(len(TB))] +
             ['ar_tq_sum_%d' % j for j in range(len(TB))] + ['arithA_all', 'arithB_all', 'ar_tq_all', 'ar_cov_all', 'arith_num'])
    return tx, names


DOC_OPT = re.compile(r'-/\s*\nset_option')


def checks_of(t):
    c = PD.text_checks(t)
    c['doc_before_option'] = len(DOC_OPT.findall(t))
    return c


def control():
    ok = []
    # selection: the end the sign gives
    a = sel_u(3, 1, 2) == 6 and sel_u(-3, 1, 2) == -3 and sel_l(3, 1, 2) == 3 and sel_l(-3, 1, 2) == -6
    ok.append(('(1) arSelU and arSelL take the end the sign gives', a))
    x = Fraction(3, 2)
    b = all(Fraction(sel_l(c, 1, 2), 1) <= c * x <= Fraction(sel_u(c, 1, 2), 1) for c in range(-5, 6))
    ok.append(('(2) c x between arSelL and arSelU for x in [1, 2], c from -5 to 5', b))
    ok.append(('(3) factor(360) and factor(16381)', factor(360, sieve(100)) == [(2, 3), (3, 2), (5, 1)] and
               factor(16381, sieve(200)) == [(16381, 1)]))
    ok.append(('(4) r_Q(1) = 2, r_Q(2) = 0, r_Q(6) = 4, r_Q(8) = 4 (6 = Q(0, 1) = Q(-1, 1), 8 = Q(1, 1) = Q(-2, 1), each with -(a, b))',
               [cq_reps(k) for k in (1, 2, 6, 8)] == [2, 0, 4, 4]))
    t1 = 'import X\ntheorem t : x = 1.5 := rfl\n'
    t2 = 'import X\n/-- d -/\nset_option maxHeartbeats 0 in\ntheorem t : True := trivial\n'
    ok.append(('(5) a planted decimal literal read 1, a doc comment above an option read 1',
               checks_of(t1)['decimal'] == 1 and checks_of(t2)['doc_before_option'] == 1))
    for k_, v in ok:
        print('  CONTROL %-80s %s' % (k_, 'AS WANTED' if v else 'NOT AS WANTED'))
    good = all(v for _, v in ok)
    print('  CONTROLS: %d of %d AS WANTED' % (sum(1 for _, v in ok if v), len(ok)))
    return good


def report(o, tx):
    U = o['U']
    print('  THE INEQUALITY: arithE + arithA - arithB < 0: %s ; its slack -U %.3f' % (U < 0, float(-U)))
    w = o['widths']
    print('  THE WIDTHS (floats, read and not entered): the m side %.3f ; the prime side %.3f ; log 23 %.3f ; log 2 %.3f ; '
          'log pi %.3f ; gamma %.3f ; the floors %.1e' % (w['m_side'], w['prime_side'], w['log23'], w['log2'], w['logpi'],
                                                      w['gamma'], w['floor']))
    tot = w['m_side'] + w['prime_side'] + w['log23'] + w['log2'] + w['logpi'] + w['gamma']
    print('  the widths summed %.3f ; the slack less them, the side`s value read from the bounds %.3f' % (tot, float(U) - tot))
    allc = True
    for p, t in sorted(tx.items()):
        c = checks_of(t)
        good = c['decimal'] == 0 and c['barred'] == 0 and c['import_first'] and c['doc_before_option'] == 0
        allc = allc and good
        print('  TEXT %-40s lines %5d bytes %8d longest list %5d decimal %d barred %d imports first %s doc above option %d '
              'sha256 %s' % (p.split('/')[-1], c['lines'], c['bytes'], c['longest_list'], c['decimal'], c['barred'],
                             c['import_first'], c['doc_before_option'], c['sha256']))
    return allc


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    if mode not in ('control', 'dry', 'write'):
        sys.exit(__doc__)
    if mode == 'control':
        sys.exit(0 if control() else 1)
    if not control():
        sys.exit('### a control NOT AS WANTED: nothing computed')
    o = compute()
    tx, names = texts(o)
    allc = report(o, tx)
    afiles = sorted(p for p in tx if re.fullmatch(re.escape(DIR) + r'ArithA\d+\.lean', p))
    chain = [(p.split('/')[-1], tx[p].split(NL)[0].split('.')[-1]) for p in afiles]
    want = [('ArithA%d.lean' % i, 'ArithFrame' if i < CHAINS else 'ArithA%d' % (i - CHAINS)) for i in range(len(afiles))]
    free = sum(1 for _p, imp in chain if imp == 'ArithFrame')
    chain_ok = chain == want and free == CHAINS
    print('  THE CHAINS: %s ; free to build at once %d against %d ; %s' % (
        ' '.join('%s<-%s' % (p.replace('.lean', ''), imp) for p, imp in chain), free, CHAINS, 'AS WANTED' if chain_ok else 'NOT AS WANTED'))
    good = all(o['checks'].values()) and allc and o['U'] < 0 and chain_ok
    frame_ok = os.path.exists(os.path.join(KPATH, FRAME)) and os.path.exists(os.path.join(KPATH, NEG))
    fnames, nnames = [], []
    if frame_ok:
        fnames, nnames = THM.findall(rd(FRAME)), THM.findall(rd(NEG))
        missing = [n for n in FRAME_USED if n not in fnames] + [n for n in NEG_THMS if n not in nnames]
        clash = sorted(set(fnames) & set(names) | set(nnames) & set(names) | set(fnames) & set(nnames))
        print('  THE HAND FILES: ArithFrame.lean %d theorems, ArithNeg.lean %d ; the named ones missing %d %s ; shared with the '
              'generated names %d' % (len(fnames), len(nnames), len(missing), missing[:4], len(clash)))
        frame_ok = not missing and not clash
    else:
        print('  THE HAND FILES: ArithFrame.lean or ArithNeg.lean absent')
    pt = rd('print_targets.txt')
    lines = pt.split(NL)
    full = ['SIDEExplicitFormula.Window.' + n for n in fnames + names + nnames]
    already = [n for n in full if n in lines]
    at = lines.index(ANCHOR) + 1 if ANCHOR in lines else 0
    listed_all = bool(full) and already == full and lines[at:at + len(full)] == full
    print('  PRINT_TARGETS: %d names to enter after %s, already listed %d ; anchor present %s ; all listed after it in order %s' % (
        len(full), ANCHOR.split('.')[-1], len(already), ANCHOR in lines, listed_all))
    if mode == 'dry':
        print('  DRY: nothing written ; ALL GOOD %s' % (good and frame_ok and (not already or listed_all)))
        return
    if not (good and frame_ok and ANCHOR in lines and (not already or listed_all)):
        sys.exit('### NOT WRITTEN: a check, the inequality, the hand files or print_targets.txt refused')
    for p, t in tx.items():
        with open(os.path.join(KPATH, p), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(t)
        back = rd(p)
        print('  WRITTEN %-40s read back %s' % (p.split('/')[-1], 'EQUAL' if back == t else 'DIFFERS'))
    if listed_all:
        print('  print_targets.txt: the %d names listed after %s already, in order: unchanged' % (len(full), ANCHOR.split('.')[-1]))
        return
    i = lines.index(ANCHOR)
    new = lines[:i + 1] + full + lines[i + 1:]
    nt = NL.join(new)
    with open(os.path.join(KPATH, 'print_targets.txt'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(nt)
    print('  print_targets.txt: %d lines to %d, read back %s' % (len(lines), len(new),
                                                              'EQUAL' if rd('print_targets.txt') == nt else 'DIFFERS'))


if __name__ == '__main__':
    main()
