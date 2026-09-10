# -*- coding: utf-8 -*-
"""b398_desk_bank.py -- THE DESK, THE LEDGER WRITES, AND THE BANK.

### ### **THE ONLY CORPUS WRITE THIS ACT MAKES IS `(R21)`'S, AND `b398_components.py` MADE IT.**
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
MARK = '<!-- b398 the li-weil bridge: undecidable from the record, and (M) named -->'
PRIOR = ('<!-- b397 the unlanded work: eight of nine landed, and a queue with triggers -->')

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


SEALTXT = io.open(os.path.join(D, 'b398_registration_2026-09-10.txt'),
                  encoding='utf-8').read()
SEALHASH = re.search(r'sha256 of every byte ABOVE this block : ([0-9a-f]{64})', SEALTXT).group(1)
SEALSTAMP = re.search(r'locked at \(UTC\) : (\S+)', SEALTXT).group(1)

AC = J('b398_components')
LG = J('b398_lockgate')
E = J('b398_reads')
C1, C2, C3, C4 = AC['c1'], AC['c2'], AC['c3'], AC['c4']
TRG = AC['triggers']
BANKOUT = os.path.join(D, 'b398_the_li_weil_bridge.txt')


def blob(rel):
    r = subprocess.run(['git', 'show', 'HEAD:' + rel], cwd=PP, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


DESK = [
    ('M-2, under b310 cap', 'STAND', 'the aggregation is still SPECIFIED-NOT-STATED'),
    ("the object's conditions", 'STAND', "the conditions are the object's and none discharged"),
    ('the uniformity row U1', 'STAND', "the row's own refusal stands"),
    ('the instrument lane, PARKED under ruling R4', 'STAND',
     'PARKED, and ### **NOW LOAD-BEARING TWICE OVER:** ### two of the three work orders this act '
     'gave triggers to ### **CANNOT FIRE UNTIL IT IS UNPARKED**'),
    ('the instrument-audit lane, PARKED under ruling R22', 'STAND', 'PARKED at b397'),
    ('the wave, and the wave candidate list', 'STAND', "PARKED by the author's ruling"),
    ('the routed items, each with its owner', 'STAND', 'each still carries its owner'),
    ('the patent receipts, absent on the mounted volumes', 'STAND', "the patent seat owns it"),
    ('the count claim above the repaired Layer-1 list', 'STAND', 'no act sent to it since b369'),
    ("the retirement ledger's own lacunae", 'STAND', 'FILED, NOT INVENTED, AND NOT REPAIRED'),
    ('where the keystone census should live, ROUTED at b375', 'STAND', 'ROUTED to the author'),
    ("the census's definition-versus-operation drift", 'STAND', 'FILED at b377, NOT REPAIRED'),
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND',
     'OPEN. ### **TRIGGER: when a row of it is cited by an act.**'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND',
     'OPEN. ### This act moves no grade. ### **TRIGGER: when a grade must be defended.**'),
    ('LIST 3 -- the undated figures across the roster', 'STAND',
     'OPEN. ### This act dates none. ### **TRIGGER: when a figure is quoted forward.**'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND',
     'OPEN. ### **TRIGGER: at the next bibliography pass.**'),
    ('the three amendments b383 drafted that are still routed', 'STAND', 'ROUTED AND UNAPPLIED'),
    ('the download-layer book`s registry drift', 'STAND', "OPEN AND THE AUTHOR`S"),
    ('the six subject clusters with no keystone', 'STAND', '`NOT-YET-SYNTHESIZED` since b385'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', 'NOT RE-MEASURED'),
    ('the ten untracked run records of earlier acts', 'STAND', 'NAMED at b382, STILL UNTRACKED'),
    ('the legacy `.git/hooks/pre-push` copies', 'STAND', '### **RULED BY `(R16)`: THEY STAY**'),
    ('the untracked `.b304-backup` artifacts', 'STAND', 'NAMED at b386, still untracked'),
    ('the 23 unreadable correspondence rows', 'STAND', 'NAMED at b388 by cause, and ROUTED'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the keystone-class documents b388 marked UNASSIGNED', 'STAND',
     '### **UNASSIGNED IS A STATE AND NOT A DEBT**'),
    ('the deposited layer, unread since b389', 'STAND',
     'STILL BLOCKED; this act did not ask the platform'),
    ('the eight-versus-six cluster-synthesis disagreement', 'STAND', 'ROUTED at b389'),
    ('the practice that let the phantom drift run', 'STAND',
     'THREE INSTANCES now, and ### **THIS ACT FOUND A FOURTH:** ### `b332`s E0 ranking still '
     'calls `K5` the softest at `DEFINED-ONLY`, and `b333` conferred `DERIVES-ON-IMPORTS` on it '
     'the next day. ### **STILL OPEN**'),
    ('the `66` superseded version citations', 'STAND', 'REPORTED at b391 and LEFT'),
    ('`CONSTANCE.md` carries no version in its own bytes', 'STAND', 'ROUTED at b391'),
    ('placement into `Tier KC`', 'STAND', 'PRICED at b393 and STILL EMPTY'),
    ('whether `SIDE-kernel` has a current citable record', 'STAND', 'ROUTED at b392'),
    ('the anchor question, unanswerable for three of five', 'STAND', 'ROUTED at b393'),
    ('the `34` federation names the drive does not hold', 'STAND', 'FILED at b395, not repaired'),
    ('the self-reading / corpus-reading distinction', 'STAND', 'FILED at b396 as a limit'),
    ('the five deafnesses of b396`s sweep', 'STAND', 'FILED at b396'),
    ('the judgement half of the preservation rule', 'STAND', 'FILED at b396: a FLOOR, not a guard'),
    ('the keystones` stale `HELD` prose', 'STAND', 'ROUTED at b397, OPEN'),
    ('the disclosure rule`s own worked instance is stale', 'STAND', 'ROUTED at b397, OPEN'),
    ('`derivative-engine` carries no printed axiom profile', 'STAND', 'ROUTED at b397, OPEN'),
    ('the keystone rows asserting profiles for an unbuilt ref', 'STAND', 'ROUTED at b397, OPEN'),
    ('the two deposited records` remediation', 'STAND',
     'DRAFTED at b395, TRIGGERED at b397 (before any wave, and the author performs it)'),
    ('`ENUMERA` names no terminal at all', 'STAND', 'TRIGGERED at b397: it needs an author'),
    ('the ten now-reachable keystones', 'STAND',
     'PRICED at b396 at `28.0` minutes, TRIGGERED at b397'),
    ('the `82` at-risk figures', 'STAND', 'TRIGGERED at b397, and PARKED by `(R22)`'),
    ('the two anchorless clusters` first syntheses', 'STAND', 'TRIGGERED at b397, not owed'),
    ('the keystone with no correspondence table', 'STAND', 'TRIGGERED at b397: writing one is '
     'authoring'),

    # ---- WHAT THIS ACT CLOSES ---------------------------------------------------------------------
    ('the work orders whose trigger read `none`', 'CLOSE',
     '### **CLOSED BY `(R23)`, AND CLOSED BY BEING FILLED.** ### All `%d` rows of the '
     'work-order table read `none`; each now names ### **A TRIGGER THAT CAN FIRE**, and `0` '
     'needed SHELVING. ### **AN ITEM WITH NO TRIGGER IS NOT QUEUED, IT IS SHELVED** -- and none '
     'of the three is shelved now' % TRG['none_rows']),

    # ---- WHAT THIS ACT ADDS ---------------------------------------------------------------------
    ('the missing identity `(M)`, the owed bridge`s first half', 'STAND',
     '### **NEW at `b398`, AND IT IS THIS ACT`S PRODUCT.** ### For every `g` in the source`s '
     'class, ### **`-Tr(theta(g) S theta(g)*) = SUM_p W_p(g conv g-bar^#)`** ### in the '
     'source`s normalization. ### **TYPED A RESULT** -- not a read (no file states it), not a '
     'ruling (it is an identity), not a construction (both sides exist at grades). ### The '
     'ledger`s owed row is ### **SHARPENED AND STILL OWED.** ### **OPEN**'),
    ('the family obstruction, which `(M)` does not touch', 'STAND',
     '### **NEW at `b398`.** ### The Sonin margin is ### **NOT DEFINED ON THE LI FAMILY** '
     '(`b327`: `G_n`s inverse Mellin transform has no compact support, outside Theorem 1`s '
     'class). ### **EVEN WITH `(M)` THE TWO SIDES ARE ONE FUNCTIONAL ON TWO DISJOINT '
     'FAMILIES**, and ### **NO NORMALIZATION FIXES A DOMAIN.** ### **OPEN**'),
    ('`(N)`, the smallest next statement toward the clause', 'STAND',
     '### **NEW at `b398`, NAMED AND NOT ATTEMPTED.** ### The compact part of `K3` holds ### '
     '**FOR EVERY CELL AND NOT AT SEVEN.** ### `6` dependencies HELD, `3` ABSENT. ### **`(N)` '
     'IS NOT `(M)`:** ### `(M)` moves the bridge, `(N)` moves the clause. ### **A KERNEL ACT '
     'CAN TAKE IT; THIS ACT IS NOT ONE.** ### **OPEN**'),
    ('the two pinned sources are not on this drive', 'STAND',
     '### **NEW at `b398`, AND IT WEAKENS EVERY SOURCE QUOTATION IN IT.** ### Neither '
     'Connes-Consani `2006.13771v1` nor Lagarias `math/0404394v4` is on this drive, so every '
     'source statement here is quoted ### **AS THE CORPUS QUOTES IT, AT THE IMPORT BAR** -- '
     'weaker than reading the source. ### **FILED, NOT REPAIRED**'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES ONE ITEM BY FILLING IT AND OPENS FOUR BY READING.**')
    rec('    ### `(R23)` closes the trigger-`none` item: all three work-order rows now name a')
    rec('    ### trigger that can fire, and ### **NONE NEEDED SHELVING.**')
    rec('    ### ### ### **AND THE FOUR THAT OPEN ARE THE ACT`S PRODUCT, NOT ITS RESIDUE:** ###')
    rec('    ### ### ### the missing identity `(M)`; the family obstruction it does not touch;')
    rec('    ### ### ### `(N)`, the smallest next statement; and the fact that neither pinned')
    rec('    ### ### ### source is on this drive.')
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
    rec('    ### ### **AND NOTHING IS PAID:** ### `%d` grades conferred, `%d` rows paid, and the'
        % (C3['grades'], C3['paid']))
    rec('    ### ### owed bridge still reads ### **OWED** ### after the act.')
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0, marks=marks, triggers=TRG['filled'])


SCOPE = (
    "**SCOPE: THE LI-WEIL BRIDGE, FROM BANKED RESULTS ONLY -- AND THE VERDICT IS UNDECIDABLE FROM "
    "THE RECORD.** RULING (R23) IS RECORDED: AN ITEM WITH NO TRIGGER IS NOT QUEUED, IT IS SHELVED; "
    "all 3 rows of the work-order table read `none` and each now names A TRIGGER THAT CAN FIRE, 0 "
    "SHELVED. **NO COMPUTATION WAS RUN, NO INSTRUMENT WAS RUN AND NO KERNEL WAS BUILT** -- the "
    "order's own condition, since an act that computes something new has CHANGED THE QUESTION; 27 "
    "reads, 27 ANCHORED. **THE PLACE-SETS DIFFER AND THAT IS THE FIRST THING PRINTED (F1 MET):** "
    "the Sonin margin's is {infinity}, and NOT BY OMISSION -- b197 read Theorem 2 of 2310.18423, "
    "*the semilocal Sonin space is ONE ARCHIMEDEAN COPY, finite places contribute no independent "
    "Sonin directions* -- while the Li margin's is {infinity} union {all finite places} plus a pole "
    "term at s = 0 that is not a place at all. **AND THE FIRST FORM OF THIS ACT'S OWN TEST GOT IT "
    "BACKWARDS:** it read b197's withdrawal of `Tr_infinity + SUM_p Tr_p` as covering the "
    "navigator's premise and called the reading REFUTED, and b197 forbids that reading in a "
    "sentence written for exactly this case -- *THAT WITHDRAWAL IS ABOUT THE SONIN TRACE SUMMAND, "
    "NOT ABOUT FILE E's TWO-TERM SPLIT ... AND IS RECORDED HERE SO THAT NOBODY LATER READS IT AS IF "
    "IT DID.* **THE SEAT READ IT AS IF IT DID, THE FILE CAUGHT IT, AND THE CORRECTION IS ON THE "
    "FACE.** **BOTH HALVES OF THE READING ARE BANKED:** half one is the clause statement's own K3 "
    "-- *the source's construction on the object returns the test function at the identity times a "
    "dimension and no arithmetic* (b310), at KERNEL TERMINALS B329.* (24, zero-axiom) and B310.*, "
    "decomposition and scaling GENERAL and the compact part PER CELL; half two is K4 VERBATIM -- "
    "*the corpus's prime side IS the source's finite-places sum, factor for factor* -- DIFFERENT "
    "ONLY IN THE CUTOFF WINDOW (b306), an exception CARRIED and not dropped, and corroborated by "
    "b327's derived `lambda_Z(n) = -S_f(n)`. **SO THE LEDGER'S OWED ROW IS NARROWER THAN IT "
    "LOOKS.** The conclusion unfolds to one identity: the Sonin margin is `W_inf(f) - Tr(theta(g) S "
    "theta(g)*)`, the Weil functional is `W_inf(f) + SUM_p W_p(f)`, and **THEY AGREE IF AND ONLY IF "
    "`-Tr(theta(g) S theta(g)*) = SUM_p W_p(f)`** -- which is exactly what the ledger types as "
    "OWED. **VERDICT: UNDECIDABLE FROM THE RECORD.** Not ASSEMBLES: the identity is not in the "
    "record. Not DIFFERENT: no constituent of the reading is refuted, and *differ at their second "
    "term* says the identification is NOT HELD, not that it is FALSE. **THE READING RESTS ON THE "
    "OWED BRIDGE ITSELF.** **THE MISSING STATEMENT (M) IS NAMED AND TYPED A RESULT** -- not a read "
    "(no file states it), not a ruling (it is an identity), not a construction (both sides exist at "
    "grades). **A SECOND OBSTRUCTION IS INDEPENDENT OF IT AND SURVIVES IT:** the Sonin margin is "
    "NOT DEFINED ON THE LI FAMILY (b327), so even with (M) the two sides are ONE FUNCTIONAL ON TWO "
    "DISJOINT FAMILIES, and NO NORMALIZATION FIXES A DOMAIN. **(F2)'s VERDICT IS MET AND ITS REASON "
    "IS NOT:** the missing statement is an IDENTITY BETWEEN TWO SECOND TERMS AT ONE PLACE-SET, "
    "prior to any question about families. NEITHER ORDER BRANCH OF COMPONENT 3 FIRES and the act "
    "says so; the owed row is SHARPENED AND STILL OWED, 0 GRADES CONFERRED, 0 ROWS PAID, 0 CONTENT "
    "LOST, the pre-edit row preserved VERBATIM, and **THE DEPOSIT'S REFUSAL IS QUOTED BESIDE IT: A "
    "DECOMPOSITION OF ONE FUNCTIONAL IS NOT AN EQUIVALENCE OF THE FACES AND DOES NOT COMPILE ONE.** "
    "**COMPONENT 4 NAMES (N)** -- the compact part of K3 for EVERY cell and not at seven -- with 6 "
    "dependencies HELD and 3 ABSENT, **NOT ATTEMPTED**, and **(N) IS NOT (M)**: (M) moves the "
    "bridge, (N) moves the clause. And b332's E0 ranking is reported STALE in one row -- it calls "
    "K5 the softest at DEFINED-ONLY and b333 conferred DERIVES-ON-IMPORTS the next day -- ROUTED, "
    "NOT REPAIRED. NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR "
    "AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, "
    "NEITHER MAP TOUCHED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO KEYSTONE EDITED, NO PRIOR ACT'S "
    "FACE BANK OR INSTRUMENT EDITED, NO FACE ROW OF THE LEDGER EDITED. NOTHING DEPOSITS; **THE "
    "PLATFORM WAS NOT CALLED AT ALL**; 0 BRANCHES TOUCHED, 0 CLONES, 0 BUILDS, NO .lean FILE "
    "TOUCHED. NEITHER PINNED SOURCE IS ON THIS DRIVE, so every source statement is quoted AS THE "
    "CORPUS QUOTES IT AT THE IMPORT BAR, which is weaker than reading the source and is said. **THE "
    "FOUR OPEN LISTS ARE RESTATED OPEN BY NAME WITH THEIR TRIGGERS.** NO NEW TRACKING DOCUMENT WAS "
    "CREATED. NO ARCHIVE OR outputs FILE TOUCHED, THE MIRROR ROSTER NOT EDITED, NO "
    ".git/hooks/pre-push DELETED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. "
    "**THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED** and THE PARTITION STAYS UNDECIDED. NO "
    "AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt "
    "item 1 restated, still unpaid. The patent lane carried on the patent seat's report, "
    "UNCONFIRMED on this seat's record. THE INSTRUMENT LANE AND THE INSTRUMENT-AUDIT LANE STAY "
    "PARKED. THE WAVE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the "
    "deposit left it and this act makes no claim about it in either direction.")


def trail_block(Q):
    return [
        '', MARK, '',
        '### **b398 — THE LI–WEIL BRIDGE, ASSEMBLED OR SHOWN ABSENT (2026-09-10)**',
        '',
        ('*No block above is edited. The b397 block (`%s`) and every block before it stand exactly '
         'as they were written.*' % PRIOR),
        '',
        ('**RULING (R23), THE AUTHOR\u2019S, RATIFIED BY THE FERRY AND STRIKEABLE: AN ITEM WITH NO '
         'TRIGGER IS NOT QUEUED, IT IS SHELVED.** All **`%d`** rows of the work-order table above '
         'read `none`; each now names **a trigger that can fire**, and **`%d` needed shelving**. '
         'Two of the three cannot fire *yet*, because the instrument lane is PARKED under (R4) — '
         'and **a block on the work is not an absence of a trigger**, which is the distinction the '
         'ruling draws. `W-ORD-LI-WEIL-BRIDGE`\u2019s trigger is **THE AUTHOR\u2019S WORD**, the '
         'ferry is that word, and **it fired in this act.**'
         % (TRG['none_rows'], TRG['shelved'])),
        '',
        ('**THE VERDICT: UNDECIDABLE FROM THE RECORD — AND BOTH HALVES OF THE READING ARE '
         'BANKED.** The place-sets differ and that is the first thing measured: the Sonin '
         'margin\u2019s is **{∞}**, and *not by omission* — b197 read Theorem 2 of 2310.18423, '
         '*the semilocal Sonin space is ONE ARCHIMEDEAN COPY, finite places contribute no '
         'independent Sonin directions* — while the Li margin\u2019s is **{∞} ∪ {all finite '
         'places}** plus a pole term at `s = 0` that is not a place at all. Half one of the '
         'reading is the clause statement\u2019s own **K3**: *the source\u2019s construction on '
         'the object returns the test function at the identity times a dimension and no '
         'arithmetic* (b310), at **kernel terminals `B329.*` (24, zero-axiom) and `B310.*`**. Half '
         'two is **K4 verbatim**: *the corpus\u2019s prime side IS the source\u2019s '
         'finite-places sum, factor for factor* — **different only in the cutoff window** (b306), '
         'an exception carried and not dropped. **So the ledger\u2019s owed row is narrower than '
         'it looked.**'),
        '',
        ('**AND THIS ACT\u2019S OWN FIRST TEST GOT IT BACKWARDS, WHICH IS ON THE FACE AND HERE.** '
         'It read b197\u2019s withdrawal of the shape `Tr_∞ + Σ_p Tr_p` as covering the premise '
         'and called the reading **REFUTED**. b197 forbids that reading in a sentence written for '
         'exactly this case: *THAT WITHDRAWAL IS ABOUT THE SONIN TRACE SUMMAND, NOT ABOUT FILE '
         'E\u2019s TWO-TERM SPLIT … AND IS RECORDED HERE SO THAT NOBODY LATER READS IT AS IF IT '
         'DID.* **The seat read it as if it did, and the file caught it.** *A withdrawal that '
         'names its own scope is not a withdrawal of everything nearby.*'),
        '',
        ('**WHAT THE CONCLUSION NEEDS, NAMED AND TYPED.** The Sonin margin is '
         '`W_∞(f) − Tr(θ(g) S θ(g)*)`; the Weil functional is `W_∞(f) + Σ_p W_p(f)`; **they agree '
         'if and only if `−Tr(θ(g) S θ(g)*) = Σ_p W_p(f)`** — which is exactly what the ledger '
         'types as OWED. **(M):** *for every `g` in the source\u2019s class, '
         '`−Tr(θ(g) S θ(g)*) = Σ_p W_p(g ⋆ ḡ♯)` in the source\u2019s normalization.* **Typed a '
         'RESULT**: not a read (no file states it), not a ruling (it is an identity), not a '
         'construction (both sides exist at grades). **A second obstruction is independent of it '
         'and survives it:** the Sonin margin **is not defined on the Li family** (b327 — `G_n`'
         '\u2019s inverse Mellin transform has no compact support, outside Theorem 1\u2019s '
         'class), so even with (M) the two sides are **one functional on two disjoint families**, '
         'and **no normalization fixes a domain.**'),
        '',
        ('**WHAT THIS OBLIGES, AT EXACTLY ITS SCOPE.** Neither of the order\u2019s two branches '
         'fires and the act says so. The owed pair row is **sharpened and still OWED**: `+%d/−%d`, '
         '**`%d` content lost**, the pre-edit row preserved verbatim, **`%d` grades conferred and '
         '`%d` rows paid**. And the deposit\u2019s refusal stands beside it: **a decomposition of '
         'one functional is NOT an equivalence of the faces and does not compile one.** **The '
         'clause has not moved. No coordinate is closed.**'
         % (C3['added'], C3['deleted'], C3['lost'], C3['grades'], C3['paid'])),
        '',
        ('**THE SMALLEST NEXT STATEMENT, NAMED AND NOT ATTEMPTED. (N):** *in the compiled '
         'finite-side module `Core/FiniteSideSeal.lean`, the **compact part** of the finite-place '
         'contribution holds for **every** cell and not at seven — for every lawful `g`, the '
         'identity-count form of `Σ_p W_p(g ⋆ ḡ♯)` equals the test function at the identity times '
         'the dimension, with no cell-by-cell case analysis.* **`%d` dependencies HELD** (K3\u2019s '
         'decomposition and scaling parts PROVED-GENERAL at b329; K3\u2019s identification '
         'DERIVED-ON-CONTENT at b310 and *not compiled*; K4 DERIVED-ON-CONTENT at b306; K1 and K2 '
         'IMPORT-UNDER-THE-BAR) and **`%d` ABSENT** (the general compact part; a compilation of '
         'b310\u2019s identification; and K8 the quantifiers, about which nothing is proved). '
         '**(N) IS NOT (M):** (M) moves the *bridge*, (N) moves the *clause*. **A kernel act can '
         'take (N) as a work order; this act is not one.** And b332\u2019s E0 ranking is reported '
         '**stale in one row** — it calls **K5** the softest at `DEFINED-ONLY` and b333 conferred '
         '`DERIVES-ON-IMPORTS` on it the next day, and nothing propagated the lift into the table. '
         '**Routed, not repaired.** **The four lists stay OPEN by name with their triggers.** '
         '**Nothing deposits and the platform was not called at all.**'
         % (C4['held'], C4['absent'])),
        '',
    ]


def corr_rows(Q):
    m = ("**THE LI-WEIL BRIDGE IS UNDECIDABLE FROM THE RECORD: BOTH HALVES OF THE READING ARE "
         "BANKED, THE ONE MISSING IDENTITY IS NAMED AND TYPED A RESULT, AND A SECOND OBSTRUCTION "
         "SURVIVES IT** (b398, the li-weil bridge)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b398, %d gates read and %d checked "
            "by digest. RULING (R23) IS RECORDED: AN ITEM WITH NO TRIGGER IS NOT QUEUED, IT IS "
            "SHELVED; all %d work-order rows read `none` and each now names A TRIGGER THAT CAN "
            "FIRE, %d SHELVED. NO COMPUTATION, NO INSTRUMENT RUN, NO KERNEL BUILT -- the order's "
            "own condition -- and %d reads, %d ANCHORED. THE PLACE-SETS DIFFER AND THAT IS PRINTED "
            "FIRST (F1 MET): the Sonin margin's is {infinity} AND NOT BY OMISSION (b197 on Theorem "
            "2 of 2310.18423: the semilocal Sonin space is ONE ARCHIMEDEAN COPY, finite places "
            "contribute no independent Sonin directions), the Li margin's is {infinity} union {all "
            "finite places} plus a pole term that is not a place. **BOTH HALVES OF THE READING ARE "
            "BANKED**: half one is the clause statement's K3 at kernel terminals B329.* (24, "
            "zero-axiom) and B310.*, half two is K4 VERBATIM -- the corpus's prime side IS the "
            "source's finite-places sum, factor for factor -- DIFFERENT ONLY IN THE CUTOFF WINDOW "
            "(b306), carried. **AND THIS ACT'S OWN FIRST TEST GOT IT BACKWARDS**: it read b197's "
            "withdrawal as covering the premise and called the reading REFUTED, and b197 forbids "
            "that reading in a sentence written for exactly this case; THE SEAT READ IT AS IF IT "
            "DID AND THE FILE CAUGHT IT. The conclusion needs one identity -- "
            "`-Tr(theta(g) S theta(g)*) = SUM_p W_p(f)` -- which is what the ledger types as OWED, "
            "so **VERDICT UNDECIDABLE FROM THE RECORD**: not ASSEMBLES (the identity is absent), "
            "not DIFFERENT (nothing is refuted, and `differ at their second term` says NOT HELD "
            "rather than FALSE). **(M) IS NAMED AND TYPED A RESULT.** A SECOND OBSTRUCTION IS "
            "INDEPENDENT AND SURVIVES IT: the Sonin margin IS NOT DEFINED ON THE LI FAMILY, so "
            "even with (M) the two sides are ONE FUNCTIONAL ON TWO DISJOINT FAMILIES. THE OWED ROW "
            "IS SHARPENED AND STILL OWED: +%d/-%d, %d CONTENT LOST, %d GRADES CONFERRED, %d ROWS "
            "PAID. **(N) IS NAMED AND NOT ATTEMPTED** -- the compact part of K3 for every cell and "
            "not at seven, %d dependencies HELD and %d ABSENT -- and (N) IS NOT (M). b332's E0 "
            "ranking is reported STALE in one row (K5, lifted at b333), ROUTED NOT REPAIRED"
            % (LG['gates_read'], LG['face_subject_gates'], TRG['none_rows'], TRG['shelved'],
               E['anchored'], E['anchored'], C3['added'], C3['deleted'], C3['lost'],
               C3['grades'], C3['paid'], C4['held'], C4['absent']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN, AND NONE IS OPENED. ### The two "
            "margins were unfolded from the files that emitted them; NO COMPUTATION WAS RUN, NO "
            "INSTRUMENT RUN, NO KERNEL BUILT, NO BRANCH TOUCHED AND NO .lean FILE TOUCHED. ### "
            "NEITHER PINNED SOURCE IS ON THIS DRIVE, so every source statement is quoted AS THE "
            "CORPUS QUOTES IT AT THE IMPORT BAR -- weaker than reading the source, and said. ### "
            "READING TWO MARGINS IS NOT BRIDGING THEM")
    prof = ("### NO AXIOM PROFILE IS ASSERTED OR RECOMPUTED. ### NOTHING WAS COMPUTED ABOUT THE "
            "OBJECT. ### NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE "
            "STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE "
            "CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO KEYSTONE EDITED, NO FACE "
            "ROW OF THE LEDGER EDITED. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL")
    grade = ("### THE PLACE-SETS ARE STATED BEFORE ANY COMPARISON AND THE SONIN ONE CARRIES THE "
             "THEOREM THAT MAKES IT ARCHIMEDEAN-ONLY. ### BOTH HALVES OF THE READING ARE TESTED "
             "AND BOTH ARE CREDITED AS BANKED, EACH WITH ITS OWNER AND ITS TERMINALS. ### THE "
             "SEAT'S OWN CORRECTED MISREADING IS PRINTED WITH THE FILE THAT CAUGHT IT. ### THE "
             "VERDICT IS ONE OF THE ORDER'S THREE, UNSOFTENED, AND THE MISSING STATEMENT IS NAMED "
             "AND ITS TYPE ARGUED. ### THE SWEEP IS BOUNDED BY THE TABLE THAT HAS THE COLUMN, AND "
             "THE DISCARDED 51-ROW SHAPE IS NAMED WITH ITS YIELD. ### A SHARPENING IS NOT A "
             "PAYMENT AND THE ROW IS STILL OWED")
    status = ("data/b398_the_li_weil_bridge.txt; data/%s; data/%s; "
              "data/b398_registration_2026-09-10.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b398); tools/b398_extract.py; tools/b398_regspec.py; "
              "tools/b398_reg_gate.py; tools/b398_components.py; tools/b398_desk_bank.py; "
              "tools/b398_checks.py; PLACE-papers FACES_LEDGER.md (the OWED pair row sharpened, "
              "with the pre-edit row preserved) and OPEN_TRAILS.md (three trigger cells and an "
              "append-only block); CORRESPONDENCE.md row %%d" % (AC['run_file'], E['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('does the li-weil bridge assemble', 'what is the missing identity',
           'is the sonin margin defined on the li family',
           'what are the two margins place-sets',
           'what is the smallest next statement toward the clause',
           'why is the bridge still owed')
MUST_NOT_HIT = ('the bridge was paid', 'a grade was conferred', 'something was computed',
                'the platform was called')


def do_key(rownum):
    KEY = 'the-li-weil-bridge'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b398 TESTED THE DECOMPOSITION READING OF THE LI-WEIL BRIDGE FROM BANKED RESULTS ONLY AND "
        "THE VERDICT IS **UNDECIDABLE FROM THE RECORD**. THE PLACE-SETS DIFFER AND THAT IS THE "
        "FIRST THING MEASURED: the Sonin margin's is {infinity} AND NOT BY OMISSION -- b197 read "
        "Theorem 2 of 2310.18423, THE SEMILOCAL SONIN SPACE IS ONE ARCHIMEDEAN COPY AND FINITE "
        "PLACES CONTRIBUTE NO INDEPENDENT SONIN DIRECTIONS -- while the Li margin's is {infinity} "
        "UNION {ALL FINITE PLACES} plus a pole term at s = 0 that is not a place at all. **BOTH "
        "HALVES OF THE NAVIGATOR'S READING ARE BANKED**: half one is the clause statement's own K3 "
        "-- the source's construction on the object returns the test function at the identity times "
        "a dimension and no arithmetic (b310) -- at KERNEL TERMINALS B329.* (24, zero-axiom) and "
        "B310.*; half two is K4 VERBATIM -- the corpus's prime side IS the source's finite-places "
        "sum, FACTOR FOR FACTOR -- DIFFERENT ONLY IN THE CUTOFF WINDOW (b306), an exception CARRIED "
        "AND NOT DROPPED, corroborated by b327's derived lambda_Z(n) = -S_f(n). SO THE LEDGER'S "
        "OWED ROW IS NARROWER THAN IT LOOKED. **AND THIS ACT'S OWN FIRST TEST GOT IT BACKWARDS**: "
        "it read b197's withdrawal of Tr_infinity + SUM_p Tr_p as covering the premise and called "
        "the reading REFUTED, and b197 forbids that reading in a sentence written for exactly this "
        "case -- THE SEAT READ IT AS IF IT DID AND THE FILE CAUGHT IT. THE CONCLUSION NEEDS EXACTLY "
        "ONE IDENTITY: **(M) for every g in the source's class, -Tr(theta(g) S theta(g)*) = SUM_p "
        "W_p(g conv g-bar^#) in the source's normalization**, TYPED A RESULT -- not a read (no file "
        "states it), not a ruling (it is an identity), not a construction (both sides exist at "
        "grades). A SECOND OBSTRUCTION IS INDEPENDENT AND SURVIVES IT: THE SONIN MARGIN IS NOT "
        "DEFINED ON THE LI FAMILY (b327: G_n's inverse Mellin transform has no compact support, "
        "outside Theorem 1's class), so even with (M) the two sides are ONE FUNCTIONAL ON TWO "
        "DISJOINT FAMILIES, AND NO NORMALIZATION FIXES A DOMAIN. THE OWED ROW IS SHARPENED AND "
        "STILL OWED, WITH %d GRADES CONFERRED AND %d ROWS PAID. **(N) IS NAMED AND NOT ATTEMPTED** "
        "-- the compact part of K3 holds FOR EVERY CELL AND NOT AT SEVEN -- with %d dependencies "
        "HELD and %d ABSENT, and **(N) IS NOT (M)**: (M) moves the bridge, (N) moves the clause. "
        "RULING (R23) IS RECORDED and all %d work-order rows now name a trigger that can fire."
        % (C3['grades'], C3['paid'], C4['held'], C4['absent'], TRG['filled']))
    grade = (
        "### NOTHING WAS COMPUTED, NO INSTRUMENT WAS RUN AND NO KERNEL WAS BUILT -- the order's own "
        "condition, since an act that computes something new has CHANGED THE QUESTION. ### NO "
        "GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO "
        "CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER "
        "RESHAPED, NO LIST CLOSED, NO KEYSTONE EDITED, NO FACE ROW OF THE LEDGER EDITED. ### THE "
        "ONLY CORPUS WRITES ARE THE OWED PAIR ROW'S LAST CELL AND THREE TRIGGER CELLS, BOTH "
        "ADDITIVE, WITH THE PRE-EDIT LINES PRESERVED VERBATIM AND 0 CONTENT LOST. ### NEITHER "
        "PINNED SOURCE IS ON THIS DRIVE AND EVERY SOURCE STATEMENT IS QUOTED AS THE CORPUS QUOTES "
        "IT. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT "
        "MOVED AND NO COORDINATE IS CLOSED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### "
        "M-2 UNCHANGED")
    where = (
        "data/b398_the_li_weil_bridge.txt; data/%s; data/%s; "
        "data/b398_registration_2026-09-10.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b398 -- %d gates read, %d checked by digest); "
        "tools/b398_extract.py; tools/b398_regspec.py; tools/b398_reg_gate.py; "
        "tools/b398_components.py; tools/b398_desk_bank.py; tools/b398_checks.py; "
        "PLACE-papers FACES_LEDGER.md and OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ('b398 (the li-weil bridge is undecidable from the record: both halves of the reading '
           'are banked, the one missing identity is named and typed a result, and a second '
           'obstruction survives it)')
    row_new = ('    # ### THE LI-WEIL BRIDGE (b398).%s'
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
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-52s reaches the b398 key : %s' % (qq, g2))
    for lbl, cond in (('the verdict is undecidable from the record',
                       'UNDECIDABLE FROM THE RECORD' in out),
                      ('the place-sets differ and are printed first',
                       'THE PLACE-SETS DIFFER' in out),
                      ('the sonin place-set is not an omission',
                       'AND NOT BY OMISSION' in out),
                      ('both halves are banked',
                       "BOTH HALVES OF THE NAVIGATOR'S READING ARE BANKED" in out),
                      ('K4 is quoted factor for factor', 'FACTOR FOR FACTOR' in out),
                      ('the cutoff exception is carried',
                       'CARRIED AND NOT DROPPED' in out),
                      ('the seat`s own misreading is on the record',
                       'THE SEAT READ IT AS IF IT DID' in out),
                      ('(M) is named and typed a result', 'TYPED A RESULT' in out),
                      ('the family obstruction survives (M)',
                       'NOT DEFINED ON THE LI FAMILY' in out),
                      ('no normalization fixes a domain',
                       'NO NORMALIZATION FIXES A DOMAIN' in out),
                      ('the row is sharpened and still owed',
                       'SHARPENED AND STILL OWED' in out),
                      ('(N) is named, not attempted, and is not (M)',
                       'IS NOT (M)' in out),
                      ('nothing was computed', 'NOTHING WAS COMPUTED' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-44s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def main():
    bar('=')
    rec('b398 -- THE DESK, THE LEDGER WRITES, AND THE BANK.')
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
    low = seg.lower()
    tr['says_r23'] = 'an item with no trigger is not queued' in low
    tr['says_block_not_absence'] = 'a block on the work is not an absence of a trigger' in low
    tr['says_verdict'] = 'undecidable from the record' in low
    tr['says_placesets'] = 'not by omission' in low
    tr['says_both_banked'] = 'both halves of the reading are\nbanked' in low \
        or 'both halves of the reading are banked' in low
    tr['says_cutoff'] = 'different only in the cutoff window' in low
    tr['says_self_correction'] = 'the seat read it as if it did' in low
    tr['says_missing_typed'] = 'typed a\nresult' in low or 'typed a result' in low
    tr['says_family'] = 'is not defined on the li family' in low
    tr['says_no_normalization'] = 'no normalization fixes a domain' in low
    tr['says_still_owed'] = 'sharpened and still owed' in low
    tr['says_not_m'] = '(n) is not (m)' in low
    tr['says_stale_k5'] = 'stale in one row' in low
    tr['says_lists_open'] = 'lists stay open by name' in low
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
        run_clock.write(D, 'b398_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b398_desk_notes', LINES)
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
            run_clock.write(D, 'b398_desk_notes', LINES)
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
    B.append('b398 -- THE LI-WEIL BRIDGE, ASSEMBLED OR SHOWN ABSENT. ### THE BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **UNDECIDABLE FROM THE RECORD. ### BOTH HALVES OF THE READING ARE')
    B.append('### ### ### BANKED, THE ONE MISSING IDENTITY IS NAMED, AND A SECOND OBSTRUCTION')
    B.append('### ### ### SURVIVES IT.**')
    B.append('')
    B.append(SUB)
    B.append('### RULING `(R23)`, RECORDED AND APPLIED.')
    B.append(SUB)
    B.append('### ### **AN ITEM WITH NO TRIGGER IS NOT QUEUED, IT IS SHELVED.**')
    B.append('### **THE POPULATION IS THE TABLE THAT HAS THE COLUMN**, found by its own header at')
    B.append('### line `%s`. ### `FACES_LEDGER.md` has ### **NO TRIGGER COLUMN AT ALL.**'
             % TRG['header'])
    B.append('### ### **ROWS WHOSE TRIGGER READ `none` : `%d`. ### ROWS NOW CARRYING ONE : `%d`.'
             % (TRG['none_rows'], TRG['filled']))
    B.append('### ### ROWS SHELVED : `%d`.**' % TRG['shelved'])
    B.append('### ### **TWO OF THE THREE CANNOT FIRE YET, BECAUSE THE INSTRUMENT LANE IS PARKED')
    B.append('### ### UNDER `(R4)` -- AND A BLOCK ON THE WORK IS NOT AN ABSENCE OF A TRIGGER**,')
    B.append('### ### which is the distinction the ruling draws.')
    B.append('### ### **AN EARLIER FORM OF THE SWEEP KEPT `51` ROWS.** ### **A SWEEP THAT KEEPS')
    B.append('### ### FIFTY-ONE IS NOT A SWEEP**, and it was bounded before the lock.')
    B.append('### **THE WRITE : `+%d / -%d` ; ### CONTENT LOST `%d`.**'
             % (TRG['added'], TRG['deleted'], TRG['lost']))
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 1 -- THE PLACE-SETS, FIRST.')
    B.append(SUB)
    B.append('### **THE SONIN MARGIN : `%s`** ### -- and ### **NOT BY OMISSION.** ### `b197` read'
             % C1['place_sonin'])
    B.append('### Theorem 2 of `2310.18423`: ### *the semilocal Sonin space is ONE ARCHIMEDEAN')
    B.append('### COPY, finite places contribute no independent Sonin directions.*')
    B.append('### **THE LI MARGIN : `%s`.**' % C1['place_li'])
    B.append('### ### **`(F1)` IS MET, AND IT IS THE FIRST THING PRINTED.**')
    B.append('### ### **AND THE DIFFERENCE IS NOT A DEFECT IN EITHER OBJECT** -- it is the reason')
    B.append('### ### the reading must ADD finite terms before the two can be compared, which is')
    B.append('### ### the reading`s own construction.')
    B.append('### **THE SONIN MARGIN`S CONSTITUENTS QUOTED : `%d`. ### THE LI MARGIN`S : `%d`.**'
             % (C1['sonin_constituents'], C1['li_constituents']))
    B.append('### ### **AND THE PROGRAMME`S OWN CAUTION IS CARRIED:** ### the')
    B.append('### ### `lambda_A`/`lambda_Z` split is ### **NOT A PLACE-SPLIT**, so `lambda_Z` is')
    B.append('### ### taken as `-S_f` because `b327` ### **DERIVED** ### it, not by definition.')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 2 -- THE READING, TESTED IN TWO HALVES.')
    B.append(SUB)
    B.append('### ### **AND THE FIRST FORM OF THIS TEST GOT IT BACKWARDS.** ### It read `b197``s')
    B.append('### ### withdrawal of `Tr_infinity + SUM_p Tr_p` as covering the premise and called')
    B.append('### ### the reading ### **REFUTED.** ### `b197` forbids that reading in a sentence')
    B.append('### ### written for exactly this case -- ### *THAT WITHDRAWAL IS ABOUT THE SONIN')
    B.append('### ### TRACE SUMMAND, NOT ABOUT FILE E`s TWO-TERM SPLIT ... AND IS RECORDED HERE SO')
    B.append('### ### THAT NOBODY LATER READS IT AS IF IT DID.*')
    B.append('### ### ### **THE SEAT READ IT AS IF IT DID, AND THE FILE CAUGHT IT.** ### The')
    B.append('### ### ### correction was made before the lock and stands on the face. ### **A')
    B.append('### ### ### WITHDRAWAL THAT NAMES ITS OWN SCOPE IS NOT A WITHDRAWAL OF EVERYTHING')
    B.append('### ### ### NEARBY.**')
    B.append('')
    B.append('### **HALF ONE : %s.**' % C2['half_one'])
    B.append('### The clause statement`s own `K3` -- ### *the source`s construction on the object')
    B.append('### returns the test function at the identity times a dimension and no arithmetic*')
    B.append('### (`b310`) -- at ### **KERNEL TERMINALS `B329.*` (24, ZERO-AXIOM) AND `B310.*`**,')
    B.append('### with the decomposition and scaling parts ### **GENERAL** ### and the compact')
    B.append('### part ### **PER CELL.**')
    B.append('### **HALF TWO : %s, VERBATIM.**' % C2['half_two'])
    B.append('### `K4` -- ### *the corpus`s prime side IS the source`s finite-places sum, factor')
    B.append('### for factor on the summand under the source`s own normalization* -- ###')
    B.append('### **DIFFERENT ONLY IN THE CUTOFF WINDOW (`b306`)**, an exception ### **CARRIED')
    B.append('### AND NOT DROPPED**; corroborated by `b327`s derived `lambda_Z(n) = -S_f(n)`.')
    B.append('### ### ### **SO THE LEDGER`S OWED ROW IS NARROWER THAN IT LOOKED.**')
    B.append('')
    B.append('### **THE CONCLUSION, UNFOLDED TO THE IDENTITY IT REQUIRES:**')
    B.append('###   the Sonin margin      `W_inf(f) - Tr(theta(g) S theta(g)*)`')
    B.append('###   the Weil functional   `W_inf(f) + SUM_p W_p(f)`')
    B.append('### ### **THEY AGREE IF AND ONLY IF `-Tr(theta(g) S theta(g)*) = SUM_p W_p(f)`**,')
    B.append('### ### and that is exactly what the ledger types as ### **OWED.**')
    B.append('')
    B.append('### ### ### **THE VERDICT : %s.**' % C2['verdict'])
    B.append('### **NOT `ASSEMBLES`:** ### the identity is not in the record.')
    B.append('### **NOT `DIFFERENT`:** ### no constituent of the reading is refuted, and the')
    B.append('### ledger`s ### *differ at their second term* ### says the identification is ###')
    B.append('### **NOT HELD**, not that it is ### **FALSE.**')
    B.append('### ### **THE READING RESTS ON THE OWED BRIDGE ITSELF**, which is why no amount of')
    B.append('### ### re-reading closes it. ### **THAT IS THE RESULT.**')
    B.append('')
    B.append('### **THE MISSING STATEMENT, NAMED AND TYPED:**')
    B.append('###   ### **(M)** ### For every `g` in the source`s class -- `g` in')
    B.append('###   `C_c^inf(R*_+)` with `g~(0) = g~(1) = 0` -- ### **`-Tr(theta(g) S theta(g)*)')
    B.append('###   ### = SUM_p W_p(g conv g-bar^#)`** ### in the source`s own normalization.')
    B.append('###   ### **TYPE : %s.** ### Not a read (no file states it, and this act looked in'
             % C2['missing_type'])
    B.append('###   the ledger, the clause statement, `b306`, `b310`, `b320`, `b321`, `b324`,')
    B.append('###   `b327` and `b329`); not a ruling (it is an identity, not a choice); not a')
    B.append('###   construction (both sides exist at grades). ### **IT IS A DERIVATION ON')
    B.append('###   ### CONTENT, AND IT IS THE OWED BRIDGE`S FIRST HALF.**')
    B.append('')
    B.append('### **AND A SECOND OBSTRUCTION, INDEPENDENT OF THE FIRST AND SURVIVING IT:**')
    B.append('### ### **THE SONIN MARGIN IS NOT DEFINED ON THE LI FAMILY** ### -- `b327`: `G_n`')
    B.append('### is a rational function whose inverse Mellin transform has ### **NO COMPACT')
    B.append('### SUPPORT**, outside Theorem 1`s class `supp g` in `[2^-1/2, 2^1/2]`. ### So even')
    B.append('### with `(M)` the two sides are ### **ONE FUNCTIONAL ON TWO DISJOINT FAMILIES** --')
    B.append('### `b327`s banked ### *ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL* -- and')
    B.append('### ### **NO NORMALIZATION FIXES A DOMAIN.**')
    B.append('### ### **OBSTRUCTIONS : `%d`, AND `(M)` CLEARS ONE OF THEM.**' % C2['obstructions'])
    B.append('### ### **`(F2)`S VERDICT IS MET AND ITS REASON IS NOT:** ### the order expected a')
    B.append('### ### normalization never fixed across the two families; the missing statement is')
    B.append('### ### an ### **IDENTITY BETWEEN TWO SECOND TERMS AT ONE PLACE-SET**, prior to any')
    B.append('### ### question about families. ### **A PREDICTION MET FOR A DIFFERENT REASON IS')
    B.append('### ### REPORTED WITH THE REASON.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 3 -- WHAT THE OUTCOME OBLIGES.')
    B.append(SUB)
    B.append('### ### **NEITHER OF THE ORDER`S TWO BRANCHES FIRES, AND THE ACT DOES NOT BORROW')
    B.append('### ### THE NEARER ONE.**')
    B.append('### **THE OWED PAIR ROW, SHARPENED AT LINE `%d`:** ### `+%d / -%d` ; content lost'
             % (C3['row_line'], C3['added'], C3['deleted']))
    B.append('### ### **`%d`** ### ; the pre-edit cell a substring of the post-edit cell : `%s` ;'
             % (C3['lost'], C3['kept']))
    B.append('### the pre-edit row preserved verbatim : `%s`.' % C3['verbatim'])
    B.append('### ### **THE ROW IS STILL `OWED` AFTER THE ACT : `%s`. ### GRADES CONFERRED : `%d`.'
             % (C3['still_owed'], C3['grades']))
    B.append('### ### ROWS PAID : `%d`.**' % C3['paid'])
    B.append('### ### **A SHARPENING IS NOT A PAYMENT.**')
    B.append('### **AND THE DEPOSIT`S REFUSAL STANDS BESIDE IT:** ### **A DECOMPOSITION OF ONE')
    B.append('### ### FUNCTIONAL IS NOT AN EQUIVALENCE OF THE FACES AND DOES NOT COMPILE ONE.**')
    B.append('### ### **THE CLAUSE HAS NOT MOVED. ### NO COORDINATE IS CLOSED.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 4 -- THE SMALLEST NEXT STATEMENT.')
    B.append(SUB)
    B.append('### ### **(N)** ### In the compiled finite-side module `Core/FiniteSideSeal.lean`,')
    B.append('### the ### **COMPACT PART** ### of the finite-place contribution holds ### **FOR')
    B.append('### EVERY CELL AND NOT AT SEVEN**: for every `g` in the source`s class, the')
    B.append('### identity-count form of `SUM_p W_p(g conv g-bar^#)` equals the test function at')
    B.append('### the identity times the dimension, ### **WITH NO CELL-BY-CELL CASE ANALYSIS.**')
    B.append('### **DEPENDENCIES HELD : `%d`.** ### `K3`s decomposition and scaling parts'
             % C4['held'])
    B.append('### (`PROVED-GENERAL`, `b329`); `K3`s identification (`DERIVED-ON-CONTENT`, `b310`,')
    B.append('### and ### *not compiled*); `K4` (`DERIVED-ON-CONTENT`, `b306`); `K1` and `K2`')
    B.append('### (`IMPORT-UNDER-THE-BAR`).')
    B.append('### **ABSENT : `%d`.** ### the general compact part (the whole of `(N)`); a'
             % C4['absent'])
    B.append('### compilation of `b310`s identification; and ### **`K8` THE QUANTIFIERS**, about')
    B.append('### which nothing is proved.')
    B.append('### ### **`(N)` IS NOT `(M)`, AND THE ACT DOES NOT BLUR THEM : `%s`.** ### `(M)`'
             % C4['distinct_from_M'])
    B.append('### ### moves the ### **BRIDGE**; `(N)` moves the ### **CLAUSE.** ### That was this')
    B.append('### ### seat`s `(E3)`, registered before the lock.')
    B.append('### ### **AND `(N)` IS NOT ATTEMPTED : ATTEMPTED `%d`.**' % C4['attempted'])
    B.append('### ### **AND `b332`S E0 RANKING IS REPORTED STALE IN ONE ROW:** ### it calls `%s`'
             % C4['b332_stale_row'])
    B.append('### ### the softest at `DEFINED-ONLY`, and `b333` conferred `DERIVES-ON-IMPORTS` on')
    B.append('### ### it the next day. ### **A TABLE THAT WAS RIGHT WHEN WRITTEN IS DATED BY THE')
    B.append('### ### ACT THAT LIFTED ITS SOFTEST ROW.** ### **ROUTED, NOT REPAIRED** -- editing')
    B.append('### ### `FINDINGS.md`s fold is not this act`s scope.')
    B.append('')
    B.append(SUB)
    B.append('### THE DESK.')
    B.append(SUB)
    B.append('### ### **ITEMS SWEPT `%d` ; CLOSED `%d` ; STANDING `%d`.**'
             % (Q['items'], Q['closed'], Q['standing']))
    B.append('### ### **ONE ITEM IS CLOSED BY BEING FILLED** -- the trigger-`none` item, under')
    B.append('### ### `(R23)` -- and ### **FOUR OPEN, ALL FOUR THE ACT`S PRODUCT AND NOT ITS')
    B.append('### ### RESIDUE:** ### `(M)`; the family obstruction; `(N)`; and the fact that')
    B.append('### ### neither pinned source is on this drive.')
    B.append('### ### **THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME WITH THEIR TRIGGERS, AND')
    B.append('### ### THIS ACT CLOSES NONE OF THEM.**')
    B.append('')
    B.append(SUB)
    B.append('### WHAT THIS BANK WAS MADE FROM. ### **NAMED, SO A READER CAN RE-RUN IT.**')
    B.append(SUB)
    B.append('### ### **THE FACE, LOCKED BEFORE ANY WRITE:**')
    B.append('###   `data/b398_registration_2026-09-10.txt`')
    B.append('###   sha256 `%s`' % SEALHASH)
    B.append('###   locked at `%s` (UTC)' % SEALSTAMP)
    B.append('### ### **THE LOCK GATE:** ### `tools/b378_lockgate.py` run as `b398` -- ###')
    B.append('### **`%d` GATES READ, `%d` PASSING, `%d` CHECKED BY DIGEST.**'
             % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    B.append('### ### **THE READS : `%d`, ALL `%d` ANCHORED, `0` AMBIGUOUS, `0` ABSENT.**'
             % (E['anchored'], E['anchored']))
    B.append('### ### **THE RUN RECORDS, EACH RESOLVED BY ITS OWN RECORDED CLOCK** (`b358`):')
    B.append('###   the extract and its four surveys   `data/%s`  `%s`'
             % (E['run_file'], E['run_clock']))
    B.append('###   the components and the writes      `data/%s`  `%s`'
             % (AC['run_file'], AC['run_clock']))
    B.append('### ### **AND THE LEDGER WRITES:** ### `CORRESPONDENCE.md` row `%d`; the'
             % rownum)
    B.append('### ### `OPEN_TRAILS.md` block marked `%s`; the index key' % MARK)
    B.append('### ### `the-li-weil-bridge`.')
    B.append('')
    B.append(SCOPE)
    B.append('')
    B.append(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### SOMETHING WAS COMPUTED.', '### A HALF WAS REFUSED.',
                '### THE BRIDGE WAS PAID.', '### A GRADE WAS CONFERRED.',
                '### A MISREADING WAS BURIED.', '### A SWEEP KEPT FIFTY-ONE.',
                '### A FACE ROW WAS EDITED.', '### THE PLATFORM WAS CALLED.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))
    rec()
    bar('=')
    rec('  ### desk %d ; closed %d ; trail %s ; row %s ; key %s'
        % (Q['items'], Q['closed'], tr['appended_only'], rownum, kok))
    bar('=')
    p = run_clock.write(D, 'b398_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             bank='b398_the_li_weil_bridge.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b398_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
