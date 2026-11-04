# -*- coding: utf-8 -*-
"""b740_worklist.py -- THE ACT'S DATA, UNDER (R350). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b740: LANE TWO, ACT ONE HUNDRED AND SIXTY-SEVEN, THE NUMERICS ACT -- b739 AT ITS WEIGHT; THE CORRIGENDUM OPENING ON THE ARM THAT
### COULD NOT PASS; S5c AND S5d STATED, THEN BUILT IN SIDE-explicit-formula'S TREE ON zq-b730 AT THE CENTRE OF BOX A TO SP3. At most
### twelve dispatches (N1).
### Carried by diff from b739_worklist.py (data/b740_carry_worklist.txt); its stage one set by the Edit tool at step zero with this act's
### figures (the carried text named b739's objects under b740's names), the build's constants from b738's worklist; later stages by the Edit tool.
### The act runs in a new session (352ad3f4), one seat; b739 ran in c6c3fbf2.
### b739 closed and pushed itself whole (relay c961e9d7, PLACE-papers 5b89b86); its closing capture and step-19 row are this act's carried
### files ((R350)(2)), each committed alone at step zero; tools/mirror_prevbuild.json carried no content change (its LF form equal to HEAD's).
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
PRE_PP = '5b89b86b0ec20b15caad055aaf6f52144991a604'    # ### PLACE-papers main before the act's own commits: b739's record
PRE_RELAY = 'c961e9d768fa393f2d42024de5766a7987d9b6c0'  # ### relay main before the act's own commits: b739's closing
PRE_PP_REMOTE_AT_START = '5b89b86b'      # ### PLACE-papers remote main at the act's start (data/act_current.json, equal to local)
PRE_RELAY_REMOTE_AT_START = 'c961e9d7'   # ### relay remote main at the act's start (the citation check's remote main row)
B718_RELAY_HEAD = 'c961e9d'  # ### the names kept for the carried readers: the previous act's last relay head (b739's closing)
B718_PP_HEAD = '5b89b86'     # ### the previous act's last PLACE-papers head (b739's record)
DATE = '2026-11-04'
SESSION_ID = '352ad3f4-37c5-4360-b9c6-cb7368f5f805'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R350) BEGIN'           # ### the act's capture anchor, as data/act_current.json
RULING_ANCHOR = 'RULING (R350) BEGIN'    # ### the ruling's BEGIN line, the citation tool's ferry source
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = 'c6c3fbf2-d7af-4287-b739-0cca197d161f'   # ### b739 ran in this session (from 'RULING (R349) BEGIN')
PREV_ANCHOR = 'RULING (R349) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b740_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 13351          # ### FINDINGS: b739's entry head (PLACE-papers 5b89b86)
B711_WEIGHT = 13281         # ### FINDINGS: b738's weight line (b739's Component 1)
B711_CORRIGENDUM = 13283    # ### FINDINGS: b739's corrigendum for b738
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 17508          # ### OPEN_TRAILS: b739's trail record (PLACE-papers 5b89b86)
B711_FACE = 'data/b739_registration_2026-11-04.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-11-04-b739.zip'   # ### b739's export, built after b739's last PLACE-papers push, CLEAN 3/3
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
ORDER_LEDGER_SPLIT = 14680  # ### OPEN_TRAILS: W-ORD-LEDGER-SPLIT-RESOLVER (b680), (R350)(3)
TRAIL_ORDERS = 17516        # ### OPEN_TRAILS: the last open-orders line, b739's, written from the generator's output
TRAIL_RESOLVED = 17546      # ### OPEN_TRAILS: b739's items for the author's strike, in its trail
TRAIL_RETIRED = 17532       # ### OPEN_TRAILS: b739's count line of the author's answers
#   ### b740 step zero: b739's and b738's worklists carried 17410/17442/17428 (b737's trail lines) under these names; set to b739's here
WATCH_LINE = 16126          # ### OPEN_TRAILS: W-ORD-QUASI-RH-FIELD-WATCH, annotated at b718's C6
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row
INSTRUMENTS = 'phase1.5/method/INSTRUMENTS.md'   # ### PLACE-papers' instruments document, its last entry I-108 (b739)
INSTRUMENTS_LAST = 108

# ### (R350)(3): the five records, in the order the ruling names them: (row, kernel, Zenodo record, the sitting row's line in data/b736_sitting.txt)
TIER3 = ((104, 'SIDE-cosmo', '19938009', 1095), (105, 'SIDE-effects', '19938005', 1105), (106, 'SIDE-trivium', '19938003', 1115),
         (107, 'SIDE-interfaces', '19931797', 1125), (108, 'SIDE-kernel', '21520474', 1135))
TIER3_BANK = 'data/b739_tier3.txt'                  # ### b740: b739's, read not written (no Zenodo field touched, (R350)(5))
READBACK_BANK = 'data/b739_zenodo_readback.json'

# ### the branches step zero deletes ((R350)(5)): the push-b739-* branches b739's close made, by name, each read from the listings and
# ### `--merged` printed before the deletes, one per command, each its own message
DELETE = (('D:/relay', ('push-b739-closing', 'push-b739-preroot', 'push-b739-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b739-preroot', 'push-b739-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R350)(8): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'), ('D:/SIDE-explicit-formula', 'challenge-b720-h2-sign-iff-rh'),
                 ('D:/SIDE-lv-conservation', 'scratch-b724'), ('D:/SIDE-explicit-formula', 'keiper-b725'), ('D:/SIDE-explicit-formula', 'c2-b725'),
                 ('D:/SIDE-kernel', 'rebuild-b721'), ('D:/SIDE-lv-conservation', 'rebuild-b721'), ('D:/SIDE-archimedean', 'rebuild-b721'),
                 ('D:/SIDE-frobenius', 'rebuild-b721'), ('D:/SIDE-spinor', 'rebuild-b721'), ('D:/SIDE-rcurve', 'rebuild-b721'))

# ### the kernels: read; written only on the rebuild-b721 branches by (R350)(7) and the author's word (4)
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')


def _kernel_paths():
    """the kernels of data/b716_federation_pin_price.txt (1), as D:/<name>, read at import ((R350) PATHS)."""
    p = os.path.join(D, 'b716_federation_pin_price.txt')
    t = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return tuple('D:/' + m.group(1) for m in re.finditer(r'(?m)^  (SIDE-[A-Za-z0-9-]+)\s+HEAD ', t))


KERNEL_PATHS = _kernel_paths()
PATHS = ('D:/relay', PP, KERNEL_DIR, LV_DIR) + tuple(k for k in KERNEL_PATHS if k not in (KERNEL_DIR, LV_DIR))   # ### (R350)'s PATHS
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, untouched (N5)
LV_MAIN = '305a87c9e09c45cc8a935b1065f26f929634c707'    # ### SIDE-lv-conservation's main at the sitting's [41] (README.md alone, (R350)(3))
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
# ### the wave 1 kernels at their own pins, (name, tag, the short commit) -- b721's (R331)(7), b739's (R349)(10)
WAVE1 = (('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-archimedean', 'v0.1.0', '8019d9d'),
         ('SIDE-frobenius', 'v0.1.0', '2efe9f2'), ('SIDE-spinor', 'v0.1.0', 'b235bc6'), ('SIDE-rcurve', 'v0.1.0', 'd5f33b4'))
CHECKPOINT_STATEMENTS = (('SIDE-archimedean', 'archimedean_forces_half'), ('SIDE-frobenius', 'indicial_forces_half'),
                         ('SIDE-spinor', 'spinor_forces_half'), ('SIDE-spinor', 'half_iff_centered_zero'), ('SIDE-rcurve', 'monotone_unique_zero'))
REBUILD_BRANCH = 'rebuild-b721'          # ### b721's branches, kept, (R350)(7)'s repair made on them alone
REBUILD_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-lv-conservation', 40706311269), ('SIDE-archimedean', 40706397470),
                ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404), ('SIDE-frobenius', 40713201832))   # ### b721's, each read by its id
AXIOM_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-archimedean', 40706397470), ('SIDE-frobenius', 40713201832),
              ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404))   # ### b739's (R349)(10): the five whose axiom step was diagnosed
AXIOM_DIAG = 'data/b729_axiom_diag.txt'  # ### the routes (R350)(7) and the author's word (4) take
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
DATA_STANDING = 'data/standing_clauses_v9.txt'   # ### v8 bound the act to d9739558; v9 from that commit, which landed it at Component 1 ((R350)(2)(v))
DATA_STANDING_V9 = 'data/standing_clauses_v9.txt'
ARM_TAGS = 'data/arm_tags.json'
REPO_VISIBILITY = 'data/repo_visibility.txt'
PLAN_BANK = 'data/b737_offlinezero_plan.txt'          # ### (R350)(3): the plan the build reads, b737's, as committed at 3dab6492 (no plan row rewritten)
REGISTRATIONS = PLAN_BANK                             # ### (carried name) the act's registration: b737's plan, its last commit C2_PLAN_FIRST
PREV_BUILD_BANK = 'data/b738_offlinezero.txt'         # ### (R350)(3): b738's build bank as committed at a31dc7a0, md5 3b66d5df07b0c59061b21b2cf7418b91
PREV_BUILD_MD5 = '3b66d5df07b0c59061b21b2cf7418b91'
STATEMENTS_BANK = 'data/b740_s5cd_statements.txt'     # ### (R350)(3)(a): the statements, committed before any Lean file
BUILD_BANK = 'data/b740_offlinezero.txt'              # ### (R350)(3)(b)-(d): the build's bank, its grade at its foot
NOTES_BANK = 'data/b740_offlinezero_notes.txt'        # ### (R350)(3): a row found wrong noted beside it, with the reason
REG_WALK_COMMIT = '15cb6cc4'                     # ### b721's H-C2-WALK commit (carried name; b739's walk read under it)
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
#   ### read not written (carried name); b739 wrote no coefficient bank
COMPUTE_BANKS = ('data/b740_standing_v1200.txt', 'data/b740_s5cd_statements.txt', 'data/b740_offlinezero.txt', 'data/b740_offlinezero_notes.txt',
                 'data/b740_address_scan.txt')
#   ### the banks of (R350)(2)-(3), each written by its component
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt',
              'data/b729_read_calls.txt', 'data/b730_read_calls.txt', 'data/b739_read_calls.txt', 'data/b740_read_calls.txt')

# ### THE SUITE'S PARTS: ten, as b739 split them under (R349)(2)(vi) and b675 rules row (2) (standing-a in two, G-NO-SORRY-MAIN's kernels
# ### halved, and the chain's first half in four, b2a-b2d); data/act_current.json committed them ten at b740's step zero (e0777ce8), no
# ### component splitting them this act, so PARTS_AT_STEP_ZERO is PARTS
PARTS = ('standing-a1', 'standing-a2', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d', 'standing-b3', 'act')
PARTS_AT_STEP_ZERO = PARTS
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b740'))
CHAIN_QUARTERS = (('b624', 'b627'), ('b628', 'b631'), ('b632', 'b635'), ('b636', 'b658'))   # ### walks 116, 129, 157, 146 s at b740
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### set by the Edit tool when a component adds a standing arm
SHARED_APPENDED = ('data/b675_corrigenda.txt',)   # ### (R350)(2): the corrigenda row
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md')   # ### the ledgers ((R350)(4)'s (W) list)
PP_WRITTEN = PP_EDITED
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the re-cut's merge (kept for the kernel rows); the MANIFEST control's reference
#   ### is the commit the mirror is built at from v1.2.1
NEXT = ('per (R350)(6), named by the author: S6 (the frontier) of W-ORD-ZQ-OFFLINE-ZERO on the measured price, the wave 1 deposit, or the carried orders')
NEXT_ACT = 'b741'


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
ACT_CURRENT_COMMIT = 'e0777ce8'         # ### data/act_current.json for b740 committed alone ((R350)(4)), before any other command
STEPZERO = '9f8d04b3'             # ### b739's closing capture, committed alone ((R350)(2))
STEPZERO_STEPS = 'cd966015'       # ### b739's step-19 row, committed alone ((R350)(2))
STEPZERO_TABLE = None             # ### the terminal table regenerated and committed ((R350)(8))
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None   # ### tools/mirror_prevbuild.json of b739: its LF form equal to HEAD's (2d637131, blob a94aa543), nothing to commit
STEPZERO_REFUSALS = ()
STEPZERO_BANKS = '3c731098'       # ### step zero's banks and carried tools, one commit (data/b740_stepzero.txt among them)
STEPZERO_BANK_COMMIT = '3c731098'
VISIBILITY_COMMIT = None
COMPUTE_TOOLS = ()                      # ### set by the Edit tool when a component seals a compute tool
REPAIRED_TOOLS = tuple(p[len('tools/'):] for p in json.load(io.open(os.path.join(D, 'act_current.json'), encoding='utf-8'))['shared_edits'])
#   ### (R350)(2), b739 event (2): read from data/act_current.json, the one hand list, which G-ACT-CURRENT reads against git; sealed before the suite runs (b696's form)
REPAIRED_DATA = ()
# ### b721's trap (event 11): the standing part of the sealed list read from the directory, not a carried tuple
STANDING_FILES = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing')) if f == 'VERSION' or f.endswith('.py')))
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset, sealed by hash beside the act's tools
# ### the seven close tools are tools/standing/fold.py's renders of its templates (tools/standing/fold/<tool>.tpl) with the act's arms module
# ### (tools/acts/b740.py) -- every byte a render reads sealed beside the act's tools; report.tpl left out of the seal (b708's report row)
FOLD_FILES = tuple(sorted('standing/fold/' + f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing', 'fold')) if f.endswith('.tpl')
                          and f != 'report.tpl')) + ('acts/b740.py',)
NEW_TOOLS = NEW_TOOLS + FOLD_FILES
STANDING_VERSION = 'v1.20.0'            # ### (R350)(2)'s repairs, landed by a commit of their own (C1_STANDING) with data/b740_standing_v1200.txt
STANDING_VERSION_ENTERING = 'v1.19.0'
LEAN_TREES = (('D:/SIDE-explicit-formula', '602cd401'), ('D:/SIDE-explicit-formula/.lake/packages/mathlib', 'de5ce8a9'))   # ### zq-b730 at b738's tip
# ### v1.18.0, (R350)(2)(ii): the act's banks whose comparative sentences the citation check reads, and a reading row for each word (tools/standing/cites.py
# ### comparative_rows); set by the Edit tool as Components 2-4 write the banks, before the lock
COMPARATIVE_BANKS = ('data/b740_corrigendum.txt', 'data/b740_s5cd_statements.txt', 'data/b740_offlinezero.txt', 'data/b740_offlinezero_notes.txt',
                     'data/b740_defects.txt')   # ### Components 1-4's banks: no
COMPARATIVE_ROWS = ()   # ### comparative word in them ("at least" excepted by the reader), so no reading row; the check reads the three for one
#   ### the trees the ruling's Lean paths are read against: zq-b730's tip, and Mathlib at its pin (the ferry's "Mathlib at the pin: Analysis/Complex/AbsMax.lean :405, ...")
STANDING_CHANGED = ()
STANDING_NEW = ()
# ### b739's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = 'c961e9d7'    # ### b739's closing, the act's relay base
B714_RECORD = 'a5b5f216'     # ### b739's record commit (relay, the head line's)
B714_ROOT = '407e3f98c4ae10e82056fabe9ce87f192973fd90a963838064d458a9d09b11b7'   # ### b739's root, data/act_roots.txt's last row
B723_ROOT_BANKS = '64e3e5e8'  # ### b739's root commit, the banks its root rode with
# ### later stages: the commits of the components, read from the logs after each was made (None until made)
C1_STANDING = '63424433'               # ### tools/standing/ v1.20.0 by a commit of its own, its controls bank data/b740_standing_v1200.txt ((R350)(2)(vi))
C1_STANDING_REPAIR = None          # ### no act data changed by the repairs
C1_RELAY = 'd50a86be'              # ### the c1 route, the corrigendum banks, the corrigenda row (60)
C1_CORR = C1_RELAY
C1_RULES = '744cb044'              # ### the rules bank of (R350)(2), data/b740_rules.txt, by a commit of its own
C1_PP = '454f2167'                 # ### PLACE-papers: FINDINGS :13387 (b739 at its weight), :13389 (the corrigendum)
C1_DISCHARGE_PP = None
C2_TOOL = 'tools/b740_offlinezero.py'
WEIGHT_LINE, CORR_LINE = None, None   # ### FINDINGS: b739's weight line and the corrigendum for b739 (Component 1), set when written
DIFFERS_LINE = None
ERRATA_LINE = None
C2_PLAN_FIRST = '3dab6492e948e79243a5ebeba7dffb575712a4be'   # ### the plan bank's last commit (b737's), the blob the build reads
C2_RELAY = None         # ### Component 2, the statements bank, committed before any Lean file ((R350)(3)(a))
C2_PP = None
PRICE_LINE = 17400
DOORS_COMMIT = None
MECH_COMMIT = None
FRONTDOORS_COMMIT = None
COUNT_BANK = None
PRINT_COMMIT = C2_RELAY  # ### (carried name) the commit carrying the act's result bank: the plan's
PLAN_MD5 = '3d61f519917a3ee20ac4d7c5fab197ef'   # ### printed at step zero (data/b740_citation_check.txt) before any Lean file
C2_AMEND = ()
SITTING_PP = ()
C3_RELAY = ()            # ### Component 3, the build to SP3 ((R350)(3)(b)), set when made
SITTING_COMMITS = ()
C3_PP = None
C4_LV = None
C4_RUN = None
C4_PP = None
C4_RELAY = None
C5_RELAY = None
REG_COMMIT = C2_PLAN_FIRST    # ### the plan's first commit, with the prints it cites
ZEROS_REG_COMMIT = REG_COMMIT
ORDERS = (142, 60, 42, 12, 28)          # ### b739's (R349)(4) triage, carried as read (data/b729_orders_triage.txt): DONE, NOT MET, MET, AUTHOR'S WORD
TRIAGE = 'data/b729_orders_triage.txt'
LV_SCRATCH_BRANCH = 'scratch-b724'      # ### b724's scratch branch of SIDE-lv-conservation, kept ((R350)(8))
LV_RUNS = (('SIDE-lv-conservation', 40964150574),)   # ### b739's one dispatch, read by its id (carried, not re-run)
LV_ROWS = 'data/b740_lv_rows.json'
CHALLENGE_BRANCH = 'challenge-b720-h2-sign-iff-rh'   # ### b720's, on SIDE-explicit-formula, standing, not merged, no tag
CHALLENGE_TIP = '3391647518cd37316a448b5013afb62a198fa6c6'
CHALLENGE_RUN = 40651875792
PIN_RUNS = (('SIDE-grh-transfer', 40652622018), ('SIDE-interfaces', 40652657325), ('SIDE-kernel', 40652692787),
            ('SIDE-lv-conservation', 40652727943), ('SIDE-simplicity', 40652762827), ('SIDE-trivium', 40652790458))   # ### b720's, read not re-run
PIN_BRANCH = 'pin-b718-de5ce8a9'   # ### b718's pin branches, left as banked ((R350)(8))
PIN_EXCLUDED = ('SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve', 'SIDE-cosmo')
PIN_HELD = ('SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium')
PIN_BUILDS = ('SIDE-simplicity',)
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PIN_TO_NEXT = ()
MAX_DISPATCHES = 12        # ### N1: at most twelve runner dispatches ((R350)(3)(d))
MAX_C2, MAX_KEIPER = 0, 0
EF_DIR = 'D:/SIDE-explicit-formula'
EF_BASE = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'   # ### SIDE-explicit-formula's main, every branch cut from it, untouched (N5)
ZQ_BRANCH = 'zq-b730'
ZQ_ENTERING = '602cd401468f9f7bfa9b131dcd0e3302402ba939'   # ### b738's tip (S5a's ASCII terminal), unmoved by b739: the build's base ((R350)(3))
ZQ_TIP = 'ba318a0b67fd95164623e4fdf109eb5d042697fa'   # ### the act's last Lean commit on zq-b730 (S5d's fix), pushed, remote equal 15:35:17Z
ZQ_FIRST = '8c6ec8d12d97bece1de8dab10511add9d97382d0'   # ### (R350)(3)(b): the act's first Lean commit (S5c), after the statements bank a9c206b9
ZQ_COMMITS = (ZQ_FIRST, '6b068a0db2ff1451e9da7bff82fe8fd66a8dad38', ZQ_TIP)   # ### S5c ; S5d with S5c's fix ; S5d's fix
ZQ_SP1 = None
ZQ_SP3 = None                # ### SP3 reached here, if reached
ZQ_MODULES = ('Xi', 'Landau', 'Heights', 'Contour', 'ZeroSum', 'FullLine', 'Lines', 'Main')   # ### the build's eight, under Schema/ZQ/EF
ZQ_OFFZERO_MODULES = ('Box', 'Diff', 'MinModulus', 'Carrier', 'Main', 'Split', 'Tail', 'IncGamma', 'Elem')   # ### under Schema/ZQ/OffZero, one a group; b740 adds S5c IncGamma, S5d Elem
ZQ_FILES = ()   # ### zq-b730's diff against its entering tip, set as the build writes
ZQ_MODULES_B730 = ('Lattice', 'Theta', 'FEPair', 'Continuation')   # ### the names the carried sections read, until each section is set for this act
ZQ_ZEROS_FIRST, ZQ_LOGDERIV_TIP = None, None
ZQ_LOGDERIV_MODULES, ZQ_ZEROS_MODULES = (), ()
MAX_LOGDERIV, MAX_ZEROS = 0, 0
EF_BRANCHES = (('keiper-b725', '01fd33c2d7dc62d4702b075de3dda9253c5c2f87'),   # ### (R350)(4): the gamma_1 bound
               ('c2-b725', '0395f15d3b2906716ccb1f09ca24171d7a921210'),       # ### (R350)(3): the theorem, built whole at this tip
               ('detect-b729', '1023301c89ab16f8d437b2a1f08a824bc95b6b0e'),   # ### b729's (R339)(5): the statement alone, not compiled; kept, unmoved
               (ZQ_BRANCH, ZQ_TIP))                                           # ### (R350)(3)-(4): the fields
EF_BRANCHES_ENTERING = ('01fd33c2d7dc62d4702b075de3dda9253c5c2f87', '0395f15d3b2906716ccb1f09ca24171d7a921210', '1023301c89ab16f8d437b2a1f08a824bc95b6b0e', ZQ_ENTERING)   # ### the four entering the act
EF_RUNS = (41854903335, 41857376723, 41859346843)   # ### (R350)(3)(b): the act's dispatches, each read by its run id: BREAKS, BREAKS, KERNEL
EF_RUNS_B738 = (41732413170, 41732882564, 41733411736, 41734667160, 41735082430, 41736472780)   # ### b738's first six (of eleven), read not re-run
ZQ_RUN = 41483457057   # ### b737's grade run, the discharge's, read not re-run
EF_RUNS_B731 = (41371666217, 41372597450, 41373409167, 41374121055, 41374814817)   # ### b731's five, read not re-run
DISPATCH_ROWS = 'data/b740_dispatch_rows.json'
ERRATA_ID = None   # ### (R350) orders no ERRATA entry
ERRATA_IDS = ()
RETIRED_COUNT = 0
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list (the root answer's addition (b))
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b740_') and f.endswith('.py') and f != 'b740_report.py')) + NEW_TOOLS + COMPUTE_TOOLS + REPAIRED_TOOLS
# ### the act's arms over its own banks: set before the lock by the Edit tool -- b739's list, the act shift G-R349-ENTERED to G-R350-ENTERED,
# ### G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0 ((R350)(2)(iv))
ACT_ARMS = ('G-ACT-CURRENT', 'G-ARM-TAGS', 'G-ARMS-RETIRED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED', 'G-CLOSING-DRY-STEP', 'G-COEFFS-LAW',
            'G-CORRIGENDUM-ENTERED', 'G-COUNT-ROUTE-PRICED', 'G-DELETES-ONE-BRANCH', 'G-DERIVATION-GRADED', 'G-DIFFERS-ERRATA', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-GUARD-HELD', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LISTINGS-BEFORE-CLAUSES',
            'G-MEMBRANE-WIRED', 'G-OFFSET-POST-HOC', 'G-POSTROOT-WRITES-NONE', 'G-PREDICTION-FIRST', 'G-R350-ENTERED',
            'G-REGISTRATIONS-FIRST', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED', 'G-SURGERY-CARRIED', 'G-TOUCH-READ',
            'G-WRITELIST-MIRROR-STATE')

# ### b740 writes one kernel branch, zq-b730 of SIDE-explicit-formula ((R350)(3), (5)); its main untouched
SITTING_TIPS = {'SIDE-explicit-formula': ZQ_TIP[:8]}
SITTING_BASE = ZQ_ENTERING
SITTING_REPOS = tuple(sorted(SITTING_TIPS))
SITTING_BRANCH = ZQ_BRANCH   # ### the act's one written branch
SITTING_BANK = 'data/b736_sitting.txt'   # ### the notes' rows [104]-[108], read unedited ((R350)(3)(a))
KERNEL_BASES = 'data/b740_kernel_bases.json'
