# -*- coding: utf-8 -*-
"""b303_pins.py -- THE PINS, ### **BY `ls-remote` ACROSS ALL THREE REPOS.**

### WHY THIS IS A TOOL AND NOT THREE SHELL LINES. ### b301 and b302 recorded their pins by typing
### what `git` printed. ### **THAT IS A SHELL-TYPED NUMBER IN EVERYTHING BUT NAME** -- the
### ahead/behind pair is COMPUTED, and `W-ORD-ADHOC-CHECK-FIXTURES` (b298) is about exactly this
### species. ### So the pair is computed here, by `git rev-list --left-right --count`, and the
### PARSER that reads it carries both polarities.

### ### **WHAT IT DOES NOT DO: ### IT DOES NOT PUSH.** ### It reads. ### A tool that could push
### while reporting the read-back would be reporting its own effect, and the read-back's whole
### value is that it is a SECOND observation of a state a DIFFERENT command produced.

### ### **THE EMPTY-SCOPE LAW (b167, and b299's `G-ADDITIVE` species): ### A REPO THAT DOES NOT
### ### RESOLVE IS REPORTED AS UNRESOLVED AND HARD-FAILS. ### IT IS NEVER SILENTLY 0/0**, because
### an unreachable remote and a synchronised remote print the same reassuring zero otherwise.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPOS = [
    ('relay', r'D:\relay'),
    ('SIDE-global-section', r'D:\SIDE-global-section'),
    ('PLACE-papers', r'D:\MY-DOwnloads\PLACE-papers'),
]


def git(repo, *args):
    """### RETURNS `(rc, stdout)`. ### **stderr IS NOT SWALLOWED INTO stdout** -- a tool that
    reads an error message as data is how a miss becomes a value."""
    p = subprocess.Popen(['git', '-C', repo] + list(args),
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _err = p.communicate()
    return p.returncode, out.decode('utf-8', 'replace').strip()


def parse_left_right(text):
    """### `git rev-list --left-right --count A...B` prints `behind<TAB>ahead`.

    ### **RETURNS `None` ON ANYTHING IT DOES NOT UNDERSTAND**, rather than a pair of zeros --
    ### which is the whole reason this is a function with fixtures instead of a `split()`.
    """
    parts = text.split()
    if len(parts) != 2:
        return None
    try:
        return int(parts[0]), int(parts[1])
    except ValueError:
        return None


def self_test(verbose=True):
    """### **BOTH POLARITIES ON THE PARSER, AND THE NEAR-MISSES ARE THE POINT.**"""
    cases = [
        ('a real pair, tab-separated', '0\t1', (0, 1)),
        ('a real pair, space-separated', '2 3', (2, 3)),
        ('both zero -- the synchronised state', '0\t0', (0, 0)),
        ('### an error message, NOT a pair', 'fatal: bad revision', None),
        ('### empty output -- the silent-zero trap', '', None),
        ('### one number only', '4', None),
        ('### three numbers', '1 2 3', None),
        ('### a non-integer', 'a\tb', None),
    ]
    bad = 0
    if verbose:
        print('  %-46s %-22s %s' % ('parser fixture', 'got/expected', 'agree'))
    for lbl, text, expect in cases:
        got = parse_left_right(text)
        ok = (got == expect)
        bad += 0 if ok else 1
        if verbose:
            print('  %-46s %-22s %s' % (lbl, '%s/%s' % (got, expect),
                                        'YES' if ok else '### NO ###'))
    return bad == 0


def main(argv):
    label = argv[0] if argv else 'PINS'
    print('=' * 100)
    print('b303_pins.py -- %s. ### BY `ls-remote`, ALL THREE REPOS.' % label)
    print('=' * 100)
    ok_suite = self_test()
    print('  parser self-test : %s' % ('PASS' if ok_suite else '### FAIL ###'))
    if not ok_suite:
        print('  ### REFUSING TO REPORT PINS FROM A PARSER THAT FAILS ITS OWN FIXTURES.')
        return 2
    print()

    hard = 0
    for name, path in REPOS:
        print('--- %s   (%s)' % (name, path))
        if not os.path.isdir(os.path.join(path, '.git')):
            print('    ### HARD FAILURE -- NOT A GIT REPOSITORY.')
            hard += 1
            continue
        rc_h, head = git(path, 'rev-parse', 'HEAD')
        rc_r, rem = git(path, 'ls-remote', 'origin', 'refs/heads/main')
        remote_sha = rem.split()[0] if (rc_r == 0 and rem.split()) else None
        print('    local HEAD   : %s' % (head if rc_h == 0 else '### UNRESOLVED'))
        print('    ls-remote    : %s' % (remote_sha or '### UNRESOLVED'))
        if rc_h != 0 or not remote_sha:
            print('    ### HARD FAILURE -- A REPO THAT DOES NOT RESOLVE IS NOT 0/0.')
            hard += 1
            continue
        rc_c, cnt = git(path, 'rev-list', '--left-right', '--count',
                        '%s...HEAD' % remote_sha)
        pair = parse_left_right(cnt) if rc_c == 0 else None
        if pair is None:
            print('    ### HARD FAILURE -- THE AHEAD/BEHIND PAIR DID NOT PARSE: %r' % cnt)
            hard += 1
            continue
        behind, ahead = pair
        print('    behind/ahead : %d / %d' % (behind, ahead))
        print('    equal        : %s' % (head == remote_sha))
        rc_d, dirty = git(path, 'status', '--porcelain')
        untracked = [l for l in dirty.splitlines() if l.startswith('??')]
        tracked = [l for l in dirty.splitlines() if not l.startswith('??')]
        print('    working tree : %d tracked change(s), %d untracked'
              % (len(tracked), len(untracked)))

    print()
    print('  ### REPOS HARD-FAILING : %d' % hard)
    print('  ### **A PIN IS A SHA READ BACK FROM THE REMOTE. ### IT SAYS WHAT IS THERE,')
    print('  ### NOT THAT WHAT IS THERE IS RIGHT.**')
    print('=' * 100)
    return 0 if hard == 0 else 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
