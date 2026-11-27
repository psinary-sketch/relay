# -*- coding: utf-8 -*-
"""b770_worklist.py -- THE ACT'S DATA, UNDER (R380). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b770: LANE TWO, ACT ONE HUNDRED AND NINETY-SEVEN, THE LEAN ACT, FOUR STATEMENTS ON THE COMPILED CONTROL AND THE CRITERION --
### b769 AT ITS WEIGHT; THREE KEYS; THE PLAN; A ZERO OFF THE LINE FROM THE COEFFICIENTS; POSITIVITY BY SUPPORT; THE COMPOSITION; THE
### LEAST NEGATIVE COEFFICIENT; THE CLOSING BUILD FROM SOURCE; THE TWO INDEX BANKS READ; THE SITTING OF THE TENTH ACT; THE AUTHOR'S
### RULINGS ENTERED. The dispatches of (4) alone, at most 40, to SIDE-explicit-formula (N1); nothing deposits, no kernel but
### SIDE-explicit-formula touched, no tag cut beyond v0.47 under (4) (N5); nothing fetched from the web.
### Carried by diff from b769_worklist.py (data/b770_carry_worklist.txt); its stage one set at step zero with this act's figures by the
### seat's script (scratch wl770.py, each constant replaced whole by its name); later stages by the Edit tool.
### (R380) was delivered in one part in session 11d67961 (b769's session): the ruling, its texts and its ferry at transcript line
### 421326 (2026-11-26T20:26:40Z); the act runs in it, one seat, with no change of session, harness or store (the step-zero reads of
### 2026-11-26T20:29:53Z-20:30:28Z).
### b769 closed (relay 376e35db, PLACE-papers 78685602); the files it left ((R380)(3)) committed at step zero.
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
PRE_PP = '78685602e75a4cfe89a2abd0cdea9188a03c6408'    # ### PLACE-papers main before the act's own commits: b769's record (the trail), pushed
PRE_RELAY = '376e35db720b27c5b3cf1e2fe5536b59c2bdcd51'  # ### relay main before the act's own commits: b769's closing step row, pushed
PRE_PP_REMOTE_AT_START = '7868560'       # ### PLACE-papers origin/main at the act's start, read from the tracking ref (no remote read at step zero), equal to local
PRE_RELAY_REMOTE_AT_START = '376e35db'   # ### relay origin/main at the act's start, read from the tracking ref, equal to local
B718_RELAY_HEAD = '376e35d'  # ### the names kept for the carried readers: the previous act's last relay head (b769's closing step row)
B718_PP_HEAD = '7868560'     # ### the previous act's last PLACE-papers head (b769's record)
DATE = '2026-11-26'
SESSION_ID = '11d67961-2aa4-4353-bc12-a982038bfa55'   # ### the transcript the ruling and the ferry stand in (one part: the ruling, its texts and its ferry at line 421326, 2026-11-26T20:26:40Z), b769's session; the act runs in it, one seat, no change of session, harness or store
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/0fa2f3b7e932577a/11d67961-2aa4-4353-bc12-a982038bfa55/scratchpad'   # ### the seat's scratchpad as the harness names it (session 11d67961, the act's own)
HOLD = 2560
ANCHOR = 'RULING (R380) BEGIN'           # ### the act's capture anchor, as data/act_current.json
RULING_ANCHOR = 'RULING (R380) BEGIN'    # ### the ruling's BEGIN line, the citation tool's ferry source
TAIL = 'FERRY END'   # ### b770: (R380) in one part; the ruling's texts after clause (13) and before the ferry (data/b770_ferry.txt), set at stage one (scratch wl770.py)
SESSIONS_AFTER = ()   # ### none: the act runs in the session its ruling was delivered in (b671's form not needed)
PREV_SESSION = '11d67961-2aa4-4353-bc12-a982038bfa55'   # ### b769 ran in this session from its delivery (2026-11-25T17:31:20Z) to its closing push (after its step row 376e35db, 2026-11-26T19:13:27Z); (R380) was delivered in it after that close
PREV_ANCHOR = 'RULING (R379) BEGIN'   # ### the first user row of 11d67961 holding b769's ruling's first line (2026-11-25T17:31:20Z), before b769's post-push combine (before its closing commit 63af44b1, 2026-11-26T19:12:30Z); G-EDIT-ROUTE's window from that combine to (R380)'s anchor
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b770_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 16259          # ### FINDINGS: b769's entry head (at 054e1f6, unmoved at 7868560)
B711_WEIGHT = None          # ### FINDINGS: b769 wrote no weight line of its own; b768 at its weight stands in b769's entry (:16265)
B711_CORRIGENDUM = 16247    # ### FINDINGS: b769's corrigendum for b768
B718_CLASSES = 10847        # ### FINDINGS: b718's CLOSE classes line (carried name, unmoved)
B711_TRAIL = 19527          # ### OPEN_TRAILS: b769's trail record (PLACE-papers 7868560)
B711_FACE = 'data/b769_registration_2026-11-25.txt'   # ### b769's face
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-11-25-b769.zip'   # ### b769's export (step [23], CLEAN), the previous act's mirror zip, read not written; its folder as b769's value held it
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707)
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it
ORDER_LEDGER_SPLIT = 14680  # ### OPEN_TRAILS: W-ORD-LEDGER-SPLIT-RESOLVER (b680), (R364)(3)
TRAIL_ORDERS = 19559        # ### OPEN_TRAILS: the last open-orders line, b769's, written from the generator's output
TRAIL_RESOLVED = 19585      # ### OPEN_TRAILS: b769's items for the author's strike, in its trail
TRAIL_RETIRED = 19571       # ### OPEN_TRAILS: b769's count line of the author's prompts
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
DELETE = (('D:/relay', ('push-b769-closing', 'push-b769-preroot', 'push-b769-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b769-preroot', 'push-b769-record')))
DELETE_TIPS = {('D:/relay', 'push-b769-closing'): '376e35db', ('D:/relay', 'push-b769-preroot'): '0c1b0d1d', ('D:/relay', 'push-b769-record'): '8737fa91',
               (PP, 'push-b769-preroot'): '054e1f6e', (PP, 'push-b769-record'): '78685602'}
#   ### b770 step zero: set from the --merged listing (scratch merged770.py, 20:44:22Z), each merged into main; the carry had shifted
#   ### b769's names onto b768's tips; PLACE-papers' keys by the worklist's PP
DELETE_TIPS_B769 = {('D:/relay', 'push-b768-closing'): '55166251', ('D:/relay', 'push-b768-preroot'): '757c75de', ('D:/relay', 'push-b768-record'): '3c9810fc',
               (PP, 'push-b768-preroot'): 'aa525973', (PP, 'push-b768-record'): 'e52e2bae'}
#   ### b769 step zero: set from the --merged listing (scratch merged769.py, 17:43:36Z), each merged into main; the carry had shifted
#   ### b768's names onto b767's tips; PLACE-papers' keys by the worklist's PP
DELETE_TIPS_B768 = {('D:/relay', 'push-b767-closing'): '048085dd', ('D:/relay', 'push-b767-preroot'): '702205dd', ('D:/relay', 'push-b767-record'): 'c8cf6966',
               (PP, 'push-b767-preroot'): '512034b2', (PP, 'push-b767-record'): 'a8be5811'}
#   ### b768 step zero: set from the --merged listing (scratch merged768.py, 13:00:03Z), each merged into main; the carry had shifted
#   ### b767's names onto b766's tips (`carry.py ruled b768 b767`, R1, 13:00:11Z); PLACE-papers' keys by the worklist's PP
DELETE_TIPS_B767 = {('D:/relay', 'push-b766-closing'): 'a0bc04cd', ('D:/relay', 'push-b766-preroot'): 'b95c2f2f', ('D:/relay', 'push-b766-record'): '603451cf',
               ('D:/MY-DOwnloads/PLACE-papers', 'push-b766-preroot'): '487e3095', ('D:/MY-DOwnloads/PLACE-papers', 'push-b766-record'): '29de0836'}
#   ### b767 step zero: set from the --merged listing (scratch merged767.py, 08:27:50Z), each merged into main; the carry had shifted
#   ### b766's names onto b765's tips (`carry.py ruled b767 b766`, R1, 08:27:59Z)
DELETE_TIPS_B766 = {('D:/relay', 'push-b765-closing'): '29d4c9b7', ('D:/relay', 'push-b765-preroot'): '35a3581d', ('D:/relay', 'push-b765-record'): 'a7bd1c51',
               ('D:/MY-DOwnloads/PLACE-papers', 'push-b765-preroot'): 'd2d8b00f', ('D:/MY-DOwnloads/PLACE-papers', 'push-b765-record'): '5638a9ad'}
#   ### b766 step zero: set from the --merged listing (scratch merged766.py, 07:00:57Z), each merged into main; the carry had shifted
#   ### b765's names onto b764's tips
DELETE_TIPS_B765 = {('D:/relay', 'push-b764-closing'): '306162ad', ('D:/relay', 'push-b764-preroot'): '08a551de', ('D:/relay', 'push-b764-record'): '828d0b7e',
                    ('D:/MY-DOwnloads/PLACE-papers', 'push-b764-preroot'): '35b75536', ('D:/MY-DOwnloads/PLACE-papers', 'push-b764-record'): '1198a637'}   # ### b765's five, kept beside (the carry's shift set back)
#   ### b765 step zero: set from the --merged listing (scratch merged765.py, 10:03:33Z-10:03:34Z), each merged into main; the carry had
#   ### shifted b764's names onto b763's tips
DELETE_TIPS_B764 = {('D:/relay', 'push-b763-closing'): '0f9b1df2', ('D:/relay', 'push-b763-preroot'): '109f5ba7', ('D:/relay', 'push-b763-record'): 'd4ec1edb',
                    ('D:/MY-DOwnloads/PLACE-papers', 'push-b763-preroot'): 'b3020098', ('D:/MY-DOwnloads/PLACE-papers', 'push-b763-record'): '7db9a66c'}   # ### b764's five, kept beside (the carry's shift set back)
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
EF_MAIN = 'ffefddc61b05fcca089ff20cc8cd2f103dd0a5f1'    # ### b768, Component 4 (the Edit tool, 03:1xZ): (R378)(4) -- the closing build from source at ffefddc6 (dispatch 14, the closing build`s one repeat, run 45521560784, route (i), the restore off) exited 0 and its axioms file equals by sha256 2a9e26774e7e0c96 the restored run 45514975816`s, THE PAIR AS WANTED; main moved from 89fd5b54 (EF_BASE) to ffefddc6 by the gated push`s default mode (03:10:3xZ, read back at the remote), v0.46 made at the read-back; the local main fast-forwarded by the one-call tool (03:10:4xZ, read back EQUAL). Readers searched before this Edit (Grep with -o, 03:11Z): checks.tpl :1261 and record.tpl :2563, the act module`s regspec overrides :615 and :624, checks 34 :1274, checks 35 :1343-:1347, the record`s kernels line :2109 and the arm at :2641, each reading EF_MAIN equal to RUNNER_COMMIT as main moved; the dispatch and rulings tools none. b767's words: (R377)(4) --(R377)(4) -- the closing build from source at 89fd5b54 (dispatch 17, run 45236921224, route (i), the restore off) exited 0 and its axioms file equals by sha256 9c2cb7f7a216790c the restored run 45235741926's, THE PAIR AS WANTED; main moved from 0ba9cd61 (EF_BASE) to 89fd5b54 by the gated push`s default mode (20:19:4xZ, read back at the remote), v0.45 made at the read-back; the local main fast-forwarded by the one-call tool (20:20:3xZ, read back EQUAL). Readers searched before this Edit (Grep, 20:2xZ): checks.tpl :1261 and record.tpl :2563, the act module's sections, none reading it as the entering main. b766's words: main entering at 0ba9cd61, v0.44; (R376)(4) moves it to the closing Lean commit alone, and only where the two axioms files are equal. b765's words: b765 (R375)(4): H-RUNNER-RESTORE HELD (16:31:02Z), so main moved from 819e4a83 (EF_BASE) to the closing Lean commit 0ba9cd61 by the gated push`s default mode (16:35:3xZ, read back at the remote), v0.44 made at the read-back; the local main fast-forwarded by the one-call tool (16:35:4xZ, read back EQUAL). b764's words: main at the close unmoved at v0.43, the trial of (R374)(7) failing. b763's words: main at the close -- moved from push-b763-form at v0.42 (02:22:05Z, tag object 001e94ff) after run 44646848292's success, then from push-b763-squares at v0.43 (05:34Z, tag object bcd4d481) after run 44670834879's, (8)'s W-ORD-SQUARES-AT-24 built in full (entering at a3aad4cc, EF_BASE); the local main fast-forwarded by the one-call tool after each (05:34:3xZ the second)
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
SECTION_BANK = 'data/b769_ledgers_c4.txt'      # ### b769's last ledgers bank (the rulings tool's group c4), read not written
SECTION4_BANK = 'data/b748_section4.txt'              # ### b748's §4 bank, read not written
SECTION1_BANK = 'data/b747_section2.txt'              # ### b747's section bank (§2), read not written
INTEGRATION_DRAFT = 'data/b746_integration_draft.txt' # ### b746's canon text for the stages, entered at b753 as XXIII, read not written
ORDER_DRAFT = 'data/b746_order_draft.txt'             # ### (carried name) b746's order draft, read not written; no order entered this act
READBACK_747 = 'data/b747_zenodo_readback.txt'        # ### b747's read-back, read not written; no Zenodo call this act ((R364)(6))
RULES_747 = 'data/b770_rules.txt'                     # ### (R364)(3): the seat's reading of the corrigendum's repairs, each for the author's strike
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
COMPUTE_BANKS = ('data/b770_corrigendum.txt', 'data/b770_price.txt', 'data/b770_plan.txt', 'data/b770_address_scan.txt')
#   ### the banks of (R380)(1)-(13) as the ruling names them, each written by its component; the dispatches of (4) alone, at most 40;
#   ### set by the Edit tool to the banks as written, before the lock
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b718_read_calls.txt', 'data/b719_read_calls.txt', 'data/b720_read_calls.txt', 'data/b721_read_calls.txt',
              'data/b729_read_calls.txt', 'data/b730_read_calls.txt', 'data/b769_read_calls.txt', 'data/b770_read_calls.txt')

# ### THE SUITE'S PARTS: ten, as b753 split them under (R363)(2)(vi) and b675 rules row (2) (standing-a in two, G-NO-SORRY-MAIN's kernels
# ### halved, and the chain's first half in four, b2a-b2d); data/act_current.json committed them ten at b754's step zero (22f59d27), no
# ### component splitting them this act, so PARTS_AT_STEP_ZERO is PARTS
PARTS = ('standing-a1', 'standing-a2', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d', 'standing-b3', 'act')
PARTS_AT_STEP_ZERO = PARTS
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b770'))
CHAIN_QUARTERS = (('b624', 'b627'), ('b628', 'b631'), ('b632', 'b635'), ('b636', 'b658'))   # ### carried from b753
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### LEFT EMPTY BY (R380)(11): tools/standing/ moved under (8) alone, by the three commits 60e769a5, 75a8c747 and 9432d7ce changing VERSION and eight files more and adding hostmask.py, no arm name gained or lost (scratch armset770.py over 376e35db and HEAD, 2026-11-27T10:50:33Z: 106 quoted at each), so no standing arm added; b769's clause (R379)(11) set to b770's before the lock. b769's: by 48ccc5c7 and 84333f27, 106 at each (2026-11-26T00:18:35Z)
SHARED_APPENDED = ('data/b675_corrigenda.txt',)   # ### (R364)(2): the corrigenda row
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### the census at its current version (the touch read's source)
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
PP_EDITED = ('FINDINGS.md', 'OPEN_TRAILS.md')
#   ### b770 step zero: (R380)(13)'s (W) list in PLACE-papers -- FINDINGS.md and OPEN_TRAILS.md, each by its path at PLACE-papers
#   ### 78685602; REGISTRY, ERRATA, the census, the register and SPIRAL_MAP.md not written ((R380)(12), N3); no sentence of any paper
#   ### written or edited; no new file
#   ### b769 step zero: (R379)(13)'s (W) list in PLACE-papers -- FINDINGS.md, OPEN_TRAILS.md, REGISTRY.md (the block of (4)(a) and
#   ### the row of (4)(c)), ERRATA.md (the entries of (5)), SPIRAL_MAP.md (the merge of (4)(b)) and clusters/lean-archive-november-2026/
#   ### (the source record of (4)(d)), each by its path at PLACE-papers e52e2bae; SPIRAL_MAP_v0_7.md, the census and the register not
#   ### written ((R379)(12), N3); no sentence of any paper written or edited
#   ### b768 step zero: (R378)(13)'s (W) list in PLACE-papers -- FINDINGS.md and OPEN_TRAILS.md, each by its path at PLACE-papers
#   ### a8be5811; REGISTRY, ERRATA, the census, the register and the two files of the map not written ((R378)(12), N3); no sentence of
#   ### any paper written or edited; no new file
#   ### b767 step zero: (R377)(13)'s (W) list in PLACE-papers -- FINDINGS.md and OPEN_TRAILS.md, each by its path at PLACE-papers
#   ### 29de0836; REGISTRY, ERRATA, the census, the register and the two files of the map not written ((R377)(12), N3); no sentence of
#   ### any paper written or edited; no new file
#   ### b766 step zero: (R376)(12)'s (W) list in PLACE-papers -- FINDINGS.md and OPEN_TRAILS.md, each by its path at PLACE-papers
#   ### 5638a9ad; REGISTRY, ERRATA, the census, the register and the two files of the map not written ((R376)(11), N3); no sentence of any
#   ### paper written or edited; no new file
#   ### b765 step zero: (R375)(13)'s (W) list in PLACE-papers -- FINDINGS.md and OPEN_TRAILS.md, each by its path at PLACE-papers
#   ### 1198a637; REGISTRY, ERRATA and the register not written ((R375)(12), N3); no sentence of any paper written or edited; no new file
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
PP_NEW = ()   # ### (R380): no new file in PLACE-papers
# ### (R364) amendment row 3 (6): THE (W) ENTRIES (R364)(8) GIVES IN WORDS, each with the clause that gives it, read by tools/standing/wlist.py
# ### (word_rows) into the (W) bank and by tools/standing/cites.py's ferry_paths for a name in no tree. The entries (8) gives "on its item's
# ### pass and not otherwise" are not rows here: each enters by its item's route ((R364)(3)(xvi), `amend.py pass`) on the pass.
W_WORDS = (('relay/HANDOFF.md', '(R380)(13): HANDOFF.md'),
           ('relay/data/b770_address_scan_commits.txt', '(R380)(3), (13): the files b769 left -- this act`s per-commit scan bank, begun by b769`s closing step-row commit, committed alone at step zero'),
           ('relay/data/b771_address_scan_commits.txt', '(R380)(13): data/b771_address_scan_commits.txt, which the closing`s route begins for the next act (the one-call tool`s scan after this act`s closing commit, b764 [K19])'),
           ('relay/data/b769_relay_push-b769-closing_push_out.txt', '(R380)(3), (9), (13): the files b769 left -- its closing push capture, written masked by the gated push and committed at step zero as left'),
           ('relay/data/b769_put_5.json', '(R380)(3), (13): the files b769 left -- its put bank answered after the root (Root banks), committed alone at step zero'),
           ('relay/data/b769_put_6.json', '(R380)(3), (13): the files b769 left -- its put bank answered after the root (Closing add), committed alone at step zero'),
           ('relay/data/b770_hook_refusals.txt', '(R380)(3), (13): the files b769 left -- data/b770_hook_refusals.txt, holding one row that b769`s close wrote, committed alone at step zero'),
           ('relay/tools/acts/b770.py', '(R380)(13): tools/acts/b770.py'),
           ('relay/tools/push_gated.sh', '(R380)(13): tools/push_gated.sh -- each capture written masked, PLACE-papers` under [K32] from its commit on ((9))'),
           ('relay/tools/project_set.py', '(R380)(9), (13): tools/project_set.py -- the Project set built at the close under [K24], as at b769'),
           ('SIDE-explicit-formula/print_targets.txt', '(R380)(4), (13): in SIDE-explicit-formula print_targets.txt -- each compiled theorem`s name joins it'),
           # ### b770 Component 3 (defect (h)): the files of (4) in the kernel's source folder, each by the plan's line naming it (data/b770_plan.txt,
           # ### relay 365e5ecb), as this list's step-zero note below orders; (f) and (g) stand in the list by amendment row 1
           ('SIDE-explicit-formula/SIDEExplicitFormula/Schema/ZQ/FromCoefficients.lean', '(R380)(4)(b), (13): in SIDE-explicit-formula the file of (4)(b) in the kernel`s source folder, named by the plan (data/b770_plan.txt :43)'),
           ('SIDE-explicit-formula/SIDEExplicitFormula/SupportPositivity.lean', '(R380)(4)(c), (13): in SIDE-explicit-formula the file of (4)(c) in the kernel`s source folder, named by the plan (data/b770_plan.txt :67)'),
           ('SIDE-explicit-formula/SIDEExplicitFormula/Composition.lean', '(R380)(4)(d), (13): in SIDE-explicit-formula the file of (4)(d) in the kernel`s source folder, named by the plan (data/b770_plan.txt :92)'),
           ('SIDE-explicit-formula/SIDEExplicitFormula/Window/CQLeast.lean', '(R380)(4)(e), (13): in SIDE-explicit-formula the file of (4)(e) in the kernel`s source folder, named by the plan (data/b770_plan.txt :112)'),
           ('PLACE-project-set/*', '(R380)(9), (13): the Project`s repository whole -- PLACE-project-set under the account, private, its clone outside every repository of the record, written by the builder`s step alone and edited by no hand'))
#   ### b770 step zero: (R380)(13)'s (W) list in words: the banks as data/b770_* and their generators as tools/b770_*.py; tools/acts/b770.py;
#   ### the files b769 left by name ((R380)(3): the masked closing push capture, data/b770_address_scan_commits.txt, the two put banks
#   ### answered after the root and data/b770_hook_refusals.txt; no answers-bank row for them stands outside git);
#   ### data/b771_address_scan_commits.txt; HANDOFF.md; tools/standing/ with VERSION (a standing kind; moved by (8) alone, (R380)(11));
#   ### tools/push_gated.sh and tools/project_set.py; in SIDE-explicit-formula the files of (4) in the kernel's source folder, each taking
#   ### its row here when the plan of (4)(a) names it and before it is written, and print_targets.txt, the workflow's file changed by
#   ### nothing ((9)); PLACE-papers by PP_EDITED; the Project's repository whole; no path under day1/, phase1.5/, phase2/ or internal/ ((13))
#   ### b769 step zero: (R379)(13)'s (W) list in words: the banks as data/b769_* and their generators as tools/b769_*.py; tools/acts/b769.py;
#   ### b768's carried files by name ((R379)(3): the masked closing push capture and data/b769_address_scan_commits.txt);
#   ### data/b770_address_scan_commits.txt; HANDOFF.md; tools/standing/ with VERSION (a standing kind; moved by (8) alone, (R379)(11));
#   ### tools/push_gated.sh and tools/project_set.py; PLACE-papers by PP_EDITED; the Project's repository whole; no path of a kernel and
#   ### none under day1/, phase1.5/, phase2/ or internal/ ((13))
#   ### b768 step zero: (R378)(13)'s (W) list in words: the banks as data/b768_* and their generators as tools/b768_*.py; tools/acts/b768.py;
#   ### b767's carried files by name ((R378)(3): the masked closing push capture and data/b768_address_scan_commits.txt; b767's command
#   ### bank tracked at b767, so not carried); data/b769_address_scan_commits.txt; HANDOFF.md; tools/standing/ with VERSION (a standing
#   ### kind; moved by (8) alone, (R378)(11)); tools/push_gated.sh and tools/project_set.py; in SIDE-explicit-formula the files of (4) in
#   ### the kernel's source folder and print_targets.txt, the workflow's file changed by nothing ((9)); PLACE-papers by PP_EDITED; the
#   ### Project's repository whole
#   ### b767 step zero: (R377)(13)'s (W) list in words: the banks as data/b767_* and their generators as tools/b767_*.py; tools/acts/b767.py;
#   ### b766's carried files by name ((R377)(3): the masked closing push capture, data/b767_address_scan_commits.txt and the command bank
#   ### as N4 read it); HANDOFF.md; tools/standing/ with VERSION (a standing kind; moved by (8) alone, (R377)(11)); tools/push_gated.sh and
#   ### tools/project_set.py; in SIDE-explicit-formula the files of (4) in the kernel's source folder, print_targets.txt and, under (5),
#   ### the workflow's file; PLACE-papers by PP_EDITED; the Project's repository whole
#   ### b766 step zero: (R376)(12)'s (W) list in words: the banks as data/b766_* and their generators as tools/b766_*.py; tools/acts/b766.py;
#   ### b765's carried files by name ((R376)(3): data/b766_address_scan_commits.txt, and b765's eight push captures under (7) [K23]);
#   ### HANDOFF.md; tools/standing/ with VERSION (a standing kind; moved by (7) alone, (R376)(10)); tools/push_gated.sh and
#   ### tools/project_set.py; in SIDE-explicit-formula the files of (4) in the kernel's source folder, each taking its row here when named
#   ### and before it is written, and print_targets.txt; PLACE-papers by PP_EDITED; the Project's repository whole
#   ### b765 step zero: (R375)(13)'s (W) list in words: the banks as data/b765_* and their generators as tools/b765_*.py; tools/acts/b765.py;
#   ### b764's carried files by name ((R375)(3): the closing push-out bank, data/b765_address_scan_commits.txt and tools/mirror_prevbuild.json);
#   ### HANDOFF.md; tools/standing/ with VERSION (a standing kind; moved by (8) and, where the dispatch route needs it, (4) alone, (R375)(11));
#   ### the builder's step of (7) under tools/ and the files of (5)(b), each taking its row here when named and before it is written; the
#   ### planted module of (4)(a) on push-b765-planted, which (13) does not name, its row from (4)(a) when chosen (read in the misses);
#   ### PLACE-papers by PP_EDITED; the repository of (7) whole, its row when made
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
NEXT = 'the act after this one, as the author answers at the root (the answers bank) ((R380)(13)): THE TIP, the act after this one brings the Day 1 record`s files current and enters each text once, The Epstein Control Object`s next edition with the statements of (4) that compiled, One Page`s next edition with the composition where [D1] stands, the monograph`s next edition taking b769`s fact items, the description at a sixth edition and the pages from the navigator`s texts, with the keys for the source of the protected name and for the current edition of a keystone row ahead of them, the four parts of the act-root chain run again and nothing published before the author`s word at a prompt of its own; or, where a statement of (4) stands CARRIED, the act that continues it; or another the author names'
NEXT_ACT = 'b771'


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
ACT_CURRENT_COMMIT = 'bcf5691f'         # ### data/act_current.json for b770 committed alone through the one-call tool ((R380)(3)), the scan in the call; its row step 1 (2026-11-26T21:01:37Z), the act's opening row
STEPZERO = '8130e16b'             # ### step 2 (21:02:19Z). The first of the files b769 left committed alone ((R380)(3)): data/b769_relay_push-b769-closing_push_out.txt, masked by the gated push, alone in its commit as G-PUSHOUT-COMMITTED reads it (checks.tpl :1674); data/b770_address_scan_commits.txt, the two put banks and data/b770_hook_refusals.txt follow, each alone
# ### b766: b765's carried files, each committed alone through the one-call tool ((R376)(3)), in the order made: (commit, step, the files);
# ### tools/mirror_prevbuild.json NOT CARRIED: its working bytes equal HEAD's (git status, 06:56Z), so no add and no commit; b765's eight
# ### push captures wait on [K23] in Component 1, each holding the account; data/b764_hook_refusals.txt and data/b765_hook_refusals.txt stay
# ### uncommitted while each holds a profile path
# ### b765: b764's carried files, each committed alone through the one-call tool ((R375)(3)), in the order made: (commit, step, the files);
# ### tools/mirror_prevbuild.json NOT CARRIED: its working bytes equal HEAD's (stat764.py and git diff, 10:04Z: no line of it differs), b764's
# ### build leaving no difference, so no add and no commit -- (R375)(3): nothing of it to carry, printed; data/b764_hook_refusals.txt stays
# ### uncommitted while its :7 holds a profile path
# ### b764: b763's carried files, each committed alone through the one-call tool ((R374)(3)), in the order made: (commit, step, the files);
# ### tools/mirror_prevbuild.json NOT CARRIED: its working bytes equal HEAD's with their 89 carriage returns removed (scratch prevbuild764.py,
# ### 17:05Z), the add staged nothing (17:07:06Z) and the tool refused the commit, "nothing staged in D:\relay" (17:07:21Z) -- (R374)(3):
# ### nothing of it carried, the refusal printed
# ### b762: b761's carried files, each committed alone through the one-call tool ((R372)(3)), in the order made: (commit, step, the files);
# ### tools/mirror_prevbuild.json NOT CARRIED: its working bytes equal HEAD's with their 89 carriage returns removed (09:53Z), the add staged
# ### nothing and the tool refused the commit, "nothing staged in D:\relay" (09:53:33Z) -- (R372)(3): nothing of it carried, the refusal printed
# ### b763: b762's carried files, each committed through the one-call tool ((R373)(3)), in the order made -- all three carried, the
# ### builder's state file with data/act_current.json naming it in shared_edits (the tool refusing a shared tool unnamed there, 18:46Z)
STEPZERO_CARRIED = (('8130e16b', 2, 'the closing push-out capture'), ('c1a03ca5', 3, 'data/b769_put_5.json'), ('f4f538eb', 4, 'data/b769_put_6.json'),
                    ('8cea6031', 5, 'data/b770_address_scan_commits.txt'), ('f05fb948', 6, 'data/b770_hook_refusals.txt'))   # ### b770: b769's carried files committed alone at step zero ((R380)(3)), (commit, step, file), 21:02:19Z-21:04:34Z; no answers-bank row for the two put banks stands outside git
STEPZERO_CARRIED_B769 = (('bb9a2737', 2, 'the closing push-out capture'), ('aea820a4', 3, 'data/b769_address_scan_commits.txt'))   # ### b769: b768's carried files committed alone at step zero ((R379)(3)), (commit, step, file), 17:55:39Z-17:56:12Z
STEPZERO_CARRIED_B768 = (('dd1d7903', 2, 'the closing push-out capture'), ('a300b357', 3, 'data/b769_address_scan_commits.txt'))   # ### b768: b767's carried files committed alone at step zero ((R378)(3)), (commit, step, file), 13:06:42Z-13:07:20Z
STEPZERO_CARRIED_B767 = (('ef89f425', 2, 'the closing push-out capture'), ('7ef61c6b', 3, 'data/b769_address_scan_commits.txt'), ('f9c59718', 4, 'the command bank as N4 read it'))   # ### b767: b766's carried files committed alone at step zero ((R377)(3)), (commit, step, file), 08:34:36Z-08:35:45Z
STEPZERO_CARRIED_B766 = (('c323bf50', 2, 'data/b769_address_scan_commits.txt'),)   # ### b766's one at step zero; the captures after [K23]
STEPZERO_CARRIED_B765 = (('3c200e7c', 2, 'the closing push-out capture'), ('2a237834', 3, 'data/b769_address_scan_commits.txt'))   # ### b765's, kept beside (the carry had shifted its scan bank's name to b766's)
STEPZERO_CARRIED_B764 = (('baff91ad', 2, 'the closing push-out capture'), ('8f4c353d', 3, 'data/b769_address_scan_commits.txt'))   # ### b764's, kept beside (the carry had shifted its scan bank's name to b765's)
STEPZERO_CARRIED_B763 =(('9fbd3ac6', 2, 'the closing push-out capture'), ('b17f66d6', 3, 'tools/mirror_prevbuild.json with data/act_current.json'),
                         ('dc063f7d', 4, 'data/b769_address_scan_commits.txt'))   # ### b763's, kept beside (the carry had shifted its scan bank's name to b764's)
STEPZERO_PREDICTIONS = None   # ### LEFT EMPTY BY (R380)(9): "The texts: the letters listed after clause (13)", [A5], [Z1], [Z2], [U1], [U2], [D1], [D2], [L1], [L2], [C10], [C11], [I1], [I2] and [S5], no predictions text among them
STEPZERO_REGISTRATION = None   # ### LEFT EMPTY BY (R380)(9): "The registration: none at this act, so the worklist's REG_COMMIT is empty." b769 left it None ((R379)(9)). b768 left it None ((R378)(6), (9)). b767 (R377)(6): H-GRADED-WINDOW, data/b767_registration.txt, committed alone before the tool's run at graded knots, b9224ba6 (step 20, 11:53:18Z); b766 left it None ((R376)(4))
STEPZERO_REGISTRATION_B765 = '7907161c'   # ### b765's, kept beside. (R375)(4), (5)(c): [G2], H-RUNNER-RESTORE and H-SPLINE-WINDOW, banked as data/b765_registration.txt (scratch reg765.py, dry 10:09:2xZ, written 10:09:33Z: the ferry's :46-:50, 3,050 bytes, sha256 117b3672...) and committed alone before any dispatch and before the tool's run, step 4 (10:09:46Z)
STEPZERO_PREDICTIONS_B764 = '69200958'   # ### b764's (R374)(10): [P1] banked verbatim as data/b764_navigator_predictions.txt (scratch pred764.py, 17 lines, sha256 49bb42fb...) and committed alone before Component 1, step 4 (17:08:35Z)
STEPZERO_CARRIED_B762 = (('6052a453', 2, 'the closing push-out capture'), ('6096dca3', 3, 'data/b769_address_scan_commits.txt'))   # ### b762's, kept beside
STEPZERO_STEPS = None             # ### b761's step rows stand committed by b761 itself (its record's step-row commit): nothing carried
STEPZERO_TABLE = ()               # ### none: (R372)(3) carries no terminal-table file (b761's were b760's, at its steps 5 and 6)
STEPZERO_TABLE_B761 = ('c4670f7f', '6059f159')   # ### b761's, kept beside for the carried arms
STEPZERO_LATE = None
STEPZERO_HASHES = None
STEPZERO_PREVBUILD = None   # ### set from git status at step zero: tools/mirror_prevbuild.json read against HEAD. b770 (scratch prevbuild770.py, 21:06:47Z): its working bytes differ from HEAD's (b17f66d6) by a BOM, 89 carriage returns and the keys files and lastChanged, as b769's mirror build wrote it (18:35:45Z); (R380)(3) names it not, so NOT CARRIED: no add and no commit, printed in the misses
STEPZERO_REFUSALS = ()   # ### b770 (R380)(3): data/b770_hook_refusals.txt, holding the one row b769's close wrote, committed alone at step zero and named in STEPZERO_CARRIED; the refusals banks of b764 to b769 stay as b769 left them, (R380)(3) naming none of them
STEPZERO_SCAN = '8cea6031'   # ### b770: data/b770_address_scan_commits.txt as b769's closing step-row commit began it, with this act's step-zero runs, committed alone, step 5 (21:04:01Z)
STEPZERO_SCAN_B769 = 'aea820a4'   # ### b769: data/b769_address_scan_commits.txt as b768's closing step-row commit began it, with this act's step-zero runs, committed alone, step 3 (17:56:12Z)
STEPZERO_SCAN_B768 = 'a300b357'   # ### b768: data/b768_address_scan_commits.txt as b767's closing step-row commit began it, with this act's step-zero runs, committed alone, step 3 (13:07:20Z)
STEPZERO_SCAN_B767 = '7ef61c6b'   # ### b767: data/b767_address_scan_commits.txt as b766's closing step-row commit began it, with this act's step-zero runs, committed alone, step 3 (08:35:13Z)
STEPZERO_SCAN_B766 = 'c323bf50'   # ### data/b766_address_scan_commits.txt as b765's closing step-row commit began it, with this act's step-zero runs, committed alone, step 2 (07:05:30Z)
STEPZERO_SCAN_B765 = '2a237834'   # ### b765's, kept beside
STEPZERO_SCAN_B764 = '8f4c353d'   # ### b764's, kept beside
STEPZERO_SCAN_B763 = 'dc063f7d'   # ### b763's, kept beside
STEPZERO_BANKS = '9ddb4f1a'      # ### step zero's banks and carried tools, one commit (data/b770_stepzero.txt among them), step 10 (22:49:34Z), the ferry and the preseal words bank among them, each dispatch row's licence naming it; set at this act's step zero by (R380)(9), b769's not carried
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
                          and f != 'report.tpl')) + ('acts/b770.py',)
NEW_TOOLS = NEW_TOOLS + FOLD_FILES
STANDING_VERSION = 'v1.38.33'            # ### b770, Component 5 (the Edit tool, after the entry's second dry refused at the record's guard, record 29 :4522, where this line still read the entering v1.38.30 under the note "set at the close"; b769 set its own before the lock, tools/b769_worklist.py :490 at 6b951d93): (R380)(8) moved tools/standing/ by its three commits in Component 1, [K31] (60e769a5, v1.38.31), [K32] (75a8c747, v1.38.32) and [K33] (9432d7ce, v1.38.33), VERSION with each (tools/standing/VERSION at HEAD v1.38.33), and (R380)(11) moves it nowhere else; v1.38.30 entering
STANDING_VERSION_ENTERING = 'v1.38.30'
LEAN_TREES = (('D:/SIDE-explicit-formula', 'ffefddc6'), ('D:/SIDE-dirichlet-mod-24', 'e5ebdd15'))   # ### (R380) SCOPE READ's Lean pins: main at v0.46 (ffefddc6, push-b768-proof's tip and push-b770-proof's base by (4), each path of (4) read there); SIDE-dirichlet-mod-24 at v0.2.0, untouched; SIDE-kernel unmoved; SIDE-explicit-formula alone touched, under (4) (N5)
# ### b764 step zero (17:3xZ, after the citation check's dry halted on two Lean paths): the trees are the pins (R374)'s SCOPE READ names for
# ### its Lean reads (data/b764_ferry.txt :3): "at v0.43" (819e4a83), "on push-b763-arith at ec14e9d9" (ControlFailureStatement.lean) and
# ### "on push-b763-keiper at a59632eb" (KeiperPolygamma.lean); the carry had left main's pin alone, so the reader read the two branch files
# ### against main and halted (ABSENT FROM THE TREE AT ITS PIN), each file standing at its named commit (scratch facts764f.py: 76 and 136 lines)
# ### v1.18.0, (R364)(2)(ii): the act's banks whose comparative sentences the citation check reads, and a reading row for each word (tools/standing/cites.py
# ### comparative_rows); set by the Edit tool as Components 2-4 write the banks, before the lock
COMPARATIVE_BANKS = ('data/b770_corrigendum.txt', 'data/b770_price.txt', 'data/b770_defects.txt')
COMPARATIVE_ROWS = ()   # ### comparative word in them ("at least" excepted by the reader), so no reading row; the check reads the three for one
#   ### the trees the ruling's Lean paths are read against: zq-b730's tip, and Mathlib at its pin (the ferry's "Mathlib at the pin: Analysis/Complex/AbsMax.lean :405, ...")
# ### b770, before the lock (the Edit tool, 2026-11-27): v1.38.31 to v1.38.33's files by [K31] to [K33] (60e769a5, 75a8c747, 9432d7ce),
# ### read by git diff --name-status 376e35db HEAD -- tools/standing/ (10:43:52Z and scratch armset770.py, 10:50:33Z): nine modified and
# ### hostmask.py added; read by regspec's STANDINGWRITTEN alone (regspec.tpl :398, the module's regspec 11), where the carry left b769's
# ### six and its empty marker under b770's name; b769's lists kept beside under its names, read by nothing
STANDING_CHANGED = ('VERSION', 'act.py', 'commit.py', 'components.py', 'fold/checks.tpl', 'fold/closing.tpl', 'fold/record.tpl', 'hook.py', 'prevdry.py')
STANDING_NEW = ('hostmask.py',)   # ### b770 (R380)(8): [K32]'s shared mask, added by 75a8c747
STANDING_CHANGED_B769 = ('VERSION', 'cadence.py', 'fold/checks.tpl', 'prevdry.py', 'roster.py', 'v1345.py')   # ### b769's: [K29] and [K30]'s files, git diff 55166251 HEAD (2026-11-25T23:26:05Z)
STANDING_NEW_B769 = ()   # ### b769's: LEFT EMPTY BY (R379)(11) at its act, none added
STANDING_CHANGED_B764 = ('VERSION', 'act.py', 'append.py', 'armnorm.py', 'carry.py', 'cites.py', 'close.py', 'commit.py', 'controls.py',
                         'fold/checks.tpl', 'fold/closing.tpl', 'fold/record.tpl', 'lsrread.py', 'nextact.py', 'remotecache.py', 'repeat.py',
                         'rootparts.py')   # ### b764: v1.37.2 to v1.38.18's modified files, read by git diff --name-status 0f9b1df2 HEAD -- tools/standing/ (22:5xZ)
STANDING_NEW_B764 = ('dispatchrate.py', 'needle.py', 'toset.py')   # ### b764: the three added, [K14]'s, [K5]'s and [K1]'s; the planted controls stand in tools/b764_repair_controls.py, an act tool
STANDING_CHANGED_B763 = ('VERSION', 'commit.py')   # ### b763's (R373)(5), kept for the carried arms
STANDING_NEW_B763 = ('v1372.py',)
STANDING_CHANGED_B762 = ()   # ### b762's: (R372)(11), no standing change, kept for the carried arms
STANDING_CHANGED_B760 = ('VERSION', 'commit.py', 'handoff.py', 'subject.py')   # ### b760's: v1.36.8 to v1.37.1's changed files (4), kept for the carried arms that cite them
STANDING_NEW_B760 = ('v1368.py', 'v1369.py', 'v1370.py', 'v1371.py')
# ### b753's commits the act reads (the names kept for the carried arms: the previous act's)
B714_CLOSING = '376e35db'    # ### b769's last commit (its closing step row), the act's relay base
B714_RECORD = 'b5c98385'     # ### b769's record commit (relay)
B714_ROOT = '14ebaf2f7e6633aca40602902b3f163ca9d09c038d53753ccc32fb1467d63ba3'   # ### b769's root, data/act_roots.txt's last row
B723_ROOT_BANKS = '2b666a38'  # ### b769's root commit, the banks its root rode with
# ### later stages: the commits of the components, read from the logs after each was made (None until made)
C1_STANDING = ('60e769a5', '75a8c747', '9432d7ce')   # ### (R380)(8): [K31] v1.38.31 (step 16, 23:19:58Z); [K32] v1.38.32 (step 20, 23:49:51Z); [K33] v1.38.33 (step 24, 00:10:09Z); [K32] and [K33] in Component 1 before the opening pass, appended as made; VERSION with each; a tuple, as checks 9 reads it (b765's form)
C1_LOCKGATE = ''     # ### b770: tools/b770_lockgate.py carried and its cite set, committed before any run, set when made
C1_LOCKGATE_B769 = ''     # ### b769: tools/b769_lockgate.py carried and its cite set, committed before any run, set when made
C1_LOCKGATE_B768 = ''     # ### b768: tools/b768_lockgate.py carried and its cite set, committed before any run, set when made
C1_LOCKGATE_B767 = '78a259ea'     # ### b767: tools/b767_lockgate.py carried and its cite set, committed before any run with the face and probe-path tools (step 65, 18:47:36Z); in CHAIN too (b764's trap)
C1_LOCKGATE_B766 = '72733b77'     # ### b766: tools/b766_lockgate.py carried and its cite set, committed before any run with the face and probe-path tools (step 68, 18:17:59Z); in CHAIN too (b764's trap). The carry had left b765's d03be64e
C1_LOCKGATE_B765 = 'd03be64e'   # ### b765's, kept beside
C1_LOCKGATE_B764 = 'ec439ca3'   # ### b764's, kept beside: tools/b764_lockgate.py carried and set, committed before any run with the face and probe-path tools (step 69, 00:27:48Z)
C1_STANDING_LATER = (('(8)(ii)', 'v1.35.5', 'e0428564'),)   # ### Component 6, (R367)(8)(ii): the closing's one count in one form, a version commit of its own with its controls 6 of 6 (step 51)
C5_FAULTS = ()   # ### (carried name) no fault count this act
DOORS = ('tools/b770_doors.py', '2bc7eca8', 'data/b770_doors.txt', 'c98beed0')   # ### (R367)(8)(v): the two passed descriptions sent by gh and each read back equal (tool step 48, bank step 50)
C5_LANDED, C5_CARRIED = 5, 0   # ### the repairs of (8): (i) the cut, (ii) v1.35.5, (iii) the gh-call reader, (iv) REGISTRY's header, (v) the two descriptions; none carried
C1_STANDING_REPAIR = None          # ### none in Component 1
C4_STANDING = None                 # ### none
C1_RELAY = '767a8641'        # ### b770: the c1 route, events rows (31)-(50) and the worklist's STEPZERO_BANKS, committed before any run of it (step 11, 23:03:51Z)
C1_CEILING_TOOL = ()         # ### b765: no ceiling tool -- the ceiling read at step zero in the price table and after Component 2 by a read-only scratch (events (52), 14:13:35Z), banked in no file
C1_CEILING_TOOL_B764 = ('542354bf',)   # ### b764's, kept beside
C1_CORR = '4d274231'         # ### b770: the corrigendum banks for b769, data/b770_corrigendum.txt, .json, the landing bank and the corrigenda bank's row (90), with events rows (51)-(52) and the worklist (step 13, 23:09:58Z); its readers checks 8 and the record's composers
C1_CORR_B769 = '1c4e6109'         # ### b769: the corrigendum banks, data/b769_corrigendum.txt, .json, the landing bank and the corrigenda bank's row (89) (step 7, 19:10:21Z, git show --name-only); b769, before the lock (the Edit tool, 2026-11-26): set where Component 1 left it empty, its readers checks 8 and the record's composers
C1_CORR_B768 = '1ddea88d'         # ### b768: the corrigendum banks, data/b768_corrigendum.txt, .json, the landing bank and the corrigenda bank's row (88) (step 7, 14:24:20Z)
C1_CORR_B767 = 'ea50f0ee'         # ### b767: the corrigendum banks, data/b767_corrigendum.txt, .json, the landing bank and the corrigenda bank's row (87) (step 8, 09:34:31Z)
C1_CORR_B766 = '06dea7e2'         # ### b766: the corrigendum banks, data/b766_corrigendum.txt, .json, the landing bank and the corrigenda bank's row (86) (step 6, 08:12:22Z)
C1_CORR_B765 = '78f504a2'    # ### b765's, kept beside
C1_CORR_B764 = '89fbe2f4'    # ### b764's, kept beside
C1_CORR_B762 = '6918f5d9'    # ### b762's, kept beside for the carried arms
C1_CORR_B761 = '9a33e6b3'    # ### b761's, kept beside for the carried arms
B757_CLOSE = '401d3bda'      # ### b758 (R368)(1): b757's steps [22]-[25] under v1.35.7, committed under component 1 (01:07:08Z, events (19))
STATEMENTS_GEN = '4f069656'  # ### (R368)(7): tools/b758_statements.py as last committed before its bank (events (42))
KERNEL_DELETES = ()   # ### LEFT EMPTY BY (R380)(9): "The worklist's KERNEL_DELETES: nothing." b770 step zero, (R380)(3), (9), (12), N5: nothing; push-b768-proof kept at ffefddc6, push-b767-proof at 89fd5b54 and push-b766-proof at 3c67b8b5, each read there at the close
KERNEL_DELETES_B769 = ()   # ### LEFT EMPTY BY (R379)(9): "The worklist's KERNEL_DELETES: nothing." b769 step zero, (R379)(3), (9), (12), N5: no kernel branch removed; push-b768-proof kept at ffefddc6, push-b767-proof at 89fd5b54 and push-b766-proof at 3c67b8b5, each read there at the close
KERNEL_DELETES_B768 = ()   # ### LEFT EMPTY BY (R378)(9): no kernel branch removed ((R378)(3), (12), N5); push-b767-proof kept at 89fd5b54 and push-b766-proof at 3c67b8b5, each read there at the close (set at b768's step zero, its marker at Component 5 before the probes, as b767 gave its own)
KERNEL_DELETES_B767 = ()   # ### LEFT EMPTY BY (R377)(12): no kernel branch removed (N5); push-b766-proof kept at 3c67b8b5 and read there at the close (set at b767's step zero, its marker at Component 5 after the act part's probe withheld two arms on it)
KERNEL_DELETES_B766 = ('push-b765-planted',)   # ### b766 step zero, (R376)(7) [K22], N5: push-b765-planted removed at the kernel's remote and in its clone after [K22], its listing printed before and its absence read after; no other kernel branch (the carry had shifted the name to push-b766-planted)
KERNEL_DELETES_B765 = ('push-b765-planted',)   # ### b765's, kept beside. b765 (R375)(4), N5: the delete sent by the one-call tool's delete route before the lock, its listing printed (the command capture's deletes read by G-DELETES-ONE-BRANCH); the remote branch stays (RDELETE_ACTS not given b765, data/b765_misses.txt (3)), named in the closing message. b763's four push-b763-* branches and push-b764-runner kept
KERNEL_DELETES_REFUSED = ()   # ### LEFT EMPTY BY (R380)(9): "The worklist's KERNEL_DELETES: nothing." and (12) "no kernel branch removed", so no delete sent and none refused (b769's (R379)(9) set to b770's before the lock; b768's (R378)(9) set to b769's at its)
KERNEL_DELETES_REFUSED_B765 = (('push-b765-planted', '2026-11-21T19:19:48Z', 'not fully merged'),)   # ### b765's, kept beside (b766 step zero: the carry had shifted its name). b765: the route's `git branch -d` refused the branch, no upstream set and its tip on no main and not in HEAD, nothing written; by (4) "where the route does not, the branch stays, its name its warning, named in the closing message for removal by the author's word" -- kept in the clone and at its remote at 7d86a245
KERNEL_REMOVED = tuple(b_ for b_ in KERNEL_DELETES if b_ not in [r_[0] for r_ in KERNEL_DELETES_REFUSED])   # ### the branches the route removed from the clone: none
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
C1_RULES = None        # ### LEFT EMPTY BY (R380)(11): "The standing clauses' bank is not rewritten."; the three keys standing in the repairs bank and its tool, so no rules bank of this act; data/b756_rules.txt's rows (a)-(c) in force (b769's clause (R379)(11) set to b770's before the lock)
B756_RULES = ('data/b756_rules.txt', '0a151012')   # ### the rule this act works by ((R366)(2)), its bank and b756's commit carrying it; b758: the carry had shifted the path to b757's name, which no commit holds (defect (e))
RULES_COMMITS = ()
C1_CEILING = '7bdb8198'      # ### b770 (R380)(3), Component 5 (the Edit tool): the ceiling read before the lock, data/b770_ceiling.txt, WITHIN THE CEILING, the close read at 22.69 h from the opening row at b768's 4.85 h from its lock (step 62, 06:27:06Z; scratch ceil770.py, its controls 7 of 7); its readers read first (scratch grep770.py, 06:21:40Z): checks 34 :1333-:1337 (the bank's blob at this commit and its last commit, its foot), record 4 :2318-:2320, the entry :5340 and the report :8568, the four set to b768 at this commit where the carried form read b769
C1_CEILING_B769 = '2285c3f7'      # ### b769 (R379)(3), Component 5 (the Edit tool): the ceiling read before the lock, data/b769_ceiling.txt, WITHIN THE CEILING, the close read at 20.26 h from the opening row (step 45, 00:54:19Z, events (79)); its readers searched first (Grep with -o, 00:58Z): checks 34 :1300-:1301 (the bank's blob at this commit and its last commit), and a kept b755 text at :6300 and :6303 that record 34's return for b769 passes by
C1_CEILING_B768 = '03fd29f9'      # ### b768 (R378)(3), Component 5 (the Edit tool): the ceiling read before the lock, data/b768_ceiling.txt, WITHIN THE CEILING, the close read at 26.48 h from the opening row (step 78, 03:23:17Z, events (126)); its readers searched first (Grep with -o, 03:2xZ): checks 34 :1262-:1263 (the bank's blob at this commit and its last commit), and a carried finding text at :5578 and :5581
C1_CEILING_B767 = '72861d88'      # ### b767 (R377)(3): the ceiling read before the lock, data/b767_ceiling.txt, WITHIN THE CEILING, the close forecast at 26.46 h from the opening row (step 68, 21:18:26Z, events (126))
C1_CEILING_B766 = '15008621'      # ### b766 (R376)(3): the ceiling read after (4)(c), data/b766_ceiling.txt, UNDER BY 4.58 h, NOTHING CARRIED (step 26, 10:16:16Z, events (52)); the carry had left b765's LEFT EMPTY marker by (R375)(3)
C1_CEILING_B765 = None       # ### b765's: no ceiling bank
C1_CEILING_B764 = 'f0ad4589'   # ### b764's, kept beside
C1_PP = '11fe9707'           # ### PLACE-papers: FINDINGS -- the corrigendum for b769 at :16329 (Component 1, step 12, 23:07:31Z)
C1_TAG_PP = ()                     # ### (carried name) no tag note this act
C1_DISCHARGE_PP = ()               # ### (carried name) no discharge this act
C2_TOOL = None                     # ### (carried name) no driver this act
WEIGHT_LINE = None   # ### LEFT EMPTY BY (R380)(1): no weight line of its own, b769 at its weight within the corrigendum (data/b770_corrigendum.txt, FINDINGS :16329), as b769's (R379)(1) read for b768
CORR_LINE = 16329    # ### FINDINGS: the corrigendum for b769 (Component 1), landed at :16329 by the c1 route's write (23:05:11Z, data/b770_corrigendum.json entry_line); B711_CORRIGENDUM stands at b769's own, 16247, read at the act's start
NEXT_TRAIL_LINE = 18491      # ### OPEN_TRAILS: (R367)(1)'s dated line giving b756's answer, in (9)'s block (Component 6, PLACE-papers b14256c2)
DIFFERS_LINE = None   # ### LEFT EMPTY BY (R380)(12): no DIFFERS entry, no clause of (R380) ordering one; "REGISTRY, ERRATA, the census, the register and SPIRAL_MAP.md not written" (v1.38.1 [K1]'s marker; b770, before the lock, the Edit tool: b769's (R379)(12), under which REGISTRY, ERRATA and SPIRAL_MAP.md were written, set to b770's)
ERRATA_LINE = None   # ### LEFT EMPTY BY (R380)(12): ERRATA not written at this act ("REGISTRY, ERRATA, the census, the register and SPIRAL_MAP.md not written"), so no entry line; b770, Component 5 (the Edit tool): set where the carry left b769's 1163 (E-2026-11-25-1, PLACE-papers 5111e451) under b770's name, the errata override of checks 53 reading K.ERRATA_LINE is None
ERRATA_LINE_B769 = 1163   # ### b769's: E-2026-11-25-1 at ERRATA :1163 (group c3, PLACE-papers 5111e451), kept beside, read by nothing
ERRATA_LINE_B764 = 1149   # ### b764 (R374)(9)(a): [E1], E-2026-11-21-1, at ERRATA's end from :1149, PLACE-papers 772d5cf0, kept beside
C2_PLAN_FIRST = '365e5ecb'   # ### Component 2's first relay commit: the plan of (4)(a), data/b770_plan.txt, committed before any dispatch (step 27, 00:30:29Z)
C2_RELAY = '9d95c615'   # ### the last of Component 2's relay commits by its phase word, set as made: the rulings tool's group c2s with the inputs bank (step 43, 01:58:41Z); [A5]'s ledger at 4ca72b16 (step 30) before it; the c2s ledgers carried by bb496b75 (step 46, Component 3's phase)
# ### (R366)(4): each tool of the map beside its banks -- (name, generator, the generator's commits before the bank, bank, the bank's commit)
C2_MAP = (('the constellation rerun', 'tools/b770_constellation.py', ('3e112065', 'd2f78fab', '16ba8fbb', 'e4701c5f'),
           'data/b770_constellation_summary.txt', '069271bb'),
          ('the reverse read', 'tools/b770_reverse.py', ('d2f78fab', '16ba8fbb'), 'data/b770_reverse_read.txt', '069271bb'),
          ('what the two find beyond (3)', 'tools/b770_reverse.py', ('d2f78fab', '16ba8fbb'), 'data/b770_beyond_three.txt', '069271bb'))
C2_WALK = ('tools/b770_coeffs.py', '3bdb6561', 'data/b770_walk.txt', '9a989df8')   # ### (generator, its commit, bank, the bank's commit)
REG_WALK = ('data/b753_registrations.txt', '3f865479')   # ### H-C3-LAW's registration read at its blob ((R365)(3)), the commit data/b755_walk.txt names
# ### Component 3 ((R365)(5)(i), (4)): the literature bank, the candidates' generators each committed before its run, the candidates bank with
# ### the prior clause, the ceiling read again; each candidate (label, generator, the generator's commits before its bank, bank, the bank's commit)
C3_LITERATURE = '51739651'
C3_CANDS = (('(a)', 'tools/b770_closed.py', ('a7034608',), 'data/b770_cand_a.txt', '1b84e4b1'),
            ('(h)', 'tools/b770_zlist.py', ('1b84e4b1',), 'data/b770_cand_h.txt', 'ea99215e'),
            ('(c)', 'tools/b770_cands.py', ('ea99215e', '1b361013'), 'data/b770_cand_c.txt', 'b4668b52'),
            ('(j)', 'tools/b770_cands.py', ('ea99215e', '1b361013'), 'data/b770_cand_j.txt', 'b4668b52'),
            ('(k)', 'tools/b770_cands.py', ('ea99215e', '1b361013'), 'data/b770_cand_k.txt', 'b4668b52'),
            ('(l)', 'tools/b770_cands.py', ('ea99215e', '1b361013'), 'data/b770_cand_l.txt', 'b4668b52'))
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
# ### b764, Component 5 (the Edit tool): every tool of the act committed before the bank it wrote, each read from git (scratch files764.py,
# ### read-only, the step rows with each commit's files, 22:5xZ): (name, tool, its commits before the bank, bank, the bank's commit as it
# ### stands at HEAD). The repairs' planted controls stand in GENS_WITH_BANK (their bank rode twice with a later state of the tool, steps 14
# ### and 15, each run made at the tool's commit before). The repairs bank and the misses bank are the seat's by the Write tool, the price
# ### table a scratch reader's, the corrigendum the act module's c1 route, the dispatch rows the dispatch tool's routes, the reproduce bank
# ### tools/research/reproduce.py's and the address scan's bank its standing route's: each stands apart. Later banks appended as made
# ### b765, Component 5 (the Edit tool): every tool of the act committed before the bank it wrote, each read from git (scratch gens765.py
# ### and steprows765.py, read-only, 15:3xZ): (name, tool, its commits before the bank, bank, the bank's commit as it stands at HEAD). The
# ### repairs' planted controls a row of its own (no commit carries both); the registration, the repairs bank, the misses read, the price
# ### table and the reading of (6)(d) the seat's by the Write tool or a scratch writer, the corrigendum the act module's c1 route, the
# ### dispatch rows the dispatch tool's routes, the reproduce bank tools/research/reproduce.py's and the address scan's bank its standing
# ### route's: each stands apart. The runner's bank and the ledgers appended as made
# ### b766, Component 5 (the Edit tool, before any run): b766's tools and banks, each row read from git and the step rows (scratch
# ### steps766r.py and gens766.py, read-only, 18:38:32Z and 18:40:06Z: 18 rows, FAIL 0, each tool's commits since the base printed beside
# ### the listed ones); the carry had left b765's ten rows, whose tools and banks b766 does not hold. The rulings tool's four groups each a
# ### row with the tool's commits before that group's bank; the dispatch tool's controls bank (24 of 24) before the tool's raises, its own
# ### bank after them; the pole data's first bank in GENS_WITH_BANK (it rode with the tool's repair, b9c3eca2)
# ### b767, Component 4 (the Edit tool, before any run): b767's tools and banks, each row read from git and the step rows (scratch
# ### steps767r.py and gens767.py, read-only, 18:49:19Z and 18:50:54Z: 9 rows read, each tool's commits and its bank's since b766's close);
# ### the source-build bank written again after its tool's repair (980af315, defect (h)) and committed alone at 057c50dc; the dispatch
# ### tool's controls bank in GENS_WITH_BANK (it rode once with the tool's repair, 4f4c7c07); the dispatch tool's own bank appended at the
# ### close. The registration, the repairs bank, the misses read, the plan and the price table the seat's by the Write tool or a scratch
# ### writer, the corrigendum the act module's c1 route, the dispatch rows and the targets the dispatch tool's routes, the reproduce bank
# ### tools/research/reproduce.py's and the address scan's bank its standing route's: each stands apart
# ### b768, Component 4 (the Edit tool, before any run): b768's tools and banks, each row read from git (scratch gens768.py, read-only,
# ### 00:44:31Z: each tool's commits since b767's close and its bank's last commit, data/b768_events.txt (106)); the dispatch tool's controls
# ### bank in GENS_WITH_BANK (it rode once with the tool's repair, e7f39dc2); the dispatch tool's own bank joins GENS at its commit at the
# ### close. The generators of the kernel's data files (tools/b768_packed_data.py, _far_data.py, _band_data.py and _arith_data.py) write
# ### kernel files and no relay bank, so no row; the plan, the price table, the misses read, the repairs bank and the ceiling read the
# ### seat's by the Write tool or a scratch writer, the corrigendum the act module's c1 route: each stands apart
# ### b769, before the lock (the Edit tool, 2026-11-25, from git by scratch gens769.py, 22:19:31Z: the relay's commits after 55166251
# ### touching each tools/b769_*.py and each data/b769_* bank): each tool of the act that wrote a bank, its commits before the bank, the
# ### bank and the bank's commit; the step-zero carries (tools/b769_carry.py, _address_scan.py, _worklist.py) as at b768 none of them
# ### b770, Component 5 (the Edit tool, 2026-11-27, from git by scratch gens770.py, read-only, 04:19:58Z: the relay's commits after
# ### 376e35db touching each tools/b770_*.py that writes a bank and each of its banks): each tool, its commits before the bank (the first
# ### its first add), the bank and the bank's last commit; the plan, the price table, the misses, the corrigendum, the repairs bank and
# ### the ceiling read the seat's by the Write tool, a scratch writer or the act module's c1 route, so no row; the names classed at
# ### step zero; the two banks that rode with their tool's commit in GENS_WITH_BANK below (checks 34, N2_GENS_N 12)
GENS = (('the repairs` planted controls', 'tools/b770_repair_controls.py', ('14221add', 'af2d623a', '5a7ec193'), 'data/b770_repair_controls.txt', '0e99a945'),
        ('the names classed', 'tools/b770_names.py', ('5266f8cb', 'd3f76ad2', '53cedf70'), 'data/b770_names.txt', '9ddb4f1a'),
        ('the two index banks read', 'tools/b770_li_index.py', ('cb5b7525', '1521f59c'), 'data/b770_li_index.txt', 'd4f80fe3'),
        ('the sitting`s inputs', 'tools/b770_sitting.py', ('4780d829', '2d4d28d7', 'a2a39a09'), 'data/b770_recut_inputs.txt', '9d95c615'),
        ('the ledgers of group c2', 'tools/b770_rulings.py', ('745e234d',), 'data/b770_ledgers_c2.txt', '4ca72b16'),
        ('the ledgers of group c2i', 'tools/b770_rulings.py', ('745e234d', 'd4f80fe3'), 'data/b770_ledgers_c2i.txt', 'f9e94487'),
        ('the ledgers of group c2s', 'tools/b770_rulings.py', ('745e234d', 'd4f80fe3', '9d95c615'), 'data/b770_ledgers_c2s.txt', 'bb496b75'),
        ('the ledgers of group c4', 'tools/b770_rulings.py', ('745e234d', 'd4f80fe3', '9d95c615', '4bfa29e4', 'ea1a9943'), 'data/b770_ledgers_c4.txt', '40ffd737'),
        ('the dispatch tool`s controls', 'tools/b770_controls.py', ('48b1dfba',), 'data/b770_controls_control.txt', 'c3edca18'),
        ('the dispatch tool`s bank', 'tools/b770_controls.py', ('48b1dfba',), 'data/b770_controls.txt', '40ffd737'))
GENS_B769 = ()   # ### b769's stand in git at tools/b769_worklist.py
GENS_B768 = ()   # ### b768's stand in git at tools/b768_worklist.py
GENS_B767 = ()   # ### b767's stand in git at tools/b767_worklist.py
GENS_B766 = ()   # ### b766's eighteen stand in git at tools/b766_worklist.py
GENS_B765 = ()   # ### b765's ten stand in git at tools/b765_worklist.py
GENS_B764 = ()   # ### b764's seven stand in git at tools/b764_worklist.py
GENS_B763 = ()   # ### b763's nine stand in git at tools/b763_worklist.py
GENS_B762 = ()   # ### b762's five stand in git at tools/b762_worklist.py
GENS_B760 = ()   # ### b760's nine stand in git at tools/b760_worklist.py
GENS_B759 = ()   # ### b759's thirteen stand in git at tools/b759_worklist.py
GENS_B758 = ()   # ### b758's ten stand in git at tools/b758_worklist.py
PASSED_BANK = None   # ### (carried name) no passed writes this act
# ### b761: two banks of the sitting tool rode in a commit with a later state of their tool, each written by the tool as last committed before
# ### the write (the tool committed before each run, (N2)): (name, tool, bank, the commit carrying both, the bank's commit as it stands at HEAD)
GENS_WITH_BANK = (('the sitting`s agenda', 'tools/b770_sitting.py', 'data/b770_sitting_agenda.txt', 'a2a39a09', 'a2a39a09'),   # ### b770: written by the tool as committed at 2d4d28d7 and committed with the inputs route's commit a2a39a09, its only commit (scratch gens770.py, 04:19:58Z; events (69), (70))
                  ('the ledgers of group c3', 'tools/b770_rulings.py', 'data/b770_ledgers_c3.txt', 'ea1a9943', 'ea1a9943'))   # ### b770: written by the tool as committed at 4bfa29e4 and committed with the c4 group's commit ea1a9943, its only commit (events (86), (88))
GENS_WITH_BANK_B769 = ()   # ### LEFT EMPTY BY (R379)(9): N2's run clause as (9) reads it, each tool committed before the command that executes it; b769: none, no bank rode with its own tool's commit (scratch gens769.py, 22:19:31Z), a reading the toset rule has no form for but this marker, checks 34 wanting none
GENS_WITH_BANK_B768 = (('the dispatch tool`s controls', 'tools/b769_controls.py', 'data/b769_controls_control.txt', 'e7f39dc2', '85f17b9a'),)   # ### b768: the bank of 17:04:19Z, written by the tool as committed at 26c49bdb, rode with the tool's repair of the import graph, e7f39dc2 (step 33, events (66)); written again by the tool at e7f39dc2 (17:11:15Z, 31 of 31, events (67)) and committed at 85f17b9a, its commit at HEAD (scratch gens768.py, 00:44:31Z)
GENS_WITH_BANK_B767 = (('the dispatch tool`s controls', 'tools/b769_controls.py', 'data/b769_controls_control.txt', '4f4c7c07', 'c8416cec'),)   # ### b767: the bank of 14:26:06Z, written by the tool as committed at 922f34c4, rode with the tool's repair of defect (l), 4f4c7c07 (step 39); written again by the tool at bf9ce5c2 (15:46:50Z) and committed alone at c8416cec (step 46), its commit at HEAD (scratch gens767.py, 18:50:54Z)
GENS_WITH_BANK_B766 = (('the pole data of L8', 'tools/b769_poledata.py', 'data/b769_poledata.txt', 'b9c3eca2', 'b9c3eca2'),)   # ### b766: written by the tool as committed at 01710c94 (16:19:19Z) and committed with the tool's repair (defect (k)), b9c3eca2 (scratch gens766.py)
GENS_WITH_BANK_B765 = ()   # ### b765's: none
GENS_WITH_BANK_B764 = (('the repairs` planted controls', 'tools/b769_repair_controls.py', 'data/b769_repair_controls.txt', 'af463213', '7e93bb18'),)   # ### b764's, kept beside
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
# ### b764, Component 5 (the Edit tool): the act's relay commits after step zero's banks (3c8e5ebc, step 5), every one, in their order, read
# ### from data/b764_steps.json and git (scratch steps764.py and files764.py, read-only, 22:5xZ: 64 rows, each commit with its files, the
# ### kernel's step 56 and PLACE-papers' step 7 apart); later commits appended as made. b763's fifty-seven keys stand in git at
# ### tools/b763_worklist.py
# ### b765, Component 5 (the Edit tool): the act's relay commits after step zero's banks (c689e662, step 5), every one, in their order,
# ### read from data/b765_steps.json and git (scratch steprows765.py and gens765.py, read-only, 15:3xZ: 50 rows, each commit with its
# ### files, PLACE-papers' step 7 and the kernel's steps apart); later commits appended as made. b764's keys stand in git at
# ### tools/b764_worklist.py
# ### b766, Component 5 (the Edit tool, before any run): the act's relay commits after step zero's banks (f85c5899, step 3), every one, in
# ### their order, read from data/b766_steps.json and git (scratch steps766r.py, read-only, 18:38:32Z: 69 rows, each commit with its files,
# ### PLACE-papers' five steps and the kernel's fourteen apart); the carry had left b765's keys and commits, none of them b766's; later
# ### commits appended as made. b765's keys stand in git at tools/b765_worklist.py
# ### b767, Component 4 (the Edit tool, before any run): the act's relay commits after step zero's banks (f6225683, step 5), every one, in
# ### their order, read from data/b767_steps.json and git (scratch steps767r.py, read-only, 18:49:19Z: 65 rows, each relay commit with its
# ### files, PLACE-papers' three steps and the kernel's fifteen apart); the carry had left it empty; later commits appended as made.
# ### b766's keys stand in git at tools/b766_worklist.py
# ### b768, Component 1 (the Edit tool): the act's relay commits after step zero's banks (850b09d5, step 4), in their order, each read from
# ### its step row (steps 5 and 7), appended as made; b767's stands in git at tools/b767_worklist.py
CHAIN = (('c1', '767a8641'), ('corr', '4d274231'),
         ('k31_ctl', '14221add'), ('price_foot', '90085aff'), ('k31', '60e769a5'), ('k31_row', '99a723a1'),
         ('wl_k31', '04c35afa'), ('k32_ctl', 'af2d623a'), ('k32', '75a8c747'), ('k32_row', '4f318345'),
         ('wl_k32', '1991ee50'), ('k33_ctl', '5a7ec193'), ('k33', '9432d7ce'), ('k33_row', '0e99a945'),
         ('wl_k33', 'f9e41612'), ('plan', '365e5ecb'), ('rulings_gen', '745e234d'), ('ledgers_c2', '4ca72b16'),
         ('wl_c2', '9543a67b'), ('controls_gen', '48b1dfba'), ('dispatch_1', 'c3edca18'), ('li_index_gen', 'cb5b7525'),
         ('li_index_fix', '1521f59c'), ('rulings_c2i', 'd4f80fe3'), ('ledgers_c2i', 'f9e94487'), ('sitting_gen', '4780d829'),
         ('sitting_fix', '2d4d28d7'), ('sitting', 'a2a39a09'), ('rulings_c2s', '9d95c615'), ('wl_wwords', 'bb496b75'),
         ('rows_66_76', '81d8ac6a'), ('rows_77_81', '68d3fc5b'), ('rulings_c3', '4bfa29e4'), ('rulings_c4', 'ea1a9943'),
         ('read_8', '7f6ca3aa'),
         ('ledgers_c4', '40ffd737'), ('prelock', 'db67cc2f'), ('prelock_stubs', '1ae60670'), ('ceiling', '7bdb8198'),
         ('wl_ceiling', '4d2a4df0'), ('scans', 'f3e6db4f'), ('tools_lock', 'd2d68e90'), ('face_blocks', 'ba1daf7f'), ('touch_sets', '4f793839'), ('critical_width', '64f15ae6'), ('touch_bank', '0f18d1d2'), ('needle_calls', '594139ba'), ('kernels_face', '9e825374'), ('probe_act', 'f0dc21d8'), ('clone_main', 'd74eba17'), ('wl_markers', '5b8d43c8'), ('probes_all', '395a4e07'), ('face_declared', 'ad351148'), ('handoff', '53a0a2e6'), ('handoff_chain', 'ea6a9b69'), ('record_banks', '4baf0e78'), ('misses_set', 'd9b4a9d6'), ('n2_n3_repairs', '3223ecd5'), ('prevdry_banks', '0647a607'))   # ### b770, Component 5 (the Edit tool, 17:07Z, after the fifty-sixth summary): step 82 from its subject (git log, 17:06:40Z). b770, Component 5 (the Edit tool, 16:53Z, after the fifty-fifth summary): step 81 from its subject (git log, 16:52:13Z). b770, Component 5 (the Edit tool, 14:55Z, after the fifty-fourth summary): step 80 from its subject (git log, 14:54:08Z). b770, Component 5 (the Edit tool, 13:38Z, after the forty-eighth summary): step 79 from its subject (git log, 13:38:10Z), b768's key for the like step. b770, Component 5 (the Edit tool, 12:52Z, after the forty-fourth summary): step 78 from its subject (the one-call tool's read-back, 12:35:58Z). b770, Component 5 (the Edit tool, 12:25Z): steps 76 and 77 from their subjects (the one-call tool's read-backs, 12:20:25Z and 12:23:56Z), the handoff placed in the chain at its time as b769's. b770, Component 5 (the Edit tool, 12:18Z, after the forty-second summary): step 75 from its subject (the one-call tool's read-back, 12:05:02Z). b770, Component 5 (the Edit tool, 12:02Z, after the forty-first summary): step 74 from its subject (git log, 12:01:56Z). b770, Component 5 (the Edit tool, 10:52Z, after the fortieth summary): steps 72 and 73 from their subjects (git log, 10:51:43Z). b770, Component 5 (the Edit tool, 10:25Z, after the act part's probe): steps 70 and 71 from their subjects (the one-call tool's read-backs, 10:02:25Z and 10:09:57Z). b770, Component 5 (the Edit tool, 09:59Z, at the needle calls): step 69 from its subject (the one-call tool's read-back, 09:46:34Z). b770, Component 5 (the Edit tool, 09:19Z, at the touch bank): steps 67 and 68 from their subjects (git log, 09:17:51Z). b770, Component 5 (the Edit tool, 08:57Z, at the touch read): step 66 from its subject (git log, 08:55:18Z), where the entry's order paragraph stopped at d2d68e90. b770, Component 5 (the Edit tool, 08:29Z): steps 63 to 65, each from its subject (git log, 08:29:04Z). b770, Component 5 (the Edit tool): steps 59 to 62, each from its step row (scratch ceilfacts770.py, 06:22:40Z; step 58 the papers` repository's c4pp); later commits appended as made. b770: steps 11, 13-28, 30-32, 34-37, 39-43, 46, 49, 52, 54, 56 and 57, each from its step row (scratch steps770s.py, 03:43:41Z; steps 56 and 57 from commit.py's row lines, 03:52:00Z and 03:55:29Z; steps 12, 29, 38, 44, 55 and 58 the papers` repository's, steps 33, 45, 47, 48, 50, 51 and 53 the kernel's); the act's relay commits after step zero's banks, in their order, appended as made; b769's stands in git at tools/b769_worklist.py
CHAIN_B765 = ()   # ### b765's fifty keys stand in git at tools/b765_worklist.py
CHAIN_B764 = ()   # ### b764's sixty keys stand in git at tools/b764_worklist.py
CHAIN_B763 = ()   # ### b763's fifty-seven keys stand in git at tools/b763_worklist.py
CHAIN_B762 = ()   # ### b762's thirteen keys stand in git at tools/b762_worklist.py
CHAIN_B761 = ()   # ### b761's twenty-one keys stand in git at tools/b761_worklist.py
CHAIN_B760 = ()   # ### b760's twenty-five keys stand in git at tools/b760_worklist.py
CHAIN_B759 = ()   # ### b759's sixty-odd keys stand in git at tools/b759_worklist.py
# ### PLACE-papers' commits of the act in their order: the corrigendum (FINDINGS); the page and [G1], [G2] (the new file and REGISTRY); the
# ### lines of (7), (8) and [O6] (OPEN_TRAILS)
# ### b763: the corrigendum with [I1] (FINDINGS); the canon's section XXV and the lines of (9) under one dated head, with the build lines
# ### of (6) and (7) (THE_METHOD_CANON.md and OPEN_TRAILS.md), appended as made
# ### b764: the corrigendum for b763 (FINDINGS, step 7); the ledgers of (7), (8) and (9) (ERRATA, OPEN_TRAILS and BIBLIOGRAPHY.md) appended
# ### when written
# ### b765: the corrigendum for b764 (FINDINGS, step 7); the lines of (4)-(9) and the author's words (OPEN_TRAILS) appended when written
# ### b766: the corrigendum for b765 (FINDINGS, step 5); the four groups of the rulings tool in OPEN_TRAILS, each after the tool's commit
# ### that cut it and before its relay banks (steps 20, 30, 50 and 65); the carry had left b765's two
# ### b767: the corrigendum for b766 (FINDINGS, step 7); the rulings tool's groups c2 and c5 in OPEN_TRAILS, each after the tool's commit
# ### that cut it and before its relay banks (steps 25 and 63); the entry and the trail at the close appended as made
# ### b768: the corrigendum for b767 (FINDINGS, step 6); the lines of (7), [R2] and [A3], and the outcome's text in OPEN_TRAILS, each after
# ### the tool's commit that cut it and before its relay banks; the entry and the trail at the close appended as made
PP_CHAIN = (('c1pp', '11fe9707'), ('c2pp', 'f945cbd9'), ('c2ipp', 'c599930d'), ('c2spp', 'a0ac08c9'), ('c3pp', 'c0146cf4'), ('c4pp', '423a6b78'))   # ### b770: the act's PLACE-papers commits in their order, appended as made (step 12, the corrigendum at FINDINGS :16329; step 29, [A5] at OPEN_TRAILS :19595; step 38, [I1] at :19597; step 44, [S5] at :19599; step 55, [Z1] to [L1] at :19603-:19609 under their head at :19601; step 58, [C11] at :19611)
PP_CHAIN_B769 = (('c1pp', 'b382b95e'), ('c2pp', '5cfb9577'), ('c2pp_map', '9aab5f65'), ('c2pp_ot', 'd4808187'), ('c2pp_arc', '4570c462'), ('c2pp_c2b', '41170e41'), ('c3pp', '5111e451'), ('c4pp', '3deb3dca'))   # ### b769: the act's PLACE-papers commits in their order, appended as made (steps 6, 15, 18, 25, 29, 32, 35 and 42: the corrigendum, the registry's block, the map's merge, [X4] and [M5] in OPEN_TRAILS, the cluster's source record, [B1] and [A4] with [C9], the four entries of ERRATA with [F2]-[F5] and [R3], [V1]), b768's keys
PP_CHAIN_B768 = (('c1pp', '9c43f4bb'), ('c2pp', 'eea70a2d'), ('c5pp', '45f187d1'))   # ### b768: the act's PLACE-papers commits in their order, appended as made (steps 6, 22 and 66)
PP_CHAIN_B767 = (('c1pp', '216d9715'), ('c2pp', 'ba23945a'), ('c5pp', 'adadfd62'))
PP_CHAIN_B766 = (('c1pp', '7a36f281'), ('c2pp', 'a183880f'), ('c3pp', '92108a44'), ('c4pp', '2d9d51ae'), ('c5pp', 'ff328d86'))
PP_CHAIN_B765 = (('c1pp', 'd9c03949'), ('ledgerspp', 'fb094a44'))   # ### b765's, kept for the carried readers that cite them
PP_CHAIN_B764 = (('c1pp', 'e383d313'), ('ledgerspp', '772d5cf0'))   # ### b764's, kept for the carried readers that cite them
PP_CHAIN_B763 = (('c1pp', '6034501c'), ('ledgerspp', '387713dd'))   # ### b763's, kept for the carried readers that cite them
# ### the order by time, relay and PLACE-papers together: each PLACE-papers key after the relay commit whose tool cut it; the ledgers written
# ### to PLACE-papers (ledgerspp) after the trial's bank and before the relay's ledgers banks (ledgers), as at b763
_KEYS = tuple(k_ for k_, _h in CHAIN)
# ### b766: each PLACE-papers key placed before the relay commit that follows it in time -- the corrigendum before its banks, each rulings
# ### group's OPEN_TRAILS commit before that group's relay banks (scratch steps766r.py: 08:09:43Z, 09:13:20Z, 10:38:25Z, 15:42:39Z, 17:49:47Z)
# ### b767: each PLACE-papers key placed before the relay commit that follows it in time -- the corrigendum before its banks, each rulings
# ### group's OPEN_TRAILS commit before that group's relay banks (scratch steps767r.py: 09:33:32Z, 12:13:27Z, 18:32:52Z)
# ### b768: each PLACE-papers key placed before the relay commit that follows it in time -- the corrigendum before its banks, each rulings
# ### group's OPEN_TRAILS commit before that group's relay banks (scratch steps768.py: 14:23:33Z, 15:35:31Z, 00:23:41Z)
# ### b769, before the lock (the Edit tool, 2026-11-25): each PLACE-papers key placed before the relay commit that follows it in time
# ### (scratch chainchk769.py, 22:25:24Z: 19:08:47Z, 19:54:20Z, 20:06:39Z, 20:47:18Z, 21:02:32Z, 21:13:23Z, 21:26:24Z and 22:12:04Z)
_PP_BEFORE = {'corr': 'c1pp', 'ledgers_c2': 'c2pp', 'ledgers_c2i': 'c2ipp', 'wl_wwords': 'c2spp', 'rulings_c4': 'c3pp', 'ledgers_c4': 'c4pp'}   # ### b770, Component 5: c4pp (step 58, 03:56:38Z) before ledgers_c4 (step 59, 04:03:19Z). b770: each papers` repository write's key placed before the relay commit that follows it in time, from the step rows (step 12 between steps 11 and 13; step 29 between steps 28 and 30; step 38 between 37 and 39; step 44 between 43 and 46; step 55 between 54 and 56), set as made; c4pp (step 58) before the next relay commit, set when it is made
TIME_ORDER = ('actcur', 'stepzero') + tuple(x_ for k_ in _KEYS for x_ in ((_PP_BEFORE[k_], k_) if k_ in _PP_BEFORE else (k_,)))
# ### b766, Component 5 (the Edit tool, before any run): each key's words, from its commit's subject and files (scratch steps766r.py,
# ### 18:38:32Z); later keys given words as made. b765's kept below under its own name, read by nothing
# ### b767, Component 4 (the Edit tool, before any run): each key's words, from its commit's subject and files (scratch steps767r.py,
# ### 18:49:19Z); later keys given words as made. b766's kept below as CHAIN_WORDS_B766 (the carry shifting its names), read by nothing
# ### b768, Component 4 (the Edit tool, while dispatch 14 built): each key's words, from its commit's subject (scratch steps768.py,
# ### 02:00:20Z); later keys given words as made. b767's kept below as CHAIN_WORDS_B767 (the carry having left them under b768's name), read
# ### by nothing
# ### b769, before the lock (the Edit tool, 2026-11-25): each key's words from its commit's subject (scratch chainchk769.py, 22:25:24Z),
# ### later keys given words as made; b768's kept below as CHAIN_WORDS_B768 (the carry having left them under b769's name), read by nothing
CHAIN_WORDS.update({'c1': 'the c1 route with b769`s findings after its lock and the navigator`s claims as events', 'c1pp': 'the corrigendum for b769',
                    'corr': 'the corrigendum banks and the corrigenda row (90)',
                    # ### b770, Component 4 (the Edit tool, while dispatch 8 builds): b770's keys, each from its commit's subject (scratch
                    # ### steps770s.py, 03:43:41Z), where the carry had left b769's; later keys given words as made
                    'k31_ctl': 'the planted control of [K31] committed before its run', 'price_foot': 'the record`s price-foot reader set to b770`s own foot',
                    'k31': '[K31] the kernel route for b770 at tools/standing/ v1.38.31', 'k31_row': '[K31]`s repairs row and its control banked',
                    'wl_k31': 'the worklist`s constants of [K31] and the corrigendum',
                    'k32_ctl': 'the planted control of [K32] committed before its run',
                    'k32': '[K32] the host`s folders masked at the source at tools/standing/ v1.38.32',
                    'k32_row': '[K32]`s repairs row and its control banked with defect (g)', 'wl_k32': 'the worklist`s constants of [K32]',
                    'k33_ctl': 'the planted control of [K33] committed before its run',
                    'k33': '[K33] the closing act held until its commit at tools/standing/ v1.38.33',
                    'k33_row': '[K33]`s repairs row, its control and the hook`s own control banked',
                    'wl_k33': 'the worklist`s constants of [K33], Component 1 complete',
                    'plan': 'the plan of (4)(a) committed before any dispatch', 'rulings_gen': 'the rulings tool for [A5] committed before its run',
                    'c2pp': '[A5] in OPEN_TRAILS', 'ledgers_c2': 'the ledgers of group c2 with events rows (59) to (63)',
                    'wl_c2': 'the worklist`s chain, the papers` repository`s chain and writes and the plan`s commit',
                    'controls_gen': 'the dispatch tool set from b768`s and committed before its first run',
                    'dispatch_1': 'events rows (64) and (65), the dispatch tool`s controls banked, the branch cut and pushed and dispatch 1 sent',
                    'li_index_gen': 'the index banks tool of (6) committed before its run',
                    'li_index_fix': 'the index banks tool`s needle of 5938 widened before its write',
                    'rulings_c2i': 'the rulings tool`s group c2i with the two index banks', 'c2ipp': '[I1] in OPEN_TRAILS',
                    'ledgers_c2i': 'the ledgers of group c2i', 'sitting_gen': 'the sitting tool of (7) committed before its run',
                    'sitting_fix': 'the sitting tool`s second shape given before its write',
                    'sitting': 'the sitting`s agenda, its one question put and passed whole, and the answers bank',
                    'rulings_c2s': 'the rulings tool`s group c2s with the inputs bank', 'c2spp': '[S5] in OPEN_TRAILS',
                    'wl_wwords': 'the (W) rows of the files of (4) after defect (h) with the ledgers of group c2s',
                    'rows_66_76': 'events rows (66) to (76) with defect (h), the dispatch rows and targets banks and the (W) bank',
                    'rows_77_81': 'events rows (77) to (81), dispatches 2 and 3 read',
                    'rulings_c3': 'the rulings tool`s group c3 with events rows (82) to (87) and the dispatch rows and targets banks',
                    'c3pp': '[Z1], [U1], [D1] and [L1] in OPEN_TRAILS',
                    'rulings_c4': 'the rulings tool`s group c4 with the worklist`s chain and kernel commits, rows (88) and (89) and the ledgers of group c3',
                    'read_8': 'dispatch 8 read with row (90) and the act module`s N2 section set', 'c4pp': '[C11] in OPEN_TRAILS',
                    'ledgers_c4': 'the ledgers of group c4 with [C11] entered and the dispatch tool`s bank, Component 4 complete',
                    'prelock': 'the act module`s pre-lock pass where b769`s forms stood under b770`s name',
                    'prelock_stubs': 'the act module`s carried stubs set from b769`s bodies and the step-zero bank`s two rows from the transcript',
                    'ceiling': 'the ceiling read before the lock, within the ceiling, with its four readers set to b768`s close',
                    'wl_ceiling': 'the worklist`s last constants before the lock with events rows (92) to (110) and defects (i) to (l)',
                    'scans': 'the address scan, the reproduction run and the orders bank with events rows (111) to (113) and defects (m) to (o)',
                    'tools_lock': 'the lock gate, the face and the probe-path tool carried and set before any run with events rows (114) to (116) and defects (p) to (r)',
                    'face_blocks': 'the face`s block file written for b770 in b769`s form with its twelve blocks, the (W) bank read from its table at 93 patterns and the worklist`s errata constants set empty, with events rows (117) to (122) and defect (s)',
                    'touch_sets': 'the touch read`s two sets, the worklist`s chain given step 66 with its words and events row (56)`s head given the guard reader`s words',
                    'critical_width': 'the touch read`s third set, the entry`s clause of (4)(c) given the term critical width and the criterion`s detection of the control as (R380)(4)(c) orders',
                    'touch_bank': 'the touch read of standing clauses v9 by hand, 64 rows each agreeing, the worklist`s chain given steps 67 and 68 with their words and the face`s block file carried to the touch bank, with events rows (123) to (129) and defects (t) and (u)',
                    'needle_calls': 'the needle calls, the entry 51 of 51, the trail 30 of 30, the touch bank`s foot and the touch read`s arm on the composed sources, the worklist`s chain given step 69 with its words and the face`s block file given it, with events row (130) and defect (v)',
                    'kernels_face': 'the probe-path refusal clear over 42373 tracked paths and the kernels face read by the record`s route, 24 kernels with main unmoved and no branch removed, with events row (131)',
                    'probe_act': 'the act part`s probe, 31 arms with 9 failing, each of b769`s ten at its second probe but the one withheld, a summary, the worklist`s chain given steps 70 and 71 with their words and the face`s block file given them, with events rows (132) and (133)',
                    'clone_main': 'standing-a1 with the kernel`s clone on the act`s branch, the clone switched to main and three markers of the worklist set to the ruling`s clauses with no value moving, with events row (134) and defect (w)',
                    'wl_markers': 'a fortieth summary, the worklist`s seven carried markers and its two standing lists set to the ruling and its chain given steps 72 and 73 with their words, with events rows (135) and (136)',
                    'probes_all': 'every part probed at 5b8d43c8 but the four held, 116 arms with 34 failing, b769`s 34 by name, a forty-first summary and the worklist`s chain given step 74 with its words, with events rows (137) and (138)',
                    'face_declared': 'the prelock print, the four held parts not run, the print again with twelve newly failing as b769`s, the cadence shown, the face given its declared arms and a forty-second summary, with events rows (139) and (140)',
                    'handoff': 'the handoff page written once by its tool',
                    'handoff_chain': 'the handoff page committed alone, the worklist given HANDOFF_COMMIT and the chain to 53a0a2e6 and a forty-third summary, with events rows (141) and (142)',
                    'record_banks': 'the four standing figures and the guard dry and the command bank by the record routes, G-DELETES-ONE-BRANCH read all true, the block file scope sentence and a forty-fourth summary, with events rows (143) and (144)',
                    'misses_set': 'the two arm misses set by the plan labels written without parentheses and defect h cite given its event, the block file defects line, floors sentence and Component 5 field given rows 145 to 150 and the worklist chain given step 79, with defects x and y and events rows (145) to (150)', 'n2_n3_repairs': 'N2 step-zero rows given the form its needles read and N3 control plants, side matcher table rows and premise matcher condition words set before the score dry runs again, the block file defects line, floors sentence and Component 5 field given rows 151 to 158 and the worklist chain given step 80, with defects z to d-prime and events rows (157) and (158)', 'prevdry_banks': 'the prev-mode dry banks of the six parts each SOURCES OK with their print CLEAR, standing-c by its second send after the host stopped its first and the author word on the stop, the score routes dry bank, the block file Component 5 field and the worklist chain given step 81, with events rows (159) to (162)', 'gate':'the gate commit with its subject composed by the one-call tool from its banks'})
CHAIN_WORDS_B768 = ({'c1': 'the c1 route with b769`s findings after its lock and the navigator`s claims as events', 'c1pp': 'the corrigendum for b769',
                    'corr': 'the corrigendum banks and the corrigenda row (88)', 'cites': 'the carried ferry cites and the corrigendum`s constants',
                    'k26_ctl': 'the planted control tool of [K26]', 'k26': '[K26] repaired at tools/standing/ v1.38.26',
                    'k26_row': '[K26]`s row and its planted control banked', 'k27_ctl': '[K27]`s control',
                    'k27': '[K27] repaired at tools/standing/ v1.38.27', 'k27_row': '[K27]`s row and its planted control banked',
                    'k28_ctl': '[K28]`s control', 'k28_ctl_fix': 'its scenario renamed before any banked run (defect (h))',
                    'k28': '[K28] repaired at tools/standing/ v1.38.28', 'k28_row': '[K28]`s row and its planted control banked',
                    'wl_c1': 'the worklist`s constants of the three keys', 'plan': 'the plan amended before any dispatch with the route for L9c`s datum',
                    'rulings_gen': 'the rulings tool for [R2] and [A3]', 'c2pp': '[R2] and [A3] in OPEN_TRAILS', 'ledgers_c2': 'the c2 ledger banks',
                    'controls_gen': 'the dispatch tool for (R380)', 'packed_gen': 'the packed data tool of the trial',
                    'packed_fix': 'its integer text limit lifted', 'controls_ns': 'the checks reading a qualified name by its namespaces',
                    'trial_sent': 'the trial at small size sent at dispatch 1', 'packed_full': 'the packed data tool given L9c1`s full mode',
                    'controls_opens': 'dispatch 1 read and the checks given a file`s opens (defect (k))',
                    'controls_graph': 'the import graph read in each header alone (defect (k))',
                    'trial_again': 'the trial at small size sent again at dispatch 2', 'rows71': 'the trial compiled and L9c1 sent at dispatch 3',
                    'rows74': 'dispatch 3 read and dispatch 4 sent', 'far_gen': 'the far data tool of L9c2', 'rows76': 'L9c2 generated and dispatch 5 sent',
                    'far_chunks': 'the far checks one chunk a declaration (defect (l))', 'rows79': 'the chunked checks and dispatch 6 sent',
                    'far_option': 'the option set before each doc comment', 'rows82': 'the far data files and dispatch 7 sent',
                    'rows84': 'dispatch 7 read and dispatch 8 sent', 'band_gen': 'the band data tool of L9c3',
                    'rows88': 'L9c2 compiled and L9c3 with archJ_comb sent at dispatch 9', 'rows91': 'L9c compiled and L11c sent at dispatch 10 (defect (m))',
                    'rows94': 'L11c compiled', 'arith_gen': 'the arithmetic data tool of L11d', 'arith_heart': 'its heartbeat option on the join',
                    'rows99': 'L11d and L12 sent at dispatch 11', 'arith_chains': 'the walk files chained two a lane (defect (n))',
                    'rows101': 'dispatch 12 sent', 'rulings_c5': 'the rulings tool`s group c5 for [P1]', 'c5pp': '[P1] in OPEN_TRAILS',
                    'ledgers_c5': 'the c5 ledger banks and the closing build sent',
                    'closing_stopped': 'the closing build stopped in part one and its repeat sent',
                    'rows109': 'the dispatch tool`s readers set (defect (p))', 'module_c5a': 'the act module`s checks and record sections set for b770',
                    'module_c5b': 'the act module`s composer, trail, report and texts set for b770', 'reproduce': 'the full reproduction run of (12) banked',
                    'wl_chains': 'the worklist`s chains, order and words, STEPZERO_BANKS and the licence reader set',
                    'lockgate_carry': 'the lock gate, the face and the probe-path tools carried and set for b770',
                    'closing_read': 'the closing build`s one repeat from source read exit 0, its axioms file equal to the restored run`s',
                    'rows_c4': 'the step rows for 4f354292 and 237a1fa0',
                    'main_tag': 'main moved to ffefddc6 by the gated push and v0.46 cut after main`s read-back',
                    'bank_orders': 'the dispatch tool`s bank and the orders bank',
                    'ceiling': 'the ceiling read before the lock, within the ceiling', 'misses2': 'the misses printed again before the lock',
                    'scan': 'the address scan banked and the entry`s two sentences on the stopped closing build set',
                    'module_c5c': 'the act module`s closing, record, checks and regspec sections set for b770',
                    'face_blocks': 'the face`s block file for b770 and the (W) bank regenerated from it',
                    'touch_set': 'the chain given the eleven commits after 4dbb48db, set at the touch read',
                    'touch': 'the touch bank by hand with rows 140 and 141 and the chain given fc0da1c2',
                    'needles': 'the needle calls with rows 142 and 143 and defect u and the face count set',
                    'probe_paths': 'the probe-path refusal and the kernels face banked and four worklist markers set before the probes',
                    'probe_fix': 'the act probe repairs of the two carried overrides and PP_WRITES with rows 147 to 150 and defects w to b-prime before the probe again',
                    'probes': 'the act part probe again and the standing parts probed with rows 151 to 153 and the face declared arms and the block file defects line set',
                   'handoff': 'the handoff page written once by its tool',
                   'handoff_chain': 'the worklist given HANDOFF_COMMIT and the chain to b25c6233',
                   'record_banks': 'the four standing figures and the guard dry and the command bank with rows 154 to 157 and the block file scope sentence and Component 5 field',
                   'chain_set': 'rows 158 to 160 and defect c-prime with the worklist chain given steps 89 to 91 and the handoff placed in the chain at its time',
                   'scores_set': 'the five score predicates set for b770 with defect d-prime and rows 161 to 164 and the worklist chain given e929ea65',
                   'closing_p1': 'the closing theorem clause read at P1 with the texts and the roster and defects d-prime and e-prime with rows 165 and 166 and the chain given 4683c04b',
                   'row167': 'row 167 after the score routes dry and the worklist chain given 3250e040',
                   'prevdry_labels': 'the prev-mode dry clear and the block file labels set without parentheses with its defects line and field and row 168',
                   'row169': 'row 169 after the face again and its bar call clear and the worklist chain given 4a594f36 and 35c92719',
                   'held_probes': 'the gate second run and the four held parts probe calls with defect f-prime and row 170 and the block file defects line',
                   'gate_third': 'rows 171 and 172 with the gate third run clear and the face as written with its bar call and the worklist chain given 9c877650 and d0f7045e',
                   'rows173': 'rows 173 and 174 with defect g-prime and the block file sentence set without its numeral and the face again with its bar call and the worklist chain given 914958a0',
                   'prevdry_banks': 'the prev-mode dry banks of the six parts this act runs and the score routes dry before the gate commit',
                   'gate': 'the gate commit with its subject composed by the one-call tool from its banks'})
CHAIN_WORDS_B767 = ({'c1': 'the c1 route with b769`s findings after its lock and the navigator`s claims as events', 'c1pp': 'the corrigendum for b769',
                    'corr': 'the corrigendum banks and the corrigenda row (87)',
                    'k25_ctl': 'the planted control tool of [K25]', 'price_foot': 'the record section reading the price table`s foot in b770`s form',
                    'k25': '[K25] repaired at tools/standing/ v1.38.25', 'k25_row': '[K25]`s row and its planted control banked',
                    'wl_c1': 'the worklist`s Component 1 constants',
                    'cert_gen': 'the certificate tool of the three forms of (4)(a)', 'cert_budget': 'its budget in the Lean by group',
                    'cert': 'the certificate banked and the plan amended before any dispatch',
                    'sbuild_gen': 'the read tool of the two stopped runs of (5)(a)', 'sbuild_route': 'its route in two parts within one run',
                    'sbuild': 'the build from source read and its route stated', 'reg': 'the registration of H-GRADED-WINDOW alone',
                    'window_gen': 'the window tool at graded knots', 'window_fix': 'its balls read back at 512 bits (defect (g))',
                    'window': 'the window read HELD, [G1]', 'rulings_gen': 'the rulings tool for [S1], [G1], [R1] and [A2]',
                    'c2pp': '[S1], [G1], [R1] and [A2] in OPEN_TRAILS', 'ledgers_c2': 'the c2 ledger banks',
                    'sbuild_closure': 'the source-build tool read over each target`s closure (defect (h))',
                    'sbuild_again': 'the source-build bank again and route (i) pushed at f6f60590',
                    'controls_gen': 'the dispatch tool for (R380)', 'controls_fix': 'its plants set to their series (defect (i))',
                    'trial_sent': 'its controls banked and the trial pair sent', 'rows67': 'L9a at dispatches 3 and 4',
                    'checks_closure': 'the checks given the kernel`s names against each file`s closure (defect (k))',
                    'checks_comments': 'the checks read past block comments (defect (l))', 'rows75': 'dispatch 5 broken and dispatch 6 compiled',
                    'logdata_gen': 'the prime table tool of L10', 'rows82': 'L10 whole at dispatch 7 and the trial read [S2]',
                    'checks_rfl': 'the checks reading rfl as an evaluation only as a proof (defect (m))',
                    'natdata_gen': 'the factor runs tool of L11b', 'natdata_fix': 'its plants read for the conjunct planted',
                    'natdata_depth': 'its runs under the recursion depth option (defect (n))', 'rows88': 'L11a whole and L11b at dispatches 9 and 10',
                    'rows92': 'L11b whole and L9b`s first two parts compiled', 'rows99': 'L9b`s third part compiled',
                    'closing_sent': 'L9b whole and the closing build sent at 89fd5b54',
                    'rulings_c5': 'the rulings tool`s group c5 for [P2] and [S2]', 'rulings_c5_e0': 'its E0 lexicon extended by the act`s two types',
                    'c5pp': '[P2] and [S2] in OPEN_TRAILS', 'ledgers_c5': 'the c5 ledger banks',
                    'lockgate_carry': 'the lock gate, the face and the probe-path tools carried and set, the branch`s base named',
                    'rows_c4': 'the step rows for 36b38f6f and 78a259ea',
                    'closing_read': 'the closing build from source read as wanted, main moved and v0.45 cut, the dispatch tool`s bank and the orders bank',
                    'module_readers': 'the act module`s carried readers set to b770, the reproduction banks and the scan bank',
                    'ceiling': 'the ceiling read before the lock, within the ceiling (defect (r))', 'misses2': 'the misses printed again before the lock',
                    'scan': 'the address scan banked and three of the entry`s sentences set', 'trail_set': 'the trail`s sentence on b769`s close set',
                    'face_blocks': 'the face`s block file for b770 and the (W) bank regenerated from it',
                    'touch_set': 'the seat`s price at graded knots in the entry and the record line, and the chain given the commits after 78a259ea, set at the touch read',
                    'touch_trail': 'the trail head`s proof branch given its own separator, set at the touch read',
                    'touch': 'the touch bank by hand, defects (s) to (u) and events rows (132) to (135)',
                    'needles': 'the needle calls on the entry, the trail and the touch bank`s foot, and the chain given the touch read`s commits',
                    'probe_act': 'the act part`s probe read, the helper of G-DERIVATION-GRADED set to the bank`s own commit (defect (v)) and two constants given their markers',
                    'probes': 'the parts probed, the pre-lock print and the face`s four declared arms (defect (w))'})
CHAIN_WORDS_B766 =({'c1': 'the c1 route with b769`s findings after its lock and the navigator`s claims as events', 'c1pp': 'the corrigendum for b769',
                    'corr': 'the corrigendum banks and the corrigenda row (86)',
                    'k22_ctl': 'the planted controls tool of the three repairs with [K22]`s control', 'ceil_check': 'the record section reading the ceiling after (4)(c) from its own bank',
                    'k22': '[K22] repaired at tools/standing/ v1.38.22', 'k22_row': '[K22]`s row and its planted control banked, push-b765-planted removed',
                    'k23_gen': 'the captures` mask tool and [K23]`s control', 'k23': '[K23] repaired at tools/standing/ v1.38.23',
                    'k23_row': 'b769`s eight captures masked, [K23]`s row and control banked', 'k24_ctl': '[K24]`s control',
                    'k24': '[K24] repaired at tools/standing/ v1.38.24', 'k24_row': '[K24]`s row and its planted control banked',
                    'cert_gen': 'the certificate tool of (4)(a)', 'cert': 'the certificate banked, [E1], and the plan',
                    'rulings_gen': 'the rulings tool for the lines of (6) and [E1]', 'c2pp': 'the lines of (6) and [E1] in OPEN_TRAILS',
                    'ledgers_c2': 'the c2 ledger banks', 'controls_gen': 'the dispatch tool of (4), its controls 24 of 24',
                    'wdata_gen': 'the window`s data file tool and dispatch 1`s banks', 'wdata': 'the window compiled at dispatch 2, [F2], and the ceiling after (4)(c)',
                    'rulings_c3': 'the rulings tool`s group c3 and dispatch 3`s banks', 'rulings_c3_fix': 'its names field closed by a comma',
                    'c3pp': '[F1] and [F2] in OPEN_TRAILS', 'ledgers_c3': 'the c3 ledger banks and dispatches 4 and 5',
                    'raise6': 'the K values row raised to 6 by the author`s word', 'kdata_gen': 'the K values` data tool of L6 (c)',
                    'kdata': 'its bank, dispatch 7 sent', 'cells_gen': 'the registry`s rows tool of (5)(a)', 'cells_fix1': 'its rows on protected lines cited by digest',
                    'cells_fix2': 'its titles read past a byte order mark', 'cells': '(5)(a) banked and the lean join tool of (5)(b)',
                    'cqdata_gen': 'the cQ data tool of L7', 'cqdata_fix': 'its plant at a leaf that stands once',
                    'raise8': 'the rows raised by the author`s word, the sweep tool and the (5)(b) banks', 'rulings_c4': 'the rulings tool`s group c4 and the sweep`s banks',
                    'rulings_c4_fix': 'its head`s apostrophes', 'c4pp': '[X1], [X2] and [X3] in OPEN_TRAILS', 'ledgers_c4': 'the c4 ledger banks and dispatch 9 read',
                    'rows81': 'L8 and dispatch 10', 'poledata_gen': 'the pole data tool of L8', 'poledata_fix': 'its import line and rewrite form (defect (k))',
                    'k0data_gen': 'the k(0) data tool of L9', 'rows87': 'L8 whole at dispatch 12 and L9 in part', 'k0blocks_gen': 'the k(0) tool`s four blocks (defect (l))',
                    'rows89': 'dispatch 13 stopped, dispatch 14 sent, the rulings tool`s group c5', 'rulings_c5_fix': 'its head`s plain wording',
                    'c5pp': '[P2] in OPEN_TRAILS as the author ratified it', 'ledgers_c5': 'the c5 ledger banks, dispatches 14 to 16 and the question',
                    'reproduce': 'the full reproduction run of (11) banked', 'lockgate_carry': 'the lock gate, the face and the probe-path tools carried, dispatch 16 and the author`s word banked',
                    'module_c5': 'the face`s constants and the first act module edits',
                    'chain_c5': 'the worklist given b770`s own chain, generators and order', 'module_rec': 'the act module`s record, trail, report, closing and checks sections for (R380) (defect (n))',
                    'scan': 'the address scan banked and three entry sentences set', 'trail_set': 'the trail composer`s three sentences',
                    'face_blocks': 'the face`s block file for b770, row (110) and the (W) bank',
                    'touch_set': 'four entry sentences the touch read found set before the record (defect (o))', 'touch': 'the touch bank, 57 rows',
                    'regcommit': 'the worklist`s REG_COMMIT read as no files by the checks sources (defect (p))',
                    'needle_arm': 'the arm`s needle call on the touch read passing', 'probe_act': 'the probe-path bank, the kernels face and the act part`s probe',
                    'wf_override': 'the workflow override reading b769`s entering main by name (defect (q)) and defect (r)',
                    'defect_s': 'defect (s) and the probes whole', 'face_declared': 'the face`s six declared arms and the needle calls on the entry and the trail'})
CHAIN_WORDS_B765 = ({'c1': 'the c1 route with b769`s findings after its lock and the navigator`s claims as events', 'c1pp': 'the corrigendum for b769',
                    'corr': 'the corrigendum banks', 'k20': '[K20] repaired at tools/standing/ v1.38.19', 'k20_row': '[K20]`s row and its planted control banked',
                    'k21': '[K21] repaired at tools/standing/ v1.38.20', 'k21_fix': '[K21]`s control set to read the act`s own handoff alone (defect (f))',
                    'k21_row': '[K21]`s row and its planted control banked', 'r4': 'tools/standing/ v1.38.21, the kernel route of (4)',
                    'r4_row': 'its planted control', 'controls_gen': 'the dispatch tool of (4) and (5)',
                    'controls_bank': 'its controls, the targets and dispatch 1 sent', 'window_gen': 'the window tool of (5)(c)',
                    'window': 'the window banked, PART TWO HELD', 'gate_gen': 'the gate tool of (5)(b)', 'gate_fix': 'its rule at twice the precision (defect (h))',
                    'gate': 'the gate banked, passing at both widths', 'held_gen': 'the held branches` tool of (6)(c)', 'held_fix': 'its mask`s control (defect (i))',
                    'held': 'the held branches banked', 'pi01_gen': 'the fetch tool of (6)(d)', 'pi01_rep': 'its route for one address once more',
                    'pi01': 'the reading of (6)(d) banked, one address not reached', 'map_gen': 'the map`s tool of (6)(b)', 'map': 'the map`s files banked',
                    'word': 'the author`s word on the runner`s cache banked', 'controls_word': 'the dispatch tool set for the word',
                    'premise_gen': 'the premise positions` tool of (6)(a)', 'premise_fix': 'its edge print widened', 'premise': 'the premise positions banked',
                    'rows45': 'dispatches 4 and 5 read', 'rows67': 'dispatch 6 read, steps 6 to 9 compiled and step 10 committed, dispatch 7 sent',
                    'rows8': 'dispatch 7 read, the lemma proved whole, the closing build from source sent', 'builder': 'the builder`s step of (7)', 'builder_ctl': 'its controls and the repository created',
                    'rulings_gen': 'the ledgers tool of (4)-(9)',
                    'rows9': 'dispatch 9 read, the pair as wanted and H-RUNNER-RESTORE HELD', 'rows9_step': 'its step row',
                    'controls_ms2': 'the dispatch tool given the second save on main by the author`s word',
                    'rows10': 'main moved and v0.44 cut, dispatch 10 stopped, the author`s word on the save on main banked',
                    'rows11': 'the dispatch tool`s controls 36 of 36 banked, dispatch 11 sent, the ledgers tool and the act module set',
                    'lockgate_carry': 'the lock gate, the face and the probe-path tools carried and set before any run',
                    'reproduce': 'the full reproduction run of (12) banked',
                    'module_c5': 'the act module set for the three words, the worklist given dispatch 11 among its runs and the face`s blocks file',
                    'trial': 'dispatch 11 read and the trial banked, the second save on main as wanted',
                    'ledgerspp': 'the lines of (4)-(9) and the author`s words of 2026-11-21 in OPEN_TRAILS',
                    'ledgers': 'the ledgers` banks and the roster'})
# ### the standing versions of the act, each (version, its commit, its controls bank, its cases): none at b761 ((R371)(11), tools/standing/
# ### tree-equal to b760's close, VERSION v1.37.1); b760's four kept under their own names for the carried readers
# ### b764, Component 5 (the Edit tool): the nineteen standing versions of (5) and (7), each (key, version, the version's commit, the commit
# ### carrying its row and its control, the control's verdict line in data/b764_repair_controls.txt), read from data/b764_repairs.txt and the
# ### step rows (scratch files764.py, 22:5xZ); [K19] READ AS DESIGNED moves none; each control's foot "[K] THE CONTROL AS WANTED: THE FAULT
# ### READ BEFORE AND CLEAN AFTER: True." at its line
# ### b765, Component 5 (the Edit tool): the three standing versions of (8) and (4), each (key, version, the version's commit, the commit
# ### carrying its row and its control, the control's verdict line in data/b765_repair_controls.txt), read from data/b765_repairs.txt, the
# ### controls bank's feet and the step rows (scratch steprows765.py, 15:3xZ); [R4] has no row in the repairs bank, its control alone, as
# ### b764's [R7]
STANDING_REPAIRS = (('[K31]', 'v1.38.31', '60e769a5', '99a723a1', 26), ('[K32]', 'v1.38.32', '75a8c747', '4f318345', 49), ('[K33]', 'v1.38.33', '9432d7ce', '0e99a945', 70))   # ### b770 (R380)(8): [K31] (steps 16-17), [K32] (steps 20-21), [K33] (steps 24-25); [K32] and [K33] appended as made, three commits of tools/standing/, each (key, version, commit, the commit carrying its row and its control, the control's verdict line in data/b770_repair_controls.txt), set as made
STANDING_REPAIRS_B769 = (('[K29]', 'v1.38.29', '48ccc5c7', '28be31c6', 32), ('[K30]', 'v1.38.30', '84333f27', 'b2982d66', 53))   # ### b769 (R379)(8): [K29] (steps 10-11, Component 1) and [K30] (steps 20-21, Component 2, after (4)(b)'s control read as wanted), two commits of tools/standing/; each (key, version, commit, the commit carrying its row and its control, the control's verdict line in data/b769_repair_controls.txt), b768's form
STANDING_REPAIRS_B768 = (('[K26]', 'v1.38.26', '70aefe23', 'ec61c120', 31), ('[K27]', 'v1.38.27', '690c4238', 'b5e8b01c', 62),
                    ('[K28]', 'v1.38.28', 'a7d37ec2', 'ea46d65a', 81))   # ### b768 (R378)(8): [K26], [K27] and [K28], each (key, version, commit, the commit carrying its row and its control, the control's verdict line in data/b768_repair_controls.txt), read from the step rows (steps 10-11, 13-14, 17-18) and the controls bank's feet
STANDING_REPAIRS_B767 = (('[K25]', 'v1.38.25', '374c1e80', '2a128592', 31),)   # ### b767 (R377)(8): [K25] alone, (key, version, commit, the commit carrying its row and its control, the control's verdict line) (steps 11 and 12)
STANDING_REPAIRS_B766 = (('[K22]', 'v1.38.22', 'b7c3ed87', '4e6d52ce', 31), ('[K23]', 'v1.38.23', 'd91f1093', 'd09d93ab', 43),
                    ('[K24]', 'v1.38.24', '751b9e7a', 'd4b10aa0', 67))   # ### b766 step zero, (R376)(7), (8): the keys [K22], [K23] and [K24] in place of [K20] and [K21], each (key, version, commit, the commit carrying its row and its control, the control's verdict line) set as made
STANDING_REPAIRS_B765 = (('[K20]', 'v1.38.19', 'e179b18b', '15e75494', 16), ('[K21]', 'v1.38.20', '899f2767', 'bcf47fa6', 28),
                         ('[R4]', 'v1.38.21', 'c2df59d7', '45fc9622', 50))   # ### b765's three, kept beside
STANDING_REPAIRS_B764 = ()   # ### b764's nineteen stand in git at tools/b764_worklist.py
REPAIRS_BANK = 'data/b770_repairs.txt'
REPAIR_CONTROLS_BANK = 'data/b770_repair_controls.txt'
STANDING_BANKS = ()   # ### b764: no version bank in the v-foot form; the versions and their controls stand in STANDING_REPAIRS
STANDING_BANKS_B763 = (('v1.37.2', 'd34f7323', 'data/b763_standing_v1372.txt', 10),)   # ### b763's (R373)(5), kept for the carried readers. b766 step zero: the three tuples' paths set to the banks' own names, as data/ holds them (the carries of b764, b765 and b766 had shifted each to the carrying act's name, data/b766_carry_worklist.txt :61-:70)
STANDING_BANKS_B760 = (('v1.36.8', '34390a25', 'data/b760_standing_v1368.txt', 9), ('v1.36.9', '1e9493e5', 'data/b760_standing_v1369.txt', 9),
                       ('v1.37.0', 'a8f8403a', 'data/b760_standing_v1370.txt', 10), ('v1.37.1', '6bc5d706', 'data/b760_standing_v1371.txt', 9))   # ### b760's (R370)(5)(i)-(iv), read not re-made
STANDING_BANKS_B759 = (('v1.36.3', '983ca5b1', 'data/b759_standing_v1363.txt', 10), ('v1.36.4', '4622b017', 'data/b759_standing_v1364.txt', 6),
                       ('v1.36.5', '34452b1a', 'data/b759_standing_v1365.txt', 5), ('v1.36.6', '8fc653fc', 'data/b759_standing_v1366.txt', 5),
                       ('v1.36.7', 'cd45450e', 'data/b759_standing_v1367.txt', 9))   # ### b759's five, read not re-made, under their own names (the carry had shifted them)
STANDING_BANKS_B758 = (('v1.35.6', 'ac6a0a77', 'data/b758_standing_v1356.txt', 11), ('v1.35.7', '248cacb8', 'data/b758_standing_v1357.txt', 16),
                       ('v1.35.8', 'ed0d3f33', 'data/b758_standing_v1358.txt', 7), ('v1.35.9', 'da79951c', 'data/b758_standing_v1359.txt', 8),
                       ('v1.36.0', 'fd45f4c5', 'data/b758_standing_v1360.txt', 10), ('v1.36.1', '9bc8cfeb', 'data/b758_standing_v1361.txt', 11),
                       ('v1.36.2', '4db55035', 'data/b758_standing_v1362.txt', 6))   # ### b758's seven, read not re-made, under their own names
# ### the kernel commits of the act, read by N5 and G-OFFSET-POST-HOC: (key, kernel, commit, the branch it stands on at the close).
# ### ### b764, Component 3 (the Edit tool, defect (f)): b764's one, by the one-call tool on push-b764-runner made at main 819e4a83 ((R374)(7));
# ### its branch set to main where the trial's success moves main to it. b763's six stand below as KERNEL_COMMITS_B763 under the branch
# ### names the remote holds (push-b763-arith, push-b763-keiper), which the carry had shifted to push-b764-*.
# ### b765, Component 5 (the Edit tool): the act's eight kernel commits on push-b765-centre, cut from push-b764-runner at 38a57e02 ((R375)(4)),
# ### and the planted commit on push-b765-planted, each by the one-call tool and pushed alone by the gated branch mode, read back (step rows)
# ### b767, Component 4 (the Edit tool, before any run): the act's fifteen kernel commits on push-b767-proof, cut from push-b766-proof at
# ### 3c67b8b5 ((R377)(4)), each by the one-call tool and pushed alone by the gated branch mode, read back (the step rows, scratch
# ### steps767r.py, 18:49:19Z); the branch each stands on at the close, push-b767-proof, set to main where the closing build moves main
# ### b768, Component 4 (the Edit tool, 2026-11-25, while dispatch 13 builds; readers searched first by the Grep tool: checks 35, the
# ### record's sections and one line each of checks.tpl and record.tpl): the act's fourteen kernel commits on push-b768-proof, cut from
# ### push-b767-proof at 89fd5b54 ((R378)(4)), each by the one-call tool and pushed alone by the gated branch mode, read back (git log
# ### 89fd5b54..push-b768-proof, 00:41:57Z); the branch each stands on at the close push-b768-proof, as b767's stood on push-b767-proof
# ### b770, Component 4 (the Edit tool, while dispatch 8 builds): the act's seven kernel commits on push-b770-proof, cut from push-b768-proof
# ### at ffefddc6 ((R380)(4)), each by the one-call tool and pushed alone by the gated branch mode, read back (the step rows, scratch
# ### steps770s.py, 03:43:41Z); the branch each stands on at the close push-b770-proof, as b768's stood on push-b768-proof
KERNEL_COMMITS = (('b', 'SIDE-explicit-formula', '1b413384', 'push-b770-proof'),       # ### (4)(b) FromCoefficients.lean (step 33, 01:11:50Z), dispatch 1 KERNEL
                  ('c', 'SIDE-explicit-formula', 'f5e2cec9', 'push-b770-proof'),       # ### (4)(c) SupportPositivity.lean (step 45, 02:01:30Z), refused ahead of a send by the Lean text check
                  ('c_fix', 'SIDE-explicit-formula', 'c8913190', 'push-b770-proof'),   # ### the compact support by an obtain pattern (step 47, 02:09:48Z), dispatch 2 KERNEL
                  ('d', 'SIDE-explicit-formula', '5e1c7b72', 'push-b770-proof'),       # ### (4)(d) Composition.lean (step 48, 02:21:04Z), dispatch 3 KERNEL
                  ('e', 'SIDE-explicit-formula', '97d7285b', 'push-b770-proof'),       # ### (4)(e) Window/CQLeast.lean (step 50, 02:35:53Z), dispatch 4 KERNEL
                  ('f', 'SIDE-explicit-formula', 'b34fdb2e', 'push-b770-proof'),       # ### (4)(f) Schema/ZQ/OffZero/Located.lean (step 51, 02:53:15Z), dispatch 5 KERNEL
                  ('g', 'SIDE-explicit-formula', 'cc2f3ba8', 'push-b770-proof'))       # ### (4)(g) Schema/ZQ/RealAxis.lean, the closing Lean commit (step 53, 03:05:11Z), dispatch 6 KERNEL, the closing build 7 and its repeat 8
KERNEL_COMMITS_B769 = ()   # ### LEFT EMPTY BY (R379)(12): no kernel touched; b769 (R379)(9), (12), N5: no kernel commit at this act
KERNEL_COMMITS_B768 = (('trial', 'SIDE-explicit-formula', 'd4c8c173', 'push-b768-proof'),        # ### (4)(a) the trial at small size: Packed and PackedTrial (step 27, 16:17:51Z), refused ahead of a send
                  ('trial_fix', 'SIDE-explicit-formula', 'e0baa667', 'push-b768-proof'),    # ### Packed set (step 29, 16:29:40Z), dispatch 1 BREAKS (abs_mul)
                  ('trial_import', 'SIDE-explicit-formula', '6d93bd31', 'push-b768-proof'), # ### Packed given Ring.Abs, PackedJoin (step 34, 17:16:56Z), dispatch 2 KERNEL
                  ('l9c12', 'SIDE-explicit-formula', 'b7198735', 'push-b768-proof'),        # ### (4)(b) L9c1's seven files, FarLags, FarClosed, FarKernel (step 36, 17:50:07Z), dispatch 3 BREAKS
                  ('wincheck', 'SIDE-explicit-formula', '49ccee24', 'push-b768-proof'),     # ### fG_zero set, WinCheck (step 38, 18:19:58Z), dispatch 4 BREAKS
                  ('l9c2', 'SIDE-explicit-formula', 'b64dfeb6', 'push-b768-proof'),         # ### L9c2's data, FarWin, FarComb (step 41, 18:43:01Z), dispatch 5 STOPPED UNDER THE HOLD
                  ('l9c2_chunks', 'SIDE-explicit-formula', 'cf3cf10f', 'push-b768-proof'),  # ### one chunk a declaration (step 44, 19:10:40Z), dispatch 6 BREAKS
                  ('l9c2_option', 'SIDE-explicit-formula', '9dd90f3d', 'push-b768-proof'),  # ### the option before each doc comment (step 47, 19:39:27Z), dispatch 7 BREAKS
                  ('l9c2_comb', 'SIDE-explicit-formula', 'ada0678e', 'push-b768-proof'),    # ### far_pair and far_comb set (step 49, 20:04:58Z), dispatch 8 KERNEL, L9c2 compiled
                  ('l9c', 'SIDE-explicit-formula', '17db013f', 'push-b768-proof'),          # ### L9c3 the band and L9c archJ_comb (step 52, 21:03:17Z), dispatch 9 KERNEL
                  ('l11c', 'SIDE-explicit-formula', '2f920d64', 'push-b768-proof'),         # ### (4)(c) L11c arith_eq_comb (step 54, 21:33:32Z), refused ahead of a send
                  ('l11c_fix', 'SIDE-explicit-formula', '9b2a69e0', 'push-b768-proof'),     # ### the projection taken apart (step 55, 21:37:57Z), dispatch 10 KERNEL
                  ('l11d_l12', 'SIDE-explicit-formula', 'e204ee77', 'push-b768-proof'),     # ### (4)(d), (e) L11d and L12 with the walk's data (step 60, 23:13:55Z), dispatch 11 STOPPED UNDER THE HOLD
                  ('l11d_chains', 'SIDE-explicit-formula', 'ffefddc6', 'push-b768-proof'))  # ### the walk files chained two a lane, the closing Lean commit (step 63, 23:48:05Z), dispatch 12 KERNEL, [P1]
KERNEL_COMMITS_B767 = (('route', 'SIDE-explicit-formula', 'f6f60590', 'push-b767-proof'),          # ### (5)(c): route (i) in the workflow, the act's opening Lean commit (step 28, 12:24:00Z)
                  ('archj', 'SIDE-explicit-formula', 'efd46832', 'push-b767-proof'),          # ### (4)(b) L9a: ArchJ.lean (step 33, 13:18:28Z)
                  ('archj2', 'SIDE-explicit-formula', '2e7caf01', 'push-b767-proof'),         # ### (4)(b) L9a: ArchJ2.lean, archJ_eq_double (step 34, 13:36:41Z)
                  ('archj3', 'SIDE-explicit-formula', '1f0e9edb', 'push-b767-proof'),         # ### (4)(b) L9b: ArchJ3.lean (step 36, 14:04:07Z), broke at dispatch 5
                  ('archj3_fix', 'SIDE-explicit-formula', '6cf6e87b', 'push-b767-proof'),     # ### ArchJ3 repaired (step 38, 14:30:48Z)
                  ('logs', 'SIDE-explicit-formula', 'caa7b338', 'push-b767-proof'),           # ### (4)(c) L10: LogData, LogBounds, LogConst (step 42, 15:17:33Z)
                  ('polecomb', 'SIDE-explicit-formula', '356e1cfb', 'push-b767-proof'),       # ### (4)(d) L11a: PoleComb.lean (step 44, 15:37:52Z)
                  ('lognat', 'SIDE-explicit-formula', 'f7a292e4', 'push-b767-proof'),         # ### (4)(d) L11b: LogNatBase, LogNatData, LogNat (step 48, 15:59:08Z), broke at dispatch 9
                  ('lognat_fix', 'SIDE-explicit-formula', 'ed88b486', 'push-b767-proof'),     # ### L11b's data under the recursion depth option (step 50, 16:10:50Z)
                  ('archpiece', 'SIDE-explicit-formula', 'a0a70ac6', 'push-b767-proof'),      # ### (4)(b) L9b part (i): ArchPiece.lean (step 52, 16:31:04Z)
                  ('archband', 'SIDE-explicit-formula', '7f3749c4', 'push-b767-proof'),       # ### L9b part (ii): ArchBand.lean (step 53, 16:44:36Z)
                  ('archclosed', 'SIDE-explicit-formula', '7d8b45c6', 'push-b767-proof'),     # ### L9b part (iii): ArchClosed.lean (step 55, 17:13:48Z)
                  ('archlam', 'SIDE-explicit-formula', '1fe55606', 'push-b767-proof'),        # ### L9b part (iv): ArchLam.lean (step 57, 17:38:11Z)
                  ('archbasis', 'SIDE-explicit-formula', '3e7710f9', 'push-b767-proof'),      # ### L9b whole: ArchBasis.lean, archJ_basis (step 58, 17:50:04Z)
                  ('archbandlocal', 'SIDE-explicit-formula', '89fd5b54', 'push-b767-proof'))  # ### L9b in the plan's form: ArchBandLocal.lean, the closing Lean commit (step 59, 18:06:20Z)
KERNEL_COMMITS_B766 = (('prime', 'SIDE-explicit-formula', '48d151e3', 'push-b766-proof'),    # ### b766 Component 3: the act's kernel commits of (R376)(4), on push-b766-proof cut from main at 0ba9cd61, each set when made. (4)(b) L1 (step 23, 09:42:43Z)
                  ('window', 'SIDE-explicit-formula', 'd814154e', 'push-b766-proof'),   # ### (4)(c): the data file, the spline and the instance (step 25, 10:07:04Z)
                  ('kvalues', 'SIDE-explicit-formula', 'a6328fbe', 'push-b766-proof'),  # ### (4)(d) L6 (a): the autocorrelation at log n as an integral (step 27, 10:28:34Z)
                  ('kbasis', 'SIDE-explicit-formula', '0f9d9f7e', 'push-b766-proof'),   # ### (4)(d) L6 (b): the integral in the B-spline basis (step 31, 10:46:40Z), broke at dispatch 4
                  ('kbasis2', 'SIDE-explicit-formula', '6b4a67ab', 'push-b766-proof'),  # ### (4)(d) L6 (b) repaired: le_or_gt for le_or_lt (step 32, 10:57:16Z)
                  ('kappa', 'SIDE-explicit-formula', '1848e7c0', 'push-b766-proof'),    # ### (4)(d) L6 (b): kappa in closed form, 5040 n^4 kappa an integer double sum (step 34, 11:18:35Z); dispatch 6 refused by the row's priced 3, raised to 6 by the author's word (11:56:45Z)
                  ('kvalues', 'SIDE-explicit-formula', '448dd77b', 'push-b766-proof'),    # ### (4)(d) L6 (c): KData.lean by tools/b766_kdata.py (13:07:48Z) and KFast.lean, the values K(n) by the recurrence of F and halving sums (step 37, 13:23:25Z)
                  ('cqvalues', 'SIDE-explicit-formula', 'edc05812', 'push-b766-proof'),   # ### (4)(d) L7: CQData.lean by tools/b766_cqdata.py (14:40:02Z) and CQValues.lean, cQ to 1023 as the combination the data holds (step 45, 14:40:55Z)
                  ('cqrepair', 'SIDE-explicit-formula', '5e9ab5d1', 'push-b766-proof'),
                  ('pole', 'SIDE-explicit-formula', '5266fb0a', 'push-b766-proof'),
                  ('poledata', 'SIDE-explicit-formula', '1d3b1bdf', 'push-b766-proof'),
                  ('polerepair', 'SIDE-explicit-formula', 'c6a46950', 'push-b766-proof'),
                  ('arch', 'SIDE-explicit-formula', '9a389982', 'push-b766-proof'),
                  ('archblocks', 'SIDE-explicit-formula', '3c67b8b5', 'push-b766-proof'))   # ### (4)(d) L9 in part, the strided sum at 1 in four blocks after dispatch 13 stopped under the hold (step 62, 16:55:11Z); L9 in part, the archimedean term by Gauss's integral and k(0) as data (step 59, 16:39:02Z); L8's data half repaired, the data file given its import (step 57, 16:30:54Z); L8's data half, the integral of the spline as intH (step 55, 16:21:24Z); L8 the pole term in the B-spline basis (step 52, 16:02:28Z); L7 repaired by the author's word of 15:20Z (words :26): the box replaced by a check over natural indices (step 47, 15:33:36Z)
KERNEL_COMMITS_B765 = (('workflow', 'SIDE-explicit-formula', '70c50d37', 'push-b765-centre'),     # ### b765's nine, kept beside under the names the kernel's refs hold (b766 step zero: the carry had shifted them to push-b766-*). (4): the key by toolchain, manifest and commit; the restore by the prefix (step 16, 11:26:26Z)
                       ('statement', 'SIDE-explicit-formula', 'd540bc98', 'push-b765-centre'),    # ### (5)(a): ControlFailureExists (step 17, 11:29:43Z)
                       ('gauss_statement', 'SIDE-explicit-formula', 'a8c2eddc', 'push-b765-centre'),   # ### (5)(b): GaussArchQ, the statement apart (step 26, 12:37:55Z)
                       ('planted_input', 'SIDE-explicit-formula', 'e83e0deb', 'push-b765-centre'),     # ### the word's (i): the workflow's planted input (step 36, 13:19:12Z)
                       ('steps14', 'SIDE-explicit-formula', '7cbc7143', 'push-b765-centre'),       # ### (5)(b) steps 1-4 (step 41, 13:58:01Z)
                       ('step5', 'SIDE-explicit-formula', '390cddef', 'push-b765-centre'),         # ### step 5, digamma_integral (step 42, 14:10:06Z)
                       ('steps69', 'SIDE-explicit-formula', '5222cd88', 'push-b765-centre'),       # ### steps 6-9, bracketQ_eq (step 44, 14:35:33Z)
                       ('step10', 'SIDE-explicit-formula', '0ba9cd61', 'main'),        # ### step 10, gaussArchQ: the closing Lean commit (step 45, 15:00:59Z), main moved to it at v0.44
                       ('planted', 'SIDE-explicit-formula', '7d86a245', 'push-b765-planted'))      # ### (4)(a): SquaresAt24.lean's closing theorem made false (step 19, 11:47:03Z)
KERNEL_COMMITS_B764 = (('runner', 'SIDE-explicit-formula', '38a57e02', 'push-b764-runner'),)   # ### b764's (R374)(7) workflow change alone, kept beside (b766 step zero: the carry's push-b765-runner set back)
KERNEL_COMMITS_B763 = (('form13', 'SIDE-explicit-formula', 'ec82fed0', 'main'),       # ### (R373)(6) (S1)-(S3) and [P1]'s six names (20:32:07Z, step 16), on main at v0.42
                       ('form45', 'SIDE-explicit-formula', '0f849552', 'main'),       # ### (S3)'s import repaired, (S4) and (S5) (21:52:14Z, step 21), on main at v0.42
                       ('statement', 'SIDE-explicit-formula', '4964e957', 'main'),    # ### the statement file by the author's word (23:51:12Z, step 28), main at v0.42 (02:22:05Z)
                       ('arith', 'SIDE-explicit-formula', 'ec14e9d9', 'push-b763-arith'),   # ### (R373)(7)'s statement, no proof (02:28:20Z, step 36), on its branch (b765, Component 5: the carry's push-b764-arith set back)
                       ('squares', 'SIDE-explicit-formula', '819e4a83', 'main'),   # ### (R373)(8) W-ORD-SQUARES-AT-24 (03:48:55Z, step 47), on push-b763-squares; main moved to it at v0.43 after run 44670834879's success (05:34Z)
                       ('keiper', 'SIDE-explicit-formula', 'a59632eb', 'push-b763-keiper'))     # ### (b765, Component 5: the carry's push-b764-keiper set back) (R373)(8) W-ORD-KEIPER-FACE, a first file (04:23:03Z, step 53), on its branch made at main 4964e957; the order not built in full, so main does not move to it
KERNEL_COMMITS_B762 = ()   # ### b762 made none ((R372)(12))
KERNEL_COMMITS_B759 = (('prints', 'SIDE-explicit-formula', 'ddb3efb9', 'main'),   # ### (R369)(5) commit one: the four print lines, on main at v0.41
                       ('weil', 'SIDE-explicit-formula', 'a3aad4cc', 'main'))     # ### (R369)(5) commit two: zq_weil_positivity_fails, main at v0.41
KERNEL_COMMITS_B758 = (('rename', 'SIDE-explicit-formula', 'd1afb4fc', 'main'), ('merge', 'SIDE-explicit-formula', '630cba16', 'main'))   # ### b758's two, on main at v0.39 and v0.40
WEIL_BRANCH = ('push-b770-proof', 'cc2f3ba872c1103a5fe7226de77d5ac84ce160d2')   # ### b770 step zero, (R380)(4), (9): the act's Lean branch, cut from push-b768-proof at ffefddc6, which is main; [1] its tip, the closing Lean commit cc2f3ba8 (step 53), pushed and read back at the remote (03:08:13Z), set at Component 4 (the Edit tool, 2026-11-27, the dispatch tool reading [0] and WEIL_BRANCH_BASE alone)
WEIL_BRANCH_B769 = ('push-b768-proof', 'ffefddc61b05fcca089ff20cc8cd2f103dd0a5f1')   # ### b769 step zero, (R379)(9): no Lean branch cut at this act; push-b768-proof, the kernel's branch read at ffefddc6 at the close and written by nothing
WEIL_BRANCH_B768 = ('push-b768-proof', 'ffefddc61b05fcca089ff20cc8cd2f103dd0a5f1')   # ### b768 step zero, (R378)(4), (9): the act's Lean branch, cut from push-b767-proof at 89fd5b54, which is main; [1] its tip, the closing Lean commit ffefddc6 (step 63), pushed and read back at the remote (23:52:51Z), set at Component 4 (the Edit tool, 2026-11-25, the dispatch tool reading [0] and WEIL_BRANCH_BASE alone, data/b768_events.txt (106))
WEIL_BRANCH_B767 = ('push-b767-proof', '89fd5b54941b246d707bd2e9708a8a24e222ba5c')   # ### b767 step zero, (R377)(4), (9): the act's Lean branch, cut from push-b766-proof at 3c67b8b5 and not from main; its tip the closing Lean commit 89fd5b54 (step 59), pushed and read back at the remote (18:06:41Z), set at Component 4 (data/b767_events.txt (111)); push-b766-proof read at 3c67b8b5 (18:43:43Z)
WEIL_BRANCH_BASE = 'ffefddc61b05fcca089ff20cc8cd2f103dd0a5f1'   # ### b770 step zero, (R380)(9): the act's Lean branch's base, push-b768-proof's commit ffefddc6 (main and v0.46), named apart from the tip
WEIL_BRANCH_BASE_B769 = 'ffefddc61b05fcca089ff20cc8cd2f103dd0a5f1'   # ### b769 step zero: SIDE-explicit-formula's main entering (v0.46), no branch cut from it
WEIL_BRANCH_BASE_B768 = '89fd5b54941b246d707bd2e9708a8a24e222ba5c'   # ### b768 step zero, (R378)(9): the act's Lean branch's base, push-b767-proof's commit 89fd5b54 (main and v0.45), named apart from the tip
WEIL_BRANCH_BASE_B767 = '3c67b8b58d6f323b1db62249a77453963368aaf7'   # ### b767 Component 4 (data/b767_events.txt (111)): the act's Lean branch's base, push-b766-proof's commit 3c67b8b5, which tools/b767_controls.py read as WEIL_BRANCH[1] (BASE_PROOF, its checks' diff and the base's workflow) while WEIL_BRANCH[1] held the base; WEIL_BRANCH[1] now the tip, as b766's carried readers in tools/acts/b767.py take it, and the base read here
WEIL_BRANCH_B766 = ('push-b766-proof', '3c67b8b58d6f323b1db62249a77453963368aaf7')   # ### b766 step zero, (R376)(4), (8): the act's Lean branch, cut from main at 0ba9cd61 and not from a runner's branch; its tip the closing Lean commit 3c67b8b5 (step 62), kept at the remote and in the clone by the author's word (data/b766_author_words_preseal.txt :32)
WEIL_BRANCH_B765 = ('push-b765-centre', '0ba9cd61e1a071446fd366896c710ae13356bf3e')   # ### b765's, kept at its tip, local and remote (b766 step zero: the carry had shifted its name; b767, Component 4: shifted again by b767's carry to push-b766-centre and set back to the name the kernel's refs hold, for-each-ref 19:06:14Z, with the four constants of b765 beside it). b765 (R375)(4): the act's Lean branch, cut from push-b764-runner at 38a57e02 by the one-call tool (11:21:41Z), its tip the closing Lean commit 0ba9cd61 (step 45), pushed alone by the gated branch mode and read back (15:01:21Z)
PLANTED_BRANCH = ('', '')   # ### b770 step zero, (R380)(4): no planted build ordered at this act, so no planted branch
PLANTED_BRANCH_B769 = ('', '')   # ### b769 step zero: no planted build, so no planted branch
PLANTED_BRANCH_B768 = ('', '')   # ### b768 step zero, (R378)(4): no planted build ordered at this act, so no planted branch
PLANTED_BRANCH_B767 = ('', '')   # ### b767 step zero, (R377)(4): no planted build ordered at this act, so no planted branch
PLANTED_BRANCH_B766 = ('push-b765-planted', '7d86a2459d167673252372a46185329b33f25970')   # ### b766 step zero, (R376)(7) [K22]: b765's planted branch, which this act removes at the kernel's remote and in its clone (the carry had shifted its name to push-b766-planted); (R376)(4) orders no planted build. b765 (R375)(4)(a): cut at d540bc98 (11:46:03Z), its one commit 7d86a245 (step 19), pushed alone and read back (11:47:22Z); the local branch deleted before the lock where the route allows, the remote kept and named in the closing message
WEIL_BRANCH_B764 = ('push-b764-runner', '38a57e02074a22eebbf33c6ff9ce5c7e58335d4a')   # ### b764's (R374)(7), kept at its tip, local and remote (b766 step zero: the carry's push-b765-runner set back)
WEIL_TAG = None   # ### LEFT EMPTY BY (R380)(4): "Where the build and its repeat each stop under the hold, [C11] is entered, main is not moved and no tag is cut." Both stopped at cc2f3ba8 (runs 45933637198 and 45935483550), [C11] at OPEN_TRAILS :19611; v0.39 to v0.46 and v0.2.0 peeling as before at the close (N5)
WEIL_TAG_B769 = None   # ### LEFT EMPTY BY (R379)(12): no tag cut or moved; b769 N5: v0.39 to v0.46 and v0.2.0 peeling as before at the close
WEIL_TAG_B768 = ('v0.46', '56a00b6511e29d15c3440aa2ae47d9656bf7796a', 'ffefddc61b05fcca089ff20cc8cd2f103dd0a5f1')   # ### b768 (R378)(4), Component 4 (the Edit tool, 03:1xZ): v0.46 cut by the gated push after main`s read-back at ffefddc6, on run 45521560784 with the restore off and on no other; (name, object, peel), the peel read back at the remote equal (data/b768_SIDE-explicit-formula_push-b768-proof_push_out.txt, 03:10:3xZ); its readers the act module`s regspec override :627, checks 34 :1278, checks 35 :1344-:1348, the kernels line :2111 and the arm at :2641
WEIL_TAG_B767 = ('v0.45', 'dbfa7b876440bae2413e04b63babbc109dda466a', '89fd5b54941b246d707bd2e9708a8a24e222ba5c')   # ### b767 (R377)(4), Component 4 (the Edit tool): v0.45 cut by the gated push after main`s read-back at 89fd5b54, on run 45236921224 with the restore off and on no other; (name, object, peel), the peel read back at the remote equal (data/b767_SIDE-explicit-formula_push-b767-proof_push_out.txt, 20:19:4xZ). b766's words: LEFT EMPTY BY (R376)(4): no tag cut -- the closing build from source and its repeat each stopped under the hold, no axioms file printed, main not moved and no [C7] by the author's word (data/b766_author_words_preseal.txt :32); the ceiling v0.45 unreached
WEIL_TAG_CEILING = 'v0.47'   # ### (R380)(9): in place of v0.46
WEIL_TAG_CEILING_B769 = 'v0.46'   # ### (R379) N5: no tag beyond v0.46
WEIL_TAG_CEILING_B768 = 'v0.46'   # ### (R378)(9): in place of v0.45
WEIL_TAG_CEILING_B767 = 'v0.45'   # ### (R376)(8): in place of v0.44
WEIL_TAG_B765 = ('v0.44', 'bd0248375a7930985f6b18886b6af5a9b125fa27', '0ba9cd61e1a071446fd366896c710ae13356bf3e')   # ### b765's, kept beside. b765 (R375)(4): v0.44 cut under HELD by the gated push after main's read-back at 0ba9cd61, on run 44918855502 with the restore off and on no other; (name, object, peel), the peel read back at the remote equal
WEIL_TAG_B764 = None   # ### b764 cut none
RUNNER_COMMIT = 'cc2f3ba872c1103a5fe7226de77d5ac84ce160d2'   # ### b770 (R380)(4): the act's closing Lean commit, the last at which a restored build read exit 0 (dispatch 6, run 45933086394), set at Component 4
RUNNER_COMMIT_B769 = ''   # ### LEFT EMPTY BY (R379)(12): no kernel touched and no dispatch sent, so no Lean written, no build and no runner commit
RUNNER_COMMIT_B768 = 'ffefddc61b05fcca089ff20cc8cd2f103dd0a5f1'   # ### b768: the act's closing Lean commit, the last at which a restored build read exit 0 ((R378)(4)): ffefddc6 (step 63), dispatch 12, run 45514975816, axioms sha256 2a9e26774e7e0c96 (data/b768_events.txt (103)); built once from source by route (i) at dispatch 13, run 45518506879 (events (104)); set at Component 4 (events (106))
RUNNER_COMMIT_B767 = '89fd5b54941b246d707bd2e9708a8a24e222ba5c'   # ### b767: the act's closing Lean commit, the last at which a restored build read exit 0 ((R377)(4)): 89fd5b54 (step 59), dispatch 16, run 45235741926, axioms sha256 9c2cb7f7a216790c (data/b767_events.txt (105)); built once from source by route (i) at dispatch 17, run 45236921224 (events (107)); set at Component 4 (events (111))
RUNNER_COMMIT_B766 = '3c67b8b58d6f323b1db62249a77453963368aaf7'   # ### b766: the act's closing Lean commit 3c67b8b5 (step 62), built from source twice and stopped under the hold twice (dispatches 15, 16), main not moved and no tag cut; step zero read main entering at 0ba9cd61, the workflow's bytes b765's closing Lean commit's; (R376)(4) does not write the workflow. b765 (R375)(4): the closing Lean commit, its workflow bytes those of e83e0deb (the key of 70c50d37 and the word's planted input), read by the arm that reads the workflow's file
RUNNER_COMMIT_B764 = '38a57e02074a22eebbf33c6ff9ce5c7e58335d4a'   # ### b764's, kept beside
WEIL_BRANCH_B763 = ('push-b763-form', '4964e95758a7b1bc8c49d0972ebb18877d4f945f')   # ### b763's (R373)(6): made at main a3aad4cc (20:14:10Z); commits ec82fed0, 0f849552, 4964e957; main moved from it (02:22:05Z); kept by (R374)(4) and (R375)(4). b765, Component 5 (the Edit tool): the carry had shifted its name to push-b764-form, here and in the two b763 names below; set back to the names the kernel's refs hold (for-each-ref, 16:0xZ)
WEIL_TAG_B763 = ('v0.42', '001e94ff09537595adfe0b59acddfb45635a0e86', '4964e95758a7b1bc8c49d0972ebb18877d4f945f')   # ### b763's (R373)(6): name, tag object, peel read back at the remote (data/b763_SIDE-explicit-formula_push-b763-form_push_out.txt, 02:22:05Z); peels as before ((R374) N5)
WEIL_BRANCH_B759 = ('push-b759-weil', 'a3aad4cceb41705fe9929c9b5600976eaf7434b5')   # ### b759's, kept
WEIL_TAG_B759 = ('v0.41', '390506fc8e1128976f68ca63219ac91d02ffa532', 'a3aad4cceb41705fe9929c9b5600976eaf7434b5')   # ### b759's, unmoved by b763 (N5)
ORDER_BRANCHES = ()   # ### b764 (R374)(8): no order of (8) writes a kernel (each is a relay or PLACE-papers build), so no order branch is made
ORDER_TAGS = ()   # ### LEFT EMPTY BY (R380)(12): no tag cut or moved beyond v0.47 under (4), which WEIL_TAG holds where cut; no order's tag
ORDER_BRANCHES_B763 = (('push-b763-squares', '819e4a832700038d103b4efc1e0ee0f1343f7c6e'),   # ### b763's (R373)(8), under the names the remote holds: SQUARES-AT-24 made at main 4964e957 (03:48:11Z), pushed alone and read back (03:52:35Z); kept by (R374)(4)
                       ('push-b763-keiper', 'a59632eb3e8f4164c491ced038130b583f4893df'))   # ### KEIPER-FACE made at main 4964e957 (04:22:20Z), pushed alone and read back (04:27:35Z); kept by (R374)(4)
ORDER_TAGS_B763 = (('v0.43', 'bcd4d4818520fc7a477c98e2c79548b80295725f', '819e4a832700038d103b4efc1e0ee0f1343f7c6e'),)   # ### b763's (R373)(8): W-ORD-SQUARES-AT-24 at main's read-back (data/b763_SIDE-explicit-formula_push-b763-squares_push_out.txt, 05:34Z); peels as before ((R374) N5)
PRESEND_SENDS = ()   # ### b764: no pre-send bank -- the three dispatches of (7) send the workflow's change with main's Lean files at v0.43, no statement, so no salt check (the targets read once, data/b764_targets.json)
PRESEND_SENDS_B763 = ('s123', 's4', 's5', 'sf', 's7', 's24', 'skp')   # ### b763's, kept for the carried readers
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
C2_PP = ('5cfb9577', '9aab5f65', 'd4808187', '4570c462', '41170e41')   # ### b769, Component 2: REGISTRY's block ((4)(a), step 15), SPIRAL_MAP.md's merge ((4)(b), step 18), [X4] with [M5] in OPEN_TRAILS (step 25), the cluster's source record ((4)(d), step 29) and [B1], [A4] and [C9] ((4)(c), (4)(d), (7), step 32); complete (no reader in the act module at this setting)
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
C3_PUTS = (('(4)(d) the two archives', 'data/b770_put_1.json', '6d71764d'),)   # ### (subject, the put bank, the commit carrying it); b769: the one put of (R379)(4)(d), set from b768's two by the Edit tool at Component 3 (no reader in tools/acts/b769.py or tools/standing/, data/b769_events.txt (63))
C3_SITTING_TOOL = ()
C3_SITTING_BANK = ()
SITTING_COMMIT = None
SITTING_BANK = None
ITEM_PP = ()   # ### no passed item's PLACE-papers write this act
SITTING_PP = ()
SITTING_GH = ()
SITTING_SETTINGS = ()
SITTING_ITEMS = None          # ### (R380)(7): the sitting of the tenth act in the light form; set from data/b770_sitting_agenda.txt when written
SITTING_STATES = {}
HANDOFF_COMMIT = '53a0a2e6'   # ### b770's, written once by tools/standing/handoff.py before the gate ((R380)(13)'s (W) list names HANDOFF.md), 154 lines, 19121 bytes, sha256 73d9d6b02772d9e8 (step 77, 2026-11-27T12:23:56Z), committed alone
HANDOFF_COMMIT_B769 = 'fdd92da2'   # ### b769's, written once by tools/standing/handoff.py before the gate ((R379)(13)'s (W) list names HANDOFF.md), 154 lines, 18809 bytes, sha256 2b2d99148e589d4f (step 60, 2026-11-26T05:24:07Z), committed alone
HANDOFF_COMMIT_B768 = '5588d3b5'   # ### b768's, written once by tools/standing/handoff.py before the gate ((R378)(13)'s (W) list names HANDOFF.md), 154 lines, 17037 bytes, sha256 11ee46e64f20f244 (step 89, 2026-11-25T08:15:13Z), committed alone
HANDOFF_COMMIT_B767 = 'aadb0eb5'   # ### b767's, written once by tools/standing/handoff.py before the gate ((R377)(13)'s (W) list names HANDOFF.md), 154 lines, 17388 bytes, sha256 49306d4b3f490139 (step 79, 2026-11-24T01:05:49Z), committed alone
HANDOFF_COMMIT_B766 = 'f2a6ba69'   # ### b766's, written once by tools/standing/handoff.py before the gate ((R376)(12)'s (W) list names HANDOFF.md), 154 lines, 16387 bytes, sha256 3b8aac8558128978 (step 83, 23:20:42Z); the carry had left b765's ab9d680e
HANDOFF_COMMIT_B765 = 'ab9d680e'   # ### b765's, 154 lines, 17603 bytes, sha256 a45ff3a51ae02d56 (step 70, 22:14:41Z)
HANDOFF_COMMIT_B764 = '6d4d47f5'   # ### b764's, 154 lines, sha256 d41904c83a03311e (step 77, 03:03:26Z)
HANDOFF_COMMIT_B763 = '26be95bb'   # ### b763's, 154 lines (step 78, 08:17:27Z)
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
PP_WRITES = (('corr', 'FINDINGS.md', '11fe9707'), ('trails_c2', 'OPEN_TRAILS.md', 'f945cbd9'), ('trails_c2i', 'OPEN_TRAILS.md', 'c599930d'),
             ('trails_c2s', 'OPEN_TRAILS.md', 'a0ac08c9'), ('trails_c3', 'OPEN_TRAILS.md', 'c0146cf4'), ('trails_c4', 'OPEN_TRAILS.md', '423a6b78'))   # ### b770 (R380)(9): each write of this act in the papers` repository, OPEN_TRAILS and FINDINGS and no other file, (key, file, commit), from the step rows (steps 12, 29, 38, 44, 55 and 58), appended as made
PP_WRITES_B769 = (('corr', 'FINDINGS.md', 'b382b95e'), ('registry_block', 'REGISTRY.md', '5cfb9577'), ('map_merge', 'SPIRAL_MAP.md', '9aab5f65'),
             ('trails_c2', 'OPEN_TRAILS.md', 'd4808187'), ('archives', 'clusters/lean-archive-november-2026/MANIFEST.txt', '4570c462'),
             ('trails_c2b', 'OPEN_TRAILS.md', '41170e41'), ('registry_c2b', 'REGISTRY.md', '41170e41'), ('errata_c3', 'ERRATA.md', '5111e451'),
             ('trails_c3', 'OPEN_TRAILS.md', '5111e451'), ('trails_c4', 'OPEN_TRAILS.md', '3deb3dca'))
# ### b769 (R379)(9): each write of this act in PLACE-papers named (OPEN_TRAILS, FINDINGS, REGISTRY, ERRATA, SPIRAL_MAP.md and the folder of
# ### (4)(d)), (key, file, commit), from the step rows (steps 6, 15, 18, 25, 29, 32, 35 and 42; data/b769_events.txt (45), (51), (54), (59),
# ### (60), (62), (63), (70)), set before the lock; the folder of (4)(d) by its manifest alone (data/b769_archives.json :104-:108), the two
# ### archives' own names written nowhere the act writes (N5); the entry and the trail at the close appended as made
PP_WRITES_B768 = (('corr', 'FINDINGS.md', '9c43f4bb'), ('trails_c2', 'OPEN_TRAILS.md', 'eea70a2d'), ('trails_c5', 'OPEN_TRAILS.md', '45f187d1'))   # ### b768: the act's PLACE-papers writes (key, file, commit), read from the step rows (steps 6, 22 and 66), appended as made; trails_c5 given at Component 5 after the act part's probe read G-REGISTRATIONS-FIRST's c5 row without it (defect (x)), its one reader the checks' pp_shas (tools/acts/b768.py :868)
PP_WRITES_B767 = (('corr', 'FINDINGS.md', '216d9715'), ('trails_c2', 'OPEN_TRAILS.md', 'ba23945a'), ('trails_c5', 'OPEN_TRAILS.md', 'adadfd62'))   # ### b767: the act's PLACE-papers writes (key, file, commit), read from the step rows (steps 7, 25 and 63); the entry and the trail appended as made
PP_WRITES_B766 = (('corr', 'FINDINGS.md', '7a36f281'), ('trails_c2', 'OPEN_TRAILS.md', 'a183880f'), ('trails_c3', 'OPEN_TRAILS.md', '92108a44'),
             ('trails_c4', 'OPEN_TRAILS.md', '2d9d51ae'), ('trails_c5', 'OPEN_TRAILS.md', 'ff328d86'))   # ### b766 (R376)(1), (4)-(6): the corrigendum for b765 (step 5); the four groups of the rulings tool in OPEN_TRAILS (steps 20, 30, 50, 65)
PP_WRITES_B765 = (('corr', 'FINDINGS.md', 'd9c03949'), ('trails', 'OPEN_TRAILS.md', 'fb094a44'))   # ### b765's, kept beside
PP_WRITES_B764 = (('corr', 'FINDINGS.md', 'e383d313'), ('errata', 'ERRATA.md', '772d5cf0'), ('trails', 'OPEN_TRAILS.md', '772d5cf0'),
                  ('register', 'BIBLIOGRAPHY.md', '772d5cf0'))   # ### b764's, kept beside
PP_WRITES_B763 = (('corr', 'FINDINGS.md', '6034501c'), ('trails', 'OPEN_TRAILS.md', '387713dd'),
                  ('canon', 'phase1.5/method/THE_METHOD_CANON.md', '387713dd'))   # ### b763's, kept for the carried readers that cite them
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
C4_READ = ('tools/b770_orders.py', '5b3d5a60', ('data/b770_orders_read.txt', 'data/b770_instruments_draft.txt'), 'f56557dd')   # ### the orders read and the two drafts
C4_PUT = ('data/b770_put_1.json', '0803754c')   # ### the one put, three questions, and the answers pair by its route, all three passed as recommended (step 22)
C4_PASSED_GEN = '9aa5fe8c'   # ### tools/b756_passed.py committed before its run, with events (21) (step 23)
C4_PASSED_PP = (('cp', 'OPEN_TRAILS.md', 'e50a394b'), ('instruments', 'phase1.5/method/INSTRUMENTS.md', '3b45826d'))   # ### steps 24, 25, each confirmed at HEAD (data/b756_passed.json)
C4_HERE = ('v1.34.8', '5b7aa91e', 'data/b770_standing_v1348.txt')   # ### W-ORD-LABEL-READER's predicate and control, controls 11 of 11 (step 26)
C4_MOVES = ('tools/b770_moves.py', '208eee6a', 'data/b770_orders_moves.txt', 'a26f30b9')   # ### the twelve status lines for this act's trail, controls 12 of 12 (steps 27, 28)
C4_CEILING = ('tools/b770_ceiling.py', 'a26f30b9', 'data/b770_ceiling_c4.txt')   # ### the ceiling after Component 4: 17.53 h against 24 h, nothing carried
C4_ORDERS = (1, 1, 5, 5)   # ### the orders: done, here, with the build, later (data/b756_orders_read.txt :87; data/b756_orders_moves.txt)
C4_CP = 'passed'           # ### CP-6 and CP-7 (data/b756_author_answers.txt :18; OPEN_TRAILS at e50a394b)
C4_LINE_GEN = None   # ### b755: no line bank; the entry's INTEGRATION line is (R365)'s, composed from the banks by the record module
C4_LINE = None       # ### Component 5: the act's INTEGRATION line by (R380)(10)'s words, bare as the entry's last line
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
REG_COMMIT = ''   # ### LEFT EMPTY BY (R380)(9): the registration none at this act, so the registration's commit empty
REG_COMMIT_B769 = ''   # ### LEFT EMPTY BY (R379)(9): nothing registered at this act, so the registration's commit empty again
REG_COMMIT_B768 = ''   # ### LEFT EMPTY BY (R378)(6), (9): nothing registered at this act, so the registration's commit empty again
REG_COMMIT_B767 = 'b9224ba6'   # ### b767 (R377)(6), (9): the registration of H-GRADED-WINDOW, data/b767_registration.txt, committed alone before the tool's run at graded knots, relay b9224ba6 (step 20, 11:53:18Z); a commit again (b766 left it empty)
REG_COMMIT_B766 = ''   # ### LEFT EMPTY BY (R376)(4): "the values being b765's and no hypothesis registered at this act" ((4)(a), data/b766_ferry.txt :18); no registration bank, the carry had left b765's 7907161c. ### b766 (the touch read's arm call, 20:38:42Z, defect (p)): the empty string where None stood, which toset.py reads as EMPTY alike (tools/standing/toset.py :12) and every truth test of the act module alike; the checks template's sources call files_of on it unguarded (checks.tpl :593), which raised on None and reads the empty name as no files, git's show refusing it with empty output; the sources' files['reg'] read by no arm (a search of the template and the act module)
REG_COMMIT_B765 = '7907161c'   # ### b765's (R375)(4), (5)(c): [G2], committed alone as data/b765_registration.txt before any dispatch (step 4, 10:09:46Z), kept beside
REG_COMMIT_B764 = '6fd013e9'   # ### b764 (R374)(9)(b): [G1], H-TAU-FINITE-PART, committed alone as data/b764_registration.txt before the tool's run (step 60, 22:15:20Z)
REG_BANK = 'data/b770_registration.txt'   # ### b767 (R377)(6): H-GRADED-WINDOW, committed alone at REG_COMMIT; b766 left it None ((R376)(4))
REG_COMMIT_B755 = C4_RULE_ZEROS   # ### b755: H-ZEROS-FROM-PRIMES committed alone (data/b755_registrations.txt (2))
ZEROS_REG_COMMIT = REG_COMMIT
ORDERS = (142, 60, 42, 12, 28)          # ### b753's (R363)(4) triage, carried as read (data/b729_orders_triage.txt): DONE, NOT MET, MET, AUTHOR'S WORD
TRIAGE = 'data/b729_orders_triage.txt'
LV_SCRATCH_BRANCH = 'scratch-b724'      # ### b724's scratch branch of SIDE-lv-conservation, kept ((R364)(8))
LV_RUNS = (('SIDE-lv-conservation', 40964150574),)   # ### b753's one dispatch, read by its id (carried, not re-run)
LV_ROWS = 'data/b770_lv_rows.json'
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
MAX_DISPATCHES = 40        # ### b770 step zero, (R380)(4), (9), N1: at most 40 dispatches of SIDE-explicit-formula, as at b768 -- at most 36 with the restore on, and with the restore off the closing build and one repeat of it where it stopped under the hold; no cap by price row; no planted build
MAX_DISPATCHES_B769 = 0        # ### b769 step zero, (R379)(9), N1: the dispatch cap 0, no dispatch of any kernel at this act; the kinds of b768's cap, its refused-send pins and its restore-off items not carried
MAX_DISPATCHES_B768 = 40        # ### b768 step zero, (R378)(4), (9), N1: at most 40 dispatches of SIDE-explicit-formula -- at most 36 with the restore on, and with the restore off the closing build and one repeat of it where it stopped under the hold; the trial's kind of b767 not used; no cap by price row; no planted build
MAX_DISPATCHES_B767 = 40        # ### b767 step zero, (R377)(4), (9), N1: at most 40 dispatches of SIDE-explicit-formula -- at most 36 with the restore on, and with the restore off the trial of (5), the closing build and one repeat of each where it stopped under the hold; no cap by price row (b766's table of rows raised not carried); no planted build
MAX_DISPATCHES_B766 = 20        # ### b766 step zero, (R376)(4), (8), N1: at most 20 dispatches of SIDE-explicit-formula -- at most 18 with the restore on, the closing one from source and one repeat of a build stopped under the hold; no planted kind and no kind for a save on main
MAX_DISPATCHES_KINDS = (('restore', 36), ('closing', 1), ('repeat', 1))   # ### b770 step zero, (R380)(4), (9): the cap's kinds as b768 held them, each with its count; the repeat one, of the closing build where it stopped under the hold
MAX_DISPATCHES_KINDS_B769 = ()   # ### LEFT EMPTY BY (R379)(9): no kind, the cap being 0 and "the kinds of b768's cap" not carried (b769 step zero)
MAX_DISPATCHES_KINDS_B768 = (('restore', 36), ('closing', 1), ('repeat', 1))   # ### b768 step zero, (R378)(4), (9): the cap's kinds, each with its count; the repeat one, of the closing build where it stopped under the hold; the trial's kind and its restored run not carried
MAX_DISPATCHES_KINDS_B767 = (('restore', 36), ('trial', 1), ('closing', 1), ('repeat', 2))   # ### b767 step zero, (R377)(4), (9): the cap's kinds, each with its count; the repeats one for the trial and one for the closing build, each where it stopped under the hold
MAX_DISPATCHES_KINDS_B766 = (('restore', 18), ('closing', 1), ('repeat', 1))   # ### b766 step zero, (R376)(8): the cap's kinds, each with its count
MAX_DISPATCHES_B765 = 13   # ### b765's, (R375)(4), N1: the planted one, at most ten with the restore on, the closing one from source and one repeat of a stopped build
MAX_DISPATCHES_B764 = 3    # ### b764's, (R374) N1: "the dispatches are the three of (7) and no other"
MAX_DISPATCHES_B763 = 18  # ### b763's, (R373) N1: the counts within its price table's upper figures (data/b763_price.txt)
MAX_DISPATCHES_B762 = 0    # ### b762's, (R372) N1: "no dispatch is sent"
MAX_DISPATCHES_M24 = 0     # ### (R373)(5): no kernel beyond SIDE-explicit-formula is written; no dispatch in SIDE-dirichlet-mod-24
MAX_DISPATCHES_B759 = (3, 0)   # ### b759's caps, (R369)(5), (11)
MAX_DISPATCHES_B758 = (4, 0)   # ### b758's caps, (R368)(10)
MAX_DISPATCHES_B757 = (14, 4)   # ### b757's caps, (R367)(10)
MAX_DISPATCHES_B756 = 0    # ### b756's: no runner dispatch
MAX_C2, MAX_KEIPER = 0, 0
EF_DIR = 'D:/SIDE-explicit-formula'
EF_BASE = 'ffefddc61b05fcca089ff20cc8cd2f103dd0a5f1'   # ### b770 step zero: SIDE-explicit-formula's main entering the act, b768's v0.46 (wlfacts770.py: main ffefddc6 equal to origin/main)
EF_BASE_B769 = 'ffefddc61b05fcca089ff20cc8cd2f103dd0a5f1'   # ### b769 step zero: SIDE-explicit-formula's main entering the act, b768's v0.46 (wlfacts769.py, 17:38:32Z: main ffefddc6 equal to origin/main)
EF_BASE_B768 = '89fd5b54941b246d707bd2e9708a8a24e222ba5c'   # ### b768 step zero: SIDE-explicit-formula's main entering the act, b767's v0.45 (wlfacts768.py, 12:54:48Z: main 89fd5b54 equal to origin/main)
EF_BASE_B767 = '0ba9cd61e1a071446fd366896c710ae13356bf3e'   # ### b766 step zero: SIDE-explicit-formula's main entering the act, b765's v0.44 (the carry had kept b765's entering pin)
EF_BASE_B765 = '819e4a832700038d103b4efc1e0ee0f1343f7c6e'   # ### b765's entering main, b763's v0.43. b764 (Component 3, the Edit tool, defect (f)'s class): SIDE-explicit-formula's main entering the act, b763's v0.43 (the carry had kept b763's entering pin under b763's comment)
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
# ### b767: the act's dispatches of SIDE-explicit-formula by run id, in their order, as rowed in data/b767_dispatch_rows.json (17 rows of
# ### kind dispatch, read 18:54:22Z): 1 trial-on, 2 trial-off, 3-6 L9a and L9b part one, 7 L10, 8-10 L11a and L11b, 11-16 L9b, 17 the closing
# ### build from source at 89fd5b54 (restore off); a repeat appended where the closing build stops under the hold
# ### b768: the act's dispatches of SIDE-explicit-formula by run id, in their order, as rowed in data/b768_dispatch_rows.json: 1-2 the trial at
# ### small size (item a), 3-9 L9c (item b), 10 L11c (item c), 11-12 L11d and L12 (item d), 13 the closing build from source at ffefddc6
# ### (restore off, route (i)); a repeat appended where the closing build stops under the hold (set at Component 4, events (106))
EF_RUNS = (45922049731, 45927530723, 45929106349, 45930524580, 45931997405, 45933086394, 45933637198, 45935483550)   # ### b770 (R380)(4), N1: the act's dispatches of SIDE-explicit-formula by run id, in their order, as rowed in data/b770_dispatch_rows.json (8 rows of kind dispatch, read by scratch ceilfacts770.py 06:22:40Z): 1-6 the steps (b) to (g) with the restore on at 1b413384, c8913190, 5e1c7b72, 97d7285b, b34fdb2e and cc2f3ba8, each COMPILED; 7 the closing build from source at cc2f3ba8 (restore off, route (i)) and 8 its one repeat, each STOPPED UNDER THE HOLD, [C11] (events (72)-(90)); set at Component 5 by the Edit tool, where the carry left it empty
EF_RUNS_B769 = ()   # ### LEFT EMPTY BY (R379)(9): the dispatch cap 0, no dispatch of SIDE-explicit-formula at this act, so no run id
EF_RUNS_B768 = (45439584241, 45447787162, 45454217113, 45459715839, 45463999522, 45469187228, 45474141600, 45478679725, 45489301040, 45494658063,
           45510384327, 45514975816, 45518506879, 45521560784)   # ### b768: 14 the closing build's one repeat at ffefddc6 (restore off, route (i)), exit 0, read at 03:04:09Z (data/b768_events.txt (122))
EF_RUNS_B767 = (45179223796, 45179932496, 45183337569, 45186143428, 45190830447, 45197769158, 45204986880, 45209587647, 45212341085, 45215343184,
           45218909055, 45221153344, 45226620548, 45231087000, 45233987503, 45235741926, 45236921224)
EF_RUNS_B766 = (45009051176, 45011065297, 45012810770, 45014250426, 45015072464, 45020375424, 45027497489, 45034393612, 45039260081, 45041946380, 45043631697, 45044513076, 45045547342, 45046730935, 45047352154, 45051503982)# ### dispatch 16 (repeat, the cap's one, of dispatch 15 stopped under the hold, 3c67b8b5, restore off, sent 17:48:30Z); dispatch 15 (closing, the closing Lean commit 3c67b8b5 from source, restore off, sent 17:04:22Z, STOPPED UNDER THE HOLD, exit 143); dispatch 14 (d-arch, L9 in part in four blocks at 3c67b8b5, sent 16:57:54Z, the archimedean row's second of 4, COMPILED, 5.2 min); dispatch 13 (d-arch, L9 in part at 9a389982, sent 16:44:52Z, the archimedean row's first of 4, STOPPED UNDER THE HOLD, exit 143, 3.7 min, not scored, defect (l)); dispatch 12 (d-pole, L8's data half repaired at c6a46950, sent 16:33:34Z, the pole row's last of 3, COMPILED, 3.7 min); dispatch 11 (d-pole, L8's data half at 1d3b1bdf, sent 16:24:05Z, BREAKS, 2.0 min, defect (k)); dispatch 10 (d-pole, L8 at 5266fb0a, sent 16:06:16Z, KERNEL, 6.9 min, the pole row's first of 3); dispatch 7 (d-k, L6 (c) at 448dd77b, sent 13:26:27Z, the row's fifth of 6). b766 step zero, after `carry.py ruled` refused b765's eleven carried unchanged (R3): (R376)(4)'s dispatches, at most 20, each set by its run id when sent (N1). Component 3: dispatch 1 (b, KERNEL, 3.2 min), 2 (c, KERNEL, 4.6 min), 3 (d-k, KERNEL, 2.8 min), 4 (d-k, BREAKS, 2.2 min), 5 (d-k, KERNEL, 2.8 min), 6 (d-k, KERNEL, 2.8 min, the closed form of kappa at 1848e7c0 under the row raised to 6), each with the restore on, restored by prefix (data/b766_dispatch_rows.json)
EF_RUNS_B765 = (44900549948, 44909786283, 44910107851, 44911649707, 44912710052, 44914928608, 44917105908, 44917471908, 44918855502, 44925522330, 44929638998)   # ### b765's eleven, read not re-run, kept beside. b765: the eleventh, the second save on main by the author's word of 2026-11-21 on it (sent 17:21:54Z, the Edit tool after). N1: this act's SIDE-explicit-formula runs, those of (R375)(4) and the word of 2026-11-21 alone, each read by its run id from the artifact (data/b765_dispatch_rows.json): the statement, the lemma's statement, the planted, lemma-step, three lemma-later, the closing from source (STOPPED UNDER THE HOLD), its one repeat (KERNEL, the pair equal: H-RUNNER-RESTORE HELD) and the save on main of the word's (iii) (sent 16:36:41Z)
EF_RUNS_B764 = (44826208702, 44838771976, 44838852797)   # ### b764's three, read not re-run (data/b764_dispatch_rows.json): the save (KERNEL, 94.2 min), the reference with the restore off (STOPPED UNDER THE HOLD, exit 143, 15.0 min) and the restore (KERNEL, 3.2 min): THE TRIAL FAILED
EF_RUNS_B763 = (44610575175, 44625270777, 44641876790, 44646848292, 44661759569, 44670834879, 44674735311)   # ### b763's seven, read not re-run (data/b763_dispatch_rows.json): dispatch 1 BREAKS, 2 KERNEL, 3 STOPPED UNDER THE HOLD, 4 KERNEL, 5 KERNEL ((7)'s statement), 6 KERNEL (SQUARES-AT-24), 7 KERNEL (KEIPER-FACE's first file)
EF_RUNS_B762 = ()   # ### b762's: none
EF_RUNS_B759 = (44162171267,)   # ### b759's one, read not re-run
M24_RUNS = ()   # ### LEFT EMPTY BY (R380)(12): no kernel touched beyond SIDE-explicit-formula, so no SIDE-dirichlet-mod-24 dispatch (N1, N5)
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
DISPATCH_ROWS = 'data/b770_dispatch_rows.json'
ERRATA_ID = None   # ### b770, before the lock (the Edit tool, 08:29Z): no ERRATA entry by (R380)(12), where the carry left b769's E-2026-11-25-1; its one reader, the template's G-DIFFERS-ERRATA predicate (checks.tpl :1572, which wants None), overridden in the act module (MARK dd4dd9cb3d4b), git grep 08:28:03Z
ERRATA_IDS = ()   # ### b770, before the lock (the Edit tool, 08:29Z): no ERRATA entry by (R380)(12); read by nothing (git grep 08:28:03Z)
ERRATA_ID_B769 = 'E-2026-11-25-1'   # ### (R379)(5): b769's first of four, ERRATA :1163, kept under its own name, read by nothing
ERRATA_IDS_B769 = ('E-2026-11-25-1', 'E-2026-11-25-2', 'E-2026-11-25-3', 'E-2026-11-25-4')   # ### (R379)(5): b769's [E2] to [E5] at ERRATA :1163, :1177, :1191 and :1205, kept under their own name, read by nothing
ERRATA_IDS_B760 = ('E-2026-11-18-1', 'E-2026-11-18-2')   # ### (R370)(10): b760's BLOCK E's two entries at the file's end (PLACE-papers f47d90f0)
RETIRED_COUNT = 0
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list (the root answer's addition (b))
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b770_') and f.endswith('.py') and f != 'b770_report.py')) + NEW_TOOLS + COMPUTE_TOOLS + REPAIRED_TOOLS
# ### the act's arms over its own banks: set before the lock by the Edit tool -- b753's list, the act shift G-R363-ENTERED to G-R364-ENTERED,
# ### G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0 ((R364)(2)(iv))
ACT_ARMS = ('G-ACT-CURRENT', 'G-ARM-TAGS', 'G-ARMS-RETIRED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED', 'G-CLOSING-DRY-STEP', 'G-COEFFS-LAW',
            'G-CORRIGENDUM-ENTERED', 'G-COUNT-ROUTE-PRICED', 'G-DELETES-ONE-BRANCH', 'G-DERIVATION-GRADED', 'G-DIFFERS-ERRATA', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-GUARD-HELD', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-LISTINGS-BEFORE-CLAUSES',
            'G-MEMBRANE-WIRED', 'G-OFFSET-POST-HOC', 'G-POSTROOT-WRITES-NONE', 'G-PREDICTION-FIRST', 'G-R380-ENTERED',
            'G-REGISTRATIONS-FIRST', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO', 'G-RULES-ROW-ENTERED', 'G-SURGERY-CARRIED', 'G-TOUCH-READ',
            'G-WRITELIST-MIRROR-STATE')

# ### b754 writes no kernel ((R364)(5)): no main touched, no branch made on a kernel
SITTING_TIPS = {}   # ### LEFT EMPTY BY (R380)(12): "no kernel touched beyond SIDE-explicit-formula", and its main not moved ([C11] by (R380)(4)), so no sitting's tips (b769's clause (R379)(12), no kernel touched, set to b770's before the lock, in b768's ground)
SITTING_BASE = EF_BASE
SITTING_REPOS = tuple(sorted(SITTING_TIPS))
SITTING_BRANCH = None
SITTING_BANK = 'data/b770_sitting.txt'   # ### the record of the sitting, one row per item
KERNEL_BASES = 'data/b770_kernel_bases.json'
