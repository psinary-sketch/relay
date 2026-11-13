# -*- coding: utf-8 -*-
"""standing/statedir.py -- v1.34.0, (R364)(3)(xv): THE STATE FOLDER, ONE RESOLVER.

The hook's calls ledger and its git-write state stood in the temp directory (tools/standing/hook.py :282, :306; tools/standing/commit.py :318),
each tool building the path for itself; b753's store read (data/b753_store.txt) found the temp directory among the places under the user's
profile that a restart, a cleanup or a change of host can clear. They stand in the state folder on the data volume -- the folder (R364)(8)
names for the step-zero restore's copies and the kept copies of a close -- outside every repository and outside the temp directory, and the
hook and the one-call tool both take their paths here. An act's own scratch that a later act reads (the kept copies, the terminal table's
regeneration) stands under act_dir. Pure but for root(), which makes the hook's folder where it is absent.

  root()                    the state folder, its hook folder made where absent
  calls_path()              the calls ledger: the hook appends one record a shell call, the one-call tool reads its tail
  ledger_path(transcript)   the git-write state of one session's transcript
  act_dir(act, *parts)      an act's own folder in the state folder (not made here)
  outside()                 (outside every repository, outside the temp directory) for the state folder as it stands
"""
import hashlib
import os
import tempfile

RELAY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATE = os.path.join(os.path.dirname(RELAY), 'relay-state')
HOOK = 'hook'


def root():
    os.makedirs(os.path.join(STATE, HOOK), exist_ok=True)
    return STATE


def calls_path():
    return os.path.join(root(), HOOK, 'standing-calls.jsonl')


def ledger_path(transcript):
    return os.path.join(root(), HOOK, 'standing-gitwrite-%s.json' % hashlib.sha256(str(transcript).encode('utf-8')).hexdigest()[:16])


def act_dir(act, *parts):
    return os.path.join(STATE, act, *parts)


def outside():
    """(no `.git` in the state folder or in any folder above it, the temp directory not above it)."""
    s = os.path.abspath(STATE)
    d, repo = s, False
    while True:
        if os.path.exists(os.path.join(d, '.git')):
            repo = True
            break
        up = os.path.dirname(d)
        if up == d:
            break
        d = up
    tmp = os.path.abspath(tempfile.gettempdir())
    try:
        under = os.path.commonpath([tmp, s]).lower() == tmp.lower()
    except ValueError:   # ### two volumes: no common path
        under = False
    return not repo, not under
