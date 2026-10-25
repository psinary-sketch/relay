# -*- coding: utf-8 -*-
"""b711_worklist.py -- THE ACT'S DATA, UNDER (R321). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b711: LANE TWO, ACT ONE HUNDRED AND THIRTY-EIGHT, THE RESEARCH ACT -- b710 AT ITS WEIGHT; THE STANDING CLAUSES AT v2; THE INDEPENDENCE
### SUPPLEMENT; THE PORT AND THE JOIN; THE SURGERY; THE AXIS; THE LIST TOWARD 443. No lean on this host; at most two runner dispatches, the
### port and the join ((R321)(4), N1).
### Written whole by the Write tool from b710_worklist.py's form (stage one: step zero; stage two, Component 5, by the Edit tool).
### The act runs in a NEW session (ec2d71b5, the author's /clear after b710's closing; the same claude process, pid 3604): the previous act's
### window is b710's own session (c9e4ce2d) from its post-push combine to that session's end (b701's form for a new session).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'df2dd7c0'         # ### PLACE-papers main before the act (b710's trail, pushed)
PRE_RELAY = 'b0d874f7'      # ### relay main before the act (b710's closing, pushed alone and read back)
DATE = '2026-10-25'
SESSION_ID = 'ec2d71b5-9c82-4b17-a54c-30c0ba8a3dce'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R321) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = 'c9e4ce2d-b9b5-4986-a582-3919fb34d296'   # ### b710 ran and closed in its own session; this act's is new
PREV_ANCHOR = 'RULING (R320) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b711_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B710_ENTRY = 10246          # ### FINDINGS: b710's entry head
B710_WEIGHT = 10230         # ### FINDINGS: b709's weight line (b710's Component 1)
B710_READINGS = 10232       # ### FINDINGS: b710's readings line
B710_CORRIGENDUM = 10234    # ### FINDINGS: b710's corrigendum for b709
B710_TRAIL = 15808          # ### OPEN_TRAILS: b710's trail record
B710_FACE = 'data/b710_registration_2026-10-24.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-24-b710.zip'   # ### b710's export, CLEAN on all three clauses over 70 files
ORDER_MOVES = 15804          # ### OPEN_TRAILS: W-ORD-MOVES-BY-LOCUS (b710)
ORDER_INDEPENDENCE = 15806   # ### OPEN_TRAILS: W-ORD-READING5-INDEPENDENCE (b710, the author's word at the root's prompt), trigger b711
ORDER_STANDING_CLAUSES = 15450   # ### OPEN_TRAILS: W-ORD-STANDING-CLAUSES-BANK (b702), taken up at b710
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707), continued at b709, next at b711
ORDER_Q0_ZEROS = 15764      # ### OPEN_TRAILS: W-ORD-Q0-ZEROS-443 (b709), trigger b711

# ### the branches step zero deletes ((R321)(8)), one per command, each its own message, in sequence, nothing chained after any
DELETE = (('D:/relay', ('push-b710', 'push-b710-preroot', 'push-b710-root', 'push-b710-record', 'push-b710-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b710', 'push-b710-order', 'push-b710-root')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R321)(8): NOT deleted, local or remote

# ### the kernels this act may write ((R321)(4)): the port branch's one module and SIDE-faces-join's lakefile and tag
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, unmoved
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main, untouched ((R321)(4))
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### the deposit, untouched
PORT_BRANCH = 'port-b707'
PORT_TIP = '92af8a344f1161e5f91df448f270bd3dea304429'   # ### b709's one commit on port-b707, the base of this act's edit
PORT_BASE = '69e239d920fa76f073cdc04f9c78132e325735e1'  # ### b707's commit on port-b707
PORT_MODULE = 'SIDELvConservation/DirichletC7Order.lean'
PORT_LINE = 212
PORT_RUN_B709 = 40123142437
JOIN_TIP = 'b37a7b6e6322b8f99b2e1bc5c43cae248782c991'
KERNEL = 'SIDE-lv-conservation'

# ### (R321)(3): the named terminals, by kernel, tag and the file the listing located (step zero, `git grep -l -w`, no line printed)
INDEPENDENCE_TERMINALS = (
    ('SIDE-bijection', 'v0.2.1', 'SIDEBijection/Theorem.lean', 'SIDEBijection.identity_formation_bijection'),
    ('SIDE-bijection', 'v0.2.1', 'SIDEBijection/Theorem.lean', 'Independence lemma'),
    ('SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/T3_StepNineBridge.lean', 'T3.T3prime_shared_witness'),
    ('SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/T3_StepNineBridge.lean', 'T3.T3doubleprime_general_commutation_fails'),
    ('SIDE-explicit-formula', 'v0.18', 'SIDEExplicitFormula/Product.lean', 'productLemma_holds'),
    ('SIDE-explicit-formula', 'v0.21', 'SIDEExplicitFormula/Schema/Family.lean', 'family_theorem'),
    ('SIDE-explicit-formula', 'v0.15', 'SIDEExplicitFormula/Schema/Converse.lean', 'h2_sign_cfg_iff_target'),
    ('SIDE-explicit-formula', 'v0.36', 'SIDEExplicitFormula/H2SignWide.lean', 'h2_sign_sum_iff_rh'),
    ('SIDE-li-map', 'v0.1.1', 'LiLinearMap.lean', 'lam_add'),
    ('SIDE-interfaces', 'v0.2.1', 'Interfaces/Kappa.lean', 'kappa_zero_of_no_mechanism'),
    ('SIDE-interfaces', 'v0.2.1', 'Interfaces/ConnectionRequiresStructure.lean', 'parametric_mechanism_theorem'),
    ('SIDE-interfaces', 'v0.2.1', 'Interfaces/ConservationProfile.lean', 'interface_split'),   # ### the declaring file at the tag (the step-zero listing named InterfaceSplit.lean, which names it only)
    ('SIDE-kernel', 'v1.8', 'Kernel/SilenceTheorem.lean', 'silence_universal'),
    ('SIDE-kernel', 'v1.8', 'Kernel/Voice3b.lean', 'offLine_of_codim_two'),
    ('SIDE-simplicity', 'v0.1.2', 'SIDESimplicity/Codimension.lean', 'the codimension terminals'))
EXCLUSION_ENGINE = 'phase1.5/method/EXCLUSION_ENGINE.md'
EE_TABLE = (185, 206)        # ### EXCLUSION_ENGINE.md: the salt-check table's header to its last row

# ### (R321)(7): the list toward 443, b709's bands' form
LIST_FROM = 325.0
LIST_STEP = 15.0
LIST_TO = 443.0
PAIR11_NEED = 405.4
PAIR15_NEED = 442.3

PAPERS = dict(EXCLUSION_ENGINE=EXCLUSION_ENGINE)
DATA_STANDING_V1 = 'data/standing_clauses_v1.txt'
DATA_STANDING = 'data/standing_clauses_v2.txt'
REGISTRATIONS = 'data/b710_registrations.txt'
AXIS_REGISTRATION = 'data/b709_registrations.txt'
INDEPENDENCE = 'data/b711_independence.txt'
READ_BANKS = ('data/b706_read_calls.txt', 'data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b710 carried them (the ferry's Component 5)
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b711'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md')
NEXT = ('b712, the re-cut act: the faces row naming the join where (R321)(4) tags it; the class-number-2 control (discriminant -15) priced for a '
        'later research act; the licensed table’s next document')

# ### stage two (Component 1, by the Edit tool; completed at Component 5): the commits in order, the tools, the sealed list, the act's arms.
# ### A commit not yet made is ''; the suite's readers of an empty commit read nothing.
STEPZERO = '181e1995ce4c7db74b27b6996ab1975a4477daec'          # ### b710's closing push capture, committed alone at step zero
STEPZERO_BANKS = '4aa6e281ddf49dd4718cfda72cb067b663928192'    # ### the step-zero banks and tools (git rev-parse, read 2026-10-25)
REG_COMMIT = ''              # ### no registration this act ((R321) registers nothing new; b710's are read)
C1_RELAY = ''                # ### Component 1: the weight line's bank, the repairs and their controls, the corrigendum
C1_PP = ''                   # ### Component 1 at PLACE-papers: b710's weight line and the corrigendum entry
C2_RELAY = ''                # ### Component 2: the port's bank
C3_RELAY = ''                # ### Component 3: the surgery, the coefficients, the axis
C3_PP = ''
C3_RELAY_B = ''
C4_RELAY = ''                # ### Component 4: the list toward 443
B709_TRAIL_HEAD = ('### b710 — lane two, act one hundred and thirty-seven, the reading act under (R320): b709 at its weight; the needles, the test and '
                   'the lock gate repaired; the standing clauses banked at v1; the four principles read against the corpus; the moves-by-locus table '
                   'entered; the readfirst flip and the cost read; the refined detection law and the surgery registered for b711')   # ### the previous act's trail head (OPEN_TRAILS :15808), under the carried suite's name
PORT_FILE = PORT_MODULE
PORT_LABEL = 'port'
PORT_RUN = None              # ### this act's one port dispatch, read by its run id at Component 2
EF_V037 = '38e273477257687d676033be0b0243af84a1e08a'
REPAIRED_TOOLS = ()          # ### shared tools of earlier acts edited by this act: none
REPAIRED_DATA = ()
NEW_TOOLS = ('act_membrane.py',)   # ### (R321)(2)(ii): the membrane's shared tool, new at b711, named in (W)
SEALED = ('b711_worklist.py', 'b711_tests.py', 'b711_citation.py', 'b711_record.py', 'b711_checks.py', 'b711_closing.py', 'b711_reg_gate.py',
          'b711_regspec.py', 'b711_corrigendum.py', 'b711_carry.py', 'b711_standing.py', 'b711_independence.py')   # ### completed at Component 5; the report tool NOT sealed (data/b708_rules.txt row (1))
ACT_ARMS = ('G-ANSWERS-BEFORE-WRITES', 'G-ANSWERS-CHECKED', 'G-ARM-SECONDS-BANKED', 'G-BRANCHES-BANKED', 'G-CARRY-SPANS', 'G-CITATION-CHECKED',
            'G-CLOSING-DRY-STEP', 'G-CORRIGENDUM-ENTERED', 'G-COST-READ', 'G-DEFECTS-LETTERED', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-FIGURES-BANKED', 'G-FIT-BANKED', 'G-FLIP-READ', 'G-GUARD-HELD', 'G-LEAN-TEST-BANKED',
            'G-LISTINGS-BEFORE-CLAUSES', 'G-LOCKGATE-ARG-REQUIRED', 'G-MOVES-ENTERED', 'G-NEEDLES-REPAIRED', 'G-NO-DISPATCH', 'G-PARTS-PRERUN',
            'G-POSTROOT-WRITES-NONE', 'G-PRINCIPLES-ROWS', 'G-R321-ENTERED', 'G-READFIRST-DIFF-BANKED', 'G-READING5-BANKED', 'G-REGISTRATIONS-ALONE',
            'G-REGISTRATIONS-REREAD', 'G-REPORT-UNSEALED', 'G-ROOTDRY-READY', 'G-ROUTE-TERMS-REGISTERED', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED',
            'G-SCORER-READS-BANKS', 'G-STANDING-CLAUSES-V1', 'G-STANDING-READERS', 'G-TOOL-REPAIRS', 'G-TRAIL-DEFECTS-EQUAL',
            'G-TRAIL-LINES-EQUAL-DEFECTS', 'G-TRAIL-RESOLVED-EQUAL', 'G-WRITELIST-MIRROR-STATE')   # ### b710's act arms as carried; rewritten for this act's banks at Component 5
