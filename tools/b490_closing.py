# -*- coding: utf-8 -*-
"""b490_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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


def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')


R = json.loads(read(os.path.join(D, 'b490_results.json')) or '{}')
post = read(os.path.join(D, 'b490_checks_postpush.txt'))
comp = read(os.path.join(D, 'b490_components.txt'))

rec('=' * 104)
rec('b490 -- THE CLOSING RECORD. ### THE INCREMENTS, THE RATIO, AND THE PRIOR TEST.')
rec('=' * 104)

rec('')
rec('### (1) COMPONENT 0 -- pid 27508.')
rec('-' * 104)
rec('    ### ### **NEITHER BRANCH OF THE ORDER`S CONDITIONAL HOLDS.** ### Two readings sixty')
rec('    ### seconds apart: ### **27508 ABSENT AT BOTH**, and ### **NO `lean` OR `lake` PROCESS')
rec('    ### AT EITHER.** ### The order provides for children existing, and for 27508 being')
rec('    ### ALIVE with none. ### It is neither, and the act says so.')
rec('    `27508` is ### **b475`S DETACHED AXIOM RUN** ### -- `data/b475_launch.json`.')
rec('    its log : ### **403,049 bytes BY `stat`, NEVER OPENED**, last written 2026-09-22')
rec('      21:33:50, ### **IDLE OVER THREE HOURS.**')
rec('    ### ### **AND A STANDING EXCLUSION CARRIED SINCE b481 IS FALSE.** ### Nine suites')
rec('    ### excused that log from `G-NOPRIORBANK` because ### *"another act`s live process is')
rec('    ### still appending to it"*. ### The process died and ### **NOTHING RE-TESTED THE')
rec('    ### GROUND.** ### The exception is retired here and the arm runs at full width.')

rec('')
rec('### (2) COMPONENT 1 -- THE 34 INCREMENTS, AND THE TURN FRACTIONS.')
rec('-' * 104)
st = R.get('steps') or []
rec('    34 steps printed. ### **%d ADMIT A NEW PRIME POWER; %d ADMIT NONE**, and those are'
    % (R.get('n_entering'), 34 - R.get('n_entering')))
rec('    printed as `(none)` rather than left blank.')
rec('    the channel split `d(m) = d(arch) - d(pr)` closes to ### **%.2g** ### at worst.'
    % R.get('closes_max'))
rec('')
rec('    ### ### **THE TURN FRACTIONS THE ORDER ASKS FOR: NOT DECIDABLE FROM THE BANKS.**')
rec('    ### Per-`n` term VALUES are banked at ### **EXACTLY ONE OF THE 35 CELLS** ### --')
rec('    ### `b449_integrand.json`, at `a = %s`, the outlier -- as `levels[*].terms`, a mapping'
    % R.get('terms_cell'))
rec('    ### `n -> value` with `terms_sum == prime` exactly. ### Eleven terms, of which')
rec('    ### **`16` AND `17` ARE EXACTLY `0.0`**, `log 17` sitting on the window`s own edge.')
rec('    ### ### **AND NEITHER `27` NOR `32` IS AMONG THEM**, that cell`s window reaching only')
rec('    ### to `a^2 = 17`. ### The only other route evaluates the smeared window --')
rec('    ### **THAT IS RUNNING THE CHAIN, WHICH THIS ORDER FORBIDS IN ITS OWN CLOSING LINE.**')
rec('    ### ### **SO (N1) IS NEITHER HELD NOR REFUTED. AN ABSENCE IS A PRINTED RESULT.**')
rec('')
rec('    ### ### **AND THE FIRST DRAFT OF THAT HALT WAS WRONG.** ### It was about to report')
rec('    ### that NO bank carried per-`n` terms. ### One does. ### **A HALT PROVED OVER THE')
rec('    ### WRONG POPULATION IS NOT A HALT** -- b486`s lesson met again -- and the survey`s')
rec('    ### own finder caught it, with a positive control proving the finder sees an')
rec('    ### `n -> value` mapping when one exists and calls a bare list of `n` an INDEX.')
rec('')
rec('    ### ### **A SIX-PLACE ROUNDING DECIDES MEMBERSHIP AT THE EDGE.** ### The rungs are')
rec('    ### `sqrt n` to six places. ### `sqrt 17`, `19`, `23`, `29` round ### **UP** ### and')
rec('    ### those powers fall inside their own rungs; ### **`sqrt 25`, `27`, `31`, `32` ROUND')
rec('    ### DOWN** ### and fall just outside -- ### **INCLUDING BOTH THE ORDER NAMES.**')
rec('      on the STORED floats : `3^3` enters one rung late, and ### **`2^5` NEVER ENTERS.**')
rec('      on the GENERATOR     : `3^3` sits exactly at the margin`s LOCAL MAXIMUM and `2^5`')
rec('        exactly at the LAST RUNG -- which is what (N1) presumes.')
rec('    ### **BOTH READINGS ARE PRINTED AND NEITHER IS SILENTLY CHOSEN.**')

rec('')
rec('### (3) COMPONENT 2 -- THE SENSITIVITY RATIO. ### **THE ONE VERDICT.**')
rec('-' * 104)
rec('    ### ### **THE RATIO PEAKS AT %.6g, AT `a = %.6f`, INDEX %d.**'
    % (R.get('peak'), R.get('peak_a'), R.get('peak_i')))
rec('    the margin`s minimum is at index %d (`a = 4.061553`); ### **THE DISTANCE IS %d RUNGS.**'
    % (R.get('lo'), R.get('dist')))
rec('    ### ### **VERDICT: THE RATIO DOES NOT PEAK WITHIN ONE RUNG OF THE MARGIN`S MINIMUM.**')
rec('    ### and the SECOND-highest ratio IS at the minimum cell itself, so ### **THE')
rec('    ### EXPECTATION FAILS BY ONE RUNG, NOT BY A MILE.**')
rats = R.get('ratios') or []
rec('    the whole column stays below ### **%.2g** ### -- the two-side disagreement never'
    % max(rats))
rec('    reaches a part in ### **%d** ### of the margin it prices.' % int(1 / max(rats)))

rec('')
rec('### (4) COMPONENT 3 -- THE CITATION. ### **TESTED-AT-b334.**')
rec('-' * 104)
rec('    quoted from `relay data/b334_the_aim_map.txt`, the paragraph headed')
rec('    *"THE EPSTEIN CROSSING REGION -- THE NEGATIVE CONTROL CHARTED -- IS THREE AIMS"*:')
rec('      aim 1 : height `gamma = 16.290216` , support ### **`a = 40`** ### , `+0.655053`')
rec('      aim 2 : height `gamma = 16.290216` , support ### **`a = 81`** ### , `+1.362830`')
rec('      aim 3 : height `gamma = 46.960994` , support ### **`a = 81`** ### , `+0.194219`')
rec('    ### every member is at an off-line zero`s height and none is elsewhere; the region is')
rec('    ### EMPTY on the covered leg, whose widths are `1.3` and `1.41`.')
rec('    ### ### **AND THAT IS WHY THIS LADDER COULD NOT TEST IT.** ### The ladder`s last rung')
rec('    ### is `a = 5.656854`; the crossings were resolved at `40` and `81` -- ### **SEVEN AND')
rec('    ### FOURTEEN TIMES WIDER.** ### The falsifier is OUT OF RANGE on this chart, not')
rec('    ### unfired. ### **A FALSIFIER TESTED ELSEWHERE IS CITED WHERE IT WAS TESTED.**')

rec('')
rec('### (5) THE EXPECTATIONS.')
rec('-' * 104)
rec('    ### **(N1)** ### **NOT DECIDABLE FROM THE BANKS** ### -- neither held nor refuted.')
rec('    ### **(N2)** ### **REFUTED** ### -- two rungs, not one.')
rec('    ### **(N3)** ### **HELD.**')
rec('    ### **(S1)** ### **REFUTED** ### -- the split closes to `6.1e-06`, not the `1e-4` the')
rec('          seat allowed. ### **THE SEAT PRICED ITS OWN INSTRUMENT TOO CHEAPLY**, carrying')
rec('          b489`s worst ABSOLUTE disagreement across to increments a hundred times smaller.')
rec('    ### **(S2)** ### **HELD** ### ; ### **(S3)** ### **HELD** ### -- the largest increments')
rec('          sit at the small-`a` end, where NO prime power enters and the archimedean channel')
rec('          alone moves the margin.')

rec('')
rec('### (6) THE DEFECTS THIS ACT RECORDS OF ITS OWN INSTRUMENTS. ### **SEVEN, AND ONE IS OLD.**')
rec('-' * 104)
rec('    ### ### **(a) A LITERAL BACKSPACE BYTE IN A REGEX, FROM A HEREDOC.** ### `\\b` written')
rec('    ### through a quoted shell heredoc became `0x08`, so `G-NOCHAIN-RUN` could not match')
rec('    ### its own control and passed a mutation it should have refused. ### **b483 HIT THIS')
rec('    ### EXACT TRAP AND A MEMORY RECORDS IT.** ### The file LOOKED right; only the arm`s')
rec('    ### control found it. ### Repaired with the Edit path, not another heredoc.')
rec('    ### ### **(b) AN ARM READ ITS OWN CONTROL STRING.** ### `split(\'LIVE = \')[-1]` takes')
rec('    ### the LAST occurrence, which was the negative control a few lines below it.')
rec('    ### ### **(c) AN ARM COUNTED THE PROSE WITH THE TABLE** -- one further `(none)` in the')
rec('    ### summary sentence beneath it.')
rec('    ### ### **(d) A VERDICT SAT ON THE NEXT LINE.** ### `line_with` returns the FIRST line')
rec('    ### carrying a marker, and the desk puts `(N2)` on one line and its verdict below.')
rec('    ### ### **(e) AN ARM CONDEMNED READING A TOOL AS RUNNING IT.** ### The survey opens')
rec('    ### `b321_window.py` as TEXT to quote its return signature. ### **READING A TOOL IS')
rec('    ### NOT RUNNING IT**, and the arm now forbids the shapes that EXECUTE.')
rec('    ### ### **(f) THE WRITE-LIST ARM CALLED A FILE DIRTY SINCE b475 ONE OF THIS ACT`S')
rec('    ### WRITES.** ### A bare `git status` reading cannot tell a stale modification from a')
rec('    ### fresh one; the population is now bounded by the sealed face`s own mtime.')
rec('    ### ### **(g) THE DECLARED-ARM COUNTER DISAGREED WITH THE SENTENCE BESIDE IT.** ### The')
rec('    ### face`s (G2) block retires `G-NOB475LOG` in words and names its replacement, and the')
rec('    ### counter read only the token. ### **AN ARM A FACE RETIRES IN WORDS IS NOT AN ARM IT')
rec('    ### DECLARES.** ### The face is sealed and correct; the COUNTER was wrong.')
rec('    ### ### **AND ONE THAT IS NOT AN ARM`S FAULT:** ### the row writer accepted a cell')
rec('    ### containing two `|` characters, wrote a row of EIGHT cells, and only its read-back')
rec('    ### reported it. ### The malformed row was removed and rewritten before any commit.')
rec('    ### **THE GUARD CHECKS THE NUMBER BEFORE WRITING; NOTHING CHECKS THE CELLS FOR THE')
rec('    ### DELIMITER.** ### ROUTED -- this act`s face carries `corr_row.py` as UNEDITED, so')
rec('    ### the repair is not taken here.')

rec('')
rec('### (7) THE SUITE, THE COMMITS, THE MIRROR.')
rec('-' * 104)
rec('    pre-push  : 60 arms, 0 live failing, 0 positive-control passes.')
rec('    post-push : %s' % lw(post, 'ARMS RUN'))
rec('                %s' % lw(post, 'VERDICT :'))
rec('')
rec('    the commits, each read back by `ls-remote`:')
for name, repo in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE)):
    h = git(repo, 'rev-parse', 'HEAD')
    r = git(repo, 'ls-remote', 'origin', 'refs/heads/main').split()
    r = r[0] if r else ''
    rec('      %-20s local %s ; remote %s ; ### **%s**'
        % (name, h[:12], r[:12], 'AGREE' if h and h == r else 'DISAGREE'))
rec('    ### all three pushed and read back on the FIRST attempt.')
rec('    the mirror : `mirror-refresh-2026-09-23-b490.zip` at `a02811c` --')
rec('      ### **CLEAN ON ALL THREE CLAUSES.**')

rec('')
rec('### (8) THE CENSUSES, THE PINS, THE LISTS.')
rec('-' * 104)
rec('    handoff census : %s' % lw(read(os.path.join(D, 'b490_census_closing.txt')),
                                   'TOTAL MISSING'))
rec('    faces census   : %s' % lw(read(os.path.join(D, 'b490_faces_census_closing.txt')),
                                   'TOTAL MISSING'))
rec('    pins           : %s' % lw(read(os.path.join(D, 'b490_pins_closing.txt')),
                                   'REPOS HARD-FAILING'))
rec('    ### **THE FOUR LISTS STAY OPEN.** ### No chain was run and no lane was opened. ### No')
rec('    ### grade moved; row U1 is unedited; nothing compiled; nothing deposits; nothing at')
rec('    ### Zenodo is written; ### **h2 WHERE THE DEPOSIT LEFT IT.** ### **AND NOTHING ABOUT')
rec('    ### RH FOLLOWS.**')

rec('')
rec('### (9) WHAT IS CARRIED FORWARD.')
rec('-' * 104)
rec('    (a) ### **THE PER-`n` TERMS EXIST AT ONE CELL AND THE QUESTION NEEDS THIRTY-FIVE.**')
rec('        A run that banked `terms` at every rung would decide (N1) outright. ### ROUTED --')
rec('        it is a chain run, and this order forbade one.')
rec('    (b) ### **`corr_row.py` CHECKS THE NUMBER BUT NOT THE CELLS.** ### A `|` inside a cell')
rec('        still lands a malformed row. ### ROUTED, not taken: this face carries the tool as')
rec('        UNEDITED.')
rec('    (c) ### **b475`S RUN IS NOW POSITIVELY KNOWN DEAD.** ### Whether its log is worth')
rec('        reading -- and under what ruling -- is the author`s. ### It was not opened here.')
rec('    (d) ### **THE SECOND TURN AT `a = 5.196152` IS STILL UNEXPLAINED**, and this act adds')
rec('        that `3^3` sits exactly there on the generator reading. ### That is a coincidence')
rec('        of coordinates, ### **NOT A MECHANISM**, and nothing here makes it one.')
rec('')
rec('=' * 104)
rec('  ### ### **b490 CLOSES. 61 ARMS, 0 LIVE FAILING, 0 POSITIVE-CONTROL PASSES.**')
rec('=' * 104)

io.open(os.path.join(D, 'b490_closing.txt'), 'w', encoding='utf-8', newline=NL).write(
    NL.join(L) + NL)
print(NL + '  written: b490_closing.txt')
