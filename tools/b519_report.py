# -*- coding: utf-8 -*-
"""b519_report.py -- COMPONENTS 1-3 FROM THE BANKED CELLS, PER VARIANT. ### `python tools/b519_report.py`
### Every count recomputed from `b519_cells_{A,B,C}.jsonl`; the scoring is READING (9)'s; the reading per variant is (R127)(2)'s
### words; the witness at Q0 is any variant with a VERIFIED-EST Q0 cell negative beyond its bound, or NONE.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
VARIANTS = ('A', 'B', 'C')
NAMES = dict(A='NOTCHED', B='EDGE-WEIGHTED', C='BOTH')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

WIT = 'the witness construction h2_sign_imp_rh names, exhibited at one rho and for that rho alone'
HARD = 'no Q0 cell is negative beyond its bound on a closing bank: the two-property window is not yet the witness'


def sign(v, B):
    return '+' if v > B else ('-' if v < -B else '?')


def cells_of(v):
    return sorted((json.loads(l) for l in io.open(os.path.join(D, 'b519_cells_%s.jsonl' % v), encoding='utf-8') if l.strip()),
                  key=lambda c: c['a'])


def main():
    res = {}
    L = ['=' * 132, 'b519 -- THREE VARIANTS OF THE TWO-PROPERTY WINDOW: Q0 AT 16.290216 AND XI AT 14.1347 ACROSS THE LADDER.', '=' * 132]
    for v in VARIANTS:
        cells = cells_of(v)
        res[v] = {}
        for obj, title in (('q', 'Q0'), ('xi', 'XI')):
            L += ['', '### (%s) %s -- %s. ### VERIFIED-EST iff |r| <= B ; signs decided beyond B ; the shortfall an ESTIMATE outside B.'
                  % (v, NAMES[v], title),
                  '  %-10s %-13s %-2s %-9s %-9s %-4s %-13s %-13s %-13s %-13s %-9s %-9s' %
                  ('a', 'P - PR + A', 's', '|r|', 'B', 'VER', 'pair', 'others', 'on-line', 'pair / rest', 'G', 'G/e^dL')]
            for c in cells:
                x = c[obj]
                L.append('  %-10.6f %+.6e %-2s %-9.2e %-9.2e %-4s %+.6e %+.6e %+.6e %+.6e %-9.4f %-9.4f'
                         % (c['a'], x['h2'], sign(x['h2'], x['B']), abs(x['r']), x['B'], 'YES' if x['verified'] else 'no',
                            x['pair'], x['others'], x['on_rest'], x['ratio'] or 0.0, x['growth'], x['growth_fraction']))
            ver = [c for c in cells if c[obj]['verified']]
            neg = [c for c in ver if c[obj]['h2'] < -c[obj]['B']]
            nar = min(neg, key=lambda c: c['a']) if neg else None
            R = res[v][obj] = dict(
                cells=len(cells), verified=len(ver), h2_neg=[c['a'] for c in neg], h2_pos=[c['a'] for c in ver if c[obj]['h2'] > c[obj]['B']],
                h2_undecided=[c['a'] for c in ver if abs(c[obj]['h2']) <= c[obj]['B']],
                narrowest=nar['a'] if nar else None, growth_at_narrowest=nar[obj]['growth'] if nar else None,
                growth_k_at_narrowest=nar[obj]['growth_k'] if nar else None,
                pair_neg=[c['a'] for c in cells if c[obj]['pair'] < 0], pair_pos=[c['a'] for c in cells if c[obj]['pair'] > 0],
                ratio_min=min(c[obj]['ratio'] for c in cells), ratio_max=max(c[obj]['ratio'] for c in cells),
                widest_a=cells[-1]['a'], widest_ratio=cells[-1][obj]['ratio'], widest_growth=cells[-1][obj]['growth'],
                widest_growth_fraction=cells[-1][obj]['growth_fraction'],
                shortfall_over_B=[c['a'] for c in cells if c[obj]['shortfall'] > c[obj]['B']], pair_kind=cells[0][obj]['pair_kind'])
            L += ['  ### VERIFIED-EST %d of %d ; P - PR + A negative beyond B : %s ; positive %d ; undecided %s'
                  % (R['verified'], R['cells'], R['h2_neg'] or 'NONE', len(R['h2_pos']), R['h2_undecided'] or 'NONE'),
                  '  ### the narrowest such width : %s ; the realized growth G there : %s (k`s: %s)'
                  % (R['narrowest'], R['growth_at_narrowest'], R['growth_k_at_narrowest']),
                  '  ### the pair (%s) negative at %d, positive at %d ; pair / rest from %+.3e to %+.3e ; at the widest cell (a = %.6f) %+.6e'
                  % (R['pair_kind'], len(R['pair_neg']), len(R['pair_pos']), R['ratio_min'], R['ratio_max'], R['widest_a'], R['widest_ratio']),
                  '  ### shortfall ESTIMATE above B at : %s' % (R['shortfall_over_B'] or 'NONE')]
        q = res[v]['q']
        if q['h2_neg']:
            q['reading'] = ('a Q0 cell is negative beyond its bound on a closing bank (narrowest a = %s, realized growth %.6g there): %s'
                            % (q['narrowest'], q['growth_at_narrowest'], WIT))
        else:
            q['reading'] = HARD + '; the ratio of the pair`s term to the rest at the widest cell (a = %.6f) is %+.6e' % (q['widest_a'], q['widest_ratio'])
    wit = [v for v in VARIANTS if res[v]['q']['h2_neg']]
    res['witness'] = wit
    L += ['', '### COMPONENT 3 -- THE READING PER VARIANT, IN (R127)(2)`S WORDS:']
    L += ['    (%s) %s : %s' % (v, NAMES[v], res[v]['q']['reading']) for v in VARIANTS]
    L += ['    ### THE WITNESS AT Q0 : %s' % (', '.join('(%s) %s' % (v, NAMES[v]) for v in wit) if wit else 'NONE'),
          '    ### Nothing is claimed of the kernel either way.', '=' * 132]
    io.open(os.path.join(D, 'b519_report.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b519_results.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print(NL.join(L[-8:]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
