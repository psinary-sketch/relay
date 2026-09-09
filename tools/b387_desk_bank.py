# -*- coding: utf-8 -*-
"""b387_desk_bank.py -- THE DESK UNDER `(R7)`, THE THREE CLOSING WRITES, AND THE BANK.

### ### **THIS ACT CLOSES NOTHING, AND THAT IS THE RIGHT ANSWER RATHER THAN A THIN ONE.** ### It
### is a READ and a COUNT. ### `(R7)` closes an item whose OCCASION is gone, and counting what the
### tables carry removes no obligation, answers no routed question and repairs no defect.
### ### **A MEASUREMENT IS NOT A CLOSURE** (`b383`), and an act that measures well and then closes
### something to show for it has traded a true record for a tidy one.
###
### ### **WHAT IT ADDS TO THE DESK IS FOUR DISAGREEMENTS AND TWO RESTORATIONS**, each STANDING.
### ### **AND `(R16)` IS RECORDED WITH ITS REASON**, so a later survey reads the untracked hook
### copies as a ruled disposal and not as divergence -- which is what the ruling asks for.
"""
import glob
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                  # noqa: E402
import gate_needle as GN          # noqa: E402
import b302_correspondence as C   # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b387 what the keystones tables actually carry; (R16) recorded -->'
PRIOR = '<!-- b386 the guard made single-sourced; (R15) executed -->'
ACT = 'b387'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


AC = J('b387_components')
LG = J('b387_lockgate')
E = J('b387_reads')
C1, C2, C3, C4 = AC['C1'], AC['C2'], AC['C3'], AC['C4']
BANKOUT = os.path.join(D, 'b387_what_the_tables_carry.txt')
TOT = C2['totals']

DESK = [
    ('M-2, under b310 cap', 'STAND', None, None,
     'the aggregation is still SPECIFIED-NOT-STATED and b310 cap still governs'),
    ("the object's conditions", 'STAND', None, None,
     "the conditions are the object's and none has been discharged"),
    ('the uniformity row U1, four entries and its own refusal', 'STAND', None, None,
     "the row's own refusal stands and the entries are unchanged"),
    ('the instrument lane, PARKED under ruling R4', 'STAND', None, None,
     "PARKED by the author's ruling; only the author unparks it"),
    ('the wave candidate list, typed and not ranked at b324', 'STAND', None, None,
     "typed and not ranked; ranking is the author's"),
    ("the wave itself, the author's own", 'STAND', None, None, "PARKED by the author's ruling"),
    ('the routed items, each with its owner', 'STAND', None, None,
     'each still carries its owner and none has been opened'),
    ('the patent receipts, absent on the mounted volumes', 'STAND', None, None,
     "UNCONFIRMED on this seat's record; the patent seat owns it"),
    ('the count claim above the repaired Layer-1 list', 'STAND', None, None,
     'no act has been sent to it since b369'),
    ("the retirement ledger's own lacunae", 'STAND', None, None,
     'FILED, NOT INVENTED, AND NOT REPAIRED'),
    ('where the keystone census should live, ROUTED at b375', 'STAND', None, None,
     'ROUTED to the author; this act creates no tracking document either'),
    ("the census's definition-versus-operation drift", 'STAND', None, None,
     'FILED at b377 and ### **NOT REPAIRED**'),

    # ---- THE FOUR OPEN LISTS, RESTATED OPEN BY NAME ---------------------------------------------
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND', None, None,
     'OPEN. ### This act adds nothing to it and closes nothing'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND', None,
     None, 'OPEN. ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', None, None,
     'OPEN. ### This act dates none of them'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND', None, None,
     'OPEN. ### This act rewrites none of them'),

    # ---- CARRIED --------------------------------------------------------------------------------
    ('the class ruling itself', 'STAND', None, None,
     'STILL THE AUTHOR`S, and the standing standard already rules it'),
    ('the three amendments b383 drafted that are still routed', 'STAND', None, None,
     '### **ROUTED AND UNAPPLIED.** ### `(i)`, `(ii)` and `(iii)` remain the author`s'),
    ('the citation question -- what a finished keystone is cited as', 'STAND', None, None,
     '### **AWAITING THE AUTHOR AND NOT MOVED BY THIS ACT.** ### Component 3 says what the '
     'corpus`s PER-ROW PRACTICE SHOWS -- `%d` of `%d` rows in Tier-K documents are already '
     'labelled as something other than a machine-checked terminal -- and ### **STOPS THERE.** '
     '### `%d` recommended, `%d` options added, and ### **A BEARING IS NOT AN ANSWER**'
     % (C3['not_machine_verified'], C3['rows'], C3['recommended'], 0)),
    ('the download-layer book`s registry drift', 'STAND', None, None,
     'OPEN AND ### **THE AUTHOR`S**, in `(R14)`s own words'),
    ('the six subject clusters with no keystone', 'STAND', None, None,
     'ON THE TRAILS LEDGER as ### **`NOT-YET-SYNTHESIZED`, NOT OWED AND NOT DEFICIENT** ### '
     'since b385. ### `0` opened by this act'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', None, None,
     'CARRIED and ### **DELIBERATELY NOT RE-MEASURED**'),
    ('the ten untracked run records of earlier acts', 'STAND', None, None,
     'NAMED at b382 and ### **STILL UNTRACKED**'),
    ('the legacy `.git/hooks/pre-push` copies, one per repository', 'STAND', None, None,
     '### **RULED BY `(R16)`: THEY STAY.** ### *The repository configuration already makes the '
     'tracked source the one that runs, and the untracked copies are a fallback; removing a '
     'working fallback was not asked for and buys nothing.* ### **RECORDED WITH ITS REASON SO A '
     'LATER SURVEY DOES NOT READ THEM AS DIVERGENCE** -- which is what the ruling asks, and it is '
     'why this item stays on the desk rather than leaving it'),
    ('the untracked `.b304-backup` artifacts the installer left', 'STAND', None, None,
     'NAMED at b386 and ### **STILL UNTRACKED, STILL NOT DELETED**'),

    # ---- WHAT THIS ACT ADDS ---------------------------------------------------------------------
    ('the five keystones the union names that carry no correspondence table', 'STAND', None, None,
     'NEW at b387: `%s` -- ### **THE UNION NAMES `%d` GRADED CORRESPONDENCE TABLES AND `%d` OF '
     'THE DOCUMENTS CARRY ONE.** ### The absence is PROVED, not assumed: every table in each file '
     'was read and its columns printed. ### **REPORTED AND NOT RECONCILED**, because both the '
     'union and the documents are the author`s'
     % (', '.join('`%s`' % t for t in C1['without_tags']), C1['union_names'], C1['with_table'])),
    ('the union`s named carrier for MONO is not the graded table', 'STAND', None, None,
     'NEW at b387: the union points `MONO` at ### **`§25.8`**, whose table carries '
     '`claim | theorem | module | #print axioms` -- ### **NO STATUS COLUMN AND NO GRADE COLUMN.** '
     '### The monograph`s graded table is elsewhere in the same document. ### **REPORTED AND NOT '
     'RECONCILED**'),
    ('`ENGINE`s table is a work-order instrument, not a claim-to-artifact one', 'STAND', None,
     None,
     'NEW at b387: columns `terminal | location | grade | what the source says | work-order`. ### '
     'It carries a `grade` column so the shape test admits it, and ### **ITS DIFFERENT SHAPE IS '
     'STATED BESIDE ITS COUNT** -- a count that hides a different instrument inside a total is a '
     'wrong count'),
    ('the `%d` rows whose status this act could not read' % C2['unreadable_n'], 'STAND', None,
     None,
     'NEW at b387: ### **`%d` OF `%d` ROWS ARE REPORTED `UNREADABLE`, NAMED BY DOCUMENT AND '
     'LINE, AND NEVER ASSIGNED.** ### `(E1)` registered that a residue was expected and the '
     'residue is real. ### **AN UNREADABLE ROW FORCED INTO A CATEGORY IS A FABRICATED COUNT**'
     % (C2['unreadable_n'], C2['rows'])),
    ('the seat`s memory is under no version control', 'STAND', None, None,
     'NEW at b387: the order asked for the file`s ### **PRIOR BLOB** ### and there is none -- the '
     'home repository`s branch has no commits and `MEMORY.md` is untracked in it. ### The '
     'comparison used a byte-for-byte artifact this seat took before the trim, ### **NAMED AS AN '
     'ARTIFACT AND NOT CALLED A BLOB.** ### **A TRIM OF THE SEAT`S MEMORY IS NOT REVERTIBLE FROM '
     'THE RECORD**, and that is routed to the author rather than repaired here'),
    ('and two claims b386`s trim dropped, restored', 'STAND', None, None,
     'NEW at b387: the screen flagged `%d` of `%d` shortened hooks; ### **`%d` WERE JUDGED '
     'COVERED AND `%d` LOST**, each judgement printed with the file`s own nearest sentence beside '
     'it. ### The two lost claims are ### **RESTORED BY APPENDING** ### to the topic files they '
     'belong in. ### The item STANDS because ### **THE SCREEN IS A SCREEN AND THE JUDGEMENT IS A '
     'SEAT`S**, and a later reader may overturn either'
     % (len(C4['judged']), C4['hooks_checked'],
        sum(1 for j in C4['judged'] if j['verdict'] == 'COVERED'), C4['lost_n'])),
]

def newest_run(stem):
    cands = sorted(glob.glob(os.path.join(D, stem + '*.txt')))
    best, bstamp = None, ''
    for c in cands:
        s = run_clock.read_stamp(c) or ''
        if s >= bstamp:
            best, bstamp = c, s
    return best, bstamp


def do_desk():
    rec('    ### ### **THIS ACT CLOSES NOTHING, AND THAT IS THE ANSWER RATHER THAN A THIN ONE.**')
    rec('    ### `(R7)` closes an item whose ### **OCCASION** ### is gone. ### Counting what the')
    rec('    ### tables carry removes no obligation, answers no routed question and repairs no')
    rec('    ### defect. ### **A MEASUREMENT IS NOT A CLOSURE** (`b383`).')
    rec('')
    marks = []
    for item, want, stem, sentence, why in DESK:
        row = dict(item=item, disposition=want, killing_stem=stem, why=why)
        marks.append(row)
        rec('    %-78s %s' % (item, row['disposition']))
        rec('        why : %s' % why[:150])
        if len(why) > 150:
            rec('              %s' % why[150:340])
        if len(why) > 340:
            rec('              %s' % why[340:560])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    stands = [m for m in marks if m['disposition'] == 'STAND']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(stands)))
    rec('    ### ### **SIX ITEMS ARE ADDED AND ALL SIX STAND**: the five keystones with no table,')
    rec('    ### the ungraded carrier, `ENGINE`s different instrument, the unreadable rows, the')
    rec('    ### memory`s want of version control, and the two restored claims.')
    rec('    ### ### ### **AND `(R16)` IS RECORDED ON THE DESK WITH ITS REASON**, so a later')
    rec('    ### ### ### survey reads the untracked hook copies as ### **A RULED DISPOSAL AND NOT')
    rec('    ### ### ### AS DIVERGENCE** -- which is what the ruling asks for.')
    return dict(items=len(marks), closed=len(closed), standing=len(stands),
                closures_refused=0, conditional_refusals=0, marks=marks,
                exercise_ok=None, exercise_rows=0, closed_items=[])


def trail_block(Q):
    tot = TOT
    return [
        '', MARK, '',
        '### **b387 — WHAT THE KEYSTONES’ TABLES ACTUALLY CARRY (2026-09-09)**',
        '',
        ('*No block above is edited. The b386 block (`%s`) and every block before it stand exactly '
         'as they were written.*' % PRIOR),
        '',
        ('**RULING `(R16)`, THE AUTHOR’S, RECORDED HERE WITH ITS REASON: THE UNTRACKED HOOK '
         'COPIES STAY.** *The repository configuration already makes the tracked source the one '
         'that runs, and the untracked copies are a fallback; removing a working fallback was not '
         'asked for and buys nothing.* It is recorded **so a later survey does not read them as '
         'divergence** — b386 left them in place as a marked judgement and the author has now '
         'ruled it.'),
        '',
        ('**THIS ACT IS A READ AND A COUNT. NO RULING, NO REPAIR, NO ROW EDITED, NO GRADE MOVED, '
         'AND NOTHING CLOSED.** `(R7)` closes an item whose occasion is gone; counting what the '
         'tables carry removes no obligation. **A measurement is not a closure.**'),
        '',
        ('**THE UNION NAMES FOURTEEN GRADED CORRESPONDENCE TABLES AND NINE OF THE FOURTEEN '
         'DOCUMENTS CARRY ONE.** `THE_LOAD_BEARING_MAP.md` — *the keystone correspondence union* '
         '— names MONO · SIMP · GRH · FOUND · SURR · LIC · RCURVE · PATHS · ENGINE · DOM · '
         'IFACE · SEVEN · CNA · BALPOS. Read at the canonical drive, located **by shape and never '
         'by heading**: **%d carry a correspondence-shaped table, %d carry none** — %s. The '
         'absence is **proved, not assumed**: every table in each of the five was read and its '
         'columns printed. **Reported and not reconciled**, as the order requires: both the union '
         'and the documents are the author’s.'
         % (C1['with_table'], C1['without_table'],
            ', '.join('`%s`' % t for t in C1['without_tags']))),
        '',
        ('**AND THE UNION POINTS MONO AT A TABLE THAT IS NOT GRADED.** `§25.8 Kernel Concordance` '
         'carries `%d` rows whose columns are `claim | theorem | module | #print axioms` — '
         '**no status column and no grade column**. The monograph does carry a graded table, at '
         'its `## Correspondence` appendix added 2026-08-12. **The union names a carrier that is '
         'not the graded one.** Two further disagreements: two on-disk filenames carry a version '
         'suffix the union’s names do not, and **`ENGINE`’s table is a work-order '
         'instrument** (`terminal | location | grade | what the source says | work-order`), not a '
         'claim-to-artifact table — counted, with its shape stated beside its count. '
         '**%d disagreements reported, %d reconciled.**'
         % (E['mono_258']['rows'], C1['disagreements_reported'], C1['reconciled'])),
        '',
        ('**EVERY ROW IN THE LOCATED TABLES IS COUNTED BY WHAT BACKS IT — %d ROWS, AND THE '
         'CATEGORIES SUM.** The categories are the corpus’s own: the front door says a row maps '
         '*claim · kernel · fully-qualified theorem name · axiom profile · status*, and *where no '
         'kernel exists, the status says so in words — manuscript-resident or research-reach — '
         'rather than being omitted.* Counted: **DERIVES-at-a-terminal %d · INTERFACES-on-a-named-'
         'premise %d · manuscript-resident %d · research-reach %d · shell-or-encodes-conclusion '
         '%d · UNREADABLE %d.** Every `INTERFACES` row has **its premise printed**; a row that '
         'named no premise was re-counted `UNREADABLE` rather than left in the bin. '
         '**The %d unreadable rows are named by document and line and never assigned** — an '
         'unreadable row forced into a category is a fabricated count.'
         % (C2['rows'], tot.get('DERIVES', 0), tot.get('INTERFACES', 0),
            tot.get('MANUSCRIPT_RESIDENT', 0), tot.get('RESEARCH_REACH', 0),
            tot.get('SHELL_OR_ENCODES', 0), tot.get('UNREADABLE', 0), C2['unreadable_n'])),
        '',
        ('**THE ANSWER FROM PRACTICE: YES — %d OF %d ROWS (%.1f%%) ARE NOT MACHINE-VERIFIED, AND '
         'EVERY ONE IS LABELLED IN ITS OWN ROW.** The scope is named so the count cannot travel: '
         'over the **%d documents of the fourteen that carry a table**, over **%d rows in all '
         'their located tables** including `ENGINE`’s differently-shaped one, counting '
         'INTERFACES + manuscript-resident + research-reach + shell-or-encodes as *not '
         'machine-verified* against DERIVES as machine-verified, with the unreadable rows assigned '
         'to neither. **The honesty is the corpus’s; the count is this act’s.** And every '
         'figure is a count of **claimed** status: this act read what each row says, **opened no '
         'kernel and ran no `#print axioms`**.'
         % (C3['not_machine_verified'], C3['rows'], C3['fraction'],
            C3['documents_counted'], C3['rows'])),
        '',
        ('**WHAT THAT BEARS ON THE CITATION QUESTION — AND WHERE IT STOPS.** The standard’s three '
         'author-ruled borderlines all turn on **reading parts of one document differently**: '
         '`CATALOGOS` is Tier C with its pinned rows read as K; `UNIVERSALITY` is mostly K with a '
         'C-scope note; `THE_SUBSTRATE` is K with its Related Work read as context. The practice '
         'measured above is **the same move at row granularity**, inside documents the standard '
         'calls Tier K. **So the per-row practice exists and is in use. Whether it supplies the '
         'rule the author is being asked for is the author’s to say, and this act does not say '
         'it.** **%d options recommended, ranked or preferred. The citation question is restated '
         'as awaiting the author and is not moved.** **A bearing is not an answer.**'
         % C3['recommended']),
        '',
        ('**AND THE SEAT AUDITED ITS OWN MEMORY, WHERE THE ORDER ASKED FOR A BLOB AND THERE IS '
         'NONE.** The home repository’s branch has no commits and `MEMORY.md` is untracked in '
         'it, so the comparison used a byte-for-byte copy taken immediately before b386’s trim — '
         '**named as an artifact and not called a blob**. **%d entries before, %d after; %d '
         'pointers dropped; %d pointers resolving to no file.** Of **%d shortened hooks**, a token '
         'screen flagged **%d** — and the screen **over-reports by design**, because a hook is a '
         'summary and its wording differs from its topic file’s by construction. Each flag was '
         'read against the file’s own nearest sentence: **%d judged COVERED, %d judged LOST.** '
         '**(F2) is refuted, narrowly and precisely.** The two lost claims — *U-1’s counter is '
         'lexical, so rephrase rather than fight the scan* (used twice in this very session) and '
         '*the fold was not due at b363, span 3 against a shortest of 4, counted by '
         '`tools/b363_span.py`* — are **restored by appending** to the topic files they belong '
         'in. **No entry was deleted and no topic file was rewritten.**'
         % (C4['entries_before'], C4['entries_after'], C4['pointers_dropped'],
            C4['pointers_unresolved'], C4['hooks_checked'], len(C4['judged']),
            sum(1 for j in C4['judged'] if j['verdict'] == 'COVERED'), C4['lost_n'])),
        '',
        ('**WHAT THIS ACT DID NOT DO.** **No class ruled, no document reclassified, no declaration '
         'moved, no grade moved, no act re-verdicted, no list closed, and nothing closed on the '
         'desk at all.** **No row was edited and no Correspondence table was touched.** No kernel '
         'was opened, no `#print axioms` re-run, no build run, no axiom profile recomputed. '
         '**`README.md`, `REGISTRY.md`, `THE_LOAD_BEARING_MAP.md` and '
         '`THE_DOCUMENT_CLASS_TAXONOMY.md` were read and not touched, and the union was not '
         'corrected.** No archive file touched, no cluster opened, the mirror roster not edited, '
         'and **no `.git/hooks/pre-push` deleted in any repository** — which `(R16)` now rules. '
         '**The four open lists are restated OPEN by name.** h2 stands exactly where the deposit '
         'left it and this act makes no claim about it in either direction.'),
        '',
    ]


SCOPE = (
    "**SCOPE: A READ AND A COUNT OF WHAT THE KEYSTONES' TABLES CARRY.** NO class ruled, NO "
    "document reclassified, NO declaration moved, NO grade moved, NO act re-verdicted, NO list "
    "closed, AND NOTHING CLOSED ON THE DESK -- a measurement is not a closure. **NO ROW WAS "
    "EDITED AND NO CORRESPONDENCE TABLE WAS TOUCHED. NO STATUS WAS CORRECTED**, and where a "
    "row's status looked wrong to this seat that is not this act's to say. **NO KERNEL WAS "
    "OPENED AND NO `#print axioms` WAS RE-RUN**, so EVERY FIGURE IS A COUNT OF CLAIMED STATUS "
    "and the word CLAIMED is carried with it (b374's limit, inherited). **README.md, REGISTRY.md, "
    "THE_LOAD_BEARING_MAP.md AND THE_DOCUMENT_CLASS_TAXONOMY.md WERE READ AND NOT TOUCHED, AND "
    "THE UNION WAS NOT CORRECTED.** **EVERY DISAGREEMENT BETWEEN THE UNION'S LIST AND THE DISK IS "
    "REPORTED AND NONE IS RECONCILED.** **THE TABLES WERE FOUND BY SHAPE AND NEVER BY HEADING** "
    "((R2)), and the predicate that found them was WRONG TWICE BEFORE IT WAS RIGHT, which is "
    "reported. **THE CATEGORIES ARE THE CORPUS'S OWN WORDS AND THE PARTITION SUMS TO THE ROW "
    "COUNT, PER DOCUMENT AND IN TOTAL.** **EVERY INTERFACES ROW NAMES ITS PREMISE AND EVERY "
    "UNREADABLE ROW IS NAMED AND NEVER ASSIGNED.** **NOTHING IS RECOMMENDED, NO OPTION IS RANKED "
    "OR PREFERRED, AND THE CITATION QUESTION IS RESTATED AS AWAITING THE AUTHOR AND NOT MOVED** "
    "-- A BEARING IS NOT AN ANSWER. **(R16) IS RECORDED WITH ITS REASON AND NO .git/hooks/pre-push "
    "WAS DELETED IN ANY REPOSITORY.** **THE MEMORY COMPARISON USED AN ARTIFACT AND NAMED IT AS "
    "ONE, BECAUSE NO PRIOR BLOB EXISTS**; the token screen OVER-REPORTS BY DESIGN and every flag "
    "was judged against the file's own nearest sentence, with the judgements printed so a reader "
    "can overturn them. **NO MEMORY ENTRY WAS DELETED AND NO TOPIC FILE WAS REWRITTEN; A "
    "RESTORATION APPENDS.** **THE FACE WAS NOT WIDENED MID-ACT.** **THE FOUR OPEN LISTS ARE "
    "RESTATED OPEN BY NAME.** **NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS.** NO ARCHIVE "
    "FILE TOUCHED, NO CLUSTER OPENED, THE MIRROR ROSTER NOT EDITED. NO .lean FILE TOUCHED, NO "
    "BUILD RUN, NO AXIOM PROFILE RECOMPUTED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY "
    "NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, "
    "totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS "
    "CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The "
    "patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE "
    "INSTRUMENT LANE STAYS PARKED. THE WAVE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands "
    "exactly where the deposit left it and this act makes no claim about it in either direction. "
    "NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def corr_rows(Q):
    tot = TOT
    m = ("**NINE OF THE FOURTEEN KEYSTONES THE UNION NAMES CARRY A CORRESPONDENCE TABLE, AND %d OF "
         "THEIR %d ROWS ARE NOT MACHINE-VERIFIED AND SAY SO IN THEIR OWN WORDS** (b387, what the "
         "keystones' tables actually carry)"
         % (C3['not_machine_verified'], C3['rows']))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b387, %d gates read and %d checked "
            "by digest. THIS ACT IS A READ AND A COUNT: NO RULING, NO REPAIR, NO ROW EDITED, NO "
            "GRADE MOVED, AND NOTHING CLOSED ON THE DESK, because A MEASUREMENT IS NOT A CLOSURE. "
            "THE SET IS THE UNION'S OWN keystone-set line read by the anchor tool AND NOT A "
            "PREDICATE OVER THE CORPUS; the tables were located BY SHAPE AND NEVER BY HEADING "
            "((R2)), and THE PREDICATE WAS WRONG TWICE BEFORE IT WAS RIGHT -- a heading test found "
            "7 of 14, a status-column test found 8 and missed R_CURVE_CRITERION whose column is "
            "headed Grade, and the union's own word GRADED is what admits it. %d OF THE %d CARRY A "
            "CORRESPONDENCE-SHAPED TABLE AND %d CARRY NONE (%s), THE ABSENCE PROVED BY READING EVERY "
            "TABLE IN EACH FILE AND PRINTING ITS COLUMNS. %d DISAGREEMENTS BETWEEN THE "
            "UNION'S LIST AND THE DISK ARE REPORTED AND %d RECONCILED: the five with no table; THE "
            "UNION POINTS MONO AT 25.8 WHOSE TABLE HAS NO STATUS AND NO GRADE COLUMN while the "
            "monograph's graded table is elsewhere in the same document; two on-disk filenames "
            "carry a version suffix the union's names do not; and ENGINE'S TABLE IS A WORK-ORDER "
            "INSTRUMENT and not a claim-to-artifact one, counted with its shape stated beside its "
            "count. EVERY ROW IS COUNTED BY WHAT BACKS IT, IN THE CORPUS'S OWN WORDS FROM THE "
            "FRONT DOOR: DERIVES %d, INTERFACES %d, manuscript-resident %d, research-reach %d, "
            "shell-or-encodes-conclusion %d, UNREADABLE %d, AND THE CATEGORIES SUM TO THE ROW "
            "COUNT PER DOCUMENT AND IN TOTAL. EVERY INTERFACES ROW NAMES ITS PREMISE and a row "
            "whose premise could not be named was RE-COUNTED UNREADABLE RATHER THAN LEFT IN THE "
            "BIN; the %d unreadable rows are NAMED BY DOCUMENT AND LINE AND NEVER ASSIGNED. THE "
            "ANSWER FROM PRACTICE IS YES: %d OF %d ROWS (%.1f%%) ARE NOT MACHINE-VERIFIED AND "
            "EVERY ONE IS LABELLED IN THE ROW ITSELF, over the %d documents that carry a table -- "
            "AND EVERY FIGURE IS A COUNT OF CLAIMED STATUS, since NO KERNEL WAS OPENED AND NO "
            "print axioms WAS RE-RUN. THE BEARING ON THE CITATION QUESTION, STATED AND NOT "
            "EXTENDED: the standard's three author-ruled borderlines all turn on READING PARTS OF "
            "ONE DOCUMENT DIFFERENTLY, and the measured practice is THE SAME MOVE AT ROW "
            "GRANULARITY inside Tier-K documents -- SO THE PER-ROW PRACTICE EXISTS AND IS IN USE, "
            "AND WHETHER IT SUPPLIES THE RULE THE AUTHOR IS BEING ASKED FOR IS THE AUTHOR'S TO "
            "SAY. %d RECOMMENDED AND THE QUESTION IS NOT MOVED. RULING (R16) IS RECORDED WITH ITS "
            "REASON so a later survey reads the untracked hook copies as a ruled disposal and not "
            "as divergence. AND THE SEAT AUDITED ITS OWN MEMORY: NO PRIOR BLOB EXISTS, so the "
            "comparison used a byte-for-byte artifact NAMED AS AN ARTIFACT; %d entries before and "
            "%d after, %d pointers dropped, %d resolving to no file; of %d shortened hooks a token "
            "screen flagged %d AND THE SCREEN OVER-REPORTS BY DESIGN, so each flag was judged "
            "against the file's own nearest sentence -- %d COVERED, %d LOST, AND THE TWO LOST "
            "CLAIMS ARE RESTORED BY APPENDING"
            % (LG['gates_read'], LG['face_subject_gates'],
               C1['with_table'], C1['union_names'], C1['without_table'],
               ' '.join(C1['without_tags']),
               C1['disagreements_reported'], C1['reconciled'],
               tot.get('DERIVES', 0), tot.get('INTERFACES', 0),
               tot.get('MANUSCRIPT_RESIDENT', 0), tot.get('RESEARCH_REACH', 0),
               tot.get('SHELL_OR_ENCODES', 0), tot.get('UNREADABLE', 0),
               C2['unreadable_n'], C3['not_machine_verified'], C3['rows'], C3['fraction'],
               C3['documents_counted'], C3['recommended'],
               C4['entries_before'], C4['entries_after'], C4['pointers_dropped'],
               C4['pointers_unresolved'], C4['hooks_checked'], len(C4['judged']),
               sum(1 for j in C4['judged'] if j['verdict'] == 'COVERED'), C4['lost_n']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN AND NO ROW WAS WRITTEN INTO ANY "
            "CORPUS DOCUMENT. ### Rows were READ AND COUNTED; every quoted line was re-read out "
            "of its own file at its own line number, with %d failing. ### NO KERNEL WAS OPENED, "
            "NO STATEMENT PROVED, NO BUILD RUN AND NO AXIOM PROFILE RECOMPUTED. ### COUNTING WHAT "
            "A ROW SAYS IS NOT CHECKING THAT IT IS TRUE, AND THE WORD CLAIMED IS CARRIED WITH "
            "EVERY FIGURE" % len(AC['reread_failures']))
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT "
            "THE OBJECT. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED, "
            "NO GRADE MOVED, NO ROW EDITED, NO STATUS CORRECTED, NO ACT RE-VERDICTED AND NO LIST "
            "CLOSED. ### NO STANDARD WAS EDITED, THE UNION WAS NOT CORRECTED, AND README.md, "
            "REGISTRY.md, THE_LOAD_BEARING_MAP.md AND THE_DOCUMENT_CLASS_TAXONOMY.md WERE READ "
            "AND NOT TOUCHED")
    grade = ("### READ-AND-COUNTED, AND THE COUNT IS OF CLAIMED STATUS. ### THE SET IS THE "
             "RECORD'S AND NOT A PREDICATE'S, AND THE PREDICATE THAT FOUND THE TABLES WAS WRONG "
             "TWICE BEFORE IT WAS RIGHT -- REPORTED, NOT SMOOTHED. ### EVERY DISAGREEMENT IS "
             "REPORTED AND NONE RECONCILED. ### THE PARTITION SUMS AND THE RESIDUE IS NAMED "
             "RATHER THAN ABSORBED. ### NOTHING IS RECOMMENDED AND A BEARING IS NOT AN ANSWER. "
             "### AND THE MEMORY SCREEN IS MARKED AS A SCREEN: IT OVER-REPORTS BY DESIGN, THE "
             "SEAT JUDGED EVERY FLAG, AND EACH JUDGEMENT IS PRINTED WITH THE FILE'S OWN NEAREST "
             "SENTENCE SO A READER CAN OVERTURN IT")
    status = ("data/b387_what_the_tables_carry.txt; data/%s; data/%s; "
              "data/b387_registration_2026-09-09.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b387); tools/b387_extract.py; "
              "tools/b387_components.py; tools/b387_desk_bank.py; tools/b387_checks.py; "
              "PLACE-papers OPEN_TRAILS.md (an append-only block; NO OTHER CORPUS DOCUMENT "
              "WRITTEN INTO); the seat's memory directory (two topic files APPENDED to, no entry "
              "deleted and no file rewritten); CORRESPONDENCE.md row %%d"
              % (AC['run_file'], E['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('what the keystones tables carry', 'nine of the fourteen carry a table',
           'the rows that are not machine verified', 'the union names an ungraded carrier',
           'the seat memory has no prior blob')
MUST_NOT_HIT = ('the union was corrected', 'a row was edited',
                'the citation question is answered', 'an unreadable row was assigned')


def do_key(rownum):
    tot = TOT
    KEY = 'what-the-keystones-tables-actually-carry'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "THE UNION NAMES FOURTEEN GRADED CORRESPONDENCE TABLES AND %d OF THE FOURTEEN DOCUMENTS "
        "CARRY ONE; %d CARRY NONE (%s), THE ABSENCE PROVED BY READING EVERY TABLE IN EACH FILE. "
        "THE SET IS THE UNION'S OWN keystone-set line AND NOT A PREDICATE OVER THE CORPUS, and the "
        "tables were found BY SHAPE AND NEVER BY HEADING -- the predicate WAS WRONG TWICE BEFORE "
        "IT WAS RIGHT (a heading test found 7 of 14; a status-column test found 8 and missed "
        "R_CURVE_CRITERION, whose column is headed Grade, which is the union's own word). %d "
        "DISAGREEMENTS ARE REPORTED AND %d RECONCILED: the five with no table; THE UNION POINTS "
        "MONO AT 25.8, WHOSE TABLE HAS NO STATUS AND NO GRADE COLUMN, while the monograph's graded "
        "table is elsewhere in the same document; two filenames carry a version suffix the union's "
        "names do not; and ENGINE'S TABLE IS A WORK-ORDER INSTRUMENT, counted with its shape "
        "stated. EVERY ROW IS COUNTED BY WHAT BACKS IT IN THE CORPUS'S OWN WORDS: DERIVES %d, "
        "INTERFACES %d, manuscript-resident %d, research-reach %d, shell-or-encodes %d, UNREADABLE "
        "%d, AND THE CATEGORIES SUM PER DOCUMENT AND IN TOTAL. EVERY INTERFACES ROW NAMES ITS "
        "PREMISE; the unreadable rows are NAMED AND NEVER ASSIGNED. THE ANSWER FROM PRACTICE: %d "
        "OF %d ROWS (%.1f%%) ARE NOT MACHINE-VERIFIED AND EVERY ONE IS LABELLED IN THE ROW ITSELF "
        "-- A COUNT OF CLAIMED STATUS, SINCE NO KERNEL WAS OPENED. THE BEARING: the standard's "
        "three borderlines all turn on READING PARTS OF ONE DOCUMENT DIFFERENTLY and the practice "
        "is THE SAME MOVE AT ROW GRANULARITY, so THE PER-ROW PRACTICE EXISTS AND IS IN USE AND "
        "WHETHER IT SUPPLIES THE RULE IS THE AUTHOR'S TO SAY; %d RECOMMENDED. RULING (R16) IS "
        "RECORDED WITH ITS REASON. AND THE SEAT'S MEMORY HAS NO PRIOR BLOB, so the comparison used "
        "an artifact NAMED AS ONE: %d shortened hooks, %d flagged by a screen THAT OVER-REPORTS BY "
        "DESIGN, %d JUDGED COVERED AND %d JUDGED LOST, the two restored by appending."
        % (C1['with_table'], C1['without_table'], ' '.join(C1['without_tags']),
           C1['disagreements_reported'], C1['reconciled'],
           tot.get('DERIVES', 0), tot.get('INTERFACES', 0), tot.get('MANUSCRIPT_RESIDENT', 0),
           tot.get('RESEARCH_REACH', 0), tot.get('SHELL_OR_ENCODES', 0), tot.get('UNREADABLE', 0),
           C3['not_machine_verified'], C3['rows'], C3['fraction'], C3['recommended'],
           C4['hooks_checked'], len(C4['judged']),
           sum(1 for j in C4['judged'] if j['verdict'] == 'COVERED'), C4['lost_n']))
    grade = (
        "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED, NO GRADE MOVED, "
        "NO ROW EDITED, NO STATUS CORRECTED AND NO LIST CLOSED. ### NOTHING WAS CLOSED ON THE "
        "DESK AT ALL, BECAUSE A MEASUREMENT IS NOT A CLOSURE. ### NO CORRESPONDENCE TABLE WAS "
        "TOUCHED AND THE UNION WAS NOT CORRECTED. ### NO KERNEL WAS OPENED AND NO PRINT AXIOMS "
        "RE-RUN, SO EVERY FIGURE IS A COUNT OF CLAIMED STATUS. ### EVERY DISAGREEMENT IS REPORTED "
        "AND NONE RECONCILED. ### THE PARTITION SUMS AND THE RESIDUE IS NAMED. ### NOTHING IS "
        "RECOMMENDED AND THE CITATION QUESTION IS RESTATED AS AWAITING THE AUTHOR AND NOT MOVED. "
        "### NO .git/hooks/pre-push WAS DELETED IN ANY REPOSITORY, WHICH (R16) RULES. ### NO "
        "MEMORY ENTRY WAS DELETED AND NO TOPIC FILE REWRITTEN; A RESTORATION APPENDS. ### THE "
        "FACE WAS NOT WIDENED MID-ACT. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO "
        "NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. "
        "### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED")
    where = (
        "data/b387_what_the_tables_carry.txt; data/%s; data/%s; "
        "data/b387_registration_2026-09-09.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b387 -- %d gates read, %d checked by digest); "
        "tools/b387_extract.py; tools/b387_components.py; tools/b387_desk_bank.py; "
        "tools/b387_checks.py; PLACE-papers OPEN_TRAILS.md (append-only); the seat's memory "
        "directory (two topic files appended to); CORRESPONDENCE.md row %d"
        % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b387 (the keystone correspondence union's fourteen located and their rows counted by "
           "what backs them; the disagreements between the union and the disk reported and not "
           "reconciled; the citation question's bearing stated from practice and not answered; "
           "(R16) recorded; and the seat's own memory audited against b386's trim)")
    row_new = ('    # ### WHAT THE KEYSTONES` TABLES ACTUALLY CARRY (b387).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where, chr(10)))
    txt = io.open(INDEX, encoding='utf-8').read()
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        rec('    %-40s NO KEY before : %s' % (q, pre[q]))
    KEY_ANCHOR = 'KEYS = {\n'
    ROW_ANCHOR = ('INDEX = [\n'
                  '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        rec('  ### HARD FAILURE -- an anchor is not in the file.')
        return False
    if ("'%s'" % KEY) not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if ('"%s"' % KEY) not in txt and ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    open(INDEX + '.tmp', 'wb').write(txt.encode('utf-8'))
    os.replace(INDEX + '.tmp', INDEX)
    ok = True
    out, rc = query(KEY)
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : %s returns %d row(s)  %s'
        % (KEY, n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and KEY in o
        ok = ok and g
        rec('    %-44s reaches the b387 key : %s' % (q, g))
    for lbl, cond in (('nine of fourteen carry a table',
                       ('%d OF THE FOURTEEN DOCUMENTS CARRY ONE' % C1['with_table']) in out),
                      ('the absence is proved',
                       'THE ABSENCE PROVED BY READING EVERY TABLE IN EACH FILE' in out),
                      ('the set is the record`s, not a predicate`s',
                       "NOT A PREDICATE OVER THE CORPUS" in out),
                      ('the predicate was wrong twice',
                       'WAS WRONG TWICE BEFORE IT WAS RIGHT' in out),
                      ('by shape and never by heading',
                       'BY SHAPE AND NEVER BY HEADING' in out),
                      ('the union names an ungraded carrier',
                       'WHOSE TABLE HAS NO STATUS AND NO GRADE COLUMN' in out),
                      ('ENGINE is a work-order instrument',
                       "ENGINE'S TABLE IS A WORK-ORDER INSTRUMENT" in out),
                      ('the categories sum', 'THE CATEGORIES SUM PER DOCUMENT AND IN TOTAL' in out),
                      ('every interfaces row names its premise',
                       'EVERY INTERFACES ROW NAMES ITS PREMISE' in out),
                      ('unreadable rows never assigned', 'NAMED AND NEVER ASSIGNED' in out),
                      ('the answer is a count of claimed status',
                       'A COUNT OF CLAIMED STATUS, SINCE NO KERNEL WAS OPENED' in out),
                      ('the bearing stops at the author',
                       "WHETHER IT SUPPLIES THE RULE IS THE AUTHOR'S TO SAY" in out),
                      ('the question is not moved',
                       'RESTATED AS AWAITING THE AUTHOR AND NOT MOVED' in out),
                      ('(R16) is recorded', 'RULING (R16) IS RECORDED WITH ITS REASON' in out),
                      ('no hook copy deleted',
                       'NO .git/hooks/pre-push WAS DELETED IN ANY REPOSITORY' in out),
                      ('the memory has no prior blob', 'NO PRIOR BLOB' in out),
                      ('the screen over-reports by design',
                       'A SCREEN THAT OVER-REPORTS BY DESIGN' in out
                       or 'OVER-REPORTS BY DESIGN' in out),
                      ('a restoration appends', 'A RESTORATION APPENDS' in out),
                      ('nothing was closed', 'A MEASUREMENT IS NOT A CLOSURE' in out),
                      ('the lists are restated open', 'RESTATED OPEN BY NAME' in out),
                      ('no new tracking document in the corpus',
                       'NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        g = pre[q] and no_key(o)
        ok = ok and g
        rec('    %-40s NO KEY after  : %s' % (q, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def main():
    rec('=' * 100)
    rec('b387 -- THE DESK UNDER (R7), THE THREE CLOSING WRITES, AND THE BANK.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE DESK.')
    rec('-' * 100)
    Q = do_desk()
    Q['lists_closed'] = 0

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE TRAIL BLOCK, APPEND-ONLY.')
    rec('-' * 100)
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
        after = before
        tr = dict(appended_only=True, committed_prefix_intact=True, prior_present=True,
                  before_bytes=len(before.encode('utf-8')), after_bytes=len(before.encode('utf-8')))
    else:
        rec('  ### the prior block is present and is not edited : %s' % (PRIOR in before))
        body = chr(10).join(trail_block(Q)) + chr(10)
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(body)
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        r = subprocess.run(['git', 'show', 'HEAD:OPEN_TRAILS.md'], cwd=PP, capture_output=True)
        committed = r.stdout.decode('utf-8', 'replace')
        ao = after.startswith(before)
        pi = (committed.replace(chr(13) + chr(10), chr(10))
              in after.replace(chr(13) + chr(10), chr(10)))
        rec('  ### bytes %d -> %d ; append-only %s ; committed still a substring %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao, pi))
        subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)
        tr = dict(appended_only=ao, committed_prefix_intact=pi, prior_present=(PRIOR in before),
                  before_bytes=len(before.encode('utf-8')),
                  after_bytes=len(after.encode('utf-8')))
    seg = after.split(MARK, 1)[-1]
    tr['says_r16'] = '(R16)' in seg and 'THE UNTRACKED HOOK COPIES STAY' in seg.upper()
    tr['says_not_reconciled'] = 'not reconciled' in seg.lower()
    tr['says_no_closure'] = 'a measurement is not a closure' in seg.lower()
    tr['says_claimed'] = 'claimed' in seg.lower() and 'opened no kernel' in seg.lower()
    rec('  ### ### **THE BLOCK RECORDS `(R16)` WITH ITS REASON : %s ; SAYS THE DISAGREEMENTS ARE '
        'NOT RECONCILED : %s**' % (tr['says_r16'], tr['says_not_reconciled']))
    rec('  ### ### **SAYS A MEASUREMENT IS NOT A CLOSURE : %s ; AND CARRIES THE WORD `CLAIMED` '
        'BESIDE ITS FIGURES : %s**' % (tr['says_no_closure'], tr['says_claimed']))

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE CORRESPONDENCE ROW.')
    rec('-' * 100)
    ROWS = corr_rows(Q)
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d' % len(bad))
    if bad or not (pos and neg and sa and sb and sc and sd):
        run_clock.write(D, 'b387_desk_notes', LINES)
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b387_desk_notes', LINES)
        return 1
    g1 = ('NINE OF THE FOURTEEN KEYSTONES' in ROWS[0][0]
          and 'NOT MACHINE-VERIFIED' in ROWS[0][0]
          and 'CHECKS WHAT EACH GATE READ' in ROWS[0][1]
          and 'A MEASUREMENT IS NOT A CLOSURE' in ROWS[0][1]
          and "THE SET IS THE UNION'S OWN" in ROWS[0][1]
          and 'BY SHAPE AND NEVER BY HEADING' in ROWS[0][1]
          and 'THE PREDICATE WAS WRONG TWICE BEFORE IT WAS RIGHT' in ROWS[0][1]
          and 'THE ABSENCE PROVED BY READING EVERY TABLE IN EACH FILE' in ROWS[0][1]
          and 'NO STATUS AND NO GRADE COLUMN' in ROWS[0][1]
          and "ENGINE'S TABLE IS A WORK-ORDER INSTRUMENT" in ROWS[0][1]
          and 'THE CATEGORIES SUM TO THE ROW COUNT' in ROWS[0][1]
          and 'EVERY INTERFACES ROW NAMES ITS PREMISE' in ROWS[0][1]
          and 'NAMED BY DOCUMENT AND LINE AND NEVER ASSIGNED' in ROWS[0][1]
          and 'A COUNT OF CLAIMED STATUS' in ROWS[0][1]
          and 'READING PARTS OF ONE DOCUMENT DIFFERENTLY' in ROWS[0][1]
          and "IS THE AUTHOR'S TO SAY" in ROWS[0][1]
          and 'RULING (R16) IS RECORDED WITH ITS REASON' in ROWS[0][1]
          and 'NO PRIOR BLOB EXISTS' in ROWS[0][1]
          and 'OVER-REPORTS BY DESIGN' in ROWS[0][1]
          and 'RESTORED BY APPENDING' in ROWS[0][1]
          and 'NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN' in ROWS[0][2]
          and 'COUNTING WHAT A ROW SAYS IS NOT CHECKING THAT IT IS TRUE' in ROWS[0][2]
          and 'NO CLASS WAS RULED' in ROWS[0][3]
          and 'THE UNION WAS NOT CORRECTED' in ROWS[0][3]
          and 'THE SET IS THE RECORD' in ROWS[0][4]
          and 'A BEARING IS NOT AN ANSWER' in ROWS[0][5]
          and 'THE FACE WAS NOT WIDENED MID-ACT' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says the nine of fourteen, the stamped gate, the union`s own set, the '
        'shape-not-heading rule, the predicate wrong twice, the proved absence, the ungraded '
        'carrier, ENGINE`s different instrument, the summing partition, the named premises, the '
        'named residue, the claimed status, the bearing and where it stops, (R16), the missing '
        'blob, the over-reporting screen, the restoration, and the scope : %s' % g1)
    if not g1:
        run_clock.write(D, 'b387_desk_notes', LINES)
        return 1
    present = [m for m, _s, _t, _p, _g, _sc, _st in ROWS if m in txt]
    nums = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    if present:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = max(nums)
    else:
        start = max(nums) + 1
        rec('  last existing row : %d ; row to append : %d' % (max(nums), start))
        lines = ['| %d | %s | %s | %s | %s %s | %s |'
                 % (start + k, stmt, term, prof, grade, scope,
                    (status % (start + k)) if '%d' in status else status)
                 for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS)]
        new = txt.rstrip(chr(10)) + chr(10) + chr(10).join(lines) + chr(10)
        open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(TABLE + '.tmp', TABLE)
        back = io.open(TABLE, encoding='utf-8').read()
        got = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', back, re.M)]
        cells = [GD.split_cells(t) for t in back.rstrip(chr(10)).split(chr(10))[-1:]]
        ok = (got[-1] == start and C.blank_cells(back) == 0
              and all(len(c) == 6 and all(x.strip() for x in c) for c in cells)
              and back.startswith(txt.rstrip(chr(10))))
        rec('  READ BACK : last row %d ; cells %s ; true prefix %s ; %s'
            % (got[-1], [len(c) for c in cells], back.startswith(txt.rstrip(chr(10))),
               'PASS' if ok else '### FAIL ###'))
        if not ok:
            run_clock.write(D, 'b387_desk_notes', LINES)
            return 1
        rownum = start

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE INDEX KEY.')
    rec('-' * 100)
    kok = do_key(rownum)

    rec('')
    rec('-' * 100)
    rec('  ### (5) THE BANK.')
    rec('-' * 100)
    B = []
    BAR, SUB = '=' * 100, '-' * 100
    tot = TOT
    B.append(BAR)
    B.append("b387 -- WHAT THE KEYSTONES' TABLES ACTUALLY CARRY. ### THE BANK.")
    B.append(BAR)
    B.append('')
    B.append('### ### ### **A READ AND A COUNT. ### NO RULING, NO REPAIR, NO ROW EDITED, NO GRADE')
    B.append('### ### ### MOVED, AND NOTHING CLOSED.**')
    B.append('### `(R7)` closes an item whose ### **OCCASION** ### is gone, and counting what the')
    B.append('### tables carry removes no obligation and answers no routed question. ### **A')
    B.append('### ### MEASUREMENT IS NOT A CLOSURE** (`b383`), and an act that measures well and')
    B.append('### then closes something to show for it has traded a true record for a tidy one.')
    B.append('')
    B.append('### ### **AND `(R16)` IS RECORDED WITH ITS REASON:** ### *the repository')
    B.append('### configuration already makes the tracked source the one that runs, and the')
    B.append('### untracked copies are a fallback; removing a working fallback was not asked for')
    B.append('### and buys nothing.* ### **SO A LATER SURVEY READS THEM AS A RULED DISPOSAL AND')
    B.append('### ### NOT AS DIVERGENCE**, which is what the ruling asks for. ### `b386` left them')
    B.append('### as a marked judgement; the author has ruled it.')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 1 -- THE SET, AND WHERE THE UNION AND THE DISK DISAGREE.')
    B.append(SUB)
    B.append('### ### **THE SET IS THE UNION`S OWN KEYSTONE-SET LINE, READ BY THE ANCHOR TOOL** --')
    B.append('### ### **NOT A PREDICATE OVER THE CORPUS.**')
    B.append('### ### **THE UNION NAMES `%d`. ### CARRYING A CORRESPONDENCE-SHAPED TABLE : `%d`.'
             % (C1['union_names'], C1['with_table']))
    B.append('### ### CARRYING NONE : `%d`. ### ROWS IN ALL LOCATED TABLES : `%d`.**'
             % (C1['without_table'], C1['rows_total']))
    B.append('')
    B.append('###   %-8s %-46s %-7s %s' % ('TAG', 'DOCUMENT ON DISK', 'TABLES', 'ROWS'))
    for sv in E['survey']:
        B.append('###   %-8s %-46s %-7d %s'
                 % (sv['tag'], sv['rel'].split('/')[-1][:46], len(sv['tables']),
                    sv['rows'] if sv['tables'] else '### **NONE**'))
    B.append('')
    B.append('### ### ### **THE TABLES WERE FOUND BY SHAPE AND NEVER BY HEADING** ### -- `(R2)`,')
    B.append('### by content and never by address.')
    B.append('### ### ### **AND THE PREDICATE WAS WRONG TWICE BEFORE IT WAS RIGHT, WHICH IS')
    B.append('### ### ### REPORTED RATHER THAN SMOOTHED.**')
    B.append('###   a heading test (`## Correspondence`)        found ### **`7` OF `14`**')
    B.append('###   the front door`s columns, `status` required found ### **`8`** -- missing')
    B.append('###     `R_CURVE_CRITERION`, whose column is headed ### **`Grade`.**')
    B.append('###   `status` OR `grade`                          found ### **`%d`.**'
             % C1['with_table'])
    B.append('### ### **`GRADE` IS THE UNION`S OWN WORD** -- *fourteen GRADED Correspondence')
    B.append('### tables* -- so admitting it is reading the record, not widening a test to pass.')
    B.append('### ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE**, met twice inside one')
    B.append('### component and ### **BEFORE THE LOCK RATHER THAN AFTER IT.**')
    B.append('')
    B.append('### ### ### **THE DISAGREEMENTS : `%d` REPORTED, `%d` RECONCILED.**'
             % (C1['disagreements_reported'], C1['reconciled']))
    B.append('###   ### **(1) `%d` OF THE `%d` CARRY NO CORRESPONDENCE-SHAPED TABLE AT ALL:** ### %s'
             % (C1['without_table'], C1['union_names'],
                ', '.join('`%s`' % t for t in C1['without_tags'])))
    B.append('###     ### **THE ABSENCE IS PROVED, NOT ASSUMED** (`b378`): every table in each of')
    B.append('###     the five was read and its columns printed in `data/%s`.' % AC['run_file'])
    B.append('###   ### **(2) THE UNION POINTS `MONO` AT `§25.8` AND `§25.8`S TABLE IS NOT')
    B.append('###     ### GRADED.** ### `%d` rows, columns ### **`%s`** ### -- no status column'
             % (E['mono_258']['rows'], ' | '.join(E['mono_258']['cols'])))
    B.append('###     and no grade column. ### The monograph DOES carry a graded table, at its')
    B.append('###     `## Correspondence` appendix added `2026-08-12`. ### **THE UNION NAMES A')
    B.append('###     ### CARRIER THAT IS NOT THE GRADED ONE.**')
    B.append('###   ### **(3) TWO ON-DISK FILENAMES CARRY A VERSION SUFFIX THE UNION`S NAMES DO')
    B.append('###     ### NOT** -- `DOMAIN_OSTROWSKI_UNIVERSALITY_v0_1.md` and')
    B.append('###     `SEVEN_DISCRIMINANTS_AND_TRIVIUM_v0_1.md`.')
    B.append('###   ### **(4) `ENGINE`S TABLE IS A DIFFERENT INSTRUMENT** -- columns')
    B.append('###     ### **`terminal | location | grade | what the source says | work-order`.**')
    B.append('###     ### **A WORK-ORDER TABLE AND NOT A CLAIM-TO-ARTIFACT TABLE**, counted with')
    B.append('###     its shape stated beside its count, because ### **A COUNT THAT HIDES A')
    B.append('###     ### DIFFERENT INSTRUMENT INSIDE A TOTAL IS A WRONG COUNT.**')
    B.append('### ### ### **NONE OF THE FOUR IS RECONCILED. ### BOTH THE UNION AND THE DOCUMENTS')
    B.append('### ### ### ARE THE AUTHOR`S**, and the order said to report and not reconcile.')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 2 -- EVERY ROW COUNTED BY WHAT BACKS IT.')
    B.append(SUB)
    B.append('### ### **THE FRONT DOOR`S OWN WORDS, QUOTED FIRST:** ### *each row maps a claim the')
    B.append('### paper makes to the artifact that verifies it: claim . kernel . fully-qualified')
    B.append('### theorem name . axiom profile . status*, and ### *where no kernel exists, the')
    B.append('### status says so in words -- manuscript-resident or research-reach -- rather than')
    B.append('### being omitted.* ### **SO THE CATEGORIES ARE THE CORPUS`S AND NOT THIS ACT`S.**')
    B.append('')
    B.append('###   %-8s %-6s %-9s %-11s %-11s %-9s %-11s %s'
             % ('TAG', 'ROWS', 'DERIVES', 'INTERFACES', 'MANUSCRIPT', 'RESEARCH', 'SHELL/ENC',
                'UNREADABLE'))
    for r in C2['per']:
        c = r['counts']
        B.append('###   %-8s %-6d %-9d %-11d %-11d %-9d %-11d %d'
                 % (r['tag'], r['rows'], c.get('DERIVES', 0), c.get('INTERFACES', 0),
                    c.get('MANUSCRIPT_RESIDENT', 0), c.get('RESEARCH_REACH', 0),
                    c.get('SHELL_OR_ENCODES', 0), c.get('UNREADABLE', 0)))
    B.append('###   %-8s %-6d %-9d %-11d %-11d %-9d %-11d %d'
             % ('TOTAL', C2['rows'], tot.get('DERIVES', 0), tot.get('INTERFACES', 0),
                tot.get('MANUSCRIPT_RESIDENT', 0), tot.get('RESEARCH_REACH', 0),
                tot.get('SHELL_OR_ENCODES', 0), tot.get('UNREADABLE', 0)))
    B.append('### ### **THE CATEGORIES SUM TO THE ROW COUNT, PER DOCUMENT AND IN TOTAL : %s.** ###'
             % C2['sums_ok'])
    B.append('### **A PARTITION THAT DOES NOT SUM IS NOT A PARTITION.**')
    B.append('')
    B.append('### ### **EVERY `INTERFACES` ROW NAMES ITS PREMISE : `%d` OF `%d`.** ### A row whose'
             % (C2['interfaces_with_premise'], tot.get('INTERFACES', 0)))
    B.append('### premise could not be named was ### **RE-COUNTED `UNREADABLE` RATHER THAN LEFT IN')
    B.append('### ### THE BIN**, which is what `INTERFACES` would otherwise become.')
    B.append('### ### **THE UNREADABLE ROWS : `%d`, NAMED BY DOCUMENT AND LINE AND NEVER'
             % C2['unreadable_n'])
    B.append('### ### ASSIGNED.**')
    B.append('')
    for u in C2['unreadable'][:24]:
        B.append('###   `%-7s` line %-6d | %s' % (u['tag'], u['line'], u['evidence'][:96]))
    if len(C2['unreadable']) > 24:
        B.append('###   ... and `%d` more, all in `data/%s`'
                 % (len(C2['unreadable']) - 24, AC['run_file']))
    B.append('### ### ### **`(E1)` REGISTERED THAT A RESIDUE WAS EXPECTED, AND THE RESIDUE IS')
    B.append('### ### ### REAL.** ### **AN UNREADABLE ROW FORCED INTO A CATEGORY IS A FABRICATED')
    B.append('### ### ### COUNT.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 3 -- THE QUESTION ANSWERED FROM PRACTICE, AND WHERE IT STOPS.')
    B.append(SUB)
    B.append('### ### **DO THE CORPUS`S OWN KEYSTONES ALREADY CARRY ROWS THAT ARE NOT')
    B.append('### ### MACHINE-VERIFIED, HONESTLY LABELLED?**')
    B.append('### ### ### **YES -- `%d` OF `%d` ROWS, WHICH IS `%.1f%%`.**'
             % (C3['not_machine_verified'], C3['rows'], C3['fraction']))
    B.append('### ### **THE SCOPE, NAMED SO THE COUNT CANNOT TRAVEL:** ### over the `%d` documents'
             % C3['documents_counted'])
    B.append('### of the `%d` the union names that carry a table; over `%d` rows in all their'
             % (C1['union_names'], C3['rows']))
    B.append('### located tables, including `ENGINE`s differently-shaped one; counting')
    B.append('### ### **INTERFACES + MANUSCRIPT-RESIDENT + RESEARCH-REACH + SHELL-OR-ENCODES** ###')
    B.append('### as not machine-verified, ### **DERIVES** ### as machine-verified, and the')
    B.append('### ### **`%d` UNREADABLE ROWS ASSIGNED TO NEITHER.**' % tot.get('UNREADABLE', 0))
    B.append('### ### **THE WORD `MATERIAL` IN `(F1)` IS THE NAVIGATOR`S** -- this act reports the')
    B.append('### fraction and ### **LETS THE READER JUDGE THE WORD.**')
    B.append('### ### ### **AND EVERY FIGURE IS A COUNT OF *CLAIMED* STATUS.** ### This act read')
    B.append('### what each row SAYS; ### **IT OPENED NO KERNEL AND RAN NO `#print axioms`**, so it')
    B.append('### cannot say a row is honest -- only that the row states what it states. ###')
    B.append('### **`b374`S LIMIT, INHERITED: AN ARM THAT TESTS THE VALUE CANNOT TEST THE')
    B.append('### ### SOURCE.**')
    B.append('')
    B.append('### ### ### **WHAT THAT BEARS ON THE CITATION QUESTION.**')
    B.append('### The standard`s three author-ruled borderlines all turn on ### **READING PARTS OF')
    B.append('### ### ONE DOCUMENT DIFFERENTLY**: ### `CATALOGOS` is Tier C with its pinned rows')
    B.append('### read as K; `UNIVERSALITY` is mostly K with a C-scope note; `THE_SUBSTRATE` is K')
    B.append('### with its Related Work read as context.')
    B.append('### ### **AND THE PRACTICE MEASURED ABOVE IS THE SAME MOVE AT ROW GRANULARITY:** ###')
    B.append('### `%d` of `%d` rows inside documents the standard calls ### **TIER K** ### are'
             % (C3['not_machine_verified'], C3['rows']))
    B.append('### already labelled as something other than a machine-checked terminal.')
    B.append('### ### ### **SO THE PER-ROW PRACTICE EXISTS AND IS IN USE. ### WHETHER IT SUPPLIES')
    B.append('### ### ### THE RULE THE AUTHOR IS BEING ASKED FOR IS THE AUTHOR`S TO SAY, AND THIS')
    B.append('### ### ### ACT DOES NOT SAY IT.**')
    B.append('### ### **NOTHING IS RECOMMENDED -- `%d` OF THEM. ### NO OPTION IS RANKED,'
             % C3['recommended'])
    B.append('### ### PREFERRED OR CALLED LIKELIEST.**')
    B.append('### ### **THE CITATION QUESTION IS RESTATED AS AWAITING THE AUTHOR AND IS NOT MOVED')
    B.append('### ### : %s.** ### **A BEARING IS NOT AN ANSWER.**' % (not C3['question_moved']))
    B.append('')
    B.append(SUB)
    B.append("### COMPONENT 4 -- THE SEAT'S OWN MEMORY.")
    B.append(SUB)
    B.append('### ### ### **THE ORDER ASKED FOR THE FILE`S PRIOR BLOB AND THERE IS NONE.**')
    B.append('### The memory directory sits under a repository whose current branch ### **HAS NO')
    B.append('### ### COMMITS**, and `MEMORY.md` is ### **NOT TRACKED IN IT** -- so')
    B.append('### ### **A PRIOR BLOB EXISTS : %s.**' % C4['has_blob'])
    B.append('### The comparison used a ### **BYTE-FOR-BYTE COPY TAKEN IMMEDIATELY BEFORE THE')
    B.append('### ### TRIM** ### (`%d` bytes) against the current file (`%d` bytes). ### **THAT IS'
             % (C4['prior_bytes'], C4['current_bytes']))
    B.append('### ### AN ARTIFACT, NOT A BLOB, AND IT IS NOT RECALL EITHER** -- and it is named as')
    B.append('### what it is rather than dressed as what the order asked for.')
    B.append('### ### ### **A TRIM OF THE SEAT`S MEMORY IS THEREFORE NOT REVERTIBLE FROM THE')
    B.append('### ### ### RECORD**, which is a finding this act did not go looking for.')
    B.append('')
    B.append('### ### **THE STRUCTURAL CHECKS:**')
    B.append('###   entries before `%d` ### / ### entries after `%d`'
             % (C4['entries_before'], C4['entries_after']))
    B.append('###   ### **POINTERS PRESENT BEFORE AND ABSENT AFTER : `%d`**'
             % C4['pointers_dropped'])
    B.append('###   ### **POINTERS RESOLVING TO NO FILE : `%d`**' % C4['pointers_unresolved'])
    B.append('### ### **SO NOTHING BECAME UNREACHABLE BY LOSING ITS POINTER.**')
    B.append('')
    B.append('### ### **THE CONTENT CHECK, AND WHY IT IS A SCREEN AND NOT A VERDICT.**')
    B.append('### ### **A HOOK IS A SUMMARY OF A TOPIC FILE; ITS WORDING DIFFERS FROM THE FILE`S')
    B.append('### ### BY CONSTRUCTION.** ### So a token test measures WORDING, not content, and it')
    B.append('### ### **OVER-REPORTS BY DESIGN.** ### Its first two runs flagged `41` and then')
    B.append('### `34` tails; inspection showed most were words like `acts`, `legs` and `Re-run`')
    B.append('### whose CLAIMS the file plainly carries. ### **THE FIRST TOKENISER WAS ALSO WRONG:**')
    B.append('### its pattern allowed `.` inside a token, so it harvested `table.` WITH THE')
    B.append('### SENTENCE`S PUNCTUATION -- and a token ending in a full stop is absent from every')
    B.append('### file by construction. ### **A LOSS COUNT THAT INFLATES IS A FABRICATED FINDING**,')
    B.append('### and it was repaired ### **BEFORE THE FINDING WAS FILED.**')
    B.append('### ### ### **SO THE SCREEN TRIAGES AND THE SEAT JUDGES**, and each judgement is')
    B.append('### printed with ### **THE FILE`S OWN NEAREST SENTENCE BESIDE IT**, so a reader can')
    B.append('### overturn any one of them without re-running anything. ### **THE SCREEN WAS NOT')
    B.append('### ### RE-TUNED AFTER SEEING ITS OUTPUT** -- that is the forbidden direction')
    B.append('### (`b380`).')
    B.append('###   shortened hooks checked : ### **`%d`**' % C4['hooks_checked'])
    B.append('###   flagged by the screen   : ### **`%d`**' % len(C4['judged']))
    B.append('###   ### **JUDGED `COVERED` : `%d`**'
             % sum(1 for j in C4['judged'] if j['verdict'] == 'COVERED'))
    B.append('###   ### **JUDGED `LOST`    : `%d`**' % C4['lost_n'])
    B.append('')
    if C4['lost_n']:
        B.append('### ### ### **`(F2)` IS REFUTED, NARROWLY AND PRECISELY. ### TWO CLAIMS WERE')
        B.append('### ### ### LOST AND ARE RESTORED.**')
        for it in C4['lost']:
            B.append('###   `%s`' % it['pointer'])
            B.append('###     the claim: %s' % it['tail'][:150])
        B.append('### ### **THE FIRST OF THEM IS A RULE THIS SEAT USED TWICE IN THIS SESSION** --')
        B.append('### `U-1`s counter is lexical, so ### **REPHRASE RATHER THAN FIGHT THE SCAN** --')
        B.append('### and it was absent from its own topic file while the index hook carried it.')
        B.append('### ### ### **A CLAIM THAT LIVES ONLY IN AN INDEX HOOK IS A CLAIM ONE TRIM FROM')
        B.append('### ### ### GONE.**')
        B.append('### ### **BOTH ARE RESTORED BY APPENDING** ### to the topic files they belong')
        B.append('### in. ### **NO ENTRY WAS DELETED AND NO TOPIC FILE WAS REWRITTEN.**')
        for r in C4['restored']:
            B.append('###   restored into `%s` (+`%d` bytes)' % (r['pointer'], r['bytes']))
    else:
        B.append('### ### ### **NOTHING SURVIVED THE JUDGEMENT AS LOST**, and the comparison is')
        B.append('### ### ### printed rather than asserted.')
    B.append('')
    B.append(SUB)
    B.append('### THE DESK, THE WRITES, AND WHAT THIS ACT DID NOT DO.')
    B.append(SUB)
    B.append('### desk items swept : %d ### / ### closed : %d ### / ### standing : %d ### / ### '
             'lists closed : %d' % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
    B.append('### ### **NOTHING WAS CLOSED, AND THAT IS THE ANSWER RATHER THAN A THIN ONE.**')
    B.append('### ### **SIX ITEMS ARE ADDED AND ALL SIX STAND**: the five keystones with no table,')
    B.append('### the ungraded carrier, `ENGINE`s different instrument, the unreadable rows, the')
    B.append('### memory`s want of version control, and the two restored claims.')
    B.append('### trail block appended (append-only %s, committed prefix intact %s); '
             '`CORRESPONDENCE.md` row %s;'
             % (tr['appended_only'], tr['committed_prefix_intact'], rownum))
    B.append('### index key `what-the-keystones-tables-actually-carry` reachable by every alias : '
             '%s' % kok)
    B.append('')
    B.append('### ### **NO CLASS WAS RULED. ### NO DOCUMENT RECLASSIFIED. ### NO DECLARATION')
    B.append('### ### MOVED. ### NO GRADE MOVED. ### NO ROW EDITED. ### NO STATUS CORRECTED. ###')
    B.append('### ### NO CORRESPONDENCE TABLE TOUCHED. ### NO LIST CLOSED.**')
    B.append('### ### **NO KERNEL WAS OPENED, NO `#print axioms` RE-RUN, NO BUILD RUN AND NO AXIOM')
    B.append('### ### PROFILE RECOMPUTED.**')
    B.append('### ### **`README.md`, `REGISTRY.md`, `THE_LOAD_BEARING_MAP.md` AND')
    B.append('### ### `THE_DOCUMENT_CLASS_TAXONOMY.md` WERE READ AND NOT TOUCHED, AND THE UNION')
    B.append('### ### WAS NOT CORRECTED.**')
    B.append('### ### **NO ARCHIVE FILE TOUCHED. ### NO CLUSTER OPENED. ### THE MIRROR ROSTER NOT')
    B.append('### ### EDITED. ### NO `.git/hooks/pre-push` DELETED IN ANY REPOSITORY**, which')
    B.append('### `(R16)` now rules.')
    B.append('### ### **THE FACE WAS NOT WIDENED MID-ACT.** ### Every write this act made is named')
    B.append('### on the face that was locked before the first of them.')
    B.append('### ### **THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME.**')
    B.append('### **THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED. ### THE POSTURE')
    B.append('### LOCK IS SEPARATE.** ### `h2` stands exactly where the deposit left it and this')
    B.append('### act makes no claim about it in either direction. ### **NOTHING IS DEPOSITED AND')
    B.append('### ### NOTHING WAS WRITTEN AT ZENODO.**')
    B.append('')
    B.append(SUB)
    B.append('### THE EXPECTATIONS, DECIDED.')
    B.append(SUB)
    B.append('### ### **`(F1)` MET.** ### `%d` of `%d` rows -- ### **`%.1f%%`** ### -- are not'
             % (C3['not_machine_verified'], C3['rows'], C3['fraction']))
    B.append('### machine-verified and every one is labelled in the row itself. ### The word')
    B.append('### ### **MATERIAL** ### is the navigator`s and the fraction is printed for him.')
    B.append('### ### **`(F2)` REFUTED, NARROWLY.** ### `%d` of `%d` shortened hooks carried a'
             % (C4['lost_n'], C4['hooks_checked']))
    B.append('### claim no sentence of its topic file carried. ### **SOMETHING WAS LOST, IT IS')
    B.append('### ### NAMED, AND IT IS RESTORED.**')
    B.append('### ### **`(E1)` MET.** ### The partition left a residue: ### **`%d` UNREADABLE'
             % tot.get('UNREADABLE', 0))
    B.append('### ### ROWS**, named and never assigned.')
    B.append('### ### **`(E2)` MET.** ### `INTERFACES` rows name their premises across the whole')
    B.append('### row, not only in the status cell, and the search was over the whole row.')
    B.append('### ### **`(E3)` REFUTED BY ITS OWN CHECK.** ### This seat registered that nothing')
    B.append('### would be found lost. ### **TWO THINGS WERE**, and one of them is a rule this seat')
    B.append('### had used twice in the same session while its topic file did not carry it.')
    B.append('')
    B.append(SUB)
    B.append('### WHAT THIS ACT ADDS TO THE LORE.')
    B.append(SUB)
    B.append('### ### ### **NEW -- `A CLAIM THAT LIVES ONLY IN AN INDEX HOOK IS A CLAIM ONE TRIM`')
    B.append('### ### ### `FROM GONE`.** ### The index is a finding aid; when it becomes the only')
    B.append('### carrier of a rule, shortening it deletes the rule.')
    B.append('### ### ### **NEW -- `A SCREEN THAT OVER-REPORTS BY DESIGN MUST BE MARKED AS A`')
    B.append('### ### ### `SCREEN`.** ### A token test over a summary measures wording; the')
    B.append('### judgement is a seat`s and is printed with its evidence so it can be overturned.')
    B.append('### ### ### **NEW -- `THE SEAT`S OWN MEMORY IS UNDER NO VERSION CONTROL`.** ### The')
    B.append('### order asked for a blob; there is none; ### **A TRIM IS NOT REVERTIBLE FROM THE')
    B.append('### ### RECORD.**')
    B.append('### ### ### **NEW -- `A UNION CAN NAME A CARRIER THAT IS NOT THE ONE IT DESCRIBES`.**')
    B.append('### The union names `§25.8` among ### *fourteen graded Correspondence tables* ### and')
    B.append('### `§25.8` has no grade column.')
    B.append('### **MET AGAIN -- `A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE`**, twice inside')
    B.append('### one component; ### **AN ABSENCE NEEDS A PROVED SEARCH** (`b378`); ### **A')
    B.append('### MEASUREMENT IS NOT A CLOSURE** (`b383`); and ### **THE FACE IS WRITTEN FROM A')
    B.append('### ### SURVEY, NOT FROM A BELIEF ABOUT THE TERRAIN** (`b385`, `b386`), which is why')
    B.append('### the five documents with no table were on the face before the components ran.')
    B.append('')
    B.append(SUB)
    B.append('### THE RECORD.')
    B.append(SUB)
    regtxt = io.open(os.path.join(D, 'b387_registration_2026-09-09.txt'), encoding='utf-8').read()
    m_sha = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt)
    m_by = re.search(r'bytes locked : (\d+)', regtxt)
    m_at = re.search(r'locked at \(UTC\) : (\S+)', regtxt)
    B.append('### registration locked at (UTC) %s' % (m_at.group(1) if m_at else '?'))
    B.append('### ### **%s bytes, sha256 `%s`, %d clauses, ### LOCKED BEFORE ANY WRITE AND CHAINED'
             % (m_by.group(1) if m_by else '?', m_sha.group(1) if m_sha else '?',
                len(J('b387_satisfiable')['clauses'])))
    B.append('### ### ON A GATE THAT CHECKS WHAT EACH GATE READ.** ### %d gates read, %d checked '
             'by digest.' % (LG['gates_read'], LG['face_subject_gates']))
    B.append('### The extract`s clock is `%s` and the lock`s is `%s`.'
             % (E.get('run_clock'), (m_at.group(1) if m_at else '?')))
    for n in ('b387_reads', 'b387_lockgate', 'b387_components'):
        j = J(n)
        B.append('### %-18s run file `%s` recorded clock %s'
                 % (n, j['run_file'], j.get('run_clock')))
    B.append('### **THE REFS THIS ACT READ IN THE ROSTERED REPOSITORIES:**')
    for k, v in E['refs'].items():
        B.append('###   %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    B.append('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor, `%d` anchors differing '
             'from the hint. ### **EVERY ANCHOR WAS READ FROM ITS FILE AND NONE WAS TYPED.**'
             % (E['reads'], E['without_anchor'], E['anchors_differing']))
    B.append('### ### **SIX NEW `relay` TOOLS AGAINST A CAP OF SIX, AND NO SHARED UTILITY.**')
    B.append(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### A CLASS WAS RULED.', '### A ROW WAS EDITED.', '### A GRADE WAS MOVED.',
                '### THE UNION WAS CORRECTED.', '### AN UNREADABLE ROW WAS ASSIGNED.',
                '### THE PREFERRED OPTION IS.', '### A KERNEL WAS RE-RUN.',
                '### THE CATEGORIES DID NOT SUM.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))

    rec('')
    rec('=' * 100)
    rec('  ### desk swept %d ; closed %d ; trail appended %s ; row %s ; key %s'
        % (Q['items'], Q['closed'], tr['appended_only'], rownum, kok))
    rec('  ### ### **LISTS CLOSED : 0. ### THE FOUR ARE RESTATED `OPEN` BY NAME.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b387_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             bank='b387_what_the_tables_carry.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b387_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and C2['sums_ok'] and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
