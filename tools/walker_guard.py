# -*- coding: utf-8 -*-
"""walker_guard.py -- A SEARCH WHOSE TOOL CALL REACHED ITS LIMIT IS INCOMPLETE, NEVER A COUNT. ### (b418.)

### ### **THE SPECIES, ONE LEVEL DOWN FROM THE VACUOUS PASS.** ### At b417 the seat's `Grep` tool ran a
### search over relay's `data/` for 20.04 seconds -- its limit -- and returned the files it had reached,
### with `numFiles: 13`, no truncation flag and no timeout text. The same query, completed, reaches forty
### files that existed then. ### **A TRUNCATION WITH NO FLAG READS EXACTLY LIKE A SMALL ANSWER.**

### ### **WHAT THIS DOES.** ### Given a walker call's recorded start and its result's recorded time (the
### session transcript carries both), `verdict()` returns `INCOMPLETE` for a call that reached the limit
### and the count for one that did not. ### **THE GUARD IS THE ONE LINE MARKED BELOW**; everything else
### is the reading that feeds it.

### ### **THE WRAPPER THIS IS, AND WHY IT HAD TO BE BUILT.** ### The order placed the guard as *one line in
### the search wrapper*. ### Relay had none: its text helpers flatten and pull needles and walk no
### directory, and the walker is the Claude Code `Grep` tool, which relay cannot edit. ### So this is the
### smallest wrapper that can carry that line.

### ### **ITS REACH, IN THE HEADER SO IT IS NOT TRUSTED BEYOND IT:** ### it guards what a record TAKES
### from a walker's result -- a result never passed through `verdict()` is not guarded. ### And it
### knows the limit it is told; the default is the tool's own observed twenty seconds, less a margin
### for clock rounding between the two recorded timestamps.
"""
import io
import json
import os
import sys
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LIMIT = 20.0
MARGIN = 0.5
INCOMPLETE = 'INCOMPLETE'


def _t(s):
    return datetime.strptime(s[:23], '%Y-%m-%dT%H:%M:%S.%f')


def seconds(call_at, result_at):
    return (_t(result_at) - _t(call_at)).total_seconds()


def verdict(call_at, result_at, count, limit=LIMIT, margin=MARGIN):
    """### RETURN `INCOMPLETE` OR THE COUNT -- NEVER A COUNT FROM A CALL THAT REACHED ITS LIMIT."""
    if seconds(call_at, result_at) >= limit - margin: return INCOMPLETE   # ### THE GUARD'S ONE LINE.
    return count


def calls_in(transcript, tool='Grep'):
    """### EVERY `tool` CALL IN A SESSION TRANSCRIPT, WITH ITS RESULT'S TIME AND METADATA."""
    uses, out = {}, []
    for line in io.open(transcript, encoding='utf-8', errors='replace'):
        try:
            o = json.loads(line)
        except Exception:
            continue
        c = (o.get('message') or {}).get('content')
        if not isinstance(c, list):
            continue
        for b in c:
            if b.get('type') == 'tool_use' and b.get('name') == tool:
                uses[b['id']] = (o.get('timestamp'), b.get('input') or {})
            elif b.get('type') == 'tool_result' and b.get('tool_use_id') in uses:
                at, inp = uses[b['tool_use_id']]
                tur = o.get('toolUseResult') if isinstance(o.get('toolUseResult'), dict) else {}
                txt = b.get('content')
                if isinstance(txt, list):
                    txt = ' '.join(x.get('text', '') for x in txt if isinstance(x, dict))
                out.append(dict(at=at, result_at=o.get('timestamp'), input=inp,
                                numFiles=tur.get('numFiles'), content=tur.get('content') or '',
                                timed_out='timed out' in (txt or '')))
    return out


def self_test(verbose=True):
    """### BOTH POLARITIES. ### **A GUARD THAT HAS ONLY EVER SAID COMPLETE IS NOT A GUARD.**"""
    cases = [
        ('b417`s call: 13:28:55.279 -> 13:29:15.319, numFiles 13',
         ('2026-09-11T13:28:55.279Z', '2026-09-11T13:29:15.319Z', 13), INCOMPLETE),
        ('a call that finished in 0.4 s with 3 files',
         ('2026-09-11T13:23:58.588Z', '2026-09-11T13:23:59.000Z', 3), 3),
        ('### a call exactly at the limit is INCOMPLETE, not a count',
         ('2026-09-11T10:00:00.000Z', '2026-09-11T10:00:20.000Z', 7), INCOMPLETE),
        ('### an empty result from a truncated call is INCOMPLETE, not an absence',
         ('2026-09-11T10:00:00.000Z', '2026-09-11T10:00:20.100Z', 0), INCOMPLETE),
        ('an empty result from a completed call is a real zero',
         ('2026-09-11T10:00:00.000Z', '2026-09-11T10:00:01.000Z', 0), 0),
    ]
    ok = True
    for lbl, args, want in cases:
        got = verdict(*args)
        good = (got == want)
        ok = ok and good
        if verbose:
            print('    %-72s got %-10s want %-10s %s' % (lbl[:72], got, want, 'PASS' if good else '### FAIL'))
    return ok


if __name__ == '__main__':
    print('walker_guard.py -- SELF-TEST, BOTH POLARITIES')
    sys.exit(0 if self_test() else 1)
