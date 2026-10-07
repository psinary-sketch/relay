# -*- coding: utf-8 -*-
"""b634_worklist.py -- THE ACT'S DATA, UNDER (R244). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b634: LANE THREE, ACT SIXTY-ONE -- THE E0 RULE READ FROM ELABORATED TYPES FOR SIDE-explicit-formula AT v0.25, BESIDE THE
### TEXTUAL READING, EVERY DISAGREEMENT CLASSED, THE UNNAMED ROWS READ; THE ACT-ROOT CENSUS PATH AT v0.5; THE CLOSING'S HEAD LINE.
### Here: the pins before the act; the kernel and its pin; the lists in force; the census paths; the ledger lines the record lines
### address; the disagreement classes; the next act.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KER = 'D:/SIDE-explicit-formula'
GS = 'D:/SIDE-global-section'
PRE_PP = 'c9e36c2'          # ### PLACE-papers main before the act (b633's record)
PRE_RELAY = '9b6f8d01'      # ### relay main before the act (b633's closing)
STEPZERO = 'f34279c8'       # ### relay: b633's closing push-out bank, committed at step zero
DATE = '2026-10-06'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b632_nodes_zeta.txt', 'chi': 'b632_nodes_chi.txt'}          # ### the lists in force since b632
PROBE = {'zeta': 'b632_probe_out.txt', 'chi': 'b632_chi_probe_out.txt'}       # ### their probes
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R244)(4): THE KERNEL AND ITS PIN
KERNEL = 'SIDE-explicit-formula'
KER_TAG, KER_PIN = 'v0.25', '8c51431'
KER_PIN_FULL = '8c51431ada7798c65fa26b07ef99a447d7c15735'
HOLD_MB = 2560
CLASSES = ('section variable', 'auto-bound implicit', 'header cut', 'notation or coercion', 'other')   # ### (R244)(4), in its order

# ### (R244)(4): THE ACT-ROOT CENSUS PATH
CEN4 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md'
CEN5 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_5.md'

# ### the ledger lines the act reads and addresses
B633_ENTRY = 7725           # ### FINDINGS: b633's entry
B633_RECORD = 13227         # ### OPEN_TRAILS: b633's trail record
CLOSING_FORM = 13028        # ### OPEN_TRAILS: the closing form, a clause at the record's form (b627)
GATE_WO = 13000             # ### OPEN_TRAILS: W-ORD-GATE-FROM-ELABORATOR, priced (b626)
BINDER_GRAMMAR = 13002      # ### OPEN_TRAILS: W-ORD-BINDER-GRAMMAR, priced (b626)
BUILD_ROUTE = 13167         # ### OPEN_TRAILS: the build route under the hold, standing (b631)

NEXT_ROUTES = [('b635, the (R110) deposit preparations: the census at v0.5, the root chain, the kernel tags and the table`s provenance '
                'counts assembled as the deposit description`s items, nothing deposited', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
