# -*- coding: utf-8 -*-
"""b664_record.py -- THE ACT'S RECORD TOOL, b664 under (R274).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b664's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### (R274)(4), from this act: no constant here names a kernel file; the kernel files are read from the act's cut bank through
### tools/b664_worklist.py's kernel_files(), the read printed.
### Carried by the Write tool from b663_record.py (the helpers, the guarded landing, the answers, the late routes) and b662_record.py (the
### sentence rows, the plain comments, the grades, the cut planned on the blobs and its check, the cut bank, the runner, the mirror); new
### here: the record lines of (R274)(1)-(4), the no-disclosure re-run of (R274)(4). The later routes are added by the Edit tool before the
### seal, each run before the face names it.
### Routes: `python tools/b664_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
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
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported
import b664_worklist as K          # noqa: E402

STANDIN = bool(os.environ.get('B664_STANDIN'))


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
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b664_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b664_findings.json': dict(entry_line=99999, title='stand-in'),
        'b664_trail.json': dict(line=99999),
        'b664_act_root.json': dict(root='0' * 64, previous='e00d7158' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
        'b664_mirror.json': dict(zip='stand-in', manifest_md5='0' * 32),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b664's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b664_scanfile_%s.md' % tag)
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
    """a row of data/b664_runner_rows.json -- every key of RUNNER_KEYS present (None where a step did not reach it); returns the row's reading
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
    """a scores row: key N1..N5 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text) -- the whole verdict, not its first
    word (b656's defect (e))."""
    if not re.match(r'^(N[1-5]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


def read_grade_row(k, row):
    """a row of the hand grades (data/b664_sentence_grades.json): block number k and [sentence number, the cell's quoted words];
    returns (k, n, words); raises on a row of another shape."""
    n, w = row
    ok_n = (isinstance(n, int) and n >= 1) or (isinstance(n, str) and re.match(r'^\d+(\.\d+)?$', n) is not None)
    if not ok_n or not isinstance(w, str) or not w.strip() or not str(k).isdigit():
        raise ValueError('grade row of another shape: %r' % (row,))
    return int(k), str(n), w


def read_kernel_files():
    """(R274)(4): the act's kernel files as tools/b664_worklist.py's kernel_files() reads them from the cut bank; returns [(file, [banks])];
    raises when the read finds no file (no constant stands in for it)."""
    kf = K.kernel_files()
    if not kf or not all(isinstance(f, str) and f.endswith('.lean') and b for f, b in kf):
        raise LookupError('no kernel file read from the cut bank')
    return kf


READERS = ['read_runner_row', 'read_score_row', 'read_head', 'read_grade_row', 'read_kernel_files']


# ================================================================================ STEP ZERO, (R274)(4): THE NO-DISCLOSURE ARM RE-RUN BY THE BANK READ
def nd_rerun(*a):
    """(R274)(4) at this act's step zero: b663's kernel file read from b663's instance bank (data/b663_epstein_instance.json, its run's `file`)
    and from no constant, the read printed; TECHNE-Core's needle sets (b616_record.nd_hits, read locally, never printed) run over the file at
    SIDE-explicit-formula main; the counts banked as data/b664_nd_rerun.txt."""
    import b616_record as R6
    j = jl(K.B663_INSTANCE_BANK)
    f = (j.get('run') or {}).get('file')
    if not f:
        sys.exit('### THE INSTANCE BANK NAMES NO FILE -- NOTHING WRITTEN')
    src = _show('D:/SIDE-explicit-formula', 'main', f) or ''
    hits = dict(R6.nd_hits(src, R6.nd_sets())[0])
    ctl = dict(R6.nd_hits(src + NL + 'planted', R6.nd_sets())[0])
    L = ['b664 -- STEP ZERO, (R274)(4): THE NO-DISCLOSURE ARM RE-RUN OVER b663`S KERNEL FILE, READ FROM ITS BANK (%s)' % utc(), '',
         '### the read: relay data/%s, key run.file -> %s (no constant); the file at SIDE-explicit-formula main %s, %d bytes' % (
             K.B663_INSTANCE_BANK, f, g('D:/SIDE-explicit-formula', 'rev-parse', '--short=7', 'main').strip(), len(src.encode('utf-8'))),
         '### TECHNE-Core`s needle sets (relay tools/b616_record.py nd_sets, read locally, the needles never printed) over the file: %s' % hits,
         '### b663`s suite read SIDEExplicitFormula/Schema/Epstein.lean in its place (relay data/b663_defects.txt (o)); this read replaces that one.',
         '### ### **THE FILE READ FROM THE BANK: %s ; HITS %d.**' % (f, sum(hits.values()))]
    put_txt('b664_nd_rerun.txt', L)
    put_json('b664_nd_rerun.json', dict(at=utc(), bank='data/' + K.B663_INSTANCE_BANK, file=f, hits=hits, bytes=len(src.encode('utf-8'))))
    print(NL.join(L[2:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R274)(1)-(4)
WH = ('*Appended 2026-10-13 by b664 to b663’s entry (:8537), under `(R274)`(1)-(2) -- b663 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b663_closing.txt):*')
FTH = ('*Appended 2026-10-13 by b664 beneath the transform-bound order (:14162, named there W-ORD-FT-FIRST-ORDER), under `(R274)`(3) -- '
       'PLACED:*')
CEH = '*Appended 2026-10-13 by b664 beneath W-ORD-EPSTEIN-CERTIFY (:14158), under `(R274)`(3) -- PLACED:*'
RH_ = ('### `(R274)`(4) -- A KERNEL FILE IS READ FROM THE ACT’S BANK, NOT FROM A CONSTANT, STANDING FROM b664, appended 2026-10-13, b664, '
       'under the author’s ruling')


def _weight():
    return ('\n' + WH + ' the plan on b590’s Schema/Epstein.lean, no rung built, the five PRICED; the dominant off-line zero of Z_Q below 150 '
            'index 0 (0.9533 + 16.2902 i), not b590’s rhoE, both printed; Schema/EpsteinQ0.lean on four named premises, each stated, not '
            'proved; open; run 38413488503 with 31 terminals at the standard three and no sorry, Q0Premises entered in the E0 rule’s list of '
            'met names by ruling and the seven premise-carrying theorems INTERFACES on it; merged alone at SIDE-explicit-formula d00ab16, tag '
            'v0.29; the computation -- the control at Z₁ reproducing j₀ = 31, every hypothesis certified by name at Q0, hθ above 150 on the '
            'READ premise B1, j₀ = 38 and the zero side −7.57·10³⁹ in balls on the banked configuration, not ball-certified; H1-H4 HELD, H3 and '
            'H4 on B1; relay ba1ba004, PLACE-papers 07d147d, FINDINGS :8535 and :8537, OPEN_TRAILS :14166, the root e00d7158… over 44 banks; '
            'the suite 78 of 80 with G-AXIOM-CLAIM carried and G-EDIT-ROUTE on (m) declared; eighteen defects, (o) the sealed scorer’s file '
            'constant naming b590’s file and the no-disclosure arm reading it. No mirror. Nothing deposited. WHAT IT SAYS (`(R274)`(2)): at a '
            'configuration whose target is false, the schema’s positivity fails and the compiled rate names the index -- the control fired; '
            'it fired on points banked at 119 digits by two agreeing routes and not ball-certified, and on one READ bound, B1; the sentence that '
            'carries the result carries both caveats by name until W-ORD-EPSTEIN-CERTIFY and the transform-bound order discharge them. Nothing '
            'in it is about ζ.\n')


def _ft():
    return ('\n' + FTH + ' the transform-bound order -- one lemma, the bound by one integration by parts -- joins b665 beside the Keiper face '
            'as that act’s second component, so B1 becomes a kernel lemma and b663’s READ caveat falls. The research order after b663: b665 '
            'the Keiper face with the transform-bound order; b667 W-ORD-EPSTEIN-CERTIFY; b669 the χ-Li converse; b670 the reading act; the '
            'close-pair bench after the companions as before.\n')


def _ce():
    return ('\n' + CEH + ' W-ORD-EPSTEIN-CERTIFY -- the 17 off-line zeros and the on-line list to 150 isolated in Arb balls by an '
            'argument-principle count -- takes the research slot after b665, before the χ-Li converse, as b667; its ruling then fixes the '
            'method and its controls before any number. When it lands, b663’s second caveat (points banked, not ball-certified) falls.\n')


def _rule():
    nd = jl('b664_nd_rerun.json')
    return ('\n' + RH_ + '\n\n**The rule.** From b664 the suite and the scorer read the act’s kernel files from the act’s plan or cut bank '
            'and from no constant, the read printed before the seal; a repair of a failure on real state under the freeze, no new arm. '
            '**Its cause:** b663’s defect (o) -- a constant in a sealed tool (tools/b663_worklist.py :44) named b590’s '
            'SIDEExplicitFormula/Schema/Epstein.lean where the scorer and the no-disclosure arm meant the act’s file. **At b664’s step zero:** '
            'the no-disclosure arm re-run over %s, the file read from relay data/%s, hits %d (relay data/b664_nd_rerun.txt). **Carried by:** '
            'tools/b664_worklist.py’s kernel_files(), read by the record tool and the suite from data/b664_cut_edits.json and '
            'data/b664_cut_SIDE-effects.json.\n' % (nd.get('file', '?'), K.B663_INSTANCE_BANK, sum((nd.get('hits') or {}).values())))


def c1(*a):
    items = [('FINDINGS.md', WH, _weight()), ('OPEN_TRAILS.md', FTH, _ft()), ('OPEN_TRAILS.md', CEH, _ce()), ('OPEN_TRAILS.md', RH_, _rule())]
    land(items, 'b664_record_lines.json', 'c1', entry=K.B663_ENTRY,
         check=[('FINDINGS.md', K.B663_ENTRY, '## The Epstein instance at Q0'), ('OPEN_TRAILS.md', K.FT_LINE, 'W-ORD-FT-FIRST-ORDER'),
                ('OPEN_TRAILS.md', K.CERTIFY_LINE, 'W-ORD-EPSTEIN-CERTIFY'), ('OPEN_TRAILS.md', K.B663_TRAIL, '### b663')],
         dry='dry' in a)


# ================================================================================ THE AUTHOR'S ANSWERS (b663's route, carried)
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID


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
    """data/b664_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
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
    head = ['### b664 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b664_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b664_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 2: THE SENTENCE ROWS, THE PLAIN COMMENTS, THE GRADES
def _bank_line(bank_lines, rid_tail):
    for i, l in enumerate(bank_lines, 1):
        if l.startswith('  %s@%s:%s |' % (K.KERNEL, K.B647_REV, rid_tail)):
            return i
    return None


def sentences(*a):
    """(R274)(5), the b651 route as b657, b659 and b662 ran it: the kernel's OVERREACHES, UNDERSTATES and UNLICENSED blocks of b647's bank
    (read at ef4cff7) read into sentence rows at the kernel's main; a block whose text is not found at main is listed, not read;
    data/b664_table_<kernel>_sentences.txt and .json."""
    import b647_record as B7
    import licensed_table as LT
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
    import collections
    gc = collections.Counter(x['generated'] for x in rows)
    main = g(K.KD, 'rev-parse', '--short=7', 'main').strip()
    L = ['b664 -- COMPONENT 2, (R274)(5): %s`S OVERREACHES, UNDERSTATES AND UNLICENSED BLOCKS READ INTO SENTENCE ROWS (%s)' % (K.KERNEL, utc()), '',
         '### rows are sentences, parents are blocks. The parents: relay data/%s, its OVERREACHES, UNDERSTATES and UNLICENSED rows (%d), read at %s; '
         'the generator: b647_record._kdoc_rows at %s main %s, each block`s context captured and each unit read by licensed_table.docstring_row; the '
         'unit: b647_record._MSPLIT as b658 repaired it -- the b651 route. A GENERATED reading per sentence; the HAND reading per sentence is the '
         'grade bank`s.' % (K.PARENTS, len(parents), K.B647_REV, K.KERNEL, main),
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
    put_txt('b664_table_%s_sentences.txt' % K.KERNEL, [l.replace('\r', '') for l in L])
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
    """(R274)(5): the kernel's plain block comments at its main scanned by the needle, then by a wider shape read by hand; `plain <hand reading>
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
    L = ['b664 -- COMPONENT 2, (R274)(5): %s`S PLAIN BLOCK COMMENTS SCANNED BY THE NEEDLE (%s)' % (K.KERNEL, utc()), '',
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
    put_txt('b664_plain_comments.txt', L)
    put_json('b664_plain_comments.json', dict(at=utc(), files=len(files), blocks=nblocks, hits=[list(h) for h in hits], controls=[len(ctl), 2 - len(neg)],
                                              wide=len(wide), asserting=(a[1] if len(a) > 1 else None)))
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
    """the block's rows as the grade bank reads them: the sentence rows, then the seat's joins (G['joins'][k] = [[a, b]]), its breaks (a row
    broken before each named marker, the pieces numbered n.1, n.2, ...: G['breaks'][k] = {n: [markers]}) and b655's bullet split (G['split']).
    Every marker must occur in its row, in order; the rows joined whitespace-wise always equal the block's sentences joined -- the check exits
    otherwise."""
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
    """the mechanical rule (b655's, b657's): a graded OVERREACHES or UNDERSTATES row replaced in place by the ACTION (by its sentences), an
    UNLICENSED one removed, MATCHES untouched; then a sentence repeating one already in the block dropped; a graded row named in `row_actions`
    replaced by its own ACTION span (a verbatim span of the block's ACTION), whatever its verdict. Returns (kept, dropped, note)."""
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
    """one line of a relay bank, as the bank has it (the re-grade's cell, (R267)(3)'s change-bank rule)."""
    t = rd(os.path.join(ROOT, *bank.split('/'))).split(NL)
    if not (0 < line <= len(t)):
        sys.exit('### %s HAS NO LINE %d -- NOTHING WRITTEN' % (bank, line))
    return t[line - 1]


def _row_cells(k, q):
    """per block k: {sentence number: (verdict, LICENSED cell, ACTION span or None, source)} for its graded rows: a re-grade's bank line, else the
    parent's cells with the row's own ACTION span where the grades name one."""
    G = jl(K.GRADES)
    ra = (G.get('row_actions') or {}).get(str(k)) or {}
    out = {}
    for n, e in ((G.get('regrade') or {}).get(str(k)) or {}).items():
        if e['verdict'] != 'UNRESOLVED':
            out[n] = (e['verdict'], _bank_line_text(e['bank'], e['line']), ('RE-CUT: ' + e['action']) if e.get('action') else None,
                      'relay %s :%d' % (e['bank'], e['line']))
    for n in ra:
        out[n] = (q['verdict'], q['licensed'], ra.get(n), 'the parent block')
    return out


def grades(*a):
    """(R274)(5): data/b664_sentence_grades.txt from the hand grades (data/b664_sentence_grades.json), every quoted word read as a verbatim
    substring of the row's LICENSED cell (or its re-grade's bank line) before anything is written; each row ACTION span read as a verbatim span
    of the block's ACTION; the cut plan beside it."""
    G = jl(K.GRADES)
    gr = G['grades']
    comp = G.get('completed') or {}
    L = ['b664 -- COMPONENT 2, (R274)(5): %s`S SENTENCE ROWS GRADED BY HAND, BOUND TO THE PARENT BLOCK`S HAND CELLS; BANKED FOR THE AUTHOR`S '
         'STRIKE BEFORE ANY EDIT (%s)' % (K.KERNEL, utc()), '',
         '### the rule (b652`s, (R265)(2), as (R267)(3) and (R274)(5) carry it): a sentence row is graded OVERREACHES, UNDERSTATES or UNLICENSED where',
         '### the parent block`s HAND LICENSED or CITED cell names, quotes or paraphrases that sentence`s claim, the grade citing the cell`s words beside',
         '### it; a sentence those cells do not reach stays MATCHES; a block whose cells reach no sentence is UNRESOLVED, not cut; an ACTION carrying',
         '### "..." is UNRESOLVED-CELL. The grade is the parent`s verdict. Where a block`s ACTION re-cuts several items, a graded row may carry its own',
         '### span of that ACTION (verbatim). (R267)(3): a row in a file the kernel`s main changed since b647 is re-graded against the change banks, the',
         '### bank`s own line quoted. The sources: relay data/%s, data/%s (b647, read at %s); the blocks read at main %s; the change banks %s; the' % (
             K.SENT, K.PARENTS, K.B647_REV, K.K_MAIN, ', '.join(K.CHANGE_BANKS)),
         '### hand grades: data/%s.' % K.GRADES,
         '### Below each block: the block as the mechanical rule leaves it -- graded rows replaced in place, repeats dropped and printed.', '']
    n_rows = n_graded = n_unres = n_drop = n_cell = 0
    by_v, J, unres = {}, [], []
    SPLIT, PREM = G.get('split') or {}, G.get('premise') or {}
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
            elif r['n'] in rg and rg[r['n']]['verdict'] == 'UNRESOLVED':
                n_unact += 1
                e = rg[r['n']]
                L.append('  s%-4s %-11s %s' % (r['n'], 'MATCHES', r['sentence']))
                L.append('        ### UNRESOLVED, RE-GRADED AT MAIN %s against relay %s :%d ("%s"): %s' % (
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
            L.append('   ### UNRESOLVED: %s; not cut.' % ('every row the cells reach is listed above, with its reason' if (un or rg)
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
    pl = jl('b664_plain_comments.json')
    unread = jl(K.SENT).get('unread') or []
    L.append('### PARENT BLOCKS NOT FOUND AT MAIN (listed, not graded): %s' % ('; '.join(unread) or 'NONE'))
    L += ['  UNRESOLVED-NO-CELL  %s -- restated at b648 (relay data/b648_sorry_repairs.txt :6, :55-:101); no b647-form cell reaches the text at main; '
          'listed for the kernel`s cell refresh, the author`s word; the seat`s hand reading printed beside it as a reading, not a grade (relay '
          'data/b664_restated_reading.txt)' % u.split(':', 1)[1] for u in unread]
    L.append('### PLAIN-COMMENT ROWS (relay data/b664_plain_comments.txt): %s' % ('; '.join('%s:%d -- %s' % tuple(h) for h in pl.get('hits') or []) or 'NONE'))
    L.append('### ROWS LISTED UNRESOLVED WITH THEIR REASONS (not cut): %d' % n_unact)
    n_cut = len([b for b in J if b.get('kept') is not None])
    files = sorted(set(b['file'] for b in J if b.get('kept') is not None))
    L.append('### ### **PARENT BLOCKS %d ; SENTENCE ROWS %d ; GRADED %d (%s) ; MATCHES %d ; UNRESOLVED BLOCKS %d (%s) ; UNRESOLVED-CELL %d ; '
             'NOT FOUND AT MAIN %d (UNRESOLVED-NO-CELL %d) ; BLOCKS TO CUT %d IN %d FILES ; REPEATS DROPPED BY THE RULE %d ; PLAIN-COMMENT ROWS %d.**' % (
                 len(J), n_rows, n_graded, ', '.join('%s %d' % kv for kv in sorted(by_v.items())), n_rows - n_graded, n_unres,
                 ', '.join('#%d' % e for e in unres) or 'none', n_cell, len(unread), len(unread), n_cut, len(files), n_drop, len(pl.get('hits') or [])))
    put_txt('b664_sentence_grades.txt', L)
    put_json('b664_sentence_cut_plan.json', dict(at=utc(), blocks=J))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE CUT PLANNED ON THE BLOBS (b655's, b662's, carried)
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


def _emph_parity(t):
    """per comment block: the parity of `**` and of a lone `*` (b657's defect (a), b658's repair: a cut must not unbalance emphasis). A lone `*`
    with whitespace on both sides (a multiplication, `2 * S`) opens and closes nothing in CommonMark and is not counted."""
    out = []
    for m in re.finditer(r'/-.*?-/', t, re.S):
        b = m.group(0)
        out.append((t[:m.start()].count(NL) + 1, b.count('**') % 2, len(re.findall(r'(?<!\*)(?<!\s)\*(?!\*)|(?<!\*)\*(?!\*)(?!\s)', b)) % 2))
    return out


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
    """(R274)(5): the cut planned on the kernel's main blobs at K_MAIN, b655's planner: every row of a graded block located in order in its file by
    its whitespace-collapsed text from the block's line at main; each changed row replaced in its span by its slot's kept output, wrapped at the
    line's indent; one edit per block. The planned file checked: its comment-stripped code equal to main's; the emphasis parity of every comment
    block unmoved."""
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
    emph_bad = [f for f in files if [x[1:] for x in _emph_parity(files[f])] != [x[1:] for x in _emph_parity(planned[f])]]
    L = ['b664 -- COMPONENT 3, (R274)(5): THE CUT PLANNED ON %s`S MAIN BLOBS AT %s (%s)' % (K.KERNEL, K.K_MAIN, utc()), '',
         '### from relay data/b664_sentence_grades.txt (rows are sentences, parents are blocks) and its hand grades; each graded block`s rows located in',
         '### order in its file from the block`s line at main; each changed row replaced in its span by its slot`s kept output, wrapped at the line`s',
         '### indent; one edit per block.',
         '### files %d ; edits %d ; rows located %s ; regions not unique %s ; files whose comment-stripped code differs from main`s %s ; files whose '
         'comment blocks` emphasis parity moves %s' % (
             len(files), len(edits), 'ALL' if not [x for x in fails if 'not found' in x] else fails,
             [x for x in fails if 'unique' in x] or 'NONE', code_bad or 'NONE', emph_bad or 'NONE'), '']
    for e in edits:
        L += ['== #%d %s:%d (rows changed %s)' % (e['k'], e['file'], e['line'], ', '.join('s' + n for n in e['changed'])),
              '   OLD: ' + e['old'].replace(NL, ' | ')[:1600], '   NEW: ' + e['new'].replace(NL, ' | ')[:1600], '']
    L += ['### ### **FILES %d ; EDITS %d ; LOCATION FAILURES %d ; CODE OUTSIDE COMMENTS CHANGED IN %d FILES ; EMPHASIS PARITY MOVED IN %d FILES.**' % (
        len(files), len(edits), len(fails), len(code_bad), len(emph_bad))]
    put_txt('b664_cut_plan.txt', L)
    put_json('b664_cut_edits.json', dict(at=utc(), main=K.K_MAIN, edits=edits, planned_sha={f: __import__('hashlib').sha256(t.encode('utf-8')).hexdigest()
                                                                                           for f, t in planned.items()}, fails=fails, code_bad=code_bad,
                                         emph_bad=emph_bad))
    print(NL.join(L[5:6] + L[-1:]))


def _planned(f):
    j = jl('b664_cut_edits.json')
    t = (_show(K.KD, j['main'], f) or '').replace(chr(13), '')
    for e in [x for x in j['edits'] if x['file'] == f]:
        t = t.replace(e['old'], e['new'], 1)
    return t


def planned_text(*a):
    """`planned_text <file>`: prints the planned text of a cut file whole, for the seat to read before writing it by the Edit tool."""
    sys.stdout.write(_planned(a[0]))


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
    """every graded row of the grade bank looked for in its file at `ref`, whitespace aside: standing or gone, by its verdict; gone when its
    sentence occurs fewer times in the file at `ref` than at main (b657's defect (b)); at main itself every graded row stands."""
    import collections
    G = jl(K.GRADES)
    files, mains, standing = {}, {}, []
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
                cnt['CUT'] += 1
    return cnt, standing


def cut_bank(*a):
    """(R274)(5): data/b664_cut_<kernel>.txt -- the branch, its commits one per file, each head blob against the plan and its comment-stripped code
    against main's, printed per file, and the grade bank re-run at the branch with its control at main; the cut files listed (file_list) for
    (R274)(4)'s read."""
    gk = lambda *x: g(K.KD, *x)   # noqa: E731
    log = [l.split(' ', 1) for l in gk('log', '--reverse', '--format=%h %s', K.K_MAIN + '..' + K.CUT_BRANCH).split(NL) if l.strip()]
    plan = jl('b664_cut_edits.json')
    pf = sorted(set(e['file'] for e in plan['edits']))
    rows, bad, extra, flist = [], [], [], []
    for h, s in log:
        fs = [x for x in gk('show', '--name-only', '--format=', h).split(NL) if x.strip()]
        f = fs[0] if len(fs) == 1 else None
        if f is None:
            bad.append('%s touches %d files' % (h, len(fs)))
            continue
        if f not in pf:
            extra.append((h, f))
            continue
        flist.append(f)
        head = _show(K.KD, K.CUT_BRANCH, f) or ''
        main = (_show(K.KD, K.K_MAIN, f) or '').replace(chr(13), '')
        eq, code = head == _planned(f), _code_only(head) == _code_only(main)
        if not (eq and code):
            bad.append(f)
        ks = [e['k'] for e in plan['edits'] if e['file'] == f]
        rows.append('  %s  %-48s blocks %-22s blob %s ; the comment-stripped diff against main %s' % (
            h, f, ', '.join('#%d' % k for k in ks), 'EQUALS THE PLAN' if eq else '### DIFFERS', 'EMPTY' if code else '### NOT EMPTY'))
    after, st = _regrade(K.CUT_BRANCH)
    ctl, st0 = _regrade(K.K_MAIN)
    L = ['b664 -- COMPONENT 3, (R274)(5): %s`S DOCSTRINGS CUT ON THE BRANCH %s (%s)' % (K.KERNEL, K.CUT_BRANCH, utc()), '',
         '### the grades: relay data/b664_sentence_grades.txt (rows are sentences, parents are blocks; the author`s word at Component 2); the plan:',
         '### data/b664_cut_plan.txt; one commit per file by the Edit tool, each working file checked against the plan before its commit; the',
         '### branch from main %s.' % K.K_MAIN, '',
         '### THE COMMITS (rows are commits, one per file):'] + rows + [
         '### the branch`s other commits (not a cut file, each touching one file): %s' % (['%s %s' % x for x in extra] or 'NONE'),
         '', '### COMMITS %d ; FILES IN THE PLAN %d ; CUT COMMITS TOUCHING ONE FILE %d ; FAULTS %s' % (len(log), len(pf), len(rows), bad or 'NONE'),
         '', '### THE GRADE BANK RE-RUN AT THE BRANCH (each graded row looked for in its file, whitespace aside):',
         '  ' + ', '.join('%s %d' % kv for kv in sorted(after.items())),
         '  graded rows still standing: %s' % (['#%d %s s%s %s' % x[:4] for x in st] or 'NONE'),
         '### THE CONTROL, the same read at main %s: ' % K.K_MAIN + ', '.join('%s %d' % kv for kv in sorted(ctl.items())), '',
         '### THE KERNEL FILES OF THIS ACT ((R274)(4), read by the suite and the scorer from this bank): %s' % (flist or 'NONE'), '',
         '### ### **CUT COMMITS %d IN %d FILES ; GRADED ROWS CUT %d ; STANDING %d (OVERREACHES %d, UNDERSTATES %d, UNLICENSED %d) ; AT MAIN STANDING %d ; '
         'FAULTS %d.**' % (len(rows), len(pf), after.get('CUT', 0), len(st), after.get('OVERREACHES (STANDING)', 0), after.get('UNDERSTATES (STANDING)', 0),
                           after.get('UNLICENSED (STANDING)', 0), len(st0), len(bad))]
    put_txt('b664_cut_%s.txt' % K.KERNEL, L)
    put_json('b664_cut_%s.json' % K.KERNEL, dict(at=utc(), commits=[x[0] for x in log], cut_commits=len(rows), extra=[list(x) for x in extra], files=len(pf),
                                                file_list=flist, faults=bad, after=dict(after), standing=[list(x) for x in st], control=dict(ctl),
                                                control_standing=len(st0)))
    print(NL.join(L[-10:]))


# ================================================================================ COMPONENT 3: THE RUNNER, (R274)(5) under (R263)(4)
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
ERR_RE = re.compile(r'^(?:error: )?(\S+\.lean):(\d+):(\d+): error: (.*)$', re.M)
README_CLAIMS = (('README.md :28', '"Axiom-free; core Lean only, no Mathlib, no `native_decide`" (the ExhaustivenessLicense paragraph)',
                  lambda n: n.startswith('SIDEEffects.ExhaustivenessLicense.'), lambda ax: ax == []),
                 ('README.md :103', '"0 axioms beyond ZFC throughout"', lambda n: True, lambda ax: set(ax) <= STD3))


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def runner(*a):
    """`runner <run id> <ref> <workflow commit> <push run id>`: the run read by its id; the artifact listed, downloaded by its id into memory,
    its sha256 against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP; every
    print of print_targets.txt at the ref read at the standard three or none with no sorryAx (the author's word: the gate's reference); the
    prints banked as SIDE-effects' first relay print bank (data/b664_prints_SIDE-effects.txt), the reference from here; the README's two axiom
    sentences checked against them, a contradiction listed as a row for the kernel's cell refresh; the push-triggered build.yml run read and
    banked beside, not the one dispatch. Banked as data/b664_runner_<kernel>.txt and a row of data/b664_runner_rows.json."""
    import hashlib
    import zipfile
    import b569_record as R9
    run_id, ref, wfc, push_run = int(a[0]), a[1], a[2], int(a[3])
    kern = K.KERNEL
    repo = 'psinary-sketch/' + kern
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('run', 'view', str(push_run), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    prun = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    wf = _show(K.KD, wfc, '.github/workflows/build-module.yml') or ''
    pt = [l.strip() for l in (_show(K.KD, ref, 'print_targets.txt') or '').split(NL) if l.strip()]
    kf = read_kernel_files()
    row = dict(kernel=kern, branch=K.CUT_BRANCH, ref=ref, target=K.TARGET, run_id=run_id, conclusion=run.get('conclusion'),
               artifact_sha256=None, mem_low=None, stopped=False, gate=None, merged=None, tag=None)
    L = ['b664 -- COMPONENT 3, (R274)(5): THE HOSTED RUNNER FOR %s, READ BY ITS RUN ID (%s)' % (kern, utc()), '',
         '### (R274)(4): the act`s kernel files, read from its cut bank and from no constant: %s' % '; '.join('%s (from %s)' % (f, ', '.join(b)) for f, b in kf),
         '### the workflow file on main (%s, put where absent under (R263)(4), the file alone, SIDE-explicit-formula`s b654 form unchanged), read back whole:' % wfc] + \
        ['    ' + l for l in wf.rstrip(NL).split(NL)] + ['', '### print_targets.txt at the ref: %d names' % len(pt), '',
         '### the one dispatch: at main, the ref input %s (the cut branch`s tip, rebased onto the workflow`s main before it was pushed) ; target %s' % (ref, K.TARGET),
         '### the run: id %s ; %s ; %s %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('workflowName'), run.get('event'), run.get('status'), run.get('conclusion'), run.get('headSha'),
             run.get('headBranch'), run.get('createdAt'), run.get('updatedAt')),
         '### BESIDE IT, NOT THE ONE DISPATCH (the author`s word): the push-triggered build.yml run on the workflow`s push to main: id %s ; %s %s ; '
         'conclusion %s ; head %s ; %s to %s' % (push_run, prun.get('workflowName'), prun.get('event'), prun.get('conclusion'), prun.get('headSha'),
                                                 prun.get('createdAt'), prun.get('updatedAt'))]
    T_ = {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        row['artifact_sha256'] = sha
        L.append('### the artifact: id %s ; name %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN',
            'AGREE' if digest and digest == sha else ('### DIFFER' if digest else 'no digest to compare -- NOTHING READ FROM IT')))
        if not digest or digest != sha:
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
    P = dict((k_, sorted(v_)) for k_, v_ in R9.prints_axioms(T_.get('axioms.txt', '')).items())
    axerr = [l for l in T_.get('axioms.txt', '').split(NL) if ': error' in l]
    per = [(n, P.get(n)) for n in pt]
    missing = [n for n, ax in per if ax is None]
    std = [(n, ax is not None and set(ax) <= STD3 and 'sorryAx' not in ax) for n, ax in per]
    claims = []
    for where, what, scope, ok_ in README_CLAIMS:
        rows_ = [(n, ax) for n, ax in per if ax is not None and scope(n)]
        bad = [n for n, ax in rows_ if not ok_(ax)]
        claims.append((where, what, len(rows_), bad))
    ok = (run.get('conclusion') == 'success' and row['artifact_sha256'] and bexit == '0' and not errs and not stops and row['mem_low'] is not None
          and row['mem_low'] >= K.HOLD and len(pt) > 0 and not missing and not axerr and all(s for _n, s in std))
    row['gate'] = 'DERIVES' if ok else ('STOPPED BENEATH THE HOLD' if stops else 'NOT DERIVES')
    row['errors'] = [list(e) for e in errs]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: samples %d ; LOW %s MB ; the hold %d ; STOP lines %s' % (
              len([l for l in mem.split(NL) if 'avail_mb=' in l]), row['mem_low'], K.HOLD, stops or 'NONE'),
          '### the build: exit %s ; error lines %d ; the log`s last lines:' % (bexit or '### UNREAD', len(errs))] + \
        ['    ' + l for l in blog.rstrip(NL).split(NL)[-6:]] + ['    %s:%d:%d: %s' % e for e in errs[:30]] + [
          '### the print step: error lines %d%s ; names refused %s' % (len(axerr), (' -- ' + ' | '.join(axerr[:4])) if axerr else '',
                                                                       T_.get('axioms_refused.txt', '').strip() or 'NONE'),
          '### THE GATE READING PER TERMINAL (the author`s word: each print at the standard three or none, no sorryAx; the prints banked here as '
          'the kernel`s first relay print bank, relay data/b664_prints_SIDE-effects.txt):'] + \
        ['  %-62s %-38s %s' % (n, ax if ax is not None else '### NOT PRINTED', 'STANDARD THREE OR NONE' if s else '### NOT') for (n, ax), (_n, s) in zip(per, std)] + \
        ['', '### THE README`S AXIOM SENTENCES AGAINST THE PRINTS (axiom claims of the G-AXIOM-CLAIM kind; a contradiction a row for the kernel`s '
         'cell refresh, not the gate):'] + \
        ['  %s %s -- prints in scope %d ; contradicted by %s' % (w, wh, n_, bad or 'NONE') for w, wh, n_, bad in claims] + [
          '', '### ### **RUN %s ; CONCLUSION %s ; ARTIFACT SHA256 %s ; MEMORY LOW %s MB (HOLD %d) ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS %d, PRINTED %d, '
          'AT THE STANDARD THREE OR NONE %d ; README AXIOM SENTENCES CONTRADICTED %d ; GATE %s.**' % (
              run_id, run.get('conclusion'), (row['artifact_sha256'] or '### NONE')[:16], row['mem_low'], K.HOLD, bexit or '### UNREAD', len(errs),
              len(pt), len(pt) - len(missing), sum(1 for _n, s in std if s), sum(1 for c in claims if c[3]), row['gate'])]
    put_txt('b664_runner_%s.txt' % kern, L)
    PL = ['b664 -- %s`S RELAY PRINT BANK, THE FIRST: the hosted runner`s #print axioms at %s (run %s, artifact sha256 %s, the platform`s digest '
          'agreeing), the reference from here (the author`s word at b664) (%s)' % (kern, ref[:7], run_id, (row['artifact_sha256'] or '-')[:16], utc()), '',
          '### rows are declarations: the full name and its axioms as printed; [] = does not depend on any axioms.'] + \
        ['  %-62s %s' % (n, ax) for n, ax in per if ax is not None]
    if row['artifact_sha256']:
        put_txt('b664_prints_%s.txt' % kern, PL)
    put_json('b664_runner_rows.json', dict(rows=[row], push_run=dict(id=push_run, conclusion=prun.get('conclusion'), head=prun.get('headSha'),
                                                                     workflow=prun.get('workflowName'), event=prun.get('event')),
                                           readme_claims=[dict(where=w, scope_prints=n_, contradicted=bad) for w, _wh, n_, bad in claims],
                                           kernel_files=[f for f, _b in kf]))
    print(L[-1])
    for e in errs[:12]:
        print('  ERROR %s:%d:%d: %s' % e)


def runner_merged(*a):
    """`runner_merged <merge sha> <tag> [<push run id>]`: the row's merge and tag, after main and the tag are read back at the remote; the
    push-triggered build.yml run on the merge's push read and banked beside it, not the one dispatch."""
    sha, tag = a[:2]
    j = jl('b664_runner_rows.json')
    for r in j['rows']:
        if r['kernel'] == K.KERNEL:
            r['merged'], r['tag'] = sha, tag
    j['tag_peeled'] = g(K.KD, 'rev-parse', '--short=7', '%s^{commit}' % tag).strip()
    if len(a) > 2:
        rc, out, err = _gh('run', 'view', a[2], '-R', 'psinary-sketch/' + K.KERNEL, '--json', 'status,conclusion,headSha,workflowName,event,createdAt,updatedAt')
        j['merge_push_run'] = dict(json.loads(out or b'{}'), id=int(a[2]))
    put_json('b664_runner_rows.json', j)
    print('  %s merged %s tag %s peeled %s' % (K.KERNEL, sha, tag, j['tag_peeled']))


# ================================================================================ THE LATE ROUTES (b663's, carried; every row read through READERS)
import collections                 # noqa: E402
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


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
    L = ['b664 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
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
    put_txt('b664_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b664_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])


def kernels(*a):
    import b641_record as R41
    put_json('b664_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


DEFECT_ROW = re.compile(r'^    \(([a-z]|b663-late)\) ')


def _defect_short():
    out = []
    for l in rdn('b664_defects.txt').split(NL):
        m = re.match(r'^    \(([a-z]|b663-late)\) ([^.]*)\.', l)
        if m:
            out.append(m.group(0).strip()[:-1])
    return out


def defects(*a):
    t = rdn('b664_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b664_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b664_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b664_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|mirror.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b664_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b664_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b664'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b664_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    with tempfile.TemporaryDirectory(prefix='b664_ra_') as tmp:
        cp = os.path.join(tmp, os.path.basename(bank_))
        b = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
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
    L = ['b664 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b664_root_arm.txt', L)
    put_json('b664_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b664 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b664_table_final.txt', L)
    put_json('b664_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


def gatebanks(*a):
    """the gate's steps between the face and the lock (b663's order), each tool's output banked by this route, never by a shell redirect."""
    import gate_hash as G
    env = dict(os.environ, PYTHONIOENCODING='utf-8')

    def runb(args, out):
        r = subprocess.run([sys.executable] + args, capture_output=True, cwd=ROOT, env=env)
        b = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            open(p + '.tmp', 'wb').write(b)
            os.replace(p + '.tmp', p)
        return r.returncode, b.decode('utf-8', 'replace')
    face_rel = 'data/b664_registration_2026-10-13.txt'
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', face_rel], 'b664_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b664_regspec.py')], 'b664_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b664_satisfiable.json', '--emit', 'b664'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b664_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b664_census_stepzero.txt'), ('b327_faces_census.py', 'b664_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b664_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b664'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    fa = os.path.join(ROOT, *face_rel.split('/'))
    for r in ('data/b664_reg_gate.txt', 'data/b664_reg_termscan.txt', 'data/b664_regspec_run.txt', 'data/audit_b664_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, fa)[:16], G.matches(ra, fa)[0]))


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b663_closing_push_out.txt')
N5_RELAY_TOOLS = ('test_met_b646.py',)        # ### the tool edit of the act and its test, on the author's word
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
FACE = os.path.join(D, 'b664_registration_2026-10-13.txt')


def TRAIL_HEAD():
    return ('### b664 — lane three, act ninety-one, the re-cut act under (R274): b663 at its weight; the two orders placed; the suite’s file '
            'constant made a bank read; SIDE-effects’ sentences graded, cut, built on the runner and merged; the mirror export')


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime((s or '')[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None


def _calls():
    return jl('b664_author_answers.json').get('calls') or []


def _ct_first(repo, pre, prefix=None):
    """the commit time of the first commit in `repo` after `pre` (whose subject opens with `prefix`, if given)."""
    for l in g(repo, 'log', '--reverse', '--format=%ct %s', pre + '..HEAD' if repo == RELAY else pre + '..main').split(NL):
        if l.strip() and (prefix is None or l.split(' ', 1)[1].startswith(prefix)):
            return int(l.split(' ', 1)[0])
    return None


def _first_kernel_ct():
    """the first kernel byte of the act: the first commit on the cut branch or on the kernel's main after K_MAIN."""
    ts = []
    for ref in (K.CUT_BRANCH, 'main'):
        for l in g(K.KD, 'log', '--reverse', '--format=%ct', '%s..%s' % (K.K_MAIN, ref)).split(NL):
            if l.strip():
                ts.append(int(l))
                break
    return min(ts) if ts else None


def _n2():
    import b664_checks as CH
    cc = rdn(K.CITATION_BANK)
    m = re.search(r'CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', cc)
    aj = _calls()
    first_ans = _iso(aj[0].get('result_ts')) if aj else None
    grades_ans = _iso(aj[1].get('result_ts')) if len(aj) > 1 else None
    c1 = _ct_first(RELAY, K.PRE_RELAY, 'b664 Component 1')
    kct = _first_kernel_ct()
    n, bad = CH.verbatim()
    ok = (m is not None and (int(m.group(3)) == 0 or (first_ans and c1 and first_ans < c1)) and n > 0 and bad == []
          and grades_ans and kct and grades_ans < kct)
    return ('HELD' if ok else 'REFUTED'), (
        'the citation check (relay data/%s): %s, its miss answered at %s before Component 1`s first commit (%s); the graded rows read again '
        'against their cells: %d, not verbatim %s; the first kernel byte (%s) after the author`s word on the grades (%s)' % (
            K.CITATION_BANK, m.group(0) if m else '### UNREAD', time.strftime('%H:%M:%SZ', time.gmtime(first_ans)) if first_ans else '?',
            time.strftime('%H:%M:%SZ', time.gmtime(c1)) if c1 else '?', n, bad or 'NONE',
            time.strftime('%H:%M:%SZ', time.gmtime(kct)) if kct else '?', time.strftime('%H:%M:%SZ', time.gmtime(grades_ans)) if grades_ans else '?'))


def _n3():
    cb = jl('b664_cut_%s.json' % K.KERNEL)
    rr = (jl('b664_runner_rows.json').get('rows') or [{}])[0]
    rt = rdn('b664_runner_%s.txt' % K.KERNEL)
    eq = re.search(r'TERMINALS (\d+), PRINTED (\d+), AT THE STANDARD THREE OR NONE (\d+)', rt)
    prints_ok = bool(eq) and eq.group(1) == eq.group(2) == eq.group(3) and int(eq.group(1)) > 0 and os.path.exists(os.path.join(D, 'b664_prints_%s.txt' % K.KERNEL))
    a_ = cb.get('after') or {}
    ok = (cb and not cb.get('standing') and not cb.get('faults') and not a_.get('OVERREACHES (STANDING)') and not a_.get('UNLICENSED (STANDING)')
          and 'the comment-stripped diff against main EMPTY' in rdn('b664_cut_%s.txt' % K.KERNEL) and prints_ok and rr.get('gate') == 'DERIVES')
    return ('HELD' if ok else 'REFUTED'), (
        'the grade bank re-run at the branch: %s, standing %d; every cut file`s comment-stripped diff against main empty, faults %s; the runner`s '
        'prints %s, banked as the kernel`s first relay print bank -- the profile they equal is their own, on the author`s word (no earlier bank); '
        'gate %s, merged %s tag %s' % (dict(a_), len(cb.get('standing') or []), cb.get('faults') or 'NONE', eq.group(0) if eq else '### UNREAD',
                                       rr.get('gate'), rr.get('merged'), rr.get('tag')))


def _n4():
    import b664_checks as CH
    kf = read_kernel_files()
    pr = rdn('b664_arms_prerun.txt')
    printed = '### (R274)(4) THE KERNEL FILES, READ FROM THE CUT BANK:' in pr and all(f in pr for f, _b in kf)
    nconst = [f for f in ('b664_worklist.py', 'b664_record.py', 'b664_checks.py') if re.search(r"^\w+\s*=\s*'SIDEEffects/[^']+\.lean'", rd(os.path.join(T, f)), re.M)]
    ok = bool(kf) and printed and not nconst and CH.kernel_files_read() == [f for f, _b in kf]
    return ('HELD' if ok else 'REFUTED'), (
        'the kernel files read from the cut bank, not a constant: %s; printed by the suite before the seal (relay data/b664_arms_prerun.txt) %s; '
        'a constant naming a kernel .lean file in the act`s tools: %s; this score written by the sealed record tool directly, no scratch driver' % (
            '; '.join('%s (%s)' % (f, ', '.join(b)) for f, b in kf), printed, nconst or 'NONE'))


def _n5():
    face = jl('b664_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    others_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b664_|audit_b664_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA)
                                                or (x.startswith('tools/') and x[6:] in N5_RELAY_TOOLS))]
    km = [l for l in g(K.KD, 'log', '--first-parent', '--format=%h %p', K.K_MAIN + '..main').split(NL) if l.strip()]
    km_ok = [l.split()[0] for l in km] == [K.MERGE, K.K_WORKFLOW] and len(km[0].split()) == 3
    k_files = sorted(x for x in g(K.KD, 'diff', '--name-only', K.K_MAIN, 'main').split(NL) if x.strip())
    want_k = sorted(['.github/workflows/build-module.yml', 'print_targets.txt'] + [f for f, _b in read_kernel_files()])
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b664_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    ok = others_ok and not pp_beyond and not kinds_beyond and not differ and km_ok and not new_arms and k_files == want_k
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unsubmitted); %s`s main written by the workflow where absent under '
            '(R263)(4) and the one merge under Component 3 alone (first-parent commits since %s: %s ; %s), its files against %s: %s (the kernel '
            'files read from the cut bank); every kernel as the face read it %s; standing arms added: %s (the act`s arms over its own banks %d); '
            'sealed tools not agreeing %s; PLACE-papers beyond FINDINGS and OPEN_TRAILS: %s; relay files of a kind beyond the banks, the tools, '
            'the root list, b663`s push-out bank and the tool edit with its test (tools/test_met_b646.py): %s; the mirror export outside every '
            'tree; no identifier of the author in any outbound request (git pushes, remote reads, the runner`s dispatch with a ref and a target, '
            'the artifact`s download)' % (
                K.DRAFT, K.KERNEL, K.K_MAIN, [l.split()[0] for l in km], 'AS RULED' if km_ok else '### OTHERWISE', K.K_MAIN, k_files, others_ok,
                new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE'))


def scores(*a):
    TF, RA = jl('b664_table_final.json'), jl('b664_root_arm.json')
    _r, _n, sh = seal_hashes()
    cm = jl('b664_commands.json')
    print('  (R274)(4): the kernel files, read from the cut bank: %s' % read_kernel_files())
    S = {
        'N1': (('HELD' if cm and not cm.get('local_lean') else 'REFUTED'),
               'commands of this act that run lean or lake on this host: %s (relay data/b664_commands.txt); the build on the hosted runner alone' % (
                   cm.get('local_lean') if cm else '### UNREAD')),
        'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    put_json('b664_scores.json', dict((k2, list(v)) for k2, v in S.items()))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:500]))


NEXT_LINE = 'b665, per `(R274)`(8), the research act: the Keiper face’s finite-n equality and the transform-bound order (:14162), its ruling then'


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else '?'


def _gtot():
    m = re.search(r'SENTENCE ROWS (\d+) ; GRADED (\d+)', rdn('b664_sentence_grades.txt'))
    return (int(m.group(2)), int(m.group(1))) if m else (0, 0)


def _title():
    rr = (jl('b664_runner_rows.json').get('rows') or [{}])[0]
    cut_n = (jl('b664_cut_%s.json' % K.KERNEL).get('after') or {}).get('CUT', 0)
    return ('## SIDE-effects’ docstrings at %d sentence rows cut of %d, built on the runner and merged at %s; the two Epstein orders placed; '
            'the suite’s file constant made a bank read' % (cut_n, _gtot()[1], rr.get('tag') or 'its next tag'))


def _finding_text():
    S, rl, J = jl('b664_scores.json'), jl('b664_record_lines.json'), jl('b664_act_root.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b664_author_answers.txt'), re.M))
    ls = (rl.get('lines') or []) + [{}, {}, {}, {}]
    rr = (jl('b664_runner_rows.json').get('rows') or [{}])[0]
    cb = jl('b664_cut_%s.json' % K.KERNEL)
    gr_n, rows_n = _gtot()
    cc = re.search(r'CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    nd = jl('b664_nd_rerun.json')
    e = ['', _title(), '',
         '*Filed at b664 on the author’s ruling `(R274)` and the author’s word (%d questions in %d calls). Banks: relay '
         '`data/b664_citation_check.txt`, `data/b664_nd_rerun.txt`, `data/b664_sentence_grades.txt`, `data/b664_restated_reading.txt`, '
         '`data/b664_cut_SIDE-effects.txt`, `data/b664_runner_SIDE-effects.txt`, `data/b664_prints_SIDE-effects.txt`, `data/b664_act_root.txt`.*' % (
             n_ans, len(_calls())), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s miss -- a defects range naming a row the bank '
         'does not have -- the navigator’s on the author’s word.' % (cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?'), '',
         '**The record lines** (`(R274)`(1)-(4)): b663 at its weight with both caveats by name (FINDINGS :%s); the transform-bound order placed '
         'beside the Keiper face at b665 (OPEN_TRAILS :%s); W-ORD-EPSTEIN-CERTIFY placed as b667 (:%s); the file-constant rule entered (:%s), '
         'its step-zero reading the no-disclosure arm over %s read from b663’s instance bank, hits %d.' % (
             ls[0].get('line'), ls[1].get('line'), ls[2].get('line'), ls[3].get('line'), nd.get('file', '?'), sum((nd.get('hits') or {}).values())), '',
         '**The kernel** (`(R274)`(5)): SIDE-effects, 7 OVERREACHES in relay `data/b647_table_kernels.txt` :10, read at ef4cff7; its main moved '
         'since by b648’s restatement of Milestones.lean, so the five Milestones blocks are not found at main -- UNRESOLVED-NO-CELL, listed for '
         'the kernel’s cell refresh with the seat’s hand reading beside them as a reading, not a grade; the two ExhaustivenessLicense.lean '
         'blocks read at main into %d sentence rows.' % rows_n, '',
         '**The grades** (`(R274)`(5) and the author’s word): %d rows graded OVERREACHES by hand, the cell’s words beside each, verbatim; '
         'each graded pair replaced by its block’s ACTION, the second copy dropped as a repeat; none UNRESOLVED among the blocks read. N2 %s.' % (
             gr_n, _sv(S, 'N2')), '',
         '**The cut and the runner** (`(R274)`(5)): %d graded rows cut in %d commit, the file’s comment-stripped diff against main empty, none '
         'standing at the branch; the workflow put on main where absent, the cut branch rebased onto it so the merged tree is the built tree; '
         'one dispatch at main with the branch tip as the ref, run %s, the artifact’s sha256 agreeing with the platform’s digest, memory low '
         '%s MB, every print at the standard three or none and banked as the kernel’s first relay print bank, the README’s two axiom '
         'sentences not contradicted; the push-triggered builds read beside; merged alone, SIDE-effects %s tagged %s. N3 %s.' % (
             (cb.get('after') or {}).get('CUT', 0), cb.get('cut_commits'), rr.get('run_id'), rr.get('mem_low'), rr.get('merged'), rr.get('tag'),
             _sv(S, 'N3')), '',
         '**The file constant** (`(R274)`(4)): the suite and the scorer read this act’s kernel files from the cut bank, the read printed before '
         'the seal; no constant names a kernel file; no scratch driver set a file name. N4 %s.' % _sv(S, 'N4'), '',
         '**The root.** b664 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b663’s record and its defect (o), b647’s block bank for '
         'SIDE-effects against b648’s restatement, and b646’s MET test after b663’s ruled line; it is re-read by the kernel’s cell refresh and '
         'by b665. It strengthens the programme’s offering of statements a reader can check: a docstring that set a grade by hand now says so, '
         'the kernel’s prints are banked for the first time on a machine the reader can name by run id, and the suite reads the act’s files '
         'from the act’s own bank.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; a docstring cut says less, not more, and a gate reading compares '
         'a print with the standard three.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the cut branch rebased onto the workflow’s main before it was pushed, so the merged tree is the built tree; (2) the '
              'README’s "Axiom-free" read as a claim about ExhaustivenessLicense’s declarations, "0 axioms beyond ZFC" as the standard three; '
              '(3) the print list the cut file’s declarations, the other modules’ theorems and Milestones’ three Props, 34 names; (4) the '
              'answer to the cut question’s gate line read by the gate question’s own answer (no b653 bank for SIDE-effects)')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b664_scores.json', 'b664_findings.json', 'b664_record_lines.json', 'b664_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b664_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}, {}, {}]
    mj = jl('b664_mirror.json')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R274) ratified.** (1) b663 at its weight, its late defect at step zero. (2) What b663 says, its caveats by name. (3) The two orders '
             'placed. (4) The suite’s file constant made a bank read. (5) The kernel: SIDE-effects, graded, cut, built, merged. (6) The mirror '
             'export. (7) The draft held at v5. (8) The act after: b665.', '',
             '**Entered:** FINDINGS.md:%s (b663’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the transform-bound order placed), :%s '
             '(W-ORD-EPSTEIN-CERTIFY placed), :%s (the file-constant rule); this record.' % (ls[0].get('line'), fj.get('entry_line'), ls[1].get('line'),
                                                                                        ls[2].get('line'), ls[3].get('line')), '',
             '**Act root:** b664 `%s` (previous `%s`, b663’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d calls (relay data/b664_author_answers.txt): the citation check’s miss before Component 1; '
             'the cut, the gate’s reference, the MET test and the runner and tag before any cut; none after the root.' % (n_ans, len(_calls())), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**The mirror:** %s, MANIFEST md5 %s.' % (mj.get('zip', 'built after this record'), mj.get('manifest_md5', '-')), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b664_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b664_scores.json')
    L = ['=' * 104, 'b664 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b664_defects.txt').rstrip(NL).split(NL)
    put_txt('b664_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b664_scores.json', 'b664_findings.json', 'b664_trail.json', 'b664_record_lines.json', 'b664_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}, {}, {}, {}]
    j = jl('b664_runner_rows.json')
    rr = (j.get('rows') or [{}])[0]
    L = ['b664 -- THE COMPONENTS, BANKED UNDER (R274).', '',
         '### COMPONENT 0 : the citation check (data/b664_citation_check.txt), step zero (data/b664_ferry.txt, data/b664_stepzero.txt, '
         'data/b664_tests_stepzero.txt, data/b664_nd_rerun.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : b663`s weight FINDINGS :%s ; the orders placed OPEN_TRAILS :%s, :%s ; the file-constant rule :%s' % (
             ls[0].get('line'), ls[1].get('line'), ls[2].get('line'), ls[3].get('line')),
         '### COMPONENT 2 : the grades (data/b664_table_SIDE-effects_sentences.txt, data/b664_sentence_grades.txt, data/b664_restated_reading.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the cut and the runner (data/b664_cut_SIDE-effects.txt, data/b664_runner_SIDE-effects.txt, data/b664_prints_SIDE-effects.txt) ; '
         'the workflow %s ; run %s ; merged %s tag %s ; the MET test made durable (data/b664_tests_met_before.txt, _met_after.txt) ; N3 %s' % (
             K.K_WORKFLOW, rr.get('run_id'), rr.get('merged'), rr.get('tag'), S['N3'][0]),
         '### COMPONENT 4 : the dry-run step (data/b664_reg_gate.txt), the seal (data/b664_seal_hashes.json), the suite, its kernel files from the cut '
         'bank ; N4 %s ; S3 %s' % (S['N4'][0], S['S3'][0]),
         '### COMPONENT 5 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; the mirror ; N1 %s ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N1'][0], S['N5'][0])]
    put_txt('b664_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b664_findings.json', dict(title=t))
    j = jl('b664_findings.json')
    j['entry_line'] = ln
    put_json('b664_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b664_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written (B664_STANDIN) -- converted by conv and run through the screens their landing runs, the needles the face
    names read in each; prints DRY-RUN STEP : CLEAN and exits 0 only when both screens are quiet and every needle is found. Writes no bank."""
    face = rd(a[0] if a else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = conv(text)
        print('  %s (the screens):' % which)
        cells, fired = screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = _face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells and not fired and nd and not miss
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


# ================================================================================ THE MIRROR, AT THE CLOSE ((R274)(6); b662's routes, carried)
import hashlib as _hl   # noqa: E402

MIRROR_TAG = '2026-10-13-b664'
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
    put_json('b664_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b664':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b664`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b664_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b664_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b664_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b664 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b664_mirror.txt', L)
    put_json('b664_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:8]:
        print(l[:240])


ROUTES = {'nd_rerun': nd_rerun, 'c1': c1, 'answers': answers, 'sentences': sentences, 'plain': plain, 'grades': grades, 'plan_cut': plan_cut,
          'planned_text': planned_text, 'check_file': check_file, 'cut_bank': cut_bank, 'runner': runner, 'runner_merged': runner_merged,
          'commands': commands, 'kernels': kernels, 'defects': defects, 'root': root, 'root_arm': root_arm, 'table_final': table_final,
          'gatebanks': gatebanks, 'scores': scores, 'desk': desk, 'components': components, 'findings': findings, 'trail': trail,
          'drycheck': drycheck, 'mbuild': mbuild, 'mroot': mroot, 'mverify': mverify, 'mbank': mbank}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b664_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
