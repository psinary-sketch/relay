# -*- coding: utf-8 -*-
"""b648_worklist.py -- THE ACT'S DATA, UNDER (R258). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b648: LANE THREE, ACT SEVENTY-FIVE -- THE SORRY LINES CLASSIFIED FOR THE AUTHOR'S WORD; THE TWO PAGES THROUGH THE TABLE AND
### RE-EMITTED; THE KEYSTONE CENSUS AT v0.8; THE h2 ROW; THE RE-CUT ORDER TO THE AUTHOR. The face is sealed after Components 2-5: these
### tools are written by the Write tool and edited through the Edit tool before the seal, sealed at Component 6.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '4492e6e'          # ### PLACE-papers main before the act (b647's record)
PRE_RELAY = '6972e068'      # ### relay main before the act (b647's closing)
STEPZERO = '78532543'       # ### relay: b647's closing push-out bank, committed at step zero
DATE = '2026-10-10'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/bc5efa87-33bc-483a-b723-ace1d978aa31/scratchpad'
HOLD = 2560
SESSION_ID = 'bc5efa87-33bc-483a-b723-ace1d978aa31'
ANCHOR = 'RULING (R258) BEGIN'   # ### the command bank starts at the ruling's delivery in the seat's session
MEMDIR = 'C:/Users/echo chamber/.claude/projects/D--/memory'

DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CEN71 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_7_1.md'
CEN8 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}

SEALED = ('b648_worklist.py', 'b648_tests.py', 'b648_record.py', 'b648_checks.py', 'b648_closing.py', 'b648_reg_gate.py', 'b648_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
