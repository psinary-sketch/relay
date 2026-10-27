# -*- coding: utf-8 -*-
"""b718_worklist.py -- THE ACT'S DATA, UNDER (R328). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b718: LANE TWO, ACT ONE HUNDRED AND FORTY-FIVE, THE DERIVATION ACT -- b717 AT ITS WEIGHT; THE CORRIGENDUM; THE STANDING LINE OF
### CONSISTENCY; THE COEFFICIENT LAW READ THROUGH THE CLASS GROUP; THE CONTROLS' RIPE WORK; TWO READS; THE TOOLSET AT v1.2.0; THE FEDERATION
### PIN, LAST AND STOPPABLE. No lean on this host; the runner dispatches those of (R328)(8) alone, twelve at most (N1).
### Carried by diff from b717_worklist.py (data/b718_carry_worklist.txt) and its stage one rewritten by the Edit tool with this act's objects
### (stage one: step zero; stage two, Component 7, by the Edit tool).
### The act runs in a NEW session (02c7cf38; the seat cleared after b717's closing, the ruling pasted at once): the previous act's window is
### b717's session 551b6446 from b717's post-push combine to its end (b671's session-change form).
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'c02f47c1'         # ### PLACE-papers main before the act (b717's trail, pushed by push-b717-record)
PRE_RELAY = '248c5a97'      # ### relay main before the act (b717's closing, pushed by push-b717-closing and read back)
DATE = '2026-10-27'
SESSION_ID = '02c7cf38-4c6a-4f88-b813-a7e15e9b85b4'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R328) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = '551b6446-5996-4c11-94be-d2a2e851a529'   # ### b717 ran and closed in its own session; this act's seat is a new one
PREV_ANCHOR = 'RULING (R327) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b718_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 10784          # ### FINDINGS: b717's entry head (b718's Component 1 appends b717's weight line beneath it)
B711_WEIGHT = 10722         # ### FINDINGS: b716's weight line (b717's Component 1)
B711_CORRIGENDUM = 10724    # ### FINDINGS: b717's corrigendum for b716 (data/b675_corrigenda.txt row (37))
B711_TRAIL = 16086          # ### OPEN_TRAILS: b717's trail record
B711_FACE = 'data/b717_registration_2026-10-27.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-27-b717.zip'   # ### b717's export, CLEAN on all three clauses, 74 entries
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707), restated in b717's trail :15914
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711), discharged by (R328)(3)(i)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it ((R328)(4))
TRAIL_ORDERS = 16030        # ### OPEN_TRAILS: b715's open orders line (b717's trail carries none of its own)
TRAIL_RESOLVED = 16076      # ### OPEN_TRAILS: b717's ten items for the author's strike
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence b717 restated
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row ((R328)(10))

# ### the branches step zero deletes ((R328)(8)): the push-b717-* branches of relay and PLACE-papers by name, each read from the listings and
# ### `--merged` printed before the deletes, one per command, each its own message, in sequence, nothing chained after any (the relay carries
# ### push-b717-closing, push-b717-preroot and push-b717-record; PLACE-papers push-b717-preroot and push-b717-record)
DELETE = (('D:/relay', ('push-b717-closing', 'push-b717-preroot', 'push-b717-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b717-preroot', 'push-b717-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R328)(8): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'),)

# ### the kernels: none written this act (N1, N5); no tier-one move; the kernels read for (R328)(6) at their current tags and not written
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
# ### (R328)(8): the twelve kernels below the target de5ce8a9 (data/b716_federation_pin_price.txt (3), :56-:138), each at D:/<name>
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PATHS = ('D:/relay', PP, EF_DIR, LV_DIR, JOIN_DIR) + tuple('D:/' + k for k in PIN_KERNELS)   # ### (R328)'s PATHS, listed at step zero
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
MAX_DISPATCHES = 12         # ### N1: the federation pin's dispatches alone, twelve at most ((R328)(8))

PAPERS = dict()
DATA_STANDING_V1 = 'data/standing_clauses_v1.txt'
DATA_STANDING_V2 = 'data/standing_clauses_v2.txt'
DATA_STANDING_V3 = 'data/standing_clauses_v3.txt'
DATA_STANDING_V4 = 'data/standing_clauses_v4.txt'
DATA_STANDING_V5 = 'data/standing_clauses_v5.txt'
DATA_STANDING_V6 = 'data/standing_clauses_v6.txt'
DATA_STANDING = 'data/standing_clauses_v7.txt'   # ### (R328)(3): v6 with the standing line of consistency appended, committed alone at step zero
ARM_TAGS = 'data/arm_tags.json'                  # ### (R327)(2): every arm tagged CLAIM or CLOSE by what it guards
REPO_VISIBILITY = 'data/repo_visibility.txt'   # ### (R324)(2): the visibility map, the author's listing of 2026-10-26
REGISTRATIONS = 'data/b716_registrations.txt'   # ### (R328)(4)(i): b716's registrations, (ii) read unchanged from dc5e808f (N2)
REG_COMMIT = 'dc5e808f9a2a95ffbe5b4d69b58e7fb216458c16'   # ### b716's first commit: the registrations with their count control
REG_FILES = ('data/b716_registrations.txt', 'data/b716_genus_control.txt', 'data/b716_genus_control.json', 'tools/b716_genus_control.py')
PRED_B717 = 'data/b717_predictions.txt'   # ### (R328)(5)(i): b717's predictions, committed alone at f47d8ab5, read not written
PRED_B717_COMMIT = 'f47d8ab5840d287bf63c1f0b59ba707ed85dbe07'
PREDICTIONS = PRED_B717
REGISTRATIONS_NEW = 'data/b718_registrations.txt'   # ### (R328)(4)(iv): committed alone before anything at either new discriminant (N2)
PRICES_6 = ('data/b716_federation_pin_price.txt', 'data/b716_epstein_count_price.txt')   # ### b716's two prices; (R328)(8) runs the first
COEFF_BANKS = ('data/b711_coeffs.txt', 'data/b713_coeffs.txt', 'data/b717_coeffs.txt')   # ### (R328)(4)(iii): the checks' banks, read not written
COMPUTE_BANKS = ('data/b718_decomp.txt', 'data/b718_decomp.json', 'data/b718_derivation.txt', 'data/b718_derivation.json',
                 'data/b718_registrations.txt', 'data/b718_a0.txt', 'data/b718_a0.json', 'data/b718_count_read.txt')
REG_B712 = '67a023887360b74483803ed02c83ae44fdf88f0b'   # ### b712's registrations with the genus control (b713's), read not written
REG_B710 = '41ff1193'        # ### data/b710_registrations.txt committed alone at b710's step zero (the refined law (i))
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b717_read_calls.txt', 'data/b718_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b717 carried them (the ferry's Component 5)
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b718'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'   # ### the census on main read by its rows (the readfirst's)
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### (R328)(6): the next edition, on main, the eleven names' rows
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'    # ### (R328)(5)(i): the companion table beside the paper
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md')   # ### (R328)(1)-(2) the record lines, (9) the watch's annotation, the entry and the trail;
#   ### no paper, no ERRATA, no REGISTRY row written this act (the REGISTRY cells priced for b719, (R328)(9))
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'   # ### b712's re-cut on RECUT_BRANCH
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'      # ### b713's tip of RECUT_BRANCH, merged into main at b714 (a86c9429); the
#                                                             ### branch deleted at b717's step zero ((R327)(9))
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'
NEXT = ('b719 ((R328)(13)): the two discriminants computed under (4)(iv)`s commit (data/b718_registrations.txt); the surgery under its '
        'registration; the REGISTRY cells written; the box of (5)(iii) where it was carried')
NEXT_ACT = 'b719'


def orders_naming(ot_text, act):
    """(R328)(3), the NEXT line's repair: every open-orders row of OPEN_TRAILS whose status names <act> -- a row is a line opening
    `*Appended` that carries `THE ORDER **`W-ORD-`; its status is its text from its last `Status`; returned as (line, order, status). Pure in
    its arguments (b711's port clause was made b717's after the seal and stood outside the sealed NEXT, events :46)."""
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
ACT_CURRENT = 'data/act_current.json'   # ### (R324)(6)(ii): the act's figures, written at step zero and committed alone
STANDING_DIR = 'tools/standing'         # ### (R328)(7): the standing close toolset, versioned by tools/standing/VERSION
STANDING_COMMIT = '71523e0d9c5091cd3a041fc4b455de202aae3a42'      # ### data/standing_clauses_v7.txt committed alone ((R328)(3))
ACT_CURRENT_COMMIT = '30965720bbeb35e2fea7b79745d656e255326822'   # ### data/act_current.json committed alone
STEPZERO = '1e6368bdf26ef7004cbdae0c167564b053a5fc34'             # ### b717's closing push capture, committed alone at step zero ((R328)(10))
STEPZERO_STEPS = '49778e8184aba9f6ccece7ce578886994fa0aec5'       # ### b717's step row 19, committed alone
STEPZERO_HASHES = '7ebab305d9986f5bb910a17f596981a873235942'      # ### data/b717_bank_hashes.json, committed alone
STEPZERO_PREVBUILD = 'b4eb540711aae490078404ad27e072cb0695b57c'   # ### tools/mirror_prevbuild.json as b717's build left it, committed alone
STEPZERO_REFUSALS = '5ef2ae3a064e51fb706d21c574e2c073bc2a336d'    # ### data/b717_hook_refusals.txt as it stands (the refusal after the closing), committed alone
STEPZERO_BANKS = 'f79a10e22d599ad5667ad85818197d5111ef7363'       # ### the step-zero banks and tools, committed together by explicit list
VISIBILITY_COMMIT = ACT_CURRENT_COMMIT   # ### no visibility map written this act: the arms reading this name read the act's figures' commit
COMPUTE_TOOLS = ()              # ### the compute tools of (R328)(4)-(5) are tools/b718_*.py and enter SEALED by its rule
REPAIRED_TOOLS = ()             # ### no shared tool outside tools/standing/ repaired this act
REPAIRED_DATA = ()
STANDING_FILES = ('VERSION', 'act.py', 'allow.py', 'arms.py', 'classes.py', 'close.py', 'components.py', 'controls.py', 'hook.py', 'keystone.py',
                  'manifest.py', 'needles.py', 'repairs.py', 'replay.py', 'rootbanks.py', 'roster.py', 'scan.py', 'words.py')
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset at v1.2.0 ((R328)(7), Component 4), sealed by hash beside the act's tools
STANDING_VERSION = 'v1.2.0'
STANDING_CHANGED = ('allow.py', 'close.py', 'replay.py', 'VERSION')                       # ### edited at v1.2.0 (data/b718_tool_repairs.txt)
STANDING_NEW = ('classes.py', 'keystone.py', 'manifest.py', 'needles.py')                 # ### new at v1.2.0
# ### b717's commits the act reads ((R328)(1))
B714_CLOSING = '983dcbe27b5771acaedd84be04091b902218711c'   # ### b717's closing, the act's relay base (the names kept for the carried arms: the previous act's)
B714_RECORD = '78866b19ed7870f55dae7e92b37db947a003dbd9'
B714_ROOT = '4df4ddac46aa791068bb527b888497ebd435381360149d7866f5d0f386aeb327'   # ### data/act_roots.txt :94
# ### stage two (Component 7, before the lock): the commits of the components, read from the logs after each was made
C1_RELAY = '6c994f8a80bb47024edf2cbfc81b7c433c2ce9ca'   # ### (R328)(1)-(2): b717's weight line and the corrigendum's banks, the corrigenda row (38)
C1_PP = '183ab09faeb12b0004f68c8aa763a0effc3a818d'      # ### the weight line (FINDINGS :10820) and the corrigendum entry (:10822)
WEIGHT_LINE, CORR_LINE = 10820, 10822
C2_REG = '8146404b577dfee3e379d19e08e8595ab8824961'     # ### (R328)(4)(iv), N2: data/b718_registrations.txt committed alone, before anything at -20 or -47
C2_RELAY = '296034384d40e64b0e346b9b8dc62ae0646e7421'   # ### (R328)(4)(ii)-(iii): the decomposition reproduced and the derivation
C3_RELAY = '0286a8ef9d930f0067df27017b7444f4fdecafce'   # ### (R328)(5): A0, the count read, the box read, the surgery priced
C4_RELAY = 'a240e6b6320a4eb8e28011bf8bebd19cea3b70c9'   # ### (R328)(6)-(7): the two reads; the toolset at v1.2.0 with the replay
C5_RELAY = ('9eeb8971f120e8f274781abf3eaa36cd490a9f79', 'a9daf4f33ca0a8d88f0480551f2830e22fc5196a')   # ### (R328)(8): the pin, stopped by the author's word (Option 2), and its one read
C6_RELAY = '309dfd05a84ccb13992907650855eb96e7aba9c9'   # ### (R328)(9): the records' banks
C6_PP = 'f6f6df50101a539d59997bb06cb200d9aba4d51f'      # ### (R328)(9): W-ORD-QUASI-RH-FIELD-WATCH annotated at OPEN_TRAILS :16126
C6_PP_REPAIR = '54a01285e8cc8243f62d674eae9462cce3b9c716'                               # ### defect (t): :16126 reworded, the outside names moved to relay data/b718_watch.txt
WATCH_LINE = 16126
NEW_DISCRIMINANTS = ((-20, 2), (-47, 5))                  # ### (R328)(4)(iv): registered, nothing computed beyond the class number and forms
PIN_RUNS = ((('SIDE-effects', 40587516142),))             # ### (R328)(8): the one dispatch, read once by its id
PIN_BRANCH = 'pin-b718-de5ce8a9'
PIN_HELD = ('SIDE-cosmo', 'SIDE-frobenius')
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md')   # ### the record lines (C1) and the watch's annotation (C6); no paper edited this act
ERRATA_ID = None
ERRATA_IDS = ()
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b718_') and f.endswith('.py') and f != 'b718_report.py')) + NEW_TOOLS + COMPUTE_TOOLS
# ### the act's arms over its own banks: b717's ritual arms carried; its arms over b717's objects (the import closure, the roster from main, the
# ### pins census, the census rows) replaced by arms over this act's (the registrations first, the keystone edits, the prices, nothing built)
ACT_ARMS = ('G-ANSWERS-BEFORE-WRITES', 'G-ANSWERS-CHECKED', 'G-ARM-SECONDS-BANKED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED',
            'G-CLOSING-DRY-STEP', 'G-CORRIGENDUM-ENTERED', 'G-DEFECTS-LETTERED', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-FIGURES-BANKED', 'G-GUARD-HELD', 'G-LISTINGS-BEFORE-CLAUSES', 'G-PARTS-PRERUN',
            'G-POSTROOT-WRITES-NONE', 'G-R328-ENTERED', 'G-READFIRST-DIFF-BANKED', 'G-REPORT-UNSEALED', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO',
            'G-RULES-ROW-ENTERED', 'G-SCORER-READS-BANKS', 'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS',
            'G-TRAIL-RESOLVED-EQUAL', 'G-WRITELIST-MIRROR-STATE',
            'G-MEMBRANE-WIRED', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-ACT-CURRENT', 'G-PIN-READ',
            'G-REGISTRATIONS-FIRST', 'G-DECOMP-REPRODUCED', 'G-DERIVATION-GRADED', 'G-A0-CERTIFIED', 'G-COUNT-READ',
            'G-READS-BANKED', 'G-TOOLSET-V120', 'G-RECORDS-PRICED', 'G-TOUCH-READ', 'G-ARM-TAGS')
# ### Component 7 (the Edit tool): b717's arms over b717's objects (the -39 list, the predictions, the onsets, the coefficients, the words, the
# ### names, the order, no dispatch) not carried -- their banks are b717's and this act writes none; this act's arms over its own banks added:
# ### the registrations first, the decomposition reproduced, the derivation graded, A0 certified, the count read, the two reads, the toolset
# ### at v1.2.0, the pin read by its run ids, the records priced, the touch read of (R328)(3)
