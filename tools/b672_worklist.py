# -*- coding: utf-8 -*-
"""b672_worklist.py -- THE ACT'S DATA, UNDER (R282). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b672: LANE THREE, ACT NINETY-NINE, THE TOOLING ACT -- b671 AT ITS WEIGHT; TWO RULES ENTERED (THREE ROWS); THE CORRESPONDENCE
### GENERATOR WRITTEN, TESTED ON PLANTED CASES AND RUN OVER THE ROSTER; THE ONE COPY OF RECORD RULED AND THE SUPERSEDED COPIES MOVED; THE
### MIRROR EXPORT. NO KERNEL EDIT.
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

# ### filled at the seal
ACT_ARMS = ()
SHARED_APPENDED = ('data/b670_state.txt',)   # ### (R282)(6) H5's dated line
SEALED = ('b672_worklist.py', 'b672_tests.py', 'b672_citation.py', 'b672_record.py', 'b672_checks.py', 'b672_closing.py', 'b672_reg_gate.py',
          'b672_regspec.py', 'correspondence_gen.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
