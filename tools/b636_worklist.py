# -*- coding: utf-8 -*-
"""b636_worklist.py -- THE ACT'S DATA, UNDER (R246). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b636: LANE THREE, ACT SIXTY-THREE -- THE ELABORATED READER OVER SIDE-structural-error-correction AT v0.2.2, ITS ROWS GRADED WITH
### PROVENANCE, THE PHASE 2 ROWS RE-READ; THE NAME PATTERNS AND THE TAG MATCHER REPAIRED; THE SEAL'S HASH ARM. Here: the pins before the
### act; the kernel and its pin; the explicit-formula kernel and the lists in force for the pages; chi_Tail's row; the census paths and
### lines; the ledger lines; the sealed tools; the next act.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
GS = 'D:/SIDE-global-section'
PRE_PP = '07f4c43'          # ### PLACE-papers main before the act (b635's correction beneath its record)
PRE_RELAY = '4b84f96d'      # ### relay main before the act (b635's closing)
STEPZERO = 'be879893'       # ### relay: b635's closing push-out bank, committed at step zero
REPAIRS = ('7b5bea0b', '51a9cc0e')   # ### relay: the two step-zero repairs, (R246)(2)(ii) and (iii), each committed alone with its test
DATE = '2026-10-07'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b632_nodes_zeta.txt', 'chi': 'b632_nodes_chi.txt'}          # ### the lists in force since b632
PROBE = {'zeta': 'b635_probe_out_zeta.txt', 'chi': 'b635_probe_out_chi.txt'}   # ### the probes in force since b635 (its Pages answer)
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R246)(4): THE KERNEL AND ITS PIN
KERNEL = 'SIDE-structural-error-correction'
KER = 'D:/SIDE-structural-error-correction'
KER_TAG, KER_PIN = 'v0.2.2', '6bf19ab'
KER_PIN_FULL = '6bf19ab0ef6a77a1b7e2bbdf5bf14fb411fc3b0c'
KER_ROOTS = ('SIDEStructuralErrorCorrection',)      # ### its one library (lakefile.toml), no package dependency (lake-manifest.json)
N_DECLS, N_THEOREMS = 62, 34                         # ### the ruling's figures: the table's rows of the kernel, the theorems among them
HOLD_MB = 2560
HOLD_ABOVE = 10                                      # ### (R246)(4): more than ten oleans missing is a HOLD
CLASSES = ('section variable', 'auto-bound implicit', 'header cut', 'notation or coercion', 'other')   # ### (R244)(4), in its order
ELAB_BANK = 'b636_elab_sec.txt'                      # ### (R246)(4): the kernel's elaborated types, by the ferry's name
DISAGREE_BANK = 'b636_gate_disagreements_sec.txt'
PHASE2_BANK = 'b636_phase2_read.txt'

# ### the explicit-formula kernel: its pin for the pages and for (R246)(2)(i)
EF = 'D:/SIDE-explicit-formula'
EF_KERNEL, EF_PIN = 'SIDE-explicit-formula', '8c51431'
CHI_TAIL = 'SIDEExplicitFormula.GRHWeil.Generic.chi_Tail_TailHyp_traceNorm_smul_Ez_le'
CHI_TAIL_BINDER = 'hM'                               # ### the binder nested two deep, read by b635's repair

# ### the census and its SEC reading
CEN5 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_5.md'
CEN4 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md'
SIEVE6 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md'
CEN5_SEC_ROW = 111          # ### §1A: the SEC kernel row
CEN5_1C = 127               # ### §1C: the Phase 2 rows read against SEC
PHASE2_ROWS = ('R12', 'R14', 'R16', 'R17')

# ### the ledger lines the act reads and addresses
B635_ENTRY = 7771           # ### FINDINGS: b635's entry
B635_RECORD = 13281         # ### OPEN_TRAILS: b635's trail record
B635_CORRECTION = 13305     # ### OPEN_TRAILS: b635's correction
BUILD_CLAUSE = 12356        # ### OPEN_TRAILS: the build clause, standing (b600); the seal rule restated beneath it ((R246)(3))
BUILD_ROUTE = 13167         # ### OPEN_TRAILS: the build route under the hold, standing (b631)
HEADLINE = 13251            # ### OPEN_TRAILS: the closing's head line, standing (b634)
MANIFEST_LINE = 12929       # ### OPEN_TRAILS: the mirror's root line in its stage, standing
GATE_WO = 13000             # ### OPEN_TRAILS: W-ORD-GATE-FROM-ELABORATOR (b626)
BINDER_GRAMMAR = 13002      # ### OPEN_TRAILS: W-ORD-BINDER-GRAMMAR, priced (b626)

# ### (R246)(3): THE SEALED TOOLS -- this act's own tools that take no edit by any means until the act closes; their sha256 recorded at the
# ### seal by the suite (`--seal`, data/b636_seal_hashes.json) and recomputed at the close by G-SEAL-HASHES
SEALED = ('b636_worklist.py', 'b636_tests.py', 'b636_record.py', 'b636_checks.py', 'b636_closing.py', 'b636_reg_gate.py', 'b636_regspec.py')

NEXT_ROUTES = [('b637, on the author`s word: the deposit (the author`s own act), or W-ORD-BINDER-GRAMMAR with the 20 unnamed rows as its '
                'test set', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
