# -*- coding: utf-8 -*-
"""b685_worklist.py -- THE ACT'S DATA, UNDER (R295). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b685: LANE TWO, ACT ONE HUNDRED AND TWELVE, THE RESEARCH ACT -- b684 AT ITS WEIGHT; THE COUNT LAW P3 (Q0Count) AT Q0 READ FROM THE
### KERNEL, SEARCHED IN THE LITERATURE, DERIVED IN BACKLUND'S FORM WITH CERTIFIED CONSTANTS, COMPOSED WITH THE CERTIFIED REGION, CONTROLLED.
### No lean on this host. Written whole by the Write tool from b684_worklist.py's form.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'a2acff6'          # ### PLACE-papers main before the act (b684's record, pushed)
PRE_RELAY = '4b97f382'      # ### relay main before the act (b684's closing, pushed)
DATE = '2026-10-18'
SESSION_ID = 'df03c73f-520a-4848-85dc-8fada095f008'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R295) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b685_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B684_ENTRY = 9200           # ### FINDINGS: b684's entry head
B684_TRAIL = 14804          # ### OPEN_TRAILS: b684's trail record

# ### the kernel this act reads (no kernel write this act, N5)
KE = 'D:/SIDE-explicit-formula'
K_TAG, K_MAIN = 'v0.33', '95f8dc8'

# ### the branches step zero deletes ((R295)(8)), one per command, each its own message, in sequence; a cut branch's tip printed as an
# ### ancestor of its kernel's main at the new tag before its delete
DELETE = (('D:/relay', ('push-b684-root', 'push-b684', 'push-b684-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b684-root', 'push-b684')),
          ('D:/SIDE-class-number-anomaly', ('push-b684-main', 'push-b684-merge', 'recut-class-number-anomaly-b684')),
          ('D:/SIDE-window', ('push-b684r-merge', 'recut-window-b684r')),
          ('D:/SIDE-trivium', ('push-b684r-merge', 'recut-trivium-b684r')),
          ('D:/SIDE-silence-principle', ('push-b684r-merge', 'recut-silence-principle-b684r')))
DELETE_REMOTE = (('D:/SIDE-class-number-anomaly', 'recut-class-number-anomaly-b684', 'v0.2.1'),
                 ('D:/SIDE-window', 'recut-window-b684r', 'v0.5.2'),
                 ('D:/SIDE-trivium', 'recut-trivium-b684r', 'v0.1.2'),
                 ('D:/SIDE-silence-principle', 'recut-silence-principle-b684r', 'v0.2.2'))
PREFIXES = ('push-b684', 'recut-')

NEXT = ('b686, the re-cut act: the licensed table`s next document and the three FOUNDATIONS cells regenerated at v0.2.2, its ruling then; '
        'b687 the research act, its candidate on the reading of (R295)(7); b690 the reading act, reading 3')

ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CLOSING-DRY-STEP', 'G-CITATION-CHECKED', 'G-R295-ENTERED', 'G-ROWGEN-STEPZERO', 'G-BRANCHES-BANKED',
            'G-DELETES-ONE-BRANCH', 'G-ANSWERS-CHECKED', 'G-RULES-BANKED', 'G-STATEMENT-BANKED', 'G-SEARCH-BANKED', 'G-PLAN-BEFORE-CONSTANTS',
            'G-COUNT-CONSTANTS', 'G-C1-STOP', 'G-C2-READ', 'G-LANDING', 'G-COUNT-TOOL-BANKS', 'G-TOOL-REPAIRS', 'G-PARTS-PRERUN',
            'G-DEFECTS-LETTERED')
STANDING_ADDED = ()         # ### (R295)'s N5: no standing arm added
SHARED_APPENDED = ('data/b670_work_orders.txt',)
PARTS = ('standing-a', 'standing-c', 'standing-b', 'act')     # ### data/b684_rules.txt row (1): the standing arms in three parts, the act's in one
SEALED = ('b685_worklist.py', 'b685_tests.py', 'b685_citation.py', 'b685_record.py', 'b685_checks.py', 'b685_closing.py', 'b685_reg_gate.py',
          'b685_regspec.py', 'b685_count.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
