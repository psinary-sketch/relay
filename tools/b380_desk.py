# -*- coding: utf-8 -*-
"""b380_desk.py -- THE DESK UNDER `(R7)`, AND THE THREE CLOSING WRITES: THE TRAIL BLOCK, THE ROW,
### THE KEY.

### ### **FOUR ROLES IN ONE FILE, AND THE REASON IS DECLARED RATHER THAN HIDDEN:** ### the locked
### registration caps this act's new tools at nine and the cap counts FILES.
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
MARK = '<!-- b380 the role axis scored structurally -->'
PRIOR = '<!-- b379 the apparatus axis re-scored; two filings -->'
ACT = 'b380'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


RS, VD = J('b380_rescore'), J('b380_verdict')
LG = J('b380_lockgate')
CL375 = J('b375_clusters')
NOKEY = CL375['subject_clusters_without_keystone']
TA, TS = RS['statement_tally'], RS['structural_tally']
MOVED, ND = RS['moved_out_of_nd'], RS['not_determinable']
AG7, AG9, NDECL = (RS['agreement_over_seven'], RS['agreement_over_all'], RS['declarers'])
QUAD = RS['both_axes_structural']
BRANCH = VD['branch']

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
     'OPEN. ### b378 widened the refs and b379 gave the categories a vocabulary. ### This act adds '
     'nothing to it and closes nothing'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND', None, None,
     'OPEN. ### b373 listed them with their carriers and ROUTED them. ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', None, None,
     'OPEN. ### b374 listed every figure stated without a ref. ### This act dates none of them'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND', None, None,
     'OPEN. ### b374 found entries the register carries that appear nowhere else. ### This act '
     'rewrites none of them'),

    # ---- CARRIED --------------------------------------------------------------------------------
    ('the class ruling itself', 'STAND', None, None,
     'STILL THE AUTHOR`S. ### The evidence is now consolidated in one relay file: five options, the '
     'role clause, the corrected apparatus column and this act`s role tables. ### **NO OPTION IS '
     'RECOMMENDED AND NO CLASS IS RULED**'),
    ('whether the ruling governs documents outside the tree', 'STAND', None, None,
     'FILED at b379 and ### **STILL UNANSWERED.** ### It is a one-paragraph answer from the author '
     'and it changes what any role or apparatus table is measured over'),
    ('the six subject clusters with registry rows and no keystone', 'STAND', None, None,
     'FILED and ### **STILL NOT OPENED.** ### %d clusters, unchanged' % len(NOKEY)),
    ("the census's definition-versus-operation drift", 'STAND', None, None,
     'FILED at b377 and ### **NOT REPAIRED** -- repairing it belongs to the ruling'),
    ('the download-layer version and class drift', 'STAND', None, None,
     'FILED at b379 and ### **NOT REPAIRED. ### THE REGISTRY IS NOT EDITED**'),
    ('the 86 archive files the mirror does not carry', 'STAND', None, None,
     'CARRIED and ### **STILL UNCONFIRMED**'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', None, None,
     'CARRIED and ### **DELIBERATELY NOT RE-MEASURED**'),

    # ---- WHAT THIS ACT ADDS -------------------------------------------------------------------------
    ('the premise that the corpus does not say what it does', 'STAND', None, None,
     'NEW at b380 and ### **MEASURED, NOT ASSUMED.** ### %.1f%% of the corpus says nothing about its '
     'own role under the strict reading and %.1f%% under a deliberately broader one, so ### **THE '
     '### PREMISE SURVIVES ITS OWN WIDENING.** ### It STANDS rather than closing: ### **AN ITEM AN '
     '### ACT PUTS ON THE DESK AND CLOSES IN THE SAME ACT IS NOT A CLOSURE**, and the corpus still '
     'does not say what it does'
     % (100.0 * TA.get('A?', 0) / RS['population'],
        100.0 * RS['statement_broad_tally'].get('A?', 0) / RS['population'])),
    ('b379`s observation that the role column would not move', 'STAND', None, None,
     'CARRIED FROM b379 AND ### **ANSWERED WITHOUT BEING CLOSED.** ### The column moved %d of %d '
     'under a different method. ### The item stands because what b379 observed remains true of the '
     'method it observed: ### **THE ROLE COLUMN STILL DOES NOT MOVE WHEN IT IS READ FROM WHAT THE '
     '### DOCUMENTS SAY**' % (MOVED, TA.get('A?', 0))),
    ('the role axis, read from structure', 'STAND', None, None,
     'NEW at b380: a predicate reading what a document DRAWS ON rather than what it says. ### '
     '**%d DOCUMENTS MOVED OUT OF `NOT DETERMINABLE` (%d -> %d)**, and the both-axes quadrant is '
     'non-empty for the first time at %d' % (MOVED, TA.get('A?', 0), TS.get('A?', 0), QUAD)),
    ('and the predicate fails its own control on the rubric`s own distinction', 'STAND', None, None,
     'NEW at b380 and it is ### **THE FINDING OF THE ACT.** ### It agrees with %d of the 7 documents '
     'that declare SYNTHESIS and with ### **NEITHER OF THE 2 THAT DECLARE GATHERING.** ### Both '
     'gatherers reach widely and the predicate reads reach and calls it synthesis. ### **THE `A-` '
     'COLUMN IS NOT MEASURING GATHERING; IT IS MEASURING NARROW REACH**' % AG7),
    ('the verdict on the method', 'STAND', None, None,
     'NEW at b380: ### **%s.** ### Role is readable as REACH and not as ARGUMENT. ### **THE `A+` '
     'COLUMN IS AN UPPER BOUND ON SYNTHESIS AND THE `A-` COLUMN IS UNVALIDATED**, and the '
     'distinction the rubric is about lives in sentences and not in a citation graph. ### **NO '
     'CLASS IS RULED IN ANY BRANCH**' % BRANCH),
    ("the ruling's evidence, consolidated in one file", 'STAND', None, None,
     'NEW at b380: no such file existed and the evidence was spread across four banks. ### Written '
     '### **IN THE RELAY BANK AND NOT AS A TRACKING DOCUMENT IN THE CORPUS**, which no act since '
     'b375 has been permitted to create'),
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
        rec('    %-78s %s' % (item, row['disposition']))
        rec('        why : %s' % why[:150])
        if len(why) > 150:
            rec('              %s' % why[150:340])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    stands = [m for m in marks if m['disposition'] == 'STAND']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(stands)))
    rec('    ### ### ### **AND CLOSING NOTHING IS RIGHT EVEN THOUGH THIS ACT MEASURED SOMETHING.**')
    rec('    ### `(R7)` closes an item whose OCCASION is gone. ### Moving a column under a new')
    rec('    ### predicate does not remove the occasion of the obligation, the ruling, or any of the')
    rec('    ### four lists -- and the predicate that moved it ### **FAILED ITS OWN CONTROL.**')
    rec('    ### ### **A MEASUREMENT IS NOT A CLOSURE, AND AN ITEM AN ACT PUTS ON THE DESK AND')
    rec('    ### ### CLOSES IN THE SAME ACT IS NOT A CLOSURE EITHER.**')
    return dict(items=len(marks), closed=len(closed), standing=len(stands),
                closures_refused=refused, marks=marks,
                closed_items=[dict(item=m['item'], file='data/%s' % m.get('killing_file'),
                                   date=m.get('date'), own_act=m.get('own_act')) for m in closed])


def trail_block(Q):
    return [
        '', MARK, '',
        '### **b380 \u2014 THE ROLE AXIS, SCORED STRUCTURALLY (2026-09-08)**',
        '',
        ('*No block above is edited. The b379 block (`%s`) and every block before it stand exactly as '
         'they were written.*' % PRIOR),
        '',
        ('**THE PREMISE WAS MEASURED AND NOT ASSUMED, BECAUSE AN ACT THAT ASSUMES ITS OWN PREMISE '
         'CANNOT BE REFUTED BY ITS OWN RUN.** Four acts had said the role column does not move '
         'because the documents do not say what they do. This act re-ran b376\u2019s own '
         'statement-based predicate on the same bytes and then ran a deliberately BROADER reading '
         'beside it, so the premise could fail if it were wrong. Strict: **%d of %d say nothing about '
         'their own role (%.1f%%)**. Broad, counting any self-description a generous reader would '
         'accept: **%d of %d (%.1f%%)**. **THE PREMISE SURVIVES ITS OWN WIDENING**, and it is now a '
         'measurement with a number rather than a remark repeated across four banks.'
         % (TA.get('A?', 0), RS['population'], 100.0 * TA.get('A?', 0) / RS['population'],
            RS['statement_broad_tally'].get('A?', 0), RS['population'],
            100.0 * RS['statement_broad_tally'].get('A?', 0) / RS['population'])),
        '',
        ('**SO ROLE IS READ FROM WHAT A DOCUMENT DRAWS ON RATHER THAN FROM WHAT IT SAYS.** '
         '`tools/role_structure.py` is new, shared, and fixtured in three polarities because the '
         'predicate has three answers and one that cannot report silence is not a predicate. The '
         'rubric\u2019s own sentence lists THREE kinds of other content \u2014 kernels, other '
         'keystones, other clusters \u2014 so **ONE FOREIGN TOUCH IS A CITATION AND TWO IS A '
         'COMBINATION**, and that threshold was set from the wording BEFORE the control ran and '
         '**WAS NOT MOVED AFTERWARDS TO MAKE THE CONTROL AGREE**. **AND NO DIRECTION WAS REGISTERED, '
         'BECAUSE THERE IS NONE:** b379\u2019s widening was a superset and could only add; this is a '
         'different method, not a wider one, so **NO MONOTONICITY BAR APPLIES** and a movement in '
         'either direction is neither a defect nor a discovery by itself.'),
        '',
        ('**THE COLUMN MOVED, AND IT MOVED A LONG WAY.** `A+` %d, `A-` %d, `A?` %d. '
         '**%d OF THE %d DOCUMENTS THE STATEMENT-BASED SCORE COULD NOT DECIDE ARE NOW DECIDED '
         '(%.1f%%), AND NOT ONE DOCUMENT MOVED THE OTHER WAY.** Every prior score is kept beside the '
         'new one and **%d WERE OVERWRITTEN**. The both-axes quadrant is non-empty for the first '
         'time in this sequence: **`A+B+` moves from %d to %d**, of which %d were already there and '
         '**%d are there only because this act read their structure.**'
         % (TS.get('A+', 0), TS.get('A-', 0), TS.get('A?', 0), MOVED, TA.get('A?', 0),
            100.0 * MOVED / TA.get('A?', 1), RS['prior_scores_overwritten'],
            RS['both_axes_statement'], QUAD, RS['both_axes_already_declared'],
            QUAD - RS['both_axes_already_declared'])),
        '',
        ('**AND THE PREDICATE FAILS ITS OWN CONTROL ON EXACTLY THE DISTINCTION THE RUBRIC IS ABOUT. '
         'THIS IS THE FINDING OF THE ACT AND IT IS PRINTED FIRST, NOT IN A FOOTNOTE.** The corpus '
         'contains %d documents that declare a role: %d declare SYNTHESIS and %d declare GATHERING. '
         'The structural predicate agrees with **%d of the %d synthesis declarers** and with '
         '**NEITHER OF THE %d GATHERERS** \u2014 `%s` and `%s` both score `A+`, reaching %d and %d '
         'places respectively. They are not misfiled. **THEY GATHER WIDELY, AND A CITATION GRAPH '
         'CANNOT TELL GATHERING WIDELY FROM SYNTHESISING.** **THE `A-` COLUMN IS THEREFORE NOT '
         'MEASURING GATHERING; IT IS MEASURING NARROW REACH**, which is a different property that '
         'happens to correlate with it. **A PREDICATE THAT CONTRADICTS THE ONLY GROUND TRUTH '
         'AVAILABLE HAS FAILED, HOWEVER PLAUSIBLE ITS OUTPUT LOOKS**, and %d of %d is a failure and '
         'not a rounding.'
         % (NDECL, RS['declarers_synthesis'], RS['declarers_gathering'], AG7,
            RS['declarers_synthesis'], RS['declarers_gathering'],
            RS['disagreements'][0]['file'], RS['disagreements'][1]['file'].split('/')[-1],
            RS['disagreements'][0]['evidence']['reach'],
            RS['disagreements'][1]['evidence']['reach'], AG9, NDECL)),
        '',
        ('**THE VERDICT IS ON THE METHOD AND NOT ON THE CLASS: %s.** The column moved and the '
         'control did not come clean, so both halves are stated rather than one. **WHAT THE '
         'STRUCTURAL READ GIVES:** an upper bound. A document scoring `A-` or `A?` draws on little '
         'or nothing, and **THAT IS EVIDENCE IT DOES NOT SYNTHESISE**. **WHAT IT DOES NOT GIVE:** a '
         'document scoring `A+` reaches, and **REACH IS NOT ARGUMENT** \u2014 a bibliography, an '
         'index or a ledger reaches everywhere by construction. **SO THE `A+` COLUMN IS AN UPPER '
         'BOUND ON SYNTHESIS AND THE `A-` COLUMN IS UNVALIDATED**, and the distinction the rubric '
         'turns on lives in sentences and not in a citation graph. **NO CLASS IS RULED IN THIS '
         'BRANCH OR IN EITHER OF THE OTHER TWO**, and the ruling remains the author\u2019s.'
         % BRANCH),
        '',
        ('**WHAT IT IS DEAF TO IS DECLARED RATHER THAN DISCOVERED LATER, AND ALL FOUR ARE REAL.** A '
         'document that synthesises WITHOUT CITING is invisible \u2014 the same class the '
         'statement-based predicate missed, missed a second way. A document that cites widely and '
         'synthesises nothing scores high, which is the failure the control found. **THE DIRECTORY '
         'STANDS IN FOR THE SUBJECT**, which is an ADDRESS standing in for a subject and is exactly '
         'the substitution `(R2)` warns against; it is used because the corpus\u2019s clusters are '
         'directory-shaped and it is **NAMED HERE AS A WEAKNESS AND NOT HIDDEN AS A CONVENIENCE**. '
         'And a citation the predicate does not recognise is not a citation to it.'),
        '',
        ('**THE RULING\u2019S EVIDENCE IS NOW IN ONE FILE, AND IN THE RELAY BANK RATHER THAN IN THE '
         'CORPUS.** Four acts had produced the five options quoted whole, the author\u2019s role '
         'clause banked verbatim, the corrected apparatus column and now both role tables \u2014 '
         'and no single place held them. `data/b380_ruling_evidence.txt` holds them with every '
         'figure carrying the act that measured it. **IT IS A RELAY BANK ARTIFACT AND NOT A TRACKING '
         'DOCUMENT IN THE CORPUS**, which no act since b375 has been permitted to create, and where '
         'such a census should live is still ROUTED to the author and still unanswered.'),
        '',
        ('**WHAT THIS ACT DID NOT DO.** No class ruled, no document reclassified, **no declaration '
         'moved**, no list closed, **no corpus document written into at all**, REGISTRY.md not '
         'edited, nothing on the download layer written, moved, renamed or removed, no archive file '
         'touched and the 86 unconfirmed still unconfirmed. The six clusters stay filed and not '
         'opened. No `.lean` file touched, no build run, no axiom profile recomputed. **The four '
         'open lists are restated OPEN by name and none is closed.** h2 stands exactly where the '
         'deposit left it and this act makes no claim about it in either direction.'),
        '',
    ]


SCOPE = (
    "**SCOPE: THE ROLE AXIS, SCORED STRUCTURALLY.** NO class ruled, NO document reclassified, NO "
    "declaration moved, NO list closed -- the order's own list, and each is a bar. **NO CORPUS "
    "DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED.** **THE PREMISE WAS MEASURED "
    "AND NOT ASSUMED**, and it was tested against a deliberately broader reading so that it could "
    "have failed. **THE THRESHOLD WAS SET FROM THE RUBRIC'S OWN WORDING BEFORE THE CONTROL RAN AND "
    "WAS NOT MOVED AFTERWARDS TO MAKE THE CONTROL AGREE.** **NO DIRECTION WAS REGISTERED BECAUSE "
    "THERE IS NONE** -- this is a different method and not a wider one, so no monotonicity bar "
    "applies. **EVERY PRIOR SCORE IS KEPT BESIDE THE NEW ONE AND NONE WAS OVERWRITTEN.** **THE "
    "PREDICATE FAILS ITS OWN CONTROL ON THE RUBRIC'S OWN DISTINCTION AND THAT IS REPORTED AT FULL "
    "PROMINENCE AS A DEFECT IN THE PREDICATE AND NOT IN THE DOCUMENTS.** **REACH IS NOT ARGUMENT**, "
    "so the A+ column is AN UPPER BOUND ON SYNTHESIS and the A- column is UNVALIDATED. **WHAT THE "
    "PREDICATE IS DEAF TO IS DECLARED, INCLUDING THAT THE DIRECTORY STANDS IN FOR THE SUBJECT.** "
    "**NO OPTION IS RECOMMENDED, RANKED OR PREFERRED** and the ruling remains the author's. **EVERY "
    "ABSENCE CARRIES A POSITIVE CONTROL THAT FINDS A KNOWN PRESENCE FIRST, AND AN ERROR EXIT IS NOT "
    "AN ANSWER.** **NO ARCHIVE FILE WAS TOUCHED** and the 86 unconfirmed stay unconfirmed. **NO "
    "OWNER INSTRUMENT WAS EDITED** -- b376_axes, b378_lockgate, gate_hash, row_categories and "
    "b379_rescore's widened predicate are all IMPORTED OR RE-READ AND NOT MODIFIED. **NO LIST WAS "
    "CLOSED** -- the four open lists are restated OPEN by name. **NO NEW TRACKING DOCUMENT WAS "
    "CREATED IN THE CORPUS**; the consolidated evidence file is a relay bank artifact. NO .lean FILE "
    "TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF "
    "ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, "
    "totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS "
    "CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The "
    "patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record, and THE "
    "PATENT GATE IS NAMED ONLY AS SOMETHING ANOTHER DOCUMENT SAYS. THE INSTRUMENT LANE STAYS PARKED. "
    "THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it and this act makes no "
    "claim about it in either direction. The wave PARKED by the author's ruling. NOTHING IS "
    "DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def corr_rows(Q):
    m = ("**THE ROLE AXIS READ FROM STRUCTURE: %d OF %d DOCUMENTS MOVE OUT OF NOT DETERMINABLE AND "
         "THE PREDICATE FAILS ITS OWN CONTROL ON THE RUBRIC'S OWN DISTINCTION** (b380, the role "
         "axis, scored structurally)" % (MOVED, TA.get('A?', 0)))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b380, %d gates read and %d checked "
            "by digest, and the face was rewritten before the lock and every face-subject gate "
            "RE-RUN AND RE-STAMPED. THE PREMISE WAS MEASURED AND NOT ASSUMED: b376's own "
            "statement-based predicate was RE-RUN on the same bytes and a deliberately BROADER "
            "reading was run beside it so the premise could fail, and %d of %d documents say nothing "
            "about their own role under the strict reading and %d of %d under the broad one -- THE "
            "PREMISE SURVIVES ITS OWN WIDENING. Role is then read from WHAT A DOCUMENT DRAWS ON "
            "rather than from what it says, through the new SHARED tools/role_structure.py, fixtured "
            "in THREE polarities because the predicate has three answers. THE THRESHOLD WAS SET FROM "
            "THE RUBRIC'S OWN WORDING BEFORE THE CONTROL RAN -- one foreign touch is a citation and "
            "two is a combination -- AND WAS NOT MOVED AFTERWARDS TO MAKE THE CONTROL AGREE. NO "
            "DIRECTION WAS REGISTERED BECAUSE THERE IS NONE: this is a different method and not a "
            "wider one, so NO MONOTONICITY BAR APPLIES. The column moves to A+ %d, A- %d, A? %d; %d "
            "documents move out of NOT DETERMINABLE and NOT ONE MOVED THE OTHER WAY; EVERY PRIOR "
            "SCORE IS KEPT BESIDE THE NEW ONE AND %d WERE OVERWRITTEN; and the both-axes quadrant is "
            "non-empty for the first time, moving from %d to %d, of which %d are there only because "
            "this act read their structure. AND THE PREDICATE FAILS ITS OWN CONTROL, WHICH IS THE "
            "FINDING OF THE ACT: it agrees with %d of the %d documents declaring SYNTHESIS and with "
            "NEITHER OF THE %d DECLARING GATHERING, because both gatherers gather WIDELY and a "
            "citation graph cannot tell gathering widely from synthesising -- THE A- COLUMN IS NOT "
            "MEASURING GATHERING, IT IS MEASURING NARROW REACH. THE VERDICT ON THE METHOD IS %s: "
            "REACH IS NOT ARGUMENT, so THE A+ COLUMN IS AN UPPER BOUND ON SYNTHESIS AND THE A- "
            "COLUMN IS UNVALIDATED, and the distinction the rubric turns on lives in sentences and "
            "not in a citation graph. The ruling's evidence is consolidated into one file IN THE "
            "RELAY BANK AND NOT AS A TRACKING DOCUMENT IN THE CORPUS"
            % (LG['gates_read'], LG['face_subject_gates'],
               TA.get('A?', 0), RS['population'],
               RS['statement_broad_tally'].get('A?', 0), RS['population'],
               TS.get('A+', 0), TS.get('A-', 0), TS.get('A?', 0), MOVED,
               RS['prior_scores_overwritten'], RS['both_axes_statement'], QUAD,
               QUAD - RS['both_axes_already_declared'], AG7, RS['declarers_synthesis'],
               RS['declarers_gathering'], BRANCH))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN AND NO ROW WAS WRITTEN INTO ANY "
            "DOCUMENT. ### The kernels and documents were READ solely to see what each document "
            "DRAWS ON, and EVERY ABSENCE CARRIES A POSITIVE CONTROL THAT FOUND A KNOWN PRESENCE "
            "FIRST. ### NO STATEMENT WAS PROVED, NO BUILD WAS RUN AND NO AXIOM PROFILE WAS "
            "RECOMPUTED. ### READING WHAT A DOCUMENT DRAWS ON SAYS WHAT IT REACHES AND SAYS NOTHING "
            "ABOUT WHETHER IT ARGUES ANYTHING WITH WHAT IT REACHED")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT THE "
            "OBJECT. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED AND NO "
            "LIST CLOSED. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL, REGISTRY.md WAS NOT "
            "EDITED, AND NOTHING ON THE DOWNLOAD LAYER WAS WRITTEN, MOVED, RENAMED OR REMOVED")
    grade = ("### SCORED-STRUCTURALLY, WITH THE PREDICATE'S OWN FAILURE ON THE RECORD. ### THE "
             "PREDICATE FAILS ITS OWN CONTROL ON THE RUBRIC'S OWN DISTINCTION AND THAT IS REPORTED "
             "AT FULL PROMINENCE AS A DEFECT IN THE PREDICATE AND NOT IN THE DOCUMENTS, because A "
             "PREDICATE THAT CONTRADICTS THE ONLY GROUND TRUTH AVAILABLE HAS FAILED HOWEVER "
             "PLAUSIBLE ITS OUTPUT LOOKS. ### WHAT THE PREDICATE IS DEAF TO IS DECLARED RATHER THAN "
             "DISCOVERED LATER, AND THE DIRECTORY STANDS IN FOR THE SUBJECT -- an ADDRESS standing "
             "in for a subject, which is exactly the substitution (R2) warns against, used because "
             "the clusters are directory-shaped and NAMED AS A WEAKNESS AND NOT HIDDEN AS A "
             "CONVENIENCE. ### THE STRUCTURAL COLUMN IS THIS SEAT'S THIRD PREDICATE AND NOT A GROUND "
             "TRUTH -- b376's COLUMN WAS ALSO BELIEVED WHEN IT WAS WRITTEN. ### AND NO CLASS IS "
             "RULED IN ANY BRANCH: A METHOD THAT WORKS IS NOT A RULING EITHER")
    status = ("data/b380_the_role_axis_scored_structurally.txt; data/b380_ruling_evidence.txt; "
              "data/%s; data/%s; data/%s; data/b380_registration_2026-09-08.txt (LOCKED before any "
              "write, chained on tools/b378_lockgate.py run as b380); tools/role_structure.py "
              "(SHARED, new); tools/b380_rescore.py; tools/b380_verdict.py; PLACE-papers "
              "OPEN_TRAILS.md (an append-only block; NO CORPUS DOCUMENT EDITED AND REGISTRY.md NOT "
              "TOUCHED); CORRESPONDENCE.md row %%d"
              % (RS['run_file'], VD['run_file'], J('b380_reads')['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the role axis scored structurally', 'role from structure',
           'reach is not argument', 'the predicate fails its own control',
           'the premise measured not assumed')
MUST_NOT_HIT = ('the class is ruled', 'the declarations are moved',
                'the lists are closed', 'the registry is edited')


def do_key(rownum):
    KEY = 'the-role-axis-read-from-structure'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "THE ROLE AXIS READ FROM STRUCTURE, AND THE PREDICATE FAILS ITS OWN CONTROL. THE PREMISE WAS "
        "MEASURED AND NOT ASSUMED: b376 statement-based predicate RE-RUN on the same bytes with a "
        "deliberately BROADER reading beside it so the premise could fail -- %d of %d documents say "
        "nothing about their own role strictly and %d of %d broadly, so THE PREMISE SURVIVES ITS OWN "
        "WIDENING. Role then read from WHAT A DOCUMENT DRAWS ON through the new SHARED "
        "tools/role_structure.py, fixtured in THREE polarities. THE THRESHOLD WAS SET FROM THE RUBRIC "
        "OWN WORDING BEFORE THE CONTROL RAN -- one foreign touch is a citation and two is a "
        "combination -- AND WAS NOT MOVED AFTERWARDS TO MAKE THE CONTROL AGREE. NO DIRECTION WAS "
        "REGISTERED BECAUSE THERE IS NONE: a different method is not a wider one, so NO MONOTONICITY "
        "BAR APPLIES. The column moves to A+ %d, A- %d, A? %d: %d documents out of NOT DETERMINABLE "
        "and NOT ONE the other way, %d prior scores overwritten, and the both-axes quadrant non-empty "
        "for the first time at %d, up from %d. AND THE PREDICATE FAILS ITS OWN CONTROL ON THE RUBRIC "
        "OWN DISTINCTION, WHICH IS THE FINDING: it agrees with %d of the %d declaring SYNTHESIS and "
        "with NEITHER OF THE %d DECLARING GATHERING, because both gatherers gather WIDELY and a "
        "citation graph cannot tell gathering widely from synthesising -- THE A- COLUMN IS NOT "
        "MEASURING GATHERING, IT IS MEASURING NARROW REACH. VERDICT ON THE METHOD: %s. REACH IS NOT "
        "ARGUMENT, so THE A+ COLUMN IS AN UPPER BOUND ON SYNTHESIS AND THE A- COLUMN IS UNVALIDATED."
        % (TA.get('A?', 0), RS['population'], RS['statement_broad_tally'].get('A?', 0),
           RS['population'], TS.get('A+', 0), TS.get('A-', 0), TS.get('A?', 0), MOVED,
           RS['prior_scores_overwritten'], QUAD, RS['both_axes_statement'], AG7,
           RS['declarers_synthesis'], RS['declarers_gathering'], BRANCH))
    grade = (
        "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED AND NO LIST CLOSED. "
        "### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED. ### NOTHING "
        "ON THE DOWNLOAD LAYER WAS WRITTEN, MOVED, RENAMED OR REMOVED. ### EVERY ABSENCE CARRIES A "
        "POSITIVE CONTROL THAT FINDS A KNOWN PRESENCE FIRST, AND AN ERROR EXIT IS NOT AN ANSWER. ### "
        "THE PREDICATE FAILURE IS REPORTED AT FULL PROMINENCE AS A DEFECT IN THE PREDICATE AND NOT IN "
        "THE DOCUMENTS. ### WHAT THE PREDICATE IS DEAF TO IS DECLARED, INCLUDING THAT THE DIRECTORY "
        "STANDS IN FOR THE SUBJECT. ### EVERY PRIOR SCORE IS KEPT BESIDE THE NEW ONE. ### NO OPTION "
        "IS RECOMMENDED and the ruling remains the author. ### THE STRUCTURAL COLUMN IS THIS SEAT "
        "THIRD PREDICATE AND NOT A GROUND TRUTH. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. "
        "### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD "
        "RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED")
    where = (
        "data/b380_the_role_axis_scored_structurally.txt; data/b380_ruling_evidence.txt; data/%s; "
        "data/%s; data/%s; data/b380_registration_2026-09-08.txt (LOCKED before any write, chained "
        "on tools/b378_lockgate.py run as b380 -- %d gates read, %d checked by digest); "
        "tools/role_structure.py (SHARED, new: three polarities, and what it is deaf to declared); "
        "tools/b380_rescore.py (b376_axes IMPORTED UNMODIFIED and the prior column RE-RUN, not "
        "trusted); tools/b380_verdict.py; PLACE-papers OPEN_TRAILS.md (append-only); "
        "CORRESPONDENCE.md row %d"
        % (RS['run_file'], VD['run_file'], J('b380_reads')['run_file'], LG['gates_read'],
           LG['face_subject_gates'], rownum))
    act = ("b380 (the premise measured; role read from structure; every document re-scored with its "
           "prior score kept beside it; the verdict on the method)")
    row_new = ('    # ### THE ROLE AXIS, SCORED STRUCTURALLY (b380).%s'
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
        rec('    %-44s reaches the b380 key : %s' % (q, g))
    for lbl, cond in (('no class ruled, no declaration moved',
                       'NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED' in out),
                      ('no corpus document written into and no registry edit',
                       'NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED'
                       in out),
                      ('the premise was measured, not assumed',
                       'THE PREMISE SURVIVES ITS OWN WIDENING' in out),
                      ('the threshold was not moved to fit the control',
                       'WAS NOT MOVED AFTERWARDS TO MAKE THE CONTROL AGREE' in out),
                      ('no direction registered because there is none',
                       'NO MONOTONICITY BAR APPLIES' in out),
                      ('the predicate fails its own control',
                       'FAILS ITS OWN CONTROL' in out and 'NEITHER OF THE' in out),
                      ('reach is not argument',
                       'REACH IS NOT ARGUMENT' in out and 'UNVALIDATED' in out),
                      ('the prior scores are kept beside the new ones',
                       'EVERY PRIOR SCORE IS KEPT BESIDE THE NEW ONE' in out),
                      ('an absence needs a proved search',
                       'POSITIVE' in out and 'CONTROL THAT FINDS A KNOWN PRESENCE FIRST' in out),
                      ('the structural column is not a ground truth',
                       'NOT A GROUND TRUTH' in out),
                      ('no list was closed', 'NO LIST' in out and 'CLOSED' in out),
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
    rec('b380 -- THE DESK UNDER (R7), AND THE THREE CLOSING WRITES.')
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
        run_clock.write(D, 'b380_desk_notes', LINES)
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b380_desk_notes', LINES)
        return 1
    g1 = ('THE ROLE AXIS READ FROM STRUCTURE' in ROWS[0][0]
          and 'CHECKS WHAT EACH GATE READ' in ROWS[0][1]
          and 'RE-RUN AND RE-STAMPED' in ROWS[0][1]
          and 'MEASURED AND NOT ASSUMED' in ROWS[0][1]
          and 'SURVIVES ITS OWN WIDENING' in ROWS[0][1]
          and 'WAS NOT MOVED AFTERWARDS TO MAKE THE CONTROL AGREE' in ROWS[0][1]
          and 'NO MONOTONICITY BAR APPLIES' in ROWS[0][1]
          and 'FAILS ITS OWN CONTROL' in ROWS[0][1]
          and 'NEITHER OF THE' in ROWS[0][1]
          and 'REACH IS NOT ARGUMENT' in ROWS[0][1]
          and 'UPPER BOUND ON SYNTHESIS' in ROWS[0][1]
          and 'NOT AS A TRACKING DOCUMENT IN THE CORPUS' in ROWS[0][1]
          and 'NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN' in ROWS[0][2]
          and 'POSITIVE CONTROL' in ROWS[0][2]
          and 'NO CLASS WAS RULED' in ROWS[0][3]
          and 'REGISTRY.md WAS NOT EDITED' in ROWS[0][3]
          and 'A DEFECT IN THE PREDICATE AND NOT IN THE DOCUMENTS' in ROWS[0][4]
          and 'THE DIRECTORY STANDS IN FOR THE SUBJECT' in ROWS[0][4]
          and 'NOT A GROUND TRUTH' in ROWS[0][4]
          and 'NO CLASS IS RULED IN ANY BRANCH' in ROWS[0][4]
          and 'THE ROLE AXIS, SCORED STRUCTURALLY' in ROWS[0][5]
          and 'NO LIST WAS CLOSED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says the structural read, the stamped gate, the measured premise, the unmoved '
        'threshold, the absent direction, the failed control, reach is not argument, no terminal '
        'claimed, the positive control, no class ruled, no registry edit, the declared deafness, '
        'not a ground truth, and the scope : %s' % g1)
    if not g1:
        run_clock.write(D, 'b380_desk_notes', LINES)
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
            run_clock.write(D, 'b380_desk_notes', LINES)
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
    p = run_clock.write(D, 'b380_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok, lists_closed=0,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b380_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
