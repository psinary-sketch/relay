# -*- coding: utf-8 -*-
"""b647_worklist.py -- THE ACT'S DATA, UNDER (R257). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b647: LANE THREE, ACT SEVENTY-FOUR -- EVERY KERNEL'S DOCSTRINGS THROUGH THE LICENSED-STATEMENT TABLE; THE NAVIGATOR'S MEMORY THROUGH
### THE TABLE; THE DESCRIPTION AT v4 WITH ITS GLOSSARY ENTRIES, A FIFTH READER, THE DRAFT HELD; THE WATCHDOG ON THE PROCESS TREE; THE CENSUS
### COLUMNS EXTENDED. The face is sealed after Components 2-5: these tools are written by the Write tool and edited through the Edit tool
### before the seal, sealed at Component 6.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '2d6daf3'          # ### PLACE-papers main before the act (b646's record)
PRE_RELAY = '48ed6db2'      # ### relay main before the act (b646's closing)
STEPZERO = '716591ed'       # ### relay: b646's closing push-out bank, committed at step zero
WATCH_COMMIT = '4ccc3df6'   # ### relay: the watchdog's tree sampling and its planted test, committed alone
DATE = '2026-10-10'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/bc5efa87-33bc-483a-b723-ace1d978aa31/scratchpad'
HOLD = 2560
SESSION_ID = 'bc5efa87-33bc-483a-b723-ace1d978aa31'
ANCHOR = 'RULING (R257) BEGIN'   # ### the command bank starts at the ruling's delivery in the seat's session
MEMDIR = 'C:/Users/echo chamber/.claude/projects/D--/memory'

EF, EF_PIN, EF_TAG = 'D:/SIDE-explicit-formula', '82550e4', 'v0.26'

DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

SEALED = ('b647_worklist.py', 'b647_tests.py', 'b647_record.py', 'b647_checks.py', 'b647_closing.py', 'b647_reg_gate.py', 'b647_regspec.py',
          'build_watch.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
