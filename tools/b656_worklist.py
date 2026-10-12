# -*- coding: utf-8 -*-
"""b656_worklist.py -- THE ACT'S DATA, UNDER (R266). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b656: LANE TWO, ACT EIGHTY-THREE, THE RESEARCH ACT -- b655 AT ITS WEIGHT; (R265)(7) CORRECTED; E1'S QUANTITIES BOUND TO THE KERNEL;
### THE DETECTION-INDEX MAP OVER HYPOTHETICAL OFF-LINE ZEROS IN CERTIFIED ARITHMETIC.
### Written whole by the Write tool from b655_worklist.py's form. The face is sealed after Components 1-3; these tools are sealed at
### Component 4. No kernel file is written in this act ((R266)(5)); the kernel is read at its tag alone.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '651aedb'          # ### PLACE-papers main before the act (b655's record, pushed)
PRE_RELAY = 'c296f930'      # ### relay main before the act (b655's closing, pushed)
STEPZERO = 'e938ec6e'       # ### relay: b655's closing push-out bank, committed at step zero with the ferry
DATE = '2026-10-12'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/1199f364-78c4-4147-843f-edf01bb11b28/scratchpad'
HOLD = 2560
SESSION_ID = '1199f364-78c4-4147-843f-edf01bb11b28'
ANCHOR = 'RULING (R266) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R266)(3): the kernel E1 lives in, read at its tag; no file of it written
KERNEL = 'SIDE-explicit-formula'
KD = 'D:/SIDE-explicit-formula'
K_TAG = 'v0.27'
K_MAIN = '111e418'          # ### the kernel's main = v0.27, before and after the act

# ### (R266)(4): the grid, J_max and the precision, fixed by the ruling (the map script carries them as constants at its head)
SIGMAS = (0.55, 0.6, 0.7, 0.8, 0.9)
TS = (14.1, 29.6, 50.0, 100.0)
J_MAX = 12
PREC_BITS = 200             # ### b627's precision, relay data/b627_margin_inputs.txt:7
H3_CELL = (0.8, 29.6)

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm of the suite is a standing arm carried from b655's face
# ### (b655's own act arms not carried). Filled at Component 4, each run at HEAD and counted before the face names it.
ACT_ARMS = ()

EDITED_SHARED = ()
NEW_TESTS = ()
SEALED = ('b656_worklist.py', 'b656_tests.py', 'b656_record.py', 'b656_checks.py', 'b656_closing.py', 'b656_reg_gate.py', 'b656_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
