# -*- coding: utf-8 -*-
"""b683_worklist.py -- THE ACT'S DATA, UNDER (R293). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b683: LANE TWO, ACT ONE HUNDRED AND TEN, THE RESEARCH ACT -- b682 AT ITS WEIGHT; THE DETECTION MAP IN THE ANGLE FORM OVER THE b681
### BALLS (W-ORD-MAP-ANGLE-FORM), ITS CONTROLS AND H3 AND H4 READ; THE 24 RULES SORTED AND THE TRACEABLE ONES ARMED ON THE AUTHOR'S WORD.
### No lean on this host. Written whole by the Write tool from b682_worklist.py's form.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'dc5613b'          # ### PLACE-papers main before the act (b682's record, pushed)
PRE_RELAY = 'fbc1053a'      # ### relay main before the act (b682's closing, pushed)
DATE = '2026-10-18'
SESSION_ID = 'df03c73f-520a-4848-85dc-8fada095f008'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R293) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b683_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B682_ENTRY = 9140           # ### FINDINGS: b682's entry head
B682_TRAIL = 14746          # ### OPEN_TRAILS: b682's trail record

# ### the branches step zero deletes ((R293)(7)), one per command, each its own message, in sequence; one remote branch named
KE = 'D:/SIDE-explicit-formula'
TB = 'D:/SIDE-bijection'
DELETE = (('D:/relay', ('push-b682-root', 'push-b682', 'push-b682-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b682-root', 'push-b682')),
          ('D:/SIDE-bijection', ('push-b682-main', 'push-b682-merge', 'recut-bijection-b682')))
DELETE_REMOTE = (('D:/SIDE-bijection', 'recut-bijection-b682', 'v0.2.1'),)
K_MAIN = '95f8dc8'

# ### the object ((R293)(2)): the order, the balls, the tool
ORDER = 'W-ORD-MAP-ANGLE-FORM'
ORDER_LINE = 14714
ORDER_FIRST = 14398
MAP_TOOL = 'tools/b677_epstein_map_angle.py'
MAP_RUN = 'tools/b683_epstein_map_angle.py'        # ### the wrapper: b677's map imported unchanged, its bank name and outputs pointed at b683
B667_MAP = 'tools/b667_epstein_map_balls.py'
BALLS = 'b681_epstein_zeros_narrowed.json'         # ### read with '.gz' appended, as b677's tool reads its bank
BALLS_GZ_SHA = 'f6613564e9d7fcd534534d0c33e418229bf32dbc0567c951ee8750438b11eb5a'
BALLS_JSON_SHA = 'c3b54356a1144ee50618fb714900dd4f982fd25a546a94f3100a176371269ce8'
B671_GZ_SHA = '51d9e6322510b738ba1332b1945bde75363a339f9fd567ea099bb675abd6f804'
B671_JSON_SHA = 'cd3a8ea1dcc7660c66a3b73a08d7c471ee6980e62e5bc4330e92e0c1b40e415b'
H_NEW, H_OLD = 1e-30, 1e-24
BAR = 2.0 ** -20
H_TOL64 = 3.162e-28                                # ### data/b677_tolerance.txt :90

# ### (R293)(6): the rules without arms
RULES_ARMS = 'b680_rules_arms.txt'
RULES_NONE = 24

NEXT = ('b684, the re-cut act: the licensed table`s next document, and the residues of b674, b676 and b678 read for whether a re-derived '
        'ACTION reaches them, its ruling then; b685 the research act, W-ORD-EPSTEIN-COUNT its candidate on the author`s placement, the Li-face '
        'test at Q0 becoming unconditional where it lands; b690 the reading act, reading 3')

ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CLOSING-DRY-STEP', 'G-CITATION-CHECKED', 'G-R293-ENTERED', 'G-ROWGEN-STEPZERO', 'G-BRANCHES-BANKED',
            'G-DELETES-ONE-BRANCH', 'G-ANSWERS-CHECKED', 'G-PLAN-BEFORE-RUN', 'G-CHAIN-BEFORE-BALLS', 'G-MAP-ROWS', 'G-ANGLE-POWERS',
            'G-HYPOTHESES-READ', 'G-ORDER-DISCHARGED', 'G-LANDING-BANKED', 'G-FORCED-RUNG-NAMED', 'G-ARMS-SORTED', 'G-ARMS-ON-WORD',
            'G-RULES-ARMS-REREAD', 'G-TOOL-REPAIRS', 'G-PARTS-PRERUN', 'G-DEFECTS-LETTERED')
# ### the author's word on (R293)(6)'s prompt (data/b683_author_answers.txt): twenty standing arms, tools/rule_arms.py's; N5 amended to them
STANDING_ADDED = ('G-RULE-PAIR-OF-READINGS', 'G-RULE-METHOD-READINESS', 'G-RULE-ROWGEN-REVIEW', 'G-RULE-TRIGGER-T1', 'G-RULE-TRIGGER-T2',
                  'G-RULE-TRIGGER-T3', 'G-RULE-TRIGGER-T5', 'G-RULE-DETACHED-PRINT', 'G-RULE-MIDACT-AFTER-ROOT', 'G-RULE-CONSUMER-TOLERANCE',
                  'G-RULE-SCORES-BEFORE-SEAL', 'G-RULE-DISPATCH-PER-TREE', 'G-RULE-WALK-TIP', 'G-RULE-ONE-GIT-WRITE', 'G-RULE-REMOTE-REREAD',
                  'G-RULE-TIE-BREAK', 'G-RULE-HEAD-LINE-QUOTED', 'G-RULE-CLOSING-DRY', 'G-RULE-LONG-PHASE-SPLIT', 'G-RULE-SUITE-PARTS')
SHARED_APPENDED = ('data/b670_work_orders.txt',)
PARTS = ('standing-a', 'standing-b', 'act')          # ### data/b678_rules.txt row 1
SEALED = ('b683_worklist.py', 'b683_tests.py', 'b683_citation.py', 'b683_record.py', 'b683_checks.py', 'b683_closing.py', 'b683_reg_gate.py',
          'b683_regspec.py', 'b683_epstein_map_angle.py', 'rule_arms.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
