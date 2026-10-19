# -*- coding: utf-8 -*-
"""b691_record.py -- THE ACT'S RECORD TOOL, b691 under (R301).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b691's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b690_record.py in stages: the helpers, the guarded landing, the readers, step zero's rowgen and branches
### routes, Component 1's weight line and the answers route first; the late routes at Component 5. Every python child is started as
### `python -X utf8`, no environment mapping passed. Routes: `python tools/b691_record.py <route> [dry]`. After the seal this tool's own print
### is how the entry, the dry entry and the trail are read (data/b690_rules.txt row (1), binding from this act).
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
import b691_worklist as K          # noqa: E402

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
        'b691_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b691_findings.json': dict(entry_line=99999, title='stand-in'),
        'b691_trail.json': dict(line=99999),
        'b691_act_root.json': dict(root='0' * 64, previous='422989da' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b691's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b691_scanfile_%s.md' % tag)
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


BRANCH_FATES = ('DELETED', 'KEPT')


def read_branch_row(r):
    """a row of data/b691_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


TRIAGE_WORDS = ('CARRY', 'DISCHARGED-BY-READING', 'RETIRE')


def read_triage_row(r):
    """a row of data/b691_orders_triage.json: the order's name (W-ORD-...), its OPEN_TRAILS line (an int), the entering act, the trigger as
    written (non-empty), whether it can still fire (a bool) with its why, and a disposition (one of TRIAGE_WORDS) with its ground; returns
    (name, disposition)."""
    if not isinstance(r, dict) or not re.match(r'^W-ORD-[A-Z0-9-]+$', r.get('name') or '') or not isinstance(r.get('line'), int) \
            or not (r.get('trigger') or '').strip() or not isinstance(r.get('can_fire'), bool) or not (r.get('why') or '').strip() \
            or r.get('disposition') not in TRIAGE_WORDS or not (r.get('ground') or '').strip():
        raise ValueError('triage row of another shape: %r' % (str(r)[:120],))
    return r['name'], r['disposition']


def read_runner_row(r):
    """a row of data/b691_runner_rows.json: the kernel, its label, the ref (40 hex), the run id and the gate; returns (kernel, label, gate)."""
    if not isinstance(r, dict) or not re.match(r'^SIDE-[\w-]+$', r.get('kernel') or '') or not re.match(r'^[\w-]+$', r.get('label') or '') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['kernel'], r['label'], r['gate']


READERS = ['read_score_row', 'read_head', 'read_branch_row', 'read_triage_row', 'read_runner_row']


# ================================================================================ STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE (b670's route, carried)
def roster():
    """the 19 roster tables of data/b586_corroboration.txt :34, at the paths that bank read (carried from b670_record.py :548-:552)."""
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b691_rowgen_<stage>.txt."""
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
    L = ['b691 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b691_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R301)(9))
def branches(*a):
    """every branch (R301)(9) names, its tip read before any delete, its fate; any branch of b690 that --merged lists and the ruling does not
    name, reported and KEPT. data/b691_branches.txt (.json)."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    named = set((r['repo'], r['branch']) for r in rows)
    extra = []
    for repo, _bs in K.DELETE:
        for x in g(repo, 'branch', '--merged', 'main', '--format=%(refname:short)').split(NL):
            x = x.strip()
            if (x.startswith('push-b690') or x.endswith('-b690')) and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b691 -- STEP ZERO, (R301)(9): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; listed by `git branch --merged main --list <name>` ; fate. Deleted',
         '### by name in the house form, each delete command naming one branch with no glob in any half, one command per message, in sequence; no',
         '### branch the ruling does not name.']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### branches of b690 that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; TO BE DELETED %d ; UNNAMED OF b690 %d.**' % (
        len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), len(rows), len(extra))]
    put_txt('b691_branches.txt', L)
    put_json('b691_branches.json', dict(at=utc(), rows=rows, extra=[list(x) for x in extra]))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R301)(1)
WH = ('*Appended 2026-10-19 by b691 to b690’s entry (:9390), under `(R301)`(1) -- b690 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b690_closing.txt), READING 3 ON THE RECORD:*')
WB = (' “b690 closed: relay 55e34098, PLACE-papers 64936ae; suite 114 of 114; root 422989da790bc2ed…; 2 prompts answered; 7 defects” '
      '(data/b690_closing.txt :1), the closing pushed and read back at relay 9fc2c81b (data/b690_closing_push_out.txt). Reading 3 by row '
      '(data/b690_reading3.txt): rows outside LICENSED or CITED 345 against b680’s 361, the drop of 16 the seven kernels cut since b680; '
      'Correspondence rows behind 57 against 55, the two added rows that read “no tag” at b680, the generator’s own claim 0; orders 165, 38 open, '
      '35 open and older than ten acts with no trigger met; keystone lag median 105 (b680: 96), maximum 244; residues 7, 3 carried with their '
      'triggers (R3b and the two in SIDE-li-map); rules 21, 13 with an arm, two traceable with a live trace and no arm fitting neither of the '
      'ruling’s words; the pair rule’s four conditions holding at both reading acts in 1 of 4; P3 named at 3 lines outside the ledgers, two '
      'kernel docstrings at EpsteinQ0.lean :106 and :110-:111 still reading “stated, not proved”. The faces line regenerated on the author’s '
      'two words with “(b689)” in the tail, the control re-emitting the committed page byte for byte, two lines changed, the header’s '
      'generation tag v0.26 = 82550e4 entered as a reading; the circuit spec at 9 rows with READFIRST-CLOSURE, W-ORD-CIRCUIT-READING at '
      'OPEN_TRAILS :14980; the three rules banked. Suite 114 arms (89 standing, 25 act-local), 114 of 114 before and after the push, the '
      'standing arms’ own checks about 0.2 s together and the shared-source builds the cost (the act-root chain 340-390 s), the pre-run’s '
      'standing-b part at 463 s; all eight scores HELD; mirror-refresh-2026-10-19-b690.zip CLEAN with the root line. Seven defects '
      '(data/b690_defects.txt): (a) three file reads through a python -c print; (b) five faults in the reading routes’ earlier forms, caught by '
      'hand-reading and fixed before the aggregate; (c) the rules census in words outside the sort rule it cites, corrected; (d) the rules bank '
      'committed again with the census after its alone-commit; (e) the navigator’s “PROSE/VACUOUS” where the sort rule has its own words; (f) '
      'the navigator’s title figure “rows licensed” that no reading takes; (g) the methods bank indented so a standing rule arm read it empty, '
      'caught by the pre-run. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b691_record_lines.json', 'c1', entry=K.B690_ENTRY,
         check=[('FINDINGS.md', K.B690_ENTRY, '## Reading 3: 345 rows outside LICENSED or CITED'), ('OPEN_TRAILS.md', K.B690_TRAIL, '### b690')], dry=dry)


# ================================================================================ THE ANSWERS BANK (b690's route, carried)
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
    """data/b691_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
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
    head = ['### b691 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b691_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b691_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 2: THE TIE, (R301)(2) -- the rule and the rows printed before any naming
TIE_DOCS = (('SIDE-archimedean', 100, 'b647_table_SIDE-archimedean.txt'), ('SIDE-rcurve', 113, 'b647_table_SIDE-rcurve.txt'))


def tie(*a):
    """data/b674_rules.txt row (2) printed verbatim (:8-:11), then each tied document's row of data/b670_licensed_table.txt and the verdict of
    its per-document table, read by line; the rule applied clause by clause in its own order -- equal OVERREACHES; a declared suite failure
    (b690's face, its declaration line); the count of rows outside LICENSED/CITED of any kind (UNDERSTATES counted); the larger table -- and
    only then the document named. data/b691_tie.txt (.json)."""
    rl = rdn('b674_rules.txt').split(NL)[7:11]
    if not rl or not rl[0].startswith('  (2) THE TIE-BREAK BEYOND THE COUNT'):
        sys.exit('### data/b674_rules.txt :8 DOES NOT CARRY ROW (2) -- NOTHING WRITTEN')
    lt = rdn('b670_licensed_table.txt').split(NL)
    face = rdn(os.path.basename(K.B690_FACE))
    decl = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', face)
    docs = []
    for k, ln, tb in TIE_DOCS:
        row = lt[ln - 1]
        if not row.startswith('  %s docstrings' % k):
            sys.exit('### data/b670_licensed_table.txt :%d IS NOT %s`s ROW -- NOTHING WRITTEN' % (ln, k))
        t = rdn(tb)
        v = re.search(r'ROWS (\d+) ; MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+)', t)
        vl = [l for l in t.split(NL) if l.startswith('### ### **%s: ROWS' % k)]
        docs.append(dict(kernel=k, line=ln, row=row.strip(), table=tb, verdict=vl[0] if vl else '', rows=int(v.group(1)), under=int(v.group(3)),
                         over=int(v.group(4)), unlic=int(v.group(5)), failing=bool(decl and k in decl.group(1))))
    L = ['b691 -- COMPONENT 2, (R301)(2): THE TIE AT 2 AND b674`S TIE-BREAK RULE, PRINTED BEFORE EITHER DOCUMENT IS NAMED (%s)' % utc(), '',
         '### THE RULE, VERBATIM FROM relay data/b674_rules.txt :8-:11:'] + ['  ' + l for l in rl] + [
         '', '### THE TABLE ROWS, VERBATIM (relay data/b670_licensed_table.txt), AND EACH DOCUMENT`S TABLE VERDICT:']
    for d in docs:
        L += ['  :%d  %s' % (d['line'], d['row']), '       relay data/%s: %s' % (d['table'], d['verdict'])]
    steps = []
    a_, b_ = docs
    steps.append(('equal OVERREACHES counts', a_['over'] == b_['over'], '%s %d, %s %d' % (a_['kernel'], a_['over'], b_['kernel'], b_['over'])))
    steps.append(('neither carries a declared suite failure (b690`s face, its declaration: %s)' % (decl.group(1) if decl else '### UNREAD'),
                  not a_['failing'] and not b_['failing'], 'NONE named' if not (a_['failing'] or b_['failing']) else 'named'))
    anyk = lambda d: d['over'] + d['under'] + d['unlic']   # noqa: E731
    steps.append(('the count of rows outside LICENSED/CITED of any kind (UNDERSTATES counted)', None,
                  '%s %d, %s %d' % (a_['kernel'], anyk(a_), b_['kernel'], anyk(b_))))
    if anyk(a_) != anyk(b_):
        cut, why = (a_ if anyk(a_) > anyk(b_) else b_), 'the greater count of any kind'
    elif a_['rows'] != b_['rows']:
        cut, why = (a_ if a_['rows'] > b_['rows'] else b_), 'the counts of any kind equal; the larger table (%s %d rows, %s %d)' % (
            a_['kernel'], a_['rows'], b_['kernel'], b_['rows'])
    else:
        cut, why = None, 'the counts and the tables equal -- the rule does not decide; raised'
    L += ['', '### THE RULE APPLIED, CLAUSE BY CLAUSE IN ITS OWN ORDER:'] + ['  %s: %s (%s)' % (s, '' if ok is None else ok, w) for s, ok, w in steps] + [
        '  the larger table: %s' % why,
        '', '### ### **THE TIE BROKEN BY b674`S ROW (2): %s IS CUT -- %s.**' % (cut['kernel'] if cut else '### NONE', why)]
    put_txt('b691_tie.txt', L)
    put_json('b691_tie.json', dict(at=utc(), rule=rl, docs=docs, cut=cut['kernel'] if cut else None, why=why))
    print(NL.join(L))


# ================================================================================ THE RUNS AND THE PRINTS (b689's routes, carried; per terminal)
STD3 = ('Classical.choice', 'Quot.sound', 'propext')


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def _deps(ax):
    """the axioms output read per terminal: [(name, [axioms] or None for 'does not depend on any axioms')], wrapped lists rejoined."""
    out = []
    for n, d in re.findall(r"^'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)",
                           re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', ax), re.M):
        out.append((n, [x.strip() for x in d.split('[', 1)[1].rstrip(']').split(',') if x.strip()] if d.startswith('depends') else []))
    return out


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <note...>`: the kernel's run read by its id; the artifact listed, downloaded by its id into
    memory, its sha256 against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP;
    the axioms output of the print step banked whole, every name of the list matched to one printed line, each terminal's axioms read against
    the standard three. data/b691_runner_<kernel>_<label>.txt, data/b691_axioms_<kernel>_<label>.txt and a row of data/b691_runner_rows.json."""
    import hashlib
    import io as _io
    import zipfile
    kernel, run_id, ref, label, note = a[0], int(a[1]), a[2], a[3], ' '.join(a[4:])
    repo = 'psinary-sketch/' + kernel
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(kernel=kernel, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None)
    L = ['b691 -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (kernel, label.upper(), utc()), '',
         '### the dispatch: %s ; the ref input %s' % (note, ref),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt'))]
    T_ = {}
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
                    T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
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
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d:' % (row['build_exit'], len(row['errors']))] + ['    ' + l for l in row['errors'][:40]] + [
          '### the log`s last lines:'] + ['    ' + l for l in blog.rstrip(NL).split(NL)[-8:]] + [
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
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d OF %d ; SORRYAX %d ; '
          'OUTSIDE THE STANDARD THREE %d ; GATE %s.**' % (
              run_id, label, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']),
              len(deps), len(tg), sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), row['gate'])]
    read_runner_row(row)
    put_txt('b691_runner_%s_%s.txt' % (kernel, label), L)
    if row['artifact_sha256']:
        put_txt('b691_axioms_%s_%s.txt' % (kernel, label), ax.split(NL) if ax else ['### EMPTY'])
        put_txt('b691_buildlog_%s_%s.txt' % (kernel, label), blog.rstrip(NL).split(NL))
    j = jl('b691_runner_rows.json') if os.path.isfile(os.path.join(D, 'b691_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('b691_runner_rows.json', dict(rows=rows))
    print(NL.join(L[:14] + L[-3:]))


def prints(*a):
    """`prints <kernel> <before bank> <after bank>`: the 'before' terminals' printed lines compared with the same names' lines in the 'after'
    bank, line for line by name; the raw axioms banks compared byte for byte beside. data/b691_prints_<kernel>.txt."""
    kernel, bb, ab = a[0], a[1], a[2]
    b, f = rdn(bb), rdn(ab)
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bd, fd = dict(_deps(b)), dict(_deps(f))
    diff = [(n, bd[n], fd.get(n)) for n in bd if fd.get(n) != bd[n]]
    new = [n for n in fd if n not in bd]
    L = ['b691 -- THE PRINTS OF %s BEFORE AND AFTER THE CUT, BY NAME AND LINE FOR LINE (%s)' % (kernel, utc()), '',
         '### before: relay data/%s (%d terminals) ; after: relay data/%s (%d terminals) ; the two banks equal line for line: %s ; rows are the '
         'terminals that differ:' % (bb, len(bd), ab, len(fd), b == f)] + (['    %s : %s | %s' % d for d in diff] or ['    NONE']) + [
        '### the names printed after and not before: %d' % len(new)] + ['    %s %s' % (n, fd[n]) for n in new]
    L += ['', '### ### **BEFORE %d TERMINALS ; EACH PRINTED AFTER %s ; DIFFERING %d ; NEW %d ; EQUAL LINE FOR LINE %s.**' % (
        len(bd), all(n in fd for n in bd), len(diff), len(new), b == f)]
    put_txt('b691_prints_%s.txt' % kernel, L)
    print(L[-1])


# ================================================================================ COMPONENT 2: THE QUOTATION SEARCH, data/b690_rules.txt row (2)
# ### one distinctive substring per removed or changed line of the cut, each checked to stand in its own removed line before it is searched
QUOTE_NEEDLES = ('R-Curve EQUIVALENCE engine', 'structural/logical core of the PROVEN', 'consolidating P22 Phases', 'V strictly monotone on every R-curve',
                 'driving the monotonicity', 'Phase-66 SIDE closure', 'seven-class catalogue', 'margin. The route shares its bottom step',
                 'zenodo.19938917', 'equivalence machinery. Conclusive checkpoint', 'This is the decisive')
# ### the second shape, case-blind and shorter (b690's lesson: a case-exact needle misses a quote re-set in bold or another case), one per
# ### removed line by case-blind containment; both shapes' yields printed
QUOTE_WIDE = ('equivalence engine', 'structural/logical core', 'P22 Phases', 'monotone on every R-curve', 'positivity Re(', 'Phase-66',
              'seven-class', 'shares its bottom step', '19938917', 'conclusive checkpoint', 'decisive (ii)')


# ### C4 (4), the EpsteinQ0 docstring re-cut: one needle per removed line, each on the clause the cut removes (not on text it keeps)
QUOTE_EPSTEIN = ('NUMBER** -- stated, not proved; open', 'the count) -- each', 'stated, not proved; open. -/')
QUOTE_EPSTEIN_WIDE = ('with a number** -- stated', 'the count) -- each', 'not proved; open. -/')
QUOTE_SETS = {'quote_rcurve': (QUOTE_NEEDLES, QUOTE_WIDE), 'quote_epstein': (QUOTE_EPSTEIN, QUOTE_EPSTEIN_WIDE)}


def quote(*a):
    """`quote <kernel dir> <base> <tip> <bank stem>`: every line the cut removes or changes (the `-` lines of git diff base..tip, comments
    alone) read, one needle of QUOTE_NEEDLES assigned to each by containment and refused where a removed line carries none or a needle stands
    in no removed line; each needle searched with git grep -n -F at the tip across the kernel's whole tracked tree; every hit printed with its
    quoting line and entered as a residue. data/b691_<stem>.txt (.json)."""
    kd, base, tip, stem = a[0], a[1], a[2], a[3]
    QUOTE_NEEDLES, QUOTE_WIDE = QUOTE_SETS[stem]
    d = g(kd, 'diff', '--unified=0', base, tip)
    removed = [l[1:] for l in d.split(NL) if l.startswith('-') and not l.startswith('---')]
    removed = [l for l in removed if l.strip()]
    rows, unassigned = [], []
    for l in removed:
        nd = [n for n in QUOTE_NEEDLES if n in l]
        if not nd:
            unassigned.append(l)
        rows.append(dict(line=l, needle=nd[0] if nd else None))
    unused = [n for n in QUOTE_NEEDLES if not any(n in r['line'] for r in rows)]
    if unassigned or unused:
        sys.exit('### A REMOVED LINE WITHOUT A NEEDLE %s OR A NEEDLE IN NO REMOVED LINE %s -- NOTHING WRITTEN' % (unassigned, unused))
    for r in rows:
        w = [n for n in QUOTE_WIDE if n.lower() in r['line'].lower()]
        r['wide'] = w[0] if w else None
    wu = [n for n in QUOTE_WIDE if not any(n.lower() in r['line'].lower() for r in rows)]
    if any(r['wide'] is None for r in rows) or wu:
        sys.exit('### THE SECOND SHAPE: A REMOVED LINE WITHOUT A NEEDLE OR A NEEDLE IN NO REMOVED LINE %s -- NOTHING WRITTEN' % wu)
    hits = []
    for r in rows:
        out = g(kd, 'grep', '-n', '-F', r['needle'], tip, '--')
        r['hits'] = [x for x in out.split(NL) if x.strip()]
        out2 = g(kd, 'grep', '-n', '-i', '-F', r['wide'], tip, '--')
        r['hits_wide'] = [x for x in out2.split(NL) if x.strip()]
        hits += [(r['wide'], h) for h in r['hits_wide']]
    L = ['b691 -- THE QUOTATION SEARCH BEFORE THE MERGE, data/b690_rules.txt row (2), OVER %s (%s)' % (os.path.basename(kd), utc()), '',
         '### the cut: git diff %s..%s ; the lines it removes or changes %d ; one needle each, checked to stand in its own removed line; each searched' % (
             base, tip, len(rows)),
         '### with git grep -n -F at the tip %s across the kernel`s whole tracked tree. Rows are removed lines: needle | hits (file:line: the quoting' % tip,
         '### line):']
    for r in rows:
        L.append('  %-44s | %d hit(s) ; case-blind %-26r %d hit(s) | removed: %s' % (r['needle'], len(r['hits']), r['wide'], len(r['hits_wide']),
                                                                               r['line'].strip()[:100]))
        L += ['      %s' % h for h in r['hits_wide']]
    q = sorted(set(h.split(':', 2)[1] + ':' + h.split(':', 3)[2] for _n, h in hits))
    # ### the positive control (an ABSENT carries a control): each needle, both shapes, at the base, where its removed line still stands
    ctl = [(r['needle'], len([x for x in g(kd, 'grep', '-n', '-F', r['needle'], base, '--').split(NL) if x.strip()]),
            len([x for x in g(kd, 'grep', '-n', '-i', '-F', r['wide'], base, '--').split(NL) if x.strip()])) for r in rows]
    L += ['', '### THE CONTROL: each needle at the base %s, where the removed line stands (needle ; case-exact hits ; case-blind hits):' % base]
    L += ['  %-44s ; %d ; %d' % c for c in ctl]
    L += ['### the control %s' % ('FIRES FOR EVERY NEEDLE IN BOTH SHAPES' if all(c[1] and c[2] for c in ctl) else '### DOES NOT FIRE FOR EVERY NEEDLE')]
    L += ['', '### THE QUOTING LINES, DISTINCT (file:line): %s' % (', '.join(q) or 'NONE'),
          '### the yields: the case-exact shape %d hit(s) on %d line(s) ; the case-blind shape %d hit(s) on %d line(s)' % (
              sum(len(r['hits']) for r in rows), len(set(h.split(':', 3)[1] + ':' + h.split(':', 3)[2] for r in rows for h in r['hits'])),
              len(hits), len(q)),
          '', '### ### **REMOVED OR CHANGED LINES %d ; NEEDLES SEARCHED %d IN TWO SHAPES ; QUOTING LINES %d -- EACH ENTERED AS A RESIDUE.**' % (
              len(rows), len(rows), len(q))]
    put_txt('b691_%s.txt' % stem, L)
    put_json('b691_%s.json' % stem, dict(at=utc(), kernel=kd, base=base, tip=tip, rows=rows, hits=[list(h) for h in hits]))
    print(NL.join(L))


# ================================================================================ COMPONENT 2: THE CUT BANK, (R301)(2) AND (7)
CUT = dict(kernel='SIDE-rcurve', table='b647_table_SIDE-rcurve.txt', base='d5f33b4', main='54c9040', tip='e3df866', tag='v0.1.1', prior='v0.1.0',
           workflow='bb14e89', targets='29885e5', before=39304553046, after=39305244594, licensed_line=113)


def _norm(t):
    return ' '.join(t.replace('--', ' ').replace('—', ' ').split())


def cut(*a):
    """data/b691_cut.txt (.json): the document named by the tie (data/b691_tie.txt); the commits on its main (the workflow and the print list
    alone, the cut on recut-rcurve-b691, the merge, the tag); the before and after runs and the prints; the distance before and after by the
    b670 method -- each non-MATCHES row of its b647 table read whole, its ACTION's text (the words after `RE-CUT:`) searched, whitespace
    normalized, in the file at the merge; the quotation search's quoting lines each entered as a residue with its line; SIDE-li-map's two
    residues carried (the cut document not its neighbour in the table); the faces header's tag source cited by file and line ((R301)(7))."""
    k = CUT['kernel']
    kd = 'D:/' + k
    tb = rdn(CUT['table'])
    blocks = re.findall(r'(?ms)^  (%s@\w+:(\S+):(\d+)) \| (OVERREACHES|UNDERSTATES|UNLICENSED) \|.*?\n      ACTION   RE-CUT: (.*?)$' % re.escape(k), tb)
    rows = []
    for rid, f, ln, verdict, action in blocks:
        src = _show(kd, CUT['main'], f) or ''
        ok = _norm(action) in _norm(src)
        rows.append(dict(row=rid, file=f, line=int(ln), verdict=verdict, action=action.strip(), applied=ok))
    before = len(rows)
    after = sum(1 for r in rows if not r['applied'])
    q = jl('b691_quote_rcurve.json')
    qlines = sorted(set((h.split(':')[1], int(h.split(':')[2]), h.split(':', 3)[3]) for _n, h in q.get('hits') or []), key=lambda x: (x[0], x[1]))
    lt = rdn('b670_licensed_table.txt').split(NL)
    nb = [lt[CUT['licensed_line'] - 2].strip()[:60], lt[CUT['licensed_line']].strip()[:60]]
    li_nb = any('SIDE-li-map' in x for x in nb)
    nodes = rdn(os.path.basename(K.NODES)).split(NL)
    pin_ln = [i + 1 for i, l in enumerate(nodes) if l.startswith('# pin: ')]
    cpl = rd(os.path.join(T, 'chain_page.py')).split(NL)
    L = ['b691 -- COMPONENT 2, (R301)(2) AND (7): THE RE-CUT OF %s, ITS DISTANCE, ITS RESIDUES (%s)' % (k, utc()), '',
         '### the document: %s, named by b674`s row (2) (relay data/b691_tie.txt: the counts of any kind equal at 2, the larger table 7 rows)' % k,
         '### the commits on its main: the workflow %s alone, the print list %s alone (the Mathlib form, carried from SIDE-trivium`s dd587f9); the cut %s'
         % (CUT['workflow'], CUT['targets'], CUT['tip']),
         '### on recut-rcurve-b691 (comments only: the module header and the T1 block, the two ACTIONs verbatim); the merge %s by --no-ff, the merged' % CUT['main'],
         '### tree the built tree; the tag %s peeled to the merge, its message naming the prior tag %s = %s (relay data/b691_rcurve_merge_push_out.txt)' % (
             CUT['tag'], CUT['prior'], CUT['base']),
         '### the runs: before %d at main 29885e5, after %d at the tip %s, both DERIVES 8 of 8 at the standard three; the prints equal line for line'
         % (CUT['before'], CUT['after'], CUT['tip']),
         '### (relay data/b691_runner_SIDE-rcurve_before.txt, _after.txt, data/b691_prints_SIDE-rcurve.txt)', '',
         '### THE DISTANCE BY THE b670 METHOD: each non-MATCHES row of relay data/%s, its ACTION`s text searched in the file at %s:' % (CUT['table'], CUT['main'])]
    L += ['  %s | %s | ACTION applied %s | %s' % (r['row'], r['verdict'], r['applied'], r['action'][:100]) for r in rows]
    L += ['', '### THE RESIDUES (data/b690_rules.txt row (2); relay data/b691_quote_rcurve.txt, two shapes): each quoting line, the line verbatim:']
    L += ['  R-%d  %s :%d | CARRIED -- a README line, outside the docstring rows the cut reaches; trigger: the next re-cut of %s or a README pass '
          '| %s' % (i, f, ln, k, t[:180]) for i, (f, ln, t) in enumerate(qlines, 1)]
    L += ['', '### SIDE-li-map`s two residues (relay data/b688_cut.txt :60, :64): the cut document`s neighbours in relay data/b670_licensed_table.txt are '
          ':%d %s and :%d %s -- SIDE-li-map (:111) %s; CARRIED, their triggers as data/b690_r3_residues.txt names them.' % (
              CUT['licensed_line'] - 1, nb[0].split(' docstrings')[0], CUT['licensed_line'] + 1, nb[1].split(' docstrings')[0],
              'is a neighbour' if li_nb else 'is not among them'),
          '', '### THE SIDE-kernel ROW`S RESIDUE (the author`s word on the (R301)(3) prompt): PATHS_TO_THE_CRITICAL_LINE_v0_7.md :301, held by the',
          '### repaired generator as CARRIED AT: VERSION DIFFERS (relay data/b691_correspondence_run.txt): the page`s clause "SIDE-kernel v1.8 = 70aba3c',
          '### (carried at lv-conservation v0.7.0)" -- v1.8 peels to %s; the carry the carrier cites, SIDE-lv-conservation v0.7.0' % g('D:/SIDE-kernel', 'rev-parse', 'v1.8^{commit}').strip()[:12],
          '### SIDELvConservation/RegisterPentagon.lean :29, :33, :86, :110, :124, :230 "SIDE-kernel v1.3 = 0bc21c0" -- v1.3 peels to %s.' % g('D:/SIDE-kernel', 'rev-parse', 'v1.3^{commit}').strip()[:12],
          '###   R-K1  PATHS_TO_THE_CRITICAL_LINE_v0_7.md :301 | CARRIED -- the page`s v1.8 against the carry v1.3 = 0bc21c0; no cell by hand; trigger: the',
          '###         next re-cut act after b691 or W-ORD-CORRESPONDENCE-BEHIND-SCOPE',
          '', '### THE FACES HEADER`S TAG ((R301)(7)), carried to the next regeneration, no page write: the page`s :3 prints "SIDE-explicit-formula v0.26 =',
          '### `82550e4`"; its source by file and line -- the node list`s pin line relay %s :%s "%s"; tools/chain_page.py :87-:96 `node_pin` (%s),' % (
              K.NODES, ','.join(str(x) for x in pin_ln), nodes[pin_ln[0] - 1] if pin_ln else '### NONE', cpl[86].strip()),
          '### :894-:899 in `build` (%s), :795-:801 the head (%s).' % (cpl[893].strip()[:60], cpl[797].strip()[:70]),
          '', '### ### **%s RE-CUT: THE DISTANCE BEFORE %d, AFTER %d ; TAG %s ; PRINTS EQUAL ; QUOTING LINES %d, EACH A RESIDUE CARRIED ; SIDE-li-map`S '
          'TWO CARRIED.**' % (k, before, after, CUT['tag'], len(qlines))]
    put_txt('b691_cut.txt', L)
    put_json('b691_cut.json', dict(at=utc(), kernel=k, rows=rows, before=before, after=after, residues=[list(x) for x in qlines], li_neighbour=li_nb,
                                   pin_lines=pin_ln, main=CUT['main'], tip=CUT['tip'], tag=CUT['tag'], run_before=CUT['before'],
                                   run_after=CUT['after']))
    print(NL.join(L))


R3_ROW = re.compile(r'^    :(\d+)\s+BEHIND\s+(BEHIND IN CARRIED PROSE \(THE KERNEL CELL`S TRAILING TEXT\)) (\S.*)$|^    :(\d+)\s+BEHIND\s+(\S.+?)\s{2,}(\S.*)$')
R3_DOC = re.compile(r'^=== (\S+)\s+(\S+) :(\d+)-:(\d+) \(span to :(\d+)\) (.+?) ; rows with a commit (\d+) ; (.*)$')
WITHHELD_DOCS = ('TECHNE_TOOLKIT',)
BEHIND_AT = '77bef05'          # ### PLACE-papers before the generator's run (the C1 landing commit; the two pages written after it, uncommitted)


def _r3_rows():
    """Reading 3's BEHIND rows as banked (relay data/b690_r3_corr.txt, b672_record.after's re-read): [(doc, line or None, cause, pins)], a
    withheld document's rows by count (line None)."""
    rows, doc, out = [], None, rdn('b690_r3_corr.txt').split(NL)
    a = out.index('### THE ROWS WITH A COMMIT (document :line ; reading ; cause ; each commit, its kernel, its reading, its tag); a withheld document`s rows by count')
    for l in out[a + 1:]:
        if l.startswith('### THE ROWS BY READING AND CAUSE'):
            break
        m = R3_DOC.match(l)
        if m:
            doc = m.group(1)
            if doc in WITHHELD_DOCS:
                n = int((re.search(r"'BEHIND': (\d+)", m.group(8)) or [0, 0])[1])
                rows += [(doc, None, 'NOT IN SHAPE', 'WITHHELD: BY COUNT')] * n
            continue
        m = R3_ROW.match(l)
        if m:
            ln, why, pins = (m.group(1), m.group(2), m.group(3)) if m.group(1) else (m.group(4), m.group(5), m.group(6))
            rows.append((doc, int(ln), why.strip(), pins.strip()))
    return rows


def behind(*a):
    """data/b691_behind.txt (.json), (R301)(3): reading 3's 57 BEHIND rows (relay data/b690_r3_corr.txt) each with the generator's reading
    beside -- the repaired generator's dry over the roster (tools/correspondence_gen.py regen_bytes, its dry ctx: local tags, the print and
    grade banks, nothing written), and the generator bank reading 3's cause column read (relay data/b672_correspondence_diff.json,
    tools/b672_record.py :492, :508, :537); what each tool counts against, by line of each tool; the cause."""
    sys.path.insert(0, T)
    import correspondence_gen as CG
    import b672_record as B
    r3 = _r3_rows()
    # ### the author's word (the (R301)(3) answer): the withheld rows named by line with the reason withheld -- re-read now by b672_record.after's
    # ### own resolution (:514-:531, its helpers _has, _ltag, _anc imported), the lines and readings printed, the cells' text not (withheld)
    wl = {}
    ro0 = dict((t['doc'], t) for t in jl('b672_roster_read.json')['tables'])
    b670 = dict((t['doc'], t) for t in jl('b670_correspondence.json')['tables'])
    for wd in WITHHELD_DOCS:
        t = ro0[wd]
        L0 = (_show(PP, BEHIND_AT, t['path']) or '').split(NL)
        ft = CG.find_table(L0, t)
        j, e = ft
        end = b670[wd]['end'] if wd in b670 and b670[wd].get('end') else e
        for i in range(j + 1, max(end, e)):
            pins = B.HEX7.findall(L0[i]) if L0[i].lstrip().startswith('|') else []
            sts = []
            for q in pins:
                hit = [k for k in t['kernels'] if B._has(k, q)] or [k for k in B.ALLK if k not in t['kernels'] and B._has(k, q)]
                if not hit:
                    sts.append('UNRESOLVED')
                    continue
                tc = B._ltag(hit[0])[1]
                sts.append('NO TAG' if not tc else ('AT THE TAG' if B._anc('D:/' + hit[0], tc, q) else ('BEHIND' if B._anc('D:/' + hit[0], q, tc) else 'OFF')))
            if 'BEHIND' in sts:
                wl.setdefault(wd, []).append(i + 1)
    for wd, lns in wl.items():
        k = 0
        for n, x in enumerate(r3):
            if x[0] == wd and x[1] is None and k < len(lns):
                r3[n] = (wd, lns[k], x[2], 'WITHHELD: %d commit(s), not printed' % 0)
                k += 1
    ro = json.load(io.open(CG.ROSTER, encoding='utf-8'))
    tags, _tl = CG.read_tags(CG.kernels_of(ro), remote=False)
    banks, _bl = CG.read_banks(tags)
    ctx = dict(tags=tags, banks=banks, grades=CG.read_grades(), present=CG.present)
    stale = dict((t['doc'], t) for t in jl('b672_correspondence_diff.json')['tables'])
    gen = {}
    for t in ro['tables']:
        # ### the pages as they stood before the generator's run (PLACE-papers BEHIND_AT): the reconciliation is the pre-write reading the
        # ### (R301)(3) prompt carried; the post-write figure is printed beside it, not in its place
        b = (_show(PP, BEHIND_AT, t['path']) or '').encode('utf-8') if 'after-write' not in a else open(os.path.join(PP, t['path']), 'rb').read()
        _nb, res = CG.regen_bytes(b, t, ctx, t['doc'])
        gen[t['doc']] = dict(status=res.get('status'), span=res.get('span'), rows=dict((r['line'], r) for r in res['rows']),
                             kernel=set(c['line'] for c in res['changes'] if c['column'] == 'kernel'),
                             held=dict((h['line'], h) for h in res.get('carry_held', [])))
    import collections
    rows, cat = [], collections.Counter()
    for doc, ln, why, pins in r3:
        G = gen.get(doc) or {}
        st = stale.get(doc) or {}
        sr = dict((r['line'], r.get('reading')) for r in st.get('rows', []))
        if doc in WITHHELD_DOCS:
            gr = ('WITHHELD -- THE DOCUMENT IS WITHHELD (b672_record.py :293 WITHHELD; a withheld document`s cells print as sha256 and length, never as '
                  'text, correspondence_gen`s header); THE TABLE %s' % G.get('status')) + ('' if ln else ' ; ### ITS LINE NOT RE-READ')
        elif G.get('status') != 'SHAPED':
            gr = 'NOT A GENERATOR ROW: THE TABLE %s' % G.get('status')
        elif ln not in G['rows']:
            gr = 'NOT A GENERATOR ROW: PAST THE TABLE :%d-:%d' % tuple(G['span'] or (0, 0))
        else:
            r = G['rows'][ln]
            kc = ('KERNEL CELL WRITTEN BY THE DRY (THE LEADING CLAUSE BEHIND ITS TAG)' if ln in G['kernel'] else
                  'KERNEL CELL HELD: CARRIED AT, VERSION DIFFERS' if ln in G['held'] else 'KERNEL CELL NOT WRITTEN')
            gr = '%s ; %s' % (r.get('reading') or 'READ', kc)
        sg = ('-' if ln is None else (sr.get(ln) or ('NOT A ROW OF THE BANK' if st.get('status') == 'SHAPED' else 'TABLE %s' % st.get('status'))))
        claim = ln is not None and ln in G.get('kernel', ())
        rows.append(dict(doc=doc, line=ln, r3_cause=why, pins=pins, generator=gr, stale=sg, claim=claim))
        cat[(why, 'WITHHELD' if doc in WITHHELD_DOCS else (gr.split(' ;')[0].split(':')[0] if not claim else 'GENERATOR`S CLAIM: BEHIND AT THE LEADING CLAUSE'))] += 1
    n_claim = sum(1 for r in rows if r['claim'])
    # ### beside it, the claimed rows read again on the pages as the generator's run left them (the working tree)
    after_claim = 0
    for t in ro['tables']:
        if not any(r['claim'] and r['doc'] == t['doc'] for r in rows):
            continue
        _nb, res2 = CG.regen_bytes(open(os.path.join(PP, t['path']), 'rb').read(), t, ctx, t['doc'])
        k2 = set(c['line'] for c in res2['changes'] if c['column'] == 'kernel')
        after_claim += sum(1 for r in rows if r['claim'] and r['doc'] == t['doc'] and r['line'] in k2)
    L = ['b691 -- COMPONENT 3, (R301)(3): THE GENERATOR`S "BEHIND" AGAINST READING 3`S 57, ROW BY ROW (%s)' % utc(), '',
         '### rows: reading 3`s BEHIND rows as banked (relay data/b690_r3_corr.txt :37-:165, b672_record.after by import, 2026-10-19T15:29:42Z), each with',
         '### the generator`s reading beside: the repaired generator`s dry (tools/correspondence_gen.py at sha256 %s, regen_bytes over the roster'
         % __import__('hashlib').sha256(open(os.path.join(T, 'correspondence_gen.py'), 'rb').read()).hexdigest()[:16],
         '### data/b672_roster_read.json, the tags read locally by read_tags(remote=False) :496-:512, nothing written) and the generator bank reading 3`s',
         '### cause column read (relay data/b672_correspondence_diff.json, %s). A withheld document`s rows by line, their commits not printed.'
         % jl('b672_correspondence_diff.json').get('at'),
         '',
         '### WHAT EACH COUNTS AGAINST, BY LINE OF EACH TOOL:',
         '###   reading 3 (tools/b672_record.py after): every backticked commit in the row, in every cell (:473 HEX7, :514), each resolved in the',
         '###     document`s kernels (:519) and set against that kernel`s local tag on main (:524-:528, `_ltag`); the row BEHIND if any one commit is',
         '###     behind (:530); over b670`s span, past the table proper (:506, :510; :535 HISTORICAL) and over the tables not in the generator`s shape',
         '###     (:533-:534 NOT IN SHAPE); its cause column read from the generator`s bank of 2026-10-16 (:492, :508, :537), not from a fresh reading.',
         '###   the generator (tools/correspondence_gen.py): the kernel cell`s leading clause alone -- its version and commit tokens (parse_kernel_cell',
         '###     :153-:196) -- against the clause`s own kernel`s highest v-tag (read_tags :496, ls-remote on a run, the local clone on a dry), in the',
         '###     shaped tables within the table proper (find_table :138); a row held, absent, untagged or without a declaration is not read for the',
         '###     clause (regen_lines :332-:369); a clause at its tag is left (clause_at_tag :224, the loop :373-:399); a carried clause reads its carry',
         '###     (:379-:397, this act`s repair). Prose and other cells are carried unverified (its own header line, b672).',
         '',
         '### THE ROWS (document :line ; reading 3`s cause ; reading 3`s commits ; the generator, fresh ; the generator`s 2026-10-16 bank, reading 3`s input):']
    for r in rows:
        L.append('    %s %s ; %s ; %s ; %s ; %s' % (r['doc'], ':%d' % r['line'] if r['line'] else '(withheld, line not re-read)', r['r3_cause'],
                                                 r['pins'] if r['doc'] not in WITHHELD_DOCS else 'COMMITS NOT PRINTED (WITHHELD)', r['generator'], r['stale']))
    L += ['', '### THE ROWS BY READING 3`S CAUSE AND THE GENERATOR`S READING:'] + ['    %-58s %-60s %d' % (k[0], k[1], v) for k, v in sorted(cat.items())]
    L += ['', '### THE CAUSE: SCOPE, NOT INPUTS. The two tools count different things against the same kind of reference (a kernel`s tag): reading 3',
          '### every commit anywhere in a row over a wider span, the generator the leading clause in the shaped table proper. The 57 are rows the',
          '### generator does not claim -- carried prose, held, historical, unshaped, absent -- save the rows it writes at the leading clause, %d here,' % n_claim,
          '### which reading 3`s cause column could not see because it read the generator`s 2026-10-16 bank (b672_record.py :492, :508, :537), not a',
          '### fresh reading. The generator compares to the kernels` tags (read_tags :496), not to its inputs; the (R301)(3) repair of the count by a',
          '### tags bank from ls-remote therefore does not apply, and none is taken.',
          '### the pages read at PLACE-papers %s, before the generator`s run (the author`s word, option 1); the claimed rows read again on the pages the' % BEHIND_AT,
          '### run wrote: THE GENERATOR`S CLAIM AFTER THE WRITE %d of %d.' % (after_claim, n_claim),
          '', '### ### **ROWS 57 (READ %d) ; THE GENERATOR`S CLAIM AMONG THEM %d ; NOT A GENERATOR ROW %d ; A GENERATOR ROW NOT CLAIMED %d ; WITHHELD %d ; '
          'THE CAUSE: SCOPE (THE LEADING CLAUSE AGAINST EVERY COMMIT IN THE ROW), AND READING 3`S CAUSE COLUMN READ FROM THE GENERATOR`S 2026-10-16 BANK.**' % (
              len(rows), n_claim, sum(1 for r in rows if r['generator'].startswith('NOT A GENERATOR ROW')),
              sum(1 for r in rows if r['doc'] not in WITHHELD_DOCS and not r['claim'] and not r['generator'].startswith('NOT A GENERATOR ROW')),
              sum(1 for r in rows if r['doc'] in WITHHELD_DOCS))]
    L.insert(L.index('### THE ROWS BY READING 3`S CAUSE AND THE GENERATOR`S READING:') - 1, '')
    L[L.index('### THE ROWS BY READING 3`S CAUSE AND THE GENERATOR`S READING:') - 1:L.index('### THE ROWS BY READING 3`S CAUSE AND THE GENERATOR`S READING:') - 1] = [
        '### THE WITHHELD ROWS (the author`s word): %s -- re-read at HEAD by b672_record.after`s resolution (:514-:531), %d BEHIND against reading 3`s %d; the'
        % ('; '.join('%s :%d' % (r['doc'], r['line']) for r in rows if r['doc'] in WITHHELD_DOCS and r['line']) or 'NONE RE-READ',
           sum(len(v) for v in wl.values()), sum(1 for r in rows if r['doc'] in WITHHELD_DOCS)),
        '### reason withheld: the document is withheld (b672_record.py :293), its cells printed as sha256 and length, never as text; its table is not',
        '### in the generator`s shape, so neither row is a generator row.']
    if len(rows) != 57:
        L.append('### REFUSED: READING 3`S ROWS READ %d, NOT 57' % len(rows))
    print(NL.join(L))
    if 'dry' in a:
        return
    put_txt('b691_behind.txt', L)
    put_json('b691_behind.json', dict(at=utc(), rows=rows, claim=n_claim, causes={'%s | %s' % k: v for k, v in cat.items()}))


# ================================================================================ COMPONENT 4 (5): THE STALE ORDERS TRIAGED, (R301)(5) -- no ledger written
TRIG = re.compile(r'\*\*Trigger:?\*\*:?\s*(.+?)(?:\s*$|(?<=[.”"])\s+(?=\*\*|\*[A-Z]))')


def _order_rows():
    """reading 3's 35 (relay data/b690_r3_orders.json unsteady_names), each with its entry line and act and status read from data/b690_r3_orders.txt."""
    j = jl('b690_r3_orders.json')
    names = j['unsteady_names']
    rows = {}
    for l in rdn('b690_r3_orders.txt').split(NL):
        m = re.match(r'^  (W-ORD-\S+)\s+:(\d+)\s+(b\d+)\s+(\d+)\s+(.+?)\s+:(\d+)\s*$', l)
        if m and m.group(1) in names:
            rows[m.group(1)] = dict(name=m.group(1), line=int(m.group(2)), act=m.group(3), age=int(m.group(4)), status=m.group(5).strip(),
                                    at=int(m.group(6)))
    return [rows[n] for n in names if n in rows], [n for n in names if n not in rows]


def triage_read(*a):
    """The read before any disposition (printed, not banked): each order's entry line at OPEN_TRAILS (its trigger as written, by the
    **Trigger:** clause), and every later line of OPEN_TRAILS and FINDINGS that names it, with the text around the name."""
    rows, miss = _order_rows()
    ot = rd(OT).split(NL)
    fi = rd(FIND).split(NL)
    sel = a[0].split(',') if a else None
    for r in rows:
        if sel and r['name'] not in sel:
            continue
        el = ot[r['line'] - 1]
        hit = [n for n, l in enumerate(ot) if r['name'] in l]
        # ### the entry line: the first line naming the order with its bold definition
        tm = re.search(r'\*\*Trigger:?\*\*:?\s*(.{0,400})', el)
        print('=== %s :%d %s age %d status %r at :%d' % (r['name'], r['line'], r['act'], r['age'], r['status'], r['at']))
        print('    ENTRY :%d (%d chars): %s' % (r['line'], len(el), el[:300]))
        print('    TRIGGER AS WRITTEN: %s' % (tm.group(1) if tm else '### NO **Trigger:** CLAUSE ON THE ENTRY LINE'))
        for n in hit:
            if n + 1 == r['line']:
                continue
            l = ot[n]
            k = l.index(r['name'])
            print('    OT :%d  ...%s...' % (n + 1, l[max(0, k - 120):k + 220].replace(NL, ' ')))
        for n, l in enumerate(fi):
            if r['name'] in l:
                k = l.index(r['name'])
                print('    FI :%d  ...%s...' % (n + 1, l[max(0, k - 120):k + 220]))
    print('### ORDERS %d ; NOT FOUND IN THE BANK %s' % (len(rows), miss or 'NONE'))


# ### the seat's hand-read dispositions (the read: triage_read's print over all 35): name -> (the trigger's file, line, its words as written --
# ### a needle that must stand at that line; can it still fire; why; the disposition; its ground's file, line and a needle that must stand there)
_A = 'the author’s word'
TRIAGE = {
    'W-ORD-LI-WEIL-BRIDGE': ('OT', 4638, 'trigger is **THE AUTHOR’S WORD**', True, 'the trigger is the author`s word, which can be given at any act; '
        'priced in lemmas at b550-b553 (OPEN_TRAILS :11203-:11290) and not attempted since', 'CARRY', 'OT', 11136, 'its trigger stays THE AUTHOR'),
    'W-ORD-WEIL-CONVERSE': ('FI', 4489, 'the kernel lane after this fold; (d) first', False, 'the lane ran: (d) b517, f1 b524, f2 b529, f3 b530, '
        'f4 b533-b534', 'DISCHARGED-BY-READING', 'FI', 4719, 'CLOSED, the seam rh_strip_imp_rh'),
    'W-ORD-XI-P7': ('FI', 4581, 'the next opening of the numerical lane', False, 'the numerical act ran at b526', 'DISCHARGED-BY-READING', 'FI', 4717,
        'CLOSED at b526'),
    'W-ORD-SEAM-UPSTREAM': ('OT', 10974, 'Trigger: the author`s word.', True, 'the author`s word, not given since b537; housekeeping when it fires '
        '(OPEN_TRAILS :11415)', 'CARRY', 'OT', 11428, 'trigger the author'),
    'W-ORD-REGISTER-DEPTH': ('OT', 10984, 'Trigger: the act after b537, unless the author rules otherwise.', False, 'a one-shot trigger, fired: the '
        'act after b537 was b538, which ran the read', 'DISCHARGED-BY-READING', 'OT', 10999, 'W-ORD-REGISTER-DEPTH under (R148)'),
    'W-ORD-DETECTION-REGION': ('OT', 11521, 'Research grade; queued, not an act.', True, 'research grade, re-scoped at b560 on the measured '
        'obstacle (E2), (E3) entered at b590; the queue holds it (the act after b558 named it, FINDINGS :8329 still re-reads it)', 'CARRY',
        'FI', 8329, 'W-ORD-DETECTION-REGION (OPEN_TRAILS :11151, :11512)'),
    'W-ORD-GRH-WEIL': ('OT', 11415, '(c) W-ORD-GRH-WEIL, 31 items', False, 'its place in the queue was taken: closed at b574 on its landing, its '
        'remainders entered beside it each with the author`s word as trigger', 'DISCHARGED-BY-READING', 'OT', 11794, 'CLOSED AT ITS LANDING'),
    'W-ORD-KEIPER-FACE': ('OT', 11704, '**W-ORD-LI-THREE-WAY’s agreement**', True, 'the author placed it in the research order at b660-b661 '
        '(OPEN_TRAILS :14104), after the v0.19 and v0.26 Keiper statements; not acted since', 'CARRY', 'OT', 14104, 'then W-ORD-KEIPER-FACE (:11704)'),
    'W-ORD-SIMPLICITY-FACE': ('OT', 12018, '**Trigger:** the author’s word. **SIMPLICITY_OF_RIEMANN_ZEROS’ edition is HELD', False, 'the word was '
        'given and the face landed at b596 (v0.17); its b631 registry item rides at W-ORD-NYMAN-BEURLING-FACE (:13163)', 'DISCHARGED-BY-READING',
        'OT', 12272, 'has landed at b596'),
    'W-ORD-PNT-CHI': ('OT', 12024, '**Off the critical path. Trigger:** the author’s word.', True, 'the author`s word, not given since b584',
        'CARRY', 'FI', 6620, 'each priced and not started, trigger the author'),
    'W-ORD-CONSTELLATION-RERUN': ('OT', 12096, '**Trigger:** before CP-8, or the author’s word sooner.', False, 'started and landed at b589',
        'DISCHARGED-BY-READING', 'OT', 12128, 'STARTED AND LANDED'),
    'W-ORD-SECOND-READER': ('OT', 12212, 'PRICED, NOT STARTED, trigger the author’s word, its form fixed now', False, 'its named batch (:12542) '
        'ran at b620; the form has since been the house practice (FINDINGS :7701, :7921, :7995)', 'DISCHARGED-BY-READING', 'FI', 7422,
        '## The second reader over the monograph'),
    'W-ORD-QUANTIFIER-COLUMN': ('OT', 12270, 'one line in each page’s head naming the column. **Trigger:** the author’s word.', False,
        'the generator landed at b622 with DENSITY', 'DISCHARGED-BY-READING', 'FI', 7470, 'W-ORD-QUANTIFIER-COLUMN with DENSITY'),
    'W-ORD-VENDOR-FINALMULT': ('OT', 12294, 'Off the critical path. **Trigger:** the author’s word.', True, 'route (b) taken at b628; route (a), '
        'the port, stays priced and not started on the author`s word', 'CARRY', 'OT', 13061, 'route (a), the port, stays priced and not started'),
    'W-ORD-SEC-AXIOM-ARTEFACT': ('OT', 12334, '**Trigger:** the author’s word. **Reason:** a T2 grade', False, 'the artefact landed at b623, '
        'v0.2.2', 'DISCHARGED-BY-READING', 'FI', 7498, 'W-ORD-SEC-AXIOM-ARTEFACT'),
    'W-ORD-E0-INDUCTION': ('OT', 12444, 'W-ORD-E0-INDUCTION, priced, not started, the author’s word its trigger', False, 'the clause landed at b624 '
        'in tools/e0_rule.py with its test', 'DISCHARGED-BY-READING', 'FI', 7516, 'W-ORD-E0-INDUCTION'),
    'W-ORD-TAG-REMOTES': ('OT', 12597, 'W-ORD-TAG-REMOTES, PRICED, NOT STARTED, THE TRIGGER THE AUTHOR’S WORD', False, 'acted at b623: nine '
        'cited tags pushed and read back, three recorded local', 'DISCHARGED-BY-READING', 'FI', 7496, 'H57a HOLDS'),
    'W-ORD-PLATT-RUNG': ('OT', 12891, 'W-ORD-PLATT-RUNG, PRICED, NOT STARTED, THE TRIGGER THE AUTHOR’S WORD', False, 'the rung landed at b626, '
        'v0.22', 'DISCHARGED-BY-READING', 'FI', 7567, 'W-ORD-PLATT-RUNG'),
    'W-ORD-NYMAN-BEURLING-FACE': ('OT', 12893, 'W-ORD-NYMAN-BEURLING-FACE, PRICED, NOT STARTED, THE TRIGGER THE AUTHOR’S WORD', False, 'the face '
        'landed at b629, v0.24; its b630-b631 registry items (:13131, :13161, :13163) ride under it, registry-read, not asserted',
        'DISCHARGED-BY-READING', 'FI', 7639, 'SIDE-explicit-formula v0.24'),
    'W-ORD-DEDEKIND-INSTANCE': ('OT', 12895, 'W-ORD-DEDEKIND-INSTANCE, PRICED, NOT STARTED, THE TRIGGER THE AUTHOR’S WORD', False, 'the instance '
        'landed at b631, v0.25', 'DISCHARGED-BY-READING', 'FI', 7683, 'SIDE-explicit-formula v0.25'),
    'W-ORD-MARGIN-BENCH': ('OT', 12897, 'W-ORD-MARGIN-BENCH, PRICED, NOT STARTED, THE TRIGGER THE AUTHOR’S WORD', False, 'the bench ran at b627',
        'DISCHARGED-BY-READING', 'FI', 7591, 'W-ORD-MARGIN-BENCH'),
    'W-ORD-GATE-FROM-ELABORATOR': ('OT', 13000, '**Trigger:** the author’s word; the finding of relay data/b625_section_vars.txt', False,
        'the elaborated reader ran at b634 over SIDE-explicit-formula and at b637 over both kernels (OPEN_TRAILS :13339)', 'DISCHARGED-BY-READING',
        'FI', 7751, 'W-ORD-GATE-FROM-ELABORATOR'),
    'W-ORD-BINDER-GRAMMAR': ('OT', 13002, '**Trigger:** the author’s word. Not started.', False, 'the grammar landed at b637', 'DISCHARGED-BY-READING',
        'FI', 7833, '## The binder grammar'),
    'W-ORD-ZETA23-SERIAL-BUILD': ('OT', 13065, 'W-ORD-ZETA23-SERIAL-BUILD, PRICED, NOT STARTED, THE TRIGGER THE AUTHOR’S WORD', True, 'the author`s '
        'word, not given since b628; the clone and cache kept at b629 (:13095)', 'CARRY', 'OT', 13095, 'THE CLONE AND THE CACHE, KEPT'),
    'W-ORD-PROBE-HOLD': ('OT', 13119, 'W-ORD-PROBE-HOLD, entered here by the author’s answer to prompt 3, priced and not started, trigger the author’s word',
        False, 'the edit landed at b630 (relay 9b01204d) with its test', 'DISCHARGED-BY-READING', 'RT', 919, 'W-ORD-PROBE-HOLD'),
    'W-ORD-TABLE-RULE-GRADES': ('OT', 13133, 'W-ORD-TABLE-RULE-GRADES, PRICED, NOT STARTED, THE TRIGGER THE AUTHOR’S WORD', False, 'the rule`s grades '
        'applied at b633 with the second reader, the table committed (FINDINGS :7701)', 'DISCHARGED-BY-READING', 'FI', 7705, 'W-ORD-TABLE-RULE-GRADES'),
    'W-ORD-DAY1-PATCH-VERSIONS': ('OT', 13397, 'W-ORD-DAY1-PATCH-VERSIONS, PRICED, NOT STARTED, TRIGGER THE AUTHOR’S WORD', False, 'the seven companions '
        'labelled under (R254)(7)', 'DISCHARGED-BY-READING', 'FI', 8039, 'the seven companions labelled'),
    'W-ORD-STATEMENT-PIN': ('OT', 13487, 'TRIGGER THE NEXT NEW LOAD-BEARING DECLARATION, ACTED ON THE AUTHOR’S WORD', True, 'its first clause met '
        'at every kernel act since b641 that added a load-bearing declaration (v0.27, v0.28, v0.29, v0.32-v0.34 among them) and not acted, its '
        'second clause the author`s word, not given', 'CARRY', 'FI', 7951, 'W-ORD-STATEMENT-PIN priced at two acts'),
    'W-ORD-PLATEAURAMP-DOCSTRING': ('OT', 13491, 'TRIGGER THE FIRST UNDERSTATES ROW OF THE REVIEW PASS', False, 'acted at b642, v0.26',
        'DISCHARGED-BY-READING', 'FI', 7973, 'W-ORD-PLATEAURAMP-DOCSTRING acted'),
    'W-ORD-EPSTEIN-ZQ': ('OT', 13493, 'TRIGGER A RULING TO BUILD IT', False, 'the ruling came at b663 and the instance was built at Q0 on named '
        'premises, v0.29; the count field passed to W-ORD-EPSTEIN-COUNT and W-ORD-EPSTEIN-COUNT-LEAN', 'DISCHARGED-BY-READING', 'FI', 8537,
        'The Epstein instance at Q0 on four named premises'),
    'W-ORD-DEDEKIND-RHS-RESTATE': ('OT', 13495, 'TRIGGER THE PROVING ACT', False, 'the proving act was b642: the premise restated with a witness, '
        'dedekind_rhs re-proved, v0.26', 'DISCHARGED-BY-READING', 'FI', 7965, 'dedekind_rhs re-proved'),
    'W-ORD-LABEL-READER': ('OT', 13605, 'TRIGGER THE NEXT EDITION ACT', True, 'no act since b644 is recorded acting it by name (no later line of '
        'OPEN_TRAILS or FINDINGS names it); the next edition act can', 'CARRY', 'FI', 8059, 'W-ORD-LABEL-READER entered'),
    'W-ORD-SEAM-ROW': ('OT', 13846, 'Trigger: grown, by this act’s reading.', False, 'acted at b651', 'DISCHARGED-BY-READING', 'FI', 8233,
        'W-ORD-SEAM-ROW acted'),
    'W-ORD-STATUS-CELLS': ('OT', 14356, '**Trigger:** the next re-cut act’s step zero.', True, 'by its words it fired at the step zero of every '
        're-cut act since b670, this act among them, and was not acted (reading 3 counts 75 orders without a status word, relay '
        'data/b690_r3_orders.json); it can fire at the next re-cut act`s step zero', 'CARRY', 'FI', 8747, 'W-ORD-STATUS-CELLS entered (:14350)'),
    'W-ORD-BESSEL-BOUND-TIGHTEN': ('OT', 14394, '**Trigger:** the next act that counts on Q0 after b671.', True, 'by its words it fired at the '
        'acts after b671 that counted on Q0 and is not recorded acted (no later line of OPEN_TRAILS or FINDINGS names it); the next count act on '
        'Q0 (W-ORD-EPSTEIN-COUNT-LEAN) can take it', 'CARRY', 'FI', 8767, 'W-ORD-BESSEL-BOUND-TIGHTEN'),
}


def triage(*a):
    """data/b691_orders_triage.txt (.json), (R301)(5): reading 3's 35 open orders older than ten acts without a trigger met or a re-dating, each
    with its OPEN_TRAILS line and entering act (reading 3's bank), its trigger as written (a needle standing at the cited line), whether it can
    still fire and why, and its disposition with its ground (a needle standing at the cited line); each row through read_triage_row. No ledger
    is written; the bank is raised at b692."""
    rows, miss = _order_rows()
    src = {'OT': rd(OT).split(NL), 'FI': rd(FIND).split(NL), 'RT': rd(os.path.join(T, 'chain_page.py')).split(NL)}
    name_of = {'OT': 'PLACE-papers OPEN_TRAILS.md', 'FI': 'PLACE-papers FINDINGS.md', 'RT': 'relay tools/chain_page.py'}
    bad, out = [], []
    for r in rows:
        t = TRIAGE.get(r['name'])
        if t is None:
            bad.append('%s: NO DISPOSITION' % r['name'])
            continue
        tf, tl, tn, cf, why, dsp, gf, gl, gn = t
        if tn not in src[tf][tl - 1]:
            bad.append('%s: THE TRIGGER %r NOT AT %s :%d' % (r['name'], tn, tf, tl))
        if gn not in src[gf][gl - 1]:
            bad.append('%s: THE GROUND %r NOT AT %s :%d' % (r['name'], gn, gf, gl))
        row = dict(name=r['name'], line=r['line'], act=r['act'], age=r['age'], status=r['status'], trigger=tn,
                   trigger_at='%s :%d' % (name_of[tf], tl), can_fire=cf, why=why, disposition=dsp, ground='%s :%d ("%s")' % (name_of[gf], gl, gn))
        read_triage_row(row)
        out.append(row)
    extra = [n for n in TRIAGE if n not in [r['name'] for r in rows]]
    if bad or miss or extra:
        sys.exit('### REFUSED -- NOTHING WRITTEN:\n  ' + '\n  '.join(bad + ['NOT IN READING 3`S BANK: %s' % miss] * bool(miss) +
                                                                  ['A DISPOSITION FOR NO ORDER: %s' % extra] * bool(extra)))
    import collections
    cnt = collections.Counter(r['disposition'] for r in out)
    L = ['b691 -- COMPONENT 4 (5), (R301)(5): THE STALE ORDERS TRIAGED (%s)' % utc(), '',
         '### the orders: reading 3`s 35 (relay data/b690_r3_orders.json unsteady_names; b670`s steadiness predicate, tools/b670_record.py :926, the age',
         '### from 690: open, older than ten acts, the status neither a trigger met nor a re-dating). Each row: the order and its OPEN_TRAILS line, the',
         '### entering act and its status as reading 3 read them; the trigger as written (its words standing at the cited line, checked by this tool);',
         '### whether it can still fire and why; the disposition -- CARRY, DISCHARGED-BY-READING (the reading cited by path and line, its words',
         '### checked there) or RETIRE (its reason). The dispositions are the seat`s hand-read of every line naming each order in OPEN_TRAILS and',
         '### FINDINGS (tools/b691_record.py triage_read). No ledger written; raised at b692.', '']
    for r in out:
        L += ['  %-30s OPEN_TRAILS :%-6d %-5s age %-3d status %r' % (r['name'], r['line'], r['act'], r['age'], r['status']),
              '      TRIGGER (%s): %s' % (r['trigger_at'], r['trigger']),
              '      CAN STILL FIRE: %s -- %s' % ('YES' if r['can_fire'] else 'NO', r['why']),
              '      DISPOSITION: %s -- %s' % (r['disposition'], r['ground'])]
    L += ['', '### ### **ORDERS %d ; CARRY %d ; DISCHARGED-BY-READING %d ; RETIRE %d ; EVERY TRIGGER AND GROUND STANDING AT ITS LINE ; NO LEDGER '
          'WRITTEN.**' % (len(out), cnt['CARRY'], cnt['DISCHARGED-BY-READING'], cnt['RETIRE'])]
    print(NL.join(L[-1:]))
    if 'dry' in a:
        return
    put_txt('b691_orders_triage.txt', L)
    put_json('b691_orders_triage.json', dict(at=utc(), rows=out, counts=dict(cnt)))


# ================================================================================ COMPONENT 3: THE RUN, the author's word on the (R301)(3) prompt (option 1)
GEN_PAGES = (('PATHS', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md'), ('RCURVE', 'phase1.5/rcurve/R_CURVE_CRITERION_v0_2_2.md'))
GEN_STEM = 'b691_correspondence_run'


def gensnap(*a):
    """data/b691_gen_snapshot.txt: the repaired generator's first run against a captured snapshot (tools/repair_snapshot.py, b417): the dry,
    from a sandbox copy of relay's tools with the roster and the grade bank copied beside; every write inside the sandbox CONTAINED, every
    live write in the watch set ESCAPED and restored. A dry: no page write by code; the snapshot shows it."""
    import repair_snapshot as RS
    r = RS.snapshot(os.path.join('tools', 'correspondence_gen.py'), with_data=('data/b672_roster_read.json', 'data/terminal_table.json'), args=['dry'])
    L = ['b691 -- COMPONENT 3: THE REPAIRED GENERATOR AGAINST A SNAPSHOT, BEFORE ITS RUN (%s)' % utc(), ''] + RS.report(r)
    L += ['', '### the sandbox`s dry, its last line: %s' % ((r['stdout'].strip().split(NL) or ['-'])[-1][:200])]
    L += ['### ### **SNAPSHOT: EXIT %d ; ESCAPED %d ; STILL DIFFERING %d.**' % (r['rc'], len(r['escaped']), len(r['still_files']))]
    print(NL.join(L))
    if 'dry' not in a:
        put_txt('b691_gen_snapshot.txt', L)


def genrun(*a):
    """data/b691_gen_live.txt: the generator's run where it lives (tools/repair_snapshot.py live), the pages the dry names written by the
    generator's own write alone, its diff banks under data/b691_correspondence_run.* permitted; every other change in the watch set restored
    or named. One ls-remote per repository, in sequence, inside the generator (read_tags)."""
    import repair_snapshot as RS
    permit = (GEN_STEM + '.txt', GEN_STEM + '.json')
    r = RS.live(os.path.join('tools', 'correspondence_gen.py'), permit=permit, args=['run', 'full', '--diff', GEN_STEM])
    L = ['b691 -- COMPONENT 3: THE GENERATOR`S RUN, LIVE, UNDER THE AUTHOR`S WORD (OPTION 1) (%s)' % utc(), ''] + RS.report(r)
    out = r['stdout'].strip().split(NL)
    L += ['', '### the run`s own lines (its summary, its tags, its write):'] + [l for l in out if l.startswith(('### ### **', '### WRITTEN', '### REFUSED'))
                                                                          or 'ls-remote' in l[:60] or (l.startswith('    SIDE-') and ' ; local ' in l)]
    L += ['### ### **LIVE: EXIT %d ; CHANGES %d ; PERMITTED %d ; RESTORED %d ; NAMED %d ; STILL DIFFERING %d.**' % (
        r['rc'], len(r['changes']), len(r['permitted']), len(r['restored']), len(r['named']), len(r['still_files']))]
    print(NL.join(L))
    print(NL.join(out[-12:]))
    put_txt('b691_gen_live.txt', L)


def rundiff(*a):
    """data/b691_correspondence_run_PATHS.txt and _RCURVE.txt: each page's diff as the generator wrote it (git diff in PLACE-papers, the page
    alone, against its HEAD), the :301 hold printed beside in the PATHS bank, the generator's run diff bank cited."""
    rt = rdn(GEN_STEM + '.txt').split(NL)
    ca = next((n for n, l in enumerate(rt) if l.startswith('### THE CARRIED-AT CLAUSES')), None)
    held_lines = [l.strip() for l in rt[ca + 1:] if l.startswith('    ')][:20] if ca is not None else []
    held_lines = held_lines[:next((n for n, l in enumerate(rt[ca + 1:]) if not l.startswith('    ')), len(held_lines))] if ca is not None else []
    for lab, path in GEN_PAGES:
        d = g(PP, 'diff', '--', path)
        L = ['b691 -- COMPONENT 3: THE GENERATOR`S WRITE TO %s, ITS DIFF (%s)' % (path, utc()), '',
             '### written by tools/correspondence_gen.py run alone (relay data/b691_gen_live.txt), its run bank relay data/%s.txt; the diff `git diff -- %s`' % (GEN_STEM, path),
             '### at PLACE-papers %s, before the page commit; the lines changed:' % g(PP, 'rev-parse', '--short', 'HEAD').strip(), '']
        L += d.rstrip(NL).split(NL) if d.strip() else ['### NO DIFF: THE PAGE AS IT WAS']
        nch = sum(1 for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))
        if lab == 'PATHS':
            L += ['', '### :301 HELD, VERSION DIFFERS (the author`s word): the page`s clause "SIDE-kernel v1.8 = 70aba3c (carried at lv-conservation v0.7.0)"; the',
                  '### carry the carrier cites, SIDE-lv-conservation v0.7.0 RegisterPentagon.lean "SIDE-kernel v1.3 = 0bc21c0"; v1.3 peels to 0bc21c06454a in',
                  '### SIDE-kernel, v1.8 to 70aba3cd7392. Carried as a residue of the SIDE-kernel row (data/b691_cut.txt).',
                  '### the run`s own hold rows (relay data/%s.txt, THE CARRIED-AT CLAUSES): %s' % (GEN_STEM, '; '.join(held_lines) or 'NOT IN THE RUN BANK')]
        L += ['', '### ### **%s: LINES CHANGED %d.**' % (path, nch)]
        print(NL.join(L))
        put_txt('b691_correspondence_run_%s.txt' % lab, L)


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, answers=answers, tie=tie, runner=runner, prints=prints, quote=quote, cut=cut, behind=behind,
              gensnap=gensnap, genrun=genrun, rundiff=rundiff, triage_read=triage_read, triage=triage)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b691_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
