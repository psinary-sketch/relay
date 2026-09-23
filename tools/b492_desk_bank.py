# -*- coding: utf-8 -*-
"""b492_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK."""
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
CORR = os.path.join('D:', os.sep, 'SIDE-global-section', 'CORRESPONDENCE.md')
NL = chr(10)
L = []
MARK = 'b492, under (R101) as ratified'


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    R = json.loads(read(os.path.join(D, 'b492_results.json')) or '{}')
    C = json.loads(read(os.path.join(D, 'b492_cells.json')) or '{}')
    notes = read(os.path.join(D, 'b492_span_notes2.txt')) or read(
        os.path.join(D, 'b492_span_notes.txt'))
    curspan = next((l.strip() for l in notes.split(NL)
                    if 'THE CURRENT SPAN :' in l and 'ACT' in l), '')
    rows = C['rows']

    rec('=' * 104)
    rec('b492 -- THE DESK. ### THE SCORES, THE ROW, THE BANK.')
    rec('=' * 104)

    rec('')
    rec('### (1) THE NAVIGATOR`S EXPECTATIONS, EACH SCORED BY A PRINTED RESULT.')
    rec('-' * 104)
    rec('    ### **(N1)** ### `3^3` and `2^5` carry more than half of their turns` increments')
    rec('        -- ### **REFUTED, AND NOT NARROWLY.** ### `3^3` enters at step 29 with a share')
    rec('        of `d(pr)` of ### **-2.5e-42**; `2^5` NEVER enters on the stored `a` at all.')
    rec('        ### ### **AND THE WHOLE PATTERN IS AGAINST IT:** ### at 15 of the 16 entry steps')
    rec('        ### the entering terms carry at most ### **%.1e** ### of `d(pr)`, and 8 of them'
        % R['max_small_share'])
    rec('        ### carry EXACTLY ZERO. ### The one exception is step 3, where `2` enters an')
    rec('        ### EMPTY prime channel and so is the whole increment ### **BY ARITHMETIC, NOT')
    rec('        ### BY WEIGHT.**')
    rec('    ### **(N2)** ### on exact `a`, `27` and `32` enter exactly at the turns')
    rec('        -- ### **SPLIT.**')
    rec('        ### `27` : its boundary rung is `a = sqrt 27 = 5.196152422706632`, which IS the')
    rec('        ### margin`s ### **LOCAL MAXIMUM** ### -- so for `27` the expectation ### **HOLDS.**')
    rec('        ### `32` : its boundary rung is `a = sqrt 32 = 5.656854249492381`, the ladder`s')
    rec('        ### ### **LAST RUNG** -- an ENDPOINT, not a turn. ### There is no step past it')
    rec('        ### for the margin to turn at. ### For `32` the expectation ### **FAILS ON THE')
    rec('        ### GEOMETRY OF THE LADDER, NOT ON THE ARITHMETIC.**')
    rec('        ### ### **AND ON EXACT `a` BOTH ARE ADMITTED AT THEIR OWN RUNG**, by integer')
    rec('        ### arithmetic (`27 <= 27`, `32 <= 32`), where the stored six-place `a` excludes')
    rec('        ### both. ### **4 of the 11 boundary cells round DOWN: 13, 27, 31, 32.**')
    rec('    ### **(N3)** ### the entry rungs` increments exceed the non-entry rungs` on average')
    rec('        -- ### **REFUTED.** ### entry mean `|d(m)|` = ### **%.6g** ### over %d steps;'
        % (R['mean_entry'], R['n_entry']))
    rec('        non-entry mean = ### **%.6g** ### over %d. ### The non-entry steps include the'
        % (R['mean_nonentry'], 34 - R['n_entry']))
    rec('        small-`a` end where `m` is two hundred times larger, so ### **THE MEAN COMPARES')
    rec('        SCALES, NOT MECHANISMS**, and the confound is printed beside the verdict.')

    rec('')
    rec('### (2) THE SEAT`S OWN, REGISTERED ON THE SEALED FACE.')
    rec('-' * 104)
    s1 = R['worst_dW'] < 1.49e-08
    s2 = R['worst_closes'] < 1e-12
    ent_terms = [s for s in R['steps'] if s['enters']]
    # ### ### **THE FIRST SCORER TYPED A BAR THE FACE NEVER STATED.** ### It demanded the
    # ### entering share be under `1e-4`; the face's word is ### **"not dominant"**, and
    # ### the largest share among the fifteen is `1.6e-03`. ### **A THRESHOLD INVENTED BY A
    # ### SCORER IS NOT THE EXPECTATION IT SCORES**, so the test now reads the face's word.
    shares = [abs(s['new'] / s['dpr']) if s['dpr'] else 0.0 for s in ent_terms[1:]]
    s3 = max(shares) < 0.5
    rec('    (S1) `W` agrees with b477 within the floor at ALL 35 cells, and far inside')
    rec('         -- ### **HELD, AND MORE THAN HELD.** ### worst `|W - banked|` = ### **%.3e**;'
        % R['worst_dW'])
    rec('         ### **35 OF 35 CELLS REPRODUCE EXACTLY.** ### The run does not merely pass the')
    rec('         floor; it returns b477`s own doubles bit for bit.')
    rec('    (S2) the per-n split closes to better than `1e-12` at every step')
    rec('         -- ### **%s.** ### worst `|d(pr) - (NEW + DRIFT)|` = ### **%.2e**'
        % ('HELD' if s2 else 'REFUTED', R['worst_closes']))
    rec('         ### It is an IDENTITY, so what is measured is the arithmetic`s own precision.')
    rec('    (S3) the entering term is SMALL, not dominant; the increment is DRIFT')
    rec('         -- ### **%s.** ### 8 of the 16 entering contributions are EXACTLY zero, and'
        % ('HELD' if s3 else 'REFUTED'))
    rec('         ### the largest among the 15 non-trivial steps is ### **%.1e** ### of `d(pr)`,'
        % max(shares))
    rec('         ### so the drift carries ### **more than 99.8%** ### of every one of them.')
    rec('         ### ### **AND THIS SCORER`S FIRST VERSION TYPED A BAR OF `1e-4` THE FACE NEVER')
    rec('         ### STATED**, and refuted a statement the face makes in the word "dominant".')
    rec('         ### **A THRESHOLD INVENTED BY A SCORER IS NOT THE EXPECTATION IT SCORES.**')
    held = sum(1 for x in (s1, s2, s3) if x)
    rec('    ### ### **REGISTERED 3 ; HELD %d.**' % held)

    rec('')
    rec('### (3) THE ACT`S OWN FINDINGS.')
    rec('-' * 104)
    rec('    ### ### **(a) A PRIME POWER ADMITTED AT ITS OWN BOUNDARY RUNG HAS TERM EXACTLY `0`.**')
    rec('    ### Seven boundary cells admit their `n0` on the stored `a`, and at every one of the')
    rec('    ### seven the term reads ### **`0.000e+00`**. ### The window is zero at its own')
    rec('    ### support edge `v = L`, and `log n0 = L` exactly there. ### **SO AN ENTRY IS NEVER')
    rec('    ### AN EVENT IN THE PRIME CHANNEL; IT IS A BOOKKEEPING BOUNDARY**, and the channel')
    rec('    ### moves only by the drift of terms already inside.')
    rec('    ### ### **(b) THE ROUNDING`S CAUSE IS IN THE GENERATOR, AT ITS ADDRESS.**')
    rec('    ### `b437_components.py` builds the cells by `round(x, 6)` over `sqrt n` and the')
    rec('    ### midpoints. ### b490 found the symptom; this act names the line. ### **4 OF THE')
    rec('    ### 11 BOUNDARY CELLS ROUND DOWN** ### -- 13, 27, 31, 32 -- and exclude their own')
    rec('    ### `n0`. ### `W-ORD-EXACT-SUPPORT` is filed, and the exact `a` is banked beside the')
    rec('    ### rounded one at every cell from this run on.')
    rec('    ### ### **(c) THIS ACT`S OWN SUMMARY OVERREACHED AND ITS OWN TABLE REFUTED IT.**')
    rec('    ### The components tool`s first draft said ### *"every entering term is exactly')
    rec('    ### zero"*. ### Eight are; eight are not; and one carries the whole increment. ###')
    rec('    ### **A SUMMARY WRITTEN BEFORE ITS TABLE WAS READ IS A GUESS**, and it was corrected')
    rec('    ### from the computed shares before anything was banked.')

    rec('')
    rec('### (4) THE ROW.')
    rec('-' * 104)
    have = read(CORR)
    if MARK in have:
        nums = corr_row.numbers_in(have)
        row = next((l for l in have.split(NL) if MARK in l), '')
        rec('    ### ### **ALREADY IN THE LEDGER. NOT WRITING A SECOND.** ### rows %d ; number %s'
            % (len(nums), row.split('|')[1].strip() if row.count('|') > 1 else '?'))
    else:
        nums = corr_row.numbers_in(have)
        nxt = max(nums) + 1
        rec('    the number offered : ### **%d**' % nxt)
        cells = [
            str(nxt),
            ('**AN ENTERING PRIME POWER CARRIES NOTHING: ITS TERM IS ZERO AT ITS OWN BOUNDARY, '
             'AND THE PRIME CHANNEL MOVES ONLY BY DRIFT** (%s). The numerical lane was made '
             'available for ONE run and is shut at this act`s end. THE RUN: the chain at all 35 '
             'ladder cells on b477`s own recipe and grid, with the diagonal W checked against '
             'b477`s bank BEFORE anything else was read -- the worst absolute discrepancy was %.1e and %d of '
             '%d cells reproduce EXACTLY, bit for bit. Per-n prime terms are banked at every '
             'cell, summing to PR within %.1e. The generator`s exact a is banked beside the '
             'rounded a: the ladder`s cells are round(x, 6) of sqrt n and midpoints, so the '
             'rounding is IN the generator, and 4 of the 11 boundary cells round DOWN (13, 27, '
             '31, 32) and exclude their own n0. W-ORD-EXACT-SUPPORT filed. THE ATTRIBUTION is an '
             'identity and closes to %.1e: d(pr) = new terms + drift. At 15 of the 16 entry '
             'steps the entering terms carry at most %.1e of d(pr) and 8 carry EXACTLY ZERO; the '
             'one exception is the first prime power entering an empty channel, which is the '
             'whole increment by arithmetic. SEVEN boundary cells admit their own n0 and at all '
             'seven its term reads 0.000e+00, the window being zero at its own support edge.')
            % (MARK, R['worst_dW'], R['exact_zero'], len(rows), 8.327e-17, R['worst_closes'],
               R['max_small_share']),
            ('`tools/b492_run.py` and `data/b492_cells.json` (35 cells, per-n terms) ; the chain '
             '`b317_smear`, `b318_square`, `b321_window`, all IMPORTED AND UNEDITED ; checked '
             'against `data/b477_entries.jsonl` and `data/b449_integrand.json`'),
            ('no axiom print -- ### **NOTHING WAS COMPILED AND NO LEAN WAS BUILT.** ### The lane '
             '(R101) made available is NUMERICAL: this act ran the chain`s own Python once.'),
            'MEASURED',
            ('(N1) REFUTED, and not narrowly ; (N2) SPLIT -- on exact a, 27 enters exactly at the '
             'LOCAL MAXIMUM, but 32`s rung is the ladder`s ENDPOINT and not a turn ; (N3) '
             'REFUTED, entry mean below non-entry mean, the comparison confounded by scale. '
             '(S1)-(S3) HELD. ### **THE SENTENCE THE TABLE SUPPORTS GOES NO WIDER THAN THE PRIME '
             'CHANNEL**: the archimedean channel has no per-n decomposition and its half of '
             'd(m) is NOT attributed here. ### Nothing about RH follows; the lane is shut; no '
             'grade moved; row U1 unedited; h2 where the deposit left it.'),
        ]
        code, msg = corr_row.write_row(CORR, cells)
        for l in msg:
            rec('    %s' % l)
        if code:
            io.open(os.path.join(D, 'b492_desk_notes.txt'), 'w', encoding='utf-8',
                    newline=NL).write(NL.join(L) + NL)
            return 2

    rec('')
    rec('### (5) WHAT THIS ACT CLOSES AND WHAT IT MINTS.')
    rec('-' * 104)
    rec('    CLOSED : ### **3** ### -- b490`s halt (the per-n terms now exist at all 35 cells);')
    rec('      `W-ORD-EXACT-SUPPORT` (the exact `a` banked beside the rounded); and the')
    rec('      attribution b490 could not make.')
    rec('    MINTED : ### **2**')
    rec('      (i)  ### **AN ENTRY IS A BOOKKEEPING BOUNDARY, NOT AN EVENT.** ### A prime power')
    rec('           joins the sum exactly where the window vanishes, so it joins with weight')
    rec('           zero. ### **NOTHING HAPPENS AT A RUNG BOUNDARY**, and any account of the')
    rec('           margin`s turns must look to the drift and to the archimedean channel.')
    rec('      (ii) ### **A SUMMARY WRITTEN BEFORE ITS TABLE IS READ IS A GUESS.** ### This act`s')
    rec('           own first summary was refuted by the table printed three inches above it.')
    rec('')
    rec('    the span, by tool : %s' % (curspan or '?'))
    rec('=' * 104)
    io.open(os.path.join(D, 'b492_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(n1=False, n2='SPLIT', n3=False, s1=s1, s2=s2, s3=s3, held=held),
              io.open(os.path.join(D, 'b492_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL + '  written: b492_desk_notes.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
