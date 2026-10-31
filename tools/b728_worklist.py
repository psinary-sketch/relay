# -*- coding: utf-8 -*-
"""b728_worklist.py -- THE ACT'S DATA, UNDER (R338). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b728: LANE TWO, ACT ONE HUNDRED AND FIFTY-FIVE, THE RESEARCH ACT -- b727 AT ITS WEIGHT; THE CORRIGENDUM AND EVERY CARRIED REPAIR WITH ITS
### CONTROL; THE ONSET SUCCESSOR DERIVED THEN REGISTERED; THE LAST C2 FIELDS; lambda_2'S PREMISES; VISIBILITY; THE SIZE ROW. At most eight dispatches (N1).
### Carried by diff from b727_worklist.py (data/b728_carry_worklist.txt); its stage one set by the Edit tool at step zero with this act's
### figures (the carried text named b727's objects under b728's names); later stages by the Edit tool.
### The act runs in b727's session (7c29db99), one seat.
### b727 closed and pushed itself whole (relay 1bf8a57c, PLACE-papers 3742f12); its closing capture and step-39 row are this act's carried
### files ((R338)(8)), each committed alone at step zero.
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
PRE_PP = '3742f12b25c9b16065fd9c30dd8e3ac3730df828'    # ### PLACE-papers main before the act's own commits: b727's record
PRE_RELAY = '1bf8a57c22b17303d08d8c05e98c1bceeba75fef'  # ### relay main before the act's own commits: b727's closing
PRE_PP_REMOTE_AT_START = '3742f12b'      # ### PLACE-papers remote main at the act's start (data/act_current.json, equal to local)
PRE_RELAY_REMOTE_AT_START = '1bf8a57c'   # ### relay remote main at the act's start (the citation check's remote main row)
B718_RELAY_HEAD = '1bf8a57'  # ### the names kept for the carried readers: the previous act's last relay head (b727's closing)
B718_PP_HEAD = '3742f12'     # ### the previous act's last PLACE-papers head (b727's record)
DATE = '2026-10-31'
SESSION_ID = '7c29db99-62df-4f5e-a436-7e99b58f5dbf'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R338) BEGIN'           # ### the act's capture anchor, as data/act_current.json
RULING_ANCHOR = 'RULING (R338) BEGIN'    # ### the ruling's BEGIN line, the citation tool's ferry source
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = '7c29db99-62df-4f5e-a436-7e99b58f5dbf'   # ### b727 ran in this session (from 'RULING (R337) BEGIN')
PREV_ANCHOR = 'RULING (R337) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b728_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 11976          # ### FINDINGS: b727's entry head (PLACE-papers 909b370)
B711_WEIGHT = 11911         # ### FINDINGS: b726's weight line (b727's Component 1)
B711_CORRIGENDUM = 11913    # ### FINDINGS: b727's corrigendum for b726
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 16746          # ### OPEN_TRAILS: b727's trail record (PLACE-papers 3742f12)
B711_FACE = 'data/b727_registration_2026-10-31.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-31-b727.zip'   # ### b727's export, built after b727's last PLACE-papers push, CLEAN 3/3
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
ORDER_LEDGER_SPLIT = 14680  # ### OPEN_TRAILS: W-ORD-LEDGER-SPLIT-RESOLVER (b680), (R338)(3)
TRAIL_ORDERS = 16757        # ### OPEN_TRAILS: the last open-orders line, b727's, written from the generator's output
TRAIL_RESOLVED = 16791      # ### OPEN_TRAILS: b727's items for the author's strike, in its trail
TRAIL_RETIRED = 16817       # ### OPEN_TRAILS: b727's count line of the author's answers
WATCH_LINE = 16126          # ### OPEN_TRAILS: W-ORD-QUASI-RH-FIELD-WATCH, annotated at b718's C6
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row
INSTRUMENTS = 'phase1.5/method/INSTRUMENTS.md'   # ### PLACE-papers' instruments document, its last entry I-108 (b727)
INSTRUMENTS_LAST = 108

# ### the branches step zero deletes ((R338)(5)): the push-b727-* branches b727's close made, by name, each read from the listings and
# ### `--merged` printed before the deletes, one per command, each its own message
DELETE = (('D:/relay', ('push-b727-closing', 'push-b727-preroot', 'push-b727-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b727-preroot', 'push-b727-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R338)(8): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'), ('D:/SIDE-explicit-formula', 'challenge-b720-h2-sign-iff-rh'),
                 ('D:/SIDE-lv-conservation', 'scratch-b724'), ('D:/SIDE-explicit-formula', 'keiper-b725'), ('D:/SIDE-explicit-formula', 'c2-b725'),
                 ('D:/SIDE-kernel', 'rebuild-b721'), ('D:/SIDE-lv-conservation', 'rebuild-b721'), ('D:/SIDE-archimedean', 'rebuild-b721'),
                 ('D:/SIDE-frobenius', 'rebuild-b721'), ('D:/SIDE-spinor', 'rebuild-b721'), ('D:/SIDE-rcurve', 'rebuild-b721'))

# ### the kernels: read; written only on the rebuild-b721 branches by (R338)(7) and the author's word (4)
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')


def _kernel_paths():
    """the kernels of data/b716_federation_pin_price.txt (1), as D:/<name>, read at import ((R338) PATHS)."""
    p = os.path.join(D, 'b716_federation_pin_price.txt')
    t = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return tuple('D:/' + m.group(1) for m in re.finditer(r'(?m)^  (SIDE-[A-Za-z0-9-]+)\s+HEAD ', t))


KERNEL_PATHS = _kernel_paths()
PATHS = ('D:/relay', PP, KERNEL_DIR, LV_DIR) + tuple(k for k in KERNEL_PATHS if k not in (KERNEL_DIR, LV_DIR))   # ### (R338)'s PATHS
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, untouched (N5)
LV_MAIN = '305a87c9e09c45cc8a935b1065f26f929634c707'    # ### SIDE-lv-conservation's main at the sitting's [41] (README.md alone, (R338)(3))
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
# ### the wave 1 kernels at their own pins, (name, tag, the short commit) -- b721's (R331)(7), b727's (R337)(10)
WAVE1 = (('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-archimedean', 'v0.1.0', '8019d9d'),
         ('SIDE-frobenius', 'v0.1.0', '2efe9f2'), ('SIDE-spinor', 'v0.1.0', 'b235bc6'), ('SIDE-rcurve', 'v0.1.0', 'd5f33b4'))
CHECKPOINT_STATEMENTS = (('SIDE-archimedean', 'archimedean_forces_half'), ('SIDE-frobenius', 'indicial_forces_half'),
                         ('SIDE-spinor', 'spinor_forces_half'), ('SIDE-spinor', 'half_iff_centered_zero'), ('SIDE-rcurve', 'monotone_unique_zero'))
REBUILD_BRANCH = 'rebuild-b721'          # ### b721's branches, kept, (R338)(7)'s repair made on them alone
REBUILD_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-lv-conservation', 40706311269), ('SIDE-archimedean', 40706397470),
                ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404), ('SIDE-frobenius', 40713201832))   # ### b721's, each read by its id
AXIOM_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-archimedean', 40706397470), ('SIDE-frobenius', 40713201832),
              ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404))   # ### b727's (R337)(10): the five whose axiom step was diagnosed
AXIOM_DIAG = 'data/b727_axiom_diag.txt'  # ### the routes (R338)(7) and the author's word (4) take
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
DATA_STANDING = 'data/standing_clauses_v9.txt'   # ### v8 bound the act to d9739558; v9 from that commit, which landed it at Component 1 ((R338)(2)(v))
DATA_STANDING_V9 = 'data/standing_clauses_v9.txt'
ARM_TAGS = 'data/arm_tags.json'
REPO_VISIBILITY = 'data/repo_visibility.txt'
REGISTRATIONS = 'data/b725_registrations.txt'    # ### b728 registers no hypothesis ((R338) orders none; b727 registered none: b725's the last, carried name)
REG_WALK_COMMIT = '15cb6cc4'                     # ### b721's H-C2-WALK commit (carried name; b727's walk read under it)
REG_COMMITS = (('data/b716_registrations.txt', 'dc5e808f'), ('data/b718_registrations.txt', '8146404b577dfee3e379d19e08e8595ab8824961'),
               ('data/b719_registrations.txt', '965cb8e84dc02192854512af53a29b1fbc2b80f5'), ('data/b720_registrations.txt', '54fc03d9'),
               ('data/b721_registrations.txt', 'e8c3dff40df43269b3f0c4b917baef7c96c0f649'),
               ('data/b725_registrations.txt', 'dc0d4133'))   # ### N2 (b725's row, its last amendment, the blob HEAD carries; b728 registers nothing)
REG_FILES = tuple(f for f, _c in REG_COMMITS)
PRED_B717 = 'data/b717_predictions.txt'
PRED_B717_COMMIT = 'f47d8ab5840d287bf63c1f0b59ba707ed85dbe07'
PREDICTIONS = PRED_B717
ONSETS_B717 = 'data/b717_onsets.txt'
REGISTRATIONS_NEW = 'data/b725_registrations.txt'
COEFF_BANKS = ('data/b711_coeffs.txt', 'data/b713_coeffs.txt', 'data/b717_coeffs.txt', 'data/b719_coeffs.txt', 'data/b720_coeffs.txt')
#   ### read not written (carried name); b727 wrote no coefficient bank
COMPUTE_BANKS = ('data/b728_standing_v180.txt', 'data/b728_onset_table.txt', 'data/b728_onset_b725_reread.txt', 'data/b728_c2.txt', 'data/b728_lambda2.txt', 'data/b728_visibility.txt', 'data/b728_address_scan.txt')
#   ### the banks of (R338)(2)-(5), each written by its component
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt',
              'data/b727_read_calls.txt', 'data/b728_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b727 carried them
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b728'))
CHAIN_QUARTERS = (('b624', 'b631'), ('b632', 'b658'))   # ### (R338)(2)(vi): b2a split where b727's banked walks halve (repeat.quarters; b2a's run 575 s at b727)
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### set by the Edit tool when a component adds a standing arm
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md', 'SPIRAL_MAP.md', 'day1/Which_Structure_Confines_v2_4_0.md')   # ### the ledgers and (R338)(2)(viii)'s SPIRAL_MAP :104 and edition :316
PP_WRITTEN = PP_EDITED
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the re-cut's merge (kept for the kernel rows); the MANIFEST control's reference
#   ### is the commit the mirror is built at from v1.2.1
NEXT = ('b729 under (R338)(10): the Beurling row’s literature read for the mechanism table and the 2C cluster’s note on the statement-grading instruments beside Invariance Barriers; '
        'H-ONSET-MASS-2’s test and W-ORD-VISIBILITY’s registration fall away, (3) having registered nothing and (6) having written no candidate')
NEXT_ACT = 'b729'


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
ACT_CURRENT_COMMIT = '55c59169'         # ### data/act_current.json for b728 committed alone, before any other git command ((R338)(8))
STEPZERO = 'a9227b53'             # ### b727's closing capture, committed alone ((R338)(8))
STEPZERO_STEPS = '6405579d'       # ### b727's step-39 row, committed alone ((R338)(8))
STEPZERO_TABLE = None             # ### the terminal table regenerated and committed ((R338)(8))
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None
STEPZERO_REFUSALS = ()
STEPZERO_BANKS = 'a9dd62ce'             # ### the step-zero banks and tools, committed together by explicit list (step 4)
STEPZERO_BANK_COMMIT = 'a9dd62ce'       # ### the step-zero bank itself (data/b728_stepzero.txt), with the price table, in that commit
VISIBILITY_COMMIT = None
COMPUTE_TOOLS = ()                      # ### set by the Edit tool when a component seals a compute tool
REPAIRED_TOOLS = tuple(p[len('tools/'):] for p in json.load(io.open(os.path.join(D, 'act_current.json'), encoding='utf-8'))['shared_edits'])
#   ### (R338)(2), b727 event (2): read from data/act_current.json, the one hand list, which G-ACT-CURRENT reads against git; sealed before the suite runs (b696's form)
REPAIRED_DATA = ()
# ### b721's trap (event 11): the standing part of the sealed list read from the directory, not a carried tuple
STANDING_FILES = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing')) if f == 'VERSION' or f.endswith('.py')))
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset, sealed by hash beside the act's tools
# ### the seven close tools are tools/standing/fold.py's renders of its templates (tools/standing/fold/<tool>.tpl) with the act's arms module
# ### (tools/acts/b728.py) -- every byte a render reads sealed beside the act's tools; report.tpl left out of the seal (b708's report row)
FOLD_FILES = tuple(sorted('standing/fold/' + f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing', 'fold')) if f.endswith('.tpl')
                          and f != 'report.tpl')) + ('acts/b728.py',)
NEW_TOOLS = NEW_TOOLS + FOLD_FILES
STANDING_VERSION = 'v1.8.0'             # ### (R338)(2)'s repairs landed v1.8.0 by a commit of their own (C1_STANDING)
STANDING_CHANGED = ()                   # ### the standing files (R338)(2) changes, set by the Edit tool when they land
STANDING_NEW = ()
# ### b727's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = '1bf8a57c'    # ### b727's closing, the act's relay base
B714_RECORD = 'a079a1ad'     # ### b727's record commit (relay, the head line's)
B714_ROOT = 'c527524ad1541ba76f916984b320b8098460600556d1e93d52ac1769202ca76e'   # ### b727's root, data/act_roots.txt's last row
B723_ROOT_BANKS = '38043c6e'  # ### b727's root commit, the banks its root rode with
# ### later stages: the commits of the components, read from the logs after each was made (None until made)
C1_STANDING = '26a54c72'                # ### (R338)(2): tools/standing/ v1.8.0
C1_STANDING_REPAIR = None
C1_RELAY = '48952a59'                   # ### (R338)(1)-(2): the corrigendum's banks and the sitting tool
C1_CORR = '48952a59'                    # ### the corrigendum banks, the corrigenda row
C1_PP = '00b235d'                      # ### FINDINGS: b727 at its weight, the observation and the corrigendum for b727
WEIGHT_LINE, CORR_LINE = 12014, 12016   # ### FINDINGS: b727's weight line and the corrigendum for b727 (Component 1)
DIFFERS_LINE = None
ERRATA_LINE = None
C2_RELAY = '13bdc06f'                   # ### (R338)(3): the onset table, POST HOC, and b725's refutation re-read
C2_AMEND = ()
C2_PP = None
C3_RELAY = ('f1c86348',)                # ### (R338)(4): tools/b728_c2.py; the banks' commit added when it is made
C3_PP = None
C4_LV = None
C4_RUN = None
C4_PP = None
C4_RELAY = None
C5_RELAY = None
REG_COMMIT = 'dc0d4133'                 # ### b727's last registration commit (carried name; b728 registers nothing)
ORDERS = (142, 60, 42, 12, 28)          # ### b727's (R337)(4) triage, carried as read (data/b727_orders_triage.txt): DONE, NOT MET, MET, AUTHOR'S WORD
TRIAGE = 'data/b727_orders_triage.txt'
LV_SCRATCH_BRANCH = 'scratch-b724'      # ### b724's scratch branch of SIDE-lv-conservation, kept ((R338)(8))
LV_RUNS = (('SIDE-lv-conservation', 40964150574),)   # ### b727's one dispatch, read by its id (carried, not re-run)
LV_ROWS = 'data/b728_lv_rows.json'
CHALLENGE_BRANCH = 'challenge-b720-h2-sign-iff-rh'   # ### b720's, on SIDE-explicit-formula, standing, not merged, no tag
CHALLENGE_TIP = '3391647518cd37316a448b5013afb62a198fa6c6'
CHALLENGE_RUN = 40651875792
PIN_RUNS = (('SIDE-grh-transfer', 40652622018), ('SIDE-interfaces', 40652657325), ('SIDE-kernel', 40652692787),
            ('SIDE-lv-conservation', 40652727943), ('SIDE-simplicity', 40652762827), ('SIDE-trivium', 40652790458))   # ### b720's, read not re-run
PIN_BRANCH = 'pin-b718-de5ce8a9'   # ### b718's pin branches, left as banked ((R338)(8))
PIN_EXCLUDED = ('SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve', 'SIDE-cosmo')
PIN_HELD = ('SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium')
PIN_BUILDS = ('SIDE-simplicity',)
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PIN_TO_NEXT = ()
MAX_DISPATCHES = 8           # ### N1: (R338)(4) six at most, (R338)(5) two at most
MAX_C2, MAX_KEIPER = 6, 2
EF_DIR = 'D:/SIDE-explicit-formula'
EF_BASE = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'   # ### SIDE-explicit-formula's main, both branches cut from it, untouched (N5)
EF_BRANCHES = (('keiper-b725', '2cb3936cfa87cfbcdc324c1bb950c9a0dbbe8147'),   # ### (R338)(5): KeiperGammaOne.lean on f52e188c
               ('c2-b725', 'b91bf5af59b36891765baee33da50ecf7291b025'))       # ### (R338)(4): the split within the field, d7ba0ee1 then b91bf5af, on ea95a8d0
EF_BRANCHES_ENTERING = ('f52e188c2409436337019ea0008d7352bde404c2', 'ea95a8d07a0ffae2012d715d5e95194cbf4df1ad')   # ### keiper-b725 and c2-b725 entering the act
EF_RUNS = (('c2', 41220283401, 'd7ba0ee187ec0175dc260fb25bd688cbe0a6a0dd', 'SIDEExplicitFormula.C2Field.M267'),
           ('c2', 41220928153, 'b91bf5af59b36891765baee33da50ecf7291b025', 'SIDEExplicitFormula.C2Field.M427'),
           ('c2', 41220930451, 'b91bf5af59b36891765baee33da50ecf7291b025', 'SIDEExplicitFormula.C2Field.M403'),
           ('keiper', 41220932768, '2cb3936cfa87cfbcdc324c1bb950c9a0dbbe8147', 'SIDEExplicitFormula.KeiperGammaOne'))   # ### N1: set from the runs read, (kind, run id, ref, target)
DISPATCH_ROWS = 'data/b728_dispatch_rows.json'
ERRATA_ID = None   # ### (R338) orders no ERRATA entry
ERRATA_IDS = ()
RETIRED_COUNT = 0
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list (the root answer's addition (b))
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b728_') and f.endswith('.py') and f != 'b728_report.py')) + NEW_TOOLS + COMPUTE_TOOLS + REPAIRED_TOOLS
# ### the act's arms over its own banks: set before the lock by the Edit tool -- b727's list, the act shift G-R337-ENTERED to G-R338-ENTERED,
# ### G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0 ((R338)(2)(iv))
ACT_ARMS = ('G-ACT-CURRENT', 'G-ARM-TAGS', 'G-ARMS-RETIRED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED', 'G-CLOSING-DRY-STEP', 'G-COEFFS-LAW',
            'G-CORRIGENDUM-ENTERED', 'G-COUNT-ROUTE-PRICED', 'G-DELETES-ONE-BRANCH', 'G-DERIVATION-GRADED', 'G-DIFFERS-ERRATA', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-GUARD-HELD', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LISTINGS-BEFORE-CLAUSES',
            'G-MEMBRANE-WIRED', 'G-OFFSET-POST-HOC', 'G-POSTROOT-WRITES-NONE', 'G-PREDICTION-FIRST', 'G-R338-ENTERED',
            'G-REGISTRATIONS-FIRST', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED', 'G-SURGERY-CARRIED', 'G-TOUCH-READ',
            'G-WRITELIST-MIRROR-STATE')

# ### (R338)(2)(viii): the three kernels' README writes (name, path, head before the write), their tips (carried names, b727's sitting's)
SITTING_REPOS = (('SIDE-archimedean', 'D:/SIDE-archimedean', '0e3336f'), ('SIDE-spinor', 'D:/SIDE-spinor', '5c34c72'), ('SIDE-rcurve', 'D:/SIDE-rcurve', 'f093005'))
SITTING_TIPS = {'SIDE-archimedean': 'b71ffb8aa3fd8e47b2e4f2228cdb78ce85f8ceb6', 'SIDE-spinor': '25c76d8ea20787f64963c4ac834ccb303239146b',
                'SIDE-rcurve': '0bcb6c1d707646fc7a02fb9fed5cf9b01f3d7a66'}
