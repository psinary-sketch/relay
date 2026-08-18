# INCIDENT: THE HELD ACTS WERE PUSHED PUBLIC FOR ~3 MINUTES — DETECTED, REPAIRED, DISCLOSED
## ### **EXECUTOR ERROR, SELF-DETECTED ON THE NEXT CHECK: A `cd`-CHAIN LANDED A COMMIT-AND-PUSH IN THE WRONG REPOSITORY, PUBLISHING THE TWO `W-CARRIER-BUILD` ACTS; THE PUBLIC BRANCH WAS FORCE-PUSHED CLEAN WITHIN MINUTES; THE EXPOSURE IS DISCLOSED, NOT MINIMIZED**

**Relay report · 2026-08-18 · executor-filed, unprompted · for the author and for counsel's awareness**

---

## WHAT HAPPENED

1. During the implications filing, a command intended for PLACE-papers ran in the relay (a `cp` in a
   prior chain had failed, leaving the shell's working directory in the wrong repository; the retry
   chain began `cd /d/relay && cp …` for the packet copy and then ran `git add -A && git commit &&
   git push origin main` — in the relay, on local `main`, WHICH SITS ON TOP OF THE HELD COMMIT).
2. ### **RESULT: origin/main briefly carried the HELD ancestry — the two `W-CARRIER-BUILD` act files
   (`reports/2026-08-13-carrier-build-act{1,2}.md`) were PUBLIC on the remote.**
3. Detected on the immediately following verification (`ls-tree origin/main | grep carrier-build`
   returned the two files — the standing check did its job).
4. ### **REPAIRED: a clean branch was rebuilt from the last good public tip (`5c7e18f`), the filing
   commit cherry-picked onto it, and `origin/main` FORCE-PUSHED to `df2f54d` — verified 0
   carrier-build files public; the local HELD-on-top arrangement restored (2 files local).**

## THE EXPOSURE, STATED PLAINLY

*The HELD files were reachable on the public remote for roughly the interval between the bad push and
the force-push (~3 minutes). Anyone who fetched in that window has them; GitHub may retain the
now-unreachable commits in its object store and cache until garbage-collected —* ### **a support
request to purge unreachable objects is the standard remedy and is COUNSEL-RELEVANT; the author
decides whether to file it.** *The acts' content is the `C1` adjudication held pending counsel — the
exposure is of exactly the material the procedure exists to hold.*

## RESIDUE AND CAUSE

*The repaired public commit (`df2f54d`) also carries six `.olean` build artifacts swept in by the
errant `add -A` — compiled from already-public `.lean` sources: clutter, not a leak; cleanup at the
author's word rather than another force-push. The PLACE-papers changes the errant command was meant
to commit were unaffected (committed separately after the repair).*

**Cause:** the session's shell keeps its working directory across commands, and three earlier
`cd`-chain misfires this session were harmless and treated as friction rather than as a hazard. This
one was not harmless. **The near-misses were the warning; the executor logged them and did not
harden.**

## PROPOSED HARDENING (for the author's word — a Rule-4 addendum, NOT minted unilaterally)

1. **Every relay `git` invocation uses `git -C D:\relay …` (and PLACE-papers likewise) — no
   cwd-dependent git, ever.**
2. **`git add -A` is banned in the relay** — adds are by explicit file list only.
3. **A push to the relay's `origin main` happens ONLY from a `push-*` branch created at the verified
   public tip** — never from local `main`; a pre-push check greps the outgoing ancestry for `HELD`.

**`h2` UNCHANGED. The register untouched. This report is the disclosure.**
