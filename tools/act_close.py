# -*- coding: utf-8 -*-
"""act_close.py -- THE CLOSE'S SHARED FUNCTIONS, standing clauses v4 rows (62)-(68) ((R323)(4)), a shared tool from b713.

### Each function answers one repair of (R323)(4), and every tool that reads the object imports it from here and keeps no form of its own:
###   (i)   w_patterns, w_allows  -- ONE LIST OF WRITES: the write list read from the act's face, its (W) table, every backticked path;
###   (ii)  step_commits          -- EVERY COMMIT OF A STEP: a step bank row's commits (its `commits` list, or its one `commit`);
###   (iii) defect_owners         -- ONE COUNTER: the defects bank's letters counted by owner, once;
###   (iv)  lock_refuses          -- THE LOCK AS A MEMBRANE: the pre-lock steps' banks refuse a rewrite once the act's lock is written;
###   (vi)  close_steps, close_refuses -- THE CLOSE IN ONE ORDER: v4 row (68) read as numbered steps, each with its evidence, and a step
###         refused while a lower step's evidence is absent.
### ((v), the capture for every push, is tools/push_gated.sh's own; the head line's remote read is tools/b713_closing.py's.) Every function is
### pure in its arguments or reads only the paths it is given; nothing here writes. Written by the Write tool at b713.
"""
import fnmatch
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
V4 = os.path.join(D, 'standing_clauses_v4.txt')


# ================================================================================ (i) ONE LIST OF WRITES
W_HEAD = re.compile(r'^### \(W\) THE WRITE LIST')
Z_HEAD = re.compile(r'^### \(Z\) THE NOTHINGS')
W_PATH = re.compile(r'`((?:relay|PLACE-papers|SIDE-[\w-]+)/[^`\s]+)`')


def w_patterns(face_text):
    """every backticked repository path of the face's (W) table, from its head to the (Z) head: ['relay/data/b712_*', ...]."""
    out, on = [], False
    for l in (face_text or '').replace(chr(13), '').split(NL):
        if W_HEAD.match(l):
            on = True
            continue
        if on and Z_HEAD.match(l):
            break
        if on:
            for p in W_PATH.findall(l):
                if p not in out:
                    out.append(p)
    return out


def w_allows(path, patterns, repo='relay'):
    """True where `<repo>/<path>` matches a (W) pattern (a glob, `*` within the name)."""
    q = '%s/%s' % (repo, path.replace('\\', '/'))
    return any(fnmatch.fnmatchcase(q, p) for p in patterns)


# ================================================================================ (ii) EVERY COMMIT OF A STEP
def step_commits(rows, phase=None, repo=None):
    """every commit a step bank's rows carry -- each row's `commits` list where it has one, else its `commit` -- for the rows of the phase and
    the repository named (all where None), in the bank's order, each once."""
    out = []
    for r in rows or []:
        if (phase is not None and r.get('phase') != phase) or (repo is not None and r.get('repo') != repo):
            continue
        for c in (r.get('commits') or [r.get('commit') or '']):
            if c and c not in out:
                out.append(c)
    return out


# ================================================================================ (iii) ONE COUNTER
OWNER = re.compile(r"^\(([a-z]'?)\) THE ([A-Z][A-Z_ -]*?)(?:’S|'S|’|')")


def defect_owners(letter_rows):
    """the defects' letters counted by owner, once: {'TOTAL': n, 'SEAT': n, 'NAVIGATOR': n, 'OTHER': n, 'by': [(letter, owner)]}. A row is
    `(x) THE <OWNER>'S ...` (the bank's own indent read through); SEAT and NAVIGATOR are the owners those words name, every other owner (a
    tool's, the carried form's) OTHER."""
    by = []
    for s in letter_rows or []:
        m = OWNER.match(s.lstrip())
        if m:
            o = m.group(2).strip()
            by.append((m.group(1), 'SEAT' if o == 'SEAT' else 'NAVIGATOR' if o == 'NAVIGATOR' else 'OTHER'))
    return dict(TOTAL=len(by), SEAT=sum(1 for _x, o in by if o == 'SEAT'), NAVIGATOR=sum(1 for _x, o in by if o == 'NAVIGATOR'),
                OTHER=sum(1 for _x, o in by if o == 'OTHER'), by=by)


# ================================================================================ (vi) THE CLOSE IN ONE ORDER
STEP = re.compile(r'\[(\d+)\] (.*?) \((data/<act>_[^)\s]+|the commands bank)\)')


def close_steps(v4_text=None):
    """v4 row (68) as [(n, words, evidence)], the evidence a path with <act> or 'the commands bank'."""
    t = v4_text if v4_text is not None else open(V4, encoding='utf-8').read()
    row = next((l for l in t.replace(chr(13), '').split(NL) if l.strip().startswith('THE CLOSE IN ONE ORDER, THE STEPS NUMBERED')), '')
    return [(int(n), w, e) for n, w, e in STEP.findall(row)]


def _evidence(e, act, dd):
    return None if not e.startswith('data/') else os.path.join(dd, os.path.basename(e.replace('<act>', act)))


def close_refuses(act, n, dd=None, v4_text=None, present=None):
    """the refusal's text where a step lower than n lacks its evidence, '' where step n may run. `present(path)` decides a bank's presence
    (default: the file exists) so a replay can read the banks as they stood at a time."""
    dd = dd or D
    has = present or os.path.exists
    steps = close_steps(v4_text)
    if not steps or n not in [s[0] for s in steps]:
        return '### THE CLOSE`S ORDER (v4 row (68)) CARRIES NO STEP [%d] -- REFUSED' % n
    miss = [(k, w, e) for k, w, e in steps if k < n and _evidence(e, act, dd) and not has(_evidence(e, act, dd))]
    if miss:
        k, w, e = miss[0]
        return ('### THE CLOSE IN ONE ORDER (standing clauses v4 row (68)): STEP [%d] REFUSED -- STEP [%d] (%s) IS UNFINISHED, ITS EVIDENCE %s '
                'ABSENT%s -- NOTHING RUN' % (n, k, w[:60], e.replace('<act>', act), (' (and %d more lower steps)' % (len(miss) - 1)) if len(miss) > 1 else ''))
    return ''


# ================================================================================ (iv) THE LOCK AS A MEMBRANE
def pre_lock_banks(act, v4_text=None):
    """the banks of the steps before the lock in v4 row (68) (the lock's own step excluded), by basename, each with its .txt/.json sibling."""
    steps = close_steps(v4_text)
    lock_n = next((k for k, w, e in steps if e.endswith('_lockgate.json')), None)
    out = []
    for k, w, e in steps:
        if lock_n is not None and k < lock_n and e.startswith('data/'):
            b = os.path.basename(e.replace('<act>', act))
            stem = re.sub(r'\.(txt|json)$', '', b)
            out += [b, stem + '.txt', stem + '.json']
    return sorted(set(out))


def lock_refuses(act, name, dd=None, v4_text=None):
    """the refusal's text where the act's lock is written (data/<act>_lockgate.json) and the bank is one a step before the lock wrote and
    stands written; '' otherwise. As the root's membrane refuses after the root (row (53)), so the lock's after the lock."""
    dd = dd or D
    base = os.path.basename(name)
    if not os.path.exists(os.path.join(dd, '%s_lockgate.json' % act)):
        return ''
    if base in pre_lock_banks(act, v4_text) and os.path.exists(os.path.join(dd, base)):
        return ('### THE LOCK AS A MEMBRANE (standing clauses v4 row (65)): %s`S LOCK IS WRITTEN (data/%s_lockgate.json) AND %s IS A BANK '
                'WRITTEN BEFORE IT -- NOTHING WRITTEN' % (act, act, base))
    return ''
