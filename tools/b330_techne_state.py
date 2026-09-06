# -*- coding: utf-8 -*-
"""b330_techne_state.py -- THE TWO TECHNE CLONES AND THE AUGUST FILES, READ AND HASHED; NOTHING RESOLVED.

### ### `--snapshot` (before the seal): both clones' HEAD, branch and remote tip by ls-remote; the untracked
### status of `modules/`; the sha256 of every August file. ### `--verify` (after the writes and the local
### commit): the August files byte-identical to the snapshot; the remote tip UNCHANGED (nothing pushed);
### the second clone's HEAD unchanged; the canonical clone's HEAD read back. ### The divergence is READ,
### neither reconciled nor described as resolved.
"""
import hashlib
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
A = r'D:\MY-DOwnloads\TECHNE-Core'
B = r'D:\MY-DOwnloads\TECHNE_Core'
AUG = os.path.join(A, 'modules', '2026-08')
SNAP = os.path.join(D, 'b330_techne_state.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def git(repo, *args):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True).stdout.decode('utf-8', 'replace').strip()


def sha(path):
    return hashlib.sha256(io.open(path, 'rb').read()).hexdigest()


def state():
    aug = {n: sha(os.path.join(AUG, n)) for n in sorted(os.listdir(AUG))}
    return {
        'A': {'path': A, 'head': git(A, 'rev-parse', '--short', 'HEAD'), 'branch': git(A, 'branch', '--show-current'),
              'remote': git(A, 'remote', 'get-url', 'origin'), 'remote_main': git(A, 'ls-remote', 'origin', 'main')[:7],
              'status': git(A, 'status', '--porcelain')},
        'B': {'path': B, 'head': git(B, 'rev-parse', '--short', 'HEAD'), 'branch': git(B, 'branch', '--show-current'),
              'remote_main': git(B, 'ls-remote', 'origin', 'main')[:7]},
        'august': aug,
    }


def main(argv):
    print('=' * 100)
    print('b330 -- THE TWO TECHNE CLONES, READ. ### %s' % ('SNAPSHOT (before the seal)' if '--verify' not in argv else 'VERIFY (after the writes)'))
    print('=' * 100)
    s = state()
    for k in ('A', 'B'):
        print('  clone %s : %s  HEAD %s  branch %s  origin/main %s' % (k, s[k]['path'], s[k]['head'], s[k]['branch'], s[k]['remote_main']))
    print('  clone A status : %r' % s['A']['status'])
    print('  August files hashed : %d' % len(s['august']))
    if '--verify' not in argv:
        io.open(SNAP, 'w', encoding='utf-8', newline='\n').write(json.dumps(s, indent=1) + '\n')
        print('  snapshot written : %s' % os.path.basename(SNAP))
        print('  ### THE DIVERGENCE (A %s vs B %s, one remote %s) IS READ AND NOT RESOLVED.' % (s['A']['head'], s['B']['head'], s['A']['remote_main']))
        print('=' * 100)
        return 0
    snap = json.load(io.open(SNAP, encoding='utf-8'))
    aug_ok = snap['august'] == s['august']
    remote_ok = snap['A']['remote_main'] == s['A']['remote_main'] == snap['B']['remote_main'] == s['B']['remote_main']
    b_ok = snap['B']['head'] == s['B']['head']
    ahead = git(A, 'rev-list', '--count', 'origin/main..HEAD')
    print('  August files byte-identical to the snapshot : %s' % aug_ok)
    print('  remote tip unchanged (NOTHING PUSHED)        : %s  (%s)' % (remote_ok, s['A']['remote_main']))
    print('  second clone untouched                       : %s  (%s)' % (b_ok, s['B']['head']))
    print('  canonical clone HEAD now %s, ahead of origin/main by %s commit(s)  ### LOCAL, NOT PUSHED' % (s['A']['head'], ahead))
    print('=' * 100)
    return 0 if (aug_ok and remote_ok and b_ok) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
