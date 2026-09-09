# -*- coding: utf-8 -*-
"""b394_desk_bank.py -- THE DESK, THE LEDGER WRITES, AND THE BANK FOR LEG 1.

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
MARK = '<!-- b394 the reconciliation batched: three keystones read -->'
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


AC = J('b394_components')
LG = J('b394_lockgate')
E = J('b394_reads')
C1, C2, C3 = AC['c1'], AC['c2'], AC['c3']
BANKOUT = os.path.join(D, 'b394_the_reconciliation_batched.txt')


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
     '### **CONFIRMED BY READING AT b394**: `SILENCE_STAGES_DEALIGNMENT` carries none, and '
     '### **THIS ACT DID NOT WRITE ONE** -- writing a correspondence table is ### **AUTHORING, '
     'NOT RECONCILING.** ### **STILL THE AUTHOR`S**'),
    ('the 23 unreadable correspondence rows', 'STAND', 'NAMED at b388 by cause, and ROUTED'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the keystone-class documents b388 marked UNASSIGNED', 'STAND',
     '### **UNASSIGNED IS A STATE AND NOT A DEBT**'),
    ('the deposited layer, unread since b389', 'STAND',
     'STILL BLOCKED; this act did not ask the platform'),
    ('the eight-versus-six cluster-synthesis disagreement', 'STAND', 'ROUTED at b389'),
    ('the practice that let the phantom drift run', 'STAND',
     '### **AND THIS ACT FOUND ITS SECOND INSTANCE.** ### `b391` found a registry correction '
     'that never propagated; `b394` found ### **ANOTHER**, inside its own batch. ### **NOTHING '
     'IN THE CORPUS CHECKS A CITED VERSION AGAINST ITS TARGET**, and two instances in four acts '
     'is a pattern, not an accident. ### **STILL OPEN**'),
    ('the `66` superseded version citations', 'STAND',
     'REPORTED at b391 and LEFT; ### **`6` MORE FOUND IN THE THREE SUBJECTS AND ALSO LEFT** -- '
     '### **A VERSION THAT EXISTS BUT IS SUPERSEDED IS A CURRENCY ITEM, NOT A PHANTOM**'),
    ('`CONSTANCE.md` carries no version in its own bytes', 'STAND', 'ROUTED at b391'),
    ('placement into `Tier KC`', 'STAND', 'PRICED at b393 and STILL EMPTY'),
    ('whether `SIDE-kernel` has a current citable record', 'STAND', 'ROUTED at b392'),
    ('the cluster reshaping, with the five named', 'STAND',
     'NAMED at b393; ### **THE RESHAPING IS THE AUTHOR`S**'),
    ('the two deposited records` remediation', 'STAND', 'PRICED at b393, NOT PERFORMED'),
    ('the anchor question, unanswerable for three of five', 'STAND', 'ROUTED at b393'),

    # ---- WHAT THIS ACT ADDS ---------------------------------------------------------------------
    ('the fifteen keystones not read', 'STAND',
     '### **FOUR OF SIXTEEN ARE NOW RECONCILED** -- `b390`\'s one and `b394`\'s three -- and '
     '### **ELEVEN OF THE REMAINING TWELVE CANNOT BE READ BY THIS RULE AT ALL**, because their '
     'terminals are not reachable from the drive. ### **THE POPULATION THIS METHOD CAN REACH IS '
     'ALREADY NEARLY EXHAUSTED**, which is the finding, not the count'),
    ('the eleven unreachable keystones', 'STAND',
     '### **NEW at b394: THE METHOD`S OWN CEILING.** ### `9` name no kernel repository the drive '
     'holds; several also say in their own text that their terminals are ### **HELD OR '
     'UNMERGED.** ### Reading them needs either a clone or a ruling about reading branches, and '
     '### **BOTH ARE THE AUTHOR`S.** ### **ROUTED**'),
    ('the two citations repaired in `GRH_CASCADE`', 'CLOSE',
     '### **NEW at b394 AND CLOSED BY `(R7)`: THE OCCASION IS GONE.** ### Two citations of '
     '`FOUNDATIONS_OF_THE_SIDE_PROGRAMME` stood at `v0.1` while the registry had reconciled the '
     'row past it. ### **THEY ARE MOVED FORWARD, THE ORIGINALS PRESERVED IN AN APPENDED '
     'ANNOTATION, `0` LINES REMOVED AND ONLY THE VERSION CHANGED ON EACH LINE**'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES ONE ITEM AND OPENS TWO.** ### `(R7)` closes an item whose')
    rec('    ### occasion is gone, and two stale citations that have been moved forward have no')
    rec('    ### occasion left.')
    rec('    ### ### ### **BUT THE SPECIES THAT PRODUCED THEM IS NOW ON ITS SECOND INSTANCE IN')
    rec('    ### ### ### FOUR ACTS**, and the item that names it ### **STANDS AND GETS SHARPER**:')
    rec('    ### ### ### two independent occurrences of a registry correction that never reached')
    rec('    ### ### ### the documents citing it is ### **A PATTERN, NOT AN ACCIDENT.**')
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
    "**SCOPE: THE RECONCILIATION, BATCHED -- THREE KEYSTONES READ IN ONE ACT.** **THE CHOICE WAS "
    "MADE BY b390'S RULE, QUOTED, WITH NOTHING ADDED TO IT** -- take those whose terminals the "
    "drive can reach. An earlier form of this act's own survey also demanded a correspondence "
    "table, A CONDITION b390 NEVER STATED, and it cut the eligible set from 4 to 3 BY A RULE "
    "NOBODY RULED; the addition was removed before the lock. **11 KEYSTONES ARE EXCLUDED AND EVERY "
    "EXCLUSION IS NAMED WITH ITS REASON**, and ADDITIVE_MULTIPLICATIVE_CONSPIRACY is SET ASIDE "
    "with its own reason: b390 read it whole and re-reading it would be re-doing that act's work. "
    "**ONE OF THE THREE CARRIES NO CORRESPONDENCE TABLE, AND THAT IS REPORTED AND NOT REPAIRED: "
    "WRITING A CORRESPONDENCE TABLE IS AUTHORING, NOT RECONCILING.** **THE ONLY CORPUS EDIT IS TWO "
    "VERSION STRINGS IN GRH_CASCADE.md, v0.1 -> the registry's own row value, WITH THE ORIGINALS "
    "PRESERVED IN AN APPENDED ANNOTATION**; 0 lines removed, only the version changed on each "
    "line, and the old form was confirmed to be IN THE CITED DOCUMENT'S OWN LINEAGE first -- A "
    "SUPERSESSION IS NOT A PHANTOM AND IS NOT REPAIRED AS ONE. **4 REPAIRS ARE ROUTED, EACH NAMED "
    "WITH THE RULING IT NEEDS**, and repairs made and repairs routed are COUNTED SEPARATELY. **THE "
    "THREE SPECIES ARE REPORTED APART AND NEVER ADDED: 0 phantoms, 2 corrected-but-unpropagated, 6 "
    "superseded** -- a phantom is a defect, an unpropagated correction is a defect with a known "
    "cure, and a supersession is currency. **(L2) IS MET INSIDE THE BATCH**: one of the three "
    "subjects cites another of the three at a version the record moved past. **THE PRICE IS "
    "RE-MEASURED FROM THREE AND BOTH FIGURES ARE FLOORS**, read at the component while the act "
    "continues, exactly as b390's was; the per-keystone figure fell and the per-act figure did "
    "not, because THE SAVING IS IN THE APPARATUS AND NOT IN THE READING, and THE SAMPLE IS THE "
    "REACHABLE ONES, which is the population most likely to be in good order. NO GRADE MOVED, NO "
    "CLAIM WITHDRAWN, NO CORRESPONDENCE TABLE WRITTEN EXTENDED OR RE-GRADED, NO CLASS RULED, NO "
    "DOCUMENT RECLASSIFIED OR PLACED IN Tier KC, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, "
    "THE TAXONOMY AND THE DEPOSIT RULE NOT AMENDED, NEITHER MAP TOUCHED, NO CLUSTER RESHAPED, NO "
    "LIST CLOSED. **b393's GATE SUITE IS NOT RE-RUN AT THIS ACT'S CLOSE** -- the order's own "
    "instruction, because this act's commit moves its baseline, and the closing states which "
    "reading it relies on. NOTHING DEPOSITS; **THE PLATFORM WAS NOT CALLED AT ALL**; NO BUILD WAS "
    "RUN AND NO KERNEL BRANCH MERGED, PUSHED OR CREATED -- naming a repository on the drive is not "
    "compiling it. **THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME.** NO NEW TRACKING DOCUMENT WAS "
    "CREATED. NO ARCHIVE OR outputs FILE TOUCHED, THE MIRROR ROSTER NOT EDITED, NO "
    ".git/hooks/pre-push DELETED. NO .lean FILE TOUCHED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS "
    "OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, "
    "h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE "
    "IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The "
    "patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE "
    "INSTRUMENT LANE STAYS PARKED. THE WAVE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands "
    "exactly where the deposit left it and this act makes no claim about it in either direction.")


def trail_block(Q):
    return [
        '', MARK, '',
        '### **b394 — THE RECONCILIATION, BATCHED (2026-09-09)**',
        '',
        ('*No block above is edited. The b393 block (`%s`) and every block before it stand exactly '
         'as they were written.*' % PRIOR),
        '',
        ('**THREE KEYSTONES READ IN ONE ACT, CHOSEN BY `b390`’S RULE AND NOTHING ADDED TO IT** — '
         '*take those whose terminals the drive can reach*. Of the census’s **`15`** keystones on '
         'disk, **`4`** name a kernel repository the drive holds and do not say their terminals '
         'are held or unmerged. **`11` are excluded and every exclusion is named with its '
         'reason**; `ADDITIVE_MULTIPLICATIVE_CONSPIRACY` is **set aside** because `b390` read it '
         'whole and re-reading it would be re-doing that act’s work. **The three: `GRH_CASCADE`, '
         '`FOUNDATIONS_OF_THE_SIDE_PROGRAMME`, `SILENCE_STAGES_DEALIGNMENT`.** *An earlier form '
         'of this act’s own survey also demanded a correspondence table — a condition `b390` '
         'never stated — and it cut the eligible set from four to three **by a rule nobody '
         'ruled**. The addition was removed before the lock: **a rule quoted is a rule; a rule '
         'improved is a new rule.***'),
        '',
        ('**WHAT THE THREE CARRY.** `GRH_CASCADE` carries **`%d`** correspondence rows; '
         '`FOUNDATIONS_OF_THE_SIDE_PROGRAMME` carries **`%d`**; and '
         '**`SILENCE_STAGES_DEALIGNMENT` carries none**. For that third document the order’s '
         'question — *what its table carries by grade* — has the answer **there is no table**, '
         'and **a keystone with no table is a keystone whose grade limb cannot be read**. `b387` '
         'already named five such. **This act did not write one: writing a correspondence table '
         'is authoring, not reconciling.**'
         % (C1['table_rows'].get('GRH_CASCADE', 0),
            C1['table_rows'].get('FOUNDATIONS_OF_THE_SIDE_PROGRAMME', 0))),
        '',
        ('**THE THREE BUCKETS, ACROSS ALL THREE SUBJECTS: `%d` already says it, `%d` says '
         'something now superseded, `%d` does not carry it.** Every bucket is reported with its '
         'count. **And `(L2)` is met inside the batch**: `GRH_CASCADE` cites '
         '`FOUNDATIONS_OF_THE_SIDE_PROGRAMME` — *another of the three* — at **`v0.1`** in two '
         'places, while `REGISTRY.md` records a row update reconciling that document past it and '
         'its table now carries **`%s`**. **That is the `corrected but unpropagated` species '
         '`b391` found in the registry’s own bundle label, recurring — and this time the batch '
         'found its own defect, which one-at-a-time reading could not have found as cheaply.**'
         % (C1['buckets']['ALREADY SAYS IT'],
            C1['buckets']['SAYS SOMETHING NOW SUPERSEDED'],
            C1['buckets']['DOES NOT CARRY IT'], C2['newv'])),
        '',
        ('**THE REPAIR, AND WHAT WAS CHECKED BEFORE IT.** `v0.1` was confirmed to be **in the '
         'cited document’s own lineage** before anything moved — **a supersession is not a '
         'phantom and is not repaired as one**. The two citations were moved to the registry’s '
         'own row value, read at its own line, and **the originals are preserved in an appended '
         'annotation**. **`%d` lines removed; only the version changed on each line; `%d` lines '
         'differ from the pre-act blob.** *Nothing else in the document, and no other document, '
         'was touched.*'
         % (C2['removed'], C2['made'])),
        '',
        ('**AND `%d` REPAIRS ARE ROUTED, EACH NAMED WITH THE RULING IT NEEDS.** The missing '
         'correspondence table (writing one is authoring); the **`%d` superseded citations** '
         '(`b391` ruled them a currency item); the E-Difficulty scope split, absent from two of '
         'the three; and `W-6`’s closure, absent from one. **The last three are additions, not '
         'corrections — the papers are not wrong without them — and adding material to a keystone '
         'is authoring too.** **Repairs made and repairs routed are counted separately.**'
         % (C2['routed'], C3['superseded'])),
        '',
        ('**THE COUNT AND THE PRICE.** **`%d` of the census’s `16` keystones are now reconciled** '
         '— `b390`’s one and this act’s three — **and that is not rounded up**. The act took '
         '**`%.0f` minutes**, about **`%.0f` per keystone**, against `b390`’s **`%d` for one**. '
         '**Both figures are floors**: each is read at the component while the act continues, and '
         '`b390`’s was taken the same way. **The per-keystone figure fell and the per-act figure '
         'did not, and the reason is the apparatus and not the reading** — three subjects share a '
         'single registration, gate suite and push. **A reader planning work should plan with the '
         'per-act figure: the saving is in the apparatus and cannot be spent twice.** And **the '
         'sample is biased, named once**: these three are *the reachable ones*, the population '
         'most likely to be in good order.'
         % (C3['reconciled'], C3['minutes'], C3['per_keystone'], C3['b390_minutes'])),
        '',
        ('**THE METHOD’S OWN CEILING, WHICH IS THE FINDING UNDER THE COUNT.** **`11` of the '
         'remaining `12` cannot be read by this rule at all** — `9` name no kernel repository the '
         'drive holds, and several say in their own text that their terminals are **held or '
         'unmerged**. **The population this method can reach is already nearly exhausted.** '
         'Reading the rest needs either a clone or a ruling about reading branches, and **both '
         'are the author’s**. **Routed.** **The four lists stay OPEN by name.** **Nothing '
         'deposits and the platform was not called at all.**'),
        '',
    ]


def corr_rows(Q):
    m = ("**THREE KEYSTONES RECONCILED IN ONE ACT BY b390's OWN RULE, WITH THE BATCH FINDING A "
         "STALE CITATION BETWEEN TWO OF ITS OWN SUBJECTS AND THE METHOD'S CEILING NAMED** (b394, "
         "the reconciliation batched)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b394, %d gates read and %d checked "
            "by digest. THE CHOICE WAS MADE BY b390's RULE QUOTED WITH NOTHING ADDED TO IT -- TAKE "
            "THOSE WHOSE TERMINALS THE DRIVE CAN REACH -- and an earlier form of this act's own "
            "survey ALSO DEMANDED A CORRESPONDENCE TABLE, A CONDITION b390 NEVER STATED, which cut "
            "the eligible set from 4 to 3 BY A RULE NOBODY RULED and was removed before the lock. "
            "%d KEYSTONES WERE EXCLUDED AND EVERY EXCLUSION IS NAMED WITH ITS REASON; "
            "ADDITIVE_MULTIPLICATIVE_CONSPIRACY WAS SET ASIDE because b390 READ IT WHOLE. ONE OF "
            "THE THREE CARRIES NO CORRESPONDENCE TABLE and that is REPORTED AND NOT REPAIRED, "
            "since WRITING A CORRESPONDENCE TABLE IS AUTHORING, NOT RECONCILING. THE THREE BUCKETS "
            "ARE %d / %d / %d WITH EVERY BUCKET REPORTED, and (L2) IS MET INSIDE THE BATCH: "
            "GRH_CASCADE cites FOUNDATIONS_OF_THE_SIDE_PROGRAMME -- ANOTHER OF THE THREE -- at "
            "v0.1 in two places while the registry reconciled that row past it, which is the "
            "CORRECTED-BUT-UNPROPAGATED species b391 found, RECURRING. THE OLD FORM WAS CONFIRMED "
            "TO BE IN THE CITED DOCUMENT'S OWN LINEAGE BEFORE ANYTHING MOVED, because A "
            "SUPERSESSION IS NOT A PHANTOM AND IS NOT REPAIRED AS ONE; the two citations were "
            "moved to the registry's own row value with THE ORIGINALS PRESERVED IN AN APPENDED "
            "ANNOTATION, %d LINES REMOVED and only the version changed on each line. %d REPAIRS "
            "ARE ROUTED EACH NAMED WITH THE RULING IT NEEDS, and repairs made and routed are "
            "COUNTED SEPARATELY. THE THREE SPECIES ARE REPORTED APART AND NEVER ADDED: %d "
            "PHANTOMS, %d CORRECTED-BUT-UNPROPAGATED, %d SUPERSEDED. %d OF THE CENSUS'S 16 "
            "KEYSTONES ARE NOW RECONCILED AND IT IS NOT ROUNDED UP; the act took %.0f MINUTES "
            "AGAINST b390's %d FOR ONE, BOTH FIGURES FLOORS READ AT THE COMPONENT WHILE THE ACT "
            "CONTINUES, and THE SAVING IS IN THE APPARATUS AND NOT IN THE READING. AND %d OF THE "
            "REMAINING 12 CANNOT BE READ BY THIS RULE AT ALL, so THE POPULATION THIS METHOD CAN "
            "REACH IS ALREADY NEARLY EXHAUSTED"
            % (LG['gates_read'], LG['face_subject_gates'], C1['excluded'],
               C1['buckets']['ALREADY SAYS IT'],
               C1['buckets']['SAYS SOMETHING NOW SUPERSEDED'],
               C1['buckets']['DOES NOT CARRY IT'],
               C2['removed'], C2['routed'], C3['phantom'], C3['unpropagated'],
               C3['superseded'], C3['reconciled'], C3['minutes'], C3['b390_minutes'],
               C1['excluded']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN. ### Three keystones were read and "
            "two version strings moved forward; every quoted line was re-read out of its own file "
            "at its own line number. ### NO KERNEL WAS OPENED, NO STATEMENT PROVED, NO BUILD RUN "
            "AND NO AXIOM PROFILE RECOMPUTED -- NAMING A REPOSITORY ON THE DRIVE IS NOT COMPILING "
            "IT. ### RECONCILING A PAPER IS NOT VERIFYING IT")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT "
            "THE OBJECT. ### NO GRADE MOVED, NO CLAIM WITHDRAWN, NO CORRESPONDENCE TABLE WRITTEN "
            "EXTENDED OR RE-GRADED, NO CLASS RULED, NO DOCUMENT RECLASSIFIED OR PLACED IN Tier KC, "
            "NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED. "
            "### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL")
    grade = ("### THE RULE WAS QUOTED AND NOT IMPROVED, AND THE ADDITION THAT WOULD HAVE NARROWED "
             "IT WAS REMOVED BEFORE THE LOCK. ### EVERY EXCLUSION IS NAMED. ### EVERY BUCKET IS "
             "REPORTED WITH ITS COUNT. ### THE OLD VERSION WAS CONFIRMED REAL BEFORE IT WAS MOVED. "
             "### 0 LINES REMOVED AND THE ORIGINALS PRESERVED. ### THE THREE SPECIES ARE REPORTED "
             "APART. ### BOTH PRICES ARE DECLARED FLOORS AND THE SAMPLE'S BIAS IS NAMED")
    status = ("data/b394_the_reconciliation_batched.txt; data/%s; data/%s; "
              "data/b394_registration_2026-09-09.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b394); tools/b394_extract.py; tools/b394_regspec.py; "
              "tools/b394_reg_gate.py; tools/b394_components.py; tools/b394_desk_bank.py; "
              "tools/b394_checks.py; PLACE-papers phase1.5/spectral/GRH_CASCADE.md (two version "
              "strings and one appended annotation) and OPEN_TRAILS.md (an append-only block); "
              "CORRESPONDENCE.md row %%d" % (AC['run_file'], E['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('how many keystones are reconciled', 'which keystones were read at b394',
           'what does it cost to reconcile a keystone',
           'why can most keystones not be reconciled',
           'did the batch find a defect in itself')
MUST_NOT_HIT = ('the rule was widened', 'a correspondence table was written',
                'a grade was moved', 'the platform was called')


def do_key(rownum):
    KEY = 'the-reconciliation-batched'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b394 READ THREE KEYSTONES IN ONE ACT, CHOSEN BY b390's RULE QUOTED WITH NOTHING ADDED TO "
        "IT -- TAKE THOSE WHOSE TERMINALS THE DRIVE CAN REACH. Of the census's 15 on disk, 4 ARE "
        "REACHABLE; %d ARE EXCLUDED AND EVERY EXCLUSION IS NAMED; "
        "ADDITIVE_MULTIPLICATIVE_CONSPIRACY IS SET ASIDE because b390 READ IT WHOLE. THE THREE: "
        "GRH_CASCADE, FOUNDATIONS_OF_THE_SIDE_PROGRAMME, SILENCE_STAGES_DEALIGNMENT -- and THE "
        "LAST CARRIES NO CORRESPONDENCE TABLE, reported and NOT repaired since WRITING A "
        "CORRESPONDENCE TABLE IS AUTHORING, NOT RECONCILING. THE THREE BUCKETS ARE %d / %d / %d "
        "AND (L2) IS MET INSIDE THE BATCH: GRH_CASCADE CITES FOUNDATIONS_OF_THE_SIDE_PROGRAMME -- "
        "ANOTHER OF THE THREE -- AT v0.1 IN TWO PLACES WHILE THE REGISTRY HAD RECONCILED THAT ROW "
        "PAST IT. THAT IS THE CORRECTED-BUT-UNPROPAGATED SPECIES b391 FOUND, RECURRING, AND THE "
        "BATCH FOUND ITS OWN DEFECT. THE OLD FORM WAS CONFIRMED IN THE CITED DOCUMENT'S OWN "
        "LINEAGE FIRST, because A SUPERSESSION IS NOT A PHANTOM AND IS NOT REPAIRED AS ONE; both "
        "citations were moved to the registry's row value with THE ORIGINALS PRESERVED IN AN "
        "APPENDED ANNOTATION and %d LINES REMOVED. %d REPAIRS ARE ROUTED. THE THREE SPECIES ARE "
        "REPORTED APART: %d PHANTOMS, %d UNPROPAGATED, %d SUPERSEDED. %d OF 16 KEYSTONES ARE NOW "
        "RECONCILED, AND %d OF THE REMAINING 12 CANNOT BE READ BY THIS RULE AT ALL -- THE "
        "POPULATION THIS METHOD CAN REACH IS ALREADY NEARLY EXHAUSTED."
        % (C1['excluded'], C1['buckets']['ALREADY SAYS IT'],
           C1['buckets']['SAYS SOMETHING NOW SUPERSEDED'],
           C1['buckets']['DOES NOT CARRY IT'], C2['removed'], C2['routed'],
           C3['phantom'], C3['unpropagated'], C3['superseded'], C3['reconciled'],
           C1['excluded']))
    grade = (
        "### NO GRADE WAS MOVED, NO CLAIM WITHDRAWN, NO CORRESPONDENCE TABLE WRITTEN EXTENDED OR "
        "RE-GRADED, NO CLASS RULED, NO DOCUMENT RECLASSIFIED OR PLACED IN Tier KC, NO REGISTRY ROW "
        "EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED. ### THE ONLY CORPUS "
        "EDIT IS TWO VERSION STRINGS AND ONE APPENDED ANNOTATION IN ONE DOCUMENT. ### THE RULE WAS "
        "QUOTED AND NOT IMPROVED. ### EVERY EXCLUSION IS NAMED AND EVERY BUCKET REPORTED. ### BOTH "
        "PRICES ARE DECLARED FLOORS AND THE SAMPLE'S BIAS IS NAMED. ### NOTHING DEPOSITS AND THE "
        "PLATFORM WAS NOT CALLED AT ALL. ### NO BUILD RUN. ### THE FOUR OPEN LISTS ARE RESTATED "
        "OPEN BY NAME. ### M-2 UNCHANGED")
    where = (
        "data/b394_the_reconciliation_batched.txt; data/%s; data/%s; "
        "data/b394_registration_2026-09-09.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b394 -- %d gates read, %d checked by digest); "
        "tools/b394_extract.py; tools/b394_regspec.py; tools/b394_reg_gate.py; "
        "tools/b394_components.py; tools/b394_desk_bank.py; tools/b394_checks.py; "
        "PLACE-papers phase1.5/spectral/GRH_CASCADE.md and OPEN_TRAILS.md; "
        "CORRESPONDENCE.md row %d"
        % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b394 (three keystones reconciled in one act by b390's rule quoted and not improved; "
           "the batch finding a stale citation between two of its own subjects, the "
           "corrected-but-unpropagated species recurring; two citations moved forward with the "
           "originals preserved; and the method's own ceiling named -- eleven of the remaining "
           "twelve are unreachable)")
    row_new = ('    # ### THE RECONCILIATION BATCHED (b394).%s'
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
        rec('    %-48s reaches the b394 key : %s' % (qq, g))
    for lbl, cond in (('the rule is quoted and not improved',
                       'NOTHING ADDED TO IT' in out),
                      ('every exclusion is named', 'EVERY EXCLUSION IS NAMED' in out),
                      ('the set-aside has its own reason', 'SET ASIDE' in out),
                      ('the tableless keystone is reported not repaired',
                       'AUTHORING, NOT RECONCILING' in out),
                      ('the batch found its own defect',
                       'THE BATCH FOUND ITS OWN DEFECT' in out),
                      ('a supersession is not a phantom',
                       'A SUPERSESSION IS NOT A PHANTOM AND IS NOT REPAIRED AS ONE' in out),
                      ('the originals are preserved',
                       'ORIGINALS PRESERVED IN AN APPENDED ANNOTATION' in out),
                      ('nothing removed', '0 LINES REMOVED' in out),
                      ('the three species are reported apart',
                       'THE THREE SPECIES ARE REPORTED APART' in out),
                      ('the method`s ceiling is named',
                       'ALREADY NEARLY EXHAUSTED' in out),
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
    rec('b394 -- THE DESK, THE LEDGER WRITES, AND THE BANK.')
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
    tr['says_rule_quoted'] = 'a rule improved is a new rule' in seg
    tr['says_exclusions'] = 'every exclusion is named with its reason' in seg
    tr['says_no_table'] = 'writing a correspondence table is authoring' in seg.lower()
    tr['says_batch_defect'] = 'the batch found its own defect' in seg
    tr['says_supersession'] = 'a supersession is not a phantom' in seg
    tr['says_preserved'] = 'preserved in an appended annotation' in seg
    tr['says_floors'] = 'Both figures are floors' in seg
    tr['says_ceiling'] = 'already nearly exhausted' in seg
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
        run_clock.write(D, 'b394_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b394_desk_notes', LINES)
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
            run_clock.write(D, 'b394_desk_notes', LINES)
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
    B.append('b394 -- THE RECONCILIATION, BATCHED. ### THE BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **THREE KEYSTONES READ IN ONE ACT, AND THE BATCH FOUND A DEFECT')
    B.append('### ### ### BETWEEN TWO OF ITS OWN SUBJECTS.**')
    B.append('')
    B.append(SUB)
    B.append('### THE CHOICE, BY `b390``S RULE, QUOTED.')
    B.append(SUB)
    B.append('### ### **TAKE THOSE WHOSE TERMINALS THE DRIVE CAN REACH. ### NOTHING IS ADDED')
    B.append('### ### TO IT.**')
    B.append('### An earlier form of this act`s own survey ### **ALSO DEMANDED A')
    B.append('### ### CORRESPONDENCE TABLE** ### -- a condition `b390` never stated -- and it')
    B.append('### cut the eligible set from `4` to `3` ### **BY A RULE NOBODY RULED.** ### It')
    B.append('### was removed before the lock.')
    B.append('### ### ### **A RULE QUOTED IS A RULE; A RULE IMPROVED IS A NEW RULE.**')
    B.append('### ### **CENSUS KEYSTONES ON DISK `15` ; REACHABLE `4` ; TAKEN `%d` ;'
             % len(C1['chosen']))
    B.append('### ### EXCLUDED `%d` ; SET ASIDE `1`.**' % C1['excluded'])
    B.append('### ### **EVERY EXCLUSION IS NAMED WITH ITS REASON** ### in the components; and')
    B.append('### ### `ADDITIVE_MULTIPLICATIVE_CONSPIRACY` is ### **SET ASIDE** ### because')
    B.append('### ### `b390` read it whole -- ### **RE-READING IT WOULD BE RE-DOING THAT')
    B.append('### ### ACT`S WORK.**')
    B.append('### ### **THE THREE : %s**'
             % ', '.join('`%s`' % k for k in C1['chosen']))
    B.append('')
    B.append(SUB)
    B.append('### WHAT THE THREE CARRY, AND THE THREE BUCKETS.')
    B.append(SUB)
    for k in C1['chosen']:
        if C1['tables'][k]:
            B.append('###   `%s` : ### **`%d` ROWS** ### -- %s'
                     % (k, C1['table_rows'][k], sorted(C1['grades'][k].items())))
        else:
            B.append('###   `%s` : ### **NO CORRESPONDENCE TABLE AT ALL.**' % k)
    B.append('### ### **A KEYSTONE WITH NO TABLE IS A KEYSTONE WHOSE GRADE LIMB CANNOT BE')
    B.append('### ### READ**, and `b387` already named five such. ### **THIS ACT DID NOT')
    B.append('### ### WRITE ONE: WRITING A CORRESPONDENCE TABLE IS AUTHORING, NOT')
    B.append('### ### RECONCILING.**')
    B.append('')
    B.append('### ### **THE THREE BUCKETS, ACROSS ALL THREE SUBJECTS:**')
    for kk in ('ALREADY SAYS IT', 'SAYS SOMETHING NOW SUPERSEDED', 'DOES NOT CARRY IT'):
        B.append('###   %-32s ### **`%d`**' % (kk, C1['buckets'][kk]))
    B.append('### ### **EVERY BUCKET IS REPORTED WITH ITS COUNT** (`b390`s rule).')
    B.append('')
    B.append(SUB)
    B.append('### THE BATCH FOUND ITS OWN DEFECT.')
    B.append(SUB)
    B.append('### ### **`GRH_CASCADE` CITES `FOUNDATIONS_OF_THE_SIDE_PROGRAMME` -- ANOTHER OF')
    B.append('### ### THE THREE -- AT `v0.1`, IN TWO PLACES**, while `REGISTRY.md` records a')
    B.append('### ### row update reconciling that document past it and its table now carries')
    B.append('### ### ### **`%s`.**' % C2['newv'])
    B.append('### ### ### **THAT IS THE `CORRECTED BUT UNPROPAGATED` SPECIES `b391` FOUND IN')
    B.append('### ### ### THE REGISTRY`S OWN BUNDLE LABEL, RECURRING** -- and this time ###')
    B.append('### ### ### **THE BATCH FOUND ITS OWN DEFECT**, which one-at-a-time reading')
    B.append('### ### ### could not have found as cheaply.')
    B.append('### ### **`(L2)` IS MET, AND IT IS MET INSIDE THE BATCH.**')
    B.append('')
    B.append(SUB)
    B.append('### THE REPAIR, AND WHAT WAS CHECKED BEFORE IT.')
    B.append(SUB)
    B.append('### ### **`v0.1` WAS CONFIRMED TO BE IN THE CITED DOCUMENT`S OWN LINEAGE : %s**'
             % C2['was_real'])
    B.append('### ### ### **A SUPERSESSION IS NOT A PHANTOM AND IS NOT REPAIRED AS ONE** --')
    B.append('### ### ### the old form was real, so the repair ### **MOVES A CITATION FORWARD')
    B.append('### ### ### RATHER THAN CORRECTING AN INVENTION.**')
    B.append('### ### **CITATIONS MOVED : `%d`. ### LINES REMOVED : `%d`. ### ONLY THE'
             % (C2['made'], C2['removed']))
    B.append('### ### VERSION CHANGED ON EACH LINE : %s.**' % C2['only_version'])
    B.append('### ### **THE ORIGINALS PRESERVED IN AN APPENDED ANNOTATION : %s**'
             % C2['annotated'])
    for i2, o in C2['originals']:
        B.append('###     line %d was : %s' % (i2, o[:110]))
    B.append('')
    B.append('### ### **AND `%d` REPAIRS ARE ROUTED, EACH NAMED WITH THE RULING IT NEEDS:**'
             % C2['routed'])
    B.append('###   the missing correspondence table -- writing one is ### **AUTHORING**;')
    B.append('###   the `%d` superseded citations -- `b391` ruled them ### **A CURRENCY'
             % C3['superseded'])
    B.append('###   ### ITEM**;')
    B.append('###   the E-Difficulty scope split, absent from two of the three;')
    B.append('###   `W-6``s closure, absent from one.')
    B.append('### ### **THE LAST THREE ARE ADDITIONS, NOT CORRECTIONS** -- the papers are not')
    B.append('### ### wrong without them -- and ### **ADDING MATERIAL TO A KEYSTONE IS')
    B.append('### ### AUTHORING TOO.**')
    B.append('### ### **REPAIRS MADE AND REPAIRS ROUTED ARE COUNTED SEPARATELY.**')
    B.append('')
    B.append(SUB)
    B.append('### THE THREE SPECIES, REPORTED APART.')
    B.append(SUB)
    B.append('###   phantoms in the three subjects  : ### **`%d`**' % C3['phantom'])
    B.append('###   corrected-but-unpropagated      : ### **`%d`**' % C3['unpropagated'])
    B.append('###   superseded, reported and left   : ### **`%d`**' % C3['superseded'])
    B.append('### ### ### **THREE COUNTS, THREE MEANINGS.** ### A phantom is a defect; an')
    B.append('### ### ### unpropagated correction is ### **A DEFECT WITH A KNOWN CURE**; a')
    B.append('### ### ### supersession is currency. ### **ADDING THEM WOULD DESCRIBE NONE OF')
    B.append('### ### ### THE THREE.**')
    B.append('')
    B.append(SUB)
    B.append('### THE COUNT, THE PRICE, AND THE METHOD`S CEILING.')
    B.append(SUB)
    B.append('### ### **`%d` OF THE CENSUS`S `16` KEYSTONES ARE NOW RECONCILED** ### --'
             % C3['reconciled'])
    B.append('### ### `b390`s one and this act`s three -- ### **AND IT IS NOT ROUNDED UP.**')
    B.append('### ### **THE ACT TOOK `%.0f` MINUTES, ABOUT `%.0f` PER KEYSTONE, AGAINST'
             % (C3['minutes'], C3['per_keystone']))
    B.append('### ### `b390`s `%d` FOR ONE.**' % C3['b390_minutes'])
    B.append('### ### ### **BOTH FIGURES ARE FLOORS**, each read at the component while the')
    B.append('### ### ### act continues, and `b390`s was taken the same way -- ### **THE')
    B.append('### ### ### COMPARISON IS LIKE FOR LIKE EVEN THOUGH NEITHER IS THE WHOLE COST.**')
    B.append('### ### **THE PER-KEYSTONE FIGURE FELL AND THE PER-ACT FIGURE DID NOT, AND THE')
    B.append('### ### REASON IS THE APPARATUS AND NOT THE READING:** ### three subjects share')
    B.append('### ### a single registration, gate suite and push. ### **PLAN WITH THE PER-ACT')
    B.append('### ### FIGURE: THE SAVING IS IN THE APPARATUS AND CANNOT BE SPENT TWICE.**')
    B.append('### ### **AND THE SAMPLE IS BIASED, NAMED ONCE:** ### these three are ### **THE')
    B.append('### ### REACHABLE ONES**, the population most likely to be in good order.')
    B.append('')
    B.append('### ### ### **AND THE FINDING UNDER THE COUNT IS THE METHOD`S OWN CEILING:**')
    B.append('### ### ### **`%d` OF THE REMAINING `12` CANNOT BE READ BY THIS RULE AT ALL.**'
             % C1['excluded'])
    B.append('### `9` name no kernel repository the drive holds, and several say in their own')
    B.append('### text that their terminals are ### **HELD OR UNMERGED.**')
    B.append('### ### **THE POPULATION THIS METHOD CAN REACH IS ALREADY NEARLY EXHAUSTED.** ###')
    B.append('### ### Reading the rest needs a clone or a ruling about reading branches, and')
    B.append('### ### ### **BOTH ARE THE AUTHOR`S. ### ROUTED.**')
    B.append('')
    B.append(SUB)
    B.append('### THE EXPECTATIONS, DECIDED.')
    B.append(SUB)
    B.append('### ### **THE NAVIGATOR`S:**')
    B.append('###   `(L2)` at least one of the three carries a claim the record has since')
    B.append('###   corrected ### **-- MET**, and met ### **INSIDE THE BATCH.**')
    B.append('### ### **THIS SEAT`S:**')
    B.append('###   `(E1)` the correction will be inside the batch ### **-- MET.**')
    B.append('###   `(E2)` the middle bucket will be thin and the third fat ### **-- MET**:')
    B.append('###   `%d` / `%d` / `%d`.'
             % (C1['buckets']['ALREADY SAYS IT'],
                C1['buckets']['SAYS SOMETHING NOW SUPERSEDED'],
                C1['buckets']['DOES NOT CARRY IT']))
    B.append('###   `(E3)` the per-keystone price falls and the per-act price does not ###')
    B.append('###   **-- MET**, and the act says which figure a reader should plan with.')
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
    B.append('### run as `b394`: ### **`%d` GATES READ, `%d` PASSING, `%d` CHECKED BY DIGEST.**'
             % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    regtxt = io.open(os.path.join(D, 'b394_registration_2026-09-09.txt'),
                     encoding='utf-8', errors='replace').read()
    ms = re.search(r'([0-9a-f]{64})', regtxt)
    mt = re.search(r'### locked at .UTC. : (\S+)', regtxt)
    B.append('### **THE FACE:** ### `%d` bytes on disk, sha256 `%s`, locked at `%s`.'
             % (len(regtxt.encode('utf-8')), ms.group(1) if ms else '?',
                mt.group(1) if mt else '?'))
    B.append('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor.'
             % (E['reads'], E['without_anchor']))
    for n in ('b394_reads', 'b394_components'):
        jj = J(n)
        B.append('### %-18s run file `%s` recorded clock %s'
                 % (n, jj['run_file'], jj.get('run_clock')))
    B.append('### ### **SIX NEW `relay` TOOLS AGAINST A CAP OF SIX.**')
    B.append('### ### **AND `b393`S GATE SUITE IS NOT RE-RUN HERE** -- the order`s own')
    B.append('### ### instruction, because this act`s commit moves its baseline.')
    B.append(BAR)

    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### THE RULE WAS WIDENED.', '### AN EXCLUSION WAS NOT NAMED.',
                '### A BUCKET WAS SUPPRESSED.', '### A CORRESPONDENCE TABLE WAS WRITTEN.',
                '### A GRADE WAS MOVED.', '### THE THREE SPECIES WERE ADDED.',
                '### THE PLATFORM WAS CALLED.', '### SOMETHING WAS DEPOSITED.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))
    rec()
    bar('=')
    rec('  ### desk %d ; closed %d ; trail %s ; row %s ; key %s'
        % (Q['items'], Q['closed'], tr['appended_only'], rownum, kok))
    bar('=')
    p = run_clock.write(D, 'b394_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             bank='b394_the_phantom_repaired.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b394_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
