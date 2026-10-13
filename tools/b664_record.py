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


ROUTES = {'nd_rerun': nd_rerun, 'c1': c1, 'answers': answers, 'sentences': sentences, 'plain': plain, 'grades': grades, 'plan_cut': plan_cut,
          'planned_text': planned_text, 'check_file': check_file, 'cut_bank': cut_bank, 'runner': runner, 'runner_merged': runner_merged}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b664_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
