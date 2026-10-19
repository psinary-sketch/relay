# -*- coding: utf-8 -*-
"""b691_worklist.py -- THE ACT'S DATA, UNDER (R301). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b691: LANE TWO, ACT ONE HUNDRED AND EIGHTEEN, THE RE-CUT ACT -- b690 AT ITS WEIGHT; THE TIE BROKEN AND THE DOCUMENT CUT UNDER THE
### QUOTATION RULE; THE GENERATOR REPAIRED AND ITS COUNT RECONCILED; THE EPSTEIN DOCSTRINGS RAISED; THE STALE ORDERS TRIAGED; ARMS SORTED;
### FIVE PARTS. No lean on this host; the runner dispatched once per tree state. Written whole by the Write tool from b690_worklist.py's form.
### The act continues the session of b689 and b690 (2c300355): its ruling is the session's third, so the anchor is (R301)'s line.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '64936ae'          # ### PLACE-papers main before the act (b690's record, pushed)
PRE_RELAY = '9fc2c81b'      # ### relay main before the act (b690's closing, pushed)
DATE = '2026-10-19'
SESSION_ID = '2c300355-703e-4575-81bc-2631a70202cf'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R301) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b691_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B690_ENTRY = 9390           # ### FINDINGS: b690's entry head
B690_TRAIL = 14982          # ### OPEN_TRAILS: b690's trail record
B690_FACE = 'data/b690_registration_2026-10-19.txt'

# ### the branches step zero deletes ((R301)(9)), one per command, each its own message, in sequence
DELETE = (('D:/relay', ('push-b690-root', 'push-b690', 'push-b690-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b690-root', 'push-b690')))
DELETE_REMOTE = ()

FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
NODES, NODES_ROW = 'data/b690_nodes_zeta.txt', 167   # ### the generator's input list at the page's last write (b690)

SEALED = ('b691_worklist.py', 'b691_tests.py', 'b691_citation.py', 'b691_record.py', 'b691_checks.py', 'b691_closing.py', 'b691_reg_gate.py',
          'b691_regspec.py')
# ### the shared tools this act repairs ((R301)(3), (6)): the generator and its test, and the rule arms; each diff in data/b691_tool_repairs.txt
REPAIRED_TOOLS = ('correspondence_gen.py', 'test_correspondence_gen.py', 'rule_arms.py')
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2', 'act')     # ### (R301)(8): five parts, standing-b split at its midpoint

# ### the order the arms read by commit time: each bank printed before the write it governs
STEPZERO = '73b0185b'        # ### relay: b690's closing push-out bank, committed alone at step zero
C1_RELAY, C1_PP = 'c582b730', '77bef05'      # ### b690's weight line (FINDINGS :9422) and its landing bank
WEIGHT_LINE = 9422
TIE_COMMIT = 'c484f795'      # ### relay: the tie bank, the rule and the rows printed before the naming
QUOTE_RCURVE_COMMIT = '500b2012'
CUT_COMMIT = '6d57ad83'      # ### relay: the SIDE-rcurve cut bank
GEN_REPAIR_COMMIT = 'a101f97f'   # ### relay: the generator's carried-at repair, its test, the dry, the behind bank
GEN_RUN_PP, GEN_RUN_RELAY = '7bbb764', 'd2b6d799'   # ### the two pages by the generator's own write; its run, snapshot and diff banks
ORDER_PP, ORDER_LINE = '19ce30a', 15010      # ### W-ORD-CORRESPONDENCE-BEHIND-SCOPE on the author's word
EPSTEIN_LINES_COMMIT = 'b79b5f78'   # ### relay: the three lines, :96-:115, the premises' status, the successor lines, before any branch
TRIAGE_COMMIT = 'bc600ede'   # ### relay: the stale orders triaged, no ledger written
ARMS_COMMIT = '4042d1a9'     # ### relay: the four arms added, each counted at HEAD before declared
GEN_PAGES = ('phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md', 'phase1.5/rcurve/R_CURVE_CRITERION_v0_2_2.md')

# ### the two merges of this act, each on the runner's gate reading: (kernel, the main the merge sits on, the built tip, the merge, the tag,
# ### the main before the act, the files the act wrote on that kernel's main)
MERGES = (('SIDE-rcurve', '29885e5', 'e3df866', '54c9040', 'v0.1.1', 'd5f33b4',
           ('.github/workflows/build-module.yml', 'SIDERCurve/Criterion.lean', 'print_targets.txt')),
          ('SIDE-explicit-formula', '9da7bc2', 'c5aa058', 'e5fcda7', 'v0.34.1', '8fbc27b',
           ('SIDEExplicitFormula/Schema/EpsteinQ0.lean', 'print_targets.txt')))
RUNNER_ROWS = 'b691_runner_rows.json'
KERNEL_COMMITS = {'SIDE-rcurve': ('bb14e89', '29885e5', 'e3df866', '54c9040'), 'SIDE-explicit-formula': ('9da7bc2', 'c5aa058', 'e5fcda7')}

ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CLOSING-DRY-STEP', 'G-CITATION-CHECKED', 'G-R301-ENTERED', 'G-ROWGEN-STEPZERO', 'G-BRANCHES-BANKED',
            'G-DELETES-ONE-BRANCH', 'G-ANSWERS-CHECKED', 'G-SCORER-READS-BANKS', 'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM',
            'G-TIE-BEFORE-NAMING', 'G-CUT-DISTANCE', 'G-PRINTS-EQUAL', 'G-QUOTE-HITS-PRINTED', 'G-GEN-CARRIED-AT', 'G-BEHIND-BANKED',
            'G-GEN-RUN-AFTER-WORD', 'G-ORDER-ENTERED', 'G-EPSTEIN-LINES-BEFORE-BRANCH', 'G-EPSTEIN-RECUT', 'G-TRIAGE-BANKED',
            'G-ARMS-ADDED-COUNTED', 'G-SORT-WORDS-FIRST', 'G-TOOL-REPAIRS', 'G-PARTS-PRERUN', 'G-ARM-SECONDS-BANKED', 'G-DEFECTS-LETTERED')
STANDING_ADDED = ('G-RULE-BINARY-HASHES', 'G-RULE-SUITE-PART-CALLS', 'G-RULE-POSTSEAL-READ', 'G-RULE-RECUT-QUOTE')   # ### (R301)(6)
SHARED_APPENDED = ()         # ### no shared data file appended this act before its root
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md') + GEN_PAGES   # ### the two pages by the generator on the author's word
TITLE = ('## SIDE-rcurve re-cut: 2 rows outside LICENSED/CITED to 0, v0.1.1; the Correspondence generator’s carried-at cells read from the '
         'carrying source, 2 pages regenerated, behind 1 by the generator’s claim and 57 by reading 3’s, the cause scope; EpsteinQ0 docstrings '
         're-cut, v0.34.1; 35 stale orders triaged; 4 arms added')
NEXT = ('b692, the research act: the author`s word between W-ORD-CIRCUIT-READING and W-ORD-EPSTEIN-COUNT-LEAN, the other carried to b694; the '
        'stale-orders triage bank (relay data/b691_orders_triage.txt) raised there')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
