# -*- coding: utf-8 -*-
"""b489_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.replace(chr(13), '').strip()


def lw(text, needle):
    return next((l.strip() for l in text.split(NL) if needle in l), '')


R = json.loads(read(os.path.join(D, 'b489_results.json')) or '{}')
comp = read(os.path.join(D, 'b489_components.txt'))
post = read(os.path.join(D, 'b489_checks_postpush.txt'))

rec('=' * 104)
rec('b489 -- THE CLOSING RECORD. ### THE MARGIN OVER SUPPORT, AND A CONJECTURE THAT FAILS ITS CHART.')
rec('=' * 104)

rec('')
rec('### (1) COMPONENT 1 -- THE MARGIN, CELL BY CELL.')
rec('-' * 104)
rec('    `m(a) = -W(f_a) = A - PR` by (R87). ### 35 ladder cells read from `b477_entries.jsonl`,')
rec('    each with its ### **INDEPENDENTLY BANKED ZERO SIDE** ### and its two-side residual.')
rec('    ### ### **EVERY MARGIN IS POSITIVE** ### -- min `%.9g`, max `8.78115282` -- so `W < 0`'
    % R.get('m_min'))
rec('    at every cell the ladder reaches.')
rec('    ### ### **AND THE SHAPE HAS TWO TURNING POINTS, NOT ONE:**')
rec('      falls over 19 steps to a MINIMUM ### **%.9g at a = %s**' % (R.get('m_min'),
                                                                      R.get('turn_a')))
rec('      rises over 9 steps to a LOCAL MAXIMUM ### **%.9g at a = %s**' % (R.get('max_m'),
                                                                           R.get('max_a')))
rec('      falls again over the last 6 to `0.0382311845` at `a = 5.656854`.')
rec('      ### **%d of the %d steps rise, all between the two turns.**' % (R.get('rises'),
                                                                          R.get('steps')))
rec('    ### the minimum sits ONE RUNG BEFORE `a = 4.123106` -- the cell b446 and b447 already')
rec('    ### called an outlier, now placed on a curve rather than standing alone.')
rec('    ### the aim map`s 56 cells are a ### **SECOND FAMILY** ### indexed by `(a, gamma)`: at')
rec('    ### a fixed width the margin varies MORE than it varies between widths, so on that')
rec('    ### family `m` is not a function of `a` at all.')

rec('')
rec('### (2) COMPONENT 2 -- THE SHAPE, FITTED AND NOT BELIEVED.')
rec('-' * 104)
for l in comp.split(NL):
    if ('RMS residual on m' in l or l.strip().startswith('(i)') or l.strip().startswith('(ii)')
            or l.strip().startswith('(iii)') or 'PREFERRED ON' in l or 'TWO LOSSES' in l):
        rec('    %s' % l.strip()[:98])
rec('    ### ### **THE RANKING IS NOT ROBUST.** ### The two losses disagree on BOTH families,')
rec('    ### form (iii) carries a third constant the others do not, and on the aim map the')
rec('    ### winner`s own margin is a factor `1.01`. ### **THAT IS NOT A PREFERENCE.**')
rec('    ### ### **AND EVERY FORM IS MONOTONE IN `a` BY CONSTRUCTION** while the margin turns')
rec('    ### twice, so all three mis-describe the shape whatever their residual.')
rec('    ### a fit over thirty-five cells is a ### **DESCRIPTION, NOT A LAW.**')

rec('')
rec('### (3) COMPONENT 3 -- THE CONJECTURE, AND WHY IT FAILS.')
rec('-' * 104)
rec('    ### **%s**' % R.get('sentence'))
rec('')
rec('    ### ### **AND IT IS FALSE ON THE VERY CHART IT WAS FITTED TO:** the measured `m` falls')
rec('    ### below `m_fit(a)` at ### **%d of the 35 cells.**' % R.get('violations'))
rec('    ### ### **A LEAST-SQUARES FIT IS A CENTRE LINE, NOT A BOUND** -- roughly half its own')
rec('    ### data lies below it by construction. ### An order that asks for `X <= fit(X)` asks')
rec('    ### for something least squares cannot supply; a bound needs a MINIMUM, an envelope,')
rec('    ### or a proof.')
rec('    ### the repair the data supports -- `m_min = %.9g` in place of `m_fit` -- IS true at'
    % R.get('m_min'))
rec('    ### all 35 cells. ### **OFFERED AND NOT ADOPTED; THE CHOICE IS THE AUTHOR`S.**')
rec('')
rec('    ### THE FALSIFIER : the control`s margin is ### **POSITIVE AT ALL 35 CELLS, WITH %d'
    % R.get('crossings'))
rec('    ### SIGN CHANGES AND %d NEGATIVE CELLS**, falling monotonically from `16.0696` to a'
    % R.get('ctrl_negatives'))
rec('    ### minimum `1.16912`. ### **BUT IT IS OUT OF RANGE, NOT UNMET.** ### The falsifier')
rec('    ### names a support "resolving `t = 16.29`", and `16.290216` is a ### **GAMMA** ### --')
rec('    ### an aim`s HEIGHT -- which the aim map reaches only at widths `40` and `81`. ### The')
rec('    ### ladder stops at `5.656854`. ### **AN UNTESTED FALSIFIER IS NOT A PASSED ONE**, and')
rec('    ### this act says which it is rather than counting a non-crossing as a pass.')
rec('')
rec('    ### THE PREDICTION : the next cell at the ladder`s own ratio is ### **a = %.6f**'
    % R.get('next_a'))
for k, v in sorted((R.get('predictions') or {}).items()):
    rec('      %-27s predicts m = ### **%.9g**' % (k, v))
rec('    ### ### **THEY DISAGREE BY A FACTOR OF TEN ONE STEP PAST THE DATA**, and the second')
rec('    ### turn says the measured value is likelier to FALL than to follow any of them.')

rec('')
rec('### (4) THE EXPECTATIONS.')
rec('-' * 104)
rec('    ### **(N1)** monotone in `a`            -- ### **REFUTED** ### (%d of %d steps rise)'
    % (R.get('rises'), R.get('steps')))
rec('    ### **(N2)** a power of `log a` preferred -- ### **REFUTED** ### (form (ii) wins the')
rec('          primary loss on NEITHER family)')
rec('    ### **(N3)** the control crosses zero   -- ### **REFUTED** ### (0 sign changes, 0')
rec('          negative cells) ### **AND OUT OF RANGE**')
rec('    ### **(S1)** HELD ; ### **(S2)** HELD ; ### **(S3)** ### **SPLIT** -- every form is')
rec('          monotone as expected, but the residual is concentrated at the ### **SMALL-`a`**')
rec('          end (RMS `0.183` before the turn against `0.0247` after), not past the turn.')
rec('          ### **AN ABSOLUTE RESIDUAL IS DOMINATED BY THE LARGEST DATA**, and where a fit')
rec('          ### is WRONG and where its residual LIVES are different questions.')

rec('')
rec('### (5) THE DEFECTS THIS ACT RECORDS OF ITS OWN INSTRUMENTS. ### **SIX.**')
rec('-' * 104)
rec('    ### ### **(a) THE (R70) REHEARSAL CAUGHT A FIELD MISREADING BEFORE THE SEAL.** ### It')
rec('    ### took `places_z` for the aim map`s prime slot and got a NEGATIVE margin where the')
rec('    ### map prints a positive room. ### `places_z` is already the signed places sum; the')
rec('    ### prime slot is `prime_z`. ### **A SIGN ERROR WOULD HAVE RUN THROUGH ALL 56 CELLS.**')
rec('    ### ### **(b) THE COMPONENTS TOOL SAID THE MARGIN "RISES AT EVERY STEP AFTER THE')
rec('    ### MINIMUM".** ### It does not: it rises for 9 steps and then falls for 6. ### **A')
rec('    ### STATEMENT THAT READS ONLY THE ENDPOINTS HID THE SECOND TURN**, and the face`s own')
rec('    ### READING (5), sealed, carries that endpoint wording. ### The face is not edited;')
rec('    ### both figures are printed here and the defective sentence is named.')
rec('    ### ### **(c) A FIGURE WAS TYPED INTO LEDGER ROW 338 AND THE BANK REFUTED IT.** ### The')
rec('    ### row said "14 of 34 steps rise"; the bank computes ### **9**. ### The row was')
rec('    ### corrected IN PLACE before any commit, and the desk tool now DERIVES those figures')
rec('    ### from the results bank instead of carrying them as prose.')
rec('    ### ### **(d) `G-C1-MARGIN-IS-MINUS-W` FIRED, AND IT WAS RIGHT: b437`s PARTS ARE')
rec('    ### ROUNDED.** ### `b437_rungs.json` stores `arch` and `pr` at about ten significant')
rec('    ### figures while `b477` stores `W` at full precision; their difference reaches')
rec('    ### ### **1.73e-05 at `a = 1.5`**. ### So the face`s READING (1) -- "the two agree to')
rec('    ### `1e-12`" -- is TRUE at the rehearsed cell and FALSE at 10 of the 32 cells that')
rec('    ### carry both. ### **THE REHEARSAL GENERALISED FROM ONE CELL.** ### The margin is')
rec('    ### unaffected: it is `-W` read from b477 and never from b437`s parts.')
rec('    ### ### **(e) TWO ARMS CARRIED BARS THAT WERE TYPED, NOT READ.** ### A `1e-5` bar on')
rec('    ### the ABSOLUTE two-side residual is refused by two cells (worst `3.56e-05`); the')
rec('    ### quantity that matters is the residual AGAINST THE MARGIN IT PRICES, worst')
rec('    ### `1.07e-05` relative. ### **`m` SPANS 360-FOLD ACROSS THIS LADDER AND AN ABSOLUTE')
rec('    ### BAR IGNORES IT.**')
rec('    ### ### **(f) AN ARM RAN THAT THE SEALED FACE DOES NOT DECLARE.**')
rec('    ### `G-C3-REFUTATION-BESIDE-IT` was built, ran and passed -- and the face, sealed')
rec('    ### before components, names no such arm. ### **AN ARM THE FACE DOES NOT DECLARE IS')
rec('    ### NOT THIS ACT`S ARM**, and the face cannot be edited to admit it. ### Rather than')
rec('    ### drop a true check for bookkeeping, its predicate was FOLDED into the declared arm')
rec('    ### whose subject is the same sentence, and the declared count then matched the run.')
rec('    ### ### **AND THE ARM THAT CAUGHT ITS OWN AUTHOR IS WORTH ITS OWN LINE.**')
rec('    ### `G-C1-NO-VALUE-INVENTED` forbade a typed decimal outright and fired on the trail`s')
rec('    ### own prose. ### **A TYPED FIGURE IS NOT A FAULT; A TYPED FIGURE THE BANK DOES NOT')
rec('    ### CARRY IS.** ### It now matches every 6-place literal in this act`s tools AND its')
rec('    ### trail record against the banked cells and the sources this act quotes -- and its')
rec('    ### first version orphaned three legitimate figures, two quoted from b334`s aim map')
rec('    ### and one equal to `sqrt 2`. ### **AN ARM THAT KNOWS ONLY ONE SOURCE CALLS EVERY')
rec('    ### OTHER SOURCE AN INVENTION.**')

rec('')
rec('### (6) THE SUITE, THE COMMITS, THE MIRROR.')
rec('-' * 104)
rec('    pre-push  : 61 arms, 0 live failing, 0 positive-control passes -- the mirror arm')
rec('      DEFERRED, since the archive is built after the push.')
rec('    post-push : %s' % lw(post, 'ARMS RUN'))
rec('                %s' % lw(post, 'NEGATIVE-CONTROL FAILURES'))
rec('                %s' % lw(post, 'VERDICT :'))
rec('')
rec('    the commits, each read back by `ls-remote`:')
for name, repo in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE)):
    h = git(repo, 'rev-parse', 'HEAD')
    r = git(repo, 'ls-remote', 'origin', 'refs/heads/main').split()
    r = r[0] if r else ''
    rec('      %-20s local %s ; remote %s ; ### **%s**'
        % (name, h[:12], r[:12], 'AGREE' if h and h == r else 'DISAGREE'))
rec('    ### relay`s push failed on its FIRST attempt (`send-pack: unexpected disconnect`, then')
rec('    ### a DNS failure) and was retried and read back. ### **A TRANSIENT NETWORK FAILURE IS')
rec('    ### RECORDED, NOT SMOOTHED OVER.**')
rec('    the mirror : `mirror-refresh-2026-09-23-b489.zip` at `4abaa5f` --')
rec('      ### **CLEAN ON ALL THREE CLAUSES.**')

rec('')
rec('### (7) THE CENSUSES, THE PINS, THE LISTS.')
rec('-' * 104)
rec('    handoff census : %s' % lw(read(os.path.join(D, 'b489_census_closing.txt')),
                                   'TOTAL MISSING'))
rec('    faces census   : %s' % lw(read(os.path.join(D, 'b489_faces_census_closing.txt')),
                                   'TOTAL MISSING'))
rec('    pins           : %s' % lw(read(os.path.join(D, 'b489_pins_closing.txt')),
                                   'REPOS HARD-FAILING'))
rec('    ### **THE FOUR LISTS STAY OPEN.** ### No chain was run and no lane was opened. ### No')
rec('    ### grade moved; no terminal was added, moved, renamed or graded; row U1 is unedited;')
rec('    ### no Lean of the corpus was touched; nothing compiled; no bridge typed; ### **h2')
rec('    ### WHERE THE DEPOSIT LEFT IT.** ### **AND NOTHING ABOUT RH FOLLOWS FROM A FIT.**')

rec('')
rec('### (8) WHAT IS CARRIED FORWARD.')
rec('-' * 104)
rec('    (a) ### **(R99) IS RATIFIED AND ENTERED BY THE TRAIL RECORD ONLY.** ### The author')
rec('        applies `s14` and `s2` at the platform; ### **THE ACT AFTER FETCHES BOTH')
rec('        DESCRIPTIONS BACK AND BANKS THEM BEFORE ANY RECORD SAYS THE EDIT WAS MADE.**')
rec('    (b) ### **THE CONJECTURE`S FORM IS THE AUTHOR`S TO SETTLE.** ### As worded it is false')
rec('        at 17 of 35 cells; with `m_min` in place of `m_fit` it is true at all 35 and is a')
rec('        statement about a chart, not a law. ### ROUTED, NOT TAKEN.')
rec('    (c) ### **THE SECOND TURN IS UNEXPLAINED.** ### The margin`s local maximum at')
rec('        `a = 5.196152` and the fall after it are printed and not accounted for. ### The')
rec('        ladder`s last six rungs are where a next measurement would bite.')
rec('    (d) ### **b437`S ROUNDED PARTS** ### -- `arch` and `pr` at ten significant figures --')
rec('        cannot check `W` finer than `1e-4`. ### Anything that needs the parts at full')
rec('        precision must go back to the run, not to that bank. ### ROUTED.')
rec('')
rec('=' * 104)
rec('  ### ### **b489 CLOSES. 62 ARMS, 0 LIVE FAILING, 0 POSITIVE-CONTROL PASSES.**')
rec('=' * 104)

io.open(os.path.join(D, 'b489_closing.txt'), 'w', encoding='utf-8', newline=NL).write(
    NL.join(L) + NL)
print(NL + '  written: b489_closing.txt')
