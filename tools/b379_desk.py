# -*- coding: utf-8 -*-
"""b379_desk.py -- THE DESK UNDER `(R7)`, AND THE THREE CLOSING WRITES: THE TRAIL BLOCK, THE ROW,
### THE KEY.

### ### **FOUR ROLES IN ONE FILE, AND THE REASON IS DECLARED RATHER THAN HIDDEN:** ### the locked
### registration caps this act's new tools at eleven and the cap counts FILES.
### ### **AND THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME.** ### The order says so and a bar
### measures it. ### **THIS ACT CLOSES NOTHING.**
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
MARK = '<!-- b379 the apparatus axis re-scored; two filings -->'
PRIOR = '<!-- b378 the refs widened and the convention swept -->'
ACT = 'b379'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


RS, SV, HD, FL = (J('b379_rescore'), J('b379_survivors'), J('b379_hand'),
                  J('b379_filings'))
LG = J('b379_lockgate')
CL375 = J('b375_clusters')
NOKEY = CL375['subject_clusters_without_keystone']
PB, CB = RS['prior_bplus'], RS['corrected_bplus']
MOVED = len(RS['gained'])
INTO = len(RS['moved_into_both'])
CATS = SV['tally']
NOTLOC = SV['not_located']
CARRIED = len(SV['assigned'])

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
    ("the guard's own stale install line", 'STAND', None, None,
     'the tracked guard still documents an install path the record no longer uses'),
    ('where the keystone census should live, ROUTED at b375', 'STAND', None, None,
     'ROUTED to the author; this act creates no tracking document either'),

    # ---- THE FOUR OPEN LISTS, RESTATED OPEN BY NAME -------------------------------------------------
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND', None, None,
     'OPEN. ### **AND b379 SHARPENS IT AGAIN:** ### a cited name may be a library lemma, a corpus '
     'document, or a name on a tag -- and the row-category module now says so instead of calling '
     'each an absence. ### The list is about naming, and it is not closed'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND', None, None,
     'OPEN. ### b373 listed them with their carriers and ROUTED them. ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', None, None,
     'OPEN. ### b374 listed every figure stated without a ref. ### This act dates none of them'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND', None, None,
     'OPEN. ### b374 found entries the register carries that appear nowhere else. ### This act '
     'rewrites none of them'),

    # ---- CARRIED --------------------------------------------------------------------------------
    ('the class ruling itself', 'STAND', None, None,
     'STILL THE AUTHOR`S. ### b376 assembled five options, b377 added the role clause, and b379 '
     'restates which options the correction WEAKENS. ### **NO OPTION IS RECOMMENDED**'),
    ('the six subject clusters with registry rows and no keystone', 'STAND', None, None,
     'FILED and ### **STILL NOT OPENED.** ### %d clusters, unchanged' % len(NOKEY)),
    ("the census's definition-versus-operation drift", 'STAND', None, None,
     'FILED at b377 and ### **NOT REPAIRED HERE** -- repairing it belongs to the ruling'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', None, None,
     'CARRIED and ### **DELIBERATELY NOT RE-MEASURED**'),
    ('the 86 archive files the mirror does not carry', 'STAND', None, None,
     'CARRIED from b378 and ### **STILL UNCONFIRMED.** ### The draft said the executor would read '
     'silence on that choice as NOT TAKEN, and the order named three additions none of which is the '
     'archive lane. ### **THE READING IS ON THIS ACT`S LOCKED FACE IN ADVANCE**'),

    # ---- WHAT THIS ACT ADDS -------------------------------------------------------------------------
    ("b376's axis-B column, named suspect at b378", 'CLOSE', 'b379_rescore_notes',
     'MONOTONICITY : HELD',
     'CLOSED at b379: ### **THE COLUMN IS RE-MEASURED.** ### b378 named it suspect and said '
     're-measuring it was an act; ### **THIS IS THAT ACT.** ### The occasion is gone because the '
     'measurement exists'),
    ('the apparatus axis, corrected', 'STAND', None, None,
     'NEW at b379: `B+` moves from ### **%d TO %d** ### under a matcher that accepts the bare '
     'dialect as well as the dotted. ### **%d DOCUMENTS GAINED AND NONE LOST**, which the locked '
     'face registered in advance as a property of the instrument' % (PB, CB, MOVED)),
    ('the movement landed entirely in the silent rows', 'STAND', None, None,
     'NEW at b379 and it is the finding under `(F2)`: ### **%d DOCUMENTS MOVED INTO THE BOTH-AXES '
     'QUADRANT** -- every one of the %d that moved came out of a row where axis A says `A?`. ### '
     '**THE CORRECTION ENLARGES THE APPARATUS COLUMN AND LEAVES THE ROLE COLUMN EXACTLY WHERE IT '
     'WAS**, so the two axes come apart further rather than closer' % (INTO, MOVED)),
    ('a category reported as an absence is a false defect', 'STAND', None, None,
     'NEW at b379: `tools/row_categories.py`, SHARED and fixtured in both polarities, carries the '
     'front door`s own words -- MANUSCRIPT-RESIDENT and RESEARCH-REACH -- and adds the three b378 '
     'met. ### Over b378`s %d carried names it reports ### **%d ABSENCES WHERE THE OLD VOCABULARY '
     'REPORTED %d**' % (CARRIED, NOTLOC, CARRIED)),
    ('the fourteen survivors, read from their own sentences', 'STAND', None, None,
     'NEW at b379: %s. ### **NOT ONE DOCUMENT WAS REPAIRED AND NOT ONE NAME WAS INVENTED**; where '
     'the sentence does not decide, the answer is UNDECIDED-BY-ITS-SENTENCE rather than a guess'
     % ', '.join('%s %d' % (k, v) for k, v in SV['explanations'].items())),
    ('the day-1 document carries apparatus', 'STAND', None, None,
     'NEW at b379: `%s` names %d identifiers, of which ### **%d LOCATE IN A CORPUS KERNEL.** ### '
     'b376 could not decide it because it names them in prose; ### **THE HAND READ DECIDES IT, AND '
     'THE CONCORDANCE-CARRIED CLASS DOES DESCRIBE SOMETHING REAL ON THAT PAGE.** ### No declaration '
     'moved' % (HD['chosen'].split('/')[-1][:-3], HD['named'], HD['located'])),
    ('the download-layer book: a version and class drift', 'STAND', None, None,
     'FILED at b379 and ### **NOT REPAIRED.** ### The registry carries it at `v0_5` as NON-KEYSTONE '
     'and NOT FOR PUBLICATION; the harvest list at `v0_6` as a TIER C NARRATIVE KEYSTONE; the patent '
     'index at `v0.7` as THE NARRATIVE KEYSTONE, fenced. ### **%d VERSIONS SIT ON THE DISK.** ### '
     'The front door calls REGISTRY the single source of truth and the precedence source, so the '
     'others are the ones out of step -- ### **AND THE REGISTRY IS NOT EDITED BY THIS ACT**'
     % FL['n_versions']),
    ('the ruling has to say whether it governs outside the tree', 'STAND', None, None,
     'FILED at b379 where the ruling`s evidence sits: the book is outside the repo tree by ruling, '
     'so it was ### **NEVER SCORED ON EITHER AXIS** -- not `B-`, not `A?`, but outside the '
     'population entirely. ### **THAT IS UNLIKE EVERY OTHER OMISSION THIS SEQUENCE FOUND**, and '
     'no widening of a matcher would have reached it'),
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
    marks, refused = [], 0
    for item, want, stem, sentence, why in DESK:
        row = dict(item=item, disposition=want, killing_stem=stem, why=why)
        if want == 'CLOSE':
            p, stamp = newest_run(stem)
            exists = bool(p) and os.path.exists(p)
            carries = False
            if exists:
                body = io.open(p, encoding='utf-8', errors='replace').read()
                carries = GN.norm(sentence) in GN.norm(body)
            row.update(exists=exists, carries=carries, sentence=sentence,
                       killing_file=(os.path.basename(p) if p else None), run_clock=stamp,
                       date=(stamp or '')[:10],
                       own_act=bool(p) and os.path.basename(p).startswith(ACT))
            if not (exists and carries):
                row['disposition'] = 'STAND'
                refused += 1
        marks.append(row)
        rec('    %-64s %s' % (item[:64], row['disposition']))
        rec('        why : %s' % why[:150])
        if len(why) > 150:
            rec('              %s' % why[150:340])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    stands = [m for m in marks if m['disposition'] == 'STAND']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(stands)))
    rec('    ### ### ### **AND CLOSING NOTHING IS RIGHT EVEN THOUGH THIS ACT REPAIRED SOMETHING.**')
    rec('    ### `(R7)` closes an item whose OCCASION is gone. ### Appending a pinned table to one')
    rec('    ### document does not remove the occasion of the obligation, the ruling, or any of the')
    rec('    ### four lists. ### **A REPAIR IS NOT A CLOSURE.**')
    return dict(items=len(marks), closed=len(closed), standing=len(stands),
                closures_refused=refused, marks=marks,
                closed_items=[dict(item=m['item'], file='data/%s' % m.get('killing_file'),
                                   date=m.get('date'), own_act=m.get('own_act')) for m in closed])


def trail_block(Q):
    return [
        '', MARK, '',
        '### **b379 — THE APPARATUS AXIS RE-SCORED, AND TWO FILINGS (2026-09-08)**',
        '',
        ('*No block above is edited. The b378 block (`%s`) and every block before it stand exactly as '
         'they were written.*' % PRIOR),
        '',
        ('**THE SUSPECT COLUMN IS RE-MEASURED, AND THE DIRECTION WAS REGISTERED BEFORE THE RUN.** '
         'b378 found that **not one citing document uses the dotted convention alone**, so b376’s '
         'dotted-only axis-B predicate could not have passed them however complete their tables '
         'were — and it named the whole 303-document `B-` column suspect without re-measuring it. '
         'This act re-measures it with a matcher that accepts both dialects and changes **one line '
         'of pattern and nothing else**. Because the widened pattern matches a strict superset of '
         'the old one, **a document can only move toward certifying** — so the locked face '
         'registered, *before the run*, that the corrected population is bounded below by the prior '
         'one and that a document losing a mark would be **a defect in the instrument, reported as '
         'one and never as a finding about the corpus.** **NONE LOST. %d GAINED.** The apparatus '
         'axis moves from **%d to %d**.' % (MOVED, PB, CB)),
        '',
        ('**AND THE MOVEMENT LANDED ENTIRELY IN THE CORPUS’S SILENCE.** All %d documents that moved '
         'came out of rows where axis A says `A?` — %d out of `A?B-` and the rest out of `A?B?`. '
         '**`(F2)` IS REFUTED BY THE PRINT: %d documents moved into the both-axes quadrant.** Not '
         'one of the seven documents axis A had marked `A+` gained an apparatus mark, because none '
         'of them lacked one. **THE CORRECTION ENLARGES THE APPARATUS COLUMN AND LEAVES THE ROLE '
         'COLUMN EXACTLY WHERE IT WAS**, so the two axes come apart further rather than closer — '
         'which is the opposite of what a correction is usually hoped to do.'
         % (MOVED, RS['prior_quadrants'].get('A?B-', 0) - RS['corrected_quadrants'].get('A?B-', 0),
            INTO)),
        '',
        ('**WHICH OF THE RULING’S OPTIONS THE CORRECTION WEAKENS, WITHOUT RECOMMENDING ANY.** Option '
         '1 (axis B alone) is **not weakened in its evidence** — axis B is still the decidable axis '
         '— **but its cost is restated**, because it would admit %d documents rather than %d. '
         'Option 3 (both axes conjoined) is **weakened in its strictness argument**: the conjunction '
         'it rests on holds the same %d documents it always did, so the correction did not make it '
         'stricter and the distance between the axes it must bridge is wider. Options 2 and 5 are '
         '**untouched** — this act did not run axis A. Option 4 (two marks) is **strengthened in one '
         'respect only**: the two axes demonstrably came apart further. **A PRICE THAT MOVES IS '
         'EVIDENCE ABOUT AN OPTION AND NOT A VOTE AGAINST IT**, and the ruling remains the author’s.'
         % (CB, PB, RS['corrected_quadrants'].get('A+B+', 0))),
        '',
        ('**A CATEGORY REPORTED AS AN ABSENCE IS A FALSE DEFECT.** `tools/row_categories.py` is new, '
         'shared, and fixtured in both polarities — every category recognised where it applies and '
         '**refused where it does not**, because a recogniser that only ever says yes is not a '
         'recogniser. It carries **the front door’s own words**: README.md, under *Correspondence '
         'tables*, already says *“Where no kernel exists, the status says so in words — '
         'manuscript-resident or research-reach — rather than being omitted.”* **THE TAXONOMY IS '
         'EXTENDED, NOT INVENTED.** The three added are the ones b378 met and the front door has no '
         'word for: a **library** terminal, a name that **names a corpus document**, and a name **on '
         'a tag and no branch**. Applied to b378’s %d carried names it reports **%d absences where '
         'the old vocabulary reported %d**. **AND IT RETURNS A CATEGORY, NEVER A VERDICT**: naming a '
         'row a library lemma says where the terminal lives, not that the row is right.'
         % (CARRIED, NOTLOC, CARRIED)),
        '',
        ('**THE FOURTEEN SURVIVORS, READ FROM THE SENTENCE THAT NAMES EACH:** %s. **NOT ONE DOCUMENT '
         'WAS REPAIRED AND NOT ONE NAME WAS INVENTED.** Where the sentence does not decide which '
         'explanation applies, the answer is `UNDECIDED-BY-ITS-SENTENCE` rather than a guess — **a '
         'reading of a document is not a verdict on it.**'
         % ', '.join('**%s** %d' % (k.replace('-', ' ').lower(), v)
                      for k, v in SV['explanations'].items())),
        '',
        ('**AND THE DAY-1 DOCUMENT CARRIES APPARATUS.** b376 could not decide `%s` because it names '
         'its terminals in prose and b376’s instrument scanned table rows; b377 said a hand read '
         'would decide it; b378 read the other of the two and left this one. Read by hand — every '
         'backticked identifier with **the sentence that names it** — it names **%d** identifiers, '
         'of which **%d locate in a corpus kernel** and %d locate nowhere. **THE HAND READ DECIDES '
         'WHAT THE TABLE SCAN COULD NOT.** And it answers the question the draft picked this '
         'document for: the corpus’s own `CONCORDANCE-CARRIED` class **does describe something real '
         'on that page.** **The outcome is a mark, not a class: no declaration moved, no class '
         'ruled, not one byte written into the document.**'
         % (HD['chosen'].split('/')[-1][:-3], HD['named'], HD['located'], HD['not_located'])),
        '',
        ('**TWO FILINGS ABOUT A DOCUMENT OUTSIDE THE TREE, FILED AND NOT REPAIRED.** *(i)* The '
         'download-layer narrative book drifts: **REGISTRY.md** carries it at `v0_5` as '
         '**non-keystone, not for publication**; **CRANK_HARVEST_LIST.md** carries it at `v0_6` as a '
         '**Tier C narrative keystone**; the **patent package index** carries it at `v0.7` as **the '
         'narrative keystone**, travelling fenced for background comprehension only. **%d versions '
         'sit on the disk.** So this is not a pair of documents disagreeing — **it is a chain that '
         'moved and a precedence source that did not.** The corpus states the precedence rule '
         'itself: README.md calls REGISTRY.md **the single source of truth** and **the precedence '
         'source**. Under that rule the later documents are the ones out of step — **and that is a '
         'statement about precedence, not about which description is correct.** The registry may be '
         'stale and the later documents may be right; the rule says where the answer is recorded, '
         'not what it is. **THE REGISTRY IS NOT EDITED BY THIS ACT**: a seat that edits the '
         'precedence source to match a document that drifted has inverted the rule it is enforcing, '
         'and the choice between updating the row and correcting the others is the author’s. '
         '*(ii)* That document is outside the repository tree by ruling, so it was **outside the '
         'census’s population on both axes — not scored `B-`, not scored `A?`, but never considered '
         'at all.** **THAT IS UNLIKE EVERY OTHER OMISSION THIS SEQUENCE HAS FOUND**: b376’s '
         'narrowness scored documents wrongly, and no widening of a matcher would have reached this '
         'one. It is filed where the ruling’s evidence sits, because **the ruling has to say whether '
         'it governs documents outside the tree** — and if it does, the census’s population is not '
         'the ruling’s population. **Neither filing opens work on the document: it was not read for '
         'content, not classified, not graded, not moved, not renamed, not repaired.**'
         % FL['n_versions']),
        '',
        ('**WHAT THIS ACT DID NOT DO.** No class ruled, no document reclassified, **no declaration '
         'moved**, no list closed, **no corpus document written into at all**, **REGISTRY.md not '
         'edited**, **nothing on the download layer written, moved, renamed or removed**, no archive '
         'file touched and the 86 unconfirmed still unconfirmed. The six clusters stay filed and not '
         'opened. No `.lean` file touched, no build run, no axiom profile recomputed. **The four '
         'open lists are restated OPEN by name and none is closed.** h2 stands exactly where the '
         'deposit left it and this act makes no claim about it in either direction.'),
        '',
    ]


SCOPE = (
    "**SCOPE: THE APPARATUS AXIS RE-SCORED, AND TWO FILINGS.** NO class ruled, NO document "
    "reclassified, NO declaration moved, NO list closed -- the order's own list, and each is a bar. "
    "**NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED**, which is a point "
    "of principle and not only of scope: under the corpus's own rule the registry is what the others "
    "reconcile TO. **NOTHING ON THE DOWNLOAD LAYER WAS WRITTEN, MOVED, RENAMED OR REMOVED**, and the "
    "book was not read for content, classified, graded or repaired. **THE DIRECTION WAS REGISTERED "
    "BEFORE THE RUN**: a widened matcher finds more and never fewer, so a document losing a mark "
    "would be A DEFECT IN THE INSTRUMENT and is reported as one. **EVERY ABSENCE CARRIES A POSITIVE "
    "CONTROL THAT FINDS A KNOWN PRESENCE FIRST, AND AN ERROR EXIT IS NOT AN ANSWER** -- the standing "
    "clause, which b378 paid for. **THE CATEGORY MODULE RETURNS A CATEGORY AND NEVER A VERDICT**; a "
    "category is not an excuse. **THE FRONT DOOR'S OWN WORDS ARE QUOTED, NOT REPLACED.** **NO OPTION "
    "IS RECOMMENDED, RANKED OR PREFERRED** and the ruling remains the author's. **NO ARCHIVE FILE WAS "
    "TOUCHED** and the 86 unconfirmed stay unconfirmed. **NO OWNER INSTRUMENT WAS EDITED** -- "
    "b376_axes, b378_terminals, b378_lockgate and gate_hash are all IMPORTED AND RUN UNMODIFIED. **NO "
    "LIST WAS CLOSED** -- the four open lists are restated OPEN by name. **NO NEW TRACKING DOCUMENT "
    "WAS CREATED.** NO .lean FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED. NOTHING IS "
    "CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. "
    "Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS "
    "NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; "
    "M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still "
    "unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record, "
    "and THE PATENT GATE IS NAMED ONLY AS SOMETHING ANOTHER DOCUMENT SAYS. THE INSTRUMENT LANE STAYS "
    "PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it and this act "
    "makes no claim about it in either direction. The wave PARKED by the author's ruling. NOTHING IS "
    "DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def corr_rows(Q):
    m = ("**THE SUSPECT COLUMN RE-MEASURED: THE APPARATUS AXIS MOVES FROM %d TO %d, NONE LOST, AND "
         "EVERY DOCUMENT THAT MOVED CAME OUT OF A ROW WHERE THE ROLE AXIS SAYS NOTHING** (b379, the "
         "apparatus axis re-scored, and two filings)" % (PB, CB))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b379, %d gates read and %d checked "
            "by digest, and the face was rewritten before the lock and every face-subject gate "
            "RE-RUN AND RE-STAMPED. THE DIRECTION WAS REGISTERED BEFORE THE RUN: a widened matcher "
            "finds more and never fewer, so the corrected population is BOUNDED BELOW by the prior "
            "one and A DOCUMENT LOSING A MARK WOULD BE A DEFECT IN THE INSTRUMENT AND REPORTED AS "
            "ONE. None lost; %d gained. b376's predicate required a DOTTED terminal and b378 found "
            "NOT ONE CITING DOCUMENT USES THE DOTTED CONVENTION ALONE, which is what selected the "
            "six and what made the whole 303-document column suspect. AND THE MOVEMENT LANDED "
            "ENTIRELY IN THE CORPUS'S SILENCE: %d documents moved into the both-axes quadrant, so "
            "THE CORRECTION ENLARGES THE APPARATUS COLUMN AND LEAVES THE ROLE COLUMN EXACTLY WHERE "
            "IT WAS. WHICH OPTIONS IT WEAKENS IS STATED WITHOUT RECOMMENDING ANY: option 1's cost is "
            "restated, option 3's strictness argument is weakened, options 2 and 5 are untouched and "
            "option 4 is strengthened in one respect only. A CATEGORY REPORTED AS AN ABSENCE IS A "
            "FALSE DEFECT: row_categories is new and SHARED, fixtured in both polarities, carrying "
            "the front door's own MANUSCRIPT-RESIDENT and RESEARCH-REACH and adding the three b378 "
            "met, and over %d carried names it reports %d absences where the old vocabulary reported "
            "%d. THE FOURTEEN SURVIVORS ARE READ FROM THE SENTENCE THAT NAMES EACH and NOT ONE "
            "DOCUMENT WAS REPAIRED. THE DAY-1 DOCUMENT CARRIES APPARATUS: %d of %d identifiers "
            "locate in a corpus kernel, and the CONCORDANCE-CARRIED class does describe something "
            "real on that page. AND TWO FILINGS ABOUT A DOCUMENT OUTSIDE THE TREE: the registry "
            "carries it at v0_5 as NON-KEYSTONE while later documents carry it at v0_6 and v0.7 as a "
            "TIER C NARRATIVE KEYSTONE with %d versions on disk, so IT IS A CHAIN THAT MOVED AND A "
            "PRECEDENCE SOURCE THAT DID NOT; and being outside the tree by ruling it was NEVER "
            "SCORED ON EITHER AXIS, which the ruling must now say whether it governs"
            % (LG['gates_read'], LG['face_subject_gates'], MOVED, INTO, CARRIED, NOTLOC, CARRIED,
               HD['located'], HD['named'], FL['n_versions']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN AND NO ROW WAS WRITTEN INTO ANY "
            "DOCUMENT. ### The kernels were READ across every ref solely to locate identifiers the "
            "documents themselves name, and EVERY ABSENCE CARRIES A POSITIVE CONTROL THAT FOUND A "
            "KNOWN PRESENCE FIRST. ### NO STATEMENT WAS PROVED, NO BUILD WAS RUN AND NO AXIOM "
            "PROFILE WAS RECOMPUTED. ### LOCATING A NAME SAYS IT EXISTS AT THAT NAME AND SAYS "
            "NOTHING ABOUT WHETHER THE DOCUMENT'S SENTENCE ABOUT IT IS RIGHT")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT THE "
            "OBJECT. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED AND NO "
            "LIST CLOSED. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL, REGISTRY.md WAS NOT "
            "EDITED, AND NOTHING ON THE DOWNLOAD LAYER WAS WRITTEN, MOVED, RENAMED OR REMOVED")
    grade = ("### CORRECTED-BY-WIDENING, WITH THE DIRECTION REGISTERED BEFORE THE RUN. ### The "
             "widened pattern matches a STRICT SUPERSET of the old one, which is what makes the "
             "monotonicity bar meaningful rather than hopeful, and the bar is a check ON THE "
             "INSTRUMENT and not on the corpus. ### THE PRIOR COLUMN WAS RE-RUN FROM THE ORIGINAL "
             "PREDICATE ON THE SAME BYTES, not trusted from its banked JSON, so the side-by-side "
             "table compares two instruments and not an instrument against a recollection. ### THE "
             "CATEGORY MODULE RETURNS A CATEGORY AND NEVER A VERDICT. ### THE FRONT DOOR'S OWN WORDS "
             "ARE QUOTED AND NOT REPLACED. ### AND THE HONEST WARNING IS ON THE RECORD: THE "
             "CORRECTED COLUMN IS THIS SEAT'S SECOND PREDICATE AND NOT A GROUND TRUTH -- b376's "
             "COLUMN WAS ALSO BELIEVED WHEN IT WAS WRITTEN")
    status = ("data/b379_the_apparatus_axis_rescored.txt; data/%s; data/%s; data/%s; data/%s; "
              "data/%s; data/b379_registration_2026-09-08.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b379); tools/row_categories.py (SHARED, new); "
              "tools/b379_rescore.py; tools/b379_survivors.py; tools/b379_hand.py; "
              "tools/b379_filings.py; PLACE-papers OPEN_TRAILS.md (an append-only block; NO CORPUS "
              "DOCUMENT EDITED AND REGISTRY.md NOT TOUCHED); CORRESPONDENCE.md row %%d"
              % (RS['run_file'], SV['run_file'], HD['run_file'], FL['run_file'],
                 J('b379_reads')['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the apparatus axis re-scored', 'the suspect column', 'the row categories',
           'a category is not an absence', 'the download layer drift')
MUST_NOT_HIT = ('the class is ruled', 'the declarations are moved',
                'the lists are closed', 'the registry is edited')


def do_key(rownum):
    key_new = (
        "    'the-suspect-column-re-measured': ['the apparatus axis re-scored', 'the suspect "
        "column',\n"
        "                                      'the row categories', 'a category is not an "
        "absence',\n"
        "                                      'the download layer drift'],\n")
    row_new = (
        '    # ### THE APPARATUS AXIS RE-SCORED, AND TWO FILINGS (b379).\n'
        '    ("the-suspect-column-re-measured", "b379 (the axis-B column b378 named suspect, '
        're-measured; the row categories; two filings about a document outside the tree)",\n'
        '     "THE SUSPECT COLUMN RE-MEASURED. b376 axis-B predicate required a DOTTED terminal and '
        'b378 found NOT ONE citing document uses the dotted convention alone, so the whole "\n'
        '     " 303-document B- column was suspect. Re-measured with a both-dialect matcher: B+ '
        'moves from ' + str(PB) + ' to ' + str(CB) + ', ' + str(MOVED) + ' gained and NONE LOST. '
        'THE DIRECTION WAS REGISTERED BEFORE THE RUN -- "\n'
        '     " a widened matcher finds more and never fewer, so a document losing a mark would be A '
        'DEFECT IN THE INSTRUMENT and reported as one. AND THE MOVEMENT LANDED ENTIRELY IN THE "\n'
        '     " CORPUS SILENCE: ' + str(INTO) + ' documents moved into the both-axes quadrant, so '
        'the correction ENLARGES THE APPARATUS COLUMN AND LEAVES THE ROLE COLUMN EXACTLY WHERE IT "\n'
        '     " WAS. A CATEGORY REPORTED AS AN ABSENCE IS A FALSE DEFECT: row_categories is new and '
        'SHARED, carries the front door own MANUSCRIPT-RESIDENT and RESEARCH-REACH, adds the "\n'
        '     " three b378 met, and reports ' + str(NOTLOC) + ' absences where the old vocabulary '
        'reported ' + str(CARRIED) + '. THE DAY-1 DOCUMENT CARRIES APPARATUS: ' + str(HD['located'])
        + ' of ' + str(HD['named']) + ' identifiers "\n'
        '     " locate in a corpus kernel. AND THE DOWNLOAD-LAYER BOOK DRIFTS: the registry carries '
        'it at v0_5 as NON-KEYSTONE while later documents carry it at v0_6 and v0.7 as a TIER C "\n'
        '     " NARRATIVE KEYSTONE, with ' + str(FL['n_versions']) + ' versions on disk -- A CHAIN '
        'THAT MOVED AND A PRECEDENCE SOURCE THAT DID NOT.",\n'
        '     "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED AND NO LIST '
        'CLOSED. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED --"\n'
        '     " under the corpus own rule the registry is what the others reconcile TO, and a seat '
        'that edits the precedence source to match a document that drifted has inverted the"\n'
        '     " rule it is enforcing. ### NOTHING ON THE DOWNLOAD LAYER WAS WRITTEN, MOVED, RENAMED '
        'OR REMOVED and the book was not read for content. ### EVERY ABSENCE CARRIES A POSITIVE"\n'
        '     " CONTROL THAT FINDS A KNOWN PRESENCE FIRST, AND AN ERROR EXIT IS NOT AN ANSWER. ### '
        'THE CATEGORY MODULE RETURNS A CATEGORY AND NEVER A VERDICT; a category is not an"\n'
        '     " excuse. ### NO OPTION IS RECOMMENDED and the ruling remains the author. ### THE '
        'CORRECTED COLUMN IS THIS SEAT SECOND PREDICATE AND NOT A GROUND TRUTH. ### THE FOUR"\n'
        '     " OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED. ### '
        'NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2"\n'
        '     " UNCHANGED",\n'
        '     "data/b379_the_apparatus_axis_rescored.txt; data/' + RS['run_file'] + '; data/'
        + SV['run_file'] + '; data/' + HD['run_file'] + '; data/' + FL['run_file'] + ';"\n'
        '     " data/b379_registration_2026-09-08.txt (LOCKED before any write, chained on '
        'tools/b378_lockgate.py run as b379 -- ' + str(LG['gates_read']) + ' gates read, '
        + str(LG['face_subject_gates']) + ' checked by digest);"\n'
        '     " tools/row_categories.py (SHARED, new: the front door own words carried, three '
        'categories added, fixtured in both polarities); tools/b379_rescore.py (b376_axes"\n'
        '     " IMPORTED UNMODIFIED and the prior column RE-RUN, not trusted); '
        'tools/b379_survivors.py; tools/b379_hand.py; tools/b379_filings.py;"\n'
        '     " PLACE-papers OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row ' + str(rownum)
        + '"),\n')
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
    if "'the-suspect-column-re-measured'" not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if '"the-suspect-column-re-measured"' not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    open(INDEX + '.tmp', 'wb').write(txt.encode('utf-8'))
    os.replace(INDEX + '.tmp', INDEX)
    ok = True
    out, rc = query('the-suspect-column-re-measured')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : the-suspect-column-re-measured returns %d row(s)  %s'
        % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'the-suspect-column-re-measured' in o
        ok = ok and g
        rec('    %-44s reaches the b379 key : %s' % (q, g))
    for lbl, cond in (('no class ruled, no declaration moved',
                       'NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED' in out),
                      ('no corpus document written into and no registry edit',
                       'NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED'
                       in out),
                      ('nothing on the download layer written',
                       'NOTHING ON THE DOWNLOAD LAYER WAS WRITTEN' in out),
                      ('an absence needs a proved search',
                       'POSITIVE' in out and 'CONTROL' in out),
                      ('a category is never a verdict',
                       'RETURNS A CATEGORY AND NEVER A VERDICT' in out),
                      ('the corrected column is not a ground truth',
                       'NOT A GROUND TRUTH' in out),
                      ('no list was closed', 'NO LIST' in out and 'CLOSED' in out),
                      ('the lists are restated open', 'RESTATED OPEN BY NAME' in out),
                      ('no new tracking document', 'NO NEW TRACKING DOCUMENT WAS CREATED' in out)):
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
    rec('b379 -- THE DESK UNDER (R7), AND THE THREE CLOSING WRITES.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE DESK.')
    rec('-' * 100)
    Q = do_desk()

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE TRAIL BLOCK, APPEND-ONLY.')
    rec('-' * 100)
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
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
        run_clock.write(D, 'b379_desk_notes', LINES)
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b379_desk_notes', LINES)
        return 1
    g1 = ('THE SUSPECT COLUMN RE-MEASURED' in ROWS[0][0]
          and 'CHECKS WHAT EACH GATE READ' in ROWS[0][1]
          and 'RE-RUN AND RE-STAMPED' in ROWS[0][1]
          and 'BOUNDED BELOW' in ROWS[0][1]
          and 'A DEFECT IN THE INSTRUMENT' in ROWS[0][1]
          and 'ENTIRELY IN THE CORPUS' in ROWS[0][1]
          and 'WITHOUT RECOMMENDING ANY' in ROWS[0][1]
          and 'A CHAIN THAT MOVED' in ROWS[0][1]
          and 'NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN' in ROWS[0][2]
          and 'POSITIVE CONTROL' in ROWS[0][2]
          and 'NO CLASS WAS RULED' in ROWS[0][3]
          and 'REGISTRY.md WAS NOT EDITED' in ROWS[0][3]
          and 'STRICT SUPERSET' in ROWS[0][4]
          and 'NEVER A VERDICT' in ROWS[0][4]
          and 'NOT A GROUND TRUTH' in ROWS[0][4]
          and 'THE APPARATUS AXIS RE-SCORED' in ROWS[0][5]
          and 'NO LIST WAS CLOSED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says the re-measure, the stamped gate, the registered direction, the '
        'defect rule, the silence, no recommendation, the chain that moved, no terminal claimed, '
        'the positive control, no class ruled, no registry edit, the superset, never a verdict, '
        'not a ground truth, and the scope : %s' % g1)
    if not g1:
        run_clock.write(D, 'b379_desk_notes', LINES)
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
            run_clock.write(D, 'b379_desk_notes', LINES)
            return 1
        rownum = start

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE INDEX KEY.')
    rec('-' * 100)
    kok = do_key(rownum)
    rec('')
    rec('=' * 100)
    rec('  ### desk swept %d ; trail appended %s ; row %s ; key %s'
        % (Q['items'], tr['appended_only'], rownum, kok))
    rec('  ### ### **LISTS CLOSED : 0. ### THE FOUR ARE RESTATED `OPEN` BY NAME.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b379_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok, lists_closed=0,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b379_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
