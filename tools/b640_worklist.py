# -*- coding: utf-8 -*-
"""b640_worklist.py -- THE ACT'S DATA, UNDER (R250). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b640: LANE THREE, ACT SIXTY-SEVEN -- THE PREMISE STATUS SPLIT TO FIVE AND THE OPEN PREMISES GIVEN WORK-ORDERS; THE DEPOSIT
### DESCRIPTION'S ASSUMPTION SECTION RECOMPOSED; A SECOND READER FOR LEGIBILITY; THE DRAFT 23228113 UPDATED AND HELD AT THE SAME PROMPT.
### Here: the pins before the act; the lists in force; the five statuses and their order as the author answered before the seal; the
### heads already carried by a work-order; the reader's staging off drive D; the draft; the mirror's name; the sealed tools; the next act.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
GS = 'D:/SIDE-global-section'
PRE_PP = '0fede2d'          # ### PLACE-papers main before the act (b639's correction beneath its record)
PRE_RELAY = 'be1a4105'      # ### relay main before the act (b639's closing)
STEPZERO = '6e33ccdc'       # ### relay: b639's closing push-out bank, committed at step zero
DATE = '2026-10-08'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/47d34df0-9823-4c9f-9efb-d1daddb7dd61/scratchpad'
PLANTED_DIR = SP + '/b637_planted'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b638_nodes_zeta.txt', 'chi': 'b638_nodes_chi.txt'}
PROBE = {'zeta': 'b635_probe_out_zeta.txt', 'chi': 'b635_probe_out_chi.txt'}
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
GLOSSARY = 'data/glossary.txt'
CEN6 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_6.md'
CEN5 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_5.md'
SIEVE6 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md'
MONO = 'day1/A_Place_to_Stand_v5_18.md'
EF, EF_PIN = 'D:/SIDE-explicit-formula', '8c51431'

# ### (R250)(3) AS THE AUTHOR ANSWERED BEFORE THE SEAL (data/b640_author_answers.txt): the five statuses, each head taking the first it meets in
# ### this order -- DOMAIN, a predicate of Mathlib's (the head's declaration outside every kernel) that every row resting on it applies to a
# ### variable the row's statement quantifies; DISCHARGED, a construction outside the SaltCheck files consumed by a proof that is not a witness's
# ### (an inline have / let / show inside a proof, or a declaration concluding the head with no Prop hypothesis whose name another declaration's
# ### proof uses, outside SaltCheck and AxiomCheck files, the consumer not itself a witness); CITED, every field T1-lit; WITNESSED, constructions
# ### outside the salt checks and none consumed (standalone witnesses); OPEN, otherwise -- a head constructed inside salt checks alone among them.
STATUSES5 = ('DOMAIN', 'DISCHARGED', 'CITED', 'WITNESSED', 'OPEN')
SALT_MARK = 'SaltCheck'
WITNESS_NAME = r'nonvacuous|inhabited|toy|empty|witness|example'
FIGURE5 = dict(OPEN=25, CITED=2, DISCHARGED=9, WITNESSED=2, DOMAIN=12)   # ### the figure put to the author with the answer, the prototype's
MATHLIB_FOUR = ('IsOpen', 'IsRoot', 'Prime', 'StrictMono')

# ### (R250)(4): THE HEADS ALREADY CARRIED BY A WORK-ORDER, cross-referenced and not duplicated, each with its OPEN_TRAILS line
CARRIED_WO = {'ConservationHypothesis': ('W-ORD-H2-BRIDGE', 10257), 'farSmall': ('W-ORD-WEIL-CONVERSE', 10608),
              'KeiperObligations': ('W-ORD-QUANTIFIER-COLUMN', 12887), 'WindowObligations': ('W-ORD-QUANTIFIER-COLUMN', 12887)}
EPSTEIN_FIELDS = ('count', 'ef')   # ### EpsteinPremises' work-order: its count field the open part (T3), its ef field cited (T1-lit)

# ### the ledger lines the act reads and addresses
B639_ENTRY = 7885
B639_WEIGHT_PRIOR = 7883
B639_RECORD = 13399
B639_CORRECTION = 13427
METHOD_ITEM = 13395
PATCH_WO = 13397
CRITERION = 12955           # ### OPEN_TRAILS: the domain-condition criterion, (R235)(2)
READER_FORM = 12839
READER_FORM_ROW = 12863
READER_ISOLATION = 13223
FERRY_LINES = (11864, 12228, 12354, 12356, 12799, 13167, 13395, 13397, 13399, 13427, 12839, 12863, 13223, 12955, 10257, 10608, 12887)

# ### THE DRAFT -- record 21539167's new version, as b639 made it (data/b639_zenodo.json)
RECORD = '21539167'
DRAFT = '23228113'
VERSION = 'v1.2.0'
TITLE = 'A Place To Stand: the SIDE reduction of the Riemann Hypothesis to a single located clause'
API = 'https://zenodo.org/api'
TOKVAR = 'ZENODO' + '_TOKEN'
B639_DESC = 'b639_deposit_description.txt'
B639_DESC_SHA = 'dab9ba5f7d7afab048c021b5bc4b1f3a6e588c1be69039c3b7de828d582db696'
DESC = 'b640_deposit_description.txt'
NO_CLAIM = 'no claim is added or withdrawn'

# ### (R250)(6): THE LEGIBILITY READER, staged off D:\ so no project memory loads (OPEN_TRAILS :13223)
READER_DIR = 'C:/reader_b640'
READER_ANSWERS = 'C:/reader_b640/answers.txt'
QUESTIONS = ('What does this programme claim?', 'What does it assume?', 'What does it leave open?')

# ### THE MIRROR -- rebuilt after the act's last push and before the draft's update
ROSTER = 'tools/mirror_roster.json'
BUILDER = 'tools/mirror_build.ps1'
MIRROR_TAG = '2026-10-08-b640'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % MIRROR_TAG
MIRROR_PREV = 'D:/MY-DOwnloads/mirror-refresh-2026-10-07-b639.zip'
MIRROR_PREV_NAME = 'mirror-refresh-2026-10-07-b639.zip'
ROSTER_FILES = 74

SEALED = ('b640_worklist.py', 'b640_tests.py', 'b640_record.py', 'b640_checks.py', 'b640_closing.py', 'b640_reg_gate.py', 'b640_regspec.py')
STATUS_TOOL = 'tools/premise_status.py'
STATUS_TEST = 'tools/test_premise_status.py'

NEXT_ROUTES = [('b641, on the author`s word: the census at v0.7 with the five-status column (the method item at OPEN_TRAILS :13395), or the open '
                'premises taken up one at a time beginning with Keiper`s obligations', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def show_bytes(path, rev='HEAD', repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
