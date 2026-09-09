# -*- coding: utf-8 -*-
"""b393_desk_bank.py -- THE DESK, THE LEDGER WRITES, AND THE BANK FOR LEG 1.

### ### **THIS ACT EDITS NO CORPUS DOCUMENT.** ### Its product is a list the closing
### message prints. ### This file writes the ledgers
### and the bank, and closes what `(R7)` permits.
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
MARK = '<!-- b393 the five clusters surfaced; the two records priced; Tier KC priced -->'
PRIOR = ('<!-- b392 the two rulings written: (R19) the finished keystone, (R20) the deposit rule -->')

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


AC = J('b393_components')
LG = J('b393_lockgate')
E = J('b393_reads')
C1, C2, C3 = AC['c1'], AC['c2'], AC['c3']
BANKOUT = os.path.join(D, 'b393_the_clusters_surfaced.txt')


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
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND',
     '### **OPEN -- AND THIS ACT SHARPENED ONE OF ITS MEMBERS.** ### `19675356` is named ONLY as '
     'a bibliography entry, and this act now knows why that matters: ### **THE CORPUS RECORDS '
     'WHAT WAS DEPOSITED AND WHERE, AND NOT AT WHAT VERSION**'),
    ('the three amendments b383 drafted that are still routed', 'STAND', 'ROUTED AND UNAPPLIED'),
    ('the download-layer book`s registry drift', 'STAND', "OPEN AND THE AUTHOR`S"),
    ('the six subject clusters with no keystone', 'STAND', '`NOT-YET-SYNTHESIZED` since b385'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', 'NOT RE-MEASURED'),
    ('the ten untracked run records of earlier acts', 'STAND', 'NAMED at b382, STILL UNTRACKED'),
    ('the legacy `.git/hooks/pre-push` copies', 'STAND', '### **RULED BY `(R16)`: THEY STAY**'),
    ('the untracked `.b304-backup` artifacts', 'STAND', 'NAMED at b386, still untracked'),
    ('the five keystones the union names that carry no correspondence table', 'STAND',
     'NAMED at b387 and ### **STILL THE AUTHOR`S**'),
    ('the 23 unreadable correspondence rows', 'STAND', 'NAMED at b388 by cause, and ROUTED'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the keystone-class documents b388 marked UNASSIGNED', 'STAND',
     '### **UNASSIGNED IS A STATE AND NOT A DEBT**'),
    ('the deposited layer, unread since b389', 'STAND',
     'STILL BLOCKED; this act did not ask the platform'),
    ('the eight-versus-six cluster-synthesis disagreement', 'STAND', 'ROUTED at b389'),
    ('the fifteen keystones not read', 'STAND',
     'PRICED at b390. ### **`b394` READS THREE OF THEM**, which is this leg`s successor and not '
     'this leg'),
    ('the practice that let the phantom drift run', 'STAND',
     'NEW at b391 and ### **STILL OPEN**: nothing checks a cited version against its target'),
    ('the `66` superseded version citations', 'STAND', 'REPORTED at b391 and LEFT'),
    ('`CONSTANCE.md` carries no version in its own bytes', 'STAND', 'ROUTED at b391'),
    ('placement into `Tier KC`', 'STAND',
     '### **PRICED AT b393 AND STILL EMPTY.** ### The obligation has ### **THREE LIMBS AND THE '
     'RECORD ANSWERS ONE**; the coverage limb is the same work `b390` priced at half an hour a '
     'document; and ### **`b382` RULED A CLASS RULING RESTS ON DECLARATION**, which no document '
     'carries for a class one day old. ### **THAT LAST IS A GATE, NOT A COST**'),
    ('whether `SIDE-kernel` has a current citable record', 'STAND', 'ROUTED at b392 as a question'),

    # ---- WHAT THIS ACT ADDS ---------------------------------------------------------------------
    ('the five clusters, now surfaced to the navigator', 'CLOSE',
     '### **NEW at b393 AND CLOSED BY `(R7)`: THE OCCASION IS GONE.** ### The item was that '
     '`b388` found them and `b391` reported them and ### **NEITHER PUT THEM IN FRONT OF THE '
     'NAVIGATOR.** ### They are printed in this act`s closing message, named, with what changed '
     'and a quotation apiece. ### **THE RESHAPING REMAINS THE AUTHOR`S AND IS A DIFFERENT ITEM, '
     'WHICH STANDS**'),
    ('the cluster reshaping, with the five named', 'STAND',
     '### **STANDING, AND NOW ACTIONABLE.** ### All five changed by ### **MEMBERSHIP**; `1` by '
     '### **ANCHOR** ### (`Simplicity / RH cascade`, overtaken by `PATHS_TO_THE_CRITICAL_LINE`); '
     '`1` is anchored on documents the census does not list; and ### **`2` HAVE NO ANCHOR AT '
     'ALL.** ### **THE RESHAPING IS THE AUTHOR`S**'),
    ('the two deposited records` remediation', 'STAND',
     '### **PRICED AT b393, NOT PERFORMED.** ### `21432399` can be given a historical note in '
     '### **ONE LINE TODAY**, because its version is known. ### **`19675356` CANNOT BE GIVEN A '
     'CURRENT-VERSION REMEDY AT ALL** ### until something records what it was deposited at -- '
     'the corpus does not, and the platform does not answer. ### **NEITHER IS RECOMMENDED; THE '
     'CHOICE IS THE AUTHOR`S**'),
    ('the anchor question, unanswerable for three of five', 'STAND',
     '### **NEW at b393: `2` CLUSTERS HAVE NO ANCHOR AND `1` IS ANCHORED OUTSIDE THE CENSUS.** '
     '### A reader meeting those two meets ### **A MEMBER LIST**, and in the third ### **THE '
     'ANCHOR AND THE MEMBERSHIP ARE GRADED ON DIFFERENT SCALES.** ### **ROUTED**'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES ONE ITEM AND OPENS THREE.** ### `(R7)` closes an item whose')
    rec('    ### occasion is gone, and the occasion here was that two acts found the five clusters')
    rec('    ### and neither surfaced them. ### **THEY ARE SURFACED, SO THE ITEM HAS NOTHING LEFT')
    rec('    ### ### TO CARRY.**')
    rec('    ### ### ### **BUT SURFACING IS NOT RESHAPING**, and the reshaping stands as its own')
    rec('    ### ### ### item -- now with the five named and the anchor question answered where it')
    rec('    ### ### ### could be answered.')
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
    rec('    ### ### **THREE ITEMS ARE ADDED AND ALL THREE STAND** -- because ### **A FINDING')
    rec('    ### ### RECORDED IS NOT A FINDING DISCHARGED**, and a class with no members is a')
    rec('    ### ### class with work still in front of it.')
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0, marks=marks)


SCOPE = (
    "**SCOPE: THE FIVE CLUSTERS SURFACED, AND TWO PRICINGS.** **THIS ACT EDITS NO CORPUS DOCUMENT "
    "AT ALL** -- its only writes are the two ledgers and its own relay files. NO cluster reshaped, "
    "split, merged, renamed or re-anchored; NO document placed in Tier KC and NO candidate named; "
    "NO class ruled, NO document reclassified, NO grade moved, NO claim withdrawn, NO registry row "
    "edited, NO standard edited, NO Correspondence row edited, NO list closed, NEITHER MAP'S (R18) "
    "HEAD NOTE TOUCHED, THE TAXONOMY AND THE DEPOSIT RULE NOT AMENDED. **NO KEYSTONE IS "
    "RECONCILED -- THAT IS b394's, AND A LEG DOES NOT REACH INTO THE NEXT LEG'S SCOPE.** **THE "
    "ANCHOR QUESTION WAS MEASURED FOR THE FIRST TIME**: b388 found the five clusters and b391 "
    "reported them and BOTH MEASURED MEMBERSHIP ONLY. The test ranks a gained census keystone "
    "against the best anchor by the census's own two figures, date and pin count, and ITS LIMIT IS "
    "STATED WITH IT -- it can only rank documents the census lists. **THE FIVE RETURN FOUR "
    "DIFFERENT ANSWERS AND THE FOUR ARE NOT ADDED**: 1 ANCHOR OVERTAKEN, 1 MEMBERSHIP ONLY, 1 "
    "ANCHOR NOT A CENSUS KEYSTONE, 2 NO ANCHOR NAMED. **THREE OF THE FOUR ARE WAYS OF NOT "
    "ANSWERING THE QUESTION AND ONLY ONE IS AN ANSWER TO IT**, so (L1) EXPECTED TWO AND IS "
    "REPORTED REFUTED -- AN UNANSWERABLE CASE IS NOT PROMOTED INTO AN AFFIRMATIVE ONE TO REACH "
    "TWO, and the locked face said the count was one before the component ran. **THE SCREEN WAS "
    "REPAIRED BEFORE ANY FINDING WAS FILED**, because its first form conflated THE ANCHOR IS NOT A "
    "KEYSTONE with THERE IS NO ANCHOR. **THE TWO RECORDS PRICE ASYMMETRICALLY AND NEITHER REMEDY "
    "IS RECOMMENDED**: 21432399 deposited the monograph at manuscript v5.8 while the repository "
    "carries v5.13, and can be given a historical note in ONE LINE TODAY because its version is "
    "known; 19675356 deposited The Silence of Foundations and THE VERSION IT WAS DEPOSITED AT IS "
    "NOT RECORDED ANYWHERE IN THE CORPUS, so it CANNOT BE GIVEN A CURRENT-VERSION REMEDY AT ALL "
    "without a read nobody can perform. **AND NEITHER REMEDY BUYS AN ANSWER TO 'IS THIS DOI SAFE "
    "TO CITE' WITHOUT A LIVE READ**, because the obligation is satisfied in the corpus and tested "
    "at the platform. **TIER KC IS PRICED AND NOT APPLIED**: its obligation has THREE LIMBS and "
    "THE RECORD ANSWERS ONE -- b387's 162 rows answer GRADE; PLACEMENT and COVERAGE are unheld; "
    "the one keystone b390 read whole WOULD FAIL THE PLACEMENT LIMB; and the application needs a "
    "DECLARATION b382 ruled a class ruling must rest on, WHICH IS A GATE AND NOT A COST. **THE "
    "CHEAP SWEEP'S FIGURES ARE A FLOOR AND NOT A VERDICT: A HEADING IS NOT A TABLE READ.** **THE "
    "FOUR OPEN LISTS ARE RESTATED OPEN BY NAME.** NOTHING DEPOSITS; NO DOI MINTED, CLAIMED OR "
    "EDITED; **THE PLATFORM WAS NOT CALLED AT ALL.** NO NEW TRACKING DOCUMENT WAS CREATED. NO "
    "ARCHIVE OR outputs FILE TOUCHED, THE MIRROR ROSTER NOT EDITED, NO .git/hooks/pre-push "
    "DELETED. NO .lean FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED. NOTHING IS CLAIMED "
    "ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing "
    "about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT "
    "MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; "
    "M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still "
    "unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's "
    "record. THE INSTRUMENT LANE STAYS PARKED. THE WAVE STAYS PARKED. THE POSTURE LOCK IS "
    "SEPARATE. h2 stands exactly where the deposit left it and this act makes no claim about it in "
    "either direction.")


def trail_block(Q):
    lines = [
        '', MARK, '',
        '### **b393 — THE FIVE CLUSTERS SURFACED, AND TWO PRICINGS (2026-09-09)**',
        '',
        ('*No block above is edited. The b392 block (`%s`) and every block before it stand exactly '
         'as they were written.*' % PRIOR),
        '',
        ('**TWO ACTS FOUND THE FIVE CLUSTERS AND NEITHER PUT THEM IN FRONT OF THE NAVIGATOR.** '
         '`b388` found them; `b391` reported them; **both measured membership only**. The order '
         'names five kinds of change and one of them — *anchor no longer the document a reader '
         'meets first* — **had never been tested**. It is tested here, by the census’s own two '
         'figures: **date and pin count**. A cluster changed by anchor if a member it gained is a '
         'census keystone **newer than the best anchor and carrying more pins**. **The test can '
         'only rank documents the census lists**, and where an anchor is not among the sixteen '
         'the question is **undecidable from the census** and is reported as that, not as a pass.'),
        '',
        ('**THE FIVE, WITH WHAT CHANGED IN EACH.**'),
        '',
    ]
    for s in C1['surfaced']:
        lines.append(
            '- **%s** — `%s` by `%d`. Gained %s. **The anchor question: %s.** *%s*'
            % (s['cluster'], s['finding'], s['by'],
               ', '.join('`%s`' % g for g in s['gained']),
               s['verdict'],
               ('`%s` is a census keystone that joined it' % s['keystones'][0])
               if s['keystones'] else 'no census keystone joined it'))
    lines += [
        '',
        ('**FOUR DIFFERENT ANSWERS TO ONE QUESTION, AND THEY ARE NOT ADDED.** `%d` **anchor '
         'overtaken**, `%d` **membership only**, `%d` **anchor not a census keystone**, `%d` **no '
         'anchor named at all**. **Three of the four are ways of not answering the anchor '
         'question and only one is an answer to it.** So **`(L1)` expected at least two and is '
         'reported REFUTED** — the locked face said the count was one before the component ran, '
         'and **an unanswerable case is not promoted into an affirmative one to reach two**.'
         % (C1['by_verdict'].get('ANCHOR OVERTAKEN', 0),
            C1['by_verdict'].get('MEMBERSHIP ONLY', 0),
            C1['by_verdict'].get('ANCHOR NOT A KEYSTONE', 0),
            C1['by_verdict'].get('NO ANCHOR NAMED', 0))),
        '',
        ('**AND THE SHAPE OF THE UNANSWERABLE IS THE PART WORTH THE AUTHOR’S TIME.** Two clusters '
         '**have no anchor at all** — `(R17)` named none and `b388` did not invent one — so **a '
         'reader meeting them meets a member list**. One is **anchored on documents the keystone '
         'census does not list** while a census keystone joined it, so **the anchor and the '
         'membership are now graded on different scales**. **No cluster is reshaped: the '
         'reshaping is the author’s and this is the read that precedes it.**'),
        '',
        ('**THE TWO RECORDS FAILING `(R20)`’S CURRENCY OBLIGATION, PRICED — AND THEY PRICE '
         'ASYMMETRICALLY.** `21432399` deposited the monograph at manuscript **`v5.8`** while the '
         'repository now carries **`v5.13`**, and the citable deposit is a different record '
         'entirely. It can be given **a historical note in one line today**, because its version '
         'is known; a new deposit would need **a whole wave** (`(R20)`’s first limb) and a '
         'platform that answers, and **would not retire the old record anyway** — the note would '
         'still be owed. `19675356` deposited *The Silence of Foundations*; the repository carries '
         '**`v2.3`**; and **the version it was deposited at is not recorded anywhere in the '
         'corpus**. Its note can only say that something old exists, and **a current-version '
         'remedy is blocked outright**: depositing without a read risks duplicating something already '
         'current, **a worse defect than the one it cures**. **Neither remedy buys an answer to '
         '“is this DOI safe to cite” without a live read**, because the obligation is satisfied '
         'in the corpus and tested at the platform. **Nothing is written at the platform and '
         'neither remedy is recommended.**'),
        '',
        ('**`Tier KC` IS PRICED AND STILL EMPTY, AND THE PRICE IS DOMINATED BY THE LIMB NOBODY '
         'HAS MEASURED.** The obligation has **three limbs** and **the record answers one**: '
         '`b387`’s **`%s` correspondence rows** across nine documents, **`%s` of them not '
         'machine-verified and labelled**, answer **grade**. **Placement** — *a table after the '
         'front matter, where a reader meets it* — is unheld: `b387` counted rows and never asked '
         'where they sit. **Coverage** — *every* load-bearing claim carried by a row — is unheld '
         'too, because **the record holds row counts and not claim counts**. And **the one '
         'keystone `b390` read whole would fail the placement limb**, with both its tables at the '
         'end and the standard’s below its provenance. Placement is minutes per document; '
         'coverage is **the same work `b390` priced at half an hour a document and called an '
         'underestimate**. **And the application needs a third thing that is not a cost at all: a '
         'DECLARATION**, which `b382` ruled a class ruling must rest on and which no document '
         'carries for a class one day old. **That is a gate, and no amount of measurement opens '
         'it.** **`0` documents placed, `0` candidates named.**'
         % (C3['rows'], C3['not_machine'])),
        '',
        ('**WHAT IS ROUTED.** *(1)* The **cluster reshaping**, now actionable with the five named '
         'and the anchor question answered where it could be. *(2)* The **two records’ '
         'remediation**, priced and not performed. *(3)* The **anchor question itself**, '
         'unanswerable for three of five. **The four lists stay OPEN by name.** **Nothing here is '
         'closed except the surfacing itself, whose occasion is gone.**'),
        '',
    ]
    return lines


def corr_rows(Q):
    m = ("**THE FIVE CLUSTERS SURFACED TO THE NAVIGATOR AND THE ANCHOR QUESTION MEASURED FOR THE "
         "FIRST TIME, WITH THE TWO DEPOSITED RECORDS AND TIER KC PRICED AND NEITHER ACTED ON** "
         "(b393, the five clusters surfaced and two pricings)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b393, %d gates read and %d checked "
            "by digest. b388 FOUND THE FIVE CLUSTERS AND b391 REPORTED THEM AND BOTH MEASURED "
            "MEMBERSHIP ONLY; THE ANCHOR QUESTION -- ANCHOR NO LONGER THE DOCUMENT A READER MEETS "
            "FIRST -- HAD NEVER BEEN TESTED, and this act tests it by the census's own two "
            "figures, DATE AND PIN COUNT, WITH THE TEST'S LIMIT STATED WITH IT: IT CAN ONLY RANK "
            "DOCUMENTS THE CENSUS LISTS. THE FIVE RETURN FOUR DIFFERENT ANSWERS AND THE FOUR ARE "
            "NOT ADDED: %d ANCHOR OVERTAKEN, %d MEMBERSHIP ONLY, %d ANCHOR NOT A CENSUS KEYSTONE, "
            "%d NO ANCHOR NAMED AT ALL -- THREE OF THE FOUR ARE WAYS OF NOT ANSWERING THE QUESTION "
            "AND ONLY ONE IS AN ANSWER TO IT, so (L1) EXPECTED TWO AND IS REPORTED REFUTED and AN "
            "UNANSWERABLE CASE IS NOT PROMOTED INTO AN AFFIRMATIVE ONE TO REACH TWO. THE SCREEN "
            "WAS REPAIRED BEFORE ANY FINDING WAS FILED because its first form conflated THE ANCHOR "
            "IS NOT A KEYSTONE with THERE IS NO ANCHOR. THE TWO RECORDS PRICE ASYMMETRICALLY: "
            "21432399 deposited the monograph at manuscript v5.8 against a repository at v5.13 and "
            "CAN BE NOTED IN ONE LINE TODAY, while 19675356's DEPOSITED VERSION IS NOT RECORDED "
            "ANYWHERE IN THE CORPUS so it CANNOT BE GIVEN A CURRENT-VERSION REMEDY AT ALL; AND "
            "NEITHER REMEDY BUYS AN ANSWER TO WHETHER A DOI IS SAFE TO CITE WITHOUT A LIVE READ. "
            "TIER KC IS PRICED AND NOT APPLIED: ITS OBLIGATION HAS THREE LIMBS AND THE RECORD "
            "ANSWERS ONE -- b387's %s ROWS ANSWER GRADE, PLACEMENT AND COVERAGE ARE UNHELD, THE "
            "ONE KEYSTONE b390 READ WHOLE WOULD FAIL THE PLACEMENT LIMB, AND THE APPLICATION NEEDS "
            "A DECLARATION WHICH IS A GATE AND NOT A COST. %d DOCUMENTS PLACED, %d CANDIDATES "
            "NAMED, %d CLUSTERS RESHAPED, AND NO CORPUS DOCUMENT EDITED AT ALL"
            % (LG['gates_read'], LG['face_subject_gates'],
               C1['by_verdict'].get('ANCHOR OVERTAKEN', 0),
               C1['by_verdict'].get('MEMBERSHIP ONLY', 0),
               C1['by_verdict'].get('ANCHOR NOT A KEYSTONE', 0),
               C1['by_verdict'].get('NO ANCHOR NAMED', 0),
               C3['rows'], C3['placed'], C3['candidates'], C1['reshaped']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN. ### It read, measured and priced "
            "and edited no corpus document. ### NO KERNEL WAS OPENED, NO STATEMENT PROVED, NO "
            "BUILD RUN AND NO AXIOM PROFILE RECOMPUTED. ### PRICING A CLASS IS NOT APPLYING IT, "
            "AND SURFACING A FINDING IS NOT ACTING ON IT")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT "
            "THE OBJECT. ### NO CLUSTER RESHAPED, NO DOCUMENT PLACED IN TIER KC, NO CLASS RULED, "
            "NO DOCUMENT RECLASSIFIED, NO GRADE MOVED, NO CLAIM WITHDRAWN, NO REGISTRY ROW EDITED, "
            "NO CORRESPONDENCE ROW EDITED, NO LIST CLOSED. ### THE TAXONOMY AND THE DEPOSIT RULE "
            "ARE NOT AMENDED. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL")
    grade = ("### THE ANCHOR QUESTION WAS MEASURED FOR THE FIRST TIME AND ITS LIMIT STATED WITH "
             "IT. ### 4 DISTINCT VERDICTS REPORTED SEPARATELY AND NEVER SUMMED. ### 0 "
             "UNANSWERABLE CASES PROMOTED TO REACH AN EXPECTATION. ### BOTH REMEDIES PRICED FOR "
             "BOTH RECORDS WITH WHAT EACH DOES NOT BUY, AND 0 RECOMMENDED. ### THE CHEAP SWEEP IS "
             "REPORTED AS A FLOOR AND NOT A VERDICT. ### 0 CORPUS DOCUMENTS EDITED")
    status = ("data/b393_the_clusters_surfaced.txt; data/%s; data/%s; "
              "data/b393_registration_2026-09-09.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b393); tools/b393_extract.py; tools/b393_regspec.py; "
              "tools/b393_reg_gate.py; tools/b393_components.py; tools/b393_desk_bank.py; "
              "tools/b393_checks.py; PLACE-papers OPEN_TRAILS.md (an append-only block, the only "
              "corpus write); CORRESPONDENCE.md row %%d" % (AC['run_file'], E['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('which five clusters changed', 'did any cluster change its anchor',
           'what would it cost to fix the two deposited records',
           'what would it cost to apply tier kc', 'why is tier kc still empty')
MUST_NOT_HIT = ('a cluster was reshaped', 'a document was placed in tier kc',
                'a remediation was recommended', 'the platform was called')


def do_key(rownum):
    KEY = 'the-five-clusters-surfaced'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b388 FOUND FIVE CLUSTERS CHANGED IN SHAPE AND b391 REPORTED THEM AND BOTH MEASURED "
        "MEMBERSHIP ONLY. b393 SURFACED THEM TO THE NAVIGATOR AND MEASURED THE ANCHOR QUESTION FOR "
        "THE FIRST TIME, by the census's own two figures DATE AND PIN COUNT, with the test's limit "
        "stated: IT CAN ONLY RANK DOCUMENTS THE CENSUS LISTS. THE FIVE RETURN FOUR DIFFERENT "
        "ANSWERS AND THE FOUR ARE NOT ADDED: %d ANCHOR OVERTAKEN (Simplicity / RH cascade, "
        "overtaken by PATHS_TO_THE_CRITICAL_LINE), %d MEMBERSHIP ONLY, %d ANCHOR NOT A CENSUS "
        "KEYSTONE, %d NO ANCHOR NAMED AT ALL. THREE OF THE FOUR ARE WAYS OF NOT ANSWERING THE "
        "QUESTION AND ONLY ONE IS AN ANSWER TO IT, SO (L1) EXPECTED TWO AND IS REPORTED REFUTED. "
        "THE TWO DEPOSITED RECORDS FAILING (R20)'s CURRENCY OBLIGATION PRICE ASYMMETRICALLY: "
        "21432399 deposited the monograph at manuscript v5.8 against a repository at v5.13 and CAN "
        "BE NOTED IN ONE LINE TODAY; 19675356's DEPOSITED VERSION IS NOT RECORDED ANYWHERE IN THE "
        "CORPUS so IT CANNOT BE GIVEN A CURRENT-VERSION REMEDY AT ALL. NEITHER REMEDY BUYS AN "
        "ANSWER TO WHETHER A DOI IS SAFE TO CITE WITHOUT A LIVE READ. TIER KC IS PRICED AND STILL "
        "EMPTY: ITS OBLIGATION HAS THREE LIMBS AND THE RECORD ANSWERS ONE -- b387's %s ROWS ANSWER "
        "GRADE; PLACEMENT AND COVERAGE ARE UNHELD; THE ONE KEYSTONE b390 READ WHOLE WOULD FAIL THE "
        "PLACEMENT LIMB; AND THE APPLICATION NEEDS A DECLARATION, WHICH IS A GATE AND NOT A COST."
        % (C1['by_verdict'].get('ANCHOR OVERTAKEN', 0),
           C1['by_verdict'].get('MEMBERSHIP ONLY', 0),
           C1['by_verdict'].get('ANCHOR NOT A KEYSTONE', 0),
           C1['by_verdict'].get('NO ANCHOR NAMED', 0), C3['rows']))
    grade = (
        "### NO CLUSTER WAS RESHAPED, SPLIT, MERGED, RENAMED OR RE-ANCHORED. ### NO DOCUMENT WAS "
        "PLACED IN TIER KC AND NO CANDIDATE WAS NAMED. ### NO CLASS RULED, NO DOCUMENT "
        "RECLASSIFIED, NO GRADE MOVED, NO CLAIM WITHDRAWN, NO REGISTRY ROW EDITED, NO "
        "CORRESPONDENCE ROW EDITED, NO LIST CLOSED. ### NO CORPUS DOCUMENT WAS EDITED AT ALL -- "
        "THE ONLY WRITES ARE THE TWO LEDGERS. ### NEITHER REMEDY WAS RECOMMENDED. ### THE CHEAP "
        "SWEEP IS A FLOOR AND NOT A VERDICT: A HEADING IS NOT A TABLE READ. ### NOTHING DEPOSITS "
        "AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY "
        "NAME. ### NO KEYSTONE WAS RECONCILED. ### M-2 UNCHANGED")
    where = (
        "data/b393_the_clusters_surfaced.txt; data/%s; data/%s; "
        "data/b393_registration_2026-09-09.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b393 -- %d gates read, %d checked by digest); "
        "tools/b393_extract.py; tools/b393_regspec.py; tools/b393_reg_gate.py; "
        "tools/b393_components.py; tools/b393_desk_bank.py; tools/b393_checks.py; "
        "PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b393 (the five clusters surfaced to the navigator with what changed in each and a "
           "quotation apiece; the anchor question measured for the first time and returning four "
           "different answers of which three are ways of not answering it; and the two deposited "
           "records and Tier KC priced, with nothing acted on)")
    row_new = ('    # ### THE FIVE CLUSTERS SURFACED (b393).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where, chr(10)))
    txt = io.open(INDEX, encoding='utf-8').read()
    pre = {}
    for qq in MUST_NOT_HIT:
        out, _rc = query(qq)
        pre[qq] = no_key(out)
        rec('    %-44s NO KEY before : %s' % (qq, pre[qq]))
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
        rec('    %-48s reaches the b393 key : %s' % (qq, g))
    for lbl, cond in (('both prior acts measured membership only',
                       'BOTH MEASURED MEMBERSHIP ONLY' in out),
                      ('the anchor question was measured for the first time',
                       'FOR THE FIRST TIME' in out),
                      ('the test`s limit is stated',
                       'IT CAN ONLY RANK DOCUMENTS THE CENSUS LISTS' in out),
                      ('four answers, not added', 'THE FOUR ARE NOT ADDED' in out),
                      ('three of four are non-answers',
                       'WAYS OF NOT ANSWERING THE QUESTION' in out),
                      ('(L1) refuted', 'REPORTED REFUTED' in out),
                      ('the records price asymmetrically', 'PRICE ASYMMETRICALLY' in out),
                      ('the Silence deposit is blocked',
                       'CANNOT BE GIVEN A CURRENT-VERSION REMEDY AT ALL' in out),
                      ('neither remedy buys the citation question',
                       'WITHOUT A LIVE READ' in out),
                      ('three limbs, one answered',
                       'THREE LIMBS AND THE RECORD ANSWERS ONE' in out),
                      ('a declaration is a gate not a cost',
                       'A GATE AND NOT A COST' in out),
                      ('nothing reshaped, nothing placed',
                       'NO CLUSTER WAS RESHAPED' in out and 'NO DOCUMENT WAS PLACED' in out),
                      ('no corpus document edited',
                       'NO CORPUS DOCUMENT WAS EDITED AT ALL' in out),
                      ('the platform was not called',
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
    rec('b393 -- THE DESK, THE LEDGER WRITES, AND THE BANK.')
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
        rec('  ### the b390 block is present and is not edited : %s' % (PRIOR in before))
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
    tr['says_membership_only'] = 'both measured membership only' in seg
    tr['says_first_time'] = 'had never been tested' in seg
    tr['says_limit'] = 'can only rank documents the census lists' in seg
    tr['says_not_added'] = 'they are not added' in seg.lower()
    tr['says_refuted'] = 'reported REFUTED' in seg
    tr['says_asymmetric'] = 'they price asymmetrically' in seg.lower()
    tr['says_blocked'] = 'blocked outright' in seg
    tr['says_three_limbs'] = 'three limbs' in seg
    tr['says_gate'] = 'is a gate, and no amount of measurement opens it' in seg
    tr['says_no_reshape'] = 'the reshaping is the author' in seg.lower()
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
        run_clock.write(D, 'b393_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b393_desk_notes', LINES)
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
            run_clock.write(D, 'b393_desk_notes', LINES)
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
    B.append('b393 -- THE FIVE CLUSTERS, SURFACED; AND TWO PRICINGS. ### THE BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **TWO ACTS FOUND THE FIVE CLUSTERS AND NEITHER PUT THEM IN FRONT')
    B.append('### ### ### OF THE NAVIGATOR.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 1 -- THE FIVE CLUSTERS, AND THE ANCHOR QUESTION.')
    B.append(SUB)
    B.append('### `b388` found them; `b391` reported them; ### **BOTH MEASURED MEMBERSHIP')
    B.append('### ### ONLY.** ### The order names five kinds of change and one of them --')
    B.append('### ### *anchor no longer the document a reader meets first* ### -- ### **HAD')
    B.append('### ### NEVER BEEN TESTED.**')
    B.append('### **THE TEST:** ### a cluster changed by anchor if a member it gained is a')
    B.append('### census keystone ### **NEWER** ### than the best anchor ### **AND** ###')
    B.append('### carrying ### **MORE PINS.** ### **ITS LIMIT IS STATED WITH IT: IT CAN ONLY')
    B.append('### ### RANK DOCUMENTS THE CENSUS LISTS.**')
    B.append('')
    for s in C1['surfaced']:
        B.append('###   ### **%s** ### -- `%s` by `%d` ### -- **%s**'
                 % (s['cluster'], s['finding'], s['by'], s['verdict']))
        B.append('###       gained %s' % ', '.join('`%s`' % g for g in s['gained']))
        if s['keystones']:
            B.append('###       of which a census keystone : `%s`' % s['keystones'][0])
    B.append('')
    B.append('### ### **FOUR DIFFERENT ANSWERS TO ONE QUESTION:**')
    for k in sorted(C1['by_verdict']):
        B.append('###   %-26s ### **`%d`**' % (k, C1['by_verdict'][k]))
    B.append('### ### ### **AND THEY ARE NOT ADDED.** ### Three of the four are ways of ###')
    B.append('### ### ### **NOT ANSWERING** ### the anchor question and only one is an')
    B.append('### ### ### answer to it.')
    B.append('### ### **CHANGED BY ANCHOR : `%d` OF `5`. ### `(L1)` EXPECTED TWO AND IS'
             % C1['anchor_changed'])
    B.append('### ### REPORTED REFUTED.**')
    B.append('### ### ### **AN UNANSWERABLE CASE IS NOT PROMOTED INTO AN AFFIRMATIVE ONE TO')
    B.append('### ### ### REACH TWO**, and the locked face said the count was one before the')
    B.append('### ### ### component ran.')
    B.append('### ### **AND THE SHAPE OF THE UNANSWERABLE IS THE PART WORTH THE AUTHOR`S')
    B.append('### ### TIME:** ### `2` clusters ### **HAVE NO ANCHOR AT ALL**, so a reader')
    B.append('### ### meeting them meets a member list; `1` is ### **ANCHORED ON DOCUMENTS')
    B.append('### ### THE CENSUS DOES NOT LIST** ### while a census keystone joined it, so')
    B.append('### ### **THE ANCHOR AND THE MEMBERSHIP ARE GRADED ON DIFFERENT SCALES.**')
    B.append('### ### ### **`%d` CLUSTERS RESHAPED. ### THE RESHAPING IS THE AUTHOR`S.**'
             % C1['reshaped'])
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 2 -- THE TWO RECORDS, PRICED ASYMMETRICALLY.')
    B.append(SUB)
    B.append('### ### **`21432399`** ### -- the monograph at manuscript `%s`; the repository'
             % C2['21432399']['deposited_at'])
    B.append('### now carries `%s`.' % C2['21432399']['repo_now'])
    B.append('###   (a) a historical note : ### **ONE LINE IN `REGISTRY.md` TODAY**, because')
    B.append('###   the version is known. ### **IT DOES NOT BUY** ### a reader who arrives at')
    B.append('###   the DOI directly anything -- a note in the corpus does not travel.')
    B.append('###   (b) a new deposit      : ### **A WHOLE WAVE** ### under `(R20)`\'s first')
    B.append('###   limb, and a platform that answers. ### **IT DOES NOT BUY** ### retirement')
    B.append('###   of the old record -- ### **A NEW VERSION OUTRANKS; IT DOES NOT RETIRE** --')
    B.append('###   so the note is still owed afterwards.')
    B.append('### ### **`19675356`** ### -- *The Silence of Foundations*; the repository now')
    B.append('### carries `%s`; and ### **THE VERSION IT WAS DEPOSITED AT IS NOT RECORDED'
             % C2['19675356']['repo_now'])
    B.append('### ### ANYWHERE IN THE CORPUS.**')
    B.append('###   (a) a historical note : writable, and ### **THIN** ### -- a note that')
    B.append('###   cannot say ### *superseded from what* ### records only that something old')
    B.append('###   exists.')
    B.append('###   (b) a new deposit      : ### **BLOCKED OUTRIGHT.** ### To deposit the')
    B.append('###   current state you must know what is already there, and ### **THE PLATFORM')
    B.append('###   ### DOES NOT ANSWER AND THE CORPUS DOES NOT RECORD IT.** ### Depositing')
    B.append('###   without a read risks duplicating something already current -- ### **A')
    B.append('###   ### WORSE DEFECT THAN THE ONE IT CURES.**')
    B.append('### ### ### **WHAT NEITHER BUYS, FOR EITHER:** ### an answer to ### *is this DOI')
    B.append('### ### ### safe to cite* ### without a live read, because ### **THE OBLIGATION')
    B.append('### ### ### IS SATISFIED IN THE CORPUS AND TESTED AT THE PLATFORM.**')
    B.append('### ### **NOTHING IS WRITTEN AT THE PLATFORM. ### NEITHER REMEDY IS')
    B.append('### ### RECOMMENDED; THE CHOICE IS THE AUTHOR`S.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 3 -- `Tier KC`, PRICED AND STILL EMPTY.')
    B.append(SUB)
    B.append('### ### **THE OBLIGATION HAS THREE LIMBS AND THE RECORD ANSWERS ONE.**')
    B.append('###   (i)   ### **GRADE** ### -- ### **ANSWERED**: `b387`\'s `%s` rows across'
             % C3['rows'])
    B.append('###   `9` documents, `%s` of them not machine-verified and labelled.'
             % C3['not_machine'])
    B.append('###   (ii)  ### **PLACEMENT** ### -- ### **NOT ANSWERED.** ### The record holds')
    B.append('###   no table position for any document.')
    B.append('###   (iii) ### **COVERAGE** ### -- ### **NOT ANSWERED.** ### The record holds')
    B.append('###   row counts and not claim counts.')
    B.append('### ### **AND THE ONE KEYSTONE `b390` READ WHOLE WOULD FAIL THE PLACEMENT')
    B.append('### ### LIMB**, with both its tables at the end and the standard`s below its')
    B.append('### ### provenance -- worth knowing ### **BEFORE** ### a placement pass is')
    B.append('### ### ordered rather than after.')
    B.append('### **THE CHEAP SWEEP, A FLOOR AND NOT A VERDICT:** ### `%s` census keystones on'
             % C3['found'])
    B.append('### disk, `%s` carrying a correspondence table, `%s` a glossary heading, `%s` a'
             % (C3['with_table'], C3['with_glossary'], C3['with_bib']))
    B.append('### references section. ### ### **A HEADING IS NOT A TABLE READ.**')
    B.append('### ### **THE PRICE:** ### grade is ### **FREE** ### for the nine already read;')
    B.append('### placement is ### **MINUTES PER DOCUMENT AND MECHANICAL**; coverage is ###')
    B.append('### **THE SAME WORK `b390` PRICED AT HALF AN HOUR A DOCUMENT AND CALLED AN')
    B.append('### ### UNDERESTIMATE.**')
    B.append('### ### ### **AND THE APPLICATION NEEDS A THIRD THING THAT IS NOT A COST AT')
    B.append('### ### ### ALL: A DECLARATION.** ### `b382` ruled a class ruling rests on')
    B.append('### ### ### declaration, and ### **NO DOCUMENT CARRIES ONE FOR A CLASS ONE DAY')
    B.append('### ### ### OLD. ### THAT IS A GATE, AND NO AMOUNT OF MEASUREMENT OPENS IT.**')
    B.append('### ### **`%d` DOCUMENTS PLACED. ### `%d` CANDIDATES NAMED.**'
             % (C3['placed'], C3['candidates']))
    B.append('')
    B.append(SUB)
    B.append('### THE EXPECTATIONS, DECIDED.')
    B.append(SUB)
    B.append('### ### **THE NAVIGATOR`S:**')
    B.append('###   `(L1)` at least two of the five changed by anchor rather than by subject')
    B.append('###   ### **-- REFUTED.** ### `%d` did.' % C1['anchor_changed'])
    B.append('### ### **THIS SEAT`S:**')
    B.append('###   `(E1)` the five will not sort into two buckets ### **-- MET**: they sort')
    B.append('###   into ### **FOUR**, and three of the four are ways of not answering.')
    B.append('###   `(E2)` the two records will price asymmetrically ### **-- MET**: one is a')
    B.append('###   one-line note today, the other ### **CANNOT BE REMEDIED AT ALL** ### on')
    B.append('###   the current-version limb.')
    B.append('###   `(E3)` the `Tier KC` price will be dominated by the unmeasured limb ###')
    B.append('###   **-- MET**, and ### **THE GATE BEHIND IT IS WORSE THAN THE COST**: a')
    B.append('###   declaration cannot be bought with measurement.')
    B.append('')
    B.append(SUB)
    B.append('### WHAT THIS ACT DID NOT DO.')
    B.append(SUB)
    B.append('### ' + SCOPE.replace('**', ''))
    B.append('')
    B.append(SUB)
    B.append('### THE APPARATUS.')
    B.append(SUB)
    B.append('### **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on the lock gate')
    B.append('### run as `b393`: ### **`%d` GATES READ, `%d` PASSING, `%d` CHECKED BY DIGEST.**'
             % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    regtxt = io.open(os.path.join(D, 'b393_registration_2026-09-09.txt'),
                     encoding='utf-8', errors='replace').read()
    ms = re.search(r'([0-9a-f]{64})', regtxt)
    mt = re.search(r'### locked at .UTC. : (\S+)', regtxt)
    B.append('### **THE FACE:** ### `%d` bytes on disk, sha256 `%s`, locked at `%s`.'
             % (len(regtxt.encode('utf-8')), ms.group(1) if ms else '?',
                mt.group(1) if mt else '?'))
    B.append('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor.'
             % (E['reads'], E['without_anchor']))
    for n in ('b393_reads', 'b393_components'):
        jj = J(n)
        B.append('### %-18s run file `%s` recorded clock %s'
                 % (n, jj['run_file'], jj.get('run_clock')))
    B.append('### ### **SIX NEW `relay` TOOLS AGAINST A CAP OF SIX.**')
    B.append(BAR)

    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### A CLUSTER WAS RESHAPED.', '### A DOCUMENT WAS PLACED IN TIER KC.',
                '### A REMEDIATION WAS RECOMMENDED.', '### THE FOUR VERDICTS WERE SUMMED.',
                '### THE RECORD HOLDS ALL THREE LIMBS.', '### A CORPUS DOCUMENT WAS EDITED.',
                '### THE PLATFORM WAS CALLED.', '### SOMETHING WAS DEPOSITED.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))
    rec()
    bar('=')
    rec('  ### desk %d ; closed %d ; trail %s ; row %s ; key %s'
        % (Q['items'], Q['closed'], tr['appended_only'], rownum, kok))
    bar('=')
    p = run_clock.write(D, 'b393_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             bank='b393_the_phantom_repaired.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b393_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
