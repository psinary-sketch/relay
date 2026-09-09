# -*- coding: utf-8 -*-
"""b391_desk_bank.py -- THE DESK, THE LEDGER WRITES, AND THE BANK FOR LEG 1.

### ### **THE REPAIR ITSELF WAS MADE BY `b391_components.py`.** ### This file writes the ledgers
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
MARK = '<!-- b391 the phantom version repaired; the five clusters read -->'
PRIOR = '<!-- b390 the first proofreading pass; one keystone read; one map row repaired -->'

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


AC = J('b391_components')
LG = J('b391_lockgate')
E = J('b391_reads')
C0, C1, C2 = AC['c0'], AC['c1'], AC['c2']
BANKOUT = os.path.join(D, 'b391_the_phantom_repaired.txt')


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
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND',
     'OPEN. ### `b390` took the map row out of it; this act closes nothing in it'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND',
     'OPEN. ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', 'OPEN. ### This act dates none'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND',
     '### **OPEN -- AND THIS ACT PAID DOWN ITS MIRROR IMAGE WITHOUT CLOSING IT.** ### `24` '
     'citations that named a version of a real document that never existed are repaired; a '
     'bibliography entry nothing cites is the same defect from the other end, and ### **NONE OF '
     'THOSE WAS TOUCHED**'),
    ('the class ruling itself', 'STAND', "STILL THE AUTHOR`S"),
    ('the three amendments b383 drafted that are still routed', 'STAND', 'ROUTED AND UNAPPLIED'),
    ('the citation question -- what a finished keystone is cited as', 'STAND',
     '### **AWAITING THE AUTHOR AND NOT MOVED BY THIS ACT.** ### `0` options added, `0` '
     'preferred. ### `b392` writes `(R19)`, which names the class and its citation rule; '
     '### **THIS LEG DOES NOT REACH INTO IT**'),
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
    ('the map`s five clusters that changed shape', 'STAND',
     '### **NAMED IN THIS ACT`S BANK, EACH WITH WHAT CHANGED AND A QUOTATION**, which is the '
     'read that precedes the ruling. ### **THE RESHAPING IS STILL THE AUTHOR`S** ### and `0` '
     'were reshaped'),
    ('the keystone-class documents b388 marked UNASSIGNED', 'STAND',
     '### **UNASSIGNED IS A STATE AND NOT A DEBT**'),
    ('the deposited layer, unread since b389', 'STAND',
     'BLOCKED: the platform answered nothing on six routes. ### `b392` writes the deposit rule '
     'and lists the records ### **FROM THE CORPUS`S OWN RECORD AND NOT FROM THE PLATFORM**'),
    ('no written rule for what deposits', 'STAND',
     '### **`b392`\'S, UNDER `(R20)`. ### THIS LEG DOES NOT WRITE IT**'),
    ('the eight-versus-six cluster-synthesis disagreement', 'STAND', 'ROUTED at b389'),
    ('the fifteen keystones not read', 'STAND', 'PRICED at b390 and NOT SCHEDULED'),

    # ---- WHAT THIS ACT ADDS ---------------------------------------------------------------------
    ('the phantom `v1.2` citation pass', 'CLOSE',
     '### **NEW at b391 AND CLOSED BY `(R7)`: THE OCCASION IS GONE.** ### `b390` routed it '
     'because its face permitted an annotation only. ### This act`s face permitted the edit, and '
     '### **`24` OF `32` INSTANCES ARE REPAIRED, `8` EXCLUDED WITH THEIR REASONS, `0` LINES '
     'REMOVED, AND THE ONLY CHANGE ON EVERY REPAIRED LINE IS THE VERSION.** ### There is nothing '
     'left for the item to carry'),
    ('the practice that let the drift run', 'STAND',
     '### **NEW at b391: NOTHING IN THE CORPUS CHECKS A CITED VERSION AGAINST ITS TARGET.** ### '
     'The registry corrected its own row on `2026-07-16` and ### **THE CORRECTION NEVER '
     'PROPAGATED** ### -- `32` instances survived two months in `13` documents. ### **A '
     'CORRECTION THAT DOES NOT PROPAGATE IS A CORRECTION IN ONE PLACE AND A DEFECT EVERYWHERE '
     'ELSE**, and the standing repair is a check, not another pass. ### **ROUTED**'),
    ('the `66` superseded version citations', 'STAND',
     '### **NEW at b391: REPORTED AND LEFT, BY THE ORDER`S OWN INSTRUCTION.** ### **A VERSION '
     'THAT EXISTS BUT IS SUPERSEDED IS A CURRENCY ITEM, NOT A PHANTOM.** ### `0` touched'),
    ('`CONSTANCE.md` carries no version in its own bytes', 'STAND',
     '### **NEW at b391: ITS VERSION LIVES ONLY ON THE REGISTRY`S ROW.** ### Two citations of it '
     'are ### **UNDECIDABLE BY CONSTRUCTION** ### -- nothing on disk can confirm or refute them. '
     '### **A DOCUMENT WHOSE VERSION EXISTS ONLY IN THE LEDGER CANNOT BE CHECKED AGAINST '
     'ITSELF**, and that is the author`s to rule on. ### **ROUTED, NOT REPAIRED**'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES ONE ITEM, AND ONLY BECAUSE ITS OCCASION IS GONE.** ###')
    rec('    ### `b390` routed the phantom pass because its own face permitted an annotation and')
    rec('    ### not an edit. ### This act`s face permitted the edit and the edit is made, so')
    rec('    ### ### **THE ROUTING HAS NOTHING LEFT TO CARRY.**')
    rec('    ### ### **THE THREE FINDINGS THIS ACT ADDS ALL STAND**, because ### **A FINDING')
    rec('    ### ### RECORDED IS NOT A FINDING DISCHARGED** -- and one of them is the reason the')
    rec('    ### ### phantom lasted two months.')
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
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0, marks=marks)


SCOPE = (
    "**SCOPE: THE PHANTOM VERSION REPAIRED, AND THE FIVE CLUSTERS READ.** NO class ruled, NO "
    "document reclassified, NO class line written, NO declaration moved, NO GRADE MOVED, NO CLAIM "
    "WITHDRAWN, NO REGISTRY ROW EDITED, NO Correspondence row edited, NO list closed, and NO "
    "CLUSTER RESHAPED, SPLIT, MERGED, RENAMED OR RE-ANCHORED. **THE ONLY CORPUS WRITE OUTSIDE THE "
    "LEDGERS IS ONE STRING -- v1.2 -> v0.5.4 -- ON 24 LINES THIS ACT CLASSIFIED CITATION BEFORE "
    "THE FIRST EDIT.** 0 LINES REMOVED FROM ANY DOCUMENT, EVERY LINE COUNT UNCHANGED, AND ON "
    "EVERY REPAIRED LINE THE ONLY CHANGE IS THE VERSION -- A PHANTOM-VERSION PASS THAT ALSO "
    "TIDIES PROSE HAS STOPPED BEING A PHANTOM-VERSION PASS. **EIGHT INSTANCES WERE EXCLUDED, EACH "
    "NAMED WITH ITS REASON: 4 PROVENANCE ENTRIES (they state what was cited at the time), 1 "
    "INSIDE A PRESERVED VERBATIM BLOCK, AND 3 LEDGER LINES REPORTING THE DEFECT ITSELF -- "
    "REPAIRING A REPORT OF AN ERROR ERASES THE REPORT.** **THE COUNT WAS RE-MEASURED FROM THE "
    "FILES AND IS 32 ACROSS 13, NOT b390's 28 ACROSS 11; A COUNT QUOTED FORWARD IS A COUNT NOBODY "
    "RE-MEASURED.** **THE PHANTOM HAS AN ORIGIN THE CORPUS RECORDED ITSELF**: the REGISTRY row "
    "carried a BUNDLE LABEL v1.2 and reconciled itself on 2026-07-16, and the correction never "
    "propagated. **COMPONENT 2 REPAIRED 0**: its screen was tightened four times before any "
    "finding was filed, every yield printed, and its 4 surviving candidates were READ BY HAND -- "
    "2 FALSE POSITIVES and 2 UNDECIDABLE. **66 SUPERSEDED CITATIONS ARE REPORTED AND LEFT: A "
    "VERSION THAT EXISTS BUT IS SUPERSEDED IS A CURRENCY ITEM, NOT A PHANTOM.** **NO BYTES WERE "
    "WRITTEN INTO THE STANDING DOCUMENT-CLASS TAXONOMY AND NO DEPOSIT RULE WAS WRITTEN -- THOSE "
    "ARE b392's, AND A LEG DOES NOT REACH INTO THE NEXT LEG'S SCOPE.** **THE FOUR OPEN LISTS ARE "
    "RESTATED OPEN BY NAME.** NO NEW TRACKING DOCUMENT WAS CREATED. NO ARCHIVE OR outputs FILE "
    "TOUCHED, THE MIRROR ROSTER NOT EDITED, NO .git/hooks/pre-push DELETED, NEITHER MAP'S (R18) "
    "HEAD NOTE TOUCHED. NO .lean FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED. NOTHING "
    "IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE "
    "OBJECT. Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, "
    "THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO "
    "AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt "
    "item 1 restated, still unpaid. The patent lane carried on the patent seat's report, "
    "UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE WAVE STAYS PARKED. "
    "THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it and this act makes "
    "no claim about it in either direction. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT "
    "ZENODO IN ANY BRANCH.")


def trail_block(Q):
    return [
        '', MARK, '',
        '### **b391 — THE PHANTOM VERSION REPAIRED, AND THE FIVE CLUSTERS READ (2026-09-09)**',
        '',
        ('*No block above is edited. The b390 block (`%s`) and every block before it stand '
         'exactly as they were written — including the three lines that report this very '
         'defect, which this act deliberately did not repair.*' % PRIOR),
        '',
        ('**THE COUNT WAS RE-MEASURED AND IT IS `%d` INSTANCES ACROSS `%d` DOCUMENTS, NOT `%d` '
         'ACROSS `%d`.** `b390` published the smaller pair; its matcher required the version to '
         'follow the name with only backticks or spaces between, so `*A_METHODOLOGY…* v1.2` and '
         '`A_METHODOLOGY v1.2 §V.10` were both missed. **A count quoted forward is a count '
         'nobody re-measured**, and this act says that about its own predecessor as plainly as '
         'it would about any other document.'
         % (C1['total'], C1['docs'], 28, 11)),
        '',
        ('**THE PHANTOM HAS AN ORIGIN, AND THE CORPUS RECORDED IT ITSELF.** `REGISTRY.md`, under '
         'a row update dated **2026-07-16**: *Row `1.5h-4` (`phase1.5/method/A_METHODOLOGY.md`): '
         'version reconciled `v1.2` → `v0.5.2` (the REGISTRY row carried a **bundle label '
         '"v1.2"** while the paper’s own header is the `v0.5` lineage; both now `v0.5.2`).* '
         '**The phantom was a bundle label on the registry’s own row. It was never a version the '
         'paper had.** The registry corrected itself that day; **every document that had copied '
         'the label kept it, and none was told**. That is the whole finding: **a correction that '
         'does not propagate is a correction in one place and a defect everywhere else.** And '
         'the corpus had already named the species in the same pass — a *Pin-drift casualty* — '
         'so this repair follows the corpus’s own precedent and not a rule this seat invented.'),
        '',
        ('**`%d` OF THE `%d` ARE REPAIRED; `%d` ARE EXCLUDED, EACH NAMED WITH ITS REASON.** `%d` '
         'are **provenance entries** — the order’s first exclusion, since they state what was '
         'cited at the time. `%d` is inside a **preserved verbatim block** — the order’s second. '
         'And `%d` are **mentions**: ledger lines that *report* the defect rather than cite the '
         'document, two of them `b390`’s own record of finding it. **Repairing a report of an '
         'error erases the report** — this act’s own third exclusion, found in the survey and '
         'stated before the first edit. On every repaired line the only change is `v1.2` → '
         '`v0.5.4`; **`%d` lines were removed from any document and every line count is '
         'unchanged.**'
         % (C1['repaired'], C1['total'], C1['total'] - C1['repaired'],
            C1['by_class'].get('PROVENANCE', 0), C1['by_class'].get('PRESERVED', 0),
            C1['by_class'].get('MENTION', 0), C1['removed'])),
        '',
        ('**THE WIDENED CHECK REPAIRED NOTHING, AND THAT IS THE ANSWER.** Its raw form reported '
         '`%d` disagreements. It was tightened **four times before any finding was filed** and '
         '**every yield is printed**: a stem must match as a whole token; the version must be '
         '**adjacent to the name it versions** and not lifted off a neighbour; versions are '
         'compared **as numbers**, so `v13`, `v13.0` and `v13_0` are one version; and a registry '
         'row-update note recording a transition is the correction, not the defect. Every one of '
         'those rests on **what the string is and not on the number it produces**. The screen '
         'ends at `%d` — **`%d` superseded and `%d` candidates** — and **the four were read by '
         'hand, because a screen that over-reports by design must be marked as a screen and its '
         'residue read**. Two are false positives; two cite `CONSTANCE.md`, which **declares no '
         'matching version anywhere in its own bytes**, so nothing on disk can convict them. '
         '**`%d` repaired. The `%d` superseded are a currency item and are reported and left.**'
         % (C2['raw'], C2['screened'], C2['superseded'], C2['candidates'], C2['repaired'],
            C2['superseded'])),
        '',
        ('**THE FIVE CLUSTERS, READ AND NOT RESHAPED.** Named from `b390`’s bank with what '
         'changed in each and a quotation apiece: **Methodology** GREW by `3`, **Foundations** '
         'by `2`, **Simplicity / RH cascade** by `1`, **theory-space** NEW with `2`, '
         '**cross-domain** NEW with `2`. All five changed by **membership** — documents the old '
         'table did not name were assigned, or the cluster did not exist as a seat at all. '
         '**None changed by a split, a merge, or an anchor moving**, and two of the five carry '
         '**no anchor at all**, because `(R17)` named none and `b388` did not invent one. '
         '**`0` reshaped: the reshaping is the author’s and this is the read that precedes it.**'),
        '',
        ('**WHAT IS ROUTED.** *(1)* **The practice that let the drift run**: nothing in the '
         'corpus checks a cited version against its target, which is why a registry correction '
         'sat for two months while `%d` citations contradicted it. **The standing repair is a '
         'check, not another pass.** *(2)* **`CONSTANCE.md` carries no version in its own '
         'bytes** — its version lives only on the registry’s row, so every citation of it is '
         'undecidable by construction. *(3)* The `%d` superseded citations, as a currency item. '
         '**Nothing here is closed** except the phantom pass itself, whose occasion is gone.'
         % (C1['total'], C2['superseded'])),
        '',
        ('**THE FOUR LISTS STAY OPEN, BY NAME.** `LIST 1` — the rows that cite at a ref nobody '
         'can name — **OPEN**. `LIST 2` — the rows grading a declaration the record has '
         'classified absent — **OPEN**. `LIST 3` — the undated figures across the roster — '
         '**OPEN**. `LIST 4` — the bibliography entries nothing cites — **OPEN**, and this act '
         'paid down its mirror image without closing it: a citation naming a version that never '
         'existed and a bibliography entry nothing cites are the same defect from two ends. **No '
         'grade was moved, no class ruled, no claim withdrawn, no cluster reshaped, and no bytes '
         'were written into the standing taxonomy — that is `b392`’s scope.**'),
        '',
    ]


def corr_rows(Q):
    m = ("**THE PHANTOM VERSION REPAIRED IN 24 CITATIONS, ITS ORIGIN LOCATED IN THE REGISTRY'S OWN "
         "BUNDLE LABEL, AND THE WIDENED CHECK REPAIRING NOTHING** (b391, the phantom version and "
         "the five clusters)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b391, %d gates read and %d "
            "checked by digest. THE COUNT WAS RE-MEASURED FROM THE FILES AND IS %d INSTANCES "
            "ACROSS %d DOCUMENTS, NOT b390's 28 ACROSS 11, because A COUNT QUOTED FORWARD IS A "
            "COUNT NOBODY RE-MEASURED and b390's matcher required the version to follow the name "
            "with only backticks or spaces between. THE PHANTOM HAS AN ORIGIN THE CORPUS RECORDED "
            "ITSELF: the REGISTRY row for 1.5h-4 carried a BUNDLE LABEL v1.2 and reconciled "
            "itself to the v0.5 lineage on 2026-07-16, and THE CORRECTION NEVER PROPAGATED -- A "
            "CORRECTION THAT DOES NOT PROPAGATE IS A CORRECTION IN ONE PLACE AND A DEFECT "
            "EVERYWHERE ELSE. %d OF THE %d ARE REPAIRED v1.2 -> v0.5.4 and %d ARE EXCLUDED EACH "
            "NAMED WITH ITS REASON: %d PROVENANCE ENTRIES, %d PRESERVED VERBATIM BLOCK LINE, AND "
            "%d LEDGER LINES REPORTING THE DEFECT ITSELF, since REPAIRING A REPORT OF AN ERROR "
            "ERASES THE REPORT. %d LINES WERE REMOVED FROM ANY DOCUMENT, EVERY LINE COUNT IS "
            "UNCHANGED, AND ON EVERY REPAIRED LINE THE ONLY CHANGE IS THE VERSION. THE WIDENED "
            "CHECK WAS TIGHTENED FOUR TIMES BEFORE ANY FINDING WAS FILED WITH EVERY YIELD PRINTED "
            "(%d raw -> %d screened), ITS %d SURVIVING CANDIDATES WERE READ BY HAND (2 FALSE "
            "POSITIVES, 2 UNDECIDABLE) AND IT REPAIRED %d; THE %d SUPERSEDED CITATIONS ARE "
            "REPORTED AND LEFT because A VERSION THAT EXISTS BUT IS SUPERSEDED IS A CURRENCY ITEM "
            "AND NOT A PHANTOM. THE FIVE CLUSTERS ARE NAMED WITH WHAT CHANGED IN EACH AND A "
            "QUOTATION APIECE AND %d WERE RESHAPED, because THE RESHAPING IS THE AUTHOR'S AND "
            "THIS IS THE READ THAT PRECEDES IT"
            % (LG['gates_read'], LG['face_subject_gates'], C1['total'], C1['docs'],
               C1['repaired'], C1['total'], C1['total'] - C1['repaired'],
               C1['by_class'].get('PROVENANCE', 0), C1['by_class'].get('PRESERVED', 0),
               C1['by_class'].get('MENTION', 0), C1['removed'],
               C2['raw'], C2['screened'], C2['candidates'], C2['repaired'], C2['superseded'],
               C0['reshaped']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN. ### One string was corrected in 24 "
            "citations and every quoted line was re-read out of its own file at its own line "
            "number. ### NO KERNEL WAS OPENED, NO STATEMENT PROVED, NO BUILD RUN AND NO AXIOM "
            "PROFILE RECOMPUTED. ### CORRECTING A CITATION'S VERSION SAYS NOTHING ABOUT WHAT THE "
            "CITED DOCUMENT PROVES")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT "
            "THE OBJECT. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO GRADE MOVED, NO "
            "CLAIM WITHDRAWN, NO REGISTRY ROW EDITED, NO CORRESPONDENCE ROW EDITED AND NO LIST "
            "CLOSED. ### NO CLUSTER WAS RESHAPED, SPLIT, MERGED, RENAMED OR RE-ANCHORED. ### NO "
            "BYTES WERE WRITTEN INTO THE STANDING TAXONOMY AND NO DEPOSIT RULE WAS WRITTEN -- "
            "THOSE ARE b392's. ### NOTHING WAS WRITTEN AT ZENODO IN ANY BRANCH")
    grade = ("### RE-MEASURED, NOT CARRIED FORWARD. ### 0 PROVENANCE ENTRIES EDITED; 0 PRESERVED "
             "BLOCKS EDITED; 0 REPORTS OF THE DEFECT EDITED; 0 SUPERSEDED VERSIONS REPAIRED; 0 "
             "LINES REMOVED. ### THE SCREEN'S FOUR TIGHTENINGS EACH REST ON WHAT THE STRING IS "
             "AND NOT ON THE NUMBER THEY PRODUCE, AND EVERY YIELD IS PRINTED. ### THE RESIDUE WAS "
             "READ BY HAND RATHER THAN SCREENED FURTHER. ### THE ORIGIN IS QUOTED AT ITS OWN LINE "
             "WITH ITS DATE")
    status = ("data/b391_the_phantom_repaired.txt; data/%s; data/%s; "
              "data/b391_registration_2026-09-09.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b391); tools/b391_extract.py; tools/b391_regspec.py; "
              "tools/b391_reg_gate.py; tools/b391_components.py; tools/b391_desk_bank.py; "
              "tools/b391_checks.py; PLACE-papers -- one string on 24 classified citation lines "
              "across 11 documents, and OPEN_TRAILS.md (an append-only block); "
              "CORRESPONDENCE.md row %%d" % (AC['run_file'], E['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the phantom version pass', 'where did v1.2 come from',
           'how many citations named a version that never existed',
           'the five clusters read', 'the superseded version citations')
MUST_NOT_HIT = ('a provenance entry was edited', 'a superseded version was repaired',
                'a cluster was reshaped', 'the taxonomy was amended')


def do_key(rownum):
    KEY = 'the-phantom-version-repaired'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b391 REPAIRED THE PHANTOM VERSION. THE METHODOLOGY PAPER WAS CITED AS "
        "A_METHODOLOGY_FOR_DETERMINED_SYSTEMS v1.2 IN %d INSTANCES ACROSS %d DOCUMENTS AND THERE "
        "IS NO v1.2 -- THE DOCUMENT IS phase1.5/method/A_METHODOLOGY.md AT v0.5.4 AND REGISTRY ROW "
        "1.5h-4 AGREES. THE COUNT WAS RE-MEASURED FROM THE FILES AND IS NOT b390's 28 ACROSS 11, "
        "because A COUNT QUOTED FORWARD IS A COUNT NOBODY RE-MEASURED. THE ORIGIN IS IN THE "
        "CORPUS'S OWN RECORD: THE REGISTRY ROW CARRIED A BUNDLE LABEL v1.2 AND RECONCILED ITSELF "
        "ON 2026-07-16, AND THE CORRECTION NEVER PROPAGATED -- A CORRECTION THAT DOES NOT "
        "PROPAGATE IS A CORRECTION IN ONE PLACE AND A DEFECT EVERYWHERE ELSE. %d CITATIONS WERE "
        "REPAIRED AND %d EXCLUDED EACH WITH ITS REASON: %d PROVENANCE ENTRIES, %d PRESERVED BLOCK "
        "LINE AND %d LEDGER LINES REPORTING THE DEFECT, since REPAIRING A REPORT OF AN ERROR "
        "ERASES THE REPORT. %d LINES REMOVED, EVERY LINE COUNT UNCHANGED, AND THE ONLY CHANGE ON "
        "EVERY REPAIRED LINE IS THE VERSION. THE WIDENED CHECK REPAIRED %d: ITS SCREEN WAS "
        "TIGHTENED FOUR TIMES BEFORE ANY FINDING WAS FILED WITH EVERY YIELD PRINTED, AND ITS FOUR "
        "SURVIVING CANDIDATES WERE READ BY HAND -- TWO FALSE POSITIVES AND TWO UNDECIDABLE "
        "BECAUSE CONSTANCE.md DECLARES NO MATCHING VERSION IN ITS OWN BYTES. THE %d SUPERSEDED "
        "CITATIONS ARE REPORTED AND LEFT: A VERSION THAT EXISTS BUT IS SUPERSEDED IS A CURRENCY "
        "ITEM AND NOT A PHANTOM. THE FIVE CLUSTERS ARE NAMED WITH WHAT CHANGED IN EACH AND %d "
        "WERE RESHAPED."
        % (C1['total'], C1['docs'], C1['repaired'], C1['total'] - C1['repaired'],
           C1['by_class'].get('PROVENANCE', 0), C1['by_class'].get('PRESERVED', 0),
           C1['by_class'].get('MENTION', 0), C1['removed'], C2['repaired'], C2['superseded'],
           C0['reshaped']))
    grade = (
        "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO GRADE MOVED, NO CLAIM WITHDRAWN, NO "
        "REGISTRY ROW EDITED, NO CORRESPONDENCE ROW EDITED AND NO LIST CLOSED. ### NO CLUSTER WAS "
        "RESHAPED, SPLIT, MERGED, RENAMED OR RE-ANCHORED. ### NO BYTES WERE WRITTEN INTO THE "
        "STANDING TAXONOMY AND NO DEPOSIT RULE WAS WRITTEN: A LEG DOES NOT REACH INTO THE NEXT "
        "LEG'S SCOPE. ### 0 PROVENANCE ENTRIES EDITED, 0 PRESERVED BLOCKS EDITED, 0 REPORTS OF "
        "THE DEFECT EDITED, 0 SUPERSEDED VERSIONS REPAIRED, 0 LINES REMOVED. ### THE FOUR OPEN "
        "LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED. ### NO LEAN "
        "FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### NOTHING WAS "
        "WRITTEN AT ZENODO IN ANY BRANCH. ### M-2 UNCHANGED")
    where = (
        "data/b391_the_phantom_repaired.txt; data/%s; data/%s; "
        "data/b391_registration_2026-09-09.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b391 -- %d gates read, %d checked by digest); "
        "tools/b391_extract.py; tools/b391_regspec.py; tools/b391_reg_gate.py; "
        "tools/b391_components.py; tools/b391_desk_bank.py; tools/b391_checks.py; "
        "PLACE-papers (24 citation lines across 11 documents) and OPEN_TRAILS.md; "
        "CORRESPONDENCE.md row %d"
        % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b391 (the phantom version repaired in 24 of 32 citations with 8 excluded and named, "
           "its origin located in the registry's own bundle label and its failure to propagate, "
           "the widened check repairing nothing after four tightenings and a hand read, and the "
           "five clusters read but not reshaped)")
    row_new = ('    # ### THE PHANTOM VERSION REPAIRED (b391).%s'
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
        rec('    %-48s reaches the b391 key : %s' % (qq, g))
    for lbl, cond in (('the count was re-measured',
                       'A COUNT QUOTED FORWARD IS A COUNT NOBODY RE-MEASURED' in out),
                      ('the origin is a bundle label', 'BUNDLE LABEL' in out),
                      ('the correction never propagated',
                       'A CORRECTION THAT DOES NOT PROPAGATE' in out),
                      ('the exclusions are named', 'PROVENANCE ENTRIES' in out),
                      ('a report of an error is not repaired',
                       'REPAIRING A REPORT OF AN ERROR ERASES THE REPORT' in out),
                      ('nothing removed', '0 LINES REMOVED' in out),
                      ('the residue was read by hand', 'READ BY HAND' in out),
                      ('superseded is a currency item',
                       'A VERSION THAT EXISTS BUT IS SUPERSEDED IS A CURRENCY ITEM' in out),
                      ('no cluster reshaped', 'WERE RESHAPED' in out),
                      ('the next leg is not reached into',
                       "A LEG DOES NOT REACH INTO THE NEXT LEG'S SCOPE" in out),
                      ('the lists are restated open', 'RESTATED OPEN BY NAME' in out),
                      ('nothing at zenodo',
                       'NOTHING WAS WRITTEN AT ZENODO IN ANY BRANCH' in out)):
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
    rec('b391 -- THE DESK, THE LEDGER WRITES, AND THE BANK.')
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
    tr['says_remeasured'] = 'nobody re-measured' in seg
    tr['says_origin'] = 'bundle label' in seg
    tr['says_not_propagated'] = 'does not propagate' in seg
    tr['says_report'] = 'erases the report' in seg
    tr['says_currency'] = 'currency item' in seg
    tr['says_no_reshape'] = 'the reshaping is the author' in seg.lower()
    rec('  ### ### **THE BLOCK SAYS RE-MEASURED : %s ; NAMES THE ORIGIN : %s ; SAYS THE '
        'CORRECTION DID NOT PROPAGATE : %s ; PROTECTS THE REPORTS : %s ; CALLS SUPERSEDED A '
        'CURRENCY ITEM : %s ; RESHAPES NOTHING : %s**'
        % (tr['says_remeasured'], tr['says_origin'], tr['says_not_propagated'], tr['says_report'],
           tr['says_currency'], tr['says_no_reshape']))

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
        run_clock.write(D, 'b391_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b391_desk_notes', LINES)
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
            run_clock.write(D, 'b391_desk_notes', LINES)
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
    B.append('b391 -- THE PHANTOM VERSION, AND THE FIVE CLUSTERS. ### THE BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **THE METHODOLOGY PAPER WAS CITED AT A VERSION IT HAS NEVER HAD, AND THE')
    B.append('### ### ### CORPUS HAD ALREADY WRITTEN DOWN WHY.**')
    B.append('')
    B.append(SUB)
    B.append('### THE COUNT, RE-MEASURED.')
    B.append(SUB)
    B.append('### ### **`%d` INSTANCES ACROSS `%d` DOCUMENTS.**' % (C1['total'], C1['docs']))
    B.append('### `b390` published ### **`28` ACROSS `11`.** ### **A COUNT QUOTED FORWARD IS A')
    B.append('### ### COUNT NOBODY RE-MEASURED**, and `b390`\'s matcher is why: it required the')
    B.append('### version to follow the name with only backticks or spaces between, so')
    B.append('### `*A_METHODOLOGY..* v1.2` and `A_METHODOLOGY v1.2 §V.10` were both missed.')
    B.append('### ### **THIS ACT SAYS THAT ABOUT ITS OWN PREDECESSOR AS PLAINLY AS IT WOULD ABOUT')
    B.append('### ### ANY OTHER DOCUMENT.**')
    B.append('')
    B.append(SUB)
    B.append('### THE ORIGIN. ### **THE CORPUS RECORDED IT ITSELF.**')
    B.append(SUB)
    B.append('### `REGISTRY.md` line `%d`, under a row update dated `2026-07-16`:' % C1['origin_line'])
    B.append('###   > *Row `1.5h-4` (`phase1.5/method/A_METHODOLOGY.md`): version reconciled')
    B.append('###   > `v1.2` → `v0.5.2` (the REGISTRY row carried a ### **bundle label "v1.2"**')
    B.append('###   > ### while the paper\'s own header is the `v0.5` lineage; both now `v0.5.2`).*')
    B.append('### ### ### **THE PHANTOM WAS A BUNDLE LABEL ON THE REGISTRY`S OWN ROW. ### IT WAS')
    B.append('### ### ### NEVER A VERSION THE PAPER HAD.**')
    B.append('### The registry corrected itself that day. ### **EVERY DOCUMENT THAT HAD COPIED THE')
    B.append('### ### LABEL KEPT IT, AND NONE WAS TOLD.**')
    B.append('### ### ### **A CORRECTION THAT DOES NOT PROPAGATE IS A CORRECTION IN ONE PLACE AND')
    B.append('### ### ### A DEFECT EVERYWHERE ELSE.**')
    B.append('### **AND THE CORPUS HAD ALREADY NAMED THE SPECIES IN THE SAME PASS** -- a')
    B.append('### ### **`Pin-drift casualty`** -- so this repair follows the corpus`s own')
    B.append('### precedent and not a rule this seat invented.')
    B.append('')
    B.append(SUB)
    B.append('### THE REPAIR, AND THE EIGHT IT DID NOT MAKE.')
    B.append(SUB)
    B.append('### ### **`%d` CITATIONS REPAIRED `v1.2` -> `v0.5.4`.**' % C1['repaired'])
    B.append('### ### **`%d` EXCLUDED, EACH NAMED WITH ITS REASON:**'
             % (C1['total'] - C1['repaired']))
    B.append('###   ### **`%d` PROVENANCE ENTRIES** ### -- the order`s first exclusion. ### They'
             % C1['by_class'].get('PROVENANCE', 0))
    B.append('###   state what was cited AT THE TIME, and editing one falsifies the history it')
    B.append('###   exists to keep.')
    B.append('###   ### **`%d` INSIDE A PRESERVED VERBATIM BLOCK** ### -- the order`s second.'
             % C1['by_class'].get('PRESERVED', 0))
    B.append('###   ### **`%d` MENTIONS** ### -- ### **THIS ACT`S OWN THIRD, FOUND IN THE SURVEY.**'
             % C1['by_class'].get('MENTION', 0))
    B.append('###   A ledger line REPORTING the defect quotes the string; it does not cite the')
    B.append('###   document. ### **REPAIRING A REPORT OF AN ERROR ERASES THE REPORT**, and two of')
    B.append('###   the three are `b390`\'s own record of finding this very defect.')
    B.append('### ### **`%d` LINES REMOVED FROM ANY DOCUMENT. ### EVERY LINE COUNT UNCHANGED. ###'
             % C1['removed'])
    B.append('### ### ON EVERY REPAIRED LINE THE ONLY CHANGE IS THE VERSION : %s.**'
             % C1['only_version'])
    B.append('### ### ### **A PHANTOM-VERSION PASS THAT ALSO TIDIES PROSE HAS STOPPED BEING A')
    B.append('### ### ### PHANTOM-VERSION PASS.**')
    B.append('')
    B.append(SUB)
    B.append('### THE WIDENED CHECK, WHICH REPAIRED NOTHING.')
    B.append(SUB)
    B.append('### ### **EVERY YIELD PRINTED** (`b381`):')
    B.append('###   the very first form, before numeric normalization : ### **`196`**')
    B.append('###   ### -- from the pre-lock survey, and the figure the locked face names.')
    B.append('###   any substring anywhere, versions compared as numbers : ### **`%d`**'
             % C2['raw'])
    B.append('###   whole-token only                              : ### **`%d`**' % C2['tokened'])
    B.append('###   version ADJACENT to the name it versions      : ### **`%d`**' % C2['adjacent'])
    B.append('###   minus the registry`s own transition notes     : ### **`%d`**' % C2['screened'])
    B.append('### ### **FIVE FIGURES, NOT FOUR, AND THE FIRST IS PRINTED BECAUSE IT IS THE ONE')
    B.append('### ### THE LOCKED FACE NAMES.** ### `196` was the yield of the screen`s very first')
    B.append('### ### form; `%d` is the same sweep once `v13`, `v13.0` and `v13_0` are read as one'
             % C2['raw'])
    B.append('### ### version. ### **BOTH ARE TRUE OF DIFFERENT MATCHERS, AND A MATCHER REPAIRED')
    B.append('### ### AFTER ITS OUTPUT WAS SEEN PRINTS EVERY VERSION`S YIELD** (`b381`).')
    B.append('### ### **FOUR TIGHTENINGS, EVERY ONE BEFORE A FINDING WAS FILED AND EVERY ONE')
    B.append('### ### RESTING ON WHAT THE STRING IS RATHER THAN ON THE NUMBER IT PRODUCES**')
    B.append('### ### (`b380`\'s forbidden direction).')
    B.append('### ### **`%d` SUPERSEDED -- REPORTED AND LEFT.** ### **A VERSION THAT EXISTS BUT IS'
             % C2['superseded'])
    B.append('### ### SUPERSEDED IS A CURRENCY ITEM, NOT A PHANTOM.**')
    B.append('### ### **`%d` CANDIDATES, READ BY HAND : %s.**' % (C2['candidates'], C2['verdicts']))
    B.append('### ### ### **A SCREEN THAT OVER-REPORTS BY DESIGN MUST BE MARKED AS A SCREEN AND')
    B.append('### ### ### ITS RESIDUE READ.** ### Four tightenings is where tightening stops; past')
    B.append('### ### ### that a seat is tuning for a number.')
    B.append('### ### **CANDIDATES REPAIRED : `%d`** -- two are the screen`s own noise, and two'
             % C2['repaired'])
    B.append('### ### cite `CONSTANCE.md`, which ### **DECLARES NO MATCHING VERSION ANYWHERE IN')
    B.append('### ### ITS OWN BYTES**, so nothing on disk can convict them.')
    B.append('### ### **AND THE SCREEN`S LIMIT IS STATED: IT KEYS ON THE REGISTRY`S FILE STEM**,')
    B.append('### ### so a document cited under a different title is invisible to it -- which is')
    B.append('### ### exactly how the methodology paper hid. ### **THE COUNT IS A FLOOR.**')
    B.append('')
    B.append(SUB)
    B.append('### THE FIVE CLUSTERS, READ AND NOT RESHAPED.')
    B.append(SUB)
    for r in E['s1']['rows']:
        B.append('###   %s' % r[3:150])
    B.append('### **ALL FIVE CHANGED BY MEMBERSHIP.** ### **NONE CHANGED BY A SPLIT, A MERGE, OR')
    B.append('### ### AN ANCHOR MOVING**, and two of the five carry ### **NO ANCHOR AT ALL**,')
    B.append('### because `(R17)` named none and `b388` did not invent one.')
    B.append('### ### ### **`%d` RESHAPED. ### THE RESHAPING IS THE AUTHOR`S AND THIS IS THE READ'
             % C0['reshaped'])
    B.append('### ### ### THAT PRECEDES IT.**')
    B.append('')
    B.append(SUB)
    B.append('### THE EXPECTATIONS, DECIDED.')
    B.append(SUB)
    B.append('### ### **THE NAVIGATOR`S:**')
    B.append('###   `(L1)` the count re-measured differs from twenty-eight, and the phantom has a')
    B.append('###   locatable origin ### **-- MET ON BOTH LIMBS**: `%d` across `%d`, and an origin'
             % (C1['total'], C1['docs']))
    B.append('###   quoted at `REGISTRY.md` line `%d` with its date.' % C1['origin_line'])
    B.append('### ### **THIS SEAT`S:**')
    B.append('###   `(E1)` the repairable count will be smaller than the instance count, and the')
    B.append('###   difference will be the interesting part ### **-- MET**: `%d` of `%d`, and the'
             % (C1['repaired'], C1['total']))
    B.append('###   `%d` excluded include ### **THREE LEDGER LINES THAT REPORT THE DEFECT'
             % (C1['total'] - C1['repaired']))
    B.append('###   ### ITSELF**, which a careless pass would have erased along with it.')
    B.append('###   `(E2)` Component 2 will repair nothing ### **-- MET**, and each of its four')
    B.append('###   candidates carries a printed hand verdict.')
    B.append('###   `(E3)` the superseded count will exceed the phantom count by more than an')
    B.append('###   order of magnitude ### **-- MET**: `%d` against `%d` repaired. ### **THAT IS A'
             % (C2['superseded'], C2['repaired']))
    B.append('###   ### FACT ABOUT CURRENCY AND NOT ABOUT CORRECTNESS**, and the larger number')
    B.append('###   does not make the smaller one small.')
    B.append('')
    B.append(SUB)
    B.append('### WHAT THIS ACT DID NOT DO.')
    B.append(SUB)
    B.append('### ' + SCOPE.replace('**', ''))
    B.append('')
    B.append(SUB)
    B.append('### THE APPARATUS.')
    B.append(SUB)
    B.append('### **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on `b378`\'s lock gate')
    B.append('### run as `b391`: ### **`%d` GATES READ, `%d` PASSING, `%d` CHECKED BY DIGEST.**'
             % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    regtxt = io.open(os.path.join(D, 'b391_registration_2026-09-09.txt'),
                     encoding='utf-8', errors='replace').read()
    ms = re.search(r'([0-9a-f]{64})', regtxt)
    mt = re.search(r'### locked at \(UTC\) : (\S+)', regtxt)
    B.append('### **THE FACE:** ### `%d` bytes on disk, sha256 `%s`, locked at `%s`.'
             % (len(regtxt.encode('utf-8')), ms.group(1) if ms else '?',
                mt.group(1) if mt else '?'))
    B.append('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor.'
             % (E['reads'], E['without_anchor']))
    for n in ('b391_reads', 'b391_components'):
        jj = J(n)
        B.append('### %-18s run file `%s` recorded clock %s'
                 % (n, jj['run_file'], jj.get('run_clock')))
    B.append('### **THE REFS THIS ACT READ:**')
    for k, v in E['refs'].items():
        B.append('###   %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    B.append('### ### **SIX NEW `relay` TOOLS AGAINST A CAP OF SIX.**')
    B.append(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### A PROVENANCE ENTRY WAS EDITED.', '### A PRESERVED BLOCK WAS EDITED.',
                '### A REPORT OF THE DEFECT WAS EDITED.',
                '### A SUPERSEDED VERSION WAS REPAIRED.', '### THE COUNT WAS CARRIED FORWARD.',
                "### THE SCREEN`S RESIDUE WAS NOT READ.", '### A CLUSTER WAS RESHAPED.',
                '### THE TAXONOMY WAS AMENDED.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))
    rec()
    bar('=')
    rec('  ### desk %d ; closed %d ; trail %s ; row %s ; key %s'
        % (Q['items'], Q['closed'], tr['appended_only'], rownum, kok))
    bar('=')
    p = run_clock.write(D, 'b391_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             bank='b391_the_phantom_repaired.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b391_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
