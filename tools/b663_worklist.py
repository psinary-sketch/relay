# -*- coding: utf-8 -*-
"""b663_worklist.py -- THE ACT'S DATA, UNDER (R273). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b663: LANE TWO, ACT NINETY, THE RESEARCH ACT -- b662 AT ITS WEIGHT; THE EPSTEIN RUNGS READ AND THE PLAN RAISED; THE Q0
### CONFIGURATION BUILT ON PREMISES; THE DETECTOR AND THE RATE INDEX AT THE REAL CONFIGURATION.
### Written whole by the Write tool from b662_worklist.py's form. The face is sealed after Components 1-5 and the dry-run step; these
### tools are sealed at Component 6.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '16be102'          # ### PLACE-papers main before the act (b662's record, pushed)
PRE_RELAY = '51838723'      # ### relay main before the act (b662's closing, pushed)
STEPZERO = '45d29d72'       # ### relay: b662's closing push-out bank, the citation check, the ferry and its scan
DATE = '2026-10-13'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
HOLD = 2560
SESSION_ID = '96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf'
ANCHOR = 'RULING (R273) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b663_citation_check.txt'

# ### (R273)(1): the record lines
B662_ENTRY = 8509           # ### FINDINGS: b662's entry head
B662_TRAIL = 14138          # ### OPEN_TRAILS: b662's trail record
EPSTEIN_LINE = 13493        # ### OPEN_TRAILS: W-ORD-EPSTEIN-ZQ, entered at b641
RUNGS_LINE = 13533          # ### OPEN_TRAILS: b642's price beside it (relay data/b642_epstein_rungs.txt)
PREMISE_LINE = 13436        # ### OPEN_TRAILS: W-ORD-PREMISE-EPSTEINPREMISES (b640)
B590_ENTRY = 6746           # ### FINDINGS: b590's Epstein instance paragraph

# ### (R273)(2)-(5): the kernel, the instance b590 built, the zero banks (on the author's word, b326's), the map carried
KERNEL = 'SIDE-explicit-formula'
KD = 'D:/SIDE-explicit-formula'
K_MAIN = 'ffbc617'          # ### the kernel's main before the act, = v0.28 (b658's merge)
K_TAG_PREV, NEXT_TAG = 'v0.28', 'v0.29'
B590_COMMIT = 'c404e72'     # ### v0.16: Schema/Detector.lean, Schema/Epstein.lean, Schema/SaltCheckEpstein.lean, AxiomCheckEpstein.lean
EPSTEIN_FILE = 'SIDEExplicitFormula/Schema/Epstein.lean'
BRANCH = 'epstein-b663'
ZEROS_ON = 'b326_epstein_zeros.json'       # ### 146 on-line ordinates below T = 150 (key 'zeros', gamma_a == gamma_b)
ZEROS_OFF = 'b326_offline.json'            # ### 17 off-line zeros, sigma in [0.52, 1.5], T = 150 (key 'zeros', rho_a == rho_b)
FORM_BANK = ('b523_registration_2026-09-25.txt', 62)   # ### the form x^2 + xy + 6y^2, h(-23) = 3
BENCH_READ = ('b548_reads.txt', 307)                   # ### the bench's reading of the same list
RHO_E = ('0.7979971571786801', '29.551761098629115')   # ### Schema/Epstein.lean :32, from data/b506_c2_results.json
MAP_FROM = 'b662_map.py'
MAP_TO = 'b663_epstein_map.py'

# ### Components 3-5: the one dispatch, the run, the merge
K_WORKFLOW = '7317db4'      # ### the workflow put on the kernel's main at b654, the file alone in its commit
RUN_ID = 38413488503
RUN_REF = 'c7d28584d0976625f63014f1e9b2e21a2a0c6c76'
RUN_TARGET = 'SIDEExplicitFormula.Schema.EpsteinQ0'
MERGE, MERGE_TAG = 'd00ab16', 'v0.29'
PRINT_TARGETS_N = 31

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm of the suite is a standing arm carried from b662's face
# ### (b662's own act arms not carried). Each run at HEAD and counted before the face names it.
ACT_ARMS = ('G-R273-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-PLAN-BANKED', 'G-PLAN-BEFORE-LEAN', 'G-WORK-ORDERS-ENTERED',
            'G-DOMINANCE-BANKED', 'G-INSTANCE-GATE', 'G-MET-WIDENED', 'G-CONTROL-BANKED', 'G-SCRIPT-DIFF-CONFINED', 'G-HYPOTHESES-SCORED')
B662_ACT_ARMS = ('G-R272-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-FINDING-AND-E2', 'G-CITATION-ACTED', 'G-REPAIR-APPENDED',
                 'G-MAP40-BANKED', 'G-KERNEL-NAMED', 'G-SENTENCES-BANKED', 'G-GRADES-VERBATIM', 'G-PROMPT-BEFORE-CUT', 'G-CUT-COMMITS',
                 'G-CUT-REGRADE')
SEALED = ('b663_worklist.py', 'b663_tests.py', 'b663_citation.py', 'b663_record.py', 'b663_epstein_map.py', 'b663_checks.py', 'b663_closing.py',
          'b663_reg_gate.py', 'b663_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
