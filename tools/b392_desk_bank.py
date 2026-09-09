# -*- coding: utf-8 -*-
"""b392_desk_bank.py -- THE DESK, THE LEDGER WRITES, AND THE BANK FOR LEG 2.

### ### **THE TWO AMENDMENTS WERE MADE BY `b392_components.py`.** ### This file writes the ledgers
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
MARK = '<!-- b392 the two rulings written: (R19) the finished keystone, (R20) the deposit rule -->'
PRIOR = '<!-- b391 the phantom version repaired; the five clusters read -->'

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


AC = J('b392_components')
LG = J('b392_lockgate')
C1, C2 = AC['c1'], AC['c2']
BANKOUT = os.path.join(D, 'b392_the_two_rulings.txt')


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
     '### **OPEN -- AND THIS ACT FOUND ONE OF ITS MEMBERS BY A DIFFERENT ROUTE.** ### The Day-1 '
     'deposit `19675356` is named ONLY as a bibliography entry in `INVARIANCE_BARRIERS.md`, and '
     'it is one of the two records failing the currency obligation. ### **THE LIST IS NOT '
     'CLOSED**'),
    ('the class ruling itself', 'CLOSE',
     '### **CLOSED BY `(R19)`, THE AUTHOR`S.** ### The finished keystone is now a named class '
     'with an obligation, a citation rule and a guard, written additively into the standing '
     'taxonomy. ### **THE OCCASION IS GONE**: the item asked for a ruling and the ruling is '
     'written. ### **WHICH DOCUMENTS BELONG IS A SEPARATE QUESTION AND IS NOT CLOSED**'),
    ('the citation question -- what a finished keystone is cited as', 'CLOSE',
     '### **CLOSED BY `(R19)`.** ### *A SYSTEMATIC SYNTHESIS WITH A VERIFICATION CONCORDANCE -- '
     'CITE THE SYNTHESIS FOR ORIENTATION, CITE EACH CONCORDANCE ROW AT ITS STATED GRADE*, with '
     'the guard that ### **THE CLASS CONFERS NO CITATION LICENSE THE TWO TIERS DO NOT ALREADY '
     'CONFER.** ### The question was what a finished keystone is cited as; it now has an answer '
     'in the standing record'),
    ('no written rule for what deposits', 'CLOSE',
     '### **CLOSED BY `(R20)`, THE AUTHOR`S.** ### Three limbs and a currency obligation, '
     'written into `REGISTRY.md` where the corpus`s precedence puts deposits, with `README.md` '
     'pointing at it. ### `b389` proved the absence; ### **THIS ACT ENDS IT**'),
    ('the three amendments b383 drafted that are still routed', 'STAND', 'ROUTED AND UNAPPLIED'),
    ('the download-layer book`s registry drift', 'STAND', "OPEN AND THE AUTHOR`S"),
    ('the six subject clusters with no keystone', 'STAND', '`NOT-YET-SYNTHESIZED` since b385'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', 'NOT RE-MEASURED'),
    ('the ten untracked run records of earlier acts', 'STAND', 'NAMED at b382, STILL UNTRACKED'),
    ('the legacy `.git/hooks/pre-push` copies', 'STAND', '### **RULED BY `(R16)`: THEY STAY**'),
    ('the untracked `.b304-backup` artifacts', 'STAND', 'NAMED at b386, still untracked'),
    ('the five keystones the union names that carry no correspondence table', 'STAND',
     'NAMED at b387 and ### **STILL THE AUTHOR`S** -- and `(R19)` now says what such a table '
     'must carry, which sharpens the item without closing it'),
    ('the 23 unreadable correspondence rows', 'STAND', 'NAMED at b388 by cause, and ROUTED'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the map`s five clusters that changed shape', 'STAND',
     '### **NAMED AT b391 WITH WHAT CHANGED IN EACH AND A QUOTATION APIECE.** ### **THE '
     'RESHAPING IS STILL THE AUTHOR`S** ### and `0` were reshaped by either leg'),
    ('the keystone-class documents b388 marked UNASSIGNED', 'STAND',
     '### **UNASSIGNED IS A STATE AND NOT A DEBT**'),
    ('the deposited layer, unread since b389', 'STAND',
     '### **STILL BLOCKED, AND THIS ACT DID NOT ASK AGAIN.** ### `(R20)`\'s census is taken '
     '### **FROM THE CORPUS`S OWN RECORD**, and every figure in it is labelled as the corpus`s '
     'claim about itself rather than a verified state'),
    ('the eight-versus-six cluster-synthesis disagreement', 'STAND', 'ROUTED at b389'),
    ('the fifteen keystones not read', 'STAND', 'PRICED at b390 and NOT SCHEDULED'),
    ('the practice that let the phantom drift run', 'STAND',
     'NEW at b391 and ### **STILL OPEN**: nothing checks a cited version against its target'),
    ('the `66` superseded version citations', 'STAND', 'REPORTED at b391 and LEFT'),
    ('`CONSTANCE.md` carries no version in its own bytes', 'STAND', 'ROUTED at b391'),

    # ---- WHAT THIS ACT ADDS ---------------------------------------------------------------------
    ('the two deposited records failing the currency obligation', 'STAND',
     '### **NEW at b392: `21432399` AND `19675356`.** ### Neither sits at a version a citable '
     'claim uses, nor carries a note saying it is historical -- the two limbs `(R20)` now '
     'states. ### **THE REMEDIATION IS ONE LINE EACH IN `REGISTRY.md` OR THE DEPOSIT NOTE, AND '
     'IT IS THE AUTHOR`S.** ### **NOTHING DEPOSITS AND THE PLATFORM IS NOT WRITTEN TO**'),
    ('whether `SIDE-kernel` has a current citable record', 'STAND',
     '### **NEW at b392, AND ROUTED AS A QUESTION RATHER THAN FILED AS A FINDING.** ### The '
     'deposit note`s three citable records are the monograph, `SIDE-lv-conservation` and the T7 '
     'search, and ### **`SIDE-kernel` IS NOT AMONG THEM** -- read off the note`s own line. ### '
     'But whether that is a defect under limb (a) depends on whether a published claim cites its '
     'terminals, ### **WHICH THIS ACT DID NOT MEASURE.** ### Its proximity test was withdrawn '
     'as unable to establish it'),
    ('placement into `Tier KC`', 'STAND',
     '### **NEW at b392: THE CLASS EXISTS AND NOBODY IS IN IT.** ### `(R19)` forbids '
     'reclassification by this act and names no candidate. ### **A CLASS NAMED IS NOT A CLASS '
     'POPULATED**, and the placement is a separate act and a separate decision'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES THREE ITEMS, AND ALL THREE BECAUSE THE AUTHOR RULED.** ###')
    rec('    ### `(R7)` closes an item whose occasion is gone. ### The class ruling asked for a')
    rec('    ### ruling and `(R19)` is written; the citation question asked what a finished')
    rec('    ### keystone is cited as and `(R19)` answers it; the missing deposit rule was proved')
    rec('    ### absent at `b389` and `(R20)` writes it.')
    rec('    ### ### ### **BUT A RULING WRITTEN IS NOT A CORPUS CONFORMING.** ### Placement into')
    rec('    ### ### ### the new class, and the two records that fail the obligation the new rule')
    rec('    ### ### ### states, are ### **ENTERED AS STANDING ITEMS IN THE SAME BREATH.**')
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
    "**SCOPE: THE TWO RULINGS WRITTEN -- (R19) THE FINISHED KEYSTONE AS A NAMED CLASS, (R20) THE "
    "DEPOSIT RULE WITH ITS CURRENCY OBLIGATION.** **BOTH AMENDMENTS ARE ADDITIVE AND EVERY PRIOR "
    "LINE OF THE TAXONOMY, THE REGISTRY AND THE README IS PRESENT AND BYTE-IDENTICAL AFTER THIS "
    "ACT, MEASURED AGAINST THE PRE-ACT BLOB; 0 LINES REMOVED FROM ANY OF THE THREE.** NO document "
    "reclassified, NO class line written on any document, NO candidate for the new class named -- "
    "(R19)'s own words. NO registry row, lineage or deposit figure edited; NO deposit note entry "
    "edited or removed. NO grade moved, NO claim withdrawn, NO Correspondence row edited, NO list "
    "closed, NO cluster reshaped, NEITHER MAP'S (R18) HEAD NOTE TOUCHED. **THE GUARD IS WRITTEN "
    "INTO THE CLASS AND NOT BESIDE IT -- THIS CLASS CONFERS NO CITATION LICENSE THE TWO TIERS DO "
    "NOT ALREADY CONFER -- AND BOTH FAILURES ARE QUOTED WITH IT: the June 2026 "
    "formation-universality over-claim and the August 2026 retirement of the scheme that spanned "
    "the tiers.** **(R20) IS WRITTEN INTO REGISTRY.md AND README.md POINTS AT IT: THE SOURCE OF "
    "TRUTH FIRST, THE FRONT DOOR POINTING AT IT.** **THE DEPOSIT CENSUS WAS TAKEN FROM THE "
    "CORPUS'S OWN RECORD AND NOT FROM THE PLATFORM, WHICH ANSWERED NOTHING ON SIX ROUTES AT b389 "
    "AND WAS NOT ASKED AGAIN; every figure is the corpus's claim about itself and is labelled "
    "so.** 16 DOIs known, 6 named by the deposit note (3 VERSION RECORDS AND THEIR 3 CONCEPT "
    "DOIs -- A DOI IS NOT A RECORD), 10 unlisted, EVERY ONE GIVEN A LIMB VERDICT. **2 RECORDS "
    "FAIL BOTH LIMBS, SO (L2) EXPECTED THREE AND IS REPORTED REFUTED: AN EXPECTATION IS NOT A "
    "TARGET AND A THIRD FAILURE WAS NOT MANUFACTURED TO MEET ONE.** **ONE RECORD WAS CLEARED "
    "ONLY BY AN ELIDED DOI THE MATCHER COULD NOT SEE, AND THE HAND READ THAT CLEARED IT IS "
    "PRINTED.** **AND THE SIDE-kernel FINDING THE SURVEY THOUGHT IT HAD WAS WITHDRAWN AS NOT "
    "ESTABLISHED BY THIS ACT'S INSTRUMENT AND ROUTED AS A QUESTION**, because its proximity test "
    "returned DOIs belonging to two other deposit lines and a third tightening would have been "
    "tuning for a result. **THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME.** NOTHING DEPOSITS; NO "
    "DOI WAS MINTED, CLAIMED OR EDITED; THE PLATFORM WAS NOT CALLED AT ALL. NO NEW TRACKING "
    "DOCUMENT WAS CREATED. NO ARCHIVE OR outputs FILE TOUCHED, THE MIRROR ROSTER NOT EDITED, NO "
    ".git/hooks/pre-push DELETED. NO .lean FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE "
    "RECOMPUTED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS "
    "COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or the roster; NO "
    "CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION "
    "STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's "
    "cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent "
    "seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE WAVE "
    "STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it and "
    "this act makes no claim about it in either direction.")


def trail_block(Q):
    return [
        '', MARK, '',
        '### **b392 — THE TWO RULINGS WRITTEN (2026-09-09)**',
        '',
        ('*No block above is edited. The b391 block (`%s`) and every block before it stand exactly '
         'as they were written.*' % PRIOR),
        '',
        ('**RULING `(R19)`, THE AUTHOR’S: THE FINISHED KEYSTONE IS A NAMED CLASS.** '
         '`phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md` gains a fifth class, **additively, '
         'with every prior line preserved byte-for-byte**: **Tier KC — the finished keystone**, a '
         'document that **synthesizes a subject cluster** *and* **carries the verification '
         'apparatus**. Its obligation: every load-bearing claim stated clearly in the body and '
         'carried by a row in a **correspondence table placed after the front matter where a '
         'reader meets it**, each row naming what backs it **in the front door’s own '
         'vocabulary** — and a claim whose backing is not machine-checked **says so in the row** '
         '— plus glossary, bibliography and other tables as the document needs them. Its citation '
         'rule, written for a reader who has never seen the taxonomy: **A SYSTEMATIC SYNTHESIS '
         'WITH A VERIFICATION CONCORDANCE — CITE THE SYNTHESIS FOR ORIENTATION, CITE EACH '
         'CONCORDANCE ROW AT ITS STATED GRADE.**'),
        '',
        ('**AND THE GUARD IS WRITTEN INTO THE CLASS, NOT BESIDE IT: THIS CLASS CONFERS NO '
         'CITATION LICENSE THE TWO TIERS DO NOT ALREADY CONFER.** It names a **conjunction** and '
         'a **furniture obligation**; nothing in it permits a synthesis conclusion to be cited as '
         'certification. Both failures are quoted with the guard so a later reader meets the '
         'reason with the rule: the **June 2026 formation-universality over-claim**, where *a '
         'Tier-C synthesis panel … was read and cited as a Tier-K certification*, and the '
         '**August 2026 retirement** of `b186`’s scheme, whose *“SYNTHESIS” class spanned Tier K '
         'and Tier C at once — collapsing the very distinction the standing taxonomy exists to '
         'enforce*. **The class states what separates it from the retired one: the retired scheme '
         'spanned the tiers by dissolving them; `Tier KC` spans them by carrying both rules at '
         'once. A class that collapses the distinction is retired; a class that keeps both sides '
         'of it is a class.** **No document is reclassified into it and no candidate is named.**'),
        '',
        ('**RULING `(R20)`, THE AUTHOR’S: THE DEPOSIT RULE, WRITTEN, WITH A CURRENCY '
         'OBLIGATION.** Written into `REGISTRY.md`, where the corpus’s precedence puts deposits, '
         'with `README.md`’s deposit note **pointing at it and not restating it** — the source of '
         'truth first, the front door pointing at it. The rule: **a manuscript wave deposits with '
         'its companion papers; a kernel deposits when a published claim cites its terminals; a '
         'pre-registered search deposits because its registration committed to publishing every '
         'outcome.** The obligation: **every deposited record either sits at a version a citable '
         'claim uses, or carries a note saying it is historical. There is no third state.** '
         '**The rule is descriptive before it is prescriptive** — its three limbs are what the '
         'corpus already did, and the deposit note’s three citable records match them one for '
         'one: the monograph (a wave), `SIDE-lv-conservation` (a kernel published claims cite), '
         'the T7 matched-arc search (a registration that committed itself). **It is discovered, '
         'not imposed.**'),
        '',
        ('**THE CENSUS, FROM THE CORPUS’S OWN RECORD AND NOT FROM THE PLATFORM.** `b389` proved '
         'the platform answers on none of six routes; **this act did not ask it again**, and '
         'every figure below is the corpus’s claim about itself. The corpus names **`%d` DOIs**. '
         'The deposit note names **`%d` of them — `3` version records and their `3` concept DOIs; '
         '**a DOI is not a record**, and a count that conflates them describes neither. **`%d` '
         'are unlisted, and every one carries a limb verdict.** **`%d` pass limb (b)** — marked '
         'historical in an errata or a lineage line — and **`%d` fail both limbs**: `21432399`, a '
         'deposited monograph record named once at an errata about a stale version stamp, and '
         '`19675356`, a Day-1 deposit named only as a bibliography entry. Neither sits at a '
         'version a citable claim uses; neither carries a note saying it is historical.'
         % (C2['known'], C2['listed'], C2['unlisted'], C2['passes'], C2['fails'])),
        '',
        ('**`(L2)` EXPECTED AT LEAST THREE AND THE COUNT IS `%d`, SO IT IS REPORTED REFUTED.** '
         '**An expectation is not a target, and a third failure was not manufactured to meet '
         'one.** The locked face said so before the census ran. **And one record was cleared only '
         'by an elided DOI**: `REGISTRY.md`’s lineage line writes `SIDE-lv-conservation v0.6.0` '
         'as `…21433178`, which a full-DOI matcher cannot see — without the hand read it would '
         'have been convicted of a defect the registry had already cleared. **A predicate that '
         'knows one shape finds one shape.**' % C2['fails']),
        '',
        ('**AND ONE THING THIS ACT THOUGHT IT HAD, WITHDRAWN.** The survey read `SIDE-kernel` as '
         'a deposit line with **no current citable record** — limb (b) everywhere, limb (a) '
         'nowhere. The test for it was proximity: a DOI counts as a kernel record if '
         '`SIDE-kernel` sits within ninety characters before it. **That test returned DOIs '
         'belonging to two other deposit lines**, including the monograph’s own concept DOI. '
         '**Proximity is not attachment.** The component had already tightened twice; a third '
         'tightening, made after seeing the second disagree with the conclusion it was supposed '
         'to support, would have been **tuning for a result**. **The finding is withdrawn as not '
         'established by this act’s instrument and the question is routed.** What remains true '
         'and checkable, read off the deposit note’s own line: **`SIDE-kernel` is not among the '
         'three citable records** — and whether that is a defect under limb (a) depends on '
         'something this act did not measure.'),
        '',
        ('**WHAT CLOSES AND WHAT DOES NOT.** Three desk items close, all because the author '
         'ruled: **the class ruling** (asked for a ruling; `(R19)` is written), **the citation '
         'question** (asked what a finished keystone is cited as; `(R19)` answers it), and **no '
         'written rule for what deposits** (`b389` proved the absence; `(R20)` ends it). **But a '
         'ruling written is not a corpus conforming**: placement into `Tier KC`, the two records '
         'failing the obligation, and the `SIDE-kernel` question are entered as **standing items '
         'in the same breath**. **The four lists stay OPEN by name** — `LIST 1`, `LIST 2`, `LIST '
         '3`, and `LIST 4`, one of whose members this act met by a different route. **The five '
         'clusters’ reshaping stays awaiting the author, with the five named at `b391`.** The '
         'remediation is priced — one line each in `REGISTRY.md` or the deposit note — and is '
         '**the author’s**. **Nothing deposits and the platform is not written to.**'),
        '',
    ]


def corr_rows(Q):
    m = ("**THE TWO RULINGS WRITTEN: THE FINISHED KEYSTONE NAMED AS A CLASS WITH A GUARD AGAINST "
         "THE FAILURE THAT BUILT THE TIERS, AND THE DEPOSIT RULE WRITTEN WHERE THE CORPUS PUTS "
         "DEPOSITS** (b392, the two rulings written)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b392, %d gates read and %d checked "
            "by digest. (R19) ADDS Tier KC -- THE FINISHED KEYSTONE -- TO THE STANDING TAXONOMY "
            "ADDITIVELY, EVERY PRIOR LINE PRESERVED BYTE-FOR-BYTE AND 0 REMOVED: a document that "
            "SYNTHESIZES A SUBJECT CLUSTER AND CARRIES THE VERIFICATION APPARATUS, obliged to "
            "state every load-bearing claim in the body and carry it in a CORRESPONDENCE TABLE "
            "PLACED AFTER THE FRONT MATTER WHERE A READER MEETS IT, each row naming its backing IN "
            "THE FRONT DOOR'S OWN VOCABULARY and saying so when the backing is not "
            "machine-checked, plus glossary, bibliography and other tables as needed. ITS CITATION "
            "RULE: A SYSTEMATIC SYNTHESIS WITH A VERIFICATION CONCORDANCE -- CITE THE SYNTHESIS "
            "FOR ORIENTATION, CITE EACH CONCORDANCE ROW AT ITS STATED GRADE. ITS GUARD, WRITTEN "
            "INTO THE CLASS: THIS CLASS CONFERS NO CITATION LICENSE THE TWO TIERS DO NOT ALREADY "
            "CONFER, quoted beside the JUNE 2026 FORMATION-UNIVERSALITY OVER-CLAIM and the AUGUST "
            "2026 RETIREMENT of the scheme that spanned the tiers, so a later reader meets the "
            "reason with the rule; and the class states that THE RETIRED SCHEME SPANNED THE TIERS "
            "BY DISSOLVING THEM WHILE Tier KC SPANS THEM BY CARRYING BOTH RULES AT ONCE. NO "
            "DOCUMENT IS RECLASSIFIED AND NO CANDIDATE IS NAMED. (R20) WRITES THE DEPOSIT RULE "
            "INTO REGISTRY.md WITH README.md POINTING AT IT -- THE SOURCE OF TRUTH FIRST, THE "
            "FRONT DOOR POINTING AT IT: a manuscript wave deposits with its companion papers, a "
            "kernel deposits when a published claim cites its terminals, a pre-registered search "
            "deposits because its registration committed to publishing every outcome; and EVERY "
            "DEPOSITED RECORD EITHER SITS AT A VERSION A CITABLE CLAIM USES OR CARRIES A NOTE "
            "SAYING IT IS HISTORICAL, WITH NO THIRD STATE. THE RULE IS DESCRIPTIVE BEFORE IT IS "
            "PRESCRIPTIVE: the deposit note's three citable records match its three limbs ONE FOR "
            "ONE, so IT IS DISCOVERED AND NOT IMPOSED. THE CENSUS WAS TAKEN FROM THE CORPUS'S OWN "
            "RECORD AND NOT FROM THE PLATFORM, WHICH ANSWERED NOTHING ON SIX ROUTES AT b389 AND "
            "WAS NOT ASKED AGAIN: %d DOIs known, %d named by the note (3 VERSION RECORDS AND THEIR "
            "3 CONCEPT DOIs, since A DOI IS NOT A RECORD), %d unlisted and EVERY ONE GIVEN A LIMB "
            "VERDICT, %d passing limb (b) and %d FAILING BOTH LIMBS. SO (L2) EXPECTED THREE AND IS "
            "REPORTED REFUTED, because AN EXPECTATION IS NOT A TARGET. ONE RECORD WAS CLEARED ONLY "
            "BY AN ELIDED DOI A FULL-DOI MATCHER CANNOT SEE, AND THE HAND READ IS PRINTED. AND THE "
            "SIDE-kernel FINDING WAS WITHDRAWN AS NOT ESTABLISHED BY THIS ACT'S INSTRUMENT, "
            "because PROXIMITY IS NOT ATTACHMENT and a third tightening would have been TUNING "
            "FOR A RESULT"
            % (LG['gates_read'], LG['face_subject_gates'], C2['known'], C2['listed'],
               C2['unlisted'], C2['passes'], C2['fails']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN. ### Two author-ruled amendments "
            "were written into the standing record and a census was taken from that record. ### "
            "NO KERNEL WAS OPENED, NO STATEMENT PROVED, NO BUILD RUN AND NO AXIOM PROFILE "
            "RECOMPUTED. ### NAMING A CLASS IS NOT PLACING A DOCUMENT IN IT, AND WRITING A "
            "DEPOSIT RULE IS NOT DEPOSITING")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT "
            "THE OBJECT. ### NO DOCUMENT RECLASSIFIED, NO CLASS LINE WRITTEN, NO GRADE MOVED, NO "
            "CLAIM WITHDRAWN, NO REGISTRY ROW OR LINEAGE OR DEPOSIT FIGURE EDITED, NO DEPOSIT "
            "NOTE ENTRY EDITED OR REMOVED, NO CORRESPONDENCE ROW EDITED, NO LIST CLOSED, NO "
            "CLUSTER RESHAPED. ### NOTHING DEPOSITS, NO DOI WAS MINTED CLAIMED OR EDITED, AND THE "
            "PLATFORM WAS NOT CALLED AT ALL")
    grade = ("### BOTH AMENDMENTS ADDITIVE WITH EVERY PRIOR LINE PRESERVED BYTE-FOR-BYTE AND 0 "
             "REMOVED. ### THE GUARD IS IN THE CLASS'S OWN TEXT AND BOTH FAILURES ARE QUOTED WITH "
             "IT. ### 0 DOCUMENTS PLACED IN THE NEW CLASS. ### THE CENSUS IS THE CORPUS'S OWN "
             "CLAIM ABOUT ITSELF AND IS LABELLED SO. ### (L2) IS REPORTED REFUTED ON THE COUNT "
             "THE COMPONENT MEASURED. ### ONE FINDING WAS WITHDRAWN RATHER THAN TUNED INTO "
             "EXISTENCE")
    status = ("data/b392_the_two_rulings.txt; data/%s; "
              "data/b392_registration_2026-09-09.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b392); tools/b392_regspec.py; "
              "tools/b392_reg_gate.py; tools/b392_components.py; tools/b392_desk_bank.py; "
              "tools/b392_checks.py; PLACE-papers "
              "phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md and REGISTRY.md and README.md "
              "(one appended section each) and OPEN_TRAILS.md (an append-only block); "
              "CORRESPONDENCE.md row %%d" % AC['run_file'])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('what is a finished keystone', 'how is a finished keystone cited',
           'the deposit rule', 'what deposits and when',
           'which deposited records fail the currency obligation')
MUST_NOT_HIT = ('a document was reclassified', 'prior taxonomy text was edited',
                'the platform was asked', 'something was deposited')


def do_key(rownum):
    KEY = 'the-two-rulings-r19-and-r20'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "RULING (R19), THE AUTHOR'S: THE FINISHED KEYSTONE IS A NAMED CLASS. Tier KC -- a document "
        "that SYNTHESIZES A SUBJECT CLUSTER AND CARRIES THE VERIFICATION APPARATUS -- was added to "
        "the standing document-class taxonomy ADDITIVELY, every prior line preserved "
        "byte-for-byte. ITS OBLIGATION: every load-bearing claim stated clearly in the body and "
        "carried by a row in a CORRESPONDENCE TABLE PLACED AFTER THE FRONT MATTER WHERE A READER "
        "MEETS IT, each row naming its backing IN THE FRONT DOOR'S OWN VOCABULARY, plus glossary, "
        "bibliography and other tables as needed. ITS CITATION RULE: A SYSTEMATIC SYNTHESIS WITH A "
        "VERIFICATION CONCORDANCE -- CITE THE SYNTHESIS FOR ORIENTATION, CITE EACH CONCORDANCE ROW "
        "AT ITS STATED GRADE. ITS GUARD: THIS CLASS CONFERS NO CITATION LICENSE THE TWO TIERS DO "
        "NOT ALREADY CONFER, quoted beside the June 2026 formation-universality over-claim and the "
        "August 2026 retirement of the scheme that spanned the tiers. NO DOCUMENT IS RECLASSIFIED "
        "AND NO CANDIDATE IS NAMED. RULING (R20), THE AUTHOR'S: THE DEPOSIT RULE, WRITTEN INTO "
        "REGISTRY.md WITH README.md POINTING AT IT. A MANUSCRIPT WAVE DEPOSITS WITH ITS COMPANION "
        "PAPERS; A KERNEL DEPOSITS WHEN A PUBLISHED CLAIM CITES ITS TERMINALS; A PRE-REGISTERED "
        "SEARCH DEPOSITS BECAUSE ITS REGISTRATION COMMITTED TO PUBLISHING EVERY OUTCOME. THE "
        "CURRENCY OBLIGATION: EVERY DEPOSITED RECORD EITHER SITS AT A VERSION A CITABLE CLAIM USES "
        "OR CARRIES A NOTE SAYING IT IS HISTORICAL, WITH NO THIRD STATE. THE RULE IS DESCRIPTIVE "
        "BEFORE IT IS PRESCRIPTIVE: the note's three citable records match its three limbs one for "
        "one. THE CENSUS WAS TAKEN FROM THE CORPUS'S OWN RECORD AND NOT FROM THE PLATFORM: %d DOIs "
        "known, %d named by the note, %d unlisted, %d passing limb (b) and %d FAILING BOTH LIMBS, "
        "so (L2) EXPECTED THREE AND IS REPORTED REFUTED. ONE RECORD WAS CLEARED ONLY BY AN ELIDED "
        "DOI. THE SIDE-kernel FINDING WAS WITHDRAWN AS NOT ESTABLISHED, because PROXIMITY IS NOT "
        "ATTACHMENT."
        % (C2['known'], C2['listed'], C2['unlisted'], C2['passes'], C2['fails']))
    grade = (
        "### NO DOCUMENT WAS RECLASSIFIED, NO CLASS LINE WRITTEN ON ANY DOCUMENT AND NO CANDIDATE "
        "NAMED. ### NO PRIOR LINE OF THE TAXONOMY, THE REGISTRY OR THE README WAS EDITED AND 0 "
        "LINES WERE REMOVED. ### NO REGISTRY ROW, LINEAGE OR DEPOSIT FIGURE EDITED; NO DEPOSIT "
        "NOTE ENTRY EDITED OR REMOVED. ### NO GRADE MOVED, NO CLAIM WITHDRAWN, NO CORRESPONDENCE "
        "ROW EDITED, NO LIST CLOSED, NO CLUSTER RESHAPED. ### NOTHING DEPOSITS AND THE PLATFORM "
        "WAS NOT CALLED AT ALL. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW "
        "TRACKING DOCUMENT WAS CREATED. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING "
        "COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED")
    where = (
        "data/b392_the_two_rulings.txt; data/%s; "
        "data/b392_registration_2026-09-09.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b392 -- %d gates read, %d checked by digest); "
        "tools/b392_regspec.py; tools/b392_reg_gate.py; tools/b392_components.py; "
        "tools/b392_desk_bank.py; tools/b392_checks.py; PLACE-papers "
        "phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md, REGISTRY.md, README.md and "
        "OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (AC['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b392 (the two rulings written: (R19) names Tier KC, the finished keystone, with an "
           "obligation, a citation rule for a stranger, and a guard quoted beside the two failures "
           "it exists to prevent; (R20) writes the deposit rule and its currency obligation where "
           "the corpus puts deposits, and the census from the corpus's own record finds two "
           "records failing both limbs, refuting (L2))")
    row_new = ('    # ### THE TWO RULINGS (b392).%s'
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
        rec('    %-48s reaches the b392 key : %s' % (qq, g))
    for lbl, cond in (('the class is named', 'Tier KC' in out),
                      ('the obligation names where the table goes',
                       'PLACED AFTER THE FRONT MATTER WHERE A READER MEETS IT' in out),
                      ('the citation rule is written for a stranger',
                       'CITE THE SYNTHESIS FOR ORIENTATION' in out),
                      ('the guard is in the statement',
                       'CONFERS NO CITATION LICENSE THE TWO TIERS DO NOT ALREADY CONFER' in out),
                      ('both failures are named',
                       'formation-universality over-claim' in out and 'retirement' in out),
                      ('no document reclassified',
                       'NO DOCUMENT IS RECLASSIFIED AND NO CANDIDATE IS NAMED' in out),
                      ('the three limbs are stated',
                       'A MANUSCRIPT WAVE DEPOSITS' in out and 'A KERNEL DEPOSITS WHEN' in out
                       and 'A PRE-REGISTERED SEARCH DEPOSITS' in out),
                      ('the obligation has no third state', 'WITH NO THIRD STATE' in out),
                      ('the rule is discovered not imposed',
                       'DESCRIPTIVE BEFORE IT IS PRESCRIPTIVE' in out),
                      ('the census avoided the platform',
                       "FROM THE CORPUS'S OWN RECORD AND NOT FROM THE PLATFORM" in out),
                      ('(L2) is refuted on the count', 'IS REPORTED REFUTED' in out),
                      ('the elided DOI is named', 'ELIDED' in out),
                      ('the withdrawn finding is named',
                       'WITHDRAWN AS NOT ESTABLISHED' in out and 'PROXIMITY IS NOT ATTACHMENT'
                       in out),
                      ('nothing deposits',
                       'NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL' in out),
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
    rec('b392 -- THE DESK, THE LEDGER WRITES, AND THE BANK.')
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
    tr['says_r19'] = '(R19)' in seg
    tr['says_r20'] = '(R20)' in seg
    tr['says_guard'] = 'CONFERS NO CITATION LICENSE' in seg
    tr['says_no_placement'] = 'No document is reclassified into it' in seg
    tr['says_no_third_state'] = 'no third state' in seg
    tr['says_not_platform'] = 'did not ask it again' in seg
    tr['says_refuted'] = 'REPORTED REFUTED' in seg
    tr['says_withdrawn'] = 'withdrawn as not established' in seg
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
        run_clock.write(D, 'b392_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b392_desk_notes', LINES)
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
            run_clock.write(D, 'b392_desk_notes', LINES)
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
    B.append('b392 -- THE TWO RULINGS WRITTEN. ### THE BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **TWO THINGS THE CORPUS HAD BEEN DOING WITHOUT A NAME OR A RULE')
    B.append('### ### ### NOW HAVE ONE.**')
    B.append('')
    B.append(SUB)
    B.append('### `(R19)` -- THE FINISHED KEYSTONE IS A NAMED CLASS.')
    B.append(SUB)
    B.append('### ### **`Tier KC` -- A DOCUMENT THAT SYNTHESIZES A SUBJECT CLUSTER *AND*')
    B.append('### ### CARRIES THE VERIFICATION APPARATUS**, added to the standing taxonomy')
    B.append('### ### **ADDITIVELY, EVERY PRIOR LINE PRESERVED BYTE-FOR-BYTE, `%d` REMOVED.**'
             % C1['file']['deleted'])
    B.append('### **ITS OBLIGATION:** ### every load-bearing claim stated clearly in the body')
    B.append('### and carried by a row in a ### **CORRESPONDENCE TABLE PLACED AFTER THE FRONT')
    B.append('### ### MATTER, WHERE A READER MEETS IT** ### -- not appended where only a')
    B.append('### returning reader will find it -- each row naming its backing ### **IN THE')
    B.append('### ### FRONT DOOR`S OWN VOCABULARY**, and saying so when that backing is not')
    B.append('### machine-checked; plus glossary, bibliography and other tables as needed.')
    B.append('### **ITS CITATION RULE, FOR A READER WHO HAS NEVER SEEN THE TAXONOMY:** ###')
    B.append('### *A SYSTEMATIC SYNTHESIS WITH A VERIFICATION CONCORDANCE -- CITE THE')
    B.append('### SYNTHESIS FOR ORIENTATION, CITE EACH CONCORDANCE ROW AT ITS STATED GRADE.*')
    B.append('')
    B.append('### ### ### **AND THE GUARD IS WRITTEN INTO THE CLASS, NOT BESIDE IT:** ###')
    B.append('### ### ### *this class confers no citation license the two tiers do not')
    B.append('### ### ### already confer.* ### It names a ### **CONJUNCTION** ### and a')
    B.append('### ### ### **FURNITURE OBLIGATION**; nothing in it permits a synthesis')
    B.append('### ### ### conclusion to be cited as certification.')
    B.append('### ### **BOTH FAILURES ARE QUOTED WITH THE GUARD : %s** ### -- the ### **JUNE'
             % (C1['quoted_failure'] and C1['quoted_retirement']))
    B.append('### ### 2026** ### formation-universality over-claim, where a Tier-C synthesis')
    B.append('### ### panel was ### *read and cited as a Tier-K certification*; and the ###')
    B.append('### ### **AUGUST 2026** ### retirement of the scheme whose *SYNTHESIS class')
    B.append('### ### spanned Tier K and Tier C at once -- collapsing the very distinction the')
    B.append('### ### standing taxonomy exists to enforce.*')
    B.append('### ### ### **SO THE CLASS STATES WHAT SEPARATES IT FROM THE RETIRED ONE:** ###')
    B.append('### ### ### the retired scheme spanned the tiers ### **BY DISSOLVING THEM**;')
    B.append('### ### ### `Tier KC` spans them ### **BY CARRYING BOTH RULES AT ONCE.**')
    B.append('### ### ### **A CLASS THAT COLLAPSES THE DISTINCTION IS RETIRED; A CLASS THAT')
    B.append('### ### ### KEEPS BOTH SIDES OF IT IS A CLASS.**')
    B.append('### ### **NO DOCUMENT IS RECLASSIFIED AND NO CANDIDATE IS NAMED : %s.**'
             % C1['no_placement'])
    B.append('')
    B.append(SUB)
    B.append('### `(R20)` -- THE DEPOSIT RULE, WITH ITS CURRENCY OBLIGATION.')
    B.append(SUB)
    B.append('### ### **WRITTEN INTO `REGISTRY.md`, WITH `README.md` POINTING AT IT** -- the')
    B.append('### ### source of truth first, the front door pointing at it, which is the')
    B.append('### ### ruling`s own instruction. ### Both additive: `+%d`/`-%d` and `+%d`/`-%d`.'
             % (C2['registry']['added'], C2['registry']['deleted'],
                C2['readme']['added'], C2['readme']['deleted']))
    B.append('### **THE RULE:** ### a manuscript wave deposits with its companion papers; a')
    B.append('### kernel deposits when a published claim cites its terminals; a')
    B.append('### pre-registered search deposits because its registration committed to')
    B.append('### publishing every outcome.')
    B.append('### ### **THE CURRENCY OBLIGATION:** ### every deposited record ### **EITHER**')
    B.append('### ### sits at a version a citable claim uses ### **OR** ### carries a note')
    B.append('### ### saying it is historical. ### **THERE IS NO THIRD STATE.**')
    B.append('### ### ### **AND THE RULE IS DESCRIPTIVE BEFORE IT IS PRESCRIPTIVE.** ### The')
    B.append('### ### ### deposit note`s three citable records match its three limbs ### **ONE')
    B.append('### ### ### FOR ONE**: the monograph (a wave), `SIDE-lv-conservation` (a kernel')
    B.append('### ### ### published claims cite), the T7 matched-arc search (a registration')
    B.append('### ### ### that committed itself). ### **IT IS DISCOVERED, NOT IMPOSED.**')
    B.append('')
    B.append(SUB)
    B.append('### THE CENSUS, FROM THE CORPUS`S OWN RECORD.')
    B.append(SUB)
    B.append('### ### **THE PLATFORM ANSWERED NOTHING ON SIX ROUTES AT `b389` AND WAS NOT')
    B.append('### ### ASKED AGAIN.** ### **EVERY FIGURE HERE IS THE CORPUS`S CLAIM ABOUT')
    B.append('### ### ITSELF**, labelled so rather than presented as a verified state.')
    B.append('###   DOIs the corpus names                    : ### **`%d`**' % C2['known'])
    B.append('###   named by the deposit note                : ### **`%d`** ### -- `3` version'
             % C2['listed'])
    B.append('###   ### records and their `3` concept DOIs. ### **A DOI IS NOT A RECORD.**')
    B.append('###   unlisted, each given a limb verdict      : ### **`%d`**' % C2['unlisted'])
    B.append('###   passing limb (b), marked historical      : ### **`%d`**' % C2['passes'])
    B.append('###   ### **FAILING BOTH LIMBS**                   : ### **`%d`**' % C2['fails'])
    B.append('### The two that fail: ### **`21432399`**, a deposited monograph record named')
    B.append('### once at an errata about a stale version stamp, and ### **`19675356`**, a')
    B.append('### Day-1 deposit named only as a bibliography entry. ### **NEITHER SITS AT A')
    B.append('### ### VERSION A CITABLE CLAIM USES; NEITHER CARRIES A HISTORICAL NOTE.**')
    B.append('')
    B.append('### ### **`(L2)` EXPECTED AT LEAST THREE. ### THE COUNT IS `%d`, SO IT IS'
             % C2['fails'])
    B.append('### ### REPORTED REFUTED.**')
    B.append('### ### ### **AN EXPECTATION IS NOT A TARGET, AND A THIRD FAILURE WAS NOT')
    B.append('### ### ### MANUFACTURED TO MEET ONE.** ### The locked face said so before the')
    B.append('### ### ### census ran, which is what makes the refutation worth reading.')
    B.append('### ### **AND ONE RECORD WAS CLEARED ONLY BY AN ELIDED DOI:** ### the registry`s')
    B.append('### lineage line writes `SIDE-lv-conservation v0.6.0` elided, which a full-DOI')
    B.append('### matcher cannot see. ### Without the hand read it would have been convicted')
    B.append('### of a defect the registry had already cleared. ### **A PREDICATE THAT KNOWS')
    B.append('### ### ONE SHAPE FINDS ONE SHAPE.**')
    B.append('')
    B.append(SUB)
    B.append('### AND ONE FINDING WITHDRAWN.')
    B.append(SUB)
    B.append('### The survey read `SIDE-kernel` as a deposit line with ### **NO CURRENT')
    B.append('### ### CITABLE RECORD** -- limb (b) everywhere, limb (a) nowhere. ### The test')
    B.append('### was proximity: a DOI counts as a kernel record if `SIDE-kernel` sits within')
    B.append('### ninety characters before it. ### **THAT TEST RETURNED DOIs BELONGING TO TWO')
    B.append('### ### OTHER DEPOSIT LINES**, including the monograph`s own concept DOI.')
    B.append('### ### ### **PROXIMITY IS NOT ATTACHMENT.**')
    B.append('### The component had already tightened twice. ### A third tightening, made')
    B.append('### after seeing the second disagree with the conclusion it was meant to')
    B.append('### support, would have been ### **TUNING FOR A RESULT**. ### **THE FINDING IS')
    B.append('### ### WITHDRAWN AS NOT ESTABLISHED BY THIS ACT`S INSTRUMENT AND THE QUESTION')
    B.append('### ### IS ROUTED.**')
    B.append('### **WHAT REMAINS TRUE AND CHECKABLE**, read off the deposit note`s own line:')
    B.append('### ### **`SIDE-kernel` IS NOT AMONG THE THREE CITABLE RECORDS** -- and whether')
    B.append('### ### that is a defect under limb (a) depends on something this act did not')
    B.append('### ### measure.')
    B.append('')
    B.append(SUB)
    B.append('### THE EXPECTATIONS, DECIDED.')
    B.append(SUB)
    B.append('### ### **THE NAVIGATOR`S:**')
    B.append('###   `(L2)` at least three deposited records fail the currency obligation ###')
    B.append('###   **-- REFUTED.** ### `%d` fail both limbs.' % C2['fails'])
    B.append('### ### **THIS SEAT`S:**')
    B.append('###   `(E1)` the three limbs will match the three citable records one for one')
    B.append('###   ### **-- MET.** ### The rule is discovered, not imposed.')
    B.append('###   `(E2)` most unlisted records will pass limb (b) ### **-- MET**: `%d` of'
             % C2['passes'])
    B.append('###   `%d`. ### **THE CORPUS HAS BEEN KEEPING ITS SUPERSESSIONS EVEN WITHOUT A'
             % C2['unlisted'])
    B.append('###   ### WRITTEN RULE TO KEEP THEM BY.**')
    B.append('###   `(E3)` the amendments will be the smallest writes of the sortie ###')
    B.append('###   **-- MET**: `+%d` lines across three files, against `b391`s `24` repaired'
             % (C1['file']['added'] + C2['registry']['added'] + C2['readme']['added']))
    B.append('###   citations. ### **A RULING IS A FEW HUNDRED WORDS; A DRIFT IS A HUNDRED')
    B.append('###   ### PLACES.**')
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
    B.append('### run as `b392`: ### **`%d` GATES READ, `%d` PASSING, `%d` CHECKED BY DIGEST.**'
             % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    regtxt = io.open(os.path.join(D, 'b392_registration_2026-09-09.txt'),
                     encoding='utf-8', errors='replace').read()
    ms = re.search(r'([0-9a-f]{64})', regtxt)
    mt = re.search(r'### locked at .UTC. : (\S+)', regtxt)
    B.append('### **THE FACE:** ### `%d` bytes on disk, sha256 `%s`, locked at `%s`.'
             % (len(regtxt.encode('utf-8')), ms.group(1) if ms else '?',
                mt.group(1) if mt else '?'))
    jj = J('b392_components')
    B.append('### b392_components   run file `%s` recorded clock %s'
             % (jj['run_file'], jj.get('run_clock')))
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
    p = run_clock.write(D, 'b392_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             bank='b392_the_phantom_repaired.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b392_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
