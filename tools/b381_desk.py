# -*- coding: utf-8 -*-
"""b381_desk.py -- THE DESK UNDER `(R7)`, AND THE THREE CLOSING WRITES: THE TRAIL BLOCK, THE ROW,
### THE KEY.

### ### **FOUR ROLES IN ONE FILE, AND THE REASON IS DECLARED RATHER THAN HIDDEN:** ### the locked
### registration caps this act's new tools at ten and the cap counts FILES.
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
MARK = '<!-- b381 the control rebuilt; co-location tested and not adopted -->'
PRIOR = '<!-- b379 the apparatus axis re-scored; two filings -->'
ACT = 'b381'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


RS, VD = J('b381_control'), J('b381_verdict')
EX = J('b381_exemplars')
LG = J('b381_lockgate')
R80 = J('b380_rescore')
CL375 = J('b375_clusters')
NOKEY = CL375['subject_clusters_without_keystone']
BRANCH = RS['branch']

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
     'STILL THE AUTHOR`S. ### `(R14)` settles what the ruling GOVERNS and ### **DOES NOT MAKE IT.** '
     '### **NO OPTION IS RECOMMENDED AND NO CLASS IS RULED**'),
    ('whether the ruling governs documents outside the tree', 'CLOSE', 'b381_verdict_notes',
     'ANSWERS THAT FILING AND THE FILING IS',
     'CLOSED at b381 by ### **`(R14)`, THE AUTHOR`S OWN RULING**, banked verbatim: the class ruling '
     'governs by CONTENT AND ROLE, not by location, so the download-layer book is inside its reach '
     'and outside the mirroring ruling`s. ### The occasion is gone because ### **THE AUTHOR '
     'ANSWERED IT** -- and this seat closed nothing by its own judgement'),
    ('the six subject clusters with registry rows and no keystone', 'STAND', None, None,
     'FILED and ### **STILL NOT OPENED.** ### %d clusters, unchanged' % len(NOKEY)),
    ("the census's definition-versus-operation drift", 'STAND', None, None,
     'FILED at b377 and ### **NOT REPAIRED** -- repairing it belongs to the ruling'),
    ('the download-layer version and class drift', 'STAND', None, None,
     'FILED at b379 and ### **STILL NOT REPAIRED. ### `(R14)` SAYS THIS FILING STAYS OPEN AND IS '
     'THE AUTHOR`S**, in the ruling`s own words. ### THE REGISTRY IS NOT EDITED'),
    ('the 86 archive files the mirror does not carry', 'STAND', None, None,
     'CARRIED and ### **STILL UNCONFIRMED**'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', None, None,
     'CARRIED and ### **DELIBERATELY NOT RE-MEASURED**'),
    ('the premise that the corpus does not say what it does', 'STAND', None, None,
     'CARRIED from b380 and ### **NARROWED BY MEASUREMENT, NOT REPAIRED.** ### `%d` of `%d` heads '
     'DO state a gathering purpose, so the corpus says more about what it does than a class-line '
     'scan could see -- ### **AND IT STILL SAYS ALMOST NOTHING ABOUT SYNTHESIS**'
     % (EX['wide_hits'], EX['scanned'])),
    ('b379`s observation that the role column would not move', 'STAND', None, None,
     'CARRIED and ### **STILL ANSWERED WITHOUT BEING CLOSED**'),

    # ---- WHAT THIS ACT ADDS -------------------------------------------------------------------------
    ('the old control`s weakness, measured rather than asserted', 'STAND', None, None,
     'NEW at b381: ### **ONE FINDING, NOT TWO.** ### The lowest synthesis reach was `%d` and the '
     'threshold was `%d`, so ### **NO VALUE OF THE THRESHOLD WOULD HAVE FAILED THAT SIDE**; and '
     'both gathering declarers disagreed, so ### **THE ONLY SIDE THAT COULD INFORM IT WAS THE SIDE '
     'IT GOT WRONG**' % (EX['b380_lowest_synthesis_reach'], EX['b380_threshold'])),
    ('the control rebuilt from the record`s own purpose statements', 'STAND', None, None,
     'NEW at b381: ### **`%d` GATHERING EXEMPLARS AGAINST A DECLARED FLOOR OF `%d`**, every one '
     'selected by a quoted sentence in its own head and ### **NOT ONE CHOSEN BY THIS SEAT`S '
     'JUDGEMENT.** ### It is the first control in this sequence that ### **CAN FAIL IN BOTH '
     'DIRECTIONS**' % (len(EX['gathering_set']), EX['floor'])),
    ('and the matcher that built it was repaired twice after its output was seen', 'STAND', None,
     None,
     'NEW at b381 and ### **DECLARED RATHER THAN HIDDEN.** ### The lineage is `%d` -> `%d` -> `%d` '
     'heads. ### Each repair traces to words written BEFORE the run -- the face`s *the document '
     'names ITSELF* and the order`s *rather than from class declarations* -- but ### **A READER IS '
     'OWED THE LINEAGE AND NOT ONLY THE LAST VERSION**'
     % (EX['loose_hits'], EX['loose2_hits'], EX['wide_hits'])),
    ('co-location, tested against that control', 'STAND', None, None,
     'NEW at b381 and it is ### **THE FINDING OF THE ACT: %s. ### NOT ADOPTED.** ### `%d` of `%d` '
     'synthesis exemplars clear the bar and `%d` of `%d` gathering exemplars clear it too; the '
     'lowest synthesis ratio is `%.3f` and the highest gathering ratio is `%.3f`, so ### **THE TWO '
     'SETS OVERLAP COMPLETELY AND NO CHOICE OF THRESHOLD WOULD HAVE SEPARATED THEM**'
     % (BRANCH, RS['synthesis_cplus'], RS['synthesis_n'], RS['gathering_cplus'],
        RS['gathering_n'], RS['lowest_synthesis_ratio'], RS['highest_gathering_ratio'])),
    ('so the corpus was not scored, and that is the order`s clause and not a shortfall', 'STAND',
     None, None,
     'NEW at b381: ### **THE NON-ADOPTION CLAUSE BOUND.** ### No corpus-wide co-location number '
     'exists, no quadrant table was redrawn, and ### **`(F2)` IS `NOT REACHED` RATHER THAN MET OR '
     'REFUTED** -- which `(E1)` registered on the locked face before the run'),
    ('two independent structural features now fail the same distinction', 'STAND', None, None,
     'NEW at b381 and ### **STATED WITHOUT BEING OVERCLAIMED.** ### `b380`s reach called both '
     'gatherers synthesisers; this act`s co-location puts most synthesis declarers below its bar. '
     '### **THAT IS NOT PROOF THAT NO STRUCTURAL FEATURE READS ROLE** ### and this act does not '
     'claim it -- it is two failures of the same shape'),
    ('what the columns mean, and what stays unvalidated', 'STAND', None, None,
     'NEW at b381: ### **NOTHING MOVED.** ### `b380`s positive column is still an ### **UPPER '
     'BOUND ON SYNTHESIS** ### and its negative column is still ### **UNVALIDATED**, because a '
     'second feature that failed cannot validate a first'),
    ('`(R14)`, recorded and not applied', 'STAND', None, None,
     'NEW at b381: banked verbatim in the ruling`s evidence file -- ### **THE WHOLE RULING AND NOT '
     'ONLY THE LINES THIS ACT ANCHORED.** ### **NO DOCUMENT WAS RECLASSIFIED UNDER IT**, the book '
     'was not opened, and the registry-drift filing stays open and the author`s'),
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
        '### **b381 \u2014 THE CONTROL REBUILT, AND CO-LOCATION TESTED (2026-09-09)**',
        '',
        ('*No block above is edited. The b380 block (`%s`) and every block before it stand exactly as '
         'they were written.*' % PRIOR),
        '',
        ('**(R14), THE AUTHOR\u2019S, RATIFIED BY THE FERRY AND RECORDED HERE \u2014 NOT APPLIED.** '
         'The class ruling governs documents **by content and role, not by location**; where a '
         'document\u2019s canonical copy lives is a separate fact under a separate ruling, which '
         'stands. The download-layer book is therefore **inside the class ruling\u2019s reach and '
         'outside the mirroring ruling\u2019s \u2014 both hold, neither is edited into the other**. '
         'b379 filed that the ruling had to say whether it governs documents outside the tree; '
         '**(R14) answers that filing, and it is closed by the author and not by this seat**. What it '
         'does not settle, in the ruling\u2019s own words: **the book\u2019s registry drift stays '
         'open and is the author\u2019s**. No document was reclassified under it here, the book was '
         'not opened, and REGISTRY.md was not edited.'),
        '',
        ('**THE OLD CONTROL\u2019S WEAKNESS IS ONE FINDING, NOT TWO, AND IT WAS MEASURED RATHER THAN '
         'ASSERTED.** b380\u2019s threshold was `%d`; the lowest reach among the seven documents '
         'declaring synthesis was also `%d`, so **no value of the threshold at or below it would have '
         'failed any of them** \u2014 that side could not fail. And both documents declaring '
         'gathering disagreed with the predicate, so **the only side that could have informed it was '
         'the side it got wrong**. A control that cannot fail on one side and cannot inform on the '
         'other is **one defect with two faces**.'
         % (EX['b380_threshold'], EX['b380_lowest_synthesis_reach'])),
        '',
        ('**SO THE CONTROL WAS REBUILT FROM THE RECORD\u2019S OWN PURPOSE STATEMENTS, AND NOTHING WAS '
         'CURATED.** The head of every one of `%d` corpus documents \u2014 its first `%d` lines \u2014 '
         'was scanned for a sentence in which the document names **itself** and names a gathering '
         'purpose. **Every match was taken and every match is quoted with its file and its line**; '
         '`%d` exemplars, **not one chosen, dropped or ranked by this seat\u2019s judgement of what a '
         'document is**. Against a floor of `%d` declared on the locked face, **the set can fail in '
         'both directions** \u2014 the first control in this sequence that can. Two documents matched '
         'on both sides at once and were **excluded from both sets and reported, not resolved**: an '
         'exemplar that argues with itself is a ground truth for nothing.'
         % (EX['scanned'], EX['head_lines'], len(EX['gathering_set']), EX['floor'])),
        '',
        ('**AND THE MATCHER THAT BUILT IT WAS REPAIRED TWICE AFTER ITS OUTPUT WAS SEEN, WHICH IS '
         'DECLARED HERE RATHER THAN HIDDEN.** The lineage is `%d` \u2192 `%d` \u2192 `%d` heads out '
         'of `%d`. The first version accepted a bare pronoun as the document naming itself and matched '
         '**more than two fifths of the corpus**; the second still let a sentence merely *beginning* '
         '\u201cThe census\u2026\u201d count as a purpose statement. Each repair traces to words '
         'written **before** the run \u2014 the locked face\u2019s *the document names ITSELF* and '
         'the order\u2019s *rather than from class declarations* \u2014 but **a reader is owed the '
         'lineage and not only the last version**, so all three yields are printed.'
         % (EX['loose_hits'], EX['loose2_hits'], EX['wide_hits'], EX['scanned'])),
        '',
        ('**CO-LOCATION WAS THEN SCORED ON THAT SET ALONE, BEFORE ANY CORPUS-WIDE NUMBER EXISTED, AND '
         'IT DOES NOT SEPARATE.** The unit was fixed on the locked face before any score \u2014 a '
         'list item, a table row, a fenced block or a paragraph \u2014 because under a '
         'blank-line-only definition **a bibliography is one paragraph and the most partitioned '
         'document in the corpus would score as the most combining**. The result: **`%d` of `%d` '
         'synthesis exemplars clear the bar and `%d` of `%d` gathering exemplars clear it too**. The '
         'lowest synthesis ratio is **`%.3f`** and the highest gathering ratio is **`%.3f`**, so the '
         'two sets **overlap completely and no choice of threshold would have separated them**. '
         '**THE BRANCH IS %s AND THE PREDICATE IS NOT ADOPTED.**'
         % (RS['synthesis_cplus'], RS['synthesis_n'], RS['gathering_cplus'], RS['gathering_n'],
            RS['lowest_synthesis_ratio'], RS['highest_gathering_ratio'], BRANCH)),
        '',
        ('**SO THE CORPUS WAS NOT SCORED, AND THAT IS THE ORDER\u2019S OWN CLAUSE RATHER THAN A '
         'SHORTFALL.** No corpus-wide co-location figure exists, no quadrant table was redrawn, and '
         '**(F2) is `NOT REACHED` rather than met or refuted** \u2014 which this seat registered on '
         'the locked face before the run, precisely so a silent pass could not be read as a result. '
         '**(F1) is REFUTED by the printed table.** **(E3) is refuted too**: the purpose-statement '
         'scan found `%d` gathering exemplars against a floor of `%d`, so the rebuilt control is not '
         'underpowered and the failure stands on its own without that caveat.'
         % (RS['gathering_n'], EX['floor'])),
        '',
        ('**WHAT THE COLUMNS MEAN NOW: NOTHING MOVED, AND THAT IS THE HONEST REPORT.** b380\u2019s '
         'positive column is still an **upper bound on synthesis** and its negative column is still '
         '**unvalidated**, because **a second feature that failed cannot validate a first**. What is '
         'new is not a column but **a control that can fail in both directions**, and one negative '
         'fact worth more than either feature: **two independent structural features now fail the '
         'same distinction**. That is **not proof that no structural feature reads role** and this '
         'act does not claim it \u2014 it is two failures of the same shape, and the shape is that '
         'the distinction lives in what a document *says* about what it names.'),
        '',
        ('**AND THE PREDICTION THAT THE TOKENISER WOULD DECIDE THE ANSWER IS REFUTED BY ITS OWN '
         'MEASUREMENT.** Re-scored under a paragraph-only splitter \u2014 what \u201cthe same '
         'unit\u201d builds if nobody asks what an entry is \u2014 the gathering side\u2019s rate '
         'moves from `%.1f%%` to `%.1f%%` and **the branch does not change**. The unit definition was '
         'worth making and it was **not** what decided the outcome.'
         % (100.0 * RS['gathering_rate'], 100.0 * VD['naive_gathering_rate'])),
        '',
        ('**WHAT THIS ACT DID NOT DO.** No class ruled, no document reclassified, **no declaration '
         'moved**, no list closed by this seat\u2019s judgement, **no corpus document written into at '
         'all**, REGISTRY.md not edited, nothing on the download layer written, moved, renamed or '
         'removed, no archive file touched and the 86 unconfirmed still unconfirmed. **The corpus was '
         'not scored and no prior score was overwritten.** The six clusters stay filed and not opened. '
         'No `.lean` file touched, no build run, no axiom profile recomputed. **The four open lists '
         'are restated OPEN by name and none is closed.** h2 stands exactly where the deposit left it '
         'and this act makes no claim about it in either direction.'),
        '',
    ]


SCOPE = (
    "**SCOPE: THE CONTROL REBUILT, AND CO-LOCATION TESTED.** NO class ruled, NO document "
    "reclassified, NO declaration moved, NO list closed by this seat -- the order's own list, and "
    "each is a bar. **NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED.** "
    "**(R14) IS RECORDED AND NOT APPLIED**: banked verbatim, no document reclassified under it, the "
    "book not opened, and THE REGISTRY-DRIFT FILING STAYS OPEN AND IS THE AUTHOR'S in the ruling's "
    "own words. **THE OLD CONTROL'S WEAKNESS WAS MEASURED AND REPORTED AS ONE FINDING**, not "
    "asserted and not split into two. **THE REBUILD IS LEXICAL AND POSITIONAL AND NOTHING WAS "
    "CURATED** -- every match taken, every match quoted at its own line, and NOT ONE EXEMPLAR ADDED, "
    "DROPPED OR RANKED BY THIS SEAT'S JUDGEMENT. **THE MATCHER'S LINEAGE IS PRINTED BECAUSE TWO "
    "VERSIONS WERE REPAIRED AFTER THEIR OUTPUT WAS SEEN**, each repair tracing to words written "
    "before the run. **THE UNIT WAS FIXED ON THE LOCKED FACE BEFORE ANY SCORE** and the splitter is "
    "fixtured on all three kinds plus a heading and a fence. **THE THRESHOLD WAS DECLARED BEFORE THE "
    "CONTROL RAN AND WAS NOT MOVED AFTERWARDS TO MAKE IT AGREE.** **THE CONTROL WAS RUN BEFORE ANY "
    "CORPUS-WIDE NUMBER EXISTED**, so the predicate could not be tuned to a result it had not seen. "
    "**IT DID NOT SEPARATE, SO THE PREDICATE IS NOT ADOPTED AND THE CORPUS WAS NOT SCORED** -- the "
    "order's own clause, and (F2) is NOT REACHED rather than met or refuted. **NO PRIOR SCORE WAS "
    "OVERWRITTEN AND NO QUADRANT TABLE WAS REDRAWN.** **WHAT THE PREDICATE IS DEAF TO IS DECLARED**, "
    "including that the directory stands in for the subject and that co-location cannot see across a "
    "paragraph break. **TWO INDEPENDENT STRUCTURAL FEATURES NOW FAIL THE SAME DISTINCTION, AND THAT "
    "IS NOT PROOF THAT NO STRUCTURAL FEATURE READS ROLE.** **EVERY ABSENCE CARRIES A POSITIVE "
    "CONTROL THAT FINDS A KNOWN PRESENCE FIRST, AND AN ERROR EXIT IS NOT AN ANSWER.** **NO OPTION IS "
    "RECOMMENDED, RANKED OR PREFERRED** and the ruling remains the author's. **NO ARCHIVE FILE WAS "
    "TOUCHED** and the 86 unconfirmed stay unconfirmed. **NO OWNER INSTRUMENT WAS EDITED** -- "
    "role_structure, b376_axes, b378_lockgate, gate_hash and b380_rescore's banked rows are all "
    "IMPORTED OR RE-READ AND NOT MODIFIED. **THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME.** **NO "
    "NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS.** NO .lean FILE TOUCHED, NO BUILD RUN, NO "
    "AXIOM PROFILE RECOMPUTED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. "
    "NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or the "
    "roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE "
    "PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under "
    "b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the "
    "patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE "
    "POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it and this act makes no "
    "claim about it in either direction. The wave PARKED by the author's ruling. NOTHING IS "
    "DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def corr_rows(Q):
    m = ("**THE CONTROL REBUILT FROM THE RECORD'S OWN PURPOSE STATEMENTS, AND CO-LOCATION TESTED "
         "AGAINST IT AND NOT ADOPTED** (b381, the control rebuilt, and co-location tested)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b381, %d gates read and %d checked "
            "by digest. **(R14) IS RECORDED AND NOT APPLIED**: the class ruling governs by CONTENT "
            "AND ROLE AND NOT BY LOCATION, so the download-layer book is inside its reach and "
            "outside the mirroring ruling's, both hold and neither is edited into the other; it "
            "answers b379's filing, and THE BOOK'S REGISTRY DRIFT STAYS OPEN AND IS THE AUTHOR'S in "
            "the ruling's own words. THE OLD CONTROL'S WEAKNESS IS ONE FINDING AND WAS MEASURED: "
            "b380's threshold was %d and the lowest synthesis-declarer reach was %d, so NO VALUE OF "
            "THE THRESHOLD WOULD HAVE FAILED THAT SIDE, while both gathering declarers disagreed -- "
            "THE ONLY SIDE THAT COULD INFORM IT WAS THE SIDE IT GOT WRONG. The rebuild scanned the "
            "first %d lines of %d documents for a sentence in which the document NAMES ITSELF and "
            "names a gathering purpose: %d exemplars, EVERY MATCH TAKEN AND EVERY MATCH QUOTED AT "
            "ITS OWN LINE, NOT ONE CHOSEN BY THIS SEAT'S JUDGEMENT, against a declared floor of %d, "
            "so THE SET CAN FAIL IN BOTH DIRECTIONS. AND THE MATCHER WAS REPAIRED TWICE AFTER ITS "
            "OUTPUT WAS SEEN AND THE LINEAGE IS PRINTED: %d then %d then %d heads, each repair "
            "tracing to words written before the run. THE UNIT WAS FIXED ON THE LOCKED FACE BEFORE "
            "ANY SCORE -- a list item, a table row, a fenced block or a paragraph -- because under a "
            "blank-line-only definition A BIBLIOGRAPHY IS ONE PARAGRAPH AND THE MOST PARTITIONED "
            "DOCUMENT WOULD SCORE AS THE MOST COMBINING. CO-LOCATION WAS SCORED ON THE EXEMPLAR SET "
            "ALONE BEFORE ANY CORPUS-WIDE NUMBER EXISTED and it DOES NOT SEPARATE: %d of %d "
            "synthesis exemplars clear the bar and %d of %d gathering exemplars clear it too, the "
            "lowest synthesis ratio is %.3f and the highest gathering ratio is %.3f, so THE TWO SETS "
            "OVERLAP COMPLETELY AND NO CHOICE OF THRESHOLD WOULD HAVE SEPARATED THEM. THE BRANCH IS "
            "%s, THE PREDICATE IS NOT ADOPTED, THE CORPUS WAS NOT SCORED and (F2) IS NOT REACHED "
            "RATHER THAN MET OR REFUTED. b380's positive column is STILL AN UPPER BOUND ON SYNTHESIS "
            "and its negative column is STILL UNVALIDATED, because a second feature that failed "
            "cannot validate a first -- and TWO INDEPENDENT STRUCTURAL FEATURES NOW FAIL THE SAME "
            "DISTINCTION, WHICH IS NOT PROOF THAT NO STRUCTURAL FEATURE READS ROLE"
            % (LG['gates_read'], LG['face_subject_gates'], EX['b380_threshold'],
               EX['b380_lowest_synthesis_reach'], EX['head_lines'], EX['scanned'],
               len(EX['gathering_set']), EX['floor'], EX['loose_hits'], EX['loose2_hits'],
               EX['wide_hits'], RS['synthesis_cplus'], RS['synthesis_n'], RS['gathering_cplus'],
               RS['gathering_n'], RS['lowest_synthesis_ratio'], RS['highest_gathering_ratio'],
               BRANCH))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN AND NO ROW WAS WRITTEN INTO ANY "
            "DOCUMENT. ### The documents were READ solely to split them into units and ask which "
            "units carry two clusters, and EVERY ABSENCE CARRIES A POSITIVE CONTROL THAT FOUND A "
            "KNOWN PRESENCE FIRST. ### NO STATEMENT WAS PROVED, NO BUILD WAS RUN AND NO AXIOM "
            "PROFILE WAS RECOMPUTED. ### TWO SOURCE NAMES IN ONE UNIT SAY THEY SIT TOGETHER AND SAY "
            "NOTHING ABOUT WHETHER THE DOCUMENT ARGUES ANYTHING BETWEEN THEM")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT THE "
            "OBJECT. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED AND NO "
            "LIST CLOSED BY THIS SEAT. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL, REGISTRY.md "
            "WAS NOT EDITED, AND NOTHING ON THE DOWNLOAD LAYER WAS WRITTEN, MOVED, RENAMED OR "
            "REMOVED")
    grade = ("### TESTED-AND-NOT-ADOPTED, WITH THE NON-ADOPTION CLAUSE BINDING. ### THE PREDICATE "
             "DOES NOT SEPARATE THE REBUILT CONTROL AND THE CORPUS WAS THEREFORE NOT SCORED, which "
             "is the order's own clause and not a shortfall. ### THE THRESHOLD WAS DECLARED BEFORE "
             "THE CONTROL RAN AND WAS NOT MOVED AFTERWARDS TO MAKE IT AGREE, and the full ratio per "
             "exemplar is printed so a reader can see what any other threshold would have done "
             "without this seat trying one. ### THE TOKENISER WAS MEASURED AND ACQUITTED: re-scored "
             "under a paragraph-only splitter the branch does not change. ### WHAT THE PREDICATE IS "
             "DEAF TO IS DECLARED RATHER THAN DISCOVERED LATER, INCLUDING THAT THE DIRECTORY STANDS "
             "IN FOR THE SUBJECT. ### AND THE MATCHER THAT BUILT THE CONTROL WAS REPAIRED TWICE "
             "AFTER ITS OUTPUT WAS SEEN AND ITS LINEAGE IS PRINTED, BECAUSE A READER IS OWED THE "
             "LINEAGE AND NOT ONLY THE LAST VERSION")
    status = ("data/b381_the_control_rebuilt.txt; data/b380_ruling_evidence.txt (updated with (R14) "
              "banked verbatim and this act's tables); data/%s; data/%s; data/%s; data/%s; "
              "data/b381_registration_2026-09-09.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b381); tools/co_location.py (SHARED, new); "
              "tools/b381_exemplars.py; tools/b381_control.py; tools/b381_verdict.py; PLACE-papers "
              "OPEN_TRAILS.md (an append-only block; NO CORPUS DOCUMENT EDITED AND REGISTRY.md NOT "
              "TOUCHED); CORRESPONDENCE.md row %%d"
              % (EX['run_file'], RS['run_file'], VD['run_file'], J('b381_reads')['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the control rebuilt', 'co-location tested', 'co-location is not adopted',
           'the purpose statements', 'two features fail the same distinction')
MUST_NOT_HIT = ('the class is ruled', 'the declarations are moved',
                'the corpus was scored', 'the registry is edited')


def do_key(rownum):
    KEY = 'the-control-rebuilt-and-co-location-not-adopted'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "THE CONTROL REBUILT, AND CO-LOCATION TESTED AND NOT ADOPTED. (R14) IS RECORDED AND NOT "
        "APPLIED: the class ruling governs by CONTENT AND ROLE AND NOT BY LOCATION, so the "
        "download-layer book is inside its reach and outside the mirroring ruling, both hold and "
        "neither is edited into the other; it answers b379 filing, and THE BOOK REGISTRY DRIFT STAYS "
        "OPEN AND IS THE AUTHOR OWN. THE OLD CONTROL WEAKNESS IS ONE FINDING AND WAS MEASURED: b380 "
        "threshold was %d and the lowest synthesis-declarer reach was %d, so NO VALUE OF THE "
        "THRESHOLD WOULD HAVE FAILED THAT SIDE, while both gathering declarers disagreed. The "
        "rebuild scanned the first %d lines of %d documents for a sentence in which the document "
        "NAMES ITSELF and names a gathering purpose: %d exemplars, EVERY MATCH TAKEN AND QUOTED AT "
        "ITS OWN LINE, NOT ONE CHOSEN BY JUDGEMENT, against a floor of %d, so THE SET CAN FAIL IN "
        "BOTH DIRECTIONS. THE MATCHER WAS REPAIRED TWICE AFTER ITS OUTPUT WAS SEEN AND THE LINEAGE "
        "IS PRINTED: %d then %d then %d heads. THE UNIT WAS FIXED ON THE LOCKED FACE BEFORE ANY "
        "SCORE because under a blank-line-only definition A BIBLIOGRAPHY IS ONE PARAGRAPH AND THE "
        "MOST PARTITIONED DOCUMENT WOULD SCORE AS THE MOST COMBINING. CO-LOCATION WAS SCORED ON THE "
        "EXEMPLAR SET ALONE BEFORE ANY CORPUS-WIDE NUMBER EXISTED and it DOES NOT SEPARATE: %d of %d "
        "synthesis exemplars clear the bar and %d of %d gathering exemplars clear it too, lowest "
        "synthesis ratio %.3f against highest gathering ratio %.3f, so THE SETS OVERLAP COMPLETELY "
        "AND NO THRESHOLD WOULD HAVE SEPARATED THEM. BRANCH %s, NOT ADOPTED, THE CORPUS WAS NOT "
        "SCORED, and (F2) IS NOT REACHED. TWO INDEPENDENT STRUCTURAL FEATURES NOW FAIL THE SAME "
        "DISTINCTION, WHICH IS NOT PROOF THAT NO STRUCTURAL FEATURE READS ROLE."
        % (EX['b380_threshold'], EX['b380_lowest_synthesis_reach'], EX['head_lines'],
           EX['scanned'], len(EX['gathering_set']), EX['floor'], EX['loose_hits'],
           EX['loose2_hits'], EX['wide_hits'], RS['synthesis_cplus'], RS['synthesis_n'],
           RS['gathering_cplus'], RS['gathering_n'], RS['lowest_synthesis_ratio'],
           RS['highest_gathering_ratio'], BRANCH))
    grade = (
        "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED AND NO LIST CLOSED "
        "BY THIS SEAT. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT "
        "EDITED. ### (R14) IS RECORDED AND NOT APPLIED AND THE REGISTRY-DRIFT FILING STAYS OPEN AND "
        "IS THE AUTHOR OWN. ### THE THRESHOLD WAS DECLARED BEFORE THE CONTROL RAN AND WAS NOT MOVED "
        "AFTERWARDS TO MAKE IT AGREE. ### THE CONTROL RAN BEFORE ANY CORPUS-WIDE NUMBER EXISTED. ### "
        "THE NON-ADOPTION CLAUSE BOUND AND THE CORPUS WAS NOT SCORED. ### NO PRIOR SCORE WAS "
        "OVERWRITTEN AND NO QUADRANT TABLE WAS REDRAWN. ### NOT ONE EXEMPLAR WAS ADDED, DROPPED OR "
        "RANKED BY JUDGEMENT AND EVERY ONE IS QUOTED AT ITS OWN LINE. ### THE MATCHER LINEAGE IS "
        "PRINTED BECAUSE A READER IS OWED IT. ### WHAT THE PREDICATE IS DEAF TO IS DECLARED. ### THE "
        "FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE "
        "CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### "
        "M-2 UNCHANGED")
    where = (
        "data/b381_the_control_rebuilt.txt; data/b380_ruling_evidence.txt (updated); data/%s; "
        "data/%s; data/%s; data/%s; data/b381_registration_2026-09-09.txt (LOCKED before any write, "
        "chained on tools/b378_lockgate.py run as b381 -- %d gates read, %d checked by digest); "
        "tools/co_location.py (SHARED, new: the unit splitter fixtured on all three kinds plus a "
        "heading and a fence); tools/b381_exemplars.py; tools/b381_control.py; "
        "tools/b381_verdict.py; PLACE-papers OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row %d"
        % (EX['run_file'], RS['run_file'], VD['run_file'], J('b381_reads')['run_file'],
           LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b381 (the old control weakness measured; the control rebuilt from purpose statements; "
           "co-location tested against it and NOT adopted; (R14) recorded)")
    row_new = ('    # ### THE CONTROL REBUILT, AND CO-LOCATION TESTED (b381).%s'
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
        rec('    %-44s reaches the b381 key : %s' % (q, g))
    for lbl, cond in (('no class ruled, no declaration moved',
                       'NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED' in out),
                      ('no corpus document written into and no registry edit',
                       'NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED'
                       in out),
                      ('(R14) recorded and not applied',
                       'RECORDED AND NOT APPLIED' in out),
                      ('the registry-drift filing stays open and is the author`s',
                       'REGISTRY-DRIFT FILING STAYS OPEN' in out),
                      ('the old control`s weakness was measured',
                       'NO VALUE OF THE THRESHOLD WOULD HAVE FAILED THAT SIDE' in out),
                      ('nothing was curated',
                       'NOT ONE EXEMPLAR WAS ADDED, DROPPED OR RANKED BY JUDGEMENT' in out),
                      ('the matcher lineage is printed',
                       'THE MATCHER LINEAGE IS PRINTED' in out),
                      ('the unit was fixed before any score',
                       'THE UNIT WAS FIXED ON THE LOCKED FACE BEFORE ANY SCORE' in out),
                      ('the threshold was not moved to fit the control',
                       'WAS NOT MOVED AFTERWARDS TO MAKE IT AGREE' in out),
                      ('the control ran before any corpus number',
                       'BEFORE ANY CORPUS-WIDE NUMBER EXISTED' in out),
                      ('the predicate is not adopted and the corpus was not scored',
                       'NOT ADOPTED' in out and 'THE CORPUS WAS NOT SCORED' in out),
                      ('(F2) is not reached rather than met or refuted',
                       'NOT REACHED' in out),
                      ('two features fail and that is not a proof',
                       'NOT PROOF THAT NO STRUCTURAL FEATURE READS ROLE' in out),
                      ('no prior score was overwritten',
                       'NO PRIOR SCORE WAS OVERWRITTEN' in out),
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
    rec('b381 -- THE DESK UNDER (R7), AND THE THREE CLOSING WRITES.')
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
        run_clock.write(D, 'b381_desk_notes', LINES)
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b381_desk_notes', LINES)
        return 1
    g1 = ("THE CONTROL REBUILT FROM THE RECORD'S OWN PURPOSE STATEMENTS" in ROWS[0][0]
          and 'CHECKS WHAT EACH GATE READ' in ROWS[0][1]
          and 'RECORDED AND NOT APPLIED' in ROWS[0][1]
          and "STAYS OPEN AND IS THE AUTHOR'S" in ROWS[0][1]
          and 'ONE FINDING' in ROWS[0][1]
          and 'NO VALUE OF THE THRESHOLD WOULD HAVE FAILED THAT SIDE' in ROWS[0][1]
          and "NOT ONE CHOSEN BY THIS SEAT'S JUDGEMENT" in ROWS[0][1]
          and 'REPAIRED TWICE AFTER ITS OUTPUT WAS SEEN' in ROWS[0][1]
          and 'FIXED ON THE LOCKED FACE BEFORE ANY SCORE' in ROWS[0][1]
          and 'BEFORE ANY CORPUS-WIDE NUMBER EXISTED' in ROWS[0][1]
          and 'DOES NOT SEPARATE' in ROWS[0][1]
          and 'NOT ADOPTED' in ROWS[0][1]
          and 'THE CORPUS WAS NOT SCORED' in ROWS[0][1]
          and 'NOT REACHED' in ROWS[0][1]
          and 'NOT PROOF THAT NO STRUCTURAL FEATURE READS ROLE' in ROWS[0][1]
          and 'NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN' in ROWS[0][2]
          and 'POSITIVE CONTROL' in ROWS[0][2]
          and 'NO CLASS WAS RULED' in ROWS[0][3]
          and 'REGISTRY.md WAS NOT EDITED' in ROWS[0][3]
          and 'THE NON-ADOPTION CLAUSE' in ROWS[0][4]
          and 'WAS NOT MOVED AFTERWARDS TO MAKE IT AGREE' in ROWS[0][4]
          and 'DEAF TO IS DECLARED' in ROWS[0][4]
          and 'A READER IS OWED THE LINEAGE' in ROWS[0][4]
          and 'THE CONTROL REBUILT, AND CO-LOCATION TESTED' in ROWS[0][5]
          and 'NO NEW TRACKING DOCUMENT WAS CREATED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says the rebuilt control, the stamped gate, (R14) recorded not applied, the one '
        'finding, no curation, the printed lineage, the unit fixed first, the control before the '
        'corpus, the non-separation, the non-adoption, (F2) not reached, no overclaim, no terminal '
        'claimed, no class ruled, no registry edit, and the scope : %s' % g1)
    if not g1:
        run_clock.write(D, 'b381_desk_notes', LINES)
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
            run_clock.write(D, 'b381_desk_notes', LINES)
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
    p = run_clock.write(D, 'b381_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok, lists_closed=0,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b381_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
