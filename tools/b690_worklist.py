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
NODES, NODES_ROW = 'data/b688_nodes_zeta.txt', 167   # ### the generator's input list at the page's last write (b688) and the Li face row
NODES_NEW = 'data/b690_nodes_zeta.txt'               # ### b688's list, :167 replaced by the amended row (data/b689_faces_rows.txt), on the author's word
PROBE = 'data/b643_probe_out_zeta.txt'               # ### b643's banked probe output: the page re-emitted without elaborating (no lean)

NEXT = ('b691, the re-cut act: the tie between SIDE-archimedean and SIDE-rcurve at 2 broken by b674`s rule read from the bank at that act`s '
        'step zero, rule (2) of data/b690_rules.txt binding, the arms for rules (1) and (2) sorted there; b692 the research act, the author`s '
        'word at b691`s ruling between W-ORD-CIRCUIT-READING and W-ORD-EPSTEIN-COUNT-LEAN')

SEALED = ('b690_worklist.py', 'b690_tests.py', 'b690_citation.py', 'b690_record.py', 'b690_checks.py', 'b690_closing.py', 'b690_reg_gate.py',
          'b690_regspec.py')
REPAIRED_TOOLS = ()          # ### no shared tool edited this act
PARTS = ('standing-a', 'standing-c', 'standing-b', 'act')     # ### data/b684_rules.txt row (1)

# ### the order the arms read by commit time: each bank printed before the write it governs
STEPZERO = '9854aad2'        # ### relay: b689's closing push-out bank, committed alone at step zero
C1_RELAY, C1_PP = '9988f12c', '3d20a1d'      # ### the weight line and the corrigendum (FINDINGS :9382, :9384)
WEIGHT_LINE, CORRIGENDUM_LINE = 9382, 9384
READINGS_COMMIT = 'd23e0d1b'  # ### relay: tools/b690_readings.py and its twelve banks, before the aggregate
READING3_COMMIT = '2c0e2c28'  # ### relay: data/b690_reading3.txt, the aggregate, after them
FACES_RELAY, FACES_PP = 'eefd27f6', '24b7bf7'  # ### the rows bank's diff and amended row, the new list, the diff bank; the page by the generator
SPEC_COMMIT = '981b6d0b'      # ### relay: data/b690_circuit_spec.txt, alone
RULES_COMMIT = '151faee5'     # ### relay: data/b690_rules.txt, alone
ORDER_PP = '288337a'          # ### PLACE-papers: W-ORD-CIRCUIT-READING at OPEN_TRAILS :14980
ORDER_LINE = 14980

# ### the standing runner arms read the last merged run: b689's (SIDE-explicit-formula v0.34), as b685's suite read b684's; no run this act
import b689_worklist as _K689   # noqa: E402
MERGES = _K689.MERGES
RUNNER_BANK = _K689.RUNNER_BANK
RUNNER_ROWS = 'b689_runner_rows.json'

ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CLOSING-DRY-STEP', 'G-CITATION-CHECKED', 'G-R300-ENTERED', 'G-ROWGEN-STEPZERO', 'G-BRANCHES-BANKED',
            'G-DELETES-ONE-BRANCH', 'G-ANSWERS-CHECKED', 'G-SCORER-READS-BANKS', 'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM',
            'G-CORRIGENDUM-ENTRY', 'G-READINGS-BEFORE-HAND', 'G-P3-HITS-LISTED', 'G-RESIDUES-CENSUS', 'G-FACES-REGENERATED',
            'G-HEADER-CURRENCY-ROW', 'G-CIRCUIT-SPEC-ALONE', 'G-ORDER-ENTERED', 'G-RULES-BANKED-ALONE', 'G-SHARED-ROWS-APPENDED',
            'G-TOOL-REPAIRS', 'G-PARTS-PRERUN', 'G-ARM-SECONDS-BANKED', 'G-DEFECTS-LETTERED')
STANDING_ADDED = ()          # ### (R300)'s N5: no standing arm added
# ### additive, (R254)(2): the corrigenda bank's row (4) under (R300)(2); b689's faces rows bank, the word-level diff, the tail and the amended
# ### row appended beneath its two rows on the author's two answers at the prompt of (R300)(3)
SHARED_APPENDED = ('data/b675_corrigenda.txt', 'data/b689_faces_rows.txt')
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', FACES_PAGE)   # ### the faces page regenerated by the generator on the author's word
TITLE = ('## Reading 3: 345 rows outside LICENSED or CITED, 7 residues, 21 rules with 13 arms, keystone lag median 105; P3 named at 3 lines, 2 '
         'still reading stated; the faces line at Q0 regenerated; the dependency-circuit reading specified; b689’s post-seal failure by corrigendum')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
