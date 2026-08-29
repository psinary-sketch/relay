# -*- coding: utf-8 -*-
"""b257 COMPONENT 2 -- the loom entry and the contribution map's OWED discharge.

### ### **BOTH ARE APPEND-ONLY. ### THE MAP'S `OWED` MARKER STAYS VISIBLE ABOVE ITS DISCHARGE**
### (b240's append-only-document law; b244's precedent when it amended a docstring it had ruled on).
### b256 is NOT rewritten.
"""
import io
import sys

PP = r'D:\MY-DOwnloads\PLACE-papers'
LOOM = PP + r'\VERIFICATION_LOOM.md'
MAP = PP + r'\phase1.5\method\CONTRIBUTION_MAP_2026-08.md'

LOOM_ENTRY = u"""
---

## 2026-08-29 \u00b7 b257 \u2014 THE GUARD EXCEPTION, ITS MECHANISM, AND THE RESTORATION

**The ruling (author, ratified on paste):** the deconfliction guard bypassed for **exactly one
commit** on PLACE-papers whose diff is the untracking of `phase1.5/method/patent-package`
(`git rm -r --cached`, no working-tree deletion) plus the `.gitignore` line.

**Why an exception was needed.** The b179 pre-commit hook enumerates staged paths with
`git diff --cached --name-only` and refuses on any foreign prefix. ### **That query cannot
distinguish a removal *from the index* from a write *of another seat's tree*.** The ruled repair is
the former; the guard was built against the latter. At first attempt the hook **refused, exit 1**,
and the research seat **halted and restored the tree** rather than bypass \u2014 `--no-verify` was not
used, and the available amendment (permit foreign *deletions*) was deliberately not made, because
amending an enforcement instrument so one's own act passes is the shape b148 and b178 both took.

### **THE MECHANISM USED: THE GUARD'S OWN DOCUMENTED OVERRIDE.**

The hook's header states its limits, and **limit (2) reads, verbatim:** *"`git commit --no-verify`
bypasses it. **A hook constrains a habit; it does not constrain a decision.**"* The hook was minted
against a reflex (`git add -A` typed out of a one-writer habit); this was a ratified decision with a
specified diff. ### **So the ruling's fallback \u2014 a one-commit amendment restored immediately
after \u2014 was never reached, and neither guard file was edited.**

**The diff, exactly as ruled:** 21 deletions from the index + 1 modification (`.gitignore`).
**Nothing removed from disk**; 221 patent files remain in the working tree, owned by the patent
seat's own local-only repo. **`git ls-files` shows 0 patent-package paths tracked.** Pushed;
`ls-remote` matches.

### The restoration, demonstrated \u2014 and it is continuity, not repair

| demonstration | result |
|:--|:--|
| `place_add.py` offered a patent path | **REFUSED** |
| b179 hook against a **synthetic** staged patent path | **REFUSED, exit 1** |
| **positive control** \u2014 same hook, non-foreign path only | **CLEAN, exit 0** |
| guard files byte-unchanged | `git status` empty on both |

### **The positive control is what makes the refusal mean something: the guard discriminates, it
does not blanket-refuse.**

**And a structural fact learned in the attempt:** `git add -f` of a real patent path staged
**nothing**, because `patent-package/` is now **its own git repository** and the parent cannot stage
inside it at all. The hook then correctly reported *"NOTHING STAGED \u2014 NOTHING VERIFIED \u2026 this
is NOT a clean verdict"* (b167's law, working). ### **There is now a structural boundary beneath the
guard, and it is stronger than the guard.**

**Historic objects are NOT purged.** b258 measured them and they are a counsel question, listed on
`COUNSEL_ITEMS.md`. *Nothing deposits.*
"""

MAP_DISCHARGE = u"""
### **DISCHARGED 2026-08-29 (b257) \u2014 THE MARKER ABOVE STANDS AS WRITTEN AND WAS TRUE WHEN WRITTEN.**

The SIGNEDNESS quotation was supplied by the author on 2026-08-29 and is now carried **verbatim** at
`TECHNE-Core/modules/2026-08/SIGNEDNESS.md` (**PRIVATE, local-only, not pushed**), with its
provenance stated. ### **This row is discharged BY CITATION. ### b256 is not rewritten, and the
`OWED` marker above is left visible** (b240's append-only law).

**Three checks are recorded beside the author's text in that module, and none edits it:** two of the
five named clients (`Loci's Ratchet`, `DESI w = \u22121`) live in `archive/` rather than in live
REGISTRY rows; and `the crown act's \u03bb_n \u2265 0` was **not confirmed at the single document this
seat read** \u2014 which is a bounded absence, not a global one.
"""


def main():
    # ---- the loom: pure append
    t = io.open(LOOM, encoding='utf-8').read()
    if 'b257 \u2014 THE GUARD EXCEPTION' in t:
        sys.stdout.write("  loom: already entered, untouched\n")
    else:
        io.open(LOOM, 'w', encoding='utf-8', newline='\n').write(t.rstrip('\n') + '\n' + LOOM_ENTRY)
        back = io.open(LOOM, encoding='utf-8').read()
        sys.stdout.write("  loom: appended %d bytes; prefix intact: %s\n"
                         % (len(LOOM_ENTRY), "YES" if back.startswith(t.rstrip('\n')) else "NO"))

    # ---- the map: append the discharge immediately after the OWED annex row block
    m = io.open(MAP, encoding='utf-8').read()
    if 'DISCHARGED 2026-08-29 (b257)' in m:
        sys.stdout.write("  map: already discharged, untouched\n")
        return 0
    anchor = u"### The full list of"
    tail_anchor = u"\n---\n\n### **THE MAP STATES GRADES AND CONFERS NONE."
    if tail_anchor not in m:
        # fall back to appending before the closing rule line
        tail_anchor = u"\n---\n\n### **THE MAP STATES GRADES"
    if tail_anchor not in m:
        sys.stdout.write("  ### REFUSED: map anchor not found; nothing written\n")
        return 1
    out = m.replace(tail_anchor, MAP_DISCHARGE + tail_anchor, 1)
    io.open(MAP, 'w', encoding='utf-8', newline='\n').write(out)
    back = io.open(MAP, encoding='utf-8').read()
    sys.stdout.write("  map: discharge appended; OWED marker still present: %s\n"
                     % ("YES" if 'QUOTATION OWED' in back else "### NO"))
    sys.stdout.write("  map: deletions? original length %d -> %d (grew: %s)\n"
                     % (len(m), len(back), "YES" if len(back) > len(m) else "### NO"))
    return 0


if __name__ == '__main__':
    sys.exit(main())
