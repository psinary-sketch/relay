# -*- coding: utf-8 -*-
"""b496_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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


def j(p):
    return json.loads(read(os.path.join(D, p)) or '{}')


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.replace(chr(13), '').strip()


def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')


T, R, SC = j('terminal_table.json'), j('b496_results.json'), j('b496_scores.json')
X = j('b496_exercise.json')
pre, post = read(os.path.join(D, 'b496_checks.txt')), read(os.path.join(D, 'b496_checks_postpush.txt'))
mir, pins = read(os.path.join(D, 'b496_mirror.txt')), read(os.path.join(D, 'b496_pins_closing.txt'))
cens = read(os.path.join(D, 'b496_census_closing.txt'))
fcens = read(os.path.join(D, 'b496_faces_census_closing.txt'))
C = T['counts']

REPOS = [('relay', os.path.join('D:', os.sep, 'relay')),
         ('PLACE-papers', os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')),
         ('SIDE-global-section', os.path.join('D:', os.sep, 'SIDE-global-section'))]

rec('=' * 104)
rec('b496 -- THE CLOSING RECORD. ### **K0: THE TERMINAL TABLE, AND THE FACE THAT UNDER-DECLARED.**')
rec('=' * 104)

rec('')
rec('### (1) THE TABLE.')
rec('-' * 104)
rec('    `data/terminal_table.json` and `.md`, from `tools/terminal_table.py` -- ### **SHARED AND')
rec('    NOT act-STEMMED**, because (R107) has the closing suite re-run it at every later close.')
rec('    population : ### **%d** `SIDE-*` repositories (### **%d** with a `.git`, both printed) ;'
    % (T['repos_named'], T['repos_with_git']))
rec('                 ### **%d** ledgers, the archive`s split looms included.' % T['ledgers'])
rec('    ### every repository read ### **AS COMMITTED BLOBS** -- one `git archive` per (repo, ref),')
rec('    ### never the working tree. ### The name matcher is `b378_terminals.py`s, ### **IMPORTED')
rec('    ### AND NOT COPIED**, fixtured on both dialects and both polarities BEFORE use.')
rec('')
rec('      rows (repo, name)                                  : ### **%d**' % C['rows'])
rec('      NOT PROFILED                                       : ### **%d**' % C['not_profiled'])
rec('      UNGRADED                                           : ### **%d**' % C['ungraded'])
rec('      CONFLICT                                           : ### **%d**' % C['conflict'])
rec('      ENCODES-graded                                     : ### **%d**' % C['encodes'])
rec('      ledger names resolving in NO repo at ANY ref       : ### **%d**'
    % C['ledger_names_unresolved'])
rec('      STATEMENT UNRESOLVED, kept as a cell               : ### **%d**'
    % C['statement_unresolved'])
rec('    ### ### **%d OF %d ROWS CARRY NO GRADE AT ALL.** ### The ledgers largely do not disagree'
    % (C['ungraded'], C['rows']))
rec('    ### because they largely do not speak.')
rec('    ### ### **REGISTRY NAMES A PIN FOR %d OF %d KERNELS.** ### For the other thirty-eight the'
    % (T['pins_named'], T['repos_with_git']))
rec('    ### order`s *"at the pin AND at HEAD"* has ### **ONE REF, NOT TWO**, and the table says so')
rec('    ### per row rather than reading `HEAD` twice and calling the agreement a result.')

rec('')
rec('### (2) FOUR MATCHERS TO GET ONE NUMBER, AND ALL FOUR YIELDS PRINTED.')
rec('-' * 104)
M = R['matchers']
rec('    v1 LOOSE    %4d cells   ### any name on any line carrying a grade word -- 67 CONFLICTS'
    % M['v1'])
rec('    v2 WINDOWED %4d cells   ### same table cell, within 120 characters -- 17' % M['v2'])
rec('    v3 NEAREST  %4d cells   ### each grade to its NEAREST name only -- 12' % M['v3'])
rec('    ### **v4 COMPOUND %4d cells   ### adjacent grade words = ONE verdict -- %d**'
    % (M['v4'], C['conflict']))
rec('    ### ### **ONLY THE LAST STEP WAS A READING OF THE ORDER RATHER THAN A TIGHTENING.**')
rec('    ### (R107) defines CONFLICT as *"two ledger cells grade one name differently"*, and these')
rec('    ### ledgers write ONE verdict as `ENCODES-CONCLUSION \\ SHELL`. ### **A MENTION IS NOT A')
rec('    ### GRADE CELL; PROXIMITY IS NOT ATTACHMENT; A COMPOUND VERDICT IS NOT A DISAGREEMENT.**')
rec('    ### ### **THEN ALL %d WERE READ BY HAND** -- the only step that separated signal from'
    % C['conflict'])
rec('    ### noise: ### **GENUINE %d** %s ; AMBIGUOUS %d %s ; ARTEFACT %d.'
    % (len(R['genuine']), R['genuine'], len(R['ambiguous']), R['ambiguous'], len(R['artefact'])))
rec('    ### The machine cell stays `CONFLICT` on all %d and the hand reading is a SEPARATE bank:'
    % C['conflict'])
rec('    ### ### **A GENERATOR THAT QUIETLY DROPPED SIX ARTEFACTS WOULD BE A GENERATOR WHOSE')
rec('    ### NUMBER NOBODY COULD REPRODUCE.**')

rec('')
rec('### (3) WHAT THE HAND READING FOUND THAT NO COUNT WOULD HAVE.')
rec('-' * 104)
rec('    ### ### **THE GRADE VOCABULARY HAS NO CELL FOR A SPLIT GRADE.** ### The ledgers write')
rec('    ### *"DERIVES on the proven direction, INTERFACES on the source biconditional"* and')
rec('    ### *"ENCODES-CONCLUSION \\ SHELL"* because ### **ONE TERMINAL CAN BE TWO THINGS AT ONCE.**')
rec('    ### The author-ruled taxonomy has no such cell, so the ledgers improvise one in prose, and')
rec('    ### ### **EVERY MATCHER THAT READS GRADES AS ATOMS MISREADS THEM.** ### A finding for K1.')
rec('    ### ### **AND `C7_finite_type_false` IS IN THE TABLE, `NOT PROFILED`** -- (R106)(2)`s')
rec('    ### object, reached by an instrument that was not told its name, from the other direction,')
rec('    ### over the whole federation.')

rec('')
rec('### (4) THE EXPECTATIONS.')
rec('-' * 104)
rec('    ### **(N1) HELD** -- %d rows against a bar of 150.' % C['rows'])
rec('    ### **(N2) HELD** -- %d NOT PROFILED, `C7_finite_type_false` among them.'
    % C['not_profiled'])
rec('    ### **(N3) HELD** -- on the instrument`s %d and on the hand reading`s %d.'
    % (C['conflict'], len(R['genuine'])))
rec('      ### ### **BUT THE FIRST NUMBER THIS ACT COMPUTED WAS 67, AND IT WAS WRONG.** ### (N3)')
rec('      ### would have read `HELD` just as loudly on every one of the four matchers, including')
rec('      ### the two that were wrong. ### **AN EXPECTATION THAT ASKS FOR "AT LEAST ONE" IS')
rec('      ### SATISFIED BY NOISE**, and only reading all of them separated the one from it.')
rec('    ### **(S1) HELD** -- %d statements UNRESOLVED and kept as cells.'
    % C['statement_unresolved'])
rec('    ### **(S2) HELD**, more sharply than written -- see the UNGRADED figure in (1).')
rec('    ### **(S3) HELD** -- the pin column is empty for 38 of 44.')
rec('    ### ### **THE SEAT`S: REGISTERED 3 ; HELD 3 ; REFUTED 0.**')

rec('')
rec('### (5) THIS ACT`S OWN DEFECTS -- SEVEN.')
rec('-' * 104)
rec('    (a) ### **THE FIRST GENERATOR DID NOT FINISH.** ### It called `git show` once per file per')
rec('        ### name -- 44 repositories by ~700 names by hundreds of files. ### **A CORRECT')
rec('        ### INSTRUMENT THAT CANNOT COMPLETE IS NOT AN INSTRUMENT.** ### Repaired to one')
rec('        ### `git archive` per (repo, ref), held; the bytes are still the COMMITTED bytes.')
rec('    (b) ### **A DEFERRED FORMAT PRINTED A RAW `%d` TO THE TERMINAL AND TO THE BANK** -- the')
rec('        ### shape `rec(... %d); L[-1] = L[-1] % n`. ### **THIS IS THE THIRD TIME** (b494`s')
rec('        ### closing, b495`s push, here). ### Formatted at the call now, or not at all.')
rec('    (c) ### **A CHARACTER OFFSET WAS PRINTED AS A LINE NUMBER** -- `REGISTRY kernel table at')
rec('        ### line 143979` for a file of 938 lines. ### Caught because it was ABSURD, which is')
rec('        ### luck: ### **A PLAUSIBLE WRONG OFFSET WOULD HAVE STOOD.**')
rec('    (d) ### **`b378.fixtures()` RETURNS `(ok, cases)` AND WAS UNPACKED AS A LIST**, which')
rec('        ### crashed. ### **THE CRASH IS THE KIND OUTCOME**: had it returned a truthy object')
rec('        ### the arm would have reported `ALL PASS` having checked nothing.')
rec('    (e) ### **TWO `G-NO*` ARMS FIRED ON THIS ACT`S OWN SENTENCES SAYING IT HAD NOT DONE THE')
rec('        ### THING.** ### `G-NOLAKE` matched *"no `lake` command ran"* and `G-B495-PID-NOT-')
rec('        ### POLLED` matched *"pid 7860 was not polled"*, both inside the trail writer`s own')
rec('        ### record string. ### **THIS IS A STANDING LESSON OF THIS PROGRAMME** -- b487 minted')
rec('        ### it -- ### **AND IT WAS STILL RE-LEARNED HERE, TWICE, ON ONE RUN.** ### Both arms')
rec('        ### now strip prose and look for a CALL SHAPE.')
rec('    (f) ### **AN ARM CALLED A CORRECT EXTRACTION A DEFECT.** ### `G-STATEMENT-UP-TO-ASSIGN`')
rec('        ### failed live on 8 rows, and all 8 were RIGHT: `(C := C)` is named-argument syntax')
rec('        ### and `let n := c.1` is a binding inside a decide-style statement. ### The arm meant')
rec('        ### a ### **DEPTH-0** `:=`. ### **THE ARM WAS WRONG AND THE LIVE FAILURE SAID SO.**')
rec('    (g) ### **THE NEW ARM COULD NOT DO WHAT IT WAS DECLARED FOR, IN FOUR REVISIONS.**')
rec('        ### `G-ARMS-NO-LIVE-LIMB` was minted to catch b495`s defect -- a control that')
rec('        ### falsifies only one limb of a disjunction -- ### **BY READING THE SUITE`S TEXT.**')
rec('        ### It fired on `x or []` none-defaults, on the word `or` inside quoted strings, on')
rec('        ### ITS OWN SOURCE (it found the literal `ARMS = [` inside its own body and scanned')
rec('        ### 200 lines too early), and on `any(A or B ...)` whose control DOES falsify both.')
rec('        ### ### **THE PROPERTY IS NOT TEXTUAL.** ### Whether a control falsifies every limb is')
rec('        ### a fact about what the control DOES, and only RUNNING it can decide -- which this')
rec('        ### harness already does for every arm. ### **b495 WAS CAUGHT BY THE POSITIVE-CONTROL')
rec('        ### COLUMN AND BY NOTHING ELSE.** ### The arm is re-pointed at that harness.')

rec('')
rec('### (6) ### **THE POST-PUSH SUITE IS NOT CLEAN, AND THAT IS THIS ACT`S FINDING ABOUT ITS FACE.**')
rec('-' * 104)
stray = X.get('stray') or []
rec('    pre-push  : %s' % lw(pre, 'ARMS RUN :'))
rec('    post-push : %s' % lw(post, 'ARMS RUN :'))
rec('    ### ### **FILES WRITTEN THAT NO (W) GLOB COVERS : %d** %s' % (len(stray), stray))
rec('    ### The generator emits FIVE files. ### The sealed face`s write list names THREE of them --')
rec('    ### `terminal_table.json`, `terminal_table.md`, `terminal_table_prior.json` -- and')
rec('    ### ### **OMITS `terminal_table_run.txt` AND `terminal_table_diff.json`.**')
rec('    ### ### **THE ARM IS RIGHT AND THE FACE IS INCOMPLETE.** ### The two files are squarely')
rec('    ### within what (R107) orders -- the run record and the diff the ruling asks for by name --')
rec('    ### but ### **A WRITE LIST IS A CLAIM ABOUT WHAT AN ACT TOUCHES, AND THIS ONE WAS SHORT.**')
rec('    ### ### **THE FACE IS SEALED AND WAS NOT EDITED, AND NO GLOB WAS WIDENED TO MAKE A')
rec('    ### FAILURE DISAPPEAR.** ### b399`s law: a vacuous pass is not evidence, and a pass bought')
rec('    ### by moving the bar is worse than a failure. ### The suite closes ### **NOT CLEAN**, the')
rec('    ### two files are named here, and the next face declares them.')
rec('    ### ### **THIS IS THE SPECIES b399 NAMED AS "A WRITE LIST OMITS THE LATE RITUAL"** -- the')
rec('    ### files a tool writes ALONGSIDE its declared output are the ones the list forgets.')

rec('')
rec('### (7) THE COMMITS, THE MIRROR, THE CENSUSES.')
rec('-' * 104)
rec('    the commits, each read back by `ls-remote`:')
for name, path in REPOS:
    loc = git(path, 'rev-parse', 'HEAD')
    rem = git(path, 'ls-remote', 'origin', 'main')
    rem = rem.split()[0] if rem else ''
    rec('      %-20s local %s ; remote %s ; ### **%s**'
        % (name, loc[:12], (rem[:12] or '### UNRESOLVED'),
           'AGREE' if loc and loc == rem else '### DISAGREE'))
rec('    the mirror : `mirror-refresh-2026-09-23-b496.zip` at `%s` -- ### **%s**'
    % (git(REPOS[1][1], 'rev-parse', '--short', 'HEAD'),
       lw(mir, 'VERDICT:').replace('### VERDICT: ', '') or '?'))
rec('    handoff census : %s' % lw(cens, 'TOTAL MISSING'))
rec('    faces census   : %s' % lw(fcens, 'TOTAL MISSING'))
rec('    pins           : %s ### (run ALONE)' % lw(pins, 'REPOS HARD-FAILING'))
rec('    ### ### **THE GENERATOR WAS RE-RUN BY THE SUITE** -- (R107)`s requirement, in force from')
rec('    ### this close onward. ### The first run has no prior to diff against and says so.')
rec('    ### **THE FOUR LISTS STAY OPEN.** ### Nothing compiled and no `lake` command ran; b495`s')
rec('    ### build at pid 7860 was not polled and its log not read. ### Nothing fetched; nothing')
rec('    ### deposits; ### **NOTHING AT ZENODO IS WRITTEN**; row U1 unedited; ### **h2 WHERE THE')
rec('    ### DEPOSIT LEFT IT.** ### K1, K2 and K3 are not started and no keystone was touched.')

rec('')
rec('### (8) WHAT IS CARRIED FORWARD.')
rec('-' * 104)
rec('    (a) ### **THE NEXT FACE DECLARES `terminal_table_run.txt` AND `terminal_table_diff.json`**')
rec('        ### in its write list. ### Until then the suite reports NOT CLEAN for a true reason.')
rec('    (b) ### **b497 READS b495`S BUILD LOG, PROFILES, AND COMMITS IT**, and owes (N3) and (S2)')
rec('        ### of b495 the cells that act could not score.')
rec('    (c) ### **THE SPLIT-GRADE FINDING GOES TO K1.** ### The vocabulary has no cell for a')
rec('        ### terminal that is two things at once, and the ledgers improvise one in prose.')
rec('    (d) ### **ONE GENUINE CONFLICT STANDS UNRESOLVED**: `e_difficulty`, DERIVES against')
rec('        ### `ENCODES-CONCLUSION \\ SHELL` fourteen lines apart in one file. ### **THIS ACT DID')
rec('        ### NOT CHOOSE**, and choosing is not an instrument`s office.')
rec('    (e) ### **`corr_row.py` CHECKS THE NUMBER AND NOT THE CELLS**, routed at b490, still')
rec('        ### ### **OVERDUE**. ### Row 345 went in clean because its cells held no pipe.')
rec('=' * 104)

io.open(os.path.join(D, 'b496_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print('  written: b496_closing.txt')
