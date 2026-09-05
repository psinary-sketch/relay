# -*- coding: utf-8 -*-
"""b327_bridge.py -- THE BRIDGE READ'S CORROBORATION, AND THE LIVE ROW IT COMPOSES.

### ### **THE DERIVATION IS IN THE SEALED REGISTRATION, SECTION (3), WRITTEN BEFORE THIS FILE.** ### It
### says: the deposit's archimedean channel `lambda_A(n)` is the source's archimedean-place term
### `S_inf(n)` PLUS the pole-at-zero constant `1`, for every `n >= 1`. ### This tool measures that
### difference by two routes and applies the registered bar.

### ### **ROUTE A -- THE CORPUS'S OWN BENCH, ITS DEFINITIONS EXECUTED FROM ITS OWN FILE.** ###
### `internal/bench/li_bench.py` has no main guard: importing it runs a 130-coefficient bench at 260
### digits. ### So its DEFINITIONS section (everything above its first module-level `print`) is read
### from the file and executed here; its run section is not. ### Nothing of it is retyped: `f_A`, `f_Z`,
### `taylor_coeffs` and `lambdas` are the bench's, called at a reduced quadrature `M` and the bench's
### own two radii, with the agreement between radii REPORTED as the accuracy claim, as the bench does.
### ### **ROUTE B -- THE SOURCE'S CLOSED FORM (4.11)**, `S_inf(n) = -SUM_{j=1}^{n} (-1)^{j+1} C(n,j)
### (1 - 2^{-j}) zeta*(j)`, `zeta*(1) = log(4 pi) + gamma`, with `mpmath.zeta`. ### The two routes
### share `mpmath` and no code path.

### ### **THE DISCRIMINATION ARM:** ### the `SAME` hypothesis -- difference `0` -- is tested by the same
### code and must FAIL, or the passing arm has not been seen to discriminate (check_harness's law).

### ### **WHAT IT DOES NOT DO:** ### it proves nothing; it moves no grade; it does not evaluate the
### Weil distribution on any test function (that is the fourth control, priced and not run).
"""
import io
import json
import os
import re
import sys
from math import comb

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
BENCH = os.path.join(PP, 'internal', 'bench', 'li_bench.py')
BALANCE = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
SRC = os.path.join(D, 'b327_source_text.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NMAX = 30
M_QUAD = 512
RADII = ('0.85', '0.75')          # ### the bench's own two radii
BAR = mp.mpf('1e-20')             # ### the registered bar, section (3)
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def load_bench_definitions():
    """### THE BENCH'S DEFINITIONS, EXECUTED FROM ITS FILE; ITS RUN SECTION CUT AT THE FIRST MODULE-LEVEL print."""
    src = io.open(BENCH, encoding='utf-8').read()
    m = re.search(r'^print\(', src, re.M)
    if not m:
        raise RuntimeError('bench has no module-level print; the cut point is not where this tool expects')
    head = src[:m.start()]
    ns = {}
    exec(compile(head, BENCH, 'exec'), ns)
    for name in ('f_A', 'f_Z', 'taylor_coeffs', 'lambdas'):
        if name not in ns:
            raise RuntimeError('bench definition missing: %s' % name)
    km = re.search(r'^KEIPER = (\{[^\n]*\})', src, re.M)
    keiper = eval(km.group(1)) if km else {}
    return ns, head.count('\n'), keiper


def s_inf_closed(n):
    """### THE SOURCE'S (4.11) AT THE TRIVIAL REPRESENTATION."""
    zstar1 = mp.log(4 * mp.pi) + mp.euler
    acc = mp.mpf(0)
    for j in range(1, n + 1):
        zj = zstar1 if j == 1 else mp.zeta(j)
        acc += (-1) ** (j + 1) * comb(n, j) * (1 - mp.mpf(2) ** (-j)) * zj
    return -acc


def main():
    rec('=' * 100)
    rec('b327_bridge.py -- THE CORROBORATION OF THE DERIVED MAP lambda_A(n) = S_inf(n) + 1. ### TWO ROUTES.')
    rec('=' * 100)
    ns, cut_line, keiper = load_bench_definitions()
    rec('  route A : the bench\'s definitions executed from %s (its first %d lines; the run section not executed)'
        % (BENCH.replace(PP, '<papers>'), cut_line))
    rec('  route B : the source\'s closed form (4.11) with mpmath.zeta ; dps = %d ; M = %d ; n <= %d' % (mp.mp.dps, M_QUAD, NMAX))
    rec('  bar     : |lambda_A(n) - S_inf(n) - 1| <= %s at every n, and the two radii within the same bar' % mp.nstr(BAR, 3))
    rec('')
    lamA, lamZ, lamLog = {}, {}, {}
    for r in RADII:
        etaA = ns['taylor_coeffs'](ns['f_A'], mp.mpf(r), M_QUAD, NMAX)
        etaZ = ns['taylor_coeffs'](ns['f_Z'], mp.mpf(r), M_QUAD, NMAX)
        etaL = ns['taylor_coeffs'](mp.log, mp.mpf(r), M_QUAD, NMAX)   # ### the pole-at-zero term alone
        lamA[r] = ns['lambdas'](etaA, NMAX)
        lamZ[r] = ns['lambdas'](etaZ, NMAX)
        lamLog[r] = ns['lambdas'](etaL, NMAX)
    r0, r1 = RADII
    rec('  %4s %24s %24s %14s %14s %14s %14s' % ('n', 'lambda_A (route A)', 'S_inf + 1 (route B)', '|diff|', 'radii agree', 'L_n(log s)-1', '|A-S_inf| SAME arm'))
    worst, worst_r, worst_log, worst_same = mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf('inf')
    table = []
    for n in range(1, NMAX + 1):
        a = lamA[r0][n]
        s = s_inf_closed(n)
        dif = abs(a - s - 1)
        agree = abs(lamA[r0][n] - lamA[r1][n])
        dlog = abs(lamLog[r0][n] - 1)
        same = abs(a - s)
        worst = max(worst, dif)
        worst_r = max(worst_r, agree)
        worst_log = max(worst_log, dlog)
        worst_same = min(worst_same, same)
        table.append(dict(n=n, lambda_A=mp.nstr(a, 25), S_inf_plus_1=mp.nstr(s + 1, 25), diff=mp.nstr(dif, 3),
                          radii=mp.nstr(agree, 3), log_term=mp.nstr(lamLog[r0][n], 25), same_arm=mp.nstr(same, 6)))
        rec('  %4d %24s %24s %14s %14s %14s %14s' % (n, mp.nstr(a, 18), mp.nstr(s + 1, 18), mp.nstr(dif, 3),
                                                     mp.nstr(agree, 3), mp.nstr(dlog, 3), mp.nstr(same, 6)))
    rec('')
    holds = (worst <= BAR) and (worst_r <= BAR)
    fires = worst_same > BAR
    rec('  worst |lambda_A - S_inf - 1| over n <= %d : %s   (bar %s)  %s' % (NMAX, mp.nstr(worst, 3), mp.nstr(BAR, 3), 'HOLDS' if worst <= BAR else '### FAILS ###'))
    rec('  worst disagreement between the two radii     : %s   %s' % (mp.nstr(worst_r, 3), 'HOLDS' if worst_r <= BAR else '### FAILS ###'))
    rec('  worst |L_n(log s) - 1| (the pole term alone) : %s   %s' % (mp.nstr(worst_log, 3), 'HOLDS' if worst_log <= BAR else '### FAILS ###'))
    rec('  ### THE DISCRIMINATION ARM -- the SAME hypothesis (difference 0) -- smallest |lambda_A - S_inf| : %s  %s'
        % (mp.nstr(worst_same, 6), 'FIRES (the SAME arm fails at every n)' if fires else '### DOES NOT FIRE -- the check cannot discriminate ###'))
    rec('')
    rec('  ### THE SUM AGAINST THE BENCH\'S OWN LITERATURE VALUES (a consistency line, not a bar):')
    for n in sorted(keiper):
        tot = lamA[r0][n] + lamZ[r0][n]
        rec('    n = %d  lambda_A + lambda_Z = %s   literature %s   |diff| %s'
            % (n, mp.nstr(tot, 14), keiper[n], mp.nstr(abs(tot - mp.mpf(keiper[n])), 3)))
    rec('')
    # ### THE BRANCHES, BY THE REGISTERED BARS AND NOTHING ELSE
    if holds and fires:
        q1 = 'DIFFERENT, constituent quoted'
        q1_why = ('the difference is the constant 1 at every n -- the `log s` term of f_A, the source\'s "contribution from '
                  'the pole at s = 0"; the gamma-factor part of the channel IS the archimedean-place term, map derived, '
                  'normalizations reconciled with nothing left over')
    elif not holds:
        q1 = 'UNDECIDED, bridge typed'
        q1_why = 'the corroboration did not return the derived difference; the derivation is wrong or under-resolved and the act says so'
    else:
        q1 = 'UNDECIDED, bridge typed'
        q1_why = 'the check could not discriminate the SAME hypothesis from the derived one'
    # ### question two is decided at definitions: the second terms, quoted
    q2 = 'DIFFERENT, constituent quoted'
    q2_why = ('the Li margin is (1/2) of the Weil norm of G_n (the source\'s (3.4)), whose second term is the finite '
              'places, lambda_Z(n) = -S_f(n); the Sonin margin\'s second term is the compressed square Tr(theta(g) S theta(g)*) '
              '-- b324, constituent (4): "The square is not a zero channel" -- and the arc measures the Weil functional on '
              'its family SEPARATELY, as the zero side (b321: "SUM_v W_v(f) = - Z"). No statement in the record identifies '
              'the compressed square with a finite-place sum, and this act claims none.')
    rec('  ### QUESTION ONE : %s -- %s' % (q1, q1_why))
    rec('  ### QUESTION TWO : %s -- %s' % (q2, q2_why))
    rec('  ### ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL: the archimedean distribution 2 Re(Gamma_R\'/Gamma_R) on')
    rec('  ### the line -- the atlas\'s kernel Re psi(1/4 + iu/2) - log pi -- is what both channels evaluate, on the Li')
    rec('  ### family through its Taylor coefficients at s = 1 and on the Sonin family through the atlas\'s integral.')
    rec('  ### THE "IF SAME" BRANCH OF THE ORDER : %s' % ('FIRES' if q2.startswith('SAME') else 'DOES NOT FIRE'))
    rec('  ### AT SCOPE, WHAT THE FINITE-RANGE CERTIFICATE SAYS ABOUT THE SONIN MARGIN ON THE LI FAMILY : nothing -- G_n(s)')
    rec('  ### is a rational function whose inverse Mellin transform has no compact support, so the Li family lies outside')
    rec('  ### Theorem 1\'s class (supp g in [2^-1/2, 2^1/2]) and the Sonin margin is not defined on it.')
    rec('  ### THE FOURTH CONTROL, PRICED, NOT RUN: the explicit formula closed on the Li family through the corpus\'s channels')
    rec('  ### (zero side over the atlas\'s 10000 ordinates; S_inf by a third route, the atlas kernel against G_n on the')
    rec('  ### line, its conditionally convergent u-tail bounded; the zero tail O(n log T / T) bounded). One act.')
    rec('=' * 100)

    verdict_ok = holds and fires
    row_cells = [
        'L1 -- the Li-to-Weil bridge: the Li coefficients as the Weil functional on the Li test family G_n(s) = 1 − (1 − 1/s)^n; the deposit\'s archimedean channel against the archimedean place; the Li margin against the Sonin margin',
        'the fourth, at two families -- the Li family (indexed by a coefficient n) and the Sonin family (indexed by a width a)',
        'IMPORTED -- J. C. Lagarias, *Li coefficients for automorphic L-functions*, arXiv:math/0404394v4, pinned by this act (sha256 `86f3d3c4…`, 423379 bytes), restating Bombieri–Lagarias 1999 (its [4]; not obtainable by this seat). INTERNAL -- `phase1.5/spectral/BALANCE_AND_POSITIVITY.md` line 427; `internal/bench/li_bench.py`; relay `data/b324_the_keystones_reread.txt`; this act\'s `data/b327_bridge_run.txt`',
        ('IMPORTED -- the source: *"λn = S∞(n) − Sf(n) + 1, in which S∞(n) and Sf(n) correspond to the contributions of the archimedean place and the finite places, respectively, and the last term is a contribution from the pole at s = 0"*; its (3.2)-(3.4): *"The special test functions Gn(s)"* with ‖G_n‖²_W = 2 Re(λ_n). '
         'DERIVED, this act, as a bar sealed before any run: the deposit\'s Li map on its own *"f_A(s) = log s + logΓ(s/2) − (s/2)log π"* gives λ_A(n) = S∞(n) + 1 for every n ≥ 1 -- the gamma factor is exactly the source\'s archimedean term and `log s` is exactly the source\'s pole constant. '
         'MEASURED, the corroboration: worst \\|λ_A(n) − S∞(n) − 1\\| = %s at n ≤ %d by two routes (the bench\'s own functions; the source\'s (4.11)), the two radii within %s; the SAME arm (difference 0) fails by at least %s at every n. '
         'QUESTION ONE: %s. QUESTION TWO: %s -- the Li margin\'s second term is the finite places; the Sonin margin\'s is the compressed square, *"The square is not a zero channel"* (b324), and the arc measures the Weil functional on its family separately, *"SUM_v W_v(f) = - Z"* (b321). ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL. No theorem is proved; no grade moves; the equivalence the deposit withholds is not stated.'
         % (mp.nstr(worst, 3), NMAX, mp.nstr(worst_r, 3), mp.nstr(worst_same, 4), q1, q2)),
        '166, 167 (b327)',
        ('OWED -- `W-ORD-LI-WEIL-BRIDGE`, sharpened: what would carry W_∞(f) − Tr(θ(g) S θ(g)*) to λ_n is a relation between the compressed square on the Sonin family and the finite-place channel λ_Z(n) = −S_f(n) on the Li family; none is in the record (b324: *"a formula carrying the archimedean margin"* … or a proof that none exists) and none is claimed. '
         'OWED -- `W-ORD-LI-FAMILY-CONTROL`: the formula closed on the Li family through the corpus\'s own channels, priced at one act, not run. The order\'s *if SAME* branch %s; at scope, the deposit\'s finite-range certificate says nothing about the Sonin margin on the Li family, whose members have no compact support and lie outside Theorem 1\'s class.'
         % ('fires' if q2.startswith('SAME') else 'did not fire')),
    ]
    row_quotes = [
        [SRC, 'correspond to the contributions of the archimedean place and the finite places', True],
        [SRC, 'the last term is a contribution from the pole at s = 0', True],
        [SRC, 'The special test functions Gn(s)', True],
        [BALANCE, 'f_A(s) = log s + logΓ(s/2) − (s/2)log π', False],
        [os.path.join(D, 'b324_the_keystones_reread.txt'), 'The square is not a zero channel', False],
        [os.path.join(D, 'b324_the_keystones_reread.txt'), 'a formula carrying the archimedean margin', False],
        [os.path.join(D, 'b321_the_window_opened.txt'), 'SUM_v W_v(f) = - Z', False],
    ]
    pairs = {
        'L1|R4': ['STATED',
                  'the pinned source, page 3: *"each positivity condition λn ≥ 0 encodes \'Weil positivity\' of Weil\'s quadratic functional for a particular test function gn(x)"* -- the fourth face\'s Li form is the Weil functional on the Li family, IMPORTED at cite.',
                  [[SRC, 'of Weil', True], [SRC, 'quadratic functional for a particular test function', True]]],
        'L1|F1': ['OWED',
                  '`W-ORD-LI-FAMILY-CONTROL`. The finite-instance identity is closed on the arc\'s family (F1) and not on the Li family; closing it there through the corpus\'s own channels -- zero side over the atlas\'s ordinates, S∞ by the atlas\'s kernel against G_n on the line -- is the fourth control, priced at one act and not run.',
                  []],
        'L1|F2': ['OWED',
                  '`W-ORD-LI-WEIL-BRIDGE`. The Sonin margin\'s archimedean term is the same distribution the Li channel evaluates; its second term is the compressed square, which no statement in the record carries to a finite-place sum. The bridge owed is that relation, or a proof that none exists (b324: *"a formula carrying the archimedean margin"*).',
                  [[os.path.join(D, 'b324_the_keystones_reread.txt'), 'a formula carrying the archimedean margin', False]]],
        'L1|F3': ['OWED',
                  '`W-ORD-LI-WEIL-BRIDGE`. The Li margin is (1/2)‖G_n‖²_W; its archimedean channel is the archimedean place plus the pole constant (this row, %s); its finite channel is what the Sonin margin does not contain. The bridge owed is the same one, seen from the Li side.' % q1,
                  []],
    }
    out = dict(nmax=NMAX, M=M_QUAD, radii=list(RADII), dps=mp.mp.dps, bar=mp.nstr(BAR, 3),
               worst_diff=mp.nstr(worst, 6), worst_radii=mp.nstr(worst_r, 6), worst_log=mp.nstr(worst_log, 6),
               same_arm_min=mp.nstr(worst_same, 6), holds=bool(holds), fires=bool(fires),
               q1=q1, q1_why=q1_why, q2=q2, q2_why=q2_why, if_same_fires=q2.startswith('SAME'),
               table=table, row=dict(id='L1', cells=row_cells, quotes=row_quotes), pairs=pairs)
    io.open(os.path.join(D, 'b327_bridge.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(out, indent=1, ensure_ascii=False) + '\n')
    io.open(os.path.join(D, 'b327_bridge_run.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    return 0 if verdict_ok else 1


if __name__ == '__main__':
    sys.exit(main())
