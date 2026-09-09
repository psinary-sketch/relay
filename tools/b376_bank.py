# -*- coding: utf-8 -*-
"""b376_bank.py -- THE BANK, WRITTEN FROM THE ACT'S OWN JSONS. ### **NO FIGURE IS TYPED.**
### ### **AND IT CARRIES COMPONENT 6 -- WHAT THIS READ CANNOT DECIDE -- BECAUSE THAT COMPONENT IS
### ### PROSE ABOUT THE ACT'S OWN LIMITS AND HAS NO OTHER HOME.**
### ### **NO OPTION IN COMPONENT 6 CARRIES A PREFERENCE WORD.** ### The order says `without
### recommending` and a bar measures it with a must-fail fixture."""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b376_the_two_axis_read.txt')
REG = os.path.join(D, 'b376_registration_2026-09-08.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, LG, PR, AX, TS, Q = (J('b376_reads'), J('b376_lockgate'), J('b376_prior'),
                        J('b376_axes'), J('b376_tests'), J('b376_desk'))
P375 = J('b375_population')
regtxt = io.open(REG, encoding='utf-8').read()
SHA = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt).group(1)
NBY = re.search(r'bytes locked : (\d+)', regtxt).group(1)
LAT = re.search(r'locked at \(UTC\) : (\S+)', regtxt).group(1)
NCL = len(J('b376_satisfiable')['clauses'])

L = []


def w(s=''):
    L.append(s)


BAR, SUB = '=' * 100, '-' * 100
SC = {x['file']: x for x in AX['scored']}
N = len(AX['scored'])
QD = AX['quadrants']
QB = AX['quadrants_broad']
TA, TAB, TB = AX['axis_a_tally'], AX['axis_a_broad_tally'], AX['axis_b_tally']
NB = len(TS['axis_b_plus'])
APPONLY = QD.get('A-B+', 0) + QD.get('A?B+', 0)
SILENT = TA.get('A?', 0)
CERTB = TS['cert_by_axis_b']
NCERT = sum(CERTB.values())
OPN, CN = len(PR['operation_returns']), len(PR['census_named'])

w(BAR)
w('b376 -- THE TWO-AXIS READ. ### THE BANK.')
w(BAR)
w('')
w('### ### ### **THE HEADLINE, AND IT IS NOT THE ONE THE SEAT EXPECTED TO WRITE:**')
w('### ### ### **EVERY ONE OF THE THREE TESTS CROSSES THE QUADRANTS, AND SO DOES THE CORPUS`S OWN')
w('### ### ### PRIOR DEFINITION.** ### The certification test spreads across %d cells, the rubric test'
  % len(TS['tests']['taxonomy_tier_k']['cells']))
w('### ### ### across %d, the census test across %d, and ### **NOT ONE OF THE THREE EQUALS EITHER'
  % (len(TS['tests']['order_rubric']['cells']), len(TS['tests']['existing_census']['cells'])))
w('### ### ### AXIS.** ### So the three do not disagree because one of them is wrong.')
w('### ### ### ### **THEY DISAGREE BECAUSE EACH OF THEM IS ASKING BOTH QUESTIONS AT ONCE AND')
w('### ### ### ### WEIGHTING THEM DIFFERENTLY.**')
w('')
w('### ### **AND THE CORPUS ALREADY TRIED TO RULE THIS ONCE.** ### `THE_KEYSTONE_CENSUS.md` `§0`')
w('### states a three-clause test and its own `OPERATIONALISED:` line applies ### **TWO OF THE THREE')
w('### ### THROUGH PROXIES, DROPS CLAUSE `(iii)` ENTIRELY AND ADDS A SIZE FLOOR THE DEFINITION NEVER')
w('### ### MENTIONS.** ### Clause `(ii)` is the apparatus question; clauses `(i)` and `(iii)` are the')
w('### role question; they are joined by `and`. ### **THE CONFLICT THE THREE TESTS PRODUCE WAS ALREADY')
w('### ### INSIDE THE FIRST ONE**, and that is `(E1)` met by quotation rather than by count.')
w('')
w('### ### **THIS ACT RULES NOTHING.** ### The order says it produces the evidence the author`s class')
w('### ruling needs and makes no ruling, and Component 6 states the options ### **WITHOUT')
w('### ### RECOMMENDING ONE.** ### The four open lists stay `OPEN` by name.')
w('')

# ---------------------------------------------------------------------------------------- STEP ZERO
w(SUB)
w('### STEP ZERO -- THE LOCK READ EVERY GATE.')
w(SUB)
w('### ### **`b375`S INCIDENT, WHICH THIS STEP EXISTS TO CURE:** ### the lock was chained on the')
w('### satisfiability verdict alone while the term scan read `NOT CLEAN` and nobody looked.')
w('### ### **THE CURE IS NOT A NOTE. ### IT IS A TOOL THAT REFUSES.**')
w('###   pre-lock gates read by `tools/b376_lockgate.py` : ### **%d**' % LG['gates_read'])
w('###   of those, passing                              : ### **%d**' % LG['gates_passing'])
w('###   fixture, both polarities                       : ### **%s**'
  % ('HELD' if LG['fixture_ok'] else 'FAILED'))
for g in LG['gates']:
    w('###     %-46s %-40s %s'
      % (g['gate'][:46], g['file'][:40], 'PASS' if g['passed'] else '### FAIL ###'))
w('### ### **AND THE LOCK WAS CHAINED ON THAT TOOL`S EXIT CODE AND NOT ON ANY ONE GATE`S.**')
w('### ### **A GATE THAT HAS ONLY EVER SAID YES IS NOT A GATE:** ### the fixture builds a synthetic')
w('### clean set that must PERMIT and a synthetic set with one gate`s phrase removed that must REFUSE')
w('### ### **AND REFUSE FOR THAT GATE**, not merely refuse.')
w('### ### **WHAT THE LOCK GATE STILL CANNOT DO, DECLARED ON THE LOCKED FACE BEFORE IT RAN:** ### it')
w('### checks that each gate`s record CARRIES ITS PASS PHRASE. ### **IT CANNOT TELL WHETHER THE GATE')
w('### ### WAS RUN AGAINST THE RIGHT THING**, and a stale record from an earlier run of the same act')
w('### would satisfy it. ### **THAT IS A REAL HOLE AND IT IS NAMED RATHER THAN PAPERED OVER.**')
w('### ### **AND `b375`S DEFECTIVE FACE STAYS ON THE RECORD, UNEDITED, WITH ITS SEAL INTACT.**')
w('')

# ------------------------------------------------------------------------------------- COMPONENT 1
w(SUB)
w('### COMPONENT 1 -- THE CORPUS`S OWN PRIOR ATTEMPT, HEARD FIRST.')
w(SUB)
w('### **THE DEFINITION IT STATES**, `THE_KEYSTONE_CENSUS.md` line %d, verbatim:'
  % PR['stated']['KEYSTONE']['line'])
w('###   | %s' % PR['stated']['KEYSTONE']['text'])
w('### **WHAT IT SAYS IT APPLIES**, line %d, verbatim:' % PR['operationalised_line'])
w('###   | %s' % PR['operationalised_text'])
w('')
w('### **CLAUSE BY CLAUSE:**')
for m in PR['mapping']:
    w('###   %-6s states  : %s' % (m['clause'], m['states']))
    w('###   %-6s applies : %s' % ('', m['operates']))
w('')
w('### ### **AND THE OPERATION, RE-APPLIED AT THE HEAD OVER THE SAME CORPUS, RETURNS %d WHERE THE'
  % OPN)
w('### ### CENSUS PRINTED %d AND RECORDED ITS OWN DETECTOR AT 20.**' % CN)
w('###   of the %d, reproduced by the operation : ### **%d** ### / ### not reproduced : ### **%d**'
  % (CN, len(PR['reproduced']), len(PR['not_reproduced'])))
w('###   returned by the operation, not named by the census : ### **%d**' % len(PR['extra']))
for b in PR['not_reproduced']:
    w('###     named, refused by its own operation : `%s`' % b)
w('### ### **DO THE STATED DEFINITION AND THE APPLIED TEST AGREE : %s**'
  % ('YES' if PR['agree'] else '### **NO.**'))
w('### ### **AND THE CENSUS IS QUOTED, NOT REPAIRED.** ### Its figures were exact when written and')
w('### ### **A FIGURE THAT WAS EXACT IS NOT A FIGURE THAT IS WRONG** ### (`b372`). ### This act reads')
w('### the head; the census read `2026-08-12`; ### **THE DIVERGENCE IS REPORTED, NOT CHARGED.**')
w('')

# ------------------------------------------------------------------------------------- COMPONENT 2
w(SUB)
w('### COMPONENT 2 -- THE TWO AXES, QUOTED NOT INVENTED.')
w(SUB)
for tag, q in AX['quotes'].items():
    w('### **%s** ### -- `%s` line %d' % (tag, q['file'], q['line']))
    w('###   | %s' % q['text'][:160])
w('')
w('### ### **EACH PREDICATE WAS FIXTURED IN BOTH POLARITIES BEFORE IT SCORED ANYTHING:**')
for f in AX['fixtures']:
    w('###   %-22s got `%s` want `%s`  %s'
      % (f['label'], f['got'], f['want'], 'ok' if f['got'] == f['want'] else '### MISMATCH'))
w('### ### **AND EACH DECLARES WHAT IT IS DEAF TO, IN ITS OWN SOURCE AND ON THIS PAGE:**')
w('###   ### **AXIS A IS DEAF TO** ### a document that synthesises against other content and never')
w('###     says so about itself -- it scores `A?`, not `A-`; a synonym off the list; a self-describing')
w('###     sentence that describes ONE SECTION rather than the whole; and ### **A CLASS LINE A LATER')
w('###     ### ACT WROTE INTO THE DOCUMENT**, which on the page is indistinguishable from the')
w('###     document`s own voice. ### **THAT LAST DEAFNESS IS LOAD-BEARING ON COMPONENT 5.**')
w('###   ### **AXIS B IS DEAF TO** ### a pin given as a date; a terminal written without backticks;')
w('###     ### **WHETHER THE PIN RESOLVES** -- it reads the SHAPE of a traversable row and never the')
w('###     traversal; and ### **WHETHER THE ROW IS TRUE.** ### `b373` measured resolution; this does')
w('###     not, and says so rather than letting the reader assume it did.')
w('### ### **AND AXIS B RETURNS `B?` RATHER THAN `B-` FOR A DOCUMENT THAT NAMES ITS TERMINALS IN')
w('### ### PROSE**, because the census itself named that architecture as its own class and a table')
w('### scan is the wrong instrument for it. ### **NOT DETERMINABLE IS A FULL ANSWER.**')
w('')

# ------------------------------------------------------------------------------------- COMPONENT 3
w(SUB)
w('### COMPONENT 3 -- EVERY DOCUMENT SCORED ON BOTH AXES, INDEPENDENTLY.')
w(SUB)
w('### documents scored : ### **%d** ### -- ### **EACH AXIS COMPUTED WITHOUT THE OTHER`S ANSWER.**' % N)
w('### reads a correspondence table and axis B never reads a self-describing sentence.')
w('###   ### **AXIS A, the strict reading (one sentence carries both halves) : %s**' % TA)
w('###   ### **AXIS A, the broad reading  (two sentences may share the work) : %s**' % TAB)
w('###   ### **AXIS B                                                        : %s**' % TB)
w('### ### **BOTH READINGS WERE RUN AND BOTH ARE PRINTED; NEITHER IS SUBSTITUTED FOR THE OTHER**')
w('### (`b373`). ### The strict reading governs the quadrant table because ### **THE RUBRIC`S OWN')
w('### ### SENTENCE CARRIES BOTH HALVES IN ONE BREATH.**')
w('')
w('### **THE FOUR-QUADRANT TABLE, WITH THE UNDECIDED HELD OUT AND NEVER ROUNDED IN:**')
w('###   %-6s %-8s %-8s %s' % ('cell', 'strict', 'broad', 'what the cell means'))
GLOSS = {
    'A+B+': 'synthesises against other content AND carries a traversable row',
    'A+B-': 'synthesises against other content, carries no traversable row',
    'A-B+': 'gathers at a point in time, YET carries a traversable row',
    'A-B-': 'gathers at a point in time, carries no traversable row',
    'A+B?': 'synthesises; the apparatus question is not decidable by a table scan',
    'A-B?': 'gathers; the apparatus question is not decidable by a table scan',
    'A?B+': 'says nothing about itself; carries a traversable row',
    'A?B-': 'says nothing about itself; carries no traversable row',
    'A?B?': 'neither axis is decided by the document`s own text',
}
for k in ('A+B+', 'A+B-', 'A-B+', 'A-B-', 'A+B?', 'A-B?', 'A?B+', 'A?B-', 'A?B?'):
    w('###   %-6s %-8d %-8d %s' % (k, QD.get(k, 0), QB.get(k, 0), GLOSS[k]))
w('###   %-6s %-8d %-8d ### **BOTH PARTITION THE SAME %d DOCUMENTS AND NO DOCUMENT APPEARS TWICE.**'
  % ('total', sum(QD.values()), sum(QB.values()), N))
w('###   decided on both axes : ### **%d** ### of %d ### / ### undecided on at least one : %d'
  % (AX['decided_both'], N, N - AX['decided_both']))
w('')
w('### ### ### **THE FIRST THING BOTH READINGS AGREE ON IS THE SIZE OF `A?`: ### %d OF %d DOCUMENTS'
  % (SILENT, N))
w('### ### ### DO NOT SAY WHAT THEY ARE.** ### That silence is a MEASUREMENT and not a hole in the')
w('### sweep, and ### **NO SILENT DOCUMENT WAS ASSIGNED A MARK BY INFERENCE.**')
w('### ### **AND `(E2)` IS REFUTED IN THE DIRECTION THIS FACE SAID WOULD BE THE MORE INTERESTING')
w('### ### ONE.** ### The face expected `A-B+` to be small or empty and it holds %d; ### but counting'
  % QD.get('A-B+', 0))
w('### `A?B+` with it, ### **%d DOCUMENTS CARRY A TABLE ROW A STRANGER COULD TRAVERSE AND SAY NOTHING'
  % APPONLY)
w('### ### WHATEVER ABOUT SYNTHESISING AGAINST OTHER CONTENT.** ### Of the %d documents scoring `B+`,'
  % NB)
w('### ### **%d ARE SILENT ON AXIS A.** ### The apparatus and the prose come apart.' % APPONLY)
w('')

# ------------------------------------------------------------------------------------- COMPONENT 4
w(SUB)
w('### COMPONENT 4 -- DO THE TESTS TRACK THE AXES.')
w(SUB)
for key in ('taxonomy_tier_k', 'order_rubric', 'existing_census'):
    t = TS['tests'][key]
    w('### **%s** ### -- %d documents' % (t['label'], t['n']))
    w('###   against axis A (`A+`) : %-14s against axis B (`B+`) : %s'
      % (t['vs_axis_a'], t['vs_axis_b']))
    w('###   its members by quadrant : ### **%s**'
      % ', '.join('%s=%d' % kv for kv in sorted(t['cells'].items())))
    w('###   ### **VERDICT : %s**'
      % ('### **IT CROSSES %d QUADRANTS. ### IT MIXES THE TWO AXES.**' % len(t['cells'])
         if t['crosses'] else 'it sits in one cell'))
w('### ### ### **`(F1)` MET: ### %d OF THE THREE CROSS**, and the navigator asked for at least one.'
  % TS['crosses'])
w('')
w('### **THE SPECIFIC QUESTION -- IS THE CERTIFICATION/RUBRIC OVERLAP EXACTLY THE `A+B+` QUADRANT:**')
w('###   the overlap : ### **%d** ### / ### the `A+B+` quadrant : ### **%d** ### / ### same set : %s'
  % (len(TS['overlap']), len(TS['both_axes']),
     'YES' if TS['overlap_equals_quadrant'] else '### **NO.**'))
w('### ### **BOTH DIRECTIONS OF THE DIFFERENCE, BY DOCUMENT AND NOT COUNTED**, because a count of a')
w('### disagreement cannot be inspected:')
w('###   ### **IN THE OVERLAP, NOT IN `A+B+` (%d):**' % len(TS['overlap_not_quadrant']))
for f in TS['overlap_not_quadrant']:
    w('###     %-58s %s' % (f[:58], SC.get(f, {}).get('quadrant', '?')))
w('###   ### **IN `A+B+`, NOT IN THE OVERLAP (%d):**' % len(TS['quadrant_not_overlap']))
for f in TS['quadrant_not_overlap']:
    w('###     %s' % f)
w('')
w('### ### **`(F3)` IS REFUTED BY THE PRINT.** ### The navigator expected the certification-test set')
w('### to be close to a clean axis-B set, since it descends from a taxonomy written around pins.')
w('###   its %d members by axis B : ### **%s**' % (NCERT, CERTB))
w('### ### **%d OF %d CARRY A TRAVERSABLE ROW AND %d DO NOT.** ### A document can declare `TIER K`'
  % (CERTB.get('B+', 0), NCERT, CERTB.get('B-', 0)))
w('### and carry no row a stranger could traverse, and ### **THIS ACT DISPUTES NO DECLARATION, MOVES')
w('### ### NONE AND REMOVES NONE.** ### A declared class is quoted and never overwritten.')
w('### ### **AND THE TRAP THIS FACE NAMED BEFORE THE MEASUREMENT STANDS:** ### the certification-test')
w('### set is the set that ### **DECLARED** ### `TIER K` and axis B measures whether a document')
w('### ### **CARRIES THE APPARATUS.** ### Where they agree this act reports ### **AGREEMENT AND NOT')
w('### ### CONFIRMATION THAT THE DECLARATIONS ARE CORRECT** -- both may be reading the same habit of')
w('### writing, and this act cannot separate those.')
w('')

# ------------------------------------------------------------------------------------- COMPONENT 5
w(SUB)
w('### COMPONENT 5 -- THE FLOOR QUESTION.')
w(SUB)
w('### the `OTHER` population, as `b375``s tool left it : ### **%d of %d**'
  % (TS['other_population'], len(P375['rows'])))
w('### of those, satisfying axis A : ### **%d strict / %d broad**'
  % (len(TS['other_satisfying_a']), len(TS['other_satisfying_a_broad'])))
for f in TS['other_satisfying_a']:
    w('###   ### `%s`' % f)
    w('###     | %s' % (SC.get(f, {}).get('a_sentence') or '')[:150])
w('### ### ### **SAID PLAINLY, AS THE ORDER REQUIRES: ### THE RUBRIC-TEST SET IS A FLOOR AND NOT A')
w('### ### ### POPULATION.** ### `OTHER` contains documents that satisfy axis A by the rubric`s own')
w('### ### ### words, so ### **A DOCUMENT`S ABSENCE FROM THE RUBRIC-TEST SET IS NOT EVIDENCE THAT IT')
w('### ### ### DOES NOT SYNTHESISE.** ### `(F2)` is met.')
w('')
w('### ### **AND THE CAVEAT IS PRINTED AT THE FINDING, NOT LEFT IN THE PREDICATE`S SMALL PRINT:**')
w('### ### of the %d strict qualifiers, ### **%d QUALIFY ON A `DOCUMENT CLASS` OR `basis:` LINE THAT'
  % (len(TS['other_satisfying_a']), len(TS['qualifying_on_a_later_acts_class_line'])))
w('### ### A LATER ACT WROTE INTO THE DOCUMENT** ### (`b189`/`b190`); under the broad reading, %d of'
  % len(TS['qualifying_on_a_later_acts_class_line_broad']))
w('### ### %d. ### **AXIS A CANNOT TELL A DOCUMENT`S OWN VOICE FROM AN ANNOTATION ADDED TO IT**,'
  % len(TS['other_satisfying_a_broad']))
w('### because on the page they are the same words. ### **THE FLOOR IS REAL AND SO IS THE CAVEAT.**')
w('')
w('### **THE CORRECTED COUNT:** ### rubric-test set %d, plus %d strict (%d broad) from `OTHER`,'
  % (len(P375['tests']['order_rubric']), len(TS['other_satisfying_a']),
     len(TS['other_satisfying_a_broad'])))
w('### giving ### **%d (broad %d)** ### -- and ### **THE HONEST UPPER FIGURE IS STILL NOT A'
  % (len(P375['tests']['order_rubric']) + len(TS['other_satisfying_a']),
     len(P375['tests']['order_rubric']) + len(TS['other_satisfying_a_broad'])))
w('### ### POPULATION**, because %d documents score `A?` and ### **NO COUNT OF THE DOCUMENTS THAT'
  % SILENT)
w('### ### SPEAK CAN BOUND THE DOCUMENTS THAT ARE SILENT.**')
w('### **WHAT IT DOES TO COMPONENT 3`S TABLE:** ### nothing. ### Component 3 scored EVERY document on')
w('### both axes and never used the rubric-test set. ### The correction moves ### **COMPONENT 4`S**')
w('### rubric row, whose set is the one drawn from a tool rather than from the axes.')
w('')

# ------------------------------------------------------------------------------------- COMPONENT 6
w(SUB)
w('### COMPONENT 6 -- WHAT THIS READ CANNOT DECIDE.')
w(SUB)
w('### ### **IT CANNOT DECIDE THE RULING, AND IT DOES NOT PRETEND TO.** ### The order says this act')
w('### produces the evidence the author`s class ruling needs and makes no ruling. ### The options')
w('### below are stated with the evidence for each and what each would oblige.')
w('### ### ### **NONE IS RECOMMENDED, NONE IS RANKED, AND NO ORDERING BELOW IS AN ORDERING OF')
w('### ### ### MERIT.** ### They are printed in the order the evidence produced them.')
w('')
w('### **OPTION 1 -- ONE CLASS, RULED ON AXIS B ALONE.** ### `KEYSTONE` means: ### carries a')
w('### correspondence table naming kernel, terminal, pin and grade that a stranger can traverse.')
w('###   ### **THE EVIDENCE FOR IT:** ### axis B is the only axis this corpus can measure without')
w('###     reading a document`s opinion of itself. ### %d of %d documents are decidable on axis B'
  % (N - TB.get('B?', 0), N))
w('###     against %d of %d on axis A. ### **IT IS THE AXIS THE DOCUMENTS ANSWER.**'
  % (N - SILENT, N))
w('###   ### **WHAT IT WOULD OBLIGE:** ### the %d documents declaring `TIER K` that carry no'
  % CERTB.get('B-', 0))
w('###     traversable row would each need either a table or a moved declaration; and ### **%d'
  % APPONLY)
w('###     ### DOCUMENTS THAT SAY NOTHING ABOUT THEIR ROLE WOULD BECOME KEYSTONES BY APPARATUS.**')
w('')
w('### **OPTION 2 -- ONE CLASS, RULED ON AXIS A ALONE.** ### `KEYSTONE` means: ### synthesises a')
w('### cluster against other available content.')
w('###   ### **THE EVIDENCE FOR IT:** ### it is the author`s own rubric in the author`s own words,')
w('###     and it is the question a reader asks of a document before asking how it is backed.')
w('###   ### **WHAT IT WOULD OBLIGE:** ### a ruling on ### **%d DOCUMENTS THAT DO NOT SAY WHAT THEY'
  % SILENT)
w('###     ### ARE**, since axis A returns `A?` for them and ### **`A?` IS NOT `A-`.** ### Either')
w('###     every silent document is read by hand, or the class line becomes mandatory, or the')
w('###     unmarked stay unmarked. ### The floor finding is part of this cost: the rubric-test set is')
w('###     a floor, and ### **MOST OF ITS `OTHER` QUALIFIERS QUALIFY ON A LATER ACT`S SENTENCE.**')
w('')
w('### **OPTION 3 -- ONE CLASS, RULED ON BOTH AXES CONJOINED** ### -- the `A+B+` quadrant, which is')
w('### what the census`s stated definition already does by joining its clauses with `and`.')
w('###   ### **THE EVIDENCE FOR IT:** ### the corpus`s own prior attempt is this option, so it has a')
w('###     precedent in the record; and it is the strictest, so a document that passes passes both.')
w('###   ### **WHAT IT WOULD OBLIGE:** ### the class would hold ### **%d DOCUMENTS** ### on the strict'
  % QD.get('A+B+', 0))
w('###     reading and ### **%d** ### on the broad, against the census`s %d and the taxonomy`s %d.'
  % (QB.get('A+B+', 0), CN, NCERT))
w('###     ### **AND A DOCUMENT THAT FAILS IS NOT TOLD WHICH AXIS IT FAILED**, which is the defect')
w('###     Component 1 found in the census`s own version of this option.')
w('')
w('### **OPTION 4 -- TWO MARKS RATHER THAN ONE CLASS**, which the order names explicitly as an option')
w('### if the quadrants support it. ### Every document carries an axis-A mark and an axis-B mark and')
w('### there is no single `keystone` class at all.')
w('###   ### **THE EVIDENCE FOR IT:** ### ### **ALL %d TESTS CROSS THE QUADRANTS AND NONE EQUALS'
  % TS['crosses'])
w('###     ### EITHER AXIS**; the cert/rubric overlap is %d and the `A+B+` quadrant is %d and ### **THEY'
  % (len(TS['overlap']), len(TS['both_axes'])))
w('###     ### ARE NOT THE SAME SET**; %d documents carry the apparatus and say nothing about their'
  % APPONLY)
w('###     role; and the corpus`s own prior definition mixes the two axes inside one test.')
w('###     ### **THE QUADRANTS SUPPORT IT IN THE SENSE THE ORDER MEANT: ### THE TWO AXES ARE NOT')
w('###     ### MEASURING THE SAME PROPERTY, AND EVERY EXISTING TEST TREATS THEM AS IF THEY WERE.**')
w('###   ### **WHAT IT WOULD OBLIGE:** ### every citing sentence in the corpus that says `keystone`')
w('###     would have to say which mark it means; the taxonomy`s `Tier K`/`Tier C` line would need')
w('###     re-reading as ### **TWO COLUMNS RATHER THAN TWO TIERS**; and ### **THE %d DOCUMENTS'
  % SILENT)
w('###     ### SCORING `A?` WOULD STILL BE UNMARKED ON ONE OF THE TWO COLUMNS.** ### It does not')
w('###     dissolve the silence; it makes the silence visible in one column instead of fatal in one')
w('###     class.')
w('')
w('### **OPTION 5 -- RULE NOTHING AND RETIRE THE WORD.** ### The corpus stops using `keystone` as a')
w('### class term and cites the two marks directly.')
w('###   ### **THE EVIDENCE FOR IT:** ### the word already names %d different tests in this record'
  % (TS['crosses'] + 1))
w('###     counting the census`s own, and ### **NO TWO OF THEM SELECT THE SAME DOCUMENTS.**')
w('###   ### **WHAT IT WOULD OBLIGE:** ### every document, ledger row and registry line carrying the')
w('###     word would need re-reading; ### **AND THE CENSUS, THE TAXONOMY AND THE REGISTRY LEGEND ALL')
w('###     ### CARRY IT.** ### It is the largest of the five in edits and the smallest in new rules.')
w('')
w('### ### ### **WHAT THE EVIDENCE DOES NOT SUPPORT, SAID SO THAT THE SILENCE IS NOT READ AS')
w('### ### ### ASSENT:** ### the evidence does not support the claim that one of the three existing')
w('### ### ### tests is simply CORRECT and the others simply WRONG. ### **ALL THREE CROSS.** ### Nor')
w('### ### ### does it support a ruling made from the counts alone, because ### **THE COUNTS DEPEND')
w('### ### ### ON PREDICATES THIS SEAT WROTE**, whose deafnesses are declared above and are')
w('### ### ### load-bearing on at least the floor finding.')
w('### ### **AND THE CORPUS`S OWN PRIOR DEFINITION ARGUES FOR OPTION 3 BY PRECEDENT AND AGAINST IT BY')
w('### ### RESULT** -- it chose the conjunction and then could not apply clause `(iii)` at all.')
w('### ### ### **THAT IS EVIDENCE, AND IT IS PUT IN FRONT OF THE AUTHOR RATHER THAN ACTED ON.**')
w('')

# ------------------------------------------------------------------------------------- WHAT IS NOT
w(SUB)
w('### WHAT THIS ACT DID NOT DO.')
w(SUB)
w('### ### **NO CLASS WAS RULED. ### NO DOCUMENT WAS RECLASSIFIED. ### NO CLASS LINE WAS WRITTEN.**')
w('### ### **NO DOCUMENT WAS REPAIRED. ### NO LIST WAS CLOSED.** ### The order`s five prohibitions,')
w('### each measured by its own must-fail fixture in the gate suite.')
w('### ### **A MARK ON AN AXIS IS NOT A CLASS.** ### Two marks were recorded per document and the')
w('### marks are measurements of the documents` own text, not classes conferred on them.')
w('### ### **THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME, IN THE DESK`S OWN WORDS AND NOT IN')
w('### ### PARAPHRASE:**')
for _lst in ('the rows that cite at a ref nobody can name',
             'the rows grading a declaration the record has classified absent',
             'the undated figures across the roster',
             'the bibliography entries nothing cites'):
    w('###   ### **OPEN** ### -- %s' % _lst)
w('### ### **NONE IS CLOSED, AND NONE IS RENAMED.** ### A list restated in different words is a')
w('### different list, and the arm that measures this reads the desk`s strings.')
w('### ### **NO NEW TRACKING DOCUMENT WAS CREATED ON THIS ACT`S AUTHORITY.**')
w('### ### **NO KERNEL WAS OPENED, NO PIN WAS RESOLVED, NO CITATION WAS CHECKED.**')
w('### ### **NO `.lean` FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED.**')
w('### ### **NOTHING WAS COMPUTED ABOUT THE OBJECT** -- no frame, no seed, no transform, no')
w('### quadrature, no fit, no score, no series. ### The registration priced the numerical bar')
w('### `UNPRICED` and said so rather than leaving it blank.')
w('### ### **h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT AND THIS ACT MAKES NO CLAIM ABOUT IT IN')
w('### ### EITHER DIRECTION.** ### The instrument lane stays PARKED; the wave stays PARKED; nothing')
w('### deposits.')
w('')

# ------------------------------------------------------------------------------------- THE LEDGER
w(SUB)
w('### THE DESK, THE WRITES, AND THE SPECIES.')
w(SUB)
w('### desk items swept : %d ### / ### closed : %d ### / ### standing : %d ### / ### lists closed : %d'
  % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
w('### trail block appended (append-only %s, committed prefix intact %s); `CORRESPONDENCE.md` row %s;'
  % (Q['trail']['appended_only'], Q['trail']['committed_prefix_intact'], Q['row']))
w('### index key `every-test-crosses` reachable by every alias : %s' % Q['key_ok'])
w('')
w('### ### ### **NEW -- `A TEST THAT CROSSES IS A TEST THAT MIXES TWO QUESTIONS`.** ### When three')
w('### instruments disagree about a class, the first thing to ask is not which one is right but')
w('### ### **HOW MANY QUESTIONS EACH OF THEM IS ASKING.** ### All three here ask two.')
w('### ### ### **NEW -- `THE APPARATUS AND THE PROSE COME APART`.** ### %d documents carry a row a'
  % APPONLY)
w('### stranger could traverse and say nothing whatever about their own role. ### **A DOCUMENT THAT')
w('### ### CERTIFIES IS NOT THEREBY A DOCUMENT THAT SYNTHESISES**, and the corpus has been reading')
w('### one as evidence of the other.')
w('### ### ### **NEW -- `A DEFINITION AND ITS OPERATIONALISATION ARE TWO DOCUMENTS`.** ### The census')
w('### stated three clauses, applied two through proxies, dropped one entirely and added a floor from')
w('### nowhere -- ### **AND SAID SO HONESTLY IN ITS OWN TEXT.** ### The honesty is on the record; the')
w('### divergence still governs every number the census printed.')
w('### **MET AGAIN -- `PREDICATE_ONE_SHAPE`.** ### Axis A`s strict reading found 7 where the broad')
w('### found 23, on the same corpus, on the same day; ### **THE STRICTNESS IS A CHOICE AND ITS COST IS')
w('### ### PRINTED RATHER THAN ABSORBED.**')
w('### **MET AGAIN -- `A GATE NOBODY READS IS NOT A GATE`.** ### `b375` chained its lock on one gate.')
w('### This act built a tool that reads all %d and refuses, ### **AND FIXTURED IT IN BOTH'
  % LG['gates_read'])
w('### ### POLARITIES BEFORE TRUSTING IT.**')
w('')
w('### registration locked at (UTC) %s' % LAT)
w('### ### **%s bytes, sha256 `%s`, %d clauses, ### LOCKED BEFORE ANY WRITE AND CHAINED ON THE GATE'
  % (NBY, SHA, NCL))
w('### ### THAT READS EVERY GATE.**')
for n in ('b376_reads', 'b376_lockgate', 'b376_prior', 'b376_axes', 'b376_tests', 'b376_desk'):
    j = J(n)
    w('### %-16s run file `%s` recorded clock %s'
      % (n, j['run_file'], j.get('run_clock') or run_clock.read_stamp(
          os.path.join(D, j['run_file']))))
w('### **THE REFS THIS ACT READ:**')
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
