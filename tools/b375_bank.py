# -*- coding: utf-8 -*-
"""b375_bank.py -- THE BANK, WRITTEN FROM THE ACT'S OWN JSONS. ### **NO FIGURE IS TYPED.**
### ### **AND IT CARRIES COMPONENT 5 -- WHAT THE CENSUS DOES NOT KNOW -- BECAUSE THAT COMPONENT IS
### ### PROSE ABOUT THE ACT'S OWN LIMITS AND HAS NO OTHER HOME.**"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b375_the_keystone_and_cluster_census.txt')
REG = os.path.join(D, 'b375_registration_2026-09-08_reissued.txt')
FIRST = os.path.join(D, 'b375_registration_2026-09-08.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, P, CL, IN, RB, Q = (J('b375_reads'), J('b375_population'), J('b375_clusters'),
                       J('b375_integration'), J('b375_rubric'), J('b375_desk'))
H374 = J('b374_hedge')
regtxt = io.open(REG, encoding='utf-8').read()
SHA = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt).group(1)
NBY = re.search(r'bytes locked : (\d+)', regtxt).group(1)
LAT = re.search(r'locked at \(UTC\) : (\S+)', regtxt).group(1)
firsttxt = io.open(FIRST, encoding='utf-8').read()
SHA1 = re.search(r'sha256 of every byte ABOVE this block : (\w+)', firsttxt).group(1)
NBY1 = re.search(r'bytes locked : (\d+)', firsttxt).group(1)
NCL = len(J('b375_satisfiable')['clauses'])

L = []


def w(s=''):
    L.append(s)


BAR, SUB = '=' * 100, '-' * 100
ROWS = {r['file']: r for r in P['rows']}
K16, K32 = set(H374['keystones']), set(P['tests']['order_rubric'])
KT, ST = RB['totals']['KEYSTONE'], RB['totals']['SUPPORT']
NOKEY = CL['subject_clusters_without_keystone']


def pct(key):
    fs = P['tests'][key]
    return (100.0 * sum(1 for f in fs if ROWS[f]['declared_line']) / len(fs)) if fs else 0.0


w(BAR)
w('b375 -- THE KEYSTONE AND CLUSTER CENSUS. ### THE BANK.')
w('2026-09-08. ### CONCURRENCY: SOLO (research seat). ### FERRY_STANDING v2, citation CURRENT.')
w('### Registration `data/b375_registration_2026-09-08_reissued.txt`, ### **LOCKED**')
w('### `%s`, %s bytes, %d clauses JOINTLY' % (SHA, NBY, NCL))
w("### SATISFIABLE, and ### **LOCKED ONLY AFTER THE AUDIT'S EXIT CODE, THE REGISTRATION GATE AND THE")
w('### ### TERM SCAN ALL CAME BACK CLEAN**, locked at (UTC) %s.' % LAT)
w('### ### **AND THE FIRST FACE IS ON THE RECORD BESIDE IT, SEAL INTACT AND NOT EDITED:**')
w('### `data/b375_registration_2026-09-08.txt`, `%s`, %s bytes. ### Section (9).' % (SHA1, NBY1))
w(BAR)
w('')

w(SUB)
w('### (1) THE ANSWER, FIRST.')
w(SUB)
w('### ### ### **THE WORD `KEYSTONE` NAMES THREE DIFFERENT TESTS IN THIS RECORD, AND THEY DO NOT')
w('### ### ### SELECT THE SAME DOCUMENTS.**')
w('###   the author-ruled taxonomy`s `Tier K` -- ### *certification at a pin* ### -- selects `%d`;'
  % len(P['tests']['taxonomy_tier_k']))
w('###   the order`s rubric -- ### *synthesis against other available content* ### -- selects `%d`;'
  % len(P['tests']['order_rubric']))
w('###   `THE_KEYSTONE_CENSUS.md`s own test selects `%d`.' % len(P['tests']['existing_census']))
w('### ### **AND `%d` DOCUMENTS ARE IN ALL THREE.**' % len(P['tests']['all_three']))
w('### ### **WHICH GOVERNS IS A RULING AND NOT A READ.** ### This act measured all three and')
w('### reconciled none, which is what the order required of it.')
w('')
w('### ### ### **AND THE CONSEQUENCE IS NOT ACADEMIC. ### THE SAME INSTRUMENT, RUN ON TWO OF THOSE')
w('### ### ### DEFINITIONS ONE ACT APART, GIVES OPPOSITE ANSWERS.**')
w('### `b374` measured the existing census`s sixteen and found the keystone layer hedging ### **LESS**')
w('### than its control: `%.1f` against `%.1f` per thousand sentences.'
  % (H374['totals']['KEYSTONE']['per_k'], H374['totals']['WORKING']['per_k']))
w('### `b375` measures the order`s rubric`s `%d` and finds the keystone layer hedging ### **MORE**'
  % len(K32))
w('### than its control: `%.1f` against `%.1f`.' % (KT['per_k'], ST['per_k']))
w('### ### **THE INSTRUMENT DID NOT CHANGE. ### THE DEFINITION OF `KEYSTONE` DID.** ### The two sets')
w('### overlap on `%d` documents. ### **A MEASUREMENT OF A LAYER IS A MEASUREMENT OF WHICHEVER'
  % len(K16 & K32))
w('### ### DEFINITION OF THAT LAYER YOU USED**, and this bank reports both rather than choosing.')
w('')
w('### ### **THE POPULATION: `%d` TRACKED DOCUMENTS, `%d` DECLARING A CLASS LINE AND `%d` NOT.**'
  % (P['documents'], P['declared'], P['not_declared']))
w('### Under the order`s four words: %s.' % P['order_tally'])
w('### ### **`%d` SUBJECT CLUSTERS HAVE REGISTRY ROWS AND NO KEYSTONE.**' % len(NOKEY))
w('### ### **COLUMN (d) -- WHAT BEARS ON A KEYSTONE AND IS NOT IN IT -- IS NON-EMPTY FOR `%d` OF `%d`.**'
  % (IN['d_nonempty'], IN['keystones']))
w('### ### **NOTHING WAS REPAIRED, NO CLASS WAS CONFERRED, AND NO LIST WAS CLOSED.**')
w('')

w(SUB)
w('### (2) COMPONENT 1 -- THE POPULATION. ### **THREE COLUMNS, NEVER MERGED.**')
w(SUB)
w('### **`%d` TRACKED MARKDOWN DOCUMENTS, CLASSIFIED FROM CONTENT AND NEVER FROM A PATH.**'
  % P['documents'])
w('### ### **DECLARING A CLASS LINE : `%d` ### / ### NOT DECLARING : `%d`.**'
  % (P['declared'], P['not_declared']))
w('### ### **AND THE AUTHOR-RULED TAXONOMY SAYS `EVERY CORPUS DOCUMENT BELONGS TO ONE OF FOUR')
w('### ### TIERS`.** ### Most carry no tier line. ### **THAT IS REPORTED AND NOT CONFERRED** -- the')
w('### order forbids conferring a class, and this act confers none.')
w('### **THE DECLARED TIERS, AS THE DOCUMENTS THEMSELVES WRITE THEM : %s**' % P['declared_tiers'])
w('### ### **AND `NOT PLACED` IS A DECLARATION**, not a blank: the ledgers refused a tier at content')
w('### and routed their home to the author. ### **THE CENSUS RECORDS THE REFUSAL AND PLACES NOTHING.**')
w('')
w('### **THE THREE TESTS, SIDE BY SIDE:**')
w('### %-46s %8s %8s' % ('test', 'selects', 'declare'))
for lbl, key in (("the taxonomy's `Tier K` (certified at a pin)", 'taxonomy_tier_k'),
                 ("the order's rubric (synthesis)", 'order_rubric'),
                 ("the existing census's own test", 'existing_census')):
    w('### %-46s %8d %7.0f%%' % (lbl, len(P['tests'][key]), pct(key)))
w('### ### **IN ALL THREE : `%d`.**' % len(P['tests']['all_three']))
for f in P['tests']['all_three']:
    w('###   `%s`' % f)
w('')
w('### **WHERE THE DIRECTORY SUGGESTS ONE CLASS AND THE CONTENT READS AS ANOTHER : `%d`**, each'
  % len(P['disagreements']))
w('### ### **REPORTED AT FULL PROMINENCE AND NOT RECLASSIFIED.**')
for x in P['disagreements'][:8]:
    w('###   %-58s %s' % (x['file'][:58], x['order_class']))
if len(P['disagreements']) > 8:
    w('###   ... and %d more, all banked in the JSON.' % (len(P['disagreements']) - 8))
w('### ### **AND NO DOCUMENT WAS DEFAULTED TO `SUPPORT`.** ### A document whose own text does not say')
w('### what it does is `OTHER` with the reason printed -- ### **DEFAULTING TO THE LARGER CLASS WOULD')
w('### ### HAVE MANUFACTURED THE CENSUS`S OWN ANSWER.**')
w('')

w(SUB)
w('### (3) COMPONENT 2 -- THE CLUSTERS.')
w(SUB)
w('### **ENUMERATED FROM THE CLUSTER DOCUMENTS THEMSELVES AND FROM THE REGISTRY`S OWN SECTIONS AND')
w('### ROWS. ### NEVER FROM DIRECTORY NAMES.**')
w('### clusters named by a cluster-synthesis document : `%d`' % len(CL['doc_clusters']))
w('### registry sections whose rows name a document  : `%d`' % len(CL['registry_sections']))
w('### ### **AND A DATED `Row addition` OR `Version-log addition` HEADING IS THE REGISTRY MAINTAINING')
w('### ### ITSELF, NOT A SUBJECT CLUSTER.** ### Both halves are reported; a rule that quietly')
w('### discarded sections would be choosing the census`s own answer.')
w('')
w('### ### **SUBJECT CLUSTERS WITH DOCUMENTS AND NO KEYSTONE : `%d`**' % len(NOKEY))
for t2 in CL['table']:
    if t2['cluster'] in NOKEY:
        w('###   `%s`' % t2['cluster'])
        w('###       %d document(s) resolved, %d SUPPORT, %d OTHER, ### **NO KEYSTONE**'
          % (t2['resolved'], len(t2['support']), t2['other']))
w('### ### **A CLUSTER WITH NO KEYSTONE IS A FINDING AND IS REPORTED AS ONE**, not as a hole in the')
w('### sweep.')
w('### ### **AND UNASSIGNED KEYSTONES : `%d`** ### -- their own text names no cluster this act can'
  % len(CL['unassigned']))
w('### enumerate, and ### **NONE IS ASSIGNED BY RESEMBLANCE.**')
w('')

w(SUB)
w('### (4) COMPONENT 3 -- THE INTEGRATION STATE. ### **FOUR COLUMNS, NEVER AVERAGED.**')
w(SUB)
w('### **keystones read : `%d`.**' % IN['keystones'])
w('### ### **(d) WHAT BEARS ON IT AND IS NOT IN IT : NON-EMPTY FOR `%d` OF `%d`**, listed by anchor'
  % (IN['d_nonempty'], IN['keystones']))
w('### and ### **NEVER SUMMARIZED** -- the order`s own words. ### A ledger line bears on a keystone')
w('### when it names one of the keystone`s objects and ### **THE KEYSTONE DOES NOT NAME THE ACT THAT')
w('### ### WROTE IT.**')
w('### **COLUMNS READING `NOT DETERMINABLE FROM THE DOCUMENT`:** ### (a) `%d`, (b) `%d`, (c) `%d`'
  % (IN['not_determinable']['a'], IN['not_determinable']['b'], IN['not_determinable']['c']))
w('### of `%d`. ### **THAT IS A FULL ANSWER AND NOT A FAILURE OF THE SWEEP** (`b367`), and'
  % IN['keystones'])
w('### ### **NOTHING WAS INFERRED TO FILL A CELL.**')
w('### ### **AND NO KERNEL WAS OPENED.** ### Column (b) records what a document NAMES, and it counts')
w('### named terminals apart from counts, which is `b372`s finding made into a column:')
w('### ### **A COUNT IS A CLAIM ABOUT AN UNNAMED MOMENT AND A NAMED TERMINAL IS NOT.**')
w('')

w(SUB)
w('### (5) COMPONENT 4 -- THE RUBRIC APPLIED, AND THE CONTROL.')
w(SUB)
w('### **`b374`s AUDIT WAS RUN UNMODIFIED**, its own fixtures passing : `%s`.'
  % RB['instrument_selftest'])
w('### %-14s %8s %10s %9s %8s %8s %10s' % ('population', 'docs', 'sentences', 'hedged', 'openQ',
                                           'notes', 'hedge/k'))
for lbl, tt in (('KEYSTONE', KT), ('SUPPORT', ST)):
    w('### %-14s %8d %10d %9d %8d %8d %10.1f'
      % (lbl, tt['docs'], tt['sentences'], tt['hedged'], tt['openq'], tt['notes'], tt['per_k']))
w('### ### **THE RUBRIC SAYS A KEYSTONE MAY NOT CARRY THESE.** ### Against the order`s own rubric the')
w('### keystone layer carries them at ### **%.1f TIMES THE CONTROL RATE.**' % (KT['per_k'] / ST['per_k']))
w('### ### ### **AND NO DOCUMENT IS PRONOUNCED TO FAIL THE RUBRIC.** ### The measurement is the')
w('### product; ### **THE DISPOSITION IS THE AUTHOR`S AND IS A LATER ACT.**')
w('### **INSTANCES QUOTED AND LOCATED : `%d`.**' % RB['quoted'])
w('### ### **AND THE THIRD CLASS -- OPEN QUESTIONS STATED AS THE DOCUMENT`S OWN -- IS THIS ACT`S OWN')
w('### ### PREDICATE AND IS MARKED AS ONE.** ### It cannot see whether a question is the document`s')
w('### own or somebody else`s, and that limit is printed with its count.')
w('')

w(SUB)
w('### (6) COMPONENT 5 -- WHAT THE CENSUS DOES NOT KNOW.')
w(SUB)
w('### ### **EACH QUESTION IS PAIRED WITH WHAT WOULD ANSWER IT**, and none of them is a question this')
w('### act could have answered and did not.')
w('')
w('### ### **(1) WHICH OF THE THREE TESTS FOR `KEYSTONE` GOVERNS.** ### **A RULING.** ### Not a read:')
w('### the taxonomy is author-ruled, the order`s rubric is the author`s, and the existing census`s')
w('### test is banked. ### **THREE AUTHORITIES, AND ONLY THE AUTHOR CAN SAY WHICH IS THE STANDARD.**')
w('### ### **(2) WHETHER THE `%d` DOCUMENTS THAT DECLARE NO CLASS ARE MEANT TO.** ### **A RULING.**'
  % P['not_declared'])
w('### The taxonomy says every corpus document belongs to a tier; most carry no tier line. ### Either')
w('### the taxonomy`s `presumptive by class` rule already places them -- in which case the census')
w('### cannot see that placement from the documents -- or they are owed a line. ### **THIS SEAT')
w('### ### CANNOT TELL WHICH FROM THE DOCUMENTS THEMSELVES.**')
w('### ### **(3) WHETHER A SUBJECT CLUSTER WITH NO KEYSTONE IS A DEFECT OR A STATE.** ### **A')
w('### ### RULING.** ### `%d` clusters have documents and no keystone; the order asked for the fact'
  % len(NOKEY))
w('### and not for a verdict, and ### **A CLUSTER MAY SIMPLY NOT BE READY FOR ONE.**')
w('### ### **(4) WHETHER THE ARCHIVED AND DEPOSITED COPIES SHOULD BE IN THE POPULATION AT ALL.** ###')
w('### **A RULING.** ### They were read and counted because the order said `every document in the')
w('### papers repo`; ### **AND THE ORDER`S RUBRIC CLASSIFIES SEVERAL ARCHIVED SNAPSHOTS AS KEYSTONES**,')
w('### which is arithmetically true and may not be what was meant.')
w('### ### **(5) WHAT A GIVEN KEYSTONE`S CLUSTER IS, WHERE ITS OWN TEXT DOES NOT SAY.** ### **A READ,')
w('### ### AND ONE THIS ACT REFUSED.** ### `%d` keystones are `UNASSIGNED`; a reader who knows the'
  % len(CL['unassigned']))
w('### subject could assign them in minutes, and ### **THIS SEAT WOULD BE ASSIGNING BY RESEMBLANCE**,')
w('### which the order forbids by name.')
w('### ### **(6) WHETHER ANY CITATION IN COLUMN (b) IS STILL TRUE.** ### **A KERNEL CHECK.** ### The')
w('### column records what a document NAMES. ### `b372` and `b373` showed what happens when a named')
w('### thing has moved, and ### **THIS ACT OPENED NO KERNEL.**')
w('### ### **(7) WHERE THIS CENSUS SHOULD LIVE.** ### **A RULING**, and the order says so: the census')
w('### ### **DOES NOT CREATE A TRACKING DOCUMENT ON ITS OWN AUTHORITY**, so it is banked as this')
w('### act`s own product and its home is routed.')
w('')

w(SUB)
w('### (7) THE DESK, AND THE FOUR OPEN LISTS.')
w(SUB)
w('### ### **`%d` SWEPT. ### `%d` CLOSED. ### `%d` STANDING.**'
  % (Q['items'], Q['closed'], Q['standing']))
w('### ### ### **CLOSING NOTHING IS THE RIGHT ANSWER FOR AN ORIENTATION AND IS SAID RATHER THAN')
w('### ### ### APOLOGISED FOR.** ### `(R7)` closes an item whose OCCASION is gone; ### **A CENSUS')
w('### ### REMOVES NO OCCASION.**')
w('### **AND THE FOUR LISTS ARE RESTATED `OPEN` BY NAME:** ### the rows that cite at a ref nobody can')
w('### name; the rows grading a declaration the record has classified absent; the undated figures')
w('### across the roster; the bibliography entries nothing cites. ### **NONE IS CLOSED HERE.**')
w('')

w(SUB)
w('### (8) THE EXPECTATIONS, SCORED.')
w(SUB)
w('### ### ### **`(F1)` -- *fewer than half the keystones declare their own class line.* ### IT SPLITS')
w('### ### ### THREE WAYS, AND IT HAD TO.**')
w('###   under the taxonomy`s `Tier K` : ### **%.0f%% DECLARE -- REFUTED**' % pct('taxonomy_tier_k'))
w('###     (and trivially so: a document is in that set BECAUSE it declared, which is worth saying')
w('###      rather than scoring as a win)')
w('###   under the order`s rubric      : ### **%.0f%% DECLARE -- CONFIRMED**' % pct('order_rubric'))
w('###   under the existing census     : ### **%.0f%% DECLARE -- REFUTED**' % pct('existing_census'))
w('### ### **SO `(F1)` IS CONFIRMED UNDER EXACTLY ONE OF THE THREE TESTS.** ### **A SINGLE ANSWER')
w('### ### WOULD HAVE BEEN A COIN FLIP ON WHICH TEST THE SEAT HAPPENED TO PICK**, and the')
w('### registration fixed the three-way scoring before any document was read.')
w('')
w('### ### ### **`(F2)` -- *at least one cluster has support documents and no keystone.* ### CONFIRMED,')
w('### ### ### AND STRONGLY: `%d` SUBJECT CLUSTERS HAVE DOCUMENTS AND NO KEYSTONE.**' % len(NOKEY))
w('### ### **AND ONE HONEST QUALIFICATION:** ### most of those clusters carry no document this act')
w('### classified `SUPPORT` either -- they carry `OTHER`, because ### **THOSE DOCUMENTS DO NOT SAY')
w('### ### WHAT THEY DO.** ### The expectation`s spirit holds; its literal wording is met by the two')
w('### registry-addendum sections, which are not subject clusters, and the census says so.')
w('')
w('### ### ### **`(F3)` -- *column (d) is non-empty for most keystones.* ### CONFIRMED: `%d` OF `%d`.**'
  % (IN['d_nonempty'], IN['keystones']))
w('### The navigator`s reason -- ### *the findings layer grew faster than the synthesis layer this')
w('### year* ### -- is consistent with the measurement and is ### **NOT TESTED BY IT**: this act')
w('### measured the state, not the rates that produced it.')
w('')
w('### **`(E1)` -- THIS SEAT`S: *the three tests will not agree, and the disagreement will be large.*')
w('### ### CONFIRMED.** ### `%d` documents in all three, out of `%d` distinct documents the three'
  % (len(P['tests']['all_three']),
     len(set(P['tests']['taxonomy_tier_k']) | K32 | set(P['tests']['existing_census']))))
w('### tests select between them.')
w('### **`(E2)` -- THIS SEAT`S: *most documents will classify `OTHER`.* ### CONFIRMED: `%d` OF `%d`.**'
  % (P['order_tally'].get('OTHER', 0), P['documents']))
w('### ### **AND THE CENSUS SAYS WHICH IT IS, AS THE REGISTRATION REQUIRED:** ### this is ### **A FACT')
w('### ### ABOUT THE RUBRIC`S REACH, NOT ABOUT THE CORPUS.** ### The rubric distinguishes by what a')
w('### document DOES, and ### **MOST DOCUMENTS DO NOT SAY WHAT THEY DO** -- which is itself the kind')
w('### of thing an orientation exists to surface.')
w('')

w(SUB)
w('### (9) THE INCIDENT THIS ACT FILED AGAINST ITSELF.')
w(SUB)
w('### ### ### **THE FIRST REGISTRATION WAS LOCKED OVER A FACE CARRYING A LIVE STRUCK-STEM USE.**')
w('### The ritual runs the term scan BEFORE the lock. ### **THIS SEAT CHAINED THE LOCK ON THE')
w('### ### SATISFIABILITY AUDIT ALONE AND DID NOT READ THE TERM SCAN`S VERDICT**, which said')
w('### `NOT CLEAN`, one live use, in the act`s own voice.')
w('### ### **THE LOCKED FILE WAS NOT EDITED AND ITS SEAL WAS NOT TOUCHED.** ### `%s`, %s bytes, and'
  % (SHA1, NBY1))
w('### it verifies. ### **THE RULE IS `REWRITE THE SENTENCE, NEVER SOFTEN THE SCAN` (`b348`), AND A')
w('### ### SEALED FILE CANNOT BE REWRITTEN** -- so the face was RE-ISSUED, corrected, and re-locked,')
w('### and ### **NO COMPONENT HAD RUN WHEN EITHER LOCK WAS TAKEN.**')
w('### ### **AND THE CURE IS IN THE MECHANISM, NOT IN A NOTE:** ### the second lock was chained on')
w('### ### **ALL THREE GATES** -- the audit`s exit code, the registration gate`s verdict and the term')
w('### scan`s verdict. ### **A GATE NOBODY READS IS NOT A GATE**, which is this record`s own lesson')
w('### about arms, arriving this time in the ritual rather than in a suite.')
w('')

w(SUB)
w('### (10) WHAT THIS ACT DID NOT DO.')
w(SUB)
w('### **NO DOCUMENT WAS REPAIRED, REWRITTEN OR RECLASSIFIED.**')
w('### **NO CLASS WAS CONFERRED ON A DOCUMENT THAT DECLARES ITS OWN**, and no declared class was')
w('### overwritten or translated into the order`s vocabulary.')
w('### **NO ROW WAS EDITED. ### NO GRADE WAS MOVED. ### NO DEPOSIT WAS TOUCHED.**')
w('### **NO CLUSTER WAS ENUMERATED FROM A DIRECTORY NAME AND NO KEYSTONE WAS ASSIGNED BY RESEMBLANCE.**')
w('### **NO CELL WAS INFERRED. ### NO KERNEL WAS OPENED. ### NO CITATION WAS CHECKED.**')
w('### **NO INSTRUMENT WAS MODIFIED**, and this act licensed none.')
w('### **NO DOCUMENT WAS PRONOUNCED TO FAIL THE RUBRIC.**')
w('### **NO LIST WAS CLOSED**, and ### **NO NEW TRACKING DOCUMENT WAS CREATED.**')
w('### **NO `.lean` FILE WAS TOUCHED. ### NO BUILD WAS RUN. ### NO AXIOM PROFILE WAS RECOMPUTED.**')
w('### **NOTHING WAS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT.**')
w('### **NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NOTHING COMPILED AND NO BRIDGE TYPED.**')
w('### **NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED.**')
w('### **NOTHING HERE BEARS ON `h2`, ON TOTALITY OR ON THE ROSTER**, and this act makes no claim about')
w('### `h2` in either direction. ### `M-2` remains (SPECIFIED-NOT-STATED) under `b310`s cap. ### The')
w('### seam`s debt item 1 stands. ### The patent lane is carried on the patent seat`s report,')
w('### UNCONFIRMED on this seat`s record. ### **THE POSTURE LOCK IS SEPARATE. ### THE INSTRUMENT LANE')
w('### ### STAYS PARKED. ### THE WAVE STAYS PARKED.** ### `h2` stands exactly where the deposit left')
w('### it. ### **NOTHING DEPOSITS.**')
w('')

w(SUB)
w('### (11) THE SPECIES, AND THE CLOCKS.')
w(SUB)
w('### ### ### **NEW -- `THREE TESTS, ONE WORD`.** ### A census is only as meaningful as the')
w('### definition it runs on, and this corpus carries three definitions of `keystone` that select')
w('### overlapping but different documents. ### **THE MEASUREMENT THAT DEPENDS ON THE DEFINITION WILL')
w('### ### REVERSE WHEN THE DEFINITION DOES**, and it did, one act apart, with the same instrument.')
w('### ### ### **NEW -- `A GATE NOBODY READS IS NOT A GATE`.** ### The ritual`s term scan runs before')
w('### the lock and this seat chained the lock on a different gate. ### **THE CURE IS TO CHAIN ON ALL')
w('### ### OF THEM**, which the second lock did.')
w('### **MET AGAIN -- `PREDICATE_ONE_SHAPE`.** ### The cluster enumerator read the registry`s dated')
w('### maintenance headings as subject clusters until the partition was declared; ### **A SECTION')
w('### ### HEADING IS NOT A SUBJECT BECAUSE IT SITS WHERE SUBJECTS SIT.**')
w('')
w('### registration re-issued and locked at (UTC) %s' % LAT)
for n in ('b375_reads', 'b375_population', 'b375_clusters', 'b375_integration', 'b375_rubric',
          'b375_desk'):
    j = J(n)
    w('### %-18s run file `%s` recorded clock %s' % (n, j['run_file'], j['run_clock']))
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
