# -*- coding: utf-8 -*-
"""b651_worklist.py -- THE ACT'S DATA, UNDER (R261). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b651: LANE THREE, ACT SEVENTY-EIGHT -- THE RE-CUTS OPENED: THE DATA AND PAGE ROWS, THE SEAM ROW, THE SIMPLICITY ROW; THE AXIOM-CLAIM
### RESOLVER; THE CENSUS AT v0.8.1; THE RESTATED LINES MERGED WHERE THE BUILD ALLOWS; THE LARGEST KERNEL'S DOCSTRINGS; THE NAVIGATOR'S ROWS.
### The face is sealed after Components 2-6: these tools are written by the Write tool and edited through the Edit tool before the seal, sealed
### at Component 7 with the three shared tools the act edited (tools/chain_page.py, tools/axiom_claim.py, tools/licensed_table.py).
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '90f2b9c'          # ### PLACE-papers main before the act (b650's trail record, pushed)
PRE_RELAY = '936766a8'      # ### relay main before the act (b650's last push)
STEPZERO = '78e850cd'       # ### relay: b650's two push-out banks, committed at step zero
DATE = '2026-10-11'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7ab48879-b65c-45b3-8af8-abdcd7120d6f/scratchpad'
HOLD = 2560
SESSION_ID = '7ab48879-b65c-45b3-8af8-abdcd7120d6f'
ANCHOR = 'RULING (R261) BEGIN'   # ### the command bank starts at the ruling's delivery in the seat's session
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CEN8 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md'
CEN81 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md'
SIMPL = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
RESTATE = {'SIDE-lv-conservation': 'b648-restate-SIDE-lv-conservation', 'SIDE-effects': 'b648-restate-SIDE-effects'}
DS_KERNEL = 'SIDE-kernel'
DS_BRANCH = 'docstrings-SIDE-kernel'
EDITED_SHARED = ('chain_page.py', 'axiom_claim.py', 'licensed_table.py')
NEW_TESTS = ('test_glossary_supersede_b651.py', 'test_axiom_claim_b651.py', 'test_clusters_served_b651.py')

SEALED = ('b651_worklist.py', 'b651_tests.py', 'b651_record.py', 'b651_checks.py', 'b651_closing.py', 'b651_reg_gate.py', 'b651_regspec.py') \
    + EDITED_SHARED


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
