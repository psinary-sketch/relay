# -*- coding: utf-8 -*-
"""b653_worklist.py -- THE ACT'S DATA, UNDER (R263). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b653: LANE THREE, ACT EIGHTY -- b652 AT ITS WEIGHT; THE MARGIN RULE ON COMPLETED RUNS; THE HOSTED RUNNER WRITTEN, RUN AND READ BACK
### FOR TWO BRANCHES; THE ELIDED CELLS COMPLETED AND CUT; THE b638 TEST REPAIRED.
### Carried from b652_worklist.py by the Write tool. The face is sealed after Components 1-4; these tools are sealed at Component 5 with the
### one shared test the act edited (tools/test_chain_page_b638.py).
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '81fa18a'          # ### PLACE-papers main before the act (b652's record, pushed)
PRE_RELAY = '466886b5'      # ### relay main before the act (b652's closing, pushed)
STEPZERO = 'a82a81ad'       # ### relay: b652's closing push-out bank, committed at step zero
DATE = '2026-10-12'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7ab48879-b65c-45b3-8af8-abdcd7120d6f/scratchpad'
HOLD = 2560
SESSION_ID = '7ab48879-b65c-45b3-8af8-abdcd7120d6f'
ANCHOR = 'RULING (R263) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CUT_BRANCH = 'docstrings-cut-SIDE-kernel'
DS_BRANCH = 'docstrings-SIDE-kernel'
RUNNER = {'SIDE-lv-conservation': dict(branch='b648-restate-SIDE-lv-conservation', target='SIDELvConservation', workflow_commit='2b5959f',
                                       run_id=38197669258, failed_run=38197369344, ref='c35a3a314ae957965535dd8dfcd8a5744ca9a384'),
          'SIDE-kernel': dict(branch=DS_BRANCH, target='Kernel Bridge MetaKernel', workflow_commit='802da94', run_id=38197671140,
                              failed_run=38197387315, ref='ee8d21a18a9ae0936523551d0bef773f56f409e1')}
CUT_COMMITS = ('898165c', '0d3f74b', 'a6cbfc6')     # ### SIDE-kernel: the three elided blocks, each file a commit
EDITED_SHARED = ('test_chain_page_b638.py',)
NEW_TESTS = ()
SEALED = ('b653_worklist.py', 'b653_tests.py', 'b653_record.py', 'b653_checks.py', 'b653_closing.py', 'b653_reg_gate.py', 'b653_regspec.py') \
    + EDITED_SHARED


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
