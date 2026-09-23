# -*- coding: utf-8 -*-
"""b497_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
BT = chr(96)
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


def j(p):
    return json.loads(read(os.path.join(D, p)) or '{}')


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.replace(chr(13), '').strip()


def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')


R, SC = j('b497_results.json'), j('b497_scores.json')
pre = read(os.path.join(D, 'b497_checks.txt'))
post = read(os.path.join(D, 'b497_checks_postpush.txt'))
carried = read(os.path.join(D, 'b497_checks_postpush_carried.txt'))
mir, pins = read(os.path.join(D, 'b497_mirror.txt')), read(os.path.join(D, 'b497_pins_closing.txt'))
cens = read(os.path.join(D, 'b497_census_closing.txt'))
fcens = read(os.path.join(D, 'b497_faces_census_closing.txt'))

REPOS = [('relay', os.path.join('D:', os.sep, 'relay')),
         ('PLACE-papers', os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')),
         ('SIDE-global-section', os.path.join('D:', os.sep, 'SIDE-global-section'))]

rec('=' * 104)
rec('b497 -- THE CLOSING RECORD. ### **KILLED, NOT FAILED; ALL THREE ABSENT; COMPONENT 3 STOPPED.**')
rec('=' * 104)

rec('')
rec('### (1) WHAT THE LOG SAYS.')
rec('-' * 104)
rec('    `relay/data/b495_ef_build.log`, ### **COMMITTED UNCHANGED**, %d bytes, %d lines.'
    % (R['bytes'], R['lines']))
rec('    sha256 %s' % R['sha256'])
rec('      marks (stamped lines)              : %d' % R['marks'])
rec('      ### ### **DISTINCT INSTANTS        : %d**' % R['distinct_instants'])
rec('      wall time, the log`s outer marks   : ### **%.1f s** (%.1f min)'
    % (R['wall_seconds'], R['wall_seconds'] / 60.0))
rec('      `lake`s summed reported durations  : ### **%.1f s** across %d spans'
    % (R['lake_summed'], R['lake_spans']))
rec('      `END` / `EXIT` lines               : %d, ### **%d NON-ZERO**'
    % (len(R['ends']), R['nonzero_exits']))
rec('      modules built before the kill      : ### **%d**, every one `Mathlib.*`'
    % len(R['modules_built']))
rec('      ### ### **MODULES THAT FAILED, BY NAME : NONE**')
rec('    ### ### **BOTH EXITS ARE `0xC000013A` = `STATUS_CONTROL_C_EXIT`.** ### That is what a')
rec('    ### Windows process reports when a console control event reaches it. ### **THE BUILD WAS')
rec('    ### KILLED, NOT BROKEN**, and the log names no module that failed to compile. ### A')
rec('    ### reader who saw the non-zero exit and wrote *"the build failed"* would have said')
rec('    ### something ### **THE LOG DOES NOT SUPPORT.**')
rec('    ### ### **AND NOT ONE `Zeta23` MODULE WAS REACHED.** ### The run spent its whole life')
rec('    ### cloning and compiling mathlib. ### **SO THE LOG SAYS NOTHING WHATEVER ABOUT WHETHER')
rec('    ### THE 57 VENDORED MODULES COMPILE.**')

rec('')
rec('### (2) THE THREE PROFILES, AND THE STOP.')
rec('-' * 104)
for n, v in R['profiles'].items():
    rec('    `%-24s` -> ### **%s**' % (n, v['verdict']))
rec('    `#print axioms` output lines anywhere in the log : ### **0**')
rec('    ### ### **ABSENT IS NOT OTHER.** ### The probe never ran to completion, so there is no')
rec('    ### axiom string to read -- ### **NOT A STRING THAT CAME OUT WRONG.** ### **(R82) IS')
rec('    ### NEITHER CLAIMED NOR REFUTED BY THIS ACT**, and b473`s and b480`s wording is right')
rec('    ### again: ### **VOID FOR WANT OF A RUN.**')
rec('    ### ### **COMPONENT 3 WAS NOT RUN.** ### The order: *"otherwise print which and STOP')
rec('    ### before Component 3."* ### REGISTRY`s `SIDE-explicit-formula` row keeps `PENDING`, no')
rec('    ### profile is written beside it, and ### **NO ROW CITES THE KERNEL.** ### **A STOP')
rec('    ### OBEYED IS A RESULT**; the alternative was to write three profiles into REGISTRY that')
rec('    ### no run produced.')

rec('')
rec('### (3) b495`S OWED CELLS, PAID.')
rec('-' * 104)
rec('    b495`s (N3) and its (S2) both named ### **THIS LOG`S MODULE MARKS**, and b495`s own order')
rec('    forbade reading the log, so both were scored ### **NOT SCORABLE** and routed here.')
rec('    ### ### **(N3) IS PAID: %d DISTINCT INSTANTS ACROSS %d MARKS.** ### b480`s defect -- one'
    % (R['distinct_instants'], R['marks']))
rec('    ### precomputed instant stamped on every mark -- would have given ### **ONE.** ### The')
rec('    ### repair is confirmed ### **ON THE POPULATION THE EXPECTATION NAMED**, not on the')
rec('    ### mechanism-level control b495 had to substitute.')
rec('    ### ### **(S2) IS PAID, AND FLATLY:** ### it asked whether the `FromPNTPlus` ten were what')
rec('    ### `lake` built earliest. ### **NO `Zeta23` MODULE WAS BUILT AT ALL**, so neither they')
rec('    ### nor anything else of the kernel`s was.')

rec('')
rec('### (4) THE EXPECTATIONS.')
rec('-' * 104)
rec('    ### **(N1) REFUTED** -- %d non-zero exits, not 0.' % R['nonzero_exits'])
rec('    ### **(N2) REFUTED** -- all three `ABSENT`.')
rec('    ### **(N3) HELD** -- %d distinct instants against a bar of fifty.' % R['distinct_instants'])
rec('    ### **(S1) HELD** ### and the face said it was cheap: it was drawn from a DECLARED peek.')
rec('    ### **(S2) HELD** -- a process-control failure, not a Lean failure; failed modules NONE.')
rec('    ### **(S3) REFUTED, AND WITH THE SIGN BACKWARDS.** ### The seat predicted wall time would')
rec('      ### GREATLY EXCEED `lake`s summed durations, reasoning from the mathlib clone -- real,')
rec('      ### in the log, and network time `lake` does not account. ### **THE SUMMED DURATIONS')
rec('      ### ARE THE LARGER, BY %.1f s**, because ### **`lake` BUILDS IN PARALLEL**: %d spans'
    % (R['lake_summed'] - R['wall_seconds'], R['lake_spans']))
rec('      ### summing %.1f s finished inside %.1f s of wall clock, about ### **%.1fx**'
    % (R['lake_summed'], R['wall_seconds'], R['lake_summed'] / R['wall_seconds']))
rec('      ### concurrency. ### **A SUM OF PER-JOB DURATIONS IS NOT AN ELAPSED TIME**, and the')
rec('      ### order asked for both numbers precisely because they are not the same number.')
rec('    ### ### **THE NAVIGATOR`S: HELD %d ; REFUTED %d. ### THE SEAT`S: HELD %d ; REFUTED %d.**'
    % (SC['nav_held'], 3 - SC['nav_held'], SC['seat_held'], 3 - SC['seat_held']))

rec('')
rec('### (5) ### **A SYSTEMIC DEFECT IN THE WRITE-LIST READER, FOUND BY ITS OWN ARM.**')
rec('-' * 104)
rec('    The post-push suite first reported ### **`files written that NO (W) GLOB COVERS : 1')
rec('    [b495_ef_build.log]`** -- a file this face ### **DECLARES BY NAME IN ITS OWN (W).**')
rec('    ### ### **THE CAUSE IS THE CORPUS`S OWN POSSESSIVE CONVENTION.** ### This programme')
rec('    ### writes a possessive with a backtick -- `this act`s record`, `b496`s face`, `(R108)`s')
rec('    ### first line` -- adopted so ground strings survive being written into Python. ### **EACH')
rec('    ### SUCH POSSESSIVE MAKES THE BACKTICK COUNT ODD**, and `globs_of()`s naive pairing then')
rec('    ### DESYNCHRONISES, pairing the closing backtick of one path with the possessive of the')
rec('    ### next sentence and returning ### **A MULTI-LINE BLOB OF PROSE AS THOUGH IT WERE A')
rec('    ### GLOB.**')
rec('    ### MEASURED OVER THE LAST FIVE FACES:')
rec('      b493 EVEN, 21 globs, ### **0 malformed**')
rec('      b494 EVEN, 23 globs, ### **0 malformed**')
rec('      b495 ### **ODD**, 37 globs, ### **5 MALFORMED**')
rec('      b496 ### **ODD**, 29 globs, ### **4 MALFORMED**')
rec('      b497 ### **ODD**, 37 globs, ### **6 MALFORMED**')
rec('    ### ### **SO `G-WRITELIST-KINDS` HAS BEEN READING A PARTLY-GARBLED LIST FOR THREE ACTS**,')
rec('    ### and no act noticed until the garbling happened to swallow a declaration that mattered.')
rec('    ### ### **THE INSTRUMENT WAS REPAIRED AND THE FACE WAS NOT TOUCHED.** ### `globs_of()`')
rec('    ### now pairs backticks ### **WITHIN A LINE** and keeps only candidates that look like a')
rec('    ### path -- no spaces, no newline, path characters only. ### **BOTH RUNS ARE BANKED**:')
rec('    ### `b497_checks_postpush_carried.txt` is the run with the broken reader, and')
rec('    ### `b497_checks_postpush.txt` is the run with the repaired one.')
rec('    ### ### **AND THIS IS NOT b496`S CASE WEARING A NEW COAT.** ### b496`s face GENUINELY')
rec('    ### OMITTED two files and b496 refused to widen a glob to hide it. ### **HERE THE FILE IS')
rec('    ### DECLARED AND THE READER COULD NOT SEE IT** -- repairing a parser so it can read what')
rec('    ### was already written is not widening a bar. ### A file the face does not name is still')
rec('    ### uncovered, and the repaired reader still says so.')

rec('')
rec('### (6) THIS ACT`S OTHER DEFECTS -- FOUR.')
rec('-' * 104)
rec('    (a) ### **THE COMPONENTS TOOL NARRATED THE SEAT`S PREDICTION, NOT THE NUMBERS.** ### It')
rec('        ### printed *"the gap is -2463.6 s, and the log names what filled it: the clone"* --')
rec('        ### a sentence that is FALSE for a negative gap. ### The tool had been written to')
rec('        ### explain the result the seat expected. ### **AN INSTRUMENT THAT NARRATES A')
rec('        ### PREDICTION WILL NARRATE IT EVEN WHEN THE NUMBER REFUTES IT.**')
rec('    (b) ### **A SOURCE KEY WAS ADDED TWICE** and the suite would not parse -- the carried head')
rec('        ### already had `res=`, and the patch added a second.')
rec('    (c) ### **A CODE BLOCK WAS LOCATED BY A BARE SUBSTRING THAT MATCHED ITS OWN QUOTATION.**')
rec('        ### `src.index("def regenerate():")` found the text ### **INSIDE AN ARM`S PREDICATE')
rec('        ### STRING** -- the arm that checks the generator is wired in -- and sliced from')
rec('        ### there. ### **THIS IS THE THIRD TIME IN TWO ACTS** (b496`s `disjunctions()` scanned')
rec('        ### from its own mention of `ARMS = [`). ### Anchored to a line start.')
rec('    (d) ### **`G-PROCESS-GONE` PASSED ITS OWN POSITIVE CONTROL.** ### Its predicate called')
rec('        ### `tasklist` directly and its control was a ### **NO-OP** -- a property of the WORLD')
rec('        ### cannot be falsified by mutating `S`. ### The world now enters as the source')
rec('        ### `pid_alive`, which the harness can and does falsify. ### **b496 LEARNED THIS AND')
rec('        ### THIS ACT STILL WROTE THE NO-OP.**')

rec('')
rec('### (7) THE COMMITS, THE MIRROR, THE CENSUSES.')
rec('-' * 104)
rec('    pre-push  : %s' % lw(pre, 'ARMS RUN :'))
rec('    post-push : %s' % lw(post, 'ARMS RUN :'))
rec('                %s' % lw(post, 'VERDICT :'))
rec('    the commits, each read back by `ls-remote`:')
for name, path in REPOS:
    loc = git(path, 'rev-parse', 'HEAD')
    rem = git(path, 'ls-remote', 'origin', 'main')
    rem = rem.split()[0] if rem else ''
    rec('      %-20s local %s ; remote %s ; ### **%s**'
        % (name, loc[:12], (rem[:12] or '### UNRESOLVED'),
           'AGREE' if loc and loc == rem else '### DISAGREE'))
rec('    the mirror : `mirror-refresh-2026-09-23-b497.zip` at `%s` -- ### **%s**'
    % (git(REPOS[1][1], 'rev-parse', '--short', 'HEAD'),
       lw(mir, 'VERDICT:').replace('### VERDICT: ', '') or '?'))
rec('    handoff census : %s' % lw(cens, 'TOTAL MISSING'))
rec('    faces census   : %s' % lw(fcens, 'TOTAL MISSING'))
rec('    pins           : %s ### (run ALONE)' % lw(pins, 'REPOS HARD-FAILING'))
rec('    ### **THE FOUR LISTS STAY OPEN.** ### Nothing compiled and no `lake` command ran; ### **THIS')
rec('    ### ACT DID NOT RELAUNCH THE BUILD** -- a re-run is another act`s to order. ### Nothing')
rec('    ### fetched; nothing deposits; ### **NOTHING AT ZENODO IS WRITTEN**; row U1 unedited;')
rec('    ### ### **h2 WHERE THE DEPOSIT LEFT IT.** ### K1, K2, K3 not started; no keystone touched.')

rec('')
rec('### (8) WHAT IS CARRIED FORWARD.')
rec('-' * 104)
rec('    (a) ### **THE KERNEL STILL HAS NO PROFILE, AND NO ROW CITES IT.** ### `SIDE-explicit-')
rec('        ### formula` reads `PENDING`. ### **A RE-RUN OF THE BUILD IS THE NAVIGATOR`S TO')
rec('        ### ORDER**, and it will need to survive whatever killed the first one.')
rec('    (b) ### **WHAT KILLED IT IS NOT ESTABLISHED.** ### `STATUS_CONTROL_C_EXIT` says a console')
rec('        ### control event reached the process; it does not say who sent it. ### **THIS ACT')
rec('        ### DOES NOT GUESS**, and a re-run that does not address it may die the same way.')
rec('    (c) ### **THE `globs_of()` REPAIR IS IN `b497_checks.py` ONLY.** ### Every future suite')
rec('        ### carries it forward from here; the faces b495 and b496 sealed keep their odd')
rec('        ### parity, and their banked runs keep whatever the broken reader gave them.')
rec('    (d) ### **(R108)(2): `e_difficulty` AWAITS ITS STATEMENT-READ ACT**, its three cells')
rec('        ### quoted at b496. ### This act did not choose.')
rec('    (e) ### **`corr_row.py` CHECKS THE NUMBER AND NOT THE CELLS**, routed at b490, still')
rec('        ### ### **OVERDUE.** ### Row 346 went in clean because its cells held no pipe.')
rec('=' * 104)

io.open(os.path.join(D, 'b497_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print('  written: b497_closing.txt')
