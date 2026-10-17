# -*- coding: utf-8 -*-
"""b675_worklist.py -- THE ACT'S DATA, UNDER (R285). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b675: LANE TWO, ACT ONE HUNDRED AND TWO, THE RESEARCH ACT -- b674 AT ITS WEIGHT; THE KERNEL'S HYPOTHESES READ AT Q0; THE
### COMPOSITION BOUND INSTANTIATED AND TESTED AGAINST THE CERTIFIED ZEROS; THE CLOSING TOOL REPAIRED AT CARRY.
### No lean on this host. Written whole by the Write tool from b674_worklist.py's form. The face is sealed after Components 1-4, the
### closing dry-run and the entry dry-run step.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '6b95ac8'          # ### PLACE-papers main before the act (b674's record, pushed)
PRE_RELAY = '27992411'      # ### relay main before the act (b674's closing, pushed)
DATE = '2026-10-16'
SESSION_ID = '51ceaa11-0301-4ed4-9e1c-71b70f1e78ca'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R285) BEGIN'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b675_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B674_ENTRY = 8851           # ### FINDINGS: b674's entry head
B674_TRAIL = 14508          # ### OPEN_TRAILS: b674's trail record

# ### b674's commits as the corrigenda bank corrects them ((R285)(1))
B674_RECORD_RELAY, B674_RECORD_PP, B674_CLOSING = '92e003e7', '6b95ac8', '27992411'
B674_HEAD_RELAY, B674_HEAD_PP = '7d432c88', '4cb90e0'      # ### the head line's commits: the pre-root pushes

# ### the branches step zero deletes ((R285)(3)); the remote deletions named apart
KE = 'D:/SIDE-explicit-formula'
WD = 'D:/SIDE-window'
DELETE = (('D:/relay', ('push-b674', 'push-b674-root', 'push-b674-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b674', 'push-b674-root')),
          (WD, ('push-b674-workflow', 'push-b674-merge', 'recut-window-b674')))
DELETE_REMOTE = ((WD, 'recut-window-b674'), (KE, 'chi-li-b669'))
MERGE = 'e36ea316e363b1fad04b7fa9def0fc7f2e78188f'           # ### SIDE-explicit-formula main = v0.32
CHI_LI_TIP = '5050a46acf269e7745ce678c3deb8deed9f2d0bf'

# ### the object ((R285)(4)): the narrowed list, read through its .gz, the inner JSON's sha256 from b671's hashes bank
ZEROS_GZ = 'b671_epstein_zeros_narrowed.json.gz'
ZEROS_GZ_SHA = '51d9e6322510b738ba1332b1945bde75363a339f9fd567ea099bb675abd6f804'
ZEROS_JSON_SHA = 'cd3a8ea1dcc7660c66a3b73a08d7c471ee6980e62e5bc4330e92e0c1b40e415b'
KREV = 'e36ea31'
LEAN = {'HStrip': ('SIDEExplicitFormula/RestBound.lean', 40), 'HCount': ('SIDEExplicitFormula/RestBound.lean', 44),
        'remainder_le': ('SIDEExplicitFormula/Schema/LiRemainder.lean', 175), 'C': ('SIDEExplicitFormula/Schema/LiRemainder.lean', 180),
        'S5': ('SIDEExplicitFormula/Schema/LiConverseCfg.lean', 157), 's': ('SIDEExplicitFormula/Schema/LiConverseCfg.lean', 192),
        'V4+': ('SIDEExplicitFormula/Schema/LiConverseCfg.lean', 259), 'A0Q': ('SIDEExplicitFormula/Schema/EpsteinQ0.lean', 104),
        'Q0Count': ('SIDEExplicitFormula/Schema/EpsteinQ0.lean', 108)}

NEXT = ('b676, the re-cut act, the document named by the tie-break rule of data/b674_rules.txt read from the licensed table at step zero '
        '(SIDE-trivium at 5 the carried candidate), its ruling then; b677 the research act on W-ORD-MAP-ANGLE-FORM; b680 the reading act, '
        'reading 2 of 2 -- `(R285)`(11)')

# ### (R264)(2), the freeze: the act's arms over its own banks; every other arm is a standing arm carried from b674's face (b674's own act
# ### arms not carried). Each run at HEAD and counted before the face names it.
ACT_ARMS = ('G-DRY-STEP-CLEAN', 'G-CLOSING-DRY-STEP', 'G-CITATION-CHECKED', 'G-MIDACT-CHECKED', 'G-R285-ENTERED', 'G-ROWGEN-STEPZERO',
            'G-BRANCHES-BANKED', 'G-CORRIGENDA-BANKED', 'G-HYPOTHESES-BEFORE-SUMS', 'G-PLAN-BEFORE-SUMS', 'G-BENCH-BALLS',
            'G-CONTROLS-AS-PLANNED', 'G-READINGS-CITED', 'G-RULES-BANKED', 'G-TOOL-REPAIRS')
SHARED_APPENDED = ()
SEALED = ('b675_worklist.py', 'b675_tests.py', 'b675_citation.py', 'b675_record.py', 'b675_checks.py', 'b675_closing.py', 'b675_reg_gate.py',
          'b675_regspec.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
