# -*- coding: utf-8 -*-
"""b655_record.py -- THE ACT'S RECORD TOOL, b655 under (R265).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b655's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows (tools/b655_regspec.py) can run each reader over one row of each shape before the seal.
### Routes: `python tools/b655_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/1199f364-78c4-4147-843f-edf01bb11b28/scratchpad'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported
import b655_worklist as K          # noqa: E402


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(path):
    return io.open(path, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(path) else ''


def rdn(name):
    return rd(os.path.join(D, name))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def _ws(s):
    return ' '.join(s.split())


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b655's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b655_scanfile_%s.md' % tag)
    R3._write(p, allt.encode('utf-8'))
    sc = R3._scan(p)
    clean = R3._clean(sc)
    ticks = odd_lines(allt)
    unread = [x for x in ('### NOT', 'None', ' ? ', '`?`') if x in allt]
    outside = [n for n in R41.OAI_NEEDLES if n in allt]
    stems = [s for s in ('gap', 'blind') if re.search(r'\b' + s, allt, re.I)]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks by line: %s ; unread figures: %s ; outside names: %s ; '
          'stems: %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', outside or 'NONE',
                         stems or 'NONE'))
    if not clean:
        print(sc[-1500:])
    fired = bool(any(nd.values()) or not clean or ticks or unread or outside or stems)
    return [tuple(c) for c in cells], fired


def land(items, bank, tag, entry=None, check=(), expect_cells=(), dry=True):
    for f, ln, needle in check:
        L = rd(FIND if f == 'FINDINGS.md' else OT).split(NL)
        if needle not in L[ln - 1]:
            sys.exit('### %s :%d DOES NOT CARRY %r -- NOTHING WRITTEN' % (f, ln, needle))
    items = [(f, h, conv(t)) for f, h, t in items]
    cells, fired = screens(items, tag, dry)
    if dry:
        for f, h, t in items:
            print('----', f, NL + t)
        return
    if cells != [tuple(x) for x in expect_cells] or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    n = {'FINDINGS.md': len(rd(FIND).split(NL)), 'OPEN_TRAILS.md': len(rd(OT).split(NL))}
    want = {}
    for f, h, t in items:
        want[h] = n[f] + 1 if rd(FIND if f == 'FINDINGS.md' else OT).endswith(NL) else n[f] + 2
        n[f] += len(t.strip(NL).split(NL)) + 1
    for f, h, _t in items:
        guard_absent(FIND if f == 'FINDINGS.md' else OT, h)
    out = []
    for f, h, t in items:
        path = FIND if f == 'FINDINGS.md' else OT
        r = append_to(path, t)
        got = line_of(path, h)
        out.append(dict(file=f, head=h, line=got, append=r))
        if got != want[h]:
            put_json(bank, dict(entry=entry, lines=out, at=utc(), stopped=True))
            sys.exit('### %s LANDED AT :%s, NOT :%d -- STOPPED' % (h[:60], got, want[h]))
    put_json(bank, dict(entry=entry, lines=out, at=utc()))
    print('  ' + ' ; '.join('%s :%s' % (x['file'], x['line']) for x in out))


# ================================================================================ THE READERS, ONE PER ROW SHAPE A ROUTE READS ((R263)(3))
RUNNER_KEYS = ('kernel', 'branch', 'ref', 'target', 'run_id', 'conclusion', 'artifact_sha256', 'mem_low', 'stopped', 'gate', 'merged', 'tag')


def read_runner_row(r):
    """a row of data/b655_runner_rows.json -- every key of RUNNER_KEYS present (None where a step did not reach it); returns the row's reading
    (kernel, outcome, merged) that the scores, the record and the closing print; raises KeyError on a row of another shape."""
    missing = [k for k in RUNNER_KEYS if k not in r]
    if missing:
        raise KeyError('runner row without %s' % missing)
    if r['stopped']:
        outcome = 'STOPPED BENEATH THE HOLD ON THE RUNNER'
    elif r['conclusion'] != 'success':
        outcome = 'RUN %s' % (r['conclusion'] or 'NOT CONCLUDED')
    else:
        outcome = 'GATE %s' % (r['gate'] or 'UNREAD')
    return dict(kernel=r['kernel'], outcome=outcome, merged=r['merged'], low=r['mem_low'], above_hold=(r['mem_low'] is not None and r['mem_low'] >= 2560))


def read_score_row(k, v):
    """a scores row: key N1..N5 or S1..S5, value [verdict, text]; returns (key, first verdict word, text)."""
    if not re.match(r'^[NS][1-5]$', k) or not isinstance(v, list) or len(v) != 2:
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0].split(' ')[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


def read_grade_row(k, row):
    """a row of the hand grades (data/b655_sentence_grades.json): block number k and [sentence number, the cell's quoted words];
    returns (k, n, words); raises on a row of another shape."""
    n, w = row
    ok_n = (isinstance(n, int) and n >= 1) or (isinstance(n, str) and re.match(r'^\d+\.\d+$', n) is not None)
    if not ok_n or not isinstance(w, str) or not w.strip() or not str(k).isdigit():
        raise ValueError('grade row of another shape: %r' % (row,))
    return int(k), (n if isinstance(n, str) else n), w


READERS = ('read_runner_row', 'read_score_row', 'read_head', 'read_grade_row')


# ================================================================================ COMPONENT 2: THE SENTENCE ROWS, THE PLAIN COMMENTS, THE GRADES
def _bank_line(bank_lines, rid_tail):
    for i, l in enumerate(bank_lines, 1):
        if l.startswith('  %s@%s:%s |' % (K.KERNEL, K.K_MAIN, rid_tail)):
            return i
    return None


def sentences(*a):
    """(R265)(2), the b651 route: the kernel's OVERREACHES, UNDERSTATES and UNLICENSED blocks of b647's bank read into sentence rows (rows are
    sentences, parents are blocks) at the kernel's main; data/b655_table_<kernel>_sentences.txt and .json."""
    import b647_record as B7
    import licensed_table as LT
    import collections
    N = _ws
    parents = [r for r in jl(K.PARENTS)['rows'] if r['verdict'] in ('OVERREACHES', 'UNDERSTATES', 'UNLICENSED')]
    bl = rdn(K.PARENTS.replace('.json', '.txt')).split(NL)
    ctx, orig = {}, LT.docstring_row

    def cap(rid, source, doc, *args, **kw):
        ctx.setdefault(N(doc), (source, args, kw))
        return orig(rid, source, doc, *args, **kw)
    LT.docstring_row = cap
    try:
        B7._kdoc_rows(K.KERNEL)
    finally:
        LT.docstring_row = orig
    rows, unread = [], []
    for p in parents:
        c = ctx.get(N(p['stated']))
        if c is None:
            unread.append(p)
            continue
        src, args, kw = c
        units = [s for s in B7._MSPLIT.split(p['stated'].strip()) if s.strip()]
        for j, u in enumerate(units, 1):
            r = orig('%s.s%d' % (p['id'], j), p['source'], u, *args, **kw)
            rows.append(dict(id=r['id'], parent=p['id'], parent_line=_bank_line(bl, p['source']), parent_verdict=p['verdict'], kind=p['kind'],
                             n=j, of=len(units), sentence=N(u), generated=r['verdict'], findings=r.get('findings') or [],
                             hand_needed=r.get('hand_needed')))
    gc = collections.Counter(x['generated'] for x in rows)
    main = g(K.KD, 'rev-parse', '--short=7', 'main').strip()
    L = ['b655 -- COMPONENT 2, (R265)(2): %s`S OVERREACHES, UNDERSTATES AND UNLICENSED BLOCKS READ INTO SENTENCE ROWS (%s)' % (K.KERNEL, utc()), '',
         '### rows are sentences, parents are blocks. The parents: relay data/%s, its OVERREACHES, UNDERSTATES and UNLICENSED rows (%d), read at %s; '
         'the generator: b647_record._kdoc_rows at %s main %s, each block`s context captured and each unit read by licensed_table.docstring_row; the '
         'unit: b647_record._MSPLIT (a sentence split where . ! or ? meets whitespace) -- the b651 route. A GENERATED reading per sentence; the HAND '
         'reading per sentence is the grade bank`s.' % (K.PARENTS, len(parents), K.K_MAIN, K.KERNEL, main),
         '### parents read %d ; parents not found at main %d (%s)' % (len(parents) - len(unread), len(unread),
                                                                       '; '.join('%s (%s)' % (u['source'], u['decl'] or u['kind']) for u in unread) or 'none'), '']
    cur = None
    for x in rows:
        if x['parent'] != cur:
            cur = x['parent']
            L += ['', '== %s (%s ; b647`s bank line :%s ; HAND %s ; %d sentences)' % (x['parent'].split(':', 1)[1], x['kind'], x['parent_line'],
                                                                                     x['parent_verdict'], x['of'])]
        L.append('  s%d %-11s %s' % (x['n'], x['generated'], x['sentence'][:600]))
    L += ['', '### ### **PARENT BLOCKS %d ; SENTENCE ROWS %d ; GENERATED: %s ; HAND PER SENTENCE: the grade bank`s.**' % (
        len(parents) - len(unread), len(rows), ', '.join('%s %d' % kv for kv in sorted(gc.items())))]
    put_txt('b655_table_%s_sentences.txt' % K.KERNEL, [l.replace('\r', '') for l in L])
    put_json(K.SENT, dict(at=utc(), main=main, rows=rows, unread=[u['id'] for u in unread]))
    print(NL.join(L[2:4] + L[-1:]))


# ### the needle of b650's finding (relay data/b650_resonances_navigator.txt :25; OPEN_TRAILS :13836): a plain comment asserting the unsupported
# ### claim -- no off-line zero; all zeros on the line; RH or GRH holding, proved or true
NEEDLE = re.compile(r'no off[- ]line zero|all (?:the )?(?:nontrivial |non-trivial )?zeros? (?:lie |are |sit )?on|zeros? on (?:the )?(?:critical line|'
                    r'σ ?= ?1/2|sigma ?= ?1/2|re ?s ?= ?1/2)|(?:\bRH\b|\bGRH\b|Riemann Hypothesis)\W{0,3}(?:holds|is (?:true|proved|proven|established))|'
                    r'(?:proves?|proof of|establish(?:es)?) (?:the )?(?:\bRH\b|\bGRH\b|Riemann Hypothesis)', re.I)


def _plain_blocks(text):
    """every plain block comment `/- ... -/` in a file (not `/--`, not `/-!`), with its first line; nesting followed."""
    out, i, n = [], 0, len(text)
    while i < n:
        j = text.find('/-', i)
        if j < 0:
            break
        if text.startswith('/--', j) or text.startswith('/-!', j):
            k, depth = j + 3, 1
        else:
            k, depth = j + 2, 1
        while k < n and depth:
            if text.startswith('/-', k):
                depth += 1
                k += 2
            elif text.startswith('-/', k):
                depth -= 1
                k += 2
            else:
                k += 1
        if not (text.startswith('/--', j) or text.startswith('/-!', j)):
            out.append((text[:j].count(NL) + 1, text[j:k]))
        i = k
    return out


def plain(*a):
    """(R265)(2): the kernel's plain block comments at its main scanned by the needle; every hit a candidate row for the hand reading."""
    import b647_record as B7
    files = [f for f in g(K.KD, 'ls-files', '*.lean').split(NL) if f.strip()]
    nblocks, hits = 0, []
    for f in files:
        t = _show(K.KD, 'main', f) or ''
        for ln, b in _plain_blocks(t):
            nblocks += 1
            for s in B7._MSPLIT.split(_ws(b.strip('/-'))):
                if NEEDLE.search(s):
                    hits.append((f, ln, _ws(s)))
    ctl = [s for s in ('NO OFF-LINE ZERO EXISTS.', 'Therefore: all nontrivial zeros on σ = 1/2.', 'The Riemann Hypothesis holds.') if NEEDLE.search(s)]
    neg = [s for s in ('the zero side is negative', 'a zero of zeta off the line is excluded at the window') if NEEDLE.search(s)]
    L = ['b655 -- COMPONENT 2, (R265)(2): %s`S PLAIN BLOCK COMMENTS SCANNED BY THE NEEDLE (%s)' % (K.KERNEL, utc()), '',
         '### rows are plain block comments (`/-`, not `/--`, not `/-!`) of the kernel`s tracked .lean files at main %s; the needle: a sentence asserting '
         'the unsupported claim, b650`s finding (relay data/b650_resonances_navigator.txt :25, OPEN_TRAILS :13836) -- tools/b655_record.py NEEDLE.' % (
             g(K.KD, 'rev-parse', '--short=7', 'main').strip()),
         '### the needle`s controls: b650`s two sentences and a planted one read %d of 3 ; two sentences that assert nothing of the kind read %d of 2.' % (
             len(ctl), len(neg)),
         '### files %d ; plain block comments %d ; needle hits %d:' % (len(files), nblocks, len(hits))]
    L += ['  %s:%d -- %s' % h for h in hits] or ['  NONE']
    # ### a second, wider shape before the count is banked: every plain-comment sentence naming RH, GRH, Riemann, the line or the zeros, for the hand
    wide = []
    W = re.compile(r'\bRH\b|\bGRH\b|Riemann|critical line|off-line|nontrivial zero|zeros? of (?:ζ|zeta|L)', re.I)
    for f in files:
        t = _show(K.KD, 'main', f) or ''
        for ln, b in _plain_blocks(t):
            for s in B7._MSPLIT.split(_ws(b.strip('/-'))):
                if W.search(s):
                    wide.append((f, ln, _ws(s)))
    L += ['### THE WIDER SHAPE (RH, GRH, Riemann, the critical line, off-line, nontrivial zeros, zeros of zeta or L), read by hand: %d sentences' % len(wide)]
    L += ['  %s:%d -- %s' % (f, ln, s[:300]) for f, ln, s in wide]
    L += ['  the hand reading: %s' % (a[0] if a else '### NOT READ')]
    L += ['', '### ### **PLAIN BLOCK COMMENTS %d ; NEEDLE HITS %d ; CONTROLS %d OF 3 READ, %d OF 2 QUIET ; WIDER SHAPE %d, ASSERTING ROWS BY HAND %s.**' % (
        nblocks, len(hits), len(ctl), 2 - len(neg), len(wide), (a[1] if len(a) > 1 else '?'))]
    put_txt('b655_plain_comments.txt', L)
    put_json('b655_plain_comments.json', dict(at=utc(), files=len(files), blocks=nblocks, hits=[list(h) for h in hits], controls=[len(ctl), 2 - len(neg)]))
    print(NL.join(L[3:]))


def blocks():
    """[(k, parent id, parent row, [sentence rows])] in the sentence bank's order, k from 1."""
    import collections
    s = jl(K.SENT)['rows']
    t = dict((r['id'], r) for r in jl(K.PARENTS)['rows'])
    by = collections.OrderedDict()
    for r in s:
        by.setdefault(r['parent'], []).append(r)
    return [(k, p, t[p], rs) for k, (p, rs) in enumerate(by.items(), 1)]


BULLET = re.compile(r'\s(?=· )')


def split_rows(rs, split):
    """the block's rows, keyed by sentence number as text; a sentence named in `split` (the author's word at b655 on #46) read as its bullet
    rows `n.1`, `n.2`, ... -- the lead before the first bullet, then each bullet -- split where a space meets the bullet mark."""
    out = []
    for r in rs:
        if str(r['n']) in split:
            for i, part in enumerate([p for p in BULLET.split(r['sentence']) if p.strip()], 1):
                out.append(dict(n='%d.%d' % (r['n'], i), sentence=_ws(part)))
        else:
            out.append(dict(n=str(r['n']), sentence=r['sentence']))
    return out


def cut(rows, graded, action, bullets=False, premise=None):
    """the mechanical rule: a graded OVERREACHES or UNDERSTATES row replaced in place by the ACTION (by its sentences; by its bullets in order,
    the i-th graded bullet by the i-th ACTION bullet, where the block's rows are bullets), an UNLICENSED one removed, MATCHES untouched; then a
    sentence that repeats one already in the block dropped -- the earlier occurrence kept, unless `premise` (the author's word at b655 on #50)
    names the conclusion and premise rows: then the occurrence after the premise row is kept, the conclusion standing where its premise stands
    before it. Returns (kept, dropped, the placement printed)."""
    import b647_record as R47
    act = action[len('RE-CUT: '):] if action.startswith('RE-CUT: ') else action
    abul = [p for p in BULLET.split(act.strip()) if p.strip()]
    out, gi = [], 0
    for r in rows:
        gr = graded.get(r['n'])
        if gr is None:
            out.append((r['n'], r['sentence']))
        elif gr == 'UNLICENSED':
            continue
        elif bullets:
            out.append((r['n'], _ws(abul[min(gi, len(abul) - 1)])))
            gi += 1
        else:
            out += [(r['n'], x) for x in R47._MSPLIT.split(act.strip()) if x.strip()]
    note = ''
    keep_at = {}
    if premise:
        c, p = str(premise['conclusion']), str(premise['premise'])
        pos_p = next((i for i, (n, _x) in enumerate(out) if n == p), None)
        csent = [x for n, x in out if n == c]
        if csent and pos_p is not None:
            idx = [i for i, (_n, x) in enumerate(out) if _ws(x) == _ws(csent[0])]
            after = [i for i in idx if i > pos_p]
            keep_at[_ws(csent[0])] = after[0] if after else idx[0]
            note = ('the conclusion row s%s drawn on the premise row s%s (%s); the premise survives as a MATCHES row, so the conclusion stands '
                    'after it, at s%s`s place; its other occurrence dropped as a repeat' % (c, p, out[pos_p][1][:120], out[keep_at[_ws(csent[0])]][0]))
    kept, dropped, seen = [], [], set()
    slots = []
    for i, (_n, x) in enumerate(out):
        w = _ws(x)
        if w in keep_at:
            if i == keep_at[w]:
                kept.append(x)
                slots.append((_n, x, True))
            else:
                dropped.append(x)
                slots.append((_n, x, False))
            continue
        if w in seen:
            dropped.append(x)
            slots.append((_n, x, False))
            continue
        seen.add(w)
        kept.append(x)
        slots.append((_n, x, True))
    cut.slots = slots
    return kept, dropped, note


def grades(*a):
    """(R265)(2): data/b655_sentence_grades.txt from the hand grades (data/b655_sentence_grades.json), every quoted word read as a verbatim
    substring of the parent's HAND LICENSED cell before anything is written; the cut plan beside it."""
    G = jl(K.GRADES)
    gr = G['grades']
    comp = G.get('completed') or {}
    L = ['b655 -- COMPONENT 2, (R265)(2): %s`S SENTENCE ROWS GRADED BY HAND, BOUND TO THE PARENT BLOCK`S HAND CELLS; BANKED FOR THE AUTHOR`S '
         'STRIKE BEFORE ANY EDIT (%s)' % (K.KERNEL, utc()), '',
         '### the rule (b652`s, (R265)(2)): a sentence row is graded OVERREACHES, UNDERSTATES or UNLICENSED where the parent block`s HAND LICENSED or',
         '### CITED cell names, quotes or paraphrases that sentence`s claim, the grade citing the cell`s words beside it; a sentence those cells do not',
         '### reach stays MATCHES; a block whose cells reach no sentence is UNRESOLVED, not cut; an ACTION carrying "..." is UNRESOLVED-CELL, completed',
         '### from the block`s own LICENSED words as b653 did (relay data/b653_elided_cells.txt) and raised with the grades. The grade is the parent`s',
         '### verdict. Each graded row carries the parent`s ACTION verbatim. The sources: relay data/%s, data/%s (b647); the hand grades:' % (K.SENT, K.PARENTS),
         '### data/%s. Every quoted cell word read as a verbatim substring of the parent`s LICENSED cell before the bank was written.' % K.GRADES,
         '### Below each block: the block as the mechanical rule leaves it -- graded rows replaced in place by the ACTION, repeats dropped and printed.', '']
    n_rows = n_graded = n_unres = n_drop = n_cell = 0
    by_v, J, unres = {}, [], []
    SPLIT, PREM = G.get('split') or {}, G.get('premise') or {}
    for k, p, q, rs0 in blocks():
        split = (SPLIT.get(str(k)) or {})
        rs = split_rows(rs0, split)
        n_rows += len(rs)
        mine = dict((str(n), w) for _k, n, w in (read_grade_row(k, x) for x in gr.get(str(k), [])))
        bad = [w for w in mine.values() if w not in q['licensed']]
        if bad:
            sys.exit('### BLOCK %d: A QUOTED WORD NOT IN THE LICENSED CELL -- NOTHING WRITTEN: %s' % (k, bad))
        far = [n for n in mine if n not in [r['n'] for r in rs]]
        if far:
            sys.exit('### BLOCK %d: A GRADED ROW THE BLOCK DOES NOT HAVE -- NOTHING WRITTEN: %s' % (k, far))
        v = q['verdict']
        L.append('== #%d %s (b647`s bank line :%s ; %s ; HAND %s ; %d sentence rows%s)' % (
            k, p.split(':', 1)[1], rs0[0]['parent_line'], q['kind'], v, len(rs),
            ('; s%s read as its bullet rows by the author`s word at b655' % ', s'.join(split)) if split else ''))
        L.append('   LICENSED : ' + q['licensed'])
        L.append('   ACTION   : ' + q['action'])
        action = q['action']
        if '...' in q['action']:
            n_cell += 1
            c = comp.get(str(k))
            L.append('   ### UNRESOLVED-CELL: the ACTION carries "..."; completed from the block`s own LICENSED words for the strike: %s' % (
                c or '### NOT COMPLETED'))
            if not c:
                sys.exit('### BLOCK %d: AN ELIDED ACTION NOT COMPLETED -- NOTHING WRITTEN' % k)
            span = c[len('RE-CUT: '):] if c.startswith('RE-CUT: ') else c
            if span.rstrip('.') not in q['licensed']:
                sys.exit('### BLOCK %d: A COMPLETION NOT A SPAN OF THE LICENSED CELL -- NOTHING WRITTEN' % k)
            L.append('   ### the completion is a verbatim span of the LICENSED cell; words from outside it 0.')
            action = c
        graded = {}
        for r in rs:
            if r['n'] in mine:
                graded[r['n']] = v
                n_graded += 1
                by_v[v] = by_v.get(v, 0) + 1
                L.append('  s%-4s %-11s %s' % (r['n'], v, r['sentence']))
                L.append('        %-11s cell: "%s"' % ('', mine[r['n']]))
            else:
                L.append('  s%-4s %-11s %s' % (r['n'], 'MATCHES', r['sentence']))
        if not graded:
            n_unres += 1
            unres.append(k)
            L.append('   ### UNRESOLVED: no sentence the cells reach; not cut.')
            J.append(dict(k=k, parent=p, file=q['file'], line=q['line'], unresolved=True))
            L.append('')
            continue
        prem = PREM.get(str(k))
        kept, dropped, note = cut(rs, graded, action, bullets=bool(split), premise=prem)
        n_drop += len(dropped)
        if split:
            L.append('   ### the ACTION read as its bullets, the i-th graded bullet row replaced by the i-th ACTION bullet (the author`s word at b655).')
        if prem:
            L.append('   ### THE PREMISE RULE (the author`s word at b655): the conclusion row printed with the row it draws on --')
            L.append('       conclusion s%s: %s' % (prem['conclusion'], [r['sentence'] for r in rs if r['n'] == str(prem['conclusion'])][0]))
            L.append('       premise    s%s: %s' % (prem['premise'], [r['sentence'] for r in rs if r['n'] == str(prem['premise'])][0]))
            L.append('       ' + note)
        L.append('   -> THE BLOCK AFTER THE CUT (%d sentences; repeats dropped %d):' % (len(kept), len(dropped)))
        L += ['        ' + x for x in kept] + ['        ### DROPPED AS A REPEAT: ' + x for x in dropped]
        J.append(dict(k=k, parent=p, file=q['file'], line=q['line'], bank_line=rs0[0]['parent_line'], verdict=v, graded=sorted(graded),
                      action=action, completed=('...' in q['action']), kept=kept, dropped=dropped, sentences=[r['sentence'] for r in rs0],
                      split=sorted(split), premise=prem))
        L.append('')
    pl = jl('b655_plain_comments.json')
    L.append('### PLAIN-COMMENT ROWS (relay data/b655_plain_comments.txt): %s' % ('; '.join('%s:%d -- %s' % tuple(h) for h in pl.get('hits') or []) or 'NONE'))
    n_cut = len([b for b in J if b.get('kept') is not None])
    files = sorted(set(b['file'] for b in J if b.get('kept') is not None))
    L.append('### ### **PARENT BLOCKS %d ; SENTENCE ROWS %d ; GRADED %d (%s) ; MATCHES %d ; UNRESOLVED BLOCKS %d (%s) ; UNRESOLVED-CELL %d ; '
             'BLOCKS TO CUT %d IN %d FILES ; REPEATS DROPPED BY THE RULE %d ; PLAIN-COMMENT ROWS %d.**' % (
                 len(J), n_rows, n_graded, ', '.join('%s %d' % kv for kv in sorted(by_v.items())), n_rows - n_graded, n_unres,
                 ', '.join('#%d' % e for e in unres) or 'none', n_cell, n_cut, len(files), n_drop, len(pl.get('hits') or [])))
    put_txt('b655_sentence_grades.txt', L)
    put_json('b655_sentence_cut_plan.json', dict(at=utc(), blocks=J))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE CUT PLANNED ON THE BLOBS, (R265)(3)
def _norm_map(text):
    """the text with every whitespace run collapsed to one space, and the raw index of each normalized character."""
    out, idx, prev_ws = [], [], False
    for i, ch in enumerate(text):
        if ch.isspace():
            if not prev_ws:
                out.append(' ')
                idx.append(i)
            prev_ws = True
        else:
            out.append(ch)
            idx.append(i)
            prev_ws = False
    return ''.join(out), idx


def _wrap(text, indent, width=118):
    import textwrap
    return ('\n' + indent).join(textwrap.wrap(text, width - len(indent), break_long_words=False, break_on_hyphens=False)) or ''


def _code_only(t):
    out, i, depth, n = [], 0, 0, len(t)
    while i < n:
        if t.startswith('/-', i):
            depth += 1
            i += 2
            continue
        if depth and t.startswith('-/', i):
            depth -= 1
            i += 2
            continue
        if depth:
            i += 1
            continue
        if t.startswith('--', i):
            j = t.find(NL, i)
            i = n if j < 0 else j
            continue
        if t[i] == '"':
            j = i + 1
            while j < n and t[j] != '"':
                j += 2 if t[j] == chr(92) else 1
            out.append(t[i:j + 1])
            i = j + 1
            continue
        out.append(t[i])
        i += 1
    return ' '.join(''.join(out).split())


def _plans():
    """per graded block: (k, q, rows, slots) -- the rows read as the grade bank reads them, the cut's slot outputs."""
    G = jl(K.GRADES)
    gr, comp, SPLIT, PREM = G['grades'], G.get('completed') or {}, G.get('split') or {}, G.get('premise') or {}
    out = []
    for k, p, q, rs0 in blocks():
        split = SPLIT.get(str(k)) or {}
        rs = split_rows(rs0, split)
        mine = dict((str(n), w) for _k, n, w in (read_grade_row(k, x) for x in gr.get(str(k), [])))
        graded = dict((r['n'], q['verdict']) for r in rs if r['n'] in mine)
        if not graded:
            continue
        action = comp.get(str(k)) if '...' in q['action'] else q['action']
        cut(rs, graded, action, bullets=bool(split), premise=PREM.get(str(k)))
        out.append((k, q, rs, cut.slots))
    return out


def plan_cut(*a):
    """(R265)(3): the cut planned on the kernel's main blobs: every row of a graded block located in order in its file by its whitespace-collapsed
    text; each changed row (graded, or dropped as a repeat) replaced in its span by its slot's kept output, wrapped at the line's indent; one
    edit per block (the region from the first changed row to the last). The planned file checked: its comment-stripped code equal to main's.
    Banked as data/b655_cut_edits.json (the edits, old and new regions) and data/b655_cut_plan.txt."""
    files, edits, fails = {}, [], []
    for k, q, rs, slots in _plans():
        f = q['file']
        if f not in files:
            files[f] = (_show(K.KD, K.K_MAIN, f) or '').replace(chr(13), '')
        text = files[f]
        start_line_off = sum(len(l) + 1 for l in text.split(NL)[:q['line'] - 1])
        norm, idx = _norm_map(text)
        nstart = next(i for i, ri in enumerate(idx) if ri >= start_line_off)
        spans, pos = {}, nstart
        for r in rs:
            s = _ws(r['sentence'])
            j = norm.find(s, pos)
            if j < 0:
                fails.append('#%d s%s not found' % (k, r['n']))
                break
            spans[r['n']] = (idx[j], idx[j + len(s) - 1] + 1)
            pos = j + len(s)
        if len(spans) != len(rs):
            continue
        out_by = {}
        for n, x, keep in slots:
            out_by.setdefault(n, []).append((x, keep))
        changed = [r['n'] for r in rs if [x for x, kp in out_by.get(r['n'], []) if kp] != [r['sentence']]]
        if not changed:
            continue
        reg0 = min(spans[n][0] for n in changed)
        reg1 = max(spans[n][1] for n in changed)
        new = text[reg0:reg1]
        for n in sorted(changed, key=lambda n_: -spans[n_][0]):
            s0, s1 = spans[n]
            line_start = text.rfind(NL, 0, s0) + 1
            indent = re.match(r'[ \t]*', text[line_start:]).group(0)
            repl = ' '.join(x for x, kp in out_by.get(n, []) if kp)
            repl = _wrap(repl, indent) if repl else ''
            a0, a1 = s0 - reg0, s1 - reg0
            if not repl:
                # ### a removed row takes the whitespace run before it (the line breaks and indent that led to it), or, where it opens the
                # ### region, the run after it, so no line of a single space or an empty line stays where the row stood
                if a0 > 0:
                    while a0 > 0 and new[a0 - 1].isspace():
                        a0 -= 1
                else:
                    while a1 < len(new) and new[a1].isspace():
                        a1 += 1
            new = new[:a0] + repl + new[a1:]
        old = text[reg0:reg1]
        if text.count(old) != 1:
            fails.append('#%d region not unique in %s' % (k, f))
        edits.append(dict(k=k, file=f, line=q['line'], old=old, new=new, changed=changed))
    planned = {}
    for f, t in files.items():
        nt = t
        for e in [x for x in edits if x['file'] == f]:
            nt = nt.replace(e['old'], e['new'], 1)
        planned[f] = nt
    code_bad = [f for f in files if _code_only(files[f]) != _code_only(planned[f])]
    L = ['b655 -- COMPONENT 3, (R265)(3): THE CUT PLANNED ON %s`S MAIN BLOBS AT %s (%s)' % (K.KERNEL, K.K_MAIN, utc()), '',
         '### from relay data/b655_sentence_grades.txt (rows are sentences, parents are blocks) and its hand grades; each graded block`s rows located in',
         '### order in its file; each changed row replaced in its span by its slot`s kept output, wrapped at the line`s indent; one edit per block.',
         '### files %d ; edits %d ; rows located %s ; regions not unique %s ; files whose comment-stripped code differs from main`s %s' % (
             len(files), len(edits), 'ALL' if not [x for x in fails if 'not found' in x] else fails,
             [x for x in fails if 'unique' in x] or 'NONE', code_bad or 'NONE'), '']
    for e in edits:
        L += ['== #%d %s:%d (rows changed %s)' % (e['k'], e['file'], e['line'], ', '.join('s' + n for n in e['changed'])),
              '   OLD: ' + e['old'].replace(NL, ' | ')[:900], '   NEW: ' + e['new'].replace(NL, ' | ')[:900], '']
    L += ['### ### **FILES %d ; EDITS %d ; LOCATION FAILURES %d ; CODE OUTSIDE COMMENTS CHANGED IN %d FILES.**' % (
        len(files), len(edits), len(fails), len(code_bad))]
    put_txt('b655_cut_plan.txt', L)
    put_json('b655_cut_edits.json', dict(at=utc(), main=K.K_MAIN, edits=edits, planned_sha={f: __import__('hashlib').sha256(t.encode('utf-8')).hexdigest()
                                                                                           for f, t in planned.items()}, fails=fails, code_bad=code_bad))
    print(NL.join(L[4:5] + L[-1:]))


def _planned(f):
    j = jl('b655_cut_edits.json')
    t = (_show(K.KD, j['main'], f) or '').replace(chr(13), '')
    for e in [x for x in j['edits'] if x['file'] == f]:
        t = t.replace(e['old'], e['new'], 1)
    return t


def check_file(*a):
    """`check_file <file> [head]`: the working file (CR stripped) or the branch head's blob against the planned text, byte for byte, and its
    comment-stripped code against main's. Prints one line; exits 1 on a difference."""
    import hashlib
    f = a[0]
    want = _planned(f)
    if len(a) > 1 and a[1] == 'head':
        got = (_show(K.KD, K.CUT_BRANCH, f) or '')
        where = 'blob at %s' % K.CUT_BRANCH
    else:
        got = io.open(os.path.join(K.KD, f), encoding='utf-8', newline='').read().replace(chr(13), '')
        where = 'working file'
    main = (_show(K.KD, K.K_MAIN, f) or '').replace(chr(13), '')
    same, code = got == want, _code_only(got) == _code_only(main)
    print('  %-48s %s %s planned (sha %s) ; code outside comments %s main`s' % (
        f, where, 'EQUALS' if same else '### DIFFERS FROM', hashlib.sha256(got.encode('utf-8')).hexdigest()[:12],
        'EQUAL TO' if code else '### DIFFERENT FROM'))
    if not (same and code):
        sys.exit(1)


def _regrade(ref):
    """every graded row of the grade bank looked for in its file at `ref`, whitespace aside: standing or gone, by its parent's verdict."""
    import collections
    G = jl(K.GRADES)
    files, standing, gone = {}, [], 0
    cnt = collections.Counter()
    for k, q, rs, _slots in _plans():
        mine = set(str(n) for _k, n, _w in (read_grade_row(k, x) for x in G['grades'].get(str(k), [])))
        f = q['file']
        if f not in files:
            files[f] = _ws(_show(K.KD, ref, f) or '')
        for r in rs:
            if r['n'] not in mine:
                cnt['MATCHES'] += 1
                continue
            if _ws(r['sentence']) in files[f]:
                standing.append((k, f, r['n'], q['verdict'], r['sentence']))
                cnt[q['verdict'] + ' (STANDING)'] += 1
            else:
                gone += 1
                cnt['CUT'] += 1
    return cnt, standing


def cut_bank(*a):
    """(R265)(3): data/b655_cut_SIDE-global-section.txt -- the branch, its commits one per file, each head blob against the plan and its
    comment-stripped code against main's, and the grade bank re-run at the branch with its control at main."""
    gk = lambda *x: g(K.KD, *x)   # noqa: E731
    log = [l.split(' ', 1) for l in gk('log', '--reverse', '--format=%h %s', 'main..' + K.CUT_BRANCH).split(NL) if l.strip()]
    plan = jl('b655_cut_edits.json')
    pf = sorted(set(e['file'] for e in plan['edits']))
    rows, bad = [], []
    for h, s in log:
        fs = [x for x in gk('show', '--name-only', '--format=', h).split(NL) if x.strip()]
        f = fs[0] if len(fs) == 1 else None
        if f is None:
            bad.append('%s touches %d files' % (h, len(fs)))
            continue
        head = _show(K.KD, K.CUT_BRANCH, f) or ''
        main = (_show(K.KD, K.K_MAIN, f) or '').replace(chr(13), '')
        eq, code = head == _planned(f), _code_only(head) == _code_only(main)
        if not (eq and code):
            bad.append(f)
        ks = [e['k'] for e in plan['edits'] if e['file'] == f]
        rows.append('  %s  %-44s blocks %-22s blob %s ; code outside comments %s' % (
            h, f, ', '.join('#%d' % k for k in ks), 'EQUALS THE PLAN' if eq else '### DIFFERS', 'EQUAL TO MAIN`S' if code else '### CHANGED'))
    after, st = _regrade(K.CUT_BRANCH)
    ctl, st0 = _regrade('main')
    L = ['b655 -- COMPONENT 3, (R265)(3): %s`S DOCSTRINGS CUT ON THE BRANCH %s (%s)' % (K.KERNEL, K.CUT_BRANCH, utc()), '',
         '### the grades: relay data/b655_sentence_grades.txt (rows are sentences, parents are blocks; the author`s word at Component 2: 49 as banked,',
         '### #46 read as bullet rows, #50 by the premise rule); the plan: data/b655_cut_plan.txt; one commit per file by the Edit tool, each',
         '### working file checked against the plan before its commit; the branch from main %s.' % K.K_MAIN, '',
         '### THE COMMITS (rows are commits, one per file):'] + rows + [
         '', '### COMMITS %d ; FILES IN THE PLAN %d ; COMMITS TOUCHING ONE FILE %d ; FAULTS %s' % (len(log), len(pf), len(rows), bad or 'NONE'),
         '', '### THE GRADE BANK RE-RUN AT THE BRANCH (each graded row looked for in its file, whitespace aside):',
         '  ' + ', '.join('%s %d' % kv for kv in sorted(after.items())),
         '  graded rows still standing: %s' % (['#%d %s s%s %s' % x[:4] for x in st] or 'NONE'),
         '### THE CONTROL, the same read at main: ' + ', '.join('%s %d' % kv for kv in sorted(ctl.items())), '',
         '### ### **COMMITS %d IN %d FILES ; GRADED ROWS CUT %d ; STANDING %d (OVERREACHES %d, UNDERSTATES %d, UNLICENSED %d) ; AT MAIN STANDING %d ; '
         'FAULTS %d.**' % (len(log), len(pf), after.get('CUT', 0), len(st), after.get('OVERREACHES (STANDING)', 0), after.get('UNDERSTATES (STANDING)', 0),
                           after.get('UNLICENSED (STANDING)', 0), len(st0), len(bad))]
    put_txt('b655_cut_SIDE-global-section.txt', L)
    put_json('b655_cut_SIDE-global-section.json', dict(at=utc(), commits=[x[0] for x in log], files=len(pf), faults=bad, after=dict(after),
                                                        standing=[list(x) for x in st], control=dict(ctl), control_standing=len(st0)))
    print(NL.join(L[-8:]))


# ================================================================================ COMPONENT 3: THE RUNNER, (R265)(3) under (R263)(4)
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
PRINT_RE = re.compile(r"^'(.+?)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", re.M)
ERR_RE = re.compile(r'^(?:error: )?(\S+\.lean):(\d+):(\d+): error: (.*)$', re.M)


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def _prints(text):
    out = []
    for m in PRINT_RE.finditer(text):
        out.append((m.group(1), sorted(x.strip() for x in (m.group(2) or '').split(',') if x.strip())))
    return out


def runner(*a):
    """`runner`: the run read by its id; the artifact listed, downloaded by its id into memory, its sha256 against the platform's digest before
    any reading; Core: the modules built in the recorded order and their failures, AllPrints' prints against AXIOM_PRINTS.txt at main (raw and
    line by line); Interfaces: the mathlib pin, the six files' prints against AXIOM_PRINTS_INTERFACES.txt at main line by line; the error
    lines; the memory log's low and any STOP; the gate per named terminal (every print at the standard three or none). Banked as
    data/b655_runner_SIDE-global-section.txt and a row of data/b655_runner_rows.json."""
    import hashlib
    import zipfile
    kern = K.KERNEL
    R = K.RUNNER[kern]
    repo = 'psinary-sketch/' + kern
    rc, out, err = _gh('run', 'view', str(R['run_id']), '-R', repo, '--json', 'status,conclusion,headSha,createdAt,updatedAt,url')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, R['run_id']))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    wf = _show(K.KD, 'main', '.github/workflows/build-module.yml') or ''
    row = dict(kernel=kern, branch=R['branch'], ref=R['ref'], target=R['target'], run_id=R['run_id'], conclusion=run.get('conclusion'),
               artifact_sha256=None, mem_low=None, stopped=False, gate=None, merged=None, tag=None)
    L = ['b655 -- COMPONENT 3, (R265)(3): THE HOSTED RUNNER FOR %s, READ BY ITS RUN ID (%s)' % (kern, utc()), '',
         '### the workflow file on main (%s, .github/workflows/build-module.yml), read back whole:' % R['workflow_commit']] + \
        ['    ' + l for l in wf.rstrip(NL).split(NL)] + ['',
         '### the dispatch, the one dispatch of this branch: ref %s ; target %s' % (R['ref'], R['target']),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head of the workflow %s ; %s to %s' % (
             R['run_id'], run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('createdAt'), run.get('updatedAt'))]
    T_ = {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        row['artifact_sha256'] = sha
        L.append('### the artifact: id %s ; name %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN',
            'AGREE' if digest and digest == sha else ('### DIFFER' if digest else 'no digest to compare')))
        if digest and digest != sha:
            row['artifact_sha256'] = None
        else:
            with zipfile.ZipFile(io.BytesIO(rz.stdout)) as z:
                for n in z.namelist():
                    T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    else:
        L.append('### the artifact: ### NONE LISTED')
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    row['mem_low'] = int(low[-1]) if low else None
    stops = [l for l in mem.split(NL) if l.startswith('STOP ')]
    row['stopped'] = bool(stops)
    order = [x for x in T_.get('order.txt', '').split(NL) if x.strip()]
    cfail = T_.get('core_fails.txt', '').strip()
    cblog, iblog = T_.get('core_build.log', ''), T_.get('interfaces_build.log', '')
    errs = [(m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)) for m in ERR_RE.finditer(cblog + NL + iblog)]
    allp = T_.get('allprints.txt', '')
    banked_core = (_show(K.KD, 'main', 'AXIOM_PRINTS.txt') or '')
    banked_if = (_show(K.KD, 'main', 'AXIOM_PRINTS_INTERFACES.txt') or '')
    core_raw = allp == banked_core
    cl_b, cl_r = banked_core.split(NL), allp.split(NL)
    core_diff = [i + 1 for i in range(max(len(cl_b), len(cl_r))) if (cl_b[i] if i < len(cl_b) else None) != (cl_r[i] if i < len(cl_r) else None)]
    ifp = T_.get('interfaces.txt', '')
    if_b = [l for l in banked_if.split(NL) if l.startswith("'")]
    if_r = [l for l in ifp.split(NL) if l.startswith("'")]
    if_diff = [i + 1 for i in range(max(len(if_b), len(if_r))) if (if_b[i] if i < len(if_b) else None) != (if_r[i] if i < len(if_r) else None)]
    P = _prints(allp) + _prints(ifp)
    off = [(n, ax) for n, ax in P if not set(ax) <= STD3 or 'sorryAx' in ax]
    exits = re.findall(r'^### (\S+) exit (\d+)$', iblog, re.M)
    ok = (run.get('conclusion') == 'success' and row['artifact_sha256'] and cfail == '0' and core_raw and not core_diff and not if_diff
          and len(if_r) == len(if_b) > 0 and not errs and not stops and row['mem_low'] is not None and row['mem_low'] >= 2560 and P and not off
          and all(e == '0' for _f, e in exits))
    row['gate'] = 'DERIVES' if ok else ('STOPPED BENEATH THE HOLD' if stops else 'NOT DERIVES')
    row['errors'] = [list(e) for e in errs]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the mathlib checkout (out/mathlib_ref.txt): %s' % ' '.join(T_.get('mathlib_ref.txt', '### UNREAD').split()),
          '### the memory log: samples %d ; LOW %s MB ; the hold 2560 ; STOP lines %s' % (
              len([l for l in mem.split(NL) if 'avail_mb=' in l]), row['mem_low'], stops or 'NONE'),
          '### CORE: modules in the recorded order %d ; failures %s ; AllPrints exit %s ; prints %d ; against AXIOM_PRINTS.txt at main: raw %s, lines '
          'differing %s' % (len(order), cfail or '### UNREAD', T_.get('allprints_exit.txt', '?').strip(), len(_prints(allp)),
                            'EQUAL' if core_raw else 'DIFFERENT', core_diff[:20] or 'NONE'),
          '### INTERFACES: files and exits %s ; prints %d ; against AXIOM_PRINTS_INTERFACES.txt at main (its %d print lines) line by line: '
          'lines differing %s' % (exits, len(if_r), len(if_b), if_diff[:20] or 'NONE'),
          '### error lines in the build logs: %d' % len(errs)] + ['    %s:%d:%d: %s' % e for e in errs[:30]] + [
          '### prints not at the standard three or none: %s' % (off[:20] or 'NONE'), '',
          '### the Interfaces prints, whole:'] + ['    ' + l for l in ifp.rstrip(NL).split(NL)] + ['',
          '### ### **RUN %s ; CONCLUSION %s ; ARTIFACT SHA256 %s ; MEMORY LOW %s MB (HOLD 2560) ; CORE MODULES %d, FAILURES %s ; TERMINALS %d (CORE %d, '
          'INTERFACES %d), AT THE STANDARD THREE OR NONE %d ; AGAINST THE BANKED PRINTS: CORE %s, INTERFACES %s ; ERROR LINES %d ; GATE %s.**' % (
              R['run_id'], run.get('conclusion'), (row['artifact_sha256'] or '### NONE')[:16], row['mem_low'], len(order), cfail or '?', len(P),
              len(_prints(allp)), len(if_r), len(P) - len(off), 'EQUAL' if core_raw and not core_diff else 'DIFFERENT',
              'EQUAL' if not if_diff and if_r else 'DIFFERENT', len(errs), row['gate'])]
    put_txt('b655_runner_%s.txt' % kern, L)
    j = jl('b655_runner_rows.json') or {'rows': []}
    j['rows'] = [r for r in j['rows'] if r['kernel'] != kern] + [row]
    put_json('b655_runner_rows.json', j)
    print(L[-1])


def runner_merged(*a):
    """`runner_merged <merge sha> <tag>`: the row's merge and tag, after main and the tag are read back at the remote."""
    sha, tag = a[:2]
    j = jl('b655_runner_rows.json')
    for r in j['rows']:
        if r['kernel'] == K.KERNEL:
            r['merged'], r['tag'] = sha, tag
    put_json('b655_runner_rows.json', j)
    print('  %s merged %s tag %s' % (K.KERNEL, sha, tag))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R265)(1), (4)
WH = ('*Appended 2026-10-12 by b655 to b654’s entry (:8313), under `(R265)`(1) -- b654 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b654_closing.txt):*')
EH = ('*Appended 2026-10-12 by b655 beneath W-ORD-EDIT-ROUTE-ARM (:13661), under `(R265)`(4) -- THE EDIT ROUTE EXTENDED TO EVERY FILE THE SEAT '
      'WRITES, STANDING FROM b655; G-EDIT-ROUTE REPAIRED:*')


def _weight():
    return ('\n' + WH + ' E1 -- rest_norm_le_rate and zeroSide_neg_at_rate, the zero side negative at every j ≥ D where the rate bound falls '
            'beneath the tie terms’ sum, every hypothesis fixed in the statement from b559’s lines -- DERIVES at the standard three on the runner '
            '(run 38259645524, memory low 12,699 MB), merged alone into SIDE-explicit-formula at 111e418, tag v0.27; transversalityWidth bound to the '
            'vendored LiCriterion.riemannXi, no theorem beside it; the AxiomCheck print re-banked and its row VERIFIED, G-AXIOM-CLAIM at one '
            'contradiction (SIDE-cosmo); the workflow file on SIDE-explicit-formula’s main at 7317db4 under `(R263)`(4); the alternation at '
            'OPEN_TRAILS :13944 and the freeze at :13946; relay 22ce9a8d, PLACE-papers 8e81846, FINDINGS :8311 and :8313, the root 4ada7117…; the '
            'suite 75 of 77, G-AXIOM-CLAIM and G-EDIT-ROUTE declared. Five defects (relay data/b654_defects.txt): (b) the navigator’s N5 omission, '
            '(e) after the trail record. The seat’s sed -i on its memory index after the close, outside every tree, entered at b655’s step zero as a '
            'dated line (relay data/b655_defects.txt). Nothing deposited.\n')


def _edit_route_rule():
    return ('\n' + EH + ' from b655 the edit-route rule covers every file the seat writes, the seat’s memory files included: an edit goes through '
            'the Edit tool, not sed -i and not a heredoc; a new file through the Write tool. G-EDIT-ROUTE`s parser read a delete command’s redirect '
            'and its target as branch names and failed on b654’s two remote deletes (relay data/b654_defects.txt (d)); under the freeze’s exception '
            '(the arm failing on real state, the failure printed) it now takes a branch deletion’s redirects out before reading its names, a glob '
            'or a variable still failing, its planted test before 25 of 28 and after 28 of 28 (relay data/b655_edit_route.txt).\n')


def c1(*a):
    items = [('FINDINGS.md', WH, _weight()), ('OPEN_TRAILS.md', EH, _edit_route_rule())]
    land(items, 'b655_record_lines.json', 'c1', entry=8313,
         check=[('FINDINGS.md', 8313, '## E1, the configuration-relative rate'), ('OPEN_TRAILS.md', 13661, 'W-ORD-EDIT-ROUTE-ARM ENTERED AND ACTED')],
         dry='dry' in a)


def _er_at(spec):
    """edit_route.py at a revision, loaded from its blob as a module of its own name in a scratch directory; the test run against it."""
    import importlib.util
    import tempfile
    d = tempfile.mkdtemp(prefix='b655_er_')
    b = subprocess.run(['git', '-C', ROOT, 'show', spec], capture_output=True).stdout
    open(os.path.join(d, 'edit_route.py'), 'wb').write(b)
    sp = importlib.util.spec_from_file_location('edit_route_at', os.path.join(d, 'edit_route.py'))
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m, d


def edit_route(*a):
    """(R265)(4): G-EDIT-ROUTE`s parser before and after its repair -- the planted test run against the pre-repair blob (relay HEAD before the
    repair commit) and against the repaired file; b654`s capture (relay data/b654_commands.json) scanned by both. Banked as data/b655_edit_route.txt."""
    import shutil
    pre = a[0] if a else K.PRE_RELAY
    old, d = _er_at('%s:tools/edit_route.py' % pre)
    import edit_route as NEW
    rows = json.load(io.open(os.path.join(D, 'b654_commands.json'), encoding='utf-8'))['rows']
    out = {}
    for name, mod in (('before', old), ('after', NEW)):
        shutil.copy(os.path.join(T, 'test_edit_route_b646.py'), os.path.join(d, 'test_edit_route_b646.py'))
        if name == 'after':
            shutil.copy(os.path.join(T, 'edit_route.py'), os.path.join(d, 'edit_route.py'))
        r = subprocess.run([sys.executable, os.path.join(d, 'test_edit_route_b646.py')], capture_output=True, text=True, encoding='utf-8',
                           errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
        cases = [l for l in (r.stdout or '').split(NL) if re.match(r'^  \(\d+\) ', l)]
        fails = [re.match(r'^  (\(\d+\))', c).group(1) for c in cases if not c.rstrip().endswith('PASS')]
        hits = mod.scan(rows)
        out[name] = dict(rc=r.returncode, cases=len(cases), failing=fails, b654_offences=[h[0]['n'] for h in hits], last=(r.stdout or '').strip().split(NL)[-1])
    L = ['b655 -- COMPONENT 1, (R265)(4): G-EDIT-ROUTE`S PARSER REPAIRED ON A PLANTED REDIRECT CASE, RUN BEFORE AND AFTER (%s)' % utc(), '',
         '### the defect: tools/edit_route.py read every word after the remote of `git push <remote> --delete` as a branch name, a redirect and its',
         '### target among them, so b654`s two deletes (relay data/b654_commands.txt #22, #23; data/b654_defects.txt (d)) read as deletions without',
         '### an explicit name. The repair (the Edit tool): _drop_redirects takes a redirect operator and its target, or a redirect glued to its',
         '### target, out of a branch deletion`s words before the names are read; a glob or a variable stays a name and still fails.',
         '### the planted test, tools/test_edit_route_b646.py, gains three cases: the planted glob delete carrying a redirect (15) and b654`s two',
         '### commands as house forms (26), (27); rows are the test`s numbered cases.', '',
         '### BEFORE (edit_route.py at relay %s, the test as edited): cases %d ; failing %s ; exit %d ; %s' % (
             pre, out['before']['cases'], out['before']['failing'] or 'none', out['before']['rc'], out['before']['last']),
         '###   b654`s capture scanned: offending rows %s' % (out['before']['b654_offences'] or 'none'),
         '### AFTER (edit_route.py repaired): cases %d ; failing %s ; exit %d ; %s' % (
             out['after']['cases'], out['after']['failing'] or 'none', out['after']['rc'], out['after']['last']),
         '###   b654`s capture scanned: offending rows %s' % (out['after']['b654_offences'] or 'none'), '',
         '### ### **BEFORE %d OF %d PASSING, b654`S OFFENCES %d ; AFTER %d OF %d PASSING, b654`S OFFENCES %d.**' % (
             out['before']['cases'] - len(out['before']['failing']), out['before']['cases'], len(out['before']['b654_offences']),
             out['after']['cases'] - len(out['after']['failing']), out['after']['cases'], len(out['after']['b654_offences']))]
    put_txt('b655_edit_route.txt', L)
    put_json('b655_edit_route.json', dict(at=utc(), pre=pre, **out))
    print(NL.join(L[-6:]))


# ================================================================================ THE LATE ROUTES (b654's, carried; every row read through READERS)
import collections                 # noqa: E402
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


def _session_rows():
    """the session's lines from the first user line carrying this act's anchor."""
    start = None
    for i, raw in enumerate(io.open(SESSION, encoding='utf-8', errors='replace'), 1):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if start is None and K.ANCHOR in raw and o.get('type') == 'user' and not o.get('isCompactSummary'):
            start = i
        if start is not None:
            yield i, o, start


def answers(*a):
    """data/b655_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
    delivered between BEGIN and END after the ruling (user lines and queued commands), and the author's plain messages, verbatim."""
    calls, results, words, plain, start = [], {}, [], [], None
    for i, o, st in _session_rows():
        start = st
        m = o.get('message') or {}
        cs = m.get('content')
        att = o.get('attachment') or {}
        texts = []
        if att.get('type') == 'queued_command' and isinstance(att.get('prompt'), str):
            texts = [att['prompt']]
        elif o.get('type') == 'user' and not o.get('isCompactSummary'):
            texts = [cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']
            for t in texts:
                if t and not t.lstrip().startswith(('<', 'BEGIN', 'RULING')) and len(t) < 400 and i > st:
                    plain.append((i, t.strip()))
        for t in texts:
            for mm in re.finditer(r'(?ms)^BEGIN\s*\n(.*?)\nEND\s*$', t or ''):
                if K.ANCHOR not in mm.group(1):
                    words.append((i, mm.group(1)))
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((i, c['id'], c['input'], o.get('timestamp')))
            if isinstance(c, dict) and c.get('type') == 'tool_result':
                t = c.get('content')
                results[c.get('tool_use_id')] = (i, ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t, o.get('timestamp'))
    if start is None:
        sys.exit('### THE ANCHOR IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    L, n = [], 0
    for i, cid, inp, ts in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %d, %s)' % (cid, K.SESSION_ID, i, ts))
        for k, q in enumerate(inp.get('questions', []), 1):
            n += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT', None))
        L += ['RESULT (transcript line %s, %s): %s' % (r[0], r[2], r[1]), '']
    W, seen = [], set()
    for i, w in words:
        if w in seen:
            continue
        seen.add(w)
        W += ['### THE AUTHOR`S WORD (transcript line %d), BEGIN to END, verbatim:' % i] + w.replace('\r', '').split(NL) + ['']
    for i, t in plain:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %d), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b655 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b655_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b655_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call (the hosted runner's)."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    L = ['b655 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d.**' % (len(rows), len(hits), len(lean))]
    put_txt('b655_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b655_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])


def kernels(*a):
    import b641_record as R41
    put_json('b655_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


def _defect_short():
    return [re.match(r'^\(([a-z])\) ([^.]*)\.', l.strip()).group(0)[:-1].lower() for l in rdn('b655_defects.txt').split(NL)
            if re.match(r'^    \([a-z]\) [^.]*\.', l)]


def defects(*a):
    t = rdn('b655_defects.txt')
    ds = [l.strip() for l in t.split(NL) if re.match(r'^    \([a-z]\) ', l)]
    put_json('b655_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b655_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b655_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|mirror.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b655_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b655_seal_hashes.json' in banks, crlf or 'none'))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b655'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import shutil
    import tempfile
    import act_root as AR
    J = jl('b655_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    tmp = tempfile.mkdtemp()
    cp = os.path.join(tmp, os.path.basename(bank_))
    shutil.copy(os.path.join(ROOT, *bank_.split('/')), cp)
    b = bytearray(open(cp, 'rb').read())
    b[0] ^= 0x01
    open(cp, 'wb').write(bytes(b))
    items2 = [('%s %s' % (bank_, AR.sha256_file(cp)) if it.split()[0] == bank_ else it) for it in J['items']]
    r2 = AR.root_of(items2, J['previous'])
    same = AR.root_of(J['items'], J['previous'])
    late = []
    for it in J['items']:
        p = it.split()
        if p[0].startswith('data/'):
            fp = os.path.join(ROOT, *p[0].split('/'))
            if not os.path.exists(fp) or AR.sha256_file(fp) != p[1]:
                late.append('%s changed' % p[0])
            elif os.path.getmtime(fp) > J.get('at_epoch', 0) + AR.ORDER_SLACK:
                late.append('%s written after the root' % p[0])
    L = ['b655 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b655_root_arm.txt', L)
    put_json('b655_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_final(*a):
    before = _rows_state(json.loads(_show(RELAY, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b655 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b655_table_final.txt', L)
    put_json('b655_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b654_closing_push_out.txt')
N5_RELAY_TOOLS = K.EDITED_SHARED
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')


def TRAIL_HEAD():
    return ('### b655 — lane three, act eighty-two, the re-cut act under (R265): b654 at its weight; SIDE-global-section’s sentences graded, cut, '
            'built on the runner and merged; G-EDIT-ROUTE repaired; the edit route extended; the mirror export')


def _runner_rows():
    return [read_runner_row(r) for r in (jl('b655_runner_rows.json').get('rows') or [])]


def _ct(repo, *a):
    s = g(repo, 'log', '-1', '--format=%ct', *a).strip()
    return int(s) if s.isdigit() else None


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime((s or '')[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None


def _n2():
    """N2: every graded row's quoted words a verbatim substring of its parent's LICENSED cell; no kernel byte written before the author's word."""
    G = jl(K.GRADES)
    par = dict((k, q) for k, _p, q, _rs in blocks())
    bad, n = [], 0
    for k, rows in G['grades'].items():
        for x in rows:
            _k, nn, w = read_grade_row(k, x)
            n += 1
            if w not in par[int(k)]['licensed']:
                bad.append('#%s s%s' % (k, nn))
    aj = jl('b655_author_answers.json').get('calls') or []
    ans = _iso(aj[0]['result_ts']) if aj and aj[0].get('result_ts') else None
    first_k = g(K.KD, 'log', '--reverse', '--format=%ct %h', K.K_MAIN + '..main').split(NL)[0].split()
    t_k = int(first_k[0]) if first_k else None
    ok = not bad and n > 0 and ans and t_k and ans < t_k
    return ('HELD' if ok else 'REFUTED'), (
        'graded rows %d, each quoting its parent`s LICENSED cell verbatim: %s; the author`s answer at %s, the first kernel byte (SIDE-global-section '
        '%s) at %s -- the answer first %s' % (n, 'ALL' if not bad else 'NOT %s' % bad, time.strftime('%H:%M:%SZ', time.gmtime(ans)) if ans else '?',
                                               first_k[1] if len(first_k) > 1 else '?', time.strftime('%H:%M:%SZ', time.gmtime(t_k)) if t_k else '?',
                                               bool(ans and t_k and ans < t_k)))


def _n4():
    """N4: G-EDIT-ROUTE at HEAD passes on b654's two deletes and fails on its planted redirect case."""
    rows = json.load(io.open(os.path.join(D, 'b654_commands.json'), encoding='utf-8'))['rows']
    b654 = ER.scan([r for r in rows if r['n'] in (22, 23)])
    planted = ER.offences("git -C /d/SIDE-x push origin --delete 'push-b99*' > /d/relay/data/b999_delete.txt 2>&1")
    ej = jl('b655_edit_route.json')
    ok = (len([r for r in rows if r['n'] in (22, 23)]) == 2 and not b654 and bool(planted) and ej.get('after', {}).get('failing') == []
          and ej.get('after', {}).get('cases') == 28)
    return ('HELD' if ok else 'REFUTED'), (
        'b654`s two deletes (#22, #23) read at HEAD: offences %d; the planted redirect glob delete read: %s; the test after the repair %s of %s, '
        'failing %s (relay data/b655_edit_route.txt)' % (len(b654), [k for k, _ in planted] or 'NONE', ej.get('after', {}).get('cases', 0) -
                                                         len(ej.get('after', {}).get('failing') or []), ej.get('after', {}).get('cases'),
                                                         ej.get('after', {}).get('failing')))


def _n5():
    face = jl('b655_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b655_|audit_b655_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('tools/') and x[6:] in N5_RELAY_TOOLS) or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    km = [l for l in g(K.KD, 'log', '--first-parent', '--format=%h %p', K.K_MAIN + '..main').split(NL) if l.strip()]
    km_ok = (len(km) == 2 and g(K.KD, 'show', '--name-only', '--format=', K.K_WORKFLOW).split() == ['.github/workflows/build-module.yml']
             and len(km[0].split()) == 3)
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b655_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    ok = kern_ok and not pp_beyond and not kinds_beyond and not differ and km_ok and not new_arms
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unsubmitted); SIDE-global-section`s main written by the workflow file under '
            '`(R263)`(4) and the one merge under Component 3 alone (first-parent commits since %s: %s ; %s); every kernel as the face read it %s; '
            'standing arms added: %s (the act`s arms over its own banks %d); sealed tools not agreeing %s; PLACE-papers beyond FINDINGS and '
            'OPEN_TRAILS: %s; relay files of a kind beyond the banks, the tools, the edit-route repair and its test and the root list: %s; no '
            'identifier of the author in any outbound request (git pushes, remote reads, the runner`s dispatch with a ref and a target, the '
            'artifact`s download, the mathlib pin`s resolution)' % (
                K.DRAFT, K.K_MAIN, [l.split()[0] for l in km], 'AS RULED' if km_ok else '### OTHERWISE', kern_ok, new_arms or 'NONE',
                len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE'))


def scores(*a):
    TF, RA = jl('b655_table_final.json'), jl('b655_root_arm.json')
    _r, _n, sh = seal_hashes()
    cm = jl('b655_commands.json')
    cb = jl('b655_cut_SIDE-global-section.json')
    rr = dict((r['kernel'], r) for r in jl('b655_runner_rows.json').get('rows') or [])
    gs = rr.get(K.KERNEL) or {}
    a_ = cb.get('after') or {}
    S = {
        'N1': (('HELD' if cm and not cm.get('local_lean') else 'REFUTED'),
               'commands of this act that run lean or lake on this host: %s (relay data/b655_commands.txt); the build on the hosted runner alone' % (
                   cm.get('local_lean') if cm else '### UNREAD')),
        'N2': _n2(),
        'N3': (('HELD' if cb and not cb.get('standing') and not a_.get('OVERREACHES (STANDING)') and not a_.get('UNLICENSED (STANDING)')
                and not cb.get('faults') and gs.get('gate') == 'DERIVES' and gs.get('merged') else 'REFUTED'),
               'the grade bank re-run at the branch: %s, standing %d (UNRESOLVED blocks none); every file`s comment-stripped code equal to main`s, '
               'faults %s; the gate %s, merged %s tag %s (relay data/b655_cut_SIDE-global-section.txt)' % (
                   a_, len(cb.get('standing') or []), cb.get('faults') or 'NONE', gs.get('gate'), gs.get('merged'), gs.get('tag'))),
        'N4': _n4(),
        'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    put_json('b655_scores.json', dict((k2, list(v)) for k2, v in S.items()))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:500]))


NEXT_LINE = ('b656, per `(R265)`(7), a research act, the author’s word pending: the rate inequality of E1 evaluated at the Q0 configuration '
             '(disc −23, the b548/b549 bench) in certified arithmetic, hypotheses fixed in that ruling before any number')


def _title():
    cb = jl('b655_cut_SIDE-global-section.json')
    rr = dict((r['kernel'], r) for r in jl('b655_runner_rows.json').get('rows') or []).get(K.KERNEL) or {}
    return ('## SIDE-global-section’s docstrings at %d sentence rows cut of %d, built on the runner and merged at %s; G-EDIT-ROUTE repaired; the '
            'edit route extended' % ((cb.get('after') or {}).get('CUT', 0), _grade_rows_total(), rr.get('tag') or '### UNMERGED'))


def _grade_rows_total():
    m = re.search(r'SENTENCE ROWS (\d+)', rdn('b655_sentence_grades.txt'))
    return int(m.group(1)) if m else 0


def _finding_text():
    S, rl, J = jl('b655_scores.json'), jl('b655_record_lines.json'), jl('b655_act_root.json')
    ans = rdn('b655_author_answers.txt')
    n_ans, n_w = len(re.findall(r'^### PROMPT ', ans, re.M)), len(re.findall(r'^### THE AUTHOR`S WORD ', ans, re.M))
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    sc = lambda k: read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else '?'   # noqa: E731
    rr = dict((r['kernel'], r) for r in jl('b655_runner_rows.json').get('rows') or []).get(K.KERNEL) or {}
    cb = jl('b655_cut_SIDE-global-section.json')
    ej = jl('b655_edit_route.json')
    mj = jl('b655_mirror.json')
    e = ['', _title(), '',
         '*Filed at b655 on the author’s ruling `(R265)` and the author’s answers (%d prompts, %d words). Banks: relay `data/b655_sentence_grades.txt`, '
         '`data/b655_cut_SIDE-global-section.txt`, `data/b655_runner_SIDE-global-section.txt`, `data/b655_edit_route.txt`, '
         '`data/b655_plain_comments.txt`, `data/b655_act_root.txt`.*' % (n_ans, n_w), '',
         '**The kernel** (`(R265)`(2)): SIDE-global-section, 43 OVERREACHES in relay `data/b647_table_kernels.txt` :12, the next by descending count '
         'after SIDE-kernel; its 51 graded blocks read into %d sentence rows by the b651 route and graded by hand by the b652 rule, each grade citing '
         'its parent’s LICENSED words verbatim; one elided ACTION completed from its LICENSED words; on the author’s word one four-bullet sentence '
         'read as its bullet rows and one conclusion sentence kept after its surviving premise; no plain comment asserting the unsupported claim '
         '(the needle and a wider shape, 138 comments). N2 %s.' % (_grade_rows_total(), sc('N2')), '',
         '**The cut and the runner** (`(R265)`(3)): %d graded rows cut by the mechanical rule in %d commits, one per file, each file’s comment-stripped '
         'code equal to main’s, the grade bank at the branch reading none standing; the workflow written on the kernel’s main in its own build path '
         '(no lakefile: Core module by module with plain lean in the recorded order, then AllPrints; the Interfaces files against mathlib4 at the '
         'declared pin), one dispatch, run %s, memory low %s MB, the artifact’s sha256 agreeing with the platform’s digest, every print at the '
         'standard three or none and equal to the banked profiles; merged alone, SIDE-global-section %s tagged %s. N3 %s.' % (
             (cb.get('after') or {}).get('CUT', 0), len(cb.get('commits') or []), rr.get('run_id'), rr.get('mem_low'), rr.get('merged'), rr.get('tag'),
             sc('N3')), '',
         '**The edit route** (`(R265)`(4)): G-EDIT-ROUTE’s parser takes a branch deletion’s redirects out before reading its names; its planted test '
         '%d of %d before and %d of %d after; b654’s two deletes now read clean and a glob delete carrying a redirect still fails. The rule covers '
         'every file the seat writes from here (OPEN_TRAILS :%s). N4 %s.' % (
             (ej.get('before') or {}).get('cases', 0) - len((ej.get('before') or {}).get('failing') or []), (ej.get('before') or {}).get('cases', 0),
             (ej.get('after') or {}).get('cases', 0) - len((ej.get('after') or {}).get('failing') or []), (ej.get('after') or {}).get('cases', 0),
             ls[1].get('line'), sc('N4')), '',
         '**The record lines** (`(R265)`(1)): b654 at its weight (FINDINGS :%s).' % ls[0].get('line'), '',
         '**The root.** b655 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this cut re-reads b647’s block table for SIDE-global-section (relay '
         '`data/b647_table_SIDE-global-section.txt`), b651’s sentence route and b652’s grading rule, as b652 and b653 did for SIDE-kernel; it is '
         're-read by the next re-cut act on SIDE-lv-conservation (35 OVERREACHES, :17). It strengthens the programme’s offering of statements a '
         'reader can check: SIDE-global-section’s headers and docstrings now say what its decided terminals carry, and its build runs on a machine '
         'the reader can name by run id, its prints equal to the banked profiles.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; a docstring cut says less, not more, and a gate reading compares a '
         'print with the standard three and confers nothing beyond it.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the needle for plain comments and its wider shape are the seat`s, b650 naming no tool; (2) the mechanical rule replaces a '
              'whole graded sentence, so a lead clause sharing its sentence leaves with it (#1, #6, #47), as the bank printed before the strike; '
              '(3) the workflow`s Core order is b314`s two passes, the AllPrints closure then the rest; (4) the mirror export is built after the '
              'act`s last PLACE-papers push and before the closing, as b652 built it, so the closing prints its MANIFEST')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b655_scores.json', 'b655_findings.json', 'b655_record_lines.json', 'b655_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b655_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R265) ratified.** (1) b654 at its weight. (2) The kernel: SIDE-global-section, its sentences graded by hand. (3) The cut, the '
             'runner, the merge. (4) G-EDIT-ROUTE repaired; the edit route extended to every file the seat writes. (5) The mirror export. (6) The '
             'draft held at v5. (7) The act after: b656.', '',
             '**Entered:** FINDINGS.md:%s (b654’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the edit route extended); this record.' % (
                 ls[0].get('line'), fj.get('entry_line'), ls[1].get('line')), '',
             '**Act root:** b655 `%s` (previous `%s`, b654’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b655_author_answers.txt, with the author’s words), none after the root.' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b655_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none of the act’s own beyond the carried line'), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b655_scores.json')
    L = ['=' * 104, 'b655 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b655_defects.txt').rstrip(NL).split(NL)
    put_txt('b655_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b655_scores.json', 'b655_findings.json', 'b655_trail.json', 'b655_record_lines.json', 'b655_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    L = ['b655 -- THE COMPONENTS, BANKED UNDER (R265).', '',
         '### COMPONENT 0 : step zero (data/b655_ferry.txt, data/b655_stepzero.txt, data/b655_tests_stepzero.txt, data/b655_defects.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : b654`s weight FINDINGS :%s ; the edit route extended OPEN_TRAILS :%s ; G-EDIT-ROUTE repaired (data/b655_edit_route.txt) ; N4 %s' % (
             ls[0].get('line'), ls[1].get('line'), S['N4'][0]),
         '### COMPONENT 2 : the grades (data/b655_table_SIDE-global-section_sentences.txt, data/b655_plain_comments.txt, data/b655_sentence_grades.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the cut and the runner (data/b655_cut_SIDE-global-section.txt, data/b655_runner_SIDE-global-section.txt) ; N3 %s' % S['N3'][0],
         '### COMPONENT 4 : the seal (data/b655_seal_hashes.json) ; S3 %s' % S['S3'][0],
         '### COMPONENT 5 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % ((J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'),
                                                                                        S['N1'][0], S['N5'][0])]
    put_txt('b655_components.txt', L)
    print(NL.join(L[2:]))


def _land_one(path, head, e, bank, extra):
    if odd_lines(e):
        sys.exit('### ODD BACKTICKS -- NOTHING WRITTEN: %s' % odd_lines(e)[:3])
    guard_absent(path, head)
    r = append_to(path, e)
    ln = read_head(path, head)
    put_json(bank, dict(extra, line=ln, head=head, append=r))
    return ln


def findings(*a):
    t, e = _finding_text()
    e = conv(e)
    dry = 'dry' in a
    cells, fired = screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells)
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, 'b655_findings.json', dict(title=t))
    j = jl('b655_findings.json')
    j['entry_line'] = ln
    put_json('b655_findings.json', j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = conv(_trail_text())
    dry = 'dry' in a
    cells, fired = screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells)
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b655_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


# ================================================================================ THE MIRROR, AT THE CLOSE ((R265)(5); b652's routes, carried)
# ### after the act's last PLACE-papers push and before the closing record: the unedited builder (-DateTag only) on the standing roster, the
# ### roots file's last line (b655's root) added to MANIFEST in the stage, verified from PLACE-papers by mirror_verify.py, banked; the closing
# ### prints its MANIFEST md5 and last commit. Its banks are written after the root and are not named by it.
import hashlib as _hl   # noqa: E402

MIRROR_TAG = '2026-10-12-b655'
ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % MIRROR_TAG
STAGE = os.path.join(os.environ.get('TEMP', SP), 'mirror-build-%s' % MIRROR_TAG)


def mbuild(*a):
    if os.path.exists(ZIP) or os.path.exists(STAGE):
        sys.exit('### THE ZIP OR ITS STAGE EXISTS -- NOT STARTED')
    loc, rem = g(PP, 'rev-parse', 'HEAD').strip(), (g(PP, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    if loc != rem:
        sys.exit('### PLACE-papers HEAD %s IS NOT THE REMOTE MAIN %s -- NOT STARTED' % (loc[:12], rem[:12]))
    t0 = time.time()
    r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', os.path.join(ROOT, 'tools', 'mirror_build.ps1'), '-DateTag',
                        MIRROR_TAG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_json('b655_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b655':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b655`s -- NOTHING WRITTEN' % last[0])
    line = 'Act root: %s %s' % (last[0], last[1])
    man_p = os.path.join(STAGE, 'MANIFEST.md')
    raw = open(man_p, 'rb').read()
    if b'Act root: ' in raw:
        sys.exit('### THE ROOT LINE IS IN THE STAGED MANIFEST ALREADY -- REFUSING TO WRITE IT TWICE')
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    sep = '\r\n' if '\r\n' in text else '\n'
    out = text.rstrip('\r\n') + sep + sep + line + sep
    before = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    open(man_p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    ps = subprocess.run(['powershell', '-NoProfile', '-Command', "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)],
                        capture_output=True, text=True)
    after = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    put_json('b655_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b655_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
    print(r.stdout[-600:])


def mbank(*a):
    import zipfile
    import b616_record as R6
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    ls = man.decode('utf-8-sig').replace(chr(13), '').split(NL)
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    commits = sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', NL.join(l for l in ls if '|' in l))))
    zb = open(ZIP, 'rb').read()
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b655_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b655 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b655_mirror.txt', L)
    put_json('b655_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:8]:
        print(l[:240])


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith('_'):
        print('usage: b655_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
