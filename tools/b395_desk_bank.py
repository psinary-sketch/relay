# -*- coding: utf-8 -*-
"""b395_desk_bank.py -- THE DESK, THE LEDGER WRITES, AND THE BANK.

### ### **THE ONLY CORPUS WRITE THIS ACT MAKES IS `(R21)`'S, AND `b395_components.py` MADE IT.**
### This file writes the ledgers and the bank, and closes what `(R7)` permits.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                  # noqa: E402
import b302_correspondence as C   # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b395 the ceiling answered: the eleven were readable all along -->'
PRIOR = '<!-- b394 the reconciliation batched: three keystones read -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


SEALTXT = io.open(os.path.join(D, 'b395_registration_2026-09-09.txt'),
                  encoding='utf-8').read()
SEALHASH = re.search(r'sha256 of every byte ABOVE this block : ([0-9a-f]{64})', SEALTXT).group(1)
SEALSTAMP = re.search(r'locked at \(UTC\) : (\S+)', SEALTXT).group(1)

AC = J('b395_components')
LG = J('b395_lockgate')
E = J('b395_reads')
C1, C2, C3, A1, A3 = AC['c1'], AC['c2'], AC['c3'], AC['a1'], AC['a3']
S2 = E['s2']
BANKOUT = os.path.join(D, 'b395_the_ceiling_answered.txt')


def blob(rel):
    r = subprocess.run(['git', 'show', 'HEAD:' + rel], cwd=PP, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


DESK = [
    ('M-2, under b310 cap', 'STAND', 'the aggregation is still SPECIFIED-NOT-STATED'),
    ("the object's conditions", 'STAND', "the conditions are the object's and none discharged"),
    ('the uniformity row U1', 'STAND', "the row's own refusal stands"),
    ('the instrument lane, PARKED under ruling R4', 'STAND', "PARKED by the author's ruling"),
    ('the wave, and the wave candidate list', 'STAND', "PARKED by the author's ruling"),
    ('the routed items, each with its owner', 'STAND', 'each still carries its owner'),
    ('the patent receipts, absent on the mounted volumes', 'STAND', "the patent seat owns it"),
    ('the count claim above the repaired Layer-1 list', 'STAND', 'no act sent to it since b369'),
    ("the retirement ledger's own lacunae", 'STAND', 'FILED, NOT INVENTED, AND NOT REPAIRED'),
    ('where the keystone census should live, ROUTED at b375', 'STAND', 'ROUTED to the author'),
    ("the census's definition-versus-operation drift", 'STAND', 'FILED at b377, NOT REPAIRED'),
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND', 'OPEN'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND',
     'OPEN. ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', 'OPEN. ### This act dates none'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND', 'OPEN'),
    ('the three amendments b383 drafted that are still routed', 'STAND', 'ROUTED AND UNAPPLIED'),
    ('the download-layer book`s registry drift', 'STAND', "OPEN AND THE AUTHOR`S"),
    ('the six subject clusters with no keystone', 'STAND', '`NOT-YET-SYNTHESIZED` since b385'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', 'NOT RE-MEASURED'),
    ('the ten untracked run records of earlier acts', 'STAND', 'NAMED at b382, STILL UNTRACKED'),
    ('the legacy `.git/hooks/pre-push` copies', 'STAND', '### **RULED BY `(R16)`: THEY STAY**'),
    ('the untracked `.b304-backup` artifacts', 'STAND', 'NAMED at b386, still untracked'),
    ('the five keystones the union names that carry no correspondence table', 'STAND',
     'CONFIRMED BY READING at b394 and NOT REPAIRED. ### **STILL THE AUTHOR`S**'),
    ('the 23 unreadable correspondence rows', 'STAND', 'NAMED at b388 by cause, and ROUTED'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the keystone-class documents b388 marked UNASSIGNED', 'STAND',
     '### **UNASSIGNED IS A STATE AND NOT A DEBT**'),
    ('the deposited layer, unread since b389', 'STAND',
     'STILL BLOCKED; this act did not ask the platform'),
    ('the eight-versus-six cluster-synthesis disagreement', 'STAND', 'ROUTED at b389'),
    ('the practice that let the phantom drift run', 'STAND',
     'TWO INSTANCES in four acts. ### **NOTHING IN THE CORPUS CHECKS A CITED VERSION AGAINST '
     'ITS TARGET.** ### **STILL OPEN**'),
    ('the `66` superseded version citations', 'STAND', 'REPORTED at b391 and LEFT'),
    ('`CONSTANCE.md` carries no version in its own bytes', 'STAND',
     'ROUTED at b391. ### **AND `b395` ADDS A SECOND FACT ABOUT IT:** ### its text names `0` '
     'documents the corpus holds, and it shares `0` with the other member of its own cluster'),
    ('placement into `Tier KC`', 'STAND', 'PRICED at b393 and STILL EMPTY'),
    ('whether `SIDE-kernel` has a current citable record', 'STAND', 'ROUTED at b392'),
    ('the two deposited records` remediation', 'STAND',
     '### **THE NOTE FOR `21432399` IS NOW DRAFTED AT `b395` AND IS WRITTEN NOWHERE.** ### '
     'For `19675356` the smallest recovering read is named and ### **THIS SEAT CANNOT PERFORM '
     'IT.** ### **STILL THE AUTHOR`S**'),
    ('the anchor question, unanswerable for three of five', 'STAND', 'ROUTED at b393'),
    ('the fifteen keystones not read', 'STAND',
     '### **AND `b395` REOPENS THIS ITEM RATHER THAN NARROWING IT.** ### `b394` reported the '
     'remaining twelve nearly unreachable; ### **TEN OF THE ELEVEN ARE READABLE WITHOUT A '
     'CLONE**, so the work is available and simply not done. ### **AVAILABLE AND NOT DONE IS A '
     'LARGER DEBT THAN BLOCKED**'),

    # ---- WHAT THIS ACT CLOSES AND ADDS -----------------------------------------------------------
    ('the eleven unreachable keystones', 'CLOSE',
     '### **CLOSED BY `(R7)`: THE OCCASION IS GONE, AND IT WAS NEVER THERE.** ### `b394` '
     'routed this item because reading the eleven `needs either a clone or a ruling about '
     'reading branches`. ### **NEITHER IS NEEDED.** ### The drive holds a named repository for '
     '### **`%d`** ### of them and every one resolves a HEAD here; the item rested on a matcher '
     'that recognised a backticked lowercase name and nothing else. ### **THE ITEM IS CLOSED '
     'AND THE WORK IT NAMED IS RETURNED TO THE ITEM ABOVE**' % C1['readable']),
    ('the predicate that produced `b394``s ceiling', 'STAND',
     '### **NEW at `b395`.** ### The matcher is repaired ### **IN THIS ACT`S OWN TOOL AND '
     'NOWHERE ELSE**; `b394``s tool, face and bank are unedited. ### **NO SWEEP HAS BEEN RUN '
     'FOR THE SAME SHAPE ELSEWHERE IN THE RECORD**, and `b370``s lore says a predicate that '
     'knows one shape finds one shape. ### **HOW MANY OTHER FINDINGS REST ON A BACKTICK IS '
     'UNMEASURED AND IS THIS ITEM.** ### **OPEN**'),
    ('`ENUMERA` names no terminal at all', 'STAND',
     '### **NEW at `b395`.** ### Its own text says `HELD` and names ### **NO FEDERATION '
     'REPOSITORY**, so no route reaches it and no clone would help. ### **WHAT IT NEEDS IS AN '
     'AUTHOR NAMING ITS TERMINAL**, which is authoring. ### **ROUTED**'),
    ('the `34` federation names the drive does not hold', 'STAND',
     '### **NEW at `b395`, AND IT IS NOT A DEFECT IN THE CORPUS.** ### The corpus names `%d` '
     'federation repositories and this drive holds `%d`; the account resolves the same `%d` '
     'unauthenticated. ### **NO DOCUMENT IS GRADED DOWN FOR A REPOSITORY THIS MACHINE DOES NOT '
     'HAVE** -- the ceiling is a fact about the working machine. ### **FILED, NOT REPAIRED**'
     % (len(S2['names']), len(S2['on_drive']), len(S2['resolves']))),
    ('`theory-space` shares nothing between its two members', 'STAND',
     '### **NEW at `b395`, AND DECIDED BY NOBODY.** ### `CONSTANCE` and `STRUCTURAL_FRACTION` '
     'name `0` documents in common and their opening lines are about different objects. ### '
     '**THEY WERE PUT IN ONE CLUSTER BY RECLASSIFICATION AND NOT BY BEING WRITTEN FOR ONE.** '
     '### Whether the cluster reads as a SUBJECT or as a DESTINATION is ### **THE AUTHOR`S '
     'QUESTION AND THIS ACT ANSWERS IT WITH A MEASUREMENT, NOT A VERDICT.** ### **ROUTED**'),
    ('`cross-domain` has something for a synthesis to be about', 'STAND',
     '### **NEW at `b395`.** ### Its two members name `%d` document(s) in common. ### **THAT IS '
     'EVIDENCE FOR A SYNTHESIS AND IS NOT A SYNTHESIS**, and `0` were written here. ### '
     '**ROUTED**' % A3['cross-domain']['shared']),
    ('the cluster reshaping, with the five named', 'CLOSE',
     '### **CLOSED BY `(R21)`, THE AUTHOR`S OWN RULING.** ### The one cluster of the five that '
     'answered the anchor question is ### **RE-ANCHORED IN THE MAP ITSELF**, additively, the '
     'prior anchor retained and not demoted; ### **THE OTHER FOUR ARE NOT RESHAPED AND WHY IS '
     'STATED BESIDE THE CHANGE.** ### The item that awaited the author has been answered by '
     'the author'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES TWO ITEMS, AND ONE OF THEM IT CLOSES BY DISPROVING IT.**')
    rec('    ### `(R7)` closes an item whose occasion is gone. ### **THE ELEVEN UNREACHABLE')
    rec('    ### ### KEYSTONES HAD NO OCCASION TO BEGIN WITH** -- the item recorded a property')
    rec('    ### ### of a matcher as a property of the corpus.')
    rec('    ### ### ### **AND CLOSING IT MAKES A STANDING ITEM BIGGER, NOT SMALLER:** ### the')
    rec('    ### ### ### fifteen-keystones item now names work that is ### **AVAILABLE AND NOT')
    rec('    ### ### ### DONE**, which is a larger debt than work that is blocked.')
    rec('')
    marks = []
    for item, want, why in DESK:
        marks.append(dict(item=item, disposition=want, why=why))
        rec('    %-74s %s' % (item[:74], want))
        for k in range(0, min(len(why), 900), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(marks) - len(closed)))
    rec('    ### ### **SIX ITEMS ARE ADDED AND ALL SIX STAND** -- because ### **A FINDING')
    rec('    ### ### RECORDED IS NOT A FINDING DISCHARGED.**')
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0, marks=marks)


SCOPE = (
    "**SCOPE: THE CEILING, ANSWERED OR PRICED -- AND THE CEILING WAS NOT THERE.** **b394 CLOSED BY "
    "CALLING ELEVEN KEYSTONES UNREACHABLE AND THAT WAS A PROPERTY OF ITS MATCHER, NOT OF THE "
    "CORPUS**: it recognised a BACKTICKED LOWERCASE repository name and nothing else, and widened "
    "to the same name written any other way the yield changes for 9 OF THE ELEVEN. THE DRIVE HOLDS "
    "A NAMED REPOSITORY FOR 8 OF THE 8 b394 SAID IT HELD NONE FOR, and every one resolves a HEAD "
    "here. **b394's FACE AND BANK ARE LOCKED AND ARE NOT EDITED; BOTH FIGURES ARE PRINTED AND THE "
    "DEFECTIVE PREDICATE IS NAMED.** THE PARTITION IS 10 ON THE DRIVE AND 1 NAMES NO TERMINAL, the "
    "parts summing to 11, so **(L1) ASKED FOR FOUR AND THE MEASUREMENT IS TEN**. FOUR ROUTES ARE "
    "PRICED IN WHAT THEY BUY: CLONE REACHES 0 FURTHER, A BRANCH-READING RULING REACHES 0 AS A "
    "READING ROUTE (the held branches are already local; a ruling is needed to GRADE them, which "
    "is the author's), ACCEPTING THE CEILING IS REFUTED, and **A FOURTH THE ORDER DID NOT POSE -- "
    "REPAIR THE PREDICATE -- REACHES 10 AT THE COST OF ONE MATCHER**. A ROUTE THAT REACHES ZERO IS "
    "REPORTED AS REACHING ZERO AND IS NOT PADDED. **(L2) HOLDS AND THE REASON IS ENUMERA, WHICH "
    "NAMES NO TERMINAL FOR ANY ROUTE TO REACH.** THE FEDERATION WAS READ LIVE WITH BOTH CONTROLS "
    "RUN FIRST: THE CORPUS NAMES 77, THE DRIVE HOLDS 43, THE ACCOUNT RESOLVES THE SAME 43, AND **A "
    "NEGATIVE IS ABSENT-OR-PRIVATE AND NEVER ABSENT**; every negative was RE-READ, because ONE "
    "READ IS NOT A MEASUREMENT -- an earlier form of this survey banked a false negative on a "
    "transient code 128. **RULING (R21) IS EXECUTED IN THE MAP ITSELF AND ADDITIVELY**: the "
    "Simplicity / RH cascade row is re-anchored to PATHS_TO_THE_CRITICAL_LINE on b393's measure, "
    "**THE PRIOR ANCHOR RETAINED AS A NAMED MEMBER AND NOT DEMOTED**, 0 members dropped, 0 content "
    "lost, the pre-edit row preserved VERBATIM in an appended block, the preserved quotation of "
    "the superseded table untouched, and **THE OTHER FOUR CLUSTERS NOT RESHAPED WITH THE REASON "
    "STATED BESIDE THE CHANGE**. THE NOTE FOR 21432399 IS DRAFTED AND WRITTEN NOWHERE; 19675356's "
    "SMALLEST RECOVERING READ IS NAMED AND THIS SEAT CANNOT PERFORM IT. NO SYNTHESIS WRITTEN, NO "
    "ANCHOR INVENTED, NEITHER ANCHORLESS CLUSTER DECIDED. NO GRADE MOVED, NO CLAIM WITHDRAWN, NO "
    "CORRESPONDENCE TABLE WRITTEN EXTENDED OR RE-GRADED, NO CLASS RULED, NO DOCUMENT RECLASSIFIED "
    "OR PLACED IN Tier KC, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, THE TAXONOMY AND THE "
    "DEPOSIT RULE NOT AMENDED, NEITHER MAP'S (R18) HEAD NOTE TOUCHED, NO LIST CLOSED. NOTHING "
    "DEPOSITS; **THE PLATFORM WAS NOT CALLED AT ALL**; 0 REPOSITORIES CLONED, 0 BRANCHES FETCHED "
    "MERGED PUSHED OR CREATED, NO BUILD RUN AND NO AXIOM PROFILE RECOMPUTED -- naming a repository "
    "the drive holds is not building it. **THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME.** NO NEW "
    "TRACKING DOCUMENT WAS CREATED. NO ARCHIVE OR outputs FILE TOUCHED, THE MIRROR ROSTER NOT "
    "EDITED, NO .git/hooks/pre-push DELETED. NO .lean FILE TOUCHED. NOTHING IS CLAIMED ABOUT THE "
    "MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the "
    "quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO "
    "COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The "
    "patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE "
    "INSTRUMENT LANE STAYS PARKED. THE WAVE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands "
    "exactly where the deposit left it and this act makes no claim about it in either direction.")


def trail_block(Q):
    return [
        '', MARK, '',
        '### **b395 — THE CEILING, ANSWERED OR PRICED (2026-09-09)**',
        '',
        ('*No block above is edited. The b394 block (`%s`) and every block before it stand exactly '
         'as they were written.*' % PRIOR),
        '',
        ('**THE CEILING WAS NOT THERE.** b394 closed by reporting that **eleven of the remaining '
         'twelve cannot be read by this rule at all**, `9` of them because *no kernel repository '
         'it names is on the drive*. That sentence was produced by a matcher that recognised a '
         '**backticked lowercase** name and nothing else. Widened to the same name written any '
         'other way, the yield changes for **`%d` of the eleven**, and **the drive holds a named '
         'repository for `%d` of the `%d` b394 said it held none for** — every one of them '
         'resolving a `HEAD` here, with the held and unmerged branches present in the local refs. '
         '**b394’s face and bank are locked and are not edited.** Both figures stand: b394 '
         'said eleven unreachable, and this act measures **`%d` of the eleven readable without a '
         'clone**. *A predicate that knows one shape finds one shape* — the corpus’s own '
         'lore, minted at b370, and this is the incident that proves it applies to the act that '
         'minted the ceiling.'
         % (C1['widened'], C1['moved'], C1['moved'], C1['readable'])),
        '',
        ('**THE PARTITION, WHICH IS A PARTITION AND NOT A COUNT.** **`%d` ON THE DRIVE** — each '
         'naming at least one repository the drive holds *as a git repository*, a directory not '
         'being a repository and the test being a `.git` inside it. **`%d` NAMES NO TERMINAL** — '
         '`ENUMERA`, whose own text says `HELD` and which names no repository at all, so there is '
         'nothing for a clone to reach. The parts sum to `%d` and the population is `%d`. **`(L1)` '
         'asked for at least four and the measurement is `%d`.**'
         % (C1['part'].get('ON THE DRIVE', 0), C1['part'].get('NAMES NO TERMINAL', 0),
            sum(C1['part'].values()), C1['rows'], C1['readable'])),
        '',
        ('**THE FOUR ROUTES, PRICED IN WHAT THEY BUY.** **Route A, clone what is clonable: reaches '
         '`0` further** — everything nameable is already here. **Route B, a ruling that reading a '
         'branch is reading: reaches `0` as a reading route** — the held branches are already in '
         'the local refs, so no ruling is needed to *read* them; a ruling is needed to *grade* '
         'them, which is a different question and stays the author’s. **Route C, accept the '
         'ceiling: refuted by the measurement.** **Route D, which the order did not pose — repair '
         'the predicate: reaches `%d`, and its whole cost is one matcher.** *A route that reaches '
         'zero is reported as reaching zero and is not padded*, and **the cheapest route was not '
         'on the list because the list inherited b394’s premise.** **`(L2)` holds**: no '
         'single route reaches all eleven, because `ENUMERA` names nothing for any route to reach '
         'and what it needs is an author.'
         % C2['best']),
        '',
        ('**THE FEDERATION, READ LIVE, WITH ITS AMBIGUITY NAMED.** The corpus names **`%d`** '
         'federation repositories, found by content across the tree and not from a typed roster; '
         'the drive holds **`%d`** as git repositories and unauthenticated `ls-remote` resolves '
         'the same **`%d`**. **Both controls ran before any figure was read off the survey** — a '
         'positive that must resolve and a negative that must not — because without them a survey '
         'of zeroes and a broken route look the same. **A negative is `ABSENT-OR-PRIVATE`, never '
         '`ABSENT`.** And **one read is not a measurement**: an earlier form of this survey '
         'returned `ABSENT-OR-PRIVATE` for `SIDE-archimedean` — a repository the drive holds and '
         'the account carries — on a transient `code 128`, so every negative is now re-read. **The '
         'ceiling is a fact about the working machine**: the `%d` names the drive does not hold '
         'are not a defect in the corpus and no document is graded down for them.'
         % (len(S2['names']), len(S2['on_drive']), len(S2['resolves']),
            len(S2['names']) - len(S2['on_drive']))),
        '',
        ('**RULING (R21), EXECUTED — AND EXECUTED IN THE ROW, NOT ONLY IN A FOOTNOTE.** The '
         '**Simplicity / RH cascade** cluster is re-anchored to `PATHS_TO_THE_CRITICAL_LINE` on '
         'the measure b393 printed: **19 pins at 2026-08-10** against `SIMPLICITY_OF_RIEMANN_ZEROS` '
         'at **13 pins at 2026-08-09**. **The prior anchor is retained as a named member and is '
         'not demoted**; the pre-edit cell is carried inside the post-edit one word for word, so '
         '`%d` members are dropped. `git` reports **`+%d / -%d`** and the deletion is the edited '
         'row itself — **`%d` pre-act lines have content gone from the file**, because the '
         'pre-edit row is preserved **verbatim** in the appended block, per this document’s '
         'own precedent. The preserved quotation of the superseded table at line `%d` is '
         'byte-identical, and **`%d` of `%d` other table rows are unchanged**. *Why one moved and '
         'four did not* is stated beside the change: only this cluster answered the anchor '
         'question, and **you cannot overtake an anchor that was never named.**'
         % (0, A1['added'], A1['deleted'], A1['lost'], A1['quoted_line'],
            A1['others_same'], A1['others'])),
        '',
        ('**THE TWO DEPOSITED RECORDS: ONE DRAFTED, NEITHER WRITTEN.** For `21432399` the one-line '
         'historical note is **drafted in the bank and written nowhere**, with what it would fix '
         'and what it would not stated apart — it discharges `(R20)`’s currency obligation '
         '*in the corpus*, and it does not answer *is this DOI safe to cite*, because **the '
         'obligation is satisfied in the corpus and tested at the platform**. For `19675356` the '
         'deposited version is recorded **nowhere in the corpus** — re-read by content across the '
         'whole tree, not in one ledger, because *absence from one file is not absence from the '
         'corpus* — and the smallest recovering read is named: one authenticated fetch of that '
         'record’s own file manifest. **This seat cannot perform it**, and it does not infer '
         'the version from repository dates: *a halt reported is worth more than an answer '
         'substituted.*'),
        '',
        ('**THE TWO ANCHORLESS CLUSTERS, MEASURED AND DECIDED BY NOBODY.** `cross-domain`’s '
         'two members name **`%d`** document(s) in common; `theory-space`’s name **`%d`**, '
         'and their opening lines are about different objects — one a book on the constancy '
         'structure of two generators, the other asking how much of mathematics is classification. '
         '**They were put in one cluster by reclassification and not by being written for one.** '
         'Whether each reads as a *subject* or as a *destination* is the author’s question, '
         'and **a zero is evidence for an answer, not an answer**: `0` syntheses written, `0` '
         'anchors invented, `0` clusters reshaped beyond `(R21)`’s one. **Both routed.** '
         '**The four lists stay OPEN by name.** **Nothing deposits and the platform was not called '
         'at all.**'
         % (A3['cross-domain']['shared'], A3['theory-space']['shared'])),
        '',
    ]


def corr_rows(Q):
    m = ("**THE CEILING WAS AN ARTEFACT OF A MATCHER: TEN OF THE ELEVEN KEYSTONES b394 CALLED "
         "UNREACHABLE ARE READABLE WITHOUT A CLONE, AND (R21) IS EXECUTED IN THE MAP** (b395, the "
         "ceiling answered)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b395, %d gates read and %d checked "
            "by digest. b394 REPORTED ELEVEN KEYSTONES UNREACHABLE, 9 OF THEM BECAUSE NO KERNEL "
            "REPOSITORY THEY NAME IS ON THE DRIVE; THAT WAS A PROPERTY OF ITS MATCHER, WHICH "
            "RECOGNISED A BACKTICKED LOWERCASE NAME AND NOTHING ELSE. WIDENED, THE YIELD CHANGES "
            "FOR %d OF THE ELEVEN AND THE DRIVE HOLDS A NAMED REPOSITORY FOR %d OF THE %d b394 "
            "SAID IT HELD NONE FOR, EVERY ONE RESOLVING A HEAD LOCALLY. **b394's FACE AND BANK ARE "
            "LOCKED AND UNEDITED AND BOTH FIGURES ARE PRINTED** -- A PREDICATE THAT KNOWS ONE "
            "SHAPE FINDS ONE SHAPE. THE PARTITION IS %d ON THE DRIVE AND %d NAMES NO TERMINAL, "
            "SUMMING TO %d, so (L1) ASKED FOR FOUR AND THE MEASUREMENT IS %d. FOUR ROUTES ARE "
            "PRICED IN WHAT THEY BUY: CLONE 0, A BRANCH-READING RULING 0 AS A READING ROUTE, "
            "ACCEPTING THE CEILING REFUTED, AND A FOURTH THE ORDER DID NOT POSE -- REPAIR THE "
            "PREDICATE -- %d. A ROUTE THAT REACHES ZERO IS REPORTED AS REACHING ZERO AND IS NOT "
            "PADDED. (L2) HOLDS BECAUSE ENUMERA NAMES NO TERMINAL FOR ANY ROUTE TO REACH. THE "
            "FEDERATION WAS READ LIVE WITH BOTH CONTROLS FIRST: %d NAMES, %d ON THE DRIVE, %d "
            "RESOLVING, AND EVERY NEGATIVE RE-READ BECAUSE ONE READ IS NOT A MEASUREMENT. (R21) IS "
            "EXECUTED IN THE ROW ITSELF AND ADDITIVELY: +%d/-%d, 0 MEMBERS DROPPED, %d PRE-ACT "
            "LINES WITH CONTENT GONE, THE PRE-EDIT ROW PRESERVED VERBATIM, THE PRESERVED QUOTATION "
            "UNTOUCHED AND %d OF %d OTHER TABLE ROWS UNCHANGED"
            % (LG['gates_read'], LG['face_subject_gates'], C1['widened'], C1['moved'],
               C1['moved'], C1['part'].get('ON THE DRIVE', 0),
               C1['part'].get('NAMES NO TERMINAL', 0), sum(C1['part'].values()),
               C1['readable'], C2['best'], len(S2['names']), len(S2['on_drive']),
               len(S2['resolves']), A1['added'], A1['deleted'], A1['lost'],
               A1['others_same'], A1['others']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN. ### The eleven keystones' own text "
            "was read and the repositories they name were resolved on this drive by HEAD and ref "
            "count. ### NO KERNEL WAS OPENED, NO STATEMENT PROVED, NO BUILD RUN, NO REPOSITORY "
            "CLONED AND NO BRANCH FETCHED MERGED PUSHED OR CREATED -- NAMING A REPOSITORY THE "
            "DRIVE HOLDS IS NOT BUILDING IT. ### READING A TERMINAL IS NOT VERIFYING IT")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT "
            "THE OBJECT. ### NO GRADE MOVED, NO CLAIM WITHDRAWN, NO CORRESPONDENCE TABLE WRITTEN "
            "EXTENDED OR RE-GRADED, NO CLASS RULED, NO DOCUMENT RECLASSIFIED OR PLACED IN Tier KC, "
            "NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO LIST CLOSED, NO SYNTHESIS WRITTEN "
            "AND NO ANCHOR INVENTED. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL")
    grade = ("### EVERY MATCHER'S YIELD IS PRINTED INCLUDING b394'S OWN. ### THE PARTITION'S PARTS "
             "SUM TO THE POPULATION. ### READABLE WITHOUT A CLONE IS DEMONSTRATED BY A LOCAL HEAD "
             "AND REF COUNT, NOT ASSERTED. ### THE RESIDUE OF NON-REPOSITORY TOKENS IS HAND-READ "
             "AND NAMED APART. ### BOTH LIVE-READ CONTROLS RAN AND DISCRIMINATED. ### b394'S "
             "LOCKED FIGURE AND THIS ACT'S CORRECTED ONE ARE BOTH PRINTED AND THE DEFECTIVE "
             "PREDICATE IS NAMED. ### THE THREE DELETION FIGURES ARE ALL PRINTED AND numstat'S -1 "
             "IS NOT SUPPRESSED")
    status = ("data/b395_the_ceiling_answered.txt; data/%s; data/%s; "
              "data/b395_registration_2026-09-09.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b395); tools/b395_extract.py; tools/b395_regspec.py; "
              "tools/b395_reg_gate.py; tools/b395_components.py; tools/b395_desk_bank.py; "
              "tools/b395_checks.py; PLACE-papers SPIRAL_MAP.md (one anchor cell and one appended "
              "(R21) block) and OPEN_TRAILS.md (an append-only block); "
              "CORRESPONDENCE.md row %%d" % (AC['run_file'], E['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('can the unreachable keystones be read', 'was b394 wrong about the ceiling',
           'how many federation repositories does the drive hold',
           'which cluster was re-anchored', 'what does a route that reaches zero cost')
MUST_NOT_HIT = ('the ceiling was real', 'a synthesis was written',
                'an anchor was invented', 'the platform was called')


def do_key(rownum):
    KEY = 'the-ceiling-answered'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b395 TESTED b394's CEILING AND IT WAS AN ARTEFACT OF b394's OWN MATCHER. b394 REPORTED "
        "ELEVEN KEYSTONES UNREACHABLE, 9 BECAUSE NO KERNEL REPOSITORY THEY NAME IS ON THE DRIVE; "
        "ITS MATCHER RECOGNISED A BACKTICKED LOWERCASE NAME AND NOTHING ELSE. WIDENED, THE YIELD "
        "CHANGES FOR %d OF THE ELEVEN AND THE DRIVE HOLDS A NAMED REPOSITORY FOR %d OF THE %d IT "
        "SAID IT HELD NONE FOR, EVERY ONE RESOLVING A HEAD LOCALLY WITH ITS HELD BRANCHES IN THE "
        "LOCAL REFS. b394's FACE AND BANK ARE LOCKED AND UNEDITED AND BOTH FIGURES ARE PRINTED -- "
        "A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE. THE PARTITION IS %d ON THE DRIVE AND %d "
        "NAMES NO TERMINAL, SUMMING TO %d, SO (L1) ASKED FOR FOUR AND THE MEASUREMENT IS %d. FOUR "
        "ROUTES ARE PRICED IN WHAT THEY BUY: CLONE REACHES 0 FURTHER, A BRANCH-READING RULING "
        "REACHES 0 AS A READING ROUTE, ACCEPTING THE CEILING IS REFUTED, AND A FOURTH THE ORDER "
        "DID NOT POSE -- REPAIR THE PREDICATE -- REACHES %d AT THE COST OF ONE MATCHER. (L2) HOLDS "
        "BECAUSE ENUMERA NAMES NO TERMINAL FOR ANY ROUTE TO REACH. THE FEDERATION WAS READ LIVE "
        "WITH BOTH CONTROLS FIRST: THE CORPUS NAMES %d, THE DRIVE HOLDS %d AND THE ACCOUNT "
        "RESOLVES THE SAME %d, WITH EVERY NEGATIVE RE-READ AND REPORTED ABSENT-OR-PRIVATE NEVER "
        "ABSENT. (R21) IS EXECUTED IN THE MAP ROW ITSELF AND ADDITIVELY, THE PRIOR ANCHOR RETAINED "
        "AND NOT DEMOTED, WITH THE PRE-EDIT ROW PRESERVED VERBATIM. THE NOTE FOR 21432399 IS "
        "DRAFTED AND WRITTEN NOWHERE; 19675356's DEPOSITED VERSION IS RECORDED NOWHERE IN THE "
        "CORPUS AND THE SMALLEST RECOVERING READ IS NAMED. NEITHER ANCHORLESS CLUSTER IS DECIDED."
        % (C1['widened'], C1['moved'], C1['moved'], C1['part'].get('ON THE DRIVE', 0),
           C1['part'].get('NAMES NO TERMINAL', 0), sum(C1['part'].values()), C1['readable'],
           C2['best'], len(S2['names']), len(S2['on_drive']), len(S2['resolves'])))
    grade = (
        "### NO GRADE WAS MOVED, NO CLAIM WITHDRAWN, NO CORRESPONDENCE TABLE WRITTEN EXTENDED OR "
        "RE-GRADED, NO CLASS RULED, NO DOCUMENT RECLASSIFIED OR PLACED IN Tier KC, NO REGISTRY ROW "
        "EDITED, THE CENSUS NOT EDITED, NO LIST CLOSED, NO SYNTHESIS WRITTEN, NO ANCHOR INVENTED. "
        "### THE ONLY CORPUS EDIT IS ONE ANCHOR CELL AND ONE APPENDED BLOCK IN SPIRAL_MAP.md. ### "
        "EVERY MATCHER'S YIELD IS PRINTED INCLUDING b394'S. ### THE PARTITION'S PARTS SUM TO THE "
        "POPULATION. ### READABLE WITHOUT A CLONE IS DEMONSTRATED, NOT ASSERTED. ### BOTH "
        "LIVE-READ CONTROLS RAN. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### "
        "NO BUILD RUN AND NO REPOSITORY CLONED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. "
        "### M-2 UNCHANGED")
    where = (
        "data/b395_the_ceiling_answered.txt; data/%s; data/%s; "
        "data/b395_registration_2026-09-09.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b395 -- %d gates read, %d checked by digest); "
        "tools/b395_extract.py; tools/b395_regspec.py; tools/b395_reg_gate.py; "
        "tools/b395_components.py; tools/b395_desk_bank.py; tools/b395_checks.py; "
        "PLACE-papers SPIRAL_MAP.md and OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ('b395 (the ceiling was an artefact of a matcher: ten of the eleven keystones '
           'b394 called unreachable are readable without a clone)')
    row_new = ('    # ### THE CEILING ANSWERED (b395).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where,
                  chr(10)))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-44s NO KEY before : %s' % (qq, pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + chr(10)
    ROW_ANCHOR = ('INDEX = [' + chr(10)
                  + '    # (key, act, one-line statement, grade as its own act recorded it, '
                    'location)' + chr(10))
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
    rec('  READ BACK : %s returns %d row(s)  %s' % (KEY, n, 'PASS' if good else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g = (not no_key(o)) and KEY in o
        ok = ok and g
        rec('    %-48s reaches the b395 key : %s' % (qq, g))
    for lbl, cond in (('the ceiling is called an artefact of a matcher',
                       'ARTEFACT OF b394' in out),
                      ('b394`s face is named locked and unedited',
                       'LOCKED AND UNEDITED' in out),
                      ('one shape finds one shape',
                       'A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE' in out),
                      ('the partition sums to the population', 'SUMMING TO' in out),
                      ('a route reaching zero says zero', 'REACHES 0 FURTHER' in out),
                      ('the unposed fourth route is named', 'THE ORDER DID NOT POSE' in out),
                      ('the negative is absent-or-private',
                       'ABSENT-OR-PRIVATE NEVER ABSENT' in out),
                      ('the prior anchor is retained and not demoted',
                       'RETAINED AND NOT DEMOTED' in out),
                      ('the note is drafted and written nowhere',
                       'DRAFTED AND WRITTEN NOWHERE' in out),
                      ('neither anchorless cluster is decided',
                       'NEITHER ANCHORLESS CLUSTER IS DECIDED' in out),
                      ('nothing deposits and the platform was not called',
                       'THE PLATFORM WAS NOT CALLED AT ALL' in out),
                      ('the lists are restated open', 'RESTATED OPEN BY NAME' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g = pre[qq] and no_key(o)
        ok = ok and g
        rec('    %-44s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def main():
    bar('=')
    rec('b395 -- THE DESK, THE LEDGER WRITES, AND THE BANK.')
    bar('=')
    bar()
    rec('  ### THE DESK UNDER (R7).')
    bar()
    Q = do_desk()

    rec()
    bar()
    rec('  ### THE TRAIL BLOCK, APPEND-ONLY.')
    bar()
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
        after = before
        tr = dict(appended_only=True, committed_prefix_intact=True, prior_present=True)
    else:
        rec('  ### the b394 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        committed = blob('OPEN_TRAILS.md')
        ao = after.startswith(before)
        pi = committed in after.replace(chr(13) + chr(10), chr(10))
        rec('  ### bytes %d -> %d ; append-only %s ; committed still a substring %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao, pi))
        subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)
        tr = dict(appended_only=ao, committed_prefix_intact=pi, prior_present=(PRIOR in before))
    seg = after.split(MARK, 1)[-1]
    tr['says_artefact'] = 'THE CEILING WAS NOT THERE' in seg
    tr['says_one_shape'] = 'a predicate that knows one shape finds one shape' in seg.lower()
    tr['says_locked_unedited'] = 'locked and are not edited' in seg
    tr['says_partition_sums'] = 'The parts sum to' in seg
    tr['says_zero_route'] = 'reaches `0` further' in seg
    tr['says_unposed'] = 'the order did not pose' in seg
    tr['says_ambiguity'] = 'ABSENT-OR-PRIVATE' in seg
    tr['says_retained'] = 'retained as a named member and is\nnot demoted' in seg or \
                          'retained as a named member' in seg
    tr['says_drafted'] = 'written nowhere' in seg
    tr['says_lists_open'] = 'four lists stay OPEN by name' in seg
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:** ### %s'
        % {k: v for k, v in tr.items() if k.startswith('says_')})

    rec()
    bar()
    rec('  ### THE CORRESPONDENCE ROW.')
    bar()
    ROWS = corr_rows(Q)
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe : %d' % len(bad))
    if bad or not (pos and neg and sa and sb and sc and sd):
        run_clock.write(D, 'b395_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b395_desk_notes', LINES)
        return 1
    nums = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    present = [mm for mm, _s, _t, _p, _g, _sc, _st in ROWS if mm in txt]
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
        cellsx = [GD.split_cells(t) for t in back.rstrip(chr(10)).split(chr(10))[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx)
               and back.startswith(txt.rstrip(chr(10))))
        rec('  READ BACK : last row %d ; cells %s ; true prefix %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(chr(10))),
               'PASS' if okr else '### FAIL ###'))
        if not okr:
            run_clock.write(D, 'b395_desk_notes', LINES)
            return 1
        rownum = start

    rec()
    bar()
    rec('  ### THE INDEX KEY.')
    bar()
    kok = do_key(rownum)

    rec()
    bar()
    rec('  ### THE BANK.')
    bar()
    B = []
    BAR, SUB = '=' * 100, '-' * 100
    B.append(BAR)
    B.append('b395 -- THE CEILING, ANSWERED OR PRICED. ### THE BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **THE CEILING WAS AN ARTEFACT OF A MATCHER, AND THE MATCHER WAS THIS')
    B.append('### ### ### SEAT`S OWN, ONE ACT AGO.**')
    B.append('')
    B.append(SUB)
    B.append('### WHAT `b394` SAID, AND WHAT PRODUCED IT.')
    B.append(SUB)
    B.append('### `b394` closed by reporting that ### **ELEVEN OF THE REMAINING TWELVE CANNOT')
    B.append('### ### BE READ BY THIS RULE AT ALL**, `9` of them because ### *no kernel')
    B.append('### repository it names is on the drive.*')
    B.append('### ### **THAT SENTENCE WAS PRODUCED BY A MATCHER THAT RECOGNISED A BACKTICKED')
    B.append('### ### LOWERCASE NAME AND NOTHING ELSE.**')
    B.append('### ### **WIDENED TO THE SAME NAME WRITTEN ANY OTHER WAY, THE YIELD CHANGES FOR')
    B.append('### ### `%d` OF THE ELEVEN**, and ### **THE DRIVE HOLDS A NAMED REPOSITORY FOR'
             % C1['widened'])
    B.append('### ### `%d` OF THE `%d` `b394` SAID IT HELD NONE FOR.**' % (C1['moved'],
                                                                          C1['moved']))
    B.append('### ### ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE** -- `b370``s')
    B.append('### ### ### lore, and this is the incident that proves it applies to the act')
    B.append('### ### ### that minted the ceiling.')
    B.append('### ### **`b394``S FACE AND BANK ARE LOCKED AND ARE NOT EDITED.** ### Both')
    B.append('### ### figures stand: `b394` said ELEVEN UNREACHABLE and this act measures')
    B.append('### ### ### **`%d` OF THE ELEVEN READABLE WITHOUT A CLONE.**' % C1['readable'])
    B.append('')
    B.append(SUB)
    B.append('### THE PARTITION. ### **A PARTITION, NOT A COUNT.**')
    B.append(SUB)
    for w, n in sorted(C1['part'].items(), key=lambda z: -z[1]):
        B.append('###   %-22s ### **`%d`**' % (w, n))
    B.append('### ### **THE PARTS SUM TO `%d`; THE POPULATION IS `%d`; EQUAL : %s.**'
             % (sum(C1['part'].values()), C1['rows'], C1['sums']))
    B.append('### ### **AND `READABLE WITHOUT A CLONE` IS DEMONSTRATED, NOT ASSERTED:** ### for')
    B.append('### ### every named repository the drive holds, this act read its `HEAD` and')
    B.append('### ### counted the refs already present, including the branches a held or')
    B.append('### ### unmerged terminal would live on.')
    B.append('### ### **`(L1)` ASKED FOR AT LEAST FOUR. ### THE MEASUREMENT IS `%d`. ### MET.**'
             % C1['readable'])
    B.append('')
    B.append(SUB)
    B.append('### THE FOUR ROUTES, PRICED IN WHAT THEY BUY.')
    B.append(SUB)
    B.append('###   ROUTE A  clone what is clonable                  ### **REACHES `0` FURTHER**')
    B.append('###   ROUTE B  a ruling that reading a branch is reading ### **REACHES `0`**')
    B.append('###   ROUTE C  accept the ceiling                      ### **REFUTED**')
    B.append('###   ROUTE D  UNPOSED -- repair the predicate         ### **REACHES `%d`**'
             % C2['best'])
    B.append('### ### **A ROUTE THAT REACHES ZERO IS REPORTED AS REACHING ZERO AND IS NOT')
    B.append('### ### PADDED.**')
    B.append('### ### **THE CHEAPEST ROUTE WAS NOT ON THE ORDER`S LIST BECAUSE THE ORDER')
    B.append('### ### INHERITED `b394``S PREMISE**, and the seat says so rather than choosing')
    B.append('### ### the best of three.')
    B.append('### ### **`(L2)` HOLDS:** ### no single route reaches all eleven, because')
    B.append('### ### `ENUMERA` names no terminal for any route to reach. ### **WHAT IT NEEDS')
    B.append('### ### IS AN AUTHOR NAMING ITS TERMINAL.**')
    B.append('')
    B.append(SUB)
    B.append('### THE FEDERATION, READ LIVE. ### **WITH ITS AMBIGUITY NAMED.**')
    B.append(SUB)
    B.append('### ### **NAMES THE CORPUS CARRIES : `%d`** ### -- found by content across the'
             % len(S2['names']))
    B.append('### tree and not from a roster this seat typed.')
    B.append('### ### **THE DRIVE HOLDS `%d` AS GIT REPOSITORIES.**' % len(S2['on_drive']))
    B.append('### ### **THE ACCOUNT RESOLVES `%d` UNAUTHENTICATED**, and it is the same `%d`.'
             % (len(S2['resolves']), len(S2['both'])))
    B.append('### ### **BOTH CONTROLS RAN BEFORE ANY FIGURE WAS READ OFF THE SURVEY : %s**'
             % S2['controls']['ok'])
    B.append('### ### -- a positive that must resolve and a negative that must not, because')
    B.append('### ### **WITHOUT THEM A SURVEY OF ZEROES AND A BROKEN ROUTE LOOK THE SAME.**')
    B.append('### ### **A NEGATIVE IS `ABSENT-OR-PRIVATE`, NEVER `ABSENT`.**')
    B.append('### ### **AND ONE READ IS NOT A MEASUREMENT:** ### an earlier form of this')
    B.append('### ### survey returned `ABSENT-OR-PRIVATE` for `SIDE-archimedean` -- a')
    B.append('### ### repository the drive holds and the account carries -- on a transient')
    B.append('### ### `code 128`. ### **EVERY NEGATIVE IS NOW RE-READ.**')
    B.append('### ### **THE CEILING IS A FACT ABOUT THE WORKING MACHINE:** ### the `%d` names'
             % (len(S2['names']) - len(S2['on_drive'])))
    B.append('### ### the drive does not hold are ### **NOT A DEFECT IN THE CORPUS**, and no')
    B.append('### ### document is graded down for them.')
    B.append('')
    B.append(SUB)
    B.append('### RULING `(R21)`, EXECUTED. ### **IN THE ROW, NOT ONLY IN A FOOTNOTE.**')
    B.append(SUB)
    B.append('### ### **THE `Simplicity / RH cascade` CLUSTER IS RE-ANCHORED TO')
    B.append('### ### `PATHS_TO_THE_CRITICAL_LINE`** ### on the measure `b393` printed: `19`')
    B.append('### pins at `2026-08-10` against `SIMPLICITY_OF_RIEMANN_ZEROS` at `13` pins at')
    B.append('### `2026-08-09`.')
    B.append('### ### **THE PRIOR ANCHOR IS RETAINED AS A NAMED MEMBER AND IS NOT DEMOTED :')
    B.append('### ### %s** ### -- the pre-edit cell is carried inside the post-edit one word'
             % A1['prior_kept'])
    B.append('### ### for word, so ### **`0` MEMBERS ARE DROPPED.**')
    B.append('### ### **THE ANCHOR IS MOVED IN THE ROW ITSELF AND NOT ONLY IN THE APPENDED')
    B.append('### ### BLOCK**, because ### **A CORRECTION THAT DOES NOT PROPAGATE IS A')
    B.append('### ### CORRECTION IN ONE PLACE AND A DEFECT EVERYWHERE ELSE** -- this seat`s')
    B.append('### ### own species, and a re-anchoring recorded only in a footnote leaves the')
    B.append('### ### table saying the old thing to every later reader.')
    B.append('### ### **THE THREE DELETION FIGURES, ALL PRINTED:**')
    B.append('###   `git numstat` deletions                             ### **`%d`**'
             % A1['deleted'])
    B.append('###   pre-act lines not present verbatim as a whole line   ### **`%d`**'
             % A1['changed'])
    B.append('###   ### **PRE-ACT LINES WHOSE CONTENT IS GONE FROM THE FILE : `%d`**'
             % A1['lost'])
    B.append('### ### **THE FACE`S BAR IS A PRESERVATION BAR AND THE THIRD FIGURE TESTS IT** --')
    B.append('### ### the changed row survives ### **VERBATIM INSIDE THE APPENDED QUOTATION**,')
    B.append('### ### and ### **`numstat``S `-1` IS PRINTED HERE AND NOT SUPPRESSED**, because')
    B.append('### ### an in-place edit of one line is one deletion to `git` and no loss to a')
    B.append('### ### reader, and ### **AN ARM MUST TEST THE BAR ITS FACE ACTUALLY SET**')
    B.append('### ### (`b390`).')
    B.append('### ### **THE PRESERVED QUOTATION AT LINE `%d` IS BYTE-IDENTICAL : %s.**'
             % (A1['quoted_line'], A1['quote_ok']))
    B.append('### ### **OTHER TABLE ROWS UNCHANGED : `%d` OF `%d`.**'
             % (A1['others_same'], A1['others']))
    B.append('### ### **WHY ONE MOVED AND FOUR DID NOT**, stated beside the change: only this')
    B.append('### ### cluster answered the anchor question. ### Of the other four, one returned')
    B.append('### ### `ANCHOR NOT A CENSUS KEYSTONE`, one `MEMBERSHIP ONLY`, and two `NO')
    B.append('### ### ANCHOR NAMED` -- ### **AND YOU CANNOT OVERTAKE AN ANCHOR THAT WAS NEVER')
    B.append('### ### NAMED.**')
    B.append('')
    B.append(SUB)
    B.append('### THE TWO DEPOSITED RECORDS. ### **ONE DRAFTED. ### NEITHER WRITTEN.**')
    B.append(SUB)
    B.append('### **`21432399`** ### -- the one-line historical note, ### **DRAFTED:**')
    B.append('###   > %s' % AC['note'])
    B.append('### ### **IT IS WRITTEN NOWHERE AND THE PLATFORM WAS NOT CALLED.**')
    B.append('### **WHAT IT WOULD FIX:** ### a reader of the record learns from the record')
    B.append('### itself that the deposited manuscript is not the current one and that the')
    B.append('### difference is deliberate. ### It discharges `(R20)``s currency obligation')
    B.append('### ### **IN THE CORPUS.**')
    B.append('### **WHAT IT WOULD NOT FIX:** ### it does not answer ### *is this DOI safe to')
    B.append('### cite*, because ### **THE OBLIGATION IS SATISFIED IN THE CORPUS AND TESTED AT')
    B.append('### ### THE PLATFORM.** ### **A NOTE ABOUT A DEPOSIT IS NOT A DEPOSIT.**')
    B.append('### **`19675356`** ### -- ### **THE VERSION IT WAS DEPOSITED AT IS RECORDED')
    B.append('### ### NOWHERE IN THE CORPUS**, re-read by content across the whole tree and not')
    B.append('### in one ledger, because ### **ABSENCE FROM ONE FILE IS NOT ABSENCE FROM THE')
    B.append('### ### CORPUS.**')
    B.append('### **THE SMALLEST READ THAT WOULD RECOVER IT:** ### one authenticated fetch of')
    B.append('### that record`s own file manifest, compared against the repository`s history.')
    B.append('### ### **ONE RECORD, ONE READ, NO CRAWL.**')
    B.append('### **WHO CAN PERFORM IT:** ### ### **NOT THIS SEAT.** ### `b389` proved the')
    B.append('### platform answers on none of six routes from here with a positive control at')
    B.append('### `200`, and this act does not call it at all. ### **A HALT REPORTED IS WORTH')
    B.append('### ### MORE THAN AN ANSWER SUBSTITUTED**, and the version is not inferred from')
    B.append('### the repository`s dates.')
    B.append('')
    B.append(SUB)
    B.append('### THE TWO ANCHORLESS CLUSTERS. ### **MEASURED. ### DECIDED BY NOBODY.**')
    B.append(SUB)
    B.append('### **`cross-domain`** ### -- its two members name ### **`%d`** ### document(s)'
             % A3['cross-domain']['shared'])
    B.append('### in common. ### **THERE IS SOMETHING FOR A SYNTHESIS TO BE ABOUT**, and ###')
    B.append('### **THAT IS EVIDENCE FOR A SYNTHESIS AND IS NOT A SYNTHESIS.**')
    B.append('### **`theory-space`** ### -- its two members name ### **`%d`** ### in common,'
             % A3['theory-space']['shared'])
    B.append('### and their opening lines are about different objects. ### **THEY WERE PUT IN')
    B.append('### ### ONE CLUSTER BY RECLASSIFICATION AND NOT BY BEING WRITTEN FOR ONE.**')
    B.append('### ### **AND A ZERO IS EVIDENCE FOR AN ANSWER, NOT AN ANSWER.** ### `0`')
    B.append('### ### syntheses written, `0` anchors invented, `0` clusters reshaped beyond')
    B.append('### ### `(R21)``s one. ### **BOTH ROUTED TO THE AUTHOR.**')
    B.append('')
    B.append(SUB)
    B.append('### THE DESK, AND WHAT THIS ACT DOES NOT DO.')
    B.append(SUB)
    B.append('### ### **ITEMS SWEPT `%d` ; CLOSED `%d` ; STANDING `%d`.**'
             % (Q['items'], Q['closed'], Q['standing']))
    B.append('### ### **ONE ITEM IS CLOSED BY BEING DISPROVED** -- the eleven unreachable')
    B.append('### ### keystones -- and ### **CLOSING IT MAKES A STANDING ITEM BIGGER:** ### the')
    B.append('### ### work is ### **AVAILABLE AND NOT DONE**, which is a larger debt than')
    B.append('### ### blocked.')
    B.append('### ### **AND A NEW ITEM OPENS THAT NOBODY HAS MEASURED:** ### the matcher is')
    B.append('### ### repaired in this act`s own tool and ### **NO SWEEP HAS BEEN RUN FOR THE')
    B.append('### ### SAME SHAPE ELSEWHERE IN THE RECORD.** ### **HOW MANY OTHER FINDINGS REST')
    B.append('### ### ON A BACKTICK IS UNMEASURED.**')
    B.append('### ### **THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME AND THIS ACT CLOSES')
    B.append('### ### NONE.**')
    B.append(SUB)
    B.append('### WHAT THIS BANK WAS MADE FROM. ### **NAMED, SO A READER CAN RE-RUN IT.**')
    B.append(SUB)
    B.append('### ### **THE FACE, LOCKED BEFORE ANY WRITE:**')
    B.append('###   `data/b395_registration_2026-09-09.txt`')
    B.append('###   sha256 `%s`' % SEALHASH)
    B.append('###   locked at `%s` (UTC)' % SEALSTAMP)
    B.append('### ### **THE LOCK GATE:** ### `tools/b378_lockgate.py` run as `b395` -- ###')
    B.append('### **`%d` GATES READ, `%d` PASSING, `%d` CHECKED BY DIGEST.**'
             % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    B.append('### ### **THE RUN RECORDS, EACH RESOLVED BY ITS OWN RECORDED CLOCK** (`b358`):')
    B.append('###   the extract and its four surveys   `data/%s`  `%s`'
             % (E['run_file'], E['run_clock']))
    B.append('###   the components and `(R21)`         `data/%s`  `%s`'
             % (AC['run_file'], AC['run_clock']))
    B.append('### ### **AND THE LEDGER WRITES:** ### `CORRESPONDENCE.md` row `%d`; the'
             % rownum)
    B.append('### ### `OPEN_TRAILS.md` block marked `%s`; the index key' % MARK)
    B.append('### ### `the-ceiling-answered`.')
    B.append('')
    B.append(SCOPE)
    B.append('')
    B.append(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### THE CEILING WAS REAL.', '### A ROUTE WAS PADDED.',
                '### A CLUSTER WAS RESHAPED.', '### A SYNTHESIS WAS WRITTEN.',
                '### AN ANCHOR WAS INVENTED.', '### A MEMBER WAS DEMOTED.',
                '### THE NOTE WAS WRITTEN.', '### THE PLATFORM WAS CALLED.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))
    rec()
    bar('=')
    rec('  ### desk %d ; closed %d ; trail %s ; row %s ; key %s'
        % (Q['items'], Q['closed'], tr['appended_only'], rownum, kok))
    bar('=')
    p = run_clock.write(D, 'b395_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             bank='b395_the_ceiling_answered.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b395_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
