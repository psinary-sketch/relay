# -*- coding: utf-8 -*-
"""b642_worklist.py -- THE ACT'S DATA, UNDER (R252). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b642: LANE THREE, ACT SIXTY-NINE -- SIDE-EXPLICIT-FORMULA v0.26 ON A BRANCH: KEIPER'S THREE IDENTITIES AT EVERY INDEX, THE WINDOW'S
### TWO, THE DEDEKIND PREMISE REFUTED IN THE KERNEL AND RESTATED WITH A WITNESS, dedekind_rhs RE-PROVED, A NON-VACUITY WITNESS PER PREMISE
### STRUCTURE, THE PLATEAURAMP DOCSTRING AT ITS PIN; THE EPSTEIN RUNGS PRICED FROM THE PIN; THE SQUEEZE'S COMPILED JAW NAMED.
### By (R252)(6) the face is sealed after the branch builds and the grades are banked: these tools are written and run before the seal,
### their edits through the Edit tool, and sealed at Component 7.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
GS = 'D:/SIDE-global-section'
PRE_PP = '93db626'          # ### PLACE-papers main before the act (b641's record and correction)
PRE_RELAY = '10fdca58'      # ### relay main before the act (b641's closing)
STEPZERO = '4efa0ffe'       # ### relay: b641's closing push-out bank, committed at step zero
DATE = '2026-10-08'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/e594f88a-2fab-4757-943d-7ab1bc3de815/scratchpad'
PLANTED_DIR = SP + '/b637_planted'
BUILD1 = SP + '/build1.py'   # ### the watchdog of b600's standing line (OPEN_TRAILS :12356), copied whole (sha256 ab2835b3...)

EF, EF_PIN, EF_BRANCH, EF_TAG = 'D:/SIDE-explicit-formula', '8c51431', 'v0.26-work', 'v0.26'
MATHLIB_PIN = 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11'
Z23, Z23_PIN = 'D:/zeta23-b628', '3635e748'
ZZF_FILE = 'Zeta23/FromPNTPlus/ZetaBounds.lean'
ZZF_LINE_SOURCE, ZZF_LINE_VENDORED = 2457, 2485   # ### ZetaZeroFree at 3635e748 and in SIDE-explicit-formula's vendored copy at 8c51431
EPSTEIN_PIN = 'c404e72'     # ### v0.16, Schema/Epstein.lean

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b638_nodes_zeta.txt', 'chi': 'b638_nodes_chi.txt'}
PROBE = {'zeta': 'b635_probe_out_zeta.txt', 'chi': 'b635_probe_out_chi.txt'}
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CEN6 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_6.md'
SURROUND = 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md'

# ### the ledger lines the act reads and addresses
B641_ENTRY = 7939
B641_RECORD = 13499
B641_CORRECTION = 13523
STMT_PIN_BLOCK = 13487      # ### (R251)(7)'s block: W-ORD-STATEMENT-PIN, the line the squeeze correction sits beneath
EPSTEIN_ZQ = 13493
FERRY_LINES = (11864, 13067, 13167, 13193, 13397, 13489, 13491, 13493, 13495, 13497, 13523)

SEALED = ('b642_worklist.py', 'b642_tests.py', 'b642_record.py', 'b642_checks.py', 'b642_closing.py', 'b642_reg_gate.py', 'b642_regspec.py')
NEXT_ROUTES = [('b643, the author`s word pending ((R252)(7)): the census at v0.7 with the status column over six statuses and the '
                'non-vacuity bank, read by the second reader', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
