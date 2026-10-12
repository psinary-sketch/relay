# -*- coding: utf-8 -*-
"""b657_record.py -- THE ACT'S RECORD TOOL, b657 under (R267).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b657's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows (tools/b657_regspec.py) can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b656_record.py (the landing, the answers, the capture, the kernels' face, the defects, the seal hashes,
### the root and its arm, the table, the scores' form, the record, the desk, the components, the mirror) and from b655_record.py (the sentence
### rows, the plain comments, the grades, the cut planned on the blobs, the cut bank, the runner); new here: (R267)(2)'s dry run of the entry
### and the trail record through their screens with the face's needles (`drycheck`, run by tools/b657_reg_gate.py before the lock, stand-ins
### for the banks not yet written), and (R267)(3)'s h2 row -- a graded row may take its cell, verdict and ACTION from b648's named row, and a
### block's graded row may carry its own span of the block's ACTION.
### Routes: `python tools/b657_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
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
import b657_worklist as K          # noqa: E402

STANDIN = bool(os.environ.get('B657_STANDIN'))


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(path):
    return io.open(path, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(path) else ''


def rdn(name):
    return rd(os.path.join(D, name))


def put_json(name, obj):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def _standins():
    """(R267)(2): the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in, none a number
    any bank carries; a stand-in run writes no bank."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b657_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b657_findings.json': dict(entry_line=99999, title='stand-in'),
        'b657_trail.json': dict(line=99999),
        'b657_act_root.json': dict(root='0' * 64, previous='4cc2bd5e' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
        'b657_runner_rows.json': dict(rows=[dict(kernel=K.KERNEL, branch=K.CUT_BRANCH, ref='0' * 40, target='SIDELvConservation', run_id=1,
                                                 conclusion='success', artifact_sha256='0' * 64, mem_low=9999, stopped=False, gate='DERIVES',
                                                 merged='0000000', tag=K.NEXT_TAG)]),
        'b657_cut_SIDE-lv-conservation.json': dict(after=dict(CUT=1), commits=['0000000'], faults=[], standing=[]),
        'b657_mirror.json': dict(zip='stand-in', manifest_md5='0' * 32),
    }


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return _standins().get(name, {}) if STANDIN else {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def _ws(s):
    return ' '.join(s.split())


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b657's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b657_scanfile_%s.md' % tag)
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
    """a row of data/b657_runner_rows.json -- every key of RUNNER_KEYS present (None where a step did not reach it); returns the row's reading
    (kernel, outcome, merged); raises KeyError on a row of another shape."""
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
    """a scores row: key N1..N5 or S1..S5, value [verdict, text]; returns (key, the whole verdict, text) -- the whole verdict, not its first
    word (b656's defect (e))."""
    if not re.match(r'^[NS][1-5]$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


def read_grade_row(k, row):
    """a row of the hand grades (data/b657_sentence_grades.json): block number k and [sentence number, the cell's quoted words];
    returns (k, n, words); raises on a row of another shape."""
    n, w = row
    ok_n = (isinstance(n, int) and n >= 1) or (isinstance(n, str) and re.match(r'^\d+(\.\d+)?$', n) is not None)
    if not ok_n or not isinstance(w, str) or not w.strip() or not str(k).isdigit():
        raise ValueError('grade row of another shape: %r' % (row,))
    return int(k), str(n), w


READERS = ('read_runner_row', 'read_score_row', 'read_head', 'read_grade_row')


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R267)(1), (2)
WH = ('*Appended 2026-10-12 by b657 to b656’s entry (:8361), under `(R267)`(1) -- b656 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b656_closing.txt):*')
DH = ('*Appended 2026-10-12 by b657 beneath the b656 record (:14000), under `(R267)`(2) -- THE ENTRY-AND-TRAIL DRY RUN A STEP OF THE '
      'REGISTRATION GATE, STANDING FROM b657:*')


def _weight():
    return ('\n' + WH + ' stopped at Component 2 on the author’s word, its finding the binding bank (relay data/b656_e1_binding.txt, 19 quantity '
            'rows) -- O-1 E1 stated at zetaZeroConfig alone (RateIndex.lean :27, :113), its carrier ζ’s nontrivial zeros by rfl (SeamClosed.lean '
            ':42, :44); O-2 no rate theorem over a general configuration (Converse.lean :161 the limit form alone); O-3 A₀ existential '
            '(LocalCount.lean :287); every quantity binding at the cell’s own configuration and the implication not; W-ORD-E1-CFG at OPEN_TRAILS '
            ':13994 for b658; the `(R265)`(7) correction at :13990, the grid lesson at :13998 as the navigator’s; N3, N4 and H1–H3 NOT SCORED, '
            'O-2 the reason; relay 63001a6b, PLACE-papers 31c03f9, FINDINGS :8359 and :8361, the root 4cc2bd5e…; the suite 75 of 76, the '
            'SIDE-cosmo row declared; eight defects (relay data/b656_defects.txt), (e)–(h) after the seal, (e) and (f) from an entry and a trail '
            'record not dry-run before it; the mirror at mirror-refresh-2026-10-12-b656.zip (MANIFEST md5 16af3ad8…). Nothing deposited.\n')


def _dry_step():
    return ('\n' + DH + ' from b657 the registration gate’s run before the lock carries the FINDINGS entry and the trail record dry-run '
            'through their guards (the screens their landing runs) with the needles the face names, CLEAN printed, before the lock is taken; '
            'a seal taken without it is a seal-order failure. b647’s lesson made mechanical after b656’s defects (e) and (f); no new arm -- a '
            'step in the gate (tools/b657_reg_gate.py, the record tool’s drycheck route, stand-ins for the banks not yet written).\n')


def c1(*a):
    items = [('FINDINGS.md', WH, _weight()), ('OPEN_TRAILS.md', DH, _dry_step())]
    land(items, 'b657_record_lines.json', 'c1', entry=8361,
         check=[('FINDINGS.md', 8361, '## E1’s quantities bound to the kernel at v0.27'),
                ('OPEN_TRAILS.md', 14000, '### b656 — lane two, act eighty-three')],
         dry='dry' in a)


# ================================================================================ COMPONENT 2: THE SENTENCE ROWS, THE PLAIN COMMENTS, THE GRADES
def _bank_line(bank_lines, rid_tail):
    for i, l in enumerate(bank_lines, 1):
        if l.startswith('  %s@%s:%s |' % (K.KERNEL, K.B647_REV, rid_tail)):
            return i
    return None


def sentences(*a):
    """(R267)(3), the b651 route as b655 ran it: the kernel's OVERREACHES, UNDERSTATES and UNLICENSED blocks of b647's bank (read at 2f71068)
    read into sentence rows at the kernel's main (b4c55b9); a block whose text is not found at main is listed, not read;
    data/b657_table_<kernel>_sentences.txt and .json."""
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
                             hand_needed=r.get('hand_needed'), at_main=src))
    gc = collections.Counter(x['generated'] for x in rows)
    main = g(K.KD, 'rev-parse', '--short=7', 'main').strip()
    L = ['b657 -- COMPONENT 2, (R267)(3): %s`S OVERREACHES, UNDERSTATES AND UNLICENSED BLOCKS READ INTO SENTENCE ROWS (%s)' % (K.KERNEL, utc()), '',
         '### rows are sentences, parents are blocks. The parents: relay data/%s, its OVERREACHES, UNDERSTATES and UNLICENSED rows (%d), read at %s; '
         'the generator: b647_record._kdoc_rows at %s main %s, each block`s context captured and each unit read by licensed_table.docstring_row; the '
         'unit: b647_record._MSPLIT (a sentence split where . ! or ? meets whitespace) -- the b651 route. A GENERATED reading per sentence; the HAND '
         'reading per sentence is the grade bank`s.' % (K.PARENTS, len(parents), K.B647_REV, K.KERNEL, main),
         '### parents read %d ; parents not found at main %d (%s)' % (len(parents) - len(unread), len(unread),
                                                                       '; '.join('%s (%s)' % (u['source'], u['decl'] or u['kind']) for u in unread) or 'none'), '']
    cur = None
    for x in rows:
        if x['parent'] != cur:
            cur = x['parent']
            L += ['', '== %s (%s ; b647`s bank line :%s ; at main %s ; HAND %s ; %d sentences)' % (
                x['parent'].split(':', 1)[1], x['kind'], x['parent_line'], x['at_main'], x['parent_verdict'], x['of'])]
        L.append('  s%d %-11s %s' % (x['n'], x['generated'], x['sentence'][:600]))
    L += ['', '### ### **PARENT BLOCKS %d ; NOT FOUND AT MAIN %d ; SENTENCE ROWS %d ; GENERATED: %s ; HAND PER SENTENCE: the grade bank`s.**' % (
        len(parents) - len(unread), len(unread), len(rows), ', '.join('%s %d' % kv for kv in sorted(gc.items())))]
    put_txt('b657_table_%s_sentences.txt' % K.KERNEL, [l.replace('\r', '') for l in L])
    put_json(K.SENT, dict(at=utc(), main=main, rows=rows, unread=[u['id'] for u in unread]))
    print(NL.join(L[2:4] + L[-1:]))


# ### the needle of b650's finding (relay data/b650_resonances_navigator.txt :25; OPEN_TRAILS :13836), b655's
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
    """(R267)(3): the kernel's plain block comments at its main scanned by the needle, then by a wider shape read by hand; `plain <hand reading>
    <asserting count>` banks the hand reading."""
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
    L = ['b657 -- COMPONENT 2, (R267)(3): %s`S PLAIN BLOCK COMMENTS SCANNED BY THE NEEDLE (%s)' % (K.KERNEL, utc()), '',
         '### rows are plain block comments (`/-`, not `/--`, not `/-!`) of the kernel`s tracked .lean files at main %s; the needle: a sentence asserting '
         'the unsupported claim, b650`s finding (relay data/b650_resonances_navigator.txt :25, OPEN_TRAILS :13836) -- b655`s NEEDLE, carried.' % (
             g(K.KD, 'rev-parse', '--short=7', 'main').strip()),
         '### the needle`s controls: b650`s two sentences and a planted one read %d of 3 ; two sentences that assert nothing of the kind read %d of 2.' % (
             len(ctl), len(neg)),
         '### files %d ; plain block comments %d ; needle hits %d:' % (len(files), nblocks, len(hits))]
    L += ['  %s:%d -- %s' % h for h in hits] or ['  NONE']
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
    put_txt('b657_plain_comments.txt', L)
    put_json('b657_plain_comments.json', dict(at=utc(), files=len(files), blocks=nblocks, hits=[list(h) for h in hits], controls=[len(ctl), 2 - len(neg)],
                                              wide=len(wide), asserting=(a[1] if len(a) > 1 else None)))
    print(NL.join(L[3:]))


def h2_row():
    """b648's named row (relay data/b648_h2_row.json, .txt): its verdict, its LICENSED cell, and the re-cut it proposed (the line after
    '### THE RE-CUT PROPOSED' in the .txt) as the ACTION (R267)(3) gives it."""
    j = jl(K.H2_ROW)['row']
    t = rdn(K.H2_ROW.replace('.json', '.txt')).split(NL)
    i = next(i for i, l in enumerate(t) if l.startswith('### THE RE-CUT PROPOSED'))
    return dict(id=j['id'], verdict=j['verdict'], licensed=j['licensed'], action='RE-CUT: ' + t[i + 1].strip())


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
    """the block's rows, keyed by sentence number as text; a sentence named in `split` read as its bullet rows `n.1`, `n.2`, ..."""
    out = []
    for r in rs:
        if str(r['n']) in split:
            for i, part in enumerate([p for p in BULLET.split(r['sentence']) if p.strip()], 1):
                out.append(dict(n='%d.%d' % (r['n'], i), sentence=_ws(part)))
        else:
            out.append(dict(n=str(r['n']), sentence=r['sentence']))
    return out


def _rows_of(k, rs0, G):
    """the block's rows as the grade bank reads them: the sentence rows, then the seat's joins (two rows the sentence split broke at an
    abbreviation, joined: G['joins'][k] = [[a, b]]), its breaks (a row broken before each named marker, the pieces numbered n.1, n.2, ...:
    G['breaks'][k] = {n: [markers]}) and b655's bullet split (G['split']). Every marker must occur in its row, in order; the rows joined
    whitespace-wise always equal the block's sentences joined -- the check exits otherwise."""
    rows = [dict(n=str(r['n']), sentence=r['sentence']) for r in rs0]
    for a, b in (G.get('joins') or {}).get(str(k)) or []:
        ia = next(i for i, r in enumerate(rows) if r['n'] == str(a))
        ib = next(i for i, r in enumerate(rows) if r['n'] == str(b))
        if ib != ia + 1:
            sys.exit('### BLOCK %d: A JOIN OF ROWS NOT ADJACENT -- NOTHING WRITTEN' % k)
        rows[ia] = dict(n=str(a), sentence=rows[ia]['sentence'] + ' ' + rows[ib]['sentence'])
        del rows[ib]
    br = (G.get('breaks') or {}).get(str(k)) or {}
    out = []
    for r in rows:
        ms = br.get(r['n'])
        if not ms:
            out.append(r)
            continue
        s, parts, pos = r['sentence'], [], 0
        for m in ms:
            j = s.find(m, pos + 1)
            if j < 0:
                sys.exit('### BLOCK %d s%s: A BREAK MARKER NOT FOUND IN ORDER -- NOTHING WRITTEN: %r' % (k, r['n'], m))
            parts.append(s[pos:j])
            pos = j
        parts.append(s[pos:])
        out += [dict(n='%s.%d' % (r['n'], i), sentence=_ws(p)) for i, p in enumerate(parts, 1)]
    if _ws(' '.join(x['sentence'] for x in out)) != _ws(' '.join(x['sentence'] for x in rs0)):
        sys.exit('### BLOCK %d: THE ROWS DO NOT REJOIN TO THE BLOCK`S SENTENCES -- NOTHING WRITTEN' % k)
    return split_rows([dict(n=x['n'], sentence=x['sentence']) for x in out], (G.get('split') or {}).get(str(k)) or {}) \
        if (G.get('split') or {}).get(str(k)) else out


def cut(rows, graded, action, bullets=False, premise=None, row_actions=None):
    """the mechanical rule (b655's): a graded OVERREACHES or UNDERSTATES row replaced in place by the ACTION (by its sentences), an UNLICENSED one
    removed, MATCHES untouched; then a sentence repeating one already in the block dropped. New at b657: a graded row named in `row_actions`
    is replaced by its own ACTION span (a verbatim span of the block's ACTION, or the h2 row's ACTION from b648), whatever its verdict.
    Returns (kept, dropped, note)."""
    import b647_record as R47
    row_actions = row_actions or {}
    act = action[len('RE-CUT: '):] if action.startswith('RE-CUT: ') else action
    abul = [p for p in BULLET.split(act.strip()) if p.strip()]
    out, gi = [], 0
    for r in rows:
        gr = graded.get(r['n'])
        if gr is None:
            out.append((r['n'], r['sentence']))
        elif r['n'] in row_actions:
            ra = row_actions[r['n']]
            ra = ra[len('RE-CUT: '):] if ra.startswith('RE-CUT: ') else ra
            out.append((r['n'], _ws(ra)))
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
            note = 'the conclusion row s%s drawn on the premise row s%s; it stands after its premise' % (c, p)
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


def _bank_line_text(bank, line):
    """one line of a relay bank, as the bank has it (the author's word on the grades at b657: the cells of the re-graded rows are taken from
    the banks that record the change at main -- data/b648_sorry_classification.txt, data/b648_sorry_repairs.txt, data/b653_runner_*)."""
    t = rd(os.path.join(ROOT, *bank.split('/'))).split(NL)
    if not (0 < line <= len(t)):
        sys.exit('### %s HAS NO LINE %d -- NOTHING WRITTEN' % (bank, line))
    return t[line - 1]


def _row_cells(k, q):
    """per block k: {sentence number: (verdict, LICENSED cell, ACTION span or None, source)} for its graded rows, the row's own source where the
    grades name one (the h2 row: b648's), else the parent's."""
    G = jl(K.GRADES)
    rf = (G.get('rows_from') or {}).get(str(k)) or {}
    ra = (G.get('row_actions') or {}).get(str(k)) or {}
    out = {}
    for n, e in ((G.get('regrade') or {}).get(str(k)) or {}).items():
        if e['verdict'] != 'UNRESOLVED':
            out[n] = (e['verdict'], _bank_line_text(e['bank'], e['line']), ('RE-CUT: ' + e['action']) if e.get('action') else None,
                      'relay %s :%d' % (e['bank'], e['line']))
    h2 = h2_row() if rf else None
    for n in set(list(rf) + list(ra)):
        if rf.get(n) == 'h2':
            out[n] = (h2['verdict'], h2['licensed'], h2['action'], 'relay data/b648_h2_row.txt (%s)' % h2['id'])
        else:
            out[n] = (q['verdict'], q['licensed'], ra.get(n), 'the parent block')
    return out


def grades(*a):
    """(R267)(3): data/b657_sentence_grades.txt from the hand grades (data/b657_sentence_grades.json), every quoted word read as a verbatim
    substring of the row's LICENSED cell (the parent's, or b648's for the h2 row) before anything is written; each row ACTION span read as a
    verbatim span of the block's ACTION (the h2 row's ACTION is b648's sentence); the cut plan beside it."""
    G = jl(K.GRADES)
    gr = G['grades']
    comp = G.get('completed') or {}
    h2 = h2_row()
    L = ['b657 -- COMPONENT 2, (R267)(3): %s`S SENTENCE ROWS GRADED BY HAND, BOUND TO THE PARENT BLOCK`S HAND CELLS; BANKED FOR THE AUTHOR`S '
         'STRIKE BEFORE ANY EDIT (%s)' % (K.KERNEL, utc()), '',
         '### the rule (b652`s, (R265)(2), as (R267)(3) carries it): a sentence row is graded OVERREACHES, UNDERSTATES or UNLICENSED where the parent',
         '### block`s HAND LICENSED or CITED cell names, quotes or paraphrases that sentence`s claim, the grade citing the cell`s words beside it; a',
         '### sentence those cells do not reach stays MATCHES; a block whose cells reach no sentence is UNRESOLVED, not cut; an ACTION carrying "..."',
         '### is UNRESOLVED-CELL, completed from the block`s own LICENSED words. The grade is the parent`s verdict. The h1_complete_at_Phi row (b648`s',
         '### h2 row, relay data/b648_h2_row.txt) is graded by its own cells: verdict %s, its LICENSED cell b648`s, its ACTION b648`s proposed' % h2['verdict'],
         '### sentence. Where a block`s ACTION re-cuts several items, a graded row may carry its own span of that ACTION (verbatim). The sources:',
         '### relay data/%s, data/%s (b647, read at %s); the blocks read at main %s; the hand grades: data/%s.' % (K.SENT, K.PARENTS, K.B647_REV,
                                                                                                              K.K_MAIN, K.GRADES),
         '### Below each block: the block as the mechanical rule leaves it -- graded rows replaced in place, repeats dropped and printed.', '']
    n_rows = n_graded = n_unres = n_drop = n_cell = 0
    by_v, J, unres = {}, [], []
    SPLIT, PREM = G.get('split') or {}, G.get('premise') or {}
    h2_seen = False
    UNACT = G.get('unacted') or {}
    n_unact = 0
    for k, p, q, rs0 in blocks():
        split = (SPLIT.get(str(k)) or {})
        rs = _rows_of(k, rs0, G)
        n_rows += len(rs)
        cells = _row_cells(k, q)
        un = UNACT.get(str(k)) or {}
        for n, (w, why) in un.items():
            if w not in q['licensed'] or n not in [r['n'] for r in rs]:
                sys.exit('### BLOCK %d s%s: AN UNACTED ROW`S WORDS NOT IN THE CELL, OR NO SUCH ROW -- NOTHING WRITTEN' % (k, n))
        rg = (G.get('regrade') or {}).get(str(k)) or {}
        for n, e in rg.items():
            bl = _bank_line_text(e['bank'], e['line'])
            if e['words'] not in bl or n not in [r['n'] for r in rs]:
                sys.exit('### BLOCK %d s%s: A RE-GRADED ROW`S WORDS NOT ON ITS BANK LINE, OR NO SUCH ROW -- NOTHING WRITTEN' % (k, n))
            if e.get('action') and e['action'] not in rd(os.path.join(ROOT, *e['bank'].split('/'))):
                sys.exit('### BLOCK %d s%s: A RE-GRADED ROW`S ACTION NOT VERBATIM IN ITS BANK -- NOTHING WRITTEN' % (k, n))
            if e['verdict'] != 'UNRESOLVED' and n not in [str(x[0]) for x in gr.get(str(k), [])]:
                sys.exit('### BLOCK %d s%s: A RE-GRADED ROW WITH A VERDICT BUT NO GRADE ROW -- NOTHING WRITTEN' % (k, n))
        mine = dict((n, w) for _k, n, w in (read_grade_row(k, x) for x in gr.get(str(k), [])))
        for n, w in mine.items():
            lic = cells[n][1] if n in cells else q['licensed']
            if w not in lic:
                sys.exit('### BLOCK %d s%s: A QUOTED WORD NOT IN ITS LICENSED CELL -- NOTHING WRITTEN: %s' % (k, n, w))
        far = [n for n in mine if n not in [r['n'] for r in rs]]
        if far:
            sys.exit('### BLOCK %d: A GRADED ROW THE BLOCK DOES NOT HAVE -- NOTHING WRITTEN: %s' % (k, far))
        action = q['action']
        for n, c in cells.items():
            if c[3] == 'the parent block' and c[2] is not None:
                span = c[2][len('RE-CUT: '):] if c[2].startswith('RE-CUT: ') else c[2]
                if span not in action:
                    sys.exit('### BLOCK %d s%s: A ROW ACTION NOT A VERBATIM SPAN OF THE BLOCK`S ACTION -- NOTHING WRITTEN' % (k, n))
        v = q['verdict']
        L.append('== #%d %s (b647`s bank line :%s ; at main %s ; %s ; HAND %s ; %d sentence rows%s)' % (
            k, p.split(':', 1)[1], rs0[0]['parent_line'], rs0[0].get('at_main'), q['kind'], v, len(rs),
            ('; s%s read as its bullet rows' % ', s'.join(split)) if split else ''))
        L.append('   LICENSED : ' + q['licensed'])
        L.append('   ACTION   : ' + q['action'])
        elided_by_rows = False
        if '...' in q['action']:
            n_cell += 1
            c = comp.get(str(k))
            if c:
                L.append('   ### UNRESOLVED-CELL: the ACTION carries "..."; completed from the block`s own LICENSED words for the strike: %s' % c)
                span = c[len('RE-CUT: '):] if c.startswith('RE-CUT: ') else c
                if span.rstrip('.') not in q['licensed']:
                    sys.exit('### BLOCK %d: A COMPLETION NOT A SPAN OF THE LICENSED CELL -- NOTHING WRITTEN' % k)
                L.append('   ### the completion is a verbatim span of the LICENSED cell; words from outside it 0.')
                action = c
            else:
                elided_by_rows = True
                L.append('   ### UNRESOLVED-CELL: the ACTION carries "..."; each graded row takes its own verbatim span of the ACTION`s words after the '
                         'elision, for the strike (no completion composed).')
        graded, row_actions = {}, {}
        for r in rs:
            if r['n'] in mine:
                c = cells.get(r['n'])
                rv = c[0] if c else v
                graded[r['n']] = rv
                if c and c[2] is not None:
                    row_actions[r['n']] = c[2]
                n_graded += 1
                by_v[rv] = by_v.get(rv, 0) + 1
                L.append('  s%-4s %-11s %s' % (r['n'], rv, r['sentence']))
                L.append('        %-11s cell: "%s"%s' % ('', mine[r['n']], (' (%s)' % c[3]) if c and c[3] != 'the parent block' else ''))
                if r['n'] in row_actions:
                    L.append('        %-11s its ACTION: %s' % ('', row_actions[r['n']]))
                if c and c[3].startswith('relay data/b648_h2_row'):
                    h2_seen = True
            elif r['n'] in rg and rg[r['n']]['verdict'] == 'UNRESOLVED':
                n_unact += 1
                e = rg[r['n']]
                L.append('  s%-4s %-11s %s' % (r['n'], 'MATCHES', r['sentence']))
                L.append('        ### UNRESOLVED, RE-GRADED AT MAIN %s (the author`s word) against relay %s :%d ("%s"): %s' % (
                    K.K_MAIN, e['bank'], e['line'], e['words'], e['reason']))
            elif r['n'] in un:
                n_unact += 1
                L.append('  s%-4s %-11s %s' % (r['n'], 'MATCHES', r['sentence']))
                L.append('        ### REACHED BY THE CELL ("%s"), NO ACTION TEXT FOR THIS ROW -- NOT CUT, RAISED FOR THE STRIKE: %s' % tuple(un[r['n']]))
            else:
                L.append('  s%-4s %-11s %s' % (r['n'], 'MATCHES', r['sentence']))
        if elided_by_rows and [n for n in graded if n not in row_actions]:
            sys.exit('### BLOCK %d: AN ELIDED ACTION AND A GRADED ROW WITHOUT ITS OWN SPAN -- NOTHING WRITTEN' % k)
        if not graded:
            n_unres += 1
            unres.append(k)
            L.append('   ### UNRESOLVED: %s; not cut.' % ('every row the cells reach is listed UNRESOLVED above, with its reason' if (un or rg)
                                                        else 'no sentence the cells reach'))
            J.append(dict(k=k, parent=p, file=q['file'], line=q['line'], unresolved=True))
            L.append('')
            continue
        prem = PREM.get(str(k))
        kept, dropped, note = cut(rs, graded, action, bullets=bool(split), premise=prem, row_actions=row_actions)
        n_drop += len(dropped)
        L.append('   -> THE BLOCK AFTER THE CUT (%d sentences; repeats dropped %d):' % (len(kept), len(dropped)))
        L += ['        ' + x for x in kept] + ['        ### DROPPED AS A REPEAT: ' + x for x in dropped]
        J.append(dict(k=k, parent=p, file=q['file'], line=q['line'], bank_line=rs0[0]['parent_line'], verdict=v, graded=sorted(graded),
                      verdicts=graded, row_actions=row_actions, action=action, completed=('...' in q['action']), kept=kept, dropped=dropped,
                      sentences=[r['sentence'] for r in rs0], split=sorted(split), premise=prem))
        L.append('')
    pl = jl('b657_plain_comments.json')
    unread = jl(K.SENT).get('unread') or []
    L.append('### PARENT BLOCKS NOT FOUND AT MAIN (listed, not graded): %s' % ('; '.join(unread) or 'NONE'))
    L.append('### PLAIN-COMMENT ROWS (relay data/b657_plain_comments.txt): %s' % ('; '.join('%s:%d -- %s' % tuple(h) for h in pl.get('hits') or []) or 'NONE'))
    L.append('### THE h2 ROW (b648`s, (R267)(3)): %s' % ('GRADED, ITS ACTION b648`S SENTENCE' if h2_seen else '### NOT GRADED'))
    L.append('### ROWS LISTED UNRESOLVED WITH THEIR REASONS (re-graded at main against the banks that record the change, the author`s word; '
             'not cut): %d' % n_unact)
    n_cut = len([b for b in J if b.get('kept') is not None])
    files = sorted(set(b['file'] for b in J if b.get('kept') is not None))
    L.append('### ### **PARENT BLOCKS %d ; SENTENCE ROWS %d ; GRADED %d (%s) ; MATCHES %d ; UNRESOLVED BLOCKS %d (%s) ; UNRESOLVED-CELL %d ; '
             'NOT FOUND AT MAIN %d ; BLOCKS TO CUT %d IN %d FILES ; REPEATS DROPPED BY THE RULE %d ; PLAIN-COMMENT ROWS %d ; THE h2 ROW %s.**' % (
                 len(J), n_rows, n_graded, ', '.join('%s %d' % kv for kv in sorted(by_v.items())), n_rows - n_graded, n_unres,
                 ', '.join('#%d' % e for e in unres) or 'none', n_cell, len(unread), n_cut, len(files), n_drop, len(pl.get('hits') or []),
                 'GRADED' if h2_seen else 'NOT GRADED'))
    put_txt('b657_sentence_grades.txt', L)
    put_json('b657_sentence_cut_plan.json', dict(at=utc(), blocks=J))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE CUT PLANNED ON THE BLOBS (b655's, carried)
def _norm_map(text):
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
        rs = _rows_of(k, rs0, G)
        cells = _row_cells(k, q)
        mine = dict((n, w) for _k, n, w in (read_grade_row(k, x) for x in gr.get(str(k), [])))
        graded = dict((r['n'], (cells[r['n']][0] if r['n'] in cells else q['verdict'])) for r in rs if r['n'] in mine)
        row_actions = dict((n, c[2]) for n, c in cells.items() if n in graded and c[2] is not None)
        if not graded:
            continue
        action = (comp.get(str(k)) or q['action']) if '...' in q['action'] else q['action']
        cut(rs, graded, action, bullets=bool(split), premise=PREM.get(str(k)), row_actions=row_actions)
        out.append((k, q, rs, cut.slots))
    return out


def plan_cut(*a):
    """(R267)(3): the cut planned on the kernel's main blobs at K_MAIN, b655's planner: every row of a graded block located in order in its file by
    its whitespace-collapsed text from the block's line at main; each changed row replaced in its span by its slot's kept output, wrapped at the
    line's indent; one edit per block. The planned file checked: its comment-stripped code equal to main's."""
    files, edits, fails = {}, [], []
    S = dict((r['parent'], r) for r in jl(K.SENT)['rows'])
    for k, q, rs, slots in _plans():
        f = q['file']
        if f not in files:
            files[f] = (_show(K.KD, K.K_MAIN, f) or '').replace(chr(13), '')
        text = files[f]
        at = S[q['id']].get('at_main') or ''
        m = re.search(r':(\d+)$', at)
        line0 = int(m.group(1)) if m else q['line']
        start_line_off = sum(len(l) + 1 for l in text.split(NL)[:line0 - 1])
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
        edits.append(dict(k=k, file=f, line=line0, old=old, new=new, changed=changed))
    planned = {}
    for f, t in files.items():
        nt = t
        for e in [x for x in edits if x['file'] == f]:
            nt = nt.replace(e['old'], e['new'], 1)
        planned[f] = nt
    code_bad = [f for f in files if _code_only(files[f]) != _code_only(planned[f])]
    L = ['b657 -- COMPONENT 3, (R267)(3): THE CUT PLANNED ON %s`S MAIN BLOBS AT %s (%s)' % (K.KERNEL, K.K_MAIN, utc()), '',
         '### from relay data/b657_sentence_grades.txt (rows are sentences, parents are blocks) and its hand grades; each graded block`s rows located in',
         '### order in its file from the block`s line at main; each changed row replaced in its span by its slot`s kept output, wrapped at the line`s',
         '### indent; one edit per block.',
         '### files %d ; edits %d ; rows located %s ; regions not unique %s ; files whose comment-stripped code differs from main`s %s' % (
             len(files), len(edits), 'ALL' if not [x for x in fails if 'not found' in x] else fails,
             [x for x in fails if 'unique' in x] or 'NONE', code_bad or 'NONE'), '']
    for e in edits:
        L += ['== #%d %s:%d (rows changed %s)' % (e['k'], e['file'], e['line'], ', '.join('s' + n for n in e['changed'])),
              '   OLD: ' + e['old'].replace(NL, ' | ')[:1200], '   NEW: ' + e['new'].replace(NL, ' | ')[:1200], '']
    L += ['### ### **FILES %d ; EDITS %d ; LOCATION FAILURES %d ; CODE OUTSIDE COMMENTS CHANGED IN %d FILES.**' % (
        len(files), len(edits), len(fails), len(code_bad))]
    put_txt('b657_cut_plan.txt', L)
    put_json('b657_cut_edits.json', dict(at=utc(), main=K.K_MAIN, edits=edits, planned_sha={f: __import__('hashlib').sha256(t.encode('utf-8')).hexdigest()
                                                                                           for f, t in planned.items()}, fails=fails, code_bad=code_bad))
    print(NL.join(L[5:6] + L[-1:]))


def _planned(f):
    j = jl('b657_cut_edits.json')
    t = (_show(K.KD, j['main'], f) or '').replace(chr(13), '')
    for e in [x for x in j['edits'] if x['file'] == f]:
        t = t.replace(e['old'], e['new'], 1)
    return t


def check_file(*a):
    """`check_file <file> [head]`: the working file (CR stripped) or the branch head's blob against the planned text, and its comment-stripped
    code against main's. Prints one line; exits 1 on a difference."""
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
    """every graded row of the grade bank looked for in its file at `ref`, whitespace aside: standing or gone, by its verdict. A row is
    gone when its sentence occurs fewer times in the file at `ref` than at main (b657: a one-word row such as "Clean." also stands
    elsewhere in its file as a MATCHES row, so presence alone cannot read it); at main itself every graded row stands."""
    import collections
    G = jl(K.GRADES)
    files, mains, standing, gone = {}, {}, [], 0
    cnt = collections.Counter()
    for k, q, rs, _slots in _plans():
        cells = _row_cells(k, q)
        mine = set(n for _k, n, _w in (read_grade_row(k, x) for x in G['grades'].get(str(k), [])))
        f = q['file']
        if f not in files:
            files[f] = _ws(_show(K.KD, ref, f) or '')
            mains[f] = _ws(_show(K.KD, K.K_MAIN, f) or '')
        for r in rs:
            if r['n'] not in mine:
                cnt['MATCHES'] += 1
                continue
            v = cells[r['n']][0] if r['n'] in cells else q['verdict']
            s = _ws(r['sentence'])
            if s in files[f] and files[f].count(s) >= mains[f].count(s):
                standing.append((k, f, r['n'], v, r['sentence']))
                cnt[v + ' (STANDING)'] += 1
            else:
                gone += 1
                cnt['CUT'] += 1
    return cnt, standing


def cut_bank(*a):
    """(R267)(3): data/b657_cut_SIDE-lv-conservation.txt -- the branch, its commits one per file, each head blob against the plan and its
    comment-stripped code against main's, and the grade bank re-run at the branch with its control at main."""
    gk = lambda *x: g(K.KD, *x)   # noqa: E731
    log = [l.split(' ', 1) for l in gk('log', '--reverse', '--format=%h %s', K.K_MAIN + '..' + K.CUT_BRANCH).split(NL) if l.strip()]
    plan = jl('b657_cut_edits.json')
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
        rows.append('  %s  %-48s blocks %-22s blob %s ; code outside comments %s' % (
            h, f, ', '.join('#%d' % k for k in ks), 'EQUALS THE PLAN' if eq else '### DIFFERS', 'EQUAL TO MAIN`S' if code else '### CHANGED'))
    after, st = _regrade(K.CUT_BRANCH)
    ctl, st0 = _regrade(K.K_MAIN)
    L = ['b657 -- COMPONENT 3, (R267)(3): %s`S DOCSTRINGS CUT ON THE BRANCH %s (%s)' % (K.KERNEL, K.CUT_BRANCH, utc()), '',
         '### the grades: relay data/b657_sentence_grades.txt (rows are sentences, parents are blocks; the author`s word at Component 2); the plan:',
         '### data/b657_cut_plan.txt; one commit per file by the Edit tool, each working file checked against the plan before its commit; the',
         '### branch from main %s.' % K.K_MAIN, '',
         '### THE COMMITS (rows are commits, one per file):'] + rows + [
         '', '### COMMITS %d ; FILES IN THE PLAN %d ; COMMITS TOUCHING ONE FILE %d ; FAULTS %s' % (len(log), len(pf), len(rows), bad or 'NONE'),
         '', '### THE GRADE BANK RE-RUN AT THE BRANCH (each graded row looked for in its file, whitespace aside):',
         '  ' + ', '.join('%s %d' % kv for kv in sorted(after.items())),
         '  graded rows still standing: %s' % (['#%d %s s%s %s' % x[:4] for x in st] or 'NONE'),
         '### THE CONTROL, the same read at main %s: ' % K.K_MAIN + ', '.join('%s %d' % kv for kv in sorted(ctl.items())), '',
         '### ### **COMMITS %d IN %d FILES ; GRADED ROWS CUT %d ; STANDING %d (OVERREACHES %d, UNDERSTATES %d, UNLICENSED %d) ; AT MAIN STANDING %d ; '
         'FAULTS %d.**' % (len(log), len(pf), after.get('CUT', 0), len(st), after.get('OVERREACHES (STANDING)', 0), after.get('UNDERSTATES (STANDING)', 0),
                           after.get('UNLICENSED (STANDING)', 0), len(st0), len(bad))]
    put_txt('b657_cut_SIDE-lv-conservation.txt', L)
    put_json('b657_cut_SIDE-lv-conservation.json', dict(at=utc(), commits=[x[0] for x in log], files=len(pf), faults=bad, after=dict(after),
                                                         standing=[list(x) for x in st], control=dict(ctl), control_standing=len(st0)))
    print(NL.join(L[-8:]))


# ================================================================================ COMPONENT 3: THE RUNNER, (R267)(3) under (R263)(4)
# ### the kernel's workflow (b653's, on main at 2b5959f), read whole: lake build of the target under the hold; a scratch file printing the axioms
# ### of T3_StepNineBridge's eight named terminals; the artifact out/ (ref.txt, cache.log, build.log, build_exit.txt, mem.log, axioms.txt).
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
PRINT_RE = re.compile(r"^'(.+?)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", re.M)
ERR_RE = re.compile(r'^(?:error: )?(\S+\.lean):(\d+):(\d+): error: (.*)$', re.M)
BANK_ROW = re.compile(r"^\s+(\S+)\s+(DERIVES|[A-Z][A-Z -]+?)\s+\[([^\]]*)\]\s*$")


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def _prints(text):
    return [(m.group(1), sorted(x.strip() for x in (m.group(2) or '').split(',') if x.strip())) for m in PRINT_RE.finditer(text)]


def _banked_prints():
    """the banked profiles of the eight terminals: b653's runner bank, its table rows (name, verdict, axioms) at the worklist's lines."""
    name, a0, a1 = K.BANKED_PRINTS
    out = {}
    for l in rdn(name).split(NL)[a0 - 1:a1]:
        m = BANK_ROW.match(l)
        if m:
            out[m.group(1)] = sorted(x.strip().strip("'") for x in m.group(3).split(',') if x.strip())
    return out


def runner(*a):
    """`runner`: the run read by its id; the artifact listed, downloaded by its id into memory, its sha256 against the platform's digest before
    any reading; the build's exit and error lines, the memory log's low and any STOP, the eight prints against the banked profiles terminal by
    terminal. Banked as data/b657_runner_SIDE-lv-conservation.txt and a row of data/b657_runner_rows.json."""
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
    L = ['b657 -- COMPONENT 3, (R267)(3): THE HOSTED RUNNER FOR %s, READ BY ITS RUN ID (%s)' % (kern, utc()), '',
         '### the workflow file on main (%s, .github/workflows/build-module.yml, b653`s, under (R263)(4)), read back whole:' % R['workflow_commit']] + \
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
    blog = T_.get('build.log', '')
    bexit = T_.get('build_exit.txt', '').strip()
    errs = [(m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)) for m in ERR_RE.finditer(blog)]
    P = _prints(T_.get('axioms.txt', ''))
    B = _banked_prints()
    per = []
    for n, ax in P:
        b = B.get(n)
        per.append((n, ax, b, set(ax) <= STD3 and 'sorryAx' not in ax, b is not None and b == ax))
    missing = sorted(set(B) - set(n for n, _a in P))
    ok = (run.get('conclusion') == 'success' and row['artifact_sha256'] and bexit == '0' and not errs and not stops and row['mem_low'] is not None
          and row['mem_low'] >= K.HOLD and len(P) == len(B) > 0 and not missing and all(s and e for _n, _a, _b, s, e in per))
    row['gate'] = 'DERIVES' if ok else ('STOPPED BENEATH THE HOLD' if stops else 'NOT DERIVES')
    row['errors'] = [list(e) for e in errs]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: samples %d ; LOW %s MB ; the hold %d ; STOP lines %s' % (
              len([l for l in mem.split(NL) if 'avail_mb=' in l]), row['mem_low'], K.HOLD, stops or 'NONE'),
          '### the build: exit %s ; error lines %d ; the log`s last lines:' % (bexit or '### UNREAD', len(errs))] + \
        ['    ' + l for l in blog.rstrip(NL).split(NL)[-6:]] + ['    %s:%d:%d: %s' % e for e in errs[:30]] + [
          '### THE GATE READING PER TERMINAL (the run`s print ; the banked profile, relay data/%s :%d-:%d):' % K.BANKED_PRINTS] + \
        ['  %-66s %-30s %s ; banked %s ; %s' % (n, ax, 'STANDARD THREE OR NONE' if s else '### NOT', b, 'EQUAL' if e else '### DIFFERENT')
         for n, ax, b, s, e in per] + ['  banked terminals not printed: %s' % (missing or 'NONE'), '',
          '### ### **RUN %s ; CONCLUSION %s ; ARTIFACT SHA256 %s ; MEMORY LOW %s MB (HOLD %d) ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS %d, AT THE '
          'STANDARD THREE OR NONE %d, EQUAL TO THE BANKED PROFILES %d ; GATE %s.**' % (
              R['run_id'], run.get('conclusion'), (row['artifact_sha256'] or '### NONE')[:16], row['mem_low'], K.HOLD, bexit or '?', len(errs), len(P),
              sum(1 for x in per if x[3]), sum(1 for x in per if x[4]), row['gate'])]
    put_txt('b657_runner_%s.txt' % kern, L)
    j = jl('b657_runner_rows.json') or {'rows': []}
    j['rows'] = [r for r in (j.get('rows') or []) if r['kernel'] != kern] + [row]
    put_json('b657_runner_rows.json', j)
    print(L[-1])


def runner_merged(*a):
    """`runner_merged <merge sha> <tag>`: the row's merge and tag, after main and the tag are read back at the remote."""
    sha, tag = a[:2]
    j = jl('b657_runner_rows.json')
    for r in j['rows']:
        if r['kernel'] == K.KERNEL:
            r['merged'], r['tag'] = sha, tag
    put_json('b657_runner_rows.json', j)
    print('  %s merged %s tag %s' % (K.KERNEL, sha, tag))


# ================================================================================ THE LATE ROUTES (b656's, carried; every row read through READERS)
import collections                 # noqa: E402
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


def _session_rows():
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
    """data/b657_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
    delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim."""
    calls, results, words, plain_, start = [], {}, [], [], None
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
                    plain_.append((i, t.strip()))
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
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %d), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b657 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b657_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b657_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
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
    L = ['b657 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
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
    put_txt('b657_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b657_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])


def kernels(*a):
    import b641_record as R41
    put_json('b657_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


def _defect_short():
    return [re.match(r'^\(([a-z])\) ([^.]*)\.', l.strip()).group(0)[:-1] for l in rdn('b657_defects.txt').split(NL)
            if re.match(r'^    \([a-z]\) [^.]*\.', l)]


def defects(*a):
    t = rdn('b657_defects.txt')
    ds = [l.strip() for l in t.split(NL) if re.match(r'^    \([a-z]\) ', l)]
    put_json('b657_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b657_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b657_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|mirror.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b657_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b657_seal_hashes.json' in banks, crlf or 'none'))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b657'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import shutil
    import tempfile
    import act_root as AR
    J = jl('b657_act_root.json')
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
    L = ['b657 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b657_root_arm.txt', L)
    put_json('b657_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b657 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b657_table_final.txt', L)
    put_json('b657_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


# ### THE SCORES, THE RECORD TEXT, THE DESK, THE COMPONENTS AND THE DRY RUN: written after Component 3 lands, before the gate's dry-run step.


# ================================================================================ THE MIRROR, AT THE CLOSE ((R267)(4); b656's routes, carried)
import hashlib as _hl   # noqa: E402

MIRROR_TAG = '2026-10-12-b657'
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
    put_json('b657_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b657':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b657`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b657_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b657_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b657_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b657 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b657_mirror.txt', L)
    put_json('b657_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:8]:
        print(l[:240])


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith('_'):
        print('usage: b657_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
