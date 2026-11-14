# -*- coding: utf-8 -*-
"""b754_sitting.py -- (R364)(5)[A]: THE REFERENCE LAYER'S PASSED ITEMS WRITTEN, each row banked in data/b754_sitting.json.

THE WORD. The author's answer to the [A] put (data/b754_put_2.json), banked by the answers route at data/b754_author_answers.txt :28
(2026-11-13T20:50:03Z): [A1] form (a), [A2] form (b), [A3] form (a), [A4] form (a), [A5] passed. The tool reads that line at every run and
refuses an item whose label it does not find there.
THE DRAFTS. Each is the ruling's own words, cut from data/b754_ferry.txt at HEAD (:20 to :24) between two exact needles, each needle found
once in its line; [A4]'s closing cites read as the amendment row 3 (3) gives them (b754_agenda.AMEND_A4, found once). The seat changes no
word of a draft: the drafts' date 2026-11-12 stands as the ruling wrote it, and the row carries the date of the write.
THE WRITE. Each write to FINDINGS.md replaces one line by one line ((R364)(5)[A]): the file's line count printed before and after and the
write refused unequal; every line but the item's read byte-equal after it; each line's ending kept. Before it: the CURRENT of each line the
item writes read at PLACE-papers HEAD and compared with the agenda's quoted line (data/b754_agenda.txt at relay HEAD), a mismatch refusing
the item; the file clean against HEAD; none of the item's lines among [Q] row (3)'s lines (the word read at run time from REGISTRY :373 and
never printed). The tool commits nothing: each item's FINDINGS write is committed through the one-call tool in a message of its own.
[A5]. PLACE-papers' description in the form of tools/b736_sitting.py :458-:472, each remote call its own command ((R364)(8)): `a5 read`
(gh in PLACE-papers' clone, the repository named by no argument, captured to the state folder), `a5 write` (the capture of today compared
with the agenda's CURRENT, then `gh repo edit --description <draft>`), `a5 back` (the read-back, compared with the draft, the row banked).
[B2] [B4] [B6] [B7]. The four kernels' descriptions passed at the [B] put (data/b754_put_3.json), the word banked by the answers route
at data/b754_author_answers.txt :88 (2026-11-13T21:20:15Z): [B1] and [B3] carried to a later sitting, [B2] and [B4] both passed, [B6]
and [B7] both passed, the readings ruled with no write standing. Each by the route of [A5] in the door's own clone, the repository named
by no argument: `b <item> read`, `b <item> write` (today's read equal to the agenda's CURRENT, then the draft cut from data/b754_ferry.txt
at HEAD, :28, :30, :32 or :33, between `DRAFTED: "` and the line's closing quote), `b <item> back` (the read-back equal to the draft, the
row banked). The READMEs of [B1] and [B3] are not written by this tool.
[L]. The lines for OPEN_TRAILS passed whole at the [L] put (data/b754_put_9.json), the word banked by the answers route at
data/b754_author_answers.txt :171 (2026-11-14T00:06:20Z): [L6], [L7] and [L8] cut from data/b754_ferry.txt :48 by the agenda's own reader
(b754_agenda.split_sub), [L14] and [L15] from the amendment rows 3 and 4 by its cut_words, each read against the digest the agenda banked;
[L1] to [L5] held with the sweep of (4)(iv), [L9] to [L13] carried by (8). Appended at OPEN_TRAILS.md's end under one dated head, a blank
line before the head and between two lines, [L6], [L7], [L8] and [L14] each closing with the words "(the navigator's)" and [L15] carrying
them in its own words, as the put said; the file's bytes before the write a prefix of its bytes after, the count before read against the
agenda's CURRENT, the two lines the items bear on (:2691, :3384) read by the agenda's digests. `l dry`, `l write` (the row banked), `l
confirm` (after the PLACE-papers commit: HEAD touching OPEN_TRAILS.md alone, its appended lines the row's).
[R]. The record lines passed at the [R] put (data/b754_put_10.json), the word banked by the answers route at data/b754_author_answers.txt
:182 (2026-11-14T00:17:39Z): both passed, [R2] carried by (8). The passed texts are cut from the word's RESULT line between needles met
once, each read against its draft in data/b754_ferry.txt :50 (the draft's digest equal to the agenda's): [R1]'s line equal to its draft's
words with the head and two substitutions; [R3]'s headings cut from its draft, §8's title the put's; the dated note with its cite set to
:182 and dated the day of the write. [R1] appended at INSTRUMENTS.md's end after a blank line; [R3] replaces :216 and :218 one line for one
line and inserts a blank line and the note after :11, the file's last dated note, every other line moving by two and byte-equal. The
CURRENT of each file read against the agenda's; no written line within two of the [Q] word's lines. `r <R1|R3> dry`, `r <R1|R3> write`
(the row banked), `r <R1|R3> confirm` (after its PLACE-papers commit: HEAD touching the item's file alone, the numstat the row's).
THE FOOT (data/b754_ferry.txt :54). `foot dry|write` renders data/b754_sitting.txt after the last put: one row per item of the agenda in
its order, its state, the author's label read at its RESULT line and compared, what was written (the sitting bank's confirmation or the
bank and commit that carry it) or why nothing was; the sitting's git writes from the step rows, each paired with its block of the
per-commit scan bank and read 0 ; 0 ; 0 ; 0; the writes beyond git; the author's answers and word with their times and the appends of the
route that banked them; and the foot line counting them. Refused where a label reads unequal, a cited commit is not among the steps, a
scan block is missing or not zero, or a line is withheld by a kind.

  python -X utf8 -u tools/b754_sitting.py control          the controls alone, nothing written and nothing read remotely
  python -X utf8 -u tools/b754_sitting.py dry <A1..A4>     the controls, the CURRENT against the agenda, the lines composed; nothing written
  python -X utf8 -u tools/b754_sitting.py write <A1..A4>   the same, then FINDINGS.md written and the item's row banked
  python -X utf8 -u tools/b754_sitting.py confirm <A1..A4> after the item's commit: PLACE-papers HEAD touching FINDINGS.md alone, its lines
                                                           the row's; the commit written to the row
  python -X utf8 -u tools/b754_sitting.py a5 <read|write|back>
  python -X utf8 -u tools/b754_sitting.py b <B2|B4|B6|B7> <read|write|back>
  python -X utf8 -u tools/b754_sitting.py l <dry|write|confirm>
  python -X utf8 -u tools/b754_sitting.py r <R1|R3> <dry|write|confirm>
  python -X utf8 -u tools/b754_sitting.py foot <dry|write>
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
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import statedir   # noqa: E402
import b754_agenda as AG   # noqa: E402
import b754_doors as DOORS   # noqa: E402

ACT = 'b754'
SELF = 'tools/%s_sitting.py' % ACT
BANK = os.path.join(RELAY, 'data', '%s_sitting.json' % ACT)
CAP = statedir.act_dir(ACT, 'sitting')
PP = AG.PP
FREL = 'FINDINGS.md'
FPATH = os.path.join(PP, FREL)
NL = '\n'
ANSWERS = 'data/%s_author_answers.txt' % ACT
ANSWERS_LINE = 28
WORD_AT = '2026-11-13T20:50:03Z'
WORD_CITE = '%s :%d' % (ANSWERS, ANSWERS_LINE)
# ### the label the author chose at each question of data/b754_put_2.json, and the form it passes
LABELS = {'[A1]': '(a) edited in place (Recommended)', '[A2]': '(b) retired (Recommended)', '[A3]': '(a) edited in place (Recommended)',
          '[A4]': '[A4] (a), [A5] passed (Recommended)'}
FORMS = {'[A1]': '(a)', '[A2]': '(b)', '[A3]': '(a)', '[A4]': '(a)', '[A5]': 'passed'}
LABEL_OF = {'[A5]': '[A4]'}   # ### [A5] answered with [A4] in the put's fourth question
# ### each write: (FINDINGS line, kind, opening needle, closing needle); kinds: 'line' the line replaced whole, 'tags' the line's tag words
# ### replaced and its words after them kept, 'head' the draft put at the line's head with its own words kept after it
SPEC = {'[A1]': [(901, 'line', 'Line :901 replaced by: "', '" Line :902'),
                 (902, 'tags', "Line :902's tag words replaced by \"", '", the deposit sentence')],
        '[A2]': [(979, 'head', 'Line :979 gains at its head, its own words staying after it: "', '" Where [A1] does not pass as (a)')],
        '[A3]': [(897, 'line', 'Line :897 replaced by: "', '" and line :898 by "'),
                 (898, 'line', 'and line :898 by "', '" FORM (b), RETIRED.')],
        '[A4]': [(905, 'line', 'Line :905 replaced by: "', '" and line :906 by "'),
                 (906, 'line', 'and line :906 by "', '" FORM (b), RETIRED.')]}
A2_POINTER = ('the anchor `riemann-hypothesis`', 'REGISTRY :953-:965')   # ### [A2]'s pointer where [A1] does not pass as (a)
TAGS = re.compile(r'^(\*[^*]+\* —) (?=\*\*)')
LINE_CUR = re.compile(r'^    :(\d+) "(.*)"$')
LINE_DIG = re.compile(r'^    :(\d+) BY LINE AND DIGEST ([0-9a-f]{16})')
A5_CUR = re.compile(r'^  CURRENT \(by gh at ([0-9T:\-]+Z), data/b754_doors\.txt\): "(.*)"$')
# ### [B]: the word on the [B] put (data/b754_put_3.json), banked by the answers route at data/b754_author_answers.txt :88
B_ANSWERS_LINE = 88
B_WORD_AT = '2026-11-13T21:20:15Z'
B_WORD_CITE = '%s :%d' % (ANSWERS, B_ANSWERS_LINE)
B_RESULT = 'RESULT (transcript line 11d67961:15385, %s' % B_WORD_AT[:-1]
# ### each question of the put by its opening words, and the label the author chose there
B_LABELS = {'[B1] and [B3]': 'Carried to a later sitting', '[B2] and [B4]': 'Both passed (Recommended)',
            '[B6] and [B7]': 'Both passed (Recommended)', "[B]'s paragraph": 'They stand (Recommended)'}
# ### each description item: its door, and the question that answered it
B_ITEMS = {'[B2]': ('SIDE-explicit-formula', '[B2] and [B4]'), '[B4]': ('SIDE-kernel', '[B2] and [B4]'),
           '[B6]': ('SIDE-bsd-multiplicity', '[B6] and [B7]'), '[B7]': ('SIDE-trivium', '[B6] and [B7]')}
B_CUR = re.compile(r'^  CURRENT: (SIDE-[a-z0-9\-]+)`s description by gh at ([0-9T:\-]+Z): "(.*)"$')
# ### [L]: the word on the [L] put (data/b754_put_9.json), banked by the answers route at data/b754_author_answers.txt :171
L_ANSWERS_LINE = 171
L_WORD_AT = '2026-11-14T00:06:20Z'
L_WORD_CITE = '%s :%d' % (ANSWERS, L_ANSWERS_LINE)
L_QUESTION = '[L] THE LINES FOR OPEN_TRAILS'
L_LABEL = 'Passed whole (Recommended)'
L_ITEMS = ('[L6]', '[L7]', '[L8]', '[L14]', '[L15]')
L_MARK = " (the navigator's)"
L_MARKED = ('[L6]', '[L7]', '[L8]', '[L14]')   # ### [L15] carries the words in its own text
OREL = 'OPEN_TRAILS.md'
OPATH = os.path.join(PP, OREL)
L_DRAFTED = re.compile(r'^(\[L\d+\]) DRAFTED.*digest ([0-9a-f]{16})\):$')
L_CUR = re.compile(r'^  CURRENT: OPEN_TRAILS\.md at main, (\d+) lines; .*\(OPEN_TRAILS :2691 ([0-9a-f]{16}) ; :3384 ([0-9a-f]{16})\)$')
# ### [R]: the word on the [R] put (data/b754_put_10.json), banked by the answers route at data/b754_author_answers.txt :182
R_ANSWERS_LINE = 182
R_WORD_AT = '2026-11-14T00:17:39Z'
R_WORD_CITE = '%s :%d' % (ANSWERS, R_ANSWERS_LINE)
R_QUESTION = '[R] THE RECORD LINES'
R_LABEL = 'Both passed (Recommended)'
IREL = 'phase1.5/method/INSTRUMENTS.md'
EREL = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
R_REL = {'[R1]': IREL, '[R3]': EREL}
R_ITEMS = ('[R1]', '[R3]')
# ### the passed texts cut from the word's RESULT line between needles, each met once
R1_NEEDLES = ('appended at INSTRUMENTS\' end after a blank line, no line moving: "', '" [R3]:')
R3_NOTE_NEEDLES = ('the two headings then at :218 and :220: "', '" No body written.')
R3_TITLE8_NEEDLES = ('(§8 "', '"; §9 the back matter')
R3_CITE = ('(relay data/b754_author_answers.txt, the line of this answer)', '(relay data/b754_author_answers.txt :%d)' % R_ANSWERS_LINE)
# ### [R1]'s line read against its draft (data/b754_ferry.txt :50): the head, then the draft's words after R1_FROM with two substitutions
R1_HEAD = "*Cross-reference (b754, ruling `(R364)`(5)[R1]).* To "
R1_FROM = "gains its cross-reference by a line appended in the instruments' own form: to "
R1_SUBS = (('data/', 'relay data/'), ('((R363)(3)(i);', '(`(R363)`(3)(i);'))
# ### [R3]'s two headings cut from its draft between needles
R3_HEAD_NEEDLES = {216: (':216 "', '"; :218 "'), 218: (':218 "', '"; one dated note')}
R3_NOTE_AFTER = 11   # ### the file's last dated note, :11; the note goes after it with a blank line
R_DRAFTED = re.compile(r'^(\[R\d\]) DRAFTED \(digest ([0-9a-f]{16})\):$')
R_CUR_I = re.compile(r'^  CURRENT: INSTRUMENTS :764 "(.*)"$')
R_CUR_E = re.compile(r'^  CURRENT: THE_EPSTEIN_CONTROL_OBJECT_v0_1\.md, (\d+) lines ; :216 "(.*)" ; :218 "(.*)" ; ')
R_INSTRUMENTS_LINES = 768   # ### the count the put gave (data/b754_put_10.json), read at PLACE-papers a9087a6d


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def run(argv, cwd=None):
    r = subprocess.run(argv, capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=cwd)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def bdigest(b):
    return hashlib.sha256(b).hexdigest()[:16]


# ---------------------------------------------------------------- the word
def word_labels(line):
    """{item: label} from the answers bank's RESULT line: each question opening on its item's tag, the label after its `"="`."""
    out = {}
    parts = line.split('"="')
    for i in range(1, len(parts)):
        q = parts[i - 1]
        j = q.rfind('"[A')
        m = re.match(r'"(\[A\d\])', q[j:]) if j >= 0 else None
        if m:
            out[m.group(1)] = parts[i].split('"', 1)[0]
    return out


def the_word():
    L = AG.git(RELAY, 'show', 'HEAD:%s' % ANSWERS).replace('\r', '').split(NL)
    line = L[ANSWERS_LINE - 1] if len(L) >= ANSWERS_LINE else ''
    if not line.startswith('RESULT (transcript line 11d67961:14163, %s' % WORD_AT[:-1]):
        raise SystemExit('### THE WORD NOT AT %s: the line opens %r -- NOTHING DONE' % (WORD_CITE, line[:80]))
    return word_labels(line)


def word_ok(item, got):
    q = LABEL_OF.get(item, item)
    return got.get(q) == LABELS[q]


def b_word_labels(line):
    """{question: label} from the [B] RESULT line: each question named by the B_LABELS key it opens on, the label after its `"="`."""
    out = {}
    parts = line.split('"="')
    for i in range(1, len(parts)):
        q = parts[i - 1]
        at = [(q.rfind('"' + k), k) for k in B_LABELS if q.rfind('"' + k) >= 0]
        if at:
            out[max(at)[1]] = parts[i].split('"', 1)[0]
    return out


def b_word():
    L = AG.git(RELAY, 'show', 'HEAD:%s' % ANSWERS).replace('\r', '').split(NL)
    line = L[B_ANSWERS_LINE - 1] if len(L) >= B_ANSWERS_LINE else ''
    if not line.startswith(B_RESULT):
        raise SystemExit('### THE [B] WORD NOT AT %s: the line opens %r -- NOTHING DONE' % (B_WORD_CITE, line[:80]))
    return b_word_labels(line)


def b_word_ok(item, got):
    q = B_ITEMS[item][1]
    return got.get(q) == B_LABELS[q] and B_LABELS[q].startswith('Both passed')


# ---------------------------------------------------------------- the drafts
def cut(text, a, b):
    """the words between needle a and needle b, each found once in text; None where either is not found once."""
    if text.count(a) != 1 or text.count(b) < 1:
        return None
    i = text.index(a) + len(a)
    j = text.find(b, i)
    if j < 0 or text.count(b, i) != 1:
        return None
    return text[i:j]


def drafts(FL, a1_form=None):
    """{item: [(line, kind, draft, ferry line)]} cut from the ferry bank; None for a draft whose needles do not meet their line once."""
    out = {}
    for item, specs in SPEC.items():
        n = [x for x in AG.FERRY if x[0] == item][0][1]
        text = AG.draft(FL, item)
        rows = []
        for k, kind, a, b in specs:
            d = cut(text, a, b)
            if d is not None and item == '[A4]' and k == 905:
                d = d.replace(*AG.AMEND_A4) if d.count(AG.AMEND_A4[0]) == 1 else None
            if d is not None and item == '[A2]' and (a1_form or FORMS['[A1]']) != '(a)':
                d = d.replace(*A2_POINTER) if d.count(A2_POINTER[0]) == 1 else None
            rows.append((k, kind, d, n))
        out[item] = rows
    return out


def a5_draft(FL, tag='[A5]'):
    s = AG.draft(FL, tag)
    a = 'DRAFTED: "'
    if s.count(a) != 1 or not s.endswith('"'):
        return None
    return s[s.index(a) + len(a):-1]


def b_current(A):
    """{door: (time, words)} from the agenda's [B2], [B4], [B6] and [B7] CURRENT lines of a description by gh."""
    out = {}
    for l in A:
        m = B_CUR.match(l)
        if m:
            out[m.group(1)] = (m.group(2), m.group(3))
    return out


# ---------------------------------------------------------------- the file, one line for one line
def split_bytes(data):
    """(parts, count): the file split at b'\\n', each part keeping a b'\\r' it carries; count the lines as a reader counts them."""
    parts = data.split(b'\n')
    return parts, len(parts) - (1 if parts[-1] == b'' else 0)


def get_line(parts, k):
    raw = parts[k - 1]
    return (raw[:-1] if raw.endswith(b'\r') else raw).decode('utf-8')


def put_lines(data, new):
    """data with each line k of `new` replaced, its ending kept; refused where a new line carries a line break."""
    parts, n0 = split_bytes(data)
    for k, s in new.items():
        if '\n' in s or '\r' in s or not (0 < k <= n0):
            raise SystemExit('### NOT ONE LINE FOR ONE LINE at :%d -- NOTHING WRITTEN' % k)
        cr = parts[k - 1].endswith(b'\r')
        parts[k - 1] = s.encode('utf-8') + (b'\r' if cr else b'')
    out = b'\n'.join(parts)
    return out


def check_write(before, after, new):
    """(count before, count after, lines differing outside the item's): the write's own reading."""
    pb, nb = split_bytes(before)
    pa, na = split_bytes(after)
    other = [k for k in range(1, min(len(pb), len(pa)) + 1) if k not in new and pb[k - 1] != pa[k - 1]]
    wrong = [k for k in new if get_line(pa, k) != new[k] or pa[k - 1].endswith(b'\r') != pb[k - 1].endswith(b'\r')]
    return nb, na, other + wrong + ([] if len(pb) == len(pa) else ['parts %d -> %d' % (len(pb), len(pa))])


def compose(item, F, D):
    """[(k, kind, old, new, draft)] for the item over FINDINGS' lines F (text), from its drafts D[item]."""
    out = []
    for k, kind, d, n in D[item]:
        if d is None:
            raise SystemExit('### %s: THE DRAFT FOR :%d NOT CUT FROM data/b754_ferry.txt :%d -- NOTHING DONE' % (item, k, n))
        old = F[k - 1]
        if kind == 'line':
            new = d
        elif kind == 'tags':
            m = TAGS.match(old)
            if not m:
                raise SystemExit('### %s: :%d CARRIES NO TAG WORDS BEFORE ITS BOLD WORDS -- NOTHING DONE' % (item, k))
            new = d + old[len(m.group(1)):]
        elif kind == 'head':
            new = d + ' ' + old
        out.append((k, kind, old, new, d))
    return out


# ---------------------------------------------------------------- the agenda's CURRENT
def agenda_current(A):
    """{(item, line): ('text', words) or ('digest', d)} from the agenda's [A1]-[A4] CURRENT blocks; and [A5]'s (time, words)."""
    out, cur, a5 = {}, None, None
    for l in A:
        m = re.match(r'^(\[A\d\]) ', l)
        if m:
            cur = m.group(1)
            continue
        if l.startswith('## '):
            cur = None
        m1, m2, m3 = LINE_CUR.match(l), LINE_DIG.match(l), A5_CUR.match(l)
        if cur and m1:
            out[(cur, int(m1.group(1)))] = ('text', m1.group(2))
        elif cur and m2:
            out[(cur, int(m2.group(1)))] = ('digest', m2.group(2))
        if cur == '[A5]' and m3:
            a5 = (m3.group(1), m3.group(2))
    return out, a5


def agrees(entry, s):
    if entry is None:
        return False
    return entry[1] == s if entry[0] == 'text' else entry[1] == digest(s)


# ---------------------------------------------------------------- the bank
def rows():
    if not os.path.exists(BANK):
        return {}
    return json.load(io.open(BANK, encoding='utf-8')).get('rows', {})


def bank(R):
    j = {'what': '(R364)(5)[A], [B], [L] and [R] the passed items written by %s, one row an item; the words %s (%s) for [A], %s (%s) for [B], '
                 '%s (%s) for [L] and %s (%s) for [R]; the drafts cut from data/b754_ferry.txt at HEAD and, for [L14] and [L15], from the amendment '
                 'rows 3 and 4, and [R]`s passed texts from the word`s RESULT line, each read against its draft; the lines cited by line and digest' % (
                     SELF, WORD_CITE, WORD_AT, B_WORD_CITE, B_WORD_AT, L_WORD_CITE, L_WORD_AT, R_WORD_CITE, R_WORD_AT), 'at': stamp(), 'rows': R}
    with open(BANK + '.tmp', 'wb') as f:
        f.write((json.dumps(j, indent=1, ensure_ascii=False, sort_keys=True) + NL).encode('utf-8'))
    os.replace(BANK + '.tmp', BANK)
    print('  BANKED %s: %d row(s) %s' % (os.path.relpath(BANK, RELAY).replace('\\', '/'), len(R), sorted(R)))


# ---------------------------------------------------------------- the controls
def controls():
    C = []

    def case(name, ok, got):
        C.append(ok)
        print('  (%d) %-78s %s ; %s' % (len(C), name[:78], 'AS WANTED' if ok else 'NOT AS WANTED', got))
    print('### THE CONTROLS (%s)' % SELF)
    FL = AG.ferry_lines()
    D = drafts(FL)
    cuts = [(it, k) for it in D for (k, _kd, d, _n) in D[it] if d]
    case('every needle meets its ferry line once, every draft cut (7 of 7)', len(cuts) == 7, '%d of 7 %s' % (len(cuts), cuts))
    d905 = [d for (k, _kd, d, _n) in D['[A4]'] if k == 905][0] or ''
    case('[A4] :905 carries row 3 (3)`s cites once, the ruling`s form none', d905.count(AG.AMEND_A4[1]) == 1 and '(FINDINGS :6880-:6884)' not in d905,
         'amended %d' % d905.count(AG.AMEND_A4[1]))
    d979 = [d for (k, _kd, d, _n) in D['[A2]'] if k == 979][0] or ''
    D_b = drafts(FL, a1_form='(b)')
    d979b = [d for (k, _kd, d, _n) in D_b['[A2]'] if k == 979][0] or ''
    case('[A2]`s pointer the anchor`s name with [A1] (a); REGISTRY :953-:965 with a planted (b)', A2_POINTER[0] in d979 and A2_POINTER[1] in d979b
         and A2_POINTER[0] not in d979b, 'as passed %s ; planted %s' % (A2_POINTER[0] in d979, A2_POINTER[1] in d979b))
    planted_text = 'x "Line :901 replaced by: "a" Line :902 b "Line :901 replaced by: "c" Line :902'
    case('a needle met twice refuses its cut (planted)', cut(planted_text, 'Line :901 replaced by: "', '" Line :902') is None, 'None')
    W = the_word()
    case('the word read at %s: every item`s label the author chose' % WORD_CITE, all(word_ok(i, W) for i in FORMS), W)
    planted = dict(W, **{'[A2]': '(a) edited in place'})
    case('a planted word with [A2]`s label changed reads not passed as (b)', not word_ok('[A2]', planted), 'word_ok %s' % word_ok('[A2]', planted))
    data = b''.join(b'line %d\r\n' % k for k in range(1, 13))
    after = put_lines(data, {5: 'five'})
    nb, na, bad = check_write(data, after, {5: 'five'})
    case('a planted CRLF file of 12 lines: :5 written, the count equal, its CR kept, the rest byte-equal', nb == na == 12 and not bad
         and after.split(b'\n')[4] == b'five\r', 'count %d -> %d ; differing %s' % (nb, na, bad or 'none'))
    try:
        put_lines(data, {5: 'two\nlines'})
        refused = False
    except SystemExit:
        refused = True
    case('a planted draft carrying a line break refused', refused, 'refused %s' % refused)
    nb2, na2, bad2 = check_write(data, data.replace(b'line 7', b'line 7x'), {5: 'line 5'})
    case('a planted change outside the item`s line read by the check', 7 in bad2, 'differing %s' % bad2)
    case('the tag words read on a planted line; a line with none refused', TAGS.match('*a · b* — **X** y') is not None and TAGS.match('**X** y') is None,
         'matched %r' % (TAGS.match('*a · b* — **X** y').group(1)))
    A = AG.git(RELAY, 'show', 'HEAD:data/%s_agenda.txt' % ACT).replace('\r', '').split(NL)
    cur, a5 = agenda_current(A)
    want = sorted((it, k) for it in SPEC for (k, _kd, _a, _b) in SPEC[it])
    case('the agenda`s CURRENT found for every line the items write (7) and for [A5]', all(w in cur for w in want) and a5 is not None,
         '%d of %d ; [A5] %s' % (sum(1 for w in want if w in cur), len(want), a5[0] if a5 else None))
    e = cur.get(('[A3]', 897))
    case('a planted CURRENT one character apart reads not agreeing', e is not None and not agrees(e, (e[1] + 'x') if e[0] == 'text' else 'x'), 'agrees False')
    word = DOORS.q_word()
    F = AG.lines(PP, 'HEAD', FREL)
    R = AG.lines(PP, 'HEAD', 'REGISTRY.md')
    prot = AG.protected_lines(F, R, word)['FINDINGS.md']
    hit = [k for (_it, k) in want if k in prot]
    case('[Q] row (3): none of the items` lines protected; :820 protected (the word read, not printed)', not hit and 820 in prot and word is not None,
         'items` lines protected %s ; :820 %s' % (hit or 'none', 820 in prot))
    d5 = a5_draft(FL) or ''
    acct = DOORS.account(PP)
    case('[A5]`s draft cut from data/b754_ferry.txt :24, withheld by no kind', bool(d5) and d5.endswith('correction).') and not DOORS.withheld(d5, acct, word),
         '%d characters, digest %s' % (len(d5), digest(d5)))
    WB = b_word()
    case('the [B] word read at %s: every question`s label the author chose (4)' % B_WORD_CITE, all(WB.get(q) == B_LABELS[q] for q in B_LABELS), WB)
    case('[B2], [B4], [B6], [B7] read passed; [B1] and [B3] carried', all(b_word_ok(i, WB) for i in B_ITEMS)
         and WB.get('[B1] and [B3]') == 'Carried to a later sitting', 'passed %s' % sorted(i for i in B_ITEMS if b_word_ok(i, WB)))
    planted_b = dict(WB, **{'[B6] and [B7]': '[B6] only'})
    case('a planted [B] word answering `[B6] only` reads [B7] not passed', not b_word_ok('[B7]', planted_b), 'b_word_ok %s' % b_word_ok('[B7]', planted_b))
    bd = dict((i, a5_draft(FL, i) or '') for i in B_ITEMS)
    bacct = dict((i, DOORS.account(DOORS.CLONES[B_ITEMS[i][0]])) for i in B_ITEMS)
    case('the four [B] drafts cut from data/b754_ferry.txt :28, :30, :32, :33, withheld by no kind',
         all(bd[i] and not DOORS.withheld(bd[i], bacct[i], word) for i in B_ITEMS),
         ' ; '.join('%s %d characters, digest %s' % (i, len(bd[i]), digest(bd[i])) for i in sorted(B_ITEMS)))
    bc = b_current(A)
    case('the agenda`s CURRENT of a description by gh found for the four doors', all(B_ITEMS[i][0] in bc for i in B_ITEMS),
         ' ; '.join('%s %s' % (d, bc[d][0]) for d in sorted(bc)))
    # -------- [L]
    WL_ = l_word()
    case('the [L] word read at %s: %r' % (L_WORD_CITE, L_LABEL), WL_ == L_LABEL, repr(WL_))
    pl_line = 'RESULT (transcript line x): Your questions have been answered: "%s, planted. How does [L] go?"="Struck whole". You can' % L_QUESTION
    case('a planted [L] word answering `Struck whole` reads not passed', l_word_label(pl_line) == 'Struck whole', repr(l_word_label(pl_line)))
    LD = l_drafts()
    ldg, lcur = l_agenda(A)
    lagree = [t for t in L_ITEMS if LD.get(t) and ldg.get(t) == digest(LD[t])]
    case('the five [L] drafts cut, each digest equal to the agenda`s (5 of 5)', len(lagree) == 5,
         ' ; '.join('%s %s/%s' % (t, digest(LD[t] or ''), ldg.get(t)) for t in L_ITEMS))
    case('a planted [L7] draft one character apart reads its digest unequal', bool(LD.get('[L7]')) and digest(LD['[L7]'] + 'x') != ldg.get('[L7]'), 'unequal')
    case('the agenda`s [L] CURRENT found: the count and the digests of :2691 and :3384', lcur is not None, repr(lcur))
    pdata = b'\xef\xbb\xbfa\nb\nc\n'
    pl = ['H', 'one', 'two']
    pafter = l_append(pdata, pl)
    pn0, pn1 = split_bytes(pdata)[1], split_bytes(pafter)[1]
    case('a planted file of 3 lines and 3 appended: its bytes a prefix, 3 + 6 = 9 lines, a blank before each', pafter.startswith(pdata) and pn0 == 3
         and pn1 == 9 and pafter.split(b'\n')[3:9] == [b'', b'H', b'', b'one', b'', b'two'], 'count %d -> %d' % (pn0, pn1))
    try:
        l_append(b'a\nb', ['x'])
        refused_l = False
    except SystemExit:
        refused_l = True
    case('a planted file not ending in a newline refused', refused_l, 'refused %s' % refused_l)
    lmark = l_compose(LD, '2026-01-01') if len(lagree) == 5 else []
    case('the head and the five lines withheld by no kind; [L6], [L7], [L8], [L14] marked, [L15] in its own words',
         len(lmark) == 6 and all(not withheld_l(s, acct, word) for s in lmark)
         and all(lmark[1 + i].endswith(L_MARK) == (t in L_MARKED) for i, t in enumerate(L_ITEMS)) and "the navigator's" in lmark[5],
         'lines %d' % len(lmark))
    # -------- [R]
    rline = r_result()
    case('the [R] word read at %s: %r' % (R_WORD_CITE, R_LABEL), r_word_label(rline) == R_LABEL, repr(r_word_label(rline)))
    pr_line = 'RESULT (transcript line x): Your questions have been answered: "%s, planted. How does [R] go?"="[R1] only". You can' % R_QUESTION
    case('a planted [R] word answering `[R1] only` reads not passed', r_word_label(pr_line) == '[R1] only', repr(r_word_label(pr_line)))
    rs = r_drafts()
    rdg, rcur = r_agenda(A)
    ragree = [t for t in R_ITEMS if rs.get(t) and rdg.get(t) == digest(rs[t])]
    case('the [R1] and [R3] drafts cut from data/b754_ferry.txt :50, each digest equal to the agenda`s (2 of 2)', len(ragree) == 2,
         ' ; '.join('%s %s/%s' % (t, digest(rs.get(t) or ''), rdg.get(t)) for t in R_ITEMS))
    TX = r_texts(rline, rs)
    case('[R1]`s line cut from the word equal to its draft with the head and the two substitutions', TX['[R1]'] is not None
         and TX['[R1]'] == TX['[R1] derived'], 'cut %s ; derived %s' % (digest(TX['[R1]'] or ''), digest(TX['[R1] derived'] or '')))
    case('a planted [R1] draft one character apart derives a line unequal to the word`s', r1_derived((rs.get('[R1]') or '') + 'x') != TX['[R1]'], 'unequal')
    case('[R3]: two headings cut from its draft, §8`s title the put`s; the note cut once, its cite :%d, no cite left unset' % R_ANSWERS_LINE,
         TX[216] is not None and TX[218] is not None and TX['title8'] is not None and TX[216] == '## 8. ' + TX['title8'] and TX[218].startswith('## 9. ')
         and TX['note'] is not None and TX['note'].count(R3_CITE[1]) == 1 and R3_CITE[0] not in TX['note'],
         'headings %d, %d characters ; note %d characters' % (len(TX[216] or ''), len(TX[218] or ''), len(TX['note'] or '')))
    case('the agenda`s [R] CURRENT found: INSTRUMENTS :764 and the Epstein document`s count, :216 and :218', rcur['I'] is not None and rcur['E'] is not None,
         'E %s' % (rcur['E'][0] if rcur['E'] else None))
    pd = b''.join(b'l%d\n' % k for k in range(1, 9))
    prep = {6: 'six', 8: 'eight'}
    pa = r_insert(put_lines(pd, prep), 2, ['', 'note'])
    pbad = r3_check(pd, pa, 2, ['', 'note'], prep)
    pp_ = pa.split(b'\n')
    case('a planted file of 8 lines: :6 and :8 replaced, a blank and a note after :2; 10 lines, the two at :8 and :10, the rest equal',
         not pbad and split_bytes(pa)[1] == 10 and pp_[2:4] == [b'', b'note'] and pp_[7] == b'six' and pp_[9] == b'eight' and pp_[4] == b'l3',
         'differing %s' % (pbad or 'none'))
    pbad2 = r3_check(pd, pa.replace(b'l4\n', b'l4x\n'), 2, ['', 'note'], prep)
    case('a planted change outside the item`s lines read by the check', bool(pbad2), 'differing %s' % pbad2)
    rlines = [TX['[R1]'] or '', TX[216] or '', TX[218] or '', TX['note'] or '']
    case('[R]`s four lines withheld by no kind', all(s and not withheld_l(s, acct, word) for s in rlines), 'lines %d' % len([s for s in rlines if s]))
    # -------- the foot
    AA = AG.git(RELAY, 'show', 'HEAD:%s' % ANSWERS).replace('\r', '').split(NL)
    put_rows = [t for t in FOOT_ITEMS if t[1]]
    feq = [t[0] for t in put_rows if len(AA) >= t[1] and foot_label(AA[t[1] - 1], t[2]) == t[3]]
    case('the foot: every put row`s label read equal at its RESULT line (%d of %d)' % (len(feq), len(put_rows)), len(feq) == len(put_rows),
         'unequal %s' % ([t[0] for t in put_rows if t[0] not in feq] or 'none'))
    pf = 'RESULT (transcript line x, 2026-01-01T00:00:00.0Z): Your questions have been answered: "[X1] one q"="Passed", "[X2] two q"="Struck". You can'
    case('the foot: a planted RESULT of two questions reads each label by its opening, an opening met in neither reads none',
         foot_label(pf, '[X1]') == 'Passed' and foot_label(pf, '[X2]') == 'Struck' and foot_label(pf, '[X3]') is None,
         '%r %r %r' % (foot_label(pf, '[X1]'), foot_label(pf, '[X2]'), foot_label(pf, '[X3]')))
    pscan = ('## THE SCAN BEFORE THE COMMIT, 2026-01-01T00:00:00Z, b754 commit component 3 in relay\nx\n### ### **PREVIOUS ADDRESS: 0 ; THE AUTHOR`S '
             'NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ; PLACES 9 ; CONTROLS 7 OF 7 AS WANTED ; 1 s.**\n## THE SCAN BEFORE THE COMMIT, '
             '2026-01-01T00:01:00Z, b754 commit component 3 in pp\n### ### **PREVIOUS ADDRESS: 1 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; '
             'THE ORCID: 0 ; PLACES 9 ; CONTROLS 7 OF 7 AS WANTED ; 1 s.**')
    pb_ = scan_blocks(pscan)
    case('the foot: two planted scan blocks read, the second`s address count 1 read not zero', len(pb_) == 2 and pb_[0]['foot'][:4] == (0, 0, 0, 0)
         and pb_[1]['foot'][:4] == (1, 0, 0, 0) and pb_[1]['repo'] == 'pp', '%d blocks' % len(pb_))
    stp = json.load(io.open(STEPS, encoding='utf-8'))['rows']
    sh = set(s['commit'][:8] for s in stp)
    cited = sorted(set(c for t in FOOT_ITEMS if t[6] for c in re.findall(r'\b(?:relay|PLACE-papers) ([0-9a-f]{8})\b', t[6])))
    case('the foot: every commit a row cites among the act`s steps (%d)' % len(cited), cited and all(c in sh for c in cited),
         'missing %s' % ([c for c in cited if c not in sh] or 'none'))
    ok = sum(C)
    print('### CONTROLS %d OF %d %s' % (ok, len(C), 'AS WANTED' if ok == len(C) else 'NOT AS WANTED'))
    return ok == len(C)


# ---------------------------------------------------------------- an item of [A1]-[A4]
def item_plan(item):
    W = the_word()
    if not word_ok(item, W):
        raise SystemExit('### %s: THE WORD AT %s READS %r, NOT %r -- NOTHING DONE' % (item, WORD_CITE, W.get(item), LABELS[item]))
    D = drafts(AG.ferry_lines())
    head = AG.git(PP, 'rev-parse', 'HEAD').strip()
    F = AG.lines(PP, 'HEAD', FREL)
    data = open(FPATH, 'rb').read()
    clean = AG.gitq(PP, 'diff', '--quiet', 'HEAD', '--', FREL)[0] == 0
    A = AG.git(RELAY, 'show', 'HEAD:data/%s_agenda.txt' % ACT).replace('\r', '').split(NL)
    cur, _a5 = agenda_current(A)
    plan = compose(item, F, D)
    print('### %s %s, the word %s (%s): label %r' % (item, FORMS[item], WORD_AT, WORD_CITE, LABELS[item]))
    print('  PLACE-papers HEAD %s ; FINDINGS.md clean against HEAD %s ; %d bytes' % (head[:8], clean, len(data)))
    agree = True
    for k, kind, old, new, d in plan:
        a = agrees(cur.get((item, k)), old)
        agree = agree and a
        print('  :%d %s ; CURRENT at HEAD digest %s, %d characters ; the agenda`s %s' % (k, kind, digest(old), len(old), 'AGREES' if a else 'DIFFERS'))
        print('      new digest %s, %d characters ; the draft %d characters (data/b754_ferry.txt :%d)' % (digest(new), len(new), len(d),
                                                                                                    [x for x in AG.FERRY if x[0] == item][0][1]))
        print('      NEW: %s' % new)
    for hk in [x[2] for x in AG.ANCHORS if x[0] == item]:
        print('  the heading :%d stands: %s' % (hk, F[hk - 1]))
    return dict(head=head, data=data, clean=clean, agree=agree, plan=plan, F=F)


def item_write(item, write):
    if not controls():
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    if item in rows():
        raise SystemExit('### %s HAS ITS ROW ALREADY -- NOTHING DONE' % item)
    P = item_plan(item)
    if not P['clean'] or not P['agree']:
        raise SystemExit('### %s: %s -- NOTHING WRITTEN' % (item, 'FINDINGS.md NOT CLEAN AGAINST HEAD' if not P['clean'] else 'THE CURRENT DIFFERS FROM THE AGENDA'))
    new = dict((k, n) for (k, _kd, _o, n, _d) in P['plan'])
    after = put_lines(P['data'], new)
    nb, na, bad = check_write(P['data'], after, new)
    print('  THE LINE COUNT: before %d ; after %d ; %s ; lines differing beyond the item`s: %s' % (nb, na, 'EQUAL' if nb == na else 'UNEQUAL', bad or 'none'))
    if nb != na or bad:
        raise SystemExit('### %s: NOT ONE LINE FOR ONE LINE -- NOTHING WRITTEN' % item)
    if not write:
        print('  DRY: nothing written')
        return
    at = stamp()
    with open(FPATH + '.tmp', 'wb') as f:
        f.write(after)
    os.replace(FPATH + '.tmp', FPATH)
    back = open(FPATH, 'rb').read()
    nb2, na2, bad2 = check_write(P['data'], back, new)
    print('  WRITTEN %s at %s ; read back: count %d -> %d, differing beyond the item`s %s, bytes %s' % (FREL, at, nb2, na2, bad2 or 'none',
                                                                                                  'EQUAL to the composed' if back == after else 'DIFFER'))
    if back != after or bad2 or nb2 != na2:
        raise SystemExit('### %s: THE READ-BACK DIFFERS -- restore FINDINGS.md through the one-call tool' % item)
    R = rows()
    R[item] = dict(form=FORMS[item], word_at=WORD_AT, word_cite=WORD_CITE, label=LABELS[item], state='WRITTEN, the commit through the one-call tool',
                   findings_head=P['head'], written_at=at, count_before=nb, count_after=na, sha_before=bdigest(P['data']), sha_after=bdigest(after),
                   lines=[dict(line=k, kind=kd, old_digest=digest(o), new_digest=digest(n), old_chars=len(o), new_chars=len(n),
                               draft_cite='data/b754_ferry.txt :%d' % [x for x in AG.FERRY if x[0] == item][0][1], agenda='AGREES')
                          for (k, kd, o, n, _d) in P['plan']],
                   note='the draft`s date 2026-11-12 stands as the ruling wrote it ((R364)(5): the seat changes no word); written %s' % at[:10],
                   confirm=None)
    bank(R)
    print('  then: `commit.py pp add FINDINGS.md`, its commit, then `%s confirm %s`' % (SELF, item.strip('[]')))


def item_confirm(item):
    R = rows()
    r = R.get(item)
    if not r or r.get('confirm'):
        raise SystemExit('### %s: %s -- NOTHING DONE' % (item, 'NO ROW' if not r else 'CONFIRMED ALREADY'))
    head = AG.git(PP, 'rev-parse', 'HEAD').strip()
    files = AG.git(PP, 'show', '--format=', '--name-only', 'HEAD').strip()
    num = AG.git(PP, 'show', '--format=', '--numstat', 'HEAD').strip()
    F = AG.lines(PP, 'HEAD', FREL)
    have = [digest(F[x['line'] - 1]) == x['new_digest'] for x in r['lines']]
    n = len(r['lines'])
    ok = files == FREL and num.split()[:2] == [str(n), str(n)] and all(have) and head != r['findings_head']
    print('### %s CONFIRM: PLACE-papers HEAD %s ; files %s ; numstat %s ; the row`s lines at HEAD %s ; %s' % (
        item, head[:8], files, num.split()[:2], have, 'AS WANTED' if ok else 'NOT AS WANTED'))
    if not ok:
        raise SystemExit('### %s: THE COMMIT DOES NOT CARRY THE ROW -- NOTHING WRITTEN' % item)
    r['confirm'] = 'PLACE-papers %s, FINDINGS.md alone, %d line(s) for %d' % (head[:8], n, n)
    r['state'] = 'PASS'
    bank(R)


# ---------------------------------------------------------------- [A5]
def a5_cap(kind):
    return os.path.join(CAP, 'A5_%s.json' % kind)


def a5_save(kind, rec):
    os.makedirs(CAP, exist_ok=True)
    with io.open(a5_cap(kind) + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(rec, ensure_ascii=False, indent=1) + NL)
    os.replace(a5_cap(kind) + '.tmp', a5_cap(kind))


def a5_load(kind):
    p = a5_cap(kind)
    return json.load(io.open(p, encoding='utf-8')) if os.path.exists(p) else None


def a5(step):
    if not controls():
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    if not word_ok('[A5]', the_word()):
        raise SystemExit('### [A5]: THE WORD AT %s DOES NOT READ PASSED -- NOTHING DONE' % WORD_CITE)
    if '[A5]' in rows():
        raise SystemExit('### [A5] HAS ITS ROW ALREADY -- NOTHING DONE')
    d = a5_draft(AG.ferry_lines())
    A = AG.git(RELAY, 'show', 'HEAD:data/%s_agenda.txt' % ACT).replace('\r', '').split(NL)
    _cur, a5c = agenda_current(A)
    today = stamp()[:10]
    gh = ['gh', 'repo', 'view', '--json', 'description', '-q', '.description']
    if step == 'read':
        t0 = stamp()
        rc, out, err = run(gh, cwd=PP)
        a5_save('read', dict(at=t0, rc=rc, out=out, err=err[:300]))
        print('%s READ PLACE-papers description: rc %d, %d characters ; the agenda`s CURRENT (%s) %s' % (t0, rc, len(out), a5c[0],
                                                                                                         'EQUAL' if out == a5c[1] else 'DIFFERS'))
        return
    if step == 'write':
        r = a5_load('read')
        if not r or r['rc'] or r['at'][:10] != today or r['out'] != a5c[1]:
            raise SystemExit('### [A5]: NO READ OF TODAY EQUAL TO THE AGENDA`S CURRENT (%s) -- NOTHING WRITTEN' % (r and (r['at'], r['rc'], r['out'] == a5c[1])))
        if a5_load('write') and a5_load('write')['at'][:10] == today:
            raise SystemExit('### [A5]: WRITTEN ALREADY TODAY (%s) -- read it back' % a5_load('write')['at'])
        t0 = stamp()
        rc, out, err = run(['gh', 'repo', 'edit', '--description', d], cwd=PP)
        a5_save('write', dict(at=t0, rc=rc, out=out[:300], err=err[:300], draft_digest=digest(d)))
        print('%s WRITE PLACE-papers description by gh repo edit: rc %d%s ; the draft %d characters, digest %s' % (t0, rc, (' ; ' + err[:200]) if rc else '',
                                                                                                                  len(d), digest(d)))
        return
    if step == 'back':
        w, r = a5_load('write'), a5_load('read')
        if not w or w['rc']:
            raise SystemExit('### [A5]: NO WRITE TO READ BACK -- NOTHING DONE')
        t0 = stamp()
        rc, out, err = run(gh, cwd=PP)
        a5_save('back', dict(at=t0, rc=rc, out=out, err=err[:300]))
        eq = rc == 0 and out == d
        print('%s READ BACK PLACE-papers description: rc %d, %d characters ; the draft %s' % (t0, rc, len(out), 'EQUAL' if eq else 'DIFFERS'))
        if not eq:
            raise SystemExit('### [A5]: THE READ-BACK DIFFERS -- no row banked')
        R = rows()
        R['[A5]'] = dict(form='passed', word_at=WORD_AT, word_cite=WORD_CITE, label=LABELS['[A4]'], state='PASS',
                         read='by gh %s, digest %s, %d characters, the agenda`s CURRENT (by gh %s) EQUAL' % (r['at'], digest(r['out']), len(r['out']), a5c[0]),
                         compared='EQUAL', draft='data/b754_ferry.txt :24, digest %s, %d characters' % (digest(d), len(d)),
                         written_at=w['at'], confirm='gh read back %s, equal' % t0, findings_head=None)
        bank(R)
        return
    raise SystemExit('usage: %s a5 <read|write|back>' % SELF)


# ---------------------------------------------------------------- [B2] [B4] [B6] [B7]
def b_cap(item, kind):
    return os.path.join(CAP, '%s_%s.json' % (item.strip('[]'), kind))


def b_save(item, kind, rec):
    os.makedirs(CAP, exist_ok=True)
    with io.open(b_cap(item, kind) + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(rec, ensure_ascii=False, indent=1) + NL)
    os.replace(b_cap(item, kind) + '.tmp', b_cap(item, kind))


def b_load(item, kind):
    p = b_cap(item, kind)
    return json.load(io.open(p, encoding='utf-8')) if os.path.exists(p) else None


def b(item, step):
    if item not in B_ITEMS:
        raise SystemExit('usage: %s b <B2|B4|B6|B7> <read|write|back>' % SELF)
    if not controls():
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    if not b_word_ok(item, b_word()):
        raise SystemExit('### %s: THE WORD AT %s DOES NOT READ PASSED -- NOTHING DONE' % (item, B_WORD_CITE))
    if item in rows():
        raise SystemExit('### %s HAS ITS ROW ALREADY -- NOTHING DONE' % item)
    door, q = B_ITEMS[item]
    clone = DOORS.CLONES[door]
    n = [x for x in AG.FERRY if x[0] == item][0][1]
    d = a5_draft(AG.ferry_lines(), item)
    if not d:
        raise SystemExit('### %s: NO DRAFT CUT FROM data/b754_ferry.txt :%d -- NOTHING DONE' % (item, n))
    A = AG.git(RELAY, 'show', 'HEAD:data/%s_agenda.txt' % ACT).replace('\r', '').split(NL)
    bc = b_current(A).get(door)
    if not bc:
        raise SystemExit('### %s: NO CURRENT OF %s`s DESCRIPTION IN THE AGENDA -- NOTHING DONE' % (item, door))
    today = stamp()[:10]
    gh = ['gh', 'repo', 'view', '--json', 'description', '-q', '.description']
    if step == 'read':
        t0 = stamp()
        rc, out, err = run(gh, cwd=clone)
        b_save(item, 'read', dict(door=door, at=t0, rc=rc, out=out, err=err[:300]))
        print('%s READ %s %s description: rc %d, %d characters ; the agenda`s CURRENT (%s) %s' % (t0, item, door, rc, len(out), bc[0],
                                                                                                 'EQUAL' if out == bc[1] else 'DIFFERS'))
        return
    if step == 'write':
        r = b_load(item, 'read')
        if not r or r['rc'] or r['at'][:10] != today or r['out'] != bc[1]:
            raise SystemExit('### %s: NO READ OF TODAY EQUAL TO THE AGENDA`S CURRENT (%s) -- NOTHING WRITTEN' % (item, r and (r['at'], r['rc'], r['out'] == bc[1])))
        if b_load(item, 'write') and b_load(item, 'write')['at'][:10] == today:
            raise SystemExit('### %s: WRITTEN ALREADY TODAY (%s) -- read it back' % (item, b_load(item, 'write')['at']))
        t0 = stamp()
        rc, out, err = run(['gh', 'repo', 'edit', '--description', d], cwd=clone)
        b_save(item, 'write', dict(door=door, at=t0, rc=rc, out=out[:300], err=err[:300], draft_digest=digest(d)))
        print('%s WRITE %s %s description by gh repo edit: rc %d%s ; the draft %d characters, digest %s' % (t0, item, door, rc,
                                                                                                          (' ; ' + err[:200]) if rc else '', len(d), digest(d)))
        return
    if step == 'back':
        w, r = b_load(item, 'write'), b_load(item, 'read')
        if not w or w['rc'] or w.get('draft_digest') != digest(d):
            raise SystemExit('### %s: NO WRITE OF THIS DRAFT TO READ BACK -- NOTHING DONE' % item)
        t0 = stamp()
        rc, out, err = run(gh, cwd=clone)
        b_save(item, 'back', dict(door=door, at=t0, rc=rc, out=out, err=err[:300]))
        eq = rc == 0 and out == d
        print('%s READ BACK %s %s description: rc %d, %d characters ; the draft %s' % (t0, item, door, rc, len(out), 'EQUAL' if eq else 'DIFFERS'))
        if not eq:
            raise SystemExit('### %s: THE READ-BACK DIFFERS -- no row banked' % item)
        R = rows()
        R[item] = dict(form='passed', door=door, word_at=B_WORD_AT, word_cite=B_WORD_CITE, label=B_LABELS[q], state='PASS',
                       read='by gh %s, digest %s, %d characters, the agenda`s CURRENT (by gh %s) EQUAL' % (r['at'], digest(r['out']), len(r['out']), bc[0]),
                       compared='EQUAL', draft='data/b754_ferry.txt :%d, digest %s, %d characters' % (n, digest(d), len(d)),
                       written_at=w['at'], confirm='gh read back %s, equal' % t0, findings_head=None)
        bank(R)
        return
    raise SystemExit('usage: %s b <B2|B4|B6|B7> <read|write|back>' % SELF)


# ---------------------------------------------------------------- [L]
def withheld_l(text, acct, word):
    return DOORS.withheld(text, acct, word)


def l_word_label(line):
    """the label the author chose at the [L] question of a RESULT line; None where the line is no RESULT of that question."""
    if not line.startswith('RESULT (transcript line') or ('"%s' % L_QUESTION) not in line:
        return None
    parts = line.split('"="')
    return parts[1].split('"', 1)[0] if len(parts) == 2 else None


def l_word():
    L = AG.git(RELAY, 'show', 'HEAD:%s' % ANSWERS).replace('\r', '').split(NL)
    return l_word_label(L[L_ANSWERS_LINE - 1] if len(L) >= L_ANSWERS_LINE else '')


def l_drafts():
    """{tag: words}: [L6], [L7], [L8] cut from data/b754_ferry.txt :48 by the agenda's reader; [L14] and [L15] from the amendment rows 3, 4."""
    ls_, _head = AG.split_sub(AG.draft(AG.ferry_lines(), '[L]'), 'L')
    R = AG.amendments()
    out = dict((t, ls_.get(t)) for t in ('[L6]', '[L7]', '[L8]'))
    out['[L14]'] = AG.cut_words(R[2]['words'], '[L14] THE DIAGONAL FIELD', 'no sentence leans on them ((6)(S3)).')
    out['[L15]'] = AG.cut_words(R[3]['words'], '[L] gains [L15]', 'a question for a later sitting.')
    return out


def l_agenda(A):
    """({tag: digest} of the agenda's [L] drafts, (count, digest :2691, digest :3384) of its CURRENT or None), read in its [L] section."""
    dg, cur, on = {}, None, False
    for l in A:
        if l.startswith('## [L] '):
            on = True
            continue
        if on and l.startswith('## '):
            break
        if on:
            m = L_DRAFTED.match(l)
            if m:
                dg[m.group(1)] = m.group(2)
            m = L_CUR.match(l)
            if m:
                cur = (int(m.group(1)), m.group(2), m.group(3))
    return dg, cur


def l_head(date):
    return ('**Dated head, %s, b754, `(R364)`(5)[L]: the lines passed whole at the sitting** (relay %s), appended at the end of the file so '
            'that no line of the trail moves. [L1] to [L5] are held with the sweep of `(R364)`(4)(iv) and carried with it; [L9] to [L13] are '
            'carried by `(R364)`(8). Each line below is the navigator\'s.' % (date, L_WORD_CITE))


def l_compose(D, date):
    """[head, [L6], [L7], [L8], [L14], [L15]]: each draft as cut, the four marked closing with L_MARK, [L15] as it reads."""
    return [l_head(date)] + [D[t] + (L_MARK if t in L_MARKED else '') for t in L_ITEMS]


def l_append(data, lines):
    """data with a blank line before each line of `lines`, each ending as the file's lines end; refused where data does not end with a
    newline or a line carries a break."""
    if not data.endswith(b'\n'):
        raise SystemExit('### THE FILE DOES NOT END WITH A NEWLINE -- NOTHING WRITTEN')
    eol = b'\r\n' if data.endswith(b'\r\n') else b'\n'
    for s in lines:
        if '\n' in s or '\r' in s:
            raise SystemExit('### A LINE CARRIES A LINE BREAK -- NOTHING WRITTEN')
    return data + b''.join(eol + s.encode('utf-8') + eol for s in lines)


def l(step):
    if step not in ('dry', 'write', 'confirm'):
        raise SystemExit('usage: %s l <dry|write|confirm>' % SELF)
    if step == 'confirm':
        return l_confirm()
    if not controls():
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    if '[L]' in rows():
        raise SystemExit('### [L] HAS ITS ROW ALREADY -- NOTHING DONE')
    lab = l_word()
    if lab != L_LABEL:
        raise SystemExit('### [L]: THE WORD AT %s READS %r, NOT %r -- NOTHING DONE' % (L_WORD_CITE, lab, L_LABEL))
    D = l_drafts()
    A = AG.git(RELAY, 'show', 'HEAD:data/%s_agenda.txt' % ACT).replace('\r', '').split(NL)
    dg, cur = l_agenda(A)
    head = AG.git(PP, 'rev-parse', 'HEAD').strip()
    O = AG.lines(PP, 'HEAD', OREL)
    data = open(OPATH, 'rb').read()
    clean = AG.gitq(PP, 'diff', '--quiet', 'HEAD', '--', OREL)[0] == 0
    n0 = split_bytes(data)[1]
    print('### [L] passed whole, the word %s (%s): label %r' % (L_WORD_AT, L_WORD_CITE, lab))
    print('  PLACE-papers HEAD %s ; %s clean against HEAD %s ; %d bytes, %d lines' % (head[:8], OREL, clean, len(data), n0))
    cur_ok = cur is not None and cur[0] == n0 and digest(O[2690]) == cur[1] and digest(O[3383]) == cur[2]
    print('  THE CURRENT against the agenda`s: count %d / %s ; :2691 %s / %s ; :3384 %s / %s ; %s' % (
        n0, cur and cur[0], digest(O[2690]), cur and cur[1], digest(O[3383]), cur and cur[2], 'AGREES' if cur_ok else 'DIFFERS'))
    word, acct = DOORS.q_word(), DOORS.account(PP)
    agree = True
    for t in L_ITEMS:
        d = D.get(t) or ''
        a = bool(d) and dg.get(t) == digest(d)
        agree = agree and a
        print('  %-5s cut %d characters, digest %s ; the agenda`s %s ; %s ; %s' % (t, len(d), digest(d), dg.get(t), 'AGREES' if a else 'DIFFERS',
                                                                           'marked' if t in L_MARKED else 'in its own words'))
    date = stamp()[:10]
    lines_ = l_compose(D, date) if agree else []
    wh = [(i, withheld_l(s, acct, word)) for i, s in enumerate(lines_) if withheld_l(s, acct, word)]
    print('  withheld by a kind: %s' % (['line %d: %s' % (i, k) for i, k in wh] or 'none'))
    if not (clean and cur_ok and agree) or wh:
        raise SystemExit('### [L]: %s -- NOTHING WRITTEN' % ('NOT CLEAN' if not clean else 'THE CURRENT DIFFERS' if not cur_ok else
                                                           'A DRAFT DIFFERS FROM THE AGENDA' if not agree else 'A LINE WITHHELD'))
    after = l_append(data, lines_)
    n1 = split_bytes(after)[1]
    nums = [n0 + 2 + 2 * i for i in range(len(lines_))]
    print('  THE LINE COUNT: before %d ; after %d ; appended %d (a blank before each) ; the bytes before a prefix of the bytes after %s' % (
        n0, n1, n1 - n0, after.startswith(data)))
    for k, s in zip(nums, lines_):
        print('  :%d digest %s, %d characters: %s' % (k, digest(s), len(s), s[:150] + (' ...' if len(s) > 150 else '')))
    if n1 != n0 + 2 * len(lines_) or not after.startswith(data):
        raise SystemExit('### [L]: THE APPEND NOT AS COMPOSED -- NOTHING WRITTEN')
    if step == 'dry':
        print('  DRY: nothing written')
        return
    at = stamp()
    with open(OPATH + '.tmp', 'wb') as f:
        f.write(after)
    os.replace(OPATH + '.tmp', OPATH)
    back = open(OPATH, 'rb').read()
    print('  WRITTEN %s at %s ; read back %s' % (OREL, at, 'EQUAL to the composed' if back == after else 'DIFFERS'))
    if back != after:
        raise SystemExit('### [L]: THE READ-BACK DIFFERS -- restore OPEN_TRAILS.md through the one-call tool')
    R = rows()
    R['[L]'] = dict(form='passed whole', word_at=L_WORD_AT, word_cite=L_WORD_CITE, label=L_LABEL, state='WRITTEN, the commit through the one-call tool',
                    ot_head=head, written_at=at, count_before=n0, count_after=n1, sha_before=bdigest(data), sha_after=bdigest(after),
                    held='[L1] to [L5] held with the sweep of (R364)(4)(iv)', carried='[L9] to [L13] by (R364)(8)',
                    lines=[dict(item=t, line=k, digest=digest(s), chars=len(s), draft_digest=digest(D[t] if t != 'head' else s),
                                agenda=dg.get(t) if t != 'head' else None, marked=t in L_MARKED)
                           for t, k, s in zip(('head',) + L_ITEMS, nums, lines_)],
                    confirm=None)
    bank(R)
    print('  then: `commit.py pp add OPEN_TRAILS.md`, its commit, then `%s l confirm`' % SELF)


def l_confirm():
    R = rows()
    r = R.get('[L]')
    if not r or r.get('confirm'):
        raise SystemExit('### [L]: %s -- NOTHING DONE' % ('NO ROW' if not r else 'CONFIRMED ALREADY'))
    head = AG.git(PP, 'rev-parse', 'HEAD').strip()
    files = AG.git(PP, 'show', '--format=', '--name-only', 'HEAD').strip()
    num = AG.git(PP, 'show', '--format=', '--numstat', 'HEAD').strip()
    O = AG.lines(PP, 'HEAD', OREL)
    have = [digest(O[x['line'] - 1]) == x['digest'] for x in r['lines']]
    add = r['count_after'] - r['count_before']
    ok = files == OREL and num.split()[:2] == [str(add), '0'] and all(have) and head != r['ot_head']
    print('### [L] CONFIRM: PLACE-papers HEAD %s ; files %s ; numstat %s ; the row`s lines at HEAD %s ; %s' % (
        head[:8], files, num.split()[:2], have, 'AS WANTED' if ok else 'NOT AS WANTED'))
    if not ok:
        raise SystemExit('### [L]: THE COMMIT DOES NOT CARRY THE ROW -- NOTHING WRITTEN')
    r['confirm'] = 'PLACE-papers %s, OPEN_TRAILS.md alone, %d line(s) appended, none removed' % (head[:8], add)
    r['state'] = 'PASS'
    bank(R)


# ---------------------------------------------------------------- [R]
def r_word_label(line):
    """the label the author chose at the [R] question of a RESULT line; None where the line is no RESULT of that question."""
    if not line.startswith('RESULT (transcript line') or ('"%s' % R_QUESTION) not in line:
        return None
    parts = line.split('"="')
    return parts[1].split('"', 1)[0] if len(parts) == 2 else None


def r_result():
    L = AG.git(RELAY, 'show', 'HEAD:%s' % ANSWERS).replace('\r', '').split(NL)
    return L[R_ANSWERS_LINE - 1] if len(L) >= R_ANSWERS_LINE else ''


def r_drafts():
    """{tag: words} of [R1], [R2], [R3] cut from data/b754_ferry.txt :50 by the agenda's reader."""
    rs, _head = AG.split_sub(AG.draft(AG.ferry_lines(), '[R]'), 'R')
    return dict(rs)


def r1_derived(d):
    """[R1]'s line as its draft gives it: R1_HEAD, then the draft's words after R1_FROM with R1_SUBS; None where R1_FROM is not met once."""
    if not d or d.count(R1_FROM) != 1:
        return None
    body = d[d.index(R1_FROM) + len(R1_FROM):]
    for a, b in R1_SUBS:
        body = body.replace(a, b)
    return R1_HEAD + body


def r_texts(line, rs):
    """{'[R1]': the line, '[R1] derived', 216, 218: the headings, 'title8': the put's §8 title, 'note': the dated note with its cite set}."""
    out = {'[R1]': cut(line, *R1_NEEDLES), '[R1] derived': r1_derived(rs.get('[R1]')), 'title8': cut(line, *R3_TITLE8_NEEDLES)}
    for k, (a, b) in R3_HEAD_NEEDLES.items():
        out[k] = cut(rs.get('[R3]') or '', a, b)
    n = cut(line, *R3_NOTE_NEEDLES)
    out['note'] = n.replace(*R3_CITE) if n and n.count(R3_CITE[0]) == 1 else None
    return out


def r_agenda(A):
    """({tag: digest} of the agenda's [R] drafts, {'I': INSTRUMENTS :764's words, 'E': (count, :216, :218)}), read in its [R] section."""
    dg, cur, on = {}, {'I': None, 'E': None}, False
    for l in A:
        if l.startswith('## [R] '):
            on = True
            continue
        if on and l.startswith('## '):
            break
        if on:
            m = R_DRAFTED.match(l)
            if m:
                dg[m.group(1)] = m.group(2)
            m = R_CUR_I.match(l)
            if m:
                cur['I'] = m.group(1)
            m = R_CUR_E.match(l)
            if m:
                cur['E'] = (int(m.group(1)), m.group(2), m.group(3))
    return dg, cur


def r_insert(data, k, new):
    """data with the lines `new` inserted after line k, each ending as line k ends; refused where k is not a line or a line carries a break."""
    parts, n0 = split_bytes(data)
    if not (0 < k < n0):
        raise SystemExit('### NO LINE :%d TO INSERT AFTER -- NOTHING WRITTEN' % k)
    for s in new:
        if '\n' in s or '\r' in s:
            raise SystemExit('### A LINE CARRIES A LINE BREAK -- NOTHING WRITTEN')
    cr = b'\r' if parts[k - 1].endswith(b'\r') else b''
    return b'\n'.join(parts[:k] + [s.encode('utf-8') + cr for s in new] + parts[k:])


def r3_check(before, after, k, ins, repl):
    """the lines differing from the plan: :1 to :k byte-equal, the inserted lines as composed, every later line moved by len(ins) and
    byte-equal but the lines of `repl` (old numbers), each its new words with its ending kept."""
    pb, nb = split_bytes(before)
    pa, na = split_bytes(after)
    m = len(ins)
    if na != nb + m or len(pa) != len(pb) + m:
        return ['count %d -> %d' % (nb, na)]
    bad = ['old :%d' % (j + 1) for j in range(k) if pa[j] != pb[j]]
    bad += ['new :%d' % (k + 1 + i) for i, s in enumerate(ins) if get_line(pa, k + 1 + i) != s]
    for j in range(k, len(pb)):
        o, n_ = pb[j], pa[j + m]
        if (j + 1) in repl:
            if get_line(pa, j + 1 + m) != repl[j + 1] or n_.endswith(b'\r') != o.endswith(b'\r'):
                bad.append('old :%d as :%d' % (j + 1, j + 1 + m))
        elif n_ != o:
            bad.append('old :%d as :%d' % (j + 1, j + 1 + m))
    return bad


def r_near(X, word):
    """the line numbers within two of a line carrying the [Q] word (the word never printed)."""
    out = set()
    if word:
        rx = re.compile(r'\b%s\b' % re.escape(word), re.I)
        for k, s in enumerate(X, 1):
            if rx.search(s):
                out |= set(range(max(1, k - 2), k + 3))
    return out


def r(item, step):
    if item not in R_REL or step not in ('dry', 'write', 'confirm'):
        raise SystemExit('usage: %s r <R1|R3> <dry|write|confirm>' % SELF)
    if step == 'confirm':
        return r_confirm(item)
    if not controls():
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    if item in rows():
        raise SystemExit('### %s HAS ITS ROW ALREADY -- NOTHING DONE' % item)
    line = r_result()
    lab = r_word_label(line)
    if lab != R_LABEL:
        raise SystemExit('### %s: THE WORD AT %s READS %r, NOT %r -- NOTHING DONE' % (item, R_WORD_CITE, lab, R_LABEL))
    rs = r_drafts()
    TX = r_texts(line, rs)
    A = AG.git(RELAY, 'show', 'HEAD:data/%s_agenda.txt' % ACT).replace('\r', '').split(NL)
    dg, cur = r_agenda(A)
    rel = R_REL[item]
    path = os.path.join(PP, rel)
    head = AG.git(PP, 'rev-parse', 'HEAD').strip()
    X = AG.lines(PP, 'HEAD', rel)
    data = open(path, 'rb').read()
    clean = AG.gitq(PP, 'diff', '--quiet', 'HEAD', '--', rel)[0] == 0
    n0 = split_bytes(data)[1]
    dd = digest(rs.get(item) or '')
    agree = bool(rs.get(item)) and dg.get(item) == dd
    print('### %s passed, the word %s (%s): label %r' % (item, R_WORD_AT, R_WORD_CITE, lab))
    print('  PLACE-papers HEAD %s ; %s clean against HEAD %s ; %d bytes, %d lines' % (head[:8], rel, clean, len(data), n0))
    print('  the draft (data/b754_ferry.txt :50) digest %s ; the agenda`s %s ; %s' % (dd, dg.get(item), 'AGREES' if agree else 'DIFFERS'))
    if item == '[R1]':
        heads_after = [k for k in range(765, n0 + 1) if X[k - 1].startswith('## ')]
        cur_ok = cur['I'] is not None and n0 == R_INSTRUMENTS_LINES and X[763] == cur['I'] and not heads_after
        print('  THE CURRENT: count %d / the put`s %d ; :764 %s the agenda`s ; a level-two head after :764 %s ; %s' % (
            n0, R_INSTRUMENTS_LINES, 'EQUAL to' if cur['I'] is not None and X[763] == cur['I'] else 'NOT EQUAL to', heads_after or 'none',
            'AGREES' if cur_ok else 'DIFFERS'))
        derived = TX['[R1]'] is not None and TX['[R1]'] == TX['[R1] derived']
        print('  the line cut from the word`s RESULT: %d characters, digest %s ; the draft`s words with the head and the two substitutions %s' % (
            len(TX['[R1]'] or ''), digest(TX['[R1]'] or ''), 'EQUAL' if derived else 'DIFFER'))
        new = [TX['[R1]'] or '']
        after = l_append(data, new)
        n1 = split_bytes(after)[1]
        nums = [n0 + 2]
        texts = [('[R1]', n0 + 2, new[0], None)]
        bad = [] if (after.startswith(data) and n1 == n0 + 2) else ['the append']
        numstat = [2, 0]
    else:
        e = cur['E']
        last = [k for k in range(1, n0 + 1) if X[k - 1].startswith('*Dated note, ')]
        cur_ok = (e is not None and n0 == e[0] and X[215] == e[1] and X[217] == e[2] and last and last[-1] == R3_NOTE_AFTER
                  and X[R3_NOTE_AFTER - 1].endswith('the version stays v0.1.*') and X[R3_NOTE_AFTER] == '')
        print('  THE CURRENT: count %d / the agenda`s %s ; :216 %s ; :218 %s ; the dated notes at %s, :%d blank %s ; %s' % (
            n0, e and e[0], 'EQUAL' if e and X[215] == e[1] else 'NOT EQUAL', 'EQUAL' if e and X[217] == e[2] else 'NOT EQUAL', last,
            R3_NOTE_AFTER + 1, X[R3_NOTE_AFTER] == '', 'AGREES' if cur_ok else 'DIFFERS'))
        derived = (TX[216] is not None and TX[218] is not None and TX['note'] is not None and TX['title8'] is not None
                   and TX[216] == '## 8. ' + TX['title8'] and TX[218].startswith('## 9. ') and ('Dated note, %s, b754:' % stamp()[:10]) in TX['note'])
        print('  the headings cut from the draft (%d, %d characters) ; §8`s title equal to the put`s %s ; the note cut from the word`s RESULT, '
              'its cite :%d, %d characters, dated today %s' % (len(TX[216] or ''), len(TX[218] or ''), TX[216] == '## 8. ' + (TX['title8'] or ''),
                                                             R_ANSWERS_LINE, len(TX['note'] or ''), ('Dated note, %s,' % stamp()[:10]) in (TX['note'] or '')))
        repl = {216: TX[216] or '', 218: TX[218] or ''}
        ins = ['', TX['note'] or '']
        mid = put_lines(data, repl)
        after = r_insert(mid, R3_NOTE_AFTER, ins)
        n1 = split_bytes(after)[1]
        bad = r3_check(data, after, R3_NOTE_AFTER, ins, repl)
        nums = [R3_NOTE_AFTER + 2, 218, 220]
        texts = [('note', R3_NOTE_AFTER + 2, ins[1], None), ('§8', 218, repl[216], X[215]), ('§9', 220, repl[218], X[217])]
        numstat = [4, 2]
    word, acct = DOORS.q_word(), DOORS.account(PP)
    Xa = after.decode('utf-8').replace('\r', '').split(NL)
    near = r_near(Xa, word)
    wh = [(t, withheld_l(s, acct, word)) for (t, _k, s, _o) in texts if withheld_l(s, acct, word)]
    print('  withheld by a kind: %s ; a written line within two of the [Q] word`s lines: %s' % (
        ['%s: %s' % (t, k) for t, k in wh] or 'none', [k for k in nums if k in near] or 'none'))
    print('  THE LINE COUNT: before %d ; after %d ; lines differing from the plan %s' % (n0, n1, bad or 'none'))
    for t, k, s, o in texts:
        print('  %-4s :%d digest %s, %d characters%s' % (t, k, digest(s), len(s), '' if o is None else ' (was digest %s)' % digest(o)))
        if not wh:
            print('      NEW: %s' % s)
    if not (clean and cur_ok and agree and derived) or wh or bad or [k for k in nums if k in near]:
        raise SystemExit('### %s: %s -- NOTHING WRITTEN' % (item, 'NOT CLEAN' if not clean else 'THE CURRENT DIFFERS' if not cur_ok else
                                                          'THE DRAFT DIFFERS FROM THE AGENDA' if not agree else
                                                          'THE PASSED TEXT DOES NOT MEET ITS DRAFT' if not derived else
                                                          'A LINE WITHHELD' if wh else 'NOT AS PLANNED' if bad else 'A LINE BY THE [Q] WORD'))
    if step == 'dry':
        print('  DRY: nothing written')
        return
    at = stamp()
    with open(path + '.tmp', 'wb') as f:
        f.write(after)
    os.replace(path + '.tmp', path)
    back = open(path, 'rb').read()
    print('  WRITTEN %s at %s ; read back %s' % (rel, at, 'EQUAL to the composed' if back == after else 'DIFFERS'))
    if back != after:
        raise SystemExit('### %s: THE READ-BACK DIFFERS -- restore %s through the one-call tool' % (item, rel))
    R = rows()
    R[item] = dict(form='passed', word_at=R_WORD_AT, word_cite=R_WORD_CITE, label=R_LABEL, state='WRITTEN, the commit through the one-call tool',
                   rel=rel, pp_head=head, written_at=at, count_before=n0, count_after=n1, sha_before=bdigest(data), sha_after=bdigest(after),
                   draft_digest=dd, agenda=dg.get(item), numstat=numstat,
                   lines=[dict(item=t, line=k, digest=digest(s), chars=len(s), old_digest=None if o is None else digest(o)) for (t, k, s, o) in texts],
                   carried='[R2] by (R364)(8)', confirm=None)
    bank(R)
    print('  then: `commit.py pp add %s`, its commit, then `%s r %s confirm`' % (rel, SELF, item.strip('[]')))


def r_confirm(item):
    R = rows()
    r_ = R.get(item)
    if not r_ or r_.get('confirm'):
        raise SystemExit('### %s: %s -- NOTHING DONE' % (item, 'NO ROW' if not r_ else 'CONFIRMED ALREADY'))
    rel = r_['rel']
    head = AG.git(PP, 'rev-parse', 'HEAD').strip()
    files = AG.git(PP, 'show', '--format=', '--name-only', 'HEAD').strip()
    num = AG.git(PP, 'show', '--format=', '--numstat', 'HEAD').strip()
    X = AG.lines(PP, 'HEAD', rel)
    have = [digest(X[x['line'] - 1]) == x['digest'] for x in r_['lines']]
    want = [str(x) for x in r_['numstat']]
    ok = files == rel and num.split()[:2] == want and all(have) and head != r_['pp_head']
    print('### %s CONFIRM: PLACE-papers HEAD %s ; files %s ; numstat %s (the row`s %s) ; the row`s lines at HEAD %s ; %s' % (
        item, head[:8], files, num.split()[:2], want, have, 'AS WANTED' if ok else 'NOT AS WANTED'))
    if not ok:
        raise SystemExit('### %s: THE COMMIT DOES NOT CARRY THE ROW -- NOTHING WRITTEN' % item)
    r_['confirm'] = 'PLACE-papers %s, %s alone, %s line(s) added and %s removed' % (head[:8], rel, want[0], want[1])
    r_['state'] = 'PASS'
    bank(R)


# ---------------------------------------------------------------- the sitting's foot ((R364)(5), data/b754_ferry.txt :54)
STEXT = os.path.join(RELAY, 'data', '%s_sitting.txt' % ACT)
SCANS = os.path.join(RELAY, 'data', '%s_address_scan_commits.txt' % ACT)
STEPS = os.path.join(RELAY, 'data', '%s_steps.json' % ACT)
FOOT_FROM = 'd6d6f88e'   # ### the sitting's first commit: the agenda generator, committed before the agenda (step 26)
FOOT_PUTS = ((28, 2, '[A]'), (88, 3, '[B]'), (98, 4, '[Q]'), (118, 5, '[U]'), (131, 6, '[H1]'), (153, 7, '[M2]'), (162, 8, '[D2]'), (171, 9, '[L]'),
             (182, 10, '[R]'))   # ### (the answers line of the RESULT, the put's number, the item)
FOOT_WORD = ((120, 121), '11d67961:16399', '2026-11-13T22:51:31Z', 'on [U1] and [U2] as passed: their rows now, their tool changes in the act '
             'after the walk, each rule in force from the act that follows its change (data/b754_events.txt (29))')
# ### each item in the agenda's order: (row, the answers line or None, the question's opening in that RESULT line, the label the author
# ### chose, the state, the sitting bank's row or None, what was written or why nothing was)
_BT = 'carried to a later sitting on the author`s word; no README written'
_RU = 'data/b754_rules.txt (%s) (relay %s)'
FOOT_ITEMS = (
    ('[A1]', 28, '[A1] riemann-hypothesis', '(a) edited in place (Recommended)', 'PASS', '[A1]', None),
    ('[A2]', 28, '[A2] two-leg-completeness', '(b) retired (Recommended)', 'PASS', '[A2]', None),
    ('[A3]', 28, '[A3] conservation-of-spectra', '(a) edited in place (Recommended)', 'PASS', '[A3]', None),
    ('[A4]', 28, '[A4] simplicity-riemann-zeros', '[A4] (a), [A5] passed (Recommended)', 'PASS', '[A4]', None),
    ('[A5]', 28, '[A4] simplicity-riemann-zeros', '[A4] (a), [A5] passed (Recommended)', 'PASS', '[A5]', None),
    ('[B1]', 88, '[B1] and [B3]', 'Carried to a later sitting', 'CARRIED', None, _BT),
    ('[B2]', 88, '[B2] and [B4]', 'Both passed (Recommended)', 'PASS', '[B2]', None),
    ('[B3]', 88, '[B1] and [B3]', 'Carried to a later sitting', 'CARRIED', None, _BT),
    ('[B4]', 88, '[B2] and [B4]', 'Both passed (Recommended)', 'PASS', '[B4]', None),
    ('[B5]', None, None, None, 'HELD', None, 'held by the amendment row 3 (4) (data/b754_amendments.json row 3), not put; nothing written to its door; [L9] gains it'),
    ('[B6]', 88, '[B6] and [B7]', 'Both passed (Recommended)', 'PASS', '[B6]', None),
    ('[B7]', 88, '[B6] and [B7]', 'Both passed (Recommended)', 'PASS', '[B7]', None),
    ("[B]'s readings", 88, "[B]'s paragraph", 'They stand (Recommended)', 'STANDS', None, 'the readings ruled with no write stand; nothing written'),
    ('[Q]', 98, '[Q] THE QUOTING RULE', 'Passed whole (Recommended)', 'PASS', None,
     _RU % ('6) to (9', 'd1d8303e') + '; tools/standing/ v1.34.2, the origin search (relay 184da293)'),
    ('[U1]', 118, '[U1] THE CADENCE', 'Passed (Recommended)', 'PASS', None,
     _RU % ('10', 'fb623a05') + '; its tool change in the act after the walk, on the author`s word at data/b754_author_answers.txt :120-:121'),
    ('[U2]', 118, '[U2] THE LEDGERS', 'Passed (Recommended)', 'PASS', None,
     _RU % ('11', 'fb623a05') + '; its tool change in the act after the walk, on the author`s word at data/b754_author_answers.txt :120-:121'),
    ('[U3]', 118, '[U3] and [U5]', '[U3] only', 'PASS', None, _RU % ('12', 'fb623a05') + '; tools/standing/ v1.34.3, the refusals counted (relay 19aa6a12)'),
    ('[U4]', 118, '[U4] THE ACT MODULE', 'Struck', 'STRUCK', None, 'nothing written'),
    ('[U5]', 118, '[U3] and [U5]', '[U3] only', 'STRUCK', None, 'nothing written'),
    ('[C1]', None, None, None, 'CARRIED', None, 'carried by (8)`s order (data/b754_ceiling.txt), not put'),
    ('[H1]', 131, '[H1] THE HANDOFF PAGE', '(a) regenerated (Recommended)', 'PASS', None,
     'tools/standing/ v1.34.4, the handoff tool (relay 0c4cda98); HANDOFF.md regenerated whole, with the amendment row 6 (relay ee03ebfa)'),
    ("[H1]'s held part", 153, "[H1]'S HELD PART", 'Carried to a later sitting', 'CARRIED', None,
     'the page in the archive`s roster and the Project set carried to a later sitting; nothing written'),
    ('[M2] (a) to (c)', 153, '[M2] PARTS (a) TO (c)', 'Passed (Recommended)', 'PASS', None,
     _RU % ('13) to (15', 'e94952cc') + '; tools/standing/ v1.34.5 with the amendment row 7 (relay 0b477b49)'),
    ('[M2] (d)', 153, '[M2] PART (d)', 'Passed (Recommended)', 'PASS', None, _RU % ('16', 'e94952cc') + '; the cuts tool in v1.34.5 (relay 0b477b49)'),
    ('[M2] rows m5-3, m5-4, m5-2', 153, '[M2] THE AMENDMENT ROW 3 (7)', 'All three join (Recommended)', 'PASS', None,
     _RU % ('17', 'e94952cc') + '; the three families in the roster`s list (relay 0b477b49)'),
    ('[D2]', 162, '[D2] THE UPDATE CHANNEL', 'Passed (Recommended)', 'PASS', None,
     'the harness`s update channel written "stable" in its user settings, outside every repository, read back equal (data/b754_events.txt (37), relay b9809404)'),
    ('[L1] to [L5]', 171, '[L] THE LINES FOR OPEN_TRAILS', 'Passed whole (Recommended)', 'HELD', None,
     'held with the sweep of (R364)(4)(iv) and carried with it; nothing written'),
    ('[L6], [L7], [L8], [L14], [L15]', 171, '[L] THE LINES FOR OPEN_TRAILS', 'Passed whole (Recommended)', 'PASS', '[L]', None),
    ('[L9] to [L13]', None, None, None, 'CARRIED', None, 'carried by (8)`s order (data/b754_ceiling.txt), not put'),
    ('[R1]', 182, '[R] THE RECORD LINES', 'Both passed (Recommended)', 'PASS', '[R1]', None),
    ('[R2]', None, None, None, 'CARRIED', None, 'carried by (8)`s order (data/b754_ceiling.txt :36, :63), not put'),
    ('[R3]', 182, '[R] THE RECORD LINES', 'Both passed (Recommended)', 'PASS', '[R3]', None),
    ('THE CLUSTER EXPORT', None, None, None, 'CARRIED', None, 'carried by (8)`s order (data/b754_ceiling.txt :37, :63), not built'),
)
SCAN_HEAD = re.compile(r'^## THE SCAN BEFORE THE COMMIT, (\S+Z), b754 commit (.+) in (\S+)$')
SCAN_FOOT = re.compile(r'^### ### \*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; '
                       r'CONTROLS (\d+) OF (\d+) AS WANTED')
RESULT_AT = re.compile(r'^RESULT \(transcript line (\S+), (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)')
APPEND_HEAD = re.compile(r'^## APPENDED BY `record answers` AT (\S+Z): (\d+) LINE\(S\); NO LINE ALREADY IN THE BANK REWRITTEN$')


def foot_labels(line):
    """[(question, label)] of a RESULT line, each question from its opening quote, each label after its `"="`."""
    parts = line.split('"="')
    out = []
    for i in range(1, len(parts)):
        seg = parts[i - 1]
        if i == 1:
            j = seg.find('answered: "')
            q = seg[j + len('answered: "'):] if j >= 0 else ''
        else:
            _prev, _s, rest = seg.partition('"')
            q = rest[3:] if rest.startswith(', "') else ''
        out.append((q, parts[i].split('"', 1)[0]))
    return out


def foot_label(line, opening):
    got = [lab for q, lab in foot_labels(line) if q.startswith(opening)]
    return got[0] if len(got) == 1 else None


def scan_blocks(text):
    out, cur = [], None
    for l in text.replace('\r', '').split(NL):
        m = SCAN_HEAD.match(l)
        if m:
            cur = dict(at=m.group(1), phase=m.group(2), repo=m.group(3), foot=None)
            out.append(cur)
            continue
        m = SCAN_FOOT.match(l)
        if m and cur is not None and cur['foot'] is None:
            cur['foot'] = tuple(int(x) for x in m.groups())
    return out


def secs(t):
    return time.mktime(time.strptime(t[:19], '%Y-%m-%dT%H:%M:%S'))


def foot_compose(at):
    """(the bank's lines, the problems): every row's label read at its RESULT line at relay HEAD, every sitting bank row PASS, every commit a
    row cites among the act's steps, each step of the sitting paired with its scan block in order, each scan 0 ; 0 ; 0 ; 0."""
    A = AG.git(RELAY, 'show', 'HEAD:%s' % ANSWERS).replace('\r', '').split(NL)
    R = rows()
    steps = json.load(io.open(STEPS, encoding='utf-8'))['rows']
    k0 = [i for i, s in enumerate(steps) if s['commit'].startswith(FOOT_FROM)]
    bad = []
    if len(k0) != 1:
        return [], ['the sitting`s first commit %s not once among the steps' % FOOT_FROM]
    sit = [(i + 1, s) for i, s in enumerate(steps) if i >= k0[0]]
    shorts = set(s['commit'][:8] for _n, s in sit)
    L = ['b754 -- (R364)(5) AND ITS FOOT (data/b754_ferry.txt :54): THE RECORD OF THE SITTING, one row per item of the agenda (data/b754_agenda.txt) '
         'in its order (%s)' % at, '',
         '### By tools/b754_sitting.py `foot write`: each row`s label read at its RESULT line in data/b754_author_answers.txt at relay HEAD and '
         'compared with the row; each written row`s confirmation from data/b754_sitting.json; the git writes from data/b754_steps.json, each '
         'paired with its block in data/b754_address_scan_commits.txt. The seat`s word in this bank is each row`s state alone.', '']
    count = {}
    for tag, ln, opening, label, state, jrow, why in FOOT_ITEMS:
        count[state] = count.get(state, 0) + 1
        L.append('%s %s' % (tag, state))
        if ln:
            line = A[ln - 1] if len(A) >= ln else ''
            m = RESULT_AT.match(line)
            got = foot_label(line, opening)
            if got != label or not m:
                bad.append('%s: the label at :%d reads %r, not %r' % (tag, ln, got, label))
            L.append('  THE AUTHOR`S WORD: %s :%d (%sZ, transcript line %s): "%s", %s' % (
                ANSWERS, ln, m.group(2) if m else '?', m.group(1) if m else '?', got, 'read equal' if got == label else 'READ UNEQUAL'))
        else:
            L.append('  THE AUTHOR`S WORD: not put')
        if jrow:
            r_ = R.get(jrow) or {}
            if r_.get('state') != 'PASS' or not r_.get('confirm'):
                bad.append('%s: the sitting bank`s row %s reads %r' % (tag, jrow, r_.get('state')))
            L.append('  WRITTEN: data/b754_sitting.json row %s, %s; %s' % (jrow, r_.get('state'), r_.get('confirm')))
        else:
            L.append('  WRITTEN: %s' % why)
            for c in re.findall(r'\b(?:relay|PLACE-papers) ([0-9a-f]{8})\b', why):
                if c not in shorts:
                    bad.append('%s: the commit %s not among the sitting`s steps' % (tag, c))
        L.append('')
    blocks = [b for b in scan_blocks(io.open(SCANS, encoding='utf-8').read()) if b['phase'] == 'component 3']
    n_rel = sum(1 for _n, s in sit if s['repo'] == 'relay')
    n_pp = sum(1 for _n, s in sit if s['repo'] == 'pp')
    L.append('## THE GIT WRITES OF THE SITTING: %d COMMITS (relay %d ; PLACE-papers %d), EACH THROUGH THE ONE-CALL TOOL AFTER ITS ADD IN A MESSAGE OF ITS OWN' % (
        len(sit), n_rel, n_pp))
    zero = 0
    if len(blocks) != len(sit):
        bad.append('scan blocks %d for %d commits' % (len(blocks), len(sit)))
    for (n, s), b in zip(sit, blocks):
        ok = (b['repo'] == s['repo'] and b['foot'] is not None and b['foot'][:4] == (0, 0, 0, 0) and b['foot'][5] == b['foot'][6]
              and abs(secs(s['at']) - secs(b['at'])) <= 120 and s['phase'] == 'component 3')
        zero += 1 if ok else 0
        if not ok:
            bad.append('step %d: the scan block %s' % (n, b))
        L.append('  step %d: %s %s %s ; the scan %s: %s over %s places, controls %s of %s' % (
            n, 'relay' if s['repo'] == 'relay' else 'PLACE-papers', s['commit'][:8], s['at'], b['at'],
            ' ; '.join(str(x) for x in b['foot'][:4]) if b['foot'] else '?', b['foot'][4] if b['foot'] else '?',
            b['foot'][5] if b['foot'] else '?', b['foot'][6] if b['foot'] else '?'))
    L.append('')
    gh = [(k, R[k]) for k in ('[A5]', '[B2]', '[B4]', '[B6]', '[B7]') if k in R]
    L.append('## THE WRITES BEYOND GIT: %d' % (len(gh) + 1))
    for k, r_ in gh:
        L.append('  %s the description of %s by gh: %s' % (k, r_.get('door', 'PLACE-papers'), r_.get('confirm')))
    L.append('  [D2] the harness`s user settings key, outside every repository (data/b754_events.txt (37))')
    L.append('')
    L.append('## THE AUTHOR`S WORDS OF THE SITTING, BANKED VERBATIM WITH THEIR TIMES BY `record answers` (tools/standing/fold.py), THE ROUTE THAT APPENDS')
    for ln, pn, item in FOOT_PUTS:
        line = A[ln - 1] if len(A) >= ln else ''
        m = RESULT_AT.match(line)
        if not m:
            bad.append('no RESULT at :%d' % ln)
        L.append('  :%d the RESULT of the %s put (data/b754_put_%d.json), %sZ, transcript line %s: %d question(s), %s' % (
            ln, item, pn, m.group(2) if m else '?', m.group(1) if m else '?', len(foot_labels(line)),
            ' ; '.join('"%s"' % lab for _q, lab in foot_labels(line))))
    (w0, w1), wt, wat, wwhat = FOOT_WORD
    whead = A[w0 - 1] if len(A) >= w0 else ''   # ### the word's head at :120, its words at :121
    if not whead.startswith('### THE AUTHOR`S WORD (transcript line %s)' % wt):
        bad.append('the word`s head at :%d reads %r' % (w0, whead[:80]))
    L.append('  :%d-:%d the author`s word, transcript line %s, %s, %s' % (w0, w1, wt, wat, wwhat))
    apps = [(k, APPEND_HEAD.match(l)) for k, l in enumerate(A, 1) if APPEND_HEAD.match(l)]
    L.append('  the appends: %d, %s; each NO LINE ALREADY IN THE BANK REWRITTEN' % (
        len(apps), ' ; '.join(':%d %s %s lines' % (k, m.group(1), m.group(2)) for k, m in apps)))
    L.append('')
    decided = sum(1 for t in FOOT_ITEMS if t[1])
    L.append('### ### **THE SITTING: %d ROWS ; DECIDED BY THE AUTHOR`S ANSWERS %d, NOT PUT %d ; %s ; GIT WRITES %d COMMITS (relay %d ; PLACE-papers %d) ; '
             'THE SCAN AT EVERY COMMIT 0 ; 0 ; 0 ; 0, %d OF %d ; WRITES BEYOND GIT %d ; THE AUTHOR`S ANSWERS %d RESULT ROWS AND %d WORD, BANKED BY '
             '`record answers` IN %d APPENDS, NO LINE REWRITTEN.**' % (
                 len(FOOT_ITEMS), decided, len(FOOT_ITEMS) - decided, ' ; '.join('%s %d' % (k, count[k]) for k in sorted(count)), len(sit), n_rel, n_pp,
                 zero, len(sit), len(gh) + 1, len(FOOT_PUTS), 1, len(apps)))
    return L, bad


def foot(step):
    if step not in ('dry', 'write'):
        raise SystemExit('usage: %s foot <dry|write>' % SELF)
    if not controls():
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    at = stamp()
    L, bad = foot_compose(at)
    word, acct = DOORS.q_word(), DOORS.account(PP)
    wh = [k for k, l in enumerate(L, 1) if withheld_l(l, acct, word)]
    for l in L:
        print('  ' + l)
    print('### THE FOOT: %d lines ; problems %s ; lines withheld by a kind %s' % (len(L), bad or 'none', wh or 'none'))
    if bad or wh or not L:
        raise SystemExit('### THE FOOT NOT AS COMPOSED -- NOTHING WRITTEN')
    if step == 'dry':
        print('  DRY: nothing written')
        return
    data = (NL.join(L) + NL).encode('utf-8')
    with open(STEXT + '.tmp', 'wb') as f:
        f.write(data)
    os.replace(STEXT + '.tmp', STEXT)
    back = open(STEXT, 'rb').read()
    print('  WRITTEN %s at %s: %d lines, %d bytes, sha256 %s ; read back %s' % (os.path.relpath(STEXT, RELAY).replace('\\', '/'), at, len(L), len(data),
                                                                             bdigest(data), 'EQUAL' if back == data else 'DIFFERS'))
    if back != data:
        raise SystemExit('### THE READ-BACK DIFFERS')


def main(argv):
    if not argv:
        raise SystemExit(__doc__)
    cmd = argv[0]
    if cmd == 'control':
        sys.exit(0 if controls() else 1)
    if cmd in ('dry', 'write', 'confirm') and len(argv) == 2 and ('[%s]' % argv[1].strip('[]')) in SPEC:
        item = '[%s]' % argv[1].strip('[]')
        if cmd == 'confirm':
            return item_confirm(item)
        return item_write(item, cmd == 'write')
    if cmd == 'a5' and len(argv) == 2:
        return a5(argv[1])
    if cmd == 'b' and len(argv) == 3:
        return b('[%s]' % argv[1].strip('[]'), argv[2])
    if cmd == 'l' and len(argv) == 2:
        return l(argv[1])
    if cmd == 'r' and len(argv) == 3:
        return r('[%s]' % argv[1].strip('[]'), argv[2])
    if cmd == 'foot' and len(argv) == 2:
        return foot(argv[1])
    raise SystemExit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
