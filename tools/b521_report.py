# -*- coding: utf-8 -*-
"""b521_report.py -- COMPONENTS 0-3 FROM THE BANKED RUNS. ### `python tools/b521_report.py`
### Every figure recomputed from `b521_order.json`, `b521_fixture.json`, `b521_validity.json`, `b521_compare.json`,
### `b521_reach.json`, `b521_cells.jsonl`; xi CITED from `b520_results.json`; the reading is (R127)(2)'s words.
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
VALIDITY = [
    '(v1) For t >= T = 150 and |s| <= 1/2, |sinc(x + iy)| <= cosh(y) min(1, 1/|x|) bounds each factor of phi-hat(t -+ gamma_0 - is).',
    '(v2) |t - gamma_0| >= t (1 - gamma_0/T) and |t + gamma_0| >= t, so the pair of shifted factors is at most mu_q t^-q, q the power.',
    '(v3) |gamma_0^2 - (t - is)^2| <= gamma_0^2 + t^2 + s^2 <= kappa_s t^2; hence |k-hat| <= c1^2 t^2 below t2 and c2^2 t^(2-2p) above.',
    '(v4) The bound is increasing in |s|, so s = 1/2 covers every zero with real part in [0, 1]: on-line (s = 0) plus the off-line excess.',
    '(v5) Integrated against 2 x (1/pi) log(t sqrt 23 / 2 pi) dt, the RvM main term, in closed form; S(t)`s remainder is NAMED, NOT BOUNDED.']


def load(n):
    return json.loads(io.open(os.path.join(D, n), encoding='utf-8').read())


def sign(v, B):
    return '+' if v > B else ('-' if v < -B else '?')


def main():
    od, fx, va, cp, re_ = (load(n) for n in ('b521_order.json', 'b521_fixture.json', 'b521_validity.json', 'b521_compare.json', 'b521_reach.json'))
    b20 = load('b520_results.json')
    # ### b521`s defect: the pass writes no cell file when the reach ends at the first width, and the first form of this
    # ### line assumed the file -- it crashed on the run (b520`s no-cell species, one line earlier). ### No file = no cell.
    cp_ = os.path.join(D, 'b521_cells.jsonl')
    cs = sorted((json.loads(l) for l in io.open(cp_, encoding='utf-8') if l.strip()), key=lambda c: c['a']) if os.path.exists(cp_) else []
    p = od['least_p']
    res = dict(least_p=p)
    L = ['=' * 132, 'b521 -- Q0`S TAIL TIGHTENED, THEN THE WIDTH PASS RE-RUN.', '=' * 132,
         '### COMPONENT 0 -- THE SMOOTHNESS ORDER. ### the new tail (closed form) against B` and the pair`s term, per p and width:',
         '  %-3s %-5s %-11s %-11s %-11s %-12s %s' % ('p', 'a', 'new tail', 'B`', 'old maj.', 'pair', 'tail < B`')]
    for r in od['rows']:
        L.append('  %-3d %-5.0f %-11.3e %-11.3e %-11.3e %+.4e %s' % (r['p'], r['a'], r['Etail'], r['Bprime'], r['Etail_old'], r['pair'], 'YES' if r['Etail'] < r['Bprime'] else 'no'))
    L.append('  ### THE LEAST p WITH THE NEW TAIL BELOW B` AT a = 60 : %s (scanned %s to %s, stopping two orders past it)' % (p, od['rows'][0]['p'], od['rows'][-1]['p']))
    L.append('  ### classK restated at p = %s: h = (gamma_0^2 + D^2)(cos(gamma_0 u) phi), phi the plateau with inner order-p B-spline, is' % p)
    L.append('      even, compactly supported on [-L, L], and C^(p-3) -- C^2 needs p >= 5 -- so k = weilTest h h (k = h * h) is in classK.')
    L.append('  ### the rebuilt window`s (R125)(2) fixture at a = 5 (p = %s): bar met at every u %s ; largest diff/bar %.3f ; %d nodes'
             % (fx['p'], fx['meets'], max(r['diff'] / r['bar'] for r in fx['rows']), fx['nodes']))
    for x in fx['integration']:
        L.append('  ### closed form against its own integrand integrated numerically, a=%.0f s=%.1f : %.4e vs %.4e (rel %.1e)' % (x['a'], x['s'], x['closed'], x['numeric'], x['rel']))
    res['fixture_meets'] = fx['meets']
    res['integration_rel_max'] = max(x['rel'] for x in fx['integration'])
    L += ['', '### COMPONENT 1 -- THE NEW TAIL. ### the validity argument in five lines:'] + ['    ' + v for v in VALIDITY]
    L.append('  ### STRIP ASSUMPTION: every zero of Z_Q0 above 150 has real part in [0, 1]; a zero outside it is not covered. (R130)(2).')
    L.append('  ### the validity fixture (a synthetic zero at height 200; the allowance at s = 1/2):')
    for r in va['rows']:
        L.append('    a=%-4.0f real part %.1f : largest image term %.3e ; allowance %.3e ; covered %s (must %s) -- %s'
                 % (r['a'], r['beta'], max(r['terms']), r['allowance'], r['covered'], r['must_cover'], 'OK' if r['ok'] else 'FAILS'))
    res['validity_ok'] = all(r['ok'] for r in va['rows'])
    L.append('  ### compared with b519`s banked old majorant (p = 5) at its %d widths: at p = %s smaller at %d ; not smaller at %s'
             % (cp['of'], cp['p'], cp['smaller'], cp['not_smaller'] or 'NONE'))
    L.append('  ### at p = 5 (the closed form alone, same window) smaller at %d of %d' % (cp['p5_smaller'], cp['of']))
    for r in cp['rows'][::20] + cp['rows'][-1:]:
        L.append('    a=%-10.6f old %.3e ; new %.3e (on %.3e, off %.3e) ; new at p=5 %.3e' % (r['a'], r['old'], r['new'], r['new_on'], r['new_off'], r['new_p5']))
    res['compare_smaller'], res['compare_of'], res['p5_smaller'] = cp['smaller'], cp['of'], cp['p5_smaller']
    L += ['', '### COMPONENT 2 -- THE REACH (b520`s rule: E_tail against B` = E_u + E_k + E_round, and a^2 within LAMQ), at p = %s:' % p,
          '  reach %s ; stop %s' % (re_['reach'], (re_['stop'] or {}).get('a'))]
    for s in re_['scan']:
        L.append('  a=%-4.0f E_tail %.3e ; B` %.3e ; ratio %.2e ; lamq %s' % (s['a'], s['Etail'], s['Bprime'], s['tail_over_Bprime'], s['lamq_ok']))
    L += ['', '### Q0, VARIANT (B) AT p = %s. ### VERIFIED-EST iff |r| <= B ; nv: none, closed-form transform ; shortfall an ESTIMATE outside B.' % p,
          '  %-6s %-13s %-2s %-9s %-9s %-4s %-13s %-13s %-13s %-13s %-8s %-8s %-8s' %
          ('a', 'P - PR + A', 's', '|r|', 'B', 'VER', 'pair', 'others', 'on-line', 'pair / rest', 'G', 'e^dL', 'G/e^dL')]
    for c in cs:
        L.append('  %-6.1f %+.6e %-2s %-9.2e %-9.2e %-4s %+.6e %+.6e %+.6e %+.6e %-8.4f %-8.4f %-8.4f'
                 % (c['a'], c['h2'], sign(c['h2'], c['B']), abs(c['r']), c['B'], 'YES' if c['verified'] else 'no', c['pair'], c['others'],
                    c['on_rest'], c['ratio'] or 0.0, c['growth'], c['growth_bound'], c['growth_fraction']))
    ver = [c for c in cs if c['verified']]
    neg = [c for c in ver if c['h2'] < -c['B']]
    cross = [c for c in cs if c['ratio'] is not None and c['ratio'] <= -1.0]
    Q = res['q'] = dict(cells=len(cs), verified=len(ver), h2_neg=[c['a'] for c in neg], h2_pos=[c['a'] for c in ver if c['h2'] > c['B']],
                        h2_undecided=[c['a'] for c in ver if abs(c['h2']) <= c['B']],
                        narrowest=(neg[0]['a'] if neg else None), growth_at_narrowest=(neg[0]['growth'] if neg else None),
                        growth_bound_at_narrowest=(neg[0]['growth_bound'] if neg else None),
                        cross_minus_one=(cross[0]['a'] if cross else None), widest_a=(cs[-1]['a'] if cs else None),
                        widest_ratio=(cs[-1]['ratio'] if cs else None), shortfall_over_B=[c['a'] for c in cs if c['shortfall'] > c['B']],
                        reach=re_['reach'])
    L += ['  ### VERIFIED-EST %d of %d read ; negative beyond B : %s ; positive %d ; undecided %s'
          % (Q['verified'], Q['cells'], Q['h2_neg'] or 'NONE', len(Q['h2_pos']), Q['h2_undecided'] or 'NONE'),
          '  ### the narrowest negative width : %s ; the pair`s ratio reaches -1 first at : %s ; at the widest cell read (a = %s) %s'
          % (Q['narrowest'] or 'NONE', Q['cross_minus_one'] or 'NONE', Q['widest_a'], Q['widest_ratio']),
          '  ### shortfall ESTIMATE above B at : %s' % (Q['shortfall_over_B'] or 'NONE')]
    x = b20['xi']
    res['xi_cited'] = dict(cells=x['cells'], verified=x['verified'], positive=len(x['h2_pos']))
    L += ['', '### COMPONENT 3 -- XI, CITED FROM b520 (not recomputed): VERIFIED-EST %d of %d, positive %d.' % (x['verified'], x['cells'], len(x['h2_pos']))]
    if Q['h2_neg']:
        reading = ('a Q0 cell is negative beyond its bound on a closing bank (narrowest a = %s, realized growth %.6g there against (d)`s %.6g, '
                   '(f)`s numerical target): %s' % (Q['narrowest'], Q['growth_at_narrowest'], Q['growth_bound_at_narrowest'], WIT))
    elif Q['widest_a'] is not None:
        reading = HARD + '; the ratio of the pair`s term to the rest at the widest cell read (a = %s) is %+.6e' % (Q['widest_a'], Q['widest_ratio'])
    else:
        st = re_['stop'] or {}
        reading = (HARD + '; no Q0 cell was read -- the reach ended at a = %s, the tail bound %.3g times the rest of the cell`s bound'
                   % (st.get('a'), st.get('tail_over_Bprime', float('nan'))))
    res['reading'] = reading
    L += ['### THE READING, IN (R127)(2)`S WORDS:', '    ' + reading, '    ### Nothing is claimed of the kernel either way.', '=' * 132]
    io.open(os.path.join(D, 'b521_report.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b521_results.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main())
