# -*- coding: utf-8 -*-
"""b758, (R368)(8): WHERE THE SENTENCES GO. "each by one PLACE-papers commit through the one-call tool. One dated note, made of the document's
own dated head and the sentences of (4) and (5) that came true, is added to each of: THE_EPSTEIN_CONTROL_OBJECT_v0_1.md, after its latest dated
note; FACES_LEDGER.md, at the file's end; THE_KEYSTONE_CENSUS_v0_8_3.md, at the file's end; REGISTRY.md, at the file's end, to the rows 1.5c-21
to 1.5c-23 and the kernel row, giving each tag with its peel and closing "The tags confer no deposit."" (data/b758_ferry.txt :23). Written whole
by the Write tool at b758's Component 5, carried in form from tools/b757_notes.py (append, insert, controls, write, confirm); committed before
it runs.

THE SENTENCES: each read from data/b758_outcomes.json at relay HEAD (the bank composed by the committed tools/b758_outcomes.py), the items whose
outcome is LANDED or BROKE, in the order (4), (5); each matched whole against the ruling's template for that outcome, cut from the ferry at relay
HEAD after its marker to the next quotation mark, each <field> filled, the run id equal to the item's run and the peel to the tag's. An item
SHOWN and not landed refuses every write. Nothing in a sentence is changed by this tool. Each tag with its peel and tag object read again from
the gated push's capture at relay HEAD.

THE PLACES, in each document's own dated form (b757's five):
  (a) THE_EPSTEIN_CONTROL_OBJECT_v0_1.md: inserted after its latest dated note (b757's at :17, the seven at :5 to :17 two apart) with a blank line
  (b) FACES_LEDGER.md: one UPDATE section appended at the file's end in b757's form (heading, italic preamble, the sentences, italic closing)
  (c) THE_KEYSTONE_CENSUS_v0_8_3.md: one note appended at the file's end in b757's form
  (d) REGISTRY.md: one dated note appended at the file's end to the rows 1.5c-21 to 1.5c-23 (:177-:179, each read by its ID) and the kernel row
      (:924, read to name SIDE-explicit-formula), each tag with its peel, closing "The tags confer no deposit."
  (e) OPEN_TRAILS.md, "appended under one dated head, no line moving: b757's root answer; the two lines the seat resolved at b757 stand as
      written, the author having struck neither; W-ORD-SQUARES-AT-24 takes its price": the head; b757's root answer, the author's word quoted
      whole from relay data/b757_author_answers.txt :20; the two lines (:18493, :18503) read at HEAD by b757's notes bank's digests and named as
      standing; the price cut from the ruling's line.

THE MOVED CITES ((8)): "The relay's lines whose cites b757's Epstein note moved, 123 by the seat's count, are read by the citation tool against
the document at HEAD, and each that no longer resolves is printed; none is edited by hand." The 123 rows are b757's notes bank's (items (a)
`moved_cites`, repo relay); each relay line read at relay HEAD by its digest; each moved cite read by the citation tool's own helpers
(b758_citation: _blob, at, first): the document's line at that number at b757's write's HEAD (3e85e952) against the line at that number at
PLACE-papers HEAD; a cite resolves where the two are equal and the line is not blank; each that does not is printed with where its line now
stands. Banked as data/b758_moved_cites.txt.

THE ORDER: (a) to (e), one at a time; a write is refused until the item before it is confirmed. The withheld kinds are tools/b754_doors.py's,
none of them printed. The bank carries digests and line numbers alone for PLACE-papers' lines; the composed lines are this act's own, printed
whole before the write.
MODES  controls | moved [--bank] | dry <item|all> | write <item> | confirm <item>      BANK data/b758_notes.json; data/b758_moved_cites.txt
"""
import hashlib
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
import b754_doors as DOORS   # noqa: E402
import b758_outcomes as OC   # noqa: E402  (the tag reader, as committed)
import figbank as FB         # noqa: E402

ACT = 'b758'
PP = DOORS.PP
FERRY = 'data/b758_ferry.txt'
OUTJ = 'data/b758_outcomes.json'
B757_NOTES = 'data/b757_notes.json'
B757_ANSWERS = 'data/b757_author_answers.txt'
BANK = os.path.join(RELAY, 'data', '%s_notes.json' % ACT)
MOVED = os.path.join(RELAY, 'data', '%s_moved_cites.txt' % ACT)
NL = '\n'
ORDER = ('a', 'b', 'c', 'd', 'e')
EPS = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
ITEMS = {
    'a': {'rel': EPS, 'how': 'insert', 'after': 17, 'present': '*Dated note, %s, b758'},
    'b': {'rel': 'FACES_LEDGER.md', 'how': 'section', 'present': '## UPDATE — filed %s (b758)'},
    'c': {'rel': 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md', 'how': 'append', 'present': '*Appended %s by b758'},
    'd': {'rel': 'REGISTRY.md', 'how': 'append', 'present': '*Dated note, b758, %s'},
    'e': {'rel': 'OPEN_TRAILS.md', 'how': 'trail', 'present': '**Dated head, %s, b758, `(R368)`(8)'},
}
EPS_NOTE_LINES = (5, 7, 9, 11, 13, 15, 17)
EPS_LAST_NEEDLE = '*Dated note, 2026-11-16, b757,'
# ### the clauses' sentences: (item key, the ferry's line, {outcome: the template's marker})
SECTIONS = (('join', 15, {'LANDED': 'THE SENTENCE IF IT COMPILES: "', 'BROKE': 'THE SENTENCE IF IT DOES NOT: "'}),
            ('coeff', 17, {'LANDED': 'THE SENTENCE IF IT COMPILES, one for the three: "', 'BROKE': 'THE SENTENCE IF IT DOES NOT: "'}))
FIELDS = ('peel', 'run id', 'n', 'module', 'line', 'where')
FIELD_RX = re.compile(r'<(%s)>' % '|'.join(re.escape(f) for f in FIELDS))
REG_ROWS = ((177, '1.5c-21'), (178, '1.5c-22'), (179, '1.5c-23'))
REG_KERNEL = 924
OT_TRAIL, OT_NEXT = 18507, 18555          # ### b757's trail head and its Next line, the file's last
OT_TRAIL_NEEDLE = '### b757 — lane two'
OT_NEXT_NEEDLE = '**Next:**'
OT_RESOLVED = ((18493, '`W-ORD-KEIPER-FACE`'), (18503, '`W-ORD-SQUARES-AT-24`'))
ANSWER_LINE, ANSWER_RESULT = 20, 17
ANSWER_HEAD = '### THE AUTHOR`S WORD (transcript line 110465), BEGIN to END, verbatim:'
B757_PP_HEAD = '3e85e952'          # ### the PLACE-papers HEAD of b757's (a) write, its notes bank's items (a) pp_head


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout


def gitb(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def bdigest(b):
    return hashlib.sha256(b).hexdigest()[:16]


def at_head(rel, need=1):
    rc, out = git(RELAY, 'show', 'HEAD:%s' % rel)
    L = out.replace('\r', '').split(NL)
    if rc or len(L) < need:
        raise SystemExit('### %s NOT READ AT RELAY HEAD -- NOTHING DONE' % rel)
    return L


# ### ---------------------------------------------------------------- the sentences and their templates (b757's readers, carried)
def template(line, marker):
    if line.count(marker) != 1:
        raise SystemExit('### THE MARKER %r STANDS %d TIMES ON THE RULING`S LINE, NOT ONCE -- NOTHING DONE' % (marker, line.count(marker)))
    a = line.index(marker) + len(marker)
    if '"' not in line[a:]:
        raise SystemExit('### THE TEMPLATE AFTER %r HAS NO CLOSING QUOTATION MARK -- NOTHING DONE' % marker)
    t = line[a:line.index('"', a)]
    if not t:
        raise SystemExit('### THE TEMPLATE AFTER %r IS EMPTY -- NOTHING DONE' % marker)
    return t


def tregex(t):
    out, pos, names = [], 0, []
    for m in FIELD_RX.finditer(t):
        out.append(re.escape(t[pos:m.start()]))
        out.append('(.+?)')
        names.append(m.group(1))
        pos = m.end()
    out.append(re.escape(t[pos:]))
    return re.compile(''.join(out) + r'\Z', re.S), names


def fill(t, s):
    """[(field, value)] where `s` is the template `t` with its fields filled; None where it is not."""
    rx, names = tregex(t)
    m = rx.match(s or '')
    if not m:
        return None
    vals = list(zip(names, m.groups()))
    if any(not v.strip() or '<' in v or '>' in v for _n, v in vals):
        return None
    return vals


def sentences(recs=None, F=None):
    """[dict(key, sentence, template, outcome, fields, run, tag, peel, tag_object)] of the items whose outcome came true, (4) then (5)."""
    recs = recs if recs is not None else json.loads(NL.join(at_head(OUTJ)))
    F = F if F is not None else at_head(FERRY, 30)
    by = dict((r.get('item'), r) for r in recs)
    out = []
    for k, fl, markers in SECTIONS:
        r = by.get(k) or {}
        w = r.get('outcome')
        if w == 'SHOWN':
            raise SystemExit('### (%s): THE RUN SHOWN AND NOT LANDED -- the gated push first -- NOTHING DONE' % k)
        if w not in markers:
            continue
        t = template(F[fl - 1], markers[w])
        vals = fill(t, r.get('sentence'))
        if vals is None:
            raise SystemExit('### (%s): THE SENTENCE IS NOT THE RULING`S TEMPLATE WITH ITS FIELDS FILLED -- NOTHING DONE' % k)
        v = dict(vals)
        if v.get('run id') != str(r.get('run')) or ('peel' in v and v['peel'] != (r.get('peel') or '')[:8]):
            raise SystemExit('### (%s): THE SENTENCE`S RUN OR PEEL IS NOT ITS ITEM`S -- NOTHING DONE' % k)
        out.append(dict(key=k, sentence=r['sentence'], template=t, outcome=w, fields=vals, run=r.get('run'), tag=r.get('tag'),
                        peel=r.get('peel'), tag_object=r.get('tag_object'), fline=fl))
    if not out:
        raise SystemExit('### NO SENTENCE OF (4) OR (5) CAME TRUE IN THE OUTCOMES BANK -- NOTHING DONE')
    return out


def tags(S):
    """[(tag, tag object, peel, capture)] of the items LANDED, each read again from its capture at relay HEAD."""
    out = []
    for s in S:
        if s['outcome'] != 'LANDED':
            continue
        br = [x for x in OC.ITEMS if x[0] == s['key']][0][3]
        cap = 'data/%s_%s_%s_push_out.txt' % (ACT, OC.EFKEY, br)
        peel, obj = OC.tag_read(NL.join(at_head(cap)), s['tag'])
        if not peel or peel != s['peel']:
            raise SystemExit('### %s: THE CAPTURE AT RELAY HEAD DOES NOT READ THE PEEL THE OUTCOMES BANK GIVES -- NOTHING DONE' % s['tag'])
        out.append((s['tag'], obj, peel, cap))
    return out


# ### ---------------------------------------------------------------- the composed lines
def body(S):
    return ' '.join(s['sentence'] for s in S)


def note_a(S, date):
    return '*Dated note, %s, b758, under the author’s ruling `(R368)`(8): %s*' % (date, body(S))


def section_b(S, date):
    return ['## UPDATE — filed %s (b758): the landing at the Epstein control, under the author’s ruling (R368)(8)' % date,
            '*Rows above are never rewritten; this update names no earlier row and edits none. Written by relay `tools/b758_notes.py` under the '
            'author’s ruling (R368)(8), in the form of b757’s section (:551): the sentences of (R368)(4) and (5) that came true, in that order, each '
            'the ruling’s text with its fields filled from the act’s banks (relay `data/b758_outcomes.txt`). No face is entered and no grade is '
            'conferred by this update.*'] + [s['sentence'] for s in S] + ['*The rows above are unedited. Filed by b758 (relay `data/b758_notes.json`).*']


def note_c(S, date):
    return "*Appended %s by b758 under the author's ruling `(R368)`(8):* %s No byte above this line changes." % (date, body(S))


def note_d(S, date, TG=None):
    TG = TG if TG is not None else tags(S)
    if TG:
        tg = 'The new tags, each read back from the remote: %s.' % '; '.join(
            'SIDE-explicit-formula `%s` (tag object `%s`), whose peel reads `%s` (relay %s)' % (t, o[:8], p, c) for t, o, p, c in TG)
    else:
        tg = 'No tag was cut at b758 (relay data/b758_outcomes.txt).'
    return ("*Dated note, b758, %s, under the author's ruling `(R368)`(8), to the rows 1.5c-21, 1.5c-22 and 1.5c-23 (:177-:179) and the "
            "kernel row at :924: %s %s No cell of the four rows and no other row is edited. The tags confer no deposit.*") % (date, body(S), tg)


def ferry23(F):
    s = F[22]
    if not s.startswith('(8) WHERE THE SENTENCES GO'):
        raise SystemExit('### THE RULING`S LINE :23 IS NOT (8) -- NOTHING DONE')
    return s


def price_words(F):
    s = ferry23(F)
    k = 'W-ORD-SQUARES-AT-24 takes its price, "'
    if s.count(k) != 1:
        raise SystemExit('### (8)`S PRICE NOT READ ONCE -- NOTHING DONE')
    a = s.index(k) + len(k)
    return s[a:s.index('"', a)]


def answer_word():
    """the author's word of b757's root answer, relay data/b757_author_answers.txt :20 under its head at :19, quoted whole."""
    A = at_head(B757_ANSWERS, ANSWER_LINE)
    if A[ANSWER_LINE - 2] != ANSWER_HEAD or not A[ANSWER_LINE - 1].startswith('b758 lands what b757 compiled, then writes.') \
            or not A[ANSWER_RESULT - 1].startswith('RESULT (transcript line 110465, 2026-11-16T19:59:46.354Z): '):
        raise SystemExit('### %s :%d IS NOT THE ROOT`S WORD AS READ -- NOTHING DONE' % (B757_ANSWERS, ANSWER_LINE))
    return A[ANSWER_LINE - 1]


def trail_lines(F, date):
    pr, word = price_words(F), answer_word()
    head = ('**Dated head, %s, b758, `(R368)`(8): the lines the ruling orders for OPEN_TRAILS** (relay data/b758_ferry.txt :23), appended at '
            'the end of the file after b757’s trail (its last line :%d) and before this act’s own trail, so that no line of the trail moves: '
            'b757’s root answer; the two lines the seat resolved at b757, standing as written; and the price of `W-ORD-SQUARES-AT-24`.') % (date, OT_NEXT)
    one = ('*Appended %s by b758 to b757’s trail (:%d), under `(R368)`(8):* b757’s one question at the root was answered by the author’s word '
           '(relay data/b757_author_answers.txt :%d, :%d, 2026-11-16T19:59:46Z), quoted whole: “%s”') % (date, OT_TRAIL, ANSWER_RESULT, ANSWER_LINE, word)
    two = ('The two lines the seat resolved at b757 for the author’s strike, :%d (`W-ORD-KEIPER-FACE`, the ruling’s words beside the join’s '
           'outcome) and :%d (`W-ORD-SQUARES-AT-24`, its price read as none banked), stand as written, the author having struck neither '
           '(`(R368)`(8); relay data/b757_events.txt (26)).') % (OT_RESOLVED[0][0], OT_RESOLVED[1][0])
    sq = '`W-ORD-SQUARES-AT-24` takes its price under `(R368)`(8), in the ruling’s words: “%s”' % pr
    return [head, one, two, sq], dict(price=pr, word=word)


# ### ---------------------------------------------------------------- the bytes (b757's, carried)
def eol_of(data):
    cr, crlf = data.count(b'\r'), data.count(b'\r\n')
    if cr == 0:
        return b'\n'
    if cr == crlf == data.count(b'\n'):
        return b'\r\n'
    raise SystemExit('### THE FILE MIXES LINE ENDINGS -- NOTHING WRITTEN')


def count_lines(data, eol):
    parts = data.split(eol)
    return len(parts) - (1 if parts[-1] == b'' else 0)


def check_lines(lines):
    for s in lines:
        if '\n' in s or '\r' in s or not s.strip():
            raise SystemExit('### A LINE CARRIES A LINE BREAK OR IS EMPTY -- NOTHING WRITTEN')


def append_block(data, lines):
    eol = eol_of(data)
    if not data.endswith(eol):
        raise SystemExit('### THE FILE DOES NOT END WITH A NEWLINE -- NOTHING WRITTEN')
    check_lines(lines)
    n0 = count_lines(data, eol)
    lead = data.endswith(eol + eol)
    out, nums, n = data, [], n0
    for i, s in enumerate(lines):
        if i == 0 and lead:
            out += s.encode('utf-8') + eol
            n += 1
        else:
            out += eol + s.encode('utf-8') + eol
            n += 2
        nums.append(n)
    return out, nums


def insert_note(data, s, after):
    """the note inserted after line `after` with a blank line, where that line and the six before it two apart are dated notes, the last b757's."""
    eol = eol_of(data)
    if not data.endswith(eol):
        raise SystemExit('### THE FILE DOES NOT END WITH A NEWLINE -- NOTHING WRITTEN')
    check_lines([s])
    L = data.split(eol)[:-1]
    form = all(len(L) > x and L[x - 1].startswith(b'*Dated note, ') and L[x - 1].endswith(b'*') and L[x] == b'' for x in EPS_NOTE_LINES)
    if after != EPS_NOTE_LINES[-1] or not form or not L[after - 1].startswith(EPS_LAST_NEEDLE.encode('utf-8')) \
            or L[after + 1].startswith(b'*Dated note, '):
        raise SystemExit('### THE NOTE AT :%d AND THE SIX ABOVE IT NOT IN THE FORM READ, OR NOT THE LATEST -- NOTHING WRITTEN' % after)
    head = eol.join(L[:after]) + eol
    return head + eol + s.encode('utf-8') + eol + data[len(head):], after + 2


def kept_whole(k, data, after):
    if ITEMS[k]['how'] != 'insert':
        return after.startswith(data) and len(after) > len(data)
    eol = eol_of(data)
    head = eol.join(data.split(eol)[:ITEMS[k]['after']]) + eol
    return after.startswith(head) and after.endswith(data[len(head):]) and len(after) > len(data)


def registry_read(data):
    """the four rows by their IDs and name at their lines; refused otherwise."""
    L = data.decode('utf-8').replace('\r', '').split(NL)
    ok = all(len(L) >= n and L[n - 1].startswith('|') and re.search(r'\|\s*%s\s*\|' % re.escape(i), L[n - 1]) for n, i in REG_ROWS) \
        and len(L) >= REG_KERNEL and L[REG_KERNEL - 1].startswith('|') and 'SIDE-explicit-formula' in L[REG_KERNEL - 1]
    if not ok:
        raise SystemExit('### REGISTRY`S ROWS 1.5c-21 TO 1.5c-23 (:177-:179) OR THE KERNEL ROW (:924) NOT AS READ -- NOTHING WRITTEN')


def trail_read(data):
    """OPEN_TRAILS ending at b757's Next line under its trail; the two resolved lines at HEAD by b757's notes bank's digests."""
    L = data.decode('utf-8').replace('\r', '').split(NL)
    L = L[:-1] if L and L[-1] == '' else L
    if not (len(L) == OT_NEXT and L[-1].startswith(OT_NEXT_NEEDLE) and L[OT_TRAIL - 1].startswith(OT_TRAIL_NEEDLE)):
        raise SystemExit('### OPEN_TRAILS DOES NOT END AT b757`S NEXT LINE :%d UNDER ITS TRAIL :%d -- NOTHING WRITTEN' % (OT_NEXT, OT_TRAIL))
    e = (json.loads(NL.join(at_head(B757_NOTES)))['items'].get('e') or {})
    dg = dict((x['line'], x['digest']) for x in e.get('lines') or [])
    st = [(n, L[n - 1].startswith(nd) and digest(L[n - 1]) == dg.get(n)) for n, nd in OT_RESOLVED]
    if not all(o for _n, o in st):
        raise SystemExit('### THE TWO LINES RESOLVED AT b757 DO NOT STAND AS WRITTEN AT HEAD %s -- NOTHING WRITTEN' % st)
    return st


def compose(k, data, date, S=None, F=None, TG=None):
    """(after, [(line number, text, kind)], lines added)."""
    eol = eol_of(data)
    n0 = count_lines(data, eol)
    S = S if S is not None else sentences()
    F = F if F is not None else at_head(FERRY, 30)
    if k == 'a':
        s = note_a(S, date)
        after, at = insert_note(data, s, ITEMS['a']['after'])
        rows = [(at, s, 'the dated note')]
    elif k == 'e':
        trail_read(data)
        lines, _cuts = trail_lines(F, date)
        after, nums = append_block(data, lines)
        rows = list(zip(nums, lines, ['the seat`s dated head', 'b757`s root answer', 'the two lines standing', 'the price']))
    else:
        if k == 'd':
            registry_read(data)
        lines = section_b(S, date) if k == 'b' else [note_c(S, date) if k == 'c' else note_d(S, date, TG)]
        after, nums = append_block(data, lines)
        kinds = (['the heading', 'the preamble'] + ['a sentence'] * len(S) + ['the closing']) if k == 'b' else ['the dated note']
        rows = list(zip(nums, lines, kinds))
    return after, rows, count_lines(after, eol) - n0


# ### ---------------------------------------------------------------- the moved cites, by the citation tool's helpers
def citation_tool():
    import fold as F_
    F_.install()
    return F_.load(ACT, 'citation', name='%s_citation' % ACT)


def moved():
    """[(path, line, cite, the line then (digest), resolves, where its line now stands)] over the 123 relay rows of b757's notes bank."""
    CT = citation_tool()
    mc = (json.loads(NL.join(at_head(B757_NOTES)))['items']['a'].get('moved_cites') or {})
    rows = [x for x in mc.get('lines') or [] if x['repo'] == 'relay']
    then = CT._blob(PP, B757_PP_HEAD, EPS).replace('\r', '').split(NL)
    _rc, ph = git(PP, 'rev-parse', 'HEAD')
    now = CT._blob(PP, ph.strip(), EPS).replace('\r', '').split(NL)
    out, unread = [], []
    for x in rows:
        rc, txt = git(RELAY, 'show', 'HEAD:%s' % x['path'])
        L = txt.replace('\r', '').split(NL)
        same = rc == 0 and len(L) >= x['line'] and digest(L[x['line'] - 1]) == x['digest']
        if not same:
            unread.append((x['path'], x['line']))
        for c in x['moved']:
            out.append((x['path'], x['line'], c) + cite_class(CT, then, now, c) + (same,))
    return out, len(rows), unread, ph.strip()


def cite_class(CT, then, now, c):
    """(digest of the line then, resolves, its class, where it stands now): RESOLVES (the line at c at HEAD the line at c then, not blank);
    MOVED BY TWO (the line then at c + 2 at HEAD, b757's insertion); NO TEXT LINE THEN (the line then blank or past the file's end: the cite
    named no text at b757's write either); ELSEWHERE (each line at HEAD carrying its text, by the citation tool's `first`, every one); GONE."""
    old = CT.at(then, c)
    if not old.strip():
        return digest(old), False, 'NO TEXT LINE THEN', ()
    if CT.at(now, c) == old:
        return digest(old), True, 'RESOLVES', (c,)
    if CT.at(now, c + 2) == old:
        return digest(old), False, 'MOVED BY TWO', (c + 2,)
    pos, k = [], CT.first(now, old)
    while k:
        if now[k - 1] == old:
            pos.append(k)
        k = CT.first(now, old, k + 1)
    return digest(old), False, 'ELSEWHERE' if pos else 'GONE', tuple(pos)


def moved_text(out, n, unread, ph, L=None):
    bad = [r for r in out if not r[4]]
    t = ['%s -- (R368)(8): THE RELAY`S LINES WHOSE CITES b757`S EPSTEIN NOTE MOVED, READ BY THE CITATION TOOL AGAINST THE DOCUMENT AT HEAD (%s, tools/b758_notes.py moved)' % (ACT, stamp()),
         '', '## THE CONTROLS'] + (L or []) + [
         '', '### the rows: relay data/b757_notes.json items (a) `moved_cites`, repo relay ; each relay line read at relay HEAD by its digest ; each '
         'moved cite: the document`s line at that number at PLACE-papers %s (b757`s write`s HEAD) against the line at that number at PLACE-papers '
         'HEAD %s, by the citation tool`s helpers (b758_citation: _blob, at, first); a cite resolves where the two are equal and not blank; each '
         'that does not printed with where its line now stands (0: nowhere); the document`s lines given by number and digest alone' % (B757_PP_HEAD, ph[:8]), '']
    for p, ln, c, dg, _res, cls, where, same in bad:
        t.append('  relay %s :%d -- cites the document`s :%d (its line then sha256 %s) -- DOES NOT RESOLVE: %s%s%s' % (
            p, ln, c, dg, cls, (' ; that line now at %s' % ', '.join(':%d' % w for w in where)) if where else '',
            '' if same else ' ; THE RELAY LINE NOT AS COUNTED'))
    for p, ln in unread:
        t.append('  relay %s :%d -- THE LINE AT RELAY HEAD NOT THE ONE b757 COUNTED (its digest differs)' % (p, ln))
    by = {}
    for r in out:
        by[r[5]] = by.get(r[5], 0) + 1
    t += ['', '### ### **THE MOVED CITES READ: RELAY LINES %d ; CITES %d ; RESOLVING %d ; NOT RESOLVING %d (MOVED BY TWO %d ; NO TEXT LINE THEN %d ; '
          'ELSEWHERE %d ; GONE %d) ; RELAY LINES NOT AS COUNTED %d ; NONE EDITED, EACH PRINTED.**' % (
              n, len(out), len(out) - len(bad), len(bad), by.get('MOVED BY TWO', 0), by.get('NO TEXT LINE THEN', 0), by.get('ELSEWHERE', 0),
              by.get('GONE', 0), len(unread))]
    return NL.join(t) + NL


# ### ---------------------------------------------------------------- the controls
def controls(S=None):
    acct, word = DOORS.account(PP), DOORS.q_word()
    F = at_head(FERRY, 30)
    out = []
    j15, c17 = F[14], F[16]
    tj, tn = template(j15, SECTIONS[0][2]['LANDED']), template(j15, SECTIONS[0][2]['BROKE'])
    tc, tcn = template(c17, SECTIONS[1][2]['LANDED']), template(c17, SECTIONS[1][2]['BROKE'])
    plant_j = tj.replace('<peel>', 'abcd1234').replace('<run id>', '7').replace('<n>', '417')
    plant_c = tc.replace('<peel>', 'bcde2345').replace('<run id>', '8')
    out.append(('four templates cut once each from the ferry; a planted fill of each compiled sentence matched with its fields',
                fill(tj, plant_j) == [('peel', 'abcd1234'), ('run id', '7'), ('n', '417')] and fill(tc, plant_c) == [('peel', 'bcde2345'), ('run id', '8')]
                and bool(tn) and bool(tcn), True))
    out.append(('the join`s planted sentence with "not asserted" planted as "asserted" refused', fill(tj, plant_j.replace('not asserted', 'asserted')) is None, True))
    out.append(('a planted sentence with its run left as the field <run id> refused', fill(tj, tj.replace('<peel>', 'abcd1234').replace('<n>', '417')) is None, True))
    recs = [dict(item='join', outcome='LANDED', sentence=plant_j, run=7, tag='v0.39', peel='abcd1234' + '0' * 32, tag_object='e' * 40),
            dict(item='coeff', outcome='LANDED', sentence=plant_c, run=8, tag='v0.40', peel='bcde2345' + '0' * 32, tag_object='f' * 40)]
    sp = sentences(recs, F)
    out.append(('the sentences of a planted pair of LANDED rows, (4) then (5)', [s['key'] for s in sp] == ['join', 'coeff'], True))
    try:
        sentences([dict(recs[0], outcome='SHOWN')] + recs[1:], F)
        refused = False
    except SystemExit:
        refused = True
    out.append(('a planted row SHOWN and not landed refuses', refused, True))
    try:
        sentences([dict(recs[0], run=9)] + recs[1:], F)
        refused = False
    except SystemExit:
        refused = True
    out.append(('a planted row whose run is not its sentence`s refused', refused, True))
    plant_b = tn.replace('<module>', 'SIDEExplicitFormula.Schema.X').replace('<line>', '18').replace('<run id>', '7')
    sb = sentences([dict(item='join', outcome='BROKE', sentence=plant_b, run=7), dict(item='coeff', outcome='NOT READ')], F)
    out.append(('a planted join BROKE and (5) not begun: the one failing sentence', [s['outcome'] for s in sb] == ['BROKE'], True))
    date = stamp()[:10]
    TG = [('v0.39', 'e' * 40, 'abcd1234' + '0' * 32, 'data/x'), ('v0.40', 'f' * 40, 'bcde2345' + '0' * 32, 'data/y')]
    composed = [note_a(sp, date), note_c(sp, date), note_d(sp, date, TG)] + section_b(sp, date) + trail_lines(F, date)[0]
    out.append(('the composed lines on the planted pair, %d, withheld by no kind' % len(composed), all(DOORS.withheld(t, acct, word) == [] for t in composed), True))
    out.append(('a planted copy carrying the account withheld', 'the account' in DOORS.withheld(composed[0] + ' ' + (acct or 'x'), acct, word), True))
    out.append(('(d) gives each planted tag with its peel and closes with the ruling`s words',
                composed[2].endswith('The tags confer no deposit.*') and all(('`%s`' % t in composed[2] and '`%s`' % p in composed[2]) for t, _o, p, _c in TG), True))
    out.append(('(d) with no tag cut (planted) still closes with the ruling`s words', note_d(sb, date, []).endswith('The tags confer no deposit.*'), True))
    tl, cuts = trail_lines(F, date)
    out.append(('(e): 4 lines; the price cut from the ruling`s line whole; b757`s root word quoted whole',
                len(tl) == 4 and cuts['price'].startswith('60 to 150 lines') and cuts['price'].endswith("(the navigator's, from no build)")
                and tl[1].endswith('“%s”' % cuts['word']), True))
    try:
        append_block(b'no newline', ['x'])
        refused = False
    except SystemExit:
        refused = True
    out.append(('the append refused on a file not ending with a newline (planted)', refused, True))
    out.append(('one blank line before each appended line (planted)',
                append_block(b'a\n', ['X', 'Y']) == (b'a\n\nX\n\nY\n', [3, 5]) and append_block(b'a\n\n', ['X']) == (b'a\n\nX\n', [3]), True))
    plant = (b'h\n\n*v0.1*\n\n' + b''.join(b'*Dated note, 2026-11-0%d, x*\n\n' % n for n in range(1, 7))
             + b'*Dated note, 2026-11-16, b757, y*\n\nz\n')
    ins, at = insert_note(plant, 'N', 17)
    out.append(('the insert on a planted file in the form: the note at :19, the bytes before and after the place kept whole',
                at == 19 and ins.split(b'\n')[18] == b'N' and ins.split(b'\n')[17] == b'' and kept_whole('a', plant, ins), True))
    try:
        insert_note(plant.replace(b'2026-11-16, b757', b'2026-11-16, b75X'), 'N', 17)
        refused = False
    except SystemExit:
        refused = True
    out.append(('the insert refused where :17 is not b757`s note (planted)', refused, True))
    try:
        compose('e', b'x\n' * 5, date, sp, F)
        refused = False
    except SystemExit:
        refused = True
    out.append(('the trail block refused on a file not ending at b757`s Next line (planted)', refused, True))
    try:
        compose('d', b'x\n' * 5, date, sp, F, TG)
        refused = False
    except SystemExit:
        refused = True
    out.append(('the REGISTRY note refused on a file without the four rows (planted)', refused, True))
    for k in ORDER:
        _rc, blob = gitb(PP, 'show', 'HEAD:%s' % ITEMS[k]['rel'])
        try:
            compose(k, blob, date, sp, F, TG)
            ok_ = True
        except SystemExit as e:
            ok_ = str(e)[:80]
        out.append(('(%s) composed on PLACE-papers HEAD`s %s with the planted pair' % (k, ITEMS[k]['rel']), ok_, True))
    CT = citation_tool()
    th, nw = ['a', 'b', '', 'q', 'r', 'w'], ['a', 'n', 'm', 'b', 'x', 'y', 'w', 'k', 'w']
    cc = [(c, cite_class(CT, th, nw, c)[2:]) for c in (1, 2, 3, 5, 6, 40)]
    out.append(('the moved-cite classes on planted lines by the citation tool`s helpers: resolves, moved by two, blank then, gone, elsewhere (each '
                'place), past the end then', cc == [(1, ('RESOLVES', (1,))), (2, ('MOVED BY TWO', (4,))), (3, ('NO TEXT LINE THEN', ())),
                                                   (5, ('GONE', ())), (6, ('ELSEWHERE', (7, 9))), (40, ('NO TEXT LINE THEN', ()))], True))
    ok = all(a == b for _, a, b in out)
    for n, a, b in out:
        print('  CONTROL %s: %s (wanted %s)' % (n, a, b))
    print('### CONTROLS %d OF %d AS WANTED ; the account and the word read at run time, neither printed' % (
        sum(1 for _, a, b in out if a == b), len(out)))
    return ok, ['  CONTROL %s: %s (wanted %s)' % x for x in out]


# ### ---------------------------------------------------------------- the bank and the modes
def load():
    return json.load(open(BANK, encoding='utf-8')) if os.path.exists(BANK) else {'act': ACT, 'clause': '(R368)(8)', 'items': {}}


def bank(R):
    tmp = BANK + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(R, indent=1, ensure_ascii=False) + NL)
    os.replace(tmp, BANK)


def show(k, rows, added, data, after, acct, word):
    it = ITEMS[k]
    print('  (%s) %s ; %d bytes before, %d after ; lines added %d ; the bytes before and after the place kept whole %s' % (
        k, it['rel'], len(data), len(after), added, kept_whole(k, data, after)))
    for n, s, kind in rows:
        wh = DOORS.withheld(s, acct, word)
        print('    :%d digest %s, %d characters ; %s ; withheld by a kind: %s' % (n, digest(s), len(s), kind, wh or 'none'))
        print('      %s' % s)


def main(argv):
    step = argv[0] if argv else ''
    if step == 'controls':
        return 0 if controls()[0] else 1
    if step == 'moved':
        ok, L = controls()
        if not ok:
            raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
        out, n, unread, ph = moved()
        text = moved_text(out, n, unread, ph, L)
        print(text)
        if '--bank' in argv:
            r = FB.write(MOVED, text)
            print('BANKED: data/b758_moved_cites.txt ; figbank: %s' % r['why'])
        return 0
    if step not in ('dry', 'write', 'confirm'):
        sys.exit(__doc__)
    k = argv[1] if len(argv) > 1 else ''
    if k not in ORDER and not (step == 'dry' and k == 'all'):
        sys.exit(__doc__)
    acct, word = DOORS.account(PP), DOORS.q_word()
    if step == 'confirm':
        R = load()
        e = R['items'].get(k)
        if not e or e.get('confirm'):
            raise SystemExit('### (%s) NOT WRITTEN, OR CONFIRMED ALREADY -- NOTHING DONE' % k)
        rel = ITEMS[k]['rel']
        _, head = git(PP, 'rev-parse', 'HEAD')
        _, files = git(PP, 'show', '--format=', '--name-only', 'HEAD')
        _, num = git(PP, 'show', '--format=', '--numstat', 'HEAD')
        _, blob = gitb(PP, 'show', 'HEAD:%s' % rel)
        O = blob.decode('utf-8').replace('\r', '').split(NL)
        _, prior = gitb(PP, 'show', '%s:%s' % (e['pp_head'], rel))
        _a, want, _n = compose(k, prior, e['date'])
        have = [len(O) >= x['line'] and digest(O[x['line'] - 1]) == x['digest'] and O[x['line'] - 1] == w[1] for x, w in zip(e['lines'], want)]
        ok = (files.strip() == rel and num.split()[:2] == [str(e['added']), '0'] and bdigest(blob) == e['sha_after'] and bdigest(prior) == e['sha_before']
              and all(have) and len(have) == len(e['lines']) and head.strip() != e['pp_head'])
        print('### (%s) CONFIRM: PLACE-papers HEAD %s ; files %s ; numstat %s (wanted %d 0) ; HEAD`s blob the composed bytes %s ; '
              'each line at HEAD composed again from the banks at relay HEAD %s ; %s' % (k, head.strip()[:8], files.strip(), num.split()[:2], e['added'],
                                                                                      bdigest(blob) == e['sha_after'], have, 'AS WANTED' if ok else 'NOT AS WANTED'))
        if not ok:
            raise SystemExit('### THE COMMIT DOES NOT CARRY (%s) AS COMPOSED -- NOTHING WRITTEN' % k)
        e['confirm'] = 'PLACE-papers %s at %s, %s alone, %d lines added, none removed' % (head.strip()[:8], stamp(), rel, e['added'])
        bank(R)
        return 0
    if not controls()[0]:
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    S, F = sentences(), at_head(FERRY, 30)
    TG = tags(S)
    _, head = git(PP, 'rev-parse', 'HEAD')
    staged = subprocess.run(['git', '-C', PP, 'diff', '--cached', '--quiet']).returncode == 0
    date = stamp()[:10]
    todo = ORDER if k == 'all' else (k,)
    if step == 'write':
        R = load()
        i = ORDER.index(k)
        if k in R['items']:
            raise SystemExit('### (%s) WRITTEN ALREADY -- NOTHING DONE' % k)
        if i and not (R['items'].get(ORDER[i - 1]) or {}).get('confirm'):
            raise SystemExit('### (%s) NOT CONFIRMED -- (%s) WAITS FOR IT -- NOTHING DONE' % (ORDER[i - 1], k))
    print('  PLACE-papers HEAD %s ; nothing staged %s ; the date %s ; the sentences %s ; the tags %s' % (
        head.strip()[:8], staged, date, ['(%s) %s' % (s['key'], s['outcome']) for s in S], ['%s %s' % (t, p[:8]) for t, _o, p, _c in TG] or 'none'))
    for q in todo:
        rel = ITEMS[q]['rel']
        path = os.path.join(PP, rel)
        clean = subprocess.run(['git', '-C', PP, 'diff', '--quiet', 'HEAD', '--', rel]).returncode == 0
        data = open(path, 'rb').read()
        present = (ITEMS[q]['present'] % date).encode('utf-8') in data
        after, rows, added = compose(q, data, date, S, F, TG)
        print('  (%s) clean against HEAD %s ; written already %s' % (q, clean, present))
        show(q, rows, added, data, after, acct, word)
        wh = [w for _, s, _ in rows for w in DOORS.withheld(s, acct, word)]
        bad = not clean or present or wh or not kept_whole(q, data, after) or not staged
        if step == 'dry':
            print('  (%s) DRY: nothing written%s' % (q, ' ; WOULD BE REFUSED' if bad else ''))
            continue
        if bad:
            raise SystemExit('### (%s) NOT CLEAN, WRITTEN ALREADY, WITHHELD, NOT KEPT WHOLE OR SOMETHING STAGED -- NOTHING WRITTEN' % q)
        at = stamp()
        with open(path + '.tmp', 'wb') as f:
            f.write(after)
        os.replace(path + '.tmp', path)
        back = open(path, 'rb').read()
        print('  WRITTEN %s at %s ; read back %s' % (rel, at, 'EQUAL to the composed' if back == after else 'DIFFERS'))
        if back != after:
            raise SystemExit('### THE READ-BACK DIFFERS -- restore %s through the one-call tool' % rel)
        R['items'][q] = {'file': rel, 'how': ITEMS[q]['how'], 'date': date, 'pp_head': head.strip(), 'written_at': at, 'added': added,
                         'count_before': count_lines(data, eol_of(data)), 'count_after': count_lines(after, eol_of(after)),
                         'sha_before': bdigest(data), 'sha_after': bdigest(after),
                         'sentences': dict((s['key'], s['outcome']) for s in S) if q != 'e' else {},
                         'lines': [{'line': n, 'digest': digest(s), 'chars': len(s), 'kind': kd} for n, s, kd in rows], 'confirm': None}
        bank(R)
        print('  then: `commit.py pp add %s`, its commit, then `tools/b758_notes.py confirm %s`' % (rel, q))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
