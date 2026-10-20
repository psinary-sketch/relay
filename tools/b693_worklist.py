# -*- coding: utf-8 -*-
"""b693_worklist.py -- THE ACT'S DATA, UNDER (R303). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b693: LANE TWO, ACT ONE HUNDRED AND TWENTY, THE RE-CUT ACT -- b692 AT ITS WEIGHT; THE POST-SEAL FIGURES BY CORRIGENDUM; TWO TOOLS
### REPAIRED AT CARRY TIME; THE NEXT DOCUMENT CUT UNDER THE QUOTATION RULE; SIX PARTS. No lean on this host; the runner dispatched once per
### tree state. Written whole by the Write tool from b692_worklist.py's form (stage one: step zero).
### The act continues the session of b689-b692 (2c300355): its ruling is the session's fifth, so the anchor is (R303)'s line.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '62b632f'          # ### PLACE-papers main before the act (b692's record, pushed)
PRE_RELAY = '1749abbb'      # ### relay main before the act (b692's closing, pushed)
DATE = '2026-10-19'
SESSION_ID = '2c300355-703e-4575-81bc-2631a70202cf'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R303) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b693_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B692_ENTRY = 9462           # ### FINDINGS: b692's entry head
B692_TRAIL = 15110          # ### OPEN_TRAILS: b692's trail record
B692_FACE = 'data/b692_registration_2026-10-19.txt'

# ### the branches step zero deletes ((R303)(5)), one per command, each its own message, in sequence
DELETE = (('D:/relay', ('push-b692-root', 'push-b692', 'push-b692-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b692-root', 'push-b692')),
          ('D:/SIDE-explicit-formula', ('push-b692-closure', 'push-b692-closure-2', 'push-b692-closure-3')))
DELETE_REMOTE = ()

FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'

PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2', 'standing-b3', 'act')     # ### (R303)(4): six parts
STEPZERO = '0a98bd1c'        # ### relay: b692's closing push-out bank, committed alone at step zero
