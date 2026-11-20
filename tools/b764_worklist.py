# -*- coding: utf-8 -*-
"""b764_worklist.py -- THE ACT'S DATA, UNDER (R374). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b764: LANE TWO, ACT ONE HUNDRED AND NINETY-ONE, THE RECORD'S UPKEEP -- b763 AT ITS WEIGHT; THE REPAIRS BY CLASS, EACH WITH ITS
### PLANTED CONTROL; THE CLOSE'S HOURS AND YIELD MEASURED; THE RUNNER TRIED ON A RESTORED BUILD; THE FIVE ORDERS THE UPKEEP CARRIES;
### AN ERRATUM, THE FINITE PART OF THE ARCHIMEDEAN TERM AND THE CENTRE PRICED ANEW; THE NAVIGATOR'S PREDICTIONS BANKED. The builds are
### the three runner dispatches of (7) alone, no lean on this host (N1); nothing deposits, no kernel beyond SIDE-explicit-formula's
### workflow file, no tag cut, no byline (N5).
### Carried by diff from b763_worklist.py (data/b764_carry_worklist.txt); its stage one set at step zero with this act's figures by the
### seat's script (scratch wl764.py, each constant replaced whole by its name); later stages by the Edit tool.
### (R374) was delivered in one part in session 11d67961 (b763's session; at transcript line 213526, 2026-11-20T16:52:08Z); the act
### runs in it, one seat, with no change of session, harness or store (the step-zero reads of 2026-11-20T16:53:28Z-16:54:22Z).
### b763 closed (relay 0f9b1df2, PLACE-papers 7db9a66c); its carried files ((R374)(3)) committed at step zero.
### ANCHOR is the act's capture anchor (data/act_current.json, the ruling's first line); RULING_ANCHOR the same line, the citation tool's
### ferry source.
"""
import io
import json
import os
import re
from standing.carry import Carried as _Carried   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the stage-one values below refuse on use until written
from standing.carry import Carried as _Carried   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the stage-one values below refuse on use until written
from standing.carry import Carried as _Carried   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the stage-one values below refuse on use until written
from standing.carry import Carried as _Carried   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the stage-one values below refuse on use until written
from standing.carry import Carried as _Carried   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the stage-one values below refuse on use until written
from standing.carry import Carried as _Carried   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the stage-one values below refuse on use until written
from standing.carry import Carried as _Carried   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the stage-one values below refuse on use until written
from standing.carry import Carried as _Carried   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the stage-one values below refuse on use until written
from standing.carry import Carried as _Carried   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the stage-one values below refuse on use until written
from standing.carry import Carried as _Carried   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the stage-one values below refuse on use until written

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '7db9a66c53f6314f0be3598f2fd680cb31f89dcb'    # ### PLACE-papers main before the act's own commits: b763's record (the trail), pushed
PRE_RELAY = '0f9b1df2f06be318841bee518183ec3ce842fb5e'  # ### relay main before the act's own commits: b763's closing step row, pushed
PRE_PP_REMOTE_AT_START = '7db9a66'       # ### PLACE-papers origin/main at the act's start, read from the tracking ref (no remote read at step zero), equal to local
PRE_RELAY_REMOTE_AT_START = '0f9b1df2'   # ### relay origin/main at the act's start, read from the tracking ref, equal to local
B718_RELAY_HEAD = '0f9b1df'  # ### the names kept for the carried readers: the previous act's last relay head (b763's closing step row)
B718_PP_HEAD = '7db9a66'     # ### the previous act's last PLACE-papers head (b763's record)
DATE = '2026-11-20'
SESSION_ID = '11d67961-2aa4-4353-bc12-a982038bfa55'   # ### the transcript the ruling and the ferry stand in (one part, at line 213526, 2026-11-20T16:52:08Z), b763's session; the act runs in it, one seat, no change of session, harness or store
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/0fa2f3b7e932577a/11d67961-2aa4-4353-bc12-a982038bfa55/scratchpad'   # ### the seat's scratchpad as the harness names it (session 11d67961, the act's own)
HOLD = 2560
ANCHOR = 'RULING (R374) BEGIN'           # ### the act's capture anchor, as data/act_current.json
RULING_ANCHOR = 'RULING (R374) BEGIN'    # ### the ruling's BEGIN line, the citation tool's ferry source
TAIL = 'FERRY END'   # ### b764: (R374) in one part, its texts after clause (14) and before the ferry (data/b764_ferry.txt), set at stage one (scratch wl764.py)
SESSIONS_AFTER = ()   # ### none: the act runs in the session its ruling was delivered in (b671's form not needed)
PREV_SESSION = '11d67961-2aa4-4353-bc12-a982038bfa55'   # ### b763 ran in this session from its delivery (2026-11-19T18:35:12Z) to its closing push (after its step rows 0f9b1df2, 2026-11-20T14:35:49Z); (R374) was delivered in it after that close
PREV_ANCHOR = 'RULING (R373) BEGIN'   # ### the first user row of 11d67961 holding b763's ruling's first line (2026-11-19T18:35:12Z), before b763's post-push combine (its command at transcript line 213081); G-EDIT-ROUTE's window from that combine to (R374)'s anchor
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b764_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 15815          # ### FINDINGS: b763's entry head (at b302009, unmoved at 7db9a66c)
B711_WEIGHT = None          # ### FINDINGS: b763 wrote no weight line of its own; b762 at its weight stands in b763's entry (:15821)
B711_CORRIGENDUM = 15797    # ### FINDINGS: b763's corrigendum for b762
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 18993          # ### OPEN_TRAILS: b763's trail record (PLACE-papers 7db9a66c)
B711_FACE = 'data/b763_registration_2026-11-19.txt'   # ### b763's face
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-11-19-b763.zip'   # ### the last export built, b763's (data/b763_mirror_build.json, its step [23], 2026-11-20T14:31:49Z)
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
ORDER_LEDGER_SPLIT = 14680  # ### OPEN_TRAILS: W-ORD-LEDGER-SPLIT-RESOLVER (b680), (R364)(3)
TRAIL_ORDERS = 19019        # ### OPEN_TRAILS: the last open-orders line, b763's, written from the generator's output
TRAIL_RESOLVED = 19045      # ### OPEN_TRAILS: b763's items for the author's strike, in its trail
TRAIL_RETIRED = 19031       # ### OPEN_TRAILS: b763's count line of the author's prompts
#   ### b754 step zero: the carry brought b750's lines (18096/18126/18110) under these names; set to b753's here, each read from OPEN_TRAILS at 2a94bf8 (b753's trail :18134-:18182)
WATCH_LINE = 16126          # ### OPEN_TRAILS: W-ORD-QUASI-RH-FIELD-WATCH, annotated at b718's C6
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row
INSTRUMENTS = 'phase1.5/method/INSTRUMENTS.md'   # ### PLACE-papers' instruments document, its last entry I-109 (b750)
INSTRUMENTS_LAST = 109   # ### I-109 entered at b750 ([E]); none at b753 to b755; at this act two rows drafted under (R366)(3)(vi) and put to the author under (5)(iii), entered only on the author's pass (b756 defect (e))

# ### (R364)(3): the five records, in the order the ruling names them: (row, kernel, Zenodo record, the sitting row's line in data/b736_sitting.txt)
TIER3 = ((104, 'SIDE-cosmo', '19938009', 1095), (105, 'SIDE-effects', '19938005', 1105), (106, 'SIDE-trivium', '19938003', 1115),
         (107, 'SIDE-interfaces', '19931797', 1125), (108, 'SIDE-kernel', '21520474', 1135))
TIER3_BANK = 'data/b739_tier3.txt'                  # ### b754: b739's, read not written (no Zenodo field touched, (R364)(5)); the carry shifted it to b753's, which does not exist
READBACK_BANK = 'data/b739_zenodo_readback.json'

# ### the branches step zero deletes ((R372)(4)): the push-b761-* branches of the relay and PLACE-papers, by name, each read from the
# ### `--merged` listing printed before the deletes, one per message by the one-call tool, each read absent after; read at step zero
# ### (18:44:42Z, scratch merged763.py): relay push-b762-closing 3fe5b17c, push-b762-preroot d298dd45, push-b762-record efb9acb6; PLACE-papers
# ### push-b762-preroot 204aac21, push-b762-record 87cab4f2 -- five, each merged into main, push-b762-closing of the relay among them
# ### (b762's closing push made it); set by the Edit tool after `carry.py ruled` refused b761's tips carried under b762's names (R1), as at b762
DELETE = (('D:/relay', ('push-b763-closing', 'push-b763-preroot', 'push-b763-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b763-preroot', 'push-b763-record')))
DELETE_TIPS = {('D:/relay', 'push-b763-closing'): '0f9b1df2', ('D:/relay', 'push-b763-preroot'): '109f5ba7', ('D:/relay', 'push-b763-record'): 'd4ec1edb',
               ('D:/MY-DOwnloads/PLACE-papers', 'push-b763-preroot'): 'b3020098', ('D:/MY-DOwnloads/PLACE-papers', 'push-b763-record'): '7db9a66c'}
#   ### b764 step zero: set from the --merged listing (scratch merged764.py, 17:04:10Z-17:04:13Z), each merged into main; the carry had
#   ### shifted b763's names onto b762's tips
DELETE_TIPS_B763 = {('D:/relay', 'push-b762-closing'): '3fe5b17c', ('D:/relay', 'push-b762-preroot'): 'd298dd45', ('D:/relay', 'push-b762-record'): 'efb9acb6',
                    ('D:/MY-DOwnloads/PLACE-papers', 'push-b762-preroot'): '204aac21', ('D:/MY-DOwnloads/PLACE-papers', 'push-b762-record'): '87cab4f2'}   # ### b763's five, kept beside
DELETE_TIPS_B762 = {('D:/relay', 'push-b761-closing'): 'fb9fbaef', ('D:/relay', 'push-b761-preroot'): 'b700a627', ('D:/relay', 'push-b761-record'): '5839cf91',
                    ('D:/MY-DOwnloads/PLACE-papers', 'push-b761-preroot'): '1e762ee8', ('D:/MY-DOwnloads/PLACE-papers', 'push-b761-record'): 'da82a9d5'}   # ### b762's five, kept beside
# ### (R373)(4): "No other clause of this ruling removes a branch" -- no kernel branch removed at any remote; this act's own push-b763-*
# ### branches, the kernel's among them, stay for the next act's step zero
DELETE_REMOTE = ()
DELETE_REMOTE_TIPS = {}
DELETE_REMOTE_B760 = (('D:/SIDE-explicit-formula', ('push-b759-weil',)),)   # ### b760's one, (R370)(4), at a3aad4cc, the carry's shift set back
DELETE_REMOTE_TIPS_B760 = {'push-b759-weil': 'a3aad4cc'}
DELETE_REMOTE_B759 = (('D:/SIDE-explicit-formula', ('push-b757-join', 'push-b757-coeff', 'push-b758-land', 'push-b758-coeff')),
                      ('D:/SIDE-dirichlet-mod-24', ('push-b757-mod24',)))   # ### b759's five as (R369)(3) named them, the carry's shift set back
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### carried: NOT deleted, local or remote
# ### (R371)(4): "The kept branches as data/b760_closing.txt's carried list (f) names them, none moved"; b760's list is b759's (f) less
# ### push-b759-weil, so the tuple stands as b760 wrote it (to be read against data/b760_closing.txt (f) before the deletes)
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'), ('D:/SIDE-explicit-formula', 'challenge-b720-h2-sign-iff-rh'),
                 ('D:/SIDE-lv-conservation', 'scratch-b724'), ('D:/SIDE-explicit-formula', 'keiper-b725'), ('D:/SIDE-explicit-formula', 'c2-b725'),
                 ('D:/SIDE-kernel', 'rebuild-b721'), ('D:/SIDE-lv-conservation', 'rebuild-b721'), ('D:/SIDE-archimedean', 'rebuild-b721'),
                 ('D:/SIDE-frobenius', 'rebuild-b721'), ('D:/SIDE-spinor', 'rebuild-b721'), ('D:/SIDE-rcurve', 'rebuild-b721'),
                 ('D:/SIDE-explicit-formula', 'detect-b729'), ('D:/SIDE-explicit-formula', 'zq-b730'),
                 ('D:/SIDE-dirichlet-mod-24', 'push-b757-workflow'), ('D:/relay', 'corrigendum-b723'))

# ### the kernels: read; written only on the rebuild-b721 branches by (R364)(7) and the author's word (4)
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')


def _kernel_paths():
    """the kernels of data/b716_federation_pin_price.txt (1), as D:/<name>, read at import ((R364) PATHS)."""
    p = os.path.join(D, 'b716_federation_pin_price.txt')
    t = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return tuple('D:/' + m.group(1) for m in re.finditer(r'(?m)^  (SIDE-[A-Za-z0-9-]+)\s+HEAD ', t))


KERNEL_PATHS = _kernel_paths()
PATHS = ('D:/relay', PP, KERNEL_DIR, LV_DIR) + tuple(k for k in KERNEL_PATHS if k not in (KERNEL_DIR, LV_DIR))   # ### (R364)'s PATHS
EF_MAIN = '819e4a832700038d103b4efc1e0ee0f1343f7c6e'    # ### b763: SIDE-explicit-formula's main at the close -- moved from push-b763-form at v0.42 (02:22:05Z, tag object 001e94ff) after run 44646848292's success, then from push-b763-squares at v0.43 (05:34Z, tag object bcd4d481) after run 44670834879's, (8)'s W-ORD-SQUARES-AT-24 built in full (entering at a3aad4cc, EF_BASE); the local main fast-forwarded by the one-call tool after each (05:34:3xZ the second)
EF_MAIN_V042 = '4964e95758a7b1bc8c49d0972ebb18877d4f945f'   # ### b763: main after (6) alone, at v0.42, before (8)'s landing
EF_MAIN_B759 = 'a3aad4cceb41705fe9929c9b5600976eaf7434b5'    # ### b759's main at its close, v0.41, b763's entering main
LV_MAIN = '305a87c9e09c45cc8a935b1065f26f929634c707'    # ### SIDE-lv-conservation's main at the sitting's [41] (README.md alone, (R364)(3))
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
# ### the wave 1 kernels at their own pins, (name, tag, the short commit) -- b721's (R331)(7), b753's (R363)(10)
WAVE1 = (('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-archimedean', 'v0.1.0', '8019d9d'),
         ('SIDE-frobenius', 'v0.1.0', '2efe9f2'), ('SIDE-spinor', 'v0.1.0', 'b235bc6'), ('SIDE-rcurve', 'v0.1.0', 'd5f33b4'))
CHECKPOINT_STATEMENTS = (('SIDE-archimedean', 'archimedean_forces_half'), ('SIDE-frobenius', 'indicial_forces_half'),
                         ('SIDE-spinor', 'spinor_forces_half'), ('SIDE-spinor', 'half_iff_centered_zero'), ('SIDE-rcurve', 'monotone_unique_zero'))
REBUILD_BRANCH = 'rebuild-b721'          # ### b721's branches, kept, (R364)(7)'s repair made on them alone
REBUILD_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-lv-conservation', 40706311269), ('SIDE-archimedean', 40706397470),
                ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404), ('SIDE-frobenius', 40713201832))   # ### b721's, each read by its id
AXIOM_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-archimedean', 40706397470), ('SIDE-frobenius', 40713201832),
              ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404))   # ### b753's (R363)(10): the five whose axiom step was diagnosed
AXIOM_DIAG = 'data/b729_axiom_diag.txt'  # ### the routes (R364)(7) and the author's word (4) take
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
DATA_STANDING = 'data/standing_clauses_v9.txt'   # ### v8 bound the act to d9739558; v9 from that commit, which landed it at Component 1 ((R364)(2)(v))
DATA_STANDING_V9 = 'data/standing_clauses_v9.txt'
ARM_TAGS = 'data/arm_tags.json'
REPO_VISIBILITY = 'data/repo_visibility.txt'
PLAN_BANK = 'data/b744_zetabox_plan.txt'              # ### (R364)(2): W-ORD-ZETA-BOX's plan bank (b744's), read for the navigator's read, its md5 printed at step zero, no row rewritten
POSCONTROL_PLAN = 'data/b744_poscontrol_plan.txt'     # ### (R364)(2): W-ORD-POSITIVE-CONTROL's plan bank (b744's), read the same way
PLAN_BANKS = (POSCONTROL_PLAN, PLAN_BANK)             # ### the order the discharges are entered: the positive control first
PLAN_MD5S = {'data/b744_poscontrol_plan.txt': 'b72ad7bbe28693a1192cfa60329fc607',   # ### b753's step-zero print, LF, 137 lines; re-printed by this act's citation check
             'data/b744_zetabox_plan.txt': 'ef777cc24752911990d56d2214fe38b6'}      # ### 183 lines
CONTROLS_BANK = 'data/b745_controls.txt'              # ### (R364)'s read-first list: b745's result bank (pc_online and the generic theorem :96-:127), read not written
CONTROLS_NOTES = 'data/b745_controls_notes.txt'       # ### b745's notes, read not written
SECTION_FILE = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'   # ### (R364)(2): the paper, section 2 written by one PLACE-papers write on the author's pass
SECTION_BANK = 'data/b763_ledgers.txt'      # ### b763's ledgers bank (the orders by their triggers), read not written
SECTION4_BANK = 'data/b748_section4.txt'              # ### b748's §4 bank, read not written
SECTION1_BANK = 'data/b747_section2.txt'              # ### b747's section bank (§2), read not written
INTEGRATION_DRAFT = 'data/b746_integration_draft.txt' # ### b746's canon text for the stages, entered at b753 as XXIII, read not written
ORDER_DRAFT = 'data/b746_order_draft.txt'             # ### (carried name) b746's order draft, read not written; no order entered this act
READBACK_747 = 'data/b747_zenodo_readback.txt'        # ### b747's read-back, read not written; no Zenodo call this act ((R364)(6))
RULES_747 = 'data/b764_rules.txt'                     # ### (R364)(3): the seat's reading of the corrigendum's repairs, each for the author's strike
REGISTRATIONS = PLAN_BANK                             # ### (carried name)
PREV_BUILD_BANK = 'data/b745_controls.txt'            # ### b745's result bank (b753 built nothing)
PREV_BUILD_MD5 = None                                 # ### printed by the citation check at step zero
PREV_STATEMENTS_BANK = 'data/b744_zetabox_plan.txt'   # ### b744's other plan
STATEMENTS_BANK = PLAN_BANK                           # ### (carried name)
C7_PLAN = STATEMENTS_BANK
S6_PLAN = STATEMENTS_BANK
BUILD_BANK = CONTROLS_BANK                            # ### (carried name) the act's last result bank
NOTES_BANK = CONTROLS_NOTES
REG_WALK_COMMIT = '15cb6cc4'                     # ### b721's H-C2-WALK commit (carried name; b753's walk read under it)
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
#   ### read not written (carried name); b753 wrote no coefficient bank
COMPUTE_BANKS = ('data/b764_corrigendum.txt', 'data/b764_price.txt', 'data/b764_repairs.txt', 'data/b764_close_yield.txt',
                 'data/b764_imp2tau.txt', 'data/b764_address_scan.txt')
#   ### the banks of (R374)(1)-(14) as the ruling names them, each written by its component; the three dispatches of (7) alone;
#   ### set by the Edit tool to the banks as written, before the lock
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt',
              'data/b729_read_calls.txt', 'data/b730_read_calls.txt', 'data/b763_read_calls.txt', 'data/b764_read_calls.txt')

# ### THE SUITE'S PARTS: ten, as b753 split them under (R363)(2)(vi) and b675 rules row (2) (standing-a in two, G-NO-SORRY-MAIN's kernels
# ### halved, and the chain's first half in four, b2a-b2d); data/act_current.json committed them ten at b754's step zero (22f59d27), no
# ### component splitting them this act, so PARTS_AT_STEP_ZERO is PARTS
PARTS = ('standing-a1', 'standing-a2', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d', 'standing-b3', 'act')
PARTS_AT_STEP_ZERO = PARTS
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b764'))
CHAIN_QUARTERS = (('b624', 'b627'), ('b628', 'b631'), ('b632', 'b635'), ('b636', 'b658'))   # ### carried from b753
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### set by the Edit tool when a component adds a standing arm
SHARED_APPENDED = ('data/b675_corrigenda.txt',)   # ### (R364)(2): the corrigenda row
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md', 'ERRATA.md', 'BIBLIOGRAPHY.md')
#   ### b764 step zero: (R374)(14)'s (W) list in PLACE-papers -- FINDINGS.md, OPEN_TRAILS.md, ERRATA.md ([E1] of (9)(a), one entry at
#   ### the file's end) and BIBLIOGRAPHY.md (the register brought current by W-ORD-BIBLIOGRAPHY-LINK, [A5] of (R373), where (8) builds it),
#   ### each by its path at PLACE-papers 7db9a66c (git ls-files, 2026-11-20T17:0xZ); REGISTRY not written; no sentence of any paper
#   ### written or edited ((R374)(13)); no new file
#   ### b763 step zero: (R373)(13)'s (W) list in PLACE-papers -- FINDINGS.md, OPEN_TRAILS.md and phase1.5/method/THE_METHOD_CANON.md
#   ### (section XXV of (9), [C1], appended at its end, no byte above it changing); REGISTRY not written (N3); no new file
#   ### b762 step zero: (R372)(13)'s (W) list in PLACE-papers -- FINDINGS.md, OPEN_TRAILS.md, REGISTRY.md and the new file of (6),
#   ### beside day1/ONE_PAGE_PROOF.md, which is not in the list: (6) orders it unedited, N3 its bytes equal before and after. THE NAME
#   ### (10:1xZ, said to the author before Component 4 as (6) orders): a standing reader finds a document's editions by the stem of its
#   ### deposited file -- tools/standing/subject.py family_of (:151, :157-:159) takes a paper's family by removing the `_v<n>` mark and
#   ### live_papers (:175-:204) reaches every file of REGISTRY d1-8's family day1/ONE_PAGE_PROOF -- so the file is day1/ONE_PAGE_PROOF_v2_0.md,
#   ### nothing else changing (stage one set day1/ONE_PAGE_v2_0.md, the ruling's first name)
#   ### b761 step zero: (R371)(13)'s (W) list in PLACE-papers -- FINDINGS.md, OPEN_TRAILS.md, REGISTRY.md and
#   ### phase1.5/method/THE_METHOD_CANON.md (the section [A2] of (7) appended at its end), each by its path at PLACE-papers 91b69bf1 (git
#   ### ls-files, 2026-11-18T21:4xZ); no paper written or edited beyond [A2] ((R371)(12)), no new file
#   ### b760 step zero: (R370)(13)'s (W) list in PLACE-papers -- FINDINGS.md, OPEN_TRAILS.md, REGISTRY.md, ERRATA.md,
#   ### THE_KEYSTONE_CENSUS_v0_8_3.md, day1/Which_Structure_Confines_v2_5_0.md (the new file of (7)) and
#   ### phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md (the five keys of (9)), each by its path at PLACE-papers d711a5d6 (the ruling
#   ### names each by path but the census); v2.4.0 and v2.3.1 of Which Structure Confines and v0.1 of the Epstein document are not in the
#   ### list: (7) and (9) order them unedited, N4 their bytes equal before and after
#   ### b759 step zero: (R369)(11)'s (W) list in PLACE-papers -- FINDINGS.md, OPEN_TRAILS.md, REGISTRY.md, ERRATA.md, FACES_LEDGER.md,
#   ### SPIRAL_MAP.md, THE_KEYSTONE_CENSUS_v0_8_3.md, the new file of (8) and the eight other documents of (9) (C1-C10 of the text
#   ### block's BLOCK D), each by its path at PLACE-papers 4ea41948 (git ls-files, 2026-11-17T18:2xZ; the ruling names most by file name alone);
#   ### v0.1 of the Epstein document is not in the list: (8) orders it unedited, N4 its bytes equal before and after
PP_WRITTEN = PP_EDITED
PP_NEW = ()   # ### (R374): no new file in PLACE-papers
# ### (R364) amendment row 3 (6): THE (W) ENTRIES (R364)(8) GIVES IN WORDS, each with the clause that gives it, read by tools/standing/wlist.py
# ### (word_rows) into the (W) bank and by tools/standing/cites.py's ferry_paths for a name in no tree. The entries (8) gives "on its item's
# ### pass and not otherwise" are not rows here: each enters by its item's route ((R364)(3)(xvi), `amend.py pass`) on the pass.
W_WORDS = (('relay/HANDOFF.md', '(R374)(14): HANDOFF.md'),
           ('relay/data/b764_address_scan_commits.txt', '(R374)(3), (14): b763`s carried files -- this act`s per-commit scan bank, by (R364)(3)(iii)`s route'),
           ('relay/data/b765_address_scan_commits.txt', '(R374)(14): the scan banks -- the next act`s per-commit scan bank, by (R364)(3)(iii)`s route'),
           ('relay/data/b763_relay_push-b763-closing_push_out.txt', '(R374)(3), (14): b763`s carried files -- the closing push-out bank with its as-of lines, committed alone'),
           ('relay/tools/mirror_prevbuild.json', '(R374)(3), (14): b763`s carried files -- the builder`s state file as b763`s build wrote it'),
           ('relay/tools/acts/b764.py', '(R374)(14): tools/acts/b764.py'),
           ('SIDE-explicit-formula/.github/workflows/build-module.yml', '(R374)(7), (14): in SIDE-explicit-formula the workflow`s file alone -- the restore of the kernel`s own build, on push-b764-runner made at main'))
#   ### b764 step zero: (R374)(14)'s (W) list in words: the banks as data/b764_* and their generators as tools/b764_*.py (standing kinds,
#   ### tools/b764_yield.py and tools/b764_imp2tau.py among them, carried as tools of this act by (6) and (9)(b)); tools/acts/b764.py;
#   ### b763's carried files by name ((R374)(3): the closing push-out bank, data/b764_address_scan_commits.txt and tools/mirror_prevbuild.json);
#   ### HANDOFF.md; tools/standing/ with VERSION (a standing kind; moved by (5) and (7) alone, (R374)(12)); PLACE-papers by PP_EDITED; in
#   ### SIDE-explicit-formula .github/workflows/build-module.yml alone ((R374)(7), (13)); the kernel files of b763's (6)-(8) drop
# ### b763 Component 1: the kernel files of (6) and (7) named before any is written ((R373)(13), "in SIDE-explicit-formula the files of (6),
# ### (7) and (8) with print_targets.txt"); (7)'s proof file and each (8) file take their row when named
#   ### b763 step zero: (R373)(13)'s (W) list in words: the banks as data/b763_* and their generators as tools/b763_*.py (standing kinds);
#   ### tools/acts/b763.py; b762's carried files by name ((R373)(3): the closing push-out bank, data/b763_address_scan_commits.txt and
#   ### tools/mirror_prevbuild.json); HANDOFF.md; tools/standing/ where (5) moves it (none at step zero); PLACE-papers by PP_EDITED; in
#   ### SIDE-explicit-formula the files of (6), (7) and (8) with print_targets.txt, each new file's row added by the Edit tool when it is named
#   ### b762 step zero: (R372)(13)'s (W) list in words: the banks as data/b762_* and their generators as tools/b762_*.py (standing kinds);
#   ### tools/acts/b762.py; b761's carried files by name ((R372)(3): the closing push-out bank, data/b762_address_scan_commits.txt and
#   ### tools/mirror_prevbuild.json); HANDOFF.md; no kernel path, (R372)(12) touching no kernel; no tools/standing/ path ((R372)(11));
#   ### the terminal-table files, b760's carried files at b761, are no part of (R372)(13)'s list and drop; PLACE-papers by PP_EDITED
#   ### b761 step zero: (R371)(13)'s (W) list in words: the banks as data/b761_* and their generators as tools/b761_*.py (standing kinds);
#   ### tools/acts/b761.py; b760's carried files by name ((R371)(3): the closing push-out bank, data/b761_address_scan_commits.txt,
#   ### tools/mirror_prevbuild.json, data/terminal_table_prior.json and data/terminal_table_run.txt); HANDOFF.md; no kernel path, (R371)(12)
#   ### touching no kernel; no tools/standing/ path by the ruling's words ((R371)(11)); PLACE-papers by PP_EDITED
#   ### b760 step zero: (R370)(13)'s (W) list in words: the banks as data/b760_* and their generators as tools/b760_*.py (standing kinds);
#   ### tools/acts/b760.py; tools/standing/ with VERSION (standing kinds); b759's carried files by name ((R370)(3): the closing push-out
#   ### bank, data/b760_address_scan_commits.txt and tools/mirror_prevbuild.json); HANDOFF.md; no kernel path, (R370)(12) writing no kernel
#   ### and (4)'s removal writing no file; PLACE-papers by PP_EDITED
#   ### b759 step zero: (R369)(11)'s (W) list in words: the banks as data/b759_* and their generators as tools/b759_*.py (standing kinds);
#   ### tools/acts/b759.py; tools/standing/ with VERSION (standing kinds); b758's carried files by name ((R369)(2): the closing push-out
#   ### bank, tools/mirror_prevbuild.json and data/b759_address_scan_commits.txt); HANDOFF.md; in SIDE-explicit-formula
#   ### Schema/Wide/HalfScaleControl.lean and print_targets.txt by the paths the tree holds at 630cba16; PLACE-papers by PP_EDITED
#   ### b755 step zero: b754's rows (CLAUDE.md, the four files of its step-zero restore) dropped -- (R365)(8)'s (W) list names neither;
#   ### data/b755_rules.txt, the carried capture and tools/mirror_prevbuild.json stand among the standing kinds (tools/standing/wlist.py)
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the re-cut's merge (kept for the kernel rows); the MANIFEST control's reference
#   ### is the commit the mirror is built at from v1.2.1
NEXT = 'the act after this one, as the author answers at the root (the answers bank) ((R374)(14)): the proof of the control`s failure from its coefficients, in the reading whose upper price the table of (9)(c) puts below the others, opened by the trial of (7) where that was carried; or the registration H-ONSET-DENSITY, with W-ORD-ADMISSIBLE-CONE joined to it by [A2] of (R373); or the reading of the eighteen named premises under W-ORD-PREMISE-POSITIONS; or another the author names'
NEXT_ACT = 'b765'


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
ACT_CURRENT_COMMIT = 'afb63f4b'   # ### data/act_current.json for b764 committed alone through the one-call tool ((R374)(3)), the scan in the call (17:06:15Z); its row step 1
STEPZERO = 'baff91ad'       # ### the first of b763's carried files committed alone ((R374)(3)): the closing push-out bank with its as-of lines, step 2 (17:06:43Z)
# ### b764: b763's carried files, each committed alone through the one-call tool ((R374)(3)), in the order made: (commit, step, the files);
# ### tools/mirror_prevbuild.json NOT CARRIED: its working bytes equal HEAD's with their 89 carriage returns removed (scratch prevbuild764.py,
# ### 17:05Z), the add staged nothing (17:07:06Z) and the tool refused the commit, "nothing staged in D:\relay" (17:07:21Z) -- (R374)(3):
# ### nothing of it carried, the refusal printed
# ### b762: b761's carried files, each committed alone through the one-call tool ((R372)(3)), in the order made: (commit, step, the files);
# ### tools/mirror_prevbuild.json NOT CARRIED: its working bytes equal HEAD's with their 89 carriage returns removed (09:53Z), the add staged
# ### nothing and the tool refused the commit, "nothing staged in D:\relay" (09:53:33Z) -- (R372)(3): nothing of it carried, the refusal printed
# ### b763: b762's carried files, each committed through the one-call tool ((R373)(3)), in the order made -- all three carried, the
# ### builder's state file with data/act_current.json naming it in shared_edits (the tool refusing a shared tool unnamed there, 18:46Z)
STEPZERO_CARRIED = (('baff91ad', 2, 'the closing push-out capture'), ('8f4c353d', 3, 'data/b764_address_scan_commits.txt'))
STEPZERO_CARRIED_B763 = (('9fbd3ac6', 2, 'the closing push-out capture'), ('b17f66d6', 3, 'tools/mirror_prevbuild.json with data/act_current.json'),
                         ('dc063f7d', 4, 'data/b763_address_scan_commits.txt'))   # ### b763's, kept beside (the carry had shifted its scan bank's name to b764's)
STEPZERO_PREDICTIONS = '69200958'   # ### (R374)(10): [P1] banked verbatim as data/b764_navigator_predictions.txt (scratch pred764.py, 17 lines, sha256 49bb42fb...) and committed alone before Component 1, step 4 (17:08:35Z)
STEPZERO_CARRIED_B762 = (('6052a453', 2, 'the closing push-out capture'), ('6096dca3', 3, 'data/b763_address_scan_commits.txt'))   # ### b762's, kept beside
STEPZERO_STEPS = None             # ### b761's step rows stand committed by b761 itself (its record's step-row commit): nothing carried
STEPZERO_TABLE = ()               # ### none: (R372)(3) carries no terminal-table file (b761's were b760's, at its steps 5 and 6)
STEPZERO_TABLE_B761 = ('c4670f7f', '6059f159')   # ### b761's, kept beside for the carried arms
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None   # ### tools/mirror_prevbuild.json NOT CARRIED ((R374)(3)): its difference its line ends alone, the add staged nothing, the tool refused the commit ("nothing staged in D:\relay", 17:07:21Z)
STEPZERO_REFUSALS = ()   # ### b761 left no refusals bank uncommitted
STEPZERO_SCAN = '8f4c353d'   # ### data/b764_address_scan_commits.txt as b763's closing step-row commit began it, with this act's step-zero runs, committed alone, step 3 (17:07:49Z)
STEPZERO_SCAN_B763 = 'dc063f7d'   # ### b763's, kept beside
STEPZERO_BANKS = '3c8e5ebc'      # ### step zero's banks and carried tools, one commit (data/b764_stepzero.txt among them), step 5, 17:51:17Z
STEPZERO_AFTER = STEPZERO_BANKS      # ### b756: no restart and no stop at step zero; step zero's banks the last step-zero commit; the name kept for the carried arms (b754's 65972bf1), each rewritten at Component 6
STEPZERO_BANK_COMMIT = STEPZERO_BANKS
STEPZERO_ANSWERS = None
STEPZERO_ANSWERS_FULL = None   # ### the same, as each dispatch row's licence names it
# ### N2: each generator commit (relay) before the zq-b730 commit holding the modules it generated
GEN_COMMITS = ()   # ### b754: no generator run, no Lean file written ((R364)(8))
GEN_COMMITS_B745 = (('04e7f854', '32bad89a'), ('32a5c72a', '32bad89a'), ('32a5c72a', '1e658870'))   # ### (R364)(4)(c): the Z4 generator's relay commits, each before the zq-b730 commit it fed (Signs.lean at t = 16, then 16 and 12)
GEN_MD5 = {'Signs': '4ef0a0f5606052abf21c797a9aba64a2'}   # ### the generator's output at 32a5c72a (`<out> 16 12`), Signs.lean at zq-b730's tip by md5
GEN_MD5_PREV = {'FrontierData': 'c8e320f9db1a12622cc147555496cf11', 'Nodes0': '7cb04ecfd3649a1daf5633de691df670',   # ### b742's generator's output at 3194b6eb (carried name, read not run)
                'Nodes1': 'a20f1f00a156e59e97f841beb8d89a76', 'Nodes2': 'efff8c97b5f9879bcf12e3f79628dc64',
                'Nodes3': '09de4381169541faf5f0066bf66905e7', 'NodesF': 'd37bbfbb8c81165521b77de16022069a'}
GENERATOR = 'tools/b745_zbgen.py'   # ### b745's (carried name, read not run): Signs.lean generated from it (md5 ac82341c at 32a5c72a); the carry shifted it to b754's, which does not exist
VISIBILITY_COMMIT = None
COMPUTE_TOOLS = ()                      # ### set by the Edit tool when a component seals a compute tool
REPAIRED_TOOLS = tuple(p[len('tools/'):] for p in json.load(io.open(os.path.join(D, 'act_current.json'), encoding='utf-8'))['shared_edits'])
#   ### (R364)(2), b753 event (2): read from data/act_current.json, the one hand list, which G-ACT-CURRENT reads against git; sealed before the suite runs (b696's form)
REPAIRED_DATA = ()
# ### b721's trap (event 11): the standing part of the sealed list read from the directory, not a carried tuple
STANDING_FILES = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing')) if f == 'VERSION' or f.endswith('.py')))
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset, sealed by hash beside the act's tools
# ### the seven close tools are tools/standing/fold.py's renders of its templates (tools/standing/fold/<tool>.tpl) with the act's arms module
# ### (tools/acts/b754.py) -- every byte a render reads sealed beside the act's tools; report.tpl left out of the seal (b708's report row)
FOLD_FILES = tuple(sorted('standing/fold/' + f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing', 'fold')) if f.endswith('.tpl')
                          and f != 'report.tpl')) + ('acts/b764.py',)
NEW_TOOLS = NEW_TOOLS + FOLD_FILES
STANDING_VERSION = 'v1.37.2'            # ### entering; (R374)(5) moves tools/standing/ one commit a key, VERSION with each, and (7) where the dispatch route or the workflow arm needs it ((R374)(12)); set at the close
STANDING_VERSION_ENTERING = 'v1.37.2'
LEAN_TREES = (('D:/SIDE-explicit-formula', '819e4a83'), ('D:/SIDE-explicit-formula', 'ec14e9d9'), ('D:/SIDE-explicit-formula', 'a59632eb'),
              ('D:/SIDE-dirichlet-mod-24', 'e5ebdd15'))   # ### (R374)(7), (13): SIDE-explicit-formula's workflow file alone written, on push-b764-runner made at main, v0.43 (819e4a83), main moved after the trial's success alone, no tag cut; SIDE-dirichlet-mod-24 at v0.2.0, untouched (N5); SIDE-kernel unmoved
# ### b764 step zero (17:3xZ, after the citation check's dry halted on two Lean paths): the trees are the pins (R374)'s SCOPE READ names for
# ### its Lean reads (data/b764_ferry.txt :3): "at v0.43" (819e4a83), "on push-b763-arith at ec14e9d9" (ControlFailureStatement.lean) and
# ### "on push-b763-keiper at a59632eb" (KeiperPolygamma.lean); the carry had left main's pin alone, so the reader read the two branch files
# ### against main and halted (ABSENT FROM THE TREE AT ITS PIN), each file standing at its named commit (scratch facts764f.py: 76 and 136 lines)
# ### v1.18.0, (R364)(2)(ii): the act's banks whose comparative sentences the citation check reads, and a reading row for each word (tools/standing/cites.py
# ### comparative_rows); set by the Edit tool as Components 2-4 write the banks, before the lock
COMPARATIVE_BANKS = ('data/b764_corrigendum.txt', 'data/b764_price.txt', 'data/b764_defects.txt')
COMPARATIVE_ROWS = ()   # ### comparative word in them ("at least" excepted by the reader), so no reading row; the check reads the three for one
#   ### the trees the ruling's Lean paths are read against: zq-b730's tip, and Mathlib at its pin (the ferry's "Mathlib at the pin: Analysis/Complex/AbsMax.lean :405, ...")
STANDING_CHANGED = ('VERSION', 'commit.py')   # ### b763 (R373)(5): v1.37.1 to v1.37.2's changed files, read at the close by git diff --name-status 3fe5b17c HEAD -- tools/standing/
STANDING_NEW = ('v1372.py',)                  # ### its controls tool, committed before its first run (d34f7323)
STANDING_CHANGED_B762 = ()   # ### b762's: (R372)(11), no standing change, kept for the carried arms
STANDING_CHANGED_B760 = ('VERSION', 'commit.py', 'handoff.py', 'subject.py')   # ### b760's: v1.36.8 to v1.37.1's changed files (4), kept for the carried arms that cite them
STANDING_NEW_B760 = ('v1368.py', 'v1369.py', 'v1370.py', 'v1371.py')
# ### b753's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = '0f9b1df2'    # ### b763's last commit (its closing step row), the act's relay base
B714_RECORD = '9079160c'     # ### b763's record commit (relay)
B714_ROOT = '34de7cffdf0093e2a1509dd764cc5c24b5667812f4e11139fe73409b9579dd54'   # ### b763's root, data/act_roots.txt's last row
B723_ROOT_BANKS = 'c1349d62'  # ### b763's root commit, the banks its root rode with
# ### later stages: the commits of the components, read from the logs after each was made (None until made)
C1_STANDING = None           # ### (R374)(12): no change under tools/standing/ in Component 1; the changes of (5) are Component 2's, one commit a key (data/b764_steps.json)
C1_LOCKGATE = 'dbd562bb'     # ### b763: tools/b763_lockgate.py carried and set, committed before any run with the face and probe-path tools (step 57, 04:37:20Z)
C1_STANDING_LATER = (('(8)(ii)', 'v1.35.5', 'e0428564'),)   # ### Component 6, (R367)(8)(ii): the closing's one count in one form, a version commit of its own with its controls 6 of 6 (step 51)
C5_FAULTS = ()   # ### (carried name) no fault count this act
DOORS = ('tools/b764_doors.py', '2bc7eca8', 'data/b764_doors.txt', 'c98beed0')   # ### (R367)(8)(v): the two passed descriptions sent by gh and each read back equal (tool step 48, bank step 50)
C5_LANDED, C5_CARRIED = 5, 0   # ### the repairs of (8): (i) the cut, (ii) v1.35.5, (iii) the gh-call reader, (iv) REGISTRY's header, (v) the two descriptions; none carried
C1_STANDING_REPAIR = None          # ### none in Component 1
C4_STANDING = None                 # ### none
C1_RELAY = 'f66a6878'        # ### b764: the c1 route written in place of the carried stub, the events rows (13)-(29), STEPZERO_BANKS (step 6, 18:02:43Z) -- set at [K5]'s needle call, which read it None at sources (18:47Z)
C1_CEILING_TOOL = ('0826dbaf', '700efb97')   # ### b763: tools/b763_ceiling.py committed before its run (step 6), and its control (6) re-planted before any reading (step 7, defect (e))
C1_CORR = '89fbe2f4'         # ### b764: the corrigendum banks, data/b764_corrigendum.txt, .json, the landing bank and the corrigenda bank's row (84) (step 8, 18:04:46Z) -- b763's 618a8486 carried until [K5]'s needle call
C1_CORR_B762 = '6918f5d9'    # ### b762's, kept beside for the carried arms
C1_CORR_B761 = '9a33e6b3'    # ### b761's, kept beside for the carried arms
B757_CLOSE = '401d3bda'      # ### b758 (R368)(1): b757's steps [22]-[25] under v1.35.7, committed under component 1 (01:07:08Z, events (19))
STATEMENTS_GEN = '4f069656'  # ### (R368)(7): tools/b758_statements.py as last committed before its bank (events (42))
KERNEL_DELETES = ()   # ### b763: (R373)(4) removes no kernel branch; this act's push-b763-* branches stay for the next act's step zero
KERNEL_DELETES_B760 = (('push-b759-weil', 'a3aad4cc'),)   # ### b760's (R370)(4): removed at SIDE-explicit-formula's remote by `commit.py SIDE-explicit-formula rdelete push-b759-weil` under v1.37.1 (flag 09:34:35Z), read back ABSENT
KERNEL_DELETES_B759 = (('push-b757-join', '6568e9c7'), ('push-b757-coeff', '596d1c9e'), ('push-b758-land', 'd1afb4fc'), ('push-b758-coeff', '630cba16'),
                       ('push-b757-mod24', 'e5ebdd15'))   # ### b759's five, the carry's shift of b758's names set back
# ### (R369)(3): the five kernel branches removed at their remotes by tools/standing/commit.py `rdelete` (v1.36.3, (R369)(4)(i), relay 983ca5b1,
# ### its controls 10 of 10), one a message, each after a flag read (GO), 19:09:51Z-19:10:41Z: the four of SIDE-explicit-formula, each tip an
# ### ancestor of the remote's main 630cba16, and push-b757-mod24 of SIDE-dirichlet-mod-24 at its main e5ebdd15; each read back absent by the
# ### route's ls-remote and again by one listing a kernel; none forced; the clones' own branches of the names not touched
KERNEL_DELETES_HALT = ()
# ### b758's halt as its worklist stood (the carry shifted its names): the four of (R368)(5), push-b757-join, push-b757-coeff, push-b758-land
# ### and push-b758-coeff, carried for want of the route; removed at b759 by (R369)(3) above
KERNEL_DELETES_HALT_B758 = ('the delete of a kernel`s branch at its remote', 'push-b757-join', 'push-b757-coeff', 'push-b758-land', 'push-b758-coeff')
CHAIN_WORDS = {}             # ### b758: each CHAIN and PP_CHAIN key's words in the entry's order paragraph, set with CHAIN at Component 5
C1_RULES = None        # ### b761: (R371) orders no rules bank and no data/b761_rules.txt is written; b760's was data/b760_rules.txt row (a) at relay 34390a25; data/b756_rules.txt's rows (a)-(c) in force
B756_RULES = ('data/b756_rules.txt', '0a151012')   # ### the rule this act works by ((R366)(2)), its bank and b756's commit carrying it; b758: the carry had shifted the path to b757's name, which no commit holds (defect (e))
RULES_COMMITS = ()
C1_CEILING = '4565bf58'      # ### b763 (R373)(3): the commit carrying data/b763_ceiling.txt's last reading, after Component 3 (03:46:09Z), with the outcomes of (7) (step 46)
C1_PP = 'e383d313'           # ### PLACE-papers: FINDINGS -- the corrigendum for b763 at :15865, FINDINGS alone (step 7, 18:03:57Z) -- set at [K5]'s needle call
C1_TAG_PP = ()                     # ### (carried name) no tag note this act
C1_DISCHARGE_PP = ()               # ### (carried name) no discharge this act
C2_TOOL = None                     # ### (carried name) no driver this act
WEIGHT_LINE = None   # ### WEIGHT_LINE LEFT EMPTY BY (R374)(1): b763 at its weight within the corrigendum, no weight line of its own (v1.38.1 [K1]'s marker)
CORR_LINE = 15865    # ### FINDINGS: the corrigendum for b763 (Component 1, PLACE-papers e383d313; data/b764_corrigendum.json entry_line), set at [K1]'s repair -- left None after the write, the fault [K1] names
NEXT_TRAIL_LINE = 18491      # ### OPEN_TRAILS: (R367)(1)'s dated line giving b756's answer, in (9)'s block (Component 6, PLACE-papers b14256c2)
DIFFERS_LINE = None   # ### LEFT EMPTY BY (R374)(13): no DIFFERS entry, ERRATA and BIBLIOGRAPHY.md the two PLACE-papers files beside FINDINGS and OPEN_TRAILS (v1.38.1 [K1]'s marker)
ERRATA_LINE = None   # ### still to set: [E1] at ERRATA's end under (R374)(9)(a), Component 4 (b760's E-2026-11-18-1 at :1127, PLACE-papers f47d90f0)
C2_PLAN_FIRST = None   # ### Component 2's first relay commit (the first key of (5)'s order of repair, [K10])
C2_RELAY = None   # ### Component 2's last relay commit (C2_RELAY_ALL, the list "set as each is made" that no arm read, removed at v1.38.17 by (R374)(5) [K4])
# ### (R366)(4): each tool of the map beside its banks -- (name, generator, the generator's commits before the bank, bank, the bank's commit)
C2_MAP = (('the constellation rerun', 'tools/b764_constellation.py', ('3e112065', 'd2f78fab', '16ba8fbb', 'e4701c5f'),
           'data/b764_constellation_summary.txt', '069271bb'),
          ('the reverse read', 'tools/b764_reverse.py', ('d2f78fab', '16ba8fbb'), 'data/b764_reverse_read.txt', '069271bb'),
          ('what the two find beyond (3)', 'tools/b764_reverse.py', ('d2f78fab', '16ba8fbb'), 'data/b764_beyond_three.txt', '069271bb'))
C2_WALK = ('tools/b764_coeffs.py', '3bdb6561', 'data/b764_walk.txt', '9a989df8')   # ### (generator, its commit, bank, the bank's commit)
REG_WALK = ('data/b753_registrations.txt', '3f865479')   # ### H-C3-LAW's registration read at its blob ((R365)(3)), the commit data/b755_walk.txt names
# ### Component 3 ((R365)(5)(i), (4)): the literature bank, the candidates' generators each committed before its run, the candidates bank with
# ### the prior clause, the ceiling read again; each candidate (label, generator, the generator's commits before its bank, bank, the bank's commit)
C3_LITERATURE = '51739651'
C3_CANDS = (('(a)', 'tools/b764_closed.py', ('a7034608',), 'data/b764_cand_a.txt', '1b84e4b1'),
            ('(h)', 'tools/b764_zlist.py', ('1b84e4b1',), 'data/b764_cand_h.txt', 'ea99215e'),
            ('(c)', 'tools/b764_cands.py', ('ea99215e', '1b361013'), 'data/b764_cand_c.txt', 'b4668b52'),
            ('(j)', 'tools/b764_cands.py', ('ea99215e', '1b361013'), 'data/b764_cand_j.txt', 'b4668b52'),
            ('(k)', 'tools/b764_cands.py', ('ea99215e', '1b361013'), 'data/b764_cand_k.txt', 'b4668b52'),
            ('(l)', 'tools/b764_cands.py', ('ea99215e', '1b361013'), 'data/b764_cand_l.txt', 'b4668b52'))
C3_CANDIDATES = 'aa102044'   # ### data/b755_candidates.txt with the prior clause, data/b755_registrations.txt's first commit (step 17)
# ### Component 4 ((R365)(5)(ii), (iii)): each rule committed alone, the list of roots, the engine, the list and the two verdicts
C4_RULE_ZEROS = '11fc3c93'   # ### H-ZEROS-FROM-PRIMES alone (step 19)
C4_RULE_RECUR = 'a937fbb7'   # ### H-RECURRENCE beside it, with its null's generator and seed, tools/b755_recur.py (step 20)
C4_ROOTS = 'e21b5c8c'        # ### data/b755_roots_59.txt, .json (step 21)
C4_ENGINE = '2b4a3942'       # ### tools/b755_list.py and the verdict mode of tools/b755_zlist.py, before any band ran (step 22)
C4_LIST = 'b03fc15e'         # ### the certified list, its controls and the two verdicts (step 23)
C5_GEN = 'fa2b038e'          # ### Component 5, (R365)(6): tools/b755_census.py committed before its run (step 24)
L16_GEN = '1c427045'         # ### Component 6, (R365)(7): tools/b755_l16.py committed before its run (step 26)
L16_PP = 'f948f606'          # ### PLACE-papers: OPEN_TRAILS.md, the dated head and the [L16] line (step 27)
L16_BANK = 'f6daeed1'        # ### the relay commit carrying data/b755_l16.json, (7)'s write and confirm bank (step 28, 2026-11-15T00:34:03Z)
# ### b755, Component 6: every generator of the act beside the bank it wrote -- (name, generator, the generator's commits before the bank, bank,
# ### the bank's commit); read by the act module's N2 arms and the record's N2 (each generator committed before its run, its commits without
# ### the bank and the bank's without the generator)
GENS_B755 = ()   # ### b755's list (the walk, the candidates, the rules at -59, the census, [L16]) stands in git at tools/b755_worklist.py
# ### b756, Component 6: every tool of the act committed before the bank it wrote -- (name, tool, its commits before the bank, bank, the
# ### bank's commit); (4)'s two ((R366)(4): each committed before its run) and the five of (3) to (5) committed so; the three of (6) (the
# ### fault count, the placing, the README route) went in with their banks in one commit each, (6) ordering no commit before a run, and
# ### stand apart in GENS_WITH_BANK
# ### b758, Component 5: every tool of the act committed before the bank it wrote -- (name, tool, its commits before the bank, bank, the
# ### commit carrying the bank as it stands at HEAD); each read by git at 03:5xZ (scratch reads, nothing written): the tool's first add the
# ### first of its commits, each of them carrying the tool and not the bank, the bank's commit the bank and not the tool, the blob at that
# ### commit equal to the working tree. The statements, the notes and the controls bank added as each is banked; the outcomes and the
# ### ceiling set again at their last writes
# ### b759, before the lock: every tool of the act committed before the bank it wrote, each read from git (scratch files759.py, read-only,
# ### 21:5xZ): the tool's first add the first of its commits, each of them carrying the tool and not the bank, the bank's commit (as it stands
# ### at HEAD) the bank and not the tool. tools/research/reproduce.py is a standing tool (its bank (11)'s) and stands apart
# ### b760, Component 6: every tool of the act committed before the bank it wrote, each read from git (scratch steps760.py, read-only, the
# ### step rows with each commit's files, 11:0xZ): the tool's first add the first of its commits, each of them carrying the tool and not the
# ### bank, the bank's commit (as it stands at HEAD) the bank and not the tool. The edition tool's commits before each bank are those before
# ### the bank was written (the search and the diff at beb7b07b, the cut again at 6b639c83, the late search at 35371470); the address scan's
# ### bank is written at the record by its standing route; tools/research/reproduce.py is a standing tool (its bank (12)'s) and stands apart
# ### b761, Component 6: every tool of the act committed before the bank it wrote, each read from git (scratch steps761.py, read-only, the
# ### step rows with each commit's files, 23:4xZ): the tool's first add the first of its commits, each of them carrying the tool and not the
# ### bank, the bank's commit (as it stands at HEAD) the bank and not the tool. The orders roster (data/b761_orders.txt) is written by the
# ### standing reader tools/standing/orders.py and the reproduce bank by tools/research/reproduce.py, each a standing tool, and stand apart
# ### b762, Component 6: every tool of the act committed before the bank it wrote, each read from git (scratch files762.py, read-only, the
# ### step rows with each commit's files, 11:2xZ): the tool's first add the first of its commits, each of them carrying the tool and not the
# ### bank, the bank's commit (as it stands at HEAD) the bank and not the tool. The registration was written by the Write tool ((R372)(9)), the
# ### corrigendum by the act module's c1 route, the roster by the standing reader tools/standing/orders.py and the reproduce bank by
# ### tools/research/reproduce.py, and stand apart
# ### b763, Component 6: every tool of the act committed before the bank it wrote, each read from git (scratch files763.py, read-only, the
# ### step rows with each commit's files, 04:5xZ); the pre-send tool by its first bank's last writing and by its last bank; the outcomes and
# ### the ledgers set when their banks are written after (8)'s runs are read. The dispatch rows are written by the dispatch tool's
# ### routes and the reproduce bank by tools/research/reproduce.py, and stand apart
GENS = (('the ceiling', 'tools/b764_ceiling.py', ('0826dbaf', '700efb97'), 'data/b764_ceiling.txt', '4565bf58'),
        ('the dispatch tool`s controls', 'tools/b764_controls.py', ('e8a89e2f',), 'data/b764_controls_control.txt', 'b5e2435a'),
        ('the pre-send bank of (S1)-(S3)', 'tools/b764_presend.py', ('456f6547', 'c83f76d4', '508c1bb0', 'be45c496'), 'data/b764_presend_s123.txt', '80f208b3'),
        ('the pre-send bank of KEIPER-FACE', 'tools/b764_presend.py', ('456f6547', 'c83f76d4', '508c1bb0', 'be45c496', '49773e96', 'f24bbcb4', '7eeb89d3',
                                                                       'e47fa937', '33ccc430'), 'data/b764_presend_skp.txt', 'bdccf9a1'),
        ('the author`s rulings of (9)', 'tools/b764_rulings.py', ('922ecaa9',), 'data/b764_author_rulings.txt', '2afcea71'),
        ('the IMP2-TAU reading of (8)', 'tools/b764_imp2tau.py', ('095e5198',), 'data/b764_imp2tau.txt', '5fa0c996'),
        ('the recut inputs of (10)', 'tools/b764_recut.py', ('3c15f127', '07a56968'), 'data/b764_recut_inputs.txt', '9779a81f'),
        ('the outcomes of (6)-(8)', 'tools/b764_outcomes.py', ('8d7b34d8', 'dbd562bb'), 'data/b764_outcomes.txt', '899577a5'),
        ('the ledgers of (9)', 'tools/b764_rulings.py', ('922ecaa9',), 'data/b764_ledgers.txt', '79c05bf2'))
GENS_B762 = ()   # ### b762's five stand in git at tools/b762_worklist.py
GENS_B760 = ()   # ### b760's nine stand in git at tools/b760_worklist.py
GENS_B759 = ()   # ### b759's thirteen stand in git at tools/b759_worklist.py
GENS_B758 = ()   # ### b758's ten stand in git at tools/b758_worklist.py
PASSED_BANK = None   # ### (carried name) no passed writes this act
# ### b761: two banks of the sitting tool rode in a commit with a later state of their tool, each written by the tool as last committed before
# ### the write (the tool committed before each run, (N2)): (name, tool, bank, the commit carrying both, the bank's commit as it stands at HEAD)
GENS_WITH_BANK = ()   # ### b762: none -- each bank of the act rode in a commit of its own, after its tool's ((N2))
# ### b758, Component 5: the act's relay commits after step zero in their order (key, commit), and PLACE-papers' in theirs, each read by the act
# ### module's N2 arms (the order by time and by ancestry) and the entry's order paragraph (CHAIN_WORDS); later commits appended as made; the
# ### lock gate and the handoff page appended by _chain where made
# ### b759, before the lock: the act's relay commits after step zero's banks (3c135c69), every one, in their order, read from git (scratch
# ### files759.py, read-only, 21:5xZ) and from data/b759_steps.json (the step-rows commit 9207bcb4 writes no row of its own); later commits
# ### appended as made
# ### b760, Component 6: the act's relay commits after step zero's banks (45919664), every one, in their order, read from git and from
# ### data/b760_steps.json (scratch steps760.py, read-only, 11:0xZ: 34 rows, each commit with its files); later commits appended as made
# ### b761, Component 6: the act's relay commits after step zero's banks (bdacc192), every one, in their order, read from git and from
# ### data/b761_steps.json (scratch steps761.py, read-only, 23:4xZ: 31 rows, each commit with its files); later commits appended as made
# ### b762, Component 6: the act's relay commits after step zero's banks (18b2afda), every one, in their order, read from git and from
# ### data/b762_steps.json (scratch files762.py, read-only, 11:2xZ: 20 rows, each commit with its files); later commits appended as made
# ### b763, Component 6: the act's relay commits after step zero's banks (f835993a), every one, in their order, read from git and from
# ### data/b763_steps.json (scratch files763.py, read-only, 04:5xZ: 57 rows, each commit with its files, the kernel's six steps apart);
# ### later commits appended as made
CHAIN = (('ceiling_gen', '0826dbaf'), ('ceiling_fix', '700efb97'), ('c1', '17b27a8c'), ('corr', '618a8486'),
         ('standing', 'd34f7323'), ('standing_bank', 'ace66e00'), ('controls_gen', 'e8a89e2f'), ('controls_bank', 'b5e2435a'),
         ('presend_gen', '456f6547'), ('send1', '33ec5111'), ('presend_fix1', 'c83f76d4'), ('presend_fix2', '508c1bb0'), ('read1', 'be45c496'),
         ('presend_s45', '80f208b3'), ('presend_s7', '49773e96'), ('presend_sf', 'f24bbcb4'), ('word', '7eeb89d3'), ('rulings_gen', '922ecaa9'),
         ('wl_squares', '423bd81f'), ('send3', '23471e6e'), ('presend_s24', 'e47fa937'), ('events_51', 'c7daa2aa'), ('outcomes_gen', '8d7b34d8'),
         ('send4', 'f260c122'), ('outcomes_c2', '3ada29d6'), ('ceiling_c2', 'ce33d56d'), ('presend_s7_bank', '08cb68fd'), ('send5', '8a3a903a'),
         ('reproduce', '9c9effb3'), ('module1', 'b9ed79b5'), ('events_59', '21905870'), ('module2', 'e0c98dea'), ('events_60', '38b107ea'),
         ('module3', 'e9cbce4f'), ('events_61', '8d72486a'), ('outcomes_c3', '4565bf58'), ('send6', '50a7a65b'), ('imp2_gen', '095e5198'),
         ('imp2', '5fa0c996'), ('events_65', '2c9ab50c'), ('presend_skp', '33ccc430'), ('presend_skp_bank', 'bdccf9a1'), ('send7', '904c3324'),
         ('rulings', '2afcea71'), ('close_carry', 'dbd562bb'), ('graders', '0729658c'), ('recut_gen', '3c15f127'), ('recut_bank0', '1d8b80a2'),
         ('recut_fix', '07a56968'), ('recut', '9779a81f'), ('events_72', 'dc72e300'), ('events_73', '84162179'), ('landing', 'ac83de9d'),
         ('events_75', 'd6303b7e'), ('outcomes8', '899577a5'), ('ledgers', '79c05bf2'))
CHAIN_B762 = ()   # ### b762's thirteen keys stand in git at tools/b762_worklist.py
CHAIN_B761 = ()   # ### b761's twenty-one keys stand in git at tools/b761_worklist.py
CHAIN_B760 = ()   # ### b760's twenty-five keys stand in git at tools/b760_worklist.py
CHAIN_B759 = ()   # ### b759's sixty-odd keys stand in git at tools/b759_worklist.py
# ### PLACE-papers' commits of the act in their order: the corrigendum (FINDINGS); the page and [G1], [G2] (the new file and REGISTRY); the
# ### lines of (7), (8) and [O6] (OPEN_TRAILS)
# ### b763: the corrigendum with [I1] (FINDINGS); the canon's section XXV and the lines of (9) under one dated head, with the build lines
# ### of (6) and (7) (THE_METHOD_CANON.md and OPEN_TRAILS.md), appended as made
PP_CHAIN = (('c1pp', '6034501c'), ('ledgerspp', '387713dd'))
# ### the order by time, relay and PLACE-papers together: each PLACE-papers key after the relay commit whose tool cut it
# ### b763: the ledgers of (9) written to PLACE-papers (387713dd, 05:50:18Z) after the outcomes of (8) (899577a5, 05:49:18Z) and before the
# ### relay's ledgers banks (79c05bf2, 05:51:30Z), as b762's pp_rulings stood before its ledger_banks
_I_LEDGERS = tuple(k_ for k_, _h in CHAIN).index('ledgers')
TIME_ORDER = (('actcur', 'stepzero') + tuple(k_ for k_, _h in CHAIN[:3]) + ('c1pp',) + tuple(k_ for k_, _h in CHAIN[3:_I_LEDGERS]) + ('ledgerspp',)
              + tuple(k_ for k_, _h in CHAIN[_I_LEDGERS:]))
CHAIN_WORDS.update({'ceiling_gen': 'the ceiling tool', 'ceiling_fix': 'its control (6) re-planted', 'c1': 'the c1 route', 'c1pp': 'the corrigendum with [I1]',
                    'corr': 'the corrigendum banks', 'standing': 'tools/standing/ v1.37.2, the route of (5)', 'standing_bank': 'its controls bank',
                    'controls_gen': 'the dispatch tool', 'controls_bank': 'its controls bank', 'presend_gen': 'the pre-send tool',
                    'send1': 'dispatch 1 sent', 'presend_fix1': 'the pre-send tool`s first mend', 'presend_fix2': 'its second', 'read1': 'dispatch 1 read',
                    'presend_s45': 'the pre-send banks of (S4), (S5) and (S1)-(S3) again', 'presend_s7': 'the pre-send tool takes (7)`s statement',
                    'presend_sf': 'the pre-send tool takes the statement file', 'word': 'the author`s word on the statement file',
                    'rulings_gen': 'the rulings tool', 'wl_squares': 'the (W) row of SQUARES-AT-24', 'send3': 'the statement file`s pre-send bank',
                    'presend_s24': 'the pre-send tool takes SQUARES-AT-24', 'events_51': 'events (51)', 'outcomes_gen': 'the outcomes tool',
                    'send4': 'dispatch 3 read and dispatch 4 sent', 'outcomes_c2': 'the outcomes of (6), main at v0.42', 'ceiling_c2': 'the ceiling after Component 2',
                    'presend_s7_bank': '(7)`s pre-send bank', 'send5': 'dispatch 5 sent', 'reproduce': 'the reproduce run',
                    'module1': 'the act module`s first pass', 'events_59': 'events (59)', 'module2': 'its second', 'events_60': 'events (60)',
                    'module3': 'its third', 'events_61': 'events (61)', 'outcomes_c3': 'the outcomes of (7) and the ceiling after Component 3',
                    'send6': 'dispatch 6 sent', 'imp2_gen': 'the IMP2-TAU tool', 'imp2': 'its bank', 'events_65': 'events (65)',
                    'presend_skp': 'the pre-send tool takes KEIPER-FACE', 'presend_skp_bank': 'its pre-send bank', 'send7': 'dispatch 7 sent',
                    'rulings': 'the author`s rulings banked', 'close_carry': 'the close`s tools carried',
                    'graders': 'the act module`s graders for b764 and the scan`s byline repair (defect (k))', 'recut_gen': 'the recut inputs tool of (10)',
                    'recut_bank0': 'its first bank', 'recut_fix': 'its foot in the verdict form (defect (l))', 'recut': 'its bank again',
                    'events_72': 'events (72) with defect (l)', 'events_73': 'events (73)',
                    'landing': 'dispatch 6 read, main at v0.43', 'events_75': 'events (75)', 'outcomes8': 'dispatch 7 read and the outcomes of (8)',
                    'ledgerspp': 'the canon`s section XXV and the lines of (9) with the build lines', 'ledgers': 'the ledgers and the roster banked'})
# ### the standing versions of the act, each (version, its commit, its controls bank, its cases): none at b761 ((R371)(11), tools/standing/
# ### tree-equal to b760's close, VERSION v1.37.1); b760's four kept under their own names for the carried readers
STANDING_BANKS = (('v1.37.2', 'd34f7323', 'data/b764_standing_v1372.txt', 10),)   # ### b763 (R373)(5): its controls 10 of 10, banked after the commit (19:54:12Z)
STANDING_BANKS_B760 = (('v1.36.8', '34390a25', 'data/b763_standing_v1368.txt', 9), ('v1.36.9', '1e9493e5', 'data/b763_standing_v1369.txt', 9),
                       ('v1.37.0', 'a8f8403a', 'data/b763_standing_v1370.txt', 10), ('v1.37.1', '6bc5d706', 'data/b763_standing_v1371.txt', 9))   # ### b760's (R370)(5)(i)-(iv), read not re-made
STANDING_BANKS_B759 = (('v1.36.3', '983ca5b1', 'data/b763_standing_v1363.txt', 10), ('v1.36.4', '4622b017', 'data/b763_standing_v1364.txt', 6),
                       ('v1.36.5', '34452b1a', 'data/b763_standing_v1365.txt', 5), ('v1.36.6', '8fc653fc', 'data/b763_standing_v1366.txt', 5),
                       ('v1.36.7', 'cd45450e', 'data/b763_standing_v1367.txt', 9))   # ### b759's five, read not re-made, under their own names (the carry had shifted them)
STANDING_BANKS_B758 = (('v1.35.6', 'ac6a0a77', 'data/b758_standing_v1356.txt', 11), ('v1.35.7', '248cacb8', 'data/b758_standing_v1357.txt', 16),
                       ('v1.35.8', 'ed0d3f33', 'data/b758_standing_v1358.txt', 7), ('v1.35.9', 'da79951c', 'data/b758_standing_v1359.txt', 8),
                       ('v1.36.0', 'fd45f4c5', 'data/b758_standing_v1360.txt', 10), ('v1.36.1', '9bc8cfeb', 'data/b758_standing_v1361.txt', 11),
                       ('v1.36.2', '4db55035', 'data/b758_standing_v1362.txt', 6))   # ### b758's seven, read not re-made, under their own names
# ### the kernel commits of the act, read by N5 and G-OFFSET-POST-HOC: (key, kernel, commit, the branch it stands on at the close).
# ### ### b764, Component 3 (the Edit tool, defect (f)): b764's one, by the one-call tool on push-b764-runner made at main 819e4a83 ((R374)(7));
# ### its branch set to main where the trial's success moves main to it. b763's six stand below as KERNEL_COMMITS_B763 under the branch
# ### names the remote holds (push-b763-arith, push-b763-keiper), which the carry had shifted to push-b764-*.
KERNEL_COMMITS = (('runner', 'SIDE-explicit-formula', '38a57e02', 'push-b764-runner'),)   # ### (R374)(7)'s workflow change alone (21:52:37Z, step 56), pushed alone and read back (21:53:1xZ)
KERNEL_COMMITS_B763 = (('form13', 'SIDE-explicit-formula', 'ec82fed0', 'main'),       # ### (R373)(6) (S1)-(S3) and [P1]'s six names (20:32:07Z, step 16), on main at v0.42
                       ('form45', 'SIDE-explicit-formula', '0f849552', 'main'),       # ### (S3)'s import repaired, (S4) and (S5) (21:52:14Z, step 21), on main at v0.42
                       ('statement', 'SIDE-explicit-formula', '4964e957', 'main'),    # ### the statement file by the author's word (23:51:12Z, step 28), main at v0.42 (02:22:05Z)
                       ('arith', 'SIDE-explicit-formula', 'ec14e9d9', 'push-b763-arith'),   # ### (R373)(7)'s statement, no proof (02:28:20Z, step 36), on its branch
                       ('squares', 'SIDE-explicit-formula', '819e4a83', 'main'),   # ### (R373)(8) W-ORD-SQUARES-AT-24 (03:48:55Z, step 47), on push-b763-squares; main moved to it at v0.43 after run 44670834879's success (05:34Z)
                       ('keiper', 'SIDE-explicit-formula', 'a59632eb', 'push-b763-keiper'))     # ### (R373)(8) W-ORD-KEIPER-FACE, a first file (04:23:03Z, step 53), on its branch made at main 4964e957; the order not built in full, so main does not move to it
KERNEL_COMMITS_B762 = ()   # ### b762 made none ((R372)(12))
KERNEL_COMMITS_B759 = (('prints', 'SIDE-explicit-formula', 'ddb3efb9', 'main'),   # ### (R369)(5) commit one: the four print lines, on main at v0.41
                       ('weil', 'SIDE-explicit-formula', 'a3aad4cc', 'main'))     # ### (R369)(5) commit two: zq_weil_positivity_fails, main at v0.41
KERNEL_COMMITS_B758 = (('rename', 'SIDE-explicit-formula', 'd1afb4fc', 'main'), ('merge', 'SIDE-explicit-formula', '630cba16', 'main'))   # ### b758's two, on main at v0.39 and v0.40
WEIL_BRANCH = ('push-b764-runner', '38a57e02074a22eebbf33c6ff9ce5c7e58335d4a')   # ### b764 (R374)(7): the act's one kernel branch, made at main 819e4a83 by the one-call tool (21:50:3xZ), its one commit 38a57e02 (step 56), pushed alone by the gated push's branch mode, scratch, and read back (data/b764_SIDE-explicit-formula_push-b764-runner_push_out.txt); kept for the next act's step zero ((R374)(4))
WEIL_TAG = None   # ### b764 (R374)(7), (13), N5: no tag cut at this act, the trial's success moving main with no tag; every reader of WEIL_TAG is rewritten for b764 at Component 5
RUNNER_COMMIT = '38a57e02074a22eebbf33c6ff9ce5c7e58335d4a'   # ### b764 (R374)(7): the commit whose workflow bytes the arm that reads the workflow's file takes, by this clause's commit and no other
WEIL_BRANCH_B763 = ('push-b763-form', '4964e95758a7b1bc8c49d0972ebb18877d4f945f')   # ### b763's (R373)(6): made at main a3aad4cc (20:14:10Z); commits ec82fed0, 0f849552, 4964e957; main moved from it (02:22:05Z); kept by (R374)(4)
WEIL_TAG_B763 = ('v0.42', '001e94ff09537595adfe0b59acddfb45635a0e86', '4964e95758a7b1bc8c49d0972ebb18877d4f945f')   # ### b763's (R373)(6): name, tag object, peel read back at the remote (data/b763_SIDE-explicit-formula_push-b763-form_push_out.txt, 02:22:05Z); peels as before ((R374) N5)
WEIL_BRANCH_B759 = ('push-b759-weil', 'a3aad4cceb41705fe9929c9b5600976eaf7434b5')   # ### b759's, kept
WEIL_TAG_B759 = ('v0.41', '390506fc8e1128976f68ca63219ac91d02ffa532', 'a3aad4cceb41705fe9929c9b5600976eaf7434b5')   # ### b759's, unmoved by b763 (N5)
ORDER_BRANCHES = ()   # ### b764 (R374)(8): no order of (8) writes a kernel (each is a relay or PLACE-papers build), so no order branch is made
ORDER_TAGS = ()   # ### b764 (R374)(7), (13): no tag cut
ORDER_BRANCHES_B763 = (('push-b763-squares', '819e4a832700038d103b4efc1e0ee0f1343f7c6e'),   # ### b763's (R373)(8), under the names the remote holds: SQUARES-AT-24 made at main 4964e957 (03:48:11Z), pushed alone and read back (03:52:35Z); kept by (R374)(4)
                       ('push-b763-keiper', 'a59632eb3e8f4164c491ced038130b583f4893df'))   # ### KEIPER-FACE made at main 4964e957 (04:22:20Z), pushed alone and read back (04:27:35Z); kept by (R374)(4)
ORDER_TAGS_B763 = (('v0.43', 'bcd4d4818520fc7a477c98e2c79548b80295725f', '819e4a832700038d103b4efc1e0ee0f1343f7c6e'),)   # ### b763's (R373)(8): W-ORD-SQUARES-AT-24 at main's read-back (data/b763_SIDE-explicit-formula_push-b763-squares_push_out.txt, 05:34Z); peels as before ((R374) N5)
PRESEND_SENDS = ('s123', 's4', 's5', 'sf', 's7', 's24', 'skp')   # ### each send's pre-send bank data/b763_presend_<send>.txt, read by the record's figures; an (8) send added as it is made
ARITH_BRANCH = None   # ### b764 (R374)(9)(c): no statement and no line of a proof sent, so no arith branch; every reader of ARITH_BRANCH is rewritten for b764 at Component 5
ARITH_BRANCH_B763 = ('push-b763-arith', 'ec14e9d937fbeb943a0f8d3103803570ee810f09')   # ### b763's (R373)(7): made at main 4964e957 (02:26:08Z), the statement alone; pushed alone and read back (02:32:35Z); main not moved from it; kept by (R374)(4)
KERNEL_COMMITS_B757 = ()   # ### b757's sixteen stand in git at tools/b757_worklist.py
M24_DIR = 'D:/SIDE-dirichlet-mod-24'
M24_BASE = '597b0869'                 # ### SIDE-dirichlet-mod-24's main entering the act, its one commit
M24_MAIN = 'e5ebdd15'                 # ### b758: its remote main, unmoved; its local main fast-forwarded to it by (6)(i)'s route (01:59:39Z, events (38))
M24_TAG = ('v0.2.0', 'e5c84316', 'e5ebdd15')   # ### (R367)(6): name, tag object, peel read back at the remote (data/b757_SIDE-dirichlet-mod-24_push-b757-mod24_push_out.txt)
# ### b758 step zero: the carry shifted b757's two kernel branch names to push-b758-* here and in KERNEL_COMMITS above; set back to the names
# ### the remote holds (ls-remote 23:4xZ: push-b757-coeff 596d1c9e, push-b757-join 6568e9c7). KERNEL_COMMITS stays b757's until Components 2-3 write b758's.
# ### b759, before the lock: the four below are b758's history, their names set back to the ones the remote held (the carry had shifted each
# ### by one act); each removed at its remote by (R369)(3) through (4)(i)'s route (data/b759_events.txt (24))
COEFF_BRANCH = ('push-b757-coeff', '596d1c9e')   # ### b757's T0, T1 and the wide direction; (R368)(5) merged its tip --no-ff into push-b758-coeff
JOIN_BRANCH = ('push-b757-join', '6568e9c7')     # ### b757's join; (R368)(4) made push-b758-land at its tip
LAND_BRANCH = ('push-b758-land', 'd1afb4fc2b34f5e62951947208461995d891c80c')   # ### (R368)(4): made at JOIN_BRANCH's tip; its one commit, the rename; main at v0.39
COEFF_LAND_BRANCH = ('push-b758-coeff', '630cba16e228a018f9dd986196142fc6feb704ec')   # ### (R368)(5): the merge of 596d1c9e; main at v0.40, b759's entering main
C1_DEFECTS = ()   # ### the defects bank's commits
C2_AMEND_RELAY = None        # ### no amendment this act
C2_AMEND_PP = C1_TAG_PP      # ### (carried name)
C2_PP = ()               # ### no PLACE-papers write in Component 2 ((R364)(3)-(5): banks of this act alone)
PRICE_LINE = 17400
DOORS_COMMIT = None
MECH_COMMIT = None
FRONTDOORS_COMMIT = None
COUNT_BANK = None
PRINT_COMMIT = None        # ### (carried name) the commit carrying the act's section bank (C2_RELAY)
PLAN_MD5 = 'ef777cc24752911990d56d2214fe38b6'   # ### data/b753_zetabox_plan.txt's md5, printed at step zero (PLAN_MD5S), unedited
C2_AMEND = ()
SITTING_KERNEL = None # ### no kernel written this act: [B1] and [B3], the two README items, carried by the author's answer (data/b754_author_answers.txt :88)
# ### b755, Component 6: no sitting, no agenda, no puts beyond the two answered at step zero and Component 1, no reads of b754's kind, no line
# ### bank ((R365) orders none of them); b754's names kept empty for the carried readers. The author's two answers stand as the amendment
# ### rows (data/b755_amendments.json), each put by the composer (data/b755_put_1.json, data/b755_put_2.json)
AGENDA_COMMIT = None
C3_AGENDA = ()
C3_PUTS = (('defect (c)', 'data/b764_put_1.json', '77ae83fe'), ('N5`s folder clause', 'data/b764_put_2.json', 'cb14bae1'))   # ### (subject, the put bank, the commit carrying it)
C3_SITTING_TOOL = ()
C3_SITTING_BANK = ()
SITTING_COMMIT = None
SITTING_BANK = None
ITEM_PP = ()   # ### no passed item's PLACE-papers write this act
SITTING_PP = ()
SITTING_GH = ()
SITTING_SETTINGS = ()
SITTING_ITEMS = None          # ### none at b764: (R374) holds no sitting (carried name)
SITTING_STATES = {}
HANDOFF_COMMIT = '26be95bb'   # ### b763: HANDOFF.md written once by tools/standing/handoff.py before the gate ((R373)(13)'s (W) list names it), 154 lines (step 78, 08:17:27Z)
HANDOFF_COMMIT_B762 = 'f702adac'   # ### b762's, 154 lines (step 28, 13:55:52Z)
HANDOFF_COMMIT_B761 = 'd2adb845'   # ### b761's, 154 lines (step 38, 02:34:06Z)
HANDOFF_COMMIT_B760 = '8d99ac80'   # ### (R370)(5): b760's, built and written by tools/standing/handoff.py at v1.36.9, 154 lines (step 14, 09:18:36Z)
# ### b760, Component 6: PLACE-papers' writes of (7), (9), (10) and (11), each (item, the file, the PLACE-papers commit), read by the act
# ### module's N3 arms against the banks' sha256 (data/b760_ledgers.json, data/b760_epstein_keys.txt) and the edition's (events (61))
# ### b761, Component 6: PLACE-papers' writes before the record, each (item, the file, the PLACE-papers commit), read by the act module's N3
# ### arms against the banks' sha256 (data/b761_ledgers.json's files; data/b761_registry_cells.json's file_sha_before and file_sha_after)
# ### b762, Component 6: PLACE-papers' writes before the record, each (item, the file, the PLACE-papers commit), read by the act module's N3
# ### arms against the banks' sha256 (data/b762_page.json's page and REGISTRY digests; data/b762_ledgers.json's file)
# ### b763, Component 6: (1)'s corrigendum with [I1]; the ledgers of (9) appended when written
PP_WRITES = (('corr', 'FINDINGS.md', '6034501c'),                                                     # ### (R373)(1): the corrigendum with [I1] (step 9)
             ('trails', 'OPEN_TRAILS.md', '387713dd'),                                                # ### (R373)(9): the lines of (9) with the build lines of (6), (7) and (8) under one dated head (step 68)
             ('canon', 'phase1.5/method/THE_METHOD_CANON.md', '387713dd'))                           # ### (R373)(9): [C1] as section XXV (step 68)
PP_WRITES_B762 = ()   # ### b762's four stand in git at tools/b762_worklist.py
PP_WRITES_B761 = ()   # ### b761's five stand in git at tools/b761_worklist.py
PP_WRITES_B760 = ()   # ### b760's six stand in git at tools/b760_worklist.py
LEDGERS_GEN = '92ef6b8e'     # ### tools/b760_ledgers.py committed before it wrote, after its two dries (step 30)
EDITION_GEN = 'beb7b07b'     # ### tools/b760_edition.py as it stood when it wrote the edition (step 24); the cut's head set at 6b639c83 after
C3_NOTES_GEN = None          # ### (carried name) b759's notes tool; b760's notes of (11) written by the ledger tool (LEDGERS_GEN)
C3_NOTES_PP = ()             # ### (carried name) b759's three notes; b760's in PP_WRITES
C3_NOTES_WRITTEN = 0
C3_DOC_PP = ()               # ### (carried name) b759's document; b760's edition in PP_WRITES
C3_CORPUS_PP = ()            # ### (carried name) b759's nine documents of (9); b760 re-cuts none
C3_ERRATA_PP = ()            # ### (carried name) b759's two; b760's in PP_WRITES
# ### Component 4 ((R366)(5)): the put and the work its answers order, each value read from the step rows (data/b756_steps.json)
C4_READ = ('tools/b764_orders.py', '5b3d5a60', ('data/b764_orders_read.txt', 'data/b764_instruments_draft.txt'), 'f56557dd')   # ### the orders read and the two drafts
C4_PUT = ('data/b764_put_1.json', '0803754c')   # ### the one put, three questions, and the answers pair by its route, all three passed as recommended (step 22)
C4_PASSED_GEN = '9aa5fe8c'   # ### tools/b756_passed.py committed before its run, with events (21) (step 23)
C4_PASSED_PP = (('cp', 'OPEN_TRAILS.md', 'e50a394b'), ('instruments', 'phase1.5/method/INSTRUMENTS.md', '3b45826d'))   # ### steps 24, 25, each confirmed at HEAD (data/b756_passed.json)
C4_HERE = ('v1.34.8', '5b7aa91e', 'data/b764_standing_v1348.txt')   # ### W-ORD-LABEL-READER's predicate and control, controls 11 of 11 (step 26)
C4_MOVES = ('tools/b764_moves.py', '208eee6a', 'data/b764_orders_moves.txt', 'a26f30b9')   # ### the twelve status lines for this act's trail, controls 12 of 12 (steps 27, 28)
C4_CEILING = ('tools/b764_ceiling.py', 'a26f30b9', 'data/b764_ceiling_c4.txt')   # ### the ceiling after Component 4: 17.53 h against 24 h, nothing carried
C4_ORDERS = (1, 1, 5, 5)   # ### the orders: done, here, with the build, later (data/b756_orders_read.txt :87; data/b756_orders_moves.txt)
C4_CP = 'passed'           # ### CP-6 and CP-7 (data/b756_author_answers.txt :18; OPEN_TRAILS at e50a394b)
C4_LINE_GEN = None   # ### b755: no line bank; the entry's INTEGRATION line is (R365)'s, composed from the banks by the record module
C4_LINE = None       # ### Component 5: the act's INTEGRATION line by (R374)(11)'s rule, bare as the entry's last line
C4_ANSWERS = None    # ### no reader of this name at b755; the answers pair of the two puts written by its route and committed at relay 3a5f0d0f (step 31), the root's question appended to it
ANSWERS_COMMITS = ()
C2_READS = ()        # ### no read of b754's kind this act
C2_CEILING = None    # ### one ceiling reading this act, after Component 3 (C1_CEILING)
ZENODO_BANK = None   # ### no Zenodo call this act ((R364)(6))
ROUTES_BANK = 'data/b747_zenodo_routes.txt'     # ### b747's routes bank, read not written
INTEGRATION_DRAFT_MD5 = '9e760351971eab06b176176dc02643ab'   # ### data/b746_integration_draft.txt carried unchanged (its md5, last committed c4d044f3)
C3_ORDER_PP = None   # ### (carried name) NOT READ for the entered/carried word from v1.27.0 ((R364)(3)(i)): the composer reads the order commit's presence in the git log
C1_ORDER_PP = None         # ### no order entered this act
SITTING_COMMITS = ()
C3_PP = None         # ### (carried name) no INTEGRATION line written apart from the entry this act
C4_LV = None
C4_RUN = None
C4_PP = None
C4_RELAY = C4_LIST       # ### b755: Component 4's last commit, the list and the two verdicts
C5_RELAY = '562707bb'    # ### b755: Component 5's bank, data/b755_census_from_primes.txt (step 25)
REG_COMMIT = C4_RULE_ZEROS   # ### b755: H-ZEROS-FROM-PRIMES committed alone (data/b755_registrations.txt (2))
ZEROS_REG_COMMIT = REG_COMMIT
ORDERS = (142, 60, 42, 12, 28)          # ### b753's (R363)(4) triage, carried as read (data/b729_orders_triage.txt): DONE, NOT MET, MET, AUTHOR'S WORD
TRIAGE = 'data/b729_orders_triage.txt'
LV_SCRATCH_BRANCH = 'scratch-b724'      # ### b724's scratch branch of SIDE-lv-conservation, kept ((R364)(8))
LV_RUNS = (('SIDE-lv-conservation', 40964150574),)   # ### b753's one dispatch, read by its id (carried, not re-run)
LV_ROWS = 'data/b764_lv_rows.json'
CHALLENGE_BRANCH = 'challenge-b720-h2-sign-iff-rh'   # ### b720's, on SIDE-explicit-formula, standing, not merged, no tag
CHALLENGE_TIP = '3391647518cd37316a448b5013afb62a198fa6c6'
CHALLENGE_RUN = 40651875792
PIN_RUNS = (('SIDE-grh-transfer', 40652622018), ('SIDE-interfaces', 40652657325), ('SIDE-kernel', 40652692787),
            ('SIDE-lv-conservation', 40652727943), ('SIDE-simplicity', 40652762827), ('SIDE-trivium', 40652790458))   # ### b720's, read not re-run
PIN_BRANCH = 'pin-b718-de5ce8a9'   # ### b718's pin branches, left as banked ((R364)(8))
PIN_EXCLUDED = ('SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve', 'SIDE-cosmo')
PIN_HELD = ('SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium')
PIN_BUILDS = ('SIDE-simplicity',)
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PIN_TO_NEXT = ()
MAX_DISPATCHES = 3         # ### (R374) N1: "the dispatches are the three of (7) and no other" -- the reference with the restore off, the run that saves, the run that restores; 0 where (7) is carried by the ceiling
MAX_DISPATCHES_B763 = 18   # ### b763's, (R373) N1: the counts within its price table's upper figures (data/b763_price.txt)
MAX_DISPATCHES_B762 = 0    # ### b762's, (R372) N1: "no dispatch is sent"
MAX_DISPATCHES_M24 = 0     # ### (R373)(5): no kernel beyond SIDE-explicit-formula is written; no dispatch in SIDE-dirichlet-mod-24
MAX_DISPATCHES_B759 = (3, 0)   # ### b759's caps, (R369)(5), (11)
MAX_DISPATCHES_B758 = (4, 0)   # ### b758's caps, (R368)(10)
MAX_DISPATCHES_B757 = (14, 4)   # ### b757's caps, (R367)(10)
MAX_DISPATCHES_B756 = 0    # ### b756's: no runner dispatch
MAX_C2, MAX_KEIPER = 0, 0
EF_DIR = 'D:/SIDE-explicit-formula'
EF_BASE = '819e4a832700038d103b4efc1e0ee0f1343f7c6e'   # ### b764 (Component 3, the Edit tool, defect (f)'s class): SIDE-explicit-formula's main entering the act, b763's v0.43 (the carry had kept b763's entering pin under b763's comment)
EF_BASE_B763 = 'a3aad4cceb41705fe9929c9b5600976eaf7434b5'   # ### b763's entering main, b759's commit two at v0.41
EF_BASE_B759 = '630cba16e228a018f9dd986196142fc6feb704ec'   # ### b759's entering main, b758's merge at v0.40
EF_BASE_B758 = '8fbab45d8a966dca53d42448e33927d885fd4ea3'   # ### b758's entering main (b743's [A4], README alone)
EF_MAIN_AFTER = EF_MAIN   # ### b759: moved by (5) alone, after its run's success ((R369)(5))
ZQ_BRANCH = 'zq-b730'
ZQ_ENTERING = '1e6588703732435b34d840bbbb840225932c9b6b'   # ### b754: zq-b730 entering at b753's tip (SPZ3), unmoved this act ((R364)(8))
ZQ_ENTERING_B745 = '14ca572560f50378a6e4715e35cba0351e5f105d'   # ### b753's entering tip, the tag's commit
ZQ_TAG = ('v0.38', '21c6edafa047635112c9ccd4fad14c56d5a2fa4f', '14ca572560f50378a6e4715e35cba0351e5f105d')   # ### (R364)(3): name, tag object, peel read back
#   ### at the remote 2026-11-07T15:09:55Z (data/b754_SIDE-explicit-formula_v0.38_push_out.txt); the series v0.1-v0.37 read by ls-remote --tags, the next v0.38
ZQ_TIP = '1e6588703732435b34d840bbbb840225932c9b6b'   # ### b754: unmoved, b753's last Lean commit on zq-b730 (W-ORD-ZETA-BOX BUILT, SPZ3); no Lean commit this act
ZQ_FIRST = 'eb097190ffab325cd7ee8da5f9879210cfcc7eb1'   # ### the first Lean commit of this act (P1-P5)
ZQ_COMMITS = ()   # ### b754: none
ZQ_COMMITS_B745 = ('eb097190ffab325cd7ee8da5f9879210cfcc7eb1', '3639d984d76f724cd4406b5e166d75d7b15fe13b', 'ae959dedcaa19c63fdbac71b871989567aca91f5',
              'ef86297462f6b90218ee4ee665b1d7f4a3fdfa0f', '32bad89a81f6051f7c4e4dd56d800d9861a0922f', '1e6588703732435b34d840bbbb840225932c9b6b')   # ### this act's: P1-P5 ; R1 (the print list's order) ; Z1-Z3 ; R2 + Instr ; Signs t=16 ; Signs 16+12 + Box
ZQ_COMMITS_B742 = ('280b28b3935854f8c71e37480ee9b88dfeb60922', '11bb0125fa08eccc78f6a1a6d415201438973f45', '5d3136a39ea9b671b60118e1424e645f89956ea7',
                   '4c04916c8541f1ee2267059a8fa0396364f1eb5c', 'c2d4f29ce84d321814b223a7e275e0653161b4d4', '14ca572560f50378a6e4715e35cba0351e5f105d')   # ### b753's six, read by the discharge
ZQ_COMMITS_B741 = ('f2de6efb669405b5e6ed270e4a82e3bc6effa500', 'de4810da5d3cfc524002630959b32e4ebc30ce66', '47f5afb3f1b40a8525ac45eba0f1bf04fe2ed155',
              '42cb968b8ce35bb024bca8995a743a809c19409e', 'c9ad907454b785b75ad2142e1dcdf9a4797cfd0c', '3329eaa106cc24891ed55374afcd4ca4f7fe33d8')   # ### T ; G1+G2 ; repairs+G4 ; G3+G5 ; cast repair ; generator repair
ZQ_COMMITS_B740 = ('8c6ec8d12d97bece1de8dab10511add9d97382d0', '6b068a0db2ff1451e9da7bff82fe8fd66a8dad38', 'ba318a0b67fd95164623e4fdf109eb5d042697fa')   # ### b753's S5c ; S5d with S5c's fix ; S5d's fix
ZQ_SP1 = None
ZQ_SP3 = '3329eaa106cc24891ed55374afcd4ca4f7fe33d8'   # ### b753: SP3 REACHED here (dispatch 6, run 41940815524)
ZQ_SP4 = '14ca572560f50378a6e4715e35cba0351e5f105d'   # ### b754: SP4 REACHED here (dispatch 7, run 42068096322)
ZQ_MODULES = ('Xi', 'Landau', 'Heights', 'Contour', 'ZeroSum', 'FullLine', 'Lines', 'Main')   # ### the build's eight, under Schema/ZQ/EF
ZQ_OFFZERO_MODULES = ('Box', 'Diff', 'MinModulus', 'Carrier', 'Main', 'Split', 'Tail', 'IncGamma', 'Elem', 'Time', 'Series', 'Sums', 'GammaVal', 'Shells', 'Centre',
                      'Interp', 'Frame', 'Strip', 'Amplify', 'NodeBase', 'Omega', 'Nodes0', 'Nodes1', 'Nodes2', 'Nodes3', 'NodesF', 'FrontierData',
                      'Frontier', 'SP4')   # ### under Schema/ZQ/OffZero; b754 adds S6's fourteen
ZQ_FILES = ()   # ### b754: none
ZQ_FILES_B745 = ('SIDEExplicitFormula/Schema/Wide/PositiveControl.lean',) + tuple('SIDEExplicitFormula/Schema/ZetaBox/%s.lean' % m for m in ('Box', 'Instr', 'Line', 'Signs', 'Split', 'Tail')) + ('print_targets.txt',)   # ### zq-b730's diff against its entering tip
ZQ_FILES_B742 = tuple('SIDEExplicitFormula/Schema/ZQ/OffZero/%s.lean' % m for m in ('Amplify', 'Frame', 'Frontier', 'FrontierData', 'Interp', 'NodeBase',
                 'Nodes0', 'Nodes1', 'Nodes2', 'Nodes3', 'NodesF', 'Omega', 'SP4', 'Strip')) + ('print_targets.txt',)   # ### b753's diff against 3329eaa1 at 14ca5725
ZQ_FILES_B741 = ('SIDEExplicitFormula/Schema/ZQ/OffZero/Centre.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/GammaVal.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/Series.lean',
            'SIDEExplicitFormula/Schema/ZQ/OffZero/Shells.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/Sums.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/Time.lean',
            'print_targets.txt')   # ### zq-b730's diff against ba318a0b at 3329eaa1
ZQ_FILES_B740 = ('SIDEExplicitFormula/Schema/ZQ/OffZero/Elem.lean', 'SIDEExplicitFormula/Schema/ZQ/OffZero/IncGamma.lean', 'print_targets.txt')   # ### b753's diff against 602cd401
ZQ_MODULES_B730 = ('Lattice', 'Theta', 'FEPair', 'Continuation')   # ### the names the carried sections read, until each section is set for this act
ZQ_ZEROS_FIRST, ZQ_LOGDERIV_TIP = None, None
ZQ_LOGDERIV_MODULES, ZQ_ZEROS_MODULES = (), ()
MAX_LOGDERIV, MAX_ZEROS = 0, 0
EF_BRANCHES = (('keiper-b725', '01fd33c2d7dc62d4702b075de3dda9253c5c2f87'),   # ### (R364)(4): the gamma_1 bound
               ('c2-b725', '0395f15d3b2906716ccb1f09ca24171d7a921210'),       # ### (R364)(3): the theorem, built whole at this tip
               ('detect-b729', '1023301c89ab16f8d437b2a1f08a824bc95b6b0e'),   # ### b729's (R339)(5): the statement alone, not compiled; kept, unmoved
               (ZQ_BRANCH, ZQ_TIP))                                           # ### (R364)(3)-(4): the fields
EF_BRANCHES_ENTERING = ('01fd33c2d7dc62d4702b075de3dda9253c5c2f87', '0395f15d3b2906716ccb1f09ca24171d7a921210', '1023301c89ab16f8d437b2a1f08a824bc95b6b0e', ZQ_ENTERING)   # ### the four entering the act
EF_RUNS = ()   # ### N1: this act's SIDE-explicit-formula runs, the three of (7) at most, each read by its run id, set as each is read (data/b764_dispatch_rows.json)
EF_RUNS_B763 = (44610575175, 44625270777, 44641876790, 44646848292, 44661759569, 44670834879, 44674735311)   # ### b763's seven, read not re-run (data/b763_dispatch_rows.json): dispatch 1 BREAKS, 2 KERNEL, 3 STOPPED UNDER THE HOLD, 4 KERNEL, 5 KERNEL ((7)'s statement), 6 KERNEL (SQUARES-AT-24), 7 KERNEL (KEIPER-FACE's first file)
EF_RUNS_B762 = ()   # ### b762's: none
EF_RUNS_B759 = (44162171267,)   # ### b759's one, read not re-run
M24_RUNS = ()   # ### N1: no SIDE-dirichlet-mod-24 dispatch this act ((R373)(5): no kernel beyond SIDE-explicit-formula)
EF_RUNS_B758 = (43997787796, 44007490629)   # ### b758's two, read not re-run: (4)'s join at v0.39 = d1afb4fc, (5)'s three results at v0.40 = 630cba16 (data/b758_outcomes.txt)
EF_RUNS_B757 = (43818699881, 43834018078, 43835333285, 43836818700, 43839463729, 43841545568)   # ### b757's six, read not re-run (tools/b757_controls.py): the join KERNEL (the print failed at the import), T0 KERNEL (print stopped at maxErrors), T0 KERNEL (10 names), T1 BREAKS (recursion depth), T1 KERNEL (31 names), the wide direction KERNEL (24 names)
M24_RUNS_B757 = (43835913340, 43836415096)   # ### b757's two SIDE-dirichlet-mod-24 runs, read not re-run: the workflow's control KERNEL (2 names), the module KERNEL (8 names)
EF_RUNS_B745 = (42388001562, 42388609600, 42391254295, 42392017104, 42393018408, 42393914259)   # ### N1: this act's dispatches, each read by its run id ((R364)(4)(c)): KERNEL (print stopped at maxErrors), KERNEL (13 names printed), BREAKS (lp_conj), KERNEL (SPZ1), KERNEL (SPZ2), KERNEL (SPZ3)
EF_RUNS_B742 = (42054839204, 42056405331, 42058361986, 42061332755, 42062848400, 42065597154, 42068096322)   # ### b753's seven, read not re-run; the last the SP4 grade run
EF_RUNS_B741 = (41931918742, 41935365948, 41936644993, 41938300160, 41939524029, 41940815524)   # ### b753's six: KERNEL (timing), BREAKS, KERNEL, BREAKS, BREAKS, KERNEL (SP3)
EF_RUNS_B740 = (41854903335, 41857376723, 41859346843)   # ### b753's three: BREAKS, BREAKS, KERNEL, read not re-run
EF_RUNS_B738 = (41732413170, 41732882564, 41733411736, 41734667160, 41735082430, 41736472780)   # ### b738's first six (of eleven), read not re-run
ZQ_RUN = 41483457057   # ### b737's grade run, the discharge's, read not re-run
EF_RUNS_B731 = (41371666217, 41372597450, 41373409167, 41374121055, 41374814817)   # ### b731's five, read not re-run
DISPATCH_ROWS = 'data/b764_dispatch_rows.json'
ERRATA_ID = 'E-2026-11-18-1'   # ### (R370)(9), (10): the citations' erratum, BLOCK E's first entry (ERRATA :1127)
ERRATA_IDS = ()   # ### b761: no ERRATA entry ((R371)(13)'s (W) list names no ERRATA.md)
ERRATA_IDS_B760 = ('E-2026-11-18-1', 'E-2026-11-18-2')   # ### (R370)(10): b760's BLOCK E's two entries at the file's end (PLACE-papers f47d90f0)
RETIRED_COUNT = 0
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list (the root answer's addition (b))
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b764_') and f.endswith('.py') and f != 'b764_report.py')) + NEW_TOOLS + COMPUTE_TOOLS + REPAIRED_TOOLS
# ### the act's arms over its own banks: set before the lock by the Edit tool -- b753's list, the act shift G-R363-ENTERED to G-R364-ENTERED,
# ### G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0 ((R364)(2)(iv))
ACT_ARMS = ('G-ACT-CURRENT', 'G-ARM-TAGS', 'G-ARMS-RETIRED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED', 'G-CLOSING-DRY-STEP', 'G-COEFFS-LAW',
            'G-CORRIGENDUM-ENTERED', 'G-COUNT-ROUTE-PRICED', 'G-DELETES-ONE-BRANCH', 'G-DERIVATION-GRADED', 'G-DIFFERS-ERRATA', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-GUARD-HELD', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LISTINGS-BEFORE-CLAUSES',
            'G-MEMBRANE-WIRED', 'G-OFFSET-POST-HOC', 'G-POSTROOT-WRITES-NONE', 'G-PREDICTION-FIRST', 'G-R374-ENTERED',
            'G-REGISTRATIONS-FIRST', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED', 'G-SURGERY-CARRIED', 'G-TOUCH-READ',
            'G-WRITELIST-MIRROR-STATE')

# ### b754 writes no kernel ((R364)(5)): no main touched, no branch made on a kernel
SITTING_TIPS = {}
SITTING_BASE = EF_BASE
SITTING_REPOS = tuple(sorted(SITTING_TIPS))
SITTING_BRANCH = None
SITTING_BANK = 'data/b764_sitting.txt'   # ### the record of the sitting, one row per item
KERNEL_BASES = 'data/b764_kernel_bases.json'
