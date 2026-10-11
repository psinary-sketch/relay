# -*- coding: utf-8 -*-
"""b649_worklist.py -- THE ACT'S DATA, UNDER (R259). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b649: LANE THREE, ACT SEVENTY-SIX -- THREE ARMS (NO SORRY ON MAIN, AXIOM CLAIMS AGAINST PRINTS, MODULE HEADERS AGAINST FILES); THE
### LEGACY MAP; THE LV-CONSERVATION BUILD MEASURED; THE POSITIVITY CLAUSE NAMED IN THE GLOSSARY AND THE GENERATORS; THE DESCRIPTION AT v5;
### THE DRAFT HELD. The face is sealed after Components 2-6: these tools are written by the Write tool and edited through the Edit tool before
### the seal, sealed at Component 7.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '4946d23'          # ### PLACE-papers main before the act (b648's record)
PRE_RELAY = 'a3cb99b6'      # ### relay main before the act (b648's closing)
STEPZERO = '1dd8f1bb'       # ### relay: b648's closing push-out bank, committed at step zero
DATE = '2026-10-11'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/bc5efa87-33bc-483a-b723-ace1d978aa31/scratchpad'
HOLD = 2560
SESSION_ID = 'bc5efa87-33bc-483a-b723-ace1d978aa31'
ANCHOR = 'RULING (R259) BEGIN'   # ### the command bank starts at the ruling's delivery in the seat's session
MEMDIR = 'C:/Users/echo chamber/.claude/projects/D--/memory'

DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CEN8 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
QUARANTINE = ('SIDE-kernel', 'SIDE-lv-conservation')   # ### b648: the branches sorry-quarantine-<kernel>
ARM_TOOLS = ('no_sorry_main.py', 'axiom_claim.py', 'module_header.py')   # ### (R259)(2): standalone, an arm of every suite from this act

SEALED = ('b649_worklist.py', 'b649_tests.py', 'b649_record.py', 'b649_checks.py', 'b649_closing.py', 'b649_reg_gate.py', 'b649_regspec.py') \
    + ARM_TOOLS


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
