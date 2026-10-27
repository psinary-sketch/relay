# -*- coding: utf-8 -*-
"""b718_worklist.py -- THE ACT'S DATA, UNDER (R328). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b718: LANE TWO, ACT ONE HUNDRED AND FORTY-FIVE, THE DERIVATION ACT -- b717 AT ITS WEIGHT; THE CORRIGENDUM; THE STANDING LINE OF
### CONSISTENCY; THE COEFFICIENT LAW READ THROUGH THE CLASS GROUP; THE CONTROLS' RIPE WORK; TWO READS; THE TOOLSET AT v1.2.0; THE FEDERATION
### PIN, LAST AND STOPPABLE. No lean on this host; the runner dispatches those of (R328)(8) alone, twelve at most (N1).
### Carried by diff from b717_worklist.py (data/b718_carry_worklist.txt) and its stage one rewritten by the Edit tool with this act's objects
### (stage one: step zero; stage two, Component 7, by the Edit tool).
### The act runs in a NEW session (02c7cf38; the seat cleared after b717's closing, the ruling pasted at once): the previous act's window is
### b717's session 551b6446 from b717's post-push combine to its end (b671's session-change form).
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'c02f47c1'         # ### PLACE-papers main before the act (b717's trail, pushed by push-b717-record)
PRE_RELAY = '248c5a97'      # ### relay main before the act (b717's closing, pushed by push-b717-closing and read back)
DATE = '2026-10-27'
SESSION_ID = '02c7cf38-4c6a-4f88-b813-a7e15e9b85b4'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/%s/scratchpad' % SESSION_ID
HOLD = 2560
ANCHOR = 'RULING (R328) BEGIN'
TAIL = 'FERRY END (part 1 of 1)'
SESSIONS_AFTER = ()         # ### one session so far (b671's form holds a continuation here if one comes)
PREV_SESSION = '551b6446-5996-4c11-94be-d2a2e851a529'   # ### b717 ran and closed in its own session; this act's seat is a new one
PREV_ANCHOR = 'RULING (R327) BEGIN'
DRAFT = '23228113'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
EXPORT = 'data/b647_navigator_memory.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CITATION_BANK = 'b718_citation_check.txt'

# ### the ledger lines of the previous act (the carried tools' B711_* names read the previous act's lines)
B711_ENTRY = 10784          # ### FINDINGS: b717's entry head (b718's Component 1 appends b717's weight line beneath it)
B711_WEIGHT = 10722         # ### FINDINGS: b716's weight line (b717's Component 1)
B711_CORRIGENDUM = 10724    # ### FINDINGS: b717's corrigendum for b716 (data/b675_corrigenda.txt row (37))
B711_TRAIL = 16086          # ### OPEN_TRAILS: b717's trail record
B711_FACE = 'data/b717_registration_2026-10-27.txt'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-27-b717.zip'   # ### b717's export, CLEAN on all three clauses, 74 entries
ORDER_LV_JOIN = 15452       # ### OPEN_TRAILS: W-ORD-LV-CLOSURE-JOIN (b702)
ORDER_LV_PORT = 15686       # ### OPEN_TRAILS: W-ORD-LV-FORWARD-PORT (b707), restated in b717's trail :15914
ORDER_LV_PORT_LATEST = 15914
ORDER_LV_PORT_TAG = 15848   # ### OPEN_TRAILS: W-ORD-LV-PORT-TAG (b711), discharged by (R328)(3)(i)
ORDER_KEYSTONE = (15454, 15496)   # ### OPEN_TRAILS: W-ORD-KEYSTONE-HEADS (b702) and b703's addition beneath it ((R328)(4))
TRAIL_ORDERS = 16030        # ### OPEN_TRAILS: b715's open orders line (b717's trail carries none of its own)
TRAIL_RESOLVED = 16076      # ### OPEN_TRAILS: b717's ten items for the author's strike
FACES_HEAD = 8              # ### FACES_LEDGER.md: the head's sentence b717 restated
FACES_JOIN_ROW = 547        # ### FACES_LEDGER.md: faces_join's row
FACES_F2 = (21, 502)        # ### FACES_LEDGER.md: F2's row and its tier row ((R328)(10))

# ### the branches step zero deletes ((R328)(8)): the push-b717-* branches of relay and PLACE-papers by name, each read from the listings and
# ### `--merged` printed before the deletes, one per command, each its own message, in sequence, nothing chained after any (the relay carries
# ### push-b717-closing, push-b717-preroot and push-b717-record; PLACE-papers push-b717-preroot and push-b717-record)
DELETE = (('D:/relay', ('push-b717-closing', 'push-b717-preroot', 'push-b717-record')),
          ('D:/MY-DOwnloads/PLACE-papers', ('push-b717-preroot', 'push-b717-record')))
DELETE_REMOTE = ()
KEPT_BRANCH = ('D:/SIDE-lv-conservation', 'port-b707')   # ### (R328)(8): NOT deleted, local or remote
KEPT_BRANCHES = (('D:/SIDE-lv-conservation', 'port-b707'),)

# ### the kernels: none written this act (N1, N5); no tier-one move; the kernels read for (R328)(6) at their current tags and not written
LV_DIR = 'D:/SIDE-lv-conservation'
EF_DIR = 'D:/SIDE-explicit-formula'
JOIN_DIR = 'D:/SIDE-faces-join'
KERNEL_DIR = 'D:/SIDE-kernel'
META_DIR = 'D:/SIDE-meta'
# ### (R328)(8): the twelve kernels below the target de5ce8a9 (data/b716_federation_pin_price.txt (3), :56-:138), each at D:/<name>
PIN_TARGET = 'de5ce8a9a66a'
PIN_KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
               'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')
PATHS = ('D:/relay', PP, EF_DIR, LV_DIR, JOIN_DIR) + tuple('D:/' + k for k in PIN_KERNELS)   # ### (R328)'s PATHS, listed at step zero
EF_MAIN = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'    # ### SIDE-explicit-formula's main, unmoved
LV_MAIN = 'd38f3e8c99c3431c604bcba13210042df7748859'    # ### SIDE-lv-conservation's main, untouched
LV_V0100 = '93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f'   # ### the deposit, untouched
PORT_BRANCH = 'port-b707'
PORT_TIP = 'cb0aea56354abb3abda3fdaef28429c6605605d5'   # ### port-b707's tip, b712's, unmoved this act
PORT_NEW_TIP = PORT_TIP
LV_TAG = 'v0.14.0'          # ### b714's tag ((R324)(3)(i), data/b714_lv_tag.txt), at PORT_TIP, read and not moved this act
LV_TAG_OBJECT = '0e7c3527c8ff693c34126b57d1b1587149e5371c'   # ### annotated, at PORT_TIP, no GitHub release (tier one)
LV_TAG_RULED = 'v0.11.0'
KERNEL = 'SIDE-lv-conservation'
JOIN_NEW_TIP = '11a472b90553deaddc411c5d69ec03611ee277c5'   # ### SIDE-faces-join main, unmoved this act
JOIN_RUN = 40210894425
JOIN_TAG = ('v0.1.0', '9bf6fe65582187a92b6ab17e03953efb2cecd913', '11a472b90553deaddc411c5d69ec03611ee277c5')   # ### tag object, peeled
EF_V037 = '38e273477257687d676033be0b0243af84a1e08a'
MAX_DISPATCHES = 12         # ### N1: the federation pin's dispatches alone, twelve at most ((R328)(8))

PAPERS = dict()
DATA_STANDING_V1 = 'data/standing_clauses_v1.txt'
DATA_STANDING_V2 = 'data/standing_clauses_v2.txt'
DATA_STANDING_V3 = 'data/standing_clauses_v3.txt'
DATA_STANDING_V4 = 'data/standing_clauses_v4.txt'
DATA_STANDING_V5 = 'data/standing_clauses_v5.txt'
DATA_STANDING_V6 = 'data/standing_clauses_v6.txt'
DATA_STANDING = 'data/standing_clauses_v7.txt'   # ### (R328)(3): v6 with the standing line of consistency appended, committed alone at step zero
ARM_TAGS = 'data/arm_tags.json'                  # ### (R327)(2): every arm tagged CLAIM or CLOSE by what it guards
REPO_VISIBILITY = 'data/repo_visibility.txt'   # ### (R324)(2): the visibility map, the author's listing of 2026-10-26
REGISTRATIONS = 'data/b716_registrations.txt'   # ### (R328)(4)(i): b716's registrations, (ii) read unchanged from dc5e808f (N2)
REG_COMMIT = 'dc5e808f9a2a95ffbe5b4d69b58e7fb216458c16'   # ### b716's first commit: the registrations with their count control
REG_FILES = ('data/b716_registrations.txt', 'data/b716_genus_control.txt', 'data/b716_genus_control.json', 'tools/b716_genus_control.py')
PRED_B717 = 'data/b717_predictions.txt'   # ### (R328)(5)(i): b717's predictions, committed alone at f47d8ab5, read not written
PRED_B717_COMMIT = 'f47d8ab5840d287bf63c1f0b59ba707ed85dbe07'
PREDICTIONS = PRED_B717
REGISTRATIONS_NEW = 'data/b718_registrations.txt'   # ### (R328)(4)(iv): committed alone before anything at either new discriminant (N2)
PRICES_6 = ('data/b716_federation_pin_price.txt', 'data/b716_epstein_count_price.txt')   # ### b716's two prices; (R328)(8) runs the first
COEFF_BANKS = ('data/b711_coeffs.txt', 'data/b713_coeffs.txt', 'data/b717_coeffs.txt')   # ### (R328)(4)(iii): the checks' banks, read not written
COMPUTE_BANKS = ('data/b718_decomp.txt', 'data/b718_decomp.json', 'data/b718_derivation.txt', 'data/b718_derivation.json',
                 'data/b718_registrations.txt', 'data/b718_a0.txt', 'data/b718_a0.json', 'data/b718_count_read.txt')
REG_B712 = '67a023887360b74483803ed02c83ae44fdf88f0b'   # ### b712's registrations with the genus control (b713's), read not written
REG_B710 = '41ff1193'        # ### data/b710_registrations.txt committed alone at b710's step zero (the refined law (i))
READ_BANKS = ('data/b707_read_calls.txt', 'data/b708_read_calls.txt', 'data/b709_read_calls.txt', 'data/b710_read_calls.txt',
              'data/b717_read_calls.txt', 'data/b718_read_calls.txt')

# ### THE SUITE'S PARTS: seven, as b706 split them and b707-b717 carried them (the ferry's Component 5)
PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b718'))
CHAIN_QUARTERS = (('b624', 'b641'), ('b642', 'b658'))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
ARCHIVE_DIR = 'archive/2026-10-22-b706-partner-copies'
STANDING_ADDED = ()          # ### N5: no standing arm added
SHARED_APPENDED = ('data/b675_corrigenda.txt',)
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'   # ### the census on main read by its rows (the readfirst's)
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'    # ### (R328)(6): the next edition, on main, the eleven names' rows
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'    # ### (R328)(5)(i): the companion table beside the paper
PP_WRITTEN = ('FINDINGS.md', 'OPEN_TRAILS.md', 'ERRATA.md', 'day1/Silence_of_Foundations.md', COMPANION, CENSUS_NEW,
              'day1/Exhaustive_Enumeration.md', 'day1/ONE_PAGE_PROOF.md', 'day1/Seven_Mechanism_Classes.md', 'day1/Spectral_Inertness.md',
              'day1/Third_Identity_Element.md')   # ### (R328)(1)-(3) the record lines; (5) the head, the companion and the six hits' papers, (6)
#   ### the census and the day papers' rows: the papers of (5)(ii) and (6) added at Component 6 (the Edit tool), Component 5's commit naming them
RECUT_DOC = 'day1/Silence_of_Foundations.md'
RECUT_BRANCH = 'recut-b712-silence'
RECUT_COMMIT = 'f5ea57cb77760a55a5b7903e920f53df4c3f19eb'   # ### b712's re-cut on RECUT_BRANCH
RECUT_TIP = '0aeca8341ae45e5e6e1fe2555dda11d1ec2eed0f'      # ### b713's tip of RECUT_BRANCH, merged into main at b714 (a86c9429); the
#                                                             ### branch deleted at b717's step zero ((R327)(9))
RECUT_MERGE = 'a86c942941806b8f1895f7f82c2a6489946bc0a3'
NEXT = ('b719 ((R328)(13)): the two discriminants computed under (4)(iv)`s commit (data/b718_registrations.txt); the surgery under its '
        'registration; the REGISTRY cells written; the box of (5)(iii) where it was carried')
NEXT_ACT = 'b719'


def orders_naming(ot_text, act):
    """(R328)(3), the NEXT line's repair: every open-orders row of OPEN_TRAILS whose status names <act> -- a row is a line opening
    `*Appended` that carries `THE ORDER **`W-ORD-`; its status is its text from its last `Status`; returned as (line, order, status). Pure in
    its arguments (b711's port clause was made b717's after the seal and stood outside the sealed NEXT, events :46)."""
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

# ### stage one (step zero): the commits made so far
ACT_CURRENT = 'data/act_current.json'   # ### (R324)(6)(ii): the act's figures, written at step zero and committed alone
STANDING_DIR = 'tools/standing'         # ### (R328)(7): the standing close toolset, versioned by tools/standing/VERSION
STANDING_COMMIT = ''            # ### data/standing_clauses_v7.txt committed alone ((R328)(3)) -- filled from the log after the commit
ACT_CURRENT_COMMIT = ''         # ### data/act_current.json committed alone
STEPZERO = ''                   # ### b717's closing push capture, committed alone at step zero ((R328)(10))
STEPZERO_STEPS = ''             # ### b717's step row 19, committed alone
STEPZERO_HASHES = ''            # ### data/b717_bank_hashes.json, committed alone
STEPZERO_REFUSALS = ''          # ### data/b717_hook_refusals.txt as it stands (the refusal after the closing), committed alone
STEPZERO_PREVBUILD = ''         # ### tools/mirror_prevbuild.json as b717's build left it, committed alone
STEPZERO_BANKS = ''             # ### the step-zero banks and tools, committed together by explicit list
VISIBILITY_COMMIT = ACT_CURRENT_COMMIT   # ### no visibility map written this act: the arms reading this name read the act's figures' commit
COMPUTE_TOOLS = ()              # ### the four compute tools of (R328)(4) are tools/b718_*.py and enter SEALED by its rule
REPAIRED_TOOLS = ()             # ### no shared tool repaired this act (CLOSE items are recorded, not repaired, (R328)(2))
REPAIRED_DATA = ()
STANDING_FILES = ('VERSION', 'act.py', 'allow.py', 'arms.py', 'close.py', 'components.py', 'controls.py', 'hook.py', 'repairs.py', 'replay.py',
                  'rootbanks.py', 'roster.py', 'scan.py', 'words.py')
NEW_TOOLS = tuple('standing/' + f for f in STANDING_FILES)   # ### the standing close toolset at v1.1.0, unchanged this act, sealed by hash beside the act's tools
# ### b717's commits the act reads ((R328)(1))
B714_CLOSING = '983dcbe27b5771acaedd84be04091b902218711c'   # ### b717's closing, the act's relay base (the names kept for the carried arms: the previous act's)
B714_RECORD = '78866b19ed7870f55dae7e92b37db947a003dbd9'
B714_ROOT = '4df4ddac46aa791068bb527b888497ebd435381360149d7866f5d0f386aeb327'   # ### data/act_roots.txt :94
# ### stage two (Component 5, before the lock): the commits of the components, read from the logs after each was made
C1_RELAY = '7c654dbe861caa912b0c30524cc095bf97990170'   # ### b717's weight line and the corrigendum's banks, the corrigenda row (37)
C1_PP = 'e0ab685b583eed3b1f9a35fbf673a603edf894ef'      # ### the weight line (:10722) and the corrigendum entry (:10724)
C2_RELAY = '3fdfacab1b55005cadf9b13778c150a455c99efb'   # ### (R328)(4)(i): the list at -39
C3_PRED = 'f47d8ab5840d287bf63c1f0b59ba707ed85dbe07'    # ### (R328)(4)(ii): data/b718_predictions.txt committed alone, before any onset (N2)
C3_RELAY = '091ecda9f44dbed5e9da97acb3250b3fb26cb8d5'   # ### (R328)(4)(iii): the onsets
C4_RELAY = '091f458676df418b6c9105e14ffe5df26d57add5'   # ### (R328)(4)(iv): the coefficients and the law
C5_PP = '84dbbf3e80e0520e24fb1726ca6d6e078e87d93d'   # ### (R328)(5)-(7)(ii): the companion, the six hits, the census v0.8.3, the Correspondence rows, ERRATA, the order
C5_RELAY = '97e4164bf0030c5162c3855cca9e7559e5c41bad'      # ### (R328)(5)-(6): their banks and diffs (the commit carrying this line; read from the log at the seal)
PP_EDITED = ('ERRATA.md', 'OPEN_TRAILS.md', 'day1/Exhaustive_Enumeration.md', 'day1/ONE_PAGE_PROOF.md', 'day1/Seven_Mechanism_Classes.md',
             'day1/Silence_of_Foundations.md', 'day1/Spectral_Inertness.md', 'day1/Third_Identity_Element.md',
             'day1/Silence_of_Foundations_CORRESPONDENCE.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md')   # ### data/b718_words_diffs.txt
ERRATA_ID = 'E-2026-10-27-2'   # ### (5); its companion entry for (6) beside it
ERRATA_IDS = ('E-2026-10-27-2', 'E-2026-10-27-3')
# ### the sealed list by the standing rule (tools/standing/close.py sealed_list: tools/<act>_*.py less the report tool, tools/standing/*.py and
# ### its VERSION), read here at import so the suite's arms and the seal read the one list
SEALED = tuple(sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b718_') and f.endswith('.py') and f != 'b718_report.py')) + NEW_TOOLS + COMPUTE_TOOLS
# ### the act's arms over its own banks: b717's ritual arms carried; its arms over b717's objects (the import closure, the roster from main, the
# ### pins census, the census rows) replaced by arms over this act's (the registrations first, the keystone edits, the prices, nothing built)
ACT_ARMS = ('G-ANSWERS-BEFORE-WRITES', 'G-ANSWERS-CHECKED', 'G-ARM-SECONDS-BANKED', 'G-BRANCHES-BANKED', 'G-CITATION-CHECKED',
            'G-CLOSING-DRY-STEP', 'G-CORRIGENDUM-ENTERED', 'G-DEFECTS-LETTERED', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN',
            'G-ENTRY-SCORES-EQUAL', 'G-ENTRY-TITLE-FORM', 'G-FIGURES-BANKED', 'G-GUARD-HELD', 'G-LISTINGS-BEFORE-CLAUSES', 'G-PARTS-PRERUN',
            'G-POSTROOT-WRITES-NONE', 'G-R328-ENTERED', 'G-READFIRST-DIFF-BANKED', 'G-REPORT-UNSEALED', 'G-ROOTDRY-READY', 'G-ROWGEN-STEPZERO',
            'G-RULES-ROW-ENTERED', 'G-SCORER-READS-BANKS', 'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS',
            'G-TRAIL-RESOLVED-EQUAL', 'G-WRITELIST-MIRROR-STATE',
            'G-MEMBRANE-WIRED', 'G-HOOK-WIRED', 'G-LETTERING-ONE', 'G-ACT-CURRENT', 'G-NO-DISPATCH',
            'G-REGISTRATIONS-FIRST', 'G-LIST-CERTIFIED', 'G-PREDICTIONS-BEFORE-ONSETS', 'G-ONSETS-HELD', 'G-COEFFS-LAW',
            'G-KEYSTONE-EDITS', 'G-NAMES-PINNED', 'G-PRICES-BANKED', 'G-ARM-TAGS')
# ### Component 6 (the Edit tool): b717's arms over b717's toolset objects (G-TOOL-REPAIRS, G-REPAIR-CONTROLS, G-TOOLSET-SCAN, G-TOOLSET-REPLAY,
# ### G-COVERAGE-TABLE) not carried -- their banks are b717's and this act writes none; the -39 test's, the names' and the tags' arms added
