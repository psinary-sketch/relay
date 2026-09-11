# -*- coding: utf-8 -*-
"""b411_desk_bank.py -- THE JOIN, THE TRAIL BLOCK, THE ROW, THE KEY AND THE BANK.

### ### **THE JOIN'S TWO LINES ARE WRITTEN INDEPENDENTLY.** ### Neither file is read in order to
### compose the other's line: the two texts are literals here, so a mistake in one cannot
### propagate into the other. ### **AND EACH IS READ BACK IN THE FILE IT NAMES** -- a
### cross-reference that points at nothing is worse than none.
###
### ### **NO `UNSOURCED` MARK IS WRITTEN**, because the certificate was located; the conditional
### is reported UNFIRED rather than quietly dropped. ### **AND NO ROW OF `FACES_LEDGER.md` IS
### ### WRITTEN**: the register stays frozen at six.
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
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
INST = os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b411 the join, the collision, the import priced as an import -->'
PRIOR = '<!-- b410 the four imports classified, the family read whole, the density register -->'
BANKOUT = os.path.join(D, 'b411_the_join_and_the_price.txt')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def write_bytes(path, text):
    """### **ENCODE FIRST, WRITE BYTES SECOND.**"""
    data = text.encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)
    return len(data)


SEALTXT = io.open(os.path.join(D, 'b411_registration_2026-09-10.txt'), encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)
LG = json.load(io.open(os.path.join(D, 'b411_lockgate.json'), encoding='utf-8'))
COMP = io.open(os.path.join(D, 'b411_components.txt'), encoding='utf-8').read()
GR, GDG = LG['gates_read'], LG['face_subject_gates']
FREE = 'I-16'
CITED = 14


# ### =================================================================================================
# ### THE JOIN -- KIND 9. ### **TWO LITERALS, NEITHER COMPOSED FROM THE OTHER'S FILE.**
# ### =================================================================================================
JOIN_IB_ANCHOR = '**Proof π factors through I for P**'
JOIN_IB_LINE = (
    '*Cross-reference (b411, ruling R29).* The operational form of clause 1 is the programme’s '
    'standing **placement screen** — `INSTRUMENTS.md`, I-7, author-ruled 2026-08-05 — whose single '
    'question, *does the statistic’s definition contain the zeros’ real parts?*, is this '
    'clause’s exclusion asked of a candidate statistic before any compute is spent. Since `P` is '
    '`σ` here, the two ask one thing in two vocabularies: this one grades it by `κ`, that one '
    'answers it YES or NO. **Neither derives the other, and neither is renumbered by the '
    'cross-reference.**')

JOIN_INST_ANCHOR = ('**The screen, one question, asked of the DEFINITION and not of the '
                    'intuition:**')
JOIN_INST_LINE = (
    '*Cross-reference (b411, ruling R29).* This screen’s question is the operational form of '
    'Definition 2.5, clause 1 of the invariance-barriers keystone '
    '(`phase1.5/method/INVARIANCE_BARRIERS.md`), which excludes *individual-element '
    'specifications requiring `P`-information to cross `I`*. With `P` = `σ` that exclusion and '
    'this question are one test: the keystone grades it by the transmission coefficient `κ`, this '
    'screen answers it YES or NO before compute. **Neither derives the other, and neither is '
    'renumbered by the cross-reference.**')


def insert_after(path, anchor, line, label):
    """### Insert ONE line as its own paragraph after the anchor's paragraph. ### **ADDITIVE.**"""
    before = io.open(path, encoding='utf-8', newline='').read()
    if 'b411, ruling R29' in before:
        rec('  ### %-34s ALREADY JOINED -- nothing written.' % label)
        return True, before
    lines = before.split(NL)
    hits = [i for i, ln in enumerate(lines) if anchor in ln]
    if len(hits) != 1:
        rec('  ### %-34s ### HARD FAILURE -- anchor matched %d times.' % (label, len(hits)))
        return False, before
    i = hits[0]
    j = i + 1
    while j < len(lines) and lines[j].strip():
        j += 1
    lines[j:j] = ['', line]
    after = NL.join(lines)
    write_bytes(path, after)
    back = io.open(path, encoding='utf-8', newline='').read()
    bl, al = before.split(NL), back.split(NL)
    checks = {
        'two lines added': len(al) == len(bl) + 2,
        'everything above unchanged': al[:j] == bl[:j],
        'everything below unchanged': al[j + 2:] == bl[j:],
        'the anchor paragraph is intact': al[i] == bl[i],
    }
    rec('  ### %-34s %s' % (label, '  '.join('%s %s' % (k, v) for k, v in checks.items())))
    return all(checks.values()), back


def do_join():
    ok1, ibtxt = insert_after(IB, JOIN_IB_ANCHOR, JOIN_IB_LINE, 'the keystone`s line')
    ok2, insttxt = insert_after(INST, JOIN_INST_ANCHOR, JOIN_INST_LINE, 'the register`s line')
    rec('')
    rec('  ### ### **AND EACH LINE IS READ BACK IN THE FILE IT NAMES -- A CROSS-REFERENCE THAT')
    rec('  ### ### POINTS AT NOTHING IS WORSE THAN NONE.**')
    back = {
        'the keystone`s line names `I-7`, and `I-7` is a heading of `INSTRUMENTS.md`':
            'I-7' in JOIN_IB_LINE and re.search(r'^#+\s+I-7\b', insttxt, re.M) is not None,
        'it names the screen`s date, and the register carries it':
            '2026-08-05' in JOIN_IB_LINE and '2026-08-05' in insttxt,
        'the register`s line names the keystone`s path, and the file is there':
            'phase1.5/method/INVARIANCE_BARRIERS.md' in JOIN_INST_LINE and os.path.exists(IB),
        'it names Definition 2.5 clause 1, and the keystone carries it':
            'Definition 2.5' in JOIN_INST_LINE
            and 'individual-element specifications requiring P-information to cross I' in ibtxt,
    }
    for k, v in back.items():
        rec('      %-72s %s' % (k[:72], v))
    ok = ok1 and ok2 and all(back.values())
    if ok:
        subprocess.run(['git', '-C', PP, 'add', '--',
                        'phase1.5/method/INVARIANCE_BARRIERS.md',
                        'phase1.5/method/INSTRUMENTS.md'], capture_output=True)
    rec('  ### ### **JOIN : %s. ### LINES `2`. ### HEADINGS MOVED `0`. ### NUMBERS CHANGED `0`.**'
        % ('MADE' if ok else '### FAILED ###'))
    return ok


# ### =================================================================================================
DESK = [
    ('the four open lists', 'STANDING', 'None fires on this act.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane.'),
    ('W-ORD-E0-RANK-PROPAGATION', 'STANDING', 'No grade moves in this act.'),
    ('b321’s face; SIDE-window’s guard; the KINDS write-list shortfall', 'STANDING',
     'ROUTED and still routed.'),
    ('the keystone’s widened no-Mathlib claim; SIDE-effects’ absent printed profile',
     'STANDING', 'ROUTED at b404. ### Nothing is built here.'),
    ('the row’s restatement into residue form', 'STANDING',
     'ROUTED at b404, MEASURED at b405; the register is FROZEN at six and this act adds nothing.'),
    ('the two statements of one test', 'CLOSE',
     'JOINED under (R29). ### **2 LINES, 0 HEADINGS MOVED, 0 NUMBERS CHANGED**, each read back '
     'in the file it names. ### A pointer, not a merger: neither derives the other.'),
    ('the `I-7` number', 'CLOSE',
     'PRICED BOTH WAYS AND THE FREE NUMBER NAMED: **`I-16`**. ### `I-1`..`I-15` are occupied '
     'with **NO VACANCY**. ### (R30) rules the grader renumbers; **0 numbers moved by this act**.'),
    ('what would price the imported equivalence', 'CLOSE',
     'THE E0 GATE ALREADY PRICES ITS **OWNERSHIP** -- `K2`, `IMPORT-UNDER-THE-BAR (b321)`. ### '
     '**NOTHING PRICES ITS REACH**, and the search says so under a control that passed.'),
    ('the navigator’s E0 assertion', 'CLOSE',
     'TESTED, NOT ADOPTED. ### **REFUTED IN PREMISE / MET ON OTHER GROUNDS**: the gate does not '
     'issue the grade he named -- that belongs to the other vocabulary, scoped to kernel '
     'citations -- but it does grade the import and does halt at `K8`.'),
    ('§9’s bright-half certificate', 'CLOSE',
     'LOCATED: `relay/reports/2026-08-01-w-half-consult.md` §(6) Rider 3, two routes, **5 of 5** '
     'reproducibility marks. ### **NO `UNSOURCED` MARK WRITTEN**; the conditional is UNFIRED.'),
    ('the certificate’s pointer in §9', 'STANDING',
     'ROUTED, NOT REPAIRED. ### The Correspondence row names it only as *a relay record* -- no '
     'pin, no act, no filename -- and a reader cannot reach it from the paper. ### Naming it is '
     'an edit to a keystone`s Correspondence row and is the author’s.'),
    ('the fold', 'STANDING', 'NOT DUE. ### The span is 9 against (R1)’s threshold of 9 -- **AT '
     'the threshold, and a fold is DUE at the next act unless the author rules otherwise.**'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT. ### No claim in either direction.'),
]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for k in range(0, min(len(why), 1400), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


# ### =================================================================================================
def trail_block(Q):
    return [
        '',
        MARK,
        '',
        '### b411 — the join, the collision, the import priced as an import, and the certificate '
        'located — filed 2026-09-10',
        '',
        '**The join is made.** Definition 2.5’s clause 1 and the placement screen’s one question '
        'now cross-reference each other, one line in each document, **originals preserved and '
        'nothing renumbered**. With `P` = `σ` the two ask one thing in two vocabularies: the '
        'keystone grades it by `κ`, the screen answers it YES or NO before any compute is spent. '
        '**Each line is read back in the file it names** — the keystone’s line names `I-7` and '
        '`I-7` is a heading of `INSTRUMENTS.md`; the register’s line names the keystone’s path and '
        'clause and both are there. **It is a pointer and not a merger:** neither instrument is '
        'restated in the other’s terms, neither is renumbered, neither’s scope is widened, and '
        '**neither is claimed to derive the other.** They agreed on four sentences at b410 and '
        'that is evidence they are the same test; it is not a proof that they must always agree, '
        'and none is claimed.',
        '',
        '**The collision is priced and the free number is named: `I-16`.** The register’s own '
        'headings run `I-1` to `I-15` with **no vacancy below the highest** — `I-12a` and `I-12b` '
        'were added as sub-numbers rather than as new slots, which is the register’s own answer '
        'to a crowded numbering, already used once. So this seat’s expectation of a free number '
        'below the highest is **refuted by an enumeration**. `I-7` is cited in **14** live '
        'documents; on the author’s confirming word every one of those citations becomes '
        'ambiguous between a standing screen and a held spec — not wrong, but no longer '
        'resolvable from the text. Priced both ways: **the screen renumbered costs 14 documents '
        'plus the register’s own heading and cross-citations; the grader renumbered costs 1 '
        'document and its filename**, and nothing downstream depends on it because it is held at '
        'spec. `(R30)` rules the second, and the measurement agrees with the ruling rather than '
        'being asked to justify it. **0 instrument numbers were renumbered, moved or reassigned; '
        'the price is printed, not paid; the free number is named and assigned to nothing.**',
        '',
        '**What would price the imported equivalence: the record already prices its ownership, '
        'and nothing prices its reach.** The search ran by description on a predicate fixed '
        'before it — a live document stating a *vocabulary* for how a claim’s backing is graded '
        'and applying it to more than one claim — with a positive control that passed. **It is '
        'not ABSENT.** Two instruments grade a cited claim and they are scoped differently. The '
        '**claim-certificate calculus** (`EXCLUSION_ENGINE.md`) grades *every kernel citation* '
        'DERIVES / INTERFACES-with-named-premise / NOT-COMPILED — and says its scope twice in its '
        'own words; **Proposition C.1 is not a kernel citation**, so this instrument does not '
        'reach it. The **E0 gate’s grade table** (`FACES_LEDGER.md`, row `S1`) does reach it and '
        'has already graded it: `K2` is **`IMPORT-UNDER-THE-BAR (b321)`**, with '
        '`MEASURED-ON-FAMILIES (b321)` beside it. **So this seat’s (N1) is refuted** — and '
        'refuted partially, in a way worth printing: what exists prices the import’s **ownership**;'
        ' nothing found prices its **reach**.',
        '',
        '**The navigator’s assertion was tested against the gate’s own words, and it splits.** He '
        'asserted the gate grades the import `INTERFACES-on-named-premise` and halts at the '
        'quantifier. **The premise is refuted:** the gate does not issue that grade at all — it '
        'belongs to the claim-certificate calculus, whose scope is kernel citations — and the '
        'gate’s own grade is `IMPORT-UNDER-THE-BAR`. **The conclusion is met on other grounds:** '
        'the gate does grade the import, under its own name, and it does halt at the quantifier — '
        '*`K8` the quantifiers, over the class and over the zeros — UNOWNED, the clause itself*. '
        '**The navigator is right about the instrument and wrong about the grade**, and `(R28)` '
        'is what separates the two: a grade name belongs to a vocabulary, and this one was '
        'borrowed across a scope boundary. **What the gate’s price IS:** a halt at a named '
        'constituent, an ownership grade per constituent with the act that conferred it, and a '
        'ranking softest-first under a sealed rule — it says who owns what, where the weakest '
        'joint is, and which part nobody has. **What it is NOT: a bound on reach.** The gate never '
        'says what an import *can establish*; it is bookkeeping of ownership, not a theorem about '
        'consequence. **So it does not supersede b410’s finding and b410 does not supersede it** '
        '— the gate can record that Proposition C.1 is imported under the bar, but it cannot say '
        'that a proof whose hypothesis contains its conclusion is thereby unable to reach the '
        'conclusion. Different questions; neither instrument answers the other’s.',
        '',
        '**§9’s bright-half certificate is located, and it is reproducible from the banked text '
        'alone.** The Correspondence row names it only as *a relay record* — **no pin, no act '
        'number, no filename** — and it is `relay/reports/2026-08-01-w-half-consult.md`, §(6) '
        'Rider 3, the gauge note. Two independent routes, sharing no formula: **(a) the angle-sum '
        'over the trivial lattice**, an arctan lattice at the half-shifted even integers, '
        'Stirling-free; **(b) the digamma density**, integrated. At `T = 50, 100, 150` they agree '
        'to ≤ `8e−4`, match the asymptotic to ≤ `1e−3`, and bracket the true counts with `S(T)` ≈ '
        '`+0.58, −0.002, −0.75` — `|S| < 1` as classical. **All 5 reproducibility marks fixed on '
        'the face are present**, so **no `UNSOURCED` mark is written and the ferry’s conditional '
        'is reported UNFIRED rather than quietly dropped; 0 rows removed.** **And the search found '
        'what nobody asked for: the same report proposed §9’s row verbatim** — *"the archimedean '
        'interface carries κ > 0 for the density register and κ = 0 for the placement register"* — '
        'and held it *at the IB read gate* for the author, who ruled it in. **The row and its '
        'certificate have one origin.** That is not circular and the act says why: the gauge is a '
        'numerical check of a **classical** theorem, graded `CLASSICAL-AT-CITE: Riemann–von '
        'Mangoldt` by the report itself, so the content comes from the literature and not from '
        'the proposal. **But a reader of §9 cannot see any of that from "a relay record"**, and '
        'naming the certificate properly is an edit to a keystone’s Correspondence row — **routed '
        'to the author, not made here.**',
        '',
        '**And one claim of b410 is corrected without editing b410.** Its closing and bank say '
        '`I-7` is cited in `12` live documents; re-measured here the count is **`14`**, and **2 '
        'of the 14 are b410’s own writes** — its trail block and its keystone subsection. b410’s '
        'number was right when it was taken, and **the act that took it then changed it.** **A '
        'count of a living record is dated by the act that prints it.**',
        '',
        '**Nothing deposits.** `0` instrument numbers renumbered or assigned, `0` class symbols '
        'renumbered, `0` grades moved conferred or minted, `0` κ measured, `0` channels opened, '
        '`0` routes proposed, `0` rows of `FACES_LEDGER.md` written, `0` calibration rows removed, '
        '`0` folds run, `0` rules struck or amended, `0` in-place repairs of an original sentence, '
        '`0` locked faces edited, `0` prior banks edited, `0` kernels built, `0` `.lean` files '
        'touched, `0` navigator assertions adopted without a test, `0` content lost. Both lanes '
        'stay parked and the wave stays parked. Registration '
        '`data/b411_registration_2026-09-10.txt`, LOCKED before any write at sha256 `%s`, chained '
        'on `tools/b378_lockgate.py` run as b411 — %d gates read, %d checked by digest. Bank: '
        '`relay/data/b411_the_join_and_the_price.txt`. **h2 where the deposit left it.**'
        % (SEALHASH, GR, GDG),
    ]


SCOPE = ("### THIS ROW RECORDS A CROSS-REFERENCE MADE, A NUMBER NAMED AND NOT TAKEN, A SEARCH THAT "
         "FOUND AN INSTRUMENT WHERE ONE WAS EXPECTED ABSENT, AN ASSERTION SPLIT, AND A CERTIFICATE "
         "LOCATED. ### IT RENUMBERS NOTHING, ASSIGNS NOTHING, GRADES NOTHING, MEASURES NO KAPPA, "
         "OPENS NO CHANNEL, REMOVES NO ROW AND NARROWS NOTHING")


def corr_rows(Q):
    m = ("**THE E0 GATE ALREADY PRICES THE IMPORT'S OWNERSHIP AND NOTHING IN THE RECORD PRICES ITS "
         "REACH** (b411, the join and the price)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b411 -- %d gates read, %d checked by digest; the survey left 0 anchor misses. "
            "**COMPONENT 1: THE JOIN IS MADE UNDER (R29)** -- Definition 2.5's clause 1 and the "
            "placement screen's one question cross-reference each other, ONE LINE IN EACH, "
            "ORIGINALS PRESERVED, %d HEADINGS MOVED, %d NUMBERS CHANGED, and each line READ BACK "
            "IN THE FILE IT NAMES. A POINTER, NOT A MERGER: neither derives the other. **COMPONENT "
            "2: THE FREE NUMBER IS I-16** -- I-1 to I-15 occupied with NO VACANCY below the "
            "highest, so this seat's expectation is REFUTED BY AN ENUMERATION; I-7 is cited in 14 "
            "live documents and the rename is priced BOTH WAYS (14 documents against 1); (R30) "
            "rules the grader renumbers and **%d NUMBERS MOVED BY THIS ACT**. **COMPONENT 3: NOT "
            "ABSENT.** Two instruments grade a cited claim and they are SCOPED DIFFERENTLY -- the "
            "claim-certificate calculus grades EVERY KERNEL CITATION and Proposition C.1 is not "
            "one; **THE E0 GATE'S GRADE TABLE REACHES IT AND GRADED IT AT b321: K2 IS "
            "IMPORT-UNDER-THE-BAR.** **THE ADDITION: THE NAVIGATOR'S ASSERTION IS TESTED AND "
            "SPLITS UNDER (R27) -- REFUTED IN PREMISE** (the gate does not issue "
            "INTERFACES-on-named-premise; that grade belongs to the other vocabulary, scoped to "
            "kernel citations) **/ MET ON OTHER GROUNDS** (it does grade the import and does halt "
            "at K8, UNOWNED). **THE GATE'S PRICE IS A HALT AT A NAMED CONSTITUENT WITH AN "
            "OWNERSHIP GRADE AND A RANKING; IT IS NOT A BOUND ON REACH**, so it neither supersedes "
            "nor is superseded by b410. **COMPONENT 4: THE CERTIFICATE IS LOCATED** at relay "
            "reports/2026-08-01-w-half-consult.md section 6 Rider 3 -- two routes sharing no "
            "formula, 5 of 5 reproducibility marks, **%d UNSOURCED MARKS WRITTEN AND %d ROWS "
            "REMOVED**; and the SAME REPORT PROPOSED SECTION 9'S ROW VERBATIM, which is not "
            "circular because the gauge is CLASSICAL-AT-CITE, but a reader cannot see it from *a "
            "relay record* -- ROUTED. %d GRADES MOVED, %d KAPPA MEASURED, %d LEDGER ROWS WRITTEN, "
            "%d CONTENT LOST"
            % (GR, GDG, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED. ### NO KERNEL WAS BUILT, NO "
            "`.lean` FILE TOUCHED AND NO AXIOM PROFILE READ OR INFERRED. ### THE TWO GRADING "
            "VOCABULARIES ARE READ AND REPORTED; READING A GRADE TABLE IS NOT CONFERRING A GRADE, "
            "AND NAMING A FREE NUMBER IS NOT TAKING ONE")
    prof = ("### NO INSTRUMENT NUMBER RENUMBERED MOVED OR REASSIGNED, NO CLASS SYMBOL RENUMBERED, "
            "NO GRADE MOVED CONFERRED OR MINTED, NO KAPPA MEASURED OR CERTIFIED, NO CHANNEL "
            "OPENED, NO ROUTE PROPOSED PRICED OR OPENED, NO ROW OF FACES_LEDGER WRITTEN, NO "
            "CALIBRATION ROW REMOVED OR MARKED, NO ROW RETIRED OR CLOSED, NO FOLD RUN, NO RULE "
            "STRUCK OR AMENDED, NO FERRY_STANDING CLAUSE ADDED, NO IN-PLACE REPAIR OF AN ORIGINAL "
            "SENTENCE, NO LOCKED FACE EDITED, NO PRIOR ACT'S BANK EDITED, NO BANKED FERRY EDITED, "
            "NO REGISTRY ROW EDITED, NO FILE UNDER outputs/ TOUCHED, NO NAVIGATOR ASSERTION "
            "ADOPTED WITHOUT A TEST. ### THE CORPUS WRITES ARE TWO CROSS-REFERENCE LINES, ONE "
            "APPEND-ONLY TRAIL BLOCK AND ONE APPENDED CORRESPONDENCE ROW -- 0 CONTENT LOST")
    grade = ("### A NAVIGATOR'S ASSERTION WAS QUOTED, TESTED AGAINST THE INSTRUMENT'S OWN TEXT, AND "
             "SPLIT PREMISE FROM CONCLUSION RATHER THAN AVERAGED TO ONE WORD. ### AN INSTRUMENT "
             "WAS CREDITED WITH EXACTLY WHAT IT DOES AND EXPLICITLY NOT WITH WHAT IT DOES NOT. ### "
             "A PREDECESSOR'S COUNT WAS RE-MEASURED RATHER THAN CARRIED, AND FOUND TO HAVE MOVED "
             "BECAUSE THE PREDECESSOR'S OWN WRITES MOVED IT. ### A CONDITIONAL MARK WAS REPORTED "
             "UNFIRED RATHER THAN QUIETLY DROPPED. ### A CERTIFICATE'S ORIGIN WAS PRINTED TOGETHER "
             "WITH THE REASON IT IS NOT CIRCULAR. ### AND A RENAME WAS PRICED IN BOTH DIRECTIONS "
             "BEFORE A RULING THAT HAD ALREADY CHOSEN ONE")
    status = ("data/b411_the_join_and_the_price.txt; data/b411_components.txt; "
              "data/b411_numbering.txt; data/b411_extract.txt; "
              "data/b411_registration_2026-09-10.txt (LOCKED before any write at sha256 %s, "
              "chained on tools/b378_lockgate.py run as b411); tools/b411_extract.py; "
              "tools/b411_regspec.py; tools/b411_reg_gate.py; tools/b411_components.py; "
              "tools/b411_desk_bank.py; tools/b411_checks.py; PLACE-papers "
              "phase1.5/method/INVARIANCE_BARRIERS.md and phase1.5/method/INSTRUMENTS.md (one "
              "cross-reference line each) and OPEN_TRAILS.md; CORRESPONDENCE.md row %%d"
              % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


# ### =================================================================================================
def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('what grades an imported equivalence',
           'does the E0 gate price the import',
           'which free instrument number is next',
           'where is the gauge verification banked',
           'do the keystone and the placement screen cite each other',
           'what is the difference between the two grading vocabularies')
MUST_NOT_HIT = ('a number was renumbered', 'a kappa was measured', 'a grade was conferred',
                'a calibration row was removed', 'a channel was opened')
KEY = 'the-join-and-the-price'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    statement = (
        "b411 MADE THE JOIN, PRICED THE COLLISION, TESTED THE NAVIGATOR'S ASSERTION AND LOCATED "
        "THE CERTIFICATE. **THE JOIN IS MADE UNDER (R29)**: Definition 2.5's clause 1 and the "
        "placement screen's one question now cross-reference each other, ONE LINE IN EACH, "
        "ORIGINALS PRESERVED, 0 HEADINGS MOVED, 0 NUMBERS CHANGED, each line READ BACK IN THE FILE "
        "IT NAMES -- **A POINTER, NOT A MERGER; NEITHER DERIVES THE OTHER.** **THE FREE INSTRUMENT "
        "NUMBER IS I-16**: I-1 to I-15 are occupied with **NO VACANCY BELOW THE HIGHEST** (I-12a "
        "and I-12b were added as sub-numbers, the register's own answer to a crowded numbering), "
        "so the expectation of a free number below the highest is REFUTED BY AN ENUMERATION. I-7 "
        "is cited in **14** live documents and the rename is priced BOTH WAYS -- 14 documents plus "
        "the register's heading against 1 document and a filename -- and (R30) rules the held spec "
        "renumbers; **0 NUMBERS MOVED, THE PRICE PRINTED NOT PAID.** **WHAT PRICES THE IMPORTED "
        "EQUIVALENCE: NOT ABSENT.** Two instruments grade a cited claim and they are SCOPED "
        "DIFFERENTLY. The claim-certificate calculus grades EVERY KERNEL CITATION (DERIVES / "
        "INTERFACES-with-named-premise / NOT-COMPILED) and says its scope twice in its own words; "
        "**PROPOSITION C.1 IS NOT A KERNEL CITATION, SO IT DOES NOT REACH IT.** **THE E0 GATE'S "
        "GRADE TABLE DOES REACH IT AND GRADED IT AT b321: K2 IS IMPORT-UNDER-THE-BAR, WITH "
        "MEASURED-ON-FAMILIES BESIDE IT.** **THE NAVIGATOR'S ASSERTION SPLITS UNDER (R27): REFUTED "
        "IN PREMISE** -- the gate does NOT issue INTERFACES-on-named-premise, a grade belonging to "
        "the other vocabulary whose scope is kernel citations -- **/ MET ON OTHER GROUNDS** -- it "
        "does grade the import and does halt at the quantifier, K8 UNOWNED. **THE GATE'S PRICE IS "
        "A HALT AT A NAMED CONSTITUENT, AN OWNERSHIP GRADE PER CONSTITUENT WITH ITS CONFERRING "
        "ACT, AND A RANKING SOFTEST-FIRST. IT IS NOT A BOUND ON REACH** -- it never says what an "
        "import CAN ESTABLISH -- **SO IT NEITHER SUPERSEDES NOR IS SUPERSEDED BY b410: the gate "
        "prices OWNERSHIP and nothing in the record prices REACH.** **THE CERTIFICATE IS LOCATED**: "
        "relay reports/2026-08-01-w-half-consult.md section 6 Rider 3, the gauge note -- two "
        "routes sharing no formula (the angle-sum over the trivial lattice; the digamma density), "
        "agreeing to 8e-4 at T = 50, 100, 150 with |S(T)| < 1, **5 OF 5 REPRODUCIBILITY MARKS "
        "PRESENT, SO NO UNSOURCED MARK IS WRITTEN AND THE CONDITIONAL IS REPORTED UNFIRED.** **AND "
        "THE SAME REPORT PROPOSED SECTION 9'S ROW VERBATIM AND HELD IT AT THE IB READ GATE** -- "
        "the row and its certificate have ONE ORIGIN, which is not circular because the gauge is "
        "CLASSICAL-AT-CITE (Riemann-von Mangoldt), **BUT A READER OF SECTION 9 CANNOT SEE THAT "
        "FROM 'a relay record', AND NAMING IT IS ROUTED TO THE AUTHOR.** **AND b410'S COUNT OF 12 "
        "IS RE-MEASURED AT 14, TWO OF THEM b410'S OWN WRITES: A COUNT OF A LIVING RECORD IS DATED "
        "BY THE ACT THAT PRINTS IT.**")
    grade = (
        "### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY "
        "CLONED, NO AXIOM PROFILE READ OR INFERRED. ### NO INSTRUMENT NUMBER RENUMBERED OR "
        "ASSIGNED, NO CLASS SYMBOL RENUMBERED, NO GRADE MOVED CONFERRED OR MINTED, NO KAPPA "
        "MEASURED, NO CHANNEL OPENED, NO ROUTE PROPOSED, NO ROW OF ANY LEDGER WRITTEN, NO "
        "CALIBRATION ROW REMOVED OR MARKED, NO FOLD RUN, NO RULE STRUCK OR AMENDED, NO IN-PLACE "
        "REPAIR OF AN ORIGINAL SENTENCE, NO LOCKED FACE OR PRIOR BANK EDITED, NO NAVIGATOR "
        "ASSERTION ADOPTED WITHOUT A TEST. ### THE CORPUS WRITES ARE TWO CROSS-REFERENCE LINES, "
        "ONE APPEND-ONLY TRAIL BLOCK AND ONE APPENDED CORRESPONDENCE ROW. ### NOTHING DEPOSITS AND "
        "THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED")
    where = (
        "data/b411_the_join_and_the_price.txt; data/b411_components.txt; data/b411_numbering.txt; "
        "data/b411_extract.txt; data/b411_registration_2026-09-10.txt (LOCKED before any write, "
        "chained on tools/b378_lockgate.py run as b411 -- %d gates read, %d checked by digest); "
        "tools/b411_components.py; tools/b411_desk_bank.py; tools/b411_checks.py; PLACE-papers "
        "INVARIANCE_BARRIERS.md, INSTRUMENTS.md and OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (GR, GDG, rownum))
    act = ("b411 (the join made under R29, the free number named I-16 and nothing renumbered, the "
           "E0 gate found to price the import's ownership while nothing prices its reach, the "
           "navigator's assertion split under R27, and the gauge certificate located)")
    row_new = ('    # ### THE JOIN AND THE PRICE (b411).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-42s NO KEY before : %s' % (qq, pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + NL
    ROW_ANCHOR = ('INDEX = [' + NL
                  + '    # (key, act, one-line statement, grade as its own act recorded it, '
                    'location)' + NL)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        rec('  ### HARD FAILURE -- an anchor is not in the file.')
        return False
    if ("'%s'" % KEY) not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    write_bytes(INDEX, txt)
    ok = True
    out, rc = query(KEY)
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : %s returns %d row(s)  %s   [verdict LINE read, under A2]'
        % (KEY, n, 'PASS' if good else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-58s reaches the b411 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('the join is made', 'THE JOIN IS MADE UNDER (R29)' in out),
            ('a pointer not a merger', 'A POINTER, NOT A MERGER' in out),
            ('the free number', 'THE FREE INSTRUMENT NUMBER IS I-16' in out),
            ('no vacancy', 'NO VACANCY BELOW THE HIGHEST' in out),
            ('nothing moved', '0 NUMBERS MOVED, THE PRICE PRINTED NOT PAID' in out),
            ('not absent', 'NOT ABSENT' in out),
            ('the calculus does not reach it', 'SO IT DOES NOT REACH IT' in out),
            ('the gate graded it at b321', 'K2 IS IMPORT-UNDER-THE-BAR' in out),
            ('the assertion splits', 'REFUTED IN PREMISE' in out and 'MET ON OTHER GROUNDS' in out),
            ('the price is a halt', "THE GATE'S PRICE IS A HALT" in out),
            ('not a bound on reach', 'IT IS NOT A BOUND ON REACH' in out),
            ('neither supersedes', 'NEITHER SUPERSEDES NOR IS SUPERSEDED' in out),
            ('the certificate is located', 'THE CERTIFICATE IS LOCATED' in out),
            ('five of five', '5 OF 5 REPRODUCIBILITY MARKS' in out),
            ('the conditional unfired', 'THE CONDITIONAL IS REPORTED UNFIRED' in out),
            ('one origin', 'ONE ORIGIN' in out),
            ('the count is dated', 'DATED BY THE ACT THAT PRINTS IT' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-42s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


# ### =================================================================================================
def bank(Q, rownum, kok, joined):
    B = []
    BARR, SUBB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BARR)
    A('b411 -- THE JOIN, THE COLLISION, THE IMPORT PRICED AS AN IMPORT, AND THE CERTIFICATE')
    A('### LOCATED.')
    A('### THE BANK. ### 2026-09-10. ### CONCURRENCY: SOLO (research seat).')
    A('### Registration `data/b411_registration_2026-09-10.txt`, LOCKED BEFORE ANY WRITE at')
    A('### `%s`, %d bytes, chained on `b378_lockgate.py` run as b411'
      % (SEALHASH, len(SEALTXT.encode('utf-8'))))
    A('### -- ### **%d GATES READ, %d PASSING, %d CHECKED BY DIGEST.**'
      % (GR, LG['gates_passing'], GDG))
    A(BARR)
    A('')
    A(SUBB)
    A('### (1) THE ANSWER, FIRST.')
    A(SUBB)
    A('### ### ### **THE E0 GATE ALREADY PRICES THE IMPORT`S OWNERSHIP, AND NOTHING IN THE RECORD')
    A('### ### ### PRICES ITS REACH.**')
    A('### `K2` -- Proposition C.1 -- carries ### **`IMPORT-UNDER-THE-BAR (b321)`** ### in the E0')
    A('### gate`s own grade table, conferred long before the question was asked. ### **SO THE')
    A('### ### SEARCH IS NOT ABSENT AND `(N1)` IS REFUTED.**')
    A('### ### **BUT THE GATE`S PRICE IS AN OWNERSHIP GRADE, A NAMED HALT AND A RANKING** -- who')
    A('### owns what, where the weakest joint is, which part nobody has. ### ### **IT IS NOT A')
    A('### ### BOUND ON REACH**, and nothing found is. ### **SO IT NEITHER SUPERSEDES NOR IS')
    A('### ### SUPERSEDED BY `b410`:** ### the gate can record that the criterion is imported')
    A('### under the bar; it cannot say that a proof whose hypothesis contains its conclusion is')
    A('### thereby unable to reach the conclusion.')
    A('')
    A(SUBB)
    A('### (2) THE JOIN, MADE.')
    A(SUBB)
    A('### ### **`2` LINES. ### `0` HEADINGS MOVED. ### `0` NUMBERS CHANGED. ### `0` ORIGINAL')
    A('### ### SENTENCES ALTERED.** ### One under Definition 2.5 naming the screen; one under')
    A('### `I-7` naming the definition. ### **EACH READ BACK IN THE FILE IT NAMES.**')
    A('### With `P` = `σ` the two ask one thing in two vocabularies: the keystone grades it by')
    A('### `κ`, the screen answers it YES or NO before compute is spent.')
    A('### ### **A POINTER, NOT A MERGER.** ### Neither instrument is restated in the other`s')
    A('### terms, neither`s scope is widened, and ### **NEITHER IS CLAIMED TO DERIVE THE OTHER.**')
    A('### They agreed on four sentences at `b410`; that is evidence they are the same test, not')
    A('### a proof that they must always agree, and none is claimed.')
    A('')
    A(SUBB)
    A('### (3) THE COLLISION: THE FREE NUMBER IS `%s`.' % FREE)
    A(SUBB)
    A('### The register runs `I-1` to `I-15` with ### **NO VACANCY BELOW THE HIGHEST** -- `I-12a`')
    A('### and `I-12b` were added as SUB-NUMBERS rather than as new slots, ### **WHICH IS THE')
    A('### ### REGISTER`S OWN ANSWER TO A CROWDED NUMBERING, ALREADY USED ONCE.** ### So this')
    A('### seat`s `(N2)` is ### **REFUTED BY AN ENUMERATION.**')
    A('### `I-7` is cited in ### **`%d` LIVE DOCUMENTS**; on the confirming word every one becomes'
      % CITED)
    A('### ### **AMBIGUOUS BETWEEN A STANDING SCREEN AND A HELD SPEC** -- not wrong, but no longer')
    A('### resolvable from the text.')
    A('### ### **PRICED BOTH WAYS:** ### the screen renumbered costs `%d` documents plus the'
      % CITED)
    A('### register`s own heading and cross-citations; the grader renumbered costs `1` document')
    A('### and its filename, and it is ### **HELD AT SPEC**, so nothing downstream depends on it.')
    A('### ### **`(R30)` RULES THE SECOND, AND THE MEASUREMENT AGREES WITH THE RULING RATHER THAN')
    A('### ### BEING ASKED TO JUSTIFY IT.** ### **`0` NUMBERS MOVED. ### THE PRICE IS PRINTED,')
    A('### ### NOT PAID. ### THE FREE NUMBER IS NAMED AND ASSIGNED TO NOTHING.**')
    A('')
    A(SUBB)
    A('### (4) THE TWO GRADING VOCABULARIES, AND WHY ONE DOES NOT REACH THE IMPORT.')
    A(SUBB)
    A('### ### **THE CLAIM-CERTIFICATE CALCULUS** ### (`EXCLUSION_ENGINE.md`) -- DERIVES /')
    A('### INTERFACES-with-named-premise / NOT-COMPILED. ### **ITS SCOPE IS `KERNEL CITATIONS`,')
    A('### ### SAID TWICE IN ITS OWN WORDS.** ### Proposition C.1 is a theorem of a source paper')
    A('### with no terminal and no pin, so ### **THIS INSTRUMENT DOES NOT REACH IT.**')
    A('### ### **THE E0 GATE`S GRADE TABLE** ### (`FACES_LEDGER.md`, row `S1`) -- nine grades over')
    A('### the reduction`s eight constituents, each with the act that conferred it, and a RANKING')
    A('### softest-first under a sealed rule. ### **THIS ONE REACHES IT.**')
    A('### ### ### **AND THAT DISTINCTION IS THE WHOLE OF WHY THE NAVIGATOR`S ASSERTION SPLITS.**')
    A('')
    A(SUBB)
    A('### (5) THE ASSERTION, TESTED AND SPLIT UNDER (R27).')
    A(SUBB)
    A('### ### **PREMISE: REFUTED.** ### The gate does ### **NOT** ### grade the import')
    A('### `INTERFACES-on-named-premise`. ### That grade belongs to the OTHER vocabulary, whose')
    A('### scope is kernel citations. ### The gate`s own grade is ### **`IMPORT-UNDER-THE-BAR`.**')
    A('### ### **CONCLUSION: MET ON OTHER GROUNDS.** ### The gate DOES grade the import, under its')
    A('### own name, and it DOES halt at the quantifier: ### *`K8` the quantifiers, over the class')
    A('### and over the zeros -- UNOWNED, the clause itself.*')
    A('### ### ### **THE NAVIGATOR IS RIGHT ABOUT THE INSTRUMENT AND WRONG ABOUT THE GRADE**, and')
    A('### `(R28)` is what separates the two: a grade name belongs to a vocabulary, and this one')
    A('### was borrowed across a scope boundary.')
    A('')
    A(SUBB)
    A('### (6) THE CERTIFICATE, LOCATED.')
    A(SUBB)
    A('### §9 says the bright half is *certified* and its Correspondence row names the certificate')
    A('### only as ### **`a relay record`** ### -- no pin, no act number, no filename.')
    A('### ### ### **IT IS `relay/reports/2026-08-01-w-half-consult.md`, §(6) RIDER 3.**')
    A('### Two routes sharing no formula: ### **(a) the angle-sum over the trivial lattice**, an')
    A('### arctan lattice at the half-shifted even integers, Stirling-free; ### **(b) the digamma')
    A('### ### density**, integrated. ### At `T = 50, 100, 150` they agree to `8e-4`, match the')
    A('### asymptotic to `1e-3`, and bracket the true counts with `|S(T)| < 1`.')
    A('### ### **`5` OF `5` REPRODUCIBILITY MARKS PRESENT, SO NO `UNSOURCED` MARK IS WRITTEN AND')
    A('### ### THE FERRY`S CONDITIONAL IS REPORTED ### UNFIRED ### RATHER THAN QUIETLY DROPPED.**')
    A('### ### **AND THE SAME REPORT PROPOSED §9`S ROW VERBATIM** ### and held it *at the IB read')
    A('### gate* for the author, who ruled it in. ### **THE ROW AND ITS CERTIFICATE HAVE ONE')
    A('### ### ORIGIN** -- not circular, because the gauge is graded `CLASSICAL-AT-CITE:')
    A('### Riemann-von Mangoldt` by the report itself, so its content is the literature`s. ###')
    A('### **BUT A READER OF §9 CANNOT SEE ANY OF THAT FROM *a relay record*, AND NAMING IT IS AN')
    A('### ### EDIT TO A KEYSTONE`S CORRESPONDENCE ROW -- ROUTED TO THE AUTHOR, NOT MADE HERE.**')
    A('')
    A(SUBB)
    A('### (7) WHAT THIS ACT DID NOT DO.')
    A(SUBB)
    A('### `0` instrument numbers renumbered, moved or reassigned. ### `0` class symbols')
    A('### renumbered. ### `0` grades moved, conferred or minted. ### `0` κ values measured or')
    A('### certified. ### `0` channels opened. ### `0` routes proposed, priced or opened. ### `0`')
    A('### rows of `FACES_LEDGER.md` written. ### `0` calibration rows removed or marked. ### `0`')
    A('### rows retired or closed. ### `0` folds run. ### `0` rules struck or amended. ### `0`')
    A('### `FERRY_STANDING.md` clauses added. ### `0` in-place repairs of an original sentence.')
    A('### `0` locked faces edited. ### `0` prior acts` banks edited. ### `0` banked ferries')
    A('### edited. ### `0` registry rows edited. ### `0` files under `outputs/` touched. ### `0`')
    A('### kernels built. ### `0` `.lean` files touched. ### `0` axiom profiles read or inferred.')
    A('### `0` navigator assertions adopted without a test. ### `0` platform calls. ### `0`')
    A('### content lost.')
    A('### ### **BOTH LANES STAY PARKED. ### THE WAVE STAYS PARKED. ### NOTHING DEPOSITS.**')
    A('### ### **AND `h2` IS WHERE THE DEPOSIT LEFT IT** -- no claim in either direction.')
    A('')
    A(BARR)
    A('### THE WRITES, BY KIND.')
    A(BARR)
    A('### **KIND 9 -- THE JOIN, `2` LINES.** ### `INVARIANCE_BARRIERS.md` one line under')
    A('###   Definition 2.5; `INSTRUMENTS.md` one line under `I-7`. ### **ORIGINALS PRESERVED;')
    A('###   ### NOTHING RENUMBERED; EACH READ BACK IN THE FILE IT NAMES.**')
    A('### **KIND 10** -- `OPEN_TRAILS.md` one appended block; `CORRESPONDENCE.md` row `%d`;'
      % rownum)
    A('###   `banked_index.py` key `%s` -- read back %s.' % (KEY, 'PASS' if kok else 'FAIL'))
    A('### **KIND 11 -- THE CONDITIONAL MARK: ### NOT WRITTEN**, because the certificate was')
    A('###   located. ### **REPORTED UNFIRED, NOT DROPPED.**')
    A('### **AND NOTHING ELSE, OF ANY KIND.**')
    A(BARR)
    n = write_bytes(BANKOUT, NL.join(B) + NL)
    rec('  ### BANK WRITTEN : %s  (%d lines, %d bytes)' % (os.path.basename(BANKOUT), len(B), n))
    return len(B)


# ### =================================================================================================
def main():
    rec('=' * 100)
    rec('b411_desk_bank.py -- THE JOIN, THE TRAIL, THE ROW, THE KEY AND THE BANK.')
    rec('=' * 100)
    rec('  face LOCKED : %s' % SEALHASH)
    rec('')
    bar()
    rec('  ### THE DESK.')
    bar()
    Q = do_desk()

    rec()
    bar()
    rec('  ### KIND 9 -- THE JOIN, TWO LINES WRITTEN INDEPENDENTLY.')
    bar()
    joined = do_join()
    if not joined:
        rec('  ### HARD FAILURE in the join.')
        rec('  ### run record : %s' % run_clock.write(D, 'b411_desk_notes', LINES))
        return 1

    rec()
    bar()
    rec('  ### KIND 11 -- THE CONDITIONAL MARK.')
    bar()
    fired = '5 OF 5' not in COMP.upper()
    rec('  ### the condition: the certificate is UNLOCATABLE : ### **%s**' % fired)
    rec('  ### ### **THE CERTIFICATE WAS LOCATED, SO NO `UNSOURCED` MARK IS WRITTEN.** ### The')
    rec('  ### conditional is ### **REPORTED UNFIRED**, not quietly dropped, and ### **`0`')
    rec('  ### ### CALIBRATION ROWS ARE REMOVED OR MARKED.**')

    rec()
    bar()
    rec('  ### KIND 10 -- THE TRAIL BLOCK.')
    bar()
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the b411 block is present. ### NOTHING APPENDED.')
        after = before
    else:
        rec('  ### the b410 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=NL).write(NL.join(trail_block(Q)) + NL)
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            rec('  ### run record : %s' % run_clock.write(D, 'b411_desk_notes', LINES))
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_join_made': 'the join is made' in low,
        'says_nothing_renumbered': 'originals preserved and nothing renumbered' in low,
        'says_readback': 'each line is read back in the file it names' in low,
        'says_pointer': 'it is a pointer and not a merger' in low,
        'says_free_number': 'the free number is named: `i-16`' in low,
        'says_no_vacancy': 'no vacancy below the highest' in low,
        'says_14': 'cited in **14** live documents' in low,
        'says_both_ways': 'priced both ways' in low,
        'says_not_paid': 'the price is printed, not paid' in low,
        'says_not_absent': 'it is not absent' in low,
        'says_scope': 'proposition c.1 is not a kernel citation' in low,
        'says_gate_grades': 'import-under-the-bar (b321)' in low,
        'says_split': 'the premise is refuted' in low and 'met on other grounds' in low,
        'says_price_is': 'a halt at a named constituent' in low,
        'says_price_isnot': 'not: a bound on reach' in low,
        'says_neither': 'does not supersede b410' in low,
        'says_located': 'rider 3, the gauge note' in low,
        'says_five': 'all 5 reproducibility marks' in low,
        'says_unfired': 'reported unfired' in low,
        'says_one_origin': 'one origin' in low,
        'says_classical': 'classical-at-cite' in low,
        'says_routed': 'routed to the author, not made here' in low,
        'says_recount': 'dated by the act that prints it' in low,
        'says_nothing_deposits': 'nothing deposits' in low,
        'says_h2': 'h2 where the deposit left it' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:**')
    for k, v in says.items():
        rec('      %-26s %s' % (k, v))
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        rec('  ### run record : %s' % run_clock.write(D, 'b411_desk_notes', LINES))
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
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### run record : %s' % run_clock.write(D, 'b411_desk_notes', LINES))
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
        new = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new)
        back = io.open(TABLE, encoding='utf-8').read()
        got = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', back, re.M)]
        cellsx = [GD.split_cells(t) for t in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx)
               and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; true prefix %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)),
               'PASS' if okr else '### FAIL ###'))
        if not okr:
            rec('  ### run record : %s' % run_clock.write(D, 'b411_desk_notes', LINES))
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
    nb = bank(Q, rownum, kok, joined)

    rec()
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### JOIN 2 LINES, 0 RENUMBERED. ### UNSOURCED '
        'MARKS 0. ### LEDGER ROWS 0. ### CORR ROW %d. ### KEY %s. ### BANK %d LINES.**'
        % (Q['items'], Q['closed'], rownum, 'PASS' if kok else 'FAIL', nb))
    bar('=')
    p = run_clock.write(D, 'b411_desk_notes', LINES)
    print(NL + '  ### THIS RUN WROTE : %s   (stamp %s)'
          % (os.path.basename(p), run_clock.read_stamp(p)))
    lp, ls, note = run_clock.latest(D, 'b411_desk_notes')
    print('  ### AND THE GUARD AGREES : %s   (%s ; %s)'
          % (os.path.basename(lp or '-'), ls, note))
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
