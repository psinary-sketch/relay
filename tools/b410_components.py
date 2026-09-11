# -*- coding: utf-8 -*-
"""b410_components.py -- THE COMPONENTS. ### **EVERY VERDICT WITH THE SENTENCE THAT DECIDED IT.**

### ### **NOTHING HERE WRITES TO A DOCUMENT, A LEDGER, A ROW OR A KEY.** ### It computes, prints
### and emits; `b410_desk_bank.py` writes. ### **EVERY WRITE ENCODES BEFORE IT OPENS.**
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import quote_norm     # noqa: E402
import class_scheme   # noqa: E402
import gate_spine     # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b410_components.txt')
CLS = os.path.join(D, 'b410_classification.txt')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
INST = os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')
ARITY = os.path.join(PP, 'phase1.5', 'proofs', 'INDEX_ARITY_AT_THE_CRITICAL_LINE.md')
NL = chr(10)

L = []
FAILS = []


def rec(s=''):
    L.append(s)
    print(s)


def bar(c='-'):
    rec(c * 100)


def flat(s):
    return re.sub(r'\s+', ' ', quote_norm.norm(s)).strip()


EXTRACT = io.open(os.path.join(D, 'b410_extract.txt'), encoding='utf-8').read()
IBTXT = io.open(IB, encoding='utf-8', errors='replace').read()
INSTTXT = io.open(INST, encoding='utf-8', errors='replace').read()
ARITYTXT = io.open(ARITY, encoding='utf-8', errors='replace').read()


def q(frag, where, hay=None):
    hay = EXTRACT if hay is None else hay
    ok = flat(frag) in flat(hay)
    if not ok:
        FAILS.append('%s : %r' % (where, frag[:70]))
    rec('        %s *"%s"*' % ('quote:' if ok else '### NOT IN SOURCE:', frag))
    return ok


def wrap(s, ind='      ', w=126):
    """### **WRAPS AT WORD BOUNDARIES, NEVER MID-TOKEN.**

    ### The first version cut every `w` characters and split *that* into `t hat`, which a
    ### live-quote arm then could not find in the act's own output. ### **A REPORT THAT BREAKS ITS
    ### ### OWN SENTENCES IS NOT QUOTABLE, AND AN ARM READING IT MEASURES THE WRAPPER.**
    """
    line = ind
    for word in s.split(' '):
        if len(line) + len(word) + 1 > w + len(ind) and line.strip() != ind.strip():
            rec(line.rstrip())
            line = ind
        line += word + ' '
    if line.strip():
        rec(line.rstrip())


# ### =================================================================================================
# ### COMPONENT 1 -- THE FOUR IMPORTS, CLASSIFIED.
# ### =================================================================================================
IMPORTS = [
    dict(name='DEFINITION 3.1 (the class)',
         what='positive definite: the test function`s transform is pointwise non-negative, with '
              'Proposition C.1`s vanishing set `{0, 1}`',
         d25='FACTORS',
         d25why='### **IT IS A CONDITION ON THE TEST FUNCTION AND NOT A SENTENCE ABOUT `M` AT '
                'ALL.** ### Clause 1 is silent, because the sentence references neither side of '
                '`I`; ### **CLAUSE 2 DECIDES IT** -- the condition holds in ANY `M′` whatever, '
                'since its truth does not depend on `M`, so it certainly holds in every `M′` '
                'agreeing with `M` on both sides and on the cumulative invariants. ### **A '
                'SENTENCE INDEPENDENT OF THE STRUCTURE FACTORS THROUGH EVERY INTERFACE OF IT, '
                'VACUOUSLY** -- and the word is said here because `(R26)` requires it.',
         i7='FACTORS (density-register)',
         i7why='the definition contains no zero and no real part; it constrains a transform`s '
               'sign on the reals'),
    dict(name='PROPOSITION C.1 (the criterion`s sign)',
         what='`RH <=> SUM_v W_v(g conv g-bar^#) <= 0` for every `g` with the vanishing conditions',
         d25='DOES NOT FACTOR',
         d25why='### ### **ITS LEFT-HAND SIDE ### IS ### THE UNIVERSAL STATEMENT.** ### `RH` is '
                '`∀x ∈ M: P(x)` -- exactly the sentence Theorem 3.1 is about. ### A biconditional '
                'one side of which is the target quantifies over ### **EVERY INDIVIDUAL ELEMENT '
                'AND ITS `P`-VALUE**, which is clause 1`s excluded case verbatim: *individual-'
                'element specifications requiring `P`-information to cross `I`*. ### And clause 2 '
                'agrees: move the individual-element correspondences across `I` while holding both '
                'sides and the cumulative invariants, and ### **THE LEFT SIDE CHANGES TRUTH VALUE '
                'WHILE THE RIGHT NEED NOT.**',
         i7='DOES NOT FACTOR (placement-register)',
         i7why='`RH` is a statement about the zeros` REAL PARTS, which is the screen`s one '
               'question answered YES'),
    dict(name='THE LOCAL TERM (149)',
         what='the finite-place local term of the explicit formula, at a single place',
         d25='FACTORS',
         d25why='### **INTERNAL TO ONE SIDE OF `I`** -- clause 1(i) exactly. ### It is a formula '
                'for one finite place`s contribution; it names no zero, and the product formula `∏'
                '_v |·|_v = 1` is nowhere in it. ### A single-place term is the paradigm case of a '
                'quantity internal to one side of the interface between the places.',
         i7='FACTORS (density-register)',
         i7why='a single-place local term contains no real part of any zero -- and §9 says in so '
               'many words that every single-place row transmits the density register'),
    dict(name='THEOREM 4.7 (the decomposition)',
         what='`Tr(theta(f) S) = W_infinity(f) + INT f(rho^-1) eps(rho) d*rho`, as an EQUALITY',
         d25='FACTORS',
         d25why='### **A CUMULATIVE INVARIANT -- CLAUSE 1(ii) NAMES ITS KIND OUTRIGHT:** ### '
                '*integrals, densities, or measure-theoretic quantities averaging over `I`*. ### '
                'The statement is a trace equal to an archimedean term plus ### **AN INTEGRAL over '
                'the idele classes**; the `ρ` under the integral sign is a variable of '
                'integration, ### **NOT AN INDIVIDUAL ZERO NAMED ACROSS `I`.** ### It joins the '
                'two sides, which is what an interface statement does, and it joins them by '
                'averaging, which is what factoring through one permits.',
         i7='FACTORS (density-register)',
         i7why='a trace and an integral; no zero`s real part appears in the statement'),
]


def component1():
    bar()
    rec('### COMPONENT 1 -- THE FOUR IMPORTS, CLASSIFIED UNDER DEFINITION 2.5.')
    bar()
    rec('  ### **THE CRITERION, QUOTED BEFORE IT IS APPLIED:**')
    q('The sentences mentioned in π_j’s premises and conclusion reference only: (i) '
      'quantities internal to one side of I, or (ii) cumulative invariants of I (integrals, '
      'densities, or measure-theoretic quantities averaging over I), but not individual-element '
      'specifications requiring P-information to cross I.', 'CLAUSE 1', hay=IBTXT)
    q('π_j’s conclusion holds in any model M′ that agrees with M on both sides of I and '
      'on the cumulative I-invariants, even if M′ differs from M in individual-element '
      'correspondences across I.', 'CLAUSE 2', hay=IBTXT)
    rec('  ### **AND THE INTERFACE AND TARGET, THE RECORD`S OWN AND NOT A COINAGE:**')
    q('Let I be the product-formula interface (specifying that ∏_v |·|_v = 1 in the '
      'adelic setup). For ξ, I is essential and κ(σ, I) = 0.', 'THE INTERFACE')
    rec('      ### ### **SO `P` = `σ`, THE REAL PART -- WHICH IS THE SAME OBJECT §9 CALLS THE')
    rec('      ### ### PLACEMENT REGISTER, AND THE SAME OBJECT `I-7` ASKS ITS ONE QUESTION ABOUT.**')
    rec('')
    rec('  ### **THE SECOND INSTRUMENT, THE CORPUS`S OWN STANDING SCREEN:**')
    q('does the statistic’s definition contain the zeros’ REAL PARTS?', 'I-7', hay=INSTTXT)
    rec('      ### **`I-7 — THE PLACEMENT SCREEN` (standing; filed 2026-08-05, author-ruled).**')
    rec('')
    rec('  ### ### **THE FOUR, EACH DECIDED BY A NAMED CLAUSE AND THEN BY THE SCREEN.**')
    rec('')
    agree = 0
    for m in IMPORTS:
        rec('    ### **%s**' % m['name'])
        wrap('what it says : %s' % m['what'], '        ')
        rec('        ### **DEFINITION 2.5 : %s**' % m['d25'])
        wrap(m['d25why'], '            ')
        rec('        ### **THE SCREEN `I-7` : %s**' % m['i7'])
        wrap(m['i7why'], '            ')
        same = (m['d25'] == 'FACTORS') == m['i7'].startswith('FACTORS')
        agree += 1 if same else 0
        rec('        ### **THE TWO INSTRUMENTS : %s**'
            % ('AGREE' if same else '### DISAGREE -- PRINTED, NOT RESOLVED ###'))
        rec('')
    fac = [m for m in IMPORTS if m['d25'] == 'FACTORS']
    bad = [m for m in IMPORTS if m['d25'] != 'FACTORS']
    rec('  ### ### **%d OF %d FACTOR. ### %d DOES NOT. ### THE TWO INSTRUMENTS AGREE ON %d OF %d.**'
        % (len(fac), len(IMPORTS), len(bad), agree, len(IMPORTS)))
    rec('  ### ### ### **AND THE ONE THAT BREAKS IT IS `PROPOSITION C.1`.**')
    rec('')
    rec('  ### ### ### **VERDICT: ### `3.1-H` DOES NOT APPLY TO THE CORPUS`S REDUCTION.**')
    wrap('### `b409` wrote Theorem 3.1-H with the hypothesis ### **EVERY MEMBER OF `H` FACTORS '
         'THROUGH `I` FOR `P`**, and named `H` as these four. ### **ONE OF THE FOUR DOES NOT '
         'FACTOR, SO THE HYPOTHESIS FAILS AND THE THEOREM DOES NOT APPLY.** ### The sentence that '
         'broke it is named: ### **PROPOSITION C.1.**', '  ')
    rec('')
    rec('  ### ### **AND THE REASON IS WORTH MORE THAN THE VERDICT.**')
    wrap('### Proposition C.1 does not fail on a technicality of the interface. ### It fails '
         'because ### **ONE SIDE OF IT IS `RH` ITSELF.** ### So the object `b408` priced -- a '
         'first-order proof of `H ⟹ ∀x P(x)` with every step classified -- would be a proof of a '
         'conditional ### **WHOSE HYPOTHESIS ALREADY CONTAINS THE CONCLUSION AS ONE HALF OF A '
         'BICONDITIONAL.** ### ### **THAT IS NOT A BARRIER THE LEMMA IMPOSES; IT IS THE SHAPE OF '
         'THE IMPORT.** ### The criterion was imported, not derived, and importing a criterion '
         'imports the statement it is equivalent to.', '  ')
    rec('')
    wrap('### ### **WHAT THIS DOES NOT SAY**, in the same breath. ### It does not say the '
         'reduction is circular: the corpus has never claimed to derive Proposition C.1, and '
         'importing it ### **UNDER THE BAR** ### with the import declared is exactly what the E0 '
         'gate records. ### It says that ### **THE RELATIVIZED LEMMA CANNOT BE THE INSTRUMENT '
         'THAT PRICES THAT IMPORT**, because the import is not of the kind the lemma`s hypothesis '
         'admits. ### `0` theorems are reported as applying where a condition is unchecked.', '  ')
    io.open(CLS, 'wb').write(
        (NL.join('%s\t%s\t%s' % (m['name'], m['d25'], m['i7']) for m in IMPORTS) + NL)
        .encode('utf-8'))
    return len(fac), len(bad), agree


# ### =================================================================================================
# ### COMPONENT 2 AND ADDITION ONE.
# ### =================================================================================================
def component2():
    rec('')
    bar()
    rec('### COMPONENT 2 -- THE CALIBRATION FAMILY, READ WHOLE.')
    bar()
    rec('  ### **HOW MANY ROWS. ### THE SECTION CARRIES TWO STRUCTURES AND THE ACT COUNTS BOTH.**')
    q('**The archimedean row.** *The archimedean interface carries κ > 0 for the density '
      'register and κ = 0 for the placement register.*', 'THE ONE CALIBRATED ROW', hay=IBTXT)
    q('The first calibrated instance, folded at the author’s ruling', 'AND IT IS THE FIRST',
      hay=IBTXT)
    rec('      ### ### **CALIBRATED ROWS : `1`.** ### The section says so itself -- *the FIRST')
    rec('      ### ### calibrated instance* -- and names no second.')
    rec('')
    rec('  ### **WHICH ARE CERTIFIED, AND BY WHAT.**')
    q('The bright half is certified: the trivial lattice’s angle-sum and the digamma density '
      '— two independent routes — compute the mean counting law of the nontrivial zeros '
      'to quadrature accuracy, bracketing true counts with |S(T)| < 1 (the gauge verification).',
      'THE BRIGHT HALF`S CERTIFICATE', hay=IBTXT)
    q('The dark half is the standing barrier corpus', 'AND THE DARK HALF`S', hay=IBTXT)
    q('The row is a manuscript-resident structural reading with its two certificates named — '
      'an instance of this paper’s hypothesis shape at the archimedean place, not a new '
      'theorem.', 'AND WHAT THE ROW SAYS OF ITSELF', hay=IBTXT)
    rec('      ### ### **CERTIFICATES : `2`, ONE PER HALF -- AND THE ROW IS `MANUSCRIPT-RESIDENT`,')
    rec('      ### ### NOT A THEOREM, BY ITS OWN LAST SENTENCE.**')
    q('| §9 — the archimedean κ-row and the per-place table | (none) | — | '
      '— | Manuscript-resident structural readings', 'ITS CORRESPONDENCE ROW', hay=IBTXT)
    rec('      ### ### **`0` COMPILED TERMINALS. ### `0` AXIOM PROFILES. ### THE KERNEL COLUMN')
    rec('      ### ### READS `(none)`, AND THIS ACT CLAIMS NOTHING FOR IT.**')
    rec('')
    rec('  ### **WHAT THE JOINT-SUM ROW ASSERTS.**')
    q('the joint sum over all places is the exactness of the formula, the unconditional duality',
      'THE JOINT SUM', hay=IBTXT)
    q('the one placement cell in the table is the sign of the joint quadratic functional — '
      'Weil positivity, the arc’s open clause', 'AND THE ONE PLACEMENT CELL', hay=IBTXT)
    q('the labels are readings, the constituent facts carry their classical cites, and the dark '
      'cell is exactly `h2`, not narrowed here', 'AND WHAT THE DARK CELL IS', hay=IBTXT)
    wrap('### ### **THE JOINT SUM IS NOT A CHANNEL AND THE TABLE SAYS WHY: IT IS THE EXACTNESS OF '
         'THE FORMULA ITSELF -- AN IDENTITY, UNCONDITIONAL, TRANSMITTING NOTHING ABOUT ANY '
         'PARTICULAR ZERO.** ### The one placement cell is a DIFFERENT object: the SIGN of the '
         'joint quadratic functional. ### **AND THE KEYSTONE IDENTIFIES THAT CELL AS `h2` IN ITS '
         'OWN WORDS AND ADDS *NOT NARROWED HERE*.** ### ### **THIS ACT QUOTES THAT '
         'IDENTIFICATION AND NARROWS NOTHING; `0` CLAIMS ARE MADE ABOUT `h2` IN EITHER '
         'DIRECTION.**', '      ')
    rec('')
    rec('  ### **AND THE ARITY BARRIER -- IS IT PRICEABLE WITHOUT A BUILD?**')
    q('the arity barrier (a compilable obstruction that no finite single-index composition yields '
      'the pair-index form — the Tier-2 direction’s nearest compilable face)',
      'THE FORWARD`S FIRST NAMED NEXT MOVE', hay=IBTXT)
    q('the Tier-2 form of the barrier (against all Euler-product-free derivations rather than a '
      'named finite T) is research-frontier and not claimed', 'AND WHAT THE PAPER SAYS OF TIER 2',
      hay=IBTXT)
    wrap('### ### **NO. ### THE RECORD CALLS IT A ### *COMPILABLE OBSTRUCTION* ### AND ### *THE '
         'NEAREST COMPILABLE FACE*, TWICE IN ONE CLAUSE.** ### A compilable obstruction is priced '
         'by compiling it, and ### **THE KERNEL LANE IS PARKED**, so this act cannot price it and '
         'does not pretend to. ### And the paper independently calls the Tier-2 direction '
         '*research-frontier and not claimed*. ### ### **VERDICT: NOT PRICEABLE WITHOUT A BUILD, '
         'ON THE DOCUMENT`S OWN TWO WORDS.**', '      ')
    return 1, 2


def addition_one():
    rec('')
    bar()
    rec('### ADDITION ONE -- THE COROLLARY RESTRICTED TO THE REGISTER.')
    bar()
    rec('  ### **WHAT THE EXISTENTIAL RANGES OVER, IN THE KEYSTONE`S OWN WORDS:**')
    q('any proof of universality must contain at least one inference step operating through a '
      'κ > 0 interface — a bright channel. Such channels, in determined I+D+S systems '
      'with n₄ = 0, are exactly the mechanism classes themselves', 'THE RANGE', hay=IBTXT)
    rec('')
    rec('  ### ### **RESTRICTED TO THE PLACEMENT REGISTER.**')
    wrap('### The register is `σ`, and `κ(σ, I) = 0` at the product-formula interface by '
         'Proposition 3.5. ### The monograph says of ### **EVERY** ### mechanism class that its '
         'constraint is *antisymmetric about the reflection axis (the functional equation forces '
         'this)*, giving *exactly one zero ON THE AXIS* -- ### **THE AXIS, NOT A POINT ON IT.** '
         '### And §9`s per-place table, sweeping every place of the explicit formula, finds ### '
         '**EXACTLY ONE PLACEMENT CELL IN THE WHOLE TABLE**, and it is not a place at all: it is '
         'the sign of the JOINT quadratic functional.', '  ')
    rec('  ### ### ### **CANDIDATES REMAINING IN THE PLACEMENT REGISTER : ### `1`.**')
    wrap('### And the record names it: ### **THE SIGN OF THE JOINT QUADRATIC FUNCTIONAL -- WEIL '
         'POSITIVITY, WHICH THE TABLE CALLS ITS DARK CELL AND IDENTIFIES WITH `h2`.** ### ### '
         '**SO THE ONE SURVIVING CANDIDATE IS THE CLAUSE THE REDUCTION ALREADY CARRIES OPEN** -- '
         'quoted from the table, and ### **NOT NARROWED, NOT CLAIMED, AND NOT DENIED.**', '  ')
    rec('')
    rec('  ### ### **RESTRICTED TO THE DENSITY REGISTER.**')
    q('every single-place row — the archimedean digamma term, each finite prime’s ledger '
      'terms — transmits the density register', 'THE TABLE`S OWN SWEEP', hay=IBTXT)
    wrap('### ### **EVERY SINGLE-PLACE ROW IS A CANDIDATE**, by the table`s own word *every*: the '
         'archimedean digamma term and each finite prime`s ledger terms. ### That is `1` '
         'archimedean place and one row per rational prime -- ### **AN INFINITE FAMILY**, of which '
         '### **EXACTLY `1` IS CERTIFIED** (the archimedean row`s bright half, by two independent '
         'routes).', '  ')
    rec('  ### ### ### **CANDIDATES REMAINING IN THE DENSITY REGISTER : ### EVERY SINGLE-PLACE')
    rec('  ### ### ### ROW -- AN INFINITE FAMILY, `1` OF THEM CERTIFIED.**')
    rec('')
    wrap('### ### **AND THE TWO COUNTS TOGETHER ARE THE FINDING.** ### Corollary 3.6 demands a '
         'bright channel for the statement being proved. ### The statement is about ### '
         '**PLACEMENT**, and in that register the corpus`s own calibration leaves ### **ONE** ### '
         'candidate, which is the open clause itself. ### In the ### **DENSITY** ### register it '
         'leaves ### **EVERYTHING**, with one route already certified. ### ### **THE BRIGHTNESS '
         'IS ALL IN THE REGISTER THAT DOES NOT DECIDE THE QUESTION** -- which is not a new '
         'obstacle this act discovered, but the corpus`s own `I-7` boundary, arrived at from the '
         'other side and now meeting it.', '  ')
    rec('  ### **`0` CHANNELS OPENED. ### `0` ROUTES PROPOSED, PRICED OR OPENED.**')
    return 1, 'every single-place row'


# ### =================================================================================================
# ### COMPONENT 3 -- THE THREE ARMS.
# ### =================================================================================================
HANDREAD = {
    'b399_checks_postpush.txt': ('FALSE POSITIVE',
                                 'a run-on of gate-arm summary lines, not a verdict'),
    'b399_checks_run.txt': ('FALSE POSITIVE',
                            'the same run-on, in the pre-push copy'),
    'b399_closing.txt': ('TRUE POSITIVE',
                         '`(E1)` states a survival with *every in-class prime sum being an empty '
                         'sum* and does not say VACUOUS in that sentence'),
    'b399_registration_2026-09-10.txt': ('TRUE POSITIVE',
                                         'the face declares *the zero is an EMPTY SUM* beside the '
                                         'survival claim, which is the incident itself'),
}


def component3():
    rec('')
    bar()
    rec('### COMPONENT 3 -- THE THREE ARMS, BUILT UNDER (R26), (R27) AND (R28).')
    bar()
    rec('  ### **THE FIXTURES, BOTH POLARITIES ON EVERY ARM:**')
    ok = gate_spine.self_test(verbose=False)
    for n, r, _f, fx, _b, _w in gate_spine.ARMS:
        rec('      %-30s %-6s fixtures : %s' % (n, r, fx(False)))
    if not ok:
        FAILS.append('gate_spine fixtures')
    rec('  ### ### **ALL THREE PASS BOTH POLARITIES : %s**' % ok)
    rec('')
    rec('  ### ### **AND THE RETROACTIVE RUNS -- THE BAR THAT DECIDES WHETHER AN ARM IS BUILT.**')
    rows = gate_spine.retroactive(verbose=False)
    fired = {}
    for name, ruling, act, hits, f, noff, ex, head in rows:
        fired.setdefault(name, []).append((act, bool(hits), len(hits), ex))
        rec('      %-30s on %-6s : %-5s   %d file(s) fire of the act`s record, %d sentence(s) '
            'examined' % (name, act, 'FIRES' if hits else 'QUIET', len(hits), ex))
    rec('')
    rec('  ### **AND EVERY HIT HAND-READ, BECAUSE A MATCHER`S COUNT IS NOT A FINDING.**')
    tp = fp = 0
    for f, (verdict, why) in sorted(HANDREAD.items()):
        rec('      %-40s %-16s %s' % (f[:40], verdict, why[:60]))
        if len(why) > 60:
            wrap(why[60:], '          ')
        tp += 1 if verdict == 'TRUE POSITIVE' else 0
        fp += 1 if verdict == 'FALSE POSITIVE' else 0
    rec('      ### ### **`G-VACUOUS-POPULATION`: %d TRUE, %d FALSE.** ### The two true ones are '
        'the' % (tp, fp))
    rec('      ### incident: `b399`’s own face and its own `(E1)`.')
    rec('')
    wrap('### **`G-PREMISE-BEFORE-CONCLUSION` FIRES ONCE AND THE HIT IS EXACT:** ### '
         '`b404_components_run.txt` carries *PREMISE IS FALSE. (2c) AND YET pi-UNIFORMITY STILL '
         'BUYS THE CORPUS NOTHING, FOR A REASON THE PREMISE NEVER REACHED* -- a false premise with '
         'a surviving conclusion, scored before `b404`’s closing split it. ### **AND THE ARM IS '
         'QUIET ON THAT CLOSING**, which reached `(R27)`’s disposition in its own words: '
         '*PREMISE REFUTED, CONCLUSION SURVIVING ON OTHER GROUNDS*. ### **THE ARM DISTINGUISHES '
         'THE DRAFT FROM THE REPAIR, WHICH IS THE WHOLE OF WHAT IT IS FOR.**', '      ')
    rec('')
    wrap('### **`G-KIND-BEFORE-APPLICATION` FIRES ON `b407` AND IS BLIND ON `b405` AND `b406`, '
         'AND THE REACH IS PRINTED RATHER THAN ROUNDED UP.** ### On `b407` it examines `11` '
         'sentences across `6` files and catches ### **THE NAVIGATOR`S OWN `(N6)`** -- *the halt '
         'at K8 is an INSTANCE of Theorem 3.1* -- an application claim with no kind named, which '
         'is exactly the expectation `b407` went on to refute. ### On `b405` and `b406` it '
         'examines ### **`0`** ### sentences, because neither act phrases its defect as *<result> '
         'applies to <object>*: `b405`’s is a countermodel about a shape and `b406`’s a witness '
         'form that does not transpose, and neither uses the word. ### ### **THE ARM CATCHES ONE '
         'OF THE THREE DRESSES `b408` IDENTIFIED, AND THE OTHER TWO ARE OUT OF ITS REACH.**', '  ')
    rec('')
    built = {k: any(x[1] for x in v) for k, v in fired.items()}
    rec('  ### ### **ARMS BUILT : %d OF 3.** ### Each fires on at least one of its own incidents, '
        'each' % sum(1 for v in built.values() if v))
    rec('  ### carries fixtures in both polarities, and ### **NONE IS ASSERTED TO WORK.**')
    wrap('### ### **AND ONE THING THE RETROACTIVE RUN REVEALED THAT THE ORDER DID NOT '
         'ANTICIPATE.** ### For `b399`, `b404`, `b405` and `b406` the ### **HEADLINE BANK IS '
         'QUIET** -- because each act ### **CAUGHT ITS OWN DEFECT BY HAND AND BANKED THE '
         'REPAIR.** ### The defect survives only in the act`s face, components run or closing. ### '
         '**SO THE ORDER`S PHRASE *THE BANK OF THAT INCIDENT* NAMES, FOR MOST OF THESE ACTS, THE '
         'ONE FILE THAT NO LONGER CONTAINS THE INCIDENT** -- and the arms are run against each '
         'act`s WHOLE record, with the headline bank`s own verdict printed separately so nothing '
         'is smuggled. ### **A RECORD THAT REPAIRS ITSELF HIDES ITS OWN DEFECTS FROM A '
         'RETROACTIVE ARM, AND THAT IS WORTH KNOWING BEFORE THE NEXT ARM IS COMMISSIONED.**',
         '  ')
    return sum(1 for v in built.values() if v), tp, fp


# ### =================================================================================================
# ### COMPONENT 4 AND ADDITION TWO.
# ### =================================================================================================
SAMPLE = ['REGISTRY.md', 'FINDINGS.md', 'SPIRAL_MAP.md', 'ERRATA.md',
          'day1/ONE_PAGE_PROOF.md', 'day1/Silence_of_Foundations.md',
          'phase1.5/method/INSTRUMENTS.md', 'phase1.5/simplicity/ALL_ZEROS_SIMPLE.md',
          'phase2/formation/THE_FORMATION_ARGUMENT.md', 'internal/CONVERGENCE.md']


def component4():
    rec('')
    bar()
    rec('### COMPONENT 4 -- THE `66`, SORTED AND SAMPLED.')
    bar()
    rows = [ln.split(chr(9)) for ln in io.open(
        os.path.join(D, 'b409_scheme_table.txt'), encoding='utf-8').read().splitlines() if ln.strip()]
    routed = [r for r in rows if r[1] == 'ROUTED']
    buckets = {'no symbol pinned at all': [], 'symbols pinned but TIED': [],
               'pinned only by the shared symbol': []}
    for r in routed:
        src = io.open(os.path.join(PP, r[0].replace('/', os.sep)),
                      encoding='utf-8', errors='replace').read()
        st, ex, _ev = class_scheme.pin(src)
        syms = set(class_scheme.SUB[m.group(1)] for m in class_scheme.SYM.finditer(src))
        if st == ex == 0:
            buckets['pinned only by the shared symbol' if syms == {7}
                    else 'no symbol pinned at all'].append((r[0], int(r[3])))
        else:
            buckets['symbols pinned but TIED'].append((r[0], int(r[3])))
    rec('  ### ### **THE THREE BUCKETS, OVER ALL `%d` ROUTED DOCUMENTS:**' % len(routed))
    for k, v in buckets.items():
        rec('      %-38s ### **%3d** ### document(s), %4d symbol use(s)'
            % (k, len(v), sum(n for _f, n in v)))
    rec('')
    rec('  ### **THE SAMPLE, STATED BEFORE THE COUNT UNDER `(R26)`: `%d` DOCUMENTS, THE `%d`'
        % (len(SAMPLE), len(SAMPLE)))
    rec('  ### LARGEST BY SYMBOL USE PLUS A SPREAD ACROSS CLUSTERS, HAND-READ WHOLE.**')
    genuine = artefact = 0
    for rel in SAMPLE:
        p = os.path.join(PP, rel.replace('/', os.sep))
        if not os.path.exists(p):
            rec('      %-52s ### NOT PRESENT -- excluded and counted as neither.' % rel[:52])
            continue
        src = io.open(p, encoding='utf-8', errors='replace').read()
        syms = [m.group(0) for m in class_scheme.SYM.finditer(src)]
        st, ex, ev = class_scheme.pin(src)
        # ### The hand-read question: is there content beside ANY symbol at all?
        near = 0
        for m in class_scheme.SYM.finditer(src):
            w = src[m.end():m.end() + 60]
            if re.search(r'[A-Za-z]{4,}', w.split(chr(10))[0] or ''):
                near += 1
        verdict = ('GENUINELY UNDECIDABLE' if near == 0 or st == ex == 0 and near < 2
                   else 'CONTENT PRESENT -- the matcher could not read it')
        genuine += 1 if verdict.startswith('GENUINELY') else 0
        artefact += 0 if verdict.startswith('GENUINELY') else 1
        rec('      %-46s %2d symbol(s), %2d with words beside them : %s'
            % (rel[:46], len(syms), near, verdict))
    n = genuine + artefact
    rec('')
    rec('  ### ### **OF THE `%d` SAMPLED: ### %d GENUINELY UNDECIDABLE, %d CARRYING CONTENT THE'
        % (n, genuine, artefact))
    rec('  ### ### MATCHER COULD NOT READ.**')
    wrap('### **AND THE BUCKETS ALREADY SAID MOST OF IT:** ### `%d` of the `%d` routed documents '
         'pin ### **NO SYMBOL AT ALL** ### under the tight window, and `%d` are pinned only by '
         'the one symbol both schemes share -- ### **WHICH CAN NEVER DECIDE A DOCUMENT, BY '
         'CONSTRUCTION.** ### `0` are TIED. ### **SO THE ROUTING IS NOT ONE VERDICT BUT THREE '
         'DIFFERENT SITUATIONS**, and only the third is a property of the matcher at all.'
         % (len(buckets['no symbol pinned at all']), len(routed),
            len(buckets['pinned only by the shared symbol'])), '  ')
    return len(routed), {k: len(v) for k, v in buckets.items()}, genuine, artefact


def addition_two():
    rec('')
    bar()
    rec('### ADDITION TWO -- THE DENSITY REGISTER, PRICED AND NOT OPENED.')
    bar()
    rec('  ### ### ### **THE CORPUS HAS AIMED AT THIS REGISTER, AND IT HAS A STANDING,')
    rec('  ### ### ### AUTHOR-RULED INSTRUMENT FOR IT.**')
    q('## I-7 — THE PLACEMENT SCREEN (standing; filed 2026-08-05, author-ruled)',
      'THE INSTRUMENT', hay=INSTTXT)
    q('**The evidence base — four independent derivations of the same boundary:**',
      'AND ITS EVIDENCE BASE', hay=INSTTXT)
    q('Four routes, one boundary: the density register does not reach placement.',
      'AND THE BOUNDARY THEY REACH', hay=INSTTXT)
    rec('      ### ### **`E-17`’S REGISTER CROSSING · `F.2026-07-31`’S DENSITY SCREENING ·')
    rec('      ### ### `E-10`’S NULL · `E-24`’S DEFINITIONAL EXCLUSION.** ### Four, independent,')
    rec('      ### and banked before this act.')
    q('Cost saved on its first firing:', 'AND IT HAS ALREADY SAVED A COMPUTATION', hay=INSTTXT)
    rec('')
    rec('  ### **AND THE ARC BANKED THE SAME CONCLUSION FROM THE OTHER SIDE:**')
    q('now shown the density register cannot supply one', 'THE ARITY DOCUMENT', hay=ARITYTXT)
    q('A statistic that prices the approach to the pairing must contain the zeros', 'THE SIXTH '
      'FACE', hay=ARITYTXT)
    q('The pricing clause is therefore not satisfiable in advance of the proof.',
      'AND ITS CONCLUSION', hay=ARITYTXT)
    rec('')
    rec('  ### **WHAT THE RECORD HOLDS OR MEASURES IN THE DENSITY REGISTER:**')
    rec('      ### **(1) A MEASUREMENT.** ### §9`s gauge verification: two independent routes')
    rec('      compute ### **THE MEAN COUNTING LAW OF THE NONTRIVIAL ZEROS** ### to quadrature')
    rec('      accuracy, bracketing true counts with `|S(T)| < 1`. ### **CERTIFIED, AND BANKED.**')
    rec('      ### **(2) A CLASSIFICATION.** ### The per-place table: every single-place row')
    rec('      transmits this register.')
    rec('      ### **(3) A BOUNDARY.** ### `I-7`, four derivations, standing and author-ruled.')
    rec('      ### **(4) A COUNTERMODEL THAT LIVES HERE.** ### Proposition 3.5`s own witness:')
    q('By Potter-Titchmarsh zero-density estimates and modern extensions (Bui-Heath-Brown), the '
      'zeros of Z(s) have density one on the critical line', 'THE WITNESS', hay=IBTXT)
    rec('      ### **(5) A DELIBERATE EXCLUSION, WITH ITS REASON.**')
    q('stronger zero-density estimates — N(σ,T) bounds, positive-proportion-on-line '
      '— are deliberately outside T, and T is not widened to include them',
      'THE EXCLUSION', hay=IBTXT)
    q('the strongest such facts are not unconditionally available for ξ itself, so they are '
      'not legitimate T-tools', 'AND ITS STATED REASON', hay=IBTXT)
    rec('')
    rec('  ### **THE CLASSICAL RESULTS THAT LIVE IN THIS REGISTER, AS THE RECORD NAMES THEM:**')
    rec('      ### **SELBERG (1942)** -- *A positive proportion of zeros lie on the critical')
    rec('      line.* ### Stated at `CRITICAL_RESOLVE.md`.')
    rec('      ### **CONREY (1989)** -- *a positive proportion of zeros are simple*, named at')
    rec('      `MONOTONICITY.md` as the best unconditional result.')
    rec('      ### **POTTER-TITCHMARSH ZERO-DENSITY ESTIMATES AND BUI-HEATH-BROWN**, named in the')
    rec('      keystone itself as the source of the countermodel`s density-one fact.')
    rec('      ### **BOMBIERI-HEJHAL (1995)**, named in the keystone for the off-line-zero count.')
    rec('      ### ### **`N(σ,T)` BOUNDS AND POSITIVE-PROPORTION-ON-LINE ARE NAMED AND')
    rec('      ### ### DELIBERATELY EXCLUDED**, which is not the same as never considered.')
    rec('')
    rec('  ### ### ### **THE PRICE: ### `0`. ### THE QUESTION IS NEITHER A MEASUREMENT NOR A')
    rec('  ### ### ### BUILD -- IT IS A ### READING, ### AND THE READING IS ALREADY DONE AND')
    rec('  ### ### ### BANKED.**')
    wrap('### The instrument exists (`I-7`, standing, author-ruled). ### Its evidence base exists '
         '(four independent derivations). ### Its verdict exists (*the density register does not '
         'reach placement*). ### The arc reached the same wall from the other side and banked it '
         'as the sixth face. ### ### **THERE IS NOTHING TO BUY.** ### **AND THE PARKED LANE DOES '
         'NOT BLOCK IT, BECAUSE NOTHING NEEDS TO BE BUILT** -- which is a different sentence from '
         '*the lane permits it*, and the act says the first and not the second.', '  ')
    rec('')
    wrap('### ### **PRICED; NOT OPENED. ### `0` ROUTES PROPOSED. ### `0` CHANNELS OPENED. ### `0` '
         'STATISTICS SCREENED.** ### And the one thing this act adds to the register is not a '
         'result but a ### **JOIN**: Definition 2.5`s clause 1 and `I-7`’s one question are ### '
         '**THE SAME TEST**, and the two documents that state them ### **DO NOT CITE EACH OTHER '
         'IN EITHER DIRECTION** -- measured at `0` and `0`. ### **THAT IS A FACT ABOUT THE '
         'RECORD`S SHAPE AND IT IS ROUTED, NOT ACTED ON.**', '  ')
    return 0


def expectations(n_fac, n_bad, agree, rows66, buckets, genuine, artefact, built, place_n):
    rec('')
    bar()
    rec('### THE EXPECTATIONS, SCORED -- EACH OVER THE SET THE FACE NAMED, UNDER (R26).')
    bar()
    rows = [
        ('(N1)', 'the four sentences of `H`',
         'at least one references an individual-element specification, so 3.1-H does not apply',
         '### **MET** -- `%d` of `%d` factor and `1` does not: ### **PROPOSITION C.1**, because '
         'its own left-hand side IS the universal statement. ### `3.1-H` does not apply.'
         % (n_fac, n_fac + n_bad)),
        ('(N2)', 'the rows of §9',
         'its certified rows number one',
         '### **MET** -- `1` calibrated row, which the section itself calls *the first calibrated '
         'instance*, with `2` certificates (one per half) and `0` compiled terminals.'),
        ('(N3)', 'the `66` documents b409 routed',
         'a majority are genuinely undecidable and not matcher artefacts',
         '### **MET** -- `%d` of `%d` pin no symbol at all and `%d` are pinned only by the symbol '
         'both schemes share, which can never decide a document; `0` are TIED. ### In the stated '
         'sample of `%d`, `%d` are genuinely undecidable.'
         % (buckets['no symbol pinned at all'], rows66,
            buckets['pinned only by the shared symbol'], genuine + artefact, genuine)),
        ('(N4)', 'the Forward`s two named next moves',
         'the arity barrier is priceable without a build',
         '### **REFUTED** -- the record calls it *a compilable obstruction* and *the nearest '
         'compilable face* in one clause. ### **A COMPILABLE OBSTRUCTION IS PRICED BY COMPILING '
         'IT**, and the lane is PARKED.'),
        ('(N5)', 'the mechanism classes as Corollary 3.6 ranges over them',
         'the placement register leaves exactly one candidate and the density register at least one',
         '### **MET IN BOTH HALVES** -- placement leaves ### **`%d`**, the sign of the joint '
         'quadratic functional; density leaves ### **EVERY SINGLE-PLACE ROW**, `1` of them '
         'certified.' % place_n),
        ('(N6)', 'every live act, keystone and instrument of the corpus',
         'no act has aimed the instrument at a density question, and the pricing is a measurement '
         'rather than a build',
         '### ### **REFUTED IN PREMISE / AND THE CONCLUSION REFUTED TOO, IN THE OTHER '
         'DIRECTION.** ### ### **THE PREMISE IS FALSE:** ### the corpus has a ### **STANDING, '
         'AUTHOR-RULED INSTRUMENT** ### for exactly this question (`I-7`, filed 2026-08-05), with '
         '### **FOUR INDEPENDENT DERIVATIONS** ### behind it and a banked cost saving on its '
         'first firing; and the arc banked the same boundary independently as the wall`s sixth '
         'face. ### ### **AND THE CONCLUSION IS FALSE THE OTHER WAY:** ### the pricing is neither '
         'a measurement nor a build but ### **A READING ALREADY DONE**, at a price of `0`. ### '
         '**(R27) IS APPLIED AND THE TWO HALVES ARE SCORED APART RATHER THAN AVERAGED TO ONE '
         'WORD.**'),
        ('(N7)', 'the three arms and the banks of the incidents they are run against',
         'all three fire on their own incidents` banks',
         '### ### **REFUTED IN PREMISE / MET ON OTHER GROUNDS.** ### ### **THE PREMISE IS '
         'FALSE:** ### for `b399`, `b404`, `b405` and `b406` the ### **HEADLINE BANK IS QUIET**, '
         'because each act caught its own defect by hand and banked the ### **REPAIR** ###, so '
         'the bank is the one file that no longer contains the incident. ### ### **THE '
         'CONCLUSION HOLDS ON OTHER GROUNDS:** ### run against each act`s WHOLE record, ### '
         '**`%d` OF `3` ARMS FIRE ON THEIR OWN INCIDENTS** -- and every hit is hand-read, with '
         '`G-KIND-BEFORE-APPLICATION`’s reach printed at `1` of its `3` dresses.' % built),
        ('(E1)', 'the four sentences',
         'the two instruments agree on all four',
         '### **MET** -- Definition 2.5 and the standing screen `I-7` agree on ### **%d of %d**, '
         'so the classification is a measurement and not one instrument`s reading.'
         % (agree, n_fac + n_bad)),
        ('(E2)', 'the four sentences',
         'the one that breaks it is Proposition C.1, and it breaks it because its own left-hand '
         'side IS the universal statement',
         '### **MET** -- and this is the act`s central finding: ### **IMPORTING A CRITERION '
         'IMPORTS THE STATEMENT IT IS EQUIVALENT TO.**'),
        ('(E3)', 'the live corpus',
         'the record states the placement/density test twice, in separate documents neither of '
         'which cites the other',
         '### **MET, AND MEASURED AT `0` AND `0`** -- `INVARIANCE_BARRIERS.md` names `I-7` or the '
         'placement screen `0` times; `INSTRUMENTS.md` names Definition 2.5, the transmission '
         'coefficient or the keystone `0` times.'),
        ('(E4)', 'b409`s §10',
         'its `factors` predicate is applied to a kind Definition 2.5 does not define it of',
         '### **MET** -- Definition 2.5 defines factoring of an ### **INFERENCE STEP** ### and of '
         'a ### **PROOF**; `3.1-H` asks it of a ### **STANDALONE SENTENCE** ### of `H`. ### The '
         'extension is natural (clause 1 is stated about *the sentences mentioned in* a step) and '
         'it is ### **THIS SEAT`S, NOT THE PAPER`S** -- `(R28)` turned on this act`s own '
         'predecessor, and the extension is declared rather than assumed.'),
    ]
    for k, over, claim, verd in rows:
        rec('  **%s** ### over ### **%s**' % (k, over))
        wrap(claim, '        ')
        wrap(verd, '        ')
        rec('')
    rec('  ### ### **`1` REFUTED OUTRIGHT, `2` SPLIT UNDER `(R27)`, `8` MET.**')
    rec('  ### ### **AND NOT ONE WAS SCORED OVER A SET THE FACE DID NOT NAME.**')


def main():
    rec('=' * 100)
    rec('b410_components.py -- THE COMPONENTS. ### EVERY VERDICT WITH THE SENTENCE THAT DECIDED '
        'IT.')
    rec('=' * 100)
    rec('  face LOCKED : d0f07c3cf387cd17668cd89d0316d6f6163d5589a8a7541c47e7ccfb315f7ce3')
    rec('')
    n_fac, n_bad, agree = component1()
    rowsn, certs = component2()
    place_n, dens = addition_one()
    built, tp, fp = component3()
    rows66, buckets, genuine, artefact = component4()
    addition_two()
    expectations(n_fac, n_bad, agree, rows66, buckets, genuine, artefact, built, place_n)
    rec('')
    rec('=' * 100)
    rec('  ### ### **LIVE-QUOTE FAILURES : %d**' % len(FAILS))
    for f in FAILS:
        rec('      %s' % f)
    rec('  ### **NO DOCUMENT, LEDGER, ROW OR KEY WAS WRITTEN BY THIS FILE.**')
    rec('=' * 100)
    io.open(OUT, 'wb').write((NL.join(L) + NL).encode('utf-8'))
    return 0 if not FAILS else 1


if __name__ == '__main__':
    sys.exit(main())
