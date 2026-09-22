# -*- coding: utf-8 -*-
"""b476_components.py -- THE EXPERIMENT AS REGISTERED. ### Run after the seal
### (sha256 `73d547bbc4a9fe5a...`). ### It PRINTS what the locked face registers, from the survey bank.
### ### **NO GRAM ENTRY IS COMPUTED HERE; NO LANE IS OPENED; NOTHING IS RE-MEASURED.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


S = json.loads(io.open(os.path.join(D, 'b476_survey.json'), encoding='utf-8').read())


def main():
    rec('=' * 104)
    rec('b476 -- THE COMPRESSION EXPERIMENT, AS REGISTERED. ### NOTHING COMPUTED BEYOND THE REHEARSAL.')
    rec('=' * 104)

    rec('')
    rec('  ### (1) THE FAMILY, CELL BY CELL, FROM THE BANKS.')
    rec('    %-9s %-8s %-18s %-12s %-30s' % ('a', 'banked', 'W = PR - A', 'p^k <= a', 'p^k <= a^2 (the form`s)'))
    for r in S['family']:
        rec('    %-9g %-8s %-18s %-12s %-30s'
            % (r['a'], 'YES' if r['W'] is not None else 'no',
               ('%.9f' % r['W']) if r['W'] is not None else '-',
               ','.join(str(x) for x in r['seed_primes']) or '-',
               ','.join(str(x) for x in r['form_primes']) or '-'))
    rec('    ### the aim-plane cells : %d, of which %d carry a banked W'
        % (len(S['cells']), len(S['above'])))
    rec('    ### the radius ladder   : %d cells, %g to %g, SAME construction, radii shared with the'
        % (len(S['ladder']), S['ladder'][0], S['ladder'][-1]))
    rec('    ###   aim plane : %s' % (S['overlap'] or 'NONE'))
    rec('    ### ### **ONE CONSTRUCTION, TWO DISJOINT RADIUS SETS.**')

    rec('')
    rec('  ### (2) THE GRAM ENTRY, AND (3) THE DIAGONAL CONTROL.')
    rh = S['rehearsal']
    rec('    the construction, named: g_a = SM.mean_zero_variant(a) ; f = SQ.autocorrelation(g) ;')
    rec('      ch = WI.channels(f.v, f.w) -- b321_run.py:139-141 and :242-245, for BOTH families.')
    rec('    G(a,b) = that same four-channel chain at f_ab = g_a conv gbar_b^# ; the chain is NOT')
    rec('      edited and f_ab is supplied to it, under (R86).')
    rec('    ### THE DIAGONAL CONTROL, REHEARSED AT a = %g BEFORE THE LOCK:' % rh['a'])
    rec('      G(a,a)          = %.12f' % rh['diag'])
    rec('      b321`s banked W = %.12f' % rh['banked'])
    rec('      ### ### **|DIFFERENCE| = %.3e ; THE FLOOR = %.2e ; WITHIN IT : %s**'
        % (rh['delta'], rh['floor'], rh['within']))
    rec('      ### A mismatch beyond the floor halts the run before any off-diagonal entry.')

    rec('')
    rec('  ### (4) THE TRUNCATION, AS THE INSTRUMENT`S.')
    rec('    banked ordinates : %d, to T = %.6f' % (S['truncation']['ordinates'], S['truncation']['T']))
    rec('    ### the truncated Gram is at most the true Gram in the Loewner order under RH -- the order`s')
    rec('    ### own statement, registered and not proved. ### **A NEGATIVE EIGENVALUE REFUTES NOTHING')
    rec('    ### ABOUT ZEROS BY ITSELF; ITS SIZE AGAINST THE TAIL BOUND IS WHAT IS READ.**')

    rec('')
    rec('  ### (5) THE CONTROL, AND THE TWO RECORD CHECKS THE ORDER`S OWN WORDS NEEDED.')
    c = S['control']
    rec('    the census : sigma in [%s, %s], t to T = %s ; located off-line zeros : %d'
        % (c['sig'][0], c['sig'][1], c['census_T'], len(c['heights'])))
    rec('    heights : %s' % ', '.join('%g' % h for h in c['heights']))
    rec('    ### ### **THE ORDER`S "t about 176.70" IS IN NO BANK THIS ACT READ, AND IT IS ABOVE THE')
    rec('    ### CENSUS`S OWN CEILING T = %s. ### THE CONTROL`S ZERO IS THE RECORD`S LOWEST, t = %g.**'
        % (c['census_T'], c['lowest']))
    r = S['resolution']
    rec('    the resolving size, PRICED by the rule %s :' % r['rule'])
    rec('      ### ### **CELLS THAT RESOLVE t = %g : %d OF %d ; THE SMALLEST RADIUS : %g**'
        % (r['t'], r['resolving'], len(r['rows']), r['smallest']))
    rec('      the weakest cell of the thirty-five : %s'
        % min(('a = %g, |hhat| = %.3e' % (x['a'], x['hhat']) for x in r['rows']),
              key=lambda s: float(s.split('= ')[-1])))
    rec('      ### ### **SO THE RESOLVING FAMILY SIZE IS ONE CELL.** ### If the instrument can see a')
    rec('      ### hyperbolic plane at all, it should see it at the smallest family the run forms.')

    rec('')
    rec('  ### (6) THE FALSIFIERS, AS THE ORDER FIXED THEM.')
    rec('    (F1) UNINFORMATIVE -- no negative index at the control`s resolving family: the instrument')
    rec('         cannot see a hyperbolic plane, and NOTHING IS SAID ABOUT ZETA.')
    rec('    (F2) HALT -- zeta`s negative eigenvalue beyond the tail bound: the chain or the record is')
    rec('         wrong somewhere; the act says so and stops, with NO CLAIM ABOUT RH EITHER WAY.')
    rec('    (F3) MEASURED -- zeta above minus the tail bound at every size to the reach while the')
    rec('         control goes indefinite at the priced size: the register is MEASURED at that reach,')
    rec('         ### **AND NO HIGHER GRADE.**')

    rec('')
    rec('  ### (7) THE PRICE, FROM THE REHEARSAL`S OWN TIMING.')
    p = S['price']
    rec('    one chain run : %.2f s' % p['seconds_per_run'])
    for label, n, e in (('the aim-plane cells', len(S['cells']), p['aim']),
                        ('the ladder cells', len(S['ladder']), p['ladder']),
                        ('both families', len(S['cells']) + len(S['ladder']), p['both'])):
        rec('    %-22s n = %-4d entries %-5d -> %6.0f s (%.1f min)'
            % (label, n, e, e * p['seconds_per_run'], e * p['seconds_per_run'] / 60.0))
    rec('    ### ### **EVERY OPTION EXCEEDS THE 600 s FOREGROUND LIMIT, SO UNDER (R86) THE RUN IS')
    rec('    ### DETACHED UNDER (R80), NAMED AND LOGGED, AND READ BY THE ACT AFTER ITS PID EXITS.**')
    rec('    ### The lane is opened by (R86) for b477 and closes at b477`s end. ### **IT IS NOT OPEN NOW.**')

    rec('')
    rec('=' * 104)
    rec('  ### ### **REGISTERED, LOCKED, AND NOT RUN. ### NO GRAM ENTRY EXISTS. ### h2 STANDS WHERE THE')
    rec('  ### DEPOSIT LEFT IT.**')
    rec('=' * 104)
    io.open(os.path.join(D, 'b476_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(family=S['family'], cells=S['cells'], ladder=S['ladder'], rehearsal=rh,
                   truncation=S['truncation'], control=c, resolution=r, price=p,
                   lane_open=False, gram_entries=0),
              io.open(os.path.join(D, 'b476_registered.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
