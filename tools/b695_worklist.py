# -*- coding: utf-8 -*-
"""b695_worklist.py -- THE ACT'S DATA, UNDER (R305). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b695: LANE TWO, ACT ONE HUNDRED AND TWENTY-TWO, THE RE-CUT ACT -- b694 AT ITS WEIGHT; THE POST-SEAL FAILURES BY CORRIGENDUM; THE
### NEXT DOCUMENT CUT UNDER THE QUOTATION RULE; THE WITNESS'S FACES ROW RAISED; THE ELEVENTH SPEC ROW. No lean on this host; the runner
### dispatched once per tree state. Written whole by the Write tool from b694_worklist.py's form (stage one: step zero).
### The act continues session b97f6790 (claude pid 20816), the session b694 closed in; the anchor is (R305)'s line, the transcript read
### from the line that carries it.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '4a21fa9'          # ### PLACE-papers main before the act (b694's record, pushed)
PRE_RELAY = '6e451686'      # ### relay main before the act (b694's closing, pushed)
DATE = '2026-10-20'
SESSION_ID = 'b97f6790-cfa6-43ae-aa06-9d3a07249ec4'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R305) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b695_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B694_ENTRY = 9548           # ### FINDINGS: b694's entry head
B694_TRAIL = 15170          # ### OPEN_TRAILS: b694's trail record
B694_FACE = 'data/b694_registration_2026-10-20.txt'

# ### the branches step zero deletes ((R305)(6)), one per command, each its own message, in sequence, nothing chained after any
DELETE = (('D:/relay', ('push-b694', 'push-b694-root', 'push-b694-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b694', 'push-b694-root')),
          ('D:/SIDE-lv-conservation', ('push-b694-lv-closure',)))
DELETE_REMOTE = ()          # ### none stood on a remote (the three ls-remote reads at step zero)

FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
NODES = 'data/b690_nodes_zeta.txt'                    # ### the list the page names at :3 since b690 (the control's list)
NODES_NEW = 'data/b695_nodes_zeta.txt'                # ### b690's list with the successor beneath :167, on the author's word at prompt 1
NODES_ROW = 168                                       # ### the successor's line in the new list
PROBE = 'data/b643_probe_out_zeta.txt'                # ### b643's banked probe output: the page re-emitted without elaborating (no lean)

PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2', 'standing-b3', 'act')     # ### six parts, as b693 drew them
# ### the chain halves as b693 drew them, b695 added to the second
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b695'))

# ### Component 2: the re-cut
KERNEL = 'SIDE-interfaces'
KERNEL_DIR = 'D:/SIDE-interfaces'
PRIOR_TAG, NEXT_TAG = 'v0.2', 'v0.2.1'
KERNEL_TABLE = 'b647_table_SIDE-interfaces.txt'

SEALED = ()
REPAIRED_TOOLS = ()
NEW_TOOLS = ()
STANDING_ADDED = ()          # ### no standing arm added this act (N5)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md')
NEXT = ('b696, the research act, on the author`s word at its ruling among W-ORD-WITNESS-TAIL-BALLS, the regularity-uses bank, '
        'CORRESPONDENCE-DOMINANCE`s build and W-ORD-EPSTEIN-COUNT-LEAN; b697 the re-cut act')
