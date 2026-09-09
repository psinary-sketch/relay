# -*- coding: utf-8 -*-
"""b379_bank.py -- THE BANK, WRITTEN FROM THE ACT'S OWN JSONS. ### **NO FIGURE IS TYPED.**"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import row_categories as RC   # noqa: E402
import run_clock              # noqa: E402

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b379_the_apparatus_axis_rescored.txt')
REG = os.path.join(D, 'b379_registration_2026-09-08.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, LG, RS, SV, HD, FL, Q = (J('b379_reads'), J('b379_lockgate'), J('b379_rescore'),
                            J('b379_survivors'), J('b379_hand'), J('b379_filings'),
                            J('b379_desk'))
regtxt = io.open(REG, encoding='utf-8').read()
SHA = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt).group(1)
NBY = re.search(r'bytes locked : (\d+)', regtxt).group(1)
LAT = re.search(r'locked at \(UTC\) : (\S+)', regtxt).group(1)
NCL = len(J('b379_satisfiable')['clauses'])

L = []


def w(s=''):
    L.append(s)


BAR, SUB = '=' * 100, '-' * 100
PB, CB = RS['prior_bplus'], RS['corrected_bplus']
MOVED, INTO = len(RS['gained']), len(RS['moved_into_both'])
PQ, CQ = RS['prior_quadrants'], RS['corrected_quadrants']
CARRIED, NOTLOC = len(SV['assigned']), SV['not_located']

w(BAR)
w('b379 -- THE APPARATUS AXIS RE-SCORED, AND TWO FILINGS. ### THE BANK.')
w(BAR)
w('')
w('### ### ### **THE HEADLINE, AND IT IS TWO SENTENCES BECAUSE THE SECOND IS THE ONE THAT MATTERS:**')
w('### ### ### **THE SUSPECT COLUMN WAS UNDERCOUNTING, AND CORRECTING IT MOVED NOTHING WHERE THE')
w('### ### ### RULING NEEDS MOVEMENT.**')
w('### The apparatus axis goes from ### **`%d` TO `%d`** ### under a matcher that accepts the bare'
  % (PB, CB))
w('### dialect as well as the dotted -- ### **`%d` GAINED, NONE LOST.** ### And ### **EVERY ONE OF THE'
  % MOVED)
w('### ### `%d` CAME OUT OF A ROW WHERE THE ROLE AXIS SAYS `A?`**, so ### **`%d` DOCUMENTS MOVED INTO'
  % (MOVED, INTO))
w('### ### THE BOTH-AXES QUADRANT.**')
w('### ### ### **`(F1)` IS MET AND `(F2)` IS REFUTED, BOTH BY THE SAME PRINTED TABLE.**')
w('### ### **THE CORRECTION ENLARGES THE APPARATUS COLUMN AND LEAVES THE ROLE COLUMN EXACTLY WHERE IT')
w('### ### WAS**, so the two axes come apart further rather than closer -- which is the opposite of')
w('### what a correction is usually hoped to do.')
w('')

# ---------------------------------------------------------------------------------- ADDITION ONE
w(SUB)
w('### ADDITION ONE -- THE DIRECTION, REGISTERED BEFORE THE RUN.')
w(SUB)
w('### ### **A WIDENED MATCHER FINDS MORE, NEVER FEWER.** ### The one change is one line of pattern:')
w('### `b376` required a terminal ### **CONTAINING A DOT**; this act accepts that ### **OR** ### a')
w('### bare Lean-shaped name. ### Everything else -- kernel, pin, grade, the table-row test, the')
w('### concordance rule -- is `b376`s, ### **IMPORTED AND UNTOUCHED.**')
w('### ### **SO THE WIDENED PATTERN MATCHES A STRICT SUPERSET OF THE OLD ONE**, and that is what')
w('### makes the monotonicity bar meaningful rather than hopeful.')
w('### ### **THE THREE CONSEQUENCES WERE REGISTERED ON THE LOCKED FACE BEFORE THIS RAN:** ### the')
w('### corrected population bounded below by the prior one; the both-axes quadrant able only to grow;')
w('### `A?B-` and `A-B-` able only to shrink. ### **A DOCUMENT THAT LOST A MARK WOULD HAVE BEEN A')
w('### ### DEFECT IN THE INSTRUMENT, REPORTED AS ONE AND NEVER AS A FINDING ABOUT THE CORPUS.**')
w('###   documents that lost ground : ### **%d** ### / gained : ### **%d**' % (len(RS['lost']), MOVED))
w('###   ### **MONOTONICITY : %s**' % ('HELD' if RS['monotone'] else '### VIOLATED'))
w('### ### **AND THE PRIOR COLUMN WAS RE-RUN FROM THE ORIGINAL PREDICATE ON THE SAME BYTES**, not')
w('### trusted from its banked JSON -- ### **SO THE TABLE BELOW COMPARES TWO INSTRUMENTS AND NOT AN')
w('### ### INSTRUMENT AGAINST A RECOLLECTION.** ### disagreements with `b376`s own JSON : ### **%d**'
  % len(RS['prior_column_mismatches']))
w('')
w('### **THE QUADRANT TABLE, PRIOR AND CORRECTED, CELL BY CELL:**')
w('###   %-8s %-10s %-10s %s' % ('cell', 'prior', 'corrected', 'movement'))
w('###   %s' % ('-' * 66))
for c in ('A+B+', 'A+B-', 'A-B+', 'A-B-', 'A+B?', 'A-B?', 'A?B+', 'A?B-', 'A?B?'):
    a, b = PQ.get(c, 0), CQ.get(c, 0)
    w('###   %-8s %-10d %-10d %s' % (c, a, b, 'same' if a == b else '### **%+d**' % (b - a)))
w('###   %-8s %-10d %-10d ### **BOTH PARTITION THE SAME %d DOCUMENTS.**'
  % ('total', sum(PQ.values()), sum(CQ.values()), RS['swept']))
w('')
w('### ### **`(E1)`, THIS SEAT`S, IS MET:** ### the movement was predicted to concentrate in the')
w('### silent rows rather than in `A+B-`, and ### **ALL OF IT DID.**')
w('')
w('### **WHICH OF THE RULING`S OPTIONS THE CORRECTION WEAKENS. ### NONE IS RECOMMENDED.**')
w('###   ### **OPTION 1, AXIS B ALONE** -- ### **NOT WEAKENED IN ITS EVIDENCE**: axis B is still the')
w('###     decidable axis. ### **ITS COST IS RESTATED**: it would admit `%d` documents rather than' % CB)
w('###     `%d`.' % PB)
w('###   ### **OPTION 2, AXIS A ALONE** -- ### **UNTOUCHED.** ### This act did not run axis A.')
w('###   ### **OPTION 3, BOTH CONJOINED** -- ### **WEAKENED IN ITS STRICTNESS ARGUMENT.** ### The')
w('###     conjunction holds the same `%d` documents it always did, so the correction did not make it'
  % CQ.get('A+B+', 0))
w('###     stricter and the distance between the two columns it must bridge is now wider.')
w('###   ### **OPTION 4, TWO MARKS** -- ### **STRENGTHENED IN ONE RESPECT ONLY:** ### the axes')
w('###     demonstrably came apart further. ### **THAT IS A CONSEQUENCE AND NOT A RECOMMENDATION.**')
w('###   ### **OPTION 5, RETIRE THE WORD** -- ### **UNTOUCHED.**')
w('### ### **AND THE HONEST WARNING:** ### the corrected column is ### **THIS SEAT`S SECOND')
w('### ### PREDICATE, NOT A GROUND TRUTH.** ### It is wider than `b376`s and may still be narrower')
w('### than the corpus. ### **`b376`S COLUMN WAS ALSO BELIEVED WHEN IT WAS WRITTEN.**')
w('')

# ---------------------------------------------------------------------------------- ADDITION TWO
w(SUB)
w('### ADDITION TWO -- THE ROW CATEGORIES. ### **A CATEGORY REPORTED AS AN ABSENCE IS A FALSE DEFECT.**')
w(SUB)
w('### `tools/row_categories.py`, ### **NEW AND SHARED**, so a later checker imports it rather than')
w('### rediscovering the distinction.')
w('### ### **THE FRONT DOOR`S OWN WORDS, CARRIED AND NOT REPLACED** (`%s`):' % RC.FRONT_DOOR)
w('###   | %s' % RC.FRONT_DOOR_QUOTE)
w('### ### **SO THE TAXONOMY IS EXTENDED, NOT INVENTED.** ### `MANUSCRIPT_RESIDENT` and')
w('### `RESEARCH_REACH` are the corpus`s; the three added are the ones `b378` met and the front door')
w('### has no word for: ### **%s.**' % ', '.join(SV['added_at_b379']))
w('### ### **FIXTURED IN BOTH POLARITIES** -- each category recognised where it applies and')
w('### ### **REFUSED WHERE IT DOES NOT**, because a recogniser that only ever says yes is not one.')
w('###   fixture cases : %d, all matching : %s' % (len(SV['fixtures']), SV['fixtures_ok']))
w('')
w('### **APPLIED TO `b378`S %d CARRIED NAMES:**' % CARRIED)
for k, v in sorted(SV['tally'].items(), key=lambda z: -z[1]):
    w('###   %-30s %d' % (k, v))
w('### ### ### **ONLY `%d` OF `%d` ARE `NOT_LOCATED` -- THE ONE CATEGORY THAT ASSERTS AN ABSENCE.**'
  % (NOTLOC, CARRIED))
w('### ### **A CHECKER WITH THESE CATEGORIES REPORTS `%d` DEFECTS WHERE THE OLD VOCABULARY REPORTED'
  % NOTLOC)
w('### ### `%d`.**' % CARRIED)
w('### ### **AND THE MODULE RETURNS A CATEGORY AND NEVER A VERDICT.** ### Naming a row a library')
w('### lemma says where the terminal lives; ### **IT DOES NOT SAY THE ROW IS RIGHT**, and a checker')
w('### that treats a category as a pass has made the opposite of `b378`s mistake.')
w('')
w('### **AND THE SURVIVORS, READ ONE STEP FURTHER FROM THE SENTENCE THAT NAMES EACH:**')
for k, v in sorted(SV['explanations'].items(), key=lambda z: -z[1]):
    w('###   %-36s %d' % (k, v))
w('### ### **NOT ONE DOCUMENT WAS REPAIRED AND NOT ONE NAME WAS INVENTED.** ### Where the sentence')
w('### does not decide, the answer is `UNDECIDED-BY-ITS-SENTENCE` rather than a guess --')
w('### ### **A READING OF A DOCUMENT IS NOT A VERDICT ON IT.**')
w('')

# ---------------------------------------------------------------------------------- THE HAND READ
w(SUB)
w('### THE DAY-1 DOCUMENT, READ BY HAND. ### **IT CARRIES APPARATUS.**')
w(SUB)
w('### **CHOSEN : `%s`** ### -- %s.' % (HD['chosen'], HD['chosen_by']))
w('### `b378` read `%s`; this act reads the other.' % os.path.basename(HD['already_done'])[:-3])
w('###   identifiers named, each with the sentence that names it : ### **%d**' % HD['named'])
w('###   ### **THE CATEGORIES : %s**' % HD['categories'])
w('###   ### **LOCATED IN A CORPUS KERNEL : %d ### / ### NOT LOCATED : %d**'
  % (HD['located'], HD['not_located']))
w('###   positive control held : %s ### / ### searches that could not run : %d'
  % (HD['control_held'], len(HD['grep_errors'])))
w('### ### ### **WHAT THE HAND READ DECIDES THAT THE TABLE SCAN COULD NOT:** ### the document')
w('### ### ### ### **%s.**' % HD['decided'])
w('### ### **AND THE QUESTION THE DRAFT PICKED THIS DOCUMENT FOR:** ### concordance language is')
w('### present on the page (### **%s**), so `b376`s `B?` was the right mark for a TABLE scan and'
  % HD['concordance_language'])
w('### ### **THE CORPUS`S OWN `CONCORDANCE-CARRIED` CLASS DOES DESCRIBE SOMETHING REAL THERE.**')
w('### ### **WHAT IT STILL DOES NOT DECIDE:** ### whether the document`s sentences about those names')
w('### are right. ### **LOCATING A NAME SAYS IT EXISTS AT THAT NAME.**')
w('### ### ### **THE OUTCOME IS A MARK, NOT A CLASS. ### NO DECLARATION WAS MOVED AND NOT ONE BYTE')
w('### ### ### WAS WRITTEN INTO THE DOCUMENT.**')
w('')

# ---------------------------------------------------------------------------------- ADDITION THREE
w(SUB)
w('### ADDITION THREE -- TWO FILINGS ABOUT A DOCUMENT OUTSIDE THE TREE.')
w(SUB)
w('### **FILING ONE -- THE VERSION AND CLASS DRIFT.**')
w('### **WHAT THE REGISTRY SAYS:**')
for r in FL['registry']:
    w('###   `%s` line %d -- %s' % (r['file'], r['line'], r['label']))
    w('###     | %s' % r['text'][:150])
w('### **WHAT OTHER DOCUMENTS SAY:**')
for r in FL['later']:
    w('###   `%s` line %d -- %s' % (r['file'], r['line'], r['label']))
    w('###     | %s' % r['text'][:150])
w('### **THE VERSIONS ON THE DISK, ENUMERATED AND NOT ASSUMED:**')
for v in FL['versions']:
    w('###   %-44s %8d bytes   sha256 `%s`' % (v['name'], v['bytes'], v['sha256'][:16]))
w('### ### ### **SO THIS IS NOT A PAIR OF DOCUMENTS DISAGREEING. ### IT IS A CHAIN THAT MOVED AND A')
w('### ### ### PRECEDENCE SOURCE THAT DID NOT** -- ### **`%d` VERSIONS SIT ON THE DISK**, and'
  % FL['n_versions'])
w('### ### that is `(E3)` as this act`s face registered it.')
w('### **THE PRECEDENCE RULE THE CORPUS STATES, QUOTED AND NOT INVENTED:**')
for r in FL['precedence']:
    w('###   `%s` line %d :' % (r['file'], r['line']))
    w('###     | %s' % r['text'][:150])
w('### ### **UNDER THAT RULE THE LATER DOCUMENTS ARE THE ONES OUT OF STEP** -- and ### **THAT IS A')
w('### ### STATEMENT ABOUT PRECEDENCE, NOT ABOUT WHICH DESCRIPTION IS CORRECT.** ### The registry may')
w('### be stale and the later documents may be right; ### **THE RULE SAYS WHERE THE ANSWER IS')
w('### ### RECORDED, NOT WHAT THE ANSWER IS.**')
w('### ### ### **FILED. ### THE REGISTRY IS NOT EDITED BY THIS ACT** -- a seat that edits the')
w('### precedence source to match a document that drifted has inverted the rule it is enforcing, and')
w('### ### **THE CHOICE BETWEEN UPDATING THE ROW AND CORRECTING THE OTHERS IS THE AUTHOR`S.**')
w('')
w('### **FILING TWO -- THE POPULATION QUESTION, FILED WHERE THE RULING`S EVIDENCE SITS.**')
w('###   the census population : ### **%d** ### tracked markdown documents in `PLACE-papers`'
  % FL['population'])
w('###   ### **THE DOWNLOAD-LAYER BOOK AMONG THEM : %d**' % FL['in_population'])
w('### ### ### **IT IS OUTSIDE THE REPOSITORY TREE BY RULING, SO IT WAS OUTSIDE THE POPULATION ON')
w('### ### ### BOTH AXES -- NOT SCORED `B-`, NOT SCORED `A?`, BUT NEVER CONSIDERED AT ALL.**')
w('### ### **AND THAT IS UNLIKE EVERY OTHER OMISSION THIS SEQUENCE HAS FOUND.** ### `b376`s')
w('### narrowness scored documents wrongly and this act corrected it; ### **THIS DOCUMENT WAS NEVER')
w('### ### SCORED, AND NO WIDENING OF A MATCHER WOULD HAVE REACHED IT.**')
w('### **WHY IT IS FILED WITH THE RULING`S EVIDENCE:** ### the corpus calls this one document a')
w('### ### **NARRATIVE KEYSTONE** ### in one place and ### **NON-KEYSTONE** ### in another. ### So')
w('### ### **THE RULING HAS TO SAY WHETHER IT GOVERNS DOCUMENTS OUTSIDE THE TREE**, and if it does,')
w('### ### **THE CENSUS`S POPULATION IS NOT THE RULING`S POPULATION.**')
w('### ### **NO OPTIONS ARE ENUMERATED HERE AND NONE IS RECOMMENDED. ### THE FACT IS FILED.**')
w('### ### **NEITHER FILING OPENS WORK ON THE DOCUMENT.** ### It was not read for content, not')
w('### classified, not graded, not moved, not renamed and not repaired.')
w('')

# ------------------------------------------------------------------------------------- WHAT IS NOT
w(SUB)
w('### WHAT THIS ACT DID NOT DO.')
w(SUB)
w('### ### **NO CLASS WAS RULED. ### NO DOCUMENT WAS RECLASSIFIED. ### NO DECLARATION WAS MOVED.')
w('### ### ### NO LIST WAS CLOSED.**')
w('### ### **NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND `REGISTRY.md` WAS NOT EDITED.**')
w('### ### **NOTHING ON THE DOWNLOAD LAYER WAS WRITTEN, MOVED, RENAMED OR REMOVED.**')
w('### ### **NO ARCHIVE FILE WAS TOUCHED** ### and the `86` `b378` left unconfirmed stay unconfirmed:')
w('### the draft said the executor would read silence on that choice as ### **NOT TAKEN**, the order')
w('### named three additions and none is the archive lane, and ### **THE READING IS ON THIS ACT`S')
w('### ### LOCKED FACE IN ADVANCE WHERE THE AUTHOR CAN CORRECT IT.**')
w('### ### **NO OWNER INSTRUMENT WAS EDITED** -- `b376_axes`, `b378_terminals`, `b378_lockgate` and')
w('### `gate_hash` are all ### **IMPORTED AND RUN UNMODIFIED**, which is what lets this act`s')
w('### side-by-side table mean anything.')
w('### ### **NO `.lean` FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED.**')
w('### ### **THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME, IN THE DESK`S OWN WORDS:**')
for _lst in ('the rows that cite at a ref nobody can name',
             'the rows grading a declaration the record has classified absent',
             'the undated figures across the roster',
             'the bibliography entries nothing cites'):
    w('###   ### **OPEN** ### -- %s' % _lst)
w('### ### **NONE IS CLOSED. ### NO NEW TRACKING DOCUMENT WAS CREATED.**')
w('### ### **NOTHING WAS COMPUTED ABOUT THE OBJECT.** ### `h2` stands exactly where the deposit left')
w('### it and this act makes no claim about it in either direction. ### The instrument lane stays')
w('### PARKED; the wave stays PARKED; nothing deposits.')
w('')

# ------------------------------------------------------------------------------------- THE LEDGER
w(SUB)
w('### THE EXPECTATIONS, THE DESK, THE WRITES, AND THE SPECIES.')
w(SUB)
w('### ### **`(F1)` MET.** ### `%d` against a prior `%d`.' % (CB, PB))
w('### ### **`(F2)` REFUTED BY THE PRINT.** ### `%d` documents moved into the both-axes quadrant.'
  % INTO)
w('### ### The reason is structural and not an accident: axis A marked only a handful of documents')
w('### ### `A+` at all, and ### **NONE OF THEM LACKED AN APPARATUS MARK TO GAIN.**')
w('### ### **`(E1)` MET.** ### The movement concentrated in the silent rows, as registered.')
w('### ### **`(E2)` PARTLY MET.** ### It predicted the option ruling on axis B alone would be')
w('### weakened most. ### **ITS EVIDENCE IS NOT WEAKENED -- AXIS B IS STILL THE DECIDABLE AXIS -- BUT')
w('### ### ITS COST IS RESTATED**, and the option most weakened is arguably the conjunction, whose')
w('### strictness argument did not survive the correction.')
w('### ### **`(E3)` MET.** ### `%d` versions on the disk: a chain, not an oversight.' % FL['n_versions'])
w('')
w('### desk items swept : %d ### / ### closed : %d ### / ### standing : %d ### / ### lists closed : %d'
  % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
w('### ### **AND THE ONE CLOSURE IS `b376`S AXIS-B COLUMN**, closed under `(R7)` because `b378` said')
w('### re-measuring it was an act and ### **THIS IS THAT ACT.**')
w('### trail block appended (append-only %s, committed prefix intact %s); `CORRESPONDENCE.md` row %s;'
  % (Q['trail']['appended_only'], Q['trail']['committed_prefix_intact'], Q['row']))
w('### index key `the-suspect-column-re-measured` reachable by every alias : %s' % Q['key_ok'])
w('')
w('### ### ### **NEW -- `A CORRECTION CAN ENLARGE ONE COLUMN AND MOVE NOTHING THAT MATTERS`.** ### The')
w('### undercount was real and the repair was real, and ### **THE QUADRANT THE RULING TURNS ON DID')
w('### ### NOT MOVE AT ALL.** ### A defect worth fixing is not the same as a defect that was holding')
w('### the answer back.')
w('### ### ### **NEW -- `A CATEGORY REPORTED AS AN ABSENCE IS A FALSE DEFECT`.** ### The vocabulary')
w('### a checker has determines how many defects it can see, and ### **A CHECKER WITH TOO FEW WORDS')
w('### ### REPORTS THE WORLD AS BROKEN.**')
w('### ### ### **NEW -- `A CHAIN THAT MOVED AND A PRECEDENCE SOURCE THAT DID NOT`.** ### Drift is')
w('### usually described as two documents disagreeing. ### **HERE IT IS THREE DESCRIPTIONS AT THREE')
w('### ### VERSIONS, AND THE ONE THE CORPUS CALLS AUTHORITATIVE IS THE OLDEST.**')
w('### **MET AGAIN -- THE DIRECTION REGISTERED BEFORE THE RUN.** ### The monotonicity bar could only')
w('### be a bar because it was written down before the answer was known.')
w('### **MET AGAIN -- A SLICE IS AN ADDRESS AND BOTH ITS ENDS ARE VERIFIED** (`b377`), and')
w('### ### **AN ABSENCE NEEDS A PROVED SEARCH** (`b378`), now standing clauses rather than lessons.')
w('')
w('### registration locked at (UTC) %s' % LAT)
w('### ### **%s bytes, sha256 `%s`, %d clauses, ### LOCKED BEFORE ANY WRITE AND CHAINED ON A GATE'
  % (NBY, SHA, NCL))
w('### ### THAT CHECKS WHAT EACH GATE READ.** ### %d gates read, %d checked by digest.'
  % (LG['gates_read'], LG['face_subject_gates']))
for n in ('b379_reads', 'b379_lockgate', 'b379_rescore', 'b379_survivors', 'b379_hand',
          'b379_filings', 'b379_desk'):
    j = J(n)
    w('### %-18s run file `%s` recorded clock %s'
      % (n, j['run_file'], j.get('run_clock') or run_clock.read_stamp(
          os.path.join(D, j['run_file']))))
w('### **THE REFS THIS ACT READ IN THE ROSTERED REPOSITORIES:**')
for k, v in E['refs'].items():
    w('###   %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
w('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor, `%d` anchors differing from the hint'
  % (E['reads'], E['without_anchor'], E['anchors_differing']))
w('### that found them. ### **EVERY ANCHOR WAS READ FROM ITS FILE AND NONE WAS TYPED.**')
w(BAR)

io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
print('  written: %s  (%d lines, %d bytes)'
      % (os.path.basename(OUT), len(L), len(chr(10).join(L).encode('utf-8'))))
bad = [i + 1 for i, s in enumerate(L) if '%s' in s or '%d' in s]
print('  ### UNFILLED PLACEHOLDERS : %s' % (bad or 'none'))
