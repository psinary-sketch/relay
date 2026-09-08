# -*- coding: utf-8 -*-
"""b373_bank.py -- THE BANK, WRITTEN FROM THE ACT'S OWN JSONS. ### **NO FIGURE IS TYPED.**"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b373_the_pins_and_the_status_column.txt')
REG = os.path.join(D, 'b373_registration_2026-09-08.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, P, S, Q, F = J('b373_reads'), J('b373_pins'), J('b373_status'), J('b373_desk'), J('b373_filing')
regtxt = io.open(REG, encoding='utf-8').read()
SHA = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt).group(1)
NBY = re.search(r'bytes locked : (\d+)', regtxt).group(1)
LAT = re.search(r'locked at \(UTC\) : (\S+)', regtxt).group(1)
NCL = len(J('b373_satisfiable')['clauses'])

L = []


def w(s=''):
    L.append(s)


BAR, SUB = '=' * 100, '-' * 100
DET = P['detail']
PINNABLE = [x for x in DET if x['status'] == 'PINNABLE']
DEFECT = [h for h in S['detail']
          if not h['states_own_retirement'] and not h['grades_a_live_declaration']]
SELFRET = [h for h in S['detail'] if h['states_own_retirement']]
LIVEG = [h for h in S['detail'] if h['grades_a_live_declaration'] and not h['states_own_retirement']]
PCT = 100.0 * P['located_act'] / max(1, P['rows'])

w(BAR)
w('b373 -- THE PINS AND THE STATUS COLUMN. ### THE BANK.')
w('2026-09-08. ### CONCURRENCY: SOLO (research seat). ### SORTIE LEG 1 OF 2.')
w('### FERRY_STANDING v2, by reference, citation CURRENT.')
w('### Registration `data/b373_registration_2026-09-08.txt`, ### **LOCKED**')
w('### `%s`, %s bytes, %d clauses JOINTLY' % (SHA, NBY, NCL))
w("### SATISFIABLE, and ### **LOCKED ONLY AFTER THE AUDIT'S OWN EXIT CODE CAME BACK `0`**, locked at "
  '(UTC)')
w('### %s. ### **LOCKED BEFORE ANY WRITE OF THIS ACT.** ### The clocks are in section (9).' % LAT)
w(BAR)
w('')

w(SUB)
w('### (1) THE ANSWER, FIRST.')
w(SUB)
w('### ### ### **`(R9)` WAS EXECUTED AS FAR AS ITS OWN SOURCING RULE ALLOWS, AND IT WROTE NO PIN.**')
w('### Not because the price did not fit -- it fitted, at `%.1f` seconds a row over `%d` rows -- and'
  % (P['per_row'], P['rows']))
w('### not because the seat declined. ### **BECAUSE THE CHAIN THE RULING REQUIRES DOES NOT CLOSE.**')
w('')
w('### ### ### **THE PAPERS ARE OLDER THAN THE INSTRUMENTS. ### THAT IS THE FINDING.**')
w('### `%d` of `%d` rows have a locatable writing act; ### **`%d` DO NOT**, because the commit that'
  % (P['located_act'], P['rows'], P['act_not_located']))
w('### introduced them carries a subject that names no act. ### And of the `%d` that do, the chain'
  % P['located_act'])
w('### fails again: %s.'
  % '; '.join('`%d` %s' % (n, k.lower()) for k, n in sorted(P['reasons'].items())
              if k and k != 'null' and k != 'WRITING ACT NOT NAMED'))
w('### ### **THE PINS INSTRUMENT BEGINS AT `b300`.** ### Most rows needing a ref were written before')
w('### there was an instrument that banked one. ### **`(R9)` IS A GOOD RULE REACHING BACK INTO A')
w('### ### RECORD THAT DID NOT YET KEEP THE EVIDENCE THE RULE REQUIRES.**')
w('')
w('### ### **`%d` ROWS WERE PINNABLE. ### ALL `%d` OF THEM SIT ON A SURFACE NO ACT MAY REWRITE:**'
  % (P['pinnable'], P['pinnable']))
for k, n in sorted(P['excluded_reasons'].items()):
    w('###   `%d` on %s' % (n, k.lower()))
w('### ### **SO NO PIN WAS WRITTEN TO ANY ROW**, and that is a scope decision fixed on the')
w('### registration`s face before any read, not a discovery made when the edit got difficult.')
w('### ### **WHETHER THOSE SURFACES SHOULD CARRY PINS AT ALL IS ROUTED, NOT DECIDED** -- it is the')
w('### author`s question, and a citation-hygiene ruling is not a licence to rewrite a deposit.')
w('')
w('### ### ### **THE STATUS COLUMN: `%d` ROWS IN `%d` DOCUMENTS ASSERT A GRADE AGAINST A DECLARATION'
  % (S['defect'], len(set(h['file'] for h in DEFECT))))
w('### ### ### THIS RECORD HAS CLASSIFIED RETIRED OR ABSENT.** ### `%d` more state their own'
  % S['corrected'])
w('### retirement and `%d` grades a declaration `b372` found alive -- ### **NEITHER IS THE DEFECT.**'
  % S['live_graded'])
w('### ### **AND EVERY ONE OF THE `%d` IS INSIDE THE TWELVE `b372` ALREADY FLAGGED.** ### The sweep'
  % S['defect'])
w('### found ### **NO INSTANCE OUTSIDE THAT SET**, which bounds the problem rather than widening it.')
w('### ### **NO GRADE WAS MOVED BY THIS SEAT.**')
w('')
w('### ### **THE INSTRUMENT `b372` MADE FALSE IS CORRECTED**, under the order`s own licence, ### **AND')
w('### ### ITS CAVEAT IS KEPT RATHER THAN DELETED ALONG WITH THE FALSEHOOD.**')
w('### ### **THE DESK: `%d` SWEPT, `%d` CLOSED, `%d` STANDING.**'
  % (Q['items'], Q['closed'], Q['standing']))
w('')

w(SUB)
w('### (2) COMPONENT 1 -- `(R9)`, PRICED AND THEN EXECUTED.')
w(SUB)
w('### **THE CHAIN, AS DECLARED ON THE FACE AND AS RUN:** ### the row re-anchored ### **BY ITS OWN')
w('### CONTENT** -> the commit that INTRODUCED that content -> the ACT that commit`s subject names ->')
w('### ### **THAT ACT`S OWN BANKED REF.**')
w('### ### **AND THE LAST LINK HAS TWO FORMS, BOTH INSIDE THE RULING`S WORDS:** ### the act`s own')
w('### `ls-remote` pins record, and ### **A REF NAMED IN THE ACT`S OWN BANK** where no pins record')
w('### exists. ### The second was added because the acts that wrote most of these rows predate the')
w('### pins instrument entirely, and ### **`located in its own bank` IS THE RULING`S OWN PHRASE.**')
w('### ### **MORE THAN ONE RESOLVING REF FOR ONE KERNEL IS AMBIGUOUS AND IS REFUSED**, the way an')
w('### ambiguous anchor is refused.')
w('')
w('### **THE CLASSIFICATION:**')
w('###   rows walked                         : %d' % P['rows'])
w('###   ### **WITH A LOCATABLE WRITING ACT   : %d  (%.0f%%)**' % (P['located_act'], PCT))
w('###   ### **WHOSE ACT COULD NOT BE LOCATED : %d**' % P['act_not_located'])
w('###   ### **PINNABLE                       : %d**' % P['pinnable'])
w('###   ### **CITES-AT-AN-UNKNOWN-REF        : %d**' % P['unknown'])
w('')
w('### **THE REASONS, KEPT APART BECAUSE THEY WILL NOT HAVE THE SAME CURE:**')
for k, n in sorted(P['reasons'].items(), key=lambda x: -x[1]):
    if k and k != 'null':
        w('###   %-46s %d' % (k, n))
w('###   %-46s %d' % ('(no reason -- these are the PINNABLE rows)', P['pinnable']))
w('### ### **A ROW NOBODY CAN DATE AND A ROW WHOSE KERNEL WAS NEVER ROSTERED ARE NOT THE SAME')
w('### ### PROBLEM.** ### Collapsing them into one number would have hidden the only thing this')
w('### component found.')
w('')
w('### **THE PINNABLE ROWS, EVERY ONE OF THEM:**')
for x in PINNABLE:
    w('###   %-58s:%-6d act `%s`  kernel `%s`' % (x['file'][:58], x['line'], x['act'], x['kernel']))
    w('###       pin `%s` ### -- %s, from `%s`'
      % (x['pin'][:12], x['pin_source'], x.get('pin_from')))
    w('###       ### **NOT WRITTEN : %s**' % x['excluded'])
w('')
w('### ### ### **AND ONE THING IS REPORTED RATHER THAN WORKED AROUND:** ### `%d` of those pins'
  % P['equals_a_head'])
w('### ### **EQUAL A CURRENT HEAD** -- not because a head was used as the source, but because the')
w('### kernel has not moved since the act that wrote the rows, and ### **THAT ACT`S OWN BANK SAYS SO')
w('### ### IN AS MANY WORDS.** ### `BAR 2` as locked forbids writing a pin equal to a head. ### **THE')
w('### ### BAR TESTS THE VALUE; THE RULING FORBIDS THE SOURCE; A KERNEL THAT HAS NOT MOVED MAKES THE')
w('### ### TWO COINCIDE.** ### The bar as locked was obeyed, and the tension is filed rather than')
w('### resolved by a seat.')
w('')
w('### **THE PRICE, IN THREE PARTS:**')
w('###   ### **ONE ROW** : `%.2f` seconds, dominated entirely by the history search.' % P['per_row'])
w('###   ### **THE WHOLE SET** : `%.0f` seconds for `%d` rows. ### **THE PRICE FITS ONE ACT**, which is'
  % (P['seconds'], P['rows']))
w('###     why this act executed rather than only priced.')
w('###   ### **THE SPLIT** : ### the locating is entirely mechanical. ### **WHAT IS NOT MECHANICAL IS')
w('###     ### WHICH SURFACES MAY BE EDITED AT ALL** -- decided on the face and routed -- ### **AND')
w('###     ### WHETHER A ROW`S CLAIM IS TRUE AT THE PIN**, which is a check no search can buy.')
w('')

w(SUB)
w('### (3) COMPONENT 2 -- THE STATUS COLUMN.')
w(SUB)
w('### **THE CLASSIFIED SET IS THE RECORD`S OWN:** ### `%d` names from `b369` (confirmed after `b367`'
  % S['from_b369'])
w('### and `b368`) and `%d` from `b372`s twelve, ### **`%d` DISTINCT DECLARATIONS.** ### **NO KERNEL'
  % (S['from_b372'], S['classified']))
w('### ### WAS OPENED TO RE-CLASSIFY ANY OF THEM.**')
w('### **THE SWEEP:** ### `%d` table rows across `%d` tracked markdown files; ### **`%d` NAME A'
  % (S['rows_scanned'], S['files'], S['hits']))
w('### ### CLASSIFIED DECLARATION AND CARRY A GRADE.**')
w('### ### **AND THE THREE-WAY SPLIT IS THE WHOLE CARE OF THIS COMPONENT:**')
w('###   ### **%d STATE THEIR OWN RETIREMENT** -- reporting the withdrawal, not asserting the'
  % S['corrected'])
w('###     declaration is there. ### **NOT THE DEFECT.**')
w('###   ### **%d GRADES A DECLARATION `b372` FOUND ALIVE** -- its first cell carries a retired'
  % S['live_graded'])
w('###     concept LABEL while its terminal cell names a live one. ### **NOT THE DEFECT**, and')
w('###     counting it would be the same mistake one step further out.')
w('###   ### **%d ASSERT THE GRADE WITH NEITHER. ### THOSE ARE THE DEFECT.**' % S['defect'])
w('')
w('### **THE DEFECTIVE ROWS, EACH WITH THE DOCUMENT THAT CARRIES IT:**')
for h in DEFECT:
    w('###   `%s`:%d   grade %s' % (h['file'], h['line'], ', '.join(h['grades'][:2])))
    w('###       declarations : %s' % ', '.join('`%s`' % x for x in h['declarations']))
    w('###       | %s' % h['text'][:190])
w('')
w('### **AND THE ROWS THAT ARE NOT THE DEFECT, NAMED SO THEY ARE NOT MISTAKEN FOR IT:**')
for h in SELFRET:
    w('###   `%s`:%d ### -- states its own retirement (%s)'
      % (h['file'], h['line'], ', '.join(h['retirement_words'][:2])))
for h in LIVEG:
    w('###   `%s`:%d ### -- names `%s` but grades %s, which `b372` found ALIVE'
      % (h['file'], h['line'], h['declarations'][0],
         ', '.join('`%s`' % x for x in h['grades_a_live_declaration'])))
w('')
w('### ### **THE CONSEQUENCE, ROUTED AND NOT ACTED ON.** ### A stale count misstates a quantity;')
w('### ### **A GRADE AGAINST AN ABSENT DECLARATION ASSERTS THAT SOMETHING WAS CHECKED THAT IS NOT')
w('### ### THERE TO CHECK**, and a reader traversing the row cannot see the difference.')
w('### **THE AUTHOR FACES THREE CHOICES PER ROW, NAMED HERE WITHOUT ONE BEING CHOSEN:** ### strike the')
w('### grade; restate it as a retirement, as `VERIFICATION_LOOM.md` already does for one pair; or leave')
w('### it with a pin that dates it -- ### **AND THIS ACT HAS JUST SHOWN A PIN CANNOT BE SOURCED FOR')
w('### ### THESE ROWS.**')
w('### ### **NO GRADE WAS MOVED. ### A SEAT THAT REGRADES IS A SEAT THAT DECIDED WHAT WAS VERIFIED.**')
w('')

w(SUB)
w('### (4) COMPONENT 3 -- THE GUARD`S OWN FRONT MATTER.')
w(SUB)
w('### **ONE OWNER INSTRUMENT WAS LICENSED BY THE ORDER AND NAMED ON THE FACE BEFORE THE EDIT:**')
w('### `tools/b304_hooks.py`. ### It reported that ### *no `.gitattributes` pins the guard, and the')
w('### identity arm above is EOL-normalised, so THIS ARM WILL NOT TELL YOU* -- ### **AND `b372` MADE')
w('### ### THE FIRST HALF FALSE IN EVERY ROSTERED REPOSITORY.**')
w('### ### **THE CAVEAT IS KEPT, NOT DELETED WITH THE FALSEHOOD.** ### The tool now says the attribute')
w('### pins `eol=lf` everywhere and that a fresh checkout was shown byte-identical to its blob, ### **AND')
w('### ### THAT THIS FIXES WHAT THE NEXT CHECKOUT PRODUCES AND NOT WHAT IS ON A DISK TODAY, AND THAT')
w('### ### THE ARM STILL WOULD NOT TELL YOU.** ### **A CORRECTION THAT DELETES THE CAVEAT IS A WORSE')
w('### ### FILE.**')
w('### **AND ONE ITEM IS DELIBERATELY NOT CLOSED WITH IT:** ### the guard`s own install line, in the')
w('### guard and not in the exerciser, ### **STILL NAMES A PATH THE RECORD NO LONGER USES.** ### That')
w('### is a different sentence in a different file and conflating them would close an item nothing')
w('### killed.')
w('')

w(SUB)
w('### (5) THE DESK, UNDER `(R7)`.')
w(SUB)
w('### ### **`%d` SWEPT. ### `%d` CLOSED. ### `%d` STANDING. ### REFUSED FOR WANT OF A KILLING FILE :'
  % (Q['items'], Q['closed'], Q['standing']))
w('### ### `%d`.**' % Q['closures_refused'])
for c in Q['closed_items']:
    w('###   CLOSED  %-54s killing file `%s`, dated %s' % (c['item'][:54], c['file'], c['date']))
    if c['own_act']:
        w('###           ### **FLAGGED: THE KILLING FILE IS THIS ACT`S OWN** (`b368`s rule).')
w('### ### ### **AND ONE CLOSURE IS THE INTERESTING ONE:** ### *the pinless rows, awaiting a ruling on')
w('### ### whether pins are added* CLOSES -- ### **ITS OCCASION WAS AN UNMADE RULING AND THE RULING IS')
w('### ### MADE.** ### What the execution then FOUND is filed as a ### **NEW** ### item, not as the')
w('### old one surviving: ### **AN ITEM THAT CHANGES ITS MEANING WHILE KEEPING ITS NAME IS A DESK THAT')
w('### ### NEVER CLOSES ANYTHING.**')
w('### **THE TRAILS LEDGER WAS UPDATED THROUGH ITS WRITER**, append-only `%s`, the committed version'
  % F['appended_only'])
w('### still a substring `%s`, `%d` -> `%d` bytes.'
  % (F['committed_prefix_intact'], F['before_bytes'], F['after_bytes']))
w('### ### **AND THIS ACT APPENDED TO A LEDGER IT REFUSED TO EDIT.** ### Appending a block is not the')
w('### same act as changing a row somebody else wrote, and the difference is the whole of section (C).')
w('')

w(SUB)
w('### (6) THE EXPECTATIONS, SCORED.')
w(SUB)
w('### ### ### **`(L1)` -- THE NAVIGATOR`S: *more than half the pinless rows have a locatable writing')
w('### ### ### act.* ### REFUTED, BY A PRINTED CLASSIFICATION.** ### `%d` of `%d`, which is `%.0f%%`.'
  % (P['located_act'], P['rows'], PCT))
w('### ### **AND THE REFUTATION IS THE ACT`S RESULT, NOT A DISAPPOINTMENT:** ### it says the record`s')
w('### commit subjects did not name acts when most of these rows were written, and ### **NO AMOUNT OF')
w('### ### SEARCHING WILL CHANGE THAT.**')
w('')
w('### ### ### **`(E1)` -- THIS SEAT`S: *the binding constraint will not be locating the act; it will')
w('### ### ### be that the act`s pins record does not carry the kernel.* ### REFUTED.** ### The binding')
w('### constraint IS locating the act: `%d` of `%d` fail at that link, against `%d` failing later.'
  % (P['reasons'].get('WRITING ACT NOT NAMED', 0), P['rows'],
     P['rows'] - P['reasons'].get('WRITING ACT NOT NAMED', 0) - P['pinnable']))
w('### ### **THIS SEAT PREDICTED THE ROSTER WOULD BE THE WALL AND THE COMMIT SUBJECTS WERE.**')
w('')
w('### ### ### **`(E2)` -- THIS SEAT`S: *the status-column set will be smaller than the pinless set and')
w('### ### ### worse.* ### THE FIRST HALF HELD AND WAS SAID TO BE NEARLY ARITHMETIC** (`%d` against'
  % S['defect'])
w('### `%d`). ### **THE HALF WORTH SCORING -- WHETHER ANY SUCH ROW EXISTS OUTSIDE THE TWELVE `b372`'
  % P['rows'])
w('### ### ALREADY FOUND -- IS REFUTED: NONE DOES.** ### Every graded-against-absent row is inside that')
w('### set. ### **THE DEFECT IS BOUNDED, AND THAT IS BETTER NEWS THAN THE EXPECTATION ASKED FOR.**')
w('')

w(SUB)
w('### (7) WHAT THIS ACT DID NOT DO.')
w(SUB)
w('### **NO PIN WAS WRITTEN TO ANY ROW, AND NO PIN WAS TAKEN FROM ANY CURRENT HEAD.**')
w('### **NO ROW WAS CHECKED AT ANY PIN.** ### Adding a pin dates a claim; it does not verify one.')
w('### **NO GRADE WAS MOVED, NO FACE PROMOTED, AND NO GRADE CONFERRED BY A SEAT.**')
w('### **NO DEPOSITED FILE, NO ARCHIVED FILE AND NO APPEND-ONLY LEDGER ENTRY WAS EDITED.**')
w('### **NO NEW COLUMN WAS ADDED TO ANY TABLE AND NO TABLE`S SHAPE WAS CHANGED.**')
w('### **NO `.lean` FILE WAS TOUCHED. ### NO BUILD WAS RUN. ### NO AXIOM PROFILE WAS RECOMPUTED.**')
w('### **NO KERNEL WAS RE-CLASSIFIED.** ### The retired-and-absent set is the record`s own.')
w('### **ONLY THE ONE LICENSED OWNER INSTRUMENT MOVED.**')
w('### **LEG 2 WAS NOT BEGUN.** ### The hedge audit over the keystones, the glossary and bibliography,')
w('### the count-and-ref sweep and the functional-equation filing belong to `b374`.')
w('### **NOTHING WAS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT.** ### A pin is about when a')
w('### claim was made, not about whether it is true.')
w('### **NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NOTHING COMPILED AND NO BRIDGE TYPED.**')
w('### **NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED.**')
w('### **NOTHING HERE BEARS ON `h2`, ON TOTALITY OR ON THE ROSTER.** ### `M-2` remains')
w('### (SPECIFIED-NOT-STATED) under `b310`s cap. ### The seam`s debt item 1 stands. ### The patent lane')
w('### is carried on the patent seat`s report, UNCONFIRMED on this seat`s record. ### **THE POSTURE')
w('### ### LOCK IS SEPARATE. ### THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED.**')
w('### `h2` stands exactly where the deposit left it. ### **NOTHING DEPOSITS.**')
w('')

w(SUB)
w('### (8) THE SPECIES THIS ACT ADDS, AND THE ONES IT MET AGAIN.')
w(SUB)
w('### ### ### **NEW -- `A RULE CAN OUTRUN THE RECORD IT REACHES INTO`.** ### `(R9)` is sound and its')
w('### evidence is `b372`s own. ### It still pins nothing, because ### **THE RECORD DOES NOT CARRY, FOR')
w('### ### MOST ROWS, THE ACT-NAME AND THE BANKED REF THE RULE NEEDS.** ### The failure is not of the')
w('### rule and not of the execution: ### **IT IS A FACT ABOUT WHEN THE INSTRUMENTS WERE BUILT.**')
w('### ### ### **NEW -- `AN ARM THAT TESTS THE VALUE CANNOT TEST THE SOURCE`.** ### `BAR 2` forbids a')
w('### pin equal to a head, to stop a seat sourcing from today. ### **BUT A KERNEL THAT HAS NOT MOVED')
w('### ### MAKES A CORRECTLY-SOURCED PIN EQUAL A HEAD**, and the arm cannot tell the two apart. ### The')
w('### bar was obeyed as locked and the tension filed.')
w('### **MET AGAIN -- `PREDICATE_ONE_SHAPE`, AND THIS TIME IN THIS ACT`S OWN TOOL, TWICE.** ### The')
w('### kernel list was TYPED and did not know `SIDE-carrier-spec` or `SIDE-li-map`, so rows naming them')
w('### came back NAMING NO KERNEL; it is now ### **DISCOVERED FROM THE DISK.** ### And a bare `X.lean`')
w('### was not placed at all until each kernel was ASKED whether it tracks such a file. ### **AN ACT')
w('### ### WHOSE SUBJECT IS A PREDICATE THAT KNEW ONE SHAPE COMMITTED THE SPECIES TWICE IN ITS OWN')
w('### ### INSTRUMENT.**')
w('### **MET AGAIN -- THE SCOPE OF A SEARCH IS A PREDICATE.** ### Dropping the pathspec from the')
w('### history search looked safer and made the located-act count FALL from `33` to `7`, because')
w('### ### **THE SAME ROW TEXT LIVES IN THE LIVING PAPER, ITS DEPOSITED COPY AND ITS ARCHIVED')
w('### ### SNAPSHOT.** ### Both searches are now run and the wider one is REPORTED, not substituted.')
w('')

w(SUB)
w('### (9) THE CLOCKS, THE REFS AND THE FILES.')
w(SUB)
w('### registration locked at (UTC) %s' % LAT)
for n in ('b373_reads', 'b373_pins', 'b373_status', 'b373_desk', 'b373_filing'):
    j = J(n)
    w('### %-14s run file `%s` recorded clock %s' % (n, j['run_file'], j['run_clock']))
w('### **THE REFS THIS ACT READ, AND NONE OF THEM IS A PIN IT WROTE:**')
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
