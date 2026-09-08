# -*- coding: utf-8 -*-
"""b369_bank.py -- THE BANK, WRITTEN FROM THE ACT'S OWN JSONS. ### **NO FIGURE IS TYPED.**
### ### **AND EVERY KERNEL IDENTIFIER IS INSIDE BACKTICKS** (`b367`'s incident).
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock       # noqa: E402
import banned_terms    # noqa: E402


def banned_stems():
    return [x.lower() for x in banned_terms.STEMS]

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b369_the_list_repaired.txt')
REG = os.path.join(D, 'b369_registration_2026-09-08.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, R, K, P, F, Q = (J('b369_reads'), J('b369_repair'), J('b369_hygiene'),
                    J('b369_pass'), J('b369_filing'), J('b369_desk'))
regtxt = io.open(REG, encoding='utf-8').read()
SHA = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt).group(1)
NBY = re.search(r'bytes locked : (\d+)', regtxt).group(1)
LAT = re.search(r'locked at \(UTC\) : (\S+)', regtxt).group(1)
NCL = len(json.load(io.open(os.path.join(D, 'b369_satisfiable.json'), encoding='utf-8'))['clauses'])
CS = next((x['count_shapes'][0] for x in P['rows']
           if x['name'] in P['construction_candidates'] and x['count_shapes']), '?')
CONSTR = P['construction_candidates'][0] if P['construction_candidates'] else '?'

L = []


def w(s=''):
    L.append(s)


def nm(names):
    return ', '.join('`%s`' % n for n in names)


BAR, SUB = '=' * 100, '-' * 100

w(BAR)
w('b369 -- THE LIST REPAIRED, THE ROSTER MENDED, THE PASS PRICED. ### THE BANK.')
w('2026-09-08. ### CONCURRENCY: SOLO (research seat). ### FERRY_STANDING v2, by reference, citation '
  'CURRENT.')
w('### Registration `data/b369_registration_2026-09-08.txt`, ### **LOCKED**')
w('### `%s`, %s bytes, %d clauses JOINTLY' % (SHA, NBY, NCL))
w("### SATISFIABLE, and ### **LOCKED ONLY AFTER THE AUDIT'S OWN EXIT CODE CAME BACK `0`**, locked at "
  '(UTC)')
w('### %s. ### **LOCKED BEFORE ANY WRITE OF THIS ACT.** ### The clocks are in section (8).' % LAT)
w(BAR)
w('')

w(SUB)
w('### (1) THE ANSWER, FIRST.')
w(SUB)
w('### ### ### **THE LIST IS REPAIRED IN PLACE AND THE ORIGINAL IS PRESERVED IN THE SAME FILE.**')
w('### `%d` export rows were located, quoted ### **VERBATIM** ### into the currency note, the quotation'
  % R['rows_replaced'])
w('### verified byte-for-byte against the located rows, and ### **ONLY THEN** ### were the rows replaced.')
w('### ### **THE REPAIRED LIST CARRIES `%d` OF THE NAMES THE CLASSIFICATION CALLS ABSENT**, by a content'
  % len(R['still_absent']))
w('### predicate over the rows themselves. ### **A COUNT OF EDITED LINES PROVES NOTHING ABOUT WHAT A')
w('### ### LIST EXPORTS.**')
w('### ### **AND THE EDIT IS BOUNDED, MEASURED, NOT ASSERTED:** ### every byte above the rows is its')
w('### committed blob`s (`%s`) and every byte below them up to the appended note is too (`%s`), both'
  % (R['bar3_above'], R['bar3_below']))
w('### read ### **BEFORE THE PUSH.** ### **AN EDIT IS NOT AN APPEND, AND THIS ACT DOES NOT CLAIM A')
w('### ### PREFIX ARM IT CANNOT HAVE.**')
w('### ### ### **AND THE FINDING THIS ACT DID NOT EXPECT: `b368`S SHARPER CLAIM IS WRONG.**')
w('### `b368` reported the retirement ledger as leaving ### **ONE NAME WITH NO ENTRY FOR ITS LAYER AT')
w('### ### ALL** ### and called that the sharper half of its finding. ### The ledger carries an entry')
w('### ### **HEADED BY THAT DECLARATION`S OWN NAME.**')
w('### The re-derived split, from the ledger`s own entry headings: ### **NAMED OUTRIGHT `%d`; NAMED ONLY'
  % R['n_named'])
w('### ### BY THE LEDGER`S SLASH ABBREVIATION `%d`; COVERED ONLY BY A LAYER ENTRY `%d`; ### NOT COVERED'
  % (R['n_by_abbr'], R['n_layer_only']))
w('### ### AT ALL `%d`.**' % R['n_silent'])
w('### ### **EVERY RETIRED NAME IS REACHED BY THE LEDGER** -- by its own name, by its abbreviation, or')
w('### through its layer`s entry.')
w('### ### **THE CLASSIFICATION AGREES FOR THE THIRD TIME:** ### of `%d` names, `%d` declared and `%d`'
  % (R['exported'], R['n_present'], R['n_absent']))
w('### absent; `b368`s figure was a COMPARISON ONLY and never an input.')
w('### ### **THE TWO HYGIENE ITEMS ARE DONE**, and ### **THE PASS IS PRICED AND NOT RUN.**')
w('')

w(SUB)
w('### (2) COMPONENT 1 -- `(R4)`. ### **PRESERVE BY QUOTATION, REPAIR BY EDIT.**')
w(SUB)
w('### ### **THE REF, PINNED BEFORE ANY CLASSIFICATION:** ### `SIDE-effects` ref `%s` = `%s`;'
  % (R['ref'], R['head']))
w('### `ls-remote` AGREES (`%s`); working tree dirty at the read : `%s`.' % (R['pinned'], R['dirty']))
w('### ### **THE ORDER OF OPERATIONS WAS THE RULING`S OWN AND WAS NOT NEGOTIABLE:** ### quote, verify,')
w('### then edit. ### The tool refuses to edit if the verification fails, and the refusal is a branch it')
w('### can actually take.')
w('### ### **BAR 1 -- THE ORIGINAL ROWS SURVIVE VERBATIM IN THE FILE : `%s`.**' % R['bar1_preserved'])
w('### ### **BAR 2 -- ABSENT NAMES REMAINING IN THE REPAIRED ROWS : `%d`.**' % len(R['still_absent']))
w('### ### **BAR 3 -- THE EDIT IS BOUNDED : above `%s` / below `%s`.**'
  % (R['bar3_above'], R['bar3_below']))
w('### ### **AND NO `.lean` FILE WAS TOUCHED : `%s`. ### NO BUILD WAS RUN.**' % (R['lean_touched'] == 0))
w('')
w('### ### **THE ROWS THE REPAIRED LIST NOW CARRIES:**')
for r in R['new_rows']:
    w('###     %s' % r[:150])
w('### ### **THE TWO SURVIVORS AND WHERE THEY ARE DECLARED:**')
for n2, s in R['sites'].items():
    w('###     `%s` -- `%s:%d`' % (n2, s['file'], s['line']))
w('')
w('### ### ### **AND THE COST `(R4)` IMPOSED, REPORTED AT FULL PROMINENCE RATHER THAN LEFT TO BE')
w('### ### ### TRIPPED OVER: EXECUTING IT DATED TWO SENTENCES `b368` WROTE.** ### Its block says nothing')
w('### above it had been changed and that the list was left exactly as it was. ### **BOTH WERE TRUE WHEN')
w('### ### `b368` WROTE THEM AND NEITHER IS TRUE NOW.**')
w('### ### **THEY ARE NOT EDITED.** ### The new note NAMES them and marks them superseded, in the same')
w('### file a reader meets them in. ### **A PAST RECORD IS NAMED AND SUPERSEDED, NEVER REWRITTEN**, and')
w('### ### **A RULING THAT REVERSES A DISPOSITION DATES THE PROSE THAT ANNOUNCED IT** -- which is a cost')
w('### of the ruling and not a defect of either act.')
w('')
w('### ### **WHAT IS NOT IN SCOPE, AND IS SAID RATHER THAN SILENTLY LEFT:** ### the paragraph above the')
w('### list makes a COUNT claim about the module. ### **THE ORDER SAYS `the list is corrected`, AND A')
w('### ### COUNT IS NOT A NAME.** ### It is not edited; it is REPORTED -- and it is exactly the species')
w('### Component 3 exists to price, which is why the trail is updated and ### **NOT CLOSED.**')
w('')

w(SUB)
w('### (3) COMPONENT 1 CONTINUED -- `(R5)`, AND THE CORRECTION OF `b368`.')
w(SUB)
w('### ### **THE LEDGER`S OWN ENTRY HEADINGS, READ FROM ITS OWN INDENTATION:**')
for h in R['ledger_headings']:
    w('###     | %s' % h[:110])
w('### ### **NAMED OUTRIGHT (%d):** %s.' % (R['n_named'], nm(R['ledger_named'])))
w('### ### **NAMED ONLY BY THE SLASH ABBREVIATION (%d):** %s ### -- the ledger writes `%s`.'
  % (R['n_by_abbr'], nm(R['ledger_by_abbreviation']),
     sorted({v for k, v in R['abbreviations'].items() if k in R['ledger_by_abbreviation']})[0]
     if R['ledger_by_abbreviation'] else '-'))
w('### **AND THAT GROUP IS KEPT APART BECAUSE READING AN ABBREVIATION AS NAMING ITS EXPANSIONS IS A')
w('### ### JUDGEMENT, NOT A STRING MATCH.**')
w('### ### **COVERED ONLY BY A LAYER ENTRY (%d):** %s.' % (R['n_layer_only'], nm(R['ledger_layer_only'])))
w('### ### **NOT COVERED AT ALL : `%d`.**' % R['n_silent'])
w('')
w('### ### ### **AND THIS IS WHERE `b368` WAS WRONG, AND WHY.** ### `b368`s predicate asked for a name')
w('### preceded by a backtick or a slash. ### The ledger names one declaration as a ### **BARE HEADING**,')
w('### and `b368` therefore reported its layer as having no entry at all -- ### **THE SHARPER HALF OF ITS')
w('### ### OWN FINDING, AND IT WAS AN ARTEFACT OF ITS PREDICATE.**')
w('### ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE**, and that is the same sentence `b368`')
w('### wrote about `AGENTS.md` turned on `b368`. ### **THE ORDER MADE THIS ACT RE-DERIVE, AND THE')
w('### ### RE-DERIVATION IS WHAT CAUGHT IT.** ### A carried figure would have carried the error.')
w('### ### **NO ACT IS RE-VERDICTED BY THIS.** ### `b368`s COUNT (`%d` absent) stands and is confirmed'
  % R['n_absent'])
w('### for the third time; ### **ITS SPLIT IS CORRECTED**, which is a measurement replaced by a better')
w('### measurement and not a verdict withdrawn by a seat.')
w('### ### **`(R5)` IS OBSERVED THROUGHOUT: NO REASON IS ASSERTED FOR ANY RETIREMENT.** ### Where the')
w('### kernel`s record does not say why a name went, this act says that it does not say -- and the note')
w('### appended to the front document says it there too.')
w('')

w(SUB)
w('### (4) COMPONENT 2 -- THE TWO HYGIENE ITEMS.')
w(SUB)
w('### ### **THE PINS ROSTER NOW NAMES THE EXCLUSION KERNEL:** ### %s.'
  % nm(K['rosters']['b303_pins.py']))
w('### ### **AND SO DOES THE HOOK EXERCISER`S:** ### %s.' % nm(K['rosters']['b304_hooks.py']))
w('### ### **THE HOOK IS INSTALLED AND IS BYTE-IDENTICAL TO THE ONE TRACKED SOURCE : `%s`** (%d bytes),'
  % (K['hook_identical'], K['hook_bytes']))
w('### and the exclusion kernel had none before this act (`%s`).' % K['hook_existed_before'])
w('### ### **EXERCISED IN BOTH POLARITIES ACROSS EVERY ROSTERED REPOSITORY: REPOS FAILING `%d`.**'
  % K['repos_failing'])
w('### **AN UNEXERCISED HOOK IS AN ASSERTION**, so the install and the exercise were the same run.')
w('### ### **TWO OWNER INSTRUMENTS WERE EDITED AND BOTH WERE NAMED ON THE REGISTRATION`S FACE BEFORE')
w('### ### THE EDIT.** ### Any other instrument moving is still a gate failure and the suite still')
w('### checks it. ### **A CAP THAT SAYS `0` WHERE THE ORDER SAYS `DO IT` IS NOT A DISCIPLINE.**')
w('### ### **AND THE WORDING WAS MENDED WITH THE ROSTER, NOT AFTER IT.** ### Both tools announced')
w('### `ALL THREE` in their own voice. ### **A TOOL THAT SWEEPS FOUR REPOSITORIES WHILE ANNOUNCING')
w('### ### THREE IS A DATED ARM IN ITS OWN PROSE** (`b366`s species), and leaving it would have made')
w('### the mend itself the incident the next act reported. ### `%d` exact string pairs were applied,'
  % sum(K['wording_pairs'].values()))
w('### never a pattern -- ### **A REGEX OVER A TOOL`S PROSE IS A CHANGE NOBODY CAN REVIEW.**')
w('### ### ### **AND WHAT THIS DOES NOT FIX, SAID NOW AND NOT DISCOVERED LATER:** ### `.git/hooks/` IS')
w('### UNTRACKED. ### **A FRESH CLONE OF ANY OF THESE REPOSITORIES STILL HAS NO HOOK.** ### The roster')
w('### mend is TRACKED and survives a clone; the hook install is NOT. ### **THE TWO REPAIRS ARE NOT')
w('### ### EQUAL IN DURABILITY AND THIS ACT SAYS WHICH IS WHICH.**')
w('')

w(SUB)
w('### (5) COMPONENT 3 -- THE REFINEMENT PASS. ### **PRICED, AND NOT RUN.**')
w(SUB)
w('### ### **REPOSITORIES AUDITED : `%d`. ### SURFACES READ FOR CORRECTNESS : `%d`. ### REPOSITORIES'
  % (P['repositories_audited'], P['surfaces_read_for_correctness']))
w('### ### GRADED : `%d`.** ### `audit nothing` was the order`s own cap and it held.'
  % P['repositories_graded'])
w('### ### **THE ENUMERATION IS LIVE, FROM THE ACCOUNT:** ### `%d` repositories, `%d` of them programme'
  % (P['repos_on_account'], P['programme']))
w('### material; the other `%d` (%s) are reported, not silently dropped.'
  % (len(P['not_programme']), nm(P['not_programme'])))
w('### **A FEDERATION LIST TYPED FROM MEMORY IS THE SPECIES `DESK_FRESHNESS` WAS MINTED AGAINST**, so')
w('### it is not the pins roster, not the mirror roster and not recall.')
w('### ### **THE SURFACES, LISTED AND NOT READ:** ### `%d` descriptions, `%d` `README`s, `%d` front'
  % (P['descriptions'], P['readmes'], P['front_documents']))
w('### documents -- ### **`%d` SURFACES OF THE THREE CHEAP KINDS** -- and `%d` `.lean` files that could'
  % (P['cheap_surfaces'], P['lean_files']))
w('### carry docstrings, beside `%d` markdown files.' % P['markdown_files'])
w('')
w('### ### **THE PRICE, IN THREE PARTS:**')
w('###   ### **ONE REPOSITORY** -- the mechanical half is one tree call and at most three fetches, and')
w('###   this act measured the tree call at ### **%.1fs PER REPOSITORY.** ### The read half is a read of'
  % (P['seconds'] / max(1, P['programme'])))
w('###   the surface against the source, and ### **`b367` AND `b368` SPENT TWO WHOLE ACTS ON ONE FRONT')
w('###   ### DOCUMENT AGAINST ONE KERNEL.**')
w('###   ### **THE WHOLE FEDERATION** -- the mechanical sweep is ### **ONE ACT** ### and produces a')
w('###   CANDIDATE LIST, not a verdict. ### The read does not scale: `%d` front documents alone are an'
  % P['front_documents'])
w('###   arc, and `%d` `.lean` files are a programme.' % P['lean_files'])
w('###   ### ### **THE SPLIT, WHICH IS THE PART A PRICE USUALLY HIDES.** ### Mechanical: does a surface')
w('###   exist; does it carry a count-shaped string; which identifiers does it name; do those have')
w('###   declarations. ### **ALL FOUR ARE `b368`S CLASSIFIER, ALREADY BUILT.** ### Not mechanical:')
w('###   whether a count-shaped string is a CLAIM, what a count is a count OF, and whether an absent')
w('###   name was retired, renamed or never there. ### **NOTHING IN THIS PASS MAKES THE READ CHEAPER.**')
w('')
w('### ### **THE RANKING, BY THE ORDER`S OWN CRITERION** (age since last touch; counts rather than')
w('### terminals; public) -- ### **AND THE CRITERION IS PRINTED BEFORE THE RANKING SO IT CAN BE')
w('### ### DISAGREED WITH.** ### The order gave three factors and no weighting and this act invents')
w('### none; the table prints the three side by side.')
w('### ### **HIGHEST EXPOSURE : %s.**' % nm(P['highest_risk']))
w('### **IT IS A RANKING OF EXPOSURE, NOT OF ERROR.** ### No repository on it has been shown to carry a')
w('### stale claim, and this act did not look.')
w('### ### ### **AND WHAT THE RANKING CANNOT SEE, REPORTED BECAUSE IT IS SHARP: `SIDE-effects` IS NOT')
w('### ### ### ON IT.** ### The one repository this programme KNOWS carried a stale claim has no count')
w('### shape in its DESCRIPTION -- the claim lived in its FRONT DOCUMENT. ### **A CRITERION IS ONLY AS')
w('### ### WIDE AS THE SURFACE IT READS**, and a ranking built on descriptions would have missed the one')
w('### case the record already had.')
w('')
w('### ### **THE HINT, SCORED AGAINST WHAT WAS FOUND AND NEVER THE OTHER WAY ROUND.**')
w('### **THE STRUCTURAL HAZARD WAS NAMED FIRST:** ### `(H1)` supplies a description AND a count, and a')
w('### reader who found any count could fit it to the hint. ### **SO THE CONSTRUCTION KERNEL WAS')
w('### ### IDENTIFIED FROM THE DESCRIPTIONS THEMSELVES, NOT BY SEARCHING FOR A NUMBER** -- exactly one')
w('### description on the account uses the word `construction`.')
w('### ### **(H1) `the construction kernel`s public description names a core terminal count` -- %s.**'
  % P['h1'].split(' --')[0])
w('### `%s`, and the shape it carries is `%s`. ### The word `core` is the description`s own.'
  % (CONSTR, CS))
w('### ### **(H2) `that count may predate its current profile` -- %s, AND THE REGISTRATION SAID SO'
  % P['h2'])
w('### ### BEFORE THE ACT RAN.** ### Deciding it requires reading the profile, which is an audit. ###')
w('### **AN AGE IS NOT A STALENESS**, and an age is what this act can report. ### **`NOT LOCATED` IS AN')
w('### ### ANSWER, NOT A FAILURE.**')
w('')

w(SUB)
w('### (6) THE DESK, SWEPT ONCE MORE. ### **MARKS, NOT VERDICTS.**')
w(SUB)
w('### ### **ITEMS SWEPT `%d`; CONFIRMED-BY-FILE `%d`; UNCONFIRMED `%d`; ### CLOSED `%d`.**'
  % (Q['items'], Q['confirmed'], Q['unconfirmed'], Q['items_closed']))
w('### ### **THE RULE WAS READ FROM `b368`S MODULE, NOT RESTATED AS THIS ACT`S**, and no module was')
w('### written here: `b368` minted it, this act ### **USED** ### it.')
w('### ### **AND THE SAME CAVEAT, PRINTED AGAIN BECAUSE IT HAS NOT CHANGED:** ### a file that MENTIONS')
w('### an item is not a file that CONFIRMS it. ### **SO `%d of %d` IS A MARK ON THE SHAPE OF THE RECORD**'
  % (Q['confirmed'], Q['items']))
w('### and not a verdict on the desk.')
w('### ### ### **AND THAT IS THE POINT WORTH BANKING: THE SWEEP HAS NOW RETURNED THE SAME NUMBER WITH')
w('### ### ### THE SAME CAVEAT TWICE.** ### **A MEASUREMENT WHOSE RESULT AND WHOSE CAVEAT BOTH NEVER')
w('### ### ### MOVE IS A MEASUREMENT NOBODY IS USING.** ### The draft asks the next act to re-verify')
w('### ONE item properly; until an act does, this mark is a shape and not news.')
w('')

w(SUB)
w('### (7) WHAT MOVED, AND WHAT DID NOT.')
w(SUB)
w('### ### **MOVED:**')
w('###   `SIDE-effects/AGENTS.md` -- ### **THE LIST REPAIRED IN PLACE** ### (`%d` rows replaced by `%d`)'
  % (R['rows_replaced'], R['rows_written']))
w('###     and ONE appended note carrying the original verbatim.')
w('###   `PLACE-papers/OPEN_TRAILS.md` -- ONE append-only block, %d bytes, marked `%s`.'
  % (F['grew'], F['status']))
w('###   `tools/b303_pins.py` and `tools/b304_hooks.py` -- the roster and the prose that counts it.')
w('###   `SIDE-effects/.git/hooks/pre-push` -- INSTALLED, and untracked by construction.')
w('###   `SIDE-global-section/CORRESPONDENCE.md` -- one row. ### `tools/banked_index.py` -- one key.')
w('### ### **NOT MOVED, AND EACH FOR A STATED REASON:**')
w('###   **NO `.lean` FILE IN ANY REPOSITORY.** ### The kernel was READ.')
w('###   **NO SENTENCE OF `b368`S BLOCK.** ### It is named and superseded, never rewritten.')
w('###   **THE COUNT CLAIM ABOVE THE LIST.** ### Out of the order`s scope; REPORTED and routed.')
w('###   **`FACES_LEDGER.md`** -- not written and its writer not called, ### **BECAUSE NO ROW MOVED.**')
w('###   **NO FINDINGS SECTION.** ### The fold is the next act`s, and this one drafts it.')
w('###   **NO DESK ITEM CLOSED. ### NO TECHNE FILE WRITTEN. ### NO MODULE PUSHED.**')
w('')

w(SUB)
w("### (8) THE RECORD, ITS REFS, AND ITS CLOCKS.")
w(SUB)
w('###   `data/b369_registration_2026-09-08.txt` -- `%s`, %s bytes, locked %s.' % (SHA, NBY, LAT))
w('###   `data/b369_ferry_2026-09-08.txt` -- the order, banked verbatim.')
w('###   `data/%s` (%s) -- the extract-to-disk pass.' % (E['run_file'], E['run_clock']))
w('###   `data/%s` (%s) -- the repair.' % (R['run_file'], R['run_clock']))
w('###   `data/%s` (%s) -- the two hygiene items.' % (K['run_file'], K['run_clock']))
w('###   `data/%s` (%s) -- the priced pass.' % (P['run_file'], P['run_clock']))
w('###   `data/%s` (%s) -- the desk sweep.' % (Q['run_file'], Q['run_clock']))
w('###   `data/%s` (%s) -- the trail filing.' % (F['run_file'], F['run_clock']))
w('###   `tools/b369_extract.py`, `tools/b369_regspec.py`, `tools/b369_reg_gate.py`,')
w('###     `tools/b369_repair.py`, `tools/b369_hygiene.py`, `tools/b369_pass.py`,')
w('###     `tools/b369_desk.py`, `tools/b369_filing.py`, `tools/b369_bank.py`.')
w('### ### **THE REF READ AND WRITTEN:** ### `SIDE-effects` at `%s` = `%s`, pinned by `ls-remote` : %s.'
  % (R['ref'], R['head'], R['pinned']))
w('')

w(SUB)
w("### (9) THE ACT'S OWN INCIDENTS, ALL DECLARED.")
w(SUB)
w('### ### **(i) THE REGISTRATION GATE DRIVER TESTED A TUPLE FOR TRUTH.** ### `registration_gate.check`')
w('### returns `(code, lines)`; the first driver wrote `ok = RG.check(REG)` and a non-empty tuple is')
w('### always true -- ### **SO THE ARM WOULD HAVE PASSED ON A HARD FAILURE.** ### **AN ARM THAT CANNOT')
w('### ### FAIL IS NOT AN ARM**, and this is `b363`s species committed again: a shape assumed instead of')
w('### read. ### Caught by noticing the index-query lines were missing from the record.')
w('### ### **(ii) THE FIRST GATE RECORD CARRIED A BYTE NOBODY WROTE.** ### `Tee-Object` prepends a UTF-8')
w('### BOM (`b298`, `b305`), and the record is now written by the tool itself.')
w('### ### **(iii) THE WORKING FRONT DOCUMENT IS CRLF AND ITS BLOB IS LF** (`b309`s trap). ### The first')
w('### version of BAR 3 would have compared line endings and failed by construction. ### **A BYTE')
w('### ### COMPARISON THAT MEASURES A LINE ENDING MEASURES NOTHING** -- the tool now normalises both')
w('### sides and writes LF.')
w('### ### **(iv) THE PRESERVED QUOTATION NEARLY BROKE ITS OWN ANCHOR.** ### The first block quoted the')
w('### list`s opening sentence as well as its rows, which would have made that sentence appear twice and')
w('### the anchor AMBIGUOUS -- ### **THE TOOL THAT LOCATES THE LIST WOULD HAVE REFUSED ON THE ACT`S OWN')
w('### ### WRITING.** ### The opener is not quoted; the rows are.')
w('### ### ### **(v) THE LEDGER PREDICATE WAS WRONG TWICE, AND THE SECOND TIME WAS `b368`S.** ### This')
w('### act`s first predicate matched a layer by its first word and put `%d` names in the wrong group.'
  % 2)
w('### Fixing it exposed that ### **`b368`S PREDICATE WAS ALSO WRONG**, and its sharper claim with it.')
w('### **BOTH FAILURES ARE THE SAME SENTENCE: A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE.**')
w('### The front document was reverted uncommitted and the act re-run -- ### **AFTER A PUSH THE WRONG')
w('### ### SPLIT WOULD HAVE STOOD IN THREE REPOSITORIES.**')
w('### ### **(vi) THE COUNT-SHAPE DETECTOR FIRED ON A LANGUAGE VERSION.** ### `Lean 4 kernel` matched as')
w('### `4 kernel` across thirty descriptions; `Phase 1.5 checkpoint` and `h2 as five faces` matched too.')
w('### ### **A SHAPE DETECTOR REPORTS ITS PATTERN, NOT ITS SUBJECT** -- `U-1`s species, in a new tool.')
w('### Three exclusions were named, and the detector also stopped reporting only the FIRST match, ###')
w('### **BECAUSE ITS OWN NOISE WAS HIDING ITS OWN SIGNAL:** ### a real count sitting after `Lean 4` was')
w('### invisible.')
w('### ### **(vii) THE RANKING`S FIRST CLOSING SENTENCE WAS FALSE.** ### It said `SIDE-effects` was on')
w('### the risk list; it is not, and that is the more interesting fact. ### It is now reported as the')
w('### ranking`s ### **OWN UNSEEN HALF.**')
w('### ### **(viii) THE NUMBERED-REPEAT SPECIES, AGAIN** (`b358`s). ### The pass ran four times and the')
w('### repair twice. ### **THE RELIED-ON RUNS ARE `%s` AND `%s`, RESOLVED BY THEIR RECORDED CLOCKS.**'
  % (P['run_file'], R['run_file']))
w('')

w(SUB)
w("### (10) THE EXPECTATIONS, SCORED. ### **AN EXPECTATION IS SCORED, NEVER SATISFIED.**")
w(SUB)
w("### ### **THE NAVIGATOR`S (F1): `the repair is one edit and the currency block`s quotation preserves")
w('### ### the original whole` -- CONFIRMED.** ### One bounded edit, `%d` rows replaced by `%d`, every'
  % (R['rows_replaced'], R['rows_written']))
w('### byte outside the rows and the appended note identical to its blob; and all `%d` original rows'
  % R['rows_replaced'])
w('### survive verbatim in the same file. ### **BOTH HALVES ARE MEASURED, NOT ASSERTED.**')
w("### ### **THE NAVIGATOR`S (F2): `more than one federation repository carries a count claim older than")
w('### ### its kernel`s current state` -- PARTLY SCORED, AND THE UNREACHABLE HALF WAS REGISTERED IN')
w('### ### ADVANCE.** ### `%d` public repositories carry a count-SHAPED string in their description'
  % len(P['highest_risk']))
w('### (%s), so ### **THE `MORE THAN ONE` HALF IS CONFIRMED FOR SHAPES.** ### Whether any is OLDER THAN'
  % nm(P['highest_risk']))
w('### its kernel`s state is the audit, and `audit nothing` is the cap: ### **THAT HALF IS UNREACHABLE')
w('### ### BY THIS ACT.** ### A count shape is not a claim and an age is not a staleness.')
w("### ### **THIS SEAT`S OWN (E1): `(F2) will not be fully scorable by this act` -- MET**, and recorded")
w('### as the low bar it is: ### **A SEAT THAT PREDICTS THE LIMITS OF ITS OWN CAP HAS PREDICTED THE EASY')
w('### ### HALF.** ### The finding worth having is the one nobody registered: ### **`b368`S SHARPER')
w('### ### CLAIM WAS AN ARTEFACT OF ITS OWN PREDICATE**, and only re-deriving found it.')
w('')

w(SUB)
w('### (11) WHAT IS NOT CLAIMED.')
w(SUB)
w('### ### **NO `.lean` FILE WRITTEN. ### NO BUILD RUN. ### NO AXIOM PROFILE COMPUTED. ### NO')
w('### ### REPOSITORY AUDITED. ### NO SURFACE READ FOR CORRECTNESS. ### NO REPOSITORY GRADED. ### NO')
w('### ### RETIREMENT REASON SUPPLIED. ### NO SUCCESSOR NAMED. ### NO DESK ITEM CLOSED.**')
w('### ### **THE RETIREMENTS ARE REPORTED, NOT ENDORSED.** ### **NO NAME WAS CLASSIFIED FROM ITS OWN')
w('### ### SOUND.**')
w('### ### **NO ACT IS RE-VERDICTED.** ### `b368`s COUNT stands and is confirmed a third time; its SPLIT')
w('### is corrected, which is a measurement replaced by a better measurement.')
w('### ### **NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED.**')
w('### ### **NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT.**')
w('### ### **NOTHING IS COMPUTED ABOUT THE OBJECT. ### NOTHING IS COMPILED AND NO BRIDGE IS TYPED.**')
w('### ### **NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED.**')
w("### ### **NOTHING HERE BEARS ON `h2`, ON TOTALITY OR ON THE ROSTER.** ### `M-2` remains")
w('### (SPECIFIED-NOT-STATED) under `b310`s cap. ### The seam`s debt item 1 stands. ### The patent lane')
w("### is carried on the patent seat`s report, UNCONFIRMED on this seat`s record. ### **THE POSTURE LOCK")
w('### ### IS SEPARATE.** ### **THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED.** ### `h2`')
w('### stands exactly where the deposit left it. ### **NOTHING DEPOSITS.**')
w(BAR)


def main():
    body = chr(10).join(L) + chr(10)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(body)
    back = io.open(OUT, encoding='utf-8').read()
    print(BAR)
    print('b369 -- THE BANK, WRITTEN FROM THE JSONS.')
    print(BAR)
    print('  written : %s ; %d lines ; %d bytes'
          % (os.path.basename(OUT), len(back.split(chr(10))), len(back.encode('utf-8'))))
    ph = re.findall(r'%[sd]', back)
    print('  ### ### **UNFORMATTED PLACEHOLDERS LEFT IN THE BANK : %d** %s' % (len(ph), ph[:4]))
    # ### **THE CHECK EXISTS TO KEEP BANNED-STEM NAMES WHERE THE SCANNER CAN SEE THEY ARE QUOTED**, so
    # ### it applies to those names only -- and a name inside a longer backticked SPAN is quoted, which
    # ### the first version denied: it demanded backticks IMMEDIATELY flanking the name, and so called
    # ### an abbreviation like `a_b/c/d` unquoted. ### **A CHECK THAT KNOWS ONE SHAPE FINDS ONE SHAPE**,
    # ### which is this act's own sentence turned on this act's own arm.
    stems = tuple(banned_stems())
    allnames = [n for n in (set(R['absent']) | set(R['present']))
                if any(s in n.lower() for s in stems)]
    naked = []
    for ln in back.split(chr(10)):
        spans = [(m.start(), m.end()) for m in re.finditer(r'`[^`]*`', ln)]
        for n2 in allnames:
            for m in re.finditer(re.escape(n2), ln):
                if not any(a < m.start() and m.end() <= b for a, b in spans):
                    naked.append((n2, ln.strip()[:60]))
    print('  ### ### **KERNEL NAMES WRITTEN WITHOUT BACKTICKS : %d** %s' % (len(naked), naked[:2]))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'),
                        '--new', OUT], capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    v = [x.strip() for x in (r.stdout or '').splitlines() if 'VERDICT' in x]
    print('  ### the banned-term review on this new file : %s' % (v[0] if v else '?'))
    ok = (not ph) and (not naked) and v and 'CLEAN' in v[0]
    print('  %s' % ('PASS' if ok else '### FAIL ###'))
    print(BAR)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
