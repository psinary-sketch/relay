# -*- coding: utf-8 -*-
"""standing/handoff.py -- THE HANDOFF PAGE REGENERATED WHOLE FROM THE BANKS ((R364)(5)[H1], passed as (a) on the author's word, relay
data/b754_author_answers.txt :131, 2026-11-13T23:08:49Z). It writes HANDOFF.md at the relay's root whole, nothing typed, under 400 lines;
the page is edited by no hand, and its earlier pages stand in that file's history. Written at b754 by the Write tool; no identifier of the
author is read into any string here.

THE PAGE, every line read from a bank at the relay's HEAD or from PLACE-papers at its HEAD, through git (the working copies not read):
  (1) THE HEAD LINE: that this tool wrote it, at which commits, from which banks.
  (2) THE HOLDS IN FORCE: the last ruling's clause on them, quoted from its ferry bank (the newest data/<act>_ferry.txt, its one line
      opening "(n) THE DRAFT stands at").
  (3) THE LAST TWELVE ACTS: the twelve closed acts of the highest numbers (an act is closed where data/<act>_closing.txt is tracked),
      newest first, each by its closing's head line (:1, opening "<act> closed: ") and its ruling's paragraph THE ACT'S PLACE, the one
      ferry line carrying it in any of its three wordings and with either apostrophe.
  (4) THE NEXT: the first "**Next:**" line after the last trail's heading ("### <act> — ...") in PLACE-papers OPEN_TRAILS.md.
  (5) THE OPEN ORDERS by count and name, from tools/standing/orders.py's reader over the same OPEN_TRAILS.md.
  (6) WHERE EACH KIND OF STATE IS HELD, by path and line: the registry's phase tables, the census's cluster and kernel tables at its
      newest edition, the reference layer, the instruments, the standing clauses, the rules banks and the registrations banks.
THE MATCHERS print their yields; a needle not found, or found more than once where one is wanted, refuses the page: nothing is written.
THE QUOTING RULE (data/b754_rules.txt (8), [Q]'s row (3)): the word is read at run time from the rule's heading in REGISTRY and held in
no tracked file; a line the page would quote that carries it, or a PLACE-papers line in that row's protected set (the section under the
heading, FINDINGS :820-:826, OPEN_TRAILS' O.7 whole, two lines either side of the word in a ledger), is cited by path, line and the
opening sixteen characters of its sha256 and not quoted. The word itself is printed nowhere.
THE HEADING BY ITS DIGEST (v1.36.8, (R370)(5)(i), the author's; data/b760_rules.txt): the heading is the one line of REGISTRY whose
sha256 opens HEAD_DIGEST, found wherever it stands, its line and its section's span printed among the yields; where no line carries that
digest, or more than one does, the page is refused. The number the heading stood at before b759's REGISTRY row moved it is read nowhere.
REACH: the page says where the record holds its state and what the last acts were, in the banks' own words; it reads no figure, grades
nothing and checks no bank's words against the record.

  python -X utf8 -u tools/standing/handoff.py dry        the page and the yields printed; nothing written
  python -X utf8 -u tools/standing/handoff.py write      HANDOFF.md written whole; the yields printed
  python -X utf8 -u tools/standing/handoff.py control    the controls, each over banks planted in memory; nothing written
"""
import hashlib
import os
import re
import subprocess
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
if S not in sys.path:
    sys.path.insert(0, S)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import orders as OR   # noqa: E402  (the orders reader; PLACE-papers' place is OR.PP)

NL = '\n'
OUT = os.path.join(RELAY, 'HANDOFF.md')
CAP = 400
TWELVE = 12
RULE_CITE = 'data/b754_rules.txt (8), [Q]`s row (3)'
HEAD_DIGEST = '53d53060a58f6b9b'   # ### (R370)(5)(i): the sha256 of rule [Q] (3)'s heading line in REGISTRY, its opening sixteen characters

CLOSING = re.compile(r'^data/b(\d+)_closing\.txt$')
FERRY = re.compile(r'^data/b(\d+)_ferry\.txt$')
HEADLINE = re.compile(r'^b(\d+) closed: ')
PLACE = re.compile("THE ACT['’`]S PLACE(?: ON THE PAPER PATH)?[.:]")
PLACE_WIDE = re.compile(r'(?i)THE ACT\W{1,3}S PLACE')          # ### the second shape: its yield printed beside, it decides nothing
HOLD = re.compile(r'^\s*\(\d+\) THE DRAFT stands at ')
HOLD_WIDE = re.compile(r'THE DRAFT stands at v\d+, HELD')     # ### the second shape, printed beside
TRAIL = re.compile('^### b(\\d+) — ')
NEXT = re.compile(r'^\*\*Next:\*\*')
O7 = re.compile(r'^(#+)\s+O\.7\b')
REGPHASE = re.compile(r'^## PHASE [0-9.]+: ')
CENSUS = re.compile(r'^phase2/method/THE_KEYSTONE_CENSUS_v(\d+(?:_\d+)*)\.md$')
CLUSTERS = re.compile('^## §1 — THE PHASES AND CLUSTERS')
KERNELS = re.compile('^## §1A — THE KERNEL COLUMN')
LAYER_OPEN = re.compile(r'^## I\. ')
LAYER_MOVE = re.compile(r'^## How findings move')
RULE_LINE = re.compile(r'^---\s*$')
ANCHOR = re.compile(r'^### ')
INSTR = 'phase1.5/method/INSTRUMENTS.md'
IHEAD = re.compile(r'^## (I-\d+)\b')
CLAUSES = re.compile(r'^data/standing_clauses_v(\d+)\.txt$')
RULES = re.compile(r'^data/b(\d+)_rules\.txt$')
REGS = re.compile(r'^data/b(\d+)_registrations\.txt$')


class Refuse(Exception):
    pass


def _git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace')


class Source(object):
    """the banks at the two heads, read through git; the working copies are not read."""

    def __init__(self, rrev='HEAD', prev='HEAD'):
        self.rrev, self.prev = rrev, prev
        self.rhead = _git(RELAY, 'rev-parse', '--short=8', rrev)[1].strip()
        self.phead = _git(OR.PP, 'rev-parse', '--short=8', prev)[1].strip()
        self._rl = self._pl = None

    def _show(self, repo, rev, path):
        rc, out = _git(repo, 'show', '%s:%s' % (rev, path))
        return None if rc else out.replace('\r', '').split(NL)

    def relay(self, path):
        return self._show(RELAY, self.rrev, path)

    def pp(self, path):
        return self._show(OR.PP, self.prev, path)

    def relay_list(self):
        if self._rl is None:
            self._rl = [p for p in _git(RELAY, 'ls-tree', '-r', '--name-only', self.rrev, '--', 'data/')[1].split(NL) if p.strip()]
        return self._rl

    def pp_list(self):
        if self._pl is None:
            self._pl = [p for p in _git(OR.PP, 'ls-tree', '-r', '--name-only', self.prev, '--', 'phase2/method/')[1].split(NL) if p.strip()]
        return self._pl


class Planted(Source):
    """the banks of `base` with some replaced in memory: a control's source."""

    def __init__(self, base, relay=None, pp=None):
        self.base, self.r, self.p = base, dict(relay or {}), dict(pp or {})
        self.rrev, self.prev, self.rhead, self.phead = base.rrev, base.prev, base.rhead, base.phead

    def relay(self, path):
        return self.r[path] if path in self.r else self.base.relay(path)

    def pp(self, path):
        return self.p[path] if path in self.p else self.base.pp(path)

    def relay_list(self):
        return self.base.relay_list()

    def pp_list(self):
        return self.base.pp_list()


def digest(line):
    return hashlib.sha256(line.encode('utf-8')).hexdigest()[:16]


def head_line(reg):
    """(R370)(5)(i), v1.36.8: the 1-based line of REGISTRY carrying rule [Q] (3)'s heading, the one line whose sha256 opens HEAD_DIGEST;
    refused where no line carries that digest or more than one does."""
    hits = [k for k, l in enumerate(reg or [], 1) if digest(l) == HEAD_DIGEST]
    if len(hits) != 1:
        raise Refuse('REGISTRY.md: %d lines carry the sha256 opening %s (rule [Q] (3)`s heading), one wanted: the quoting rule cannot run' % (
            len(hits), HEAD_DIGEST))
    return hits[0]


def qword(src):
    """the quoting rule's word, read at run time from the heading head_line finds: (compiled matcher, the word, the heading's level, its line)."""
    reg = src.pp('REGISTRY.md')
    if not reg:
        raise Refuse('REGISTRY.md not read: the quoting rule cannot run')
    k = head_line(reg)
    m = re.match(r'^(#+)\s*\**\s*([A-Za-z][A-Za-z\-]*)', reg[k - 1])
    if not m:
        raise Refuse('REGISTRY.md :%d carries the heading`s digest and no heading`s leading word: the quoting rule cannot run' % k)
    return re.compile(r'\b%s\b' % re.escape(m.group(2)), re.I), m.group(2), len(m.group(1)), k


def _section(lines, start, level):
    end = len(lines)
    for k in range(start, len(lines)):
        mm = re.match(r'^(#+)\s', lines[k])
        if mm and len(mm.group(1)) <= level:
            end = k
            break
    return set(range(start, end + 1))


def protected(path, lines, q):
    """[Q]'s row (3) over one PLACE-papers ledger: the 1-based lines that are cited and not quoted."""
    rx, _w, level = q[:3]
    out = set()
    if path == 'REGISTRY.md':
        out |= _section(lines, head_line(lines), level)
    if path == 'FINDINGS.md':
        out |= set(range(820, 827))
    if path == 'OPEN_TRAILS.md':
        s = [k + 1 for k, l in enumerate(lines) if O7.match(l)]
        if s:
            out |= _section(lines, s[0], len(O7.match(lines[s[0] - 1]).group(1)))
    for k, l in enumerate(lines, 1):
        if rx.search(l):
            out |= set(range(max(1, k - 2), min(len(lines), k + 2) + 1))
    return out


def quote(where, k, text, q, Y, held=False):
    """the line as the bank holds it, or its cite where the quoting rule holds it."""
    if held or q[0].search(text):
        Y['cited'].append('%s :%d' % (where, k))
        return '*not quoted under %s: %s :%d, sha256 %s*' % (RULE_CITE, where, k, digest(text))
    return text.strip()


def _nums(paths, rx):
    return sorted(int(m.group(1)) for p in paths for m in [rx.match(p)] if m)


def holds(src, q, Y):
    fs = _nums(src.relay_list(), FERRY)
    if not fs:
        raise Refuse('no ferry bank data/<act>_ferry.txt at relay %s' % src.rhead)
    path = 'data/b%d_ferry.txt' % fs[-1]
    f = src.relay(path) or []
    hits = [k for k, l in enumerate(f, 1) if HOLD.match(l)]
    wide = [k for k, l in enumerate(f, 1) if HOLD_WIDE.search(l)]
    Y['yields'].append('HOLDS  %s : the clause opening "(n) THE DRAFT stands at" %d line(s) %s ; the second shape %d %s' % (
        path, len(hits), [':%d' % k for k in hits], len(wide), [':%d' % k for k in wide]))
    if len(hits) != 1:
        raise Refuse('the holds clause read %d times in %s, one wanted' % (len(hits), path))
    return path, hits[0], quote(path, hits[0], f[hits[0] - 1], q, Y)


def acts(src, q, Y):
    cs = _nums(src.relay_list(), CLOSING)
    if len(cs) < TWELVE:
        raise Refuse('%d closed acts at relay %s, twelve wanted' % (len(cs), src.rhead))
    out = []
    for a in reversed(cs[-TWELVE:]):
        cp, fp = 'data/b%d_closing.txt' % a, 'data/b%d_ferry.txt' % a
        c, f = src.relay(cp), src.relay(fp)
        m = HEADLINE.match(c[0]) if c else None
        if not m or int(m.group(1)) != a:
            raise Refuse('%s :1 does not open "b%d closed: "' % (cp, a))
        if f is None:
            raise Refuse('%s not at relay %s' % (fp, src.rhead))
        hits = [k for k, l in enumerate(f, 1) if PLACE.search(l)]
        wide = [k for k, l in enumerate(f, 1) if PLACE_WIDE.search(l)]
        Y['yields'].append('ACT b%d : %s :1 head line READ ; %s THE ACT`S PLACE %d line(s) %s ; the second shape %d %s' % (
            a, cp, fp, len(hits), [':%d' % k for k in hits], len(wide), [':%d' % k for k in wide]))
        if len(hits) != 1:
            raise Refuse('THE ACT`S PLACE read %d times in %s, one wanted' % (len(hits), fp))
        out.append((a, cp, quote(cp, 1, c[0], q, Y), fp, hits[0], quote(fp, hits[0], f[hits[0] - 1], q, Y)))
    return out


def the_next(src, q, Y):
    lines = src.pp('OPEN_TRAILS.md')
    if not lines:
        raise Refuse('PLACE-papers OPEN_TRAILS.md not read at %s' % src.phead)
    heads = [(k, int(m.group(1))) for k, l in enumerate(lines, 1) for m in [TRAIL.match(l)] if m]
    if not heads:
        raise Refuse('no trail heading "### <act> — " in OPEN_TRAILS.md at %s' % src.phead)
    hk, ha = heads[-1]
    nx = [k for k in range(hk + 1, len(lines) + 1) if NEXT.match(lines[k - 1])]
    Y['yields'].append('NEXT  OPEN_TRAILS.md : trail headings %d, the last b%d at :%d ; "**Next:**" lines after it %d %s' % (
        len(heads), ha, hk, len(nx), [':%d' % k for k in nx]))
    if not nx:
        raise Refuse('no "**Next:**" line after the last trail heading (:%d) in OPEN_TRAILS.md' % hk)
    k = nx[0]
    return lines, ha, hk, k, quote('PLACE-papers OPEN_TRAILS.md', k, lines[k - 1], q, Y, held=k in protected('OPEN_TRAILS.md', lines, q))


def open_orders(lines, Y):
    rows = OR.read(lines)
    op = [n for n, o in rows if o['status'] == 'OPEN']
    Y['yields'].append('ORDERS  tools/standing/orders.py read : orders %d ; OPEN %d ; CLOSED %d' % (len(rows), len(op), len(rows) - len(op)))
    if not rows:
        raise Refuse('the orders reader read no order in OPEN_TRAILS.md')
    return rows, op


def _one(where, lines, rx, Y, label):
    hits = [k for k, l in enumerate(lines or [], 1) if rx.search(l)]
    Y['yields'].append('STATE  %s : %s %d line(s) %s' % (where, label, len(hits), [':%d' % k for k in hits][:8]))
    if not hits:
        raise Refuse('%s: %s not found' % (where, label))
    return hits


def state(src, q, Y):
    L = []
    reg = src.pp('REGISTRY.md')
    rp = protected('REGISTRY.md', reg, q)
    ph = _one('PLACE-papers REGISTRY.md', reg, REGPHASE, Y, 'the phase tables (## PHASE <n>: )')
    L.append('- the registry`s phase tables: PLACE-papers REGISTRY.md ' + ' ; '.join(
        ':%d %s' % (k, quote('PLACE-papers REGISTRY.md', k, reg[k - 1].lstrip('# '), q, Y, held=k in rp)) for k in ph))
    eds = sorted(((tuple(int(x) for x in m.group(1).split('_')), p) for p in src.pp_list() for m in [CENSUS.match(p)] if m))
    Y['yields'].append('STATE  PLACE-papers phase2/method/ : the census`s versioned editions %d, the newest %s' % (len(eds), eds[-1][1] if eds else None))
    if not eds:
        raise Refuse('no versioned edition of the census in phase2/method/')
    cpath = eds[-1][1]
    cen = src.pp(cpath)
    cl = _one('PLACE-papers ' + cpath, cen, CLUSTERS, Y, 'the cluster table (§1)')
    kn = _one('PLACE-papers ' + cpath, cen, KERNELS, Y, 'the kernel table (§1A)')
    L.append('- the census`s cluster and kernel tables, at its newest edition: PLACE-papers %s :%d (the phases and clusters), :%d (the kernels)' % (
        cpath, cl[0], kn[0]))
    fi = src.pp('FINDINGS.md')
    op_ = _one('PLACE-papers FINDINGS.md', fi, LAYER_OPEN, Y, 'the reference layer`s opening heading (## I. )')[0]
    mv = _one('PLACE-papers FINDINGS.md', fi, LAYER_MOVE, Y, 'the heading "## How findings move"')[0]
    end = next((k for k in range(mv + 1, len(fi) + 1) if RULE_LINE.match(fi[k - 1])), None)
    if end is None:
        raise Refuse('FINDINGS.md: no rule line after "## How findings move" (:%d)' % mv)
    an = sum(1 for k in range(op_, end) if ANCHOR.match(fi[k - 1]))
    Y['yields'].append('STATE  PLACE-papers FINDINGS.md : the layer :%d-:%d, its anchors (### ) %d' % (op_, end, an))
    L.append('- the reference layer: PLACE-papers FINDINGS.md :%d-:%d, %d anchors, the rule for how an anchor moves at :%d' % (op_, end, an, mv))
    ins = src.pp(INSTR)
    ih = [(k, m.group(1)) for k, l in enumerate(ins or [], 1) for m in [IHEAD.match(l)] if m]
    Y['yields'].append('STATE  PLACE-papers %s : instrument heads (## I-<n>) %d' % (INSTR, len(ih)))
    if not ih:
        raise Refuse('%s: no instrument head' % INSTR)
    L.append('- the instruments: PLACE-papers %s, %d entries, the newest %s at :%d' % (INSTR, len(ih), ih[-1][1], ih[-1][0]))
    rl = src.relay_list()
    for rx, label, form in ((CLAUSES, 'the standing clauses', None), (RULES, 'the rules banks', 'data/<act>_rules.txt'),
                            (REGS, 'the registrations banks', 'data/<act>_registrations.txt')):
        ps = sorted(((int(m.group(1)), p) for p in rl for m in [rx.match(p)] if m))
        Y['yields'].append('STATE  relay data/ : %s %d' % (label, len(ps)))
        if not ps:
            raise Refuse('relay data/: %s not found' % label)
        if form is None:
            L.append('- %s: relay %s (the newest of %d editions)' % (label, ps[-1][1], len(ps)))
        else:
            L.append('- %s: relay %s, %d banks, %s to %s' % (label, form, len(ps), ps[0][1], ps[-1][1]))
    return L


def build(src, cap=CAP):
    """(the page's lines, the yields); Refuse where a needle is missing or the page is over the cap."""
    Y = dict(yields=[], cited=[])
    q = qword(src)
    sec = _section(src.pp('REGISTRY.md'), q[3], q[2])
    Y['yields'].append('QUOTING RULE  PLACE-papers REGISTRY.md : the heading by the sha256 opening %s at :%d ; its section :%d-:%d, %d lines, none printed' % (
        HEAD_DIGEST, q[3], min(sec), max(sec), len(sec)))
    hp, hk, ht = holds(src, q, Y)
    A = acts(src, q, Y)
    tl, ha, hh, nk, nt = the_next(src, q, Y)
    rows, op = open_orders(tl, Y)
    st = state(src, q, Y)
    ver = (src.relay('tools/standing/VERSION') or ['?'])[0].strip()
    P = ['# HANDOFF', '',
         '*Written whole by `tools/standing/handoff.py` (tools/standing/ %s) at relay `%s` and PLACE-papers `%s`, %s, from the banks: '
         'the closings and ferries of b%d to b%d (data/<act>_closing.txt :1, data/<act>_ferry.txt), %s (the holds), PLACE-papers '
         'OPEN_TRAILS.md (the Next and the open orders), REGISTRY.md, FINDINGS.md, %s and the census, and the relay`s standing clauses, '
         'rules banks and registrations banks; edited by no hand ((R364)(5)[H1]). Its earlier pages stand in this file`s history.*' % (
             ver, src.rhead, src.phead, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), A[-1][0], A[0][0], hp, INSTR), '',
         '## The holds in force', '', 'The last ruling`s clause on them, %s :%d:' % (hp, hk), '', '> ' + ht, '',
         '## The last twelve acts, newest first', '']
    for a, cp, ct, fp, fk, ft in A:
        P += ['### b%d' % a, '', '%s :1:' % cp, '', '> ' + ct, '', '%s :%d, THE ACT`S PLACE:' % (fp, fk), '', '> ' + ft, '']
    P += ['## The Next', '', 'PLACE-papers OPEN_TRAILS.md :%d, the trail of b%d headed at :%d:' % (nk, ha, hh), '', '> ' + nt, '',
          '## The open orders', '',
          '%d open of %d orders, read by `tools/standing/orders.py` from PLACE-papers OPEN_TRAILS.md at `%s`:' % (len(op), len(rows), src.phead), '',
          ', '.join('`%s`' % n for n in op) if op else '(none)', '',
          '## Where each kind of state is held', ''] + st + ['']
    Y['yields'].append('THE QUOTING RULE : lines cited and not quoted %d %s' % (len(Y['cited']), Y['cited']))
    Y['yields'].append('THE PAGE : %d lines (cap %d)' % (len(P), cap))
    if len(P) >= cap:
        raise Refuse('the page reads %d lines, the cap %d' % (len(P), cap))
    return P, Y


def _refused(src, **kw):
    try:
        build(src, **kw)
    except Refuse as e:
        return str(e)
    return None


def control():
    """the controls over banks planted in memory; returns (all as wanted, lines)."""
    base = Source()
    L, res = ['### THE CONTROLS OF tools/standing/handoff.py ((R364)(5)[H1]), at relay %s and PLACE-papers %s' % (base.rhead, base.phead)], []

    def case(kind, what, got, want):
        ok = got == want
        res.append(ok)
        L.append('  (%d) %s %s: %s -- %s' % (len(res), kind, what, got, 'AS WANTED' if ok else 'NOT AS WANTED'))

    try:
        P, Y = build(base)
        rec = (len(P) < CAP, sum(1 for y in Y['yields'] if y.startswith('ACT ')), all('PLACE 1 line(s)' in y for y in Y['yields'] if y.startswith('ACT ')))
    except Refuse as e:
        P, Y, rec = [], dict(yields=['### REFUSED: %s' % e], cited=[]), (False, 0, False)
    L += ['      ' + y for y in Y['yields']]
    case('RECORD', 'the page built from the banks at the two heads: under the cap, twelve acts, THE ACT`S PLACE once in each', rec, (True, TWELVE, True))
    cs = _nums(base.relay_list(), CLOSING)
    newest = cs[-1]
    fp, cp = 'data/b%d_ferry.txt' % newest, 'data/b%d_closing.txt' % newest
    f = base.relay(fp)
    k = next(i for i, l in enumerate(f) if PLACE.search(l))
    gone = f[:k] + f[k + 1:]
    case('CONSTRUCTED', 'b%d`s ferry with its THE ACT`S PLACE line taken out: refused, naming that ferry' % newest,
         fp in (_refused(Planted(base, relay={fp: gone})) or ''), True)
    curly = list(f)
    curly[k] = PLACE.sub(lambda m: m.group(0).replace("'", '’'), curly[k])
    try:
        Pc, _ = build(Planted(base, relay={fp: curly}))
        got = any('’S PLACE' in l for l in Pc)
    except Refuse:
        got = False
    case('CONSTRUCTED', 'b%d`s THE ACT`S PLACE written with the curly apostrophe (b745`s form): found and quoted' % newest, got, True)
    twin = f[:k + 1] + [f[k]] + f[k + 1:]
    case('CONSTRUCTED', 'b%d`s ferry carrying THE ACT`S PLACE twice: refused (one wanted)' % newest,
         'one wanted' in (_refused(Planted(base, relay={fp: twin})) or ''), True)
    c = base.relay(cp)
    case('CONSTRUCTED', '%s :1 not opening "b%d closed: ": refused' % (cp, newest),
         cp in (_refused(Planted(base, relay={cp: ['a planted head'] + c[1:]})) or ''), True)
    tl = base.pp('OPEN_TRAILS.md')
    rx, word, _lv, _hk = qword(base)
    hk = [i for i, l in enumerate(tl) if TRAIL.match(l)][-1]
    nk = next(i for i in range(hk + 1, len(tl)) if NEXT.match(tl[i]))
    nt = tl[nk].strip()
    planted = list(tl)
    planted[nk - 1] = planted[nk - 1] + ' ' + word
    try:
        Pq, Yq = build(Planted(base, pp={'OPEN_TRAILS.md': planted}))
        got = (any(nt in l for l in Pq), any('not quoted' in l and ':%d' % (nk + 1) in l for l in Pq))
    except Refuse:
        got = None
    case('CONSTRUCTED', 'the word planted on the line before the Next (the word read at run time, not printed): the Next cited, not quoted',
         got, (False, True))
    case('CONSTRUCTED', 'OPEN_TRAILS.md with no trail heading: refused',
         'no trail heading' in (_refused(Planted(base, pp={'OPEN_TRAILS.md': [l for l in tl if not TRAIL.match(l)]})) or ''), True)
    reg = base.pp('REGISTRY.md')
    above = reg[:_hk - 1] + ['a planted line'] + reg[_hk - 1:]
    try:
        qa = qword(Planted(base, pp={'REGISTRY.md': above}))
        got = (qa[3] - _hk, sorted(_section(above, qa[3], qa[2])) == [x + 1 for x in sorted(_section(reg, _hk, _lv))])
    except Refuse:
        got = None
    case('CONSTRUCTED', 'REGISTRY.md with a line planted above the heading: the heading and its section found one line down ((R370)(5)(i))',
         got, (1, True))
    case('CONSTRUCTED', 'REGISTRY.md with the heading removed: refused, no line carrying its digest (the quoting rule cannot run)',
         '0 lines carry' in (_refused(Planted(base, pp={'REGISTRY.md': reg[:_hk - 1] + reg[_hk:]})) or ''), True)
    case('CONSTRUCTED', 'REGISTRY.md with a second such heading: refused, two lines carrying its digest (the quoting rule cannot run)',
         '2 lines carry' in (_refused(Planted(base, pp={'REGISTRY.md': reg + [reg[_hk - 1]]})) or ''), True)
    case('CONSTRUCTED', 'the page`s cap set at 20 lines: refused', 'the cap 20' in (_refused(base, cap=20) or ''), True)
    L.append('### ### **HANDOFF CONTROLS %d ; AS WANTED %d ; ALL AS WANTED %s.**' % (len(res), sum(res), all(res)))
    return all(res), L


def main(argv):
    if not argv or argv[0] not in ('dry', 'write', 'control'):
        sys.exit(__doc__)
    if argv[0] == 'control':
        ok, L = control()
        print(NL.join(L))
        sys.exit(0 if ok else 1)
    try:
        P, Y = build(Source())
    except Refuse as e:
        print('### REFUSED, NOTHING WRITTEN: %s' % e)
        sys.exit(2)
    print(NL.join(Y['yields']))
    if argv[0] == 'dry':
        print('=' * 80)
        print(NL.join(P))
        return
    b = (NL.join(P) + NL).encode('utf-8')
    with open(OUT + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(OUT + '.tmp', OUT)
    print('written HANDOFF.md: %d lines, %d bytes, sha256 %s' % (len(P), len(b), hashlib.sha256(b).hexdigest()[:16]))


if __name__ == '__main__':
    main(sys.argv[1:])
