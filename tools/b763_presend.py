# -*- coding: utf-8 -*-
"""tools/b763_presend.py -- (R373)(5): "the pre-send reads of (R368)(4) carried"; (R373)(6): "THE SALT CHECK, printed before each send: each
statement beside the definitions it rests on (primeSum, primeTermQ, poleTerm, weilTest, classK, h2_sign_upto), binding no hypothesis beyond what
its sentence above names"; (R373)(7): "THE CONTROL THAT NO ZERO IS USED: the file that carries the proof imports no module under Schema/ZQ/OffZero,
neither Schema/Detector nor a module of Schema/Wide that carries a detector, and names none of zq_offline_zero, wide_detector, detector,
zq_arith_side_re_neg and zq_li_nonneg_fails; printed before each send."

The two reads and their controls are tools/b758_presend.py's, imported and not changed (its reader of the targets, the libraries and the
namespaces tools/b757_join.py's, through it): (i) each fully qualified declaration name in one module over the targets' modules and their import
closure in the kernel's tree, the duplicates printed, 0 wanted; (ii) each line of print_targets.txt against the workflow's filter (build-module.yml
:91), the lines it refuses printed, the two known (:358 and :359, each carrying the Greek capital lambda).

THE SALT CHECK, this file's own, read from the blobs at the revision, each kernel line read by predicate and printed by line number and digest
alone, never quoted. For each statement of a send: its header found (the declaration's keyword and name at a line's start, comments and
docstrings blanked first, so prose is not read); each bound hypothesis classed by the full match of its type against the table CLASSES, and the
class read against the classes its sentence names (SENDS); its conclusion (a theorem's type, a definition's body) read against the sentence's
predicates; the definitions of the ruling's six (and the others named in DEFS) it names, each printed with its file, line and the digest of its
text at the revision. The send's files: no sorry and no admit outside comments, no axiom, no variable line, no unsafe, no implemented_by or
extern, no option that skips the kernel's check; `lemma` counted (SPIRAL_MAP section 7 rule 9). A statement passes where it is found, every
hypothesis is of a class its sentence names, and every predicate holds; a send passes where each statement passes and its files are clean.

THE NO-ZERO CONTROL over one file at a revision: its own import lines (the ruling's word: the file "imports"), each read against the barred
modules -- under SIDEExplicitFormula.Schema.ZQ.OffZero, SIDEExplicitFormula.Schema.Detector, and each module under
SIDEExplicitFormula.Schema.Wide whose text at the revision declares a name holding "detector"; the five names read in the file's code with
comments blanked, a name in prose counted beside and not read. The import closure's barred modules are counted beside, as information: the
ruling bars the file's imports, and Schema/Detector stands upstream of cQ, primeTermQ, archTermQ and zqZeroConfig (data/b763_events.txt (10)).

  control                       b758's controls, the salt check's and the no-zero control's planted controls, printed
  read <rev>                    b758's two reads at a revision, printed
  salt <rev> <send>             the salt check of a send at a revision, printed (sends: SENDS' keys)
  zero <rev> <path>             the no-zero control over one file at a revision, printed
  bank <before> <tip> <send>    the controls, both reads at each revision, the salt check of the send at the tip (and the no-zero control over
                                the send's files where the send is of (7)), written to data/b763_presend_<send>.txt with the foot read at the tip
Reads only; the one write is the bank (through standing.figbank).
"""
import hashlib
import os
import re
import sys

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b758_presend as P         # noqa: E402  ### b758's two reads and controls, imported and not changed
import figbank as FB             # noqa: E402

NL = '\n'
ACT = 'b763'
KNOWN = [358, 359]   # ### the filter's two known refusals at a3aad4cc (v0.41): 489 lines, 487 passed, 2 refused
FF = 'SIDEExplicitFormula/FormFinite.lean'
PA = 'SIDEExplicitFormula/PoleAutocorrelation.lean'
PS = 'SIDEExplicitFormula/ParitySplit.lean'
AW = 'SIDEExplicitFormula/AdmissibleWeights.lean'
CF = 'SIDEExplicitFormula/ControlFailureStatement.lean'
OP = 'SIDEExplicitFormula/OnePageStatement.lean'
SQ = 'SIDEExplicitFormula/SquaresAt24.lean'

# ### the classes of a bound hypothesis, each by the full match of its type (whitespace collapsed)
CLASSES = (
    ('weights', 'weights c : N -> R (the sentence: "for any real weights c")', r'ℕ → ℝ'),
    ('testfn', 'a test function R -> C', r'ℝ → ℂ'),
    ('realfn', 'a real function R -> R (the sentence: "h real")', r'ℝ → ℝ'),
    ('real', 'a real number (a width L, or a point)', r'ℝ'),
    ('vanish', 'vanishing outside [-L, L]', r'∀ u : ℝ, \w+ < \|u\| → \w+ u = 0'),
    ('log2', 'L below log 2', r'\w+ < Real\.log 2'),
    ('c2', 'twice continuously differentiable', r'ContDiff ℝ 2 \w+'),
    ('cont', 'continuous (implied by twice continuously differentiable)', r'Continuous \w+'),
    ('compact', 'compact support', r'HasCompactSupport \w+'),
    ('even', 'even', r'∀ x, (\w+) \(-x\) = \1 x'),
    ('odd', 'odd', r'∀ x, (\w+) \(-x\) = -\1 x'),
    ('cpoint', 'a complex point, the variable of the transform (as a real point is of a function)', r'ℂ'),
    ('agree', 'two weights agreeing up to the integer part of e^L (the sentence: "turns on the values of c up to the integer part of e^L")',
     r'∀ n : ℕ, n ≤ ⌊Real\.exp \w+⌋₊ → \w+ n = \w+ n'),
    ('nat', 'a natural number (FORM A`s n, "at a named n", which the statement takes as its parameter; the modulus N and the index n of One Page`s rows; the prime p of (8)`s squares)', r'ℕ'),
    ('evenR', 'even, the variable typed (as the source row binds it)', r'∀ x : ℝ, (\w+) \(-x\) = \1 x'),
    ('nezero', 'the modulus not zero (as the source row binds it, a variable of its file)', r'NeZero \w+'),
    ('character', 'a Dirichlet character (the row: "at a primitive character")', r'DirichletCharacter ℂ \w+'),
    ('primitive', 'primitive (the row: "a primitive character")', r'\w+\.IsPrimitive'),
    ('nontriv', 'not the trivial character (the row: "χ ≠ 1")', r'\w+ ≠ 1'),
    ('config', 'a configuration (the row: "over a configuration")', r'Schema\.WeilConfig'),
    ('prime', 'p prime (the order: "a prime above 3")', r'\w+\.Prime'),
    ('factprime', 'p prime, as an instance (the order: "a prime above 3")', r'Fact \w+\.Prime'),
    ('above3', 'p above 3 (the order: "a prime above 3")', r'3 < \w+'),
    ('mod4', 'p 1 modulo 4 (a step of the order`s proof: reciprocity at 3 for such a prime)', r'\w+ % 4 = 1'),
)
CLASS_WORDS = dict((k, w) for k, w, _r in CLASSES)

# ### the definitions a statement may rest on: (name, the file at the revision, the pattern of its use in a statement)
DEFS = (('primeSum', 'SIDEExplicitFormula/B321Identity.lean'), ('primeTermQ', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean'),
        ('poleTerm', 'SIDEExplicitFormula/B321Identity.lean'), ('weilTest', 'Zeta23/ExplicitFormula.lean'),
        ('classK', 'SIDEExplicitFormula/H2Sign.lean'), ('h2_sign_upto', 'SIDEExplicitFormula/DetectionRegion.lean'),
        ('archTerm', 'SIDEExplicitFormula/B321Identity.lean'), ('paperFT', 'Zeta23/Defs.lean'),
        ('plateau', 'SIDEExplicitFormula/TwoPropertyWindow.lean'), ('archTermQ', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean'),
        ('cQ', 'SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean'), ('zeroSide', 'SIDEExplicitFormula/B321Identity.lean'),
        ('admissibleWeights', 'SIDEExplicitFormula/AdmissibleWeights.lean'), ('liCoeff', 'SIDEExplicitFormula/Schema/Wide/Converse.lean'),
        ('zqZeroConfig', 'SIDEExplicitFormula/Schema/ZQ/Zeros.lean'))
SIX = ('primeSum', 'primeTermQ', 'poleTerm', 'weilTest', 'classK', 'h2_sign_upto')

# ### the sends: each statement (name, file, sentence, the classes its sentence names, [(the predicate's words, its pattern on the conclusion)])
S1 = ('weights', 'testfn', 'real', 'vanish')
S2 = ('testfn', 'real', 'log2', 'vanish')
S3 = ('testfn', 'realfn', 'real', 'c2', 'cont', 'compact', 'even', 'odd')
S4 = ('testfn', 'realfn', 'real', 'cpoint', 'c2', 'cont', 'compact', 'even', 'odd')
S5 = ('weights', 'testfn', 'real', 'vanish', 'agree')
S7 = ('real', 'nat')
SF0 = ()                                                              # ### a row that binds nothing
SFK = ('testfn', 'c2', 'compact', 'evenR')                            # ### the two explicit formulas
SFC = ('nat', 'nezero', 'character', 'primitive', 'nontriv')          # ### the row at a character
# ### the autocorrelations (S4) names, as patterns: of e, of o, of h = e + o, and of a real g
WE = r'Zeta23\.EF\.weilTest \(fun u => \(e u : ℂ\)\) \(fun u => \(e u : ℂ\)\)'
WO = WE.replace('e u', 'o u')
WG = WE.replace('e u', 'g u')
WH = r'Zeta23\.EF\.weilTest \(fun u => \(\(e u \+ o u : ℝ\) : ℂ\)\) \(fun u => \(\(e u \+ o u : ℝ\) : ℂ\)\)'
SENDS = {
    's123': dict(clause='(R373)(6), statements (S1), (S2) and (S3), sent together (dispatch 1; again at dispatch 2 with (S3)`s import repaired, beside (S4) and (S5))', of7=False, files=(FF, PA), stmts=(
        ('primeTermQ_window', FF, '(S1)', S1, (
            ('the prime-power side at any weights c', r'^Schema\.primeTermQ c k ='),
            ('equal to the sum over n up to the integer part of e^L', r'= ∑ n ∈ Finset\.range \(⌊Real\.exp L⌋₊ \+ 1\), \(\(c n / Real\.sqrt n : ℝ\) : ℂ\) \* \(2 \* k \(Real\.log n\)\)$'))),
        ('primeSum_eq_primeTermQ', FF, '(S1)', S1, (
            ('zeta`s primeSum is primeTermQ at the von Mangoldt weights', r'^primeSum k = Schema\.primeTermQ \(fun n => ArithmeticFunction\.vonMangoldt n\) k$'),)),
        ('primeSum_window', FF, '(S1)', S1, (
            ('primeSum on a window is the sum over n up to the integer part of e^L', r'^primeSum k = ∑ n ∈ Finset\.range \(⌊Real\.exp L⌋₊ \+ 1\),'),)),
        ('primeSum_eq_zero_of_lt_log_two', FF, '(S2)', S2, (
            ('primeSum k = 0', r'^primeSum k = 0$'),)),
        ('paperFT_neg_half_I', PA, '(S3)', S3, (
            ('the transform at -i/2 is the integral against e^(x/2)', r'^Zeta23\.paperFT h \(-I / 2\) = ∫ u : ℝ, h u \* \(\(Real\.exp \(u / 2\) : ℝ\) : ℂ\)$'),)),
        ('paperFT_half_I', PA, '(S3)', S3, (
            ('the transform at i/2 is the integral against e^(-x/2)', r'^Zeta23\.paperFT h \(I / 2\) = ∫ u : ℝ, h u \* \(\(Real\.exp \(-u / 2\) : ℝ\) : ℂ\)$'),)),
        ('poleTerm_weilTest', PA, '(S3)', S3, (
            ('poleTerm (weilTest h h) = 2 Re(A conj B), A at -i/2 and B at i/2',
             r'^poleTerm \(Zeta23\.EF\.weilTest h h\) = \(\(2 \* \(Zeta23\.paperFT h \(-I / 2\) \* conj \(Zeta23\.paperFT h \(I / 2\)\)\)\.re : ℝ\) : ℂ\)$'),)),
        ('paperFT_real_neg_half_I', PA, '(S3)', S3, (
            ('the transform of a real g at -i/2', r'^Zeta23\.paperFT \(fun u => \(g u : ℂ\)\) \(-I / 2\) ='),
            ('is C + S', r'∫ u : ℝ, g u \* Real\.cosh \(u / 2\)\) \+ ∫ u : ℝ, g u \* Real\.sinh \(u / 2\) : ℝ\) : ℂ\)$'))),
        ('paperFT_real_half_I', PA, '(S3)', S3, (
            ('the transform of a real g at i/2', r'^Zeta23\.paperFT \(fun u => \(g u : ℂ\)\) \(I / 2\) ='),
            ('is C - S', r'∫ u : ℝ, g u \* Real\.cosh \(u / 2\)\) - ∫ u : ℝ, g u \* Real\.sinh \(u / 2\) : ℝ\) : ℂ\)$'))),
        ('poleTerm_weilTest_real', PA, '(S3)', S3, (
            ('the pole term of a real autocorrelation', r'^poleTerm \(Zeta23\.EF\.weilTest \(fun u => \(g u : ℂ\)\) \(fun u => \(g u : ℂ\)\)\) ='),
            ('is 2 (C^2 - S^2)', r'= \(\(2 \* \(\(∫ u : ℝ, g u \* Real\.cosh \(u / 2\)\) \^ 2 - \(∫ u : ℝ, g u \* Real\.sinh \(u / 2\)\) \^ 2\) : ℝ\) : ℂ\)$'))),
        ('integral_mul_sinh_eq_zero_of_even', PA, '(S3)', S3, (
            ('the integral against sinh(x/2) vanishes', r'^∫ u : ℝ, g u \* Real\.sinh \(u / 2\) = 0$'),)),
        ('integral_mul_cosh_eq_zero_of_odd', PA, '(S3)', S3, (
            ('the integral against cosh(x/2) vanishes', r'^∫ u : ℝ, g u \* Real\.cosh \(u / 2\) = 0$'),)),
        ('poleTerm_weilTest_even', PA, '(S3)', S3, (
            ('on an even real g: twice the square of the integral of g cosh(x/2)',
             r'^poleTerm \(Zeta23\.EF\.weilTest \(fun u => \(g u : ℂ\)\) \(fun u => \(g u : ℂ\)\)\) = \(\(2 \* \(∫ u : ℝ, g u \* Real\.cosh \(u / 2\)\) \^ 2 : ℝ\) : ℂ\)$'),)),
        ('poleTerm_weilTest_odd', PA, '(S3)', S3, (
            ('on an odd real g: minus twice the square of the integral of g sinh(x/2)',
             r'^poleTerm \(Zeta23\.EF\.weilTest \(fun u => \(g u : ℂ\)\) \(fun u => \(g u : ℂ\)\)\) = \(\(-\(2 \* \(∫ u : ℝ, g u \* Real\.sinh \(u / 2\)\) \^ 2\) : ℝ\) : ℂ\)$'),)),
        ('basePlateau', PA, '(S3)', S3, (
            ('its body: the plateau at ramp fraction 1/2 and half-width 1', r'^plateau \(1 / 2\) 1 '),)),
        ('oddWindow', PA, '(S3)', S3, (
            ('its body: u times basePlateau', r'^fun u => u \* basePlateau u$'),)),
        ('basePlateau_contDiff', PA, '(S3)', S3, (('twice continuously differentiable', r'^ContDiff ℝ 2 basePlateau$'),)),
        ('basePlateau_nonneg', PA, '(S3)', S3, (('at or above 0', r'^0 ≤ basePlateau u$'),)),
        ('oddWindow_contDiff', PA, '(S3)', S3, (('twice continuously differentiable', r'^ContDiff ℝ 2 oddWindow$'),)),
        ('oddWindow_hasCompactSupport', PA, '(S3)', S3, (('compact support', r'^HasCompactSupport oddWindow$'),)),
        ('oddWindow_odd', PA, '(S3)', S3, (('odd', r'^oddWindow \(-x\) = -oddWindow x$'),)),
        ('oddWindow_sinh_pos', PA, '(S3)', S3, (('its integral against sinh(x/2) positive', r'^0 < ∫ u : ℝ, oddWindow u \* Real\.sinh \(u / 2\)$'),)),
        ('exists_classK_poleTerm_re_neg', PA, '(S3)', S3, (
            ('a k in classK with the real part of poleTerm k below 0', r'^∃ k : ℝ → ℂ, classK k ∧ \(poleTerm k\)\.re < 0$'),)),
    )),
    's4': dict(clause='(R373)(6), statement (S4), sent with (S5) and with (S1) to (S3) repaired in dispatch 2, (S3) having broken at dispatch 1 on an import, so sent together and not apart; the domain classes (twice continuously differentiable, '
                      'continuous, compact support) are the domain of the form`s three terms, which the sentence`s "each of the three terms of the '
                      'form at h" takes; the seat splits (S4) into the additivity of each term and the split itself, and says so',
               of7=False, files=(PS,), stmts=(
        ('paperFT_add', PS, '(S4)', S4, (('the transform additive', r'^Zeta23\.paperFT \(fun u => f u \+ g u\) z = Zeta23\.paperFT f z \+ Zeta23\.paperFT g z$'),)),
        ('poleTerm_add', PS, '(S4)', S4, (('the pole term additive', r'^poleTerm \(fun x => f x \+ g x\) = poleTerm f \+ poleTerm g$'),)),
        ('exists_window', PS, '(S4)', S4, (('a compact support lies in a window', r'^∃ L : ℝ, ∀ u : ℝ, L < \|u\| → k u = 0$'),)),
        ('primeSum_add', PS, '(S4)', S4, (('the prime sum additive', r'^primeSum \(fun x => f x \+ g x\) = primeSum f \+ primeSum g$'),)),
        ('zeroSide_add', PS, '(S4)', S4, (('the zero side additive', r'^zeroSide \(fun x => f x \+ g x\) = zeroSide f \+ zeroSide g$'),)),
        ('archTerm_add', PS, '(S4)', S4, (('the archimedean term additive', r'^archTerm \(fun x => f x \+ g x\) = archTerm f \+ archTerm g$'),)),
        ('weilTest_ofReal_apply', PS, '(S4)', S4, (
            ('the autocorrelation of real functions at x is the integral of f(t) g(t - x)',
             r'^Zeta23\.EF\.weilTest \(fun u => \(f u : ℂ\)\) \(fun u => \(g u : ℂ\)\) x = \(\(∫ t : ℝ, f t \* g \(t - x\) : ℝ\) : ℂ\)$'),)),
        ('integral_parity_split', PS, '(S4)', S4, (
            ('the cross terms cancel', r'^∫ t : ℝ, \(e t \+ o t\) \* \(e \(t - x\) \+ o \(t - x\)\) = \(∫ t : ℝ, e t \* e \(t - x\)\) \+ ∫ t : ℝ, o t \* o \(t - x\)$'),)),
        ('weilTest_parity_split', PS, '(S4)', S4, (
            ('weilTest h h = weilTest e e + weilTest o o as functions', r'^%s = fun x => %s x \+ %s x$' % (WH, WE, WO)),)),
        ('autocorr_facts', PS, '(S4)', S4, (
            ('the autocorrelation twice continuously differentiable', r'^ContDiff ℝ 2 \(%s\) ∧' % WG),
            ('with compact support', r'∧ HasCompactSupport \(%s\) ∧' % WG),
            ('and even', r'∧ ∀ x, %s \(-x\) = %s x$' % (WG, WG)))),
        ('poleTerm_parity_split', PS, '(S4)', S4, (('the pole term at h is its sum at e and at o', r'^poleTerm \(%s\) = poleTerm \(%s\) \+ poleTerm \(%s\)$' % (WH, WE, WO)),)),
        ('primeSum_parity_split', PS, '(S4)', S4, (('the prime sum at h is its sum at e and at o', r'^primeSum \(%s\) = primeSum \(%s\) \+ primeSum \(%s\)$' % (WH, WE, WO)),)),
        ('archTerm_parity_split', PS, '(S4)', S4, (('the archimedean term at h is its sum at e and at o', r'^archTerm \(%s\) = archTerm \(%s\) \+ archTerm \(%s\)$' % (WH, WE, WO)),)),
        ('form_parity_split', PS, '(S4)', S4, (
            ('the form at h', r'^poleTerm \(%s\) - primeSum \(%s\) \+ archTerm \(%s\) =' % (WH, WH, WH)),
            ('is the form at e plus the form at o', r'= \(poleTerm \(%s\) - primeSum \(%s\) \+ archTerm \(%s\)\) \+ \(poleTerm \(%s\) - primeSum \(%s\) \+ archTerm \(%s\)\)$'
             % (WE, WE, WE, WO, WO, WO)))),
    )),
    's5': dict(clause='(R373)(6), statement (S5), sent with (S4) and with (S1) to (S3) repaired in dispatch 2, so sent together and not apart, importing FormFinite and DetectionRegion and neither (S3) nor (S4); the seat splits (S5) into the set, the linearity of the '
                      'prime-power side in the weights on a window, the convexity, the congruence and the von Mangoldt membership, and says so',
               of7=False, files=(AW,), stmts=(
        ('admissibleWeights', AW, '(S5)', S5, (
            ('its body: the weights c at which pole term less prime-power side with c plus archimedean term is at or above 0 on each window in classK of width L',
             r'^\{c \| ∀ k : ℝ → ℂ, classK k → \(∀ u : ℝ, L < \|u\| → k u = 0\) → 0 ≤ poleTerm k - Schema\.primeTermQ c k \+ archTerm k\}$'),)),
        ('primeTermQ_combo', AW, '(S5)', S5, (
            ('on a window the prime-power side is linear in the weights',
             r'^Schema\.primeTermQ \(a • c₁ \+ b • c₂\) k = \(a : ℂ\) \* Schema\.primeTermQ c₁ k \+ \(b : ℂ\) \* Schema\.primeTermQ c₂ k$'),)),
        ('admissibleWeights_convex', AW, '(S5)', S5, (('convex at each width', r'^Convex ℝ \(admissibleWeights L\)$'),)),
        ('admissibleWeights_congr', AW, '(S5)', S5, (
            ('membership turns on the weights up to the integer part of e^L', r'^c₁ ∈ admissibleWeights L ↔ c₂ ∈ admissibleWeights L$'),)),
        ('h2_sign_upto_iff_mem', AW, '(S5)', S5, (
            ('h2_sign_upto L says that the von Mangoldt function is a member',
             r'^h2_sign_upto L ↔ \(fun n : ℕ => ArithmeticFunction\.vonMangoldt n\) ∈ admissibleWeights L$'),)),
    )),
    's7': dict(clause='(R373)(7), the statement of each form the table prices, FORM B and FORM A, each a definition of a Prop in a file of its own, '
                      'with no sorry and no proof, compiled by one dispatch on push-b763-arith before any line of a proof; FORM B`s named window '
                      'in eight definitions beside them (the B-spline of order 6 carried onto [-log 32, log 32], the family`s frequency as relay '
                      'data/b709_grid.txt :46 prints it, the window of kind N, its autocorrelation and the width log 1024); FORM A takes n as its '
                      'parameter, no bank naming n',
               of7=True, files=(CF,), stmts=(
        ('bsplineSix', CF, '(7) B', S7, (
            ('its body: the cardinal B-spline of order 6, (1/120) times the sum over j up to 6 of (-1)^j C(6, j) (x - j)_+^5',
             r'^\(1 / 120\) \* ∑ j ∈ Finset\.range 7, \(-1 : ℝ\) \^ j \* \(Nat\.choose 6 j : ℝ\) \* \(max \(x - j\) 0\) \^ 5$'),)),
        ('witnessStep', CF, '(7) B', S7, (('its body: a third of log 32', r'^Real\.log 32 / 3$'),)),
        ('witnessPhi', CF, '(7) B', S7, (
            ('its body: the B-spline carried onto [-log 32, log 32]', r'^bsplineSix \(\(u \+ Real\.log 32\) / witnessStep\) / witnessStep$'),)),
        ('witnessFreq', CF, '(7) B', S7, (
            ('its body: the family`s frequency, 16.290215720390390792963', r'^16290215720390390792963 / 10 \^ 21$'),)),
        ('witnessCos', CF, '(7) B', S7, (('its body: cos(g u) phi(u)', r'^Real\.cos \(witnessFreq \* u\) \* witnessPhi u$'),)),
        ('witnessH', CF, '(7) B', S7, (
            ('its body: the window of kind N, (g^2 + D^2)[cos(g u) phi(u)]', r'^witnessFreq \^ 2 \* witnessCos u \+ deriv \(deriv witnessCos\) u$'),)),
        ('witnessK', CF, '(7) B', S7, (
            ('its body: the autocorrelation of the window', r'^Zeta23\.EF\.weilTest \(fun u => \(witnessH u : ℂ\)\) \(fun u => \(witnessH u : ℂ\)\)$'),)),
        ('witnessWidth', CF, '(7) B', S7, (('its body: the width log 1024', r'^Real\.log 1024$'),)),
        ('ControlFailureB', CF, '(7) B', S7, (
            ('the named k in classK', r'^classK witnessK ∧'),
            ('vanishing outside [-L, L], L named', r'∧ \(∀ u : ℝ, witnessWidth < \|u\| → witnessK u = 0\) ∧'),
            ('the real part of poleTerm k - primeTermQ cQ k + archTermQ k below 0',
             r'∧ \(poleTerm witnessK - Schema\.primeTermQ Schema\.ZQ\.cQ witnessK \+ Schema\.archTermQ witnessK\)\.re < 0$'))),
        ('ControlFailureA', CF, '(7) A', S7, (
            ('Wide.liCoeff zqZeroConfig n < 0', r'^Schema\.Wide\.liCoeff Schema\.ZQ\.zqZeroConfig n < 0$'),)),
    )),
    'sf': dict(clause='(R373)(6), "with them, on the same branch": the statement file of W-ORD-STATEMENT-FILE (OPEN_TRAILS :18889), priced within '
                      'this build (data/b763_price.txt :22); One Page v2.0`s Correspondence (day1/ONE_PAGE_PROOF_v2_0.md :36-:54), the 19 rows '
                      'of SIDE-explicit-formula, each stated apart from its proof and closed by the name the row cites, the two definitions as '
                      'their unfolding; the three rows of SIDE-kernel v1.5 (:55-:57) named in its docstring, that kernel not imported',
               of7=False, files=(OP,), stmts=(
        ('classK_def', OP, ':36', ('testfn',), (
            ('the class of test functions, unfolded', r'^B321\.classK k ↔ \(\(∀ x : ℝ, k \(-x\) = k x\) ∧ ContDiff ℝ 2 k ∧ HasCompactSupport k ∧ ∃ h : ℝ → ℂ, ContDiff ℝ 2 h ∧ HasCompactSupport h ∧ k = Zeta23\.EF\.weilTest h h\)$'),)),
        ('h2_sign_def', OP, ':37', SF0, (
            ('the clause, unfolded', r'^B321\.h2_sign ↔ ∀ k : ℝ → ℂ, B321\.classK k → 0 ≤ B321\.poleTerm k - B321\.primeSum k \+ B321\.archTerm k$'),)),
        ('b321_identity', OP, ':38', SFK, (
            ('the explicit formula for zeta', r'^B321\.zeroSide k = B321\.b321Norm \* \(B321\.poleTerm k - B321\.primeSum k \+ B321\.archTerm k\)$'),)),
        ('h2_sign_iff_rh', OP, ':39', SF0, (('the clause is equivalent to the Riemann Hypothesis', r'^B321\.h2_sign ↔ RiemannHypothesis$'),)),
        ('h2_sign_chi_iff_grh_chi', OP, ':40', SFC, (
            ('the same at a primitive character other than 1', r'^GRHWeil\.h2_sign_chi χ ↔ GRHWeil\.GRH_chi χ$'),)),
        ('h2_sign_cfg_iff_target', OP, ':41', ('config',), (('the same over a configuration', r'^Schema\.h2_sign_cfg C ↔ C\.target$'),)),
        ('li_nonneg_iff_rh', OP, ':42', SF0, (('Li`s criterion', r'^\(∀ n : ℕ, 0 ≤ LiWeil\.LiCoeff n\) ↔ RiemannHypothesis$'),)),
        ('arith_limit_nonneg_iff_rh', OP, ':43', SF0, (
            ('the Bombieri-Lagarias form', r'^\(∀ \(n : ℕ\) \(L : ℂ\), Filter\.Tendsto \(fun δ => Zeta23\.EF\.literatureRHS \(LiWeil\.symMember n δ\)\) \(𝓝\[>\] 0\) \(𝓝 L\) → 0 ≤ L\.re\) ↔ RiemannHypothesis$'),)),
        ('h2_sign_iff_forall_upto', OP, ':44', SF0, (('bounded support', r'^B321\.h2_sign ↔ ∀ L₀ : ℝ, B321\.h2_sign_upto L₀$'),)),
        ('liCoeff_one_pos', OP, ':45', SF0, (('λ₁ > 0', r'^0 < LiWeil\.LiCoeff 1$'),)),
        ('zeta_box', OP, ':46', SF0, (
            ('a zero of zeta on the line between heights 12 and 16', r'^∃ ρ : ℂ, riemannZeta ρ = 0 ∧ ρ\.re = 1 / 2 ∧ \(12 : ℝ\) < ρ\.im ∧ ρ\.im < 16$'),)),
        ('zq_explicit_formula_instance', OP, ':47', SFK, (
            ('the explicit formula for the control', r'^Schema\.zeroSideQ Schema\.ZQ\.zqZeroConfig k = B321\.poleTerm k - Schema\.primeTermQ \(fun n => Schema\.ZQ\.cQ n\) k \+ Schema\.archTermQ k$'),)),
        ('zq_offline_zero', OP, ':48', SF0, (('a zero of the control off the line', r'^∃ ρ ∈ \(Schema\.ZQ\.zqZeroConfig\)\.carrier, ρ\.re ≠ 1 / 2$'),)),
        ('zq_weil_positivity_fails', OP, ':49', SF0, (
            ('the inequality fails for the control, on the arithmetic side', r'^¬ ∀ k : ℝ → ℂ, B321\.classK k → 0 ≤ B321\.poleTerm k - Schema\.primeTermQ \(fun n => Schema\.ZQ\.cQ n\) k \+ Schema\.archTermQ k$'),)),
        ('zq_li_nonneg_fails', OP, ':50', SF0, (('Li`s nonnegativity fails for the control', r'^¬ \(∀ n : ℕ, 0 ≤ Schema\.Wide\.liCoeff Schema\.ZQ\.zqZeroConfig n\)$'),)),
        ('zq_coeff_not_multiplicative', OP, ':51', SF0, (
            ('the coefficients of the control not multiplicative', r'^¬ ArithmeticFunction\.IsMultiplicative \(⟨fun n => \(Schema\.rQ n : ℝ\) / 2, by simp \[Schema\.rQ_zero\]⟩ : ArithmeticFunction ℝ\)$'),)),
        ('zeta_isMultiplicative_control', OP, ':52', SF0, (
            ('the coefficients of zeta multiplicative', r'^ArithmeticFunction\.IsMultiplicative ArithmeticFunction\.zeta$'),)),
        ('cQ_not_nonneg', OP, ':53', SF0, (('the log-derivative coefficients of the control not all nonnegative', r'^¬ \(∀ n : ℕ, 0 ≤ Schema\.ZQ\.cQ n\)$'),)),
        ('vonMangoldt_nonneg_control', OP, ':54', ('nat',), (('Λ nonnegative', r'^0 ≤ ArithmeticFunction\.vonMangoldt n$'),)),
    )),
    's24': dict(clause='(R373)(8), W-ORD-SQUARES-AT-24 under [A4], its home SIDE-explicit-formula (OPEN_TRAILS :18503, its price :18563): a prime '
                       'above 3 has -1, 2 and 3 all squares modulo it exactly when it is 1 modulo 24, by Mathlib`s supplementary laws for -1 and 2 '
                       'and reciprocity at 3; on a push-b763-* branch of its own, after Component 3, where the ceiling leaves its upper figure',
                of7=False, files=(SQ,), stmts=(
        ('not_isSquare_two_zmod_three', SQ, '(8) SQUARES-AT-24', SF0, (('2 not a square modulo 3', r'^¬ IsSquare \(2 : ZMod 3\)$'),)),
        ('isSquare_three_iff', SQ, '(8) SQUARES-AT-24', ('nat', 'factprime', 'above3', 'mod4'), (
            ('3 a square modulo p exactly when p is 1 modulo 3', r'^IsSquare \(3 : ZMod p\) ↔ p % 3 = 1$'),)),
        ('squares_at_24', SQ, '(8) SQUARES-AT-24', ('nat', 'prime', 'above3'), (
            ('-1, 2 and 3 all squares modulo p exactly when p is 1 modulo 24',
             r'^\(IsSquare \(-1 : ZMod p\) ∧ IsSquare \(2 : ZMod p\) ∧ IsSquare \(3 : ZMod p\)\) ↔ p % 24 = 1$'),)),
    )),
}

# ### the no-zero control's barred modules and names ((R373)(7))
OFFZERO = 'SIDEExplicitFormula.Schema.ZQ.OffZero'
DETECTOR = 'SIDEExplicitFormula.Schema.Detector'
WIDE = 'SIDEExplicitFormula.Schema.Wide.'
BARRED_NAMES = ('zq_offline_zero', 'wide_detector', 'detector', 'zq_arith_side_re_neg', 'zq_li_nonneg_fails')
NAMED = re.compile(r"(?<![\w'])(%s)(?![\w'])" % '|'.join(BARRED_NAMES))
DECL_DETECTOR = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*(?:theorem|lemma|def|abbrev)\s+[\w.']*detector",
                           re.M | re.I)


def _ws(s):
    return ' '.join(s.split())


def _dig(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def blank_comments(t):
    """the text with every comment and docstring blanked to spaces, each newline kept, so line numbers stand."""
    out, i, n, depth = [], 0, len(t), 0
    while i < n:
        if t.startswith('/-', i):
            depth += 1
            out.append('  ')
            i += 2
        elif depth and t.startswith('-/', i):
            depth -= 1
            out.append('  ')
            i += 2
        elif depth:
            out.append(NL if t[i] == NL else ' ')
            i += 1
        elif t.startswith('--', i):
            j = t.find(NL, i)
            j = n if j < 0 else j
            out.append(' ' * (j - i))
            i = j
        elif t[i] == '"':
            j = i + 1
            while j < n and t[j] != '"':
                j += 2 if t[j] == '\\' else 1
            out.append(t[i:j + 1])
            i = j + 1
        else:
            out.append(t[i])
            i += 1
    return ''.join(out)


OPEN, CLOSE = '({[⦃⟨', ')}]⦄⟩'


def _group_end(s, i):
    d = 0
    for j in range(i, len(s)):
        if s[j] in OPEN:
            d += 1
        elif s[j] in CLOSE:
            d -= 1
            if d == 0:
                return j
    return -1


def header(text, name):
    """(kind, line, [(binder names, type)], the type, the body to the next blank line) of the declaration `name`, read from the text with its
    comments blanked; None where no declaration of that name opens a line."""
    t = blank_comments(text.replace('\r', ''))
    m = re.search(r"^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*(theorem|lemma|def|abbrev)\s+%s(?=[\s:({\[⦃])" % re.escape(name), t, re.M)
    if not m:
        return None
    line = t[:m.start()].count(NL) + 1
    rest, i, binders = t[m.end():], 0, []
    while i < len(rest):
        if rest[i].isspace():
            i += 1
            continue
        if rest[i] in '({[⦃':
            j = _group_end(rest, i)
            if j < 0:
                return None
            inner, d, k = rest[i + 1:j], 0, None
            for q, ch in enumerate(inner):
                if ch in OPEN:
                    d += 1
                elif ch in CLOSE:
                    d -= 1
                elif ch == ':' and d == 0 and not inner.startswith(':=', q):
                    k = q
                    break
            binders.append((_ws(inner[:k]) if k is not None else '', _ws(inner[k + 1:]) if k is not None else _ws(inner)))
            i = j + 1
            continue
        break
    tail, typ = rest[i:], ''
    if tail.startswith(':='):
        k = 0
    elif tail.startswith(':'):
        d, k = 0, 1
        while k < len(tail):
            c = tail[k]
            if c in OPEN:
                d += 1
            elif c in CLOSE:
                d -= 1
            elif d == 0 and tail.startswith(':=', k):
                break
            k += 1
        typ = tail[1:k]
    else:
        return None
    body = re.split(r'\n\s*\n', tail[k + 2:], maxsplit=1)[0]
    return m.group(1), line, binders, _ws(typ), _ws(body)


def classify(typ):
    for k, _w, pat in CLASSES:
        if re.fullmatch(pat, typ):
            return k
    return None


def file_facts(text):
    """the file's checks with comments blanked: counts of sorry/admit, axiom, variable, unsafe, implemented_by/extern, skipKernelTC, lemma."""
    c = blank_comments(text.replace('\r', ''))
    cnt = lambda pat: len(re.findall(pat, c, re.M))  # noqa: E731
    return dict(sorry=cnt(r'(?<![\w.])(?:sorry|admit)(?![\w])'), axiom=cnt(r'^\s*(?:private\s+)?axiom\s'), variable=cnt(r'^\s*variable\b'),
                unsafe=cnt(r'(?<![\w.])unsafe(?![\w])'), extern=cnt(r'implemented_by|@\[extern'), skip=cnt(r'skipKernelTC'),
                lemma=cnt(r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected)\s+)?lemma\s'),
                imports=[x for x in P.imports_of(text.replace('\r', ''))])


def def_at(get, name, path):
    """(line, digest of the definition's text to its next blank line) of `def name` in the file at the revision; (0, '') where unread."""
    tx = get(path)
    if not tx:
        return 0, ''
    h = header(tx, name)
    if not h or h[0] not in ('def', 'abbrev'):
        return 0, ''
    return h[1], _dig(_ws('%s %s %s' % (' '.join('(%s : %s)' % b for b in h[2]), h[3], h[4])))


def salt_of(get, send, def_get=None):
    """the salt check of a send, pure over `get(path) -> text`: (lines, passed, statements passed, statements)."""
    S = SENDS[send] if isinstance(send, str) else send
    L, ok_all, n_ok = [], True, 0
    texts = dict((f, get(f) or '') for f in S['files'])
    for f in S['files']:
        ff = file_facts(texts[f])
        clean = texts[f] != '' and not (ff['sorry'] or ff['axiom'] or ff['variable'] or ff['unsafe'] or ff['extern'] or ff['skip'])
        ok_all = ok_all and clean
        L.append('  THE FILE %s: %s ; sorry or admit %d ; axiom %d ; variable %d ; unsafe %d ; implemented_by or extern %d ; skipKernelTC %d ; '
                 'lemma %d ; imports %s -> %s' % (f, 'READ, %d lines, sha256 %s' % (texts[f].count(NL) + 1, _dig(texts[f])) if texts[f] else 'UNREAD',
                                                 ff['sorry'], ff['axiom'], ff['variable'], ff['unsafe'], ff['extern'], ff['skip'], ff['lemma'],
                                                 ' '.join(ff['imports']) or 'none', 'CLEAN' if clean else 'REFUSED'))
    for name, f, sent, allowed, preds in S['stmts']:
        h = header(texts.get(f, ''), name)
        if not h:
            ok_all = False
            L.append('  %s %s (%s): UNREAD -- no declaration of that name opens a line -> REFUSED' % (sent, name, f))
            continue
        kind, line, binders, typ, body = h
        concl = body if kind in ('def', 'abbrev') else typ
        hyp, bad = [], []
        for names, btyp in binders:
            k = classify(btyp)
            for nm in (names.split() or ['(anonymous)']):
                if k is None:
                    bad.append(nm)
                    hyp.append('%s UNCLASSED (its type sha256 %s)' % (nm, _dig(btyp)))
                elif k not in allowed:
                    bad.append(nm)
                    hyp.append('%s %s, A CLASS THE SENTENCE DOES NOT NAME' % (nm, CLASS_WORDS[k]))
                else:
                    hyp.append('%s %s' % (nm, CLASS_WORDS[k]))
        pr = [(w, bool(re.search(p, concl))) for w, p in preds]
        rests = [nm for nm, _p in DEFS if re.search(r"(?<![\w'])(?:[\w']+\.)*%s(?![\w'])" % re.escape(nm), _ws(' '.join(b[1] for b in binders) + ' ' + concl))]
        dg = def_get or get
        passed = not bad and all(v for _w, v in pr)
        ok_all = ok_all and passed
        n_ok += 1 if passed else 0
        L.append('  %s %s, a %s at %s :%d (its header sha256 %s): %s' % (sent, name, kind, f, line, _dig(_ws(' '.join('(%s : %s)' % b for b in binders)) + ' : ' + concl),
                                                                         'PASSED' if passed else 'REFUSED'))
        L.append('     binds: %s' % ('; '.join(hyp) if hyp else 'no hypothesis'))
        L.append('     concludes: %s' % ' ; '.join('%s %s' % (w, 'HOLDS' if v else 'DOES NOT HOLD') for w, v in pr))
        L.append('     rests on: %s ; of the ruling`s six: %s' % (
            ', '.join('%s (%s :%d, sha256 %s)' % ((nm, dict(DEFS)[nm]) + def_at(dg, nm, dict(DEFS)[nm])) for nm in rests) or 'none of DEFS',
            ', '.join(nm for nm in SIX if nm in rests) or 'none'))
    return L, ok_all, n_ok, len(S['stmts'])


def wide_carriers(get, files):
    """the modules under Schema/Wide whose text declares a name holding "detector"."""
    out = []
    for p in sorted(files):
        if p.startswith('SIDEExplicitFormula/Schema/Wide/') and p.endswith('.lean'):
            if DECL_DETECTOR.search(blank_comments((get(p) or '').replace('\r', ''))):
                out.append(p[:-5].replace('/', '.'))
    return out


def zero_of(text, carriers, path='(planted)'):
    """the no-zero control over one file's text, pure: (lines, passed)."""
    t = (text or '').replace('\r', '')
    imps = P.imports_of(t)
    barred = [m for m in imps if m == OFFZERO or m.startswith(OFFZERO + '.') or m == DETECTOR or (m.startswith(WIDE) and m in carriers)]
    code = blank_comments(t)
    named = sorted(set(NAMED.findall(code)))
    prose = len(NAMED.findall(t)) - len(NAMED.findall(code))
    passed = bool(t) and not barred and not named
    L = ['  THE NO-ZERO CONTROL over %s: %s ; its imports %d (%s) ; barred among them %d%s ; the five names in its code %d%s ; in its prose %d, '
         'not read -> %s' % (path, 'READ' if t else 'UNREAD', len(imps), ' '.join(imps) or 'none', len(barred),
                              (' (' + ' '.join(barred) + ')') if barred else '', len(named), (' (' + ' '.join(named) + ')') if named else '', prose,
                              'PASSED' if passed else 'REFUSED')]
    return L, passed


def _getter(rev):
    cache = {}

    def get(path):
        if path not in cache:
            cache[path] = P.J.g('show', '%s:%s' % (rev, path))
        return cache[path]
    return get


def zero_at(rev, path):
    sha = P.J.g('rev-parse', rev).strip()
    get = _getter(sha)
    files = P.tree_files(sha)
    car = wide_carriers(get, files)
    L, ok = zero_of(get(path), car, path)
    # ### beside, as information: the barred modules in the file's import closure in the tree
    libs = P.J.libs_at(sha)
    mod = path[:-5].replace('/', '.')
    texts, _out = P.closure([mod], sha, libs, files)
    up = sorted(m for m in texts if m != mod and (m == DETECTOR or m.startswith(OFFZERO) or m in car))
    return ['## THE NO-ZERO CONTROL AT %s (%s)' % (rev, sha[:8]),
            '  the modules under Schema/Wide carrying a detector at %s: %d (%s)' % (sha[:8], len(car), ' '.join(car))] + L + [
            '  BESIDE, NOT THE CONTROL: the file`s import closure in the tree %d modules, of them barred by the control`s list %d (%s); the ruling '
            'bars the file`s own imports' % (len(texts), len(up), ' '.join(up[:6]) + (' ...' if len(up) > 6 else ''))], ok


def salt_at(rev, send):
    sha = P.J.g('rev-parse', rev).strip()
    L, ok, n_ok, n = salt_of(_getter(sha), send)
    return ['## THE SALT CHECK OF SEND %s AT %s (%s): %s' % (send, rev, sha[:8], SENDS[send]['clause'])] + L, ok, n_ok, n


def salt_controls():
    L, ok = [], []
    good = ['import SIDEExplicitFormula.Schema.EpsteinZQ', '', '/-- prose: a sorry and a detector named in a docstring -/',
            'theorem t (c : ℕ → ℝ) (k : ℝ → ℂ) (L : ℝ) (hk : ∀ u : ℝ, L < |u| → k u = 0) :',
            '    Schema.primeTermQ c k =',
            '      ∑ n ∈ Finset.range (⌊Real.exp L⌋₊ + 1), ((c n / Real.sqrt n : ℝ) : ℂ) * (2 * k (Real.log n)) := by',
            '  simp -- a sorry in a line comment', '']
    spec = dict(clause='planted', files=('F.lean',), stmts=(('t', 'F.lean', '(S1)', S1, SENDS['s123']['stmts'][0][4]),))
    cases = [('the planted statement as its sentence words it', good, True),
             ('a hypothesis beyond the sentence bound', good[:3] + [good[3][:-2] + ' (hRH : RiemannHypothesis) :'] + good[4:], False),
             ('a hypothesis of a class the sentence does not name (L below log 2 on (S1))',
              good[:3] + [good[3][:-2] + ' (hL : L < Real.log 2) :'] + good[4:], False),
             ('the conclusion short of its sentence (the range to the floor of e^L)', good[:5] + [good[5].replace('⌋₊ + 1)', '⌋₊)')] + good[6:], False),
             ('a sorry in the proof', good[:6] + ['  sorry', ''], False),
             ('the statement absent (renamed)', good[:3] + [good[3].replace('theorem t ', 'theorem t2 ')] + good[4:], False),
             ('a variable line in the file', good[:2] + ['variable (hRH : RiemannHypothesis)', ''] + good[2:], False),
             ('a lemma in place of a theorem, counted and not refused', good[:3] + [good[3].replace('theorem t ', 'lemma t ')] + good[4:], True)]
    for what, lines, want in cases:
        _L, got, _a, _b = salt_of(lambda p, x=NL.join(lines): x, spec, def_get=lambda p: '')
        ok.append(got == want)
        L.append('  (s%d) %s: %s -> %s' % (len(ok), what, 'PASSED' if got else 'REFUSED', 'AS WANTED' if got == want else 'NOT AS WANTED'))
    return L, ok


def zero_controls():
    L, ok = [], []
    car = ['SIDEExplicitFormula.Schema.Wide.HalfScale']
    base = ['import SIDEExplicitFormula.Schema.EpsteinZQ', '', '/-- prose: no detector and no zq_offline_zero here -/',
            'theorem t : Schema.ZQ.cQ 4 = 0 := by', '  simp -- detector in a line comment', '']
    cases = [('a clean file, the barred names in its prose alone', base, True),
             ('Schema/Detector imported', ['import SIDEExplicitFormula.Schema.Detector'] + base, False),
             ('a module under Schema/ZQ/OffZero imported', ['import SIDEExplicitFormula.Schema.ZQ.OffZero.Box'] + base, False),
             ('a Schema/Wide module carrying a detector imported', ['import SIDEExplicitFormula.Schema.Wide.HalfScale'] + base, False),
             ('a Schema/Wide module carrying none imported', ['import SIDEExplicitFormula.Schema.Wide.Config'] + base, True),
             ('zq_li_nonneg_fails named in code', base[:4] + ['  exact (zq_li_nonneg_fails).elim', ''], False),
             ('detector named, qualified, in code', base[:4] + ['  exact Schema.detector', ''], False),
             ('a name holding detector as a part (detectorBase), not one of the five', base[:4] + ['  exact detectorBase', ''], True)]
    for what, lines, want in cases:
        _L, got = zero_of(NL.join(lines), car)
        ok.append(got == want)
        L.append('  (z%d) %s: %s -> %s' % (len(ok), what, 'PASSED' if got else 'REFUSED', 'AS WANTED' if got == want else 'NOT AS WANTED'))
    # ### at a real revision: v0.41, where Schema/Wide/HalfScale imports Schema/Detector and declares wide_detector
    zl, zp = zero_at('a3aad4cceb41705fe9929c9b5600976eaf7434b5', 'SIDEExplicitFormula/Schema/Wide/HalfScale.lean')
    ok.append(zp is False)
    L.append('  (z%d) at v0.41, Schema/Wide/HalfScale.lean over itself: %s -> %s' % (len(ok), 'PASSED' if zp else 'REFUSED', 'AS WANTED' if zp is False else 'NOT AS WANTED'))
    sha41 = P.J.g('rev-parse', 'a3aad4cceb41705fe9929c9b5600976eaf7434b5').strip()
    hs = 'SIDEExplicitFormula.Schema.Wide.HalfScale' in wide_carriers(_getter(sha41), P.tree_files(sha41))
    ok.append(hs)
    L.append('  (z%d) at v0.41, Schema/Wide/HalfScale read among the Schema/Wide modules carrying a detector: %s -> %s' % (
        len(ok), 'YES' if hs else 'NO', 'AS WANTED' if hs else 'NOT AS WANTED'))
    # ### the salt check at v0.41, where no statement of (6) stands: refused
    _sl, sp, _a, _b = salt_of(_getter('a3aad4cceb41705fe9929c9b5600976eaf7434b5'), 's123')
    ok.append(sp is False)
    L.append('  (z%d) at v0.41, the salt check of send s123, no file of (6) in the tree: %s -> %s' % (len(ok), 'PASSED' if sp else 'REFUSED',
                                                                                                    'AS WANTED' if sp is False else 'NOT AS WANTED'))
    return L, ok


def all_controls():
    L, ok = P.controls()
    sL, sok = salt_controls()
    zL, zok = zero_controls()
    return (L + ['  THE SALT CHECK`S PLANTED CONTROLS:'] + sL + ['  THE NO-ZERO CONTROL`S PLANTED CONTROLS, AND THREE AT v0.41:'] + zL,
            ok + sok + zok)


def cmd_bank(before, tip, send):
    if send not in SENDS:
        sys.exit('### no send %r -- the sends: %s' % (send, ' '.join(sorted(SENDS))))
    L, ok = all_controls()
    lb, fb = P.read_at(before)
    lt, ft = P.read_at(tip)
    st, spass, n_ok, n = salt_at(tip, send)
    zl, zpass = [], True
    if SENDS[send]['of7']:
        for f in SENDS[send]['files']:
            l_, p_ = zero_at(tip, f)
            zl += l_
            zpass = zpass and p_
    known = ft['filtered'] == KNOWN
    bank = os.path.join(D, '%s_presend_%s.txt' % (ACT, send))
    out = ['%s -- (R373)(5), (6), (7): THE PRE-SEND READS OF (R368)(4), CARRIED, AND THE SALT CHECK OF SEND %s, IN SIDE-explicit-formula, BEFORE '
           'THE DISPATCH (%s)' % (ACT, send, P._now()), '',
           '### (i) each fully qualified declaration name in one module, over the targets` modules and their import closure in the tree, the',
           '### duplicates printed, 0 wanted at the tip; (ii) each line of print_targets.txt against build-module.yml :91`s filter, the lines it',
           '### refuses printed, the two known wanted (:358 and :359); the file not edited for them, the workflow not widened. The reads and their',
           '### controls are tools/b758_presend.py`s, imported and not changed. THE SALT CHECK is this tool`s: each statement`s hypotheses classed',
           '### against its sentence, its conclusion read against the sentence`s predicates, the definitions it rests on by file, line and digest;',
           '### each kernel line by predicate, line number and digest alone, none quoted.',
           '', '## THE CONTROLS'] + L + ['', '### main as b762 left it (v0.41), where the branch is made'] + lb + [
           '', '### the tip the dispatch is sent at'] + lt + ['', '### %s: the salt check, printed before the send' % SENDS[send]['clause']] + st + (
           (['', '### (R373)(7): the no-zero control over the send`s files, printed before the send'] + zl) if SENDS[send]['of7'] else []) + ['',
           '### ### **THE PRE-SEND READS AT %s: DUPLICATES %d (OVER THE TARGETS %d) ; ANONYMOUS PAIRS %d (OF %d, %d UNREAD) ; REFUSED BY THE FILTER %d (%s), '
           'THE TWO KNOWN %s ; TARGETS %d MODULES FOR %d NAMES, %d REFUSED, MODULES REFUSED %d ; THE SALT CHECK OF SEND %s %s (%d OF %d STATEMENTS)%s ; '
           'CONTROLS %d OF %d.**' % (
               ft['sha'][:8], ft['dup_c'], ft['dup_t'], ft['anon_pairs'], ft['anon'], ft['anon_unread'], len(ft['filtered']),
               ', '.join(':%d' % k for k in ft['filtered']) or 'none', 'YES' if known else 'NO', ft['modules'], ft['names'], ft['refused_targets'],
               ft['target_refused'], send, 'PASSED' if spass else 'REFUSED', n_ok, n,
               (' ; THE NO-ZERO CONTROL %s' % ('PASSED' if zpass else 'REFUSED')) if SENDS[send]['of7'] else '', sum(ok), len(ok))]
    r = FB.write(bank, NL.join(out))
    print(NL.join(out))
    print('written data/%s ; figbank: %s' % (os.path.basename(bank), r['why']))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        L_, ok_ = all_controls()
        print(NL.join(L_))
        print('### CONTROLS %d OF %d AS WANTED' % (sum(ok_), len(ok_)))
    elif a[:1] == ['read'] and len(a) == 2:
        P.cmd_read(a[1])
    elif a[:1] == ['salt'] and len(a) == 3 and a[2] in SENDS:
        sL_, sp_, n_ok_, n_ = salt_at(a[1], a[2])
        print(NL.join(sL_))
        print('### THE SALT CHECK OF SEND %s %s (%d OF %d STATEMENTS)' % (a[2], 'PASSED' if sp_ else 'REFUSED', n_ok_, n_))
    elif a[:1] == ['zero'] and len(a) == 3:
        zL_, zp_ = zero_at(a[1], a[2])
        print(NL.join(zL_))
        print('### THE NO-ZERO CONTROL %s' % ('PASSED' if zp_ else 'REFUSED'))
    elif a[:1] == ['bank'] and len(a) == 4:
        cmd_bank(a[1], a[2], a[3])
    else:
        sys.exit(__doc__)
