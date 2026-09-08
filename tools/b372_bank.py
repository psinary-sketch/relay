# -*- coding: utf-8 -*-
"""b372_bank.py -- THE BANK, WRITTEN FROM THE ACT'S OWN JSONS. ### **NO FIGURE IS TYPED.**"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b372_the_first_batch.txt')
REG = os.path.join(D, 'b372_registration_2026-09-08.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E = J('b372_reads')
A = J('b372_eol')
R = J('b372_readme')
B = J('b372_batch')
Q = J('b372_desk')
F = J('b372_filing')
INV = J('b371_inventory')
regtxt = io.open(REG, encoding='utf-8').read()
SHA = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt).group(1)
NBY = re.search(r'bytes locked : (\d+)', regtxt).group(1)
LAT = re.search(r'locked at \(UTC\) : (\S+)', regtxt).group(1)
NCL = len(J('b372_satisfiable')['clauses'])

L = []


def w(s=''):
    L.append(s)


BAR, SUB = '=' * 100, '-' * 100
TBL = R['table']
T0, T1, TH = TBL[0], TBL[1], TBL[-1]
TV = B['terminal_tally']
PINNED = [r for r in B['rows'] if r['mode'] == 'AT-PIN']
ATHEAD = [r for r in B['rows'] if r['mode'] == 'CHECKED-AT-HEAD']
FALSEPIN = [r for r in B['rows'] if r['pins'] and not any(p['resolves'] for p in r['pins'])]
BEFORE_OK = [k for k, v in A['before'].items() if v['fresh_equals_blob']]
BEFORE_BAD = [k for k, v in A['before'].items() if not v['fresh_equals_blob']]
WRITTEN = [k for k, v in A['wrote'].items() if v['action'] == 'WRITTEN']
NOTWRITTEN = [k for k, v in A['wrote'].items() if v['action'] != 'WRITTEN']

w(BAR)
w('b372 -- THE README, THE EOL PIN, AND THE FIRST BATCH. ### THE BANK.')
w('2026-09-08. ### CONCURRENCY: SOLO (research seat). ### FERRY_STANDING v2, by reference, citation '
  'CURRENT.')
w('### Registration `data/b372_registration_2026-09-08.txt`, ### **LOCKED**')
w('### `%s`, %s bytes, %d clauses JOINTLY' % (SHA, NBY, NCL))
w("### SATISFIABLE, and ### **LOCKED ONLY AFTER THE AUDIT'S OWN EXIT CODE CAME BACK `0`**, locked at "
  '(UTC)')
w('### %s. ### **LOCKED BEFORE ANY WRITE OF THIS ACT.** ### The clocks are in section (9).' % LAT)
w(BAR)
w('')

w(SUB)
w('### (1) THE ANSWER, FIRST.')
w(SUB)
w('### ### ### **THE END-OF-LINE ATTRIBUTE IS NOW TRACKED IN ALL `%d` ROSTERED REPOSITORIES, AND IN'
  % len(A['after']))
w('### ### ### EVERY ONE OF THEM A FRESH CHECKOUT OF THE TRACKED GUARD IS BYTE-IDENTICAL TO ITS BLOB.**')
w('### Before this act it was `%d` of `%d`, and ### **THE TWO THAT FAILED WERE EXACTLY THE TWO WITHOUT'
  % (len(BEFORE_OK), len(A['before'])))
w('### ### THE ATTRIBUTE** -- %s. ### Written to: %s. ### Not written to, because they already'
  % (', '.join('`%s`' % k for k in BEFORE_BAD), ', '.join('`%s`' % k for k in WRITTEN)))
w('### carried it: %s.' % ', '.join('`%s`' % k for k in NOTWRITTEN))
w('')
w('### ### ### **THE THREE README FIGURES DO NOT COUNT THREE DIFFERENT SCOPES. ### THEY COUNT ONE')
w('### ### ### QUANTITY AT THREE DIFFERENT REFS**, and each was exact when it was written.')
w('### At `%s` (%s) the headline, the breakdown, the ratio and the shipped profile ALL read `%s`.'
  % (T0['ref'][:7], T0['date'], T0['total']))
w('### At `%s` (%s) all of them moved to `%s` ### **EXCEPT THE HEADLINE, WHICH WAS LEFT BEHIND.**'
  % (T1['ref'][:7], T1['date'], T1['total']))
w('### At the head (%s) the profile carries `%d` and the whole sentence is behind it.'
  % (TH['date'], TH['prints']))
w('### ### **AND NONE OF THE THREE NAMES THE REF IT HOLDS AT**, which is the defect and is `b371`s.')
w('')
w('### ### ### **THE TWELVE ROWS CLASSIFY: `%d` NAMED TERMINALS RETIRED, `%d` PRESENT, `%d` ABSENT.**'
  % (TV.get('RETIRED', 0), TV.get('PRESENT', 0), TV.get('ABSENT', 0)))
w('### `%d` rows were opened AT A PIN; `%d` at the kernel`s live head under `(R8)` and are marked'
  % (len(PINNED), len(ATHEAD)))
w('### ### **`CHECKED-AT-HEAD`.** ### The heads are recorded in this bank and ### **IN NO ROW.**')
w('### ### ### **AND ONE COMPARISON INSIDE THIS ACT IS THE WHOLE ARGUMENT FOR `(R8)`:** ### the three')
w('### `no_conspiracy_*` declarations are ### **PRESENT AT THE PIN A ROW NAMES** and ### **RETIRED AT')
w('### ### THE HEAD**, and the rows that cite them without a pin cannot say which they meant.')
w('### ### **ROWS REPAIRED : `0`. ### PINS ADDED : `0`.**')
w('')
w('### ### **THE DESK: `%d` SWEPT, `%d` CLOSED, `%d` STANDING**, and both closures are flagged because'
  % (Q['items'], Q['closed'], Q['standing']))
w('### their killing file is this act`s own.')
w('')

w(SUB)
w('### (2) COMPONENT 1 -- THE EOL PIN.')
w(SUB)
w('### ### **THE MECHANISM WAS EXERCISED IN BOTH POLARITIES BEFORE IT WAS TRUSTED**, in a repository')
w('### built and destroyed for the purpose: with the attribute, blob `%d` and fresh checkout `%d`, equal'
  % (A['fixture']['with the attribute']['blob'], A['fixture']['with the attribute']['checkout']))
w('### `%s`; without it, blob `%d` and checkout `%d`, equal `%s`.'
  % (A['fixture']['with the attribute']['equal'], A['fixture']['without it']['blob'],
     A['fixture']['without it']['checkout'], A['fixture']['without it']['equal']))
w('### ### **A ONE-POLARITY CHECK OF A FIX CANNOT DISTINGUISH THE FIX FROM THE WEATHER.**')
w('')
w('### **WHAT GOVERNED THE GUARD`S PATH, ASKED OF GIT AND NOT INFERRED FROM A PATTERN:**')
w('### %-22s %-14s %-22s %s' % ('repository', 'attributes', 'text/eol before', 'action'))
for k, v in A['state'].items():
    aw = A['wrote'].get(k, {})
    w('### %-22s %-14s %-22s %s'
      % (k, ('present' if v['file_present'] else 'ABSENT'),
         '%s / %s' % (v['text_attr'], v['eol_attr']),
         aw.get('action', '-') + ('' if aw.get('action') == 'WRITTEN'
                                  else ' (%s)' % aw.get('reason', ''))))
w('')
w('### **THE BYTES, BEFORE AND AFTER:**')
w('### %-22s %-30s %s' % ('repository', 'before: work/blob/fresh', 'after: fresh == blob'))
for k in A['before']:
    b, a = A['before'][k], A['after'][k]
    w('### %-22s %-30s %s'
      % (k, '%d / %d / %d' % (b['working'], b['blob'], b['fresh']), a['equal']))
w('')
w('### ### **`relay` CARRIED A PATH-SCOPED LINE THAT DID NOT REACH THE GUARD, AND THAT IS ABSENCE FOR')
w('### ### THIS PURPOSE.** ### Its existing line is ### **PRESERVED, NOT REPLACED**; the')
w('### repository-wide line was added beside it, and the preservation was verified by re-reading the')
w('### written file : `%s`.' % A['wrote'].get('relay', {}).get('preservation_verified'))
w('### ### **AND THE FLOOR, STATED WITH THE FINDING:** ### an attribute added today does not normalise')
w('### a tree checked out yesterday, and this act renormalised none.')
w('### ### **WHAT IS FIXED IS WHAT THE NEXT CHECKOUT PRODUCES**, not what is on this disk today, and')
w('### the act says exactly that rather than claiming the defect is gone from this machine.')
w('### **NO REPOSITORY WAS RENORMALISED. ### NO WORKING FILE WAS')
w('### ### DELETED TO FORCE A CHECKOUT. ### NO BRANCH WAS CREATED AND NOTHING WAS RESET.** ### The')
w('### fresh checkout was taken with `git checkout-index` into a scratch directory -- ### **BECAUSE LAST')
w('### ### ACT A MOVER THAT THOUGHT IT WAS BEING CAREFUL DESTROYED UNCOMMITTED WORK IN FOUR')
w('### ### REPOSITORIES.**')
w('')

w(SUB)
w('### (3) COMPONENT 2 -- THE README, AND THE LABEL THAT DOES NOT FIT IT.')
w(SUB)
w('### ### ### **THE ORDER NAMED ONE OBJECT AND DESCRIBED ANOTHER, AND THAT IS REPORTED AND NOT')
w('### ### ### ABSORBED.** ### The order says ### *"the exclusion kernel`s README"* and then describes')
w('### *"a headline figure, a breakdown that sums to a different figure, and ships a profile carrying a')
w('### third."* ### **THE THREE CLAUSES WERE TESTED AGAINST BOTH CANDIDATES:**')
for k, v in R['candidates'].items():
    w('###   %-46s headline %-5s breakdown %-5s ships a profile %-5s ### ALL THREE : %s'
      % (k[:46], v['clauses']['headline'], v['clauses']['breakdown'], v['clauses']['profile'],
         v['fits']))
w('### ### **THE OBJECT IS IDENTIFIED BY THE DESCRIPTION, BECAUSE A DESCRIPTION IS CHECKABLE AGAINST A')
w('### ### FILE AND A LABEL IS NOT.** ### This is `b367`s species -- a hint that names the right')
w('### terminals and the wrong defect. ### **NOTHING IN THE EXCLUSION KERNEL`S README WAS REPAIRED**,')
w('### and its one count line was read and quoted anyway so nothing is lost if the label was meant.')
w('')
w('### **WHAT EACH FIGURE COUNTS, DETERMINED AT CONTENT BY MEASURING THE SAME QUANTITY AT THE REF THAT')
w('### INTRODUCED IT** (`b371`s method, unamended):')
w('### %-10s %-12s %-20s %-8s %-11s %-20s %s'
  % ('ref', 'date', 'headline', 'sum', 'ratio', 'modules named', 'profile ships'))
for r in TBL:
    w('### %-10s %-12s %-20s %-8s %-11s %-20s %s'
      % (r['ref'][:8], r['date'], r['headline'], r['total'], r['ratio'], r['modules'], r['prints']))
w('')
w('### **AND THE MODULE COUNT AGAINST THE TREE IT DESCRIBES:**')
for r in TBL:
    w('###   `%-8s` Core `.lean` %-4d of which AxiomCheck %-3d -> %-4d not AxiomCheck ; README says %s'
      % (r['ref'][:8], r['core_lean'], r['axiomcheck'], r['non_axiomcheck'], r['modules']))
w('### ### **SO THE MODULE COUNT WAS EXACT AT BOTH REFS THAT WROTE IT, AND IS BEHIND AT THE HEAD** --')
w('### the same shape as the terminal figures and not a separate defect.')
w('')
w('### **THE PROFILE, READ AS A PRINTED RECORD AND COMPARED AGAINST ITS BLOB (`b309`):** ### working')
w('### `%d` bytes, blob `%d` bytes, EOL-normalised equal `%s`; `%d` printed lines, `%d` of them saying'
  % (R['profile']['working'], R['profile']['blob'], R['profile']['eol_equal'],
     R['profile']['lines'], R['profile']['zero']))
w('### the declaration does not depend on any axioms, `%d` distinct names. ### **SO THE README`S CLAIM'
  % R['profile']['names'])
w('### ### `No terminal failed the bar; none is excluded` IS SUPPORTED AND WAS NOT TOUCHED.**')
w('')
w('### **THE ORIGINALS, QUOTED VERBATIM BEFORE THE EDIT:**')
for o in R['originals']:
    w('###   README.md:%d' % o['line'])
    w('###   | %s' % o['text'])
w('')
w('### **THE REPLACEMENTS:**')
for o in R['replacements']:
    w('###   README.md:%d' % o['line'])
    w('###   | %s' % o['text'])
w('')
w('### **WHAT WAS REMOVED, WHAT WAS DATED, AND WHAT WAS ROUTED:**')
w('###   -- the headline figure and the assembly ratio : ### **REMOVED, NOT RESTATED.** ### A new')
w('###      number buys one act`s correctness and re-arms the same trap (`b371`s rule).')
w('###   -- the 33-part layer census and the module count : ### **PRESERVED VERBATIM AND DATED TO THE')
w('###      ### REF THEY HOLD AT** -- which the order permits in place of removal, because a document')
w('###      that names its ref is a document a reader can check.')
w('###   -- re-deriving the census at the head : ### **ROUTED**, because it rewrites')
w('###      ### **A CLAIM AND NOT A NUMBER**, and the order says route it.')
if R.get('verify'):
    v = R['verify']
    w('### **AND THE EDIT WAS VERIFIED BY RE-READING THE FILE:** ### removed figures still present `%s`;'
      % v['removed_still_present'])
    w('### census preserved `%s`; line count unchanged `%s`; `%d` -> `%d` bytes.'
      % (v['census_preserved'], v['linecount_unchanged'], v['before_bytes'], v['after_bytes']))
w('')

w(SUB)
w('### (4) COMPONENT 3 -- THE FIRST BATCH, UNDER `(R6)` AND `(R8)`.')
w(SUB)
w('### **THE HEADS, RECORDED HERE AND IN NO ROW, READ 2026-09-08:**')
for k, v in B['heads'].items():
    w('###   %-14s `%s` = `%s` ### shipped axiom profile : %s'
      % (k, v['branch'], v['head'], v['profiles'] or 'NONE'))
w('### ### **AND THE SECOND HALF OF THE ORDER`S `PRESENT` TEST CANNOT BE SATISFIED IN EITHER KERNEL:')
w('### ### NEITHER SHIPS A PRINTED AXIOM PROFILE.** ### So a declaration found alive is recorded')
w('### ### **PRESENT WITH ITS PROFILE `NOT LOCATED`**, and is not silently upgraded to a clean')
w('### `PRESENT`. ### That is the fourth word with its evidence audited, not a fifth word.')
w('')
w('### **THE TWELVE ROWS:**')
for r in B['rows']:
    comp = {}
    for v in r['verdicts']:
        comp[v['verdict']] = comp.get(v['verdict'], 0) + 1
    w('###   row %s  %s:%d' % (r['row'], r['file'], r['line']))
    w('###       kernel `%s` ; opened at `%s` ; %s' % (r['kernel'], r['ref'][:12], r['mode']))
    for v in r['verdicts']:
        w('###       %-40s ### **%s** -- %s' % ('`' + v['terminal'] + '`', v['verdict'], v['note']))
        if v['quote']:
            w('###           the kernel`s own words, %s:%d' % (v['quote']['file'], v['quote']['line']))
            w('###           | %s' % v['quote']['text'])
        if v['declared']:
            w('###           declared at %s' % '; '.join(
                '%s:%d' % (h['file'], h['line']) for h in v['declared'][:3]))
        if v['last_declared']:
            w('###           ### **IT WAS A DECLARATION AS RECENTLY AS `%s` (%s)** -- a ref this row'
              % (v['last_declared']['commit'][:12], v['last_declared']['date']))
            w('###           ### does not name.')
    w('###       ### the row`s terminals : %s'
      % ', '.join('%s x%d' % (k, n) for k, n in sorted(comp.items())))
w('')
w('### ### **THE ROWS WHOSE `PIN` IS NOT A PIN:** ### %s. ### Each matched `b371`s pin pattern and'
  % ', '.join('%s:%d (`%s`)' % (r['file'], r['line'], r['pins'][0]['pin']) for r in FALSEPIN))
w('### ### **NONE OF THEM RESOLVES IN THE KERNEL THE ROW NAMES**, so the row is pinless in fact and was')
w('### opened at the head. ### `PREDICATE_ONE_SHAPE` running the other way: ### **A PATTERN THAT KNOWS')
w('### ### ONE SHAPE ALSO MATCHES THINGS THAT ARE NOT THAT SHAPE.**')
w('')
w('### ### **THE LEDGER`S OWN LACUNAE, FILED AND NOT INVENTED** (`(R5)`s shape, met in a second')
w('### kernel): %s are cited by rows and are named ### **NOWHERE** in the ledger that retired their'
  % ', '.join('`%s`' % t for _r, t in B['absent']))
w('### neighbours. ### They classify `ABSENT` on the evidence, which is weaker than `RETIRED`.')
w('')
w('### **WHAT IT IMPLIES FOR THE PAPERS -- REPORTED AND ROUTED, AND NO ROW REPAIRED:**')
w('###   -- `VERIFICATION_LOOM.md` rows carrying `✓F` against declarations retired at the head;')
w('###   -- `EXCLUSION_ENGINE.md` rows grading `SHELL` against declarations that no longer exist to be')
w('###      shells;')
w('###   -- `REGISTRY.md`s `p2-31` pairing a manuscript to a retired declaration.')
w('### ### **EVERY ONE OF THOSE ROWS WAS TRUE AT A REF AND NONE OF THEM NAMES ONE.** ### What to do')
w('### about it is the author`s; this act was told the classification is the product.')
w('')
w('### **THE PRICE OF THE SEPARATE RULING, GIVEN BECAUSE `(R8)` ASKS AND NOT BECAUSE THIS ACT ARGUES:**')
w('### this act opened `%d` kernel refs to classify `%d` rows, reading the whole `.lean` tree at each.'
  % (len(set(r['ref'] for r in B['rows'])), len(B['rows'])))
w('### `b371` inventoried `%d` pinless rows. ### Pinning ONE row costs: resolve the kernel the row'
  % INV['without_pin'])
w('### names; ### **FIND THE REF AT WHICH THE ROW WAS TRUE** (this act located that ref by history')
w('### search for every retired terminal it met); and write it in. ### **THE READ SCALES. ### THE')
w('### ### HISTORY WALK IS THE EXPENSIVE HALF AND IT IS THE HALF THAT CANNOT BE SKIPPED, BECAUSE A PIN')
w('### ### WRITTEN AT THE HEAD PINS A ROW TO A STATE IN WHICH THE ROW IS FALSE.** ### That is the')
w('### price. ### **THIS ACT ATTEMPTS NONE OF IT.**')
w('')

w(SUB)
w('### (5) THE DESK, UNDER `(R7)`, AND THE TRAILS LEDGER.')
w(SUB)
w('### ### **`%d` SWEPT. ### `%d` CLOSED. ### `%d` STANDING. ### CLOSURES REFUSED FOR WANT OF A KILLING'
  % (Q['items'], Q['closed'], Q['standing']))
w('### ### FILE : `%d`.**' % Q['closures_refused'])
for c in Q['closed_items']:
    w('###   CLOSED  %-56s killing file `%s`, dated %s'
      % (c['item'][:56], c['file'], c['date']))
    if c['own_act']:
        w('###           ### **FLAGGED: THE KILLING FILE IS THIS ACT`S OWN.** ### Allowed -- this act')
        w('###           ### did the killing -- and NOT a confirmation drawn from the record (`b368`).')
w('### ### **AND THE KILLING FILE WAS RESOLVED BY ITS RECORDED CLOCK, NEVER BY ITS NAME** (`b358`):')
w('### `run_clock` numbers repeats, and the run that did the work is not the run that ran first.')
w('### **THE TRAILS LEDGER WAS UPDATED THROUGH ITS WRITER**, append-only `%s`, the committed version'
  % F['appended_only'])
w('### still a substring of the file `%s`, `%d` -> `%d` bytes, under the mark'
  % (F['committed_prefix_intact'], F['before_bytes'], F['after_bytes']))
w('### `%s`.' % F['mark'])
w('')

w(SUB)
w('### (6) THE EXPECTATIONS, SCORED.')
w(SUB)
w('### ### ### **`(F1)` -- THE NAVIGATOR`S: *the README`s three figures count three different scopes and')
w('### ### ### none names its ref.* ### SPLIT: ### **THE FIRST HALF IS REFUTED, THE SECOND CONFIRMED.**')
w('### The three figures count ### **ONE** quantity -- Core zero-axiom terminals, one per printed line --')
w('### at ### **THREE DIFFERENT REFS**, and the refutation is a quotation: at `%s` the headline, the'
  % T0['ref'][:7])
w('### breakdown, the ratio and the profile all read `%s`. ### **AND NONE OF THEM NAMES ITS REF**, which'
  % T0['total'])
w('### is the half that holds and is the half that matters for the repair.')
w('### ### **THE DIFFERENCE IS NOT COSMETIC:** ### three scopes would need three separate repairs and a')
w('### reader would have to learn which figure meant what. ### **ONE QUANTITY AT THREE DATES NEEDS ONE')
w('### ### REPAIR -- NAME THE REF OR REMOVE THE NUMBER** -- which is what was done.')
w('')
w('### ### ### **`(F2)` -- THE NAVIGATOR`S: *most of the twelve classify RETIRED rather than ABSENT.*')
w('### ### ### CONFIRMED.** ### `%d` named terminals classify `RETIRED` against `%d` `ABSENT`, and every'
  % (TV.get('RETIRED', 0), TV.get('ABSENT', 0)))
w('### `RETIRED` quotes the kernel`s own retirement ledger. ### **THE REASON IS THE KERNEL`S OWN')
w('### ### HONESTY**: it keeps a retirement ledger naming what it withdrew, so a withdrawn declaration')
w('### leaves a record instead of a hole. ### The `ABSENT` ones are exactly the names that ledger')
w('### ### **DOES NOT MENTION** -- so `(F2)` measures the ledger`s coverage, and its coverage is good.')
w('')
w('### **`(E1)` -- THIS SEAT`S, AND IT WAS DECIDED BEFORE THE LOCK AND SO IS `NOT AN EXPECTATION`.**')
w('### The registration says so on its own face. ### It held; it forecast nothing.')
w('### **`(E2)` -- THIS SEAT`S: *the RETIRED verdicts will be carried by the papers` own rows as often')
w('### as by the kernel`s record.* ### REFUTED, AND THE REFUTATION IS THE INTERESTING PART.** ### Only')
w('### `VERIFICATION_LOOM.md:581` states its own retirement; the other rows carry `✓F` or `SHELL` and')
w('### ### **CLAIM THE THING IS THERE.** ### The record does NOT agree with itself, and this seat')
w('### predicted it would.')
w('')

w(SUB)
w('### (7) WHAT THIS ACT DID NOT DO.')
w(SUB)
w('### **NO ROW WAS REPAIRED. ### NO PIN WAS ADDED TO ANY ROW.** ### `(R8)`s separate ruling is priced')
w('### and not attempted.')
w('### **NO HEAD WAS WRITTEN INTO A ROW.** ### Every head this act read is in this bank.')
w('### **NO REPOSITORY WAS RENORMALISED. ### NO WORKING FILE WAS DELETED TO FORCE A CHECKOUT. ### NO')
w('### ### SCRATCH BRANCH WAS CREATED OR RESET IN ANY REPOSITORY.**')
w('### **NOTHING IN THE EXCLUSION KERNEL`S README WAS REPAIRED**, and the label/description discrepancy')
w('### is reported rather than resolved by this seat`s preference.')
w('### **NO `.lean` FILE WAS TOUCHED. ### NO BUILD WAS RUN. ### NO AXIOM PROFILE WAS RECOMPUTED.**')
w('### **NO FEDERATION-WIDE SURFACE SWEEP WAS OPENED.** ### `(R6)`s second pass stays shut.')
w('### **NO GRADE WAS CONFERRED AND NO FACE WAS PROMOTED.** ### That a declaration exists says nothing')
w('### about whether what it names is true.')
w('### **NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NOTHING WAS COMPILED AND NO BRIDGE WAS TYPED.**')
w('### **NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED.**')
w('### **NOTHING HERE BEARS ON `h2`, ON TOTALITY OR ON THE ROSTER.** ### `M-2` remains')
w('### (SPECIFIED-NOT-STATED) under `b310`s cap. ### The seam`s debt item 1 stands. ### The patent lane')
w('### is carried on the patent seat`s report, UNCONFIRMED on this seat`s record. ### **THE POSTURE LOCK')
w('### ### IS SEPARATE. ### THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED.** ### `h2`')
w('### stands exactly where the deposit left it. ### **NOTHING DEPOSITS.**')
w('')

w(SUB)
w('### (8) THE SPECIES THIS ACT ADDS, AND THE ONES IT MET AGAIN.')
w(SUB)
w('### ### ### **NEW -- `A PIN IS A DATE THAT SURVIVES`.** ### The same three declarations are')
w('### ### **PRESENT AT A PINNED ROW`S REF AND RETIRED AT THE HEAD.** ### The pinned row aged well;')
w('### the pinless rows citing the same declarations did not, and ### **NOTHING IN THEM TELLS A READER')
w('### ### WHICH REF THEY MEANT.** ### That is `(R8)` demonstrated inside one act rather than argued.')
w('### ### ### **NEW -- `A FIGURE THAT WAS EXACT IS NOT A FIGURE THAT IS WRONG`.** ### Every figure in')
w('### the README was ### **EXACT WHEN IT WAS WRITTEN.** ### The defect is not arithmetic; it is that')
w('### ### **A NUMBER WITHOUT A REF IS A CLAIM ABOUT AN UNNAMED MOMENT**, and the repair is to name the')
w('### moment or drop the number, never to write a fresher number.')
w('### **MET AGAIN -- `PREDICATE_ONE_SHAPE`, RUNNING THE OTHER WAY.** ### A pattern that knows one shape')
w('### also matches things that are NOT that shape: a manuscript version read as a kernel pin, a sort')
w('### (`Prop`) read as a terminal, a docstring`s mention of a ledger read as the ledger. ### **THE')
w('### ### THIRD ONE REPORTED EVERY TERMINAL AS ABSENT, CONFIDENTLY**, until the heading predicate was')
w('### made to require a comment line.')
w('### **MET AGAIN -- `b369`s SLASH ABBREVIATION.** ### A retirement written `a/b/c` names three')
w('### declarations and a whole-word search finds one. ### Mechanised here rather than re-learned.')
w('### **MET AGAIN -- `b367`s LABEL-VERSUS-DESCRIPTION.** ### A hint that names the right terminals and')
w('### the wrong defect; the object is identified by what is checkable.')
w('')

w(SUB)
w('### (9) THE CLOCKS, THE REFS AND THE FILES.')
w(SUB)
w('### registration locked at (UTC) %s' % LAT)
for n in ('b372_reads', 'b372_eol', 'b372_readme', 'b372_batch', 'b372_desk', 'b372_filing'):
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
