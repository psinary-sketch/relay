# -*- coding: utf-8 -*-
"""place_add.py -- THE RESEARCH SEAT'S STAGING GUARD (built b148, after a breach).

### WHY THIS EXISTS. At b148 this seat ran `git add -A` in PLACE-papers and swept
### in EIGHT UNTRACKED FILES BELONGING TO THE PATENT SEAT -- seven figure SVGs and
### a figures README under phase1.5/method/patent-package/. The parallel-seats
### deconfliction had been ratified ONE ACT EARLIER, at b147.

### THE MECHANISM, WHICH IS THE PART WORTH BUILDING AGAINST: `git add -A` stages
### everything in the worktree, and this seat used it safely for many acts
### BECAUSE IT WAS THE ONLY WRITER. ### THE DECONFLICTION CHANGED THE GROUND UNDER
### A HABIT AND THE HABIT DID NOT NOTICE. A command that was safe under
### one-writer assumptions is not safe under two, and NOTHING ABOUT THE COMMAND
### CHANGED TO SIGNAL IT.

### WHY NOT .git/info/exclude: both seats share one clone on disk. Excluding the
### patent tree would break the PATENT seat's ability to stage its own work.
### A GUARD MUST CONSTRAIN THE SEAT THAT NEEDS CONSTRAINING, NOT THE REPOSITORY.

### WHAT IT DOES: stages exactly the paths given, refusing any that fall under a
### foreign-seat prefix, and REFUSES `-A` / `.` outright. It does not modify,
### move, or delete anything.

Usage:
    python place_add.py <path> [<path> ...]
"""
import os
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPO = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

# Prefixes this seat does not own. Per the b147 deconfliction: the patent seat
# writes only within the patent-package tree; the research seat owns the
# ledgers, the keystones and HANDOFF.
FOREIGN = ['phase1.5/method/patent-package/']


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    bad = [a for a in argv if a in ('-A', '--all', '.', '-u')]
    if bad:
        print("### REFUSED: %s stages the whole worktree." % ", ".join(bad))
        print("### That is the exact command that caused the b148 breach.")
        print("### Name the paths this seat owns, explicitly.")
        return 2
    foreign = []
    for a in argv:
        n = a.replace('\\', '/').lstrip('./')
        for f in FOREIGN:
            if n.startswith(f):
                foreign.append((a, f))
    if foreign:
        print("### REFUSED -- these paths belong to another seat:")
        for a, f in foreign:
            print("    %-58s (under %s)" % (a, f))
        print("### The b147 deconfliction: any edit either seat needs across the")
        print("### line ROUTES TO THE AUTHOR. This seat does not stage them.")
        return 2
    r = subprocess.run(['git', 'add', '--'] + list(argv), cwd=REPO)
    if r.returncode == 0:
        print("staged (%d path%s), foreign-seat prefixes checked: %s"
              % (len(argv), '' if len(argv) == 1 else 's', ", ".join(FOREIGN)))
    return r.returncode


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
