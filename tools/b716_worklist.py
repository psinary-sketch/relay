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
REPO_VISIBILITY = 'data/repo_visibility.txt'   # ### (R325)(2): the visibility map, the author's listing of 2026-10-26; (R326)(6) reads it
REGISTRATIONS = 'data/b716_registrations.txt'   # ### (R326)(4): the -39 registrations, committed alone at step zero, ahead of every other bank (N2)
REG_COMMIT = 'dc5e808f9a2a95ffbe5b4d69b58e7fb216458c16'   # ### the registrations with their count control (data/b716_genus_control.*, its tool), the act's first commit
REG_FILES = ('data/b716_registrations.txt', 'data/b716_genus_control.txt', 'data/b716_genus_control.json', 'tools/b716_genus_control.py')
PRICE = 'data/b716_price.txt'
PRICES_6 = ('data/b716_federation_pin_price.txt', 'data/b716_epstein_count_price.txt')   # ### (R326)(6): two prices, nothing built
REG_B712 = '67a023887360b74483803ed02c83ae44fdf88f0b'   # ### b712's registrations with the genus control (b713's), read not written
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
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', 'day1/Silence_of_Foundations.md', 'ERRATA.md', 'day1/ONE_PAGE_PROOF.md',
              'day1/Seven_Mechanism_Classes.md', 'day1/Spectral_Inertness.md')   # ### (R326)(1)-(2) the record lines; (5)(iii)-(iv) the keystone edits on main
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'   # ### b712's re-cut on RECUT_BRANCH
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'      # ### b713's tip of RECUT_BRANCH, merged into main at b714 (a86c9429); the
#                                                             ### branch deleted at b715's step zero ((R325)(9))
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'
NEXT = ('b717 ((R326)(10)): the computation at -39 under (4)`s commit (dc5e808f) where its price fits one act (data/b716_price.txt); the '
        'author`s words on (5)(i)-(ii) applied (the heads draft II and III, the six lint hits); and the federation pin where (6)(i) prices it '
        'within one act (data/b716_federation_pin_price.txt)')
NEXT_ACT = 'b717'


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
ACT_CURRENT_COMMIT = '060acae95b64180ba130e6cc57718676b9619e64'   # ### data/act_current.json committed alone
STEPZERO = '94a9aa6d8f7d4e3eda2eb9fa3ea71ccb79228d3b'           # ### b715's closing push capture, committed alone at step zero ((R326)(7))
STEPZERO_STEPS = '5a5cd6c0aa6c1c545a5a64d1f579052b8bcee93e'     # ### b715's step row 21, committed alone
STEPZERO_HASHES = '8ee0101664d13f3807c23866ddf7e7fad5818b37'    # ### data/b715_bank_hashes.json, committed alone
STEPZERO_REFUSALS = 'd6964db89ffc6efd296165caf558c073e1221c8a'  # ### data/b715_hook_refusals.txt as it stands, committed alone
STEPZERO_REFUSALS_B714 = '211bdb3a63a34f54fd25ebb4b12c2c86f278c034'   # ### data/b714_hook_refusals.txt as it stands, committed alone
STEPZERO_PREVBUILD = '0fbfbf9e1e257a2c6076d5f4e76715b40e47ff10'  # ### tools/mirror_prevbuild.json as b715's build left it, committed alone
STEPZERO_BANKS = 'ee0dbf176b4a66f24f754e84e39b2785c0fad834'     # ### the step-zero banks and tools, committed together by explicit list
STANDING_COMMIT = ACT_CURRENT_COMMIT    # ### no standing clauses written this act (v5 b715's): the arms reading this name read the act's figures' commit
VISIBILITY_COMMIT = ACT_CURRENT_COMMIT  # ### no visibility map written this act (b715's)
COMPUTE_TOOLS = ()                      # ### no compute tool this act: nothing of -39 computed beyond its count control (N2)
REPAIRED_TOOLS = ('mirror_verify.py',)  # ### the shared verifier, repaired by (R326)(3)(iii) (clause 3 through tools/standing/roster.py roster_at)
REPAIRED_DATA = ()
STANDING_FILES = ('VERSION', 'act.py', 'allow.py', 'arms.py', 'close.py', 'components.py', 'controls.py', 'hook.py', 'repairs.py', 'replay.py',
                  'rootbanks.py', 'roster.py', 'scan.py', 'words.py')
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### (R326)(3): the standing close toolset at v1.1.0, sealed by hash beside the act's tools
# ### b715's commits the act reads ((R326)(1))
B714_CLOSING = 'cf51ee95d8d7d96ccd1e64a3e17b32b9103b2eb6'   # ### b715's closing, the act's relay base (the names kept for the carried arms: the previous act's)
B714_RECORD = 'fdddea138375be1dc1bbcc0e6f8150ac17d643f6'
B714_ROOT = 'c0e86c02b7c5a8a4a7d1be2f741ae2bc8f04fdede278e26ae1ddb588c10f5729'   # ### data/act_roots.txt :93
# ### stage two (Component 5, before the lock): the commits of the components, read from the logs after each was made
C1_RELAY = 'fb4e662ec6f5c68eadc7ee8a00f5400fe580009e'      # ### b715's weight line and the corrigendum's banks, the corrigenda row (36)
C1_PP = '4320b719e3a061e32260bb386242471b87b787b9'         # ### the weight line and the corrigendum entry (FINDINGS :10616, :10618)
C2_RELAY = '8e69db7139d55861873312481245a681c7330214'      # ### (R326)(3): the standing toolset at v1.1.0, its controls, the replay, the coverage table
C3_PP = '29c175277eb985b0c4b47bb070b1351f5f08bafe'         # ### (R326)(5)(iii)-(iv): Silence :212, ERRATA E-2026-10-27-1, 8 pins in 4 files
C3_RELAY = 'e4fd02f3151caa72d041f840ad81061d0fe295a2'      # ### (R326)(5)(iii)-(v): the keystone banks
C4_RELAY = '170a08021fd7c4199d99f877b8eb345006935e4d'      # ### (R326)(4)(iv), (6): the three prices, nothing built
PP_EDITED = ('day1/Silence_of_Foundations.md', 'ERRATA.md', 'day1/ONE_PAGE_PROOF.md', 'day1/Seven_Mechanism_Classes.md', 'day1/Spectral_Inertness.md')
ERRATA_ID = 'E-2026-10-27-1'
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b716_') and f.endswith('.py') and f != 'b716_report.py')) + NEW_TOOLS + COMPUTE_TOOLS
# ### the act's arms over its own banks: b715's ritual arms carried; its arms over b715's objects (the import closure, the roster from main, the
# ### pins census, the census rows) replaced by arms over this act's (the registrations first, the keystone edits, the prices, nothing built)
ACT_ARMS = ('G-ANSWERS-BEFORE-WRITES', 'G-ANSWERS-CHECKED', 'G-ARM-SECONDS-BANKED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED',
            'G-CLOSING-DRY-STEP', 'G-CORRIGENDUM-ENTERED', 'G-DEFECTS-LETTERED', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-FIGURES-BANKED', 'G-GUARD-HELD', 'G-LISTINGS-BEFORE-CLAUSES', 'G-PARTS-PRERUN',
            'G-POSTROOT-WRITES-NONE', 'G-R326-ENTERED', 'G-READFIRST-DIFF-BANKED', 'G-REPORT-UNSEALED', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO',
            'G-RULES-ROW-ENTERED', 'G-SCORER-READS-BANKS', 'G-TOOL-REPAIRS', 'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS',
            'G-TRAIL-RESOLVED-EQUAL', 'G-WRITELIST-MIRROR-STATE',
            'G-REPAIR-CONTROLS', 'G-MEMBRANE-WIRED', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-ACT-CURRENT', 'G-TOOLSET-SCAN',
            'G-TOOLSET-REPLAY', 'G-COVERAGE-TABLE', 'G-NO-DISPATCH',
            'G-REGISTRATIONS-FIRST', 'G-KEYSTONE-EDITS', 'G-PRICES-BANKED')
