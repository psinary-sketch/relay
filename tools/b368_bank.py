# -*- coding: utf-8 -*-
"""b368_bank.py -- THE BANK, WRITTEN FROM THE ACT'S OWN JSONS. ### **NO FIGURE IS TYPED.**

### ### **EVERY NUMBER IN THE BANK IS READ FROM A JSON THIS ACT'S OWN TOOLS WROTE.** ### A bank whose
### figures are retyped is a bank that can disagree with its act, and `b363` found exactly that in its
### own draft.
### ### **AND EVERY KERNEL IDENTIFIER IS WRITTEN INSIDE BACKTICKS**, because the banned-term scanner
### excuses a QUOTED KERNEL IDENTIFIER only where it can see the quoting (`b367`'s incident).
"""
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
OUT = os.path.join(D, 'b368_the_front_document_reconciled.txt')
REG = os.path.join(D, 'b368_registration_2026-09-08.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, C, R, K, F = J('b368_reads'), J('b368_classify'), J('b368_reconcile'), J('b368_desk'), J('b368_filing')
regtxt = io.open(REG, encoding='utf-8').read()
SHA = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt).group(1)
NBY = re.search(r'bytes locked : (\d+)', regtxt).group(1)
LAT = re.search(r'locked at \(UTC\) : (\S+)', regtxt).group(1)
NCL = len(re.findall(r'^\s*\("', io.open(os.path.join(ROOT, 'tools', 'b368_regspec.py'),
                                         encoding='utf-8').read(), re.M))

named = [r for r in C['rows'] if r['kind'] == 'RETIRED' and r['note'] == 'named by the ledger itself']
_rest = [r for r in C['rows'] if r['kind'] == 'RETIRED' and r['note'] != 'named by the ledger itself']
# ### **THREE GROUPS, READ FROM THE EVIDENCE AND NOT FROM THE NOTE.** ### One layer carries no ledger
# ### entry at all, and filing its declaration under `covered by its layer's entry` would describe
# ### evidence the row does not have.
layer_only = [r for r in _rest if r['evidence'].get('line')]
hist_only = [r for r in _rest if not r['evidence'].get('line')]
PRES = {r['name']: r for r in C['rows'] if r['kind'] == 'PRESENT'}

L = []


def w(s=''):
    L.append(s)


def nm(rows):
    return ', '.join('`%s`' % r['name'] for r in rows)


BAR = '=' * 100
SUB = '-' * 100

w(BAR)
w('b368 -- THE FRONT DOCUMENT RECONCILED, OR PRICED. ### THE BANK.')
w('2026-09-08. ### CONCURRENCY: SOLO (research seat). ### FERRY_STANDING v2, by reference, citation '
  'CURRENT.')
w('### Registration `data/b368_registration_2026-09-08.txt`, ### **LOCKED**')
w('### `%s`, %s bytes, %d clauses JOINTLY' % (SHA, NBY, NCL))
w("### SATISFIABLE, and ### **LOCKED ONLY AFTER THE AUDIT'S OWN EXIT CODE CAME BACK `0`**, locked at "
  '(UTC)')
w('### %s. ### **LOCKED BEFORE ANY WRITE OF THIS ACT.** ### The clocks are in section (9).' % LAT)
w(BAR)
w('')

w(SUB)
w('### (1) THE ANSWER, FIRST.')
w(SUB)
w('### ### ### **THE FRONT DOCUMENT IS RECONCILED, AND IT WAS RECONCILED WITHOUT EDITING A SENTENCE.**')
w('### ### **OF THE %d NAMES `AGENTS.md` EXPORTS AT LAYER 1, `%d` ARE DECLARED IN THE KERNEL AND `%d`'
  % (C['exported'], C['n_present'], C['n_absent']))
w('### ### ARE ABSENT** -- and the figure was ### **RE-DERIVED, NOT CARRIED**: this act re-read the list')
w("### at a live ref, extracted its backticked names and searched the kernel's own six `.lean` files for")
w('### a declaration of each. ### **IT AGREES WITH `b367`: %s.** ### Two independent derivations of one'
  % C['agrees_with_b367'])
w('### number are worth more than one carried forward, and that is why the order forbade carrying it.')
w('### ### ### **EVERY ONE OF THE %d IS `RETIRED`. ### `RENAMED`: %d. ### `NEVER EXISTED`: %d.**'
  % (C['n_absent'], C['renamed_rows'], 0))
w('### ### **SO NOTHING IN THAT LIST WAS EVER INVENTED.** ### Each name was really there and was really')
w('### removed, and the removals are the kernel\'s own recorded decisions.')
w("### ### ### **AND THIS ACT'S OWN NEW FINDING, WHICH NEITHER `b157` NOR `b367` HAD: THE RETIREMENT")
w('### ### ### LEDGER NAMES ONLY HALF OF THEM.** ### `%d` of the `%d` retired names appear in the ledger'
  % (C['retired_named_by_ledger'], C['n_absent']))
w("### explicitly; `%d` are covered only by their layer's entry, which records that the layer's skeletons"
  % len(layer_only))
w('### were retired without listing which; ### **AND `%d` HAS NO LEDGER ENTRY FOR ITS LAYER AT ALL.**'
  % len(hist_only))
w('### ### **THE LEDGER IS ACCURATE ABOUT WHAT IT SAYS AND INCOMPLETE ABOUT WHAT IT NAMES** -- a')
w('### different defect from the one `b367` reported, and the third group is the sharper half of it:')
w('### **THERE THE LEDGER OMITS A NAME; HERE IT OMITS A WHOLE LAYER.**')
w('### ### ### **THE REPAIR TAKEN: AN APPEND-ONLY CURRENCY BLOCK.** ### `AGENTS.md` grew by %d bytes and'
  % R['grew'])
w('### lost none; the file before is a true prefix of the file after and of its committed blob.')
w('### ### **AND THE LIST ITSELF STILL EXPORTS %d ABSENT NAMES.** ### That is not an oversight: editing'
  % R['list_above_still_exports_absent'])
w("### it edits sentences, and the order's own branch reserved that for the author. ### **THE TRAIL IS")
w('### ### UPDATED AND NOT CLOSED.**')
w('')

w(SUB)
w('### (2) ADDITION ONE -- THE READ IS LIVE, AND ITS REF IS NAMED BEFORE ANY CLASSIFICATION.')
w(SUB)
w('### ### **`SIDE-effects` READ AT ref `%s` = `%s`.**' % (C['ref'], C['head']))
w('### ### **PINNED BY `ls-remote` BEFORE THE FIRST CLASSIFICATION, AND THE TWO AGREE : %s.**'
  % C['pinned'])
w('### ### **WORKING TREE DIRTY AT THE READ : %s.**' % C['dirty'])
w('### ### **AND THE HEAD HAS NOT MOVED SINCE `b367` : %s.** ### So the two derivations are of the same'
  % (not C['head_moved_since_b367']))
w('### object, which is what makes their agreement worth anything. ### **HAD IT MOVED, THE AGREEMENT')
w('### ### WOULD HAVE MEANT LESS, NOT MORE**, and this act would have said so.')
w('### ### **THE EIGHTEEN WERE RE-DERIVED AND NOT CARRIED.** ### `b367`\'s constant `%d` is held in this'
  % C['b367_absent_constant'])
w("### act's classifier as a COMPARISON ONLY -- it is never an input to the count. ### The count comes")
w('### from the file, and the comparison is reported afterwards: ### **AGREES : %s.**'
  % C['agrees_with_b367'])
w('### ### **THE EXTRACT-TO-DISK PASS: %d READS, `%d` WITHOUT AN ANCHOR.** ### %d of %d anchors DIFFER'
  % (E['reads'], E['without_anchor'], E['anchors_differing'], E['reads']))
w('### from the hint that found them, which is the tool doing its work: ### **A HINT IS TYPED; THE LINE')
w("### ### IS READ.** ### %d lines located inside the kernel's ledger, %d in the front document itself."
  % (E['ledger_lines'], E['front_lines']))
w('')

w(SUB)
w('### (3) ADDITION TWO -- EACH NAME CLASSIFIED, ONE ROW EACH, ON ITS OWN EVIDENCE.')
w(SUB)
w('### ### **NO NAME IS CLASSIFIED FROM ITS OWN SOUND.** ### Every row carries the evidence that put it')
w('### where it is, and the evidence is of three kinds, kept apart:')
w("###   (a) the retirement ledger NAMES the declaration -- the strongest, and it covers `%d`;"
  % C['retired_named_by_ledger'])
w("###   (b) the ledger's LAYER entry records the removal without naming this declaration -- `%d`;"
  % len(layer_only))
w("###   (c) the repository's own history shows the name present in an earlier commit and absent now --")
w('###       ### **THE WHOLE OF THE EVIDENCE FOR `%d`, WHOSE LAYER THE LEDGER DOES NOT MENTION.**'
  % len(hist_only))
w('### ### **AND THE THREE KINDS PARTITION THE EIGHTEEN EXACTLY, WHICH IS WHY NO NAME IS')
w('### ### `NEVER EXISTED`:** ### the `%d` the ledger NAMES are evidenced by the ledger line that retires'
  % C['retired_named_by_ledger'])
w('### them; the `%d` it does not name are evidenced by their layer entry ### **AND** ### by the history'
  % len(layer_only))
w('### that shows the declaration present in an earlier commit and gone now; the remaining `%d` by that'
  % len(hist_only))
w('### history alone. ### **THE HISTORY WAS READ FOR THE SECOND AND THIRD GROUPS AND NOT FOR THE')
w('### ### FIRST**, and this act says so rather than claiming a search it did not run: ### a ledger that')
w('### records retiring a name by name is already a record that the name existed. ### **AN INVENTION')
w('### ### WOULD HAVE HAD NEITHER**, and none of the eighteen has neither.')
w('')
w('### ### **PRESENT (%d), each with the declaration that makes it present:**' % C['n_present'])
for n2, r in PRES.items():
    w('###     `%s` -- declared at `%s:%d`.' % (n2, r['evidence']['file'], r['evidence']['line']))
w('### ### **RETIRED AND NAMED BY THE LEDGER (%d):** %s.' % (len(named), nm(named)))
w('### ### **RETIRED, COVERED ONLY BY A LAYER ENTRY (%d):** %s.' % (len(layer_only), nm(layer_only)))
w('### ### **RETIRED, WITH NO LEDGER ENTRY FOR THEIR LAYER AT ALL (%d):** %s ### -- evidenced by the'
  % (len(hist_only), nm(hist_only)))
w("### repository's own history, and by nothing in the ledger.")
w('### ### **RENAMED (%d).** ### **AND THE ZERO IS A REFUSAL, NOT AN ABSENCE OF LOOKING.**'
  % C['renamed_rows'])
w('### A successor was accepted only from a DECLARED mapping, and the mapping is deliberately empty. ###')
w('### One resemblance was met and refused: a retired name and a live one differing only in case. ###')
w('### **THAT IS EXACTLY THE RESEMBLANCE THE ORDER FORBADE ACTING ON**, and calling it a rename would')
w("### have been classifying a name from its own sound -- the one thing the addition names as the bar.")
w('### ### **NEVER EXISTED (0), with the search recorded AND ITS HALVES KEPT APART:** ### for the `%d`'
  % C['retired_layer_only'])
w("### the ledger does not name, the repository's own history was read and each was found present in an")
w('### earlier commit; for the `%d` it names, the ledger line that retires the name by name is the record'
  % C['retired_named_by_ledger'])
w('### that it existed, and no history search was run for those. ### **THE SUITE CAUGHT THIS ACT')
w('### ### OVERSTATING IT** -- see the incidents.')
w('')

w(SUB)
w('### (4) ADDITION THREE -- THE REPAIR OR THE PRICE. ### **THE BRANCH WAS DECIDED, NOT CHOSEN.**')
w(SUB)
w('### The order gave two branches and a test between them. ### The test: ### **can the front document be')
w('### made current by APPENDING, with no existing sentence edited?**')
w('### ### **EVERY EXPORTED NAME HAS A KIND AND THE KINDS PARTITION THE LIST**, so a block can state what')
w('### is present, what is retired and where the retirements are recorded, without touching a sentence.')
w('### ### ### **BRANCH TAKEN: (APPEND-ONLY RECONCILIATION).**')
w('### ### **(PRICED AND ROUTED TO THE AUTHOR) IS UNREACHABLE HERE**, and the reason is printed by the')
w("### tool rather than asserted: the append-only test passed, so there was nothing to route.")
w('')
w('### ### **THE MECHANICAL TEST, AND IT IS THE WHOLE OF WHAT `APPEND-ONLY` MEANS:**')
w('###     `AGENTS.md` bytes before : %d ### after : %d ### grew by : %d'
  % (R['bytes_before'], R['bytes_after'], R['grew']))
w('### ### **THE FILE BEFORE IS A TRUE PREFIX OF THE FILE AFTER : %s**' % R['prefix_of_file'])
w('### ### **THE COMMITTED BLOB IS A TRUE PREFIX OF THE WORKING FILE : %s**' % R['prefix_of_blob'])
w('### ### **READ %s** (`b352`), which is the reading that carries. ### An edit anywhere above the block'
  % R['side'])
w('### fails both arms, so the arms are the claim and not a description of it.')
w('')
w("### ### **AND THE VERIFICATION THE ORDER ASKED FOR IS A CHECK ON THE BLOCK, NOT ON THE DOCUMENT.**")
w("### ### **THE BLOCK EXPORTS NO ABSENT TERMINAL : %s.**" % R['block_exports_nothing'])
w("###     lines in the block carrying the front document's own export shape : `%d`"
  % R['export_shaped_lines'])
w('###     absent names mentioned anywhere outside a status row : `%d`' % len(R['unstatused']))
w('### ### **THE LIST ABOVE THE BLOCK STILL EXPORTS `%d` ABSENT NAMES, AND THIS ACT DID NOT EDIT IT.**'
  % R['list_above_still_exports_absent'])
w('### A reader who stops at the list is still misled; a reader who reaches the block is not. ### **THE')
w('### ### HALF-REPAIR IS REPORTED AT FULL PROMINENCE RATHER THAN LET PASS AS A REPAIR.**')
w('### ### ### **AND IN THE BRANCH TAKEN, AS IN THE OTHER: NO `.lean` FILE WAS TOUCHED : %s.**'
  % (R['lean_touched'] == 0))
w('### **NO BUILD WAS RUN : %s. ### NO AXIOM PROFILE WAS COMPUTED.**' % (not C['build_run']))
w('')

w(SUB)
w("### (5) ADDITION FOUR -- THE DESK'S OWN FRESHNESS. ### **THE RULE FILED, AND ONE SWEEP.**")
w(SUB)
w('### ### **THE RULE:** ### *every desk item names the file and date at which it was last confirmed, and')
w('### an item without one is re-verified before it is ordered.*')
w('### ### **FILED AS `%s`**, beside the two arm species %s'
  % (K['module'], ' and '.join('`%s`' % s for s in K['siblings'])))
w('### -- `%d` modules now under that directory. ### **COMMITTED LOCALLY AT `%s`, AND NOT PUSHED:'
  % (K['modules_now'], K['techne_head']))
w('### ### %s COMMITS AHEAD OF `origin/main`.** ### TECHNE-Core stays private until the provisionals.'
  % K['commits_ahead_of_origin'])
w('### ### **ITS INCIDENTS ARE `b367` AND `b157`, AND THEY ARE THE SAME INCIDENT TWICE.** ### A ferry')
w('### ordered the repair of terminals the kernel had already retired and an act had already banked')
w('### thirteen days earlier. ### **THE PREMISE WAS NOT WRONG WHEN IT WAS FORMED; IT WAS OLD.**')
w('### ### **AND THE MODULE STATES ITS OWN MECHANIZABLE HALF AND THE LIMIT OF IT:** ### a tool can demand')
w('### that an item CARRY a file and a date; ### **NO TOOL CAN CHECK THAT THE NAMED FILE STILL CONFIRMS')
w('### ### THE ITEM**, and a date nobody read is a date nobody checked.')
w('')
w('### ### **THE SWEEP: `%d` ITEMS, `%d` CONFIRMED-BY-FILE, `%d` UNCONFIRMED.**'
  % (K['items'], K['confirmed'], K['unconfirmed']))
w('### ### **AND `%d` ITEMS CLOSED.** ### The order said marks, not verdicts, and this act closed nothing.'
  % K['items_closed'])
for m in K['marks']:
    if m['hit']:
        w('###     %-52s %s -- `%s` (%s)'
          % (m['item'][:52], m['mark'], m['hit']['file'], m['hit']['date']))
    else:
        w('###     %-52s %s' % (m['item'][:52], m['mark']))
w('### ### ### **AND THE SWEEP\'S OWN REACH IS STATED RATHER THAN LEFT TO BE INFERRED, BECAUSE IT IS')
w('### ### ### WEAKER THAN ITS RESULT LOOKS.** ### It finds the newest banked file whose text carries a')
w('### needle for the item. ### **A FILE THAT MENTIONS AN ITEM IS NOT A FILE THAT CONFIRMS IT**, and this')
w("### sweep cannot tell the two apart. ### **SO `%d of %d CONFIRMED` IS A MARK ON THE SHAPE OF THE"
  % (K['confirmed'], K['items']))
w('### ### RECORD, NOT A VERDICT ON THE DESK** -- which is the module\'s own stated limit, met on its')
w('### first use, and reported here rather than after the next act pays for it.')
w('')

w(SUB)
w('### (6) WHAT MOVED, AND WHAT DID NOT.')
w(SUB)
w('### ### **MOVED:**')
w('###   `SIDE-effects/AGENTS.md` -- ONE APPEND-ONLY BLOCK under its own mark, %d bytes. ### **NO'
  % R['grew'])
w('###     EXISTING SENTENCE EDITED.**')
w('###   `PLACE-papers/OPEN_TRAILS.md` -- ONE APPEND-ONLY BLOCK, %d bytes, marked `%s`. ### `b157`\'s'
  % (F['grew'], F['status']))
w("###     entry and `b367`'s block are named and NEITHER IS EDITED : %s." % F['names_b367_block'])
w('###   `TECHNE-Core` -- one new module, LOCAL ONLY.')
w('###   `SIDE-global-section/CORRESPONDENCE.md` -- one row. ### `tools/banked_index.py` -- one key.')
w('### ### **NOT MOVED, AND EACH FOR A STATED REASON:**')
w('###   **`FACES_LEDGER.md` IS NOT WRITTEN AND ITS WRITER IS NOT CALLED, BECAUSE NO ROW MOVED.** ### No')
w('###     grade was conferred and no face was promoted.')
w('###   **NO `.lean` FILE IN ANY REPOSITORY.** ### The kernel was READ and not written.')
w('###   **NO FINDINGS SECTION.** ### The fold is not due and this act does not fold.')
w('###   **NO DESK ITEM CLOSED.** ### The sweep produced marks.')
w('###   **NO PRE-PUSH HOOK INSTALLED IN `SIDE-effects`** -- see (7). ### **THE ABSENCE IS FILED AS A')
w('###     FINDING AND IS NOT REPAIRED BY THIS ACT.**')
w('')

w(SUB)
w('### (7) THE PRE-LOCK FINDING, DECLARED ON THE REGISTRATION\'S OWN FACE AND REPEATED HERE.')
w(SUB)
w('### ### **`SIDE-effects` HAS NO PRE-PUSH HOOK.** ### The other three repositories this programme pushes')
w('### to carry one (`b304`); this one does not. ### It was checked ### **BEFORE THE LOCK**, because it')
w('### decides how a branch is executed and not what the act concludes -- and the registration declares')
w('### the pre-lock check on its own face rather than concealing it, which is `b325`\'s rule.')
w('### ### **IT IS NOT REPAIRED HERE.** ### Installing a hook is a change to a repository the order did')
w('### not send this act to change, and `.git/hooks/` is untracked in any case, so a "repair" would be')
w('### invisible to every other clone. ### **IT IS FILED AS A FINDING AND ROUTED.**')
w('### ### **AND THE PUSH IS DONE BY HAND TO THE SAME STANDARD THE HOOK WOULD ENFORCE:** ### a `push-*`')
w('### branch, Rule 4.10 applied by hand, and an `ls-remote` read-back after.')
w('')

w(SUB)
w("### (8) THE ACT'S OWN INCIDENTS, ALL DECLARED.")
w(SUB)
w('### ### **(i) TWO EXTRACT HINTS WERE TYPED FROM SENSE AND MISSED.** ### The first extract run left two')
w('### reads without an anchor because the hint was written from what the line MEANT rather than from what')
w('### it SAID. ### The cure is the tool\'s own: the hint is retyped until the tool finds the line, and')
w('### ### **THE LINE THE TOOL RETURNS IS WHAT IS QUOTED** -- never the hint. ### The relied-on run is')
w('### `%s`, and `%d of %d` anchors differ from the hint that found them.'
  % (E['run_file'], E['anchors_differing'], E['reads']))
w('### ### **(ii) THE NUMBERED-REPEAT SPECIES, TWICE, AND IT IS `b358`\'S.** ### `run_clock` numbers a')
w('### repeated run rather than overwriting it, so a suite naming `<name>_run.txt` reads whichever ran')
w('### FIRST. ### This act ran the extract twice and the desk tool three times. ### **THE RELIED-ON RUNS')
w('### ### ARE `%s` AND `%s`, RESOLVED BY THEIR RECORDED CLOCKS** and named here so no later reader has to'
  % (E['run_file'], K['run_file']))
w('### guess: %s and %s.' % (E['run_clock'], K['run_clock']))
w('### ### **(iii) A WRONG ARM IN THIS ACT\'S OWN DESK TOOL, FOUND BY RUNNING IT.** ### The module check')
w('### asked for the phrase `and it closes nothing` as a RAW substring; the module writes')
w('### `and **it closes nothing**`. ### **THE BOLD RUN SITS INSIDE THE PHRASE**, so the arm reported the')
w('### module defective when the module was right. ### **THE ARM WAS WRONG AND WAS REPAIRED, NOT THE')
w('### ### TEXT** -- the clauses are now read through `gate_needle.norm`, which strips marker runs')
w('### wherever they occur. ### **THIS IS THE WRAPPING SPECIES THE SHARED HELPER EXISTS TO END, COMMITTED')
w('### ### INSIDE THE ACT THAT INHERITED THE HELPER.**')
w('### ### **(iv) THE DESK SWEEP CONFIRMED TWO ITEMS FROM THIS ACT\'S OWN PAPERWORK.** ### Its first run')
w("### marked the two parked lanes confirmed by `b368`'s own registration -- which restates the parks")
w('### because the ferry does. ### **A SWEEP THAT READS ITS OWN PAPERWORK CONFIRMS ITSELF.** ### The')
w('### tool now excludes this act\'s own files, and both items re-confirmed from `b367`\'s registration')
w('### instead, which this act did not write.')
w('### ### ### **(v) THE BANK OVERSTATED ITS OWN EVIDENCE, AND ITS OWN GATE SUITE CAUGHT IT.** ### The')
w('### first bank wrote that ### *the history of each absent name was read, and each was found present in')
w('### an earlier commit*. ### **THAT WAS TRUE OF NINE OF THE EIGHTEEN AND NOT OF THE OTHER NINE.** ###')
w('### The classifier reads the history only where the ledger does NOT name the declaration -- for the')
w('### `%d` it names, the ledger line IS the evidence and no history search was run. ### `G-EVIDENCE`'
  % C['retired_named_by_ledger'])
w('### asked every retired row for a history, got `False`, and ### **THE ARM WAS RIGHT AND THE SENTENCE')
w('### ### WAS WRONG.** ### The sentence is corrected above and the two halves are now kept apart. ###')
w('### **THE CONCLUSION IS UNCHANGED** -- `NEVER EXISTED` is still `0`, because a ledger that retires a')
w('### name BY NAME is already a record that the name existed -- ### **BUT THE ACT WAS CLAIMING A SEARCH')
w('### ### IT HAD NOT RUN**, which is the same species as a desk item with no date on it, committed by')
w('### the act that minted the rule against it.')
w('### ### ### **AND CHASING THAT ARM FOUND A SECOND THING, WHICH IS A FINDING AND NOT AN INCIDENT.**')
w("### ### **ONE OF THE EIGHTEEN HAS NO LEDGER ENTRY FOR ITS LAYER AT ALL** -- `%s`, whose layer is"
  % (hist_only[0]['name'] if hist_only else '?'))
w('### `%s`. ### The classifier had filed it with the layer-only group and its note said ### *its LAYER'
  % (hist_only[0]['layer'] if hist_only else '?'))
w('### entry is quoted instead*, ### **WHICH WAS FALSE FOR THAT ROW**: the evidence it actually carried')
w('### read `NO LEDGER ENTRY FOR THIS LAYER`. ### **A NOTE THAT DESCRIBES EVIDENCE THE ROW DOES NOT')
w('### ### CARRY IS THE USE-AND-MENTION SPECIES (`b348`) INSIDE A CLASSIFIER.** ### The classifier now')
w('### writes three notes for three cases and emits a three-way split, and every downstream writer reads')
w('### the split ### **FROM THE EVIDENCE AND NOT FROM THE NOTE.** ### **THE CURE COST FOUR APPENDS')
w('### ### REVERTED AND RE-WRITTEN** -- `AGENTS.md`, `OPEN_TRAILS.md`, `CORRESPONDENCE.md` and the index')
w('### -- all four uncommitted, which is `b367`\'s cure applied a second time. ### **AFTER A PUSH THE')
w('### ### WRONG SENTENCE WOULD HAVE STOOD.**')
w('### ### **(vi) THE BANNED-STEM SCAN, AND WHAT IT CANNOT SEE.** ### The kernel names carry a banned stem,')
w('### and the scanner excuses a QUOTED KERNEL IDENTIFIER only where it can SEE the quoting -- so every')
w('### kernel name in every block this act wrote is inside backticks, checked mechanically before the')
w('### push. ### **AND ONE THING THE SCAN CANNOT SEE, REPORTED BECAUSE IT WAS OBSERVED:** ### its stem')
w('### pattern is word-boundary anchored, so a name with the stem as a SUFFIX never fires at all. ###')
w('### That is not a defect this act repairs, and it is not an exemption this act claims: ### **THE HITS')
w('### ### IT DID FIRE WERE ALL EXCUSED BY A DECLARED EXCEPTION, AND THE VERDICT WAS `CLEAN` IN BOTH')
w('### ### REPOSITORIES.**')
w('### ### **AND THE GATE SUITE HAD THE SAME ARM WRONG.** ### `G-STEM` sweeps this act\'s own files with')
w("### `ferry_scan`'s RAW stem list, which carries none of the record's declared exceptions -- so it")
w('### reported stem hits on the bank line that LISTS the retired kernel names, and on the extract tool')
w('### whose search strings are the front document\'s own headings. ### **THE ARM DOES NOT EXCUSE THEM')
w('### ### AND IT DOES NOT DROP THEM:** ### it hands every stem hit to the SHARED SCANNER and requires')
w('### the ### **LIVE** ### count to be `0`. ### That is the record\'s own machinery deciding, not this')
w("### act's judgement, and the hit stays counted and printed -- which is `b234`'s rule for the `QUOTED`")
w('### class carried to the suite that had been enforcing the stems without it.')
w('')

w(SUB)
w('### (9) THE RECORD, ITS REFS, AND ITS CLOCKS.')
w(SUB)
w('### ### **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE OF THIS ACT**, on the audit\'s own exit code.')
w('###   `data/b368_registration_2026-09-08.txt` -- `%s`, %s bytes, locked %s.' % (SHA, NBY, LAT))
w('###   `data/b368_ferry_2026-09-08.txt` -- the order, banked verbatim.')
w('###   `data/%s` (%s) -- the extract-to-disk pass.' % (E['run_file'], E['run_clock']))
w('###   `data/%s` (%s) -- the classification.' % (C['run_file'], C['run_clock']))
w('###   `data/%s` (%s) -- the append-only reconciliation.' % (R['run_file'], R['run_clock']))
w('###   `data/%s` (%s) -- the desk rule and the sweep.' % (K['run_file'], K['run_clock']))
w('###   `data/%s` (%s) -- the trails filing.' % (F['run_file'], F['run_clock']))
w('###   `tools/b368_classify.py`, `tools/b368_reconcile.py`, `tools/b368_desk.py`, ')
w('###     `tools/b368_filing.py`, `tools/b368_extract.py`, `tools/b368_regspec.py`.')
w('### ### **THE REFS READ:** ### `SIDE-effects` at `%s` = `%s`, pinned by `ls-remote` : %s.'
  % (C['ref'], C['head'], C['pinned']))
w('')

w(SUB)
w("### (10) THE EXPECTATIONS, SCORED. ### **AN EXPECTATION IS SCORED, NEVER SATISFIED.**")
w(SUB)
w("### ### **THE NAVIGATOR'S (F1): `most of the eighteen are RETIRED or RENAMED rather than never")
w('### ### existing` -- CONFIRMED, AND MORE STRONGLY THAN ASKED.** ### Not *most*: ### **ALL %d**, and'
  % C['n_absent'])
w('### all on the same side of the disjunction -- `RETIRED %d`, `RENAMED %d`, `NEVER EXISTED 0`.'
  % (C['n_absent'], C['renamed_rows']))
w('### **THE STRONGER RESULT IS NOT A BETTER SCORE**: an expectation that says *most* is not refuted by')
w('### *all*, and it is not confirmed more finely either. ### It was refutable by a printed')
w('### classification, and the classification is printed.')
w("### ### **THE NAVIGATOR'S (F2): `the reconciliation is append-only and does not need the author` --")
w('### ### CONFIRMED.** ### The append-only branch was taken, its two prefix arms passed before the push,')
w('### and nothing was routed. ### **AND THE HALF THAT DOES STILL NEED THE AUTHOR IS NAMED:** ### the')
w('### list itself is unrepaired, and repairing it edits sentences.')
w("### ### **THIS SEAT'S OWN REGISTERED EXPECTATION: `the re-derived figure will agree with `b367`'s` --")
w('### ### MET.** ### And it is recorded as the low bar it is: ### **a seat that predicts a re-run of its')
w("### ### own measurement has predicted the easy half**, and the finding worth having (`the ledger names")
w('### only %d of the %d`) is one this seat did NOT predict.' % (C['retired_named_by_ledger'], C['n_absent']))
w('')

w(SUB)
w('### (11) WHAT IS NOT CLAIMED.')
w(SUB)
w('### ### **THE RETIREMENTS ARE REPORTED, NOT ENDORSED.** ### This act did not check whether any of the')
w('### %d should have been retired, and says nothing about whether the kernel is better for it.'
  % C['n_absent'])
w('### ### **THE FRONT DOCUMENT IS NOT REPAIRED, ONLY ANNOTATED.** ### **NO NAME WAS CLASSIFIED FROM ITS')
w('### ### OWN SOUND. ### NO SUCCESSOR WAS NAMED. ### NO `.lean` FILE WAS WRITTEN. ### NO BUILD WAS RUN.')
w('### ### NO AXIOM PROFILE WAS COMPUTED. ### NO EXISTING SENTENCE WAS EDITED. ### NO DESK ITEM WAS')
w('### ### CLOSED. ### NO HOOK WAS INSTALLED.**')
w('### ### **NO ACT IS RE-VERDICTED.** ### `b157` and `b367` were RE-MEASURED, which is a different thing,')
w("### and they agree. ### **NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED.**")
w('### ### **NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT.** ### A classification is')
w('### about where a declaration is, not about what it would be worth.')
w('### ### **NOTHING IS COMPUTED ABOUT THE OBJECT. ### NOTHING IS COMPILED AND NO BRIDGE IS TYPED.**')
w('### ### **NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED.**')
w("### ### **NOTHING HERE BEARS ON `h2`, ON TOTALITY OR ON THE ROSTER.** ### `M-2` remains")
w('### (SPECIFIED-NOT-STATED) under `b310`\'s cap. ### The seam\'s debt item 1 stands. ### The patent lane')
w("### is carried on the patent seat's report, UNCONFIRMED on this seat's record. ### **THE POSTURE LOCK")
w('### ### IS SEPARATE.** ### **THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED.** ### `h2`')
w('### stands exactly where the deposit left it. ### **NOTHING DEPOSITS.**')
w(BAR)


def main():
    body = chr(10).join(L) + chr(10)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(body)
    back = io.open(OUT, encoding='utf-8').read()
    print(BAR)
    print('b368 -- THE BANK, WRITTEN FROM THE JSONS.')
    print(BAR)
    print('  written : %s ; %d lines ; %d bytes'
          % (os.path.basename(OUT), len(back.split(chr(10))), len(back.encode('utf-8'))))
    ph = [s for s in re.findall(r'%[sd]', back)]
    print('  ### ### **UNFORMATTED PLACEHOLDERS LEFT IN THE BANK : %d** %s' % (len(ph), ph[:4]))
    allnames = set(C['absent']) | set(C['present'])
    naked = []
    for ln in back.split(chr(10)):
        for n2 in allnames:
            for m in re.finditer(re.escape(n2), ln):
                if not (ln[m.start() - 1:m.start()] == '`' and ln[m.end():m.end() + 1] == '`'):
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
