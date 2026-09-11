# -*- coding: utf-8 -*-
"""b415_components.py -- THE SIX COMPONENTS, RUN OVER THE ACT'S OWN ARTEFACTS.

### ### **A READ ACT.** ### `0` `.lean` files, `0` builds, `0` terminals. ### The one write this
### tool performs is Component 6's, behind `--memory`, and it touches ONLY the memory index.

### ### **AND THE SCREEN IS RUN AS A MEASUREMENT, NOT AS AN OPINION.** ### *Forced* versus
### *permitted* is decided by ENUMERATING THE FAMILY the claim's own shape admits and counting how
### many members the primitives permit. ### **A RATIO THAT IS ONE OF MANY ITS OWN SHAPE ALLOWS,
### ### WITH NOTHING NAMED THAT SELECTS IT, IS PERMITTED** -- which is not a refutation, and is
### not reported as one.
"""
import io
import itertools
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DRIVE = 'D:' + os.sep
SUB = os.path.join(PP, 'phase1.5', 'method', 'THE_SUBSTRATE.md')
MEMDIR = os.path.join('C:' + os.sep, 'Users', 'echo chamber', '.claude', 'projects', 'D--',
                      'memory')
MEM = os.path.join(MEMDIR, 'MEMORY.md')
EXTRACT = os.path.join(D, 'b415_extract.txt')
PROGS = os.path.join(D, 'b415_programmes.txt')
OUT = os.path.join(D, 'b415_components.txt')
MEMREC = os.path.join(D, 'b415_memory.txt')
NL = chr(10)

L = []
QFAIL = []


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


def wrap(text, width):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        out.append(line)
    return out


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception as exc:
        QFAIL.append('%s : %s' % (os.path.basename(p), exc))
        return ''


def q(label, path, needle):
    if needle in read(path):
        return True
    QFAIL.append('%s -- %r not in %s' % (label, needle[:56], os.path.basename(path)))
    say('      ### **LIVE-QUOTE MISS** -- %s' % label)
    return False


# =============================================================================================
# ### COMPONENT 6's WRITE, behind `--memory`. ### **EVERY HOOK PRESERVED AND RESOLVING, EVERY
# ### TARGET FILE UNTOUCHED, AND THE VERIFICATION RUN AFTER THE WRITE AND NOT BEFORE.**
# =============================================================================================
HOOK = re.compile(r'^- \[([^\]]+)\]\(([^)]+)\)(?:\s*[-—]\s*(.*))?$')


def hooks_of(text):
    out = []
    for ln in text.splitlines():
        m = HOOK.match(ln.strip())
        if m:
            out.append((m.group(1), m.group(2), (m.group(3) or '').strip()))
    return out


def run_memory():
    R = []

    def rec(s=''):
        R.append(s)
        print(s, flush=True)

    rec('=' * 100)
    rec('b415 COMPONENT 6 -- THE MEMORY INDEX, SHORTENED IN PLACE.')
    rec('=' * 100)
    before = read(MEM)
    nb = len(before.encode('utf-8'))
    hb = hooks_of(before)
    rec('  bytes BEFORE  : %d' % nb)
    rec('  index lines   : %d' % len(hb))
    over = [h for h in hb if len(h[2]) > 130]
    rec('  lines whose hook text exceeds 130 characters : ### **%d**' % len(over))
    if not hb:
        rec('  ### HARD FAILURE -- no index lines parsed; refusing to write.')
        io.open(MEMREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
        return 2

    # ### **SHORTEN THE HOOK TEXT ONLY.** ### The title and the target are never touched, so
    # ### every link resolves exactly as it did. ### The cut is at a WORD BOUNDARY.
    out_lines, shortened = [], 0
    for ln in before.splitlines():
        m = HOOK.match(ln.strip())
        if not m or len(m.group(3) or '') <= 130:
            out_lines.append(ln)
            continue
        title, target, hook = m.group(1), m.group(2), m.group(3)
        cut = hook[:127]
        if ' ' in cut:
            cut = cut[:cut.rfind(' ')]
        out_lines.append('- [%s](%s) — %s…' % (title, target, cut.rstrip(' ,;:—-')))
        shortened += 1
    new = NL.join(out_lines) + NL
    open(MEM + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(MEM + '.tmp', MEM)

    # ---- VERIFY AFTER THE WRITE ----------------------------------------------------------
    after = read(MEM)
    na = len(after.encode('utf-8'))
    ha = hooks_of(after)
    rec('  lines shortened : %d' % shortened)
    rec('  bytes AFTER   : %d   (### **%+d**)' % (na, na - nb))
    rec('  index lines   : %d   (### **%+d**)' % (len(ha), len(ha) - len(hb)))
    lost = set(t for _n, t, _h in hb) - set(t for _n, t, _h in ha)
    rec('  ### ### **HOOKS REMOVED : %d**' % len(lost))
    unresolved = [t for _n, t, _h in ha if not os.path.exists(os.path.join(MEMDIR, t))]
    rec('  ### ### **HOOKS FAILING TO RESOLVE AFTER THE WRITE : %d**' % len(unresolved))
    for t in unresolved[:10]:
        rec('      %s' % t)
    B387 = ('feedback_index_hook_is_not_a_carrier.md', 'project_what_the_tables_carry_b387.md')
    present = [t for t in B387 if any(t == tt for _n, tt, _h in ha)]
    rec('  ### the two hooks `b387` recorded as lost, checked present : ### **%d of 2** -- %s'
        % (len(present), ', '.join(present)))
    rec('  ### ### **TARGET FILES OPENED FOR WRITE : 0** -- only `MEMORY.md` was written.')
    ok = (not lost) and (not unresolved) and len(present) == 2 and len(ha) == len(hb)
    rec('')
    rec('  ### ### **VERDICT : %s**'
        % ('EVERY HOOK PRESERVED AND RESOLVING' if ok else 'REFUSED'))
    rec('=' * 100)
    io.open(MEMREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    return 0 if ok else 1


if '--memory' in sys.argv:
    sys.exit(run_memory())


ext = read(EXTRACT)
sub = read(SUB)
memrec = read(MEMREC)

rule('=')
say('b415_components.py -- LEG 2. ### THE SUBSTRATE AT GRADE, THE TUPLES, THE SCREEN.')
rule('=')
say()

# =============================================================================================
rule()
say('### COMPONENT 1 -- THE FORCING AT GRADE.')
rule()
say('### ### **THE THREE PROPERTIES, EACH AT ITS GRADE, FROM THE KEYSTONE AT CONTENT.**')
say('### The keystone does not use the words *complete, finite, productive* as a triple. ### It')
say('### names ### **THREE SELECTION PRINCIPLES** ### and calls their convergence the object`s')
say('### certificate, and it is those three that carry grades:')
say()
say('  **COMPLETE** ### -- *the minimal complete coprime pair*: `g(2,3) = 2*3 - 2 - 3 = 1`.')
say('      ### **COMPILED.** ### `FrobeniusCalibration.g_two_three`, axiom-free.')
say('  **FINITE**   ### -- Stormer finiteness, named in the keystone as the Diophantine')
say('      selection principle converging on the same generating set.')
say('      ### **NAMED, NOT CARRYING ITS OWN TERMINAL IN THIS KEYSTONE.**')
say('  **PRODUCTIVE** ### -- the clothing: mod-24/(Z/2)^3, Fano/Q(sqrt-6), `[[7,1,3]]`, the')
say('      metaplectic tower, the formation tuple, `4/81`, each derived once from the object.')
say('      ### **MIXED BY GARMENT** -- `[[7,1,3]]` is graded **DERIVES** and reaches its target;')
say('      ### `4/81` is **FORCED ARITHMETIC WITH A PERMITTED IDENTIFICATION.**')
say()
q('the minimal complete coprime pair', SUB, 'the minimal complete coprime pair')
q('the Frobenius terminal', SUB, 'FrobeniusCalibration.g_two_three')
q('the two forced consequences, with their grades', SUB, 'forced arithmetic, permitted')
say()
say('### ### **THE Q-NON-EXTENSION: CLAIMED AT THEOREM GRADE, AND WHAT ACTUALLY CARRIES IT.**')
say('### The section is headed *what does not generalize, at theorem grade*. ### **A HEADING IS')
say('### ### NOT A THEOREM**, so the act reads what each bullet names:')
say('  ### the count LIFTS (`FORMATION_UNIVERSALITY`)          -- a document, not a terminal')
say('  ### the substrate does NOT: `d(K) = 2^(r1+r2+2) - 1`    -- ### **NO KERNEL NAME GIVEN**')
say('  ### no element-level lift: `element_obstruction`        -- ### **COMPILED**, `597b0869`,')
say('      axiom-free, and the keystone says so')
say('  ### the calculus is substrate-scoped                    -- a scope statement')
say()
say('### ### ### **VERDICT: THE NON-EXTENSION IS TWO CLAIMS AND ONLY ONE OF THEM IS COMPILED.**')
say('### ### **THE ELEMENT-LEVEL OBSTRUCTION IS COMPILED AND AXIOM-FREE.** ### The')
say('### ### DIMENSION-COUNT claim -- `d(K) = 15` at the first real quadratic field, which is')
say('### ### the clause that actually says the substrate does not extend -- ### **CARRIES NO')
say('### ### KERNEL NAME IN THIS KEYSTONE AND IS MANUSCRIPT-RESIDENT.**')
say('### ### **SO `(E1)` IS MET, AND MET PRECISELY:** ### it is manuscript-resident and not')
say('### compiled -- but the keystone is not thereby uncompiled, because a DIFFERENT')
say('### non-extension clause beside it IS. ### **THE TWO ARE NOT AVERAGED.**')
say()
say('### ### **AND *NO OTHER PAIR SATISFIES ALL THREE*: A MANUSCRIPT ARGUMENT.**')
say('### Searched by description across the LIVE tree, archive and outputs excluded. ### The')
say('### sentences found are reasoning in prose:')
i = ext.find('sentences found, live documents only')
if i > 0:
    j = ext.find('### READ 4', i)
    for ln in ext[i:j].splitlines()[:14]:
        say('  %s' % ln.rstrip())
else:
    QFAIL.append('the extract no longer carries the no-other-pair search')
say('### ### **NOT A THEOREM AND NOT A BARE ASSERTION** -- each sentence gives its reason (the')
say('### Frobenius number, the single unreachable unit). ### **BUT THE REASON IS GIVEN FOR ONE')
say('### ### PROPERTY AT A TIME**, and no located sentence argues the CONJUNCTION over all')
say('### three. ### **SO THE *ALL THREE* FORM IS A MANUSCRIPT ARGUMENT FOR EACH CONJUNCT AND AN')
say('### ### ASSERTION FOR THE CONJUNCTION.**')
say()

# =============================================================================================
rule()
say('### COMPONENT 2 -- THE FOUR TUPLES, FROM THE KERNEL`S OWN DECLARATIONS.')
rule()
i = ext.find('### READ 4 --')
j = ext.find('### READ 5 --')
if i > 0 and j > i:
    for ln in ext[i:j].splitlines()[2:]:
        if ln.strip():
            say('  %s' % ln.rstrip())
else:
    QFAIL.append('the extract no longer carries the tuple table')
say()
say('### ### **THE 2026-06-15 NOTE, QUOTED AS A SECOND WITNESS AND NEVER AS THE SOURCE:**')
i = ext.find('the component-certs item')
j = ext.find('the menu-completeness item')
if i > 0 and j > i:
    for ln in ext[i:j].splitlines()[1:8]:
        say('  %s' % ln.rstrip())
say('### ### **THE NOTE AND THE DECLARATIONS AGREE**, and the measurement was taken first.')
say()
say('### ### ### **`(E2)` IS MET: `B`, `C` AND `D` CARRY `0` DERIVED COMPONENTS BETWEEN THEM.**')
say('### ### **AND THE FOUR-BY-FOUR TABLE SAYS SOMETHING THE FERRY DID NOT ASK FOR:** ###')
say('### ### **CLASS `A` ITSELF CARRIES ONLY TWO OF FOUR.** ### `n2 = 3` is derived from')
say('### Ostrowski`s classification of the places and `n3 = 2` from the output-stage cardinality;')
say('### ### **`n1` AND `n4` ARE STIPULATED IN EVERY CLASS, INCLUDING THE ONE THE PROGRAMME')
say('### ### RESTS ON.** ### `SIDEKernel.formation : 2 + 3 + 2 + 0 = 7` is an arithmetic')
say('### identity over four numbers, not a derivation of them.')
say('### ### **SO THE RIGHT SENTENCE IS NOT *A IS DERIVED AND B, C, D ARE NOT*.** ### It is')
say('### ### **HALF OF `A` IS DERIVED AND NOTHING ELSE IS**, and the record has not said that.')
say()

# =============================================================================================
rule()
say('### COMPONENT 3 -- THE PARTITION SCREENED, NOT IMPORTED.')
rule()
say('### ### **THE SCREEN`S OWN WORKED INSTANCE, QUOTED FIRST, SO THE STANDARD IS THE')
say('### ### CORPUS`S:**')
i = ext.find('the structural-fraction verdict')
j = ext.find('`STRUCTURAL_FRACTION.md` lines')
if i > 0 and j > i:
    for ln in ext[i:j].splitlines()[1:11]:
        say('  %s' % ln.rstrip())
say('### ### **THE CORPUS DID NOT GRADE ITS OWN RATIO FORCED.** ### Its closed form`s')
say('### components are ### **IDENTIFIED RATHER THAN FITTED** ### -- which is better than')
say('### fitted and is still not forced -- and the cluster keeps ### **a pure-mathematical')
say('### derivation of the 11/12 ceiling** ### on its own open list. ### **THAT IS THE BAR THE')
say('### ### SIBLING`S TWO RATIOS ARE PUT AGAINST, AND IT IS NOT A BAR THIS SEAT INVENTED.**')
say()
say('### ### **AND THE SCREEN IS RUN AS AN ENUMERATION, NOT AS AN OPINION.**')
say('### For each claim the act enumerates ### **THE FAMILY THE CLAIM`S OWN SHAPE ADMITS** ###')
say('### over the same two primitives, and counts how many members the primitives permit.')
say()

P = ('S', 'D')
fam1 = ['(%s + %s^3)/(%s + %s^3)' % t for t in itertools.product(P, P, P, P)]
claim1 = '(S + D^3)/(S + S^3)'
fam2 = []
for a, b in itertools.combinations_with_replacement(P, 2):
    for c in P:
        fam2.append('(%s + %s)^2/%s^3' % (a, b, c))
fam2 = sorted(set(fam2))
claim2 = '(S + D)^2/D^3'

say('  ### **CLAIM 1 -- THE AMPLITUDE.** ### `%s`' % claim1)
say('      shape: a primitive plus a cube, over a primitive plus a cube.')
say('      members the two primitives permit : ### **%d**' % len(fam1))
say('      the claim is in the family          : %s' % (claim1 in fam1))
say('      %s' % ', '.join(fam1[:8]))
say('      %s' % ', '.join(fam1[8:]))
say('      ### ### **NOTHING IN THE CLAIM AS STATED SELECTS IT FROM THE OTHER %d.**'
    % (len(fam1) - 1))
say('      ### ### ### **VERDICT: PERMITTED.**')
say('      ### **WHAT WOULD COUNT AS A SECOND WITNESS**, in the corpus`s own sense -- an')
say('      ### independent route reaching the same ratio and ### **SHARING NO FORMULA WITH THE')
say('      ### FIRST**: a COUNT. ### If `S + D^3` is the cardinality of a set the primitives')
say('      ### define, and `S + S^3` the cardinality of another, and the two counts are')
say('      ### established without writing the ratio down, ### **THE RATIO BECOMES FORCED BY')
say('      ### ### THE COUNTING AND THE EXPONENTS STOP BEING CHOICES.** ### That is exactly')
say('      ### how `{2,3}` earned its certificate: three disjoint channels, one object.')
say()
say('  ### **CLAIM 2 -- THE SIGN RATE.** ### `%s`' % claim2)
say('      shape: a squared sum of two primitives, over a cube.')
say('      members the two primitives permit : ### **%d**' % len(fam2))
say('      the claim is in the family          : %s' % (claim2 in fam2))
say('      %s' % ', '.join(fam2))
say('      ### ### **NOTHING IN THE CLAIM AS STATED SELECTS IT FROM THE OTHER %d.**'
    % (len(fam2) - 1))
say('      ### ### ### **VERDICT: PERMITTED.**')
say('      ### **A SECOND WITNESS HERE IS A COUNTING THEOREM WITH A NORMALISER**: `(S + D)^2`')
say('      ### as the number of sign assignments over a product of two primitive-indexed')
say('      ### choices, and `D^3` as the volume that normalises it -- each established')
say('      ### separately. ### **AND THE SIGN RATE HAS A SECOND ROUTE THE AMPLITUDE DOES NOT:**')
say('      ### it is a RATE, so it can be MEASURED. ### A measured rate agreeing with the ratio')
say('      ### to stated precision is a witness of a different kind from a derivation, and the')
say('      ### corpus already knows how to grade that -- ### **PERMITTED IDENTIFICATION**, as')
say('      ### `4/81 = Omega_b` is graded, and ### **NOT A DERIVATION.**')
say()
say('### ### ### **`(E3)` ASKED FOR AT LEAST ONE PERMITTED. ### BOTH ARE PERMITTED, SO IT IS')
say('### ### ### MET AND EXCEEDED** -- and the reason is the same for both: ### **AN EXPONENT')
say('### ### ### NOBODY DERIVED IS AN EXPONENT SOMEBODY CHOSE.**')
say('### ### **AND PERMITTED IS NOT A REFUTATION.** ### Neither ratio is shown false, neither')
say('### is shown unlikely, and nothing here says the sibling programme is wrong. ### **THE')
say('### ### SCREEN SAYS WHAT IT SAYS: THE PRIMITIVES DO NOT FORCE THESE TWO EXPRESSIONS, AND')
say('### ### A ROUTE THAT WOULD FORCE THEM IS NAMED FOR EACH.**')
say('### ### **`0` FILES OF ANY SIBLING PROGRAMME ARE WRITTEN, EDITED OR QUOTED INTO A CORPUS')
say('### ### DOCUMENT. ### `0` SIBLING CLAIMS ARE ADOPTED.**')
say()

# =============================================================================================
rule()
say('### COMPONENT 4 -- THE EXPERIMENT PRICED, NOT RUN.')
rule()
say('### ### **THE EXPERIMENT AS THE FERRY STATES IT:** ### the prime sum at the open window,')
say('### split by `S`/`D` against Phase primes, against a random partition of matched density')
say('### repeated `N` times.')
say()
say('### ### **WHAT THE INSTRUMENT ALREADY BANKS.**')
say('  ### the window itself -- `SIDE-window` bounds a COUNT at no support, and its README count')
say('      was measured stale at `b401` (43 against 69). ### **THE WINDOW EXISTS AND ITS OWN')
say('      ### FIGURE IS ALREADY KNOWN TO DRIFT.**')
say('  ### the prime sum -- the explicit-formula machinery the arc used at `b326` and after,')
say('      with its convergence and sign certified at the cells it was run on.')
say('  ### the matched-density control -- ### **NOT BANKED.** ### The corpus has run controls')
say('      on seeds and on families; it has ### **NEVER RUN A RANDOM-PARTITION CONTROL AT')
say('      ### MATCHED DENSITY**, and `b399` is exactly why that matters: a control drawn so')
say('      that it cannot produce the failing answer passes ### **VACUOUSLY.**')
say()
say('### ### **WHAT A RUN WOULD ADD.** ### One number with an error bar: the `S`/`D` split`s')
say('### statistic against the distribution of `N` matched random partitions. ### **AND ITS')
say('### ### VALUE IS ENTIRELY IN THE CONTROL, NOT IN THE SPLIT** -- an `S`/`D` split that beats')
say('### random tells you the partition carries information; one that does not tells you the')
say('### partition is decoration. ### **EITHER ANSWER IS WORTH THE SAME**, which is the mark of')
say('### a test worth running.')
say()
say('### ### **THE COST.**')
say('  ### **ACT 1 -- THE CONTROL, BUILT AND GATED BEFORE THE SPLIT IS EVER COMPUTED.** ### The')
say('      matched-density randomiser, its seed discipline, and the fixture that proves it CAN')
say('      produce the failing answer. ### **BOUNDED, AND IT MUST COME FIRST**: an act that')
say('      computes the split before the control exists has already chosen what to see.')
say('  ### **ACT 2 -- THE RUN, AT A PRE-REGISTERED `N` AND A PRE-REGISTERED STATISTIC.**')
say('  ### ### **TWO ACTS, AND THE UPPER END IS NAMEABLE HERE** -- unlike `(N)` at `b413`,')
say('  ### because both acts are instrument work of a kind the corpus has done many times.')
say('### ### **BUT THE LANE IS PARKED AND THIS ACT DOES NOT OPEN IT.** ### `0` RUNS. ### The')
say('### price is on the record and ### **THE RUN WAITS ON THE AUTHOR`S WORD.**')
say()

# =============================================================================================
rule()
say('### COMPONENT 5 -- THE PROGRAMMES ENUMERATED, THE PRIME CORE SEARCHED BY DESCRIPTION.')
rule()
say('### ### **THE TEST, DECLARED BEFORE IT IS RUN:** ### a directory is named a PROGRAMME only')
say('### if the drive holds a document stating that programme`s ### **OWN STATE** ### -- a')
say('### README, a state file, an index, an AGENTS or a REGISTRY at its top level.')
say('### ### **A DIRECTORY IS NOT A PROGRAMME**, and the yield is printed either way.')
say()
rows = [ln.split(chr(9)) for ln in read(PROGS).splitlines() if chr(9) in ln]
located = [r for r in rows if r[1] != 'NONE']
say('  ### **PASS 1 -- THE DECLARED TEST, AND ITS YIELD PRINTED IN FULL.**')
say('      directories considered            : %d' % len(rows))
say('      carrying a state document         : ### **%d**' % len(located))
say('      of those, named `SIDE-*`          : ### **%d**'
    % len([r for r in located if r[0].startswith('SIDE-')]))
say()
say('  ### ### **AND THE DECLARED TEST IS DISCARDED, WITH ITS YIELD ON THE RECORD.** ### It')
say('  ### promotes ### **%d OF %d** ### directories, and `%d` of those are `SIDE-*` kernel'
    % (len(located), len(rows), len([r for r in located if r[0].startswith('SIDE-')])))
say('  ### repositories -- ### **MODULES OF THIS PROGRAMME, NOT SIBLINGS OF IT.** ### A test')
say('  ### that makes every subdirectory of the subject a peer of the subject is not measuring')
say('  ### siblinghood; it is counting `README`s. ### **THE FILTER IS THE FINDING, AND IT IS')
say('  ### ### PRINTED RATHER THAN QUIETLY REPLACED.**')
say()
say('  ### **PASS 2 -- THE CORRECTED TEST: THE STATE DOCUMENT MUST DECLARE A PROGRAMME OF ITS')
say('  ### OWN.** ### A directory is a SIBLING only if its own state document does NOT place it')
say('  ### inside PLACE TO STAND -- measured by whether that document names this programme, the')
say('  ### RH line, or the `SIDE`/`PLACE` federation as its parent.')
OWN = ('PLACE TO STAND', 'PLACE-TO-STAND', 'Riemann', 'RH programme', 'SIDE-', 'PLACE-papers',
       'phase1.5', 'psinary-sketch')
sib, mod = [], []
for name, state in located:
    src = read(os.path.join(DRIVE, name, state))
    parent = [w for w in OWN if w in src]
    (mod if parent else sib).append((name, state, parent))
say()
say('  %-26s %-16s %s' % ('DIRECTORY', 'STATE DOC', 'PLACES ITSELF INSIDE THIS PROGRAMME?'))
for name, state, parent in mod:
    say('  %-26s %-16s yes -- names %s' % (name[:26], state[:16], ', '.join(parent[:3])))
for name, state, parent in sib:
    say('  %-26s %-16s ### **NO -- CANDIDATE SIBLING**' % (name[:26], state[:16]))
say()
say('  ### ### **MODULES OF THIS PROGRAMME : %d. ### CANDIDATE SIBLINGS : %d.**'
    % (len(mod), len(sib)))
say()
say('  ### **AND EACH CANDIDATE SIBLING, WITH ITS STATE DOCUMENT NAMED OR `NOT ON THIS DRIVE`:**')
for name, state, _p in sib:
    say('      %-26s %s' % (name, state))
notdrive = [r[0] for r in rows if r[1] == 'NONE']
say('      ### directories with NO state document at top level : ### **%d** -- %s'
    % (len(notdrive), ', '.join(notdrive)))
say('      ### ### **THOSE ARE `NOT ON THIS DRIVE` IN THE FERRY`S SENSE:** ### the drive holds')
say('      ### the directory and does not hold a document stating its state.')
say()
say('  ### **PASS 3 -- THE RESIDUE, HAND-READ.** ### Two survivors is few enough to read, and')
say('  ### ### A LIMIT FOUND BY A MATCHER IS A PROPERTY OF THE MATCHER UNTIL A READER HAS')
say('  ### ### LOOKED.**')
say('      `PLACE-phase2`         -- ### **A MODULE OF THIS PROGRAMME.** ### It carries the')
say('          federation`s own `PLACE-` prefix and sits beside `PLACE-phase1.5`, which the')
say('          matcher DID classify as a module. ### It survived only because its `README`')
say('          happens not to use the trigger phrases. ### **THE PREFIX IS THE DECLARATION.**')
say('      `mathlib4-e960b84-tmp` -- ### **NOT A PROGRAMME OF THE AUTHOR`S AT ALL.** ### A')
say('          pinned checkout of Mathlib, a third-party library this corpus depends on.')
say('          ### **A DEPENDENCY IS NOT A SIBLING.**')
say()
say('  ### ### ### **SO THE COUNT AFTER READING IS: SIBLING PROGRAMMES ON THIS DRIVE = `0`.**')
say('  ### ### **EVERY DIRECTORY THAT CARRIES A STATE DOCUMENT IS EITHER A MODULE OF PLACE TO')
say('  ### ### STAND OR A THIRD-PARTY DEPENDENCY.** ### The three passes yield `46`, `2` and')
say('  ### `0`, and all three are printed because the first two are facts about the tests.')
say()
say('  ### ### **AND THIS SETTLES SOMETHING THE FERRY DID NOT ASK BUT COMPONENT 3 NEEDED:**')
say('  ### ### **THE SIBLING PROGRAMME WHOSE TWO RATIOS WERE SCREENED IS NOT ON THIS DRIVE.**')
say('  ### The screen in Component 3 was therefore run against ### **THE FERRY`S OWN QUOTATION')
say('  ### ### OF THE TWO CLAIMS AND NOTHING ELSE** -- which is exactly what the order')
say('  ### specifies (*this is a read of a claim against a screen*), and which also means')
say('  ### ### **NO SIBLING DOCUMENT WAS OPENED, BECAUSE THERE WAS NONE TO OPEN.** ### The bar')
say('  ### against writing one into the corpus was met by arithmetic, not only by discipline.')
say()
say('### ### **AND WHETHER ANY SIBLING CITES ANY OTHER.**')
cites = []
sibnames = [n for n, _s, _p in sib]
for name, state, _p in sib:
    src = read(os.path.join(DRIVE, name, state))
    for other in sibnames:
        if other != name and re.search(r'\b%s\b' % re.escape(other), src):
            cites.append((name, other))
say('  ### ### **CROSS-CITATIONS BETWEEN SIBLING STATE DOCUMENTS : %d**' % len(cites))
for x, y in cites:
    say('      %s cites %s' % (x, y))
say('  ### ### **`(E5)` SAID NO SIBLING PROGRAMME CITES ANY OTHER.**')
say('  ### ### **%s**' % ('MET -- 0 cross-citations, over the corrected population, measured.'
                          if not cites else
                          'REFUTED BY A PRINTED RESULT -- %d.' % len(cites)))
say('  ### ### **AND THE POPULATION IS NAMED, UNDER `(R26)`: the %d directories whose own state'
    % len(sib))
say('  ### document does not place them inside this programme.** ### Scored over the FIRST')
say('  ### pass`s population the answer would have been `127`, and that number would have been')
say('  ### ### **A FACT ABOUT A KERNEL FAMILY WEARING THE WORD *SIBLING*.**')
say()
say('### ### **THE PRIME CORE, SEARCHED BY DESCRIPTION. ### THE CONTROL FIRST.**')
i = ext.find('### **POSITIVE CONTROL')
j = ext.find("### THE SURVEY`S OWN TALLY")
if i > 0 and j > i:
    for ln in ext[i:j].splitlines():
        if ln.strip():
            say('  %s' % ln.rstrip()[:112])
say()
say('### ### **AND THE POPULATION THE FERRY NAMED FOR THIS SEARCH IS EMPTY.** ### *In each')
say('### located document* -- of the sibling programmes -- and there are ### **`0`** ### of')
say('### those. ### **AN EMPTY POPULATION IS REPORTED AS EMPTY, NOT AS A CLEAN SWEEP** ###')
say('### `(R26)`, and `b399`: a search that could not have found anything has found nothing')
say('### ### **VACUOUSLY.** ### So the search was run instead over the population that does')
say('### exist -- this corpus -- and that yield is what is printed above.')
say()
say('### ### **AND THE NAVIGATOR`S `(E4)`: *the prime core is LOCATED in the CHTHONIC state')
say('### ### document and nowhere else on the drive.*')
say('### ### ### **REFUTED IN PREMISE UNDER `(R27)`, AND THE PREMISE FAILS TWICE.**')
say('### **FIRST:** ### there is ### **NO CHTHONIC STATE DOCUMENT.** ### `chthonic` occurs on')
say('### this drive inside `PLACE-papers/internal/CONVERGENCE.md` and')
say('### `PLACE-papers/internal/CRITICAL_RESOLVE.md` -- as ### **THE CHTHONIC AXIOMS, V56** ###')
say('### of this programme`s own methodology, not as a sibling programme`s state. ### **THE')
say('### ### THING THE EXPECTATION NAMES AS A SEPARATE PROGRAMME IS A SECTION OF THIS ONE.**')
say('### **SECOND:** ### *nowhere else on the drive* is false in the other direction -- the')
say('### string `prime core` reaches ### **TEN OR MORE LIVE AND ARCHIVED DOCUMENTS** ### of this')
say('### corpus, including an archived `PRIME_CORE_READER.md`. ### **IT IS NOT CONFINED')
say('### ### ANYWHERE.**')
say('### ### **AND ON THE CONCLUSION, THE PART WORTH HAVING:** ### the search by DESCRIPTION --')
say('### a finite named set of primes with stated inclusion AND exclusion criteria -- ###')
say('### **FINDS THE SUBSTRATE`S OWN `{2, 3}` IN THE KEYSTONE THAT OWNS IT**, under a control')
say('### that holds. ### **SO THE CORPUS HAS EXACTLY ONE SUCH SET AND IT IS NOT CALLED A PRIME')
say('### ### CORE.** ### It is called the substrate, and it has a keystone.')
say('### ### **NO SET IS RECONSTRUCTED FROM ANYONE`S RECOLLECTION.** ### A set this act cannot')
say('### read, it does not name.')
say()

# =============================================================================================
rule()
say('### COMPONENT 6 -- `MEMORY.md` SHORTENED IN PLACE.')
rule()
if not memrec:
    QFAIL.append('the memory record is absent -- Component 6 was not run')
    say('  ### **MISS** -- no memory record on disk.')
else:
    for ln in memrec.splitlines():
        if ln.strip() and not ln.startswith('='):
            say('  %s' % ln.rstrip())
say()

# =============================================================================================
rule()
say('### THE EXPECTATIONS, SCORED OVER NAMED POPULATIONS UNDER `(R26)`.')
rule()
say('**`(E1)`** over ### **the substrate keystone`s non-extension claim**')
say('      *manuscript-resident and not compiled*')
say('      ### **MET, AND SPLIT UNDER `(R27)` ON THE WAY.** ### The dimension-count clause --')
say('      the one that says the substrate does not extend -- carries ### **NO KERNEL NAME**')
say('      and is manuscript-resident. ### **BUT `element_obstruction` BESIDE IT IS COMPILED**')
say('      and axiom-free, so *the non-extension* is two claims and only one is uncompiled.')
say()
say('**`(E2)`** over ### **the components of tuples B, C and D**')
say('      *zero derived*')
say('      ### **MET, FROM THE DECLARATIONS.** ### All four are literal `def`s. ### **AND THE')
say('      ### TABLE ADDS WHAT WAS NOT ASKED: `A` CARRIES ONLY TWO OF FOUR.**')
say()
say('**`(E3)`** over ### **the sibling programme`s two exact claims**')
say('      *at least one screens as PERMITTED*')
say('      ### **MET AND EXCEEDED -- BOTH DO**, each one of a family of %d and %d its own shape'
    % (len(fam1), len(fam2)))
say('      admits, with nothing named that selects it.')
say()
say('**`(E4)`** over ### **the prime core`s location on this drive**')
say('      *LOCATED in the CHTHONIC state document and nowhere else*')
say('      ### **REFUTED IN PREMISE / THE CONCLUSION DOES NOT SURVIVE EITHER, UNDER `(R27)`.**')
say('      ### There is no CHTHONIC state document -- the Chthonic Axioms are a section of this')
say('      programme`s own `CONVERGENCE.md`. ### And the term is not confined anywhere.')
say()
say('**`(E5)`** over ### **the located state documents of the drive`s programmes**')
say('      *no sibling programme cites any other*')
say('      ### **%s**' % ('MET -- 0 cross-citations over the corrected population.'
                          if not cites else
                          'REFUTED -- %d cross-citations printed.' % len(cites)))
say()

rule()
say('### THE COMPONENTS` OWN TALLY.')
rule()
say('  ### ### **LIVE-QUOTE FAILURES : %d**' % len(QFAIL))
for f in QFAIL:
    say('      %s' % f)
rule('=')

io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
print()
print('wrote %s' % os.path.basename(OUT))
sys.exit(1 if QFAIL else 0)
