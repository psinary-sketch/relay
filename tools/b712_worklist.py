# -*- coding: utf-8 -*-
"""b712_worklist.py -- THE ACT'S DATA, UNDER (R322). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b712: LANE TWO, ACT ONE HUNDRED AND THIRTY-NINE, THE RE-CUT ACT -- b711 AT ITS WEIGHT; THE CORRIGENDUM; THE STANDING CLAUSES AT v3;
### THE PORT AND THE JOIN; THE FACES ROW; THE -15 CONTROL REGISTERED AND PRICED; THE NEXT DOCUMENT RE-CUT. No lean on this host; at most four
### runner dispatches, up to three for the port and one for the join ((R322)(4), N1).
### Written whole by the Write tool from b711_worklist.py's form (stage one: step zero; stage two, Component 5, by the Edit tool).
### The act runs in a NEW session (3bbc6267, the author's /clear after b711's closing; the same claude process, pid 3604): the previous act's
### window is b711's own session (ec2d71b5) from its post-push combine to that session's end (b701's form for a new session).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '693a46d5'         # ### PLACE-papers main before the act (b711's trail, pushed)
PRE_RELAY = '4a383ac8'      # ### relay main before the act (b711's closing, pushed alone and read back)
DATE = '2026-10-25'
SESSION_ID = '3bbc6267-f2de-40fb-b160-263f3c982c61'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R322) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = 'ec2d71b5-9c82-4b17-a54c-30c0ba8a3dce'   # ### b711 ran and closed in its own session; this act's is new
PREV_ANCHOR = 'RULING (R321) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b712_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B711_ENTRY = 10306          # ### FINDINGS: b711's entry head
B711_WEIGHT = 10282         # ### FINDINGS: b710's weight line (b711's Component 1)
B711_CORRIGENDUM = 10284    # ### FINDINGS: b711's corrigendum for b710
B711_TRAIL = 15850          # ### OPEN_TRAILS: b711's trail record
B711_FACE = 'data/b711_registration_2026-10-25.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-25-b711.zip'   # ### b711's export, CLEAN on all three clauses over 70 files
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707), its latest open-orders row :15876 (b711's trail)
ORDER_LV_PORT_LATEST = 15876
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711), for the author's word

# ### the branches step zero deletes ((R322)(8)), one per command, each its own message, in sequence, nothing chained after any
DELETE = (('D:/relay', ('push-b711-preroot', 'push-b711-preroot2', 'push-b711-root', 'push-b711-record', 'push-b711-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b711-preroot', 'push-b711-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R322)(8): NOT deleted, local or remote

# ### the kernels this act may write ((R322)(4)): the port branch's modules and SIDE-faces-join's lakefile and tag
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, unmoved
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main, untouched ((R322)(4))
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### the deposit, untouched
PORT_BRANCH = 'port-b707'
PORT_TIP = 'be3052acd2c6fe013ba482a5eddcfb236ce88738'   # ### b711's one commit on port-b707, the base of this act's edit
PORT_BASE = '92af8a344f1161e5f91df448f270bd3dea304429'  # ### b709's commit on port-b707
PORT_MODULE = 'SIDELvConservation/DirichletC7Order.lean'
PORT_LINE = 501
PORT_RUN_B711 = 40154341879
JOIN_TIP = 'b37a7b6e6322b8f99b2e1bc5c43cae248782c991'
KERNEL = 'SIDE-lv-conservation'
MAX_PORT_DISPATCHES = 3
MAX_DISPATCHES = 4

PAPERS = dict()
DATA_STANDING_V1 = 'data/standing_clauses_v1.txt'
DATA_STANDING_V2 = 'data/standing_clauses_v2.txt'
DATA_STANDING = 'data/standing_clauses_v3.txt'
REGISTRATIONS = 'data/b712_registrations.txt'
REG_B710 = '41ff1193'        # ### data/b710_registrations.txt committed alone at b710's step zero (the refined law (i), carried at (R322)(6)(ii))
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt', 'data/b711_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b711 carried them (the ferry's Component 5)
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b712'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md')
NEXT = ('b713, the research act at discriminant -15 where (R322)(6) prices it within one act’s budget, its registrations read unchanged from '
        'data/b712_registrations.txt’s commit; the keystone heads’ trigger read against the compile steps (4) and (7) reach')

# ### stage one (step zero): the commits made so far
REG_COMMIT = '67a023887360b74483803ed02c83ae44fdf88f0b'        # ### data/b712_registrations.txt with its genus control, committed alone, first
STANDING_COMMIT = 'cf193d0e7d19014359bc9c05ee4c41af6620bbd5'   # ### data/standing_clauses_v3.txt, committed alone
STEPZERO = 'ddd8785d08b760599c465a56e57fe3b1147ec824'          # ### b711's closing push capture, committed alone at step zero
STEPZERO_STEPS = 'cb8a8580249f2a150d1a805dba36a06d4b921b11'    # ### b711's closing step row, committed alone at step zero
STEPZERO_BANKS = ''          # ### the step-zero banks and tools (stage two)
C1_RELAY = ''
C1_PP = ''
C2_RELAY = ''
C2_PP = ''
C3_RELAY = ''
C3_PP = ''
C4_RELAY = ''
C4_PP = ''
REPAIRED_TOOLS = ()
REPAIRED_DATA = ()
NEW_TOOLS = ()
COMPUTE_TOOLS = ('b712_genus_control.py',)
SEALED = ()
ACT_ARMS = ()
