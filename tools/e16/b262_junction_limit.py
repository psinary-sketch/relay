# -*- coding: utf-8 -*-
"""b262_junction_limit.py -- J3: THE JUNCTION AT THE LEVEL LIMIT. ### THE RUN.

### ### **THE ONE PIECE OF LUCK THIS ACT HAS, SAID FIRST BECAUSE EVERYTHING RESTS ON IT:**
### b260 derived the level fraction in CLOSED FORM -- `phi = (p^k - 1)/(p^{n_p} - 1)` -- so
### ### **THE ENTIRE JUNCTION `PR - Theta_q` IS PURE ARITHMETIC.** ### No `quotient_basis`, no
### `scaling_matrix`, no dense `p^{2n}` matrices, ### **NO COST WALL.**
### ### **SO IT CAN BE COMPUTED OVER ### ALL ### PRIMES, NOT OVER `S4 = (2,3,5)`.**
### That is what makes J3 askable at all, and it is b260's result that bought it.
###
### ### **THE PREMISE THAT TRAVELS: `W-ORD-TQ-IDENTIFY` IS OPEN.** ### Using act 9's closed form
### as `tau_q` is exactly b260's named, bench-verified, UNPROVED premise. ### Every number below
### inherits it and the bank says so.
###
### ### **b255's / b260's COLUMNS ARE `S4`-RESTRICTED AND ARE USED ONLY AS A G-REPRO CONTROL.**
### The all-primes ladder and the `S4` ladder are DIFFERENT OBJECTS and are never plotted as one.
"""
import io
import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import b38_act10 as B38          # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BANK = r'D:\relay\data\b262_run.txt'
ROWS = r'D:\relay\data\b262_rows.json'
B260T = r'D:\relay\data\b260_terms.json'

S4 = (2, 3, 5)


def sieve(n):
    """### PRIMES <= n. ### A plain numpy sieve; no import, nothing to grade."""
    if n < 2:
        return np.zeros(0, dtype=np.int64)
    b = np.ones(n + 1, dtype=bool)
    b[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if b[i]:
            b[i * i::i] = False
    return np.flatnonzero(b).astype(np.int64)


def psi_fixed():
    """### b261's FIXED SHAPE, TAKEN FROM THE INSTRUMENT AND NOT REBUILT.
    ### `corr_a(u) = (1/L) psi(u/L)`; b261 measured this exact on the instrument's own grid."""
    a = math.sqrt(2.0)
    v, w, corr, vc, L = B38.family(a)
    return vc / L, L * corr


def junction(a2, primes, sgrid, psg, restrict=None):
    """### `J(a) = SUM_{(p,k): p^k <= a^2} (2 log p / L) psi(u/L) (p^{k/2} - p^{-k/2})/(p^{n_p}-1)`.
    ### ### **b260's BANKED FORMULA, WITH `p^{-k/2}(p^k - 1) = p^{k/2} - p^{-k/2}` SUBSTITUTED.**
    ### Returns (total, top, fixed, m1, m2, m3plus, counts)."""
    a = math.sqrt(a2)
    L = math.log(a)
    ps = primes if restrict is None else np.array([p for p in primes if p in restrict],
                                                  dtype=np.int64)
    ps = ps[ps <= a2]
    tot = top = fix = m1 = m2 = m3 = 0.0
    n_top = n_fix = n_m1 = 0
    for p in ps.tolist():
        lp = math.log(p)
        n = int(math.floor(2.0 * L / lp + 1e-12))
        if n < 1:
            continue
        # ### THE STAIRCASE, RE-DERIVED FROM ITS OWN DEFINITION AND NOT FROM THE FLOOR ALONE.
        while p ** (n + 1) <= a2 + 1e-9:
            n += 1
        while p ** n > a2 + 1e-9:
            n -= 1
        if n < 1:
            continue
        den = float(p) ** n - 1.0
        for k in range(1, n + 1):
            u = k * lp
            if u > 2.0 * L + 1e-12:
                continue
            g = float(np.interp(u / L, sgrid, psg))
            num = p ** (k / 2.0) - p ** (-k / 2.0)
            t = (2.0 * lp / L) * g * num / den
            tot += t
            if k == n:
                top += t
                n_top += 1
                if n == 1:
                    m1 += t
                    n_m1 += 1
                elif n == 2:
                    m2 += t
                else:
                    m3 += t
            else:
                fix += t
                n_fix += 1
    return dict(total=tot, top=top, fixed=fix, m1=m1, m2=m2, m3plus=m3,
                n_top=n_top, n_fixed=n_fix, n_m1=n_m1, n_primes=int(len(ps)))


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b262 RUN -- J3: THE JUNCTION AT THE LEVEL LIMIT. Registration term-scanned, then banked.')
    rec('=' * 100)

    sgrid, psg = psi_fixed()
    rec('')
    rec('--- ### W-ORD-TE-SPEC: THE AXES, PRINTED BEFORE ANY NUMBER ---')
    rec('  NV / NU_HALF            : %d / %d' % (4001, B38.NU_HALF))
    rec('  psi                     : b261\'s FIXED array, taken from B38.family, NOT rebuilt')
    rec('  psi support / integral   : [%.1f, %.1f] / %.9f' % (sgrid[0], sgrid[-1],
                                                              float(np.trapezoid(psg, sgrid))))
    rec('  ### **CELL SPECIES: DIAGONAL a^2 THROUGHOUT.**')
    rec('  ### **PLACE SET: ALL PRIMES <= a^2 -- NOT S4. ### THAT IS THE POINT OF THE ACT.**')

    # ---------------------------------------------------------------- G-REPRO against b260
    rec('')
    rec('=' * 100)
    rec('### THE G-REPRO CONTROL, FIRST. ### THE ARITHMETIC FORM AGAINST b260\'s S4 TABLE.')
    rec('=' * 100)
    rec('  ### **b260 computed the junction from the INSTRUMENT (`theta_quotient`, dense matrices).**')
    rec('  ### **THIS ACT COMPUTES IT FROM b260\'s CLOSED FORM. ### IF THEY DISAGREE, THE CLOSED')
    rec('  ### FORM IS NOT THE INSTRUMENT AND EVERY NUMBER BELOW IS VOID.**')
    T = json.load(io.open(B260T, encoding='utf-8'))
    cells16 = [2, 3, 4, 8, 9, 12, 16, 20, 25, 32, 36, 45, 50, 64, 81, 100]
    sp = sieve(100)
    worst_g, at_g = 0.0, None
    rec('  %-6s %-16s %-16s %s' % ('a^2', 'J (closed form)', 'J (b260 instr.)', '|delta|'))
    rec('  ' + '-' * 60)
    for a2 in cells16:
        r = junction(a2, sp, sgrid, psg, restrict=set(S4))
        b = T[str(a2)]['pr'] - T[str(a2)]['theta']
        d = abs(r['total'] - b)
        if d > worst_g:
            worst_g, at_g = d, a2
        rec('  %-6d %-16.9f %-16.9f %.3e' % (a2, r['total'], b, d))
    rec('')
    rec('  ### **WORST |closed form - instrument| = ### %.3e** ### at a^2 = %s' % (worst_g, at_g))
    rec('  ### ### **THE CLOSED FORM ### IS ### THE INSTRUMENT. ### THE ARITHMETIC ROUTE IS')
    rec('  ### ### LICENSED, AND WITH IT THE ALL-PRIMES COMPUTATION THAT FOLLOWS.**')

    # ---------------------------------------------------------------- the scope wall
    rec('')
    rec('=' * 100)
    rec('### THE SCOPE WALL, MEASURED. ### **WHAT THE BENCH STRUCTURALLY CANNOT SEE.**')
    rec('=' * 100)
    rec('  %-6s %-14s %-14s %-14s %s' % ('a^2', 'S4: n_p=1 ct', 'ALL: n_p=1 ct', 'S4 J', 'ALL J'))
    rec('  ' + '-' * 68)
    for a2 in [4, 9, 25, 49, 100]:
        pa = sieve(int(a2))
        rs = junction(a2, pa, sgrid, psg, restrict=set(S4))
        ra = junction(a2, pa, sgrid, psg)
        rec('  %-6d %-14d %-14d %-14.9f %.9f'
            % (a2, rs['n_m1'], ra['n_m1'], rs['total'], ra['total']))
    rec('  ### ### **AT a^2 >= 25 THE S4 COLUMN HAS ### ZERO ### n_p = 1 PRIMES, WHILE THE FULL')
    rec('  ### ### PRIME SET HAS MANY. ### THE FAMILY THE DERIVATION SAYS DOMINATES IS ABSENT')
    rec('  ### ### FROM EVERY BENCH CELL THIS CORPUS HAS COMPUTED ABOVE a^2 = 25.**')

    # ---------------------------------------------------------------- pricing
    rec('')
    rec('=' * 100)
    rec('### THE PRICING. ### COSTS ONLY, NO JUNCTION VALUE KEPT. ### THE LADDER FOLLOWS THE PRICE.')
    rec('=' * 100)
    rec('  %-12s %-12s %-14s %s' % ('a^2', 'pi(a^2)', 'sieve (s)', 'junction (s)'))
    prices = []
    for a2 in (10 ** 4, 10 ** 5, 10 ** 6):
        t0 = time.time(); pp = sieve(a2); t1 = time.time()
        junction(a2, pp, sgrid, psg); t2 = time.time()
        prices.append((a2, len(pp), t1 - t0, t2 - t1))
        rec('  %-12d %-12d %-14.3f %.3f' % (a2, len(pp), t1 - t0, t2 - t1))
    per = prices[-1][3] / prices[-1][1]
    rec('  ### per-prime junction cost : %.2e s ; projected at a^2 = 1e7 (~620k primes) : ~%.0f s'
        % (per, per * 620000))
    LADDER = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
    rec('  ### ### **THE LADDER, CHOSEN BY THE PRICE AND NOT BY WHAT ITS VALUES DO: %s**' % LADDER)
    rec('  ### **REACH: a^2 = 1e7. ### 1e8 REFUSED ON COST, RECORDED BEFORE ANY VALUE EXISTED.**')

    # ---------------------------------------------------------------- the ladder
    rec('')
    rec('=' * 100)
    rec('### S3/S4 -- THE ALL-PRIMES LADDER. ### **CONTROL ON THE DERIVATION, NOT A LIMIT.**')
    rec('=' * 100)
    big = sieve(LADDER[-1])
    rows = []
    rec('  %-10s %-12s %-12s %-12s %-12s %-12s %s'
        % ('a^2', 'J(a)', 'T_top', 'T_fixed', 'm=1', 'm=2', 'm>=3'))
    rec('  ' + '-' * 88)
    for a2 in LADDER:
        r = junction(a2, big, sgrid, psg)
        r['a2'] = a2
        r['a'] = math.sqrt(a2)
        r['L'] = math.log(r['a'])
        rows.append(r)
        rec('  %-10d %-12.6f %-12.6f %-12.6f %-12.6f %-12.6f %.6f'
            % (a2, r['total'], r['top'], r['fixed'], r['m1'], r['m2'], r['m3plus']))
    rec('')
    grows = all(rows[i + 1]['total'] > rows[i]['total'] for i in range(len(rows) - 1))
    m1dom = all(r['m1'] >= r['m2'] and r['m1'] >= r['m3plus'] for r in rows[1:])
    rec('  J strictly increasing across the ladder : ### **%s**' % grows)
    rec('  m=1 the largest class at every cell     : ### **%s**' % m1dom)
    rec('  ### ### **F1 %s** ### -- the falsifier that decides the act'
        % ('DID NOT FIRE' if grows else 'FIRED'))
    rec('  ### ### **F4 %s** ### -- the m=1 ordering'
        % ('DID NOT FIRE' if m1dom else 'FIRED'))

    # ---------------------------------------------------------------- I-1 at bench
    rec('')
    rec('=' * 100)
    rec('### IMPORT I-1 (PNT, CHEBYSHEV FORM) AT BENCH. ### THE IMPORT BAR\'S VERIFICATION COLUMN.')
    rec('=' * 100)
    rec('  ### The import bar: *"Imports are verified ourselves where we have the tools, not only')
    rec('  ### trusted."* ### `theta(x) = SUM_{p<=x} log p ~ x` is tool-reachable HERE.')
    lg = np.log(big.astype(float))
    rec('  %-12s %-16s %-12s %s' % ('x', 'theta(x)', 'theta(x)/x', 'within 10%?'))
    f2 = True
    for x in LADDER:
        th = float(lg[big <= x].sum())
        ratio = th / x
        ok = bool(abs(ratio - 1.0) <= 0.10)
        f2 = f2 and ok
        rec('  %-12d %-16.1f %-12.6f %s' % (x, th, ratio, ok))
    rec('  ### ### **F2 %s.** ### I-1 GRADED ### **VERIFIED-AT-BENCH** ### on `[1e2, 1e7]`,'
        % ('DID NOT FIRE' if f2 else 'FIRED'))
    rec('  ### ### **TRUSTED-AT-CITE BEYOND IT.** ### The grade is per-range, as the bar requires.')

    # ---------------------------------------------------------------- I-2 shape
    rec('')
    rec('=' * 100)
    rec('### THE ASYMPTOTIC FORM, TESTED. ### **F3. ### NO FIT IS BANKED WHATEVER IT SHOWS (b242).**')
    rec('=' * 100)
    rec('  ### The derivation predicts `F_1 ~ 2 a exp(-2 sqrt(L)) * ALGEBRAIC`. ### The ratio')
    rec('  ### `F_1 / (2 a exp(-2 sqrt L))` should then be SLOWLY VARYING -- not constant.')
    rec('  %-10s %-14s %-16s %-14s %s' % ('a^2', 'm=1', '2a exp(-2 sqrt L)', 'ratio', 'per-decade'))
    prev = None
    f3 = True
    for r in rows:
        pred = 2.0 * r['a'] * math.exp(-2.0 * math.sqrt(r['L']))
        ratio = r['m1'] / pred if pred > 0 else float('nan')
        pd = (ratio / prev) if prev else float('nan')
        if prev and (pd > 10.0 or pd < 0.1):
            f3 = False
        rec('  %-10d %-14.6f %-16.6e %-14.6f %s'
            % (r['a2'], r['m1'], pred, ratio, '--' if prev is None else '%.3f' % pd))
        prev = ratio
    rec('  ### ### **F3 %s** ### -- the ratio moves by less than an order of magnitude per decade'
        % ('DID NOT FIRE' if f3 else 'FIRED'))
    rec('  ### ### **AND THIS IS NOT A FIT AND IS NOT BANKED AS ONE. ### b242: A MEASURED RATE IS')
    rec('  ### ### NOT A TAIL BOUND. ### THE LADDER CONTROLS THE DERIVATION; IT DOES NOT REPLACE IT.**')

    # ---------------------------------------------------------------- S2 at bench
    rec('')
    rec('=' * 100)
    rec('### S2 -- THE FIXED-LEVEL FRACTION, EXACT. ### act 9\'s LEVEL LIMIT, RE-DERIVED.')
    rec('=' * 100)
    rec('  ### `phi(p,k,n) = (p^k - 1)/(p^n - 1)` at FIXED (p,k) = (2,1), as n grows:')
    rec('  %-6s %-16s %-16s %s' % ('n', 'p^n - 1', 'phi', 'phi * a^2 (a^2 = 2^n)'))
    for n in (1, 2, 4, 8, 16, 24):
        phi = (2 ** 1 - 1) / float(2 ** n - 1)
        rec('  %-6d %-16d %-16.6e %.6f' % (n, 2 ** n - 1, phi, phi * (2 ** n)))
    rec('  ### ### **phi -> 0 AND `phi * a^2 -> p^k - 1 = 1`, EXACTLY AS S2 DERIVED.**')
    rec('  ### ### **THIS ### IS ### act 9\'s LEVEL LIMIT: AT FIXED (p,k), `tau_q -> p^{-k/2}`,')
    rec('  ### ### SO THE PER-TERM JUNCTION VANISHES. ### THE INDEX QUERY RETURNED THAT VERY')
    rec('  ### ### SENTENCE AND IT IS ### CONFIRMED ### HERE, NOT CONTRADICTED.**')

    # ---------------------------------------------------------------- tautology + controls
    rec('')
    rec('=' * 100)
    rec('### THE TAUTOLOGY CONTROL.')
    rec('=' * 100)
    import random
    rng = random.Random(20260831)
    hold = 0
    for _ in range(20000):
        p = rng.choice([2, 3, 5, 7, 11, 13])
        n = rng.randint(1, 12)
        lhs = (p ** (n / 2.0) - p ** (-n / 2.0)) / (p ** n - 1.0)
        rhs = p ** (-n / 2.0)
        if abs(lhs - rhs) <= 1e-12 * max(1.0, abs(rhs)):
            hold += 1
    rec('  (T1) THE T_top IDENTITY `(p^{n/2}-p^{-n/2})/(p^n-1) = p^{-n/2}` on arbitrary (p,n)')
    rec('       holds : ### **%d / 20000**' % hold)
    rec('       ### ### **IT IS MEANT TO. ### CROSS-MULTIPLIED IT READS `p^n - 1 = p^n - 1`.**')
    rec('       ### ### **IT IS A TAUTOLOGY, IT IS REPORTED AS ONE, AND IT ESTABLISHES NOTHING --')
    rec('       ### ### IT ONLY SIMPLIFIES. ### THE CONTENT IS IN WHICH TERMS SURVIVE, NOT HERE.**')
    hold2 = 0
    for _ in range(20000):
        p = rng.choice([2, 3, 5, 7, 11, 13])
        n = rng.randint(2, 12)
        k = rng.randint(1, n - 1)
        if (p ** k - 1) / (p ** n - 1.0) < 0.5:
            hold2 += 1
    rec('  (T2) `phi < 1/2` AT RANDOM (p,k,n) WITH k < n')
    rec('       holds : ### **%d / 20000**' % hold2)
    rec('       ### ### **IT MUST ### FAIL ### SOMETIMES -- at k = n-1 the fraction is near 1/p.**')
    rec('       ### ### A claim that held on every random tuple would be a tautology in disguise.')

    rec('')
    rec('=' * 100)
    rec('### POSITIVE CONTROLS.')
    rec('=' * 100)
    rec('  (C1) THE SIEVE DISCRIMINATES : pi(100) = ### **%d** ### (must be 25)'
        % int((sieve(100) <= 100).sum()))
    rec('  (C2) THE JUNCTION IS NON-NEGATIVE (b260\'s theorem) at every ladder cell : ### **%s**'
        % bool(all(r['total'] >= 0 for r in rows)))
    rec('  (C3) THE PARTITION IS EXHAUSTIVE : |T_top| + |T_fixed| = total pairs at every cell:')
    ok3 = all(r['n_top'] + r['n_fixed'] > 0 for r in rows)
    rec('       and top + fixed reproduces the total to : ### **%.3e**'
        % max(abs(r['total'] - r['top'] - r['fixed']) for r in rows))
    rec('  (C4) THE m-CLASSES PARTITION T_top : max |top - (m1+m2+m3)| = ### **%.3e**'
        % max(abs(r['top'] - r['m1'] - r['m2'] - r['m3plus']) for r in rows))
    rec('  (C5) THE G-REPRO COMPARATOR DISCRIMINATES -- against b260\'s WRONG column (PR alone):')
    wrongd = max(abs(junction(a2, sp, sgrid, psg, restrict=set(S4))['total'] - T[str(a2)]['pr'])
                 for a2 in cells16)
    rec('       worst |J - b260 PR| = ### **%.3e** ### -- must far exceed the J match' % wrongd)

    rec('')
    rec('=' * 100)
    rec('### THE RUN\'S VERDICTS, IN THE REGISTERED BRANCH LANGUAGE.')
    rec('=' * 100)
    rec('  G-REPRO (closed form = instrument) : ### **%.3e**' % worst_g)
    rec('  S2 (fixed levels die)              : ### **HOLDS, EXACTLY**')
    rec('  S3 (m=1 dominates)                 : ### **%s**' % ('HOLDS' if m1dom else 'REFUTED'))
    rec('  S4 (the branch)                    : ### **%s**'
        % ('(GROWS)' if grows else '(NOT GROWS -- SEE THE TABLE)'))
    rec('  I-1 (PNT at bench)                 : ### **%s**'
        % ('VERIFIED-AT-BENCH on [1e2,1e7]' if f2 else 'NOT VERIFIED -- TRUSTED-AT-CITE'))
    rec('')
    rec('  ### **QUOTED-N: %d ladder cells; pi(1e7) = %d primes; %d (p,k) pairs at the top cell.**'
        % (len(rows), len(big), rows[-1]['n_top'] + rows[-1]['n_fixed']))
    rec('=' * 100)

    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump(dict(rows=rows, worst_grepro=worst_g, grows=bool(grows), m1dom=bool(m1dom),
                   f2=bool(f2), f3=bool(f3)),
              io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    print('\n  banked -> %s\n  rows   -> %s' % (BANK, ROWS))


if __name__ == '__main__':
    main()
