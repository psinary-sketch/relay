# -*- coding: utf-8 -*-
"""standing/actlog.py -- v1.29.0, (R359)(3)(vi), b748 defects (g), (l): A CONTROL READING A PRIOR ACT'S LOG READS IT TO THAT ACT'S LOCK AND
CHOOSES COMMITS BY ITS STEP ROWS, NOT BY GREP.

b748's (gate) replay read b747's log to c19fde00, the third of six gate commits, and missed 88f39b22 (the fourth); its (rows) control chose
b747's step-rows commits by `--grep=the step row` and took 0c118109, a component commit whose body names step rows. Here the commits come
from the act's own step bank (data/<act>_steps.json as the relay's HEAD holds it): by phase, to the act's lock where the reader asks for the
commits before it; and the commits of the act's range that no row names (a step-rows commit writes none of its own) by the files they touch.

  rows(act)                          the act's step rows, as committed
  lock(act)                          the lock row's commit (None where the act has none)
  by_phase(act, phase, repo='relay') the commits of the rows of that phase, in their order; a phase before the lock read to the lock
  unrowed(act)                       the relay commits between the act's first row and its last that no row names, oldest first
  step_rows_commits(act)             of those, the ones whose files are the act's step bank (with the scan's banks) alone
"""
import json
import os
import subprocess

RELAY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def rows(act, ref='HEAD'):
    t = _git('show', '%s:data/%s_steps.json' % (ref, act))
    try:
        return (json.loads(t) or {}).get('rows') or []
    except ValueError:
        return []


def lock(act, ref='HEAD'):
    return next((r['commit'] for r in rows(act, ref) if r.get('phase') == 'lock' and r.get('repo') == 'relay'), None)


def by_phase(act, phase, repo='relay', ref='HEAD'):
    R = rows(act, ref)
    k = next((i for i, r in enumerate(R) if r.get('phase') == 'lock'), len(R))
    pre = phase in ('step zero', 'component 1', 'component 2', 'component 3', 'component 4', 'gate', 'lock')
    return [r['commit'] for i, r in enumerate(R) if r.get('phase') == phase and r.get('repo') == repo and (not pre or i <= k)]


def unrowed(act, ref='HEAD'):
    R = [r for r in rows(act, ref) if r.get('repo') == 'relay']
    if not R:
        return []
    named = set(r['commit'] for r in R)
    # ### the act's span: its first row to the commit before the next act's first row (the step-rows commits after its closing commit
    # ### included, b747's 7d34b587), or to its last row where the next act has none yet
    nxt = [r for r in rows('b%d' % (int(act[1:]) + 1), ref) if r.get('repo') == 'relay']
    end = (nxt[0]['commit'] + '^') if nxt else R[-1]['commit']
    span = [h for h in _git('rev-list', '--reverse', '--first-parent', '%s^..%s' % (R[0]['commit'], end)).split('\n') if h]
    span = [h for h in span if not any(_git('log', '-1', '--format=%s', h).startswith('%s ' % a) for a in ('b%d' % (int(act[1:]) + 1),))]
    return [h for h in span if h not in named]


def step_rows_commits(act, ref='HEAD'):
    beside = {'data/%s_steps.json' % act, 'data/%s_address_scan.txt' % act, 'data/%s_address_scan_postlock.txt' % act,
              'data/%s_address_scan_commits.txt' % act, 'data/%s_bank_hashes.json' % act, 'data/%s_hook_refusals.txt' % act}
    out = []
    for h in unrowed(act, ref):
        names = [p for p in _git('show', '--name-only', '--format=', h).split('\n') if p]
        if 'data/%s_steps.json' % act in names and set(names) <= beside:
            out.append(h)
    return out
