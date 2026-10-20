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


TRIAGE_WORDS = ('CARRY', 'DISCHARGED-BY-READING', 'RETIRE')


def read_triage_row(r):
    """a row of data/b691_orders_triage.json: the order's name (W-ORD-...), its OPEN_TRAILS line (an int), the trigger as written (non-empty),
    and a disposition (one of TRIAGE_WORDS) with its ground; returns (name, line, disposition, ground)."""
    if not isinstance(r, dict) or not re.match(r'^W-ORD-[A-Z0-9-]+$', r.get('name') or '') or not isinstance(r.get('line'), int) \
            or not (r.get('trigger') or '').strip() or r.get('disposition') not in TRIAGE_WORDS or not (r.get('ground') or '').strip():
        raise ValueError('triage row of another shape: %r' % (str(r)[:120],))
    return r['name'], r['line'], r['disposition'], r['ground']


READERS = ['read_score_row', 'read_head', 'read_branch_row', 'read_runner_row', 'read_triage_row']


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


# ================================================================================ COMPONENT 4: THE TRIAGE RAISED BY CLASS, (R302)(4)
def triage_counts(*a):
    """data/b691_orders_triage.json read row by row: the counts per disposition class, the RETIRE rows by name and reason, each class's rows by
    name and OPEN_TRAILS line, beside the bank's own verdict (data/b691_orders_triage.txt :151). data/b692_triage_counts.txt."""
    j = jl('b691_orders_triage.json')
    rows = [read_triage_row(r) for r in (j.get('rows') or [])]
    by = dict((w, [r for r in rows if r[2] == w]) for w in TRIAGE_WORDS)
    verdict = rdn('b691_orders_triage.txt').split(NL)[150] if len(rdn('b691_orders_triage.txt').split(NL)) > 150 else ''
    L = ['b692 -- COMPONENT 4, (R302)(4): THE STALE-ORDERS TRIAGE RAISED BY CLASS (%s)' % utc(), '',
         '### the bank: relay data/b691_orders_triage.json, rows %d, each read through read_triage_row; its verdict at data/b691_orders_triage.txt :151:' % len(rows),
         '###   ' + verdict.strip(), '',
         '### THE COUNTS PER CLASS: ' + ' ; '.join('%s %d' % (w, len(by[w])) for w in TRIAGE_WORDS), '',
         '### THE RETIRE ROWS, BY NAME AND REASON:'] + (['  %s (OPEN_TRAILS :%d) -- %s' % (n, ln, gr) for n, ln, _d, gr in by['RETIRE']] or ['  NONE'])
    for w in ('CARRY', 'DISCHARGED-BY-READING'):
        L += ['', '### %s (%d), by name and OPEN_TRAILS line:' % (w, len(by[w]))] + ['  %s :%d' % (n, ln) for n, ln, _d, _g in by[w]]
    L += ['', '### ### **ORDERS %d ; CARRY %d ; DISCHARGED-BY-READING %d ; RETIRE %d ; THE BANK`S VERDICT EQUAL %s.**' % (
        len(rows), len(by['CARRY']), len(by['DISCHARGED-BY-READING']), len(by['RETIRE']),
        ('ORDERS %d ; CARRY %d ; DISCHARGED-BY-READING %d ; RETIRE %d' % (len(rows), len(by['CARRY']), len(by['DISCHARGED-BY-READING']), len(by['RETIRE']))) in verdict)]
    put_txt('b692_triage_counts.txt', L)
    print(NL.join(L[:12] + L[-1:]))


CITE_AT = re.compile(r'(?:PLACE-papers |relay )?((?:FINDINGS|OPEN_TRAILS)\.md|data/[\w.+-]+\.(?:txt|json|md)) :(\d+)(?: \("([^"]+)"\))?')


def _orders_plan():
    """each triage row with its line in data/b691_orders_triage.txt and the author's check at the (R302)(4) prompt applied: a
    DISCHARGED-BY-READING row whose reading cites a bank by path and line (its quoted words standing at that line now) is written as
    discharged; one that does not is written as CARRY with the trigger its row gives. Returns [(row, triage line, written disposition, why)]."""
    j = jl('b691_orders_triage.json')
    tl = rdn('b691_orders_triage.txt').split(NL)
    plan = []
    for r in j.get('rows') or []:
        n, ln, d, gr = read_triage_row(r)
        at = [i + 1 for i, l in enumerate(tl) if l.startswith('  %s ' % n)]
        why, w = '', d
        if d == 'DISCHARGED-BY-READING':
            m = CITE_AT.search(gr)
            if not m:
                tm = re.search(r'(?:relay )?(tools/[\w.+-]+\.py :\d+)', gr)
                w, why = 'CARRY', ('its reading cites a tool by path and line (%s) and no bank' % tm.group(1)) if tm else \
                    'its reading cites no bank by path and line'
            else:
                f, k, q = m.group(1), int(m.group(2)), m.group(3)
                path = os.path.join(PP, f) if f.endswith('.md') and not f.startswith('data/') else os.path.join(D, f[len('data/'):])
                line_ = (rd(path).split(NL) + [''] * k)[k - 1]
                if q and q not in line_:
                    w, why = 'CARRY', 'its reading`s words do not stand at %s :%d now' % (f, k)
                else:
                    why = 'its reading cited at %s :%d%s' % (f, k, ', its words standing there' if q else '')
        plan.append((r, at[0] if at else None, w, why))
    return plan


def orders(*a):
    """`orders [dry]`: (R302)(4) on the author's word -- one OPEN_TRAILS entry per triage row, each citing its row by line in relay
    data/b691_orders_triage.txt; the demoted count printed before any entry lands; data/b692_orders_lines.json."""
    plan = _orders_plan()
    dem = [(r['name'], why) for r, _t, w, why in plan if r['disposition'] == 'DISCHARGED-BY-READING' and w == 'CARRY']
    print('  ### THE AUTHOR`S CHECK BEFORE THE WRITES: DISCHARGED-BY-READING rows %d ; demoted to CARRY %d %s' % (
        sum(1 for r, _t, _w, _y in plan if r['disposition'] == 'DISCHARGED-BY-READING'), len(dem), dem or ''))
    if any(t is None for _r, t, _w, _y in plan):
        sys.exit('### A TRIAGE ROW HAS NO LINE IN THE BANK -- NOTHING WRITTEN')
    items = []
    for r, t, w, why in plan:
        head = '*Appended 2026-10-19 by b692 under `(R302)`(4) and the author’s word at its prompt -- `%s` %s (relay data/b691_orders_triage.txt :%d):*' % (
            r['name'], 'CARRIED' if w == 'CARRY' else 'DISCHARGED BY READING', t)
        trig = r['trigger'].strip()
        if w == 'CARRY':
            body = (' the order entered at OPEN_TRAILS :%d stands open, its trigger as written: “%s”; %s. Ground: %s%s. Status OPEN.' % (
                r['line'], trig, ('it can still fire -- ' + r['why'].strip()) if r.get('can_fire') else ('its row reads it cannot fire as written -- '
                                                                                                      + r['why'].strip()), r['ground'].strip(),
                (' (a DISCHARGED-BY-READING row written as CARRY on the author’s check: %s)' % why) if r['disposition'] != 'CARRY' else ''))
        else:
            body = (' the order entered at OPEN_TRAILS :%d is discharged by the reading %s (%s); its trigger as written: “%s”. Status DISCHARGED.' % (
                r['line'], r['ground'].strip(), why, trig))
        items.append(('OPEN_TRAILS.md', head, NL + head + body + NL))
    land(items, 'b692_orders_lines.json', 'order', entry=None, dry='dry' in a)


# ================================================================================ THE CAPTURE AND THE COMMANDS (b691's, carried)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
PREV_ACT, PREV_ANCHOR = 'b691', 'RULING (R301) BEGIN'


def _anchor_ts(anchor, session=SESSION):
    for ln in io.open(session, encoding='utf-8', errors='replace'):
        if anchor in ln:
            try:
                j = json.loads(ln)
            except ValueError:
                continue
            if j.get('type') == 'user' and not j.get('isCompactSummary'):
                return j.get('timestamp')
    return None


def _bg_calls():
    """b688's repair, carried: the calls the seat sent with the tool's run_in_background parameter, from the ruling's line on. {(ts, cmd)}."""
    out = set()
    for _i, o, _st, _sid in _session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and (c.get('input') or {}).get('run_in_background'):
                out.add((o.get('timestamp'), (c.get('input') or {}).get('command')))
    return out


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    bg = _bg_calls()
    for i, r in enumerate(rows):
        r['n'] = i + 1
        r['bg'] = (r.get('ts'), r.get('cmd')) in bg
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')
SED = re.compile(r'(^|[;&|(]\s*|\s)sed\s')
PY_PRINT_READ = re.compile(r'python[^\n]*\s-c\s')
REDIRECT_ANY = re.compile(r'(?<![<>=\-\w])(?:\d?>>?|&>)(?!&)\s*\S')
PIPE_FILTER = re.compile(r'\|\s*(?:head|tail|wc|grep|cut|sort|uniq|awk|less|more|tr)\b')
SED_KIND = 'R sed in any form (data/b685_rules.txt row (2))'


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def sed_cmd(cmd):
    return SED.search(QUOTED.sub('""', cmd)) is not None


def prev_capture():
    """G-EDIT-ROUTE's window over the previous act (b687's repair; the same session): b691's capture AFTER ITS POST-PUSH SUITE -- every
    command from the call that combined b691's post-push parts into data/b691_checks_postpush.txt to the first user line of (R302)."""
    rows = ER.capture(SESSION, PREV_ANCHOR, SUBAGENTS)
    end = _anchor_ts(K.ANCHOR)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV_ACT in r['cmd'] and '--combine' in r['cmd']]
    if not first or not end:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE OR THIS ACT`S ANCHOR IS NOT IN THE SESSION`S CAPTURE -- NOTHING READ')
    out = [dict(r, src='%s %s' % (PREV_ACT, r['src'])) for r in rows if first[0] <= r['ts'] < end]
    for i, r in enumerate(out):
        r['n'] = 'p%d' % (i + 1)
    return out


def edit_route_offences(rows):
    out = []
    for r in rows:
        o = list(ER.offences(r['cmd']))
        if r['tool'] in ('Bash', 'PowerShell') and sed_cmd(r['cmd']) and not any(k.startswith('S sed') for k, _ in o):
            o.append((SED_KIND, r['cmd'].split(NL)[0][:120]))
        if o:
            out.append((r, o))
    return out


MOVE_OR_DELETE = re.compile(r'\bgit\s+(-C\s+\S+\s+)?(mv|rm)\b|\bgit\s+(-C\s+\S+\s+)?branch\s+-[dD]\b|--delete\b|(^|[;&|]\s*|\s)rm\s+-|Remove'
                            + r'-Item|\bos\.remove\b')
REDIRECT_NULL = re.compile(r'\d?>\s*/dev/null')


def delete_shape(cmd):
    """(R302)(6): a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    return names, [ch for ch in '*?[' if ch in c]


IDENT = ('psinary', 'hotmail', 'seale', 'york', 'orcid', '0009-0008')


def outbound():
    out = []
    for i, o, _st, _sid in _session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') in ('WebSearch', 'Agent', 'WebFetch'):
                inp = c.get('input') or {}
                text = inp.get('query') or inp.get('prompt') or inp.get('url') or ''
                out.append(dict(line=i, tool=c['name'], ts=o.get('timestamp'), text=text))
    for r in out:
        r['identifiers'] = [w for w in IDENT if w in r['text'].lower()]
    return out


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = edit_route_offences(rows)
    prev = prev_capture()
    phits = edit_route_offences(prev)
    sh_ = [r for r in rows if r['tool'] in ('Bash', 'PowerShell')]
    lean = [r for r in sh_ if local_lean(r['cmd'])]
    mv = [r for r in sh_ if MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in sh_ if re.search(r'(^|&&\s*|;\s*)gh workflow run\b|b692_record\.py dispatch [^\s;]+ [^\s;]+ [^\s;]+\s*(?:;|$)',
                                        QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in sh_ if (r.get('bg') or re.search(r'Start-Process|\bnohup\b|run_in_background', QUOTED.sub('""', r['cmd'])))]
    seds = [r for r in sh_ if sed_cmd(r['cmd'])]
    nulls = [r for r in sh_ if REDIRECT_NULL.search(QUOTED.sub('""', r['cmd']))]
    redir = [r for r in sh_ if REDIRECT_ANY.search(QUOTED.sub('""', r['cmd']))]
    pipes = [r for r in sh_ if PIPE_FILTER.search(QUOTED.sub('""', r['cmd']))]
    pyreads = [r for r in sh_ if PY_PRINT_READ.search(r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    ob = outbound()
    L = ['b692 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (b691, this same session %s, from its post-push combine to (R302)`s line): %d '
              'commands from %s, its offences printed whole (%d):' % (K.SESSION_ID[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES, BY THE RECORD TOOL`S dispatch ROUTE (%d):' % len(disp)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN, BY THEIR TEXT OR THE TOOL`S run_in_background PARAMETER (%d):' % len(
        detach)] + (['  #%d %s%s' % (r['n'], '[run_in_background] ' if r.get('bg') else '', r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING sed IN ANY FORM (data/b685_rules.txt row (2)) (%d):' % len(seds)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in seds] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT ONTO /dev/null, read outside quoted strings (%d):' % len(nulls)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], r['cmd'].split(NL)[0][:200]) for r in nulls] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT OF ANY STREAM, read outside quoted strings (%d):' % len(redir)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in redir] or ['  NONE'])
    L += ['', '### THE COMMANDS PIPING INTO A SHELL FILTER (head, tail, wc, grep and the like), read outside quoted strings -- this act`s defect (a) '
              'among them (%d):' % len(pipes)] + (['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in pipes] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT RUN AN INTERPRETER`S ONE-LINE PROGRAM (python -c), each its first line (%d):' % len(pyreads)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:220]) for r in pyreads] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R302)(6): one branch per command, no glob in any half): ' + ('; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git (web searches, subagent prompts and fetches), each with the author`s identifiers found in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; REDIRECTS ONTO /dev/null %d ; '
              'REDIRECTS OF ANY STREAM %d ; PIPES INTO A SHELL FILTER %d ; ONE-LINE PROGRAMS %d ; MOVE OR DELETE COMMANDS %d ; BRANCH DELETES OF ONE '
              'BRANCH AND NO GLOB %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(nulls), len(redir), len(pipes), len(pyreads), len(mv),
                  sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl), len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    put_txt('b692_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b692_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        prev=dict(act=PREV_ACT, session=K.SESSION_ID, rows=len(prev),
                                                  offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                        seds=[r['n'] for r in seds], null_redirects=[r['n'] for r in nulls], redirects=[r['n'] for r in redir],
                                        pipes=[r['n'] for r in pipes], py_programs=[r['n'] for r in pyreads], moves_deletes=[r['n'] for r in mv],
                                        delete_shapes=[dict(n=n, deletes=d, globs=gl) for n, d, gl in shapes], outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r, o in phits:
        print('  PREVIOUS-ACT OFFENCE #%s %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b692_defects.txt').split(NL)
    for i, l in enumerate(L):
        if DEFECT_ROW.match(l):
            j = i + 1
            while j < len(L) and L[j].startswith('    ') and not DEFECT_ROW.match(L[j]) and not L[j].startswith('    ###'):
                j += 1
            m = re.match(r"^\(([a-z]'?)\) (.*?)\.(?= |$)", ' '.join(x.strip() for x in L[i:j]))
            if m:
                out.append(m.group(0)[:-1])
    return out


def defects(*a):
    t = rdn('b692_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b692_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


# ================================================================================ THE LATE ROUTES (b691's, carried with b692's names)
def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle', 'SIDE-bijection', 'SIDE-class-number-anomaly',
                                   'SIDE-spinor', 'SIDE-li-map', 'SIDE-rcurve', 'SIDE-archimedean']


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    put_json('b692_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-explicit-formula read after the closure step`s three commits and with the scratch branch standing; none '
          'written after this read until the scratch branch`s delete at the close)' % len(ks))


def seal_hashes():
    import hashlib
    rec_ = jl('b692_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b692_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def root_banks_state(banks, rev='HEAD'):
    import hashlib
    head = g(ROOT, 'rev-parse', rev).strip()
    rem = (g(ROOT, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    rows = []
    for b in banks:
        st = g(ROOT, 'status', '--porcelain', '--', b).strip()
        r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (head, b)], capture_output=True)
        p = os.path.join(ROOT, *b.split('/'))
        now = open(p, 'rb').read() if os.path.exists(p) else None
        eq = r.returncode == 0 and now is not None and hashlib.sha256(r.stdout).hexdigest() == hashlib.sha256(now).hexdigest()
        rows.append(dict(bank=b, status=st or 'clean', at_head=r.returncode == 0, equal=eq))
    return dict(head=head, remote=rem, rows=rows, clean=all(x['status'] == 'clean' and x['equal'] for x in rows) and bool(rows),
                pushed=bool(head) and head == rem)


ROOT_EXCLUDE = re.compile(r'^b692_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*)\.?(txt|json|md|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b692_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(K.SHARED_APPENDED))


def rootbanks(*a):
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['b692 -- G-ROOT-BANKS-COMMITTED`S READING: THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ;'
         ' carried by HEAD ; HEAD`s blob equal to the file' % utc(), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('b692_root_banks.txt', L)
    put_json('b692_root_banks.json', dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b692_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### G-ROOT-BANKS-COMMITTED: A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b692'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b692_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='b692_ra_') as tmp:
        cp_ = os.path.join(tmp, os.path.basename(bank_))
        b_ = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
        b_[0] ^= 0x01
        open(cp_, 'wb').write(bytes(b_))
        items2 = [('%s %s' % (bank_, AR.sha256_file(cp_)) if it.split()[0] == bank_ else it) for it in J['items']]
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
    L = ['b692 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '-')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b692_root_arm.txt', L)
    put_json('b692_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_final(*a):
    before = _rows_state(json.loads(_show(ROOT, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b692 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(ROOT, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b692_table_final.txt', L)
    put_json('b692_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


# ================================================================================ THE PER-ARM SECONDS (b690's route, carried)
def _g2_of(path):
    t = rd(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _standing():
    import b691_worklist as K691
    return sorted((set(_g2_of(os.path.join(D, 'b691_registration_2026-10-19.txt'))) - set(K691.ACT_ARMS)) | set(K.STANDING_ADDED))


def armsecs(*a):
    st = _standing()
    rows, phases, runs = [], {}, {}
    for p in K.PARTS:
        j = jl('b692_arm_seconds_%s.json' % p)
        phases[p] = j.get('phases') or {}
        runs[p] = j.get('run_secs')
        for nm, s in (j.get('arms') or {}).items():
            rows.append(dict(arm=nm, part=p, secs=s, standing=nm in st))
    srows = sorted([r for r in rows if r['standing']], key=lambda r: -r['secs'])
    miss = sorted(set(st) - set(r['arm'] for r in srows))
    L = ['b692 -- THE STANDING ARMS` SECONDS AT HEAD, BY PART, FROM THE PRE-RUN (%s): the per-part seconds the ferry`s Component 5 names' % utc(), '',
         '### the source: data/b692_arm_seconds_<part>.json, written by tools/b692_checks.py at its pre-run, each arm`s seconds the sum of its',
         '### three readings (LIVE on the sources, NEG on a copy, POS on a mutated copy); each part`s run seconds and its phases -- the sources',
         '### built once for all its arms -- printed beside, not divided among them. Rows are standing arms, slowest first:']
    L += ['  %-46s %-11s %8.3f s' % (r['arm'], r['part'], r['secs']) for r in srows]
    L += ['', '### THE PARTS` SECONDS: ' + ' | '.join('%s %s s' % (p, runs[p]) for p in K.PARTS),
          '### THE PARTS` PHASES (seconds): ' + ' | '.join('%s: %s' % (p, '; '.join('%s %.0f' % kv for kv in ph.items())) for p, ph in phases.items()),
          '### the standing arms not clocked: %s' % (miss or 'NONE'),
          '', '### ### **STANDING ARMS CLOCKED %d OF %d ; THE THREE SLOWEST %s ; THEIR SECONDS SUMMED %.1f.**' % (
              len(srows), len(st), ', '.join('%s (%s, %.2f s)' % (r['arm'], r['part'], r['secs']) for r in srows[:3]) or 'NONE',
              sum(r['secs'] for r in srows))]
    put_txt('b692_arm_seconds.txt', L)
    put_json('b692_arm_seconds.json', dict(at=utc(), rows=srows, phases=phases, run_secs=runs, standing=len(st), clocked=len(srows), missing=miss,
                                           slowest=[r['arm'] for r in srows[:3]]))
    print(L[-1])


# ================================================================================ THE SCORES: (N1)-(N5) OF (R302)'S FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and not the entry; the entry reads the scorer's bank. `scores` writes
# ### data/b692_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there and is read at the close.
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b691_closing_push_out.txt')


def _git_ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t.isdigit() else None


def _iso_epoch(s):
    import calendar
    try:
        return calendar.timegm(time.strptime((s or '')[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', 'FINDINGS.md', 'OPEN_TRAILS.md')
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _files_of(repo, rev):
    return sorted(x for x in g(repo, 'show', '--name-only', '--pretty=format:', rev).split(NL) if x.strip())


def _runner_state():
    """N1's second clause: every runner row read by its id with the artifact's sha256 equal to the platform's, and every closure bank's sha256
    in its text hashes bank equal to the bank's bytes."""
    import hashlib
    rows = jl(K.RUNNER_ROWS).get('rows') or []
    arts = bool(rows) and all(r.get('artifact_sha256') for r in rows)
    cl = []
    for r in rows:
        c = r.get('closure') or {}
        if c.get('bank'):
            p = os.path.join(D, c['bank'])
            hb = rdn(c['bank'].replace('.jsonl.gz', '_hashes.txt'))
            sha = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
            cl.append((c['bank'], sha == c.get('sha256') and bool(sha) and sha in hb))
    return dict(rows=len(rows), arts=arts, closures=cl)


def _n1():
    cm = jl('b692_commands.json')
    rs = _runner_state()
    ok = bool(cm) and not cm.get('local_lean') and rs['arts'] and bool(rs['closures']) and all(v for _b, v in rs['closures'])
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s (relay data/b692_commands.txt, %d commands read); runner rows %d, every '
        'artifact`s sha256 equal to the platform`s before any reading %s; the closure banks, each sha256 carried by its text hashes bank: %s' % (
            cm.get('local_lean') if cm else 'unread', len(cm.get('rows') or []), rs['rows'], rs['arts'],
            '; '.join('%s %s' % (b, v) for b, v in rs['closures']) or 'none'))


def _modules_state():
    ef = 'D:/' + K.EF
    diff = [x for x in g(ef, 'diff', '--name-only', K.EF_BEFORE, K.EF_TIP, '--', 'SIDEExplicitFormula', 'Zeta23', 'Vendored', 'print_targets.txt',
                         'lakefile.toml').split(NL) if x.strip()]
    allf = sorted(x for x in g(ef, 'diff', '--name-only', K.EF_BEFORE, K.EF_TIP).split(NL) if x.strip())
    prints = rdn('b692_prints_SIDE-explicit-formula.txt')
    tags = [t for t in g(ef, 'tag', '--points-at', K.EF_TIP).split() + sum((g(ef, 'tag', '--points-at', c).split() for c in K.CLOSURE_COMMITS), [])]
    return dict(diff=diff, files=allf, prints='EQUAL LINE FOR LINE True' in prints and 'BEFORE 72 TERMINALS' in prints, tags=tags,
                main=g(ef, 'rev-parse', '--short=7', 'main').strip())


def _n2():
    m = _modules_state()
    t0, moved, tags = _kernels_moved()
    ok = m['diff'] == [] and m['files'] == ['.github/workflows/build-module.yml', 'CircuitClosure.lean'] and m['prints'] and not m['tags'] and not tags
    return ('HELD' if ok else 'REFUTED'), (
        'git diff %s..%s over SIDEExplicitFormula, Zeta23, Vendored, print_targets.txt and lakefile.toml: %s; the files the closure step wrote: %s; the '
        'print list at main before (run 39312568167) and after (run 39340192180) equal line for line (relay data/b692_prints_SIDE-explicit-formula.txt): '
        '%s; tags at the closure commits: %s; tags made on any kernel since the act began: %s' % (
            K.EF_BEFORE, K.EF_TIP, m['diff'] or 'EMPTY', m['files'], m['prints'], m['tags'] or 'NONE', tags or 'NONE'))


def _controls_state():
    c, s = rdn('b692_circuit_controls.txt'), rdn('b692_circuit_shorts_branch.txt')
    return dict(main='SHORTS 0 ON THE BANK' in c and 'SHORTS ON THE BANK        relay data/%s | SHORTS 0 | as wanted (0) True' % K.CLOSURE_BANK in c,
                branch='SHORTS 1 (RECORDS CARRYING sorryAx)' in s and 'THE ONE FIRST' in s and 'circuit_shorts_control_b692' in s,
                hcount='Wide.HCount A TERMINAL OF THE STRIP-FREE THEOREM True' in c, premise='NO PREMISE AT h2_sign_iff_rh True' in c,
                planted='THE PLANTED COPY READ AS ONE SHORT' in c)


def _n3():
    c = _controls_state()
    ok = all(c.values())
    return ('HELD' if ok else 'REFUTED'), (
        'SHORTS 0 on main (relay data/b692_circuit_controls.txt): %s, the planted copy read as one short %s; SHORTS 1 on the scratch branch at '
        'B321.circuit_shorts_control_b692 from run 39342395110 (relay data/b692_circuit_shorts_branch.txt): %s; Wide.HCount among the strip-free '
        'theorem`s TERMINALS: %s; no premise at h2_sign_iff_rh: %s' % (c['main'], c['planted'], c['branch'], c['hcount'], c['premise']))


def _dominance_state():
    d = rdn('b692_circuit_dominance.txt')
    m = re.search(r'CLAUSE-DOMINANCE (\d+) OF (\d+) FACES KERNELS REACHED \((SIDE-[\w-]+) (IN|NOT IN)\) ; (\d+) NOT REACHED \(([^)]*)\)', d)
    rf_t = _git_ct(ROOT, K.READ_RELAY)
    # ### the diff bank's commit against the scores bank's own writing, which precedes the entry (data/b686_rules.txt row (1)): no ledger
    # ### line and no findings bank read here
    return dict(frac=bool(m), named=bool(m) and m.group(3) == K.EF and m.group(6) == ', '.join(K.NOT_REACHED),
                rows='  %-24s' % K.EF in d and all(('  %-24s' % k) in d for k in K.NOT_REACHED),
                readfirst='data/b692_readfirst_diff.txt' in _files_of(ROOT, K.READ_RELAY) and bool(rf_t) and rf_t < time.time(),
                frac_text=m.group(0) if m else 'unread')


def _n4():
    d = _dominance_state()
    ok = d['frac'] and d['named'] and d['rows'] and d['readfirst']
    return ('HELD' if ok else 'REFUTED'), (
        'CLAUSE-DOMINANCE printed as a fraction with each faces kernel named and its reading beside (relay data/b692_circuit_dominance.txt): "%s" '
        '%s; READFIRST-CLOSURE`s diff against the hand list banked (relay data/b692_readfirst_diff.txt, relay %s) before any claim about it is '
        'written: %s' % (d['frac_text'], d['named'] and d['rows'], K.READ_RELAY, d['readfirst']))


def _kernels_moved():
    t0 = _iso_epoch(_anchor_ts(K.ANCHOR) or '')
    moved, tags = [], []
    for k in dict.fromkeys(_kerns()):
        p = 'D:/' + k
        for l in g(p, 'log', '--format=%h %ct', 'main').split(NL)[:40]:
            x = l.split()
            if len(x) == 2 and x[1].isdigit() and t0 and int(x[1]) > t0:
                moved.append((k, x[0]))
        for l in g(p, 'for-each-ref', '--format=%(refname:short) %(creatordate:unix)', 'refs/tags').split(NL):
            x = l.split()
            if len(x) == 2 and x[1].isdigit() and t0 and int(x[1]) > t0:
                tags.append((k, x[0]))
    return t0, moved, tags


def _amended_after(repo, lock):
    """commits amended at or after the lock: the reflog's `commit (amend)` entries by their time."""
    out = []
    for l in g(repo, 'reflog', '--date=unix', '--format=%gd %gs').split(NL):
        m = re.match(r'HEAD@\{(\d+)\} (commit \(amend\).*)$', l.strip())
        if m and lock and int(m.group(1)) >= lock:
            out.append(m.group(2)[:60])
    return out


def _n5():
    face = jl('b692_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    t0, moved, tags = _kernels_moved()
    allowed = set((k, c[:7]) for k, cs in K.KERNEL_COMMITS.items() for c in cs)
    beyond_main = [m for m in moved if (m[0], m[1][:7]) not in allowed]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b692_', x) and x[6:] not in K.REPAIRED_TOOLS + K.NEW_TOOLS]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b692_|audit_b692_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA) or x in K.SHARED_APPENDED
                                                or (x.startswith('tools/') and x[6:] in K.REPAIRED_TOOLS + K.NEW_TOOLS))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import rule_arms as RA
    import b691_worklist as K691
    arms_added = sorted(set(RA.NAMES) - set(K691.STANDING_ADDED) - set(_g2_of(os.path.join(D, 'b691_registration_2026-10-19.txt'))))
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock)) if lock else []
    ob = jl('b692_commands.json').get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    wf_ident = [w for w in IDENT if w in g('D:/' + K.EF, 'show', 'main:.github/workflows/build-module.yml').lower()]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = k_ok and not beyond_main and not tags and not pp_beyond and not kinds_beyond and not shared_tools and not differ and not arms_added \
        and not amended and not ident and not wf_ident and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; kernel main commits '
            'since the act began beyond the closure step`s three (%s): %s; tags made since the act began: %s; no standing arm added (tools/rule_arms.py`s '
            'names beyond b691`s face): %s; the shared tools edited beyond the (R302)(2) repair %s: %s; sealed tools not agreeing (rule_arms.py among '
            'them): %s; commits amended after the seal: %s; PLACE-papers beyond FINDINGS, OPEN_TRAILS and INSTRUMENTS.md: %s; relay files of a kind '
            'beyond the act`s banks and tools, the reader, the repaired tool, the corrigenda bank, the table, the root list and b691`s push-out '
            'bank: %s; "patent" in the lines written: %s; outbound requests other than git %d, an identifier of the author in %s; in '
            'SIDE-explicit-formula`s workflow file: %s' % (
                K.DRAFT, k_ok, ', '.join(K.CLOSURE_COMMITS), beyond_main or 'NONE', tags or 'NONE', arms_added or 'NONE', list(K.REPAIRED_TOOLS),
                shared_tools or 'NONE', differ or 'NONE', amended or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE', pat or 'NONE', len(ob),
                [r['line'] for r in ident] or 'NONE', wf_ident or 'NONE'))


def _s_scores():
    import collections
    TF, RA_ = jl('b692_table_final.json'), jl('b692_root_arm.json')
    _r, _n, sh = seal_hashes()
    return {
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))
               if TF else 'waits on the final table (relay data/b692_table_final.json)'),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally' if RA_
               else 'waits on the root and its arm (relay data/b692_root_arm.json), computed after the entry'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }


def scores(*a):
    """`scores [dry]` writes data/b692_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b692_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        return
    if close:
        put_json('b692_scores_close.json', dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, 'b692_scores.json')):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('b692_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def scores_line(S):
    """the entry's scores line, composed from the scores bank alone (the act arm G-ENTRY-SCORES-EQUAL composes it the same way and compares)."""
    return '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.'


# ================================================================================ THE RECORD: THE ENTRY BEFORE THE ROOT, THE TRAIL CARRYING IT
def TRAIL_HEAD():
    return ('### b692 — lane two, act one hundred and nineteen, the research act under (R302): b691’s post-root items by corrigendum; the '
            'suite-parts arm repaired; the dependency-circuit reading built and run at SIDE-explicit-formula; clause-dominance read; the triage '
            'raised by class')


def _calls():
    return jl('b692_author_answers.json').get('calls') or []


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _figs():
    """the figures the title and the entry carry, each read from its bank."""
    dm = re.search(r'CLAUSE-DOMINANCE (\d+) OF (\d+) FACES KERNELS REACHED', rdn('b692_circuit_dominance.txt'))
    fin = re.search(r'THE CLAUSE`S FACE IN (\d+) OF (\d+) FACES THE PAGE NAMES', rdn('b692_circuit_dominance.txt'))
    rb = rdn(K.READING_BANK)
    w = re.search(r'SAME-TYPE THEOREM PAIRS (\d+), AT OR UNDER FEW = (\d+): (\d+)', rb)
    sh = re.search(r'SHORTS (\d+) ;', rb)
    se = re.search(r'SERIES (\d+) NAMES, THE LONGEST CHAIN (\d+)', rb)
    ld = re.search(r'LOAD`S THREE HIGHEST ([^.]*)\.\*\*', rb)
    rf = re.search(r'LINES DIFFERING (\d+) \(HAND ONLY (\d+), OF WHICH IN THE CLOSURE (\d+) ; TEXT ONLY (\d+)\)', rdn('b692_readfirst_diff.txt'))
    rc = re.search(r'ITEMS (\d+) ; CITED BY THE TEXT ITSELF (\d+)', rdn('b692_readfirst_closure.txt'))
    sl = re.search(r'DEFECTS PER ACT ([\d.]+) -> ([\d.]+) AS ARMS ([\d.]+) -> ([\d.]+) ; THE FACTOR ([\d.]+)', rdn('b692_suite_load.txt'))
    sa = re.search(r'WITH A SOURCE READ (\d+) ; ANSWERING A DEFECT ALONE (\d+)', rdn('b692_suite_load.txt'))
    heads = [x.get('head') or '' for x in jl('b692_orders_lines.json').get('lines') or []]
    i = lambda m, k: int(m.group(k)) if m else None   # noqa: E731
    return dict(dom=(i(dm, 1), i(dm, 2)), faces=(i(fin, 1), i(fin, 2)), pairs=i(w, 3), pairs_all=i(w, 1), few=i(w, 2), shorts=i(sh, 1),
                series=(i(se, 1), i(se, 2)), load=ld.group(1) if ld else '', rf=(i(rf, 1), i(rf, 2), i(rf, 3), i(rf, 4)), rc=(i(rc, 1), i(rc, 2)),
                sl=sl.groups() if sl else None, sa=(i(sa, 1), i(sa, 2)), carried=sum(1 for h in heads if '` CARRIED (' in h),
                discharged=sum(1 for h in heads if '` DISCHARGED BY READING (' in h), retired=0, orders=len(heads))


def _title():
    """the ferry's form, adjusted to what the act did: the kernel at its main's tag v0.34.1, no other faces kernel reached, no order retired."""
    f = _figs()
    return ('## The dependency-circuit reading at SIDE-explicit-formula v0.34.1: CLAUSE-DOMINANCE %s of %s, WIDTH %s pairs, SHORTS %s; '
            'READFIRST-CLOSURE against the hand list, %s lines differ; %s stale orders carried, %s discharged by reading; b691’s post-root items by '
            'corrigendum' % (f['dom'][0], f['dom'][1], f['pairs'], f['shorts'], f['rf'][0], f['carried'], f['discharged']))


def _finding_text():
    """the FINDINGS entry, composed before the root: its scores line from the scores bank alone (data/b686_rules.txt row (1)); the root is
    carried by the trail record."""
    S = jl('b692_scores.json')
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b692_author_answers.txt'), re.M))
    c1 = _rl_lines('b692_record_lines.json') + ['-']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    sl = f['sl'] or ('-', '-', '-', '-', '-')
    e = ['', _title(), '',
         'The dependency-circuit reading is built and run: on SIDE-explicit-formula, the one faces kernel the act reached, the clause’s compiled face '
         'h2_sign lies in the closure of the main theorem h2_sign_iff_rh, and of the %s faces the page names it lies in the closure of %s -- '
         'h2_sign_iff_rh and forall_upto_iff_rh -- while the Li, arithmetic-limit, Taylor, register-4, height and Nyman–Beurling faces each reach '
         'RiemannHypothesis without it; SHORTS 0 on main, and a planted sorry on a scratch branch read as one short where it was planted.' % (
             f['faces'][1], f['faces'][0]), '',
         '*Filed at b692 on the author’s ruling `(R302)` and the author’s words at its prompts; %d questions put. Banks: relay '
         '`data/b692_closure_step.txt`, `data/%s` and its hashes bank, `data/%s`, `data/b692_circuit_bars.txt`, `data/b692_circuit_dominance.txt`, '
         '`data/b692_circuit_controls.txt`, `data/b692_circuit_shorts_branch.txt`, `data/b692_readfirst_diff.txt`, `data/b692_suite_load.txt`, '
         '`data/b692_circuit_spec.txt`, `data/b692_corrigendum.txt`, `data/b692_tool_repairs.txt`, `data/b692_triage_counts.txt`, '
         '`data/b692_candidates_priced.txt`.*' % (n_ans, K.CLOSURE_BANK, K.READING_BANK), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed; %d answers checked before they were acted on. '
         'b691 at its weight (FINDINGS :%s), its head line quoted.' % (cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-',
                                                                      checks, c1[0]), '',
         '**The corrigendum** (`(R302)`(2)): b691’s two items after the root entered by one generated entry in b678’s form (FINDINGS :%d), lettered '
         'b691’s (l), G-RULE-SUITE-PARTS failing undeclared, and (m), the trail commit’s subject amended before its push; the corrigenda bank '
         'appended; data/b692_rules.txt row (1): a commit made after the seal that fails an arm is left as it stands.' % K.CORRIGENDUM_LINE, '',
         '**The parts arm** (`(R302)`(2)): the pattern widened alone read the same governing lists and left b691’s banks failing, so on the author’s '
         'word the arm reads a governing part as met by itself or by its numbered halves; at HEAD b691’s run banks pass, the planted control fires.', '',
         '**The closure step** (`(R302)`(3)(a)): CircuitClosure.lean at the kernel’s root, imported by no module, and the workflow’s closure step '
         'committed alone on main; three runs, the third whole -- %s records over 179 programme modules, banked as a gz beside its text hashes bank; '
         'the print list equal line for line before and after, the modules untouched, no tag. Priced at four dispatches of 414 s; the two repairs of '
         'the script spent the price at the first faces kernel, so SIDE-lv-conservation is carried to b694.' % rdn(K.CLOSURE_BANK.replace(
             '.jsonl.gz', '_hashes.txt')).split('RECORDS ')[-1].split(' ;')[0], '',
         '**The readings** (`(R302)`(3)(b)): SERIES of h2_sign_iff_rh %s names, the longest chain %s; TERMINALS no premise and no axiom beyond the '
         'standard three; SHORTS %s; WIDTH %s theorem pairs of one type meeting in at most %s names, of %s same-type pairs -- copies of helper '
         'lemmas between the kernel, Zeta23 and the vendored trees, the native and the vendored Li converses not among them, their types '
         'differing; LOAD led by %s. The bars were banked before the run.' % (f['series'][0], f['series'][1], f['shorts'], f['pairs'], f['few'],
                                                                             f['pairs_all'], f['load']), '',
         '**CLAUSE-DOMINANCE** (`(R302)`(3)(c)): %s of %s faces kernels reached, SIDE-explicit-formula IN; SIDE-lv-conservation not reached; '
         'within the kernel the face in %s of %s faces’ closures.' % (f['dom'][0], f['dom'][1], f['faces'][0], f['faces'][1]), '',
         '**READFIRST-CLOSURE** (`(R302)`(3)(c)): from the ferry, %s paths cited by the text itself and %s items transitively; against the hand '
         'list %s lines differ -- %s on the hand list alone (%s of them reached through other banks), %s cited by the text alone; the diff banked, no '
         'bank rewritten.' % (f['rc'][1], f['rc'][0], f['rf'][0], f['rf'][1], f['rf'][2], f['rf'][3]), '',
         '**SUITE-LOAD** (`(R302)`(3)(d)): the tenth row; of 24 rule arms %s read a source defect, each answering it alone; defects per act %s to %s '
         'as arms rose %s to %s, the factor %s -- a ratio of means, not a fit.' % (f['sa'][0], sl[0], sl[1], sl[2], sl[3], sl[4]), '',
         '**INSTRUMENTS** (`(R302)`(3)(e)): I-40, the dependency-circuit reading, in the page’s own form.', '',
         '**The orders** (`(R302)`(4)): on the author’s word with its check, the %s stale orders written to OPEN_TRAILS one entry each -- carried %s, '
         'discharged by reading %s, retired %s; one discharged row demoted because its reading cites a tool, no bank.' % (
             f['orders'], f['carried'], f['discharged'], f['retired']), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b690’s specification, b691’s closing, triage and arms, and the '
         'faces page’s node list; it is re-read by b693’s re-cut act, which takes the push tool’s branch mode as a carry-time repair, and by b694, '
         'which takes SIDE-lv-conservation’s closure and the priced candidates. It strengthens the programme’s offering of a located clause by '
         'computing where the clause sits among the compiled faces instead of stating it.', '',
         '**Carried to:** b693 (the re-cut act: rule (2) of data/b690_rules.txt binding; push_gated.sh’s branch mode, closing b691’s (d)); b694 '
         '(SIDE-lv-conservation’s closure; W-ORD-EPSTEIN-COUNT-LEAN or a candidate priced in relay data/b692_candidates_priced.txt -- the Weil-face '
         'witness at Q0 or the regularity-uses bank); the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) “at v0.34” read as the kernel’s main, whose tag is v0.34.1, docstrings and twelve print-list names since v0.34; (2) the faces '
              'kernels read from the generator input’s rows, SIDE-explicit-formula’s node rows and the correspondence row’s SIDE-lv-conservation; (3) '
              'the kernel’s own names its three libraries, the vendored trees among them; (4) the price as four dispatches at b689’s 414 s; (5) the '
              'corrigendum generated by relay tools/b692_corrigendum.py in b678’s form, b678’s reader imported, as b689 and b690 did; (6) the main '
              'theorem h2_sign_iff_rh and the clause’s face h2_sign, a premise a Prop binder naming a programme definition of type Prop; (7) the '
              'kernel branches read from data/b691_epstein_cut.txt and data/b691_closing.txt beside the cut bank; (8) I-40 placed beneath the I-16 '
              'to I-39 footer; (9) one OPEN_TRAILS entry for each triage row')


def _trail_text():
    S, J = jl('b692_scores.json'), jl('b692_act_root.json')
    fj = jl('b692_findings.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b692_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b692_record_lines.json') + ['-']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R302) ratified.** (1) b691 at its weight. (2) The two items entered, the arm repaired, one rule. (3) The dependency-circuit reading: '
             'the closure step, the reader, the readings, the tenth row, INSTRUMENTS. (4) The triage by class. (5) W-ORD-EPSTEIN-COUNT-LEAN carried, '
             'two candidates priced. (6) The branches. (7) The readfirst bank. (8) The draft held at v5. (9) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b691’s weight), :%d (the corrigendum), :%s (the entry); OPEN_TRAILS.md:%d-:%d (the 35 orders); '
             'phase1.5/method/INSTRUMENTS.md I-40; this record.' % (c1[0], K.CORRIGENDUM_LINE, fj.get('entry_line'), K.ORDERS_LINES[0], K.ORDERS_LINES[1]), '',
             '**Act root:** b692 `%s` (previous `%s`, b691’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s (relay data/b692_author_answers.txt); none after the root.' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The kernels:** SIDE-explicit-formula -- the closure step ccec1ba, 59a867c, 4313875 on main, no tag; runs 39337850198, 39339047763, '
             '39340192180 and the shorts control 39342395110 at circuit-shorts-control-b692 (5866ff2), each read by its run id; SIDE-lv-conservation '
             'carried to b694.', '',
             '**The banks:** the closure relay data/b692_closure_step.txt and data/%s; the readings relay data/%s, data/b692_circuit_dominance.txt, '
             'data/b692_circuit_controls.txt, data/b692_readfirst_diff.txt, data/b692_suite_load.txt; the spec relay data/b692_circuit_spec.txt; the '
             'corrigendum relay data/b692_corrigendum.txt; the repair relay data/b692_tool_repairs.txt.' % (
                 K.CLOSURE_BANK.replace('.jsonl.gz', '_hashes.txt'), K.READING_BANK), '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b692_closing.txt).', '',
             '**The open orders:** `W-ORD-EPSTEIN-COUNT-LEAN` (b694, its trigger read as met; two candidates priced); `W-ORD-CIRCUIT-READING` built '
             'at SIDE-explicit-formula, SIDE-lv-conservation`s closure carried to b694; `W-ORD-CORRESPONDENCE-BEHIND-SCOPE` (the next re-cut act); the '
             '12 orders carried at OPEN_TRAILS :%d-:%d.' % K.ORDERS_LINES, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b692_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S, C = jl('b692_scores.json'), jl('b692_scores_close.json')
    L = ['=' * 104, 'b692 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s%s' % (
        k2, S[k2][0], S[k2][1], ('  ### AT THE CLOSE: %s -- %s' % (C[k2][0], C[k2][1])) if (S[k2][0] == 'PENDING' and C.get(k2)) else '')
        for k2 in SCORE_KEYS]
    L += [''] + rdn('b692_defects.txt').rstrip(NL).split(NL)
    put_txt('b692_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b692_scores.json', 'b692_findings.json', 'b692_trail.json', 'b692_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b692_record_lines.json') + ['-']
    L = ['b692 -- THE COMPONENTS, BANKED UNDER (R302).', '',
         '### COMPONENT 0 : the citation check (data/b692_citation_check.txt), step zero (data/b692_ferry.txt, data/b692_readfirst.txt, '
         'data/b692_stepzero.txt, data/b692_tests_stepzero.txt, data/b692_rowgen_stepzero.txt, data/b692_branches.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b691`s weight FINDINGS :%s, the corrigendum :%d (data/b692_corrigendum.txt), the arm repaired (data/b692_tool_repairs.txt '
         'row 1, data/b692_parts_after.txt), the rule (data/b692_rules.txt)' % (c1[0], K.CORRIGENDUM_LINE),
         '### COMPONENT 2 : the closure step (data/b692_closure_step.txt, data/%s) ; N2 %s' % (K.CLOSURE_BANK.replace('.jsonl.gz', '_hashes.txt'), S['N2'][0]),
         '### COMPONENT 3 : the reader and the readings (data/%s, data/b692_circuit_dominance.txt, data/b692_circuit_controls.txt, '
         'data/b692_readfirst_diff.txt, data/b692_circuit_spec.txt, data/b692_suite_load.txt) ; N3 %s ; N4 %s' % (K.READING_BANK, S['N3'][0], S['N4'][0]),
         '### COMPONENT 4 : INSTRUMENTS I-40 (data/b692_instruments_diff.txt), the triage by class (data/b692_triage_counts.txt), the orders at '
         'OPEN_TRAILS :%d-:%d (data/b692_orders_lines.json)' % K.ORDERS_LINES,
         '### COMPONENT 5 : the carry-time reading (data/b692_tool_repairs.txt), the dry-run steps (data/b692_reg_gate.txt), the seal '
         '(data/b692_seal_hashes.json), the suite in five parts, the per-part seconds (data/b692_arm_seconds.txt) ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('b692_components.txt', L)
    print(NL.join(L[2:]))


def _land_one(path, head, e, bank, extra):
    if odd_lines(e):
        sys.exit('### ODD BACKTICKS -- NOTHING WRITTEN: %s' % odd_lines(e)[:3])
    guard_absent(path, head)
    r = append_to(path, e)
    ln = read_head(path, head)
    put_json(bank, dict(extra, line=ln, head=head, append=r, at=utc()))
    return ln


def findings(*a):
    t, e = _finding_text()
    e = conv(e)
    dry = 'dry' in a
    cells_, fired = screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells_)
        return
    if not os.path.isfile(os.path.join(D, 'b692_scores.json')):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, 'b692_findings.json', dict(title=t))
    j = jl('b692_findings.json')
    j['entry_line'] = ln
    put_json('b692_findings.json', j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = conv(_trail_text())
    dry = 'dry' in a
    cells_, fired = screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells_)
        return
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b692_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


FACE_REL = 'data/b692_registration_2026-10-19.txt'
FACE = os.path.join(D, 'b692_registration_2026-10-19.txt')


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written -- converted by conv and run through the screens their landing runs, the needles the face names read in
    each; prints DRY-RUN STEP : CLEAN and exits 0 only when both screens are quiet and every needle is found. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = conv(text)
        print('  %s (the screens):' % which)
        cells_, fired = screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = _face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells_ and not fired and nd and not miss
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells_ or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


def gatebanks(*a):
    """the gate's steps between the face and the lock (b665's order), each tool's output banked by this route, never by a shell redirect."""
    import gate_hash as G
    env = dict(os.environ, PYTHONIOENCODING='utf-8')

    def runb(args, out):
        r = subprocess.run([sys.executable] + args, capture_output=True, cwd=ROOT, env=env)
        b_ = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            open(p + '.tmp', 'wb').write(b_)
            os.replace(p + '.tmp', p)
        return r.returncode, b_.decode('utf-8', 'replace')
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b692_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b692_regspec.py')], 'b692_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b692_satisfiable.json', '--emit', 'b692'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b692_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b692_census_stepzero.txt'), ('b327_faces_census.py', 'b692_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b692_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b692'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b692_reg_gate.txt', 'data/b692_reg_termscan.txt', 'data/b692_regspec_run.txt', 'data/audit_b692_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b691's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '2026-10-19-b692'
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
    put_json('b692_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b692':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b692`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b692_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b692_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b692_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b692 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b692 (the last export b691`s, D:/MY-DOwnloads/mirror-refresh-2026-10-19-b691.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b692_mirror.txt', L)
    put_json('b692_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


# ================================================================================ THE CARRY-TIME READING (the ferry's Component 5)
REPAIRS = [
    ('THE STANDING SET FOR b692 (answering (R302)(2) and N5: no standing arm added): the standing arms are b691`s face`s (G2) arms less b691`s',
     'act arms, the twenty-four rule arms of tools/rule_arms.py among them; STANDING_ADDED empty (tools/b692_worklist.py).'),
    ('THE PARTS ARM`S REPAIR READ BY THE SUITE (answering (R302)(2)): tools/rule_arms.py is this act`s one repaired shared tool, its diff row 1',
     'above; G-INSTRUMENTS-UNEDITED reads every other instrument unedited, correspondence_gen.py and its test (b691`s repairs) back among them;',
     'rule_arms.py is sealed with this act`s tools (tools/b692_worklist.py SEALED), its hash compared at the close (N5).'),
    ('THE READER A SEALED TOOL (answering (R302)(3)(b)): tools/circuit_read.py, new this act, sealed with the act`s tools; G-CONVERSION-ONE and',
     'G-DELETE-FREE read the b692 tools and the repaired tool as before.'),
    ('THE RUNNER ARMS OVER THIS ACT`S FOUR RUNS AND NO MERGE (answering (R302)(3)(a)-(b): the closure step on main, no cut, no tag): G-RUNNER-READ',
     'reads four rows -- after, after2, after3 at the closure step`s three commits and shorts at the scratch branch`s tip -- each at its own',
     'ref; G-RUNNER-GATE four gate readings; G-MERGES-ON-GATE reads SIDE-explicit-formula`s main at the third closure commit, no merge and no',
     'tag there, v0.34 and v0.34.1 unmoved; G-WORKFLOW-FILES reads the workflow at main equal to the one the act wrote at ccec1ba, the closure',
     'step in it, the print list against the third run`s print bank.'),
    ('THE PLACE-papers SCOPE (answering (R302)(3)(e) and (4)): G-PP-SCOPE allows FINDINGS, OPEN_TRAILS and INSTRUMENTS.md; the faces page among',
     'the files read unedited (CURRENTS).'),
    ('THE PREVIOUS ACT`S WINDOW IN THIS SAME SESSION: G-EDIT-ROUTE`s previous-act window reads b691`s capture after its post-push suite -- from the',
     'call that combined b691`s post-push parts to (R302)`s line -- in session 2c300355.'),
    ('THE STEP-ZERO TESTS` SET: G-STEPZERO-TESTS reads the step-zero bank`s failing set -- test_chain_page.py (9) and test_chain_page_b638.py',
     '(4)-(7) -- as the bank recorded it, against the tests tracked at relay f5318624.'),
    ('THE BRANCHES ARMS OVER THIRTEEN DELETES (answering (R302)(6) and the author`s word at its prompt): G-BRANCHES-DELETED reads the five',
     'names gone from relay and PLACE-papers and the eight kernel branches gone from SIDE-rcurve and SIDE-explicit-formula, local and remote;',
     'G-DELETES-ONE-BRANCH reads thirteen deletes of one branch each, no glob; the scratch branch circuit-shorts-control-b692 deleted at the close',
     'and read by the closing.'),
]
CARRY_HEAD = '### THE CARRY-TIME READING OF THE TOOLS (the ferry`s Component 5), AGAINST b691`S SEALED COPIES'


def _fn_src(src, name):
    """a top-level function's source, from its `def` line to the next top-level line; '' where the tool carries no such function."""
    if ('\ndef %s(' % name) not in src:
        return ''
    i = src.index('\ndef %s(' % name) + 1
    m = re.search(r'\n(?=\S)', src[i + 1:])
    return src[i:i + 1 + m.start() + 1] if m else src[i:]


def _const_src(src, name):
    m = re.search(r'(?ms)^%s = .*?(?=^\S)' % re.escape(name), src)
    return m.group(0) if m else ''


INST_READ = ('edit_route.py', 'e0_rule.py', 'b678_corrigendum.py', 'chain_page.py', 'b670_record.py', 'b672_record.py', 'repair_snapshot.py',
             'correspondence_gen.py')


def repairs(*a):
    """the carry-time section of data/b692_tool_repairs.txt: each tool carried from a sealed b691 copy read against b691's seal hash first and
    its diff counted by hunks; the standing instruments this act's tools import read against the last seal record naming them and against
    relay before the act; the repaired readings' diffs against b691's sealed copies printed whole; row 1 (the repaired shared tool) above it
    read. The bank's head is kept: the route replaces only its own section, from its head line to the bank's end."""
    import difflib
    import hashlib
    seal = jl('b691_seal_hashes.json').get('tools') or {}
    rows = []
    for t0 in ('b691_citation.py', 'b691_closing.py', 'b691_reg_gate.py', 'b691_regspec.py', 'b691_tests.py', 'b691_worklist.py',
               'b691_record.py', 'b691_checks.py'):
        t1 = t0.replace('b691_', 'b692_')
        old, new = os.path.join(T, t0), os.path.join(T, t1)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        ex = os.path.exists(new)
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8',
                           errors='replace').stdout if ex else ''
        rows.append((t0, t1, now, seal.get(t0), len(re.split(r'(?m)^(?=@@ )', d)[1:]), ex))
    inst = {}
    for t in INST_READ:
        nowh = hashlib.sha256(open(os.path.join(T, t), 'rb').read()).hexdigest()
        acts = [x for x in ('b691', 'b690', 'b689', 'b688', 'b687', 'b686', 'b685', 'b684', 'b683') if (jl('%s_seal_hashes.json' % x).get('tools') or {}).get(t)]
        headh = hashlib.sha256(subprocess.run(['git', '-C', ROOT, 'show', '%s:tools/%s' % (K.PRE_RELAY, t)], capture_output=True).stdout).hexdigest()
        inst[t] = (nowh, acts[0] if acts else None, (jl('%s_seal_hashes.json' % acts[0])['tools'][t]) if acts else None, headh,
                   g(ROOT, 'log', '-1', '--format=%h %cI', '--', 'tools/' + t).strip())
    s0r, s1r = rd(os.path.join(T, 'b691_record.py')), rd(os.path.join(T, 'b692_record.py'))
    s0c, s1c = rd(os.path.join(T, 'b691_checks.py')), rd(os.path.join(T, 'b692_checks.py'))
    nd = []
    for (a0, f0), (a1, f1), s0, s1 in ((('b691_record.py', 'prev_capture'), ('b692_record.py', 'prev_capture'), s0r, s1r),
                                       (('b691_checks.py', 'branches_ok'), ('b692_checks.py', 'branches_ok'), s0c, s1c),
                                       (('b691_checks.py', 'runner_ok'), ('b692_checks.py', 'runner_ok'), s0c, s1c),
                                       (('b691_checks.py', 'merges_ok'), ('b692_checks.py', 'merges_ok'), s0c, s1c),
                                       (('b691_checks.py', 'wf_ok'), ('b692_checks.py', 'wf_ok'), s0c, s1c)):
        nd += list(difflib.unified_diff(_fn_src(s0, f0).split(NL), _fn_src(s1, f1).split(NL) if s1 else [],
                                        '%s %s (sealed)' % (a0, f0), '%s %s%s' % (a1, f1, '' if s1 else ' (NOT YET CARRIED)'), n=1, lineterm=''))
    for c in ('CURRENTS', 'NEED', 'STEPZERO_FAILING'):
        nd += list(difflib.unified_diff(_const_src(s0c, c).split(NL), _const_src(s1c, c).split(NL), 'b691_checks.py %s (sealed)' % c,
                                        'b692_checks.py %s' % c, n=1, lineterm=''))
    old = rdn('b692_tool_repairs.txt')
    head = old[:old.index(CARRY_HEAD)] if CARRY_HEAD in old else old
    row1 = '  ROW 1  tools/rule_arms.py' in head
    L = [CARRY_HEAD + ' (%s)' % utc(), '',
         '### rows are repairs with the defect or order they answer, after the carried tools: b691`s sealed copy and its seal record; the hunks of',
         '### the diff to b692`s copy. Every hunk is the act`s own text -- its names, its banks, its sections and its predicates over this act`s',
         '### banks -- save the repairs below. The repaired shared tool is row 1 above, with its diff.', '']
    for t0, t1, now, s, nh, ex in rows:
        L.append('  %-20s -> %-20s b691 sealed %s ; the seal`s record %s ; %s ; hunks %s' % (t0, t1, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh if ex else 'NOT YET CARRIED'))
    for t, (nowh, act, sh, headh, last) in inst.items():
        L.append('  %-22s  the standing instrument, unedited in this act: %s ; at relay %s %s ; the last seal record naming it (%s`s) %s ; its last '
                 'commit %s' % (t, nowh[:16], K.PRE_RELAY, headh[:16], act or 'NONE', (sh or '### NONE')[:16], last))
    L.append('')
    for i, r in enumerate(REPAIRS, 1):
        L += ['  REPAIR %d -- %s' % (i, r[0])] + ['  ' + x for x in r[1:]]
    L += ['', '### THE DIFF OF THE REPAIRED READINGS AGAINST b691`S SEALED COPIES (tools/b691_record.py sha256 %s, tools/b691_checks.py sha256 %s), '
          'WHOLE:' % ((seal.get('b691_record.py') or '### NONE')[:16], (seal.get('b691_checks.py') or '### NONE')[:16])]
    L += ['    ' + l for l in nd]
    carried = sum(1 for r in rows if r[5])
    unedited = all(v[0] == v[3] for v in inst.values())
    L += ['', '### ### **REPAIRS %d ; THE SEALED COPIES %s ; TOOLS CARRIED %d OF %d ; THE STANDING INSTRUMENTS UNEDITED %s ; THE REPAIRED SHARED '
          'TOOL 1, ITS DIFF BANKED %s ; THE REPAIRED READINGS` DIFF LINES %d.**' % (
              len(REPAIRS), 'AGREE' if all(s == now for _a, _b, now, s, _n, _e in rows) else '### DIFFER', carried, len(rows), unedited, row1, len(nd))]
    put_txt('b692_tool_repairs.txt', head.rstrip(NL).split(NL) + ['', ''] + L)
    print(L[-1])


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, c1=c1, dispatch=dispatch, runner=runner, prints=prints, triage_counts=triage_counts,
              orders=orders, commands=commands, defects=defects, kernels=kernels, rootbanks=rootbanks, root=root, root_arm=root_arm,
              table_final=table_final, armsecs=armsecs, scores=scores, desk=desk, components=components, findings=findings, trail=trail,
              drycheck=drycheck, gatebanks=gatebanks, mbuild=mbuild, mroot=mroot, mverify=mverify, mbank=mbank, repairs=repairs)

if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ROUTES:
        print('usage: b692_record.py ' + ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    ROUTES[r](*sys.argv[2:])
