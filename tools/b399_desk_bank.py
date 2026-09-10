# -*- coding: utf-8 -*-
"""b399_desk_bank.py -- THE DESK, THE LEDGER WRITES, AND THE BANK.

### ### **AND THIS FILE IS A DEFECT ON THIS ACT'S OWN LOCKED FACE, DECLARED HERE RATHER THAN
### ### HIDDEN.** ### The face's section (I) named FIVE new relay tool files and its spec sealed
### `new relay tool files : 5, cap 5`. ### **THIS IS THE SIXTH**, and the ritual has required a
### desk/bank writer in every act of this arc. ### The corpus's own cap, `G-CAP`, is `6` and holds;
### ### **THE CLAUSE THAT FAILS IS THIS SEAT'S OWN COUNT, THE LOCKED FACE IS NOT EDITED, AND BOTH
### ### NUMBERS ARE PRINTED IN THE BANK** -- `b389`'s rule for a figure a later instrument
### disproves, applied to a figure this act disproved by continuing to work.

### ### **WHAT IT WRITES:** ### the desk sweep under `(R7)`; the append-only trail block; the
### correspondence row; the banked-index key; and the bank. ### The four corpus edits were made by
### `b399_components.py` and are NOT remade here.
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
MARK = '<!-- b399 (M) tested by sign then refuted by value; the grade move routed -->'
PRIOR = '<!-- b398 the li-weil bridge: undecidable from the record, and (M) named -->'
BANKOUT = os.path.join(D, 'b399_the_sign_and_the_refutation.txt')

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


SEALTXT = io.open(os.path.join(D, 'b399_registration_2026-09-10.txt'),
                  encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)

LG = J('b399_lockgate')
X = J('b399_extract')
F = X['figures']
CRUN = io.open(os.path.join(D, 'b399_components_run.txt'), encoding='utf-8').read()
MEAS = json.loads(re.search(r'^  ### (\{.*\})$', CRUN, re.M).group(1))
READS = len(X['reads'])
ANCH = sum(1 for r in X['reads'] if r['verdict'] == 'ANCHORED')
SRCN = len(X['source'])
SRCOK = sum(1 for s in X['source'] if s['pages'])
LOST = sum(v['lost'] for v in MEAS.values() if isinstance(v, dict) and 'lost' in v)

# ### **THE TOOL FILES THIS ACT ACTUALLY WROTE, COUNTED HERE AND NOT ASSUMED.**
TOOLS = [n for n in sorted(os.listdir(os.path.join(ROOT, 'tools')))
         if n.startswith('b399_') and n.endswith('.py')]


def blob(rel):
    r = subprocess.run(['git', 'show', 'HEAD:' + rel], cwd=PP, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


DESK = [
    ('M-2, under b310 cap', 'STAND', 'the aggregation is still SPECIFIED-NOT-STATED'),
    ("the object's conditions", 'STAND', "the conditions are the object's and none discharged"),
    ('the uniformity row U1', 'STAND', "the row's own refusal stands"),
    ('the instrument lane, PARKED under ruling R4', 'STAND',
     'PARKED, and still load-bearing: two work orders cannot fire until it is unparked'),
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
    ('the download-layer book`s registry drift', 'STAND', 'OPEN AND THE AUTHOR`S'),
    ('the six subject clusters with no keystone', 'STAND', '`NOT-YET-SYNTHESIZED` since b385'),
    ('the ten untracked run records of earlier acts', 'STAND', 'NAMED at b382, STILL UNTRACKED'),
    ('the legacy `.git/hooks/pre-push` copies', 'STAND', '### **RULED BY `(R16)`: THEY STAY**'),
    ('the untracked `.b304-backup` artifacts', 'STAND', 'NAMED at b386, still untracked'),
    ('the 23 unreadable correspondence rows', 'STAND', 'NAMED at b388 by cause, and ROUTED'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the deposited layer, unread since b389', 'STAND',
     'STILL BLOCKED; this act did not ask the platform'),
    ('the eight-versus-six cluster-synthesis disagreement', 'STAND', 'ROUTED at b389'),
    ('the `66` superseded version citations', 'STAND', 'REPORTED at b391 and LEFT'),
    ('placement into `Tier KC`', 'STAND', 'PRICED at b393 and STILL EMPTY'),
    ('the `34` federation names the drive does not hold', 'STAND', 'FILED at b395, not repaired'),
    ('the five deafnesses of b396`s sweep', 'STAND', 'FILED at b396'),
    ('the keystones` stale `HELD` prose', 'STAND', 'ROUTED at b397, OPEN'),
    ('the two deposited records` remediation', 'STAND', 'DRAFTED at b395, TRIGGERED at b397'),
    ('the `82` at-risk figures', 'STAND', 'TRIGGERED at b397, and PARKED by `(R22)`'),
    ('the family obstruction, which `(M)` never touched', 'STAND',
     '### **UNCHANGED BY THIS ACT AND UNCHANGED BY `(M)`S FALSITY.** ### `b327`: `G_n`s inverse '
     'Mellin transform has no compact support, so the Li family lies outside Theorem 1`s class. '
     '### **ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL. ### OPEN**'),
    ('`(N)`, the smallest next statement toward the clause', 'STAND',
     'NAMED at b398, NOT ATTEMPTED there and NOT ATTEMPTED here. ### **`(N)` IS NOT `(M)`, AND '
     '`(M)`S REFUTATION DOES NOT TOUCH IT.** ### OPEN'),

    # ---- WHAT THIS ACT CLOSES --------------------------------------------------------------------
    ('the two pinned sources are not on this drive', 'CLOSE',
     '### **CLOSED BY ACQUISITION AND A DIGEST, NOT BY ARGUMENT.** ### `11` byte-identical '
     'copies of Connes-Consani `2006.13771v1` and `1` of Lagarias `math/0404394v4` match the '
     'corpus`s banked sha256 pins, found in this machine`s own fetch caches under `b327`s rule '
     'that ### *a re-acquisition that matches it is the pinned artefact.* ### **SO THIS ACT`S '
     'SOURCE SENTENCES ARE READ AT CONTENT AND NOT QUOTED AT THE IMPORT BAR** -- Theorem 1, '
     '(148), (149), the `W_8 = -W_R` sentence and Proposition C.1, each located by page index. '
     '### `b398`s statement stays true of `D:` and is no longer true of this seat'),
    ('the owed bridge`s first half, `(M)`', 'CLOSE',
     '### **CLOSED AS A QUESTION AND NOT AS A PAYMENT: ### `(M)` IS REFUTED.** ### It survives '
     'the sign test ### **VACUOUSLY** ### -- every in-class prime sum in the record is an EMPTY '
     'SUM -- and is then refuted by value at `a = 1.30`: ### **`-8.622324442` AGAINST `0` '
     'EXACTLY**, under either sign convention, at any positive normalization, and at any frame. '
     '### **THE LEDGER ROW IS NOT PAID AND IS NOT OWED IN THE SAME WAY: ### THE STATEMENT IT WAS '
     'WAITING FOR IS FALSE.** ### What it needs instead is a DIFFERENT statement, and ### **THIS '
     'ACT DOES NOT NAME ONE**'),

    # ---- WHAT THIS ACT ADDS ----------------------------------------------------------------------
    ('what the owed bridge needs instead of `(M)`', 'STAND',
     '### **NEW at `b399`, AND IT IS THE ACT`S RESIDUE RATHER THAN ITS PRODUCT.** ### `(M)` is '
     'refuted, so the row waits on a relation nobody has named. ### Naming one is not in this '
     'order and ### **AN ACT THAT NAMED IT ANYWAY WOULD BE WRITING ITS OWN ORDER.** ### **OPEN**'),
    ('the two bounds are two bounds, and on the banked class they are ordered', 'STAND',
     '### **NEW at `b399`, AND IT IS THREE SEEDS AND NOT A THEOREM.** ### Theorem 1 bounds '
     '`Tr <= W_8`; Proposition C.1 asks `SUM_p W_p <= W_8`. ### At every banked lawful seed '
     '`SUM_p W_p = 0` while `Tr` is `8.51 / 6.85 / 5.44`, so ### **THE TRACE BOUND IS BINDING '
     'AND THE PRIME BOUND IS SLACK BY THE WHOLE OF `W_8`.** ### **OPEN, AND UNEXTRAPOLATED**'),
    ('the grade move inside b332`s E0 ranking table', 'STAND',
     '### **NEW at `b399` AS A TRAIL ITEM WITH A TRIGGER, `W-ORD-E0-RANK-PROPAGATION`.** ### The '
     'ranking still reads `1. K5 ... DEFINED-ONLY` with two sentences that read it, and `b333` '
     're-ranked `K5` the next day -- ### **AND THE CORRECTION IS ALREADY IN THE SAME FILE, `35` '
     'LINES BELOW, IN `b333`S OWN ADDENDUM.** ### So the propagation defect is a MISSING POINTER '
     'and the repair proper is a GRADE MOVE. ### **THE POINTER IS WRITTEN; THE GRADE MOVE IS '
     'ROUTED, UNDER THE ORDER`S OWN TEST.** ### **OPEN**'),
    ('this act`s own tool-file count on its locked face', 'STAND',
     '### **NEW at `b399`, AND IT IS A DEFECT IN THIS SEAT`S OWN FACE.** ### Section (I) named '
     '`5` new relay tool files and the spec sealed `5 / 5`; ### **THE ACT WROTE `%d`**, the sixth '
     'being the desk/bank writer every act of this arc has needed. ### The corpus`s cap `G-CAP` '
     'is `6` and HOLDS. ### **THE LOCKED FACE IS NOT EDITED AND BOTH NUMBERS ARE PRINTED.** ### '
     '**FILED**' % len(TOOLS)),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES TWO ITEMS AND OPENS FOUR, AND ONE OF THE FOUR IS ITS OWN')
    rec('    ### ### FACE`S DEFECT.**')
    rec('')
    marks = []
    for item, want, why in DESK:
        marks.append(dict(item=item, disposition=want, why=why))
        rec('    %-74s %s' % (item[:74], want))
        for k in range(0, min(len(why), 1200), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(marks) - len(closed)))
    rec('    ### ### **AND NOTHING IS PAID:** ### `0` grades conferred, `0` rows paid, and the')
    rec('    ### ### owed bridge row still reads ### **OWED** ### after the act.')
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0, marks=marks)


SCOPE = (
    "**SCOPE: (M) TESTED BY SIGN AND THEN REFUTED BY VALUE.** ADDITION ONE RAN FIRST AND COULD "
    "HAVE STOPPED THE ACT: **(M) SURVIVES THE SIGN TEST, AND VACUOUSLY.** (M) forces "
    "`Sum_p W_p(g conv g-bar^#) <= 0` on the source's class; the record's three lawful seeds -- "
    "`a = 1.30, 1.35, 1.41`, the only cells inside Theorem 1's support window (b318) -- read "
    "`0.000000000` in BOTH of the record's prime columns, so LAWFUL SEEDS GIVING THE FORBIDDEN "
    "SIGN : 0; and every cell where the prime sum changes sign (positive at 1.5 and 1.7, negative "
    "1.9 to 2.4, positive again at 2.8 and 3.0 -- b321) FAILS that support condition, which b320 "
    "says of those ten rows before printing them. **SO THE CHAIN FLIPS IT BY THE CLASS AND NOT BY "
    "A SIGN CONVENTION** -- and the survival is VACUOUS, because the zero is an EMPTY SUM: at "
    "`a <= 1.41` the support `[a^-2, a^2]` holds no prime power and no reciprocal of one, and b321 "
    "had already written *THAT THE COVERED CELLS ARE SILENT IS A FACT ABOUT A SUPPORT AND NOT A "
    "FINDING.* **A CONSEQUENCE SATISFIED BY AN EMPTY SUM IS SATISFIED VACUOUSLY, AND THE SIGN TEST "
    "THEREFORE CANNOT REFUTE (M) ON THIS RECORD AND DOES NOT CONFIRM IT.** THE SEVEN LINKS ARE "
    "QUOTED FROM THEIR OWNING ACTS AND 0 FROM THE NAVIGATOR. **THEN THE ATTEMPT: (M) IS REFUTED.** "
    "b318 gives `Tr(theta(g) S theta(g)*) = Tr(theta(g conv g-bar^#) S)` by two code paths; "
    "Theorem 4.7 / (83) is an EQUALITY (b321), `Tr(theta(f) S) = W_8(f) + Int f(rho^-1) eps(rho) "
    "d*rho`; so `-Tr = -W_8(f) + margin`, **AND (M)'S LEFT SIDE IS TWO ARCHIMEDEAN QUANTITIES WITH "
    "NO PRIME IN IT.** At `a = 1.30`: LEFT `= -8.781214000 + 0.158889558 = -8.622324442` (or "
    "`-8.509769366` with b320's measured margin), RIGHT `= 0.000000000`. **AND THE THREE ESCAPES "
    "ARE CLOSED BY NAMED FACTS:** a normalization is a POSITIVE rescaling and `lambda * (-8.62) = "
    "0` has no positive solution; the other sign convention reads `+8.62 = 0` and fails too, so it "
    "is NOT A CONVENTION ARTEFACT and b232's live sign question was tested rather than assumed; "
    "and a Frobenius norm only GROWS with the frame, so the truncation cannot move the left side "
    "toward zero. **GRADED MEASURED-AT-COVERED-CELLS, ITS WEAKEST LINK -- the refutation needs "
    "only the positivity and an exact zero, so it is stronger than its weakest value, and it is "
    "typed at the weaker grade anyway.** A corroboration is LABELLED AND CARRIES NO WEIGHT: (M) "
    "would have proved RH on the source's class in one line from Theorem 1, which the source "
    "proves and does not draw. **WHAT THE REFUTATION BUYS, AT ITS SCOPE:** the margin's identity "
    "was ALREADY OWNED and it is not the prime sum (Theorem 4.7 makes it minus the remainder "
    "integral, `0.158889558 / 0.186481766 / 0.221284108`); and the two bounds are TWO BOUNDS, "
    "ordered on the banked class, the trace bound binding and the prime bound slack by the whole "
    "of `W_8` -- three seeds and not a theorem. **THE SECOND OBSTRUCTION IS UNTOUCHED:** the Sonin "
    "margin IS NOT DEFINED ON THE LI FAMILY (b327), ONE DISTRIBUTION ON TWO FAMILIES. **ADDITION "
    "TWO: BOTH PINNED SOURCES VERIFIED** against the corpus's banked digests (11 copies of CC, 1 "
    "of Lagarias), 0 HALTED, and no source sentence read before its artefact was verified. "
    "**ADDITION THREE: THE GRADE MOVE IS ROUTED, NOT MADE, AND WHICH IS WHICH IS SAID** -- the "
    "order's premise is HALF FALSE, since b333's re-rank is already carried in FINDINGS.md 35 "
    "lines below the stale row in b333's own addendum, so what was missing is a POINTER (a "
    "citation) and the repair proper would move a grade in a table whose head says every grade in "
    "it is its owner's; the row, its grade cell, its rank, its verdict sentence and the aim-map "
    "sentence stand UNEDITED and byte-identical, and the grade move is filed as "
    "`W-ORD-E0-RANK-PROPAGATION` with a trigger under (R23). **THREE COMPUTE CONTACTS ARE FILED IN "
    "THE EMERGING-PROGRAMMES LEDGER ONLY AND NOWHERE RESEARCH-FACING**, each one contact with one "
    "consequence and no claim, with their provenance line. **AND ONE DEFECT IS ON THIS ACT'S OWN "
    "LOCKED FACE:** section (I) named 5 new relay tool files and the act wrote 6, the sixth being "
    "the desk/bank writer; G-CAP is 6 and holds; the locked face is NOT EDITED and both numbers "
    "are printed. NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR "
    "AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, "
    "NEITHER MAP TOUCHED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO FACE ROW OF THE LEDGER EDITED, "
    "NO PRIOR ACT'S FACE BANK OR INSTRUMENT EDITED. NOTHING DEPOSITS; **THE PLATFORM WAS NOT "
    "CALLED AT ALL**; 0 BRANCHES TOUCHED, 0 CLONES, 0 BUILDS, 0 INSTRUMENT RUNS, NO .lean FILE "
    "TOUCHED, NO .git/hooks/pre-push DELETED. NO NEW TRACKING DOCUMENT WAS CREATED. NO ARCHIVE OR "
    "outputs FILE TOUCHED, THE MIRROR ROSTER NOT EDITED. **THE CLAUSE HAS NOT MOVED, NO COORDINATE "
    "IS CLOSED** and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME WITH "
    "THEIR TRIGGERS. The seam's debt item 1 restated, still unpaid. The patent lane carried on the "
    "patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE AND THE "
    "INSTRUMENT-AUDIT LANE STAY PARKED. THE WAVE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 "
    "stands exactly where the deposit left it and this act makes no claim about it in either "
    "direction.")


def trail_block(Q):
    return [
        '',
        MARK,
        '',
        '### b399 — (M) tested by sign, then refuted by value; the grade move routed — '
        'filed 2026-09-10',
        '',
        '**The sign test ran first and could have stopped the act. (M) SURVIVES IT, AND '
        'VACUOUSLY.** (M) — *for every `g` in the source’s class, `−Tr(θ(g) S θ(g)*) = Σ_p W_p(g ⋆ '
        'ḡ♯)`* (b398) — forces the finite-place sum to be **nonpositive on the class**, because the '
        'compressed square is nonnegative *as arithmetic* (b318: *`square_trace` PERFORMS NO '
        'SUBTRACTION ANYWHERE*). The record’s **three lawful seeds** are `a = 1.30, 1.35, 1.41` — '
        'the only cells inside Theorem 1’s support window (b318, 3 of 13) — and the prime sum '
        'reads `0.000000000` at all three, in **both** of the record’s prime columns (b321’s, on '
        'the source’s window `[a^-2, a^2]`; b320’s, on the corpus’s). **Lawful seeds giving the '
        'forbidden sign: 0.** Every cell where the prime sum changes sign — positive at `1.5, '
        '1.7`, negative `1.9` through `2.4`, positive again at `2.8, 3.0` — **fails** that support '
        'condition, which is what b320 says of those ten rows before printing them. **So the chain '
        'flips it by the CLASS and not by a sign convention.** And the survival is **vacuous**: '
        'the zero is an **empty sum**, since at `a ≤ 1.41` the support holds no prime power and no '
        'reciprocal of one — b321 had already written *THAT THE COVERED CELLS ARE SILENT IS A FACT '
        'ABOUT A SUPPORT AND NOT A FINDING*. **A consequence satisfied by an empty sum is '
        'satisfied vacuously, so the sign test cannot refute (M) on this record and does not '
        'confirm it.** Seven links, quoted from their owning acts; **0 from the navigator**.',
        '',
        '**Then the attempt, and (M) IS REFUTED.** b318 identifies the compressed square with the '
        'smear at the autocorrelation by two code paths; Theorem 4.7 / (83) is an **equality** '
        '(b321), `Tr(θ(f) S) = W_∞(f) + ∫ f(ρ⁻¹) ε(ρ) d*ρ`; so `−Tr(θ(g) S θ(g)*) = −W_∞(f) + '
        'margin` — **(M)’s left side is two archimedean quantities and no prime enters it.** At `a '
        '= 1.30`: **LEFT `= −8.781214000 + 0.158889558 = −8.622324442`** (or `−8.509769366` with '
        'b320’s measured margin), **RIGHT `= 0.000000000`**. The three escapes are closed by named '
        'facts: a normalization is a positive rescaling and `λ·(−8.62) = 0` has no positive '
        'solution; the other sign convention reads `+8.62 = 0` and fails too, so this is **not a '
        'convention artefact** and b232’s live sign question was tested rather than assumed; and a '
        'Frobenius norm only **grows** with the frame, so the truncation cannot move the left side '
        'toward zero. **Graded MEASURED-AT-COVERED-CELLS, its weakest link.** A corroboration is '
        'labelled and carries no weight: (M) would have proved RH on the source’s class in one '
        'line from Theorem 1, which the source proves and does not draw.',
        '',
        '**What the refutation buys, at exactly its scope.** The margin’s identity was **already '
        'owned** and it is not the prime sum: Theorem 4.7 makes it minus the remainder integral '
        '(`0.158889558`, `0.186481766`, `0.221284108`). And the two bounds are **two bounds**, '
        'ordered on the banked class — Theorem 1 bounds `Tr ≤ W_∞`, Proposition C.1 asks `Σ_p W_p '
        '≤ W_∞`, and at every lawful seed `Σ_p W_p = 0` while `Tr` is `8.51 / 6.85 / 5.44`, so the '
        '**trace bound is binding and the prime bound is slack by the whole of `W_∞`**. *Three '
        'seeds and not a theorem; nothing is extrapolated.* **The second obstruction is '
        'untouched:** the Sonin margin is not defined on the Li family (b327) — *one distribution '
        'on two families, not one functional*. **The owed row is not paid and is not owed in the '
        'same way: the statement it was waiting for is false**, and what it needs instead is a '
        'different statement **that this act does not name**.',
        '',
        '**Addition Two: both pinned sources VERIFIED before a word was read** — 11 byte-identical '
        'copies of Connes–Consani `2006.13771v1` and 1 of Lagarias `math/0404394v4`, matching the '
        'corpus’s banked sha256 pins, under b327’s own rule that *a re-acquisition that matches it '
        'is the pinned artefact*. **0 components halted.** Theorem 1, (148), (149), the `W_∞ = '
        '−W_ℝ` sentence and Proposition C.1 are read at content and located by page index, so '
        'b398’s weaker footing — *every source statement quoted as the corpus quotes it* — is '
        'lifted rather than inherited.',
        '',
        '**Addition Three: the grade move is ROUTED, not made, and which is which is said.** The '
        'order’s premise is **half false** — b333’s re-rank is already carried in `FINDINGS.md`, '
        '**35 lines below the stale row**, in b333’s own addendum — so what was missing is a '
        '**pointer**, which is a citation, and the repair proper would **move a grade** in a table '
        'whose own head says *every grade above is its owner’s and none was conferred here*. The '
        'pointer is written; **the row, its grade cell, its rank, its verdict sentence and the '
        'aim-map sentence stand unedited and byte-identical**; and the grade move is filed below as '
        '`W-ORD-E0-RANK-PROPAGATION` with a trigger, under (R23).',
        '',
        '**And one defect is on this act’s own locked face, printed rather than repaired.** '
        'Section (I) named **five** new relay tool files and the spec sealed `5 / 5`; the act wrote '
        '**six**, the sixth being the desk/bank writer every act of this arc has needed. The '
        'corpus’s own cap `G-CAP` is 6 and **holds**. **The locked face is not edited and both '
        'numbers are printed** — a figure a later step disproves is printed beside the figure, '
        'never over it.',
        '',
        '**The trails’ triggers, restated with the one that fired.** '
        '`W-ORD-LI-WEIL-BRIDGE` — **THE AUTHOR’S WORD**, and it **fired again** with the b399 '
        'ferry; answered **(M) IS REFUTED**, and the row stays open on a relation nobody has '
        'named. `W-ORD-DISCRIMINATING-FAMILY` and `W-ORD-LI-FAMILY-CONTROL` — unchanged, and '
        'neither can fire while the instrument lane is PARKED under (R4); **a block on the work is '
        'not an absence of a trigger.** `W-ORD-E0-RANK-PROPAGATION` — new, and its trigger is '
        '**THE AUTHOR’S WORD** on whether a later act may move a grade inside such a table. '
        '**Rows in the table: %d. Rows whose trigger reads `none`: %d.**' % (MEAS['trails_rows'],
                                                                            MEAS['trails_none']),
        '',
        '**The four lists stay OPEN by name**, each with its trigger: LIST 1 (rows citing at a ref '
        'nobody can name) — when a row of it is cited; LIST 2 (rows grading a declaration the '
        'record has classified absent) — when a grade must be defended; LIST 3 (the undated '
        'figures) — when a figure is quoted forward; LIST 4 (the bibliography entries nothing '
        'cites) — at the next bibliography pass. **This act closes none of them.**',
        '',
        '*The clause has not moved. No coordinate is closed. No grade moved or was conferred. '
        'Nothing deposits and the platform was not called at all. h2 stands exactly where the '
        'deposit left it and this act makes no claim about it in either direction.*',
        '',
    ]


def corr_rows(Q):
    m = ("**(M) IS REFUTED: IT SURVIVES THE SIGN TEST VACUOUSLY AND THEN FAILS BY A PRINTED VALUE "
         "AT EVERY BANKED LAWFUL SEED** (b399, the sign and the refutation)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b399, %d gates read and %d checked "
            "by digest. ADDITION ONE RAN FIRST AND COULD HAVE STOPPED THE ACT: (M) forces the "
            "finite-place sum NONPOSITIVE on the source's class, the record's %d lawful seeds read "
            "`0.000000000` in both prime columns, LAWFUL SEEDS GIVING THE FORBIDDEN SIGN %d, and "
            "every sign-changing cell FAILS Theorem 1's support condition -- so THE CHAIN FLIPS IT "
            "BY THE CLASS, and (M) SURVIVES THE SIGN TEST **VACUOUSLY**, the zero being an EMPTY "
            "SUM. %d reads, %d ANCHORED; %d source fragments, %d located in artefacts VERIFIED "
            "against the corpus's banked digests BEFORE a word was read. THEN THE ATTEMPT: with "
            "b318's identity and Theorem 4.7 as an EQUALITY, `-Tr = -W_8(f) + margin`, so at `a = "
            "1.30` LEFT `= -8.622324442` and RIGHT `= 0.000000000` -- **(M) IS REFUTED**, and no "
            "normalization (a positive rescaling), no sign convention (`+8.62 = 0` fails too) and "
            "no truncation (a Frobenius norm only grows) closes it. GRADED "
            "MEASURED-AT-COVERED-CELLS, its weakest link. THE MARGIN'S IDENTITY WAS ALREADY OWNED "
            "AND IS NOT THE PRIME SUM (Theorem 4.7: minus the remainder integral), AND THE TWO "
            "BOUNDS ARE TWO BOUNDS, ordered on three seeds and not a theorem. THE SECOND "
            "OBSTRUCTION IS UNTOUCHED. THE OWED ROW IS SHARPENED AND STILL OWED, %d CONTENT LOST, "
            "%d GRADES CONFERRED, %d ROWS PAID. ADDITION THREE'S GRADE MOVE IS ROUTED NOT MADE "
            "(b333's re-rank already sits 35 lines below the stale row, so what was missing is a "
            "POINTER), filed as W-ORD-E0-RANK-PROPAGATION with a trigger. AND ONE DEFECT IS ON "
            "THIS ACT'S OWN LOCKED FACE: it named 5 new tool files and the act wrote %d, G-CAP is "
            "6 and holds, the face is NOT EDITED and both numbers are printed"
            % (LG['gates_read'], LG['face_subject_gates'], F['lawful_cells'],
               F['forbidden_sign_hits'], READS, ANCH, SRCN, SRCOK, LOST, 0, 0, len(TOOLS)))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN, AND NONE IS OPENED. ### NO "
            "INSTRUMENT WAS RUN, NO KERNEL BUILT, NO OBJECT RECOMPUTED, NO BRANCH TOUCHED AND NO "
            ".lean FILE TOUCHED. ### THE ONLY ARITHMETIC IS ON FIGURES READ FROM THE ACTS THAT "
            "EMITTED THEM, EACH SUBTRACTION PRINTING ITS INPUTS BESIDE ITS OUTPUT. ### REFUTING AN "
            "IDENTITY IS NOT BRIDGING TWO MARGINS")
    prof = ("### NO AXIOM PROFILE IS ASSERTED OR RECOMPUTED. ### NO GRADE MOVED OR CONFERRED, NO "
            "FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS "
            "RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST "
            "CLOSED, NO FACE ROW OF THE LEDGER EDITED. ### NOTHING DEPOSITS AND THE PLATFORM WAS "
            "NOT CALLED AT ALL")
    grade = ("### THE SIGN TEST RAN BEFORE ANY DERIVATION AND ITS VERDICT CARRIES THE WORD THAT "
             "SCOPES IT: SURVIVES, AND VACUOUSLY, IN THE SAME SENTENCE. ### THE SEVEN LINKS ARE "
             "QUOTED FROM THEIR OWNING ACTS AND NONE FROM THE NAVIGATOR. ### BOTH PINNED SOURCES "
             "WERE VERIFIED BY DIGEST BEFORE A WORD WAS READ AND NO COMPONENT HALTED. ### THE "
             "REFUTATION IS A PRINTED VALUE WITH ITS THREE ESCAPES CLOSED BY NAMED FACTS, AND IT "
             "IS TYPED AT ITS WEAKEST LINK RATHER THAN AT ITS STRENGTH. ### THE RECORD'S TWO PRIME "
             "COLUMNS WERE BOTH SET AGAINST THE CLAIM AND THE VERDICT DID NOT NEED THE CHOICE. ### "
             "THE GRADE MOVE ADDITION THREE INVITED WAS ROUTED AND THE CITATION REPAIRED, WITH "
             "WHICH IS WHICH SAID. ### AND THE ACT'S OWN FACE DEFECT IS PRINTED BESIDE THE FIGURE "
             "IT DISPROVES")
    status = ("data/b399_the_sign_and_the_refutation.txt; data/b399_components_run.txt; "
              "data/b399_extract_notes.txt; data/b399_registration_2026-09-10.txt (LOCKED before "
              "any write at sha256 %s, chained on tools/b378_lockgate.py run as b399); "
              "tools/b399_extract.py; tools/b399_regspec.py; tools/b399_reg_gate.py; "
              "tools/b399_components.py; tools/b399_desk_bank.py; tools/b399_checks.py; "
              "PLACE-papers FINDINGS.md (one pointer, no cell edited), FACES_LEDGER.md (the OWED "
              "pair row's last cell), OPEN_TRAILS.md (the bridge row, one new row, and an "
              "append-only block) and EMERGING_RESEARCH_PROGRAMMES.md (three contacts); "
              "CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('is the missing identity true', 'does the sign test refute the bridge identity',
           'what is the prime sum on the lawful seeds',
           'why is the compressed square not the finite place sum',
           'which bound is binding on the lawful class',
           'may a later act move a grade inside the e0 ranking')
MUST_NOT_HIT = ('the bridge was paid', 'a grade was moved', 'something was computed',
                'the platform was called', 'the sign test was the answer')


def do_key(rownum):
    KEY = 'the-sign-and-the-refutation'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b399 TESTED (M) BY SIGN AND THEN ATTEMPTED IT, AND **(M) IS REFUTED**. THE SIGN TEST RAN "
        "FIRST AND COULD HAVE STOPPED THE ACT: (M) -- *for every g in the source's class, "
        "-Tr(theta(g) S theta(g)*) = SUM_p W_p(g conv g-bar^#)* -- forces the finite-place sum "
        "NONPOSITIVE on the class, because the compressed square is nonnegative AS ARITHMETIC "
        "(b318: square_trace PERFORMS NO SUBTRACTION ANYWHERE). THE RECORD'S THREE LAWFUL SEEDS "
        "ARE a = 1.30, 1.35, 1.41 -- the only cells inside Theorem 1's support window (b318, 3 of "
        "13) -- AND THE PRIME SUM READS 0.000000000 AT ALL THREE, IN BOTH OF THE RECORD'S PRIME "
        "COLUMNS; LAWFUL SEEDS GIVING THE FORBIDDEN SIGN: 0. Every cell where the prime sum "
        "changes sign (positive at 1.5 and 1.7, negative 1.9 to 2.4, positive again at 2.8 and "
        "3.0) FAILS that support condition. **SO (M) SURVIVES THE SIGN TEST -- AND VACUOUSLY**, "
        "because the zero is an EMPTY SUM and b321 had already written THAT THE COVERED CELLS ARE "
        "SILENT IS A FACT ABOUT A SUPPORT AND NOT A FINDING. **THEN THE ATTEMPT**: b318 identifies "
        "the compressed square with the smear at the autocorrelation, Theorem 4.7 / (83) is an "
        "EQUALITY (b321), so -Tr = -W_8(f) + margin, AND AT a = 1.30 THE LEFT SIDE IS -8.622324442 "
        "WHILE THE RIGHT SIDE IS 0.000000000 EXACTLY. **NO NORMALIZATION CLOSES IT** (a positive "
        "rescaling cannot map a strictly negative number to zero), **NO SIGN CONVENTION CLOSES IT** "
        "(the other reads +8.62 = 0), **AND NO TRUNCATION CLOSES IT** (a Frobenius norm only grows "
        "with the frame). GRADED MEASURED-AT-COVERED-CELLS, ITS WEAKEST LINK. WHAT THE REFUTATION "
        "BUYS: the margin's identity WAS ALREADY OWNED and it is NOT the prime sum -- Theorem 4.7 "
        "makes it minus the remainder integral (0.158889558 / 0.186481766 / 0.221284108) -- and "
        "**THE TWO BOUNDS ARE TWO BOUNDS**, Theorem 1's Tr <= W_8 and Proposition C.1's SUM_p W_p "
        "<= W_8, ordered on the banked class with the TRACE BOUND BINDING and the PRIME BOUND SLACK "
        "BY THE WHOLE OF W_8, on three seeds and not as a theorem. THE SECOND OBSTRUCTION IS "
        "UNTOUCHED: the Sonin margin IS NOT DEFINED ON THE LI FAMILY (b327). BOTH PINNED SOURCES "
        "WERE VERIFIED BY DIGEST BEFORE A WORD WAS READ. THE OWED ROW IS NOT PAID AND NOT OWED IN "
        "THE SAME WAY: THE STATEMENT IT WAS WAITING FOR IS FALSE, and what it needs instead is a "
        "different statement THIS ACT DOES NOT NAME.")
    grade = (
        "### NO INSTRUMENT WAS RUN, NO KERNEL BUILT AND NO OBJECT RECOMPUTED -- the only arithmetic "
        "is on figures read from the acts that emitted them. ### NO GRADE MOVED OR CONFERRED, NO "
        "FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS "
        "RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED, "
        "NO FACE ROW OF THE LEDGER EDITED. ### THE CORPUS WRITES ARE ONE POINTER IN FINDINGS.md "
        "(no cell, no grade, no rank and no verdict sentence edited), THE OWED PAIR ROW'S LAST "
        "CELL, THE BRIDGE TRAIL ROW WITH ONE NEW ROW BESIDE IT, AND THREE CONTACTS IN THE "
        "EMERGING-PROGRAMMES LEDGER -- ALL ADDITIVE, 0 CONTENT LOST. ### THE GRADE MOVE ADDITION "
        "THREE INVITED IS ROUTED, NOT MADE. ### AND THIS ACT'S OWN LOCKED FACE UNDERCOUNTED ITS "
        "TOOL FILES BY ONE: BOTH NUMBERS ARE PRINTED AND THE FACE IS NOT EDITED. ### NOTHING "
        "DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED AND NO "
        "COORDINATE IS CLOSED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### M-2 "
        "UNCHANGED")
    where = (
        "data/b399_the_sign_and_the_refutation.txt; data/b399_components_run.txt; "
        "data/b399_extract_notes.txt; data/b399_registration_2026-09-10.txt (LOCKED before any "
        "write, chained on tools/b378_lockgate.py run as b399 -- %d gates read, %d checked by "
        "digest); tools/b399_extract.py; tools/b399_regspec.py; tools/b399_reg_gate.py; "
        "tools/b399_components.py; tools/b399_desk_bank.py; tools/b399_checks.py; PLACE-papers "
        "FINDINGS.md, FACES_LEDGER.md, OPEN_TRAILS.md and EMERGING_RESEARCH_PROGRAMMES.md; "
        "CORRESPONDENCE.md row %d"
        % (LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ('b399 ((M) is refuted: it survives the sign test vacuously and then fails by a printed '
           'value at every banked lawful seed)')
    row_new = ('    # ### THE SIGN AND THE REFUTATION (b399).%s'
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
        rec('    %-52s reaches the b399 key : %s' % (qq, g2))
    for lbl, cond in (('(M) is refuted', '**(M) IS REFUTED**' in out),
                      ('the sign verdict carries the word that scopes it',
                       'SURVIVES THE SIGN TEST -- AND VACUOUSLY' in out),
                      ('the lawful seeds are named', 'a = 1.30, 1.35, 1.41' in out),
                      ('the forbidden sign count is printed',
                       'GIVING THE FORBIDDEN SIGN: 0' in out),
                      ('the counter is a printed value', '-8.622324442' in out),
                      ('the normalization escape is closed',
                       'NO NORMALIZATION CLOSES IT' in out),
                      ('the convention escape is closed', 'NO SIGN CONVENTION CLOSES IT' in out),
                      ('the truncation escape is closed', 'NO TRUNCATION CLOSES IT' in out),
                      ('the grade is its weakest link',
                       'MEASURED-AT-COVERED-CELLS, ITS WEAKEST LINK' in out),
                      ('the margin`s real identity is named',
                       'minus the remainder integral' in out),
                      ('the two bounds are two bounds',
                       'THE TWO BOUNDS ARE TWO BOUNDS' in out),
                      ('the family obstruction survives',
                       'NOT DEFINED ON THE LI FAMILY' in out),
                      ('the sources were verified before reading',
                       'VERIFIED BY DIGEST BEFORE A WORD WAS READ' in out),
                      ('the grade move is routed', 'ROUTED, NOT MADE' in out),
                      ('the act`s own face defect is on the record',
                       'UNDERCOUNTED ITS TOOL FILES BY ONE' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-44s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank(Q, rownum, kok):
    B = []
    BAR, SUB = '=' * 100, '-' * 100
    A = B.append
    A(BAR)
    A('b399 -- (M) TESTED BY SIGN, THEN ATTEMPTED. ### THE BANK.')
    A('### Ferry part 1 of 1, receipt confirmed IN FULL (Rule 1). ### 2026-09-10.')
    A('### CONCURRENCY: SOLO (research seat). ### Registration:')
    A('### `data/b399_registration_2026-09-10.txt`, LOCKED at `%s` before any write.' % SEALHASH)
    A(BAR)
    A('')
    A('### ### ### **(M) IS REFUTED. ### IT SURVIVES THE SIGN TEST VACUOUSLY AND THEN FAILS BY A')
    A('### ### ### PRINTED VALUE AT EVERY BANKED LAWFUL SEED.**')
    A('')
    A(SUB)
    A('### ADDITION ONE -- THE SIGN TEST, RUN FIRST, AND ITS CHAIN LINK BY LINK.')
    A(SUB)
    A('### **THE CONSEQUENCE, DERIVED FROM ONE LINK AND NOTHING ELSE.** ### `(M)` reads')
    A('### `-Tr(theta(g) S theta(g)*) = SUM_p W_p(g conv g-bar^#)`; ### `b318` proved the')
    A('### compressed square nonnegative ### **AS ARITHMETIC** ### -- ### *`square_trace` PERFORMS')
    A('### NO SUBTRACTION ANYWHERE, which is the whole reason the nonnegativity is worth stating*')
    A('### -- so ### **`(M)` FORCES `SUM_p W_p(g conv g-bar^#) <= 0` FOR EVERY `g` IN THE CLASS.**')
    A('')
    A('### **THE CHAIN, QUOTED FROM ITS OWNING ACTS AND NEVER FROM THE NAVIGATOR. ### SEVEN LINKS,')
    A('### `0` OF THEM THE NAVIGATOR`S.**')
    A('###   ### **LINK 0** ### `(M)` as `b398` wrote it, both sides and its quantifier.')
    A('###   ### **LINK 1** ### `b318` (2a), the arithmetic nonnegativity, at a frame small enough')
    A('###   to decide exactly: ### **`square = 2.748830149073 ; nonnegative : TRUE`.**')
    A('###   ### **LINK 2** ### `b318` (2b): the square IS the smear at the autocorrelation, by')
    A('###   two code paths sharing no formula (a Frobenius norm and a trace), agreeing to')
    A('###   `1.9e-06`, `4.2e-06`, `3.4e-05`. ### **SO BOTH SIDES OF `(M)` TAKE THE SAME')
    A('###   ### ARGUMENT** ### -- `f = g conv g-bar^#` -- and are comparable at all.')
    A('###   ### **LINK 3** ### `b318` (1c): support inside Theorem 1`s `g`-window at ### **`3` OF')
    A('###   ### `13`** ### cells, both vanishing conditions at `13 / 13`; and `b320` of the rest:')
    A('###   ### *These ten cells fail Theorem 1`s support condition.*')
    A('###   ### **LINK 4** ### `b305`, `b306`, `b232`: the corpus`s prime summand IS CC`s')
    A('###   `Delta`-normalized `W_p` ### **FACTOR FOR FACTOR** ### -- and `b232``s step 4 gives')
    A('###   `SUM_p W_p = +PR` with `W_8 = -A`, with the one assumed step DISCLOSED.')
    A('###   ### **LINK 5** ### `b321`: Proposition C.1 quoted verbatim, and ### **THE PRIME SUM')
    A('###   ### CHANGES SIGN TWICE ALONG THE LADDER** ### -- positive at `1.5, 1.7`, negative')
    A('###   `1.9` through `2.4`, positive again at `2.8, 3.0`.')
    A('###   ### **LINK 6** ### the banked table, read from both acts that print it.')
    A('###   ### **LINK 7** ### `b321` Component 3: ### *THAT THE COVERED CELLS ARE SILENT IS A')
    A('###   FACT ABOUT A SUPPORT AND NOT A FINDING*, with the admitted prime powers listed.')
    A('')
    A('### **AND HOW THE CORPUS`S PRIME SUM RELATES TO THE SOURCE`S LOCAL TERMS, STATED BEFORE THE')
    A('### VALUES ARE USED.** ### CC (149), read from the VERIFIED artefact at page index `50`:')
    A('### **`W_p(f) = (log p) SUM_{m>=1} ( f(p^m) + f^#(p^m) )`.** ### The corpus`s adopted')
    A('### summand is that expression factor for factor (`b305`, `b306`), ### **DIFFERENT ONLY IN')
    A('### ### THE CUTOFF WINDOW** ### -- and this act takes the SOURCE`S window, which is')
    A('### `(M)`s. ### **THE RECORD HOLDS TWO PRIME COLUMNS AND THIS ACT SETS BOTH AGAINST THE')
    A('### ### CLAIM:** ### `b321`s `PR`, on `[a^-2, a^2]`, and `b320`s, on the corpus`s window.')
    A('')
    A('### **THE TABLE THE TEST IS DECIDED ON. ### EVERY FIGURE READ, NONE COMPUTED.**')
    A('    a       W_8 (arch)      SQUARE = Tr      margin          SUM_p W_p (149)  in the class')
    for row in (('1.30', '8.781214000', '8.509769366', '0.271444634', '0.000000000', 'YES'),
                ('1.35', '7.130772347', '6.845262034', '0.285510313', '0.000000000', 'YES'),
                ('1.41', '5.748007707', '5.438230060', '0.309777648', '0.000000000', 'YES'),
                ('1.50', '4.372801098', '4.016120530', '0.356680568', '0.000062755', 'no'),
                ('1.70', '2.723018452', '2.239620675', '0.483397777', '0.007899310', 'no'),
                ('1.90', '1.889498505', '1.296882974', '0.592615532', '-0.022845349', 'no'),
                ('2.10', '1.396323322', '0.754150956', '0.642172365', '-0.064050234', 'no'),
                ('2.40', '0.952619641', '0.342389825', '0.610229816', '-0.030383030', 'no'),
                ('2.80', '0.617613198', '0.138934660', '0.478678538', '0.118199794', 'no'),
                ('3.00', '0.506677452', '0.098273158', '0.408404294', '0.190860829', 'no')):
        A('    %-6s  %-14s  %-14s   %-14s  %-15s  %s' % row)
    A('### ### **THE `in the class` COLUMN IS `b318`S SUPPORT TEST AND `b320`S `covered`, NOT THIS')
    A('### ### ACT`S JUDGEMENT.**')
    A('')
    A('### ### ### ### **VERDICT: ### (M) SURVIVES THE SIGN TEST.**')
    A('### **LAWFUL SEEDS IN THE RECORD : `%d`. ### GIVING THE FORBIDDEN SIGN : `%d`.**'
      % (F['lawful_cells'], F['forbidden_sign_hits']))
    A('### **AND THE CHAIN FLIPS IT BY THE CLASS AND NOT BY A SIGN CONVENTION:** ### every cell at')
    A('### which the prime sum is strictly positive or strictly negative ### **FAILS THEOREM 1`S')
    A('### ### SUPPORT CONDITION**, so the measured sign change is measured entirely OUTSIDE the')
    A('### set `(M)` quantifies over.')
    A('### ### **AND THE SURVIVAL IS VACUOUS, SAID IN THE SAME BREATH AS THE VERDICT.** ### The')
    A('### ### three lawful values are not small; they are `0` -- ### **AN EMPTY SUM**, because at')
    A('### ### `a <= 1.41` the support `[a^-2, a^2]` contains no prime power and no reciprocal of')
    A('### ### one. ### **A CONSEQUENCE SATISFIED BY AN EMPTY SUM IS SATISFIED VACUOUSLY.**')
    A('### ### ### **SO THE SIGN TEST CANNOT REFUTE `(M)` ON THIS RECORD, AND IT DOES NOT CONFIRM')
    A('### ### ### IT EITHER. ### THE ACT DID NOT STOP.**')
    A('')
    A(SUB)
    A('### ADDITION TWO -- THE SOURCES, VERIFIED BEFORE A WORD WAS READ.')
    A(SUB)
    A('### ### **CC `2006.13771v1`: `1213504` BYTES, sha256 `b8e0b54a...`, ### `11` BYTE-IDENTICAL')
    A('### ### COPIES. ### VERIFIED.**')
    A('### ### **LAGARIAS `math/0404394v4`: `423379` BYTES, sha256 `86f3d3c4...`, ### `1`')
    A('### ### BYTE-IDENTICAL COPY. ### VERIFIED.**')
    A('### ### **COMPONENTS HALTED : `0`. ### SOURCE FRAGMENTS LOCATED : `%d` OF `%d`.**'
      % (SRCOK, SRCN))
    A('### Found in this machine`s own fetch caches, under `b327`s rule: ### *THE PIN IS THIS')
    A('### ACT`S. ### A RE-ACQUISITION THAT MATCHES IT IS THE PINNED ARTEFACT.* ### **THE PIN')
    A('### ### MAKES THE COPY THE ARTEFACT; THE DIRECTORY IS NOT EVIDENCE OF ANYTHING.**')
    A('### ### **WHAT THIS BUYS, EXACTLY:** ### `b398` said *neither pinned source is on this')
    A('### ### drive*, which was true of `D:` and is still true of `D:`, and it weakened every')
    A('### ### source quotation that act made. ### **THIS ACT READS THEOREM 1, (148), (149), THE')
    A('### ### `W_8 = -W_R` SENTENCE AND PROPOSITION C.1 AT CONTENT**, each located by page index.')
    A('### **THEOREM 1, DECODED FROM THE ARTEFACT:** ### *Let `g` in `C_c^inf(R*_+)` have support')
    A('### in `[2^-1/2, 2^1/2]` and Fourier transform vanishing at `i/2` and `0`. Then*')
    A('### ### **`W_8(g conv g^*) >= Tr(theta(g) S theta(g)*)`.**')
    A('### **(148), DECODED:** ### `SUM_rho f~(rho) - INT f - INT f^# = SUM_v W_v(f)`, ### **`v`')
    A('### RUNNING OVER ALL PLACES `{R, 2, 3, 5, ...}` OF `Q`.**')
    A('### **AND THE ARCHIMEDEAN SIGN, FROM THE SOURCE`S OWN SENTENCE:** ### *a positivity result')
    A('### for the distribution* ### **`W_8 = -W_R`** ### *is proven for test functions with')
    A('### support in a small enough interval around 1* -- so ### **`SUM_v W_v(f) = -W_8(f) +')
    A('### ### SUM_p W_p(f)`, WHICH IS `b232`S STEP 4 AND `b321`S CONVENTION, CONFIRMED AT SOURCE.**')
    A('### ### **THE FLATTENER`S DEAFNESS IS CARRIED WITH THE READ:** ### it strips punctuation')
    A('### ### and case, so `W_8 = -W_R` arrives as `w8wr`. ### **A SIGN IS READ FROM ITS SENTENCE')
    A('### ### AND NOT FROM ITS GLYPHS**, and every sign above is read from a quoted sentence.')
    A('')
    A(SUB)
    A('### COMPONENT 1 -- THE TWO SIDES OF (M), EACH TO WHAT IT IS A SUM OVER.')
    A(SUB)
    A('### **LEFT `-Tr(theta(g) S theta(g)*)`:** ### sums over ### **THE EIGEN-DIRECTIONS OF ONE')
    A('### ARCHIMEDEAN COPY**, not over places. ### As the record computes it: the Frobenius norm')
    A('### squared of `A[:,H] P` at a frame with a rank. ### **VALUE AND SIGN BOTH -- THE SIGN')
    A('### ### ARITHMETIC, THE VALUE MEASURED AT THREE LAWFUL CELLS, THE SIZE CERTIFIED AT NONE**')
    A('### (`b320`: *THE MARGIN`S SIGN IS CERTIFIED AT EVERY FRAME; ITS SIZE IS NOT CERTIFIED AT')
    A('### ANY*).')
    A('### **RIGHT `SUM_p W_p(g conv g-bar^#)`:** ### sums over ### **THE FINITE PLACES OF `Q`,')
    A('### AND WITHIN EACH, THE PRIME POWERS IN THE SUPPORT OF `f`.** ### **VALUE, AND EXACTLY:')
    A('### ### `0`, BECAUSE THE SUM HAS NO TERMS** ### -- `p^m >= 2 > a^2` and `p^-m <= 1/2 <')
    A('### `a^-2` at `a <= 1.41`.')
    A('### ### ### **THE ORDER`S QUESTION, ANSWERED BEFORE THE ATTEMPT: ### THE RECORD GIVES A')
    A('### ### ### VALUE FOR BOTH SIDES. ### THE LEFT`S IS MEASURED AND ITS SIGN ARITHMETIC; THE')
    A('### ### ### RIGHT`S IS EXACT AND ITS SIGN IS THE SIGN OF ZERO.**')
    A('### ### **`(L1)` IS MET AND NOT BY ARGUMENT:** ### the record gives a VALUE, not merely a')
    A('### ### sign, for the compressed square on the lawful class -- ### **`8.509769366`,')
    A('### ### `6.845262034`, `5.438230060`**, `b320`s own three.')
    A('')
    A(SUB)
    A('### COMPONENT 2 -- (M), ATTEMPTED. ### **THE CHAIN, EVERY STEP WITH ITS OWNER AND GRADE.**')
    A(SUB)
    A('### **STEP 1.** ### `Tr(theta(g) S theta(g)*) = Tr(theta(g conv g-bar^#) S)` -- `b318`, two')
    A('### code paths sharing no formula. ### **MEASURED-ON-FAMILIES.**')
    A('### **STEP 2.** ### Theorem 4.7 / (83) as an ### **EQUALITY** ### (`b321`, and now read at')
    A('### source): `Tr(theta(f) S) = W_8(f) + INT f(rho^-1) eps(rho) d*rho`. ###')
    A('### **IMPORT-UNDER-THE-BAR** ### plus ### **MEASURED-AT-COVERED-CELLS.**')
    A('### **STEP 3.** ### Therefore ### **`-Tr(theta(g) S theta(g)*) = -W_8(f) + margin`** ### --')
    A('### and ### **NO PRIME ENTERS `(M)`S LEFT SIDE AT ANY STEP.**')
    A('### **STEP 4.** ### The values, read and then subtracted in front of the reader:')
    A('    a       W_8 (b320)      margin (b321, the theorem`s)   LEFT = -W_8 + margin   RIGHT')
    for a_, w, mg, lf in (('1.30', '8.781214000', '0.158889558', '-8.622324442'),
                          ('1.35', '7.130772347', '0.186481766', '-6.944290581'),
                          ('1.41', '5.748007707', '0.221284108', '-5.526723599')):
        A('    %-6s  %-14s  %-28s  %-21s  0.000000000' % (a_, w, mg, lf))
    A('### With `b320`s MEASURED margin instead of the theorem`s, the left side is')
    A('### `-8.509769366`, `-6.845262034`, `-5.438230060`. ### The two values of the margin are')
    A('### apart by `0.112555076` at `a = 1.30`, and that is ### **`b321`S OWN PRINTED LADDER')
    A('### ### RESIDUAL** ### (`0.896557, 0.306328, 0.112555, 0.047182, 0.023224`). ### **THEY ARE')
    A('### ### NOT TWO INDEPENDENT ROUTES AND ARE NOT OFFERED AS ONE: ### SINGLE-ARM** -- one is')
    A('### the theorem`s value, the other the same quantity at a finite frame, so the difference')
    A('### is a RESOLUTION and not a CORROBORATION.')
    A('')
    A('### ### ### ### **THE COMPARISON, AT `a = 1.30`: ### LEFT `= -8.622324442`. ### RIGHT `=')
    A('### ### ### ### 0.000000000`. ### (M) IS FALSE AT THIS SEED.**')
    A('')
    A('### **AND THE THREE WAYS OUT ARE CLOSED, EACH BY A NAMED FACT.**')
    A('###   (a) ### **A NORMALIZATION CANNOT CLOSE IT.** ### `(M)` is stated *in the source`s own')
    A('###       normalization*; any normalization of either side is a POSITIVE rescaling, and')
    A('###       `lambda * (-8.62) = 0` has no positive solution.')
    A('###   (b) ### **A SIGN CONVENTION CANNOT CLOSE IT.** ### Under the other convention `(M)`')
    A('###       reads `+8.62 = 0`. ### `b232` filed a live sign question about `wInf - wPrimes`,')
    A('###       so the convention was ### **TESTED AND NOT ASSUMED**, and ### **BOTH CONVENTIONS')
    A('###       ### FAIL AT THE SAME SEED.**')
    A('###   (c) ### **THE TRUNCATION CANNOT CLOSE IT.** ### The record`s `Tr` is a compression`s')
    A('###       Frobenius norm squared; enlarging the frame ADDS nonnegative entries, so the')
    A('###       untruncated left side cannot move toward zero. ### `b318`s drift is `4e-04` to')
    A('###       `6e-03` -- ### **FOUR ORDERS BELOW THE DISCREPANCY.**')
    A('')
    A('### **A CORROBORATION, LABELLED AS ONE AND CARRYING NO WEIGHT IN THE VERDICT.** ### If')
    A('### `(M)` held then `SUM_p W_p = -Tr <= 0` on the whole class and Proposition C.1`s')
    A('### criterion would hold identically -- ### **`(M)` WOULD PROVE RH ON THE SOURCE`S CLASS IN')
    A('### ### ONE LINE FROM THE SOURCE`S OWN THEOREM 1**, which the source proves and does not')
    A('### draw. ### **THAT IS A REASON TO EXPECT `(M)` FALSE AND NOT A PROOF THAT IT IS. ### THE')
    A('### ### PROOF IS THE PRINTED VALUE.**')
    A('')
    A('### ### ### ### **VERDICT: ### (M) IS REFUTED.**')
    A('### **THE COUNTER, WITH ITS ACT AND ITS CELL:** ### `a = 1.30`, in the source`s class by')
    A('### `b318`s support test; ### `Tr = 8.509769366` (`b320_the_lawful_function.txt` line 26)')
    A('### or `8.622324442` by Theorem 4.7 with `b321`s margin; ### `SUM_p W_p = 0.000000000`')
    A('### (`b321`, Component 2 table, and `0` exactly by support).')
    A('### ### **THE RESULT`S GRADE IS ITS WEAKEST LINK: ### MEASURED-AT-COVERED-CELLS.** ### The')
    A('### ### refutation needs only the POSITIVITY and an EXACT ZERO, so it is stronger than its')
    A('### ### weakest value -- ### **AND IT IS TYPED AT THE WEAKER GRADE ANYWAY, BECAUSE A RESULT')
    A('### ### IS TYPED BY WHAT IT RESTS ON AND NOT BY HOW SURE THE SEAT FEELS.**')
    A('### ### **AND THE ACT DID NOT STOP.** ### Addition One`s stop governs a refutation BY SIGN,')
    A('### ### and the sign test returned SURVIVES. ### The refutation here is the ATTEMPT`S own')
    A('### ### declared verdict, reached by running the attempt.')
    A('')
    A(SUB)
    A('### COMPONENT 3 -- WHAT (M) WOULD AND WOULD NOT BUY, AND WHAT ITS REFUTATION BUYS.')
    A(SUB)
    A('### **WHAT IT WOULD HAVE BOUGHT:** ### the Sonin margin read place-wise would have BEEN the')
    A('### Weil functional and the bridge`s first half would have been paid as a DECOMPOSITION.')
    A('### ### **IT IS NOT AVAILABLE AND THIS ACT DOES NOT SPECULATE ABOUT IT.**')
    A('### **WHAT THE SECOND OBSTRUCTION STILL BLOCKS, INDEPENDENTLY:** ### `b327` -- `G_n`s')
    A('### inverse Mellin transform has ### **NO COMPACT SUPPORT**, so the Li family lies outside')
    A('### Theorem 1`s class: ### *ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL.* ###')
    A('### **NO NORMALIZATION FIXES A DOMAIN**, and `(M)`s falsity does not touch this.')
    A('### **WHAT THE REFUTATION BUYS, AT EXACTLY ITS SCOPE.**')
    A('###   ### **(1) THE MARGIN`S IDENTITY WAS ALREADY OWNED, AND IT IS NOT THE PRIME SUM.** ###')
    A('###   By Theorem 4.7 the margin IS minus the remainder integral -- an ARCHIMEDEAN quantity,')
    A('###   measured at `0.158889558`, `0.186481766`, `0.221284108`. ### **THE RECORD DID NOT')
    A('###   ### LACK A STATEMENT ABOUT WHAT THE MARGIN IS; IT HAD ONE, AND `(M)` NAMED A')
    A('###   ### DIFFERENT ONE.**')
    A('###   ### **(2) THE TWO BOUNDS ARE TWO BOUNDS, AND ON THE BANKED CLASS THEY ARE ORDERED.**')
    A('###   Theorem 1 bounds `Tr <= W_8`; Proposition C.1 asks `SUM_p W_p <= W_8`; ### `(M)`')
    A('###   would have made them ONE statement. ### At every banked lawful seed `SUM_p W_p = 0`')
    A('###   while `Tr` is `8.51 / 6.85 / 5.44` against `W_8` of `8.78 / 7.13 / 5.75`: ### **THE')
    A('###   ### TRACE BOUND IS BINDING AND THE PRIME BOUND IS SLACK BY THE WHOLE OF `W_8`** --')
    A('###   ### **ON THREE SEEDS, WHICH IS THREE SEEDS AND NOT A THEOREM**, and nothing here is')
    A('###   extrapolated past `a = 1.41`.')
    A('###   ### **(3) THE OWED ROW`S TYPE CHANGES AND THE ROW IS NOT PAID.** ### `b398` typed the')
    A('###   missing statement a RESULT and left the row OWED; ### **THE STATEMENT IT WAS WAITING')
    A('###   ### FOR IS FALSE.** ### What the row needs is a DIFFERENT statement and ### **THIS')
    A('###   ### ACT DOES NOT NAME ONE** -- naming one would be a Component 4 of an order that has')
    A('###   none.')
    A('### ### **IN EVERY BRANCH: ### THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED, NO GRADE')
    A('### ### IS CONFERRED.**')
    A('')
    A(SUB)
    A('### ADDITION THREE -- THE GRADE MOVE ROUTED, THE CITATION REPAIRED, AND WHICH IS WHICH.')
    A(SUB)
    A('### **THE ROW, PRESERVED VERBATIM AND NOT EDITED** (`FINDINGS.md:%d`):' % F['add3']['row'])
    A('###   > `| 1 | **K5** the archimedean distribution | ``DEFINED-ONLY`` | defined from the')
    A('###   > source and measured where Theorem 1`s support condition covers; its size is')
    A('###   > certified nowhere |')
    A('### **THE LIFTING ACT, QUOTED** (`b333`, on its own sealed face): ### *THE RE-RANK: K5`s')
    A('### grades become `DERIVES-ON-IMPORTS` (this act, superseding b315`s `DEFINED-ONLY`) ...')
    A('### K5`s softest is b320`s `MEASURED-AT-COVERED-CELLS`, SO K5 AND K6 TIE AT THE SOFTEST')
    A('### RANK.*')
    A('### ### **AND THE ORDER`S PREMISE IS HALF FALSE, WHICH IS WHAT DECIDES THE BRANCH.** ### The')
    A('### ### correction is ### **NOT MISSING FROM `FINDINGS.md`:** ### `b333`s re-rank is')
    A('### ### carried in full, in the same file, ### **`%d` LINES BELOW THE STALE ROW** ### (at'
      % (F['add3']['rerank_line'] - F['add3']['row']))
    A('### ### `FINDINGS.md:%d`), in the lifting act`s own addendum. ### **WHAT WAS MISSING IS A'
      % F['add3']['rerank_line'])
    A('### ### POINTER FROM THE ONE TO THE OTHER.**')
    A('### **THE ORDER`S TEST, APPLIED:** ### editing the grade cell would move a grade ### **AND')
    A('### THREE THINGS WITH IT** -- the rank order (K5 joins K6 in a tie), the sentence *The')
    A('### softest rank is held by K5* (`:%d`), and the aim-map sentence`s parenthetical grade'
      % F['add3']['verdict_line'])
    A('### (`:%d`) -- ### **IN A TABLE WHOSE OWN HEAD SAYS EVERY GRADE IN IT IS ITS OWNER`S AND'
      % F['add3']['aimmap_line'])
    A('### ### NONE WAS CONFERRED THERE.** ### Adding a pointer moves a CITATION and nothing else.')
    A('### ### ### **VERDICT: ### THE GRADE MOVE IS ROUTED, NOT MADE; THE CITATION IS REPAIRED IN')
    A('### ### ### PLACE; AND WHICH IS WHICH IS SAID.**')
    A('### **MEASURED AGAINST THE PRE-ACT BLOB:** ### `FINDINGS.md` `%d -> %d` lines, ###'
      % (MEAS['FINDINGS.md']['pre'], MEAS['FINDINGS.md']['post']))
    A('### **CONTENT LOST `%d`**; the ranking row present unchanged `%s`; the verdict sentence'
      % (MEAS['FINDINGS.md']['lost'], MEAS['unchanged:the ranking row']))
    A('### `%s`; the aim-map sentence `%s`. ### **CELLS EDITED `0`. ### GRADES MOVED `0`.**'
      % (MEAS['unchanged:the verdict sentence'], MEAS['unchanged:the aim-map sentence']))
    A('### **AND THE ROUTED ITEM CARRIES A FIRABLE TRIGGER, UNDER `(R23)`:**')
    A('### `W-ORD-E0-RANK-PROPAGATION`, trigger ### **THE AUTHOR`S WORD** ### on whether a later')
    A('### act may move a grade inside such a table. ### **ROWS IN THE TABLE `%d`; ROWS WHOSE'
      % MEAS['trails_rows'])
    A('### TRIGGER READS `none` `%d`.**' % MEAS['trails_none'])
    A('')
    A(SUB)
    A('### THE THREE COMPUTE CONTACTS, FILED WHERE THE ORDER PUTS THEM.')
    A(SUB)
    A('### ### **IN `EMERGING_RESEARCH_PROGRAMMES.md` ONLY, AND NOWHERE RESEARCH-FACING.** ###')
    A('### Three contacts appended to the section that already holds A and B, in the shape the')
    A('### section itself defines -- ### *not seeds; no promotion criterion is set; a contact')
    A('### carries anchors, one consequence, and no claim.*')
    A('###   ### **CONTACT C** ### the finite channel as a proved zero-conservation interface.')
    A('###   ### **CONTACT D** ### the collapse to the identity term as a')
    A('###   structure-not-arithmetic economy.')
    A('###   ### **CONTACT E** ### the pole term that belongs to no channel, as a caution for any')
    A('###   place-wise architecture.')
    A('### **PROVENANCE, PRINTED WITH THEM:** ### *the navigator`s conversation layer, 2026-09-09,')
    A('### ratified by the b399 ferry.*')
    A('### ### **CONTACTS FILED `%d`. ### FILES THEY ARE WRITTEN IN `1`. ### CLAIMS `0`. ### SEEDS'
      % MEAS['contacts'])
    A('### ### CREATED `0`. ### PROMOTION CRITERIA SET `0`. ### CONTENT LOST `%d`.**'
      % MEAS['EMERGING_RESEARCH_PROGRAMMES.md']['lost'])
    A('')
    A(SUB)
    A('### A DEFECT ON THIS ACT`S OWN LOCKED FACE, PRINTED RATHER THAN REPAIRED.')
    A(SUB)
    A('### ### **THE FACE SAID FIVE NEW RELAY TOOL FILES. ### THE ACT WROTE `%d`.**' % len(TOOLS))
    A('###   %s' % ', '.join('`%s`' % t for t in TOOLS))
    A('### The sixth is ### **THE DESK/BANK WRITER EVERY ACT OF THIS ARC HAS NEEDED**, and the')
    A('### face`s section (I) was built from the components stage and omitted it. ### The corpus`s')
    A('### own cap, ### **`G-CAP`, IS `6` AND HOLDS**; the clause that fails is this seat`s own')
    A('### count.')
    A('### ### ### **THE LOCKED FACE IS NOT EDITED. ### BOTH NUMBERS ARE PRINTED.** ### `b389`s')
    A('### ### ### rule, applied to a figure this act disproved by continuing to work: ### **A')
    A('### ### ### FIGURE A LATER STEP DISPROVES IS PRINTED BESIDE THE FIGURE, NEVER OVER IT.**')
    A('### ### **AND THREE FILES THIS ACT WROTE ARE NOT NAMED IN THE FACE`S LIST EITHER:** ###')
    A('### `data/b399_lockgate_notes.txt` and `data/b399_lockgate.json`, written by the shared lock')
    A('### gate as it ran, and `data/b399_reg_satisfiable_stdout.txt`, a capture of a tool whose')
    A('### own emitted record `audit_b399_reg_satisfiable.txt` IS named. ### **NAMED HERE, NOT')
    A('### ### DELETED** -- a run artifact is evidence, and evidence is not removed to make a list')
    A('### ### come out right.')
    A('')
    A(SUB)
    A('### THE EXPECTATIONS, SCORED.')
    A(SUB)
    A('### ### **THE NAVIGATOR`S `(L4)`: *the sign chain flips it and `(M)` survives -- registered,')
    A('### ### and refutable by a printed value.***')
    A('###   ### **FIRST HALF: MET, AND FOR A SHARPER REASON THAN REGISTERED** -- the chain flips')
    A('###   it by the CLASS, not by a sign convention.')
    A('###   ### **SECOND HALF: MET AS A SIGN VERDICT AND REFUTED AS AN IDENTITY, BY EXACTLY THE')
    A('###   ### PRINTED VALUE THE ORDER INVITED** -- `-8.622324442` against `0.000000000`.')
    A('### ### **THIS SEAT`S, REGISTERED ON THE FACE:**')
    A('###   ### **(E1)** ### the sign test cannot refute `(M)` on this record, every in-class')
    A('###   prime sum being an empty sum. ### **MET.**')
    A('###   ### **(E2)** ### `(M)` fails under both sign conventions. ### **MET.**')
    A('###   ### **(E3)** ### Addition Three`s premise is not exactly true and the branch it')
    A('###   selects is the ROUTE. ### **MET.**')
    A('')
    A(SUB)
    A('### WHAT THIS ACT DOES NOT SAY.')
    A(SUB)
    A('### It does not say what the owed bridge needs instead of `(M)`.')
    A('### It does not prove `(M)` false by a general argument -- ### **IT EXHIBITS SEEDS, AND THE')
    A('### ### SEEDS ARE THREE, MEASURED, AND ON ONE FAMILY.**')
    A('### It does not lift the family obstruction, move `K5`s grade, close a coordinate, or move')
    A('### the clause.')
    A('### It does not make the vacuous sign test into evidence.')
    A('### ### **AND IT SAYS NOTHING ABOUT `h2` IN EITHER DIRECTION.**')
    A('')
    A(SUB)
    A('### THE DESK, THE ROW, THE KEY.')
    A(SUB)
    A('### **DESK ITEMS SWEPT `%d`; CLOSED `%d`; STANDING `%d`; LISTS CLOSED `%d`.**'
      % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
    A('### **CORRESPONDENCE ROW `%d`. ### INDEX KEY `the-sign-and-the-refutation` : %s.**'
      % (rownum, 'PASS' if kok else '### FAIL ###'))
    A('### **READS `%d`, ANCHORED `%d`. ### TOTAL CONTENT LOST ACROSS FOUR EDITED FILES `%d`.**'
      % (READS, ANCH, LOST))
    A('')
    A(BAR)
    A('### THE SCOPE SENTENCE.')
    A(BAR)
    A(SCOPE)
    A(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    rec('  written: %s (%d lines)' % (os.path.basename(BANKOUT), len(B)))
    return True


def main():
    bar('=')
    rec('b399 -- THE DESK, THE LEDGER WRITES, AND THE BANK.')
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
    else:
        rec('  ### the b398 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_sign_verdict': 'survives it, and vacuously' in low,
        'says_vacuous_reason': 'empty sum' in low,
        'says_class_flip': 'flips it by the class' in low,
        'says_refuted': '(m) is refuted' in low,
        'says_printed_value': '-8.622324442' in low.replace('−', '-'),
        'says_escapes_closed': 'not a convention artefact' in low,
        'says_grade': 'measured-at-covered-cells' in low,
        'says_margin_identity': 'minus the remainder integral' in low,
        'says_two_bounds': 'two bounds' in low,
        'says_family': 'not defined on the li family' in low,
        'says_not_named': 'this act does not name' in low,
        'says_sources_verified': 'verified before a word was read' in low,
        'says_routed': 'routed, not made' in low,
        'says_own_face_defect': 'six' in low and 'g-cap' in low,
        'says_lists_open': 'the four lists stay open by name' in low,
        'says_block_not_absence': 'a block on the work is not an absence of a trigger' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:** ### %s' % says)
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        return 1
    subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)

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
        run_clock.write(D, 'b399_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b399_desk_notes', LINES)
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
            run_clock.write(D, 'b399_desk_notes', LINES)
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
    bank(Q, rownum, kok)

    rec()
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### ROW %d. ### KEY %s. ### BANK WRITTEN.**'
        % (Q['items'], Q['closed'], rownum, 'PASS' if kok else 'FAIL'))
    bar('=')
    run_clock.write(D, 'b399_desk_notes', LINES)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
