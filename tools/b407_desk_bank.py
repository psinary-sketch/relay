# -*- coding: utf-8 -*-
"""b407_desk_bank.py -- THE DESK, THE TRAIL BLOCK, THE ROW, THE KEY AND THE BANK.

### ### **THIS ACT MAKES NO IN-PLACE REPAIR AND WRITES NO ROW OF `FACES_LEDGER.md`.** ### The
### verdict on the halt is `NOT AN INSTANCE`, and the face fixed before the read that nothing is
### filed to the row on any other verdict. ### **A RESEMBLANCE IS NOT AN INSTANCE, AND AN ACT THAT
### ### FILED ONE WOULD HAVE TYPED THE BRIDGE THE ROW EXISTS TO REFUSE.**
###
### ### **AND EVERY RUN RECORD THIS FILE WRITES IS READ BACK BY ITS OWN RETURNED PATH**, never by a
### directory listing -- the guard `b407` adds to `run_clock` exists because `b406` did the other
### thing three times.
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
MARK = '<!-- b407 the barrier own instance, and the repair priced where it is thin -->'
PRIOR = '<!-- b406 the sites without an existential, and the finite side qualifier swept -->'
BANKOUT = os.path.join(D, 'b407_the_barriers_own_instance.txt')

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


SEALTXT = io.open(os.path.join(D, 'b407_registration_2026-09-10.txt'), encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)
LG = json.load(io.open(os.path.join(D, 'b407_lockgate.json'), encoding='utf-8'))
COMP = io.open(os.path.join(D, 'b407_components.txt'), encoding='utf-8').read()

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
     'ROUTED at b404, MEASURED at b405, and still not applied.'),
    ('the shape-to-instance route', 'STANDING',
     'PRICED at b405. ### b407 adds one printed reason it stays untaken: the reduction is not the '
     'kind of object the theorem quantifies over.'),
    ('the second standing sentence -- every write encodes before it opens', 'STANDING',
     'ROUTED at b406 to the author. ### b407 carries it and does not promote it.'),
    ('whether the row could cite ONE theorem instead of describing six sites', 'CLOSE',
     'ANSWERED: ### **NO, NOT YET.** ### The halt at K8 is NOT AN INSTANCE of Theorem 3.1 -- the '
     'failing hypothesis is the one about pi. ### The resemblance is exact and is printed beside '
     'the verdict; nothing is filed to the row.'),
    ('whether any of the six names an interface in the lemma’s sense', 'CLOSE',
     'ANSWERED: 0 of 6 on Definition 2.2’s test, 4 of 6 on the loose split test. ### Both '
     'counts printed; the strict one governs; kappa is decided nowhere.'),
    ('b406’s escape-kind price of 5 of 6', 'CLOSE',
     'CORRECTED TO 4. ### (i) moved to NOT FILLABLE because the record’s own list puts RH on '
     'BOTH sides of the escape-kind dichotomy. ### A price is not protected by having been this '
     'seat’s.'),
    ('what would thicken the repair from a corollary to a tool', 'CLOSE',
     'NAMED: the TIER-2 form of the barrier. ### And the blocker is named by kind: **OPEN '
     'MATHEMATICS, NOT A PARKED LANE** -- the document calls it research-frontier itself.'),
    ('the (R20) shortfall at the SIDE-kernel question', 'STANDING',
     'ROUTED TO THE AUTHOR. ### Limb 2 is the one; widening it would make the rule prescribe what '
     'the corpus has not done, against its own *discovered, not imposed*. ### The cost is stated '
     'so the author is not asked to pay it blind.'),
    ('the stale-run-record species', 'CLOSE',
     'MECHANIZED. ### `run_clock.latest()` added ADDITIVELY, with two fixtures in both polarities; '
     'the instrument already stamped and only the reader was missing. ### Both options priced '
     'before the choice, and the choice was fixed on the locked face.'),
    ('the spectral-realization face as a bright channel', 'STANDING',
     'ANSWERED IN PART: it IS one in Corollary 3.6’s sense, by the record’s own words. ### '
     'But the disclaimer and the demand are NOT one sentence -- an existential over three channels '
     'is not negated by disclaiming one. ### What would make them one is named: Tier 2.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT. ### No claim in either direction.'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES FIVE ITEMS AND LEAVES THE REST STANDING.**')
    rec('')
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for k in range(0, min(len(why), 1200), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block(Q):
    return [
        '',
        MARK,
        '',
        '### b407 — the barrier read against the method, the escape-kind price corrected, and the '
        'repair priced where it is thin — filed 2026-09-10',
        '',
        '**The E0 gate’s halt at `K8` is NOT AN INSTANCE of the Sieve Ceiling Lemma, and the '
        'hypothesis that fails is not the one a reader would expect.** Four of Theorem 3.1’s five '
        'hypotheses are MET at the corpus’s own object, in the document’s own words: `ξ` is '
        'determined (*"ξ(s) determined by its specification chain n² → θ → Mellin"*); the '
        'interface is named (*"the product-formula interface"*); the target parameter is the '
        'clause’s own (*"x is a zero with Re(x) = 1/2"*); and **`κ = 0` is ASSERTED by the record '
        'itself** — *"For ξ, I is essential and κ(σ, I) = 0."* **THE HYPOTHESIS THAT FAILS IS THE '
        'ONE ABOUT `π`**: the theorem is about *"a formal first-order proof in ZFC ∪ S"* whose '
        '*"every inference step"* is classified, and the corpus’s reduction is not that object. '
        'The E0 gate’s own table says so: its constituents unfold to IMPORTS UNDER THE BAR (`K1`, '
        '`K2`, `K4`, `K6`), derivations on content, kernel terminals, measurements at cells, a '
        'bench residual, and one UNOWNED constituent. **AN IMPORT UNDER THE BAR IS NOT AN '
        'INFERENCE STEP; IT IS A PREMISE THE CORPUS HAS NOT DISCHARGED.** And the document adds a '
        'second, independent reason in its own scope line: *"that open-class form, Tier 2, is '
        'research-frontier and not claimed here."*',
        '',
        '**And the resemblance is exact, which is precisely why it must not be filed as an '
        'instance.** Definition 2.5 says a step factors through `I` when it references only '
        '*"cumulative invariants of I (integrals, densities, or measure-theoretic quantities '
        'averaging over I), but not individual-element specifications requiring P-information to '
        'cross I"*. The corpus’s criterion is a **sum over the places** — a cumulative invariant of '
        'exactly that interface — and every constituent the E0 gate does NOT halt at is one of its '
        'parts. The one it DOES halt at is the individual-element specification: `K8`, *"UNOWNED: '
        'over the class (infinite) and, through the explicit formula, over the zeros."* **THE E0 '
        'GATE HALTS PRECISELY WHERE DEFINITION 2.5 SAYS A FACTORING PROOF MUST STOP** — two '
        'instruments built for different purposes, drawing the line in the same place. **That is a '
        'resemblance, not an instance.** This session has met the distinction twice before — a '
        'compiled countermodel about a SHAPE at b405, a witness form that does not transpose at '
        'b406 — and reporting it as an instance would be the third time and the first failure. '
        '**NOTHING IS FILED TO ROW `U1`. What the row would need is a formalisation of the '
        'reduction as a first-order proof with every step classified — which is not a build, and '
        'the parked lane does not block it. It is a piece of writing nobody has done.**',
        '',
        '**None of the six sites names an interface in the lemma’s sense, and four of them name a '
        'split that is an interface somewhere else.** Definition 2.2 makes an interface a formula '
        'of a DETERMINED STRUCTURE and makes *essential* mean *removable from the SPECIFICATION*; '
        '**not one of the six names a specification.** The sites are sentences about what the '
        'record holds and needs, and the lemma’s subject is a structure and its axioms. **STRICT: '
        '0 of 6. LOOSE: 4 of 6** — `(i)` the explicit formula, `(iv)` the prime side against an '
        'archimedean quantity, `(v)` Theorem 6.1’s finite places against Theorem 5.1’s '
        'archimedean, `(vi)` local against global. **Both counts are printed and the kinder one is '
        'not reported alone.** No transmission coefficient is measured, asserted or inferred by '
        'this act.',
        '',
        '**b406’s escape-kind price was optimistic by one, and the correction comes from the '
        'record’s own list.** `THE_DIFFICULTY_KINDS.md` files *RH-sign’s receding `N₀(T)`* under '
        '**scale-horizon** and *RH-derivative* under **raw-infinitude** — **the same object on both '
        'sides of its own dichotomy.** So the escape-kind is a property of the QUESTION asked about '
        'an object, not of the object, and a cell can be filled only where the site says which '
        'question it is asking. `(i)`’s index is the class and the zeros — a height, which is a '
        'scale, and an infinite set, which is not — and its text does not say which. **THE PRICE '
        'FALLS FROM 5 OF 6 TO 4 OF 6.** It was this seat’s own price, set two acts ago, and it is '
        'corrected here with its number and its reason: **a price is not protected by having been '
        'this seat’s.**',
        '',
        '**The repair is thin, and what would thicken it is named — with the right kind of blocker '
        'beside it.** Corollary 3.6 gives an EXISTENTIAL over channels: *"at least one inference '
        'step operating through a κ > 0 interface — a bright channel"*, with no channel named. But '
        'the record adds two sentences that change the answer: the channels *"are exactly the '
        'mechanism classes themselves"*, and *"every derivation chain from θ to a zero-location '
        'constraint factors through the archimedean, multiplicative, or global structure of ℚ. No '
        'fourth source exists."* **So the existential ranges over THREE named things.** The '
        'smallest statement that would turn the corollary from an existential into a NAME is **the '
        'Tier-2 form of the barrier** — that no Euler-product-free derivation establishes `P` for '
        '`ξ`, over the open class rather than a named finite toolkit. **AND THE BLOCKER IS NOT THE '
        'PARKED LANE.** No build bears on a Tier-2 barrier; the document calls it '
        'research-frontier in its own words. **A statement nobody has written is not a statement a '
        'parked lane is withholding**, and this act says which one it met.',
        '',
        '**The spectral-realization face IS the corollary’s bright channel, and the disclaimer is '
        'NOT the demand from the other side.** Its output stage is, in the deposit’s own words, '
        '*"that the zeros themselves are the spectrum of a self-adjoint operator with a positive '
        'pairing"* — an interface across which element-level information about individual zeros '
        'crosses by construction, and a mechanism class (`C₅`), which is what the corollary says '
        'its channels are. **But a disclaimer of ONE of THREE is not the negation of an '
        'existential over THREE.** What would make them one sentence is named and not supplied: a '
        'statement that `C₃` and `C₄` are `P`-dark at this target — **the same Tier-2 statement**, '
        'which the document says it has not claimed. **They become one sentence exactly when the '
        'Tier-1 barrier is lifted to Tier 2.** Quoted, decided by nobody, and **not typed as a '
        'bridge**: this act does not read a disclaimer as an assertion of its converse.',
        '',
        '**`(R20)`’s shortfall is routed with its price.** The limb is the second — *a kernel '
        'deposits when a published claim cites its terminals* — the only limb whose subject is a '
        'kernel, and one whose antecedent is false for a kernel with no citing claim, which is '
        'exactly the `SIDE-kernel` question b392 left standing. **Widening it would make the rule '
        'prescribe what the corpus has not done — against its own *"The rule is descriptive before '
        'it is prescriptive"* and *"It is discovered, not imposed."*** A rule that claims to '
        'describe cannot be widened by a seat. **ROUTED; 0 rules struck, amended, widened or '
        're-ruled.**',
        '',
        '**And the stale-run-record species is mechanized, additively.** b406 read a dead run '
        'record three times because `run_clock` versions its output and the newest-by-mtime file '
        'was not the newest run. Both options were priced before the choice and the choice fixed '
        'on the locked face: amending `write` to print would widen **every act’s** output, so the '
        'guard is a new reader instead. **`run_clock.latest()` returns the newest run BY ITS OWN '
        'CLOCK and REFUSES rather than guesses when a candidate carries none** — a guard that falls '
        'back to mtime is the defect, not the cure. Its positive fixture touches the OLDER record '
        'last so that mtime and the clock disagree, because **a fixture that agrees with the defect '
        'cannot catch it.** The instrument already stamped every record and already read the stamp '
        'back; **only the latest-by-stamp reader was missing.** Purely additive: no existing caller '
        'moves and no existing byte changes.',
        '',
        '**Nothing deposits.** `0` rows of `FACES_LEDGER.md` written, `0` in-place repairs, `0` '
        'coordinates added, `0` names minted, `0` rules widened, `0` grades moved, `0` bridges '
        'typed, `0` transmission coefficients measured, `0` kernels built, `0` `.lean` files '
        'touched, `0` content lost. Both lanes stay parked and the wave stays parked. Registration '
        '`data/b407_registration_2026-09-10.txt`, LOCKED before any write at sha256 `%s`, chained '
        'on `tools/b378_lockgate.py` run as b407 — %d gates read, %d checked by digest. Bank: '
        '`relay/data/b407_the_barriers_own_instance.txt`. **h2 where the deposit left it.**'
        % (SEALHASH, LG['gates_read'], LG['face_subject_gates']),
    ]


SCOPE = ("### THIS ROW RECORDS A THEOREM READ AGAINST A METHOD AND FOUND NOT TO APPLY, A PRICE "
         "CORRECTED, A MISSING STATEMENT NAMED AND A GUARD BUILT. ### IT CERTIFIES NO EQUIVALENCE, "
         "OPENS NO TERMINAL, MOVES NO GRADE, MEASURES NO COEFFICIENT AND TYPES NO BRIDGE")


def corr_rows(Q):
    m = ("**THE CORPUS'S OWN BARRIER THEOREM DOES NOT APPLY TO THE CORPUS'S OWN REDUCTION, AND THE "
         "HYPOTHESIS THAT FAILS IS THE ONE ABOUT WHAT A PROOF IS -- WHILE THE RESEMBLANCE IS EXACT "
         "TO THE CONSTITUENT** (b407, the barrier's own instance)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b407 -- %d gates read, %d checked by digest; the survey left 0 anchor misses. "
            "**ADDITION THREE: NOT AN INSTANCE OF THEOREM 3.1.** Four hypotheses are MET at the "
            "corpus's own object in the document's own words, kappa = 0 among them (*For xi, I is "
            "essential and kappa(sigma, I) = 0*); the one that FAILS is that pi be a formal "
            "first-order proof in ZFC union S with every inference step classified, and the "
            "corpus's reduction is a chain of IMPORTS UNDER THE BAR, derivations on content, "
            "kernel terminals, measurements at cells and one UNOWNED constituent. AN IMPORT UNDER "
            "THE BAR IS NOT AN INFERENCE STEP. **AND THE RESEMBLANCE IS EXACT AND PRINTED BESIDE "
            "THE VERDICT**: the criterion is a sum over places, a cumulative invariant of that "
            "interface, and THE E0 GATE HALTS PRECISELY WHERE DEFINITION 2.5 SAYS A FACTORING "
            "PROOF MUST STOP. **COMPONENT 1: 0 of 6 sites name an interface in Definition 2.2's "
            "sense, 4 of 6 name a split that is an interface elsewhere** -- both counts printed, "
            "the strict one governing, and NO COEFFICIENT MEASURED. **COMPONENT 2: b406's "
            "escape-kind price falls from 5 to 4**, because the record's own list files RH under "
            "BOTH kinds, so the kind is a property of the question. **COMPONENT 3: the smallest "
            "statement thickening the repair is the TIER-2 FORM OF THE BARRIER, and the blocker is "
            "OPEN MATHEMATICS AND NOT THE PARKED LANE.** **ADDITION FOUR: the spectral-realization "
            "face IS a bright channel, and a disclaimer of one of three channels is NOT the "
            "negation of an existential over three.** **ADDITION ONE: (R20) limb 2 ROUTED with its "
            "price.** **ADDITION TWO: run_clock.latest() added additively with two fixtures.** %d "
            "ROWS WRITTEN, %d BRIDGES TYPED, %d COEFFICIENTS MEASURED, %d RULES WIDENED, %d "
            "KERNELS BUILT, %d CONTENT LOST"
            % (LG['gates_read'], LG['face_subject_gates'], 0, 0, 0, 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED. ### NO KERNEL WAS BUILT, NO "
            "`.lean` FILE TOUCHED AND NO AXIOM PROFILE READ OR INFERRED. ### THE ONLY COMPILED "
            "OBJECTS NAMED ARE NAMED AS THINGS THE RECORD CITES, NOT AS THINGS THIS ACT MEASURED. "
            "### READING A THEOREM'S HYPOTHESES IS NOT CLAIMING ITS CONCLUSION")
    prof = ("### NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK, "
            "AMENDED, WIDENED OR RE-RULED, NO CLASS RULED, NO REGISTRY ROW EDITED, NO KEYSTONE "
            "EDITED, NO LOCKED FACE EDITED, NO BANKED FERRY EDITED, NO PRIOR ACT'S BANK EDITED, NO "
            "ROW OF FACES_LEDGER WRITTEN, NO FERRY_STANDING CLAUSE ADDED, NO IN-PLACE REPAIR MADE, "
            "NO LIST CLOSED. ### THE CORPUS WRITES ARE ONE APPEND-ONLY TRAIL BLOCK AND ONE "
            "APPENDED CORRESPONDENCE ROW; THE RELAY WRITES ARE ONE APPENDED INDEX KEY AND ONE "
            "ADDITIVE FUNCTION IN A SHARED INSTRUMENT WHOSE EXISTING BYTES DO NOT MOVE -- 0 "
            "CONTENT LOST")
    grade = ("### FOUR OF FIVE HYPOTHESES WERE CHECKED AND REPORTED MET BEFORE THE FIFTH WAS "
             "REPORTED FAILING, SO THE VERDICT IS NOT A DISMISSAL. ### THE RESEMBLANCE IS PRINTED "
             "BESIDE THE VERDICT AND NOT INSTEAD OF IT, BECAUSE IT IS EXACT AND THAT IS PRECISELY "
             "WHY IT MUST NOT BE FILED. ### BOTH READINGS OF COMPONENT 1 ARE PRINTED AND THE "
             "KINDER ONE IS NOT REPORTED ALONE. ### A PRICE THIS SEAT SET TWO ACTS AGO WAS "
             "CORRECTED AGAINST THE RECORD RATHER THAN DEFENDED. ### A BLOCKER WAS NAMED BY KIND, "
             "BECAUSE A STATEMENT NOBODY HAS WRITTEN IS NOT A STATEMENT A PARKED LANE IS "
             "WITHHOLDING. ### AND A DEPOSIT'S DISCLAIMER WAS NOT READ AS AN ASSERTION OF ITS "
             "CONVERSE")
    status = ("data/b407_the_barriers_own_instance.txt; data/b407_components.txt; "
              "data/b407_extract.txt; data/b407_registration_2026-09-10.txt (LOCKED before any "
              "write at sha256 %s, chained on tools/b378_lockgate.py run as b407); "
              "tools/b407_extract.py; tools/b407_regspec.py; tools/b407_reg_gate.py; "
              "tools/b407_components.py; tools/b407_desk_bank.py; tools/b407_checks.py; "
              "relay tools/run_clock.py (one added function and its fixture); PLACE-papers "
              "OPEN_TRAILS.md (one append-only block); CORRESPONDENCE.md row %%d"
              % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('does the sieve ceiling lemma apply to the corpus reduction',
           'is the corpus reduction a formal proof',
           'do the uniformity sites name an interface',
           'what would make the corollary name a channel',
           'is the spectral realization the bright channel',
           'how do you find the newest run record')
MUST_NOT_HIT = ('the theorem applies to the reduction', 'a coefficient was measured',
                'a row was written to the ledger', 'a rule was widened', 'a kernel was built')
KEY = 'the-barriers-own-instance'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b407 PUT THE CORPUS'S OWN BARRIER THEOREM TO THE CORPUS'S OWN REDUCTION AND FOUND IT DOES "
        "NOT APPLY. **FOUR OF THEOREM 3.1'S FIVE HYPOTHESES ARE MET AT THE CORPUS'S OWN OBJECT, IN "
        "THE DOCUMENT'S OWN WORDS**: xi is determined; the interface is the product formula; the "
        "target parameter is the clause's own; and **kappa = 0 IS ASSERTED BY THE RECORD ITSELF** "
        "-- *For xi, I is essential and kappa(sigma, I) = 0*. **THE HYPOTHESIS THAT FAILS IS THE "
        "ONE ABOUT pi**: the theorem is about a formal first-order proof in ZFC union S whose "
        "every inference step is classified, and the corpus's reduction is a chain of IMPORTS "
        "UNDER THE BAR (K1, K2, K4, K6), derivations on content, kernel terminals, measurements at "
        "cells, a bench residual and one UNOWNED constituent. **AN IMPORT UNDER THE BAR IS NOT AN "
        "INFERENCE STEP; IT IS A PREMISE THE CORPUS HAS NOT DISCHARGED.** A second printed reason "
        "stands beside it: the document scopes its own barrier to Tier 1 and says the open-class "
        "form is *research-frontier and not claimed here*. **AND THE RESEMBLANCE IS EXACT, WHICH IS "
        "WHY IT MUST NOT BE FILED**: Definition 2.5 lets a factoring step reference only cumulative "
        "invariants and not individual-element specifications; the corpus's criterion is a SUM OVER "
        "THE PLACES, every constituent the E0 gate does not halt at is one of its parts, and the "
        "one it DOES halt at is K8, the individual-element specification. **THE E0 GATE HALTS "
        "PRECISELY WHERE DEFINITION 2.5 SAYS A FACTORING PROOF MUST STOP.** Nothing is filed to row "
        "U1. **COMPONENT 1: 0 OF 6 SITES NAME AN INTERFACE IN DEFINITION 2.2'S SENSE** -- not one "
        "names a SPECIFICATION -- **and 4 of 6 name a SPLIT that is an interface elsewhere in the "
        "record**; both counts printed, no coefficient measured. **COMPONENT 2: b406'S ESCAPE-KIND "
        "PRICE FALLS FROM 5 TO 4**, because THE_DIFFICULTY_KINDS files RH-sign under scale-horizon "
        "and RH-derivative under raw-infinitude -- the same object on both sides of its own "
        "dichotomy -- so **THE ESCAPE-KIND IS A PROPERTY OF THE QUESTION, NOT OF THE OBJECT**, and "
        "(i) cannot be filled from its own text. **COMPONENT 3: THE SMALLEST STATEMENT THICKENING "
        "THE REPAIR IS THE TIER-2 FORM OF THE BARRIER** -- with it, Corollary 3.6 stops being an "
        "existential over the three mechanism classes the corpus's exhaustiveness names and becomes "
        "a NAME, C5 -- **AND THE BLOCKER IS OPEN MATHEMATICS AND NOT THE PARKED LANE.** **ADDITION "
        "FOUR: THE SPECTRAL-REALIZATION FACE IS A BRIGHT CHANNEL IN THE COROLLARY'S SENSE, AND THE "
        "DEPOSIT'S DISCLAIMER IS NOT THE DEMAND FROM THE OTHER SIDE** -- a disclaimer of one of "
        "three channels is not the negation of an existential over three; they become one sentence "
        "exactly at Tier 2. **ADDITION ONE: (R20)'s limb 2 is the one that would be widened, and "
        "widening it costs the rule's own claim to be discovered, not imposed -- ROUTED.** "
        "**ADDITION TWO: run_clock.latest() added ADDITIVELY**, returning the newest run by its own "
        "clock and REFUSING rather than guessing when a candidate carries none.")
    grade = (
        "### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY "
        "CLONED, NO AXIOM PROFILE READ OR INFERRED AND NO TRANSMISSION COEFFICIENT MEASURED, "
        "ASSERTED OR INFERRED. ### NO GRADE MOVED, NO ROW OF FACES_LEDGER WRITTEN, NO COORDINATE "
        "ADDED, NO NAME MINTED, NO RULE STRUCK OR WIDENED, NO BRIDGE TYPED, NO IN-PLACE REPAIR "
        "MADE, NO KEYSTONE EDITED, NO LOCKED FACE EDITED, NO BANKED FERRY EDITED, NO FERRY_STANDING "
        "CLAUSE ADDED, NO LIST CLOSED. ### THE ONE SHARED INSTRUMENT TOUCHED WAS AMENDED ADDITIVELY "
        "AND ITS EXISTING BYTES DID NOT MOVE. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED "
        "AT ALL. ### THE CLAUSE HAS NOT MOVED")
    where = (
        "data/b407_the_barriers_own_instance.txt; data/b407_components.txt; data/b407_extract.txt; "
        "data/b407_registration_2026-09-10.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b407 -- %d gates read, %d checked by digest); "
        "tools/b407_extract.py; tools/b407_components.py; tools/b407_desk_bank.py; "
        "tools/b407_checks.py; relay tools/run_clock.py; PLACE-papers OPEN_TRAILS.md; "
        "CORRESPONDENCE.md row %d" % (LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b407 (the corpus's own barrier theorem put to its own reduction and found not to "
           "apply, the failing hypothesis named, the resemblance printed beside it, and the "
           "repair's missing statement identified as Tier 2)")
    row_new = ('    # ### THE BARRIER-S OWN INSTANCE (b407).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where, chr(10)))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-42s NO KEY before : %s' % (qq, pre[qq]))
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
        rec('    %-58s reaches the b407 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('the verdict is NOT AN INSTANCE', 'DOES NOT APPLY' in out),
            ('the failing hypothesis is named', 'THE ONE ABOUT pi' in out),
            ('kappa = 0 is reported as ASSERTED by the record', 'IS ASSERTED BY THE RECORD' in out),
            ('the import-under-the-bar reason', 'NOT AN INFERENCE STEP' in out),
            ('the resemblance is printed', 'PRECISELY WHERE DEFINITION 2.5' in out),
            ('both counts of component 1', '0 OF 6 SITES NAME AN INTERFACE' in out
             and '4 of 6 name a SPLIT' in out),
            ('the price correction', 'FALLS FROM 5 TO 4' in out),
            ('the escape-kind finding', 'PROPERTY OF THE QUESTION' in out),
            ('the smallest statement', 'TIER-2 FORM OF THE BARRIER' in out),
            ('the blocker named by kind', 'NOT THE PARKED LANE' in out),
            ('the disclaimer is not the demand', 'IS NOT THE DEMAND FROM THE OTHER SIDE' in out),
            ('(R20) routed', 'ROUTED' in out),
            ('the guard is additive', 'ADDITIVELY' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-42s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank(Q, rownum, kok):
    B = []
    BAR, SUB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BAR)
    A("b407 -- THE BARRIER'S OWN INSTANCE, AND THE REPAIR PRICED WHERE IT IS THIN. ### THE BANK.")
    A('### 2026-09-10. ### CONCURRENCY: SOLO (research seat).')
    A('### Registration `data/b407_registration_2026-09-10.txt`, LOCKED BEFORE ANY WRITE at')
    A('### `%s`, %d bytes, chained on `b378_lockgate.py` run as b407' % (SEALHASH,
                                                                         len(SEALTXT.encode('utf-8'))))
    A('### -- ### **%d GATES READ, %d PASSING, %d CHECKED BY DIGEST.**'
      % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    A(BAR)
    A('')
    A(SUB)
    A('### (1) THE ANSWER, FIRST.')
    A(SUB)
    A('### ### ### **THE CORPUS’S OWN BARRIER THEOREM DOES NOT APPLY TO THE CORPUS’S OWN')
    A('### ### ### REDUCTION -- AND THE HYPOTHESIS THAT FAILS IS NOT THE ONE ANYONE WOULD GUESS.**')
    A('### Four of Theorem 3.1’s five hypotheses are ### **MET AT THE CORPUS’S OWN')
    A('### ### OBJECT, IN THE DOCUMENT’S OWN WORDS**: ### `xi` is determined; the interface is')
    A('### the product formula; the target parameter is the clause’s own; and ### **`kappa = 0`')
    A('### ### IS ASSERTED BY THE RECORD ITSELF** -- *"For ξ, I is essential and')
    A('### κ(σ, I) = 0."*')
    A('### ### **THE ONE THAT FAILS IS THE ONE ABOUT `π`.** ### The theorem is about *"a')
    A('### formal first-order proof in ZFC ∪ S"* whose *"every inference step"* is classified,')
    A('### and the corpus’s reduction is a chain of ### **IMPORTS UNDER THE BAR** ### (`K1`,')
    A('### `K2`, `K4`, `K6`), derivations on content, kernel terminals, measurements at cells, a')
    A('### bench residual, and one ### **UNOWNED** ### constituent. ### ### **AN IMPORT UNDER THE')
    A('### ### BAR IS NOT AN INFERENCE STEP; IT IS A PREMISE THE CORPUS HAS NOT DISCHARGED.**')
    A('### **AND A SECOND, INDEPENDENT PRINTED REASON, FROM THE DOCUMENT’S OWN SCOPE:** ###')
    A('### *"that open-class form, Tier 2, is research-frontier and not claimed here."*')
    A('')
    A(SUB)
    A('### (2) AND THE RESEMBLANCE IS EXACT -- WHICH IS WHY IT MUST NOT BE FILED.')
    A(SUB)
    A('### Definition 2.5 lets a factoring step reference only *"cumulative invariants of I')
    A('### (integrals, densities, or measure-theoretic quantities averaging over I), but not')
    A('### individual-element specifications requiring P-information to cross I"*.')
    A('### ### **THE CORPUS’S CRITERION IS A SUM OVER THE PLACES** -- a cumulative invariant of')
    A('### exactly that interface -- and ### **EVERY CONSTITUENT THE E0 GATE DOES NOT HALT AT IS')
    A('### ### ONE OF ITS PARTS.** ### The one it DOES halt at is the individual-element')
    A('### specification: `K8`, *"UNOWNED: over the class (infinite) and, through the explicit')
    A('### formula, over the zeros."*')
    A('### ### ### **THE E0 GATE HALTS PRECISELY WHERE DEFINITION 2.5 SAYS A FACTORING PROOF MUST')
    A('### ### ### STOP** -- two instruments built for different purposes, drawing the line in the')
    A('### ### ### same place.')
    A('### ### **AND THAT IS A RESEMBLANCE, NOT AN INSTANCE.** ### This session has met the')
    A('### distinction twice: a compiled countermodel about a SHAPE at `b405`, a witness form that')
    A('### does not transpose at `b406`. ### **REPORTING IT AS AN INSTANCE WOULD BE THE THIRD TIME')
    A('### ### AND THE FIRST FAILURE.**')
    A('### ### **SO NOTHING IS FILED TO ROW `U1`. ### `0` ROWS WRITTEN.** ### What the row would')
    A('### need is a formalisation of the reduction as a first-order proof with every step')
    A('### classified -- ### **NOT A BUILD, AND THE PARKED LANE DOES NOT BLOCK IT. ### A PIECE OF')
    A('### ### WRITING NOBODY HAS DONE.**')
    A('')
    A(SUB)
    A('### (3) COMPONENT 1 -- BOTH COUNTS, AND THE KINDER ONE NOT REPORTED ALONE.')
    A(SUB)
    A('### **STRICT (Definition 2.2): ### `0` OF 6.** ### An interface is a formula of a')
    A('### ### **DETERMINED STRUCTURE**, and *essential* means *removable from the')
    A('### ### **SPECIFICATION***. ### ### **NOT ONE OF THE SIX SITES NAMES A SPECIFICATION.**')
    A('### **LOOSE (names a SPLIT the record elsewhere calls an interface of `xi`): ### `4` OF 6** --')
    A('###   `(i)` the explicit formula; `(iv)` the prime side against an archimedean quantity;')
    A('###   `(v)` Theorem 6.1’s finite places against Theorem 5.1’s archimedean;')
    A('###   `(vi)` local against global.')
    A('### ### **THE SITES ARE SENTENCES ABOUT WHAT THE RECORD HOLDS AND NEEDS; THE LEMMA’S')
    A('### ### SUBJECT IS A STRUCTURE AND ITS AXIOMS.**')
    A('### ### **AND `kappa` IS DECIDED NOWHERE.** ### `0` coefficients measured, asserted or')
    A('### inferred by this act.')
    A('')
    A(SUB)
    A('### (4) COMPONENT 2 -- A PRICE THIS SEAT SET, CORRECTED AGAINST THE RECORD.')
    A(SUB)
    A('### `THE_DIFFICULTY_KINDS.md` files *RH-sign’s receding `N_0(T)`* under')
    A('### ### **`scale-horizon`** ### and *RH-derivative* under ### **`raw-infinitude`** --')
    A('### ### **THE SAME OBJECT ON BOTH SIDES OF ITS OWN DICHOTOMY.**')
    A('### ### ### **SO THE ESCAPE-KIND IS A PROPERTY OF THE QUESTION ASKED ABOUT AN OBJECT, NOT OF')
    A('### ### ### THE OBJECT**, and a cell can be filled only where the site says which question')
    A('### it is asking. ### `(i)`’s index is the class and the zeros -- a HEIGHT, which is a')
    A('### scale, and an infinite SET, which is not -- and its text does not say which.')
    A('### ### **THE PRICE FALLS FROM `5` OF 6 TO `4` OF 6.** ### It was this seat’s own price,')
    A('### set two acts ago, and it is corrected with its number and its reason. ### **A PRICE IS')
    A('### ### NOT PROTECTED BY HAVING BEEN THIS SEAT’S.**')
    A('')
    A(SUB)
    A('### (5) COMPONENT 3 -- THE SMALLEST STATEMENT, AND THE BLOCKER NAMED BY KIND.')
    A(SUB)
    A('### Corollary 3.6 gives an ### **EXISTENTIAL OVER CHANNELS** ### with no channel named. ###')
    A('### But the record adds two sentences that change the answer: the channels *"are exactly the')
    A('### mechanism classes themselves"*, and *"every derivation chain from θ to a')
    A('### zero-location constraint factors through the archimedean, multiplicative, or global')
    A('### structure of ℚ. No fourth source exists."*')
    A('### ### **SO THE EXISTENTIAL RANGES OVER THREE NAMED THINGS.**')
    A('### ### ### **THE SMALLEST STATEMENT: THE TIER-2 FORM OF THE BARRIER** -- that no')
    A('### Euler-product-free derivation establishes `P` for `xi`, over the ### **OPEN CLASS** ###')
    A('### rather than a named finite toolkit. ### With it, the corollary stops being an')
    A('### existential and becomes ### **A NAME: `C5`.**')
    A('### ### **AND THE BLOCKER IS NOT THE PARKED LANE.** ### No build bears on a Tier-2 barrier;')
    A('### the document calls it ### **RESEARCH-FRONTIER** ### in its own words. ### **A STATEMENT')
    A('### ### NOBODY HAS WRITTEN IS NOT A STATEMENT A PARKED LANE IS WITHHOLDING**, and this act')
    A('### says which one it met.')
    A('')
    A(SUB)
    A('### (6) ADDITION FOUR -- A BRIGHT CHANNEL, AND TWO SENTENCES THAT ARE NOT ONE.')
    A(SUB)
    A('### **IS THE FACE A BRIGHT CHANNEL? ### ### YES, BY THE RECORD’S OWN WORDS.** ### Its')
    A('### output stage is *"that the zeros themselves are the spectrum of a self-adjoint operator')
    A('### with a positive pairing"* -- ### **AN INTERFACE ACROSS WHICH ELEMENT-LEVEL INFORMATION')
    A('### ### ABOUT INDIVIDUAL ZEROS CROSSES BY CONSTRUCTION** -- and it is a mechanism class,')
    A('### `C5`, which is what the corollary says its channels are.')
    A('### **ARE THE DISCLAIMER AND THE DEMAND ONE SENTENCE? ### ### NO.** ### The corollary is an')
    A('### existential over the ### **THREE** ### channels the corpus’s own exhaustiveness')
    A('### names, and the deposit disclaims the output stage of ### **ONE** ### of them. ###')
    A('### ### **A DISCLAIMER OF ONE OF THREE IS NOT THE NEGATION OF AN EXISTENTIAL OVER THREE.**')
    A('### ### **WHAT WOULD MAKE THEM ONE, NAMED AND NOT SUPPLIED:** ### a statement that `C3` and')
    A('### `C4` are `P`-dark at this target -- ### **THE SAME TIER-2 STATEMENT COMPONENT 3 NAMED.**')
    A('### ### **THEY BECOME ONE SENTENCE EXACTLY WHEN THE TIER-1 BARRIER IS LIFTED TO TIER 2, AND')
    A('### ### THE RECORD SAYS IN ITS OWN WORDS THAT IT HAS NOT DONE THAT.**')
    A('### **QUOTED, DECIDED BY NOBODY, AND NOT TYPED AS A BRIDGE.** ### **THIS ACT DOES NOT READ A')
    A('### ### DISCLAIMER AS AN ASSERTION OF ITS CONVERSE.**')
    A('')
    A(SUB)
    A('### (7) ADDITION ONE -- `(R20)` ROUTED WITH ITS PRICE.')
    A(SUB)
    A('### **THE LIMB IS THE SECOND:** ### *a kernel deposits when a published claim cites its')
    A('### terminals*. ### It is the only limb whose subject is a kernel, and for a kernel with no')
    A('### citing claim ### **ITS ANTECEDENT IS FALSE** -- which is exactly the `SIDE-kernel`')
    A('### question `b392` left standing.')
    A('### **WHAT THE WIDENING COSTS, IN THE RULE’S OWN WORDS:** ### *"The rule is descriptive')
    A('### before it is prescriptive"*; *"It is discovered, not imposed."*')
    A('### ### ### **WIDENING LIMB 2 WOULD MAKE THE RULE PRESCRIBE WHAT THE CORPUS HAS NOT DONE --')
    A('### ### ### THE CLAIM IT MAKES ABOUT ITSELF, DESTROYED.** ### **A RULE THAT CLAIMS TO')
    A('### ### DESCRIBE CANNOT BE WIDENED BY A SEAT.** ### ROUTED, with the cost stated so the')
    A('### author is not asked to pay it blind.')
    A('')
    A(SUB)
    A('### (8) ADDITION TWO -- THE GUARD, BUILT ADDITIVELY.')
    A(SUB)
    A('### **BOTH OPTIONS PRICED BEFORE THE CHOICE, AND THE CHOICE FIXED ON THE LOCKED FACE:**')
    A('###   ### **(a)** ### amend `write` to print what it wrote -- one line, and it widens')
    A('###       ### **EVERY ACT’S OUTPUT.** ### The reason `quote_norm` was left alone.')
    A('###   ### **(b)** ### add a latest-by-stamp reader -- ### **PURELY ADDITIVE.**')
    A('### ### **`(b)` WAS FIXED AND `(b)` WAS BUILT.**')
    A('### `run_clock.latest()` returns the newest run ### **BY ITS OWN CLOCK** ### and')
    A('### ### **REFUSES RATHER THAN GUESSES** ### when a candidate carries none -- because ### **A')
    A('### ### GUARD THAT FALLS BACK TO MTIME WHEN IT CANNOT KNOW IS THE DEFECT, NOT THE CURE.**')
    A('### **ITS POSITIVE FIXTURE TOUCHES THE OLDER RECORD LAST**, so mtime and the clock disagree')
    A('### and a mtime reader returns the wrong file: ### **A FIXTURE THAT AGREES WITH THE DEFECT')
    A('### ### CANNOT CATCH IT.**')
    A('### ### **AND THE INSTRUMENT ALREADY HELD MOST OF THE CURE:** ### `write` has always put the')
    A('### clock on the first line and `read_stamp` has always read it back. ### **ONLY THE')
    A('### ### LATEST-BY-STAMP READER WAS MISSING.**')
    A('')
    A(SUB)
    A('### (9) THE WRITES, AND WHAT THEY COST THE RECORD.')
    A(SUB)
    A('### **`OPEN_TRAILS.md`** ### -- one append-only block.')
    A('### **`CORRESPONDENCE.md`** ### -- row `%d`, appended, six cells non-empty.' % rownum)
    A('### **THE INDEX** ### -- one key, `%s`, %s.' % (KEY, 'PASS' if kok else '### FAIL ###'))
    A('### **`tools/run_clock.py`** ### -- one added function and its fixture; ### **EVERY EXISTING')
    A('### ### BYTE WHERE IT WAS.**')
    A('### **AND NOTHING ELSE.** ### `0` rows of `FACES_LEDGER.md`, `0` in-place repairs, `0`')
    A('### coordinates added, `0` names minted, `0` rules widened, `0` grades moved, `0` bridges')
    A('### typed, `0` coefficients measured, `0` `.lean` files touched, `0` kernels built, `0`')
    A('### `FERRY_STANDING` clauses, `0` content lost. ### ### **NOTHING DEPOSITS.**')
    A('')
    A(SUB)
    A('### (10) WHAT THIS ACT DOES NOT SAY.')
    A(SUB)
    A('### It does not say the barrier theorem is wrong, or small, or inapplicable in general. ###')
    A('### **IT SAYS THE CORPUS’S REDUCTION IS NOT THE KIND OF OBJECT THE THEOREM QUANTIFIES')
    A('### ### OVER**, and that four of its five hypotheses are met.')
    A('### It does not endorse `kappa(σ, I) = 0`. ### **IT REPORTS THAT THE RECORD ASSERTS IT,')
    A('### ### IN THE RECORD’S OWN SENTENCE, AND STOPS.**')
    A('### It does not say the spectral realization exists, or can. ### **THE DEPOSIT DISCLAIMS IT')
    A('### ### AND THIS ACT DOES NOT READ A DISCLAIMER AS ITS CONVERSE.**')
    A('### It files nothing to row `U1`, mints no name, widens no rule, and closes no list.')
    A('### ### **NOTHING DEPOSITS. ### THE PLATFORM WAS NOT CALLED AT ALL. ### `h2` STANDS EXACTLY')
    A('### ### WHERE THE DEPOSIT LEFT IT AND THIS ACT MAKES NO CLAIM ABOUT IT IN EITHER')
    A('### ### DIRECTION.**')
    A(BAR)
    io.open(BANKOUT, 'wb').write((chr(10).join(B) + chr(10)).encode('utf-8'))
    rec('  bank written : %s (%d lines)' % (os.path.basename(BANKOUT), len(B)))
    return len(B)


def main():
    bar('=')
    rec('b407 -- THE DESK, THE TRAIL BLOCK, THE ROW, THE KEY AND THE BANK.')
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
        rec('  ### the b406 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            rec('  ### run record : %s' % run_clock.write(D, 'b407_desk_notes', LINES))
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_not_an_instance': 'not an instance' in low,
        'says_four_met': 'four of theorem 3.1' in low,
        'says_kappa_asserted': 'is asserted by the record' in low,
        'says_failing_hyp': 'the hypothesis that fails is the one about' in low,
        'says_import_not_step': 'is not an inference step' in low,
        'says_tier2_scope': 'research-frontier and not claimed here' in low,
        'says_resemblance': 'precisely where definition 2.5 says' in low,
        'says_no_row': 'nothing is filed to row' in low,
        'says_strict_loose': 'strict: 0 of 6' in low and 'loose: 4 of 6' in low,
        'says_price': 'from 5 of 6 to 4 of 6' in low,
        'says_both_sides': 'the same object on both sides' in low,
        'says_smallest': 'tier-2 form of the barrier' in low,
        'says_blocker': 'not the parked lane' in low,
        'says_channel': 'bright channel' in low,
        'says_one_of_three': 'one of three is not the negation' in low,
        'says_r20': 'discovered, not imposed' in low,
        'says_guard': 'refuses rather than guesses' in low,
        'says_nothing_deposits': 'nothing deposits' in low,
        'says_h2': 'h2 where the deposit left it' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:**')
    for k, v in says.items():
        rec('      %-26s %s' % (k, v))
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        rec('  ### run record : %s' % run_clock.write(D, 'b407_desk_notes', LINES))
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
        rec('  ### run record : %s' % run_clock.write(D, 'b407_desk_notes', LINES))
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
        write_bytes(TABLE, new)
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
            rec('  ### run record : %s' % run_clock.write(D, 'b407_desk_notes', LINES))
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
    nb = bank(Q, rownum, kok)

    rec()
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### ROWS OF FACES_LEDGER WRITTEN : 0. ### CORR ROW '
        '%d. ### KEY %s. ### BANK %d LINES.**'
        % (Q['items'], Q['closed'], rownum, 'PASS' if kok else 'FAIL', nb))
    bar('=')
    # ### **THE RUN RECORD IS READ FROM THE RUN, NEVER FROM A DIRECTORY LISTING** (b406, and the
    # ### reason `run_clock.latest` exists). ### The path this run wrote is PRINTED here.
    p = run_clock.write(D, 'b407_desk_notes', LINES)
    print(chr(10) + '  ### THIS RUN WROTE : %s   (stamp %s)'
          % (os.path.basename(p), run_clock.read_stamp(p)))
    lp, ls, note = run_clock.latest(D, 'b407_desk_notes')
    print('  ### AND THE GUARD AGREES : %s   (%s ; %s)'
          % (os.path.basename(lp or '-'), ls, note))
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
