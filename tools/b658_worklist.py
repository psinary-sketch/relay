# -*- coding: utf-8 -*-
"""b658_worklist.py -- THE ACT'S DATA, UNDER (R268). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b658: LANE TWO, ACT EIGHTY-FIVE, THE RESEARCH ACT -- b657 AT ITS WEIGHT; THE SPLITTER REPAIRED; E1-CFG STATED IN A BANK AND
### ATTEMPTED ON THE RUNNER.
### Written whole by the Write tool from b657_worklist.py's and b654_worklist.py's forms. The face is sealed after Components 1-4 and the
### dry-run step; these tools are sealed at Component 5.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '3f0e33f'          # ### PLACE-papers main before the act (b657's record, pushed)
PRE_RELAY = '640df77a'      # ### relay main before the act (b657's closing, pushed)
STEPZERO = 'c4a45cbb'       # ### relay: b657's closing push-out bank, committed at step zero with the ferry
DATE = '2026-10-12'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
HOLD = 2560
SESSION_ID = '96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf'
ANCHOR = 'RULING (R268) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R268)(2): the splitter (tools/b647_record.py `_MSPLIT`, :846) and its planted test; the two emphases at SIDE-lv-conservation main
LV = 'D:/SIDE-lv-conservation'
LV_MAIN = '8e3bc76'         # ### b657's merge, tag v0.13.0
EMPHASES = (('SIDELvConservation/ZeroActingPartial.lean', 104, 'a lone closing `*` after "is not compiled." (the block from :101)'),
            ('SIDELvConservation/ZeroActingPartial.lean', 107, 'three `**`, the opening one before "Three facts juxtaposed." never closed (the block from :107)'))
CELL_REFRESH_LINE = 14036   # ### OPEN_TRAILS: "Rows a later cell refresh reaches" in b657's trail record (:14022)

# ### (R268)(3)-(4): the research branch of SIDE-explicit-formula
KERNEL = 'SIDE-explicit-formula'
EF = 'D:/SIDE-explicit-formula'
EF_MAIN = '111e418'         # ### SIDE-explicit-formula main before the act (b654's merge, tag v0.27)
EF_TAG = 'v0.27'
NEXT_TAG = 'v0.28'
CFG_BRANCH = 'e1cfg-b658'
EF_WORKFLOW = '7317db4'     # ### SIDE-explicit-formula main: the workflow file under (R263)(4), b654's
# ### the one dispatch of the branch (Component 3), at the branch on the author's word: its workflow reads print_targets.txt
RUNNER = {KERNEL: dict(branch=CFG_BRANCH, target='SIDEExplicitFormula.Schema.RateIndexCfg SIDEExplicitFormula.TransversalityWidth',
                       workflow_commit='f18ab7e', run_id=38324985690, ref='f18ab7e649bad2f8aa3f97b5b7e570728231f57e')}
ZETA_TERMINALS = ('SIDEExplicitFormula.B321.rest_norm_le_rate', 'SIDEExplicitFormula.B321.zeroSide_neg_at_rate')

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm of the suite is a standing arm carried from b657's face
# ### (b657's own act arms not carried). Each run at HEAD and counted before the face names it. Named at Component 5.
ACT_ARMS = ('G-R268-ENTERED', 'G-EMPHASES-LINE', 'G-SPLITTER-REPAIRED', 'G-DRY-STEP-CLEAN', 'G-STATEMENT-TRACED', 'G-PROMPT-BEFORE-LEAN',
            'G-CFG-LANDED', 'G-ZETA-PRINT-UNCHANGED', 'G-PRINT-TARGETS')
B657_ACT_ARMS = ('G-R267-ENTERED', 'G-DRY-STEP-LINE', 'G-DRY-STEP-CLEAN', 'G-KERNEL-NAMED', 'G-SENTENCES-BANKED', 'G-GRADES-VERBATIM', 'G-H2-ROW',
                 'G-REGRADE-BANKED', 'G-PROMPTS-BEFORE-CUT', 'G-CUT-COMMITS', 'G-CUT-REGRADE')

# ### (R268)(2): the shared tool the act edits and its new planted test
EDITED_SHARED = ('b647_record.py',)
NEW_TESTS = ('test_msplit_b658.py',)
SEALED = ('b658_worklist.py', 'b658_tests.py', 'b658_record.py', 'b658_checks.py', 'b658_closing.py', 'b658_reg_gate.py', 'b658_regspec.py') \
    + EDITED_SHARED + NEW_TESTS


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
