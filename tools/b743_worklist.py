# -*- coding: utf-8 -*-
"""b743_worklist.py -- THE ACT'S DATA, UNDER (R353). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b743: LANE TWO, ACT ONE HUNDRED AND SEVENTY, THE DISCHARGE SITTING -- b742 AT ITS WEIGHT; W-ORD-ZQ-OFFLINE-ZERO DISCHARGED ON THE
### NAVIGATOR'S READ; THE CORRIGENDUM OPENING ON THE PROMPT SENTENCE THAT MISLED; THE SITTING OVER THE EPSTEIN SENTENCES, THE LEDGER ROWS, THE
### RUBRIC, THE TWO OUTLINES AND FOUR ORDERS, ONE ITEM PER GIT WRITE ON THE AUTHOR'S NUMBER. No Lean, no dispatch (N1).
### Carried by diff from b742_worklist.py (data/b743_carry_worklist.txt); its stage one set by the Edit tool at step zero with this act's
### figures (the carried text named b742's objects under b743's names); later stages by the Edit tool.
### The act runs in b742's session (c66dda9f, continued after a context summary), one seat; the anchor divides the two acts' commands.
### b742 closed and pushed itself whole (relay 16a36428, PLACE-papers 3dc9c05); its closing capture and step-22 row are this act's carried
### files ((R353)(3)), each committed alone at step zero; tools/mirror_prevbuild.json carried no content change (its LF form equal to HEAD's).
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
PRE_PP = '3dc9c05d9e3f87d910f27b33abc85d16a520d926'    # ### PLACE-papers main before the act's own commits: b742's record
PRE_RELAY = '16a364280c4a5ad9dc6f51aacd237077c0c9c9b0'  # ### relay main before the act's own commits: b742's closing
PRE_PP_REMOTE_AT_START = '3dc9c05d'      # ### PLACE-papers remote main at the act's start (data/act_current.json, equal to local)
PRE_RELAY_REMOTE_AT_START = '16a36428'   # ### relay remote main at the act's start (the citation check's remote main row)
B718_RELAY_HEAD = '16a3642'  # ### the names kept for the carried readers: the previous act's last relay head (b742's closing)
B718_PP_HEAD = '3dc9c05'     # ### the previous act's last PLACE-papers head (b742's record)
DATE = '2026-11-06'
SESSION_ID = 'c66dda9f-cc02-473a-b740-111b6d66dec3'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/0fa2f3b7e932577a/%s/scratchpad' % SESSION_ID   # ### b742's form, carried
HOLD = 2560
ANCHOR = 'RULING (R353) BEGIN'           # ### the act's capture anchor, as data/act_current.json
RULING_ANCHOR = 'RULING (R353) BEGIN'    # ### the ruling's BEGIN line, the citation tool's ferry source
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = 'c66dda9f-cc02-473a-b740-111b6d66dec3'   # ### b742 ran in this session (from 'RULING (R352) BEGIN' to 'RULING (R353) BEGIN')
PREV_ANCHOR = 'RULING (R352) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b743_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 13687          # ### FINDINGS: b742's entry head (carried at 3dc9c05)
B711_WEIGHT = 13617         # ### FINDINGS: b741's weight line (b742's Component 1)
B711_CORRIGENDUM = 13619    # ### FINDINGS: b742's corrigendum for b741
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 17658          # ### OPEN_TRAILS: b742's trail record (PLACE-papers 3dc9c05)
B711_FACE = 'data/b742_registration_2026-11-05.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-11-05-b742.zip'   # ### b742's export, built after b742's last PLACE-papers push, CLEAN 3/3
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
ORDER_LEDGER_SPLIT = 14680  # ### OPEN_TRAILS: W-ORD-LEDGER-SPLIT-RESOLVER (b680), (R353)(3)
TRAIL_ORDERS = 17666        # ### OPEN_TRAILS: the last open-orders line, b742's, written from the generator's output
TRAIL_RESOLVED = 17696      # ### OPEN_TRAILS: b742's items for the author's strike, in its trail
TRAIL_RETIRED = 17682       # ### OPEN_TRAILS: b742's count line of the author's prompts
#   ### b743 step zero: the carry brought b741's lines (17620/17650/17636) under these names; set to b742's here, each read from OPEN_TRAILS at 3dc9c05
WATCH_LINE = 16126          # ### OPEN_TRAILS: W-ORD-QUASI-RH-FIELD-WATCH, annotated at b718's C6
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row
INSTRUMENTS = 'phase1.5/method/INSTRUMENTS.md'   # ### PLACE-papers' instruments document, its last entry I-108 (b742)
INSTRUMENTS_LAST = 108

# ### (R353)(3): the five records, in the order the ruling names them: (row, kernel, Zenodo record, the sitting row's line in data/b736_sitting.txt)
TIER3 = ((104, 'SIDE-cosmo', '19938009', 1095), (105, 'SIDE-effects', '19938005', 1105), (106, 'SIDE-trivium', '19938003', 1115),
         (107, 'SIDE-interfaces', '19931797', 1125), (108, 'SIDE-kernel', '21520474', 1135))
TIER3_BANK = 'data/b739_tier3.txt'                  # ### b743: b739's, read not written (no Zenodo field touched, (R353)(5)); the carry shifted it to b742's, which does not exist
READBACK_BANK = 'data/b739_zenodo_readback.json'

# ### the branches step zero deletes ((R353)(5)): the push-b742-* branches b742's close made, by name, each read from the listings and
# ### `--merged` printed before the deletes, one per command, each its own message
DELETE = (('D:/relay', ('push-b742-closing', 'push-b742-preroot', 'push-b742-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b742-preroot', 'push-b742-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### carried: NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'), ('D:/SIDE-explicit-formula', 'challenge-b720-h2-sign-iff-rh'),
                 ('D:/SIDE-lv-conservation', 'scratch-b724'), ('D:/SIDE-explicit-formula', 'keiper-b725'), ('D:/SIDE-explicit-formula', 'c2-b725'),
                 ('D:/SIDE-kernel', 'rebuild-b721'), ('D:/SIDE-lv-conservation', 'rebuild-b721'), ('D:/SIDE-archimedean', 'rebuild-b721'),
                 ('D:/SIDE-frobenius', 'rebuild-b721'), ('D:/SIDE-spinor', 'rebuild-b721'), ('D:/SIDE-rcurve', 'rebuild-b721'),
                 ('D:/SIDE-explicit-formula', 'detect-b729'), ('D:/SIDE-explicit-formula', 'zq-b730'))   # ### (R353)(4) names c2-b725, keiper-b725, detect-b729, zq-b730

# ### the kernels: read; written only on the rebuild-b721 branches by (R353)(7) and the author's word (4)
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')


def _kernel_paths():
    """the kernels of data/b716_federation_pin_price.txt (1), as D:/<name>, read at import ((R353) PATHS)."""
    p = os.path.join(D, 'b716_federation_pin_price.txt')
    t = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return tuple('D:/' + m.group(1) for m in re.finditer(r'(?m)^  (SIDE-[A-Za-z0-9-]+)\s+HEAD ', t))


KERNEL_PATHS = _kernel_paths()
PATHS = ('D:/relay', PP, KERNEL_DIR, LV_DIR) + tuple(k for k in KERNEL_PATHS if k not in (KERNEL_DIR, LV_DIR))   # ### (R353)'s PATHS
EF_MAIN = '8fbab45d8a966dca53d42448e33927d885fd4ea3'    # ### SIDE-explicit-formula's main after [A4]: badacccb + README.md alone ((R353)(6))
LV_MAIN = '305a87c9e09c45cc8a935b1065f26f929634c707'    # ### SIDE-lv-conservation's main at the sitting's [41] (README.md alone, (R353)(3))
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
# ### the wave 1 kernels at their own pins, (name, tag, the short commit) -- b721's (R331)(7), b742's (R352)(10)
WAVE1 = (('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-archimedean', 'v0.1.0', '8019d9d'),
         ('SIDE-frobenius', 'v0.1.0', '2efe9f2'), ('SIDE-spinor', 'v0.1.0', 'b235bc6'), ('SIDE-rcurve', 'v0.1.0', 'd5f33b4'))
CHECKPOINT_STATEMENTS = (('SIDE-archimedean', 'archimedean_forces_half'), ('SIDE-frobenius', 'indicial_forces_half'),
                         ('SIDE-spinor', 'spinor_forces_half'), ('SIDE-spinor', 'half_iff_centered_zero'), ('SIDE-rcurve', 'monotone_unique_zero'))
REBUILD_BRANCH = 'rebuild-b721'          # ### b721's branches, kept, (R353)(7)'s repair made on them alone
REBUILD_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-lv-conservation', 40706311269), ('SIDE-archimedean', 40706397470),
                ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404), ('SIDE-frobenius', 40713201832))   # ### b721's, each read by its id
AXIOM_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-archimedean', 40706397470), ('SIDE-frobenius', 40713201832),
              ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404))   # ### b742's (R352)(10): the five whose axiom step was diagnosed
AXIOM_DIAG = 'data/b729_axiom_diag.txt'  # ### the routes (R353)(7) and the author's word (4) take
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
DATA_STANDING = 'data/standing_clauses_v9.txt'   # ### v8 bound the act to d9739558; v9 from that commit, which landed it at Component 1 ((R353)(2)(v))
DATA_STANDING_V9 = 'data/standing_clauses_v9.txt'
ARM_TAGS = 'data/arm_tags.json'
REPO_VISIBILITY = 'data/repo_visibility.txt'
PLAN_BANK = 'data/b743_sitting_agenda.txt'            # ### (R353)(4): the sitting's agenda, every draft banked before its item was put (the F drafts at the question)
REGISTRATIONS = PLAN_BANK                             # ### (carried name) the act's registration: the agenda, its one commit REG_COMMIT
PREV_BUILD_BANK = 'data/b742_offlinezero.txt'         # ### (R353)(1): b742's build bank as committed at bca1d1ba
PREV_BUILD_MD5 = None                                 # ### printed by the citation check at step zero
PREV_STATEMENTS_BANK = 'data/b742_c7_plan.txt'        # ### b742's plan (read by b742's arms; not this act's)
STATEMENTS_BANK = 'data/b743_sitting_agenda.txt'      # ### (carried name) the agenda
C7_PLAN = STATEMENTS_BANK
S6_PLAN = STATEMENTS_BANK
BUILD_BANK = 'data/b743_sitting.txt'                  # ### (carried name) the act's result bank: the sitting's record, its foot the tally
NOTES_BANK = None                                     # ### no notes bank this act
REG_WALK_COMMIT = '15cb6cc4'                     # ### b721's H-C2-WALK commit (carried name; b742's walk read under it)
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
#   ### read not written (carried name); b742 wrote no coefficient bank
COMPUTE_BANKS = ('data/b743_standing_v1230.txt', 'data/b743_sitting_agenda.txt', 'data/b743_sitting.txt', 'data/b743_sitting_greps.txt',
                 'data/b743_address_scan.txt')
#   ### the banks of (R353)(2)-(3), each written by its component
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt',
              'data/b729_read_calls.txt', 'data/b730_read_calls.txt', 'data/b742_read_calls.txt', 'data/b743_read_calls.txt')

# ### THE SUITE'S PARTS: ten, as b742 split them under (R352)(2)(vi) and b675 rules row (2) (standing-a in two, G-NO-SORRY-MAIN's kernels
# ### halved, and the chain's first half in four, b2a-b2d); data/act_current.json committed them ten at b743's step zero (e0777ce8), no
# ### component splitting them this act, so PARTS_AT_STEP_ZERO is PARTS
PARTS = ('standing-a1', 'standing-a2', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d', 'standing-b3', 'act')
PARTS_AT_STEP_ZERO = PARTS
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b743'))
CHAIN_QUARTERS = (('b624', 'b627'), ('b628', 'b631'), ('b632', 'b635'), ('b636', 'b658'))   # ### walks 116, 129, 157, 146 s at b743
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### set by the Edit tool when a component adds a standing arm
SHARED_APPENDED = ('data/b675_corrigenda.txt',)   # ### (R353)(2): the corrigenda row
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'ERRATA.md',
             'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md', 'day1/Which_Structure_Confines_v2_4_0.md', 'phase2/method/THE_EULER_SPECIFICATION.md',
             'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md', 'phase1.5/method/THE_METHOD_CANON.md',
             'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md', 'phase1.5/method/CERTIFIED_EVALUATION_IN_THE_STRIP_v0_1.md')
#   ### the ledgers and the files the author's numbers passed under (R353)(4)(A)-(F) ((R353)(5)'s (W) list); two new (the skeletons)
PP_WRITTEN = PP_EDITED
PP_NEW = ('phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md', 'phase1.5/method/CERTIFIED_EVALUATION_IN_THE_STRIP_v0_1.md')
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the re-cut's merge (kept for the kernel rows); the MANIFEST control's reference
#   ### is the commit the mirror is built at from v1.2.1
NEXT = ('per (R353)(7), named by the author at the sitting`s end (relay data/b743_sitting.txt, [(7)]): plan both controls -- b744 writes the plan '
        'banks of W-ORD-ZETA-BOX and W-ORD-POSITIVE-CONTROL at their prices, no build, carrying the condition of [F2] (the on-line conclusion drawn '
        'through the schema`s own theorem, not a separate finite-case lemma)')   # ### the author's word at the sitting's end
NEXT_ACT = 'b744'


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
ACT_CURRENT_COMMIT = '4b15f910'         # ### data/act_current.json for b743 committed alone ((R353)(4)), before any other command
STEPZERO = '88a8c498'             # ### b742's closing capture, committed alone ((R353)(3))
STEPZERO_STEPS = 'c68b4c10'       # ### b742's step-22 row, committed alone ((R353)(3))
STEPZERO_TABLE = None             # ### the terminal table regenerated and committed ((R353)(8))
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None   # ### tools/mirror_prevbuild.json of b742: its LF form equal to HEAD's (2d637131, blob a94aa543), nothing to commit
STEPZERO_REFUSALS = ()
STEPZERO_BANKS = '61fabf98'       # ### step zero's banks and carried tools, one commit (data/b743_stepzero.txt among them)
STEPZERO_BANK_COMMIT = STEPZERO_BANKS
STEPZERO_ANSWERS = None   # ### b742's: '1f96d4ea'     # ### the author's word at PROMPT 1 amending (R353)(3), with its amendment row: the commit every dispatch row names ((R353)(2)(i))
STEPZERO_ANSWERS_FULL = None   # ### the same, as each dispatch row's licence names it
# ### N2: each generator commit (relay) before the zq-b730 commit holding the modules it generated
GEN_COMMITS = ()   # ### b742's generator commits (22f8d6b1, 6467c061, 3194b6eb) are cited by the discharge, not this act's
GEN_MD5 = {'FrontierData': 'c8e320f9db1a12622cc147555496cf11', 'Nodes0': '7cb04ecfd3649a1daf5633de691df670',   # ### the generator's output at 3194b6eb
           'Nodes1': 'a20f1f00a156e59e97f841beb8d89a76', 'Nodes2': 'efff8c97b5f9879bcf12e3f79628dc64',
           'Nodes3': '09de4381169541faf5f0066bf66905e7', 'NodesF': 'd37bbfbb8c81165521b77de16022069a'}
GENERATOR = 'tools/b742_s6gen.py'   # ### b742's, read not run
VISIBILITY_COMMIT = None
COMPUTE_TOOLS = ()                      # ### set by the Edit tool when a component seals a compute tool
REPAIRED_TOOLS = tuple(p[len('tools/'):] for p in json.load(io.open(os.path.join(D, 'act_current.json'), encoding='utf-8'))['shared_edits'])
#   ### (R353)(2), b742 event (2): read from data/act_current.json, the one hand list, which G-ACT-CURRENT reads against git; sealed before the suite runs (b696's form)
REPAIRED_DATA = ()
# ### b721's trap (event 11): the standing part of the sealed list read from the directory, not a carried tuple
STANDING_FILES = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing')) if f == 'VERSION' or f.endswith('.py')))
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset, sealed by hash beside the act's tools
# ### the seven close tools are tools/standing/fold.py's renders of its templates (tools/standing/fold/<tool>.tpl) with the act's arms module
# ### (tools/acts/b743.py) -- every byte a render reads sealed beside the act's tools; report.tpl left out of the seal (b708's report row)
FOLD_FILES = tuple(sorted('standing/fold/' + f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing', 'fold')) if f.endswith('.tpl')
                          and f != 'report.tpl')) + ('acts/b743.py',)
NEW_TOOLS = NEW_TOOLS + FOLD_FILES
STANDING_VERSION = 'v1.23.0'            # ### (R353)(3)'s repairs, landed by a commit of their own (C1_STANDING) with data/b743_standing_v1230.txt
STANDING_VERSION_ENTERING = 'v1.22.0'
LEAN_TREES = (('D:/SIDE-explicit-formula', '14ca5725'), ('D:/SIDE-explicit-formula/.lake/packages/mathlib', 'de5ce8a9'))   # ### zq-b730 at b742's tip
# ### v1.18.0, (R353)(2)(ii): the act's banks whose comparative sentences the citation check reads, and a reading row for each word (tools/standing/cites.py
# ### comparative_rows); set by the Edit tool as Components 2-4 write the banks, before the lock
COMPARATIVE_BANKS = ('data/b743_corrigendum.txt', 'data/b743_sitting_agenda.txt', 'data/b743_sitting.txt',
                     'data/b743_defects.txt')   # ### Components 1-3's banks: no
COMPARATIVE_ROWS = ()   # ### comparative word in them ("at least" excepted by the reader), so no reading row; the check reads the three for one
#   ### the trees the ruling's Lean paths are read against: zq-b730's tip, and Mathlib at its pin (the ferry's "Mathlib at the pin: Analysis/Complex/AbsMax.lean :405, ...")
STANDING_CHANGED = ('cites.py', 'commit.py', 'dispatchrows.py', 'rootprompt.py', 'subjects.py', 'VERSION')   # ### v1.23.0 at 7c6648ac (and tools/push_gated.sh)
STANDING_NEW = ('pushcheck.py', 'v1230.py')
# ### b742's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = '16a36428'    # ### b742's closing, the act's relay base
B714_RECORD = 'ced30a77'     # ### b742's record commit (relay, the head line's)
B714_ROOT = '9c9c6a90c282a4a41bc02f1e9af47f9a3f1b5191acdd48efb41a86e6d0fe3543'   # ### b742's root, data/act_roots.txt's last row
B723_ROOT_BANKS = '11628c89'  # ### b742's root commit, the banks its root rode with
# ### later stages: the commits of the components, read from the logs after each was made (None until made)
C1_STANDING = '7c6648ac'           # ### tools/standing/ v1.23.0 by a commit of its own, its controls bank data/b743_standing_v1230.txt ((R353)(3)(vii))
C1_STANDING_REPAIR = None          # ### no act data changed by the repairs
C1_RELAY = '44268469'              # ### the c1 route, the corrigendum banks, the corrigenda row (63), the rules bank, the citation check CLEAN
C1_CORR = C1_RELAY
C1_RULES = C1_RELAY          # ### data/b743_rules.txt rode in Component 1's relay commit, not a commit of its own (a defect of b743)
C1_PP = '78b38fff'                      # ### PLACE-papers: FINDINGS (b742 at its weight), (the corrigendum); set after it lands
C1_DISCHARGE_PP = '4541d90d'   # ### W-ORD-ZQ-OFFLINE-ZERO discharged in OPEN_TRAILS by a commit of its own ((R353)(2))
C2_TOOL = None
WEIGHT_LINE, CORR_LINE = 13729, 13731   # ### FINDINGS: b742's weight line and the corrigendum for b742 (Component 1, PLACE-papers 78b38fff), set at Component 3
DIFFERS_LINE = None
ERRATA_LINE = None
C2_PLAN_FIRST = 'f18360ae'   # ### the agenda's one commit (written before the first item was put, committed with the sitting's bank at the sitting's end: a defect of b743)
C2_RELAY = 'f18360ae'   # ### Component 2, the sitting's banks: the record, the agenda, the greps tool and bank, the [A5] description, step rows 7-22
C2_PP = None
PRICE_LINE = 17400
DOORS_COMMIT = None
MECH_COMMIT = None
FRONTDOORS_COMMIT = None
COUNT_BANK = None
PRINT_COMMIT = C2_RELAY  # ### (carried name) the commit carrying the act's result bank: data/b743_sitting.txt
PLAN_MD5 = '9875a24319a66b15840629f1135894e0'   # ### the agenda's md5 at f18360ae (LF), equal to the working file's
C2_AMEND = ()
SITTING_PP = ('8ddc94a8', 'a790da0c', 'e7e9cbc1', '9b4af2c6', '1d941779', '488b4d09', '1fa7ddab', 'ca359d12', '05624b9d', 'e43a8a84',
              '7c11c115', '5c365d1d', 'c6c39f38', '5641b41f', '276eecde', '5b3f3efc')   # ### [A1] [A2] [A3] [B1]-[B6] [C] [D] [E] [F1]-[F4], one git write per passed item
SITTING_KERNEL = ('SIDE-explicit-formula', '8fbab45d8a966dca53d42448e33927d885fd4ea3')   # ### [A4]: README.md alone on its main ((R353)(6))
SITTING_GH = ('psinary-sketch/SIDE-explicit-formula',)   # ### [A5]: the description by gh, the author's second wording after GitHub's 350-character refusal, read back
SITTING_ITEMS = 44   # ### decided: A 5 + B 6 + C 8 + D 10 + E 10 + F 4 + G 1 (A6-A9 banked only); passed 43, G deleted, struck 0
C3_RELAY = ()   # ### Component 3, the build to SP4 ((R353)(3)(b)): the tool, the dispatch rows; the build bank and its notes at Component 4
SITTING_COMMITS = ()
C3_PP = None
C4_LV = None
C4_RUN = None
C4_PP = None
C4_RELAY = None
C5_RELAY = None
REG_COMMIT = C2_PLAN_FIRST    # ### the plan's first commit, with the prints it cites
ZEROS_REG_COMMIT = REG_COMMIT
ORDERS = (142, 60, 42, 12, 28)          # ### b742's (R352)(4) triage, carried as read (data/b729_orders_triage.txt): DONE, NOT MET, MET, AUTHOR'S WORD
TRIAGE = 'data/b729_orders_triage.txt'
LV_SCRATCH_BRANCH = 'scratch-b724'      # ### b724's scratch branch of SIDE-lv-conservation, kept ((R353)(8))
LV_RUNS = (('SIDE-lv-conservation', 40964150574),)   # ### b742's one dispatch, read by its id (carried, not re-run)
LV_ROWS = 'data/b743_lv_rows.json'
CHALLENGE_BRANCH = 'challenge-b720-h2-sign-iff-rh'   # ### b720's, on SIDE-explicit-formula, standing, not merged, no tag
CHALLENGE_TIP = '3391647518cd37316a448b5013afb62a198fa6c6'
CHALLENGE_RUN = 40651875792
PIN_RUNS = (('SIDE-grh-transfer', 40652622018), ('SIDE-interfaces', 40652657325), ('SIDE-kernel', 40652692787),
            ('SIDE-lv-conservation', 40652727943), ('SIDE-simplicity', 40652762827), ('SIDE-trivium', 40652790458))   # ### b720's, read not re-run
PIN_BRANCH = 'pin-b718-de5ce8a9'   # ### b718's pin branches, left as banked ((R353)(8))
PIN_EXCLUDED = ('SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve', 'SIDE-cosmo')
PIN_HELD = ('SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium')
PIN_BUILDS = ('SIDE-simplicity',)
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PIN_TO_NEXT = ()
MAX_DISPATCHES = 0         # ### N1: no runner dispatch this act ((R353)(6))
MAX_C2, MAX_KEIPER = 0, 0
EF_DIR = 'D:/SIDE-explicit-formula'
EF_BASE = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'   # ### SIDE-explicit-formula's main entering the act, every branch cut from it
EF_MAIN_AFTER = '8fbab45d8a966dca53d42448e33927d885fd4ea3'   # ### main after [A4]: README.md alone beyond EF_BASE ((R353)(6), the author's number)
ZQ_BRANCH = 'zq-b730'
ZQ_ENTERING = '14ca572560f50378a6e4715e35cba0351e5f105d'   # ### b742's tip (SP4), unmoved: this act writes no Lean file ((R353)(6))
ZQ_TIP = ZQ_ENTERING   # ### unmoved
ZQ_FIRST = None   # ### no Lean commit this act
ZQ_COMMITS = ()   # ### none this act
ZQ_COMMITS_B742 = ('280b28b3935854f8c71e37480ee9b88dfeb60922', '11bb0125fa08eccc78f6a1a6d415201438973f45', '5d3136a39ea9b671b60118e1424e645f89956ea7',
                   '4c04916c8541f1ee2267059a8fa0396364f1eb5c', 'c2d4f29ce84d321814b223a7e275e0653161b4d4', '14ca572560f50378a6e4715e35cba0351e5f105d')   # ### b742's six, read by the discharge
ZQ_COMMITS_B741 = ('f2de6efb669405b5e6ed270e4a82e3bc6effa500', 'de4810da5d3cfc524002630959b32e4ebc30ce66', '47f5afb3f1b40a8525ac45eba0f1bf04fe2ed155',
              '42cb968b8ce35bb024bca8995a743a809c19409e', 'c9ad907454b785b75ad2142e1dcdf9a4797cfd0c', '3329eaa106cc24891ed55374afcd4ca4f7fe33d8')   # ### T ; G1+G2 ; repairs+G4 ; G3+G5 ; cast repair ; generator repair
ZQ_COMMITS_B740 = ('8c6ec8d12d97bece1de8dab10511add9d97382d0', '6b068a0db2ff1451e9da7bff82fe8fd66a8dad38', 'ba318a0b67fd95164623e4fdf109eb5d042697fa')   # ### b742's S5c ; S5d with S5c's fix ; S5d's fix
ZQ_SP1 = None
ZQ_SP3 = '3329eaa106cc24891ed55374afcd4ca4f7fe33d8'   # ### b742: SP3 REACHED here (dispatch 6, run 41940815524)
ZQ_SP4 = '14ca572560f50378a6e4715e35cba0351e5f105d'   # ### b743: SP4 REACHED here (dispatch 7, run 42068096322)
ZQ_MODULES = ('Xi', 'Landau', 'Heights', 'Contour', 'ZeroSum', 'FullLine', 'Lines', 'Main')   # ### the build's eight, under Schema/ZQ/EF
ZQ_OFFZERO_MODULES = ('Box', 'Diff', 'MinModulus', 'Carrier', 'Main', 'Split', 'Tail', 'IncGamma', 'Elem', 'Time', 'Series', 'Sums', 'GammaVal', 'Shells', 'Centre',
                      'Interp', 'Frame', 'Strip', 'Amplify', 'NodeBase', 'Omega', 'Nodes0', 'Nodes1', 'Nodes2', 'Nodes3', 'NodesF', 'FrontierData',
                      'Frontier', 'SP4')   # ### under Schema/ZQ/OffZero; b743 adds S6's fourteen
ZQ_FILES = ()   # ### zq-b730's diff against its entering tip: none (no Lean file this act)
ZQ_FILES_B742 = tuple('SIDEExplicitFormula/Schema/ZQ/OffZero/%s.lean' % m for m in ('Amplify', 'Frame', 'Frontier', 'FrontierData', 'Interp', 'NodeBase',
                 'Nodes0', 'Nodes1', 'Nodes2', 'Nodes3', 'NodesF', 'Omega', 'SP4', 'Strip')) + ('print_targets.txt',)   # ### b742's diff against 3329eaa1 at 14ca5725
ZQ_FILES_B741 = ('SIDEExplicitFormula/Schema/ZQ/OffZero/Centre.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/GammaVal.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/Series.lean',
            'SIDEExplicitFormula/Schema/ZQ/OffZero/Shells.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/Sums.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/Time.lean',
            'print_targets.txt')   # ### zq-b730's diff against ba318a0b at 3329eaa1
ZQ_FILES_B740 = ('SIDEExplicitFormula/Schema/ZQ/OffZero/Elem.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/IncGamma.lean', 'print_targets.txt')   # ### b742's diff against 602cd401
ZQ_MODULES_B730 = ('Lattice', 'Theta', 'FEPair', 'Continuation')   # ### the names the carried sections read, until each section is set for this act
ZQ_ZEROS_FIRST, ZQ_LOGDERIV_TIP = None, None
ZQ_LOGDERIV_MODULES, ZQ_ZEROS_MODULES = (), ()
MAX_LOGDERIV, MAX_ZEROS = 0, 0
EF_BRANCHES = (('keiper-b725', '01fd33c2d7dc62d4702b075de3dda9253c5c2f87'),   # ### (R353)(4): the gamma_1 bound
               ('c2-b725', '0395f15d3b2906716ccb1f09ca24171d7a921210'),       # ### (R353)(3): the theorem, built whole at this tip
               ('detect-b729', '1023301c89ab16f8d437b2a1f08a824bc95b6b0e'),   # ### b729's (R339)(5): the statement alone, not compiled; kept, unmoved
               (ZQ_BRANCH, ZQ_TIP))                                           # ### (R353)(3)-(4): the fields
EF_BRANCHES_ENTERING = ('01fd33c2d7dc62d4702b075de3dda9253c5c2f87', '0395f15d3b2906716ccb1f09ca24171d7a921210', '1023301c89ab16f8d437b2a1f08a824bc95b6b0e', ZQ_ENTERING)   # ### the four entering the act
EF_RUNS = ()   # ### N1: no dispatch this act ((R353)(6))
EF_RUNS_B742 = (42054839204, 42056405331, 42058361986, 42061332755, 42062848400, 42065597154, 42068096322)   # ### b742's seven, read not re-run; the last the SP4 grade run
EF_RUNS_B741 = (41931918742, 41935365948, 41936644993, 41938300160, 41939524029, 41940815524)   # ### b742's six: KERNEL (timing), BREAKS, KERNEL, BREAKS, BREAKS, KERNEL (SP3)
EF_RUNS_B740 = (41854903335, 41857376723, 41859346843)   # ### b742's three: BREAKS, BREAKS, KERNEL, read not re-run
EF_RUNS_B738 = (41732413170, 41732882564, 41733411736, 41734667160, 41735082430, 41736472780)   # ### b738's first six (of eleven), read not re-run
ZQ_RUN = 41483457057   # ### b737's grade run, the discharge's, read not re-run
EF_RUNS_B731 = (41371666217, 41372597450, 41373409167, 41374121055, 41374814817)   # ### b731's five, read not re-run
DISPATCH_ROWS = 'data/b743_dispatch_rows.json'
ERRATA_ID = 'E-2026-11-06-1'   # ### (R353)(4)(B), [B6]: (R345)(6)'s sentence withdrawn by (R346)(2), appended at PLACE-papers 05624b9
ERRATA_IDS = (ERRATA_ID,)
RETIRED_COUNT = 0
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list (the root answer's addition (b))
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b743_') and f.endswith('.py') and f != 'b743_report.py')) + NEW_TOOLS + COMPUTE_TOOLS + REPAIRED_TOOLS
# ### the act's arms over its own banks: set before the lock by the Edit tool -- b742's list, the act shift G-R352-ENTERED to G-R353-ENTERED,
# ### G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0 ((R353)(2)(iv))
ACT_ARMS = ('G-ACT-CURRENT', 'G-ARM-TAGS', 'G-ARMS-RETIRED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED', 'G-CLOSING-DRY-STEP', 'G-COEFFS-LAW',
            'G-CORRIGENDUM-ENTERED', 'G-COUNT-ROUTE-PRICED', 'G-DELETES-ONE-BRANCH', 'G-DERIVATION-GRADED', 'G-DIFFERS-ERRATA', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-GUARD-HELD', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LISTINGS-BEFORE-CLAUSES',
            'G-MEMBRANE-WIRED', 'G-OFFSET-POST-HOC', 'G-POSTROOT-WRITES-NONE', 'G-PREDICTION-FIRST', 'G-R353-ENTERED',
            'G-REGISTRATIONS-FIRST', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED', 'G-SURGERY-CARRIED', 'G-TOUCH-READ',
            'G-WRITELIST-MIRROR-STATE')

# ### b743 writes one kernel main, SIDE-explicit-formula's, README.md alone, on the author's number ((R353)(4)(A) [A4], (6)); no branch moved
SITTING_TIPS = {'SIDE-explicit-formula': EF_MAIN_AFTER[:8]}
SITTING_BASE = EF_BASE
SITTING_REPOS = tuple(sorted(SITTING_TIPS))
SITTING_BRANCH = 'push-b743-sitting'   # ### the one kernel write, main's README.md (8fbab45d); push_gated.sh takes a push-* branch at main's tip (b736's form), made at the push stage
SITTING_BANK = 'data/b743_sitting.txt'   # ### the record of the sitting, one row per item
KERNEL_BASES = 'data/b743_kernel_bases.json'
