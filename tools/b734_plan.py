# -*- coding: utf-8 -*-
"""b734_plan.py -- (R344)(3): THE explicitFormula FIELD'S PLAN BANK, WRITTEN FROM THE DEPENDENCY PRINT, NO BUILD AND NO LEAN FILE.

Every row is one Epstein lemma the field wants, its Prop, the (b) constants of data/b734_ef_print.json it answers (every (b) constant answered once, the control), the nearest compiled neighbour
read from the tree at zq-b730 09053d3b by name (line and span read, not typed), and the seat's own price in lines. The measured ratios are read through standing.pricebank from data/b731_price_measured.txt
and, for count, from the tree and b733's dispatch rows; nothing there is typed.

  python -X utf8 -u tools/b734_plan.py plan [--bank]
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'standing'))
import dispatchrows as DR  # noqa: E402
import pricebank as PB  # noqa: E402

K = 'D:/SIDE-explicit-formula'
SHA = '09053d3b07367aa7ef2e26cbeb27fd35d8734d82'
BANK = 'data/b734_explicitformula_plan.txt'
PRINT = 'data/b734_ef_print.json'
CHI = 'SIDEExplicitFormula/Chi/%s.lean'
ZQ = 'SIDEExplicitFormula/Schema/ZQ/%s.lean'
WEIL = 'Zeta23/WeilEF/%s.lean'
SC = 'SIDEExplicitFormula/Schema/EpsteinZQ.lean'
CHAIN = ('Contour', 'FullLine', 'Horizontal', 'Landau', 'GoodHeights', 'FullLineAssembly', 'ZeroSumLimit', 'ZeroSummability', 'VerticalLine', 'XiLogDeriv', 'GammaWide', 'Main')

W = 'Zeta23.WeilEF.'
GAMMA_MODULES = ('Zeta23.DigammaSeries.', 'Zeta23.StirlingVert.')
# ### (id, group, seat's lines, title, Prop, (neighbour path, name), the (b) constants answered, the library members answered)
ROWS = [
    ('E0', None, 0, 'the statement, compiled', 'ZQExplicitFormula zqZeroConfig (fun n => cQ n), its terms zeroSideQ, poleTerm, primeTermQ, archTermQ, bracketQ, each compiled at Schema/EpsteinZQ.lean and Schema/ZQ/Zeros.lean; the zeros are zqZeroConfig, supplied.',
     (SC, 'ZQExplicitFormula'), ('Zeta23.EF.EF_lit', 'Zeta23.EF.literatureRHS', 'Zeta23.EF.literatureRHS.eq_1', 'Zeta23.EF.gammaBracket', 'Zeta23.zetaZeros'), ()),
    ('E1', None, 0, 'the digamma facts, the constant itself', 'NO ANALOGUE IS WANTED: the Gamma of Q0`s completed function is the Gamma of these statements. Each constant is used as it stands, by import, at s in place of s/2; the only reach Q0 asks is 1/2 <= Re s <= 3/2, and digamma_growth_strip_wide (1/4 <= Re s <= 2) already compiles it.',
     (CHI % 'GammaWide', 'digamma_growth_strip_wide'), 'GAMMA', ()),
    ('E2', 'A', 60, 'the completed function and its logarithmic derivative', 'for s with 0 < Re s, s <> 1, zqFn s <> 0: logDeriv lamQ s = -log qBase + digamma s + logDeriv zqFn s, where lamQ s := qBase^(-s) * Gamma s * zqFn s, equal to zqPair.Lambda by mul_zqFn_eq. The conductor term is the constant -log qBase = log(sqrt23/2pi).',
     (CHI % 'XiLogDeriv', 'logDeriv_completedLFunction'), (W + 'analyticAt_Gammaℝ', W + 'differentiableAt_Gammaℝ', W + 'completedZeta_eventuallyEq_mul', W + 'logDeriv_Gammaℝ', W + 'logDeriv_completedZeta'), ('Complex.Gammaℝ', 'Complex.Gammaℝ_def', 'Gammaℝ', 'Gammaℝ_def', 'Gammaℝ_ne_zero_of_re_pos', 'completedRiemannZeta', 'riemannZeta')),
    ('E3', 'A', 35, 'the reflection of the logarithmic derivative', 'for s <> 0, s <> 1, lamQ s <> 0: logDeriv lamQ (1 - s) = -logDeriv lamQ s, from zqPair_Λ_one_sub. Q0 is self-dual: no dual function and no root number.',
     (WEIL % 'XiLogDeriv', 'logDeriv_completedZeta_one_sub'), (W + 'logDeriv_completedZeta_one_sub',), ()),
    ('E4', 'A', 45, 'the zeros of the completed function', 'for -1/2 < Re s < 3/2, s <> 0, s <> 1: lamQ s = 0 <-> s in zqZeroConfig.carrier, its order at s being zqZeroConfig.mult s by zq_order_eq_Lam; and lamQ s <> 0 on a horizontal free of the carrier.',
     (CHI % 'XiLogDeriv', 'completedLFunction_zeros_strip'), (W + 'completedZeta_zeros_strip', W + 'completedZeta_ne_zero_on_horizontals', 'Zeta23.IsNontrivialZero.eq_1'), ()),
    ('E5', 'B', 170, 'Landau`s partial fraction at zqFn', 'exists C > 0, for all t with 6 <= |t|, exists a finite Z, Z = the zeros of zqFn in closedBall (2 + it) (22/25 * 91/50), the sum of their orders <= C log(|t| + 3), and for s in closedBall (2 + it) (3/2) with zqFn s <> 0, |logDeriv zqFn s - sum m_rho / (s - rho)| <= C log(|t| + 3). The disk lemma is the compiled logDeriv_partial_fraction_disk; the lower bound at the centre is zq_norm_ge at Re = 2, the upper bound aE_growth over |1 - s| >= 4.',
     (CHI % 'Landau', 'LFunction_logDeriv_partial_fraction'), (W + 'zeta_logDeriv_partial_fraction',), ()),
    ('E6', 'C', 340, 'the good heights, over the wide windows', 'exists Cg > 0, exists R : Nat -> Real, for all j, j + 7 <= R j <= j + 8, and on Im s = +-R j, 1/2 <= Re s <= 2: zqFn s <> 0 and |logDeriv zqFn s| <= Cg log(j + 10)^2. With it the window lemmas of Wide.N that the ZeroConfig class has and WideConfig has not, the 18 members of (d) marked TAKES-ZeroConfig read for what the chain uses.',
     (CHI % 'GoodHeights', 'good_heights_chi'), (W + 'good_heights', W + 'good_heights_at', W + 'sum_mult_six_windows', W + 'card_le_sum_mult', W + 'isNontrivialZero_of_mem_closedBall'), ()),
    ('E7', 'D', 200, 'the rectangle identity, two poles', 'for 1 < c <= 3/2, 7 <= R, lamQ <> 0 on the horizontals: exists Z, Z = the carrier with |Im| < R, and RectangleIntegral` (Hfn k * logDeriv lamQ) ((1 - c) - iR) (c + iR) = sum_Z m_rho Hfn k rho - Hfn k 0 - Hfn k 1. The poles are zeta`s, not chi`s: chi`s rectangle has none, so this row`s neighbour is the zeta module.',
     (WEIL % 'Contour', 'rectangle_identity'), (W + 'rectangle_identity',), ()),
    ('E8', 'D', 200, 'the horizontals vanish', 'at the heights of E6, for 1 < c <= 3/2: HIntegral (Hfn k * logDeriv lamQ) (1 - c) c (+-R j) -> 0; the left half of the side by E3.',
     (CHI % 'Horizontal', 'horizontal_vanish_chi'), (W + 'horizontal_vanish',), ()),
    ('E9', 'E', 95, 'the zero sum converges, wide', 'for Z : WideConfig with Wide.HCount Z A0, k in C_c^2: Summable (fun rho => (Z.mult rho) * paperFT k (gammaOf rho)). The compiled proof takes |Im gamma| < 1/2; the wide strip gives |Im gamma| < 1, so the exponential is e^Lambda and not e^(Lambda/2), over zero_sum_inv_sq_wide, compiled.',
     (WEIL % 'ZeroSummability', 'EF_zero_sum_summable_gen'), (W + 'EF_zero_sum_summable',), ()),
    ('E10', 'E', 90, 'the zero sum`s limit', 'the sums over |Im rho| < R j of m_rho Hfn k rho tend to the tsum over zqZeroConfig.carrier.',
     (CHI % 'ZeroSumLimit', 'zero_sum_limit_chi'), (W + 'zero_sum_limit',), ()),
    ('E11', 'F', 220, 'the two lines', 'on Re s = 3/2: logDeriv lamQ splits by E2; logDeriv zqFn is continuous and bounded (the series, cC_summable); the integrands are integrable against Hfn`s decay on -1 <= Re s <= 2 (norm_Hfn_le); the left vertical equals the reflected right by E3.',
     (CHI % 'FullLine', 'verticals_eq_chi'), (W + 'continuous_logDeriv_zeta_line', W + 'continuous_logDeriv_Gammaℝ_line', W + 'integrable_Hfn_mul_logDeriv_zeta', W + 'integrable_Hfn_mul_logDeriv_Gammaℝ', W + 'integrable_mul_logDeriv_zeta_of_decay', W + 'integrable_mul_logDeriv_Gammaℝ_of_decay', W + 'logDeriv_completedZeta_line', W + 'norm_logDeriv_zeta_le_of_one_lt_re', W + 'verticals_eq'), ()),
    ('E12', 'F', 75, 'the full-line identity', '(1/2pi) * integral (Fline_Q k c) = tsum over zqZeroConfig.carrier of m_rho Hfn k rho - Hfn k 0 - Hfn k 1, at c = 3/2.',
     (CHI % 'FullLineAssembly', 'full_line_identity_chi'), (W + 'full_line_identity',), ()),
    ('E13', 'G', 180, 'the prime side on Re s = 3/2', '(1/2pi) * integral Hfn k (3/2 + it) * (-logDeriv zqFn (3/2 + it)) dt = tsum c(n) n^(-1/2) k(log n). Absolute convergence is cC_summable at exactly 3/2 and nowhere left of it, so the contour sits at c = 3/2, not zeta`s and chi`s 5/4. c is real and signed, so zeta`s positivity is no route and chi`s complex coefficients are the template.',
     (CHI % 'VerticalLine', 'prime_side_line_chi'), (W + 'prime_side_line', W + 'integrand_eq_tsum'), ()),
    ('E14', 'G', 170, 'the Gamma line`s shift', 'integral (Hfn k (c + it) + Hfn k (1 - c - it)) * digamma (c + it) dt = integral paperFT k t * (digamma (1/2 + it) + digamma (1/2 - it)) dt at c = 3/2; Gamma has no pole on Re s > 0; growth from digamma_growth_strip_wide; the conductor term by conductor_line_shift, compiled and free of chi, with its right-line twin by vertical_line_shift.',
     (CHI % 'VerticalLine', 'gamma_line_shift_chi'), (W + 'gamma_line_shift', W + 'norm_logDeriv_Gammaℝ_le'), ()),
    ('E15', 'G', 50, 'the bracket', 'for r real: digamma (1/2 + ir) + digamma (1/2 - ir) - 2 log qBase = bracketQ r, by digamma_conj: Gamma`s bracket at Gamma`/Gamma(s), no halving and no 1/4, log(sqrt23/2pi) in place of log pi, the conductor term present.',
     (CHI % 'Main', 'gammaFactor_bracket'), (W + 'gammaR_bracket',), ()),
    ('E16', 'H', 200, 'THE FIELD', 'zq_explicitFormula : ZQExplicitFormula zqZeroConfig (fun n => cQ n): for k in C_c^2 even, zeroSideQ zqZeroConfig k = poleTerm k - primeTermQ cQ k + archTermQ k. Hfn k 1 = paperFT k (-i/2), Hfn k 0 = paperFT k (i/2), so the pole term is b321`s; k even folds k(log n) + k(-log n) into 2 k(log n).',
     (CHI % 'Main', 'EF_lit_chi_holds'), (W + 'EF_lit_zeta',), ()),
]
ORDER = (('A', 'Schema/ZQ/EF/Xi', 'E2 E3 E4', 'none'), ('B', 'Schema/ZQ/EF/Landau', 'E5', 'A'), ('C', 'Schema/ZQ/EF/Heights', 'E6', 'B'), ('D', 'Schema/ZQ/EF/Contour', 'E7 E8', 'A, C'),
         ('E', 'Schema/ZQ/EF/ZeroSum', 'E9 E10', 'A'), ('F', 'Schema/ZQ/EF/FullLine', 'E11 E12', 'D, E'), ('G', 'Schema/ZQ/EF/Lines', 'E13 E14 E15', 'A'), ('H', 'Schema/ZQ/EF/Main', 'E16', 'F, G'))
RISKS = (
    'the right edge has no room: the series and Z_Q`s bounds start at Re s = 3/2 and the carrier is open at 3/2, so c = 3/2 exactly, 1 - c = -1/2; every lemma that took 5/4 or an open margin is restated at the edge. norm_Hfn_le reaches -1 <= Re s <= 2 and conductor_line_shift 1/2 <= c <= 2, so both hold.',
    'the windows: 18 members of (d) carry ZeroConfig and read no zeta word; none applies to WideConfig as it stands. E6 and E9 pay for it and the print`s (d) count is not a count of what imports.',
    'the poles: chi`s chain has none and zeta`s has two, with the self-dual reflection; the template is zeta`s at E3 and E7 and chi`s at the Gamma, the conductor and the signed coefficients. No single file is the neighbour.',
    'the partial fraction`s centre: Re = 2 stays available, zq_norm_ge holding on Re s >= 3/2, so chi`s radii 91/50 and 3/2 transfer. The growth is aE_growth`s |s + 2|^3 over |1 - s|, a polynomial as chi`s is; this is read from statements and not compiled.',
    'multiplicity: Z.mult is the order of Lambda_Q by zq_order_eq_Lam, and the rectangle`s left edge at -1/2 keeps the trivial zero at -1 outside; both read from statements, neither compiled in this use.',
)
RATIO_NAMES = ('continuation', 'logDeriv', 'zeros', 'count')
# ### the compiled names the Props lean on, read from the tree, each a control
LEANS_ON = ((ZQ % 'Continuation', 'mul_zqFn_eq'), (ZQ % 'FEPair', 'zqPair_Λ_one_sub'), (ZQ % 'Zeros', 'zq_order_eq_Lam'), (ZQ % 'Zeros', 'zqZeroConfig'), (ZQ % 'Growth', 'aE_growth'), (ZQ % 'Growth', 'zq_norm_ge'),
            (ZQ % 'LogDeriv', 'cC_summable'), (ZQ % 'LogDeriv', 'zq_logDeriv'), (WEIL % 'Landau', 'logDeriv_partial_fraction_disk'), (WEIL % 'FullLine', 'norm_Hfn_le'), (WEIL % 'VerticalLine', 'vertical_line_shift'),
            (WEIL % 'GammaRBracket', 'digamma_conj'), (CHI % 'Main', 'conductor_line_shift'), ('SIDEExplicitFormula/Schema/Wide/Config.lean', 'zero_sum_inv_sq_wide'))


def git(*a):
    return subprocess.run(['git', '-C', K] + list(a), capture_output=True, text=True, encoding='utf-8').stdout


def tree(path):
    return git('show', SHA + ':' + path).split('\n')


def rd(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
        return f.read()


def locate(path, name):
    """(line, span): the declaration by name in the tree, its span to the next top-level declaration."""
    L = tree(path)
    pat = re.compile(r'^(theorem|def|structure|lemma) +%s\b' % re.escape(name))
    at = [i for i, x in enumerate(L) if pat.match(x)]
    if len(at) != 1:
        return None
    i = at[0]
    j = next((n for n in range(i + 1, len(L)) if re.match(r'^(theorem|def|structure|lemma|/--|end |namespace |section )', L[n])), len(L))
    return i + 1, j - i


def lines_of(path):
    return len(tree(path)) - 1


def est():
    return PB.estimates(rd('data/b729_count_price.txt'))


def controls(pr, rows):
    b = set(pr['b'])
    answered = []
    for r in rows:
        answered += r['b']
    lib = set(x for r in rows for x in r['lib'])
    C = [('every (b) programme constant answered by a row', set(answered) == b),
         ('no (b) constant answered twice', len(answered) == len(set(answered))),
         ('every (b) library member answered', lib == set(pr['b_library'])),
         ('every neighbour found once in the tree, by name', all(r['at'] for r in rows)),
         ('the price bank`s explicitFormula row reads 3000-5000 and 40-80, :24', est().get('explicitFormula') == ((3000, 5000), (40, 80))),
         ('every compiled name the Props lean on found once in the tree (%d)' % len(LEANS_ON), all(locate(p, n) for p, n in LEANS_ON)),
         ('continuation`s ratio reproduces b731`s printed 0.278-0.557', '%.3f-%.3f' % PB.ratio(dict(lines=835, dispatches=6), (1500, 3000), (25, 50))[:2] == '0.278-0.557'),
         ('a planted name is refused by the locator', locate(CHI % 'Main', 'no_such_theorem_b734') is None)]
    return C


def measured():
    """the four measured rows, the first three read from the b731 bank, count from the tree at the pin and b733's dispatch rows."""
    m = PB.measured_rows(rd('data/b731_price_measured.txt'))
    d = json.loads(rd('data/b733_dispatch_rows.json'))
    n = sum(1 for r in d if r['kind'] == 'dispatch')
    m['count'] = est()['count'] + (lines_of(ZQ % 'Growth') + lines_of(ZQ % 'Count'), n)
    return m


def build():
    pr = json.loads(rd(PRINT))
    rows = []
    for (i, g, n, t, p, (path, name), bs, lib) in ROWS:
        if bs == 'GAMMA':
            bs = tuple(x for x in pr['b'] if x.startswith(GAMMA_MODULES) or x in ('harmonic.eq_1', W + 'digamma_conj'))
        rows.append(dict(id=i, group=g, lines=n, title=t, prop=p, path=path, name=name, b=list(bs), lib=list(lib), at=locate(path, name)))
    return pr, rows


def bank():
    pr, rows = build()
    C = controls(pr, rows)
    g = sum(1 for _, ok in C if ok)
    fm = DR.free()
    O = ['b734 -- THE explicitFormula FIELD`S PLAN, (R344)(3): WRITTEN FROM data/b734_ef_print.txt, EACH (b) CONSTANT WITH ITS EPSTEIN ANALOGUE, THE TWO ROUTES PRICED, NOTHING BUILT AND NO LEAN FILE WRITTEN (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### every neighbour read from the tree at zq-b730 09053d3b by name, its line and span by this tool; every (b) constant from the print`s own list; each price in lines the seat`s, a range where it says so, no bound. No lean process on this host. Free memory read before this computation: %d MB at %s.' % fm, '',
         '## THE CONTROLS FIRST'] + ['  %-70s %s' % (w, 'AS WANTED' if ok else 'NOT AS WANTED') for w, ok in C] + ['', '### CONTROLS %d OF %d AS WANTED' % (g, len(C)), '']
    O += ['## THE FIELD', '  Schema/EpsteinZQ.lean :141 ZQPremises.explicitFormula : ZQExplicitFormula Z c, :127 its one clause ef:',
          '    forall k, ContDiff R 2 k -> HasCompactSupport k -> (forall x, k (-x) = k x) -> zeroSideQ Z k = poleTerm k - primeTermQ c k + archTermQ k.',
          '  The theorem aimed at: zq_explicitFormula : ZQExplicitFormula zqZeroConfig (fun n => cQ n), the Z of zq_zeros and the c of zq_logDeriv, on zq-b730 alone. The field is open at this bank; no sentence here calls it closed or the instance DERIVES.', '',
          '## WHAT THE PRINT SETTLES',
          '  The closure is %d programme constants: (a) %d, (b) %d, (d) %d. (c) and the library members of (b) are LEXICAL, %d and %d, read from the closure`s own text; no compiled library closure was printed, so neither figure is a compiled count.' % (len(pr['a']) + len(pr['b']) + len(pr['d']), len(pr['a']), len(pr['b']), len(pr['d']), len(pr['c']), len(pr['b_library'])),
          '  Of the (b) 92, 52 are Gamma facts the ruling names, each standing as it is for Q0 (row E1): the ruling`s list is applied as it stands and the row says what those 52 cost, nothing. %d of the 92 want an analogue, and they fall into %d rows.' % (sum(len(r['b']) for r in rows[2:]), len([r for r in rows if r['lines']])),
          '  THE RULING`S QUESTION, (R344)(3) and (6): ZETA SITS IN THE JOINTS. WeilEF is not a contour chain over four inputs the fields supply: the %d constants above carry zeta or its completed function in their own statements, the partial fraction, the good heights, the rectangle, the horizontals, the two lines, the prime side, the bracket and the main theorem among them, and none is a hypothesis to instantiate. The closed fields answer the chain`s inputs, the continuation, the series, the zeros and the count; the joints are the analogues below. So the field is a build at the price below, not an instantiation, and the instance`s DERIVES is not an act away.' % sum(len(r['b']) for r in rows[2:]),
          '  The nearest compiled neighbour is not WeilEF. The kernel holds a second compiled run of this chain, SIDEExplicitFormula.Chi, EF_lit_chi_holds at Chi/Main.lean :269, whose conductor term (conductor_line_shift, :194), signed coefficients and wide digamma are what Q0 asks; zeta`s poles and self-duality are the rest. No row is reached by Q0 that neither run compiled except the wide windows and the edge c = 3/2.', '']
    m = measured()
    rate = sorted(m[f][2] / m[f][3] for f in RATIO_NAMES)
    O += ['## THE ROWS, EACH (b) CONSTANT WITH ITS ANALOGUE']
    for r in rows:
        nb = 'NOT FOUND' if not r['at'] else '%s :%d %s, %d lines' % (r['path'], r['at'][0], r['name'], r['at'][1])
        O += ['', '  %s  %s' % (r['id'], r['title']), '      Prop       %s' % r['prop'], '      neighbour  %s' % nb,
              '      price      %s' % ('0 lines, 0 dispatches, compiled' if not r['lines'] else '%d lines, the seat`s ; %.1f-%.1f dispatches at the measured rate ; group %s' % (r['lines'], r['lines'] / rate[-1], r['lines'] / rate[0], r['group'])),
              '      answers    %d (b) constants: %s' % (len(r['b']), ', '.join(r['b']))]
        if r['lib']:
            O.append('      and the library members, LEXICAL: %s' % ', '.join(r['lib']))
    fresh = sum(r['lines'] for r in rows)
    O += ['', '## THE MEASURED RATIOS, b730-b733, THE SEAT`S READING OF THEM, NOT A BOUND',
          '  field         est lines   est disp   lines  dispatches  lines per dispatch   the explicitFormula row (3000-5000 lines, 40-80 dispatches, data/b729_count_price.txt :24) re-read by that ratio']
    env = []
    for f in RATIO_NAMES:
        el, ed, n, d = m[f]
        rp = PB.reprice(*(est()['explicitFormula'] + (PB.ratio(dict(lines=n, dispatches=d), el, ed),)))
        env.append(rp)
        O.append('  %-13s %-11s %-10s %-6d %-11d %-20.0f %d-%d lines, %d-%d dispatches' % (f, '%d-%d' % el, '%d-%d' % ed, n, d, n / d, rp[0], rp[1], rp[2], rp[3]))
    lo, hi = min(e[0] for e in env), max(e[1] for e in env)
    dlo, dhi = min(e[2] for e in env), max(e[3] for e in env)
    O += ['  THE ENVELOPE %d-%d lines, %d-%d dispatches; the ratios disagree and that spread is no confidence interval.' % (lo, hi, dlo, dhi)]
    chi = sum(lines_of(CHI % x) for x in CHAIN)
    weil = sum(lines_of(WEIL % x) for x in ('Contour', 'FullLine', 'Horizontal', 'Landau', 'GoodHeights', 'FullLineAssembly', 'ZeroSumLimit', 'ZeroSummability', 'VerticalLine', 'XiLogDeriv', 'GammaRBracket', 'Main'))
    O += ['  THE SECOND RUN, READ FROM THE TREE: Chi`s chain %d lines beside WeilEF`s %d, %.3f. It is the only measured ratio of this chain against itself.' % (chi, weil, chi / weil)]
    d_lo, d_hi = int(fresh / rate[-1]), int(fresh / rate[0]) + 1
    ab1, ab2 = 2350 + 80 + 250, 2350 + 80 + 250 + 300 + 350 + 60
    a_lo, a_hi = int(ab1 / rate[-1]), int(ab2 / rate[0]) + 1
    O += ['', '## THE TWO ROUTES, PRICED SIDE BY SIDE, EACH THE SEAT`S',
          '  FRESH: the rows above, the chain rebuilt for Lambda_Q on chi`s and zeta`s templates, nothing compiled edited. %d lines by the rows, the seat`s range 1,700-2,800; %d-%d dispatches at the measured %.0f-%.0f lines a dispatch, over eight groups.' % (fresh, d_lo, d_hi, rate[0], rate[-1]),
          '  ABSTRACTION: WeilEF generalised over a structure the four fields instantiate. The chain`s proofs are the same proofs over hypotheses, the seat`s 2,350 lines; the structure 80 and the Q0 instance 250, so %d for one consumer, which is the fresh route with the plumbing added and no second user. To earn the structure, zeta and chi must instantiate it as well, the seat`s 300 and 350 and an embedding of ZeroConfig in WideConfig 60, so %d; and chi`s dual function, root number and absent poles make the structure carry what Q0 does not use. %d-%d dispatches by the same rate, and nothing in the ruling names a consumer past Q0.' % (ab1, ab2, a_lo, a_hi),
          '  Both are floors on a specified implementation in I-10`s form, and neither is an estimate of the other.', '',
          '## THE RECOMMENDATION',
          '  THE FRESH ROUTE, at %d lines and %d-%d dispatches. The reason: the abstraction pays for a generality with one consumer left, zeta and chi being compiled and closed; the fresh route is the path the chain has already taken once at %.3f of its length, and it leaves every compiled theorem`s closure as it stands. What would reverse this: a second Epstein instance named for the programme; then the structure has a consumer and the comparison reopens.' % (fresh, d_lo, d_hi, chi / weil), '',
          '## THE ORDER OF BUILD; EACH GROUP ONE DISPATCH READ BY ITS RUN ID, FREE MEMORY READ BEFORE IT AND CARRIED IN EVERY ROW BY standing.dispatchrows',
          '  group | module | rows | lines | after']
    for g_, mod, rs, aft in ORDER:
        O.append('  %s | SIDEExplicitFormula.%s | %s | %d | %s' % (g_, mod.replace('/', '.'), rs, sum(r['lines'] for r in rows if r['group'] == g_), aft))
    O += ['', '## THE STOP POINTS',
          '  after each group, its run read before the next dispatch; a failing group is repaired from its log and re-dispatched, each re-dispatch counted.',
          '  at b733`s rate, 5 dispatches over 3 groups, eight groups are some 13-14 dispatches, so the author may hold the build to one act at a ceiling of 16, or sit it twice, A-D then E-H, at 8 and 8. Both are the author`s to name.',
          '  group B or C fails past repair: the field stops OPEN at the partial fraction or the heights, four of five fields standing, the sorry-free remainder printed.',
          '  group D fails: OPEN at the rectangle, the good heights standing as a result of their own.',
          '  the ceiling spent: OPEN at the lemma reached, the same.',
          '  CLOSED: zq_explicitFormula with its axiom print, the standard three, no sorryAx; five of five fields; only then may a later act state ZQPremises and speak of the instance.', '',
          '## WHERE THE PRICE CAN BREAK, READ FROM STATEMENTS AND NOT COMPILED']
    O += ['  (%d) %s' % (i + 1, x) for i, x in enumerate(RISKS)]
    O += ['', '### ### **THE PLAN: %d ROWS, %d TO BUILD, 2 COMPILED ; EVERY (b) CONSTANT ANSWERED, %d OF %d ; THE FRESH ROUTE RECOMMENDED AT %d LINES, %d-%d DISPATCHES ; ABSTRACTION %d-%d LINES, %d-%d DISPATCHES ; EIGHT GROUPS ; NOTHING BUILT ; CONTROLS %d OF %d.**' % (len(rows), len([r for r in rows if r['lines']]), sum(len(r['b']) for r in rows), len(pr['b']), fresh, d_lo, d_hi, ab1, ab2, a_lo, a_hi, g, len(C))]
    return '\n'.join(O) + '\n', g == len(C)


def main():
    t, ok = bank()
    print(t if '--bank' not in sys.argv else t.rstrip().split('\n')[-1])
    if '--bank' in sys.argv and ok:
        with open(os.path.join(ROOT, BANK), 'w', encoding='utf-8', newline='\n') as f:
            f.write(t)
        print('written', BANK)
    if not ok:
        sys.exit('### THE CONTROLS DID NOT ALL HOLD; NOTHING BANKED')


if __name__ == '__main__':
    main()
