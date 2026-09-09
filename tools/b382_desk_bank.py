# -*- coding: utf-8 -*-
"""b382_desk_bank.py -- THE DESK UNDER `(R7)`, THE THREE CLOSING WRITES, AND THE BANK.

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
MARK = '<!-- b382 the sequence stopped; the evidence closed -->'
PRIOR = '<!-- b379 the apparatus axis re-scored; two filings -->'
ACT = 'b382'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


AC = J('b382_account')
LG = J('b382_lockgate')
C81, EX81, VD81 = J('b381_control'), J('b381_exemplars'), J('b381_verdict')
RS80 = J('b380_rescore')
CL375 = J('b375_clusters')
NOKEY = CL375['subject_clusters_without_keystone']
EVID = os.path.join(D, 'b380_ruling_evidence.txt')
BANKOUT = os.path.join(D, 'b382_the_sequence_stopped.txt')

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

    # ---- CARRIED, AND RESTATED FOR THE RULING -------------------------------------------------------
    ('the class ruling itself', 'STAND', None, None,
     'STILL THE AUTHOR`S. ### The evidence is now ### **CLOSED AND NAMED COMPLETE** ### as this '
     'sequence`s product. ### **NO CLASS IS RULED, NO OPTION RECOMMENDED, AND NOTHING ORDERED**'),
    ('the download-layer book`s registry drift', 'STAND', None, None,
     'OPEN AND ### **THE AUTHOR`S**, in `(R14)`s own words. ### The registry is not edited and the '
     'book is not opened'),
    ('the six subject clusters with registry rows and no keystone', 'STAND', None, None,
     'FILED and ### **STILL NOT OPENED.** ### %d clusters, unchanged since b375' % len(NOKEY)),
    ("the census's definition-versus-operation drift", 'STAND', None, None,
     'FILED at b377 and ### **NOT REPAIRED** -- repairing it belongs to the ruling'),
    ('the 86 archive files the mirror does not carry', 'STAND', None, None,
     'CARRIED and ### **STILL UNCONFIRMED**'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', None, None,
     'CARRIED and ### **DELIBERATELY NOT RE-MEASURED.** ### b377`s amendment forbade it and no '
     'later order has lifted that'),
    ('the premise that the corpus does not say what it does', 'STAND', None, None,
     'CARRIED and ### **RE-MEASURED UNDER ALL THREE READINGS AT b382:** ### `%d` of `%d` strict, '
     '`%d` of `%d` broad, `%d` of `%d` by purpose statement. ### **EVEN THE MOST GENEROUS FINDS '
     'ROLE STATED BY A MINORITY**'
     % (AC['population'] - AC['strict_silent'], AC['population'],
        AC['population'] - AC['broad_silent'], AC['population'],
        AC['b381_wide'], AC['b381_scanned'])),

    # ---- WHAT THIS ACT ADDS -------------------------------------------------------------------------
    ('the evidence sequence, b375 through b381', 'CLOSE', 'b382_account_notes',
     'NOTHING IS CLOSED BY THIS ACT EXCEPT THE SEQUENCE ITSELF',
     'CLOSED at b382 by the author`s own instruction. ### **THE OCCASION IS GONE BECAUSE THE '
     'AUTHOR STOPPED IT:** ### the relating-word feature is NOT built, and the reason is recorded '
     'as the author`s -- ### **IT WOULD NEED A SENTENCE UNDERSTOOD RATHER THAN A STRUCTURE '
     'MEASURED, WHICH IS A READER AND NOT A PREDICATE.** ### `%d` acts accounted for, every claim '
     'anchored, `%d` quotations failing to re-read' % (AC['acts_covered'], len(AC['reread_failures']))),
    ('the conclusion the evidence supports', 'STAND', None, None,
     'NEW at b382 and it is ### **ABOUT METHOD AND NOT A CLASS:** ### role is not recoverable from '
     'a document`s structure, and it is stated by too few documents to be recoverable from their '
     'prose, so a class ruling ### **MUST REST ON DECLARATION RATHER THAN ON CLASSIFICATION.** ### '
     '**AND THE LIMIT IS STATED WITH IT: TWO FAILED FEATURES ARE EVIDENCE AND NOT PROOF**'),
    ('what a declaration rule would oblige, priced', 'STAND', None, None,
     'NEW at b382 and ### **PRICED, NOT ORDERED. ### A PRICE IS NOT A PROPOSAL.** ### One rule '
     'document; ### **`%d` DOCUMENTS LACKING A CLASS LINE**, and separately `%d` of the `%d` say '
     'nothing about their own role so for most the line cannot be written from the document`s own '
     'text -- ### **THE OVERLAP OF THE TWO IS NOT IN THE RECORD AND IS NAMED UNCOUNTED**; and a '
     'phased application ### **NAMED UNPRICED RATHER THAN ESTIMATED**'
     % (AC['not_declared_class_line'], AC['strict_silent'], AC['population'])),
    ('the exemplar caution, carried forward', 'STAND', None, None,
     'NEW at b382: the gathering exemplar set came from a matcher repaired twice after its output '
     'was seen (`%d` -> `%d` -> `%d`). ### **IF IT IS EVER REUSED IT IS RE-DERIVED AND NOT '
     'INHERITED**, and ### **NOTHING CURRENTLY RESTS ON IT** -- measured against b381`s own banked '
     'JSON, not repeated from it' % (EX81['loose_hits'], EX81['loose2_hits'], EX81['wide_hits'])),
    ('the ten untracked run records of earlier acts', 'STAND', None, None,
     'NAMED at b382 and ### **STILL UNTRACKED.** ### b381 swept them in with `git add -A` and '
     'reverted them; ### **THEY ARE NOT THIS ACT`S TO COMMIT EITHER**, and naming them is the '
     'whole of what this act does about them -- so a later act does not rediscover them as a '
     'defect'),
    ('and this act`s own tool cap was mis-described on its locked face', 'STAND', None, None,
     'NEW at b382 and ### **REPORTED RATHER THAN QUIETLY EXCEEDED.** ### The face caps the act at '
     '### **SIX FILES** ### and the clause spec`s description then named ### **SEVEN ROLES.** ### '
     'The cap is the number: the desk sweeper and the bank writer are ### **ONE FILE**, and the '
     'act ships six'),
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
        '### **b382 \u2014 THE SEQUENCE STOPPED, AND THE EVIDENCE CLOSED (2026-09-09)**',
        '',
        ('*No block above is edited. The b381 block (`%s`) and every block before it stand exactly as '
         'they were written.*' % PRIOR),
        '',
        ('**THE AUTHOR STOPPED THE SEQUENCE, AND THE REASON IS RECORDED AS THE AUTHOR\u2019S.** The '
         'executor\u2019s draft offered a third structural feature or a stop; the author took the '
         'stop. **The relating-word feature is NOT built**, because reach and co-location both failed '
         'on a control rebuilt to be capable of failing, and a third feature **would need a sentence '
         'understood rather than a structure measured, which is a reader and not a predicate**. This '
         'act closes the evidence and **does not rule**.'),
        '',
        ('**THE SEQUENCE\u2019S OWN ACCOUNT, QUOTED AND NOT SUMMARISED.** Seven acts, b375 through '
         'b381, each given what it asked, what it found and what it left \u2014 and **every claim '
         'about a prior act carried by a line from that act\u2019s own bank, re-read out of that '
         'file at its own line number before it was written**. Quotations that failed to re-read: '
         '**%d**. b375 found the corpus carries three definitions of *keystone* and that the same '
         'instrument, run on two of them one act apart, gives opposite answers. b376 found **all '
         'three tests cross the quadrants** and that the corpus\u2019s own census drops a clause it '
         'states and adds a size floor its definition never mentions. b377 found the missing element '
         'was the pin, not the terminal, and fixed the reconciliation figure as **a floor and not an '
         'answer**. b378 found that a count taken at one ref is not a count \u2014 and that its own '
         'sweep had been silently dead. b379 corrected the apparatus column and **moved nothing where '
         'the ruling needs movement**. b380 moved the role column for the first time and **failed its '
         'own control on both documents that declare gathering**. b381 rebuilt the control so it '
         'could fail in both directions and **the second feature failed on it**.'
         % len(AC['reread_failures'])),
        '',
        ('**THE STANDING COUNT, RE-MEASURED RATHER THAN CARRIED, BECAUSE THE CONCLUSION RESTS ON IT.** '
         'Documents that state a role: **%d of %d** under b376\u2019s strict reading, **%d of %d** '
         'under its broad one, and **%d of %d** under b381\u2019s purpose-statement reading \u2014 '
         'the most generous of the three. **Even the most generous finds role stated by a minority**, '
         'and finds it stated almost entirely on one side: %d heads state a *gathering* purpose while '
         '**%d documents declare synthesis in their class line**. The side the rubric turns on is the '
         'side the corpus is nearly silent about.'
         % (AC['population'] - AC['strict_silent'], AC['population'],
            AC['population'] - AC['broad_silent'], AC['population'],
            AC['b381_wide'], AC['b381_scanned'], AC['b381_wide'], C81['synthesis_n'])),
        '',
        ('**THE CONCLUSION THE EVIDENCE SUPPORTS, ABOUT METHOD AND NOT A CLASS: role is not '
         'recoverable from a document\u2019s structure, and it is stated by too few documents to be '
         'recoverable from their prose. So a class ruling, whatever it rules, must rest on '
         'DECLARATION rather than on classification.** The first half is evidenced by two features '
         'that failed on a control built to fail; the second by the count above. **And the limit is '
         'stated with the conclusion and not below it: two failed features are evidence and not '
         'proof.** A third feature might separate the control; the author judged it a reader\u2019s '
         'work and not a predicate\u2019s, and **that judgement is recorded as the author\u2019s and '
         'not as a measurement this seat made**.'),
        '',
        ('**WHAT A DECLARATION RULE WOULD OBLIGE, PRICED FROM THE RECORD\u2019S OWN FIGURES AND NOT '
         'ORDERED \u2014 a price is not a proposal.** *(i)* A rule saying what a declaration must '
         'say, and **which of the three definitions of keystone it declares against**: one document, '
         'the author\u2019s, and the piece nothing else can proceed without. *(ii)* A class line in '
         'every document lacking one: **%d documents**, each a one-line append. And what the line '
         '*costs* is not typing: **%d of the %d say nothing about their own role**, so for most '
         'documents it cannot be written from the document\u2019s own text and is a judgement '
         '\u2014 the author\u2019s. **How many of the %d are also among the %d is not in the '
         'record**: the class-line census banked counts and not lists, so the overlap is **named '
         'uncounted rather than estimated** \u2014 two figures over two populations are not a '
         'subset. *(iii)* A phased application: '
         '**UNPRICED, and named unpriced rather than estimated**, because the record counts documents '
         'and clusters and does not count reviewer effort or elapsed time.'
         % (AC['not_declared_class_line'], AC['strict_silent'], AC['population'],
            AC['not_declared_class_line'], AC['strict_silent'])),
        '',
        ('**THE EXEMPLAR CAUTION TRAVELS WITH THE SET.** b381\u2019s gathering exemplars came from a '
         'matcher **repaired twice after its output was seen** \u2014 %d then %d then %d heads out '
         'of %d, all three printed rather than the last presented as the first. **If that set is ever '
         'reused it is re-derived and not inherited.** And **nothing currently rests on it**, checked '
         'against b381\u2019s own banked JSON rather than repeated from it: the branch did not adopt, '
         'the corpus was not scored, and no prior score was overwritten.'
         % (EX81['loose_hits'], EX81['loose2_hits'], EX81['wide_hits'], EX81['scanned'])),
        '',
        ('**THE OPEN ITEMS, RESTATED FOR THE RULING.** The four lists stand **OPEN by name**: the '
         'rows citing at a ref nobody can name; the rows grading a declaration the record has '
         'classified absent; the undated figures across the roster; the bibliography entries nothing '
         'cites. **The download-layer book\u2019s registry drift stays OPEN and is the '
         'author\u2019s**, in (R14)\u2019s own words \u2014 the registry is not edited and the book '
         'is not opened. **The %d subject clusters with registry rows and no keystone stay filed and '
         'not opened.** And the reconciliation figure stays **a floor against the wider question**, '
         'which b377\u2019s amendment forbade re-measuring and no later order has lifted.'
         % len(NOKEY)),
        '',
        ('**THE TEN UNTRACKED RUN RECORDS ARE NAMED AND STILL UNTRACKED.** b381 swept records left by '
         'b259, b346\u2013b349, b363 and b371 into a commit with `git add -A` and reverted them. '
         'They are named in this act\u2019s own record **so a later act does not rediscover them as '
         'a defect**, and **naming them is the whole of what this act does about them** \u2014 they '
         'are not this act\u2019s to commit either.'),
        '',
        ('**AND THIS ACT\u2019S OWN TOOL CAP WAS MIS-DESCRIBED ON ITS LOCKED FACE, WHICH IS REPORTED '
         'RATHER THAN QUIETLY EXCEEDED.** The face caps the act at **six** new relay tool files and '
         'the clause spec\u2019s description then named **seven roles**. The cap is the number: the '
         'desk sweeper and the bank writer are one file, and the act ships six. **The face stands and '
         'the contradiction is reported**, which is what the face\u2019s own opening sentence '
         'requires.'),
        '',
        ('**WHAT THIS ACT DID NOT DO.** No class ruled, **no declaration moved**, **no declaration '
         'rule ordered**, no list closed, **no corpus document written into at all**, REGISTRY.md not '
         'edited, nothing on the download layer touched, no archive file touched and the 86 '
         'unconfirmed still unconfirmed. **No prior score overwritten and the corpus not scored.** '
         'The relating-word feature was **not built**, by the author\u2019s instruction, and not '
         'built under another name. No `.lean` file touched, no build run, no axiom profile '
         'recomputed. h2 stands exactly where the deposit left it and this act makes no claim about '
         'it in either direction.'),
        '',
    ]


SCOPE = (
    "**SCOPE: THE SEQUENCE STOPPED, AND THE EVIDENCE CLOSED.** NO class ruled, NO document "
    "reclassified, NO declaration moved, NO declaration rule ordered, NO list closed. **NO CORPUS "
    "DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED.** **THE RELATING-WORD FEATURE "
    "WAS NOT BUILT**, by the author's instruction, and not built under another name; the reason is "
    "recorded as THE AUTHOR'S JUDGEMENT and not as a measurement this seat made. **THE ACCOUNT IS "
    "QUOTED AND NOT SUMMARISED**: every claim about a prior act carries a line from that act's own "
    "bank, RE-READ AT ITS OWN LINE NUMBER BEFORE IT WAS WRITTEN, and the count that failed to "
    "re-read is ZERO. **THE LOAD-BEARING COUNT WAS RE-MEASURED UNDER ALL THREE READINGS AND NOT "
    "CARRIED**, and the conclusion is required to survive the most generous. **THE CONCLUSION IS "
    "ABOUT METHOD AND NOT A CLASS**, and its limit is stated with it: TWO FAILED FEATURES ARE "
    "EVIDENCE AND NOT PROOF. **THE OBLIGATIONS ARE PRICED AND NONE IS ORDERED -- A PRICE IS NOT A "
    "PROPOSAL** -- and the part the record cannot price is NAMED UNPRICED RATHER THAN ESTIMATED. "
    "**THE EXEMPLAR CAUTION TRAVELS WITH THE SET**: re-derived and not inherited if reused, and the "
    "claim that nothing rests on it is CHECKED AGAINST b381'S BANKED JSON rather than repeated from "
    "it. **THE EVIDENCE FILE IS FINALISED BY AN APPENDED BLOCK AND NOTHING ABOVE IT WAS EDITED.** "
    "**THE TEN UNTRACKED RUN RECORDS ARE NAMED AND STILL UNTRACKED** -- naming them is not "
    "committing them. **AND THIS ACT'S OWN TOOL CAP WAS MIS-DESCRIBED ON ITS LOCKED FACE AND THE "
    "CONTRADICTION IS REPORTED RATHER THAN QUIETLY EXCEEDED**: six is the number and six is what "
    "shipped. **EVERY ABSENCE CARRIES A POSITIVE CONTROL THAT FINDS A KNOWN PRESENCE FIRST, AND AN "
    "ERROR EXIT IS NOT AN ANSWER.** **NO OPTION IS RECOMMENDED, RANKED OR PREFERRED** and the ruling "
    "remains the author's. **NO ARCHIVE FILE WAS TOUCHED** and the 86 unconfirmed stay unconfirmed. "
    "**NO OWNER INSTRUMENT WAS EDITED** -- role_structure, co_location, b378_lockgate, gate_hash and "
    "every prior act's bank are READ AND NOT MODIFIED. **THE FOUR OPEN LISTS ARE RESTATED OPEN BY "
    "NAME.** **NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS.** NO .lean FILE TOUCHED, NO BUILD "
    "RUN, NO AXIOM PROFILE RECOMPUTED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED "
    "SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or "
    "the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE "
    "PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under "
    "b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the "
    "patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE "
    "WAVE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it "
    "and this act makes no claim about it in either direction. NOTHING IS DEPOSITED AND NOTHING WAS "
    "WRITTEN AT ZENODO.")


def corr_rows(Q):
    m = ("**THE EVIDENCE SEQUENCE CLOSED: ROLE IS NOT RECOVERABLE FROM STRUCTURE AND IS STATED BY "
         "TOO FEW DOCUMENTS TO BE RECOVERABLE FROM PROSE, SO A CLASS RULING MUST REST ON "
         "DECLARATION** (b382, the sequence stopped, and the evidence closed)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b382, %d gates read and %d checked "
            "by digest. THE AUTHOR STOPPED THE SEQUENCE AND THE REASON IS RECORDED AS THE AUTHOR'S: "
            "the relating-word feature is NOT BUILT because a third feature would need A SENTENCE "
            "UNDERSTOOD RATHER THAN A STRUCTURE MEASURED, WHICH IS A READER AND NOT A PREDICATE. "
            "THE ACCOUNT IS QUOTED AND NOT SUMMARISED: %d acts, every claim about a prior act "
            "carried by a line from that act's own bank RE-READ AT ITS OWN LINE NUMBER, and %d "
            "quotations failed to re-read. b375 found THREE DEFINITIONS OF KEYSTONE and the same "
            "instrument giving opposite answers on two of them; b376 found ALL THREE TESTS CROSS "
            "THE QUADRANTS and the census dropping a clause it states while adding a size floor its "
            "definition never mentions; b377 found the missing element was THE PIN and fixed the "
            "reconciliation figure as A FLOOR AND NOT AN ANSWER; b378 found A COUNT TAKEN AT ONE "
            "REF IS NOT A COUNT and that its own sweep had been silently dead; b379 corrected the "
            "apparatus column and MOVED NOTHING WHERE THE RULING NEEDS MOVEMENT; b380 moved the "
            "role column and FAILED ITS OWN CONTROL ON BOTH GATHERING DECLARERS; b381 rebuilt the "
            "control so it could fail in both directions and THE SECOND FEATURE FAILED ON IT. THE "
            "LOAD-BEARING COUNT WAS RE-MEASURED AND NOT CARRIED: %d of %d documents state a role "
            "strictly, %d of %d broadly, %d of %d by purpose statement, and EVEN THE MOST GENEROUS "
            "READING FINDS ROLE STATED BY A MINORITY and almost entirely on one side. THE "
            "CONCLUSION IS ABOUT METHOD AND NOT A CLASS, and ITS LIMIT IS STATED WITH IT: TWO "
            "FAILED FEATURES ARE EVIDENCE AND NOT PROOF. WHAT A DECLARATION RULE WOULD OBLIGE IS "
            "PRICED AND NOT ORDERED: one rule document, %d documents lacking a class line, and "
            "separately %d of the %d saying nothing about their own role -- THE OVERLAP OF THE TWO "
            "IS NOT IN THE RECORD AND IS NAMED UNCOUNTED -- and a phased application NAMED UNPRICED "
            "RATHER THAN ESTIMATED. THE EXEMPLAR CAUTION TRAVELS WITH THE SET and NOTHING CURRENTLY "
            "RESTS ON IT, measured against b381's banked JSON. THE FOUR LISTS, THE REGISTRY DRIFT, "
            "THE SIX CLUSTERS AND THE FLOOR ARE ALL RESTATED OPEN, and NOTHING IS CLOSED BY THIS "
            "ACT EXCEPT THE SEQUENCE ITSELF"
            % (LG['gates_read'], LG['face_subject_gates'], AC['acts_covered'],
               len(AC['reread_failures']), AC['population'] - AC['strict_silent'],
               AC['population'], AC['population'] - AC['broad_silent'], AC['population'],
               AC['b381_wide'], AC['b381_scanned'], AC['not_declared_class_line'],
               AC['strict_silent'], AC['population']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN AND NO ROW WAS WRITTEN INTO ANY "
            "DOCUMENT. ### Seven prior banks were READ and quoted, each quotation re-read out of "
            "its own file at its own line number before it was written. ### NO STATEMENT WAS "
            "PROVED, NO BUILD WAS RUN AND NO AXIOM PROFILE WAS RECOMPUTED. ### AN ACCOUNT OF WHAT "
            "SEVEN ACTS FOUND IS NOT A NEW FINDING, AND THIS ACT MEASURED EXACTLY ONE THING: THE "
            "COUNT ITS CONCLUSION RESTS ON")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT THE "
            "OBJECT. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED, NO "
            "DECLARATION RULE ORDERED AND NO LIST CLOSED. ### NO CORPUS DOCUMENT WAS WRITTEN INTO "
            "AT ALL, REGISTRY.md WAS NOT EDITED, AND NOTHING ON THE DOWNLOAD LAYER WAS TOUCHED")
    grade = ("### EVIDENCE-CLOSED, AND THE CONCLUSION IS ABOUT METHOD. ### THE ORDER'S OWN WORD IS "
             "SUPPORTS AND NOT PROVES, and the act uses it: TWO FAILED FEATURES ARE EVIDENCE AND "
             "NOT PROOF, and a third might have separated the control. ### THE AUTHOR'S REASON FOR "
             "NOT BUILDING IT IS RECORDED AS THE AUTHOR'S JUDGEMENT AND NOT AS A MEASUREMENT THIS "
             "SEAT MADE. ### THE LOAD-BEARING COUNT WAS RE-MEASURED UNDER THREE READINGS AND THE "
             "CONCLUSION IS REQUIRED TO SURVIVE THE MOST GENEROUS OF THEM. ### THE OBLIGATIONS ARE "
             "PRICED AND NONE IS ORDERED, AND THE PART THE RECORD CANNOT PRICE IS NAMED UNPRICED "
             "RATHER THAN ESTIMATED. ### AND THIS ACT'S OWN LOCKED FACE MIS-DESCRIBED ITS TOOL CAP "
             "-- SIX FILES AGAINST SEVEN NAMED ROLES -- AND THE CONTRADICTION IS REPORTED RATHER "
             "THAN QUIETLY EXCEEDED")
    status = ("data/b382_the_sequence_stopped.txt; data/b380_ruling_evidence.txt (FINALISED by an "
              "appended block and NAMED COMPLETE as this sequence's product; nothing above it "
              "edited); data/%s; data/%s; data/b382_registration_2026-09-09.txt (LOCKED before any "
              "write, chained on tools/b378_lockgate.py run as b382); tools/b382_extract.py; "
              "tools/b382_account.py; tools/b382_desk_bank.py; PLACE-papers OPEN_TRAILS.md (an "
              "append-only block; NO CORPUS DOCUMENT EDITED AND REGISTRY.md NOT TOUCHED); "
              "CORRESPONDENCE.md row %%d"
              % (AC['run_file'], J('b382_reads')['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the sequence stopped', 'the evidence closed', 'role must be declared',
           'two failed features are evidence not proof', 'the declaration rule priced')
MUST_NOT_HIT = ('the class is ruled', 'the declarations are moved',
                'the declaration rule is ordered', 'the registry is edited')


def do_key(rownum):
    KEY = 'the-sequence-stopped-and-the-evidence-closed'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "THE SEQUENCE STOPPED AND THE EVIDENCE CLOSED. The author stopped it and the reason is "
        "recorded as the author own: the relating-word feature is NOT BUILT because a third feature "
        "would need A SENTENCE UNDERSTOOD RATHER THAN A STRUCTURE MEASURED, WHICH IS A READER AND "
        "NOT A PREDICATE. THE ACCOUNT IS QUOTED AND NOT SUMMARISED: %d acts from the census "
        "forward, every claim about a prior act carried by a line from that act own bank RE-READ AT "
        "ITS OWN LINE NUMBER, and %d quotations failed to re-read. THE LOAD-BEARING COUNT WAS "
        "RE-MEASURED AND NOT CARRIED: %d of %d documents state a role strictly, %d of %d broadly, "
        "%d of %d by purpose statement -- EVEN THE MOST GENEROUS READING FINDS ROLE STATED BY A "
        "MINORITY and almost entirely on one side, since only %d documents declare synthesis. THE "
        "CONCLUSION, ABOUT METHOD AND NOT A CLASS: ROLE IS NOT RECOVERABLE FROM A DOCUMENT "
        "STRUCTURE AND IS STATED BY TOO FEW DOCUMENTS TO BE RECOVERABLE FROM THEIR PROSE, SO A "
        "CLASS RULING MUST REST ON DECLARATION RATHER THAN ON CLASSIFICATION -- and ITS LIMIT IS "
        "STATED WITH IT: TWO FAILED FEATURES ARE EVIDENCE AND NOT PROOF. WHAT A DECLARATION RULE "
        "WOULD OBLIGE IS PRICED AND NOT ORDERED: one rule document naming which of the three "
        "definitions a declaration declares against; %d documents lacking a class line, and "
        "separately %d of the %d saying nothing about their own role so for most the line cannot "
        "be written from the document own text -- THE OVERLAP OF THE TWO IS NOT IN THE RECORD AND "
        "IS NAMED UNCOUNTED; and a phased application NAMED UNPRICED RATHER THAN ESTIMATED. THE EXEMPLAR CAUTION TRAVELS WITH THE SET: re-derived and not "
        "inherited if reused, and NOTHING CURRENTLY RESTS ON IT, measured against b381 banked JSON. "
        "THE FOUR LISTS, THE REGISTRY DRIFT, THE SIX CLUSTERS AND THE FLOOR ARE RESTATED OPEN."
        % (AC['acts_covered'], len(AC['reread_failures']),
           AC['population'] - AC['strict_silent'], AC['population'],
           AC['population'] - AC['broad_silent'], AC['population'],
           AC['b381_wide'], AC['b381_scanned'], C81['synthesis_n'],
           AC['not_declared_class_line'], AC['strict_silent'], AC['population']))
    grade = (
        "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED, NO DECLARATION "
        "RULE ORDERED AND NO LIST CLOSED. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND "
        "REGISTRY.md WAS NOT EDITED. ### THE RELATING-WORD FEATURE WAS NOT BUILT AND NOT BUILT "
        "UNDER ANOTHER NAME. ### THE ACCOUNT IS QUOTED AND EVERY QUOTATION RE-READ AT ITS OWN LINE. "
        "### THE LOAD-BEARING COUNT WAS RE-MEASURED UNDER THREE READINGS AND THE CONCLUSION SURVIVES "
        "THE MOST GENEROUS. ### THE OBLIGATIONS ARE PRICED AND NONE IS ORDERED -- A PRICE IS NOT A "
        "PROPOSAL -- AND THE PART THE RECORD CANNOT PRICE IS NAMED UNPRICED. ### TWO FAILED "
        "FEATURES ARE EVIDENCE AND NOT PROOF. ### THE EVIDENCE FILE WAS FINALISED BY AN APPENDED "
        "BLOCK AND NOTHING ABOVE IT WAS EDITED. ### THE TEN UNTRACKED RUN RECORDS ARE NAMED AND "
        "STILL UNTRACKED. ### THIS ACT LOCKED FACE MIS-DESCRIBED ITS OWN TOOL CAP AND THE "
        "CONTRADICTION IS REPORTED RATHER THAN QUIETLY EXCEEDED. ### THE FOUR OPEN LISTS ARE "
        "RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN "
        "FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED")
    where = (
        "data/b382_the_sequence_stopped.txt; data/b380_ruling_evidence.txt (FINALISED, appended, "
        "named complete); data/%s; data/%s; data/b382_registration_2026-09-09.txt (LOCKED before "
        "any write, chained on tools/b378_lockgate.py run as b382 -- %d gates read, %d checked by "
        "digest); tools/b382_extract.py; tools/b382_account.py; tools/b382_desk_bank.py; "
        "PLACE-papers OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row %d"
        % (AC['run_file'], J('b382_reads')['run_file'], LG['gates_read'],
           LG['face_subject_gates'], rownum))
    act = ("b382 (the sequence's own account, quoted; the conclusion about method; the exemplar "
           "caution; the open items restated)")
    row_new = ('    # ### THE SEQUENCE STOPPED, AND THE EVIDENCE CLOSED (b382).%s'
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
        rec('    %-44s reaches the b382 key : %s' % (q, g))
    for lbl, cond in (('no class ruled, no declaration moved',
                       'NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED' in out),
                      ('no declaration rule ordered',
                       'NO DECLARATION RULE ORDERED' in out),
                      ('no corpus document written into and no registry edit',
                       'NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED'
                       in out),
                      ('the relating-word feature was not built',
                       'NOT BUILT AND NOT BUILT UNDER ANOTHER NAME' in out),
                      ('the account is quoted and every quotation re-read',
                       'EVERY QUOTATION RE-READ AT ITS OWN LINE' in out),
                      ('the count was re-measured under three readings',
                       'RE-MEASURED UNDER THREE READINGS' in out),
                      ('the conclusion survives the most generous reading',
                       'SURVIVES' in out and 'MOST GENEROUS' in out),
                      ('the obligations are priced and none ordered',
                       'A PRICE IS NOT A PROPOSAL' in out),
                      ('the unpriced part is named unpriced',
                       'NAMED UNPRICED' in out),
                      ('two failed features are evidence and not proof',
                       'TWO FAILED FEATURES ARE EVIDENCE AND NOT PROOF' in out),
                      ('the evidence file was appended and not rewritten',
                       'APPENDED BLOCK AND NOTHING ABOVE IT WAS EDITED' in out),
                      ('the untracked records are named and still untracked',
                       'NAMED AND STILL UNTRACKED' in out),
                      ('the tool-cap contradiction is reported',
                       'CONTRADICTION IS REPORTED RATHER THAN QUIETLY EXCEEDED' in out),
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
    rec('b382 -- THE DESK UNDER (R7), AND THE THREE CLOSING WRITES.')
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
        run_clock.write(D, 'b382_desk_notes', LINES)
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b382_desk_notes', LINES)
        return 1
    g1 = ('THE EVIDENCE SEQUENCE CLOSED' in ROWS[0][0]
          and 'CHECKS WHAT EACH GATE READ' in ROWS[0][1]
          and 'A READER AND NOT A PREDICATE' in ROWS[0][1]
          and 'QUOTED AND NOT SUMMARISED' in ROWS[0][1]
          and 'RE-READ AT ITS OWN LINE NUMBER' in ROWS[0][1]
          and 'RE-MEASURED AND NOT CARRIED' in ROWS[0][1]
          and 'MOST GENEROUS' in ROWS[0][1]
          and 'MUST REST ON' in ROWS[0][1]
          and 'EVIDENCE AND NOT PROOF' in ROWS[0][1]
          and 'PRICED AND NOT ORDERED' in ROWS[0][1]
          and 'NAMED UNPRICED' in ROWS[0][1]
          and 'NOTHING CURRENTLY RESTS ON IT' in ROWS[0][1]
          and 'NOTHING IS CLOSED BY THIS ACT EXCEPT THE SEQUENCE ITSELF' in ROWS[0][1]
          and 'NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN' in ROWS[0][2]
          and 'NO CLASS WAS RULED' in ROWS[0][3]
          and 'REGISTRY.md WAS NOT EDITED' in ROWS[0][3]
          and 'SUPPORTS AND NOT PROVES' in ROWS[0][4]
          and "RECORDED AS THE AUTHOR'S JUDGEMENT" in ROWS[0][4]
          and 'MIS-DESCRIBED ITS TOOL CAP' in ROWS[0][4]
          and 'THE SEQUENCE STOPPED, AND THE EVIDENCE CLOSED' in ROWS[0][5]
          and 'NO NEW TRACKING DOCUMENT WAS CREATED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says the closed sequence, the stamped gate, the author`s reason, the quoted '
        'account, the re-read quotations, the re-measured count, the method conclusion, its limit, '
        'the priced obligations, the unpriced part, the caution, no terminal claimed, no class '
        'ruled, no registry edit, the mis-described cap, and the scope : %s' % g1)
    if not g1:
        run_clock.write(D, 'b382_desk_notes', LINES)
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
            run_clock.write(D, 'b382_desk_notes', LINES)
            return 1
        rownum = start

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE INDEX KEY.')
    rec('-' * 100)
    kok = do_key(rownum)
    rec('')
    rec('-' * 100)
    rec('  ### (5) THE EVIDENCE FILE, FINALISED BY AN APPENDED BLOCK.')
    rec('-' * 100)
    ev_before = io.open(EVID, encoding='utf-8').read()
    EMARK = '### b382 -- THE SEQUENCE IS CLOSED. ### THIS FILE IS COMPLETE AS ITS PRODUCT.'
    if EMARK in ev_before:
        rec('  ### ALREADY FINALISED -- the mark is present. ### NOTHING APPENDED.')
        ev_ok, ev_after = True, ev_before
    else:
        block = ['', '=' * 100, EMARK, '=' * 100,
                 '### **THE SEQUENCE `b375`-`b381` IS CLOSED BY THE AUTHOR`S INSTRUCTION AT `b382`.**',
                 '### The relating-word feature was ### **NOT BUILT**, and the reason is the',
                 '### author`s: ### **IT WOULD NEED A SENTENCE UNDERSTOOD RATHER THAN A STRUCTURE',
                 '### ### MEASURED, WHICH IS A READER AND NOT A PREDICATE.**',
                 '',
                 '### ### **THE CONCLUSION THE EVIDENCE SUPPORTS, ABOUT METHOD AND NOT A CLASS:**',
                 '### ### ### **ROLE IS NOT RECOVERABLE FROM A DOCUMENT`S STRUCTURE, AND IT IS',
                 '### ### ### STATED BY TOO FEW DOCUMENTS TO BE RECOVERABLE FROM THEIR PROSE. ### SO',
                 '### ### ### A CLASS RULING, WHATEVER IT RULES, MUST REST ON DECLARATION RATHER',
                 '### ### ### THAN ON CLASSIFICATION.**',
                 '### ### **AND THE LIMIT IS STATED WITH IT: TWO FAILED FEATURES ARE EVIDENCE AND',
                 '### ### NOT PROOF.** ### A third feature might separate the control.',
                 '',
                 '### **THE COUNT THE SECOND HALF RESTS ON, RE-MEASURED AT `b382` UNDER ALL THREE',
                 '### READINGS THE SEQUENCE PRODUCED:**',
                 '###   b376 strict  : %d of %d state a role'
                 % (AC['population'] - AC['strict_silent'], AC['population']),
                 '###   b376 broad   : %d of %d'
                 % (AC['population'] - AC['broad_silent'], AC['population']),
                 '###   b381 purpose : %d of %d   ### **THE MOST GENEROUS**'
                 % (AC['b381_wide'], AC['b381_scanned']),
                 '### ### **AND ONLY %d DOCUMENTS DECLARE SYNTHESIS**, so the side the rubric turns'
                 % C81['synthesis_n'],
                 '### on is the side the corpus is nearly silent about.',
                 '',
                 '### **WHAT A DECLARATION RULE WOULD OBLIGE, PRICED AND ### NOT ORDERED:**',
                 '###   (i)   one rule document, saying which of the three definitions of',
                 '###         `keystone` a declaration declares against',
                 '###   (ii)  a class line in %d documents that lack one; and separately %d of'
                 % (AC['not_declared_class_line'], AC['strict_silent']),
                 '###         the %d say nothing about their own role, so for most the line'
                 % AC['population'],
                 '###         ### **CANNOT BE WRITTEN FROM THE DOCUMENT`S OWN TEXT.** ### The',
                 '###         overlap of the two is ### **NOT IN THE RECORD AND IS NAMED',
                 '###         ### UNCOUNTED.**',
                 '###   (iii) a phased application : ### **UNPRICED, AND NAMED UNPRICED**',
                 '',
                 '### ### **THE EXEMPLAR CAUTION, CARRIED WITH THE SET:** ### `b381`s gathering',
                 '### exemplars came from a matcher ### **REPAIRED TWICE AFTER ITS OUTPUT WAS',
                 '### ### SEEN** (%d -> %d -> %d of %d heads). ### **IF THAT SET IS EVER REUSED IT'
                 % (EX81['loose_hits'], EX81['loose2_hits'], EX81['wide_hits'], EX81['scanned']),
                 '### ### IS RE-DERIVED AND NOT INHERITED**, and ### **NOTHING CURRENTLY RESTS ON',
                 '### ### IT** -- the branch did not adopt, the corpus was not scored and no prior',
                 '### score was overwritten.',
                 '',
                 '### ### ### **THIS FILE IS COMPLETE AS THIS SEQUENCE`S PRODUCT.** ### It is not',
                 '### an exhaustive account of everything bearing on the ruling; ### **COMPLETE',
                 '### ### MEANS THE SEQUENCE ADDS NOTHING FURTHER TO IT.** ### It remains a relay',
                 '### bank artifact and ### **NOT A TRACKING DOCUMENT IN THE CORPUS.**',
                 '### ### **THE RULING IS THE AUTHOR`S AND NOTHING HERE MAKES IT.**',
                 '=' * 100, '']
        io.open(EVID, 'a', encoding='utf-8', newline=chr(10)).write(chr(10).join(block) + chr(10))
        ev_after = io.open(EVID, encoding='utf-8').read()
        ev_ok = ev_after.startswith(ev_before)
        rec('  ### bytes %d -> %d ; ### **APPEND-ONLY : %s** ; nothing above it edited'
            % (len(ev_before.encode('utf-8')), len(ev_after.encode('utf-8')), ev_ok))
    ev_bad = [i + 1 for i, x in enumerate(ev_after.split(chr(10))) if '%s' in x or '%d' in x]
    rec('  ### unfilled placeholders in the evidence file : %s' % (ev_bad or 'none'))

    rec('')
    rec('-' * 100)
    rec('  ### (6) THE BANK.')
    rec('-' * 100)
    B = []
    BAR, SUB = '=' * 100, '-' * 100
    B.append(BAR)
    B.append('b382 -- THE SEQUENCE STOPPED, AND THE EVIDENCE CLOSED. ### THE BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **THE AUTHOR STOPPED THE SEQUENCE, AND THIS ACT CLOSES THE EVIDENCE')
    B.append('### ### ### WITHOUT RULING.**')
    B.append('### The relating-word feature is ### **NOT BUILT.** ### The reason is recorded as the')
    B.append('### author`s and not as a measurement this seat made: ### **IT WOULD NEED A SENTENCE')
    B.append('### ### UNDERSTOOD RATHER THAN A STRUCTURE MEASURED, WHICH IS A READER AND NOT A')
    B.append('### ### PREDICATE.**')
    B.append('')
    B.append('### ### ### **THE CONCLUSION THE EVIDENCE SUPPORTS, ABOUT METHOD AND NOT A CLASS:')
    B.append('### ### ### ROLE IS NOT RECOVERABLE FROM A DOCUMENT`S STRUCTURE, AND IT IS STATED BY')
    B.append('### ### ### TOO FEW DOCUMENTS TO BE RECOVERABLE FROM THEIR PROSE. ### SO A CLASS')
    B.append('### ### ### RULING MUST REST ON DECLARATION RATHER THAN ON CLASSIFICATION.**')
    B.append('### ### **AND THE LIMIT IS STATED WITH THE CONCLUSION AND NOT BELOW IT: TWO FAILED')
    B.append('### ### FEATURES ARE EVIDENCE AND NOT PROOF.**')
    B.append('')
    B.append(SUB)
    B.append('### THE ACCOUNT, THE CONCLUSION, THE CAUTION AND THE OPEN ITEMS.')
    B.append(SUB)
    B.append('### ### **THE FULL ACCOUNT IS THIS ACT`S RUN RECORD, `data/%s`**, where every claim'
             % AC['run_file'])
    B.append('### about a prior act carries a line from that act`s own bank with its file and its')
    B.append('### line number. ### **QUOTATIONS THAT FAILED TO RE-READ : %d.**'
             % len(AC['reread_failures']))
    B.append('### ### **ACTS ACCOUNTED FOR : %d** ### -- `b375` through `b381`, each with what it'
             % AC['acts_covered'])
    B.append('### asked, what it found and what it left.')
    B.append('')
    B.append('### ### **THE LOAD-BEARING COUNT, RE-MEASURED AND NOT CARRIED:**')
    B.append('###   %-56s %-14s %s' % ('READING', 'STATES A ROLE', 'SAYS NOTHING'))
    B.append('###   %-56s %-14s %d'
             % ('b376 strict', '%d of %d' % (AC['population'] - AC['strict_silent'],
                                             AC['population']), AC['strict_silent']))
    B.append('###   %-56s %-14s %d'
             % ('b376 broad', '%d of %d' % (AC['population'] - AC['broad_silent'],
                                            AC['population']), AC['broad_silent']))
    B.append('###   %-56s %-14s %d'
             % ('b381 purpose statement -- THE MOST GENEROUS',
                '%d of %d' % (AC['b381_wide'], AC['b381_scanned']),
                AC['b381_scanned'] - AC['b381_wide']))
    B.append('### ### **THE CONCLUSION SURVIVES THE MOST GENEROUS READING : %s**, and only `%d`'
             % (AC['generous_minority'], C81['synthesis_n']))
    B.append('### documents declare synthesis at all -- ### **THE SIDE THE RUBRIC TURNS ON IS THE')
    B.append('### ### SIDE THE CORPUS IS NEARLY SILENT ABOUT.**')
    B.append('')
    B.append('### WHAT A DECLARATION RULE WOULD OBLIGE, PRICED AND NOT ORDERED.')
    B.append('### ### ### **A PRICE IS NOT A PROPOSAL.** ### Priced from the record`s own figures,')
    B.append('### and nothing below is ordered, recommended or ranked.')
    B.append('###   ### **(i)** ### one rule document, naming which of the three definitions of')
    B.append('###     `keystone` a declaration declares against. ### **THE PIECE NOTHING ELSE CAN')
    B.append('###     ### PROCEED WITHOUT.**')
    B.append('###   ### **(ii)** ### a class line in ### **`%d` DOCUMENTS THAT LACK ONE**, each a'
             % AC['not_declared_class_line'])
    B.append('###     one-line append. ### And what the line COSTS is not typing: ### **`%d` OF THE'
             % AC['strict_silent'])
    B.append('###     ### `%d` SAY NOTHING ABOUT THEIR OWN ROLE**, so for most documents the line'
             % AC['population'])
    B.append('###     ### **CANNOT BE WRITTEN FROM THE DOCUMENT`S OWN TEXT AND IS A JUDGEMENT --')
    B.append('###     ### THE AUTHOR`S.**')
    B.append('###     ### ### **AND HOW MANY OF THE `%d` ARE ALSO AMONG THE `%d` IS NOT IN THE'
             % (AC['not_declared_class_line'], AC['strict_silent']))
    B.append('###     ### RECORD:** ### the class-line census banked counts and not lists, so the')
    B.append('###     overlap is ### **NAMED UNCOUNTED RATHER THAN ESTIMATED.** ### **TWO FIGURES')
    B.append('###     ### OVER TWO POPULATIONS ARE NOT A SUBSET.**')
    B.append('###   ### **(iii)** ### a phased application : ### **UNPRICED, AND NAMED UNPRICED')
    B.append('###     ### RATHER THAN ESTIMATED.** ### The record counts documents and clusters and')
    B.append('###     ### **DOES NOT COUNT REVIEWER EFFORT OR ELAPSED TIME.** ### `(E2)` MET.')
    B.append('')
    B.append('### ### **THE EXEMPLAR CAUTION.** ### `b381`s gathering set came from a matcher')
    B.append('### ### **REPAIRED TWICE AFTER ITS OUTPUT WAS SEEN** ### -- `%d` then `%d` then `%d`'
             % (EX81['loose_hits'], EX81['loose2_hits'], EX81['wide_hits']))
    B.append('### of `%d` heads, all three printed.' % EX81['scanned'])
    B.append('### ### **IF THAT SET IS EVER REUSED IT IS RE-DERIVED AND NOT INHERITED.**')
    B.append('### ### **AND NOTHING CURRENTLY RESTS ON IT : %s** --'
             % AC['nothing_rests_on_the_set'])
    B.append('### measured against `b381`s own banked JSON rather than repeated from it.')
    B.append('')
    B.append('### ### **THE OPEN ITEMS, RESTATED FOR THE RULING:** ### the four lists, ### **OPEN BY')
    B.append('### ### NAME**; the download-layer book`s registry drift, ### **OPEN AND THE AUTHOR`S**')
    B.append('### under `(R14)`s own words; the ### **`%d` SUBJECT CLUSTERS WITH NO KEYSTONE**, filed'
             % len(NOKEY))
    B.append('### and not opened; and the reconciliation figure, ### **A FLOOR AGAINST THE WIDER')
    B.append('### ### QUESTION** ### and deliberately not re-measured.')
    B.append('### ### ### **NOTHING IS CLOSED BY THIS ACT EXCEPT THE SEQUENCE ITSELF.**')
    B.append('')
    B.append(SUB)
    B.append('### THE DESK, THE WRITES, AND WHAT THIS ACT DID NOT DO.')
    B.append(SUB)
    B.append('### desk items swept : %d ### / ### closed : %d ### / ### standing : %d ### / ### '
             'lists closed : %d' % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
    B.append('### ### **AND THE ONE CLOSURE IS THE SEQUENCE**, closed by the author`s instruction')
    B.append('### and not by this seat`s judgement.')
    B.append('### trail block appended (append-only %s, committed prefix intact %s); '
             '`CORRESPONDENCE.md` row %s;'
             % (tr['appended_only'], tr['committed_prefix_intact'], rownum))
    B.append('### index key `the-sequence-stopped-and-the-evidence-closed` reachable by every alias '
             ': %s' % kok)
    B.append('### the ruling`s evidence file ### **FINALISED BY AN APPENDED BLOCK (append-only %s)**'
             % ev_ok)
    B.append('### and ### **NAMED COMPLETE AS THIS SEQUENCE`S PRODUCT.**')
    B.append('')
    B.append('### ### **THE TEN UNTRACKED RUN RECORDS OF EARLIER ACTS, NAMED AND STILL UNTRACKED:**')
    for u in J('b382_reads')['untracked']:
        B.append('###   `%s`' % u)
    B.append('### ### **`b381` SWEPT THEM IN WITH `git add -A` AND REVERTED THEM.** ### They are not')
    B.append('### this act`s to commit either, and ### **NAMING THEM IS THE WHOLE OF WHAT THIS ACT')
    B.append('### ### DOES ABOUT THEM** -- so a later act does not rediscover them as a defect.')
    B.append('')
    B.append('### ### **AND THIS ACT`S OWN LOCKED FACE MIS-DESCRIBED ITS TOOL CAP.** ### The face')
    B.append('### caps the act at ### **SIX FILES** ### and the clause spec`s description then named')
    B.append('### ### **SEVEN ROLES** ### -- regspec, extract, reg gate, account, desk sweeper, bank')
    B.append('### writer, gate suite. ### **THE CAP IS THE NUMBER AND THE DESCRIPTION WAS THE')
    B.append('### ### ERROR:** ### the desk sweeper and the bank writer are one file and the act')
    B.append('### ships six.')
    B.append('### ### **THE CONTRADICTION IS REPORTED RATHER THAN QUIETLY EXCEEDED**, which is what')
    B.append('### the face`s own opening sentence requires: ### **THE FACE STANDS.**')
    B.append('')
    B.append('### ### **NO CLASS WAS RULED. ### NO DOCUMENT WAS RECLASSIFIED. ### NO DECLARATION WAS')
    B.append('### ### MOVED. ### NO DECLARATION RULE WAS ORDERED. ### NO LIST WAS CLOSED. ### NO')
    B.append('### ### PRIOR SCORE WAS OVERWRITTEN. ### THE REGISTRY WAS NOT EDITED.**')
    B.append('### ### **NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL.** ### Nothing on the download')
    B.append('### layer was touched and the book was not opened. ### No archive file was touched and')
    B.append('### the `86` unconfirmed stay unconfirmed. ### **NO `.lean` FILE TOUCHED, NO BUILD')
    B.append('### ### RUN, NO AXIOM PROFILE RECOMPUTED.**')
    B.append('### **THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED. ### THE POSTURE')
    B.append('### LOCK IS SEPARATE.** ### `h2` stands exactly where the deposit left it and this act')
    B.append('### makes no claim about it in either direction. ### **NOTHING IS DEPOSITED AND')
    B.append('### ### NOTHING WAS WRITTEN AT ZENODO.**')
    B.append('')
    B.append(SUB)
    B.append('### WHAT THIS ACT ADDS TO THE LORE.')
    B.append(SUB)
    B.append('### ### ### **NEW -- `AN ACT THAT CLOSES EVIDENCE MUST STATE THE LIMIT WITH THE')
    B.append('### ### ### CONCLUSION AND NOT BELOW IT`.** ### Two features failed. ### The')
    B.append('### temptation is to write that role is not structurally readable; ### **WHAT THE')
    B.append('### ### EVIDENCE SUPPORTS IS THAT TWO INSTRUMENTS DID NOT READ IT**, and the')
    B.append('### difference belongs in the same sentence as the finding.')
    B.append('### ### ### **NEW -- `A PRICE IS NOT A PROPOSAL`.** ### Pricing what a rule would cost')
    B.append('### is how a seat informs a ruling ### **WITHOUT MAKING IT**, and the part the record')
    B.append('### cannot price is ### **NAMED UNPRICED RATHER THAN ESTIMATED.**')
    B.append('### ### ### **NEW -- `TWO FIGURES OVER TWO POPULATIONS ARE NOT A SUBSET`.** ### This')
    B.append('### act`s first draft of the price wrote ### **`307` DOCUMENTS LACK A CLASS LINE, OF')
    B.append('### ### WHICH `340` CANNOT HAVE ONE WRITTEN FROM THEIR OWN TEXT** -- and `340` is')
    B.append('### larger than `307`, because the two counts are taken over different populations')
    B.append('### and the record banks them as ### **COUNTS AND NOT LISTS**, so their overlap is not')
    B.append('### computable from it. ### **THE CLAIM WAS REPLACED BY TWO SEPARATE FIGURES WITH THE')
    B.append('### ### OVERLAP NAMED UNCOUNTED**, and the row, the key, the trail block and the')
    B.append('### evidence epilogue were each rewritten rather than left carrying it. ### **A NUMBER')
    B.append('### ### THAT CANNOT BE A SUBSET OF THE NUMBER IT IS QUOTED AGAINST IS THE CHEAPEST')
    B.append('### ### ARITHMETIC CHECK THERE IS, AND THIS ACT DID NOT MAKE IT UNTIL A COMMIT')
    B.append('### ### MESSAGE PUT THE TWO SIDE BY SIDE.**')
    B.append('### ### ### **NEW -- `A CAP IS A NUMBER, NOT A LIST`.** ### This act`s own face capped')
    B.append('### it at six files and then described seven roles. ### **THE NUMBER BOUND AND THE')
    B.append('### ### DESCRIPTION WAS THE DEFECT**, reported rather than quietly exceeded.')
    B.append('### **MET AGAIN -- VERIFY EVERY CANDIDATE ANCHOR AGAINST ITS FILE BEFORE WRITING IT**')
    B.append('### (`b313`/`b317`): three of this act`s anchors were typed from the paste`s visual')
    B.append('### wrapping and found nothing; ### **THE TOOL CAUGHT ALL THREE AND ZERO SURVIVED.**')
    B.append('### **MET AGAIN -- STAGE BY AN EXPLICIT FILE LIST, NEVER BY `-A`** (`b381`), and')
    B.append('### ### **A QUOTATION WITH HOLES IN IT IS NOT A QUOTATION** (`b381`).')
    B.append('')
    B.append(SUB)
    B.append('### THE RECORD.')
    B.append(SUB)
    regtxt = io.open(os.path.join(D, 'b382_registration_2026-09-09.txt'), encoding='utf-8').read()
    m_sha = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt)
    m_by = re.search(r'bytes locked : (\d+)', regtxt)
    m_at = re.search(r'locked at \(UTC\) : (\S+)', regtxt)
    B.append('### registration locked at (UTC) %s' % (m_at.group(1) if m_at else '?'))
    B.append('### ### **%s bytes, sha256 `%s`, %d clauses, ### LOCKED BEFORE ANY WRITE AND CHAINED'
             % (m_by.group(1) if m_by else '?', m_sha.group(1) if m_sha else '?',
                len(J('b382_satisfiable')['clauses'])))
    B.append('### ### ON A GATE THAT CHECKS WHAT EACH GATE READ.** ### %d gates read, %d checked by '
             'digest.' % (LG['gates_read'], LG['face_subject_gates']))
    for n in ('b382_reads', 'b382_lockgate', 'b382_account'):
        j = J(n)
        B.append('### %-16s run file `%s` recorded clock %s' % (n, j['run_file'], j.get('run_clock')))
    B.append('### %-16s run file `%s`' % ('b382_desk_bank', os.path.basename('PENDING')))
    B.append('### **THE REFS THIS ACT READ IN THE ROSTERED REPOSITORIES:**')
    for k, v in J('b382_reads')['refs'].items():
        B.append('###   %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    B.append('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor, `%d` anchors differing '
             'from the hint' % (J('b382_reads')['reads'], J('b382_reads')['without_anchor'],
                                J('b382_reads')['anchors_differing']))
    B.append('### that found them. ### **EVERY ANCHOR WAS READ FROM ITS FILE AND NONE WAS TYPED.**')
    B.append('### ### **SIX NEW `relay` TOOLS AGAINST A CAP OF SIX, AND NO SHARED UTILITY:** ### this')
    B.append('### act ### **ASSEMBLES AND CONCLUDES RATHER THAN MEASURING**, and needed no new')
    B.append('### instrument. ### **A SHARED UTILITY WITH NO SECOND CALLER IS A FILE, NOT A')
    B.append('### ### UTILITY.**')
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
    p = run_clock.write(D, 'b382_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             evidence_appended=ev_ok, evidence_placeholders=len(ev_bad),
             bank='b382_the_sequence_stopped.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b382_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and ev_ok and not ev_bad and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
