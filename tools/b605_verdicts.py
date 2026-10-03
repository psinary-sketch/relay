# -*- coding: utf-8 -*-
"""b605_verdicts.py -- THE VERDICT COLUMN RE-READ, UNDER (R215)(2)(i)-(ii) AND (4). ### DATA ONLY.

### Read by tools/b605_record.py (the verdict bank, the edition, the scores) and by tools/b605_checks.py. The rows are b604's
### (tools/b604_rows.py, imported, never copied); this file carries only the v0.3 verdict of each row: its KIND (what the
### conclusion is), its new verdict (FACE, BRIGHT, DARK or NOT A ROUTE), the deciding test where one decides, and the reason in
### one line. Every reading here is the seat's, declared on the face and strikeable.
###
### (R215)(2)(i): a row whose conclusion is not a candidate argument toward h2_sign, simplicity or a GRH_chi target reads NOT A
### ROUTE, its test column "—"; test 1 applies only to a statistic or average over the zeros offered as a placement argument.
### (R215)(2)(ii): the compiled iff-faces of the located clause are one object and read FACE under the clause's one verdict;
### the Li ladder's bright row is its arithmetic end, the Keiper face, and liCoeff_one_pos a FINITE rung of it, bright by test 4.
"""

# ### the located clause's group: the clause, its one verdict and the test that decided it, named once
CLAUSE = dict(
    name='the located clause',
    what='Weil positivity on classK (`h2_sign`), and in the schema `h2_sign_cfg` against its target, at ζ, at χ and over the family',
    verdict='BRIGHT',
    test=2,
    why='decided at `h2_sign_iff_rh` by test 2: the clause carries the explicit formula’s prime sum (`EF_lit_zetaZeroConfig` at ζ, '
        '`EF_lit_chi_holds` at χ), so a route through it fails at the Epstein configuration; test 1 n/a (not a statistic), test 3 '
        'read at the χ and family forms (the conductor once per summand), test 4 UNIVERSAL, test 5 a declaration at its pin',
)

# ### the kinds a conclusion can be; the ruling's four ("a compiled identity, a census, a method theorem ... a face") are the
# ### first four, and N1 / H39a's second clause read them
KINDS = {
    'face': 'an iff-face of the located clause',
    'identity': 'a compiled identity',
    'census': 'a census or count',
    'method': 'a method theorem or derivation',
    'instrument': 'a test’s own instrument',
    'construction': 'a construction',
    'target': 'a target stated',
    'reading': 'a reading',
    'record': 'a statement about the corpus',
    'status': 'a status: an open, an absence, a route to a definition',
    'bench': 'a bench measurement',
    'fence': 'a fence',
    'verdict': 'a findings-pass decision',
    'statistic': 'a statistic or average over the zeros offered as a placement argument',
    'route': 'a candidate route toward a target',
    'ladder': 'the Li ladder’s arithmetic end',
    'rung': 'a FINITE rung of the Li ladder',
}
RULED_FOUR = ('identity', 'census', 'method', 'face')

FACE, BRIGHT, DARK, NAR = 'FACE', 'BRIGHT', 'DARK', 'NOT A ROUTE'


def V(kind, verdict, test, why):
    return dict(kind=kind, verdict=verdict, test=test, why=why)


def F_(why):
    return V('face', FACE, None, 'an iff-face of the located clause: ' + why)


def N_(kind, why):
    return V(kind, NAR, None, why)


NEW = {
    # ### Simplicity / RH cascade -- the pages' conclusions
    'RH-01': F_('the clause at ζ, both directions compiled'),
    'RH-02': F_('the deposit’s Route 3 clause, the clause restated'),
    'RH-03': N_('identity', 'a compiled identity: the explicit formula at ζ’s zero configuration, true wherever the zeros lie'),
    'RH-04': F_('the clause as its finite-support rungs at every support length (the forall_upto pair)'),
    'RH-05': F_('the finite-support rungs at every length as RH (the forall_upto pair)'),
    'RH-06': N_('identity', 'a compiled identity: the Li–Weil bridge from the arithmetic limits to λ_n'),
    'RH-07': F_('Li’s criterion, which holds of any function with the Hadamard shape and says nothing by itself of the prime side'),
    'RH-08': F_('Li’s criterion at the Bombieri–Lagarias arithmetic limits'),
    'RH-09': F_('the register-4 form of Li’s criterion'),
    'RH-10': F_('the Taylor form of Li’s criterion'),
    'RH-11': V('ladder', BRIGHT, 4, 'the Li ladder’s arithmetic end, the Keiper face: each λ_n computed from ζ’s Stieltjes side, rungs whose '
                                   'limit is UNIVERSAL; test 2 cleared (at the Epstein configuration the same computation reads its own '
                                   'constants and a rung goes negative), tests 1 and 3 n/a, test 5 a declaration at its pin'),
    'RH-12': N_('identity', 'a compiled identity: λ₁’s closed form in γ and log 4π, the value the rung of RH-13 reads'),
    'RH-13': V('rung', BRIGHT, 4, 'a FINITE rung of the Li ladder, its sign compiled with no premise from ζ’s Stieltjes side; test 2 read at '
                                  'the ladder’s arithmetic end, tests 1 and 3 n/a, test 5 a declaration at its pin'),
    'RH-14': N_('method', 'bounds on finitely many Stieltjes and ζ values from named premises: the rungs’ inputs, no rung’s sign concluded'),
    'RH-15': N_('target', 'the simplicity target itself unfolded (every zero of multiplicity one), not an argument toward it'),
    'RH-16': V('statistic', DARK, 1, 'a proportion over a window offered toward simplicity: an average over the zeros, not each zero'),
    'RH-17': N_('method', 'a method theorem of the schema: positivity conjunctive over a sum of two configurations, true of every configuration'),
    'RH-18': N_('method', 'a method theorem of the schema: doubling a configuration doubles each multiplicity and leaves positivity unchanged'),
    'RH-19': N_('method', 'a method theorem: a non-implication with a counter-model in the schema, closing a route toward simplicity rather than offering one'),
    'RH-20': N_('identity', 'a compiled identity: the explicit formula at every primitive χ ≠ 1, true wherever the zeros lie'),
    'RH-21': F_('the clause at χ, both directions compiled'),
    'RH-22': F_('the schema’s form, every configuration’s positivity against its target, of which the ζ and χ faces are instances'),
    'RH-23': N_('method', 'a method theorem of the schema: positivity conjunctive over a finite sum, by induction'),
    'RH-24': F_('the clause over the family mod q: one summed configuration against GRH_chi for every member'),
    'RH-25': N_('instrument', 'test 2’s own instrument: a method theorem generic over configurations, meeting every off-line point with a negative window'),
    'RH-26': N_('instrument', 'the detector’s corollary, generic over configurations: test 2’s instrument, not a route'),
    'RH-27': N_('construction', 'a construction: a window in classK with its transform on named obligations; no zero is named'),
    'RH-28': N_('reading', 'a reading of the faces: how multiplicity is weighted; it argues toward no target'),
    'RH-29': N_('reading', 'a reading of the method theorems: positivity conjunctive over sums and not implying simplicity; it argues toward no target'),
    'RH-30': V('route', DARK, 3, 'a candidate route toward GRH_chi for every character mod q through the Dedekind product: an imprimitive '
                                 'character enters at its level, not its conductor (EulerFactorPremise), and the trivial character with ζ’s pole term'),
    # ### Simplicity / RH cascade -- the current version's own conclusions
    'RH-31': N_('status', 'a statement of what a file states and does not establish; the identity at complete roster is the clause, not an argument toward it'),
    'RH-32': N_('bench', 'a computed check at finite instance, a recorded measurement'),
    'RH-33': N_('record', 'a statement of the route by which a term reaches the corpus, at the grade barrier'),
    'RH-34': N_('method', 'a derivation about the identity’s apportionment, exact algebra; no target is argued'),
    'RH-35': N_('method', 'a derivation about the apportionment’s share at a cell; no target is argued'),
    'RH-36': N_('record', 'a finding about the owners’ requirements; no target is argued'),
    'RH-37': N_('method', 'a derivation closing a read-route for a term’s definition; no target is argued'),
    'RH-38': N_('reading', 'a reading: a term’s definition left open; no target is argued'),
    'RH-39': V('statistic', DARK, 1, 'the density lane’s collapse to one density: a scale-average offered toward the identity, not each zero’s real part'),
    'RH-40': V('statistic', DARK, 1, 'the density’s kernel and Ψ: a statistic offered toward the balanced window, not each zero’s real part'),
    'RH-41': N_('record', 'a scope location: the lane’s chain conditional on one member'),
    'RH-42': N_('record', 'a refusal at the carrier’s edge: a licensing question'),
    'RH-43': V('statistic', DARK, 1, 'the density route’s open remainder, priced at control of Ψ’s profile: a statistic offered toward the '
                                     'identity, not each zero’s real part'),
    'RH-44': N_('status', 'an open of type: the licensing question at the carrier’s edge'),
    'RH-45': N_('status', 'a route toward a definitional choice, the member of the family, not toward a target'),
    'RH-46': N_('status', 'a route toward defining a split, not toward a target'),
    'RH-47': N_('fence', 'a fence: the record withholding weight from a location and a crossing'),
    'RH-48': N_('record', 'a reach note about a bench parameter; it re-grades nothing'),
    'RH-49': N_('record', 'a disclaimed bearing: the record offers the lane as no argument'),
    'RH-50': N_('record', 'a read of what the finite-place result does not establish'),
    'RH-51': N_('record', 'a read of the archimedean place’s space; no value is derived'),
    'RH-52': N_('census', 'a census of one name’s objects'),
    'RH-53': N_('bench', 'a bench reading of eigenfunction signs at the archimedean place'),
    'RH-54': N_('status', 'an absence: a formalization not yet written'),
    'RH-55': N_('census', 'an enumeration of witness sites, with a channel’s closed form'),
    'RH-56': N_('bench', 'a bench record of an instrument’s residual'),
    'RH-57': N_('bench', 'a bench record of an instrument and its control, offered as no argument'),
    # ### Foundations
    'FD-01': N_('instrument', 'test 2’s own instrument: the compiled witness on the control configuration'),
    'FD-02': N_('identity', 'a compiled identity: the explicit formula at the Epstein configuration on a window'),
    'FD-03': N_('record', 'a statement about the corpus’s barrier keystone'),
    # ### Methodology
    'MT-01': N_('census', 'a census of the Core terminals’ prints'),
    'MT-02': N_('record', 'a statement of which files are interfaces'),
    'MT-03': N_('record', 'a statement of scope: what is checked how'),
    'MT-04': N_('method', 'a decided property of the built object; no target is argued'),
    'MT-05': N_('record', 'a statement of what blocks what'),
    'MT-06': N_('verdict', 'a findings-pass decision of independence'),
    'MT-07': N_('record', 'a limit of the document'),
    'MT-08': N_('record', 'the findings pass’s own record'),
    'MT-09': N_('census', 'a fold, counted'),
    'MT-10': N_('record', 'a divergence between two ledgers, printed for the author'),
    'MT-11': N_('record', 'reads of the assembly and its values; no target is argued'),
    'MT-12': N_('status', 'a live debt: nothing constructed'),
    'MT-13': N_('record', 'a statement of what blocks what'),
    'MT-14': N_('record', 'a fold refresh about the folds'),
    'MT-15': N_('record', 'an arc’s one statement about the record’s acts'),
    'MT-16': N_('record', 'an arc’s one statement about the record’s measurements'),
    'MT-17': N_('record', 'an arc’s one statement about the record’s classifications'),
    'MT-18': N_('record', 'an arc’s one statement about the grading discipline'),
    'MT-19': N_('record', 'an arc’s one statement about an instrument and the deposit'),
    'MT-20': N_('record', 'an arc’s one statement about readings of other hands'),
    'MT-21': N_('record', 'an arc’s one statement about the bookkeeping'),
    'MT-22': N_('reading', 'a reading of the editions’ corrections'),
    # ### Cubit / Trivium and Matter / cosmology
    'CT-01': N_('verdict', 'a findings-pass decision of independence, a Trivium fact'),
    'MC-01': N_('verdict', 'a findings-pass decision of independence, a cosmology row'),
}

# ### the FACE group, in row order (the clause's one verdict above it)
FACE_GROUP = [k for k, v in NEW.items() if v['verdict'] == FACE]

# ### the "forall_upto window" of H39c, read at the kernel: DetectionRegion.lean at v0.21 carries `h2_sign_upto` as a def and the
# ### pair; no declaration fixes a single rung at a finite support length, so no row states one
UPTO_READ = ('SIDE-explicit-formula v0.21 SIDEExplicitFormula/DetectionRegion.lean :29 `def h2_sign_upto`, :47 `h2_sign_iff_forall_upto`, '
             ':52 `forall_upto_iff_rh`: the pair are FACES (UNIVERSAL); no declaration fixes one rung at a finite support length')
