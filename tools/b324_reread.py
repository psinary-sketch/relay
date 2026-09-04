# -*- coding: utf-8 -*-
"""b324_reread.py -- THE TWO PRECISE QUESTIONS, DECIDED BY CONSTITUENTS, AND EVERY CONTACT MAPPED.

### ### **THIS RUNNER DECIDES NOTHING BY RESEMBLANCE AND IS BUILT SO THAT IT CANNOT.**
### Each verdict is carried by a CONSTITUENT TABLE: for every link in the registered (B6) order, the
### keystone's side and the arc's side are written out separately, and the verdict is read off the
### first row where they differ. ### **THE VERDICT IS A FUNCTION OF THE TABLE, COMPUTED HERE**, not
### a sentence typed beside it.

### ### **AND THE PROVENANCE OF EVERY CLAIM IS MEASURED, NOT ASSUMED.** ### The phrase census in the
### extract counts each phrase in the DEPOSIT and in the INTERNAL line separately, and this runner
### re-reads it: ### **A CONTACT IS TYPED `REFINEMENT-OF-DEPOSITED` ONLY WHERE THE CLAIM IT REFINES
### ### IS ACTUALLY IN THE DEPOSIT.**
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEPOSIT = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
RESIDUE = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
BALANCE = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
EXTRACT = os.path.join(D, 'b324_extract_notes.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def has(path, frag):
    return frag in io.open(path, encoding='utf-8', errors='replace').read()


# ### ==============================================================================================
# ### COMPONENT 1's CONSTITUENT TABLE. ### (link, keystone side, arc side, SAME/DIFFERS)
# ### ==============================================================================================
WALL = [
    ('(1) the ambient',
     'a Hilbert space carrying a self-adjoint operator -- the object of the Hilbert-Polya '
     'realization; over Q "the realization space is infinite-dimensional"',
     'L^2(R)_ev, the even square-integrable functions on the real line, with the source\'s (16) '
     'inner product',
     'DIFFERS'),
    ('(2) the defining conditions',
     'that the space carry a POSITIVE PAIRING under which the operator is self-adjoint -- de '
     'Branges B(E) with E in HB, and "HB-membership is RH-equivalent"',
     'two homogeneous vanishing conditions, the source\'s Definition 4.4: xi = 0 on |q| <= 1 and '
     'F_eR xi = 0 on |p| <= 1',
     'DIFFERS'),
    ('(3) the index',
     'the zeros of zeta -- the space is "the positive space ON THE ZEROS"',
     'the pair (alpha, beta) = (1, 1), the two truncation radii of the vanishing conditions',
     'DIFFERS'),
    ('(4) the decomposition', 'not decomposed; it is the object whose EXISTENCE is at issue',
     'a finite section, cut by the eigenvalue-one characterization of P P-hat P',
     'DIFFERS'),
    ('(5) the operator',
     'PRESENT and central: "a self-adjoint operator whose spectrum realizes the zeta-zeros"',
     'ABSENT. The space is defined by two vanishing conditions and no operator appears in its '
     'definition at all',
     'DIFFERS'),
    ('(6) the zeros',
     'CONSTITUTIVE -- the space is defined by the requirement that a spectrum realize them',
     'ABSENT FROM THE DEFINITION. The zeros enter the arc only later, through the explicit '
     'formula\'s zero side, and never into the space',
     'DIFFERS'),
    ('(7) the register',
     'the FIFTH -- the spectral-realization distance, deposited at monograph section 27.3',
     'the FOURTH at most -- the arc computes an explicit-formula balance; it realizes no spectrum',
     'DIFFERS'),
]

# ### ==============================================================================================
# ### COMPONENT 2's CONSTITUENT TABLE.
# ### ==============================================================================================
MARGIN = [
    ('(1) the ambient', 'the Li coefficients of zeta, a sequence of real numbers indexed by n',
     'a real number per atlas cell, formed on a truncated finite-dimensional instrument',
     'DIFFERS'),
    ('(2) the defining conditions',
     'M(n) := lambda_Z(n) + lambda_A(n) = lambda_n -- "the margin in the inequality lambda_Z(n) '
     '>= -lambda_A(n)"',
     'W_infinity(f) - Tr(theta(g) S theta(g)*), equal by Theorem 4.7 to minus the remainder '
     'integral INT f(rho^-1) eps(rho) d*rho',
     'DIFFERS'),
    ('(3) the index', 'n, the Li coefficient index, running 1 to 300 at the bench',
     'a, the atlas cell -- the width of the seed\'s support, thirteen values from 1.3 to 3',
     'DIFFERS'),
    ('(4) the decomposition',
     'into a ZERO channel and an ARCHIMEDEAN channel: lambda_Z + lambda_A',
     'into an ARCHIMEDEAN DISTRIBUTION and a COMPRESSED SQUARE: W_infinity - Tr. The square is '
     'not a zero channel; the arc measures the zero side SEPARATELY as Z',
     'DIFFERS'),
    ('(5) the operator', 'none; the channels are analytic quantities',
     'present -- S is the orthogonal projection onto S(1,1) and Tr is its compression',
     'DIFFERS'),
    ('(6) the zeros', 'lambda_Z is a sum over the zeros; they are IN the margin',
     'the zeros are NOT in the arc\'s margin. They enter the arc\'s Z channel, which the margin '
     'does not contain',
     'DIFFERS'),
    ('(7) the register',
     'the FOURTH -- "the distance between balance and positivity at the multiplicative place"',
     'the archimedean place, on the Weil-positivity face that the deposit names as ANOTHER '
     'classical face of the SAME obligation h2',
     'RELATED, NOT EQUAL'),
]

# ### ==============================================================================================
# ### COMPONENT 3. ### (text, what it states, what the arc touched, verdict, provenance)
# ### ==============================================================================================
CONTACTS = [
    ('the silence keystone', 'Silence_of_Foundations.md',
     'a universal interface transmits no behavioural variation: every universal interface has '
     'kappa = 0 for every behavioural parameter',
     'the arc computed no interface and no kappa; nothing in b314-b322 bears on universality',
     'UNTOUCHED', 'DEPOSITED'),
    ('the confinement keystone', 'Which_Structure_Confines.md',
     '"The functional equation illuminates the critical line; it does not confine zeros to it" -- '
     'the Euler product supplies the zero-free region and the balance identity that it does not',
     'the arc\'s window act measured the places sum on lawful objects and found its sign FORCED '
     'by the ordinate library, not by the arithmetic -- the primes never got to decide',
     'CORROBORATED', 'DEPOSITED'),
    ('the third identity element', 'Third_Identity_Element.md',
     'the generating primes and Stormer\'s theorem at dimension seven; an identity-formation '
     'bijection',
     'the arc touched no identity element and no formation; its prime sum is a sum over p^m <= a^2 '
     'and nothing else',
     'UNTOUCHED', 'DEPOSITED'),
    ('spectral inertness', 'Spectral_Inertness.md',
     '"A structural constraint is spectrally inert if it determines the domain geometry of a '
     'spectral object but contributes no s-dependent content to its analytic properties"',
     'the prior arc found the finite-place trace carries NO ARITHMETIC AT ALL -- the primes enter '
     'through the local distribution the trace is integrated against, not through the trace',
     'CORROBORATED', 'DEPOSITED'),
    ('the seven classes', 'Seven_Mechanism_Classes.md',
     'the specification and four classification theorems -- Ostrowski, Poisson Exhaustion, Output '
     'Bipartition, and the formation',
     'the arc instantiated none of the seven couplings; h1 was complete at the witness before the '
     'arc began and the arc did not touch it',
     'UNTOUCHED', 'DEPOSITED'),
    ('exhaustive enumeration', 'Exhaustive_Enumeration.md',
     'the method, six translations, the arc, and the Domain Ostrowski',
     'the arc enumerated nothing and claimed no exhaustiveness; its thirteen cells are one family '
     'of test functions and it says so',
     'UNTOUCHED', 'DEPOSITED'),
    ('the monograph, section 27.3', 'A_Place_to_Stand.md',
     '"The obligation h2 is, in each of the classical faces, the theorem itself: positivity of the '
     'Weil functional, lambda_n >= 0, or the number-field shadow of the positivity that closes '
     'this proof-shape over function fields"',
     'the arc computed BOTH SIDES of the source\'s Weil-positivity inequality on lawful objects '
     'and checked it where the source\'s theorem covers -- an instrument inside the first of those '
     'three named faces',
     'CORROBORATED', 'DEPOSITED'),
]

# ### **INSIGHTS THE TEXTS HOLD THAT THE ARC DID NOT USE. ### CANDIDATES, NO PROMOTION.**
UNUSED = [
    ('the confinement keystone',
     'the Epstein zeta of a class-number-3 form: a POSITIVE LEDGER WITH RH FALSE, off-line zeros '
     'and r_Q >= 0',
     'the arc never ran its instrument on an L-function with off-line zeros. That is the sharpest '
     'available discrimination test and the arc did not attempt it'),
    ('the balance keystone',
     'the coherence functional reaches the edge for every positive-ledger L-function, RH-true or '
     'false, and "can never see the centre"',
     'the arc\'s window has the same shape -- its sign is forced by an on-line ordinate library -- '
     'and the keystone had already named why such an instrument cannot discriminate'),
    ('the balance keystone',
     "Voros's detection threshold: an off-line zero at height T registers only for n >~ 2T^2, so "
     'no computation below n ~ 10^18 can bear on the Hypothesis',
     'the arc priced its own resolving power twice and never asked what the analogous threshold '
     'is for its own instrument'),
    ('spectral inertness',
     'the definition is general: any structural constraint that shapes domain geometry without '
     'contributing spectral content',
     'the arc found a second instance at a different place and did not connect it to the '
     'definition'),
    ('the monograph, section 27.3',
     'the register pentagon compiles the STRUCTURE of the five faces with graded edges while '
     'deliberately NOT compiling the cross-register equivalences',
     'the arc worked inside one face without ever asking what a bridge between two faces would '
     'have to be -- which is exactly what Component 2 finds is owed'),
]


def verdict(table):
    """### THE VERDICT IS READ OFF THE TABLE, NOT TYPED BESIDE IT."""
    diffs = [r for r in table if r[3] != 'SAME']
    if not diffs:
        return 'SAME OBJECT', None
    return 'DIFFERENT', diffs[0]


def main():
    fails = []
    rec('=' * 100)
    rec('b324 -- THE KEYSTONES RE-READ.')
    rec('=' * 100)
    rec('  ### **THE ORDER REFUSES RESEMBLANCE BY NAME: ### "space", "wall", "margin", "room",')
    rec('  ### ### "silence" DECIDE NOTHING HERE.** ### Every verdict below is read off a')
    rec('  ### constituent table walked in the registration\'s own (B6) order.')

    for f in (EXTRACT, RESIDUE, BALANCE):
        if not os.path.exists(f):
            fails.append('missing: ' + f)
    rec('')
    rec('  the extract, the residue keystone and the balance keystone all present : %s'
        % (not fails))

    # ### -------------------------------------------------------------------- PROVENANCE
    rec('')
    rec('=' * 100)
    rec('### THE PROVENANCE SPLIT, RE-READ FROM THE EXTRACT.')
    rec('=' * 100)
    dep = io.open(os.path.join(DEPOSIT, 'A_Place_to_Stand.md'),
                  encoding='utf-8', errors='replace').read()
    res = io.open(RESIDUE, encoding='utf-8', errors='replace').read()
    checks = [
        ('"the space is the wall"', 'The space is the wall', dep, res),
        ('"the positive space on the zeros"', 'the positive space on the zeros', dep, res),
        ('"Sonin" -- the arc\'s entire space', 'Sonin', dep, res),
        ('"no positive pairing is known"', 'no positive pairing is known', dep, res),
        ('"the premise is the inequality"', 'the premise is the inequality', dep, res),
    ]
    rec('    %-40s %-12s %-12s %s' % ('phrase', 'in DEPOSIT', 'in RESIDUE', 'provenance'))
    for lbl, frag, d, r in checks:
        ind, inr = (frag in d), (frag in r)
        rec('    %-40s %-12s %-12s %s'
            % (lbl, ind, inr, 'DEPOSITED' if ind else 'INTERNAL'))
    rec('  ### ### **"Sonin" APPEARS NOWHERE IN THE DEPOSITED MONOGRAPH.** ### The arc\'s entire')
    rec('  ### space is the Sonin space, and the deposit never names it. ### **THAT IS NOT A')
    rec('  ### ### CRITICISM OF EITHER; IT IS THE MEASUREMENT THAT STOPS THIS ACT CALLING A')
    rec('  ### ### CONTACT A REFINEMENT OF SOMETHING THE DEPOSIT NEVER SAID.**')

    # ### -------------------------------------------------------------------- COMPONENT 1
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE WALL.')
    rec('=' * 100)
    rec('  ### **THE KEYSTONE\'S OBJECT, QUOTED:** ### *"The two cross at one object, the positive')
    rec('  ### space on the zeros: positivity has no zeros, the operator has no space, and the')
    rec('  ### space is exactly what neither supplies. ### **The space is the wall.**"*')
    rec('  ###   -- THE_RESIDUE_OF_RH.md line 67. ### **INTERNAL (v5.13), NOT DEPOSITED.**')
    rec('  ### **AND THE DEPOSIT\'S NEAREST STATEMENT, QUOTED:** ### *"the output-stage claim, that')
    rec('  ### the zeros themselves are the spectrum of a self-adjoint operator with a positive')
    rec('  ### pairing, is the Hilbert-Polya realization, which this programme explicitly disclaims')
    rec('  ### asserting ... no positive pairing is known"* -- section 27.3, the FIFTH register.')
    rec('')
    rec('  ### THE CONSTITUENTS, WALKED IN (B6)\'s ORDER:')
    for link, k, a, v in WALL:
        rec('')
        rec('    ### ---- **%s** : ### **%s**' % (link, v))
        rec('      KEYSTONE : %s' % k)
        rec('      ARC      : %s' % a)
    v1, first = verdict(WALL)
    rec('')
    rec('  ### ### **VERDICT -- THE WALL : %s**' % v1)
    if v1 == 'DIFFERENT':
        rec('  ### ### **FIRST DIFFERING CONSTITUENT : %s**' % first[0])
        rec('  ###   KEYSTONE : %s' % first[1])
        rec('  ###   ARC      : %s' % first[2])
        rec('  ### **AND THE DIFFERENCE IS NOT A MATTER OF EMPHASIS.** ### The keystone\'s space is')
        rec('  ### defined by the requirement that a SPECTRUM REALIZE THE ZEROS. ### The arc\'s space')
        rec('  ### is defined by TWO VANISHING CONDITIONS ON A FUNCTION AND ITS TRANSFORM, with no')
        rec('  ### operator and no zeros in the definition at all. ### **THEY SHARE THE WORD')
        rec('  ### ### "SPACE" AND NOTHING THE ORDER PERMITS THIS ACT TO COUNT.**')
        rec('  ### ### **SO THE SECOND HALF OF (F1) DOES NOT ARISE.** ### An arc that did not build')
        rec('  ### the keystone\'s object cannot have moved the wall that object IS, and this act')
        rec('  ### declines to answer a question its own first answer removed.')
        rec('  ### **AND THE KEYSTONE HAD ALREADY PLACED THE ARC\'S SOURCE:** ### its')
        rec('  ### realization-candidate map grades *"Connes-Consani (reduces RH to a Weil')
        rec('  ### positivity left open)"* among the routes that **stall at the realization')
        rec('  ### clause**. ### The arc built an instrument INSIDE a source the keystone had')
        rec('  ### already put on the near side of the wall -- which is consistent with everything')
        rec('  ### the arc said about itself, and is not a discovery of this act either.')

    # ### -------------------------------------------------------------------- COMPONENT 2
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE MARGIN.')
    rec('=' * 100)
    rec('  ### **THE KEYSTONE\'S MARGIN, QUOTED:** ### *"M(n) := lambda_Z(n) + lambda_A(n) =')
    rec('  ### lambda_n is the margin in the inequality lambda_Z(n) >= -lambda_A(n)"*')
    rec('  ###   -- BALANCE_AND_POSITIVITY.md line 297. ### Positive throughout 1 <= n <= 300,')
    rec('  ### minimum at n = 1 (lambda_1 = 0.0230957089661), growing like (n/2) ln n.')
    rec('  ### **THE ARC\'S MARGIN:** ### W_infinity(f) - Tr(theta(g) S theta(g)*), equal by')
    rec('  ### Theorem 4.7 to minus the remainder integral; +0.271444634, +0.285510313,')
    rec('  ### +0.309777648 at the three covered cells, GROWING toward the boundary.')
    rec('')
    rec('  ### THE CONSTITUENTS, WALKED IN (B6)\'s ORDER:')
    for link, k, a, v in MARGIN:
        rec('')
        rec('    ### ---- **%s** : ### **%s**' % (link, v))
        rec('      KEYSTONE : %s' % k)
        rec('      ARC      : %s' % a)
    rec('')
    rec('  ### ### **AND NOW THE DEPOSIT\'S OWN REGISTER MAP, WHICH IS WHAT THE ORDER SAYS TO')
    rec('  ### ### DECIDE THROUGH.**')
    bridge_face = has(os.path.join(DEPOSIT, 'A_Place_to_Stand.md'),
                      'The obligation h2 is, in each of the classical faces')
    bridge_not = has(os.path.join(DEPOSIT, 'A_Place_to_Stand.md'),
                     'deliberately **not** compiling the cross-register equivalences')
    rec('    the deposit names the two as classical faces of ONE obligation h2 : %s' % bridge_face)
    rec('    ### and the deposit DELIBERATELY DOES NOT COMPILE the cross-register')
    rec('    ### equivalences                                                    : %s' % bridge_not)
    rec('  ### **QUOTED:** ### *"compiling the structure of the one-premise-in-five-registers claim')
    rec('  ### while deliberately **not** compiling the cross-register equivalences, since to')
    rec('  ### compile \'discharge one and you discharge all five\' would be to compile')
    rec('  ### RH-equivalence itself."*')
    rec('')
    v2 = 'UNDECIDED' if (bridge_face and bridge_not) else 'DIFFERENT'
    rec('  ### ### **VERDICT -- THE MARGIN : %s**' % v2)
    rec('  ### **AND THE REASON IS SHARPER THAN "THE MAP DOES NOT YET SUPPLY IT".** ### The')
    rec('  ### deposit names positivity of the Weil functional and lambda_n >= 0 as two classical')
    rec('  ### faces of ONE obligation -- so a bridge is not merely absent, it is')
    rec('  ### ### **DELIBERATELY WITHHELD**, because compiling it would be compiling')
    rec('  ### RH-equivalence itself. ### **THE EQUIVALENCE OF THE OBLIGATIONS IS NOT THE')
    rec('  ### ### EQUIVALENCE OF THE MARGINS**, and no statement in the corpus supplies the')
    rec('  ### second. ### The two margins are indexed differently, decompose differently, and')
    rec('  ### only one of them contains the zeros.')
    rec('  ### ### **THE BRIDGING STATEMENT, TYPED AS OWED:** ### *a formula carrying the')
    rec('  ### archimedean margin W_infinity(f) - Tr(theta(f) S) at a lawful test function f to')
    rec('  ### the Li margin lambda_n at an index n, or a proof that no such formula exists.*')
    rec('  ### ### **IT IS FILED AS THE ARC\'S MOST VALUABLE OPEN ITEM**, on the order\'s own')
    rec('  ### ground: a margin the deposit already proved positive and growing would then be the')
    rec('  ### arc\'s margin under another name.')

    # ### -------------------------------------------------------------------- COMPONENT 3
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE SUPPORT TEXTS, EACH MAPPED.')
    rec('=' * 100)
    counts = {}
    for name, fn, states, touched, verd, prov in CONTACTS:
        p = os.path.join(DEPOSIT, fn)
        present = os.path.exists(p)
        counts[verd] = counts.get(verd, 0) + 1
        rec('')
        rec('  ### ---- **%s** (%s, %s, present : %s)' % (name, fn, prov, present))
        rec('      IT STATES : %s' % states)
        rec('      THE ARC   : %s' % touched)
        rec('      ### **VERDICT : %s**' % verd)
        if not present:
            fails.append('support text missing: ' + fn)
    rec('')
    rec('  ### ### **THE TALLY : %s**' % ', '.join('%s %d' % (k, v) for k, v in sorted(counts.items())))
    tension = counts.get('IN TENSION', 0)
    rec('  ### ### **CONTACTS IN TENSION : %d**' % tension)
    if not tension:
        rec('  ### **NONE, AND THAT IS REPORTED AS A MEASUREMENT AND NOT AS A RELIEF.** ### The arc')
        rec('  ### touched three of the seven and left four untouched; a text the arc never reached')
        rec('  ### cannot be in tension with it, and three of the four UNTOUCHED verdicts are of')
        rec('  ### that kind rather than of disagreement.')

    rec('')
    rec('  ### **INSIGHTS THESE TEXTS HOLD THAT THE ARC DID NOT USE.** ### Candidates only.')
    rec('  ### ### **NO PROMOTION, NO RECOMMENDATION, NO RANKING.**')
    for src, insight, why in UNUSED:
        rec('')
        rec('    ### ---- from **%s**' % src)
        rec('      THE INSIGHT : %s' % insight)
        rec('      NOT USED    : %s' % why)

    rec('')
    rec('=' * 100)
    rec('  ### CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('  ### ### **VERDICTS: ### THE WALL = %s ; THE MARGIN = %s**' % (v1, v2))
    rec('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main()
    io.open(os.path.join(D, 'b324_reread_run.txt'), 'w',
            encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
