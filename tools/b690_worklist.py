# -*- coding: utf-8 -*-
"""b690_worklist.py -- THE ACT'S DATA, UNDER (R300). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b690: LANE TWO, ACT ONE HUNDRED AND SEVENTEEN, THE READING ACT, READING 3 -- b689 AT ITS WEIGHT; THE POST-SEAL FAILURE BY CORRIGENDUM;
### THE CENSUS; P3 ACROSS THE CORPUS; THE FACES ROW RAISED; THE CIRCUIT INSTRUMENT SPECIFIED; THREE RULES BANKED.
### No lean on this host and no runner dispatched. Written whole by the Write tool from b689_worklist.py's form. The act continues b689's session
### (2c300355): its ruling is the session's second, so the anchor is (R300)'s line and the capture runs from it.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'a5b86a5'          # ### PLACE-papers main before the act (b689's record, pushed)
PRE_RELAY = 'c8afcb43'      # ### relay main before the act (b689's closing, pushed)
DATE = '2026-10-19'
SESSION_ID = '2c300355-703e-4575-81bc-2631a70202cf'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R300) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b690_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B689_ENTRY = 9348           # ### FINDINGS: b689's entry head
B689_TRAIL = 14952          # ### OPEN_TRAILS: b689's trail record
B689_FACE = 'data/b689_registration_2026-10-19.txt'
B689_DEFECT_E = 38          # ### data/b689_defects.txt: (e)
B689_CMD_LINE = 238         # ### data/b689_commands.txt: #177 in the every-command list

# ### the branches step zero deletes ((R300)(6)), one per command, each its own message, in sequence
DELETE = (('D:/relay', ('push-b689-root', 'push-b689', 'push-b689-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b689-root', 'push-b689')),
          ('D:/SIDE-explicit-formula', ('push-b689-merge', 'strip-free-b689')))
DELETE_REMOTE = (('D:/SIDE-explicit-formula', 'strip-free-b689'),)

FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
NODES, NODES_ROW = 'data/b688_nodes_zeta.txt', 167

NEXT = ('b691, the re-cut act: the tie between SIDE-archimedean and SIDE-rcurve at 2 broken by b674`s rule read from the bank at that act`s '
        'step zero, rule (2) of data/b690_rules.txt binding, the arms for rules (1) and (2) sorted there; b692 the research act, the author`s '
        'word at b691`s ruling between W-ORD-CIRCUIT-READING and W-ORD-EPSTEIN-COUNT-LEAN')

SEALED = ('b690_worklist.py', 'b690_tests.py', 'b690_citation.py', 'b690_record.py', 'b690_checks.py', 'b690_closing.py', 'b690_reg_gate.py',
          'b690_regspec.py')
REPAIRED_TOOLS = ()
PARTS = ('standing-a', 'standing-c', 'standing-b', 'act')     # ### data/b684_rules.txt row (1)


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
