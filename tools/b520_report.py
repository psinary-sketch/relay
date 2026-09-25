# -*- coding: utf-8 -*-
"""b520_report.py -- COMPONENTS 1-3 FROM THE BANKED CELLS. ### `python tools/b520_report.py`
### Every count recomputed from `b520_cells.jsonl` and `b520_reach.json`; the reading is (R127)(2)'s words.
"""
import io
import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
DELTA = 0.9532604747946607 - 0.5
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

WIT = 'the witness construction h2_sign_imp_rh names, exhibited at one rho and for that rho alone'
HARD = 'no Q0 cell is negative beyond its bound on a closing bank: the two-property window is not yet the witness'


def sign(v, B):
    return '+' if v > B else ('-' if v < -B else '?')


def main():
    reach = json.loads(io.open(os.path.join(D, 'b520_reach.json'), encoding='utf-8').read())
    rows = sorted((json.loads(l) for l in io.open(os.path.join(D, 'b520_cells.jsonl'), encoding='utf-8') if l.strip()), key=lambda c: c['a'])
    res = dict(reach=reach['reach'], stop=reach['stop'], lamq_top=reach['lamq_top'])
    L = ['=' * 132, 'b520 -- VARIANT (B) WIDENED PAST THE LADDER: a = 15 TO 60 WITHIN REACH.', '=' * 132,
         '### COMPONENT 0 -- THE REACH: Q0 %s (stopped at %s) ; xi %s (stopped at %s) ; LAMQ to n = %d.'
         % (reach['reach']['q'], reach['stop']['q'], reach['reach']['xi'], reach['stop']['xi'], reach['lamq_top'])]
    for a, n in sorted(reach['named'].items(), key=lambda kv: float(kv[0])):
        for o in ('q', 'xi'):
            if n.get(o):
                L.append('  a=%s %-3s E_tail %.3e against B` %.3e -- %s ; shortfall ESTIMATE %.2e'
                         % (a, o, n[o]['Etail'], n[o]['Bprime'], 'within' if n[o]['Etail'] <= n[o]['Bprime'] else 'BEYOND', n[o]['shortfall']))
            else:
                L.append('  a=%s %-3s NOT READ (past its reach)' % (a, o))
    for obj, title in (('q', 'COMPONENT 1 -- Q0'), ('xi', 'COMPONENT 2 -- XI')):
        cs = [c for c in rows if obj in c]
        L += ['', '### %s. ### VERIFIED-EST iff |r| <= B ; nv: none, closed-form transform ; the shortfall an ESTIMATE outside B.' % title,
              '  %-6s %-13s %-2s %-9s %-9s %-4s %-13s %-13s %-13s %-13s %-8s %-8s %-8s' %
              ('a', 'P - PR + A', 's', '|r|', 'B', 'VER', 'pair', 'others', 'on-line', 'pair / rest', 'G', 'e^dL', 'G/e^dL')]
        for c in cs:
            x = c[obj]
            L.append('  %-6.1f %+.6e %-2s %-9.2e %-9.2e %-4s %+.6e %+.6e %+.6e %+.6e %-8.4f %-8.4f %-8.4f'
                     % (c['a'], x['h2'], sign(x['h2'], x['B']), abs(x['r']), x['B'], 'YES' if x['verified'] else 'no', x['pair'], x['others'],
                        x['on_rest'], x['ratio'] or 0.0, x['growth'], x['growth_bound'], x['growth_fraction']))
        ver = [c for c in cs if c[obj]['verified']]
        neg = [c for c in ver if c[obj]['h2'] < -c[obj]['B']]
        cross = [c for c in cs if c[obj]['ratio'] is not None and c[obj]['ratio'] <= -1.0]
        R = res[obj] = dict(
            cells=len(cs), verified=len(ver), h2_neg=[c['a'] for c in neg], h2_pos=[c['a'] for c in ver if c[obj]['h2'] > c[obj]['B']],
            h2_undecided=[c['a'] for c in ver if abs(c[obj]['h2']) <= c[obj]['B']],
            narrowest=(min(neg, key=lambda c: c['a'])['a'] if neg else None),
            growth_at_narrowest=(min(neg, key=lambda c: c['a'])[obj]['growth'] if neg else None),
            growth_bound_at_narrowest=(min(neg, key=lambda c: c['a'])[obj]['growth_bound'] if neg else None),
            cross_minus_one=(min(cross, key=lambda c: c['a'])['a'] if cross else None),
            growth_fraction_at_cross=(min(cross, key=lambda c: c['a'])[obj]['growth_fraction'] if cross else None),
            pair_neg=[c['a'] for c in cs if c[obj]['pair'] < 0],
            widest_a=(cs[-1]['a'] if cs else None), widest_ratio=(cs[-1][obj]['ratio'] if cs else None),
            shortfall_over_B=[c['a'] for c in cs if c[obj]['shortfall'] > c[obj]['B']])
        L += ['  ### VERIFIED-EST %d of %d read ; P - PR + A negative beyond B : %s ; positive %d ; undecided %s'
              % (R['verified'], R['cells'], R['h2_neg'] or 'NONE', len(R['h2_pos']), R['h2_undecided'] or 'NONE'),
              '  ### the narrowest negative width : %s ; realized growth there %s of (d)`s %s' % (R['narrowest'], R['growth_at_narrowest'], R['growth_bound_at_narrowest']),
              '  ### the pair`s ratio to the rest reaches -1 first at : %s (realized fraction there %s) ; at the widest cell read (a = %s) %s'
              % (R['cross_minus_one'], R['growth_fraction_at_cross'], R['widest_a'], R['widest_ratio']),
              '  ### shortfall ESTIMATE above B at : %s' % (R['shortfall_over_B'] or 'NONE')]
    q = res['q']
    if q['h2_neg']:
        reading = ('a Q0 cell is negative beyond its bound on a closing bank (narrowest a = %s, realized growth %.6g there against (d)`s %.6g, '
                   '(f)`s numerical target): %s' % (q['narrowest'], q['growth_at_narrowest'], q['growth_bound_at_narrowest'], WIT))
    elif q['widest_a'] is not None:
        reading = HARD + '; the ratio of the pair`s term to the rest at the widest cell read (a = %s) is %+.6e' % (q['widest_a'], q['widest_ratio'])
    else:
        # ### b520`s own defect: the registered reach rule could leave Q0 with no cell read, and the first form of this line
        # ### assumed a widest cell -- it crashed on the run. ### (R127)(2)`s words, with the reason no ratio is printed.
        st = reach['stop']['q'] or {}
        reading = (HARD + '; no Q0 cell was read -- the instrument`s reach ended at a = %s, the tail bound %.3g times the rest of the '
                   'cell`s bound -- so no ratio at a widest cell is printed' % (st.get('a'), st.get('tail_over_Bprime', float('nan'))))
    res['reading'] = reading
    L += ['', '### COMPONENT 3 -- THE READING, IN (R127)(2)`S WORDS:', '    ' + reading, '    ### Nothing is claimed of the kernel either way.', '=' * 132]
    io.open(os.path.join(D, 'b520_report.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b520_results.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print(NL.join(L[:12] + L[-6:]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
