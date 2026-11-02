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
