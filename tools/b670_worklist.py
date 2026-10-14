# -*- coding: utf-8 -*-
"""b670_worklist.py -- THE ACT'S DATA, UNDER (R280). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b670: LANE ONE, ACT NINETY-SEVEN, THE READING ACT -- b669 AT ITS WEIGHT; THE TEN ACTS b660-b669 READ FROM THEIR CLOSINGS; THE FOUR
### CONSISTENCY READINGS AND THE METHOD-READINESS TABLE BANKED; THE QUEUE READ; THE b670 ITEMS ENTERED; THE MIRROR EXPORT.
### Written whole by the Write tool from b669_worklist.py's form. No kernel byte is written in this act; the face is sealed after Components 1-5
### and the dry-run step.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '165a645'          # ### PLACE-papers main before the act (b669's record, pushed)
PRE_RELAY = 'e527a09e'      # ### relay main before the act (b669's closing, pushed)
STEPZERO = 'cb892134'       # ### relay: b669's closing push-out bank, the citation check, the ferry and its scan, the rules and defects banks
DATE = '2026-10-14'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
HOLD = 2560
SESSION_ID = '96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf'
ANCHOR = 'RULING (R280) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b670_citation_check.txt'

# ### the ledger lines this act's record lines are placed by (read at step zero, relay data/b670_citation_check.txt)
B669_ENTRY = 8707           # ### FINDINGS: b669's entry head
B669_TRAIL = 14324          # ### OPEN_TRAILS: b669's trail record
CONSTELLATION = 12092       # ### OPEN_TRAILS: W-ORD-CONSTELLATION-RERUN's items (rowgen diff per table), the rule of reading (i)
ACTS = tuple('b%d' % i for i in range(660, 670))

# ### the kernels this act reads and does not write
KE = 'D:/SIDE-explicit-formula'
OPEN_BRANCH, OPEN_TIP = 'chi-li-b669', 'b804bf2'
CUT = (('SIDE-kernel', 'b652'), ('SIDE-global-section', 'b655'), ('SIDE-lv-conservation', 'b657'), ('SIDE-structural-error-correction', 'b659'),
       ('SIDE-carrier-spec', 'b662'), ('SIDE-effects', 'b664'), ('SIDE-cosmo', 'b666'), ('SIDE-grh-transfer', 'b668'))   # ### from the cut banks:
# ### data/b652_sidekernel_cut.txt (its standing 0 at data/b653_closing.txt), data/b655_ ... data/b668_cut_SIDE-*.txt
NEXT_ACTS = ('b671 W-ORD-EPSTEIN-BALL-WIDTH; b672 the Correspondence generator -- a tooling act in the re-cut slot, one tool committed alone '
             'with its test, every kernel`s Correspondence table regenerated from its tags and print banks and diffed against the table as it '
             'stands, nothing written by hand; b673 V4 and V5 on chi-li-b669; b674 the re-cut act on the kernel the tie rule picks between '
             'SIDE-window and SIDE-trivium at 5, then the document with the most rows outside LICENSED or CITED in data/b670_licensed_table.txt, '
             'alternating with research acts as before; b680 reading 2 of 2')
# ### the author's placement by the navigator's note on the progress report (relay data/b670_author_answers.txt), strikeable; (R280)(8)'s
# ### "b672 the re-cut act on the next kernel by count" stands superseded by it, the supersession cited beside it where it is entered
NEXT_CUT = (('SIDE-window', 25), ('SIDE-trivium', 24))   # ### data/b647_table_kernels.txt, OVERREACHES 5 each, the next by count after the eight:
# ### a tie, the tie rule at OPEN_TRAILS :14238 deciding at b672's ruling

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm is a standing arm carried from b669's face (b669's own act arms
# ### not carried). Each run at HEAD and counted before the face names it. Filled at Component 6.
ACT_ARMS = ()
B669_ACT_ARMS = ('G-R279-ENTERED', 'G-DRY-STEP-CLEAN', 'G-CITATION-CHECKED', 'G-MIDACT-CHECKED', 'G-REPAIR-APPENDED', 'G-PLAN-BEFORE-LEAN',
                 'G-PLAN-SEARCHES-PRINTED', 'G-CONSUMERS-SECTION', 'G-WALK-ZERO', 'G-LANDINGS-BANKED', 'G-SPLIT-MERGED', 'G-OPEN-BRANCH-UNMERGED',
                 'G-HYPOTHESES-SCORED', 'G-KERNEL-FILES-FROM-BANK')
SEALED = ('b670_worklist.py', 'b670_tests.py', 'b670_citation.py', 'b670_record.py', 'b670_checks.py', 'b670_closing.py', 'b670_reg_gate.py',
          'b670_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
