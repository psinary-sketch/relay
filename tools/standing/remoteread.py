# -*- coding: utf-8 -*-
"""standing/remoteread.py -- v1.33.0, (R363)(7)(ix), b752 events (13): A REMOTE READ THAT FAILS IS NOT AN EMPTY ANSWER.

g() of tools/b698_record.py (:91-:92, sealed and unedited) returns git's output alone and drops its exit code and its error text, so the root
route's ls-remote (:1272), failing, reads as no head and prints HEAD NOT THE REMOTE MAIN (tools/standing/repeat.py :272-:274), as at b752's
root at about 06:19Z. The reader here keeps both: a remote read (ls-remote, fetch) that exits non-zero prints FAILED with the exit code and the
error text, apart from a head that differs, and the route stops; its one retry, run by the seat, is an event. Every other git call returns
its output as b698's g() did. rebind(R) replaces R.g; b698's own is kept as R._g_output_only.

  read(repo, *args) -> (stdout, code, stderr)
  python -X utf8 -u tools/standing/remoteread.py control      a read against a remote name that does not resolve, printing FAILED
"""
import subprocess
import sys

REMOTE = ('ls-remote', 'fetch')


class RemoteReadFailed(SystemExit):
    pass


def read(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout, r.returncode, (r.stderr or '').strip()


def g(repo, *a):
    out, code, err = read(repo, *a)
    if code and a and a[0] in REMOTE:
        raise RemoteReadFailed('### FAILED: git -C %s %s -- exit %d: %s ((R363)(7)(ix): a failed remote read, not an empty answer; the route stops, '
                               'its one retry an event)' % (repo, ' '.join(a), code, err[:300] or '(no error text)'))
    return out


def rebind(R):
    if not hasattr(R, '_g_output_only'):
        R._g_output_only = R.g
        R.g = g
    return R


def control(repo='D:/relay'):
    """(ok, lines): b698's g() and this g() over `ls-remote <a remote name that does not resolve>`: the old reads '' (no head), the new FAILED."""
    bad = 'no-such-remote-b753'
    old = subprocess.run(['git', '-C', repo, 'ls-remote', bad, 'refs/heads/main'], capture_output=True, text=True).stdout
    try:
        g(repo, 'ls-remote', bad, 'refs/heads/main')
        new = None
    except RemoteReadFailed as e:
        new = str(e)
    local = g(repo, 'rev-parse', '--short=8', 'HEAD').strip()
    ok = old == '' and bool(new) and new.startswith('### FAILED') and len(local) == 8
    return ok, ['### (remote) ls-remote against `%s`: b698`s g() returns %r (read as no head) ; the kept reader: %s ; a local read unchanged: %s ; THE CONTROL %s' % (
        bad, old, (new or '### NO FAILURE')[:200], local, 'AS WANTED' if ok else 'NOT AS WANTED')]


if __name__ == '__main__':
    if sys.argv[1:2] == ['control']:
        ok, L = control()
        print('\n'.join(L))
        sys.exit(0 if ok else 1)
    sys.exit(__doc__)
