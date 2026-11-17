# -*- coding: utf-8 -*-
"""b758_worklist.py -- THE ACT'S DATA, UNDER (R368). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b758: LANE TWO, ACT ONE HUNDRED AND EIGHTY-FIVE, THE LANDING -- b757 CLOSED BY ITS CARRIED STEPS AFTER THE READER'S REPAIR; THE
### JOIN LANDED AT v0.39; T0, T1 AND THE WIDE DIRECTION LANDED AT v0.40; TWO ROUTES; THE STATEMENTS BANKED FOR SECTIONS 6 TO 8.
### Each build a runner dispatch read by its run id, no lean process on this host (N1); nothing deposits, no Zenodo call (N5).
### Carried by diff from b757_worklist.py (data/b758_carry_worklist.txt); its stage one set at step zero with this act's figures by the
### seat's script (scratch wl758.py, each constant replaced whole by its name); later stages by the Edit tool.
### (R368) was delivered in session 11d67961 (b757's session, transcript line 112358, 2026-11-16T23:21:58Z); the act runs in it,
### one seat, with no change of session, harness or store (the step-zero reads of 2026-11-16T23:24:49Z).
### b757 stopped at its close step [22] on the author's word (data/b757_author_words.txt), its record pushed (relay ff65ccdb, PLACE-papers
### b8c0bd73); its uncommitted files are this act's carried files ((R368)(2)), committed at step zero; its steps [22]-[25] are Component 1's.
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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'b8c0bd73975a6352a2e18610b1c1051e87d733c5'    # ### PLACE-papers main before the act's own commits: b757's record (the trail), pushed
PRE_RELAY = 'ff65ccdb374c0379c44bec68a135c4a24aec9925'  # ### relay main before the act's own commits: b757's step row after its record, pushed
PRE_PP_REMOTE_AT_START = 'b8c0bd7'       # ### PLACE-papers origin/main at the act's start, read from the tracking ref (no remote read at step zero), equal to local
PRE_RELAY_REMOTE_AT_START = 'ff65ccdb'   # ### relay origin/main at the act's start, read from the tracking ref, equal to local
B718_RELAY_HEAD = 'ff65ccd'  # ### the names kept for the carried readers: the previous act's last relay head (b757's step row after its record; its close stopped at [22])
B718_PP_HEAD = 'b8c0bd7'     # ### the previous act's last PLACE-papers head (b757's record)
DATE = '2026-11-16'
SESSION_ID = '11d67961-2aa4-4353-bc12-a982038bfa55'   # ### the transcript the ruling and the ferry stand in (line 112358, 2026-11-16T23:21:58Z), b757's session; the act runs in it, one seat, no change of session, harness or store
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/0fa2f3b7e932577a/11d67961-2aa4-4353-bc12-a982038bfa55/scratchpad'   # ### the seat's scratchpad as the harness names it (session 11d67961, the act's own)
HOLD = 2560
ANCHOR = 'RULING (R368) BEGIN'           # ### the act's capture anchor, as data/act_current.json
RULING_ANCHOR = 'RULING (R368) BEGIN'    # ### the ruling's BEGIN line, the citation tool's ferry source
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()   # ### none: the act runs in the session its ruling was delivered in (b671's form not needed)
PREV_SESSION = '11d67961-2aa4-4353-bc12-a982038bfa55'   # ### b757 ran in this session from its delivery (2026-11-16T04:32:48Z) to its stop at close step [22]; (R368) was delivered in it after that stop
PREV_ANCHOR = 'RULING (R367) BEGIN'   # ### the first user row of 11d67961 holding b757's ruling's first line (2026-11-16T04:32:48Z), before b757's post-push combine (2026-11-16T21:54:54Z); G-EDIT-ROUTE's window from that combine to (R368)'s anchor
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b758_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 15436          # ### FINDINGS: b757's entry head (at 9325fce1, unmoved at b8c0bd73)
B711_WEIGHT = 15414         # ### FINDINGS: b756's weight line (b757's Component 1)
B711_CORRIGENDUM = 15416    # ### FINDINGS: b757's corrigendum for b756
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 18507          # ### OPEN_TRAILS: b757's trail record (PLACE-papers b8c0bd73)
B711_FACE = 'data/b757_registration_2026-11-16.txt'   # ### b757's face
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-11-15-b756.zip'   # ### the last export built, b756's (data/b756_mirror_build.json): b757 built none before its stop at [22]; its step [23], in this act's Component 1, builds b757's, and the name moves to it when built
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
ORDER_LEDGER_SPLIT = 14680  # ### OPEN_TRAILS: W-ORD-LEDGER-SPLIT-RESOLVER (b680), (R364)(3)
TRAIL_ORDERS = 18521        # ### OPEN_TRAILS: the last open-orders line, b757's, written from the generator's output
TRAIL_RESOLVED = 18549      # ### OPEN_TRAILS: b757's items for the author's strike, in its trail
TRAIL_RETIRED = 18535       # ### OPEN_TRAILS: b757's count line of the author's prompts
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

# ### the branches step zero deletes ((R368)(2)): the push-b757-* branches of the relay and PLACE-papers, by name, each read from the
# ### `--merged` listing printed before the deletes as a captured shell command (23:4xZ: relay 35a12168 and ff65ccdb, PLACE-papers 9325fce
# ### and b8c0bd7, each merged into main), one per command, each its own message; no push-b757-closing, b757 having stopped at [22]
DELETE = (('D:/relay', ('push-b757-preroot', 'push-b757-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b757-preroot', 'push-b757-record')))   # ### the four; the kernels' push-b757-* stay until (5) lands
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
EF_MAIN = '630cba16e228a018f9dd986196142fc6feb704ec'    # ### b758: SIDE-explicit-formula's main at the close -- (5)'s merge at v0.40 (04:37:50Z, tag object d86d8cf5), after (4)'s landing at v0.39 = d1afb4fc (02:56:24Z) (entering at 8fbab45d, EF_BASE)
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
SECTION_BANK = 'data/b757_outcomes.txt'      # ### b757's outcomes bank ((R368)(1) reads its :132; (5)'s grades its :30, :71-:72, :101-:126), read not written
SECTION4_BANK = 'data/b748_section4.txt'              # ### b748's §4 bank, read not written
SECTION1_BANK = 'data/b747_section2.txt'              # ### b747's section bank (§2), read not written
INTEGRATION_DRAFT = 'data/b746_integration_draft.txt' # ### b746's canon text for the stages, entered at b753 as XXIII, read not written
ORDER_DRAFT = 'data/b746_order_draft.txt'             # ### (carried name) b746's order draft, read not written; no order entered this act
READBACK_747 = 'data/b747_zenodo_readback.txt'        # ### b747's read-back, read not written; no Zenodo call this act ((R364)(6))
RULES_747 = 'data/b758_rules.txt'                     # ### (R364)(3): the seat's reading of the corrigendum's repairs, each for the author's strike
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
COMPUTE_BANKS = ('data/b758_presend.txt', 'data/b758_epstein_statements.txt', 'data/b758_corrigendum.txt', 'data/b758_dispatch_rows.json',
                 'data/b758_address_scan.txt')
#   ### the banks of (R368)(1)-(9) as the ruling names them, each written by its component; the builds' banks named when written;
#   ### set by the Edit tool to the banks as written, before the lock
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt',
              'data/b729_read_calls.txt', 'data/b730_read_calls.txt', 'data/b757_read_calls.txt', 'data/b758_read_calls.txt')

# ### THE SUITE'S PARTS: ten, as b753 split them under (R363)(2)(vi) and b675 rules row (2) (standing-a in two, G-NO-SORRY-MAIN's kernels
# ### halved, and the chain's first half in four, b2a-b2d); data/act_current.json committed them ten at b754's step zero (22f59d27), no
# ### component splitting them this act, so PARTS_AT_STEP_ZERO is PARTS
PARTS = ('standing-a1', 'standing-a2', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d', 'standing-b3', 'act')
PARTS_AT_STEP_ZERO = PARTS
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b758'))
CHAIN_QUARTERS = (('b624', 'b627'), ('b628', 'b631'), ('b632', 'b635'), ('b636', 'b658'))   # ### carried from b753
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### set by the Edit tool when a component adds a standing arm
SHARED_APPENDED = ('data/b675_corrigenda.txt',)   # ### (R364)(2): the corrigenda row
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md',
             'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md')
#   ### b758 step zero: (R368)(10)'s (W) list in PLACE-papers -- FINDINGS.md, OPEN_TRAILS.md, REGISTRY.md, FACES_LEDGER.md and the two
#   ### documents of (8), each by its path at PLACE-papers b8c0bd73 (the ruling names them by their file names alone)
#   ### (R365)(9), N5: FINDINGS -- the weight line, the corrigendum, the entry; OPEN_TRAILS -- (7)'s line and the trail; nothing else
PP_WRITTEN = PP_EDITED
PP_NEW = ()
# ### (R364) amendment row 3 (6): THE (W) ENTRIES (R364)(8) GIVES IN WORDS, each with the clause that gives it, read by tools/standing/wlist.py
# ### (word_rows) into the (W) bank and by tools/standing/cites.py's ferry_paths for a name in no tree. The entries (8) gives "on its item's
# ### pass and not otherwise" are not rows here: each enters by its item's route ((R364)(3)(xvi), `amend.py pass`) on the pass.
W_WORDS = (('relay/HANDOFF.md', '(R368)(10): HANDOFF.md -- the handoff page regenerated once before the gate, by tools/standing/handoff.py'),
           ('relay/data/b759_address_scan_commits.txt', '(R368)(10): the scan banks -- the next act`s per-commit scan bank, by (R364)(3)(iii)`s route'),
           ('relay/data/b757_checks_postpush*', '(R368)(2), (10): b757`s carried files -- the post-push suite`s banks, committed alone'),
           ('relay/data/b757_chain_half_*_checks_postpush.json', '(R368)(2), (10): b757`s carried files -- the post-push suite`s chain banks'),
           ('relay/data/b757_lsr_postpush_*', '(R368)(2), (10): b757`s carried files -- the post-push suite`s remote-read banks'),
           ('relay/data/b757_exercise*.json', '(R368)(2), (10): b757`s carried files -- the exercise banks the suite rewrote'),
           ('relay/data/b757_put_3.json', '(R368)(2), (10): b757`s carried files -- the [22] halt question as the composer banked it'),
           ('relay/data/b757_author_words.txt', '(R368)(1), (2), (10): b757`s carried files -- the author`s word of 2026-11-16T23:02:40Z'),
           ('relay/data/b757_address_scan_commits.txt', '(R368)(2), (10): b757`s carried files -- the per-commit scan bank'),
           ('relay/data/b757_hook_refusals.txt', '(R368)(1), (10): b757`s refusals bank with its post-lock row :7 (2026-11-16T23:19:16Z), an event of the corrigendum'),
           ('relay/data/b757_scores_close.json', '(R368)(1), (10): b757`s close`s banks -- [22] the scores close'),
           ('relay/data/b757_mirror*', '(R368)(1), (10): b757`s close`s banks -- [23] the mirror'),
           ('relay/data/b757_report.txt', '(R368)(1), (10): b757`s close`s banks -- [24] the report`s scores line'),
           ('relay/data/b757_closing.txt', '(R368)(1), (10): b757`s close`s banks -- [25] the closing record'),
           ('relay/data/b757_faces_census_closing.txt', '(R368)(1), (10): b757`s close`s banks -- [25] the closing`s census read'),
           ('relay/data/b757_pins_closing.txt', '(R368)(1), (10): b757`s close`s banks -- [25] the closing`s pins read'),
           ('relay/data/b757_steps.json', '(R368)(1), (10): b757`s close`s banks -- the close`s step rows'),
           ('SIDE-explicit-formula/SIDEExplicitFormula/Schema/ZQ/OffZero/Time.lean', '(R368)(4), (10): the one commit renaming sRe at :18 to timeSRe, with its uses in that file'),
           ('SIDE-explicit-formula/print_targets.txt', '(R368)(5), (10): the conflicted merge resolved as the union of both sides, lines naming no declaration of the merged tree removed'))
#   ### b758 step zero: (R368)(10)'s (W) list in words: HANDOFF.md; the next act's scan bank (b759, as b757 named b758's); b757's carried
#   ### files and its close's banks by name (its push captures stand among the standing kinds, data/<prev>_*_push_out.txt); in
#   ### SIDE-explicit-formula Schema/ZQ/OffZero/Time.lean and print_targets.txt by the paths the tree holds at 6568e9c7; PLACE-papers by PP_EDITED
#   ### b755 step zero: b754's rows (CLAUDE.md, the four files of its step-zero restore) dropped -- (R365)(8)'s (W) list names neither;
#   ### data/b755_rules.txt, the carried capture and tools/mirror_prevbuild.json stand among the standing kinds (tools/standing/wlist.py)
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the re-cut's merge (kept for the kernel rows); the MANIFEST control's reference
#   ### is the commit the mirror is built at from v1.2.1
NEXT = 'the act after this one, as the author answers at the root (the answers bank) ((R368)(10)): sections 6 to 8 entered from the draft of the navigator with the word of the author; or the written proof of the class-number-3 coefficient law with the four carried orders priced beside it; or another the author names'
NEXT_ACT = 'b759'


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
ACT_CURRENT_COMMIT = '49c58344'         # ### data/act_current.json for b758 committed alone through the one-call tool ((R368)(2)), the scan in the call; its row step 1 (23:38:49Z)
STEPZERO = 'a44f2c06'             # ### the first of b757's carried files committed alone ((R368)(2)): the post-push suite's 27 banks; step 2 (23:39:28Z)
# ### b758: b757's carried files, each group committed alone ((R368)(2)), in the order made: (commit, step, the files)
STEPZERO_CARRIED = (('a44f2c06', 2, 'the post-push suite`s 27 banks'), ('59a3244b', 3, 'the 11 exercise banks the suite rewrote'),
                    ('b8ea1f01', 4, 'the two record-push captures'), ('776cf191', 5, 'data/b757_put_3.json'),
                    ('9869af85', 6, 'data/b757_author_words.txt'), ('2672f85d', 7, 'data/b757_address_scan_commits.txt'),
                    ('41ff314d', 8, 'data/b757_hook_refusals.txt with its row :7'))
STEPZERO_STEPS = None             # ### b757's step rows stand committed by b757 itself (its record's step-row commit): nothing carried
STEPZERO_TABLE = None             # ### b757 left no terminal table uncommitted
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None   # ### none: b757 built no mirror before its stop at [22] (tools/mirror_prevbuild.json restored to its HEAD bytes at b757, 19:44:53Z, and unchanged since)
STEPZERO_REFUSALS = ('41ff314d',)   # ### data/b757_hook_refusals.txt with its post-lock row :7 (PIPE, 23:19:16Z), committed alone, step 8
STEPZERO_SCAN = '2672f85d'   # ### data/b757_address_scan_commits.txt as b757's record step-row commit left it, committed alone, step 7
STEPZERO_BANKS = '53fdf82d'      # ### step zero's banks and carried tools, one commit (data/b758_stepzero.txt among them), step 9 (00:02:52Z)
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
                          and f != 'report.tpl')) + ('acts/b758.py',)
NEW_TOOLS = NEW_TOOLS + FOLD_FILES
STANDING_VERSION = 'v1.35.5'            # ### entering; (R368)(1)'s reader repair lands by a commit of its own that moves VERSION (C1_STANDING), its controls printed before any use; (3), (6) and (9) by later versions, before the gate
STANDING_VERSION_ENTERING = 'v1.35.5'
LEAN_TREES = (('D:/SIDE-explicit-formula', '8fbab45d'), ('D:/SIDE-explicit-formula', '6568e9c7'), ('D:/SIDE-explicit-formula', '596d1c9e'),
              ('D:/SIDE-dirichlet-mod-24', 'e5ebdd15'))   # ### (R368)'s scope read: SIDE-explicit-formula's main, push-b757-join and push-b757-coeff; SIDE-dirichlet-mod-24 at main
# ### v1.18.0, (R364)(2)(ii): the act's banks whose comparative sentences the citation check reads, and a reading row for each word (tools/standing/cites.py
# ### comparative_rows); set by the Edit tool as Components 2-4 write the banks, before the lock
COMPARATIVE_BANKS = ('data/b758_corrigendum.txt', 'data/b758_presend.txt', 'data/b758_epstein_statements.txt', 'data/b758_defects.txt')
COMPARATIVE_ROWS = ()   # ### comparative word in them ("at least" excepted by the reader), so no reading row; the check reads the three for one
#   ### the trees the ruling's Lean paths are read against: zq-b730's tip, and Mathlib at its pin (the ferry's "Mathlib at the pin: Analysis/Complex/AbsMax.lean :405, ...")
STANDING_CHANGED = ('VERSION', 'commit.py', 'fold/closing.tpl', 'fold/record.tpl')   # ### v1.35.4 and v1.35.5's changed files, by git diff --name-status 38024feb..c92fca81 -- tools/standing/ (4; b757, Component 6)
STANDING_NEW = ('v1354.py', 'v1355.py')   # ### their new files, the same diff (2)
# ### b753's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = 'ff65ccdb'    # ### b757's last commit (its step row after the record; no closing, the close stopped at [22]), the act's relay base
B714_RECORD = '5cf8c377'     # ### b757's record commit (relay)
B714_ROOT = '95f84fdeeb9dac74d1b65c8964609ed5c6cb8bd257ebda274b41adcb2cdd6ed9'   # ### b757's root, data/act_roots.txt's last row (:137)
B723_ROOT_BANKS = '6b47664a'  # ### b757's root commit, the banks its root rode with
# ### later stages: the commits of the components, read from the logs after each was made (None until made)
C1_STANDING = 'da79951c'     # ### b758: the kernel route, v1.35.9, a commit of its own moving VERSION with its controls (data/b758_standing_v1359.txt), before any kernel write (events (34)); N2's "standing change before its use" read at it
C1_LOCKGATE = None           # ### b758: the act's lock gate, set when made (b757's 24fca573 carried until Component 5, read by _chain as this act's)
C1_STANDING_LATER = (('(8)(ii)', 'v1.35.5', 'e0428564'),)   # ### Component 6, (R367)(8)(ii): the closing's one count in one form, a version commit of its own with its controls 6 of 6 (step 51)
C5_FAULTS = ()   # ### (carried name) no fault count this act
DOORS = ('tools/b758_doors.py', '2bc7eca8', 'data/b758_doors.txt', 'c98beed0')   # ### (R367)(8)(v): the two passed descriptions sent by gh and each read back equal (tool step 48, bank step 50)
C5_LANDED, C5_CARRIED = 5, 0   # ### the repairs of (8): (i) the cut, (ii) v1.35.5, (iii) the gh-call reader, (iv) REGISTRY's header, (v) the two descriptions; none carried
C1_STANDING_REPAIR = None          # ### none in Component 1
C4_STANDING = None                 # ### none
C1_RELAY = 'f20e2be2'        # ### b758: the c1 route committed before it wrote (01:25:08Z, events (33))
C1_CORR = '2f3287de'         # ### b758: the corrigendum banks, data/b758_corrigendum.txt, .json, the corrigenda bank's row (78) (01:27:18Z, events (33))
B757_CLOSE = '401d3bda'      # ### b758 (R368)(1): b757's steps [22]-[25] under v1.35.7, committed under component 1 (01:07:08Z, events (19))
STATEMENTS_GEN = '4f069656'  # ### (R368)(7): tools/b758_statements.py as last committed before its bank (events (42))
KERNEL_DELETES = ()          # ### (R368)(5): the merged kernel branches deleted at the remote after v0.40, (branch, its tip), set as each is deleted: none, the route lacking
# ### (R368)(5) orders the four deleted "at the remote by the tool's route, each by name"; the route stands nowhere: tools/standing/commit.py's
# ### kernel delete (:755-:765) is `git branch -d/-D`, local alone; tools/push_gated.sh "deletes nothing" (:22); `pushto` (v1.36.1) pushes a
# ### commit to a branch name; the hook refuses a plain git write (PLAINGIT). Read at 04:3xZ with the four at the remote by one ls-remote
# ### (push-b757-coeff 596d1c9e, push-b757-join 6568e9c7, push-b758-coeff 630cba16, push-b758-land d1afb4fc, each merged into main 630cba16);
# ### no delete substituted, local or plain; the four carried with the route printed (events (52))
KERNEL_DELETES_HALT = ('the delete of a kernel`s branch at its remote', 'push-b757-join', 'push-b757-coeff', 'push-b758-land', 'push-b758-coeff')
CHAIN_WORDS = {}             # ### b758: each CHAIN and PP_CHAIN key's words in the entry's order paragraph, set with CHAIN at Component 5
C1_RULES = None              # ### no rules bank this act: (R367) orders none; data/b756_rules.txt's rows (a)-(c), in force from b757, read at b756's commit
B756_RULES = ('data/b757_rules.txt', '0a151012')   # ### the rule this act works by ((R366)(2)), its bank and b756's commit carrying it
RULES_COMMITS = ()
C1_CEILING = '0f620cdb'            # ### b758 (R368)(2): the commit carrying data/b758_ceiling.txt's last reading -- the second, after Component 3 (04:43:13Z, 5.35 h of 16, nothing carried), the first at b9e4c79f (02:40:22Z)
C1_PP = '6c50d50d'           # ### b758: PLACE-papers FINDINGS -- the corrigendum for b757 at :15484 (01:26:32Z, events (33))
C1_TAG_PP = ()                     # ### (carried name) no tag note this act
C1_DISCHARGE_PP = ()               # ### (carried name) no discharge this act
C2_TOOL = None                     # ### (carried name) no driver this act
WEIGHT_LINE, CORR_LINE = None, None   # ### FINDINGS: b757's weight line and the corrigendum for b757 (Component 1)
NEXT_TRAIL_LINE = 18491      # ### OPEN_TRAILS: (R367)(1)'s dated line giving b756's answer, in (9)'s block (Component 6, PLACE-papers b14256c2)
DIFFERS_LINE = None
ERRATA_LINE = None
C2_PLAN_FIRST = None   # ### Component 2's first commit
C2_RELAY_ALL = ()   # ### Component 2's relay commits in order, set as each is made
C2_RELAY = None   # ### the last of them
# ### (R366)(4): each tool of the map beside its banks -- (name, generator, the generator's commits before the bank, bank, the bank's commit)
C2_MAP = (('the constellation rerun', 'tools/b758_constellation.py', ('3e112065', 'd2f78fab', '16ba8fbb', 'e4701c5f'),
           'data/b758_constellation_summary.txt', '069271bb'),
          ('the reverse read', 'tools/b758_reverse.py', ('d2f78fab', '16ba8fbb'), 'data/b758_reverse_read.txt', '069271bb'),
          ('what the two find beyond (3)', 'tools/b758_reverse.py', ('d2f78fab', '16ba8fbb'), 'data/b758_beyond_three.txt', '069271bb'))
C2_WALK = ('tools/b758_coeffs.py', '3bdb6561', 'data/b758_walk.txt', '9a989df8')   # ### (generator, its commit, bank, the bank's commit)
REG_WALK = ('data/b753_registrations.txt', '3f865479')   # ### H-C3-LAW's registration read at its blob ((R365)(3)), the commit data/b755_walk.txt names
# ### Component 3 ((R365)(5)(i), (4)): the literature bank, the candidates' generators each committed before its run, the candidates bank with
# ### the prior clause, the ceiling read again; each candidate (label, generator, the generator's commits before its bank, bank, the bank's commit)
C3_LITERATURE = '51739651'
C3_CANDS = (('(a)', 'tools/b758_closed.py', ('a7034608',), 'data/b758_cand_a.txt', '1b84e4b1'),
            ('(h)', 'tools/b758_zlist.py', ('1b84e4b1',), 'data/b758_cand_h.txt', 'ea99215e'),
            ('(c)', 'tools/b758_cands.py', ('ea99215e', '1b361013'), 'data/b758_cand_c.txt', 'b4668b52'),
            ('(j)', 'tools/b758_cands.py', ('ea99215e', '1b361013'), 'data/b758_cand_j.txt', 'b4668b52'),
            ('(k)', 'tools/b758_cands.py', ('ea99215e', '1b361013'), 'data/b758_cand_k.txt', 'b4668b52'),
            ('(l)', 'tools/b758_cands.py', ('ea99215e', '1b361013'), 'data/b758_cand_l.txt', 'b4668b52'))
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
GENS = (('the pre-send reads', 'tools/b758_presend.py', ('06eaa976', '2e103c46'), 'data/b758_presend.txt', '7aaa2863'),
        ('the landing read', 'tools/b758_join.py', ('7aaa2863',), 'data/b758_land.txt', 'b83b3cac'),
        ('the merge of (5)', 'tools/b758_join.py', ('7aaa2863', 'f8b607a5'), 'data/b758_coeff.txt', '6e14bfe4'),
        ('the controls tool`s controls', 'tools/b758_controls.py', ('7aaa2863',), 'data/b758_controls_control.txt', 'b83b3cac'),
        ('the outcomes', 'tools/b758_outcomes.py', ('6db2be8d',), 'data/b758_outcomes.txt', '6490bf35'),
        ('the moved cites of (8)', 'tools/b758_notes.py', ('4ca805a4', '5559a08b'), 'data/b758_moved_cites.txt', 'ca551bb4'),
        ('the ceiling', 'tools/b758_ceiling.py', ('96a22fde',), 'data/b758_ceiling.txt', '0f620cdb'),
        ('the statements of (7)', 'tools/b758_statements.py', ('5764d817', '4f069656'), 'data/b758_epstein_statements.txt', '0f620cdb'),
        ('the notes of (8)', 'tools/b758_notes.py', ('4ca805a4', '5559a08b', 'a90f680a'), 'data/b758_notes.json', '5615a84f'),   # ### defect (c): repaired a90f680a
        ('the dispatches', 'tools/b758_controls.py', ('7aaa2863',), 'data/b758_controls.txt', '63f25a83'))
PASSED_BANK = None   # ### (carried name) no passed writes this act
GENS_WITH_BANK = ()  # ### none: each act tool committed before its run
# ### b758, Component 5: the act's relay commits after step zero in their order (key, commit), and PLACE-papers' in theirs, each read by the act
# ### module's N2 arms (the order by time and by ancestry) and the entry's order paragraph (CHAIN_WORDS); later commits appended as made; the
# ### lock gate and the handoff page appended by _chain where made
CHAIN = (('presend_gen', '06eaa976'), ('presend_fix', '2e103c46'), ('v1356', 'ac6a0a77'), ('words', 'b663b331'), ('v1357', '248cacb8'),
         ('b757_close', '401d3bda'), ('v1358', 'ed0d3f33'), ('c1', 'f20e2be2'), ('corr', '2f3287de'), ('v1359', 'da79951c'), ('join_gen', '7aaa2863'),
         ('dispatch1', 'b83b3cac'), ('join_ext', 'f8b607a5'), ('v1360', 'fd45f4c5'), ('v1361', '9bc8cfeb'), ('v1362', '4db55035'), ('side_rule', 'ae24d870'),
         ('statements_gen', '5764d817'), ('statements_fix', '4f069656'), ('outcomes_gen', '6db2be8d'), ('notes_gen', '4ca805a4'), ('notes_fix', '5559a08b'),
         ('moved', 'ca551bb4'), ('ceiling_gen', '96a22fde'), ('ceiling1', 'b9e4c79f'), ('read1', '064afdd6'), ('rows1', 'a3371bc3'), ('landed', '6e14bfe4'),
         ('record1', '54fb61ff'), ('record2', '32e23cbe'), ('closing', 'c6a1f6ec'), ('regspec', 'ae675194'), ('overrides', '7822fd02'),
         ('checks', '12d2fc58'), ('carries', 'a85d414c'), ('read2', '4905d3e3'), ('rows2', 'ac6def8e'), ('landed2', '6490bf35'), ('deletes', 'cfca142a'),
         ('statements', '0f620cdb'), ('notes_fix2', 'a90f680a'), ('notes', '5615a84f'), ('controls', '63f25a83'))
PP_CHAIN = (('c1pp', '6c50d50d'), ('pp_a', 'babcc8ea'), ('pp_b', 'fbfec0f5'), ('pp_c', '7f96a8c6'), ('pp_d', 'a3fad736'), ('pp_e', 'cd42d8e9'))   # ### the corrigendum, then the notes of (8), (a) to (e)
# ### the order by time, relay and PLACE-papers together: each PLACE-papers key after the relay commit whose tool cut it
TIME_ORDER = ('actcur', 'stepzero', 'presend_gen', 'presend_fix', 'v1356', 'words', 'v1357', 'b757_close', 'v1358', 'c1', 'c1pp', 'corr', 'v1359',
              'join_gen', 'dispatch1', 'join_ext', 'v1360', 'v1361', 'v1362', 'side_rule', 'statements_gen', 'statements_fix', 'outcomes_gen', 'notes_gen',
              'notes_fix', 'moved', 'ceiling_gen', 'ceiling1', 'read1', 'rows1', 'landed', 'record1', 'record2', 'closing', 'regspec', 'overrides',
              'checks', 'carries', 'read2', 'rows2', 'landed2', 'deletes', 'statements', 'pp_a', 'notes_fix2', 'pp_b', 'pp_c', 'pp_d', 'pp_e', 'notes',
              'controls')
CHAIN_WORDS.update({'presend_gen': 'the pre-send tool', 'presend_fix': 'its bound on the names of anonymous instances', 'v1356': 'v1.35.6, the reader`s repair',
                    'words': 'the author`s answer and the amendment of (1)', 'v1357': 'v1.35.7, the bound', 'b757_close': 'b757`s four carried steps',
                    'v1358': 'v1.35.8, the title rule', 'c1': 'the c1 route', 'c1pp': 'the corrigendum', 'corr': 'the corrigendum banks',
                    'v1359': 'v1.35.9, the kernel route', 'join_gen': 'the join reader and the controls tool, with the pre-send bank',
                    'dispatch1': 'the landing read and dispatch 1', 'join_ext': 'the join tool extended for (5)', 'v1360': 'v1.36.0, the fast-forward route',
                    'v1361': 'v1.36.1, the push route', 'v1362': 'v1.36.2, the arm and the face', 'side_rule': 'the side rule narrowed',
                    'statements_gen': 'the statements tool', 'statements_fix': 'its bank route', 'outcomes_gen': 'the outcomes tool', 'notes_gen': 'the notes tool',
                    'notes_fix': 'its moved-cite reader sorted', 'moved': 'the moved cites', 'ceiling_gen': 'the ceiling tool',
                    'ceiling1': 'the record`s reads and the ceiling`s first reading', 'read1': 'dispatch 1 read and the outcomes', 'rows1': 'its step row',
                    'landed': 'the join landed at v0.39 and the merge with dispatch 2', 'record1': 'the entry rewritten', 'record2': 'the trail record',
                    'closing': 'the closing record', 'regspec': 'the regspec and the report', 'overrides': 'the overrides and the delete arms',
                    'checks': 'the checks rewritten', 'carries': 'the three close tools carried', 'read2': 'dispatch 2 read and the outcomes',
                    'rows2': 'its step row', 'landed2': 'the three landed at v0.40', 'deletes': 'the deletes carried, the route lacking',
                    'statements': 'the ceiling after Component 3 and the statements of (7)', 'pp_a': 'the Epstein note', 'notes_fix2': 'the notes tool repaired',
                    'pp_b': 'the FACES_LEDGER update', 'pp_c': 'the census note', 'pp_d': 'the REGISTRY note', 'pp_e': 'the OPEN_TRAILS block',
                    'notes': 'the notes bank', 'controls': 'the controls bank'})
# ### the standing versions of the act, each (version, its commit, its controls bank, its cases): every one a commit of its own moving VERSION
STANDING_BANKS = (('v1.35.6', 'ac6a0a77', 'data/b758_standing_v1356.txt', 11), ('v1.35.7', '248cacb8', 'data/b758_standing_v1357.txt', 16),
                  ('v1.35.8', 'ed0d3f33', 'data/b758_standing_v1358.txt', 7), ('v1.35.9', 'da79951c', 'data/b758_standing_v1359.txt', 8),
                  ('v1.36.0', 'fd45f4c5', 'data/b758_standing_v1360.txt', 10), ('v1.36.1', '9bc8cfeb', 'data/b758_standing_v1361.txt', 11),
                  ('v1.36.2', '4db55035', 'data/b758_standing_v1362.txt', 6))   # ### b758: the reader's repair (R368)(1), the bound (amendment row 1), the title rule (3), the kernel route, the two routes (6)(i)-(ii), the arm and the face (6)
STANDING_BANKS_B757 = (('v1.35.4', '26ac811e', 'data/b757_standing_v1354.txt', 20), ('v1.35.5', 'e0428564', 'data/b757_standing_v1355.txt', 6))
# ### the kernel commits of the act, read by N5 and G-OFFSET-POST-HOC: (key, kernel, commit, the branch it stands on at the close)
KERNEL_COMMITS = (('rename', 'SIDE-explicit-formula', 'd1afb4fc', 'main'),             # ### (R368)(4): the one commit of push-b758-land, on main at v0.39
                  ('merge', 'SIDE-explicit-formula', '630cba16', 'main'))   # ### (R368)(5): the merge of 596d1c9e, made on push-b758-coeff, on main at v0.40 (04:37:50Z)
KERNEL_COMMITS_B757 = ()   # ### b757's sixteen stand in git at tools/b757_worklist.py
M24_DIR = 'D:/SIDE-dirichlet-mod-24'
M24_BASE = '597b0869'                 # ### SIDE-dirichlet-mod-24's main entering the act, its one commit
M24_MAIN = 'e5ebdd15'                 # ### b758: its remote main, unmoved; its local main fast-forwarded to it by (6)(i)'s route (01:59:39Z, events (38))
M24_TAG = ('v0.2.0', 'e5c84316', 'e5ebdd15')   # ### (R367)(6): name, tag object, peel read back at the remote (data/b757_SIDE-dirichlet-mod-24_push-b757-mod24_push_out.txt)
# ### b758 step zero: the carry shifted b757's two kernel branch names to push-b758-* here and in KERNEL_COMMITS above; set back to the names
# ### the remote holds (ls-remote 23:4xZ: push-b757-coeff 596d1c9e, push-b757-join 6568e9c7). KERNEL_COMMITS stays b757's until Components 2-3 write b758's.
COEFF_BRANCH = ('push-b757-coeff', '596d1c9e')   # ### b757's T0, T1 and the wide direction; (R368)(5) merges its tip --no-ff into push-b758-coeff
JOIN_BRANCH = ('push-b757-join', '6568e9c7')     # ### b757's join; (R368)(4) makes push-b758-land at its tip
LAND_BRANCH = ('push-b758-land', 'd1afb4fc2b34f5e62951947208461995d891c80c')   # ### (R368)(4): made at JOIN_BRANCH's tip (01:30:21Z); its one commit, the rename (01:32:10Z, events (36))
COEFF_LAND_BRANCH = ('push-b758-coeff', '630cba16e228a018f9dd986196142fc6feb704ec')   # ### (R368)(5): made at main d1afb4fc after (4)'s success (02:57:11Z); the merge of 596d1c9e (02:58:47Z, events (48))
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
C3_PUTS = (('defect (c)', 'data/b758_put_1.json', '77ae83fe'), ('N5`s folder clause', 'data/b758_put_2.json', 'cb14bae1'))   # ### (subject, the put bank, the commit carrying it)
C3_SITTING_TOOL = ()
C3_SITTING_BANK = ()
SITTING_COMMIT = None
SITTING_BANK = None
ITEM_PP = ()   # ### no passed item's PLACE-papers write this act
SITTING_PP = ()
SITTING_GH = ()
SITTING_SETTINGS = ()
SITTING_ITEMS = None          # ### no sitting this act ((R368)); one question at the root ((R368)(10))
SITTING_STATES = {}
HANDOFF_COMMIT = None         # ### (R368)(10): HANDOFF.md written once by tools/standing/handoff.py before the gate; set when made (b757's c37cdb05 carried until Component 5)
C3_RELAY = ('4905d3e3', 'ac6def8e', '6490bf35', 'cfca142a')   # ### Component 3 ((R368)(5)): dispatch 2's read, its step row, the landing at v0.40, the deletes carried (events (52))
C3_NOTES_GEN = 'a90f680a'   # ### b758 (R368)(8): tools/b758_notes.py as last committed before its writes of (b) to (e), controls 24 of 24, defect (c); (a) written under 5559a08b (events (44), (53))
C3_NOTES_PP = (('(a)', 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md', 'babcc8ea'),
               ('(b)', 'FACES_LEDGER.md', 'fbfec0f5'),
               ('(c)', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md', '7f96a8c6'),
               ('(d)', 'REGISTRY.md', 'a3fad736'),
               ('(e)', 'OPEN_TRAILS.md', 'cd42d8e9'))   # ### (item, the file, the PLACE-papers commit), steps 51 and 53-56, each confirmed at HEAD by tools/b758_notes.py (data/b758_notes.json, relay 5615a84f)
C3_NOTES_WRITTEN = 5   # ### the notes of (8): five writes, one PLACE-papers commit each (data/b758_notes.json)
# ### Component 4 ((R366)(5)): the put and the work its answers order, each value read from the step rows (data/b756_steps.json)
C4_READ = ('tools/b758_orders.py', '5b3d5a60', ('data/b758_orders_read.txt', 'data/b758_instruments_draft.txt'), 'f56557dd')   # ### the orders read and the two drafts
C4_PUT = ('data/b758_put_1.json', '0803754c')   # ### the one put, three questions, and the answers pair by its route, all three passed as recommended (step 22)
C4_PASSED_GEN = '9aa5fe8c'   # ### tools/b756_passed.py committed before its run, with events (21) (step 23)
C4_PASSED_PP = (('cp', 'OPEN_TRAILS.md', 'e50a394b'), ('instruments', 'phase1.5/method/INSTRUMENTS.md', '3b45826d'))   # ### steps 24, 25, each confirmed at HEAD (data/b756_passed.json)
C4_HERE = ('v1.34.8', '5b7aa91e', 'data/b758_standing_v1348.txt')   # ### W-ORD-LABEL-READER's predicate and control, controls 11 of 11 (step 26)
C4_MOVES = ('tools/b758_moves.py', '208eee6a', 'data/b758_orders_moves.txt', 'a26f30b9')   # ### the twelve status lines for this act's trail, controls 12 of 12 (steps 27, 28)
C4_CEILING = ('tools/b758_ceiling.py', 'a26f30b9', 'data/b758_ceiling_c4.txt')   # ### the ceiling after Component 4: 17.53 h against 24 h, nothing carried
C4_ORDERS = (1, 1, 5, 5)   # ### the orders: done, here, with the build, later (data/b756_orders_read.txt :87; data/b756_orders_moves.txt)
C4_CP = 'passed'           # ### CP-6 and CP-7 (data/b756_author_answers.txt :18; OPEN_TRAILS at e50a394b)
C4_LINE_GEN = None   # ### b755: no line bank; the entry's INTEGRATION line is (R365)'s, composed from the banks by the record module
C4_LINE = None       # ### Component 5: the act's INTEGRATION line
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
LV_ROWS = 'data/b758_lv_rows.json'
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
MAX_DISPATCHES = 4         # ### (R368)(10), ferry :27: "At most 4 dispatches" (N1); set at step zero, before Component 2's first dispatch
MAX_DISPATCHES_M24 = 0     # ### (R368)(10): no kernel touched beyond SIDE-explicit-formula's tree and the two local mains of (6)(i): no dispatch there
MAX_DISPATCHES_B757 = (14, 4)   # ### b757's caps, (R367)(10)
MAX_DISPATCHES_B756 = 0    # ### b756's: no runner dispatch
MAX_C2, MAX_KEIPER = 0, 0
EF_DIR = 'D:/SIDE-explicit-formula'
EF_BASE = '8fbab45d8a966dca53d42448e33927d885fd4ea3'   # ### SIDE-explicit-formula's main entering the act (b743's [A4], README alone)
EF_MAIN_AFTER = EF_MAIN   # ### b758: moved by (4) and (5) alone, each after its run's success ((R368)(4), (5))
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
EF_RUNS = (43997787796, 44007490629)   # ### N1: this act's SIDE-explicit-formula runs, each read by its run id, set as each is read ((R368)(4), (5): at most 4): (4)'s, read 02:53:56Z (events (47)); (5)'s, completed 04:34:40Z, read 04:35:49Z
M24_RUNS = ()   # ### N1: no SIDE-dirichlet-mod-24 dispatch this act ((R368)(6)(i) moves its local main alone)
EF_RUNS_B757 = (43818699881, 43834018078, 43835333285, 43836818700, 43839463729, 43841545568)   # ### b757's six, read not re-run (tools/b757_controls.py): the join KERNEL (the print failed at the import), T0 KERNEL (print stopped at maxErrors), T0 KERNEL (10 names), T1 BREAKS (recursion depth), T1 KERNEL (31 names), the wide direction KERNEL (24 names)
M24_RUNS_B757 = (43835913340, 43836415096)   # ### b757's two SIDE-dirichlet-mod-24 runs, read not re-run: the workflow's control KERNEL (2 names), the module KERNEL (8 names)
EF_RUNS_B745 = (42388001562, 42388609600, 42391254295, 42392017104, 42393018408, 42393914259)   # ### N1: this act's dispatches, each read by its run id ((R364)(4)(c)): KERNEL (print stopped at maxErrors), KERNEL (13 names printed), BREAKS (lp_conj), KERNEL (SPZ1), KERNEL (SPZ2), KERNEL (SPZ3)
EF_RUNS_B742 = (42054839204, 42056405331, 42058361986, 42061332755, 42062848400, 42065597154, 42068096322)   # ### b753's seven, read not re-run; the last the SP4 grade run
EF_RUNS_B741 = (41931918742, 41935365948, 41936644993, 41938300160, 41939524029, 41940815524)   # ### b753's six: KERNEL (timing), BREAKS, KERNEL, BREAKS, BREAKS, KERNEL (SP3)
EF_RUNS_B740 = (41854903335, 41857376723, 41859346843)   # ### b753's three: BREAKS, BREAKS, KERNEL, read not re-run
EF_RUNS_B738 = (41732413170, 41732882564, 41733411736, 41734667160, 41735082430, 41736472780)   # ### b738's first six (of eleven), read not re-run
ZQ_RUN = 41483457057   # ### b737's grade run, the discharge's, read not re-run
EF_RUNS_B731 = (41371666217, 41372597450, 41373409167, 41374121055, 41374814817)   # ### b731's five, read not re-run
DISPATCH_ROWS = 'data/b758_dispatch_rows.json'
ERRATA_ID = None   # ### no erratum this act
ERRATA_IDS = ()   # ### no erratum this act
RETIRED_COUNT = 0
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list (the root answer's addition (b))
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b758_') and f.endswith('.py') and f != 'b758_report.py')) + NEW_TOOLS + COMPUTE_TOOLS + REPAIRED_TOOLS
# ### the act's arms over its own banks: set before the lock by the Edit tool -- b753's list, the act shift G-R363-ENTERED to G-R364-ENTERED,
# ### G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0 ((R364)(2)(iv))
ACT_ARMS = ('G-ACT-CURRENT', 'G-ARM-TAGS', 'G-ARMS-RETIRED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED', 'G-CLOSING-DRY-STEP', 'G-COEFFS-LAW',
            'G-CORRIGENDUM-ENTERED', 'G-COUNT-ROUTE-PRICED', 'G-DELETES-ONE-BRANCH', 'G-DERIVATION-GRADED', 'G-DIFFERS-ERRATA', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-GUARD-HELD', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LISTINGS-BEFORE-CLAUSES',
            'G-MEMBRANE-WIRED', 'G-OFFSET-POST-HOC', 'G-POSTROOT-WRITES-NONE', 'G-PREDICTION-FIRST', 'G-R368-ENTERED',
            'G-REGISTRATIONS-FIRST', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED', 'G-SURGERY-CARRIED', 'G-TOUCH-READ',
            'G-WRITELIST-MIRROR-STATE')

# ### b754 writes no kernel ((R364)(5)): no main touched, no branch made on a kernel
SITTING_TIPS = {}
SITTING_BASE = EF_BASE
SITTING_REPOS = tuple(sorted(SITTING_TIPS))
SITTING_BRANCH = None
SITTING_BANK = 'data/b758_sitting.txt'   # ### the record of the sitting, one row per item
KERNEL_BASES = 'data/b758_kernel_bases.json'
