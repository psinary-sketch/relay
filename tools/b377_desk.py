# -*- coding: utf-8 -*-
"""b377_desk.py -- THE DESK UNDER `(R7)`, AND THE THREE CLOSING WRITES: THE TRAIL BLOCK, THE ROW,
### THE KEY.

### ### **FOUR ROLES IN ONE FILE, AND THE REASON IS DECLARED RATHER THAN HIDDEN:** ### the locked
### registration caps this act's new tools at eight and the cap counts FILES.
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
MARK = '<!-- b377 the unblocked obligation; the pin was the missing element -->'
PRIOR = '<!-- b376 the two-axis read; every test crosses -->'
ACT = 'b377'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


BR, EV = J('b377_branch'), J('b377_evidence')
AX376, TS376 = J('b376_axes'), J('b376_tests')
CL375, IN375 = J('b375_clusters'), J('b375_integration')
A1 = [r for r in BR['six'] if r['arm'] == 1]
A2 = [r for r in BR['six'] if r['arm'] == 2]
ND = BR['not_determinable']
NOKEY = CL375['subject_clusters_without_keystone']
NROWS = sum(len(r['rows']) for r in A1)
NPINS = len(BR['pins'])

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
     'ROUTED to the author and not answered by a seat; this act creates no tracking document either'),

    # ---- THE FOUR OPEN LISTS, RESTATED OPEN BY NAME -------------------------------------------------
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND', None, None,
     'OPEN. ### **b373 executed (R9) backward and the chain closed for almost none of the set.** ### '
     'b377 executed (R9) FORWARD for the rows it wrote, which is a different half of the same rule '
     'and closes nothing on this list'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND', None, None,
     'OPEN. ### **b373 listed them with their carriers and ROUTED them, with three choices named and '
     'none chosen.** ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', None, None,
     'OPEN. ### **b374 listed every figure stated without a ref in its own sentence.** ### This act '
     'dates none of them'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND', None, None,
     'OPEN. ### **b374 found entries the register carries that appear nowhere else under their own '
     'key.** ### This act rewrites none of them'),

    # ---- CARRIED FROM b375/b376 ---------------------------------------------------------------------
    ('the word KEYSTONE naming three different tests', 'STAND', None, None,
     'CARRIED. ### **b376 SHARPENED IT: every one of the three CROSSES the two axes, so they disagree '
     'because each asks two questions at once.** ### Which governs is A RULING AND NOT A READ'),
    ('the documents that carry the apparatus and say nothing about their role', 'STAND', None, None,
     'CARRIED from b376 and ### **NOW WITH EVIDENCE THE AUTHOR SUPPLIED:** ### the role clause banked '
     'at this act speaks to exactly the property those documents are silent on'),
    ('the documents that do not say what they are', 'STAND', None, None,
     'CARRIED from b376: %d of %d score `A?`. ### **REPORTED, NOT CONFERRED**'
     % (AX376['axis_a_tally'].get('A?', 0), len(AX376['scored']))),

    # ---- WHAT THIS ACT ADDS -------------------------------------------------------------------------
    ("the author's role clause, banked as evidence", 'STAND', None, None,
     'NEW at b377: the author states what keystones are FOR -- clarifying results, exploring '
     'ramifications and insights, covering any and all pertinent or interesting materials, and NOT '
     'tunnel vision in explanatory clarity driven by the current lane. ### **IT SPEAKS TO THE ROLE '
     'AXIS AND NOT THE APPARATUS AXIS**, it is set beside each of the five options with a bearing '
     'line, and ### **THIS ACT RULES NOTHING FROM IT**'),
    ('the pin was the missing element, not the terminal', 'STAND', None, None,
     'NEW at b377 and it ### **REVISES HOW b376`S `B-` SHOULD BE READ:** ### of the six documents '
     'declaring TIER K with no traversable row, several already carry a Correspondence table with '
     'claims, terminals and profiles. ### **WHAT THEY LACK IS THE PIN**, which is one of the three '
     'things the taxonomy obliges -- grade . terminal . pin'),
    ('the six, split by the branch the order fixed', 'STAND', None, None,
     'NEW at b377: ### **%d TOOK ARM 1 (a pinned addendum APPENDED, %d rows, %d kernels read) AND %d '
     'TOOK ARM 2 (ROUTED, nothing repaired).** ### The branch was applied and not chosen, and the '
     'evidence deciding each is printed per document' % (len(A1), NROWS, NPINS, len(A2))),
    ('the terminals a document names that no kernel declares', 'STAND', None, None,
     'NEW at b377 and it is ### **THE FINDING ARM 2 EXISTS TO PRODUCE:** ### documents in this set '
     'name identifiers that are not declared in any of the 43 kernels on disk. ### **THAT IS A '
     'FINDING ABOUT THOSE DOCUMENTS AND NOT ABOUT THE TIER**, and none of them was repaired, '
     'demoted or disputed'),
    ('the two that are NOT DETERMINABLE, reported and left', 'STAND', None, None,
     'NEW at b377 under the amendment: ### **NOT DETERMINABLE IS NOT ABSENT.** ### Each is reported. '
     'What would settle it is a hand read of the prose that names '
     'terminals, not a table scan. ### **NEITHER IS REPAIRED, ROUTED AS LACKING, OR COUNTED AMONG '
     'THE SIX**'),
    ("the census's definition-versus-operation drift", 'STAND', None, None,
     'FILED at b377 against THE_KEYSTONE_CENSUS: three clauses stated, two applied through proxies, '
     'one not applied at all, a size floor added the definition never mentions, and ### **THREE '
     'DIFFERENT NUMBERS OUT OF ONE DOCUMENT.** ### FILED, NOT OPENED, NOT REPAIRED -- repairing it '
     'belongs to the ruling'),
    ('the subject clusters with registry rows and no keystone', 'STAND', None, None,
     'FILED at b377 as a work-order and ### **NOT OPENED:** ### %d clusters. ### Restated beside the '
     'role clause, this is the synthesis layer`s most visible incompleteness, and ### **MOST OF IT '
     'SITS OUTSIDE THE CURRENT LANE**, which is the risk the clause names. ### Priced for one unit '
     'and ### **NOT PRICED FOR THE WHOLE**, because no act in this record has written a keystone that '
     'did not exist' % len(NOKEY)),
    ('column (d) is a FLOOR, and the wider question is named', 'STAND', None, None,
     'NEW at b377 under the amendment: the banked figure %d of %d was taken against the findings '
     'layer alone. ### **IT IS A LOWER BOUND ON THE WIDER QUESTION** -- what bears on a keystone`s '
     'subject anywhere in the corpus, including other clusters, other kernels, the emerging-'
     'programmes ledger and the faces ledger. ### **NAMED, AND DELIBERATELY NOT RE-MEASURED HERE**'
     % (IN375['d_nonempty'], IN375['keystones'])),
    ('the class ruling itself', 'STAND', None, None,
     'STILL THE AUTHOR`S. ### b376 assembled five options with what each would oblige; b377 adds the '
     'role clause as evidence and a bearing line per option. ### **NO OPTION IS RECOMMENDED AND NO '
     'CLASS IS RULED**'),
    ("the lock gate's remaining hole", 'STAND', None, None,
     'CARRIED from b376 and ### **HIT IN PRACTICE AT b377:** ### the gate proves each record carries '
     'its pass phrase, not that the gate was run against the current bytes. ### This act re-ran every '
     'gate after its face reached final bytes ### **BY THE SEAT`S DISCIPLINE AND NOT BY THE TOOL`S**, '
     'and the next ferry is drafted to close it in the tool'),
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
    a1names = ', '.join('`%s`' % os.path.basename(r['file'])[:-3] for r in A1) or 'none'
    a2names = ', '.join('`%s`' % os.path.basename(r['file'])[:-3] for r in A2) or 'none'
    ndnames = ', '.join('`%s`' % os.path.basename(r['file'])[:-3] for r in ND) or 'none'
    return [
        '', MARK, '',
        '### **b377 — THE UNBLOCKED OBLIGATION, AND THE RULING’S EVIDENCE ASSEMBLED (2026-09-08)**',
        '',
        ('*No block above is edited. The b376 block (`%s`) and every block before it stand exactly as '
         'they were written.*' % PRIOR),
        '',
        ('**This act repairs where an obligation the taxonomy already states can be met, routes where '
         'it cannot, and assembles evidence for a ruling it does not make** — no class ruled, no '
         'document reclassified, no declaration moved, no list closed. **THE FOUR OPEN LISTS BELOW '
         'STAY OPEN BY NAME.**'),
        '',
        ('**THE AUTHOR’S ROLE CLAUSE IS BANKED AS EVIDENCE.** In the author’s own words, 2026-09-08: '
         '*“Keystones are for clarifying results and as well as for exploring ramifications and '
         'insights”*, and *“the keystones should cover any and all pertinent or interesting '
         'materials, not just having tunnel vision in explanatory clarity just because we have been '
         'relentlessly focused on a particular problem at a particular research phase.”* **WHAT IT '
         'BEARS ON IS STATED AND NOT INFERRED:** every content word in it is about what a keystone is '
         '*for* — clarifying, exploring, covering — and **not one word of it is about whether a '
         'document carries a correspondence table.** It speaks to the role axis; it widens that axis '
         'beyond b375’s *synthesis against other available content*; and **a clause that bears on one '
         'axis does not rule a question that spans two.** It is set beside each of b376’s five '
         'options with one line saying whether and how it bears, and **none of those lines '
         'recommends.**'),
        '',
        ('**THE PIN WAS THE MISSING ELEMENT, NOT THE TERMINAL — AND THAT REVISES HOW b376’S `B-` '
         'SHOULD BE READ.** b376 scored six Tier-K-declaring documents as carrying no traversable '
         'row. Read one at a time, several of them already carry a Correspondence table with claims, '
         'terminals and axiom profiles; **what they lack is the pin**, which is one of the three '
         'things the taxonomy obliges — *grade · terminal · pin*. b376’s predicate demanded all four '
         'of kernel, terminal, pin and grade **in one row** and could not see a table whose terminals '
         'are bare rather than dotted. **THE DEFECT THERE WAS PARTLY THE PREDICATE’S AND THIS ACT '
         'SAYS SO**, which is what its locked face said it would do if this happened.'),
        '',
        ('**THE BRANCH THE ORDER FIXED, APPLIED AND NOT CHOSEN: %d TOOK ARM 1 AND %d TOOK ARM 2.** '
         'Arm 1 — %s — names terminals that were **located in a kernel repository on disk, checked '
         'there, and found to resolve to exactly one kernel**; each received an **appended** '
         'Correspondence addendum carrying kernel · terminal · axiom profile · grade · **pin**, where '
         'the pin is this act’s own reading of that kernel’s head (`(R9)`’s forward half) and is '
         'never copied from another document or another row. %d rows across %d kernels. Arm 2 — %s — '
         'name identifiers that **no kernel on disk declares**, or that resolve ambiguously to more '
         'than one; **they are ROUTED with what is missing stated by name and nothing is repaired.** '
         '**ONE UNRESOLVED TERMINAL SENDS THE WHOLE DOCUMENT TO ARM 2**, because a table right in '
         'four rows and wrong in one is a table a stranger cannot trust — and **a row this act wrote '
         'that a stranger could not traverse would be worse than the absence it replaced.**'
         % (len(A1), len(A2), a1names, NROWS, NPINS, a2names)),
        '',
        ('**AND NOT DETERMINABLE IS NOT ABSENT.** %s declare Tier K and scored `NOT DETERMINABLE` on '
         'the apparatus axis. They are **reported and left** — not repaired, not routed as lacking, '
         'and **not counted among the six.** What the read could not decide: whether they carry the '
         'apparatus, because they name their terminals in prose or under a concordance and a table '
         'scan is the wrong instrument for that architecture — which is the corpus’s own point when '
         'it made `CONCORDANCE-CARRIED` a class of its own. What would decide it: a hand read of the '
         'naming sentences, one claim at a time, checking each named terminal at its kernel.'
         % ndnames),
        '',
        ('**TWO FILINGS, NEITHER OPENED.** *(i)* `THE_KEYSTONE_CENSUS.md` states a three-clause '
         'definition and applies two of them through proxies, **does not apply the third at all, and '
         'adds a `6 KB` size floor its definition never mentions** — and **three different numbers '
         'come out of one document** (its detector returned 20; it publishes 16 after a hand '
         'correction from its own SUPPORT row; re-applied at the head its own operation returns 29). '
         'The document is honest about the hand correction in its own text; **the drift still governs '
         'every number it printed.** Filed, not repaired: repairing it belongs to the ruling. *(ii)* '
         '**%d subject clusters have registry rows and no keystone.** Restated beside the role '
         'clause, that is the synthesis layer’s most visible incompleteness, and most of it sits '
         'outside the current lane — which is precisely the risk the clause names. **Filed as a '
         'work-order and NOT OPENED**, priced for one unit and **not priced for the whole**, because '
         'no act in this record has yet written a keystone that did not already exist, and a price '
         'from no measurement is an estimate wearing a measurement’s clothes.' % len(NOKEY)),
        '',
        ('**AND ONE BANKED FIGURE IS RESTATED AS A FLOOR.** b375 measured what bears on a keystone '
         'and is not in it — non-empty for **%d of %d** — **against the findings layer alone**, which '
         'is weighted toward the current lane. Under the role clause the reconciling question is '
         'wider: what bears on a keystone’s *subject* anywhere in the corpus, including other '
         'clusters, other kernels, the emerging-programmes ledger and the faces ledger. **THE BANKED '
         'FIGURE IS THEREFORE A LOWER BOUND AND NOT AN ANSWER**, the wider question is named as the '
         'one the reconciliation must ask, and **this act does not re-measure it.**'
         % (IN375['d_nonempty'], IN375['keystones'])),
        '',
        ('**WHAT THIS ACT DID NOT DO.** No class was ruled — the five options stand as b376 wrote '
         'them, now with a bearing line each and still no recommendation. No document was '
         'reclassified and **no declaration was moved, demoted or annotated as wrong: a document says '
         'what it says.** No existing byte was changed in any document written into — every write is '
         'an append and the committed blob remains a true prefix. No `.lean` file touched, no build '
         'run, no axiom profile recomputed: profiles in the appended rows are reproduced as the '
         'document states them. **The four open lists are restated OPEN by name and none is closed.** '
         'No new tracking document was created. h2 stands exactly where the deposit left it and this '
         'act makes no claim about it in either direction.'),
        '',
    ]


SCOPE = (
    "**SCOPE: ONE REPAIR-OR-ROUTE UNDER AN OBLIGATION THE TAXONOMY ALREADY STATES, PLUS ASSEMBLY OF "
    "EVIDENCE FOR THE AUTHOR'S RULING.** NO class ruled, NO document reclassified, NO declaration "
    "moved, NO list closed — the order's own list, and each is a bar. **A DOCUMENT SAYS WHAT IT "
    "SAYS**: every document here declares TIER K in its own words and this act disputes, moves and "
    "demotes none of them. **EVERY WRITE INTO A DOCUMENT IS AN APPEND** and the committed blob "
    "remains a TRUE PREFIX; no existing byte changed. **NO TERMINAL WAS WRITTEN INTO A ROW WITHOUT "
    "BEING LOCATED IN A KERNEL ON DISK, CHECKED THERE, AND FOUND TO RESOLVE TO EXACTLY ONE KERNEL**; "
    "one unresolved terminal sent the whole document to ARM 2. **EVERY PIN IS THIS ACT'S OWN READING "
    "OF THAT KERNEL'S HEAD** ((R9)'s forward half), never copied from a document or a row. **NOT "
    "DETERMINABLE IS NOT ABSENT**: the not-determinable documents are reported and left, not "
    "repaired, not routed as lacking, not counted among the six. **NO OPTION CARRIES A PREFERENCE "
    "WORD** and the ruling remains the author's. **BOTH FILINGS ARE FILED AND NEITHER IS OPENED**; "
    "the census is quoted, not repaired. **THE COLUMN-(d) FIGURE IS A FLOOR** and the wider question "
    "is named and NOT re-measured. **NO LIST WAS CLOSED** — the four open lists are restated OPEN by "
    "name. **NO NEW TRACKING DOCUMENT WAS CREATED.** NO .lean FILE TOUCHED, NO BUILD RUN, NO AXIOM "
    "PROFILE RECOMPUTED — profiles are reproduced as the documents state them. NOTHING IS CLAIMED "
    "ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing "
    "about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT "
    "MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 "
    "REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. "
    "The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE "
    "INSTRUMENT LANE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit "
    "left it and this act makes no claim about it in either direction. The wave PARKED by the "
    "author's ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def corr_rows(Q):
    m = ("**THE PIN WAS THE MISSING ELEMENT, NOT THE TERMINAL: %d OF THE SIX TIER-K DOCUMENTS WITH NO "
         "TRAVERSABLE ROW TOOK THE APPEND ARM AND %d TOOK THE ROUTE ARM, UNDER A BRANCH THE ORDER "
         "FIXED AND THIS ACT APPLIED** (b377, the unblocked obligation)" % (len(A1), len(A2)))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A GATE THAT READS EVERY "
            "PRE-LOCK GATE** -- b376's lock gate run as b377, 7 of 7 read and passing, inherited "
            "rather than rebuilt. THE AUTHOR'S ROLE CLAUSE IS BANKED VERBATIM AS EVIDENCE AND NOT AS "
            "A RULING -- keystones are for clarifying results and exploring ramifications and "
            "insights, and should cover any and all pertinent or interesting materials rather than "
            "tunnel vision in explanatory clarity driven by a particular problem at a particular "
            "research phase -- and IT SPEAKS TO THE ROLE AXIS AND NOT THE APPARATUS AXIS, so it is "
            "set beside each of b376's five options with one bearing line and NO RECOMMENDATION. "
            "READ ONE AT A TIME, SEVERAL OF THE SIX ALREADY CARRY A CORRESPONDENCE TABLE WITH CLAIMS, "
            "TERMINALS AND AXIOM PROFILES AND WHAT THEY LACK IS THE PIN, which is one of the three "
            "things the taxonomy obliges; b376's predicate demanded all four in one row and could not "
            "see a table whose terminals are bare rather than dotted, SO THE DEFECT THERE WAS PARTLY "
            "THE PREDICATE'S AND THIS ACT SAYS SO. %d rows were appended across %d kernels, EVERY "
            "TERMINAL LOCATED IN A KERNEL ON DISK, CHECKED THERE AND FOUND TO RESOLVE TO EXACTLY ONE "
            "KERNEL, AND EVERY PIN THIS ACT'S OWN READING OF THAT KERNEL'S HEAD. ONE UNRESOLVED "
            "TERMINAL SENT THE WHOLE DOCUMENT TO ARM 2 because a table right in four rows and wrong "
            "in one is a table a stranger cannot trust. AND NOT DETERMINABLE IS NOT ABSENT. THE TWO "
            "DOCUMENTS THE TABLE SCAN LEFT UNDECIDED ARE REPORTED AND LEFT. Each states what the read "
            "did not settle and what would settle it. TWO FILINGS, NEITHER OPENED: the census states three "
            "clauses and applies two through proxies, DOES NOT APPLY THE THIRD AT ALL AND ADDS A SIZE "
            "FLOOR ITS DEFINITION NEVER MENTIONS, with three different numbers out of one document; "
            "and %d subject clusters have registry rows and no keystone, restated beside the role "
            "clause as the synthesis layer's most visible incompleteness. AND THE BANKED COLUMN-(d) "
            "FIGURE %d OF %d IS RESTATED AS A FLOOR against a wider question this act NAMES AND DOES "
            "NOT RE-MEASURE"
            % (NROWS, NPINS, len(NOKEY), IN375['d_nonempty'], IN375['keystones']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN. ### THE KERNELS WERE OPENED -- which "
            "b376 did not do -- SOLELY TO LOCATE AND CHECK TERMINALS THE DOCUMENTS THEMSELVES NAME, "
            "and every one written into a row was found declared in EXACTLY ONE kernel repository at "
            "that repository's committed head. ### NO STATEMENT WAS PROVED, NO BUILD WAS RUN AND NO "
            "AXIOM PROFILE WAS RECOMPUTED: profiles in the appended rows are reproduced AS THE "
            "DOCUMENT STATES THEM. ### LOCATING A TERMINAL SAYS IT EXISTS AT THAT NAME AT THAT PIN "
            "AND SAYS NOTHING ABOUT WHETHER THE DOCUMENT'S SENTENCE ABOUT IT IS RIGHT")
    prof = ("### NO AXIOM PROFILE COMPUTED. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED "
            "ABOUT THE OBJECT -- no frame, no seed, no transform, no quadrature, no fit, no score, no "
            "series. ### NO CLASS WAS RULED, NO DOCUMENT WAS RECLASSIFIED, NO DECLARATION WAS MOVED "
            "AND NO LIST WAS CLOSED -- the order's four prohibitions, each measured by its own "
            "must-fail fixture. ### EVERY WRITE INTO A DOCUMENT IS AN APPEND AND THE COMMITTED BLOB "
            "REMAINS A TRUE PREFIX")
    grade = ("### REPAIRED-WHERE-THE-OBLIGATION-COULD-BE-MET, ROUTED WHERE IT COULD NOT. ### The "
             "obligation is the STANDING TAXONOMY'S OWN, quoted verbatim: every such claim states its "
             "grade . terminal . pin. ### THE BRANCH WAS FIXED BY THE ORDER BEFORE ANY DOCUMENT WAS "
             "READ AND THIS ACT APPLIED IT RATHER THAN CHOOSING PER DOCUMENT, and the evidence "
             "deciding each arm is printed per document so a reader can check the branch rather than "
             "trust it. ### A NAME DECLARED IN TWO KERNELS IS NOT A TERMINAL THIS ACT CAN WRITE INTO "
             "A ROW: choosing the first would be the act inventing a correspondence the document did "
             "not state. ### NO OPTION IN THE EVIDENCE CARRIES A PREFERENCE WORD AND THE RULING "
             "REMAINS THE AUTHOR'S")
    status = ("data/b377_the_unblocked_obligation.txt; data/%s; data/%s; data/%s; data/%s; "
              "data/b377_registration_2026-09-08.txt (LOCKED before any write, chained on "
              "tools/b376_lockgate.py RUN AS b377 which read all 7 pre-lock gates); "
              "tools/b377_branch.py; tools/b377_evidence.py; tools/b377_extract.py; "
              "PLACE-papers OPEN_TRAILS.md (an append-only block) and the ARM-1 documents "
              "(an APPENDED Correspondence addendum each; NO EXISTING BYTE CHANGED); "
              "CORRESPONDENCE.md row %%d"
              % (BR['run_file'], EV['run_file'],
                 J('b377_reads')['run_file'], J('b377_lockgate')['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the unblocked obligation', 'the pin was the missing element',
           'the branch applied', 'the role clause', 'the six documents')
MUST_NOT_HIT = ('the class is ruled', 'the declarations are moved',
                'the lists are closed', 'the census is repaired')


def do_key(rownum):
    key_new = (
        "    'the-pin-was-missing': ['the unblocked obligation', 'the pin was the missing element',\n"
        "                           'the branch applied', 'the role clause', 'the six documents'],\n")
    row_new = (
        '    # ### THE UNBLOCKED OBLIGATION (b377).\n'
        '    ("the-pin-was-missing", "b377 (one repair-or-route under an obligation the taxonomy '
        'already states, plus evidence for a ruling it does NOT make)",\n'
        '     "THE PIN WAS THE MISSING ELEMENT, NOT THE TERMINAL. Of the six documents declaring TIER '
        'K and scoring no traversable row at b376, several ALREADY CARRY a Correspondence table "\n'
        '     " with claims, terminals and axiom profiles; what they lack is THE PIN, one of the '
        'three things the taxonomy obliges (grade . terminal . pin). b376 predicate demanded all "\n'
        '     " four in one row and could not see a table whose terminals are bare rather than '
        'dotted, SO THAT DEFECT WAS PARTLY THE PREDICATE OWN AND THIS ACT SAYS SO. Under a branch "\n'
        '     " the order fixed before any document was read, ' + str(len(A1)) + ' took ARM 1 (a '
        'pinned addendum APPENDED, ' + str(NROWS) + ' rows, ' + str(NPINS) + ' kernels) and '
        + str(len(A2)) + ' took ARM 2 (ROUTED, nothing repaired). "\n'
        '     " The author role clause is banked verbatim as EVIDENCE: keystones are for clarifying '
        'results and exploring ramifications and insights, and should cover any and all pertinent "\n'
        '     " or interesting materials rather than tunnel vision in explanatory clarity driven by a '
        'particular problem at a particular research phase. IT SPEAKS TO THE ROLE AXIS AND NOT "\n'
        '     " THE APPARATUS AXIS. Two filings, neither opened: the census definition-versus-'
        'operation drift, and ' + str(len(NOKEY)) + ' subject clusters with registry rows and no "\n'
        '     " keystone. And the banked column-(d) figure ' + str(IN375['d_nonempty']) + ' of '
        + str(IN375['keystones']) + ' is restated as a FLOOR against a wider question this act names '
        'and does not re-measure.",\n'
        '     "### NO CLASS WAS RULED, NO DOCUMENT WAS RECLASSIFIED, NO DECLARATION WAS MOVED AND NO '
        'LIST WAS CLOSED. ### A DOCUMENT SAYS WHAT IT SAYS. ### EVERY WRITE INTO A DOCUMENT IS AN"\n'
        '     " APPEND and the committed blob remains a TRUE PREFIX. ### NO TERMINAL WAS WRITTEN '
        'WITHOUT BEING LOCATED IN A KERNEL ON DISK, CHECKED THERE AND FOUND TO RESOLVE TO EXACTLY"\n'
        '     " ONE KERNEL; ONE UNRESOLVED TERMINAL SENT THE WHOLE DOCUMENT TO ARM 2. ### EVERY PIN '
        'IS THIS ACT OWN READING OF THAT KERNEL HEAD, never copied from a document or a row."\n'
        '     " ### NOT DETERMINABLE IS NOT ABSENT. ### THE TWO THE SCAN LEFT UNDECIDED ARE REPORTED '
        'AND LEFT, not repaired, not routed as lacking, not counted among the six. ### NO OPTION"\n'
        '     " CARRIES A PREFERENCE WORD AND THE RULING REMAINS THE AUTHOR. ### BOTH FILINGS ARE '
        'FILED AND NEITHER IS OPENED; the census is QUOTED, NOT REPAIRED. ### THE FOUR OPEN LISTS"\n'
        '     " ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED. ### NO LEAN FILE '
        'TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED. ### NOTHING COMPUTED ABOUT THE"\n'
        '     " OBJECT. ### NO COORDINATE IS CLOSED. ### M-2 UNCHANGED",\n'
        '     "data/b377_the_unblocked_obligation.txt; data/' + BR['run_file'] + '; data/'
        + EV['run_file'] + '; data/' + J('b377_reads')['run_file'] + ';"\n'
        '     " data/b377_registration_2026-09-08.txt (LOCKED before any write, CHAINED ON b376 LOCK '
        'GATE RUN AS b377 -- 7 of 7 pre-lock gates read and passing, INHERITED NOT REBUILT);"\n'
        '     " tools/b377_branch.py (the branch applied and not chosen; a name declared in two '
        'kernels is not a terminal it can write into a row); tools/b377_evidence.py (the role"\n'
        '     " clause, the five options quoted whole with a bearing line each, and the two filings); '
        'PLACE-papers OPEN_TRAILS.md (append-only) and the ARM-1 documents (an APPENDED"\n'
        '     " Correspondence addendum each, NO EXISTING BYTE CHANGED); CORRESPONDENCE.md row '
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
    if "'the-pin-was-missing'" not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if '"the-pin-was-missing"' not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    open(INDEX + '.tmp', 'wb').write(txt.encode('utf-8'))
    os.replace(INDEX + '.tmp', INDEX)
    ok = True
    out, rc = query('the-pin-was-missing')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : the-pin-was-missing returns %d row(s)  %s'
        % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'the-pin-was-missing' in o
        ok = ok and g
        rec('    %-44s reaches the b377 key : %s' % (q, g))
    for lbl, cond in (('no class ruled, no declaration moved',
                       'NO CLASS WAS RULED, NO DOCUMENT WAS RECLASSIFIED, NO DECLARATION WAS MOVED'
                       in out),
                      ('a document says what it says', 'A DOCUMENT SAYS WHAT IT SAYS' in out),
                      ('every write is an append', 'EVERY WRITE INTO A DOCUMENT IS AN' in out),
                      ('one unresolved terminal sends the document to arm 2',
                       'ONE UNRESOLVED TERMINAL SENT THE WHOLE DOCUMENT TO ARM 2' in out),
                      ('not determinable is not absent',
                       'NOT DETERMINABLE IS NOT ABSENT' in out),
                      ('no list was closed', 'NO LIST' in out and 'WAS CLOSED' in out),
                      ('the lists are restated open',
                       'RESTATED OPEN BY NAME' in out),
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
    rec('b377 -- THE DESK UNDER (R7), AND THE THREE CLOSING WRITES.')
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
        run_clock.write(D, 'b377_desk_notes', LINES)
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b377_desk_notes', LINES)
        return 1
    g1 = ('THE PIN WAS THE MISSING ELEMENT' in ROWS[0][0]
          and 'READS EVERY PRE-LOCK GATE' in ROWS[0][1]
          and 'ROLE AXIS AND NOT THE APPARATUS AXIS' in ROWS[0][1]
          and 'PARTLY THE PREDICATE' in ROWS[0][1]
          and 'NOT DETERMINABLE IS NOT ABSENT' in ROWS[0][1]
          and 'RESTATED AS A FLOOR' in ROWS[0][1]
          and 'NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN' in ROWS[0][2]
          and 'EXACTLY ONE kernel' in ROWS[0][2]
          and 'NO CLASS WAS RULED' in ROWS[0][3]
          and 'TRUE PREFIX' in ROWS[0][3]
          and 'APPLIED IT RATHER THAN CHOOSING' in ROWS[0][4]
          and 'NO OPTION IN THE EVIDENCE CARRIES A PREFERENCE WORD' in ROWS[0][4]
          and 'ONE REPAIR-OR-ROUTE' in ROWS[0][5]
          and 'NO LIST WAS CLOSED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says the pin was missing, the lock read every gate, the role axis, the predicate`s '
        'own share of the defect, not-determinable, the floor, no terminal claimed and exactly one '
        'kernel, no class ruled and a true prefix, the branch applied, no preference word, and the '
        'scope : %s' % g1)
    if not g1:
        run_clock.write(D, 'b377_desk_notes', LINES)
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
            run_clock.write(D, 'b377_desk_notes', LINES)
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
    p = run_clock.write(D, 'b377_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok, lists_closed=0,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b377_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
