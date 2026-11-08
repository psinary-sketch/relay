# -*- coding: utf-8 -*-
"""standing/lockdate.py -- v1.26.0, (R356)(3)(ii), b745 events, N4: THE ONE READER OF THE LOCK DATE.

b745 read its lock twice: N4 dated the lock by the face's `locked at (UTC)` line (written after the lock commit, so it found the seal commit
2959bc55 as the first commit carrying the face at or after that time), while the root prompt's ceiling was given af0330bb by hand. One date,
two readings. Here there is one: the lock commit's hash as the record tool's step route wrote it, the `lock` row of data/<act>_steps.json, and
its commit time from git. N4 (the act module's _post_lock_edits) and the ceiling (rootprompt.ceiling_at_lock) both call lock_commit().

  lock_commit(rows, repo='relay') -> full sha or None    the relay lock row's commit; None where no lock row stands; Refused-like ValueError
                                                          where two lock rows stand (standing.repeat.one_lock)
  lock_of(act, data) -> full sha or None                 the same, read from data/<act>_steps.json
  lock_epoch(sha, root) -> int                           the commit's committer time from git
  tracked_at(sha, root, prefix) -> [paths]               the paths tracked at the lock commit under a prefix (the ceiling's tracked_at_lock)

  python -X utf8 -u tools/standing/lockdate.py <act>     prints the act's lock commit and its time
"""
import json
import os
import subprocess
import sys

S = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(os.path.dirname(S))


def lock_commit(rows, repo='relay'):
    hs = [r.get('commit') for r in (rows or []) if r.get('phase') == 'lock' and r.get('repo', 'relay') == repo]
    if len(hs) > 1:
        raise ValueError('TWO LOCK ROWS STAND in the step bank: %s' % [h[:8] for h in hs])
    return hs[0] if hs else None


def lock_of(act, data=None):
    p = os.path.join(data or os.path.join(RELAY, 'data'), '%s_steps.json' % act)
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8') as f:
        return lock_commit((json.load(f) or {}).get('rows') or [])


def _g(root, *a):
    return subprocess.run(['git', '-C', root] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def lock_epoch(sha, root=RELAY):
    out = _g(root, 'log', '-1', '--format=%ct', sha).strip()
    return int(out) if out.isdigit() else None


def tracked_at(sha, root=RELAY, prefix=''):
    return [x for x in _g(root, 'ls-tree', '-r', '--name-only', sha).split('\n') if x.strip() and x.startswith(prefix)]


def main(argv):
    if not argv:
        sys.exit(__doc__)
    h = lock_of(argv[0])
    print('  %s lock commit (data/%s_steps.json, the lock row): %s ; committed %s' % (argv[0], argv[0], h or 'NONE', lock_epoch(h) if h else '-'))


if __name__ == '__main__':
    main(sys.argv[1:])
