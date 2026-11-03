# -*- coding: utf-8 -*-
"""standing/scratchfsck.py -- v1.16.0, (R346)(3)(iv), b735 defect (p): THE SCRATCH CLONE'S FSCK. The clone zqwork lost its .git/objects/pack directory between two dispatches and the loss was found by a failing command,
its cause not established. The rule: a scratch clone's fsck is read before and after every dispatch read, printed; a row carrying a clone and not both reads is refused by standing.dispatchrows.

  read(clone)    (ok, the one line printed), by `git fsck --connectivity-only`, a read

### v1.17.0, (R347)(2)(iv), b736 defect (m): THE PACK LOSS TWICE, CAUSE NOT ESTABLISHED. Beside the fsck, the disk's free space and the process
### listing, so the cause has a place to show: snapshot(clone) before and after every dispatch read and every clone operation, printed;
### standing.dispatchrows refuses a row naming a clone without both snapshots.
  snapshot(clone) dict(at, fsck_ok, fsck, disk_free_mb, procs), a read; nothing written
  line(snap)      the snapshot's one printed line
"""
import shutil
import subprocess
import time

PROC_NAMES = ('git', 'python', 'lean', 'lake', 'claude', 'node')


def read(clone):
    r = subprocess.run(['git', '-C', clone, 'fsck', '--connectivity-only', '--no-progress'], capture_output=True, text=True, encoding='utf-8', errors='replace')
    bad = [l for l in (r.stdout + r.stderr).split('\n') if l.strip() and not l.startswith(('dangling', 'notice', 'Checking', 'Verifying'))]
    ok = r.returncode == 0 and not bad
    return ok, 'fsck %s exit %d%s' % (clone.rstrip('/').split('/')[-1], r.returncode, '' if ok else ' ; %s' % (bad[:1] or ['']))


def procs():
    """the process counts by image name (tasklist's CSV, no shell filter), the names PROC_NAMES; {} where tasklist does not answer."""
    try:
        r = subprocess.run(['tasklist', '/FO', 'CSV', '/NH'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30)
    except (OSError, subprocess.SubprocessError):
        return {}
    out = dict((k, 0) for k in PROC_NAMES)
    for l in r.stdout.split('\n'):
        nm = l.split('","')[0].strip('"').lower()
        base = nm[:-4] if nm.endswith('.exe') else nm
        if base in out:
            out[base] += 1
    return out


def snapshot(clone):
    ok, ln = read(clone)
    try:
        free = shutil.disk_usage(clone).free // (1024 * 1024)
    except OSError:
        free = None
    return dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), fsck_ok=ok, fsck=ln, disk_free_mb=free, procs=procs())


def line(snap):
    return '%s ; %s ; disk free %s MB ; procs %s' % (snap.get('at'), snap.get('fsck'), snap.get('disk_free_mb'),
                                                     ' '.join('%s %d' % kv for kv in sorted((snap.get('procs') or {}).items())) or 'NOT READ')
