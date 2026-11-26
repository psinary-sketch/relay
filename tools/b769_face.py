# -*- coding: utf-8 -*-
"""b769_face.py -- THE ACT'S FACE, COMPOSED: b768's sealed face (lines above its lock block) read unedited, the standing paragraphs between b768's blocks carried by the
act shift, the act's own blocks from tools/b769_face_blocks.txt, the field of pre-face commits read from the logs ((R338)(2)(iv)(a)), and the (W) row of the standing composer: the files the ruling's clauses order
written, read from the ruling, added to the list where it does not cover them (b731's (R341)(2)(i)). The carried paragraphs are found by b768's own blocks' first and last lines in b768's face, no line number kept.
Writes data/b769_registration_<DATE>.txt alone, and only before the lock: it refuses when the face already carries a lock block. Carried from tools/b768_face.py by tools/b769_carry.py (data/b769_carry_face.txt),
its OLD, MAP, PAT, the LOGS comment, FIXES and the summaries reader set by hand before any run (data/b769_events.txt (86)), and the arms declared before the lock (DECLARED, DECLARED_LINES, NEWLY) set by hand from the probes
(data/b769_probe_<part>.txt) and the pre-lock comparison, empty and PENDING until then.
### (R379)(13): the (W) row and N5's write clause regenerated from the ruling by tools/standing/amend.py over the act's amendment rows (data/b769_amendments.json, absent at b769: no amendment row, as at b768, the carry's "three amendment rows" an older act's words), the regeneration printed into the face's (W) section before the lock.
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
import b769_worklist as K   # noqa: E402
OLD, NEW = os.path.join(D, 'b768_registration_2026-11-24.txt'), os.path.join(D, 'b769_registration_%s.txt' % K.DATE)   # ### b769: b768's face by its own date, the one data/b768_registration_*.txt in the tree (the Glob tool, 2026-11-26T01:17Z; the carry had shifted b767's -11-23)
OLD_BLOCKS, BLOCKS = os.path.join(T, 'b768_face_blocks.txt'), os.path.join(T, 'b769_face_blocks.txt')
FERRY = os.path.join(D, 'b769_ferry.txt')
ORDER = ('HEAD', 'ZERO', 'A', 'B_TOOLS', 'B_LAST', 'C', 'D', 'NEEDLES', 'G2', 'G2_RUN', 'W', 'Z')
KEEP = ('keiper-b725', 'c2-b725', 'detect-b729', 'zq-b730', 'scratch-b724', 'rebuild-b721', 'b732_phase2_frontdoors')
# ### b769 (the Edit tool, before any run, data/b769_events.txt (86)): the shift of b768's face by one act (b768 -> b769, b767 -> b768,
# ### R378 -> R379), one pass of one alternation so that no name is shifted twice; tools/standing/ moved by (R379)(8) alone, v1.38.28 to
# ### v1.38.30 ([K29] and [K30], data/b769_repairs.txt), which b769's own blocks say; a name two acts back, b766's among them, stands
# ### unshifted (the carry had left b768's pair b766 -> b767 carried to b766 -> b768, and b768's face's date as b767's -11-23)
MAP = {'b768_registration_2026-11-24': 'b769_registration_%s' % K.DATE, 'b768': 'b769', 'b767': 'b768', '(R378)': '(R379)', 'R378': 'R379'}
PAT = re.compile('|'.join(re.escape(x) for x in KEEP + ('b768_registration_2026-11-24', '(R378)', 'R378', 'b768', 'b767')))
# ### b769: b768's closing commits as (R379)'s SCOPE READ gives them, relay 55166251 and PLACE-papers e52e2bae (data/b769_ferry.txt :3), the
# ### worklist's PRE_RELAY and PRE_PP: the pre-face commits after them (the carry had left b767's 048085dd and a8be5811 in this comment)
LOGS = ((ROOT, K.PRE_RELAY), (K.PP, K.PRE_PP))
W_ANCHOR = '### No Zeta23 or vendored byte;'
# ### b769 (the Edit tool, before any run, data/b769_events.txt (86)): the sentences of b768's face carried between its blocks read
# ### against b769 (b768's face :45-:46, :93-:94, :142-:145, :155-:161, :165-:166, :177-:178, :189-:209, :213-:243, :248-:254, :261-:287 and
# ### :351-:352, the gaps by scratch gaps769.py, 2026-11-26T01:17:58Z) and set where (R379) or the standing toolset at v1.38.30 reads
# ### otherwise. (G1)'s order at :201, "COMPONENTS 0-4 AND COMPONENT 5`S BANKS", stands (data/b769_ferry.txt :174-:179); the freeze's
# ### "(R378)(13)`s (W) list" (:243) and the arms' "(R378)(13)`s (W) row" (:278), shifted to (R379)(13)'s, stand, b769's (W) list being
# ### (R379)(13)'s (data/b769_ferry.txt :48). Set: (G1)'s pre-run in ten parts (:206), G-ACTROOT-VERIFY's half (:264) and the arms'
# ### paragraph on the suite's parts (:281) from [K27] to [K29], b769's kind NO PAPER AND NO LEAN holding standing-b2a to standing-b2d as
# ### at LEAN AND NO PAPER, each writing its banks with no arm (tools/standing/cadence.py HOLD_KINDS, v1.38.29, data/b769_events.txt (47));
# ### G-DELETES-ONE-BRANCH's allowance at v1.38.28 (:251) to v1.38.30 (tools/standing/VERSION :1); and the tools run unedited (:160),
# ### b768's tools/b757_ghcalls.py and tools/b758_presend.py, of which b769 imports the first alone (tools/acts/b769.py :4151), to the
# ### earlier acts' tools that b769's tools and module import beside b722's (the Grep tool over tools/b769_*.py and tools/acts/b769.py,
# ### 2026-11-26T01:18Z: b756_constellation, b757_ghcalls, b761_registry, b766_registry_cells and b766_lean_join). The run list's count at
# ### :241-:243 and :277 is read against the pre-lock print when it is run.
FIXES = (
    ('`fold.py checks --prerun` IN ITS TEN PARTS (R202)(3), standing-b2a TO standing-b2d NOT RUN AT THIS ACT`S KIND BY [K27], EACH WRITING ',
     '`fold.py checks --prerun` IN ITS TEN PARTS (R202)(3), standing-b2a TO standing-b2d NOT RUN AT THIS ACT`S KIND BY [K29], EACH WRITING '),
    ('`tools/b725_*.py`, `tools/b757_ghcalls.py` and `tools/b758_presend.py` run unedited',
     '`tools/b725_*.py`, `tools/b756_constellation.py`, `tools/b757_ghcalls.py`, `tools/b761_registry.py`, `tools/b766_registry_cells.py` and '
     '`tools/b766_lean_join.py` run unedited'),
    ('tools/standing/allow.py at v1.38.28', 'tools/standing/allow.py at v1.38.30'),
    ('-- at this act`s kind by [K27] standing-b2a to standing-b2d, the first half`s four quarters, not run,',
     '-- at this act`s kind by [K29] standing-b2a to standing-b2d, the first half`s four quarters, not run,'),
    ('no arm in standing-a1, standing-b2a to standing-b2d not run at this act`s kind by [K27], each writing its banks with no arm,',
     'no arm in standing-a1, standing-b2a to standing-b2d not run at this act`s kind by [K29], each writing its banks with no arm,'),
)
# ### b768's, as b768 set them (the carry shifting their names)
FIXES_B768 = (
    ('`fold.py checks --prerun` IN ITS TEN PARTS (R202)(3), each its own',
     '`fold.py checks --prerun` IN ITS TEN PARTS (R202)(3), standing-b2a TO standing-b2d NOT RUN AT THIS ACT`S KIND BY [K27], EACH WRITING '
     'ITS BANKS WITH NO ARM, each its own'),
    ('`tools/b725_*.py` and `tools/b768_*.py` run unedited', '`tools/b725_*.py`, `tools/b757_ghcalls.py` and `tools/b758_presend.py` run unedited'),
    ('tools/standing/allow.py at v1.38.25', 'tools/standing/allow.py at v1.38.28'),
    ('recomputes the chain at commit in five parts by act with the', 'recomputes the chain at commit by act with the'),
    ('-- standing-b2a to standing-b2d the first half`s four quarters,',
     '-- at this act`s kind by [K27] standing-b2a to standing-b2d, the first half`s four quarters, not run,'),
    ('### each banked, and standing-b3 the second half through b769, the arm counted there once over every banked verdict',
     '### and standing-b3 its own half, b659 to b769, with the boundary`s two lines of relay data/act_roots.txt read as before, the arm '
     'counted there once over every banked verdict'),
    ('no arm in standing-a1 or in standing-b2a to standing-b2d,',
     'no arm in standing-a1, standing-b2a to standing-b2d not run at this act`s kind by [K27], each writing its banks with no arm,'),
)
# ### b768's three, as b768 set them (the carry shifting their names)
FIXES_B767 = (
    ('(outside (R379)(12)`s (W) list)', '(outside (R379)(13)`s (W) list)'),
    ('read (R379)(12)`s (W) row and the rules banks', 'read (R379)(13)`s (W) row and the rules banks'),
    ('tools/standing/allow.py at v1.38.24', 'tools/standing/allow.py at v1.38.25'),
)
# ### b768's three, as b768 set them (the carry shifting their names), and b765's as b768 kept them
FIXES_B766 = (
    ('(outside (R379)(13)`s (W) list)', '(outside (R379)(12)`s (W) list)'),
    ('read (R379)(13)`s (W) row and the rules banks', 'read (R379)(12)`s (W) row and the rules banks'),
    ('tools/standing/allow.py at v1.38.21', 'tools/standing/allow.py at v1.38.24'),
)
FIXES_B765 = (
    ('(outside (R378)(14)`s (W) list)', '(outside (R378)(13)`s (W) list)'),
    ('read (R378)(14)`s (W) row and the rules banks', 'read (R378)(13)`s (W) row and the rules banks'),
    ('tools/standing/allow.py at v1.38.18', 'tools/standing/allow.py at v1.38.21'),
)
# ### b769 (the Edit tool, before any run, data/b769_events.txt (86)): the arms failing at the pre-run on real state, declared by name before
# ### the lock, each with its reason, set by hand from b769's probes and `tools/standing/prelock.py print b769` when they are run; None until
# ### then, and main() refuses while DECLARED or DECLARED_LINES is None (the carry had left b768's under these names, kept below as
# ### DECLARED_B768, DECLARED_LINES_B768 and NEWLY_B768, read by nothing).
# ### b769 (the Edit tool, 2026-11-26T05:09Z, after every part probed at 0cbd368c, the four held parts called and `tools/standing/prelock.py
# ### print b769` at 05:06:23Z: arms read 116, failing 34, banks absent NONE, NEWLY FAILING 12; data/b769_events.txt (106), (107)): b768's
# ### three stand, each ground read again at its line at 05:08Z before it was written, every file counted first (the probes of standing-a1
# ### :20, :22, :23 and standing-a2 :38, :66, :68, :127; tools/b649_checks.py :452-:454; tools/standing/fold/checks.tpl :1784 and :1788;
# ### tools/rule_arms.py :389, :617; tools/no_sorry_main.py :4-:11; data/b757_defects.txt (q) at :30; no data/b769_*cut* tracked or
# ### untracked by `git ls-files`, 05:08:24Z; the sorry hits by kernel and folder in the probe of standing-a1 :22, 15 of 15 in
# ### SIDEExplicitFormula/C2Field/). G-DELETES-ONE-BRANCH is not declared: (R379)(3)'s sentence is worded for tools/standing/allow.py :50
# ### and its reader reads the five step-zero deletes inside the ruling (data/b769_events.txt (15)); at the act part's probe it reads the
# ### command bank `record commands` writes, absent until that route runs before the lock (data/b769_events.txt (100); the probe of the act
# ### part :29), as at b768's second probe (data/b768_events.txt (151)). NEWLY the twelve of the pre-lock print: b768's eleven
# ### (data/b768_prelock.txt :3-:13) and G-DELETES-ONE-BRANCH, which b768's pre-run lists do not hold failing, as the comparison reads
# ### them (tools/standing/prelock.py :72-:88). The [K10] line cites b769's Component 5 at the ferry's :179 (clause (9), :40, names it),
# ### where the carry left b768's line number, :100. G-NO-SORRY-MAIN's clone cites row (97), the clone at main with no switch sent, and
# ### the probe of standing-a1 :20, its pair read equal, where the carry left b768's rows.
DECLARED = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN')
DECLARED_LINES = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried; the arm at tools/standing/fold/checks.tpl :1788) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction (the probe of standing-a2 :68); tools/axiom_claim.py outside (W), no bank rewritten, carried as b768 declared it on its face.",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :127), as at b768`s pre-run. b769 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b769_*cut* tracked or untracked, read 2026-11-26T05:08:24Z), so it adds to neither count, and the searches read failing NONE (:38). (R379) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11; the arm at tools/standing/fold/checks.tpl :1784); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20, :22; standing-a2 :66), each a file of SIDE-explicit-formula`s SIDEExplicitFormula/C2Field/ folder (the probe of standing-a1 :22 by kernel and folder: 15 of 15), the fifteen b768 declared on its face. b769 touches no kernel and moves no kernel ref ((R379)(9), (12), N5): SIDE-explicit-formula`s main stands at ffefddc6 as b768 left it (the probe of standing-a1 :19), so the C2Field files stand on main as before and the count stands at b768`s 15; the kernel`s clone stood at main with no switch sent (data/b769_events.txt (97)), its pair read equal when standing-a1 ran (the probe of standing-a1 :20); the counter counts the text.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and appended to the post-seal events bank at step [21] for the next corrigendum, not a letter (the ferry`s Component 5, data/b769_ferry.txt :179; (R374)(5) [K10], standing).",
)
NEWLY = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD', 'G-LOCKGATE-EIGHT',
         'G-NOTHING-RAN-AHEAD', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS',
         'G-WRITELIST-MIRROR-STATE')
# ### b768's, as b768 wrote them (the carry shifting their names): b768 (the Edit tool, 2026-11-25T08:0xZ, after the six probes run, act,
# ### standing-a1, a2, c, b1 and b3, and `tools/standing/prelock.py
# ### print b768` at 08:00:56Z: arms read 116, failing 34, NEWLY FAILING 11, the four held parts' banks absent by [K27]): three of b767's
# ### four stand, each ground read again at its line before it was written (the probes of standing-a1 :20, :22, :23 and standing-a2 :38,
# ### :66, :68, :127; tools/b649_checks.py :452-:454; tools/standing/fold/checks.tpl :1784 and :1788, five below b768's cites since [K27]'s
# ### edit; tools/rule_arms.py :389, :617; tools/no_sorry_main.py :4-:11; data/b757_defects.txt (q) at :30; no data/b769_*cut* by name,
# ### 08:02:58Z; the sorry hits by kernel and folder in the probe of standing-a1 :22, 15 of 15 in SIDEExplicitFormula/C2Field/).
# ### G-DELETES-ONE-BRANCH is not declared: (R379)(3)'s sentence is worded for tools/standing/allow.py :50 and its reader reads the five
# ### step-zero deletes inside the ruling (data/b769_events.txt (12)); at the act part's probe its nine conjuncts read true and the command
# ### bank absent, `record commands` not yet run (data/b769_events.txt (147), (151); the probe of the act part :29). NEWLY the eleven of
# ### the pre-lock print, equal to b768's eleven by name.
DECLARED_B768 = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN')
DECLARED_LINES_B768 = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried; the arm at tools/standing/fold/checks.tpl :1788) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction (the probe of standing-a2 :68); tools/axiom_claim.py outside (W), no bank rewritten, carried as b768 declared it on its face.",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :127), as at b768`s pre-run. b769 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b769_*cut* in the tree, read 2026-11-25T08:02:58Z), so it adds to neither count, and the searches read failing NONE (:38). (R379) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11; the arm at tools/standing/fold/checks.tpl :1784); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20, :22; standing-a2 :66), each a file of SIDE-explicit-formula`s SIDEExplicitFormula/C2Field/ folder (the probe of standing-a1 :22 by kernel and folder: 15 of 15), the fifteen b768 declared on its face. b769 moved SIDE-explicit-formula`s main under (R379)(4) alone, 89fd5b54 to ffefddc6 by the gated push after the closing build from source, 89fd5b54 an ancestor of ffefddc6 (data/b769_events.txt (124)), its changes fifty Lean files added under SIDEExplicitFormula/Window/ and none modified (data/b769_events.txt (132)), so the C2Field files stand on main as before and the count stands at b768`s 15; the act`s fifty Window files carry none (the axioms print of run 45521560784, the build from source at ffefddc6 with the restore off, reads 2,038 axiom lines with sorryAx in none, data/b769_events.txt (122)), and the kernel`s clone stood at main when standing-a1 ran (data/b769_events.txt (146)); the counter counts the text.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and appended to the post-seal events bank at step [21] for the next corrigendum, not a letter (the ferry`s Component 5, data/b769_ferry.txt :100; (R374)(5) [K10], standing).",
)
NEWLY_B768 = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD', 'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD',
         'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS', 'G-WRITELIST-MIRROR-STATE')
# ### b768's, as b768 wrote them (the carry shifting their names): b769 (the Edit tool, 2026-11-24T00:5xZ, after the ten probes and
# ### `tools/standing/prelock.py print b769` at 00:55:49Z): the arms failing
# ### at the pre-run on real state, declared by name before the lock, each with its reason. b768's six read against b769's probes: G-DELETE-FREE,
# ### G-RUNNER-GATE and G-PUSHOUT-COMMITTED pass at standing-a2 (data/b769_probe_standing-a2.txt :135), so three of b768's stand, each ground
# ### read again and written new, and G-DELETES-ONE-BRANCH beside them, failing beyond the face at b765 and b768 and declared here, its
# ### conjunct read alone (scratch dob769.py, 00:57:36Z). Every cite read at its line before it was written (checks.tpl :821-:834, :1706,
# ### :1779, :1783; b649_checks.py :452-:454; no_sorry_main.py :4-:11; rule_arms.py :389, :617; allow.py :169-:179; tools/acts/b769.py
# ### :472-:478). NEWLY the eleven of the pre-lock print, b768's thirteen less G-PUSHOUT-COMMITTED and G-RUNNER-GATE.
DECLARED_B767 = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN', 'G-DELETES-ONE-BRANCH')
DECLARED_LINES_B767 = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried; the arm at tools/standing/fold/checks.tpl :1783) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction (the probe of standing-a2 :68); tools/axiom_claim.py outside (W), no bank rewritten, carried as b768 declared it on its face (data/b768_registration_2026-11-22.txt).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :127), as at b768`s pre-run. b769 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b769_*cut* in the tree, read 2026-11-24T00:58:20Z), so it adds to neither count, and the searches read failing NONE (:38). (R379) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11; the arm at tools/standing/fold/checks.tpl :1779); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20, :22; standing-a2 :66): each a file of SIDE-explicit-formula`s SIDEExplicitFormula/C2Field/ folder (read by kernel and folder, 00:58:32Z: 15 of 15), b726`s certificates carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b768. b769 moved SIDE-explicit-formula`s main under (R379)(4) alone, 0ba9cd61 to 89fd5b54 by the gated push after the closing build from source, 0ba9cd61 an ancestor of 89fd5b54 (data/b769_events.txt (118), (119)), so the C2Field files stand on main as before and the count stands at b768`s 15; the act`s sixteen Window files carry none (each compiled with sorryAx in none, data/b769_events.txt (109)), and the kernel`s clone stood at main when standing-a1 ran (data/b769_events.txt (138)). The axioms print of run 45236921224, the build from source at 89fd5b54 with the restore off, reads 884 axiom lines with sorryAx in none (data/b769_events.txt (118)); the counter counts the text.",
    "### `G-DELETES-ONE-BRANCH` wants each branch delete of the command capture one branch, no glob, no variable, nothing chained after, each allowed by the ruling`s own delete clauses read through tools/standing/allow.py (tools/standing/fold/checks.tpl :821-:834, the arm at :1706; the act module`s override at tools/acts/b769.py :472-:478, KERNEL_DELETES empty and no rdelete route run); the allowance reader takes a branch`s name only from a clause saying \"delete\" or \"deleted\" (tools/standing/allow.py :169-:179, data/b769_misses.txt (1)), and (R379) words the step-zero removal \"THE REMOVALS\" ((3), data/b769_ferry.txt :15) and in N5 \"the branches removed are\" (:122), so the five step-zero deletes of the relay`s and PLACE-papers` push-b768-* branches (data/b769_events.txt (11)) read OUTSIDE, the allowance naming none (scratch dob769.py, 2026-11-24T00:57:36Z: ok False, five OUTSIDE; the empty set ok True; the same ferry with one clause naming the five \"deleted\" read ok True, AS WANTED). It fails at the act part (the probe of the act part :29), as beyond the face at b765 and b768, its cause read at step zero (data/b769_events.txt (12)); (R379)(3) orders no repair, so the reader is not changed and the deletes stand as made, each by the one-call tool`s route, none forced; no kernel branch removed.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and appended to the post-seal events bank at step [21] for the next corrigendum, not a letter (the ferry`s Component 5, data/b769_ferry.txt :120; (R374)(5) [K10], standing).",
)
NEWLY_B767 = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD', 'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD',
         'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS', 'G-WRITELIST-MIRROR-STATE')
# ### b768's, as b768 wrote them (the carry shifting their names): b768 (the Edit tool, 23:1xZ, after the probes and
# ### `tools/standing/prelock.py print b768` at 23:01:45Z, b768 events (118)): b765's four, each ground read again against b768's own state
# ### and written new, and two beyond them, G-RUNNER-GATE (b768 defect (h)) and G-PUSHOUT-COMMITTED (b768 defect (r)); G-DELETE-FREE on
# ### tools/project_set.py :542 (b768 defect (s)). NEWLY_B766 the thirteen of b768's pre-lock print.
DECLARED_B766 = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN', 'G-DELETE-FREE', 'G-RUNNER-GATE', 'G-PUSHOUT-COMMITTED')
DECLARED_LINES_B766 = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried; the arm at tools/standing/fold/checks.tpl :1783) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b768 declared it on its face (data/b768_registration_2026-11-21.txt).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :127), as at b768`s pre-run. b769 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b769_*cut* in the tree), so it adds to neither count, and the searches read failing NONE (:38). (R379) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11; the arm at tools/standing/fold/checks.tpl :1779); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean, b726`s certificates carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b768. b769 moves no main: SIDE-explicit-formula`s main stands at 0ba9cd61 by the author`s word (data/b769_author_words_preseal.txt :32), the act`s Lean on push-b769-proof alone, which the arm does not read, and the kernel`s clone stood at main when standing-a1 ran (data/b769_events.txt (115)); the count stands at b768`s 15. The axioms print of run 44918855502, the build from source at main 0ba9cd61, reads 593 axiom lines each within the standard three and sorryAx nowhere (data/b768_events.txt (58)), so no fallback branch was taken; the counter counts the text.",
    "### `G-DELETE-FREE` reads the act`s own tools, their code with prose stripped, and of a shared tool the ruling orders edited the lines this act added (tools/standing/fold/checks.tpl :239-:246, :1814), for a delete call of any kind, a temporary folder`s cleanup set apart where the call`s first argument is a name the same file bound from tempfile or a parameter every call of which passes one (tools/standing/deletefree.py :1-:12); it fails on one line, in tools/project_set.py`s write route as [K24] edited it (relay 751b9e7a): `os.remove(os.path.join(CLONE, x))` at :542, the removal from the Project set`s clone of each name its index holds that the close`s export does not, before the set is written (the probe of standing-a2 :80; data/b769_defects.txt (s)). The route runs at the close`s step [23a], in the Project`s clone on the act`s branch, so that the repository equals the export file for file as (R379)(7) [K24] orders; nothing of the relay, PLACE-papers or a kernel is removed by it, and what it removes is kept in its record as `removed`. The tool ran its control in that form (data/b769_repair_controls.txt) and is not edited after it; b768`s line in the control, now :378, is b768`s and not read at b769.",
    "### `G-RUNNER-GATE` wants one command in the capture for each dispatch row, the route`s commands those of `gh workflow run` or of tools/b769_controls.py`s dispatch route not dry (tools/acts/b769.py :1048-:1049, :1054; the predicate at tools/standing/fold/checks.tpl :1231-:1242, the arm at tools/acts/b769.py :1451): the dispatch rows 16 and EF_RUNS 16, every row above the hold, the restore on 14 and off for the closing build and its repeat alone; the route`s commands in the capture 17, the one beyond a row the command of 11:19:08Z whose dispatch route the price row`s guard refused at 11:20:41Z, nothing sent (data/b769_events.txt (59), (116); data/b769_defects.txt (h)). Read on the composed sources the predicate is False as composed and True on a copy without that one command (scratch gate766b.py, 21:34:53Z). The capture is the act`s and is not edited; no dispatch went out beyond the sixteen rows.",
    "### `G-PUSHOUT-COMMITTED` wants the worklist`s STEPZERO commit to carry data/b768_relay_push-b768-closing_push_out.txt alone and to stand an ancestor of HEAD (tools/standing/fold/checks.tpl :1674, the sources at :602), b768`s step zero having committed b764`s closing push-out so; b769`s step zero committed c323bf50, data/b769_address_scan_commits.txt alone (tools/b769_worklist.py :389), because b768`s closing push-out carried the account and (R379)(3) and (7) [K23] put b768`s eight captures, masked, in Component 1, committed together at d09d93ab (data/b769_events.txt (39), (116)). No commit can give the arm its object: the capture stands committed masked with the seven others, and none is rewritten (data/b769_defects.txt (r)).",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and appended to the post-seal events bank at step [21] for the next corrigendum, not a letter (the ferry`s Component 5, data/b769_ferry.txt :125; (R374)(5) [K10], standing).",
)
NEWLY_B766 = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD', 'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD',
         'G-PUSHOUT-COMMITTED', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-RUNNER-GATE', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS',
         'G-WRITELIST-MIRROR-STATE')
# ### b768's, as b768 wrote them: the arms failing at the pre-run on real state, declared by name before the lock, each with its reason; set from the probes. b768 (the
# ### Edit tool, 22:2xZ): b764's four, each line read against b769's own state from b769's probes (standing-a1 :20, :23 at 20:33:44Z;
# ### standing-a2 :38, :80, :127 at 20:59:57Z, its 25 failing b768's 25 by name), G-DELETE-FREE now on tools/project_set.py :340 (defect
# ### (t)); every cite read at its line before it was written (checks.tpl :1779, :1783, :1814; b649_checks.py :452-:454; no_sorry_main.py
# ### :4-:11; rule_arms.py :389, :617; deletefree.py :1-:12; project_set.py :308, :332, :340, :348). NEWLY the twelve of
# ### `tools/standing/prelock.py print b769` at 22:11:44Z, G-DELETE-FREE not among them, failing at b768's pre-run.
DECLARED_B765 = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN', 'G-DELETE-FREE')
DECLARED_LINES_B765 = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried; the arm at tools/standing/fold/checks.tpl :1783) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b768 declared it on its face (data/b768_registration_2026-11-20.txt).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :127), as at b768`s pre-run. b769 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b769_*cut* in the tree; the cuts of (7) are written beside the archive, outside the relay), so it adds to neither count, and the searches read fail NONE (:38). (R379) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11; the arm at tools/standing/fold/checks.tpl :1779); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean, b726`s certificates carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b768. b769`s three files of (5), on main since (4)`s HELD, add no token: the count stands at b768`s 15, and each build that compiled them read sorry warnings 0 (data/b769_events.txt (48), (54), (58)). The axioms print of run 44918855502, the build from source of v0.44`s tree at main 0ba9cd61, reads 593 axiom lines each within the standard three and sorryAx nowhere, the 18 certificate names of print_targets.txt among its targets (read at main by count), so no fallback branch was taken (data/b769_events.txt (58)); the counter counts the text.",
    "### `G-DELETE-FREE` reads the act`s own tools, their code with prose stripped, for a delete call of any kind, a temporary folder`s cleanup set apart where the call`s first argument is a name the same file bound from tempfile or a parameter every call of which passes one (tools/standing/fold/checks.tpl :1814, tools/standing/deletefree.py :1-:12); it fails on one line of tools/project_set.py, (7)`s builder: in its control, `os.remove(os.path.join(tmp, gone))` at :340, the planted removal of one copy from the folder the control made by tempfile.mkdtemp at :332, which the case A COPY REMOVED reads as MISSING, a joined path the reader does not set apart; the tool`s two folder cleanups by shutil.rmtree at :308 and :348 set apart (the probe of standing-a2 :80; data/b769_defects.txt (t)). It removes a file the same control copied under the system`s temporary folder, and nothing of the record is deleted. The tool ran and banked in that form (data/b769_project_set_control.txt) and is not edited, as b768 kept its own for b768 (i); that the reader does not follow a joined temporary path is a fault of tools/standing/, which (R379)(11) moves under (8) and (4) alone, carried to the next reading of the close.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and appended to the post-seal events bank at step [21] for the next corrigendum, not a letter (the ferry`s Component 5, data/b769_ferry.txt :132; (R378)(5) [K10], standing).",
)
NEWLY_B765 = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD', 'G-LOCKGATE-EIGHT',
         'G-NOTHING-RAN-AHEAD', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS',
         'G-WRITELIST-MIRROR-STATE')
# ### b764's, as b768 kept them (the carry's substitution shifting their names)
DECLARED_B764 = ('G-AXIOM-CLAIM', 'G-RULE-RECUT-QUOTE', 'G-NO-SORRY-MAIN', 'G-DELETE-FREE')
DECLARED_LINES_B764 = (
    "### `G-AXIOM-CLAIM` reads 0 claims (tools/axiom_claim.py at standing-a1: CONTRADICTED 0, UNVERIFIABLE 0, VERIFIED 0, UNBOUND 0, MENTION 0; the probe of standing-a1 :23); its predicate (tools/b649_checks.py :452-:454, carried; the arm at tools/standing/fold/checks.tpl :1783) asks at least one row as well as none CONTRADICTED, so it fails on the empty reading, not on a contradiction; tools/axiom_claim.py outside (W), no bank rewritten, carried as b768 carried it (data/b768_events.txt (85)).",
    "### `G-RULE-RECUT-QUOTE` counts every data/b<act>_*cut.txt as a cut bank of a paper`s re-cut (tools/rule_arms.py :389) and wants a quotation-search bank for each (:617); b757 banked (R367)(8)(i)`s check as data/b757_cut.txt, a name the pattern takes, re-cut no paper and banked no search (data/b757_defects.txt (q)), so the arm reads \"acts with more cut banks than searches [757]\" (the probe of standing-a2 :38, :127), as at b768`s pre-run. b769 re-cuts no paper and banks neither a cut bank the pattern takes nor a quotation search (no data/b769_*cut.txt in the tree), so it adds to neither count, and the searches read fail NONE (:38). (R379) names neither the pattern nor b757`s bank, so neither is changed and no pushed bank is rewritten.",
    "### `G-NO-SORRY-MAIN` wants each kernel`s remote main, its clone`s HEAD and its local main equal and no token `sorry` outside comments and strings in any file a lean_lib of its main reaches, any hit failing the arm (tools/no_sorry_main.py :4-:11; the arm at tools/standing/fold/checks.tpl :1779); it reads 23 kernels, pairs unequal 0, sorry in code 15 (the probe of standing-a1 :20, :22): each SIDE-explicit-formula/SIDEExplicitFormula/C2Field/M<n>.lean, b726`s certificates (commit c9add92) carried onto main with c2-b725`s tree, each a `first` whose second branch is `sorry` after `decide +kernel`, as at b768. The axioms print of run 44670834879, the run that built v0.43`s tree at main 819e4a83, reads each C2Walk.cert_m<n> with no axiom (its artifact`s axioms.txt :136-:153, as b768 read it, data/b768_events.txt (85)), so no fallback branch was taken and sorryAx stands nowhere in its print; the counter counts the text. b769 writes no Lean byte: its one kernel write is the workflow`s file on push-b769-runner, and the kernel`s clone stood at main when standing-a1 ran (data/b769_events.txt (57)); (R379) removes no kernel branch ((4)), and the M<n> files stand as landed.",
    "### `G-DELETE-FREE` reads the act`s own tools, their code with prose stripped, for a delete call of any kind, a temporary folder`s cleanup set apart where the call`s first argument is a name the same file bound from tempfile or a parameter every call of which passes one (tools/standing/fold/checks.tpl :1814, tools/standing/deletefree.py :1-:12); it fails on five lines of tools/b769_repair_controls.py, the controls` cleanups in their finally blocks at :874-:876, :957-:959, :1047-:1049, :1137-:1139 and :1237-:1239, each `shutil.rmtree(t_, ignore_errors=True)` in a loop over the block`s own tempfile.mkdtemp folders, the path read absolute and its name by the control`s own prefix before the call, a loop variable the reader does not follow (the probe of standing-a2 :80; data/b769_defects.txt (i)). Each removes a folder its own block made under the system`s temporary folder, and nothing of the record is deleted. The tool ran and banked in that form (data/b769_repair_controls.txt) and is not edited, as b762 kept its own for b762 (j); that the reader does not follow a loop variable is a fault of tools/standing/, which (R379)(12) moves under (5) and (7) alone, carried to the next act of the record`s upkeep.",
    "### An arm failing at step [7] on real state beyond these is printed with its time in the closing message and appended to the post-seal events bank at step [21] for the next corrigendum, not a letter (the ferry`s Component 5, data/b769_ferry.txt :155; (R379)(5) [K10]).",
)
NEWLY_B764 = ('G-ARMS-DECLARED-EQ-RUN', 'G-CLOSING-DRY-STEP', 'G-DELETE-FREE', 'G-DELETES-ONE-BRANCH', 'G-DRY-STEP-CLEAN', 'G-GUARD-HELD',
         'G-LOCKGATE-EIGHT', 'G-NOTHING-RAN-AHEAD', 'G-ROOTDRY-READY', 'G-RULE-SCORES-BEFORE-SEAL', 'G-SEAL-VERIFIES', 'G-SEALED-AFTER-COMPONENTS',
         'G-WRITELIST-MIRROR-STATE')
# ### b768's comment on its three, as b768 wrote it (the carry shifting its names): DECLARED and DECLARED_LINES set by hand from b768's probes
# ### (standing-a1 :20, :22, :23 at 01:16:37Z; standing-a2 :38, :80, :127 at 01:21:42Z, and again at 02:30:37Z with the same 25 failing by
# ### name): b763's three, each line read against b768's own state, and G-DELETE-FREE for b768's defect (i). NEWLY the thirteen of
# ### `tools/standing/prelock.py print b768` at 02:38:52Z. b769's set from b769's probes and its pre-lock comparison when they are run.


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
    """the paragraphs of b768's face standing between its blocks: gap[k], the lines after block k up to the next; the lines found by each block's own last
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
    """### b769, from the bank (no count kept by hand): the hook's refusals before this lock counted by kind, against b768's bank, and the kinds
    above b768's count, each one event by [U3] (data/b754_rules.txt (12)). Returns (n, kinds, sentence)."""
    own, prev = _refusal_rows('b769'), _refusal_rows('b768')
    ko, kp = _kinds(own), _kinds(prev)
    kinds = ', '.join('%s %d' % (k, ko[k]) for k in sorted(ko)) or 'NONE'
    pk = ', '.join('%s %d' % (k, kp[k]) for k in sorted(kp)) or 'none'
    if not own:
        return '0', 'NONE', ('The hook refused nothing before this lock (data/b769_hook_refusals.txt absent), so by [U3] no kind stands above '
                             'b768`s count (data/b768_hook_refusals.txt: %s).' % pk)
    rows = '; '.join('%s :%d %s' % (kind, n, t[11:]) for n, t, kind in own)
    above = ', '.join('%s %d against %d' % (k, ko[k], kp.get(k, 0)) for k in sorted(ko) if ko[k] > kp.get(k, 0))
    s = ('The hook refused %d call%s before this lock, each before it ran (data/b769_hook_refusals.txt: %s), counted by kind %s against b768`s '
         'bank`s %s; by [U3] each kind above b768`s count is one event of data/b769_events.txt and takes no letter: %s.'
         % (len(own), '' if len(own) == 1 else 's', rows, kinds, pk, above or 'none above it'))
    return str(len(own)), kinds, s


def summaries():
    """### b769 (the Edit tool, before any run, data/b769_events.txt (118)), from the events bank: the act's summaries of the session, the
    rows of any actor whose head names a SUMMARY or SUMMARIES -- b769 entered each in the host's rows, (2) to (117) and after, and the reader
    takes any actor's as b768's did. A row's head is read across its lines, from its tag to the first full stop after which most letters of
    the next thirty characters are small (the body's opening, "A summary of the session ..." among them); each row counted for each
    summary its head names (two for "TWO SUMMARIES", three for "THREE SUMMARIES"; otherwise one, and one more for each " AND A " in the clause
    naming it), and b768's thirteen findings after its lock (b769 events (24) to (36), under the head COMPONENT 1 with no section of their
    own, rows (28), (29), (35) and (36) naming b768's summaries) left out by their numbers, row (24) read as "The first of the thirteen" and
    row (36) as "The thirteenth of the thirteen" before they are left out. b769, the Edit tool before any run (data/b769_events.txt (86)):
    a head naming "<WORD> SUMMARIES" counted by its number word (row (74), SEVEN SUMMARIES, where b768's reader read two and three alone);
    and the one summary b769 entered in a row's body and not in a host row of its own, the summary at transcript line 381349 (18:51:16Z) in
    row (45)'s "After the ritual of the summary at transcript line 381349", read by that phrase in the row (BODY_SUMMARIES). The count read
    against the chain read's boundaries after the delivery's line by hand before the face is composed. Returns the phrase "<n words>
    summaries within it (events (a), ..., (z))"."""
    t = open(os.path.join(D, 'b769_events.txt'), encoding='utf-8').read()
    def _row(n_, src_):
        m_ = re.search(r"(?ms)^    \(%d\) .*?(?=^    \(\d+\) |^\S|\Z)" % n_, src_)
        return m_.group(0) if m_ else ''
    r24_, r36_ = ' '.join(_row(24, t).split()), ' '.join(_row(36, t).split())
    if 'The first of the thirteen' not in r24_ or 'The thirteenth of the thirteen' not in r36_:
        raise SystemExit("REFUSED: the events bank's rows (24) and (36) not read as the first and the last of b768's thirteen findings after its lock")
    FOUND_AFTER_B768 = set(str(n_) for n_ in range(24, 37))
    BODY_SUMMARIES = {'45': 'After the ritual of the summary at transcript line 381349'}
    for n_, ph_ in BODY_SUMMARIES.items():
        if ph_ not in ' '.join(_row(int(n_), t).split()):
            raise SystemExit("REFUSED: the events bank's row (%s) does not carry the summary its body was read to name" % n_)
    hits = []
    for m in re.finditer(r"(?ms)^    \((\d+)\) THE [A-Z']+ \[[^\]]*\]: (.*?)(?=^    \(\d+\) |^\S|\Z)", t):
        row_ = ' '.join(x_.strip() for x_ in m.group(2).split('\n'))
        head_ = row_
        for p_ in re.finditer(r'\. ', row_):
            nx_ = [c_ for c_ in row_[p_.end():p_.end() + 30] if c_.isalpha()]
            if nx_ and sum(1 for c_ in nx_ if c_.islower()) * 2 > len(nx_):
                head_ = row_[:p_.start() + 1]
                break
        if m.group(1) in BODY_SUMMARIES:
            hits.append((m.group(1), 1))
            continue
        cl_ = [c_ for c_ in head_.split(';') if re.search(r'\bSUMMAR(?:Y|IES)\b', c_)]
        if not cl_ or 'BEFORE THE DELIVERY' in head_ or m.group(1) in FOUND_AFTER_B768:
            continue
        c_ = cl_[0]
        w_ = re.search(r'\b([A-Z][A-Z-]*) SUMMARIES\b', c_)
        hits.append((m.group(1), WORDS.index(w_.group(1).lower()) if w_ and w_.group(1).lower() in WORDS[2:] else 1 + c_.split('SUMMAR')[0].count(' AND A ')))
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
    if DECLARED is None or DECLARED_LINES is None:   # ### b769: the declared arms set from b769's probes before any composition
        print('REFUSED: DECLARED and DECLARED_LINES not set from b769`s probes')
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
    t = t.replace('@@NEWLY@@', 'PENDING (tools/standing/prelock.py print b769 not yet run)' if NEWLY is None else (' '.join('`%s`' % a for a in NEWLY) if NEWLY else 'NONE'))
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
    stale = sorted(set(re.findall(r'b769_registration_(?!%s)[\d-]+' % K.DATE, t)))
    if stale:
        print('REFUSED: a stale face date', stale)
        return 2
    ferry = open(FERRY, encoding='utf-8', newline='').read()
    rows = AM.rows_of('b769')
    row = AM.w_row(ferry, rows, t)
    if t.count(W_ANCHOR) != 1:
        print('REFUSED: the (W) anchor')
        return 2
    if row:
        t = t.replace(W_ANCHOR, row + '\n' + W_ANCHOR)
    regen = AM.regenerate('b769', ferry, t, rows)
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
