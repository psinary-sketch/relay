# -*- coding: utf-8 -*-
"""b661_worklist.py -- THE ACT'S DATA, UNDER (R271). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b661: LANE TWO, ACT EIGHTY-EIGHT, THE RESEARCH ACT -- b660 AT ITS WEIGHT; THE BINDING RE-READ AT v0.28; THE DETECTION-INDEX MAP AT
### Z₁ WITH EVERY HYPOTHESIS CERTIFIED PER CELL.
### Written whole by the Write tool from b659_worklist.py's form. The face is sealed after Components 1-3 and the dry-run step; these tools
### are sealed at Component 4. No kernel edit, no lean run on this host ((R271)(6), N1).
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '2e07a61'          # ### PLACE-papers main before the act (b660's record, pushed)
PRE_RELAY = '2e439312'      # ### relay main before the act (b660's closing, pushed)
STEPZERO = 'a2443559'       # ### relay: b660's closing push-out bank, committed at step zero with the ferry
DATE = '2026-10-13'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
SESSION_ID = '96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf'
ANCHOR = 'RULING (R271) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R271)(2)-(4): the kernel read, never written
KERNEL = 'SIDE-explicit-formula'
KD = 'D:/SIDE-explicit-formula'
K_TAG = 'v0.28'
K_MAIN = 'ffbc617'          # ### v0.28 = main, b658's merge
K_PREV_TAG = 'v0.27'        # ### b656's binding read here (111e418)
CFG_FILE = 'SIDEExplicitFormula/Schema/RateIndexCfg.lean'
THEOREM = 'zeroSide_neg_at_rate_cfg'

# ### (R271)(1): the record line -- b660's weight appended to b660's entry
B660_ENTRY = 8461           # ### FINDINGS: b660's entry head (relay data/b660_closing.txt :7)
B660_TRAIL = 14092          # ### OPEN_TRAILS: b660's trail record

# ### (R271)(3)-(5): the binding, the prompt, the map
BINDING_COMMIT = '7fb75681'  # ### relay: the binding bank, committed alone before the one prompt
MAP_COMMIT = '8ce31653'      # ### relay: the map script, the map bank and the control bank
MAP_CELLS = 20
H3_CELL = ('0.8', '29.6')

# ### No kernel is built in this act: the standing runner arms read SIDE-explicit-formula at its last run (b658's runner banks), its
# ### workflow file on main (b654's commit of the file alone, 7317db4, edited at b658 to read print_targets.txt) and its main the merge of
# ### the built tree tagged v0.28, unmoved by this act -- b656's form.
RUNNER = {KERNEL: dict(branch='e1cfg-b658', target='SIDEExplicitFormula.Schema.RateIndexCfg SIDEExplicitFormula.TransversalityWidth',
                       workflow_commit='7317db4', run_id=38324985690, ref='f18ab7e649bad2f8aa3f97b5b7e570728231f57e')}
RUNNER_ROWS = 'b658_runner_rows.json'
RUNNER_BANK = 'b658_runner_SIDE-explicit-formula.txt'
PRINT_TARGETS_N = 8

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm of the suite is a standing arm carried from b659's face
# ### (b659's own act arms not carried; b660 sealed no face). Each run at HEAD and counted before the face names it.
ACT_ARMS = ('G-R271-ENTERED', 'G-DRY-STEP-CLEAN', 'G-BINDING-BANKED', 'G-PROMPT-BEFORE-NUMBER', 'G-MAP-SCRIPT-HEAD', 'G-MAP-BANKED',
            'G-CERTS-BEFORE-INDEX', 'G-MAP-CONTROL', 'G-HYPOTHESES-SCORED')
B659_ACT_ARMS = ('G-R269-ENTERED', 'G-E1CFG-DISCHARGED', 'G-DRY-STEP-CLEAN', 'G-KERNEL-NAMED', 'G-SENTENCES-BANKED', 'G-GRADES-VERBATIM',
                 'G-PROMPT-BEFORE-CUT', 'G-CUT-COMMITS', 'G-CUT-REGRADE')

EDITED_SHARED = ()
NEW_TESTS = ()
SEALED = ('b661_worklist.py', 'b661_tests.py', 'b661_record.py', 'b661_map.py', 'b661_checks.py', 'b661_closing.py', 'b661_reg_gate.py',
          'b661_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def kshow(path, rev=K_TAG):
    return show(path, rev=rev, repo=KD)
