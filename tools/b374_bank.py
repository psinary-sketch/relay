# -*- coding: utf-8 -*-
"""b374_bank.py -- THE BANK, WRITTEN FROM THE ACT'S OWN JSONS. ### **NO FIGURE IS TYPED.**
### ### **AND THE FILING IS CARRIED HERE VERBATIM FROM ITS OWN RUN FILE**, not re-composed."""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b374_the_descriptive_layer.txt')
REG = os.path.join(D, 'b374_registration_2026-09-08.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, H, N, G, Q = J('b374_reads'), J('b374_hedge'), J('b374_entries'), J('b374_figures'), J('b374_desk')
FQ = J('b374_funceq')
regtxt = io.open(REG, encoding='utf-8').read()
SHA = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt).group(1)
NBY = re.search(r'bytes locked : (\d+)', regtxt).group(1)
LAT = re.search(r'locked at \(UTC\) : (\S+)', regtxt).group(1)
NCL = len(J('b374_satisfiable')['clauses'])

L = []


def w(s=''):
    L.append(s)


BAR, SUB = '=' * 100, '-' * 100
KT, DT, WT = H['totals']['KEYSTONE'], H['totals']['DEPOSITED'], H['totals']['WORKING']
L2 = G['l2']
KS_K = 1000.0 * L2['keystone'] / L2['sentences']['KEYSTONE']
OT_K = 1000.0 * L2['other'] / L2['sentences']['WORKING']
DP_K = 1000.0 * L2['deposited'] / L2['sentences']['DEPOSITED']

w(BAR)
w('b374 -- THE DESCRIPTIVE LAYER, MEASURED NOT OPINED. ### THE BANK. ### SORTIE LEG 2 OF 2.')
w('2026-09-08. ### CONCURRENCY: SOLO (research seat). ### FERRY_STANDING v2, citation CURRENT.')
w('### Registration `data/b374_registration_2026-09-08.txt`, ### **LOCKED**')
w('### `%s`, %s bytes, %d clauses JOINTLY' % (SHA, NBY, NCL))
w("### SATISFIABLE, and ### **LOCKED ONLY AFTER THE AUDIT'S OWN EXIT CODE CAME BACK `0`**, locked at "
  '(UTC)')
w('### %s. ### **LOCKED BEFORE ANY WRITE OF THIS ACT.** ### The clocks are in section (9).' % LAT)
w(BAR)
w('')

w(SUB)
w('### (1) THE ANSWER, FIRST.')
w(SUB)
w('### ### ### **THE KEYSTONES HEDGE LESS THAN HALF AS OFTEN AS THE WORKING NOTES, AND CARRY UNDATED')
w('### ### ### FIGURES AT VERY NEARLY THE SAME RATE.**')
w('### Hedges per thousand sentences: ### **KEYSTONE `%.1f`, DEPOSITED `%.1f`, WORKING NOTE `%.1f`.**'
  % (KT['per_k'], DT['per_k'], WT['per_k']))
w('### Undated figures per thousand sentences: ### **KEYSTONE `%.1f`, DEPOSITED `%.1f`, OTHER `%.1f`.**'
  % (KS_K, DP_K, OT_K))
w('### ### **SO `(L2)` HOLDS ON BOTH HALVES AND THE TWO HALVES ARE NOT EQUALLY STRONG**, and this bank')
w('### says which is which rather than reporting a conjunction.')
w('')
w('### ### **THE GLOSSARY IS ENTIRELY CURRENT: `%d` ENTRIES, `%d` `CURRENT`, AND THE LIVING APPENDIX'
  % (N['glossary']['entries'], N['glossary']['tally'].get('CURRENT', 0)))
w('### ### AND ITS FROZEN TWIN DIVERGE BY NOTHING AT ALL.**')
w('### ### **THE BIBLIOGRAPHY: `%d` ENTRIES, `%d` OF THEM POINTING AT AN EXTERNAL WORK, `%d` CITED'
  % (N['bibliography']['entries'], N['bibliography']['external'], N['bibliography']['not_located']))
w('### ### NOWHERE IN THE CORPUS BUT THE REGISTER ITSELF.**')
w('')
w('### ### **THE COUNT-AND-REF SWEEP: `%d` FIGURES ACROSS THE ROSTER ARE STATED WITHOUT A REF, TAG,'
  % G['undated_total'])
w('### ### VERSION OR DATE IN THEIR OWN SENTENCE.** ### **THE LIST IS THE PRODUCT AND IT IS NOT')
w('### ### RANKED.**')
w('')
w('### ### **AND THE FUNCTIONAL EQUATION IS FILED AT THE LEVEL OF THE FAMILY, WITH BOTH HALVES QUOTED,')
w('### ### THE GRADE CARRIED AND ITS IMPORT NAMED, AND THE LIMIT IN THE FILING ITSELF.**')
w('### ### **NOTHING WAS REPAIRED IN ANY COMPONENT.** ### No sentence rewritten, no entry rewritten,')
w('### no figure dated, no document graded.')
w('')

w(SUB)
w('### (2) COMPONENT 1 -- THE HEDGE AUDIT, RUN UNMODIFIED.')
w(SUB)
w('### **THE INSTRUMENT WAS IMPORTED AND ITS OWN FIXTURES RUN BEFORE IT WAS TRUSTED : `%s`.**'
  % H['instrument_selftest'])
w('### ### **NOT ONE STEM, GRADE TOKEN OR TEST WAS TOUCHED, TUNED OR EXTENDED FOR THIS SURFACE.**')
w('### **THE SCOPE IS THE CENSUS`S OWN:** ### it names `%d` keystones in its table; ### **`%d` RESOLVED'
  % (len(H['census_names']), len(H['keystones'])))
w('### ### TO A TRACKED PATH, `%d` UNRESOLVED, `%d` AMBIGUOUS**, and `%d` deposited companions.'
  % (len(H['unresolved']), len(H['ambiguous']), len(H['deposited'])))
w('### The comparison population is the census`s own operationalised test, `%d` documents.'
  % H['support'])
w('### ### **A SEAT THAT PICKED ITS OWN KEYSTONES WOULD BE MEASURING ITS OWN CHOICE.**')
w('')
w('### %-24s %8s %10s %8s %8s %8s %10s'
  % ('population', 'docs', 'sentences', 'hedged', 'bare', 'unsrc', 'hedge/k'))
for lbl, tt in (('KEYSTONE', KT), ('DEPOSITED COMPANION', DT), ('WORKING NOTE', WT)):
    w('### %-24s %8d %10d %8d %8d %8d %10.1f'
      % (lbl, tt['docs'], tt['sentences'], tt['hedged'], tt['hedged_bare'], tt['unsourced'],
         tt['per_k']))
w('')
w('### ### **AND THE INSTRUMENT`S OWN DISTINCTION IS KEPT:** ### a hedge beside a GRADE token is the')
w('### record working as designed; a hedge without one is the thing to look at. ### The two are')
w('### counted apart above and neither is called a fault.')
w('### ### **THE THIRD CLASS IS THIS ACT`S OWN AND IS NAMED `UNSOURCED EXPECTATION`, NOT `IMPORTED`**,')
w('### because ### **THE PREDICATE CANNOT SEE WHETHER AN EXPECTATION IS FOREIGN** -- only that the')
w('### document offers no source for it. ### **THE SECOND WORD WOULD CLAIM WHAT THE TOOL CANNOT SEE.**')
w('### **WORKING NOTES PER DOCUMENT: KEYSTONE `%.2f`, DEPOSITED `%.2f`, WORKING NOTE `%.2f`.**'
  % (KT['notes_per_doc'], DT['notes_per_doc'], WT['notes_per_doc']))
w('### ### **AND A HEDGE IS NOT A FAULT.** ### A document that says *this is conditional* is doing')
w('### exactly what this record demands everywhere else. ### **THE COUNT IS NOT A SCORE.**')
w('### **QUOTATIONS BANKED, EACH LOCATED IN ITS FILE : `%d`.**' % H['quoted'])
w('')

w(SUB)
w('### (3) COMPONENT 2 -- THE GLOSSARY AND THE BIBLIOGRAPHY.')
w(SUB)
w('### ### **THE GLOSSARY HAS NO FILE OF ITS OWN.** ### It is an appendix inside a Day-1 paper, and')
w('### that paper has a ### **FROZEN TWIN** ### among the deposited companions. ### Both facts are')
w('### reported because the order named `the translation glossary` as though it were a file.')
w('### ### **AND THE TWO COPIES DIVERGE BY NOTHING: `%d` ONLY-LIVING, `%d` ONLY-FROZEN.**'
  % (len(N['glossary']['only_living']), len(N['glossary']['only_frozen'])))
w('### ### **THE GLOSSARY, `%d` ENTRIES : %s**'
  % (N['glossary']['entries'], N['glossary']['tally']))
w('### ### **NOT ONE TERM HAS GONE OUT OF USE UNDER ITS OWN NAME.**')
w('')
w('### **THE BIBLIOGRAPHY, `%d` ENTRIES:** ### `%d` point at an EXTERNAL work, and ### **AN EXTERNAL'
  % (N['bibliography']['entries'], N['bibliography']['external']))
w('### ### WORK WAS NEVER EXPECTED TO LIVE IN THIS RECORD AT ALL.** ### So the in-record test is')
w('### stated for what it is: ### **IS THE ENTRY STILL CITED UNDER THAT KEY.**')
w('### ### **THE TALLY : %s**' % N['bibliography']['tally'])
w('### ### **CITED NOWHERE BUT THE REGISTER ITSELF : `%d`**, and each is an author-year key rather'
  % N['bibliography']['not_located'])
w('### than an external ID:')
for b in N['bibliography']['detail']:
    if b['verdict'] == 'NOT LOCATED':
        w('###   `%-22s` BIBLIOGRAPHY.md:%d' % (b['key'], b['line']))
w('### ### **THAT IS A FINDING ABOUT THE REGISTER, NOT ABOUT THE WORK.** ### A reference nothing')
w('### cites is a reference the corpus carries and does not use.')
w('### **NO ENTRY WAS MERGED, RE-KEYED, RESOLVED OR REWRITTEN, AND NO `TITLE-UNVERIFIED` ENTRY WAS')
w('### GIVEN A TITLE BY THIS SEAT.** ### **NO FIFTH WORD WAS USED.**')
w('')

w(SUB)
w('### (4) COMPONENT 3 -- THE COUNT-AND-REF SWEEP.')
w(SUB)
w('### **THE WINDOW IS THE SENTENCE AND THAT IS A DECLARED CHOICE.** ### A document that dates itself')
w('### once in a header does not thereby date every figure in it -- ### **A READER LANDING ON A ROW')
w('### ### READS THE ROW** -- and the document-wide reading is named so the author can disagree.')
w('')
w('### %-24s %8s %10s %12s %8s' % ('repository', 'docs', 'figures', 'without a ref', 'pct'))
for k, v in G['totals'].items():
    w('### %-24s %8d %10d %12d %7.0f%%' % (k, v['docs'], v['figures'], v['undated'], v['pct']))
w('')
w('### **THE PAPERS REPOSITORY, BY CLASS:**')
for k, v in sorted(G['by_class'].items(), key=lambda x: -x[1]):
    w('###   %-24s %6d' % (k, v))
w('### ### **THE FROZEN CLASSES WERE READ, COUNTED, AND ARE NOT REPAIRED IN ANY LEG.**')
w('### ### **AND THE PREDICATE`S REACH IS PRINTED WITH ITS RESULT:** ### a figure is a numeral')
w('### governing a countable noun from a finite given list, and ### **A NOUN OFF THAT LIST IS')
w('### ### INVISIBLE.** ### That is the reach, not a defect hidden.')
w('### **THE LIST IS BANKED AS JSON, `%d` LINES, AND IT IS NOT RANKED, NOT PRIORITISED AND NOT A'
  % G['undated_total'])
w('### PLAN.** ### **A LIST THAT ARRIVES AS A PLAN HAS DECIDED SOMETHING**, and this leg decides')
w('### nothing.')
w('')

w(SUB)
w('### (5) COMPONENT 4 -- THE FILING.')
w(SUB)
w('### **CARRIED HERE VERBATIM FROM ITS OWN RUN FILE `data/%s`, NOT RE-COMPOSED.**' % FQ['run_file'])
w('### **QUOTATIONS PULLED BY ANCHOR : `%d` of `%d`. ### NOT PULLED : `%d`.**'
  % (FQ['pulled'], FQ['pulled'] + FQ['not_pulled'], FQ['not_pulled']))
w('')
fq = io.open(os.path.join(D, FQ['run_file']), encoding='utf-8', errors='replace').read()
mark = '  ### (2) THE FILING.'
if mark in fq:
    body = fq.split(mark, 1)[1]
    body = body.split('=' * 100)[0]
    for ln in body.split(chr(10)):
        if ln.strip():
            w('### ' + ln.rstrip()[2:] if ln.startswith('  ') else '### ' + ln.rstrip())
w('')

w(SUB)
w('### (6) THE DESK, UNDER `(R7)`.')
w(SUB)
w('### ### **`%d` SWEPT. ### `%d` CLOSED. ### `%d` STANDING.**'
  % (Q['items'], Q['closed'], Q['standing']))
w('### ### ### **AND CLOSING NOTHING IS THE RIGHT ANSWER FOR THIS LEG, AND IS SAID RATHER THAN')
w('### ### ### APOLOGISED FOR.** ### `(R7)` closes an item whose OCCASION IS GONE. ### This leg')
w('### measured and repaired nothing, so ### **IT KILLED NO OCCASION AND MAY CLOSE NOTHING.** ### It')
w('### adds three items instead, each a list this leg produced and left.')
w('### ### **A DESK THAT ONLY ACCUMULATES IS A LIST** -- `(R7)`s own warning -- ### **AND A LEG WHOSE')
w('### ### ORDER SAYS `REPAIR NOTHING` FOUR TIMES IS A LEG THAT ACCUMULATES BY INSTRUCTION.** ### The')
w('### tension is real and is filed rather than argued away.')
w('')

w(SUB)
w('### (7) THE EXPECTATIONS, SCORED.')
w(SUB)
w('### ### ### **`(L2)` -- THE NAVIGATOR`S: *the keystones carry fewer hedges than the working notes')
w('### ### ### but more undated figures.* ### CONFIRMED ON BOTH HALVES, AND THE HALVES ARE NOT')
w('### ### ### EQUALLY STRONG.**')
w('### ### **THE HEDGE HALF IS STRONG:** ### `%.1f` against `%.1f` per thousand sentences, a factor of'
  % (KT['per_k'], WT['per_k']))
w('### `%.1f`. ### The keystones hedge less than half as often.' % (WT['per_k'] / KT['per_k']))
w('### ### **THE FIGURE HALF IS NARROW AND IS SAID TO BE:** ### `%.1f` against `%.1f`, a factor of'
  % (KS_K, OT_K))
w('### `%.2f`. ### **THE DIRECTION IS THE ONE PREDICTED AND THE MARGIN IS SMALL**, and a reader should'
  % (KS_K / OT_K))
w('### not carry it as though it matched the first half.')
w('### ### **AND BOTH ARE REPORTED PER THOUSAND SENTENCES BECAUSE THE POPULATIONS DIFFER BY MORE THAN')
w('### ### AN ORDER OF MAGNITUDE IN SIZE** -- a raw total would have scored the expectation on a fact')
w('### about file sizes.')
w('')
w('### ### ### **`(E1)` -- THIS SEAT`S: *the unsourced-expectation predicate will fire most on the most')
w('### ### ### careful documents.* ### REFUTED ON THE RATE.** ### The keystones carry `%d` unsourced'
  % KT['unsourced'])
w('### expectations across `%d` sentences and the working notes `%d` across `%d`; per thousand that is'
  % (KT['sentences'], WT['unsourced'], WT['sentences']))
w('### `%.2f` against `%.2f`. ### **THE PREDICTION WAS THAT CANDOUR WOULD LOOK LIKE DEFECT, AND ON'
  % (1000.0 * KT['unsourced'] / KT['sentences'], 1000.0 * WT['unsourced'] / WT['sentences']))
w('### ### THIS MEASUREMENT IT DOES NOT.**')
w('### ### ### **`(E2)` -- THIS SEAT`S: *the bibliography will classify almost entirely CURRENT or')
w('### ### ### EXTERNAL, and the glossary is where a RETIRED referent would sit.* ### THE FIRST HALF')
w('### ### ### HELD; THE SECOND IS REFUTED.** ### The bibliography is `%d` `CURRENT` of `%d`; ### **THE'
  % (N['bibliography']['tally'].get('CURRENT', 0), N['bibliography']['entries']))
w('### ### GLOSSARY IS ENTIRELY `CURRENT` AND HOLDS NO `RETIRED` REFERENT AT ALL.** ### The rot this')
w('### seat expected in the older surface is not there, and ### **THE ENTRIES NOTHING CITES ARE IN THE')
w('### ### NEWER SURFACE, NOT THE OLDER ONE.**')
w('')

w(SUB)
w('### (8) WHAT THIS ACT DID NOT DO.')
w(SUB)
w('### **NOTHING WAS REPAIRED IN ANY COMPONENT.** ### No sentence rewritten, no entry rewritten, no')
w('### figure dated, no hedge removed, no working note cleared.')
w('### **NO DOCUMENT WAS GRADED AND NO PROSE WAS JUDGED.**')
w('### **THE HEDGE AUDIT WAS NOT MODIFIED, TUNED OR EXTENDED.**')
w('### **NO ENTRY WAS MERGED OR RE-KEYED. ### NO FROZEN SURFACE WAS EDITED.**')
w('### **NO PIN WAS ADDED AND NO GRADE WAS MOVED.** ### `b373`s findings are carried, not acted on.')
w('### **THE FILING CLAIMS NOTHING BEYOND ITS TWO ACTS**, joins nothing they did not join, and carries')
w('### the sentence that says how far they do not go.')
w('### **NO `.lean` FILE WAS TOUCHED. ### NO BUILD WAS RUN. ### NO AXIOM PROFILE WAS RECOMPUTED.**')
w('### **NO OWNER INSTRUMENT WAS EDITED.** ### This act licensed none.')
w('### **NOTHING WAS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT.**')
w('### **NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NOTHING COMPILED AND NO BRIDGE TYPED.**')
w('### **NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED.**')
w('### **NOTHING HERE BEARS ON `h2`, ON TOTALITY OR ON THE ROSTER.** ### `M-2` remains')
w('### (SPECIFIED-NOT-STATED) under `b310`s cap. ### The seam`s debt item 1 stands. ### The patent lane')
w('### is carried on the patent seat`s report, UNCONFIRMED on this seat`s record. ### **THE POSTURE')
w('### ### LOCK IS SEPARATE. ### THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED.**')
w('### `h2` stands exactly where the deposit left it. ### **NOTHING DEPOSITS.**')
w('')

w(SUB)
w('### (9) THE SPECIES, AND THE CLOCKS.')
w(SUB)
w('### ### **NEW -- `A COUNT OVER PROSE IS A COUNT OF SHAPES, AND THE SHAPES ARE NOT FAULTS`.** ### The')
w('### instrument says so in its own reach paragraph, and this act repeats it because ### **A LEG THAT')
w('### ### PRODUCES FOUR TABLES OF COUNTS OVER SOMEBODY`S WRITING WILL BE READ AS A SCORECARD UNLESS')
w('### ### IT REFUSES TO BE ONE IN ITS OWN TEXT.**')
w('### ### **NEW -- `A LEG ORDERED TO REPAIR NOTHING CANNOT CLOSE A DESK ITEM`.** ### `(R7)` closes an')
w('### item whose occasion is gone, and measuring removes no occasion. ### **THE DESK GREW BY THREE')
w('### ### AND CLOSED NOTHING, BY INSTRUCTION AND NOT BY NEGLECT.**')
w('### **MET AGAIN -- `PREDICATE_ONE_SHAPE`.** ### The bibliography parser read ANY wholly-backticked')
w('### table cell as a key, and a row whose third cell is a DOCUMENT PATH came back as an entry nothing')
w('### cites. ### **A PREDICATE THAT READS THE WRONG COLUMN INVENTS ENTRIES**, and it invented one')
w('### before the guard was written.')
w('')
w('### registration locked at (UTC) %s' % LAT)
for n in ('b374_reads', 'b374_hedge', 'b374_entries', 'b374_figures', 'b374_funceq', 'b374_desk'):
    j = J(n)
    w('### %-16s run file `%s` recorded clock %s' % (n, j['run_file'], j['run_clock']))
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
