# -*- coding: utf-8 -*-
"""standing/scratchfsck.py -- v1.16.0, (R346)(3)(iv), b735 defect (p): THE SCRATCH CLONE'S FSCK. The clone zqwork lost its .git/objects/pack directory between two dispatches and the loss was found by a failing command,
its cause not established. The rule: a scratch clone's fsck is read before and after every dispatch read, printed; a row carrying a clone and not both reads is refused by standing.dispatchrows.

  read(clone)    (ok, the one line printed), by `git fsck --connectivity-only`, a read
"""
import subprocess


def read(clone):
    r = subprocess.run(['git', '-C', clone, 'fsck', '--connectivity-only', '--no-progress'], capture_output=True, text=True, encoding='utf-8', errors='replace')
    bad = [l for l in (r.stdout + r.stderr).split('\n') if l.strip() and not l.startswith(('dangling', 'notice', 'Checking', 'Verifying'))]
    ok = r.returncode == 0 and not bad
    return ok, 'fsck %s exit %d%s' % (clone.rstrip('/').split('/')[-1], r.returncode, '' if ok else ' ; %s' % (bad[:1] or ['']))
