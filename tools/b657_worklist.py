# -*- coding: utf-8 -*-
"""b657_worklist.py -- THE ACT'S DATA, UNDER (R267). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b657: LANE THREE, ACT EIGHTY-FOUR, THE RE-CUT ACT -- b656 AT ITS WEIGHT; THE DRY RUN AS A GATE STEP; SIDE-LV-CONSERVATION'S SENTENCES
### GRADED, CUT, BUILT ON THE RUNNER AND MERGED; THE MIRROR EXPORT.
### Written whole by the Write tool from b656_worklist.py's and b655_worklist.py's forms. The face is sealed after Components 1-3 and the
### dry-run step; these tools are sealed at Component 4.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '31c03f9'          # ### PLACE-papers main before the act (b656's record, pushed)
PRE_RELAY = '63001a6b'      # ### relay main before the act (b656's closing, pushed)
STEPZERO = '9b02d1ab'       # ### relay: b656's closing push-out bank, committed at step zero with the ferry
DATE = '2026-10-12'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/1199f364-78c4-4147-843f-edf01bb11b28/scratchpad'
HOLD = 2560
SESSION_ID = '1199f364-78c4-4147-843f-edf01bb11b28'
ANCHOR = 'RULING (R267) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R267)(3): the kernel, 35 OVERREACHES at relay data/b647_table_kernels.txt :17; b647 read it at 2f71068, its main is now b4c55b9
KERNEL = 'SIDE-lv-conservation'
KD = 'D:/SIDE-lv-conservation'
B647_REV = '2f71068'        # ### the rev b647's block bank read
K_MAIN = 'b4c55b9'          # ### the kernel's main before the act (b653's merge), where the blocks are read and the cut is planned
PARENTS = 'b647_table_SIDE-lv-conservation.json'
SENT = 'b657_table_SIDE-lv-conservation_sentences.json'
GRADES = 'b657_sentence_grades.json'
H2_ROW = 'b648_h2_row.json'
CUT_BRANCH = 'docstrings-cut-SIDE-lv-conservation'
K_WORKFLOW = '2b5959f'      # ### SIDE-lv-conservation main: the workflow file under (R263)(4), b653's
MATHLIB_PIN = '5e932f97dd25535344f80f9dd8da3aab83df0fe6'   # ### lakefile.lean :12
NEXT_TAG = 'v0.13.0'        # ### the next in the kernel's series after v0.12.0
# ### the one dispatch of the cut branch (Component 3): the workflow on main since b653 (2b5959f), its print step naming T3's eight
# ### terminals; their banked profiles are b653's runner bank :120-:127 (relay data/b653_runner_SIDE-lv-conservation.txt)
RUNNER = {KERNEL: dict(branch=CUT_BRANCH, target='SIDELvConservation', workflow_commit=K_WORKFLOW, run_id=38305820585,
                       ref='c230e6d8b02a3330eaec4d2e213fa5e905be13a8')}
BANKED_PRINTS = ('b653_runner_SIDE-lv-conservation.txt', 120, 127)

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm of the suite is a standing arm carried from b656's face
# ### (b656's own act arms not carried). Each run at HEAD and counted before the face names it.
ACT_ARMS = ('G-R267-ENTERED', 'G-DRY-STEP-LINE', 'G-DRY-STEP-CLEAN', 'G-KERNEL-NAMED', 'G-SENTENCES-BANKED', 'G-GRADES-VERBATIM', 'G-H2-ROW',
            'G-REGRADE-BANKED', 'G-PROMPTS-BEFORE-CUT', 'G-CUT-COMMITS', 'G-CUT-REGRADE')
B656_ACT_ARMS = ('G-R266-ENTERED', 'G-CORRECTION-LINE', 'G-MIRROR-CLAUSE-LINE', 'G-BINDING-BANKED', 'G-PROMPT-AFTER-BINDING', 'G-STOPPED-AT-C2',
                 'G-E1-CFG-FILED', 'G-NO-PLATEAU-WIDTH')

EDITED_SHARED = ()
NEW_TESTS = ()
SEALED = ('b657_worklist.py', 'b657_tests.py', 'b657_record.py', 'b657_checks.py', 'b657_closing.py', 'b657_reg_gate.py', 'b657_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
