# -*- coding: utf-8 -*-
"""b655_worklist.py -- THE ACT'S DATA, UNDER (R265). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b655: LANE THREE, ACT EIGHTY-TWO, THE RE-CUT ACT -- b654 AT ITS WEIGHT; THE NEXT KERNEL'S SENTENCES GRADED, CUT, BUILT ON THE RUNNER
### AND MERGED; G-EDIT-ROUTE REPAIRED; THE EDIT ROUTE EXTENDED; THE MIRROR EXPORT.
### Written whole by the Write tool from b654_worklist.py's form. The face is sealed after Components 1-3; these tools are sealed at
### Component 4 with the shared tool the act edits (tools/edit_route.py) and its test.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '8e81846'          # ### PLACE-papers main before the act (b654's record, pushed)
PRE_RELAY = '22ce9a8d'      # ### relay main before the act (b654's closing, pushed)
STEPZERO = '9aa36fcb'       # ### relay: b654's closing push-out bank, committed at step zero
DATE = '2026-10-12'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/1199f364-78c4-4147-843f-edf01bb11b28/scratchpad'
HOLD = 2560
SESSION_ID = '1199f364-78c4-4147-843f-edf01bb11b28'
ANCHOR = 'RULING (R265) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R265)(2): the kernel, by descending OVERREACHES count in relay data/b647_table_kernels.txt (:12, 43; SIDE-kernel's 114 cut at b652-b653)
KERNEL = 'SIDE-global-section'
KD = 'D:/SIDE-global-section'
K_MAIN = '17ce9ff'          # ### the kernel's main before the act, the rev b647 read
PARENTS = 'b647_table_SIDE-global-section.json'
SENT = 'b655_table_SIDE-global-section_sentences.json'
GRADES = 'b655_sentence_grades.json'
CUT_BRANCH = 'docstrings-cut-SIDE-global-section'
K_WORKFLOW = '0b5949a'      # ### SIDE-global-section main: the workflow file under (R263)(4), in the kernel's own build path (the author's word)
MATHLIB_PIN = 'cecd0c4d56a6410638a13491d566104756f892bf'
RUNNER = {KERNEL: dict(branch=CUT_BRANCH, target='all', workflow_commit=K_WORKFLOW, run_id=38276189411,
                       ref='8cea5b45f50d0f40ffde372b40f7005a4922a7bd')}

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm of the suite is a standing arm carried from b654's face
# ### (b654's own act arms not carried)
ACT_ARMS = ('G-R265-ENTERED', 'G-EDIT-ROUTE-LINE', 'G-EDIT-ROUTE-REPAIRED', 'G-KERNEL-NAMED', 'G-SENTENCES-BANKED', 'G-PLAIN-COMMENTS',
            'G-GRADES-VERBATIM', 'G-REGRADE-BEFORE-CUT', 'G-CUT-COMMITS', 'G-CUT-REGRADE', 'G-PROMPT-BEFORE-CUT')

# ### (R265)(4): the shared tool the act edits and its test
EDITED_SHARED = ('edit_route.py', 'test_edit_route_b646.py')
NEW_TESTS = ()
SEALED = ('b655_worklist.py', 'b655_tests.py', 'b655_record.py', 'b655_checks.py', 'b655_closing.py', 'b655_reg_gate.py', 'b655_regspec.py') \
    + EDITED_SHARED


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
