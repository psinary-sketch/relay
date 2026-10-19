# -*- coding: utf-8 -*-
"""b689_worklist.py -- THE ACT'S DATA, UNDER (R299). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b689: LANE TWO, ACT ONE HUNDRED AND SIXTEEN, THE RESEARCH ACT -- b688 AT ITS WEIGHT; DEFECT (f) REPAIRED BY CORRIGENDUM; THE
### HEAD-LINE ARM REPAIRED; THE STRIP-FREE LI CONVERSE PLANNED FROM ITS BANKS, RAISED, AND ON THE AUTHOR'S WORD BUILT ON A BRANCH.
### No lean on this host. Written whole by the Write tool from b688_worklist.py's form. The act opens a NEW session (2c300355): the ruling
### is its first, so the anchor is (R299)'s line and the capture runs from it; the process listing before any bank write showed one seat.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'c3af808'          # ### PLACE-papers main before the act (b688's record, pushed)
PRE_RELAY = '007d4ead'      # ### relay main before the act (b688's closing, pushed)
DATE = '2026-10-19'
SESSION_ID = '2c300355-703e-4575-81bc-2631a70202cf'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R299) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b689_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B688_ENTRY = 9314           # ### FINDINGS: b688's entry head
B688_CITE_SENTENCE = 9320   # ### FINDINGS: b688's citation sentence, "the two commit cites ... tested directly" (defect (f))
B688_TRAIL = 14924          # ### OPEN_TRAILS: b688's trail record
B688_TRAIL_DEFECTS = 14946  # ### OPEN_TRAILS: b688's trail record's defects line

# ### the branches step zero deletes ((R299)(6)), one per command, each its own message, in sequence
DELETE = (('D:/relay', ('push-b688-root', 'push-b688', 'push-b688-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b688-root', 'push-b688')),
          ('D:/SIDE-li-map', ('push-b688-main', 'push-b688-merge', 'recut-li-map-b688')),
          ('D:/SIDE-spinor', ('push-b688-spinor-merge', 'recut-spinor-b688r')))
DELETE_REMOTE = ()

# ### (R299)(2): the corrigendum and the arm
CORRIGENDA_BANK = 'data/b675_corrigenda.txt'
ARM_TOOL, ARM_LINE = 'tools/rule_arms.py', 387

# ### (R299)(3)-(4): the strip-free Li converse
KERNEL = 'D:/SIDE-explicit-formula'
KERNEL_REPO = 'psinary-sketch/SIDE-explicit-formula'
V033 = '95f8dc8'            # ### v0.33's commit (peeled)
BRANCH = 'strip-free-b689'
STRIP_PLAN, STRIP_SECTION = 'data/b679_strip_plan.txt', 11
STRIP_USES = 'data/b676_strip_uses.txt'

NEXT = ('b690, the reading act, reading 3: the census of residues (R3b, the two SIDE-li-map residues, any from b689), the keystone lag '
        're-read, the rules and arms census, P3`s new status read across every line naming T-COUNT or "stated, not proved" at Q0, the faces '
        'successor row of (R299)(5) raised; b691 the re-cut act: the tie between SIDE-archimedean and SIDE-rcurve at 2 broken by b674`s rule')

SEALED = ('b689_worklist.py', 'b689_tests.py', 'b689_citation.py', 'b689_record.py', 'b689_checks.py', 'b689_closing.py', 'b689_reg_gate.py',
          'b689_regspec.py')
PARTS = ('standing-a', 'standing-c', 'standing-b', 'act')     # ### data/b684_rules.txt row (1)


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
