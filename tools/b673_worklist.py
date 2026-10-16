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
# ### the workflow file's commit on main: 7317db4 put it where absent, the file alone (b654); the standing runner arms read it so
K_WORKFLOW = '7317db4'
# ### the last merged run, from Component 3-4: this act's run 38960681935 at the branch tip 5050a46, merged at e36ea31, tag v0.32; the
# ### three earlier runs of the attempt each at its own tip (data/b673_runner_rows.json; data/b673_defects.txt (l))
TIP = '5050a46acf269e7745ce678c3deb8deed9f2d0bf'
MERGE = 'e36ea316e363b1fad04b7fa9def0fc7f2e78188f'
RUNS = ((38957029697, '516803e6557703cb225bba30e4c1ac28ae1c396f'), (38958296252, 'b1d4342559f7725028f8a139ff47a235e2c66c29'),
        (38959501957, '921fb71e6c6952b2f7ac8a3e09305170cba4ceda'), (38960681935, TIP))
FIRST_KERNEL_COMMIT = '25c360b'     # ### the first Lean commit of the attempt: after the plan, the prompt and the control
RUNNER = {KERNEL: dict(branch=OPEN_BRANCH, target='SIDEExplicitFormula.Schema.LiCfg SIDEExplicitFormula.Chi.LiForward '
                                                  'SIDEExplicitFormula.Schema.PowerSum SIDEExplicitFormula.Schema.LiRemainder '
                                                  'SIDEExplicitFormula.Schema.LiConverseCfg SIDEExplicitFormula.LiConverseNative',
                       workflow_commit=K_WORKFLOW, run_id=38960681935, ref=TIP, dispatched_at='main',
                       prior_run=38959501957, prior_ref='921fb71e6c6952b2f7ac8a3e09305170cba4ceda')}
RUNNER_ROWS, RUNNER_BANK = 'b673_runner_rows.json', 'b673_runner_SIDE-explicit-formula_run38960681935.txt'
PRINT_TARGETS_N = 29
LANDED = 29

# ### the control's input ((R283)(4)): b671's narrowed balls, read through gzip, never written
Q0_NARROWED = 'b671_epstein_zeros_narrowed.json.gz'
Q0_NARROWED_SHA = '51d9e6322510b738ba1332b1945bde75363a339f9fd567ea099bb675abd6f804'
Q0_NARROWED_JSON_SHA = 'cd3a8ea1dcc7660c66a3b73a08d7c471ee6980e62e5bc4330e92e0c1b40e415b'
CONTROL_N = 4000

NEXT = ('b674, the re-cut act between SIDE-window and SIDE-trivium -- `(R283)`(9)')

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm is a standing arm carried from b672's face (b672's own act
# ### arms not carried). Each run at HEAD and counted before the face names it.
ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-MIDACT-CHECKED', 'G-R283-ENTERED', 'G-CONTROL-BEFORE-LEAN',
            'G-PLAN-SIGN-FIRST', 'G-PROMPT-BEFORE-LEAN', 'G-RUNS-BY-TIP', 'G-LANDING', 'G-WALK-ZERO', 'G-H5-SIDE-BY-SIDE',
            'G-CONVERSE-DISCHARGED', 'G-RULES-BANKED', 'G-LANDING-DRAFTS', 'G-HYPOTHESES-SCORED', 'G-BRANCH-MERGED')
B672_ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-MIDACT-CHECKED', 'G-R282-ENTERED', 'G-OPEN-BRANCH-KEPT', 'G-RULES-ENTERED',
                 'G-LEDGER-SPLIT-ITEM', 'G-GEN-PLANTED', 'G-GEN-COMMITTED-ALONE', 'G-ROSTER-READ', 'G-ONE-COPY-LIST', 'G-GEN-RUN',
                 'G-GEN-IDENTICAL-RERUN', 'G-ROWS-KEPT', 'G-READING-II-AFTER', 'G-STATE-LINE', 'G-ORDERS-ENTERED', 'G-B651-LINE',
                 'G-NOTHING-MOVED', 'G-HYPOTHESES-SCORED')
SHARED_APPENDED = ()
SEALED = ('b673_worklist.py', 'b673_tests.py', 'b673_citation.py', 'b673_record.py', 'b673_checks.py', 'b673_closing.py', 'b673_reg_gate.py',
          'b673_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
