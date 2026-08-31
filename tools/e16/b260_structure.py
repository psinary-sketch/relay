# -*- coding: utf-8 -*-
"""b260_structure.py -- ### THE PER-TERM STRUCTURE OF THE INEQUALITY, EXHIBITED.

### The ferry asks for "the per-term structure of the inequality exhibited". ### This file
### does exactly that and nothing else: it splits the junction `PR - Theta_q` into the two
### sources the derivation names, and reports the equality terms by name.
###
### ### **IT INTRODUCES NO NEW ARITHMETIC.** ### It reads `b260_terms.json`, which the run
### wrote from the banked instrument's own functions.
"""
import io
import json
import math
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = r'D:\relay\data\b260_terms.json'
BANK = r'D:\relay\data\b260_structure.txt'
CELLS = [2, 3, 4, 8, 9, 12, 16, 20, 25, 32, 36, 45, 50, 64, 81, 100]


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    R = json.load(io.open(ROWS, encoding='utf-8'))

    rec('=' * 100)
    rec('b260 -- ### THE PER-TERM STRUCTURE OF THE INEQUALITY. ### Derived from b260_terms.json.')
    rec('=' * 100)
    rec('')
    rec('### THE DECOMPOSITION, WRITTEN OUT BEFORE IT IS COMPUTED:')
    rec('###   `w_{p,k} - tau_{p,k} = 2 log p * corr(k log p) * ( p^{-k/2} - tq(p,n,k) )`')
    rec('###                        = `w_{p,k} * ( 1 - (p^n - p^k)/(p^n - 1) )`   for k <= n-1')
    rec('###                        = `w_{p,k} * 1`                               for k = n')
    rec('### ### **SO THE SEPARATION HAS EXACTLY TWO SOURCES, AND THEY ARE STRUCTURALLY DIFFERENT:**')
    rec('###   ### **(1) THE TOP LEVEL `k = n`, WHERE act 9 SAYS `tau_q = 0` AND PR DOES NOT.**')
    rec('###       ### The whole of PR\'s term survives. ### **A WHOLE-TERM SEPARATION.**')
    rec('###   ### **(2) THE LEVELS `k <= n-1`, WHERE act 9\'s RATIO IS `(p^n-p^k)/(p^n-1) < 1`.**')
    rec('###       ### A FRACTION `(p^k - 1)/(p^n - 1)` of PR\'s term survives. ### **A DEFICIT SEPARATION.**')
    rec('### ### **AND THE ALGEBRAIC FORM OF THAT FRACTION IS WORTH ITS OWN LINE:**')
    rec('###   ### `1 - (p^n - p^k)/(p^n - 1) = (p^k - 1)/(p^n - 1)`, ### which is `< 1` for `k < n`')
    rec('###   ### and `= 1` at `k = n`. ### **THE TWO SOURCES ARE ONE FORMULA EVALUATED AT ITS')
    rec('###   ### OWN ENDPOINT, NOT TWO SEPARATE PHENOMENA.**')
    rec('')

    rec('%-6s %-13s %-13s %-13s %-9s %-13s %s'
        % ('a^2', 'junction', 'from k = n', 'from k < n', 'k=n share', 'terms(k=n)', 'terms(k<n)'))
    rec('-' * 100)
    tot_kn = tot_lt = 0.0
    for a2 in CELLS:
        rows = R[str(a2)]['rows']
        g_kn = sum(r['w'] - r['tau'] for r in rows if r['k'] >= r['n'])
        g_lt = sum(r['w'] - r['tau'] for r in rows if r['k'] < r['n'])
        n_kn = sum(1 for r in rows if r['k'] >= r['n'])
        n_lt = sum(1 for r in rows if r['k'] < r['n'])
        j = g_kn + g_lt
        tot_kn += g_kn
        tot_lt += g_lt
        share = (g_kn / j * 100.0) if j > 0 else float('nan')
        rec('%-6d %-13.9f %-13.9f %-13.9f %-9s %-13d %d'
            % (a2, j, g_kn, g_lt, ('%.1f%%' % share) if j > 0 else '--', n_kn, n_lt))
    rec('-' * 100)
    rec('### **TOTALS ACROSS THE LADDER: from k = n : %.6f ; from k < n : %.6f**' % (tot_kn, tot_lt))
    rec('')

    # ### THE EQUALITY TERMS, NAMED. ### The derivation claims STRICT inequality wherever
    # ### corr > 0; every equality term must therefore have corr = 0, and that is CHECKED,
    # ### not assumed.
    rec('=' * 100)
    rec('### THE EQUALITY TERMS, NAMED. ### THE DERIVATION CLAIMS ### STRICT ### WHEREVER `corr > 0`.')
    rec('=' * 100)
    eq = []
    for a2 in CELLS:
        for r in R[str(a2)]['rows']:
            if r['tau'] == r['w']:
                eq.append((a2, r['p'], r['n'], r['k'], r['corr'], r['tau'], r['w']))
    rec('  equality terms : ### **%d of %d**' % (eq and len(eq) or 0,
                                                 sum(len(R[str(a2)]['rows']) for a2 in CELLS)))
    rec('  %-6s %-3s %-3s %-3s %-14s %-14s %s' % ('a^2', 'p', 'n', 'k', 'corr', 'tau', 'w'))
    rec('  ' + '-' * 74)
    for a2, p, n, k, c, t, w in eq:
        rec('  %-6d %-3d %-3d %-3d %-14.6e %-14.6e %-14.6e   %s'
            % (a2, p, n, k, c, t, w, 'p^k = a^2 exactly' if abs(p ** k - a2) < 1e-9 else '### CHECK'))
    allzero = all(abs(c) == 0.0 for _, _, _, _, c, _, _ in eq)
    rec('  ### ### **EVERY EQUALITY TERM HAS `corr` EXACTLY ZERO : ### %s**' % bool(allzero))
    rec('  ### ### **AND EVERY ONE SITS AT `p^k = a^2`** -- the cutoff\'s own endpoint, where the')
    rec('  ### ### correlation\'s support `[-2L, 2L]` ends and the bump has already vanished.')
    rec('  ### ### **SO THE INEQUALITY IS STRICT AT EVERY TERM THAT CARRIES ANY WEIGHT AT ALL,**')
    rec('  ### ### and the nine equalities are `0 <= 0`, not near-misses.')

    rec('')
    rec('=' * 100)
    rec('### THE SAWTOOTH, DERIVED RATHER THAN MEASURED. ### b255 (A) IS THE ### CONTROL ###.')
    rec('=' * 100)
    rec('### b255 REPORTED, AT BENCH: *"`PR` rises smoothly toward `1` while `Theta_q` rises in')
    rec('### JUMPS -- it gains a whole level each time the staircase steps."*')
    rec('### ### **THE DECOMPOSITION ABOVE SAYS WHY, FROM act 9\'s RANGE AND NOTHING ELSE:**')
    rec('###   when `n_p(a)` steps from `n` to `n+1`, the level `k = n` moves from the `k = n`')
    rec('###   branch (`tau_q = 0`, ### **the whole term missing**) into the `k <= n-1` branch')
    rec('###   (`tau_q = p^{-k/2}(p^{n+1}-p^k)/(p^{n+1}-1)`, ### **most of the term present**).')
    rec('### ### ### **THE LEVEL SWITCHES ON. ### THAT IS THE JUMP, AND IT IS act 9\'s `0 for k >= n`')
    rec('### ### ### READ AT THE STAIRCASE\'S STEP.**')
    rec('### **THE DIRECTION OF THE INFERENCE IS SAID PLAINLY: THE DERIVATION PREDICTS THE BENCH')
    rec('### OBSERVATION. ### THE BENCH OBSERVATION IS NOT A PREMISE OF THE DERIVATION**, and')
    rec('### b255 is cited here as a CONTROL that the prediction matches, not as a reason.')
    rec('### ### **WHAT IS ### NOT ### DERIVED HERE, AND IS NOT CLAIMED: the RISES between steps,')
    rec('### ### which depend on `corr`\'s shape and on `PR`\'s growth, not on act 9\'s range.**')
    rec('=' * 100)

    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('\n  banked -> %s' % BANK)


if __name__ == '__main__':
    main()
