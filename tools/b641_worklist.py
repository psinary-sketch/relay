# -*- coding: utf-8 -*-
"""b641_worklist.py -- THE ACT'S DATA, UNDER (R251). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b641: LANE THREE, ACT SIXTY-EIGHT -- THE NEEDLE AND THE ROOT ORDER; THE PROVENANCE OF A PHRASE; THE RESEARCH DISCHARGE -- KEIPER'S
### SEVEN, THE WINDOW'S TWO, THE EPSTEIN COUNT FIELD, THE DEDEKIND PREMISES, THE PATCH VERSIONS -- EACH TO ONE STATUS WITH ITS REASON; THE
### OPENAI/MATH SOURCES READ AND BANKED; W-ORD-STATEMENT-PIN ENTERED.
### Here: the pins before the act; the lists in force; the obligations read at their pin with the seat's read of what would discharge each,
### written before the seal from the kernel source, Mathlib at the kernel's pin and the references fetched (each fetch's digest banked); the
### clone's path; the sealed tools; the next act.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
GS = 'D:/SIDE-global-section'
PRE_PP = 'e8320b5'          # ### PLACE-papers main before the act (b640's record and correction)
PRE_RELAY = 'c7c31e0c'      # ### relay main before the act (b640's closing, answers re-banked)
STEPZERO = '43e02fa1'       # ### relay: b640's closing push-out bank, committed at step zero
NEEDLE_COMMIT = 'c607f25c'  # ### relay: Question 1's needle repaired with its test, alone (Component 0)
ORDER_COMMIT = 'a2b0c105'   # ### relay: W-ORD-ROOT-ORDER in tools/act_root.py with its test, alone (Component 0)
DATE = '2026-10-08'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/e594f88a-2fab-4757-943d-7ab1bc3de815/scratchpad'
PLANTED_DIR = SP + '/b637_planted'
CLONE = SP + '/openai-math'
CLONE_URL = 'https://github.com/openai/math'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b638_nodes_zeta.txt', 'chi': 'b638_nodes_chi.txt'}
PROBE = {'zeta': 'b635_probe_out_zeta.txt', 'chi': 'b635_probe_out_chi.txt'}
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CEN6 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_6.md'
CEN5 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_5.md'
SIEVE6 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md'
MONO = 'day1/A_Place_to_Stand_v5_18.md'
EF, EF_PIN = 'D:/SIDE-explicit-formula', '8c51431'
MATHLIB_PIN = 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11'   # ### SIDE-explicit-formula lake-manifest.json at 8c51431
EF_TOOLCHAIN = 'leanprover/lean4:v4.34.0-rc1'

# ### the ledger lines the act reads and addresses
B640_ENTRY = 7911
B640_RECORD = 13455
B640_CORRECTION = 13481
PATCH_WO = 13397
KEIPER_WO = 12380            # ### W-ORD-KEIPER-FACE's obligations, named where the proofs stop (b601): lemma (1)'s four and lemma (2)'s three
FERRY_LINES = (11864, 13067, 13167, 13193, 13397, 13455, 13481, 12380)
STATUSES = ('DISCHARGED', 'CITED', 'OPEN')   # ### (R251)(5): exactly one each; none presumed

# ### (R251)(4): THE PHRASE
PHRASE = 'carried openly as open'

# ### (R251)(5): THE OBLIGATIONS, IN THE RULING'S ORDER. Each: (key, component, head, field, file, line, the seat's read). The read names what
# ### would discharge it -- a kernel theorem (named, axiom print read), a literature theorem (reference read, statement matched), or neither --
# ### and the status with its reason in one sentence and the discharger. CANDIDATE: the statement of a new kernel declaration, raised as a
# ### prompt at its component and written nowhere.
KEIPER_FILE, BOUNDS_FILE = 'SIDEExplicitFormula/Keiper.lean', 'SIDEExplicitFormula/KeiperBounds.lean'
WINDOW_FILE, EPSTEIN_FILE, FAMILY_FILE = 'SIDEExplicitFormula/Schema/PlateauRamp.lean', 'SIDEExplicitFormula/Schema/Epstein.lean', 'SIDEExplicitFormula/Schema/Family.lean'
DLMF = {'5.2': 'https://dlmf.nist.gov/5.2', '5.15': 'https://dlmf.nist.gov/5.15', '25.2': 'https://dlmf.nist.gov/25.2', '25.6': 'https://dlmf.nist.gov/25.6'}
OBLIGATIONS = [
    dict(key='K1', comp=3, head='KeiperObligations', field='binomial : BinomialTransform', file=KEIPER_FILE, line=127, defline=117,
         status='OPEN',
         read='true by the kernel`s definitions: with s = 1/(1 - z), logDeriv (phi riemannXi) z = SUM_k xiLogCoeff k z^k (1 - z)^-(k+2), whose z^n '
              'coefficient is SUM_k C(n+1, k+1) xiLogCoeff k (taylorCoeff, Vendored/Bulka/Lc/LiCriterion/Basic.lean :541; riemannXi 1 = 1/2); no '
              'kernel theorem proves it past n = 0 (binomialTransform_zero), no Mathlib lemma at the pin composes Taylor coefficients under '
              'z -> 1/(1 - z), and no reference was read whose statement is the kernel`s at its normalization',
         reason='No compiled proof and no matched citation: the identity holds only at n = 0 in the kernel (binomialTransform_zero).',
         discharger='a kernel theorem binomialTransform_holds : BinomialTransform, by the composition of Taylor series at 0 under z -> 1/(1 - z), '
                    'logDeriv (phi riemannXi) analytic at 0 since riemannXi 1 = 1/2 is not zero',
         candidate='theorem binomialTransform_holds : SIDEExplicitFormula.Keiper.BinomialTransform'),
    dict(key='K2', comp=3, head='KeiperObligations', field='split : LogDerivSplit', file=KEIPER_FILE, line=128, defline=122,
         status='OPEN',
         read='true: riemannXi = 1/2 s riemannZeta1 s GammaR s near 1, each factor nonzero there, so xi`/xi is 1/s + riemannZeta1`/riemannZeta1 + '
              'GammaR`/GammaR and 1/s has the Taylor coefficients (-1)^k at 1; proved at k = 0 only (logDerivSplit_zero); Mathlib holds logDeriv_mul, '
              'no kernel theorem uses it here',
         reason='No compiled proof: the split is proved at its first coefficient only (logDerivSplit_zero).',
         discharger='a kernel theorem logDerivSplit_holds : LogDerivSplit, by Mathlib`s logDeriv_mul on a neighbourhood of 1 where s, riemannZeta1 s '
                    'and GammaR s are nonzero, and the Taylor coefficients of 1/s at 1',
         candidate='theorem logDerivSplit_holds : SIDEExplicitFormula.Keiper.LogDerivSplit'),
    dict(key='K3', comp=3, head='KeiperObligations', field='stieltjesLog : StieltjesLog', file=KEIPER_FILE, line=129, defline=101,
         status='OPEN',
         read='true: poleCoeff are the Taylor coefficients of riemannZeta1 at 1 (riemannZeta1 = 1 + (s - 1) riemannZeta0 near 1, stieltjes n = '
              '(-1)^n riemannZeta0^(n)(1)), and F` = F (F`/F) read coefficient by coefficient is the field; proved at k = 0 only (stieltjesLog_zero)',
         reason='No compiled proof: the power-series logarithm is proved at its first coefficient only (stieltjesLog_zero).',
         discharger='a kernel theorem stieltjesLog_holds : StieltjesLog, by Leibniz`s rule on riemannZeta1 * logDeriv riemannZeta1 = deriv '
                    'riemannZeta1 near 1 and the identification of poleCoeff as riemannZeta1`s Taylor coefficients',
         candidate='theorem stieltjesLog_holds : SIDEExplicitFormula.Keiper.StieltjesLog'),
    dict(key='K4', comp=3, head='KeiperObligations', field='gammaZeta : GammaRZetaValues', file=KEIPER_FILE, line=130, defline=107,
         status='OPEN',
         read='reference read: DLMF 5.15.3, psi^(n)(1/2) = (-1)^(n+1) n! (2^(n+1) - 1) zeta(n + 1); the field is that value carried through '
              'logDeriv GammaR s = -1/2 log pi + 1/2 psi(s/2) to the (k+1)-th Taylor coefficient at 1, (-1)^k (1 - 2^-(k+2)) zeta(k + 2) by the '
              'seat`s computation, so its statement is a consequence of the reference and not the reference`s own; Mathlib at the pin holds '
              'digamma = logDeriv Gamma with digamma_one_half and no derivative of it of higher order',
         reason='Not cited, since the field is the reference`s value carried through a derivation the kernel does not hold, and not compiled.',
         discharger='a kernel theorem gammaRZetaValues_holds : GammaRZetaValues from DLMF 5.15.3 cited as a premise of its own, or from '
                    'psi^(n) as a Hurwitz zeta value, with the chain rule through GammaR s = pi^(-s/2) Gamma(s/2)',
         candidate='theorem gammaRZetaValues_holds : SIDEExplicitFormula.Keiper.GammaRZetaValues'),
    dict(key='B1', comp=3, head='BoundPremises', field='gamma_tight : StieltjesBoundsAt 0', file=BOUNDS_FILE, line=110, defline=98,
         status='OPEN',
         read='reference read: DLMF 5.2.3 gives gamma = 0.57721 56649 01532 86060... to 20 digits, short of the table`s interval at 10^-30; Mathlib '
              'at the pin bounds gamma in (1/2, 2/3) only (stieltjes_zero_coarse, table_refines_coarse); the imaginary part 0 is the kernel`s '
              '(stieltjes_zero)',
         reason='The reference read gives 20 digits against the 30 the interval needs, and no kernel proof bounds gamma that tightly.',
         discharger='a value of gamma to at least 30 digits with its error bound at a named reference, read and matched, or a certified '
                    'interval computation in the kernel (Euler-Maclaurin with an explicit remainder)',
         candidate='theorem gamma_tight_holds : SIDEExplicitFormula.KeiperBounds.StieltjesBoundsAt 0'),
    dict(key='B2', comp=3, head='BoundPremises', field='higher_stieltjes : forall n, 1 <= n -> n <= 11 -> StieltjesBoundsAt n', file=BOUNDS_FILE,
         line=111, defline=98, status='OPEN',
         read='no reference read gives gamma_1..gamma_11 to 10^-30 (DLMF 25.2 read: it defines the Stieltjes constants and prints none of these '
              'values); Mathlib at the pin names no Stieltjes constant beyond gamma',
         reason='No reference read carries the eleven values to the table`s width and no kernel proof bounds them.',
         discharger='a rigorous published computation of gamma_1..gamma_11 with error bounds (for instance Johansson and Blagouchine, Math. Comp. '
                    '2019, not read here) matched entry by entry, or certified interval arithmetic in the kernel',
         candidate='theorem higher_stieltjes_holds : forall n : Nat, 1 <= n -> n <= 11 -> SIDEExplicitFormula.KeiperBounds.StieltjesBoundsAt n'),
    dict(key='B3', comp=3, head='BoundPremises', field='zeta_values : forall j, 2 <= j -> j <= 12 -> ZetaValueBoundsAt j', file=BOUNDS_FILE,
         line=112, defline=101, status='OPEN',
         read='even j: Mathlib`s riemannZeta_two_mul_nat gives zeta(2k) through a Bernoulli number and pi^(2k), but Mathlib`s pi bounds stop at '
              '20 digits (pi_gt_d20, pi_lt_d20); odd j: no bound at the pin, and DLMF 25.6 read prints no value to 30 digits',
         reason='Neither the even values (pi known to 20 digits at the pin) nor the odd ones are bounded to 10^-30 by a compiled proof or a matched citation.',
         discharger='pi to at least 32 digits in the kernel with the Bernoulli values for even j, and for odd j a certified series bound with an '
                    'explicit tail, computed in the kernel, or a published table of zeta(3)..zeta(11) with error bounds read and matched',
         candidate='theorem zeta_values_holds : forall j : Nat, 2 <= j -> j <= 12 -> SIDEExplicitFormula.KeiperBounds.ZetaValueBoundsAt j'),
    dict(key='W1', comp=4, head='WindowObligations', field='conv_step : ConvStep W h', file=WINDOW_FILE, line=182, defline=173,
         status='OPEN',
         read='true for the family (box and normalised box compactly supported and integrable; Fubini); the docstring`s reading (:19-:20) that '
              'Mathlib at the pin holds the convolution theorem for Schwartz functions only is not borne out at de5ce8a9, which holds '
              'Real.fourier_mul_convolution_eq for integrable functions (Mathlib/Analysis/Fourier/Convolution.lean :119), at real frequency, '
              'while ConvStep is at every complex z (paperFT`s Fourier-Laplace form)',
         reason='No compiled proof; Mathlib`s integrable-function convolution theorem at the pin covers real frequencies, not the complex z the field quantifies.',
         discharger='a kernel theorem convStep_holds : ConvStep W h, from Real.fourier_mul_convolution_eq applied to the windows weighted by '
                    'exp(-Im z u) (an exponential weight passes through a convolution), or by Fubini directly',
         candidate='theorem convStep_holds (W h : Real) : SIDEExplicitFormula.Schema.PlateauRamp.ConvStep W h'),
    dict(key='W2', comp=4, head='WindowObligations', field='smooth : Smooth4 W h', file=WINDOW_FILE, line=183, defline=178,
         status='OPEN',
         read='true: for continuous f, (f * nbox h)` = h^-1 (f(x + h/2) - f(x - h/2)) by the fundamental theorem of calculus, so each convolution '
              'raises the order by one, window W h p is C^(p-1) for p >= 1 and C^4 from p = 5 (h <= 0 makes the window 0 past p = 0); Mathlib`s '
              'HasCompactSupport.contDiff_convolution_left carries the smooth factor`s order and the box is not smooth',
         reason='No compiled proof and no Mathlib lemma at the pin gives the order raised by a box convolution.',
         discharger='a kernel theorem smooth4_holds : Smooth4 W h, by induction on p through intervalIntegral.integral_hasDerivAt_right',
         candidate='theorem smooth4_holds (W h : Real) : SIDEExplicitFormula.Schema.PlateauRamp.Smooth4 W h'),
    dict(key='E1', comp=4, head='EpsteinPremises', field='count : exists A0, HCount Z A0', file=EPSTEIN_FILE, line=44, defline=41,
         status='OPEN',
         read='its meaning, by the docstring (:38-:40) and its uses: T3, the local count N(t, t + 1) <= A0 log(|t| + 3) with A0 >= 1 (HCount, '
              'SIDEExplicitFormula/RestBound.lean :44) read off the bench`s zero list; epsteinConfig (:51) hands it to WeilConfig.count, the '
              'count the schema`s summability consumes (Schema/Config.lean :30); witnessed only in the salt checks (SaltCheckEpstein.lean toy_count '
              ':70, empty_count :108); over the abstract Z the field is a hypothesis about Z, Mathlib at the pin holds no Epstein zeta function, '
              'and a finite zero list cannot bound every t',
         reason='The count is a hypothesis about an abstract configuration with no construction of Z_Q`s zeros to prove it of and no matched citation.',
         discharger='a local zero count for Z_Q`s zeros: a kernel theorem once Z_Q`s zero configuration is built, or a Riemann-von Mangoldt '
                    'count for Epstein zeta functions of binary forms at a named reference with its statement matched (none read here)',
         candidate='theorem epstein_count_holds : exists A0 : Real, SIDEExplicitFormula.B321.HCount ZQ A0  -- ZQ, the zero configuration of '
                   'x^2 + xy + 6y^2`s Epstein zeta function, not yet constructed'),
    dict(key='D1', comp=5, head='TrivialSummandPremise', field='(the premise, a Prop over every k)', file=FAMILY_FILE, line=257, defline=257,
         status='OPEN',
         read='refuted as stated by the seat`s computation, not compiled: take k real, nonnegative, continuous, not zero and supported in '
              '(-log 2, log 2); both prime sums vanish (vonMangoldt n is nonzero only for n >= 2, log n >= log 2), the Gamma terms agree '
              '(gammaBracket_chi at the trivial character mod 1 is log(1/pi) + Re psi(1/4 + ir/2) = gammaBracket r, its parity 0), so the premise '
              'asks poleTerm k = 0, while poleTerm k = INT k(u) (e^(-u/2) + e^(u/2)) du > 0',
         reason='As stated the premise is false, so nothing can discharge it, and dedekind_rhs rests on it.',
         discharger='none for the premise; what closes it is its refutation, a kernel theorem not_trivialSummandPremise, after which the '
                    'Dedekind reading with zeta`s pole term carried is dedekind_instance`s, which takes no premise',
         candidate='theorem not_trivialSummandPremise : Not SIDEExplicitFormula.Schema.Family.TrivialSummandPremise'),
    dict(key='D2', comp=5, head='EulerFactorPremise', field='(the premise at a modulus q)', file=FAMILY_FILE, line=265, defline=265,
         status='OPEN',
         read='true at every q whose non-trivial characters are all primitive (q = 3, the kernel`s dedekind_three: the one non-trivial '
              'character mod 3 has conductor 3, both sides reading it at the same level); false at q = 6 by the seat`s computation, not compiled: '
              'the odd character mod 6 is induced from conductor 3, and for k supported in (-log 2, log 2) the prime terms agree while the Gamma '
              'terms differ by log 2 times (1/2 pi) INT paperFT k = log 2 k(0)',
         reason='The premise holds at some moduli and fails at others, and no kernel theorem proves it at any.',
         discharger='kernel theorems eulerFactorPremise_of_primitive (every non-trivial character mod q primitive implies the premise at q, '
                    'q = 3 among them) and not_eulerFactorPremise_six',
         candidate='theorem eulerFactorPremise_of_primitive (q : Nat) [NeZero q] (h : forall chi : DirichletCharacter Complex q, chi != 1 -> '
                   'chi.IsPrimitive) : SIDEExplicitFormula.Schema.Family.EulerFactorPremise q ; theorem not_eulerFactorPremise_six : Not '
                   '(SIDEExplicitFormula.Schema.Family.EulerFactorPremise 6)'),
    dict(key='P1', comp=5, head='W-ORD-DAY1-PATCH-VERSIONS', field='(the seven labels, OPEN_TRAILS :13397)', file='OPEN_TRAILS.md', line=13397,
         defline=13397, status='OPEN',
         read='the seven patch versions resolved below from b639`s file bank and each file`s label at PLACE-papers HEAD; no label is written this '
              'act, the write list naming no day1 file',
         reason='The versions are resolved and not written; the dated lines land at each companion`s next edition.',
         discharger='the work-order`s seven dated lines and labels at each companion`s next edition, one act (:13397)', candidate=''),
]
# ### the seven companions of :13397, b639's file bank (relay data/b639_deposit_files.txt) giving the label and the lines differing from v1.1.2
COMPANIONS = ('Exhaustive_Enumeration.md', 'Which_Structure_Confines.md', 'Spectral_Inertness.md', 'Seven_Mechanism_Classes.md',
              'Third_Identity_Element.md', 'Silence_of_Foundations.md', 'ONE_PAGE_PROOF.md')

# ### (R251)(6): the files read from the clone, by path at its commit
OAI_FILES = ('lean/lean-toolchain', 'lean/lake-manifest.json', 'lean/ComparatorChallenges/README.md',
             'lean/ComparatorChallenges/QuasiRiemannHypothesis.lean', 'lean/ComparatorChallenges/QuasiRiemannHypothesis.json',
             'lean/formalization.yaml', 'lean/docs/003.md')

SEALED = ('b641_worklist.py', 'b641_tests.py', 'b641_record.py', 'b641_checks.py', 'b641_closing.py', 'b641_reg_gate.py', 'b641_regspec.py')
NEEDLE_TOOL, NEEDLE_TEST = 'tools/b640_record.py', 'tools/test_reader_needle_b641.py'
ORDER_TOOL, ORDER_TEST = 'tools/act_root.py', 'tools/test_act_root_order_b641.py'

NEXT_ROUTES = [('b642, the author`s word pending ((R251)(8)): the census at v0.7 with the status column from (5), read by the second reader', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
