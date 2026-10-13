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

EDITED_SHARED = ()
NEW_TESTS = ()


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def kshow(path, rev=K_TAG):
    return show(path, rev=rev, repo=KD)
