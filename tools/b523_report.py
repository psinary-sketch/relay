# -*- coding: utf-8 -*-
"""b523_report.py -- COMPONENTS 1-5 FROM THE BANKED RUNS. ### `python tools/b523_report.py`
### Every figure read from `b523_sigma.json`, `b523_count.json`, `b523_reread.json`; the verdict by READING (7)`s rule.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DERIV = [
    '(d1) Z_Q0(s) = 2 + SUM_{n>=2} r(n) n^{-s}; on Re s = sigma, |Z - 2| <= eta(sigma) = SUM_{n>=2} r(n) n^{-sigma}.',
    '(d2) r(n) is counted exactly for n <= N0 = 10^6 (b325`s counter); for every n, r(n) <= 2 a(n), a(n) = SUM_{d|n} (d/23),',
    '     because the three reduced forms of disc -23 together represent n exactly 2 a(n) times (checked to 20000; r <= 2a to N0).',
    '(d3) so eta(sigma) <= SUM_{2<=n<=N0} r(n) n^{-sigma} + 2 [zeta(sigma) L(sigma, chi) - SUM_{n<=N0} a(n) n^{-sigma}], decreasing in sigma.',
    '(d4) sigma_max is the least sigma (to 1e-3, rounded up) with that bound below 2: Re Z > 0 there and on every line to its right,',
    '(d5) so no zero has real part >= sigma_max, and by Lambda(s) = Lambda(1 - s) none has real part <= 1 - sigma_max.']
COUNTD = [
    '(c1) Lambda(s) = (sqrt23/2pi)^s Gamma(s) Z(s) = Lambda(1-s); xi = s(s-1) Lambda. On the box [1-s1, s1] x [-T, T] the argument',
    '     principle and the two symmetries give N(T) <= (1/pi)[pi + T log(sqrt23/2pi) + Im logGamma(1/2+iT)] + S(T), S = (1/pi) D_L arg Z.',
    '(c2) On Re s = s1 >= sigma_max, Re Z >= 2 - eta(s1) = g0 > 0: that side moves arg Z by less than pi/2.',
    '(c3) On [1/2 + iT, s1 + iT] (Backlund): |D arg Z| <= (m + 1) pi, m the zeros of Re Z(sigma + iT) there; Jensen on the disc of',
    '     radius R = s1 + eta about s1 bounds m <= log(M / g0) / log(R / r), r = s1 - 1/2, M the maximum of |Z| on the circle.',
    '(c4) M from Rademacher`s Phragmen-Lindelof for (s-1) Z(s) between Re s = -eta (functional equation, |Gamma| ratio sup G on a',
    '     grid with Stirling`s remainder beyond) and Re s = 1 + eta (the series): M <= max(A,B) (T+R+2+eta)^{2+2 eta} / (T-R).',
    '(c5) Hence N(T) <= M0(T) + E(T), M0 = (T/pi) log(T sqrt23 / 2 pi e) + 1, E printed; Stirling`s |M_exact - M0| checked on a grid.']


def load(n):
    return json.loads(io.open(os.path.join(D, n), encoding='utf-8').read())


def main():
    sg, ct, rr = load('b523_sigma.json'), load('b523_count.json'), load('b523_reread.json')
    rows = rr['rows']
    neg = [r for r in rows if r['neg522']]
    pp = ct['params']
    res = dict(sigma_max=sg['sigma_max'], control=sg['control'], E150=ct['E150'], stirling_ok=ct['stirling_ok'],
               controls_ok=all(c['inside'] and c['shifted_outside'] for c in ct['controls']),
               neg522=len(rr['neg522']), neg_sigma=len(rr['neg_sigma']), neg_full=len(rr['neg_full']), survivors=rr['survivors'],
               narrowest=(min(rr['survivors']) if rr['survivors'] else None),
               sigma_cost=len(rr['neg522']) - len(rr['neg_sigma']), s_cost=len(rr['neg_sigma']) - len(rr['neg_full']),
               in_reach_full=[r['a'] for r in rows if r['in_reach_full']])
    L = ['=' * 132, 'b523 -- THE WITNESS`S THREE CAVEATS PRICED.', '=' * 132,
         '### COMPONENT 1 -- sigma_max = %.3f. ### the derivation in five lines:' % sg['sigma_max']] + ['    ' + x for x in DERIV] + [
         '  eta(sigma_max) = %.6f (exact part to N0 %.6f + tail bound %.3e) ; eta at sigma_max - 0.01 : %.6f'
         % (sg['eta_at'], sg['head'], sg['tail_bound'], sg['eta_below']),
         '  eta at 1.2 / 1.5 / 2.0 / 2.5 : %.4f / %.4f / %.4f / %.4f' % (sg['eta_1.2'], sg['eta_1.5'], sg['eta_2.0'], sg['eta_2.5']),
         '  three forms sum to 2 a(n) to %s ; r(n) <= 2 a(n) to N0 : %s' % (sg['forms_equal_2a_to'], sg['r_le_2a_to_N0']),
         '  ### positive control: the bank`s largest real part %.4f lies below sigma_max : %s' % (sg['bank_max_real_part'], sg['control']),
         '', '### COMPONENT 2 -- THE TAIL WITH REAL PART UP TO sigma_max (s_max = %.3f), b521`s closed form otherwise unchanged:' % rr['s_max'],
         '  %-4s %-11s %-11s %-11s %-11s %-11s %-9s %s' % ('a', 'h2', 'tail old', 'tail sigma', 'B sigma', 'B`', 'neg522', 'neg sigma')]
    for r in rows:
        L.append('  %-4.0f %+.4e %-11.3e %-11.3e %-11.3e %-11.3e %-9s %s' % (r['a'], r['h2'], r['tail_old'], r['tail_sigma'], r['B_sigma'], r['Bprime'],
                                                                         r['neg522'], r['neg_sigma']))
    L += ['  ### negative beyond bound under the sigma re-pricing : %d of b522`s %d ; narrowest %s'
          % (len(rr['neg_sigma']), len(rr['neg522']), min(rr['neg_sigma']) if rr['neg_sigma'] else 'NONE'),
          '', '### COMPONENT 3 -- S(t) BOUNDED ABOVE 150. ### No citation: Z_Q0 is not an L-function (no Euler product; it is 2/3 of',
          '### zeta_K + L(psi) + L(psi-bar)), so a Backlund bound for one degree-two L-function does not bound its zeros; the crude bound',
          '### is proved here from the argument principle on the box:'] + ['    ' + x for x in COUNTD] + [
          '  constants: eta %.1f ; sigma1 %.3f ; R %.3f ; r %.3f ; A %.4g ; B %.4g ; G %.6f ; g0 %.4f ; e1 = (1+2 eta)/log(R/r) = %.4f'
          % (pp['eta'], pp['sigma1'], pp['R'], pp['r'], pp['A'], pp['B'], pp['G'], pp['g0'], pp['e1']),
          '  ### E(150) = %.3f ; E(10^4) = %.3f ; Stirling |M_exact - M0| max %.2e within pad %.2f : %s'
          % (ct['E150'], ct['E1e4'], ct['stirling_max_diff'], ct['stirling_pad'], ct['stirling_ok'])]
    for c in ct['controls']:
        L.append('  control T=%-6.1f : N_bank %d, M_exact %.3f, E %.2f -- inside %s ; the count shifted by ceil(E)+1 outside %s'
                 % (c['T'], c['n_bank'], c['M_exact'], c['E'], c['inside'], c['shifted_outside']))
    L += ['  %-4s %-11s %-11s %-11s %-9s %s' % ('a', 'tail full', 'B full', 'margin', 'neg full', 'IN reach (R131)(2) under full')]
    for r in rows:
        L.append('  %-4.0f %-11.3e %-11.3e %+.4e %-9s %s' % (r['a'], r['tail_full'], r['B_full'], r['margin_full'], r['neg_full'], r['in_reach_full']))
    # ### b523`s defect: READING (4) required this line and the first form of the report did not print it.
    tail_led = [r['a'] for r in rows if not r['in_reach_full']]
    res['tail_led_full'] = tail_led
    L += ['  ### READING (4): under the full tail %d of %d cells are OUT of (R131)(2)`s reach (tail above B`) -- their verification is the'
          % (len(tail_led), len(rows)),
          '  ### tail majorant`s, VERIFIED-EST-TAIL in (R130)(1)`s words; the sign is decided beyond that bound, not the quadrature`s.',
          '  ### negative beyond the full bound : %d ; narrowest %s' % (len(rr['neg_full']), min(rr['neg_full']) if rr['neg_full'] else 'NONE'),
          '', '### COMPONENT 4 -- THE u > 1200 SHORTFALL AGAINST THE MARGIN, AT b522`S NEGATIVE CELLS:']
    for r in neg:
        L.append('  a=%-3.0f shortfall ESTIMATE %.3e ; margin under the full bound %+.4e ; ratio %s'
                 % (r['a'], r['shortfall'], r['margin_full'], ('%.2e' % r['shortfall_over_margin']) if r['shortfall_over_margin'] is not None else 'NO MARGIN'))
    rat = [r['shortfall_over_margin'] for r in neg if r['shortfall_over_margin'] is not None]
    res['shortfall_ratio_max'] = max(rat) if rat else None
    L.append('  ### largest shortfall / margin : %s' % res['shortfall_ratio_max'])
    n = len(rr['survivors'])
    verdict = ('MET IN SUBSTANCE BY THE NUMBERS: %d of b522`s %d negative cells survive all three re-pricings, VERIFIED-EST under the '
               'full bound, the narrowest at a = %s' % (n, len(rr['neg522']), res['narrowest'])) if n else (
               'NOT MET: none of b522`s %d negative cells survives all three re-pricings' % len(rr['neg522']))
    res['verdict'] = verdict
    L += ['', '### COMPONENT 5 -- THE READING.',
          '  ### SURVIVING ALL THREE : %d of %d ; narrowest %s' % (n, len(rr['neg522']), res['narrowest'] or 'NONE'),
          '  ### (R118)(1)`S BAR, BY THE COUNT ALONE (READING (7)): ' + verdict + '.',
          '  ### The navigator`s ruling follows at the next paste; the seat lifts nothing and adds no sentence to step (9).',
          '  ### Standing on: the strip now [1 - sigma_max, sigma_max] (proved, C1); S(t) bounded (proved, with G and Stirling`s pad',
          '  ### checked numerically on grids, C3); the shortfall an ESTIMATE, printed against each margin (C4). Not a statement about RH.',
          '=' * 132]
    io.open(os.path.join(D, 'b523_report.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b523_results.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main())
