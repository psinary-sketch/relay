# -*- coding: utf-8 -*-
"""b692_record.py -- THE ACT'S RECORD TOOL, b692 under (R302).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b692's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b691_record.py in stages: the helpers, the guarded landing, the readers, step zero's rowgen and branches
### routes and the answers route first; Component 1's weight line at Component 1; the late routes at Component 5. Every python child is
### started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b692_record.py <route> [dry]`. After the seal this tool's
### own print is how the entry, the dry entry and the trail are read (data/b690_rules.txt row (1)); no commit is amended after the seal
### (data/b692_rules.txt row (1)).
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
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported
import b692_worklist as K          # noqa: E402

SP = K.SP
STANDIN = 'standin' in sys.argv[2:]          # ### the dry-run step's stand-ins, by argument (environment variables left as they are)
RELAY = ROOT


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
        'b692_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b692_findings.json': dict(entry_line=99999, title='stand-in'),
        'b692_trail.json': dict(line=99999),
        'b692_act_root.json': dict(root='0' * 64, previous='7b052f8b' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return _standins().get(name, {}) if STANDIN else {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def grc(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').returncode


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b692's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b692_scanfile_%s.md' % tag)
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
def read_score_row(k, v):
    """a scores row: key N1..N5 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text)."""
    if not re.match(r'^(N[1-5]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


BRANCH_FATES = ('DELETED', 'KEPT', 'RAISED')


def read_branch_row(r):
    """a row of data/b692_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


def read_runner_row(r):
    """a row of data/b692_runner_rows.json: the kernel, its label, the ref (40 hex), the run id and the gate; returns (kernel, label, gate)."""
    if not isinstance(r, dict) or not re.match(r'^SIDE-[\w-]+$', r.get('kernel') or '') or not re.match(r'^[\w-]+$', r.get('label') or '') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['kernel'], r['label'], r['gate']


READERS = ['read_score_row', 'read_head', 'read_branch_row', 'read_runner_row']


# ================================================================================ STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE (b670's route, carried)
def roster():
    """the 19 roster tables of data/b586_corroboration.txt :34, at the paths that bank read (carried from b670_record.py :548-:552)."""
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b692_rowgen_<stage>.txt."""
    stage = a[0] if a and a[0] not in ('dry',) else 'stepzero'
    R = roster()
    paths = [os.path.join(PP, p) for _n, p in R]
    miss = [p for p in paths if not os.path.exists(p)]
    if len(R) != 19 or miss:
        sys.exit('### THE ROSTER IS NOT 19 PATHS AT HEAD: %d, missing %s' % (len(R), miss))
    t0 = time.time()
    con = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'rowgen', 'rowgen.py'), 'constellation', PP] + paths,
                         capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=500)
    dif = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'rowgen', 'diff_rowpin.py'), os.path.join(T, 'rowgen', 'namemap.json')] + paths,
                         capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=500)
    secs = int(time.time() - t0)
    co, do = (con.stdout or '') + (con.stderr or ''), (dif.stdout or '') + (dif.stderr or '')
    tail = lambda t: [l for l in t.replace(chr(13), '').split(NL) if l.strip()][-12:]   # noqa: E731
    L = ['b692 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b692_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R302)(6))
KERNEL_BRANCHES = (('D:/SIDE-rcurve', 'push-b691-main', 'local'), ('D:/SIDE-rcurve', 'push-b691-merge', 'local'),
                   ('D:/SIDE-rcurve', 'recut-rcurve-b691', 'local'), ('D:/SIDE-rcurve', 'recut-rcurve-b691', 'remote'),
                   ('D:/SIDE-explicit-formula', 'push-b691-epstein-main', 'local'), ('D:/SIDE-explicit-formula', 'push-b691-epstein-merge', 'local'),
                   ('D:/SIDE-explicit-formula', 'recut-epstein-b691', 'local'), ('D:/SIDE-explicit-formula', 'recut-epstein-b691', 'remote'))
KERNEL_BRANCH_SOURCES = 'data/b691_cut.txt :5 (recut-rcurve-b691), data/b691_epstein_cut.txt :23, data/b691_closing.txt :240-:242'


def branches(*a):
    """every branch (R302)(6) names for step zero, its tip read before any delete, its fate; the kernel branches b691 made, listed for the
    one prompt (fate RAISED until the author's word); any branch of b691 that --merged lists and the ruling does not name, reported and
    KEPT. data/b692_branches.txt (.json). The remote tips are read from the remote-tracking refs (no ls-remote here)."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    krows = []
    for repo, b, where in KERNEL_BRANCHES:
        ref = ('refs/heads/' if where == 'local' else 'refs/remotes/origin/') + b
        tip = g(repo, 'rev-parse', '--verify', '--quiet', ref).strip()
        merged = grc(repo, 'merge-base', '--is-ancestor', ref, 'main') == 0
        krows.append(dict(repo=repo, branch=b, where=where, tip=tip, merged=merged, fate='RAISED'))
    named = set((r['repo'], r['branch']) for r in rows + krows)
    extra = []
    for repo in sorted(set([r_ for r_, _bs in K.DELETE] + [r_ for r_, _b, _w in KERNEL_BRANCHES])):
        for x in g(repo, 'branch', '--merged', 'main', '--format=%(refname:short)').split(NL):
            x = x.strip()
            if (x.startswith('push-b691') or x.endswith('-b691')) and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows + krows:
        read_branch_row(r)
    L = ['b692 -- STEP ZERO, (R302)(6): THE BRANCHES THE RULING NAMES AND THE KERNEL BRANCHES b691 MADE, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; merged into main ; fate. The five named deleted by name in the house',
         '### form, each delete command naming one branch with no glob in any half, one command per message, in sequence; the kernel branches',
         '### raised as one prompt with the names verbatim (%s), deleted on the author`s word and not before.' % KERNEL_BRANCH_SOURCES, '',
         '### THE FIVE (R302)(6) NAMES:']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### THE KERNEL BRANCHES b691 MADE (the remote rows read from the remote-tracking ref):']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in krows]
    L += ['', '### branches of b691 that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **NAMED %d (MERGED %d) ; KERNEL BRANCHES %d (MERGED %d), RAISED ; UNNAMED OF b691 %d.**' % (
        len(rows), sum(1 for r in rows if r['merged']), len(krows), sum(1 for r in krows if r['merged']), len(extra))]
    put_txt('b692_branches.txt', L)
    put_json('b692_branches.json', dict(at=utc(), rows=rows, kernel_rows=krows, extra=[list(x) for x in extra]))
    print(NL.join(L[6:]))


# ================================================================================ THE ANSWERS BANK (b691's route, carried)
def _session_rows():
    for sid, anc in ((K.SESSION_ID, K.ANCHOR),) + K.SESSIONS_AFTER:
        start = None
        for i, raw in enumerate(io.open('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, encoding='utf-8', errors='replace'), 1):
            try:
                o = json.loads(raw)
            except ValueError:
                continue
            if start is None and anc in raw.replace('’', "'") and o.get('type') == 'user' and not o.get('isCompactSummary'):
                start = i
            if start is not None:
                yield i, o, start, sid
        if start is None and sid != K.SESSION_ID:
            sys.exit('### THE ANCHOR %r IS NOT A USER LINE OF SESSION %s -- NOTHING WRITTEN' % (anc, sid))


def answers(*a):
    """data/b692_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
    every word of the author delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim; a word opened by
    BEGIN with no END noted (b689's route)."""
    calls, results, words, plain_, start = [], {}, [], [], None
    for i, o, st, sid in _session_rows():
        start = st if sid == K.SESSION_ID else start
        ln = i if sid == K.SESSION_ID else '%s:%d' % (sid[:8], i)
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
                    plain_.append((ln, t.strip()))
        texts = [re.sub(r'(?s)^\s*<pasted_content[^>]*>\s*(.*?)\s*</pasted_content[^>]*>\s*$', r'\1', t or '') for t in texts]
        ask = set(x[1] for x in calls)
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion' and o.get('type') == 'assistant':
                calls.append((ln, c['id'], c['input'], o.get('timestamp')))
                ask.add(c['id'])
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask and o.get('type') == 'user':
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or '')
                results[c.get('tool_use_id')] = (ln, t, o.get('timestamp'))
                texts.append(t)
        for t in texts:
            for mm in re.finditer(r'(?s)(?:\A\s*|="|="\(for the seat, verbatim\):\s*)BEGIN\s*(.*?)\s*END(?=\s*\Z|")', t or ''):
                if K.ANCHOR not in mm.group(1) and 'RULING (' not in mm.group(1)[:20]:
                    words.append((ln, mm.group(1)))
    if start is None:
        sys.exit('### THE ANCHOR IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    L, n = [], 0
    for i, cid, inp, ts in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %s, %s)' % (cid, K.SESSION_ID, i, ts))
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
        W += ['### THE AUTHOR`S WORD (transcript line %s), BEGIN to END, verbatim:' % i] + w.replace('\r', '').split(NL) + ['']
    for cid, (i, t, _ts) in results.items():
        for mm in re.finditer(r'="BEGIN(?:(?!END").)*?"(?=, "|\.\s|$)', t or '', re.S):
            if not re.search(r'END"\s*$', mm.group(0)):
                W += ['### NOTE (transcript line %s): a word opened by BEGIN and carrying NO END marker -- %r ... %r; its text is the RESULT line '
                      'above.' % (i, mm.group(0)[2:80], mm.group(0)[-60:]), '']
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %s), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b692 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b692_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b692_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R302)(1)
WH = ('*Appended 2026-10-19 by b692 to b691’s entry (:9424), under `(R302)`(1) -- b691 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b691_closing.txt):*')
WB = (' “b691 closed: relay 62a530c6, PLACE-papers 9a0dc76; suite 119 of 121; root 7b052f8b5968b799…; 4 prompts answered; 11 defects” '
      '(data/b691_closing.txt :1), the closing f5318624 pushed and read back at relay main (data/b691_closing_push_out.txt). The re-cut: '
      'SIDE-rcurve, rows outside LICENSED or CITED 2 to 0, tag v0.1.1, the quotation search’s four quoting lines (SIDE-rcurve README.md :3, :9, '
      ':11, :19) each carried as a residue, R-1 to R-4 (data/b691_cut.txt :15-:18, :33). The generator’s run on the author’s word: two pages, '
      'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md 3 lines changed and phase1.5/rcurve/R_CURVE_CRITERION_v0_2_2.md 1 '
      '(data/b691_correspondence_run_PATHS.txt :31, data/b691_correspondence_run_RCURVE.txt :20); the :301 clause held as VERSION DIFFERS, '
      'SIDE-kernel v1.8 against the carry v1.3 = 0bc21c0, a residue for the SIDE-kernel row. The EpsteinQ0 docstrings re-cut: three lines, :106 '
      'and :110-:111, docstrings alone, v0.34.1 = e5fcda7, v0.34 unmoved (data/b691_epstein_lines.txt :63, data/b691_epstein_cut.txt :10). The '
      'stale orders: 35 triaged, CARRY 11, DISCHARGED-BY-READING 24, RETIRE 0 (data/b691_orders_triage.txt :151). Four rule arms added under '
      '`(R301)`(6), G-RULE-BINARY-HASHES, G-RULE-SUITE-PART-CALLS, G-RULE-POSTSEAL-READ and G-RULE-RECUT-QUOTE (data/b691_arms_added.txt :41). '
      'The failure the face declares: G-RULE-ONE-GIT-WRITE (data/b691_closing.txt :244-:245). Eleven defects, every one the seat’s '
      '(data/b691_defects.txt :5-:48): (a) reads through a shell filter or an interpreter’s print; (b) two redirects onto /dev/null; (c) two git '
      'writes in one message, twice; (d) the cut branches pushed outside the push tool; (e) the carried-at repair’s first form pairing one version '
      'with another version’s commit; (f) the behind route’s first forms; (g) the quotation search’s first forms; (h) the mid-act check’s commit '
      'scope; (i) step zero’s own rows; (j) the cut route’s duplicate keyword; (k) the banked diff’s blank context lines. The two items after the '
      'root are entered by the corrigendum beneath, lettered (l) and (m). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b692_record_lines.json', 'c1', entry=K.B691_ENTRY,
         check=[('FINDINGS.md', K.B691_ENTRY, '## SIDE-rcurve re-cut: 2 rows outside LICENSED/CITED to 0'), ('OPEN_TRAILS.md', K.B691_TRAIL, '### b691')],
         dry=dry)


# ================================================================================ COMPONENT 2: THE CLOSURE STEP ON THE RUNNER, (R302)(3)(a)
STD3 = ('propext', 'Classical.choice', 'Quot.sound')
# ### each kernel's libraries as its lakefile gives them: (the tree path, the module prefix the path maps to); a module is a .lean file under
# ### the path, its name the path's dotted form under the library's srcDir
LIBS = {'SIDE-explicit-formula': (('SIDEExplicitFormula/', ''), ('Zeta23/', ''), ('Vendored/Bulka/Lc/', 'Vendored/Bulka/'),
                                  ('Vendored/Bulka/Hadamard/', 'Vendored/Bulka/'), ('Vendored/Bulka/FunctionsOfOneComplexVariable/', 'Vendored/Bulka/'))}


def target_of(kernel, rev):
    """every module of the kernel's libraries at rev, read from git's tree listing (no filter), dotted under each library's srcDir."""
    mods = []
    for path, src in LIBS[kernel]:
        for f in g('D:/' + kernel, 'ls-tree', '-r', '--name-only', rev, '--', path).split(NL):
            f = f.strip()
            if f.endswith('.lean'):
                mods.append(f[len(src):-len('.lean')].replace('/', '.'))
    return mods


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def dispatch(*a):
    """`dispatch <kernel> <ref sha> <label> [dry]`: ONE dispatch of build-module.yml at main with the ref input, the target every module of
    the kernel's libraries at the ref; refused where data/b692_dispatches.json already carries the ref's tree (one dispatch per tree state).
    The run id read from the run list (the newest workflow_dispatch run created after the dispatch); a row banked."""
    kernel, ref, label = a[0], a[1], a[2]
    repo = 'psinary-sketch/' + kernel
    full = g('D:/' + kernel, 'rev-parse', ref).strip()
    tree = g('D:/' + kernel, 'rev-parse', full + '^{tree}').strip()
    j = jl('b692_dispatches.json') if os.path.isfile(os.path.join(D, 'b692_dispatches.json')) else {}
    rows = j.get('rows') or []
    seen = [r for r in rows if r.get('tree') == tree] + [dict(tree=tree, run_id=39312568167)] * (tree == '0add5a12761f111d502ed95452f84b28a467f33a')
    if seen:
        sys.exit('### THE TREE %s IS ALREADY BUILT (run %s) -- NOT DISPATCHED' % (tree[:12], seen[0].get('run_id')))
    mods = target_of(kernel, full)
    target = ' '.join(mods)
    print('  kernel %s ; ref %s ; tree %s ; modules %d ; target %d characters' % (kernel, full, tree, len(mods), len(target)))
    if 'dry' in a:
        return
    t0 = utc()
    rc, out, err = _gh('workflow', 'run', 'build-module.yml', '-R', repo, '--ref', 'main', '-f', 'ref=' + full, '-f', 'target=' + target)
    if rc != 0:
        sys.exit('### THE DISPATCH REFUSED: %s' % err[-400:])
    run_id = None
    for _i in range(12):
        time.sleep(5)
        rc, out, err = _gh('run', 'list', '-R', repo, '--workflow', 'build-module.yml', '--event', 'workflow_dispatch', '--limit', '5', '--json',
                           'databaseId,createdAt,status')
        new = [r for r in json.loads(out or b'[]') if r.get('createdAt', '') >= t0]
        if new:
            run_id = sorted(new, key=lambda r: r['createdAt'])[-1]['databaseId']
            break
    rows.append(dict(kernel=kernel, label=label, ref=full, tree=tree, modules=len(mods), dispatched=t0, run_id=run_id))
    put_json('b692_dispatches.json', dict(rows=rows))
    print('  dispatched %s ; run id %s' % (t0, run_id))


def _deps(ax):
    """the axioms output read per terminal: [(name, [axioms] or None for 'does not depend on any axioms')], wrapped lists rejoined."""
    out = []
    for n, d in re.findall(r"^'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)",
                           re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', ax), re.M):
        out.append((n, [x.strip() for x in d.split('[', 1)[1].rstrip(']').split(',') if x.strip()] if d.startswith('depends') else []))
    return out


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <tag> <note...>`: the kernel's run read by its id; the artifact listed, downloaded by its id into
    memory, its sha256 against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP;
    the axioms output of the print step banked whole, every name of the list matched to one printed line; the closure step's out/closure.jsonl.gz
    banked as a binary bank data/b692_circuit_<kernel>_<tag>_<tip>.jsonl.gz beside its text hashes bank (data/b680_rules.txt row (1)).
    data/b692_runner_<kernel>_<label>.txt, data/b692_axioms_<kernel>_<label>.txt and a row of data/b692_runner_rows.json."""
    import gzip
    import hashlib
    import io as _io
    import zipfile
    kernel, run_id, ref, label, tag, note = a[0], int(a[1]), a[2], a[3], a[4], ' '.join(a[5:])
    repo = 'psinary-sketch/' + kernel
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(kernel=kernel, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None, closure=None)
    L = ['b692 -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (kernel, label.upper(), utc()), '',
         '### the dispatch: %s ; the ref input %s' % (note, ref),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt'))]
    T_, B_ = {}, {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        L.append('### the artifact: id %s ; %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN',
            'AGREE' if digest and digest == sha else '### NOTHING READ FROM IT'))
        if digest and digest == sha:
            row['artifact_sha256'] = sha
            with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
                for n in z.namelist():
                    B_[n] = z.read(n)
                    if not n.endswith('.gz'):
                        T_[n] = B_[n].decode('utf-8', 'replace').replace(chr(13), '')
    else:
        L.append('### the artifact: ### NONE LISTED')
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    row['mem_low'] = int(low[-1]) if low else None
    row['stopped'] = any(l.startswith('STOP ') for l in mem.split(NL))
    blog = T_.get('build.log', '')
    row['build_exit'] = T_.get('build_exit.txt', '').strip() or None
    row['errors'] = [l for l in blog.split(NL) if ': error' in l or l.startswith('error:')]
    ax = T_.get('axioms.txt', '').rstrip(NL)
    row['axioms_sha256'] = hashlib.sha256(ax.encode('utf-8')).hexdigest() if ax else None
    deps = _deps(ax)
    tg = [l.strip() for l in T_.get('print_targets.txt', '').split(NL) if l.strip()]
    printed = [n for n, _d in deps]
    unmatched = [n for n in tg if n not in printed]
    outside = [(n, d) for n, d in deps if not set(d) <= set(STD3)]
    clog = T_.get('closure_log.txt', '').rstrip(NL)
    gzb = B_.get('closure.jsonl.gz')
    cl_rows, cl_head = 0, {}
    if gzb:
        txt = gzip.decompress(gzb).decode('utf-8')
        lines = [l for l in txt.split(NL) if l.strip()]
        cl_head = json.loads(lines[-1]) if lines and '"header"' in lines[-1] else {}
        cl_rows = len(lines) - (1 if cl_head else 0)
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d:' % (row['build_exit'], len(row['errors']))] + ['    ' + l for l in row['errors'][:40]] + [
          '### the log`s last lines:'] + ['    ' + l for l in blog.rstrip(NL).split(NL)[-6:]] + [
          '### the closure step: its log`s last lines:'] + ['    ' + l for l in clog.split(NL)[-8:]] + [
          '### the closure bank: %s' % (('out/closure.jsonl.gz %d bytes, sha256 %s ; records %d ; the header`s count %s ; programme modules %d' % (
              len(gzb), hashlib.sha256(gzb).hexdigest(), cl_rows, cl_head.get('records'), len(cl_head.get('modules') or []))) if gzb else '### NONE IN THE ARTIFACT'),
          '### the print step: the list (out/print_targets.txt) %d names ; terminals printed %d ; every name printed once %s ; axiom-free %d ; '
          'sorryAx %d ; outside the standard three %d ; refused %s' % (
              len(tg), len(deps), not unmatched and len(printed) == len(set(printed)) == len(tg), sum(1 for _n, d in deps if not d),
              sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), T_.get('axioms_refused.txt', '').strip() or 'NONE'),
          '### rows are terminals: name | the axioms printed | within the standard three:']
    L += ['  %-62s %s %s' % (n, d, 'STD3' if set(d) <= set(STD3) else '### OUTSIDE') for n, d in deps]
    L += ['  %-62s ### NOT PRINTED' % n for n in unmatched]
    ok = run.get('conclusion') == 'success' and row['artifact_sha256'] and row['build_exit'] == '0' and not row['errors'] and not row['stopped'] \
        and row['mem_low'] is not None and row['mem_low'] >= K.HOLD and deps and not unmatched and not outside
    row['gate'] = 'DERIVES' if ok else 'NOT DERIVES'
    tip = (run.get('headSha') and ref[:7]) or ref[:7]
    if gzb and row['artifact_sha256']:
        stem = 'b692_circuit_%s_%s_%s' % (kernel, tag, tip)
        p = os.path.join(D, stem + '.jsonl.gz')
        open(p + '.tmp', 'wb').write(gzb)
        os.replace(p + '.tmp', p)
        row['closure'] = dict(bank=stem + '.jsonl.gz', sha256=hashlib.sha256(gzb).hexdigest(), bytes=len(gzb), records=cl_rows)
        put_txt(stem + '_hashes.txt', [
            'b692 -- THE CLOSURE BANK`S HASHES, %s AT %s (the tip %s), BY THE RUNNER (%s)' % (kernel, tag, ref, utc()), '',
            '### rows are binary banks this text bank roots (data/b680_rules.txt row (1)): the bank | sha256 | bytes | the run | the artifact.',
            '  data/%s.jsonl.gz | %s | %d | run %d | artifact %s sha256 %s' % (stem, row['closure']['sha256'], len(gzb), run_id, art.get('id'),
                                                                            row['artifact_sha256']),
            '', '### ### **RECORDS %d ; THE HEADER`S COUNT %s ; PROGRAMME MODULES %d ; THE REF %s.**' % (
                cl_rows, cl_head.get('records'), len(cl_head.get('modules') or []), ref)])
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d OF %d ; SORRYAX %d ; '
          'OUTSIDE THE STANDARD THREE %d ; CLOSURE RECORDS %d ; GATE %s.**' % (
              run_id, label, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']),
              len(deps), len(tg), sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), cl_rows, row['gate'])]
    read_runner_row(row)
    put_txt('b692_runner_%s_%s.txt' % (kernel, label), L)
    if row['artifact_sha256']:
        put_txt('b692_axioms_%s_%s.txt' % (kernel, label), ax.split(NL) if ax else ['### EMPTY'])
        put_txt('b692_buildlog_%s_%s.txt' % (kernel, label), blog.rstrip(NL).split(NL))
        put_txt('b692_closurelog_%s_%s.txt' % (kernel, label), clog.split(NL) if clog else ['### EMPTY'])
    j = jl('b692_runner_rows.json') if os.path.isfile(os.path.join(D, 'b692_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('b692_runner_rows.json', dict(rows=rows))
    print(NL.join(L[:8] + [l for l in L if l.startswith('### the closure')] + L[-1:]))


def prints(*a):
    """`prints <kernel> <before bank> <after bank>`: the 'before' terminals' printed lines compared with the same names' lines in the 'after'
    bank, line for line by name; the raw axioms banks compared byte for byte beside. data/b692_prints_<kernel>.txt."""
    kernel, bb, ab = a[0], a[1], a[2]
    b, f = rdn(bb), rdn(ab)
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bd, fd = dict(_deps(b)), dict(_deps(f))
    diff = [(n, bd[n], fd.get(n)) for n in bd if fd.get(n) != bd[n]]
    new = [n for n in fd if n not in bd]
    L = ['b692 -- THE PRINTS OF %s BEFORE AND AFTER THE CLOSURE STEP, BY NAME AND LINE FOR LINE (%s)' % (kernel, utc()), '',
         '### before: relay data/%s (%d terminals) ; after: relay data/%s (%d terminals) ; the two banks equal line for line: %s ; rows are the '
         'terminals that differ:' % (bb, len(bd), ab, len(fd), b == f)] + (['    %s : %s | %s' % d for d in diff] or ['    NONE']) + [
        '### the names printed after and not before: %d' % len(new)] + ['    %s %s' % (n, fd[n]) for n in new]
    L += ['', '### ### **BEFORE %d TERMINALS ; EACH PRINTED AFTER %s ; DIFFERING %d ; NEW %d ; EQUAL LINE FOR LINE %s.**' % (
        len(bd), all(n in fd for n in bd), len(diff), len(new), b == f)]
    put_txt('b692_prints_%s.txt' % kernel, L)
    print(L[-1])


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, c1=c1, dispatch=dispatch, runner=runner, prints=prints)

if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ROUTES:
        print('usage: b692_record.py ' + ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    ROUTES[r](*sys.argv[2:])
