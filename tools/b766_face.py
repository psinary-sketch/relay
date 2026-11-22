# -*- coding: utf-8 -*-
"""b766_face.py -- THE ACT'S FACE, COMPOSED: b765's sealed face (lines above its lock block) read unedited, the standing paragraphs between b765's blocks carried by the
act shift, the act's own blocks from tools/b766_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b765's own blocks' first and last lines in b765's face, no line number kept.
Writes data/b766_registration_<DATE>.txt alone, and only before the lock: it refuses when the face already carries a lock block. Carried from tools/b765_face.py by tools/b766_carry.py (data/b766_carry_face.txt),
its OLD, MAP, PAT, the LOGS comment, FIXES and the summaries reader set by hand before any run (data/b766_events.txt (101)), and the arms declared before the lock (DECLARED, DECLARED_LINES, NEWLY) set by hand from the probes
(data/b766_probe_<part>.txt) and the pre-lock comparison, empty and PENDING until then.
### (R376)(13): the (W) row and N5's write clause regenerated from the ruling by tools/standing/amend.py over the act's three amendment rows (data/b766_amendments.json: the author's words of 2026-11-21 on W-ORD-H2-PI1, on the runner's cache and on the save on main, each widening none and narrowing none), the regeneration printed into the face's (W) section before the lock.
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
import b766_worklist as K   # noqa: E402
OLD, NEW = os.path.join(D, 'b765_registration_2026-11-21.txt'), os.path.join(D, 'b766_registration_%s.txt' % K.DATE)   # ### b766: b765's face by its own date (the carry shifted b764's -11-20)
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b765_face_blocks.txt'), os.path.join(T, 'b766_face_blocks.txt')
FERRY = os.path.join(D, 'b766_ferry.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'zq-b730', 'scratch-b724', 'rebuild-b721', 'b732_phase2_frontdoors')
# ### b766 (the Edit tool, before any run, data/b766_events.txt (101)): the shift of b765's face by one act (b765 -> b766, b764 -> b765,
# ### R375 -> R376), one pass of one alternation so that no name is shifted twice; tools/standing/ moved by (R376)(7) alone, v1.38.21 to
# ### v1.38.24 (data/b766_repairs.txt), which b766's own blocks say; a name two acts back, b763's among them, stands unshifted (the carry
# ### had left b765's pair b763 -> b764 carried to b763 -> b765, and b765's face's date as b764's -11-20)
MAP = {'b765_registration_2026-11-21': 'b766_registration_%s' % K.DATE, 'b765': 'b766', 'b764': 'b765', '(R375)': '(R376)', 'R375': 'R376'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('b765_registration_2026-11-21', '(R375)', 'R375', 'b765', 'b764')))
# ### b766: b765's closing commits as (R376)'s SCOPE READ gives them, relay 29d4c9b7 and PLACE-papers 5638a9ad (data/b766_ferry.txt :3), the
# ### worklist's PRE_RELAY and PRE_PP: the pre-face commits after them (the carry had left b764's 306162ad and 1198a637 in this comment)
LOGS = ((ROOT, K.PRE_RELAY), (K.PP, K.PRE_PP))
W_ANCHOR = '### No Zeta23 or vendored byte;'
# ### b766 (the Edit tool, before any run, data/b766_events.txt (101)): three sentences of b765's face carried between its blocks read
# ### against b766 (b765's face :201, :243, :251 and :278, the search tool, 18:2xZ) and set. (G1)'s order at :201 names "COMPONENTS 0-4 AND
# ### COMPONENT 5`S BANKS", b765's ferry's components and b766's alike (data/b766_ferry.txt :120-:125), and stands. The freeze paragraph
# ### (:243) and the arms' paragraph (:278) name "(R375)(13)`s (W) list" and "(R375)(13)`s (W) row", carried as (R376)(13)'s; b766's (W)
# ### list is (R376)(12)'s (:46). The arms' paragraph (:251) reads G-DELETES-ONE-BRANCH's allowance "through tools/standing/allow.py at
# ### v1.38.21", b765's VERSION; b766's is v1.38.24 (tools/standing/VERSION :1). b765's three kept below as b765 set them
FIXES = (
    ('(outside (R376)(13)`s (W) list)', '(outside (R376)(12)`s (W) list)'),
    ('read (R376)(13)`s (W) row and the rules banks', 'read (R376)(12)`s (W) row and the rules banks'),
    ('tools/standing/allow.py at v1.38.21', 'tools/standing/allow.py at v1.38.24'),
)
FIXES_B765 = (
    ('(outside (R375)(14)`s (W) list)', '(outside (R375)(13)`s (W) list)'),
    ('read (R375)(14)`s (W) row and the rules banks', 'read (R375)(13)`s (W) row and the rules banks'),
    ('tools/standing/allow.py at v1.38.18', 'tools/standing/allow.py at v1.38.21'),
)
# ### b766 (the Edit tool, before any run, data/b766_events.txt (101)): the arms failing at the pre-run on real state, declared by name before
# ### the lock, each with its reason, are set from b766's own probes and its pre-lock comparison when they are run; until then None, and the
# ### face refuses to compose (main() below). b765's three, as carried (the carry's substitution shifting their names), kept beside.
# ### b766 (the Edit tool, 23:1xZ, after the probes and `tools/standing/prelock.py print b766` at 23:01:45Z, data/b766_events.txt (118)):
# ### b765's four, each ground read again against b766's own state and written new (the carried lines below shifted by the carry), and
# ### two beyond them, G-RUNNER-GATE (defect (h)) and G-PUSHOUT-COMMITTED (defect (r)); G-DELETE-FREE now on tools/project_set.py :542
# ### (defect (s)); every cite read at its line before it was written (checks.tpl :239-:246, :602, :1231-:1242, :1674, :1779, :1783,
# ### :1814; b649_checks.py :452-:454; no_sorry_main.py :4-:11; rule_arms.py :389, :617; deletefree.py :1-:12; project_set.py :378,
# ### :542; tools/acts/b766.py :1048-:1049, :1054, :1451; tools/b766_worklist.py :389). NEWLY the thirteen of the pre-lock print.
DECLARED = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN', 'G-DELETE-FREE', 'G-RUNNER-GATE', 'G-PUSHOUT-COMMITTED')
DECLARED_LINES = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried; the arm at tools/standing/fold/checks.tpl :1783) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b765 declared it on its face (data/b765_registration_2026-11-21.txt).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :127), as at b765`s pre-run. b766 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b766_*cut* in the tree), so it adds to neither count, and the searches read failing NONE (:38). (R376) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11; the arm at tools/standing/fold/checks.tpl :1779); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean, b726`s certificates carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b765. b766 moves no main: SIDE-explicit-formula`s main stands at 0ba9cd61 by the author`s word (data/b766_author_words_preseal.txt :32), the act`s Lean on push-b766-proof alone, which the arm does not read, and the kernel`s clone stood at main when standing-a1 ran (data/b766_events.txt (115)); the count stands at b765`s 15. The axioms print of run 44918855502, the build from source at main 0ba9cd61, reads 593 axiom lines each within the standard three and sorryAx nowhere (data/b765_events.txt (58)), so no fallback branch was taken; the counter counts the text.",
    "### `G-DELETE-FREE` reads the act`s own tools, their code with prose stripped, and of a shared tool the ruling orders edited the lines this act added (tools/standing/fold/checks.tpl :239-:246, :1814), for a delete call of any kind, a temporary folder`s cleanup set apart where the call`s first argument is a name the same file bound from tempfile or a parameter every call of which passes one (tools/standing/deletefree.py :1-:12); it fails on one line, in tools/project_set.py`s write route as [K24] edited it (relay 751b9e7a): `os.remove(os.path.join(CLONE, x))` at :542, the removal from the Project set`s clone of each name its index holds that the close`s export does not, before the set is written (the probe of standing-a2 :80; data/b766_defects.txt (s)). The route runs at the close`s step [23a], in the Project`s clone on the act`s branch, so that the repository equals the export file for file as (R376)(7) [K24] orders; nothing of the relay, PLACE-papers or a kernel is removed by it, and what it removes is kept in its record as `removed`. The tool ran its control in that form (data/b766_repair_controls.txt) and is not edited after it; b765`s line in the control, now :378, is b765`s and not read at b766.",
    "### `G-RUNNER-GATE` wants one command in the capture for each dispatch row, the route`s commands those of `gh workflow run` or of tools/b766_controls.py`s dispatch route not dry (tools/acts/b766.py :1048-:1049, :1054; the predicate at tools/standing/fold/checks.tpl :1231-:1242, the arm at tools/acts/b766.py :1451): the dispatch rows 16 and EF_RUNS 16, every row above the hold, the restore on 14 and off for the closing build and its repeat alone; the route`s commands in the capture 17, the one beyond a row the command of 11:19:08Z whose dispatch route the price row`s guard refused at 11:20:41Z, nothing sent (data/b766_events.txt (59), (116); data/b766_defects.txt (h)). Read on the composed sources the predicate is False as composed and True on a copy without that one command (scratch gate766b.py, 21:34:53Z). The capture is the act`s and is not edited; no dispatch went out beyond the sixteen rows.",
    "### `G-PUSHOUT-COMMITTED` wants the worklist`s STEPZERO commit to carry data/b765_relay_push-b765-closing_push_out.txt alone and to stand an ancestor of HEAD (tools/standing/fold/checks.tpl :1674, the sources at :602), b765`s step zero having committed b764`s closing push-out so; b766`s step zero committed c323bf50, data/b766_address_scan_commits.txt alone (tools/b766_worklist.py :389), because b765`s closing push-out carried the account and (R376)(3) and (7) [K23] put b765`s eight captures, masked, in Component 1, committed together at d09d93ab (data/b766_events.txt (39), (116)). No commit can give the arm its object: the capture stands committed masked with the seven others, and none is rewritten (data/b766_defects.txt (r)).",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and appended to the post-seal events bank at step [21] for the next corrigendum, not a letter (the ferry`s Component 5, data/b766_ferry.txt :125; (R374)(5) [K10], standing).",
)
NEWLY = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD', 'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD',
         'G-PUSHOUT-COMMITTED', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-RUNNER-GATE', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS',
         'G-WRITELIST-MIRROR-STATE')
# ### b765's, as b765 wrote them: the arms failing at the pre-run on real state, declared by name before the lock, each with its reason; set from the probes. b765 (the
# ### Edit tool, 22:2xZ): b764's four, each line read against b766's own state from b766's probes (standing-a1 :20, :23 at 20:33:44Z;
# ### standing-a2 :38, :80, :127 at 20:59:57Z, its 25 failing b765's 25 by name), G-DELETE-FREE now on tools/project_set.py :340 (defect
# ### (t)); every cite read at its line before it was written (checks.tpl :1779, :1783, :1814; b649_checks.py :452-:454; no_sorry_main.py
# ### :4-:11; rule_arms.py :389, :617; deletefree.py :1-:12; project_set.py :308, :332, :340, :348). NEWLY the twelve of
# ### `tools/standing/prelock.py print b766` at 22:11:44Z, G-DELETE-FREE not among them, failing at b765's pre-run.
DECLARED_B765 = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN', 'G-DELETE-FREE')
DECLARED_LINES_B765 = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried; the arm at tools/standing/fold/checks.tpl :1783) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b765 declared it on its face (data/b765_registration_2026-11-20.txt).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :127), as at b765`s pre-run. b766 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b766_*cut* in the tree; the cuts of (7) are written beside the archive, outside the relay), so it adds to neither count, and the searches read fail NONE (:38). (R376) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11; the arm at tools/standing/fold/checks.tpl :1779); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean, b726`s certificates carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b765. b766`s three files of (5), on main since (4)`s HELD, add no token: the count stands at b765`s 15, and each build that compiled them read sorry warnings 0 (data/b766_events.txt (48), (54), (58)). The axioms print of run 44918855502, the build from source of v0.44`s tree at main 0ba9cd61, reads 593 axiom lines each within the standard three and sorryAx nowhere, the 18 certificate names of print_targets.txt among its targets (read at main by count), so no fallback branch was taken (data/b766_events.txt (58)); the counter counts the text.",
    "### `G-DELETE-FREE` reads the act`s own tools, their code with prose stripped, for a delete call of any kind, a temporary folder`s cleanup set apart where the call`s first argument is a name the same file bound from tempfile or a parameter every call of which passes one (tools/standing/fold/checks.tpl :1814, tools/standing/deletefree.py :1-:12); it fails on one line of tools/project_set.py, (7)`s builder: in its control, `os.remove(os.path.join(tmp, gone))` at :340, the planted removal of one copy from the folder the control made by tempfile.mkdtemp at :332, which the case A COPY REMOVED reads as MISSING, a joined path the reader does not set apart; the tool`s two folder cleanups by shutil.rmtree at :308 and :348 set apart (the probe of standing-a2 :80; data/b766_defects.txt (t)). It removes a file the same control copied under the system`s temporary folder, and nothing of the record is deleted. The tool ran and banked in that form (data/b766_project_set_control.txt) and is not edited, as b765 kept its own for b765 (i); that the reader does not follow a joined temporary path is a fault of tools/standing/, which (R376)(11) moves under (8) and (4) alone, carried to the next reading of the close.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and appended to the post-seal events bank at step [21] for the next corrigendum, not a letter (the ferry`s Component 5, data/b766_ferry.txt :132; (R375)(5) [K10], standing).",
)
NEWLY_B765 = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD', 'G-LOCKGATE-EIGHT',
         'G-NOTHING-RAN-AHEAD', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS',
         'G-WRITELIST-MIRROR-STATE')
# ### b764's, as b765 kept them (the carry's substitution shifting their names)
DECLARED_B764 = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN', 'G-DELETE-FREE')
DECLARED_LINES_B764 = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried; the arm at tools/standing/fold/checks.tpl :1783) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b765 carried it (data/b765_events.txt (85)).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :127), as at b765`s pre-run. b766 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b766_*cut.txt in the tree), so it adds to neither count, and the searches read fail NONE (:38). (R376) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11; the arm at tools/standing/fold/checks.tpl :1779); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20, :22): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean, b726`s certificates (commit c9add92) carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b765. The axioms print of run 44670834879, the run that built v0.43`s tree at main 819e4a83, reads each C2Walk.cert_m<n> with no axiom (its artifact`s axioms.txt :136-:153, as b765 read it, data/b765_events.txt (85)), so no fallback branch was taken and sorryAx stands nowhere in its print; the counter counts the text. b766 writes no Lean byte: its one kernel write is the workflow`s file on push-b766-runner, and the kernel`s clone stood at main when standing-a1 ran (data/b766_events.txt (57)); (R376) removes no kernel branch ((4)), and the M<n> files stand as landed.",
    "### `G-DELETE-FREE` reads the act`s own tools, their code with prose stripped, for a delete call of any kind, a temporary folder`s cleanup set apart where the call`s first argument is a name the same file bound from tempfile or a parameter every call of which passes one (tools/standing/fold/checks.tpl :1814, tools/standing/deletefree.py :1-:12); it fails on five lines of tools/b766_repair_controls.py, the controls` cleanups in their finally blocks at :874-:876, :957-:959, :1047-:1049, :1137-:1139 and :1237-:1239, each `shutil.rmtree(t_, ignore_errors=True)` in a loop over the block`s own tempfile.mkdtemp folders, the path read absolute and its name by the control`s own prefix before the call, a loop variable the reader does not follow (the probe of standing-a2 :80; data/b766_defects.txt (i)). Each removes a folder its own block made under the system`s temporary folder, and nothing of the record is deleted. The tool ran and banked in that form (data/b766_repair_controls.txt) and is not edited, as b762 kept its own for b762 (j); that the reader does not follow a loop variable is a fault of tools/standing/, which (R376)(12) moves under (5) and (7) alone, carried to the next act of the record`s upkeep.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and appended to the post-seal events bank at step [21] for the next corrigendum, not a letter (the ferry`s Component 5, data/b766_ferry.txt :155; (R376)(5) [K10]).",
)
NEWLY_B764 = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DELETE-FREE', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD',
         'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS',
         'G-WRITELIST-MIRROR-STATE')
# ### b765's comment on its three, as b765 wrote it (the carry shifting its names): DECLARED and DECLARED_LINES set by hand from b765's probes
# ### (standing-a1 :20, :22, :23 at 01:16:37Z; standing-a2 :38, :80, :127 at 01:21:42Z, and again at 02:30:37Z with the same 25 failing by
# ### name): b763's three, each line read against b765's own state, and G-DELETE-FREE for b765's defect (i). NEWLY the thirteen of
# ### `tools/standing/prelock.py print b765` at 02:38:52Z. b766's set from b766's probes and its pre-lock comparison when they are run.


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
    """the paragraphs of b765's face standing between its blocks: gap[k], the lines after block k up to the next; the lines found by each block's own last
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
    """### b766, from the bank (no count kept by hand): the hook's refusals before this lock counted by kind, against b765's bank, and the kinds
    above b765's count, each one event by [U3] (data/b754_rules.txt (12)). Returns (n, kinds, sentence)."""
    own, prev = _refusal_rows('b766'), _refusal_rows('b765')
    ko, kp = _kinds(own), _kinds(prev)
    kinds = ', '.join('%s %d' % (k, ko[k]) for k in sorted(ko)) or 'NONE'
    pk = ', '.join('%s %d' % (k, kp[k]) for k in sorted(kp)) or 'none'
    if not own:
        return '0', 'NONE', ('The hook refused nothing before this lock (data/b766_hook_refusals.txt absent), so by [U3] no kind stands above '
                             'b765`s count (data/b765_hook_refusals.txt: %s).' % pk)
    rows = '; '.join('%s :%d %s' % (kind, n, t[11:]) for n, t, kind in own)
    above = ', '.join('%s %d against %d' % (k, ko[k], kp.get(k, 0)) for k in sorted(ko) if ko[k] > kp.get(k, 0))
    s = ('The hook refused %d call%s before this lock, each before it ran (data/b766_hook_refusals.txt: %s), counted by kind %s against b765`s '
         'bank`s %s; by [U3] each kind above b765`s count is one event of data/b766_events.txt and takes no letter: %s.'
         % (len(own), '' if len(own) == 1 else 's', rows, kinds, pk, above or 'none above it'))
    return str(len(own)), kinds, s


def summaries():
    """### b766 (the Edit tool, before any run, data/b766_events.txt (101)), from the events bank: the act's summaries of the session, the rows
    of any actor whose head names a SUMMARY or SUMMARIES -- b766 entered each in the host's rows, (4) to (99), and the reader takes any
    actor's as b765's did. A row's head is read across its lines, from its tag to the first full stop after which most letters of the next
    thirty characters are small (the body's opening, "A summary of the session ..." among them); each row counted for each
    summary its head names (two for "TWO SUMMARIES", three for "THREE SUMMARIES"; otherwise one, and one more for each " AND A " in the clause
    naming it), and b765's findings after its lock (b766 events (20) to (23)) left out by their section, from its head "b765'S FOUR FINDINGS
    AFTER ITS LOCK" to the next, "THE NAVIGATOR'S CLAIMS, FROM (R376)(1)" (b766 events :135 and :155). The count read against the chain
    read's boundaries after the delivery's line by hand before the face is composed (24 to :283114 at the summary of 18:19:30Z). Returns the
    phrase "<n words> summaries within it (events (a), ..., (z))"."""
    t = open(os.path.join(D, 'b766_events.txt'), encoding='utf-8').read()
    a_, b_ = "\nb765'S FOUR FINDINGS AFTER ITS LOCK", "\nTHE NAVIGATOR'S CLAIMS, FROM (R376)(1)"
    if t.count(a_) != 1 or t.count(b_) != 1 or t.index(a_) > t.index(b_):
        raise SystemExit("REFUSED: the events bank's section of b765's findings after its lock not found once, before the navigator's claims")
    t = t[:t.index(a_)] + t[t.index(b_):]
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
        if not cl_ or 'BEFORE THE DELIVERY' in head_:
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
    if DECLARED is None or DECLARED_LINES is None:   # ### b766: the declared arms set from b766's probes before any composition
        print('REFUSED: DECLARED and DECLARED_LINES not set from b766`s probes')
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
    t = t.replace('@@NEWLY@@', 'PENDING (tools/standing/prelock.py print b766 not yet run)' if NEWLY is None else (' '.join('`%s`' % a for a in NEWLY) if NEWLY else 'NONE'))
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
    stale = sorted(set(re.findall(r'b766_registration_(?!%s)[\d-]+' % K.DATE, t)))
    if stale:
        print('REFUSED: a stale face date', stale)
        return 2
    ferry = open(FERRY, encoding='utf-8', newline='').read()
    rows = AM.rows_of('b766')
    row = AM.w_row(ferry, rows, t)
    if t.count(W_ANCHOR) != 1:
        print('REFUSED: the (W) anchor')
        return 2
    if row:
        t = t.replace(W_ANCHOR, row + '\n' + W_ANCHOR)
    regen = AM.regenerate('b766', ferry, t, rows)
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
