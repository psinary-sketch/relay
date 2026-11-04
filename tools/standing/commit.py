# -*- coding: utf-8 -*-
"""standing/commit.py -- v1.21.0, (R351)(2)(i), b740 events (1), (2), (4): THE SUBJECT AND THE ROW THAT TRAVEL WITH THEIR COMMIT. One call makes a
gate, lock or seal commit: it composes the subject from the bank (tools/standing/subjects.py), makes the commit and writes its step row, in that
order, with no shell between the subject and the commit (git is run by argument list, so no shell's escape character touches the subject).
Everything that could refuse the row is read before the commit, so a commit and its row never part:
  - the record the subject names must exist: the seal's data/<act>_seal_hashes.json, the lock's data/<act>_lockgate.json;
  - a lock row already in the step bank refuses a second `lock` and a `gate` (the commit after the lock takes `seal`, standing.repeat.one_lock);
  - the composed subject must pass subjects.check(); something must be staged (the add is its own message, one git write per message).
The commit's subject is read back from git and compared with the composed one; the row is written by the record tool's step route.
After a seal commit the post-seal exclude list is printed (tools/standing/hook.py excludes), read before any read ((R351)(2)(iv)).

  python -X utf8 -u tools/standing/commit.py <relay|pp> <gate|lock|seal> [words ...]
"""
import json
import os
import subprocess
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
REPOS = {'relay': RELAY, 'pp': 'D:/MY-DOwnloads/PLACE-papers'}
PHASES = ('gate', 'lock', 'seal')
RECORD = {'seal': '%s_seal_hashes.json', 'lock': '%s_lockgate.json'}
if S not in sys.path:
    sys.path.insert(0, S)

import subjects as SJ   # noqa: E402


class Refused(Exception):
    pass


def _git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')


def reader(data):
    def read(name):
        p = os.path.join(data, name)
        if not os.path.exists(p):
            return None
        with open(p, encoding='utf-8') as f:
            return json.load(f) if name.endswith('.json') else f.read()
    return read


def preflight(act, phase, words, repo, rows, read):
    """the subject, or Refused before anything is written: the phase, the record it names, the step bank's lock row, the subject's check, the index."""
    if phase not in PHASES:
        raise Refused('the phase %r is not one of %s' % (phase, ' | '.join(PHASES)))
    if phase in RECORD and not read(RECORD[phase] % act):
        raise Refused('THE RECORD THE SUBJECT NAMES DOES NOT EXIST: data/%s' % (RECORD[phase] % act))
    if phase in ('lock', 'gate') and any(r.get('phase') == 'lock' for r in rows):
        raise Refused('A LOCK ROW STANDS: the commit after the lock takes phase `seal`, and the seal record must exist first')
    subj = SJ.compose(act, phase, words, read)
    bad = SJ.check(act, phase, subj, read)
    if bad:
        raise Refused('the composed subject faults: %s' % '; '.join(bad))
    if _git(repo, 'diff', '--cached', '--quiet').returncode == 0:
        raise Refused('nothing staged in %s (the add is its own message)' % repo)
    return subj


def commit(repo, subj):
    """the commit by argument list; (full sha, the subject read back)."""
    r = _git(repo, 'commit', '-q', '-m', subj)
    if r.returncode != 0:
        raise Refused('git commit exit %d: %s' % (r.returncode, (r.stderr or r.stdout).strip()[:200]))
    full = _git(repo, 'rev-parse', 'HEAD').stdout.strip()
    back = _git(repo, 'log', '-1', '--format=%s', full).stdout.rstrip('\n')
    return full, back


def record_row(key, phase, full):
    """the row by the record tool's own step route (data/<act>_steps.json, its bank hashes kept by that tool)."""
    r = subprocess.run([sys.executable, '-X', 'utf8', '-u', os.path.join(S, 'fold.py'), 'record', 'step', key, phase, full],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout + r.stderr).strip()


def run(key, phase, words, act=None, data=None, row_writer=None, after_seal=None):
    """one call: preflight, commit, read back, row. Returns a dict of what was done; Refused where nothing was."""
    import act as A
    act = act or A.current()['act']
    data = data or os.path.join(RELAY, 'data')
    repo = REPOS[key] if key in REPOS else key
    read = reader(data)
    rows = (read('%s_steps.json' % act) or {}).get('rows') or []
    subj = preflight(act, phase, words, repo, rows, read)
    full, back = commit(repo, subj)
    rc, out = (row_writer or record_row)(key, phase, full)
    done = dict(act=act, repo=key, phase=phase, commit=full, subject=subj, read_back=back, equal=back == subj, row_exit=rc, row=out,
                rowed=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    if phase == 'seal':
        done['excludes'] = (after_seal or excludes)()
    return done


def excludes():
    r = subprocess.run([sys.executable, '-I', '-X', 'utf8', os.path.join(S, 'hook.py'), 'excludes'], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return (r.stdout or r.stderr).strip()


def main(argv):
    if len(argv) < 2 or argv[0] not in REPOS:
        sys.exit(__doc__)
    try:
        d = run(argv[0], argv[1], ' '.join(argv[2:]))
    except Refused as e:
        sys.exit('### commit.py REFUSED, NOTHING COMMITTED, NO ROW WRITTEN: %s' % e)
    print('  commit %s %s' % (d['repo'], d['commit'][:8]))
    print('  subject   : %s' % d['subject'])
    print('  read back : %s -- %s' % (d['read_back'], 'EQUAL' if d['equal'] else '### NOT EQUAL'))
    print('  row       : %s (exit %d)' % (d['row'], d['row_exit']))
    if 'excludes' in d:
        print(d['excludes'])
    if not d['equal'] or d['row_exit'] != 0:
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
