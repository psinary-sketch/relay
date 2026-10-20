# -*- coding: utf-8 -*-
"""b692_worklist.py -- THE ACT'S DATA, UNDER (R302). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b692: LANE TWO, ACT ONE HUNDRED AND NINETEEN, THE RESEARCH ACT -- b691 AT ITS WEIGHT; THE POST-ROOT ITEMS BY CORRIGENDUM; THE
### SUITE-PARTS ARM REPAIRED; THE DEPENDENCY-CIRCUIT READING BUILT AND RUN; CLAUSE-DOMINANCE READ; THE TRIAGE RAISED BY CLASS. No lean on
### this host; the runner dispatched once per tree state. Written whole by the Write tool from b691_worklist.py's form.
### The act continues the session of b689-b691 (2c300355): its ruling is the session's fourth, so the anchor is (R302)'s line.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '9a0dc76'          # ### PLACE-papers main before the act (b691's record, pushed)
PRE_RELAY = 'f5318624'      # ### relay main before the act (b691's closing, pushed)
DATE = '2026-10-19'
SESSION_ID = '2c300355-703e-4575-81bc-2631a70202cf'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R302) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b692_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B691_ENTRY = 9424           # ### FINDINGS: b691's entry head
B691_TRAIL = 15012          # ### OPEN_TRAILS: b691's trail record
B691_FACE = 'data/b691_registration_2026-10-19.txt'

# ### the branches step zero deletes ((R302)(6)), one per command, each its own message, in sequence
DELETE = (('D:/relay', ('push-b691-root', 'push-b691', 'push-b691-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b691-root', 'push-b691')))
DELETE_REMOTE = ()

FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
NODES, NODES_ROW = 'data/b690_nodes_zeta.txt', 167   # ### the generator's input list at the page's last write (b690)

PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2', 'act')     # ### (R302)(2): the names the repaired arm reads
STEPZERO = '2fb05eaa'        # ### relay: b691's closing push-out bank, committed alone at step zero

# ### the act's tools sealed at the carry-time seal, the repaired shared tool (rule_arms.py, (R302)(2)) and the reader among them (N5: the
# ### repair sealed before the suite runs, its hash equal at the close)
SEALED = ('b692_worklist.py', 'b692_tests.py', 'b692_citation.py', 'b692_record.py', 'b692_checks.py', 'b692_closing.py', 'b692_reg_gate.py',
          'b692_regspec.py', 'b692_corrigendum.py', 'b692_parts_probe.py', 'circuit_read.py', 'rule_arms.py')
REPAIRED_TOOLS = ('rule_arms.py',)       # ### (R302)(2) on the author's word (V2); its diff in data/b692_tool_repairs.txt row 1
NEW_TOOLS = ('circuit_read.py',)         # ### (R302)(3)(b): the reader, a new relay tool

# ### the order the arms read by commit time
C1_RELAY, C1_PP = '6eb0f91a', '93dc02c'      # ### b691's weight line (FINDINGS :9454) and the corrigendum (FINDINGS :9456)
WEIGHT_LINE, CORRIGENDUM_LINE = 9454, 9456
RULES_COMMIT = '29a83341'                    # ### relay: data/b692_rules.txt alone
CLOSURE_COMMITS = ('ccec1ba', '59a867c', '4313875')   # ### SIDE-explicit-formula main: the script and the step, its two repairs
CLOSURE_RELAY = '7a3daca6'                   # ### relay: the closure step's banks
READ_RELAY = 'e512e5b0'                      # ### relay: the reader and its readings
SPEC_COMMIT = 'c865120f'                     # ### relay: data/b692_circuit_spec.txt alone
INSTRUMENTS_PP = '90a3293'                   # ### PLACE-papers: INSTRUMENTS.md I-40 alone
ORDERS_PP, ORDERS_LINES = 'c20a631', (15040, 15108)   # ### PLACE-papers: the 35 OPEN_TRAILS entries on the author's word
C4_RELAY = '3a299aac'
EF = 'SIDE-explicit-formula'
EF_BEFORE = 'e5fcda7'                        # ### SIDE-explicit-formula main before the act (v0.34.1)
EF_TIP = '4313875'                           # ### its main after the closure step
SHORTS_BRANCH, SHORTS_TIP = 'circuit-shorts-control-b692', '5866ff2'
CLOSURE_BANK = 'b692_circuit_SIDE-explicit-formula_v0.34.1_4313875.jsonl.gz'
SHORTS_BANK = 'b692_circuit_SIDE-explicit-formula_shorts-control_5866ff2.jsonl.gz'
READING_BANK = 'b692_circuit_SIDE-explicit-formula_v0.34.1.txt'
PRICE, PRICE_SPENT = 1656, 1780
NOT_REACHED = ('SIDE-lv-conservation',)
RUNNER_ROWS = 'b692_runner_rows.json'
RUNNER_LABELS = (('after', 'ccec1ba'), ('after2', '59a867c'), ('after3', '4313875'), ('shorts', '5866ff2'))
KERNEL_COMMITS = {'SIDE-explicit-formula': CLOSURE_COMMITS}

ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CLOSING-DRY-STEP', 'G-CITATION-CHECKED', 'G-R302-ENTERED', 'G-ROWGEN-STEPZERO', 'G-BRANCHES-BANKED',
            'G-DELETES-ONE-BRANCH', 'G-ANSWERS-CHECKED', 'G-SCORER-READS-BANKS', 'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM',
            'G-CORRIGENDUM-ENTERED', 'G-PARTS-ARM-REPAIRED', 'G-RULES-BANKED', 'G-CLOSURE-STEP', 'G-CLOSURE-BANKED', 'G-PRICE-KEPT',
            'G-READER-CONTROLS', 'G-WIDTH-BAR-NAMED', 'G-DOMINANCE-PRINTED', 'G-READFIRST-DIFF-BANKED', 'G-SPEC-TENTH-ROW', 'G-SUITE-LOAD-BANKED',
            'G-INSTRUMENTS-ENTRY', 'G-TRIAGE-ENTERED', 'G-SHORTS-PUSH-EXCEPTION', 'G-TOOL-REPAIRS', 'G-PARTS-PRERUN', 'G-ARM-SECONDS-BANKED',
            'G-DEFECTS-LETTERED')
STANDING_ADDED = ()          # ### no standing arm added this act (N5)
SHARED_APPENDED = ('data/b675_corrigenda.txt',)   # ### rows (5)-(6), (R302)(2), additive per (R254)(2)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/method/INSTRUMENTS.md')
TITLE = ('## The dependency-circuit reading at SIDE-explicit-formula v0.34.1: CLAUSE-DOMINANCE 1 of 1, WIDTH 25 pairs, SHORTS 0; READFIRST-CLOSURE '
         'against the hand list, 23 lines differ; 12 stale orders carried, 23 discharged by reading; b691’s post-root items by corrigendum')
NEXT = ('b693, the re-cut act: the licensed table`s next document by b652`s order and b674`s tie-break, rule (2) of data/b690_rules.txt binding; '
        'SIDE-lv-conservation, the faces kernel the circuit step did not reach, carried by name to b694; b694 the research act: '
        'W-ORD-EPSTEIN-COUNT-LEAN or a candidate of (R302)(5) on the author`s word')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
