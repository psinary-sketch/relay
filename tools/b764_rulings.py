# -*- coding: utf-8 -*-
"""tools/b764_rulings.py -- b764, (R374)(7), (8) and (9): THE READ OF outputs/ FOR A DEPOSITED COPY; THE TEXTS OF THE RULING ENTERED IN
ERRATA, OPEN_TRAILS AND THE REGISTER BIBLIOGRAPHY.md.

Carried from tools/b763_rulings.py (its forms: the texts read from the ferry bank between their marker lines and checked against their
lines; each file appended at its end, its bytes at HEAD a prefix of its new bytes; the controls before the write; the ledgers banked by
line and sha256) by the Write tool, and committed before its run (N2). ERRATA's entry by the route of b760's (tools/b760_ledgers.py :316:
the file, a blank line, the entry, a line end).

  deposit dry|write   (9)(a): whether a file under PLACE-papers outputs/ holds a copy of the paper of REGISTRY's row 1.5c-15
                      (phase1.5/spectral/SEVEN_DISCRIMINANTS_AND_TRIVIUM_v0_1.md): for each file, how many of the paper's distinct lines of 40
                      characters or more stand in it as lines, and whether its :246, :264 and :292 do; counts and booleans alone, no line
                      printed. Controls: the paper itself reads whole, the archive's copy reads, a planted copy inside a deposited file reads,
                      the paper with its lines taken out reads none. Bank: data/b764_deposit_read.txt and .json.
  ledgers dry|write   appended at each file's end, no line moving, <DATE> the UTC date of the write:
                      ERRATA.md, [E1], its fields filled, its clause on a deposited copy from the deposit read's verdict;
                      OPEN_TRAILS.md, one dated head and under it [F1], [C1], [C2] or [C3] (from data/b764_xlines.json, the trial's fields
                      and run ids), [D1] for each order of (8) built in full, [D2], [M1] (from data/b764_imp2tau.json, its closing sentence
                      the author's word of 2026-11-20 (iv), data/b764_author_words_preseal.txt :9), [L1] (its prices from data/b764_price.txt)
                      and [B1], each a paragraph of its own;
                      BIBLIOGRAPHY.md, a section of its own: the five works the Epstein document's section 9.10 marks as not yet in the
                      register, each from the bank that holds it, a title no bank establishes marked TITLE-UNVERIFIED (nothing fetched).
                      Controls before the write, printed; the roster by tools/standing/orders.py's rule in memory, before and after, printed
                      and no condition. Bank: data/b764_ledgers.txt and .json, each appended text by line and sha256, its words printed by the
                      dry run alone.

No PLACE-papers line is printed but the texts this tool composes; no git write.
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
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b764_worklist as K   # noqa: E402

ACT, NL = 'b764', '\n'
PP = K.PP
FERRY = os.path.join(D, 'b764_ferry.txt')
FERRY_SHA = '594aa5dbae2a1a72'   # ### data/b764_stepzero.txt :18: the ferry bank's sha256
WORDS = os.path.join(D, 'b764_author_words_preseal.txt')
WORD_IV = 9                       # ### the author's word of 2026-11-20, (iv): [M1]'s closing sentence, between its first and last double quote
M1_OLD = "The source's appendix is read by the author's fetch."
ERRATA, OT, BIB, FIND = 'ERRATA.md', 'OPEN_TRAILS.md', 'BIBLIOGRAPHY.md', 'FINDINGS.md'
FILES = (ERRATA, OT, BIB)
WANT = dict(E1=(49, 61), F1=(65, 65), C1=(69, 69), C2=(73, 73), C3=(77, 77), D1=(81, 81), D2=(85, 85), G1=(89, 101), M1=(105, 105),
            M2=(109, 109), L1=(113, 113), B1=(117, 117), P1=(121, 137))
FIELD = re.compile(r'<[A-Za-z][^<>\n]*>')
NEW_NAME = 'W-ORD-RUNNER-CACHE'
XJSON = os.path.join(D, 'b764_xlines.json')
DROWS = os.path.join(D, 'b764_dispatch_rows.json')
IMP = os.path.join(D, 'b764_imp2tau.json')
PRICE = os.path.join(D, 'b764_price.txt')
DBANK, DJSON = os.path.join(D, 'b764_deposit_read.txt'), os.path.join(D, 'b764_deposit_read.json')
LBANK, LJSON = os.path.join(D, 'b764_ledgers.txt'), os.path.join(D, 'b764_ledgers.json')

# ### (9)(a): the paper and the copies read
PAPER = 'phase1.5/spectral/SEVEN_DISCRIMINANTS_AND_TRIVIUM_v0_1.md'
ARCHIVE = 'archive/2026-08-27-trim-backfill/SEVEN_DISCRIMINANTS_AND_TRIVIUM_v0_1.md'
CITED = (246, 264, 292)
NONE_CLAUSE = 'NO DEPOSITED ARTIFACT HOLDS THE PAPER.'

# ### (8) W-ORD-E0-RANK-PROPAGATION, [D2]: the table of b332 and b333's re-rank in its addendum, by line at the act's start (K.PRE_PP)
E0_TABLE, E0_RERANK, E0_ADDENDUM = 3078, 3117, 3105
E0_TABLE_HEAD = '| rank | constituent | softest grade | why it sits here |'
Q_FROM, Q_TO = 'Ranking, softest first:', 'K4 (DERIVED-ON-CONTENT).'

# ### (8) W-ORD-BIBLIOGRAPHY-LINK: the section appended to the register, each work from the bank that holds it (nothing fetched, (13))
BIB_SOURCES = (('data/b751_literature.txt', 22, ('On the Zeros of Epstein Zeta Functions', '1204.6297v1')),
               ('data/b358_source_lagarias0404394.txt', 3005, ('X.-J. Li, The positivity of a sequence of numbers and the Riemann hypothesis',)),
               ('data/b358_source_lagarias0404394.txt', 3006, ('Theory 65 (1997), 325',)))
BIB_KEYS = ('1204.6297', 'Li1997', 'Epstein1903', 'Baker1971', 'Stark1975')
BIB_HEAD = '## §6 — THE EPSTEIN DOCUMENT’S WORKS NOT YET IN THE REGISTER *(added <DATE>, b764)*'
BIB_TEXT = [
    BIB_HEAD, '',
    '*Brought current under `(R374)`(8), `W-ORD-BIBLIOGRAPHY-LINK` (OPEN_TRAILS :18967): the five works that '
    'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md marks in its §9.10 as not yet in this register, each entered at the grade the record '
    'holds it and from the bank that holds it. Nothing was fetched; a title that no bank of the record establishes is marked `TITLE-UNVERIFIED`, '
    'as this file’s law orders, and none is completed from memory. No entry above this section is edited.*', '',
    '| key | work | grade in this corpus |',
    '|:--|:--|:--|',
    '| `1204.6297` | Y. Lee, *On the Zeros of Epstein Zeta Functions*, arXiv:1204.6297v1 [math.NT] (2012) | `READ-AT-CONTENT` — read in full at '
    'b751 (relay `data/b751_literature.txt`, S1, its sha256 there); the Epstein document’s §5 states the classical theorems in its statements |',
    '| `Li1997` | X.-J. Li, *The positivity of a sequence of numbers and the Riemann hypothesis*, J. Number Theory **65** (1997), 325–333 | '
    '`POINTER-ONLY` — named in the corpus, not read; its title, venue and pages as the pinned source math/0404394 prints them at its reference '
    '[35] (relay `data/b358_source_lagarias0404394.txt` :3005-:3006) |',
    '| `Epstein1903` | P. Epstein (1903) | `TITLE-UNVERIFIED` — named in the Epstein document’s §2 for the continuation and the functional '
    'equation, not read; no bank of the record gives its title |',
    '| `Baker1971` | A. Baker (1971) | `TITLE-UNVERIFIED` — cited as the Epstein document’s §9.10 records the kernel citing it (C2Walk.lean, '
    'the docstring of `walk`), for the eighteen fields of class number 2; not read |',
    '| `Stark1975` | H. M. Stark (1975) | `TITLE-UNVERIFIED` — cited as the same docstring cites it, for the same fields; not read |']


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def today():
    return time.strftime('%Y-%m-%d', time.gmtime())


def git(repo, *a, raw=False):
    r = subprocess.run(['git', '-C', repo, *a], capture_output=True)
    return r.stdout if raw else r.stdout.decode('utf-8', 'replace')


def fsha(p):
    try:
        with open(p, 'rb') as f:
            return sha(f.read())[:16]
    except OSError:
        return 'ABSENT'


def put(path, text):
    with open(path + '.tmp', 'wb') as f:
        f.write(text.encode('utf-8'))
    os.replace(path + '.tmp', path)


def ids():
    import b764_address_scan as SC
    return dict(name=SC.author_name(), orcid=SC.author_orcid(), address=SC.previous_address())


def idcount(text, I):
    low = text.lower()
    return dict(name=low.count(I['name'].lower()), orcid=low.count(I['orcid'].lower()), address=low.count(I['address'].lower()),
                github=low.count('github.com/'))


def at_head(path):
    b = git(PP, 'show', 'HEAD:' + path, raw=True)
    with open(os.path.join(PP, *path.split('/')), 'rb') as f:
        w = f.read()
    if not b or b != w:
        die('%s: ITS WORKING FILE IS NOT ITS BYTES AT HEAD (%d, %d bytes)' % (path, len(b), len(w)))
    if b'\r' in b or not b.endswith(b'\n'):
        die('%s: CARRIAGE RETURNS OR NO FINAL LINE END' % path)
    return b.decode('utf-8')


def at_pre(path):
    return git(PP, 'show', '%s:%s' % (K.PRE_PP, path), raw=True).decode('utf-8').replace('\r', '').split(NL)


def relay_line(path, n):
    with open(os.path.join(RELAY, *path.split('/')), encoding='utf-8') as f:
        L = f.read().replace('\r', '').split(NL)
    return L[n - 1] if len(L) >= n else ''


# ================================================================================ THE TEXTS
def ferry():
    with open(FERRY, 'rb') as f:
        b = f.read()
    if sha(b)[:16] != FERRY_SHA:
        die('THE FERRY BANK IS NOT ITS STEP-ZERO BYTES (sha256 %s)' % sha(b)[:16])
    return b.decode('utf-8').split(NL)


def texts(L):
    """{key: (first line, last line, text)} for each piece between '---- [K] ...' and '---- end [K]'; the lines checked against WANT."""
    out = {}
    for i, l in enumerate(L):
        m = re.match(r'^---- \[([A-Z]\d*)\] ', l)
        if m:
            k = m.group(1)
            j = L.index('---- end [%s]' % k, i)
            out[k] = (i + 2, j, NL.join(L[i + 1:j]))
    got = dict((k, (a, b)) for k, (a, b, _t) in out.items())
    if got != WANT:
        die('THE RULING`S TEXTS NOT AT THEIR LINES: %s' % sorted(set(got.items()) ^ set(WANT.items())))
    return out


def word_iv():
    with open(WORDS, encoding='utf-8') as f:
        L = f.read().replace('\r', '').split(NL)
    l = L[WORD_IV - 1]
    if not l.startswith('(iv) In [M1], the closing sentence reads: "'):
        die('THE AUTHOR`S WORD (iv) NOT AT data/b764_author_words_preseal.txt :%d' % WORD_IV)
    return l[l.index('"') + 1:l.rindex('"')]


# ================================================================================ (9)(a) THE READ OF outputs/
def _lines(rel):
    with open(os.path.join(PP, *rel.split('/')), 'rb') as f:
        return f.read().decode('utf-8', 'replace').replace('\r', '').split(NL)


def _score(keys, cite, T_):
    S = set(l.strip() for l in T_)
    return len(keys & S), [c in S for c in cite]


def deposit_read():
    P = _lines(PAPER)
    if P != at_pre(PAPER):
        die('THE PAPER IS NOT ITS BYTES AT THE ACT`S START')
    keys = set(l.strip() for l in P if len(l.strip()) >= 40)
    cite = [P[n - 1].strip() for n in CITED]
    files = []
    for base, _d, fs in os.walk(os.path.join(PP, 'outputs')):
        for f in sorted(fs):
            files.append(os.path.relpath(os.path.join(base, f), PP).replace('\\', '/'))
    files.sort()
    rows = []
    for rel in files:
        n, c = _score(keys, cite, _lines(rel))
        rows.append(dict(path=rel, lines=len(_lines(rel)), hit=n, cites=c))
    found = [r['path'] for r in rows if r['hit'] or any(r['cites'])]
    pn, pc = _score(keys, cite, P)
    an, ac = _score(keys, cite, _lines(ARCHIVE))
    dep = [r['path'] for r in rows if r['path'].startswith('outputs/DEPOSITED')]
    host = _lines(dep[0]) if dep else []
    plant_n, plant_c = _score(keys, cite, host + [P[CITED[1] - 1]])
    gone_n, gone_c = _score(keys, cite, [l for l in P if l.strip() not in keys])
    ctl = [('the paper itself reads whole: %d of %d, the three lines %s' % (pn, len(keys), pc), pn == len(keys) and all(pc)),
           ('the archive`s copy reads: %d of %d, the three lines %s' % (an, len(keys), ac), an > len(keys) // 2 and all(ac)),
           ('a planted copy of :%d inside %s reads found: %s' % (CITED[1], dep[0] if dep else 'NONE', plant_c), bool(dep) and plant_c[1]),
           ('the paper with its lines of 40 characters or more taken out reads none: %d, %s' % (gone_n, gone_c), gone_n == 0 and not any(gone_c)),
           ('the files under outputs/ read: %d, %d of them under a DEPOSITED folder' % (len(rows), len(dep)), len(rows) > 0 and len(dep) > 0)]
    return dict(rows=rows, found=found, keys=len(keys), ctl=ctl, verdict='FOUND' if found else 'NONE')


def deposit(mode):
    R = deposit_read()
    ok = all(o for _w, o in R['ctl'])
    P = ['%s -- (R374)(9)(a): WHETHER A FILE UNDER PLACE-papers outputs/ HOLDS A COPY OF %s (%s)' % (ACT, PAPER, utc()), '',
         '### tools/b764_rulings.py deposit; PLACE-papers HEAD %s, the paper read at the act`s start %s (equal); each file under outputs/ by its'
         % (git(PP, 'rev-parse', '--short=8', 'HEAD').strip(), K.PRE_PP[:8]),
         '### lines, stripped: how many of the paper`s %d distinct lines of 40 characters or more stand in it, and whether :%d, :%d and :%d do;'
         % ((R['keys'],) + CITED),
         '### counts and booleans alone, no line of any file printed.', '', '## THE CONTROLS']
    P += ['  %-120s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in R['ctl']]
    P += ['', '## THE FILES: path | lines | the paper`s lines in it | :%d | :%d | :%d' % CITED]
    P += ['  %s | %d | %d of %d | %s | %s | %s' % ((r['path'], r['lines'], r['hit'], R['keys']) + tuple(r['cites'])) for r in R['rows']]
    P += ['', '## THE VERDICT: %s' % (('NO FILE UNDER outputs/ HOLDS THE PAPER: [E1] reads "%s"' % NONE_CLAUSE) if R['verdict'] == 'NONE' else
                                      'FOUND IN %s: [E1]`s clause is the seat`s to compose' % R['found']),
          '### ### **THE DEPOSIT READ: FILES %d ; FOUND %d ; CONTROLS %d OF %d ; %s.**' % (
              len(R['rows']), len(R['found']), sum(1 for _w, o in R['ctl'] if o), len(R['ctl']),
              ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    put(DBANK, NL.join(P) + NL)
    put(DJSON, json.dumps(dict(at=utc(), act=ACT, paper=PAPER, cited=list(CITED), keys=R['keys'], rows=R['rows'], found=R['found'],
                               verdict=R['verdict'], controls=[[w, o] for w, o in R['ctl']]), ensure_ascii=False, indent=1) + NL)
    print('written data/b764_deposit_read.txt and .json')


# ================================================================================ THE FIELDS
def price_fields():
    with open(PRICE, encoding='utf-8') as f:
        L = f.read().split(NL)
    lp = {}
    for l in L:
        m = re.match(r'^  \(9\)\(c\) \[L-(i|ii|iii|iv)\] .*\| dispatches \d+-\d+ \| ([0-9.]+-[0-9.]+ h), BESIDE, NOT SUMMED$', l)
        if m:
            lp[m.group(1)] = m.group(2)
    foot = [re.search(r'\(7\) ([0-9.]+-[0-9.]+ h) IN (\d+) DISPATCHES', l) for l in L if l.startswith('### ### **THE PRICE TABLE')]
    p7 = ('%s in %s dispatches (relay data/b764_price.txt)' % (foot[0].group(1), foot[0].group(2))) if foot and foot[0] else None
    return [lp.get(k) for k in ('i', 'ii', 'iii', 'iv')], p7


def e0_fields():
    F = at_pre(FIND)
    t, r = F[E0_TABLE - 1], F[E0_RERANK - 1]
    heads = [n for n in range(E0_RERANK - 1, 0, -1) if F[n - 1].startswith('#')]
    a = r.find(Q_FROM)
    b = r.find(Q_TO, a)
    q = r[a:b + len(Q_TO)] if a >= 0 and b >= 0 else ''
    ok = (t == E0_TABLE_HEAD and r.startswith('**The re-rank, under the sealed rule with nothing adjusted.**') and bool(heads) and
          heads[0] == E0_ADDENDUM and 'b333' in F[E0_ADDENDUM - 1] and r.count(Q_FROM) == 1 and bool(q))
    return q, ok, heads[0] if heads else None


def imp_fields():
    J = json.load(open(IMP, encoding='utf-8')) if os.path.isfile(IMP) else {}
    return J.get('verdict'), len(J.get('cells') or []), J.get('digits'), J.get('controls')


def trial_lines(X):
    """data/b764_xlines.json: {"trial": {"key": "C2" | "C3", "fields": [[placeholder, value], ...], "runs": [run id, ...]}}."""
    if not os.path.isfile(XJSON):
        return None
    J = json.load(open(XJSON, encoding='utf-8'))
    r = J['trial']
    if r['key'] not in ('C2', 'C3'):
        die('THE TRIAL`S LINE OF NO KNOWN KEY: %r' % r['key'])
    t = X[r['key']][2]
    for ph, val in r['fields']:
        if ph not in t:
            die('%s: THE FIELD %r NOT IN ITS TEMPLATE' % (r['key'], ph))
        t = t.replace(ph, val, 1)
    return r['key'], t, r['fields'], [str(x) for x in r.get('runs', [])]


# ================================================================================ THE LEDGERS
def compose(date, base, R_dep):
    X = texts(ferry())
    lp, p7 = price_fields()
    q, e0_ok, _h = e0_fields()
    verdict, n_cells, digits, _c = imp_fields()
    iv = word_iv()
    E = {}
    e1 = X['E1'][2].replace('<DATE>', date)
    m = re.search(r'<Where the seat\'s read of outputs/ finds a deposited copy.*?>', e1)
    if m and R_dep.get('verdict') == 'NONE':
        e1 = e1.replace(m.group(0), NONE_CLAUSE, 1)
    E['E1'] = e1
    E['F1'] = X['F1'][2].replace('<DATE>', date)
    E['C1'] = X['C1'][2].replace('<price>', p7 or '<price>', 1)
    tl = trial_lines(X)
    if tl:
        E[tl[0]] = tl[1]
    E['D2'] = X['D2'][2].replace('<line>', str(E0_TABLE), 1).replace('<line>', str(E0_RERANK), 1).replace('<the quotation>', '“%s”' % q, 1)
    m1 = X['M1'][2]
    if verdict == 'HELD':
        m1 = m1.replace('<n>', str(n_cells), 1).replace('<d>', str(digits), 1)
        if M1_OLD in m1:
            m1 = m1.replace(M1_OLD, iv, 1)
        E['M1'] = m1
    l1 = X['L1'][2]
    for v in lp:
        l1 = l1.replace('<price>', v or '<price>', 1)
    E['L1'] = l1
    E['B1'] = X['B1'][2]
    # ### the register's section, then the line of [D1] that names its line
    bib = NL.join(BIB_TEXT).replace('<DATE>', date)
    new_bib = base[BIB] + NL + '---' + NL + NL + bib + NL
    bib_line = new_bib.split(NL).index(BIB_HEAD.replace('<DATE>', date)) + 1
    what = ('the register BIBLIOGRAPHY.md brought current, its §6 at :%d entering the five works the Epstein document’s §9.10 marks as not yet '
            'in it, each at the grade the record holds it and from the bank that holds it, nothing fetched (relay data/b764_ledgers.txt); from it '
            'each keystone draws its own list by key at its re-cut' % bib_line)
    E['D1'] = X['D1'][2].replace("<the order's name>", 'W-ORD-BIBLIOGRAPHY-LINK', 1).replace(
        '<what was built, by its bank or its file and line>', what, 1)
    n_ot = len(base[OT].split(NL)) - 1
    head = ('**Dated head, %s, b764, `(R374)`(7), (8) and (9): the lines the ruling orders for OPEN_TRAILS** (relay data/b764_ferry.txt '
            ':64-:118), appended at the end of the file after b763’s trail (its last line :%d) and before this act’s own trail, so that no line of '
            'the trail moves: the fact item of the seven discriminants beside ERRATA E-%s-1; the runner’s order entered and the line of its '
            'trial; the line of the order of (8) built in full and the line of the E0 rank; the finite part’s comparison made; the centre priced '
            'anew; the bridge carried. The orders of (8) not built in full take no line here and are carried by name with their prices in the '
            'act’s entry.' % (date, n_ot, date))
    order = ['F1', 'C1', 'C2', 'C3', 'D1', 'D2', 'M1', 'L1', 'B1']
    paras = [head] + [E[k] for k in order if k in E]
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    T_ = {ERRATA: E['E1'], OT: ot, BIB: bib}
    new = {ERRATA: base[ERRATA] + NL + E['E1'] + NL, OT: base[OT] + NL + ot + NL, BIB: new_bib}
    return dict(X=X, E=E, texts=T_, new=new, head=head, tl=tl, lp=lp, p7=p7, q=q, e0_ok=e0_ok, imp=(verdict, n_cells, digits), iv=iv,
                bib_line=bib_line, ot_first=n_ot + 2, order=order)


def ledgers(mode):
    from standing import orders as O
    date = today()
    base = dict((p, at_head(p)) for p in FILES)
    R_dep = json.load(open(DJSON, encoding='utf-8')) if os.path.isfile(DJSON) else {}
    C = compose(date, base, R_dep)
    X, E, new = C['X'], C['E'], C['new']
    I = ids()
    # ### each entered text against the ruling's with its fields filled, read independently of compose()
    want = {}
    want['E1'] = X['E1'][2].replace('<DATE>', date)
    want['E1'] = re.sub(r'<Where the seat\'s read of outputs/ finds a deposited copy.*?>', NONE_CLAUSE, want['E1'], count=1)
    want['F1'] = X['F1'][2].replace('<DATE>', date)
    where = dict(E1=ERRATA)
    eq = {}
    for k, v in E.items():
        tpl = X[k][2] if k != 'M1' else X[k][2].replace(M1_OLD, C['iv'])
        pat = re.escape(tpl)
        for ph in sorted(set(FIELD.findall(tpl)), key=len, reverse=True):
            pat = pat.replace(re.escape(ph), '(.+?)')
        eq[k] = bool(re.fullmatch(pat, v, re.S)) and (NL + v + NL) in (NL + C['texts'][where.get(k, OT)] + NL)
    eq_e1f1 = E['E1'] == want['E1'] and E['F1'] == want['F1']
    left = sorted(set(m for t in C['texts'].values() for m in FIELD.findall(t)))
    ticks = [(p, k + 1) for p, t in C['texts'].items() for k, l in enumerate(t.split(NL)) if l.count('`') % 2]
    rows_d = json.load(open(DROWS, encoding='utf-8')) if os.path.isfile(DROWS) else []
    rows_d = rows_d.get('rows', rows_d) if isinstance(rows_d, dict) else rows_d
    runs_known = set(str(r.get('run')) for r in rows_d if isinstance(r, dict) and r.get('run'))
    runs_cited = C['tl'][3] if C['tl'] else []
    src_ok = [(p, n, all(s in relay_line(p, n) for s in ss)) for p, n, ss in BIB_SOURCES]
    keys_new = [k for k in BIB_KEYS if k in base[BIB]]
    st = lambda R, n: (R.get(n) or {}).get('status')   # noqa: E731
    before = dict(O.read(base[OT].split(NL)))
    after = dict(O.read(new[OT].split(NL)))
    moved = sorted(n for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    open_b = sum(1 for n in before if st(before, n) == 'OPEN')
    open_a = sum(1 for n in after if st(after, n) == 'OPEN')
    rows = []
    for p in FILES:
        b, n_ = base[p], new[p]
        nl_, k_ = n_.split(NL), len(b.split(NL)) - 1
        while k_ < len(nl_) and nl_[k_] in ('', '---'):
            k_ += 1
        rows.append(dict(path=p, lines_before=len(b.split(NL)) - 1, lines_after=len(n_.split(NL)) - 1, first_new=k_ + 1,
                         sha_before=sha(b)[:16], sha_after=sha(n_)[:16], text_sha=sha(C['texts'][p])[:16], prefix=n_.startswith(b),
                         ids_equal=idcount(b, I) == idcount(n_, I), ids_added=sum(idcount(C['texts'][p], I).values())))
    v, nc, dg = C['imp']
    ctl = [('each file`s bytes at HEAD a prefix of its new bytes: no line moves', all(r['prefix'] for r in rows)),
           ('each text as entered equals the ruling`s with its fields filled ([M1] with the author`s word (iv) in its closing sentence), each whole '
            'in its file`s text: %s' % ' '.join('%s %s' % (k, eq[k]) for k in sorted(eq)), all(eq.values()) and eq_e1f1),
           ('no field left in the appended texts (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts equal before and after in each file, and 0 in the appended texts',
            all(r['ids_equal'] for r in rows) and not any(r['ids_added'] for r in rows)),
           ('ERRATA holds no E-%s-1 and OPEN_TRAILS no %s before the write' % (date, NEW_NAME),
            ('E-%s-1' % date) not in base[ERRATA] and NEW_NAME not in base[OT]),
           ('the deposit read banked, its verdict %s, [E1]`s clause from it' % (R_dep.get('verdict') or 'ABSENT'),
            R_dep.get('verdict') == 'NONE' and NONE_CLAUSE in E['E1']),
           ('the trial`s line composed from data/b764_xlines.json (%s), each run id it cites in data/b764_dispatch_rows.json (%s)' % (
               C['tl'][0] if C['tl'] else 'ABSENT', runs_cited or 'none'), bool(C['tl']) and bool(runs_cited) and all(x in runs_known for x in runs_cited)),
           ('the finite part`s bank HELD at %s cells to %s digits (data/b764_imp2tau.json, controls %s), [M1] entered' % (nc, dg, imp_fields()[3]),
            v == 'HELD' and nc == 9 and 'M1' in E),
           ('[D2]: FINDINGS :%d the table`s head, :%d b333`s re-rank under its addendum`s heading :%d, the quotation read once from its bytes at %s'
            % (E0_TABLE, E0_RERANK, E0_ADDENDUM, K.PRE_PP[:8]), C['e0_ok']),
           ('[L1]`s four prices and [C1]`s read from data/b764_price.txt (%s ; %s)' % (C['lp'], C['p7']), all(C['lp']) and bool(C['p7'])),
           ('the register`s section: each source line holds what it is cited for (%s) ; no key already in the register (%s)' % (
               ' '.join('%s :%d %s' % s for s in src_ok), keys_new or 'none'), all(s[2] for s in src_ok) and not keys_new)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R374)(7), (8) AND (9): ERRATA, OPEN_TRAILS AND THE REGISTER BIBLIOGRAPHY.md, EACH APPENDED AT ITS END (%s)' % (ACT, utc()), '',
         '### tools/b764_rulings.py ledgers; PLACE-papers HEAD %s; the texts from the ferry bank (data/b764_ferry.txt :%d-:%d), the trial`s line from'
         % (git(PP, 'rev-parse', '--short=8', 'HEAD').strip(), WANT['E1'][0], WANT['B1'][1]),
         '### data/b764_xlines.json (sha256 %s), [M1]`s closing sentence from data/b764_author_words_preseal.txt :%d, the deposit read from' % (fsha(XJSON), WORD_IV),
         '### data/b764_deposit_read.json (sha256 %s), and the seat`s own two texts (the dated head and the register`s section); <DATE> %s; each by'
         % (fsha(DJSON), date),
         '### line and sha256 here.', '', '## THE CONTROLS']
    P += ['  %-130s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed; no condition)',
          '  open before %d -> after %d ; orders %d -> %d ; added %s' % (open_b, open_a, len(before), len(after), [(n, st(after, n)) for n in added] or 'none'),
          '  statuses moving: %s' % ([(n, st(before, n), st(after, n)) for n in moved] or 'none')]
    P += ['', '## THE FILES: path | lines before -> after | the appended text from | its sha256 | the file`s sha256 before -> after']
    P += ['  %s | %d -> %d | :%d | %s | %s -> %s' % (r['path'], r['lines_before'], r['lines_after'], r['first_new'], r['text_sha'], r['sha_before'],
                                                     r['sha_after']) for r in rows]
    nl_ot = new[OT].split(NL)
    P += ['', '## THE PARAGRAPHS BY LINE: OPEN_TRAILS head :%d ; ' % (nl_ot.index(C['head']) + 1) + ' ; '.join(
        '%s :%d (sha256 %s)' % (k, nl_ot.index(E[k]) + 1, sha(E[k])[:16]) for k in C['order'] if k in E),
        '  ERRATA [E1] from :%d (sha256 %s) ; BIBLIOGRAPHY §6 at :%d (sha256 %s)' % (rows[0]['first_new'], sha(E['E1'])[:16], C['bib_line'],
                                                                                   sha(C['texts'][BIB])[:16])]
    P += ['', '### ### **THE LEDGERS: FILES 3 OF 3 APPENDED, NO LINE MOVING ; [E1] IN ERRATA ; %d LINES IN OPEN_TRAILS UNDER ONE HEAD (%s) ; THE '
              'REGISTER`S §6, FIVE WORKS ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
                  len([k for k in C['order'] if k in E]), ', '.join(k for k in C['order'] if k in E), sum(1 for _w, o in ctl if o), len(ctl),
                  ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        for p in FILES:
            print(NL + '### THE TEXT APPENDED TO %s (the dry run`s print alone):' % p)
            print(C['texts'][p])
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    if os.path.exists(LBANK):
        die('THE BANK STANDS ALREADY')
    if any(idcount(NL.join(P), I).values()):
        die('AN IDENTIFIER IN THE BANK')
    for p in FILES:
        with open(os.path.join(PP, *p.split('/')), 'wb') as f:
            f.write(new[p].encode('utf-8'))
    if any(fsha(os.path.join(PP, *p.split('/'))) != sha(new[p])[:16] for p in FILES):
        die('A WRITTEN FILE IS NOT ITS COMPOSITION')
    put(LBANK, NL.join(P) + NL)
    put(LJSON, json.dumps(dict(at=utc(), act=ACT, date=date, files=rows, entered=dict((k, [nl_ot.index(t) + 1 if k != 'E1' else rows[0]['first_new'],
                                                                                         sha(t)[:16]]) for k, t in E.items()),
                               head=[nl_ot.index(C['head']) + 1, sha(C['head'])[:16]], bib_line=C['bib_line'], trial=C['tl'][:1] + C['tl'][2:] if C['tl'] else None,
                               roster=dict(before_open=open_b, after_open=open_a, added=added, moved=[[n, st(before, n), st(after, n)] for n in moved]),
                               xlines_sha=fsha(XJSON), deposit_sha=fsha(DJSON), controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written ERRATA.md, OPEN_TRAILS.md and BIBLIOGRAPHY.md ; data/b764_ledgers.txt and .json')


def main(argv):
    what, mode = (argv + ['', ''])[:2]
    if mode not in ('dry', 'write'):
        sys.exit(__doc__)
    if what == 'deposit':
        deposit(mode)
    elif what == 'ledgers':
        ledgers(mode)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
