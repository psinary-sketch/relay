# -*- coding: utf-8 -*-
"""b767_face.py -- THE ACT'S FACE, COMPOSED: b766's sealed face (lines above its lock block) read unedited, the standing paragraphs between b766's blocks carried by the
act shift, the act's own blocks from tools/b767_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b766's own blocks' first and last lines in b766's face, no line number kept.
Writes data/b767_registration_<DATE>.txt alone, and only before the lock: it refuses when the face already carries a lock block. Carried from tools/b766_face.py by tools/b767_carry.py (data/b767_carry_face.txt),
its OLD, MAP, PAT, the LOGS comment, FIXES and the summaries reader set by hand before any run (data/b767_events.txt (111)), and the arms declared before the lock (DECLARED, DECLARED_LINES, NEWLY) set by hand from the probes
(data/b767_probe_<part>.txt) and the pre-lock comparison, empty and PENDING until then.
### (R377)(13): the (W) row and N5's write clause regenerated from the ruling by tools/standing/amend.py over the act's three amendment rows (data/b767_amendments.json: the author's words of 2026-11-21 on W-ORD-H2-PI1, on the runner's cache and on the save on main, each widening none and narrowing none), the regeneration printed into the face's (W) section before the lock.
### The face is written whole to a scratch name beside it and moved over the face only after the write returns (no zero-byte husk on an error).
### Composed after the act's last commit before the gate and before the gate's add (tools/standing/fold/checks.tpl nothing_ahead_ok reads every commit to
### the lock declared on the face by hash but the gate's step commits).
"""
import os
import re
import subprocess
import sys

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
from standing import faceform as FF   # noqa: E402,F401
from standing.faceform import PRE_FACE_TITLE   # noqa: E402
from standing import amend as AM   # noqa: E402
import b767_worklist as K   # noqa: E402
OLD, NEW = os.path.join(D, 'b766_registration_2026-11-22.txt'), os.path.join(D, 'b767_registration_%s.txt' % K.DATE)   # ### b767: b766's face by its own date (the carry shifted b765's -11-21)
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b766_face_blocks.txt'), os.path.join(T, 'b767_face_blocks.txt')
FERRY = os.path.join(D, 'b767_ferry.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'zq-b730', 'scratch-b724', 'rebuild-b721', 'b732_phase2_frontdoors')
# ### b767 (the Edit tool, before any run, data/b767_events.txt (111)): the shift of b766's face by one act (b766 -> b767, b765 -> b766,
# ### R376 -> R377), one pass of one alternation so that no name is shifted twice; tools/standing/ moved by (R377)(8) alone, v1.38.24 to
# ### v1.38.25 ([K25], data/b767_repairs.txt), which b767's own blocks say; a name two acts back, b764's among them, stands unshifted (the
# ### carry had left b766's pair b764 -> b765 carried to b764 -> b766, and b766's face's date as b765's -11-21)
MAP = {'b766_registration_2026-11-22': 'b767_registration_%s' % K.DATE, 'b766': 'b767', 'b765': 'b766', '(R376)': '(R377)', 'R376': 'R377'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('b766_registration_2026-11-22', '(R376)', 'R376', 'b766', 'b765')))
# ### b767: b766's closing commits as (R377)'s SCOPE READ gives them, relay a0bc04cd and PLACE-papers 29de0836 (data/b767_ferry.txt :3), the
# ### worklist's PRE_RELAY and PRE_PP: the pre-face commits after them (the carry had left b765's 29d4c9b7 and 5638a9ad in this comment)
LOGS = ((ROOT, K.PRE_RELAY), (K.PP, K.PRE_PP))
W_ANCHOR = '### No Zeta23 or vendored byte;'
# ### b767 (the Edit tool, before any run, data/b767_events.txt (111)): three sentences of b766's face carried between its blocks read
# ### against b767 (b766's face :202, :244, :252 and :279, the search tool, 18:3xZ) and set. (G1)'s order at :202 names "COMPONENTS 0-4 AND
# ### COMPONENT 5`S BANKS", b766's ferry's components and b767's alike (data/b767_ferry.txt :115-:120), and stands. The freeze paragraph
# ### (:244) and the arms' paragraph (:279) name "(R376)(12)`s (W) list" and "(R376)(12)`s (W) row", shifted to (R377)(12)'s; b767's (W)
# ### list is (R377)(13)'s (data/b767_ferry.txt :53). The arms' paragraph (:252) reads G-DELETES-ONE-BRANCH's allowance "through
# ### tools/standing/allow.py at v1.38.24", b766's VERSION; b767's is v1.38.25 by [K25] (tools/standing/VERSION :1)
FIXES = (
    ('(outside (R377)(12)`s (W) list)', '(outside (R377)(13)`s (W) list)'),
    ('read (R377)(12)`s (W) row and the rules banks', 'read (R377)(13)`s (W) row and the rules banks'),
    ('tools/standing/allow.py at v1.38.24', 'tools/standing/allow.py at v1.38.25'),
)
# ### b766's three, as b766 set them (the carry shifting their names), and b765's as b766 kept them
FIXES_B766 = (
    ('(outside (R377)(13)`s (W) list)', '(outside (R377)(12)`s (W) list)'),
    ('read (R377)(13)`s (W) row and the rules banks', 'read (R377)(12)`s (W) row and the rules banks'),
    ('tools/standing/allow.py at v1.38.21', 'tools/standing/allow.py at v1.38.24'),
)
FIXES_B765 = (
    ('(outside (R376)(14)`s (W) list)', '(outside (R376)(13)`s (W) list)'),
    ('read (R376)(14)`s (W) row and the rules banks', 'read (R376)(13)`s (W) row and the rules banks'),
    ('tools/standing/allow.py at v1.38.18', 'tools/standing/allow.py at v1.38.21'),
)
# ### b767 (the Edit tool, before any run, data/b767_events.txt (111)): the arms failing at the pre-run on real state, declared by name before
# ### the lock, each with its reason, are set from b767's own probes and its pre-lock comparison when they are run; until then None, and the
# ### face refuses to compose (main() below). b766's six, as carried (the carry's substitution shifting their names), kept beside as _B766.
DECLARED = None
DECLARED_LINES = None
NEWLY = None
# ### b766's, as b766 wrote them (the carry shifting their names): b766 (the Edit tool, 23:1xZ, after the probes and
# ### `tools/standing/prelock.py print b766` at 23:01:45Z, b766 events (118)): b765's four, each ground read again against b766's own state
# ### and written new, and two beyond them, G-RUNNER-GATE (b766 defect (h)) and G-PUSHOUT-COMMITTED (b766 defect (r)); G-DELETE-FREE on
# ### tools/project_set.py :542 (b766 defect (s)). NEWLY_B766 the thirteen of b766's pre-lock print.
DECLARED_B766 = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN', 'G-DELETE-FREE', 'G-RUNNER-GATE', 'G-PUSHOUT-COMMITTED')
DECLARED_LINES_B766 = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried; the arm at tools/standing/fold/checks.tpl :1783) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b766 declared it on its face (data/b766_registration_2026-11-21.txt).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :127), as at b766`s pre-run. b767 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b767_*cut* in the tree), so it adds to neither count, and the searches read failing NONE (:38). (R377) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11; the arm at tools/standing/fold/checks.tpl :1779); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean, b726`s certificates carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b766. b767 moves no main: SIDE-explicit-formula`s main stands at 0ba9cd61 by the author`s word (data/b767_author_words_preseal.txt :32), the act`s Lean on push-b767-proof alone, which the arm does not read, and the kernel`s clone stood at main when standing-a1 ran (data/b767_events.txt (115)); the count stands at b766`s 15. The axioms print of run 44918855502, the build from source at main 0ba9cd61, reads 593 axiom lines each within the standard three and sorryAx nowhere (data/b766_events.txt (58)), so no fallback branch was taken; the counter counts the text.",
    "### `G-DELETE-FREE` reads the act`s own tools, their code with prose stripped, and of a shared tool the ruling orders edited the lines this act added (tools/standing/fold/checks.tpl :239-:246, :1814), for a delete call of any kind, a temporary folder`s cleanup set apart where the call`s first argument is a name the same file bound from tempfile or a parameter every call of which passes one (tools/standing/deletefree.py :1-:12); it fails on one line, in tools/project_set.py`s write route as [K24] edited it (relay 751b9e7a): `os.remove(os.path.join(CLONE, x))` at :542, the removal from the Project set`s clone of each name its index holds that the close`s export does not, before the set is written (the probe of standing-a2 :80; data/b767_defects.txt (s)). The route runs at the close`s step [23a], in the Project`s clone on the act`s branch, so that the repository equals the export file for file as (R377)(7) [K24] orders; nothing of the relay, PLACE-papers or a kernel is removed by it, and what it removes is kept in its record as `removed`. The tool ran its control in that form (data/b767_repair_controls.txt) and is not edited after it; b766`s line in the control, now :378, is b766`s and not read at b767.",
    "### `G-RUNNER-GATE` wants one command in the capture for each dispatch row, the route`s commands those of `gh workflow run` or of tools/b767_controls.py`s dispatch route not dry (tools/acts/b767.py :1048-:1049, :1054; the predicate at tools/standing/fold/checks.tpl :1231-:1242, the arm at tools/acts/b767.py :1451): the dispatch rows 16 and EF_RUNS 16, every row above the hold, the restore on 14 and off for the closing build and its repeat alone; the route`s commands in the capture 17, the one beyond a row the command of 11:19:08Z whose dispatch route the price row`s guard refused at 11:20:41Z, nothing sent (data/b767_events.txt (59), (116); data/b767_defects.txt (h)). Read on the composed sources the predicate is False as composed and True on a copy without that one command (scratch gate766b.py, 21:34:53Z). The capture is the act`s and is not edited; no dispatch went out beyond the sixteen rows.",
    "### `G-PUSHOUT-COMMITTED` wants the worklist`s STEPZERO commit to carry data/b766_relay_push-b766-closing_push_out.txt alone and to stand an ancestor of HEAD (tools/standing/fold/checks.tpl :1674, the sources at :602), b766`s step zero having committed b764`s closing push-out so; b767`s step zero committed c323bf50, data/b767_address_scan_commits.txt alone (tools/b767_worklist.py :389), because b766`s closing push-out carried the account and (R377)(3) and (7) [K23] put b766`s eight captures, masked, in Component 1, committed together at d09d93ab (data/b767_events.txt (39), (116)). No commit can give the arm its object: the capture stands committed masked with the seven others, and none is rewritten (data/b767_defects.txt (r)).",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and appended to the post-seal events bank at step [21] for the next corrigendum, not a letter (the ferry`s Component 5, data/b767_ferry.txt :125; (R374)(5) [K10], standing).",
)
NEWLY_B766 = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD', 'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD',
         'G-PUSHOUT-COMMITTED', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-RUNNER-GATE', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS',
         'G-WRITELIST-MIRROR-STATE')
# ### b766's, as b766 wrote them: the arms failing at the pre-run on real state, declared by name before the lock, each with its reason; set from the probes. b766 (the
# ### Edit tool, 22:2xZ): b764's four, each line read against b767's own state from b767's probes (standing-a1 :20, :23 at 20:33:44Z;
# ### standing-a2 :38, :80, :127 at 20:59:57Z, its 25 failing b766's 25 by name), G-DELETE-FREE now on tools/project_set.py :340 (defect
# ### (t)); every cite read at its line before it was written (checks.tpl :1779, :1783, :1814; b649_checks.py :452-:454; no_sorry_main.py
# ### :4-:11; rule_arms.py :389, :617; deletefree.py :1-:12; project_set.py :308, :332, :340, :348). NEWLY the twelve of
# ### `tools/standing/prelock.py print b767` at 22:11:44Z, G-DELETE-FREE not among them, failing at b766's pre-run.
DECLARED_B765 = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN', 'G-DELETE-FREE')
DECLARED_LINES_B765 = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried; the arm at tools/standing/fold/checks.tpl :1783) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b766 declared it on its face (data/b766_registration_2026-11-20.txt).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :127), as at b766`s pre-run. b767 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b767_*cut* in the tree; the cuts of (7) are written beside the archive, outside the relay), so it adds to neither count, and the searches read fail NONE (:38). (R377) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11; the arm at tools/standing/fold/checks.tpl :1779); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean, b726`s certificates carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b766. b767`s three files of (5), on main since (4)`s HELD, add no token: the count stands at b766`s 15, and each build that compiled them read sorry warnings 0 (data/b767_events.txt (48), (54), (58)). The axioms print of run 44918855502, the build from source of v0.44`s tree at main 0ba9cd61, reads 593 axiom lines each within the standard three and sorryAx nowhere, the 18 certificate names of print_targets.txt among its targets (read at main by count), so no fallback branch was taken (data/b767_events.txt (58)); the counter counts the text.",
    "### `G-DELETE-FREE` reads the act`s own tools, their code with prose stripped, for a delete call of any kind, a temporary folder`s cleanup set apart where the call`s first argument is a name the same file bound from tempfile or a parameter every call of which passes one (tools/standing/fold/checks.tpl :1814, tools/standing/deletefree.py :1-:12); it fails on one line of tools/project_set.py, (7)`s builder: in its control, `os.remove(os.path.join(tmp, gone))` at :340, the planted removal of one copy from the folder the control made by tempfile.mkdtemp at :332, which the case A COPY REMOVED reads as MISSING, a joined path the reader does not set apart; the tool`s two folder cleanups by shutil.rmtree at :308 and :348 set apart (the probe of standing-a2 :80; data/b767_defects.txt (t)). It removes a file the same control copied under the system`s temporary folder, and nothing of the record is deleted. The tool ran and banked in that form (data/b767_project_set_control.txt) and is not edited, as b766 kept its own for b766 (i); that the reader does not follow a joined temporary path is a fault of tools/standing/, which (R377)(11) moves under (8) and (4) alone, carried to the next reading of the close.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and appended to the post-seal events bank at step [21] for the next corrigendum, not a letter (the ferry`s Component 5, data/b767_ferry.txt :132; (R376)(5) [K10], standing).",
)
NEWLY_B765 = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD', 'G-LOCKGATE-EIGHT',
         'G-NOTHING-RAN-AHEAD', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS',
         'G-WRITELIST-MIRROR-STATE')
# ### b764's, as b766 kept them (the carry's substitution shifting their names)
DECLARED_B764 = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN', 'G-DELETE-FREE')
DECLARED_LINES_B764 = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried; the arm at tools/standing/fold/checks.tpl :1783) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b766 carried it (data/b766_events.txt (85)).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :127), as at b766`s pre-run. b767 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b767_*cut.txt in the tree), so it adds to neither count, and the searches read fail NONE (:38). (R377) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11; the arm at tools/standing/fold/checks.tpl :1779); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20, :22): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean, b726`s certificates (commit c9add92) carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b766. The axioms print of run 44670834879, the run that built v0.43`s tree at main 819e4a83, reads each C2Walk.cert_m<n> with no axiom (its artifact`s axioms.txt :136-:153, as b766 read it, data/b766_events.txt (85)), so no fallback branch was taken and sorryAx stands nowhere in its print; the counter counts the text. b767 writes no Lean byte: its one kernel write is the workflow`s file on push-b767-runner, and the kernel`s clone stood at main when standing-a1 ran (data/b767_events.txt (57)); (R377) removes no kernel branch ((4)), and the M<n> files stand as landed.",
    "### `G-DELETE-FREE` reads the act`s own tools, their code with prose stripped, for a delete call of any kind, a temporary folder`s cleanup set apart where the call`s first argument is a name the same file bound from tempfile or a parameter every call of which passes one (tools/standing/fold/checks.tpl :1814, tools/standing/deletefree.py :1-:12); it fails on five lines of tools/b767_repair_controls.py, the controls` cleanups in their finally blocks at :874-:876, :957-:959, :1047-:1049, :1137-:1139 and :1237-:1239, each `shutil.rmtree(t_, ignore_errors=True)` in a loop over the block`s own tempfile.mkdtemp folders, the path read absolute and its name by the control`s own prefix before the call, a loop variable the reader does not follow (the probe of standing-a2 :80; data/b767_defects.txt (i)). Each removes a folder its own block made under the system`s temporary folder, and nothing of the record is deleted. The tool ran and banked in that form (data/b767_repair_controls.txt) and is not edited, as b762 kept its own for b762 (j); that the reader does not follow a loop variable is a fault of tools/standing/, which (R377)(12) moves under (5) and (7) alone, carried to the next act of the record`s upkeep.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and appended to the post-seal events bank at step [21] for the next corrigendum, not a letter (the ferry`s Component 5, data/b767_ferry.txt :155; (R377)(5) [K10]).",
)
NEWLY_B764 = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DELETE-FREE', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD',
         'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS',
         'G-WRITELIST-MIRROR-STATE')
# ### b766's comment on its three, as b766 wrote it (the carry shifting its names): DECLARED and DECLARED_LINES set by hand from b766's probes
# ### (standing-a1 :20, :22, :23 at 01:16:37Z; standing-a2 :38, :80, :127 at 01:21:42Z, and again at 02:30:37Z with the same 25 failing by
# ### name): b763's three, each line read against b766's own state, and G-DELETE-FREE for b766's defect (i). NEWLY the thirteen of
# ### `tools/standing/prelock.py print b766` at 02:38:52Z. b767's set from b767's probes and its pre-lock comparison when they are run.


def shift(s):
    return PAT.sub(lambda m: MAP.get(m.group(0), m.group(0)), s)


def blocks(path):
    out, cur = {}, None
    for l in open(path, encoding='utf-8').read().split('\n'):
        m = re.match(r'^@@@ (\S+)$', l)
        if m:
            cur = m.group(1)
            out[cur] = []
        elif cur:
            out[cur].append(l)
    return {k: '\n'.join(v).rstrip('\n') for k, v in out.items()}


def carried(o, old):
    """the paragraphs of b766's face standing between its blocks: gap[k], the lines after block k up to the next; the lines found by each block's own last
    and first lines, each read once."""
    gaps = {}
    i = 0
    for n, k in enumerate(ORDER):
        ls = old[k].split('\n')
        first = next(l for l in ls if l and '@@' not in l)
        last = ls[-1]
        a = o.index(first, i)
        b = o.index(last, a)
        if n:
            gaps[ORDER[n - 1]] = o[i:a]
        i = b + 1
    return gaps


WORDS = ('no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 'twenty-four')


def _refusal_rows(act):
    """the hook's refusals bank of an act, one row a line ("<time> | <KIND> | <tool> | ..."), as (line number, time, kind); () where absent."""
    p = os.path.join(D, '%s_hook_refusals.txt' % act)
    if not os.path.exists(p):
        return ()
    out = []
    for n, l in enumerate(open(p, encoding='utf-8').read().split('\n'), 1):
        f = [x.strip() for x in l.split(' | ')]
        if len(f) >= 2 and re.match(r'^\d{4}-\d\d-\d\dT[\d:]+Z$', f[0]) and re.match(r'^[A-Z]+$', f[1]):
            out.append((n, f[0], f[1]))
    return tuple(out)


def _kinds(rows):
    k = {}
    for _n, _t, kind in rows:
        k[kind] = k.get(kind, 0) + 1
    return k


def refusals():
    """### b767, from the bank (no count kept by hand): the hook's refusals before this lock counted by kind, against b766's bank, and the kinds
    above b766's count, each one event by [U3] (data/b754_rules.txt (12)). Returns (n, kinds, sentence)."""
    own, prev = _refusal_rows('b767'), _refusal_rows('b766')
    ko, kp = _kinds(own), _kinds(prev)
    kinds = ', '.join('%s %d' % (k, ko[k]) for k in sorted(ko)) or 'NONE'
    pk = ', '.join('%s %d' % (k, kp[k]) for k in sorted(kp)) or 'none'
    if not own:
        return '0', 'NONE', ('The hook refused nothing before this lock (data/b767_hook_refusals.txt absent), so by [U3] no kind stands above '
                             'b766`s count (data/b766_hook_refusals.txt: %s).' % pk)
    rows = '; '.join('%s :%d %s' % (kind, n, t[11:]) for n, t, kind in own)
    above = ', '.join('%s %d against %d' % (k, ko[k], kp.get(k, 0)) for k in sorted(ko) if ko[k] > kp.get(k, 0))
    s = ('The hook refused %d call%s before this lock, each before it ran (data/b767_hook_refusals.txt: %s), counted by kind %s against b766`s '
         'bank`s %s; by [U3] each kind above b766`s count is one event of data/b767_events.txt and takes no letter: %s.'
         % (len(own), '' if len(own) == 1 else 's', rows, kinds, pk, above or 'none above it'))
    return str(len(own)), kinds, s


def summaries():
    """### b767 (the Edit tool, before any run, data/b767_events.txt (111)), from the events bank: the act's summaries of the session, the rows
    of any actor whose head names a SUMMARY or SUMMARIES -- b767 entered each in the host's rows, (4) to (110), and the reader takes any
    actor's as b766's did. A row's head is read across its lines, from its tag to the first full stop after which most letters of the next
    thirty characters are small (the body's opening, "A summary of the session ..." among them); each row counted for each
    summary its head names (two for "TWO SUMMARIES", three for "THREE SUMMARIES"; otherwise one, and one more for each " AND A " in the clause
    naming it), and b766's eleven findings after its lock (b767 events (20) to (30), under the head COMPONENT 1 with no section of their
    own, row (30) b766's summary between its closing add and its commit) left out by their numbers, row (20) read as "the first of eleven"
    and row (30) as "The eleventh of the eleven" before they are left out. The count read against the chain read's boundaries after the
    delivery's line by hand before the face is composed (18 to :310085 at the summary of 18:38:15Z). Returns the phrase "<n words>
    summaries within it (events (a), ..., (z))"."""
    t = open(os.path.join(D, 'b767_events.txt'), encoding='utf-8').read()
    def _row(n_, src_):
        m_ = re.search(r"(?ms)^    \(%d\) .*?(?=^    \(\d+\) |^\S|\Z)" % n_, src_)
        return m_.group(0) if m_ else ''
    r20_, r30_ = ' '.join(_row(20, t).split()), ' '.join(_row(30, t).split())
    if 'the first of eleven' not in r20_ or 'The eleventh of the eleven' not in r30_:
        raise SystemExit("REFUSED: the events bank's rows (20) and (30) not read as the first and the last of b766's eleven findings after its lock")
    FOUND_AFTER_B766 = set(str(n_) for n_ in range(20, 31))
    hits = []
    for m in re.finditer(r"(?ms)^    \((\d+)\) THE [A-Z']+ \[[^\]]*\]: (.*?)(?=^    \(\d+\) |^\S|\Z)", t):
        row_ = ' '.join(x_.strip() for x_ in m.group(2).split('\n'))
        head_ = row_
        for p_ in re.finditer(r'\. ', row_):
            nx_ = [c_ for c_ in row_[p_.end():p_.end() + 30] if c_.isalpha()]
            if nx_ and sum(1 for c_ in nx_ if c_.islower()) * 2 > len(nx_):
                head_ = row_[:p_.start() + 1]
                break
        cl_ = [c_ for c_ in head_.split(';') if re.search(r'\bSUMMAR(?:Y|IES)\b', c_)]
        if not cl_ or 'BEFORE THE DELIVERY' in head_ or m.group(1) in FOUND_AFTER_B766:
            continue
        c_ = cl_[0]
        hits.append((m.group(1), 2 if 'TWO SUMMARIES' in c_ else 3 if 'THREE SUMMARIES' in c_ else 1 + c_.split('SUMMAR')[0].count(' AND A ')))
    ns, n_ = [h_[0] for h_ in hits], sum(h_[1] for h_ in hits)
    lst = ', '.join('(%s)' % n for n in ns[:-1]) + (' and (%s)' % ns[-1] if len(ns) > 1 else '(%s)' % ns[-1] if ns else '')
    return '%s summar%s within it (events %s)' % (WORDS[n_] if n_ < len(WORDS) else n_, 'y' if n_ == 1 else 'ies', lst)


def pre_face():
    hs = []
    for repo, r in LOGS:
        rng = r if '..' in r else r + '..HEAD'
        hs += subprocess.run(['git', '-C', repo, 'rev-list', '--reverse', rng], capture_output=True, text=True).stdout.split()
    return ' '.join(h[:8] for h in hs)


def main():
    if os.path.exists(NEW) and 'THE REGISTRATION LOCK' in open(NEW, encoding='utf-8').read():
        print('REFUSED: the face carries its lock block')
        return 2
    if DECLARED is None or DECLARED_LINES is None:   # ### b767: the declared arms set from b767's probes before any composition
        print('REFUSED: DECLARED and DECLARED_LINES not set from b767`s probes')
        return 2
    o = open(OLD, encoding='utf-8', newline='').read().split('\n')
    o = o[:o.index(next(l for l in o if l.startswith('### THE REGISTRATION LOCK'))) - 1]
    G = carried(o, blocks(OLD_BLOCKS))
    B = blocks(BLOCKS)
    parts = []
    for k in ORDER:
        parts += [B[k]] + [shift(l) for l in G.get(k, [])]
    t = '\n'.join(parts) + '\n'
    t = t.replace('@@PREFACE@@', PRE_FACE_TITLE + ' ' + pre_face())
    t = t.replace('@@DATE@@', K.DATE)
    rn, rk, rs = refusals()
    t = t.replace('@@REFUSED_N@@', rn).replace('@@REFUSED_KINDS@@', rk).replace('@@REFUSALS_ZERO@@', rs)
    t = t.replace('@@SUMMARIES@@', summaries())
    t = t.replace('@@DECLARED@@', ' '.join('`%s`' % a for a in DECLARED) + '.' if DECLARED else 'NONE.')
    t = t.replace('@@DECLARED_LINES@@\n', ''.join(l + '\n' for l in DECLARED_LINES))
    t = t.replace('@@NEWLY@@', 'PENDING (tools/standing/prelock.py print b767 not yet run)' if NEWLY is None else (' '.join('`%s`' % a for a in NEWLY) if NEWLY else 'NONE'))
    for a_, b_ in FIXES:
        if t.count(a_) != 1:
            print('REFUSED: a carried sentence to set found %d times: %s' % (t.count(a_), a_[:80].replace('\n', ' / ')))
            return 2
        t = t.replace(a_, b_)
        print('SET:', b_[:100].replace('\n', ' / '))
    left = [x for x in re.findall(r'@@\w+@@', t) if x != '@@N5_WRITES@@']
    if left:
        print('REFUSED: unfilled', sorted(set(left)))
        return 2
    stale = sorted(set(re.findall(r'b767_registration_(?!%s)[\d-]+' % K.DATE, t)))
    if stale:
        print('REFUSED: a stale face date', stale)
        return 2
    ferry = open(FERRY, encoding='utf-8', newline='').read()
    rows = AM.rows_of('b767')
    row = AM.w_row(ferry, rows, t)
    if t.count(W_ANCHOR) != 1:
        print('REFUSED: the (W) anchor')
        return 2
    if row:
        t = t.replace(W_ANCHOR, row + '\n' + W_ANCHOR)
    regen = AM.regenerate('b767', ferry, t, rows)
    t = t.replace(W_ANCHOR, '\n'.join(regen) + '\n' + W_ANCHOR)
    t = t.replace('@@N5_WRITES@@', AM.n5_clause(ferry, rows, t).upper())
    left = re.findall(r'@@\w+@@', t)
    if left:
        print('REFUSED: unfilled', sorted(set(left)))
        return 2
    print('\n'.join(regen))
    print('(W) COVERS THE RULING`S CLAUSE-ORDERED FILES:', AM.writes(ferry, rows), '; THE COMPOSER`S ROW:', row or 'NONE NEEDED', '; MISSING AFTER:', AM.missing(ferry, rows, t))
    if '--dry' in sys.argv:
        print('DRY: nothing written', len(t), 'chars', t.count('\n'), 'lines')
        if '--show' in sys.argv:
            print(t)
        return 0
    tmp = NEW + '.part'
    with open(tmp, 'w', encoding='utf-8', newline='') as f:
        f.write(t)
    os.replace(tmp, NEW)
    print('WROTE', NEW, len(t), 'chars', t.count('\n'), 'lines')
    return 0


if __name__ == '__main__':
    sys.exit(main())
