# relay/tools/retired/ -- tools taken out of use, kept byte-for-byte

**First entry, b418 (2026-09-11). No retired directory existed in relay before this act.**

## `b369_hygiene.py`

**Retired by b418's Component 3, under the author's ferry.** Moved here byte-for-byte from `tools/`;
its bytes equal its blob at relay `1dc9f72`.

**The reason.** It was written at b369 to mend two rosters and install and exercise the pre-push
guard. Its success conditions were dated by its own success: its wording pairs were applied at b369
and cannot apply again, and its hook check reads `SIDE-effects/.git/hooks/pre-push`, which no guard
runs from since `core.hooksPath` names `.githooks`. Repaired at b417, it runs and its verdict is
FAILED on every run from now on. A tool whose verdict can never pass is a guard with nothing to say.

**Its last verdict.** `COMPONENT 2 : FAILED` -- relay `data/b417_live.txt`, reported and not edited.

**Its writes, as measured** (relay `data/b417_snapshot.txt`, `data/b417_live.txt`):
- broken (before b417's repair), it wrote nothing: it died on a retired path before its first write;
- run against a captured snapshot, it wrote its own three run records (contained), and through
  `b304_hooks.py`'s guard exercise it wrote one git object into each of SIDE-global-section,
  PLACE-papers and SIDE-effects (escaped; counted, not collected);
- run live, it rewrote `data/b369_hooks.txt` and `data/b369_hygiene.json` and created a new
  `b369_hygiene_notes` run record under a prior act's stem; all three were restored.

**What would have caught it.** `tools/repair_snapshot.py` (b417): a repaired tool runs first against
a captured snapshot, every write diffed, before it runs live. It is what did catch it at b417 -- its
escaped writes were two calls deep, and its own source names none of the repositories it wrote into.
The species is `SAFE_BY_BEING_BROKEN.md` (TECHNE-Core, local).

**Dated by this move, said rather than discovered.** These relay tools name its old path
`tools/b369_hygiene.py`; each is a frozen record of its own act, and each one that reads or runs the
file at that path will now find it absent:
- `tools/b369_bank.py`
- `tools/b369_checks.py`
- `tools/b369_correspondence.py`
- `tools/b369_filing.py`
- `tools/b369_index_append.py`
- `tools/b416_checks.py`
- `tools/b416_components.py`
- `tools/b416_desk_bank.py`
- `tools/b416_extract.py`
- `tools/b417_checks.py`
- `tools/b417_components.py`
- `tools/b417_desk_bank.py`
- `tools/b417_extract.py`
- `tools/b417_regspec.py`
- `tools/b418_extract.py`
- `tools/banked_index.py`
