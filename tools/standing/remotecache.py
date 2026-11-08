# -*- coding: utf-8 -*-
"""standing/remotecache.py -- v1.22.0, (R352)(2)(ii), b741 event (4): ONE REMOTE READ PER REPOSITORY PER SUITE RUN, CACHED ACROSS ITS PARTS, EACH READ TIMED.

b741's post-push part standing-b2c ran its act-root chain phase 1970 s against the pre-push run's 183 s (data/b741_checks_standing-b2c.txt :5;
the slow run's table in session 352ad3f4's transcript, its own bank overwritten by the re-run). Each part is its own process and read every
repository's remote again (tools/b616_claims.py remote_refs caches within one process only): 38 repositories in each of ten parts, and no
read's time was recorded, so a slow read could not be named. The repair: the first part of a suite run reads each repository once and banks
the refs in a run cache outside data/ and tools/; every later part of the same run reads the cache. Every read made is timed.

  run_key(act, mode, repos)   the suite run's key: the act, the mode (run, prerun, mid, probe, seal) and, for each repository named, its
                              HEAD and a digest of its remote-tracking refs (a push moves them, so the post-push run never reads the pre-push
                              run's cache)
  wrap(reader, key, log)      a remote_refs in place of `reader`: a repository in the run cache is read from it (no remote read), any other
                              is read by `reader`, timed and added; log[path] = dict(reads, secs, cached, at)
  summary(log)                (repositories, reads made, cached, seconds summed, the slowest (path, secs))
A cache older than MAX_AGE seconds is not read; a failed read (no refs/heads/) is not cached.
"""
import hashlib
import json
import os
import subprocess
import tempfile
import time

DIR = os.path.join(tempfile.gettempdir(), 'relay_remote_cache')
MAX_AGE = 4 * 3600


def _utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _rev(repo, ref):
    r = subprocess.run(['git', '-C', repo, 'rev-parse', '--verify', '-q', ref], capture_output=True, text=True)
    return (r.stdout.strip() or '-')[:12]


def _remotes(repo):
    """a digest of every remote-tracking ref the clone holds: a push to any branch moves it."""
    r = subprocess.run(['git', '-C', repo, 'for-each-ref', '--format=%(refname) %(objectname)', 'refs/remotes/origin'], capture_output=True, text=True)
    return hashlib.sha256(r.stdout.encode('utf-8')).hexdigest()[:10]


def run_key(act, mode, repos):
    return '%s_%s_%s' % (act, mode, hashlib.sha256('|'.join('%s %s %s' % (p, _rev(p, 'HEAD'), _remotes(p)) for p in repos).encode('utf-8')).hexdigest()[:16])


def _path(key):
    return os.path.join(DIR, key.replace('/', '_').replace(':', '_') + '.json')


def _load(key):
    p = _path(key)
    if not os.path.exists(p):
        return {}
    try:
        with open(p, encoding='utf-8') as f:
            j = json.load(f)
    except (OSError, ValueError):
        return {}
    return j if time.time() - j.get('_epoch', 0) <= MAX_AGE else {}


def _save(key, j):
    os.makedirs(DIR, exist_ok=True)
    p = _path(key)
    j.setdefault('_epoch', time.time())
    with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        json.dump(j, f)
    os.replace(p + '.tmp', p)


def wrap(reader, key, log):
    memo = {}

    def remote_refs(path):
        if path in memo:
            return memo[path]
        c = _load(key)
        if path in c and isinstance(c[path], dict) and c[path].get('refs'):
            log[path] = dict(reads=0, secs=0.0, cached=True, at=c[path].get('at'))
            memo[path] = c[path]['refs']
            return memo[path]
        t0 = time.time()
        refs = reader(path)
        dt = round(time.time() - t0, 2)
        log[path] = dict(reads=1, secs=dt, cached=False, at=_utc())
        att = (getattr(reader, 'attempts', None) or {}).get(path)   # ### v1.26.0, (R356)(3)(v): a retried read's two timings
        if att:
            log[path]['attempts'] = list(att)
        memo[path] = refs
        if any(k.startswith('refs/heads/') for k in refs):
            c = _load(key)
            c[path] = dict(refs=refs, at=_utc(), secs=dt)
            _save(key, c)
        return refs
    return remote_refs


def summary(log):
    made = [(p, v['secs']) for p, v in log.items() if not v.get('cached')]
    slow = max(made, key=lambda x: x[1]) if made else ('-', 0.0)
    return len(log), len(made), sum(1 for v in log.values() if v.get('cached')), round(sum(s for _p, s in made), 1), slow
