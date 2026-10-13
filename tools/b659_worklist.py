# -*- coding: utf-8 -*-
"""b659_worklist.py -- THE ACT'S DATA, UNDER (R269). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b659: LANE THREE, ACT EIGHTY-SIX, THE RE-CUT ACT -- b658 AT ITS WEIGHT; THE NEXT KERNEL'S SENTENCES GRADED, CUT, BUILT ON THE RUNNER
### AND MERGED; THE MAP RE-ENTERED; THE MIRROR EXPORT.
### Written whole by the Write tool from b657_worklist.py's and b658_worklist.py's forms. The face is sealed after Components 1-3 and the
### dry-run step; these tools are sealed at Component 4.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '5871eaa'          # ### PLACE-papers main before the act (b658's record, pushed)
PRE_RELAY = '8b7d2901'      # ### relay main before the act (b658's closing, pushed)
STEPZERO = 'd75be0e6'       # ### relay: b658's closing push-out bank, committed at step zero with the ferry
DATE = '2026-10-13'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
HOLD = 2560
SESSION_ID = '96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf'
ANCHOR = 'RULING (R269) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R269)(2): the kernel, 13 OVERREACHES at relay data/b647_table_kernels.txt :22, the next after SIDE-kernel (114), SIDE-global-section (43)
# ### and SIDE-lv-conservation (35); b647 read it at 6bf19ab, its main unmoved since (no change bank)
KERNEL = 'SIDE-structural-error-correction'
KD = 'D:/SIDE-structural-error-correction'
B647_REV = '6bf19ab'
K_MAIN = '6bf19ab'          # ### the kernel's main before the act (b623's AxiomCheck commit), where the blocks are read and the cut is planned
PARENTS = 'b647_table_SIDE-structural-error-correction.json'
SENT = 'b659_table_SIDE-structural-error-correction_sentences.json'
GRADES = 'b659_sentence_grades.json'
CUT_BRANCH = 'docstrings-cut-SIDE-structural-error-correction'
TARGET = 'SIDEStructuralErrorCorrection'
NEXT_TAG = 'v0.2.3'         # ### the next in the kernel's series after v0.2.2
KEPT_LOCAL = 'sec-axiom-b623'
BANKED_PRINTS = ('b623_sec_prints.txt', 3, 64)   # ### the kernel's 62 banked prints, b623's AxiomCheck run (rows are declarations)
K_WORKFLOW = '6679a3a'      # ### the commit putting the workflow on the kernel's main (pushed through push_gated.sh, read back), under (R263)(4)
# ### the one dispatch of the cut branch (Component 3), at the branch: its workflow reads print_targets.txt (the branch's, the 62 banked names)
RUNNER = {KERNEL: dict(branch=CUT_BRANCH, target=TARGET, workflow_commit=K_WORKFLOW, run_id=38335955879,
                       ref='17f4acf5a5f3821703c6166a5f3702b39831dd02')}

# ### (R269)(1), (3): the record lines
E1CFG_LINE = 13994          # ### OPEN_TRAILS: W-ORD-E1-CFG, filed at b656 (relay data/b656_closing.txt)

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm of the suite is a standing arm carried from b658's face
# ### (b658's own act arms not carried). Each run at HEAD and counted before the face names it. Named at Component 4.
ACT_ARMS = ('G-R269-ENTERED', 'G-E1CFG-DISCHARGED', 'G-DRY-STEP-CLEAN', 'G-KERNEL-NAMED', 'G-SENTENCES-BANKED', 'G-GRADES-VERBATIM',
            'G-PROMPT-BEFORE-CUT', 'G-CUT-COMMITS', 'G-CUT-REGRADE')
B658_ACT_ARMS = ('G-R268-ENTERED', 'G-EMPHASES-LINE', 'G-SPLITTER-REPAIRED', 'G-DRY-STEP-CLEAN', 'G-STATEMENT-TRACED', 'G-PROMPT-BEFORE-LEAN',
                 'G-CFG-LANDED', 'G-ZETA-PRINT-UNCHANGED', 'G-PRINT-TARGETS')

EDITED_SHARED = ()
NEW_TESTS = ()
SEALED = ('b659_worklist.py', 'b659_tests.py', 'b659_record.py', 'b659_checks.py', 'b659_closing.py', 'b659_reg_gate.py', 'b659_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
