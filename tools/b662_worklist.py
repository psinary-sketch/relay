# -*- coding: utf-8 -*-
"""b662_worklist.py -- THE ACT'S DATA, UNDER (R272). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b662: LANE THREE, ACT EIGHTY-NINE, THE RE-CUT ACT -- b661 AT ITS WEIGHT AND ITS MAP READ; THE MAP RE-RUN AT J_max = D + 40; THE
### CITATION CHECK AS A GATE STEP; THE ADDITIVE BREACH REPAIRED; SIDE-carrier-spec'S SENTENCES GRADED, CUT, BUILT ON THE RUNNER AND MERGED;
### THE MIRROR EXPORT.
### Written whole by the Write tool from b659_worklist.py's and b661_worklist.py's forms. The face is sealed after Components 1-4 and the
### dry-run step; these tools are sealed at Component 5.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '13ee2d4'          # ### PLACE-papers main before the act (b661's record, pushed)
PRE_RELAY = '6cca73cf'      # ### relay main before the act (b661's closing, pushed)
STEPZERO = '4545c986'       # ### relay: the citation check, the ferry and its scan, b661's closing push-out bank
DATE = '2026-10-13'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
HOLD = 2560
SESSION_ID = '96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf'
ANCHOR = 'RULING (R272) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R272)(1)-(5): the record lines and the repair
B661_ENTRY = 8485           # ### FINDINGS: b661's entry head
B661_TRAIL = 14110          # ### OPEN_TRAILS: b661's trail record
MAP_LINE = 14070            # ### OPEN_TRAILS: the detection map re-entered (b659), "the map's line" of (R272)(2)
CITATION_LINE = 13840       # ### OPEN_TRAILS: W-ORD-CITATION-CHECK, entered at b650
SHARED_BANK = 'data/b650_same_season_last_year.txt'
BREACH_COMMIT, BREACH_PARENT = '7ebd1c4d', '58c8d3c8'

# ### (R272)(3): the map re-run
MAP_J_EXTRA = 40            # ### the one constant, on the author's word: J_max = D + 40

# ### (R272)(6): the kernel, 9 OVERREACHES at relay data/b647_table_kernels.txt :7, read at b3916cc, its main unmoved since (no change bank)
KERNEL = 'SIDE-carrier-spec'
KD = 'D:/SIDE-carrier-spec'
B647_REV = 'b3916cc'
K_MAIN = 'b3916cc'
PARENTS = 'b647_table_SIDE-carrier-spec.json'
SENT = 'b662_table_SIDE-carrier-spec_sentences.json'
GRADES = 'b662_sentence_grades.json'
CUT_BRANCH = 'docstrings-cut-SIDE-carrier-spec'
TARGET = 'SIDECarrierSpec'
NEXT_TAG = 'v0.4.2'         # ### the next in the kernel's series after v0.4.1 (main b3916cc), b659's form (a patch step for a docstring cut)
README_PROFILES = ('README.md', 75, 101)   # ### the kernel's banked axiom profiles at v0.4.1, README.md :75-:101 (rows are declarations, short names)
K_WORKFLOW = '553e9c4'      # ### the commit putting the workflow on the kernel's main (the file alone; pushed through push_gated.sh, read back)
TARGET_MODULES = ('SIDECarrierSpec.ArithContent SIDECarrierSpec.Grading.AdelicFrame SIDECarrierSpec.Grading.DivisorLadder '
                  'SIDECarrierSpec.IdempotentNoGo SIDECarrierSpec.Level SIDECarrierSpec.SaltCheck SIDECarrierSpec.Spec')   # ### no root module file
# ### the one dispatch (Component 4), on the author's word: at main, the ref input the cut branch's tip (the branch predates the workflow on
# ### main; a first call at the branch was refused with HTTP 422 and ran nothing, defect (f))
RUNNER = {KERNEL: dict(branch=CUT_BRANCH, target=TARGET_MODULES, workflow_commit=K_WORKFLOW, run_id=38370416643,
                       ref='55421a3dd5423c3ae80215bac36ac973f88da662', dispatched_at='main',
                       refused='gh workflow run --ref docstrings-cut-SIDE-carrier-spec: HTTP 422, Workflow does not have workflow_dispatch trigger')}

EDITED_SHARED = ()
NEW_TESTS = ()


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
