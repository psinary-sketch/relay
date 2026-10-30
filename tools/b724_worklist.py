# -*- coding: utf-8 -*-
"""b724_worklist.py -- THE ACT'S DATA, UNDER (R334). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b724: LANE TWO, ACT ONE HUNDRED AND FIFTY-ONE, THE SECOND CHECKPOINT ACT -- b723 AT ITS WEIGHT; THE TEN REPEAT CLASSES AND THE
### ROOT ROUTE REPAIRED; THE LEDGER SPLIT, STOPPABLE; THE OPEN ORDERS TRIAGED; THE lv NEGATION AND ITS ERRATUM; THE LEGACY IMPORTS. The
### runner dispatch is (R334)(5)'s one alone (N1).
### Carried by diff from b723_worklist.py (data/b724_carry_worklist.txt); its stage one set by the Edit tool at step zero with this act's
### figures (the carried text named b723's objects under b724's names); later stages by the Edit tool.
### The act runs in the SAME session as b723 (02c7cf38; the ruling pasted after b723's closing push): the previous act's window is this
### session cut at b723's anchor, b706's same-session form. b723 closed and pushed itself whole (relay b8334f17, PLACE-papers 698fe441, both
### read back); its closing capture and step-54 row are this act's carried files ((R334)(8)), each committed alone at step zero.
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
PRE_PP = '698fe4418e4f2b9d2601b363798011681b5b0153'    # ### PLACE-papers main before the act's own commits: b723's record, pushed and read back by b723
PRE_RELAY = 'b8334f172a2913635e22ddaf6fc97b41d40ea745'  # ### relay main before the act's own commits: b723's closing, pushed and read back by b723
PRE_PP_REMOTE_AT_START = '698fe441'      # ### PLACE-papers remote main at the act's start (data/act_current.json, equal to local)
PRE_RELAY_REMOTE_AT_START = 'b8334f17'   # ### relay remote main at the act's start (the citation check's remote main row)
B718_RELAY_HEAD = 'b8334f1'  # ### the names kept for the carried readers: the previous act's last relay head (b723's closing)
B718_PP_HEAD = '698fe44'     # ### the previous act's last PLACE-papers head (b723's record)
DATE = '2026-10-29'
SESSION_ID = '02c7cf38-4c6a-4f88-b813-a7e15e9b85b4'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R334) BEGIN'           # ### the act's capture anchor, as data/act_current.json
RULING_ANCHOR = 'RULING (R334) BEGIN'    # ### the ruling's BEGIN line, the citation tool's ferry source
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = SESSION_ID   # ### b723 ran in this session (from 'RULING (R333) BEGIN', with compactions); b706's same-session form
PREV_ANCHOR = 'RULING (R333) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b724_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 11490          # ### FINDINGS: b723's entry head (PLACE-papers 698fe441)
B711_WEIGHT = 11399         # ### FINDINGS: b722's weight line (b723's Component 1)
B711_CORRIGENDUM = 11401    # ### FINDINGS: b723's corrigendum for b722
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 16366          # ### OPEN_TRAILS: b723's trail record (PLACE-papers 698fe441)
B711_FACE = 'data/b723_registration_2026-10-29.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-29-b723.zip'   # ### b723's export, built after b723's last PLACE-papers push, CLEAN 3/3
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
ORDER_LEDGER_SPLIT = 14680  # ### OPEN_TRAILS: W-ORD-LEDGER-SPLIT-RESOLVER (b680), (R334)(3)
TRAIL_ORDERS = 16372        # ### OPEN_TRAILS: the last open-orders line, b723's, written from the generator's output
TRAIL_RESOLVED = 16406      # ### OPEN_TRAILS: b723's items for the author's strike, in its trail (landed at 698fe441)
TRAIL_RETIRED = 16418       # ### OPEN_TRAILS: W-ORD-STATUS-CELLS RETIRED, open orders 143 before, 142 after
WATCH_LINE = 16126          # ### OPEN_TRAILS: W-ORD-QUASI-RH-FIELD-WATCH, annotated at b718's C6
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row
INSTRUMENTS = 'phase1.5/method/INSTRUMENTS.md'   # ### PLACE-papers' instruments document, its last entry I-108 (b723)
INSTRUMENTS_LAST = 108

# ### the branches step zero deletes ((R334)(9)): the push-b723-* branches b723's close made, by name, each read from the listings and
# ### `--merged` printed before the deletes, one per command, each its own message
DELETE = (('D:/relay', ('push-b723-closing', 'push-b723-preroot', 'push-b723-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b723-preroot', 'push-b723-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R334)(9): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'), ('D:/SIDE-explicit-formula', 'challenge-b720-h2-sign-iff-rh'),
                 ('D:/SIDE-kernel', 'rebuild-b721'), ('D:/SIDE-lv-conservation', 'rebuild-b721'), ('D:/SIDE-archimedean', 'rebuild-b721'),
                 ('D:/SIDE-frobenius', 'rebuild-b721'), ('D:/SIDE-spinor', 'rebuild-b721'), ('D:/SIDE-rcurve', 'rebuild-b721'))

# ### the kernels: read; written only on the rebuild-b721 branches by (R334)(7) and the author's word (4)
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')


def _kernel_paths():
    """the kernels of data/b716_federation_pin_price.txt (1), as D:/<name>, read at import ((R334) PATHS)."""
    p = os.path.join(D, 'b716_federation_pin_price.txt')
    t = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return tuple('D:/' + m.group(1) for m in re.finditer(r'(?m)^  (SIDE-[A-Za-z0-9-]+)\s+HEAD ', t))


KERNEL_PATHS = _kernel_paths()
PATHS = ('D:/relay', PP, KERNEL_DIR, LV_DIR) + tuple(k for k in KERNEL_PATHS if k not in (KERNEL_DIR, LV_DIR))   # ### (R334)'s PATHS
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
# ### the wave 1 kernels at their own pins, (name, tag, the short commit) -- b721's (R331)(7), b723's (R333)(10)
WAVE1 = (('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-archimedean', 'v0.1.0', '8019d9d'),
         ('SIDE-frobenius', 'v0.1.0', '2efe9f2'), ('SIDE-spinor', 'v0.1.0', 'b235bc6'), ('SIDE-rcurve', 'v0.1.0', 'd5f33b4'))
CHECKPOINT_STATEMENTS = (('SIDE-archimedean', 'archimedean_forces_half'), ('SIDE-frobenius', 'indicial_forces_half'),
                         ('SIDE-spinor', 'spinor_forces_half'), ('SIDE-spinor', 'half_iff_centered_zero'), ('SIDE-rcurve', 'monotone_unique_zero'))
REBUILD_BRANCH = 'rebuild-b721'          # ### b721's branches, kept, (R334)(7)'s repair made on them alone
REBUILD_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-lv-conservation', 40706311269), ('SIDE-archimedean', 40706397470),
                ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404), ('SIDE-frobenius', 40713201832))   # ### b721's, each read by its id
AXIOM_RUNS = (('SIDE-kernel', 40706230156), ('SIDE-archimedean', 40706397470), ('SIDE-frobenius', 40713201832),
              ('SIDE-spinor', 40706542282), ('SIDE-rcurve', 40706645404))   # ### b723's (R333)(10): the five whose axiom step was diagnosed
AXIOM_DIAG = 'data/b723_axiom_diag.txt'  # ### the routes (R334)(7) and the author's word (4) take
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
DATA_STANDING = 'data/standing_clauses_v9.txt'   # ### v8 bound the act to d9739558; v9 from that commit, which landed it at Component 1 ((R334)(2)(v))
DATA_STANDING_V9 = 'data/standing_clauses_v9.txt'
ARM_TAGS = 'data/arm_tags.json'
REPO_VISIBILITY = 'data/repo_visibility.txt'
REGISTRATIONS = 'data/b724_registrations.txt'    # ### (R334)(4): written and committed alone at Component 3, before any figure it names
REG_WALK_COMMIT = '15cb6cc4'                     # ### b721's H-C2-WALK commit (carried name; b723's walk read under it)
REG_COMMITS = (('data/b716_registrations.txt', 'dc5e808f'), ('data/b718_registrations.txt', '8146404b577dfee3e379d19e08e8595ab8824961'),
               ('data/b719_registrations.txt', '965cb8e84dc02192854512af53a29b1fbc2b80f5'), ('data/b720_registrations.txt', '54fc03d9'),
               ('data/b721_registrations.txt', 'e8c3dff40df43269b3f0c4b917baef7c96c0f649'))   # ### N2 (b724's row added at Component 3)
REG_FILES = tuple(f for f, _c in REG_COMMITS)
PRED_B717 = 'data/b717_predictions.txt'
PRED_B717_COMMIT = 'f47d8ab5840d287bf63c1f0b59ba707ed85dbe07'
PREDICTIONS = PRED_B717
ONSETS_B717 = 'data/b717_onsets.txt'
REGISTRATIONS_NEW = 'data/b724_registrations.txt'
COEFF_BANKS = ('data/b711_coeffs.txt', 'data/b713_coeffs.txt', 'data/b717_coeffs.txt', 'data/b719_coeffs.txt', 'data/b720_coeffs.txt')
#   ### read not written (carried name); b723 wrote no coefficient bank
COMPUTE_BANKS = ('data/b724_price.txt', 'data/b724_standing_v140.txt', 'data/b724_root_corrigendum.txt', 'data/b724_split_price.txt',
                 'data/b724_orders_triage.txt', 'data/b724_lv.txt', 'data/b724_lv_rows.json', 'data/b724_release_list.txt', 'data/b724_legacy.txt')
#   ### the banks of (R334)(2)-(6), each written by its component (the price table at step zero)
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt',
              'data/b723_read_calls.txt', 'data/b724_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b723 carried them
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b724'))
CHAIN_QUARTERS = (('b624', 'b631'), ('b632', 'b658'))   # ### (R334)(2)(vi): b2a split where b723's banked walks halve (repeat.quarters; b2a's run 575 s at b723)
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### set by the Edit tool when a component adds a standing arm
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_WRITTEN = ('ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md')   # ### the weight line, the corrigendum, the entry and the trail; (R334)(5)'s ERRATA entry; no archive file ((3) carried)
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'   # ### the re-cut's merge (kept for the kernel rows); the MANIFEST control's reference
#   ### is the commit the mirror is built at from v1.2.1
NEXT = ('b725 ((R334)(10)), the research act: H-ONSET-MASS registered (the onset at a zero predicted from the on-line mass the template '
        'window sees, read from the certified list, in the refined Li law’s form) and tested on zeros not yet computed; H-DIAL at c = 0.6, 0.8 '
        'and 1.0; lambda_2 > 0 by the fourth Keiper obligation at index 1 and a gamma_1 bound; the C2 compile by the certificate route on a '
        'branch of SIDE-explicit-formula. Then b726, the wave 1 act')
NEXT_ACT = 'b725'


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
STANDING_DIR = 'tools/standing'         # ### the standing close toolset, versioned by tools/standing/VERSION, at v1.3.0 entering this act
STANDING_COMMIT = 'd973955897'          # ### standing clauses v9 (b723's Component 1), binding this act whole (carried name)
ACT_CURRENT_COMMIT = '0b81b3dd'         # ### data/act_current.json for b724 committed alone, before any other command ((R334)(8))
STEPZERO = '9e3f4e39'                   # ### b723's closing capture, committed alone ((R334)(8))
STEPZERO_STEPS = '6b1eedb6'             # ### b723's step-54 row, committed with data/b723_bank_hashes.json beside it (the citation check's miss)
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None
STEPZERO_REFUSALS = ()
STEPZERO_BANKS = '21681ef9'             # ### the step-zero banks and tools, committed together by explicit list
STEPZERO_BANK_COMMIT = 'd5432f23'       # ### the step-zero bank itself (data/b724_stepzero.txt), with the price table, after the banks' commit
VISIBILITY_COMMIT = None
COMPUTE_TOOLS = ()                      # ### set by the Edit tool when a component seals a compute tool
REPAIRED_TOOLS = ()
REPAIRED_DATA = ()
# ### b721's trap (event 11): the standing part of the sealed list read from the directory, not a carried tuple
STANDING_FILES = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing')) if f == 'VERSION' or f.endswith('.py')))
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset, sealed by hash beside the act's tools
# ### the seven close tools are tools/standing/fold.py's renders of its templates (tools/standing/fold/<tool>.tpl) with the act's arms module
# ### (tools/acts/b724.py) -- every byte a render reads sealed beside the act's tools; report.tpl left out of the seal (b708's report row)
FOLD_FILES = tuple(sorted('standing/fold/' + f for f in os.listdir(os.path.join(ROOT, 'tools', 'standing', 'fold')) if f.endswith('.tpl')
                          and f != 'report.tpl')) + ('acts/b724.py',)
NEW_TOOLS = NEW_TOOLS + FOLD_FILES
STANDING_VERSION = 'v1.4.0'             # ### (R334)(2), landed by a commit of its own at Component 1 (v1.3.0 entering the act)
STANDING_CHANGED = ('standing/VERSION', 'standing/fold/checks.tpl', 'standing/fold/record.tpl', 'standing/fold/reg_gate.tpl',
                    'standing/fold/regspec.tpl', 'standing/hook.py', 'standing/peek.py')   # ### the standing files (R334)(2) changes
STANDING_NEW = ('standing/carry.py', 'standing/repeat.py', 'standing/v140.py')
# ### b723's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = 'b8334f17'    # ### b723's closing, the act's relay base
B714_RECORD = '14bf5ec5'     # ### b723's record commit (relay, the head line's)
B714_ROOT = '9296406733ce0d44e197b8110ae942efb9f6fa121f7416214560282cbf42d553'   # ### b723's root, data/act_roots.txt :101, carried as recorded
B723_ROOT_BANKS = 'f585420f'  # ### b723's root banks' commit, the root route's control replays b723's banks there ((R334)(2))
# ### later stages: the commits of the components, read from the logs after each was made (None until made)
C1_STANDING = '6938625834306c5e83709956b541332cd9f2c026'   # ### tools/standing/ v1.4.0, by a commit of its own (Component 1, step 6)
C1_RELAY = 'e5f9f7a50390c66ede87f9e8ebc72a58d01909ce'      # ### v1.4.0's controls bank, the root corrigendum row and bank, the defects bank (step 7)
C1_CORR = 'a5a7144213ee8d4815608014a4501651ddff1e74'       # ### the corrigendum banks and the b675 corrigenda row (44) (step 9)
C1_PP = '88f234edbc2585d6ddd68f23f47931d1a50aa8b3'         # ### FINDINGS: b723's weight line and the corrigendum (step 8)
WEIGHT_LINE, CORR_LINE = 11534, 11536   # ### FINDINGS: b723's weight line and the corrigendum for b723 (Component 1)
DIFFERS_LINE = None
ERRATA_LINE = None                      # ### ERRATA.md: read by its id (ERRATA_ID), not by a line
C2_RELAY = 'b34fb50ee74bc438f0d066eaeeb00195a3a30bde'      # ### (R334)(3): the ledger split carried whole with its price (step 10)
C2_PP = None                            # ### nothing of (3) landed (N3)
C3_RELAY = '688c9e99dc7e0a6655f3bcc0500dfb331cf1ff3f'      # ### (R334)(4): the triage bank (step 11)
C3_PP = None                            # ### the DONE orders' dated closing lines written with the trail at the close
C4_LV = 'c9cd1ea90e1367fb6ba4d55e4d3538a0179b69a3'         # ### the lv negation's commit on its scratch branch (Component 4)
C4_RUN = 40964150574                    # ### its one dispatch, read by its run id
C4_PP = 'c3c6ba8657516d671b1ce9d21baaecf2deb286c9'         # ### ERRATA.md: E-2026-10-29-1 (step 12)
C4_RELAY = 'bb304a67ee996928fe25da1e1e808c073fb51228'      # ### the lv bank, its rows and the release sitting's list (step 13)
C5_RELAY = '01dd9f44492034c649b5fcbfeef0f220caa923aa'      # ### (R334)(6): the legacy imports carried with the remaining price (step 14)
REG_COMMIT = None                       # ### (R334)(10): the act registers no hypothesis
ORDERS = (142, 60, 42, 12, 28)          # ### (R334)(4): the open orders triaged (data/b724_orders_triage.txt :531): DONE, NOT MET, MET, AUTHOR'S WORD
TRIAGE = 'data/b724_orders_triage.txt'
LV_SCRATCH_BRANCH = 'scratch-b724'      # ### (R334)(5)'s scratch branch of SIDE-lv-conservation, at C4_LV over the deposit pin
LV_RUNS = (('SIDE-lv-conservation', 40964150574),)   # ### N1: (R334)(5)'s one dispatch, read by its id
LV_ROWS = 'data/b724_lv_rows.json'
CHALLENGE_BRANCH = 'challenge-b720-h2-sign-iff-rh'   # ### b720's, on SIDE-explicit-formula, standing, not merged, no tag
CHALLENGE_TIP = '3391647518cd37316a448b5013afb62a198fa6c6'
CHALLENGE_RUN = 40651875792
PIN_RUNS = (('SIDE-grh-transfer', 40652622018), ('SIDE-interfaces', 40652657325), ('SIDE-kernel', 40652692787),
            ('SIDE-lv-conservation', 40652727943), ('SIDE-simplicity', 40652762827), ('SIDE-trivium', 40652790458))   # ### b720's, read not re-run
PIN_BRANCH = 'pin-b718-de5ce8a9'   # ### b718's pin branches, left as banked ((R334)(8))
PIN_EXCLUDED = ('SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve', 'SIDE-cosmo')
PIN_HELD = ('SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium')
PIN_BUILDS = ('SIDE-simplicity',)
PIN_CARRIED = ('SIDE-archimedean', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-rcurve',
               'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PIN_TO_NEXT = ()
MAX_DISPATCHES = 1           # ### N1: (R334)(5)'s one
PP_EDITED = ('ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md')   # ### (R334)(5)'s ERRATA entry beside the two ledgers
ERRATA_ID = 'E-2026-10-29-1'
ERRATA_IDS = ('E-2026-10-29-1',)
RETIRED_COUNT = 0
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list (the root answer's addition (b))
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b724_') and f.endswith('.py') and f != 'b724_report.py')) + NEW_TOOLS + COMPUTE_TOOLS
# ### the act's arms over its own banks: set before the lock by the Edit tool -- b723's list, the act shift G-R333-ENTERED to G-R334-ENTERED,
# ### G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0 ((R334)(2)(iv))
ACT_ARMS = ('G-ACT-CURRENT', 'G-ARM-TAGS', 'G-ARMS-RETIRED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED', 'G-CLOSING-DRY-STEP', 'G-COEFFS-LAW',
            'G-CORRIGENDUM-ENTERED', 'G-COUNT-ROUTE-PRICED', 'G-DELETES-ONE-BRANCH', 'G-DERIVATION-GRADED', 'G-DIFFERS-ERRATA', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-GUARD-HELD', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LISTINGS-BEFORE-CLAUSES',
            'G-MEMBRANE-WIRED', 'G-OFFSET-POST-HOC', 'G-POSTROOT-WRITES-NONE', 'G-PREDICTION-FIRST', 'G-R334-ENTERED',
            'G-REGISTRATIONS-FIRST', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED', 'G-SURGERY-CARRIED', 'G-TOUCH-READ',
            'G-WRITELIST-MIRROR-STATE')
