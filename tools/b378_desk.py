# -*- coding: utf-8 -*-
"""b378_desk.py -- THE DESK UNDER `(R7)`, AND THE THREE CLOSING WRITES: THE TRAIL BLOCK, THE ROW,
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
MARK = '<!-- b378 the refs widened and the convention swept -->'
PRIOR = '<!-- b377 the unblocked obligation; the pin was the missing element -->'
ACT = 'b378'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


TM, AR, HD = J('b378_terminals'), J('b378_archives'), J('b378_hand')
LG = J('b378_lockgate')
BR377 = J('b377_branch')
CL375 = J('b375_clusters')
NOKEY = CL375['subject_clusters_without_keystone']
TALLY = TM['tally']


def T(k):
    for kk, v in TALLY.items():
        if k in kk:
            return v
    return 0


CARRIED = TM['carried']
NOTFOUND = T('NOT-FOUND-ON-ANY-REF')
MATHLIB = T('Mathlib')
DOCNAME = T('NAMES-A-CORPUS-DOCUMENT')
NONMAIN = T('FOUND-ON-A-NON-main-REF')
MULTI = T('MORE THAN ONE KERNEL')
REFS = TM['refs']
KERN = TM['kernels']

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
     'OPEN. ### **AND THIS ACT SHARPENS IT RATHER THAN CLOSING IT:** ### it showed that a ref nobody '
     'named may still be findable -- two identifiers sat on a TAG -- so the list is about naming and '
     'not about existence'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND', None, None,
     'OPEN. ### b373 listed them with their carriers and ROUTED them. ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', None, None,
     'OPEN. ### b374 listed every figure stated without a ref in its own sentence. ### This act dates '
     'none of them'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND', None, None,
     'OPEN. ### b374 found entries the register carries that appear nowhere else. ### This act '
     'rewrites none of them'),

    # ---- CARRIED --------------------------------------------------------------------------------
    ('the class ruling itself', 'STAND', None, None,
     'STILL THE AUTHOR`S. ### b376 assembled five options, b377 added the role clause and a bearing '
     'line each. ### **NO OPTION IS RECOMMENDED AND NO CLASS IS RULED HERE EITHER**'),
    ('the six subject clusters with registry rows and no keystone', 'STAND', None, None,
     'FILED at b377 and ### **STILL NOT OPENED.** ### The order adopted the draft and named three '
     'additions, none of which is the cluster lane; ### **THE READING IS DECLARED ON THIS ACT`S '
     'LOCKED FACE IN ADVANCE** so the author can correct it. ### %d clusters' % len(NOKEY)),
    ("the census's definition-versus-operation drift", 'STAND', None, None,
     'FILED at b377 and ### **NOT REPAIRED HERE** -- repairing it belongs to the ruling'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', None, None,
     'CARRIED from b377 and ### **DELIBERATELY NOT RE-MEASURED** ### by this act'),

    # ---- WHAT THIS ACT ADDS -------------------------------------------------------------------------
    ("the lock gate's remaining hole", 'CLOSE', 'b378_lockgate_notes',
     'FACE-SUBJECT GATES CHECKED BY DIGEST',
     'CLOSED at b378 ### **IN THE TOOL, WHICH IS WHERE THE DRAFT SAID TO CLOSE IT.** ### '
     '`tools/gate_hash.py` stamps a gate record with the sha256 of what the gate read; '
     '`tools/b378_lockgate.py` requires every face-subject gate to carry a stamp equal to the face '
     'it is about to lock, and REFUSES a record carrying none. ### **FIXTURED IN FOUR POLARITIES, '
     'AND THE STALE-DIGEST POLARITY IS THE ONE b377 SUFFERED**'),
    ('an upper bound taken at one ref is not a count', 'STAND', None, None,
     'NEW at b378: b377 searched %d refs -- one per kernel -- and reported %d identifiers unresolved. '
     '### **THIS ACT SEARCHED %d REFS AND THE FIGURE FELL TO %d.** ### The earlier number was never '
     'wrong; ### **IT WAS AN UPPER BOUND TAKEN AT ONE REF AND WAS NOT LABELLED AS ONE**'
     % (KERN, CARRIED, REFS, NOTFOUND)),
    ('a search that cannot run looks exactly like a search that found nothing', 'STAND', None, None,
     'NEW at b378 and it is ### **THE SHARPEST LESSON OF THE ACT.** ### The first sweep handed '
     '`git grep -E` a Python-only pattern; every invocation died with `Invalid preceding regular '
     'expression`; the caller read the fatal exit as NO MATCHES; and the sweep reported ### **0 FOUND '
     'ACROSS 270 REFS.** ### It was exposed only by a CONTRADICTION with b377`s own record. ### **THE '
     'CURE IS A POSITIVE CONTROL AND AN EXIT CODE READ PROPERLY**, and both are now in the tool'),
    ('identifiers found only on a tag', 'STAND', None, None,
     'NEW at b378: %d of the carried identifiers are declared on `refs/tags/phase-1.5-module-1-v2` of '
     '`SIDE-effects` and on no branch. ### **A TAG IS A REF AND b377 DID NOT SEARCH IT**' % NONMAIN),
    ('identifiers that name a corpus document rather than a terminal', 'STAND', None, None,
     'NEW at b378: %d of the carried identifiers are `.md` documents in PLACE-papers. ### **THEY WERE '
     'NEVER TERMINALS AND WERE COUNTED AS MISSING ONES**' % DOCNAME),
    ('identifiers that are Mathlib names', 'STAND', None, None,
     'NEW at b378: %d are declared in `Mathlib` on this disk. ### **A PAPER MAY CITE A LIBRARY LEMMA '
     'IT DID NOT PROVE; THAT IS A CATEGORY AND NOT A FAULT**' % MATHLIB),
    ('the identifiers no searched ref declares', 'STAND', None, None,
     'NEW at b378 and ### **THIS IS THE RESIDUE THAT SURVIVES THE WIDENING:** ### %d names that no '
     'ref of any kernel on this disk declares, and that Mathlib does not either. ### **NOT REPAIRED, '
     'NOT DISPUTED, AND THE DOCUMENTS THAT NAME THEM ARE NOT REWRITTEN**' % NOTFOUND),
    ('the two conventions, swept and neither rewritten', 'STAND', None, None,
     'NEW at b378: the citing documents split BARE-only and BOTH; ### **NO DOCUMENT USES THE DOTTED '
     'CONVENTION ALONE.** ### b376`s axis-B predicate required DOTTED, so ### **IT COULD NOT HAVE '
     'PASSED ANY OF THEM**, and that is what selected the six'),
    ("b376's axis-B column is named as suspect and not re-measured", 'STAND', None, None,
     'NEW at b378: the narrowness that selected the six also scored 303 documents `B-`. ### **THAT '
     'COLUMN IS NAMED AS SUSPECT HERE AND IS NOT RE-MEASURED**, because re-measuring it is an act and '
     'not a footnote'),
    ('the archive files the mirror carries, confirmed', 'STAND', None, None,
     'NEW at b378: %d of %d CONFIRMED PRESENT by digest AND by title line, ### **NEVER BY FILENAME.** '
     '### %d files sit under `archive/` and %d of those the mirror does not carry -- ### **CONTEXT, '
     'NOT THE ORDERED REPORT.** ### **NOTHING WAS REMOVED; THE REMOVAL IS THE AUTHOR`S**'
     % (AR['confirmed'], AR['ordered_population'], AR['context_archive_files'],
        AR['context_not_carried'])),
    ('one NOT DETERMINABLE document, read by hand', 'STAND', None, None,
     'NEW at b378: `%s` names %d identifiers; ### **%d LOCATE IN EXACTLY ONE KERNEL**, %d in more '
     'than one, %d in none. ### The hand read decides what the table scan could not: ### **IT '
     'CARRIES SOME APPARATUS.** ### The other of the two is LEFT, and ### **NO DECLARATION WAS '
     'MOVED**' % (HD['chosen'].split('/')[-1][:-3], HD['named'], HD['located'],
                  HD['ambiguous'], HD['not_located'])),
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
        '### **b378 — THE REFS WIDENED AND THE CONVENTION SWEPT (2026-09-08)**',
        '',
        ('*No block above is edited. The b377 block (`%s`) and every block before it stand exactly as '
         'they were written.*' % PRIOR),
        '',
        ('**AN UPPER BOUND TAKEN AT ONE REF IS NOT A COUNT.** b377 searched `main` at each kernel — '
         '%d refs, one per repository — and reported **%d identifiers that no kernel declares**. This '
         'act re-ran the search across **every branch and every tag**, with the refs enumerated live '
         'from each repository and printed: **%d refs behind %d distinct commits.** The figure falls '
         'to **%d**. b377’s number was never wrong; **it was an upper bound taken at one ref and was '
         'not labelled as one**, and it is labelled as one now.'
         % (KERN, CARRIED, REFS, TM['commits'], NOTFOUND)),
        '',
        ('**WHERE THE OTHER %d WENT, EACH TO EXACTLY ONE CLASSIFICATION.** **%d are `Mathlib` names** '
         'declared in the Mathlib package on this disk — a paper may cite a library lemma it did not '
         'prove, and **that is a category and not a fault.** **%d name a corpus document rather than '
         'a terminal** — `OPEN_TRAILS`, `THE_RESIDUE_OF_RH`, `THE_CODOMAIN_SPECIFICATION` and others '
         'are `.md` files, and **they were never terminals and were counted as missing ones.** **%d '
         'are declared on `refs/tags/phase-1.5-module-1-v2` of `SIDE-effects` and on no branch at '
         'all** — **a tag is a ref, and b377 did not search it.** And **%d is declared in more than '
         'one kernel**, which b377’s own rule already says is not a terminal a document can cite; '
         'carrying that rule here is what stopped this act reading the first of several silently, as '
         'its own first run did.'
         % (CARRIED - NOTFOUND, MATHLIB, DOCNAME, NONMAIN, MULTI)),
        '',
        ('**AND THE SHARPEST FINDING IS ABOUT THE SEARCH ITSELF: A SEARCH THAT CANNOT RUN LOOKS '
         'EXACTLY LIKE A SEARCH THAT FOUND NOTHING.** This act’s first sweep handed `git grep -E` a '
         'Python-only pattern containing `(?:…)`. POSIX ERE rejects it. Every one of the 209 '
         'invocations died with *Invalid preceding regular expression*, the caller read the non-zero '
         'exit as **no matches**, and the sweep reported **0 identifiers found across 270 refs** — a '
         'clean, confident, entirely false answer. **IT WAS EXPOSED ONLY BY A CONTRADICTION WITH '
         'b377’S OWN RECORD**, which had found one of these names in two kernels. The tool now (i) '
         'hands `git` a POSIX pattern, (ii) treats an exit code above 1 as **an error and not an '
         'answer**, and (iii) carries **a positive control** — a name known to sit on a non-`main` '
         'ref — and **refuses to report an absence until it has proved it can find a presence.**'),
        '',
        ('**THE TWO CONVENTIONS, SWEPT, AND NEITHER REWRITTEN.** The corpus writes terminal names '
         '**bare** in its older documents and **dotted** in its newer ones. The matcher built here '
         'accepts both, is fixtured in both polarities, and carries a **discrimination arm** proving '
         'it still refuses a name absent under either — because a matcher that accepts everything is '
         'not a matcher. Swept across the six citing documents: **three use the bare convention only, '
         'three use both, and not one uses the dotted convention alone.** **b376’s axis-B predicate '
         'required a dotted terminal, so it could not have passed any of them.** **THE COST IS NOT '
         'HYPOTHETICAL: IT SELECTED THE SIX**, and b377 inherited that selection as its whole '
         'population. **Where else it may have cost the same is named and not swept:** b376’s entire '
         'axis-B column — 303 documents scored `B-` on that predicate — **is named here as suspect '
         'and is NOT re-measured**, because re-measuring it is an act and not a footnote. b375’s '
         'census comparison used a *heading* test rather than a terminal test and is **not** affected; '
         'said so that the suspicion is bounded rather than free-floating. **No document is rewritten '
         'into the other dialect. Both are correct in their own terms.**'),
        '',
        ('**THE HELD BRANCH THE DOCUMENT NAMES IN ITS OWN TEXT WAS SEARCHED BY NAME.** '
         '`THE_RESIDUE_OF_RH` says its artifacts are *read from the held branch '
         '`word-pairing-interface`* and, in the same breath, *not merged, nothing deposited*. That '
         'branch exists, was enumerated live, and was searched — **and none of the carried '
         'identifiers is on it.** The positive control **is**, which is how we know the branch was '
         'genuinely read. **A DOCUMENT THAT TELLS YOU WHERE TO LOOK HAD ALREADY DONE HALF THE WORK, '
         'AND THE ANSWER THERE IS STILL NO.**'),
        '',
        ('**THE ARCHIVES THE MIRROR CARRIES: %d OF %d CONFIRMED PRESENT.** Each was confirmed on the '
         'canonical drive **by a verified sha256 digest AND by a title-line match — never by '
         'filename**, because the mirror export is flat and derives each name from its source path, '
         'and the repository strips version suffixes besides. The filename comparison is printed '
         'beside each verdict **so a reader can see it was not used as evidence.** For context and '
         'labelled as context: **%d files sit under `archive/` on the drive and the mirror carries %d '
         'of them**; the other %d were **not confirmed by this act and it makes no claim about '
         'them.** **NOTHING WAS REMOVED, MOVED OR RENAMED. THE REMOVAL IS THE AUTHOR’S AND DEPENDS ON '
         'THIS REPORT** — which is exactly why the report had to be able to say NOT CONFIRMED.'
         % (AR['confirmed'], AR['ordered_population'], AR['context_archive_files'],
            AR['ordered_population'], AR['context_not_carried'])),
        '',
        ('**AND THE LOCK GATE’S REMAINING HOLE IS CLOSED IN THE TOOL, WHICH IS WHERE THE DRAFT SAID '
         'TO CLOSE IT.** b376 proved every gate passed and could not prove what any of them passed '
         '*on*; b377 hit that when a late rewrite left gate records stale. `tools/gate_hash.py` (new, '
         'shared) stamps a gate’s own run record with the **sha256 of the bytes that gate read**, '
         'appending and never rewriting. `tools/b378_lockgate.py` requires every face-subject gate to '
         'carry a stamp **equal to the face it is about to lock**, and **refuses a record carrying no '
         'stamp at all** — an absent claim is not a true one. It is fixtured in **four** polarities: '
         'clean permits; a missing phrase, **a stale digest**, and a missing stamp each refuse **for '
         'that gate**. This act’s own face was rewritten twice before the lock, and **every '
         'face-subject gate was re-run and re-stamped**; %d gates read, %d checked by digest. **WHAT '
         'IT STILL DOES NOT PROVE, SAID ON THE FACE:** the stamp is the *caller’s* claim about what '
         'it fed the gate, not the gate vouching for itself — which would need the shared instruments '
         'edited, and **this act edits none.**'
         % (LG['gates_read'], LG['face_subject_gates'])),
        '',
        ('**ONE `NOT DETERMINABLE` DOCUMENT, READ BY HAND.** b376 could not decide `%s` because it '
         'names its terminals in prose and b376’s instrument scanned table rows. Read by hand — every '
         'backticked identifier with **the sentence that names it** — it names **%d** identifiers, of '
         'which **%d locate in exactly one kernel**, %d in more than one, and %d in none. **THE HAND '
         'READ DECIDES WHAT THE TABLE SCAN COULD NOT: THE DOCUMENT CARRIES APPARATUS.** The other of '
         'the two is **left exactly as b377 left it**. **The outcome is a mark, not a class: no '
         'declaration was moved, no class was ruled, and not one byte was written into the '
         'document.**'
         % (HD['chosen'].split('/')[-1][:-3], HD['named'], HD['located'], HD['ambiguous'],
            HD['not_located'])),
        '',
        ('**WHAT THIS ACT DID NOT DO.** No class ruled, no document reclassified, **no declaration '
         'moved**, no list closed, **no corpus document written into at all**, **no archive file '
         'removed, moved or renamed**. The six clusters stay **filed and not opened** — the order '
         'adopted the executor’s draft and named three additions, none of them the cluster lane, and '
         '**that reading is declared on this act’s locked face in advance** where the author can '
         'correct it. The census stays quoted and not repaired; the column-(d) figure stays a floor '
         'and is not re-measured. No `.lean` file touched, no build run, no axiom profile recomputed. '
         '**The four open lists are restated OPEN by name and none is closed.** h2 stands exactly '
         'where the deposit left it and this act makes no claim about it in either direction.'),
        '',
    ]


SCOPE = (
    "**SCOPE: THE REFS WIDENED, THE CONVENTION SWEPT, AND THE ARCHIVES CONFIRMED.** NO class ruled, "
    "NO document reclassified, NO declaration moved, NO list closed -- the order's own list, and each "
    "is a bar. **NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL** -- not the six, not the two, not the "
    "archives, not the census. **NO ARCHIVE FILE WAS REMOVED, MOVED OR RENAMED**; the removal is the "
    "author's and depends on this report. **NO DOCUMENT WAS REWRITTEN INTO THE OTHER CONVENTION**: "
    "bare and dotted are both correct in their own dialect. **EVERY REF WAS ENUMERATED LIVE FROM ITS "
    "OWN REPOSITORY AND PRINTED**, never typed. **AN ABSENCE IS ONLY REPORTED FROM A SEARCH THAT "
    "PROVED IT CAN FIND A PRESENCE**: a positive control runs first and a git exit above 1 is an "
    "error and not an answer. **A NAME DECLARED IN MORE THAN ONE KERNEL IS NOT A TERMINAL A DOCUMENT "
    "CAN CITE** and is classified as such rather than read as the first of several. **NO ARCHIVE WAS "
    "CONFIRMED ON A FILENAME**: digest AND title line, with the filename comparison printed so a "
    "reader can see it was not used. **b376's AXIS-B COLUMN IS NAMED AS SUSPECT AND NOT "
    "RE-MEASURED.** **NO OWNER INSTRUMENT WAS EDITED**, b376's lock gate included. **NO LIST WAS "
    "CLOSED** -- the four open lists are restated OPEN by name. **NO NEW TRACKING DOCUMENT WAS "
    "CREATED.** NO .lean FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED. NOTHING IS CLAIMED "
    "ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about "
    "the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO "
    "COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The "
    "patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE "
    "INSTRUMENT LANE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit "
    "left it and this act makes no claim about it in either direction. The wave PARKED by the "
    "author's ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def corr_rows(Q):
    m = ("**AN UPPER BOUND TAKEN AT ONE REF IS NOT A COUNT: SEARCHING %d REFS INSTEAD OF %d CUT THE "
         "UNRESOLVED IDENTIFIERS FROM %d TO %d, AND THE FIRST SWEEP THAT SAID ZERO WAS A SEARCH THAT "
         "COULD NOT RUN** (b378, the refs widened and the convention swept)"
         % (REFS, KERN, CARRIED, NOTFOUND))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT NOW "
            "CHECKS WHAT EACH GATE READ** -- tools/gate_hash.py stamps a gate record with the sha256 "
            "of the bytes that gate read, tools/b378_lockgate.py requires every face-subject gate to "
            "carry a stamp EQUAL TO THE FACE IT IS ABOUT TO LOCK and REFUSES a record carrying none, "
            "and it is fixtured in FOUR polarities where the stale-digest polarity is the one b377 "
            "suffered; %d gates read and %d checked by digest, and THIS ACT'S OWN FACE WAS REWRITTEN "
            "BEFORE THE LOCK AND EVERY FACE-SUBJECT GATE WAS RE-RUN AND RE-STAMPED. THE REFS WERE "
            "ENUMERATED LIVE FROM EACH REPOSITORY AND PRINTED: %d refs behind %d distinct commits "
            "across %d kernels, against b377's %d. OF THE %d IDENTIFIERS CARRIED FORWARD, %d ARE "
            "Mathlib NAMES, %d NAME A CORPUS DOCUMENT RATHER THAN A TERMINAL, %d ARE DECLARED ONLY ON "
            "A TAG AND ON NO BRANCH, %d IS DECLARED IN MORE THAN ONE KERNEL, AND %d ARE DECLARED BY NO "
            "REF OF ANY KERNEL ON THIS DISK NOR BY Mathlib. AND THE SHARPEST FINDING IS ABOUT THE "
            "SEARCH ITSELF: THE FIRST SWEEP HANDED git grep A PYTHON-ONLY PATTERN, EVERY INVOCATION "
            "DIED, THE CALLER READ THE FATAL EXIT AS NO MATCHES, AND IT REPORTED ZERO FOUND ACROSS "
            "270 REFS -- EXPOSED ONLY BY A CONTRADICTION WITH b377'S OWN RECORD, and cured by a POSIX "
            "pattern, an exit code read properly, and A POSITIVE CONTROL THAT MUST FIND A PRESENCE "
            "BEFORE ANY ABSENCE IS REPORTED. THE MATCHER NOW ACCEPTS BOTH CONVENTIONS with fixtures "
            "in both polarities and a discrimination arm, and the sweep found NOT ONE CITING DOCUMENT "
            "USING THE DOTTED CONVENTION ALONE, so b376's DOTTED-ONLY axis-B predicate COULD NOT HAVE "
            "PASSED ANY OF THEM -- WHICH IS WHAT SELECTED THE SIX -- and b376's 303-document axis-B "
            "column is NAMED AS SUSPECT AND NOT RE-MEASURED. THE HELD BRANCH THE DOCUMENT NAMES IN "
            "ITS OWN TEXT WAS SEARCHED BY NAME and carries none of the carried identifiers, though it "
            "does carry the positive control. %d OF %d ARCHIVE FILES THE MIRROR CARRIES ARE CONFIRMED "
            "PRESENT BY DIGEST AND BY TITLE LINE AND NEVER BY FILENAME, with %d files under archive/ "
            "and %d of those not carried reported as CONTEXT AND NOT AS THE ORDERED REPORT. AND ONE "
            "NOT DETERMINABLE DOCUMENT WAS READ BY HAND: %d identifiers named, %d locating in exactly "
            "one kernel, SO THE HAND READ DECIDES WHAT THE TABLE SCAN COULD NOT"
            % (LG['gates_read'], LG['face_subject_gates'], REFS, TM['commits'], KERN, KERN,
               CARRIED, MATHLIB, DOCNAME, NONMAIN, MULTI, NOTFOUND,
               AR['confirmed'], AR['ordered_population'], AR['context_archive_files'],
               AR['context_not_carried'], HD['named'], HD['located']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN AND NO ROW WAS WRITTEN INTO ANY "
            "DOCUMENT. ### The kernels were READ across every ref solely to locate identifiers the "
            "documents themselves name. ### NO STATEMENT WAS PROVED, NO BUILD WAS RUN AND NO AXIOM "
            "PROFILE WAS RECOMPUTED. ### LOCATING A NAME SAYS IT EXISTS AT THAT NAME ON THAT REF AND "
            "SAYS NOTHING ABOUT WHETHER THE DOCUMENT'S SENTENCE ABOUT IT IS RIGHT")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT THE "
            "OBJECT -- no frame, no seed, no transform, no quadrature, no fit, no score, no series. "
            "### NO CLASS WAS RULED, NO DOCUMENT WAS RECLASSIFIED, NO DECLARATION WAS MOVED AND NO "
            "LIST WAS CLOSED. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND NO ARCHIVE FILE WAS "
            "REMOVED, MOVED OR RENAMED. ### NO DOCUMENT WAS REWRITTEN INTO THE OTHER CONVENTION")
    grade = ("### CORRECTED-BY-WIDENING, WITH THE EARLIER FIGURE RESTATED AS AN UPPER BOUND TAKEN AT "
             "ONE REF. ### EVERY REF WAS ENUMERATED LIVE FROM ITS OWN REPOSITORY AND PRINTED, never "
             "typed and never assumed. ### AN ABSENCE IS ONLY REPORTED FROM A SEARCH THAT PROVED IT "
             "CAN FIND A PRESENCE, and a git exit above 1 is an error and not an answer. ### A NAME "
             "DECLARED IN MORE THAN ONE KERNEL IS NOT A TERMINAL A DOCUMENT CAN CITE and is "
             "classified as such rather than read as the first of several -- b377 minted that rule "
             "and this act's own first run did not carry it. ### THE MATCHER ACCEPTS BOTH DIALECTS "
             "AND ITS DISCRIMINATION ARM PROVES IT STILL REFUSES A NAME ABSENT UNDER EITHER. ### NO "
             "ARCHIVE WAS CONFIRMED ON A FILENAME AND THE FILENAME COMPARISON IS PRINTED SO A READER "
             "CAN SEE IT WAS NOT USED")
    status = ("data/b378_the_refs_widened.txt; data/%s; data/%s; data/%s; data/%s; data/%s; "
              "data/b378_registration_2026-09-08.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py which read all %d pre-lock gates and checked %d of them by "
              "digest); tools/gate_hash.py (SHARED, new); tools/b378_lockgate.py; "
              "tools/b378_terminals.py; tools/b378_archives.py; tools/b378_hand.py; "
              "PLACE-papers OPEN_TRAILS.md (an append-only block; NO CORPUS DOCUMENT EDITED); "
              "CORRESPONDENCE.md row %%d"
              % (TM['run_file'], AR['run_file'], HD['run_file'],
                 J('b378_reads')['run_file'], LG['run_file'],
                 LG['gates_read'], LG['face_subject_gates']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the refs widened', 'an upper bound at one ref', 'the two conventions',
           'the archives confirmed', 'a search that cannot run')
MUST_NOT_HIT = ('the class is ruled', 'the declarations are moved',
                'the lists are closed', 'the archives are removed')


def do_key(rownum):
    key_new = (
        "    'an-upper-bound-at-one-ref': ['the refs widened', 'an upper bound at one ref',\n"
        "                                 'the two conventions', 'the archives confirmed',\n"
        "                                 'a search that cannot run'],\n")
    row_new = (
        '    # ### THE REFS WIDENED AND THE CONVENTION SWEPT (b378).\n'
        '    ("an-upper-bound-at-one-ref", "b378 (the terminal search re-run across every ref; the '
        'two conventions swept; the archives confirmed and NOT removed)",\n'
        '     "AN UPPER BOUND TAKEN AT ONE REF IS NOT A COUNT. b377 searched ' + str(KERN)
        + ' refs -- one per kernel -- and reported ' + str(CARRIED) + ' identifiers no kernel "\n'
        '     " declares. Searching ' + str(REFS) + ' refs behind ' + str(TM['commits'])
        + ' distinct commits cuts it to ' + str(NOTFOUND) + '. Of the rest, ' + str(MATHLIB)
        + ' are Mathlib names, ' + str(DOCNAME) + ' name a corpus document rather than a "\n'
        '     " terminal, ' + str(NONMAIN) + ' are declared ONLY ON A TAG and on no branch, and '
        + str(MULTI) + ' is declared in more than one kernel. AND THE SHARPEST FINDING IS ABOUT THE '
        'SEARCH ITSELF: the "\n'
        '     " first sweep handed git grep a Python-only pattern, every invocation died, the caller '
        'read the fatal exit as NO MATCHES, and it reported ZERO FOUND ACROSS 270 REFS -- "\n'
        '     " a clean confident false answer exposed only by a CONTRADICTION with b377 own record. '
        'THE MATCHER NOW ACCEPTS BOTH CONVENTIONS and the sweep found NOT ONE citing "\n'
        '     " document using the dotted convention alone, so b376 DOTTED-ONLY axis-B predicate '
        'COULD NOT HAVE PASSED ANY OF THEM -- WHICH IS WHAT SELECTED THE SIX. ' + str(AR['confirmed'])
        + ' of "\n'
        '     " ' + str(AR['ordered_population']) + ' archive files the mirror carries are CONFIRMED '
        'PRESENT by digest AND title line and NEVER by filename. And one NOT DETERMINABLE document "\n'
        '     " was read by hand: ' + str(HD['located']) + ' of ' + str(HD['named'])
        + ' identifiers locate in exactly one kernel, SO THE HAND READ DECIDES WHAT THE TABLE SCAN '
        'COULD NOT.",\n'
        '     "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED AND NO LIST '
        'CLOSED. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL. ### NO ARCHIVE FILE WAS"\n'
        '     " REMOVED, MOVED OR RENAMED; the removal is the author and depends on this report. ### '
        'NO DOCUMENT WAS REWRITTEN INTO THE OTHER CONVENTION: bare and dotted are both"\n'
        '     " correct in their own dialect. ### AN ABSENCE IS ONLY REPORTED FROM A SEARCH THAT '
        'PROVED IT CAN FIND A PRESENCE, and a git exit above 1 is an error and not an answer."\n'
        '     " ### A NAME DECLARED IN MORE THAN ONE KERNEL IS NOT A TERMINAL A DOCUMENT CAN CITE. '
        '### b376 AXIS-B COLUMN IS NAMED AS SUSPECT AND NOT RE-MEASURED. ### THE FOUR OPEN"\n'
        '     " LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED. ### NO '
        'LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2"\n'
        '     " UNCHANGED",\n'
        '     "data/b378_the_refs_widened.txt; data/' + TM['run_file'] + '; data/' + AR['run_file']
        + '; data/' + HD['run_file'] + '; data/' + LG['run_file'] + ';"\n'
        '     " data/b378_registration_2026-09-08.txt (LOCKED before any write, CHAINED ON A LOCK '
        'GATE THAT CHECKS WHAT EACH GATE READ -- ' + str(LG['gates_read']) + ' gates read, '
        + str(LG['face_subject_gates']) + ' checked by digest);"\n'
        '     " tools/gate_hash.py (SHARED, new: it stamps a gate record with the sha256 of what the '
        'gate read); tools/b378_lockgate.py (fixtured in FOUR polarities);"\n'
        '     " tools/b378_terminals.py (every ref, both conventions, and a positive control that '
        'must find a presence before any absence is reported); tools/b378_archives.py;"\n'
        '     " tools/b378_hand.py; PLACE-papers OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row '
        + str(rownum) + '"),\n')
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
    if "'an-upper-bound-at-one-ref'" not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if '"an-upper-bound-at-one-ref"' not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    open(INDEX + '.tmp', 'wb').write(txt.encode('utf-8'))
    os.replace(INDEX + '.tmp', INDEX)
    ok = True
    out, rc = query('an-upper-bound-at-one-ref')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : an-upper-bound-at-one-ref returns %d row(s)  %s'
        % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'an-upper-bound-at-one-ref' in o
        ok = ok and g
        rec('    %-44s reaches the b378 key : %s' % (q, g))
    for lbl, cond in (('no class ruled, no declaration moved',
                       'NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED' in out),
                      ('no corpus document written into',
                       'NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL' in out),
                      ('no archive removed', 'NO ARCHIVE FILE WAS' in out and 'REMOVED' in out),
                      ('neither convention rewritten',
                       'NO DOCUMENT WAS REWRITTEN INTO THE OTHER CONVENTION' in out),
                      ('an absence needs a proved search',
                       'PROVED IT CAN FIND A PRESENCE' in out),
                      ('a name in two kernels is not citable',
                       'MORE THAN ONE KERNEL IS NOT A TERMINAL' in out),
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
    rec('b378 -- THE DESK UNDER (R7), AND THE THREE CLOSING WRITES.')
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
        run_clock.write(D, 'b378_desk_notes', LINES)
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b378_desk_notes', LINES)
        return 1
    g1 = ('AN UPPER BOUND TAKEN AT ONE REF IS NOT A COUNT' in ROWS[0][0]
          and 'CHECKS WHAT EACH GATE READ' in ROWS[0][1]
          and 'RE-RUN AND RE-STAMPED' in ROWS[0][1]
          and 'ENUMERATED LIVE' in ROWS[0][1]
          and 'ONLY ON A TAG' in ROWS[0][1]
          and 'COULD NOT RUN' in ROWS[0][1] or 'DIED' in ROWS[0][1]
          and 'NAMED AS SUSPECT AND NOT RE-MEASURED' in ROWS[0][1]
          and 'NEVER BY FILENAME' in ROWS[0][1]
          and 'NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN' in ROWS[0][2]
          and 'NO CLASS WAS RULED' in ROWS[0][3]
          and 'NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL' in ROWS[0][3]
          and 'UPPER BOUND TAKEN AT ONE REF' in ROWS[0][4]
          and 'PROVED IT CAN FIND A PRESENCE' in ROWS[0][4]
          and 'DISCRIMINATION ARM' in ROWS[0][4]
          and 'THE REFS WIDENED' in ROWS[0][5]
          and 'NO LIST WAS CLOSED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says the upper bound, the stamped lock gate, the live refs, the tag, the '
        'broken sweep, the suspect column, never-by-filename, no terminal claimed, no class ruled, '
        'no corpus document written into, the proved search, and the scope : %s' % g1)
    if not g1:
        run_clock.write(D, 'b378_desk_notes', LINES)
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
            run_clock.write(D, 'b378_desk_notes', LINES)
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
    p = run_clock.write(D, 'b378_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok, lists_closed=0,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b378_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
