# -*- coding: utf-8 -*-
"""b721_worklist.py -- THE ACT'S DATA, UNDER (R331). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b721: LANE TWO, ACT ONE HUNDRED AND FORTY-EIGHT, THE TABLE ACT -- b720 AT ITS WEIGHT; THE CORRIGENDUM AND THREE REPAIRS; THE C2
### TABLE TESTED AT TWO DISCRIMINANTS IT CHOOSES; THE TABLE OVER h = 3, 4, 5; THE OFFSET; THE SURGERY, STOPPABLE; THE FROZEN LINE'S WORDS AND
### ITS REBUILD; THE FEDERATION PIN CLOSED. No lean on this host (N1); the runner dispatches are (R331)(7)(iii)'s alone, six at most.
### Carried by diff from b720_worklist.py (data/b721_carry_worklist.txt) and its stage one rewritten whole by the Write tool with this act's
### objects at step zero (the carried text named b720's objects under b721's names); stage two, Component 8, by the Edit tool.
### The act runs in the SAME session as b720 (02c7cf38; the ruling pasted after b720's closing, no clear): the previous act's window is this
### session cut at b720's anchor, b706's same-session form. b720 closed and pushed itself whole (relay 8834a5b6, PLACE-papers b826da8c, both
### read back); its closing capture and step-38 row are this act's carried files ((R331)(9)).
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'b826da8ce1e766add12006b048f9f737f93922bd'    # ### PLACE-papers main before the act's own commits: b720's trail, pushed and read back by b720
PRE_RELAY = '8834a5b6bc5cea2d3bb64de5bbc898ee58d5c9e6'  # ### relay main before the act's own commits: b720's closing, pushed and read back by b720
PRE_PP_REMOTE_AT_START = 'b826da8c'      # ### PLACE-papers remote main at the act's start (read at step zero, equal to local)
PRE_RELAY_REMOTE_AT_START = '8834a5b6'   # ### relay remote main at the act's start (read at step zero, equal to local)
B718_RELAY_HEAD = '8834a5b'  # ### the names kept for the carried readers: the previous act's last relay head (b720's closing)
B718_PP_HEAD = 'b826da8'     # ### the previous act's last PLACE-papers head (b720's trail)
DATE = '2026-10-28'
SESSION_ID = '02c7cf38-4c6a-4f88-b813-a7e15e9b85b4'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R331) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = SESSION_ID   # ### b720 ran in this session (from 'RULING (R330) BEGIN', with a compaction); b706's same-session form
PREV_ANCHOR = 'RULING (R330) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b721_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 11072          # ### FINDINGS: b720's entry head (PLACE-papers 4186d07b, its title in the author's words)
B711_WEIGHT = 11018         # ### FINDINGS: b719's weight line (b720's Component 1)
B711_CORRIGENDUM = 11020    # ### FINDINGS: b720's corrigendum for b719
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 16218          # ### OPEN_TRAILS: b720's trail record (PLACE-papers b826da8c)
B711_FACE = 'data/b720_registration_2026-10-28.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-28-b720.zip'   # ### b720's export, built after b720's last push, 74 files, CLEAN
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
TRAIL_ORDERS = 16030        # ### OPEN_TRAILS: b715's open orders line
TRAIL_RESOLVED = 16256      # ### OPEN_TRAILS: b720's items for the author's strike, in its trail (landed at b826da8c)
WATCH_LINE = 16126          # ### OPEN_TRAILS: W-ORD-QUASI-RH-FIELD-WATCH, annotated at b718's C6
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row

# ### the branches step zero deletes ((R331)(9)): the push-b720-* branches b720's close made, by name, each read from the listings and
# ### `--merged` printed before the deletes (state721 at step zero), one per command, each its own message
DELETE = (('D:/relay', ('push-b720-closing', 'push-b720-preroot', 'push-b720-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b720-preroot', 'push-b720-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R331)(9): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'),)

# ### the kernels: the rebuild branches of (R331)(7)(iii), one per wave 1 kernel at its own pin; no main, no tag
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')


def _kernel_paths():
    """the kernels of data/b716_federation_pin_price.txt (1), as D:/<name>, read at import ((R331) PATHS)."""
    p = os.path.join(D, 'b716_federation_pin_price.txt')
    t = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return tuple('D:/' + m.group(1) for m in re.finditer(r'(?m)^  (SIDE-[A-Za-z0-9-]+)\s+HEAD ', t))


KERNEL_PATHS = _kernel_paths()
PATHS = ('D:/relay', PP, KERNEL_DIR, LV_DIR, EF_DIR) + tuple(k for k in KERNEL_PATHS if k not in (EF_DIR, KERNEL_DIR, LV_DIR))   # ### (R331)'s PATHS
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, untouched (N5)
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main, untouched (N5)
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### the deposit, untouched (N5); the rebuild's pin for SIDE-lv-conservation
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
# ### (R331)(7): the wave 1 kernels at their own pins, (name, tag, the ruling's short commit); the full commits read at step zero
WAVE1 = (('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-archimedean', 'v0.1.0', '8019d9d'),
         ('SIDE-frobenius', 'v0.1.0', '2efe9f2'), ('SIDE-spinor', 'v0.1.0', 'b235bc6'), ('SIDE-rcurve', 'v0.1.0', 'd5f33b4'))
CHECKPOINT_STATEMENTS = (('SIDE-archimedean', 'archimedean_forces_half'), ('SIDE-frobenius', 'indicial_forces_half'),
                         ('SIDE-spinor', 'spinor_forces_half'), ('SIDE-spinor', 'half_iff_centered_zero'), ('SIDE-rcurve', 'monotone_unique_zero'))
REBUILD_BRANCH = 'rebuild-b721-own-pin'   # ### (R331)(7)(iii): one branch per kernel at its pinned commit, set at Component 6
REBUILD_RUNS = ()                         # ### (kernel, run id), each read by its id; set at Component 6

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
REGISTRATIONS = 'data/b720_registrations.txt'    # ### N2: b720's registrations, read unchanged from their commit (f5353ca9, 54fc03d9)
REG_COMMIT = '54fc03d9'                          # ### the last commit of data/b720_registrations.txt (the prediction's rows)
REG_COMMITS = (('data/b716_registrations.txt', 'dc5e808f'), ('data/b718_registrations.txt', '8146404b577dfee3e379d19e08e8595ab8824961'),
               ('data/b719_registrations.txt', '965cb8e84dc02192854512af53a29b1fbc2b80f5'), ('data/b720_registrations.txt', '54fc03d9'))   # ### N2
REG_FILES = tuple(f for f, _c in REG_COMMITS)
PRED_B717 = 'data/b717_predictions.txt'
PRED_B717_COMMIT = 'f47d8ab5840d287bf63c1f0b59ba707ed85dbe07'
PREDICTIONS = PRED_B717
ONSETS_B717 = 'data/b717_onsets.txt'
REGISTRATIONS_NEW = 'data/b721_registrations.txt'   # ### (R331)(3)(ii), N2: committed alone before any figure at either C2 discriminant
COEFF_BANKS = ('data/b711_coeffs.txt', 'data/b713_coeffs.txt', 'data/b717_coeffs.txt', 'data/b719_coeffs.txt', 'data/b720_coeffs.txt')   # ### read not written
COMPUTE_BANKS = ('data/b721_coeffs.txt', 'data/b721_coeffs.json', 'data/b721_derivation.txt', 'data/b721_derivation.json',
                 'data/b721_registrations.txt', 'data/b721_offset.txt', 'data/b721_frozen_line.txt', 'data/b721_frozen_line_drafts.txt')
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b720 carried them
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b721'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md')   # ### (R331)(1)-(2) the weight line and corrigendum, (8) the pin's orders CLOSED, the entry and
#   ### the trail; no paper written this act
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the re-cut's merge (kept for the kernel rows); the MANIFEST control's reference
#   ### is the commit the mirror is built at from v1.2.1 ((R331)(2)(iii))
NEXT = ('b722 ((R331)(11)): the h = 3 and h = 4 discriminants computed under (4)`s commit; the offset`s pairs and the surgery where (5)-(6) carried them; '
        'the release sitting`s front-door list assembled from (7)(ii) and the edits already planned')
NEXT_ACT = 'b722'


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
ACT_CURRENT_COMMIT = None               # ### data/act_current.json for b721 committed alone
STEPZERO = None                         # ### b720's closing capture, committed alone ((R331)(9))
STEPZERO_STEPS = None                   # ### b720's step-38 row, committed alone ((R331)(9))
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None
STEPZERO_REFUSALS = None
STEPZERO_BANKS = None                   # ### the step-zero banks and tools, committed together by explicit list
VISIBILITY_COMMIT = None
COMPUTE_TOOLS = ()
REPAIRED_TOOLS = ()
REPAIRED_DATA = ()
STANDING_FILES = ('VERSION', 'act.py', 'allow.py', 'arms.py', 'classes.py', 'close.py', 'components.py', 'controls.py', 'hook.py', 'keystone.py',
                  'manifest.py', 'needles.py', 'repairs.py', 'replay.py', 'rootbanks.py', 'roster.py', 'scan.py', 'words.py')
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset, sealed by hash beside the act's tools
STANDING_VERSION = 'v1.2.0'             # ### v1.2.1 once (R331)(2) lands it (Component 1)
STANDING_CHANGED = ()                   # ### the standing files (R331)(2)'s three repairs change, set at Component 1
STANDING_NEW = ()
# ### b720's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = '8834a5b6'    # ### b720's closing, the act's relay base
B714_RECORD = '6d7cb5f7'     # ### b720's record commit (relay, the last before the closing)
B714_ROOT = 'b5a76ed924905059cdc9da73936b81a4507eaf9ea286f6e2f3438c9300eab77b'   # ### b720's root, data/act_roots.txt :98
# ### stage two (Component 8, before the lock): the commits of the components, read from the logs after each was made
C1_RELAY = None             # ### the corrigendum's relay banks
C1_PP = None                # ### the weight line and the corrigendum in FINDINGS
WEIGHT_LINE, CORR_LINE = None, None
DIFFERS_LINE = None
ERRATA_LINE = None
C2_REG = None                # ### (R331)(3)(ii), N2: data/b721_registrations.txt committed alone, before any figure at either C2 discriminant
C2_PRED = None               # ### (R331)(4): the h = 3 and h = 4 predictions, a commit of their own
C2_CTL = None                # ### the coefficients' controls C1-C3, printed first
C2_RELAY = None              # ### the coefficients at the two C2 discriminants, every row read
C3_RELAY = None              # ### (R331)(4): the table over h = 3, 4, 5, data/b721_derivation.txt
C4_REG = None
C4_PP = None
C4_RELAY = None              # ### (R331)(5): the offset
C5_REG = None
C5_RELAY = None              # ### (R331)(6): the surgery
C6_RELAY = None              # ### (R331)(7): the frozen line, its drafts and the rebuild
C6_PP = None
C6_PP_REPAIR = None
C7_PP = None                 # ### (R331)(8): the federation pin's orders CLOSED in OPEN_TRAILS
NEW_DISCRIMINANTS = ()       # ### (R331)(3)(i): the two C2 discriminants the rule names, set when it names them
CHALLENGE_BRANCH = 'challenge-b720-h2-sign-iff-rh'   # ### b720's, on SIDE-explicit-formula, standing, not merged, no tag
CHALLENGE_TIP = '3391647518cd37316a448b5013afb62a198fa6c6'
CHALLENGE_RUN = 40651875792
PIN_RUNS = (('SIDE-grh-transfer', 40652622018), ('SIDE-interfaces', 40652657325), ('SIDE-kernel', 40652692787),
            ('SIDE-lv-conservation', 40652727943), ('SIDE-simplicity', 40652762827), ('SIDE-trivium', 40652790458))   # ### b720's, read not re-run
PIN_BRANCH = 'pin-b718-de5ce8a9'   # ### b718's pin branches, left as banked ((R331)(9))
PIN_EXCLUDED = ('SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve', 'SIDE-cosmo')   # ### never pushed on the pin branch
PIN_HELD = ('SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium')   # ### BREAKS, held, nothing repaired
PIN_BUILDS = ('SIDE-simplicity',)
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')   # ### b718's nine local bump branches
PIN_TO_NEXT = ()             # ### (R331)(8): the federation pin CLOSED at its banked state; nothing carried
MAX_DISPATCHES = 6           # ### N1: the rebuild's six at most
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md')
ERRATA_ID = None
ERRATA_IDS = ()
RETIRED_COUNT = 0            # ### no arm retired this act; the run list of 116 binds
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b721_') and f.endswith('.py') and f != 'b721_report.py')) + NEW_TOOLS + COMPUTE_TOOLS
# ### the act's arms over its own banks: set at Component 8 by the Edit tool, as `b721_record.py armnames` prints them beyond the standing
ACT_ARMS = ()
