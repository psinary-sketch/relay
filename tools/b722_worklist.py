# -*- coding: utf-8 -*-
"""b722_worklist.py -- THE ACT'S DATA, UNDER (R332). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b722: LANE TWO, ACT ONE HUNDRED AND FORTY-NINE, THE INSTRUMENTS ACT -- b721 AT ITS WEIGHT; THE CORRIGENDUM AND THREE REPAIRS; -31 AND
### -55 UNDER e8c3dff4; THE FOURTEEN CLASS-NUMBER-2 FIELDS UNDER H-C2-WALK; THE C2 STATEMENT FOR LEAN; THE INSTRUMENTS AND THEIR REPRODUCTION
### RUNNER; THE PROPAGATION READ (v8); THE AUTHOR'S NAME AND ADDRESS; THE AXIOM STEP DIAGNOSED. No lean on this host and nothing dispatched (N1).
### Carried by diff from b721_worklist.py (data/b722_carry_worklist.txt) and its stage one rewritten whole by the Write tool with this act's
### objects at step zero (the carried text named b721's objects under b722's names); stage two, Component 8, by the Edit tool.
### The act runs in the SAME session as b721 (02c7cf38; the ruling pasted after b721's closing, no clear): the previous act's window is this
### session cut at b721's anchor, b706's same-session form. b721 closed and pushed itself whole (relay 30c0b3c8, PLACE-papers 2b194142, both
### read back); its closing capture and step-42 row are this act's carried files ((R332)(11)).
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '2b194142b2962ed55c17cfa82a12f63bd4bb610c'    # ### PLACE-papers main before the act's own commits: b721's record, pushed and read back by b721
PRE_RELAY = '30c0b3c874440888e96d074f3d00a40d5ca57ec1'  # ### relay main before the act's own commits: b721's closing, pushed and read back by b721
PRE_PP_REMOTE_AT_START = '2b194142'      # ### PLACE-papers remote main at the act's start (read at step zero, equal to local)
PRE_RELAY_REMOTE_AT_START = '30c0b3c8'   # ### relay remote main at the act's start (read at step zero, equal to local)
B718_RELAY_HEAD = '30c0b3c'  # ### the names kept for the carried readers: the previous act's last relay head (b721's closing)
B718_PP_HEAD = '2b19414'     # ### the previous act's last PLACE-papers head (b721's record)
DATE = '2026-10-28'
SESSION_ID = '02c7cf38-4c6a-4f88-b813-a7e15e9b85b4'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R332) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = SESSION_ID   # ### b721 ran in this session (from 'RULING (R331) BEGIN', with compactions); b706's same-session form
PREV_ANCHOR = 'RULING (R331) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b722_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 11178          # ### FINDINGS: b721's entry head (PLACE-papers 2b194142, its title in the author's words)
B711_WEIGHT = 11108         # ### FINDINGS: b720's weight line (b721's Component 1)
B711_CORRIGENDUM = 11110    # ### FINDINGS: b721's corrigendum for b720
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 16264          # ### OPEN_TRAILS: b721's trail record (PLACE-papers 2b194142)
B711_FACE = 'data/b721_registration_2026-10-28.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-28-b721.zip'   # ### b721's export, built after b721's last PLACE-papers push, 74 files, CLEAN
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
TRAIL_ORDERS = 16030        # ### OPEN_TRAILS: b715's open orders line
TRAIL_RESOLVED = 16302      # ### OPEN_TRAILS: b721's items for the author's strike, in its trail (landed at 2b194142)
WATCH_LINE = 16126          # ### OPEN_TRAILS: W-ORD-QUASI-RH-FIELD-WATCH, annotated at b718's C6
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row
INSTRUMENTS = 'phase1.5/method/INSTRUMENTS.md'   # ### (R332)(6): PLACE-papers' instruments document, its last entry I-40 (b692) at :486
INSTRUMENTS_LAST = 40

# ### the branches step zero deletes ((R332)(11)): the push-b721-* branches b721's close made, by name, each read from the listings and
# ### `--merged` printed before the deletes (state722 at step zero), one per command, each its own message
DELETE = (('D:/relay', ('push-b721-closing', 'push-b721-preroot', 'push-b721-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b721-preroot', 'push-b721-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R332)(11): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'), ('D:/SIDE-explicit-formula', 'challenge-b720-h2-sign-iff-rh'),
                 ('D:/SIDE-kernel', 'rebuild-b721'), ('D:/SIDE-lv-conservation', 'rebuild-b721'), ('D:/SIDE-archimedean', 'rebuild-b721'),
                 ('D:/SIDE-frobenius', 'rebuild-b721'), ('D:/SIDE-spinor', 'rebuild-b721'), ('D:/SIDE-rcurve', 'rebuild-b721'))

# ### the kernels: read, not written; nothing dispatched this act (N1)
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')


def _kernel_paths():
    """the kernels of data/b716_federation_pin_price.txt (1), as D:/<name>, read at import ((R332) PATHS)."""
    p = os.path.join(D, 'b716_federation_pin_price.txt')
    t = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return tuple('D:/' + m.group(1) for m in re.finditer(r'(?m)^  (SIDE-[A-Za-z0-9-]+)\s+HEAD ', t))


KERNEL_PATHS = _kernel_paths()
PATHS = ('D:/relay', PP, KERNEL_DIR, LV_DIR, EF_DIR) + tuple(k for k in KERNEL_PATHS if k not in (EF_DIR, KERNEL_DIR, LV_DIR))   # ### (R332)'s PATHS
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
# ### the wave 1 kernels at their own pins, (name, tag, the short commit) -- b721's (R331)(7)
WAVE1 = (('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-archimedean', 'v0.1.0', '8019d9d'),
         ('SIDE-frobenius', 'v0.1.0', '2efe9f2'), ('SIDE-spinor', 'v0.1.0', 'b235bc6'), ('SIDE-rcurve', 'v0.1.0', 'd5f33b4'))
CHECKPOINT_STATEMENTS = (('SIDE-archimedean', 'archimedean_forces_half'), ('SIDE-frobenius', 'indicial_forces_half'),
                         ('SIDE-spinor', 'spinor_forces_half'), ('SIDE-spinor', 'half_iff_centered_zero'), ('SIDE-rcurve', 'monotone_unique_zero'))
REBUILD_BRANCH = 'rebuild-b721'          # ### b721's branches, kept for b723 ((R332)(11))
REBUILD_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-lv-conservation', 40706311269), ('SIDE-archimedean', 40706397470),
                ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404), ('SIDE-frobenius', 40713201832))   # ### b721's, each read by its id
AXIOM_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-archimedean', 40706397470), ('SIDE-frobenius', 40713201832),
              ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404))   # ### (R332)(10): the five whose axiom step is diagnosed
REBUILD_ROWS = 'data/b721_rebuild_rows.json'
FROBENIUS_COPY = 'f9410d2e64ad'
FROBENIUS_TWO_LINES = '6b06215745d0'

PAPERS = dict()
DATA_STANDING_V1 = 'data/standing_clauses_v1.txt'
DATA_STANDING_V2 = 'data/standing_clauses_v2.txt'
DATA_STANDING_V3 = 'data/standing_clauses_v3.txt'
DATA_STANDING_V4 = 'data/standing_clauses_v4.txt'
DATA_STANDING_V5 = 'data/standing_clauses_v5.txt'
DATA_STANDING_V6 = 'data/standing_clauses_v6.txt'
DATA_STANDING_V7 = 'data/standing_clauses_v7.txt'
DATA_STANDING = 'data/standing_clauses_v7.txt'   # ### binds the act whole; v8 from the commit that lands it at Component 6 ((R332)(8))
DATA_STANDING_V8 = 'data/standing_clauses_v8.txt'
ARM_TAGS = 'data/arm_tags.json'
REPO_VISIBILITY = 'data/repo_visibility.txt'
REGISTRATIONS = 'data/b721_registrations.txt'    # ### N2: b721's registrations, read unchanged from their commits
REG_COMMIT = 'e8c3dff4'                          # ### the last commit of data/b721_registrations.txt (H-C3-31, H-C4-55)
REG_WALK_COMMIT = '15cb6cc4'                     # ### H-C2-WALK's commit (:62-:70, the fourteen registered blind)
REG_COMMITS = (('data/b716_registrations.txt', 'dc5e808f'), ('data/b718_registrations.txt', '8146404b577dfee3e379d19e08e8595ab8824961'),
               ('data/b719_registrations.txt', '965cb8e84dc02192854512af53a29b1fbc2b80f5'), ('data/b720_registrations.txt', '54fc03d9'),
               ('data/b721_registrations.txt', 'e8c3dff40df43269b3f0c4b917baef7c96c0f649'))   # ### N2
REG_FILES = tuple(f for f, _c in REG_COMMITS)
PRED_B717 = 'data/b717_predictions.txt'
PRED_B717_COMMIT = 'f47d8ab5840d287bf63c1f0b59ba707ed85dbe07'
PREDICTIONS = PRED_B717
ONSETS_B717 = 'data/b717_onsets.txt'
REGISTRATIONS_NEW = None                         # ### no registration written this act; (3) and (4) read b721's unchanged
COEFF_BANKS = ('data/b711_coeffs.txt', 'data/b713_coeffs.txt', 'data/b717_coeffs.txt', 'data/b719_coeffs.txt', 'data/b720_coeffs.txt')   # ### read not written
COMPUTE_BANKS = ('data/b722_coeffs.txt', 'data/b722_coeffs.json', 'data/b722_walk.txt', 'data/b722_walk.json', 'data/b722_c2_statement.txt',
                 'data/b722_instruments.txt', 'data/b722_reproduce.txt', 'data/b722_propagation.txt', 'data/b722_axiom_diag.txt',
                 'data/b722_llm_line_drafts.txt')
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt',
              'data/b722_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b721 carried them
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b722'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### (R332)(7): G-RESEARCH-REPRODUCES joins at Component 5 (set by the Edit tool when it lands)
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', INSTRUMENTS)   # ### (R332)(1)-(2) the weight line and corrigendum, (6) the instruments, the entry
#   ### and the trail; (8)'s ledger notes where its run finds hits (set at Component 6); no paper written this act
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the re-cut's merge (kept for the kernel rows); the MANIFEST control's reference
#   ### is the commit the mirror is built at from v1.2.1
NEXT = ('b723 ((R332)(13)), the wave 1 act: the axiom step repaired on the rebuild-b721 branches and dispatched at the six pins, '
        'SIDE-lv-conservation`s sorry discharged or carried in its wording, the sign core`s paper drafted in paper mode, and the front-door list '
        'assembled for the release sitting; the C2 compile at the route the author names from (5)`s price; the surgery under H-SHAPE in an act of '
        'its own; the offset`s next pair where a list extension forms it')
NEXT_ACT = 'b723'


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
STANDING_DIR = 'tools/standing'         # ### the standing close toolset, versioned by tools/standing/VERSION, at v1.2.1 entering this act
STANDING_COMMIT = None                  # ### standing clauses v8, landed by a commit of its own at Component 6
ACT_CURRENT_COMMIT = '91cb997e13'       # ### data/act_current.json for b722 committed alone
STEPZERO = 'faf9dccddf'                 # ### b721's closing capture, committed alone ((R332)(11))
STEPZERO_STEPS = '86801b0fd8'           # ### b721's step-42 row, committed alone ((R332)(11))
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None
STEPZERO_REFUSALS = None
STEPZERO_BANKS = '39521b71f3'           # ### the step-zero banks and tools, committed together by explicit list
VISIBILITY_COMMIT = None
COMPUTE_TOOLS = ()
REPAIRED_TOOLS = ()
REPAIRED_DATA = ()
# ### b721's trap (event 11): the standing part of the sealed list read from the directory, not a carried tuple
STANDING_FILES = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing')) if f == 'VERSION' or f.endswith('.py')))
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset, sealed by hash beside the act's tools
STANDING_VERSION = 'v1.2.2'             # ### v1.2.2 landed at Component 1 ((R332)(2)), relay 99b0388d
STANDING_CHANGED = ('VERSION',)         # ### the standing files (R332)(2)'s three repairs change
STANDING_NEW = ('readfirst.py', 'sealcheck.py', 'used.py', 'v122.py')
# ### b721's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = '30c0b3c8'    # ### b721's closing, the act's relay base
B714_RECORD = '74dc741f'     # ### b721's record commit (relay, the last before the closing)
B714_ROOT = 'c6e2079dbe1c904f470c13d63da91ce79f2fb2eef176b29573308aa7334ad8aa'   # ### b721's root, data/act_roots.txt :99
# ### stage two (Component 8, before the lock): the commits of the components, read from the logs after each was made
C1_RELAY = '99b0388d4f'
C1_PP = 'cbb3b47f16'
WEIGHT_LINE, CORR_LINE = 11216, 11218
DIFFERS_LINE = None
ERRATA_LINE = None
C2_REG = None
C2_SELECT = None
C2_HALT = None
C2_PICKER = None
C2_PRED = None
C2_CTL = None
C2_RELAY = None
C3_RULE = None
C3_RELAY = None
C3_PREDICT_TOOL = None
C4_REG = None
C4_PP = None
C4_PRED = None
C4_RELAY = None
C5_REG = None
C5_RELAY = None
C6_FROZEN = None
C6_DRAFTS = None
C6_CENSUS = None
C6_REBUILD_5 = None
C6_RELAY = None
C6_PP = None
C6_PP_REPAIR = None
C7_PP = None
NEW_DISCRIMINANTS = (-31, -55)   # ### (R332)(3): computed under e8c3dff4
WALK_DISCRIMINANTS = (-24, -51, -52, -88, -91, -115, -123, -148, -187, -232, -235, -267, -403, -427)   # ### (R332)(4), under H-C2-WALK
WALK_CONTROL = -15
H34_DISCRIMINANTS = (-31, -55)
CHALLENGE_BRANCH = 'challenge-b720-h2-sign-iff-rh'   # ### b720's, on SIDE-explicit-formula, standing, not merged, no tag
CHALLENGE_TIP = '3391647518cd37316a448b5013afb62a198fa6c6'
CHALLENGE_RUN = 40651875792
PIN_RUNS = (('SIDE-grh-transfer', 40652622018), ('SIDE-interfaces', 40652657325), ('SIDE-kernel', 40652692787),
            ('SIDE-lv-conservation', 40652727943), ('SIDE-simplicity', 40652762827), ('SIDE-trivium', 40652790458))   # ### b720's, read not re-run
PIN_BRANCH = 'pin-b718-de5ce8a9'   # ### b718's pin branches, left as banked ((R332)(11))
PIN_EXCLUDED = ('SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve', 'SIDE-cosmo')
PIN_HELD = ('SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium')
PIN_BUILDS = ('SIDE-simplicity',)
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PIN_TO_NEXT = ()
MAX_DISPATCHES = 0           # ### N1: nothing dispatched this act
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md', INSTRUMENTS)
ERRATA_ID = None
ERRATA_IDS = ()
RETIRED_COUNT = 0            # ### no arm retired this act; the run list 116, 117 once (R332)(7) adds its arm
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b722_') and f.endswith('.py') and f != 'b722_report.py')) + NEW_TOOLS + COMPUTE_TOOLS
# ### the act's arms over its own banks: set at Component 8 by the Edit tool, as `b722_record.py armnames` prints them beyond the standing
ACT_ARMS = ()
