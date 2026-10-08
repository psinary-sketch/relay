# -*- coding: utf-8 -*-
"""b639_worklist.py -- THE ACT'S DATA, UNDER (R249). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b639: LANE THREE, ACT SIXTY-SIX -- THE DEPOSIT ON THE (R110) ROUTE: THE 50 PREMISE HEADS CLASSED BY STATUS, THE DESCRIPTION IN THE
### READER'S ORDER, THE FILES WITH THEIR DIGESTS, A DRAFT READ BACK FROM THE SERVICE, THE AUTHOR'S WORD, THEN PUBLICATION AND THE DOI
### RECORDED; THE ROSTER AT CENSUS v0.6 AND THE MIRROR REBUILT. Here: the pins before the act; the lists in force; the glossary; the census
### and the sieve; the kernels the status reads; the ledger lines; the record, its version and its title; the eleven files of v1.1.2 and the
### edition each is matched to; the bank's three; the mirror's name; the sealed tools; the next act.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
GS = 'D:/SIDE-global-section'
PRE_PP = 'dfb52fd'          # ### PLACE-papers main before the act (b638's record)
PRE_RELAY = '5c869cff'      # ### relay main before the act (b638's closing)
STEPZERO = 'b48f6be0'       # ### relay: b638's closing push-out bank, committed at step zero
ROSTER_COMMIT = '05532681'  # ### relay: the roster edit of (R249)(3), committed alone at step zero
DATE = '2026-10-07'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/47d34df0-9823-4c9f-9efb-d1daddb7dd61/scratchpad'
PLANTED_DIR = SP + '/b637_planted'   # ### b637's planted module, copied here whole (B637Planted.lean sha256 735629f5...)

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b638_nodes_zeta.txt', 'chi': 'b638_nodes_chi.txt'}         # ### the lists in force since b638 (b632's with the glossary mark)
PROBE = {'zeta': 'b635_probe_out_zeta.txt', 'chi': 'b635_probe_out_chi.txt'}  # ### the probes in force since b635 (its Pages answer)
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
GLOSSARY = 'data/glossary.txt'
GLOSSARY_MARK = '# glossary'

# ### the census, the sieve, the monograph
CEN6 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_6.md'
CEN5 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_5.md'
SIEVE6 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md'
MONO = 'day1/A_Place_to_Stand_v5_18.md'
CEN6_PREMISES_HEAD = '### The named premises the INTERFACES rows rest on, at v0.6'
CEN6_SUM_NEEDLE = '*50 heads carry rule-graded rows'

# ### (R249)(2): THE KERNELS THE STATUS READS -- each at the commit the terminal table read its rows at (relay data/terminal_table.json, the
# ### row's `head`), each a local clone at D:/<kernel>; Zeta23's own record (its AUDIT.md) at the clone relay data/anthropic-zeta23/formal-math
EF, EF_PIN = 'D:/SIDE-explicit-formula', '8c51431'
ZETA23_CLONE = 'D:/relay/data/anthropic-zeta23/formal-math'
ZETA23_AUDIT = 'zeta23/AUDIT.md'
STATUSES = ('DISCHARGED IN KERNEL', 'DISCHARGED ELSEWHERE', 'CITED', 'OPEN')
SALT_MARK = 'SaltCheck'          # ### a file whose path carries it is a salt check: its witnesses show non-vacuity and discharge nothing
TIER_MARKS = r'\bT0\b|\bT1-open\b|\bT2\b|\bT3\b|\bT4\b'   # ### a docstring carrying any of these beside T1-lit is not cited whole
RULING_OPEN = ('EpsteinPremises', 'WindowObligations', 'KeiperObligations', 'TrivialSummandPremise', 'EulerFactorPremise')
RULING_CITED = ('NymanBeurlingPremise', 'PlattTrudgianHeight')

# ### THE FIGURE PUT TO THE AUTHOR BEFORE THE SEAL (the prompt on the discharge reading and its answer: "20 discharged in kernel, 28 open,
# ### 2 cited"), from the scratchpad prototype before its declaration reader read comments out; the tool prints the heads that moved against it
PROTO_FIGURE = dict(figure='20 discharged in kernel / 28 open / 2 cited, rule rows 73 / 48 / 2', members={
    'Alternates': 'DISCHARGED IN KERNEL', 'AnalyticOnNhd': 'DISCHARGED IN KERNEL', 'BoundPremises': 'OPEN', 'ConservationHypothesis': 'OPEN',
    'Continuous': 'DISCHARGED IN KERNEL', 'Dealigned': 'OPEN', 'DealignedAt': 'OPEN', 'EpsteinPremises': 'OPEN', 'EqOn': 'DISCHARGED IN KERNEL',
    'EulerFactorPremise': 'OPEN', 'HCount': 'DISCHARGED IN KERNEL', 'HasCompactSupport': 'DISCHARGED IN KERNEL', 'HasDerivAt': 'DISCHARGED IN KERNEL',
    'IdempotentAdd': 'OPEN', 'Integrable': 'DISCHARGED IN KERNEL', 'IsEvenFn': 'OPEN', 'IsExpansion': 'OPEN', 'IsOpen': 'OPEN', 'IsRoot': 'OPEN',
    'IsSign': 'OPEN', 'IsSignedCompletion': 'OPEN', 'IsTrivialPoint': 'DISCHARGED IN KERNEL', 'KeiperObligations': 'OPEN', 'Monotone': 'DISCHARGED IN KERNEL',
    'NontrivialZeroExistsInStrip': 'OPEN', 'NotDiv': 'DISCHARGED IN KERNEL', 'NymanBeurlingPremise': 'CITED', 'PWSetup': 'DISCHARGED IN KERNEL',
    'PerClassExcludes': 'OPEN', 'PlattTrudgianHeight': 'CITED', 'Prime': 'OPEN', 'Proper': 'OPEN', 'Register4_channelInequality': 'OPEN',
    'Register4_positivity': 'OPEN', 'SatisfiesCWeil': 'OPEN', 'SelfDualFE': 'OPEN', 'StepsI': 'DISCHARGED IN KERNEL', 'StepsMI': 'DISCHARGED IN KERNEL',
    'StrictMono': 'OPEN', 'StructuralExhaustiveness': 'DISCHARGED IN KERNEL', 'SymPairBound': 'DISCHARGED IN KERNEL', 'Tendsto': 'DISCHARGED IN KERNEL',
    'TrivialSummandPremise': 'OPEN', 'WindowObligations': 'OPEN', 'ZeroActingPairing': 'DISCHARGED IN KERNEL', 'ZetaSeam': 'DISCHARGED IN KERNEL',
    'farSmall': 'OPEN', 'identity': 'OPEN', 'is_xi_zero': 'OPEN', 'zeroSideNeg': 'DISCHARGED IN KERNEL'})

# ### THE SEAT'S HAND-READ OF EVERY DISCHARGE, BESIDE THE COMPUTED STATUS (the author's answer: residual witnesses outside the SaltCheck files
# ### read by hand in a column beside), for the author's strike; three kinds: AT A USE, a theorem builds the hypothesis it hands the lemma;
# ### INSTANCES, a general predicate of Mathlib's whose instances the kernel constructs; WITNESS ONLY, the one construction a concrete object
HANDREAD = {
    'PWSetup': 'AT A USE -- built by have in the four converse proofs and handed to the lemmas resting on it',
    'EqOn': 'AT A USE -- built by have inside the Mellin proof of C7OrderBounds',
    'ZetaSeam': 'AT A USE -- zetaSeam closes the seam unconditionally (Zeta23/Statement/SeamClosed.lean)',
    'zeroSideNeg': 'AT A USE -- zeroSideNeg_holds, unconditional',
    'SymPairBound': 'AT A USE -- symPair_bound n, unconditional, for every n',
    'StructuralExhaustiveness': 'AT A USE -- structural_exhaustiveness_proved (Bridge/TheBridgeComplete.lean), unconditional in the kernel; '
                                'its reach is the kernel`s own mechanism type (README :16, ERRATA E-2026-09-14-1)',
    'Monotone': 'AT A USE -- hullMono, monotone hull for every family, unconditional',
    'AnalyticOnNhd': 'INSTANCES -- a general predicate of Mathlib`s; the kernel constructs instances, not checked here row by row',
    'Continuous': 'INSTANCES -- a general predicate of Mathlib`s; the kernel constructs instances, not checked here row by row',
    'HasCompactSupport': 'INSTANCES -- a general predicate of Mathlib`s; the kernel constructs instances, not checked here row by row',
    'HasDerivAt': 'INSTANCES -- a general predicate of Mathlib`s; the kernel constructs instances, not checked here row by row',
    'Integrable': 'INSTANCES -- a general predicate of Mathlib`s; the kernel constructs instances, not checked here row by row',
    'Tendsto': 'INSTANCES -- a general predicate of Mathlib`s; the kernel constructs instances, not checked here row by row',
    'Alternates': 'WITNESS ONLY -- flip_alternates and transfer_nonvacuous, the one concrete sequence; the rows take it of any sequence',
    'HCount': 'WITNESS ONLY -- emptyZ_count, the empty configuration',
    'IsSign': 'WITNESS ONLY -- flip_is_sign, the one concrete sequence',
    'SatisfiesCWeil': 'WITNESS ONLY -- cweil_inhabited, the aggregation built to satisfy it',
    'StepsI': 'WITNESS ONLY -- ipow_stepsI, the powers of i',
    'StepsMI': 'WITNESS ONLY -- measured_stepsMI, the measured ladder',
}

# ### THE SEAT'S HAND-READ OF THE WORK-ORDER LINES THE STATUS PRINTS FOR AN OPEN HEAD (a W-ORD token and the head's name on one line), for the
# ### author's strike: FOR IT, the work-order takes the head up; NAMES IT, the line names the head for another purpose; THE WORD, the match is
# ### the English word and not the predicate
WO_HANDREAD = {
    'ConservationHypothesis': ('FOR IT', 'W-ORD-H2-BRIDGE (:10257): SIDE-kernel`s ConservationHypothesis and h2_sign, the bridge between them'),
    'farSmall': ('FOR IT', 'W-ORD-WEIL-CONVERSE (:10608): the converse`s table, farSmall its named hypothesis'),
    'KeiperObligations': ('NAMES IT', 'W-ORD-QUANTIFIER-COLUMN (:12887): its quantifier shape as a premise bundle, not its discharge'),
    'WindowObligations': ('NAMES IT', 'W-ORD-QUANTIFIER-COLUMN (:12887): its quantifier shape as a premise bundle, not its discharge'),
    'identity': ('THE WORD', 'the lines match the English word ("it is an identity", :4961), not the predicate identity'),
}

# ### the ledger lines the act reads and addresses
B638_ENTRY = 7861           # ### FINDINGS: b638's entry
B638_WEIGHT_PRIOR = 7859    # ### FINDINGS: b637 at its weight (b638's line)
B638_RECORD = 13369         # ### OPEN_TRAILS: b638's trail record
READER_CLAUSE = 13365       # ### OPEN_TRAILS: the reader's clause, standing (b638)
G036_NOTE = 13367           # ### OPEN_TRAILS: the G036 note (b638)
R110 = 9514                 # ### OPEN_TRAILS: (R110) ratified -- the route, the token in the environment, every write fetched back
R110_GUARD = 9520           # ### OPEN_TRAILS: STEP (G), the guard's token limb
FORM = 11864                # ### OPEN_TRAILS: the form of an edition
PRECEDENCE = 12228          # ### OPEN_TRAILS: the precedence order
AUTHORITY = 12354           # ### OPEN_TRAILS: the authority order
BUILD_CLAUSE = 12356        # ### OPEN_TRAILS: the build clause
N5_SCORER = 12799           # ### OPEN_TRAILS: the N5 scorer, standing
MANIFEST_ROOT = 12929       # ### OPEN_TRAILS: the act root in MANIFEST, standing
BUILD_ROUTE = 13167         # ### OPEN_TRAILS: the build route under the hold
ACT_ROOT_WO = 12210         # ### OPEN_TRAILS: W-ORD-ACT-ROOT, the deposit description's carrying of the root a separate (R110) item
FERRY_LINES = (11864, 12228, 12354, 12356, 12799, 13167, 13365, 13366, 13367, 13368, 13369)
README_SUPPORT = (106, 107, 127, 129)   # ### README: the ceiling sentence and the supportable paragraphs for v0.17-v0.21 and v0.22-v0.25
README_NOTE = 158           # ### README: the deposit note (`day1/`)
REGISTRY_ROW = 83           # ### REGISTRY: the deposit row d1-1
GLOSSARY_DEPOSIT = 'the deposit'
GLOSSARY_LOCATED = 'the located clause'

# ### (R249)(4): THE RECORD -- the monograph's, as README's deposit note and REGISTRY's d1-1 row name it; the version string and the title as
# ### the author answered before the seal (data/b639_author_answers.txt)
RECORD = '21539167'
CONCEPT = '19675355'
RECORD_VERSION = 'v1.1.2'
VERSION = 'v1.2.0'
TITLE = 'A Place To Stand: the SIDE reduction of the Riemann Hypothesis to a single located clause'
API = 'https://zenodo.org/api'
TOKVAR = 'ZENODO' + '_TOKEN'

# ### v1.1.2's eleven files, each with the md5 the record states (relay data/b574_zenodo_fetch.txt) and the document the author's answers
# ### match it to: a document whose bytes changed after the deposit has a newer edition whatever its label says; the diagrams byte-identical
INHERITED = [
    ('A_Place_to_Stand.md', 'e90e2d06d5cadc059c62c29a849e9f8c', MONO),
    ('ERRATA.md', '8fa2ea2839199583d24119680d31c23f', 'ERRATA.md'),
    ('Exhaustive_Enumeration.md', '218d290942dbfb7d150088d7c6dfe811', 'day1/Exhaustive_Enumeration.md'),
    ('FORMATION_ARCHITECTURE.html', '5d8cf664416d4311c34a5b2c95a13dc9', 'day1/diagrams/FORMATION_ARCHITECTURE.html'),
    ('ONE_PAGE_PROOF.md', '0c727f16277beb41b62ec29254d0aebc', 'day1/ONE_PAGE_PROOF.md'),
    ('PAPER_DEPENDENCIES.svg', '14ad53eabbc775280ac1808639498346', 'day1/diagrams/PAPER_DEPENDENCIES.svg'),
    ('Seven_Mechanism_Classes.md', '6caa6e80300584c037cf48882941ad00', 'day1/Seven_Mechanism_Classes.md'),
    ('Silence_of_Foundations.md', 'c6e1593165449e004e0791239cac149f', 'day1/Silence_of_Foundations.md'),
    ('Spectral_Inertness.md', 'db5ab3d3d231cb83a243338c4aa35f76', 'day1/Spectral_Inertness.md'),
    ('Third_Identity_Element.md', 'ae918605afbd706faf54aa8474a30eb3', 'day1/Third_Identity_Element.md'),
    ('Which_Structure_Confines.md', '6b18d69bcf9e619d3b2fb22376ccc432', 'day1/Which_Structure_Confines.md'),
]
DEPOSITED_DIR = 'outputs/DEPOSITED-v1.1.2'   # ### PLACE-papers: the deposited bytes, -text (CP-5, b575)
BANK3 = [CEN6, SIEVE6]                       # ### the versioned keystones the deposit note lists; the mirror's zip is the third

# ### THE MIRROR -- built after the act's last PLACE-papers push and before the draft, by the unedited builder on the 74-file roster
ROSTER = 'tools/mirror_roster.json'
BUILDER = 'tools/mirror_build.ps1'
MIRROR_TAG = '2026-10-07-b639'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % MIRROR_TAG
MIRROR_PREV = 'D:/MY-DOwnloads/mirror-refresh-2026-10-07-b638.zip'   # ### b638's build, on the 73-file roster
ROSTER_FILES = 74

# ### THE SEALED TOOLS -- this act's own tools that take no edit by any means until the act closes (OPEN_TRAILS :13307)
SEALED = ('b639_worklist.py', 'b639_tests.py', 'b639_record.py', 'b639_checks.py', 'b639_closing.py', 'b639_reg_gate.py', 'b639_regspec.py')

NEXT_ROUTES = [('b640, on the author`s word: the census at v0.7 with (R249)(2)`s status column and its row count over both provenances, or the '
                'per-cluster fact-item editions of Phase 1.2 under the reader`s clause', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def show_bytes(path, rev='HEAD', repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
