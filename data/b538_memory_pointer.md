---
name: mirror-after-last-push
description: "STANDING b537 — mirror builds run after the act's last PLACE-papers push, never before; builder name via -DateTag only"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 0e414d80-fcb3-4850-8359-5f1a764bc0e3
  modified: 2026-09-25T22:26:20.622Z
---

A mirror build runs after the act's last PLACE-papers push, never before. After the build, nothing more is written to PLACE-papers in that act. Any later record, such as the zip's sha256 or the verification, goes to relay, which clause 2 of `mirror_verify.py` does not compare.

**Why:** at b537 the seat built `mirror-refresh-2026-09-25-b537.zip` from `7c1c2da`, before its own OPEN_TRAILS append (`b7e0c52`). After the push, clause 2 read STALE and the mirror lacked the two work-orders (defect (c)). The author ordered a rebuild, `mirror-refresh-2026-09-25-b537-post.zip`, which reads CLEAN at `b7e0c52`. The pre-push zip is kept, superseded, and not deleted. The author made this ordering standing.

**How to apply:**
- On an act that builds a mirror, order it: record → PLACE-papers commit and push → build → head block → verify → relay-only closing.
- The builder (`tools/mirror_build.ps1`, never edited, per (R96)) takes only `-DateTag`. Both the zip name `mirror-refresh-<DateTag>.zip` and the stage folder `%TEMP%\mirror-build-<DateTag>` derive from it, so a variant name goes through `-DateTag`.
- The builder deletes an existing stage folder or zip of the same name. Check both paths are absent with `test ! -e … &&` in the same command ([[delete-only-verified-absolute-path]]).
- For the head block, split on LF only and keep the trailing CRLF (b537 defect (b)).
- **DISCHARGED at b538** (2026-09-25, on (R148)(5)): b538's OPEN_TRAILS record carries the pointer line. The bullet as written at b537 follows. **OWED, as of b537:** the next act that touches OPEN_TRAILS carries ONE line pointing to relay `data/b537_closing_addendum.txt`. That line is "the upload is the -post build; the pre-push build is superseded, kept, not deleted." It is b537 defect (d), the navigator's, and the author chose option 1. Discharge it there, then mark this bullet DISCHARGED.
