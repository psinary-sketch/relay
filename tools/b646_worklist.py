# -*- coding: utf-8 -*-
"""b646_worklist.py -- THE ACT'S DATA, UNDER (R256). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b646: LANE THREE, ACT SEVENTY-THREE -- THE EDIT-ROUTE ARM; THE SEVEN COMPANIONS THROUGH THE INTAKE FORM; THE MONOGRAPH'S AGENDA
### TO THE AUTHOR; THE DEPOSIT DESCRIPTION AT v3 UNDER COMPOSITION RULES, THE MET LIST WIDENED, dedekind_rhs' RE-GRADED, A FOURTH READER,
### THE DRAFT HELD; THE SEAT'S MEMORY THROUGH THE TABLE; THE CROSS-FIELD RESONANCES ENTRY. The face is sealed after Components 2-5:
### these tools are written by the Write tool and edited through the Edit tool before the seal, sealed at Component 6.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '96779e5'          # ### PLACE-papers main before the act (b645's record)
PRE_RELAY = '8ba62dc2'      # ### relay main before the act (b645's closing)
STEPZERO = '61b92a3b'       # ### relay: b645's closing push-out bank, committed at step zero
ARM_COMMIT = '1711ce74'     # ### relay: the edit-route arm and its planted test, committed alone
DATE = '2026-10-09'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f004d01d-ad93-416c-a916-fe6e52403753/scratchpad'
HOLD = 2560
ANCHOR = 'RULING (R256) BEGIN'   # ### the command bank starts at the ruling's first delivery in the seat's session
MEMDIR = 'C:/Users/echo chamber/.claude/projects/D--/memory'

EF, EF_PIN, EF_TAG = 'D:/SIDE-explicit-formula', '82550e4', 'v0.26'
KERNEL, KERNEL_TAG, KERNEL_PIN = 'D:/SIDE-kernel', 'v1.5', '0e5233f'

# ### (R256)(3): the seven Day 1 companions at their patch labels (PLACE-papers day1/, at PRE_PP)
COMPANIONS = (('Exhaustive_Enumeration', 'v2.3.1'), ('Which_Structure_Confines', 'v2.3.1'), ('Spectral_Inertness', 'v2.3.1'),
              ('Seven_Mechanism_Classes', 'v3.3.1'), ('Third_Identity_Element', 'v2.3.1'), ('Silence_of_Foundations', 'v2.3.1'),
              ('ONE_PAGE_PROOF', 'v1.0.1'))
AGENDA = 'b645_v6_agenda.txt'   # ### (R256)(3): b645 wrote the agenda; no b646 agenda file

# ### the ledger lines the act reads and addresses
B645_ENTRY = 8061
B645_OUTSIDERS = 8079
B645_RECORD = 13633
RESEARCH_ARC_MODEL = 11521      # ### OPEN_TRAILS's research-arc line, the form's model (b560, (R170)(2))
SURROUND = 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md'

DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

SEALED = ('b646_worklist.py', 'b646_tests.py', 'b646_record.py', 'b646_checks.py', 'b646_closing.py', 'b646_reg_gate.py', 'b646_regspec.py',
          'edit_route.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
