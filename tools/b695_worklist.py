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

# ### the commits, in order (relay unless named)
STEPZERO = '12c223b1'        # ### b694's closing push-out bank, alone
STEPZERO_BANKS = 'e0d83d74'  # ### the step-zero banks and tools
C1_RELAY, C1_PP = '254ef39f', '52093a9'
C2_RELAY = '74aa4b9d'
C3_ROWS = 'a5d64b5d'         # ### the faces rows printed, before the prompt
C3_SPEC = '0e85a627'         # ### the spec bank, alone
C3_RELAY, C3_PP = '1b6994b6', 'c354650'
WEIGHT_LINE, CORRIGENDUM_LINE = 9578, 9580
TRAIL_LINES = (15198, 15200)
KI_BEFORE, KI_WF, KI_PT, KI_CUT, KI_MERGE = 'cbdcd5f', '9b4c484', '58854f0', '69b143b', 'c8bd217'
KI_PRIOR_PEEL = '1728796'    # ### v0.2 peeled (an annotated tag one commit before the main the act found)
RUNNER_LABELS = (('before', KI_PT), ('after', KI_CUT))
RUNS = (39487947819, 39488049232)

SEALED = ('b695_worklist.py', 'b695_tests.py', 'b695_citation.py', 'b695_record.py', 'b695_checks.py', 'b695_closing.py', 'b695_reg_gate.py',
          'b695_regspec.py', 'b695_corrigendum.py')
REPAIRED_TOOLS = ()
NEW_TOOLS = ()
ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CLOSING-DRY-STEP', 'G-CITATION-CHECKED', 'G-R305-ENTERED', 'G-ROWGEN-STEPZERO', 'G-BRANCHES-BANKED',
            'G-DELETES-ONE-BRANCH', 'G-ANSWERS-CHECKED', 'G-SCORER-READS-BANKS', 'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-CORRIGENDUM-ENTERED',
            'G-TIE-PRINTED-FIRST', 'G-RECUT-DISTANCE', 'G-QUOTE-BEFORE-MERGE', 'G-RESIDUES-READ', 'G-PRINTS-EQUAL', 'G-CELLS-HELD',
            'G-FACES-ROWS-PRINTED', 'G-FACES-CHECKED', 'G-PAGE-REGENERATED', 'G-TRAIL-LINES-LANDED', 'G-SPEC-ELEVENTH', 'G-READFIRST-DIFF-BANKED',
            'G-TOOL-REPAIRS', 'G-PARTS-PRERUN', 'G-ARM-SECONDS-BANKED', 'G-DEFECTS-LETTERED', 'G-BINARY-ROWS-READ')
STANDING_ADDED = ()          # ### no standing arm added this act (N5)
SHARED_APPENDED = ('data/b675_corrigenda.txt',)   # ### rows (9) and (10); additive per (R254)(2)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')   # ### the page on the author's words at prompts 1 and 2
NEXT = ('b696, the research act, on the author`s word at its ruling among W-ORD-WITNESS-TAIL-BALLS, the regularity-uses bank, '
        'CORRESPONDENCE-DOMINANCE`s build and W-ORD-EPSTEIN-COUNT-LEAN; b697 the re-cut act')
