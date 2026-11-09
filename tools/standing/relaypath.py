# -*- coding: utf-8 -*-
"""standing/relaypath.py -- THE RECORD'S READERS TAKE A RELAY PATH ONCE (v1.27.0, (R357)(3)(vii), b746 defect (p)).

b746's N2 score route read rdn('data/b746_section1.txt'); rdn joined data/ to a name already carrying it and read '' from no file, so the
score's dry form printed "[S1] passed: False" over a bank holding [S1] PASS. Here each reader joins its root once and refuses a path that
resolves to no file, printing the name and the path; a read that may find no file says so at its call (optional=True) and reads ''.

  rdn(name, optional=False)  a bank's name under data/, joined once: rdn('data/x.txt') resolves to data/data/x.txt and is REFUSED
  rdp(rel, optional=False)   a relay-relative path ('data/...', 'tools/...'), joined once to the relay root
  rd(path, optional=False)   an absolute path as it stands
"""
import io
import os

RELAY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(RELAY, 'data')


def refuse(name, path):
    raise SystemExit('### REFUSED: %s resolves to no file (%s) -- the record reads no bank that is not there (v1.27.0, (R357)(3)(vii))' % (name, path))


def _read(name, path, optional):
    if not os.path.isfile(path):
        if optional:
            return ''
        refuse(name, path)
    return io.open(path, encoding='utf-8').read().replace(chr(13), '')


def rd(path, optional=False):
    return _read(path, path, optional)


def rdn(name, optional=False):
    return _read(name, os.path.join(D, name), optional)


def rdp(rel, optional=False):
    return _read(rel, os.path.join(RELAY, rel), optional)


# ================================================================================ v1.29.0, (R359)(3)(iv), b748 defect (j)
# ### b748's line bank read the cluster table by `git grep` of PLACE-papers CLUSTERS.md, a file that does not exist, and printed NONE for
# ### "a row naming the instance" -- a vacuous read. Every reader of the record over a repository file goes through these two, which refuse
# ### a path the repository does not hold and print the path, the rows read and their count.
import subprocess  # noqa: E402


def tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', '--', rel], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode == 0


def rows_of(repo, rel, lo=None, hi=None, out=None):
    """the lines lo..hi (1-based, inclusive) of a file the repository tracks, read from the working tree; REFUSED (SystemExit) where the
    file is not tracked or not on disk; the path, the range and the row count printed (into `out`, a list, where given)."""
    path = os.path.join(repo, rel)
    if not tracked(repo, rel) or not os.path.isfile(path):
        refuse('%s in %s' % (rel, repo), path)
    L = io.open(path, encoding='utf-8').read().replace(chr(13), '').split('\n')
    a, b = (lo or 1), (hi or len(L))
    got = L[a - 1:b]
    msg = '  READ %s :%d-:%d of %s, %d rows' % (rel, a, a + len(got) - 1, repo, len(got))
    (out.append(msg) if out is not None else print(msg))
    return got


def grep_of(repo, rel, needle, out=None):
    """[(line number, text)] of the rows of a tracked file carrying `needle` (a plain string); REFUSED where the file is not tracked -- a
    grep of a file that is not there reads NONE and says nothing. The path and the count of rows matched beside the file's row count printed."""
    L = rows_of(repo, rel, out=[])
    hits = [(i, l) for i, l in enumerate(L, 1) if needle in l]
    msg = '  GREP %s in %s for %r: %d of %d rows' % (rel, repo, needle, len(hits), len(L))
    (out.append(msg) if out is not None else print(msg))
    return hits
