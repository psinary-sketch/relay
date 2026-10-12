# -*- coding: utf-8 -*-
"""b654_worklist.py -- THE ACT'S DATA, UNDER (R264). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b654: LANE TWO, ACT EIGHTY-ONE, THE RESEARCH ACT -- b653 AT ITS WEIGHT; THE ALTERNATION AND THE FREEZE; E1 STATED AND ATTEMPTED ON
### THE RUNNER; THE TRANSVERSALITY WIDTH DEFINED; THE AxiomCheck PRINT RE-BANKED.
### Written whole by the Write tool from b653_worklist.py's form. The face is sealed after Components 1-4; these tools are sealed at
### Component 5.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '16ec28f'          # ### PLACE-papers main before the act (b653's record, pushed)
PRE_RELAY = 'a2beb696'      # ### relay main before the act (b653's closing, pushed)
STEPZERO = 'eda9fea0'       # ### relay: b653's closing push-out bank, committed at step zero
DATE = '2026-10-12'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/1199f364-78c4-4147-843f-edf01bb11b28/scratchpad'
HOLD = 2560
SESSION_ID = '1199f364-78c4-4147-843f-edf01bb11b28'
ANCHOR = 'RULING (R264) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R264)(5): b653's runner artifact for SIDE-lv-conservation, re-read by its id and its sha256 (relay data/b653_runner_SIDE-lv-conservation.txt :107)
LV_ART = dict(repo='psinary-sketch/SIDE-lv-conservation', run_id=38197669258, artifact_id=11724116681,
              sha256='21b63ad8b6220fa2c77769f3cf2d94ff8ec8b725bb73375d747d476d24b06289', built='c35a3a314ae957965535dd8dfcd8a5744ca9a384',
              merged='b4c55b9')

# ### (R264)(3)-(4): the research branch of SIDE-explicit-formula
EF = 'D:/SIDE-explicit-formula'
EF_MAIN = '82550e4'         # ### SIDE-explicit-formula main before the act
E1_BRANCH = 'e1-rate-b654'
DETECTION = ('detection-region-b559', '8faf7de')
EF_WORKFLOW = '7317db4'     # ### SIDE-explicit-formula main: the workflow file under (R263)(4), pushed through push_gated.sh
RUNNER = {'SIDE-explicit-formula': dict(branch=E1_BRANCH, target='SIDEExplicitFormula.RateIndex SIDEExplicitFormula.TransversalityWidth',
                                        workflow_commit=EF_WORKFLOW, run_id=38259645524, failed_run=None,
                                        ref='472887163f31063f3ca7e946ca6a0a790c2f6b7f')}
E1_TERMINALS = ('SIDEExplicitFormula.B321.rest_norm_le_rate', 'SIDEExplicitFormula.B321.zeroSide_neg_at_rate')
WIDTH_TERMINAL = 'SIDEExplicitFormula.transversalityWidth'
E1_FILE, WIDTH_FILE = 'SIDEExplicitFormula/RateIndex.lean', 'SIDEExplicitFormula/TransversalityWidth.lean'

EDITED_SHARED = ()
NEW_TESTS = ()
SEALED = ('b654_worklist.py', 'b654_tests.py', 'b654_record.py', 'b654_checks.py', 'b654_closing.py', 'b654_reg_gate.py', 'b654_regspec.py') \
    + EDITED_SHARED


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
