# -*- coding: utf-8 -*-
"""b687_worklist.py -- THE ACT'S DATA, UNDER (R297). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b687: LANE TWO, ACT ONE HUNDRED AND FOURTEEN, THE RESEARCH ACT -- b686 AT ITS WEIGHT; THE DERIVATION OF b685 TESTED AT MATCHED RANGE,
### IN THE JENSEN DISC, AND AT EVERY INTERMEDIATE STEP, FOR ζ AND FOR Z_Q.
### No lean on this host. Written whole by the Write tool from b686_worklist.py's form. A new session opens the act (a90bcdb6), so SESSION_ID
### is this session's and no session follows it.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '9b9a7c6'          # ### PLACE-papers main before the act (b686's record, pushed)
PRE_RELAY = '3e547498'      # ### relay main before the act (b686's closing, pushed)
DATE = '2026-10-18'
SESSION_ID = 'a90bcdb6-256f-4841-97ff-9638e378446c'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R297) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b687_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B686_ENTRY = 9260           # ### FINDINGS: b686's entry head
B686_TRAIL = 14862          # ### OPEN_TRAILS: b686's trail record
B685_ENTRY = 9228           # ### FINDINGS: b685's entry head (the derivation under test)
ORDER_LINE = 14832          # ### OPEN_TRAILS: W-ORD-EPSTEIN-COUNT's re-dating line, its trigger the readings

# ### the branches step zero deletes ((R297)(6)), one per command, each its own message, in sequence
SPINOR = 'D:/SIDE-spinor'
DELETE = (('D:/relay', ('push-b686-root', 'push-b686', 'push-b686-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b686-root', 'push-b686')),
          (SPINOR, ('push-b686-main', 'push-b686-merge', 'recut-spinor-b686')))
DELETE_REMOTE = ((SPINOR, 'recut-spinor-b686'),)
SPINOR_TAG = 'v0.1.1'

# ### (R297)(2)-(3): the derivation under test and its inputs
COUNT_PLAN = 'data/b685_count_plan.txt'
COUNT_TOOL = 'tools/b685_count.py'
COUNT_PARTS = ('data/b685_count_part1.json', 'data/b685_count_part2.json', 'data/b685_count_part4.json')
Q0_BALLS = 'data/b681_epstein_zeros_narrowed.json.gz'
Q0_BALLS_HASHES = 'data/b681_epstein_zeros_narrowed_hashes.txt'
HEIGHTS_Z = (100, 1000, 10000)
HEIGHTS_Q = (50, 100, 149)
HEIGHTS_MATCHED = ('e', 10, 100)
JENSEN = ('1.7', '2.05')    # ### (R297)(3)(ii): the centre's real part and the radius
P3_WORDS = ('DERIVED — constants certified in balls, analytic steps sourced by line, intermediate inequalities checked against computed values '
            'at sample heights, the ζ instance inside the located bounds at matched range, not compiled')

NEXT = ('b688, the re-cut act, with the licensed table`s next document and R4 (SpinorLeg.lean :21) re-derived in b684`s form, its ruling then; '
        'b689 the research act, its candidate on (R297)(5)`s landing; b690 the reading act, reading 3')

ACT_ARMS = ()               # ### written at Component 4, after the readings
STANDING_ADDED = ()         # ### (R297)'s N5: no standing arm added
SHARED_APPENDED = ('data/b670_work_orders.txt',)    # ### (R297)(5): the two order rows, appended (additive, (R254)(2))
PARTS = ('standing-a', 'standing-c', 'standing-b', 'act')     # ### data/b684_rules.txt row (1): the standing arms in three parts, the act's in one
SEALED = ('b687_worklist.py', 'b687_tests.py', 'b687_citation.py', 'b687_record.py', 'b687_checks.py', 'b687_closing.py', 'b687_reg_gate.py',
          'b687_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
