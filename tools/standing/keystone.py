# -*- coding: utf-8 -*-
"""standing/keystone.py -- THE ACT'S OWN TRAIL APPEND EXEMPT FROM THE KEYSTONE-EDITS ARM BY ITS COMMIT (v1.2.0; (R328)(7), b717's event
(9), the class CONTROL). An arm that reads each file an act edited on PLACE-papers main "unchanged since" its edit commit reads, file by
file, the commits that touched it after that commit up to the head read: a file is unchanged where none did, and EXEMPT where every one
of them is among the exempt commits -- the act's own later steps that the order makes write that file (the trail record's append to
OPEN_TRAILS.md), read from the act's step bank by phase, not named in code. Any other commit touching it fails the file. Provenance:
b717's G-KEYSTONE-EDITS read OPEN_TRAILS.md at its C5 commit 84dbbf3e against HEAD, passed pre-push and failed post-push once the
record's step [15] (PLACE-papers c02f47c) appended the trail, as the order makes it.

  touched_after(files, base, head, repo) -> {file: [commits]}
  unchanged_since(files, base, head='HEAD', exempt=(), repo='pp') -> dict(rows [(file, state, commits)], ok)
  exempt_of(act, phases=('record',), repo='pp') -> [commits]     the act's step rows of those phases in the repository
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

NL = '\n'


def touched_after(files, base, head='HEAD', repo='pp'):
    out = {}
    for f in files:
        log = A.gs(repo, 'log', '--format=%H', '%s..%s' % (base, head), '--', f)
        out[f] = [c for c in (log or '').split(NL) if c.strip()]
    return out


def unchanged_since(files, base, head='HEAD', exempt=(), repo='pp'):
    """each file read against the commits that touched it after `base` up to `head`: UNCHANGED (none), EXEMPT (each among `exempt`, full
    or abbreviated hashes) or CHANGED. ok where no file is CHANGED."""
    full = []
    for e in exempt:
        h = A.gs(repo, 'rev-parse', e)
        if h:
            full.append(h)
    rows = []
    for f, cs in touched_after(files, base, head, repo).items():
        state = 'UNCHANGED' if not cs else ('EXEMPT' if all(c in full for c in cs) else 'CHANGED')
        rows.append((f, state, cs))
    return dict(rows=rows, ok=all(s != 'CHANGED' for _f, s, _c in rows), exempt=full)


def exempt_of(act, phases=('record',), repo='pp'):
    """the act's step-bank commits of the phases the order makes write after the edit commit (the trail record's), in the repository."""
    return [r['commit'] for r in A.steps(act) if r.get('repo') == repo and r.get('phase') in phases]
