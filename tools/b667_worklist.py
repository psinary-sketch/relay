# -*- coding: utf-8 -*-
"""b667_worklist.py -- THE ACT'S DATA, UNDER (R277). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b667: LANE TWO, ACT NINETY-FOUR, THE RESEARCH ACT -- b666 AT ITS WEIGHT; THE EVALUATION ROUTE RAISED IN A PLAN; Q0'S ZEROS BELOW 150
### ISOLATED IN BALLS, THE LIST'S COMPLETENESS COUNTED, THE b663 CONTROL RE-RUN ON THE BALLS.
### Written whole by the Write tool from b666_worklist.py's form. No kernel is edited this act and no runner is dispatched: the kernel
### constants of b666 are not carried. The face is sealed after Components 1-5 and the dry-run step.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EF = 'D:/SIDE-explicit-formula'
PRE_PP = 'c143bcb'          # ### PLACE-papers main before the act (b666's record, pushed)
PRE_RELAY = 'd43a72f9'      # ### relay main before the act (b666's closing, pushed)
STEPZERO = 'bd6f388d'       # ### relay: b666's closing push-out bank, the citation check, the ferry and its scan
DATE = '2026-10-13'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
SESSION_ID = '96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf'
ANCHOR = 'RULING (R277) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b667_citation_check.txt'

# ### the ledger lines this act's record lines are placed by (read at step zero, relay data/b667_citation_check.txt)
B666_ENTRY = 8621           # ### FINDINGS: b666's entry head
B666_TRAIL = 14240          # ### OPEN_TRAILS: b666's trail record
ORDER = 14158               # ### OPEN_TRAILS: W-ORD-EPSTEIN-CERTIFY (b663), placed at :14188 by b664

# ### the object ((R277)(2)): the bench's list, read and never written
Q0_ON, Q0_OFF = 'b326_epstein_zeros.json', 'b326_offline.json'
B326_BANKS = ('data/b326_epstein_zeros.json', 'data/b326_offline.json')
CONTROL_BANK = 'data/b663_epstein_control.txt'
PLAN_BANK = 'data/b667_epstein_plan.txt'

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm of the suite is a standing arm carried from b666's face
# ### (b666's own act arms not carried). Each run at HEAD and counted before the face names it. Filled at Component 6.
ACT_ARMS = ('G-R277-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-PLAN-BEFORE-NUMBER', 'G-OBSTRUCTIONS-BANKED', 'G-ROUTE-CHECKS',
            'G-CONTROLS-FIXED', 'G-SQUARES-CERTIFIED', 'G-REGION-COUNTED', 'G-MAP-ON-BALLS', 'G-LANDING-DATED', 'G-B326-UNTOUCHED', 'G-RUNS-BANKED')
B666_ACT_ARMS = ('G-R276-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-TIE-RULE-ENTERED', 'G-KERNEL-NAMED', 'G-SENTENCES-BANKED',
                 'G-GRADES-VERBATIM', 'G-AXIOM-ROW-CELL', 'G-PROMPT-BEFORE-CUT', 'G-CUT-COMMITS', 'G-CUT-REGRADE', 'G-AXIOM-CLAIM-AFTER',
                 'G-KERNEL-FILES-FROM-BANK')
SEALED = ('b667_worklist.py', 'b667_tests.py', 'b667_citation.py', 'b667_record.py', 'b667_checks.py', 'b667_closing.py', 'b667_reg_gate.py',
          'b667_regspec.py', 'b667_epstein_certify.py', 'b667_epstein_map_balls.py')

# ### THE RUNNER ARMS, STANDING: no dispatch this act, so they read the latest dispatch's bank and the kernel it merged (b661's precedent,
# ### which read b658's runner rows): b666's run on SIDE-cosmo, its workflow, its print list and its merge, as relay data/b666_runner_rows.json
# ### and data/b666_runner_SIDE-cosmo.txt bank them -- the state those arms find unchanged.
KERNEL = 'SIDE-cosmo'
KD = 'D:/SIDE-cosmo'
RUNNER = {KERNEL: dict(branch='docstrings-cut-SIDE-cosmo', target='SIDECosmo', workflow_commit='f5d8c7d', run_id=38471056772,
                       ref='1ddeb7c28d0833ea63011460d861ef196646ab64', dispatched_at='main', prior_run=38470740945)}
RUNNER_ROWS, RUNNER_BANK = 'b666_runner_rows.json', 'b666_runner_SIDE-cosmo.txt'
PRINT_TARGETS_N = 53
NEXT_TAG = 'v0.3.1'


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
