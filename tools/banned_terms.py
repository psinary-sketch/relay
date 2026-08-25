# -*- coding: utf-8 -*-
"""banned_terms.py -- THE BANNED-TERM REVIEW, BUILT (b142).

### WHY THIS EXISTS. Rule 3 bans two stems from the record's own voice. The
### review has been run act after act by hand-rolled one-liners, rewritten each
### time. b139 filed the general answer -- BUILD THE CHECK RATHER THAN PRAISE
### THE HABIT -- and b141 applied it to the probe habit. This applies it to the
### banned-term habit, which was the last discretionary check in the closing
### sequence.

### THE STEMS: "gap" and "blind".
### THE EXCEPTIONS, which are part of the rule and not softenings of it:
###   - QUOTED KERNEL IDENTIFIERS (sector_pattern_gap and its kin);
###   - CLAY / BIBLIOGRAPHY CITATIONS ("mass gap");
###   - RETIRED TERMS QUOTED INSIDE CORRECTION RECORDS (EXECUTOR_RULES sec 5);
###   - this file itself, which cannot state the rule without naming the stems.
### Anything else is a LIVE USE and must be corrected before shipping.

### THE SCOPE, AND IT IS THE WHOLE DIFFICULTY -- SEE THE DEFECT NOTE BELOW.
### The rule governs THE ACT'S OWN VOICE, so the scope is the act's ADDED LINES
### plus the whole of files the act CREATES. It is NOT whole existing files: a
### thirty-thousand-line ledger carries decades of quoted history that the act
### did not write and may not rewrite.

# ### DEFECT FIXED b142, ON THE CHECK'S FIRST RUN, AND IT IS THE SAME SPECIES
# ### AS THE PROBE GENERATOR'S: the first version scanned WHOLE FILES and
# ### returned 178 "live uses", every one of them a pre-existing line in a
# ### ledger this act only appended to. A scanner with no scope control does not
# ### report the rule -- it reports the corpus. ### THE SCOPE IS NOW DERIVED
# ### MECHANICALLY FROM THE ACT'S OWN DIFF, which is the probe-generation
# ### convention's principle carried to the second check that needed it.
# ### A SECOND DEFECT, FIXED IN THE SAME PASS: stdout was inheriting cp1252 and
# ### crashed on the first Greek letter it met. A check that dies on its own
# ### input is not a check.

# ### SECOND SCOPE DEFECT, FIXED b143, AND IT IS A DIFFERENT ONE. The diff scope
# ### counts a MOVED file as added lines. The twenty-fifth seam's archival split
# ### wrote five BYTE-EXACT archives of historical ledger text, and the review
# ### reported live uses inside them. ### THAT TEXT IS NOT THE ACT'S VOICE -- IT
# ### IS THE RECORD'S OWN HISTORY, AND "CORRECTING" IT WOULD BOTH DESTROY THE
# ### BYTE-EXACTNESS THE ARCHIVE EXISTS TO GUARANTEE AND FALSIFY WHAT THE RECORD
# ### ACTUALLY SAID. --exclude takes a path substring and is REQUIRED to be
# ### explicit: the exclusions used are printed in the scope block, so an
# ### exclusion can never be silent.

Usage:
    python banned_terms.py --diff <repo> [<rev>]     scope = added lines vs rev
    python banned_terms.py --new <file> [<file>...]  scope = whole file (new files)
    python banned_terms.py --exclude <substring>     drop paths containing it
    both may be combined; --new files are appended to the --diff scope.
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_emit as AE

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

STEMS = ['gap', 'blind']
PAT = re.compile(r'\b(' + '|'.join(STEMS) + r')\w*', re.I)

EXCEPT = [
    (re.compile(r'sector_pattern_gap|\w_gap\b|\bgap_\w|`[^`]*gap[^`]*`', re.I),
     'QUOTED KERNEL IDENTIFIER'),
    # ### the hyphenated form was a REGEX BUG, not a softening: "mass-gap
    # ### exclusion (Yang-Mills)" is the same standing Clay exception as "mass gap".
    (re.compile(r'mass[- ]gap|yang-?mills', re.I), 'CLAY / BIBLIOGRAPHY CITATION'),
    (re.compile(r'retired|superseded|correction record|corrected in place|CORRECTED IN PLACE|'
                r'formerly|no longer|banned|vocabulary repair',
                re.I), 'RETIRED TERM IN A CORRECTION RECORD'),
    (re.compile(r'STEMS|stems scanned|banned[- ]term', re.I), "THE SCANNER'S OWN RULE TEXT"),
]


# ### THE ARCHIVED-HEADING EXCEPTION, ADDED b143, AND IT IS EXACT RATHER THAN A
# ### GUESS. The twenty-fifth seam's pointer headers carry a MACHINE-GENERATED
# ### INDEX of the headings that moved to the archive, so that a citation to an
# ### archived section resolves in one hop. Those lines are VERBATIM QUOTATIONS
# ### OF HISTORICAL TITLES. ### EDITING ONE WOULD BREAK THE INDEX'S ONLY PURPOSE
# ### -- it would no longer name the heading it points at. The test is membership
# ### in the actual set of archived headings, read from the archive files, NOT a
# ### pattern that might match something else.
ARCHIVED_HEADINGS = set()


def load_archived_headings(archdir):
    if not os.path.isdir(archdir):
        return
    for fn in os.listdir(archdir):
        if fn == 'README.md' or not fn.endswith('.md'):
            continue
        txt = io.open(os.path.join(archdir, fn), encoding='utf-8', errors='replace').read()
        for h in re.findall(r'^##+ .*$', txt, re.M):
            ARCHIVED_HEADINGS.add(h.lstrip('#').strip())


# ### DEFECT FIXED b146, AND IT IS THE FIRST DEFECT IN THIS FAMILY THAT MADE A
# ### CHECK FALSELY PASS RATHER THAN FALSELY FAIL. Exceptions were matched against
# ### the WHOLE LINE, so any exception trigger anywhere on a line excused EVERY
# ### banned stem on that line. A genuine live use in this act's own draft --
# ### "THIS IS A REFUSAL, NOT A GAP" -- was excused because the same sentence
# ### ended "...retired the axis", which fired the retired-term exception thirty
# ### words away. ### AN EXCEPTION MUST BE ADJACENT TO WHAT IT EXCUSES. Matching
# ### is now done in a WINDOW around each individual hit, not across the line.
# ### A CHECK THAT WRONGLY EXCUSES IS WORSE THAN ONE THAT WRONGLY ALARMS: a false
# ### alarm is investigated, a false pass is filed as CLEAN and never seen again.
WINDOW = 40


# ### THE FOURTH DECLARED EXCEPTION, IMPLEMENTED b146. The docstring has listed
# ### "this file itself, which cannot state the rule without naming the stems"
# ### since b142, but it was never coded -- it only ever fired INCIDENTALLY, when
# ### a stem happened to sit near the words "stems scanned". The b146 windowing
# ### fix removed that accident and exposed the hole. ### A DECLARED EXCEPTION
# ### THAT IS NOT IMPLEMENTED IS NOT AN EXCEPTION; IT IS A COINCIDENCE THAT HAS
# ### BEEN HOLDING.
SELF = os.path.basename(__file__)


def classify(line, at=None, path=None):
    if path and os.path.basename(path) == SELF:
        return "THE SCANNER'S OWN SOURCE (declared exception, file-level)"
    s = line.strip()
    if s.startswith('> - ') and s[4:].strip() in ARCHIVED_HEADINGS:
        return 'QUOTED ARCHIVED HEADING (machine-generated index)'
    seg = line if at is None else line[max(0, at - WINDOW):at + WINDOW]
    for rx, name in EXCEPT:
        if rx.search(seg):
            return name
    return None


def added_lines(repo, rev):
    """### THE SCOPE, MECHANICALLY DERIVED. Nothing is typed; the act's own diff
    says which lines are the act's voice."""
    out = subprocess.run(['git', 'diff', rev, '-U0'], cwd=repo, capture_output=True,
                         text=True, encoding='utf-8', errors='replace').stdout
    cur, rows, n = None, [], 0
    for line in out.splitlines():
        if line.startswith('+++ b/'):
            cur = line[6:]
        elif line.startswith('@@'):
            m = re.search(r'\+(\d+)', line)
            n = int(m.group(1)) if m else 0
        elif line.startswith('+') and not line.startswith('+++') and cur:
            rows.append((cur, n, line[1:]))
            n += 1
    return rows


def main(argv):
    scope, srcs, excl = [], [], []
    i = 0
    while i < len(argv):
        if argv[i] == '--exclude':
            excl.append(argv[i + 1])
        elif argv[i] == '--archive-headings':
            load_archived_headings(argv[i + 1])
        i += 1
    i = 0
    while i < len(argv):
        if argv[i] == '--diff':
            repo = argv[i + 1]
            rev = argv[i + 2] if i + 2 < len(argv) and not argv[i + 2].startswith('--') else 'HEAD'
            scope += added_lines(repo, rev)
            srcs.append("added lines in %s vs %s" % (repo, rev))
            i += 3 if rev != 'HEAD' or (i + 2 < len(argv) and not argv[i + 2].startswith('--')) else 2
        elif argv[i] == '--new':
            i += 1
            while i < len(argv) and not argv[i].startswith('--'):
                txt = io.open(argv[i], encoding='utf-8', errors='replace').read()
                scope += [(argv[i], k, ln) for k, ln in enumerate(txt.splitlines(), 1)]
                srcs.append("whole file %s (created this act)" % os.path.basename(argv[i]))
                i += 1
        else:
            i += 1

    # ### THE EXCLUSION IS APPLIED BEFORE THE HITS ARE COUNTED. Applied after, it
    # ### would trim the display and leave the verdict unchanged -- a filter that
    # ### hides what it does not excuse, which is worse than no filter at all.
    if excl:
        before = len(scope)
        scope = [r for r in scope
                 if not any(x in r[0].replace(chr(92), '/') for x in excl)]
        srcs.append("EXCLUDED %d lines whose path contains: %s   ### stated, never silent"
                    % (before - len(scope), ", ".join(excl)))

    hits = live = 0
    rows = []
    for path, ln, text in scope:
        # ### EVERY hit on a line is classified SEPARATELY, in its own window.
        for m in PAT.finditer(text):
            hits += 1
            cls = classify(text, m.start(), path)
            if cls is None:
                live += 1
            rows.append((path, ln, cls,
                         (text.strip()[:60] + "   <<hit: " + m.group(0) + ">>")))

    files = sorted({p for p, _, _ in scope})
    print("=" * 78)
    print("BANNED-TERM REVIEW (banned_terms.py, b142) -- RUN, NOT CLAIMED")
    print("=" * 78)
    print("  stems scanned    : %s" % ", ".join(STEMS))
    for s in srcs:
        print("  scope            : %s" % s)
    print("  files in scope   : %d" % len(files))
    print("  lines in scope   : %d   ### the act's own voice, not the corpus" % len(scope))
    if ARCHIVED_HEADINGS:
        print("  archived headings: %d loaded, used as an EXACT exception set"
              % len(ARCHIVED_HEADINGS))
    print("  hits found       : %d" % hits)
    print("  live uses        : %d" % live)
    if rows:
        print("\n  THE HIT TABLE -- every hit shown with its class; none dropped:")
        for p, ln, cls, text in rows:
            print("   %-32s :%-6d %s" % (os.path.basename(p), ln,
                                         cls or "### LIVE USE -- CORRECT BEFORE SHIPPING"))
            print("      %s" % text)
    verdict = "CLEAN" if live == 0 else "NOT CLEAN"
    # ### --emit: THE TOOL WRITES ITS OWN AUDIT BLOCK (b153). The actor
    # ### embeds it verbatim and never retypes it.
    if '--emit' in argv:
        i = argv.index('--emit')
        act = argv[i + 1] if i + 1 < len(argv) else 'unknown'
        blk, sp = AE.emit('banned_terms', act, srcs,
                          [('stems', ', '.join(STEMS)), ('files', len(files)),
                           ('lines', len(scope)), ('hits', hits),
                           ('live uses', live)], verdict)
        print("\n" + blk)
        print("  sidecar written: %s" % sp)
    print("\n  VERDICT          : %s" % verdict)
    print("  ### the verdict reads the LIVE count, not the hit count -- a scope may")
    print("  ### carry excepted hits and still be clean, and that is the whole")
    print("  ### reason the classes are printed rather than filtered silently.")
    return 0 if live == 0 else 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
