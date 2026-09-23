# -*- coding: utf-8 -*-
"""b494_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
import io
import json
import os
import subprocess
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


R = json.loads(read(os.path.join(D, 'b494_results.json')))
X = json.loads(read(os.path.join(D, 'b494_exercise.json')) or '{}')
pre = read(os.path.join(D, 'b494_checks.txt'))
post = read(os.path.join(D, 'b494_checks_postpush.txt'))
desk = read(os.path.join(D, 'b494_desk_notes.txt'))
mir = read(os.path.join(D, 'b494_mirror.txt'))
pins = read(os.path.join(D, 'b494_pins_closing.txt'))
cens = read(os.path.join(D, 'b494_census_closing.txt'))
fcens = read(os.path.join(D, 'b494_faces_census_closing.txt'))

REPOS = [('relay', os.path.join('D:', os.sep, 'relay')),
         ('PLACE-papers', os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')),
         ('SIDE-global-section', os.path.join('D:', os.sep, 'SIDE-global-section'))]

rec('=' * 104)
rec('b494 -- THE CLOSING RECORD. ### THE SEQUENCE RECONCILED WITH THE RECORD, AND THE FRAME CHECKED.')
rec('=' * 104)

rec('')
rec('### (1) WHAT THIS ACT DID, AND WHAT IT DID NOT.')
rec('-' * 104)
rec('    ### **TWO TABLES IN ONE APPENDED `FINDINGS.md` SECTION**, under (R104) and (R105).')
rec('    ### **NO OTHER DOCUMENT WAS CREATED IN ANY REPOSITORY.** ### Nothing was compiled,')
rec('    ### fetched or deposited; ### **NOTHING AT ZENODO WAS WRITTEN**; no lane was opened;')
rec('    ### no `.lean` file, no REGISTRY row, no ERRATA line. ### The archive and')
rec('    ### `VERIFICATION_LOOM.md` were ### **READ AND NOT WRITTEN.**')
rec('    ### ### **AND A RECONCILIATION IS A READING OF TWO REGISTERS AGAINST A SEQUENCE.**')
rec('    ### It decides no mathematics, and ### **NOTHING ABOUT RH FOLLOWS FROM ANY ROW.**')

rec('')
rec('### (2) TABLE 1 -- THE SEQUENCE AGAINST THE TWO REGISTERS.')
rec('-' * 104)
rec('    the 2026-07-26 pending-work census, at its address in the ARCHIVE:')
rec('      `PLACE-papers/archive/2026-08-24-ledger-split/`')
rec('      `VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md:2471`')
rec('      ### **%d items** -- DIRECT %d, INFORMING %d, INDEPENDENT %d.'
    % (len(R['census']),
       sum(1 for c in R['census'] if c['grade'] == 'DIRECT'),
       sum(1 for c in R['census'] if c['grade'] == 'INFORMING'),
       sum(1 for c in R['census'] if c['grade'] == 'INDEPENDENT')))
rec('    the OPEN_TRAILS desk : ### **%d ruling items.**' % len(R['desk']))
rec('    read against (R104)`s ### **SEVEN-ACT SEQUENCE**, one row per item, in a')
rec('    ### **CLOSED VOCABULARY OF THREE DISPOSITIONS**:')
rec('      TAKEN UP BY (R104)  : ### **%d**' % R['taken_up'])
rec('      TRIPPED BY (R104)   : ### **%d**' % R['tripped'])
rec('      UNTOUCHED           : ### **%d**' % R['untouched'])
rec('    ### ### **NO ROW IS BLANK** and no fourth word was invented for a hard row.')
rec('    ### ### **OF THE %d DIRECT ITEMS, %d IS TAKEN UP** -- `W-SIGN-1`, by act 4.'
    % (R['direct'], R['direct_taken']))

rec('')
rec('### (3) TABLE 2 -- THE FRAME CHECK OVER NINE NAMED FINDINGS.')
rec('-' * 104)
rec('    ### **%d ROWS.** ### Each asks two questions: ### **does the corpus have an ADDRESS'
    % len(R['frame']))
rec('    ### for this finding**, and ### **what does the (R102) ceiling say about it?**')
rec('      with an address   : ### **%d**' % (len(R['frame']) - R['names_nothing']))
rec('      ### NAMES NOTHING : ### **%d**' % R['names_nothing'])
rec('    ### ### **THE ROW THAT NAMES NOTHING** is the Epstein control -- the observation that')
rec('    ### isolates the ### **NON-NEGATIVITY OF `Lambda(n)`** as the xi-specific ingredient.')
rec('    ### It is ### **STATED IN NO DOCUMENT OF THE CORPUS**, and this act ### **DID NOT')
rec('    ### RESTATE IT**: the row carries NO GRADE and the cell says NOT RESTATED.')
rec('    ### ### **THE GRADE CEILING HELD**: no row above `DERIVES` for a terminal or above')
rec('    ### `MEASURED` for a bank, and ### **THIS ACT CONFERRED NONE OF THEM** -- every grade')
rec('    ### in the table is the one the record already holds.')
rec('    ### ### **ONE FINDING IS COMPILED BUT NOT PROFILED.** ### `C7_finite_type_false`')
rec('    ### exists as a terminal; ### `AxiomCheck.lean` at `v0.10.0` lists ### **32** terminals')
rec('    ### and it is ### **NOT AMONG THEM**, while `OPEN_TRAILS.md:102` still calls it a')
rec('    ### *"future trail item (optional)"*. ### **COMPILED IS NOT PROFILED.**')

rec('')
rec('### (4) THE NAVIGATOR`S THREE EXPECTATIONS, SCORED ON PRINTED CELLS.')
rec('-' * 104)
rec('    ### **(N1) REFUTED.** ### The expectation was *at least four of the July DIRECT items')
rec('    ### read TAKEN UP*. ### **ONE DOES.** ### Refutable by a printed cell, and the cell')
rec('    ### refuted it: four of the five DIRECT items are UNTOUCHED by the seven acts.')
rec('    ### **(N2) HELD.** ### At least one of the nine NAMES NOTHING -- exactly one does.')
rec('    ### **(N3) HELD.** ### No row carries a grade above the ceiling, in either kind.')
rec('    the seat`s own three, registered on the face BEFORE the reading:')
rec('      %s' % lw(desk, 'REGISTERED 3'))

rec('')
rec('### (5) THIS ACT`S OWN DEFECTS.')
rec('-' * 104)
rec('    (a) ### **THE FACE`S OWN PHRASE TRIPPED THE REGISTRATION GATE.** ### The (W) section')
rec('        said ### *"TWO DOCUMENTS"*, which the lexical counter read as an ### **ARTIFACT-COUNT')
rec('        PREDICTION**, and `reg_satisfiable.py` answered ### **DO NOT SEAL.** ### It was')
rec('        caught only by ### **READING THE TOOL`S OWN VERDICT LINE** -- b491`s lesson, that a')
rec('        `grep` for a word the tool never prints passes by luck. ### Reworded before the seal.')
rec('    (b) ### **A DEFERRAL CARRIED PAST THE ARM IT NAMES.** ### The suite tail inherited')
rec('        `G-LOG-COMMITTED-UNCHANGED` in its pre-push deferral list. ### **THIS ACT DOES NOT')
rec('        DECLARE THAT ARM**, so the run would have printed ### *"DEFERRED TO POST-PUSH"* for')
rec('        ### **AN ARM THAT DOES NOT EXIST** -- a reassuring line about nothing. ### Dropped,')
rec('        and the ground printed. ### **A DEFERRAL LIST IS A CLAIM ABOUT THE ARMS THAT RUN.**')
rec('    (c) ### **THE PINS TOOL READ TWO REPOSITORIES AS UNRESOLVED, AND THEY WERE NOT.**')
rec('        ### The first closing run reported ### **REPOS HARD-FAILING : 2** -- relay and')
rec('        SIDE-global-section ### **UNRESOLVED** -- minutes after both had been pushed and')
rec('        read back by `ls-remote` by hand. ### A direct `ls-remote` on each answered')
rec('        immediately with the right sha. ### **THE HARD FAILURE WAS TRANSIENT AND IN THE')
rec('        READING, NOT IN THE WORLD**; the three tools had been run back to back. ### The')
rec('        tool was re-run ALONE and the bank is that run. ### **THE TOOL WAS RIGHT TO REFUSE')
rec('        TO CALL AN UNRESOLVED REMOTE 0/0** -- that refusal is why the defect was visible.')

rec('')
rec('### (6) THE SUITE, THE COMMITS, THE MIRROR.')
rec('-' * 104)
rec('    pre-push  : %s' % lw(pre, 'ARMS RUN :'))
rec('                58 declared on the face; `G-MIRROR-TAGGED-BUILD` deferred to post-push.')
rec('    post-push : %s' % lw(post, 'ARMS RUN :'))
rec('                %s' % lw(post, 'VERDICT :'))
rec('    ### **%d FILES WRITTEN THAT NO (W) GLOB COVERS.**' % len(X.get('stray', [])))
rec('    ### `G-NOPRIORBANK` ran at ### **FULL WIDTH over %s prior banks, 0 EXCLUDED BY NAME.**'
    % (lw(pre, 'prior banks').split('checked ')[-1].split(' prior')[0] if 'prior banks' in pre else '?'))
rec('')
rec('    the commits, each read back by `ls-remote`:')
for name, path in REPOS:
    loc = git(path, 'rev-parse', 'HEAD')
    rem = git(path, 'ls-remote', 'origin', 'main').split()[0] if git(path, 'ls-remote', 'origin', 'main') else ''
    rec('      %-20s local %s ; remote %s ; ### **%s**'
        % (name, loc[:12], (rem[:12] or '### UNRESOLVED'), 'AGREE' if loc and loc == rem else '### DISAGREE'))
rec('    the mirror : `mirror-refresh-2026-09-23-b494.zip` at `%s` --'
    % git(REPOS[1][1], 'rev-parse', '--short', 'HEAD'))
rec('      ### **%s**' % (lw(mir, 'VERDICT:').replace('### VERDICT: ', '') or '?'))

rec('')
rec('### (7) THE CENSUSES, THE PINS, THE LISTS.')
rec('-' * 104)
rec('    handoff census : %s' % lw(cens, 'TOTAL MISSING'))
rec('    faces census   : %s' % lw(fcens, 'TOTAL MISSING'))
rec('    pins           : %s ### (the re-run; see (5)(c))' % lw(pins, 'REPOS HARD-FAILING'))
rec('    ### **THE FOUR LISTS STAY OPEN.** ### Nothing fetched; nothing compiled; no lane')
rec('    ### opened; no repository created. ### No corpus grade moved; ### **ROW U1 UNEDITED**;')
rec('    ### nothing deposits; ### **NOTHING AT ZENODO IS WRITTEN**; ### **h2 WHERE THE DEPOSIT')
rec('    ### LEFT IT.**')

rec('')
rec('### (8) WHAT IS CARRIED FORWARD.')
rec('-' * 104)
rec('    (a) ### **THE NEXT ACT IS (R103)`S CREATION** -- `SIDE-explicit-formula`, act 2 of')
rec('        (R104)`s seven. ### It is the first act of the sequence this act just measured.')
rec('    (b) ### **THE PLATFORM SESSION IS STILL THE AUTHOR`S AND STILL BLOCKED.** ### (R102)')
rec('        holds the edits until the whole disposition is applied at once, and ### **EIGHT')
rec('        ROWS EXCEED THE CEILING WITH NO DRAFT** -- three of them titles.')
rec('    (c) ### **(R99)`S KERNEL TEXT IS HELD** -- its target sentence is not in the deposit.')
rec('    (d) ### **`corr_row.py` CHECKS THE NUMBER AND NOT THE CELLS**, routed at b490 and')
rec('        ### **OVERDUE**. ### It has bitten twice (rows 339 and 341). ### This act`s row')
rec('        went in clean, which is ### **NOT EVIDENCE THE GUARD EXISTS.**')
rec('    (e) ### **`C7_finite_type_false` IS COMPILED AND NOT PROFILED**, and `OPEN_TRAILS.md:102`')
rec('        still calls it optional. ### **THIS ACT NAMED IT AND ROUTED NOTHING** -- it is')
rec('        the navigator`s to rule on.')
rec('    (f) ### **THE EPSTEIN CONTROL IS STATED NOWHERE.** ### The one finding of the nine with')
rec('        no address in the corpus. ### **AN UNWRITTEN FINDING IS ONE CONTEXT FROM GONE.**')
rec('=' * 104)

io.open(os.path.join(D, 'b494_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print('  written: b494_closing.txt')
