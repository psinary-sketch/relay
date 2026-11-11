# -*- coding: utf-8 -*-
"""standing/chain.py -- v1.33.0, (R363)(7)(iii), b752 events (6): THE CHAIN READ AND THE ANSWER READ FROM THE BLOB ROW.

THE CHAIN READ (from the hold's script, read and rewritten in the standing form): for a session's transcript, every row naming a parent
(parentUuid) that no row of the file holds, by line and time. A compaction boundary is told apart by this rule: a row of subtype
compact_boundary carries no parentUuid and a logicalParentUuid; it is a BOUNDARY, never counted as an absent parent, and it is printed with
whether its logical parent stands in the file. A row naming an absent parent is a WRITE LOST (the row it names was never written or was lost
before the file was read), whatever its type. Run at step zero, before the answers route's dry and before the lock; a row it finds after the
act's opening row is an event, and the answers and author-words routes print its count beside what they bank.

THE BLOB ANSWER: where a put's call (AskUserQuestion) has no ordinary result row (a user row's tool_result) and an api-request-blob row of
the transcript carries a tool_result for that call, the answer is read from that row, marked READ FROM THE api-request-blob ROW with its
line. b752's root answer: call toolu_01A9s3DA... at :10971, its user row :10972 naming a parent the file does not hold and carrying no
answer, the answer in the blob row :11286. No past bank is rewritten by it.

  chain(path) -> dict(rows, lost=[(line, ts, type)], boundaries=[(line, ts, logical_in_file)])      ABSENT path: SystemExit printing ABSENT
  blob_results(path, ids) -> {id: (line, text)}
  fill(lines, blob) -> (lines, filled)        the composed answers lines, each `### NO RESULT` of a call the blob row answers replaced, marked

  python -X utf8 -u tools/standing/chain.py read <session id> [<session id> ...]
  python -X utf8 -u tools/standing/chain.py control
"""
import io
import json
import os
import re
import sys

PROJ = 'C:/Users/echo chamber/.claude/projects/D--'
B752 = '43048615-75cd-4480-bfa6-362a3c13092b'
B752_LOST = (10972, 12569, 12570, 12571, 12572, 12573, 12892, 12903, 12904)


def path_of(sid, proj=PROJ):
    p = '%s/%s.jsonl' % (proj, sid)
    if not os.path.isfile(p):
        raise SystemExit('### ABSENT: session %s -- no transcript at %s; NOTHING READ' % (sid, p))
    return p


def _rows(path):
    for i, raw in enumerate(io.open(path, encoding='utf-8', errors='replace'), 1):
        try:
            yield i, json.loads(raw)
        except ValueError:
            yield i, None


def chain(path):
    rows = list(_rows(path))
    uu = set(o.get('uuid') for _i, o in rows if o and o.get('uuid'))
    lost, bounds = [], []
    for i, o in rows:
        if not o:
            continue
        if o.get('subtype') == 'compact_boundary' and not o.get('parentUuid'):
            bounds.append((i, o.get('timestamp'), o.get('logicalParentUuid') in uu))
            continue
        if o.get('parentUuid') and o['parentUuid'] not in uu:
            lost.append((i, o.get('timestamp'), o.get('type')))
    return dict(rows=len(rows), lost=lost, boundaries=bounds)


def lines(sid, r, after=None):
    """the print: the counts, every lost row, every boundary; with after (a line), the rows past it counted apart (each an event)."""
    late = [x for x in r['lost'] if after is not None and x[0] > after]
    L = ['### THE CHAIN READ, session %s: ROWS %d ; WRITES LOST (a parent no row holds) %d%s ; COMPACTION BOUNDARIES %d (a boundary carries no parent '
         'and a logical parent; never counted lost)' % (sid[:8], r['rows'], len(r['lost']), (' ; AFTER LINE %d: %d' % (after, len(late))) if after is not None else '',
                                                        len(r['boundaries']))]
    L += ['   LOST :%d %s %s' % x for x in r['lost']]
    L += ['   BOUNDARY :%d %s logical parent in the file %s' % x for x in r['boundaries']]
    return L


def blob_results(path, ids):
    ids, out = set(ids), {}
    for i, o in _rows(path):
        if not o or o.get('type') != 'api-request-blob':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ids and c['tool_use_id'] not in out:
                t = c.get('content')
                out[c['tool_use_id']] = (i, ''.join(x.get('text', '') for x in t if isinstance(x, dict)) if isinstance(t, list) else (t or ''))
    return out


CALL = re.compile(r'^### CALL tool-use id (\S+) ')
NONE = re.compile(r'^RESULT \(transcript line None(?:, None)?\): ### NO RESULT$')


def fill(lines_, blob):
    out, cur, filled = [], None, []
    for l in lines_:
        m = CALL.match(l)
        if m:
            cur = m.group(1)
        if cur in blob and NONE.match(l):
            ln, t = blob[cur]
            out.append('RESULT (READ FROM THE api-request-blob ROW, transcript line %d; no ordinary result row): %s' % (ln, t))
            filled.append((cur, ln))
            continue
        out.append(l)
    return out, filled


def unanswered(path):
    """the AskUserQuestion call ids of the file's assistant rows that no user row's tool_result answers."""
    asks, done = [], set()
    for _i, o in _rows(path):
        if not o:
            continue
        for c in (o.get('message') or {}).get('content') or [] if isinstance((o.get('message') or {}).get('content'), list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion' and o.get('type') == 'assistant':
                asks.append(c['id'])
            if isinstance(c, dict) and c.get('type') == 'tool_result' and o.get('type') == 'user':
                done.add(c.get('tool_use_id'))
    return [a for a in asks if a not in done]


def _version(path):
    """the harness version the transcript's last row carrying one names; '-' where none."""
    v = '-'
    for _i, o in _rows(path):
        if o and o.get('version'):
            v = o['version']
    return v


def store_read(sid, prev_sid=None, proj=PROJ, store='D:/claude-store/projects-D--', settings='C:/Users/echo chamber/.claude/settings.json'):
    """v1.33.0, (R363)(7)(viii), at step zero: the retention setting; the projects path, a junction or not, with its target; this session's
    transcript by both paths at one size; the harness's version beside the previous session's. (ok, lines): ok where the setting reads 3650,
    the path is a junction to the store and both sizes agree."""
    try:
        ret = json.load(io.open(settings, encoding='utf-8')).get('cleanupPeriodDays')
    except (OSError, ValueError):
        ret = 'UNREADABLE'
    real = os.path.realpath(proj).replace('\\', '/')
    junction = real.lower() != proj.lower()
    a, b = path_of(sid, proj), '%s/%s.jsonl' % (store, sid)
    sa, sb = os.path.getsize(a), (os.path.getsize(b) if os.path.isfile(b) else None)
    v, pv = _version(a), (_version(path_of(prev_sid, proj)) if prev_sid else '-')
    ok = ret == 3650 and junction and real.lower() == store.lower() and sa == sb
    return ok, ['### THE STORE READ ((R363)(7)(viii)): retention %s days ; the projects path %s%s ; session %s by both paths %s and %s bytes%s ; '
                'the harness %s, the previous session %s ; %s' % (ret, 'A JUNCTION TO ' if junction else '### NOT A JUNCTION, ', real, sid[:8], sa, sb,
                                                                  '' if sa == sb else ' ### DIFFERING', v, pv, 'AS WANTED' if ok else '### NOT AS WANTED')]


def route_fill(lines_, sids, proj=PROJ):
    """for the answers route: the composed lines filled from the blob rows of the act's sessions, and the note it prints -- each session's
    chain count (writes lost) beside what it banks. A session absent prints ABSENT and stops the route (path_of)."""
    out, notes = list(lines_), []
    for s in sids:
        p = path_of(s, proj)
        out, filled = fill(out, blob_results(p, unanswered(p)))
        r = chain(p)
        notes.append('%s: writes lost %d, answers read from the blob row %d %s' % (s[:8], len(r['lost']), len(filled), filled or ''))
    return out, '  the chain read beside the bank ((R363)(7)(iii)): ' + ' ; '.join(notes)


def control(this=None):
    """(ok, lines): session 43048615 replayed, its nine lost rows; b752's unanswered put filled from the blob row, marked; a planted id that no
    file holds printing ABSENT; this act's session (when given) read."""
    p = path_of(B752)
    r = chain(p)
    got = tuple(x[0] for x in r['lost'])
    L = lines(B752, r) + ['   12892 IS A WRITE LOST: an assistant row whose parent, the row written 4 s before it, no row of the file holds; not a boundary '
                          '(it carries a parent and no logical parent)']
    un = unanswered(p)
    bl = blob_results(p, un)
    composed = ['### CALL tool-use id %s (session %s, transcript line 10971, -)' % (un[0] if un else '-', B752[:8]), 'RESULT (transcript line None, None): ### NO RESULT']
    f, filled = fill(composed, bl)
    try:
        path_of('00000000-0000-0000-0000-000000000000')
        absent = False
    except SystemExit as e:
        absent = str(e).startswith('### ABSENT')
    ok = got == B752_LOST and len(un) == 1 and len(filled) == 1 and filled[0][1] == 11286 and absent
    L += ['### b752`s puts without an ordinary result: %d %s ; filled from the blob row: %s ; the bank line: %s' % (len(un), un, filled, f[1][:140]),
          '### a planted session id no file holds: %s' % ('ABSENT' if absent else '### READ AS PRESENT')]
    if this:
        rt = chain(path_of(this))
        L += lines(this, rt)
    L.append('### (chain) THE NINE ROWS %s ; THE BLOB ANSWER AT :11286 %s ; THE CONTROL %s' % ('REPRODUCED' if got == B752_LOST else '### NOT %s' % (got,),
             'BANKED WITH THE MARK' if filled else '### NOT FOUND', 'AS WANTED' if ok else 'NOT AS WANTED'))
    return ok, L


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        ok, L = control(a[1] if len(a) > 1 else None)
        print('\n'.join(L))
        sys.exit(0 if ok else 1)
    if a[:1] == ['read'] and len(a) > 1:
        for s in a[1:]:
            print('\n'.join(lines(s, chain(path_of(s)))))
        sys.exit(0)
    sys.exit(__doc__)
