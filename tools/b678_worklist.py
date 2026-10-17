# -*- coding: utf-8 -*-
"""b678_worklist.py -- THE ACT'S DATA, UNDER (R288). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b678: LANE TWO, ACT ONE HUNDRED AND FIVE, THE RE-CUT ACT -- b677 AT ITS WEIGHT; THE Q0 LINES ANSWERED BY ONE GENERATED CORRIGENDUM
### ENTRY; THE LICENSED TABLE'S NEXT DOCUMENT CUT.
### No lean on this host. Written whole by the Write tool from b677_worklist.py's form. The face is sealed after Components 1-3, the
### closing dry-run and the entry dry-run step.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'f614597'          # ### PLACE-papers main before the act (b677's record, pushed)
PRE_RELAY = 'da8a46bc'      # ### relay main before the act (b677's closing, pushed)
DATE = '2026-10-17'
SESSION_ID = 'df03c73f-520a-4848-85dc-8fada095f008'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R288) BEGIN'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b678_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B677_ENTRY = 8943           # ### FINDINGS: b677's entry head
B677_TRAIL = 14592          # ### OPEN_TRAILS: b677's trail record
B675_FINDING = 8881         # ### FINDINGS: b675's finding, the corrigendum's citation
Q0_ORDER_LINE = 14556       # ### OPEN_TRAILS: W-ORD-Q0-CLASS-LINES

# ### the branches step zero deletes ((R288)(4)), one per command, no glob in any half
DELETE = (('D:/relay', ('push-b677', 'push-b677-root', 'push-b677-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b677', 'push-b677-root')))
DELETE_REMOTE = ()

KE = 'D:/SIDE-explicit-formula'
KREV = 'e36ea31'
STRIP_FIELD = ('Zeta23/Defs.lean', 142)

# ### the next document ((R288)(3)): named by b652's order (the next kernel by descending count, data/b652_ferry.txt :19) and, at the tie of
# ### SIDE-bijection and SIDE-silence-principle at 4, by data/b674_rules.txt row 2 (rows outside of any kind equal at 4; the larger table)
TABLE_BANK, KERNELS_BANK, RULES_BANK, TIE_RULE_ROW = 'b670_licensed_table.txt', 'b647_table_kernels.txt', 'b674_rules.txt', 2
CUT_SINCE = (('SIDE-window', 'b674_cut.txt', 'THE DISTANCE BEFORE 5, AFTER 1'), ('SIDE-trivium', 'b676_cut.txt', 'THE DISTANCE BEFORE 5, AFTER 1'))
TD = 'D:/SIDE-silence-principle'
CANDIDATE = 'SIDE-silence-principle'
T_PRE_MAIN = '667c254'                          # ### its main at the read pin, = tag v0.2.0
T_LAST_TAG, T_NEXT_TAG = 'v0.2.0', 'v0.2.1'
T_BRANCH = 'recut-silence-principle-b678'
T_TARGET = 'SIDESilencePrinciple'
T_FILE = 'SIDESilencePrinciple/Basic.lean'
T_CUT_FILES = (T_FILE,)
T_WORKFLOW, T_MAIN, T_CUT = '5d2e587', '6968b6c', '8829bcc'    # ### the workflow alone, the print list alone (main), the cut (the branch)
T_MERGE = None                                                  # ### filled at the merge
T_RUNS = ((39055170313, 'before'), (39055212218, 'after'))     # ### one dispatch per tree state, read by its run id

NEXT = ('b679, the research act, the strip variant its object, with data/b676_strip_uses.txt (22 uses) and LiConverseCfg.lean :231 (the point '
        '1/(1 − R) excluded once R > 3) as its readfirst, its ruling then; b680 the reading act, reading 2 of 2, with the ledger split archive-3 and '
        'the census of the suite`s arms by what each reads; b681 the narrowing act under W-ORD-EPSTEIN-BALL-WIDTH at the width b677 measured, its '
        'candidate -- `(R288)`(7)')

# ### (R264)(2), the freeze: filled at Component 4
ACT_ARMS = ()
SHARED_APPENDED = ()
PARTS = ('standing-a', 'standing-b', 'act')      # ### (R288)(1): the standing arms in two foreground parts, the act's in one
LEFT = (('D:/relay', ()), ('D:/MY-DOwnloads/PLACE-papers', ()))
SEALED = ('b678_worklist.py', 'b678_tests.py', 'b678_citation.py', 'b678_record.py', 'b678_checks.py', 'b678_closing.py', 'b678_reg_gate.py',
          'b678_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
