# -*- coding: utf-8 -*-
"""b693_worklist.py -- THE ACT'S DATA, UNDER (R303). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b693: LANE TWO, ACT ONE HUNDRED AND TWENTY, THE RE-CUT ACT -- b692 AT ITS WEIGHT; THE POST-SEAL FIGURES BY CORRIGENDUM; TWO TOOLS
### REPAIRED AT CARRY TIME; THE NEXT DOCUMENT CUT UNDER THE QUOTATION RULE; SIX PARTS. No lean on this host; the runner dispatched once per
### tree state. Written whole by the Write tool from b692_worklist.py's form (stage one: step zero).
### The act continues the session of b689-b692 (2c300355): its ruling is the session's fifth, so the anchor is (R303)'s line.
### ### After the host's reboot (between relay 0574078e and 91c2df0c) the act resumed in a new session, 88ac42e2, from the author's resume
### order; SESSIONS_AFTER names it with its anchor, and every reader of the act's transcript reads both, the first from (R303)'s line, the
### second from the resume order's line. The scratchpad stays the first session's (it survived the reboot).
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
SESSIONS_AFTER = (('88ac42e2-47ac-48cb-ad82-03a97a19ab1e', 'RESUME b693 after a host reboot'),)   # ### the resume session and its anchor
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

# ### (R303)(4) on the author's word (the chain split by act): standing-b2 verifies the first half and banks its verdicts, carrying no arm;
# ### standing-b3 verifies the second and runs G-ACTROOT-VERIFY once over both; the boundary link read from data/act_roots.txt by both
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))

# ### the act's tools sealed at the carry-time seal, the repaired shared tools among them (N5: each repair sealed before the suite runs, its
# ### hash equal at the close)
SEALED = ('b693_worklist.py', 'b693_tests.py', 'b693_citation.py', 'b693_record.py', 'b693_checks.py', 'b693_closing.py', 'b693_reg_gate.py',
          'b693_regspec.py', 'b693_corrigendum.py', 'b693_parts_probe.py', 'circuit_read.py', 'push_gated.sh', 'test_push_gated.sh',
          'act_root.py', 'test_act_root.py')
# ### the shared tools repaired this act, each with its diff in data/b693_tool_repairs.txt: the reader's readfirst route at step zero (row 1),
# ### the push tool's branch mode and its test ((R303)(2), rows 3-4), the act-root verify's range and its test ((R303)(4) on the author's word,
# ### rows 6-7)
REPAIRED_TOOLS = ('circuit_read.py', 'push_gated.sh', 'test_push_gated.sh', 'act_root.py', 'test_act_root.py')
NEW_TOOLS = ()

# ### the order the arms read by commit time
C1_RELAY, C1_PP = '91156d5d', '45c6e16'      # ### b692's weight line (FINDINGS :9498) and the corrigendum (FINDINGS :9500)
WEIGHT_LINE, CORRIGENDUM_LINE = 9498, 9500
ANSWERS_RELAY = '602b88c3'                   # ### relay: the four answers banked, each checked
REPAIRS_RELAY = 'be2d7e90'                   # ### relay: the closing tool's range repair and the push tool's branch mode
TIE_RELAY = 'c26a17f0'                       # ### relay: the tie-break rule and the rows printed before the naming
BEFORE_RELAY = 'e9e50187'                    # ### relay: the before print bank
CUTRUN_RELAY = 'cb654a48'                    # ### relay: the cut, its quotation search and its run
CUT_RELAY = '13946343'                       # ### relay: the cut bank, the merge and the tag
PARTS_RELAY = '0574078e'                     # ### relay: the parts probe and the act-root range
RESUME_RELAY = '91c2df0c'                    # ### relay: the resume bank, the first commit after the reboot
ARCH = 'SIDE-archimedean'
ARCH_BEFORE = '8019d9d'                      # ### SIDE-archimedean main before the act (v0.1.0)
ARCH_WF, ARCH_PT = '79a8527', '7769d0e'      # ### the workflow and the print list, each alone on main
ARCH_CUT, ARCH_MERGE = '2bd9cc8', 'fcecc45'  # ### the cut on recut-archimedean-b693; the merge by --no-ff, tagged v0.1.1
ARCH_TAG, ARCH_PRIOR_TAG = 'v0.1.1', 'v0.1.0'
RECUT_BRANCH = 'recut-archimedean-b693'
RUNNER_ROWS = 'b693_runner_rows.json'
RUNNER_LABELS = (('before', ARCH_PT), ('after', ARCH_CUT))
KERNEL_COMMITS = {ARCH: (ARCH_WF, ARCH_PT, ARCH_CUT, ARCH_MERGE)}
KERNEL_TAGS = ((ARCH, ARCH_TAG),)
# ### the kernel branches this act made, left for b694's step-zero list
KERNEL_BRANCHES_LEFT = ((ARCH, 'push-b693-archimedean-main', 'local'), (ARCH, 'push-b693-archimedean-merge', 'local'),
                        (ARCH, RECUT_BRANCH, 'local'), (ARCH, RECUT_BRANCH, 'remote'))
BRANCH_MODE_BRANCH = 'push-b693-root'        # ### (R303)(2) and the author's word at prompt 4: the branch mode's one exercise

ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CLOSING-DRY-STEP', 'G-CITATION-CHECKED', 'G-R303-ENTERED', 'G-ROWGEN-STEPZERO', 'G-BRANCHES-BANKED',
            'G-DELETES-ONE-BRANCH', 'G-ANSWERS-CHECKED', 'G-SCORER-READS-BANKS', 'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM',
            'G-CORRIGENDUM-ENTERED', 'G-RANGE-FROM-BANK', 'G-BRANCH-MODE-TESTED', 'G-BRANCH-MODE-EXERCISED', 'G-TIE-PRINTED', 'G-CUT-MERGED',
            'G-QUOTE-BEFORE-MERGE', 'G-DISTANCE-READ', 'G-CELLS-HELD', 'G-READFIRST-DIFF-BANKED', 'G-PARTS-PROBE-READ',
            'G-CHAIN-RANGE-REPAIRED', 'G-CHAIN-CONTROL', 'G-RESUME-BANKED', 'G-TOOL-REPAIRS', 'G-PARTS-PRERUN', 'G-ARM-SECONDS-BANKED',
            'G-DEFECTS-LETTERED')
STANDING_ADDED = ()          # ### no standing arm added this act (N5)
SHARED_APPENDED = ('data/b675_corrigenda.txt',)   # ### row (7), (R303)(2), additive per (R254)(2)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md')
TITLE = ('## SIDE-archimedean re-cut: 2 rows outside LICENSED/CITED to 0, v0.1.1; b692’s LOAD figures by corrigendum; push_gated.sh branch '
         'mode; the closing tool’s defects range read from the bank')
NEXT = ('b694, the research act, on the author`s word at its ruling among W-ORD-EPSTEIN-COUNT-LEAN, the faces kernel the circuit step carried '
        '(SIDE-lv-conservation), the Weil-face witness at Q0 and the regularity-uses bank, each priced in (R302)(5) and the circuit banks')
