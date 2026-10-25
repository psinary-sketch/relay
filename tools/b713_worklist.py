# -*- coding: utf-8 -*-
"""b713_worklist.py -- THE ACT'S DATA, UNDER (R323). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b713: LANE TWO, ACT ONE HUNDRED AND FORTY, THE RESEARCH ACT AT DISCRIMINANT -15 -- b712 AT ITS WEIGHT; THE AUTHOR'S WORD ON THREE
### ITEMS; THE CORRIGENDUM; THE STANDING CLAUSES AT v4; THE ZERO LIST, THE PREDICTIONS, THE ONSETS AND THE COEFFICIENTS AT -15; THE SOURCE PIN.
### No lean on this host and no runner dispatch (N1).
### Carried by diff from b712_worklist.py (data/b713_carry_worklist.txt) and rewritten whole by the Write tool with this act's objects (stage
### one: step zero; stage two, Component 5, by the Edit tool).
### The act runs in the SAME session as b712 (3bbc6267; the ruling pasted after b712's closing, no /clear): the previous act's window is this
### session from b712's post-push combine to this act's anchor (b711's same-session form).
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'ada52b01'         # ### PLACE-papers main before the act (b712's trail, pushed by push-b712-record)
PRE_RELAY = '1290446c'      # ### relay main before the act (b712's closing, pushed by push-b712-closing and read back)
DATE = '2026-10-25'
SESSION_ID = '3bbc6267-f2de-40fb-b160-263f3c982c61'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R323) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = SESSION_ID   # ### b712 ran and closed in this same session
PREV_ANCHOR = 'RULING (R322) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b713_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 10378          # ### FINDINGS: b712's entry head
B711_WEIGHT = 10346         # ### FINDINGS: b711's weight line (b712's Component 1)
B711_CORRIGENDUM = 10348    # ### FINDINGS: b712's corrigendum for b711
B711_TRAIL = 15890          # ### OPEN_TRAILS: b712's trail record
B711_FACE = 'data/b712_registration_2026-10-25.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-25-b712.zip'   # ### b712's export, CLEAN on all three clauses over 70 files
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707), restated in b712's trail :15914
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711), for the author's word (b714)
TRAIL_ORDERS = 15914        # ### OPEN_TRAILS: b712's open orders line
TRAIL_RESOLVED = 15920      # ### OPEN_TRAILS: b712's three items for the author's strike, given the author's word at (R323)(2)
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence (R323)(2)(ii) edits
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row

# ### the branches step zero deletes ((R323)(7)), named from data/b712_closing.txt :388 and listed before the deletes, one per command, each its
# ### own message, in sequence, nothing chained after any
DELETE = (('D:/relay', ('push-b712-closing', 'push-b712-preroot', 'push-b712-preroot2', 'push-b712-record', 'push-b712-record2')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b712-entry', 'push-b712-record')),
          ('D:/SIDE-faces-join', ('push-b712-join',)))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R323)(7): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'), ('D:/MY-DOwnloads/PLACE-papers', 'recut-b712-silence'))

# ### the kernels: none written this act (N1, N5)
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, unmoved
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main, untouched
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### the deposit, untouched
PORT_BRANCH = 'port-b707'
PORT_TIP = 'cb0aea56354abb3abda3fdaef28429c6605605d5'   # ### port-b707's tip, b712's, unmoved this act
PORT_NEW_TIP = PORT_TIP
KERNEL = 'SIDE-lv-conservation'
JOIN_NEW_TIP = '11a472b90553deaddc411c5d69ec03611ee277c5'   # ### SIDE-faces-join main, unmoved this act
JOIN_RUN = 40210894425
JOIN_TAG = ('v0.1.0', '9bf6fe65582187a92b6ab17e03953efb2cecd913', '11a472b90553deaddc411c5d69ec03611ee277c5')   # ### tag object, peeled
EF_V037 = '38e273477257687d676033be0b0243af84a1e08a'
MAX_DISPATCHES = 0          # ### N1: no runner dispatch

PAPERS = dict()
DATA_STANDING_V1 = 'data/standing_clauses_v1.txt'
DATA_STANDING_V2 = 'data/standing_clauses_v2.txt'
DATA_STANDING_V3 = 'data/standing_clauses_v3.txt'
DATA_STANDING = 'data/standing_clauses_v4.txt'
REGISTRATIONS = 'data/b712_registrations.txt'   # ### read unchanged from REG_COMMIT ((R323)(5))
REG_COMMIT = '67a023887360b74483803ed02c83ae44fdf88f0b'   # ### b712's registrations with the genus control, committed alone
PRICE = 'data/b712_price.txt'
REG_B710 = '41ff1193'        # ### data/b710_registrations.txt committed alone at b710's step zero (the refined law (i))
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b712_read_calls.txt', 'data/b713_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b712 carried them (the ferry's Component 5)
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b713'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', 'FACES_LEDGER.md')   # ### (R323)(2)(ii): the faces ledger's head :8; the re-cut on its branch
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'   # ### b712's re-cut on RECUT_BRANCH; pushed this act in branch mode, not merged
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'      # ### (R323)(2)(iii): the two MISSING lines restored by Edit on RECUT_BRANCH, the
#                                                             ### branch's tip pushed --branch --scratch (read back at the remote), not merged
NEXT = ('b714, the keystone heads act where W-ORD-KEYSTONE-HEADS’s trigger reads met against the join’s tag and the re-cut, the re-cut’s '
        'merge on the author’s word where given, and W-ORD-LV-PORT-TAG on the author’s word where given')
NEXT_ACT = 'b714'


def orders_naming(ot_text, act):
    """(R322)(3), the NEXT line's repair: every open-orders row of OPEN_TRAILS whose status names <act> -- a row is a line opening
    `*Appended` that carries `THE ORDER **`W-ORD-`; its status is its text from its last `Status`; returned as (line, order, status). Pure in
    its arguments (b711's port clause was made b712's after the seal and stood outside the sealed NEXT, events :46)."""
    out = []
    for i, l in enumerate((ot_text or '').replace(chr(13), '').split(NL), 1):
        m = re.search(r'THE ORDER \*\*`(W-ORD-[A-Z0-9-]+)`', l)
        if not (l.startswith('*Appended') and m):
            continue
        k = l.rfind('Status')
        st = l[k:] if k >= 0 else ''
        if re.search(r'\b%s\b' % re.escape(act), st):
            out.append((i, m.group(1), st.strip()))
    return out


def next_line(pp=PP, act=NEXT_ACT, text=None):
    """the NEXT line read at closing time: the ruling's named items (NEXT), then every open-orders row whose status names the next act, read
    from OPEN_TRAILS now (or from <text>, for a control)."""
    if text is None:
        p = os.path.join(pp, 'OPEN_TRAILS.md')
        text = io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''
    rows = orders_naming(text, act)
    return NEXT + '; the open orders whose status names %s (OPEN_TRAILS, read at closing time): %s' % (
        act, '; '.join('%s (:%d, %s)' % (o, i, s[:160]) for i, o, s in rows) or 'NONE')

# ### stage one (step zero): the commits made so far
STANDING_COMMIT = '89bea62186f636921a0f88144114ee9f22bc5b47'   # ### data/standing_clauses_v4.txt, committed alone
STEPZERO = '82e128b4ab4334307364ed7abb612e3501c2195d'          # ### b712's closing push capture, committed alone at step zero
STEPZERO_STEPS = 'b8de4d0c83aa738b268779afb310ad756f6211c9'    # ### b712's closing step row (step 25), committed alone at step zero
STEPZERO_BANKS = 'dc373260a0baa7d6266e87703ee91c7f7cb38199'    # ### the step-zero banks and tools, committed together by explicit list
COMPUTE_TOOLS = ('b713_list.py', 'b713_predict.py', 'b713_onsets.py', 'b713_coeffs.py')   # ### (R323)(5): each writing its own bank alone
REPAIRED_TOOLS = ()          # ### shared tools of earlier acts edited by this act (repair (v): tools/push_gated.sh), filled at Component 1
REPAIRED_DATA = ()
NEW_TOOLS = ()
SEALED = ()                  # ### stage two
ACT_ARMS = ()                # ### stage two
