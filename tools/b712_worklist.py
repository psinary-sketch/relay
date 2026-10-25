# -*- coding: utf-8 -*-
"""b712_worklist.py -- THE ACT'S DATA, UNDER (R322). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b712: LANE TWO, ACT ONE HUNDRED AND THIRTY-NINE, THE RE-CUT ACT -- b711 AT ITS WEIGHT; THE CORRIGENDUM; THE STANDING CLAUSES AT v3;
### THE PORT AND THE JOIN; THE FACES ROW; THE -15 CONTROL REGISTERED AND PRICED; THE NEXT DOCUMENT RE-CUT. No lean on this host; at most four
### runner dispatches, up to three for the port and one for the join ((R322)(4), N1).
### Written whole by the Write tool from b711_worklist.py's form (stage one: step zero; stage two, Component 5, by the Edit tool).
### The act runs in a NEW session (3bbc6267, the author's /clear after b711's closing; the same claude process, pid 3604): the previous act's
### window is b711's own session (ec2d71b5) from its post-push combine to that session's end (b701's form for a new session).
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '693a46d5'         # ### PLACE-papers main before the act (b711's trail, pushed)
PRE_RELAY = '4a383ac8'      # ### relay main before the act (b711's closing, pushed alone and read back)
DATE = '2026-10-25'
SESSION_ID = '3bbc6267-f2de-40fb-b160-263f3c982c61'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R322) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = 'ec2d71b5-9c82-4b17-a54c-30c0ba8a3dce'   # ### b711 ran and closed in its own session; this act's is new
PREV_ANCHOR = 'RULING (R321) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b712_citation_check.txt'

# ### the ledger lines this act's record lines are placed by
B711_ENTRY = 10306          # ### FINDINGS: b711's entry head
B711_WEIGHT = 10282         # ### FINDINGS: b710's weight line (b711's Component 1)
B711_CORRIGENDUM = 10284    # ### FINDINGS: b711's corrigendum for b710
B711_TRAIL = 15850          # ### OPEN_TRAILS: b711's trail record
B711_FACE = 'data/b711_registration_2026-10-25.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-25-b711.zip'   # ### b711's export, CLEAN on all three clauses over 70 files
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707), its latest open-orders row :15876 (b711's trail)
ORDER_LV_PORT_LATEST = 15876
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711), for the author's word

# ### the branches step zero deletes ((R322)(8)), one per command, each its own message, in sequence, nothing chained after any
DELETE = (('D:/relay', ('push-b711-preroot', 'push-b711-preroot2', 'push-b711-root', 'push-b711-record', 'push-b711-closing')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b711-preroot', 'push-b711-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R322)(8): NOT deleted, local or remote

# ### the kernels this act may write ((R322)(4)): the port branch's modules and SIDE-faces-join's lakefile and tag
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, unmoved
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main, untouched ((R322)(4))
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### the deposit, untouched
PORT_BRANCH = 'port-b707'
PORT_TIP = 'be3052acd2c6fe013ba482a5eddcfb236ce88738'   # ### b711's one commit on port-b707, the base of this act's edit
PORT_BASE = '92af8a344f1161e5f91df448f270bd3dea304429'  # ### b709's commit on port-b707
PORT_MODULE = 'SIDELvConservation/DirichletC7Order.lean'
PORT_LINE = 501
PORT_RUN_B711 = 40154341879
JOIN_TIP = 'b37a7b6e6322b8f99b2e1bc5c43cae248782c991'
KERNEL = 'SIDE-lv-conservation'
MAX_PORT_DISPATCHES = 3
MAX_DISPATCHES = 4

PAPERS = dict()
DATA_STANDING_V1 = 'data/standing_clauses_v1.txt'
DATA_STANDING_V2 = 'data/standing_clauses_v2.txt'
DATA_STANDING = 'data/standing_clauses_v3.txt'
REGISTRATIONS = 'data/b712_registrations.txt'
REG_B710 = '41ff1193'        # ### data/b710_registrations.txt committed alone at b710's step zero (the refined law (i), carried at (R322)(6)(ii))
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt', 'data/b711_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b711 carried them (the ferry's Component 5)
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b712'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', 'FACES_LEDGER.md')   # ### (R322)(5): the faces ledger's row; the re-cut on its branch, not main
NEXT = ('b713, the research act at discriminant -15 where (R322)(6) prices it within one act’s budget, its registrations read unchanged from '
        'data/b712_registrations.txt’s commit; the keystone heads’ trigger read against the compile steps (4) and (7) reach')
NEXT_ACT = 'b713'


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
REG_COMMIT = '67a023887360b74483803ed02c83ae44fdf88f0b'        # ### data/b712_registrations.txt with its genus control, committed alone, first
STANDING_COMMIT = 'cf193d0e7d19014359bc9c05ee4c41af6620bbd5'   # ### data/standing_clauses_v3.txt, committed alone
STEPZERO = 'ddd8785d08b760599c465a56e57fe3b1147ec824'          # ### b711's closing push capture, committed alone at step zero
STEPZERO_STEPS = 'cb8a8580249f2a150d1a805dba36a06d4b921b11'    # ### b711's closing step row, committed alone at step zero
STEPZERO_BANKS = '46750da99871168eed2276f399a049d124ebf5c1'   # ### the step-zero banks and tools, committed together by explicit list
C1_RELAY = '3e1c958c7434b5b7ecc395d53d4471b19c4e4401'        # ### Component 1: the weight line, the corrigendum, the repairs and controls
C1_PP = 'a7f77d3ad08414881899fc8606c36bf817652d9b'           # ### FINDINGS :10346 (b711's weight) and :10348 (the corrigendum)
B712_WEIGHT = 10346
B712_CORRIGENDUM = 10348
C2_RELAY = 'ee71a7a9'        # ### Component 2: the port, the join, the grade and the tag's banks
C2_PP = ''
C3_RELAY = 'c885392d'        # ### Component 3: the price tool and its banks
C3_PP = '2351a31a799f0b887b7236865c215c55b236a614'           # ### FACES_LEDGER.md's b712 update block, by the Edit tool
C4_RELAY = 'c2492dcf'        # ### Component 4: the re-cut tool, its banks and the worklist's re-cut rows
C4_PP = ''                   # ### none on main: the re-cut is on its branch, not pushed
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'   # ### on RECUT_BRANCH from 2351a31a; distance 19 -> 1 (the held :210 cell), MATCHES 143 of 143
C3_RELAY_B = ''
INDEPENDENCE_COMMIT = ''     # ### no supplement this act
REG_B709 = 'data/b709_registrations.txt'
B709_TRAIL_HEAD = '### b711 — lane two, act one hundred and thirty-eight, the research act under (R321)'   # ### the previous act's trail head (the suite's name carried)
PORT_FILE = PORT_MODULE
PORT_LABEL = 'port'
PORT_RUN = None              # ### this act's port dispatches, read by run id at Component 2 (up to three)
PORT_EDIT1 = '42da39ea2c03859ef6e74a9b752d9783816b430a'     # ### edit 1 (:501) on be3052ac; run 40210206913 held at :574:39
PORT_NEW_TIP = 'cb0aea56354abb3abda3fdaef28429c6605605d5'   # ### edit 2 (:574) on 42da39ea; run 40210536172 built 12 of 12; each pushed by push_gated.sh branch mode
PORT_RUNS = (40210206913, 40210536172)
JOIN_NEW_TIP = '11a472b90553deaddc411c5d69ec03611ee277c5'   # ### SIDE-faces-join main: lv-conservation re-pinned at PORT_NEW_TIP, pushed from push-b712-join
JOIN_RUN = 40210894425       # ### faces_join DERIVES at the standard three (data/b712_join_grade.txt)
JOIN_TAG = ('v0.1.0', '9bf6fe65582187a92b6ab17e03953efb2cecd913', '11a472b90553deaddc411c5d69ec03611ee277c5')   # ### tag object, peeled (data/b712_join_tag.txt)
EF_V037 = '38e273477257687d676033be0b0243af84a1e08a'
REPAIRED_TOOLS = ()          # ### shared tools of earlier acts edited by this act: none
REPAIRED_DATA = ()
NEW_TOOLS = ()               # ### no shared tool new this act (act_membrane.py was b711's)
COMPUTE_TOOLS = ('b712_genus_control.py',)   # ### the genus control alone, an identity between coefficients (N3: no -15 zero computed)
SEALED = ('b712_worklist.py', 'b712_tests.py', 'b712_citation.py', 'b712_record.py', 'b712_checks.py', 'b712_closing.py', 'b712_reg_gate.py',
          'b712_regspec.py', 'b712_corrigendum.py', 'b712_carry.py', 'b712_standing.py', 'b712_price.py', 'b712_recut.py',
          'b712_locate.py') + COMPUTE_TOOLS   # ### the report tool NOT sealed ((R322)(3): a report and not an arm)
# ### the act's arms over its own banks (Component 5): b711's ritual arms carried, its arms over b711's objects (v2, the supplement, the port
# ### held, the order, the five computations, the registrations read unchanged) replaced by arms over this act's (v3, the repairs' controls, the
# ### membrane, the port, the dispatches, the join and its tag, the faces row, the registrations first, nothing computed, the genus control, the
# ### price, the re-cut's compile, distance and branch)
ACT_ARMS = ('G-ANSWERS-BEFORE-WRITES', 'G-ANSWERS-CHECKED', 'G-ARM-SECONDS-BANKED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED',
            'G-CLOSING-DRY-STEP', 'G-CORRIGENDUM-ENTERED', 'G-DEFECTS-LETTERED', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-FIGURES-BANKED', 'G-GUARD-HELD', 'G-LISTINGS-BEFORE-CLAUSES', 'G-PARTS-PRERUN',
            'G-POSTROOT-WRITES-NONE', 'G-R322-ENTERED', 'G-READFIRST-DIFF-BANKED', 'G-REPORT-UNSEALED', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO',
            'G-RULES-ROW-ENTERED', 'G-SCORER-READS-BANKS', 'G-TOOL-REPAIRS', 'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS',
            'G-TRAIL-RESOLVED-EQUAL', 'G-WRITELIST-MIRROR-STATE',
            'G-STANDING-CLAUSES-V3', 'G-REPAIR-CONTROLS', 'G-MEMBRANE-WIRED', 'G-PORT-BANKED', 'G-DISPATCHES-AT-MOST-FOUR', 'G-JOIN-DERIVES',
            'G-JOIN-TAG', 'G-FACES-ROW', 'G-REGISTRATIONS-FIRST', 'G-NOTHING-COMPUTED', 'G-GENUS-CONTROL', 'G-PRICE-BANKED',
            'G-RECUT-COMPILE-FIRST', 'G-RECUT-DISTANCE', 'G-RECUT-ON-BRANCH')
