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


def quote(*a):
    """`quote <kernel dir> <base> <tip> <bank stem>`: every line the cut removes or changes (the `-` lines of git diff base..tip, comments
    alone) read, one needle of QUOTE_NEEDLES assigned to each by containment and refused where a removed line carries none or a needle stands
    in no removed line; each needle searched with git grep -n -F at the tip across the kernel's whole tracked tree; every hit printed with its
    quoting line and entered as a residue. data/b691_<stem>.txt (.json)."""
    kd, base, tip, stem = a[0], a[1], a[2], a[3]
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
    r3 = _r3_rows()
    ro = json.load(io.open(CG.ROSTER, encoding='utf-8'))
    tags, _tl = CG.read_tags(CG.kernels_of(ro), remote=False)
    banks, _bl = CG.read_banks(tags)
    ctx = dict(tags=tags, banks=banks, grades=CG.read_grades(), present=CG.present)
    stale = dict((t['doc'], t) for t in jl('b672_correspondence_diff.json')['tables'])
    gen = {}
    for t in ro['tables']:
        b = open(os.path.join(PP, t['path']), 'rb').read()
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
        if ln is None:
            gr = 'WITHHELD: BY COUNT (THE TABLE NOT IN THE GENERATOR`S SHAPE: %s)' % G.get('status')
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
        cat[(why, gr.split(' ;')[0].split(':')[0] if not claim else 'GENERATOR`S CLAIM: BEHIND AT THE LEADING CLAUSE')] += 1
    n_claim = sum(1 for r in rows if r['claim'])
    L = ['b691 -- COMPONENT 3, (R301)(3): THE GENERATOR`S "BEHIND" AGAINST READING 3`S 57, ROW BY ROW (%s)' % utc(), '',
         '### rows: reading 3`s BEHIND rows as banked (relay data/b690_r3_corr.txt :37-:165, b672_record.after by import, 2026-10-19T15:29:42Z), each with',
         '### the generator`s reading beside: the repaired generator`s dry (tools/correspondence_gen.py at sha256 %s, regen_bytes over the roster'
         % __import__('hashlib').sha256(open(os.path.join(T, 'correspondence_gen.py'), 'rb').read()).hexdigest()[:16],
         '### data/b672_roster_read.json, the tags read locally by read_tags(remote=False) :496-:512, nothing written) and the generator bank reading 3`s',
         '### cause column read (relay data/b672_correspondence_diff.json, %s). A withheld document`s rows by count.' % jl('b672_correspondence_diff.json').get('at'),
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
        L.append('    %s %s ; %s ; %s ; %s ; %s' % (r['doc'], ':%d' % r['line'] if r['line'] else '(withheld)', r['r3_cause'],
                                                 r['pins'] if r['doc'] not in WITHHELD_DOCS else 'BY COUNT', r['generator'], r['stale']))
    L += ['', '### THE ROWS BY READING 3`S CAUSE AND THE GENERATOR`S READING:'] + ['    %-58s %-60s %d' % (k[0], k[1], v) for k, v in sorted(cat.items())]
    L += ['', '### THE CAUSE: SCOPE, NOT INPUTS. The two tools count different things against the same kind of reference (a kernel`s tag): reading 3',
          '### every commit anywhere in a row over a wider span, the generator the leading clause in the shaped table proper. The 57 are rows the',
          '### generator does not claim -- carried prose, held, historical, unshaped, absent -- save the rows it writes at the leading clause, %d here,' % n_claim,
          '### which reading 3`s cause column could not see because it read the generator`s 2026-10-16 bank (b672_record.py :492, :508, :537), not a',
          '### fresh reading. The generator compares to the kernels` tags (read_tags :496), not to its inputs; the (R301)(3) repair of the count by a',
          '### tags bank from ls-remote therefore does not apply, and none is taken.',
          '', '### ### **ROWS 57 (READ %d) ; THE GENERATOR`S CLAIM AMONG THEM %d ; NOT A GENERATOR ROW %d ; A GENERATOR ROW NOT CLAIMED %d ; WITHHELD %d ; '
          'THE CAUSE: SCOPE (THE LEADING CLAUSE AGAINST EVERY COMMIT IN THE ROW), AND READING 3`S CAUSE COLUMN READ FROM THE GENERATOR`S 2026-10-16 BANK.**' % (
              len(rows), n_claim, sum(1 for r in rows if r['generator'].startswith('NOT A GENERATOR ROW')),
              sum(1 for r in rows if r['line'] and not r['claim'] and not r['generator'].startswith('NOT A GENERATOR ROW')),
              sum(1 for r in rows if r['line'] is None))]
    if len(rows) != 57:
        L.append('### REFUSED: READING 3`S ROWS READ %d, NOT 57' % len(rows))
    print(NL.join(L))
    if 'dry' in a:
        return
    put_txt('b691_behind.txt', L)
    put_json('b691_behind.json', dict(at=utc(), rows=rows, claim=n_claim, causes={'%s | %s' % k: v for k, v in cat.items()}))


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, answers=answers, tie=tie, runner=runner, prints=prints, quote=quote, cut=cut, behind=behind)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b691_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
