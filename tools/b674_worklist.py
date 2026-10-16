# -*- coding: utf-8 -*-
"""b674_worklist.py -- THE ACT'S DATA, UNDER (R284). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b674: LANE TWO, ACT ONE HUNDRED AND ONE, THE RE-CUT ACT -- b673 AT ITS WEIGHT; H5 THROUGH THE BRIDGE; THE TWO DRAFTS RAISED
### VERBATIM FOR THE AUTHOR'S WORD; THE TIE READ FROM ITS BANK AND THE NAMED DOCUMENT'S ROWS CUT; THE CLOSING TOOL REPAIRED AT CARRY.
### No lean on this host. Written whole by the Write tool from b673_worklist.py's form. The face is sealed after Components 1-4 and the
### dry-run step.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'f755f99'          # ### PLACE-papers main before the act (b673's record, pushed)
PRE_RELAY = '6f98c458'      # ### relay main before the act (b673's closing, pushed)
DATE = '2026-10-16'
SESSION_ID = 'b895aca8-50cf-4976-9217-c566f780a886'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R284) BEGIN'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b674_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B673_ENTRY = 8819           # ### FINDINGS: b673's entry head
B673_TRAIL = 14482          # ### OPEN_TRAILS: b673's trail record
DISCHARGE = 14478           # ### OPEN_TRAILS: b673's W-ORD-LI-CONVERSE-NATIVE discharge line
TIE_RULE = 14238            # ### OPEN_TRAILS: b666's tie rule, standing from b666
TIE_BANK, TIE_ROWS = 'b670_licensed_table.txt', (119, 120)    # ### the two documents at 5 rows outside LICENSED or CITED
CEILING_SITES = (('README.md', 125), ('REGISTRY.md', 960), ('FINDINGS.md', 6354))    # ### b670's reading (iii), re-read at step zero
LANDING_DRAFTS = (48, 58)   # ### data/b673_landing.txt: the ceiling successor's head and the faces line's head

# ### the kernels of the tie and the branches step zero deletes ((R284)(6))
KE = 'D:/SIDE-explicit-formula'
TIE_KERNELS = ('SIDE-window', 'SIDE-trivium')
DELETE = (('D:/relay', ('push-b673-root', 'push-b673', 'push-b673-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b673-root', 'push-b673')),
          (KE, ('push-b673-merge', 'chi-li-b669')))
MERGE = 'e36ea316e363b1fad04b7fa9def0fc7f2e78188f'
CHI_LI_TIP = '5050a46acf269e7745ce678c3deb8deed9f2d0bf'

# ### filled at the seal
ACT_ARMS = ()
SHARED_APPENDED = ()
SEALED = ('b674_worklist.py', 'b674_tests.py', 'b674_citation.py', 'b674_record.py', 'b674_checks.py', 'b674_closing.py', 'b674_reg_gate.py',
          'b674_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
