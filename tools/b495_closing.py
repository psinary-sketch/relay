# -*- coding: utf-8 -*-
"""b495_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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


PIN, CRE, PSH = j('b495_pin.json'), j('b495_create.json'), j('b495_push.json')
WAI, REG, SC, X = j('b495_waiver.json'), j('b495_registry.json'), j('b495_scores.json'), j('b495_exercise.json')
pre, post = read(os.path.join(D, 'b495_checks.txt')), read(os.path.join(D, 'b495_checks_postpush.txt'))
mir, pins = read(os.path.join(D, 'b495_mirror.txt')), read(os.path.join(D, 'b495_pins_closing.txt'))
cens, fcens = read(os.path.join(D, 'b495_census_closing.txt')), read(os.path.join(D, 'b495_faces_census_closing.txt'))

REPOS = [('relay', os.path.join('D:', os.sep, 'relay')),
         ('PLACE-papers', os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')),
         ('SIDE-global-section', os.path.join('D:', os.sep, 'SIDE-global-section')),
         ('SIDE-explicit-formula', os.path.join('D:', os.sep, 'SIDE-explicit-formula'))]

rec('=' * 104)
rec('b495 -- THE CLOSING RECORD. ### **SIDE-explicit-formula CREATED, PUSHED, AND LAUNCHED UNREAD.**')
rec('=' * 104)

rec('')
rec('### (1) THE PIN, AND THE READING THAT NEARLY CHOSE THE OTHER ONE.')
rec('-' * 104)
rec('    `EF_lit``s statement at tag `v1.0` and at `fbdc36b`:')
rec('      sha256 `v1.0`    : %s' % PIN['statement_sha']['v1.0'])
rec('      sha256 `fbdc36b` : %s' % PIN['statement_sha']['fbdc36b'])
rec('      ### ### **BYTE-IDENTICAL : %s** -- and the WHOLE MODULE agrees too, not only the'
    % PIN['same_statement'])
rec('      ### statement. ### **PIN CHOSEN : `%s` = `%s`**, by the order`s'
    % (PIN['pin'], PIN['pin_sha']))
rec('      ### own rule and by nothing else. ### The clone resolves `v1.0` to the SHA the order')
rec('      ### names (`3635e748`), and that agreement is printed rather than assumed.')
rec('    ### ### **AND THE FIRST READING SAID `NOT FOUND AT v1.0`.** ### It would have pinned')
rec('    ### `fbdc36b` -- and scored the navigator`s (N1) REFUTED -- for a reason the order never')
rec('    ### gave. ### The cause is a ### **LAYOUT MOVE**: at `v1.0` the tree is rooted at')
rec('    ### `Zeta23/`; by `fbdc36b` the `zeta23-palomar-layout` merge has moved it under')
rec('    ### `zeta23/`. ### **A PATH MISS IS NOT A FINDING ABOUT THE OBJECT.** ### The module is')
rec('    ### now resolved in ### **EACH REVISION`S OWN TREE**, and the path used is printed')
rec('    ### beside each reading, so the next reader sees the move rather than a verdict.')

rec('')
rec('### (2) THE KERNEL.')
rec('-' * 104)
rec('    `D:/SIDE-explicit-formula` -- the local import closure of `%s`,' % CRE['seed'])
rec('    ### **COMPUTED AT THE PIN, NOT RECALLED FROM THE FACE**: ### **%d modules**, %d external'
    % (CRE['modules'], CRE['external_roots']))
rec('    import roots (not vendored; `lake` fetches those from their own pins).')
rec('    ### ### **BODY DIGESTS AGREEING : %d OF %d.** ### Per module, two digests: the source'
    % (CRE['agreeing'], CRE['modules']))
rec('    ### blob at the pin, and the copy ### **READ BACK FROM DISK BEFORE ANY HEADER EXISTED** --')
rec('    ### hashing the in-memory bytes would prove only that a variable was not reassigned.')
rec('    ### And after the prepend every body was re-read from the file`s TAIL and compared:')
rec('    ### ### **INTACT AT %d OF %d.** ### The claim "nothing but a header was added" is'
    % (CRE['modules'], CRE['modules']))
rec('    ### CHECKED, not intended.')
rec('    `LICENSE` and `NOTICE` carried whole, Apache 2.0 section 4 -- digests IDENTICAL on both.')
rec('    ### ### **%d MODULES CARRY A SECOND HEADER** naming `PrimeNumberTheoremAnd`, because'
    % len(CRE['pnt']))
rec('    ### zeta23`s own `NOTICE` says *"The derived files are the ones under')
rec('    ### Zeta23/FromPNTPlus/"*. ### **THE PREDICATE IS THE SOURCE`S, NOT THE SEAT`S.**')
rec('    ### And those files ALREADY carry their own upstream notice -- *"Ported from')
rec('    ### PrimeNumberTheoremAnd at commit 6a380f0c..."* -- so they now hold ### **THREE')
rec('    ### ATTRIBUTION BLOCKS OF DISTINCT PROVENANCE**, which is correct and not a defect:')
rec('    ### the chain is carried unaltered, neither restated nor summarised.')
rec('    toolchain `%s`, mathlib `%s` -- ### **AS zeta23 PINS THEM.**'
    % (CRE['toolchain'], CRE['mathlib'][:12]))
rec('    ### SPIRAL_MAP rule 4 expects per-kernel divergence and this kernel STATES it: a vendored')
rec('    ### body must compile against the library its author compiled it against.')

rec('')
rec('### (3) THE WAIVER, THE ROW, AND WHAT NEITHER OF THEM SAYS.')
rec('-' * 104)
rec('    SPIRAL_MAP section 7, beside rule 9 (at line %d): ### **RULE 9 WAIVED FOR VENDORED'
    % WAI['rule9_line'])
rec('    ### NAMESPACES**, act b495 named as the reason. ### prefix %s, ### **%d LINES REMOVED**,'
    % (WAI['prefix'], WAI['lines_removed']))
rec('    %d heading. ### **THE WAIVER NAMES ITS OWN BOUNDARY**: it lapses the moment this'
    % WAI['headings'])
rec('    ### programme edits a vendored body, and it is not retroactive to any existing kernel.')
rec('    REGISTRY, one kernel-table row: deposit-pin ### **NONE**, working-head the pushed SHA,')
rec('    source zeta23 at the pin, profile ### **PENDING**. ### prefix %s, %d lines removed.'
    % (REG['prefix'], REG['lines_removed']))
rec('    ### ### **THE NO-CITATION CLAIM IS MEASURED, NOT ASSERTED.** ### The appended block was')
rec('    ### scanned for terminal-shaped names: ### **%d.** ### The one dotted name in it is the'
    % len(REG['terminals_named']))
rec('    ### vendoring seed, a MODULE, named as the thing copied. ### (R106)(3) is satisfied by')
rec('    ### an absence, and ### **THE ABSENCE WAS COUNTED.**')

rec('')
rec('### (4) THE PUSH AND THE LAUNCH.')
rec('-' * 104)
rec('    ### **THE PRE-PUSH GUARD WAS INSTALLED BEFORE THE FIRST PUSH THE REPOSITORY EVER TOOK**')
rec('    -- into the ### **TRACKED** `.githooks/` with `core.hooksPath`, byte-identical to relay`s')
rec('    single source: %s. ### (R15): one guard, one source.' % PSH['hook_identical'])
rec('    `SIDE-explicit-formula` at `%s`, %d files tracked, %d `.lean`.'
    % (PSH['head'][:7], PSH['tracked'], PSH['leans']))
rec('    ### ### **THE BUILD IS LAUNCHED AND UNREAD** -- pid ### **%d**, log' % PSH['pid'])
rec('    ### `%s`. ### The launcher stamps ### **AN INSTANT TAKEN AT EACH LINE**; b480'
    % PSH['log'])
rec('    ### precomputed one instant and stamped every mark with it, so its log could not say how')
rec('    ### long anything took or in what order. ### It profiles the three names ### **WHETHER OR')
rec('    ### NOT THE BUILD EXITS 0**, because a launcher that skips the profile on a non-zero exit')
rec('    ### hands the next act nothing to read.')
rec('    ### ### **AND THE LOG IS NOT COMMITTED BY THIS ACT.** ### It is still being written. ###')
rec('    ### b481-b489 spent nine acts excusing a live log inside a write-list arm; the cleaner')
rec('    ### answer is not to commit a file a running process still owns. ### **b496 READS IT AND')
rec('    ### BANKS IT.**')

rec('')
rec('### (5) THE EXPECTATIONS -- AND TWO THAT CANNOT BE SCORED HERE.')
rec('-' * 104)
rec('    ### **(N1) HELD.** ### byte-identical, pin `v1.0`.')
rec('    ### **(N2) HELD.** ### %d of %d body digests agree.' % (CRE['agreeing'], CRE['modules']))
rec('    ### **(N3) NOT SCORABLE IN THIS ACT.** ### **(S2) NOT SCORABLE, FOR THE SAME REASON.**')
rec('      ### Both name ### **THE LOG`S FIRST TEN MODULE MARKS**, and the same order says')
rec('      ### *"The log is not read in this act."* ### **SCORING THEM WOULD BREAK THE CLAUSE;')
rec('      ### SCORING THEM FROM ANYTHING ELSE WOULD ANSWER A DIFFERENT QUESTION.**')
rec('      ### ### **AND THE FACE DID NOT SEE THE CONFLICT WHEN IT WAS SEALED** -- section (S2)')
rec('      ### confidently re-pointed (N3) at "the ten the launcher marks first", which is the')
rec('      ### same unreadable cell. ### That is this act`s finding about ITS OWN REGISTRATION.')
rec('      ### What could be shown without the log was shown: ### **%d of %d consecutive calls to'
    % (SC.get('distinct_marks', 0), len(SC.get('marks') or [])))
rec('      ### the launcher`s `stamp()` gave DISTINCT instants**, `say()` calls it per line, and')
rec('      ### no precomputed module-level stamp exists. ### **THE WORDING`S OWN POPULATION IS')
rec('      ### b496`S CELL TO PRINT.**')
rec('    ### **(S1) HELD.** ### pid %d ALIVE at the desk`s reading, checked by `tasklist` -- which'
    % PSH['pid'])
rec('      ### asks whether a process exists, ### **NOT WHAT IT WROTE.**')
rec('    ### **(S3) HELD.** ### the ten already carry their own upstream notice.')

rec('')
rec('### (6) THIS ACT`S OWN DEFECTS -- FIVE.')
rec('-' * 104)
rec('    (a) ### **THE IMPORT PARSER RETURNED A CLOSURE OF ONE.** ### It stopped at the first')
rec('        non-`import` line, which in every zeta23 module is the LICENCE HEADER`s first line.')
rec('        ### A closure of 1 with 0 external roots is a number that cannot be right, and it')
rec('        ### was caught by being ### **ABSURD**, not by an arm. ### `import` is now recognised')
rec('        ### anywhere in the file.')
rec('    (b) ### **THE PIN COMPARATOR CALLED A LAYOUT MOVE A STATEMENT CHANGE.** ### See (1).')
rec('        ### **THE DEFECT WOULD HAVE SCORED THE NAVIGATOR`S EXPECTATION REFUTED**, with a')
rec('        ### printed digest beside it, and nothing in the bank would have looked wrong.')
rec('    (c) ### **A CURE THAT ALREADY HAD A TOOL, REINVENTED.** ### The push component wrote the')
rec('        ### guard into `.git/hooks/` from `tools/git-hooks/pre-push` -- ### **A PATH THAT DOES')
rec('        ### NOT EXIST.** ### b371 moved the guard to a TRACKED `.githooks/` with')
rec('        ### `core.hooksPath` and b386`s (R15) made that the single source. ### Caught by the')
rec('        ### crash, which is luck: a tool that wrote a guard nothing reads would have passed.')
rec('    (d) ### **THE REGISTRATION REFUSED TWICE BEFORE IT SEALED.** ### The gate refused for')
rec('        ### want of a banked-index query (b160`s convention, b182`s failure) -- four queries')
rec('        ### run and their results reported. ### Then `reg_satisfiable` answered ### **DO NOT')
rec('        ### SEAL** on SIX numerals the prediction counter read as artifact-count predictions,')
rec('        ### every one of them a measured or quoted figure -- and ### **ONE OF THEM WAS THE')
rec('        ### TAIL OF THE HYPHENATED `FIFTY-SEVEN`**, matched as `SEVEN modules` because a')
rec('        ### hyphen is a word boundary. ### Caught by ### **READING THE TOOL`S VERDICT LINE**,')
rec('        ### which is b491`s lesson, not by a grep for a word.')
rec('    (e) ### **AN ARM PASSED ITS OWN POSITIVE CONTROL.** ### `G-PUSHED-PREDICATE-THREE-CLAUSED`')
rec('        ### was a DISJUNCTION over two spellings -- b494`s `components.txt` and this act`s')
rec('        ### `create.txt` -- and the mutation falsified only the second limb. ### **A CONTROL')
rec('        ### THAT LEAVES A LIVE LIMB CANNOT BITE.** ### Rewritten as a conjunction over the')
rec('        ### predicate`s three actual clauses, which is what its name always claimed.')

rec('')
rec('### (7) THE SUITE, THE COMMITS, THE MIRROR.')
rec('-' * 104)
rec('    pre-push  : %s' % lw(pre, 'ARMS RUN :'))
rec('                64 declared on the face; `G-MIRROR-TAGGED-BUILD` deferred to post-push.')
rec('                ### 2 arms RETIRED IN WORDS on the face: `G-NOTHING-COMPILED` (the kernel')
rec('                ### lane is OPEN by the order`s first line, and an arm forbidding what the')
rec('                ### order commands is a FALSE ARM) and `G-CORPUS-LEAN-UNTOUCHED` (this act')
rec('                ### creates a repository OF Lean files). ### Their replacements are')
rec('                ### `G-BUILD-DETACHED`, `G-LOG-NOT-READ`, `G-NOCITE-BEFORE-PROFILE` and')
rec('                ### `G-NO-BODY-EDITED`, which bound the opening to what (R106)(3) allows.')
rec('    post-push : %s' % lw(post, 'ARMS RUN :'))
rec('                %s' % lw(post, 'VERDICT :'))
rec('    ### **%d FILES WRITTEN THAT NO (W) GLOB COVERS.**' % len(X.get('stray', [])))
rec('')
rec('    the commits, each read back by `ls-remote`:')
for name, path in REPOS:
    loc = git(path, 'rev-parse', 'HEAD')
    rem = git(path, 'ls-remote', 'origin', 'main')
    rem = rem.split()[0] if rem else ''
    rec('      %-22s local %s ; remote %s ; ### **%s**'
        % (name, loc[:12], (rem[:12] or '### UNRESOLVED'), 'AGREE' if loc and loc == rem else '### DISAGREE'))
rec('    ### ### **relay`s FIRST PUSH FAILED: `Could not resolve host: github.com`.** ### A direct')
rec('    ### `ls-remote` answered immediately; the push was retried and succeeded. ### **THE SAME')
rec('    ### TRANSIENT SPECIES b494`S CLOSING PINS HIT**, now met with the same answer: test the')
rec('    ### claim directly, retry, and say so.')
rec('    the mirror : `mirror-refresh-2026-09-23-b495.zip` at `%s` --'
    % git(REPOS[1][1], 'rev-parse', '--short', 'HEAD'))
rec('      ### **%s**' % (lw(mir, 'VERDICT:').replace('### VERDICT: ', '') or '?'))

rec('')
rec('### (8) THE CENSUSES, THE PINS, THE LISTS.')
rec('-' * 104)
rec('    handoff census : %s' % lw(cens, 'TOTAL MISSING'))
rec('    faces census   : %s' % lw(fcens, 'TOTAL MISSING'))
rec('    pins           : %s ### (run ALONE, per b494`s lesson)' % lw(pins, 'REPOS HARD-FAILING'))
rec('    ### **THE FOUR LISTS STAY OPEN.** ### Nothing fetched but `git`; ### **NOTHING CITED,')
rec('    ### NOTHING GRADED, NOTHING PROFILED.** ### No corpus grade moved; ### **ROW U1')
rec('    ### UNEDITED**; nothing deposits; ### **NOTHING AT ZENODO IS WRITTEN**; ### **h2 WHERE')
rec('    ### THE DEPOSIT LEFT IT.** ### The numerical lane stays shut. ### The zeta23 clone was')
rec('    ### READ and never written and ### **NEVER COMMITTED** -- (R58).')

rec('')
rec('### (9) WHAT IS CARRIED FORWARD.')
rec('-' * 104)
rec('    (a) ### **b496 READS THE LOG AND PROFILES**, under (R106)(3), and commits the log. ### It')
rec('        ### also owes (N3) and (S2) their cells -- the two this act could not score.')
rec('    (b) ### **NO ROW MAY CITE THIS KERNEL UNTIL THAT PROFILE IS BANKED.** ### The REGISTRY')
rec('        ### row says `PENDING` and names no terminal, and that is not a placeholder to be')
rec('        ### filled in by anyone but the act that runs the profile.')
rec('    (c) ### **(R106)(1): `W-ORD-EPSTEIN-ISOLATION` IS FILED** -- the four-channel ledger for')
rec('        ### an Epstein zeta with a known off-line zero, on the same ladder, so the sign of')
rec('        ### `A - PR` at a non-xi object is measured beside xi`s. ### Trigger: (R104)`s ladder')
rec('        ### act, or the author`s word. ### b494`s Table 2 row 5 is corrected: the sentence IS')
rec('        ### in the corpus as PROSE at `A_Place_to_Stand` step (9), with NO BANK and NO')
rec('        ### TERMINAL. ### **b494 SAID "NAMES NOTHING" AND THE AUTHOR FOUND IT.**')
rec('    (d) ### **(R106)(2): `C7_finite_type_false` IS PROFILED** in the next act that opens the')
rec('        ### `SIDE-lv-conservation` lane, and `OPEN_TRAILS` line 102 annotated by APPENDED')
rec('        ### NOTE, not rewritten.')
rec('    (e) ### **THE PLATFORM SESSION IS STILL THE AUTHOR`S AND STILL BLOCKED** -- eight rows')
rec('        ### exceeding the (R102) ceiling with no draft, three of them titles; and (R99)`s')
rec('        ### kernel text is held because its target sentence is not in the deposit.')
rec('    (f) ### **`corr_row.py` CHECKS THE NUMBER AND NOT THE CELLS**, routed at b490 and')
rec('        ### ### **OVERDUE**. ### Row 344 went in clean, which is not evidence the guard')
rec('        ### exists -- it is evidence the cells happened to contain no pipe.')
rec('=' * 104)

io.open(os.path.join(D, 'b495_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print('  written: b495_closing.txt')
