# -*- coding: utf-8 -*-
"""b515_report.py -- COMPONENTS 1-3 FROM THE BANKED CELLS. ### `python tools/b515_report.py`
### Every count recomputed from `b515_cells.jsonl`; the scoring is READING (9)'s; the reading is (R122)(2)'s words, with (d)'s
### growth factor exp(2 delta L) banked beside the narrowest negative width when there is one.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
UPPER = 60                  # ### READING (9): the ladder's upper half is its 59 widest widths, index 60 to 118
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

WIT = 'the window is the witness construction h2_sign_imp_rh names, exhibited at one rho'
HARD = 'no Q0 cell is negative on a closing bank'


def sign(v, B):
    return '+' if v > B else ('-' if v < -B else '?')


def main():
    cells = sorted((json.loads(l) for l in io.open(os.path.join(D, 'b515_cells.jsonl'), encoding='utf-8') if l.strip()),
                   key=lambda c: c['a'])
    upper = set(round(c['a'], 9) for c in cells[UPPER:])
    res = {}
    L = ['=' * 132, 'b515 -- THE WINDOW WITH A ZERO AT THE ON-LINE POINT: Q0 AT 16.290216 AND XI AT 14.1347 ACROSS THE LADDER.', '=' * 132]
    for obj, title in (('q', 'COMPONENT 1 -- Q0'), ('xi', 'COMPONENT 2 -- XI')):
        L += ['', '### %s. ### VERIFIED-EST iff |r| <= B ; signs decided beyond B ; the u > 1200 shortfall an ESTIMATE outside B.' % title,
              '  %-10s %-13s %-2s %-13s %-2s %-9s %-9s %-4s %-13s %-13s %-13s %-13s %-9s' %
              ('a', 'm = A - PR', 's', 'P - PR + A', 's', '|r|', 'B', 'VER', 'pair', 'others', 'on-line', 'pair / rest', 'shortfall')]
        for c in cells:
            x = c[obj]
            L.append('  %-10.6f %+.6e %-2s %+.6e %-2s %-9.2e %-9.2e %-4s %+.6e %+.6e %+.6e %+.6e %-9.2e'
                     % (c['a'], x['m'], sign(x['m'], x['B']), x['h2'], sign(x['h2'], x['B']), abs(x['r']), x['B'],
                        'YES' if x['verified'] else 'no', x['pair'], x['others'], x['on_rest'], x['ratio'] or 0.0, x['shortfall']))
        ver = [c for c in cells if c[obj]['verified']]
        neg = [c for c in ver if c[obj]['h2'] < -c[obj]['B']]
        R = res[obj] = dict(
            cells=len(cells), verified=len(ver),
            m_neg=[c['a'] for c in ver if c[obj]['m'] < -c[obj]['B']], m_pos=[c['a'] for c in ver if c[obj]['m'] > c[obj]['B']],
            h2_pos=[c['a'] for c in ver if c[obj]['h2'] > c[obj]['B']], h2_neg=[c['a'] for c in neg],
            h2_undecided=[c['a'] for c in ver if abs(c[obj]['h2']) <= c[obj]['B']],
            h2_neg_upper=[c['a'] for c in neg if round(c['a'], 9) in upper],
            narrowest=min((c['a'] for c in neg), default=None),
            growth_at_narrowest=min(neg, key=lambda c: c['a'])[obj]['growth'] if neg else None,
            pair_neg=[c['a'] for c in cells if c[obj]['pair'] < 0], pair_pos=[c['a'] for c in cells if c[obj]['pair'] > 0],
            ratio_min=min(c[obj]['ratio'] for c in cells), ratio_max=max(c[obj]['ratio'] for c in cells),
            shortfall_over_B=[c['a'] for c in cells if c[obj]['shortfall'] > c[obj]['B']],
            pair_kind=cells[0][obj]['pair_kind'])
        L += ['  ### VERIFIED-EST %d of %d ; margin negative (decided) %s ; positive %d' % (R['verified'], R['cells'], R['m_neg'] or 'NONE', len(R['m_pos'])),
              '  ### P - PR + A negative beyond B (verified) : %s ; positive %d ; undecided %s' % (R['h2_neg'] or 'NONE', len(R['h2_pos']), R['h2_undecided'] or 'NONE'),
              '  ### the narrowest such width : %s ; (d)`s growth factor exp(2 delta L) there : %s' % (R['narrowest'], R['growth_at_narrowest']),
              '  ### the pair (%s) negative at %d cells, positive at %d ; pair / rest from %+.3e to %+.3e' %
              (R['pair_kind'], len(R['pair_neg']), len(R['pair_pos']), R['ratio_min'], R['ratio_max']),
              '  ### cells whose u > 1200 shortfall ESTIMATE exceeds B : %s' % (R['shortfall_over_B'] or 'NONE')]
    q = res['q']
    if q['h2_neg']:
        reading = ('a Q0 cell is negative on a closing bank (narrowest a = %s, exp(2 delta L) = %.6g there): %s' % (q['narrowest'], q['growth_at_narrowest'], WIT))
    else:
        reading = HARD + ': the witness construction h2_sign_imp_rh names is not exhibited at this rho by this window'
    res['reading'] = reading
    L += ['', '### COMPONENT 3 -- THE READING, IN (R122)(2)`S WORDS:', '    ' + reading,
          '    ### Nothing is claimed of the kernel either way.', '=' * 132]
    io.open(os.path.join(D, 'b515_report.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b515_results.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print(NL.join(L[-16:]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
