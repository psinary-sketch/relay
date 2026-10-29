# -*- coding: utf-8 -*-
"""b723_worklist.py -- THE ACT'S DATA, UNDER (R333). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b723: LANE TWO, ACT ONE HUNDRED AND FIFTY, THE CHECKPOINT ACT -- b722 AT ITS WEIGHT; THE CORRIGENDUM AND THE REPEAT CLASSES REPAIRED
### (tools/standing/ v1.3.0); THE OPEN ORDERS GENERATED AND THE TWENTY READ; H-SUPPORT, H-ZETAK AND H-DIAL REGISTERED, THEN COMPUTED; THE C2
### CLOSED FORM; WAVE 1'S AXIOM STEP; THE LEDGER SPLIT, STOPPABLE. The runner dispatches are (R333)(7)'s alone, six at most (N1).
### Carried by diff from b722_worklist.py (data/b723_carry_worklist.txt) and its stage one rewritten whole by the Write tool with this act's
### objects at step zero (the carried text named b722's objects under b723's names, the rebuild branches among them); later stages by the
### Edit tool, until (R333)(2)(i) folds the close tools into tools/standing/ v1.3.0.
### The act runs in the SAME session as b722 (02c7cf38; the ruling pasted during b722's close, the act opened by the author's word "Go: b723"
### after b722's closing push): the previous act's window is this session cut at b722's anchor, b706's same-session form. b722 closed and
### pushed itself whole (relay 1607e994, PLACE-papers 1553808a, both read back); its closing capture and step-37 row are this act's carried
### files ((R333)(9)), and the two hook-refusal banks the author's word (1) orders committed.
### ANCHOR is the act's capture anchor (data/act_current.json, the first line of the author's word); RULING_ANCHOR is the ruling's own BEGIN
### line, which the citation tool reads the ferry from (the ruling pasted before the act opened).
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '1553808a9278e28e2e819e4f39008bd3df37d54b'    # ### PLACE-papers main before the act's own commits: b722's record, pushed and read back by b722
PRE_RELAY = '1607e994dd6c98250428d8197665bf440950e5ca'  # ### relay main before the act's own commits: b722's closing, pushed and read back by b722
PRE_PP_REMOTE_AT_START = '1553808a'      # ### PLACE-papers remote main at the act's start (read at step zero, equal to local)
PRE_RELAY_REMOTE_AT_START = '1607e994'   # ### relay remote main at the act's start (read at step zero, equal to local)
B718_RELAY_HEAD = '1607e99'  # ### the names kept for the carried readers: the previous act's last relay head (b722's closing)
B718_PP_HEAD = '1553808'     # ### the previous act's last PLACE-papers head (b722's record)
DATE = '2026-10-29'
SESSION_ID = '02c7cf38-4c6a-4f88-b813-a7e15e9b85b4'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'Go: b723'                      # ### the act's capture anchor, as data/act_current.json (the author's word (1))
RULING_ANCHOR = 'RULING (R333) BEGIN'    # ### the ruling's BEGIN line, the citation tool's ferry source
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = SESSION_ID   # ### b722 ran in this session (from 'RULING (R332) BEGIN', with compactions); b706's same-session form
PREV_ANCHOR = 'RULING (R332) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b723_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 11359          # ### FINDINGS: b722's entry head (PLACE-papers 1553808a)
B711_WEIGHT = 11216         # ### FINDINGS: b721's weight line (b722's Component 1)
B711_CORRIGENDUM = 11218    # ### FINDINGS: b722's corrigendum for b721
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 16310          # ### OPEN_TRAILS: b722's trail record (PLACE-papers 1553808a)
B711_FACE = 'data/b722_registration_2026-10-28.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-28-b722.zip'   # ### b722's export, built after b722's last PLACE-papers push, 74 files, CLEAN
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
ORDER_LEDGER_SPLIT = 14680  # ### OPEN_TRAILS: W-ORD-LEDGER-SPLIT-RESOLVER (b680), (R333)(8)
TRAIL_ORDERS = 16250        # ### OPEN_TRAILS: the last open-orders line (its ten, (R333)(3)(i)'s control)
TRAIL_RESOLVED = 16350      # ### OPEN_TRAILS: b722's items for the author's strike, in its trail (landed at 1553808a)
WATCH_LINE = 16126          # ### OPEN_TRAILS: W-ORD-QUASI-RH-FIELD-WATCH, annotated at b718's C6
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row
INSTRUMENTS = 'phase1.5/method/INSTRUMENTS.md'   # ### PLACE-papers' instruments document, its last entry I-108 (b722)
INSTRUMENTS_LAST = 108

# ### the branches step zero deletes ((R333)(9)): the push-b722-* branches b722's close made, by name, each read from the listings and
# ### `--merged` printed before the deletes, one per command, each its own message
DELETE = (('D:/relay', ('push-b722-closing', 'push-b722-preroot', 'push-b722-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b722-preroot', 'push-b722-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R333)(9): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'), ('D:/SIDE-explicit-formula', 'challenge-b720-h2-sign-iff-rh'),
                 ('D:/SIDE-kernel', 'rebuild-b721'), ('D:/SIDE-lv-conservation', 'rebuild-b721'), ('D:/SIDE-archimedean', 'rebuild-b721'),
                 ('D:/SIDE-frobenius', 'rebuild-b721'), ('D:/SIDE-spinor', 'rebuild-b721'), ('D:/SIDE-rcurve', 'rebuild-b721'))

# ### the kernels: read; written only on the rebuild-b721 branches by (R333)(7) and the author's word (4)
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')


def _kernel_paths():
    """the kernels of data/b716_federation_pin_price.txt (1), as D:/<name>, read at import ((R333) PATHS)."""
    p = os.path.join(D, 'b716_federation_pin_price.txt')
    t = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return tuple('D:/' + m.group(1) for m in re.finditer(r'(?m)^  (SIDE-[A-Za-z0-9-]+)\s+HEAD ', t))


KERNEL_PATHS = _kernel_paths()
PATHS = ('D:/relay', PP, KERNEL_DIR, LV_DIR) + tuple(k for k in KERNEL_PATHS if k not in (KERNEL_DIR, LV_DIR))   # ### (R333)'s PATHS
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
# ### the wave 1 kernels at their own pins, (name, tag, the short commit) -- b721's (R331)(7), b722's (R332)(10)
WAVE1 = (('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-archimedean', 'v0.1.0', '8019d9d'),
         ('SIDE-frobenius', 'v0.1.0', '2efe9f2'), ('SIDE-spinor', 'v0.1.0', 'b235bc6'), ('SIDE-rcurve', 'v0.1.0', 'd5f33b4'))
CHECKPOINT_STATEMENTS = (('SIDE-archimedean', 'archimedean_forces_half'), ('SIDE-frobenius', 'indicial_forces_half'),
                         ('SIDE-spinor', 'spinor_forces_half'), ('SIDE-spinor', 'half_iff_centered_zero'), ('SIDE-rcurve', 'monotone_unique_zero'))
REBUILD_BRANCH = 'rebuild-b721'          # ### b721's branches, kept, (R333)(7)'s repair made on them alone
REBUILD_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-lv-conservation', 40706311269), ('SIDE-archimedean', 40706397470),
                ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404), ('SIDE-frobenius', 40713201832))   # ### b721's, each read by its id
AXIOM_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-archimedean', 40706397470), ('SIDE-frobenius', 40713201832),
              ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404))   # ### b722's (R332)(10): the five whose axiom step was diagnosed
AXIOM_DIAG = 'data/b722_axiom_diag.txt'  # ### the routes (R333)(7) and the author's word (4) take
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
DATA_STANDING_V8 = 'data/standing_clauses_v8.txt'
DATA_STANDING = 'data/standing_clauses_v9.txt'   # ### v8 bound the act to d9739558; v9 from that commit, which landed it at Component 1 ((R333)(2)(v))
DATA_STANDING_V9 = 'data/standing_clauses_v9.txt'
ARM_TAGS = 'data/arm_tags.json'
REPO_VISIBILITY = 'data/repo_visibility.txt'
REGISTRATIONS = 'data/b723_registrations.txt'    # ### (R333)(4): written and committed alone at Component 3, before any figure it names
REG_WALK_COMMIT = '15cb6cc4'                     # ### b721's H-C2-WALK commit (carried name; b722's walk read under it)
REG_COMMITS = (('data/b716_registrations.txt', 'dc5e808f'), ('data/b718_registrations.txt', '8146404b577dfee3e379d19e08e8595ab8824961'),
               ('data/b719_registrations.txt', '965cb8e84dc02192854512af53a29b1fbc2b80f5'), ('data/b720_registrations.txt', '54fc03d9'),
               ('data/b721_registrations.txt', 'e8c3dff40df43269b3f0c4b917baef7c96c0f649'))   # ### N2 (b723's row added at Component 3)
REG_FILES = tuple(f for f, _c in REG_COMMITS)
PRED_B717 = 'data/b717_predictions.txt'
PRED_B717_COMMIT = 'f47d8ab5840d287bf63c1f0b59ba707ed85dbe07'
PREDICTIONS = PRED_B717
ONSETS_B717 = 'data/b717_onsets.txt'
REGISTRATIONS_NEW = 'data/b723_registrations.txt'
COEFF_BANKS = ('data/b711_coeffs.txt', 'data/b713_coeffs.txt', 'data/b717_coeffs.txt', 'data/b719_coeffs.txt', 'data/b720_coeffs.txt',
               'data/b722_coeffs.txt')   # ### read not written; (R333)(6)'s check reads the class-number-2 rows of b711-b722
COMPUTE_BANKS = ('data/b723_orders.txt', 'data/b723_orders_twenty.txt', 'data/b723_support_rule.txt', 'data/b723_zetak.txt',
                 'data/b723_support.txt', 'data/b723_dial_price.txt', 'data/b723_c2_closed_form.txt', 'data/b723_c2_check.txt',
                 'data/b723_axiom.txt', 'data/b723_axiom_rows.json', 'data/b723_split_price.txt')   # ### the banks of (R333)(3)-(8), Component 7
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt',
              'data/b722_read_calls.txt', 'data/b723_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b722 carried them
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b723'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### set by the Edit tool when a component adds a standing arm
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md')   # ### the weight line, the corrigendum, the entry and the trail; (R333)(8)'s archive-3 files where it lands
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the re-cut's merge (kept for the kernel rows); the MANIFEST control's reference
#   ### is the commit the mirror is built at from v1.2.1
NEXT = ('b724 ((R333)(11)), the wave 1 act: the sign core`s paper drafted in paper mode, the front-door list assembled for the release sitting, '
        'and the support-face detection theorem with explicit constants named as the Lean target in place of the Li-face version; the C2 '
        'compile where the author names it from b722`s price; the surgery under H-SHAPE in an act of its own')
NEXT_ACT = 'b724'


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
STANDING_DIR = 'tools/standing'         # ### the standing close toolset, versioned by tools/standing/VERSION, at v1.2.2 entering this act
STANDING_COMMIT = 'd973955897'          # ### standing clauses v9, landed by a commit of its own at Component 1 ((R333)(2)(v))
ACT_CURRENT_COMMIT = '1e0500f9c6'       # ### data/act_current.json for b723 committed alone, before any other command (the author's word (1))
STEPZERO = 'a9d8b6626b'                 # ### b722's closing capture, committed alone ((R333)(9))
STEPZERO_STEPS = '945b75203d'           # ### b722's step-37 row, committed alone ((R333)(9))
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None
STEPZERO_REFUSALS = ('5bc549cef5', '29cb27b429')   # ### the two hook-refusal banks, each its own commit (the author's word (1)): b720's, b721's
STEPZERO_BANKS = '026335ad2a'           # ### the step-zero banks and tools, committed together by explicit list
VISIBILITY_COMMIT = None
COMPUTE_TOOLS = ('research/reproduce.py',)   # ### Component 1: its I-76 row edited this act (the inputs read at the bank's own time), sealed
REPAIRED_TOOLS = ()
REPAIRED_DATA = ()
# ### b721's trap (event 11): the standing part of the sealed list read from the directory, not a carried tuple
STANDING_FILES = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing')) if f == 'VERSION' or f.endswith('.py')))
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset, sealed by hash beside the act's tools
# ### Component 1, (R333)(2)(i) on the author's word (Option 2): the seven close tools are tools/standing/fold.py's renders of its templates
# ### (tools/standing/fold/<tool>.tpl) with the act's arms module (tools/acts/b723.py) -- every byte a render reads sealed beside the act's tools
# ### Component 7, before the lock: report.tpl left out of the seal -- the standing report tool is run unsealed before and after the root
# ### (b708's report row: "no report tool sealed", the suite's G-REPORT-UNSEALED); the act's report sections ride in acts/b723.py, sealed
FOLD_FILES = tuple(sorted('standing/fold/' + f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing', 'fold')) if f.endswith('.tpl')
                          and f != 'report.tpl')) + ('acts/b723.py',)
NEW_TOOLS = NEW_TOOLS + FOLD_FILES
STANDING_VERSION = 'v1.3.0'             # ### (R333)(2), landed at Component 1
STANDING_CHANGED = ('standing/close.py', 'standing/fold.py', 'standing/legacy.py', 'standing/peek.py', 'standing/v130.py', 'standing/VERSION') \
    + FOLD_FILES[:-1] \
    + ('standing/orders.py',)           # ### the standing files (R333)(2)'s repairs change or add; (R333)(3)(i)'s generator, Component 2
STANDING_NEW = ()
# ### b722's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = '1607e994'    # ### b722's closing, the act's relay base
B714_RECORD = '65430407'     # ### b722's record commit (relay, the last before the closing)
B714_ROOT = '0d26295f7b567e20fcf6c938b9e154fe6f1358cf7d9e401ac1f872b6b2182e20'   # ### b722's root, data/act_roots.txt :100
# ### later stages: the commits of the components, read from the logs after each was made
C1_RELAY = 'fac1cda8cb'   # ### b722 at its weight and the corrigendum for b722 (data/b723_corrigendum.txt), after v1.3.0 (be821907)
C1_PP = '763ae914f3'      # ### FINDINGS :11399 (the weight line) and :11401 (the corrigendum)
WEIGHT_LINE, CORR_LINE = 11399, 11401   # ### FINDINGS: b722's weight line and the corrigendum for b722 (tools/b723_c1.py, Component 1)
DIFFERS_LINE = None
ERRATA_LINE = None
# ### Component 7, before the lock, the Edit tool: the components' commits as the step bank rows them (data/b723_steps.json, steps 7-34)
C1_ADDR = 'd0ee06a86e'    # ### (R332)(9)'s scan with its second name arm (the author's word (1))
C1_V130 = 'be821907a6'    # ### tools/standing/ v1.3.0: the seven close tools folded (the author's word (2), Option 2), (iii), (iv), (b)
C1_I76 = '82e62fd75c'     # ### I-76 read at b544's pins, tools/research/reproduce.py's row edited (the root answer's (c))
C2_RELAY = '709ba3eb6c'   # ### tools/standing/orders.py, its rule printed before its output, its controls; the twenty read (data/b723_orders_twenty.txt)
C2_PP = '9e09854805'      # ### three closing lines on OPEN_TRAILS ((R333)(3)(ii))
C2_RULING = 'd9fbceb45e'  # ### the latest-status rule (the author's word (3))
C2_LOCATOR = '5f61725ee6'  # ### the locator reading tried (the author's word (4)(3)), broken by the record, the earlier rule standing
C2_WEED_PP = '70d9c0d0cd'  # ### OPEN_TRAILS' dated line, W-ORD-E1-CFG CLOSED (the author's word (5))
C2_REPRINT = '9c026ef706'  # ### the orders reprinted after the weed: controls 6 of 6 at 763ae914, at HEAD 193 / 143 / 50
REG_COMMIT = '9ad2642115'  # ### data/b723_registrations.txt committed alone ((R333)(4), N2)
C3_RULE_TOOL = 'f7ee91e604'  # ### H-SUPPORT's rule tool, computing no onset
C3_PRED = '0e91c670a1'    # ### H-SUPPORT's rule output and each a*_pred, by a commit of their own before any onset
C4_ZETAK = '23f54c746c'   # ### H-ZETAK: controls, then the two windows (data/b723_zetak.txt)
C4_ONSET_TOOL = '7f77844c0b'  # ### H-SUPPORT's onset tool, after its C1 and before any onset
C4_SUPPORT = '1530d2f252'  # ### H-SUPPORT's onsets (data/b723_support.txt)
C4_GRADES = 'ac75a51cef'  # ### the grade words in (R333)(5)'s vocabulary
C4_DIAL = 'ca2c6a9d28'    # ### H-DIAL's build priced, carried (data/b723_dial_price.txt)
C4_RULINGS = 'a8c4160e02'  # ### the author's word (4)(1)-(2): off52 beside the refutation, the five products POST HOC
C5_RELAY = 'cdc46c59a6'   # ### the C2 closed form written and checked POST HOC (data/b723_c2_closed_form.txt, data/b723_c2_check.txt)
C6_AXIOM = ('f26236c99e', '0e68a2d7e7', 'f81abaf9ca')   # ### the axiom step at 3, 5 and 6 of 6 pins; the split priced and carried in the second
C6_RELAY = 'f81abaf9ca'
REBUILD_COMMITS = (('SIDE-archimedean', '610cbdf91f'), ('SIDE-rcurve', 'f3a5ae5486'), ('SIDE-spinor', '526727ef7a'),
                   ('SIDE-frobenius', 'b4ef3958cd'), ('SIDE-kernel', 'c683fcd7f4'))   # ### (R333)(7): one commit each on rebuild-b721
B723_RUNS = (('SIDE-archimedean', 40881801296), ('SIDE-rcurve', 40881833590), ('SIDE-spinor', 40885978813),
             ('SIDE-frobenius', 40885967139), ('SIDE-kernel', 40887008505))   # ### five runs, each read by its id (N1: six at most)
ORDERS = (193, 143, 50)   # ### the generator at HEAD after the weed (data/b723_orders.txt :282)
TWENTY = 'data/b723_orders_twenty.txt'
NEW_DISCRIMINANTS = (-31, -55)   # ### b722's, read by the carried arms (b722 computed them under e8c3dff4)
WALK_DISCRIMINANTS = (-24, -51, -52, -88, -91, -115, -123, -148, -187, -232, -235, -267, -403, -427)   # ### b722's fourteen, under H-C2-WALK
WALK_CONTROL = -15
H34_DISCRIMINANTS = (-31, -55)
CHALLENGE_BRANCH = 'challenge-b720-h2-sign-iff-rh'   # ### b720's, on SIDE-explicit-formula, standing, not merged, no tag
CHALLENGE_TIP = '3391647518cd37316a448b5013afb62a198fa6c6'
CHALLENGE_RUN = 40651875792
PIN_RUNS = (('SIDE-grh-transfer', 40652622018), ('SIDE-interfaces', 40652657325), ('SIDE-kernel', 40652692787),
            ('SIDE-lv-conservation', 40652727943), ('SIDE-simplicity', 40652762827), ('SIDE-trivium', 40652790458))   # ### b720's, read not re-run
PIN_BRANCH = 'pin-b718-de5ce8a9'   # ### b718's pin branches, left as banked ((R333)(9))
PIN_EXCLUDED = ('SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve', 'SIDE-cosmo')
PIN_HELD = ('SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium')
PIN_BUILDS = ('SIDE-simplicity',)
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PIN_TO_NEXT = ()
MAX_DISPATCHES = 6           # ### N1: (R333)(7)'s, one per kernel, six at most
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md')
ERRATA_ID = None
ERRATA_IDS = ()
RETIRED_COUNT = 0            # ### tools/standing/arms.py RETIRED unchanged; (R333)(2)(iv)'s G-READFIRST-DIFF-BANKED left the arm list itself at v1.3.0 (be821907), the run list 116
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list (the root answer's addition (b))
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b723_') and f.endswith('.py') and f != 'b723_report.py')) + NEW_TOOLS + COMPUTE_TOOLS
# ### the act's arms over its own banks: set before the lock by the Edit tool -- b722's list, the act shift G-R332-ENTERED to G-R333-ENTERED,
# ### G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0 ((R333)(2)(iv))
ACT_ARMS = ('G-ACT-CURRENT', 'G-ARM-TAGS', 'G-ARMS-RETIRED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED', 'G-CLOSING-DRY-STEP', 'G-COEFFS-LAW',
            'G-CORRIGENDUM-ENTERED', 'G-COUNT-ROUTE-PRICED', 'G-DELETES-ONE-BRANCH', 'G-DERIVATION-GRADED', 'G-DIFFERS-ERRATA', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-GUARD-HELD', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LISTINGS-BEFORE-CLAUSES',
            'G-MEMBRANE-WIRED', 'G-OFFSET-POST-HOC', 'G-POSTROOT-WRITES-NONE', 'G-PREDICTION-FIRST', 'G-R333-ENTERED',
            'G-REGISTRATIONS-FIRST', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED', 'G-SURGERY-CARRIED', 'G-TOUCH-READ',
            'G-WRITELIST-MIRROR-STATE')
