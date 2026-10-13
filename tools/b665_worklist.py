# -*- coding: utf-8 -*-
"""b665_worklist.py -- THE ACT'S DATA, UNDER (R275). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b665: LANE TWO, ACT NINETY-TWO, THE RESEARCH ACT -- b664 AT ITS WEIGHT; THE KEIPER FINITE-n EQUALITY AND THE TRANSFORM BOUND STATED
### IN ONE BANK, ATTEMPTED ON THE RUNNER, LANDED EACH ON ITS OWN READING.
### Written whole by the Write tool from b664_worklist.py's form. The face is sealed after Components 1-5 and the dry-run step; these tools are
### sealed at Component 6.
### (R274)(4), standing: NO CONSTANT HERE NAMES A KERNEL FILE. The act's kernel files are read from its banks (data/b665_keiper_statement.json,
### key files -- the statement bank's planned files; data/b665_attempt.json, key file_list -- the branch commit's files) by kernel_files()
### below, the read printed by every tool that uses it.
"""
import io
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'b1a2bab'          # ### PLACE-papers main before the act (b664's record, pushed)
PRE_RELAY = 'efdd9309'      # ### relay main before the act (b664's closing, pushed)
STEPZERO = '0b2d09ce'       # ### relay: b664's closing push-out bank, the citation check, the ferry and its scan
DATE = '2026-10-13'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
HOLD = 2560
SESSION_ID = '96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf'
ANCHOR = 'RULING (R275) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b665_citation_check.txt'

# ### (R275)(1): the record line
B664_ENTRY = 8563           # ### FINDINGS: b664's entry head
B664_TRAIL = 14194          # ### OPEN_TRAILS: b664's trail record
FT_LINE = 14162             # ### OPEN_TRAILS: the transform-bound order (named there W-ORD-FT-FIRST-ORDER)
FT_JOINED = 14186           # ### OPEN_TRAILS: b664's line joining the order to b665
CERTIFY_LINE = 14158        # ### OPEN_TRAILS: W-ORD-EPSTEIN-CERTIFY (b667)

# ### (R275)(2)-(4): the kernel and the attempt
KERNEL = 'SIDE-explicit-formula'
KD = 'D:/SIDE-explicit-formula'
K_MAIN = 'd00ab16'          # ### the kernel's main at the act's start = v0.29
MATHLIB = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
MATHLIB_PIN = 'de5ce8a9'
BRANCH = 'keiper-b665'
NEXT_TAG = 'v0.30'
STATEMENT_BANK = 'b665_keiper_statement'      # ### .txt and .json, Component 2
ATTEMPT_BANK = 'b665_attempt.json'            # ### Component 3: the branch commit, its files, the run
KEIPER_BANK, TB_BANK = 'b665_keiper.txt', 'b665_transform_bound.txt'
CONTROL_BANK = 'b665_keiper_control.txt'
B663_CONTROL = 'b663_epstein_control.txt'

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm of the suite is a standing arm carried from b664's face
# ### (b664's own act arms not carried). Each run at HEAD and counted before the face names it. Filled at Component 6.
ACT_ARMS = ()
B664_ACT_ARMS = ('G-R274-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-ND-RERUN', 'G-ORDERS-PLACED', 'G-FILE-RULE-ENTERED', 'G-KERNEL-NAMED',
                 'G-SENTENCES-BANKED', 'G-GRADES-VERBATIM', 'G-NOCELL-LISTED', 'G-PROMPT-BEFORE-CUT', 'G-CUT-COMMITS', 'G-CUT-REGRADE',
                 'G-MET-TEST-DURABLE', 'G-KERNEL-FILES-FROM-BANK')
SEALED = ('b665_worklist.py', 'b665_tests.py', 'b665_citation.py', 'b665_record.py', 'b665_checks.py', 'b665_closing.py', 'b665_reg_gate.py',
          'b665_regspec.py')


def kernel_files():
    """(R274)(4), standing: the act's kernel files read from its banks and from no constant: the statement bank's planned files
    (data/b665_keiper_statement.json, key files) and the attempt bank's commit files (data/b665_attempt.json, key file_list), joined; with the
    bank each came from. Only .lean files are kernel files here; print_targets.txt is read beside them by the tools that need it."""
    out = {}
    for name, key in ((STATEMENT_BANK + '.json', 'files'), (ATTEMPT_BANK, 'file_list')):
        try:
            j = json.load(io.open(os.path.join(D, name), encoding='utf-8'))
        except Exception:
            continue
        for x in j.get(key) or []:
            f = x['file'] if isinstance(x, dict) else x
            if f.endswith('.lean'):
                out.setdefault(f, set()).add('data/' + name)
    return sorted((f, sorted(s)) for f, s in out.items())


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
