# -*- coding: utf-8 -*-
"""b666_worklist.py -- THE ACT'S DATA, UNDER (R276). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b666: LANE THREE, ACT NINETY-THREE, THE RE-CUT ACT -- b665 AT ITS WEIGHT; SIDE-cosmo'S SENTENCES GRADED, CUT, BUILT ON THE RUNNER AND
### MERGED, THE AXIOM-CLAIM ROW AMONG THEM; THE TIE RULE; THE MIRROR EXPORT.
### Written whole by the Write tool from b664_worklist.py's and b665_worklist.py's forms. The face is sealed after Components 1-3 and the
### dry-run step; these tools are sealed at Component 4.
### (R274)(4), standing: NO CONSTANT HERE NAMES A KERNEL FILE. The act's kernel files are read from its cut bank (data/b666_cut_edits.json, the
### plan's edits; data/b666_cut_SIDE-cosmo.json, the cut's commits) by kernel_files() below, the read printed by every tool that uses it.
"""
import io
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'a708de2'          # ### PLACE-papers main before the act (b665's record, pushed)
PRE_RELAY = '0ff929e0'      # ### relay main before the act (b665's closing, pushed)
STEPZERO = '06149425'       # ### relay: b665's closing push-out bank, the citation check, the ferry and its scan
DATE = '2026-10-13'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
HOLD = 2560
SESSION_ID = '96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf'
ANCHOR = 'RULING (R276) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b666_citation_check.txt'

# ### (R276)(1)-(2): the record lines
B665_ENTRY = 8591           # ### FINDINGS: b665's entry head
B665_TRAIL = 14218          # ### OPEN_TRAILS: b665's trail record
ALTERNATION = 13944         # ### OPEN_TRAILS: the alternation of research and re-cut acts (b654, (R264)(2))

# ### (R276)(2): the kernel, 6 OVERREACHES at relay data/b647_table_kernels.txt :9, read at c5cba30, its main unmoved since (no change bank owed)
KERNEL = 'SIDE-cosmo'
KD = 'D:/SIDE-cosmo'
B647_REV = 'c5cba30'
K_MAIN = 'c5cba30'
CHANGE_BANKS = ()
PARENTS = 'b647_table_SIDE-cosmo.json'
SENT = 'b666_table_SIDE-cosmo_sentences.json'
GRADES = 'b666_sentence_grades.json'
AXIOM_BANK = 'data/b649_axiom_claim_rows.txt'   # ### the axiom-claim bank, its ROW 1 the cell of SteaneExemplar :6's axiom sentence ((R276)(2))
CUT_BRANCH = 'docstrings-cut-SIDE-cosmo'
TARGET = 'SIDECosmo'
NEXT_TAG = 'v0.3.1'         # ### the next patch step after v0.3 (the kernel's series as its tag list prints it: v0.2, v0.3)
K_WORKFLOW = 'f5d8c7d'      # ### the commit putting the workflow on the kernel's main (the file alone; pushed through push_gated.sh, read back)
RUNNER = {KERNEL: dict(branch=CUT_BRANCH, target=TARGET, workflow_commit=K_WORKFLOW, run_id=38471056772,
                       ref='1ddeb7c28d0833ea63011460d861ef196646ab64', dispatched_at='main', prior_run=38470740945,
                       push_runs=(38470582495, 38470730498, 38471044694))}
MERGE, MERGE_TAG = 'ca04c8c', NEXT_TAG
PRINT_TARGETS_N = 53

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm of the suite is a standing arm carried from b665's face
# ### (b665's own act arms not carried). Each run at HEAD and counted before the face names it. Filled at Component 4.
ACT_ARMS = ('G-R276-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-TIE-RULE-ENTERED', 'G-KERNEL-NAMED', 'G-SENTENCES-BANKED',
            'G-GRADES-VERBATIM', 'G-AXIOM-ROW-CELL', 'G-PROMPT-BEFORE-CUT', 'G-CUT-COMMITS', 'G-CUT-REGRADE', 'G-AXIOM-CLAIM-AFTER',
            'G-KERNEL-FILES-FROM-BANK')
B665_ACT_ARMS = ('G-R275-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-STATEMENT-TRACED', 'G-PROMPT-BEFORE-LEAN', 'G-LANDINGS-BANKED',
                 'G-FALLBACK-STRIPPED', 'G-H3-CONTROL', 'G-CAVEAT-DATED', 'G-ORDER-DISCHARGED', 'G-KERNEL-FILES-FROM-BANK', 'G-HYPOTHESES-SCORED')
SEALED = ('b666_worklist.py', 'b666_tests.py', 'b666_citation.py', 'b666_record.py', 'b666_checks.py', 'b666_closing.py', 'b666_reg_gate.py',
          'b666_regspec.py')


def kernel_files():
    """(R274)(4), standing: the act's kernel files read from its banks and from no constant: the cut plan's edited files (data/b666_cut_edits.json)
    and the cut bank's commits' files (data/b666_cut_SIDE-cosmo.json, key file_list), joined; with the bank each came from."""
    out = {}
    for name, key in (('b666_cut_edits.json', 'edits'), ('b666_cut_SIDE-cosmo.json', 'file_list')):
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
