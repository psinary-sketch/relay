# -*- coding: utf-8 -*-
"""standing/pushcheck.py -- v1.23.0, (R353)(3)(iii), b742 events (4): THE PUSH TOOL REFUSES AT ITSELF WHEN ITS BRANCH OR ITS STEP ROW IS ABSENT.

b742 sent `tools/push_gated.sh /d/relay push-b742-preroot` at 22:01:12Z before the step rows' commit and before the branch was made; the script
went on to `git rev-parse refs/heads/push-b742-preroot` and git refused ("ambiguous argument"), exit 128 at the ref -- a refusal by accident of the
order of its lines, with the step rows still uncommitted. tools/push_gated.sh now calls this check after its push-*|repair-* test and before it
reads any ref; a refusal exits 13 with nothing checked out and nothing pushed:
  - the branch must stand in the repository (refs/heads/<branch>);
  - the relay's step bank for the act (data/<act>_steps.json) must be tracked and carry no change against the relay's HEAD (the row committed
    before the push, b741's order: the steps committed, the branch made, then the push).

  python -X utf8 tools/standing/pushcheck.py <repo> <branch> [act]     exit 0 CLEAR, 13 REFUSED (one line naming each fault)
"""
import os
import subprocess
import sys

S = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(os.path.dirname(S))
ACT_REPOS = tuple(os.path.normcase(os.path.abspath(p)) for p in (RELAY, 'D:/MY-DOwnloads/PLACE-papers'))


def _git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')


def faults(repo, branch, act, relay=RELAY):
    out = []
    if _git(repo, 'rev-parse', '-q', '--verify', 'refs/heads/%s' % branch).returncode != 0:
        out.append('THE BRANCH %s IS NOT IN %s (make it after the step rows are committed)' % (branch, repo))
    steps = 'data/%s_steps.json' % act
    top = os.path.normcase(os.path.abspath(_git(repo, 'rev-parse', '--show-toplevel').stdout.strip() or repo))
    if top not in ACT_REPOS:
        return out   # a fixture repository (tools/test_push_gated.sh's temporary clones): the branch read, no act's step bank stands for it
    if _git(relay, 'ls-files', '--error-unmatch', steps).returncode != 0:
        out.append('THE STEP BANK %s IS NOT TRACKED IN THE RELAY' % steps)
    elif _git(relay, 'diff', '--quiet', 'HEAD', '--', steps).returncode != 0:
        out.append('THE STEP BANK %s CARRIES AN UNCOMMITTED ROW (commit the step rows before the push)' % steps)
    if top == os.path.normcase(os.path.abspath(relay)):   # ### v1.24.0, (R354)(2)(iv)
        for p in rewritten(relay, act, 'refs/remotes/origin/main', 'refs/heads/%s' % branch):
            out.append('A PUSHED BANK REWRITTEN: %s differs from its pushed form other than by an append (write the corrected form to a new bank at a '
                       'suffixed path, data/%s_2.txt, with a dated note naming the pushed one)' % (p, p[5:-4]))
    return out


def rewritten(repo, act, base, head):
    """v1.24.0, (R354)(2)(iv), b743 events (15): the act's text banks (data/<act>_*.txt) present at `base` (the remote's main as last pushed) whose
    form at `head` is not the pushed form with lines appended -- a pushed bank is never rewritten. The banks appended by design after the lock
    (standing.act.post_lock_appended) are read apart. A base or head that does not resolve reads nothing."""
    if _git(repo, 'rev-parse', '-q', '--verify', base).returncode != 0 or _git(repo, 'rev-parse', '-q', '--verify', head).returncode != 0:
        return []
    try:
        if S not in sys.path:
            sys.path.insert(0, S)
        import act as A
        apart = set(A.post_lock_appended(act))
    except Exception:  # noqa: BLE001
        apart = set()
    out = []
    for l in _git(repo, 'diff', '--name-status', base, head, '--', 'data/%s_*.txt' % act).stdout.split('\n'):
        x = l.split('\t')
        if len(x) < 2 or x[0][:1] not in ('M', 'D') or x[1] in apart:
            continue
        old = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (base, x[1])], capture_output=True).stdout.replace(b'\r', b'')
        new = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (head, x[1])], capture_output=True).stdout.replace(b'\r', b'')
        if x[0][:1] == 'D' or not new.startswith(old):
            out.append(x[1])
    return out


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    act = argv[2] if len(argv) > 2 else None
    if not act:
        sys.path.insert(0, S)
        import act as A
        act = A.current()['act']
    bad = faults(argv[0], argv[1], act)
    if bad:
        for b in bad:
            print('push_gated: REFUSED AT THE TOOL -- %s. NOTHING IS PUSHED' % b, file=sys.stderr)
        sys.exit(13)
    print('push_gated: pushcheck CLEAR -- branch %s stands; %s committed' % (argv[1], 'data/%s_steps.json' % act))


if __name__ == '__main__':
    main(sys.argv[1:])
