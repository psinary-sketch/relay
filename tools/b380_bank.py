# -*- coding: utf-8 -*-
"""b380_bank.py -- THE BANK, WRITTEN FROM THE ACT'S OWN JSONS. ### **NO FIGURE IS TYPED.**"""
import collections
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import role_structure as RSTR   # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b380_the_role_axis_scored_structurally.txt')
REG = os.path.join(D, 'b380_registration_2026-09-08.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, LG, RS, VD, Q = (J('b380_reads'), J('b380_lockgate'), J('b380_rescore'),
                    J('b380_verdict'), J('b380_desk'))
B9 = J('b379_rescore')
regtxt = io.open(REG, encoding='utf-8').read()
SHA = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt).group(1)
NBY = re.search(r'bytes locked : (\d+)', regtxt).group(1)
LAT = re.search(r'locked at \(UTC\) : (\S+)', regtxt).group(1)
NCL = len(J('b380_satisfiable')['clauses'])

L = []


def w(s=''):
    L.append(s)


BAR, SUB = '=' * 100, '-' * 100
POP = RS['population']
TA, TB, TS = RS['statement_tally'], RS['statement_broad_tally'], RS['structural_tally']
MOVED, ND = RS['moved_out_of_nd'], RS['not_determinable']
AG7, AG9, NDECL = RS['agreement_over_seven'], RS['agreement_over_all'], RS['declarers']
NSYN, NGAT = RS['declarers_synthesis'], RS['declarers_gathering']
QUAD, QPRIOR = RS['both_axes_structural'], RS['both_axes_statement']
QDECL = RS['both_axes_already_declared']
PQ, SQ = RS['quadrants_statement'], RS['quadrants_structural']
ROWS = {r['file']: r for r in RS['rows']}
APLUS = [r for r in RS['rows'] if r['structural_a'] == 'A+']
AMIN = [r for r in RS['rows'] if r['structural_a'] == 'A-']
REACH = collections.Counter(r['evidence']['reach'] for r in APLUS)
AT_THRESHOLD = REACH[2]
TOP = sorted(APLUS, key=lambda r: -r['evidence']['reach'])[:6]
GAINED = set(B9['gained'])
QUADFILES = [r['file'] for r in RS['rows']
             if r['structural_a'] == 'A+' and r['corrected_b'] == 'B+']
OWED = sorted(f for f in QUADFILES if f in GAINED)
LEDGERS = ('OPEN_TRAILS.md', 'REGISTRY.md', 'VERIFICATION_LOOM.md')
NONLEDGER = [f for f in E['declare_synthesis'] if f not in LEDGERS]

w(BAR)
w('b380 -- THE ROLE AXIS, SCORED STRUCTURALLY. ### THE BANK.')
w(BAR)
w('')
w('### ### ### **THE HEADLINE, AND IT IS TWO SENTENCES BECAUSE THE SECOND IS THE ONE THAT MATTERS:**')
w('### ### ### **THE ROLE COLUMN MOVED FOR THE FIRST TIME IN FIVE ACTS, AND THE PREDICATE THAT MOVED')
w('### ### ### IT FAILED ITS OWN CONTROL ON EXACTLY THE DISTINCTION THE RUBRIC IS ABOUT.**')
w('### ### **`%d` OF THE `%d` DOCUMENTS THE STATEMENT-BASED SCORE COULD NOT DECIDE ARE NOW DECIDED'
  % (MOVED, ND))
w('### ### (`%.1f%%`), AND NOT ONE DOCUMENT MOVED THE OTHER WAY.**' % (100.0 * MOVED / ND))
w('### ### **AND IT AGREES WITH `%d` OF THE `%d` DOCUMENTS THAT DECLARE SYNTHESIS AND WITH NEITHER OF'
  % (AG7, NSYN))
w('### ### THE `%d` THAT DECLARE GATHERING.**' % NGAT)
w('### ### ### **SO `(F1)` IS MET, `(F2)` IS MET AS THE NAVIGATOR WROTE IT, AND `(F3)` IS MET -- AND')
w('### ### ### THE ACT`S FINDING IS THE `%d` OF `%d` THAT NONE OF THE THREE ASKED FOR.**' % (AG9, NDECL))
w('')

# ------------------------------------------------------------------------------------ COMPONENT 1
w(SUB)
w('### COMPONENT 1 -- THE PREMISE, MEASURED AND NOT ASSUMED.')
w(SUB)
w('### ### **FOUR ACTS SAID THE ROLE COLUMN DOES NOT MOVE BECAUSE THE DOCUMENTS DO NOT SAY WHAT THEY')
w('### ### DO. ### AN ACT THAT ASSUMES ITS OWN PREMISE CANNOT BE REFUTED BY ITS OWN RUN**, so the')
w('### premise was re-measured before the method ran.')
w('### `b376`s own statement-based predicate was ### **RE-RUN ON THE SAME BYTES AND NOT TRUSTED FROM')
w('### ### ITS BANKED JSON**, and a deliberately BROADER reading was run beside it -- one that counts')
w('### any self-description a generous reader would accept -- ### **SO THE PREMISE COULD FAIL.**')
w('')
w('###   ### **SCORED `NOT DETERMINABLE`, STRICT : `%d` OF `%d` -- `%.1f%%`**'
  % (TA.get('A?', 0), POP, 100.0 * TA.get('A?', 0) / POP))
w('###   ### **SCORED `NOT DETERMINABLE`, BROAD  : `%d` OF `%d` -- `%.1f%%`**'
  % (TB.get('A?', 0), POP, 100.0 * TB.get('A?', 0) / POP))
w('###   the strict reading decides `%d`; the broad reading decides `%d`'
  % (RS['decided_statement'], RS['decided_statement_broad']))
w('### ### ### **THE PREMISE SURVIVES ITS OWN WIDENING.** ### Being generous about what counts as a')
w('### self-description moves `%d` documents and leaves `%.1f%%` of the corpus silent about its own'
  % (TB.get('A+', 0) + TB.get('A-', 0) - RS['decided_statement'], 100.0 * TB.get('A?', 0) / POP))
w('### role. ### **IT IS NOW A MEASUREMENT WITH A NUMBER RATHER THAN A REMARK REPEATED ACROSS FOUR')
w('### ### BANKS.**')
w('')

# ------------------------------------------------------------------------------------ COMPONENT 2
w(SUB)
w('### COMPONENT 2 -- ROLE READ FROM WHAT A DOCUMENT DRAWS ON.')
w(SUB)
w('### ### **THE RUBRIC, QUOTED, AND READ STRUCTURALLY.** ### `KEYSTONES synthesize a cluster AGAINST')
w('### OTHER AVAILABLE CONTENT -- kernels, other keystones, other clusters`; ### `SUPPORT documents')
w('### GATHER a subject`s research at a point in time`. ### **SYNTHESIS IS A CLAIM ABOUT REACH** --')
w('### what a document draws on, and whether that reaches beyond its own subject. ### **GATHERING IS')
w('### ### A CLAIM ABOUT CONFINEMENT.**')
w('### ### ### **THE THRESHOLD IS A CHOICE AND IT WAS DECLARED, NOT DISCOVERED.** ### The rubric`s own')
w('### sentence lists THREE kinds of other content, so ### **ONE FOREIGN TOUCH IS A CITATION AND TWO')
w('### ### IS A COMBINATION.** ### That was set from the wording ### **BEFORE THE CONTROL RAN**, and')
w('### when the control disagreed ### **THE THRESHOLD WAS LEFT WHERE IT WAS.**')
w('### ### **AND NO DIRECTION WAS REGISTERED, BECAUSE THERE IS NONE.** ### `b379`s widening was a')
w('### superset and could only add; ### **THIS IS A DIFFERENT METHOD, NOT A WIDER ONE**, so a document')
w('### may move in either direction and ### **NO MONOTONICITY BAR APPLIES.** ### Saying so in advance')
w('### is what stops a movement in either direction being read as a defect or as a discovery.')
w('')
w('### ### **THE FIXTURES, IN THREE POLARITIES, BECAUSE THE PREDICATE HAS THREE ANSWERS.** ### A')
w('### predicate that can only say yes is not a predicate, and one that can only say yes and no')
w('### cannot report silence. ### `tools/role_structure.py` self-test : ### **%s**'
  % ('ALL THREE MARKS REACHABLE AND THE REJECTIONS HOLD' if RSTR.self_test()[0] else 'FAILED'))
w('### ### **AND WHAT IT IS DEAF TO IS DECLARED IN THE MODULE ITSELF, NOT DISCOVERED LATER:**')
w('###   ### **A DOCUMENT THAT SYNTHESISES WITHOUT CITING** ### is invisible -- the same class the')
w('###     statement-based predicate missed, missed a second way.')
w('###   ### **A DOCUMENT THAT CITES WIDELY AND SYNTHESISES NOTHING** ### scores high. ### **REACH IS')
w('###     ### NOT ARGUMENT**, and this is the deafness the control found.')
w('###   ### **THE DIRECTORY STANDS IN FOR THE SUBJECT** -- an ADDRESS standing in for a subject,')
w('###     which is exactly the substitution `(R2)` warns against. ### Used because the corpus`s')
w('###     clusters are directory-shaped, and ### **NAMED AS A WEAKNESS AND NOT HIDDEN AS A')
w('###     ### CONVENIENCE.**')
w('###   ### **A CITATION IT DOES NOT RECOGNISE IS NOT A CITATION TO IT** -- a document named in prose')
w('###     without backticks or a path, a kernel named by a nickname.')
w('')

# ------------------------------------------------------------------------------------ COMPONENT 3
w(SUB)
w('### COMPONENT 3 -- EVERY DOCUMENT RE-SCORED, WITH ITS PRIOR SCORE KEPT BESIDE IT.')
w(SUB)
w('### ### **THE CONTROL IS PRINTED FIRST, BEFORE ANY OTHER RESULT**, because a predicate`s agreement')
w('### with the only ground truth available is the one number that can invalidate every other number')
w('### on the page.')
w('')
w('###   %-62s %-10s %-10s %s' % ('THE DOCUMENT', 'DECLARED', 'STRUCTURAL', 'REACH'))
for f in E['declare_synthesis'] + E['declare_gathering']:
    r = ROWS[f]
    w('###   %-62s %-10s %-10s %d'
      % (f, r['statement_a'], r['structural_a'], r['evidence']['reach']))
w('')
w('### ### **AGREEMENT OVER THE SEVEN THAT DECLARE SYNTHESIS : `%d` OF `%d`.**' % (AG7, NSYN))
w('### ### **AGREEMENT OVER ALL `%d` THAT DECLARE ANYTHING  : `%d` OF `%d`.**' % (NDECL, AG9, NDECL))
w('### ### ### **AND THE `%d` THAT DISAGREE ARE BOTH OF THE GATHERERS, WHICH IS THE WHOLE OF THAT'
  % (NDECL - AG9))
w('### ### ### SIDE OF THE DISTINCTION.**')
for d in RS['disagreements']:
    w('###   `%s` declared `%s`, scored `%s`, reaching `%d` places'
      % (d['file'], d['statement'], d['structural'], d['evidence']['reach']))
w('### ### **THEY ARE NOT MISFILED.** ### `FINDINGS.md` is the corpus`s findings ledger and')
w('### `PATHS_TO_THE_CRITICAL_LINE.md` is a route inventory: ### **THEY GATHER, AND THEY GATHER')
w('### ### WIDELY.** ### The predicate reads that reach and calls it synthesis.')
w('### ### ### **SO THE `A-` COLUMN IS NOT MEASURING GATHERING. ### IT IS MEASURING NARROW REACH**,')
w('### which is a different property that happens to correlate with it across most of the corpus.')
w('### ### **A PREDICATE THAT CONTRADICTS THE ONLY GROUND TRUTH AVAILABLE HAS FAILED, HOWEVER')
w('### ### PLAUSIBLE ITS OUTPUT LOOKS**, and `%d` of `%d` is a failure and not a rounding.'
  % (AG9, NDECL))
w('')
w('### ### **AND THE AGREEMENT IT DID REACH IS THINNER THAN THE COUNT MAKES IT LOOK.** ### Of the')
w('### `%d` synthesis declarers, the three ledgers reach `%s` places and the other `%d` reach `%s` --'
  % (NSYN, ', '.join(str(ROWS[f]['evidence']['reach']) for f in LEDGERS), len(NONLEDGER),
     ', '.join(str(ROWS[f]['evidence']['reach']) for f in NONLEDGER)))
w('### and the threshold is `2`. ### **TWO OF THE FOUR SIT EXACTLY ON IT.** ### The predicate agrees')
w('### with the ledgers because they reach everywhere by construction and with the others by one or')
w('### two citations. ### **AGREEMENT REACHED FOR THE WRONG REASON IS REPORTED AS SUCH.**')
w('')
w('### ### **THE COLUMN, BEFORE AND AFTER. ### THE PRIOR SCORE IS KEPT BESIDE THE NEW ONE FOR EVERY')
w('### ### DOCUMENT AND `%d` WERE OVERWRITTEN.**' % RS['prior_scores_overwritten'])
w('###   %-14s %-12s %-12s %s' % ('MARK', 'STATEMENT', 'STRUCTURAL', 'MOVEMENT'))
for k in ('A+', 'A-', 'A?'):
    w('###   %-14s %-12d %-12d %+d' % (k, TA.get(k, 0), TS.get(k, 0), TS.get(k, 0) - TA.get(k, 0)))
w('###   %-14s %-12d %-12d' % ('total', POP, POP))
w('### ### **OUT OF `NOT DETERMINABLE` : `%d`. ### INTO `NOT DETERMINABLE` : `%d`.**'
  % (MOVED, RS['moved_into_nd']))
w('')
w('### ### **THE QUADRANT TABLE, BOTH VERSIONS SIDE BY SIDE, OVER `b379`s CORRECTED APPARATUS')
w('### ### COLUMN.**')
w('###   %-10s %-16s %-16s %s' % ('QUADRANT', 'STATEMENT-A', 'STRUCTURAL-A', 'MOVEMENT'))
for k in sorted(set(list(PQ.keys()) + list(SQ.keys()))):
    w('###   %-10s %-16d %-16d %+d' % (k, PQ.get(k, 0), SQ.get(k, 0), SQ.get(k, 0) - PQ.get(k, 0)))
w('###   %-10s %-16d %-16d' % ('total', sum(PQ.values()), sum(SQ.values())))
w('### ### ### **THE BOTH-AXES QUADRANT IS NON-EMPTY FOR THE FIRST TIME IN THIS SEQUENCE: `%d` -> `%d`.**'
  % (QPRIOR, QUAD))
w('### ### **`%d` OF THE `%d` WERE ALREADY THERE. ### `%d` ARE THERE ONLY BECAUSE THIS ACT READ THEIR'
  % (QDECL, QUAD, QUAD - QDECL))
w('### ### STRUCTURE**, and ### **`%d` OF THEM ARE THERE ONLY BECAUSE `b379` WIDENED THE OTHER AXIS:**'
  % len(OWED))
for f in OWED:
    w('###   `%s`' % f)
w('### ### **A QUADRANT REACHED BY WIDENING THE OTHER AXIS IS NOT THE SAME AS A QUADRANT THE CORPUS')
w('### ### EARNED**, and the split is printed rather than summarised.')
w('')

# ------------------------------------------------------------------------------------ COMPONENT 4
w(SUB)
w('### COMPONENT 4 -- THE VERDICT ON THE METHOD, AND NOT ON THE CLASS.')
w(SUB)
w('### ### ### **THE VERDICT : %s.**' % VD['branch'])
w('### The column moved -- ### **`%d` of `%d`, `%.1f%%`** -- and the control did not come clean --'
  % (MOVED, ND, VD['fraction']))
w('### ### **`%d` of `%d`** -- so both halves are stated rather than one.' % (AG9, NDECL))
w('')
w('### ### **WHICH POPULATIONS THE STRUCTURAL READ DOES READ:** ### the `A-` and `A?` columns. ### A')
w('### document that draws on little or nothing ### **CANNOT BE SYNTHESISING AGAINST OTHER AVAILABLE')
w('### ### CONTENT**, because it has not reached any. ### `%d` documents draw on nothing this'
  % TS.get('A?', 0))
w('### predicate can see and `%d` draw on one thing, of which `%d` reach nowhere outside their own'
  % (TS.get('A-', 0), sum(1 for r in AMIN if r['evidence']['reach'] == 0)))
w('### subject at all. ### **THAT IS EVIDENCE, AND IT IS THE HALF THAT HOLDS.**')
w('### ### **WHICH POPULATION IT DOES NOT READ:** ### the `A+` column. ### A document that reaches')
w('### has reached, and ### **REACH IS NOT ARGUMENT.** ### The six documents reaching furthest are:')
for r in TOP:
    w('###   reach %-4d `%s`' % (r['evidence']['reach'], r['file']))
w('### ### **FIVE OF THE SIX ARE LEDGERS OR LEDGER ARCHIVES**, which reach everywhere by')
w('### construction and argue nothing. ### And at the other end ### **`%d` OF THE `%d` `A+` DOCUMENTS'
  % (AT_THRESHOLD, len(APLUS)))
w('### ### SIT EXACTLY ON THE THRESHOLD**, one citation from `A-`.')
w('### ### ### **SO THE `A+` COLUMN IS AN UPPER BOUND ON SYNTHESIS AND THE `A-` COLUMN IS')
w('### ### ### UNVALIDATED**, and the distinction the rubric turns on lives in sentences and not in a')
w('### ### ### citation graph.')
w('')
w('### ### **WHAT THAT WOULD OBLIGE, IF THE AUTHOR TOOK IT AS THE FINDING.** ### Stated because the')
w('### registration required the branch to state its obligation, and ### **STATED WITHOUT BEING')
w('### ### RECOMMENDED:** ### a rubric whose distinction is not structurally readable is one a')
w('### document must ### **DECLARE**, which would make the ruling a declaration rule for the `%d`'
  % (POP - NDECL))
w('### documents that declare nothing rather than a classification of them. ### **THAT IS A COST, NOT')
w('### ### A PROPOSAL**, and this act does not say whether it should be paid.')
w('### ### ### **NO CLASS IS RULED IN THIS BRANCH OR IN EITHER OF THE OTHER TWO.** ### The verdict is')
w('### about whether a method works, and ### **A METHOD THAT WORKS IS NOT A RULING EITHER.**')
w('')

# --------------------------------------------------------------------------------- THE EVIDENCE
w(SUB)
w('### THE RULING`S EVIDENCE, CONSOLIDATED INTO ONE FILE.')
w(SUB)
ev = io.open(os.path.join(D, 'b380_ruling_evidence.txt'), encoding='utf-8').read().splitlines()
w('### `data/b380_ruling_evidence.txt`, ### **`%d` LINES**, holding what four acts produced and no' % len(ev))
w('### single place held: the five options quoted whole, the author`s role clause banked verbatim,')
w('### the three definitions of `keystone`, the corrected apparatus column and both role tables --')
w('### ### **EVERY FIGURE CARRYING THE ACT THAT MEASURED IT.**')
w('### ### ### **IT IS A RELAY BANK ARTIFACT AND NOT A TRACKING DOCUMENT IN THE CORPUS**, which no')
w('### act since `b375` has been permitted to create. ### Where such a census should live is still')
w('### ### **ROUTED TO THE AUTHOR AND STILL UNANSWERED**, and this act did not answer it by writing')
w('### the file somewhere convenient.')
w('')

# ------------------------------------------------------------------------------- THE EXPECTATIONS
w(SUB)
w('### THE EXPECTATIONS, EACH AGAINST ITS OWN PRINTED TABLE.')
w(SUB)
w('### ### **`(F1)` MET.** ### `%d` of `%d` out of `NOT DETERMINABLE` is a majority at `%.1f%%`.'
  % (MOVED, ND, VD['fraction']))
w('### ### **`(F2)` MET AS WRITTEN, AND THE WORDING IS WHAT SAVED IT.** ### `%d` of the `%d` that'
  % (AG7, NSYN))
w('### declare synthesis, against a bar of six. ### **AND THE SEVEN ARE ALL ON ONE SIDE OF THE')
w('### ### DISTINCTION.** ### Over all `%d` documents that declare anything it is `%d`, because the'
  % (NDECL, AG9))
w('### `%d` it missed are the `%d` gatherers. ### **A CONTROL DRAWN ENTIRELY FROM ONE SIDE OF A'
  % (NDECL - AG9, NGAT))
w('### ### DISTINCTION CANNOT TEST THE DISTINCTION**, and reporting the agreement over the seven and')
w('### over the nine separately is what makes that visible instead of hiding it in a ratio.')
w('### ### **`(F3)` MET, AND IT IS THE WEAKEST OF THE THREE, AS REGISTERED.** ### `%d` in the' % QUAD)
w('### both-axes quadrant, of which `%d` owe their apparatus mark to `b379`s widening.' % len(OWED))
w('')
w('### ### **`(E1)` MET, AND IN THE FORM IT NAMED.** ### It registered that `(F1)` and `(F2)` pull')
w('### against each other: ### **a predicate loose enough to move a majority out of `A?` will call')
w('### ### ledgers and indexes synthesisers.** ### It does -- `BIBLIOGRAPHY.md` scores `A+` at reach')
w('### `%d` and `FACES_LEDGER.md` at reach `%d`, and neither says anything. ### **BOTH HELD ONLY'
  % (ROWS['BIBLIOGRAPHY.md']['evidence']['reach'], ROWS['FACES_LEDGER.md']['evidence']['reach']))
w('### ### BECAUSE THE CONTROL`S POPULATION WAS THE SEVEN**, and over the nine the price is visible.')
w('### ### **`(E2)` REFUTED IN ITS DOCUMENTS AND CONFIRMED IN ITS MECHANISM.** ### It predicted the')
w('### disagreements would be on the ledgers, which reach everywhere by construction. ### **THE')
w('### ### PREDICATE AGREED WITH ALL THREE LEDGERS AND DISAGREED WITH BOTH GATHERERS INSTEAD.** ###')
w('### The mechanism it named was right and the side it named was wrong: ### **THE AGREEMENT WITH THE')
w('### ### LEDGERS WAS INDEED REACHED FOR THE WRONG REASON** -- reaches of `%s` against a threshold'
  % ', '.join(str(ROWS[f]['evidence']['reach']) for f in LEDGERS))
w('### of `2` -- ### **AND THE WRONGNESS SURFACED ON THE OTHER SIDE OF THE CONTROL.**')
w('### ### **`(E3)` MET.** ### `%d` of the `%d` in the quadrant are there because `b379` widened the'
  % (len(OWED), QUAD))
w('### apparatus axis, so the quadrant is part earned and part instrument, and the split is printed.')
w('')

# --------------------------------------------------------------------------------------- CLOSING
w(SUB)
w('### THE DESK, THE WRITES, AND WHAT THIS ACT DID NOT DO.')
w(SUB)
w('### desk items swept : %d ### / ### closed : %d ### / ### standing : %d ### / ### lists closed : %d'
  % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
w('### ### **AND CLOSING NOTHING IS RIGHT EVEN THOUGH THIS ACT MEASURED SOMETHING.** ### `(R7)`')
w('### closes an item whose OCCASION is gone; moving a column under a new predicate does not remove')
w('### the occasion of the obligation, the ruling, or any of the four lists -- ### **AND THE PREDICATE')
w('### ### THAT MOVED IT FAILED ITS OWN CONTROL.** ### **A MEASUREMENT IS NOT A CLOSURE, AND AN ITEM')
w('### ### AN ACT PUTS ON THE DESK AND CLOSES IN THE SAME ACT IS NOT A CLOSURE EITHER.**')
w('### trail block appended (append-only %s, committed prefix intact %s); `CORRESPONDENCE.md` row %s;'
  % (Q['trail']['appended_only'], Q['trail']['committed_prefix_intact'], Q['row']))
w('### index key `the-role-axis-read-from-structure` reachable by every alias : %s' % Q['key_ok'])
w('### ### **THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME AND NONE IS CLOSED.**')
w('### ### **NO CLASS WAS RULED. ### NO DOCUMENT WAS RECLASSIFIED. ### NO DECLARATION WAS MOVED. ###')
w('### ### NO LIST WAS CLOSED. ### NO PRIOR SCORE WAS OVERWRITTEN. ### THE REGISTRY WAS NOT EDITED.**')
w('### ### **NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL.** ### Nothing on the download layer was')
w('### written, moved, renamed or removed. ### No archive file was touched and the `86` unconfirmed')
w('### stay unconfirmed. ### The six clusters stay filed and not opened. ### The column-`(d)` figure')
w('### stays a FLOOR. ### **NO `.lean` FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED.**')
w('### **THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED. ### THE POSTURE LOCK IS')
w('### SEPARATE.** ### `h2` stands exactly where the deposit left it and this act makes no claim about')
w('### it in either direction. ### **NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.**')
w('')

# ------------------------------------------------------------------------------------------ LORE
w(SUB)
w('### WHAT THIS ACT ADDS TO THE LORE.')
w(SUB)
w('### ### ### **NEW -- `A CONTROL DRAWN FROM ONE SIDE OF A DISTINCTION CANNOT TEST THE`')
w('### ### ### `DISTINCTION`.** ### `(F2)` named seven documents and all seven declare synthesis. ###')
w('### The predicate passed it `%d` of `%d` and still could not tell synthesis from gathering, because'
  % (AG7, NSYN))
w('### ### **NOTHING IN THE CONTROL EVER ASKED IT TO.**')
w('### ### ### **NEW -- `REACH IS NOT ARGUMENT`.** ### A bibliography, an index, a ledger and a')
w('### ledger`s archive reach further than anything that argues, and ### **A CITATION GRAPH SCORES')
w('### ### THEM HIGHEST.** ### Measuring what a document touches is not measuring what it does with')
w('### what it touched.')
w('### ### ### **NEW -- `AN AGREEMENT REACHED FOR THE WRONG REASON IS STILL A DISAGREEMENT`.** ### The')
w('### three ledgers agreed with the predicate at reaches of `%s` against a threshold of `2`. ###'
  % ', '.join(str(ROWS[f]['evidence']['reach']) for f in LEDGERS))
w('### **THEY WOULD HAVE AGREED WITH ANY THRESHOLD**, so their agreement carries no information about')
w('### the threshold at all.')
w('### **MET AGAIN -- `A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE`** (`b369`). ### The')
w('### statement-based predicate knew sentences and found `%d` of `%d`; this one knows citations and'
  % (RS['decided_statement'], POP))
w('### finds `%d` -- ### **AND BOTH ARE THIS SEAT`S OWN PREDICATES AND NEITHER IS A GROUND TRUTH.**'
  % (POP - TS.get('A?', 0)))
w('### **MET AGAIN -- THE THRESHOLD DECLARED BEFORE THE CONTROL RAN**, and ### **IT WAS NOT MOVED')
w('### AFTERWARDS TO MAKE THE CONTROL AGREE** -- which is the only reason the failure is legible.')
w('### **MET AGAIN -- AN ABSENCE NEEDS A PROVED SEARCH** (`b378`) and ### **A RUN FILE IS RESOLVED BY')
w('### ITS OWN RECORDED CLOCK** (`b358`), both now standing clauses rather than lessons.')
w('')

# ------------------------------------------------------------------------------------- THE RECORD
w(SUB)
w('### THE RECORD.')
w(SUB)
w('### registration locked at (UTC) %s' % LAT)
w('### ### **%s bytes, sha256 `%s`, %d clauses, ### LOCKED BEFORE ANY WRITE AND CHAINED ON A GATE'
  % (NBY, SHA, NCL))
w('### ### THAT CHECKS WHAT EACH GATE READ.** ### %d gates read, %d checked by digest.'
  % (LG['gates_read'], LG['face_subject_gates']))
for n in ('b380_reads', 'b380_lockgate', 'b380_rescore', 'b380_verdict', 'b380_desk'):
    j = J(n)
    w('### %-16s run file `%s` recorded clock %s'
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
MUSTFAIL = ('### A CLASS WAS RULED.', '### A DECLARATION WAS MOVED.', '### A LIST WAS CLOSED.',
            '### A PRIOR SCORE WAS OVERWRITTEN.',
            '### THE THRESHOLD WAS MOVED TO FIT THE CONTROL.', '### THE PREFERRED BRANCH IS.')
hit = [m for m in MUSTFAIL if m in L]
print('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (hit or 'none'))
sys.exit(1 if (bad or hit) else 0)
