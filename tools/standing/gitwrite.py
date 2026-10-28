# -*- coding: utf-8 -*-
"""standing/gitwrite.py -- ONE GIT WRITE PER MESSAGE, COUNTING WRITES ONLY (v1.2.1; (R331)(2)(ii), b720's event (12)).

The rule (b673 row 3): one git write per assistant message. The old reading (tools/rule_arms.py G-RULE-ONE-GIT-WRITE, and the record
tool's N5 through it) counts CALLS: a call whose text matches GIT_WRITE anywhere counts one, however many writes it carries. Read here:
each call's text, quoted strings blanked, is split into its commands (at `;`, `&&`, `||` and new lines); a command is a write when
GIT_WRITE (read from tools/rule_arms.py, not copied) matches it and it is not a listing; a message's writes are the sum over its calls'
commands. A listing is never a write: `git branch` with no name or with --list/-l/-a/-r/-v/--merged/--no-merged/--contains/
--show-current only, `git tag` with no name or -l/--list, and every git read (log, show, status, diff, ls-remote, rev-parse, ...).

  commands(cmd) -> [command texts]          is_listing(command) -> bool          writes(cmd) -> [write commands]
  per_message(calls) -> {mid: [(ts, n)]}    reading(calls) -> (ok, messages_with_writes, over, note)
  old_reading(calls) -> the call-counting reading, for the control
  calls_of(session_path, lo, hi) -> [dict(mid, ts, cmd)]   the shell calls of a transcript between two UTC stamps
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import rule_arms as RA   # noqa: E402

SPLIT = re.compile(r';|&&|\|\||\n')
LIST_FLAGS = r'(?:\s+(?:--list|-l|-a|-r|-v|-vv|--all|--remotes|--merged|--no-merged|--contains|--show-current|--points-at)\b(?:\s+[^\s-]\S*)?)*'
LISTING = re.compile(r'^\s*git\s+(?:-C\s+\S+\s+)*(?:branch|tag)' + LIST_FLAGS + r'\s*$')


def commands(cmd):
    return [c.strip() for c in SPLIT.split(RA.QUOTED.sub('""', cmd or '')) if c.strip()]


def is_listing(c):
    return bool(LISTING.match(c))


def writes(cmd):
    return [c for c in commands(cmd) if RA.GIT_WRITE.search(c) and not is_listing(c)]


def per_message(calls):
    per = {}
    for c in calls:
        n = len(writes(c['cmd']))
        if n:
            per.setdefault(c['mid'], []).append((c['ts'], n))
    return per


def reading(calls):
    per = per_message(calls)
    over = [(m, v[0][0], sum(n for _t, n in v)) for m, v in per.items() if sum(n for _t, n in v) > 1]
    return bool(calls) and not over, len(per), over, 'messages carrying a git write %d ; with more than one %s' % (
        len(per), [(ts, n) for _m, ts, n in over][:3] or 'NONE')


def old_reading(calls):
    """tools/rule_arms.py's reading of G-RULE-ONE-GIT-WRITE, by call (its :481-:488), over the same calls."""
    per = {}
    for c in calls:
        if RA.GIT_WRITE.search(RA.QUOTED.sub('""', c['cmd'])):
            per.setdefault(c['mid'], []).append(c['ts'])
    over = [(m, ts[0], len(ts)) for m, ts in per.items() if len(ts) > 1]
    return bool(calls) and not over, len(per), over, 'messages carrying a git write %d ; with more than one %s' % (
        len(per), [(ts, n) for _m, ts, n in over][:3] or 'NONE')


def calls_of(path, lo, hi):
    out = []
    for l in io.open(path, encoding='utf-8', errors='replace'):
        try:
            j = json.loads(l)
        except ValueError:
            continue
        ts = j.get('timestamp') or ''
        if j.get('type') != 'assistant' or not (lo <= ts <= hi):
            continue
        msg = j.get('message') or {}
        for c in msg.get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') in ('Bash', 'PowerShell'):
                out.append(dict(mid=msg.get('id') or '', ts=ts, cmd=(c.get('input') or {}).get('command', '')))
    return out
