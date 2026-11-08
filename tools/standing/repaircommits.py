# -*- coding: utf-8 -*-
"""standing/repaircommits.py -- v1.15.0, (R345)(2)(iv)-(v), b734 events (5) and defects (p), (w).

(iv) A REPAIR LANDED BY A COMMIT OF ITS OWN CARRIES ITS CONTROL IN THE VERSION'S BANK AND MOVES VERSION. b734's 21a94e81 and 117ab5bc touched the standing tools after v1.14.0's commit and left VERSION
where it stood; no version's bank read them. `outside(version_commit, tip)` lists the commits after a version's commit, to a tip, that touch tools/standing/ and leave tools/standing/VERSION
unmoved. The lock gate refuses while one stands.

(v) THE ENTRY NAMES EVERY REPAIR COMMIT THE EVENTS BANK NAMES. b734's entry at FINDINGS :12751 names 21a94e81 and not 117ab5bc. `named(events, defects)` reads the commits the act's banks call
repairs, in order; `clause(ids)` is the entry's sentence, composed from them; the composer takes no id by hand.

  outside(version_commit, tip='HEAD') -> [(hash8, subject)]
  named(events_text, defects_text='') -> [hash8]   clause(ids) -> str   missing(entry, ids) -> [hash8]
"""
import os
import re
import subprocess

RELAY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPAIR = re.compile(r'\brepair', re.I)
ID = re.compile(r'(?<![0-9a-f])[0-9a-f]{8}(?![0-9a-f])')


def _git(*a):
    return subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def outside(version_commit, tip='HEAD'):
    out = []
    for row in _git('log', '--reverse', '--format=%h %s', '--abbrev=8', '%s..%s' % (version_commit, tip), '--', 'tools/standing/').split('\n'):
        if not row.strip():
            continue
        h, sub = row.split(' ', 1)
        if 'tools/standing/VERSION' not in _git('show', '--name-only', '--format=', h).split():
            out.append((h, sub))
    return out


def late(commits, gate):
    """v1.28.0, (R358)(3)(iii), b747 defects (j), (a'): the commits at or after the gate, in order, that touch tools/standing/ -- a standing
    repair lands with its version before the gate, not between the gate and the lock. Pure: commits [(hash8, subject, touches_standing)] in
    order, gate the gate commit's hash8 (or None: nothing is late before the gate)."""
    if not gate:
        return []
    hs = [c[0] for c in commits]
    if gate not in hs:
        return []
    return [(h, 'AT OR AFTER THE GATE: ' + s) for h, s, t in commits[hs.index(gate):] if t]


def after_gate(act, tip='HEAD'):
    """late() over the act's step bank (its FIRST gate row: b747 carried six gate commits, f2dd38e0 to 6295b920, and its VERSION moved in the
    fourth, 88f39b22; read from the last, the move stood before the gate and passed) and the relay's log from the gate commit to `tip`."""
    import json
    try:
        rows = json.load(open(os.path.join(RELAY, 'data', '%s_steps.json' % act), encoding='utf-8')).get('rows') or []
    except (OSError, ValueError):
        return []
    gates = [r for r in rows if r.get('phase') == 'gate' and r.get('repo') == 'relay']
    if not gates:
        return []
    g8 = gates[0]['commit'][:8]
    commits = []
    for row in _git('log', '--reverse', '--format=%h %s', '--abbrev=8', '%s^..%s' % (g8, tip)).split('\n'):
        if row.strip():
            h, sub = row.split(' ', 1)
            commits.append((h, sub, any(n.startswith('tools/standing/') for n in _git('show', '--name-only', '--format=', h).split())))
    return late(commits, g8)


def named(events, defects=''):
    """the eight-hex ids of the rows that call themselves repairs, each row of a bank a line, the commit known to the repository; in order, each once."""
    out = []
    for text in (events or '', defects or ''):
        for l in text.split('\n'):
            if not REPAIR.search(l):
                continue
            for h in ID.findall(l):
                if h not in out and _git('cat-file', '-t', h).strip() == 'commit':
                    out.append(h)
    return out


def clause(ids):
    return 'the repair commits the banks name: %s' % (', '.join('`%s`' % h for h in ids) if ids else 'none')


def missing(entry, ids):
    return [h for h in ids if h not in (entry or '')]
