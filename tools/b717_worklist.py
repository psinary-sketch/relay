# -*- coding: utf-8 -*-
"""b717_worklist.py -- THE ACT'S DATA, UNDER (R327). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b717: LANE TWO, ACT ONE HUNDRED AND FORTY-FOUR, THE TEST ACT -- b716 AT ITS WEIGHT; CLAIM AND CLOSE; THE CORRIGENDUM; THE TEST
### AT -39; THE AUTHOR'S WORDS APPLIED; THE ELEVEN NAMES; TWO ITEMS SCHEDULED. No lean on this host and no runner dispatch (N1).
### Carried by diff from b716_worklist.py (data/b717_carry_worklist.txt) and its stage one rewritten by the Edit tool with this act's objects
### (stage one: step zero; stage two, Component 5, by the Edit tool).
### The act runs in a NEW session (551b6446; the seat cleared after b716's closing, the ruling pasted at once): the previous act's window is
### b716's session 0c15655e from b716's post-push combine to its end (b671's session-change form).
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'b855623d'         # ### PLACE-papers main before the act (b716's trail, pushed by push-b716-record)
PRE_RELAY = '983dcbe2'      # ### relay main before the act (b716's closing, pushed by push-b716-closing and read back)
DATE = '2026-10-27'
SESSION_ID = '551b6446-5996-4c11-94be-d2a2e851a529'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R327) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = '0c15655e-4d46-485e-9b80-fada479be2d0'   # ### b716 ran and closed in its own session; this act's seat is a new one
PREV_ANCHOR = 'RULING (R326) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b717_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 10686          # ### FINDINGS: b716's entry head (b717's Component 1 appends b716's weight line beneath it)
B711_WEIGHT = 10616         # ### FINDINGS: b715's weight line (b716's Component 1)
B711_CORRIGENDUM = 10618    # ### FINDINGS: b716's corrigendum for b715 (data/b675_corrigenda.txt row (36))
B711_TRAIL = 16044          # ### OPEN_TRAILS: b716's trail record
B711_FACE = 'data/b716_registration_2026-10-27.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-27-b716.zip'   # ### b716's export, CLEAN on all three clauses, 74 entries
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707), restated in b716's trail :15914
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711), discharged by (R327)(3)(i)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it ((R327)(4))
TRAIL_ORDERS = 16030        # ### OPEN_TRAILS: b715's open orders line (b716's trail carries none of its own)
TRAIL_RESOLVED = 16076      # ### OPEN_TRAILS: b716's ten items for the author's strike
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence b716 restated
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row ((R327)(10))

# ### the branches step zero deletes ((R327)(8)): the push-b716-* branches of relay and PLACE-papers by name, each read from the listings and
# ### `--merged` printed before the deletes, one per command, each its own message, in sequence, nothing chained after any (the relay carries
# ### push-b716-closing, push-b716-preroot and push-b716-record; PLACE-papers push-b716-preroot and push-b716-record)
DELETE = (('D:/relay', ('push-b716-closing', 'push-b716-preroot', 'push-b716-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b716-preroot', 'push-b716-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R327)(8): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'),)

# ### the kernels: none written this act (N1, N5); no tier-one move; the kernels read for (R327)(6) at their current tags and not written
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PATHS = ('D:/relay', PP, EF_DIR, LV_DIR, KERNEL_DIR, META_DIR)   # ### (R327)'s PATHS (six; SIDE-faces-join not among them), listed at step zero
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
DATA_STANDING_V5 = 'data/standing_clauses_v5.txt'
DATA_STANDING = 'data/standing_clauses_v6.txt'   # ### (R327)(2): v5 with the CLAIM AND CLOSE row appended, committed alone at step zero
ARM_TAGS = 'data/arm_tags.json'                  # ### (R327)(2): every arm tagged CLAIM or CLOSE by what it guards
REPO_VISIBILITY = 'data/repo_visibility.txt'   # ### (R324)(2): the visibility map, the author's listing of 2026-10-26
REGISTRATIONS = 'data/b716_registrations.txt'   # ### (R327)(4): b716's -39 registrations, read unchanged from dc5e808f (N2); nothing added
REG_COMMIT = 'dc5e808f9a2a95ffbe5b4d69b58e7fb216458c16'   # ### b716's first commit: the registrations with their count control
REG_FILES = ('data/b716_registrations.txt', 'data/b716_genus_control.txt', 'data/b716_genus_control.json', 'tools/b716_genus_control.py')
PRICE = 'data/b716_price.txt'    # ### (R327)(4): the price the computation runs under, read not written
PRICES_6 = ('data/b716_federation_pin_price.txt', 'data/b716_epstein_count_price.txt')   # ### (R327)(7): b716's two prices, scheduled, nothing built
PREDICTIONS = 'data/b717_predictions.txt'   # ### (R327)(4)(ii): committed alone before any onset at -39 (N2)
COMPUTE_BANKS = ('data/b717_list.txt', 'data/b717_list.json', 'data/b717_predictions.txt', 'data/b717_predictions.json',
                 'data/b717_onsets.txt', 'data/b717_onsets.json', 'data/b717_coeffs.txt', 'data/b717_coeffs.json')
REG_B712 = '67a023887360b74483803ed02c83ae44fdf88f0b'   # ### b712's registrations with the genus control (b713's), read not written
REG_B710 = '41ff1193'        # ### data/b710_registrations.txt committed alone at b710's step zero (the refined law (i))
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b716_read_calls.txt', 'data/b717_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b716 carried them (the ferry's Component 5)
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b717'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'   # ### the census on main read by its rows (the readfirst's)
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### (R327)(6): the next edition, on main, the eleven names' rows
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'    # ### (R327)(5)(i): the companion table beside the paper
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', 'ERRATA.md', 'day1/Silence_of_Foundations.md', COMPANION, CENSUS_NEW)   # ### (R327)(1)-(3) the record
#   ### lines; (5) the head, the companion and the six hits' papers, (6) the census and the day papers' rows: the papers of (5)(ii) and (6) added
#   ### at the components that name them (stage two)
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'   # ### b712's re-cut on RECUT_BRANCH
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'      # ### b713's tip of RECUT_BRANCH, merged into main at b714 (a86c9429); the
#                                                             ### branch deleted at b716's step zero ((R326)(9))
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'
NEXT = ('b718 ((R327)(11)): the federation pin under (7)(i), one branch per kernel carrying the bump to de5ce8a9, each build read by its run '
        'id (data/b716_federation_pin_price.txt); the composition law re-read against -39`s result; the CLOSE classes of b716 and b717 gathered '
        'into tools/standing/ v1.2.0')
NEXT_ACT = 'b718'


def orders_naming(ot_text, act):
    """(R327)(3), the NEXT line's repair: every open-orders row of OPEN_TRAILS whose status names <act> -- a row is a line opening
    `*Appended` that carries `THE ORDER **`W-ORD-`; its status is its text from its last `Status`; returned as (line, order, status). Pure in
    its arguments (b711's port clause was made b716's after the seal and stood outside the sealed NEXT, events :46)."""
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
ACT_CURRENT = 'data/act_current.json'   # ### (R327)(3)(ii): the act's figures, written at step zero and committed alone
STANDING_DIR = 'tools/standing'         # ### (R327)(3): the standing close toolset, versioned by tools/standing/VERSION
STANDING_COMMIT = '66232bcab0cb409c67e7e092dcadcd943b8298db'      # ### data/standing_clauses_v6.txt committed alone ((R327)(2))
ACT_CURRENT_COMMIT = '3739e9c7bdba43fc9dae279b5729b1346c359cff'   # ### data/act_current.json committed alone
STEPZERO = '5527b92e25abeb2b30d611d1e57fd894b0abcd53'             # ### b716's closing push capture, committed alone at step zero ((R327)(8))
STEPZERO_STEPS = '42ce2bbc56abe9680cc43b151f66e946d4b1a50e'       # ### b716's step row 18, committed alone
STEPZERO_HASHES = '43a3a62cd9e42746c13181943f93e97515008fbf'      # ### data/b716_bank_hashes.json, committed alone (defect (k))
STEPZERO_REFUSALS = '696e12cb0011f8a8b26a917acd09b5059605ffe5'    # ### data/b716_hook_refusals.txt as it stands, committed alone (defect (k))
STEPZERO_PREVBUILD = ''         # ### tools/mirror_prevbuild.json unchanged by b716's build after its commit: nothing to commit
STEPZERO_BANKS = 'c86f2b73b1b61c8a330a3817ceac52527d9f9486'   # ### the step-zero banks and tools, committed together by explicit list
VISIBILITY_COMMIT = ACT_CURRENT_COMMIT   # ### no visibility map written this act: the arms reading this name read the act's figures' commit
COMPUTE_TOOLS = ()              # ### the four compute tools of (R327)(4) are tools/b717_*.py and enter SEALED by its rule
REPAIRED_TOOLS = ()             # ### no shared tool repaired this act (CLOSE items are recorded, not repaired, (R327)(2))
REPAIRED_DATA = ()
STANDING_FILES = ('VERSION', 'act.py', 'allow.py', 'arms.py', 'close.py', 'components.py', 'controls.py', 'hook.py', 'repairs.py', 'replay.py',
                  'rootbanks.py', 'roster.py', 'scan.py', 'words.py')
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset at v1.1.0, unchanged this act, sealed by hash beside the act's tools
# ### b716's commits the act reads ((R327)(1))
B714_CLOSING = '983dcbe27b5771acaedd84be04091b902218711c'   # ### b716's closing, the act's relay base (the names kept for the carried arms: the previous act's)
B714_RECORD = '78866b19ed7870f55dae7e92b37db947a003dbd9'
B714_ROOT = '4df4ddac46aa791068bb527b888497ebd435381360149d7866f5d0f386aeb327'   # ### data/act_roots.txt :94
# ### stage two (Component 5, before the lock): the commits of the components, read from the logs after each was made
C1_RELAY = '7c654dbe861caa912b0c30524cc095bf97990170'   # ### b716's weight line and the corrigendum's banks, the corrigenda row (37)
C1_PP = 'e0ab685b583eed3b1f9a35fbf673a603edf894ef'      # ### the weight line (:10722) and the corrigendum entry (:10724)
C2_RELAY = ''      # ### (R327)(4)(i): the list at -39
C3_PRED = ''       # ### (R327)(4)(ii): data/b717_predictions.txt committed alone, before any onset (N2)
C3_RELAY = ''      # ### (R327)(4)(iii): the onsets
C4_RELAY = ''      # ### (R327)(4)(iv): the coefficients and the law
C5_PP = ''         # ### (R327)(5)-(6): the head, the companion, the six hits, the census v0.8.3, the Correspondence rows, ERRATA
C5_RELAY = ''      # ### (R327)(5)-(6): their banks and diffs
PP_EDITED = ()     # ### filled at Component 5 from its diffs bank
ERRATA_ID = ''     # ### filled at Component 5
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b717_') and f.endswith('.py') and f != 'b717_report.py')) + NEW_TOOLS + COMPUTE_TOOLS
# ### the act's arms over its own banks: b716's ritual arms carried; its arms over b716's objects (the import closure, the roster from main, the
# ### pins census, the census rows) replaced by arms over this act's (the registrations first, the keystone edits, the prices, nothing built)
ACT_ARMS = ('G-ANSWERS-BEFORE-WRITES', 'G-ANSWERS-CHECKED', 'G-ARM-SECONDS-BANKED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED',
            'G-CLOSING-DRY-STEP', 'G-CORRIGENDUM-ENTERED', 'G-DEFECTS-LETTERED', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-FIGURES-BANKED', 'G-GUARD-HELD', 'G-LISTINGS-BEFORE-CLAUSES', 'G-PARTS-PRERUN',
            'G-POSTROOT-WRITES-NONE', 'G-R327-ENTERED', 'G-READFIRST-DIFF-BANKED', 'G-REPORT-UNSEALED', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO',
            'G-RULES-ROW-ENTERED', 'G-SCORER-READS-BANKS', 'G-TOOL-REPAIRS', 'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS',
            'G-TRAIL-RESOLVED-EQUAL', 'G-WRITELIST-MIRROR-STATE',
            'G-REPAIR-CONTROLS', 'G-MEMBRANE-WIRED', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-ACT-CURRENT', 'G-TOOLSET-SCAN',
            'G-TOOLSET-REPLAY', 'G-COVERAGE-TABLE', 'G-NO-DISPATCH',
            'G-REGISTRATIONS-FIRST', 'G-KEYSTONE-EDITS', 'G-PRICES-BANKED')
