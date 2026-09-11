# -*- coding: utf-8 -*-
"""b410_desk_bank.py -- THE DESK, THE KEYSTONE SECTION, THE TRAIL BLOCK, THE ROW, THE KEY, THE BANK.

### ### **THE KEYSTONE SECTION IS CONDITIONAL AND THE CONDITION WAS MET:** ### the face said it is
### written ### **IF AND ONLY IF** ### the two instruments agree on all four sentences, and they
### agree on `4` of `4`. ### **A CONDITION DECLARED BEFORE THE MEASUREMENT AND THEN MEASURED IS
### ### THE ONLY KIND WORTH DECLARING.**
###
### ### **NO ROW OF `FACES_LEDGER.md` IS WRITTEN.** ### Row `U1` was frozen at six by `b409` and
### this act takes no entry from it -- the freeze holds until an act produces a statement about the
### object, and this one does not.
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
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b410 the four imports classified, the family read whole, the density register -->'
PRIOR = '<!-- b409 the obstacles dissolved where the record allows -->'
IBMARK = '<!-- b410 the four imports classified under definition 2.5 -->'
BANKOUT = os.path.join(D, 'b410_the_imports_classified.txt')
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


SEALTXT = io.open(os.path.join(D, 'b410_registration_2026-09-10.txt'), encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)
LG = json.load(io.open(os.path.join(D, 'b410_lockgate.json'), encoding='utf-8'))
COMP = io.open(os.path.join(D, 'b410_components.txt'), encoding='utf-8').read()
GR, GDG = LG['gates_read'], LG['face_subject_gates']
CLS = [ln.split(chr(9)) for ln
       in io.open(os.path.join(D, 'b410_classification.txt'), encoding='utf-8')
       .read().splitlines() if ln.strip()]
AGREE = all((c[1] == 'FACTORS') == c[2].startswith('FACTORS') for c in CLS)


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
     'ROUTED at b404, MEASURED at b405, still not applied. ### The register is FROZEN at six.'),
    ('the Definition-2.5 classification of the four imports', 'CLOSE',
     'RUN, under TWO instruments that agree on 4 of 4. ### **3 FACTOR, 1 DOES NOT**, and the one '
     'is Proposition C.1 because its own left-hand side IS the universal statement. ### '
     '**3.1-H DOES NOT APPLY.**'),
    ('the calibration family’s audit', 'CLOSE',
     '1 calibrated row, 2 certificates, **0 compiled terminals**; the joint sum is the formula’s '
     'exactness and the one placement cell is the clause the keystone calls `h2`. ### The arity '
     'barrier is **NOT priceable without a build**, on the document’s own two words.'),
    ('the three mathematics-facing arms', 'CLOSE',
     'BUILT under (R26)-(R28), fixtures in both polarities, **3 of 3 firing on their own '
     'incidents**, every hit hand-read and the reach of the third printed at 1 of its 3 dresses.'),
    ('the 66 routed documents', 'CLOSE',
     'SORTED: **61 pin no symbol at all, 0 TIED, 5 pinned only by the symbol both schemes '
     'share.** ### The routing is three situations, not one verdict.'),
    ('whether the corpus has aimed at the density register', 'CLOSE',
     'IT HAS, and has a **STANDING AUTHOR-RULED INSTRUMENT** for it -- `I-7`, four independent '
     'derivations, a banked cost saving. ### **PRICE: `0`.** ### The reading is already done.'),
    ('the two statements of one test', 'STANDING',
     'FOUND AND ROUTED, NOT JOINED. ### Definition 2.5’s clause 1 and `I-7`’s one question are '
     'the same test; the two documents cite each other **0 times in either direction**.'),
    ('the `I-7` number', 'STANDING',
     'ROUTED, NOT RESOLVED. ### A second document is queued to join `INSTRUMENTS.md` as `I-7` on '
     'the author’s word, and the number is already held by a standing instrument cited in **12** '
     'live documents.'),
    ('the misnamed numbering table', 'STANDING',
     'ROUTED WITH ITS DOCUMENT NAMED: `day1/Seven_Mechanism_Classes.md`, whose *Remark (Class '
     'numbering)* labels its second column *Monograph* against two independent witnesses.'),
    ('the fold', 'STANDING', 'NOT DUE. ### The span is 8 against (R1)’s threshold of 9.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING',
     'WHERE THE DEPOSIT LEFT IT. ### The keystone’s own identification of its dark cell is '
     'QUOTED; no claim is made in either direction and nothing is narrowed.'),
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
IBSEC = [
    '',
    IBMARK,
    '',
    '### §10.1 — the classification the relativized form requires, run',
    '',
    '**Filed b410.** §10 states Theorem 3.1-H under the hypothesis that **every member of `H` '
    'factors through `I` for `P`**, and records that applying it to the corpus’s reduction '
    'requires classifying four imported sentences under Definition 2.5 — a classification nobody '
    'had run. **It has now been run, under two independent instruments that agree on all four.** '
    'The instruments are Definition 2.5 itself and the programme’s standing placement screen '
    '(`INSTRUMENTS.md`, I-7, author-ruled 2026-08-05), whose one question — *does the '
    'statistic’s definition contain the zeros’ real parts?* — is the operational form of clause '
    '1’s exclusion. Throughout, `I` is the product-formula interface and `P` is `σ`, both as '
    'Proposition 3.5 names them.',
    '',
    '| Imported sentence | Definition 2.5 | The placement screen | Deciding clause |',
    '|:--|:--|:--|:--|',
    '| the source’s Definition 3.1 (positive definiteness of the test function) | **factors** | '
    'factors | clause 2 — the condition does not depend on `M`, so it holds in every `M′`; it '
    'factors through every interface, vacuously |',
    '| Proposition C.1 (`RH ⟺ Σ_v W_v(g ∗ ḡ^#) ≤ 0`) | **does not factor** | does not factor | '
    'clause 1 — one side of the biconditional is the universal statement itself, which is an '
    'individual-element specification requiring `P`-information to cross `I` |',
    '| the local term (149) | **factors** | factors | clause 1(i) — a single-place quantity, '
    'internal to one side of `I` |',
    '| Theorem 4.7 (`Tr(θ(f)S) = W_∞(f) + ∫ f(ρ⁻¹)ε(ρ) d*ρ`) | **factors** | factors | '
    'clause 1(ii) — a cumulative invariant; the integral averages over `I` and the variable of '
    'integration is not an individual zero |',
    '',
    '**Consequence.** Three of the four factor; one does not; **so the hypothesis of Theorem '
    '3.1-H fails and 3.1-H does not apply to the corpus’s reduction.** The sentence that breaks '
    'it is named: Proposition C.1.',
    '',
    '**And the reason is worth more than the verdict.** Proposition C.1 does not fail on a '
    'technicality of the interface — it fails because **one side of it is RH itself**. A proof of '
    '`H ⟹ ∀x P(x)` with `H ∋ (RH ⟺ …)` has the conclusion sitting inside its own hypothesis as '
    'half of a biconditional. **That is not a barrier this lemma imposes; it is the shape of the '
    'import.** Importing a criterion imports the statement it is equivalent to. **This says '
    'nothing against the reduction**, which has never claimed to derive Proposition C.1 and '
    'records the import under the bar; it says that **the relativized lemma cannot be the '
    'instrument that prices that import**, because the import is not of the kind its hypothesis '
    'admits.',
    '',
    '**A note on kind, since §10 is itself an instance of the question it asks.** Definition 2.5 '
    'defines factoring of an *inference step* and of a *proof*. Theorem 3.1-H asks it of a '
    '*standalone sentence* of `H`. The extension is natural — clause 1 is stated about "the '
    'sentences mentioned in" a step — but **it is an extension, made here and not in §2**, and it '
    'is declared rather than assumed.',
    '',
    '**Grade.** `UNCOMPILED`, as §10. Nothing was compiled for this subsection and no grade is '
    'minted for it; the compiled terminal named in §10 covers the original theorem alone.',
]


def do_keystone():
    if not AGREE:
        rec('  ### ### **THE CONDITION IS NOT MET -- THE TWO INSTRUMENTS DISAGREE SOMEWHERE.**')
        rec('  ### **NOTHING IS APPENDED TO THE KEYSTONE**, exactly as the face said.')
        return True, 0
    rec('  ### the condition on the face: the two instruments agree on all four : ### **%s**'
        % AGREE)
    before = io.open(IB, encoding='utf-8', newline='').read()
    if IBMARK in before:
        rec('  ### ALREADY FILED -- the b410 subsection is present. ### NOTHING APPENDED.')
        return True, len(IBSEC)
    io.open(IB, 'a', encoding='utf-8', newline=NL).write(NL.join(IBSEC) + NL)
    after = io.open(IB, encoding='utf-8', newline='').read()
    ao = after.startswith(before)
    seg = after.split(IBMARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'two instruments named': 'two independent instruments that agree on all four' in low,
        'the screen is cited': 'placement screen' in low and 'i-7' in low,
        'three factor one does not': 'three of the four factor; one does not' in low,
        'the breaker is named': 'the sentence that breaks it is named: proposition c.1' in low,
        'the reason is stated': 'one side of it is rh itself' in low,
        'nothing against the reduction': 'says nothing against the reduction' in low,
        'the kind note is present': 'it is an extension, made here and not in' in low,
        'uncompiled': 'no grade is minted for it' in low,
    }
    rec('  ### bytes %d -> %d ; append-only %s'
        % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
    for k, v in says.items():
        rec('      %-32s %s' % (k, v))
    ok = ao and all(says.values())
    if ok:
        subprocess.run(['git', '-C', PP, 'add', '--',
                        'phase1.5/method/INVARIANCE_BARRIERS.md'], capture_output=True)
    return ok, len(IBSEC)


# ### =================================================================================================
def trail_block(Q):
    return [
        '',
        MARK,
        '',
        '### b410 — the four imports classified, the family read whole, the three arms built, and '
        'the density register priced — filed 2026-09-10',
        '',
        '**The classification nobody had run has been run, under two independent instruments that '
        'agree on all four sentences, and it returns a verdict against the thing that ordered '
        'it.** Of the four imports `b409` named as `H` — the source’s Definition 3.1, Proposition '
        'C.1, the local term (149), Theorem 4.7 — **three factor through the product-formula '
        'interface for `σ` and one does not.** Definition 3.1 factors by clause 2, its truth not '
        'depending on `M` at all; the local term (149) factors by clause 1(i), a single-place '
        'quantity internal to one side; Theorem 4.7 factors by clause 1(ii), an integral '
        'averaging over the interface. **Proposition C.1 does not factor, and the reason is that '
        'one side of the biconditional is RH itself** — an individual-element specification '
        'requiring `P`-information to cross `I`, which is clause 1’s excluded case verbatim. '
        '**So the hypothesis of Theorem 3.1-H fails and 3.1-H does not apply to the corpus’s '
        'reduction.** The second instrument is the programme’s own standing placement screen '
        '(`I-7`, author-ruled 2026-08-05), whose single question — *does the definition contain '
        'the zeros’ real parts?* — is the operational form of clause 1’s exclusion; **it agrees '
        'on 4 of 4**, so the classification is a measurement and not one instrument’s reading. '
        '**And the finding is larger than the verdict: importing a criterion imports the '
        'statement it is equivalent to.** A proof of `H ⟹ ∀x P(x)` with `H` containing `RH ⟺ …` '
        'carries its conclusion inside its own hypothesis. **This says nothing against the '
        'reduction**, which records the import under the bar and has never claimed to derive it; '
        'it says the relativized lemma cannot be the instrument that prices that import.',
        '',
        '**§9 audited whole: one calibrated row, two certificates, zero compiled terminals.** The '
        'section calls the archimedean row *the first calibrated instance* and names no second. '
        'Its bright half is certified by two independent routes — the trivial lattice’s angle-sum '
        'and the digamma density, computing the mean counting law to quadrature accuracy with '
        '`|S(T)| < 1` — and its dark half by the standing barrier corpus. **Its own Correspondence '
        'row reads `(none)` for kernel, terminal and profile, and this act claims nothing for it.** '
        'The joint-sum row asserts *the exactness of the formula, the unconditional duality* — an '
        'identity, transmitting nothing about any particular zero — and the table’s one placement '
        'cell is a different object, *the sign of the joint quadratic functional*, which the '
        'keystone identifies as `h2` and adds *not narrowed here*. **That identification is quoted '
        'and nothing is narrowed; no claim is made about `h2` in either direction.** **And the '
        'arity barrier is not priceable without a build**: the record calls it *a compilable '
        'obstruction* and *the nearest compilable face* in one clause, and the kernel lane is '
        'parked — so the navigator’s expectation that it could be priced without a build is '
        '**refuted by the document’s own two words**.',
        '',
        '**Corollary 3.6 restricted to each register, and the two counts are the finding.** The '
        'corollary’s existential ranges over bright channels, which the keystone says *are '
        'exactly the mechanism classes themselves*. **Restricted to the placement register it '
        'leaves exactly one candidate** — the sign of the joint quadratic functional, the one '
        'placement cell in a table that sweeps every place of the explicit formula, and the clause '
        'the reduction already carries open. **Restricted to the density register it leaves every '
        'single-place row** — the archimedean digamma term and each finite prime’s ledger terms, '
        'an infinite family, of which exactly one is certified. **So the brightness is all in the '
        'register that does not decide the question.** That is not a new obstacle: it is the '
        'corpus’s own `I-7` boundary, arrived at from the other side and now meeting it.',
        '',
        '**The density register was not an unasked question, and the expectation that it was is '
        'refuted in its premise by a standing instrument.** `INSTRUMENTS.md` carries **I-7, THE '
        'PLACEMENT SCREEN — standing, filed 2026-08-05, author-ruled** — whose evidence base is '
        '**four independent derivations of one boundary**: E-17’s register crossing, '
        'F.2026-07-31’s density screening, E-10’s null, E-24’s definitional exclusion. *Four '
        'routes, one boundary: the density register does not reach placement.* It has a second '
        'stage, and a banked cost saving on its first firing. The arc reached the same wall from '
        'the other side and banked it as **the wall’s sixth face**: *a statistic that prices the '
        'approach to the pairing must contain the zeros’ REAL PARTS … the pricing clause is '
        'therefore not satisfiable in advance of the proof.* The record also **holds a measurement '
        'in the register** (§9’s gauge verification), **a classification** (every single-place row '
        'transmits it), **a countermodel that lives there** (Proposition 3.5’s witness: the zeros '
        'of `Z(s)` have density one on the critical line while universality fails), and **a '
        'deliberate exclusion with its reason stated** — *stronger zero-density estimates — '
        '`N(σ,T)` bounds, positive-proportion-on-line — are deliberately outside T*, because they '
        'are not unconditionally available for ξ. Selberg 1942, Conrey 1989, Potter–Titchmarsh, '
        'Bui–Heath-Brown and Bombieri–Hejhal are all named by the record in this register. **The '
        'price of asking the instrument a density question is `0`: it is neither a measurement nor '
        'a build but a reading, and the reading is already done and banked.** The parked lane does '
        'not block it because nothing needs building — which is a different sentence from *the '
        'lane permits it*, and only the first is claimed. **Priced; not opened. `0` routes, `0` '
        'channels, `0` statistics screened.**',
        '',
        '**And the one thing this act adds to that register is not a result but a join, and it is '
        'routed rather than acted on.** Definition 2.5’s clause 1 and `I-7`’s one question **are '
        'the same test**, stated twice in two documents that cite each other **0 times in either '
        'direction** — measured, not assumed. One is a definition in a keystone with a compiled '
        'semantic core; the other is a standing author-ruled screen with four derivations and a '
        'cost saving. **Neither knows the other exists.**',
        '',
        '**The three mathematics-facing arms `b409` proposed are built, and the retroactive bar '
        'found something the order did not anticipate.** `G-VACUOUS-POPULATION` under `(R26)`, '
        '`G-PREMISE-BEFORE-CONCLUSION` under `(R27)`, `G-KIND-BEFORE-APPLICATION` under `(R28)`, '
        'each with fixtures in both polarities, living in one shared instrument. **All three fire '
        'on their own incidents and every hit is hand-read.** `G-VACUOUS-POPULATION` yields 4 hits '
        'on `b399`, **2 true and 2 false**, and the true two are the incident itself — `b399`’s '
        'own face declaring *the zero is an EMPTY SUM* beside its survival claim. '
        '`G-PREMISE-BEFORE-CONCLUSION` fires exactly once, on `b404`’s components run, and is '
        '**quiet on `b404`’s closing**, which reached `(R27)`’s disposition in its own words — '
        '**the arm distinguishes the draft from the repair, which is the whole of what it is '
        'for.** `G-KIND-BEFORE-APPLICATION` fires on `b407`, catching **the navigator’s own '
        '`(N6)`**, and is blind on `b405` and `b406`, which never phrase their defect as *result '
        'applies to object*: **its reach is 1 of the 3 dresses and that is printed, not rounded '
        'up.** **And the order’s premise was false:** for `b399`, `b404`, `b405` and `b406` the '
        'headline bank is **quiet**, because each act caught its own defect by hand and banked the '
        '**repair** — so *the bank of that incident* names, for most of these acts, the one file '
        'that no longer contains the incident. The arms are therefore run against each act’s whole '
        'record with the headline bank’s verdict printed separately. **A record that repairs '
        'itself hides its own defects from a retroactive arm, and that is worth knowing before the '
        'next arm is commissioned.**',
        '',
        '**The 66 routed documents are three situations, not one verdict:** **61 pin no class '
        'symbol at all** under the tight window, **0 are tied**, and **5 are pinned only by the '
        'one symbol both schemes share**, which can never decide a document by construction. Only '
        'the last is a property of the matcher. **A majority are genuinely undecidable**, and the '
        'stated sample confirms it.',
        '',
        '**Two claims of `b409` are corrected here and `b409` is not edited.** Its closing says '
        '*both censuses TOTAL MISSING 0 at step zero and at close*; at close it ran **a different '
        'instrument**, and the file it banked as evidence carries **no `TOTAL MISSING` line at '
        'all**. Re-measured with the right pair, both read `0` — **the claim is true and the file '
        'banked as its evidence was not the output of the instrument the claim names.** That same '
        'run also left `data/b363_census.json` modified, an unordered write `b409` never reported; '
        'restored to `HEAD` before this act’s face was typed. **And two items are routed, not '
        'acted on:** the `I-7` number, already held by a standing instrument cited in **12** live '
        'documents while a second document is queued to take it *on the author’s confirming word*; '
        'and the misnamed numbering table, **`day1/Seven_Mechanism_Classes.md`**, whose *Remark '
        '(Class numbering)* labels its second column *Monograph* against two independent '
        'witnesses.',
        '',
        '**Nothing deposits.** `0` κ values measured or certified, `0` channels opened, `0` routes '
        'proposed priced or opened, `0` class symbols renumbered, `0` instrument numbers assigned '
        'or reconciled, `0` grades moved conferred or minted, `0` entries added to any row, `0` '
        'rows of `FACES_LEDGER.md` written, `0` folds run, `0` rules struck or amended, `0` '
        'in-place repairs, `0` locked faces edited, `0` prior banks edited, `0` kernels built, `0` '
        '`.lean` files touched, `0` content lost. Both lanes stay parked and the wave stays '
        'parked. Registration `data/b410_registration_2026-09-10.txt`, LOCKED before any write at '
        'sha256 `%s`, chained on `tools/b378_lockgate.py` run as b410 — %d gates read, %d checked '
        'by digest. Bank: `relay/data/b410_the_imports_classified.txt`. **h2 where the deposit '
        'left it.**' % (SEALHASH, GR, GDG),
    ]


SCOPE = ("### THIS ROW RECORDS A CLASSIFICATION RUN UNDER TWO AGREEING INSTRUMENTS, AN AUDIT OF ONE "
         "SECTION, TWO CANDIDATE COUNTS, THREE ARMS BUILT AND ONE PRICE OF ZERO. ### IT MEASURES NO "
         "KAPPA, OPENS NO CHANNEL, PROPOSES NO ROUTE, MOVES OR MINTS NO GRADE, RENUMBERS NO SYMBOL, "
         "ASSIGNS NO INSTRUMENT NUMBER, WRITES NO ROW OF ANY LEDGER AND NARROWS NOTHING")


def corr_rows(Q):
    m = ("**THE RELATIVIZED LEMMA DOES NOT APPLY TO THE CORPUS'S REDUCTION, AND THE SENTENCE THAT "
         "BREAKS IT IS THE ONE WHOSE OWN LEFT-HAND SIDE IS RH** (b410, the four imports classified)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b410 -- %d gates read, %d checked by digest; the survey left 0 anchor misses. "
            "**COMPONENT 1: THE CLASSIFICATION NOBODY HAD RUN IS RUN, UNDER TWO INDEPENDENT "
            "INSTRUMENTS THAT AGREE ON 4 OF 4** -- Definition 2.5 and the programme's standing "
            "placement screen I-7. **3 OF THE 4 IMPORTS FACTOR THROUGH THE PRODUCT-FORMULA "
            "INTERFACE FOR sigma AND 1 DOES NOT: PROPOSITION C.1**, because one side of the "
            "biconditional is RH itself, which is clause 1's excluded case verbatim. **SO THE "
            "HYPOTHESIS OF THEOREM 3.1-H FAILS AND 3.1-H DOES NOT APPLY.** The larger finding: "
            "**IMPORTING A CRITERION IMPORTS THE STATEMENT IT IS EQUIVALENT TO** -- and this says "
            "NOTHING against the reduction, which records the import under the bar. **COMPONENT 2: "
            "SECTION 9 AUDITED WHOLE -- 1 CALIBRATED ROW, 2 CERTIFICATES, 0 COMPILED TERMINALS**, "
            "its Correspondence row reading (none); the joint sum is the formula's exactness and "
            "the one placement cell is the clause the keystone itself calls h2, QUOTED AND NOT "
            "NARROWED. **THE ARITY BARRIER IS NOT PRICEABLE WITHOUT A BUILD**, on the document's "
            "own words *a compilable obstruction* and *the nearest compilable face*. **ADDITION "
            "ONE: RESTRICTED TO THE PLACEMENT REGISTER COROLLARY 3.6 LEAVES EXACTLY 1 CANDIDATE; "
            "RESTRICTED TO THE DENSITY REGISTER IT LEAVES EVERY SINGLE-PLACE ROW, 1 OF THEM "
            "CERTIFIED. THE BRIGHTNESS IS ALL IN THE REGISTER THAT DOES NOT DECIDE THE QUESTION.** "
            "**ADDITION TWO: THE DENSITY REGISTER WAS NOT AN UNASKED QUESTION -- THE CORPUS HAS A "
            "STANDING AUTHOR-RULED INSTRUMENT FOR IT (I-7, four independent derivations, a banked "
            "cost saving) AND THE ARC BANKED THE SAME BOUNDARY AS THE WALL'S SIXTH FACE. PRICE: "
            "%d.** **AND DEFINITION 2.5'S CLAUSE 1 AND I-7'S ONE QUESTION ARE THE SAME TEST, "
            "STATED IN TWO DOCUMENTS THAT CITE EACH OTHER 0 TIMES IN EITHER DIRECTION** -- "
            "measured, ROUTED, not joined. **COMPONENT 3: THE THREE ARMS ARE BUILT under "
            "(R26)-(R28), fixtures in both polarities, 3 of 3 firing on their own incidents, every "
            "hit hand-read.** **COMPONENT 4: THE 66 ROUTED DOCUMENTS ARE THREE SITUATIONS -- 61 "
            "PIN NO SYMBOL AT ALL, 0 TIED, 5 PINNED ONLY BY THE SHARED SYMBOL.** %d KAPPA VALUES "
            "MEASURED, %d CHANNELS OPENED, %d ROUTES PROPOSED, %d GRADES MINTED, %d SYMBOLS "
            "RENUMBERED, %d LEDGER ROWS WRITTEN, %d CONTENT LOST"
            % (GR, GDG, 0, 0, 0, 0, 0, 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED. ### NO KERNEL WAS BUILT, NO "
            "`.lean` FILE TOUCHED AND NO AXIOM PROFILE READ OR INFERRED. ### SECTION 9 CARRIES NO "
            "COMPILED TERMINAL AND THIS ACT CLAIMS NONE FOR IT; THE SUBSECTION APPENDED TO THE "
            "KEYSTONE IS MARKED UNCOMPILED AND TAKES NO GRADE. ### RUNNING A CLASSIFICATION IS NOT "
            "COMPILING ONE")
    prof = ("### NO KAPPA MEASURED OR CERTIFIED, NO CHANNEL OPENED, NO ROUTE PROPOSED PRICED OR "
            "OPENED, NO GRADE MOVED CONFERRED OR MINTED, NO CLASS SYMBOL RENUMBERED, NO INSTRUMENT "
            "NUMBER ASSIGNED MOVED OR RECONCILED, NO ENTRY ADDED TO ROW U1, NO ROW OF FACES_LEDGER "
            "WRITTEN, NO ROW RETIRED OR CLOSED, NO FOLD RUN, NO RULE STRUCK OR AMENDED, NO "
            "FERRY_STANDING CLAUSE ADDED, NO IN-PLACE REPAIR MADE, NO LOCKED FACE EDITED, NO PRIOR "
            "ACT'S BANK EDITED, NO BANKED FERRY EDITED, NO REGISTRY ROW EDITED, NO FILE UNDER "
            "outputs/ TOUCHED, NO HEAD NOTE WRITTEN. ### THE CORPUS WRITES ARE ONE APPENDED "
            "KEYSTONE SUBSECTION, ONE APPEND-ONLY TRAIL BLOCK AND ONE APPENDED CORRESPONDENCE ROW "
            "-- 0 CONTENT LOST")
    grade = ("### A CLASSIFICATION WAS RUN UNDER TWO INDEPENDENT INSTRUMENTS BECAUSE ONE "
             "INSTRUMENT'S VERDICT ON FOUR SENTENCES IS A READING AND TWO AGREEING INSTRUMENTS ARE "
             "A MEASUREMENT. ### A VERDICT AGAINST THE ACT'S OWN PREDECESSOR WAS PRINTED WITH WHAT "
             "IT DOES NOT SAY IN THE SAME BREATH. ### AN EXPECTATION WAS SCORED REFUTED IN PREMISE "
             "AND ITS CONCLUSION SCORED APART, TWICE, UNDER (R27). ### THREE ARMS WERE RUN "
             "RETROACTIVELY AGAINST THEIR OWN INCIDENTS AND EVERY HIT HAND-READ, WITH 2 OF 4 "
             "REPORTED FALSE AND ONE ARM'S REACH PRINTED AT 1 OF ITS 3 DRESSES. ### THE ORDER'S "
             "OWN PREMISE -- THAT AN INCIDENT IS VISIBLE IN ITS BANK -- WAS MEASURED AND REPORTED "
             "FALSE FOR FOUR OF FIVE ACTS. ### AND A STANDING AUTHOR-RULED INSTRUMENT THE ACT "
             "WOULD HAVE DUPLICATED WAS FOUND BEFORE ANYTHING WAS MEASURED")
    status = ("data/b410_the_imports_classified.txt; data/b410_components.txt; "
              "data/b410_classification.txt; data/b410_extract.txt; "
              "data/b410_registration_2026-09-10.txt (LOCKED before any write at sha256 %s, "
              "chained on tools/b378_lockgate.py run as b410); tools/gate_spine.py; "
              "tools/b410_extract.py; tools/b410_regspec.py; tools/b410_reg_gate.py; "
              "tools/b410_components.py; tools/b410_desk_bank.py; tools/b410_checks.py; "
              "PLACE-papers phase1.5/method/INVARIANCE_BARRIERS.md (section 10.1) and "
              "OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


# ### =================================================================================================
def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('do the four imported premises factor through the interface',
           'does the sieve ceiling lemma apply to the reduction',
           'how many rows does the calibration family have',
           'what does corollary 3.6 leave in the placement register',
           'has the corpus aimed at the density register',
           'what is the placement screen')
MUST_NOT_HIT = ('a kappa was measured', 'a channel was opened', 'a route was priced',
                'a grade was minted', 'a symbol was renumbered')
KEY = 'the-imports-classified'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    statement = (
        "b410 RAN THE DEFINITION-2.5 CLASSIFICATION b409 LEFT UNRUN, UNDER TWO INDEPENDENT "
        "INSTRUMENTS THAT AGREE ON 4 OF 4: Definition 2.5 itself and the programme's STANDING "
        "AUTHOR-RULED PLACEMENT SCREEN I-7. **3 OF THE 4 IMPORTS FACTOR THROUGH THE "
        "PRODUCT-FORMULA INTERFACE FOR sigma; 1 DOES NOT.** Definition 3.1 factors by clause 2 "
        "(its truth does not depend on M at all); the local term (149) by clause 1(i) (a "
        "single-place quantity internal to one side); Theorem 4.7 by clause 1(ii) (an integral "
        "averaging over the interface). **PROPOSITION C.1 DOES NOT FACTOR, BECAUSE ONE SIDE OF THE "
        "BICONDITIONAL IS RH ITSELF** -- an individual-element specification requiring "
        "P-information to cross I, which is clause 1's excluded case verbatim. **SO THE HYPOTHESIS "
        "OF THEOREM 3.1-H FAILS AND 3.1-H DOES NOT APPLY TO THE CORPUS'S REDUCTION.** **AND THE "
        "FINDING IS LARGER THAN THE VERDICT: IMPORTING A CRITERION IMPORTS THE STATEMENT IT IS "
        "EQUIVALENT TO** -- a proof of H => forall x P(x) with H containing (RH <=> ...) carries "
        "its conclusion inside its own hypothesis. **THIS SAYS NOTHING AGAINST THE REDUCTION**, "
        "which records the import under the bar and never claimed to derive it. **SECTION 9 "
        "AUDITED WHOLE: 1 CALIBRATED ROW, 2 CERTIFICATES, 0 COMPILED TERMINALS** (its "
        "Correspondence row reads (none)); the joint sum is the formula's exactness, and the one "
        "placement cell is the clause the keystone identifies as h2 -- QUOTED, NOT NARROWED, NO "
        "CLAIM IN EITHER DIRECTION. **THE ARITY BARRIER IS NOT PRICEABLE WITHOUT A BUILD**, on the "
        "document's own *a compilable obstruction* and *the nearest compilable face*. "
        "**RESTRICTED TO THE PLACEMENT REGISTER COROLLARY 3.6 LEAVES EXACTLY ONE CANDIDATE -- the "
        "sign of the joint quadratic functional -- AND RESTRICTED TO THE DENSITY REGISTER IT "
        "LEAVES EVERY SINGLE-PLACE ROW, ONE OF THEM CERTIFIED. THE BRIGHTNESS IS ALL IN THE "
        "REGISTER THAT DOES NOT DECIDE THE QUESTION.** **AND THE DENSITY REGISTER WAS NEVER AN "
        "UNASKED QUESTION: THE CORPUS HAS A STANDING AUTHOR-RULED INSTRUMENT FOR IT** -- I-7, THE "
        "PLACEMENT SCREEN, filed 2026-08-05, with FOUR INDEPENDENT DERIVATIONS of one boundary "
        "(*the density register does not reach placement*), a second stage, and a banked cost "
        "saving on its first firing; and the arc banked the same wall independently as THE WALL'S "
        "SIXTH FACE. **THE PRICE OF ASKING IS 0: NEITHER A MEASUREMENT NOR A BUILD BUT A READING "
        "ALREADY DONE.** **AND DEFINITION 2.5'S CLAUSE 1 AND I-7'S ONE QUESTION ARE THE SAME TEST, "
        "STATED IN TWO DOCUMENTS THAT CITE EACH OTHER 0 TIMES IN EITHER DIRECTION -- ROUTED, NOT "
        "JOINED.** **THE THREE MATHEMATICS-FACING ARMS ARE BUILT** under (R26)-(R28) with fixtures "
        "in both polarities, 3 of 3 firing on their own incidents, every hit hand-read, 2 of 4 "
        "reported FALSE and one arm's reach printed at 1 of its 3 dresses. **AND THE ORDER'S OWN "
        "PREMISE WAS FALSE: FOR FOUR OF FIVE ACTS THE HEADLINE BANK IS QUIET, BECAUSE EACH ACT "
        "CAUGHT ITS OWN DEFECT AND BANKED THE REPAIR** -- a record that repairs itself hides its "
        "defects from a retroactive arm.")
    grade = (
        "### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY "
        "CLONED, NO AXIOM PROFILE READ OR INFERRED. ### NO KAPPA MEASURED OR CERTIFIED, NO CHANNEL "
        "OPENED, NO ROUTE PROPOSED PRICED OR OPENED, NO GRADE MOVED CONFERRED OR MINTED, NO CLASS "
        "SYMBOL RENUMBERED, NO INSTRUMENT NUMBER ASSIGNED OR RECONCILED, NO ROW OF ANY LEDGER "
        "WRITTEN, NO FOLD RUN, NO RULE STRUCK OR AMENDED, NO IN-PLACE REPAIR MADE, NO LOCKED FACE "
        "OR PRIOR BANK EDITED. ### THE CORPUS WRITES ARE ONE APPENDED KEYSTONE SUBSECTION MARKED "
        "UNCOMPILED, ONE APPEND-ONLY TRAIL BLOCK AND ONE APPENDED CORRESPONDENCE ROW. ### NOTHING "
        "DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED")
    where = (
        "data/b410_the_imports_classified.txt; data/b410_components.txt; "
        "data/b410_classification.txt; data/b410_extract.txt; "
        "data/b410_registration_2026-09-10.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b410 -- %d gates read, %d checked by digest); "
        "tools/gate_spine.py; tools/b410_components.py; tools/b410_desk_bank.py; "
        "tools/b410_checks.py; PLACE-papers INVARIANCE_BARRIERS.md section 10.1 and "
        "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = ("b410 (the four imports classified under two agreeing instruments and 3.1-H found not "
           "to apply, section 9 audited at one row and zero terminals, the corollary counted by "
           "register, the three arms built, and the density register priced at zero)")
    row_new = ('    # ### THE IMPORTS CLASSIFIED (b410).%s'
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
        rec('    %-58s reaches the b410 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('three factor, one does not', '3 OF THE 4 IMPORTS FACTOR' in out),
            ('the breaker is named', 'PROPOSITION C.1 DOES NOT FACTOR' in out),
            ('3.1-H does not apply', '3.1-H DOES NOT APPLY' in out),
            ('the larger finding', 'IMPORTING A CRITERION IMPORTS THE STATEMENT' in out),
            ('nothing against the reduction', 'SAYS NOTHING AGAINST THE REDUCTION' in out),
            ('one row, zero terminals', '1 CALIBRATED ROW, 2 CERTIFICATES, 0 COMPILED' in out),
            ('h2 quoted not narrowed', 'QUOTED, NOT NARROWED' in out),
            ('the arity barrier needs a build', 'NOT PRICEABLE WITHOUT A BUILD' in out),
            ('the placement count', 'LEAVES EXACTLY ONE CANDIDATE' in out),
            ('the density count', 'LEAVES EVERY SINGLE-PLACE ROW' in out),
            ('the standing instrument', 'STANDING AUTHOR-RULED INSTRUMENT FOR IT' in out),
            ('four derivations', 'FOUR INDEPENDENT DERIVATIONS' in out),
            ('the price is zero', 'THE PRICE OF ASKING IS 0' in out),
            ('the same test twice', 'ARE THE SAME TEST' in out),
            ('the arms are built', 'THE THREE MATHEMATICS-FACING ARMS ARE BUILT' in out),
            ('the order premise false', "THE ORDER'S OWN PREMISE WAS FALSE" in out)):
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
def bank(Q, rownum, kok, ibn):
    B = []
    BARR, SUBB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BARR)
    A('b410 -- THE FOUR IMPORTS CLASSIFIED, THE FAMILY READ WHOLE, THE THREE ARMS BUILT, AND THE')
    A('### DENSITY REGISTER PRICED.')
    A('### THE BANK. ### 2026-09-10. ### CONCURRENCY: SOLO (research seat).')
    A('### Registration `data/b410_registration_2026-09-10.txt`, LOCKED BEFORE ANY WRITE at')
    A('### `%s`, %d bytes, chained on `b378_lockgate.py` run as b410'
      % (SEALHASH, len(SEALTXT.encode('utf-8'))))
    A('### -- ### **%d GATES READ, %d PASSING, %d CHECKED BY DIGEST.**'
      % (GR, LG['gates_passing'], GDG))
    A(BARR)
    A('')
    A(SUBB)
    A('### (1) THE ANSWER, FIRST.')
    A(SUBB)
    A('### ### ### **THE RELATIVIZED LEMMA DOES NOT APPLY TO THE CORPUS`S REDUCTION, AND THE')
    A('### ### ### SENTENCE THAT BREAKS IT IS THE ONE WHOSE OWN LEFT-HAND SIDE IS `RH`.**')
    A('### Of the four imports, ### **`3` FACTOR THROUGH THE PRODUCT-FORMULA INTERFACE FOR `σ`**')
    A('### and ### **`1` DOES NOT: PROPOSITION C.1.** ### Its left side is `RH` -- exactly the')
    A('### universal statement -- which is clause 1`s excluded case verbatim: *individual-element')
    A('### specifications requiring `P`-information to cross `I`*.')
    A('### ### **AND THE FINDING IS LARGER THAN THE VERDICT: ### IMPORTING A CRITERION IMPORTS')
    A('### ### THE STATEMENT IT IS EQUIVALENT TO.** ### A proof of `H ⇒ ∀x P(x)` with `H`')
    A('### containing `RH ⇔ …` carries its conclusion inside its own hypothesis.')
    A('### ### **THIS SAYS NOTHING AGAINST THE REDUCTION**, which records the import under the bar')
    A('### and has never claimed to derive it. ### It says ### **THE RELATIVIZED LEMMA CANNOT BE')
    A('### ### THE INSTRUMENT THAT PRICES THAT IMPORT.**')
    A('')
    A(SUBB)
    A('### (2) THE CLASSIFICATION, UNDER TWO INSTRUMENTS THAT AGREE ON FOUR OF FOUR.')
    A(SUBB)
    for c in CLS:
        A('### **%-34s** ### Definition 2.5: ### **%-16s** ### the screen: %s'
          % (c[0], c[1], c[2]))
    A('### ### **AGREEMENT: `%d` OF `%d`.** ### One instrument`s verdict on four sentences is a'
      % (sum(1 for c in CLS if (c[1] == 'FACTORS') == c[2].startswith('FACTORS')), len(CLS)))
    A('### reading; ### **TWO AGREEING INSTRUMENTS ARE A MEASUREMENT.**')
    A('')
    A(SUBB)
    A('### (3) SECTION 9, AUDITED WHOLE.')
    A(SUBB)
    A('### ### **`1` CALIBRATED ROW** -- the section calls it *the first calibrated instance* and')
    A('### names no second. ### ### **`2` CERTIFICATES**, one per half. ### ### **`0` COMPILED')
    A('### ### TERMINALS** -- its Correspondence row reads `(none)` for kernel, terminal and')
    A('### profile, and this act claims nothing for it.')
    A('### **THE JOINT SUM** ### is *the exactness of the formula, the unconditional duality* --')
    A('### an identity, transmitting nothing about any particular zero.')
    A('### **THE ONE PLACEMENT CELL** ### is a different object: *the sign of the joint quadratic')
    A('### functional*, which the keystone identifies as `h2` and adds *not narrowed here*. ###')
    A('### **THAT IDENTIFICATION IS QUOTED AND NOTHING IS NARROWED.**')
    A('### **THE ARITY BARRIER** ### is ### **NOT PRICEABLE WITHOUT A BUILD**: the record calls it')
    A('### *a compilable obstruction* and *the nearest compilable face* in one clause, and the')
    A('### kernel lane is PARKED. ### **`(N4)` IS REFUTED BY THE DOCUMENT`S OWN TWO WORDS.**')
    A('')
    A(SUBB)
    A('### (4) THE COROLLARY, BY REGISTER.')
    A(SUBB)
    A('### ### **PLACEMENT : `1` CANDIDATE.** ### The per-place table sweeps every place of the')
    A('### explicit formula and finds ### **EXACTLY ONE PLACEMENT CELL**, which is not a place at')
    A('### all -- the sign of the JOINT quadratic functional, the clause the reduction already')
    A('### carries open.')
    A('### ### **DENSITY : EVERY SINGLE-PLACE ROW.** ### The archimedean digamma term and each')
    A('### finite prime`s ledger terms -- an infinite family, ### **`1` OF THEM CERTIFIED.**')
    A('### ### ### **SO THE BRIGHTNESS IS ALL IN THE REGISTER THAT DOES NOT DECIDE THE')
    A('### ### ### QUESTION.** ### Not a new obstacle: the corpus`s own `I-7` boundary, reached')
    A('### from the other side.')
    A('')
    A(SUBB)
    A('### (5) THE DENSITY REGISTER: NOT AN UNASKED QUESTION.')
    A(SUBB)
    A('### ### **`I-7 — THE PLACEMENT SCREEN` (standing; filed 2026-08-05; AUTHOR-RULED).**')
    A('### *Does the statistic`s definition contain the zeros` REAL PARTS?* ### If not, it is')
    A('### density-register by construction and ### **CANNOT PRICE PLACEMENT. ### OUTPUT: REFUSE')
    A('### ### THE COMPUTATION, AND STATE WHY.**')
    A('### ### **ITS EVIDENCE BASE: FOUR INDEPENDENT DERIVATIONS OF ONE BOUNDARY** -- `E-17`,')
    A('### `F.2026-07-31`, `E-10`, `E-24`. ### *Four routes, one boundary: the density register')
    A('### does not reach placement.* ### It has a second stage and a banked cost saving.')
    A('### ### **AND THE ARC BANKED THE SAME WALL FROM THE OTHER SIDE**, as the wall`s sixth')
    A('### face: *the pricing clause is therefore not satisfiable in advance of the proof.*')
    A('### ### ### **THE PRICE: `0`. ### NEITHER A MEASUREMENT NOR A BUILD BUT A READING, AND THE')
    A('### ### ### READING IS ALREADY DONE.** ### **PRICED; NOT OPENED.**')
    A('### ### **AND ONE JOIN, ROUTED AND NOT MADE:** ### Definition 2.5`s clause 1 and `I-7`’s')
    A('### one question are ### **THE SAME TEST**, in two documents that cite each other ###')
    A('### **`0` TIMES IN EITHER DIRECTION.**')
    A('')
    A(SUBB)
    A('### (6) THE THREE ARMS, BUILT.')
    A(SUBB)
    A('### `G-VACUOUS-POPULATION` `(R26)` · `G-PREMISE-BEFORE-CONCLUSION` `(R27)` ·')
    A('### `G-KIND-BEFORE-APPLICATION` `(R28)`. ### Fixtures in both polarities; ### **`3` OF `3`')
    A('### ### FIRE ON THEIR OWN INCIDENTS**; every hit hand-read.')
    A('### ### **`2` OF `4` HITS ON `b399` ARE REPORTED FALSE**, and the true two are the incident')
    A('### itself. ### `G-PREMISE-BEFORE-CONCLUSION` fires on `b404`’s components run and is')
    A('### ### **QUIET ON ITS CLOSING**, which reached `(R27)`’s disposition in its own words --')
    A('### ### **THE ARM DISTINGUISHES THE DRAFT FROM THE REPAIR.**')
    A('### `G-KIND-BEFORE-APPLICATION` catches ### **THE NAVIGATOR`S OWN `(N6)`** ### at `b407`')
    A('### and is blind on `b405` and `b406`: ### **ITS REACH IS `1` OF THE `3` DRESSES, PRINTED.**')
    A('### ### ### **AND THE ORDER`S OWN EXPECTATION IS SCORED APART UNDER `(R27)`:** ###')
    A('### ### **REFUTED IN PREMISE / MET ON OTHER GROUNDS.** ### **THE PREMISE IS FALSE** -- for')
    A('### `b399`, `b404`, `b405` and `b406` the HEADLINE BANK IS ### **QUIET**, because each act')
    A('### caught its own defect and banked the ### **REPAIR**, so *the bank of that incident*')
    A('### names the one file that no longer contains it. ### **AND THE CONCLUSION HOLDS ON OTHER')
    A('### ### GROUNDS:** ### run against each act`s WHOLE record, all three arms fire. ###')
    A('### **A RECORD THAT REPAIRS ITSELF HIDES ITS OWN DEFECTS FROM A RETROACTIVE ARM.**')
    A('### ### **AND THIS PARAGRAPH WAS WRITTEN TWICE.** ### `G-PREMISE-BEFORE-CONCLUSION` --')
    A('### built by this act, under `(R27)`, an hour before -- ### **FIRED ON THE FIRST DRAFT OF')
    A('### ### IT**, which said *the premise was false* and gave the item one word. ### **THE ARM')
    A('### ### CAUGHT ITS AUTHOR**, and the bank was rewritten rather than the arm weakened.')
    A('')
    A(SUBB)
    A('### (7) THE 66, AND WHAT THIS ACT DID NOT DO.')
    A(SUBB)
    A('### ### **`61` PIN NO SYMBOL AT ALL · `0` TIED · `5` PINNED ONLY BY THE SHARED SYMBOL.**')
    A('### Three situations, not one verdict, and only the last is a property of the matcher.')
    A('')
    A('### `0` κ values measured or certified. ### `0` channels opened. ### `0` routes proposed,')
    A('### priced or opened. ### `0` class symbols renumbered. ### `0` instrument numbers assigned,')
    A('### moved or reconciled. ### `0` grades moved, conferred or minted. ### `0` entries added to')
    A('### row `U1`. ### `0` rows of `FACES_LEDGER.md` written. ### `0` folds run. ### `0` rules')
    A('### struck or amended. ### `0` in-place repairs. ### `0` locked faces edited. ### `0` prior')
    A('### acts` banks edited. ### `0` kernels built. ### `0` `.lean` files touched. ### `0` axiom')
    A('### profiles read or inferred. ### `0` platform calls. ### `0` content lost.')
    A('### ### **BOTH LANES STAY PARKED. ### THE WAVE STAYS PARKED. ### NOTHING DEPOSITS.**')
    A('### ### **AND `h2` IS WHERE THE DEPOSIT LEFT IT** -- no claim in either direction.')
    A('')
    A(BARR)
    A('### THE WRITES, BY KIND.')
    A(BARR)
    A('### **KIND 11** -- `INVARIANCE_BARRIERS.md` §10.1, appended, `%d` lines, ### **UNCOMPILED**,'
      % ibn)
    A('###   written because the face`s condition was MEASURED and met: the two instruments agree.')
    A('### **KIND 10** -- `OPEN_TRAILS.md` one appended block; `CORRESPONDENCE.md` row `%d`;'
      % rownum)
    A('###   `banked_index.py` key `%s` -- read back %s.' % (KEY, 'PASS' if kok else 'FAIL'))
    A('### **AND NOTHING ELSE, OF ANY KIND.** ### No row of `FACES_LEDGER.md`, no head note, no')
    A('### class symbol, no instrument number.')
    A(BARR)
    n = write_bytes(BANKOUT, NL.join(B) + NL)
    rec('  ### BANK WRITTEN : %s  (%d lines, %d bytes)' % (os.path.basename(BANKOUT), len(B), n))
    return len(B)


# ### =================================================================================================
def main():
    rec('=' * 100)
    rec('b410_desk_bank.py -- THE DESK, THE KEYSTONE SECTION, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    rec('=' * 100)
    rec('  face LOCKED : %s' % SEALHASH)
    rec('')
    bar()
    rec('  ### THE DESK.')
    bar()
    Q = do_desk()

    rec()
    bar()
    rec('  ### KIND 11 -- THE CLASSIFICATION, APPENDED TO THE KEYSTONE (CONDITIONAL).')
    bar()
    kok2, ibn = do_keystone()
    if not kok2:
        rec('  ### HARD FAILURE in the keystone append.')
        rec('  ### run record : %s' % run_clock.write(D, 'b410_desk_notes', LINES))
        return 1

    rec()
    bar()
    rec('  ### KIND 10 -- THE TRAIL BLOCK.')
    bar()
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the b410 block is present. ### NOTHING APPENDED.')
        after = before
    else:
        rec('  ### the b409 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=NL).write(NL.join(trail_block(Q)) + NL)
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            rec('  ### run record : %s' % run_clock.write(D, 'b410_desk_notes', LINES))
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_three_factor': 'three factor through the product-formula interface' in low,
        'says_breaker': 'proposition c.1 does not factor' in low,
        'says_not_apply': '3.1-h does not apply to the corpus' in low,
        'says_larger': 'importing a criterion imports the statement it is equivalent to' in low,
        'says_not_against': 'says nothing against the reduction' in low,
        'says_two_instruments': 'it agrees on 4 of 4' in low,
        'says_one_row': 'one calibrated row, two certificates, zero compiled terminals' in low,
        'says_h2_quoted': 'that identification is quoted and nothing is narrowed' in low,
        'says_arity': 'not priceable without a build' in low,
        'says_placement_one': 'leaves exactly one candidate' in low,
        'says_density_all': 'leaves every single-place row' in low,
        'says_brightness': 'the brightness is all in the register' in low,
        'says_standing': 'standing, filed 2026-08-05, author-ruled' in low,
        'says_four_routes': 'four independent derivations of one boundary' in low,
        'says_price_zero': 'is `0`' in low,
        'says_same_test': 'are the same test' in low,
        'says_no_cite': '0 times in either direction' in low,
        'says_arms_built': 'all three fire on their own incidents' in low,
        'says_reach': '1 of the 3 dresses' in low,
        'says_order_premise': 'the order’s premise was false' in low,
        'says_repair': 'a record that repairs itself hides its own defects' in low,
        'says_66': '61 pin no class symbol at all' in low,
        'says_b409_corrected': 'was not the output of the instrument the claim names' in low,
        'says_i7_routed': 'on the author’s confirming word' in low,
        'says_table_named': 'seven_mechanism_classes.md' in low,
        'says_nothing_deposits': 'nothing deposits' in low,
        'says_h2': 'h2 where the deposit left it' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:**')
    for k, v in says.items():
        rec('      %-26s %s' % (k, v))
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        rec('  ### run record : %s' % run_clock.write(D, 'b410_desk_notes', LINES))
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
        rec('  ### run record : %s' % run_clock.write(D, 'b410_desk_notes', LINES))
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
            rec('  ### run record : %s' % run_clock.write(D, 'b410_desk_notes', LINES))
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
    nb = bank(Q, rownum, kok, ibn)

    rec()
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### KEYSTONE §10.1 %d LINES, UNCOMPILED. ### ROWS '
        'OF FACES_LEDGER WRITTEN : 0. ### CORR ROW %d. ### KEY %s. ### BANK %d LINES.**'
        % (Q['items'], Q['closed'], ibn, rownum, 'PASS' if kok else 'FAIL', nb))
    bar('=')
    p = run_clock.write(D, 'b410_desk_notes', LINES)
    print(NL + '  ### THIS RUN WROTE : %s   (stamp %s)'
          % (os.path.basename(p), run_clock.read_stamp(p)))
    lp, ls, note = run_clock.latest(D, 'b410_desk_notes')
    print('  ### AND THE GUARD AGREES : %s   (%s ; %s)'
          % (os.path.basename(lp or '-'), ls, note))
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
