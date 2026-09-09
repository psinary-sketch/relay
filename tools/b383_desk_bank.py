# -*- coding: utf-8 -*-
"""b383_desk_bank.py -- THE DESK UNDER `(R7)`, THE THREE CLOSING WRITES, AND THE BANK.

### ### **FIVE ROLES IN ONE FILE, AND THE REASON IS A CAP THIS ACT`S OWN FACE GOT WRONG.** ### The
### locked face caps this act at ### **SIX** ### new `relay` tool files, and the clause spec`s own
### description then named ### **SEVEN ROLES** ### -- regspec, extract, reg gate, account, desk
### sweeper, bank writer, gate suite -- against a demand of six.
### ### ### **THE CAP IS THE NUMBER AND THE DESCRIPTION WAS THE ERROR**, so the desk sweeper and the
### bank writer are one file and the act ships six. ### **THE FACE STANDS AND THE CONTRADICTION IS
### ### REPORTED**, which is what the face`s own opening sentence requires.
### ### **AND THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME.** ### The order says so and a bar
### measures it.
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
MARK = '<!-- b383 the standard read; the sequence reconciled -->'
PRIOR = '<!-- b379 the apparatus axis re-scored; two filings -->'
ACT = 'b383'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


AC = J('b383_components')
LG = J('b383_lockgate')
E = J('b383_reads')
CL375 = J('b375_clusters')
NOKEY = CL375['subject_clusters_without_keystone']
BANKOUT = os.path.join(D, 'b383_the_standard_read.txt')

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
     'OPEN. ### This act adds nothing to it and closes nothing'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND', None, None,
     'OPEN. ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', None, None,
     'OPEN. ### This act dates none of them'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND', None, None,
     'OPEN. ### This act rewrites none of them'),

    # ---- CARRIED ------------------------------------------------------------------------------------
    ('the class ruling itself', 'STAND', None, None,
     'STILL THE AUTHOR`S -- and ### **THE STANDING STANDARD ALREADY RULES IT.** ### b383 read it at '
     'content: four tiers, each obligation, each citation rule, author-ruled 2026-07-28'),
    ('the download-layer book`s registry drift', 'STAND', None, None,
     'OPEN AND ### **THE AUTHOR`S**, in `(R14)`s own words'),
    ('the subject clusters with registry rows and no keystone', 'STAND', None, None,
     '### **RESTATED AT b383 UNDER THE AUTHOR`S AMENDMENT: `%d` CLUSTERS ARE `NOT-YET-SYNTHESIZED`, '
     'NOT OWED AND NOT DEFICIENT.** ### A cluster may have SEVERAL keystones, ONE, or NONE YET; the '
     'relation is many-to-many and changes over time. ### **NO GRADE MOVED AND NO ACT '
     'RE-VERDICTED**' % len(NOKEY)),
    ("the census's definition-versus-operation drift", 'STAND', None, None,
     'FILED at b377 and ### **NOT REPAIRED**'),
    ('the 86 archive files the mirror does not carry', 'STAND', None, None,
     'CARRIED and ### **STILL UNCONFIRMED**'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', None, None,
     'CARRIED and ### **DELIBERATELY NOT RE-MEASURED**'),
    ('the ten untracked run records of earlier acts', 'STAND', None, None,
     'NAMED at b382 and ### **STILL UNTRACKED.** ### Not this act`s to commit either'),

    # ---- WHAT THIS LEG ADDS -------------------------------------------------------------------------
    ('the standing standard, read at content', 'STAND', None, None,
     'NEW at b383: the author-ruled document-class taxonomy, the registry`s phase attribute section '
     'and the keystone correspondence union, ### **ALL THREE QUOTED FROM THE CANONICAL DRIVE WITH '
     'EVERY LINE RE-READ AT ITS OWN LINE NUMBER** ### -- `%d` quotations failing to re-read'
     % len(AC['reread_failures'])),
    ('the sequence reconciled to it', 'CLOSE', 'b383_components_notes',
     'THE STANDARD HAD ALREADY RULED THE CLASS QUESTION, AND THE SEQUENCE SPENT',
     'CLOSED at b383: ### **`%d` OF THE `%d` ACTS DUPLICATED A RULED STANDARD AND `%d` ADD.** ### '
     'The occasion is gone because the reconciliation exists -- and ### **THE SEQUENCE VIOLATED THE '
     'FRESHNESS RULE THIS SEAT MINTED AT b368**: it ran on a belief with no date on it while the '
     'standard that dated it sat in the tree, author-ruled since 2026-07-28'
     % (AC['duplicated'], AC['acts_reconciled'], AC['adds'])),
    ('the navigator`s reading, tested against the standard`s own words', 'STAND', None, None,
     'NEW at b383: ### **VERDICT `%s`.** ### The two axes ARE the two tiers, in the standard`s own '
     'words. ### But the conjunction is ### **NOT MERELY UNNAMED -- IT IS EXCLUDED**: the citation '
     'rules contradict, the mixed document is disposed of by ruling ONE tier and reading the parts '
     'apart, and a predecessor scheme was RETIRED for spanning the two' % AC['verdict']),
    ('the author`s model, banked verbatim', 'STAND', None, None,
     'NEW at b383: `%d` lines, ### **`%d` DROPPED.** ### Banked as the author`s statement and '
     '### **NOT ADOPTED AS THIS SEAT`S FINDING**; no document measured against it and none ruled '
     'under it' % (AC['model_lines'], AC['model_dropped'])),
    ('the four amendments, drafted and routed', 'STAND', None, None,
     'NEW at b383: ### **`%d` DRAFTED, `%d` APPLIED, `%d` STANDARDS EDITED.** ### (i) the '
     'finished-keystone furniture obligation -- ### **A REAL AMENDMENT AND NOT A GLOSS**, because '
     'the standard`s load-bearing citation rule currently excludes the combination it asks for; '
     '(ii) the cluster unit as the author replaced it; (iii) the per-document tier sweep, priced; '
     '(iv) ### **ROUTED AS A REQUEST**' % (AC['amendments_drafted'], AC['amendments_applied'],
                                           AC['standards_edited'])),
    ('and the reviewer-reservoir rule could not be located', 'STAND', None, None,
     'NEW at b383 and ### **REPORTED, NOT RESOLVED.** ### A controlled sweep of the canonical tree, '
     'the relay tools and the TECHNE modules -- positive control firing on `%d` files, this act`s '
     'own files excluded -- found no such rule. ### **A SEAT CANNOT RESTATE A RULE IT CANNOT READ**'
     % AC['control_hits']),
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
        '### **b383 \u2014 THE STANDARD READ, THE SEQUENCE RECONCILED, THE MODEL BANKED '
        '(2026-09-09)**',
        '',
        ('*No block above is edited. The b382 block (`%s`) and every block before it stand exactly as '
         'they were written.*' % PRIOR),
        '',
        ('**THE CORPUS ALREADY CARRIED AN AUTHOR-RULED ANSWER TO THE CLASS QUESTION, AND THE SEQUENCE '
         'DID NOT CITE IT.** `THE_DOCUMENT_CLASS_TAXONOMY.md` \u2014 *standing standard, 2026-07-28, '
         'Tier E added 2026-08-08, author-ruled* \u2014 fixes four tiers, and for each one **what it '
         'must carry and how it may be cited**. Tier K is keystone-certified, its obligation *every '
         'such claim states its **grade \u00b7 terminal \u00b7 pin***, and it **may be cited as '
         'certification**. Tier C is cluster-synthesis, which **organizes** certified results '
         '*asserting relationships not individually certified*, and is **cited for orientation and '
         'organization \u2014 NEVER as certification**; the standard calls that *the taxonomy\u2019s '
         'load-bearing rule*. Tier N is reference-only; Tier E is filing-facing, **cites Tier K, and '
         'nothing cites Tier E**. The taxonomy exists **to make two failures structurally impossible: '
         'a synthesis being read as a certification, and a filing-facing framing being read as the '
         'record.** Read at the canonical drive; the mirror was not opened.'),
        '',
        ('**AND TWO MORE STANDING ANSWERS SAT BESIDE IT.** The registry\u2019s **PHASE ATTRIBUTE** '
         'section (added 2026-08-12) reconciles *the rubric\u2019s WHEN and the registry\u2019s '
         'WHERE*, which **now coexist permanently**: every row carries one of `1 \u00b7 1.1 \u00b7 '
         '1.2 \u00b7 1.5 \u00b7 2 \u00b7 SUPPORT`, and the attribute is the join between when the '
         'work happened and where the row lives. And `THE_LOAD_BEARING_MAP.md` \u2014 **the keystone '
         'correspondence union** \u2014 already names its own set: **14 graded Correspondence '
         'tables**, each named, assembled into one graph of terminal \u00b7 pin \u00b7 grade \u00b7 '
         'citing keystones.'),
        '',
        ('**SO THE SEQUENCE RECONCILES AS %d DUPLICATED AND %d ADDS, STATED WITHOUT DEFENCE.** '
         'b375 asked what the corpus means by *keystone* \u2014 **the standard had ruled it**. b377 '
         'asked whether documents lacked what the taxonomy requires \u2014 **the taxonomy states the '
         'obligation**. b379 re-measured the apparatus column \u2014 **the union already named the '
         'fourteen**. What the sequence ADDS is narrower than its banks suggest: b376\u2019s two-axis '
         '**separation**; b378\u2019s facts about kernels at refs; and b380, b381 and b382 \u2014 '
         '**two negative results about two predicates, and a conclusion the standard assumes but '
         'nowhere argues.**'
         % (AC['duplicated'], AC['adds'])),
        '',
        ('**AND THE SEQUENCE VIOLATED A FRESHNESS RULE THIS SEAT ITSELF MINTED AT b368.** '
         '`DESK_FRESHNESS.md`: *every desk item names the FILE and the DATE at which it was last '
         'confirmed; an item without one is RE-VERIFIED before it is ordered* \u2014 and *the cost '
         'was not a wrong belief, it was **a right belief with no date on it**, and a second act spent '
         'to re-derive what a first act had already banked*. The premise the sequence ran on carried '
         'no date. **The standard that dated it was author-ruled on 2026-07-28 and sat in the tree the '
         'whole time.**'),
        '',
        ('**THE NAVIGATOR\u2019S READING WAS TESTED AGAINST THE STANDARD\u2019S OWN WORDS AND IS '
         '%s.** Right in substance: the two axes **are** the two tiers \u2014 Tier K\u2019s '
         'obligation *is* the apparatus axis, Tier C\u2019s *organizes \u2026 relationships not '
         'individually certified* *is* the role axis. Wrong in one particular, and it matters: the '
         'conjunction is **not merely unnamed \u2014 it is excluded**. The two citation rules '
         'contradict (may be cited as certification / **NEVER** as certification), so no single '
         'document can carry both. The standard already disposes of the mixed document by **ruling '
         'one tier and reading the parts apart** \u2014 *CATALOGOS \u2026 **Read the panels as C, '
         'the pinned terminals as K***. And b186\u2019s predecessor scheme was **RETIRED** precisely '
         'because its class *spanned Tier K and Tier C at once \u2014 collapsing the very distinction '
         'the standing taxonomy exists to enforce*.'
         % AC['verdict']),
        '',
        ('**WHICH MAKES THE AUTHOR\u2019S FINISHED KEYSTONE A REAL AMENDMENT AND NOT A '
         'CLARIFICATION.** The model, banked verbatim as the author\u2019s statement of 2026-09-09 '
         '(%d lines, **%d dropped**): every document belongs to a subject cluster so its content is '
         'checked and synthesized into that cluster\u2019s keystone; **not every document need '
         'become a keystone**; a finished keystone **stands on its own covering all conclusions and '
         'insights from its cluster**; support papers **are the process and publish alongside the '
         'keystone**, as the deposited group upload did; and a keystone\u2019s **every statement is '
         'clear in body and documented to its kernel witness by a correspondence table accessible '
         'after the front matter**, with glossary, bibliography and other tables as needed. That asks '
         'one document to carry the Tier-C role **and** the Tier-K obligation \u2014 which the '
         'standing standard as written does not permit.'
         % (AC['model_lines'], AC['model_dropped'])),
        '',
        ('**FOUR AMENDMENTS ARE DRAFTED AND ROUTED; %d ARE APPLIED AND %d STANDARDS ARE EDITED.** '
         '*(i)* the finished-keystone furniture obligation, in the author\u2019s words \u2014 and it '
         'must also say **what a finished keystone is cited as**, which this seat does not choose. '
         '*(ii)* **THE CLUSTER UNIT**, as the author\u2019s own amendment replaced it: every document '
         'belongs to a subject cluster so its content is read into that cluster\u2019s synthesis '
         'rather than sitting isolated; **a cluster may have SEVERAL keystones, ONE, or NONE YET**; '
         'the relation is many-to-many and changes over time, because *clusters and the constellations '
         'of kernels that serve them are amorphous, and a keystone is a synthesis at a moment* \u2014 '
         'later research **may produce another keystone beside it rather than superseding it**. '
         '*(iii)* the per-document tier sweep, which **the standard itself names as its standing '
         'follow-on** and which has been unrun since July, priced below. *(iv)* the reviewer-reservoir '
         'rule \u2014 **routed as a request, because this act could not locate it**.'
         % (AC['amendments_applied'], AC['standards_edited'])),
        '',
        ('**THE %d SUBJECT CLUSTERS WITH NO KEYSTONE ARE RESTATED AS `NOT-YET-SYNTHESIZED`, NOT OWED '
         'AND NOT DEFICIENT** \u2014 and the author\u2019s rule is stated here beside the count, as '
         'the amendment requires, so **a plurality is never read as an anomaly and an absence is never '
         'read as a defect**. **No grade is moved and no act is re-verdicted** by the restatement. The '
         'author\u2019s reason, banked verbatim: *it is a laboratory \u2014 an ongoing research '
         'programme that hopes to continue synthesizing further research with and against these '
         'foundational results as they stand.*' % len(NOKEY)),
        '',
        ('**THE PER-DOCUMENT TIER SWEEP, PRICED FROM THE RECORD\u2019S OWN FIGURES AND NOT ORDERED.** '
         'The standard estimates *~200 records*; the census measured **%d documents**, of which **%d '
         'already carry a class line** and **%d carry none**. So the sweep is %d to confirm and %d to '
         'decide from scratch \u2014 and the two population figures are themselves something the '
         'sweep would reconcile, neither being wrong for its own date. **What the record cannot price '
         'is the per-document judgement**: most documents say nothing about their own role, so most '
         'tier calls cannot be made from the document\u2019s own text. **UNPRICED, and named unpriced '
         'rather than estimated.**'
         % (AC['declared_class_line'] + AC['not_declared_class_line'], AC['declared_class_line'],
            AC['not_declared_class_line'], AC['declared_class_line'],
            AC['not_declared_class_line'])),
        '',
        ('**AND THE REVIEWER-RESERVOIR RULE COULD NOT BE LOCATED.** A controlled sweep of the '
         'canonical tree, the relay tools and the TECHNE modules \u2014 **positive control firing on '
         '%d files**, this act\u2019s own files excluded \u2014 found no such rule under that name '
         'or the wordings tried. **A seat cannot restate a rule it cannot read**, and a seat that '
         'supplies the words itself has written a new rule under an old name. **(iv) is routed as a '
         'request for the rule\u2019s location or its text.**' % AC['control_hits']),
        '',
        ('**WHAT THIS ACT DID NOT DO.** **No standard edited** \u2014 the taxonomy, the registry and '
         'the union are byte-identical to their blobs. **No amendment applied.** No class ruled, no '
         'document reclassified, **no declaration moved**, no grade moved, **no act re-verdicted**, no '
         'list closed, **no corpus document written into at all**. Nothing on the download layer '
         'touched, no archive file touched and the 86 unconfirmed still unconfirmed. The mirror was '
         'not opened. No `.lean` file touched, no build run, no axiom profile recomputed. **The four '
         'open lists are restated OPEN by name.** h2 stands exactly where the deposit left it and this '
         'act makes no claim about it in either direction.'),
        '',
    ]


SCOPE = (
    "**SCOPE: THE STANDARD READ, THE SEQUENCE RECONCILED, THE MODEL BANKED.** NO class ruled, NO "
    "document reclassified, NO declaration moved, NO grade moved, NO act re-verdicted, NO list "
    "closed. **NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED** -- the taxonomy, the registry "
    "and the keystone correspondence union are BYTE-IDENTICAL TO THEIR BLOBS at the end of this "
    "act. **NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED.** **READ AT "
    "THE CANONICAL DRIVE, NEVER THE MIRROR**, and the mirror archive was not opened. **EVERY QUOTED "
    "LINE WAS RE-READ OUT OF ITS OWN FILE AT ITS OWN LINE NUMBER** and the count that failed is "
    "ZERO. **NO OBLIGATION AND NO CITATION RULE WAS PARAPHRASED.** **THE NAVIGATOR'S READING WAS "
    "TESTED AGAINST THE STANDARD'S OWN WORDS AND NOT ADOPTED ON HIS WORD**, and the line that "
    "decides the verdict is quoted. **THE RECONCILIATION IS WITHOUT DEFENCE**: a DUPLICATED verdict "
    "is not followed by a reason the duplication was reasonable. **THE AUTHOR'S MODEL IS BANKED "
    "VERBATIM AND NOT ADOPTED AS THIS SEAT'S FINDING** -- no document is measured against it and "
    "none is ruled under it. **THE AMENDMENTS ARE DRAFTED AND ROUTED; THE AUTHOR AMENDS.** **THE "
    "CLUSTER RULE IS STATED BESIDE EVERY CLUSTER-TO-KEYSTONE COUNT**, so a plurality is never read "
    "as an anomaly and an absence is never read as a defect, and the clusters without a keystone "
    "are NOT-YET-SYNTHESIZED rather than owed or deficient. **THE SWEEP IS PRICED AND NOT ORDERED, "
    "AND THE PART THE RECORD CANNOT PRICE IS NAMED UNPRICED.** **AMENDMENT (iv) IS ROUTED AS A "
    "REQUEST BECAUSE THE RULE COULD NOT BE LOCATED** -- a controlled sweep with a positive control "
    "that fired and with this act's own files excluded. **EVERY ABSENCE CARRIES A POSITIVE CONTROL "
    "THAT FINDS A KNOWN PRESENCE FIRST.** **NO OPTION IS RECOMMENDED, RANKED OR PREFERRED** and the "
    "ruling remains the author's. **NO ARCHIVE FILE WAS TOUCHED** and the 86 unconfirmed stay "
    "unconfirmed. **NO OWNER INSTRUMENT WAS EDITED.** **THE FOUR OPEN LISTS ARE RESTATED OPEN BY "
    "NAME.** **NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS.** NO .lean FILE TOUCHED, NO "
    "BUILD RUN, NO AXIOM PROFILE RECOMPUTED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED "
    "SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or "
    "the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE "
    "PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under "
    "b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the "
    "patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE "
    "WAVE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it "
    "and this act makes no claim about it in either direction. NOTHING IS DEPOSITED AND NOTHING WAS "
    "WRITTEN AT ZENODO.")


def corr_rows(Q):
    m = ("**THE STANDING STANDARD ALREADY RULED THE CLASS QUESTION, AND THE EIGHT-ACT SEQUENCE "
         "RECONCILES AS %d DUPLICATED AND %d ADDS** (b383, the standard read, the sequence "
         "reconciled, the model banked)" % (AC['duplicated'], AC['adds']))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b383, %d gates read and %d checked "
            "by digest, and THE AUTHOR'S AMENDMENT TO COMPONENT 4(ii) ARRIVED BEFORE THE LOCK so "
            "its own conditional did not fire and it governs the face as well as the routed text. "
            "THE THREE STANDING SOURCES WERE READ AT THE CANONICAL DRIVE AND NEVER THE MIRROR, and "
            "every quoted line was RE-READ AT ITS OWN LINE NUMBER with %d failing. "
            "THE_DOCUMENT_CLASS_TAXONOMY, author-ruled 2026-07-28, fixes FOUR TIERS and for each "
            "one WHAT IT MUST CARRY AND HOW IT MAY BE CITED: Tier K states grade-terminal-pin and "
            "MAY BE CITED AS CERTIFICATION; Tier C organizes certified results and is NEVER CITED "
            "AS CERTIFICATION, which the standard calls its load-bearing rule; Tier N is "
            "reference-only; Tier E cites Tier K and nothing cites Tier E. The registry's PHASE "
            "ATTRIBUTE section reconciles the rubric's WHEN with the registry's WHERE, which NOW "
            "COEXIST PERMANENTLY. And THE_LOAD_BEARING_MAP, the keystone correspondence union, "
            "ALREADY NAMES 14 GRADED CORRESPONDENCE TABLES. NONE OF THE THREE WAS CITED BY ANY OF "
            "THE EIGHT ACTS. THE NAVIGATOR'S READING IS %s: the two axes ARE the two tiers in the "
            "standard's own words, but the conjunction is NOT MERELY UNNAMED -- IT IS EXCLUDED, "
            "because the two citation rules contradict, because the standard disposes of the mixed "
            "document by RULING ONE TIER AND READING THE PARTS APART, and because a predecessor "
            "scheme was RETIRED for spanning the two. SO THE AUTHOR'S FINISHED KEYSTONE IS A REAL "
            "AMENDMENT AND NOT A CLARIFICATION. The model is banked verbatim, %d lines and %d "
            "dropped. FOUR AMENDMENTS ARE DRAFTED AND ROUTED, %d APPLIED AND %d STANDARDS EDITED. "
            "The %d clusters without a keystone are RESTATED AS NOT-YET-SYNTHESIZED, NOT OWED AND "
            "NOT DEFICIENT, with the author's many-to-many rule stated beside the count and NO "
            "GRADE MOVED AND NO ACT RE-VERDICTED. The per-document tier sweep, which the standard "
            "itself names as its standing follow-on and which has been unrun since July, is PRICED "
            "AND NOT ORDERED at %d documents to confirm and %d to decide from scratch, with the "
            "per-document judgement NAMED UNPRICED. And the reviewer-reservoir rule COULD NOT BE "
            "LOCATED by a controlled sweep whose positive control fired, so amendment (iv) IS "
            "ROUTED AS A REQUEST: A SEAT CANNOT RESTATE A RULE IT CANNOT READ. AND THE SEQUENCE "
            "VIOLATED THE FRESHNESS RULE THIS SEAT MINTED AT b368 -- it ran on a right belief with "
            "no date on it while the standard that dated it sat author-ruled in the tree"
            % (LG['gates_read'], LG['face_subject_gates'], len(AC['reread_failures']),
               AC['verdict'], AC['model_lines'], AC['model_dropped'],
               AC['amendments_applied'], AC['standards_edited'], len(NOKEY),
               AC['declared_class_line'], AC['not_declared_class_line']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN AND NO ROW WAS WRITTEN INTO ANY "
            "DOCUMENT. ### Three standing documents were READ AT CONTENT and quoted, each quotation "
            "re-read out of its own file at its own line number. ### NO STATEMENT WAS PROVED, NO "
            "BUILD WAS RUN AND NO AXIOM PROFILE WAS RECOMPUTED. ### QUOTING A STANDARD IS NOT "
            "AMENDING IT, AND DRAFTING AN AMENDMENT IS NOT APPLYING ONE")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT THE "
            "OBJECT. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED, NO "
            "GRADE MOVED, NO ACT RE-VERDICTED AND NO LIST CLOSED. ### NO CORPUS DOCUMENT WAS "
            "WRITTEN INTO AT ALL, NO STANDARD WAS EDITED, AND REGISTRY.md WAS NOT EDITED")
    grade = ("### RECONCILED-TO-THE-STANDING-STANDARD, AND THE RECONCILIATION IS WITHOUT DEFENCE. "
             "### A DUPLICATED VERDICT IS NOT FOLLOWED BY A REASON THE DUPLICATION WAS REASONABLE, "
             "because the order excluded a defence and a reconciliation that explains itself at "
             "every row IS one. ### THE NAVIGATOR'S READING WAS TESTED AGAINST THE STANDARD'S OWN "
             "WORDS AND NOT ADOPTED ON HIS WORD, and CORRECTED is a verdict the order listed. ### "
             "THE AUTHOR'S MODEL IS RECORDED AND NOT APPLIED. ### THE AMENDMENTS ARE TEXTS AND NOT "
             "EDITS; THE AUTHOR AMENDS. ### A SEAT CANNOT RESTATE A RULE IT CANNOT READ, so (iv) is "
             "a request. ### AND THE FRESHNESS RULE THE SEQUENCE VIOLATED WAS MINTED BY THIS SEAT "
             "ITSELF AT b368, WHICH IS REPORTED RATHER THAN SOFTENED")
    status = ("data/b383_the_standard_read.txt; data/%s; data/%s; "
              "data/b383_amendment_2026-09-09.txt (the author's amendment, banked verbatim, "
              "ARRIVED BEFORE THE LOCK); data/b383_registration_2026-09-09.txt (LOCKED before any "
              "write, chained on tools/b378_lockgate.py run as b383); tools/b383_extract.py; "
              "tools/b383_components.py; tools/b383_desk_bank.py; PLACE-papers OPEN_TRAILS.md (an "
              "append-only block; NO CORPUS DOCUMENT EDITED, NO STANDARD EDITED AND REGISTRY.md NOT "
              "TOUCHED); CORRESPONDENCE.md row %%d"
              % (AC['run_file'], E['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the standing standard read', 'the sequence reconciled', 'the four tiers',
           'the keystone correspondence union', 'the cluster unit')
MUST_NOT_HIT = ('the standard is edited', 'the amendment is applied',
                'a cluster is owed a keystone', 'the class is ruled')


def do_key(rownum):
    KEY = 'the-standing-standard-read-and-the-sequence-reconciled'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "THE STANDING STANDARD ALREADY RULED THE CLASS QUESTION. THE_DOCUMENT_CLASS_TAXONOMY, "
        "author-ruled 2026-07-28, fixes FOUR TIERS and for each one WHAT IT MUST CARRY AND HOW IT MAY "
        "BE CITED: Tier K states grade-terminal-pin and MAY BE CITED AS CERTIFICATION; Tier C "
        "organizes certified results and is NEVER CITED AS CERTIFICATION, the standard's own "
        "load-bearing rule; Tier N is reference-only; Tier E cites Tier K and nothing cites Tier E. "
        "The taxonomy exists to make two failures structurally impossible: a synthesis read as a "
        "certification, and a filing-facing framing read as the record. The registry's PHASE "
        "ATTRIBUTE section reconciles the rubric's WHEN with the registry's WHERE, now coexisting "
        "permanently. THE_LOAD_BEARING_MAP, the keystone correspondence union, ALREADY NAMES 14 "
        "GRADED CORRESPONDENCE TABLES. NONE OF THE THREE WAS CITED BY ANY OF THE EIGHT ACTS. THE "
        "SEQUENCE RECONCILES AS %d DUPLICATED AND %d ADDS, without defence: what it adds is b376's "
        "two-axis SEPARATION, b378's facts about kernels at refs, and TWO NEGATIVE RESULTS ABOUT TWO "
        "PREDICATES plus a conclusion the standard assumes but nowhere argues. AND THE SEQUENCE "
        "VIOLATED THE FRESHNESS RULE THIS SEAT MINTED AT b368: a right belief with no date on it, "
        "while the standard that dated it sat author-ruled in the tree. THE NAVIGATOR'S READING IS "
        "%s: the two axes ARE the two tiers, but the conjunction is NOT MERELY UNNAMED -- IT IS "
        "EXCLUDED, since the citation rules contradict, the mixed document is disposed of by RULING "
        "ONE TIER AND READING THE PARTS APART, and a predecessor scheme was RETIRED for spanning the "
        "two. SO THE AUTHOR'S FINISHED KEYSTONE IS A REAL AMENDMENT AND NOT A CLARIFICATION. The "
        "author's model is banked verbatim, %d lines and %d dropped. FOUR AMENDMENTS DRAFTED AND "
        "ROUTED, %d APPLIED, %d STANDARDS EDITED. The %d clusters without a keystone are RESTATED AS "
        "NOT-YET-SYNTHESIZED, NOT OWED AND NOT DEFICIENT, with the author's many-to-many rule stated "
        "beside the count. The per-document tier sweep is PRICED AND NOT ORDERED at %d to confirm and "
        "%d to decide from scratch, the judgement NAMED UNPRICED. And the reviewer-reservoir rule "
        "COULD NOT BE LOCATED, so (iv) IS ROUTED AS A REQUEST."
        % (AC['duplicated'], AC['adds'], AC['verdict'], AC['model_lines'], AC['model_dropped'],
           AC['amendments_applied'], AC['standards_edited'], len(NOKEY),
           AC['declared_class_line'], AC['not_declared_class_line']))
    grade = (
        "### NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED -- the taxonomy, the registry and "
        "the union are BYTE-IDENTICAL TO THEIR BLOBS. ### NO CLASS WAS RULED, NO DOCUMENT "
        "RECLASSIFIED, NO DECLARATION MOVED, NO GRADE MOVED, NO ACT RE-VERDICTED AND NO LIST CLOSED. "
        "### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED. ### READ AT "
        "THE CANONICAL DRIVE, NEVER THE MIRROR. ### EVERY QUOTED LINE RE-READ AT ITS OWN LINE NUMBER "
        "AND NO OBLIGATION OR CITATION RULE PARAPHRASED. ### THE READING WAS TESTED AGAINST THE "
        "STANDARD'S OWN WORDS AND NOT ADOPTED ON HIS WORD. ### THE RECONCILIATION IS WITHOUT "
        "DEFENCE. ### THE AUTHOR'S MODEL IS RECORDED AND NOT APPLIED. ### THE CLUSTER RULE IS STATED "
        "BESIDE THE COUNT SO A PLURALITY IS NOT AN ANOMALY AND AN ABSENCE IS NOT A DEFECT. ### THE "
        "SWEEP IS PRICED AND NOT ORDERED AND THE UNPRICED PART IS NAMED. ### A SEAT CANNOT RESTATE A "
        "RULE IT CANNOT READ. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING "
        "DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING "
        "COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED")
    where = (
        "data/b383_the_standard_read.txt; data/%s; data/%s; data/b383_amendment_2026-09-09.txt "
        "(banked verbatim, ARRIVED BEFORE THE LOCK); data/b383_registration_2026-09-09.txt (LOCKED "
        "before any write, chained on tools/b378_lockgate.py run as b383 -- %d gates read, %d "
        "checked by digest); tools/b383_extract.py; tools/b383_components.py; "
        "tools/b383_desk_bank.py; PLACE-papers OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row "
        "%d" % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b383 (the standing standard read at content; the eight-act sequence reconciled to it; "
           "the author's model banked; four amendments drafted and routed)")
    row_new = ('    # ### THE STANDARD READ, THE SEQUENCE RECONCILED (b383).%s'
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
        rec('    %-44s reaches the b383 key : %s' % (q, g))
    for lbl, cond in (('no standard edited and no amendment applied',
                       'NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED' in out),
                      ('no class ruled, no declaration moved',
                       'NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED' in out),
                      ('no grade moved and no act re-verdicted',
                       'NO GRADE MOVED, NO ACT RE-VERDICTED' in out),
                      ('no corpus document written into and no registry edit',
                       'NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED'
                       in out),
                      ('read at the canonical drive, never the mirror',
                       'READ AT THE CANONICAL DRIVE, NEVER THE MIRROR' in out),
                      ('every quoted line re-read at its own line number',
                       'RE-READ AT ITS OWN LINE NUMBER' in out),
                      ('nothing paraphrased',
                       'NO OBLIGATION OR CITATION RULE PARAPHRASED' in out),
                      ('the reading tested and not adopted on his word',
                       "NOT ADOPTED ON HIS WORD" in out),
                      ('the reconciliation is without defence',
                       'WITHOUT' in out and 'DEFENCE' in out),
                      ('the model recorded and not applied',
                       "THE AUTHOR'S MODEL IS RECORDED AND NOT APPLIED" in out),
                      ('the cluster rule stated beside the count',
                       'A PLURALITY IS NOT AN ANOMALY AND AN ABSENCE IS NOT A DEFECT' in out),
                      ('the clusters are not-yet-synthesized',
                       'NOT-YET-SYNTHESIZED, NOT OWED AND NOT DEFICIENT' in out),
                      ('the sweep priced and not ordered',
                       'PRICED AND NOT ORDERED' in out and 'NAMED UNPRICED' in out),
                      ('a seat cannot restate a rule it cannot read',
                       'A SEAT CANNOT RESTATE A RULE IT CANNOT READ' in out),
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
    rec('b383 -- THE DESK UNDER (R7), AND THE THREE CLOSING WRITES.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE DESK.')
    rec('-' * 100)
    Q = do_desk()
    # ### **THE DESK CLOSES NO LIST, AND THE FIGURE IS SET WHERE THE DESK ESTABLISHES IT**
    # ### rather than in the final update, because the bank below reads it.
    Q['lists_closed'] = 0

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
        run_clock.write(D, 'b383_desk_notes', LINES)
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b383_desk_notes', LINES)
        return 1
    g1 = ('THE STANDING STANDARD ALREADY RULED THE CLASS QUESTION' in ROWS[0][0]
          and 'CHECKS WHAT EACH GATE READ' in ROWS[0][1]
          and 'ARRIVED BEFORE THE LOCK' in ROWS[0][1]
          and 'CANONICAL DRIVE AND NEVER THE MIRROR' in ROWS[0][1]
          and 'RE-READ AT ITS OWN LINE NUMBER' in ROWS[0][1]
          and 'FOUR TIERS' in ROWS[0][1]
          and 'NEVER CITED AS CERTIFICATION' in ROWS[0][1]
          and '14 GRADED CORRESPONDENCE TABLES' in ROWS[0][1]
          and 'NONE OF THE THREE WAS CITED BY ANY OF THE EIGHT ACTS' in ROWS[0][1]
          and 'DUPLICATED' in ROWS[0][1]
          and 'VIOLATED THE FRESHNESS RULE' in ROWS[0][1]
          and 'IT IS EXCLUDED' in ROWS[0][1]
          and 'A REAL AMENDMENT AND NOT A CLARIFICATION' in ROWS[0][1]
          and 'NOT-YET-SYNTHESIZED, NOT OWED AND NOT DEFICIENT' in ROWS[0][1]
          and 'NO GRADE MOVED AND NO ACT RE-VERDICTED' in ROWS[0][1]
          and 'PRICED AND NOT ORDERED' in ROWS[0][1]
          and 'NAMED UNPRICED' in ROWS[0][1]
          and 'A SEAT CANNOT RESTATE A RULE IT CANNOT READ' in ROWS[0][1]
          and 'NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN' in ROWS[0][2]
          and 'QUOTING A STANDARD IS NOT AMENDING IT' in ROWS[0][2]
          and 'NO CLASS WAS RULED' in ROWS[0][3]
          and 'NO STANDARD WAS EDITED' in ROWS[0][3]
          and 'WITHOUT DEFENCE' in ROWS[0][4]
          and "NOT ADOPTED ON HIS WORD" in ROWS[0][4]
          and 'THE AUTHOR AMENDS' in ROWS[0][4]
          and 'MINTED BY THIS SEAT' in ROWS[0][4]
          and 'THE STANDARD READ, THE SEQUENCE RECONCILED' in ROWS[0][5]
          and 'NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says the ruled standard, the stamped gate, the pre-lock amendment, the canonical '
        'read, the re-read quotations, the four tiers, the fourteen tables, the uncited sources, '
        'the reconciliation, the freshness violation, the excluded conjunction, the real amendment, '
        'the not-yet-synthesized clusters, the priced sweep, the unreadable rule, and the scope '
        ': %s' % g1)
    if not g1:
        run_clock.write(D, 'b383_desk_notes', LINES)
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
            run_clock.write(D, 'b383_desk_notes', LINES)
            return 1
        rownum = start

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE INDEX KEY.')
    rec('-' * 100)
    kok = do_key(rownum)
    rec('')
    rec('-' * 100)
    rec('  ### (5) THE THREE STANDING DOCUMENTS, UNEDITED.')
    rec('-' * 100)
    ev_ok, ev_bad = True, []
    unedited = AC['standards_unedited']
    for k, v in unedited.items():
        rec('    %-56s byte-identical to its blob : %s' % (k, v))
        ev_ok = ev_ok and bool(v)
    rec('  ### ### **STANDARDS EDITED : %d. ### AMENDMENTS APPLIED : %d.**'
        % (AC['standards_edited'], AC['amendments_applied']))
    rec('  ### ### **QUOTING A STANDARD IS NOT AMENDING IT, AND DRAFTING AN AMENDMENT IS NOT')
    rec('  ### ### APPLYING ONE.**')

    rec('')
    rec('-' * 100)
    rec('  ### (6) THE BANK.')
    rec('-' * 100)
    B = []
    BAR, SUB = '=' * 100, '-' * 100
    B.append(BAR)
    B.append('b383 -- THE STANDARD READ, THE SEQUENCE RECONCILED, THE MODEL BANKED. ### THE BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **THE CORPUS ALREADY CARRIED AN AUTHOR-RULED ANSWER TO THE CLASS')
    B.append('### ### ### QUESTION, AND THE EIGHT-ACT SEQUENCE DID NOT CITE IT.**')
    B.append('### `THE_DOCUMENT_CLASS_TAXONOMY.md` -- ### **STANDING STANDARD, 2026-07-28,')
    B.append('### ### AUTHOR-RULED** -- fixes four tiers and, for each one, ### **WHAT IT MUST CARRY')
    B.append('### ### AND HOW IT MAY BE CITED.** ### The registry`s ### **PHASE ATTRIBUTE** ###')
    B.append('### section reconciles the rubric`s `WHEN` with the registry`s `WHERE`. ### And')
    B.append('### `THE_LOAD_BEARING_MAP.md`, ### **THE KEYSTONE CORRESPONDENCE UNION**, already names')
    B.append('### ### **14 GRADED CORRESPONDENCE TABLES.**')
    B.append('### ### ### **THE SEQUENCE RECONCILES AS %d DUPLICATED AND %d ADDS.**'
             % (AC['duplicated'], AC['adds']))
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 1 -- THE STANDING STANDARD, QUOTED AT THE CANONICAL DRIVE.')
    B.append(SUB)
    B.append('### ### **THE FULL QUOTATION SET IS THIS ACT`S RUN RECORD, `data/%s`**,'
             % AC['run_file'])
    B.append('### where every line carries its file and its line number and ### **WAS RE-READ OUT OF')
    B.append('### ### THAT FILE BEFORE IT WAS WRITTEN.** ### **QUOTATIONS THAT FAILED TO RE-READ :')
    B.append('### ### %d.**' % len(AC['reread_failures']))
    B.append('### ### **SOURCES READ : %d. ### TIERS QUOTED WITH OBLIGATION AND CITATION RULE : %d.**'
             % (AC['sources_read'], AC['tiers_quoted']))
    B.append('')
    B.append('### ### **THE FOUR TIERS, IN THE STANDARD`S OWN TERMS:**')
    B.append('###   ### **TIER K -- KEYSTONE-CERTIFIED.** ### Claims backed by a machine-checked')
    B.append('###     kernel terminal at a pin. ### *Obligation:* every such claim states its')
    B.append('###     ### **`grade . terminal . pin`**, and the axiom profile in full. ### *Citation')
    B.append('###     rule:* ### **MAY BE CITED AS CERTIFICATION.**')
    B.append('###   ### **TIER C -- CLUSTER-SYNTHESIS.** ### A document that ### **ORGANIZES** ###')
    B.append('###     certified results, asserting ### *relationships not individually certified.*')
    B.append('###     ### *Citation rule:* ### **CITE FOR ORIENTATION AND ORGANIZATION -- NEVER AS')
    B.append('###     ### CERTIFICATION.** ### The standard calls this ### **ITS LOAD-BEARING RULE.**')
    B.append('###   ### **TIER N -- NOTES / EXPLORATORY.** ### *Citation rule:* ### **REFERENCE-ONLY')
    B.append('###     ### -- a Tier-N claim is a lead, not a result.**')
    B.append('###   ### **TIER E -- FILING-FACING.** ### Every technical claim still states its')
    B.append('###     ### **`grade . terminal . pin`** -- ### *Tier E relaxes the audience, never the')
    B.append('###     certificate.* ### *Citation rule:* ### **TIER E CITES TIER K; NOTHING CITES')
    B.append('###     ### TIER E.**')
    B.append('### ### ### **AND THE FAILURE IT WAS BUILT TO PREVENT, IN ITS OWN WORDS:** ### *the')
    B.append('### ### taxonomy exists to make two failures structurally impossible: a synthesis being')
    B.append('### ### read as a certification, and a filing-facing framing being read as the record.*')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 2 -- THE SEQUENCE RECONCILED, WITHOUT DEFENCE.')
    B.append(SUB)
    B.append('###   %-6s %-58s %s' % ('ACT', 'WHAT IT ASKED', 'VERDICT'))
    for r in AC['rows']:
        B.append('###   %-6s %-58s ### **%s**' % (r['act'], r['asked'][:58], r['verdict']))
    B.append('### ### **DUPLICATED : %d ### / ### ADDS : %d.**' % (AC['duplicated'], AC['adds']))
    B.append('### ### ### **THE STANDARD HAD ALREADY RULED THE CLASS QUESTION AND NONE OF THE EIGHT')
    B.append('### ### ### ACTS CITED IT, THE REGISTRY SECTION, OR THE UNION.**')
    B.append('### ### **WHAT THE SEQUENCE ADDS IS NARROWER THAN ITS OWN BANKS SUGGEST:** ###')
    B.append('### `b376`s two-axis ### **SEPARATION**; `b378`s facts about kernels at refs; and')
    B.append('### `b380`, `b381`, `b382` -- ### **TWO NEGATIVE RESULTS ABOUT TWO PREDICATES AND A')
    B.append('### ### CONCLUSION THE STANDARD ASSUMES BUT NOWHERE ARGUES.**')
    B.append('')
    B.append('### ### ### **AND THE SEQUENCE VIOLATED A FRESHNESS RULE THIS SEAT MINTED AT `b368`.**')
    B.append('### `DESK_FRESHNESS.md`: ### *every desk item names the FILE and the DATE at which it')
    B.append('### was last confirmed; an item without one is RE-VERIFIED before it is ordered* -- and')
    B.append('### ### *the cost was not a wrong belief. ### It was ### **A RIGHT BELIEF WITH NO DATE')
    B.append('### ### ON IT**, and a second act spent to re-derive what a first act had already')
    B.append('### banked.* ### **THE PREMISE THE SEQUENCE RAN ON CARRIED NO DATE.**')
    B.append('')
    B.append('### ### ### **THE NAVIGATOR`S READING : %s.**' % AC['verdict'])
    B.append('### ### **RIGHT IN SUBSTANCE:** ### the two axes ARE the two tiers -- Tier K`s')
    B.append('### obligation IS the apparatus axis; Tier C`s ### *organizes ... relationships not')
    B.append('### individually certified* ### IS the role axis.')
    B.append('### ### **WRONG IN ONE PARTICULAR, AND IT MATTERS: THE CONJUNCTION IS NOT MERELY')
    B.append('### ### UNNAMED. ### IT IS EXCLUDED.**')
    B.append('###   ### **(a)** ### the two citation rules contradict -- ### **MAY BE CITED AS')
    B.append('###     ### CERTIFICATION** ### against ### **NEVER AS CERTIFICATION** -- so no single')
    B.append('###     document can carry both;')
    B.append('###   ### **(b)** ### the standard already disposes of the mixed document by')
    B.append('###     ### **RULING ONE TIER AND READING THE PARTS APART**: ### *CATALOGOS ... Read')
    B.append('###     the panels as C, the pinned terminals as K*;')
    B.append('###   ### **(c)** ### and `b186`s predecessor scheme was ### **RETIRED** ### precisely')
    B.append('###     because its class ### *spanned Tier K and Tier C at once -- collapsing the very')
    B.append('###     distinction the standing taxonomy exists to enforce.*')
    B.append('### ### ### **SO THE AUTHOR`S FINISHED KEYSTONE IS A REAL AMENDMENT AND NOT A')
    B.append('### ### ### CLARIFICATION.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 3 -- THE AUTHOR`S MODEL, BANKED VERBATIM.')
    B.append(SUB)
    B.append('### ### **%d LINES, %d DROPPED**, sliced whole from the ferry between two ends each'
             % (AC['model_lines'], AC['model_dropped']))
    B.append('### verified unique. ### The full text is in `data/%s`.' % AC['run_file'])
    B.append('### ### **IT IS BANKED AS THE AUTHOR`S STATEMENT AND NOT ADOPTED AS THIS SEAT`S')
    B.append('### ### FINDING:** ### no document is measured against it and ### **NONE IS RULED')
    B.append('### ### UNDER IT.**')
    B.append('### ### **THE AUTHOR`S REASON, BANKED VERBATIM:** ### *it is a laboratory -- an ongoing')
    B.append('### research programme that hopes to continue synthesizing further research with and')
    B.append('### against these foundational results as they stand.*')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 4 -- THE FOUR AMENDMENTS, DRAFTED AND ROUTED.')
    B.append(SUB)
    B.append('### ### **DRAFTED : %d. ### APPLIED : %d. ### STANDARDS EDITED : %d.**'
             % (AC['amendments_drafted'], AC['amendments_applied'], AC['standards_edited']))
    B.append('###   ### **(i) THE FINISHED-KEYSTONE FURNITURE OBLIGATION**, in the author`s words --')
    B.append('###     and ### **A REAL AMENDMENT**, because it asks one document to carry the Tier-C')
    B.append('###     role and the Tier-K obligation at once. ### **THE AUTHOR MUST ALSO SAY WHAT A')
    B.append('###     ### FINISHED KEYSTONE IS CITED AS. ### THIS SEAT DOES NOT CHOOSE.**')
    B.append('###   ### **(ii) THE CLUSTER UNIT**, as the author`s amendment of 2026-09-09 replaced')
    B.append('###     it: every document belongs to a subject cluster so its content is read into')
    B.append('###     that cluster`s synthesis rather than sitting isolated; ### **A CLUSTER MAY')
    B.append('###     ### HAVE SEVERAL KEYSTONES, ONE, OR NONE YET**; the relation is many-to-many')
    B.append('###     and changes over time, because clusters and their kernel constellations are')
    B.append('###     ### **AMORPHOUS**, and a keystone is ### **A SYNTHESIS AT A MOMENT** -- later')
    B.append('###     research may produce ### **ANOTHER KEYSTONE BESIDE IT RATHER THAN SUPERSEDING')
    B.append('###     ### IT.**')
    B.append('###   ### **(iii) THE PER-DOCUMENT TIER SWEEP**, which the standard itself names as')
    B.append('###     ### **ITS STANDING FOLLOW-ON** ### and which has been unrun since July.')
    B.append('###   ### **(iv) THE REVIEWER-RESERVOIR RULE** -- ### **ROUTED AS A REQUEST.**')
    B.append('')
    B.append('### ### ### **THE CLUSTER COUNT, WITH THE AUTHOR`S RULE STATED BESIDE IT:**')
    B.append('###   ### **`%d` SUBJECT CLUSTERS HAVE REGISTRY ROWS AND NO KEYSTONE.**' % len(NOKEY))
    B.append('###   ### **THE RULE:** ### a cluster may have SEVERAL keystones, ONE, or NONE YET;')
    B.append('###   the relation is many-to-many and it changes over time. ### **A CLUSTER WITH NO')
    B.append('###   ### KEYSTONE IS `NOT-YET-SYNTHESIZED`, NOT OWED AND NOT DEFICIENT.**')
    B.append('###   ### ### **SO A PLURALITY IS NEVER READ AS AN ANOMALY AND AN ABSENCE IS NEVER')
    B.append('###   ### ### READ AS A DEFECT**, and ### **NO GRADE IS MOVED AND NO ACT IS')
    B.append('###   ### ### RE-VERDICTED** ### by the restatement.')
    B.append('')
    B.append('### ### **THE SWEEP, PRICED FROM THE RECORD`S OWN FIGURES AND ### NOT ORDERED:**')
    B.append('###   the standard`s own estimate      : ### **`~200` RECORDS**, its words')
    B.append('###   the census`s measured population : ### **`%d` DOCUMENTS**'
             % (AC['declared_class_line'] + AC['not_declared_class_line']))
    B.append('###   already carrying a class line    : ### **`%d`**' % AC['declared_class_line'])
    B.append('###   carrying none                    : ### **`%d`**' % AC['not_declared_class_line'])
    B.append('### ### **SO `%d` TO CONFIRM AND `%d` TO DECIDE FROM SCRATCH**, and the two population'
             % (AC['declared_class_line'], AC['not_declared_class_line']))
    B.append('### figures are themselves something the sweep would reconcile -- neither is wrong for')
    B.append('### its own date.')
    B.append('### ### ### **WHAT THE RECORD CANNOT PRICE IS THE PER-DOCUMENT JUDGEMENT**, since most')
    B.append('### documents say nothing about their own role. ### **UNPRICED, AND NAMED UNPRICED')
    B.append('### ### RATHER THAN ESTIMATED. ### A PRICE IS NOT A PROPOSAL.**')
    B.append('')
    B.append('### ### **AND THE REVIEWER-RESERVOIR RULE COULD NOT BE LOCATED.** ### A controlled')
    B.append('### sweep of the canonical tree, the relay tools and the TECHNE modules ran before the')
    B.append('### lock, with a ### **POSITIVE CONTROL FIRING ON `%d` FILES** ### and with this act`s'
             % AC['control_hits'])
    B.append('### own files ### **EXCLUDED** ### (`b368`s rule).')
    B.append('### ### **A SEAT CANNOT RESTATE A RULE IT CANNOT READ**, and a seat that supplies the')
    B.append('### words itself has ### **WRITTEN A NEW RULE UNDER AN OLD NAME.** ### So `(iv)` is a')
    B.append('### ### **REQUEST FOR THE RULE`S LOCATION OR ITS TEXT.**')
    B.append('')
    B.append(SUB)
    B.append('### THE DESK, THE WRITES, AND WHAT THIS ACT DID NOT DO.')
    B.append(SUB)
    B.append('### desk items swept : %d ### / ### closed : %d ### / ### standing : %d ### / ### '
             'lists closed : %d' % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
    B.append('### trail block appended (append-only %s, committed prefix intact %s); '
             '`CORRESPONDENCE.md` row %s;'
             % (tr['appended_only'], tr['committed_prefix_intact'], rownum))
    B.append('### index key `the-standing-standard-read-and-the-sequence-reconciled` reachable by')
    B.append('### every alias : %s' % kok)
    B.append('### ### **THE THREE STANDING DOCUMENTS, BYTE-IDENTICAL TO THEIR BLOBS:**')
    for k, v in AC['standards_unedited'].items():
        B.append('###   %-56s %s' % (k, v))
    B.append('### ### ### **QUOTING A STANDARD IS NOT AMENDING IT, AND DRAFTING AN AMENDMENT IS NOT')
    B.append('### ### ### APPLYING ONE.**')
    B.append('')
    B.append('### ### **NO STANDARD WAS EDITED. ### NO AMENDMENT WAS APPLIED. ### NO CLASS WAS')
    B.append('### ### RULED. ### NO DOCUMENT WAS RECLASSIFIED. ### NO DECLARATION WAS MOVED. ### NO')
    B.append('### ### GRADE WAS MOVED. ### NO ACT WAS RE-VERDICTED. ### NO LIST WAS CLOSED. ### THE')
    B.append('### ### REGISTRY WAS NOT EDITED.**')
    B.append('### ### **NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL** ### and ### **THE MIRROR WAS')
    B.append('### ### NOT OPENED.** ### No archive file was touched and the `86` unconfirmed stay')
    B.append('### unconfirmed. ### **NO `.lean` FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE')
    B.append('### ### RECOMPUTED.**')
    B.append('### **THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED. ### THE POSTURE')
    B.append('### LOCK IS SEPARATE.** ### `h2` stands exactly where the deposit left it and this act')
    B.append('### makes no claim about it in either direction. ### **NOTHING IS DEPOSITED AND')
    B.append('### ### NOTHING WAS WRITTEN AT ZENODO.**')
    B.append('')
    B.append(SUB)
    B.append('### WHAT THIS LEG ADDS TO THE LORE.')
    B.append(SUB)
    B.append('### ### ### **NEW -- `AN EIGHT-ACT SEQUENCE CAN RE-DERIVE A RULED STANDARD WITHOUT`')
    B.append('### ### ### `EVER CITING IT`.** ### The taxonomy, the registry section and the union')
    B.append('### were all in the tree, author-ruled, dated, and ### **NONE WAS CITED ONCE.** ### The')
    B.append('### cost was not a wrong answer: three of the eight acts reached the RIGHT answer')
    B.append('### ### **BY MEASUREMENT, WHERE A READ WOULD HAVE DONE.**')
    B.append('### ### ### **NEW -- `THE RULE THAT NAMES A SPECIES DOES NOT PREVENT IT`.** ### This')
    B.append('### seat minted `DESK_FRESHNESS` at `b368` -- ### *a right belief with no date on it* ###')
    B.append('### -- and then ran an eight-act sequence on exactly that. ### **A MINTED RULE IS NOT A')
    B.append('### ### CARRIED RULE**, which is `b378`s species arriving one level up.')
    B.append('### ### ### **NEW -- `AN UNNAMED CLASS AND AN EXCLUDED ONE ARE DIFFERENT FINDINGS`.**')
    B.append('### The reading said the standard never names the conjunction. ### It does more: ###')
    B.append('### **IT FORECLOSES IT BY ITS LOAD-BEARING CITATION RULE AND RETIRED A PREDECESSOR FOR')
    B.append('### ### SPANNING THE TWO** -- which turns the author`s model from a gloss into an')
    B.append('### amendment, and that is the difference the verdict `%s` records.' % AC['verdict'])
    B.append('### ### ### **NEW -- `A SEAT CANNOT RESTATE A RULE IT CANNOT READ`.** ### Supplying the')
    B.append('### words is ### **WRITING A NEW RULE UNDER AN OLD NAME**, so the request is routed')
    B.append('### instead.')
    B.append('### **MET AGAIN -- A SWEEP EXCLUDES ITS OWN ACT`S FILES** (`b368`): the reservoir probe')
    B.append('### list counted itself until it was excluded.')
    B.append('### **MET AGAIN -- AN ABSENCE NEEDS A PROVED SEARCH** (`b378`), and ### **A QUOTATION')
    B.append('### WITH HOLES IN IT IS NOT A QUOTATION** (`b381`).')
    B.append('')
    B.append(SUB)
    B.append('### THE RECORD.')
    B.append(SUB)
    regtxt = io.open(os.path.join(D, 'b383_registration_2026-09-09.txt'), encoding='utf-8').read()
    m_sha = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt)
    m_by = re.search(r'bytes locked : (\d+)', regtxt)
    m_at = re.search(r'locked at \(UTC\) : (\S+)', regtxt)
    B.append('### registration locked at (UTC) %s' % (m_at.group(1) if m_at else '?'))
    B.append('### ### **%s bytes, sha256 `%s`, %d clauses, ### LOCKED BEFORE ANY WRITE AND CHAINED'
             % (m_by.group(1) if m_by else '?', m_sha.group(1) if m_sha else '?',
                len(J('b383_satisfiable')['clauses'])))
    B.append('### ### ON A GATE THAT CHECKS WHAT EACH GATE READ.** ### %d gates read, %d checked by '
             'digest.' % (LG['gates_read'], LG['face_subject_gates']))
    B.append('### ### **AND THE AUTHOR`S AMENDMENT TO COMPONENT 4(ii) ARRIVED BEFORE THIS LOCK**, so')
    B.append('### its own conditional did not fire and it governs the face as well as the routed')
    B.append('### text. ### The extract`s clock is `%s` and the lock`s is `%s`.'
             % (E.get('run_clock'), (m_at.group(1) if m_at else '?')))
    for n in ('b383_reads', 'b383_lockgate', 'b383_components'):
        j = J(n)
        B.append('### %-18s run file `%s` recorded clock %s'
                 % (n, j['run_file'], j.get('run_clock')))
    B.append('### **THE REFS THIS ACT READ IN THE ROSTERED REPOSITORIES:**')
    for k, v in E['refs'].items():
        B.append('###   %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    B.append('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor. ### **EVERY ANCHOR WAS '
             'READ FROM ITS FILE AND NONE WAS TYPED**, and the three standing sources were read at'
             % (E['reads'], E['without_anchor']))
    B.append('### ### **THE CANONICAL DRIVE, NEVER THE MIRROR.**')
    B.append('### ### **SIX NEW `relay` TOOLS AGAINST A CAP OF SIX, AND NO SHARED UTILITY.**')
    B.append(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### A CLASS WAS RULED.', '### A DECLARATION WAS MOVED.', '### A LIST WAS CLOSED.',
                '### THE DECLARATION RULE IS ORDERED.', '### THE PREFERRED OPTION IS.',
                '### A QUOTATION DID NOT RE-READ.', '### THE EVIDENCE FILE WAS REWRITTEN.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))

    rec('')
    rec('=' * 100)
    rec('  ### desk swept %d ; trail appended %s ; row %s ; key %s'
        % (Q['items'], tr['appended_only'], rownum, kok))
    rec('  ### ### **LISTS CLOSED : 0. ### THE FOUR ARE RESTATED `OPEN` BY NAME.**')
    rec('  ### ### **THE ONE DESK CLOSURE IS THE SEQUENCE ITSELF.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b383_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             evidence_appended=ev_ok, evidence_placeholders=len(ev_bad),
             bank='b383_the_sequence_stopped.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b383_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and ev_ok and not ev_bad and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
