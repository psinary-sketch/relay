# -*- coding: utf-8 -*-
"""standing/commit.py -- v1.21.0, (R351)(2)(i), b740 events (1), (2), (4): THE SUBJECT AND THE ROW THAT TRAVEL WITH THEIR COMMIT. One call makes a
gate, lock or seal commit: it composes the subject from the bank (tools/standing/subjects.py), makes the commit and writes its step row, in that
order, with no shell between the subject and the commit (git is run by argument list, so no shell's escape character touches the subject).
Everything that could refuse the row is read before the commit, so a commit and its row never part:
  - the record the subject names must exist: the seal's data/<act>_seal_hashes.json, the lock's data/<act>_lockgate.json;
  - a lock row already in the step bank refuses a second `lock` and a `gate` (the commit after the lock takes `seal`, standing.repeat.one_lock);
  - the composed subject must pass subjects.check(); something must be staged (the add is its own message, one git write per message).
The commit's subject is read back from git and compared with the composed one; the row is written by the record tool's step route.
After a seal commit the post-seal exclude list is printed (tools/standing/hook.py excludes), read before any read ((R351)(2)(iv)).
v1.22.0, (R352)(2)(v): a refusal prints its class, REPEAT of the earlier act's row that carries its head words, or NEW (repeat_of).
v1.23.0, (R353)(3)(ii), b742 events (1)-(2): no subject text is taken for lock, gate and seal; words given refuse the commit. The gate subject
is composed from the index and the banks (subjects.gate_words); the seal and lock subjects are the composer's whole (subjects.check).

v1.24.0, (R354)(2)(ii)-(iii), b743 events (4), (7)-(9): THE REPAIR PHASE. `repair`, between the lock and the seal, for the act module alone, under
three conditions printed in the row: an author's lift banked in the events with its time (a line naming THE LIFT and an HH:MM:SSZ); the hook
restored, the settings file's sha256 now equal to the value the events bank names before the lift; the diff against HEAD confined to
tools/acts/<act>.py and to the lines the events name (":<n>" in the events rows). The head "<act> repair:" (the author's at b743, events (9)),
the seat's words after it naming the edits; the row written as phase `repair`. N4 reads such a commit as a post-lock edit and scores REFUTED.

v1.26.0, (R356)(3)(i), (iii), b745 events (1), N4: the lock phase runs reg_seal.py --lock on the face its gate record names, adds the face and
reads the staged blob back (lock_face, lock_check): the lock block stands in the lock commit or nothing is committed. The act phases (ACT_PHASES:
step zero, component N, pre-root, record, closing) take the seat's words; the subject "<act> <phase>: <words>", the row in the same call.

v1.28.0, (R358)(3)(ii), (iii), (iv), (v), (vii), (viii), b747 defects (b), (d)-(f), (k), (n), (r), (v), (z), (a'):
  (iv) EVERY GIT WRITE THROUGH THE ONE-CALL TOOL: `add <paths>`, `restore <path>` and `delete <branch>` beside the commit phases; every write takes
       the act's write mark (an exclusive file under the relay's .git), and a call made while another write of the act holds it is refused, the
       open one printed (b747 (k): an add and a commit in one message).
  (ii) THE SCAN OVER THE STAGED SET BEFORE EVERY COMMIT: the act's tools/<act>_address_scan.py run before the commit, its four counts printed;
       a count above 0, a control not as wanted, or no foot refuses the commit.
  (v)  THE CARRY BEFORE THE ACT'S FIRST COMMIT: `step zero` refuses while the act's module, worklist or scan tool is not carried.
  (iii) NO STANDING CHANGE AT THE GATE: the gate refuses a staged tools/standing/ path (the repair lands with its version before the gate).
  (vii) THE SATISFIABILITY READ BEFORE THE GATE COMMIT: the gate refuses unless data/audit_<act>_reg_satisfiable.txt reads JOINTLY SATISFIABLE
       stamped against the face; a contradictory clause is printed by name.
  (viii) A STANDING REPAIR WITH THE RECORD'S DRY: a commit staging tools/standing/ files refuses unless data/<act>_standing_dry.txt is staged
       beside them, CLEAN or PENDING, naming each staged standing file at its staged sha256 (tools/standing/standingdry.py).

v1.28.1, (R358)(3)(iv), b748 defect (k): THE CLOSE'S WRITES THROUGH THE SAME TOOL: `root` among the act phases (the root banks commit);
  `branch <name>`, the act's push branch alone (push-<act>-preroot|record|closing) at HEAD, under the write mark; a relay act commit whose
  staged set is the step bank alone (with the scan's banks) is a step-rows commit: its words must be the rows' own composition
  (subjects.step_rows_words) and it writes no row of its own, so the step bank is clean before the push.

v1.29.0, (R359)(3)(i)-(iii), b748 events (2), defects (b), (d), (k), (r):
  (i)   ONE CALL OF THE TOOL PER MESSAGE: the hook records every shell call with its message's request stamp (hook.py record_call, the calls
        ledger in the temporary directory); the tool reads that ledger before it writes and refuses where another git write was allowed in the
        same message, the bare `git add` counted as a write (message_refusal; b748's root message: an add and the root commit in one message).
  (ii)  THE SCAN BEFORE A COMMIT WRITES ITS OWN BANK: run_scan runs the act's scan without --bank and appends its run to
        data/<act>_address_scan_commits.txt (standing.act.scan_commits_name); the act's scan bank is written once at its step and the
        post-lock bank after the lock, so a commit leaves the root-named banks as committed and the root's dry run reads READY with no restore.
  (iii) NO COMMIT WITHOUT THE SCAN: run() takes no scanner=False; the hook refuses a git write by plain git (PLAINGIT), so every add, commit,
        restore, branch and delete runs through this tool and its scan (b747's closing push capture be4a5a0d: a plain add, then a commit
        with no scan).

v1.35.4, (R367)(3), THE ROUTE FOR KERNEL WRITES, BEFORE ANY BUILD: b745 committed in a kernel by plain git from a scratch clone (relay
  data/b745_commands.txt :375-:376); since v1.29.0 the hook refuses a git write by plain git and this tool took two repositories, so no kernel
  was written after b745. The tool now takes the kernels of KERNELS, each opened by an act's ruling for that act alone (KERNEL_ACTS; b757:
  SIDE-explicit-formula and SIDE-dirichlet-mod-24); any other repository name, a third kernel among them, is refused before anything is read.
  In a kernel: `add` and `restore` as in the relay; `branch <push-<act>-word> <commit>` makes the branch at the named commit and checks it out;
  `switch <main | push-<act>-word>` checks out the one or the other; `merge <commit>` merges one named commit into the checked-out
  push-<act>-* branch without fast-forward and without committing -- a conflict in a file the ruling names (NAMED_CONFLICTS) is left for the
  seat to resolve and add, a conflict in any other file aborts the merge, nothing concluded; `delete <push-<act>-word>` deletes a branch not
  checked out (forced for the act's control branches and for a branch whose tip the remote's main holds). The act phases' commit in a kernel
  stands on the checked-out push-<act>-* branch alone, with the relay's commit identity, no file left conflicted, and the act's scan over the
  staged set naming the kernel among the repositories it read; a commit while a merge stands open concludes that merge. No gate, lock, seal
  or repair in a kernel. Pushes stay with tools/push_gated.sh as it stands.

v1.36.0, (R368)(6)(i), THE FAST-FORWARD OF A KERNEL'S LOCAL MAIN: tools/push_gated.sh moves a kernel's main at the remote from the pushed branch
  and leaves the clone's own main where it stood (SIDE-dirichlet-mod-24's at 597b0869 beside the remote's e5ebdd15 since b757). `ff main` reads
  the remote's main by one ls-remote of origin, wants that commit in the clone and the local main its ancestor, and moves the local main to it:
  `merge --ff-only` where main is checked out on a clean tree, `update-ref` from the old value where it is not; the local main read back equal.
  A local main that is not an ancestor (a divergent main), a remote main the clone lacks, or a read that fails is refused, nothing written; a
  local main already equal writes nothing. Opened act by act by FF_ACTS, apart from KERNEL_ACTS: b758 opens SIDE-dirichlet-mod-24 to this
  route alone and to no other write.

v1.36.1, (R368)(6)(ii), THE PUSH OF A NAMED COMMIT TO A NAMED NON-MAIN BRANCH OF A KERNEL, NOT FORCED: `pushto <commit> <branch>` reads the
  branch's remote tip by one ls-remote of origin; an absent branch is made, a tip the clone holds and that is an ancestor of the commit is
  moved forward, a tip equal to the commit writes nothing; a tip that is not an ancestor, or one the clone lacks (its ancestry unread), is
  refused, nothing pushed. main, master, HEAD, a refs/ name or a name outside the branch form is refused. The push is `git push origin
  <sha>:refs/heads/<branch>` with no force, read back by ls-remote equal to the commit. Opened act by act by PUSHTO_ACTS: no act at b758.

v1.36.3, (R369)(4)(i), THE ROUTE THAT REMOVES A BRANCH AT A KERNEL'S REMOTE: b758 found none (its worklist's KERNEL_DELETES_HALT: the kernel
  `delete` is `git branch -d/-D`, local alone; push_gated.sh deletes nothing; `pushto` pushes a commit to a name). `rdelete <branch>` reads
  the remote's main and the branch by one ls-remote of origin each, wants both commits in the clone and the branch's tip an ancestor of the
  remote's main, and removes refs/heads/<branch> at the remote by `git push origin :refs/heads/<branch>`, not forced; the branch read back
  absent by ls-remote. Refused, nothing removed: main (and any name outside the branch form); a name on the act's kept list (its worklist's
  KEPT_BRANCHES rows for that kernel, the previous closing's carried list (f)); a name the act's ruling does not name (RDELETE_ACTS, act by
  act and kernel by kernel); a tip that is no ancestor of the remote's main, a commit the clone lacks, a branch absent at the remote, or a
  read that fails. The clone's own branches are not touched. b759 opens the five branches of (R369)(3).

v1.36.7, (R369)(5) AND (11): THE KERNEL ROUTE OPENED FOR b759 AT SIDE-explicit-formula ALONE. KERNEL_ACTS and FF_ACTS named b757 and b758,
  so every kernel write of (5) (the branch push-b759-weil at main, its two commits, the local main after the gated push) was refused before it
  was read. b759 opens SIDE-explicit-formula in both; SIDE-dirichlet-mod-24 stays closed (its one write, (3)'s removal, by `rdelete`); no
  file is named for a conflicted merge, (5) merging nothing.

v1.37.1, (R370)(5)(iv) AND (4): THE REMOVAL ROUTE'S TABLE OPENS SIDE-explicit-formula FOR b760, for the one kernel branch of (4),
  push-b759-weil, "read there to be an ancestor of main before and read absent after". RDELETE_ACTS named b759 alone, so the removal was
  refused for b760 before anything was read. b760 opens that one name at that one kernel; SIDE-dirichlet-mod-24 stays closed; KERNEL_ACTS,
  FF_ACTS and PUSHTO_ACTS do not name b760, no other kernel write being ordered; the kept list (b760's worklist's KEPT_BRANCHES) carries
  b759's list (f) less push-b759-weil, whose entry lapses with the removal.

v1.37.2, (R373)(5): THE KERNEL ROUTE OPENED FOR b763 AT SIDE-explicit-formula ALONE, "as b757 made it and b759 used it". KERNEL_ACTS and
  FF_ACTS named b757, b758 and b759, so every kernel write of b763's builds (the branches push-b763-* at a named commit, their commits, the
  local main after the gated push) was refused before it was read; (5): "Where that route refuses this act's branch names, the seat makes the
  one change under tools/standing/ that admits them". b763 opens SIDE-explicit-formula in both tables; SIDE-dirichlet-mod-24 stays closed
  ("No kernel beyond SIDE-explicit-formula is written"); no file is named for a conflicted merge; PUSHTO_ACTS and RDELETE_ACTS do not name
  b763, (4) removing no kernel branch and this act's own push-b763-* branches staying for the next act's step zero.

v1.38.18, (R374)(7) AND (12): THE KERNEL ROUTE OPENED FOR b764 AT SIDE-explicit-formula ALONE, for the trial of the runner on a restored
  build: "THE CHANGE, on a branch push-b764-runner of SIDE-explicit-formula made at main, by the route of (R373)(5)"; "ON SUCCESS, and at no
  other time: main moved to the branch tip by the gated push's default mode and read back". KERNEL_ACTS and FF_ACTS named b757, b758, b759
  and b763, so the branch, its commit of the workflow's file and the local main after the gated push were each refused for b764 before
  anything was read. b764 opens SIDE-explicit-formula in both tables; SIDE-dirichlet-mod-24 stays closed ("no kernel touched beyond
  SIDE-explicit-formula, and there the workflow's file alone"); no file is named for a conflicted merge; PUSHTO_ACTS and RDELETE_ACTS do
  not name b764, (4) removing no kernel branch and push-b764-runner staying for the next act's step zero.

v1.38.22, (R376)(7) [K22]: THE KERNEL ROUTE FOR b766, AND ONE BRANCH NOT MERGED REMOVED BY ITS NAME. KERNEL_ACTS and FF_ACTS named b757 to
  b765, so (4)'s branch push-b766-proof, its commits and the local main after the gated push were refused for b766 before anything was read;
  RDELETE_ACTS named b759 and b760, and the local delete took the act's own push-<act>-* names alone, `git branch -d` refusing a branch not
  merged (b765's worklist KERNEL_DELETES_REFUSED: push-b765-planted, 7d86a245, "not fully merged"). b766 opens SIDE-explicit-formula in
  KERNEL_ACTS and FF_ACTS; RDELETE_ACTS names push-b765-planted for b766 at that kernel alone; FORCED_DELETES names the same one name, "for
  which one name the local delete forces a branch that is not merged": kernel_delete_args() admits that name to the local delete with
  `git branch -D`, and rdelete_plan() takes its tip though it is no ancestor of the remote's main (the seat's read: the ruling orders the
  branch "removed at the kernel's remote and in its clone", and the removal route refused a tip not merged, so the one name's forcing reads
  for both; the remote's ref is removed by `git push origin :refs/heads/<branch>`, which forces no push). Every other name stands as
  before: a second name, the act's own branch not merged, main and SIDE-dirichlet-mod-24 refused or taken as v1.38.21 took them.

v1.38.25, (R377)(8) [K25]: THE KERNEL ROUTE FOR b767. KERNEL_ACTS and FF_ACTS named b757 to b766, so (4)'s branch push-b767-proof, cut
  from push-b766-proof at 3c67b8b5, its commits and the local main after the gated push were refused for b767 before anything was read.
  b767 opens SIDE-explicit-formula in KERNEL_ACTS and FF_ACTS ("tools/standing/commit.py admits b767 to KERNEL_ACTS and FF_ACTS at
  SIDE-explicit-formula"); RDELETE_ACTS and FORCED_DELETES name nothing for b767 ("RDELETE_ACTS names nothing for b767"; (12) "no kernel
  branch removed", push-b766-proof kept at 3c67b8b5); SIDE-dirichlet-mod-24 stays closed ("no kernel touched beyond SIDE-explicit-formula");
  no file is named for a conflicted merge; PUSHTO_ACTS does not name b767.

v1.38.26, (R378)(8) [K26]: THE KERNEL ROUTE FOR b768. KERNEL_ACTS and FF_ACTS named b757 to b767, so (4)'s branch push-b768-proof, cut
  from push-b767-proof at 89fd5b54, its commits and the local main after the gated push were refused for b768 before anything was read.
  b768 opens SIDE-explicit-formula in KERNEL_ACTS and FF_ACTS ("tools/standing/commit.py admits b768 to KERNEL_ACTS and FF_ACTS at
  SIDE-explicit-formula"); RDELETE_ACTS and FORCED_DELETES name nothing for b768 ("RDELETE_ACTS names nothing for b768"; (12) "no kernel
  branch removed", push-b767-proof kept at 89fd5b54 and push-b766-proof at 3c67b8b5); SIDE-dirichlet-mod-24 stays closed ("no kernel
  touched beyond SIDE-explicit-formula"); no file is named for a conflicted merge; PUSHTO_ACTS does not name b768.

v1.38.31, (R380)(8) [K31]: THE KERNEL ROUTE FOR b770. KERNEL_ACTS and FF_ACTS named b757 to b768 (b769 wrote no Lean and opened no
  kernel), so (4)'s branch push-b770-proof, cut from push-b768-proof at ffefddc6, its commits and the local main after the gated push were
  refused for b770 before anything was read. b770 opens SIDE-explicit-formula in KERNEL_ACTS and FF_ACTS ("tools/standing/commit.py admits
  b770 to KERNEL_ACTS and FF_ACTS at SIDE-explicit-formula"); RDELETE_ACTS and FORCED_DELETES name nothing for b770 ("RDELETE_ACTS names
  nothing for b770"; (12) "no kernel branch removed", push-b768-proof kept at ffefddc6, push-b767-proof at 89fd5b54 and push-b766-proof at
  3c67b8b5); SIDE-dirichlet-mod-24 stays closed ("no kernel touched beyond SIDE-explicit-formula"); no file is named for a conflicted
  merge; PUSHTO_ACTS does not name b770. Its control (tools/b770_repair_controls.py K31) plants a second kernel's name and reads it refused.

  python -X utf8 -u tools/standing/commit.py <relay|pp> <gate|lock|seal>
  python -X utf8 -u tools/standing/commit.py <relay|pp> branch push-<act>-<preroot|record|closing>
  python -X utf8 -u tools/standing/commit.py relay repair <the words naming the edits>
  python -X utf8 -u tools/standing/commit.py <relay|pp> "component 1" <the words>
  python -X utf8 -u tools/standing/commit.py <relay|pp> add <path> [<path> ...]
  python -X utf8 -u tools/standing/commit.py <relay|pp> restore <path>
  python -X utf8 -u tools/standing/commit.py <relay|pp> delete <branch>
  python -X utf8 -u tools/standing/commit.py <kernel> add <path> [<path> ...]
  python -X utf8 -u tools/standing/commit.py <kernel> branch push-<act>-<word> <commit>
  python -X utf8 -u tools/standing/commit.py <kernel> switch <main | push-<act>-<word>>
  python -X utf8 -u tools/standing/commit.py <kernel> merge <commit>
  python -X utf8 -u tools/standing/commit.py <kernel> "component 2" <the words>
  python -X utf8 -u tools/standing/commit.py <kernel> delete push-<act>-<word>
  python -X utf8 -u tools/standing/commit.py <kernel> ff main
  python -X utf8 -u tools/standing/commit.py <kernel> pushto <commit> <branch>
  python -X utf8 -u tools/standing/commit.py <kernel> rdelete <branch>
"""
import json
import os
import subprocess
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
REPOS = {'relay': RELAY, 'pp': 'D:/MY-DOwnloads/PLACE-papers'}
PHASES = ('gate', 'lock', 'seal', 'repair')
RECORD = {'seal': '%s_seal_hashes.json', 'lock': '%s_lockgate.json'}
SETTINGS = 'D:/.claude/settings.json'   # ### the seat's project settings carrying the hook (b743 events (4): its sha256 read before and after each lift)
# ### v1.35.4, (R367)(3): the kernels the tool writes; each opened by an act's ruling for that act alone; the one file each ruling names for a
# ### conflicted merge. fold/record.tpl's STEP_REPOS carries the same kernels (the step route's rows), the controls reading the two equal.
KERNELS = {'SIDE-explicit-formula': 'D:/SIDE-explicit-formula', 'SIDE-dirichlet-mod-24': 'D:/SIDE-dirichlet-mod-24'}
KERNEL_ACTS = {'b757': ('SIDE-explicit-formula', 'SIDE-dirichlet-mod-24'),   # ### (R367)(4): the holds lifted "in this act alone"
               'b758': ('SIDE-explicit-formula',),   # ### v1.35.9, (R368)(5), (10): "lifted for SIDE-explicit-formula in this act alone"; SIDE-dirichlet-mod-24's local main by (6)(i)'s route alone
               'b759': ('SIDE-explicit-formula',),   # ### v1.36.7, (R369)(5), (11): "lifted for SIDE-explicit-formula in this act alone"; "no kernel touched beyond SIDE-explicit-formula's tree and the five branches of (3)"
               'b763': ('SIDE-explicit-formula',),   # ### v1.37.2, (R373)(5): "No kernel beyond SIDE-explicit-formula is written"
               'b764': ('SIDE-explicit-formula',),   # ### v1.38.18, (R374)(7): push-b764-runner made at main and its commit of the workflow's file; "there the workflow's file alone"
               'b765': ('SIDE-explicit-formula',),   # ### v1.38.21, (R375)(4), (5), (12) "no kernel touched beyond SIDE-explicit-formula": push-b765-centre cut from push-b764-runner, push-b765-planted from it, the files of (5), print_targets.txt and the workflow's file (the seat's read of (11), data/b765_misses.txt (2))
               'b766': ('SIDE-explicit-formula',),   # ### v1.38.22, (R376)(7) [K22], (4), (11) "no kernel touched beyond SIDE-explicit-formula": push-b766-proof cut from main at 0ba9cd61, the files of (4) in the kernel's source folder and print_targets.txt; the local delete of push-b765-planted by FORCED_DELETES
               'b767': ('SIDE-explicit-formula',),   # ### v1.38.25, (R377)(8) [K25], (4), (12) "no kernel touched beyond SIDE-explicit-formula": push-b767-proof cut from push-b766-proof at 3c67b8b5, the files of (4) in the kernel's source folder, print_targets.txt and, under (5), the workflow's file
               'b768': ('SIDE-explicit-formula',),   # ### v1.38.26, (R378)(8) [K26], (4), (12) "no kernel touched beyond SIDE-explicit-formula": push-b768-proof cut from push-b767-proof at 89fd5b54, the files of (4) in the kernel's source folder and print_targets.txt
               'b770': ('SIDE-explicit-formula',)}   # ### v1.38.31, (R380)(8) [K31], (4), (12) "no kernel touched beyond SIDE-explicit-formula": push-b770-proof cut from push-b768-proof at ffefddc6, the files of (4) in the kernel's source folder and print_targets.txt
NAMED_CONFLICTS = {'b757': {'SIDE-explicit-formula': ('print_targets.txt',)},   # ### (R367)(4): "the one file this ruling names for (3)'s conflicted merge"
                   'b758': {'SIDE-explicit-formula': ('print_targets.txt',)}}   # ### v1.35.9, (R368)(5): "One file is named for a conflicted merge: print_targets.txt"
# ### v1.36.0, (R368)(6)(i): `ff main`, a kernel's local main fast-forwarded to its remote's main, opened act by act by its own table and
# ### read inside the route, not by KERNEL_ACTS -- (R368)(10): "no kernel touched beyond SIDE-explicit-formula's tree and the two local mains of (6)(i)"
FF_ACTS = {'b758': ('SIDE-dirichlet-mod-24', 'SIDE-explicit-formula'),
           'b759': ('SIDE-explicit-formula',),   # ### v1.36.7, (R369)(5): the local main following the remote's after the gated push moves it to v0.41
           'b763': ('SIDE-explicit-formula',),   # ### v1.37.2, (R373)(5): the local main following the remote's after each gated push that moves main (v0.42 and on)
           'b764': ('SIDE-explicit-formula',),   # ### v1.38.18, (R374)(7): the local main following the remote's after the gated push moves main on the trial's success alone
           'b765': ('SIDE-explicit-formula',),   # ### v1.38.21, (R375)(4): the local main following the remote's after the gated push moves main under the HELD outcome alone
           'b766': ('SIDE-explicit-formula',),   # ### v1.38.22, (R376)(7) [K22], (4): the local main following the remote's after the gated push moves main to the closing Lean commit on equal axioms files alone
           'b767': ('SIDE-explicit-formula',),   # ### v1.38.25, (R377)(8) [K25], (4): the local main following the remote's after the gated push moves main to the closing Lean commit on equal axioms files alone
           'b768': ('SIDE-explicit-formula',),   # ### v1.38.26, (R378)(8) [K26], (4): the local main following the remote's after the gated push moves main to the closing Lean commit on equal axioms files alone
           'b770': ('SIDE-explicit-formula',)}   # ### v1.38.31, (R380)(8) [K31], (4): the local main following the remote's after the gated push moves main to the closing Lean commit on equal axioms files alone
# ### v1.36.1, (R368)(6)(ii): `pushto <commit> <branch>`, a named commit pushed to a named non-main branch of a kernel, not forced, opened act by
# ### act by its own table -- "It has no use in this act once (5) lands, zq-b730 staying at 1e658870; it is built for the acts after": none opened
PUSHTO_ACTS = {}
# ### v1.36.3, (R369)(4)(i): `rdelete <branch>`, a branch removed at a kernel's remote, opened act by act and kernel by kernel by its own table
# ### naming the branches the act's ruling removes -- (R369)(3): "at the remote of SIDE-explicit-formula push-b757-join, push-b757-coeff,
# ### push-b758-land and push-b758-coeff, and at the remote of SIDE-dirichlet-mod-24 push-b757-mod24"
RDELETE_ACTS = {'b759': {'SIDE-explicit-formula': ('push-b757-join', 'push-b757-coeff', 'push-b758-land', 'push-b758-coeff'),
                         'SIDE-dirichlet-mod-24': ('push-b757-mod24',)},
                # ### v1.37.1, (R370)(5)(iv) and (4): "The branch push-b759-weil of SIDE-explicit-formula is deleted at its remote by the standing
                # ### removal route, read there to be an ancestor of main before and read absent after"; no other kernel and no other name
                'b760': {'SIDE-explicit-formula': ('push-b759-weil',)},
                # ### v1.38.22, (R376)(7) [K22]: "RDELETE_ACTS names push-b765-planted for b766"; its tip 7d86a245 not merged, taken by FORCED_DELETES
                'b766': {'SIDE-explicit-formula': ('push-b765-planted',)}}
# ### v1.38.22, (R376)(7) [K22]: "for which one name the local delete forces a branch that is not merged" -- the one name, act by act and kernel
# ### by kernel, that the local delete takes with -D though it is not the act's own push branch, and that the removal at the remote takes though
# ### its tip is no ancestor of the remote's main (the seat's read, the ruling ordering it "removed at the kernel's remote and in its clone");
# ### a name here must stand in RDELETE_ACTS for the same act and kernel, or neither route takes it
FORCED_DELETES = {'b766': {'SIDE-explicit-formula': ('push-b765-planted',)}}
# ### v1.38.25, (R377)(8) [K25]: "RDELETE_ACTS names nothing for b767" -- neither table is given b767, so the removal at a remote and the forced
# ### local delete refuse every name for b767, push-b766-proof among them ((12) "no kernel branch removed")
# ### v1.38.26, (R378)(8) [K26]: "RDELETE_ACTS names nothing for b768" -- neither table is given b768, so the removal at a remote and the forced
# ### local delete refuse every name for b768, push-b767-proof and push-b766-proof among them ((12) "no kernel branch removed")
# ### v1.38.31, (R380)(8) [K31]: "RDELETE_ACTS names nothing for b770" -- neither table is given b770, so the removal at a remote and the forced
# ### local delete refuse every name for b770, push-b768-proof, push-b767-proof and push-b766-proof among them ((12) "no kernel branch removed")
NOREPLY = '@users.noreply.github.com'
REPOS.update(KERNELS)
if S not in sys.path:
    sys.path.insert(0, S)
if T not in sys.path:
    sys.path.append(T)   # ### v1.26.0: reg_seal.py for lock_check

import subjects as SJ   # noqa: E402


class Refused(Exception):
    pass


def _git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')


def reader(data):
    def read(name):
        p = os.path.join(data, name)
        if not os.path.exists(p):
            return None
        with open(p, encoding='utf-8') as f:
            return json.load(f) if name.endswith('.json') else f.read()
    read.data = data   # ### v1.28.0: the gate's satisfiability read finds the audit and the face beside the banks
    return read


def data_dir(read):
    return getattr(read, 'data', os.path.join(RELAY, 'data'))


def face_stamped(act, data):
    """the satisfiability audit stamped against the act's registration face as it stands (gate_hash.matches), False where either is absent."""
    import glob
    import gate_hash as G
    faces = sorted(glob.glob(os.path.join(data, '%s_registration_*.txt' % act)))
    audit = os.path.join(data, 'audit_%s_reg_satisfiable.txt' % act)
    if not faces or not os.path.isfile(audit):
        return False
    return G.matches(audit, faces[-1])[0] is True


def _hash_matches(banked, now):
    """a banked sha256 in full or in the events' short form "1E22BFFE...68FBB2" against the hash now (case ignored)."""
    b, n = banked.upper().replace('…', '...'), (now or '').upper()
    if '...' in b:
        a, z = b.split('...', 1)
        return bool(a) and bool(z) and n.startswith(a) and n.endswith(z)
    return bool(b) and n == b


def repair_check(act, words, rows, events, settings_now, names, old_lines):
    """v1.24.0, (R354)(2)(ii): the repair phase's three conditions, pure in its arguments -- the step rows, the events text, the settings file's
    sha256 now, the staged names and the HEAD-side line numbers the staged diff touches. Returns (subject, the condition lines) or raises Refused."""
    import re
    ev = (events or '').replace('\r', '')
    if not any(r.get('phase') == 'lock' for r in rows):
        raise Refused('NO LOCK ROW: the repair phase stands between the lock and the seal')
    if any(r.get('phase') == 'seal' for r in rows):
        raise Refused('A SEAL ROW STANDS: the repair phase stands before the seal')
    if not (words or '').strip():
        raise Refused('THE REPAIR NAMES NO EDIT: the words after "%s repair:" name the edits and the lift' % act)
    lines = ev.split('\n')
    lifts = [i for i, l in enumerate(lines) if re.search(r'\bTHE LIFT\b', l) and re.search(r'\b\d\d:\d\d:\d\dZ\b', l)]
    c1 = bool(lifts)
    pre = [m.group(1) for l in lines[:lifts[0]] for m in re.finditer(r'settings\.json sha256 ([0-9A-Fa-f]{6,}(?:(?:\.\.\.|…)[0-9A-Fa-f]{4,})?)', l)] if c1 else []
    c2 = bool(pre) and _hash_matches(pre[-1], settings_now)
    named = sorted(set(int(m.group(1)) for l in lines for m in re.finditer(r'(?<![\w/.]):(\d{2,5})\b', l)))
    mod = 'tools/acts/%s.py' % act
    c3 = list(names) == [mod] and bool(old_lines) and set(old_lines) <= set(named)
    conds = ['  (1) the author`s lift banked in the events with its time: %s' % (('%d LIFT row(s), the first: %s' % (len(lifts), lines[lifts[0]].strip()[:90])) if c1 else '### NONE'),
             '  (2) the hook restored, %s now %s against the value banked before the lift %s: %s' % (SETTINGS, (settings_now or 'UNREAD')[:16], (pre[-1] if pre else 'NONE'), 'EQUAL' if c2 else '### NOT EQUAL'),
             '  (3) the diff against HEAD: files %s ; lines %s ; the lines the events name %s: %s' % (list(names), sorted(old_lines), named[:12], 'CONFINED' if c3 else '### NOT CONFINED')]
    if not (c1 and c2 and c3):
        raise Refused('THE REPAIR`S CONDITIONS NOT MET: %s' % ' '.join(c.strip() for c in conds if '###' in c))
    return '%s repair: %s' % (act, words.strip()), conds


def lock_check(face_text, rec):
    """v1.26.0, (R356)(3)(i), b745 events (1), N4: THE LOCK BLOCK IN THE LOCK COMMIT. Pure in its arguments -- the face's text as it stands in
    the commit (the staged blob, or a commit's blob in the controls) and the lock gate's record. The face must carry reg_seal's lock block, and
    the digest of the bytes above it must equal the record's face_sha. Returns the condition lines or raises Refused."""
    import reg_seal as RS
    t = (face_text or '').replace('\r\n', '\n')
    body, banked = RS.split_body(t)
    has = RS.LOCKMARK in t and banked is not None
    dig = RS.digest(body)
    eq = has and dig == (rec or {}).get('face_sha') and banked == dig
    conds = ['  (1) the face %s carries the lock block in the commit: %s' % ((rec or {}).get('face'), 'YES' if has else '### NO'),
             '  (2) the digest of the bytes above it %s against the gate record`s face_sha %s: %s' % (dig[:16], str((rec or {}).get('face_sha'))[:16],
                                                                                                 'EQUAL' if eq else '### NOT EQUAL')]
    if not (has and eq):
        raise Refused('THE LOCK BLOCK IS NOT IN THE LOCK COMMIT: %s' % ' '.join(c.strip() for c in conds if '###' in c))
    return conds


def lock_face(repo, act, read, data, run_seal=True):
    """v1.26.0, (R356)(3)(i): inside the lock tool, between the gate and the lock commit -- reg_seal.py --lock on the face the gate record names,
    where the face carries no lock block yet, the face added to the index, and the staged blob read back through lock_check."""
    rec = read('%s_lockgate.json' % act) or {}
    face = rec.get('face')
    if not face:
        raise Refused('THE GATE RECORD NAMES NO FACE: data/%s_lockgate.json' % act)
    p = os.path.join(data, face)
    with open(p, encoding='utf-8') as f:
        has = (f.read().find('THE REGISTRATION LOCK') >= 0)
    if not has and run_seal:
        r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--lock', p], capture_output=True, text=True,
                           encoding='utf-8', errors='replace')
        print((r.stdout + r.stderr).rstrip())
        if r.returncode != 0:
            raise Refused('reg_seal.py --lock exit %d on data/%s: the face is not locked' % (r.returncode, face))
    rel = os.path.relpath(p, repo).replace(os.sep, '/')
    a = _git(repo, 'add', '--', rel)
    if a.returncode != 0:
        raise Refused('git add of data/%s exit %d' % (face, a.returncode))
    blob = _git(repo, 'show', ':' + rel).stdout
    conds = lock_check(blob, rec)
    print('\n'.join(['  THE LOCK BLOCK IN THE LOCK COMMIT ((R356)(3)(i)):'] + conds))
    return conds


ACT_PHASES = ('step zero', 'component 1', 'component 2', 'component 3', 'component 4', 'component 5', 'component 6', 'pre-root', 'root', 'record', 'closing')   # ### v1.28.1: root ; v1.34.6, (R365)(2)(iii) with b755's amendment row 1: components 5 and 6
WRITES = ('add', 'restore', 'delete', 'branch', 'switch', 'merge', 'ff', 'pushto', 'rdelete')   # ### v1.28.1: branch, the push-<act>-<stage> branch at HEAD ; v1.35.4, (R367)(3): switch and merge, a kernel's alone ; v1.36.0, (R368)(6)(i): ff, a kernel's alone, by FF_ACTS ; v1.36.1, (R368)(6)(ii): pushto, a kernel's alone, by PUSHTO_ACTS ; v1.36.3, (R369)(4)(i): rdelete, a kernel's alone, by RDELETE_ACTS
MARK = os.path.join(RELAY, '.git', 'standing_write_open.json')


# ================================================================================ v1.28.0 (iv): THE WRITE MARK
def _alive(pid):
    """the process `pid` still running (Windows: OpenProcess and its exit code; elsewhere signal 0)."""
    try:
        pid = int(pid)
    except (TypeError, ValueError):
        return False
    if os.name == 'nt':
        import ctypes
        k = ctypes.windll.kernel32
        h = k.OpenProcess(0x1000, False, pid)
        if not h:
            return False
        code = ctypes.c_ulong()
        ok = k.GetExitCodeProcess(h, ctypes.byref(code))
        k.CloseHandle(h)
        return bool(ok) and code.value == 259
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def mark_refusal(mark, alive):
    """None, or the refusal, for a write while the mark `mark` (its dict, or None) stands and its holder is `alive`. Pure."""
    if not mark:
        return None
    if alive:
        return 'ANOTHER WRITE OF THE ACT IS OPEN: %s (pid %s, since %s) -- one git write per message, every write through this tool' % (
            mark.get('what'), mark.get('pid'), mark.get('at'))
    return None


def open_mark(what, path=MARK):
    """take the act's write mark, exclusively; a mark whose holder has exited is removed and named; a live one refuses."""
    for _ in range(2):
        try:
            fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            try:
                with open(path, encoding='utf-8') as f:
                    m = json.load(f)
            except (OSError, ValueError):
                m = dict(what='unreadable mark', pid=None, at='?')
            bad = mark_refusal(m, _alive(m.get('pid')))
            if bad:
                raise Refused(bad)
            print('  a stale write mark removed: %s (pid %s, exited)' % (m.get('what'), m.get('pid')))
            os.remove(path)
            continue
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(dict(what=what, pid=os.getpid(), at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), f)
        return path
    raise Refused('THE WRITE MARK COULD NOT BE TAKEN: %s' % path)


def close_mark(path=MARK):
    try:
        os.remove(path)
    except OSError:
        pass


# ================================================================================ v1.28.0 (ii), (v), (iii), (vii): THE CHECKS BEFORE A COMMIT
def scan_counts(text):
    """(counts dict, controls ok) from the scan's foot, or (None, False) where it carries none. Pure."""
    import re
    m = re.search(r'PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS (\d+) OF (\d+) AS WANTED', text or '')
    if not m:
        return None, False
    c = dict(address=int(m.group(1)), name=int(m.group(2)), previous=int(m.group(3)), orcid=int(m.group(4)), places=int(m.group(5)))
    return c, m.group(6) == m.group(7)


def scan_refusal(text, rc):
    c, ctl = scan_counts(text)
    if rc != 0 or c is None:
        return 'THE SCAN DID NOT RUN TO ITS FOOT (exit %d)' % rc
    if not ctl:
        return 'THE SCAN`S CONTROLS NOT AS WANTED'
    if c['address'] or c['name'] or c['previous'] or c['orcid']:
        return 'THE SCAN FOUND AN OCCURRENCE: address %d, name %d, previous name %d, ORCID %d' % (c['address'], c['name'], c['previous'], c['orcid'])
    return None


def run_scan(act, what='a commit', bank_dir=None, bank_act=None):
    """v1.28.0 (ii), v1.29.0 (R359)(3)(ii): the act's scan over the staged set, run WITHOUT --bank; its run appended to the per-commit bank
    data/<act>_address_scan_commits.txt (bank_dir for a control), never to the act's scan bank or the post-lock bank. v1.34.0, (R364)(3)(iii):
    `bank_act` the act whose per-commit bank takes the run -- the next act's, for the closing step-row commit, whose own act's bank stands
    committed and is pushed after it (the closes of b749 to b753 appended there after its last commit, five running)."""
    import act as A
    p = os.path.join(T, '%s_address_scan.py' % act)
    if not os.path.isfile(p):
        raise Refused('THE ACT`S SCAN TOOL IS NOT CARRIED: tools/%s_address_scan.py' % act)
    r = subprocess.run([sys.executable, '-X', 'utf8', '-u', p, 'scan'], capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=RELAY)
    out = (r.stdout or '') + (r.stderr or '')
    bad = scan_refusal(out, r.returncode)
    foot = [l for l in out.split('\n') if 'PREVIOUS ADDRESS:' in l and '**' in l]
    print('  THE SCAN OVER THE STAGED SET ((R358)(3)(ii)): %s' % (foot[-1].strip() if foot else '### NO FOOT'))
    if r.returncode == 0 and foot:   # ### a refused or footless run is printed above, not banked as a run
        bp = os.path.join(bank_dir or os.path.join(RELAY, 'data'), A.scan_commits_name(bank_act or act))
        prior = open(bp, encoding='utf-8').read() if os.path.exists(bp) else ''
        body = A.scan_commits_append(prior, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), what, out.replace('\r', ''))
        with open(bp + '.tmp', 'wb') as fh:
            fh.write(body.encode('utf-8'))
        os.replace(bp + '.tmp', bp)
        shown = bp.replace(os.sep, '/')
        if shown.lower().startswith(RELAY.replace(os.sep, '/').lower() + '/'):
            shown = shown[len(RELAY) + 1:]
        print('  appended to %s (the per-commit bank, v1.29.0 (ii))' % shown)
    if bad:
        raise Refused(bad)
    return out   # ### v1.35.4, (R367)(3): the run's text, so a kernel's commit reads the repositories it names


# ================================================================================ v1.29.0 (i): ONE CALL OF THE TOOL PER MESSAGE
def _calls_path():
    """v1.34.0, (R364)(3)(xv): the calls ledger by the one resolver (tools/standing/statedir.py), as the hook reads it; the temp directory where
    the resolver does not import, as the hook falls back."""
    try:
        import statedir as SD
        return SD.calls_path()
    except Exception:  # noqa: BLE001
        return os.path.join(__import__('tempfile').gettempdir(), 'standing-calls.jsonl')


CALLS = _calls_path()


def calls_tail(path=CALLS, n=400):
    """the calls ledger's last n records (hook.py record_call writes one per shell call: request, id, at, cmd, refused)."""
    try:
        with open(path, 'rb') as f:
            f.seek(0, 2)
            size = f.tell()
            f.seek(max(0, size - 400000))
            raw = f.read().decode('utf-8', errors='replace').split('\n')
    except OSError:
        return []
    out = []
    for l in raw[-n:]:
        try:
            out.append(json.loads(l))
        except ValueError:
            continue
    return out


def _runs_me(cmd, argv):
    """the command runs this tool (a command of it matching gitwrite.RUNS_COMMIT) with these first two arguments."""
    import gitwrite as GW
    raw = (cmd or '').replace('\\', '/')
    return any(GW.RUNS_COMMIT.match(c) for c in GW.commands(raw)) and all(a in raw for a in argv[:2])


def message_refusal(records, argv, GW=None):
    """(refusal or None, note). Pure over the ledger's records. This call's record is the latest allowed one running this tool with these
    arguments; another allowed record of the same message (the same request stamp) carrying a git write -- a call of this tool or a bare
    git add -- refuses this one. No record found: no refusal, the note says so (the hook stands in front)."""
    if GW is None:
        import gitwrite as GW
    mine = next((k for k in range(len(records) - 1, -1, -1) if not records[k].get('refused') and _runs_me(records[k].get('cmd'), argv)), None)
    if mine is None:
        return None, 'no ledger record of this call (run outside the hook)'
    req = records[mine].get('request')
    if not req:
        return None, 'this call`s record carries no request stamp'
    others = [r for k, r in enumerate(records) if k != mine and r.get('request') == req and not r.get('refused') and GW.writes(r.get('cmd') or '')]
    if others:
        o = others[0]
        return ('ANOTHER GIT WRITE LANDED IN THIS MESSAGE (request %s): %s at %s -- one call of the tool per message, the add its own message' % (
            req, ' '.join((o.get('cmd') or '').split())[:90], o.get('at'))), 'refused'
    return None, 'the message %s carries this call alone among git writes' % req


def carry_check(act, exists):
    """None, or the refusal, for the act's first commit: its module, worklist and scan tool carried (exists: rel path -> bool). Pure."""
    need = ('tools/acts/%s.py' % act, 'tools/%s_worklist.py' % act, 'tools/%s_address_scan.py' % act)
    miss = [n for n in need if not exists(n)]
    return ('THE CARRY HAS NOT RUN: %s not carried -- the carry runs before the act`s first commit and its scan' % ', '.join(miss)) if miss else None


def gate_standing_refusal(staged):
    std = [n for n in (staged or []) if n.startswith('tools/standing/')]
    return ('A STANDING CHANGE AT THE GATE: %s staged -- a standing repair lands with its version before the gate' % ', '.join(std[:4])) if std else None


def satisfiable_refusal(audit, stamped):
    """None, or the refusal, from the satisfiability audit's text and whether it is stamped against the face as it stands. Pure."""
    if not audit:
        return 'THE SATISFIABILITY READ HAS NOT RUN: data/audit_<act>_reg_satisfiable.txt absent (record gatebanks before the gate commit)'
    v = [l for l in audit.split('\n') if 'VERDICT' in l]
    if not v or 'JOINTLY SATISFIABLE' not in v[-1]:
        bad = [l.strip() for l in audit.split('\n') if 'CONTRADICTORY' in l and 'VERDICT' not in l]
        return 'NOT SATISFIABLE: %s' % ('; '.join(b[:120] for b in bad[:3]) or (v[-1].strip() if v else 'no verdict'))
    if not stamped:
        return 'THE SATISFIABILITY READ IS NOT STAMPED AGAINST THE FACE AS IT STANDS: run record gatebanks again'
    return None


def act_check(act, phase, words):
    """v1.26.0, (R356)(3)(iii), b745 events: every act commit through the tool, its row in the same call. The subject is "<act> <phase>: <words>"
    with words given; the phase one of ACT_PHASES."""
    if phase not in ACT_PHASES:
        raise Refused('the act phase %r is not one of %s' % (phase, ' | '.join(ACT_PHASES)))
    w = (words or '').strip()
    if not w:
        raise Refused('THE ACT COMMIT NAMES NOTHING: the words after "%s %s:" name what the commit carries' % (act, phase))
    if w.startswith('%s ' % act):
        raise Refused('THE WORDS REPEAT THE HEAD: give the words after "%s %s:" only' % (act, phase))
    return '%s %s: %s' % (act, phase, w)


def staged_lines(repo):
    """(names, the HEAD-side line numbers the staged diff touches), from `git diff --cached -U0`."""
    import re
    names = [p for p in _git(repo, 'diff', '--cached', '--name-only').stdout.split('\n') if p]
    old = []
    for m in re.finditer(r'^@@ -(\d+)(?:,(\d+))? \+\d+(?:,\d+)? @@', _git(repo, 'diff', '--cached', '-U0').stdout, re.M):
        a, n = int(m.group(1)), int(m.group(2)) if m.group(2) is not None else 1
        old += list(range(a, a + n)) if n else [a]
    return names, old


def settings_sha():
    import hashlib
    try:
        return hashlib.sha256(open(SETTINGS, 'rb').read()).hexdigest().upper()
    except OSError:
        return None


def preflight(act, phase, words, repo, rows, read, lock_runner=None):
    """the subject, or Refused before anything is written: the phase, the record it names, the step bank's lock row, the subject's check, the index."""
    if phase in ACT_PHASES:   # ### v1.26.0, (R356)(3)(iii)
        subj = act_check(act, phase, words)
        if phase == 'step zero':   # ### v1.28.0, (R358)(3)(v)
            bad = carry_check(act, lambda n: os.path.isfile(os.path.join(RELAY, n)))
            if bad:
                raise Refused(bad)
        if _git(repo, 'diff', '--cached', '--quiet').returncode == 0:
            raise Refused('nothing staged in %s (the add is its own message)' % repo)
        return subj
    if phase not in PHASES:
        raise Refused('the phase %r is not one of %s' % (phase, ' | '.join(PHASES + ACT_PHASES)))
    if phase == 'repair':   # ### v1.24.0, (R354)(2)(ii)
        if os.path.abspath(repo) != os.path.abspath(RELAY):
            raise Refused('the repair phase is the relay`s alone (the act module)')
        names, old = staged_lines(repo)
        subj, conds = repair_check(act, words, rows, read('%s_events.txt' % act) or '', settings_sha(), names, old)
        print('\n'.join(['  THE REPAIR PHASE`S CONDITIONS ((R354)(2)(ii)):'] + conds))
        return subj
    if phase in RECORD and not read(RECORD[phase] % act):
        raise Refused('THE RECORD THE SUBJECT NAMES DOES NOT EXIST: data/%s' % (RECORD[phase] % act))
    if phase in ('lock', 'gate') and any(r.get('phase') == 'lock' for r in rows):
        raise Refused('A LOCK ROW STANDS: the commit after the lock takes phase `seal`, and the seal record must exist first')
    # ### v1.23.0, (R353)(3)(ii), b742 events (1)-(2): the tool takes no subject text for lock, gate and seal; the subject is the composer's whole
    if (words or '').strip():
        raise Refused('SUBJECT TEXT GIVEN FOR %s: the commit tool composes the %s subject from the banks and takes no words (%r)' % (phase.upper(), phase, words.strip()[:60]))
    staged = [p for p in _git(repo, 'diff', '--cached', '--name-only').stdout.split('\n') if p] if phase == 'gate' else None
    if phase == 'gate':   # ### v1.28.0, (R358)(3)(iii), (vii)
        bad = gate_standing_refusal(staged) or satisfiable_refusal(read('audit_%s_reg_satisfiable.txt' % act), face_stamped(act, data_dir(read)))
        if bad:
            raise Refused(bad)
    subj = SJ.compose(act, phase, '', read, staged=staged)
    bad = SJ.check(act, phase, subj, read)
    if bad:
        raise Refused('the composed subject faults: %s' % '; '.join(bad))
    if phase == 'lock' and lock_runner is not None:   # ### v1.26.0, (R356)(3)(i): the lock block written and staged inside the tool
        lock_runner()
    if _git(repo, 'diff', '--cached', '--quiet').returncode == 0:
        raise Refused('nothing staged in %s (the add is its own message)' % repo)
    return subj


def commit(repo, subj):
    """the commit by argument list; (full sha, the subject read back)."""
    r = _git(repo, 'commit', '-q', '-m', subj)
    if r.returncode != 0:
        raise Refused('git commit exit %d: %s' % (r.returncode, (r.stderr or r.stdout).strip()[:200]))
    full = _git(repo, 'rev-parse', 'HEAD').stdout.strip()
    back = _git(repo, 'log', '-1', '--format=%s', full).stdout.rstrip('\n')
    return full, back


def record_row(key, phase, full):
    """the row by the record tool's own step route (data/<act>_steps.json, its bank hashes kept by that tool)."""
    r = subprocess.run([sys.executable, '-X', 'utf8', '-u', os.path.join(S, 'fold.py'), 'record', 'step', key, phase, full],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout + r.stderr).strip()


def standing_dry_refusal(repo, act, names):
    """v1.28.0 (viii): None, or the refusal, for the staged `names` -- tools/standing/ staged with the record's dry over it (standingdry.check)."""
    import hashlib
    import standingdry as SD
    if not any(n.startswith('tools/standing/') for n in names):
        return None
    dry_rel = 'data/%s_standing_dry.txt' % act
    dry = _git(repo, 'show', ':' + dry_rel).stdout if dry_rel in names else ''
    sha = {}
    for n in names:
        if n.startswith('tools/standing/'):
            b = subprocess.run(['git', '-C', repo, 'show', ':' + n], capture_output=True).stdout
            sha[n] = hashlib.sha256(b.replace(b'\r\n', b'\n')).hexdigest()
    return SD.check(names, dry, sha)


STAGES = ('preroot', 'record', 'closing')


def branch_refusal(act, verb, name):
    """v1.28.1: None, or the refusal, for a branch create -- the act's push branch alone, push-<act>-<preroot|record|closing>. Pure."""
    if verb != 'branch':
        return None
    if name not in ['push-%s-%s' % (act, s) for s in STAGES]:
        return 'NOT THE ACT`S PUSH BRANCH: %r -- the branch write makes push-%s-<%s> alone' % (name, act, '|'.join(STAGES))
    return None


def rows_only(act, names):
    """v1.28.1: True where the staged set is the step bank alone (with the scan's banks): a step-rows commit, which carries rows and writes
    none of its own (b747's practice), so the step bank is clean before the push. Pure."""
    steps = 'data/%s_steps.json' % act
    beside = {steps, 'data/%s_address_scan.txt' % act, 'data/%s_address_scan_postlock.txt' % act, 'data/%s_address_scan_commits.txt' % act}
    return steps in names and set(names) <= beside


def scan_left_out(act, names, untracked):
    """v1.31.0, (R361)(3)(v), b750 defect (x), REPEAT b749 (c): None, or the refusal, for a relay commit staging `names` while the act's scan bank
    (data/<act>_address_scan.txt, or its post-lock bank) stands written and untracked (`untracked`, the relay's untracked paths) and is not staged.
    b750's scan bank, written 02:02:49Z, was left out of relay cc1fc182 and of the gate commit ac800f3d, and the root route's dry read 54 of 55
    banks; the gate route now runs the staged-set scan as the commit route does, and no commit leaves the scan's own bank behind. Pure."""
    left = [b for b in ('data/%s_address_scan.txt' % act, 'data/%s_address_scan_postlock.txt' % act) if b in set(untracked or ()) and b not in set(names or ())]
    return ('THE SCAN LEFT OUT OF A COMMIT: %s written and untracked, not staged -- stage it in this commit (the add is its own message)' % ', '.join(left)) if left else None


def close_left_out(banks, names, untracked):
    """v1.38.24, (R376)(7) [K24], b765 post-seal row (88): None, or the refusal, for a relay commit staging `names` while a bank of the close's
    mirror [23] or of the Project set's build [23a] (`banks`, standing.act.close_carried) stands written and untracked (`untracked`, the
    relay's untracked paths) and is not staged. b765's builder's three banks, written after the relay's pre-root push, stood outside a commit
    when its root read them; from b766 the build follows the mirror after the root, the closing commit [25] carries its banks with the
    mirror's, and no relay commit leaves one behind. Pure."""
    u, n = set(untracked or ()), set(names or ())
    left = [b for b in banks or () if b in u and b not in n]
    return ('THE CLOSE`S BANKS LEFT OUT OF A COMMIT ((R376)(7) [K24]): %s written and untracked, not staged -- the closing commit [25] carries '
            'the mirror`s banks and the Project set`s together (the add is its own message)' % ', '.join(left)) if left else None


def version_refusal(names, head_version, staged_version):
    """v1.34.0, (R364)(3)(vi), (R345)(2)(iv), b753 events (7), (8), (9): None, or the refusal, for a relay commit staging `names`: a path under
    tools/standing/ staged without tools/standing/VERSION staged with it and moved (its staged text not its HEAD text; a patch number
    suffices). Pure; the caller reads the two VERSION texts (HEAD's and the index's)."""
    std = [n for n in names or () if n.startswith('tools/standing/') and n != 'tools/standing/VERSION']
    if not std:
        return None
    if 'tools/standing/VERSION' not in set(names):
        return ('A STANDING CHANGE WITHOUT ITS VERSION ((R364)(3)(vi)): %d path(s) under tools/standing/ staged (%s) and tools/standing/VERSION '
                'not staged with them -- move VERSION (a patch number suffices) and stage it in this commit' % (len(std), ', '.join(std[:4])))
    if (head_version or '').strip() == (staged_version or '').strip():
        return ('A STANDING CHANGE WITHOUT ITS VERSION ((R364)(3)(vi)): tools/standing/VERSION staged unmoved (%s) beside %s' % (
            (staged_version or '').strip(), ', '.join(std[:4])))
    return None


def shared_refusal(act, names, listed):
    """v1.35.2, (R366)(6), b755 (o) REPEAT b754 (c') REPEAT b753 (v'), 3 acts by data/b756_faults.txt: None, or the refusal, for a relay commit
    staging a shared tool (under tools/, outside tools/<act>_*, tools/acts/ and tools/standing/: standing.act.shared_edits' reading) that
    data/act_current.json's shared_edits as staged (`listed`) does not name. b753, b754 and b755 each committed tools/mirror_prevbuild.json at
    step zero and left the field unwritten, and G-ACT-CURRENT failed on that clause at the act part's probe. Pure; the caller reads the list."""
    sh = [n for n in names or () if n.startswith('tools/') and not n.startswith(('tools/%s_' % act, 'tools/acts/', 'tools/standing/'))]
    miss = [n for n in sh if n not in set(listed or ())]
    if not miss:
        return None
    return ('A SHARED TOOL STAGED AND NOT IN act_current`s shared_edits ((R364)(3)(xvi), b755 (o)): %s -- run `python -X utf8 -u '
            'tools/standing/amend.py shared --staged --write`, then stage data/act_current.json beside it (the add its own message)' % ', '.join(miss))


def staged_shared_refusal(repo, act, names):
    """v1.35.2: shared_refusal over the index, act_current's shared_edits read as staged (`git show :data/act_current.json`)."""
    try:
        listed = json.loads(_git(repo, 'show', ':data/act_current.json').stdout or '{}').get('shared_edits') or []
    except ValueError:
        listed = []
    return shared_refusal(act, names, listed)


def postlock_refusal(act, read, names):
    """v1.38.10, (R374)(5) [K11]: the seal commit refused where the post-lock address scan is not in its place by the close order's step [8a]
    (standing.act.postlock_place): a run of data/<act>_address_scan_postlock.txt stamped at or after the seal record's time, its bank staged
    with the seal. None where it stands; `read` the tool's reader of relay data/ (a control's stand-in)."""
    import act as A
    ok, why = A.postlock_place(act, (read(RECORD['seal'] % act) or {}).get('at'), read('%s_address_scan_postlock.txt' % act) or '', names)
    return None if ok else ('THE POST-LOCK SCAN NOT IN ITS PLACE ((R374)(5) [K11], the close order`s step [8a]): %s -- run `tools/%s_address_scan.py '
                            'scan --bank` after close.py`s seal route and stage its bank with the seal' % (why, act))


def staged_version_refusal(repo, names=None):
    """v1.34.0, (R364)(3)(vi): version_refusal over `repo`'s staged set (read from the index where `names` is None), HEAD's VERSION against
    the index's. The one reading run() and the controls' replay on a scratch clone both call."""
    if names is None:
        names = [p for p in _git(repo, 'diff', '--cached', '--name-only').stdout.split('\n') if p]
    return version_refusal(names, _git(repo, 'show', 'HEAD:tools/standing/VERSION').stdout, _git(repo, 'show', ':tools/standing/VERSION').stdout)


# ================================================================================ v1.35.4, (R367)(3): THE ROUTE FOR KERNEL WRITES
def repo_refusal(key, act):
    """None, or the refusal, for a write ordered in `key` while `act` runs: relay and pp always; a kernel of KERNELS where KERNEL_ACTS opens it
    for the act; any other name -- a third kernel among them -- refused. Pure."""
    if key in ('relay', 'pp'):
        return None
    if key not in KERNELS:
        return 'NOT A REPOSITORY THE TOOL WRITES: %r -- relay | pp | the kernels an act`s ruling opens (%s) ((R367)(3))' % (key, ', '.join(sorted(KERNELS)))
    if key not in KERNEL_ACTS.get(act, ()):
        return 'A KERNEL THE ACT`S RULING DOES NOT OPEN: %s while %s runs -- the kernels are opened act by act (%s) ((R367)(3))' % (
            key, act, '; '.join('%s: %s' % (a, ', '.join(k)) for a, k in sorted(KERNEL_ACTS.items())))
    return None


def push_branch_ok(act, name):
    """the name is the act's push branch in a kernel, push-<act>-<word>. Pure."""
    import re
    return bool(re.match(r'^push-%s-[a-z0-9][a-z0-9-]*$' % re.escape(act), name or ''))


def kernel_branch_refusal(act, name):
    return None if push_branch_ok(act, name) else 'NOT THE ACT`S PUSH BRANCH IN A KERNEL: %r -- a kernel`s branch is push-%s-<word> ((R367)(3))' % (name, act)


def merge_branch_refusal(act, head):
    """None, or the refusal, for a merge or a commit in a kernel while `head` is checked out (None or '' where HEAD is detached). Pure."""
    if push_branch_ok(act, head):
        return None
    return 'A KERNEL`S MERGE OR COMMIT ON A BRANCH OUTSIDE THE push-%s-* FORM: %r checked out -- nothing written ((R367)(3))' % (act, head or 'a detached HEAD')


def conflict_refusal(act, key, conflicted):
    """None, or the refusal, for a merge whose conflicted files are `conflicted`: each must be a file the act's ruling names for `key`. Pure."""
    named = (NAMED_CONFLICTS.get(act) or {}).get(key) or ()
    out = sorted(c for c in conflicted or () if c not in named)
    if out:
        return 'A CONFLICT IN A FILE THE RULING DOES NOT NAME: %s (named for %s: %s) -- THE MERGE ABORTED, NOTHING CONCLUDED ((R367)(3))' % (
            ', '.join(out), key, ', '.join(named) or 'none')
    return None


def identity_refusal(kernel, relay):
    """None, or the refusal, for a kernel's commit: `kernel` and `relay` the (user.email, user.name) each repository resolves; the kernel's must
    equal the relay's, and the relay's address be of the noreply form. Pure; neither is printed."""
    if not kernel[0] or not kernel[1] or tuple(kernel) != tuple(relay) or not (relay[0] or '').endswith(NOREPLY):
        return 'THE KERNEL`S COMMIT IDENTITY IS NOT THE RELAY`S NOREPLY IDENTITY: address equal %s, name equal %s, the noreply form %s -- nothing committed ((R367) N5)' % (
            kernel[0] == relay[0], kernel[1] == relay[1], (relay[0] or '').endswith(NOREPLY))
    return None


def scan_names(out, key):
    """the act's scan run `out` names `key` among the repositories it read (its line '## THE REPOSITORIES READ ...: a; b; c'). Pure."""
    for l in (out or '').split('\n'):
        if l.startswith('## THE REPOSITORIES READ'):
            return key in [x.strip() for x in l.split(':', 1)[-1].split(';')]
    return False


def _head_branch(repo):
    return _git(repo, 'symbolic-ref', '--short', '-q', 'HEAD').stdout.strip()


def _merging(repo):
    return _git(repo, 'rev-parse', '-q', '--verify', 'MERGE_HEAD').stdout.strip()


def _dirty(repo):
    return [l for l in _git(repo, 'status', '--porcelain', '--untracked-files=no').stdout.split('\n') if l.strip()]


def _conflicted(repo):
    return [p for p in _git(repo, 'diff', '--name-only', '--diff-filter=U').stdout.split('\n') if p]


def _identity(repo):
    return (_git(repo, 'config', 'user.email').stdout.strip(), _git(repo, 'config', 'user.name').stdout.strip())


def _commit_of(repo, rev):
    return _git(repo, 'rev-parse', '-q', '--verify', '%s^{commit}' % rev).stdout.strip()


def kernel_write(key, verb, args, act, repo):
    """the git argument list for a kernel's write, or Refused before anything is written; `merge` is completed by kernel_merge_after."""
    if verb in ('restore', 'delete', 'switch', 'merge') and len(args) != 1:
        raise Refused('ONE %s PER CALL' % verb.upper())
    if verb == 'add':
        return ['add', '--'] + list(args)
    if verb == 'restore':
        return ['checkout', '--', args[0]]
    if verb in ('branch', 'switch', 'merge') and (_dirty(repo) or _merging(repo)):
        raise Refused('THE KERNEL`S TREE IS NOT CLEAN OR A MERGE STANDS OPEN (%d tracked changes, MERGE_HEAD %s) -- nothing written' % (
            len(_dirty(repo)), _merging(repo)[:8] or 'none'))
    if verb == 'branch':
        if len(args) != 2:
            raise Refused('A KERNEL`S BRANCH NAMES ITS COMMIT: branch push-%s-<word> <commit> ((R367)(3))' % act)
        bad = kernel_branch_refusal(act, args[0])
        if bad:
            raise Refused(bad)
        full = _commit_of(repo, args[1])
        if not full:
            raise Refused('NOT A COMMIT OF %s: %s' % (key, args[1]))
        if _commit_of(repo, 'refs/heads/%s' % args[0]):
            raise Refused('THE BRANCH STANDS ALREADY IN %s: %s' % (key, args[0]))
        return ['checkout', '-q', '-b', args[0], full]
    if verb == 'switch':
        if args[0] != 'main':
            bad = kernel_branch_refusal(act, args[0])
            if bad:
                raise Refused(bad)
        return ['checkout', '-q', args[0]]
    if verb == 'merge':
        bad = merge_branch_refusal(act, _head_branch(repo))
        if bad:
            raise Refused(bad)
        full = _commit_of(repo, args[0])
        if not full:
            raise Refused('NOT A COMMIT OF %s: %s' % (key, args[0]))
        return ['merge', '--no-ff', '--no-commit', full]
    if verb == 'delete':
        bad, _a = kernel_delete_args(key, act, args[0], False)
        if bad:
            raise Refused(bad)
        tip = _commit_of(repo, 'refs/heads/%s' % args[0])
        if not tip:
            raise Refused('NO SUCH BRANCH IN %s: %s' % (key, args[0]))
        if _head_branch(repo) == args[0]:
            raise Refused('THE BRANCH IS CHECKED OUT: %s -- switch first' % args[0])
        held = _git(repo, 'merge-base', '--is-ancestor', tip, 'refs/remotes/origin/main').returncode == 0
        return kernel_delete_args(key, act, args[0], held)[1]
    raise Refused('the write %r is not one of %s' % (verb, ' | '.join(WRITES)))


def forced_name(key, act, name, table=None, rtable=None):
    """v1.38.22, (R376)(7) [K22]: the name stands in FORCED_DELETES (or `table`, a control's) and in RDELETE_ACTS (or `rtable`) for the act at
    the kernel. Pure."""
    t = FORCED_DELETES if table is None else table
    r = RDELETE_ACTS if rtable is None else rtable
    return name in ((t.get(act) or {}).get(key) or ()) and name in ((r.get(act) or {}).get(key) or ())


def kernel_delete_args(key, act, name, held, table=None, rtable=None):
    """v1.38.22, (R376)(7) [K22]: (refusal, None) or (None, the git arguments) for a kernel's local branch delete: the one name FORCED_DELETES
    names for the act at the kernel, `branch -D`; else the act's push branch, `-D` where the remote's main holds its tip (`held`) or for the
    act's control branches and `-d` otherwise; any other name refused. Pure."""
    if forced_name(key, act, name, table=table, rtable=rtable):
        return None, ['branch', '-D', name]
    bad = kernel_branch_refusal(act, name)
    if bad:
        return bad, None
    return None, ['branch', '-D' if (held or name.startswith('push-%s-control' % act)) else '-d', name]


def kernel_merge_after(key, act, repo, rc, out):
    """after `git merge --no-ff --no-commit`: the line printed, or Refused with the merge aborted where it conflicts outside the named files."""
    mh = _merging(repo)
    if rc == 0:
        if not mh:
            return 'ALREADY CONTAINED, NOTHING MERGED: %s' % out.strip()[:120]
        return 'MERGED WITHOUT CONFLICT, NOT CONCLUDED: MERGE_HEAD %s, %d paths staged -- the commit route concludes it' % (
            mh[:8], len([p for p in _git(repo, 'diff', '--cached', '--name-only').stdout.split('\n') if p]))
    conf = _conflicted(repo)
    bad = conflict_refusal(act, key, conf) if conf else 'THE MERGE FAILED WITH NO FILE CONFLICTED (exit %d): %s' % (rc, out.strip()[:160])
    if bad:
        if _merging(repo):
            _git(repo, 'merge', '--abort')
        raise Refused('%s ; after the abort: HEAD %s, MERGE_HEAD %s, tracked changes %d' % (
            bad, _commit_of(repo, 'HEAD')[:8], _merging(repo)[:8] or 'none', len(_dirty(repo))))
    return 'CONFLICTED IN A FILE THE RULING NAMES: %s (MERGE_HEAD %s) -- the seat resolves it, adds it by this tool, and the commit route concludes the merge' % (
        ', '.join(conf), mh[:8])


def ff_refusal(key, act):
    """v1.36.0, (R368)(6)(i): None, or the refusal, for `ff` in `key` while `act` runs: a kernel of KERNELS that FF_ACTS opens for the act. Pure."""
    if key not in KERNELS:
        return 'THE FAST-FORWARD IS A KERNEL`S ALONE: %r -- the kernels %s ((R368)(6)(i))' % (key, ', '.join(sorted(KERNELS)))
    if key not in FF_ACTS.get(act, ()):
        return 'A KERNEL THE ACT`S RULING DOES NOT OPEN TO THE FAST-FORWARD: %s while %s runs (%s) ((R368)(6)(i))' % (
            key, act, '; '.join('%s: %s' % (a, ', '.join(k)) for a, k in sorted(FF_ACTS.items())) or 'none')
    return None


def remote_head(repo, branch):
    """(the sha of origin's refs/heads/<branch> by one ls-remote, or '' ; the exit). Reads only."""
    ref = 'refs/heads/%s' % branch
    r = _git(repo, 'ls-remote', 'origin', ref)
    sha = ''
    for l in (r.stdout or '').split('\n'):
        p = l.split('\t')
        if len(p) == 2 and p[1].strip() == ref:
            sha = p[0].strip()
    return sha, r.returncode


def ff_plan(old, new, ancestor, checked_out, clean):
    """the git argument list of the fast-forward, None where the local main equals the remote's (nothing to write), or Refused. Pure."""
    if not new:
        raise Refused('THE REMOTE`S MAIN NOT READ -- nothing written ((R368)(6)(i))')
    if not old:
        raise Refused('NO LOCAL MAIN IN THE CLONE -- nothing written ((R368)(6)(i))')
    if old == new:
        return None
    if not ancestor:
        raise Refused('THE LOCAL MAIN %s IS NOT AN ANCESTOR OF THE REMOTE`S MAIN %s -- NOT A FAST-FORWARD, nothing written ((R368)(6)(i))' % (
            old[:8], new[:8]))
    if checked_out:
        if not clean:
            raise Refused('MAIN IS CHECKED OUT AND THE TREE IS NOT CLEAN OR A MERGE STANDS OPEN -- nothing written ((R368)(6)(i))')
        return ['merge', '--ff-only', '-q', new]
    return ['update-ref', '-m', 'commit.py ff main ((R368)(6)(i))', 'refs/heads/main', new, old]


def ff_route(key, args, act, repo):
    """v1.36.0, (R368)(6)(i): `ff main` in a kernel FF_ACTS opens; the line printed, or Refused."""
    if list(args) != ['main']:
        raise Refused('THE FAST-FORWARD TAKES main ALONE: `ff main` ((R368)(6)(i))')
    new, rc = remote_head(repo, 'main')
    if rc != 0:
        raise Refused('THE REMOTE`S MAIN NOT READ (ls-remote exit %d) -- nothing written ((R368)(6)(i))' % rc)
    full = _commit_of(repo, new) if new else ''
    if new and not full:
        raise Refused('THE REMOTE`S MAIN %s IS NOT IN THE CLONE -- nothing written ((R368)(6)(i))' % new[:8])
    old = _commit_of(repo, 'refs/heads/main')
    anc = bool(old and full) and _git(repo, 'merge-base', '--is-ancestor', old, full).returncode == 0
    co = _head_branch(repo) == 'main'
    cmd = ff_plan(old, full, anc, co, not (_dirty(repo) or _merging(repo)))
    track = _commit_of(repo, 'refs/remotes/origin/main')
    if cmd is None:
        return 'ALREADY AT THE REMOTE`S MAIN: main %s, read at the remote %s ; nothing written' % (old[:8], full[:8])
    r = _git(repo, *cmd)
    back = _commit_of(repo, 'refs/heads/main')
    if r.returncode != 0 or back != full:
        raise Refused('THE FAST-FORWARD FAILED: git %s exit %d (%s) ; main reads %s, the remote`s %s' % (
            cmd[0], r.returncode, ((r.stderr or r.stdout) or '').strip()[:120], back[:8], full[:8]))
    return 'FAST-FORWARDED: main %s -> %s, the remote`s main read by ls-remote (the remote-tracking main %s) ; %s ; read back %s, EQUAL' % (
        old[:8], full[:8], track[:8] or 'none', 'main checked out: merge --ff-only' if co else 'main not checked out: update-ref from the old value',
        back[:8])


def pushto_refusal(key, act, table=None):
    """v1.36.1, (R368)(6)(ii): None, or the refusal, for `pushto` in `key` while `act` runs: a kernel of KERNELS that PUSHTO_ACTS (or `table`, a
    control's) opens for the act. Pure."""
    t = PUSHTO_ACTS if table is None else table
    if key not in KERNELS:
        return 'THE PUSH TO A NAMED BRANCH IS A KERNEL`S ALONE: %r -- the kernels %s ((R368)(6)(ii))' % (key, ', '.join(sorted(KERNELS)))
    if key not in t.get(act, ()):
        return 'A KERNEL THE ACT`S RULING DOES NOT OPEN TO THE PUSH TO A NAMED BRANCH: %s while %s runs (%s) ((R368)(6)(ii))' % (
            key, act, '; '.join('%s: %s' % (a, ', '.join(k)) for a, k in sorted(t.items())) or 'no act opened: the route built for the acts after')
    return None


def pushto_name_refusal(name):
    """None, or the refusal, for the branch named: a non-main branch in the branch form. Pure."""
    import re
    n = name or ''
    if (n.lower() in ('main', 'master', 'head') or n.startswith(('refs/', '-')) or '..' in n or '//' in n or n.endswith(('/', '.', '.lock'))
            or not re.match(r'^[A-Za-z0-9][A-Za-z0-9._/-]*$', n)):
        return 'NOT A NON-MAIN BRANCH NAME: %r -- main, master, HEAD, a refs/ name and a name outside the branch form are refused ((R368)(6)(ii))' % name
    return None


def pushto_plan(full, tip, tip_local, ancestor):
    """'new' (the branch made), 'forward' (its tip moved forward), None (the tip equal to the commit: nothing to push), or Refused. Pure."""
    if not full:
        raise Refused('NOT A COMMIT OF THE CLONE -- nothing pushed ((R368)(6)(ii))')
    if not tip:
        return 'new'
    if not tip_local:
        raise Refused('THE BRANCH`S REMOTE TIP %s IS NOT IN THE CLONE -- its ancestry unread, nothing pushed ((R368)(6)(ii))' % tip[:8])
    if tip_local == full:
        return None
    if not ancestor:
        raise Refused('THE BRANCH`S REMOTE TIP %s IS NOT AN ANCESTOR OF %s -- NOT A FAST-FORWARD, nothing pushed, no push forced ((R368)(6)(ii))' % (
            tip[:8], full[:8]))
    return 'forward'


def pushto_route(key, args, act, repo):
    """v1.36.1, (R368)(6)(ii): `pushto <commit> <branch>` in a kernel PUSHTO_ACTS opens; the line printed, or Refused."""
    if len(args) != 2:
        raise Refused('THE PUSH NAMES ITS COMMIT AND ITS BRANCH: `pushto <commit> <branch>` ((R368)(6)(ii))')
    bad = pushto_name_refusal(args[1])
    if bad:
        raise Refused(bad)
    full = _commit_of(repo, args[0])
    tip, rc = remote_head(repo, args[1])
    if rc != 0:
        raise Refused('THE BRANCH`S REMOTE TIP NOT READ (ls-remote exit %d) -- nothing pushed ((R368)(6)(ii))' % rc)
    tip_local = _commit_of(repo, tip) if tip else ''
    anc = bool(tip_local and full) and _git(repo, 'merge-base', '--is-ancestor', tip_local, full).returncode == 0
    kind = pushto_plan(full, tip, tip_local, anc)
    if kind is None:
        return 'ALREADY AT THE COMMIT: refs/heads/%s at the remote reads %s ; nothing pushed' % (args[1], tip[:8])
    r = _git(repo, 'push', '--porcelain', 'origin', '%s:refs/heads/%s' % (full, args[1]))
    back, rc2 = remote_head(repo, args[1])
    if r.returncode != 0 or rc2 != 0 or back != full:
        raise Refused('THE PUSH FAILED OR ITS READ-BACK IS UNEQUAL: git push exit %d (%s) ; the remote reads %s, the commit %s' % (
            r.returncode, ((r.stderr or r.stdout) or '').strip()[:120], back[:8] or 'none', full[:8]))
    return 'PUSHED, NOT FORCED: %s to refs/heads/%s at the remote (%s) ; read back by ls-remote %s, EQUAL' % (
        full[:8], args[1], 'the branch made' if kind == 'new' else 'its tip %s moved forward' % tip[:8], back[:8])


def kept_names(act, key):
    """v1.36.3, (R369)(4)(i): the names the act's worklist keeps in kernel `key` -- its KEPT_BRANCHES rows (path, name) whose path is the
    kernel's (the previous closing's carried list (f)); Refused where the worklist or the list cannot be read. Reads only."""
    import importlib.util
    p = os.path.join(T, '%s_worklist.py' % act)
    if not os.path.exists(p):
        raise Refused('THE ACT`S WORKLIST NOT FOUND: tools/%s_worklist.py -- the kept list unread, nothing removed ((R369)(4)(i))' % act)
    try:
        spec = importlib.util.spec_from_file_location('%s_worklist_kept' % act, p)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        rows = tuple(m.KEPT_BRANCHES)
    except Exception as e:  # noqa: BLE001
        raise Refused('THE KEPT LIST NOT READ from tools/%s_worklist.py (%s: %s) -- nothing removed ((R369)(4)(i))' % (act, type(e).__name__, str(e)[:80]))
    want = os.path.normcase(os.path.normpath(KERNELS[key]))
    return tuple(n for path, n in rows if os.path.normcase(os.path.normpath(path)) == want)


def rdelete_refusal(key, act, name, table=None, kept=None):
    """v1.36.3, (R369)(4)(i): None, or the refusal, for `rdelete <name>` in `key` while `act` runs: a kernel of KERNELS that RDELETE_ACTS (or
    `table`, a control's) opens for the act; not main and in the branch form; not on the kept list (`kept`, a control's, or the act's
    worklist's for the kernel); named by the act's ruling. Pure where `kept` is given."""
    t = RDELETE_ACTS if table is None else table
    if key not in KERNELS:
        return 'THE REMOVAL AT A REMOTE IS A KERNEL`S ALONE: %r -- the kernels %s ((R369)(4)(i))' % (key, ', '.join(sorted(KERNELS)))
    named = (t.get(act) or {}).get(key) or ()
    if not named:
        return 'A KERNEL THE ACT`S RULING DOES NOT OPEN TO THE REMOVAL AT ITS REMOTE: %s while %s runs (%s) ((R369)(4)(i))' % (
            key, act, '; '.join('%s: %s' % (a, ', '.join(sorted(k))) for a, k in sorted(t.items())) or 'none')
    if pushto_name_refusal(name):
        return 'MAIN, OR A NAME OUTSIDE THE BRANCH FORM: %r -- main is never removed, nothing removed ((R369)(4)(i))' % name
    if name in (kept_names(act, key) if kept is None else kept):
        return 'A NAME ON THE KEPT LIST: %s in %s -- nothing removed ((R369)(4)(i))' % (name, key)
    if name not in named:
        return 'A BRANCH THE ACT`S RULING DOES NOT NAME FOR REMOVAL: %s in %s (named: %s) -- nothing removed ((R369)(4)(i))' % (
            name, key, ', '.join(named))
    return None


def rdelete_plan(main_sha, tip, main_local, tip_local, ancestor, forced=False):
    """'remove', or Refused: the remote's main read, the branch at the remote, both commits in the clone, the tip an ancestor of main -- or,
    v1.38.22, (R376)(7) [K22], `forced`, the one name FORCED_DELETES names, its tip read in the clone and taken though not merged. Pure."""
    if not main_sha:
        raise Refused('THE REMOTE`S MAIN NOT READ -- nothing removed ((R369)(4)(i))')
    if not tip:
        raise Refused('THE BRANCH IS ABSENT AT THE REMOTE -- nothing to remove ((R369)(4)(i))')
    if not main_local:
        raise Refused('THE REMOTE`S MAIN %s IS NOT IN THE CLONE -- the ancestry unread, nothing removed ((R369)(4)(i))' % main_sha[:8])
    if not tip_local:
        raise Refused('THE BRANCH`S REMOTE TIP %s IS NOT IN THE CLONE -- the ancestry unread, nothing removed ((R369)(4)(i))' % tip[:8])
    if not ancestor and not forced:
        raise Refused('THE BRANCH`S REMOTE TIP %s IS NOT AN ANCESTOR OF THE REMOTE`S MAIN %s -- UNMERGED, nothing removed ((R369)(4)(i))' % (
            tip[:8], main_sha[:8]))
    return 'remove'


def rdelete_route(key, args, act, repo, table=None, kept=None, ftable=None):
    """v1.36.3, (R369)(4)(i): `rdelete <branch>` in a kernel RDELETE_ACTS opens; the line printed, or Refused. v1.38.22, (R376)(7) [K22]: the
    one name FORCED_DELETES names (or `ftable`, a control's) taken though its tip is not merged."""
    if len(args) != 1:
        raise Refused('ONE BRANCH PER CALL: `rdelete <branch>` ((R369)(4)(i))')
    name = args[0]
    bad = rdelete_refusal(key, act, name, table=table, kept=kept)
    if bad:
        raise Refused(bad)
    forced = forced_name(key, act, name, table=ftable, rtable=table)
    main_sha, rc1 = remote_head(repo, 'main')
    if rc1 != 0:
        raise Refused('THE REMOTE`S MAIN NOT READ (ls-remote exit %d) -- nothing removed ((R369)(4)(i))' % rc1)
    tip, rc2 = remote_head(repo, name)
    if rc2 != 0:
        raise Refused('THE BRANCH`S REMOTE TIP NOT READ (ls-remote exit %d) -- nothing removed ((R369)(4)(i))' % rc2)
    main_local = _commit_of(repo, main_sha) if main_sha else ''
    tip_local = _commit_of(repo, tip) if tip else ''
    anc = bool(main_local and tip_local) and _git(repo, 'merge-base', '--is-ancestor', tip_local, main_local).returncode == 0
    rdelete_plan(main_sha, tip, main_local, tip_local, anc, forced=forced)
    r = _git(repo, 'push', '--porcelain', 'origin', ':refs/heads/%s' % name)
    back, rc3 = remote_head(repo, name)
    if r.returncode != 0 or rc3 != 0 or back:
        raise Refused('THE REMOVAL FAILED OR ITS READ-BACK IS NOT ABSENT: git push exit %d (%s) ; the remote reads %s (exit %d)' % (
            r.returncode, ((r.stderr or r.stdout) or '').strip()[:120], back[:8] or 'absent', rc3))
    if not anc:
        return ('REMOVED AT THE REMOTE, NO PUSH FORCED: refs/heads/%s (its tip %s, NOT an ancestor of the remote`s main %s, taken by its name in '
                'FORCED_DELETES, (R376)(7) [K22]) ; read back by ls-remote ABSENT' % (name, tip[:8], main_sha[:8]))
    return 'REMOVED AT THE REMOTE, NOT FORCED: refs/heads/%s (its tip %s, an ancestor of the remote`s main %s) ; read back by ls-remote ABSENT' % (
        name, tip[:8], main_sha[:8])


def usage_lines():
    """v1.31.0, (R361)(3)(viii), b750 defects (b), (k), (o), (u), (y): the tool's usage, its phases and its word form, printed by the carry at step
    zero (tools/standing/carry.py ruled) so the seat reads them before its opening call."""
    use = [l.strip() for l in (__doc__ or '').split('\n') if l.strip().startswith('python -X utf8 -u tools/standing/commit.py')]
    return ['THE ONE-CALL TOOL`S USAGE ((R361)(3)(viii)), read before the opening call:'] + ['  ' + u for u in use] + [
        '  the phases: %s (no words) ; %s (words after "<act> <phase>: ", never opening "<act> ") ; the writes: %s' % (
            ' | '.join(PHASES[:3]), ' | '.join(ACT_PHASES), ' | '.join(WRITES)),
        '  repair takes the words naming the edits; a step-rows commit takes the tool`s words: "the step row for relay <sha8>"']


def write_route(key, verb, args, act=None, repo=None, mark_path=MARK):
    """v1.28.0 (iv): an add, a restore or a branch delete, under the act's write mark; Refused where nothing was written. v1.35.4, (R367)(3):
    a kernel of KERNELS (opened for the act) takes add, restore, branch <name> <commit>, switch, merge and delete by kernel_write; `repo` a
    scratch clone standing for the kernel, for a control; a key that names a path (an earlier control's scratch clone) reads as before."""
    import act as A
    act = act or A.current()['act']
    kern = key in KERNELS
    repo = repo or (REPOS[key] if key in REPOS else key)
    if verb not in WRITES:
        raise Refused('the write %r is not one of %s' % (verb, ' | '.join(WRITES)))
    if not args:
        raise Refused('THE %s NAMES NOTHING' % verb.upper())
    if any(ch in a for a in args for ch in '*?['):
        raise Refused('A GLOB IN THE %s: name each path (%s)' % (verb.upper(), ' '.join(args)[:80]))
    if verb == 'ff':   # ### v1.36.0, (R368)(6)(i): its own table, apart from KERNEL_ACTS
        bad = ff_refusal(key, act)
        if bad:
            raise Refused(bad)
    elif verb == 'pushto':   # ### v1.36.1, (R368)(6)(ii): its own table
        bad = pushto_refusal(key, act)
        if bad:
            raise Refused(bad)
    elif verb == 'rdelete':   # ### v1.36.3, (R369)(4)(i): its own table, the kept list and the named branches, read again in the route
        if len(args) != 1:
            raise Refused('ONE BRANCH PER CALL: `rdelete <branch>` ((R369)(4)(i))')
        bad = rdelete_refusal(key, act, args[0])
        if bad:
            raise Refused(bad)
    elif kern:
        bad = repo_refusal(key, act)
        if bad:
            raise Refused(bad)
    elif verb in ('switch', 'merge'):
        raise Refused('THE %s WRITE IS A KERNEL`S ALONE ((R367)(3)): %s' % (verb.upper(), key))
    if not kern:
        if verb in ('restore', 'delete', 'branch') and len(args) != 1:
            raise Refused('ONE %s PER CALL' % verb.upper())
        bad = branch_refusal(act, verb, args[0])   # ### v1.28.1
        if bad:
            raise Refused(bad)
    mark = open_mark('%s %s in %s: %s' % (act, verb, key, ' '.join(args)[:120]), path=mark_path)
    try:
        if verb == 'ff':   # ### v1.36.0
            return ff_route(key, args, act, repo)
        if verb == 'pushto':   # ### v1.36.1
            return pushto_route(key, args, act, repo)
        if verb == 'rdelete':   # ### v1.36.3
            return rdelete_route(key, args, act, repo)
        if kern:
            cmd = kernel_write(key, verb, args, act, repo)
        else:
            cmd = {'add': ['add', '--'] + list(args), 'restore': ['checkout', '--', args[0]], 'delete': ['branch', '-d', args[0]],
                   'branch': ['branch', '--', args[0]]}[verb]
        r = _git(repo, *cmd)
        if kern and verb == 'merge':
            return kernel_merge_after(key, act, repo, r.returncode, (r.stdout or '') + (r.stderr or ''))
    finally:
        close_mark(mark_path)
    if r.returncode != 0:
        raise Refused('git %s exit %d: %s' % (' '.join(cmd[:2]), r.returncode, (r.stderr or r.stdout).strip()[:200]))
    return (r.stdout + r.stderr).strip()


def flag_read(flag=None):
    """v1.34.0, (R364)(3)(xxi): (pending, why, times) by tools/standing/hold.py; `flag` a planted (pending, why, times)."""
    if flag is not None:
        return flag
    import hold as HD
    p, w = HD.restart_pending()
    return p, w, (HD.restart_times() if p else {})


def run(key, phase, words, act=None, data=None, row_writer=None, after_seal=None, scanner=None, scan_dir=None, flag=None, repo=None):
    """one call: preflight, commit, read back, row. Returns a dict of what was done; Refused where nothing was. `scan_dir`: the folder the
    per-commit scan bank is written in (a control's scratch clone), the relay's data/ where None. v1.34.0, (R364)(3)(xxi): the restart flag read
    before every commit; set, the lock is refused and any other commit is the boundary the seat stops at (printed). v1.35.4, (R367)(3): a
    kernel's commit -- an act phase alone, on the checked-out push-<act>-* branch, with the relay's identity, nothing left conflicted, the
    scan's run naming the kernel; an open merge concluded by it, its second parent read back; `repo` a scratch clone standing for the kernel."""
    import act as A
    import hold as HD
    fp, fw, ft = flag_read(flag)
    if fp and phase == 'lock':
        raise Refused('THE RESTART FLAG SET (%s; the keys last written %s): THE LOCK NOT TAKEN -- an event of the act; the seat stops for the '
                      'author`s word ((R364)(3)(xxi))' % (fw, ', '.join('%s %s' % kv for kv in sorted(ft.items())) or 'not read'))
    act = act or A.current()['act']
    data = data or os.path.join(RELAY, 'data')
    kern = key in KERNELS
    repo = repo or (REPOS[key] if key in REPOS else key)
    read = reader(data)
    rows = (read('%s_steps.json' % act) or {}).get('rows') or []
    lr = (lambda: lock_face(repo, act, read, data)) if (phase == 'lock' and key == 'relay') else None
    mh = None
    if kern:   # ### v1.35.4, (R367)(3): every condition read before the mark is taken and before anything is written
        bad = repo_refusal(key, act)
        if not bad and phase not in ACT_PHASES:
            bad = 'NO %s IN A KERNEL: a kernel takes the act phases alone (%s) ((R367)(3))' % (phase.upper(), ' | '.join(ACT_PHASES))
        bad = bad or merge_branch_refusal(act, _head_branch(repo)) or identity_refusal(_identity(repo), _identity(RELAY))
        if not bad and _conflicted(repo):
            bad = 'A FILE LEFT CONFLICTED IN %s: %s -- resolve it and add it by this tool before the commit concludes the merge' % (key, ', '.join(_conflicted(repo)))
        if bad:
            raise Refused(bad)
        mh = _merging(repo) or None
    mark = open_mark('%s commit %s in %s' % (act, phase, key)) if row_writer is None else None   # ### v1.28.0 (iv): the act's write mark
    try:
        subj = preflight(act, phase, words, repo, rows, read, lock_runner=lr)
        names = [p for p in _git(repo, 'diff', '--cached', '--name-only').stdout.split('\n') if p]
        bad = standing_dry_refusal(repo, act, names)   # ### v1.28.0 (viii)
        if bad:
            raise Refused(bad)
        if os.path.abspath(repo) == os.path.abspath(RELAY):   # ### v1.34.0, (R364)(3)(vi): VERSION moves with every standing change
            bad = staged_version_refusal(repo, names)
            if bad:
                raise Refused(bad)
        if os.path.abspath(repo) == os.path.abspath(RELAY):   # ### v1.35.2, (R366)(6), b755 (o): a shared tool with act_current's shared_edits naming it
            bad = staged_shared_refusal(repo, act, names)
            if bad:
                raise Refused(bad)
        if os.path.abspath(repo) == os.path.abspath(RELAY):   # ### v1.31.0, (R361)(3)(v)
            unt = [p for p in _git(repo, 'ls-files', '--others', '--exclude-standard', '--', 'data/').stdout.split('\n') if p]
            bad = scan_left_out(act, names, unt) or close_left_out(A.close_carried(act), names, unt)   # ### v1.38.24, (R376)(7) [K24]
            if bad:
                raise Refused(bad)
        if phase == 'seal' and os.path.abspath(repo) == os.path.abspath(RELAY):   # ### v1.38.10, (R374)(5) [K11]: the post-lock scan in its place, step [8a]
            bad = postlock_refusal(act, read, names)
            if bad:
                raise Refused(bad)
        only = phase in ACT_PHASES and os.path.abspath(repo) == os.path.abspath(RELAY) and rows_only(act, names)   # ### v1.28.1
        if only:
            head = json.loads(_git(repo, 'show', 'HEAD:data/%s_steps.json' % act).stdout or '{}')
            staged = json.loads(_git(repo, 'show', ':data/%s_steps.json' % act).stdout or '{}')
            want = SJ.step_rows_words(SJ.step_rows_added(head, staged))
            if not want or words.strip() != want:
                raise Refused('A STEP-ROWS COMMIT NAMES ITS ROWS: the words must read %r, given %r' % (want or '(no row staged)', words.strip()))
        if scanner is False:   # ### v1.29.0 (iii): no commit without the scan
            raise Refused('A COMMIT WITHOUT THE SCAN: the tool runs the act`s scan over the staged set before every commit')
        # ### v1.34.0, (R364)(3)(iii): the closing step-row commit's scan, taken over its staged set before it as every commit's is, is written to
        # ### the next act's per-commit bank as that bank's opening rows; nothing is appended to the act's own bank, committed and then pushed
        nxt = ('b%d' % (int(act[1:]) + 1)) if (only and phase == 'closing') else None
        what = '%s commit %s in %s' % (act, phase, key) + ((', the closing step-row commit: its scan written to %s`s per-commit bank as its opening rows '
                                                            '((R364)(3)(iii))' % nxt) if nxt else '')
        sc = (scanner or (lambda a: run_scan(a, what, bank_dir=scan_dir, bank_act=nxt)))(act)   # ### v1.28.0 (ii); v1.29.0 (ii) the per-commit bank
        if kern and not scan_names(sc, key):   # ### v1.35.4, (R367)(3): the scan over the kernel's staged set, read from its own run
            raise Refused('THE SCAN DID NOT READ THE KERNEL: %s is not among the repositories its run names (its line "## THE REPOSITORIES READ") '
                          '-- nothing committed' % key)
        full, back = commit(repo, subj)
    finally:
        if mark:
            close_mark(mark)
    if only:
        rc, out = 0, 'NONE WRITTEN: a step-rows commit carries the rows and writes none of its own (v1.28.1)'
    else:
        rc, out = (row_writer or record_row)(key, phase, full)
    done = dict(act=act, repo=key, phase=phase, commit=full, subject=subj, read_back=back, equal=back == subj, row_exit=rc, row=out,
                rowed=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), flag=HD.boundary_line(fp, fw, ft))
    if mh:   # ### v1.35.4, (R367)(3): the merge the commit concluded, its second parent read back against the MERGE_HEAD it found
        p2 = _commit_of(repo, '%s^2' % full)
        done['merge'] = 'THE MERGE CONCLUDED: the commit`s second parent %s, the MERGE_HEAD %s: %s' % (p2[:8], mh[:8], 'EQUAL' if p2 == mh else '### NOT EQUAL')
        done['equal'] = done['equal'] and p2 == mh
    if phase == 'seal':
        done['excludes'] = (after_seal or excludes)()
    return done


def repeat_of(msg, act, data=None):
    """v1.22.0, (R352)(2)(v), b741 event (1): a refusal printed with its class: the latest earlier act's events or defects row carrying the
    refusal's head words (the text before its first colon), "REPEAT of <act> event (<n>)" / "defect (<x>)", or NEW where none does."""
    import re
    data = data or os.path.join(RELAY, 'data')
    head = msg.split(':')[0].strip()
    n = int(act[1:])
    hits = []
    for f in os.listdir(data):
        m = re.match(r'^b(\d+)_(events|defects)\.txt$', f)
        if not m or int(m.group(1)) >= n:
            continue
        with open(os.path.join(data, f), encoding='utf-8', errors='replace') as fh:
            for l in fh.read().replace('\r', '').split('\n'):
                r = re.match(r"^    \(((?:[a-z]'*)|\d+)\) ", l)   # ### v1.34.0, (R364)(3)(viii)
                if r and head and head in l:
                    hits.append((int(m.group(1)), m.group(2)[:-1], r.group(1)))
    if not hits:
        return 'NEW'
    a, kind, x = max(hits)
    return 'REPEAT of b%d %s (%s)' % (a, kind, x)


def excludes():
    r = subprocess.run([sys.executable, '-I', '-X', 'utf8', os.path.join(S, 'hook.py'), 'excludes'], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return (r.stdout or r.stderr).strip()


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    if argv[0] not in ('relay', 'pp') and argv[1] not in ('ff', 'pushto', 'rdelete'):   # ### v1.35.4, (R367)(3): a third kernel, or a kernel the act's ruling does not open, refused before anything is read ; v1.36.0, v1.36.1, v1.36.3: ff, pushto and rdelete read by their own tables in write_route
        import act as A
        bad = repo_refusal(argv[0], A.current()['act'])
        if bad:
            sys.exit('### commit.py REFUSED, NOTHING WRITTEN: %s ### THE CLASS: %s' % (bad, repeat_of(bad, A.current()['act'])))
    bad, note = message_refusal(calls_tail(), argv)   # ### v1.29.0 (i)
    print('  ONE CALL PER MESSAGE ((R359)(3)(i)): %s' % note)
    if bad:
        import act as A
        sys.exit('### commit.py REFUSED, NOTHING WRITTEN: %s ### THE CLASS: %s' % (bad, repeat_of(bad, A.current()['act'])))
    if argv[1] in WRITES:   # ### v1.28.0 (iv)
        try:
            out = write_route(argv[0], argv[1], argv[2:])
        except Refused as e:
            import act as A
            sys.exit('### commit.py REFUSED, NOTHING WRITTEN: %s ### THE CLASS: %s' % (e, repeat_of(str(e), A.current()['act'])))
        print('  %s %s: %s%s' % (argv[1], argv[0], ' '.join(argv[2:]), ('\n  ' + out) if out else ''))
        return
    try:
        d = run(argv[0], argv[1], ' '.join(argv[2:]))
    except Refused as e:
        import act as A
        sys.exit('### commit.py REFUSED, NOTHING COMMITTED, NO ROW WRITTEN: %s ### THE CLASS: %s' % (e, repeat_of(str(e), A.current()['act'])))
    print('  commit %s %s' % (d['repo'], d['commit'][:8]))
    print('  subject   : %s' % d['subject'])
    print('  read back : %s -- %s' % (d['read_back'], 'EQUAL' if d['equal'] else '### NOT EQUAL'))
    print('  row       : %s (exit %d)' % (d['row'], d['row_exit']))
    if d.get('merge'):
        print('  merge     : %s' % d['merge'])   # ### v1.35.4, (R367)(3)
    print('  %s' % d.get('flag'))   # ### v1.34.0, (R364)(3)(xxi)
    if 'excludes' in d:
        print(d['excludes'])
    if not d['equal'] or d['row_exit'] != 0:
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
