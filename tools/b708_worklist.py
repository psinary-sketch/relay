# -*- coding: utf-8 -*-
"""b708_worklist.py -- THE ACT'S DATA, UNDER (R318). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b708: LANE TWO, ACT ONE HUNDRED AND THIRTY-FIVE, THE RE-CUT ACT -- b707 AT ITS WEIGHT; THE WRITE LIST AND THE REPORT TOOL; THE PROBE
### THROUGH THE WORKFLOW'S STEP; THE REMAINING ENTRY-TAG PRINTS; THE NEXT DOCUMENT CUT; THE FINE GRID REGISTERED. No lean on this host; the
### runner dispatches of (R318)(4)-(5) (the probe branch and the entry-tag scratch branch of SIDE-explicit-formula) (N1).
### Written whole by the Write tool from b707_worklist.py's form (stage one: step zero; stage two, Component 5, by the Edit tool).
### The act runs in a NEW session (0be08567, the author's /clear after b707's closing); b707 ran and closed in aa198636 (b701's form: the
### previous act's window is the other session's transcript from its post-push combine to its end).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '95dc6f6'          # ### PLACE-papers main before the act (b707's record, pushed)
PRE_RELAY = 'b5898a61'      # ### relay main before the act (b707's closing, pushed alone and read back)
DATE = '2026-10-23'
SESSION_ID = '0be08567-3854-47cf-9c08-6d080b4d7312'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R318) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = 'aa198636-2b15-4720-b66c-e037128baa5f'   # ### b707 ran and closed in THIS OTHER session (b701's form)
PREV_ANCHOR = 'RULING (R317) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b708_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B707_ENTRY = 10106          # ### FINDINGS: b707's entry head
B707_WEIGHT = 10084         # ### FINDINGS: b706's weight line (b707's Component 1)
B707_CORRIGENDUM = 10086    # ### FINDINGS: b707's corrigendum for b706
B707_TRAIL = 15688          # ### OPEN_TRAILS: b707's trail record
B707_FACE = 'data/b707_registration_2026-10-22.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-22-b707.zip'   # ### b707's export, CLEAN on all three clauses over 70 files
ORDER_STANDING_CLAUSES = 15450   # ### OPEN_TRAILS: W-ORD-STANDING-CLAUSES-BANK (b702), trigger b710
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702); the join held at b706 (:15634); the forward-port entered at b707 (:15686)
ORDER_KEYSTONE = 15454      # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702), its trigger moved at :15496 (b703); held at every re-cut act
ORDER_TAG_PRINTS = 15590    # ### OPEN_TRAILS: W-ORD-ENTRY-TAG-PRINTS (b705), discharged at :15642 (b706), its remainder entered at :15684 (b707)
ORDER_TAG_PRINTS_DISCHARGED = 15642
ORDER_TAG_REMAINDER = 15684  # ### OPEN_TRAILS: the two unbanked mentions, trigger b708 (the first)
ORDER_WORKFLOW_PROBE = 15544   # ### OPEN_TRAILS: W-ORD-WORKFLOW-PROBE-STEP (b705), discharged at :15638 (b706) with the trigger for the chain's next probe, b708
ORDER_WORKFLOW_PROBE_DISCHARGED = 15638
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT entered and opened (b707); its next dispatch at b709
B707_REPORT = 'data/b707_report.txt'
B707_REPORT_ROOT = 'data/b707_report_root.txt'

# ### the branches step zero deletes ((R318)(8)), one per command, each its own message, in sequence, nothing chained after any
DELETE = (('D:/relay', ('push-b707', 'push-b707-root', 'push-b707-root2', 'push-b707-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b707', 'push-b707-root')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R318)(8): NOT deleted, local or remote

FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'   # ### (R316)(3): the 17 retired copies beneath it; (R317)(2): kept out of the terminal table's ledger reach
# ### THE SUITE'S PARTS: seven, as b706 split them and b707 carried them (the ferry's Component 5); the family reading of G-RULE-SUITE-PARTS
# ### repaired at b707 so that standing-b2a and standing-b2b read as the halves of the family standing-b2.
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
PARTS_B707 = PARTS
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b708'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))   # ### the first half split in two for standing-b2a / standing-b2b

# ### THE KERNELS THIS ACT WRITES: SIDE-explicit-formula on scratch branches alone ((R318)(4)-(5): probe-b708 and prints-b708-v0.17, each
# ### deleted after its bank is committed); no main moved, no tag made or moved; SIDE-lv-conservation's port-b707 read, not edited ((R318)(7))
KERNEL = 'SIDE-explicit-formula'
KERNEL_DIR = 'D:/SIDE-explicit-formula'
EF_DIR = 'D:/SIDE-explicit-formula'
LV_DIR = 'D:/SIDE-lv-conservation'
JOIN_DIR = 'D:/SIDE-faces-join'
EF_V037 = '38e273477257687d676033be0b0243af84a1e08a'    # ### v0.37 peeled, the kernel's current tag
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main (one commit past v0.37: the workflow's probe step, b706)
EF_V017 = '5a1630b8292b29657b0e9b488b25034c6989c737'    # ### v0.17 peeled (simplicity_iff; SIMPLICITY :442's mention)
EF_LEAN = 'leanprover/lean4:v4.34.0-rc1'                 # ### the shared pin: SIDE-explicit-formula's lean-toolchain :1
EF_MATHLIB = 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11'  # ### the shared pin: SIDE-explicit-formula's lake-manifest.json :10, :13
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### SIDE-lv-conservation v0.10.0 peeled, the deposit -- the port's base
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main (unmoved by b707; unmoved by this act)
PORT_BRANCH = 'port-b707'
PORT_COMMIT = '69e239d920fa76f073cdc04f9c78132e325735e1'   # ### the one commit on port-b707 (b707), kept at the remote, not edited this act
PORT_RUN = 39888369981
JOIN_TIP = 'b37a7b6e6322b8f99b2e1bc5c43cae248782c991'   # ### SIDE-faces-join's manifest commit (b706), unmoved
WORKFLOW = '.github/workflows/build-module.yml'
PROBE_BRANCH = 'probe-b708'                              # ### (R318)(4): cut from main (badaccc), the modules' tree v0.37's; one file added, ChainProbe.lean
PROBE_FILE = 'ChainProbe.lean'
NODES_B704 = 'data/b704_nodes_zeta.txt'                  # ### the list the faces page names at :3 (b704's regeneration)
B704_PROBE_OUT = 'data/b704_probe_out_zeta.txt'          # ### b704's probe bank (run 39721668586, through the closure step)
CANDIDATES = ('SIDEExplicitFormula.B321.h2_sign_sum_iff_rh', "SIDEExplicitFormula.B321.h2_sign'_imp_rh")   # ### b704's two candidate nodes (data/b704_probe.json)
PROBE_WATCH = ['SIDEExplicitFormula.RegisterDepth']
PRINTS_BRANCH = 'prints-b708-v0.17'                      # ### (R318)(5): the one scratch branch, cut at v0.17 in b706's form
TAG_THEOREMS = {'v0.17': 'SIDEExplicitFormula.Simplicity.simplicity_iff'}   # ### SIMPLICITY :442 names the Prop `simplicity` at v0.17 = 5a1630b by `simplicity_iff`
TAG_MODULES = {'v0.17': 'SIDEExplicitFormula.Simplicity'}                    # ### the theorem's module at the tag (read by the tagstate route, git grep bounded to the tree)
MENTIONS_UNBANKED = (('SIMPLICITY_OF_RIEMANN_ZEROS', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 442, 'v0.17'),
                     ('FACES_LEDGER', 'FACES_LEDGER.md', 20, None))   # ### data/b706_cells_reread.txt :16 and :37; the second names no kernel and no tag (b707's (e))

# ### (R318)(6): the licensed table's next document -- named by the tie route at step zero (data/b708_tie.txt), the form a companion's cut takes
CUT_DOC = 'day1/Spectral_Inertness.md'
CUT_TABLE = 'b646_table_Spectral_Inertness.txt'
CUT_HELD = ()                                            # ### filled at Component 3 by the Edit tool where a row is held (a Correspondence cell, a keystone head)

# ### (R318)(3): the fine grid's registration, written at step zero and committed alone before any computation of this act (N3)
REGISTRATION_B705 = 'data/b705_registrations.txt'        # ### (iii) :15-:54, committed alone at relay d139cfcf and unchanged
REGISTRATION_B707 = 'data/b707_registrations.txt'        # ### the higher pairs' route, committed alone at relay 6e8ece87
ONSET_BANK = 'data/b707_onset.txt'
ONSET_CONTROLS = 'data/b707_onset_controls.txt'

B707_TRAIL_HEAD = ('### b707 — lane two, act one hundred and thirty-four, the research act under (R317): b706 at its weight; the renames’ readers and the '
                   'split arm repaired; the sign-onset radius at Q0 on the family at two frequencies; the twelve higher pairs’ route registered; '
                   'lv-conservation’s forward-port opened and held at C7OrderBounds')
# ### stage two (Component 5, by the Edit tool): the commits in order, the sealed tools and the act's arms.
STEPZERO = ''                # ### b707's closing push capture, committed alone at step zero
STEPZERO_BANKS = ''          # ### the ferry, the citation check, the readfirst bank, rowgen, the branches, the tests, the first tools
REG_COMMIT = ''              # ### data/b708_registrations.txt and data/b708_rules.txt committed alone, before any computation (N3)
SEALED = ('b708_worklist.py', 'b708_tests.py', 'b708_citation.py', 'b708_record.py', 'b708_checks.py', 'b708_closing.py', 'b708_reg_gate.py',
          'b708_regspec.py', 'b708_corrigendum.py')   # ### the report tool tools/b708_report.py is NOT sealed: written after the root's word (data/b708_rules.txt row (1))
REPAIRED_TOOLS = ()
REPAIRED_DATA = ()
NEW_TOOLS = ()
ACT_ARMS = ()                # ### filled at Component 5 by the Edit tool
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', 'day1/Spectral_Inertness.md')   # ### the cut document joins at Component 3 (the tie route's naming)
NEXT = ('b709, the research act: the fine grid as (R318)(3) registers it; the higher pairs’ route as data/b707_registrations.txt registers it; '
        'the port’s next dispatch at C7OrderBounds.lean :277 and :380; the next axis of data/b705_i6_ranking.txt. b710 the reading act, reading 5, '
        'with W-ORD-STANDING-CLAUSES-BANK and the readfirst flip read against readings 3 and 4')
