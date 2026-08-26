# -*- coding: utf-8 -*-
"""place_papers_pre_commit.py -- THE SEAT BOUNDARY, ENFORCED IN THE COMMAND PATH (built b179).

### WHY THIS EXISTS, AND IT IS NOT THE REASON THE FIRST GUARD EXISTS.
### At b148 this seat swept EIGHT patent-seat files into a commit and pushed them.
### The answer then was tools/place_add.py -- a safe staging command, built and
### TESTED AGAINST THE EXACT BREACH before entering service.
### At b178 this seat did it again, with EIGHTY-SIX files.
### ### place_add.py WAS PRESENT, WORKING, AND UNUSED. `git add -A` was typed instead.

### SO THE CAUSE OF THE SECOND BREACH IS NOT A MISSING GUARD.
### ### IT IS THAT THE GUARD HAD TO BE CHOSEN, AND A GUARD THAT MUST BE CHOSEN IS
### ### NOT ENFORCEMENT -- IT IS THE SAME INTENTION WEARING A TOOL'S CLOTHES.
### A pre-commit hook is different in exactly one way that matters: ### IT SITS IN
### THE PATH OF THE ORDINARY COMMAND. `git commit` runs it whether or not the
### operator remembered the rule. That is the whole of the fix.

### WHY A DENY-LIST OF FOREIGN PREFIXES AND NOT AN ALLOW-LIST OF THIS SEAT'S TREE.
### The ferry asked for a refusal of "any staged path outside the research seat's
### tree", which reads as an allow-list. ### AN ALLOW-LIST WOULD REQUIRE ENUMERATING
### THE RESEARCH SEAT'S TREE, AND THE b147 DECONFLICTION NEVER ENUMERATED IT --
### it named what the PATENT seat owns and said the research seat owns the ledgers,
### the keystones and HANDOFF. ### INVENTING THAT ENUMERATION WOULD BE MAKING THE
### AUTHOR'S DEFINITION, WHICH THE EXECUTOR DOES NOT DO. The deny-list encodes the
### boundary exactly as ratified and nothing more. ### THE ALLOW-LIST FORM REMAINS
### AVAILABLE AND IS THE AUTHOR'S TO CHOOSE.

### SINGLE SOURCE OF TRUTH: the prefixes are READ FROM tools/place_add.py, not
### copied. ### TWO GUARDS WITH TWO COPIES OF THE SAME LIST IS A LIE WAITING FOR
### ONE OF THEM TO BE EDITED.

# ### THE LIMIT, STATED HERE BECAUSE A GUARD WHOSE REACH IS NOT STATED WILL BE
# ### TRUSTED BEYOND IT:
# ### (1) .git/hooks IS NOT VERSIONED AND IS NOT CLONED. This file is committed as
# ###     the hook's SOURCE AND ITS REASON; the installed copy lives outside the
# ###     repository. ### SO A FRESH CLONE HAS NO ENFORCEMENT UNTIL SOMEONE
# ###     INSTALLS IT -- which is "a guard that must be chosen", one level up.
# ###     ### THE FIX IS REAL AND IT IS PARTIAL, AND THE CLASS IS NOT CLOSED.
# ### (2) `git commit --no-verify` bypasses it. A hook constrains a habit; it does
# ###     not constrain a decision.
# ### (3) It reads PATHS. It cannot tell whose work a path holds if the boundary
# ###     ever moves, and it knows nothing about the commit's message -- that is
# ###     commit_selfcheck.py's job (b149), and this does not replace it.
"""

import os
import re
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

HERE = os.path.dirname(os.path.abspath(__file__))
PLACE_ADD = os.path.join(os.path.dirname(HERE), 'place_add.py')


def foreign_prefixes():
    """### READ from place_add.py so the two guards cannot drift apart."""
    with open(PLACE_ADD, encoding='utf-8') as fh:
        src = fh.read()
    m = re.search(r"^FOREIGN\s*=\s*\[(.*?)\]", src, re.S | re.M)
    if not m:
        # ### A GUARD THAT CANNOT FIND ITS RULE MUST FAIL CLOSED, NEVER OPEN.
        print("### HOOK ABORT: FOREIGN list not found in %s" % PLACE_ADD)
        print("### FAILING CLOSED -- a guard that cannot read its own rule")
        print("### refuses the commit rather than allowing it.")
        sys.exit(2)
    return re.findall(r"'([^']+)'", m.group(1))


def staged(repo):
    r = subprocess.run(['git', 'diff', '--cached', '--name-only'],
                       cwd=repo, capture_output=True, text=True)
    return [l.strip().replace('\\', '/') for l in r.stdout.splitlines() if l.strip()]


def main():
    repo = os.environ.get('PLACE_REPO') or os.getcwd()
    pref = foreign_prefixes()
    files = staged(repo)
    hits = [(f, p) for f in files for p in pref if f.startswith(p)]

    print("--- SEAT-BOUNDARY PRE-COMMIT (b179) ---")
    print("  repo             : %s" % repo)
    print("  staged paths     : %d" % len(files))
    print("  foreign prefixes : %s" % ", ".join(pref))
    print("  foreign hits     : %d" % len(hits))

    if hits:
        print()
        print("### REFUSED -- THE COMMIT WOULD WRITE ANOTHER SEAT'S TREE.")
        for f, p in hits[:12]:
            print("    %-64s (under %s)" % (f[:64], p))
        if len(hits) > 12:
            print("    ... and %d more" % (len(hits) - 12))
        print()
        print("### THE b147 DECONFLICTION: the patent seat writes ONLY within the")
        print("### patent-package tree, and ANY EDIT EITHER SEAT NEEDS ACROSS THE")
        print("### LINE ROUTES TO THE AUTHOR. This seat does not commit them.")
        print("### THIS IS THE b148 BREACH (8 files) AND THE b178 BREACH (86).")
        print("### To stage safely:  python relay/tools/place_add.py <paths>")
        return 1

    if not files:
        # ### b167's LAW, AND IT CAUGHT THIS FILE ON ITS OWN FIRST CONTROL RUN:
        # ### A VERDICT OVER AN EMPTY SCOPE IS NOT A VERDICT. The first negative
        # ### control printed CLEAN over ZERO staged paths and proved nothing.
        # ### WHY THE EXIT CODE DIFFERS FROM banned_terms.py's HARD FAILURE (2):
        # ### a scanner asked to verify nothing has FAILED AT ITS JOB, but a commit
        # ### hook seeing nothing staged HAS NOT BEEN ASKED YET -- git refuses the
        # ### empty commit itself. ### THE VERDICT LANGUAGE MUST STILL NOT READ AS
        # ### A CLEARANCE, WHICH IS THE PART THAT MATTERS.
        print("  VERDICT          : ### NOTHING STAGED -- NOTHING VERIFIED")
        print("  ### this is NOT a clean verdict. No path was examined, so no")
        print("  ### boundary was checked. b167's law: a verdict over an empty")
        print("  ### scope is not a verdict.")
        return 0

    print("  VERDICT          : CLEAN -- no foreign-seat path staged")
    print("  ### and a clean verdict here means ONE thing only: no staged path")
    print("  ### begins with a foreign prefix. ### IT IS NOT A REVIEW OF THE COMMIT.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
