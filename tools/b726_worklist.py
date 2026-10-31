# -*- coding: utf-8 -*-
"""b726_worklist.py -- THE ACT'S DATA, UNDER (R336). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b726: LANE TWO, ACT ONE HUNDRED AND FIFTY-THREE, THE WAVE 1 ACT -- b725 AT ITS WEIGHT; THE CORRIGENDUM AND THE CARRIED ITEMS; THE C2
### BUILD PER FIELD; WHICH STRUCTURE CONFINES v2.4.0 BY THE FORM OF AN EDITION; THE FRONT-DOOR LIST TRIAGED; THE LLM LINE; THE MECHANISM
### TABLE. The runner dispatches are (R336)(3)'s, eighteen at most (N1).
### Carried by diff from b725_worklist.py (data/b726_carry_worklist.txt); its stage one set by the Edit tool at step zero with this act's
### figures (the carried text named b725's objects under b726's names); later stages by the Edit tool.
### The act runs in a NEW session (7c29db99; the previous act's session 02c7cf38, closed before this one, one seat by the step-zero listing).
### b725 closed and pushed itself whole (relay e2246a8e, PLACE-papers 06af23f0); its closing capture and step-40 row are this act's carried
### files ((R336)(8)), each committed alone at step zero.
### ANCHOR is the act's capture anchor (data/act_current.json, the ruling's first line); RULING_ANCHOR the same line, the citation tool's
### ferry source.
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '06af23f0b65ad35750d143b6efd5bfaa0f5f0988'    # ### PLACE-papers main before the act's own commits: b725's record
PRE_RELAY = 'e2246a8e2319b08bc297eb93c4bd6442c16e79ba'  # ### relay main before the act's own commits: b725's closing
PRE_PP_REMOTE_AT_START = '06af23f0'      # ### PLACE-papers remote main at the act's start (data/act_current.json, equal to local)
PRE_RELAY_REMOTE_AT_START = 'e2246a8e'   # ### relay remote main at the act's start (the citation check's remote main row)
B718_RELAY_HEAD = 'e2246a8'  # ### the names kept for the carried readers: the previous act's last relay head (b725's closing)
B718_PP_HEAD = '06af23f'     # ### the previous act's last PLACE-papers head (b725's record)
DATE = '2026-10-30'
SESSION_ID = '7c29db99-62df-4f5e-a436-7e99b58f5dbf'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R336) BEGIN'           # ### the act's capture anchor, as data/act_current.json
RULING_ANCHOR = 'RULING (R336) BEGIN'    # ### the ruling's BEGIN line, the citation tool's ferry source
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = '02c7cf38-4c6a-4f88-b813-a7e15e9b85b4'   # ### b725 ran in its own session (from 'RULING (R335) BEGIN')
PREV_ANCHOR = 'RULING (R335) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b726_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 11755          # ### FINDINGS: b725's entry head (PLACE-papers 9f07bc70)
B711_WEIGHT = 11681         # ### FINDINGS: b724's weight line (b725's Component 1)
B711_CORRIGENDUM = 11683    # ### FINDINGS: b725's corrigendum for b724
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 16581          # ### OPEN_TRAILS: b725's trail record (PLACE-papers 06af23f0)
B711_FACE = 'data/b725_registration_2026-10-30.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-30-b725.zip'   # ### b725's export, built after b725's last PLACE-papers push, CLEAN 3/3
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
ORDER_LEDGER_SPLIT = 14680  # ### OPEN_TRAILS: W-ORD-LEDGER-SPLIT-RESOLVER (b680), (R336)(3)
TRAIL_ORDERS = 16596        # ### OPEN_TRAILS: the last open-orders line, b725's, written from the generator's output
TRAIL_RESOLVED = 16636      # ### OPEN_TRAILS: b725's items for the author's strike, in its trail
TRAIL_RETIRED = 16667       # ### OPEN_TRAILS: b725's count line of the author's answers
WATCH_LINE = 16126          # ### OPEN_TRAILS: W-ORD-QUASI-RH-FIELD-WATCH, annotated at b718's C6
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row
INSTRUMENTS = 'phase1.5/method/INSTRUMENTS.md'   # ### PLACE-papers' instruments document, its last entry I-108 (b725)
INSTRUMENTS_LAST = 108

# ### the branches step zero deletes ((R336)(5)): the push-b725-* branches b725's close made, by name, each read from the listings and
# ### `--merged` printed before the deletes, one per command, each its own message
DELETE = (('D:/relay', ('push-b725-closing', 'push-b725-preroot', 'push-b725-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b725-preroot', 'push-b725-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R336)(5): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'), ('D:/SIDE-explicit-formula', 'challenge-b720-h2-sign-iff-rh'),
                 ('D:/SIDE-lv-conservation', 'scratch-b724'), ('D:/SIDE-explicit-formula', 'keiper-b725'), ('D:/SIDE-explicit-formula', 'c2-b725'),
                 ('D:/SIDE-kernel', 'rebuild-b721'), ('D:/SIDE-lv-conservation', 'rebuild-b721'), ('D:/SIDE-archimedean', 'rebuild-b721'),
                 ('D:/SIDE-frobenius', 'rebuild-b721'), ('D:/SIDE-spinor', 'rebuild-b721'), ('D:/SIDE-rcurve', 'rebuild-b721'))

# ### the kernels: read; written only on the rebuild-b721 branches by (R336)(7) and the author's word (4)
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')


def _kernel_paths():
    """the kernels of data/b716_federation_pin_price.txt (1), as D:/<name>, read at import ((R336) PATHS)."""
    p = os.path.join(D, 'b716_federation_pin_price.txt')
    t = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return tuple('D:/' + m.group(1) for m in re.finditer(r'(?m)^  (SIDE-[A-Za-z0-9-]+)\s+HEAD ', t))


KERNEL_PATHS = _kernel_paths()
PATHS = ('D:/relay', PP, KERNEL_DIR, LV_DIR) + tuple(k for k in KERNEL_PATHS if k not in (KERNEL_DIR, LV_DIR))   # ### (R336)'s PATHS
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
# ### the wave 1 kernels at their own pins, (name, tag, the short commit) -- b721's (R331)(7), b725's (R335)(10)
WAVE1 = (('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-archimedean', 'v0.1.0', '8019d9d'),
         ('SIDE-frobenius', 'v0.1.0', '2efe9f2'), ('SIDE-spinor', 'v0.1.0', 'b235bc6'), ('SIDE-rcurve', 'v0.1.0', 'd5f33b4'))
CHECKPOINT_STATEMENTS = (('SIDE-archimedean', 'archimedean_forces_half'), ('SIDE-frobenius', 'indicial_forces_half'),
                         ('SIDE-spinor', 'spinor_forces_half'), ('SIDE-spinor', 'half_iff_centered_zero'), ('SIDE-rcurve', 'monotone_unique_zero'))
REBUILD_BRANCH = 'rebuild-b721'          # ### b721's branches, kept, (R336)(7)'s repair made on them alone
REBUILD_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-lv-conservation', 40706311269), ('SIDE-archimedean', 40706397470),
                ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404), ('SIDE-frobenius', 40713201832))   # ### b721's, each read by its id
AXIOM_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-archimedean', 40706397470), ('SIDE-frobenius', 40713201832),
              ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404))   # ### b725's (R335)(10): the five whose axiom step was diagnosed
AXIOM_DIAG = 'data/b725_axiom_diag.txt'  # ### the routes (R336)(7) and the author's word (4) take
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
DATA_STANDING = 'data/standing_clauses_v9.txt'   # ### v8 bound the act to d9739558; v9 from that commit, which landed it at Component 1 ((R336)(2)(v))
DATA_STANDING_V9 = 'data/standing_clauses_v9.txt'
ARM_TAGS = 'data/arm_tags.json'
REPO_VISIBILITY = 'data/repo_visibility.txt'
REGISTRATIONS = 'data/b725_registrations.txt'    # ### b726 registers no hypothesis ((R336) orders none; b725's the last, carried name)
REG_WALK_COMMIT = '15cb6cc4'                     # ### b721's H-C2-WALK commit (carried name; b725's walk read under it)
REG_COMMITS = (('data/b716_registrations.txt', 'dc5e808f'), ('data/b718_registrations.txt', '8146404b577dfee3e379d19e08e8595ab8824961'),
               ('data/b719_registrations.txt', '965cb8e84dc02192854512af53a29b1fbc2b80f5'), ('data/b720_registrations.txt', '54fc03d9'),
               ('data/b721_registrations.txt', 'e8c3dff40df43269b3f0c4b917baef7c96c0f649'),
               ('data/b725_registrations.txt', 'dc0d4133'))   # ### N2 (b725's row, its last amendment, the blob HEAD carries; b726 registers nothing)
REG_FILES = tuple(f for f, _c in REG_COMMITS)
PRED_B717 = 'data/b717_predictions.txt'
PRED_B717_COMMIT = 'f47d8ab5840d287bf63c1f0b59ba707ed85dbe07'
PREDICTIONS = PRED_B717
ONSETS_B717 = 'data/b717_onsets.txt'
REGISTRATIONS_NEW = 'data/b725_registrations.txt'
COEFF_BANKS = ('data/b711_coeffs.txt', 'data/b713_coeffs.txt', 'data/b717_coeffs.txt', 'data/b719_coeffs.txt', 'data/b720_coeffs.txt')
#   ### read not written (carried name); b725 wrote no coefficient bank
COMPUTE_BANKS = ('data/b726_price.txt', 'data/b726_standing_v160.txt', 'data/b726_root_row.txt', 'data/b726_c2.txt',
                 'data/b726_edition_diff.txt', 'data/b726_zenodo_read.json', 'data/b726_frontdoors.txt', 'data/b726_beurling_read.txt',
                 'data/b726_mechanisms.txt')
#   ### the banks of (R336)(2)-(7), each written by its component (the price table at step zero)
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt',
              'data/b725_read_calls.txt', 'data/b726_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b725 carried them
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b726'))
CHAIN_QUARTERS = (('b624', 'b631'), ('b632', 'b658'))   # ### (R336)(2)(vi): b2a split where b725's banked walks halve (repeat.quarters; b2a's run 575 s at b725)
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### set by the Edit tool when a component adds a standing arm
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', 'day1/Which_Structure_Confines_v2_4_0.md')   # ### the weight line, the corrigendum, the entry, the trail and the edition ((R336)(8)'s (W) list); no ERRATA entry ordered
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the re-cut's merge (kept for the kernel rows); the MANIFEST control's reference
#   ### is the commit the mirror is built at from v1.2.1
NEXT = ('the release sitting on the author’s word, the list of (R336)(5) as its agenda; then b727 ((R336)(10)), the research act: the onset '
        'successor from the six banked products and off18’s, M and A read from the computed form before any registration; the Beurling row’s '
        'instance if found; lambda_2’s two premises; W-ORD-VISIBILITY from H-INTERFERENCE’s table')
NEXT_ACT = 'b727'


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
ACT_CURRENT_COMMIT = '59216ce1'         # ### data/act_current.json for b726 committed alone, before any other git command ((R336)(8))
STEPZERO = 'ce435473'                   # ### b725's closing capture, committed alone ((R336)(8))
STEPZERO_STEPS = 'd6b9c2a9'             # ### b725's step-40 row, committed alone ((R336)(8))
STEPZERO_TABLE = 'f187e976'             # ### the terminal table regenerated and committed ((R336)(8))
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None
STEPZERO_REFUSALS = ()
STEPZERO_BANKS = 'bc253274'             # ### the step-zero banks and tools, committed together by explicit list (step 4)
STEPZERO_BANK_COMMIT = 'bc253274'       # ### the step-zero bank itself (data/b726_stepzero.txt), with the price table, in that commit
VISIBILITY_COMMIT = None
COMPUTE_TOOLS = ()                      # ### set by the Edit tool when a component seals a compute tool
REPAIRED_TOOLS = ()
REPAIRED_DATA = ()
# ### b721's trap (event 11): the standing part of the sealed list read from the directory, not a carried tuple
STANDING_FILES = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing')) if f == 'VERSION' or f.endswith('.py')))
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset, sealed by hash beside the act's tools
# ### the seven close tools are tools/standing/fold.py's renders of its templates (tools/standing/fold/<tool>.tpl) with the act's arms module
# ### (tools/acts/b726.py) -- every byte a render reads sealed beside the act's tools; report.tpl left out of the seal (b708's report row)
FOLD_FILES = tuple(sorted('standing/fold/' + f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing', 'fold')) if f.endswith('.tpl')
                          and f != 'report.tpl')) + ('acts/b726.py',)
NEW_TOOLS = NEW_TOOLS + FOLD_FILES
STANDING_VERSION = 'v1.6.0'             # ### (R336)(2)(iii)'s repairs landed v1.6.0 by a commit of their own (C1_STANDING)
STANDING_CHANGED = ()                   # ### the standing files (R336)(2) changes, set by the Edit tool when they land
STANDING_NEW = ()
# ### b725's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = 'e2246a8e'    # ### b725's closing, the act's relay base
B714_RECORD = '14593dda'     # ### b725's record commit (relay, the head line's)
B714_ROOT = 'd85513caeb001601649df5f7a5cf4b634e3db0c6a8d65db87be0ddac99a73d97'   # ### b725's root, data/act_roots.txt :104
B723_ROOT_BANKS = '34fee845'  # ### b725's root commit (step 37), the banks its root rode with
# ### later stages: the commits of the components, read from the logs after each was made (None until made)
C1_STANDING = '0dc805b2'                # ### (R336)(2)(iii): tools/standing/ v1.6.0
C1_STANDING_REPAIR = None
C1_RELAY = '5f46a6a3'                   # ### (R336)(2)(ii): b723's row on its branch, act_roots, the c1 route
C1_CORR = 'fe20cd09'                    # ### the corrigendum banks, the corrigenda row
C1_PP = 'e3818db7'                      # ### FINDINGS: b725 at its weight, the observation and the corrigendum for b725
WEIGHT_LINE, CORR_LINE = 11797, 11801   # ### FINDINGS: b725's weight line and the corrigendum for b725 (Component 1)
DIFFERS_LINE = None
ERRATA_LINE = None
C2_RELAY = '8b6a6c71'                   # ### (R336)(3): the C2 bank's commit, after the components' (the fields ran beside them)
C2_AMEND = ()
C2_PP = None
C3_RELAY = ('d49a7ba8',)                # ### (R336)(4)-(7): the edition's diff, the front-door list, the mechanism table, their tools
C3_PP = '2f3deb91'                      # ### (R336)(4): the edition, beside v2.3.1
C4_LV = None
C4_RUN = None
C4_PP = None
C4_RELAY = None
C5_RELAY = None
REG_COMMIT = 'dc0d4133'                 # ### b725's last registration commit (carried name; b726 registers nothing)
ORDERS = (142, 60, 42, 12, 28)          # ### b725's (R335)(4) triage, carried as read (data/b725_orders_triage.txt): DONE, NOT MET, MET, AUTHOR'S WORD
TRIAGE = 'data/b725_orders_triage.txt'
LV_SCRATCH_BRANCH = 'scratch-b724'      # ### b724's scratch branch of SIDE-lv-conservation, kept ((R336)(8))
LV_RUNS = (('SIDE-lv-conservation', 40964150574),)   # ### b725's one dispatch, read by its id (carried, not re-run)
LV_ROWS = 'data/b726_lv_rows.json'
CHALLENGE_BRANCH = 'challenge-b720-h2-sign-iff-rh'   # ### b720's, on SIDE-explicit-formula, standing, not merged, no tag
CHALLENGE_TIP = '3391647518cd37316a448b5013afb62a198fa6c6'
CHALLENGE_RUN = 40651875792
PIN_RUNS = (('SIDE-grh-transfer', 40652622018), ('SIDE-interfaces', 40652657325), ('SIDE-kernel', 40652692787),
            ('SIDE-lv-conservation', 40652727943), ('SIDE-simplicity', 40652762827), ('SIDE-trivium', 40652790458))   # ### b720's, read not re-run
PIN_BRANCH = 'pin-b718-de5ce8a9'   # ### b718's pin branches, left as banked ((R336)(8))
PIN_EXCLUDED = ('SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve', 'SIDE-cosmo')
PIN_HELD = ('SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium')
PIN_BUILDS = ('SIDE-simplicity',)
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PIN_TO_NEXT = ()
MAX_DISPATCHES = 18          # ### N1: (R336)(3)'s, eighteen at most
EF_DIR = 'D:/SIDE-explicit-formula'
EF_BASE = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'   # ### SIDE-explicit-formula's main, both branches cut from it, untouched (N5)
EF_BRANCHES = (('keiper-b725', 'f52e188c2409436337019ea0008d7352bde404c2'),   # ### b725's, kept
               ('c2-b725', 'ea95a8d07a0ffae2012d715d5e95194cbf4df1ad'))       # ### (R336)(3): the split c9add92f, the binder repair on it
EF_RUNS = (('(3) D=-15', 41147584871), ('(3) D=-15', 41148340840), ('(3) D=-20', 41148615288), ('(3) D=-24', 41149195356), ('(3) D=-40', 41149723199),
           ('(3) D=-35', 41149939848), ('(3) D=-52', 41150124566), ('(3) D=-51', 41150327748), ('(3) D=-88', 41150696282), ('(3) D=-91', 41151096621),
           ('(3) D=-123', 41151758237), ('(3) D=-115', 41152040078), ('(3) D=-148', 41152352459), ('(3) D=-232', 41152579553), ('(3) D=-187', 41152916381),
           ('(3) D=-235', 41153237700), ('(3) D=-267', 41153599031), ('(3) D=-427', 41154021667))   # ### each read by its id
DISPATCH_ROWS = 'data/b726_dispatch_rows.json'
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md')   # ### the two ledgers, the edition beside them read by G-PP-SCOPE ((R336)(8))
ERRATA_ID = None             # ### b726 files no ERRATA ((R336)(1)-(2): the corrigendum is b725's weight line, no ERRATA row)
ERRATA_IDS = ()
RETIRED_COUNT = 0
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list (the root answer's addition (b))
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b726_') and f.endswith('.py') and f != 'b726_report.py')) + NEW_TOOLS + COMPUTE_TOOLS
# ### the act's arms over its own banks: set before the lock by the Edit tool -- b725's list, the act shift G-R335-ENTERED to G-R336-ENTERED,
# ### G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0 ((R336)(2)(iv))
ACT_ARMS = ('G-ACT-CURRENT', 'G-ARM-TAGS', 'G-ARMS-RETIRED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED', 'G-CLOSING-DRY-STEP', 'G-COEFFS-LAW',
            'G-CORRIGENDUM-ENTERED', 'G-COUNT-ROUTE-PRICED', 'G-DELETES-ONE-BRANCH', 'G-DERIVATION-GRADED', 'G-DIFFERS-ERRATA', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-GUARD-HELD', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LISTINGS-BEFORE-CLAUSES',
            'G-MEMBRANE-WIRED', 'G-OFFSET-POST-HOC', 'G-POSTROOT-WRITES-NONE', 'G-PREDICTION-FIRST', 'G-R336-ENTERED',
            'G-REGISTRATIONS-FIRST', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED', 'G-SURGERY-CARRIED', 'G-TOUCH-READ',
            'G-WRITELIST-MIRROR-STATE')
