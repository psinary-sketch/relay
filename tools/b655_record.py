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


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith('_'):
        print('usage: b655_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
