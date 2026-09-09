# -*- coding: utf-8 -*-
"""b385_desk_bank.py -- THE DESK UNDER `(R7)`, THE THREE CLOSING WRITES, AND THE BANK.

### ### **THE DESK CLOSES FOUR ITEMS THIS TIME, AND ONE OF THE FOUR IT DID NOT DO.** ### `(R7)`
### closes an item whose OCCASION is gone -- and the occasion of the faces-ledger item went at
### ### **`b360`, TWENTY-FIVE ACTS AGO.** ### The desk carried it because the item ### **CARRIED
### ### NO DATE**, which is exactly the species `DESK_FRESHNESS` was minted at `b368` to catch.
### ### ### **SO THE CLOSURE IS FILED `ALREADY DONE BY THE RECORD` AND NOT CLAIMED BY THIS ACT**,
### and the twenty-five acts are printed rather than quietly dropped.
###
### ### **AND ONE CLOSURE IS A REFUTATION OF A PRIOR ACT`S REPORTED ABSENCE.** ### `b383` said the
### reservoir rule was NOT LOCATED, on a controlled sweep whose positive control fired. ### It was
### wrong, and ### **THE REASON IS THE FINDING**: it searched for the navigator`s NAME for the
### rule and the rule uses none of those words. ### **A CONTROLLED SEARCH FOR THE WRONG STRING IS
### ### STILL A CONTROLLED SEARCH FOR THE WRONG STRING.**
###
### ### **THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME**, and a bar measures it.
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
MARK = '<!-- b385 the six on the trails; the rule found; the three done -->'
PRIOR = '<!-- b384 the fold, b371 through b383 -->'
ACT = 'b385'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


AC = J('b385_components')
LG = J('b385_lockgate')
E = J('b385_reads')
CL375 = J('b375_clusters')
NOKEY = CL375['subject_clusters_without_keystone']
BANKOUT = os.path.join(D, 'b385_the_six_on_the_trails.txt')

# ### THE RULE, WHERE THE EXTRACT LOCATED IT. ### Read out of the extract`s own probe record rather
# ### than typed, so the location in the desk and the bank is the located one and not a remembered one.
RULE_FILE = AC['rule_file']
RULE_LINE = E['probe_hits']['SESSION PROTOCOL'][0][1]

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
     'STILL THE AUTHOR`S, and ### **THE STANDING STANDARD ALREADY RULES IT** ### as b383 read it'),
    ("the census's definition-versus-operation drift", 'STAND', None, None,
     'FILED at b377 and ### **NOT REPAIRED**'),
    ('the four amendments b383 drafted', 'STAND', None, None,
     '### **ROUTED AND UNAPPLIED.** ### And ### **`(iv)` IS NOW ANSWERABLE WITHOUT A RULING**: '
     'the rule it asked the author to supply ### **HAS BEEN LOCATED IN THE RECORD** ### by this '
     'act, so the request is superseded by a finding rather than by an amendment'),
    ('the citation question -- what a finished keystone is cited as', 'STAND', None, None,
     'NEW at b385 and ### **ROUTED, NOT ANSWERED.** ### `%d` options from the standard`s own '
     'practice, ### **`%d` RECOMMENDED**, and the failure the tiers exist to prevent quoted '
     'beside them' % (AC['options'], AC['options_recommended'])),
    ('the download-layer book`s registry drift', 'STAND', None, None,
     'OPEN AND ### **THE AUTHOR`S**, in `(R14)`s own words'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', None, None,
     'CARRIED and ### **DELIBERATELY NOT RE-MEASURED**'),
    ('the ten untracked run records of earlier acts', 'STAND', None, None,
     'NAMED at b382 and ### **STILL UNTRACKED.** ### Not this act`s to commit either'),

    # ---- WHAT THIS ACT ADDS ---------------------------------------------------------------------
    ('the subject clusters with registry rows and no keystone', 'STAND', None, None,
     '### **`%d`, NOW ENTERED ON THE TRAILS LEDGER AS `NOT-YET-SYNTHESIZED`** -- one entry each, '
     'the many-to-many rule stated beside every one, and ### **NOT OWED AND NOT DEFICIENT.** ### '
     '`%d` were opened, ranked or prioritised. ### The item stays STANDING because ### **AN ENTRY '
     'ON A TRAIL IS NOT A SYNTHESIS**' % (AC['entries_written'], AC['clusters_opened'])),
    ('the navigator`s paraphrase of the reservoir rule, scored', 'STAND', None, None,
     'NEW at b385: `%d` clauses, ### **`%d` ACCURATE AND `%d` OVER-STATED.** ### The '
     'over-statement is exact -- the rule makes ### **THE MANIFEST`S `md5` + `last-commit` '
     'COLUMNS** ### the authority and the Currency check widens it to three fields, but neither '
     'place makes the whole manifest the authority'
     % (AC['clauses_scored'], AC['accurate'], AC['over_stated'])),
    ('and the rule has no name in the record', 'STAND', None, None,
     'NEW at b385: the corpus calls it a ### **SESSION PROTOCOL** ### and a ### **STANDING '
     'RULE**, never a reviewer-reservoir rule. ### **A NAME THAT IS NOT IN THE RECORD IS NOT AN '
     'ERROR IN THE RULE** -- it is a name, and searching for it is what cost b383 an act'),

    # ---- WHAT THIS ACT CLOSES -------------------------------------------------------------------
    ('and b383`s absence claim about the reservoir rule', 'CLOSE', 'b385_components_notes',
     "AND `b383`S ABSENCE CLAIM IS REFUTED BY THIS ACT, SAID FIRST RATHER THAN FOLDED INTO A "
     "RESULT.",
     'CLOSED at b385 by ### **REFUTATION.** ### The rule IS in `%s` at line `%d`, under a heading '
     'the corpus calls a SESSION PROTOCOL and a STANDING RULE. ### `b383` searched for ### **THE '
     'NAVIGATOR`S NAME FOR THE RULE** ### and the rule uses none of those words -- its control '
     'fired, its sweep was honest, and ### **A CONTROLLED SEARCH FOR THE WRONG STRING IS STILL A '
     'CONTROLLED SEARCH FOR THE WRONG STRING**' % (RULE_FILE, RULE_LINE)),
    ("the guard's own stale install line", 'CLOSE', 'b385_components_notes',
     'AND THE GUARD`S BEHAVIOUR IS NOT CHANGED : True',
     'CLOSED at b385: the tracked guard documented `cp ... .git/hooks/pre-push` while ### **EVERY '
     'ROSTERED REPOSITORY RUNS `core.hooksPath = .githooks`.** ### Repaired under `(R4)` -- the '
     'stale line quoted in the bank from the PRE-REPAIR file, the file`s line then corrected -- '
     'and ### **THE GUARD`S BEHAVIOUR IS NOT CHANGED : %s.** ### Only the comment moved'
     % AC['guard_behaviour_unchanged']),
    ('the 86 archive files the mirror does not carry', 'CLOSE', 'b385_components_notes',
     'NOTHING WAS REMOVED, MOVED OR RENAMED. ### THE REMOVAL IS THE AUTHOR`S.',
     'CLOSED at b385 ### **WITH ITS EXCEPTION REPORTED**: `%d` `.md` files under `archive/` '
     'confirmed ### **BY DIGEST AGAINST THEIR OWN GIT BLOBS (`%d` of `%d`) AND BY CONTENT (`%d` '
     'of `%d`)**, the one content exception named by path. ### The filename comparison was '
     'computed and ### **PRINTED UNUSED** -- no verdict depends on it. ### **`%d` REMOVED, MOVED '
     'OR RENAMED**; the removal is the author`s'
     % (AC['archive_files'], AC['archive_digest_ok'], AC['archive_files'],
        AC['archive_content_ok'], AC['archive_files'], AC['archive_removed'])),
    ('the faces ledger`s absence from the mirror roster', 'CLOSE', 'b385_components_notes',
     'DISPOSITION : ALREADY DONE BY THE RECORD.',
     'CLOSED at b385 and ### **NOT BY THIS ACT.** ### `b359` filed the absence; ### **`b360` '
     'ADDED IT WHEN IT EXECUTED THE AUTHOR`S ROSTER RULING**, and the desk then carried the item '
     'for ### **TWENTY-FIVE ACTS AFTER IT WAS DONE.** ### That is `DESK_FRESHNESS` biting the '
     'desk one act after the fold that recorded it. ### **THE ROSTER WAS NOT EDITED : %s**'
     % (not AC['roster_edited'])),
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
        if len(why) > 340:
            rec('              %s' % why[340:540])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    stands = [m for m in marks if m['disposition'] == 'STAND']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d. ### CLOSURES '
        'REFUSED FOR WANT OF A KILLING SENTENCE : %d.**'
        % (len(marks), len(closed), len(stands), refused))
    rec('    ### ### ### **AND ONE OF THE FOUR CLOSURES WAS NOT DONE BY THIS ACT.** ### The')
    rec('    ### faces-ledger item was ### **ALREADY DONE BY THE RECORD AT `b360`** ### and')
    rec('    ### carried for ### **TWENTY-FIVE ACTS** ### because the item carried no date.')
    rec('    ### ### **A DESK ITEM WITHOUT A DATE IS AN ITEM NOBODY HAS RE-READ**, which is')
    rec('    ### ### `DESK_FRESHNESS` (`b368`) biting the desk one act after the fold that')
    rec('    ### ### recorded it.')
    rec('    ### ### ### **AND ONE CLOSURE IS A REFUTATION OF A PRIOR ACT`S REPORTED ABSENCE**,')
    rec('    ### ### ### which is closed by finding the thing and not by giving up on it.')
    rec('    ### ### **THE CLUSTER ITEM IS NOT CLOSED BY BEING ENTERED ON A TRAIL. ### AN ENTRY')
    rec('    ### ### IS NOT A SYNTHESIS**, and the occasion of the item is the synthesis.')
    return dict(items=len(marks), closed=len(closed), standing=len(stands),
                closures_refused=refused, marks=marks,
                closed_items=[dict(item=m['item'], file='data/%s' % m.get('killing_file'),
                                   date=m.get('date'), own_act=m.get('own_act')) for m in closed])


def entry_paras():
    """### THE SIX TRAIL ENTRIES, ONE PARAGRAPH EACH, ### **BUILT FROM THE COMPONENT RECORD AND
    ### NOT RETYPED.** ### The many-to-many rule is appended to EVERY one of them by construction,
    ### so a later reader cannot meet an entry without it."""
    out = []
    for e in AC['entries']:
        out.append(
            '**`%s` — NOT-YET-SYNTHESIZED.** *Where its material sits:* %s. *What a '
            'synthesis would draw on:* %s. *What would make it ripe:* %s. **The rule, beside the '
            'entry: a cluster may have SEVERAL keystones, ONE, or NONE YET; the relation is '
            'many-to-many and it changes over time — so this cluster is NOT-YET-SYNTHESIZED, '
            '_not owed and not deficient_.**'
            % (e['cluster'], e['where'], e['draws'],
               re.sub(r'#{2,}', '', e['ripe']).replace('  ', ' ').strip()))
        out.append('')
    return out


def trail_block(Q):
    return [
        '', MARK, '',
        '### **b385 — THE SIX ON THE TRAILS, THE RULE FOUND, AND THE THREE THAT WAITED ON '
        'NOTHING (2026-09-09)**',
        '',
        ('*No block above is edited. The b384 block (`%s`) and every block before it stand exactly '
         'as they were written.*' % PRIOR),
        '',
        ('**THE %d SUBJECT CLUSTERS WITH NO KEYSTONE ARE ENTERED HERE, ONE ENTRY EACH, AS '
         '`NOT-YET-SYNTHESIZED`.** The author’s ruling is that a recognized cluster needing a '
         'synthesis belongs on the standing to-do system and is referred to when ripe — so '
         'these are **trail entries and nothing is opened**: **%d clusters were opened, ranked or '
         'prioritised**, no document was read for content beyond its registry row, and **no '
         'synthesis was begun**. The many-to-many rule stands beside every entry, so **a plurality '
         'is never read as an anomaly and an absence is never read as a defect**.'
         % (AC['entries_written'], AC['clusters_opened'])),
        '',
    ] + entry_paras() + [
        ('**AND THE REVIEWER-RESERVOIR RULE IS LOCATED — WHICH REFUTES b383’S ABSENCE '
         'CLAIM, AND THAT IS SAID FIRST RATHER THAN FOLDED INTO A RESULT.** It sits in `%s` at line '
         '`%d`, under **`## SESSION PROTOCOL — reviewer mirror-refresh (standing rule, '
         '2026-07-29)`**: *Any session in which the chat reviewer reasons about paper **content** '
         'begins with a fresh mirror-refresh export*, with a **Procedure** naming the reviewer set '
         'and the `MANIFEST.md` columns, a **Why this is a hard rule, not a nicety** citing **two '
         'recorded errors**, and a **Currency check** in which *the MANIFEST wins and the claim is '
         'stale*. b383’s sweep was honest and its positive control fired; **it searched for '
         'the navigator’s NAME for the rule** — `reservoir`, `reviewer pool`, `reviewer '
         'budget` — **and the rule uses none of those words**. **A controlled search for the '
         'wrong string is still a controlled search for the wrong string**, and a positive control '
         'proves the matcher works, not that the term is the right one. **Amendment (iv) is '
         'therefore answered by a finding and not by a ruling.**' % (RULE_FILE, RULE_LINE)),
        '',
        ('**THE NAVIGATOR’S PARAPHRASE IS SCORED CLAUSE BY CLAUSE: %d CLAUSES, %d ACCURATE, %d '
         'OVER-STATED.** Accurate: *a session reasoning about paper content begins with a fresh '
         'mirror-refresh export* (the rule’s subject is narrower — **the chat reviewer** '
         '— and a narrowing in the rule is not an over-statement in the paraphrase); and *with '
         'two recorded errors cited as its occasion* (the rule cites **exactly two**, and the count '
         'and the framing are its own). **Over-stated: *the export’s manifest is the '
         'reviewer’s authority over recall*.** The rule makes the **MANIFEST’s `md5` + '
         '`last-commit` columns** the authority, and the Currency check widens the disagreement test '
         'to three fields — **but neither place makes the whole manifest the authority**. '
         '**And the name is not in the record**: the corpus calls this a *SESSION PROTOCOL* and a '
         '*standing rule*, never a reviewer-reservoir rule. **A name that is not in the record is '
         'not an error in the rule.**'
         % (AC['clauses_scored'], AC['accurate'], AC['over_stated'])),
        '',
        ('**THE THREE THAT WAITED ON NOTHING ARE EACH DONE OR ROUTED, NONE PARTLY.** *(a) The '
         'guard’s stale install line — **DONE**.* The tracked guard documented `cp ... '
         '.git/hooks/pre-push` while every rostered repository runs `core.hooksPath = .githooks`; '
         'repaired under **(R4): preserve by quotation, repair by edit**, the stale line quoted from '
         'the pre-repair file and the file’s line then corrected, and **the guard’s '
         'behaviour is not changed — only the comment moved**. *(b) The archive files — '
         '**DONE WITH EXCEPTIONS REPORTED**.* **%d `.md` files under `archive/` confirmed by digest '
         'against their own git blobs (%d of %d) and by content (%d of %d)**, the one content '
         'exception named by path; **the filename comparison was computed and printed unused**, so '
         'no verdict depends on it; and **%d were removed, moved or renamed — the removal is '
         'the author’s**. *(c) The faces ledger — **ALREADY DONE BY THE RECORD**.* b359 '
         'filed the absence and **b360 added it when it executed the author’s roster ruling**; '
         '**the desk carried the item for twenty-five acts after it was done**, and **the roster was '
         'not edited by this act**.'
         % (AC['archive_files'], AC['archive_digest_ok'], AC['archive_files'],
            AC['archive_content_ok'], AC['archive_files'], AC['archive_removed'])),
        '',
        ('**THE CITATION QUESTION IS STATED FOR THE AUTHOR AND NOT ANSWERED.** b383 found that a '
         'document carrying both tiers has no citation rule, and that the standard disposes of mixed '
         'documents by **ruling one tier and reading the parts apart**. **%d options are put, all '
         'three drawn from the standard’s own ruled borderlines and this seat supplies no '
         'fourth**: the `CATALOGOS` pattern (rule it Tier C, read the pinned rows as K — which '
         'obliges row-by-row citation and a document that marks which is which); the `UNIVERSALITY` '
         'pattern (rule it Tier K with a C-scope note — which moves the burden onto the '
         'synthesis sentences); and the `THE_SUBSTRATE` pattern (rule it Tier K, the other material '
         'read as context — which requires the synthesis to assert nothing the document would '
         'be cited for). The failure the tiers exist to prevent is quoted beside them: the June 2026 '
         'formation-universality over-claim, where **a Tier-C synthesis panel was read as a '
         'certification**. **No option is recommended, ranked or called likeliest: %d of the %d. '
         'The question is the author’s.**'
         % (AC['options'], AC['options_recommended'], AC['options'])),
        '',
        ('**WHAT THIS ACT DID NOT DO.** **No class ruled, no document reclassified, no declaration '
         'moved, no grade moved, no act re-verdicted, no list closed.** **No standard edited** and '
         '**no amendment applied** — the four b383 drafted stay routed. **No corpus document '
         'was written into except this ledger**, which is appended to and never edited; `REGISTRY.md` '
         'was **read and not touched**. **No archive file was removed, moved or renamed** and **no '
         'cluster was opened**; **the mirror roster was not edited**. The one repair this act made is '
         '`.githooks/pre-push` line 10 under (R4), **a comment and not behaviour**. No `.lean` file '
         'touched, no build run, no axiom profile recomputed. **The four open lists are restated OPEN '
         'by name.** h2 stands exactly where the deposit left it and this act makes no claim about it '
         'in either direction.'),
        '',
    ]


SCOPE = (
    "**SCOPE: THE SIX ENTERED ON THE TRAILS, THE RULE FOUND, AND THE THREE DISPATCHED.** NO class "
    "ruled, NO document reclassified, NO declaration moved, NO grade moved, NO act re-verdicted, NO "
    "list closed. **NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED** -- the four b383 drafted "
    "stay ROUTED AND UNAPPLIED. **REGISTRY.md WAS READ AND NOT TOUCHED**, and no corpus document "
    "was written into except OPEN_TRAILS.md, which was APPENDED TO AND NEVER EDITED. **THE SIX "
    "CLUSTERS ARE TRAIL ENTRIES AND NOTHING WAS OPENED, RANKED OR PRIORITISED**; no document was "
    "read for content beyond its registry row and NO SYNTHESIS WAS BEGUN. **THE MANY-TO-MANY RULE "
    "IS STATED BESIDE EVERY ENTRY**, so a plurality is never read as an anomaly and an absence is "
    "never read as a defect, and a cluster with no keystone is NOT-YET-SYNTHESIZED rather than owed "
    "or deficient. **THE RULE WAS LOCATED AND QUOTED WHOLE WITH ITS LOCATION, AND THE PARAPHRASE "
    "WAS SCORED AGAINST IT CLAUSE BY CLAUSE** with the over-statement named exactly; the paraphrase "
    "was NOT adopted as the rule's text. **b383's ABSENCE CLAIM IS REFUTED AND THE REFUTATION IS "
    "SAID FIRST**, not folded into a result. **EVERY ABSENCE CLAIM CARRIES A POSITIVE CONTROL THAT "
    "FINDS A KNOWN PRESENCE FIRST.** **EVERY QUOTED LINE WAS RE-READ OUT OF ITS OWN FILE AT ITS OWN "
    "LINE NUMBER**, and the ONE line this act itself repaired under (R4) is reported in its own "
    "line rather than counted as a failed re-read. **THE GUARD'S BEHAVIOUR IS NOT CHANGED -- ONLY "
    "A COMMENT MOVED.** **NO ARCHIVE FILE WAS REMOVED, MOVED OR RENAMED**, the confirmation was BY "
    "DIGEST AND BY CONTENT AND NEVER BY FILENAME, and the filename comparison was computed and "
    "PRINTED UNUSED. **THE MIRROR ROSTER WAS NOT EDITED** and the faces-ledger item was ALREADY "
    "DONE BY THE RECORD AT b360. **NO OPTION IS RECOMMENDED, RANKED OR PREFERRED** and the citation "
    "question remains the author's. **THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME.** **NO NEW "
    "TRACKING DOCUMENT WAS CREATED IN THE CORPUS.** NO .lean FILE TOUCHED, NO BUILD RUN, NO AXIOM "
    "PROFILE RECOMPUTED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS "
    "COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or the roster; NO CLASS "
    "IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS "
    "UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The "
    "seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's "
    "report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE WAVE STAYS "
    "PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it and this act "
    "makes no claim about it in either direction. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT "
    "ZENODO.")


def corr_rows(Q):
    m = ("**THE REVIEWER-RESERVOIR RULE IS LOCATED IN THE REGISTRY'S SESSION-PROTOCOL SECTION AND "
         "b383'S ABSENCE CLAIM IS REFUTED; THE SIX NOT-YET-SYNTHESIZED CLUSTERS ARE ENTERED ON THE "
         "TRAILS** (b385, the six on the trails, the rule found, the three that waited on nothing)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b385, %d gates read and %d checked "
            "by digest. THE RULE IS IN %s AT LINE %d under ## SESSION PROTOCOL -- reviewer "
            "mirror-refresh (standing rule, 2026-07-29), QUOTED WHOLE WITH ITS LOCATION. b383 "
            "REPORTED IT NOT LOCATED AND WAS WRONG, AND THE REASON IS THE FINDING: IT SEARCHED FOR "
            "THE NAVIGATOR'S NAME FOR THE RULE -- reservoir, reviewer pool, reviewer budget -- AND "
            "THE RULE USES NONE OF THOSE WORDS. Its control fired and its sweep was honest, so A "
            "CONTROLLED SEARCH FOR THE WRONG STRING IS STILL A CONTROLLED SEARCH FOR THE WRONG "
            "STRING, and a positive control proves the matcher works and NOT THAT THE TERM IS THE "
            "RIGHT ONE. THE NAVIGATOR'S PARAPHRASE WAS SCORED CLAUSE BY CLAUSE: %d CLAUSES, %d "
            "ACCURATE, %d OVER-STATED -- the over-statement exact, since the rule makes THE "
            "MANIFEST'S md5 AND last-commit COLUMNS the authority and the Currency check widens the "
            "disagreement test to three fields, but NEITHER PLACE MAKES THE WHOLE MANIFEST THE "
            "AUTHORITY. AND THE NAME IS NOT IN THE RECORD: the corpus calls it a SESSION PROTOCOL "
            "and a standing rule. THE %d SUBJECT CLUSTERS WITH NO KEYSTONE ARE ENTERED ON THE "
            "TRAILS LEDGER AS NOT-YET-SYNTHESIZED, one entry each with where its material sits, "
            "what a synthesis would draw on and what would make it ripe, and THE MANY-TO-MANY RULE "
            "STATED BESIDE EVERY ONE so a plurality is never an anomaly and an absence is never a "
            "defect; %d CLUSTERS WERE OPENED, RANKED OR PRIORITISED and NO SYNTHESIS WAS BEGUN. THE "
            "THREE THAT WAITED ON NOTHING ARE EACH DONE OR ROUTED AND NONE PARTLY: the guard's "
            "stale install line REPAIRED UNDER (R4) with THE GUARD'S BEHAVIOUR NOT CHANGED; the "
            "archive files CONFIRMED BY DIGEST AGAINST THEIR GIT BLOBS (%d of %d) AND BY CONTENT "
            "(%d of %d) AND NEVER BY FILENAME, the filename comparison COMPUTED AND PRINTED UNUSED, "
            "with %d REMOVED, MOVED OR RENAMED; and the faces ledger ALREADY DONE BY THE RECORD AT "
            "b360, WHICH THE DESK CARRIED FOR TWENTY-FIVE ACTS AFTER IT WAS DONE BECAUSE THE ITEM "
            "CARRIED NO DATE. THE CITATION QUESTION IS ROUTED AND NOT ANSWERED at %d options from "
            "the standard's own ruled borderlines with %d RECOMMENDED"
            % (LG['gates_read'], LG['face_subject_gates'], RULE_FILE, RULE_LINE,
               AC['clauses_scored'], AC['accurate'], AC['over_stated'],
               AC['entries_written'], AC['clusters_opened'],
               AC['archive_digest_ok'], AC['archive_files'],
               AC['archive_content_ok'], AC['archive_files'], AC['archive_removed'],
               AC['options'], AC['options_recommended']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN AND NO ROW WAS WRITTEN INTO ANY "
            "CORPUS DOCUMENT. ### A standing rule was READ AT CONTENT and quoted whole, every "
            "quotation re-read out of its own file at its own line number, and THE ONE LINE THIS "
            "ACT ITSELF REPAIRED UNDER (R4) IS REPORTED IN ITS OWN LINE RATHER THAN COUNTED AS A "
            "FAILED RE-READ, because a line quoted and then repaired CANNOT RE-READ BY "
            "CONSTRUCTION. ### NO STATEMENT WAS PROVED, NO BUILD WAS RUN AND NO AXIOM PROFILE WAS "
            "RECOMPUTED. ### FINDING A RULE IS NOT RULING ONE, AND ENTERING A CLUSTER ON A TRAIL "
            "IS NOT SYNTHESIZING IT")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT THE "
            "OBJECT. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED, NO "
            "GRADE MOVED, NO ACT RE-VERDICTED AND NO LIST CLOSED. ### NO STANDARD WAS EDITED, NO "
            "AMENDMENT WAS APPLIED, AND REGISTRY.md WAS READ AND NOT TOUCHED. ### NO ARCHIVE FILE "
            "WAS REMOVED, MOVED OR RENAMED AND THE MIRROR ROSTER WAS NOT EDITED")
    grade = ("### LOCATED-AND-SCORED, AND THE REFUTATION IS SAID FIRST. ### b383's REPORTED ABSENCE "
             "IS REFUTED BY THIS ACT AND THE CORRECTION LEADS THE RECORD RATHER THAN BEING FOLDED "
             "INTO A RESULT. ### THE PARAPHRASE WAS SCORED AGAINST THE RULE'S OWN WORDS AND NOT "
             "ADOPTED AS THE RULE'S TEXT, AND THE OVER-STATEMENT IS NAMED EXACTLY RATHER THAN "
             "GENERALLY. ### A CONTROLLED SEARCH FOR THE WRONG STRING IS STILL A CONTROLLED SEARCH "
             "FOR THE WRONG STRING. ### ONE CLOSURE WAS ALREADY DONE BY THE RECORD AND IS NOT "
             "CLAIMED BY THIS ACT. ### NOTHING IS RECOMMENDED AND THE CITATION QUESTION REMAINS THE "
             "AUTHOR'S")
    status = ("data/b385_the_six_on_the_trails.txt; data/%s; data/%s; "
              "data/b385_registration_2026-09-09.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b385); tools/b385_extract.py; "
              "tools/b385_components.py; tools/b385_desk_bank.py; tools/b385_checks.py; "
              "PLACE-papers OPEN_TRAILS.md (an append-only block; NO OTHER CORPUS DOCUMENT WRITTEN "
              "INTO, NO STANDARD EDITED AND REGISTRY.md NOT TOUCHED); relay .githooks/pre-push "
              "(one comment line repaired under (R4), behaviour unchanged); CORRESPONDENCE.md row "
              "%%d" % (AC['run_file'], E['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the reviewer reservoir rule located', 'the mirror-refresh session protocol',
           'the six not-yet-synthesized clusters', 'the paraphrase scored clause by clause',
           'the three that waited on nothing')
MUST_NOT_HIT = ('the rule is not located', 'a cluster is owed a keystone',
                'the citation question is answered', 'an archive file was removed')


def do_key(rownum):
    KEY = 'the-reservoir-rule-located-and-the-six-on-the-trails'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "THE REVIEWER-RESERVOIR RULE IS LOCATED IN %s AT LINE %d, under ## SESSION PROTOCOL -- "
        "reviewer mirror-refresh (standing rule, 2026-07-29), and b383'S ABSENCE CLAIM IS REFUTED. "
        "b383 SEARCHED FOR THE NAVIGATOR'S NAME FOR THE RULE -- reservoir, reviewer pool, reviewer "
        "budget -- AND THE RULE USES NONE OF THOSE WORDS; its control fired and its sweep was "
        "honest, so A CONTROLLED SEARCH FOR THE WRONG STRING IS STILL A CONTROLLED SEARCH FOR THE "
        "WRONG STRING. THE NAVIGATOR'S PARAPHRASE WAS SCORED CLAUSE BY CLAUSE: %d CLAUSES, %d "
        "ACCURATE, %d OVER-STATED -- the rule makes THE MANIFEST'S md5 AND last-commit COLUMNS the "
        "authority and the Currency check widens the disagreement test to three fields, but NEITHER "
        "PLACE MAKES THE WHOLE MANIFEST THE AUTHORITY. AND THE NAME IS NOT IN THE RECORD: the "
        "corpus calls it a SESSION PROTOCOL and a standing rule, and A NAME THAT IS NOT IN THE "
        "RECORD IS NOT AN ERROR IN THE RULE. THE %d SUBJECT CLUSTERS WITH NO KEYSTONE ARE ENTERED "
        "ON THE TRAILS LEDGER AS NOT-YET-SYNTHESIZED, NOT OWED AND NOT DEFICIENT, one entry each "
        "with the many-to-many rule stated beside every one, and %d WERE OPENED, RANKED OR "
        "PRIORITISED. THE THREE THAT WAITED ON NOTHING ARE EACH DONE OR ROUTED AND NONE PARTLY: the "
        "guard's install line REPAIRED UNDER (R4) WITH ITS BEHAVIOUR UNCHANGED; %d archive files "
        "CONFIRMED BY DIGEST AND BY CONTENT AND NEVER BY FILENAME with %d REMOVED, MOVED OR "
        "RENAMED; and the faces ledger ALREADY DONE BY THE RECORD AT b360, CARRIED ON THE DESK FOR "
        "TWENTY-FIVE ACTS AFTER IT WAS DONE. THE CITATION QUESTION IS ROUTED AND NOT ANSWERED."
        % (RULE_FILE, RULE_LINE, AC['clauses_scored'], AC['accurate'], AC['over_stated'],
           AC['entries_written'], AC['clusters_opened'], AC['archive_files'],
           AC['archive_removed']))
    grade = (
        "### NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED -- the four b383 drafted stay "
        "ROUTED AND UNAPPLIED. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION "
        "MOVED, NO GRADE MOVED, NO ACT RE-VERDICTED AND NO LIST CLOSED. ### REGISTRY.md WAS READ "
        "AND NOT TOUCHED AND NO CORPUS DOCUMENT WAS WRITTEN INTO EXCEPT AN APPEND-ONLY TRAIL BLOCK. "
        "### EVERY QUOTED LINE RE-READ AT ITS OWN LINE NUMBER, AND THE ONE LINE THIS ACT REPAIRED "
        "UNDER (R4) IS REPORTED IN ITS OWN LINE RATHER THAN COUNTED AS A FAILED RE-READ. ### THE "
        "PARAPHRASE WAS SCORED AGAINST THE RULE AND NOT ADOPTED AS ITS TEXT. ### EVERY ABSENCE "
        "CLAIM CARRIES A POSITIVE CONTROL. ### NOTHING WAS OPENED, RANKED OR PRIORITISED AND NO "
        "SYNTHESIS WAS BEGUN. ### THE GUARD'S BEHAVIOUR IS NOT CHANGED -- ONLY A COMMENT MOVED. ### "
        "NO ARCHIVE FILE WAS REMOVED, MOVED OR RENAMED AND THE MIRROR ROSTER WAS NOT EDITED. ### "
        "NOTHING IS RECOMMENDED AND THE CITATION QUESTION REMAINS THE AUTHOR'S. ### THE FOUR OPEN "
        "LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. "
        "### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 "
        "UNCHANGED")
    where = (
        "data/b385_the_six_on_the_trails.txt; data/%s; data/%s; "
        "data/b385_registration_2026-09-09.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b385 -- %d gates read, %d checked by digest); "
        "tools/b385_extract.py; tools/b385_components.py; tools/b385_desk_bank.py; "
        "tools/b385_checks.py; PLACE-papers OPEN_TRAILS.md (append-only); relay "
        ".githooks/pre-push (one comment line under (R4)); CORRESPONDENCE.md row %d"
        % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b385 (the six not-yet-synthesized clusters entered on the trails; the reviewer-reservoir "
           "rule located and b383's absence claim refuted; the three that waited on nothing "
           "dispatched; the citation question routed)")
    row_new = ('    # ### THE RULE LOCATED, THE SIX ON THE TRAILS (b385).%s'
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
        rec('    %-44s reaches the b385 key : %s' % (q, g))
    for lbl, cond in (('the rule is located with its file and line',
                       ('LOCATED IN %s AT LINE %d' % (RULE_FILE, RULE_LINE)) in out),
                      ("b383's absence claim is refuted",
                       "b383'S ABSENCE CLAIM IS REFUTED" in out),
                      ('the wrong-string species is banked',
                       'A CONTROLLED SEARCH FOR THE WRONG STRING IS STILL A CONTROLLED SEARCH FOR '
                       'THE WRONG STRING' in out),
                      ('the paraphrase is scored and not adopted',
                       'SCORED AGAINST THE RULE AND NOT ADOPTED AS ITS TEXT' in out),
                      ('the over-statement is named exactly',
                       'NEITHER PLACE MAKES THE WHOLE MANIFEST THE AUTHORITY' in out),
                      ('the name is not in the record',
                       'A NAME THAT IS NOT IN THE RECORD IS NOT AN ERROR IN THE RULE' in out),
                      ('the clusters are not-yet-synthesized',
                       'NOT-YET-SYNTHESIZED, NOT OWED AND NOT DEFICIENT' in out),
                      ('nothing was opened, ranked or prioritised',
                       'NOTHING WAS OPENED, RANKED OR PRIORITISED AND NO SYNTHESIS WAS BEGUN'
                       in out),
                      ("the guard's behaviour is unchanged",
                       "THE GUARD'S BEHAVIOUR IS NOT CHANGED -- ONLY A COMMENT MOVED" in out),
                      ('never by filename', 'NEVER BY FILENAME' in out),
                      ('nothing removed and the roster not edited',
                       'NO ARCHIVE FILE WAS REMOVED, MOVED OR RENAMED AND THE MIRROR ROSTER WAS '
                       'NOT EDITED' in out),
                      ('already done by the record at b360',
                       'ALREADY DONE BY THE RECORD AT b360' in out),
                      ('the (R4) repair is reported in its own line',
                       'RATHER THAN COUNTED AS A FAILED RE-READ' in out),
                      ('no standard edited and no amendment applied',
                       'NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED' in out),
                      ('the registry was read and not touched',
                       'REGISTRY.md WAS READ AND NOT TOUCHED' in out),
                      ('nothing recommended', "NOTHING IS RECOMMENDED AND THE CITATION QUESTION "
                       "REMAINS THE AUTHOR'S" in out),
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
    rec('b385 -- THE DESK UNDER (R7), THE THREE CLOSING WRITES, AND THE BANK.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE DESK.')
    rec('-' * 100)
    Q = do_desk()
    Q['lists_closed'] = 0

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE TRAIL BLOCK, APPEND-ONLY -- AND THE SIX ENTRIES GO IN THROUGH ITS WRITER.')
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

    # ### **THE ENTRIES ARE COUNTED IN THE LEDGER ITSELF AND NOT ONLY IN THE COMPONENT RECORD.**
    # ### The order says the six are entered THROUGH THE TRAILS WRITER, so the count that matters is
    # ### the one the ledger carries after the write.
    seg = after.split(MARK, 1)[-1]
    entered = [e['cluster'] for e in AC['entries'] if ('`%s`' % e['cluster']) in seg]
    rule_beside = seg.count('a cluster may have SEVERAL keystones, ONE, or NONE YET')
    rec('  ### ### **CLUSTER ENTRIES PRESENT IN THE APPENDED BLOCK : %d of %d.**'
        % (len(entered), len(AC['entries'])))
    rec('  ### ### **THE MANY-TO-MANY RULE STATED BESIDE AN ENTRY : %d TIMES.**' % rule_beside)
    for e in AC['entries']:
        rec('      %-62s in the ledger : %s'
            % (e['cluster'][:62], e['cluster'] in entered))
    tr.update(entries_in_ledger=len(entered), rule_beside=rule_beside)

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
        run_clock.write(D, 'b385_desk_notes', LINES)
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b385_desk_notes', LINES)
        return 1
    g1 = ('THE REVIEWER-RESERVOIR RULE IS LOCATED' in ROWS[0][0]
          and "b383'S ABSENCE CLAIM IS REFUTED" in ROWS[0][0]
          and 'CHECKS WHAT EACH GATE READ' in ROWS[0][1]
          and ('THE RULE IS IN %s AT LINE %d' % (RULE_FILE, RULE_LINE)) in ROWS[0][1]
          and 'SESSION PROTOCOL' in ROWS[0][1]
          and "THE NAVIGATOR'S NAME FOR THE RULE" in ROWS[0][1]
          and 'A CONTROLLED SEARCH FOR THE WRONG STRING' in ROWS[0][1]
          and 'NOT THAT THE TERM IS THE RIGHT ONE' in ROWS[0][1]
          and 'OVER-STATED' in ROWS[0][1]
          and 'NEITHER PLACE MAKES THE WHOLE MANIFEST THE AUTHORITY' in ROWS[0][1]
          and 'NOT-YET-SYNTHESIZED' in ROWS[0][1]
          and 'THE MANY-TO-MANY RULE' in ROWS[0][1]
          and 'NO SYNTHESIS WAS BEGUN' in ROWS[0][1]
          and 'NONE PARTLY' in ROWS[0][1]
          and 'REPAIRED UNDER (R4)' in ROWS[0][1]
          and 'NEVER BY FILENAME' in ROWS[0][1]
          and 'COMPUTED AND PRINTED UNUSED' in ROWS[0][1]
          and 'ALREADY DONE BY THE RECORD AT b360' in ROWS[0][1]
          and 'TWENTY-FIVE ACTS' in ROWS[0][1]
          and 'ROUTED AND NOT ANSWERED' in ROWS[0][1]
          and 'NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN' in ROWS[0][2]
          and 'FINDING A RULE IS NOT RULING ONE' in ROWS[0][2]
          and 'CANNOT RE-READ BY CONSTRUCTION' in ROWS[0][2]
          and 'NO CLASS WAS RULED' in ROWS[0][3]
          and 'REGISTRY.md WAS READ AND NOT TOUCHED' in ROWS[0][3]
          and 'THE REFUTATION IS SAID FIRST' in ROWS[0][4]
          and 'NOT ADOPTED AS THE RULE' in ROWS[0][4]
          and 'NOTHING IS RECOMMENDED' in ROWS[0][4]
          and 'THE SIX ENTERED ON THE TRAILS' in ROWS[0][5]
          and 'THE MANY-TO-MANY RULE IS STATED BESIDE EVERY ENTRY' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says the located rule with its line, the refuted absence claim, the wrong-string '
        'species, the scored paraphrase and its exact over-statement, the six entries with the '
        'many-to-many rule, the three dispositions, the (R4) repair, the unused filename '
        'comparison, the b360 closure and its twenty-five acts, the routed question, and the '
        'scope : %s' % g1)
    if not g1:
        run_clock.write(D, 'b385_desk_notes', LINES)
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
            run_clock.write(D, 'b385_desk_notes', LINES)
            return 1
        rownum = start

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE INDEX KEY.')
    rec('-' * 100)
    kok = do_key(rownum)

    rec('')
    rec('-' * 100)
    rec('  ### (5) THE ONE REPAIR, AND WHAT IT DID NOT CHANGE.')
    rec('-' * 100)
    rec('    the guard was repaired under (R4)              : %s' % AC['guard_repaired'])
    rec('    the guard`s behaviour is unchanged             : %s'
        % AC['guard_behaviour_unchanged'])
    rec('    the mirror roster was edited                   : %s' % AC['roster_edited'])
    rec('    standards edited                               : %d' % AC['standards_edited'])
    rec('    archive files removed, moved or renamed        : %d' % AC['archive_removed'])
    rec('    clusters opened, ranked or prioritised         : %d' % AC['clusters_opened'])
    rec('    options recommended                            : %d' % AC['options_recommended'])
    rec('    the citation question answered                 : %s' % AC['question_answered'])
    rec('  ### ### **FINDING A RULE IS NOT RULING ONE, AND ENTERING A CLUSTER ON A TRAIL IS NOT')
    rec('  ### ### SYNTHESIZING IT.**')

    rec('')
    rec('-' * 100)
    rec('  ### (6) THE BANK.')
    rec('-' * 100)
    B = []
    BAR, SUB = '=' * 100, '-' * 100
    B.append(BAR)
    B.append('b385 -- THE SIX ON THE TRAILS, THE RULE FOUND, AND THE THREE THAT WAITED ON NOTHING.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **THE RULE `b383` REPORTED ABSENT IS IN THE REGISTRY, AND THE ABSENCE')
    B.append('### ### ### CLAIM IS REFUTED BY THIS ACT -- SAID FIRST RATHER THAN FOLDED INTO A')
    B.append('### ### ### RESULT.**')
    B.append('### `%s` line `%d`, under ### **`## SESSION PROTOCOL -- reviewer mirror-refresh'
             % (RULE_FILE, RULE_LINE))
    B.append('### ### (standing rule, 2026-07-29)`.**')
    B.append('### ### **WHY `b383` MISSED IT, WHICH IS THE FINDING AND NOT THE EXCUSE:** ### it')
    B.append('### searched for ### **THE NAVIGATOR`S NAME FOR THE RULE** -- `reservoir`,')
    B.append('### `reviewer pool`, `reviewer budget` -- ### **AND THE RULE USES NONE OF THOSE')
    B.append('### ### WORDS.** ### Its control fired, its sweep was honest and its files were')
    B.append('### right. ### **A CONTROLLED SEARCH FOR THE WRONG STRING IS STILL A CONTROLLED')
    B.append('### ### SEARCH FOR THE WRONG STRING**, and a positive control proves the matcher')
    B.append('### works -- ### **NOT THAT THE TERM IS THE RIGHT ONE.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 1 -- THE SIX NOT-YET-SYNTHESIZED CLUSTERS, ON THE TRAILS LEDGER.')
    B.append(SUB)
    B.append('### ### **ENTRIES WRITTEN : %d. ### CLUSTERS THE CENSUS COUNTED : %d. ### CLUSTERS'
             % (AC['entries_written'], AC['clusters_counted']))
    B.append('### ### OPENED, RANKED OR PRIORITISED : %d.**' % AC['clusters_opened'])
    B.append('### ### **ENTERED THROUGH THE TRAILS WRITER**, as the order requires, and the')
    B.append('### ledger itself carries ### **%d OF %d** ### after the write.'
             % (tr['entries_in_ledger'], len(AC['entries'])))
    B.append('### ### **THE MANY-TO-MANY RULE IS STATED BESIDE EVERY ENTRY -- `%d` TIMES IN THE'
             % tr['rule_beside'])
    B.append('### ### APPENDED BLOCK**, so no later reader can meet an entry without it.')
    B.append('###   ### **THE RULE:** ### a cluster may have SEVERAL keystones, ONE, or NONE YET;')
    B.append('###   the relation is many-to-many and it changes over time. ### **A CLUSTER WITH NO')
    B.append('###   ### KEYSTONE IS `NOT-YET-SYNTHESIZED`, NOT OWED AND NOT DEFICIENT.**')
    B.append('')
    for e in AC['entries']:
        B.append('###   ### **`%s`**' % e['cluster'])
        B.append('###     where its material sits   : %s' % e['where'])
        B.append('###     a synthesis would draw on : %s' % e['draws'][:180])
        if len(e['draws']) > 180:
            B.append('###                               %s' % e['draws'][180:360])
        B.append('###     what would make it ripe   : %s'
                 % re.sub(r'#{2,}', '', e['ripe'])[:180].strip())
        if len(re.sub(r'#{2,}', '', e['ripe']).strip()) > 180:
            B.append('###                               %s'
                     % re.sub(r'#{2,}', '', e['ripe']).strip()[180:400])
        B.append('###     the rule beside it        : %s' % e['rule_beside'])
    B.append('')
    B.append('### ### ### **NOTHING IS OPENED. ### THESE ARE TRAIL ENTRIES.** ### No document was')
    B.append('### read for content beyond its registry row and ### **NO SYNTHESIS WAS BEGUN.**')
    B.append('### ### **AND THE `ANNEX` ENTRY SAYS OF ITSELF THAT IT IS NOT A SUBJECT CLUSTER**,')
    B.append('### rather than being quietly dropped from a count the census made.')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 2 -- THE RESERVOIR RULE. ### **LOCATED.**')
    B.append(SUB)
    B.append('### ### **THE TARGETED SEARCH, ITS TERMS AND ITS POSITIVE CONTROL** -- the full')
    B.append('### record is `data/%s` and `data/%s`.' % (E['run_file'], AC['run_file']))
    B.append('###   ### **POSITIVE CONTROL** `internal-until-fruit` (a known rule) : `%d` file(s)'
             % E['control_hits'])
    for k, v in E['probes'].items():
        B.append('###   term %-24s : `%d` file(s)' % ('`%s`' % k, v))
    B.append('### ### ### **THE THREE TERMS THAT FOUND IT WERE `SESSION PROTOCOL`,')
    B.append('### ### ### `reviewer`s authority` AND `not from recall` -- ### **ALL THREE FROM THE')
    B.append('### ### ### RULE`S OWN VOCABULARY, WHICH THE ORDER SUPPLIED.**')
    B.append('### ### **THE ORDER`S OWN WORDING IS WHAT FOUND IT**, and that is worth recording:')
    B.append('### the navigator described the rule`s CONTENT and `b383` searched for its NAME.')
    B.append('')
    B.append('### ### **THE RULE IS QUOTED WHOLE WITH ITS LOCATION IN `data/%s`**,' % AC['run_file'])
    B.append('### every line carrying its file and its line number and ### **RE-READ OUT OF THAT')
    B.append('### ### FILE BEFORE IT WAS WRITTEN.** ### Its parts: the standing-rule heading; the')
    B.append('### rule sentence (### *any session in which the chat reviewer reasons about paper')
    B.append('### ### content begins with a fresh mirror-refresh export*###); a ### **PROCEDURE**')
    B.append('### naming the reviewer set and the `MANIFEST.md` columns; a ### **WHY THIS IS A HARD')
    B.append('### ### RULE, NOT A NICETY** ### citing ### **TWO RECORDED ERRORS**; and a')
    B.append('### ### **CURRENCY CHECK** ### in which ### *the MANIFEST wins and the claim is')
    B.append('### stale.*')
    B.append('')
    B.append('### ### ### **THE PARAPHRASE, SCORED CLAUSE BY CLAUSE: `%d` CLAUSES, `%d` ACCURATE,'
             % (AC['clauses_scored'], AC['accurate']))
    B.append('### ### ### `%d` OVER-STATED, `0` NARROWED.**' % AC['over_stated'])
    for p in AC['paraphrase']:
        B.append('###   ### **%-12s** ### *%s*' % (p['mark'] + ' :', p['clause']))
    B.append('### ### **THE OVER-STATEMENT IS NAMED EXACTLY AND NOT GENERALLY:** ### the rule does')
    B.append('### not make the MANIFEST the authority. ### It makes ### **THE MANIFEST`S `md5` +')
    B.append('### ### `last-commit` COLUMNS** ### the authority, and the Currency check widens the')
    B.append('### disagreement test to three fields (`version, md5, or last-commit`) -- ###')
    B.append('### **BUT NEITHER PLACE MAKES THE WHOLE MANIFEST THE AUTHORITY.** ### The paraphrase')
    B.append('### is wider than the rule.')
    B.append('### ### **AND ONE ACCURATE CLAUSE IS ACCURATE WITH A NARROWING NOTED:** ### the')
    B.append('### rule`s subject is ### **THE CHAT REVIEWER**, not a session in general -- ### **A')
    B.append('### ### NARROWING IN THE RULE IS NOT AN OVER-STATEMENT IN THE PARAPHRASE**, and the')
    B.append('### two are scored apart.')
    B.append('')
    B.append('### ### **AND THE NAME IS NOT IN THE RECORD.** ### The corpus does not call this a')
    B.append('### `reviewer-reservoir rule` anywhere; it calls it a ### **SESSION PROTOCOL** ###')
    B.append('### and a ### **STANDING RULE.** ### **A NAME THAT IS NOT IN THE RECORD IS NOT AN')
    B.append('### ### ERROR IN THE RULE** -- it is a name, reported as the navigator`s.')
    B.append('### ### ### **`(F1)` IS MET ON BOTH HALVES:** ### the rule is LOCATED in a')
    B.append('### session-protocol section, and ### **THE PARAPHRASE OVER-STATED ITS SCOPE IN')
    B.append('### ### EXACTLY ONE CLAUSE.**')
    B.append('### ### ### **AND AMENDMENT `(iv)` IS ANSWERED BY A FINDING AND NOT BY A RULING**,')
    B.append('### which is the better of the two outcomes `b383` routed.')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 3 -- THE THREE THAT WAITED ON NOTHING. ### **EACH DONE OR ROUTED,')
    B.append('### NONE PARTLY.**')
    B.append(SUB)
    for it in AC['items']:
        B.append('###   %-52s ### **%s**' % (it['item'], it['disposition']))
    B.append('')
    B.append('### ### **(a) THE GUARD`S STALE INSTALL LINE -- `DONE`.** ### The tracked guard')
    B.append('### documented `cp ... .git/hooks/pre-push` while ### **EVERY ROSTERED REPOSITORY')
    B.append('### ### RUNS `core.hooksPath = .githooks`** ### since `b371` moved it. ### Repaired')
    B.append('### under ### **`(R4)`: PRESERVE BY QUOTATION, REPAIR BY EDIT** -- the stale line')
    B.append('### quoted from the PRE-REPAIR file and the file`s line then corrected.')
    B.append('### ### **THE GUARD`S BEHAVIOUR IS NOT CHANGED : %s.** ### Only the comment moved.'
             % AC['guard_behaviour_unchanged'])
    B.append('### ### ### **AND THE QUOTATION CANNOT RE-READ, BY CONSTRUCTION** -- so it is')
    B.append('### ### ### reported in its own line and ### **NOT COUNTED AS A FAILED RE-READ.**')
    B.append('###   quotations that failed to re-read              : `%d`'
             % len(AC['reread_failures']))
    B.append('###   quotations this act itself repaired under (R4) : `%d`' % AC['repaired_count'])
    B.append('')
    B.append('### ### **(b) THE ARCHIVE FILES -- `DONE WITH EXCEPTIONS REPORTED`.**')
    B.append('###   files under `archive/`, ALL EXTENSIONS : `%d`' % AC['archive_all'])
    B.append('###   of them `.md`                          : `%d`' % AC['archive_files'])
    B.append('###   ### **DIGEST AGAINST THE GIT BLOB     : `%d` CONFIRMED / `%d` NOT**'
             % (AC['archive_digest_ok'], AC['archive_digest_bad']))
    B.append('###   ### **CONTENT (TITLE OR PURPOSE)      : `%d` CONFIRMED / `%d` NOT**'
             % (AC['archive_content_ok'], AC['archive_content_bad']))
    B.append('###   ### **CONFIRMED BY DIGEST AND BY CONTENT AND ### NEVER BY FILENAME** -- the')
    B.append('###   filename comparison was ### **COMPUTED AND PRINTED UNUSED** ### and')
    B.append('###   ### **NO VERDICT ABOVE DEPENDS ON IT : %s.**' % (not AC['filename_used']))
    B.append('### ### ### **`%d` REMOVED, MOVED OR RENAMED. ### THE REMOVAL IS THE AUTHOR`S.**'
             % AC['archive_removed'])
    B.append('### ### **`b378` COUNTED `92` AND THIS ACT COUNTS `92`** -- and ### **MY REGISTERED')
    B.append('### ### EXPECTATION `(E2)` THAT THE TWO WOULD DIFFER IS REFUTED BY MY OWN RUN**,')
    B.append('### which is printed rather than dropped. ### Neither figure is wrong for its date')
    B.append('### and ### **WHAT EACH COUNTED IS SAID.**')
    B.append('')
    B.append('### ### **(c) THE FACES LEDGER AND THE MIRROR ROSTER -- `ALREADY DONE BY THE')
    B.append('### ### RECORD`.**')
    B.append('###   roster entries : `%d`. ### `FACES_LEDGER.md` present : %s.'
             % (AC['items'][2]['roster_entries'], AC['faces_present']))
    B.append('### ### **`b359` FILED THE ABSENCE; `b360` ADDED IT WHEN IT EXECUTED THE AUTHOR`S')
    B.append('### ### ROSTER RULING** -- and the desk then carried the item for ### **TWENTY-FIVE')
    B.append('### ### ACTS AFTER IT WAS DONE.**')
    B.append('### ### ### **THAT IS `DESK_FRESHNESS` BITING THE DESK ONE ACT AFTER THE FOLD THAT')
    B.append('### ### ### RECORDED IT** -- ### **A RIGHT BELIEF WITH NO DATE ON IT**, in the')
    B.append('### rule`s own words. ### **NOTHING WAS ADDED AND THE ROSTER WAS NOT EDITED : %s.**'
             % (not AC['roster_edited']))
    B.append('### ### ### **THE CLOSURE IS FILED AND IT IS NOT CLAIMED BY THIS ACT.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 4 -- THE CITATION QUESTION. ### **ROUTED, NOT ANSWERED.**')
    B.append(SUB)
    B.append('### ### **THE QUESTION, IN THE STANDARD`S OWN WORDS: WHAT IS A FINISHED KEYSTONE')
    B.append('### ### CITED AS?** ### Tier K ### *may be cited as certification*; ### Tier C is')
    B.append('### ### *cited for orientation and organization -- NEVER as certification*, which')
    B.append('### the standard calls ### **ITS LOAD-BEARING RULE.** ### The author`s finished')
    B.append('### keystone carries the Tier-C role and the Tier-K obligation at once, and ###')
    B.append('### **THE TWO CITATION RULES CONTRADICT.**')
    B.append('### ### **THE FAILURE THE TIERS EXIST TO PREVENT, QUOTED BESIDE THE OPTIONS:** ###')
    B.append('### the formation-universality over-claim of June 2026, in which ### **A TIER-C')
    B.append('### ### SYNTHESIS PANEL WAS READ AS A CERTIFICATION.**')
    B.append('### ### **`%d` OPTIONS, ALL THREE THE STANDARD`S OWN RULED BORDERLINES. ### THIS'
             % AC['options'])
    B.append('### ### SEAT SUPPLIES NO FOURTH.**')
    B.append('###   ### **OPTION A -- THE `CATALOGOS` PATTERN: RULE IT TIER C, READ THE PINNED')
    B.append('###     ### ROWS AS K.** ### *Obliges:* citation for orientation, with the')
    B.append('###     Correspondence rows cited as certification ### **ROW BY ROW, NOT DOCUMENT BY')
    B.append('###     ### DOCUMENT** -- so the document must MARK which is which, and the failure')
    B.append('###     above is prevented by the marking and not by the class.')
    B.append('###   ### **OPTION B -- THE `UNIVERSALITY` PATTERN: RULE IT TIER K, WITH A C-SCOPE')
    B.append('###     ### NOTE.** ### *Obliges:* the document is citable as certification and')
    B.append('###     every synthesis claim in it carries a scope note saying it is not -- ###')
    B.append('###     **THE BURDEN MOVES TO THE SYNTHESIS SENTENCES.**')
    B.append('###   ### **OPTION C -- THE `THE_SUBSTRATE` PATTERN: RULE IT TIER K, THE OTHER')
    B.append('###     ### MATERIAL READ AS CONTEXT.** ### *Obliges:* the synthesis material makes')
    B.append('###     ### **NO ASSERTION THE DOCUMENT WOULD BE CITED FOR** -- ### a strong')
    B.append('###     condition on what a finished keystone may say.')
    B.append('### ### **AND A FOURTH THING THE AUTHOR MAY WISH TO SETTLE INSTEAD OF CHOOSING:**')
    B.append('### ### `Tier E` shows the standard ALREADY KNOWS HOW TO RELAX AN AUDIENCE WITHOUT')
    B.append('### ### RELAXING A CERTIFICATE. ### **THAT IS NOT A FOURTH OPTION AND IT IS NOT')
    B.append('### ### OFFERED AS ONE.**')
    B.append('### ### ### **NOTHING IS RECOMMENDED. ### NO OPTION IS RANKED, PREFERRED OR')
    B.append('### ### ### CALLED LIKELIEST -- `%d` OF `%d`. ### THE QUESTION IS THE AUTHOR`S :'
             % (AC['options_recommended'], AC['options']))
    B.append('### ### ### ANSWERED %s.**' % AC['question_answered'])
    B.append('')
    B.append(SUB)
    B.append('### THE DESK, THE WRITES, AND WHAT THIS ACT DID NOT DO.')
    B.append(SUB)
    B.append('### desk items swept : %d ### / ### closed : %d ### / ### standing : %d ### / ### '
             'lists closed : %d' % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
    B.append('### ### **AND ONE OF THE FOUR CLOSURES WAS ALREADY DONE BY THE RECORD**, which is')
    B.append('### filed as such rather than counted as this act`s work.')
    B.append('### trail block appended (append-only %s, committed prefix intact %s); '
             '`CORRESPONDENCE.md` row %s;'
             % (tr['appended_only'], tr['committed_prefix_intact'], rownum))
    B.append('### index key `the-reservoir-rule-located-and-the-six-on-the-trails` reachable by')
    B.append('### every alias : %s' % kok)
    B.append('')
    B.append('### ### **NO CLASS WAS RULED. ### NO DOCUMENT WAS RECLASSIFIED. ### NO DECLARATION')
    B.append('### ### WAS MOVED. ### NO GRADE WAS MOVED. ### NO ACT WAS RE-VERDICTED. ### NO LIST')
    B.append('### ### WAS CLOSED.**')
    B.append('### ### **NO STANDARD WAS EDITED (`%d`) AND NO AMENDMENT WAS APPLIED** -- the four'
             % AC['standards_edited'])
    B.append('### `b383` drafted stay ### **ROUTED AND UNAPPLIED.**')
    B.append('### ### **`REGISTRY.md` WAS READ AND NOT TOUCHED**, and ### **NO CORPUS DOCUMENT WAS')
    B.append('### ### WRITTEN INTO EXCEPT `OPEN_TRAILS.md`**, which was appended to and never')
    B.append('### edited. ### **THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME.**')
    B.append('### ### **NO ARCHIVE FILE WAS REMOVED, MOVED OR RENAMED (`%d`). ### NO CLUSTER WAS'
             % AC['archive_removed'])
    B.append('### ### OPENED (`%d`). ### THE MIRROR ROSTER WAS NOT EDITED.**' % AC['clusters_opened'])
    B.append('### ### **THE ONE REPAIR THIS ACT MADE IS `.githooks/pre-push` LINE 10 UNDER `(R4)`,')
    B.append('### ### A COMMENT AND NOT A BEHAVIOUR.**')
    B.append('### ### **NO `.lean` FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED.**')
    B.append('### **THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED. ### THE POSTURE')
    B.append('### LOCK IS SEPARATE.** ### `h2` stands exactly where the deposit left it and this')
    B.append('### act makes no claim about it in either direction. ### **NOTHING IS DEPOSITED AND')
    B.append('### ### NOTHING WAS WRITTEN AT ZENODO.**')
    B.append('')
    B.append(SUB)
    B.append('### THE NAVIGATOR`S EXPECTATIONS, AND MINE.')
    B.append(SUB)
    B.append('### ### **`(F1)` MET ON BOTH HALVES.** ### The rule is LOCATED in a session-protocol')
    B.append('### section and ### **THE PARAPHRASE OVER-STATED ITS SCOPE** ### in exactly one')
    B.append('### clause of three.')
    B.append('### ### **`(F2)` MET, THOUGH NOT IN THE WAY IT PREDICTED.** ### All three of')
    B.append('### Component 3`s items completed ### **WITHOUT A RULING** -- but one of them')
    B.append('### completed ### **BEFORE THE ACT BEGAN**, at `b360`, and the desk had been carrying')
    B.append('### it for twenty-five acts. ### **AN EXPECTATION MET BY A DIFFERENT MECHANISM IS')
    B.append('### ### STILL WORTH SAYING SO.**')
    B.append('### ### ### **AND MY OWN REGISTERED EXPECTATION `(E2)` IS REFUTED BY MY OWN RUN:**')
    B.append('### I registered that the archive count would differ from `b378`s. ### **BOTH COUNT')
    B.append('### ### `92`.** ### Printed, not dropped.')
    B.append('')
    B.append(SUB)
    B.append('### WHAT THIS ACT ADDS TO THE LORE.')
    B.append(SUB)
    B.append('### ### ### **NEW -- `A CONTROLLED SEARCH FOR THE WRONG STRING IS STILL A CONTROLLED`')
    B.append('### ### ### `SEARCH FOR THE WRONG STRING`.** ### `b383` ran an honest sweep with a')
    B.append('### firing positive control and reported an absence that was false. ### **THE')
    B.append('### ### CONTROL PROVES THE MATCHER WORKS. ### IT SAYS NOTHING ABOUT WHETHER THE TERM')
    B.append('### ### IS THE RIGHT ONE**, and `b378`s rule -- an absence needs a proved search --')
    B.append('### is hereby ### **NECESSARY AND NOT SUFFICIENT.**')
    B.append('### ### ### **NEW -- `SEARCHING FOR A NAME WHEN YOU WERE GIVEN A DESCRIPTION`.** ###')
    B.append('### The order described the rule`s CONTENT and `b383` searched for its NAME. ### The')
    B.append('### three terms that found it -- `SESSION PROTOCOL`, `reviewer`s authority`, `not')
    B.append('### from recall` -- ### **ALL CAME FROM THE ORDER`S OWN DESCRIPTION.**')
    B.append('### ### ### **NEW -- `A DESK ITEM WITHOUT A DATE IS AN ITEM NOBODY HAS RE-READ`.**')
    B.append('### The faces-ledger item was done at `b360` and carried for twenty-five acts. ###')
    B.append('### **`DESK_FRESHNESS` BIT THE DESK ONE ACT AFTER THE FOLD THAT RECORDED IT**, which')
    B.append('### is `b384`s ### *a minted rule is not a carried rule* ### arriving again.')
    B.append('### ### ### **NEW -- `A LINE QUOTED AND THEN REPAIRED CANNOT RE-READ, BY`')
    B.append('### ### ### `CONSTRUCTION`.** ### `(R4)` says preserve by quotation and repair by')
    B.append('### edit, so the re-read arm ### **MUST** ### fail on that one line. ### **THAT IS')
    B.append('### ### THE RULE WORKING AND NOT A DEFECT**, and it is reported in its own line')
    B.append('### rather than counted as a failure.')
    B.append('### **MET AGAIN -- AN ABSENCE NEEDS A PROVED SEARCH** (`b378`), ### **A SWEEP')
    B.append('### EXCLUDES ITS OWN ACT`S FILES** (`b368`, `b383`), and ### **A COUNT IS NOT A LIST**')
    B.append('### -- the two archive figures are two counts over two dates and neither is a subset')
    B.append('### of the other.')
    B.append('')
    B.append(SUB)
    B.append('### THE RECORD.')
    B.append(SUB)
    regtxt = io.open(os.path.join(D, 'b385_registration_2026-09-09.txt'), encoding='utf-8').read()
    m_sha = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt)
    m_by = re.search(r'bytes locked : (\d+)', regtxt)
    m_at = re.search(r'locked at \(UTC\) : (\S+)', regtxt)
    B.append('### registration locked at (UTC) %s' % (m_at.group(1) if m_at else '?'))
    B.append('### ### **%s bytes, sha256 `%s`, %d clauses, ### LOCKED BEFORE ANY WRITE AND CHAINED'
             % (m_by.group(1) if m_by else '?', m_sha.group(1) if m_sha else '?',
                len(J('b385_satisfiable')['clauses'])))
    B.append('### ### ON A GATE THAT CHECKS WHAT EACH GATE READ.** ### %d gates read, %d checked by '
             'digest.' % (LG['gates_read'], LG['face_subject_gates']))
    B.append('### The extract`s clock is `%s` and the lock`s is `%s`.'
             % (E.get('run_clock'), (m_at.group(1) if m_at else '?')))
    for n in ('b385_reads', 'b385_lockgate', 'b385_components'):
        j = J(n)
        B.append('### %-18s run file `%s` recorded clock %s'
                 % (n, j['run_file'], j.get('run_clock')))
    B.append('### **THE REFS THIS ACT READ IN THE ROSTERED REPOSITORIES:**')
    for k, v in E['refs'].items():
        B.append('###   %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    B.append('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor. ### **EVERY ANCHOR WAS '
             'READ FROM ITS FILE AND NONE WAS TYPED**, and the rule was read at'
             % (E['reads'], E['without_anchor']))
    B.append('### ### **THE CANONICAL DRIVE, NEVER THE MIRROR.**')
    B.append('### ### **FIVE NEW `relay` TOOLS AGAINST A CAP OF SIX, AND NO SHARED UTILITY.**')
    B.append(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### A CLASS WAS RULED.', '### A DECLARATION WAS MOVED.', '### A LIST WAS CLOSED.',
                '### THE RULE WAS NOT LOCATED.', '### THE PREFERRED OPTION IS.',
                '### A CLUSTER WAS OPENED.', '### AN ARCHIVE FILE WAS REMOVED.',
                '### THE ROSTER WAS EDITED.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))

    rec('')
    rec('=' * 100)
    rec('  ### desk swept %d ; trail appended %s ; entries in the ledger %d/%d ; row %s ; key %s'
        % (Q['items'], tr['appended_only'], tr['entries_in_ledger'], len(AC['entries']),
           rownum, kok))
    rec('  ### ### **LISTS CLOSED : 0. ### THE FOUR ARE RESTATED `OPEN` BY NAME.**')
    rec('  ### ### **FOUR DESK CLOSURES, AND ONE OF THEM WAS NOT THIS ACT`S WORK.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b385_desk_notes', LINES)
    ok_entries = (tr['entries_in_ledger'] == len(AC['entries'])
                  and tr['rule_beside'] >= len(AC['entries']))
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             entries_in_ledger=tr['entries_in_ledger'], rule_beside=tr['rule_beside'],
             bank='b385_the_six_on_the_trails.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             rule_file=RULE_FILE, rule_line=RULE_LINE,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b385_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and ok_entries and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
