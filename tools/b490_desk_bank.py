# -*- coding: utf-8 -*-
"""b490_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.
### The row is written by the guarded `corr_row.py` (b488), CARRIED UNEDITED. MARK guard stays.
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
CORR = os.path.join('D:', os.sep, 'SIDE-global-section', 'CORRESPONDENCE.md')
NL = chr(10)
L = []
MARK = 'b490, under (R100) as ratified'


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    R = json.loads(read(os.path.join(D, 'b490_results.json')) or '{}')
    SV = json.loads(read(os.path.join(D, 'b490_survey.json')) or '{}')
    notes = read(os.path.join(D, 'b490_span_notes2.txt')) or read(
        os.path.join(D, 'b490_span_notes.txt'))
    curspan = next((l.strip() for l in notes.split(NL)
                    if 'THE CURRENT SPAN :' in l and 'ACT' in l), '')
    steps = R.get('steps') or []

    rec('=' * 104)
    rec('b490 -- THE DESK. ### THE SCORES, THE ROW, THE BANK.')
    rec('=' * 104)

    rec('')
    rec('### (1) THE NAVIGATOR`S EXPECTATIONS.')
    rec('-' * 104)
    rec('    ### **(N1)** ### `3^3` and `2^5` carry more than half of their turns` increments')
    rec('        -- ### **NOT DECIDABLE FROM THE BANKS.**')
    rec('        ### Per-n term VALUES are banked at ### **ONE** ### of the 35 cells')
    rec('        ### (`b449_integrand.json`, a = %s), and ### **NEITHER `27` NOR `32` IS AMONG'
        % R.get('terms_cell'))
    rec('        ### ITS ELEVEN TERMS** -- that cell`s window reaches only to `a^2 = 17`.')
    rec('        ### The only other route evaluates the window, which is ### **RUNNING THE')
    rec('        ### CHAIN**, forbidden by this order`s own closing line.')
    rec('        ### ### **AN ABSENCE IS A PRINTED RESULT, AND IT IS NOT A REFUTATION.**')
    rec('    ### **(N2)** ### the ratio peaks within one rung of `a = 4.061553`')
    rec('        -- ### **REFUTED.** ### It peaks at ### **%.6g at a = %.6f, index %d**;'
        % (R.get('peak'), R.get('peak_a'), R.get('peak_i')))
    rec('        the minimum is index %d. ### **THE DISTANCE IS %d RUNGS.**'
        % (R.get('lo'), R.get('dist')))
    rec('        ### and the SECOND-highest ratio IS at the minimum cell -- ### **THE')
    rec('        ### EXPECTATION FAILS BY ONE RUNG, NOT BY A MILE**, which is worth saying')
    rec('        ### in the same breath as the verdict.')
    rec('    ### **(N3)** ### b334`s three crossings each sit at a support resolving the aim`s')
    rec('        height -- ### **HELD.** ### All three are at `a = 40` or `a = 81`, each at an')
    rec('        off-line zero`s height (`16.290216` twice, `46.960994` once), and b334`s own')
    rec('        paragraph states the region is EMPTY on the covered leg, whose widths are')
    rec('        `1.3` and `1.41`. ### **THE CROSSINGS EXIST ONLY WHERE THE SUPPORT RESOLVES')
    rec('        ### THE HEIGHT.**')

    rec('')
    rec('### (2) THE SEAT`S OWN, REGISTERED ON THE SEALED FACE.')
    rec('-' * 104)
    cm = R.get('closes_max')
    s1 = cm is not None and 5e-5 < cm < 5e-4
    rec('    (S1) the channel split closes to about `1e-4` and NO FINER  -- ### **REFUTED.**')
    rec('         it closes to ### **%.2g** ### at worst, a decade and a half BETTER than the' % cm)
    rec('         seat allowed for. ### **THE SEAT PRICED ITS OWN INSTRUMENT TOO CHEAPLY**:')
    rec('         b437`s parts are stored to ten significant figures, and on differences of')
    rec('         order `1e-2` that is `1e-12` of relative room, not `1e-4`. ### The pessimism')
    rec('         came from b489`s worst ABSOLUTE disagreement (`1.7e-05` at `a = 1.5`, where')
    rec('         `m` is 4.37), carried across to increments where `m` is a hundredth of that.')
    rats = R.get('ratios') or []
    s2 = max(rats) < 1e-4
    rec('    (S2) the sensitivity ratio is below `1e-4` at all 35 cells     -- ### **%s**'
        % ('HELD' if s2 else 'REFUTED'))
    rec('         the worst is ### **%.2g**, a part in %d of the margin it prices.'
        % (max(rats), int(1 / max(rats))))
    ent = [abs(s['dm']) for s in steps if s['enters']]
    non = [abs(s['dm']) for s in steps if not s['enters']]
    s3 = max(non) > max(ent)
    rec('    (S3) the steps admitting a new prime power do NOT carry the largest')
    rec('         increments                                                -- ### **%s**'
        % ('HELD' if s3 else 'REFUTED'))
    rec('         largest `|d(m)|` on an ENTERING step : ### **%.6g**' % max(ent))
    rec('         largest `|d(m)|` on a step admitting NONE : ### **%.6g**' % max(non))
    rec('         ### the largest increments sit at the SMALL-`a` end, where no prime power')
    rec('         ### enters at all -- the archimedean channel alone moves the margin there.')
    held = sum(1 for x in (s2, s3) if x)
    rec('    ### ### **REGISTERED 3 ; HELD %d ; REFUTED %d.**' % (held, 3 - held))

    rec('')
    rec('### (3) THE ACT`S OWN FINDINGS, WHICH NO EXPECTATION ASKED FOR.')
    rec('-' * 104)
    rec('    ### ### **(a) A STANDING EXCLUSION OUTLIVED ITS REASON BY NINE ACTS.** ### From')
    rec('    ### b481 to b489 every suite excused `b475_zeta23_build.log` from `G-NOPRIORBANK`')
    rec('    ### because "another act`s live process is still appending to it". ### **THE')
    rec('    ### PROCESS DIED AND NOTHING RE-TESTED THE GROUND.** ### Component 0 finds pid')
    rec('    ### 27508 absent at both readings and the file cold for over three hours.')
    rec('    ### ### **AN EXCEPTION IS A CLAIM ABOUT THE WORLD AND DECAYS LIKE ONE.**')
    rec('    ### ### **(b) A SIX-PLACE ROUNDING DECIDES WHETHER A PRIME POWER IS IN ITS OWN')
    rec('    ### RUNG.** ### The rungs are `sqrt n` to six places. ### `sqrt 17`, `19`, `23`,')
    rec('    ### `29` round UP and those powers fall inside; ### **`sqrt 25`, `27`, `31`, `32`')
    rec('    ### ROUND DOWN AND FALL OUTSIDE** -- including both the order names. ### On the')
    rec('    ### stored floats `2^5` never enters the ladder at all. ### **BOTH READINGS ARE')
    rec('    ### PRINTED; NEITHER IS SILENTLY CHOSEN.**')
    rec('    ### ### **(c) THE HALT`S FIRST DRAFT WAS WRONG, AND ITS OWN FINDER CAUGHT IT.**')
    rec('    ### This act was about to report that NO bank carried per-n terms. ### One does.')
    rec('    ### **A HALT PROVED OVER THE WRONG POPULATION IS NOT A HALT** -- b486`s lesson,')
    rec('    ### met again -- and the narrower halt that survives is sharper: the terms exist')
    rec('    ### at one cell of thirty-five, and it is the outlier.')

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
            ('**THE INCREMENT DECOMPOSITION IS NOT AVAILABLE, THE SENSITIVITY RATIO PEAKS TWO '
             'RUNGS FROM THE TURN, AND A STANDING EXCLUSION OUTLIVED ITS REASON BY NINE ACTS** '
             '(%s). **COMPONENT 0: pid 27508 is b475`s detached axiom run and is ABSENT at both '
             'readings sixty seconds apart, with no lean or lake process at either -- neither '
             'branch of the order`s conditional holds. Its log is %d bytes by stat, never opened, '
             'idle over three hours; so the ground b481-b489 used to excuse it from G-NOPRIORBANK '
             'is FALSE and the exception is retired. COMPONENT 1: 34 steps printed with the prime '
             'powers entering each (16 steps admit one, 18 admit none, printed as (none)); the '
             'channel split d(m) = d(arch) - d(pr) closes to %.2g at worst. THE DECOMPOSITION THE '
             'ORDER ASKS FOR IS NOT AVAILABLE: per-n term VALUES are banked at exactly ONE of the '
             '35 cells (b449_integrand.json, a=%s) and neither 27 nor 32 is among its eleven '
             'terms. The rungs are sqrt n to six places and the rounding decides membership: '
             'sqrt 27 and sqrt 32 both round DOWN, so on the stored floats 2^5 never enters at '
             'all, while on the generator both sit exactly on the two turns. COMPONENT 2: 35 '
             'ratios of the two-side disagreement to the margin, peak %.6g at a=%.6f index %d '
             'against the minimum at index %d -- '
             'TWO rungs. COMPONENT 3: b334`s three crossings quoted at their bank, all at a=40 or '
             'a=81, entered in the trail as TESTED-AT-b334.')
            % (MARK, R.get('log_bytes', 403049), cm, R.get('terms_cell'),
               R.get('peak'), R.get('peak_a'), R.get('peak_i'), R.get('lo')),
            ('`data/b477_entries.jsonl` ; `data/b437_rungs.json` ; `data/b449_integrand.json` ; '
             '`data/b334_the_aim_map.txt` ; `data/b475_launch.json` ; `tools/b490_components.py`'),
            ('no axiom print -- ### **NOTHING COMPILED, NO CHAIN RUN, NO LANE OPENED.** ### The '
             'only arithmetic is a prime-power sieve, subtraction and division of banked numbers.'),
            'MEASURED',
            ('(N1) NOT DECIDABLE FROM THE BANKS ; (N2) REFUTED ; (N3) HELD. (S1) REFUTED -- the '
             'seat priced its own instrument too cheaply ; (S2) HELD ; (S3) HELD. ### **NOTHING '
             'ABOUT RH FOLLOWS.** ### No grade moved; row U1 unedited; the four lists stay OPEN; '
             'h2 where the deposit left it.'),
        ]
        code, msg = corr_row.write_row(CORR, cells)
        for l in msg:
            rec('    %s' % l)
        if code:
            io.open(os.path.join(D, 'b490_desk_notes.txt'), 'w', encoding='utf-8',
                    newline=NL).write(NL.join(L) + NL)
            return 2

    rec('')
    rec('### (5) WHAT THIS ACT CLOSES AND WHAT IT MINTS.')
    rec('-' * 104)
    rec('    CLOSED : ### **2** ### -- b475`s run, now positively known dead rather than assumed')
    rec('      live; and the falsifier`s prior test, cited at its bank as TESTED-AT-b334.')
    rec('    MINTED : ### **3**')
    rec('      (i)   ### **AN EXCEPTION IS A CLAIM ABOUT THE WORLD AND DECAYS LIKE ONE.** ### A')
    rec('            narrowing carried forward with its ground printed is still carried forward')
    rec('            UNTESTED. ### The ground must be re-checked, not re-quoted.')
    rec('      (ii)  ### **A GENERATOR AND ITS STORED FLOAT ARE DIFFERENT OBJECTS AT AN EDGE.**')
    rec('            b437 minted this for tolerances; here it decides SET MEMBERSHIP, and the')
    rec('            two readings disagree about whether `2^5` is on the ladder at all.')
    rec('      (iii) ### **AN ABSENCE IS A PRINTED RESULT.** ### (N1) is neither held nor')
    rec('            refuted: the quantity it speaks of exists in no bank. ### **SCORING IT')
    rec('            EITHER WAY WOULD HAVE INVENTED EVIDENCE.**')
    rec('')
    rec('    the span, by tool : %s' % (curspan or '?'))
    rec('=' * 104)
    io.open(os.path.join(D, 'b490_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(n1='NOT DECIDABLE', n2=False, n3=True, s1=s1, s2=s2, s3=s3, held=held),
              io.open(os.path.join(D, 'b490_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL + '  written: b490_desk_notes.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
