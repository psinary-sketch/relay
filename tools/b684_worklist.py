# -*- coding: utf-8 -*-
"""b684_worklist.py -- THE ACT'S DATA, UNDER (R294). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b684: LANE TWO, ACT ONE HUNDRED AND ELEVEN, THE RE-CUT ACT -- b683 AT ITS WEIGHT; THE LICENSED TABLE'S NEXT DOCUMENT CUT; THE THREE
### RESIDUES OF b674, b676 AND b678 RE-DERIVED AND, ON THE AUTHOR'S WORD, APPLIED; THE SUITE'S STANDING PART SPLIT.
### No lean on this host. Written whole by the Write tool from b683_worklist.py's form.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '31746ff'          # ### PLACE-papers main before the act (b683's record, pushed)
PRE_RELAY = 'f38ed009'      # ### relay main before the act (b683's closing, pushed)
DATE = '2026-10-18'
SESSION_ID = 'df03c73f-520a-4848-85dc-8fada095f008'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R294) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b684_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B683_ENTRY = 9170           # ### FINDINGS: b683's entry head
B683_TRAIL = 14776          # ### OPEN_TRAILS: b683's trail record

# ### the branches step zero deletes ((R294)(5)), one per command, each its own message, in sequence
KE = 'D:/SIDE-explicit-formula'
DELETE = (('D:/relay', ('push-b683-root', 'push-b683', 'push-b683-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b683-root', 'push-b683')))
DELETE_REMOTE = ()
K_MAIN = '95f8dc8'

# ### (R294)(3): the licensed table's next document, named by b652's order and b674's tie-break
RULES_BANK, TIE_RULE_ROW = 'b674_rules.txt', 2
TABLE_BANK, KERNELS_BANK = 'b670_licensed_table.txt', 'b647_table_kernels.txt'
CUT_SINCE = (('SIDE-window', 'data/b674_cut.txt', 'SIDE-window'), ('SIDE-trivium', 'data/b676_cut.txt', 'SIDE-trivium'),
             ('SIDE-silence-principle', 'data/b678_cut.txt', 'SIDE-silence-principle'), ('SIDE-bijection', 'data/b682_cut.txt', 'SIDE-bijection'))

# ### (R294)(4): the three residues -- the kernel, its tag (= main), its cut bank and lines, its table bank and the row's lines, its print bank
RESIDUES = (
    dict(kernel='SIDE-window', tag='v0.5.1', act='b674', cut='data/b674_cut.txt', cut_lines=(27, 33), table='data/b647_table_SIDE-window.txt',
         row=(15, 19), file='SIDEWindow/Sawtooth.lean', prints='data/b674_axioms_SIDE-window_after.txt', next_tag='v0.5.2'),
    dict(kernel='SIDE-trivium', tag='v0.1.1', act='b676', cut='data/b676_cut.txt', cut_lines=(35, 43), table='data/b647_table_SIDE-trivium.txt',
         row=(10, 14), file='Trivium/Bijection.lean', prints='data/b676_axioms_SIDE-trivium_after.txt', next_tag='v0.1.2'),
    dict(kernel='SIDE-silence-principle', tag='v0.2.1', act='b678', cut='data/b678_cut.txt', cut_lines=(38, 58),
         table='data/b647_table_SIDE-silence-principle.txt', row=(10, 29), file='SIDESilencePrinciple/Basic.lean',
         prints='data/b678_axioms_SIDE-silence-principle_after.txt', next_tag='v0.2.2'),
)

NEXT = ('b685, the research act: W-ORD-EPSTEIN-COUNT, the count law for Z_Q that P3 (Q0Count) names, by route (i) in the literature or route '
        '(ii) certified by the argument principle under the (3c) bound, its plan to read data/b675_hypotheses.txt, data/b683_map_h.txt and '
        'data/b667_epstein_plan.txt before any route is chosen; b690 the reading act, reading 3')

ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CLOSING-DRY-STEP', 'G-CITATION-CHECKED', 'G-R294-ENTERED', 'G-ROWGEN-STEPZERO', 'G-BRANCHES-BANKED',
            'G-DELETES-ONE-BRANCH', 'G-ANSWERS-CHECKED', 'G-SPLIT-RULE-BANKED', 'G-NAMING-BEFORE-CUT', 'G-KERNEL-CUT', 'G-RESIDUES-BEFORE-ACTIONS',
            'G-RESIDUE-CUTS', 'G-RESIDUE-CARRIED', 'G-PRINTS-EQUAL', 'G-TOOL-REPAIRS', 'G-PARTS-PRERUN', 'G-DEFECTS-LETTERED')
STANDING_ADDED = ()         # ### (R294)'s N5: no standing arm added
SHARED_APPENDED = ('data/b670_work_orders.txt',)
PARTS = ('standing-a', 'standing-c', 'standing-b', 'act')     # ### (R294)(2): the standing arms in three parts, the act's in one
SEALED = ('b684_worklist.py', 'b684_tests.py', 'b684_citation.py', 'b684_record.py', 'b684_checks.py', 'b684_closing.py', 'b684_reg_gate.py',
          'b684_regspec.py', 'rule_arms.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
