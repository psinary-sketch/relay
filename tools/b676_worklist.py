# -*- coding: utf-8 -*-
"""b676_worklist.py -- THE ACT'S DATA, UNDER (R286). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b676: LANE TWO, ACT ONE HUNDRED AND THREE, THE RE-CUT ACT -- b675 AT ITS WEIGHT; THE DOCUMENT NAMED BY THE RULE AND CUT IN b674'S
### FORM; THE Q0 LINES READ AND BANKED; THE STRIP USES LISTED.
### No lean on this host. Written whole by the Write tool from b675_worklist.py's form. The face is sealed after Components 1-4, the
### closing dry-run and the entry dry-run step.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '0b51683'          # ### PLACE-papers main before the act (b675's record, pushed)
PRE_RELAY = '7e867b61'      # ### relay main before the act (b675's closing, pushed)
DATE = '2026-10-17'
SESSION_ID = 'fcdfb5b9-96dd-44c6-84e3-cd8d0d0ba63d'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R286) BEGIN'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b676_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B675_ENTRY = 8881           # ### FINDINGS: b675's entry head
B675_TRAIL = 14532          # ### OPEN_TRAILS: b675's trail record

# ### the branches step zero deletes ((R286)(5)); no remote deletion is named
KE = 'D:/SIDE-explicit-formula'
DELETE = (('D:/relay', ('push-b675', 'push-b675-root', 'push-b675-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b675', 'push-b675-root')))
DELETE_REMOTE = ()
KREV = 'e36ea31'
MERGE = 'e36ea316e363b1fad04b7fa9def0fc7f2e78188f'           # ### SIDE-explicit-formula main = v0.32

# ### the strip ((R286)(4)): the merged proof's files read by git show at KREV
STRIP_FIELD = ('Zeta23/Defs.lean', 142)
HSTRIP = ('SIDEExplicitFormula/RestBound.lean', 40)
V5_FILE = 'SIDEExplicitFormula/Schema/LiRemainder.lean'
COMP_FILE = 'SIDEExplicitFormula/Schema/LiConverseCfg.lean'

# ### the re-cut ((R286)(2)): the candidate the ruling carries; its main before the act and its last tag
TD = 'D:/SIDE-trivium'
CANDIDATE = 'SIDE-trivium'
T_PRE_MAIN = '1aac3a9'
T_LAST_TAG, T_LAST_TAG_AT = 'v0.1', 'ec92d62'
T_NEXT_TAG = 'v0.1.1'
T_BRANCH = 'recut-trivium-b676'
# ### the route as run (the navigator's answers on the print list and the 'before' bank): the workflow alone on main, the print list alone on
# ### main after it, the cut on the branch; the two runs, one per tree state; the target modules (the root module imports Bijection alone)
T_WORKFLOW, T_MAIN, T_CUT = 'dd587f9', '7074154', 'db315fe'
T_TARGET = 'Trivium Trivium.CardDerived'
T_CUT_FILES = ('Trivium/Bijection.lean',)
T_RUNS = ((39004445565, 'before'), (39004541707, 'after'))
TABLE_BANK, TABLE_ROWS = 'b670_licensed_table.txt', (119, 120)
KERNELS_BANK, KERNELS_ROWS = 'b647_table_kernels.txt', (24, 25)
RULES_BANK, TIE_RULE_ROW = 'b674_rules.txt', 2

NEXT = ('b677, the research act on W-ORD-MAP-ANGLE-FORM, its ruling then, its plan to read data/b671_tie_diagnostic.txt and '
        'data/b667_h4_reading.txt before any form is chosen; b678 the re-cut act; b679 the research act, the strip variant its candidate; b680 '
        'the reading act, reading 2 of 2 -- `(R286)`(8)')

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm is a standing arm carried from b675's face (b675's own act
# ### arms not carried). Each run at HEAD and counted before the face names it. Filled at Component 5.
ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CLOSING-DRY-STEP', 'G-CITATION-CHECKED', 'G-MIDACT-CHECKED', 'G-R286-ENTERED', 'G-ROWGEN-STEPZERO',
            'G-BRANCHES-BANKED', 'G-NAMING-BEFORE-BRANCH', 'G-CUT-COMMENT-ONLY', 'G-PRINTS-EQUAL', 'G-CUT-DISTANCE', 'G-CORRESPONDENCE-DRY',
            'G-Q0-LINES-BANKED', 'G-Q0-ORDER-ENTERED', 'G-STRIP-USES-BANKED', 'G-TOOL-REPAIRS')
SHARED_APPENDED = ('data/b670_work_orders.txt',)    # ### the orders bank, its order row appended under (R254)(2) ((R286)(3))
LEFT = (('D:/relay', ()), ('D:/MY-DOwnloads/PLACE-papers', ()),
        ('D:/SIDE-trivium', ('push-b676-main', 'push-b676-merge', 'recut-trivium-b676')))   # ### left for the next ferry's list
SEALED = ('b676_worklist.py', 'b676_tests.py', 'b676_citation.py', 'b676_record.py', 'b676_checks.py', 'b676_closing.py', 'b676_reg_gate.py',
          'b676_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
