# -*- coding: utf-8 -*-
"""b710_worklist.py -- THE ACT'S DATA, UNDER (R320). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b710: LANE TWO, ACT ONE HUNDRED AND THIRTY-SEVEN, THE READING ACT, READING 5 -- b709 AT ITS WEIGHT; THE NEEDLES, THE TEST AND THE LOCK
### GATE; THE STANDING CLAUSES BANKED; THE PRINCIPLES READ AGAINST THE CORPUS; THE MOVES-BY-LOCUS TABLE; THE READFIRST FLIP; THE COST READING;
### THE b711 REGISTRATIONS. No lean on this host; no runner dispatch ((R320)(7), N1).
### Written whole by the Write tool from b709_worklist.py's form (stage one: step zero; stage two, Component 5, by the Edit tool).
### The act runs in a NEW session (c9e4ce2d, the author's /clear after b709's closing): the previous act's window is b709's own session
### (0be08567) from its post-push combine to that session's end (b701's form for a new session).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '07978f3'          # ### PLACE-papers main before the act (b709's record, pushed)
PRE_RELAY = '42dd8768'      # ### relay main before the act (b709's closing, pushed alone and read back)
DATE = '2026-10-24'
SESSION_ID = 'c9e4ce2d-b9b5-4986-a582-3919fb34d296'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R320) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = '0be08567-3854-47cf-9c08-6d080b4d7312'   # ### b709 ran and closed in its own session; this act's is new
PREV_ANCHOR = 'RULING (R319) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b710_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B709_ENTRY = 10198          # ### FINDINGS: b709's entry head
B709_WEIGHT = 10184         # ### FINDINGS: b708's weight line (b709's Component 1)
B709_CORRIGENDUM = 10186    # ### FINDINGS: b709's corrigendum for b708
B709_TRAIL = 15766          # ### OPEN_TRAILS: b709's trail record
B709_FACE = 'data/b709_registration_2026-10-23.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-23-b709.zip'   # ### b709's export, CLEAN on all three clauses over 70 files
ORDER_STANDING_CLAUSES = 15450   # ### OPEN_TRAILS: W-ORD-STANDING-CLAUSES-BANK (b702), trigger b710, taken up this act ((R320)(4))
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_KEYSTONE = 15454      # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707), continued at b709, next at b711
ORDER_Q0_ZEROS = 15764      # ### OPEN_TRAILS: W-ORD-Q0-ZEROS-443 (b709), trigger b711

# ### the branches step zero deletes ((R320)(7)), one per command, each its own message, in sequence, nothing chained after any
DELETE = (('D:/relay', ('push-b709', 'push-b709-root', 'push-b709-root2', 'push-b709-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b709', 'push-b709-root')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R320)(7): NOT deleted, local or remote; this act writes nothing on it

# ### the kernels: none written this act ((R320)(7): no dispatch; N1: no lean on this host)
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, unmoved
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main, unmoved
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### the deposit
PORT_BRANCH = 'port-b707'
PORT_TIP = '92af8a344f1161e5f91df448f270bd3dea304429'   # ### b709's one commit on port-b707, held for b711
JOIN_TIP = 'b37a7b6e6322b8f99b2e1bc5c43cae248782c991'

# ### the act's papers ((R320)(5) and the ferry's read-first list), each at its file of record after b706's renames
PAPERS = dict(
    TECHNE_TOOLKIT='phase1.5/method/TECHNE_TOOLKIT.md',      # ### the ferry's TECHNE_TOOLKIT_v8_3: the versioned copy renamed in place at b706 (PP f915d6d), v8.3 at :8
    METHOD_CANON='phase1.5/method/THE_METHOD_CANON.md',
    E_DIFFICULTY_THEOREM='phase2/method/E_DIFFICULTY_THEOREM.md',
    EXHAUSTIVE_ENUMERATION='day1/Exhaustive_Enumeration.md',
    ENUMERA='phase1.5/method/ENUMERA.md',
    INSTRUMENTS='phase1.5/method/INSTRUMENTS.md',
    BRIGHTENING_MOVES='phase1.5/method/THE_BRIGHTENING_MOVES.md')

# ### the repaired tools ((R320)(3)): shared files the ruling orders edited, named in (W)
LOCKGATE = 'tools/b378_lockgate.py'
LEAN_TEST = 'tools/test_elab_reader_b634.py'
DATA_STANDING = 'data/standing_clauses_v1.txt'
READING5 = 'data/b710_reading5.txt'
REGISTRATIONS = 'data/b710_registrations.txt'
READ_BANKS = ('data/b705_read_calls.txt', 'data/b706_read_calls.txt', 'data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b709 carried them (the ferry's Component 5)
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b710'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
# ### stage two (Component 5, by the Edit tool): the commits in order, the sealed tools and the act's arms.
STEPZERO = 'e87faf67f23a21fd599075586beb6c7501ff61f9'          # ### b709's closing push capture, committed alone at step zero
REG_COMMIT = '41ff11930c65de002e76c09d36e6a3845c522e8e'        # ### the registrations and the rules bank, committed alone before any other bank
STEPZERO_BANKS = '513a8f6d04831cbc7063ebf3f1ea91a17608dfe7'    # ### the ferry, the citation check, the readfirst bank, rowgen, the branches, the tests, the fit
C1_RELAY = 'cf4a17ff62a676522fedf4fd060accb26c2d6a94'          # ### Component 1: the weight line's banks, the repairs and their controls, the corrigendum
C1_PP = '802a6c4c26ce16cd66d1f891b1c99201a59e1dcf'             # ### Component 1 at PLACE-papers: FINDINGS :10230, :10232, :10234
C2_RELAY = '3e37d9f96e3bb750b6c7265d9f88f12051f0b3e6'          # ### Component 2: the standing clauses bank, its control, the readers repointed
C3_RELAY = '8bd5cde581273486cd19bd10107a4addd117d477'          # ### Component 3: reading 5 and its route banks
C3_PP = 'e8f914110cc62de81ae98e03dff820e2b1fc66e5'             # ### Component 3 at PLACE-papers: W-ORD-MOVES-BY-LOCUS at OPEN_TRAILS :15804
C3_RELAY_B = '844513ead529d3c40f92f0a5b1413230467519ca'        # ### Component 3: the answer's check and the record's landing bank
C4_RELAY = 'b940ce1c42abac2b9cf3f1631d6753a174d3fca3'          # ### Component 4: the registrations re-read
ORDER_MOVES = 15804          # ### OPEN_TRAILS: W-ORD-MOVES-BY-LOCUS (b710), the author's word at the table's prompt
B709_TRAIL_HEAD = ('### b709 — lane two, act one hundred and thirty-six, the research act under (R319): b708 at its weight; the needle repaired and the carry read by '
                   'diff; the sign-onset radius at Q0 on the fine grid; the detection law over the higher pairs to height 325; SIDE-lv-conservation’s forward-port, '
                   '11 of 12 modules building; the second axis registered for b711')
# ### b709's one run, read as banked by the standing runner arms (no dispatch this act, (R320)(7)): the port branch at b709's tip
KERNEL = 'SIDE-lv-conservation'
PORT_BASE = '69e239d920fa76f073cdc04f9c78132e325735e1'   # ### b707's commit on port-b707, the base of b709's one commit
PORT_FILE = 'SIDELvConservation/C7OrderBounds.lean'
PORT_RUN = 40123142437
PORT_LABEL = 'port'
EF_V037 = '38e273477257687d676033be0b0243af84a1e08a'
REPAIRED_TOOLS = ('b378_lockgate.py', 'test_elab_reader_b634.py', 'ferry_scan.py')   # ### the shared tools (R320)(3)-(4) order edited, named in (W)
REPAIRED_DATA = ()
NEW_TOOLS = ('b710_fit.py', 'b710_standing.py', 'b710_reading5.py', 'b710_locate.py')
SEALED = ('b710_worklist.py', 'b710_tests.py', 'b710_citation.py', 'b710_record.py', 'b710_checks.py', 'b710_closing.py', 'b710_reg_gate.py',
          'b710_regspec.py', 'b710_corrigendum.py', 'b710_carry.py', 'b710_fit.py', 'b710_standing.py', 'b710_reading5.py',
          'b710_locate.py')   # ### the report tool tools/b710_report.py is NOT sealed (data/b708_rules.txt row (1))
ACT_ARMS = ('G-ANSWERS-BEFORE-WRITES', 'G-ANSWERS-CHECKED', 'G-ARM-SECONDS-BANKED', 'G-BRANCHES-BANKED', 'G-CARRY-SPANS', 'G-CITATION-CHECKED',
            'G-CLOSING-DRY-STEP', 'G-CORRIGENDUM-ENTERED', 'G-COST-READ', 'G-DEFECTS-LETTERED', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-FIGURES-BANKED', 'G-FIT-BANKED', 'G-FLIP-READ', 'G-GUARD-HELD', 'G-LEAN-TEST-BANKED',
            'G-LISTINGS-BEFORE-CLAUSES', 'G-LOCKGATE-ARG-REQUIRED', 'G-MOVES-ENTERED', 'G-NEEDLES-REPAIRED', 'G-NO-DISPATCH', 'G-PARTS-PRERUN',
            'G-POSTROOT-WRITES-NONE', 'G-PRINCIPLES-ROWS', 'G-R320-ENTERED', 'G-READFIRST-DIFF-BANKED', 'G-READING5-BANKED', 'G-REGISTRATIONS-ALONE',
            'G-REGISTRATIONS-REREAD', 'G-REPORT-UNSEALED', 'G-ROOTDRY-READY', 'G-ROUTE-TERMS-REGISTERED', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED',
            'G-SCORER-READS-BANKS', 'G-STANDING-CLAUSES-V1', 'G-STANDING-READERS', 'G-TOOL-REPAIRS', 'G-TRAIL-DEFECTS-EQUAL',
            'G-TRAIL-LINES-EQUAL-DEFECTS', 'G-TRAIL-RESOLVED-EQUAL', 'G-WRITELIST-MIRROR-STATE')   # ### the arms over this act's banks (Component 5, the Edit tool)
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md')
NEXT = ('b711, the research act: the port’s next line (DirichletC7Order.lean :212:55) and, where the build completes, the join’s dispatch; '
        'W-ORD-Q0-ZEROS-443 with pairs 11 and 15 against the refined detection law; the surgery and the coefficient observation; the axis (e) as b709 registered it')
