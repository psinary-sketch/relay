# -*- coding: utf-8 -*-
"""b664_worklist.py -- THE ACT'S DATA, UNDER (R274). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b664: LANE THREE, ACT NINETY-ONE, THE RE-CUT ACT -- b663 AT ITS WEIGHT; THE TWO ORDERS PLACED; THE SUITE'S FILE CONSTANT MADE A
### BANK READ; SIDE-effects' SENTENCES GRADED, CUT, BUILT ON THE RUNNER AND MERGED; THE MIRROR EXPORT.
### Written whole by the Write tool from b662_worklist.py's and b663_worklist.py's forms. The face is sealed after Components 1-3 and the
### dry-run step; these tools are sealed at Component 4.
### (R274)(4): NO CONSTANT HERE NAMES A KERNEL FILE. The act's kernel files are read from its cut bank (data/b664_cut_edits.json, the plan's
### edits; data/b664_cut_SIDE-effects.json, the cut's commits) by kernel_files() below, the read printed by every tool that uses it.
"""
import io
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '07d147d'          # ### PLACE-papers main before the act (b663's record, pushed)
PRE_RELAY = 'ba1ba004'      # ### relay main before the act (b663's closing, pushed)
STEPZERO = 'b71abf77'       # ### relay: b663's closing push-out bank, the citation check, the ferry and its scan
DATE = '2026-10-13'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
HOLD = 2560
SESSION_ID = '96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf'
ANCHOR = 'RULING (R274) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b664_citation_check.txt'

# ### (R274)(1)-(4): the record lines
B663_ENTRY = 8537           # ### FINDINGS: b663's entry head
B663_TRAIL = 14166          # ### OPEN_TRAILS: b663's trail record
CERTIFY_LINE = 14158        # ### OPEN_TRAILS: W-ORD-EPSTEIN-CERTIFY
FT_LINE = 14162             # ### OPEN_TRAILS: the transform-bound order (named there W-ORD-FT-FIRST-ORDER)
B663_INSTANCE_BANK = 'b663_epstein_instance.json'   # ### the bank b663's kernel file is read from, (R274)(4)

# ### (R274)(5): the kernel, 7 OVERREACHES at relay data/b647_table_kernels.txt, read at ef4cff7; its main moved since (9a279ac, b648's
# ### restatement of Milestones.lean, built at b652): (R267)(3)'s change banks apply
KERNEL = 'SIDE-effects'
KD = 'D:/SIDE-effects'
B647_REV = 'ef4cff7'
K_MAIN = '9a279ac'
CHANGE_BANKS = ('data/b648_sorry_classification.txt', 'data/b648_sorry_repairs.txt', 'data/b652_build_results.json', 'data/b652_effects_push_out.txt')
PARENTS = 'b647_table_SIDE-effects.json'
SENT = 'b664_table_SIDE-effects_sentences.json'
GRADES = 'b664_sentence_grades.json'
CUT_BRANCH = 'docstrings-cut-SIDE-effects'
TARGET = 'SIDEEffects'
NEXT_TAG = 'v0.1.1'         # ### the next patch step after v0.1 (the kernel's series as its tag list prints it)
K_WORKFLOW = 'ff7825d'      # ### the commit putting the workflow on the kernel's main (the file alone; pushed through push_gated.sh, read back)
RUNNER = {KERNEL: dict(branch=CUT_BRANCH, target=TARGET, workflow_commit=K_WORKFLOW, run_id=38431820497,
                       ref='4c25526c286b41297ecbbe0bea72939e5618d012', dispatched_at='main', push_runs=(38431754330, 38432169079))}
MERGE, MERGE_TAG = '78bbcff', NEXT_TAG
PRINT_TARGETS_N = 34

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm of the suite is a standing arm carried from b663's face
# ### (b663's own act arms not carried). Each run at HEAD and counted before the face names it.
ACT_ARMS = ('G-R274-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-ND-RERUN', 'G-ORDERS-PLACED', 'G-FILE-RULE-ENTERED', 'G-KERNEL-NAMED',
            'G-SENTENCES-BANKED', 'G-GRADES-VERBATIM', 'G-NOCELL-LISTED', 'G-PROMPT-BEFORE-CUT', 'G-CUT-COMMITS', 'G-CUT-REGRADE',
            'G-MET-TEST-DURABLE', 'G-KERNEL-FILES-FROM-BANK')
B663_ACT_ARMS = ('G-R273-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-PLAN-BANKED', 'G-PLAN-BEFORE-LEAN', 'G-WORK-ORDERS-ENTERED',
                 'G-DOMINANCE-BANKED', 'G-INSTANCE-GATE', 'G-MET-WIDENED', 'G-CONTROL-BANKED', 'G-SCRIPT-DIFF-CONFINED', 'G-HYPOTHESES-SCORED')
SEALED = ('b664_worklist.py', 'b664_tests.py', 'b664_citation.py', 'b664_record.py', 'b664_checks.py', 'b664_closing.py', 'b664_reg_gate.py',
          'b664_regspec.py')


def kernel_files():
    """(R274)(4): the act's kernel files read from its banks and from no constant: the cut plan's edited files (data/b664_cut_edits.json) and
    the cut bank's commits' files (data/b664_cut_SIDE-effects.json, key file_list), joined; with the bank each came from."""
    out = {}
    for name, key in (('b664_cut_edits.json', 'edits'), ('b664_cut_SIDE-effects.json', 'file_list')):
        try:
            j = json.load(io.open(os.path.join(D, name), encoding='utf-8'))
        except Exception:
            continue
        v = j.get(key) or []
        for x in v:
            f = x['file'] if isinstance(x, dict) else x
            out.setdefault(f, set()).add('data/' + name)
    return sorted((f, sorted(s)) for f, s in out.items())


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
