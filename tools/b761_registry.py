# -*- coding: utf-8 -*-
"""tools/b761_registry.py -- b761, (R371)(9): THE SUBJECT AND TO KC CELLS OF PHASE 1.5, appended at REGISTRY's end in the form of b720's
SUBJECT / TO-KC block (tools/b720_registry.py; REGISTRY :1100-:1241), which is not edited.

Written by the Write tool at b761's Component 3 and committed before its first run, dry included (b761 defect (h)).

  dry      prints the controls, the rows' readings and, where the identifier and protected-word controls hold, the block; writes nothing
  write    appends the block to PLACE-papers REGISTRY.md after the controls; banks data/b761_registry_cells.txt and .json

THE ROWS: each row id opening 1.5 that b720's block reads "not yet read" (read from the block by its row pattern, the yield printed), and
1.5c-21 to 1.5c-24, which that block does not name; in (9)'s order: 1.5a-5, 1.5a-6, 1.5a-7, 1.5a-9, 1.5b-6, 1.5c-24, 1.5d-4, 1.5e-7,
1.5f-4, 1.5g-4, 1.5h-6, 1.5h-7, 1.5h-8, 1.5h-9, then the rest in the block's order, the three the block does not name after them in their
id order. Each row's document is the path its REGISTRY row's File cell names, read at PLACE-papers HEAD.
SUBJECT: one clause quoted from the document's own text -- its PURPOSE line ("**PURPOSE:**" in the head, before the first '## ') where the
head carries one; else its abstract's first prose sentence; else its opening's (the first prose paragraph after the title, a line
carrying an identifier, a date, an ornament, a list item, a line wholly in emphasis or a metadata label passed over; the documents'
lines hard-wrapped, so a sentence is read across its paragraph; a sentence of fewer than five words before a longer one taken as a
label) -- cut at its first ';' and, past 220 characters, at a comma, its lines cited; emphasis marks removed, the words kept; a clause
carrying the protected word cited by line and digest alone. Repaired at Component 3 after its first dry run (22:40:29Z), committed
before its second.
TO KC: the class the standing class line declares ("**DOCUMENT CLASS — THE STANDING TAXONOMY (...): TIER X**"), or no class line; which
of Correspondence, Glossary, References or Bibliography, and Errata its headings carry, each by its lines; the newest tag of
SIDE-explicit-formula (the kernel clone's tags in creation order) that its text carries by the tag's name beside the kernel's name or by
the opening seven characters of the tag's peeled commit, or names no tag; and the word candidate by b720's rule (REGISTRY :1102): a head
declaring Tier K or Tier C, or naming itself a keystone candidate.
A row whose Status cell reads SUPERSEDED or WITHDRAWN, or whose document is absent at HEAD, reads so from its row, no text read; a row
whose File cell names no document reads "a kernel row". THE CEILING: the clock read before each row; past 2026-11-19T13:31:58Z the row is
carried, named, and not read.
CONTROLS before the write: the file's bytes at HEAD a prefix of its new bytes; a planted row id outside the list refused; each SUBJECT's
cited line read back carrying its clause (the first row's printed); rule [Q] (3)'s heading by its digest at :374 before and after, no
line above it changing; the identifiers and the protected word 0 in the block; each table row's cells four and its backticks even.

No PLACE-papers line is printed but the texts this tool composes; the protected word is never printed or stored; no git write.
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
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT, NL = 'b761', '\n'
PP = 'D:/MY-DOwnloads/PLACE-papers'
KERNEL = 'D:/SIDE-explicit-formula'
REG = 'REGISTRY.md'
END = '2026-11-19T13:31:58Z'   # ### (R371)(3): the ceiling, data/b761_stepzero.txt
QHEAD, QLINE = '53d53060a58f6b9b', 374
FIRST = ['1.5a-5', '1.5a-6', '1.5a-7', '1.5a-9', '1.5b-6', '1.5c-24', '1.5d-4', '1.5e-7', '1.5f-4', '1.5g-4', '1.5h-6', '1.5h-7', '1.5h-8', '1.5h-9']
EXTRA = ['1.5c-21', '1.5c-22', '1.5c-23', '1.5c-24']
M_WANT = 58
BANK = os.path.join(D, 'b761_registry_cells.txt')
BJSON = os.path.join(D, 'b761_registry_cells.json')
ROW_ID = re.compile(r'^\|\s*(?:\*\*)?`?([A-Za-z0-9]+(?:\.[0-9A-Za-z]+)?-[0-9A-Za-z.]+)`?(?:\*\*)?\s*\|')   # ### b720's matcher
NYR = re.compile(r'^\| `([^`]+)` \| not yet read \| not yet read')
B720_HEAD = '## SUBJECT / TO-KC ATTRIBUTE'
B720_END = '<!-- b720 (R330)(5)(i) ATTRIBUTE BLOCK'
CLS = re.compile(r'^\*\*DOCUMENT CLASS — THE STANDING TAXONOMY \([^)]*\):\s*(?:#+\s*)?([A-Z][A-Z ]+?)\*\*')
META = re.compile(r'^(author|orcid|version|status|date|license|licence|doi|keywords?|msc|filed|lane|predecessor|successor|supersedes|'
                  r'superseded|provenance|act|ruling|cluster spine|paper p\d|class-numbering scheme|document class|correction|changelog)\b', re.I)
TAXONOMY = 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md'
KINDS = (('Correspondence', r'correspondence'), ('Glossary', r'glossary'), ('References or Bibliography', r'references|bibliography'), ('Errata', r'errata'))
K_NAME = r'SIDE-explicit-formula`?(?:’s|\'s)?'


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a, raw=False):
    r = subprocess.run(['git', '-C', repo, *a], capture_output=True)
    return (r.stdout if raw else r.stdout.decode('utf-8', 'replace')), r.returncode


def put(path, text):
    with open(path + '.tmp', 'wb') as f:
        f.write(text.encode('utf-8'))
    os.replace(path + '.tmp', path)


def ids():
    import b761_address_scan as SC
    return dict(name=SC.author_name(), orcid=SC.author_orcid(), address=SC.previous_address())


def idcount(text, I):
    low = text.lower()
    return sum((low.count(I['name'].lower()), low.count(I['orcid'].lower()), low.count(I['address'].lower()), low.count('github.com/')))


def at_head():
    b, _rc = git(PP, 'show', 'HEAD:' + REG, raw=True)
    with open(os.path.join(PP, REG), 'rb') as f:
        w = f.read()
    if not b or b != w or b'\r' in b or not b.endswith(b'\n'):
        die('REGISTRY: ITS WORKING FILE IS NOT ITS BYTES AT HEAD, OR CARRIES CARRIAGE RETURNS, OR NO FINAL LINE END')
    return b.decode('utf-8')


def qword(L):
    """the protected word: the heading word of the line carrying rule [Q] (3)'s digest; returned, never printed."""
    hits = [k for k, l in enumerate(L, 1) if sha(l)[:16] == QHEAD]
    if hits != [QLINE]:
        die('RULE [Q] (3)`S HEADING NOT AT :%d BY ITS DIGEST (%s)' % (QLINE, hits))
    m = re.match(r'^(#+)\s*\**\s*([A-Za-z][A-Za-z\-]*)', L[QLINE - 1])
    if not m:
        die('THE HEADING AT :%d CARRIES NO WORD' % QLINE)
    return m.group(2)


def tags():
    out, _rc = git(KERNEL, 'for-each-ref', 'refs/tags', '--sort=creatordate', '--format=%(refname:short) %(*objectname:short=7)')
    t = [tuple(l.split()) for l in out.split(NL) if l.strip()]
    if not t or any(len(x) != 2 for x in t):
        die('THE KERNEL CLONE`S TAGS NOT READ AS ANNOTATED TAGS')
    return t


# ================================================================================ THE ROWS
def the_ids(L):
    h = [k for k, l in enumerate(L, 1) if l.startswith(B720_HEAD)]
    e = [k for k, l in enumerate(L, 1) if l.startswith(B720_END)]
    if len(h) != 1 or len(e) != 1:
        die('b720`S BLOCK NOT READ ONCE (%s, %s)' % (h, e))
    blk = [(k, l) for k, l in enumerate(L, 1) if h[0] < k < e[0]]
    nyr = [(m.group(1), k) for k, l in blk for m in [NYR.match(l)] if m]
    ids15 = [r for r, _k in nyr if r.startswith('1.5')]
    named = set(m.group(1) for _k, l in blk for m in [re.match(r'^\| (?:### \*\*)?`([^`]+)`', l)] if m)
    if any(x in named for x in EXTRA):
        die('b720`S BLOCK NAMES %s' % [x for x in EXTRA if x in named])
    rest = [r for r in ids15 if r not in FIRST]
    order = FIRST + rest + sorted(x for x in EXTRA if x not in FIRST)
    if len(set(order)) != len(order) or set(FIRST) - set(ids15) - set(EXTRA):
        die('THE ORDER`S IDS NOT EACH ONCE, OR A FIRST ID OUTSIDE THE LIST')
    return order, dict(nyr=len(nyr), ids15=len(ids15), head=h[0], end=e[0])


def row_of(L, rid, allowed, stop):
    """the row's first line in REGISTRY above b720's block (b618's pointer rows set aside); an id outside the list refused."""
    if rid not in allowed:
        raise ValueError('REFUSED: %s is not a row of (R371)(9)' % rid)
    for k, l in enumerate(L[:stop - 1], 1):
        m = ROW_ID.match(l)
        if m and m.group(1) == rid:
            c = [x.strip() for x in l.split('|')]
            if len(c) > 3 and c[3].startswith('`REGISTRY.md:'):
                continue
            return k, c
    raise ValueError('REFUSED: %s names no row' % rid)


def plain(s):
    """a line's words with the emphasis marks removed: the corpus's '### ' marker, bold and italic stars."""
    s = s.lstrip('\ufeff').strip()
    s = re.sub(r'#{3} ', '', s)
    return re.sub(r'\*+', '', s).strip()


LABEL = re.compile(r'^\*\*([A-Z][A-Za-z ]{0,24})[.:]\*\*\s*')
STRUCT = ('#', '>', '|', '<', '```', '---', '===', '[', '!')
LIST = re.compile(r'^(\d+\.|[-+*])\s')
SPLIT = re.compile(r'(?:(?<=[.!?])|(?<=[.!?]["”’)]))\s+(?=[A-Z(“"$])')


def words(s):
    return len(re.findall(r'[A-Za-z]{2,}', s))


def starts_prose(s, I, qw):
    """a line that may open the opening's paragraph: no structure, no list item, no line wholly in emphasis (an epigraph, a dedication,
    a headnote), no label of provenance or metadata, no identifier, no protected word."""
    s0 = s.strip()
    if not s0 or s0.startswith(STRUCT) or LIST.match(s0):
        return False
    if idcount(s0, I) or qw.lower() in s0.lower():
        return False
    if re.fullmatch(r'\*\*[^*]+\*\*', s0) or (s0.startswith('*') and not s0.startswith('**') and s0.endswith('*')) or re.fullmatch(r'_[^_]+_', s0):
        return False
    lab = LABEL.match(s0)
    if lab and META.match(lab.group(1)):
        return False
    return not META.match(plain(s0))


def para(Dl, k):
    """the paragraph opening at line k, the documents' lines being hard-wrapped: k and each line after it to a blank, structural or
    list line, as (its last line, its lines joined by one space)."""
    j = k
    while j < len(Dl) and Dl[j].strip() and not Dl[j].strip().startswith(STRUCT) and not LIST.match(Dl[j].strip()):
        j += 1
    return j, ' '.join(x.strip() for x in Dl[k - 1:j])


def span_text(Dl, k, j):
    return plain(LABEL.sub('', ' '.join(x.strip() for x in Dl[k - 1:j]).strip()))


def clause_of(text):
    """one clause: the first sentence of five words or more (a shorter one before it, a label, passed over), cut at its first '; ' and,
    past 220 characters, at its last comma or dash before 220."""
    ss = SPLIT.split(text.strip())
    s = next((x for x in ss if words(x) >= 5), ss[0])
    s = s.split('; ')[0].strip()
    cut = False
    if len(s) > 220:
        k = max(s.rfind(', ', 0, 220), s.rfind(' — ', 0, 220))
        s, cut = (s[:k] if k > 60 else s[:220].rsplit(' ', 1)[0]), True
    for ch in ('`', '$'):
        if s.count(ch) % 2:
            s, cut = s[:s.rfind(ch)].rstrip(), True
    s = s.rstrip(' ,;:—').rstrip('.')
    return s, cut


def subject(Dl, I, qw):
    h2 = next((k for k, l in enumerate(Dl, 1) if l.startswith('## ')), len(Dl) + 1)
    pu = [k for k, l in enumerate(Dl[:h2 - 1], 1) if l.startswith('**PURPOSE:**')]
    if pu:
        k = pu[0]
        rest = Dl[k - 1][len('**PURPOSE:**'):]
        m = re.match(r'\s*\*([^*]+)\*', rest)
        src = m.group(1) if m else rest.split(' — ')[0]
        return 'PURPOSE', k, k, plain(src)
    ab = [k for k, l in enumerate(Dl, 1) if re.match(r'^#+\s*(?:\d+\.?\s*)?(?i:abstract)\b', l)]
    start, src = (ab[0] + 1, 'abstract') if ab else (2, 'opening')
    for k in range(start, len(Dl) + 1):
        if starts_prose(Dl[k - 1], I, qw):
            j, txt = para(Dl, k)
            if words(txt) >= 8 and not idcount(txt, I) and qw.lower() not in txt.lower():
                return src, k, j, span_text(Dl, k, j)
    return src, None, None, ''


def newest(txt, TG):
    best = None
    for n, c in TG:
        tn = r'`?' + re.escape(n) + r'`?(?![\w]|\.\d)'
        a = re.search(K_NAME + r'[ \t]*(?:at[ \t]+|@[ \t]*|tag[ \t]+|=[ \t]*|,[ \t]*)?' + tn, txt) or \
            re.search(r'(?<![\w.])' + tn + r'[ \t]+(?:of|on|in)[ \t]+`?' + K_NAME, txt)
        b = re.search(r'(?<![0-9a-f])' + c + r'[0-9a-f]*(?![0-9a-z])', txt)
        if a or b:
            hit = a or b
            best = (n, c, 'by its name' if a else 'by its peeled commit `%s`' % c, txt[:hit.start()].count(NL) + 1)
    return best


def read_doc(path, I, qw, TG):
    raw, rc = git(PP, 'show', 'HEAD:' + path)
    if rc or not raw:
        return None
    Dl = raw.replace('\r', '').split(NL)
    if Dl and Dl[-1] == '':
        Dl = Dl[:-1]
    h2 = next((k for k, l in enumerate(Dl, 1) if l.startswith('## ')), len(Dl) + 1)
    cl = [(k, m.group(1).strip()) for k, l in enumerate(Dl[:h2 - 1], 1) for m in [CLS.match(l.lstrip('\ufeff'))] if m]
    heads = []
    for name, rx in KINDS:
        ks = [k for k, l in enumerate(Dl, 1) if l.startswith('#') and re.search(r'(?i)\b(?:%s)\b' % rx, l)]
        if ks:
            heads.append((name, ks))
    kc = [k for k, l in enumerate(Dl[:h2 - 1], 1) if re.search(r'(?i)keystone candidate', l)]
    src, k, j, line = subject(Dl, I, qw)
    return dict(lines=len(Dl), cls=cl[0] if cl else None, heads=heads, kc=kc, src=src, k=k, j=j, line=line, tag=newest(raw, TG), D=Dl)


def cells(rid, k, c, I, qw, TG):
    st = c[6] if len(c) > 6 else ''
    fcell = c[3] if len(c) > 3 else ''
    m = re.search(r'`(phase[^`]+\.md)`', fcell)
    if re.search(r'\b(SUPERSEDED|WITHDRAWN)\b', st) or (not m and re.search(r'(?i)superseded|withdrawn', fcell)):
        w = 'withdrawn' if 'WITHDRAWN' in st.upper() or 'withdrawn' in fcell.lower() else 'superseded'
        return dict(kind=w, subject='%s, as its row reads (REGISTRY :%d); no text read' % (w, k), tokc='%s; no text read' % w)
    if not m:
        return dict(kind='kernel', subject='a kernel row (REGISTRY :%d)' % k, tokc='a kernel row')
    path = m.group(1)
    d = read_doc(path, I, qw, TG)
    if d is None:
        return dict(kind='absent', path=path, subject='absent at HEAD, as its row names it (REGISTRY :%d, `%s`); no text read' % (k, path), tokc='absent; no text read')
    j2 = None
    if not d['k']:
        subj, cl_, cut = 'no %s sentence read (`%s`)' % (d['src'], path), '', False
    else:
        cl_, cut = clause_of(d['line'])
        j2 = next((x for x in range(d['k'], d['j'] + 1) if cl_ in span_text(d['D'], d['k'], x)), d['j'])
        where = '%s :%d' % (d['src'], d['k']) + ('–:%d' % j2 if j2 > d['k'] else '')
        if qw.lower() in cl_.lower() or idcount(cl_, I):
            subj = 'its %s line cited by line and digest alone: :%d (sha256 %s)' % (d['src'], d['k'], sha(d['D'][d['k'] - 1])[:16])
            cl_ = ''
        else:
            subj = '“%s%s” (%s)' % (cl_.replace('|', '\\|'), ' …' if cut else '', where)
    parts = ['class %s (:%d)' % (d['cls'][1], d['cls'][0]) if d['cls'] else 'no class line']
    parts.append('; '.join('%s %s' % (n, ', '.join(':%d' % x for x in ks[:4]) + (' and %d more' % (len(ks) - 4) if len(ks) > 4 else '')) for n, ks in d['heads'])
                 if d['heads'] else 'none of Correspondence, Glossary, References or Bibliography, Errata')
    parts.append('SIDE-explicit-formula `%s` %s (:%d)' % (d['tag'][0], d['tag'][2], d['tag'][3]) if d['tag'] else 'names no tag')
    tier = d['cls'][1] if d['cls'] else ''
    if re.fullmatch(r'TIER (K|C)', tier) or d['kc']:
        parts.append('**candidate** (%s)' % ('Tier %s declared' % tier[-1] if tier else 'names itself a keystone candidate, :%d' % d['kc'][0]))
    elif tier == 'TIER KC':
        parts.append('declares Tier KC whole, where b720’s rule gives the word to a head declaring one half (Tier K or Tier C), so the word is not given here; `%s` :69 names no candidate' % TAXONOMY)
    else:
        parts.append('not a candidate by b720’s rule')
    return dict(kind='read', path=path, src=d['src'], k=d['k'], j=j2, clause=cl_, cut=cut, subject=subj, tokc=' · '.join(parts),
                cls=d['cls'], heads=d['heads'], tag=d['tag'][:2] if d['tag'] else None,
                line_text=NL.join(d['D'][d['k'] - 1:j2]) if d['k'] else '')


# ================================================================================ THE BLOCK
def compose(L, order, info, I, qw, TG, date):
    allowed = set(order)
    rows, carried = [], []
    for rid in order:
        if utc() > END:
            carried.append(rid)
            continue
        k, c = row_of(L, rid, allowed, info['head'])
        r = cells(rid, k, c, I, qw, TG)
        r.update(id=rid, row=k)
        rows.append(r)
    rule = [k for k, l in enumerate(L, 1) if 'The word `candidate` marks' in l]
    out = ['<!-- b761 (R371)(9) SUBJECT / TO-KC CELLS, %s -->' % date, '',
           '## SUBJECT / TO-KC CELLS OF PHASE 1.5 *(added %s, b761, under the author’s ruling `(R371)`(9); in the form of b720’s block (:%d), which is not edited)*' % (date, info['head']), '',
           '**The rows of Phase 1.5 that b720’s block reads `not yet read`, and 1.5c-21 to 1.5c-24, which it does not name, each with its two cells. `SUBJECT`: one clause quoted from the document’s own text — its PURPOSE line where its head carries one, else its abstract’s first sentence, else its opening’s — cut at its first semicolon, its lines cited; the documents’ lines being hard-wrapped, a sentence is read across its paragraph; a line wholly in emphasis (an epigraph, a dedication, a headnote), a list, a date, a label of metadata and a sentence of fewer than five words before the first longer one (a label) are passed over; emphasis marks are removed and the words kept. `TO KC`: four parts read from the document at PLACE-papers HEAD — the class its standing class line declares, or no class line; which of the headings Correspondence, Glossary, References or Bibliography, and Errata it carries, each by its lines; the newest tag of SIDE-explicit-formula its text carries by the tag’s name beside the kernel’s name or by the opening seven characters of the tag’s peeled commit, or names no tag; and the word `candidate` by b720’s rule (:%s). A row whose document is withdrawn, superseded or absent reads so from its own row; a row with no document reads a kernel row. The rows stand in the order `(R371)`(9) gives: the keystones’ rows first, then the rest in b720’s order, the three rows b720’s block does not name after them. No row is moved between phases here: each row’s placement is put to the author after these cells are read (the block at :%d).**' % (
               ', :'.join(str(x) for x in rule) or '?', [k for k, l in enumerate(L, 1) if l.startswith('## THE PHASES BY SUBJECT')][0]), '',
           '| row | `SUBJECT` | `TO KC` |', '|:--|:--|:--|']
    for r in rows:
        out.append('| `%s` | %s | %s |' % (r['id'], r['subject'], r['tokc']))
    out += ['', '> **COUNTED:** %d rows: %d of b720’s block opening 1.5 (its rows reading `not yet read` %d) and 1.5c-21 to 1.5c-24; read %d, carried over the ceiling %d%s.' % (
        len(order), info['ids15'], info['nyr'], len(rows), len(carried), (' (%s)' % ', '.join(carried)) if carried else ''), '',
            '<!-- b761 (R371)(9) CELLS BLOCK, %s -->' % date, '',
            '*Appended by b761. No row above is edited; b720’s block stands as written, and its `not yet read` cells for these rows are read here. Nothing deposits.*']
    return NL.join(out), rows, carried


def run(mode):
    base = at_head()
    L = base.split(NL)[:-1]
    qw = qword(L)
    I = ids()
    TG = tags()
    order, info = the_ids(L)
    date = time.strftime('%Y-%m-%d', time.gmtime())
    block, rows, carried = compose(L, order, info, I, qw, TG, date)
    new = base + NL + block + NL
    NLn = new.split(NL)[:-1]
    # ### THE CONTROLS
    planted = []
    for pid in ('1.5z-99', 'd1-1'):
        try:
            row_of(L, pid, set(order), info['head'])
            planted.append((pid, 'NOT REFUSED'))
        except ValueError:
            planted.append((pid, 'REFUSED'))
    back = []
    for r in rows:
        if r['kind'] == 'read' and r['clause']:
            Dl, _rc = git(PP, 'show', 'HEAD:' + r['path'])
            Dl = Dl.replace('\r', '').split(NL)
            back.append((r['id'], '%d-%d' % (r['k'], r['j']), r['clause'] in span_text(Dl, r['k'], r['j']) and NL.join(Dl[r['k'] - 1:r['j']]) == r['line_text']))
    tbl = [l for l in block.split(NL) if l.startswith('| `')]
    cellbad = [l[:12] for l in tbl if len(re.split(r'(?<!\\)\|', l)) != 5 or l.count('`') % 2]
    ticks = [k for k, l in enumerate(block.split(NL), 1) if l.count('`') % 2]
    qb = [k for k, l in enumerate(L, 1) if sha(l)[:16] == QHEAD]
    qa = [k for k, l in enumerate(NLn, 1) if sha(l)[:16] == QHEAD]
    ctl = [('the matcher`s yield: b720`s block rows reading not yet read %d, opening 1.5 %d; with 1.5c-21 to 1.5c-24, %d rows (wanted %d)' % (
                info['nyr'], info['ids15'], len(order), M_WANT), len(order) == M_WANT),
           ('the file`s bytes at HEAD a prefix of its new bytes', new.startswith(base)),
           ('a planted row id outside the list refused %s' % planted, all(x[1] == 'REFUSED' for x in planted)),
           ('each SUBJECT`s cited line read back carrying its clause: %d of %d; the first %s' % (sum(1 for x in back if x[2]), len(back), back[:1]),
            bool(back) and all(x[2] for x in back)),
           ('rule [Q] (3)`s heading by its digest at :%d before and after (%s -> %s), no line above it changing' % (QLINE, qb, qa),
            qb == [QLINE] and qa == [QLINE] and NLn[:QLINE] == L[:QLINE]),
           ('the identifiers 0 in the block (%d) and the protected word 0 in it' % idcount(block, I), idcount(block, I) == 0 and qw.lower() not in block.lower()),
           ('each table row four cells and its backticks even (off %s), each line`s backticks even (off %s)' % (cellbad, ticks), not cellbad and not ticks),
           ('the rows read %d, carried over the ceiling %d' % (len(rows), len(carried)), len(rows) + len(carried) == len(order))]
    ok = all(o for _w, o in ctl)
    kinds = {}
    for r in rows:
        kinds[r['kind']] = kinds.get(r['kind'], 0) + 1
    cand = sum(1 for r in rows if '**candidate**' in r['tokc'])
    P = ['%s -- (R371)(9): THE SUBJECT AND TO KC CELLS OF PHASE 1.5, APPENDED AT REGISTRY`S END (%s)' % (ACT, utc()), '',
         '### tools/b761_registry.py %s; PLACE-papers HEAD %s; the kernel clone`s tags %d (the newest %s); each row`s clause by its line and sha256 here, its' % (
             mode, git(PP, 'rev-parse', '--short=8', 'HEAD')[0].strip(), len(TG), TG[-1][0]),
         '### words in REGISTRY alone; the protected word neither printed nor stored.', '', '## THE CONTROLS']
    P += ['  %-130s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE ROWS: id | its row | kind | the SUBJECT`s source and line | the clause`s sha256 (cut) | class | the headings | the newest tag | candidate']
    for r in rows:
        if r['kind'] == 'read':
            P.append('  %s | :%d | read | %s :%s | %s%s | %s | %s | %s | %s' % (
                r['id'], r['row'], r['src'], ('%d-%d' % (r['k'], r['j'])) if r['k'] and r['j'] != r['k'] else r['k'], sha(r['clause'])[:16] if r['clause'] else 'by digest', ' (cut)' if r['cut'] else '',
                ('%s :%d' % (r['cls'][1], r['cls'][0])) if r['cls'] else 'none', ', '.join('%s %s' % (n, ks[:4]) for n, ks in r['heads']) or 'none',
                ('%s %s' % r['tag']) if r['tag'] else 'none', 'candidate' if '**candidate**' in r['tokc'] else '-'))
        else:
            P.append('  %s | :%d | %s | - | - | - | - | - | -' % (r['id'], r['row'], r['kind']))
    P += ['', '## THE SENTENCE: the cells: %d rows read of %d; %d carried over the ceiling' % (len(rows), len(order), len(carried)),
          '', '### ### **THE CELLS: ROWS %d OF %d READ (%s) ; CANDIDATE %d ; CARRIED %d ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
              len(rows), len(order), ', '.join('%s %d' % kv for kv in sorted(kinds.items())), cand, len(carried), sum(1 for _w, o in ctl if o), len(ctl),
              ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        if idcount(block, I) == 0 and qw.lower() not in block.lower():
            print(NL + '### THE BLOCK AS COMPOSED (the dry run`s print alone):')
            print(block)
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    if idcount(NL.join(P), I) or qw.lower() in NL.join(P).lower():
        die('AN IDENTIFIER OR THE PROTECTED WORD IN THE BANK')
    with open(os.path.join(PP, REG), 'wb') as f:
        f.write(new.encode('utf-8'))
    with open(os.path.join(PP, REG), 'rb') as f:
        if f.read() != new.encode('utf-8'):
            die('THE WRITTEN FILE IS NOT ITS COMPOSITION')
    put(BANK, NL.join(P) + NL)
    put(BJSON, json.dumps(dict(at=utc(), act=ACT, date=date, rows_read=len(rows), m=len(order), carried=carried, candidate=cand, kinds=kinds,
                               block_first_line=len(L) + 2, block_sha256=sha(block)[:16], file_sha_before=sha(base)[:16], file_sha_after=sha(new)[:16],
                               rows=[dict(id=r['id'], row=r['row'], kind=r['kind'], src=r.get('src'), line=r.get('k'), line_end=r.get('j'), clause_sha256=sha(r['clause'])[:16] if r.get('clause') else None,
                                          cut=r.get('cut'), cls=list(r['cls']) if r.get('cls') else None, heads=[[n, ks] for n, ks in r.get('heads') or []],
                                          tag=list(r['tag']) if r.get('tag') else None, candidate='**candidate**' in r['tokc']) for r in rows],
                               sentence='the cells: %d rows read of %d; %d carried over the ceiling' % (len(rows), len(order), len(carried)),
                               controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written REGISTRY.md (%d lines to %d, the block from :%d); data/b761_registry_cells.txt and .json' % (len(L), len(NLn), len(L) + 2))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] not in (['dry'], ['write']):
        sys.exit(__doc__)
    run(a[0])
