# -*- coding: utf-8 -*-
"""b700_worklist.py -- THE ACT'S DATA, UNDER (R310). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b700: LANE TWO, ACT ONE HUNDRED AND TWENTY-SEVEN, THE READING ACT, READING 4 -- b699 AT ITS WEIGHT; THE TRAIL'S DEFECTS LINE, THE HEAD
### LINE'S COUNTS AND THE ROOT-NAMED CLAIM BY CORRIGENDUM; THE CENSUS WITH FIVE READINGS ADDED; THE SLATE FOR b701 PRICED. No lean on this host;
### no runner dispatched. Written whole by the Write tool from b699_worklist.py's form (stage one: step zero; stage two, Component 4, by the
### Edit tool). The act runs in the session b698 and b699 ran in (c677eaf2); the anchor is (R310)'s line.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '049855a'          # ### PLACE-papers main before the act (b699's record, pushed)
PRE_RELAY = '85dd43d7'      # ### relay main before the act (b699's closing, pushed)
DATE = '2026-10-21'
SESSION_ID = 'c677eaf2-5ebd-414d-85fe-7a54a52c47cd'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R310) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b700_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B699_ENTRY = 9726           # ### FINDINGS: b699's entry head
B699_TRAIL = 15336          # ### OPEN_TRAILS: b699's trail record
B699_FACE = 'data/b699_registration_2026-10-21.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-21-b699.zip'

# ### the branches step zero deletes ((R310)(5)), one per command, each its own message, in sequence, nothing chained after any
DELETE = (('D:/relay', ('push-b699', 'push-b699-root', 'push-b699-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b699', 'push-b699-root')),
          ('D:/SIDE-substrate-cluster', ('push-b699-substrate-main', 'push-b699-substrate-merge', 'recut-substrate-cluster-b699')))
DELETE_REMOTE = (('D:/SIDE-substrate-cluster', 'recut-substrate-cluster-b699'),)

FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b700'))
EF_DIR = 'D:/SIDE-explicit-formula'
