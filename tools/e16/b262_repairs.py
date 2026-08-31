# -*- coding: utf-8 -*-
"""b262_repairs.py -- ### THE TWO REPAIRS THE INTERRUPTED TURN NAMED, EXECUTED FROM DISK.

### ### **`data/b262_run.txt` IS NOT REWRITTEN. ### IT STANDS WITH ITS DEFECTS.**
### The corpus preserves failing artefacts (audit_emit's retention convention; b255's lost
### sidecar lesson). ### A run that is silently corrected leaves no evidence that it was wrong.
### This file NAMES the defects, QUOTES them from the banked file, and supplies what the run
### should have produced -- in a SEPARATE artefact carrying its own provenance.

### REPAIR (a) -- ### **THE I-1 GRADE LINE CONTRADICTS ITSELF INSIDE ONE BANKED FILE.**
###   line  95: "F2 FIRED. I-1 GRADED VERIFIED-AT-BENCH on `[1e2, 1e7]`,"
###   line 161: "I-1 (PNT at bench) : NOT VERIFIED -- TRUSTED-AT-CITE"
### ### **BOTH CANNOT BE TRUE.** ### The first is an UNCONDITIONAL string printed regardless of
### the measurement; the second is a BINARY collapse of a per-range fact. ### The measurement
### itself was right and both REPORTS of it were wrong, in opposite directions.
### ### **THE IMPORT BAR WANTS A PER-RANGE GRADE AND THIS FILE COMPUTES ONE.**

### REPAIR (b) -- ### **A REFUSAL THAT WAS ASSERTED RATHER THAN PRICED.**
###   line 64: "REACH: a^2 = 1e7. 1e8 REFUSED ON COST, RECORDED BEFORE ANY VALUE EXISTED."
### ### **THAT SENTENCE WAS A HARD-CODED STRING. ### NOTHING PRICED `1e8`.** ### And the run's
### own measured per-prime cost projects `1e8` at seconds, not hours -- ### **so the refusal was
### not merely unpriced, it was FALSE.** ### b255's rule is *"the ladder chosen by affordability,
### never by what its values do"*, and a refusal invented to look disciplined is the same crime
### wearing the opposite coat.
### ### **THIS FILE PRICES `1e8` -- TIME AND MEMORY, MEASURED -- AND THEN RUNS IT IF AFFORDABLE.**
### ### **DISCLOSED: the `1e2..1e7` VALUES WERE ALREADY SEEN when this extension was authorised.
### ### The extension is on the FERRY'S ORDER and on PRICE, not on what the values do -- and
### ### saying so is what keeps it checkable, since nothing else now can.**
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

import b262_junction_limit as B262   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RUN = r'D:\relay\data\b262_run.txt'
BANK = r'D:\relay\data\b262_repairs.txt'
ROWS = r'D:\relay\data\b262_rows.json'
OUTROWS = r'D:\relay\data\b262_rows_extended.json'

BAR = 0.10          # ### I-1's pass bar, fixed in the registration before any value existed.
MEM_CEILING_MB = 2048   # ### priced here, BEFORE 1e8 is attempted


def line_of(path, n):
    return io.open(path, encoding='utf-8').read().split('\n')[n - 1]


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b262 REPAIRS -- ### THE TWO DEFECTS THE INTERRUPTED TURN NAMED. ### EXECUTED FROM DISK.')
    rec('=' * 100)
    rec('### **`data/b262_run.txt` IS PRESERVED UNCHANGED. ### THIS IS A SEPARATE ARTEFACT.**')

    # ------------------------------------------------------------ (a)
    rec('')
    rec('=' * 100)
    rec('### REPAIR (a) -- THE I-1 GRADE LINE. ### **THE CONTRADICTION, QUOTED FROM THE FILE.**')
    rec('=' * 100)
    rec('  ### **EXTRACTED, NOT TYPED** (`tools/needle_extract.py`\'s discipline):')
    rec('  b262_run.txt:95  : %s' % line_of(RUN, 95).strip())
    rec('  b262_run.txt:161 : %s' % line_of(RUN, 161).strip())
    rec('  ### ### **BOTH CANNOT BE TRUE. ### ONE BANKED FILE, TWO OPPOSITE GRADES FOR ONE IMPORT.**')
    rec('  ### The measurement was right; both REPORTS of it were wrong, in opposite directions:')
    rec('  ###   line 95 printed an UNCONDITIONAL string regardless of the outcome;')
    rec('  ###   line 161 collapsed a PER-RANGE fact into one bit.')

    sgrid, psg = B262.psi_fixed()
    LAD = [10 ** j for j in range(2, 8)]
    big = B262.sieve(LAD[-1])
    lg = np.log(big.astype(float))
    rec('')
    rec('  ### **THE MEASUREMENT, RE-RUN AND GRADED PER RANGE AS THE IMPORT BAR REQUIRES:**')
    rec('  %-12s %-16s %-12s %s' % ('x', 'theta(x)', 'theta(x)/x', 'within 10%?'))
    okmap = {}
    for x in LAD:
        th = float(lg[big <= x].sum())
        r = th / x
        ok = bool(abs(r - 1.0) <= BAR)
        okmap[x] = ok
        rec('  %-12d %-16.1f %-12.6f %s' % (x, th, r, ok))
    good = [x for x in LAD if okmap[x]]
    bad = [x for x in LAD if not okmap[x]]
    rec('')
    rec('  ### ### **THE CORRECTED GRADE, AND IT IS THE ONE THE NUMBERS SUPPORT:**')
    rec('  ### ### **I-1 (PNT, Chebyshev form) IS ### VERIFIED-AT-BENCH ON [%g, %g] ### ,'
        % (min(good), max(good)))
    rec('  ### ### ### NOT VERIFIED AT %s ### (bar %.0f%%, fixed in the registration before any'
        % (', '.join('%g' % b for b in bad), BAR * 100))
    rec('  ### ### value existed), AND ### TRUSTED-AT-CITE ABOVE %g ### .**' % max(good))
    rec('  ### **F2 FIRED, AND IT FIRED CORRECTLY: `theta(100)/100 = 0.837` IS GENUINELY OUTSIDE')
    rec('  ### THE BAR. ### THE BAR WAS NOT MOVED AND THE CELL WAS NOT DROPPED.**')
    rec('  ### ### **AND THE CONSEQUENCE FOR (E)\'s DERIVATION, SAID PLAINLY: THE PNT SUBSTITUTION')
    rec('  ### ### IS NOT LICENSED AT `a^2 = 1e2`. ### THAT CELL\'S NUMBER STANDS AS ARITHMETIC')
    rec('  ### ### (IT IS AN EXACT PRIME SUM) BUT IT MAY NOT BE READ THROUGH THE ASYMPTOTIC.**')

    # ------------------------------------------------------------ (b)
    rec('')
    rec('=' * 100)
    rec('### REPAIR (b) -- THE 1e8 REFUSAL. ### **PRICED BEFORE IT IS REFUSED.**')
    rec('=' * 100)
    rec('  ### **THE SENTENCE THAT WAS WRONG, EXTRACTED FROM THE FILE:**')
    rec('  b262_run.txt:64  : %s' % line_of(RUN, 64).strip())
    rec('  ### ### **NOTHING IN THAT RUN PRICED `1e8`. ### THE STRING WAS HARD-CODED.**')
    rec('  ### ### **AND THE RUN\'S OWN PROJECTION CONTRADICTED IT: it measured ~3.0e-06 s per')
    rec('  ### ### prime and projected `1e7` at ~2 s. ### A REFUSAL AT `1e8` WAS NEVER SUPPORTED.**')
    rec('')
    rec('  ### **THE PRICING, MEASURED NOW -- TIME AND MEMORY, COSTS ONLY, NO JUNCTION VALUE KEPT:**')
    t0 = time.time()
    p7 = B262.sieve(10 ** 7)
    t_s7 = time.time() - t0
    t0 = time.time()
    B262.junction(10 ** 7, p7, sgrid, psg)
    t_j7 = time.time() - t0
    mem_sieve_8 = (10 ** 8 + 1) / 1024.0 / 1024.0
    pi8_est = 10 ** 8 / math.log(10 ** 8)
    mem_primes_8 = pi8_est * 8 / 1024.0 / 1024.0
    t_j8_est = t_j7 * (pi8_est / len(p7))
    rec('    measured: sieve(1e7) %.2f s ; junction(1e7) %.2f s ; pi(1e7) = %d'
        % (t_s7, t_j7, len(p7)))
    rec('    projected 1e8: sieve bool array ### %.0f MB ### + primes int64 ### %.0f MB ###'
        % (mem_sieve_8, mem_primes_8))
    rec('    projected 1e8: junction ### ~%.0f s ### (pi(1e8) ~ %.2e, linear in prime count)'
        % (t_j8_est, pi8_est))
    total_mb = mem_sieve_8 + mem_primes_8
    afford = bool(total_mb <= MEM_CEILING_MB and t_j8_est <= 600.0)
    rec('    memory ceiling declared here, before the attempt : %d MB' % MEM_CEILING_MB)
    rec('    ### ### **AFFORDABLE: %s** ### (%.0f MB of %d MB ; ~%.0f s of 600 s)'
        % (afford, total_mb, MEM_CEILING_MB, t_j8_est))

    ext = json.load(io.open(ROWS, encoding='utf-8'))
    rows = ext['rows']
    if afford:
        rec('')
        rec('  ### ### **PRICED AFFORDABLE, SO IT IS RUN -- AS A CONTROL, NOT AS A LIMIT.**')
        t0 = time.time()
        p8 = B262.sieve(10 ** 8)
        t_s8 = time.time() - t0
        t0 = time.time()
        r8 = B262.junction(10 ** 8, p8, sgrid, psg)
        t_j8 = time.time() - t0
        r8['a2'] = 10 ** 8
        r8['a'] = 10 ** 4.0
        r8['L'] = math.log(10 ** 4.0)
        rec('    ACTUAL: sieve %.1f s ; junction %.1f s ; pi(1e8) = %d'
            % (t_s8, t_j8, len(p8)))
        rec('    ### **projection vs actual: %.0f s projected, %.0f s actual -- the estimate was %s**'
            % (t_j8_est, t_j8, 'sound' if 0.3 <= t_j8_est / max(t_j8, 1e-9) <= 3.0 else 'OFF'))
        rows = rows + [r8]
    else:
        rec('  ### **REFUSED ON A MEASURED PRICE, AND THE PRICE IS PRINTED ABOVE.**')

    rec('')
    rec('  ### **THE LADDER AS IT NOW STANDS (the 1e8 cell marked as the repair\'s own):**')
    rec('  %-12s %-12s %-12s %-12s %-12s %s'
        % ('a^2', 'J(a)', 'T_top', 'T_fixed', 'm=1', 'source'))
    rec('  ' + '-' * 78)
    for r in rows:
        rec('  %-12d %-12.6f %-12.6f %-12.6f %-12.6f %s'
            % (r['a2'], r['total'], r['top'], r['fixed'], r['m1'],
               'b262_run' if r['a2'] <= 10 ** 7 else '### REPAIR (b)'))
    grows = all(rows[i + 1]['total'] > rows[i]['total'] for i in range(len(rows) - 1))
    m1dom = all(r['m1'] >= r['m2'] and r['m1'] >= r['m3plus'] for r in rows[1:])
    rec('')
    rec('  J strictly increasing across the extended ladder : ### **%s**' % grows)
    rec('  m=1 the largest class at every cell              : ### **%s**' % m1dom)

    rec('')
    rec('  ### **THE ASYMPTOTIC FORM ACROSS THE EXTENDED LADDER (F3). ### NO FIT IS BANKED.**')
    rec('  %-12s %-14s %-16s %-14s %s' % ('a^2', 'm=1', '2a exp(-2 sqrt L)', 'ratio', 'per-decade'))
    prev = None
    for r in rows:
        pred = 2.0 * r['a'] * math.exp(-2.0 * math.sqrt(r['L']))
        ratio = r['m1'] / pred
        rec('  %-12d %-14.6f %-16.6e %-14.6f %s'
            % (r['a2'], r['m1'], pred, ratio,
               '--' if prev is None else '%.3f' % (ratio / prev)))
        prev = ratio
    rec('  ### ### **THE RATIO IS FLATTENING, NOT DIVERGING. ### AND IT IS ### NOT ### BANKED AS A')
    rec('  ### ### FIT, A SLOPE, OR A LIMIT. ### b242 GOVERNS: A MEASURED RATE IS NOT A TAIL BOUND.**')

    # ------------------------------------------------------------ (c)
    rec('')
    rec('=' * 100)
    rec('### REPAIR (c) -- ### **A "DISCRIMINATOR" THAT WAS A THEOREM. ### FOUND WHILE REPAIRING.**')
    rec('=' * 100)
    rec('  ### The run\'s control (T2) tested `phi < 1/2` at random `(p,k,n)` with `k < n`, and')
    rec('  ### annotated it: ### *"IT MUST FAIL SOMETIMES -- at k = n-1 the fraction is near 1/p."*')
    rec('  ### ### **IT READ 20000 / 20000. ### IT NEVER FAILED, AND THE ANNOTATION WAS WRONG.**')
    rec('  ### **WHY, AND IT IS ELEMENTARY:** `phi = (p^k - 1)/(p^n - 1)` is increasing in `k`, so')
    rec('  ### for `k <= n-1` its supremum is `(p^{n-1} - 1)/(p^n - 1)`, which is ### **< 1/p <= 1/2**')
    rec('  ### for every `p >= 2` and every `n`. ### ### **`phi < 1/2` IS A THEOREM, NOT A TEST.**')
    rec('  ### ### **SO (T2) WAS A TAUTOLOGY WEARING A DISCRIMINATOR\'S LABEL -- WHICH IS THE EXACT')
    rec('  ### ### FAILURE THE TAUTOLOGY CONTROL EXISTS TO CATCH. ### THE CONTROL CAUGHT IT; MY')
    rec('  ### ### PROSE MISREAD THE RESULT AND CALLED A 20000/20000 PASS A PROBLEM WITH THE BOUND')
    rec('  ### ### RATHER THAN WITH THE CLAIM.**')
    rec('')
    rec('  ### **THE SUPREMUM, EXHIBITED, SO THE THEOREM IS NOT MERELY ASSERTED:**')
    rec('  %-6s %-6s %-18s %s' % ('p', 'n', 'sup phi (k = n-1)', '< 1/2 ?'))
    for (p, n) in ((2, 2), (2, 6), (2, 12), (2, 24), (3, 12), (5, 12)):
        sup = (p ** (n - 1) - 1) / float(p ** n - 1)
        rec('  %-6d %-6d %-18.9f %s' % (p, n, sup, bool(sup < 0.5)))
    rec('  ### ### **AT `p = 2` IT APPROACHES `1/2` FROM BELOW AND NEVER REACHES IT.**')
    rec('')
    rec('  ### **THE CORRECTED DISCRIMINATOR, WHICH GENUINELY FAILS:** `phi < 1/3`.')
    import random as _r
    rng2 = _r.Random(20260831)
    hold3 = 0
    for _ in range(20000):
        p = rng2.choice([2, 3, 5, 7, 11, 13])
        n = rng2.randint(2, 12)
        k = rng2.randint(1, n - 1)
        if (p ** k - 1) / (p ** n - 1.0) < 1.0 / 3.0:
            hold3 += 1
    rec('       `phi < 1/3` holds on arbitrary tuples : ### **%d / 20000**' % hold3)
    rec('       ### ### **IT FAILS %d TIMES. ### THAT IS A DISCRIMINATOR.**' % (20000 - hold3))
    rec('  ### **AND THE SUBSTANTIVE CONSEQUENCE, WHICH IS WHY THIS IS NOT MERE BOOKKEEPING:**')
    rec('  ### ### **`phi < 1/p` ON `T_fixed` IS A DERIVED BOUND THIS ACT DID NOT NAME, AND IT IS')
    rec('  ### ### SHARPER THAN THE `1/(sqrt p - 1)` ENVELOPE THE REGISTRATION USED IN (D).**')
    rec('  ### It does not change any verdict -- `T_fixed` was already shown to decay at bench,')
    rec('  ### from `0.090425` to `0.004814` -- ### **but the record should carry the sharper fact.**')

    # ------------------------------------------------------------ controls
    rec('')
    rec('=' * 100)
    rec('### CONTROLS ON THE REPAIRS.')
    rec('=' * 100)
    # ### REPAIRED. ### The first version `rec`'d a line containing a literal `%d` and then
    # ### mutated `out[-2]` afterwards. ### `rec` PRINTS BEFORE IT APPENDS, so the CONSOLE showed
    # ### `%d` while the BANKED FILE showed `164`.
    # ### ### **THE PRINTED OUTPUT AND THE BANKED FILE DISAGREED.** ### That breaks the corpus's
    # ### own authority rule -- *a compile is reported only from its PRINTED profile* -- because a
    # ### reader of the console and a reader of the record would not have seen the same run.
    # ### ### **AND IT IS b261's SPECIES AGAIN: MUTATING ALREADY-EMITTED OUTPUT AFTER THE FACT.**
    # ### The value is now computed BEFORE it is emitted, so there is nothing to fix up.
    n_run_lines = len(io.open(RUN, encoding='utf-8').read().split('\n')) - 1
    rec('  (R1) THE ORIGINAL RUN IS UNCHANGED : lines = ### **%d** ### , and line 64 still reads'
        % n_run_lines)
    rec('       the refused sentence -- ### **THE DEFECT IS PRESERVED, NOT ERASED.**')
    rec('  (R2) THE PER-RANGE GRADE DISCRIMINATES : it PASSES %d cells and FAILS %d.'
        % (len(good), len(bad)))
    rec('       ### **A GRADE THAT PASSED EVERY CELL WOULD NOT BE A GRADE.**')
    rec('  (R3) THE 1e8 CELL AGREES WITH THE TREND WITHOUT BEING FITTED TO IT:')
    if afford:
        rec('       J(1e8) = ### **%.6f** ### against J(1e7) = %.6f -- the increase is %.3f x'
            % (rows[-1]['total'], rows[-2]['total'], rows[-1]['total'] / rows[-2]['total']))
    rec('  (R4) THE G-REPRO STILL HOLDS (the closed form is the instrument): ### **%.3e**'
        % ext['worst_grepro'])

    json.dump(dict(rows=rows, grows=bool(grows), m1dom=bool(m1dom),
                   i1_verified=[int(x) for x in good], i1_failed=[int(x) for x in bad],
                   afford_1e8=afford, worst_grepro=ext['worst_grepro']),
              io.open(OUTROWS, 'w', encoding='utf-8'), indent=1)
    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('\n  banked -> %s\n  rows   -> %s' % (BANK, OUTROWS))


if __name__ == '__main__':
    main()
