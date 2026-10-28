# -*- coding: utf-8 -*-
"""b719_worklist.py -- THE ACT'S DATA, UNDER (R329). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b719: LANE TWO, ACT ONE HUNDRED AND FORTY-SIX, THE COEFFICIENT ACT -- b718'S CLOSE COMPLETED AT STEP ZERO UNDER b718'S SEALED TOOLS;
### THE CORRIGENDUM; THE ELEVEN DIFFERS; THE JOIN'S PREMISE IN ERRATA; THE LAW AT -20 AND -47 WITH H-24 AND H-47 REGISTERED BEFORE; THE
### DERIVATION'S REMAINING STEP; THE OFFSET READ, POST HOC; THE SURGERY, STOPPABLE; THE ARMS RETIRED. No lean on this host and no runner
### dispatch this act (N1).
### Carried by diff from b718_worklist.py (data/b719_carry_worklist.txt) and its stage one rewritten whole by the Write tool with this act's
### objects at step zero (the carried text named b718's objects under b719's names); stage two, Component 7, by the Edit tool.
### The act runs in the SAME session as b718 (02c7cf38; b718 halted before its root on the author's guard and its close is completed at this
### act's step zero): the previous act's window is this session cut at b718's anchor, b706's same-session form.
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'b6cbbbdc277ca5e752c622476a48109ffe7ad387'    # ### PLACE-papers main before the act's own commits: b718's last PLACE-papers push (its trail), read back at step zero
PRE_RELAY = '9818a7f019b05c1b310fb18859fc229ab97f2ade'  # ### relay main before the act's own commits: b718's closing, pushed and read back at step zero
PRE_PP_REMOTE_AT_START = 'c02f47c1'      # ### PLACE-papers remote main at the act's start (b717's trail; b718 pushed nothing)
PRE_RELAY_REMOTE_AT_START = '248c5a97'   # ### relay remote main at the act's start (b717's closing; b718 pushed nothing)
B718_RELAY_HEAD = '5fe0c41'  # ### b718's record commit, the relay head the author's word pushes ((R329)(2))
B718_PP_HEAD = 'f8010aa'     # ### b718's FINDINGS entry commit, the PLACE-papers head the author's word pushes
DATE = '2026-10-28'
SESSION_ID = '02c7cf38-4c6a-4f88-b813-a7e15e9b85b4'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R329) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = SESSION_ID   # ### b718 ran in this session (from 'RULING (R328) BEGIN', with a compaction); b706's same-session form
PREV_ANCHOR = 'RULING (R328) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b719_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 10858          # ### FINDINGS: b718's entry head (landed at b718's step [12], PLACE-papers f8010aa)
B711_WEIGHT = 10820         # ### FINDINGS: b717's weight line (b718's Component 1)
B711_CORRIGENDUM = 10822    # ### FINDINGS: b718's corrigendum for b717 (data/b675_corrigenda.txt row (38))
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line, citing (R328)(6) for the toolset (event (10); (R329)(3)'s fact correction)
B711_TRAIL = 16128          # ### OPEN_TRAILS: b718's trail record, landed at b718's step [15] at this act's step zero (PLACE-papers b6cbbbd)
B711_FACE = 'data/b718_registration_2026-10-27.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-27-b718.zip'   # ### b718's export, built after b718's last push at this act's step zero, 74 files, CLEAN
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
TRAIL_ORDERS = 16030        # ### OPEN_TRAILS: b715's open orders line
TRAIL_RESOLVED = 16164      # ### OPEN_TRAILS: b718's items for the author's strike, in its trail (landed at b6cbbbd)
WATCH_LINE = 16126          # ### OPEN_TRAILS: W-ORD-QUASI-RH-FIELD-WATCH, annotated at b718's C6
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row

# ### the branches step zero deletes ((R329)(12)): the push-b718-* branches b718's close makes at this act's step zero, by name, each read from
# ### the listings and `--merged` printed before the deletes, one per command, each its own message (set by the Edit tool after b718's close)
DELETE = (('D:/relay', ('push-b718-closing', 'push-b718-preroot', 'push-b718-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b718-preroot', 'push-b718-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R329)(12): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'),)

# ### the kernels: none written this act (N1, N5); lv read for (R329)(5) at its deposit and not written
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
# ### the federation pin: moved to b720 ((R329)(11)); its names kept for the carried readers, nothing dispatched
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PATHS = ('D:/relay', PP, LV_DIR)   # ### (R329)'s PATHS, listed at step zero
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, unmoved
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main, untouched (N5)
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### the deposit, untouched (N5); (R329)(5) reads RegisterPentagon.lean :149-:152 at it
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
MAX_DISPATCHES = 0          # ### N1: no runner dispatch this act

PAPERS = dict()
DATA_STANDING_V1 = 'data/standing_clauses_v1.txt'
DATA_STANDING_V2 = 'data/standing_clauses_v2.txt'
DATA_STANDING_V3 = 'data/standing_clauses_v3.txt'
DATA_STANDING_V4 = 'data/standing_clauses_v4.txt'
DATA_STANDING_V5 = 'data/standing_clauses_v5.txt'
DATA_STANDING_V6 = 'data/standing_clauses_v6.txt'
DATA_STANDING = 'data/standing_clauses_v7.txt'   # ### binds the act whole (the ferry); unchanged this act
ARM_TAGS = 'data/arm_tags.json'                  # ### (R329)(10): the tags the retirement reads
REPO_VISIBILITY = 'data/repo_visibility.txt'
REGISTRATIONS = 'data/b718_registrations.txt'    # ### (R329)(6)(i), N2: b718's registrations, read unchanged from 8146404b
REG_COMMIT = '8146404b577dfee3e379d19e08e8595ab8824961'   # ### b718's commit of data/b718_registrations.txt, alone
REG_FILES = ('data/b718_registrations.txt',)
PRED_B717 = 'data/b717_predictions.txt'   # ### (R329)(8)(i): b717's -39 predictions, committed alone at f47d8ab5, read not written
PRED_B717_COMMIT = 'f47d8ab5840d287bf63c1f0b59ba707ed85dbe07'
PREDICTIONS = PRED_B717
ONSETS_B717 = 'data/b717_onsets.txt'      # ### (R329)(8)(i): b717's onset bank for -39
REGISTRATIONS_NEW = 'data/b719_registrations.txt'   # ### (R329)(6)(i): committed alone before any figure at -20 or -47 (N2)
COEFF_BANKS = ('data/b711_coeffs.txt', 'data/b713_coeffs.txt', 'data/b717_coeffs.txt')   # ### -23, -15, -39: the checks' banks, read not written
COMPUTE_BANKS = ('data/b719_coeffs.txt', 'data/b719_coeffs.json', 'data/b719_derivation.txt', 'data/b719_derivation.json',
                 'data/b719_registrations.txt', 'data/b719_offset.txt', 'data/b719_surgery.txt')
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b718 carried them
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b719'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', 'ERRATA.md')   # ### (R329)(3)-(4) the corrigendum entries, (5) the ERRATA entry, the entry and
#   ### the trail; no paper, no REGISTRY row written this act (the REGISTRY cells moved to b720, (R329)(11))
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'
NEXT = ('b720 ((R329)(14)): the REGISTRY cells, the pin`s remainder and the challenge file, for wave 1`s sign core; the next tier of the '
        'offset under (8)(ii)`s registration; the surgery where (9) carried it')
NEXT_ACT = 'b720'


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
ACT_CURRENT_COMMIT = None               # ### data/act_current.json for b719 committed alone
STEPZERO = None                         # ### b718's step-20 row committed alone ((R329)(12)), after b718's close
STEPZERO_STEPS = None
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
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset at v1.2.0, sealed by hash beside the act's tools
STANDING_VERSION = 'v1.2.0'
STANDING_CHANGED = ()                   # ### (R329)(10) changes the suite's run list (set at Component 6)
STANDING_NEW = ()
# ### b718's commits the act reads ((R329)(2)); set after b718's close at step zero
B714_CLOSING = '9818a7f0'    # ### b718's closing, the act's relay base (the names kept for the carried arms: the previous act's)
B714_RECORD = '098289c8'     # ### b718's record commit (relay), pushed at step zero (5fe0c412 the pre-root push, 1c1ce75e the root)
B714_ROOT = 'b2f1908e325787b31b36d9249d7d68baa7f4e4d905498b4ac04164810fc7fc8b'   # ### b718's root, data/act_roots.txt :96, computed at step zero
# ### stage two (Component 7, before the lock): the commits of the components, read from the logs after each was made
C1_RELAY = None
C1_PP = None
WEIGHT_LINE, CORR_LINE = None, None
C2_REG = None                # ### (R329)(6)(i), N2: data/b719_registrations.txt committed alone, before any figure at -20 or -47
C2_RELAY = None
C3_RELAY = None
C4_REG = None                # ### (R329)(8)(ii): the offset's hypothesis added to data/b719_registrations.txt by a commit of its own
C4_RELAY = None
C5_REG = None                # ### (R329)(9): H-SHAPE committed before any number
C5_RELAY = None
C6_RELAY = None
C6_PP = None
C6_PP_REPAIR = None
NEW_DISCRIMINANTS = ((-20, 2), (-47, 5))   # ### (R329)(6): b718's registered discriminants, computed this act
PIN_RUNS = ()                # ### N1: no dispatch this act
PIN_BRANCH = 'pin-b718-de5ce8a9'   # ### b718's local pin branches, carried to b720 unpushed
PIN_HELD = ('SIDE-cosmo', 'SIDE-frobenius')
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md', 'ERRATA.md')
ERRATA_ID = None             # ### (R329)(5): the ERRATA entry's id, set when written
ERRATA_IDS = ()
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b719_') and f.endswith('.py') and f != 'b719_report.py')) + NEW_TOOLS + COMPUTE_TOOLS
# ### the act's arms over its own banks: set at Component 7 by the Edit tool (b718's ritual arms carried; its arms over b718's objects replaced
# ### by arms over this act's: the registrations first, the coefficients, the derivation graded, the offset post hoc, the surgery, the retirement)
ACT_ARMS = ()
