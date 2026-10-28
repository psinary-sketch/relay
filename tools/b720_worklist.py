# -*- coding: utf-8 -*-
"""b720_worklist.py -- THE ACT'S DATA, UNDER (R330). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b720: LANE TWO, ACT ONE HUNDRED AND FORTY-SEVEN, THE DECOMPOSITION ACT -- b719 AT ITS WEIGHT; THE CORRIGENDUM; -35 AND -40
### REGISTERED BEFORE ANY FIGURE, THEN COMPUTED; THE DERIVATION'S -2 WITH BOTH CONFIGURATIONS; THE REGISTRY CELLS FOR WAVE 1; THE CHALLENGE
### FILE; THE PIN'S REMAINDER, LAST AND STOPPABLE. No lean on this host (N1); the runner dispatches are (R330)(5)(ii)-(iii)'s alone.
### Carried by diff from b719_worklist.py (data/b720_carry_worklist.txt) and its stage one rewritten whole by the Write tool with this act's
### objects at step zero (the carried text named b719's objects under b720's names); stage two, Component 7, by the Edit tool.
### The act runs in the SAME session as b719 (02c7cf38; the ruling pasted after b719's closing, no clear): the previous act's window is this
### session cut at b719's anchor, b706's same-session form. b719 closed and pushed itself whole (relay ef648cb9, PLACE-papers b92bb70a, both
### read back); its closing capture and step-33 row are this act's carried files ((R330)(7)).
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'b92bb70a916c4c3ed6a00fdb3f28b9d2eb9e20b4'    # ### PLACE-papers main before the act's own commits: b719's trail, pushed and read back by b719
PRE_RELAY = 'ef648cb95098481e582042cb4a0dbb8cf9efdeb1'  # ### relay main before the act's own commits: b719's closing, pushed and read back by b719
PRE_PP_REMOTE_AT_START = 'b92bb70a'      # ### PLACE-papers remote main at the act's start (read at step zero, equal to local)
PRE_RELAY_REMOTE_AT_START = 'ef648cb9'   # ### relay remote main at the act's start (read at step zero, equal to local)
B718_RELAY_HEAD = 'ef648cb'  # ### the names kept for the carried readers: the previous act's last relay head (b719's closing)
B718_PP_HEAD = 'b92bb70'     # ### the previous act's last PLACE-papers head (b719's trail)
DATE = '2026-10-28'
SESSION_ID = '02c7cf38-4c6a-4f88-b813-a7e15e9b85b4'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R330) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = SESSION_ID   # ### b719 ran in this session (from 'RULING (R329) BEGIN', with a compaction); b706's same-session form
PREV_ANCHOR = 'RULING (R329) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b720_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 10982          # ### FINDINGS: b719's entry head (PLACE-papers 2b7a6f2b)
B711_WEIGHT = 10896         # ### FINDINGS: b718's weight line (b719's Component 1)
B711_CORRIGENDUM = 10898    # ### FINDINGS: b719's corrigendum for b718
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name)
B711_TRAIL = 16172          # ### OPEN_TRAILS: b719's trail record (PLACE-papers b92bb70a)
B711_FACE = 'data/b719_registration_2026-10-28.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-28-b719.zip'   # ### b719's export, built after b719's last push, 74 files, CLEAN
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
TRAIL_ORDERS = 16030        # ### OPEN_TRAILS: b715's open orders line
TRAIL_RESOLVED = 16210      # ### OPEN_TRAILS: b719's items for the author's strike, in its trail (landed at b92bb70a)
WATCH_LINE = 16126          # ### OPEN_TRAILS: W-ORD-QUASI-RH-FIELD-WATCH, annotated at b718's C6
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row

# ### the branches step zero deletes ((R330)(7)): the push-b719-* branches b719's close made, by name, each read from the listings and
# ### `--merged` printed before the deletes (state720 at step zero), one per command, each its own message
DELETE = (('D:/relay', ('push-b719-closing', 'push-b719-record', 'push-b719-root')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b719-record', 'push-b719-root')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R330)(7): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'),)

# ### the kernels: SIDE-explicit-formula gains the challenge branch ((R330)(5)(ii)); the pin's bump branches pushed ((5)(iii)); no main, no tag
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')


def _kernel_paths():
    """the kernels of data/b716_federation_pin_price.txt (1), as D:/<name>, read at import ((R330) PATHS)."""
    p = os.path.join(D, 'b716_federation_pin_price.txt')
    t = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return tuple('D:/' + m.group(1) for m in re.finditer(r'(?m)^  (SIDE-[A-Za-z0-9-]+)\s+HEAD ', t))


KERNEL_PATHS = _kernel_paths()
PATHS = ('D:/relay', PP, EF_DIR) + tuple(k for k in KERNEL_PATHS if k != EF_DIR)   # ### (R330)'s PATHS, listed at step zero
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, untouched (N5)
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main, untouched (N5)
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### the deposit, untouched (N5)
PORT_BRANCH = 'port-b707'
PORT_TIP = 'cb0aea56354abb3abda3fdaef28429c6605605d5'   # ### port-b707's tip, unmoved
PORT_NEW_TIP = PORT_TIP
LV_TAG = 'v0.14.0'
LV_TAG_OBJECT = '0e7c3527c8ff693c34126b57d1b1587149e5371c'
LV_TAG_RULED = 'v0.11.0'
KERNEL = 'SIDE-lv-conservation'
JOIN_NEW_TIP = '11a472b90553deaddc411c5d69ec03611ee277c5'   # ### SIDE-faces-join main, unmoved
JOIN_RUN = 40210894425
JOIN_TAG = ('v0.1.0', '9bf6fe65582187a92b6ab17e03953efb2cecd913', '11a472b90553deaddc411c5d69ec03611ee277c5')   # ### tag object, peeled
EF_V037 = '38e273477257687d676033be0b0243af84a1e08a'

PAPERS = dict()
DATA_STANDING_V1 = 'data/standing_clauses_v1.txt'
DATA_STANDING_V2 = 'data/standing_clauses_v2.txt'
DATA_STANDING_V3 = 'data/standing_clauses_v3.txt'
DATA_STANDING_V4 = 'data/standing_clauses_v4.txt'
DATA_STANDING_V5 = 'data/standing_clauses_v5.txt'
DATA_STANDING_V6 = 'data/standing_clauses_v6.txt'
DATA_STANDING = 'data/standing_clauses_v7.txt'   # ### binds the act whole (the ferry); unchanged this act
ARM_TAGS = 'data/arm_tags.json'
REPO_VISIBILITY = 'data/repo_visibility.txt'
REGISTRATIONS = 'data/b719_registrations.txt'    # ### N2: b719's registrations, read unchanged from their commits (ac88ffb1, 7b1ab86f, 965cb8e8)
REG_COMMIT = '965cb8e84dc02192854512af53a29b1fbc2b80f5'   # ### the last commit of data/b719_registrations.txt (H-SHAPE)
REG_COMMITS = (('data/b716_registrations.txt', 'dc5e808f'), ('data/b718_registrations.txt', '8146404b577dfee3e379d19e08e8595ab8824961'),
               ('data/b719_registrations.txt', '965cb8e84dc02192854512af53a29b1fbc2b80f5'))   # ### N2: each read unchanged from its commit
REG_FILES = tuple(f for f, _c in REG_COMMITS)
PRED_B717 = 'data/b717_predictions.txt'
PRED_B717_COMMIT = 'f47d8ab5840d287bf63c1f0b59ba707ed85dbe07'
PREDICTIONS = PRED_B717
ONSETS_B717 = 'data/b717_onsets.txt'
REGISTRATIONS_NEW = 'data/b720_registrations.txt'   # ### (R330)(3), N2: committed alone before any figure at -35 or -40
COEFF_BANKS = ('data/b711_coeffs.txt', 'data/b713_coeffs.txt', 'data/b717_coeffs.txt', 'data/b719_coeffs.txt')   # ### -23, -15, -39, -20 and -47: read not written
COMPUTE_BANKS = ('data/b720_coeffs.txt', 'data/b720_coeffs.json', 'data/b720_derivation.txt', 'data/b720_derivation.json',
                 'data/b720_registrations.txt', 'data/b720_offset_price.txt')
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b719 carried them
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b720'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', 'REGISTRY.md')   # ### (R330)(1)-(2) the weight line and corrigendum, (5)(i) REGISTRY's block,
#   ### the entry and the trail; no paper written this act
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the MANIFEST control's reference, as carried; (R330)(2)(ii) reads it from its source
NEXT = ('b721 ((R330)(10)): the surgery under H-SHAPE; the offset`s next tier under H-OFFSET, post hoc on its first seventeen rows; the registry cells for the next wave`s rows; '
        'the pin where (5)(iii) carried it')
NEXT_ACT = 'b721'


def orders_naming(ot_text, act):
    """the NEXT line's repair: every open-orders row of OPEN_TRAILS whose status names <act> -- a row is a line opening
    `*Appended` that carries `THE ORDER **`W-ORD-`; its status is its text from its last `Status`; returned as (line, order, status). Pure in
    its arguments."""
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

# ### stage one (step zero): the commits made so far, each set by the Edit tool after it is made
ACT_CURRENT = 'data/act_current.json'
STANDING_DIR = 'tools/standing'         # ### the standing close toolset, versioned by tools/standing/VERSION, at v1.2.0 entering this act
STANDING_COMMIT = None                  # ### no standing clauses version written this act (v7 binds)
ACT_CURRENT_COMMIT = '675d8598'         # ### data/act_current.json for b720 committed alone
STEPZERO = 'ec7071b5'                   # ### b719's closing capture, committed alone ((R330)(7))
STEPZERO_STEPS = '9ec21954'             # ### b719's step-33 row, committed alone ((R330)(7))
STEPZERO_LATE = '6755e0c9'              # ### the late step row for dbea2e3f ((R330)(2)(i))
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None
STEPZERO_REFUSALS = None
STEPZERO_BANKS = 'e3b3de12'             # ### the step-zero banks and tools, committed together by explicit list
VISIBILITY_COMMIT = None
COMPUTE_TOOLS = ()
REPAIRED_TOOLS = ()
REPAIRED_DATA = ()
STANDING_FILES = ('VERSION', 'act.py', 'allow.py', 'arms.py', 'classes.py', 'close.py', 'components.py', 'controls.py', 'hook.py', 'keystone.py',
                  'manifest.py', 'needles.py', 'repairs.py', 'replay.py', 'rootbanks.py', 'roster.py', 'scan.py', 'words.py')
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset at v1.2.0, sealed by hash beside the act's tools
STANDING_VERSION = 'v1.2.0'
STANDING_CHANGED = ()                   # ### no standing file changed this act
STANDING_NEW = ()
# ### b719's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = 'ef648cb9'    # ### b719's closing, the act's relay base
B714_RECORD = 'fa268307'     # ### b719's record commit (relay, the last before the closing)
B714_ROOT = '09e524a73dde38bfe1f9bdd3337b7644997a3f5ed649caec7835cd6d04803b6b'   # ### b719's root, data/act_roots.txt :97
# ### stage two (Component 7, before the lock): the commits of the components, read from the logs after each was made
C1_RELAY = '67987367'       # ### the corrigendum's relay banks (step 7)
C1_PP = '5f34d8c3'          # ### the weight line and the corrigendum in FINDINGS (step 6)
WEIGHT_LINE, CORR_LINE = 11018, 11020   # ### FINDINGS :11018 (the weight line), :11020 (the corrigendum)
DIFFERS_LINE = None
ERRATA_LINE = None
C2_REG = 'f5353ca9'          # ### (R330)(3), N2: data/b720_registrations.txt committed alone, before any figure at -35 or -40 (step 8)
C2_PRED = '54fc03d9'         # ### the shape rule's prediction, its controls first, added by a commit of its own before any coefficient (step 9)
C2_CTL = '16fb14c2'          # ### the coefficients' controls C1-C3, printed first (step 10)
C2_RELAY = '29c10c06'        # ### the coefficients at -35 and -40, every row read (step 11)
C3_RELAY = 'ce378824'        # ### the derivation's -2, data/b720_derivation.txt (step 12)
C4_REG = None                # ### no registration this component (the carried name kept for the carried readers)
C4_PP = '5872b8979c01aaf66fe926ae4a4925fc22687fc5'   # ### (R330)(5)(i): REGISTRY's three rows and attribute block, additive (step 13)
C4_RELAY = 'ad94c11c'        # ### the registry tool and data/b720_registry_diff.txt (step 14)
C5_REG = None
C5_RELAY = '41a0adcf'        # ### (R330)(5)(ii): the challenge tool and its banks (step 15)
C6_RELAY = '03f755e7'        # ### (R330)(5)(iii), (6): the pin tool, its banks and the offset's price (step 16)
C6_PP = None
C6_PP_REPAIR = None
NEW_DISCRIMINANTS = ((-35, 2), (-40, 2))   # ### (R330)(3): class number 2, two units, fundamental
CHALLENGE_BRANCH = 'challenge-b720-h2-sign-iff-rh'   # ### (R330)(5)(ii): on SIDE-explicit-formula, not on main, no tag
CHALLENGE_TIP = '3391647518cd37316a448b5013afb62a198fa6c6'
CHALLENGE_RUN = 40651875792
PIN_RUNS = (('SIDE-grh-transfer', 40652622018), ('SIDE-interfaces', 40652657325), ('SIDE-kernel', 40652692787),
            ('SIDE-lv-conservation', 40652727943), ('SIDE-simplicity', 40652762827), ('SIDE-trivium', 40652790458))   # ### each read by its id
PIN_BRANCH = 'pin-b718-de5ce8a9'   # ### b718's local pin branches, carried to b720
PIN_EXCLUDED = ('SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve', 'SIDE-cosmo')   # ### N4: the freeze and SIDE-cosmo, never pushed
PIN_HELD = ('SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium')   # ### BREAKS, held, nothing repaired
PIN_BUILDS = ('SIDE-simplicity',)
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')   # ### b718's nine local bump branches, as step zero's citation check read them
PIN_TO_NEXT = PIN_HELD       # ### to b721 ((R330)(10)): the pin where (5)(iii) carried it
MAX_DISPATCHES = 1 + len(PIN_RUNS)   # ### N1: the challenge's one and the pin's six
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md', 'REGISTRY.md')
ERRATA_ID = None
ERRATA_IDS = ()
RETIRED_COUNT = 0            # ### no arm retired this act; b719's run list of 116 binds
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b720_') and f.endswith('.py') and f != 'b720_report.py')) + NEW_TOOLS + COMPUTE_TOOLS
# ### the act's arms over its own banks: set at Component 7 by the Edit tool -- the thirty-two of the suite's act part (b719's less the arms
# ### b719 retired, G-R329-ENTERED shifted to G-R330-ENTERED), as `b720_record.py armnames` prints them beyond the standing (set late, defect (y))
ACT_ARMS = ('G-ACT-CURRENT', 'G-ARM-TAGS', 'G-ARMS-RETIRED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED', 'G-CLOSING-DRY-STEP', 'G-COEFFS-LAW',
            'G-CORRIGENDUM-ENTERED', 'G-COUNT-ROUTE-PRICED', 'G-DELETES-ONE-BRANCH', 'G-DERIVATION-GRADED', 'G-DIFFERS-ERRATA', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-GUARD-HELD', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LISTINGS-BEFORE-CLAUSES',
            'G-MEMBRANE-WIRED', 'G-OFFSET-POST-HOC', 'G-POSTROOT-WRITES-NONE', 'G-PREDICTION-FIRST', 'G-R330-ENTERED', 'G-READFIRST-DIFF-BANKED',
            'G-REGISTRATIONS-FIRST', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED', 'G-SURGERY-CARRIED', 'G-TOUCH-READ',
            'G-WRITELIST-MIRROR-STATE')
