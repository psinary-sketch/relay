# -*- coding: utf-8 -*-
"""b514_report.py -- COMPONENTS 1-3 FROM THE BANKED CELLS. ### `python tools/b514_report.py`
### Every count recomputed from `b514_cells.jsonl`; the scoring is READING (9)'s; the reading is (R122)(2)'s words and no others.
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

WIT = ('the window is the witness construction h2_sign_imp_rh names, exhibited at one rho')
HARD = ('the converse`s construction is harder than a modulated bump')


def sign(v, B):
    return '+' if v > B else ('-' if v < -B else '?')


def main():
    cells = sorted((json.loads(l) for l in io.open(os.path.join(D, 'b514_cells.jsonl'), encoding='utf-8') if l.strip()),
                   key=lambda c: c['a'])
    res = {}
    L = ['=' * 124, 'b514 -- THE MATCHED WINDOW: Q0 AT 16.290216 AND XI AT 14.1347 ACROSS THE LADDER`S WIDTHS.', '=' * 124]
    for obj, title in (('q', 'COMPONENT 1 -- Q0'), ('xi', 'COMPONENT 2 -- XI')):
        L += ['', '### %s. ### VERIFIED-EST iff |r| <= B ; signs decided beyond B ; the u > 1200 shortfall an ESTIMATE outside B.' % title,
              '  %-10s %-13s %-2s %-13s %-2s %-10s %-10s %-4s %-13s %-13s %-13s %-9s %-10s' %
              ('a', 'm = A - PR', 's', 'P - PR + A', 's', '|r|', 'B', 'VER', 'pair', 'others', 'on-line', 'share', 'shortfall')]
        for c in cells:
            x = c[obj]
            L.append('  %-10.6f %+.6e %-2s %+.6e %-2s %-10.2e %-10.2e %-4s %+.6e %+.6e %+.6e %-9.4f %-10.2e'
                     % (c['a'], x['m'], sign(x['m'], x['B']), x['h2'], sign(x['h2'], x['B']), abs(x['r']), x['B'],
                        'YES' if x['verified'] else 'no', x['pair'], x['others'], x['on_rest'], x['share'] or 0.0, x['shortfall']))
        ver = [c for c in cells if c[obj]['verified']]
        res[obj] = dict(
            cells=len(cells), verified=len(ver),
            m_neg=[c['a'] for c in ver if c[obj]['m'] < -c[obj]['B']],
            m_pos=[c['a'] for c in ver if c[obj]['m'] > c[obj]['B']],
            m_undecided=[c['a'] for c in ver if abs(c[obj]['m']) <= c[obj]['B']],
            h2_neg=[c['a'] for c in ver if c[obj]['h2'] < -c[obj]['B']],
            h2_undecided=[c['a'] for c in ver if abs(c[obj]['h2']) <= c[obj]['B']],
            pair_neg=[c['a'] for c in cells if c[obj]['pair'] < 0],
            share_max=max((c[obj]['share'] for c in ver), default=None),
            share_max_a=max(ver, key=lambda c: c[obj]['share'])['a'] if ver else None,
            share_over_half=[c['a'] for c in ver if c[obj]['share'] > 0.5],
            shortfall_over_B=[c['a'] for c in cells if c[obj]['shortfall'] > c[obj]['B']],
            pair_kind=cells[0][obj]['pair_kind'] if cells else None)
        R = res[obj]
        L += ['  ### VERIFIED-EST %d of %d ; margin negative (decided) %s ; positive %d ; undecided %s' %
              (R['verified'], R['cells'], R['m_neg'] or 'NONE', len(R['m_pos']), R['m_undecided'] or 'NONE'),
              '  ### P - PR + A negative (decided, verified) : %s ; undecided %s' % (R['h2_neg'] or 'NONE', R['h2_undecided'] or 'NONE'),
              '  ### the pair (%s) negative at : %s ; share max %.4f at a = %s ; share above 0.50 at : %s' %
              (R['pair_kind'], R['pair_neg'] or 'NONE', R['share_max'] or 0.0, R['share_max_a'], R['share_over_half'] or 'NONE'),
              '  ### cells whose u > 1200 shortfall ESTIMATE exceeds B : %s' % (R['shortfall_over_B'] or 'NONE')]
    neg = res['q']['h2_neg']
    reading = ('a Q0 cell is negative on a closing bank (a = %s): %s' % (neg, WIT)) if neg else ('no Q0 cell is negative on a closing bank: ' + HARD)
    res['reading'] = reading
    L += ['', '### COMPONENT 3 -- THE READING, IN (R122)(2)`S WORDS AND NO OTHERS:', '    ' + reading,
          '    ### Nothing is claimed of the kernel either way.', '=' * 124]
    io.open(os.path.join(D, 'b514_report.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b514_results.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print(NL.join(L[-12:]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
