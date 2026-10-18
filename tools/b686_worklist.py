# -*- coding: utf-8 -*-
"""b686_worklist.py -- THE ACT'S DATA, UNDER (R296). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b686: LANE TWO, ACT ONE HUNDRED AND THIRTEEN, THE RE-CUT ACT -- b685 AT ITS WEIGHT; THE LICENSED TABLE'S NEXT DOCUMENT CUT BY THE
### b670 METHOD; THE THREE FOUNDATIONS CELLS REGENERATED AT v0.2.2; THE N4 SCORER'S CIRCULARITY REPAIRED AT CARRY.
### No lean on this host. Written whole by the Write tool from b684_worklist.py's and b685_worklist.py's forms. A new session opens the act
### (3bd076e1), so SESSION_ID is this session's and no session follows it.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'd201ac8'          # ### PLACE-papers main before the act (b685's record, pushed)
PRE_RELAY = '5c051335'      # ### relay main before the act (b685's closing, pushed)
DATE = '2026-10-18'
SESSION_ID = '3bd076e1-80b3-48c6-919f-407447a1df25'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R296) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b686_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B685_ENTRY = 9228           # ### FINDINGS: b685's entry head
B685_TRAIL = 14834          # ### OPEN_TRAILS: b685's trail record

# ### the branches step zero deletes ((R296)(5)), one per command, each its own message, in sequence
KE = 'D:/SIDE-explicit-formula'
DELETE = (('D:/relay', ('push-b685-root', 'push-b685', 'push-b685-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b685-root', 'push-b685')))
DELETE_REMOTE = ()
K_MAIN = '95f8dc8'

# ### (R296)(4): the licensed table's next document, named by b652's order and b674's tie-break
RULES_BANK, TIE_RULE_ROW = 'b674_rules.txt', 2
TABLE_BANK, KERNELS_BANK = 'b670_licensed_table.txt', 'b647_table_kernels.txt'
CUT_SINCE = (('SIDE-window', 'data/b684_cut.txt', 'SIDE-window'), ('SIDE-trivium', 'data/b684_cut.txt', 'SIDE-trivium'),
             ('SIDE-silence-principle', 'data/b684_cut.txt', 'SIDE-silence-principle'), ('SIDE-bijection', 'data/b682_cut.txt', 'SIDE-bijection'),
             ('SIDE-class-number-anomaly', 'data/b684_cut.txt', 'SIDE-class-number-anomaly'))

# ### (R296)(3): the three FOUNDATIONS cells, the generator's input at v0.2.2
FOUND = 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md'
FOUND_LINES = (628, 629, 630)
SILENCE_TAG = 'v0.2.2'
SILENCE_PRINTS = 'data/b684_axioms_SIDE-silence-principle_after.txt'
DIFF_STEM = 'b686_correspondence_diff'
B682_DISTANCE = (55, 0)     # ### b682's distance by b670's method and by the generator's (data/b682_cut.txt)

NEXT = ('b687, the research act on W-ORD-EPSTEIN-COUNT`s three readings as OPEN_TRAILS :14832 states them, its ruling then, its plan to read '
        'data/b685_count_plan.txt and data/b685_count_controls.txt before any reading; b690 the reading act, reading 3')

ACT_ARMS = ()               # ### set at carry time (Component 4), each run at HEAD before the face names it
STANDING_ADDED = ()         # ### (R296)'s N5: no standing arm added
SHARED_APPENDED = ()
PARTS = ('standing-a', 'standing-c', 'standing-b', 'act')     # ### data/b684_rules.txt row (1): the standing arms in three parts, the act's in one
SEALED = ('b686_worklist.py', 'b686_tests.py', 'b686_citation.py', 'b686_record.py', 'b686_checks.py', 'b686_closing.py', 'b686_reg_gate.py',
          'b686_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
