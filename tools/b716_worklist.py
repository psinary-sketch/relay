# -*- coding: utf-8 -*-
"""b716_worklist.py -- THE ACT'S DATA, UNDER (R326). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b716: LANE TWO, ACT ONE HUNDRED AND FORTY-THREE, THE REGISTRATIONS ACT -- b715 AT ITS WEIGHT; THE CORRIGENDUM; THE TOOLSET AT
### v1.1.0; THE -39 REGISTRATION; THE KEYSTONE ITEMS; TWO PRICES. No lean on this host; runner dispatches dry builds for (R326)(6)(i) alone (N1).
### Carried by diff from b715_worklist.py (data/b716_carry_worklist.txt) and its stage one rewritten by the Edit tool with this act's objects
### (stage one: step zero; stage two, Component 5, by the Edit tool).
### The act runs in a NEW session (0c15655e; the seat cleared after b715's closing, a read-only request then the ruling pasted): the
### previous act's window is b715's session bde68a30 from b715's post-push combine to its end (b671's session-change form).
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '4ff9e8a4'         # ### PLACE-papers main before the act (b715's trail, pushed by push-b715-record)
PRE_RELAY = 'cf51ee95'      # ### relay main before the act (b715's closing, pushed by push-b715-closing and read back)
DATE = '2026-10-27'
SESSION_ID = '0c15655e-4d46-485e-9b80-fada479be2d0'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R326) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = 'bde68a30-a303-4bfc-a0eb-fd2e81af3fd2'   # ### b715 ran and closed in its own session; this act's seat is a new one
PREV_ANCHOR = 'RULING (R325) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b716_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 10582          # ### FINDINGS: b715's entry head (b716's Component 1 reads :10582; the carry left b714's :10512)
B711_WEIGHT = 10550         # ### FINDINGS: b714's weight line (b715's Component 1)
B711_CORRIGENDUM = 10552    # ### FINDINGS: b715's corrigendum for b714 (data/b675_corrigenda.txt row (35))
B711_TRAIL = 16006          # ### OPEN_TRAILS: b715's trail record (the carry left b714's :15962)
B711_FACE = 'data/b715_registration_2026-10-26.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-26-b715.zip'   # ### b715's export, CLEAN on all three clauses over 70 files
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707), restated in b715's trail :15914
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711), discharged by (R326)(3)(i)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it ((R326)(4))
TRAIL_ORDERS = 15992        # ### OPEN_TRAILS: b715's open orders line
TRAIL_RESOLVED = 15998      # ### OPEN_TRAILS: b715's nine items for the author's strike
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence b715 restated
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row ((R326)(10))

# ### the branches step zero deletes ((R326)(7)): push-b715-record and push-b715-closing, by name, each read from the listings and `--merged`
# ### printed before the deletes, one per command, each its own message, in sequence, nothing chained after any (push-b715-entry and
# ### push-b715-preroot were deleted inside b715, its event (7); the relay carries push-b715-record and push-b715-closing, PLACE-papers
# ### push-b715-record)
DELETE = (('D:/relay', ('push-b715-closing', 'push-b715-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b715-record',)))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R326)(7): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'),)

# ### the kernels: none written this act (N1, N5); no tier-one move; SIDE-kernel and SIDE-meta read for (R326)(6)-(7) and not written
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PATHS = ('D:/relay', PP, EF_DIR, LV_DIR, JOIN_DIR, KERNEL_DIR, META_DIR)   # ### (R326)'s PATHS, listed at step zero
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, unmoved
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main, untouched
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### the deposit, untouched
PORT_BRANCH = 'port-b707'
PORT_TIP = 'cb0aea56354abb3abda3fdaef28429c6605605d5'   # ### port-b707's tip, b712's, unmoved this act
PORT_NEW_TIP = PORT_TIP
LV_TAG = 'v0.14.0'          # ### b715's tag ((R325)(3)(i), data/b715_lv_tag.txt), at PORT_TIP, read and not moved this act
LV_TAG_OBJECT = '0e7c3527c8ff693c34126b57d1b1587149e5371c'   # ### annotated, at PORT_TIP, no GitHub release (tier one)
LV_TAG_RULED = 'v0.11.0'
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
DATA_STANDING_V4 = 'data/standing_clauses_v4.txt'
DATA_STANDING = 'data/standing_clauses_v5.txt'
REPO_VISIBILITY = 'data/repo_visibility.txt'   # ### (R325)(2): the visibility map, the author's listing of 2026-10-26; (R326)(6) reads it
REGISTRATIONS = 'data/b712_registrations.txt'   # ### b713's registrations; the registrations moved to b716 ((R326)), read not written
REG_COMMIT = '67a023887360b74483803ed02c83ae44fdf88f0b'   # ### b712's registrations with the genus control, committed alone
PRICE = 'data/b712_price.txt'
REG_B710 = '41ff1193'        # ### data/b710_registrations.txt committed alone at b710's step zero (the refined law (i))
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b715_read_calls.txt', 'data/b716_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b715 carried them (the ferry's Component 5)
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b716'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md'   # ### (R326)(7): the census read; its rows the readfirst's
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'    # ### (R326)(7): the next edition, on main, the chain's rows
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', CENSUS_NEW)   # ### (R326)(1)-(2) the record lines; (7) the census at v0.8.2
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'   # ### b712's re-cut on RECUT_BRANCH
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'      # ### b713's tip of RECUT_BRANCH, merged into main at b715 (a86c9429); the
#                                                             ### branch deleted at this act's step zero ((R326)(9))
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'
NEXT = ('b716, the registrations act: the carried items of (R326)(8) on the standing toolset -- the heads draft and the question of inline '
        'footings or a companion correspondence; the six lint hits; the 19 names with no pin; the SIDESystem finding at Silence :212 and :183; '
        'the composition law for the least negative index and its -39 registration; the residual; the rectangle certification of pair 7; the '
        'Sonin restriction\'s price and the law\'s identity reading')
NEXT_ACT = 'b716'


def orders_naming(ot_text, act):
    """(R326)(3), the NEXT line's repair: every open-orders row of OPEN_TRAILS whose status names <act> -- a row is a line opening
    `*Appended` that carries `THE ORDER **`W-ORD-`; its status is its text from its last `Status`; returned as (line, order, status). Pure in
    its arguments (b711's port clause was made b715's after the seal and stood outside the sealed NEXT, events :46)."""
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
ACT_CURRENT = 'data/act_current.json'   # ### (R326)(3)(ii): the act's figures, written at step zero and committed alone
STANDING_DIR = 'tools/standing'         # ### (R326)(3): the standing close toolset, versioned by tools/standing/VERSION
ACT_CURRENT_COMMIT = '7dee7cad186132e251444896866145a3e8567fed'   # ### data/act_current.json committed alone
STEPZERO = 'de51ac0f85b7e2795440d5f3082e2e475453253c'           # ### b715's closing push capture, committed alone at step zero ((R326)(9))
STEPZERO_STEPS = '140e6f01ff4079070bd5a71148e87d73bcd481af'     # ### b715's step row 18, committed alone
STEPZERO_HASHES = '0e8f8463c7ab75f33d5f4a45cb6f43eaa451f2f9'    # ### data/b715_bank_hashes.json, committed alone
STEPZERO_REFUSALS = '771306c9f036e1071173c067f6792e79b5adb6c3'  # ### data/b715_hook_refusals.txt as it stands, committed alone, beside event (10)
STEPZERO_BANKS = '8e5610f02709f3a34e8980c3c00a73f36fa2c608'     # ### the step-zero banks and tools, committed together by explicit list
STANDING_COMMIT = ACT_CURRENT_COMMIT    # ### no standing clauses written this act (v5 b715's): the arms reading this name read the act's figures' commit
VISIBILITY_COMMIT = ACT_CURRENT_COMMIT  # ### no visibility map written this act (b715's)
COMPUTE_TOOLS = ()                      # ### no compute tool this act
REPAIRED_TOOLS = ('b303_pins.py', 'mirror_build.ps1')   # ### shared tools of earlier acts edited by ruling ((R326)(5)-(6); data/b716_tool_repairs.txt (C))
REPAIRED_DATA = ()
STANDING_FILES = ('VERSION', 'act.py', 'arms.py', 'close.py', 'components.py', 'controls.py', 'hook.py', 'repairs.py', 'replay.py', 'roster.py', 'scan.py')
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### (R326)(3): the standing close toolset at v1.0.0, sealed by hash beside the act's tools
# ### b715's commits the act reads ((R326)(1))
B714_CLOSING = '1992a71c4670ac3118f383f1bbf0ef9e992fa15a'
B714_RECORD = 'ce2c846400284eee07c6451757727f2a5f9bc68f'
B714_ROOT = '242b06d6e9bcca81e1d86d02c089b829354df27b347e5ac7265c94979e66bd0b'
# ### stage two (Component 6, before the lock): the commits of the components, read from the logs after each was made
C1_RELAY = '7d8d3d98b93dbbc686046beb2faafe9c04e0d773'      # ### b715's weight line and the corrigendum's banks, the corrigenda row (35)
C1_PP = '2d9654b39eb3737fe1ab840f88b039c375bfd8c5'         # ### the weight line and the corrigendum entry (FINDINGS :10550, :10552)
C2_PREP = '93f32342d073e2c384a9398aff6d9407a0fea0e7'       # ### the measurement before the copy and the author's word (1)
C2_RELAY = 'cfee370b4b0ff29d3cf7e795515855372986abfb'      # ### (R326)(3): the standing toolset at v1.0.0, the scan, the replay, the coverage table
C3_RELAY = 'b3ff33ce00df176784f2e755cbd679469380f985'      # ### (R326)(4): the class repairs and their controls; the hook switched
C4_RELAY = '4660aea044eef1199130e16cb2c0f56952951c92'      # ### (R326)(5)-(6): the roster from main (the author's word (2)), the pins census
C5_RELAY = '2694cfef6ddb6ec54e0e8ae161ead6e8eb635e5d'      # ### (R326)(7): the chain rows' evidence and the census diff
C5_PP = '332710b83192b6cad9774e3cb549dd03463a0e84'         # ### (R326)(7): the census v0.8.2 on main
SEALED = ('b716_worklist.py', 'b716_tests.py', 'b716_citation.py', 'b716_record.py', 'b716_checks.py', 'b716_closing.py', 'b716_reg_gate.py',
          'b716_regspec.py', 'b716_corrigendum.py', 'b716_carry.py', 'b716_standing.py', 'b716_import_closure.py') + NEW_TOOLS + COMPUTE_TOOLS   # ### the report tool NOT sealed (data/b708_rules.txt row (1)); the toolset sealed by hash beside the act's tools ((R326) Component 6)
# ### the act's arms over its own banks (Component 6): b715's ritual arms carried, its arms over b715's objects (v5 written, the lv tag, the re-cut
# ### merged, the heads draft held, the law, the residual, the rectangle, the Sonin price, the pilot; b715's hook and repairs tools) replaced by
# ### arms over this act's (the act's figures, the toolset's scan and replay, the coverage table, the class repairs' controls, the standing hook,
# ### the roster from main, the pins census, the census rows)
ACT_ARMS = ('G-ANSWERS-BEFORE-WRITES', 'G-ANSWERS-CHECKED', 'G-ARM-SECONDS-BANKED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED',
            'G-CLOSING-DRY-STEP', 'G-CORRIGENDUM-ENTERED', 'G-DEFECTS-LETTERED', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-FIGURES-BANKED', 'G-GUARD-HELD', 'G-LISTINGS-BEFORE-CLAUSES', 'G-PARTS-PRERUN',
            'G-POSTROOT-WRITES-NONE', 'G-R326-ENTERED', 'G-READFIRST-DIFF-BANKED', 'G-REPORT-UNSEALED', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO',
            'G-RULES-ROW-ENTERED', 'G-SCORER-READS-BANKS', 'G-TOOL-REPAIRS', 'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS',
            'G-TRAIL-RESOLVED-EQUAL', 'G-WRITELIST-MIRROR-STATE',
            'G-REPAIR-CONTROLS', 'G-MEMBRANE-WIRED', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-ACT-CURRENT', 'G-TOOLSET-SCAN',
            'G-TOOLSET-REPLAY', 'G-COVERAGE-TABLE', 'G-IMPORT-CLOSURE', 'G-ROSTER-FROM-MAIN', 'G-PINS-CENSUS', 'G-CENSUS-ROWS',
            'G-NO-DISPATCH')
