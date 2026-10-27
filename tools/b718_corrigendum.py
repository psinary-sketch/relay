# -*- coding: utf-8 -*-
"""b718_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R328)(2): b717's ten events after its lock and seal (relay data/b717_events.txt, rows
(1)-(10) at four spaces) and the five items b717's close left uncommitted (the closing push capture, step row 19 of data/b717_steps.json,
data/b717_bank_hashes.json, tools/mirror_prevbuild.json, the hook's refusal of a Read call without a limit after the closing), answered by one
generated FINDINGS entry, each item tagged CLAIM or CLOSE under (R327)(2) (standing clauses v6 row (80); the ruling cites row (2), the
citation check's miss) and NEW or REPEAT with the act and letter of its class. The events' tags are read from the events bank's own heads;
the five items' tags are the seat's, each with its source. The navigator reads events (1), (2), (7), (8), (9), (10) and the five items as
CLOSE; each difference from that reading is printed and stands as the seat's. The two CLAIM items b717's counter carries -- its defects (p)
and (s) -- are named. The counter line prints CLAIM n and CLOSE m over the fifteen items.
### Carried from tools/b717_corrigendum.py by diff (data/b718_carry_corrigendum.txt) and rewritten whole by the Write tool: the carried tool
### described b716's nineteen events and eighteen defects; (R328)(2) orders b717's ten events and five items.
### THE CHECKS BEFORE ANY WRITE: the events bank's rows at four spaces number ten, (1)-(10), each head carrying its needle and its bracketed
### tag; each REPEAT's cited event row present in the bank it names; each item's source present (the file, its commit at this act's step
### zero carrying it alone, the refusal's line); b717's defects (p) and (s) tagged CLAIM; the corrigenda bank's last row (37). Any miss:
### nothing composed.
### Routes: `dry` prints the entry, the bank and the corrigenda row; `write` lands the entry on FINDINGS through b718_record's guarded landing
### and writes data/b718_corrigendum.txt (.json). The corrigenda bank's row (38) is appended by the seat through the Edit tool from the row
### this tool prints.
"""
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b678_corrigendum as C78   # noqa: E402  ### b678's tool, imported unchanged: rd
from b652_record import conv     # noqa: E402  ### the one conversion
import b718_record as REC         # noqa: E402  ### the guarded landing, git
import b718_worklist as K         # noqa: E402  ### the step-zero commits

TITLE = ('## Corrigendum to b717’s record (relay data/b717_events.txt and the five items its close left uncommitted): ten events and five '
         'items, each CLAIM or CLOSE and NEW or REPEAT, under (R328)(2)')
CORRIGENDA_LAST = 37
NAVIGATOR_CLOSE = [1, 2, 7, 8, 9, 10]

# ### the classes of the CLOSE items, gathered for tools/standing/ v1.2.0 ((R328)(6))
CLASSES = {
    'FORM': 'a writer and its reader in two forms: a face line, a needle or a bank written outside the words the standing reader takes',
    'CONTROL': 'an arm`s pattern or control that cannot fire, or fires on a reference it should not read',
    'ORDER': 'the close`s own sequencing: a step omitted, a file left uncommitted, a figure summed by hand, a plant on the wrong side of the lock',
    'HOOK': 'a call the hook refused before it ran (row (77)): a Read with no limit -- its refusal written into the act`s refusal bank',
}

# ### b717's events: (row, the head's needle, the class); the tag and its NEW or REPEAT read from the row's own bracket
EVENTS = [
    (1, 'G-ROOTDRY-READY', 'FORM'),
    (2, 'G-DELETES-ONE-BRANCH', 'CONTROL'),
    (3, 'G-ARMS-NO-LIVE-LIMB', 'CONTROL'),
    (4, 'CARRIED_FAILING names two arms', 'FORM'),
    (5, 'THE SEAL REFUSED', 'ORDER'),
    (6, "THE RUNS ON b716'S BANKS", 'ORDER'),
    (7, "AT THE ROOT'S PROMPT", 'ORDER'),
    (8, 'G-ARM-SECONDS-BANKED', 'ORDER'),
    (9, 'G-KEYSTONE-EDITS FAILS', 'CONTROL'),
    (10, 'THE MANIFEST CONTROL NOT AS WANTED', 'CONTROL'),
]

# ### the five items: (key, what, its source checked, the seat's tag, NEW or the REPEAT's words, the class)
ITEMS = [
    ('A', 'the closing push capture data/b717_relay_push-b717-closing_push_out.txt left untracked by b717’s close',
     ('commit', 'STEPZERO', 'data/b717_relay_push-b717-closing_push_out.txt'), 'CLOSE',
     'REPEAT of b716, its close`s capture carried at b717`s step zero ((R327)(8), the named pair)', 'ORDER'),
    ('B', 'step row 19 of data/b717_steps.json (the closing, 248c5a97) left uncommitted by b717’s close',
     ('commit', 'STEPZERO_STEPS', 'data/b717_steps.json'), 'CLOSE',
     'REPEAT of b716, its step row 18 carried at b717`s step zero ((R327)(8), the named pair)', 'ORDER'),
    ('C', 'data/b717_bank_hashes.json as b717’s close left it, uncommitted',
     ('commit', 'STEPZERO_HASHES', 'data/b717_bank_hashes.json'), 'CLOSE',
     'REPEAT of b717 (k) (relay data/b717_defects.txt), b716`s hashes committed at b717`s step zero', 'ORDER'),
    ('D', 'tools/mirror_prevbuild.json as b717’s build left it (blob 53e58138, HEAD bc235618), uncommitted though b717’s closing :82 reads '
     '"committed with this closing"',
     ('commit', 'STEPZERO_PREVBUILD', 'tools/mirror_prevbuild.json'), 'CLOSE',
     'REPEAT of b716, whose step zero committed b715`s build file alone (relay 0fbfbf9e)', 'ORDER'),
    ('E', 'the hook’s refusal of a Read call with no limit after b717’s closing (data/b717_hook_refusals.txt :5, 19:51:46Z)',
     ('line', 'b717_hook_refusals.txt', 5, '19:51:46Z | READ | Read'), 'CLOSE',
     'REPEAT of b717 (v) (relay data/b717_defects.txt)', 'HOOK'),
]

# ### the two CLAIM items b717's counter carries
COUNTER_CLAIMS = ['p', 's']


def _event_rows(text):
    """the events bank's rows: {n: head}, a row a line opening four spaces and '(n) '; the head runs to the next row."""
    out, cur = {}, None
    for l in text.replace(chr(13), '').split(NL):
        m = re.match(r'^    \((\d+)\) (.*)$', l)
        if m:
            cur = int(m.group(1))
            out[cur] = m.group(2)
        elif cur is not None and l.startswith('     ') and not l.startswith('    ###'):
            out[cur] += ' ' + l.strip()
        else:
            cur = None
    return out


def _bracket(head):
    m = re.match(r"^THE SEAT'S \[(CLAIM|CLOSE) ; ([^\]]*)\]:", head)
    return (m.group(1), m.group(2)) if m else (None, None)


def _letter_rows(act):
    p = os.path.join(D, '%s_defects.txt' % act)
    t = C78.rd(p).replace(chr(13), '') if os.path.exists(p) else ''
    return dict((m.group(1), m.group(2)) for m in re.finditer(r"(?m)^\s{4}\(([a-z]'?)\) (.*)$", t))


def _event_ref_ok(col):
    """a REPEAT naming an act's event (n): that row present in the act's events bank."""
    m = re.match(r'^REPEAT (b\d+) event \((\d+)\)$', col)
    if not m:
        return True
    return int(m.group(2)) in _event_rows(C78.rd(os.path.join(D, '%s_events.txt' % m.group(1))))


def _item_ok(src):
    if src[0] == 'commit':
        sha = getattr(K, src[1], '')
        files = [x for x in REC.g(ROOT, 'show', '--name-only', '--format=', sha).split(NL) if x.strip()] if sha else []
        return files == [src[2]]
    _k, name, ln, needle = src
    L = C78.rd(os.path.join(D, name)).replace(chr(13), '').split(NL)
    return len(L) >= ln and needle in L[ln - 1]


def compose():
    ev = _event_rows(C78.rd(os.path.join(D, 'b717_events.txt')))
    miss_e = [n for n, h, _c in EVENTS if h not in ev.get(n, '')]
    tags = dict((n, _bracket(ev.get(n, ''))) for n, _h, _c in EVENTS)
    no_tag = [n for n, t in tags.items() if t[0] is None]
    bad_ref = [n for n, t in tags.items() if t[1] and not _event_ref_ok(t[1])]
    bad_item = [k for k, _w, src, _t, _r, _c in ITEMS if not _item_ok(src)]
    dl = _letter_rows('b717')
    claims = sorted(x for x, h in dl.items() if _bracket(h)[0] == 'CLAIM')
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', C78.rd(os.path.join(D, 'b675_corrigenda.txt')))]
    bad = [k for k, v in (('the ten event rows', sorted(ev) == list(range(1, 11))), ('each event`s head', not miss_e),
                          ('each event`s bracketed tag', not no_tag), ('each REPEAT`s cited event row', not bad_ref),
                          ('each item`s source', not bad_item), ('b717`s CLAIM letters (p), (s)', claims == COUNTER_CLAIMS),
                          ('the corrigenda bank`s last row (%d)' % CORRIGENDA_LAST, cr and max(cr) == CORRIGENDA_LAST)) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (events %s ; heads missed %s ; untagged %s ; refs %s ; items %s ; claims %s)' % (
            bad, sorted(ev), miss_e, no_tag, bad_ref, bad_item, claims))
    return dict(events=ev, tags=tags, letters=dl)


def _col(c):
    return 'NEW' if c == 'NEW' else c.replace('REPEAT ', 'REPEAT of ', 1)


def counts(s):
    t = [s['tags'][n][0] for n, _h, _c in EVENTS] + [i[3] for i in ITEMS]
    rep = sum(1 for n, _h, _c in EVENTS if s['tags'][n][1] != 'NEW') + sum(1 for i in ITEMS if i[4] != 'NEW')
    return t.count('CLAIM'), t.count('CLOSE'), rep, len(t)


def differences(s):
    d = ['(%d)' % n for n in NAVIGATOR_CLOSE if s['tags'][n][0] != 'CLOSE']
    d += ['item %s' % i[0] for i in ITEMS if i[3] != 'CLOSE']
    return d


def unread(s):
    return ['(%d)' % n for n, _h, _c in EVENTS if n not in NAVIGATOR_CLOSE]


def _entry_lines(s):
    nc, nl, rep, n = counts(s)
    diff = differences(s)
    L = ['*b717’s events bank (relay data/b717_events.txt) carries ten rows (1)-(10), entered after its lock and seal and not lettered, each '
         'tagged in its own bracket; b717’s close left five items uncommitted, each committed alone at b718’s step zero. Under (R328)(2) each '
         'item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the '
         'corpus meets, or CLOSE, where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. A '
         'CLOSE item is recorded and counted, its class gathered for the toolset’s v1.2.0. The navigator reads events (1), (2), (7), (8), (9), '
         '(10) and the five items as CLOSE; the seat’s tags differ from that reading at %s; events %s the navigator’s reading does not name, '
         'the seat’s tag standing.*' % ('no item' if not diff else ', '.join(diff), ', '.join(unread(s))), '',
         '**b717’s events:**', '']
    for k, h, c in EVENTS:
        t, r = s['tags'][k]
        L += ['**(%d) %s** (relay data/b717_events.txt, row (%d); %s; %s; class %s).' % (k, h, k, t, _col(r), c)]
    L += ['', '**The five items b717’s close left uncommitted:**', '']
    for key, what, src, t, r, c in ITEMS:
        where = ('committed alone at relay %s' % getattr(K, src[1])[:8]) if src[0] == 'commit' else 'relay data/%s :%d' % (src[1], src[2])
        L += ['**(%s) %s** (%s; %s; %s; class %s).' % (key, what, where, t, r, c)]
    L += ['', '**The CLOSE classes for the toolset’s v1.2.0** (b718’s, (R328)(6)):', '']
    for k, v in CLASSES.items():
        ev = ['(%d)' % e[0] for e in EVENTS if e[2] == k]
        it = ['(%s)' % i[0] for i in ITEMS if i[5] == k]
        L += ['- **%s** -- %s: events %s; items %s.' % (k, v, ', '.join(ev) or 'none', ', '.join(it) or 'none')]
    pl = _letter_rows('b717')
    L += ['', '**The counter:** CLAIM %d, CLOSE %d over the %d items (ten events, five items); REPEAT %d of %d. The two CLAIM items b717’s '
          'counter carries (CLAIM 2, data/b717_closing.txt :5) are its defects (%s) and (%s) (relay data/b717_defects.txt): %s; and %s.' % (
              nc, nl, n, rep, n, COUNTER_CLAIMS[0], COUNTER_CLAIMS[1], _claim_head(pl['p']), _claim_head(pl['s'])), '',
          ('*Filed at b718 on the author’s ruling `(R328)`(2): generated by relay `tools/b718_corrigendum.py`, written whole at b718, from '
           'b717’s events bank read unedited and the five items’ commits at b718’s step zero; banked as relay `data/b718_corrigendum.txt`, the '
           'corrigenda bank `data/b675_corrigenda.txt` appended at row (38). It answers b717’s record; no sealed tool, face, trail or root-named '
           'bank of b717 is edited.*')]
    return L


def _claim_head(h):
    """a CLAIM letter's first clause: the bracket dropped, cut at its first semicolon after the time."""
    body = re.sub(r"^THE SEAT'S \[[^\]]*\]: ", '', h)
    return body.split('; ')[0].rstrip('.')


def entry_text(s):
    return NL + TITLE + NL + NL + NL.join(_entry_lines(s)) + NL


ROW = ('  (38) b717\'s record (relay data/b717_events.txt, rows (1)-(10), and the five items its close left uncommitted): every item tagged\n'
       '      CLAIM or CLOSE under (R327)(2) and NEW or REPEAT; CLAIM %d, CLOSE %d, by class for v1.2.0 (FORM, CONTROL, ORDER, HOOK); REPEAT\n'
       '      %d of %d; b717`s counter`s two CLAIM items its defects (p) and (s); the navigator`s reading and the seat`s differ at %s.\n'
       '      THE CORRECTION: FINDINGS :%s, relay data/b718_corrigendum.txt.')


def _row_text(s, ln):
    nc, nl, rep, n = counts(s)
    d = differences(s)
    return ROW % (nc, nl, rep, n, 'no item' if not d else ', '.join(d), ln)


def bank_lines(s, landed_line=None):
    nc, nl, rep, n = counts(s)
    L = ['b718 -- THE CORRIGENDUM ENTRY FOR b717`S EVENTS AND THE FIVE ITEMS, (R328)(2) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the figures read before the write: the event rows %d, each tagged in its bracket ; every REPEAT`s cited event row found ; the five '
         'items` sources found ; b717`s CLAIM letters %s ; the corrigenda bank`s last row (%d).' % (len(s['events']), COUNTER_CLAIMS, CORRIGENDA_LAST),
         '### THE NAVIGATOR`S READING AND THE SEAT`S: events (1), (2), (7), (8), (9), (10) and the five items CLOSE by the navigator ; the seat`s '
         'differences %s ; not named by the navigator %s.' % (differences(s) or 'NONE', ', '.join(unread(s))), '']
    L += ['  ' + l for l in _entry_lines(s)]
    L += ['', '### ### **ITEMS %d: EVENTS 10, ITEMS 5 ; CLAIM %d, CLOSE %d ; REPEAT %d, NEW %d ; THE EVENTS BANK UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
        n, nc, nl, rep, n - rep, landed_line if landed_line else 'NOT YET WRITTEN')]
    return L


def _put(name, data):
    import act_membrane as MEM
    p = os.path.join(D, name)
    MEM.guard_path('b718', p, REC.R.ROOT_EXCLUDE)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data.encode('utf-8'))
    os.replace(p + '.tmp', p)


def main(route):
    s = compose()
    text = entry_text(s)
    if route == 'dry':
        REC.R.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        print(_row_text(s, 'NOT YET WRITTEN'))
        return
    if route == 'write':
        REC.land([('FINDINGS.md', TITLE, text)], 'b718_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
        ln = (REC.jl('b718_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    else:
        sys.exit('usage: b718_corrigendum.py dry | write')
    L = bank_lines(s, ln)
    _put('b718_corrigendum.txt', NL.join(L) + NL)
    nc, nl, rep, n = counts(s)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, claim=nc, close=nl, repeat=rep, items=n,
             events=[dict(row=e[0], tag=s['tags'][e[0]][0], column=s['tags'][e[0]][1], cls=e[2]) for e in EVENTS],
             items_uncommitted=[dict(key=i[0], what=i[1], tag=i[3], column=i[4], cls=i[5]) for i in ITEMS],
             counter_claims=COUNTER_CLAIMS, classes=CLASSES, differences=differences(s), row=38)
    _put('b718_corrigendum.json', json.dumps(j, indent=1, ensure_ascii=False) + NL)
    print(L[-1])
    print(_row_text(s, ln))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'dry')
