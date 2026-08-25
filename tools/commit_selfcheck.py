# -*- coding: utf-8 -*-
"""commit_selfcheck.py -- THE COMMIT SELF-DESCRIPTION CHECK (built b149).

### WHY THIS EXISTS. At b148 this seat pushed a commit whose message ended
### "The patent package was READ, NEVER WRITTEN, per the deconfliction" -- in the
### same commit that wrote eight patent-package files. ### THE SENTENCE WAS FALSE
### AT THE MOMENT IT WAS WRITTEN, AND NOTHING IN THE CLOSING SEQUENCE COMPARED THE
### MESSAGE AGAINST ITS OWN FILE LIST. A claim of compliance asserted inside the
### act it describes passes every other check the record owns.

### WHAT IT CHECKS, before a push:
###   (1) FOREIGN-SEAT PATHS -- any staged path under a prefix this seat does not
###       own is a hard failure, regardless of what the message says.
###   (2) READ-ONLY CLAIMS -- if the message asserts a tree was read and not
###       written, no staged path may fall under that tree.
###   (3) COMPLIANCE ASSERTIONS -- if the message asserts compliance with a
###       standing ruling, the check's own hit table must be carried in the act
###       record. The tool prints the table; carrying it is the operator's duty
###       and the convention's requirement.

# ### THE LIMIT OF THIS CHECK, STATED IN ITS OWN HEADER BECAUSE A CHECK WHOSE
# ### REACH IS NOT STATED WILL BE TRUSTED BEYOND IT. This compares a MESSAGE to a
# ### FILE LIST against EXPLICIT PATTERNS. ### IT CANNOT READ MEANING. It will
# ### catch "read, never written" beside a written path, and a foreign-seat prefix
# ### in the diff. ### IT WILL NOT CATCH A FALSE COMPLIANCE CLAIM PHRASED IN WORDS
# ### IT DOES NOT KNOW, and it cannot tell a true claim from a lucky one. It
# ### narrows one failure mode; it does not close the class.

Usage:
    python commit_selfcheck.py <repo> [<rev>]     # default: staged (HEAD vs index)
    python commit_selfcheck.py <repo> <rev> --msg-file <path>
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_emit as AE

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Prefixes this (research) seat does not own -- the b147 deconfliction.
FOREIGN = ['phase1.5/method/patent-package/']

# (pattern in the message, the tree it claims is read-only)
READ_ONLY_CLAIMS = [
    (re.compile(r'patent package was READ,?\s*NEVER WRITTEN', re.I), 'phase1.5/method/patent-package/'),
    (re.compile(r'patent package is READ,?\s*never written', re.I), 'phase1.5/method/patent-package/'),
    (re.compile(r'READ,?\s*NEVER WRITTEN', re.I), 'phase1.5/method/patent-package/'),
]

COMPLIANCE = re.compile(r'per the deconfliction|in compliance with|per Rule 4\.1[01]|'
                        r'never written|read-only|untouched by this seat', re.I)


# ### DEFECT FIXED b149, ON THIS CHECK'S OWN FIRST RUN, AND IT IS A PLAIN
# ### CORRECTNESS BUG RATHER THAN A LIMIT. The first version used --name-only,
# ### which lists a DELETED path identically to a WRITTEN one. The b148 CORRECTION
# ### commit -- which `git rm --cached`ed the eight foreign paths, i.e. did the
# ### OPPOSITE of writing them -- came back FAIL. ### A CHECK THAT CANNOT TELL
# ### WRITING FROM UN-WRITING WOULD HAVE CONDEMNED THE REPAIR ALONGSIDE THE
# ### BREACH. Status is now read: only A/M/C/R/T count as writing; D does not.
# ### AND IT FIXES THE QUOTATION PROBLEM AS A SIDE EFFECT: the read-only claim
# ### check compares against WRITES, not against MENTIONS, so a message that
# ### QUOTES a false claim in order to correct it does not itself fail.
WROTE = ('A', 'M', 'C', 'R', 'T')


def files_of(repo, rev):
    """Returns (written, touched). ### ONLY `written` IS EVIDENCE OF A WRITE."""
    args = (['diff', '--cached', '--name-status'] if rev is None
            else ['show', '--name-status', '--format=', rev])
    out = subprocess.run(['git'] + args, cwd=repo, capture_output=True,
                         text=True, encoding='utf-8', errors='replace').stdout
    written, touched = [], []
    for line in out.splitlines():
        parts = [p for p in line.split('\t') if p.strip()]
        if len(parts) < 2:
            continue
        st, path = parts[0].strip(), parts[-1].strip().replace('\\', '/')
        touched.append((st, path))
        if st[:1] in WROTE:
            written.append(path)
    return written, touched


def message_of(repo, rev, msg_file):
    if msg_file:
        return open(msg_file, encoding='utf-8', errors='replace').read()
    if rev is None:
        return ''
    return subprocess.run(['git', 'log', '-1', '--format=%B', rev], cwd=repo,
                          capture_output=True, text=True, encoding='utf-8',
                          errors='replace').stdout


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    repo = argv[0]
    rev = argv[1] if len(argv) > 1 and not argv[1].startswith('--') else None
    msg_file = argv[argv.index('--msg-file') + 1] if '--msg-file' in argv else None

    files, touched = files_of(repo, rev)
    msg = message_of(repo, rev, msg_file)

    print("=" * 76)
    print("COMMIT SELF-DESCRIPTION CHECK (commit_selfcheck.py, b149)")
    print("=" * 76)
    print("  repo            : %s" % repo)
    print("  rev             : %s" % (rev or '(staged)'))
    dels = [p for s, p in touched if s[:1] == 'D']
    print("  paths touched   : %d" % len(touched))
    print("  paths WRITTEN   : %d   ### only these are evidence of a write" % len(files))
    if dels:
        print("  paths DELETED   : %d   ### un-writing is not writing" % len(dels))
    print("  message chars   : %d" % len(msg))

    fails = []

    print("\n  (1) FOREIGN-SEAT PATHS")
    hits = [f for f in files for p in FOREIGN if f.startswith(p)]
    if hits:
        for h in hits:
            print("      ### FOREIGN: %s" % h)
        fails.append("%d foreign-seat path(s) WRITTEN" % len(hits))
    else:
        print("      none  (prefixes checked: %s)" % ", ".join(FOREIGN))

    print("\n  (2) READ-ONLY CLAIMS IN THE MESSAGE vs THE FILE LIST")
    any_claim = False
    for rx, tree in READ_ONLY_CLAIMS:
        m = rx.search(msg)
        if not m:
            continue
        any_claim = True
        viol = [f for f in files if f.startswith(tree)]
        print("      claim found : %r" % m.group(0))
        print("      claims tree : %s" % tree)
        if viol:
            for v in viol:
                print("      ### CONTRADICTED BY: %s" % v)
            fails.append("message claims %r while writing %d path(s) under %s"
                         % (m.group(0), len(viol), tree))
        else:
            print("      consistent  : NO WRITTEN path under that tree")
            print("      ### the claim check compares against WRITES, not mentions,")
            print("      ### so a message QUOTING a false claim to correct it passes.")
    if not any_claim:
        print("      no read-only claim detected in the message")

    print("\n  (3) COMPLIANCE ASSERTION")
    c = COMPLIANCE.search(msg)
    if c:
        print("      assertion found: %r" % c.group(0))
        print("      ### THE CONVENTION REQUIRES THIS HIT TABLE IN THE ACT RECORD.")
        print("      ### A compliance claim that is not accompanied by the check's")
        print("      ### own output is an assertion, not a verification.")
    else:
        print("      none detected")

    verdict = "CLEAN" if not fails else "FAIL"
    if '--emit' in argv:
        i = argv.index('--emit')
        act = argv[i + 1] if i + 1 < len(argv) else 'unknown'
        blk, sp = AE.emit('commit_selfcheck', act, [repo, str(rev or '(staged)')],
                          [('written', len(files)), ('foreign', len(hits)),
                           ('ro-claim', 'yes' if any_claim else 'none'),
                           ('compliance', 'yes' if c else 'none')], verdict)
        print("\n" + blk)
        print("  sidecar written: %s" % sp)
    print("\n  ### VERDICT: %s" % verdict)
    for f in fails:
        print("      - %s" % f)
    print("  ### REACH: explicit patterns only. This cannot read meaning and does")
    print("  ### not close the class -- see the header.")
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
