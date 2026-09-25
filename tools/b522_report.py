# -*- coding: utf-8 -*-
"""b522_report.py -- COMPONENTS 0-3 FROM THE BANKED RUN. ### `python tools/b522_report.py`
### Every figure recomputed from `b522_reach.json` and `b522_cells.jsonl`; xi CITED from `b520_results.json`; the reading
### is (R127)(2)'s words. ### A missing cell file is read as no cell (b521`s defect (b), carried).
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

WIT = 'the witness construction h2_sign_imp_rh names, exhibited at one rho and for that rho alone'
HARD = 'no Q0 cell is negative beyond its bound on a closing bank: the two-property window is not yet the witness'


def load(n):
    return json.loads(io.open(os.path.join(D, n), encoding='utf-8').read())


def sign(v, B):
    return '+' if v > B else ('-' if v < -B else '?')


def main():
    re_ = load('b522_reach.json')
    b20 = load('b520_' + 'results.json')
    cp_ = os.path.join(D, 'b522_cells.jsonl')
    cs = sorted((json.loads(l) for l in io.open(cp_, encoding='utf-8') if l.strip()), key=lambda c: c['a']) if os.path.exists(cp_) else []
    res = dict(p=re_['p'], within=re_['within'], outside=re_['outside'])
    L = ['=' * 132, 'b522 -- VARIANT (B) AT p = %d, THE REACH READ PER WIDTH.' % re_['p'], '=' * 132,
         '### COMPONENT 0 -- THE REACH TABLE (R131)(2): IN iff E_tail <= B` = E_u + E_k + E_round at that width, a^2 within LAMQ (n to %d).' % re_['lamq_top'],
         '  %-5s %-11s %-11s %-10s %s' % ('a', 'E_tail', 'B`', 'tail/B`', 'reach')]
    for r in re_['table']:
        L.append('  %-5.0f %-11.3e %-11.3e %-10.3e %s' % (r['a'], r['Etail'], r['Bprime'], r['tail_over_Bprime'], 'IN' if r['within'] else 'OUT'))
    L.append('  ### WITHIN REACH : %d of %d ; OUT at : %s' % (len(re_['within']), len(re_['table']), re_['outside'] or 'NONE'))
    L += ['', '### COMPONENT 1 -- Q0, VARIANT (B) AT p = %d, gamma_0 = 16.290216, EVERY WIDTH WITHIN REACH. ### VERIFIED-EST iff |r| <= B ;'
          ' nv: none, closed-form transform ; shortfall an ESTIMATE outside B.' % re_['p'],
          '  %-5s %-13s %-2s %-9s %-9s %-6s %-4s %-13s %-13s %-13s %-13s %-8s %-8s %-8s' %
          ('a', 'P - PR + A', 's', '|r|', 'B', 'tail%', 'VER', 'pair', 'others', 'on-line', 'pair / rest', 'G', 'e^dL', 'G/e^dL')]
    for c in cs:
        L.append('  %-5.0f %+.6e %-2s %-9.2e %-9.2e %-6.3f %-4s %+.6e %+.6e %+.6e %+.6e %-8.4f %-8.4f %-8.4f'
                 % (c['a'], c['h2'], sign(c['h2'], c['B']), abs(c['r']), c['B'], c['tail_share'], 'YES' if c['verified'] else 'no',
                    c['pair'], c['others'], c['on_rest'], c['ratio'] or 0.0, c['growth'], c['growth_bound'], c['growth_fraction']))
    ver = [c for c in cs if c['verified']]
    neg = [c for c in ver if c['h2'] < -c['B']]
    cross = [c for c in cs if c['ratio'] is not None and c['ratio'] <= -1.0]
    Q = res['q'] = dict(cells=len(cs), verified=len(ver), h2_neg=[c['a'] for c in neg], h2_pos=[c['a'] for c in ver if c['h2'] > c['B']],
                        h2_undecided=[c['a'] for c in ver if abs(c['h2']) <= c['B']],
                        narrowest=(neg[0]['a'] if neg else None), growth_at_narrowest=(neg[0]['growth'] if neg else None),
                        growth_bound_at_narrowest=(neg[0]['growth_bound'] if neg else None),
                        cross_minus_one=(cross[0]['a'] if cross else None),
                        growth_fraction_at_cross=(cross[0]['growth_fraction'] if cross else None),
                        widest_a=(cs[-1]['a'] if cs else None), widest_ratio=(cs[-1]['ratio'] if cs else None),
                        ratio_min=(min(c['ratio'] for c in cs) if cs else None), tail_share_max=(max(c['tail_share'] for c in cs) if cs else None),
                        shortfall_over_B=[c['a'] for c in cs if c['shortfall'] > c['B']])
    L += ['  ### VERIFIED-EST %d of %d read ; negative beyond B : %s ; positive %d ; undecided %s'
          % (Q['verified'], Q['cells'], Q['h2_neg'] or 'NONE', len(Q['h2_pos']), Q['h2_undecided'] or 'NONE'),
          '  ### the narrowest width negative beyond bound : %s' % (Q['narrowest'] or 'NONE'),
          '  ### the pair`s ratio reaches -1 first at : %s (G / e^dL there %s) ; most negative ratio read %s ; at the widest cell read (a = %s) %s'
          % (Q['cross_minus_one'] or 'NONE', Q['growth_fraction_at_cross'], Q['ratio_min'], Q['widest_a'], Q['widest_ratio']),
          '  ### the tail`s share of B, largest over the cells read : %s ; shortfall ESTIMATE above B at : %s'
          % (Q['tail_share_max'], Q['shortfall_over_B'] or 'NONE')]
    x = b20['xi']
    res['xi_cited'] = dict(cells=x['cells'], verified=x['verified'], positive=len(x['h2_pos']))
    L += ['', '### COMPONENT 2 -- XI, CITED FROM b520 (not recomputed): VERIFIED-EST %d of %d, positive %d.' % (x['verified'], x['cells'], len(x['h2_pos']))]
    if Q['h2_neg']:
        reading = ('a Q0 cell is negative beyond its bound on a closing bank (narrowest a = %s, realized growth %.6g there against (d)`s %.6g, '
                   '(f)`s numerical target): %s' % (Q['narrowest'], Q['growth_at_narrowest'], Q['growth_bound_at_narrowest'], WIT))
    elif Q['widest_a'] is not None:
        reading = HARD + '; the ratio of the pair`s term to the rest at the widest cell read (a = %s) is %+.6e' % (Q['widest_a'], Q['widest_ratio'])
    else:
        reading = HARD + '; no Q0 cell was read -- no width of a = 15..60 was within reach'
    res['reading'] = reading
    L += ['', '### COMPONENT 3 -- THE READING, IN (R127)(2)`S WORDS:', '    ' + reading, '    ### Nothing is claimed of the kernel either way.', '=' * 132]
    io.open(os.path.join(D, 'b522_report.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b522_results.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main())
