# -*- coding: utf-8 -*-
"""b668_worklist.py -- THE ACT'S DATA, UNDER (R278). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b668: LANE THREE, ACT NINETY-FIVE, THE RE-CUT ACT -- b667 AT ITS WEIGHT; SIDE-grh-transfer'S SENTENCES GRADED, CUT, BUILT ON THE
### RUNNER AND MERGED; THE PLAN-FORM SECTION AND THE MID-ACT CITATION CHECK ENTERED; THE MIRROR EXPORT.
### Written whole by the Write tool from b666_worklist.py's form (the re-cut act before it) and b667's. The face is sealed after Components
### 1-3 and the dry-run step.
### (R274)(4), standing: NO CONSTANT HERE NAMES A KERNEL FILE. The act's kernel files are read from its cut bank (data/b668_cut_edits.json, the
### plan's edits; data/b668_cut_SIDE-grh-transfer.json, the cut's commits) by kernel_files() below, the read printed by every tool that uses it.
"""
import io
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '7904281'          # ### PLACE-papers main before the act (b667's record, pushed)
PRE_RELAY = 'aeccc731'      # ### relay main before the act (b667's closing, pushed)
STEPZERO = 'aad61b62'       # ### relay: b667's closing push-out bank, the citation check, the ferry and its scan
DATE = '2026-10-14'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
HOLD = 2560
SESSION_ID = '96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf'
ANCHOR = 'RULING (R278) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b668_citation_check.txt'

# ### the ledger lines this act's record lines are placed by (read at step zero, relay data/b668_citation_check.txt)
B667_ENTRY = 8649           # ### FINDINGS: b667's entry head
B667_TRAIL = 14270          # ### OPEN_TRAILS: b667's trail record
CITATION_RULE = 14136       # ### OPEN_TRAILS: W-ORD-CITATION-CHECK ACTED, A GATE STEP FROM b662
ALTERNATION = 13944         # ### OPEN_TRAILS: the alternation of research and re-cut acts (b654, (R264)(2))

# ### the kernel ((R278)(2)): SIDE-grh-transfer, the second of the two at 6 OVERREACHES under the tie rule (OPEN_TRAILS :14238)
KERNEL = 'SIDE-grh-transfer'
KD = 'D:/SIDE-grh-transfer'
B647_REV = '858cbf6'
K_MAIN = '858cbf6'
CHANGE_BANKS = ()
PARENTS = 'b647_table_SIDE-grh-transfer.json'
SENT = 'b668_table_SIDE-grh-transfer_sentences.json'
GRADES = 'b668_sentence_grades.json'
BANKED_PRINTS = 'data/b555_probe_g2.txt'     # ### the kernel's banked prints: 21 declarations at 858cbf6, each at the standard three
CUT_BRANCH = 'docstrings-cut-SIDE-grh-transfer'
# ### the dispatch target: the kernel's 14 modules by name -- the lib SIDEGRHTransfer has no root module (no SIDEGRHTransfer.lean; lakefile
# ### :17-:19 globs .submodules), so the workflow's print step, which imports each name of the target, can import modules and not the lib
TARGET = ('SIDEGRHTransfer.CharacterCodim SIDEGRHTransfer.CharacterModular SIDEGRHTransfer.CharacterSpectral SIDEGRHTransfer.CharacterSymmetry '
          'SIDEGRHTransfer.CharacterTopological SIDEGRHTransfer.CharacterTransfer SIDEGRHTransfer.GRHBridge SIDEGRHTransfer.Voice1Vendored '
          'SIDEGRHTransfer.Voice2Vendored SIDEGRHTransfer.Voice3Vendored SIDEGRHTransfer.Voice3bVendored SIDEGRHTransfer.Voice5Vendored '
          'SIDEGRHTransfer.Voice6Vendored SIDEGRHTransfer.Voice7Vendored')
NEXT_TAG = 'v0.5.1'         # ### the next patch step after v0.5.0 (the kernel's series as its tag list prints it: v0.1.0 ... v0.5.0)
K_WORKFLOW = '7f3e315'      # ### the commit putting the workflow on the kernel's main (Component 3, pushed and read back)
RUNNER = {KERNEL: dict(branch=CUT_BRANCH, target=TARGET, workflow_commit=K_WORKFLOW, run_id=38587853597,
                       ref='d487072543ddd8c09376fd424678b524aba06c93', dispatched_at='main', prior_run=None)}
RUNNER_ROWS, RUNNER_BANK = 'b668_runner_rows.json', 'b668_runner_SIDE-grh-transfer.txt'
MERGE, MERGE_TAG = '6e149db', NEXT_TAG
PRINT_TARGETS_N = 53

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm of the suite is a standing arm carried from b667's face
# ### (b667's own act arms not carried). Each run at HEAD and counted before the face names it. Filled at Component 4.
ACT_ARMS = ('G-R278-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-MIDACT-CHECKED', 'G-PLANFORM-ENTERED', 'G-RESEARCH-ORDER-ENTERED',
            'G-SENTENCES-BANKED', 'G-GRADES-VERBATIM', 'G-PROMPT-BEFORE-CUT', 'G-CUT-COMMITS', 'G-CUT-REGRADE', 'G-AXIOM-CLAIM-AFTER',
            'G-KERNEL-FILES-FROM-BANK', 'G-ITEMS-ENTERED', 'G-CENSUS-ROW')
B667_ACT_ARMS = ('G-R277-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-PLAN-BEFORE-NUMBER', 'G-OBSTRUCTIONS-BANKED', 'G-ROUTE-CHECKS',
                 'G-CONTROLS-FIXED', 'G-SQUARES-CERTIFIED', 'G-REGION-COUNTED', 'G-MAP-ON-BALLS', 'G-LANDING-DATED', 'G-B326-UNTOUCHED', 'G-RUNS-BANKED')
SEALED = ('b668_worklist.py', 'b668_tests.py', 'b668_citation.py', 'b668_record.py', 'b668_checks.py', 'b668_closing.py', 'b668_reg_gate.py',
          'b668_regspec.py')


def kernel_files():
    """(R274)(4), standing: the act's kernel files read from its banks and from no constant: the cut plan's edited files (data/b668_cut_edits.json)
    and the cut bank's commits' files (data/b668_cut_SIDE-grh-transfer.json, key file_list), joined; with the bank each came from."""
    out = {}
    for name, key in (('b668_cut_edits.json', 'edits'), ('b668_cut_SIDE-grh-transfer.json', 'file_list')):
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
