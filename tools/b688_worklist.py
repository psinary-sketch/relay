# -*- coding: utf-8 -*-
"""b688_worklist.py -- THE ACT'S DATA, UNDER (R298). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b688: LANE TWO, ACT ONE HUNDRED AND FIFTEEN, THE RE-CUT ACT -- b687 AT ITS WEIGHT; THE LICENSED TABLE'S NEXT DOCUMENT CUT BY THE b670
### METHOD; R4 RE-DERIVED IN b684'S FORM; THE SEAT'S LATTICE-SUM ROUTE ENTERED ON ITS CHECK; THE FACES LINE ON THE LI FACE AT Q0 RAISED FOR
### REGENERATION WITH P3'S NEW STATUS.
### No lean on this host. Written whole by the Write tool from b687_worklist.py's form. The act continues b687's session (a90bcdb6): its ruling
### is the session's second, so the anchor is (R298)'s line and the capture runs from it.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '51d3aac'          # ### PLACE-papers main before the act (b687's record, pushed)
PRE_RELAY = 'de011ebd'      # ### relay main before the act (b687's closing, pushed)
DATE = '2026-10-19'
SESSION_ID = 'a90bcdb6-256f-4841-97ff-9638e378446c'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R298) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b688_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B687_ENTRY = 9286           # ### FINDINGS: b687's entry head
B687_TRAIL = 14894          # ### OPEN_TRAILS: b687's trail record

# ### the branches step zero deletes ((R298)(6)), one per command, each its own message, in sequence
DELETE = (('D:/relay', ('push-b687-root', 'push-b687', 'push-b687-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b687-root', 'push-b687')))
DELETE_REMOTE = ()

# ### (R298)(3): the faces line
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
NODES_PRE = 'data/b680_nodes_zeta.txt'          # ### the generator's input list at the page's last write (b680)
NODES_ROW = 167                                  # ### the Li face at Q0's backmatter row in it
PROBE = 'data/b643_probe_out_zeta.txt'

# ### (R298)(4): the licensed table's next document, named by b652's order and b674's tie-break
RULES_BANK, TIE_RULE_ROW = 'b674_rules.txt', 2
TABLE_BANK, KERNELS_BANK = 'b670_licensed_table.txt', 'b647_table_kernels.txt'
CUT_SINCE = (('SIDE-window', 'data/b684_cut.txt', 'SIDE-window'), ('SIDE-trivium', 'data/b684_cut.txt', 'SIDE-trivium'),
             ('SIDE-silence-principle', 'data/b684_cut.txt', 'SIDE-silence-principle'), ('SIDE-bijection', 'data/b682_cut.txt', 'SIDE-bijection'),
             ('SIDE-class-number-anomaly', 'data/b684_cut.txt', 'SIDE-class-number-anomaly'), ('SIDE-spinor', 'data/b686_cut.txt', 'SIDE-spinor'))

# ### (R298)(5): R4
SPINOR = 'D:/SIDE-spinor'
SPINOR_TAG = 'v0.1.1'
R4_FILE = 'SIDESpinor/SpinorLeg.lean'

NEXT = ('b689, the research act: the strip-free form of the Li converse -- the w = 1 split of data/b679_strip_plan.txt section 11, the '
        'hypothesis ρ ≠ 0 alone in place of HExcl`s (−1/2, 0] half -- its ruling then, its plan to read that section and data/b676_strip_uses.txt '
        'before any Lean; b690 the reading act, reading 3')

ACT_ARMS = ()               # ### written at Component 5
STANDING_ADDED = ()         # ### (R298)'s N5: no standing arm added
SHARED_APPENDED = ()
PARTS = ('standing-a', 'standing-c', 'standing-b', 'act')     # ### data/b684_rules.txt row (1)
SEALED = ('b688_worklist.py', 'b688_tests.py', 'b688_citation.py', 'b688_record.py', 'b688_checks.py', 'b688_closing.py', 'b688_reg_gate.py',
          'b688_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
