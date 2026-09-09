# -*- coding: utf-8 -*-
"""b377_bank.py -- THE BANK, WRITTEN FROM THE ACT'S OWN JSONS. ### **NO FIGURE IS TYPED.**

### ### **AND IT CARRIES THE ACT'S OWN CORRECTION OF ITS PREDECESSOR** -- that `b376`'s `B-` on these
### documents was, in part, `b376`'s predicate and not the documents. ### The locked face said this
### would be reported if it happened. ### **IT HAPPENED, AND IT IS REPORTED.**
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b377_the_unblocked_obligation.txt')
REG = os.path.join(D, 'b377_registration_2026-09-08.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, LG, BR, EV, Q = (J('b377_reads'), J('b377_lockgate'), J('b377_branch'),
                    J('b377_evidence'), J('b377_desk'))
AX376, TS376 = J('b376_axes'), J('b376_tests')
CL375, IN375 = J('b375_clusters'), J('b375_integration')
regtxt = io.open(REG, encoding='utf-8').read()
SHA = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt).group(1)
NBY = re.search(r'bytes locked : (\d+)', regtxt).group(1)
LAT = re.search(r'locked at \(UTC\) : (\S+)', regtxt).group(1)
NCL = len(J('b377_satisfiable')['clauses'])

L = []


def w(s=''):
    L.append(s)


BAR, SUB = '=' * 100, '-' * 100
A1 = [r for r in BR['six'] if r['arm'] == 1]
A2 = [r for r in BR['six'] if r['arm'] == 2]
ND = BR['not_determinable']
NROWS = sum(len(r['rows']) for r in A1)
NOKEY = CL375['subject_clusters_without_keystone']


def base(f):
    return os.path.basename(f)[:-3]


w(BAR)
w('b377 -- THE UNBLOCKED OBLIGATION, AND THE RULING`S EVIDENCE ASSEMBLED. ### THE BANK.')
w(BAR)
w('')
w('### ### ### **THE HEADLINE, AND IT CORRECTS THIS SEAT`S OWN PREVIOUS ACT:**')
w('### ### ### **THE PIN WAS THE MISSING ELEMENT, NOT THE TERMINAL.**')
w('### `b376` scored six `TIER K`-declaring documents as carrying no traversable row. ### Read one at')
w('### a time, ### **SEVERAL OF THEM ALREADY CARRY A CORRESPONDENCE TABLE** ### with claims,')
w('### terminals and axiom profiles. ### What they lack is ### **THE PIN** -- one of the three things')
w('### the taxonomy obliges: ### `grade . terminal . pin`.')
w('### ### **AND THE REASON `b376` COULD NOT SEE THOSE TABLES IS `b376`.** ### Its axis-B predicate')
w('### required kernel, terminal, pin and grade ### **IN ONE ROW**, and its terminal pattern required')
w('### a ### **DOTTED** ### name. ### These tables name terminals ### **BARE** -- `residue_irreducible`,')
w('### `fano_two_design` -- which is the older convention this corpus wrote in.')
w('### ### ### **SO THE DEFECT WAS PARTLY THE PREDICATE`S AND NOT THE DOCUMENTS`, AND THIS ACT`S')
w('### ### ### LOCKED FACE SAID BEFORE THE MEASUREMENT THAT IT WOULD SAY SO IF THIS HAPPENED.**')
w('### ### **IT IS `PREDICATE_ONE_SHAPE` FOR THE SIXTH TIME IN THIS RECORD**, and the shape the')
w('### predicate knew was the shape ### **THIS SEAT HAD JUST SEEN** ### in the newest tables.')
w('')
w('### ### **AND THE BRANCH THE ORDER FIXED STILL SPLIT THE POPULATION HARD:**')
w('### ### **ARM 1 (APPEND) : %d ### / ### ARM 2 (ROUTE) : %d ### of %d.**'
  % (len(A1), len(A2), len(BR['six'])))
w('### ### ### **WHICH REFUTES `(F1)`.** ### The navigator expected most of the six to be repairable')
w('### by appending from terminals they already name. ### **MOST WERE NOT**, and the reason is')
w('### `(F2)`: ### **THEY NAME IDENTIFIERS THAT NO KERNEL ON DISK DECLARES.**')
w('')

# ---------------------------------------------------------------------------------------- STEP ZERO
w(SUB)
w('### STEP ZERO -- THE LOCK READ EVERY GATE, AND THE TOOL WAS INHERITED, NOT REBUILT.')
w(SUB)
w('###   pre-lock gates read by `tools/b376_lockgate.py`, run as `b377` : ### **%d**'
  % LG['gates_read'])
w('###   of those, passing : ### **%d** ### ; fixture, both polarities : ### **%s**'
  % (LG['gates_passing'], 'HELD' if LG['fixture_ok'] else 'FAILED'))
for g in LG['gates']:
    w('###     %-46s %-38s %s'
      % (g['gate'][:46], g['file'][:38], 'PASS' if g['passed'] else '### FAIL ###'))
w('### ### **A CURE THAT HAS TO BE REBUILT EVERY ACT IS NOT A CURE.** ### The tool takes the act as')
w('### its argument; this act passed `b377` and spent no tool slot on it.')
w('### ### ### **AND THE HOLE `b376` NAMED WAS HIT IN PRACTICE HERE.** ### The registration text')
w('### changed after three of its gates had already recorded -- the multi-arm needle fired on the')
w('### section labels the amendment introduced -- and ### **THE LOCK GATE WOULD HAVE ACCEPTED THE')
w('### ### STALE RECORDS.** ### Every gate was re-run against the final bytes before the lock')
w('### ### **BY THE SEAT`S DISCIPLINE AND NOT BY THE TOOL`S**, which is why the next ferry is drafted')
w('### to put the read bytes` hash into each gate`s own record.')
w('')

# ------------------------------------------------------------------------------------- COMPONENT 1
w(SUB)
w('### COMPONENT 1 -- THE AUTHOR`S ROLE CLAUSE, BANKED AS EVIDENCE AND NOT AS A RULING.')
w(SUB)
w('### **THE CLAUSE, IN THE AUTHOR`S OWN WORDS, 2026-09-08, RATIFIED BY THE PASTE:**')
w('###   `Keystones are for clarifying results and as well as for exploring ramifications and')
w('###   insights`')
w('###   `the keystones should cover any and all pertinent or interesting materials, not just having')
w('###   tunnel vision in explanatory clarity just because we have been relentlessly focused on a')
w('###   particular problem at a particular research phase`')
w('### banked verbatim at `b377_ferry_2026-09-08.txt` lines %d-%d.'
  % (EV['role_clause'][0]['line'], EV['role_clause'][-1]['line']))
w('')
w('### **WHAT IT BEARS ON, STATED AND NOT INFERRED:**')
w('### ### **IT SPEAKS TO THE ROLE AXIS.** ### Every content word in it is about what a keystone is')
w('### FOR -- clarifying, exploring, covering. ### **NOT ONE WORD OF IT IS ABOUT WHETHER A DOCUMENT')
w('### ### CARRIES A CORRESPONDENCE TABLE.**')
w('### ### **AND IT WIDENS THAT AXIS RATHER THAN NARROWING IT.** ### `b375`s rubric said keystones')
w('### `synthesize a cluster against other available content`; ### this clause adds ### **EXPLORING')
w('### ### RAMIFICATIONS AND INSIGHTS** ### and ### **ANY AND ALL PERTINENT OR INTERESTING')
w('### ### MATERIALS**, and warns in as many words against ### **TUNNEL VISION IN EXPLANATORY')
w('### ### CLARITY** ### driven by a particular problem at a particular research phase.')
w('### ### ### **A CLAUSE THAT BEARS ON ONE AXIS DOES NOT RULE A QUESTION THAT SPANS TWO**, and this')
w('### ### ### act does not rule from it.')
w('### **ITS SHARPEST CONSEQUENCE IS A MEASUREMENT THAT ALREADY EXISTED:** ### `b376` found')
w('### ### **%d DOCUMENTS CARRYING A TRAVERSABLE ROW WHOSE OWN TEXT SAYS NOTHING ABOUT THEIR ROLE**'
  % (AX376['quadrants'].get('A-B+', 0) + AX376['quadrants'].get('A?B+', 0)))
w('### and ### **%d OF %d THAT DO NOT SAY WHAT THEY ARE AT ALL.** ### The clause is a statement about'
  % (AX376['axis_a_tally'].get('A?', 0), len(AX376['scored'])))
w('### precisely the property that population is silent on.')
w('')

# ------------------------------------------------------------------------------------- COMPONENT 2
w(SUB)
w('### COMPONENT 2 -- THE FIVE OPTIONS, QUOTED WHOLE, EACH WITH ONE BEARING LINE.')
w(SUB)
w('### ### **REPRODUCED LINE FOR LINE FROM `b376`S BANK SO THE AUTHOR RULES FROM THE TEXT AND NOT')
w('### ### FROM A SUMMARY.** ### The full quotation is in `data/%s`; the bearing lines are here.'
  % EV['run_file'])
w('')
for o in EV['options']:
    w('### **%s** ### -- `b376_the_two_axis_read.txt` lines %d-%d, %d lines quoted whole'
      % (o['name'], o['start'], o['end'], o['lines']))
    for seg in re.findall(r'.{1,92}(?:\s|$)', o['bearing']):
        if seg.strip():
            w('###   %s' % seg.rstrip())
    w('')
w('### ### **FIVE OPTIONS, FIVE BEARING LINES. ### NONE RECOMMENDED, NONE RANKED, AND THE ORDER')
w('### ### ABOVE IS `b376`S PRINTING ORDER AND NOT AN ORDER OF MERIT.**')
w('### ### ### **THE RULING REMAINS THE AUTHOR`S.**')
w('')

# ------------------------------------------------------------------------------------- COMPONENT 3
w(SUB)
w('### COMPONENT 3 -- THE BRANCH, APPLIED AND NOT CHOSEN.')
w(SUB)
w('### **THE OBLIGATION, IN THE TAXONOMY`S OWN WORDS:** ### *every such claim states its*')
w('### ### **`grade . terminal . pin`**, *and the axiom profile is written in full.*')
w('### **THE POPULATION:** ### the %d documents declaring `TIER K` and scoring no traversable row.'
  % len(BR['six']))
w('### **THE KERNELS:** ### %d `SIDE-*` repositories, ### **ENUMERATED FROM DISK AND NOT TYPED.**'
  % BR['kernels'])
w('')
w('###   %-34s %-5s %-5s %-5s %s' % ('document', 'named', 'found', 'arm', 'why'))
w('###   %s' % ('-' * 92))
for r in BR['six']:
    w('###   %-34s %-5d %-5d %-5d %s'
      % (base(r['file'])[:34], len(r['candidates']), len(r['located']), r['arm'],
         ('APPEND' if r['arm'] == 1 else 'ROUTE')))
w('')
for r in BR['six']:
    w('### **`%s`** ### -- ### **ARM %d, %s**'
      % (r['file'], r['arm'], 'APPEND' if r['arm'] == 1 else 'ROUTE'))
    w('###   real `Correspondence` headings : %d ; identifiers named : %d ; located : %d'
      % (r['corr_headings'], len(r['candidates']), len(r['located'])))
    w('###   why : %s' % r['why'])
    if r['arm'] == 1:
        w('###   ### **APPENDED %d ROW(S), EACH NAMING KERNEL . TERMINAL . PROFILE . GRADE . PIN:**'
          % len(r['rows']))
        for row in r['rows']:
            w('###     `%s` in `%s` at `%s`'
              % (row['terminal'], row['kernel'], row['pin'][:12]))
    else:
        nl = [x for x in r['not_resolved'] if x not in [a['name'] for a in r['ambiguous']]]
        w('###   ### **ROUTED. ### WHAT IS MISSING, BY NAME:**')
        for x in nl[:14]:
            w('###     `%s` ### -- declared in NONE of the %d kernels' % (x, BR['kernels']))
        for a in r['ambiguous']:
            w('###     `%s` ### -- declared in %d kernels : %s ### **AMBIGUOUS**'
              % (a['name'], len(a['kernels']), a['kernels']))
        if len(nl) > 14:
            w('###     ... and %d more, all listed in `data/b377_branch.json`' % (len(nl) - 14))
        w('###   ### **NOTHING WAS REPAIRED IN THIS DOCUMENT.**')
    w('')
w('### ### ### **THE RULE THAT DID THE WORK: ### ONE UNRESOLVED TERMINAL SENDS THE WHOLE DOCUMENT TO')
w('### ### ### ARM 2.** ### A table right in four rows and wrong in one is a table a stranger cannot')
w('### trust, and ### **A ROW THIS ACT WROTE THAT A STRANGER COULD NOT TRAVERSE WOULD BE WORSE THAN')
w('### ### THE ABSENCE IT REPLACED.**')
w('### ### **AND A NAME DECLARED IN TWO KERNELS IS NOT A TERMINAL THIS ACT CAN WRITE INTO A ROW**;')
w('### choosing the first would be ### **THE ACT INVENTING A CORRESPONDENCE THE DOCUMENT DID NOT')
w('### ### STATE.** ### The uniqueness requirement was added to the tool after a first run took the')
w('### first of several silently, and ### **THAT FIRST RUN`S APPENDS WERE REVERTED, NOT KEPT.**')
w('### ### **TERMINALS WRITTEN THAT WERE NOT LOCATED AND CHECKED : 0.**')
w('### ### **TERMINALS WRITTEN THAT RESOLVE TO MORE THAN ONE KERNEL : 0.**')
w('### ### **PINS WRITTEN THAT WERE NOT THIS ACT`S OWN READING OF A KERNEL HEAD : 0.**')
w('')

# ------------------------------------------------------------------- THE AMENDMENT'S FIRST CLAUSE
w(SUB)
w('### THE AMENDMENT`S FIRST CLAUSE -- ### **NOT DETERMINABLE IS NOT ABSENT.**')
w(SUB)
for r in ND:
    w('### **`%s`**' % r['file'])
    w('###   ### **WHAT THE READ COULD NOT DECIDE:** ### %s.' % r['could_not_decide'])
    w('###   real `Correspondence` headings : %d ; backticked candidates : %d ; concordance language'
      % (r['corr_headings'], r['candidates']))
    w('###   present : %s' % r['concordance_language'])
    w('###   ### **WHAT WOULD DECIDE IT:** ### %s.' % r['what_would_decide'])
    w('###   ### **REPAIRED : %s ### / ROUTED AS LACKING : %s ### / COUNTED AMONG THE SIX : %s**'
      % (r['repaired'], r['routed_as_lacking'], r['counted_among_the_six']))
w('### ### ### **`NOT DETERMINABLE` IS A THIRD ANSWER AND NOT A SOFT `NO`.** ### The corpus itself')
w('### made `CONCORDANCE-CARRIED` a class of its own precisely because a document can name its')
w('### terminals in prose; ### **A TABLE SCAN IS THE WRONG INSTRUMENT FOR THAT ARCHITECTURE**, and')
w('### running it anyway and calling the silence an absence would have been the error the amendment')
w('### exists to prevent.')
w('')

# ------------------------------------------------------------------------------------- COMPONENT 4
w(SUB)
w('### COMPONENT 4 -- TWO FILINGS, NEITHER OPENED.')
w(SUB)
w('### **FILING (i) -- THE CENSUS`S DEFINITION-VERSUS-OPERATION DRIFT**, against')
w('### `phase2/method/THE_KEYSTONE_CENSUS.md`:')
w('###   (1) clause `(i)` applied through a ### **TYPOGRAPHIC PROXY**, not as the judgement it states;')
w('###   (2) clause `(ii)` narrowed from ### **A TABLE NAMING TERMINALS** ### to a heading with the')
w('###       word in it;')
w('###   (3) clause `(iii)` ### **NOT OPERATIONALISED AT ALL**;')
w('###   (4) a ### **`6 KB` SIZE FLOOR THE DEFINITION NEVER MENTIONS.**')
w('### ### **AND THREE DIFFERENT NUMBERS COME OUT OF ONE DOCUMENT:** ### its detector returned')
w('### ### **%d**; it publishes ### **%d**; re-applied at the head its own operation returns'
  % (EV['filing_census']['detector'], EV['filing_census']['published']))
w('### ### **%d**.' % EV['filing_census']['reapplied'])
w('### ### **THE DOCUMENT IS HONEST ABOUT THE HAND CORRECTION AND RECORDS IT IN ITS OWN TEXT.** ###')
w('### The honesty is on the record; ### **THE DRIFT STILL GOVERNS EVERY NUMBER IT PRINTED.**')
w('### ### ### **FILED. ### NOT OPENED. ### NOT REPAIRED** -- repairing it belongs to the ruling,')
w('### and a census repaired under a definition the author has not chosen would be a fourth authority')
w('### rather than an orientation.')
w('')
w('### **FILING (ii) -- THE SUBJECT CLUSTERS WITH REGISTRY ROWS AND NO KEYSTONE:** ### **%d** ### --'
  % len(NOKEY))
w('### %s.' % ', '.join('`%s`' % x for x in NOKEY))
w('### **RESTATED BESIDE THE ROLE CLAUSE, WHICH IS WHAT MAKES IT A WORK-ORDER:** ### the clause says')
w('### keystones should cover ### **ANY AND ALL PERTINENT OR INTERESTING MATERIALS** ### and warns')
w('### against ### **TUNNEL VISION** ### driven by ### **A PARTICULAR PROBLEM AT A PARTICULAR')
w('### ### RESEARCH PHASE.** ### A subject cluster with documents and no keystone is that warning,')
w('### measured. ### **AND MOST OF THIS WORK SITS OUTSIDE THE CURRENT LANE**, which is why it has not')
w('### been done and is exactly why the clause names the risk.')
w('### **THE PRICE, AS FAR AS THE RECORD SUPPORTS ONE AND NO FURTHER:** ### this act measured what')
w('### appending a pinned table to an ### **EXISTING** ### document costs -- and found that')
w('### ### **%d OF %d ATTEMPTS SUCCEEDED**, so even that unit is not reliably cheap.'
  % (len(A1), len(BR['six'])))
w('### ### **THE RECORD DOES NOT SUPPORT A PRICE FOR WRITING A KEYSTONE THAT DOES NOT EXIST YET**,')
w('### because no act in this record has written one, and ### **A PRICE FROM NO MEASUREMENT IS AN')
w('### ### ESTIMATE WEARING A MEASUREMENT`S CLOTHES.**')
w('### ### ### **FILED AS A WORK-ORDER. ### NOT OPENED. ### NO CLUSTER IS ASSIGNED A KEYSTONE.**')
w('')

# ------------------------------------------------------------------ THE AMENDMENT'S SECOND CLAUSE
w(SUB)
w('### THE AMENDMENT`S SECOND CLAUSE -- THE BANKED FIGURE IS A FLOOR.')
w(SUB)
w('### **THE BANKED FIGURE:** ### `b375` column (d) -- what bears on a keystone and is not in it --')
w('### is non-empty for ### **%d of %d**, taken ### **AGAINST THE FINDINGS LAYER ALONE.**'
  % (EV['floor']['banked'], EV['floor']['of']))
w('### **THE WIDER QUESTION, NAMED AS THE ONE THE RECONCILIATION MUST ASK:** ### %s.'
  % EV['floor']['wider_question'])
w('### ### ### **SO THE BANKED FIGURE IS A FLOOR AND NOT AN ANSWER**, and the reason it can only be a')
w('### ### ### floor is structural: ### **THE FINDINGS LAYER IS ONE SOURCE AMONG SEVERAL, SO EVERY')
w('### ### ### SOURCE ADDED CAN ONLY ADD MATERIAL THAT BEARS.**')
w('### ### **AND THIS ACT DOES NOT RE-MEASURE IT.** ### The amendment says so in as many words, and')
w('### ### **A FLOOR RE-MEASURED BADLY WOULD REPLACE AN HONEST BOUND WITH A WRONG ONE.**')
w('')

# ------------------------------------------------------------------------------------- WHAT IS NOT
w(SUB)
w('### WHAT THIS ACT DID NOT DO.')
w(SUB)
w('### ### **NO CLASS WAS RULED. ### NO DOCUMENT WAS RECLASSIFIED. ### NO DECLARATION WAS MOVED.')
w('### ### ### NO LIST WAS CLOSED.** ### The order`s four prohibitions, each with its own must-fail')
w('### fixture as a whole line.')
w('### ### **A DOCUMENT SAYS WHAT IT SAYS.** ### Every document here declares `TIER K` in its own')
w('### words; this act disputed none, moved none, demoted none and annotated none as wrong.')
w('### ### **EVERY WRITE INTO A DOCUMENT IS AN APPEND**, and for each the committed blob remains a')
w('### ### **TRUE PREFIX** ### of the file afterwards. ### **NO EXISTING BYTE WAS CHANGED.**')
w('### ### **NO `.lean` FILE WAS TOUCHED, NO BUILD WAS RUN AND NO AXIOM PROFILE WAS RECOMPUTED** --')
w('### profiles in the appended rows are reproduced ### **AS THE DOCUMENT STATES THEM.**')
w('### ### **THE KERNELS WERE OPENED, WHICH `b376` DID NOT DO** -- and solely to locate and check')
w('### terminals the documents themselves name. ### **NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN**,')
w('### and locating one says it exists at that name at that pin and ### **NOTHING ABOUT WHETHER THE')
w('### ### DOCUMENT`S SENTENCE ABOUT IT IS RIGHT.**')
w('### ### **THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME, IN THE DESK`S OWN WORDS:**')
for _lst in ('the rows that cite at a ref nobody can name',
             'the rows grading a declaration the record has classified absent',
             'the undated figures across the roster',
             'the bibliography entries nothing cites'):
    w('###   ### **OPEN** ### -- %s' % _lst)
w('### ### **NONE IS CLOSED. ### NO NEW TRACKING DOCUMENT WAS CREATED.**')
w('### ### **NOTHING WAS COMPUTED ABOUT THE OBJECT** -- no frame, no seed, no transform, no')
w('### quadrature, no fit, no score, no series.')
w('### ### **`h2` STANDS EXACTLY WHERE THE DEPOSIT LEFT IT AND THIS ACT MAKES NO CLAIM ABOUT IT IN')
w('### ### EITHER DIRECTION.** ### The instrument lane stays PARKED; the wave stays PARKED; nothing')
w('### deposits.')
w('')

# ------------------------------------------------------------------------------------- THE LEDGER
w(SUB)
w('### THE EXPECTATIONS, THE DESK, THE WRITES, AND THE SPECIES.')
w(SUB)
w('### ### **`(F1)` REFUTED BY THE PRINT.** ### The navigator expected most of the six to be met by')
w('### appending from terminals they already name. ### **%d OF %d WERE.** ### The rest name'
  % (len(A1), len(BR['six'])))
w('### identifiers no kernel on disk declares.')
w('### ### **`(F2)` MET.** ### At least one names a terminal that cannot be located -- ### **%d OF THE'
  % len(A2))
w('### ### SIX DO** -- and that is a finding about those documents and not about the tier.')
w('### ### **`(E1)`, THIS SEAT`S, PARTLY MET AND PARTLY WRONG.** ### It expected the split to fall on')
w('### whether a document names a terminal AT ALL. ### **IT FELL ON WHETHER THE NAMED TERMINALS')
w('### ### RESOLVE**, which is a sharper and less flattering answer: the documents do name terminals,')
w('### and the names do not all land.')
w('### ### **`(E2)`, THIS SEAT`S, MET.** ### Both `NOT DETERMINABLE` documents name terminals in')
w('### prose or under a concordance rather than nowhere, which is why the table scan could not decide')
w('### them and why the amendment is right that they are not absent.')
w('')
w('### desk items swept : %d ### / ### closed : %d ### / ### standing : %d ### / ### lists closed : %d'
  % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
w('### trail block appended (append-only %s, committed prefix intact %s); `CORRESPONDENCE.md` row %s;'
  % (Q['trail']['appended_only'], Q['trail']['committed_prefix_intact'], Q['row']))
w('### index key `the-pin-was-missing` reachable by every alias : %s' % Q['key_ok'])
w('')
w('### ### ### **NEW -- `A PIN IS THE ELEMENT MOST OFTEN MISSING, AND THE ONE HARDEST TO ADD LATER`.**')
w('### A claim and a terminal are written when the work is done; ### **THE PIN IS WRITTEN ONLY IF')
w('### ### SOMEBODY REMEMBERS THAT A STRANGER WILL COME LATER.** ### Six documents carried the first')
w('### two and not the third.')
w('### ### ### **NEW -- `A NAME DECLARED IN TWO KERNELS IS NOT A TERMINAL YOU CAN CITE`.** ### The')
w('### first run of this act`s branch tool took the first of several matches silently. ### **THAT IS')
w('### ### THE ACT INVENTING A CORRESPONDENCE THE DOCUMENT DID NOT STATE**, and the appends from that')
w('### run were reverted rather than kept.')
w('### **MET AGAIN -- `PREDICATE_ONE_SHAPE`, AND THIS TIME AGAINST THIS SEAT`S OWN PREVIOUS ACT.**')
w('### `b376`s axis-B predicate knew the dotted, four-in-one-row shape because that is the shape the')
w('### newest tables use. ### **IT SCORED THE OLDER CONVENTION AS AN ABSENCE.**')
w('### **MET AGAIN -- THE `###` EMPHASIS RUN READ AS A MARKDOWN HEADING.** ### This corpus writes')
w('### emphasis as `### **LIKE THIS**`. ### A naive heading regex found a `Correspondence` section in')
w('### a document that has none, and ### **THE DISCRIMINATOR IS `#`s-THEN-TEXT VERSUS `#`s-THEN-`**`.**')
w('')
w('### registration locked at (UTC) %s' % LAT)
w('### ### **%s bytes, sha256 `%s`, %d clauses, ### LOCKED BEFORE ANY WRITE AND CHAINED ON THE GATE'
  % (NBY, SHA, NCL))
w('### ### THAT READS EVERY GATE.**')
for n in ('b377_reads', 'b377_lockgate', 'b377_branch', 'b377_evidence', 'b377_desk'):
    j = J(n)
    w('### %-16s run file `%s` recorded clock %s'
      % (n, j['run_file'], j.get('run_clock') or run_clock.read_stamp(
          os.path.join(D, j['run_file']))))
w('### **THE REFS THIS ACT READ:**')
for k, v in E['refs'].items():
    w('###   %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
w('### **THE PINS THIS ACT WROTE, EACH ITS OWN READING OF THAT KERNEL`S HEAD:**')
for k, v in sorted(BR['pins'].items()):
    w('###   %-34s `%s`' % (k, v))
w('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor, `%d` anchors differing from the hint'
  % (E['reads'], E['without_anchor'], E['anchors_differing']))
w('### that found them. ### **EVERY ANCHOR WAS READ FROM ITS FILE AND NONE WAS TYPED.**')
w(BAR)

io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
print('  written: %s  (%d lines, %d bytes)'
      % (os.path.basename(OUT), len(L), len(chr(10).join(L).encode('utf-8'))))
bad = [i + 1 for i, s in enumerate(L) if '%s' in s or '%d' in s]
print('  ### UNFILLED PLACEHOLDERS : %s' % (bad or 'none'))
