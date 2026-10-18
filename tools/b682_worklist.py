# -*- coding: utf-8 -*-
"""b682_worklist.py -- THE ACT'S DATA, UNDER (R292). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b682: LANE TWO, ACT ONE HUNDRED AND NINE, THE RE-CUT ACT -- b681 AT ITS WEIGHT; THE CORRESPONDENCE READER EXTENDED TO THE RUNNER
### PRINT BANKS AND THE CELLS REGENERATED (W-ORD-CORRESPONDENCE-RUNNER-BANKS); THE LICENSED TABLE'S NEXT DOCUMENT CUT.
### No lean on this host. Written whole by the Write tool from b681_worklist.py's form.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '837ba79'          # ### PLACE-papers main before the act (b681's record, pushed)
PRE_RELAY = 'f17fef29'      # ### relay main before the act (b681's closing, pushed)
DATE = '2026-10-18'
SESSION_ID = 'df03c73f-520a-4848-85dc-8fada095f008'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R292) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b682_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B681_ENTRY = 9110           # ### FINDINGS: b681's entry head
B681_TRAIL = 14716          # ### OPEN_TRAILS: b681's trail record

# ### the branches step zero deletes ((R292)(6)), one per command, in sequence; no remote branch named
KE = 'D:/SIDE-explicit-formula'
DELETE = (('D:/relay', ('push-b681-root', 'push-b681', 'push-b681-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b681-root', 'push-b681')))
DELETE_REMOTE = ()
K_MAIN = '95f8dc8'

# ### the object ((R292)(2)): the order, the five cells, the generator
ORDER = 'W-ORD-CORRESPONDENCE-RUNNER-BANKS'
ORDER_LINE = 14648
CARRIED_LINE = 14620
GEN = 'tools/correspondence_gen.py'
GEN_TEST = 'tools/test_correspondence_gen.py'
FOUNDATIONS = 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md'
FOUNDATIONS_COPY = 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md'
FIVE = (628, 629, 630)
RUNNER_KERNELS = (('SIDE-window', 'v0.5.1', 'b674'), ('SIDE-trivium', 'v0.1.1', 'b676'), ('SIDE-silence-principle', 'v0.2.1', 'b678'))

NEXT = ('b683, the research act: the map in the angle form over the b681 balls under W-ORD-MAP-ANGLE-FORM, its plan to read '
        'data/b677_map_plan.txt, data/b677_tolerance.txt and data/b681_narrow.txt before any run; W-ORD-EPSTEIN-COUNT the alternative on the '
        'author’s placement; the 24 rules without arms held for the author’s decision')

ACT_ARMS = ()               # ### filled at Component 5, each arm run at HEAD and counted before it is declared
STANDING_ADDED = ()         # ### (R292)'s N5: no standing arm added
SHARED_APPENDED = ('data/b670_work_orders.txt',)
PARTS = ('standing-a', 'standing-b', 'act')          # ### data/b678_rules.txt row 1
SEALED = ('b682_worklist.py', 'b682_tests.py', 'b682_citation.py', 'b682_record.py', 'b682_checks.py', 'b682_closing.py', 'b682_reg_gate.py',
          'b682_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
