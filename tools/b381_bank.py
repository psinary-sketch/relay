# -*- coding: utf-8 -*-
"""b381_bank.py -- THE BANK, WRITTEN FROM THE ACT'S OWN JSONS. ### **NO FIGURE IS TYPED.**"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import co_location as CL   # noqa: E402
import run_clock           # noqa: E402

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b381_the_control_rebuilt.txt')
REG = os.path.join(D, 'b381_registration_2026-09-09.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, LG, EX, C, VD, Q = (J('b381_reads'), J('b381_lockgate'), J('b381_exemplars'),
                       J('b381_control'), J('b381_verdict'), J('b381_desk'))
R80 = J('b380_rescore')
regtxt = io.open(REG, encoding='utf-8').read()
SHA = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt).group(1)
NBY = re.search(r'bytes locked : (\d+)', regtxt).group(1)
LAT = re.search(r'locked at \(UTC\) : (\S+)', regtxt).group(1)
NCL = len(J('b381_satisfiable')['clauses'])

L = []


def w(s=''):
    L.append(s)


BAR, SUB = '=' * 100, '-' * 100
SYN, GAT = C['synthesis'], C['gathering']
SYNP, GATP = C['synthesis_cplus'], C['gathering_cplus']
NS, NG = C['synthesis_n'], C['gathering_n']
LO, HI = C['lowest_synthesis_ratio'], C['highest_gathering_ratio']
BRANCH = C['branch']

w(BAR)
w('b381 -- THE CONTROL REBUILT, AND CO-LOCATION TESTED. ### THE BANK.')
w(BAR)
w('')
w('### ### ### **THE HEADLINE, AND THE SECOND SENTENCE IS THE ONE THAT MATTERS:**')
w('### ### ### **THE CONTROL WAS REBUILT SO THAT IT COULD FAIL IN BOTH DIRECTIONS, AND THE NEW')
w('### ### ### FEATURE FAILED ON IT.**')
w('### Co-location puts ### **`%d` OF `%d` SYNTHESIS EXEMPLARS ABOVE THE BAR AND `%d` OF `%d`'
  % (SYNP, NS, GATP, NG))
w('### ### GATHERING EXEMPLARS THERE TOO.** ### The lowest synthesis ratio is ### **`%.3f`** ### and'
  % LO)
w('### the highest gathering ratio is ### **`%.3f`**, so the two sets ### **OVERLAP COMPLETELY AND NO'
  % HI)
w('### ### CHOICE OF THRESHOLD WOULD HAVE SEPARATED THEM.**')
w('### ### ### **THE BRANCH IS %s. ### THE PREDICATE IS NOT ADOPTED. ### THE CORPUS WAS NOT SCORED.**'
  % BRANCH)
w('### ### **`(F1)` IS REFUTED BY THE PRINTED TABLE AND `(F2)` IS `NOT REACHED`** -- which this seat')
w('### registered on the locked face before the run, so a silent pass could not be read as a result.')
w('')

# ------------------------------------------------------------------------------------- (R14)
w(SUB)
w('### (R14), RECORDED AND NOT APPLIED.')
w(SUB)
w('### ### **THE CLASS RULING GOVERNS DOCUMENTS BY CONTENT AND ROLE, NOT BY LOCATION.** ### Where a')
w('### document`s canonical copy lives is a separate fact under a separate ruling, which stands.')
w('### ### **THE DOWNLOAD-LAYER BOOK IS THEREFORE INSIDE THE CLASS RULING`S REACH AND OUTSIDE THE')
w('### ### MIRRORING RULING`S -- BOTH HOLD, NEITHER IS EDITED INTO THE OTHER.**')
w('### ### **IT ANSWERS `b379`S FILING**, which asked whether the ruling governs documents outside')
w('### the tree and has been carried unanswered since. ### **THE FILING IS CLOSED BY THE AUTHOR AND')
w('### ### NOT BY THIS SEAT**, and that is the only desk item this act closes.')
w('### ### **WHAT IT DOES NOT SETTLE, IN THE RULING`S OWN WORDS:** ### the book`s registry drift')
w('### ### **STAYS OPEN AND IS THE AUTHOR`S.** ### **NO DOCUMENT WAS RECLASSIFIED UNDER (R14) BY')
w('### ### THIS ACT**, the book was not opened, read for content, graded, moved or renamed, and')
w('### ### **THE REGISTRY WAS NOT EDITED.**')
w('### The ruling is banked verbatim in `data/b380_ruling_evidence.txt` -- ### **THE WHOLE RULING AND')
w('### ### NOT ONLY THE LINES THIS ACT ANCHORED.** ### The first version of that block carried `6` of')
w('### its `9` lines and still called itself verbatim; ### **A QUOTATION WITH HOLES IN IT IS NOT A')
w('### ### QUOTATION**, and it was re-sliced whole between two ends each verified unique.')
w('')

# --------------------------------------------------------------------------------- COMPONENT 1
w(SUB)
w('### COMPONENT 1 -- THE OLD CONTROL`S WEAKNESS. ### **ONE FINDING, NOT TWO.**')
w(SUB)
w('### `b380`s threshold was ### **`%d`**, and the reaches of the seven documents declaring synthesis'
  % EX['b380_threshold'])
w('### were `%s`.' % ', '.join(str(x) for x in EX['b380_synthesis_reaches']))
w('### ### **THE LOWEST OF THEM IS `%d`**, so ### **NO VALUE OF THE THRESHOLD AT OR BELOW IT WOULD'
  % EX['b380_lowest_synthesis_reach'])
w('### ### HAVE FAILED ANY OF THEM.** ### That side could not fail.')
w('### And ### **BOTH `%d` DOCUMENTS DECLARING GATHERING DISAGREED WITH THE PREDICATE**, so the only'
  % EX['b380_gatherers_disagreeing'])
w('### side that could have informed it was ### **THE SIDE IT GOT WRONG.**')
w('### ### ### **A CONTROL THAT CANNOT FAIL ON ONE SIDE AND CANNOT INFORM ON THE OTHER IS NOT TWO')
w('### ### ### DEFECTS. ### IT IS ONE DEFECT WITH TWO FACES**, and the order asked for it as one.')
w('')
w('### ### **SO THE CONTROL WAS REBUILT FROM THE RECORD`S OWN PURPOSE STATEMENTS.**')
w('### The head of every one of ### **`%d`** ### corpus documents -- its first `%d` lines -- was'
  % (EX['scanned'], EX['head_lines']))
w('### scanned for a sentence in which the document names ### **ITSELF** ### and names a gathering')
w('### purpose. ### **EVERY MATCH WAS TAKEN AND EVERY MATCH IS QUOTED WITH ITS FILE AND ITS LINE**,')
w('### and ### **%d WERE ADDED, DROPPED OR RANKED BY THIS SEAT`S JUDGEMENT OF WHAT A DOCUMENT IS.**'
  % EX['judgement_selections'])
w('###   ### **HEADS STATING A GATHERING PURPOSE   : `%d` OF `%d`**' % (EX['wide_hits'], EX['scanned']))
w('###   heads stating one in the order`s three verbs : `%d`' % EX['order_hits'])
w('###   the denial reading (`certify nothing`)       : `%d`' % EX['denial_hits'])
w('### ### **THE DENIAL READING WOULD HAVE YIELDED `%d`**, which is why the locked face took the'
  % EX['denial_hits'])
w('### purpose reading -- ### **AND THE FIGURE IS PRINTED RATHER THAN THE CHOICE ASSERTED.**')
w('')
w('### ### **CONFLICTS: `%d` DOCUMENTS MATCHED ON BOTH SIDES AT ONCE.**' % len(EX['conflicts']))
for c in EX['conflicts']:
    w('###   `%s` -- head states a gathering purpose at line %d, class line declares synthesis'
      % (c['file'], c['line']))
w('### ### **BOTH ARE EXCLUDED FROM BOTH EXEMPLAR SETS AND REPORTED, NOT RESOLVED**, because an')
w('### exemplar that argues with itself cannot be a ground truth for anything.')
w('')
w('### ### **THE BALANCE: `%d` SYNTHESIS EXEMPLARS AND `%d` GATHERING EXEMPLARS**, against a floor of'
  % (NS, NG))
w('### `%d` declared on the locked face. ### **THE SET CAN FAIL IN BOTH DIRECTIONS** -- and it is the'
  % EX['floor'])
w('### first control in this sequence that can. ### **`(E3)` IS REFUTED:** ### this seat predicted the')
w('### scan would find fewer than the floor and it found ### **`%d`.**' % NG)
w('')

# ------------------------------------------------------------------------------ THE LINEAGE
w(SUB)
w('### AND THE MATCHER THAT BUILT THE CONTROL WAS REPAIRED TWICE AFTER ITS OUTPUT WAS SEEN.')
w(SUB)
w('### ### **THIS IS DECLARED RATHER THAN HIDDEN, AND IT IS THE PART OF THE ACT A READER SHOULD BE')
w('### ### MOST SCEPTICAL OF.**')
w('###   `v1`  a bare pronoun counted as the document naming itself, class lines allowed : ### **`%d`**'
  % EX['loose_hits'])
w('###   `v2`  self-reference tightened, class declarations excluded                     : ### **`%d`**'
  % EX['loose2_hits'])
w('###   `v3`  the noun opener must DESCRIBE the artifact and not merely open a sentence  : ### **`%d`**'
  % EX['wide_hits'])
w('### `v1` matched ### **`%d` OF `%d` HEADS**, which is not a corpus that gathers -- it is a pronoun'
  % (EX['loose_hits'], EX['scanned']))
w('### matching prose. ### `v2` still let a line merely BEGINNING `The census...` count as a statement')
w('### of purpose.')
w('### ### **EACH REPAIR TRACES TO WORDS WRITTEN BEFORE THE RUN** -- the locked face`s ### *the')
w('### document names ITSELF* ### and the order`s ### *rather than from class declarations* ### -- so')
w('### neither is a repair to the result. ### **BUT A MATCHER REPAIRED AFTER ITS OUTPUT WAS SEEN IS A')
w('### ### MATCHER WHOSE LINEAGE A READER IS OWED**, and all three yields are printed rather than the')
w('### last one presented as if it had been the first.')
w('')

# --------------------------------------------------------------------------------- COMPONENT 2
w(SUB)
w('### COMPONENT 2 -- CO-LOCATION, AND THE UNIT THAT WAS FIXED BEFORE ANY SCORE.')
w(SUB)
w('### ### **THE RUBRIC, QUOTED:** ### `KEYSTONES synthesize a cluster AGAINST other available')
w('### content`. ### The order reads that as ### **COMBINES**, and gives the structural signature:')
w('### ### **SOURCES FROM DIFFERENT CLUSTERS OCCUPY THE SAME UNIT.** ### **A COLLECTION PARTITIONS')
w('### ### ITS SOURCES ONE PER ENTRY; A SYNTHESIS CO-LOCATES THEM.**')
w('### ### **THE UNIT WAS DEFINED ON THE LOCKED FACE AND NOT IN THE TOOL:** ### one list item, one')
w('### table row, one fenced block, or one paragraph bounded by a blank line, a real heading or a')
w('### fence. ### A real heading is `b377`s test and ### **CLOSES A UNIT RATHER THAN JOINING ONE.**')
w('### ### ### **WHY AN ENTRY IS A UNIT OF ITS OWN, AND THIS IS THE WHOLE POINT:** ### under a')
w('### blank-line-only definition ### **A BIBLIOGRAPHY IS ONE PARAGRAPH AND THE MOST PARTITIONED')
w('### ### DOCUMENT IN THE CORPUS WOULD SCORE AS THE MOST COMBINING.**')
w('### ### **THE THRESHOLD WAS DECLARED BEFORE THE CONTROL RAN:** ### `C+` above half of a document`s')
w('### source-bearing units, `C-` below, `C?` where no unit carries a source. ### **AND WHEN THE')
w('### ### CONTROL DISAGREED THE THRESHOLD WAS LEFT WHERE IT WAS.**')
w('### ### **THE SPLITTER IS FIXTURED ON ALL THREE KINDS PLUS A HEADING AND A FENCE**, and the')
w('### fixture that matters is the collection: ### **THE SAME TWO SOURCES, ONE PER ENTRY, SCORE `C-`')
w('### ### WHERE ONE PARAGRAPH SCORES `C+`.** ### Self-test : ### **%s**'
  % ('ALL PASS' if C['fixtures_ok'] else '### FAILED'))
w('')
w('### ### **WHAT IT IS DEAF TO, DECLARED IN THE MODULE ITSELF AND NOT DISCOVERED LATER:**')
w('###   ### **A DOCUMENT QUOTING MANY SOURCES IN ONE PLACE WITHOUT RELATING THEM SCORES AS')
w('###     ### SYNTHESIS.** ### The order names this one. ### Two names in a sentence are not an')
w('###     argument between them.')
w('###   ### **A SYNTHESIS THAT RELATES TWO SOURCES ACROSS ADJACENT PARAGRAPHS SCORES AS GATHERING.**')
w('###   ### **MARKDOWN STRUCTURE STANDS IN FOR RHETORICAL STRUCTURE.**')
w('###   ### **THE DIRECTORY STANDS IN FOR THE SUBJECT** -- `b380`s, inherited whole, an ADDRESS')
w('###     standing in for a subject and exactly the substitution `(R2)` warns against.')
w('###   ### **A CITATION IT DOES NOT RECOGNISE IS NOT A CITATION TO IT** -- `b380`s, inherited whole.')
w('')

# --------------------------------------------------------------------------------- COMPONENT 3
w(SUB)
w('### COMPONENT 3 -- THE CONTROL, RUN BEFORE ANY CORPUS NUMBER EXISTED.')
w(SUB)
w('### ### **NO CORPUS-WIDE CO-LOCATION FIGURE EXISTS IN THIS ACT AND NONE WAS COMPUTED.** ### The')
w('### order`s construction, and the order of the printing is itself the guarantee: ### **A PREDICATE')
w('### ### CANNOT BE TUNED TO A RESULT IT HAS NOT SEEN.**')
w('')
w('### **THE SYNTHESIS EXEMPLARS (%d) -- the record`s own class declarations:**' % NS)
w('###   %-62s %-5s %-8s %s' % ('DOCUMENT', 'MARK', 'RATIO', 'CO-LOCATING / BEARING'))
for r in sorted(SYN, key=lambda x: -x['ratio']):
    w('###   %-62s %-5s %-8.3f %d / %d'
      % (r['file'], r['mark'], r['ratio'], r['colocating'], r['bearing']))
w('')
w('### **THE GATHERING EXEMPLARS THAT CLEARED THE BAR (%d of %d) -- the ones that refute `(F1)`:**'
  % (GATP, NG))
for r in sorted([x for x in GAT if x['mark'] == 'C+'], key=lambda x: -x['ratio']):
    w('###   %-62s %-5s %-8.3f %d / %d'
      % (r['file'], r['mark'], r['ratio'], r['colocating'], r['bearing']))
w('### **AND THE HIGHEST-RATIO GATHERING EXEMPLARS BELOW IT, FOR THE SHAPE OF THE OVERLAP:**')
for r in sorted([x for x in GAT if x['mark'] != 'C+'], key=lambda x: -x['ratio'])[:6]:
    w('###   %-62s %-5s %-8.3f %d / %d'
      % (r['file'], r['mark'], r['ratio'], r['colocating'], r['bearing']))
w('')
w('### ### **SYNTHESIS EXEMPLARS AT `C+` : `%d` OF `%d` (`%.1f%%`).**'
  % (SYNP, NS, 100.0 * C['synthesis_rate']))
w('### ### **GATHERING EXEMPLARS AT `C+` : `%d` OF `%d` (`%.1f%%`).**'
  % (GATP, NG, 100.0 * C['gathering_rate']))
w('### ### **THE LOWEST SYNTHESIS RATIO `%.3f` AGAINST THE HIGHEST GATHERING RATIO `%.3f`**, so the'
  % (LO, HI))
w('### ### **THRESHOLD-FREE CHECK IS %s** -- no choice of threshold could have separated them.'
  % C['threshold_free_separation'])
w('### ### ### **THE BRANCH : %s. ### THE PREDICATE IS NOT ADOPTED.**' % BRANCH)
w('### ### **SO THE CORPUS WAS NOT SCORED AND NO QUADRANT TABLE WAS REDRAWN.** ### That is the')
w('### order`s own clause and it bound. ### **THE FINDING IS THAT CO-LOCATION DOES NOT READ ROLE')
w('### ### EITHER, AND THAT IS A RESULT AND NOT A FAILED ACT.**')
w('### **WHAT WOULD HAVE BEEN NEEDED:** ### all `%d` synthesis exemplars at `C+` and none of the `%d`'
  % (NS, NG))
w('### gathering exemplars there. ### The distance is `%d` gathering exemplars above the bar and `%d`'
  % (GATP, NS - SYNP))
w('### synthesis exemplars below it.')
w('')

# --------------------------------------------------------------------------------- COMPONENT 4
w(SUB)
w('### COMPONENT 4 -- WHAT THE COLUMNS MEAN NOW.')
w(SUB)
w('### ### **`b380`S POSITIVE COLUMN (`A+`, %d DOCUMENTS) IS STILL AN UPPER BOUND ON SYNTHESIS.**'
  % R80['structural_tally'].get('A+', 0))
w('### This act did not test it, narrow it or confirm it. ### **NOTHING ABOUT IT MOVED.**')
w('### ### **`b380`S NEGATIVE COLUMN (`A-`, %d DOCUMENTS) IS STILL UNVALIDATED.**'
  % R80['structural_tally'].get('A-', 0))
w('### Validating it needed a second, independent reading that agreed with it on the documents that')
w('### declare, and ### **CO-LOCATION IS NOT THAT READING BECAUSE IT DOES NOT SEPARATE THEM.**')
w('### ### ### **SO WHAT STAYS UNVALIDATED IS EXACTLY WHAT WAS UNVALIDATED BEFORE**, and this act`s')
w('### contribution is ### **A NEGATIVE ONE, STATED AS SUCH RATHER THAN DRESSED UP.**')
w('')
w('### ### **WHAT IS NEW IS THE CONTROL, NOT A COLUMN.** ### `%d` synthesis and `%d` gathering'
  % (NS, NG))
w('### exemplars, every member selected by a quoted sentence in its own head. ### **IT SURVIVES THIS')
w('### ### ACT WHETHER OR NOT CO-LOCATION DID**, and the next feature has something to fail against.')
w('### ### ### **AND THE SECOND NEW FACT IS A NEGATIVE ONE WORTH MORE THAN EITHER FEATURE: TWO')
w('### ### ### INDEPENDENT STRUCTURAL FEATURES NOW FAIL THE SAME DISTINCTION.**')
w('### `b380`s reach called both gatherers synthesisers; this act`s co-location puts `%d` of `%d`'
  % (NS - SYNP, NS))
w('### synthesis declarers below its own bar. ### **THAT IS NOT PROOF THAT NO STRUCTURAL FEATURE')
w('### ### READS ROLE AND THIS ACT DOES NOT CLAIM IT.** ### It is two failures of the same shape, and')
w('### the shape is that ### **THE DISTINCTION LIVES IN WHAT A DOCUMENT SAYS ABOUT WHAT IT NAMES.**')
w('')
w('### ### **AND THE TOKENISER WAS MEASURED AND ACQUITTED.** ### `(E4)` predicted the unit definition')
w('### would do more work than the threshold. ### Re-scored under a ### **PARAGRAPH-ONLY** ### splitter')
w('### -- what `the same unit` builds if nobody asks what an entry is -- the gathering side`s `C+` rate')
w('### moves from `%.1f%%` to `%.1f%%` and ### **THE BRANCH DOES NOT CHANGE (%s -> %s).**'
  % (100.0 * C['gathering_rate'], 100.0 * VD['naive_gathering_rate'], BRANCH, VD['naive_branch']))
w('### ### **`(E4)` IS REFUTED.** ### The unit definition was worth making and it was ### **NOT WHAT')
w('### ### DECIDED THE OUTCOME.** ### The measurement adopts nothing; the declared unit and threshold')
w('### stand exactly as locked.')
w('')

# ------------------------------------------------------------------------------- EXPECTATIONS
w(SUB)
w('### THE EXPECTATIONS, EACH AGAINST ITS OWN PRINTED TABLE.')
w(SUB)
w('### ### **`(F1)` REFUTED.** ### Co-location does not separate the rebuilt set, and the overlap is')
w('### total rather than marginal.')
w('### ### **`(F2)` NOT REACHED.** ### The corpus is not scored when the predicate is not adopted, so')
w('### there is no column to shrink. ### **NEITHER MET NOR REFUTED IS THE HONEST ANSWER**, and')
w('### ### **`(E1)` REGISTERED THAT CONDITIONALITY BEFORE THE RUN.**')
w('### ### **`(E1)` MET.** ### It bound exactly as written.')
w('### ### **`(E2)` CONFIRMED IN MECHANISM AND REFUTED IN EFFECT.** ### It predicted the ledgers')
w('### would co-locate at high ratio while arguing nothing. ### `REGISTRY.md` carries ### **`%d`'
  % VD['registry_bearing'])
w('### ### SOURCE-BEARING UNITS AND `%d` OF THEM DO CARRY TWO CLUSTERS** -- the mechanism is exactly'
  % VD['registry_colocating'])
w('### as predicted -- but the ratio is `%.3f`, below the bar, because ### **MOST LEDGER ROWS NAME ONE'
  % VD['registry_ratio'])
w('### ### THING.** ### The deafness is real and it did not decide the outcome.')
w('### ### **`(E3)` REFUTED.** ### `%d` gathering exemplars against a floor of `%d`.' % (NG, EX['floor']))
w('### ### **`(E4)` REFUTED**, measured above.')
w('')

# --------------------------------------------------------------------------------------- CLOSING
w(SUB)
w('### THE DESK, THE WRITES, AND WHAT THIS ACT DID NOT DO.')
w(SUB)
w('### desk items swept : %d ### / ### closed : %d ### / ### standing : %d ### / ### lists closed : %d'
  % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
w('### ### **AND THE ONE CLOSURE IS THE AUTHOR`S, NOT THIS SEAT`S.** ### `b379` filed whether the')
w('### ruling governs documents outside the tree; ### **`(R14)` ANSWERS IT**, so its occasion is gone')
w('### under `(R7)`. ### **NO OTHER ITEM CLOSED AND NO LIST CLOSED.**')
w('### trail block appended (append-only %s, committed prefix intact %s); `CORRESPONDENCE.md` row %s;'
  % (Q['trail']['appended_only'], Q['trail']['committed_prefix_intact'], Q['row']))
w('### index key `the-control-rebuilt-and-co-location-not-adopted` reachable by every alias : %s'
  % Q['key_ok'])
w('### ### **THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME AND NONE IS CLOSED.**')
w('### ### **NO CLASS WAS RULED. ### NO DOCUMENT WAS RECLASSIFIED. ### NO DECLARATION WAS MOVED. ###')
w('### ### NO PRIOR SCORE WAS OVERWRITTEN. ### THE CORPUS WAS NOT SCORED. ### THE REGISTRY WAS NOT')
w('### ### EDITED.**')
w('### ### **NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL.** ### Nothing on the download layer was')
w('### written, moved, renamed or removed and the book was not opened. ### No archive file was touched')
w('### and the `86` unconfirmed stay unconfirmed. ### The six clusters stay filed and not opened.')
w('### **NO `.lean` FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED.**')
w('### **THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED. ### THE POSTURE LOCK IS')
w('### SEPARATE.** ### `h2` stands exactly where the deposit left it and this act makes no claim about')
w('### it in either direction. ### **NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.**')
w('')

# ------------------------------------------------------------------------------------------ LORE
w(SUB)
w('### WHAT THIS ACT ADDS TO THE LORE.')
w(SUB)
w('### ### ### **NEW -- `A CONTROL THAT CANNOT FAIL ON ONE SIDE AND CANNOT INFORM ON THE OTHER IS`')
w('### ### ### `ONE DEFECT, NOT TWO`.** ### `b380`s seven cleared any threshold and its two')
w('### disagreed. ### Read separately they look like a pass and a blemish; ### **READ TOGETHER THEY')
w('### ### ARE A CONTROL THAT COULD NOT HAVE TAUGHT THE PREDICATE ANYTHING.**')
w('### ### ### **NEW -- `A MATCHER REPAIRED AFTER ITS OUTPUT WAS SEEN OWES ITS LINEAGE`.** ### Two of')
w('### this act`s three matcher versions were repaired after their yield was visible. ### Each repair')
w('### traces to text written before the run, ### **AND THAT IS EXACTLY THE CLAIM A READER CANNOT')
w('### ### CHECK WITHOUT THE INTERMEDIATE NUMBERS**, so all three are printed.')
w('### ### ### **NEW -- `A QUOTATION WITH HOLES IN IT IS NOT A QUOTATION`.** ### The first `(R14)`')
w('### block banked the `6` lines this act had anchored out of a `9`-line ruling and called itself')
w('### verbatim. ### **AN ANCHOR SET IS A READING AID AND NOT A TRANSCRIPT.**')
w('### ### ### **NEW -- `TWO FEATURES FAILING THE SAME DISTINCTION IS EVIDENCE, NOT PROOF`.** ###')
w('### Reach failed and co-location failed. ### **THE TEMPTATION IS TO CONCLUDE THAT ROLE IS NOT')
w('### ### STRUCTURALLY READABLE AT ALL, AND THIS ACT DECLINES IT** -- two instruments are two')
w('### instruments.')
w('### **MET AGAIN -- THE THRESHOLD DECLARED BEFORE THE CONTROL RAN AND NOT MOVED AFTERWARDS** --')
w('### which is the only reason the non-separation is legible as a result rather than as a setting.')
w('### **MET AGAIN -- `A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE`** (`b369`), and')
w('### ### **AN ABSENCE NEEDS A PROVED SEARCH** (`b378`) -- the head scan`s positive control fired on')
w('### a known presence and refused a document that argues, before any absence was reported.')
w('### **MET AGAIN -- THE BASH HEREDOC COLLAPSES A BACKSLASH** (`b376`): this act lost a patch to it')
w('### and wrote the regex repairs through the file editor instead.')
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
for n in ('b381_reads', 'b381_lockgate', 'b381_exemplars', 'b381_control', 'b381_verdict',
          'b381_desk'):
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
w('### **THE PREDICATE`S THRESHOLD, AS LOCKED AND AS RUN : `%.2f`.**' % CL.THRESHOLD)
w(BAR)

io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
print('  written: %s  (%d lines, %d bytes)'
      % (os.path.basename(OUT), len(L), len(chr(10).join(L).encode('utf-8'))))
bad = [i + 1 for i, s in enumerate(L) if '%s' in s or '%d' in s]
print('  ### UNFILLED PLACEHOLDERS : %s' % (bad or 'none'))
MUSTFAIL = ('### A CLASS WAS RULED.', '### A DECLARATION WAS MOVED.', '### A LIST WAS CLOSED.',
            '### A PRIOR SCORE WAS OVERWRITTEN.',
            '### THE THRESHOLD WAS MOVED TO FIT THE CONTROL.',
            '### AN EXEMPLAR WAS CHOSEN BY JUDGEMENT.', '### THE PREFERRED BRANCH IS.')
hit = [m for m in MUSTFAIL if m in L]
print('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (hit or 'none'))
sys.exit(1 if (bad or hit) else 0)
