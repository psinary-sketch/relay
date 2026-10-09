# -*- coding: utf-8 -*-
"""b643_worklist.py -- THE ACT'S DATA, UNDER (R253). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b643: LANE THREE, ACT SEVENTY -- THE TWO READERS REPAIRED (DATA BINDERS, PRIMED NAMES) AND RERUN; THE PAGES RE-EMITTED AT v0.26; THE
### KEYSTONE CENSUS AT v0.7 WITH SIX STATUSES, A NON-VACUITY COLUMN, A CONSUMERS COLUMN AND HINGES MARKED, EVERY CELL FROM BANKS; THE PI-0-1
### FORM READ AT SOURCE; THE SECOND READER. By (R253)(8) the face is sealed after Components 2-6: these tools are written and run before the
### seal, their edits through the Edit tool, and sealed at Component 7.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
GS = 'D:/SIDE-global-section'
PRE_PP = '69b74d0'          # ### PLACE-papers main before the act (b642's record and correction)
PRE_RELAY = '13b1c48b'      # ### relay main before the act (b642's closing)
STEPZERO = '3f9a7920'       # ### relay: b642's closing push-out bank, committed at step zero
E0_COMMIT = '07c43e89'      # ### relay: (R253)(3)(a), tools/e0_rule.py and its planted test, alone
B378_COMMIT = '213902e2'    # ### relay: (R253)(3)(b), tools/b378_terminals.py decl_re and its planted test, alone
E0_TOOL, E0_TEST = 'tools/e0_rule.py', 'tools/test_e0_databinder_b643.py'
B378_TOOL, B378_TEST = 'tools/b378_terminals.py', 'tools/test_primed_names_b643.py'
DATE = '2026-10-08'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/e594f88a-2fab-4757-943d-7ab1bc3de815/scratchpad'
PLANTED_DIR = SP + '/b637_planted'
BUILD1 = SP + '/build1.py'   # ### the watchdog of b600's standing line (OPEN_TRAILS :12356), copied whole (sha256 ab2835b3...)

EF, EF_PIN, EF_TAG = 'D:/SIDE-explicit-formula', '82550e4', 'v0.26'
EF_PIN_PREV, EF_TAG_PREV = '8c51431', 'v0.25'
SEC, SEC_PIN = 'D:/SIDE-structural-error-correction', '6bf19ab'
MATHLIB_PIN = 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES_PREV = {'zeta': 'b638_nodes_zeta.txt', 'chi': 'b638_nodes_chi.txt'}
PROBE_PREV = {'zeta': 'b635_probe_out_zeta.txt', 'chi': 'b635_probe_out_chi.txt'}
NODES = {'zeta': 'b643_nodes_zeta.txt', 'chi': 'b643_nodes_chi.txt'}
PROBE = {'zeta': 'b643_probe_out_zeta.txt', 'chi': 'b643_probe_out_chi.txt'}
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CEN6 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_6.md'
CEN7 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_7.md'
GLOSSARY = 'data/glossary.txt'

# ### the ledger lines the act reads and addresses
B642_ENTRY = 7965
B642_RECORD = 13535
B642_CORRECTION = 13561
B642_WEIGHT_LINE = 7963     # ### b642's line beneath b641's entry
OT_WORKORDERS = (13489, 13491, 13493, 13495, 13497)
OT_SQUEEZE, OT_EPSTEIN = 13527, 13533

SEALED = ('b643_worklist.py', 'b643_tests.py', 'b643_record.py', 'b643_checks.py', 'b643_closing.py', 'b643_reg_gate.py', 'b643_regspec.py')
NEXT_ROUTES = [('b644, the author`s word pending ((R253)(7)): the description re-cut as synthesis under the b640 plan, the census at v0.7 '
                'joining the file set, and W-ORD-H2-LATTICE; the deposit draft 23228113 held', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
