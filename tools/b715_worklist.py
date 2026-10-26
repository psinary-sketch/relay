# -*- coding: utf-8 -*-
"""b715_worklist.py -- THE ACT'S DATA, UNDER (R325). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b715: LANE TWO, ACT ONE HUNDRED AND FORTY-TWO, THE TOOLSET ACT -- b714 AT ITS WEIGHT; THE CORRIGENDUM; ONE STANDING CLOSE TOOLSET
### AND ITS REPLAY; THE CLASS REPAIRS; THE MIRROR'S ROSTER; THE PINS CENSUS; THE CHAIN'S CENSUS ROWS. No lean on this host and no runner
### dispatch (N1).
### Carried by diff from b714_worklist.py (data/b715_carry_worklist.txt) and its stage one rewritten by the Edit tool with this act's objects
### (stage one: step zero; stage two, Component 5, by the Edit tool).
### The act runs in a NEW session (bde68a30; the seat cleared after b714's closing, the ruling pasted as the session's first message): the
### previous act's window is b714's session 3bbc6267 from b714's post-push combine to its end (b671's session-change form).
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '6959f75f'         # ### PLACE-papers main before the act (b714's trail, pushed by push-b714-record)
PRE_RELAY = '1992a71c'      # ### relay main before the act (b714's closing, pushed by push-b714-closing and read back)
DATE = '2026-10-26'
SESSION_ID = 'bde68a30-a303-4bfc-a0eb-fd2e81af3fd2'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R325) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = '3bbc6267-f2de-40fb-b160-263f3c982c61'   # ### b714 ran and closed in b713's session; this act's seat is a new one
PREV_ANCHOR = 'RULING (R324) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b715_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 10512          # ### FINDINGS: b714's entry head
B711_WEIGHT = 10474         # ### FINDINGS: b713's weight line (b714's Component 1)
B711_CORRIGENDUM = 10476    # ### FINDINGS: b714's corrigendum for b713
B711_TRAIL = 15962          # ### OPEN_TRAILS: b714's trail record
B711_FACE = 'data/b714_registration_2026-10-26.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-26-b714.zip'   # ### b714's export, CLEAN on all three clauses over 70 files
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707), restated in b714's trail :15914
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711), discharged by (R325)(3)(i)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it ((R325)(4))
TRAIL_ORDERS = 15992        # ### OPEN_TRAILS: b714's open orders line
TRAIL_RESOLVED = 15998      # ### OPEN_TRAILS: b714's nine items for the author's strike
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence b714 restated
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row ((R325)(10))

# ### the branches step zero deletes ((R325)(9)): push-b714-entry, push-b714-preroot, push-b714-record, push-b714-closing and
# ### recut-b712-silence (merged at a86c9429), each read from the listings and `--merged` printed before the deletes, one per command, each its
# ### own message, in sequence, nothing chained after any
DELETE = (('D:/relay', ('push-b714-closing', 'push-b714-preroot', 'push-b714-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b714-entry', 'push-b714-record', 'recut-b712-silence')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R325)(9): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'),)   # ### the re-cut deleted at this step zero, merged at a86c9429

# ### the kernels: none written this act (N1, N5); no tier-one move; SIDE-kernel and SIDE-meta read for (R325)(6)-(7) and not written
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PATHS = ('D:/relay', PP, EF_DIR, LV_DIR, JOIN_DIR, KERNEL_DIR, META_DIR)   # ### (R325)'s PATHS, listed at step zero
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, unmoved
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main, untouched
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### the deposit, untouched
PORT_BRANCH = 'port-b707'
PORT_TIP = 'cb0aea56354abb3abda3fdaef28429c6605605d5'   # ### port-b707's tip, b712's, unmoved this act
PORT_NEW_TIP = PORT_TIP
LV_TAG = 'v0.14.0'          # ### b714's tag ((R324)(3)(i), data/b714_lv_tag.txt), at PORT_TIP, read and not moved this act
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
REPO_VISIBILITY = 'data/repo_visibility.txt'   # ### (R324)(2): the visibility map, the author's listing of 2026-10-26; (R325)(6) reads it
REGISTRATIONS = 'data/b712_registrations.txt'   # ### b713's registrations; the registrations moved to b716 ((R325)), read not written
REG_COMMIT = '67a023887360b74483803ed02c83ae44fdf88f0b'   # ### b712's registrations with the genus control, committed alone
PRICE = 'data/b712_price.txt'
REG_B710 = '41ff1193'        # ### data/b710_registrations.txt committed alone at b710's step zero (the refined law (i))
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b714_read_calls.txt', 'data/b715_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b714 carried them (the ferry's Component 5)
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b715'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md'   # ### (R325)(7): the census read; its rows the readfirst's
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'    # ### (R325)(7): the next edition, on main, the chain's rows
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', CENSUS_NEW)   # ### (R325)(1)-(2) the record lines; (7) the census at v0.8.2
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'   # ### b712's re-cut on RECUT_BRANCH
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'      # ### b713's tip of RECUT_BRANCH, merged into main at b714 (a86c9429); the
#                                                             ### branch deleted at this act's step zero ((R325)(9))
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'
NEXT = ('b716, the registrations act: the carried items of (R325)(8) on the standing toolset -- the heads draft and the question of inline '
        'footings or a companion correspondence; the six lint hits; the 19 names with no pin; the SIDESystem finding at Silence :212 and :183; '
        'the composition law for the least negative index and its -39 registration; the residual; the rectangle certification of pair 7; the '
        'Sonin restriction\'s price and the law\'s identity reading')
NEXT_ACT = 'b716'


def orders_naming(ot_text, act):
    """(R325)(3), the NEXT line's repair: every open-orders row of OPEN_TRAILS whose status names <act> -- a row is a line opening
    `*Appended` that carries `THE ORDER **`W-ORD-`; its status is its text from its last `Status`; returned as (line, order, status). Pure in
    its arguments (b711's port clause was made b714's after the seal and stood outside the sealed NEXT, events :46)."""
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
ACT_CURRENT = 'data/act_current.json'   # ### (R325)(3)(ii): the act's figures, written at step zero and committed alone
STANDING_DIR = 'tools/standing'         # ### (R325)(3): the standing close toolset, versioned by tools/standing/VERSION
ACT_CURRENT_COMMIT = ''                 # ### filled when data/act_current.json is committed alone
STEPZERO = ''                           # ### b714's closing push capture, committed alone at step zero ((R325)(9))
STEPZERO_STEPS = ''                     # ### b714's step row 18, committed alone
STEPZERO_HASHES = ''                    # ### data/b714_bank_hashes.json, committed alone
STEPZERO_REFUSALS = ''                  # ### data/b714_hook_refusals.txt as it stands, committed alone, beside event (10)
STEPZERO_BANKS = ''                     # ### the step-zero banks and tools, committed together by explicit list
COMPUTE_TOOLS = ()                      # ### no compute tool this act
REPAIRED_TOOLS = ()                     # ### shared tools of earlier acts edited by this act (data/b715_tool_repairs.txt)
REPAIRED_DATA = ()
NEW_TOOLS = ()                          # ### the standing toolset's files, listed from tools/standing/ at Component 2
# ### b714's commits the act reads ((R325)(1))
B714_CLOSING = '1992a71c4670ac3118f383f1bbf0ef9e992fa15a'
B714_RECORD = 'ce2c846400284eee07c6451757727f2a5f9bc68f'
B714_ROOT = '242b06d6e9bcca81e1d86d02c089b829354df27b347e5ac7265c94979e66bd0b'
# ### stage two (Component 5): the commits of the components, read from the logs after each was made (filled then)
C1_RELAY = '3468cb19da7216174ae9eae61147ca80739e381c'      # ### the weight line, the corrigendum, the repairs, the lv tag
C1_PP = 'f51b0ae2437bd5c28a7fe3c938e5867f8f074590'         # ### the weight line and the corrigendum entry (FINDINGS :10474, :10476)
C2_RELAY = '3a9ff539f130a4ba4a8f6b6a0c00e3662782d0ae'      # ### Components 2 and 3 in one commit: the merge's banks, the heads draft
C2_PP_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### (R325)(3)(ii): recut-b712-silence merged into main, --no-ff
C3_RELAY = C2_RELAY                                        # ### (7)-(9): the law, the residual, the rectangle
C4_RELAY = '15729469749812e942195e9fcd7fbe78dab5389e'      # ### (10): the Sonin price
PILOT_RELAY = '6641f5066fb8f39f8dfaec4e3616b697928bfc4a'   # ### the pilot, on the author's word (2)
SEALED = ('b715_worklist.py', 'b715_tests.py', 'b715_citation.py', 'b715_record.py', 'b715_checks.py', 'b715_closing.py', 'b715_reg_gate.py',
          'b715_regspec.py', 'b715_corrigendum.py', 'b715_carry.py', 'b715_standing.py', 'b715_hook.py', 'b715_repairs.py') + COMPUTE_TOOLS   # ### the report tool NOT sealed (data/b708_rules.txt row (1))
# ### the act's arms over its own banks (Component 5): b714's ritual arms carried, its arms over b714's objects (v4, the faces head's edit, the
# ### re-cut's additive check, the source pin, the list's controls and completeness, the predictions first, the registrations unchanged, the
# ### onsets, the coefficients) replaced by arms over this act's (v5, the repairs' controls, the membrane and the hook, one lettering, the lv tag,
# ### the re-cut merged, the heads draft held, the law, the residual, the rectangle, the Sonin price, the pilot, no dispatch)
ACT_ARMS = ('G-ANSWERS-BEFORE-WRITES', 'G-ANSWERS-CHECKED', 'G-ARM-SECONDS-BANKED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED',
            'G-CLOSING-DRY-STEP', 'G-CORRIGENDUM-ENTERED', 'G-DEFECTS-LETTERED', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-FIGURES-BANKED', 'G-GUARD-HELD', 'G-LISTINGS-BEFORE-CLAUSES', 'G-PARTS-PRERUN',
            'G-POSTROOT-WRITES-NONE', 'G-R325-ENTERED', 'G-READFIRST-DIFF-BANKED', 'G-REPORT-UNSEALED', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO',
            'G-RULES-ROW-ENTERED', 'G-SCORER-READS-BANKS', 'G-TOOL-REPAIRS', 'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS',
            'G-TRAIL-RESOLVED-EQUAL', 'G-WRITELIST-MIRROR-STATE',
            'G-STANDING-CLAUSES-V5', 'G-REPAIR-CONTROLS', 'G-MEMBRANE-WIRED', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LV-TAG',
            'G-RECUT-MERGED', 'G-HEADS-DRAFT-HELD', 'G-LAW-READ', 'G-RESIDUAL-READ', 'G-RECT-CERTIFIED', 'G-SONIN-PRICED',
            'G-PILOT-BANKED', 'G-NO-DISPATCH')
