# -*- coding: utf-8 -*-
"""b671_worklist.py -- THE ACT'S DATA, UNDER (R281). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b671: LANE TWO, ACT NINETY-EIGHT, THE RESEARCH ACT -- b670 AT ITS WEIGHT; THE SEQUENCE LINE AND ITS FIVE TRIGGERS ENTERED; THE
### THREE CENSUS ITEMS; W-ORD-EPSTEIN-BALL-WIDTH: Q0'S 163 POINTS NARROWED TO THE MAP'S INPUT WIDTH (THE ON-LINE AT σ = ½ BY A CERTIFIED SIGN
### CHANGE OF Λ_Q, THE OFF-LINE BY BISECTION ON THE COUNT), THE CONTROLS, THE b663 CONTROL RUN ONCE ON THE NARROWED BALLS. NO KERNEL EDIT.
### Written whole by the Write tool from b670_worklist.py's form. The face is sealed after Components 1-5 and the dry-run step.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'c740f56'          # ### PLACE-papers main before the act (b670's record, pushed)
PRE_RELAY = '87410d3c'      # ### relay main before the act (b670's closing, pushed)
STEPZERO = 'a8d58d46'       # ### relay: b670's closing push-out bank, the citation check, the ferry and its scan, the defects bank, the citation tool
DATE = '2026-10-14'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
HOLD = 2560
SESSION_ID = '96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf'
ANCHOR = 'RULING (R281) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b671_citation_check.txt'

# ### the ledger lines this act's record lines are placed by (read at step zero, relay data/b671_citation_check.txt)
B670_ENTRY = 8733           # ### FINDINGS: b670's entry head
B670_TRAIL = 14360          # ### OPEN_TRAILS: b670's trail record
RESEARCH_ORDER = 14294      # ### OPEN_TRAILS: the research order after b668 -- the sequence line beneath it, (R281)(2)
CERTIFY, BALL_WIDTH, KERNEL_ITEM = 14158, 14264, 14266   # ### OPEN_TRAILS: W-ORD-EPSTEIN-CERTIFY, its control half, the kernel item for P1/P2

# ### the kernels this act reads and does not write
KE = 'D:/SIDE-explicit-formula'
OPEN_BRANCH, OPEN_TIP = 'chi-li-b669', 'b804bf2'

# ### the object (R281)(3): b667's certified squares, read and never written
Q0_CERT = 'b667_epstein_zeros_certified.json.gz'
Q0_ON_N, Q0_OFF_N = 146, 17

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm is a standing arm carried from b670's face (b670's own act arms
# ### not carried). Each run at HEAD and counted before the face names it. Filled at Component 6.
ACT_ARMS = ()
B670_ACT_ARMS = ('G-R280-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-MIDACT-CHECKED', 'G-TEN-ACTS-CITED', 'G-DEFECTS-BY-KIND',
                 'G-SWEEP-BANKED', 'G-LICENSED-TABLE', 'G-CORRESPONDENCE-READ', 'G-CEILING-EQUAL', 'G-QUEUE-READ', 'G-STATE-LINE', 'G-METHODS-TABLE',
                 'G-ZFR-ONE-REQUEST', 'G-ITEMS-ENTERED', 'G-OPEN-BRANCH-KEPT', 'G-TECHNE-WITHHELD')
SEALED = ('b671_worklist.py', 'b671_tests.py', 'b671_citation.py', 'b671_record.py', 'b671_checks.py', 'b671_closing.py', 'b671_reg_gate.py',
          'b671_regspec.py', 'b671_narrow.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
