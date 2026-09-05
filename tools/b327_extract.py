# -*- coding: utf-8 -*-
"""b327_extract.py -- THE EXTRACT STEP FOR THE FACES LEDGER. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### A cross-reference ledger of every face or equivalence
### the corpus has met, with every row's claim QUOTED from the file that emits it. ### The cheapest
### way to write such a ledger is from memory of the record, and b283's law is the answer: ### **a
### quotation is located at its emitting file and its line BEFORE it is written anywhere else**, and
### the gate suite pulls its needles from THIS file.

### ### **THE EMITTERS.** ### The deposited monograph at its VERIFIED copy (`outputs/DEPOSITED-v1.1.2/`,
### the copy `REGISTRY.md` d1-1 records as md5-matched to Zenodo) for the five faces and the refusal
### to compile the equivalences; the deposited confinement keystone likewise; two INTERNAL keystones
### (the residue keystone for the wall, the balance keystone for the Li margin and the channel split);
### the corpus's own bench for the split's definition; the arc keystone for the two-radius family;
### and the banks of the acts that own each measured result -- b309, b310, b311 (the fixed-point
### silence), b320, b321 (the Sonin margin and the finite-instance identity), b324 (the wall and the
### margin decided), b325 and b326 (the negative control), b288 (the eigenvalue-one juxtaposition).
### ### **THE PENTAGON MODULE AS BANKED** (`data/read_pentagon.txt`) for the citation the corpus names.

### ### **WHAT IT DOES NOT DO.** ### It does not decide, grade or relate. ### A fragment found is a
### fragment found; whether it is the right fragment is this seat's reading, declared as such.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEPOSIT = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b327_extract_notes.txt')
MONO = os.path.join(DEPOSIT, 'A_Place_to_Stand.md')
CONF = os.path.join(DEPOSIT, 'Which_Structure_Confines.md')
RESIDUE = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
BALANCE = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
BENCH = os.path.join(PP, 'internal', 'bench', 'li_bench.py')
TWORAD = os.path.join(PP, 'phase2', 'method', 'THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')


def d(n):
    return os.path.join(D, n)


WANTED = [
    # ### ---- THE DEPOSIT: the five faces, the register sentence, the refusal, the finite-range certificate
    ('R1 the first face, universality', MONO, 'First: the *universality hypothesis* carried by the Universal Silence Theorem'),
    ('R2 the second face, conservation', MONO, 'Second: the proposition named `ConservationHypothesis`'),
    ('R3 the third face, totality', MONO, 'Third: the totality of the realization of mechanisms through places'),
    ('R4 the fourth face, balance to positivity', MONO, 'Fourth: the distance between *balance* and *positivity* at the multiplicative place'),
    ('R4 ### its sharpest form, the inter-channel inequality', MONO, 'the premise is the inequality λ_Z(n) ≥ −λ_A(n) between two independently computable channels'),
    ('R5 the fifth face, the spectral-realization distance', MONO, 'Fifth: the *spectral-realization distance*'),
    ('R5 ### no positive pairing is known', MONO, 'no positive pairing is known'),
    ('THE REGISTER SENTENCE', MONO, 'A reader who discharges any one of them discharges all five'),
    ('THE REFUSAL TO COMPILE THE EQUIVALENCES', MONO, 'deliberately **not** compiling the cross-register equivalences'),
    ('THE THREE CLASSICAL FACES OF h2', MONO, 'positivity of the Weil functional, λ_n ≥ 0, or the number-field shadow'),
    ('THE FINITE-RANGE CERTIFICATE', MONO, 'certifies λ_n ≥ 0 for n up to Voros\'s detection threshold'),
    ('### its scope sentence', MONO, 'a certificate reaching exactly to where discrimination would begin, and no further'),
    ('### its premise, named and open', MONO, 'the decomposition conjunct (Guinand–Weil) and the tail premise remain named and open'),
    ('THE COMPILED BOUNDARY MARKER', MONO, 'certifiedInput_not_zeroRealizing` (v0.9.0) proves'),
    ('THE PINS OF THE COMPILED LAYER', MONO, 'SIDE-lv-conservation v0.7.0 = `2d86182`'),
    ('THE CONFINEMENT KEYSTONE\'S FINDING', CONF, 'it does not confine zeros to it'),
    # ### ---- INTERNAL KEYSTONES
    ('THE WALL, at the residue keystone', RESIDUE, 'The space is the wall'),
    ('### the located circularity', RESIDUE, 'the operator is *free given the positive space*'),
    ('### the realization-candidate map grades the arc\'s source', RESIDUE, 'Connes–Consani (reduces RH to a Weil positivity left open)'),
    ('### the positive ledger with RH false', RESIDUE, 'positive ledger but RH false'),
    ('THE LI MARGIN, at the balance keystone', BALANCE, 'M(n) := λ_Z(n) + λ_A(n) = λ_n is the margin'),
    ('### positive to n = 300 at the bench', BALANCE, 'nevertheless stays positive throughout 1 ≤ n ≤ 300'),
    ('### lambda_Z negative in two ranges', BALANCE, 'λ_Z(n) < 0 for n ∈ [156, 186] ∪ [247, 287]'),
    ('### THE SPLIT, IN THE KEYSTONE\'S OWN WORDS', BALANCE, 'f_A(s) = log s + logΓ(s/2) − (s/2)log π and f_Z(s) = log((s−1)ζ(s))'),
    ('### the split is not over places', BALANCE, 'The programme\'s split is not S_∞/S_NA over places'),
    ('### the joint as bookkeeping', BALANCE, 'is an exact restatement of Li\'s criterion under the above split'),
    ('### the Fano incidence dark to second-order statistics', BALANCE, 'the Fano incidence is provably dark to all second-order statistics'),
    ('THE SPLIT, at the bench that computes it', BENCH, 'f_A(s) = log s + logGamma(s/2) - (s/2) log pi'),
    ('### and the Li map it applies', BENCH, 'lambda_n = n * sum_{j=1..n} C(n-1, j-1) * eta_j'),
    ('### and the code that is the archimedean channel', BENCH, 'return mp.log(s) + mp.loggamma(s / 2) - (s / 2) * mp.log(mp.pi)'),
    ('THE TWO-RADIUS FAMILY, at the arc keystone', TWORAD, 'THE FAMILY IS CONSTRUCTED'),
    ('### its dimension', TWORAD, 'DIMENSION `(p^n - p^a)(p^n - p^b)`'),
    ('### the family is not a route', TWORAD, 'A family existing is not a route existing'),
    ('### the annihilation criterion', TWORAD, 'IF AND ONLY IF'),
    ('THE PENTAGON DOORS, at PATHS', PATHS, 'Never the cross-register equivalences'),
    # ### ---- THE BANKED PENTAGON MODULE: the citation the corpus names
    ('THE CITATION THE CORPUS NAMES FOR LI\'S CRITERION', d('read_pentagon.txt'), 'Bombieri–Lagarias 1999, via the Guinand–Weil explicit formula'),
    ('### R4\'s decomposition edge, combinatorial only', d('read_pentagon.txt'), 'COMBINATORIAL stream-level only'),
    # ### ---- THE ACTS THAT OWN EACH MEASURED RESULT
    ('THE FIXED-POINT MECHANISM, b309', d('b309_the_scaling_trace.txt'), 'THE SCALING MAP HAS NO FIXED POINT OFF THE BALL'),
    ('### and the only fixed point it has', d('b309_the_scaling_trace.txt'), 'IS THE ONE PLACE THE OBJECT IS REQUIRED TO VANISH'),
    ('THE SILENCE, b310', d('b310_the_smear_collapses.txt'), 'RETURNS ONE TERM AND THERE IS NO'),
    ('### the test function read at one point', d('b310_the_smear_collapses.txt'), 'THE TEST FUNCTION READ AT ONE POINT, TIMES A DIMENSION'),
    ('### it does not type at infinity, b311', d('b311_the_identitys_neighbourhood.txt'), 'THE QUESTION THE FINITE'),
    ('### the source\'s positivity has non-function content only at the identity, b311', d('b311_the_identitys_neighbourhood.txt'), 'WHOSE ONLY NON-FUNCTION CONTENT IS AT THE'),
    ('THE SONIN MARGIN, b320 -- Theorem 1 holds', d('b320_the_lawful_function.txt'), 'AND THE CONTROL HOLDS'),
    ('### its three margins', d('b320_the_lawful_function.txt'), 'margin `+0.271444634`'),
    ('### sign certified, size not', d('b320_the_lawful_function.txt'), "THE MARGIN'S SIGN IS CERTIFIED AT EVERY FRAME; ITS SIZE IS NOT CERTIFIED AT ANY"),
    ('### no theorem proved', d('b320_the_lawful_function.txt'), 'NO THEOREM IS PROVED HERE'),
    ('THE MARGIN IS MINUS THE REMAINDER INTEGRAL, b321', d('b321_the_window_opened.txt'), "makes b320's margin exactly minus the remainder integral"),
    ('THE FINITE-INSTANCE IDENTITY, b321 -- the explicit formula closes', d('b321_the_window_opened.txt'), 'THE EXPLICIT-FORMULA CONTROL HOLDS -- AT ALL THIRTEEN CELLS'),
    ('### its residuals', d('b321_the_window_opened.txt'), '`2.2e-09` to `3.6e-05`'),
    ('### the balance collapses to minus the zero side', d('b321_the_window_opened.txt'), 'SUM_v W_v(f) = - Z'),
    ('### the count is forced', d('b321_the_window_opened.txt'), 'THAT COUNT IS FORCED BY THE SHAPE OF THE COMPUTATION'),
    ('THE WALL DECIDED DIFFERENT, b324', d('b324_the_keystones_reread.txt'), 'VERDICT: ### DIFFERENT. ### SEVEN OF SEVEN.'),
    ('THE MARGIN UNDECIDED, b324', d('b324_the_keystones_reread.txt'), 'THE MARGIN: ### UNDECIDED'),
    ('### equivalence of obligations is not equivalence of margins', d('b324_the_keystones_reread.txt'), 'EQUIVALENCE OF THE OBLIGATIONS IS NOT'),
    ('### the bridging statement typed', d('b324_the_keystones_reread.txt'), 'a formula carrying the archimedean margin'),
    ('### the zeros are in one margin and not the other', d('b324_the_keystones_reread.txt'), 'THEY ARE NOT IN THE ARC\'S'),
    ('### the arc\'s margin figures', d('b324_the_keystones_reread.txt'), 'Theorem 4.7 to minus the remainder integral'),
    ('THE NEGATIVE CONTROL AT b326\'S RESULT', d('b326_the_reach.txt'), 'TWENTY-SIX CELLS TO `a = 400` : DOES NOT SEE IT'),
    ('### the family finding', d('b326_the_reach.txt'), 'A FAMILY THAT SEES THE FAILURE NEEDS A SIGN'),
    ('### the seed priced, not built', d('b326_the_reach.txt'), 'A seed that changes sign there is'),
    ('### the entailment at scope', d('b326_the_reach.txt'), 'IT IS A TEST THIS FAMILY CANNOT FAIL'),
    ('### the theorem does not transfer', d('b326_the_reach.txt'), "IT DOES NOT SAY THE SOURCE'S INEQUALITY OR THE OBJECT'S DECOMPOSITION TRANSFER"),
    ('### the ledger is the Li one, b325', d('b325_the_negative_control.txt'), 'POSITIVITY IS OF THE COEFFICIENT SEQUENCE, NOT OF THE ZEROS'),
    ('THE EIGENVALUE-ONE JUXTAPOSITION, b288', d('b288_the_family_and_the_complement.txt'), "THE INSTRUMENTS' WEIGHTS DIVERGE PRECISELY AS ONE APPROACHES THE OBJECT'S SPACE"),
    ('### routed, not computed', d('b288_the_family_and_the_complement.txt'), 'A JUXTAPOSITION, ROUTED, NOT COMPUTED'),
    ('### the weight, at the corpus', d('b288_the_family_and_the_complement.txt'), 'the weight is `lam_n^2/(1-lam_n^2)`'),
    ('THE EIGENVALUE-ONE CUT, b323 fold', d('b323_the_fold.txt'), 'the eigenvalue-one cut'),
    # ### ---- THE FRAGMENTS THE LEDGER'S ROWS AND PAIRS QUOTE, ADDED SO THAT EVERY GATE NEEDLE IS IN THIS FILE
    ('R1 ### the hypothesis is load-bearing', MONO, 'the hypothesis is load-bearing; removing it from the proof of `silence_universal` leaves an unsolved goal'),
    ('R1 ### the kernel pin, at the banked module', d('read_pentagon.txt'), 'SIDE-kernel v1.3 = 0bc21c0'),
    ('R2 ### the premise itself', MONO, 'This proposition is the premise itself, stated at the multiplicative place'),
    ('R2 ### the certificate does not discharge it', MONO, 'shapes and motivates it, but does not discharge it'),
    ('R2 ### the compiled conditional', d('read_pentagon.txt'), 'ConservationBridge.riemann_hypothesis'),
    ('R3 ### the totality premise', MONO, 'what remains open is not the theorem but this totality premise it consumes'),
    ('R3 ### not compiled', d('read_pentagon.txt'), 'Register3_totalityThroughPlaces'),
    ('R4 ### the finite-range pin', MONO, 'v0.8.0 = `6efa9e5`'),
    ('R4 ### the sharpest form', MONO, 'On the exact channel decomposition of the Li coefficients, this face takes its sharpest form'),
    ('R5 ### disclaimed', MONO, 'which this programme explicitly disclaims asserting'),
    ('F1 ### the fourth at most, b324', d('b324_the_keystones_reread.txt'), 'the FOURTH at most'),
    ('F1 ### realizes no spectrum, b324', d('b324_the_keystones_reread.txt'), 'it computes an explicit-formula balance and realizes no spectrum'),
    ('F1 ### the count forced, b321', d('b321_the_window_opened.txt'), 'IS FORCED BY THE SHAPE OF THE COMPUTATION'),
    ('F1 ### zeta closes, b326', d('b326_the_reach.txt'), 'ZETA: CLOSES AT TWENTY-SIX OF TWENTY-SIX CELLS'),
    ('F1 ### the Epstein function closes, b326', d('b326_the_reach.txt'), 'CLOSES AT TWENTY-ONE OF TWENTY-ONE CELLS'),
    ('F1 ### the formula closes for both, b326', d('b326_the_reach.txt'), 'THE EXPLICIT FORMULA CLOSES FOR BOTH'),
    ('F2 ### the remainder integral measured, b321', d('b321_the_window_opened.txt'), '0.158889558'),
    ('F2 ### the instrument inside the first face, b324', d('b324_the_keystones_reread.txt'), 'THE ARC BUILT AN INSTRUMENT INSIDE THE FIRST OF THREE NAMED FACES'),
    ('F2 ### the remainder is the margin, b323', d('b323_the_fold.txt'), 'THAT REMAINDER IS THE MARGIN b320 MEASURED'),
    ('F2 ### the square is not a zero channel, b324', d('b324_the_keystones_reread.txt'), 'The square is not a zero channel'),
    ('F3 ### the split, the balance keystone', BALANCE, 'f_A(s) = log s + logΓ(s/2) − (s/2)log π'),
    ('F4 ### the fifth register, b324', d('b324_the_keystones_reread.txt'), 'the FIFTH, the spectral-realization distance'),
    ('F5 ### does not type at infinity, the fold', FINDINGS, 'does not type at the archimedean place'),
    ('F5 ### evaluated on the object\'s space, the fold', FINDINGS, 'evaluated on the object'),
    ('F6 ### supplied by source', TWORAD, '(SUPPLIED BY SOURCE)'),
    ('F6 ### the standing boundary', TWORAD, 'NO FINITE-SIDE STRUCTURAL FACT TYPES AT `infinity`'),
    ('F6 ### vectors outside the object, the adelic fold', FINDINGS, 'compute with vectors that lie outside the object'),
    ('F7 ### the entailment, b326', d('b326_the_reach.txt'), 'IS A TEST THIS FAMILY CANNOT FAIL'),
    ('R3-F1 ### the clause lives at totality, b323', d('b323_the_fold.txt'), 'THE CLAUSE LIVES AT TOTALITY, AND THIS ARC NAMES THE MECHANISM BY WHICH NO FINITE'),
]


def main():
    lines = []

    def rec(s=''):
        lines.append(s)

    rec('=' * 100)
    rec('b327_extract.py -- THE FACES LEDGER. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
    rec('=' * 100)
    rec('  ### **THE DEPOSITED TEXTS ARE READ AT THE VERIFIED COPY. ### THE PROJECT MIRROR IS NOT OPENED.**')
    rec('')
    missing, paths_missing = 0, 0
    for lbl, path, frag in WANTED:
        rec('### ==== %s' % lbl)
        if not os.path.exists(path):
            paths_missing += 1
            rec('###      %s | ### **FILE NOT PRESENT**' % path)
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        hits = [(i + 1, ln) for i, ln in enumerate(body) if frag in ln]
        short = path.replace(PP, '<papers>').replace(ROOT, '<relay>').replace('\\', '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('  ### **A FRAGMENT FOUND IS A FRAGMENT FOUND. ### WHETHER IT IS THE RIGHT ONE IS THIS SEAT\'S READING.**')
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    print('\n'.join(lines[-4:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
