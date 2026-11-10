# -*- coding: utf-8 -*-
"""standing/wlist.py -- v1.31.0, (R361)(3)(ii), b750 defects (h), (i): THE WRITES OUTSIDE THE (W) LIST REFUSED BEFORE THEY LAND.

b750's seat wrote a tracked tool outside the act's (W) list twice in Component 1 (tools/standing/deletes.py by the Write tool, tools/act_close.py
by the Edit tool), each found and restored before any commit, neither refused. The (W) list is regenerated into a bank, and the hook
(tools/standing/hook.py, kind WLIST) reads that bank and refuses a Write or Edit of a TRACKED path the list does not cover, before it lands.
A path tracked by no repository (the scratch directory, the seat's memory, a new untracked bank) is not a write the list governs.

THE LIST, REGENERATED (the bank data/<act>_wlist.json, written by `wlist.py bank`):
  the face's (W) table where the face stands (data/<act>_face.txt, else tools/<act>_face_blocks.txt), read by tools/act_close.py w_patterns;
  before the face, the act's standing kinds: relay data/<act>_*, tools/<act>_*, tools/acts/<act>.py, tools/standing/*, data/act_current.json,
  data/act_roots.txt, data/b675_corrigenda.txt, data/<next>_rules.txt, tools/mirror_prevbuild.json, the previous act's closing push capture
  (data/<prev>_*_push_out.txt), PLACE-papers FINDINGS.md and OPEN_TRAILS.md, and the worklist's PP_EDITED;
  in both, the ruling's clause-ordered files with the amendment rows (tools/standing/amend.py writes) and the files written after the lock by
  design (standing.act.by_design).
The bank carries the sha256 of every source it read (or ABSENT); the hook refuses on a stale bank (a source changed since) as on an absent one,
so the list it reads is the list as regenerated, never an older one.

  python -X utf8 -u tools/standing/wlist.py bank [<act>]      regenerate, print and write data/<act>_wlist.json
  python -X utf8 -u tools/standing/wlist.py show [<act>]      regenerate and print, nothing written
  patterns(act) -> (patterns, source, sources)   fault(path, act=None) -> None or the refusal's detail   repo_of(path) -> (name, top, rel) or None
"""
import fnmatch
import hashlib
import io
import json
import os
import subprocess
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
for p_ in (S, T):
    if p_ not in sys.path:
        sys.path.insert(0, p_)


def _cur():
    with io.open(os.path.join(D, 'act_current.json'), encoding='utf-8') as f:
        return json.load(f)


def _sha(p):
    if p.endswith('#PP_EDITED'):   # ### the worklist read for its PP_EDITED alone: its other constants move through the act and change no row
        act = os.path.basename(p).split('_worklist.py')[0]
        return hashlib.sha256(repr(_worklist_pp(act)).encode('utf-8')).hexdigest() if os.path.isfile(p[:-len('#PP_EDITED')]) else 'ABSENT'
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read().replace(b'\r\n', b'\n')).hexdigest()
    except OSError:
        return 'ABSENT'


def source_paths(act):
    """the files the regeneration reads, relay-relative, each read for its digest."""
    return ['data/%s_ferry.txt' % act, 'data/%s_amendments.json' % act, 'tools/%s_worklist.py#PP_EDITED' % act, 'data/%s_face.txt' % act,
            'tools/%s_face_blocks.txt' % act]


def _worklist_pp(act):
    p = os.path.join(T, '%s_worklist.py' % act)
    if not os.path.isfile(p):
        return ()
    import carry as CA
    try:
        return tuple(CA.literals(io.open(p, encoding='utf-8').read()).get('PP_EDITED') or ())
    except SyntaxError:
        return ()


def kinds(act, prev, nxt):
    """the act's standing kinds, before the face (the rows every face of b737-b750 carried for these files)."""
    out = ['relay/data/%s_*' % act, 'relay/tools/%s_*' % act, 'relay/tools/acts/%s.py' % act, 'relay/tools/standing/*', 'relay/data/act_current.json',
           'relay/data/act_roots.txt', 'relay/data/b675_corrigenda.txt', 'relay/data/%s_rules.txt' % nxt, 'relay/tools/mirror_prevbuild.json',
           'relay/data/%s_*_push_out.txt' % prev, 'PLACE-papers/FINDINGS.md', 'PLACE-papers/OPEN_TRAILS.md']
    for p in _worklist_pp(act):
        if 'PLACE-papers/%s' % p not in out:
            out.append('PLACE-papers/%s' % p)
    return out


def patterns(act=None):
    """(patterns, source, sources): source 'face' (the face's (W) table) or 'kinds' (before the face)."""
    cur = _cur()
    act = act or cur['act']
    prev, nxt = cur.get('prev') or '', cur.get('next') or ''
    import act_close as AC
    import amend as AM
    import act as A_
    face = ''
    src = 'kinds'
    for rel in ('data/%s_face.txt' % act, 'tools/%s_face_blocks.txt' % act):
        p = os.path.join(RELAY, *rel.split('/'))
        if os.path.isfile(p):
            face = io.open(p, encoding='utf-8').read()
            if AC.w_patterns(face):
                src = 'face (%s)' % rel
                break
    pats = list(AC.w_patterns(face)) if src != 'kinds' else kinds(act, prev, nxt)
    fp = os.path.join(D, '%s_ferry.txt' % act)
    ruling = io.open(fp, encoding='utf-8').read() if os.path.isfile(fp) else ''
    for w in AM.writes(ruling, AM.rows_of(act)):
        repo, rel = AM._split(w)
        q = '%s/%s' % (repo, rel)
        if q not in pats:
            pats.append(q)
    for b in A_.by_design(act):
        q = 'relay/%s' % b
        if q not in pats:
            pats.append(q)
    sources = dict((rel, _sha(os.path.join(RELAY, *rel.split('/')))) for rel in source_paths(act))
    return pats, src, sources


def bank_path(act):
    return os.path.join(D, '%s_wlist.json' % act)


def regenerate(act=None, write=False):
    act = act or _cur()['act']
    pats, src, sources = patterns(act)
    L = ['%s -- (R361)(3)(ii): THE (W) LIST REGENERATED FOR THE HOOK (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
         '  the source: %s ; patterns %d' % (src, len(pats))] + ['  %s' % p for p in pats] + \
        ['  the sources read (sha256 of the LF bytes, or ABSENT):'] + ['    %s %s' % (k, v[:16]) for k, v in sources.items()]
    if write:
        j = dict(act=act, at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), source=src, patterns=pats, sources=sources)
        p = bank_path(act)
        with open(p + '.tmp', 'wb') as f:
            f.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        L.append('  written data/%s_wlist.json' % act)
    return L


def _git(top, *a):
    return subprocess.run(['git', '-C', top] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')


def repo_of(path):
    """(repository name, its top, the path relative to it) for a path inside a git working tree, or None. The name is the top's base name
    (relay, PLACE-papers, SIDE-...), the form of the (W) table's backticked paths."""
    p = os.path.abspath(path or '')
    d = os.path.dirname(p)
    while d and not os.path.isdir(d):
        nd = os.path.dirname(d)
        if nd == d:
            return None
        d = nd
    if not d:
        return None
    r = _git(d, 'rev-parse', '--show-toplevel')
    if r.returncode != 0 or not r.stdout.strip():
        return None
    top = os.path.abspath(r.stdout.strip())
    try:
        rel = os.path.relpath(p, top).replace(os.sep, '/')
    except ValueError:
        return None
    if rel.startswith('..'):
        return None
    return os.path.basename(top), top, rel


def allows(repo, rel, pats):
    q = '%s/%s' % (repo, rel)
    return any(fnmatch.fnmatchcase(q, x) for x in pats)


def fault(path, act=None, bank=None):
    """None where the write is allowed; else the refusal's detail. Allowed: a path in no repository, a path its repository does not track,
    a tracked path the regenerated list covers. Refused: a tracked path outside the list; any tracked path while the bank is absent or stale."""
    ro = repo_of(path)
    if ro is None:
        return None
    repo, top, rel = ro
    if _git(top, 'ls-files', '--error-unmatch', '--', rel).returncode != 0:
        return None
    act = act or _cur()['act']
    if bank is None:
        try:
            with io.open(bank_path(act), encoding='utf-8') as f:
                bank = json.load(f)
        except (OSError, ValueError):
            return 'the (W) bank data/%s_wlist.json is absent or unreadable; %s/%s is tracked -- regenerate the list first (python -X utf8 -u tools/standing/wlist.py bank)' % (act, repo, rel)
        stale = [k for k, v in (bank.get('sources') or {}).items() if _sha(os.path.join(RELAY, *k.split('/'))) != v]
        if stale:
            return 'the (W) bank data/%s_wlist.json is stale (%s changed since it was written) -- regenerate the list (python -X utf8 -u tools/standing/wlist.py bank)' % (act, ', '.join(stale))
    if allows(repo, rel, bank.get('patterns') or ()):
        return None
    return 'a write of %s/%s, a tracked path outside the act`s (W) list (data/%s_wlist.json, %s)' % (repo, rel, act, bank.get('source'))


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    a = sys.argv[1:]
    if not a or a[0] not in ('bank', 'show'):
        sys.exit(__doc__)
    print(NL.join(regenerate(a[1] if len(a) > 1 else None, write=(a[0] == 'bank'))))
