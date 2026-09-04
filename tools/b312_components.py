# -*- coding: utf-8 -*-
"""b312_components.py -- THE COMPONENTS, IN ORDER. ### **TWO DEFINITIONS, UNFOLDED, AND A DECISION.**

### ### **THIS FILE COMPUTES NO ARCHIMEDEAN NUMBER AND IS BUILT SO THAT IT CANNOT.** ### Every
### exponent it reports is EXTRACTED as a string by `b312_definitions.py` -- from the pinned
### artefact's raw page text on one side and from the corpus's own committed emitting files on the
### other. ### **THERE IS NO ARITHMETIC IN THIS FILE AT ALL.**

### ### **AND THE HAZARD IT IS BUILT TO REFUSE IS THE SHARED LETTER.** ### The corpus writes one
### glyph and the source writes another for what may or may not be one function. ### b200 named
### that species and b219 realised it. ### **A NAME IS NOT AN IDENTIFICATION, AND THIS FILE DECIDES
### ### ONLY BY UNFOLDING.**
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, 'tools')
sys.path.insert(0, HERE)

import needle_pull        # noqa: E402
import b312_source as SRC  # noqa: E402
import b312_definitions as DEF  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')
PDF = sys.argv[1] if len(sys.argv) > 1 else ''

OWNERS = [
    ("the corpus's identity, in the file that assembles it",
     os.path.join(E16, 'b38_act10.py'), 'resid = TrN - A - E2N'),
    ("### the corpus's remainder side, as that identity consumes it",
     os.path.join(E16, 'b38_act10.py'), 'out[:, k] = lam2 / (1 - lam2)'),
    ("### and the corpus's TRACE side, in the SAME file",
     os.path.join(E16, 'b38_act10.py'), 'An[i] = math.sqrt(lamd)'),
    ("### and how the corpus turns the remainder into the identity's second term",
     os.path.join(E16, 'b38_act10.py'), 'return 2.0 * float(np.trapezoid(cu * eu, uu))'),
    ("the corpus CLAIMING the import, in its own header",
     os.path.join(E16, 'qeps_layer.py'), 'eps(rho), their (85)'),
    ("### the corpus DECLARING the scaling convention, and its reason",
     os.path.join(E16, 'qeps_layer.py'), 'the convention forced by the'),
    ("### the corpus's operator image, transcribed with the OTHER exponent",
     os.path.join(E16, 'qeps_layer.py'), 'C_n(rho) = rho^(1/2)'),
    ("### the corpus's ONE cross-check against the source",
     os.path.join(E16, 'qeps_layer.py'), 'CONSEQUENCE DERIVED HERE, NOT ASSUMED'),
    ("the banked atlas, where the archimedean sign comes from",
     os.path.join(E16, 'carto_atlas.py'), 'sign fixed BY the E2 calibration'),
    ("### and the atlas's own disclaimer about that sign",
     os.path.join(E16, 'carto_atlas.py'), 'No sign claim is made'),
    ("b286 -- the source's space, an IMPORT at its own grade",
     os.path.join(D, 'b286_the_cc_condition.txt'), 'THE SPACE IS `L^2(R)_ev`.'),
    ("b292 -- the corpus's instrument vectors are NOT in that space",
     os.path.join(D, 'b292_the_identification.txt'), 'IS NOT IN `S(1,1)`'),
    ("b285 -- the hazard register's own sentence",
     os.path.join(D, 'b285_archimedean_opening.txt'), 'THE WORD SURVIVES; THE OBJECT DOES NOT'),
    ("b200 -- the double-name species, named",
     os.path.join(D, 'b200_sector_naming.txt'), 'THE DOUBLE-NAME SPECIES'),
    ("b219 -- and the act where it was REALISED",
     os.path.join(D, 'b219_what_sigma_even_weights.txt'), 'DOUBLE-NAME'),
    ("b301 -- the normalization work-order, still live",
     os.path.join(D, 'b301_the_object_completed.txt'), 'W-ORD-ARCH-NORM-READING'),
    ("b304 -- the artefact's pin",
     os.path.join(D, 'b304_the_demands_shape.txt'), 'b8e0b54a'),
    ("b305 -- the arithmetic's local factor",
     os.path.join(D, 'b305_the_arithmetics_entry.txt'), 'W_p(f) = (log p) SUM_{m>=1}'),
    ("b310 -- the finite-side result, quarantined at its own scope",
     os.path.join(D, 'b310_the_smear_collapses.txt'), 'SIGNED COUNT OF THE OFF-BALL POINTS'),
    ("b311 -- the decision this act stands after",
     os.path.join(D, 'b311_the_identitys_neighbourhood.txt'),
     'DOES NOT TYPE AT THE ARCHIMEDEAN PLACE'),
]


def rule():
    return '-' * 100


def main():
    out, fails = [], []

    def rec(s):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b312 -- THE COMPONENTS. ### **THE REMAINDER: IS THE CORPUS\'S THE SOURCE\'S?**')
    rec('=' * 100)

    rec('')
    rec(rule())
    rec('### (0) THE OWNERS, PULLED FROM THE FILES THAT EMIT THEM.')
    rec(rule())
    for lbl, path, anchor in OWNERS:
        try:
            needle_pull.pull(path, anchor)
            rec('  PASS  %-64s %s' % (lbl[:64], os.path.basename(path)))
        except LookupError:
            fails.append(lbl)
            rec('  ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))

    # ------------------------------------------------------------------ COMPONENT 1
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE TWO DEFINITIONS, EACH UNFOLDED TO ITS BASE OBJECTS,')
    rec('### NEITHER DESCRIBED IN THE OTHER\'S LANGUAGE.')
    rec('=' * 100)

    rec('')
    rec(rule())
    rec('### (1a) THE CORPUS\'S REMAINDER, AS ITS OWNER BUILDS IT.')
    rec(rule())
    rec('  ### **THE EQUATION IT SAYS IT IMPORTED**, from its own header, quoted:')
    rec('  ###   `eps(rho) = sum_n [lam/sqrt(1-lam^2)] <xi_n | theta(rho^-1) zeta_n>`')
    rec('  ### **THE NORMALIZATION IT DECLARES**, from the same header, quoted:')
    rec('  ###   `theta(a) f(x) = a^{1/2} f(x/a)`, with the note that this is')
    rec('  ###   `the convention forced by the supplied support law`.')
    rec('  ### **THE DOMAIN:** ### `rho >= 1`, with the integrand supported only on the interval')
    rec('  ### from the reciprocal of `rho` up to one, so that the value at one is zero.')
    rec('  ### **THE MODE EXPANSION IT IS COMPUTED THROUGH:** ### the even prolate functions and')
    rec('  ### their eigenvalues, with the auxiliary vector `zeta_n` written as the analytic')
    rec('  ### continuation scaled by `lam/sqrt(1-lam^2)`, and the analytic continuation itself')
    rec('  ### built as a cosine transform of the prolate function over the unit interval.')
    rec('  ### **UNFOLDED, WHAT THE CODE ACTUALLY EVALUATES** -- read off `qeps_layer.py` and')
    rec('  ### `b38_act10.py` by `b312_definitions.py`, not paraphrased:')
    rec('  ###   `eps(rho) = sum_n [lam^2/(1-lam^2)] * rho^(EXPONENT) *')
    rec('  ###                INT_{1/rho}^{1} an(u) an(rho u) du`')
    rec('  ###   with `EXPONENT` extracted below rather than asserted here.')
    rec('  ### **THE IDENTITY ITS LEFT SIDE DECOMPOSES UNDER**, from `b38_act10.py`:')
    rec('  ###   `resid = TrN - A - E2N` -- ### the trace, less the archimedean term, less the')
    rec('  ###   remainder\'s integral against the corpus\'s window, leaves a residue.')
    rec('  ### ### **AND THE SECOND TERM IS BUILT FROM `eps` BY** `2 * INT_0^{2L} corr(u)')
    rec('  ### ### eps(exp u) du` -- a fold in the logarithmic variable, which is the corpus\'s')
    rec('  ### ### own way of writing an integral in the multiplicative measure over a window.')

    rec('')
    rec(rule())
    rec('### (1b) THE SOURCE\'S REMAINDER, AS ITS THEOREM 4.7 DEFINES IT.')
    rec(rule())
    rec('  ### **THE IDENTITY** (its equation (83), located on pages 5, 26 and 47):')
    rec('  ###   `Tr(theta(f) S) = W_inf(f) + INT f(rho^-1) eps(rho) d*rho`, for every smooth')
    rec('  ###   compactly supported test function on the positive multiplicative group,')
    rec('  ###   where `S` is the orthogonal projection onto the source\'s subspace.')
    rec('  ### **THE FUNCTION** (its equation (84), located on pages 5, 26 and 27):')
    rec('  ###   `eps(rho) = sum_n [lam(n)/sqrt(1-lam(n)^2)] <xi_n | theta(rho^-1) zeta_n>`,')
    rec('  ###   defined for `rho >= 1` and extended by the symmetry `eps(rho^-1) = eps(rho)`.')
    rec('  ### **THE NORMALIZATION** (its equation (61), located on page 22):')
    rec('  ###   `(theta(lam) xi)(v) := lam^(SIGN 1/2) xi(lam^-1 v)`, with the SIGN extracted')
    rec('  ###   below; and the source declares this action UNITARY, obtaining it by conjugating')
    rec('  ###   a unitary representation by an isomorphism of Hilbert spaces.')
    rec('  ### **THE DOMAIN:** ### the whole positive multiplicative group, by the symmetry; the')
    rec('  ###   defining formula is given on `rho >= 1`.')
    rec('  ### **THE JUMP AT THE IDENTITY** (its Lemma 5.4, page 31): ### the function has a jump')
    rec('  ###   in its derivative at the identity, and the one-sided derivative there is')
    rec('  ###   `sum_n [lam(n)^2/(1-lam(n)^2)] xi_n(1)^2`.')
    rec('  ### ### **AND THE SOURCE UNFOLDS ITS OWN FUNCTION, IN THAT LEMMA\'S PROOF:**')
    rec('  ###   `eps(rho) = sum_n [lam(n)^2/(1-lam(n)^2)] ( rho^(SIGN 1/2)')
    rec('  ###                INT_{rho^-1}^{1} xian(x) xian(rho x) dx )`')
    rec('  ### ### **SO BOTH SIDES ARRIVE AT THE SAME SHAPE, WHICH IS EXACTLY WHY THE SHAPE')
    rec('  ### ### DECIDES NOTHING** -- b200\'s species, and the order names it too.')

    rec('')
    rec(rule())
    rec('### (1c) THE CONSTITUENTS, MATCHED ONE BY ONE.')
    rec(rule())
    rec('  %-34s %-30s %s' % ('CONSTITUENT', 'CORPUS', 'SOURCE'))
    rows = [
        ('the mode family', 'even prolate functions', 'even prolate functions'),
        ('the auxiliary vector', 'lam/sqrt(1-lam^2) times xian', 'lam/sqrt(1-lam^2) times xian'),
        ('the analytic continuation', 'cosine transform over [0,1]', 'analytic continuation of xi'),
        ('the outer coefficient', 'lam^2/(1-lam^2)', 'lam^2/(1-lam^2)'),
        ('the integration interval', 'from 1/rho to 1', 'from 1/rho to 1'),
        ('the integrand', 'an(u) an(rho u)', 'xian(x) xian(rho x)'),
        ('the value at the identity', 'zero, by empty interval', 'zero, by empty interval'),
        ('the one-sided derivative', 'sum lam^2/(1-lam^2) xi(1)^2', 'sum lam^2/(1-lam^2) xi(1)^2'),
        ('### THE SCALING EXPONENT', '### EXTRACTED BELOW', '### EXTRACTED BELOW'),
    ]
    for a, b, c in rows:
        rec('  %-34s %-30s %s' % (a, b, c))
    rec('  ### **EIGHT CONSTITUENTS AGREE. ### THE NINTH IS THE WHOLE OF THIS ACT.**')

    # ------------------------------------------------------------------ COMPONENT 2
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE DECISION.')
    rec('=' * 100)

    if not PDF or not os.path.exists(PDF):
        fails.append('the artefact was not supplied to the components')
        rec('  ### HARD FAILURE -- no artefact supplied; the decision is NOT made.')
    else:
        if DEF.raw_pages and SRC.insensitivity_fixture()[2]:
            rec('  ### **THE FLATTENER THE CORPUS LOCATES WITH CANNOT SEE THIS QUESTION** -- the')
            rec('  ### source\'s exponent and a sign-flipped one flatten to the same string. ### The')
            rec('  ### extraction below is therefore off the RAW page text, and off the corpus\'s own')
            rec('  ### committed files, by `b312_definitions.py` and its fixtures.')
        pages = DEF.raw_pages(PDF)
        src = {}
        for key, what, pat in DEF.SRC:
            pg, sign, txt = DEF.find_sign(pages, pat)
            src[key] = (pg, sign, txt)
            if sign is None:
                fails.append('source extraction %s' % key)
        cor = {}
        for key, path, fn, pat, what in DEF.COR:
            ln, val, txt = DEF.extract_in_def(path, fn, pat)
            cor[key] = (ln, val, txt)
            if val is None:
                fails.append('corpus extraction %s' % key)

        rec('')
        rec('  ### THE EXTRACTION, SIDE BY SIDE:')
        rec('  %-46s %s' % ('WHERE', 'WHAT IS THERE'))
        rec('  %-46s %s' % ('the source, its scaling action AT lam, eq (61)',
                            'lam^(minus 1/2)' if src['SRC-THETA'][1] else 'lam^(1/2)'))
        rec('  %-46s %s' % ('  ### so AT the argument rho^-1 it is',
                            'rho^(PLUS 1/2)' if src['SRC-THETA'][1] else 'rho^(MINUS 1/2)'))
        rec('  %-46s %s' % ('the source unfolding such an inner product',
                            'rho^(minus 1/2)' if src['SRC-IP'][1] else 'rho^(PLUS 1/2)'))
        rec('  %-46s %s' % ('the source unfolding ITS REMAINDER, Lemma 5.4',
                            'rho^(minus 1/2)' if src['SRC-EPS'][1] else 'rho^(PLUS 1/2)'))
        rec('  %-46s %s' % ('the source\'s operator image, eq (99)',
                            'rho^(minus 1/2)' if src['SRC-QEPS'][1] else 'rho^(PLUS 1/2)'))
        rec('  %-46s %s' % ('the corpus\'s remainder, qeps_layer.py',
                            'rho ** %s' % cor['COR-EPS'][1]))
        rec('  %-46s %s' % ('the corpus\'s remainder in the identity file',
                            'rho ** %s' % cor['COR-EPSGRID'][1]))
        rec('  %-46s %s' % ('the corpus\'s operator image, qeps_layer.py',
                            'rho ** %s' % cor['COR-QEPS'][1]))
        rec('  %-46s %s' % ('the corpus\'s TRACE side, b38_act10.py',
                            'the square root of %s' % cor['COR-TRACE'][1]))

        src_plus = not src['SRC-EPS'][1]
        cor_minus = str(cor['COR-EPS'][1]).startswith('-')
        grid_minus = str(cor['COR-EPSGRID'][1]).startswith('-')
        qcor_plus = not str(cor['COR-QEPS'][1]).startswith('-')
        different = src_plus and cor_minus

        rec('')
        rec(rule())
        rec('### (2a) THE VERDICT.')
        rec(rule())
        if different:
            rec('  ### ### ### **DIFFERENT.**')
            rec('  ### ### **THE FIRST DIFFERING CONSTITUENT, AT FULL PROMINENCE:**')
            rec('  ###')
            rec('  ###   ### **THE SCALING ACTION\'S NORMALIZATION EXPONENT.**')
            rec('  ###')
            rec('  ###   ### THE SOURCE, ITS OWN EQUATION (61), PAGE %s:' % src['SRC-THETA'][0])
            rec('  ###     ### **`(theta(lam) xi)(v) := lam^(-1/2) xi(lam^-1 v)`**')
            rec('  ###     ### -- so at the argument the remainder uses, `rho^(+1/2)`.')
            rec('  ###   ### THE CORPUS, ITS OWN HEADER:')
            rec('  ###     ### **`theta(a) f(x) = a^(1/2) f(x/a)`**')
            rec('  ###     ### -- so at the same argument, `rho^(-1/2)`.')
            rec('  ###')
            rec('  ###   ### AND NEITHER IS INFERRED FROM THE OTHER\'S PROSE. ### **BOTH SIDES ALSO')
            rec('  ###   ### WRITE THE UNFOLDED FORMULA OUT, AND THE UNFOLDED FORMULAE DISAGREE IN')
            rec('  ###   ### THE SAME PLACE:**')
            rec('  ###     source, Lemma 5.4 proof, page %s : `rho^(+1/2)`' % src['SRC-EPS'][0])
            rec('  ###       %s' % src['SRC-EPS'][2])
            rec('  ###     corpus, `qeps_layer.py` line %s : `rho ** %s`'
                % (cor['COR-EPS'][0], cor['COR-EPS'][1]))
            rec('  ###       %s' % cor['COR-EPS'][2])
            rec('  ###')
            rec('  ###   ### **THE TWO FUNCTIONS THEREFORE DIFFER BY A FACTOR OF `rho`, WHICH IS')
            rec('  ###   ### NOT A SCALAR.** ### The corpus\'s is the source\'s divided by `rho`.')
        else:
            rec('  ### THE EXTRACTION DID NOT PRODUCE THE DISAGREEMENT THE BANK DESCRIBES.')
            fails.append('the verdict does not follow from the extraction')

        rec('')
        rec(rule())
        rec('### (2b) THREE THINGS THAT MAKE THE VERDICT HARDER TO DOUBT.')
        rec(rule())
        rec('  ### **(i) THE SOURCE IS SELF-CONSISTENT AT THREE INDEPENDENT PLACES.** ### Its')
        rec('  ### definition (61) on page %s; its own worked unfolding of an inner product of'
            % src['SRC-THETA'][0])
        rec('  ### exactly this shape on page %s; and its Lemma 5.4 proof on page %s.'
            % (src['SRC-IP'][0], src['SRC-EPS'][0]))
        rec('  ### **A TRANSCRIPTION SLIP IN THE SOURCE WOULD HAVE TO HAVE HAPPENED THREE TIMES,')
        rec('  ### ### THE SAME WAY.**')
        rec('  ### **(ii) THE CORPUS DISAGREES WITH ITSELF, IN THE SAME TWO FILES.**')
        rec('  ###   its operator image carries `rho ** %s`, which AGREES with the source : %s'
            % (cor['COR-QEPS'][1], qcor_plus))
        rec('  ###   its remainder carries `rho ** %s`, which does not : %s'
            % (cor['COR-EPS'][1], cor_minus))
        rec('  ###   and inside `b38_act10.py`, the identity\'s TRACE side applies the square root')
        rec('  ###   of the scaling -- the source\'s convention -- while its REMAINDER side applies')
        rec('  ###   `rho ** %s`. ### **ONE IDENTITY, TWO CONVENTIONS, ONE FILE : %s**'
            % (cor['COR-EPSGRID'][1], grid_minus))
        rec('  ### **(iii) THE CORPUS\'S STATED REASON DOES NOT REACH THE CONCLUSION IT DRAWS.**')
        rec('  ###   Its header says the convention is `forced by the supplied support law`, and')
        rec('  ###   the support law it cites is that the scaled auxiliary vector is nonzero')
        rec('  ###   exactly when `u >= 1/rho`. ### **BUT THAT CONDITION IS IDENTICAL UNDER BOTH')
        rec('  ###   ### CONVENTIONS: A SUPPORT CONDITION FIXES A DOMAIN, NOT AN AMPLITUDE.** ###')
        rec('  ###   The support law is SILENT on the exponent, so it cannot have forced it.')

        rec('')
        rec(rule())
        rec('### (2c) WHY THIS SURVIVED -- DERIVED, NOT GUESSED.')
        rec(rule())
        rec('  ### The corpus\'s ONE cross-check against the source at this point is the one-sided')
        rec('  ### derivative at the identity, which its header derives and the source\'s Lemma 5.4')
        rec('  ### states; the two agree. ### **BUT THAT CHECK CANNOT SEE THE FACTOR, AND')
        rec('  ### ### PROVABLY SO.**')
        rec('  ###   Write the common integral as `F(rho)`, so that the corpus\'s function is')
        rec('  ###   `rho^(-1/2) F(rho)` and the source\'s is `rho^(+1/2) F(rho)`.')
        rec('  ###   The interval of integration is empty at the identity, so `F(1) = 0`.')
        rec('  ###   The derivative of `rho^s F(rho)` at the identity is `s F(1) + F\'(1)`,')
        rec('  ###   and with `F(1) = 0` that is `F\'(1)` ### **FOR EVERY `s` WHATEVER.**')
        rec('  ### ### **SO A CROSS-CHECK TAKEN AT A ZERO OF THE FUNCTION CANNOT SEE A')
        rec('  ### ### MULTIPLICATIVE FACTOR THAT IS FINITE AND NONZERO THERE.** ### That is the')
        rec('  ### whole of why a corpus that checked itself against the source found agreement.')

        rec('')
        rec(rule())
        rec('### (2d) THE ARCHIMEDEAN SIGN CONVENTION, CHECKED AGAINST THE BANKED ATLAS')
        rec('### RATHER THAN ASSUMED -- AS THE ORDER REQUIRES.')
        rec(rule())
        rec('  ### The corpus\'s archimedean term comes from `carto_atlas.py`, whose own header')
        rec('  ### records the explicit formula it uses and then says, of the sign:')
        rec('  ###   ### **`[sign fixed BY the E2 calibration]`**')
        rec('  ### and, two lines above:')
        rec('  ###   ### **`DISCLAIMED REGISTER: a computation maps and cannot prove. No sign')
        rec('  ###   ### claim is made.`**')
        rec('  ### ### **SO THE CORPUS HAS NO INDEPENDENTLY DERIVED ARCHIMEDEAN SIGN TO CHECK')
        rec('  ### ### AGAINST: ### ITS SIGN WAS FITTED, BY ITS OWN DECLARATION.** ### The order')
        rec('  ### said to check rather than assume, and what the check FINDS is that the thing to')
        rec('  ### be checked against is itself a calibration.')
        rec('  ### ### **AND THAT IS NOT A COMPLAINT ABOUT THE ATLAS** -- the atlas disclaims')
        rec('  ### exactly this and always has. ### **IT IS THE REASON A FACTOR IN A NEIGHBOURING')
        rec('  ### ### TERM WOULD NOT HAVE ANNOUNCED ITSELF THROUGH THAT CHANNEL EITHER.**')

        rec('')
        rec(rule())
        rec('### (2e) WHAT THIS ACT DOES **NOT** CONCLUDE.')
        rec(rule())
        rec('  ### **IT DOES NOT CONCLUDE THAT ANY BANKED NUMBER IS WRONG.** ### It compared two')
        rec('  ### written definitions and computed nothing. ### Every banked measurement stands')
        rec('  ### exactly where its own act left it, at its own grade.')
        rec('  ### **IT DOES NOT CONCLUDE THAT THE CORPUS MEANT THE SOURCE\'S FUNCTION AND MISSED.**')
        rec('  ### A corpus may define its own object. ### **WHAT IT MAY NOT DO IS CALL THAT OBJECT')
        rec('  ### ### THE SOURCE\'S, AND THE HEADER DOES.** ### Which of those two happened is not')
        rec('  ### decided here, because deciding it needs a computation this act may not run.')
        rec('  ### **AND IT DOES NOT SETTLE THE EQUATION NUMBERS.** ### The corpus cites `their')
        rec('  ### (85)` and `eq (100)` where the pinned artefact has (84) and (99); its header')
        rec('  ### says `arXiv-v1 / Selecta numbering`, and a uniform offset of one between two')
        rec('  ### editions is the obvious reading. ### **THE SELECTA EDITION IS NOT PINNED BY THIS')
        rec('  ### ### CORPUS, SO THIS ACT CANNOT CHECK IT AND DOES NOT.** ### The offset is')
        rec('  ### UNIFORM across both citations, which is consistent with an edition shift and')
        rec('  ### not with a mis-citation, and that is as far as the evidence goes.')

        rec('')
        rec(rule())
        rec('### (2f) THE WORK-ORDER THIS RAISES, TYPED AND NOT RUN.')
        rec(rule())
        rec('  ### ### **`W-ORD-REMAINDER-EXPONENT`** -- FILED HERE, OPEN.')
        rec('  ###   ### **WHAT IT ASKS:** ### whether the corpus\'s remainder should carry the')
        rec('  ###     source\'s exponent, and what changes in the corpus\'s identity if it does.')
        rec('  ###   ### **THE EXACT CHECK, NAMED SO THE NEXT ACT DOES NOT HAVE TO INVENT IT:**')
        rec('  ###     re-run the corpus\'s own identity with the remainder\'s exponent flipped and')
        rec('  ###     nothing else touched, and compare the residue against the banked one. ###')
        rec('  ###     **THAT IS A COMPUTATION, AND THIS ACT MAY NOT RUN IT.**')
        rec('  ###   ### **WHAT IT MUST NOT DO:** ### edit any banked file, move any grade, or')
        rec('  ###     re-verdict any act before that comparison exists.')
        rec('  ###   ### **AND IT INHERITS `W-ORD-ARCH-NORM-READING`**, which b301 filed and which')
        rec('  ###     is still live: the normalization reading at the archimedean place is the')
        rec('  ###     open question this act has now given a second, sharper instance of.')

    # ------------------------------------------------------------------ COMPONENT 3
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE ENTAILMENT. ### **IT DOES NOT RUN.**')
    rec('=' * 100)
    rec('  ### The order runs Component 3 ONLY on SAME, and states the alternative in its own')
    rec('  ### words: ### **on DIFFERENT or UNDECIDED, the corpus\'s remainder is its own object')
    rec('  ### and the entailment does not run.**')
    rec('  ### ### **THE VERDICT IS DIFFERENT, SO:**')
    rec('  ###   ### the corpus\'s finite-instance identity is NOT restated as the source\'s')
    rec('  ###     Theorem 4.7 here;')
    rec('  ###   ### b310\'s finite-side result is NOT attached to it, and stays quarantined at its')
    rec('  ###     own scope, where b310 and b311 left it;')
    rec('  ###   ### the open clause\'s finite-instance form is NOT written;')
    rec('  ###   ### and the weight-and-eigenvalue juxtaposition is NOT re-examined -- it was to be')
    rec('  ###     promoted to nothing even on SAME, and on DIFFERENT it is not even asked.')
    rec('  ### ### **AND NO CLAIM IS MADE ABOUT THE IMBALANCE\'S CAUSE.** ### The order permits one')
    rec('  ### only if the identification lands. ### **IT DID NOT LAND.** ### The temptation is')
    rec('  ### obvious and is refused by name: a factor found in a term of the identity is NOT')
    rec('  ### thereby the explanation of anything the identity does, and saying otherwise would')
    rec('  ### be this act computing a consequence it has no instrument for.')

    rec('')
    rec('=' * 100)
    rec('### THE VERDICT ON THE NAVIGATOR\'S REGISTERED EXPECTATION.')
    rec('=' * 100)
    rec('  ### The expectation, quoted from the order: ### **SAME FUNCTION up to the normalization')
    rec('  ### the corpus records by a factor; refutable by a differing constituent.**')
    rec('  ### ### ### **REFUTED.**')
    rec('  ###   ### **AND REFUTED IN THE REGION ITS OWN HEDGE POINTED AT**, which is the honest')
    rec('  ###     thing to say for it: it named the normalization as the risk and named the')
    rec('  ###     refutation condition correctly.')
    rec('  ###   ### **BUT THE HEDGE DOES NOT COVER THE FINDING.** ### *Up to a factor* is a')
    rec('  ###     scalar\'s licence. ### **THE FACTOR HERE IS `rho`, AND A FUNCTION OF THE')
    rec('  ###     ### VARIABLE IS NOT A SCALAR.** ### Two functions differing by `rho` agree at')
    rec('  ###     exactly one point, and that point is the identity, where both are zero.')
    rec('  ### ### **THIS IS THE THIRD ACT RUNNING WHOSE SEALED PREDICTION FAILED AT A')
    rec('  ### ### NORMALIZATION**, after b309\'s and b310\'s. ### The order put the normalization')
    rec('  ### first for that reason, and the reason held.')

    rec('')
    rec('  ### CHECKS FAILING : %d' % len(fails))
    for f in fails:
        rec('    ### FAILED: %s' % f)
    rec('=' * 100)
    return (0 if not fails else 1), out


if __name__ == '__main__':
    code, lines = main()
    io.open(os.path.join(D, 'b312_components_run.txt'), 'w', encoding='utf-8',
            newline='\n').write('\n'.join(lines) + '\n')
    sys.exit(code)
