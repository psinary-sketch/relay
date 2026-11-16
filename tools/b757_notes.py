# -*- coding: utf-8 -*-
"""b757, (R367)(9) and the ferry's Component 6: WHERE THE SENTENCES GO. "each write by one PLACE-papers commit through the one-call tool
with its scan, the angle-bracket fields filled from the act's banks and nothing else changed. Each document below takes one dated note made of
that document's own dated head and the outcome sentences of (4), (5), (6) and (7) that came true, in that order" (data/b757_ferry.txt :27).
Carried in form from tools/b756_notes.py (append, insert, controls, write, confirm).

THE SENTENCES: each cut from data/b757_outcomes.txt at relay HEAD (its "  THE SENTENCE: " line in the section of its item, the bank composed by
the committed tools/b757_outcomes.py), and matched whole against the ruling's own template for the outcome the bank's foot reads, cut from the
ferry at relay HEAD between its opening quotation mark and the next: the template's literal words equal, each <field> filled, the one optional
segment of (6) (<; with it, ...>) present or absent whole. The run id each sentence carries equal to its section's run read. Nothing in a
sentence is changed by this tool.

THE PLACES, as (9) gives them:
  (a) THE_EPSTEIN_CONTROL_OBJECT_v0_1.md: inserted after the note at :15 with a blank line, in the form of the six above it (:5 to :15, each a
      dated note, a blank line between), without (6)'s sentence, closing "none written into a section here; §6 to §8 take these up"; the
      cites of this document's lines that the insertion moves printed (mode `moved`, and banked at (a)'s write)
  (b) FACES_LEDGER.md: one UPDATE section appended at the file's end in the form of the section at :541 (heading, its italic preamble, the
      body, its italic closing, a blank line between each), without (6)'s sentence
  (c) THE_KEYSTONE_CENSUS_v0_8_3.md: one note appended at the file's end in the form of the note at :1568
  (d) REGISTRY.md: one dated note appended at the file's end in the form of the note at :1244, to the rows 1.5c-21, 1.5c-22 and 1.5c-23
      (:177-:179) and the kernel row at :924, giving each new tag with its peeled commit (read from the gated push's capture) and closing "The
      tags confer no deposit."
  (e) OPEN_TRAILS.md: appended at the file's end under one dated head before this act's own trail, no line moving: the line of (1) (b756's
      root answer, in the sentence tools/acts/b757.py's c1 route composes); W-ORD-KEIPER-FACE CARRIED with the ruling's quoted words, and the
      join's outcome beside them (the words were written for the join compiled; the join broke); the four orders CARRIED to the act after the
      build; W-ORD-SQUARES-AT-24 ENTERED in the ruling's words with its trigger, and its price as no bank gives one; [L22] quoted whole with
      the closing words "(the navigator's)" cut from (9)'s line. A blank line before the head and before each line (b756's form).

THE ORDER: (a) to (e), one at a time; a write is refused until the item before it is confirmed. The withheld kinds are tools/b754_doors.py's
(the account the clone's remote names, [Q] row (3)'s word read at run time, an identifier), none of them printed. The bank carries digests
and line numbers alone for PLACE-papers' lines; the composed lines are this act's own, printed whole before the write.
MODES  controls | moved [--bank] | dry <item|all> | write <item> | confirm <item>      BANK data/b757_notes.json; data/b757_notes_moved.txt
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
sys.path.insert(0, T)
import b754_doors as DOORS   # noqa: E402

ACT = 'b757'
PP = DOORS.PP
FERRY = 'data/b757_ferry.txt'
OUTC = 'data/b757_outcomes.txt'
TAGBANK = 'data/b757_SIDE-dirichlet-mod-24_push-b757-mod24_push_out.txt'
ANSWERS = 'data/b756_author_answers.txt'
BANK = os.path.join(RELAY, 'data', '%s_notes.json' % ACT)
MOVED = os.path.join(RELAY, 'data', '%s_notes_moved.txt' % ACT)
NL = '\n'
ORDER = ('a', 'b', 'c', 'd', 'e')
EPS = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
ITEMS = {
    'a': {'rel': EPS, 'how': 'insert', 'after': 15, 'keys': ('4', 'T0', 'T1', '7'), 'present': '*Dated note, %s, b757'},
    'b': {'rel': 'FACES_LEDGER.md', 'how': 'section', 'keys': ('4', 'T0', 'T1', '7'), 'present': '## UPDATE — filed %s (b757)'},
    'c': {'rel': 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md', 'how': 'append', 'keys': ('4', 'T0', 'T1', '6', '7'),
          'present': '*Appended %s by b757'},
    'd': {'rel': 'REGISTRY.md', 'how': 'append', 'keys': ('4', 'T0', 'T1', '6', '7'), 'present': '*Dated note, b757, %s'},
    'e': {'rel': 'OPEN_TRAILS.md', 'how': 'trail', 'present': '**Dated head, %s, b757, `(R367)`(9)'},
}
EPS_NOTE_LINES = (5, 7, 9, 11, 13, 15)
# ### the items of (4)-(7): (key, the outcomes bank's section head, the ferry's line, {the foot's word: the template's marker})
SECTIONS = (
    ('4', '## (4) THE JOIN', 15, {'BROKE': 'THE SENTENCE IF IT DOES NOT: "', 'COMPILED': 'THE SENTENCE IF IT COMPILES: "'}),
    ('T0', '## (5) T0', 18, {'COMPILED': 'IF IT COMPILES: "', 'OPEN': 'IF IT DOES NOT: "'}),
    ('T1', '## (5) T1', 19, {'COMPILED': 'IF IT COMPILES: "', 'OPEN': 'IF IT DOES NOT: "'}),
    ('6', '## (6) THE MODULUS-24 MODULE', 21, {'COMPILED': 'IF THE MODULE COMPILES: "', 'OPEN': 'IF IT DOES NOT: "'}),
    ('7', '## (7) THE ONE DIRECTION', 23, {'COMPILED': 'IF IT COMPILES: "', 'PRICED': 'IF IT IS PRICED AND NOT BUILT: "'}),
)
FOOT = re.compile(r'^### ### \*\*THE OUTCOMES: JOIN (\w+) ; T0 (\w+) ; T1 (\w+) ; MOD24 (\w+) ; WIDE (\w+)\.\*\*$')
FIELDS = ('module', 'line', 'run id', 'tag', 'peel', 'axioms', 'name', 'where it stopped', 'lines', 'dispatches', 'the steps compiled',
          'branch', 'commit')
FIELD_RX = re.compile(r'<(%s)>' % '|'.join(re.escape(f) for f in FIELDS))
STD3 = ('propext', 'Classical.choice', 'Quot.sound')
FOUR = ('W-ORD-EXPLICIT-FORMULA-C1', 'W-ORD-E2-SEPARATION', 'W-ORD-BESSEL-BOUND-TIGHTEN', 'W-ORD-B518-FLOAT')
OT_TRAIL, OT_NEXT = 18422, 18487          # ### b756's trail head and its Next line, the file's last
OT_TRAIL_NEEDLE = '### b756 — lane two, act one hundred and eighty-three'
OT_NEXT_NEEDLE = '**Next:** ((R366)(7)) the build as b757'
ANSWER_LINE = 27
ANSWER_OPENS = 'RESULT (transcript line 86704, 2026-11-16T01:19:42.171Z): '
ANSWER_CLOSES = '="Build as b757". You can now continue with these answers in mind.'
LEDGER_NAMES = r'\b(?:FINDINGS|OPEN_TRAILS|REGISTRY|ERRATA|INSTRUMENTS|SPIRAL_MAP|VERIFICATION_LOOM|README|FACES_LEDGER|HANDOFF)\b'


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


# ### ---------------------------------------------------------------- the sentences and their templates
def template(line, marker):
    """the ruling's sentence after `marker` on its line, to the next quotation mark; the marker standing once."""
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
    """(compiled regex, field names, the optional segment or None): literal words escaped, each <field> a lazy group, (6)'s <; ...> optional."""
    opt, tail = None, ''
    head = t
    if '<;' in t:
        i, j = t.index('<;'), t.rindex('>')
        if j < i:
            raise SystemExit('### THE OPTIONAL SEGMENT HAS NO CLOSING MARK -- NOTHING DONE')
        head, opt, tail = t[:i], t[i + 1:j], t[j + 1:]
    out, pos, names = [], 0, []
    for m in FIELD_RX.finditer(head):
        out.append(re.escape(head[pos:m.start()]))
        out.append('(.+?)')
        names.append(m.group(1))
        pos = m.end()
    out.append(re.escape(head[pos:]))
    rx = ''.join(out) + ('(?:%s)?' % re.escape(opt) if opt is not None else '') + re.escape(tail) + r'\Z'
    return re.compile(rx, re.S), names, opt


def fill(t, s):
    """[(field, value)] where `s` is the template `t` with its fields filled; None where it is not; the optional segment's presence."""
    rx, names, opt = tregex(t)
    m = rx.match(s)
    if not m:
        return None, None
    vals = list(zip(names, m.groups()))
    if any(not v.strip() or '<' in v or '>' in v for _n, v in vals):
        return None, None
    return vals, (opt is not None and opt in s)


def sections(O):
    """{key: (section lines)} of the outcomes bank, each from its head to the next '## '."""
    out, cur = {}, None
    for l in O:
        if l.startswith('## '):
            cur = next((k for k, h, _f, _m in SECTIONS if l.startswith(h)), None)
            if cur:
                out[cur] = []
            continue
        if cur:
            out[cur].append(l)
    return out


def sentences():
    """{key: dict(sentence, template, outcome, fields, opt, run)}: each sentence cut from the outcomes bank at relay HEAD and matched whole
    against the ruling's template for the outcome its foot reads."""
    O, F = at_head(OUTC), at_head(FERRY, 30)
    foot = [m for m in (FOOT.match(l) for l in O) if m]
    if len(foot) != 1:
        raise SystemExit('### THE OUTCOMES BANK`S FOOT READ %d TIMES, NOT ONCE -- NOTHING DONE' % len(foot))
    words = dict(zip(('4', 'T0', 'T1', '6', '7'), foot[0].groups()))
    S = sections(O)
    out = {}
    for k, _h, fl, markers in SECTIONS:
        w = words[k]
        if w not in markers:
            raise SystemExit('### (%s): THE FOOT READS %s, WHICH NO TEMPLATE OF THIS TOOL TAKES -- NOTHING DONE' % (k, w))
        sl = [l for l in S.get(k, []) if l.startswith('  THE SENTENCE: ')]
        runs = [m.group(1) for m in (re.match(r'^  THE RUN (\d+) READ', l) for l in S.get(k, [])) if m]
        if len(sl) != 1 or len(runs) != 1:
            raise SystemExit('### (%s): SENTENCES %d, RUNS READ %d IN ITS SECTION, NOT ONE EACH -- NOTHING DONE' % (k, len(sl), len(runs)))
        s = sl[0][len('  THE SENTENCE: '):]
        t = template(F[fl - 1], markers[w])
        vals, opt = fill(t, s)
        if vals is None:
            raise SystemExit('### (%s): THE SENTENCE IS NOT THE RULING`S TEMPLATE WITH ITS FIELDS FILLED -- NOTHING DONE' % k)
        rid = [v for n, v in vals if n == 'run id']
        if rid and set(rid) != {runs[0]}:
            raise SystemExit('### (%s): THE SENTENCE`S RUN %s IS NOT ITS SECTION`S RUN %s -- NOTHING DONE' % (k, rid, runs[0]))
        ax = [v for n, v in vals if n == 'axioms']
        if any(not set(x.replace('axioms: ', '').split(', ')) <= set(STD3) for x in ax):
            raise SystemExit('### (%s): AN AXIOMS FIELD OUTSIDE THE STANDARD THREE %s -- NOTHING DONE' % (k, ax))
        out[k] = dict(sentence=s, template=t, outcome=w, fields=vals, opt=opt, run=runs[0], fline=fl)
    return out


def tag_peel():
    """(tag, tag object, peel) of v0.2.0 from the gated push's capture: made at the read-back, peeled local equal to remote."""
    L = at_head(TAGBANK)
    made = [m for m in (re.match(r'^push_gated: tag (v[\d.]+) made at the read-back ([0-9a-f]{40}) \(([0-9a-f]{40})\)$', l) for l in L) if m]
    peel = [m for m in (re.match(r'^push_gated: tag (v[\d.]+) peeled local ([0-9a-f]{40}) remote ([0-9a-f]{40})$', l) for l in L) if m]
    if len(made) != 1 or len(peel) != 1 or made[0].group(1) != peel[0].group(1) or not (made[0].group(2) == peel[0].group(2) == peel[0].group(3)):
        raise SystemExit('### THE TAG`S MAKING AND PEEL NOT READ ONCE EACH AND EQUAL IN %s -- NOTHING DONE' % TAGBANK)
    return made[0].group(1), made[0].group(3), made[0].group(2)


# ### ---------------------------------------------------------------- the composed lines
def note_a(S, date):
    body = ' '.join(S[k]['sentence'] for k in ITEMS['a']['keys'])
    return ('*Dated note, %s, b757, under the author’s ruling `(R367)`(9)(a): %s These four sentences are the build’s outcomes at b757, '
            'none written into a section here; §6 to §8 take these up.*') % (date, body)


def section_b(S, date):
    return ['## UPDATE — filed %s (b757): the build’s outcomes at the Epstein control, under the author’s ruling (R367)(9)(b)' % date,
            '*Rows above are never rewritten; this update names no earlier row and edits none. Written by relay `tools/b757_notes.py` under the '
            'author’s ruling (R367)(9)(b), in the form of b712’s section (:541): the outcome sentences of (R367)(4), (5) and (7) that came true, in '
            'that order, each the ruling’s text with its fields filled from the act’s banks (relay `data/b757_outcomes.txt`). No face is entered '
            'and no grade is conferred by this update.*'] + [S[k]['sentence'] for k in ITEMS['b']['keys']] + [
            '*The rows above are unedited. Filed by b757 (relay `data/b757_notes.json`).*']


def note_c(S, date):
    body = ' '.join(S[k]['sentence'] for k in ITEMS['c']['keys'])
    return "*Appended %s by b757 under the author's ruling `(R367)`(9)(c):* %s No byte above this line changes." % (date, body)


def note_d(S, date):
    body = ' '.join(S[k]['sentence'] for k in ITEMS['d']['keys'])
    tag, obj, peel = tag_peel()
    return ("*Dated note, b757, %s, under the author's ruling `(R367)`(9)(d), to the rows 1.5c-21, 1.5c-22 and 1.5c-23 (:177-:179) and the "
            "kernel row at :924: %s The new tag: SIDE-dirichlet-mod-24 `%s` (tag object `%s`), whose peel reads `%s`, read back from the remote "
            "(relay %s); SIDE-explicit-formula takes no tag at b757 (relay data/b757_outcomes.txt). No cell of the four rows and no other row is "
            "edited. The tags confer no deposit.*") % (date, body, tag, obj[:8], peel, TAGBANK)


def ferry27(F):
    s = F[26]
    if not s.startswith('(9) WHERE THE SENTENCES GO'):
        raise SystemExit('### THE RULING`S LINE :27 IS NOT (9) -- NOTHING DONE')
    return s


def keiper_words(F):
    s = ferry27(F)
    k = 'W-ORD-KEIPER-FACE CARRIED, "'
    if s.count(k) != 1:
        raise SystemExit('### (9)`S KEIPER WORDS NOT READ ONCE -- NOTHING DONE')
    a = s.index(k) + len(k)
    return s[a:s.index('"', a)]


def four_words(F):
    s = ferry27(F)
    w = ('%s, %s, %s and %s CARRIED to the act after the build, by the author\'s cut of 2026-11-15, with the written proofs of the '
         'class-number-3 law and of the closed form named beside them') % FOUR
    if s.count(w) != 1:
        raise SystemExit('### (9)`S FOUR ORDERS NOT READ ONCE AS WRITTEN -- NOTHING DONE')
    return w


def l22(F):
    """(the [L22] line cut whole, the closing words cut from (9)'s own line)."""
    s = ferry27(F)
    k = 'and one line closing "'
    if s.count(k) != 1:
        raise SystemExit('### (9)`S CLOSING WORDS NOT READ ONCE -- NOTHING DONE')
    a = s.index(k) + len(k)
    closing = s[a:s.index('"', a)]
    if closing != "(the navigator's)":
        raise SystemExit('### THE CLOSING WORDS NOT AS READ -- NOTHING DONE')
    i = s.index('"[L22] ')
    if not s.endswith('"') or s.rindex('"') == i:
        raise SystemExit('### [L22] HAS NO CLOSING QUOTATION MARK -- NOTHING DONE')
    t = s[i + 1:-1]
    if '"' in t or not t.startswith('[L22] A reading, promoting nothing.'):
        raise SystemExit('### THE CUT OF [L22] CARRIES A QUOTATION MARK OR DOES NOT OPEN AS READ -- NOTHING DONE')
    return t, closing


def squares_words(F):
    s = F[20]
    k = "CARRIED AS A NAMED ORDER, W-ORD-SQUARES-AT-24, entered in OPEN_TRAILS with its price and its trigger the author's word: "
    e = ' IF THE MODULE COMPILES:'
    if not s.startswith('(6) THE MODULUS-24 MODULE') or s.count(k) != 1 or e not in s[s.index(k):]:
        raise SystemExit('### (6)`S NAMED ORDER NOT READ ONCE -- NOTHING DONE')
    a = s.index(k) + len(k)
    return s[a:s.index(e, a)]


def answer_line():
    """(1)'s line, in the sentence tools/acts/b757.py's c1 route composes (its _c1_trail), read from b756's answers bank at relay HEAD."""
    A = at_head(ANSWERS, ANSWER_LINE)
    s = A[ANSWER_LINE - 1]
    if not (s.startswith(ANSWER_OPENS) and s.endswith(ANSWER_CLOSES)):
        raise SystemExit('### %s :%d IS NOT THE ROOT`S RESULT AS READ -- NOTHING DONE' % (ANSWERS, ANSWER_LINE))
    return ('b756’s one question at the root was answered “Build as b757” (relay data/b756_author_answers.txt :%d, 2026-11-16T01:19:42Z): the act '
            'after b756 is b757, the build, as b756’s trail reads it (:%d).') % (ANSWER_LINE, OT_NEXT)


def trail_lines(F, date):
    keiper, four, sq = keiper_words(F), four_words(F), squares_words(F)
    l22_t, closing = l22(F)
    head = ('**Dated head, %s, b757, `(R367)`(9): the lines the ruling orders for OPEN_TRAILS** (relay data/b757_ferry.txt :9, :21, :27), '
            'appended at the end of the file after b756’s trail (its last line :%d) and before this act’s own trail, so that no line of the trail '
            'moves: `(R367)`(1)’s line; the order carried with the ruling’s words beside the join’s outcome; the four orders carried to the act '
            'after the build; the order entered under `(R367)`(6); and [L22], quoted whole from the ruling with the closing words (9) gives it.'
            ) % (date, OT_NEXT)
    one = '*Appended %s by b757 to b756’s trail (:%d), under `(R367)`(1):* %s' % (date, OT_TRAIL, answer_line())
    kp = ('`W-ORD-KEIPER-FACE` CARRIED under `(R367)`(9), the ruling’s words, written for the join compiled: “%s” (relay data/b757_ferry.txt '
          ':27). The join broke at b757 (relay data/b757_outcomes.txt, `(R367)`(4)): keiper-b725 stands at 01fd33c2 as it stood, unjoined, and '
          'Keiper’s definition at every n stands open.') % keiper
    fours = [('`%s` CARRIED to the act after the build under `(R367)`(9), by the author’s cut of 2026-11-15, one of the four orders the ruling '
              'carries so, with the written proofs of the class-number-3 law and of the closed form named beside them (relay data/b757_ferry.txt '
              ':27).') % n for n in FOUR]
    sqr = ('`W-ORD-SQUARES-AT-24` ENTERED under `(R367)`(6), a named order on SIDE-dirichlet-mod-24 beside OPEN_TRAILS :12649, in the ruling’s '
           'words: “%s” Its trigger: the author’s word. Its price: none banked at b757, the price table carrying no row for it and the ruling '
           'giving no figure (relay data/b757_price.txt; data/b757_ferry.txt :21).') % sq
    return [head, one, kp] + fours + [sqr, '%s %s' % (l22_t, closing)], dict(keiper=keiper, four=four, squares=sq, l22=l22_t, closing=closing)


# ### ---------------------------------------------------------------- the bytes
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
    """each line after one blank line: one blank between the file's last text and the first line (none added where the file ends with a
    blank line already), and one between each; returns (after, [line numbers])."""
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
    """the note inserted after line `after` with a blank line, where that line and the five before it two apart are dated notes."""
    eol = eol_of(data)
    if not data.endswith(eol):
        raise SystemExit('### THE FILE DOES NOT END WITH A NEWLINE -- NOTHING WRITTEN')
    check_lines([s])
    L = data.split(eol)[:-1]
    form = all(len(L) > x and L[x - 1].startswith(b'*Dated note, ') and L[x - 1].endswith(b'*') and L[x] == b'' for x in EPS_NOTE_LINES)
    if after != EPS_NOTE_LINES[-1] or not form or not L[after - 1].startswith(b'*Dated note, 2026-11-15, b756:'):
        raise SystemExit('### THE NOTE AT :%d AND THE FIVE ABOVE IT NOT IN THE FORM READ -- NOTHING WRITTEN' % after)
    head = eol.join(L[:after]) + eol
    return head + eol + s.encode('utf-8') + eol + data[len(head):], after + 2


def kept_whole(k, data, after):
    if ITEMS[k]['how'] != 'insert':
        return after.startswith(data) and len(after) > len(data)
    eol = eol_of(data)
    head = eol.join(data.split(eol)[:ITEMS[k]['after']]) + eol
    return after.startswith(head) and after.endswith(data[len(head):]) and len(after) > len(data)


def compose(k, data, date, S=None, F=None):
    """(after, [(line number, text, kind)], lines added)."""
    it = ITEMS[k]
    eol = eol_of(data)
    n0 = count_lines(data, eol)
    S = S if S is not None else sentences()
    F = F if F is not None else at_head(FERRY, 30)
    if k == 'a':
        s = note_a(S, date)
        after, at = insert_note(data, s, it['after'])
        rows = [(at, s, 'the dated note')]
    elif k == 'e':
        L = data.split(eol)[:-1]
        if not (len(L) == OT_NEXT and L[-1].decode('utf-8').startswith(OT_NEXT_NEEDLE) and L[OT_TRAIL - 1].decode('utf-8').startswith(OT_TRAIL_NEEDLE)):
            raise SystemExit('### OPEN_TRAILS DOES NOT END AT b756`S NEXT LINE :%d UNDER ITS TRAIL :%d -- NOTHING WRITTEN' % (OT_NEXT, OT_TRAIL))
        lines, _cuts = trail_lines(F, date)
        after, nums = append_block(data, lines)
        kinds = ['the seat`s dated head', '(1)`s line'] + ['an order`s line'] * 6 + ['[L22], the ruling`s text and its closing words']
        rows = list(zip(nums, lines, kinds))
    else:
        lines = section_b(S, date) if k == 'b' else [note_c(S, date) if k == 'c' else note_d(S, date)]
        after, nums = append_block(data, lines)
        kinds = (['the heading', 'the preamble'] + ['a sentence'] * len(it['keys']) + ['the closing']) if k == 'b' else ['the dated note']
        rows = list(zip(nums, lines, kinds))
    return after, rows, count_lines(after, eol) - n0


# ### ---------------------------------------------------------------- the cites the insertion moves
def moved():
    """[(repo, path, line, [cited numbers], [moved numbers], digest of the line)]: every line of PLACE-papers and of the relay at HEAD naming the
    Epstein document, its cites read from the name to the next path or ledger name; those above :15 moved by two at (a)'s insert."""
    stop = re.compile(r'[\w./-]+\.(?:md|lean|txt|py|json|tpl)\b|' + LEDGER_NAMES)
    name = re.compile(r'THE_EPSTEIN_CONTROL_OBJECT(?:_v0_1)?(?:\.md)?')
    out, named = [], {'PLACE-papers': 0, 'relay': 0}
    for repo, root in (('PLACE-papers', PP), ('relay', RELAY)):
        rc, txt = git(root, 'grep', '-n', '-I', '-F', 'THE_EPSTEIN_CONTROL_OBJECT', 'HEAD', '--')
        for row in txt.replace('\r', '').split(NL):
            if not row.startswith('HEAD:'):
                continue
            _h, path, ln, line = row.split(':', 3)
            if repo == 'PLACE-papers' and path == EPS:
                continue
            named[repo] += 1
            cites = []
            for m in name.finditer(line):
                rest = line[m.end():]
                st = stop.search(rest)
                seg = rest[:st.start()] if st else rest
                cites += [int(x) for x in re.findall(r'(?<![\w.]):(\d+)', seg)]
            mv = sorted(set(c for c in cites if c > 15))
            if mv:
                out.append((repo, path, int(ln), sorted(set(cites)), mv, digest(line)))
    return out, named


def moved_text(rows, named):
    out = ['b757 -- (R367)(9)(a): THE CITES OF THE EPSTEIN DOCUMENT`S LINES THAT THE INSERTION AFTER :15 MOVES BY TWO (%s, tools/b757_notes.py moved)' % stamp(),
           '', '### the lines naming the document at HEAD, its own lines apart: PLACE-papers %d ; relay %d ; each line`s cites read from the name to '
           'the next path or ledger name ; a line printed by path, line and the sha256 of its text (16 hex), its cites by number' % (
               named['PLACE-papers'], named['relay']), '']
    for repo, path, ln, cites, mv, dg in rows:
        out.append('  %s %s :%d (sha256 %s) -- cites %s ; moved %s -> %s' % (repo, path, ln, dg, cites, ['%d' % c for c in mv],
                                                                            ['%d' % (c + 2) for c in mv]))
    out += ['', '### ### **THE CITES THE INSERTION MOVES: LINES %d (PLACE-papers %d, relay %d) ; CITES MOVED %d ; NONE EDITED, EACH PRINTED.**' % (
        len(rows), sum(1 for r in rows if r[0] == 'PLACE-papers'), sum(1 for r in rows if r[0] == 'relay'), sum(len(r[4]) for r in rows))]
    return NL.join(out) + NL


# ### ---------------------------------------------------------------- the controls
def controls():
    acct, word = DOORS.account(PP), DOORS.q_word()
    S, F = sentences(), at_head(FERRY, 30)
    out = []
    out.append(('the five sentences each the ruling`s template for its outcome with its fields filled, the run equal to its section`s: %s' % (
        ', '.join('(%s) %s' % (k, S[k]['outcome']) for k in ('4', 'T0', 'T1', '6', '7'))), len(S) == 5, True))
    t0 = S['T0']
    out.append(('T0`s sentence with "not multiplicative" planted as "multiplicative" refused by its template',
                fill(t0['template'], t0['sentence'].replace('are not multiplicative', 'are multiplicative'))[0] is None, True))
    out.append(('T1`s sentence with its run id left as the placeholder <run id> (planted) refused', fill(S['T1']['template'], S['T1']['sentence'].replace(
        'run %s' % S['T1']['run'], 'run <run id>'))[0] is None, True))
    s6 = S['6']
    bare = s6['sentence'].replace('; with it, ab = a + b + 1 for 2 <= a < b exactly at (2, 3)', '')
    out.append(('(6)`s optional segment: present in the banked sentence, and the sentence without it (planted) matched with it absent',
                s6['opt'] is True and fill(s6['template'], bare)[1] is False, True))
    try:
        template(F[22].replace('IF IT COMPILES: "', 'IF IT COMPILES: '), 'IF IT COMPILES: "')
        refused = False
    except SystemExit:
        refused = True
    out.append(('a template whose marker is missing (planted) refused', refused, True))
    tag, obj, peel = tag_peel()
    out.append(('the tag read from the gated push`s capture: %s, peel %s, local equal to remote' % (tag, peel[:8]), tag == 'v0.2.0' and peel.startswith('e5ebdd15'), True))
    date = stamp()[:10]
    composed = [note_a(S, date), note_c(S, date), note_d(S, date)] + section_b(S, date) + trail_lines(F, date)[0]
    out.append(('the composed lines, %d, withheld by no kind' % len(composed), all(DOORS.withheld(t, acct, word) == [] for t in composed), True))
    out.append(('a planted copy carrying the account withheld', 'the account' in DOORS.withheld(composed[0] + ' ' + (acct or 'x'), acct, word), True))
    out.append(('(a) and (b) carry no sentence of (6); (c) and (d) carry all five', s6['sentence'] not in composed[0]
                and all(s6['sentence'] != x for x in section_b(S, date)) and s6['sentence'] in composed[1] and s6['sentence'] in composed[2], True))
    out.append(('(a) closes with the ruling`s words', composed[0].endswith('none written into a section here; §6 to §8 take these up.*'), True))
    out.append(('(d) closes with the ruling`s words', composed[2].endswith('The tags confer no deposit.*'), True))
    tl, cuts = trail_lines(F, date)
    out.append(('(e): [L22] cut whole and closing "(the navigator`s)" ; the four orders and the KEIPER words read once each ; 9 lines',
                tl[-1].endswith(" (the navigator's)") and len(tl) == 9 and all(('`%s` CARRIED' % n) in x for n, x in zip(FOUR, tl[3:7])), True))
    try:
        append_block(b'no newline', ['x'])
        refused = False
    except SystemExit:
        refused = True
    out.append(('the append refused on a file not ending with a newline (planted)', refused, True))
    out.append(('one blank line before each appended line, a blank already at the end or not (planted)',
                append_block(b'a\n', ['X', 'Y']) == (b'a\n\nX\n\nY\n', [3, 5]) and append_block(b'a\n\n', ['X']) == (b'a\n\nX\n', [3]), True))
    try:
        eol_of(b'a\r\nb\n')
        refused = False
    except SystemExit:
        refused = True
    out.append(('a file mixing line endings refused (planted)', refused, True))
    plant = (b'h\n\n*v0.1*\n\n' + b''.join(b'*Dated note, 2026-11-0%d, x*\n\n' % n for n in range(1, 6))
             + b'*Dated note, 2026-11-15, b756: y*\n\n## 1\n')
    ins, at = insert_note(plant, 'N', 15)
    out.append(('the insert on a planted file in the form: the note at :17, the bytes before and after the place kept whole',
                at == 17 and ins.split(b'\n')[16] == b'N' and ins.split(b'\n')[15] == b'' and kept_whole('a', plant, ins), True))
    try:
        insert_note(plant.replace(b'2026-11-15, b756', b'2026-11-15, b75X'), 'N', 15)
        refused = False
    except SystemExit:
        refused = True
    out.append(('the insert refused where :15 is not b756`s note (planted)', refused, True))
    try:
        compose('e', b'x\n' * 5, date, S, F)
        refused = False
    except SystemExit:
        refused = True
    out.append(('the trail block refused on a file not ending at b756`s Next line (planted)', refused, True))
    ok = all(a == b for _, a, b in out)
    for n, a, b in out:
        print('  CONTROL %s: %s (wanted %s)' % (n, a, b))
    for k in ('4', 'T0', 'T1', '6', '7'):
        print('    (%s) %s, the ferry :%d ; fields %s%s' % (k, S[k]['outcome'], S[k]['fline'], S[k]['fields'],
                                                         ' ; the optional segment present' if S[k]['opt'] else ''))
    print('### CONTROLS %d OF %d AS WANTED ; the account and the word read at run time, neither printed' % (
        sum(1 for _, a, b in out if a == b), len(out)))
    return ok


# ### ---------------------------------------------------------------- the bank and the modes
def load():
    return json.load(open(BANK, encoding='utf-8')) if os.path.exists(BANK) else {'act': ACT, 'clause': '(R367)(9)', 'items': {}}


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
        return 0 if controls() else 1
    if step == 'moved':
        rows, named = moved()
        text = moved_text(rows, named)
        print(text)
        if '--bank' in argv:
            with open(MOVED + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
                fh.write(text)
            os.replace(MOVED + '.tmp', MOVED)
            print('BANKED: data/b757_notes_moved.txt')
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
        _, prior = gitb(PP, 'show', '%s:%s' % (e['pp_head'], rel))   # ### the file at the write's own HEAD, composed again with its date
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
    if not controls():
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    S, F = sentences(), at_head(FERRY, 30)
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
    print('  PLACE-papers HEAD %s ; nothing staged %s ; the date %s' % (head.strip()[:8], staged, date))
    for q in todo:
        rel = ITEMS[q]['rel']
        path = os.path.join(PP, rel)
        clean = subprocess.run(['git', '-C', PP, 'diff', '--quiet', 'HEAD', '--', rel]).returncode == 0
        data = open(path, 'rb').read()
        present = (ITEMS[q]['present'] % date).encode('utf-8') in data
        after, rows, added = compose(q, data, date, S, F)
        print('  (%s) clean against HEAD %s ; written already %s' % (q, clean, present))
        show(q, rows, added, data, after, acct, word)
        wh = [w for _, s, _ in rows for w in DOORS.withheld(s, acct, word)]
        bad = not clean or present or wh or not kept_whole(q, data, after) or not staged
        if step == 'dry':
            print('  (%s) DRY: nothing written%s' % (q, ' ; WOULD BE REFUSED' if bad else ''))
            continue
        if bad:
            raise SystemExit('### (%s) NOT CLEAN, WRITTEN ALREADY, WITHHELD, NOT KEPT WHOLE OR SOMETHING STAGED -- NOTHING WRITTEN' % q)
        mv = None
        if q == 'a':
            mrows, named = moved()
            mv = dict(named=named, lines=[dict(repo=r_, path=p_, line=l_, cites=c_, moved=m_, digest=d_) for r_, p_, l_, c_, m_, d_ in mrows])
            print(moved_text(mrows, named))
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
                         'sentences': dict((x, S[x]['outcome']) for x in ITEMS[q].get('keys', ())),
                         'lines': [{'line': n, 'digest': digest(s), 'chars': len(s), 'kind': kd} for n, s, kd in rows],
                         'moved_cites': mv, 'confirm': None}
        bank(R)
        print('  then: `commit.py pp add %s`, its commit, then `tools/b757_notes.py confirm %s`' % (rel, q))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
