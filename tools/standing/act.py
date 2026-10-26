# -*- coding: utf-8 -*-
"""standing/act.py -- THE ACT, READ AT RUN TIME: the one source of the standing toolset's act figures, data/act_current.json, and the
readers every standing module shares (the chain, a bank now or at a commit, a root's named banks). No act's figure, name or object stands
here: the act, its neighbours and ranges are read from the file and from data/act_roots.txt at the call.

Extracted, not imported (the author's word (1)(a) of the toolset act): jl, rd, the git reader and the root's banks copied out of the
close's per-act tools and the shared modules they import (provenance: tools/b714_components_standin.py jl and sha; tools/act_root.py
sha256_file; tools/b698_record.py root_banks), with no import of a module whose name carries an act number.
"""
import hashlib
import json
import os
import re
import subprocess

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
# the ruling's PATHS: the repositories the close reads, by the step bank's repository keys
REPOS = dict(relay=RELAY, pp='D:/MY-DOwnloads/PLACE-papers')
NAMES = dict(relay='relay', pp='PLACE-papers')
CHAIN = os.path.join(D, 'act_roots.txt')
ACT_NAME = re.compile(r'^b\d{3}$')


def current():
    """data/act_current.json, read now."""
    with open(os.path.join(D, 'act_current.json'), encoding='utf-8') as f:
        return json.load(f)


def chain():
    """the chain's rows in order, each (act, root, previous root), read from data/act_roots.txt."""
    out = []
    for l in rd_path(CHAIN).split(NL):
        p = l.split()
        if len(p) == 3 and ACT_NAME.match(p[0]):
            out.append(tuple(p))
    return out


def prev_of(act):
    """the act before `act` on the chain, or, for the act not yet appended, the chain's last row's act."""
    acts = [r[0] for r in chain()]
    if act in acts:
        i = acts.index(act)
        return acts[i - 1] if i > 0 else None
    return acts[-1] if acts else None


def git(repo, *args):
    """a git read in a repository by its key, its stdout as bytes (None on a failure)."""
    r = subprocess.run(['git', '-C', REPOS.get(repo, repo)] + list(args), capture_output=True)
    return r.stdout if r.returncode == 0 else None


def gs(repo, *args):
    b = git(repo, *args)
    return None if b is None else b.decode('utf-8', 'replace').replace('\r', '').strip()


def blob(rev, rel, repo='relay'):
    """a file's bytes at a commit (None where the commit does not carry it)."""
    return git(repo, 'show', '%s:%s' % (rev, rel))


def rd_path(p):
    return open(p, encoding='utf-8', errors='replace').read().replace('\r', '') if os.path.isfile(p) else ''


def rd(name, rev=None):
    """a bank's text under relay data/, now or at a commit, CR removed ('' where absent)."""
    if rev is None:
        return rd_path(os.path.join(D, name))
    b = blob(rev, 'data/' + name)
    return '' if b is None else b.decode('utf-8', 'replace').replace('\r', '')


def jl(name, rev=None):
    t = rd(name, rev)
    try:
        return json.loads(t) if t.strip() else {}
    except ValueError:
        return {}


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(p):
    with open(p, 'rb') as f:
        return sha256_bytes(f.read())


def root_named(act):
    """the banks an act's root names, {relay path: sha256}: its root bank's `banks` map, or its `items` rows "data/<name> <sha256>"."""
    rj = jl('%s_act_root.json' % act)
    banks = dict(rj.get('banks') or {})
    for it in rj.get('items') or []:
        p = it.split(' ')
        if len(p) == 2 and p[0].startswith('data/'):
            banks.setdefault(p[0], p[1])
    return banks


def steps(act, rev=None):
    """the act's step bank rows (data/<act>_steps.json `rows`)."""
    return jl('%s_steps.json' % act, rev).get('rows') or []


def step_commit(act, phase, repo='relay'):
    """the last step row's commit of a phase in a repository (None where there is none)."""
    cs = [r['commit'] for r in steps(act) if r.get('phase') == phase and r.get('repo') == repo]
    return cs[-1] if cs else None
