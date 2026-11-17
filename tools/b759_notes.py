# -*- coding: utf-8 -*-
"""tools/b759_notes.py -- (R369)(8), WHERE ELSE IT IS WRITTEN: "REGISTRY gains one row for the document, numbered by the ledger's own rule
after 1.5c-23, its status "REVIEW; entered at v0.2 by b759; not deposited", no cell blank, the row conferring no grade, and one dated note at
the file's end giving v0.41 with its peel where it was cut and closing "The tags confer no deposit."; FACES_LEDGER.md and
THE_KEYSTONE_CENSUS_v0_8_3.md each take one dated note at the file's end, made of the document's own dated head and the sentences of (5) and
(8) that came true" (data/b759_ferry.txt :27). Written whole at b759's Component 5 in the form of tools/b758_notes.py (append, insert, controls,
write); committed before it runs; one PLACE-papers commit an item, through the one-call tool, after the document's own commit.

THE SOURCES, each read at its repository's HEAD: (5)'s sentence from data/b759_outcomes.json (LANDED or NOTHING LANDED; SHOWN refuses); (8)'s
sentence from data/b759_compose.txt, the line under its head; the document's dated head, v0.2 :3 at PLACE-papers HEAD (the document committed
first); the tag and its peel read again from the gated push's capture (tools/b759_outcomes.py's tag reader) and equal to the outcomes bank's.

THE ITEMS:
  reg     REGISTRY.md: the row, its ID from tools/standing/rowid.py's rule (the file's maximum over every table of the prefix, plus one),
          inserted after the row 1.5c-23 (read once by its ID); one dated note appended at the file's end to the row and the kernel row
  faces   FACES_LEDGER.md: one UPDATE section appended at the file's end in b758's form
  census  phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md: one note appended at the file's end in b758's form
PLACE-papers' own lines are read by digest; the composed lines are this act's and are printed whole before the write.
MODES  control | dry <item|all> | write <item>      BANK data/b759_notes.json (a row an item, written at its write)
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b759_worklist as K     # noqa: E402
import b759_outcomes as OC    # noqa: E402  (the tag reader, as committed)
import rowid as RID           # noqa: E402

ACT = 'b759'
PP = K.PP
NL = '\n'
OUTJ = 'data/b759_outcomes.json'
COMPOSE = 'data/b759_compose.txt'
CAP = 'data/b759_SIDE-explicit-formula_push-b759-weil_push_out.txt'
V02 = K.PP_NEW[0]
BANK = os.path.join(RELAY, 'data', 'b759_notes.json')
ITEMS = {'reg': 'REGISTRY.md', 'faces': 'FACES_LEDGER.md', 'census': 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'}
ORDER = ('reg', 'faces', 'census')
AFTER_ID = '1.5c-23'
KERNEL_ROW = '| **`SIDE-explicit-formula`**'
S8_HEAD = '## THE SENTENCE OF (8), ITS FIELDS FILLED'


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a, raw=False):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, (r.stdout if raw else r.stdout.decode('utf-8', 'replace'))


def digest(s):
    return hashlib.sha256(s if isinstance(s, bytes) else s.encode('utf-8')).hexdigest()[:16]


def relay_head(rel):
    rc, out = git(RELAY, 'show', 'HEAD:%s' % rel)
    if rc:
        raise SystemExit('### %s NOT READ AT RELAY HEAD -- NOTHING DONE' % rel)
    return out.replace('\r', '')


# ### ---------------------------------------------------------------- the sources
def sentence8(text):
    L = text.split(NL)
    i = [k for k, l in enumerate(L) if l == S8_HEAD]
    if len(i) != 1 or i[0] + 1 >= len(L) or not L[i[0] + 1].startswith('  '):
        return None
    return L[i[0] + 1].strip()


def title_of(line):
    t = line.lstrip('#').strip()
    small = ('at', 'of', 'the', 'and', 'in', 'on')
    w = t.split()
    return ' '.join(x.capitalize() if (k == 0 or x.lower() not in small) and x.isalpha() else (x.lower() if x.isalpha() else x) for k, x in enumerate(w))


def tag_sentence(tg):
    if not tg:
        return 'No tag was cut at b759 (relay data/b759_outcomes.txt).'
    t, obj, peel = tg
    return 'The new tag, read back from the remote: SIDE-explicit-formula `%s` (tag object `%s`), whose peel reads `%s` (relay %s).' % (t, obj[:8], peel, CAP)


def sources():
    rec = json.loads(relay_head(OUTJ))[0]
    oc = rec.get('outcome') or ''
    if not (oc.startswith('LANDED') or oc == 'NOTHING LANDED') or not rec.get('sentence'):
        raise SystemExit('### (5)`S OUTCOME READS %r: NO SENTENCE CAME TRUE YET -- NOTHING DONE' % oc)
    s8 = sentence8(relay_head(COMPOSE))
    if not s8 or '<' in s8:
        raise SystemExit('### (8)`S SENTENCE NOT READ, OR A FIELD LEFT, IN data/b759_compose.txt AT RELAY HEAD -- NOTHING DONE')
    rc, v2 = git(PP, 'show', 'HEAD:%s' % V02)
    v2l = v2.replace('\r', '').split(NL)
    if rc or len(v2l) < 3 or not (v2l[2].startswith('*v0.2, ') and v2l[2].endswith('*')):
        raise SystemExit('### THE DOCUMENT`S DATED HEAD NOT READ AT PLACE-papers HEAD (commit v0.2 first) -- NOTHING DONE')
    tg = None
    if oc.startswith('LANDED'):
        peel, obj = OC.tag_read(relay_head(CAP), rec.get('tag'))
        if not peel or peel != rec.get('peel') or obj != rec.get('tag_object'):
            raise SystemExit('### THE CAPTURE AT RELAY HEAD DOES NOT READ THE OUTCOMES BANK`S TAG -- NOTHING DONE')
        tg = (rec['tag'], obj, peel)
    return dict(s5=rec['sentence'], s8=s8, head=v2l[2], title=title_of(v2l[0]), words=len(v2.split()), tag=tg, outcome=oc)


# ### ---------------------------------------------------------------- the bytes
def check_lf(data):
    if b'\r' in data:
        raise SystemExit('### THE FILE CARRIES A CARRIAGE RETURN -- NOTHING WRITTEN')
    if not data.endswith(b'\n'):
        raise SystemExit('### THE FILE DOES NOT END WITH A LINE END -- NOTHING WRITTEN')


def append_lines(data, lines):
    """the lines appended after one blank line each, at the end of an LF file ending with a line end."""
    check_lf(data)
    for s in lines:
        if NL in s or '\r' in s or not s.strip():
            raise SystemExit('### A COMPOSED LINE CARRIES A LINE BREAK OR IS EMPTY -- NOTHING WRITTEN')
    return data + ''.join(NL + s + NL for s in lines).encode('utf-8')


def insert_after_id(data, rid, row):
    """the row inserted after the one table line whose first cell is rid; (new data, the line it takes)."""
    check_lf(data)
    L = data.decode('utf-8').split(NL)
    at = [k for k, l in enumerate(L) if re.match(r'^\|\s*%s\s*\|' % re.escape(rid), l)]
    if len(at) != 1:
        raise SystemExit('### THE ROW %s STANDS %d TIMES, NOT ONCE -- NOTHING WRITTEN' % (rid, len(at)))
    L.insert(at[0] + 1, row)
    return NL.join(L).encode('utf-8'), at[0] + 2


# ### ---------------------------------------------------------------- the composed lines
def compose(k, data, S, date):
    """(new data, [(line, text)], notes) for item k."""
    if k == 'reg':
        text = data.decode('utf-8')
        rid = RID.next_id(text, '1.5c')
        if rid in [i for _l, i, _p, _n in RID.rows(text)]:
            raise SystemExit('### THE ID %s IS HELD ALREADY -- NOTHING WRITTEN' % rid)
        row = '| %s | %s | `%s` | v0.2 | — (no grade conferred) | REVIEW; entered at v0.2 by b759; not deposited | %s |' % (
            rid, S['title'], V02, '{:,}'.format(S['words']))
        d1, rl = insert_after_id(data, AFTER_ID, row)
        L1 = d1.decode('utf-8').split(NL)
        kr = [i + 1 for i, l in enumerate(L1) if l.startswith(KERNEL_ROW)]
        if len(kr) != 1:
            raise SystemExit('### THE KERNEL ROW STANDS %d TIMES, NOT ONCE -- NOTHING WRITTEN' % len(kr))
        note = ("*Dated note, b759, %s, under the author's ruling `(R369)`(8), to the row %s (:%d) and the kernel row at :%d: the row enters "
                "THE_EPSTEIN_CONTROL_OBJECT at v0.2 (`%s`), v0.1 standing beside it unchanged, and confers no grade. %s No cell of the kernel row "
                "and no other row is edited. The tags confer no deposit.*") % (date, rid, rl, kr[0], V02, tag_sentence(S['tag']))
        d2 = append_lines(d1, [note])
        n2 = d2.decode('utf-8').split(NL)
        return d2, [(rl, row), (len(n2) - 1, note)], dict(id=rid, row_line=rl, kernel_row=kr[0])
    if k == 'faces':
        L = data.decode('utf-8').split(NL)
        prev = [i + 1 for i, l in enumerate(L) if l.startswith('## UPDATE — filed ') and '(b758)' in l]
        if len(prev) != 1:
            raise SystemExit('### b758`S UPDATE SECTION NOT READ ONCE -- NOTHING WRITTEN')
        lines = ['## UPDATE — filed %s (b759): the Epstein document at v0.2, under the author’s ruling (R369)(8)' % date,
                 '*Rows above are never rewritten; this update names no earlier row and edits none. Written by relay `tools/b759_notes.py` under the '
                 'author’s ruling (R369)(8), in the form of b758’s section (:%d): the document’s own dated head, then the sentences of (R369)(5) and (8) '
                 'that came true, in that order, each the ruling’s text with its fields filled from the act’s banks (relay `data/b759_outcomes.txt`, '
                 '`data/b759_compose.txt`). No face is entered and no grade is conferred by this update.*' % prev[0],
                 S['head'], S['s5'], S['s8'], '*The rows above are unedited. Filed by b759 (relay `data/b759_notes.json`).*']
        d = append_lines(data, lines)
        n = len(L)
        return d, [(n + 1 + 2 * j, s) for j, s in enumerate(lines)], dict(after=prev[0])
    if k == 'census':
        L = data.decode('utf-8').split(NL)
        note = ("*Appended %s by b759 under the author's ruling `(R369)`(8):* THE_EPSTEIN_CONTROL_OBJECT stands at v0.2 (`%s`), its dated head "
                "reading “%s” %s %s No byte above this line changes.") % (date, V02, S['head'].strip('*'), S['s5'], S['s8'])
        d = append_lines(data, [note])
        return d, [(len(L) + 1, note)], {}
    raise SystemExit('### NO ITEM %r' % k)


# ### ---------------------------------------------------------------- the controls
def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    pl = b'| ID | T |\n|:--|:--|\n| 1.5c-22 | a |\n| 1.5c-23 | b |\n\n## next\n'
    d, at = insert_after_id(pl, '1.5c-23', '| 1.5c-24 | c |')
    c('the row inserted after its predecessor`s ID, read once', (at, d.decode().split(NL)[3:5]), at == 5 and d.decode().split(NL)[4] == '| 1.5c-24 | c |')
    try:
        insert_after_id(pl + b'| 1.5c-23 | again |\n', '1.5c-23', 'x')
        twice = 'WRITTEN'
    except SystemExit:
        twice = 'REFUSED'
    c('a predecessor ID standing twice refused', twice, twice == 'REFUSED')
    a = append_lines(b'x\n', ['*n*'])
    try:
        append_lines(b'x', ['*n*'])
        noend = 'WRITTEN'
    except SystemExit:
        noend = 'REFUSED'
    c('an append: one blank line then the note; a file with no final line end refused', (a, noend), a == b'x\n\n*n*\n' and noend == 'REFUSED')
    c('the title from the document`s heading', title_of('# THE EPSTEIN CONTROL OBJECT AT DISCRIMINANT −23'),
      title_of('# THE EPSTEIN CONTROL OBJECT AT DISCRIMINANT −23') == 'The Epstein Control Object at Discriminant −23')
    c('the tag sentence, cut and not cut', (tag_sentence(('v9', 'a' * 40, 'b' * 40))[:60], tag_sentence(None)),
      '`v9` (tag object `aaaaaaaa`), whose peel reads `%s`' % ('b' * 40) in tag_sentence(('v9', 'a' * 40, 'b' * 40))
      and tag_sentence(None).startswith('No tag was cut'))
    s8 = sentence8('x\n%s\n  THE_EPSTEIN stands.\n' % S8_HEAD)
    c('(8)`s sentence read under its head; absent None', (s8, sentence8('x\n')), s8 == 'THE_EPSTEIN stands.' and sentence8('x\n') is None)
    c('the ID by the file`s maximum over every table', RID.next_id('| 1.5c-23 | a |\n| 1.5c-30 | b |\n', '1.5c'), RID.next_id('| 1.5c-23 | a |\n| 1.5c-30 | b |\n', '1.5c') == '1.5c-31')
    return L, ok


def load():
    return json.load(io.open(BANK, encoding='utf-8')) if os.path.exists(BANK) else []


def main(argv):
    if argv[:1] == ['control']:
        L, ok = controls()
        print(NL.join(L))
        print('### CONTROLS %d OF %d AS WANTED' % (sum(ok), len(ok)))
        return
    if len(argv) != 2 or argv[0] not in ('dry', 'write') or argv[1] not in ORDER + ('all',) or (argv[0] == 'write' and argv[1] == 'all'):
        sys.exit(__doc__)
    L, ok = controls()
    if not all(ok):
        print(NL.join(L))
        sys.exit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    S = sources()
    date = time.strftime('%Y-%m-%d', time.gmtime())
    print('  THE SOURCES: (5) %s, %d characters ; (8) %d characters ; the head %s ; the tag %s ; the document %s words' % (
        S['outcome'], len(S['s5']), len(S['s8']), digest(S['head']), S['tag'][0] if S['tag'] else 'NONE', S['words']))
    R = load()
    for k in (ORDER if argv[1] == 'all' else (argv[1],)):
        rel = ITEMS[k]
        p = os.path.join(PP, *rel.split('/'))
        rc, hb = git(PP, 'show', 'HEAD:%s' % rel, raw=True)
        wb = open(p, 'rb').read()
        if rc or hb != wb:
            sys.exit('### %s: THE WORKING COPY IS NOT HEAD`S BLOB -- NOTHING DONE' % rel)
        if argv[0] == 'write' and any(r.get('item') == k for r in R):
            sys.exit('### %s WRITTEN ALREADY (data/b759_notes.json) -- NOTHING DONE' % k)
        if argv[0] == 'write' and k != 'reg' and not any(r.get('item') == ORDER[ORDER.index(k) - 1] for r in R):
            sys.exit('### THE ITEM BEFORE %s NOT WRITTEN -- one at a time, in order -- NOTHING DONE' % k)
        d, rows, notes = compose(k, hb, S, date)
        print('## %s (%s): HEAD sha256 %s, %d bytes -> %d bytes, sha256 %s ; %s' % (k, rel, digest(hb), len(hb), len(d), digest(d), notes))
        for ln, s in rows:
            print('  :%d %s' % (ln, s))
        if argv[0] == 'write':
            with open(p, 'wb') as fh:
                fh.write(d)
            back = open(p, 'rb').read()
            print('  written ; read back %s' % ('EQUAL' if back == d else 'NOT EQUAL'))
            R.append(dict(item=k, file=rel, at=stamp(), head_sha=digest(hb), new_sha=digest(back), bytes=len(back), lines=[[ln, s] for ln, s in rows],
                          notes=notes, read_back=back == d))
            js = json.dumps(R, indent=1, ensure_ascii=False)
            with open(BANK + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
                fh.write(js + NL)
            os.replace(BANK + '.tmp', BANK)
            print('  banked data/b759_notes.json (%d rows)' % len(R))


if __name__ == '__main__':
    main(sys.argv[1:])
