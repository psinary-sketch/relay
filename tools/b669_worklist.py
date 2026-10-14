# -*- coding: utf-8 -*-
"""b669_worklist.py -- THE ACT'S DATA, UNDER (R279). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b669: LANE TWO, ACT NINETY-SIX, THE RESEARCH ACT -- b668 AT ITS WEIGHT; THE LI COEFFICIENT STATED OVER THE CONFIGURATION; THE FORWARD
### HALF AT χ AND THE CONVERSE PLANNED, PRICED, ATTEMPTED ON THE RUNNER, LANDED EACH ON ITS OWN READING.
### Written whole by the Write tool from b668_worklist.py's form. The face is sealed after Components 1-4 and the dry-run step.
### (R274)(4), standing: NO CONSTANT HERE NAMES A KERNEL FILE. The act's kernel files are read from its plan bank (data/b669_chi_li_plan.json,
### key kernel_files) by kernel_files() below, the read printed by every tool that uses it.
"""
import io
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'f691545'          # ### PLACE-papers main before the act (b668's record, pushed)
PRE_RELAY = 'bfc407e5'      # ### relay main before the act (b668's closing, pushed)
STEPZERO = '00a52f73'       # ### relay: b668's closing push-out bank, the citation check, the ferry and its scan, the defects bank
DATE = '2026-10-14'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
HOLD = 2560
SESSION_ID = '96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf'
ANCHOR = 'RULING (R279) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b669_citation_check.txt'

# ### the ledger lines this act's record lines are placed by (read at step zero, relay data/b669_citation_check.txt)
B668_ENTRY = 8677           # ### FINDINGS: b668's entry head
B668_TRAIL = 14300          # ### OPEN_TRAILS: b668's trail record
CHI_LI_PRICED = (11732, 11796)   # ### OPEN_TRAILS: the χ-Li converse priced (b570) and REMAINDER 1 (b574), the author's word on the order cite
LI_WEIL_PRICING = 11609     # ### OPEN_TRAILS: the LI-WEIL-BRIDGE converse re-priced, (V1)-(V4)
BULKA_ROUTE = 6136          # ### FINDINGS: prior art for the Li form, Bulka's repository

# ### the kernel ((R279)(2)-(4)): SIDE-explicit-formula at v0.30, Mathlib at the pin
KERNEL = 'SIDE-explicit-formula'
KD = 'D:/SIDE-explicit-formula'
K_MAIN = 'v0.30'
MATHLIB = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
PIN = 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11'
BRANCH = 'chi-li-b669'
NEXT_TAG = 'v0.31'
K_WORKFLOW = None           # ### filled at Component 3 (the kernel's build-module workflow, read there)
RUNNER = {}                 # ### filled at Component 3
PRINT_TARGETS_N = None

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm is a standing arm carried from b668's face (b668's own act arms
# ### not carried). Each run at HEAD and counted before the face names it. Filled at Component 5.
ACT_ARMS = ()
B668_ACT_ARMS = ('G-R278-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-MIDACT-CHECKED', 'G-PLANFORM-ENTERED', 'G-RESEARCH-ORDER-ENTERED',
                 'G-SENTENCES-BANKED', 'G-GRADES-VERBATIM', 'G-PROMPT-BEFORE-CUT', 'G-CUT-COMMITS', 'G-CUT-REGRADE', 'G-AXIOM-CLAIM-AFTER',
                 'G-KERNEL-FILES-FROM-BANK', 'G-ITEMS-ENTERED', 'G-CENSUS-ROW')
SEALED = ('b669_worklist.py', 'b669_tests.py', 'b669_citation.py', 'b669_record.py', 'b669_checks.py', 'b669_closing.py', 'b669_reg_gate.py',
          'b669_regspec.py')


def kernel_files():
    """(R274)(4), standing: the act's kernel files read from its plan bank (data/b669_chi_li_plan.json, key kernel_files) and its landing bank
    (data/b669_chi_li_landing.json, key file_list), joined; with the bank each came from."""
    out = {}
    for name, key in (('b669_chi_li_plan.json', 'kernel_files'), ('b669_chi_li_landing.json', 'file_list')):
        try:
            j = json.load(io.open(os.path.join(D, name), encoding='utf-8'))
        except Exception:
            continue
        for x in j.get(key) or []:
            f = x['file'] if isinstance(x, dict) else x
            out.setdefault(f, set()).add('data/' + name)
    return sorted((f, sorted(s)) for f, s in out.items())


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
