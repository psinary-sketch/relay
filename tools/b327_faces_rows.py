# -*- coding: utf-8 -*-
"""b327_faces_rows.py -- THE SEED ROWS AND THE PAIR TABLE OF THE FACES LEDGER. ### **DATA, NOT A WRITER.**

### ### **EVERY QUOTED CLAIM CARRIES THE FILE THAT EMITS IT AND A FRAGMENT THE WRITER VERIFIES BEFORE
### THE ROW IS WRITTEN.** ### A row whose fragment is not in its file is refused by `b327_faces_row.py`.
### ### **GRADES ARE THE OWNING ACTS'.** ### `PROVED` names a kernel terminal at a pin; `MEASURED` names
### the act and the number; `IMPORTED` names the pinned source; `NAMED-ONLY` is the corpus's own naming
### and nothing more. ### **NO ROW'S GRADE IS ANOTHER ROW'S**, and the pair table below states relations
### the record already states, types bridges it owes, or says NONE -- one of the three for every pair.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
MONO = os.path.join(DEP, 'A_Place_to_Stand.md')
CONF = os.path.join(DEP, 'Which_Structure_Confines.md')
RESIDUE = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
BALANCE = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
BENCH = os.path.join(PP, 'internal', 'bench', 'li_bench.py')
TWORAD = os.path.join(PP, 'phase2', 'method', 'THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
PENT = os.path.join(D, 'read_pentagon.txt')
SRC = os.path.join(D, 'b327_source_text.txt')


def bank(n):
    return os.path.join(D, n)


COLUMNS = ['id', 'face or equivalence', 'register',
           'source, with the emitting file (deposited / internal / imported)',
           'what the corpus holds -- PROVED, MEASURED, IMPORTED, or NAMED-ONLY, each graded, the claim quoted from the emitting file',
           'rows touched (SIDE-global-section CORRESPONDENCE.md)',
           'bridges owed, typed']

# ### each row: id, cells[1:], quotes = [(path, fragment, flat)]
ROWS = [
    dict(id='R1',
         cells=[
             'R1 -- the universality hypothesis, carried by the Universal Silence Theorem',
             'the first: kernel-theoretic',
             'DEPOSITED -- `outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md` section 27.3, line 1779; compiled as STRUCTURE only, `Register1_universalityHypothesis` (SIDE-lv-conservation v0.7.0 = `2d86182`, banked at relay `data/read_pentagon.txt`)',
             'NAMED -- the deposit: *"First: the universality hypothesis carried by the Universal Silence Theorem. Chapter 14 states it plainly -- the hypothesis is load-bearing; removing it from the proof of `silence_universal` leaves an unsolved goal"*. PROVED, the surround only: `silence_universal` (SIDE-kernel v1.3 = `0bc21c0`) is the theorem UNDER the hypothesis; the hypothesis is the face and is not proved. Grade as the deposit leaves it: one of five registers of the one open premise.',
             'none in CORRESPONDENCE.md; the pentagon\'s rows are SIDE-lv-conservation\'s, filed at the PATHS keystone',
             'none typed by this act. To R2-R5: the register sentence, deliberately NOT compiled (the head of this ledger).',
         ],
         quotes=[(MONO, 'First: the *universality hypothesis* carried by the Universal Silence Theorem', False),
                 (MONO, 'the hypothesis is load-bearing; removing it from the proof of `silence_universal` leaves an unsolved goal', False),
                 (PENT, 'SIDE-kernel v1.3 = 0bc21c0', False)]),
    dict(id='R2',
         cells=[
             'R2 -- `ConservationHypothesis`: every xi-zero forces the Euler balance equation at some prime',
             'the second: formal-interface',
             'DEPOSITED -- section 27.3, line 1779; compiled as STRUCTURE only, `Register2_conservationHypothesis` restating `ConservationBridge.ConservationHypothesis` verbatim from SIDE-kernel v1.3 = `0bc21c0` (relay `data/read_pentagon.txt`)',
             'NAMED -- the deposit: *"This proposition is the premise itself, stated at the multiplicative place"*, with the conservation CERTIFICATE (Chapter 13) that *"shapes and motivates it, but does not discharge it"*. PROVED, one direction only: the compiled conditional `ConservationBridge.riemann_hypothesis` (R2 implies RH, SIDE-kernel v1.3) -- the pentagon\'s DERIVES edge; the converse is not compiled and the face stays open.',
             'none in CORRESPONDENCE.md',
             'none typed by this act. R2 implies RH is compiled (DERIVES); nothing carries R2 to or from R1, R3, R4, R5 beyond the uncompiled register sentence.',
         ],
         quotes=[(MONO, 'Second: the proposition named `ConservationHypothesis`', False),
                 (MONO, 'This proposition is the premise itself, stated at the multiplicative place', False),
                 (MONO, 'shapes and motivates it, but does not discharge it', False),
                 (PENT, 'ConservationBridge.riemann_hypothesis', False)]),
    dict(id='R3',
         cells=[
             'R3 -- the totality of the realization of mechanisms through places',
             'the third: category-shaped',
             'DEPOSITED -- section 27.3, line 1779; NOT COMPILED (the pentagon module lists R3 under NOT-COMPILED, its native shadow the T3 pinned sorry, relay `data/read_pentagon.txt`)',
             'NAMED-ONLY -- the deposit: *"Third: the totality of the realization of mechanisms through places -- the sentence in step (8) of the assembly, \'if an off-line zero existed, some mechanism would produce it,\' together with the claim that place-level exclusion reflects to mechanism level"*, and *"what remains open is not the theorem but this totality premise it consumes"*. Nothing more is held.',
             'none in CORRESPONDENCE.md',
             'none typed by this act. The archimedean instrument arc\'s statement that the clause lives at totality is a STATED contact (pair R3-F1), not a bridge.',
         ],
         quotes=[(MONO, 'Third: the totality of the realization of mechanisms through places', False),
                 (MONO, 'what remains open is not the theorem but this totality premise it consumes', False),
                 (PENT, 'Register3_totalityThroughPlaces', False)]),
    dict(id='R4',
         cells=[
             'R4 -- the distance between balance and positivity at the multiplicative place',
             'the fourth: analytic',
             'DEPOSITED -- section 27.3, lines 1779 and 1796; compiled as STRUCTURE only, `Register4_positivity` (SIDE-lv-conservation v0.7.0 = `2d86182`); the finite-range certificate `partialPositivity_finiteRange` (v0.8.0 = `6efa9e5`); the channel decomposition `lam_add` (SIDE-li-map `73cee42`)',
             'NAMED -- the face: *"the premise is the inequality λ_Z(n) ≥ −λ_A(n) between two independently computable channels"*, for every n. PROVED, the finite range: *"`partialPositivity_finiteRange` (v0.8.0) certifies λ_n ≥ 0 for n up to Voros\'s detection threshold N₀(T) ≈ 2T², with the on-line term\'s nonnegativity proved -- a certificate reaching exactly to where discrimination would begin, and no further"*, its premise *"the decomposition conjunct (Guinand–Weil) and the tail premise remain named and open"*. PROVED, the split\'s linearity: `lam_add`, *"COMBINATORIAL stream-level only"*. MEASURED: see F3.',
             'none in CORRESPONDENCE.md; the balance keystone\'s bench is INTERNAL',
             'OWED -- `W-ORD-LI-WEIL-BRIDGE` (pair F2-F3): a formula carrying the arc\'s archimedean margin to the Li margin, or a proof none exists. To the Li margin (F3): STATED, the deposit\'s own sentence. To the Sonin margin (F2): STATED, the arc built its instrument inside this face (b324).',
         ],
         quotes=[(MONO, 'the premise is the inequality λ_Z(n) ≥ −λ_A(n) between two independently computable channels', False),
                 (MONO, 'a certificate reaching exactly to where discrimination would begin, and no further', False),
                 (MONO, 'the decomposition conjunct (Guinand–Weil) and the tail premise remain named and open', False),
                 (MONO, 'v0.8.0 = `6efa9e5`', False),
                 (PENT, 'COMBINATORIAL stream-level only', False)]),
    dict(id='R5',
         cells=[
             'R5 -- the spectral-realization distance: input-stage coupling certified, output-stage realization disclaimed',
             'the fifth: spectral-geometric',
             'DEPOSITED -- section 27.3, lines 1779 and 1796; compiled as STRUCTURE only, `Register5_input` / `Register5_output_HilbertPolya` (v0.7.0 = `2d86182`); the boundary marker `certifiedInput_not_zeroRealizing` (v0.9.0 = `e3d08b6`)',
             'NAMED, and DISCLAIMED as a claim -- the deposit: *"the output-stage claim, that the zeros themselves are the spectrum of a self-adjoint operator with a positive pairing, is the Hilbert–Pólya realization, which this programme explicitly disclaims asserting"*; over Q *"no positive pairing is known"*. PROVED, the input and the distance: `C5_input_at_Phi` (h1) and *"`certifiedInput_not_zeroRealizing` (v0.9.0) proves that the certified {n²} heat-trace input spectrum is *not* a zero-realizing spectrum"* -- a negative that names the distance without shortening it.',
             'none in CORRESPONDENCE.md',
             'none typed by this act. To the wall (F4): STATED -- the same distance under its internal name.',
         ],
         quotes=[(MONO, 'Fifth: the *spectral-realization distance*', False),
                 (MONO, 'which this programme explicitly disclaims asserting', False),
                 (MONO, 'no positive pairing is known', False),
                 (MONO, 'certifiedInput_not_zeroRealizing` (v0.9.0) proves', False)]),
    dict(id='F1',
         cells=[
             'F1 -- the finite-instance identity: the explicit formula Z = P − PR + A realized on lawful objects (the source\'s (148) in the corpus\'s chain)',
             'the fourth\'s instrument, at the archimedean place of the Weil-positivity face; it *"computes an explicit-formula balance and realizes no spectrum"* (b324)',
             'INTERNAL -- relay `data/b321_the_window_opened.txt`, `data/b326_the_reach.txt`; the atlas `tools/e16/carto_atlas.py`; folded in `FINDINGS.md` (THE ARCHIMEDEAN INSTRUMENT ARC)',
             'MEASURED, as a CONTROL -- b321: *"THE EXPLICIT-FORMULA CONTROL HOLDS -- AT ALL THIRTEEN CELLS"*, residuals *"`2.2e-09` to `3.6e-05`"* against the atlas\'s own bar; b326: closes for zeta at 26 of 26 cells to a = 400 and for the Epstein function at 21 of 21 below its library\'s ceiling. And the sign finding, b321: the balance collapses to *"SUM_v W_v(f) = - Z"*, so its non-positive count *"IS FORCED BY THE SHAPE OF THE COMPUTATION"*. A control that holds certifies the instrument, not the object; no theorem is proved.',
             '154, 155 (b321); 164, 165 (b326)',
             'OWED -- `W-ORD-LI-FAMILY-CONTROL` (pair L1-F1): the formula closed on the Li family through the corpus\'s own channels, priced and not run. OWED -- `W-ORD-DISCRIMINATING-FAMILY` (pair F1-F7).',
         ],
         quotes=[(bank('b324_the_keystones_reread.txt'), 'it computes an explicit-formula balance and realizes no spectrum', False),
                 (bank('b321_the_window_opened.txt'), 'THE EXPLICIT-FORMULA CONTROL HOLDS -- AT ALL THIRTEEN CELLS', False),
                 (bank('b321_the_window_opened.txt'), '`2.2e-09` to `3.6e-05`', False),
                 (bank('b321_the_window_opened.txt'), 'SUM_v W_v(f) = - Z', False),
                 (bank('b321_the_window_opened.txt'), 'IS FORCED BY THE SHAPE OF THE COMPUTATION', False),
                 (bank('b326_the_reach.txt'), 'ZETA: CLOSES AT TWENTY-SIX OF TWENTY-SIX CELLS', False),
                 (bank('b326_the_reach.txt'), 'CLOSES AT TWENTY-ONE OF TWENTY-ONE CELLS', False)]),
    dict(id='F2',
         cells=[
             'F2 -- the Sonin margin: W_∞(f) − Tr(θ(g) S θ(g)*) on f = g conv g^#, supp g in [2^−1/2, 2^1/2], two vanishing conditions (the source\'s Theorem 1 class)',
             'the fourth\'s archimedean instrument -- *"the FOURTH at most"* (b324, constituent (7))',
             'INTERNAL -- relay `data/b320_the_lawful_function.txt`, `data/b321_the_window_opened.txt`, `data/b324_the_keystones_reread.txt`. IMPORTED -- Connes–Consani, arXiv:2006.13771v1 (pinned sha256 `b8e0b54a…`, b304/b305), Theorem 1 and Theorem 4.7 at the import bar',
             'MEASURED -- b320: *"AND THE CONTROL HOLDS"* at a = 1.30, 1.35, 1.41, margins *"`+0.271444634`"*, `+0.285510313`, `+0.309777648`, 27 of 27 frames; *"THE MARGIN\'S SIGN IS CERTIFIED AT EVERY FRAME; ITS SIZE IS NOT CERTIFIED AT ANY"*. b321: Theorem 4.7 *"makes b320\'s margin exactly minus the remainder integral"*, measured `0.158889558`, `0.186481766`, `0.221284108`. IMPORTED -- the inequality (Theorem 1) and the equality (Theorem 4.7) are the source\'s; b320: *"NO THEOREM IS PROVED HERE"*.',
             '152, 153 (b320); 154, 155 (b321); 160, 161 (b324)',
             'OWED -- `W-ORD-LI-WEIL-BRIDGE` (pair F2-F3), typed by b324 and read at L1. To the wall (F4): STATED, DIFFERENT at seven of seven constituents (b324). To the negative control (F7): STATED, the inequality does not transfer (Gamma(s) against Gamma(s/2), b326).',
         ],
         quotes=[(bank('b324_the_keystones_reread.txt'), 'the FOURTH at most', False),
                 (bank('b320_the_lawful_function.txt'), 'AND THE CONTROL HOLDS', False),
                 (bank('b320_the_lawful_function.txt'), 'margin `+0.271444634`', False),
                 (bank('b320_the_lawful_function.txt'), "THE MARGIN'S SIGN IS CERTIFIED AT EVERY FRAME; ITS SIZE IS NOT CERTIFIED AT ANY", False),
                 (bank('b320_the_lawful_function.txt'), 'NO THEOREM IS PROVED HERE', False),
                 (bank('b321_the_window_opened.txt'), "makes b320's margin exactly minus the remainder integral", False),
                 (bank('b321_the_window_opened.txt'), '0.158889558', False)]),
    dict(id='F3',
         cells=[
             'F3 -- the Li margin: M(n) := λ_Z(n) + λ_A(n) = λ_n, the margin in λ_Z(n) ≥ −λ_A(n)',
             'the fourth, at the bench',
             'INTERNAL -- `phase1.5/spectral/BALANCE_AND_POSITIVITY.md` lines 297, 410, 427; `internal/bench/li_bench.py`. DEPOSITED -- section 27.3 (the inequality; the finite-range certificate, see R4)',
             'MEASURED -- the keystone: *"M(n) := λ_Z(n) + λ_A(n) = λ_n is the margin"*; the bench to n = 300: the margin *"nevertheless stays positive throughout 1 ≤ n ≤ 300"* (minimum at n = 1, λ₁ = 0.0230957089661) while *"λ_Z(n) < 0 for n ∈ [156, 186] ∪ [247, 287]"*. The split, in the keystone\'s own words: *"f_A(s) = log s + logΓ(s/2) − (s/2)log π and f_Z(s) = log((s−1)ζ(s))"*, and *"The programme\'s split is not S_∞/S_NA over places"*. PROVED: the finite-range certificate and `lam_add` (see R4). NAMED: the all-n inequality, which is the face R4 itself.',
             '160, 161 (b324)',
             'OWED -- `W-ORD-LI-WEIL-BRIDGE` (pair F2-F3). To R4: STATED. To the negative control (F7): STATED, the Epstein ledger is *"positive ledger but RH false"* (the residue keystone) and the positivity is of the coefficient sequence (b325).',
         ],
         quotes=[(BALANCE, 'M(n) := λ_Z(n) + λ_A(n) = λ_n is the margin', False),
                 (BALANCE, 'nevertheless stays positive throughout 1 ≤ n ≤ 300', False),
                 (BALANCE, 'λ_Z(n) < 0 for n ∈ [156, 186] ∪ [247, 287]', False),
                 (BALANCE, 'f_A(s) = log s + logΓ(s/2) − (s/2)log π and f_Z(s) = log((s−1)ζ(s))', False),
                 (BALANCE, "The programme's split is not S_∞/S_NA over places", False),
                 (RESIDUE, 'positive ledger but RH false', False)]),
    dict(id='F4',
         cells=[
             'F4 -- the spectral-realization wall: *"the positive space on the zeros"*; *"The space is the wall."*',
             'the fifth (b324: *"the FIFTH, the spectral-realization distance"*)',
             'INTERNAL -- `phase1.5/proofs/THE_RESIDUE_OF_RH.md` lines 65, 67, 90 (ms v5.13); DEPOSITED, the nearest statement only -- section 27.3, *"no positive pairing is known"*. b324 measured that *"THE SPACE IS THE WALL"* appears zero times in the deposited monograph.',
             'NAMED-ONLY, at the wall\'s own name (internal) -- *"The two cross at one object, **the positive space on the zeros**: positivity has no zeros, the operator has no space, and the space is exactly what neither supplies"*; the located circularity: *"the operator is *free given the positive space*"*. MEASURED at definitions, b324: the arc\'s constructed space against the wall\'s space, *"VERDICT: ### DIFFERENT. ### SEVEN OF SEVEN."*; and the keystone\'s own candidate map grades the arc\'s source *"Connes–Consani (reduces RH to a Weil positivity left open)"*. The realization itself is disclaimed (R5).',
             '160 (b324)',
             'none typed by this act. To R5: STATED, the same distance. To the Sonin margin (F2): STATED, DIFFERENT (b324) -- a non-identity, not a bridge. To the Li margin (F3): STATED at the level of the obligation only, *"EQUIVALENCE OF THE OBLIGATIONS IS NOT"* equivalence of the margins (b324).',
         ],
         quotes=[(RESIDUE, 'The space is the wall', False),
                 (RESIDUE, 'the operator is *free given the positive space*', False),
                 (RESIDUE, 'Connes–Consani (reduces RH to a Weil positivity left open)', False),
                 (MONO, 'no positive pairing is known', False),
                 (bank('b324_the_keystones_reread.txt'), 'VERDICT: ### DIFFERENT. ### SEVEN OF SEVEN.', False),
                 (bank('b324_the_keystones_reread.txt'), 'the FIFTH, the spectral-realization distance', False),
                 (bank('b324_the_keystones_reread.txt'), 'EQUIVALENCE OF THE OBLIGATIONS IS NOT', False)]),
    dict(id='F5',
         cells=[
             'F5 -- the fixed-point silence: at a finite place the source\'s construction on the object\'s space returns the test function at the identity times a dimension and carries no arithmetic; the scaling map\'s only fixed point is where the object vanishes',
             'the third\'s instrument at a finite place -- and the mechanism *"does not type at the archimedean place"* (the fold of b307–b313)',
             'INTERNAL -- relay `data/b309_the_scaling_trace.txt`, `data/b310_the_smear_collapses.txt`, `data/b311_the_identitys_neighbourhood.txt`; folded in `FINDINGS.md` (THE INSTRUMENT ARC)',
             'MEASURED and DERIVED (the acts\' own grades: COMPUTED; COMPUTED AND DERIVED; DECIDED AT DEFINITIONS) -- b309: *"THE SCALING MAP HAS NO FIXED POINT OFF THE BALL"* and the only one it has *"IS THE ONE PLACE THE OBJECT IS REQUIRED TO VANISH"* (exactly zero at 44 cell/power pairs, three zero-axiom terminals); b310: `T(w) = w_0 (p^n − 1)^2`, *"THE TEST FUNCTION READ AT ONE POINT, TIMES A DIMENSION"* count, no term surviving away from the identity; b311: at the archimedean place *"THE QUESTION THE FINITE"* side answers does not parse -- a refusal, not a negative result.',
             '130, 131 (b309); 132, 133 (b310); 134, 135 (b311)',
             'none typed by this act. To the archimedean rows (F1, F2): STATED non-transfer (b311). To the two-radius family (F6): STATED, the same object at a finite place.',
         ],
         quotes=[(bank('b309_the_scaling_trace.txt'), 'THE SCALING MAP HAS NO FIXED POINT OFF THE BALL', False),
                 (bank('b309_the_scaling_trace.txt'), 'IS THE ONE PLACE THE OBJECT IS REQUIRED TO VANISH', False),
                 (bank('b310_the_smear_collapses.txt'), 'THE TEST FUNCTION READ AT ONE POINT, TIMES A DIMENSION', False),
                 (bank('b311_the_identitys_neighbourhood.txt'), 'THE QUESTION THE FINITE', False),
                 (FINDINGS, 'does not type at the archimedean place', False)]),
    dict(id='F6',
         cells=[
             'F6 -- the two-radius family: one sentence, two truncation radii at every place; the finite family constructed, the archimedean family read at its source',
             'the object\'s space at each place -- and *"A family existing is not a route existing"* (the arc keystone)',
             'INTERNAL -- `phase2/method/THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md` (Tier C, b299), quoting b293, b295, b296, b286, b291, b285',
             'MEASURED and DERIVED, the finite side -- b293: *"THE FAMILY IS CONSTRUCTED."*, *"DIMENSION `(p^n - p^a)(p^n - p^b)`, DERIVED AND VERIFIED WITH ZERO MISMATCHES"*, set equality with the corpus\'s space at (0,0); b296: the annihilation criterion *"IF AND ONLY IF"*, necessity derived. IMPORTED, the archimedean member -- b286 *"(SUPPLIED BY SOURCE)"*. NAMED, the archimedean family as an object -- the arc\'s standing boundary: *"NO FINITE-SIDE STRUCTURAL FACT TYPES AT `infinity`."*',
             '104 (b293); 107 (b296); 114, 126 (b299)',
             'none typed by this act. To F5: STATED. To the Sonin margin (F2): STATED, the archimedean instruments *"compute with vectors that lie outside the object"*\'s own space (the adelic fold).',
         ],
         quotes=[(TWORAD, 'THE FAMILY IS CONSTRUCTED', False),
                 (TWORAD, 'DIMENSION `(p^n - p^a)(p^n - p^b)`', False),
                 (TWORAD, 'IF AND ONLY IF', False),
                 (TWORAD, '(SUPPLIED BY SOURCE)', False),
                 (TWORAD, 'A family existing is not a route existing', False),
                 (TWORAD, 'NO FINITE-SIDE STRUCTURAL FACT TYPES AT `infinity`', False),
                 (FINDINGS, 'compute with vectors that lie outside the object', False)]),
    dict(id='F7',
         cells=[
             'F7 -- the Epstein negative control at b326\'s result: the arc\'s instrument aimed at Z_Q (x² + xy + 6y², disc −23, h = 3), a positive Li ledger with RH false',
             'a control on the fourth\'s instrument -- the Weil-positivity face tested on a function whose hypothesis fails',
             'INTERNAL -- relay `data/b325_the_negative_control.txt`, `data/b326_the_reach.txt`. DEPOSITED, the premise of the test -- `outputs/DEPOSITED-v1.1.2/Which_Structure_Confines.md` line 85',
             'MEASURED -- b326: *"THE ARC\'S FAMILY, TWENTY-SIX CELLS TO `a = 400` : DOES NOT SEE IT"*; the formula closes for the Epstein function at 21 of 21 cells below its ceiling on a library of 146 on-line and 17 off-line zeros. THE FAMILY FINDING: *"A FAMILY THAT SEES THE FAILURE NEEDS A SIGN"* structure the arc\'s construction does not have -- the off-line four-term sums come out positive for a seed whose transform keeps its sign across β and 1 − β; *"A seed that changes sign there is"* priced, not built. THE ENTAILMENT: the zeta window at this reach *"IS A TEST THIS FAMILY CANNOT FAIL"*. b325: the ledger is the Li one, *"POSITIVITY IS OF THE COEFFICIENT SEQUENCE, NOT OF THE ZEROS"*. The deposit\'s premise: *"it does not confine zeros to it"*.',
             '162, 163 (b325); 164, 165 (b326)',
             'OWED -- `W-ORD-DISCRIMINATING-FAMILY` (pair F1-F7): the seed with a sign change across β and 1 − β, the construction that would let the instrument say no. To the Sonin margin (F2): STATED non-transfer. To the Li margin (F3): STATED, the positive ledger.',
         ],
         quotes=[(bank('b326_the_reach.txt'), "TWENTY-SIX CELLS TO `a = 400` : DOES NOT SEE IT", False),
                 (bank('b326_the_reach.txt'), 'A FAMILY THAT SEES THE FAILURE NEEDS A SIGN', False),
                 (bank('b326_the_reach.txt'), 'A seed that changes sign there is', False),
                 (bank('b326_the_reach.txt'), 'IS A TEST THIS FAMILY CANNOT FAIL', False),
                 (bank('b325_the_negative_control.txt'), 'POSITIVITY IS OF THE COEFFICIENT SEQUENCE, NOT OF THE ZEROS', False),
                 (CONF, 'it does not confine zeros to it', False)]),
]

# ### THE PAIR TABLE. ### key (a, b) with a before b in ROW ORDER (R1..R5, F1..F7, L1).
# ### value: (kind, text, quotes). kind in STATED / OWED / NONE. ### **EVERY PAIR IS PRESENT OR THE
# ### WRITER REFUSES**; the live row L1's pairs are supplied by b327_bridge.py through the same table.
REG_SENT = ('the deposit, section 27.3: *"These are one premise in five registers: kernel-theoretic, formal-interface, '
            'category-shaped, analytic, and spectral-geometric. A reader who discharges any one of them discharges all five."* '
            '-- and the equivalence is *"deliberately **not**"* compiled; this ledger compiles nothing.')
REG_Q = [(MONO, 'A reader who discharges any one of them discharges all five', False),
         (MONO, 'deliberately **not** compiling the cross-register equivalences', False)]

PAIRS = {}
for a, b in [('R1', 'R2'), ('R1', 'R3'), ('R1', 'R4'), ('R1', 'R5'), ('R2', 'R3'), ('R2', 'R4'), ('R2', 'R5'),
             ('R3', 'R4'), ('R3', 'R5'), ('R4', 'R5')]:
    PAIRS[(a, b)] = ('STATED', REG_SENT, REG_Q)

PAIRS[('R3', 'F1')] = ('STATED', 'the archimedean instrument arc\'s fold, b323: *"THE CLAUSE LIVES AT TOTALITY, AND THIS ARC NAMES THE MECHANISM BY WHICH NO FINITE"* instrument reaches it -- every quantity a truncation whose error the arc measures.',
                       [(bank('b323_the_fold.txt'), 'THE CLAUSE LIVES AT TOTALITY, AND THIS ARC NAMES THE MECHANISM BY WHICH NO FINITE', False)])
PAIRS[('R4', 'F1')] = ('STATED', 'b324, constituent (7): the arc\'s register is *"the FOURTH at most; it computes an explicit-formula balance and realizes no spectrum"*.',
                       [(bank('b324_the_keystones_reread.txt'), 'it computes an explicit-formula balance and realizes no spectrum', False)])
PAIRS[('R4', 'F2')] = ('STATED', 'b324: *"THE ARC BUILT AN INSTRUMENT INSIDE THE FIRST OF THREE NAMED FACES"* -- positivity of the Weil functional, which the deposit names and the arc did not.',
                       [(bank('b324_the_keystones_reread.txt'), 'THE ARC BUILT AN INSTRUMENT INSIDE THE FIRST OF THREE NAMED FACES', False)])
PAIRS[('R4', 'F3')] = ('STATED', 'the deposit, section 27.3: *"On the exact channel decomposition of the Li coefficients, this face takes its sharpest form: the premise is the inequality λ_Z(n) ≥ −λ_A(n) between two independently computable channels."*',
                       [(MONO, 'On the exact channel decomposition of the Li coefficients, this face takes its sharpest form', False)])
PAIRS[('R5', 'F4')] = ('STATED', 'b324, constituent (7) of the wall: the keystone\'s register is *"the FIFTH, the spectral-realization distance"* -- the wall is R5 under its internal name, and the deposit\'s nearest sentence is *"no positive pairing is known"*.',
                       [(bank('b324_the_keystones_reread.txt'), 'the FIFTH, the spectral-realization distance', False),
                        (MONO, 'no positive pairing is known', False)])
PAIRS[('F1', 'F2')] = ('STATED', 'b323: the identity\'s archimedean side splits, by Theorem 4.7, as the compressed square plus a remainder -- *"THAT REMAINDER IS THE MARGIN b320 MEASURED"*.',
                       [(bank('b323_the_fold.txt'), 'THAT REMAINDER IS THE MARGIN b320 MEASURED', False)])
PAIRS[('F1', 'F7')] = ('OWED', '`W-ORD-DISCRIMINATING-FAMILY`. The record states the closure -- b326: *"THE EXPLICIT FORMULA CLOSES FOR BOTH"* -- and states that the arc\'s family cannot discriminate: *"A FAMILY THAT SEES THE FAILURE NEEDS A SIGN"* structure the construction does not have. THE BRIDGE OWED IS A CONSTRUCTION: a lawful seed whose transform changes sign across β and 1 − β, priced at b326 at one act; it is the act that would let the identity on this instrument say no.',
                       [(bank('b326_the_reach.txt'), 'THE EXPLICIT FORMULA CLOSES FOR BOTH', False),
                        (bank('b326_the_reach.txt'), 'A FAMILY THAT SEES THE FAILURE NEEDS A SIGN', False)])
PAIRS[('F2', 'F3')] = ('OWED', '`W-ORD-LI-WEIL-BRIDGE`. b324 typed it: *"a formula carrying the archimedean margin"* `W_infinity(f) - Tr(theta(f) S)` at a lawful test function to the Li margin `lambda_n` at an index n, or a proof that no such formula exists. THE LIVE ROW L1 READS IT: the archimedean distribution is one on both families; the margins differ at their second term (a compressed square against the finite places), so the bridge stays OWED and is typed there.',
                       [(bank('b324_the_keystones_reread.txt'), 'a formula carrying the archimedean margin', False)])
PAIRS[('F2', 'F4')] = ('STATED', 'b324: the arc\'s space against the wall\'s space, *"VERDICT: ### DIFFERENT. ### SEVEN OF SEVEN."* -- a non-identity the record states; no bridge.',
                       [(bank('b324_the_keystones_reread.txt'), 'VERDICT: ### DIFFERENT. ### SEVEN OF SEVEN.', False)])
PAIRS[('F2', 'F7')] = ('STATED', 'b326: *"IT DOES NOT SAY THE SOURCE\'S INEQUALITY OR THE OBJECT\'S DECOMPOSITION TRANSFER"* -- Theorem 1 is stated for Gamma(s/2) and the Sonin space on zeta\'s unit; Z_Q\'s factor carries Gamma(s). A stated non-transfer.',
                       [(bank('b326_the_reach.txt'), "IT DOES NOT SAY THE SOURCE'S INEQUALITY OR THE OBJECT'S DECOMPOSITION TRANSFER", False)])
PAIRS[('F3', 'F4')] = ('STATED', 'b324: the deposit names positivity of the Weil functional, λ_n ≥ 0, and the number-field shadow as faces of one obligation, and *"EQUIVALENCE OF THE OBLIGATIONS IS NOT"* equivalence of the margins.',
                       [(bank('b324_the_keystones_reread.txt'), 'EQUIVALENCE OF THE OBLIGATIONS IS NOT', False)])
PAIRS[('F3', 'F7')] = ('STATED', 'the residue keystone: the sharpest test is a family with a *"positive ledger but RH false"* -- the Epstein zeta of a class-number-3 form; b325: the ledger is the Li one, *"POSITIVITY IS OF THE COEFFICIENT SEQUENCE, NOT OF THE ZEROS"*.',
                       [(RESIDUE, 'positive ledger but RH false', False),
                        (bank('b325_the_negative_control.txt'), 'POSITIVITY IS OF THE COEFFICIENT SEQUENCE, NOT OF THE ZEROS', False)])
PAIRS[('F5', 'F1')] = ('STATED', 'the instrument arc\'s fold: *"The mechanism that produces that silence does not type at the archimedean place"* -- a stated non-transfer from the finite-place silence to the archimedean instrument.',
                       [(FINDINGS, 'does not type at the archimedean place', False)])
PAIRS[('F5', 'F2')] = ('STATED', 'b311: the source\'s positivity is *"WHOSE ONLY NON-FUNCTION CONTENT IS AT THE"* identity -- the archimedean distribution\'s divergence at ρ = 1 is the one place the finite-place silence and the archimedean margin meet, and the finite mechanism does not type there.',
                       [(bank('b311_the_identitys_neighbourhood.txt'), 'WHOSE ONLY NON-FUNCTION CONTENT IS AT THE', False)])
PAIRS[('F5', 'F6')] = ('STATED', 'the instrument arc\'s fold: at a finite place the source\'s own construction, *"evaluated on the object"*\'s space -- the two-radius family\'s diagonal member -- returns the test function at one point times a dimension.',
                       [(FINDINGS, 'evaluated on the object', False)])
PAIRS[('F6', 'F2')] = ('STATED', 'the adelic fold: *"The archimedean instruments compute with vectors that lie outside the object"*\'s own space -- the family\'s archimedean member and the instrument\'s vectors are kept apart.',
                       [(FINDINGS, 'compute with vectors that lie outside the object', False)])

ORDER = ['R1', 'R2', 'R3', 'R4', 'R5', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'L1']

# ### the live row's pairs are added by b327_bridge.py; every remaining pair is NONE, made explicit by
# ### the writer so that no pair is silently absent.
NONE_TEXT = 'NONE -- the record states no relation and this act types no bridge.'
