# -*- coding: utf-8 -*-
"""b673_worklist.py -- THE ACT'S DATA, UNDER (R283). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b673: LANE TWO, ACT ONE HUNDRED, THE RESEARCH ACT -- b672 AT ITS WEIGHT; V4 AND V5 PLANNED WITH THEIR SIGNS AND CONSTANTS, THE
### CONSTANT CHECKED AT Q0, THE LEMMAS ATTEMPTED ON THE RUNNER, THE CONVERSES COMPOSED WHERE THEY LAND. No lean on this host; the kernel
### written only on its branch chi-li-b669 and on main by the merges of Component 4.
### Written whole by the Write tool from b672_worklist.py's form. The face is sealed after Components 1-4 and the dry-run step.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '8b85716'          # ### PLACE-papers main before the act (b672's record, pushed)
PRE_RELAY = 'db2b75f4'      # ### relay main before the act (b672's closing, pushed)
STEPZERO = '53aec8b0'       # ### relay: b672's closing push-out bank, the citation check, the ferry and its scan, the read-first bank
DATE = '2026-10-16'
SESSION_ID = 'b895aca8-50cf-4976-9217-c566f780a886'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R283) BEGIN'
# ### a continuation in a later session is named here with its first user line's words (b646 (e), b671 (i)); none yet
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b673_citation_check.txt'

# ### the ledger lines this act's record lines are placed by (read at step zero, relay data/b673_citation_check.txt)
B672_ENTRY = 8791           # ### FINDINGS: b672's entry head
B672_TRAIL = 14454          # ### OPEN_TRAILS: b672's trail record
OPEN_CONVERSE = 14334       # ### OPEN_TRAILS: b669's trail line naming W-ORD-LI-CONVERSE-NATIVE, its trigger "S5 DERIVES"

# ### the kernel this act writes: SIDE-explicit-formula, on its branch, then main by the merges of Component 4 alone
KE = 'D:/SIDE-explicit-formula'
KD = KE
KERNEL = 'SIDE-explicit-formula'
OPEN_BRANCH, OPEN_TIP = 'chi-li-b669', 'b804bf2'
LAST_TAG, NEXT_TAG = 'v0.31', 'v0.32'
MATHLIB = 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11'
CONVERSE_FILE = 'SIDEExplicitFormula/Schema/LiConverseCfg.lean'
V4_LINE, V5_LINE, S5_LINE, S6_LINE = 129, 139, 145, 159
# ### the last merged run, b669's, which the standing runner arms read until this act's run lands (carried from b672_worklist.py unchanged)
K_WORKFLOW = '7317db4'
RUNNER = {KERNEL: dict(branch='chi-li-forward-b669', target='SIDEExplicitFormula.Schema.LiCfg SIDEExplicitFormula.Chi.LiForward',
                       workflow_commit=K_WORKFLOW, run_id=38607173157, ref='5a194fc9cafe8274bdeebe804f92d6e8a8b387f7', dispatched_at='main',
                       prior_run=38606143304, prior_ref='b804bf2b682b31aea7fe48ac214e040082703cfc')}
RUNNER_ROWS, RUNNER_BANK = 'b669_runner_rows.json', 'b669_runner_SIDE-explicit-formula_run38607173157.txt'
PRINT_TARGETS_N = 5

# ### the control's input ((R283)(4)): b671's narrowed balls, read through gzip, never written
Q0_NARROWED = 'b671_epstein_zeros_narrowed.json.gz'
Q0_NARROWED_SHA = '51d9e6322510b738ba1332b1945bde75363a339f9fd567ea099bb675abd6f804'
Q0_NARROWED_JSON_SHA = 'cd3a8ea1dcc7660c66a3b73a08d7c471ee6980e62e5bc4330e92e0c1b40e415b'
CONTROL_N = 4000

# ### filled at the seal
ACT_ARMS = ()
SHARED_APPENDED = ()
SEALED = ('b673_worklist.py', 'b673_tests.py', 'b673_citation.py', 'b673_record.py', 'b673_checks.py', 'b673_closing.py', 'b673_reg_gate.py',
          'b673_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
