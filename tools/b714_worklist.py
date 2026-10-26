# -*- coding: utf-8 -*-
"""b714_worklist.py -- THE ACT'S DATA, UNDER (R324). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b714: LANE TWO, ACT ONE HUNDRED AND FORTY-ONE, THE KEYSTONE HEADS ACT -- b713 AT ITS WEIGHT; THE TIERS AND THE VISIBILITY MAP; THE
### lv TAG AND THE RE-CUT'S MERGE; THE HEAD OF THE RE-CUT; THE CORRIGENDUM WITH NEW AND REPEAT; THE STANDING CLAUSES AT v5; THE LAW'S IDENTITY;
### THE RESIDUAL; PAIR 7'S RECTANGLE; THE SONIN PRICE. No lean on this host and no runner dispatch (N1).
### Carried by diff from b713_worklist.py (data/b714_carry_worklist.txt) and its stage one rewritten by the Edit tool with this act's objects
### (stage one: step zero; stage two, Component 5, by the Edit tool).
### The act runs in the SAME session as b713 (3bbc6267; the ruling pasted after b713's closing and one read-only request, no /clear): the
### previous act's window is this session from b713's post-push combine to this act's anchor (b711's same-session form).
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'e284156f'         # ### PLACE-papers main before the act (b713's trail, pushed by push-b713-record)
PRE_RELAY = '2f76d11c'      # ### relay main before the act (b713's closing, pushed by push-b713-closing and read back)
DATE = '2026-10-26'
SESSION_ID = '3bbc6267-f2de-40fb-b160-263f3c982c61'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R324) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = SESSION_ID   # ### b713 ran and closed in this same session
PREV_ANCHOR = 'RULING (R323) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b714_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 10440          # ### FINDINGS: b713's entry head
B711_WEIGHT = 10412         # ### FINDINGS: b712's weight line (b713's Component 1)
B711_CORRIGENDUM = 10414    # ### FINDINGS: b713's corrigendum for b712
B711_TRAIL = 15928          # ### OPEN_TRAILS: b713's trail record
B711_FACE = 'data/b713_registration_2026-10-25.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-25-b713.zip'   # ### b713's export, CLEAN on all three clauses over 70 files
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707), restated in b713's trail :15914
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711), discharged by (R324)(3)(i)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it ((R324)(4))
TRAIL_ORDERS = 15948        # ### OPEN_TRAILS: b713's open orders line
TRAIL_RESOLVED = 15954      # ### OPEN_TRAILS: b713's nine items for the author's strike
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence b713 restated
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row ((R324)(10))

# ### the branches step zero deletes ((R324)(11)), named from data/b713_closing.txt's branch row (f) ("the push-b713* branches of relay and
# ### PLACE-papers") and the listing printed before the deletes, one per command, each its own message, in sequence, nothing chained after any
DELETE = (('D:/relay', ('push-b713-closing', 'push-b713-preroot', 'push-b713-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b713-entry', 'push-b713-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R324)(11): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'), ('D:/MY-DOwnloads/PLACE-papers', 'recut-b712-silence'))   # ### the re-cut kept
#                                                             ### until the next act's step zero after its merge ((R324)(3)(ii))

# ### the kernels: none written this act (N1, N5); one tier-one move, the lv port's annotated tag ((R324)(3)(i))
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, unmoved
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main, untouched
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### the deposit, untouched
PORT_BRANCH = 'port-b707'
PORT_TIP = 'cb0aea56354abb3abda3fdaef28429c6605605d5'   # ### port-b707's tip, b712's, unmoved this act
PORT_NEW_TIP = PORT_TIP
LV_TAG = 'v0.11.0'          # ### (R324)(3)(i): annotated, at PORT_TIP, no GitHub release (tier one)
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
REPO_VISIBILITY = 'data/repo_visibility.txt'   # ### (R324)(2): the visibility map, the author's listing of 2026-10-26
REGISTRATIONS = 'data/b712_registrations.txt'   # ### b713's registrations, read at (R324)(7) beside b710's
REG_COMMIT = '67a023887360b74483803ed02c83ae44fdf88f0b'   # ### b712's registrations with the genus control, committed alone
PRICE = 'data/b712_price.txt'
REG_B710 = '41ff1193'        # ### data/b710_registrations.txt committed alone at b710's step zero (the refined law (i))
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b713_read_calls.txt', 'data/b714_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b713 carried them (the ferry's Component 5)
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b714'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', 'day1/Silence_of_Foundations.md')   # ### (R324)(3)(ii) the merge; (4) the head on the word
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'   # ### b712's re-cut on RECUT_BRANCH
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'      # ### b713's tip of RECUT_BRANCH (the two MISSING lines restored), pushed in branch
#                                                             ### mode at b713, merged into main this act by a merge commit ((R324)(3)(ii))
NEXT = ('b715, the registrations act: the composition law for the least negative index sharpened from n = 24 and n = 48 and their '
        'exponents, registered with its falsifier for discriminant -39 and priced; a residual law registered from (R324)(8) where its reading '
        'supports one; the Sonin restriction compiled where (R324)(10) prices it within one act')
NEXT_ACT = 'b715'


def orders_naming(ot_text, act):
    """(R324)(3), the NEXT line's repair: every open-orders row of OPEN_TRAILS whose status names <act> -- a row is a line opening
    `*Appended` that carries `THE ORDER **`W-ORD-`; its status is its text from its last `Status`; returned as (line, order, status). Pure in
    its arguments (b711's port clause was made b713's after the seal and stood outside the sealed NEXT, events :46)."""
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
STANDING_COMMIT = ''        # ### data/standing_clauses_v5.txt, committed alone (filled when made)
VISIBILITY_COMMIT = ''      # ### data/repo_visibility.txt, committed alone (filled when made)
STEPZERO = ''               # ### b713's closing push capture, committed alone at step zero
STEPZERO_STEPS = ''         # ### b713's closing step row (step 23), committed alone at step zero
STEPZERO_BANKS = ''         # ### the step-zero banks and tools, committed together by explicit list
COMPUTE_TOOLS = ('b714_law.py', 'b714_residual.py', 'b714_rect.py')   # ### (R324)(7)-(9): each writing its own bank alone
REPAIRED_TOOLS = ()          # ### shared tools of earlier acts edited by this act (data/b714_tool_repairs.txt), filled at Component 1
REPAIRED_DATA = ()
NEW_TOOLS = ()               # ### (R324)(6): new shared tools (the lettering, the hook), filled at Component 1
# ### b713's commits the act reads ((R324)(1), (7))
B713_PRED_RELAY = 'be4db146a2676fc5758cc81644f669efe4aca03a'   # ### b713's predictions, committed alone
B713_ONSETS_RELAY = '9816b87d31567b02bad2dbf4e67f203c6af2c44f'  # ### b713's onsets
# ### stage two (Component 5): the commits of the components, read from the logs after each was made (filled then)
C1_RELAY = ''
C1_PP = ''
C2_RELAY = ''
C2_PP_MERGE = ''
C3_RELAY = ''
C4_RELAY = ''
SEALED = ('b714_worklist.py', 'b714_tests.py', 'b714_citation.py', 'b714_record.py', 'b714_checks.py', 'b714_closing.py', 'b714_reg_gate.py',
          'b714_regspec.py', 'b714_corrigendum.py', 'b714_carry.py', 'b714_standing.py') + COMPUTE_TOOLS   # ### the report tool NOT sealed (data/b708_rules.txt row (1))
# ### the act's arms over its own banks (Component 5): b713's ritual arms carried, its arms over b713's objects (v3, the port, the dispatches, the
# ### join and its tag, the faces row, the registrations first, nothing computed, the genus control, the price, the re-cut's compile, distance and
# ### branch) replaced by arms over this act's (v4, the six repairs' controls, the membrane, the faces head's edit, the re-cut's additive check and
# ### its branch, the source pin, the list's controls and completeness, the predictions first, the registrations unchanged, the onsets, the
# ### coefficients, no dispatch)
ACT_ARMS = ('G-ANSWERS-BEFORE-WRITES', 'G-ANSWERS-CHECKED', 'G-ARM-SECONDS-BANKED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED',
            'G-CLOSING-DRY-STEP', 'G-CORRIGENDUM-ENTERED', 'G-DEFECTS-LETTERED', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-FIGURES-BANKED', 'G-GUARD-HELD', 'G-LISTINGS-BEFORE-CLAUSES', 'G-PARTS-PRERUN',
            'G-POSTROOT-WRITES-NONE', 'G-R324-ENTERED', 'G-READFIRST-DIFF-BANKED', 'G-REPORT-UNSEALED', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO',
            'G-RULES-ROW-ENTERED', 'G-SCORER-READS-BANKS', 'G-TOOL-REPAIRS', 'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS',
            'G-TRAIL-RESOLVED-EQUAL', 'G-WRITELIST-MIRROR-STATE',
            'G-STANDING-CLAUSES-V4', 'G-REPAIR-CONTROLS', 'G-MEMBRANE-WIRED', 'G-FACES-HEAD-EDIT', 'G-RECUT-ADDITIVE', 'G-SOURCE-PIN',
            'G-LIST-CONTROLS', 'G-LIST-COMPLETE', 'G-PREDICTIONS-FIRST', 'G-REGISTRATIONS-UNCHANGED', 'G-ONSETS-SCORED', 'G-COEFFS-OBSERVED',
            'G-NO-DISPATCH')
