# -*- coding: utf-8 -*-
"""b526_report.py -- COMPONENTS 0-3 FROM THE BANKS. ### `python tools/b526_report.py`
### Component 1 recomputed from `b526_xi7_cells.jsonl`; Component 2`s halt from `b526_bump.json`; Component 3`s form of words
### re-derived from Component 1 alone, Component 2 having read nothing.
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


def load(n):
    return json.loads(io.open(os.path.join(D, n), encoding='utf-8').read())


def sign(v, B):
    return '+' if v > B else ('-' if v < -B else '?')


def main():
    nt, bp = load('b526_notes.json'), load('b526_bump.json')
    cs = sorted((json.loads(l) for l in io.open(os.path.join(D, 'b526_xi7_cells.jsonl'), encoding='utf-8') if l.strip()), key=lambda c: c['a'])
    L = ['=' * 132, 'b526 -- XI AT ORDER 7, AND BOTH OBJECTS ON THE KERNEL`S OWN phi.', '=' * 132,
         '### COMPONENT 0 -- (R136)(1)`S SENTENCE APPENDED: ' + ' ; '.join('%s prefix proved %s' % (w['file'], w.get('prefix')) for w in nt['writes']),
         '    the sentence, quoted from the ferry: ' + nt['sentence'], '',
         '### COMPONENT 1 -- XI, VARIANT (B) AT RAMP ORDER 7, gamma_0 = 14.1347, a = 15..60, the reach per width (IN iff E_tail <= B`).',
         '  %-5s %-13s %-2s %-9s %-9s %-4s %-3s %-9s %-13s %-13s %-8s %-8s' % ('a', 'P - PR + A', 's', '|r|', 'B', 'VER', 'IN', 'tail/B`',
                                                                         'pair', 'pair / rest', 'G', 'G/e^dL')]
    for c in cs:
        L.append('  %-5.0f %+.6e %-2s %-9.2e %-9.2e %-4s %-3s %-9.1e %+.6e %+.6e %-8.4f %-8.4f'
                 % (c['a'], c['h2'], sign(c['h2'], c['B']), abs(c['r']), c['B'], 'YES' if c['verified'] else 'no', 'IN' if c['within'] else 'OUT',
                    c['Etail'] / c['Bprime'], c['pair'], c['ratio'] or 0.0, c['growth'], c['growth_fraction']))
    inn = [c for c in cs if c['within']]
    ver = [c for c in inn if c['verified']]
    pos = [c['a'] for c in ver if c['h2'] > c['B']]
    neg = [c['a'] for c in ver if c['h2'] < -c['B']]
    und = [c['a'] for c in ver if abs(c['h2']) <= c['B']]
    X = dict(cells=len(cs), within=len(inn), verified=len(ver), positive=pos, negative=neg, undecided=und,
             tail_over_bprime_max=max(c['Etail'] / c['Bprime'] for c in cs) if cs else None,
             shortfall_over_B=[c['a'] for c in cs if c['shortfall'] > c['B']])
    L += ['  ### widths computed %d ; IN %d ; VERIFIED-EST among IN %d ; positive beyond bound %d ; negative %s ; undecided %s'
          % (X['cells'], X['within'], X['verified'], len(pos), neg or 'NONE', und or 'NONE'),
          '  ### tail / B` largest %.2e -- xi`s cells are VERIFIED-EST, not tail-led ; shortfall ESTIMATE above B at %s'
          % (X['tail_over_bprime_max'] or 0, X['shortfall_over_B'] or 'NONE'), '',
          '### COMPONENT 2 -- HALTED: the kernel`s phi has no values to evaluate.']
    for q in bp['quotes']:
        L.append('    %s : %s' % (q['file'], ['line %d: %s' % (n, t.strip()) for n, t in q['hits']]))
    L += ['    kernel : %s' % bp['kernel_lines'],
          '    ### someContDiffBumpBase E := Nonempty.some hb.out, HasContDiffBump a Prop: the base is Classical.choice`s, fixed by no definition;',
          '    ### the kernel`s plateau is determined by the properties it proves and by nothing else.',
          '    ### positive control -- two bases pass every field (R = %.4f): %s ; A = smoothTransition((R-|x|)/(R-1)), B = smoothTransition twice ;'
          % (bp['R'], bp['both_pass']),
          '    ###   they differ by up to %.4f pointwise (x = %.3f of rIn), and in what the window would cite at a = 34: %s'
          % (bp['max_pointwise_diff'], bp['at_x'], {k: {'phi-hat(gamma_0)': round(v['at_gamma0'], 6), 'G': round(v['growth'], 6)} for k, v in bp['transforms'].items()}),
          '    ### negative control -- a candidate with support to 2, not R, rejected by the same checks: %s' % bp['bad_rejected'],
          '    ### Q0 and xi on the kernel`s phi: NOT READ ; the crossing and its G: NOT READ.', '']
    all_pos = bool(ver) and len(pos) == len(ver) == len(cs)
    form = ('"positive for xi at every verified width to 60 at ramp order 7, the order at which the Epstein control is negative from 34; '
            'xi VERIFIED-EST, the control VERIFIED-EST-TAIL; two constants of the count numerical; both on the order-7 B-spline window, '
            'not on the kernel`s instance, whose values the kernel leaves to a choice"') if all_pos else None
    X['form'] = form
    X['instance_reading'] = ('the order-7 B-spline window is the one instance the corpus may cite numbers on for the pair xi/Q0; the '
                             'kernel`s theorems cover it (every C^4 compactly supported phi), and the kernel`s named instance is not a '
                             'specific function, so no number is citable "on the kernel`s phi" until the kernel names one')
    L += ['### COMPONENT 3 -- THE FORM OF WORDS, RE-DERIVED FROM COMPONENT 1 (COMPONENT 2 READ NOTHING):',
          '    ' + (form or 'NOT RE-DERIVED: xi at order 7 is not positive at every verified width to 60 -- the (R134) form stands'),
          '    ### the seat`s reading of the instance: ' + X['instance_reading'], '=' * 132]
    io.open(os.path.join(D, 'b526_report.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b526_results.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(X, indent=1, ensure_ascii=False) + NL)
    print(NL.join(L[-14:]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
