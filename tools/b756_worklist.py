# -*- coding: utf-8 -*-
"""b756_worklist.py -- THE ACT'S DATA, UNDER (R366). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b756: LANE TWO, ACT ONE HUNDRED AND EIGHTY-THREE, THE CLEARING ACT -- b755 AT ITS WEIGHT; ITS RESULTS WRITTEN INTO THE DOCUMENTS
### THEY BEAR ON; THE CONSTELLATION MAP RUN AGAIN AND READ IN REVERSE; THE TWELVE READY ORDERS PLACED; CP-6 AND CP-7 GIVEN THEIR LINES;
### THE TOOL CHANGES CARRIED FROM THE SITTING; NOTHING COMPUTED, NOTHING BUILT.
### No runner dispatch, no Lean file, no lean process on this host (N1); nothing deposits, no Zenodo call (N5).
### Carried by diff from b755_worklist.py (data/b756_carry_worklist.txt); its stage one set at step zero with this act's figures by the
### seat's script (scratch wl756.py, each constant replaced whole by its name); later stages by the Edit tool.
### (R366) was delivered in session 11d67961 (b755's closing session, transcript line 69885, 2026-11-15T12:27:47Z); the act runs in it,
### one seat, with no change of session, harness or store (the step-zero reads of 2026-11-15T12:29:05Z).
### b755 closed and pushed itself whole (relay b19867ac, PLACE-papers 9011a84), its closing step row committed before its closing push; its
### closing push capture and tools/mirror_prevbuild.json are this act's carried files ((R366)(7)), committed at step zero, each alone.
### ANCHOR is the act's capture anchor (data/act_current.json, the ruling's first line); RULING_ANCHOR the same line, the citation tool's
### ferry source.
"""
import io
import json
import os
import re
from standing.carry import Carried as _Carried   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the stage-one values below refuse on use until written
from standing.carry import Carried as _Carried   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the stage-one values below refuse on use until written

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '9011a848e56be137819e490477d65dc91b87c16a'    # ### PLACE-papers main before the act's own commits: b755's record (the trail), pushed
PRE_RELAY = 'b19867ac7d76f2d0a3965120e8ceafbb5bac025a'  # ### relay main before the act's own commits: b755's closing step row, pushed
PRE_PP_REMOTE_AT_START = '9011a84'       # ### PLACE-papers origin/main at the act's start, read from the tracking ref (no remote read at step zero), equal to local
PRE_RELAY_REMOTE_AT_START = 'b19867ac'   # ### relay origin/main at the act's start, read from the tracking ref, equal to local
B718_RELAY_HEAD = 'b19867a'  # ### the names kept for the carried readers: the previous act's last relay head (b755's closing step row)
B718_PP_HEAD = '9011a84'     # ### the previous act's last PLACE-papers head (b755's record)
DATE = '2026-11-15'
SESSION_ID = '11d67961-2aa4-4353-bc12-a982038bfa55'   # ### the transcript the ruling and the ferry stand in (line 69885, 2026-11-15T12:27:47Z), b755's closing session; the act runs in it, one seat, no change of session, harness or store
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/0fa2f3b7e932577a/11d67961-2aa4-4353-bc12-a982038bfa55/scratchpad'   # ### the seat's scratchpad as the harness names it (session 11d67961, the act's own)
HOLD = 2560
ANCHOR = 'RULING (R366) BEGIN'           # ### the act's capture anchor, as data/act_current.json
RULING_ANCHOR = 'RULING (R366) BEGIN'    # ### the ruling's BEGIN line, the citation tool's ferry source
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()   # ### none: the act runs in the session its ruling was delivered in (b671's form not needed)
PREV_SESSION = '11d67961-2aa4-4353-bc12-a982038bfa55'   # ### b755 ran in this session from its delivery (2026-11-14T18:27:54Z) to its closing; (R366) was delivered in it after b755's close
PREV_ANCHOR = 'RULING (R365) BEGIN'   # ### the first user row of 11d67961 holding b755's ruling's first line (2026-11-14T18:27:54Z), before b755's post-push combine (2026-11-15T07:55:38Z); G-EDIT-ROUTE's window from that combine to (R366)'s anchor
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b756_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 15296          # ### FINDINGS: b755's entry head (at 7d6c10b, unmoved at 9011a84)
B711_WEIGHT = 15250         # ### FINDINGS: b754's weight line (b755's Component 1)
B711_CORRIGENDUM = 15252    # ### FINDINGS: b755's corrigendum for b754
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 18350          # ### OPEN_TRAILS: b755's trail record (PLACE-papers 9011a84)
B711_FACE = 'data/b755_registration_2026-11-14.txt'   # ### b755's face; the carry's shift of the date set to the file's own
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-11-14-b755.zip'   # ### b755's export, built after b755's last PLACE-papers push (data/b755_mirror_build.json); the date set to the file's own
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
ORDER_LEDGER_SPLIT = 14680  # ### OPEN_TRAILS: W-ORD-LEDGER-SPLIT-RESOLVER (b680), (R364)(3)
TRAIL_ORDERS = 18366        # ### OPEN_TRAILS: the last open-orders line, b755's, written from the generator's output
TRAIL_RESOLVED = 18394      # ### OPEN_TRAILS: b755's items for the author's strike, in its trail
TRAIL_RETIRED = 18380       # ### OPEN_TRAILS: b755's count line of the author's prompts
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

# ### the branches step zero deletes ((R364)(5)): the push-b753-* branches b753's close made, by name, each read from the listings and
# ### `--merged` printed before the deletes, one per command, each its own message
DELETE = (('D:/relay', ('push-b755-closing', 'push-b755-preroot', 'push-b755-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b755-preroot', 'push-b755-record')))   # ### (R364)(2): the five; b753 made no kernel branch
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### carried: NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'), ('D:/SIDE-explicit-formula', 'challenge-b720-h2-sign-iff-rh'),
                 ('D:/SIDE-lv-conservation', 'scratch-b724'), ('D:/SIDE-explicit-formula', 'keiper-b725'), ('D:/SIDE-explicit-formula', 'c2-b725'),
                 ('D:/SIDE-kernel', 'rebuild-b721'), ('D:/SIDE-lv-conservation', 'rebuild-b721'), ('D:/SIDE-archimedean', 'rebuild-b721'),
                 ('D:/SIDE-frobenius', 'rebuild-b721'), ('D:/SIDE-spinor', 'rebuild-b721'), ('D:/SIDE-rcurve', 'rebuild-b721'),
                 ('D:/SIDE-explicit-formula', 'detect-b729'), ('D:/SIDE-explicit-formula', 'zq-b730'))   # ### (R364)(4) names c2-b725, keiper-b725, detect-b729, zq-b730

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
EF_MAIN = '8fbab45d8a966dca53d42448e33927d885fd4ea3'    # ### SIDE-explicit-formula's main after [A4]: badacccb + README.md alone ((R364)(6))
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
SECTION_BANK = 'data/b752_attribution_plan.txt'      # ### b752's plan bank ((R366)(3)(ii), (iii) cite its :21), read not written
SECTION4_BANK = 'data/b748_section4.txt'              # ### b748's §4 bank, read not written
SECTION1_BANK = 'data/b747_section2.txt'              # ### b747's section bank (§2), read not written
INTEGRATION_DRAFT = 'data/b746_integration_draft.txt' # ### b746's canon text for the stages, entered at b753 as XXIII, read not written
ORDER_DRAFT = 'data/b746_order_draft.txt'             # ### (carried name) b746's order draft, read not written; no order entered this act
READBACK_747 = 'data/b747_zenodo_readback.txt'        # ### b747's read-back, read not written; no Zenodo call this act ((R364)(6))
RULES_747 = 'data/b756_rules.txt'                     # ### (R364)(3): the seat's reading of the corrigendum's repairs, each for the author's strike
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
COMPUTE_BANKS = ('data/b756_rules.txt', 'data/b756_corrigendum.txt', 'data/b756_reverse_read.txt', 'data/b756_orders_read.txt',
                 'data/b756_address_scan.txt')
#   ### the banks of (R366)(1)-(5) as the ruling names them, each written by its component; the constellation's banks named when written;
#   ### set by the Edit tool to the banks as written, before the lock
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt',
              'data/b729_read_calls.txt', 'data/b730_read_calls.txt', 'data/b755_read_calls.txt', 'data/b756_read_calls.txt')

# ### THE SUITE'S PARTS: ten, as b753 split them under (R363)(2)(vi) and b675 rules row (2) (standing-a in two, G-NO-SORRY-MAIN's kernels
# ### halved, and the chain's first half in four, b2a-b2d); data/act_current.json committed them ten at b754's step zero (22f59d27), no
# ### component splitting them this act, so PARTS_AT_STEP_ZERO is PARTS
PARTS = ('standing-a1', 'standing-a2', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d', 'standing-b3', 'act')
PARTS_AT_STEP_ZERO = PARTS
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b756'))
CHAIN_QUARTERS = (('b624', 'b627'), ('b628', 'b631'), ('b632', 'b635'), ('b636', 'b658'))   # ### carried from b753
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### set by the Edit tool when a component adds a standing arm
SHARED_APPENDED = ('data/b675_corrigenda.txt',)   # ### (R364)(2): the corrigenda row
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/method/INSTRUMENTS.md', 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md',
             'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'day1/Which_Structure_Confines_v2_4_0.md',
             'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md')
#   ### b756 step zero: (R366)(7)'s (W) list in PLACE-papers -- FINDINGS.md, OPEN_TRAILS.md, INSTRUMENTS ((5)(iii), (3)(vi)) and the four
#   ### documents of (3)(i) to (iv), each by its path at PLACE-papers 9011a84 (the ruling names them by their file names alone)
#   ### (R365)(9), N5: FINDINGS -- the weight line, the corrigendum, the entry; OPEN_TRAILS -- (7)'s line and the trail; nothing else
PP_WRITTEN = PP_EDITED
PP_NEW = ()
# ### (R364) amendment row 3 (6): THE (W) ENTRIES (R364)(8) GIVES IN WORDS, each with the clause that gives it, read by tools/standing/wlist.py
# ### (word_rows) into the (W) bank and by tools/standing/cites.py's ferry_paths for a name in no tree. The entries (8) gives "on its item's
# ### pass and not otherwise" are not rows here: each enters by its item's route ((R364)(3)(xvi), `amend.py pass`) on the pass.
W_WORDS = (('relay/HANDOFF.md', '(R366)(7): HANDOFF.md -- the handoff page regenerated once before the gate, by tools/standing/handoff.py'),
           ('relay/data/b757_address_scan_commits.txt', '(R366)(7): the scan banks -- the next act`s per-commit scan bank, by (R364)(3)(iii)`s route'))
#   ### b756 step zero: b755's rows carried with their clause moved to (R366)(7); the scan bank the next act's (b757), as b755's named b756's.
#   ### A kernel's README under (6) alone is entered when Component 5 names the kernel (an amendment row or a word row, before the write)
#   ### b755 step zero: b754's rows (CLAUDE.md, the four files of its step-zero restore) dropped -- (R365)(8)'s (W) list names neither;
#   ### data/b755_rules.txt, the carried capture and tools/mirror_prevbuild.json stand among the standing kinds (tools/standing/wlist.py)
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the re-cut's merge (kept for the kernel rows); the MANIFEST control's reference
#   ### is the commit the mirror is built at from v1.2.1
NEXT = '((R366)(7)) the build as b757 (the four branches of the criterion kernel joined under a tag on main; T0 and T1; the criterion over the wider strip; the modulus-24 lemma; the written proofs of the class-number-3 law and of the closed form), or another the author names'
NEXT_ACT = 'b757'   # ### NEXT above holds the act's own words for the question as put; from v1.34.7 tools/standing/nextact.py's line() heads the entry's and the closing's line with (R366)(1)(i)'s words and the answers bank


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
ACT_CURRENT_COMMIT = 'f6323978'         # ### data/act_current.json for b756 committed alone through the one-call tool ((R366)(7)), the scan in the call; its row step 1
STEPZERO = 'ac2ce70b'             # ### b755's closing push capture, committed alone ((R366)(7)); its row in the commit's call (step 2)
STEPZERO_STEPS = None             # ### b753's closing step row was committed by b753 itself (d921bceb) before its closing push: nothing carried
STEPZERO_TABLE = None             # ### b753 left no terminal table uncommitted
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None   # ### tools/mirror_prevbuild.json of b755: NO COMMIT -- b755's mirror left its content equal to HEAD (9171e0e2's blob, 4,316 bytes, lastChanged 2026-11-12-b754) and its working copy carrying 88 CRs alone; restored to HEAD by `commit.py relay restore` (2026-11-15T12:39:20Z), nothing to commit ((R366)(7))
STEPZERO_REFUSALS = ()
STEPZERO_BANKS = '1ff55fec'      # ### step zero's banks and carried tools, one commit (data/b756_stepzero.txt among them), row step 3, 2026-11-15T13:09:46Z
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
                          and f != 'report.tpl')) + ('acts/b756.py',)
NEW_TOOLS = NEW_TOOLS + FOLD_FILES
STANDING_VERSION = 'v1.35.3'            # ### the version the close runs under: entering v1.34.6; (R366)(1)'s two repairs v1.34.7 (C1_STANDING), (5)(i)'s HERE v1.34.8 (C4_HERE), (6)'s five v1.34.9 to v1.35.3 (C1_STANDING_LATER), each a commit of its own with its control banked, before the gate
STANDING_VERSION_ENTERING = 'v1.34.6'
LEAN_TREES = ()   # ### (R366) writes no Lean tree: no kernel touched beyond a README under (6), no Lean file written ((R366)(8)); the constellation reads declarations by git and writes none
# ### v1.18.0, (R364)(2)(ii): the act's banks whose comparative sentences the citation check reads, and a reading row for each word (tools/standing/cites.py
# ### comparative_rows); set by the Edit tool as Components 2-4 write the banks, before the lock
COMPARATIVE_BANKS = ('data/b756_corrigendum.txt', 'data/b756_rules.txt', 'data/b756_reverse_read.txt', 'data/b756_orders_read.txt',
                     'data/b756_defects.txt')
COMPARATIVE_ROWS = ()   # ### comparative word in them ("at least" excepted by the reader), so no reading row; the check reads the three for one
#   ### the trees the ruling's Lean paths are read against: zq-b730's tip, and Mathlib at its pin (the ferry's "Mathlib at the pin: Analysis/Complex/AbsMax.lean :405, ...")
STANDING_CHANGED = ('VERSION', 'amend.py', 'carry.py', 'commit.py', 'fold/checks.tpl', 'fold/record.tpl', 'gitwrite.py', 'manifest.py', 'nextact.py',
                    'orders.py', 'postseal.py', 'roster.py', 'subject.py')   # ### v1.34.7 to v1.35.3's changed files, by git diff --name-status b19867ac..ec63f53e -- tools/standing (13; b756, Component 6)
STANDING_NEW = ('cadence.py', 'deletefree.py', 'ledgers.py', 'ranahead.py', 'v1347.py', 'v1348.py', 'v1349.py', 'v1350.py', 'v1351.py', 'v1352.py',
                'v1353.py')   # ### their new files, the same diff (11)
# ### b753's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = 'b19867ac'    # ### b755's closing (its step row), the act's relay base
B714_RECORD = '6a7120a4'     # ### b755's record commit (relay)
B714_ROOT = '0ed5cf5ded61ecf1b26a9029e78500e39bf7317316dcc4bb9f1f47da16f1cbf5'   # ### b755's root, data/act_roots.txt's last row (:135)
B723_ROOT_BANKS = '80422324'  # ### b755's root commit, the banks its root rode with
# ### later stages: the commits of the components, read from the logs after each was made (None until made)
C1_STANDING = 'dc8319ea'     # ### tools/standing/ v1.34.7 by a commit of its own that moves VERSION, its control and the standing dry banked ((R366)(1)(i), (ii); step 4)
C1_LOCKGATE = '5e37bf97'     # ### tools/b756_lockgate.py carried from tools/b755_lockgate.py and committed before it runs ((R366)(1); step 5)
C1_STANDING_LATER = (('[U1]', 'v1.34.9', 'be3fc2b3'), ('[U2]', 'v1.35.0', '2c3acfca'), ('the faults, first', 'v1.35.1', '7fae9822'),
                     ('the faults, second', 'v1.35.2', '520777a8'), ('[H1]`s held part', 'v1.35.3', '47449d8b'))   # ### Component 5, (R366)(6): each a version commit of its own with its controls (steps 29, 31, 33, 34, 36)
C5_FAULTS = ('tools/b756_faults.py', '21b0c76e', 'tools/b756_faults_placed.py', 'aadd9d2d')   # ### the count and the placing (16 rows; 11 landed, 1 carried, 4 no code)
DOORS = ('tools/b756_doors.py', 'ec63f53e', 'data/b756_doors.txt')   # ### (6)'s README route: [B1] and [B3] HALTED, the two descriptions refused by the server at 350 characters, all four carried whole (step 37)
C5_LANDED, C5_CARRIED = 5, 1   # ### the tool changes of (6): [U1], [U2], the two fault versions, [H1] landed; the README route carried whole ([B1], [B3], the two descriptions)
C1_STANDING_REPAIR = None          # ### none in Component 1
C4_STANDING = None                 # ### none
C1_RELAY = '0a151012'        # ### the c1 route, the corrigendum banks, the corrigenda row (76), the rules bank (step 7)
C1_CORR = C1_RELAY
C1_RULES = '0a151012'        # ### data/b756_rules.txt, rows (a)-(c) of (R366)(2), in force from b757: committed with the c1 banks (C1_RELAY, step 7)
RULES_COMMITS = ()
C1_CEILING = '7300f70e'            # ### the ceiling read again after Component 3 ((R365)(8)), data/b755_ceiling.txt (step 18); the act's one ceiling bank
C1_PP = 'd1133807'           # ### PLACE-papers: FINDINGS -- b755 at its weight (:15344) and the corrigendum for b755 (:15346); OPEN_TRAILS -- (R366)(1)(i)'s dated line (:18402) (step 6)
C1_TAG_PP = ()                     # ### (carried name) no tag note this act
C1_DISCHARGE_PP = ()               # ### (carried name) no discharge this act
C2_TOOL = None                     # ### (carried name) no driver this act
WEIGHT_LINE, CORR_LINE = 15344, 15346   # ### FINDINGS: b755's weight line and the corrigendum for b755 (Component 1, PLACE-papers d1133807)
NEXT_TRAIL_LINE = 18402      # ### OPEN_TRAILS: (R366)(1)(i)'s dated line giving b755's answer (Component 1, PLACE-papers d1133807)
DIFFERS_LINE = None
ERRATA_LINE = None
C2_PLAN_FIRST = '3e112065'   # ### Component 2's first commit: tools/b756_constellation.py carried and repaired, committed before its run (step 8)
C2_RELAY_ALL = ('3e112065', 'd2f78fab', '16ba8fbb', 'e4701c5f', '069271bb')   # ### Component 2's relay commits in order (steps 8, 9, 10, 11, 12)
C2_RELAY = '069271bb'   # ### the last of them: the map's banks (step 12)
# ### (R366)(4): each tool of the map beside its banks -- (name, generator, the generator's commits before the bank, bank, the bank's commit)
C2_MAP = (('the constellation rerun', 'tools/b756_constellation.py', ('3e112065', 'd2f78fab', '16ba8fbb', 'e4701c5f'),
           'data/b756_constellation_summary.txt', '069271bb'),
          ('the reverse read', 'tools/b756_reverse.py', ('d2f78fab', '16ba8fbb'), 'data/b756_reverse_read.txt', '069271bb'),
          ('what the two find beyond (3)', 'tools/b756_reverse.py', ('d2f78fab', '16ba8fbb'), 'data/b756_beyond_three.txt', '069271bb'))
C2_WALK = ('tools/b756_coeffs.py', '3bdb6561', 'data/b756_walk.txt', '9a989df8')   # ### (generator, its commit, bank, the bank's commit)
REG_WALK = ('data/b753_registrations.txt', '3f865479')   # ### H-C3-LAW's registration read at its blob ((R365)(3)), the commit data/b755_walk.txt names
# ### Component 3 ((R365)(5)(i), (4)): the literature bank, the candidates' generators each committed before its run, the candidates bank with
# ### the prior clause, the ceiling read again; each candidate (label, generator, the generator's commits before its bank, bank, the bank's commit)
C3_LITERATURE = '51739651'
C3_CANDS = (('(a)', 'tools/b756_closed.py', ('a7034608',), 'data/b756_cand_a.txt', '1b84e4b1'),
            ('(h)', 'tools/b756_zlist.py', ('1b84e4b1',), 'data/b756_cand_h.txt', 'ea99215e'),
            ('(c)', 'tools/b756_cands.py', ('ea99215e', '1b361013'), 'data/b756_cand_c.txt', 'b4668b52'),
            ('(j)', 'tools/b756_cands.py', ('ea99215e', '1b361013'), 'data/b756_cand_j.txt', 'b4668b52'),
            ('(k)', 'tools/b756_cands.py', ('ea99215e', '1b361013'), 'data/b756_cand_k.txt', 'b4668b52'),
            ('(l)', 'tools/b756_cands.py', ('ea99215e', '1b361013'), 'data/b756_cand_l.txt', 'b4668b52'))
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
GENS = (('the constellation rerun', 'tools/b756_constellation.py', ('3e112065', 'd2f78fab', '16ba8fbb', 'e4701c5f'), 'data/b756_constellation_summary.txt', '069271bb'),
        ('the reverse read', 'tools/b756_reverse.py', ('d2f78fab', '16ba8fbb'), 'data/b756_reverse_read.txt', '069271bb'),
        ('the notes of (3)', 'tools/b756_notes.py', ('d8eaaa2b',), 'data/b756_notes.json', '9518d3a0'),
        ('the orders read', 'tools/b756_orders.py', ('5b3d5a60',), 'data/b756_orders_read.txt', 'f56557dd'),
        ('the twelve status lines', 'tools/b756_moves.py', ('208eee6a',), 'data/b756_orders_moves.txt', 'a26f30b9'),
        ('the ceiling after Component 4', 'tools/b756_ceiling.py', ('a26f30b9',), 'data/b756_ceiling_c4.txt', '1e35bedd'))
PASSED_BANK = '0b87054f'   # ### data/b756_passed.json, the passed writes' bank (the two writes and their confirms), committed at Component 6 before the act module (step 38)
GENS = GENS + ((('the two passed writes', 'tools/b756_passed.py', ('9aa5fe8c',), 'data/b756_passed.json', PASSED_BANK),) if PASSED_BANK else ())
GENS_WITH_BANK = (('the faults counted', 'tools/b756_faults.py', 'data/b756_faults.txt', '21b0c76e'),
                  ('the faults placed', 'tools/b756_faults_placed.py', 'data/b756_faults_placed.txt', 'aadd9d2d'),
                  ('the README route', 'tools/b756_doors.py', 'data/b756_doors.txt', 'ec63f53e'))
# ### b756, Component 6: the act's relay commits after step zero in their order (key, commit), and PLACE-papers' in theirs, each read by the act
# ### module's N2 arms (the order by time and by ancestry); the handoff page appended where made
CHAIN = (('standing', 'dc8319ea'), ('lockgate', '5e37bf97'), ('corr', '0a151012'), ('c2first', '3e112065'), ('c2_hand', 'd2f78fab'),
         ('c2_reverse', '16ba8fbb'), ('c2_digest', 'e4701c5f'), ('map', '069271bb'), ('notes_gen', 'd8eaaa2b'), ('notes', '9518d3a0'),
         ('orders_gen', '5b3d5a60'), ('orders', 'f56557dd'), ('put', '0803754c'), ('passed_gen', '9aa5fe8c'), ('v1348', '5b7aa91e'),
         ('moves_gen', '208eee6a'), ('moves', 'a26f30b9'), ('ceiling', '1e35bedd'), ('v1349', 'be3fc2b3'), ('v1350', '2c3acfca'),
         ('faults', '21b0c76e'), ('v1351', '7fae9822'), ('v1352', '520777a8'), ('placed', 'aadd9d2d'), ('v1353', '47449d8b'), ('doors', 'ec63f53e'))
PP_CHAIN = (('c1pp', 'd1133807'), ('pp_i', 'ed23042f'), ('pp_ii', 'a680411c'), ('pp_iii', '1795559c'), ('pp_iv', '2cab7417'), ('pp_v', '6fb72eba'),
            ('pp_cp', 'e50a394b'), ('pp_instruments', '3b45826d'))
# ### the order by time, relay and PLACE-papers together: each PLACE-papers key after the relay commit whose tool cut it
TIME_ORDER = ('actcur', 'stepzero', 'standing', 'lockgate', 'c1pp', 'corr', 'c2first', 'c2_hand', 'c2_reverse', 'c2_digest', 'map', 'notes_gen',
              'pp_i', 'pp_ii', 'pp_iii', 'pp_iv', 'pp_v', 'notes', 'orders_gen', 'orders', 'put', 'passed_gen', 'pp_cp', 'pp_instruments', 'v1348',
              'moves_gen', 'moves', 'ceiling', 'v1349', 'v1350', 'faults', 'v1351', 'v1352', 'placed', 'v1353', 'doors')
# ### the standing versions of the act, each (version, its commit, its controls bank, its cases): every one a commit of its own moving VERSION
STANDING_BANKS = (('v1.34.7', 'dc8319ea', 'data/b756_standing_v1347.txt', 16), ('v1.34.8', '5b7aa91e', 'data/b756_standing_v1348.txt', 11),
                  ('v1.34.9', 'be3fc2b3', 'data/b756_standing_v1349.txt', 33), ('v1.35.0', '2c3acfca', 'data/b756_standing_v1350.txt', 15),
                  ('v1.35.1', '7fae9822', 'data/b756_standing_v1351.txt', 13), ('v1.35.2', '520777a8', 'data/b756_standing_v1352.txt', 20),
                  ('v1.35.3', '47449d8b', 'data/b756_standing_v1353.txt', 13))
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
C3_PUTS = (('defect (c)', 'data/b756_put_1.json', '77ae83fe'), ('N5`s folder clause', 'data/b756_put_2.json', 'cb14bae1'))   # ### (subject, the put bank, the commit carrying it)
C3_SITTING_TOOL = ()
C3_SITTING_BANK = ()
SITTING_COMMIT = None
SITTING_BANK = None
ITEM_PP = ()   # ### no passed item's PLACE-papers write this act
SITTING_PP = ()
SITTING_GH = ()
SITTING_SETTINGS = ()
SITTING_ITEMS = None          # ### no sitting this act ((R366)); one put of at most four questions before the lock ((R366)(5)) and one question at the root ((R366)(7))
SITTING_STATES = {}
HANDOFF_COMMIT = None   # ### (R366)(7): HANDOFF.md regenerated once by tools/standing/handoff.py before the gate; set from its commit (b755's was 99e8a2c6)
C3_RELAY = ('d8eaaa2b', '9518d3a0')   # ### Component 3 ((R366)(3)): the notes tool with events (20) (step 13), the worklist's C3 values (step 19)
C3_NOTES_GEN = 'd8eaaa2b'   # ### Component 3: tools/b756_notes.py committed before its run, controls 11 of 11 and its dry over the five places (step 13)
C3_NOTES_PP = (('(i)', 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md', 'ed23042f'),
               ('(ii)', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'a680411c'),
               ('(iii)', 'day1/Which_Structure_Confines_v2_4_0.md', '1795559c'),
               ('(iv)', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md', '2cab7417'),
               ('(v)', 'OPEN_TRAILS.md', '6fb72eba'))   # ### (item, the file, the PLACE-papers commit), steps 14-18, each confirmed at HEAD by `tools/b756_notes.py confirm`
C3_NOTES_WRITTEN = 9   # ### the notes of (3): four notes and five trail lines, 9 of 9, each the ruling's text between its quotation marks (data/b756_notes.json)
# ### Component 4 ((R366)(5)): the put and the work its answers order, each value read from the step rows (data/b756_steps.json)
C4_READ = ('tools/b756_orders.py', '5b3d5a60', ('data/b756_orders_read.txt', 'data/b756_instruments_draft.txt'), 'f56557dd')   # ### the orders read and the two drafts
C4_PUT = ('data/b756_put_1.json', '0803754c')   # ### the one put, three questions, and the answers pair by its route, all three passed as recommended (step 22)
C4_PASSED_GEN = '9aa5fe8c'   # ### tools/b756_passed.py committed before its run, with events (21) (step 23)
C4_PASSED_PP = (('cp', 'OPEN_TRAILS.md', 'e50a394b'), ('instruments', 'phase1.5/method/INSTRUMENTS.md', '3b45826d'))   # ### steps 24, 25, each confirmed at HEAD (data/b756_passed.json)
C4_HERE = ('v1.34.8', '5b7aa91e', 'data/b756_standing_v1348.txt')   # ### W-ORD-LABEL-READER's predicate and control, controls 11 of 11 (step 26)
C4_MOVES = ('tools/b756_moves.py', '208eee6a', 'data/b756_orders_moves.txt', 'a26f30b9')   # ### the twelve status lines for this act's trail, controls 12 of 12 (steps 27, 28)
C4_CEILING = ('tools/b756_ceiling.py', 'a26f30b9', 'data/b756_ceiling_c4.txt')   # ### the ceiling after Component 4: 17.53 h against 24 h, nothing carried
C4_ORDERS = (1, 1, 5, 5)   # ### the orders: done, here, with the build, later (data/b756_orders_read.txt :87; data/b756_orders_moves.txt)
C4_CP = 'passed'           # ### CP-6 and CP-7 (data/b756_author_answers.txt :18; OPEN_TRAILS at e50a394b)
C4_LINE_GEN = None   # ### b755: no line bank; the entry's INTEGRATION line is (R365)'s, composed from the banks by the record module
C4_LINE = None       # ### Component 6: the act's INTEGRATION line
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
LV_ROWS = 'data/b756_lv_rows.json'
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
MAX_DISPATCHES = 0         # ### N1: no runner dispatch this act
MAX_C2, MAX_KEIPER = 0, 0
EF_DIR = 'D:/SIDE-explicit-formula'
EF_BASE = '8fbab45d8a966dca53d42448e33927d885fd4ea3'   # ### SIDE-explicit-formula's main entering the act (b743's [A4], README alone)
EF_MAIN_AFTER = EF_BASE   # ### unmoved: no kernel's main is touched ((R364)(6))
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
EF_RUNS = ()   # ### N1: no runner dispatch this act
EF_RUNS_B745 = (42388001562, 42388609600, 42391254295, 42392017104, 42393018408, 42393914259)   # ### N1: this act's dispatches, each read by its run id ((R364)(4)(c)): KERNEL (print stopped at maxErrors), KERNEL (13 names printed), BREAKS (lp_conj), KERNEL (SPZ1), KERNEL (SPZ2), KERNEL (SPZ3)
EF_RUNS_B742 = (42054839204, 42056405331, 42058361986, 42061332755, 42062848400, 42065597154, 42068096322)   # ### b753's seven, read not re-run; the last the SP4 grade run
EF_RUNS_B741 = (41931918742, 41935365948, 41936644993, 41938300160, 41939524029, 41940815524)   # ### b753's six: KERNEL (timing), BREAKS, KERNEL, BREAKS, BREAKS, KERNEL (SP3)
EF_RUNS_B740 = (41854903335, 41857376723, 41859346843)   # ### b753's three: BREAKS, BREAKS, KERNEL, read not re-run
EF_RUNS_B738 = (41732413170, 41732882564, 41733411736, 41734667160, 41735082430, 41736472780)   # ### b738's first six (of eleven), read not re-run
ZQ_RUN = 41483457057   # ### b737's grade run, the discharge's, read not re-run
EF_RUNS_B731 = (41371666217, 41372597450, 41373409167, 41374121055, 41374814817)   # ### b731's five, read not re-run
DISPATCH_ROWS = 'data/b756_dispatch_rows.json'
ERRATA_ID = None   # ### no erratum this act
ERRATA_IDS = ()   # ### no erratum this act
RETIRED_COUNT = 0
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list (the root answer's addition (b))
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b756_') and f.endswith('.py') and f != 'b756_report.py')) + NEW_TOOLS + COMPUTE_TOOLS + REPAIRED_TOOLS
# ### the act's arms over its own banks: set before the lock by the Edit tool -- b753's list, the act shift G-R363-ENTERED to G-R364-ENTERED,
# ### G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0 ((R364)(2)(iv))
ACT_ARMS = ('G-ACT-CURRENT', 'G-ARM-TAGS', 'G-ARMS-RETIRED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED', 'G-CLOSING-DRY-STEP', 'G-COEFFS-LAW',
            'G-CORRIGENDUM-ENTERED', 'G-COUNT-ROUTE-PRICED', 'G-DELETES-ONE-BRANCH', 'G-DERIVATION-GRADED', 'G-DIFFERS-ERRATA', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-GUARD-HELD', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LISTINGS-BEFORE-CLAUSES',
            'G-MEMBRANE-WIRED', 'G-OFFSET-POST-HOC', 'G-POSTROOT-WRITES-NONE', 'G-PREDICTION-FIRST', 'G-R366-ENTERED',
            'G-REGISTRATIONS-FIRST', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED', 'G-SURGERY-CARRIED', 'G-TOUCH-READ',
            'G-WRITELIST-MIRROR-STATE')

# ### b754 writes no kernel ((R364)(5)): no main touched, no branch made on a kernel
SITTING_TIPS = {}
SITTING_BASE = EF_BASE
SITTING_REPOS = tuple(sorted(SITTING_TIPS))
SITTING_BRANCH = None
SITTING_BANK = 'data/b756_sitting.txt'   # ### the record of the sitting, one row per item
KERNEL_BASES = 'data/b756_kernel_bases.json'
