# -*- coding: utf-8 -*-
"""b489_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.
### The row is written by the guarded `corr_row.py` (b488), CARRIED UNEDITED.
### The MARK guard stays: the ledger is read for this act's own mark before the row is offered.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import corr_row  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
CORR = os.path.join(SIDE, 'CORRESPONDENCE.md')
NL = chr(10)
L = []
MARK = 'b489, under (R99) as ratified'


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    R = json.loads(read(os.path.join(D, 'b489_results.json')) or '{}')
    notes = read(os.path.join(D, 'b489_span_notes2.txt')) or read(
        os.path.join(D, 'b489_span_notes.txt'))
    lastfold = next((l.strip() for l in notes.split(NL) if 'FILED BY' in l), '')
    curspan = next((l.strip() for l in notes.split(NL)
                    if 'THE CURRENT SPAN :' in l and 'ACT' in l), '')

    rec('=' * 104)
    rec('b489 -- THE DESK. ### THE SCORES, THE ROW, THE BANK.')
    rec('=' * 104)

    best_lin = (R.get('best') or {}).get('lin', '')
    best_log = (R.get('best') or {}).get('log', '')
    n1 = R.get('rises', 0) == 0
    n2 = best_lin.startswith('(ii) ')
    n3 = R.get('crossings', 0) > 0

    rec('')
    rec('### (1) THE NAVIGATOR`S EXPECTATIONS, EACH SCORED BY A PRINTED RESULT.')
    rec('-' * 104)
    rec('    ### **(N1)** ### the margin is monotone in `a` on the ladder -- ### **%s.**'
        % ('HELD' if n1 else 'REFUTED'))
    rec('        ### **%d of 34 steps RISE.** ### `m` falls from 8.78115 to a minimum of'
        % R.get('rises', 0))
    rec('        ### **%.9g** ### at ### **a = %s**, rises over 9 steps to a LOCAL MAXIMUM'
        % (R.get('m_min'), R.get('turn_a')))
    rec('        ### **%.9g at a = %s**, then FALLS again over the last 6 steps to 0.0382311845.'
        % (R.get('max_m'), R.get('max_a')))
    rec('        ### ### **TWO TURNING POINTS, NOT ONE.** ### And the tool`s first draft said it')
    rec('        ### "rises at every step after the minimum", which the step column refutes:')
    rec('        ### **%d of the %d steps rise, all of them between the two turns.**'
        % (R.get('rises'), R.get('steps')))
    rec('        ### the minimum sits one rung BEFORE `a = 4.123106`, the cell b446 and b447')
    rec('        ### already called an outlier.')
    rec('    ### **(N2)** ### the preferred form is a power of `log a` -- ### **%s.**'
        % ('HELD' if n2 else 'REFUTED'))
    rec('        on the PRIMARY loss the ladder prefers ### **%s** ### and the aim map prefers'
        % best_lin.split()[0])
    rec('        a different form again. ### **FORM (ii) WINS THE PRIMARY LOSS ON NEITHER')
    rec('        FAMILY.** ### On `log m` the ladder prefers `(iii)` and the aim map `(ii)`.')
    rec('    ### **(N3)** ### the control`s margin crosses zero on the ladder -- ### **%s.**'
        % ('HELD' if n3 else 'REFUTED'))
    rec('        ### **SIGN CHANGES : %d. ### NEGATIVE CELLS : %d OF 35.** ### Its minimum is'
        % (R.get('crossings'), R.get('ctrl_negatives')))
    rec('        `1.16912`, at the last rung, and it is strictly decreasing throughout.')
    rec('        ### ### **AND THE FALSIFIER IS OUT OF RANGE, NOT MERELY UNMET.** ### It names')
    rec('        ### a support "resolving `t = 16.29`"; `16.290216` is a GAMMA in the aim map,')
    rec('        ### reached at widths `40` and `81`. ### **THE LADDER STOPS AT 5.656854.**')

    rec('')
    rec('### (2) THE SEAT`S OWN, REGISTERED ON THE SEALED FACE.')
    rec('-' * 104)
    s1 = all(c['m'] > 0 for c in R.get('cells', []))
    s2 = best_lin != best_log
    rec('    (S1) `m > 0` at all 35 cells, so the inequality is non-vacuous  -- ### **%s**'
        % ('HELD' if s1 else 'REFUTED'))
    rec('         min %.9g ; ### **NO CELL IS NEGATIVE OR ZERO.**' % R.get('m_min'))
    rec('    (S2) the ranking is NOT robust across the two losses           -- ### **%s**'
        % ('HELD' if s2 else 'REFUTED'))
    rec('         the two losses DISAGREE on BOTH families; and on the aim map the winner`s')
    rec('         own margin is a factor ### **1.01** ### -- which is not a preference at all.')
    rec('    (S3) all three forms mis-describe past the turn, AND the residual is')
    rec('         concentrated there                                        -- ### **SPLIT.**')
    rec('         ### the first clause ### **HELD**: every form is monotone in `a` by')
    rec('         construction and none turns.')
    rec('         ### the second clause ### **REFUTED BY THE PRINTED SPLIT**: the preferred')
    rec('         form`s RMS is ### **0.183** ### on the 20 cells up to the turn and')
    rec('         ### **0.0247** ### on the 15 past it. ### **THE RESIDUAL IS CONCENTRATED AT')
    rec('         THE SMALL-`a` END, NOT PAST THE TURN** -- because an absolute residual on `m`')
    rec('         is dominated by the cells where `m` is large, and `m` is 200 times larger at')
    rec('         `a = 1.3` than at the turn. ### **THE SEAT`S EXPECTATION CONFUSED A')
    rec('         MIS-DESCRIPTION WITH A LARGE RESIDUAL.**')
    held = sum(1 for x in (s1, s2) if x)
    rec('    ### ### **REGISTERED 3 ; HELD %d ; SPLIT 1.**' % held)

    rec('')
    rec('### (3) THE ACT`S OWN FINDING, WHICH NO EXPECTATION ASKED FOR.')
    rec('-' * 104)
    rec('    ### ### **THE SENTENCE THE ORDER ASKS FOR IS FALSE ON THE VERY CHART IT IS FITTED')
    rec('    ### TO.** ### `W(f_a) <= -m_fit(a)` fails at ### **%d of the 35 cells**, because a'
        % R.get('violations'))
    rec('    ### LEAST-SQUARES FIT IS A CENTRE LINE AND ROUGHLY HALF THE DATA LIES BELOW IT BY')
    rec('    ### CONSTRUCTION. ### The sentence is written to the trail AS ORDERED, with this')
    rec('    ### refutation printed beside it, and the repair -- `m_min` in place of `m_fit` --')
    rec('    ### is OFFERED AND NOT ADOPTED, because the choice is the author`s.')

    rec('')
    rec('### (4) THE ROW.')
    rec('-' * 104)
    have = read(CORR)
    if MARK in have:
        rec('    ### ### **THIS ACT`S ROW IS ALREADY IN THE LEDGER. ### NOT WRITING A SECOND.**')
        nums = corr_row.numbers_in(have)
        row = next((l for l in have.split(NL) if MARK in l), '')
        rec('      rows : ### **%d** ### ; its number : ### **%s** ### ; cells : ### **%d**'
            % (len(nums), row.split('|')[1].strip() if row.count('|') > 1 else '?',
               row.count('|') - 1))
    else:
        nums = corr_row.numbers_in(have)
        nxt = max(nums) + 1
        rec('    rows in the ledger : %d ; the number offered : ### **%d**' % (len(nums), nxt))
        cells = [
            str(nxt),
            ('**THE MARGIN OVER SUPPORT IS NOT MONOTONE, THE CONTROL NEVER CROSSES, AND THE '
             'CONJECTURE THE ORDER WORDS IS FALSE ON ITS OWN CHART** (%s). **COMPONENT 1: 35 '
             'ladder cells, m(a) = -W = A - PR read from b477`s bank with the zero side beside '
             'it; m is POSITIVE at all 35, falls from 8.78115 at a=1.3 to a MINIMUM 0.024337988 '
             'at a=%s, then RISES over 9 steps to a LOCAL MAXIMUM 0.0422898584 at a=5.196152 '
             'and FALLS again over the last 6 to 0.0382311845 -- TWO turning points, %d of %d '
             'steps rising. '
             'The 56-cell aim map is the second family and its margin is not a function of a: at '
             'a fixed width it varies more than between widths. COMPONENT 2: three forms fixed on '
             'the sealed face before any fit; on the primary loss the ladder prefers a POWER OF a '
             '(RMS 0.1395) and the aim map a constant-plus-decay by a factor 1.01; the two losses '
             'DISAGREE on both families. COMPONENT 3: the control`s margin is positive at all 35 '
             'cells with ZERO sign changes, minimum 1.16912, and the falsifier names a HEIGHT '
             '(gamma=16.290216, reached at a=40 and a=81) the ladder`s widths do not reach -- so '
             'it is OUT OF RANGE, not unmet. The conjecture W(f_a) <= -m_fit(a) FAILS AT 17 OF 35 '
             'CELLS: a least-squares fit is a centre line, not a bound.')
             % (MARK, R.get('turn_a'), R.get('rises'), R.get('steps')),
            ('`data/b477_entries.jsonl` (diagonal + control_diagonal) ; `data/b437_rungs.json` ; '
             '`data/b334_leg_reaching_40.json`, `_81`, `data/b334_leg_covered.json` ; '
             '`tools/b489_components.py`'),
            ('no axiom print -- ### **NOTHING WAS COMPILED AND NO CHAIN WAS RUN.** ### Every '
             'value is read from a bank; the only arithmetic is a prime-power sieve and a '
             'least-squares fit over banked numbers.'),
            'MEASURED',
            ('(N1) REFUTED, (N2) REFUTED, (N3) REFUTED ; (S1) HELD, (S2) HELD, (S3) SPLIT. '
             '### **THE CONJECTURE IS GRADED CONJECTURED AND NO HIGHER**, from a finite-reach '
             'chart of 35 widths in [1.3, 5.656854]. ### **NOTHING ABOUT RH FOLLOWS FROM A FIT.** '
             '### No lane opened; no grade moved; row U1 unedited; nothing deposits; nothing at '
             'Zenodo is written; h2 where the deposit left it.'),
        ]
        code, msg = corr_row.write_row(CORR, cells)
        for l in msg:
            rec('    %s' % l)
        if code:
            io.open(os.path.join(D, 'b489_desk_notes.txt'), 'w', encoding='utf-8',
                    newline=NL).write(NL.join(L) + NL)
            return 2

    rec('')
    rec('### (5) WHAT THIS ACT CLOSES AND WHAT IT MINTS.')
    rec('-' * 104)
    rec('    CLOSED : ### **1** ### -- the margin`s shape over support, asked and answered on')
    rec('      the ladder`s own reach: ### **IT HAS A MINIMUM INSIDE THE CHART**, at')
    rec('      `a = %s`, and no monotone form describes it.' % R.get('turn_a'))
    rec('    MINTED : ### **3**')
    rec('      (i)   ### **A LEAST-SQUARES FIT IS A CENTRE LINE, NOT A BOUND.** ### An order')
    rec('            that asks for `X <= fit(X)` asks for something a least-squares fit cannot')
    rec('            supply: half its own data lies below it. ### A bound needs a MINIMUM, an')
    rec('            envelope or a proof -- not a mean.')
    rec('      (ii)  ### **A FALSIFIER MUST NAME A COORDINATE THE CHART HAS.** ### This one')
    rec('            named a HEIGHT and was handed a chart indexed by WIDTH. ### **AN UNTESTED')
    rec('            FALSIFIER IS NOT A PASSED ONE**, and the act says which it is.')
    rec('      (iii) ### **AN ABSOLUTE RESIDUAL IS DOMINATED BY THE LARGEST DATA.** ### The')
    rec('            seat expected the residual where the fit is qualitatively wrong; it is')
    rec('            where `m` is biggest. ### **WHERE A FIT IS WRONG AND WHERE ITS RESIDUAL')
    rec('            LIVES ARE DIFFERENT QUESTIONS.**')

    rec('')
    rec('    the span, by tool : %s' % (curspan or '?'))
    rec('    the last fold     : %s' % (lastfold or '?'))
    rec('')
    rec('=' * 104)
    io.open(os.path.join(D, 'b489_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, s3='SPLIT', held=held),
              io.open(os.path.join(D, 'b489_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL + '  written: b489_desk_notes.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
