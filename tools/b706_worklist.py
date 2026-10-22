# -*- coding: utf-8 -*-
"""b706_worklist.py -- THE ACT'S DATA, UNDER (R316). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b706: LANE TWO, ACT ONE HUNDRED AND THIRTY-THREE, THE RE-CUT ACT -- b705 AT ITS WEIGHT; THE POST-SEAL FAILURES SORTED AND THREE TOOLS
### REPAIRED; THE PARTNER COPIES RENAMED IN PLACE; THE JOIN'S MANIFEST; THE WORKFLOW'S PROBE STEP; THE GENERATOR'S REACH; THE ENTRY-TAG
### PRINTS; THE FACES ROW. No lean on this host; three runner dispatches (the join, the two entry-tag branches) (N1).
### Written whole by the Write tool from b705_worklist.py's form (stage one: step zero; stage two, Component 5, by the Edit tool).
### The act runs in the SAME session as b705 (44411d52); the anchor is (R316)'s line, unique in it after (R315)'s.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'c4c4273'          # ### PLACE-papers main before the act (b705's record, pushed)
PRE_RELAY = 'f9a60e40'      # ### relay main before the act (b705's closing, pushed alone and read back)
DATE = '2026-10-22'
SESSION_ID = '44411d52-210c-4cc1-9c1f-45be454f0521'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R316) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = SESSION_ID   # ### b705 ran and closed in THIS session (b703's form: the previous window is the same transcript, anchor to anchor)
PREV_ANCHOR = 'RULING (R315) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b706_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B705_ENTRY = 9990           # ### FINDINGS: b705's entry head
B705_WEIGHT = 9974          # ### FINDINGS: b704's weight line (b705's Component 1)
B705_CORRIGENDUM = 9976     # ### FINDINGS: b705's corrigendum for b704
B705_TRAIL = 15592          # ### OPEN_TRAILS: b705's trail record
B705_FACE = 'data/b705_registration_2026-10-22.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-22-b705.zip'
ORDER_PARTNER = 15446       # ### OPEN_TRAILS: W-ORD-PAPER-PARTNER-COPIES (b702), disposition (iii), trigger b706 -- (R316)(3)
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702), its opening step read at :15494 (b703); the join built at b705
ORDER_LV_JOIN_READ = 15494
ORDER_KEYSTONE = 15454      # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702), its trigger moved at :15496 (b703)
ORDER_KEYSTONE_MOVED = 15496
ORDER_E0 = 15506            # ### OPEN_TRAILS: W-ORD-E0-MET-CLASSK (b703), companions :15548 (b704); its content done at b705 on the word
ORDER_PROBE_STEP = 15544    # ### OPEN_TRAILS: W-ORD-WORKFLOW-PROBE-STEP (b704), trigger b706 -- (R316)(5)
ORDER_EF_REACH = 15546      # ### OPEN_TRAILS: W-ORD-CORRESPONDENCE-EF-REACH (b704), trigger b706 -- (R316)(6)
ORDER_TAG_PRINTS = 15590    # ### OPEN_TRAILS: W-ORD-ENTRY-TAG-PRINTS (b705), trigger b706 -- (R316)(7)
ORDERS_B705 = (15590,)      # ### OPEN_TRAILS: b705's one order
FACES_ORDER = 15444         # ### OPEN_TRAILS: W-ORD-FACES-PROBE-CURRENT (b702), discharged at :15542 (b704); the page's generator form

# ### the branches step zero deletes ((R316)(9)), one per command, each its own message, in sequence, nothing chained after any
DELETE = (('D:/relay', ('push-b705', 'push-b705-root', 'push-b705-root2', 'push-b705-root3', 'push-b705-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b705', 'push-b705-root')),
          ('D:/SIDE-faces-join', ('push-b705-join',)))
DELETE_REMOTE = ()

FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
# ### THE SUITE'S PARTS: standing-b2 (576-577 s at b705's post-push run, the chain's first half) SPLIT at this act per data/b684_rules.txt
# ### row (1), the split named here before the pre-run: standing-b2a reads the chain over b624-b641, standing-b2b over b642-b658.
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
PARTS_B705 = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b706'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))   # ### the first half split in two for standing-b2a / standing-b2b

# ### THE KERNELS THIS ACT WRITES: SIDE-faces-join (its lakefile, (R316)(4)); SIDE-explicit-formula (its workflow on main, (R316)(5); two scratch
# ### branches at the entry tags, (R316)(7)); nothing written to any other kernel
KERNEL = 'SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-faces-join'
EF_DIR = 'D:/SIDE-explicit-formula'
LV_DIR = 'D:/SIDE-lv-conservation'
EF_V037 = '38e273477257687d676033be0b0243af84a1e08a'    # ### v0.37 peeled; SIDE-explicit-formula's main at the act's start
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### SIDE-lv-conservation v0.10.0 peeled, the deposit
LV_MAIN = 'd38f3e8c99c3'                                 # ### SIDE-lv-conservation's main at the act's start (b705's closing)
EF_LEAN = 'leanprover/lean4:v4.34.0-rc1'
EF_MATHLIB = 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11'
EF_V01 = 'baed4df861dac05224f01dad17453648d3d7fe0a'     # ### v0.1 peeled (ch_iff_rh), as the papers cite it
EF_V02 = '5c72cad24303f23d92256ebd466d3a3d32424a4b'     # ### v0.2 peeled (h2_sign_iff_rh)
PRINT_BRANCHES = (('v0.1', 'prints-b706-v0.1'), ('v0.2', 'prints-b706-v0.2'))   # ### (R316)(7): the scratch branches, deleted after their banks
JOIN_MODULE = 'FacesJoin'
JOIN_TERMINAL = 'faces_join'
JOIN_TAG = 'v0.1.0'
JOIN_TIP_B705 = '732c1b49aada7f6266414a010e42652c877882f6'   # ### SIDE-faces-join's one commit at b705, the held run's ref
JOIN_RUN_B705 = 39799253764
WORKFLOW = '.github/workflows/build-module.yml'
PROBE_FILE = 'ChainProbe.lean'                            # ### (R316)(5): the root file the new step runs when the ref carries one

# ### stage two (Component 5, by the Edit tool): the commits in order, the sealed tools and the act's arms.
STEPZERO = ''                # ### b705's closing push capture, committed alone at step zero
STEPZERO_BANKS = ''
C1_RELAY, C1_PP = '', ''
C2_RELAY, C2_PP = '', ''
C3_RELAY, C3_PP = '', ''
C4_RELAY, C4_PP = '', ''
JOIN_TIP = ''                # ### SIDE-faces-join's manifest commit, the ref of this act's one join dispatch
JOIN_RUN = 0
JOIN_GATE = ''
B705_TRAIL_HEAD = ('### b705 — lane two, act one hundred and thirty-two, the research act under (R315): b704 at its weight; the eight failures '
                   'sorted and three predicates repaired; the closure join built as its own kernel and held at its one run; the count’s contour '
                   'read; the detection law over seventeen pairs and the notched window at the lowest band zero; the perspective ranking; E0’s '
                   'lexicon extended')
SEALED = ('b706_worklist.py', 'b706_tests.py', 'b706_citation.py', 'b706_record.py', 'b706_checks.py', 'b706_closing.py', 'b706_reg_gate.py',
          'b706_regspec.py', 'b706_corrigendum.py', 'b706_standing_figures.py')
REPAIRED_TOOLS = ('correspondence_gen.py',)   # ### (R316)(6): the parser extended by the Edit tool, its control byte for byte
NEW_TOOLS = ()
ACT_ARMS = ()
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', 'REGISTRY.md')
NEXT = ('b707, the research act: the sign-onset radius at Q0 as data/b705_registrations.txt (iii) registered it, with its controls; the '
        'top-ranked axis at full grade; the detection law’s twelve higher pairs priced by a route beyond b675’s modulus rule, registered before '
        'any number. b708 the re-cut act with the opening probe through the workflow’s step. b710 the reading act, reading 5')
