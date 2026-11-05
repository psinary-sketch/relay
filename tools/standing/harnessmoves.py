# -*- coding: utf-8 -*-
"""standing/harnessmoves.py -- v1.22.0, (R352)(2)(ii), b741 event (4): THE HARNESS'S BACKGROUND MOVE, BANKED AS THE HARNESS'S ACT, DISTINCT FROM A SEAT'S
BACKGROUND RUN. b741's post-push standing-b2c was sent in the foreground; at its 600 s timeout the harness moved it to the background ("Command did not
complete within its 600s timeout and was moved to the background (ID: bh6cl8npl)"). The seat sent nothing with run_in_background, and N1's count of
suite parts sent in the background read 0 -- correctly for the seat, silently for the harness. Here the two are read apart from the session's transcript:

  moves(transcript)    [dict(at, tool_use_id, command, task, timeout_s)] -- every tool call the harness moved to the background
  seat_bg(transcript)  [dict(at, tool_use_id, command)] -- every tool call the seat sent with run_in_background
  line(transcript)     "MOVED BY THE HARNESS n (...) ; SENT IN THE BACKGROUND BY THE SEAT m"
"""
import json
import re

MOVED = re.compile(r'did not complete within its (\d+)s timeout and was moved to the background \(ID: (\w+)\)')


def _rows(transcript):
    with open(transcript, encoding='utf-8', errors='replace') as f:
        for l in f:
            try:
                yield json.loads(l)
            except ValueError:
                continue


def _calls(transcript):
    calls, results = {}, []
    for j in _rows(transcript):
        c = (j.get('message') or {}).get('content')
        if not isinstance(c, list):
            continue
        for b in c:
            if not isinstance(b, dict):
                continue
            if b.get('type') == 'tool_use':
                calls[b.get('id')] = dict(at=j.get('timestamp'), input=b.get('input') or {}, name=b.get('name'))
            elif b.get('type') == 'tool_result':
                t = b.get('content')
                t = t if isinstance(t, str) else ' '.join(x.get('text', '') for x in (t or []) if isinstance(x, dict))
                results.append((b.get('tool_use_id'), j.get('timestamp'), t))
    return calls, results


def moves(transcript):
    calls, results = _calls(transcript)
    out = []
    for tid, at, t in results:
        m = MOVED.search(t or '')
        if m:
            c = calls.get(tid) or {}
            out.append(dict(at=c.get('at'), moved_at=at, tool_use_id=tid, command=(c.get('input') or {}).get('command', '')[:300], task=m.group(2), timeout_s=int(m.group(1))))
    return out


def seat_bg(transcript):
    calls, _r = _calls(transcript)
    return [dict(at=c['at'], tool_use_id=k, command=c['input'].get('command', '')[:300]) for k, c in calls.items() if c['input'].get('run_in_background')]


def line(transcript):
    mv, bg = moves(transcript), seat_bg(transcript)
    def what(c):
        p = re.search(r'--part (\S+)', c)
        return ('the suite part %s%s' % (p.group(1), ' (post-push)' if 'postpush' in c or 'rerun-postpush' in c else '')) if p else re.sub(r'\s+', ' ', c)[:90]
    return 'MOVED BY THE HARNESS %d (%s) ; CALLS SENT IN THE BACKGROUND BY THE SEAT %d' % (
        len(mv), ', '.join('%s, sent %s, its notice %s, %s' % (m['task'], m['at'], m['moved_at'], what(m['command'])) for m in mv) or 'none', len(bg))
