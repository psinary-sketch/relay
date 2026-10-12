# -*- coding: utf-8 -*-
"""b652_worklist.py -- THE ACT'S DATA, UNDER (R262). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b652: LANE THREE, ACT SEVENTY-NINE -- b651 AT ITS WEIGHT; THE CONVERSION RULE; THE BUILD MARGIN MEASURED AND THE THREE BRANCHES
### RETRIED UNDER IT; SIDE-KERNEL'S DOCSTRINGS CUT FROM THE SENTENCE ROWS; THE INSTRUMENT VERDICT.
### Carried from b651_worklist.py by the Write tool. The face is sealed after Components 1-4: these tools are written by the Write tool and
### edited through the Edit tool before the seal, sealed at Component 5 with the one shared tool the act edited (tools/licensed_table.py).
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'a6e63c1'          # ### PLACE-papers main before the act (b651's record, pushed)
PRE_RELAY = '1a4caf67'      # ### relay main before the act (b651's closing, pushed)
STEPZERO = '1958b8e9'       # ### relay: b651's closing push-out bank, committed at step zero
DATE = '2026-10-11'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7ab48879-b65c-45b3-8af8-abdcd7120d6f/scratchpad'
HOLD = 2560
SESSION_ID = '7ab48879-b65c-45b3-8af8-abdcd7120d6f'
ANCHOR = 'RULING (R262) BEGIN'   # ### the command bank starts at the ruling's delivery in the seat's session
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RESTATE = {'SIDE-lv-conservation': 'b648-restate-SIDE-lv-conservation', 'SIDE-effects': 'b648-restate-SIDE-effects'}
DS_KERNEL = 'SIDE-kernel'
CUT_BRANCH = 'docstrings-cut-SIDE-kernel'
DS_BRANCH = 'docstrings-SIDE-kernel'
EDITED_SHARED = ('licensed_table.py',)
NEW_TESTS = ('test_conversion_b652.py', 'test_licensed_table_instrument_b652.py')
LANDED = {'FINDINGS': (8257,), 'OPEN_TRAILS': (13896, 13898)}

SEALED = ('b652_worklist.py', 'b652_tests.py', 'b652_record.py', 'b652_checks.py', 'b652_closing.py', 'b652_reg_gate.py', 'b652_regspec.py') \
    + EDITED_SHARED


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
