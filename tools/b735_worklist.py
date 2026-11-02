# -*- coding: utf-8 -*-
"""b735_worklist.py -- THE ACT'S DATA, UNDER (R345). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b735: LANE TWO, ACT ONE HUNDRED AND SIXTY-TWO, THE BUILD ACT -- b734 AT ITS WEIGHT; THE CORRIGENDUM OPENING ON THE CONTROLS THAT DID NOT COMPILE; THE explicitFormula FIELD
### BUILT ON THE FRESH ROUTE ON zq-b730, STOPPABLE AT THE PLAN'S FIVE BREAK POINTS, GRADED. At most sixteen dispatches (N1).
### Carried by diff from b734_worklist.py (data/b735_carry_worklist.txt); its stage one set by the Edit tool at step zero with this act's
### figures (the carried text named b734's objects under b735's names); later stages by the Edit tool.
### The act runs in b734's session (7c29db99), one seat.
### b734 closed and pushed itself whole (relay 5609d5fd, PLACE-papers 509fe00); its closing capture and step-30 row are this act's carried
### files ((R345)(2)), each committed alone at step zero.
### ANCHOR is the act's capture anchor (data/act_current.json, the ruling's first line); RULING_ANCHOR the same line, the citation tool's
### ferry source.
"""
import io
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '509fe0022bfbb0fbaa13c991ccd3ce94b3b3170c'    # ### PLACE-papers main before the act's own commits: b734's record
PRE_RELAY = '5609d5fd75eb5c49f2bb8e7bb9bd60c8af089838'  # ### relay main before the act's own commits: b734's closing
PRE_PP_REMOTE_AT_START = '509fe002'      # ### PLACE-papers remote main at the act's start (data/act_current.json, equal to local)
PRE_RELAY_REMOTE_AT_START = '5609d5fd'   # ### relay remote main at the act's start (the citation check's remote main row)
B718_RELAY_HEAD = '5609d5f'  # ### the names kept for the carried readers: the previous act's last relay head (b734's closing)
B718_PP_HEAD = '509fe00'     # ### the previous act's last PLACE-papers head (b734's record)
DATE = '2026-11-02'
SESSION_ID = '7c29db99-62df-4f5e-a436-7e99b58f5dbf'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R345) BEGIN'           # ### the act's capture anchor, as data/act_current.json
RULING_ANCHOR = 'RULING (R345) BEGIN'    # ### the ruling's BEGIN line, the citation tool's ferry source
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = '7c29db99-62df-4f5e-a436-7e99b58f5dbf'   # ### b734 ran in this session (from 'RULING (R344) BEGIN')
PREV_ANCHOR = 'RULING (R344) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b735_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 12751          # ### FINDINGS: b734's entry head (PLACE-papers 8c65149)
B711_WEIGHT = 12684         # ### FINDINGS: b733's weight line (b734's Component 1)
B711_CORRIGENDUM = 12686    # ### FINDINGS: b734's corrigendum for b733
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 17225          # ### OPEN_TRAILS: b734's trail record (PLACE-papers 509fe00)
B711_FACE = 'data/b734_registration_2026-11-02.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-11-02-b734.zip'   # ### b734's export, built after b734's last PLACE-papers push, CLEAN 3/3
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
ORDER_LEDGER_SPLIT = 14680  # ### OPEN_TRAILS: W-ORD-LEDGER-SPLIT-RESOLVER (b680), (R345)(3)
TRAIL_ORDERS = 17235        # ### OPEN_TRAILS: the last open-orders line, b734's, written from the generator's output
TRAIL_RESOLVED = 17275      # ### OPEN_TRAILS: b734's items for the author's strike, in its trail
TRAIL_RETIRED = 17251       # ### OPEN_TRAILS: b734's count line of the author's answers
WATCH_LINE = 16126          # ### OPEN_TRAILS: W-ORD-QUASI-RH-FIELD-WATCH, annotated at b718's C6
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row
INSTRUMENTS = 'phase1.5/method/INSTRUMENTS.md'   # ### PLACE-papers' instruments document, its last entry I-108 (b734)
INSTRUMENTS_LAST = 108

# ### the branches step zero deletes ((R345)(5)): the push-b734-* branches b734's close made, by name, each read from the listings and
# ### `--merged` printed before the deletes, one per command, each its own message
DELETE = (('D:/relay', ('push-b734-closing', 'push-b734-preroot', 'push-b734-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b734-preroot', 'push-b734-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R345)(8): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'), ('D:/SIDE-explicit-formula', 'challenge-b720-h2-sign-iff-rh'),
                 ('D:/SIDE-lv-conservation', 'scratch-b724'), ('D:/SIDE-explicit-formula', 'keiper-b725'), ('D:/SIDE-explicit-formula', 'c2-b725'),
                 ('D:/SIDE-kernel', 'rebuild-b721'), ('D:/SIDE-lv-conservation', 'rebuild-b721'), ('D:/SIDE-archimedean', 'rebuild-b721'),
                 ('D:/SIDE-frobenius', 'rebuild-b721'), ('D:/SIDE-spinor', 'rebuild-b721'), ('D:/SIDE-rcurve', 'rebuild-b721'))

# ### the kernels: read; written only on the rebuild-b721 branches by (R345)(7) and the author's word (4)
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')


def _kernel_paths():
    """the kernels of data/b716_federation_pin_price.txt (1), as D:/<name>, read at import ((R345) PATHS)."""
    p = os.path.join(D, 'b716_federation_pin_price.txt')
    t = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return tuple('D:/' + m.group(1) for m in re.finditer(r'(?m)^  (SIDE-[A-Za-z0-9-]+)\s+HEAD ', t))


KERNEL_PATHS = _kernel_paths()
PATHS = ('D:/relay', PP, KERNEL_DIR, LV_DIR) + tuple(k for k in KERNEL_PATHS if k not in (KERNEL_DIR, LV_DIR))   # ### (R345)'s PATHS
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, untouched (N5)
LV_MAIN = '305a87c9e09c45cc8a935b1065f26f929634c707'    # ### SIDE-lv-conservation's main at the sitting's [41] (README.md alone, (R345)(3))
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
# ### the wave 1 kernels at their own pins, (name, tag, the short commit) -- b721's (R331)(7), b734's (R344)(10)
WAVE1 = (('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-archimedean', 'v0.1.0', '8019d9d'),
         ('SIDE-frobenius', 'v0.1.0', '2efe9f2'), ('SIDE-spinor', 'v0.1.0', 'b235bc6'), ('SIDE-rcurve', 'v0.1.0', 'd5f33b4'))
CHECKPOINT_STATEMENTS = (('SIDE-archimedean', 'archimedean_forces_half'), ('SIDE-frobenius', 'indicial_forces_half'),
                         ('SIDE-spinor', 'spinor_forces_half'), ('SIDE-spinor', 'half_iff_centered_zero'), ('SIDE-rcurve', 'monotone_unique_zero'))
REBUILD_BRANCH = 'rebuild-b721'          # ### b721's branches, kept, (R345)(7)'s repair made on them alone
REBUILD_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-lv-conservation', 40706311269), ('SIDE-archimedean', 40706397470),
                ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404), ('SIDE-frobenius', 40713201832))   # ### b721's, each read by its id
AXIOM_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-archimedean', 40706397470), ('SIDE-frobenius', 40713201832),
              ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404))   # ### b734's (R344)(10): the five whose axiom step was diagnosed
AXIOM_DIAG = 'data/b729_axiom_diag.txt'  # ### the routes (R345)(7) and the author's word (4) take
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
DATA_STANDING = 'data/standing_clauses_v9.txt'   # ### v8 bound the act to d9739558; v9 from that commit, which landed it at Component 1 ((R345)(2)(v))
DATA_STANDING_V9 = 'data/standing_clauses_v9.txt'
ARM_TAGS = 'data/arm_tags.json'
REPO_VISIBILITY = 'data/repo_visibility.txt'
REGISTRATIONS = 'data/b734_explicitformula_plan.txt'    # ### (R345)(3), N2: the plan bank as committed at b734, its md5 printed before any Lean file
REG_WALK_COMMIT = '15cb6cc4'                     # ### b721's H-C2-WALK commit (carried name; b734's walk read under it)
REG_COMMITS = (('data/b716_registrations.txt', 'dc5e808f'), ('data/b718_registrations.txt', '8146404b577dfee3e379d19e08e8595ab8824961'),
               ('data/b719_registrations.txt', '965cb8e84dc02192854512af53a29b1fbc2b80f5'), ('data/b720_registrations.txt', '54fc03d9'),
               ('data/b721_registrations.txt', 'e8c3dff40df43269b3f0c4b917baef7c96c0f649'),
               ('data/b725_registrations.txt', 'dc0d4133'))   # ### N2 (b725's row, its last amendment, the blob HEAD carries)
FIT_COMMIT, PRED_COMMIT = None, None
ONSET_COMMIT = None
REG_FILES = tuple(f for f, _c in REG_COMMITS)
PRED_B717 = 'data/b717_predictions.txt'
PRED_B717_COMMIT = 'f47d8ab5840d287bf63c1f0b59ba707ed85dbe07'
PREDICTIONS = PRED_B717
ONSETS_B717 = 'data/b717_onsets.txt'
REGISTRATIONS_NEW = 'data/b725_registrations.txt'
COEFF_BANKS = ('data/b711_coeffs.txt', 'data/b713_coeffs.txt', 'data/b717_coeffs.txt', 'data/b719_coeffs.txt', 'data/b720_coeffs.txt')
#   ### read not written (carried name); b734 wrote no coefficient bank
COMPUTE_BANKS = ('data/b735_standing_v1150.txt', 'data/b735_explicitformula.txt', 'data/b735_address_scan.txt')
#   ### the banks of (R345)(2)-(3), each written by its component
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt',
              'data/b729_read_calls.txt', 'data/b730_read_calls.txt', 'data/b734_read_calls.txt', 'data/b735_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b734 carried them
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b735'))
CHAIN_QUARTERS = (('b624', 'b631'), ('b632', 'b658'))   # ### (R345)(2)(vi): b2a split where b734's banked walks halve (repeat.quarters; b2a's run 575 s at b734)
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### set by the Edit tool when a component adds a standing arm
SHARED_APPENDED = ('data/b675_corrigenda.txt',)   # ### (R345)(2): the corrigenda row
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md')   # ### the ledgers alone (N5, the (W) list of (R345)(9))
PP_WRITTEN = PP_EDITED
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the re-cut's merge (kept for the kernel rows); the MANIFEST control's reference
#   ### is the commit the mirror is built at from v1.2.1
NEXT = ('per (R345)(6): the act after the build closes is the second sitting, data/b732_phase2_frontdoors.txt its agenda by (R337)’s form; if the build stops at a break point, b736 continues it on the same plan')
NEXT_ACT = 'b736'


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
STANDING_DIR = 'tools/standing'         # ### the standing close toolset, versioned by tools/standing/VERSION, at v1.5.0 entering this act
STANDING_COMMIT = 'd973955897'          # ### standing clauses v9 (b723's Component 1), binding this act whole (carried name)
ACT_CURRENT_COMMIT = 'e317a258'         # ### data/act_current.json for b735 committed alone, before any other write ((R345)(4))
STEPZERO = '284c87f1'             # ### b734's closing capture, committed alone ((R345)(2))
STEPZERO_STEPS = '45866be1'       # ### b734's step-30 row, committed alone ((R345)(2))
STEPZERO_TABLE = None             # ### the terminal table regenerated and committed ((R345)(8))
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None
STEPZERO_REFUSALS = ()
STEPZERO_BANKS = '556868c3'
STEPZERO_BANK_COMMIT = '556868c3'
VISIBILITY_COMMIT = None
COMPUTE_TOOLS = ()                      # ### set by the Edit tool when a component seals a compute tool
REPAIRED_TOOLS = tuple(p[len('tools/'):] for p in json.load(io.open(os.path.join(D, 'act_current.json'), encoding='utf-8'))['shared_edits'])
#   ### (R345)(2), b734 event (2): read from data/act_current.json, the one hand list, which G-ACT-CURRENT reads against git; sealed before the suite runs (b696's form)
REPAIRED_DATA = ()
# ### b721's trap (event 11): the standing part of the sealed list read from the directory, not a carried tuple
STANDING_FILES = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing')) if f == 'VERSION' or f.endswith('.py')))
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset, sealed by hash beside the act's tools
# ### the seven close tools are tools/standing/fold.py's renders of its templates (tools/standing/fold/<tool>.tpl) with the act's arms module
# ### (tools/acts/b735.py) -- every byte a render reads sealed beside the act's tools; report.tpl left out of the seal (b708's report row)
FOLD_FILES = tuple(sorted('standing/fold/' + f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing', 'fold')) if f.endswith('.tpl')
                          and f != 'report.tpl')) + ('acts/b735.py',)
NEW_TOOLS = NEW_TOOLS + FOLD_FILES
STANDING_VERSION = 'v1.15.0'            # ### entering at v1.14.0; (R345)(2)'s repairs landed this version by a commit of their own (C1_STANDING)
LEAN_TREES = (('D:/SIDE-explicit-formula', '09053d3b'),)   # ### (R345)(3): the tree the ruling's Lean paths are read against, zq-b730's tip
STANDING_CHANGED = ('standing/VERSION', 'standing/actmodule.py', 'standing/allow.py', 'standing/fold.py', 'standing/fold/checks.tpl')
STANDING_NEW = ('standing/compilecontrol.py', 'standing/counterline.py', 'standing/deletes.py', 'standing/repaircommits.py', 'standing/v1150.py')
# ### b734's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = '5609d5fd'    # ### b734's closing, the act's relay base
B714_RECORD = 'd768ca35'     # ### b734's record commit (relay, the head line's)
B714_ROOT = '30fc573f3862c3f6cf3d9af1ba832252d1027e69b4496f4a47b2776b4146a1cb'   # ### b734's root, data/act_roots.txt's last row
B723_ROOT_BANKS = 'efb643c7'  # ### b734's root commit, the banks its root rode with
# ### later stages: the commits of the components, read from the logs after each was made (None until made)
C1_STANDING = 'deac7a43'
C1_STANDING_REPAIR = None
C1_RELAY = 'f479a7fe'
C1_CORR = 'f479a7fe'     # ### the corrigendum's banks rode with the record lines' commit
C1_PP = '71795853'
WEIGHT_LINE, CORR_LINE = 12791, 12793
DIFFERS_LINE = None
ERRATA_LINE = None
C2_RELAY = None
DOORS_COMMIT = None
MECH_COMMIT = None
FRONTDOORS_COMMIT = None
COUNT_BANK = None
PRINT_COMMIT = '39b4eecb'    # ### the name the carried arms read: the build's bank at this act
PLAN_MD5 = '5d3868f41eb7aa5be5fa4f7ab57e8df7'   # ### (R345)(3): data/b734_explicitformula_plan.txt as committed at de03cb85
C2_AMEND = ()
C2_PP = C1_PP            # ### (R345)(5): (2) whole before (3); b735 enters no order, the corrigendum's commit stands first in N2's chain
C3_RELAY = ()
C3_PP = None
C4_LV = None
C4_RUN = None
C4_PP = None
C4_RELAY = None
C5_RELAY = None
REG_COMMIT = 'de03cb85'    # ### the plan bank's last commit, its row (R345)(4)'s
ZEROS_REG_COMMIT = REG_COMMIT
ORDERS = (142, 60, 42, 12, 28)          # ### b734's (R344)(4) triage, carried as read (data/b729_orders_triage.txt): DONE, NOT MET, MET, AUTHOR'S WORD
TRIAGE = 'data/b729_orders_triage.txt'
LV_SCRATCH_BRANCH = 'scratch-b724'      # ### b724's scratch branch of SIDE-lv-conservation, kept ((R345)(8))
LV_RUNS = (('SIDE-lv-conservation', 40964150574),)   # ### b734's one dispatch, read by its id (carried, not re-run)
LV_ROWS = 'data/b735_lv_rows.json'
CHALLENGE_BRANCH = 'challenge-b720-h2-sign-iff-rh'   # ### b720's, on SIDE-explicit-formula, standing, not merged, no tag
CHALLENGE_TIP = '3391647518cd37316a448b5013afb62a198fa6c6'
CHALLENGE_RUN = 40651875792
PIN_RUNS = (('SIDE-grh-transfer', 40652622018), ('SIDE-interfaces', 40652657325), ('SIDE-kernel', 40652692787),
            ('SIDE-lv-conservation', 40652727943), ('SIDE-simplicity', 40652762827), ('SIDE-trivium', 40652790458))   # ### b720's, read not re-run
PIN_BRANCH = 'pin-b718-de5ce8a9'   # ### b718's pin branches, left as banked ((R345)(8))
PIN_EXCLUDED = ('SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve', 'SIDE-cosmo')
PIN_HELD = ('SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium')
PIN_BUILDS = ('SIDE-simplicity',)
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PIN_TO_NEXT = ()
MAX_DISPATCHES = 16        # ### N1: (R345)(3)'s sixteen at most
MAX_C2, MAX_KEIPER = 0, 0
EF_DIR = 'D:/SIDE-explicit-formula'
EF_BASE = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'   # ### SIDE-explicit-formula's main, every branch cut from it, untouched (N5)
ZQ_BRANCH = 'zq-b730'
ZQ_ENTERING = '09053d3b07367aa7ef2e26cbeb27fd35d8734d82'   # ### b733's tip, unmoved by b734; the build lands on zq-b730
ZQ_FIRST = 'd0f63854'   # ### the first Lean commit of the build, group A's
ZQ_TIP = 'b25fd82c0f216505d67c4c72c70f6e1b3f307d03'    # ### the build's landed tip, dispatch 11's ref
ZQ_MODULES = ('Xi', 'Landau', 'Heights', 'Contour', 'ZeroSum', 'FullLine', 'Lines', 'Main')   # ### the build's eight, under Schema/ZQ/EF
ZQ_FILES = tuple('SIDEExplicitFormula/Schema/ZQ/EF/%s.lean' % m for m in ZQ_MODULES) + ('print_targets.txt',)   # ### zq-b730's diff against its entering tip
ZQ_MODULES_B730 = ('Lattice', 'Theta', 'FEPair', 'Continuation')   # ### the names the carried sections read, until each section is set for this act
ZQ_ZEROS_FIRST, ZQ_LOGDERIV_TIP = None, None
ZQ_LOGDERIV_MODULES, ZQ_ZEROS_MODULES = (), ()
MAX_LOGDERIV, MAX_ZEROS = 0, 0
EF_BRANCHES = (('keiper-b725', '01fd33c2d7dc62d4702b075de3dda9253c5c2f87'),   # ### (R345)(4): the gamma_1 bound
               ('c2-b725', '0395f15d3b2906716ccb1f09ca24171d7a921210'),       # ### (R345)(3): the theorem, built whole at this tip
               ('detect-b729', '1023301c89ab16f8d437b2a1f08a824bc95b6b0e'),   # ### b729's (R339)(5): the statement alone, not compiled; kept, unmoved
               (ZQ_BRANCH, ZQ_TIP))                                           # ### (R345)(3)-(4): the fields
EF_BRANCHES_ENTERING = ('01fd33c2d7dc62d4702b075de3dda9253c5c2f87', '0395f15d3b2906716ccb1f09ca24171d7a921210', '1023301c89ab16f8d437b2a1f08a824bc95b6b0e', ZQ_ENTERING)   # ### the four entering the act
EF_RUNS = tuple(('build-module', r['run'], r['sha'], r['target']) for r in json.load(open(os.path.join(ROOT, 'data', 'b735_dispatch_rows.json'), encoding='utf-8')) if r['kind'] == 'dispatch')   # ### N1: (kind, run id, ref, target), (R345)(3)'s eleven, read from the rows and not typed
EF_RUNS_B731 = (41371666217, 41372597450, 41373409167, 41374121055, 41374814817)   # ### b734's five, read not re-run
DISPATCH_ROWS = 'data/b735_dispatch_rows.json'
ERRATA_ID = None   # ### (R345) orders no ERRATA entry
ERRATA_IDS = ()
RETIRED_COUNT = 0
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list (the root answer's addition (b))
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b735_') and f.endswith('.py') and f != 'b735_report.py')) + NEW_TOOLS + COMPUTE_TOOLS + REPAIRED_TOOLS
# ### the act's arms over its own banks: set before the lock by the Edit tool -- b734's list, the act shift G-R344-ENTERED to G-R345-ENTERED,
# ### G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0 ((R345)(2)(iv))
ACT_ARMS = ('G-ACT-CURRENT', 'G-ARM-TAGS', 'G-ARMS-RETIRED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED', 'G-CLOSING-DRY-STEP', 'G-COEFFS-LAW',
            'G-CORRIGENDUM-ENTERED', 'G-COUNT-ROUTE-PRICED', 'G-DELETES-ONE-BRANCH', 'G-DERIVATION-GRADED', 'G-DIFFERS-ERRATA', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-GUARD-HELD', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LISTINGS-BEFORE-CLAUSES',
            'G-MEMBRANE-WIRED', 'G-OFFSET-POST-HOC', 'G-POSTROOT-WRITES-NONE', 'G-PREDICTION-FIRST', 'G-R345-ENTERED',
            'G-REGISTRATIONS-FIRST', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED', 'G-SURGERY-CARRIED', 'G-TOUCH-READ',
            'G-WRITELIST-MIRROR-STATE')

# ### the three kernels' README writes (name, path, head before the write), their tips (carried names, b734's sitting's)
SITTING_REPOS = ()     # ### b735 writes no kernel's main (N5): no sitting
SITTING_TIPS = {}
