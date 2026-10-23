# -*- coding: utf-8 -*-
"""b707_worklist.py -- THE ACT'S DATA, UNDER (R317). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b707: LANE TWO, ACT ONE HUNDRED AND THIRTY-FOUR, THE RESEARCH ACT -- b706 AT ITS WEIGHT; THE RENAMES' READERS AND THE SPLIT ARM
### REPAIRED; THE SIGN-ONSET RADIUS AT Q0; THE HIGHER PAIRS' ROUTE REGISTERED; lv-CONSERVATION'S FORWARD-PORT OPENED. No lean on this host;
### one runner dispatch (the port branch of SIDE-lv-conservation) (N1).
### Written whole by the Write tool from b706_worklist.py's form (stage one: step zero; stage two, Component 5, by the Edit tool).
### The act runs in a NEW session (aa198636, the author's /clear after b706's closing); b706 ran and closed in 44411d52 (b701's form: the
### previous act's window is the other session's transcript from its anchor to its end).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'c9e0086'          # ### PLACE-papers main before the act (b706's record, pushed)
PRE_RELAY = '37e4a12f'      # ### relay main before the act (b706's closing, pushed alone and read back)
DATE = '2026-10-22'
SESSION_ID = 'aa198636-2b15-4720-b66c-e037128baa5f'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R317) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = '44411d52-210c-4cc1-9c1f-45be454f0521'   # ### b706 ran and closed in THIS OTHER session (b701's form)
PREV_ANCHOR = 'RULING (R316) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b707_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B706_ENTRY = 10046          # ### FINDINGS: b706's entry head
B706_WEIGHT = 10028         # ### FINDINGS: b705's weight line (b706's Component 1)
B706_CORRIGENDUM = 10030    # ### FINDINGS: b706's corrigendum for b705
B706_TRAIL = 15644          # ### OPEN_TRAILS: b706's trail record
B706_FACE = 'data/b706_registration_2026-10-22.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-22-b706.zip'   # ### b706's export, NOT CLEAN on clause 3 (the roster's 17 retired names)
ORDER_STANDING_CLAUSES = 15450   # ### OPEN_TRAILS: W-ORD-STANDING-CLAUSES-BANK (b702), trigger b710
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702); its opening step read at :15494 (b703); the join held at b706 (:15634)
ORDER_LV_JOIN_HELD = 15634  # ### OPEN_TRAILS: b706's annotation beneath W-ORD-LV-CLOSURE-JOIN -- the hold at GammaBounds.lean :177, the forward-port for the next ruling
ORDER_FACES_MANIFEST = 15636
ORDER_KEYSTONE = 15454      # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702), its trigger moved at :15496 (b703)
ORDER_TAG_PRINTS = 15590    # ### OPEN_TRAILS: W-ORD-ENTRY-TAG-PRINTS (b705), discharged at :15642 (b706); its remainder (the two unbanked mentions) entered here
ORDER_TAG_PRINTS_DISCHARGED = 15642
ORDERS_B706 = (15632, 15634, 15636, 15638, 15640, 15642)   # ### OPEN_TRAILS: b706's six order lines
B706_REPORT = 'data/b706_report.txt'

# ### the branches step zero deletes ((R317)(7)), one per command, each its own message, in sequence, nothing chained after any
DELETE = (('D:/relay', ('push-b706', 'push-b706-root', 'push-b706-root2', 'push-b706-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b706', 'push-b706-root')),
          ('D:/SIDE-faces-join', ('push-b706-join',)),
          ('D:/SIDE-explicit-formula', ('push-b706-ef',)))
DELETE_REMOTE = ()

FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'   # ### (R316)(3): the 17 retired copies beneath it; (R317)(2): kept out of the terminal table's ledger reach
# ### THE SUITE'S PARTS: seven, as b706 split them (the ferry's Component 5); the family reading of G-RULE-SUITE-PARTS repaired at the carry so
# ### that standing-b2a and standing-b2b read as the halves of the family standing-b2 ((R317)(2), b706's (l)).
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
PARTS_B706 = PARTS
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b707'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))   # ### the first half split in two for standing-b2a / standing-b2b

# ### THE KERNELS THIS ACT WRITES: SIDE-lv-conservation (the port branch port-b707 cut from its deposit v0.10.0, (R317)(5)); nothing written to
# ### any other kernel; SIDE-faces-join's module unchanged, its next dispatch waiting on the port
KERNEL = 'SIDE-lv-conservation'
KERNEL_DIR = 'D:/SIDE-lv-conservation'
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
EF_V037 = '38e273477257687d676033be0b0243af84a1e08a'    # ### v0.37 peeled
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main (one commit past v0.37: the workflow's probe step, b706)
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### SIDE-lv-conservation v0.10.0 peeled, the deposit -- the port's base
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main at the act's start (b694's closure step; unmoved by this act)
LV_LEAN = 'leanprover/lean4:v4.29.1'                     # ### lv's pin at v0.10.0 (lean-toolchain :1)
LV_MATHLIB = '5e932f97dd25535344f80f9dd8da3aab83df0fe6'   # ### lv's Mathlib at v0.10.0 (lake-manifest.json :8, :11; lakefile.lean :12)
EF_LEAN = 'leanprover/lean4:v4.34.0-rc1'                 # ### the shared pin: SIDE-explicit-formula's lean-toolchain :1
EF_MATHLIB = 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11'  # ### the shared pin: SIDE-explicit-formula's lake-manifest.json :10, :13
PORT_BRANCH = 'port-b707'
PORT_FILES = ('lean-toolchain', 'lake-manifest.json', 'SIDELvConservation/GammaBounds.lean')   # ### (R317)(5): the two files moved to the pin and the one line repaired
JOIN_TIP = 'b37a7b6e6322b8f99b2e1bc5c43cae248782c991'   # ### SIDE-faces-join's manifest commit (b706), unmoved by this act
JOIN_RUN = 39850337262
JOIN_HELD_AT = 'SIDELvConservation/GammaBounds.lean:177:8'
JOIN_BUILDLOG_LINE = 163                                 # ### data/b706_buildlog_SIDE-faces-join_join.txt :163, the error line
WORKFLOW = '.github/workflows/build-module.yml'
LV_MODULES = 12                                          # ### SIDELvConservation/*.lean at 93c27ec (git ls-tree -r)
LV_LEAN_FILES = 15                                       # ### every .lean at 93c27ec: the 12 modules, AxiomCheck.lean, PinnedGoal.lean, lakefile.lean -- the ruling's "15"

# ### (R317)(3): the onset tool, its banks and the registration it computes
ONSET_TOOL = 'tools/b707_onset.py'
ONSET_BANK = 'data/b707_onset.txt'
REGISTRATION_B705 = 'data/b705_registrations.txt'        # ### (iii) :15-:54, committed alone at relay d139cfcf and unchanged (N2)
REGISTRATION_B705_COMMIT = 'd139cfcf'
CC_BANK = 'data/b705_source_cc_2006_13771.txt'           # ### Connes-Consani, by page (== PAGE n rows)

B706_TRAIL_HEAD = ('### b706 — lane two, act one hundred and thirty-three, the re-cut act under (R316): b705 at its weight; the six post-seal failures '
                   'sorted and three tools repaired; the seventeen partner pairs renamed in place; the join’s manifest repaired and the join held at '
                   'lv-conservation’s module; the workflow’s probe step; the generator reaching the central kernel; the entry-tag prints at v0.1 and v0.2; '
                   'the faces row held')
SEALED = ('b707_worklist.py', 'b707_tests.py', 'b707_citation.py', 'b707_record.py', 'b707_checks.py', 'b707_closing.py', 'b707_reg_gate.py',
          'b707_regspec.py', 'b707_corrigendum.py', 'b707_onset.py', 'b707_report.py')
REPAIRED_TOOLS = ('terminal_table.py', 'rule_arms.py')   # ### (R317)(2): the table's scope and the split arm's family reading, each by the Edit tool
REPAIRED_DATA = ('tools/mirror_roster.json',)             # ### (R317)(2): the roster's 17 entries re-pointed by the Edit tool
NEW_TOOLS = ('b707_onset.py', 'b707_report.py')
ACT_ARMS = ()                # ### stage two (Component 5, by the Edit tool)
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md')
NEXT = ('b708, the re-cut act: the opening probe through the workflow’s step; the two remaining entry-tag prints; the licensed table’s next '
        'document. b709 the research act: the higher pairs’ route as (R317)(4) registers it; the port’s next dispatch; the next axis. b710 the '
        'reading act, reading 5, with W-ORD-STANDING-CLAUSES-BANK')
