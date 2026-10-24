# -*- coding: utf-8 -*-
"""b709_worklist.py -- THE ACT'S DATA, UNDER (R319). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b709: LANE TWO, ACT ONE HUNDRED AND THIRTY-SIX, THE RESEARCH ACT -- b708 AT ITS WEIGHT; THE NEEDLE AND THE CARRY BY DIFF; THE FINE GRID;
### THE PORT'S NEXT LINES; THE HIGHER PAIRS; THE NEXT AXIS. No lean on this host; one runner dispatch (the port branch of SIDE-lv-conservation
### at its new tip, (R319)(4), N1).
### Written whole by the Write tool from b708_worklist.py's form (stage one: step zero; stage two, Component 5, by the Edit tool).
### The act runs in the SAME session as b708 (0be08567): the previous act's window is this session's transcript from b708's post-push combine to
### (R319)'s anchor (b700's form for the same session).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '6abebe6'          # ### PLACE-papers main before the act (b708's record, pushed)
PRE_RELAY = '60739238'      # ### relay main before the act (b708's closing, pushed alone and read back)
DATE = '2026-10-23'
SESSION_ID = '0be08567-3854-47cf-9c08-6d080b4d7312'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R319) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = SESSION_ID   # ### b708 ran and closed in THIS session (b700's form: the window from b708's post-push combine to this act's anchor)
PREV_ANCHOR = 'RULING (R318) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b709_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B708_ENTRY = 10152          # ### FINDINGS: b708's entry head
B708_WEIGHT = 10138         # ### FINDINGS: b707's weight line (b708's Component 1)
B708_CORRIGENDUM = 10140    # ### FINDINGS: b708's corrigendum for b707
B708_TRAIL = 15724          # ### OPEN_TRAILS: b708's trail record
B708_FACE = 'data/b708_registration_2026-10-23.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-23-b708.zip'   # ### b708's export, CLEAN on all three clauses over 70 files
ORDER_STANDING_CLAUSES = 15450   # ### OPEN_TRAILS: W-ORD-STANDING-CLAUSES-BANK (b702), trigger b710
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702); the join held at b706 (:15634); the forward-port entered at b707 (:15686)
ORDER_KEYSTONE = 15454      # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702), held at every re-cut act
ORDER_TAG_PRINTS = 15590    # ### OPEN_TRAILS: W-ORD-ENTRY-TAG-PRINTS (b705), discharged at :15642 (b706), its remainder entered at :15684 (b707), read to its end at b708
ORDER_TAG_REMAINDER = 15684
ORDER_WORKFLOW_PROBE = 15544   # ### OPEN_TRAILS: W-ORD-WORKFLOW-PROBE-STEP (b705), discharged at :15638 (b706) with the trigger b708; annotated DISCHARGED at b709 ((R319)(2))
ORDER_WORKFLOW_PROBE_DISCHARGED = 15638
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT entered and opened (b707); continued this act ((R319)(4))
B708_REPORT = 'data/b708_report.txt'

# ### the branches step zero deletes ((R319)(7)), one per command, each its own message, in sequence, nothing chained after any
DELETE = (('D:/relay', ('push-b708', 'push-b708-root', 'push-b708-root2', 'push-b708-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b708', 'push-b708-root')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R319)(7): NOT deleted, local or remote; this act commits on it ((R319)(4))

FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b708 carried them (the ferry's Component 5)
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b709'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))

# ### THE KERNEL THIS ACT WRITES: SIDE-lv-conservation on its port branch alone ((R319)(4): C7OrderBounds.lean :277 and :380 repaired by the Edit
# ### tool, one commit, pushed in branch mode, dispatched once); no main moved, no tag made or moved, no merge
KERNEL = 'SIDE-lv-conservation'
KERNEL_DIR = 'D:/SIDE-lv-conservation'
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
EF_V037 = '38e273477257687d676033be0b0243af84a1e08a'    # ### v0.37 peeled, the kernel's current tag
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main (one commit past v0.37), unmoved by this act
EF_LEAN = 'leanprover/lean4:v4.34.0-rc1'                 # ### the shared pin
EF_MATHLIB = 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11'  # ### the shared pin: Mathlib's rev at SIDE-explicit-formula and on port-b707
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### SIDE-lv-conservation v0.10.0 peeled, the deposit -- the port's base
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main (unmoved by b707, b708 and this act)
PORT_BRANCH = 'port-b707'
PORT_BASE = '69e239d920fa76f073cdc04f9c78132e325735e1'  # ### b707's one commit on port-b707, this act's base on the branch
PORT_RUN_B707 = 39888369981
PORT_FILE = 'SIDELvConservation/C7OrderBounds.lean'      # ### the one module this act edits, at :277 and :380 ((R319)(4))
PORT_LINES = (277, 380)
PORT_MODULES = 12                                        # ### the lakefile's modules at 93c27ec (b707: 6 of 12 built)
PORT_FILES_15 = 15                                       # ### the .lean files at 93c27ec (b707: 6 of 15 built)
JOIN_TIP = 'b37a7b6e6322b8f99b2e1bc5c43cae248782c991'   # ### SIDE-faces-join's manifest commit (b706), unmoved
WORKFLOW = '.github/workflows/build-module.yml'

# ### (R319)(3) and (5): the two computation tools, their banks and hashes banks alone
GRID_TOOL = 'b709_grid.py'
GRID_BANK = 'data/b709_grid.txt'
PAIRS_TOOL = 'b709_pairs.py'
PAIRS_BANK = 'data/b709_pairs.txt'
REGISTRATION_B708 = 'data/b708_registrations.txt'        # ### the fine grid, committed alone at relay 6045dd8c; computed this act as registered
REGISTRATION_B707 = 'data/b707_registrations.txt'        # ### the higher pairs' route, committed alone at relay 6e8ece87; computed this act as registered
ONSET_BANK = 'data/b707_onset.txt'
ONSET_CONTROLS = 'data/b707_onset_controls.txt'
RANKING = 'data/b705_i6_ranking.txt'                     # ### :58 the second axis, (e) representation coordinates ((R319)(6))

B708_TRAIL_HEAD = ('### b708 — lane two, act one hundred and thirty-five, the re-cut act under (R318): b707 at its weight; the faces chain probed through the '
                   'workflow’s step at v0.37; the entry-tag prints complete; day1/Spectral_Inertness.md re-cut; the onset’s fine grid registered')
# ### stage two (Component 5, by the Edit tool): the commits in order, the sealed tools and the act's arms.
STEPZERO = 'c1b64ca5'        # ### b708's closing push capture, committed alone at step zero
STEPZERO_BANKS = '17d67b307a412a3bfc3dba8aa167d25df73ac29d'   # ### the ferry, the citation check, the readfirst bank, rowgen, the branches, the tests, the first tools
REG_COMMIT = '510dc29b374ff89afa3ac4ccfadab74a05b7ce8e'              # ### data/b709_registrations.txt and data/b709_rules.txt committed alone, before any computation (N2)
C1_RELAY = '7e8a6f9ec492c84351ba793534ea6f507f5d148b'   # ### Component 1's relay commit (the weight line's banks, the repair's controls, the corrigendum banks, the order)
C1_PP = 'c31eca883d11cc573557e2dc8391ca34ba3341d5'      # ### Component 1's PLACE-papers commit (the weight line :10184, the corrigendum entry :10186, the order's annotation :15762)
C2_RELAY = '91607edbc2bbc52cb66fc45341934ef1edaea73c'   # ### Component 2's relay commit (the pairs); the grid's commit before it bf1f2e16c26950b17617337939a5cd2617e28911
C2_RELAY_GRID = 'bf1f2e16c26950b17617337939a5cd2617e28911'
C2_PP = 'caf18664eee7eadfeab4917ce9550717cedbef0d'      # ### Component 2's PLACE-papers commit: W-ORD-Q0-ZEROS-443 entered at OPEN_TRAILS :15764 (the author's bound at 325)
ORDER_Q0_ZEROS = 15764       # ### OPEN_TRAILS: W-ORD-Q0-ZEROS-443 (b709), trigger b711
PAIRS_BOUND = 325            # ### the author's word of 2026-10-24: the higher pairs bounded at height 325; pairs 11 and 15 beyond reach, W-ORD-Q0-ZEROS-443 for b711
C3_RELAY = ''                # ### Component 3's relay commit (the port banks)
C3_PP = ''                   # ### none: Component 3 writes no ledger
C4_RELAY = ''                # ### Component 4's relay commit (the axis named; the registrations re-read)
PORT_TIP = '92af8a344f1161e5f91df448f270bd3dea304429'   # ### this act's one commit on port-b707 (Component 3), pushed in branch mode and read back (data/b709_port_push_out.txt)
PORT_RUN = 40123142437       # ### this act's one dispatch, read by its run id (Component 3): completed, failure; 11 of 12 modules built; DirichletC7Order held at :212:55
PORT_BUILT = 11              # ### modules built of PORT_MODULES at the run (b707: 6); C7OrderBounds now builds
PORT_NEXT_LINE = 'SIDELvConservation/DirichletC7Order.lean:212:55'   # ### the next failing line, a changed signature (the same hasMellin argument as :277)
PORT_LABEL = 'port'
SEALED = ('b709_worklist.py', 'b709_tests.py', 'b709_citation.py', 'b709_record.py', 'b709_checks.py', 'b709_closing.py', 'b709_reg_gate.py',
          'b709_regspec.py', 'b709_corrigendum.py', 'b709_carry.py', 'b709_grid.py', 'b709_pairs.py')   # ### the report tool tools/b709_report.py is NOT sealed (data/b708_rules.txt row (1))
REPAIRED_TOOLS = ()
REPAIRED_DATA = ()
NEW_TOOLS = ()
ACT_ARMS = ()                # ### filled at Component 5 by the Edit tool
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md')
NEXT = ('b710, the reading act, reading 5: the standing-clauses bank (W-ORD-STANDING-CLAUSES-BANK) written and the ferry carried by version from b711; '
        'the readfirst flip read against readings 3 and 4; the reading of the principles S, I, D and E against the corpus; the moves-by-locus table '
        'drafted for the author’s word. b711 the research act: the join’s dispatch where the port completes; the second axis')
