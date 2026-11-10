# -*- coding: utf-8 -*-
"""b751_worklist.py -- THE ACT'S DATA, UNDER (R361). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b751: LANE TWO, ACT ONE HUNDRED AND SEVENTY-EIGHT, THE LOCATED ZERO -- b750 AT ITS WEIGHT; THE CORRIGENDUM OPENING ON THE
### SUITE PARTS RUN OUT OF THEIR ORDER AND THE WRITES OUTSIDE THE (W) LIST; THE LITERATURE BANKED; THE PAPER'S SECTION 5 WRITTEN.
### No runner dispatch, no Lean file, no lean process on this host (N1); no Zenodo call (N5).
### Carried by diff from b750_worklist.py (data/b751_carry_worklist.txt); its stage one set at step zero with this act's figures by the
### seat's script (scratch wl751.py, each constant replaced whole by its name); later stages by the Edit tool.
### The act runs in the same session as b750 (6151c0de), one seat, after a context summary.
### b750 closed and pushed itself whole (relay 467a1968, PLACE-papers 88942b4), its closing step row committed before its closing push; its
### closing push capture and tools/mirror_prevbuild.json are this act's carried files ((R361)(3)), committed at step zero, each alone.
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
PRE_PP = '88942b4202bdb4528a44879f034217d70b776866'    # ### PLACE-papers main before the act's own commits: b750's record (the trail)
PRE_RELAY = '467a1968507a69dc75fb637fbac91e3a620f140a'  # ### relay main before the act's own commits: b750's closing step row
PRE_PP_REMOTE_AT_START = '88942b4'       # ### PLACE-papers remote main at the act's start (data/act_current.json, equal to local)
PRE_RELAY_REMOTE_AT_START = '467a1968'   # ### relay remote main at the act's start (the citation check's remote main row)
B718_RELAY_HEAD = '467a196'  # ### the names kept for the carried readers: the previous act's last relay head (b750's closing)
B718_PP_HEAD = '88942b4'     # ### the previous act's last PLACE-papers head (b750's record)
DATE = '2026-11-10'
SESSION_ID = '6151c0de-d2ec-42cf-a477-c48b99346e01'   # ### the transcript's name
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/0fa2f3b7e932577a/6151c0de-d2ec-42cf-a477-c48b99346e01/scratchpad'   # ### this session's scratchpad as the harness names it after the summary
HOLD = 2560
ANCHOR = 'RULING (R361) BEGIN'           # ### the act's capture anchor, as data/act_current.json
RULING_ANCHOR = 'RULING (R361) BEGIN'    # ### the ruling's BEGIN line, the citation tool's ferry source
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = '6151c0de-d2ec-42cf-a477-c48b99346e01'   # ### b750 ran in this session (from 'RULING (R360) BEGIN' to its closing); b751 follows it in the same session after a context summary
PREV_ANCHOR = 'RULING (R360) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b751_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 14627          # ### FINDINGS: b750's entry head (at 88942b4)
B711_WEIGHT = 14536         # ### FINDINGS: b749's weight line (b750's Component 1)
B711_CORRIGENDUM = 14538    # ### FINDINGS: b750's corrigendum for b749
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 18084          # ### OPEN_TRAILS: b750's trail record (PLACE-papers 88942b4)
B711_FACE = 'data/b750_registration_2026-11-09.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-11-09-b750.zip'   # ### b750's export, built after b750's last PLACE-papers push, CLEAN 3/3
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
ORDER_LEDGER_SPLIT = 14680  # ### OPEN_TRAILS: W-ORD-LEDGER-SPLIT-RESOLVER (b680), (R361)(3)
TRAIL_ORDERS = 18096        # ### OPEN_TRAILS: the last open-orders line, b750's, written from the generator's output
TRAIL_RESOLVED = 18126      # ### OPEN_TRAILS: b750's items for the author's strike, in its trail
TRAIL_RETIRED = 18110       # ### OPEN_TRAILS: b750's count line of the author's prompts
#   ### b751 step zero: the carry brought b749's lines (18050/18076/18062) under these names; set to b750's here, each read from OPEN_TRAILS at 88942b4 (b750's trail :18084-:18132)
WATCH_LINE = 16126          # ### OPEN_TRAILS: W-ORD-QUASI-RH-FIELD-WATCH, annotated at b718's C6
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row
INSTRUMENTS = 'phase1.5/method/INSTRUMENTS.md'   # ### PLACE-papers' instruments document, its last entry I-108 (b750)
INSTRUMENTS_LAST = 109   # ### I-109 entered at b750 ([E])

# ### (R361)(3): the five records, in the order the ruling names them: (row, kernel, Zenodo record, the sitting row's line in data/b736_sitting.txt)
TIER3 = ((104, 'SIDE-cosmo', '19938009', 1095), (105, 'SIDE-effects', '19938005', 1105), (106, 'SIDE-trivium', '19938003', 1115),
         (107, 'SIDE-interfaces', '19931797', 1125), (108, 'SIDE-kernel', '21520474', 1135))
TIER3_BANK = 'data/b739_tier3.txt'                  # ### b751: b739's, read not written (no Zenodo field touched, (R361)(5)); the carry shifted it to b750's, which does not exist
READBACK_BANK = 'data/b739_zenodo_readback.json'

# ### the branches step zero deletes ((R361)(5)): the push-b750-* branches b750's close made, by name, each read from the listings and
# ### `--merged` printed before the deletes, one per command, each its own message
DELETE = (('D:/relay', ('push-b750-closing', 'push-b750-preroot', 'push-b750-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b750-preroot', 'push-b750-record')))   # ### (R361)(2): the five; b750 made no kernel branch
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### carried: NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'), ('D:/SIDE-explicit-formula', 'challenge-b720-h2-sign-iff-rh'),
                 ('D:/SIDE-lv-conservation', 'scratch-b724'), ('D:/SIDE-explicit-formula', 'keiper-b725'), ('D:/SIDE-explicit-formula', 'c2-b725'),
                 ('D:/SIDE-kernel', 'rebuild-b721'), ('D:/SIDE-lv-conservation', 'rebuild-b721'), ('D:/SIDE-archimedean', 'rebuild-b721'),
                 ('D:/SIDE-frobenius', 'rebuild-b721'), ('D:/SIDE-spinor', 'rebuild-b721'), ('D:/SIDE-rcurve', 'rebuild-b721'),
                 ('D:/SIDE-explicit-formula', 'detect-b729'), ('D:/SIDE-explicit-formula', 'zq-b730'))   # ### (R361)(4) names c2-b725, keiper-b725, detect-b729, zq-b730

# ### the kernels: read; written only on the rebuild-b721 branches by (R361)(7) and the author's word (4)
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')


def _kernel_paths():
    """the kernels of data/b716_federation_pin_price.txt (1), as D:/<name>, read at import ((R361) PATHS)."""
    p = os.path.join(D, 'b716_federation_pin_price.txt')
    t = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return tuple('D:/' + m.group(1) for m in re.finditer(r'(?m)^  (SIDE-[A-Za-z0-9-]+)\s+HEAD ', t))


KERNEL_PATHS = _kernel_paths()
PATHS = ('D:/relay', PP, KERNEL_DIR, LV_DIR) + tuple(k for k in KERNEL_PATHS if k not in (KERNEL_DIR, LV_DIR))   # ### (R361)'s PATHS
EF_MAIN = '8fbab45d8a966dca53d42448e33927d885fd4ea3'    # ### SIDE-explicit-formula's main after [A4]: badacccb + README.md alone ((R361)(6))
LV_MAIN = '305a87c9e09c45cc8a935b1065f26f929634c707'    # ### SIDE-lv-conservation's main at the sitting's [41] (README.md alone, (R361)(3))
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
# ### the wave 1 kernels at their own pins, (name, tag, the short commit) -- b721's (R331)(7), b750's (R360)(10)
WAVE1 = (('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-archimedean', 'v0.1.0', '8019d9d'),
         ('SIDE-frobenius', 'v0.1.0', '2efe9f2'), ('SIDE-spinor', 'v0.1.0', 'b235bc6'), ('SIDE-rcurve', 'v0.1.0', 'd5f33b4'))
CHECKPOINT_STATEMENTS = (('SIDE-archimedean', 'archimedean_forces_half'), ('SIDE-frobenius', 'indicial_forces_half'),
                         ('SIDE-spinor', 'spinor_forces_half'), ('SIDE-spinor', 'half_iff_centered_zero'), ('SIDE-rcurve', 'monotone_unique_zero'))
REBUILD_BRANCH = 'rebuild-b721'          # ### b721's branches, kept, (R361)(7)'s repair made on them alone
REBUILD_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-lv-conservation', 40706311269), ('SIDE-archimedean', 40706397470),
                ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404), ('SIDE-frobenius', 40713201832))   # ### b721's, each read by its id
AXIOM_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-archimedean', 40706397470), ('SIDE-frobenius', 40713201832),
              ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404))   # ### b750's (R360)(10): the five whose axiom step was diagnosed
AXIOM_DIAG = 'data/b729_axiom_diag.txt'  # ### the routes (R361)(7) and the author's word (4) take
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
DATA_STANDING = 'data/standing_clauses_v9.txt'   # ### v8 bound the act to d9739558; v9 from that commit, which landed it at Component 1 ((R361)(2)(v))
DATA_STANDING_V9 = 'data/standing_clauses_v9.txt'
ARM_TAGS = 'data/arm_tags.json'
REPO_VISIBILITY = 'data/repo_visibility.txt'
PLAN_BANK = 'data/b744_zetabox_plan.txt'              # ### (R361)(2): W-ORD-ZETA-BOX's plan bank (b744's), read for the navigator's read, its md5 printed at step zero, no row rewritten
POSCONTROL_PLAN = 'data/b744_poscontrol_plan.txt'     # ### (R361)(2): W-ORD-POSITIVE-CONTROL's plan bank (b744's), read the same way
PLAN_BANKS = (POSCONTROL_PLAN, PLAN_BANK)             # ### the order the discharges are entered: the positive control first
PLAN_MD5S = {'data/b744_poscontrol_plan.txt': 'b72ad7bbe28693a1192cfa60329fc607',   # ### b750's step-zero print, LF, 137 lines; re-printed by this act's citation check
             'data/b744_zetabox_plan.txt': 'ef777cc24752911990d56d2214fe38b6'}      # ### 183 lines
CONTROLS_BANK = 'data/b745_controls.txt'              # ### (R361)'s read-first list: b745's result bank (pc_online and the generic theorem :96-:127), read not written
CONTROLS_NOTES = 'data/b745_controls_notes.txt'       # ### b745's notes, read not written
SECTION_FILE = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'   # ### (R361)(2): the paper, section 2 written by one PLACE-papers write on the author's pass
SECTION_BANK = 'data/b751_section5.txt'               # ### (R361)(2): the paper's §5 bank, the draft as put at [S5], written this act (Component 2)
SECTION4_BANK = 'data/b748_section4.txt'              # ### b748's §4 bank, read not written
SECTION1_BANK = 'data/b747_section2.txt'              # ### b747's section bank (§2), read not written
INTEGRATION_DRAFT = 'data/b746_integration_draft.txt' # ### b746's canon text for the stages, entered at b750 as XXIII, read not written
ORDER_DRAFT = 'data/b746_order_draft.txt'             # ### (carried name) b746's order draft, read not written; no order entered this act
READBACK_747 = 'data/b747_zenodo_readback.txt'        # ### b747's read-back, read not written; no Zenodo call this act ((R361)(6))
RULES_747 = 'data/b751_rules.txt'                     # ### (R361)(3): the seat's reading of the corrigendum's repairs, each for the author's strike
REGISTRATIONS = PLAN_BANK                             # ### (carried name)
PREV_BUILD_BANK = 'data/b745_controls.txt'            # ### b745's result bank (b750 built nothing)
PREV_BUILD_MD5 = None                                 # ### printed by the citation check at step zero
PREV_STATEMENTS_BANK = 'data/b744_zetabox_plan.txt'   # ### b744's other plan
STATEMENTS_BANK = PLAN_BANK                           # ### (carried name)
C7_PLAN = STATEMENTS_BANK
S6_PLAN = STATEMENTS_BANK
BUILD_BANK = CONTROLS_BANK                            # ### (carried name) the act's last result bank
NOTES_BANK = CONTROLS_NOTES
REG_WALK_COMMIT = '15cb6cc4'                     # ### b721's H-C2-WALK commit (carried name; b750's walk read under it)
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
#   ### read not written (carried name); b750 wrote no coefficient bank
COMPUTE_BANKS = ('data/b751_standing_v1310.txt', 'data/b751_literature.txt', 'data/b751_section5.txt',
                 'data/b751_address_scan.txt')
#   ### the banks of (R361)(2)-(5), each written by its component
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt',
              'data/b729_read_calls.txt', 'data/b730_read_calls.txt', 'data/b750_read_calls.txt', 'data/b751_read_calls.txt')

# ### THE SUITE'S PARTS: ten, as b750 split them under (R360)(2)(vi) and b675 rules row (2) (standing-a in two, G-NO-SORRY-MAIN's kernels
# ### halved, and the chain's first half in four, b2a-b2d); data/act_current.json committed them ten at b751's step zero (22f59d27), no
# ### component splitting them this act, so PARTS_AT_STEP_ZERO is PARTS
PARTS = ('standing-a1', 'standing-a2', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d', 'standing-b3', 'act')
PARTS_AT_STEP_ZERO = PARTS
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b751'))
CHAIN_QUARTERS = (('b624', 'b627'), ('b628', 'b631'), ('b632', 'b635'), ('b636', 'b658'))   # ### carried from b750
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### set by the Edit tool when a component adds a standing arm
SHARED_APPENDED = ('data/b675_corrigenda.txt',)   # ### (R361)(2): the corrigenda row
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md')   # ### (R361)(2), (6): the paper's §5 the one PLACE-papers write on a passed item, with the ledger entries
#   ### (R361)(1)-(6) and the ferry's (N5): the weight line, the corrigendum entry and the FINDINGS entry; OPEN_TRAILS for the order of (4)
#   ### and the trail; the paper for section 2 on the author's pass ((R361)(2)); no door or record edited
PP_WRITTEN = PP_EDITED
PP_NEW = ()
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the re-cut's merge (kept for the kernel rows); the MANIFEST control's reference
#   ### is the commit the mirror is built at from v1.2.1
NEXT = 'the attribution order`s plan act, as the author named it at b750`s root ((R361)(7)), confirmed or renamed at this act`s root, opening on I-109`s figure and the class-group signature of the negative n; section 6 after it'
NEXT_ACT = 'b752'


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
ACT_CURRENT_COMMIT = '540920f6'         # ### data/act_current.json for b751 committed alone through the one-call tool ((R361)(5)), the scan in the call; its row step 1
STEPZERO = '78fd4424'             # ### b750's closing push capture, committed alone ((R361)(3)); its row step 2, in the commit's call
STEPZERO_STEPS = None             # ### b750's closing step row was committed by b750 itself (467a1968) before its closing push: nothing carried
STEPZERO_TABLE = None             # ### b750 left no terminal table uncommitted
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None   # ### tools/mirror_prevbuild.json of b750: a CRLF-only difference from HEAD's blob, restored through the tool at step zero, nothing to commit
STEPZERO_REFUSALS = ()
STEPZERO_BANKS = '92810ff9'      # ### step zero's banks and carried tools, one commit (data/b751_stepzero.txt among them; step row 3)
STEPZERO_BANK_COMMIT = STEPZERO_BANKS
STEPZERO_ANSWERS = None
STEPZERO_ANSWERS_FULL = None   # ### the same, as each dispatch row's licence names it
# ### N2: each generator commit (relay) before the zq-b730 commit holding the modules it generated
GEN_COMMITS = ()   # ### b751: no generator run, no Lean file written ((R361)(8))
GEN_COMMITS_B745 = (('04e7f854', '32bad89a'), ('32a5c72a', '32bad89a'), ('32a5c72a', '1e658870'))   # ### (R361)(4)(c): the Z4 generator's relay commits, each before the zq-b730 commit it fed (Signs.lean at t = 16, then 16 and 12)
GEN_MD5 = {'Signs': '4ef0a0f5606052abf21c797a9aba64a2'}   # ### the generator's output at 32a5c72a (`<out> 16 12`), Signs.lean at zq-b730's tip by md5
GEN_MD5_PREV = {'FrontierData': 'c8e320f9db1a12622cc147555496cf11', 'Nodes0': '7cb04ecfd3649a1daf5633de691df670',   # ### b742's generator's output at 3194b6eb (carried name, read not run)
                'Nodes1': 'a20f1f00a156e59e97f841beb8d89a76', 'Nodes2': 'efff8c97b5f9879bcf12e3f79628dc64',
                'Nodes3': '09de4381169541faf5f0066bf66905e7', 'NodesF': 'd37bbfbb8c81165521b77de16022069a'}
GENERATOR = 'tools/b745_zbgen.py'   # ### b745's (carried name, read not run): Signs.lean generated from it (md5 ac82341c at 32a5c72a); the carry shifted it to b751's, which does not exist
VISIBILITY_COMMIT = None
COMPUTE_TOOLS = ()                      # ### set by the Edit tool when a component seals a compute tool
REPAIRED_TOOLS = tuple(p[len('tools/'):] for p in json.load(io.open(os.path.join(D, 'act_current.json'), encoding='utf-8'))['shared_edits'])
#   ### (R361)(2), b750 event (2): read from data/act_current.json, the one hand list, which G-ACT-CURRENT reads against git; sealed before the suite runs (b696's form)
REPAIRED_DATA = ()
# ### b721's trap (event 11): the standing part of the sealed list read from the directory, not a carried tuple
STANDING_FILES = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing')) if f == 'VERSION' or f.endswith('.py')))
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset, sealed by hash beside the act's tools
# ### the seven close tools are tools/standing/fold.py's renders of its templates (tools/standing/fold/<tool>.tpl) with the act's arms module
# ### (tools/acts/b751.py) -- every byte a render reads sealed beside the act's tools; report.tpl left out of the seal (b708's report row)
FOLD_FILES = tuple(sorted('standing/fold/' + f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing', 'fold')) if f.endswith('.tpl')
                          and f != 'report.tpl')) + ('acts/b751.py',)
NEW_TOOLS = NEW_TOOLS + FOLD_FILES
STANDING_VERSION = 'v1.30.0'            # ### entering; (R361)(3)'s repairs land as v1.31.0 by a commit of its own (C1_STANDING) with data/b751_standing_v1310.txt
STANDING_VERSION_ENTERING = 'v1.30.0'
LEAN_TREES = (('D:/SIDE-explicit-formula', '14ca5725'), ('D:/SIDE-explicit-formula/.lake/packages/mathlib', 'de5ce8a9'))   # ### zq-b730 at the tag's commit
# ### v1.18.0, (R361)(2)(ii): the act's banks whose comparative sentences the citation check reads, and a reading row for each word (tools/standing/cites.py
# ### comparative_rows); set by the Edit tool as Components 2-4 write the banks, before the lock
COMPARATIVE_BANKS = ('data/b751_corrigendum.txt', 'data/b751_literature.txt', 'data/b751_section5.txt',
                     'data/b751_defects.txt')
COMPARATIVE_ROWS = ()   # ### comparative word in them ("at least" excepted by the reader), so no reading row; the check reads the three for one
#   ### the trees the ruling's Lean paths are read against: zq-b730's tip, and Mathlib at its pin (the ferry's "Mathlib at the pin: Analysis/Complex/AbsMax.lean :405, ...")
STANDING_CHANGED = ('VERSION', 'carry.py', 'commit.py', 'fold/checks.tpl', 'hook.py', 'repeat.py', 'rootprompt.py', 'standingdry.py')   # ### v1.31.0's changed files (e46f9e9d)
STANDING_NEW = ('limits.py', 'linematch.py', 'v1310.py', 'wlist.py')       # ### v1.31.0's new files (e46f9e9d)
# ### b750's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = '467a1968'    # ### b750's closing (its step row), the act's relay base
B714_RECORD = 'cb732c95'     # ### b750's record commit (relay)
B714_ROOT = 'fbd3c1d6dd1a0bc1887bd67cc5f4c3adcdeea62c48a16cbf7e41e075704fcad3'   # ### b750's root, data/act_roots.txt's last row
B723_ROOT_BANKS = 'c671c4cf'  # ### b750's root commit, the banks its root rode with
# ### later stages: the commits of the components, read from the logs after each was made (None until made)
C1_STANDING = 'e46f9e9d'           # ### tools/standing/ v1.31.0 by a commit of its own, its controls bank data/b751_standing_v1310.txt ((R361)(3)); step row 4
C1_STANDING_REPAIR = None          # ### none in Component 1
C4_STANDING = None                 # ### none yet
C1_RELAY = None                    # ### the c1 route, the corrigendum banks, the corrigenda row; set after it is made
C1_CORR = C1_RELAY
C1_RULES = C1_STANDING             # ### data/b751_rules.txt committed with v1.31.0
C1_PP = '42206b44'                 # ### PLACE-papers: FINDINGS -- b750 at its weight (:14667) and the corrigendum for b750 (:14669); step row 5
C1_TAG_PP = ()                     # ### (carried name) no tag note this act
C1_DISCHARGE_PP = ()               # ### (carried name) no discharge this act
C2_TOOL = None                     # ### (carried name) no driver this act
WEIGHT_LINE, CORR_LINE = None, None   # ### FINDINGS: b750's weight line and the corrigendum for b750 (Component 1); set after it is made
DIFFERS_LINE = None
ERRATA_LINE = None
C2_PLAN_FIRST = None         # ### (carried name) Component 2's first commit: the section bank (definitions printed from the tree)
C2_RELAY_ALL = ()   # ### Component 2's relay commits (the literature bank, the section bank, the sitting row); set after made
C2_RELAY = None   # ### the last of them; set after made
C2_AMEND_RELAY = None        # ### no amendment this act
C2_AMEND_PP = C1_TAG_PP      # ### (carried name)
C2_PP = ()               # ### (R361)(2): the paper's §5, one PLACE-papers write on [S5]'s pass; set after made
PRICE_LINE = 17400
DOORS_COMMIT = None
MECH_COMMIT = None
FRONTDOORS_COMMIT = None
COUNT_BANK = None
PRINT_COMMIT = None        # ### (carried name) the commit carrying the act's section bank (C2_RELAY)
PLAN_MD5 = 'ef777cc24752911990d56d2214fe38b6'   # ### data/b750_zetabox_plan.txt's md5, printed at step zero (PLAN_MD5S), unedited
C2_AMEND = ()
SITTING_PP = C2_PP    # ### (R361)(2): the sitting's PLACE-papers writes
SITTING_KERNEL = None # ### no kernel written this act ((R361)(5))
SITTING_GH = ()       # ### no description written
SITTING_ITEMS = 1          # ### (R361)(2)(vi): one sitting item, [S5], in b736's form
# ### b750's objects (its sitting, (R360)(2)), carried names, read not written at b751; b751 step zero: the carry's shift of the two paths set back to b750's
AGENDA_COMMIT = '7ce3e6ea'                       # ### b750's agenda, eleven items with every draft, before the first item (b750 step row 7)
CQ_GEN = ('a1655706', 'tools/b750_cq_sign.py', '789afca8211cb39b4cc890ce5cb9daae')   # ### b750 [E]'s generator, committed before its run (b750 step row 13)
CQ_BANK = ('56ddafa5', 'data/b750_cq_sign.txt')   # ### b750 [E]'s bank, its controls before its figure (b750 step row 14)
CQ_FOOT = ('NEGATIVE 102 ; THE SMALLEST NEGATIVE n = 48, cQ = -7.742402021816 ; WITHIN 1e-40 OF ZERO 2498 (EXACTLY ZERO 2498), COUNTED NEITHER WAY ; '
           'NONNEGATIVE 399 ; THE LARGEST |cQ| 190.565466363 AT n = 2808 ; CONTROLS (K1)-(K4) ALL AS WANTED')
SITTING_COMMIT = '00dc4267'                      # ### the sitting record with the answers pair (step row 20)
# ### the passed items' PLACE-papers writes in order: (item, commit, the one file, lines added, lines removed), as git show --numstat printed them
ITEM_PP = (('[A1]', '7fbaff0d', 'phase1.5/method/THE_METHOD_CANON.md', 38, 0), ('[A2]', 'c3def6fd', 'phase1.5/method/THE_METHOD_CANON.md', 4, 0),
           ('[B1]', 'fd842c0f', 'README.md', 1, 1), ('[B2]', 'c7bf1443', 'README.md', 6, 0), ('[C]', '510eeea9', 'REGISTRY.md', 2, 0),
           ('[E]', '90804717', 'phase1.5/method/INSTRUMENTS.md', 6, 0), ('[F1]', '6fc025a1', 'SPIRAL_MAP.md', 1, 0),
           ('[F2]', '0dc0acb3', 'day1/Which_Structure_Confines_v2_4_0.md', 2, 0), ('[G1]', '00188c31', 'ERRATA.md', 14, 0), ('[G2]', '2d145638', 'ERRATA.md', 14, 0))
SITTING_STATES = {'[A1]': 'PASS', '[A2]': 'PASS', '[B1]': 'PASS', '[B2]': 'PASS', '[C]': 'PASS', '[D]': 'KEEP', '[E]': 'PASS',
                  '[F1]': 'PASS', '[F2]': 'PASS', '[G1]': 'PASS', '[G2]': 'PASS'}
C3_RELAY = ()              # ### Component 3 ((R361)(4)): the line's bank data/b751_line.txt; set after made
ZENODO_BANK = None   # ### no Zenodo call this act ((R361)(6))
ROUTES_BANK = 'data/b747_zenodo_routes.txt'     # ### b747's routes bank, read not written
INTEGRATION_DRAFT_MD5 = '9e760351971eab06b176176dc02643ab'   # ### data/b746_integration_draft.txt carried unchanged (its md5, last committed c4d044f3)
C3_ORDER_PP = None   # ### (carried name) NOT READ for the entered/carried word from v1.27.0 ((R361)(3)(i)): the composer reads the order commit's presence in the git log
C1_ORDER_PP = None         # ### no order entered this act
SITTING_COMMITS = ()
C3_PP = None         # ### (carried name) no INTEGRATION line written apart from the entry this act
C4_LV = None
C4_RUN = None
C4_PP = None
C4_RELAY = None
C5_RELAY = None
REG_COMMIT = C2_RELAY    # ### b751: the section bank's commit, with the prints it cites
ZEROS_REG_COMMIT = REG_COMMIT
ORDERS = (142, 60, 42, 12, 28)          # ### b750's (R360)(4) triage, carried as read (data/b729_orders_triage.txt): DONE, NOT MET, MET, AUTHOR'S WORD
TRIAGE = 'data/b729_orders_triage.txt'
LV_SCRATCH_BRANCH = 'scratch-b724'      # ### b724's scratch branch of SIDE-lv-conservation, kept ((R361)(8))
LV_RUNS = (('SIDE-lv-conservation', 40964150574),)   # ### b750's one dispatch, read by its id (carried, not re-run)
LV_ROWS = 'data/b751_lv_rows.json'
CHALLENGE_BRANCH = 'challenge-b720-h2-sign-iff-rh'   # ### b720's, on SIDE-explicit-formula, standing, not merged, no tag
CHALLENGE_TIP = '3391647518cd37316a448b5013afb62a198fa6c6'
CHALLENGE_RUN = 40651875792
PIN_RUNS = (('SIDE-grh-transfer', 40652622018), ('SIDE-interfaces', 40652657325), ('SIDE-kernel', 40652692787),
            ('SIDE-lv-conservation', 40652727943), ('SIDE-simplicity', 40652762827), ('SIDE-trivium', 40652790458))   # ### b720's, read not re-run
PIN_BRANCH = 'pin-b718-de5ce8a9'   # ### b718's pin branches, left as banked ((R361)(8))
PIN_EXCLUDED = ('SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve', 'SIDE-cosmo')
PIN_HELD = ('SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium')
PIN_BUILDS = ('SIDE-simplicity',)
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PIN_TO_NEXT = ()
MAX_DISPATCHES = 0         # ### N1: no runner dispatch this act
MAX_C2, MAX_KEIPER = 0, 0
EF_DIR = 'D:/SIDE-explicit-formula'
EF_BASE = '8fbab45d8a966dca53d42448e33927d885fd4ea3'   # ### SIDE-explicit-formula's main entering the act (b743's [A4], README alone)
EF_MAIN_AFTER = EF_BASE   # ### unmoved: no kernel's main is touched ((R361)(6))
ZQ_BRANCH = 'zq-b730'
ZQ_ENTERING = '1e6588703732435b34d840bbbb840225932c9b6b'   # ### b751: zq-b730 entering at b750's tip (SPZ3), unmoved this act ((R361)(8))
ZQ_ENTERING_B745 = '14ca572560f50378a6e4715e35cba0351e5f105d'   # ### b750's entering tip, the tag's commit
ZQ_TAG = ('v0.38', '21c6edafa047635112c9ccd4fad14c56d5a2fa4f', '14ca572560f50378a6e4715e35cba0351e5f105d')   # ### (R361)(3): name, tag object, peel read back
#   ### at the remote 2026-11-07T15:09:55Z (data/b751_SIDE-explicit-formula_v0.38_push_out.txt); the series v0.1-v0.37 read by ls-remote --tags, the next v0.38
ZQ_TIP = '1e6588703732435b34d840bbbb840225932c9b6b'   # ### b751: unmoved, b750's last Lean commit on zq-b730 (W-ORD-ZETA-BOX BUILT, SPZ3); no Lean commit this act
ZQ_FIRST = 'eb097190ffab325cd7ee8da5f9879210cfcc7eb1'   # ### the first Lean commit of this act (P1-P5)
ZQ_COMMITS = ()   # ### b751: none
ZQ_COMMITS_B745 = ('eb097190ffab325cd7ee8da5f9879210cfcc7eb1', '3639d984d76f724cd4406b5e166d75d7b15fe13b', 'ae959dedcaa19c63fdbac71b871989567aca91f5',
              'ef86297462f6b90218ee4ee665b1d7f4a3fdfa0f', '32bad89a81f6051f7c4e4dd56d800d9861a0922f', '1e6588703732435b34d840bbbb840225932c9b6b')   # ### this act's: P1-P5 ; R1 (the print list's order) ; Z1-Z3 ; R2 + Instr ; Signs t=16 ; Signs 16+12 + Box
ZQ_COMMITS_B742 = ('280b28b3935854f8c71e37480ee9b88dfeb60922', '11bb0125fa08eccc78f6a1a6d415201438973f45', '5d3136a39ea9b671b60118e1424e645f89956ea7',
                   '4c04916c8541f1ee2267059a8fa0396364f1eb5c', 'c2d4f29ce84d321814b223a7e275e0653161b4d4', '14ca572560f50378a6e4715e35cba0351e5f105d')   # ### b750's six, read by the discharge
ZQ_COMMITS_B741 = ('f2de6efb669405b5e6ed270e4a82e3bc6effa500', 'de4810da5d3cfc524002630959b32e4ebc30ce66', '47f5afb3f1b40a8525ac45eba0f1bf04fe2ed155',
              '42cb968b8ce35bb024bca8995a743a809c19409e', 'c9ad907454b785b75ad2142e1dcdf9a4797cfd0c', '3329eaa106cc24891ed55374afcd4ca4f7fe33d8')   # ### T ; G1+G2 ; repairs+G4 ; G3+G5 ; cast repair ; generator repair
ZQ_COMMITS_B740 = ('8c6ec8d12d97bece1de8dab10511add9d97382d0', '6b068a0db2ff1451e9da7bff82fe8fd66a8dad38', 'ba318a0b67fd95164623e4fdf109eb5d042697fa')   # ### b750's S5c ; S5d with S5c's fix ; S5d's fix
ZQ_SP1 = None
ZQ_SP3 = '3329eaa106cc24891ed55374afcd4ca4f7fe33d8'   # ### b750: SP3 REACHED here (dispatch 6, run 41940815524)
ZQ_SP4 = '14ca572560f50378a6e4715e35cba0351e5f105d'   # ### b751: SP4 REACHED here (dispatch 7, run 42068096322)
ZQ_MODULES = ('Xi', 'Landau', 'Heights', 'Contour', 'ZeroSum', 'FullLine', 'Lines', 'Main')   # ### the build's eight, under Schema/ZQ/EF
ZQ_OFFZERO_MODULES = ('Box', 'Diff', 'MinModulus', 'Carrier', 'Main', 'Split', 'Tail', 'IncGamma', 'Elem', 'Time', 'Series', 'Sums', 'GammaVal', 'Shells', 'Centre',
                      'Interp', 'Frame', 'Strip', 'Amplify', 'NodeBase', 'Omega', 'Nodes0', 'Nodes1', 'Nodes2', 'Nodes3', 'NodesF', 'FrontierData',
                      'Frontier', 'SP4')   # ### under Schema/ZQ/OffZero; b751 adds S6's fourteen
ZQ_FILES = ()   # ### b751: none
ZQ_FILES_B745 = ('SIDEExplicitFormula/Schema/Wide/PositiveControl.lean',) + tuple('SIDEExplicitFormula/Schema/ZetaBox/%s.lean' % m for m in ('Box', 'Instr', 'Line', 'Signs', 'Split', 'Tail')) + ('print_targets.txt',)   # ### zq-b730's diff against its entering tip
ZQ_FILES_B742 = tuple('SIDEExplicitFormula/Schema/ZQ/OffZero/%s.lean' % m for m in ('Amplify', 'Frame', 'Frontier', 'FrontierData', 'Interp', 'NodeBase',
                 'Nodes0', 'Nodes1', 'Nodes2', 'Nodes3', 'NodesF', 'Omega', 'SP4', 'Strip')) + ('print_targets.txt',)   # ### b750's diff against 3329eaa1 at 14ca5725
ZQ_FILES_B741 = ('SIDEExplicitFormula/Schema/ZQ/OffZero/Centre.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/GammaVal.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/Series.lean',
            'SIDEExplicitFormula/Schema/ZQ/OffZero/Shells.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/Sums.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/Time.lean',
            'print_targets.txt')   # ### zq-b730's diff against ba318a0b at 3329eaa1
ZQ_FILES_B740 = ('SIDEExplicitFormula/Schema/ZQ/OffZero/Elem.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/IncGamma.lean', 'print_targets.txt')   # ### b750's diff against 602cd401
ZQ_MODULES_B730 = ('Lattice', 'Theta', 'FEPair', 'Continuation')   # ### the names the carried sections read, until each section is set for this act
ZQ_ZEROS_FIRST, ZQ_LOGDERIV_TIP = None, None
ZQ_LOGDERIV_MODULES, ZQ_ZEROS_MODULES = (), ()
MAX_LOGDERIV, MAX_ZEROS = 0, 0
EF_BRANCHES = (('keiper-b725', '01fd33c2d7dc62d4702b075de3dda9253c5c2f87'),   # ### (R361)(4): the gamma_1 bound
               ('c2-b725', '0395f15d3b2906716ccb1f09ca24171d7a921210'),       # ### (R361)(3): the theorem, built whole at this tip
               ('detect-b729', '1023301c89ab16f8d437b2a1f08a824bc95b6b0e'),   # ### b729's (R339)(5): the statement alone, not compiled; kept, unmoved
               (ZQ_BRANCH, ZQ_TIP))                                           # ### (R361)(3)-(4): the fields
EF_BRANCHES_ENTERING = ('01fd33c2d7dc62d4702b075de3dda9253c5c2f87', '0395f15d3b2906716ccb1f09ca24171d7a921210', '1023301c89ab16f8d437b2a1f08a824bc95b6b0e', ZQ_ENTERING)   # ### the four entering the act
EF_RUNS = ()   # ### N1: no runner dispatch this act
EF_RUNS_B745 = (42388001562, 42388609600, 42391254295, 42392017104, 42393018408, 42393914259)   # ### N1: this act's dispatches, each read by its run id ((R361)(4)(c)): KERNEL (print stopped at maxErrors), KERNEL (13 names printed), BREAKS (lp_conj), KERNEL (SPZ1), KERNEL (SPZ2), KERNEL (SPZ3)
EF_RUNS_B742 = (42054839204, 42056405331, 42058361986, 42061332755, 42062848400, 42065597154, 42068096322)   # ### b750's seven, read not re-run; the last the SP4 grade run
EF_RUNS_B741 = (41931918742, 41935365948, 41936644993, 41938300160, 41939524029, 41940815524)   # ### b750's six: KERNEL (timing), BREAKS, KERNEL, BREAKS, BREAKS, KERNEL (SP3)
EF_RUNS_B740 = (41854903335, 41857376723, 41859346843)   # ### b750's three: BREAKS, BREAKS, KERNEL, read not re-run
EF_RUNS_B738 = (41732413170, 41732882564, 41733411736, 41734667160, 41735082430, 41736472780)   # ### b738's first six (of eleven), read not re-run
ZQ_RUN = 41483457057   # ### b737's grade run, the discharge's, read not re-run
EF_RUNS_B731 = (41371666217, 41372597450, 41373409167, 41374121055, 41374814817)   # ### b731's five, read not re-run
DISPATCH_ROWS = 'data/b751_dispatch_rows.json'
ERRATA_ID = None   # ### no erratum this act
ERRATA_IDS = ()   # ### no erratum this act
RETIRED_COUNT = 0
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list (the root answer's addition (b))
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b751_') and f.endswith('.py') and f != 'b751_report.py')) + NEW_TOOLS + COMPUTE_TOOLS + REPAIRED_TOOLS
# ### the act's arms over its own banks: set before the lock by the Edit tool -- b750's list, the act shift G-R360-ENTERED to G-R361-ENTERED,
# ### G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0 ((R361)(2)(iv))
ACT_ARMS = ('G-ACT-CURRENT', 'G-ARM-TAGS', 'G-ARMS-RETIRED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED', 'G-CLOSING-DRY-STEP', 'G-COEFFS-LAW',
            'G-CORRIGENDUM-ENTERED', 'G-COUNT-ROUTE-PRICED', 'G-DELETES-ONE-BRANCH', 'G-DERIVATION-GRADED', 'G-DIFFERS-ERRATA', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-GUARD-HELD', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LISTINGS-BEFORE-CLAUSES',
            'G-MEMBRANE-WIRED', 'G-OFFSET-POST-HOC', 'G-POSTROOT-WRITES-NONE', 'G-PREDICTION-FIRST', 'G-R361-ENTERED',
            'G-REGISTRATIONS-FIRST', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED', 'G-SURGERY-CARRIED', 'G-TOUCH-READ',
            'G-WRITELIST-MIRROR-STATE')

# ### b751 writes no kernel ((R361)(5)): no main touched, no branch made on a kernel
SITTING_TIPS = {}
SITTING_BASE = EF_BASE
SITTING_REPOS = tuple(sorted(SITTING_TIPS))
SITTING_BRANCH = None
SITTING_BANK = 'data/b751_sitting.txt'   # ### the record of the sitting, one row per item
KERNEL_BASES = 'data/b751_kernel_bases.json'
