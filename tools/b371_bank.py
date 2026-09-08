# -*- coding: utf-8 -*-
"""b371_bank.py -- THE BANK, WRITTEN FROM THE ACT'S OWN JSONS. ### **NO FIGURE IS TYPED.**"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b371_the_first_target.txt')
REG = os.path.join(D, 'b371_registration_2026-09-08.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, S, R, INV, H, Q, F = (J('b371_reads'), J('b371_settle'), J('b371_repair_desc'),
                         J('b371_inventory'), J('b371_hookpath'), J('b371_desk'), J('b371_filing'))
regtxt = io.open(REG, encoding='utf-8').read()
SHA = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt).group(1)
NBY = re.search(r'bytes locked : (\d+)', regtxt).group(1)
LAT = re.search(r'locked at \(UTC\) : (\S+)', regtxt).group(1)
NCL = len(J('b371_satisfiable')['clauses'])

L = []


def w(s=''):
    L.append(s)


BAR, SUB = '=' * 100, '-' * 100

w(BAR)
w("b371 -- THE AUDIT'S FIRST TARGET, THE DESK CLOSED, THE HOOK MADE DURABLE. ### THE BANK.")
w('2026-09-08. ### CONCURRENCY: SOLO (research seat). ### FERRY_STANDING v2, by reference, citation '
  'CURRENT.')
w('### Registration `data/b371_registration_2026-09-08.txt`, ### **LOCKED**')
w('### `%s`, %s bytes, %d clauses JOINTLY' % (SHA, NBY, NCL))
w("### SATISFIABLE, and ### **LOCKED ONLY AFTER THE AUDIT'S OWN EXIT CODE CAME BACK `0`**, locked at "
  '(UTC)')
w('### %s. ### **LOCKED BEFORE ANY WRITE OF THIS ACT.** ### The clocks are in section (8).' % LAT)
w(BAR)
w('')

w(SUB)
w('### (1) THE ANSWER, FIRST.')
w(SUB)
w('### ### ### **THE COUNT CLAIM IS `%s`, AND THE NAVIGATOR`S EXPECTATION IS REFUTED ON ITS FIRST HALF.**'
  % S['verdict'])
w('### The description named a `Core` figure of `%d`. ### **THAT FIGURE WAS EXACT AT TAG `%s`, WHERE THE'
  % (S['figure'], S['tag']))
w('### ### PRINTED PROFILE CARRIED `%d`** -- and the repository is ### **`%s` COMMITS PAST THAT TAG**,'
  % (S['prints_at_tag'], S['head_ahead_of_tag']))
w('### its profile now carrying ### **`%d`.**' % S['prints_at_head'])
w('### ### **SO THE TWO COUNT THE SAME THING AT DIFFERENT REFS, NOT DIFFERENT THINGS** -- which is what')
w('### `SCOPE-DEPENDENT` would have required. ### **THE FIGURE WAS RIGHT AND THE REPOSITORY MOVED PAST')
w('### ### IT.** ### The description is repaired.')
w('### ### ### **THE DESK CLOSED FOR THE FIRST TIME: `%d` ITEMS SWEPT, `%d` CLOSED, `%d` STANDING.**'
  % (Q['items'], Q['closed'], Q['standing']))
w('### **`SCAFFOLD-TERMINALS` IS CLOSED, AFTER `b157`, `b367`, `b368` AND `b369`.**')
w('### ### ### **THE GUARD IS `%s`.** ### It lives at `%s/pre-push` in each of the `%d` rostered'
  % (H['outcome'], H['tracked_dir'], len(H['repos'])))
w('### repositories, ### **TRACKED BY GIT**, byte-identical to the one source, exercised in both')
w('### polarities with `%d` failing. ### **AND A CLONE IS STILL NOT GUARDED**, and this act says so.'
  % len(H['failing']))
w('### ### **THE ROW INVENTORY IS LISTED AND NOT CHECKED: `%d` ROWS CITE A KERNEL AND A TERMINAL, `%d`'
  % (INV['rows'], INV['with_pin']))
w('### ### OF THEM WITH A PIN AND `%d` WITH NONE.** ### `%d` name a declaration this record has already'
  % (INV['without_pin'], INV['flagged_count']))
w('### classified absent. ### **ROWS CHECKED : `%d`. ### KERNELS OPENED : `%d`.**'
  % (INV['rows_checked'], INV['kernels_opened']))
w('')

w(SUB)
w('### (2) COMPONENT 1 -- THE ONE CONFIRMED LIVE CLAIM, SETTLED.')
w(SUB)
w('### ### **THE TEST WAS FIXED BEFORE THE READ, BECAUSE THIS IS WHERE A SEAT WOULD FIT A NUMBER TO A')
w('### ### HINT:** ### `SCOPE-DEPENDENT` requires that the two words count ### **DIFFERENT THINGS**;')
w('### `STALE` is what remains when they count ### **THE SAME THING AT DIFFERENT REFS.**')
w('### ### **THE PROFILE, MEASURED AT BOTH REFS BY THE SAME MEASUREMENT:**')
w('###     at tag `%s` = `%s` : ### **`%d` zero-axiom prints**' % (S['tag'], S['tag_commit'][:7]
                                                                   if S['tag_commit'] else '?',
                                                                   S['prints_at_tag']))
w('###     at `HEAD` = `%s` : ### **`%d` of `%d` lines, `%d` otherwise**'
  % (S['head'][:7], S['prints_at_head'], S['prints_at_head_all'],
     S['prints_at_head_all'] - S['prints_at_head']))
w('### ### **BAR 2 -- THE BLOB AND THE WORKING FILE AGREE : %s**, and `ls-remote` matches `HEAD` : %s.'
  % (S['blob_equals_working'], S['pinned']))
w('### ### ### **THE DECIDING EQUALITY: THE DESCRIPTION SAYS `%d`; THE PROFILE AT THE TAG CARRIED `%d`.'
  % (S['figure'], S['prints_at_tag']))
w('### ### ### EQUAL : %s.**' % S['same_quantity'])
w('### ### **AND THE ARITHMETIC COINCIDENCE IS REPORTED AS A COINCIDENCE AND NOT PROMOTED TO A SCOPE.**')
w('### The record does name summands that add to the figure -- the kernel`s own correspondence says the')
w('### audit at the tag reconciled exactly, and the papers registry pins the same. ### **BUT THOSE ARE')
w('### ### THE COMPOSITION OF THE TAG`S OWN COUNT, NOT A SUBSET OF A LARGER PRESENT ONE**, and reading')
w('### them as a scope would have been the inference the registration forbade before the read.')
w('### ### **THE DESCRIPTION CARRIED NO QUALIFIER AT ALL** -- no ref, no tag, no version, no date. ###')
w('### **WHICH IS PRECISELY WHY THE FIGURE READ AS CURRENT.**')
w('')
w('### ### **THE REPAIR, AND THE ORIGINAL PRESERVED BEFORE IT.**')
w('### ### **A DESCRIPTION HAS NO HISTORY AND NOTHING ELSE WILL REMEMBER IT**, so the old text is banked')
w('### here, verbatim:')
w('###     | %s' % R['before'])
w('### and the account now carries, read back byte-for-byte (`%s`):' % R['set_byte_for_byte'])
w('###     | %s' % R['after'])
w('### ### ### **THE COUNT IS REMOVED RATHER THAN UPDATED, AND THAT IS THIS SEAT`S JUDGEMENT, FLAGGED')
w('### ### ### AS ONE.** ### Replacing `%d` with `%d` would be correct today and stale on the next commit'
  % (S['figure'], S['prints_at_head']))
w('### that adds a terminal -- and the repository is `%s` commits past the last time anybody updated it.'
  % S['head_ahead_of_tag'])
w('### **WHAT REPLACES IT IS A PROPERTY, NOT A COUNT**, and it names the artifact that holds the number.')
w('### ### **THE AUTHOR MAY PREFER A DATED NUMBER**, and that wording is banked so the choice is one')
w('### edit away:')
w('###     | %s' % R['alternative_banked'])
w('### ### **AND THE REGISTER SENTENCE SURVIVED THE EDIT : %s** -- the one clause in that description'
  % R['register_sentence_survived'])
w('### this seat must not touch, and the arm that proves it did not.')
w('### ### **AND THE DURABILITY IS STATED WITH THE FINDING, NOT AFTER IT:** ### a description is')
w('### ### **ACCOUNT METADATA, NOT A TRACKED FILE.** ### The correction survives a clone and survives')
w('### nothing else, and ### **NO TRACKED ARTIFACT WOULD FAIL IF IT DRIFTED AGAIN.**')
w('')
w('### ### ### **AND THE ADJACENT FINDING, REPORTED AND ROUTED AND NOT REPAIRED -- AND IT IS THE')
w('### ### ### SHARPER HALF.** ### The kernel`s own `README.md` says `%s` terminals in its headline; its'
  % S['readme_headline'])
w('### own parenthetical breakdown sums to `%d`; its assembly ratio says `%d/%d`; and the profile the'
  % (S['readme_breakdown_sum'], S['readme_ratio'][0], S['readme_ratio'][1]))
w('### same repository ships carries `%d`. ### **THE HEADLINE DISAGREES WITH ITS OWN BREAKDOWN, AND BOTH'
  % S['prints_at_head'])
w('### ### DISAGREE WITH THE PROFILE.**')
w('### ### **IT IS SHARPER THAN THE DESCRIPTION BECAUSE THE `README` IS A TRACKED FILE AND THE')
w('### ### DESCRIPTION IS NOT** -- `DURABILITY_SPLIT`: ### **THE DRIFT THAT TRAVELS WITH A CLONE IS THE')
w('### ### ONE NOBODY HAS BEEN ORDERED TO FIX.** ### Outside this component`s target; routed.')
w('')

w(SUB)
w('### (3) COMPONENT 2 -- THE ROW INVENTORY. ### **LISTED, NOT CHECKED.**')
w(SUB)
w('### ### **ROWS CHECKED : `%d`. ### KERNELS OPENED : `%d`. ### COMPLETENESS CLAIMED : %s.**'
  % (INV['rows_checked'], INV['kernels_opened'], INV['completeness_claimed']))
w('### ### **THE PREDICATE WAS DECLARED BEFORE THE SWEEP AND ITS FAILURE MODE WITH IT** ###')
w('### (`PREDICATE_ONE_SHAPE`): a row whose pin is written in a shape the predicate does not know is')
w('### reported PINLESS, and the sweep says so rather than claiming to have found them all.')
w('### ### **THE SWEEP:** ### `%d` table rows across `%d` tracked markdown files; ### **`%d` NAME A'
  % (INV['table_rows_scanned'], INV['files'], INV['rows']))
w('### ### KERNEL AND A TERMINAL**; of those, ### **`%d` NAME A PIN AND `%d` NAME NONE**; `%d` distinct'
  % (INV['with_pin'], INV['without_pin'], INV['distinct_pins']))
w('### pins are named across the pinned set.')
w('### ### ### **AND THE PINLESS SET IS A FINDING, NOT A HOLE IN THE SWEEP.** ### `(R6)` checks a row')
w('### ### *"at the kernel and pin the row itself names"* ### -- so ### **A ROW WITHOUT A PIN CANNOT BE')
w('### ### CHECKED THE WAY THE RULING SPECIFIES.** ### `%d` of `%d` cannot.'
  % (INV['without_pin'], INV['rows']))
w('')
w('### ### **THE CROSS-REFERENCE, AND IT IS NOT A CHECK.** ### `%d` rows name a declaration this record'
  % INV['flagged_count'])
w('### already classified ABSENT at `b368` and re-derived at `b369`. ### **COMPARING A NAME AGAINST A')
w('### ### BANKED FINDING OPENS NO KERNEL AND VERIFIES NO ROW.**')
for f in INV['flagged'][:12]:
    w('###     %-48s:%-5d %s%s' % (f['file'][:48], f['line'],
                                   ', '.join('`%s`' % x for x in f['names']),
                                   '' if f['has_pin'] else '   ### (and it names no pin)'))
w('### ### **A ROW SO FLAGGED IS NOT THEREBY WRONG.** ### The banked finding is about one kernel at one')
w('### ref; a row may name a different kernel, an older ref, or a name that moved. ### **IT IS A ROW')
w('### ### WHOSE CHECK THE RANKING SHOULD ORDER FIRST, AND THAT IS ALL THE FLAG MEANS.**')
w('')
w('### ### **THE PRICE, IN THREE PARTS.**')
w('###   ### **ONE ROW:** ### mechanically, resolve the pin, fetch the kernel at it, search for the')
w('###   declaration -- ### **`b368`S CLASSIFIER WITH A REF ARGUMENT, AND IT ALREADY EXISTS.** ### The')
w('###   read is deciding whether the row`s CLAIM is what the terminal supports, and ### **A NAME')
w('###   ### PRESENT IS NOT A ROW TRUE.**')
w('###   ### **THE WHOLE SET:** ### the mechanical half over the pinned set is ONE ACT, because a fetch')
w('###   amortises across every row naming the same pin and there are only `%d` distinct pins.'
  % INV['distinct_pins'])
w('###   ### **THE PINLESS SET IS NOT CHEAPER -- IT IS UNPRICEABLE UNDER `(R6)` AS WRITTEN**, and needs')
w('###   a ruling before it needs an act.')
w('###   ### **THE SPLIT:** ### a tool settles whether a pin resolves, whether the kernel at it declares')
w('###   the name, and whether the kernel has moved. ### **A TOOL CANNOT SETTLE WHETHER THE ROW`S')
w('###   ### SENTENCE IS WHAT THE TERMINAL SUPPORTS.**')
w('### ### **THE RANKING IS BY THE ORDER`S OWN CRITERION, PRINTED BEFORE THE RANKING** -- pin age;')
w('### count rather than terminal; kernel moved since. ### **AND ONE FACTOR CANNOT BE FILLED WITHOUT')
w('### ### OPENING A KERNEL:** ### `%s` ### -- so it is recorded as `NOT FILLED` for every row and the'
  % INV['factor_c'])
w('### ranking runs on the other two, and says so.')
w('')

w(SUB)
w('### (4) COMPONENT 3 -- THE GUARD, MOVED TO A TRACKED PATH.')
w(SUB)
w('### ### **OUTCOME : `%s`, AND IT WAS CHOSEN BY A TEST AND NOT BY PREFERENCE.**' % H['outcome'])
w('### The order`s question was whether a tracked directory can hold the guard and whether the')
w('### repository then RUNS it. ### **IT CAN AND IT DOES**, in all `%d`.' % len(H['repos']))
w('### ### **THE MOVE:** ### `%s/pre-push` in each repository, ### **TRACKED BY GIT**, byte-identical'
  % H['tracked_dir'])
w('### to the one source (`%d` bytes), with `core.hooksPath` set to read it.' % H['source_bytes'])
w('### ### **THE EXERCISE: BOTH POLARITIES IN EVERY REPOSITORY, `%d` FAILING.** ### A push from a'
  % len(H['failing']))
w('### non-`push-*` branch REFUSED, a push from a `push-*` branch ALLOWED, head unmoved and branch')
w('### restored in each. ### **AN UNEXERCISED HOOK IS AN ASSERTION.**')
w('### ### ### **AND `DURABLE` IS THE ORDER`S WORD, NOT A CLAIM THAT A CLONE IS GUARDED.** ###')
w('### `core.hooksPath` lives in `.git/config`, which is ### **NOT TRACKED.** ### **A FRESH CLONE STILL')
w('### ### RUNS NO GUARD UNTIL SOMEONE RUNS `%s`.**' % H['residual_step'])
w('### ### **WHAT CHANGED IS WHICH HALF IS MISSING.** ### Before: the clone had neither the guard nor')
w('### the wiring, and the guard existed only on one machine. ### Now: the clone carries ### **THE')
w('### ### GUARD** ### and lacks ### **ONE COMMAND.** ### A smaller hole, and not no hole.')
w('### ### **THE OLD LOCATION IS LEFT IN PLACE AND INERT** in all four. ### **A SAFETY NET AND A TRAP**')
w('### -- if the config is unset it becomes live again, and two copies can drift. ### The exerciser`s')
w('### byte-identity arm against the one source is what catches the drift.')
w('### ### **AND THE EXERCISER FOLLOWED THE GUARD IN THE SAME ACT.** ### `tools/b304_hooks.py` read the')
w('### old location; a guard that moves while its checker does not is ### **`GUARD_WITH_NOTHING')
w('### ### LISTENING`, ALREADY IN THIS RECORD`S OWN LORE.** ### It is the one owner instrument this act')
w('### edited, named on the registration`s face before the edit.')
w('### ### ### **AND ONE THING THIS ACT BROKE AND DID NOT FIX:** ### the guard`s own front matter still')
w('### names the superseded install path. ### **A GUARD`S OWN FRONT MATTER IS A SURFACE TOO** -- the')
w('### exact species Components 1 and 2 were spent on, committed by this act`s own repair. ### Not')
w('### repaired here: the cap licensed ONE instrument edit, and editing the guard would change the bytes')
w('### all four copies are compared against. ### **REPORTED AND ROUTED.**')
w('')

w(SUB)
w('### (5) THE DESK, UNDER `(R7)`. ### **IT CLOSED.**')
w(SUB)
w('### ### **ITEMS SWEPT `%d`; CLOSED `%d`; STANDING `%d`; UNCONFIRMED `%d`.**'
  % (Q['items'], Q['closed'], Q['standing'], Q['unconfirmed']))
w('### ### **CLOSURES REFUSED FOR WANT OF A KILLING FILE : `%d`.**' % Q['closures_refused'])
w('### **A CLOSURE WITHOUT A KILLING FILE IS AN OPINION**, so each closure below names a banked file,')
w('### that file was checked to EXIST and to CARRY the sentence claimed for it, and its date is its own.')
for c in Q['closed_items']:
    w('###     %-56s <- `%s` (%s)' % (c['item'][:56], c['file'], c['date']))
w('### ### ### **AND THIS IS THE FIRST TIME THE NUMBER HAS MOVED.** ### `b368`, `b369` and `b370` each')
w('### swept and each reported the same nine marks with the same caveat. ### **THE MEASUREMENT DID NOT')
w('### ### CHANGE BECAUSE THE RULE DID NOT LET IT** -- and `b370``s own bank had said a measurement')
w('### whose result and whose caveat both never move is a measurement nobody is using. ### `(R7)`')
w('### changed the rule and the desk moved in the same act.')
w('### ### **AND NONE OF THOSE THREE ACTS IS RE-VERDICTED.** ### Each obeyed the rule it was given; the')
w('### author changed the rule. ### **THIS ACT SAYS SO RATHER THAN QUIETLY CLOSING WHAT THREE ACTS WERE')
w('### ### FORBIDDEN TO.**')
w('### ### **ONE CLOSURE IS FLAGGED BECAUSE ITS KILLING FILE IS THIS ACT`S OWN** -- the hook`s')
w('### non-durability, killed by Component 3. ### **ALLOWED, BECAUSE THIS ACT DID THE KILLING**, and')
w('### marked so no reader mistakes it for a confirmation drawn from the record (`b368`s incident).')
w('')

w(SUB)
w('### (6) WHAT MOVED, AND WHAT DID NOT.')
w(SUB)
w('### ### **MOVED:**')
w('###   the `SIDE-global-section` public DESCRIPTION -- repaired; the original preserved in this bank.')
w('###   `.githooks/pre-push` in all `%d` rostered repositories -- NEW, TRACKED.' % len(H['repos']))
w('###   `core.hooksPath` in all `%d` -- LOCAL CONFIG, and not tracked.' % len(H['repos']))
w('###   `tools/b304_hooks.py` -- the one licensed owner instrument, following the guard.')
w('###   `PLACE-papers/OPEN_TRAILS.md` -- ONE append-only block, %d bytes, closing `SCAFFOLD-TERMINALS`.'
  % F['grew'])
w('###   `SIDE-global-section/CORRESPONDENCE.md` -- one row. ### `tools/banked_index.py` -- one key.')
w('### ### **NOT MOVED, AND EACH FOR A STATED REASON:**')
w('###   **NO ROW WAS CHECKED AND NO KERNEL WAS OPENED FOR ANY ROW.**')
w('###   **THE KERNEL`S `README.md`** -- the adjacent finding; outside the target, routed.')
w('###   **THE GUARD`S OWN FRONT MATTER** -- stale install path; outside the cap, routed.')
w('###   **THE COUNT CLAIM ABOVE THE REPAIRED LAYER-1 LIST** -- still owed, and it STANDS on the desk.')
w('###   **NO `.lean` FILE. ### NO BUILD. ### NO AXIOM PROFILE RECOMPUTED.**')
w('###   **`FACES_LEDGER.md`** -- not written and its writer not called, ### **BECAUSE NO ROW MOVED.**')
w('###   **NO FINDINGS SECTION. ### NO TECHNE FILE. ### NO MODULE PUSHED.**')
w('')

w(SUB)
w("### (7) THE EXPECTATIONS, SCORED. ### **AN EXPECTATION IS SCORED, NEVER SATISFIED.**")
w(SUB)
w('### ### ### **THE NAVIGATOR`S: `the count claim is SCOPE-DEPENDENT and the description does not say')
w('### ### ### so plainly` -- SPLIT, AND THE SPLIT IS THE INTERESTING PART.**')
w('### ### **THE FIRST HALF IS REFUTED.** ### It is not scope-dependent: there is no scope, there is a')
w('### REF. ### The description`s figure and the profile measure ### **THE SAME QUANTITY**, and the')
w('### figure was exact when it was written.')
w('### ### **THE SECOND HALF IS CONFIRMED, AND MORE STRONGLY THAN IT WAS PUT.** ### The description did')
w('### not merely fail to say its scope plainly -- ### **IT NAMED NO REF, TAG, VERSION OR DATE AT ALL**,')
w('### which is exactly why a reader takes the figure as current.')
w('### ### **AND IT WAS REFUTABLE BY THE DESCRIPTION`S OWN WORDS, WHICH IS WHAT MADE IT A GOOD')
w('### ### EXPECTATION** -- the words are quoted in (2) and a reader can check both halves.')
w('### ### **THIS SEAT`S (E1): `the inventory will find rows naming a kernel and a terminal but no pin,')
w('### ### and they will outnumber the rows that name all three` -- HALF MET, HALF REFUTED.** ### Such')
w('### rows exist and there are `%d` of them; ### **BUT THEY DO NOT OUTNUMBER THE PINNED SET, WHICH HAS'
  % INV['without_pin'])
w('### ### `%d`.** ### The prediction of existence was cheap; the prediction of the ratio was wrong.'
  % INV['with_pin'])
w('### ### **THIS SEAT`S (E2): `the hook will be made durable rather than struck` -- MET, AND IT WAS THE')
w('### ### WEAK ONE AND WAS RECORDED AS SUCH BEFORE THE ACT RAN.** ### It predicted that a copy would')
w('### copy. ### **A SEAT THAT PREDICTS ITS OWN NEXT COMMAND HAS PREDICTED NOTHING.**')
w('')

w(SUB)
w("### (8) THE RECORD, ITS REFS, AND ITS CLOCKS.")
w(SUB)
w('###   `data/b371_registration_2026-09-08.txt` -- `%s`, %s bytes, locked %s.' % (SHA, NBY, LAT))
w('###   `data/b371_ferry_2026-09-08.txt` -- the order, banked verbatim.')
w('###   `data/%s` (%s) -- the extract-to-disk pass.' % (E['run_file'], E['run_clock']))
w('###   `data/%s` (%s) -- the settling.' % (S['run_file'], S['run_clock']))
w('###   `data/%s` (%s) -- the repair, and its read-back.' % (R['run_file'], R['run_clock']))
w('###   `data/%s` (%s) -- the row inventory.' % (INV['run_file'], INV['run_clock']))
w('###   `data/%s` (%s) -- the guard moved and exercised.' % (H['run_file'], H['run_clock']))
w('###   `data/%s` (%s) -- the desk, under `(R7)`.' % (Q['run_file'], Q['run_clock']))
w('###   `data/%s` (%s) -- the closures, filed.' % (F['run_file'], F['run_clock']))
w('### ### **THE REFS:** ### `SIDE-global-section` at `%s` = `%s`, `ls-remote` equal : %s; tag `%s` = '
  % (E['refs']['SIDE-global-section']['branch'], E['refs']['SIDE-global-section']['head'],
     E['refs']['SIDE-global-section']['pinned'], S['tag']))
w('### `%s`, and `HEAD` is `%s` commits ahead of it.' % (S['tag_commit'], S['head_ahead_of_tag']))
w('')

w(SUB)
w("### (9) THE ACT'S OWN INCIDENTS, ALL DECLARED.")
w(SUB)
w('### ### ### **(i) THE PLACEHOLDER-SPLIT SPECIES, A FIFTH TIME** (`b365`, `b368`, `b369`, `b370`,')
w('### ### ### here, TWICE). ### A format string ends one line and its argument is attached to the NEXT')
w('### call, so the first line prints its placeholder into the record and the value never reaches it.')
w('### **THE EXAMPLE IS ELIDED HERE AND THE ELISION IS MARKED**, because writing the placeholder out')
w('### makes this bank fail its own check -- the use-and-mention species (`b348`) meeting a literal scan.')
w('### ### ### **AND IT HAPPENED TWICE IN THIS ACT: ONCE IN THE REPAIR TOOL, AND THEN AGAIN IN THIS')
w('### ### ### BANK WRITER, IN THE SENTENCE REPORTING THE FIRST ONE.** ### Both were caught by the')
w('### bank`s own placeholder check, which is the only thing that has ever caught this. ###')
w('### **CAUGHT BY READING THE ACT`S OWN OUTPUT, WHICH IS THE ONLY THING THAT EVER CATCHES IT.** ### The')
w('### repair tool was fixed and made ### **IDEMPOTENT** ### in the same pass, so the re-run verified its')
w('### arms and issued no second edit.')
w('### ### **(ii) THREE EXTRACT HINTS MISSED ON THE FIRST RUN.** ### Two were typed across line wraps.')
w('### ### **THE THIRD WAS GENUINELY AMBIGUOUS -- SIX IDENTICAL TABLE HEADERS IN ONE DOCUMENT -- AND')
w('### ### THE TOOL REFUSED IT**, which is the tool working: an ambiguous anchor is not a located line.')
w('### ### **(iii) A GARBLED WORD IN THE REGISTRATION`S OWN DRAFT.** ### An attempt to avoid a banned')
w('### stem mangled the word it was avoiding, and it was caught by reading the file before the lock.')
w('### ### ### **(iv) AND THE ONE THAT COST THE MOST: THIS ACT`S OWN HOOK-MOVER DESTROYED UNCOMMITTED')
w('### ### ### WORK IN FOUR REPOSITORIES.** ### Its polarity exercise put a throwaway commit on a')
w('### scratch branch and then `reset --hard`ed it away. ### **A SCRATCH BRANCH CARRIES WHATEVER IS')
w('### ### UNCOMMITTED, AND DISCARDING THE BRANCH DISCARDS THE WORK.** ### On its second run it wiped')
w('### this act`s own trail block, its correspondence row, its index key and its one licensed instrument')
w('### edit -- ### **ALL OF THEM UNCOMMITTED, ALL OF THEM WRITTEN BY THIS ACT MINUTES EARLIER.**')
w('### ### **IT WAS CAUGHT BY THE SUITE AND NOT BY THE TOOL**, and only because `G-HOOKPATH` ###')
w('### **RE-READS THE FILESYSTEM INSTEAD OF TRUSTING THE MOVER`S OWN JSON** -- the JSON said TRACKED in')
w('### all four; the filesystem said nothing was. ### **A TOOL THAT REPORTS A RESULT ITS OWN NEXT STEP')
w('### ### DESTROYS WILL REPORT IT HONESTLY AND BE WRONG.**')
w('### ### ### **AND CHASING IT FOUND THE SAME DEFECT IN THE SHARED INSTRUMENT, LATENT SINCE `b304`.**')
w('### `tools/b304_hooks.py` uses no `reset` -- it checks out back and deletes the branch -- ### **BUT')
w('### ### THE THROWAWAY COMMIT IS MADE ON THAT BRANCH, AND DELETING THE BRANCH DELETES WHATEVER THE')
w('### ### COMMIT CARRIED.** ### Run on a dirty tree it destroys uncommitted work exactly as this act`s')
w('### tool did, and ### **IT DESTROYED THIS ACT`S STAGED GUARD IN ALL FOUR REPOSITORIES ON ITS NEXT')
w('### ### RUN, PROVING IT.**')
w('### ### **THE DEFECT HAS BEEN IN THAT TOOL SINCE `b304` AND HAD NEVER FIRED**, because the closing')
w('### sequence only ever runs it ### **AFTER THE PUSH, WHEN EVERY TREE IS CLEAN.** ### **A')
w('### ### GUARD-CHECKER THAT IS SAFE ONLY BECAUSE OF WHEN IT HAPPENS TO BE CALLED IS NOT SAFE.**')
w('### ### **BOTH TOOLS NOW REFUSE A DIRTY TREE**, and the shared one counts a refusal as a FAILURE of')
w('### the run rather than a pass, ### **SO NOBODY READS A SKIPPED EXERCISE AS AN EXERCISED ONE.** ###')
w('### That repair is inside the one licensed instrument edit and is a safety fix, not a widening.')
w('### ### **AND THE POLARITY BAR IS MET WHERE IT ALWAYS WAS: AFTER THE PUSH, ON CLEAN TREES.**')
w('### ### **EVERYTHING DESTROYED WAS DETERMINISTIC AND WAS REBUILT BY RE-RUNNING ITS WRITER**, which is')
w('### the only reason this is an incident and not a loss -- ### **AND THAT IS AN ARGUMENT FOR WRITERS')
w('### ### THAT REGENERATE, NOT A REASON TO BE RELAXED ABOUT DESTROYING THINGS.**')
w('### ### **(v) AND THIS ACT`S OWN REPAIR CREATED A STALE SURFACE.** ### Moving')
w('### the guard made its own front matter`s install line wrong. ### **AN ACT AUDITING STALE SURFACES')
w('### ### MADE ONE**, in the same run, and reported it rather than leaving it for the next sweep.')
w('')

w(SUB)
w('### (10) WHAT IS NOT CLAIMED.')
w(SUB)
w('### ### **NO ROW WAS CHECKED AND NO KERNEL WAS OPENED FOR ANY ROW.** ### **NO REPOSITORY WAS AUDITED')
w('### ### BEYOND THE SINGLE SETTLED CLAIM**, and the second pass `(R6)` describes is NOT OPENED.')
w('### ### **NO `.lean` FILE WAS TOUCHED. ### NO BUILD WAS RUN. ### NO AXIOM PROFILE WAS RECOMPUTED** --')
w('### the profile was READ as a printed record, at a ref and against its blob.')
w('### ### **NO ITEM WAS CLOSED WITHOUT ITS KILLING FILE AND DATE.**')
w('### ### **NO ACT IS RE-VERDICTED.** ### `(R7)` reverses a disposition three acts carried; that is the')
w('### author`s ruling and not this seat`s finding about those acts.')
w('### ### **A CLONE IS NOT GUARDED**, and `MADE DURABLE` is the order`s word for what was done, not a')
w('### claim that it is.')
w('### ### **NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED.** ### **NOTHING IS CLAIMED ABOUT')
w('### ### THE MATHEMATICS OF ANY NAMED SUBJECT** -- a count is about what a document says, not about')
w('### what is true.')
w('### ### **NOTHING IS COMPUTED ABOUT THE OBJECT. ### NOTHING IS COMPILED AND NO BRIDGE IS TYPED.**')
w('### ### **NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED.**')
w("### ### **NOTHING HERE BEARS ON `h2`, ON TOTALITY OR ON THE ROSTER.** ### `M-2` remains")
w('### (SPECIFIED-NOT-STATED) under `b310`s cap. ### The seam`s debt item 1 stands. ### The patent lane')
w("### is carried on the patent seat`s report, UNCONFIRMED on this seat`s record. ### **THE POSTURE LOCK")
w('### ### IS SEPARATE. ### THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED.** ### `h2`')
w('### stands exactly where the deposit left it. ### **NOTHING DEPOSITS.**')
w(BAR)


def main():
    body = chr(10).join(L) + chr(10)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(body)
    back = io.open(OUT, encoding='utf-8').read()
    print(BAR)
    print('b371 -- THE BANK, WRITTEN FROM THE JSONS.')
    print(BAR)
    print('  written : %s ; %d lines ; %d bytes'
          % (os.path.basename(OUT), len(back.split(chr(10))), len(back.encode('utf-8'))))
    ph = re.findall(r'%[sd]', back)
    print('  ### ### **UNFORMATTED PLACEHOLDERS LEFT IN THE BANK : %d** %s' % (len(ph), ph[:4]))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'),
                        '--new', OUT], capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    v = [x.strip() for x in (r.stdout or '').splitlines() if 'VERDICT' in x]
    print('  ### the banned-term review on this new file : %s' % (v[0] if v else '?'))
    ok = (not ph) and v and 'CLEAN' in v[0]
    print('  %s' % ('PASS' if ok else '### FAIL ###'))
    print(BAR)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
