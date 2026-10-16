# -*- coding: utf-8 -*-
"""b672_worklist.py -- THE ACT'S DATA, UNDER (R282). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b672: LANE THREE, ACT NINETY-NINE, THE TOOLING ACT -- b671 AT ITS WEIGHT; THREE RULES ENTERED; THE CORRESPONDENCE GENERATOR
### WRITTEN, TESTED ON PLANTED CASES AND RUN OVER THE ROSTER; THE COPY OF RECORD AS REGISTRY NAMES IT, NOTHING MOVED (THE NAVIGATOR'S
### ANSWER ON THE REGISTRY); THE MIRROR EXPORT. NO KERNEL EDIT.
### Written whole by the Write tool from b671_worklist.py's form. The face is sealed after Components 1-3 and the dry-run step.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'd6d2d4b'          # ### PLACE-papers main before the act (b671's record, pushed)
PRE_RELAY = '64158393'      # ### relay main before the act (b671's closing, pushed)
STEPZERO = '3176a028'       # ### relay: b671's closing push-out bank, the citation check, the ferry and its scan, the defects bank, the citation tool
DATE = '2026-10-16'
SESSION_ID = 'b895aca8-50cf-4976-9217-c566f780a886'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R282) BEGIN'
# ### a continuation in a later session is named here with its first user line's words (b646 (e), b671 (i)); none yet
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b672_citation_check.txt'

# ### the ledger lines this act's record lines are placed by (read at step zero, relay data/b672_citation_check.txt)
B671_ENTRY = 8761           # ### FINDINGS: b671's entry head
B671_TRAIL = 14412          # ### OPEN_TRAILS: b671's trail record
CENSUS_ITEMS = 14386        # ### OPEN_TRAILS: b671's census items with W-ORD-ONE-COPY, item (b)

# ### the kernels this act reads and does not write
KE = 'D:/SIDE-explicit-formula'
OPEN_BRANCH, OPEN_TIP = 'chi-li-b669', 'b804bf2'

# ### the last merged run, b669's, which the standing runner arms read: no build in this act (carried from b671_worklist.py unchanged)
KERNEL = 'SIDE-explicit-formula'
NEXT_TAG = 'v0.31'
K_WORKFLOW = '7317db4'
RUNNER = {KERNEL: dict(branch='chi-li-forward-b669', target='SIDEExplicitFormula.Schema.LiCfg SIDEExplicitFormula.Chi.LiForward',
                       workflow_commit=K_WORKFLOW, run_id=38607173157, ref='5a194fc9cafe8274bdeebe804f92d6e8a8b387f7', dispatched_at='main',
                       prior_run=38606143304, prior_ref='b804bf2b682b31aea7fe48ac214e040082703cfc')}
RUNNER_ROWS, RUNNER_BANK = 'b669_runner_rows.json', 'b669_runner_SIDE-explicit-formula_run38607173157.txt'
PRINT_TARGETS_N = 5
KD = KE

# ### the object (R282)(3): the roster's tables -- b586's 19 with a table (b670's reading (ii)) and E_DIFFICULTY_THEOREM's (v1.0.4 :327)
ROSTER_BANK = 'b586_corroboration.txt'
READING_II = 'b670_correspondence.txt'
STATE = 'b670_state.txt'

# ### the generator's commits, each the tool and its test alone (or the tool alone), committed before the run ((R282)(4))
GEN_COMMITS = ('944affbd', '05e8af50', 'a3082922')
GEN_FILES = ('tools/correspondence_gen.py', 'tools/test_correspondence_gen.py')
GEN_FILES_BASE = ('correspondence_gen.py', 'test_correspondence_gen.py')
# ### the PLACE-papers files this act writes beyond FINDINGS and OPEN_TRAILS: the roster's files the generator wrote (relay
# ### data/b672_correspondence_diff.json), the partner written identically, and b651's line carried to SIMPLICITY's v1.1.3 ((R282)(5))
B651_COPY = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md'
B651_SOURCE = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md'
NEXT = 'b673 V4 and V5 on chi-li-b669; b674 the re-cut act between SIDE-window and SIDE-trivium by the tie rule -- `(R282)`(10)'

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm is a standing arm carried from b671's face (b671's own act arms
# ### not carried). Each run at HEAD and counted before the face names it.
ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-MIDACT-CHECKED', 'G-R282-ENTERED', 'G-OPEN-BRANCH-KEPT', 'G-RULES-ENTERED',
            'G-LEDGER-SPLIT-ITEM', 'G-GEN-PLANTED', 'G-GEN-COMMITTED-ALONE', 'G-ROSTER-READ', 'G-ONE-COPY-LIST', 'G-GEN-RUN',
            'G-GEN-IDENTICAL-RERUN', 'G-ROWS-KEPT', 'G-READING-II-AFTER', 'G-STATE-LINE', 'G-ORDERS-ENTERED', 'G-B651-LINE',
            'G-NOTHING-MOVED', 'G-HYPOTHESES-SCORED')
B671_ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-MIDACT-CHECKED', 'G-SEQUENCE-ENTERED', 'G-CENSUS-ITEMS', 'G-PLAN-BEFORE-NUMBER',
                 'G-CONTROLS-FIRST', 'G-NARROWED-LIST', 'G-NARROW-LOG', 'G-CARRY-DIFF', 'G-MAP-DIFF', 'G-MAP-READ', 'G-HYPOTHESES-SCORED',
                 'G-LANDING', 'G-TIE-DIAGNOSTIC', 'G-B667-UNEDITED', 'G-OPEN-BRANCH-KEPT', 'G-R281-ENTERED')
SHARED_APPENDED = ('data/b670_state.txt',)   # ### (R282)(6) H5's dated line
SEALED = ('b672_worklist.py', 'b672_tests.py', 'b672_citation.py', 'b672_record.py', 'b672_checks.py', 'b672_closing.py', 'b672_reg_gate.py',
          'b672_regspec.py', 'correspondence_gen.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
