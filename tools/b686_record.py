# -*- coding: utf-8 -*-
"""b686_record.py -- THE ACT'S RECORD TOOL, b686 under (R296).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b686's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b684_record.py (the helpers, the guarded landing, the readers, step zero's rowgen and branches routes,
### the answers route, the naming, the runner, the prints and the cut's diff, each taking its kernel as an argument) and b685_record.py (the
### late routes, added at Component 4 with the carry-time repair of (R296)(2)).
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b686_record.py <route> [dry]`.
"""
import io
import itertools
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
import b686_worklist as K          # noqa: E402

SP = K.SP
STANDIN = 'standin' in sys.argv[2:]          # ### the dry-run step's stand-ins, by argument (environment variables left as they are)


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
    none a number any bank carries; a stand-in run writes no bank. Carried from b684_record.py with b686's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b686_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b686_findings.json': dict(entry_line=99999, title='stand-in'),
        'b686_trail.json': dict(line=99999),
        'b686_act_root.json': dict(root='0' * 64, previous='3f5aa053' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b686's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b686_scanfile_%s.md' % tag)
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
    """a row of data/b686_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


def read_runner_row(r):
    """a row of data/b686_runner_rows.json: the kernel, its label (before or after), the ref (40 hex), the run id and the gate; returns
    (kernel, label, gate)."""
    if not isinstance(r, dict) or not re.match(r'^SIDE-[\w-]+$', r.get('kernel') or '') or r.get('label') not in ('before', 'after') \
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
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b686_rowgen_<stage>.txt."""
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
    L = ['b686 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b686_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R296)(5))
def branches(*a):
    """every branch (R296)(5) names, its tip read before any delete, its fate; any branch under the push-b685 prefix that --merged lists and
    the ruling does not name, reported and KEPT. No remote branch is named this act. data/b686_branches.txt (.json)."""
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
            if x.startswith('push-b685') and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b686 -- STEP ZERO, (R296)(5): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local ; tip ; listed by `git branch --merged main --list <name>` ; fate. Deleted by name in',
         '### the house form, each delete command naming one branch with no glob in any half, one command per message, in sequence; no branch',
         '### the ruling does not name.']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                               r['fate']) for r in rows]
    L += ['', '### branches under the push-b685 prefix that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; TO BE DELETED %d ; UNNAMED UNDER THE PREFIX %d.**' % (
        len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), len(rows), len(extra))]
    put_txt('b686_branches.txt', L)
    put_json('b686_branches.json', dict(at=utc(), rows=rows, extra=[list(x) for x in extra]))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R296)(1)
WH = ('*Appended 2026-10-18 by b686 to b685’s entry (:9228), under `(R296)`(1) -- b685 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b685_closing.txt), P3 STANDING STATED, NOT PROVED:*')
WB = (' “b685 closed: relay ea8e7f49, PLACE-papers d201ac8; suite 108 of 109; root 3f5aa05397b47486…; 3 prompts answered; 6 defects” '
      '(data/b685_closing.txt :1), the closing pushed and read back at relay 5c051335 (data/b685_closing_push_out.txt). HCount at Q0 asks '
      'N(t, t + 1] ≤ 10 log(|t| + 3) over Q0’s zeros in the open strip (−1/2, 3/2); the certified zeros cover −150 ≤ t ≤ 149 with at most 4 '
      'per unit window, the narrowest margin 13.607, the list’s own constant 0.878; the open part t > 149 (data/b685_p3.txt). Ten candidates '
      'read at their sources, each PDF pinned by sha256: five located (Trudgian 2015, Bennett-Martin-O’Bryant-Rechnitzer 2021, '
      'Hasanalizade-Shen-Wong 2021, Grenié-Molteni), each bounding one L-function and not the sum Z_Q; five not located (Lee 2012 and 2018, '
      'Mukhopadhyay et al., Bombieri-Hejhal), giving no explicit count (data/b685_search.txt). Route (ii) derived a = 0.432572 ± 4.33e-41, '
      'b = 0, c = 1.262442 ± 1.26e-40 for T ≥ 149, the window bound 8.31 at t = 150 against 50.30 (data/b685_count.txt); C1 clause (i) PASS '
      'at T = 100, 1000 and 10⁴ and clause (ii) FAIL against Hasanalizade-Shen-Wong Corollary 1.2 at all three, the seat’s reading of their '
      'π/4 banked as the seat’s; the composition not run; P5 run without it -- N_Q(150)’s interval [176.14, 183.00] containing the certified '
      '180, C2’s planted constant moving it to [208.83, 216.29], a shift of 32.985022 as expected (data/b685_count_controls.txt); H1-H3 and '
      'H6 HELD, H4 NOT SCORABLE, H5 REFUTED; P3 kept stated, not proved; `W-ORD-EPSTEIN-COUNT` OPEN at OPEN_TRAILS :14832 with the three '
      'readings as its trigger. Suite 108 of 109 pre-push and post-push, G-RULE-HEAD-LINE-QUOTED declared on the face -- the ruling’s (1) '
      'summarising b684’s head line and not quoting it, the navigator’s (e); N3 NOT SCORABLE, N1, N2, N4, N5 and S1-S3 HELD. Six defects: '
      '(a)-(c) and (e) the navigator’s, (d) the search run before the statement bank, (f) the sealed N4 scorer reading the landed entry '
      'while the entry prints the scores -- repaired at b686’s carry under `(R296)`(2). mirror-refresh-2026-10-18-b685.zip CLEAN with the '
      'root line. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b686_record_lines.json', 'c1', entry=K.B685_ENTRY,
         check=[('FINDINGS.md', K.B685_ENTRY, '## The count law for Z_Q'), ('OPEN_TRAILS.md', K.B685_TRAIL, '### b685')], dry=dry)


# ================================================================================ THE ANSWERS BANK (b684's route, carried)
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
    """data/b686_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
    every word of the author delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim. Tool calls are
    read from the assistant lines alone (b683's trap: the api-request-blob lines carry copies of earlier calls)."""
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
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %s), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b686 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b686_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b686_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 3: THE NAMING, (R296)(4) -- before any kernel write
def _kern_rows():
    """the kernels table's rows (data/b647_table_kernels.txt): rows | MATCHES | UNDERSTATES | OVERREACHES | UNLICENSED (its header :4)."""
    out = []
    for i, l in enumerate(rdn(K.KERNELS_BANK).split(NL), 1):
        m = re.match(r'^  (SIDE-[\w-]+)\s+([0-9a-f]{7}) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|', l)
        if m:
            out.append(dict(line=i, text=l, kernel=m.group(1), pin=m.group(2), rows=int(m.group(3)), under=int(m.group(5)),
                            over=int(m.group(6)), unlic=int(m.group(7))))
    return out


def _cut_figure(t, k):
    """a kernel's figure after its cut, read from its cut bank: b684's bank carries four kernels -- the named one's verdict line 'THE
    DISTANCE BEFORE n, AFTER m' (relay data/b684_cut.txt :44) and the residues' re-read rows '<kernel> before n (<bank>) ; after m' (:78-:79);
    a bank of one kernel, its own verdict line."""
    m = re.search(r'THE DISTANCE BEFORE (\d+), AFTER (\d+)', t)
    if k == 'SIDE-class-number-anomaly' or 'RESIDUES' not in t:
        return int(m.group(2)) if m else None
    sec = re.search(r'%s before (\d+) \([^)]*\) ; after (\d+)' % re.escape(k), t)
    return int(sec.group(2)) if sec else None


def naming(*a):
    """(R296)(4) and N2: the order's line (data/b652_ferry.txt :19), the tie-break rule's row and the table rows printed verbatim from their
    banks; every kernel's standing count read from the licensed table (a kernel cut since its read stands at its cut bank's figure); the
    document named by the descending count and, at a tie, by the rule's letter; then the named kernel's workflow directory, print list and
    print bank read or declared absent -- before any kernel write. data/b686_naming.txt (.json). Carried from b684_record.py's naming."""
    rules = rdn(K.RULES_BANK).split(NL)
    i0 = [i for i, l in enumerate(rules) if l.startswith('  (%d) ' % K.TIE_RULE_ROW)][0]
    rule = [rules[i0]] + [l for l in itertools.takewhile(lambda x: x.startswith('      '), rules[i0 + 1:])]
    order_line = rd(os.path.join(D, 'b652_ferry.txt')).split(NL)[18]
    lt = rdn(K.TABLE_BANK).split(NL)
    standing = {}
    for i, l in enumerate(lt, 1):
        m = re.match(r'^  (SIDE-[\w-]+) docstrings \(read at ([0-9a-f]{7})\)\s+(\d+) ->\s+(\d+)', l)
        if m:
            standing[m.group(1)] = (i, int(m.group(4)), l)
    cut_since = {}
    for k, bank, needle in K.CUT_SINCE:
        t = rd(os.path.join(ROOT, *bank.split('/')))
        f = _cut_figure(t, k) if needle in t else None
        if f is not None:
            cut_since[k] = (f, bank)
    rank = []
    for r in _kern_rows():
        ln, now, _l = standing.get(r['kernel'], (None, None, None))
        if r['kernel'] in cut_since:
            now = cut_since[r['kernel']][0]
        rank.append((now if now is not None else -1, r['under'] + r['over'] + r['unlic'], r['rows'], r['kernel'], ln, r))
    rank.sort(key=lambda x: (-x[0], x[3]))
    top = rank[0][0]
    tied = [x for x in rank if x[0] == top]
    by_rule = sorted(tied, key=lambda x: (-x[1], -x[2], x[3]))
    named = by_rule[0][3] if (len(tied) == 1 or (by_rule[0][1], by_rule[0][2]) != (by_rule[1][1], by_rule[1][2])) else None
    td = 'D:/' + named if named else None
    wf = g(td, 'ls-tree', '--name-only', 'main', '.github/workflows/').split() if td else []
    pt = g(td, 'ls-tree', '--name-only', 'main').split() if td else []
    pfx = re.sub(r'(^|-)(\w)', lambda m: m.group(2).upper(), named) if named else 'X'
    pshape = r"'%s\.[A-Za-z0-9_.']+' (depends on axioms|does not depend on any axioms)" % pfx
    pb = sorted(set(g(ROOT, 'grep', '-lE', pshape, '--', 'data/').split()))
    tags = sorted(g(td, 'tag', '--list').split(), key=lambda x: [int(n) for n in re.findall(r'\d+', x)]) if td else []
    lf = (_show(td, 'main', 'lakefile.lean') or '') + (_show(td, 'main', 'lakefile.toml') or '') if td else ''
    req = re.search(r'(?im)^\s*require\b[^\n]*mathlib', lf) or re.search(r'(?is)\[\[require\]\][^\[]*name\s*=\s*"mathlib"', lf)
    L = ['b686 -- COMPONENT 3, (R296)(4): THE ORDER, THE RULE ROW AND THE TABLE ROWS, VERBATIM, BEFORE THE DOCUMENT IS NAMED (%s)' % utc(), '',
         '### THE ORDER, verbatim (relay data/b652_ferry.txt :19): ' + order_line.strip(),
         '### THE RULE, verbatim with path and line (relay data/%s :%d):' % (K.RULES_BANK, i0 + 1)] + ['    ' + l for l in rule] + [
         '', '### THE TABLE ROWS, verbatim with path and line: the licensed table (relay data/%s) for each kernel of the kernels table (relay' % K.TABLE_BANK,
         '### data/%s, columns rows | MATCHES | UNDERSTATES | OVERREACHES | UNLICENSED, its header :4); a kernel cut since its read stands at' % K.KERNELS_BANK,
         '### its cut bank`s figure (%s); ordered by the count now standing:' % '; '.join('%s at %d, relay %s' % (k, v[0], v[1]) for k, v in cut_since.items())]
    for now, anyk, nrows, k, ln, r in rank:
        L.append('  %2d  %-34s licensed table :%s  "%s"' % (now, k, ln, (standing.get(k) or (0, 0, ''))[2].strip()))
        L.append('      %-34s kernels table :%d  "%s"  (outside of any kind %d ; rows %d)' % ('', r['line'], r['text'].strip(), anyk, nrows))
    L += ['', '### THE NAMING: the greatest count standing is %d, carried by %s%s.' % (
        top, ', '.join(x[3] for x in tied), ' alone, so no tie and the rule of row %d not reached' % K.TIE_RULE_ROW if len(tied) == 1 else '')]
    if len(tied) > 1:
        L.append('### A TIE: neither carries a declared suite failure (b685`s suite 108 of 109, its one failure G-RULE-HEAD-LINE-QUOTED, a rule arm over '
                 'the ruling`s text and no kernel`s, relay data/b685_closing.txt :1); the rule of row %d by its letter -- rows outside LICENSED/CITED of '
                 'any kind: %s; %s' % (K.TIE_RULE_ROW, ', '.join('%s %d (rows %d)' % (x[3], x[1], x[2]) for x in tied),
                                       'EQUAL, so the larger table: %s' % ', '.join('%s %d rows' % (x[3], x[2]) for x in by_rule)
                                       if len(set(x[1] for x in tied)) == 1 else 'the greater count decides'))
    L += ['### NAMED: %s docstrings' % (named or '### NONE'),
          '', '### THE NAMED KERNEL`S WORKFLOW DIRECTORY, PRINT LIST AND PRINT BANK (read before any kernel write):',
          '  %s main %s ; its tags %s, the last %s at %s: .github/workflows/ carries %s -- %s' % (
              named, g(td, 'rev-parse', '--short', 'main').strip(), tags, tags[-1] if tags else '-',
              g(td, 'rev-parse', '--short', (tags[-1] if tags else 'main') + '^{commit}').strip(),
              wf or 'NOTHING', 'a build-module.yml' if any('build-module' in f for f in wf) else 'NO build-module.yml (no dispatch input; no print step)'),
          '  print_targets.txt at its root: %s ; AxiomCheck*.lean at its root: %s' % ('print_targets.txt' in pt, [f for f in pt if f.startswith('AxiomCheck')] or 'NONE'),
          '  relay tracked banks carrying a printed axiom line of a %s declaration (git grep -lE over data/): %s -- %s' % (
              pfx, pb or 'NONE', 'NO PRINT BANK' if not pb else 'a print bank'),
          '  its dependency form: Mathlib by a require clause %s (a lakefile.toml [[require]] block or a lakefile.lean require) ; lean-toolchain %s' % (
              bool(req), (_show(td, 'main', 'lean-toolchain') or '').strip()),
          '', '### ### **NAMED %s ; TIED %d ; WORKFLOW build-module.yml %s ; PRINT LIST %s ; PRINT BANK %s.**' % (
              named or '### NONE', len(tied), 'PRESENT' if any('build-module' in f for f in wf) else 'ABSENT',
              'PRESENT' if 'print_targets.txt' in pt else 'ABSENT', 'PRESENT' if pb else 'ABSENT')]
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('b686_naming.txt', L)
    put_json('b686_naming.json', dict(at=utc(), named=named, tied=[x[3] for x in tied], top=top, workflows=wf, print_banks=pb, tags=tags,
                                      rank=[[x[0], x[1], x[2], x[3], x[4]] for x in rank]))
    print(NL.join(L[-12:]))


# ================================================================================ THE RUNS, THE PRINTS, THE CUT'S DIFF (b684's routes, per kernel)
def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <note...>`: the kernel's run read by its id; the artifact listed, downloaded by its id into
    memory, its sha256 against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP;
    the axioms output of the print step banked whole, every name of the list matched to one printed line. data/b686_runner_<kernel>_<label>.txt,
    data/b686_axioms_<kernel>_<label>.txt and a row of data/b686_runner_rows.json. Carried from b684_record.py's runner."""
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
    L = ['b686 -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (kernel, label.upper(), utc()), '',
         '### the dispatch: %s ; the ref input %s' % (note, ref),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; %s to %s' % (run_id, run.get('url'), run.get('status'), run.get('conclusion'),
                                                                           run.get('createdAt'), run.get('updatedAt'))]
    T_ = {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        L.append('### the artifact: id %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('size_in_bytes'), sha, digest or '### NONE GIVEN', 'AGREE' if digest and digest == sha else '### NOTHING READ FROM IT'))
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
    deps = re.findall(r"^'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)", re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', ax), re.M)
    tg = [l.strip() for l in T_.get('print_targets.txt', '').split(NL) if l.strip()]
    printed = [n for n, _d in deps]
    unmatched = [n for n in tg if n not in printed]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d ; the log`s last lines:' % (row['build_exit'], len(row['errors']))] + \
        ['    ' + l for l in blog.rstrip(NL).split(NL)[-6:]] + [
          '### the print step: the list (out/print_targets.txt) %d names ; terminals printed %d ; every name printed once %s ; axiom-free %d ; '
          'sorryAx %d ; refused %s' % (len(tg), len(deps), not unmatched and len(printed) == len(set(printed)) == len(tg),
                                       sum(1 for _n, d in deps if d.startswith('does not')), sum(1 for _n, d in deps if 'sorryAx' in d),
                                       T_.get('axioms_refused.txt', '').strip() or 'NONE')]
    ok = run.get('conclusion') == 'success' and row['artifact_sha256'] and row['build_exit'] == '0' and not row['errors'] and not row['stopped'] \
        and row['mem_low'] is not None and row['mem_low'] >= K.HOLD and deps and not unmatched and not any('sorryAx' in d for _n, d in deps)
    row['gate'] = 'DERIVES' if ok else 'NOT DERIVES'
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d OF %d ; SORRYAX %d ; GATE %s.**' % (
        run_id, label, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']), len(deps),
        len(tg), sum(1 for _n, d in deps if 'sorryAx' in d), row['gate'])]
    read_runner_row(row)
    put_txt('b686_runner_%s_%s.txt' % (kernel, label), L)
    if row['artifact_sha256']:
        put_txt('b686_axioms_%s_%s.txt' % (kernel, label), ax.split(NL))
    j = jl('b686_runner_rows.json') if os.path.isfile(os.path.join(D, 'b686_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('b686_runner_rows.json', dict(rows=rows))
    print(NL.join(L))


def prints(*a):
    """`prints <kernel> <before bank> <after bank>`: the 'before' and 'after' axioms outputs compared line for line (the merge only where they are
    equal at every line). data/b686_prints_<kernel>.txt."""
    kernel, bb, ab = a[0], a[1], a[2]
    b, f = rdn(bb), rdn(ab)
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bl, fl = b.rstrip(NL).split(NL), f.rstrip(NL).split(NL)
    diff = [(i + 1, x, y) for i, (x, y) in enumerate(zip(bl, fl)) if x != y] + ([('length', len(bl), len(fl))] if len(bl) != len(fl) else [])
    L = ['b686 -- THE PRINTS OF %s BEFORE AND AFTER THE CUT, LINE FOR LINE (%s)' % (kernel, utc()), '',
         '### before: relay data/%s (%d lines) ; after: relay data/%s (%d lines)' % (bb, len(bl), ab, len(fl)), '### the lines that differ:'] + (
             ['    %s : %s | %s' % d for d in diff] or ['    NONE'])
    L += ['', '### ### **PRINTS BEFORE %d LINES ; AFTER %d LINES ; DIFFERING %d ; EQUAL LINE FOR LINE %s.**' % (len(bl), len(fl), len(diff), not diff)]
    put_txt('b686_prints_%s.txt' % kernel, L)
    print(L[-1])


def _strip_comments(t):
    """the Lean text with every block comment (nested /- -/, docstrings and module docs included) and every line comment removed, whitespace
    runs collapsed: what the elaborator reads."""
    out, i, depth = [], 0, 0
    while i < len(t):
        if t.startswith('/-', i):
            depth, i = depth + 1, i + 2
            continue
        if depth and t.startswith('-/', i):
            depth, i = depth - 1, i + 2
            continue
        if not depth and t.startswith('--', i):
            j = t.find(NL, i)
            i = len(t) if j < 0 else j
            continue
        if not depth:
            out.append(t[i])
        i += 1
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


def cutdiff(*a):
    """`cutdiff <kernel> <base> <tip> <branch> <control needle> <file...>`: the cut's diff printed whole; the files it touches; each file's text
    with its comments stripped compared before and after (equal = no line the elaborator reads changed), with a positive control (a one-word
    code change in the after text must make the comparison unequal). data/b686_cut_diff_<kernel>.txt."""
    kernel, base, tip, branch, needle, want = a[0], a[1], a[2], a[3], a[4], list(a[5:])
    td = 'D:/' + kernel
    files = g(td, 'diff', '--name-only', base, tip).split()
    d = g(td, 'diff', '--unified=0', base, tip).replace(chr(13), '')
    rows = []
    for f in files:
        b, n = _show(td, base, f) or '', _show(td, tip, f) or ''
        eq = _strip_comments(b) == _strip_comments(n)
        ctl = _strip_comments(b) == _strip_comments(n.replace(needle, needle + '_', 1))
        rows.append((f, eq, ctl, needle in n))
    plus = [l for l in d.split(NL) if l.startswith('+') and not l.startswith('+++')]
    minus = [l for l in d.split(NL) if l.startswith('-') and not l.startswith('---')]
    L = ['b686 -- THE CUT`S DIFF OF %s, RESTRICTED TO COMMENT AND DOCSTRING LINES (%s)' % (kernel, utc()), '',
         '### %s %s (main) -> %s (the cut, %s); files %s ; lines added %d, removed %d' % (kernel, base, tip, branch, files, len(plus), len(minus)),
         '### rows are files: the text with every comment stripped equal before and after ; the control (a one-word code change in the after',
         '### text, %r) unequal ; the control`s needle present:' % needle]
    L += ['  %-34s CODE EQUAL %s ; CONTROL UNEQUAL %s ; NEEDLE PRESENT %s' % (f, eq, not ctl, nd) for f, eq, ctl, nd in rows]
    L += ['', '### the diff, whole:'] + ['    ' + l for l in d.rstrip(NL).split(NL)]
    ok = files == want and all(eq and not ctl and nd for _f, eq, ctl, nd in rows)
    L += ['', '### ### **FILES %d ; CODE EQUAL WITH COMMENTS STRIPPED %s ; CONTROLS UNEQUAL %s ; COMMENT AND DOCSTRING LINES ALONE %s.**' % (
        len(files), all(r[1] for r in rows), all(not r[2] for r in rows), ok)]
    put_txt('b686_cut_diff_%s.txt' % kernel, L)
    print(L[-1])


# ================================================================================ COMPONENT 2: THE CELLS, (R296)(3) (b682's routes, carried)
DIFF_ROW = re.compile(r'^    (\S+) :(\d+) \| (kernel|profile|status) \| (SIDE-[a-z0-9-]+) \| OLD (.*) \| NEW (.*)$')


def read_diff_row(line):
    """a row of the generator's diff: document, line, column, kernel, the cell before and after; returns (document, line, column, old, new)."""
    m = DIFF_ROW.match(line or '')
    if not m:
        raise ValueError('diff row of another shape: %r' % ((line or '')[:120],))
    return m.group(1), int(m.group(2)), m.group(3), m.group(5), m.group(6)


READERS += ['read_diff_row']


def gendry(*a):
    """tools/correspondence_gen.py `dry full` over the roster the generator reads (data/b672_roster_read.json), nothing written to any roster
    file; its whole print banked as data/b686_correspondence_diff.txt, rows the cells with before and after, the three cells of (R296)(3)
    (FOUNDATIONS :628-:630) printed first, every other changed cell beside them. Carried from b682_record.py's gendry."""
    t0 = time.time()
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'correspondence_gen.py'), 'dry', 'full'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', cwd=ROOT, timeout=560)
    out = (r.stdout or '') + (r.stderr or '')
    full = out.split(NL)
    k = max(i for i, l in enumerate(full) if l.startswith('b672 -- THE CORRESPONDENCE GENERATOR'))
    body = [l for l in full[k:] if l != '### DRY: nothing written']
    rows = [read_diff_row(l) for l in body if DIFF_ROW.match(l)]
    rk = [(l, DIFF_ROW.match(l).group(4)) for l in body if DIFF_ROW.match(l)]
    v = [l for l in body if l.startswith('### ### **TABLES')]
    tm = re.search(r'TABLES (\d+) ; SHAPED (\d+)', v[0]) if v else None
    three = [x for x in rows if x[0] == 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME' and x[1] in K.FOUND_LINES]
    other = [x for x in rows if x not in three]
    kerns = collections.Counter(kk for _l, kk in rk)
    L = ['b686 -- COMPONENT 2, (R296)(3): THE CORRESPONDENCE GENERATOR`S DRY RUN, BANKED AS A CELL DIFF (%s)' % utc(), '',
         '### tools/correspondence_gen.py (unedited since b682, %s) run `dry full` at relay %s over the roster it reads, relay' % (
             g(ROOT, 'log', '-1', '--format=%h', '--', 'tools/correspondence_gen.py').strip(), g(ROOT, 'rev-parse', '--short=8', 'HEAD').strip()),
         '### data/b672_roster_read.json: TABLES %s ; SHAPED %s; the local clones` tags, no remote call; NOTHING WRITTEN to any roster file;' % (
             tm.group(1) if tm else '?', tm.group(2) if tm else '?'),
         '### SIDE-silence-principle at %s, its print bank relay %s (built at 675679c, merged at v0.2.2). Rows are cells with before and after (the' % (
             K.SILENCE_TAG, K.SILENCE_PRINTS),
         '### THE DIFF section below: document :line | column | kernel | OLD | NEW); exit %d ; %d s.' % (r.returncode, int(time.time() - t0)), '',
         '### THE THREE CELLS OF (R296)(3) (FOUNDATIONS :628-:630), from the diff: %d' % len(three)]
    L += ['    :%d %s | OLD %s | NEW %s' % (x[1], x[2], x[3][:90], x[4][:90]) for x in three]
    L += ['', '### EVERY OTHER CELL THE GENERATOR WOULD WRITE (beyond the three the ruling names): %d, by kernel %s' % (len(other), dict(kerns))]
    L += ['    %s :%d %s | OLD %s | NEW %s' % (x[0], x[1], x[2], x[3][:80], x[4][:80]) for x in other] or ['    NONE']
    L += ['', '### THE GENERATOR`S PRINT, WHOLE:'] + body
    L += ['', '### ### **CELLS CHANGED %d ; THE THREE CELLS AT FOUNDATIONS :628-:630 %d ; OTHER CELLS %d ; TABLES %s ; SHAPED %s ; GENERATOR EXIT %d ; '
              'NOTHING WRITTEN TO THE ROSTER.**' % (len(rows), len(three), len(other), tm.group(1) if tm else '?', tm.group(2) if tm else '?', r.returncode)]
    put_txt('%s.txt' % K.DIFF_STEM, L)
    put_json('%s.json' % K.DIFF_STEM, dict(at=utc(), rows=[list(x) for x in rows], three=[list(x) for x in three], other=[list(x) for x in other],
                                          rc=r.returncode))
    print(NL.join(L[8:9 + len(three)] + L[9 + len(three):12 + len(three) + len(other)] + L[-1:]))


def dist(*a):
    """the distance by b670's method (tools/b672_record.py `after`, b670's method over the stable anchors) and by the generator's claim, with
    b670's heading-text reader beside them, each route run by import with its bank writers captured in memory so nothing of b670's or b672's is
    written; printed beside b682's 55 and 0. data/b686_correspondence_<stage>.txt (.json). Carried from b682_record.py's dist."""
    stage = a[0] if a else 'before'
    import b670_record as B
    import b672_record as B2
    s1 = {}
    B.put_txt = lambda name, lines: s1.__setitem__(name, lines)
    B.put_json = lambda name, obj: s1.__setitem__(name, obj)
    B.corr()
    v1 = [l for l in s1['b670_correspondence.txt'] if l.startswith('### ### **')][-1]
    s2 = {}
    B2.put_txt = lambda name, lines: s2.__setitem__(name, lines)
    B2.put_json = lambda name, obj: s2.__setitem__(name, obj)
    B2.after()
    T2 = s2['b672_correspondence_after.txt']
    vv = [l for l in T2 if l.startswith('### ### **')]
    m1 = re.search(r'BEHIND (\d+)', v1)
    m2 = re.search(r'ROWS WITH A COMMIT (\d+) .*? BEHIND (\d+) \(b670', vv[-2]) if len(vv) >= 2 else None
    m3 = re.search(r'AT THE LEADING CLAUSE \(THE GENERATOR`S CLAIM\) (\d+)', vv[-1]) if vv else None
    L = ['b686 -- COMPONENT 2, (R296)(3): THE CORRESPONDENCE DISTANCE %s THE GENERATOR`S WRITE, BY b670`S METHOD AND BY THE GENERATOR`S CLAIM (%s)' % (
        stage.upper(), utc()), '',
         '### the methods as b680 and b682 ran them: b670`s (tools/b670_record.py `corr`) by its heading-text reader; b672`s re-read of b670`s',
         '### method over the stable anchors (tools/b672_record.py `after`), its last two verdicts the distance by b670`s method and at the',
         '### generator`s claim; each run by import, its bank writers captured, nothing of b670`s or b672`s written.',
         '### PLACE-papers HEAD %s.' % g(PP, 'rev-parse', '--short', 'HEAD').strip(), '',
         '### BY b670`S HEADING-TEXT READER: ' + v1,
         '### BY THE STABLE ANCHORS (b672`s re-read): ' + (vv[-2] if len(vv) >= 2 else '### UNREAD'),
         '### THE GENERATOR`S CLAIM: ' + (vv[-1] if vv else '### UNREAD'), '',
         '### ### **%s: BEHIND BY b670`S METHOD %s AGAINST b682`S %d ; AT THE GENERATOR`S CLAIM %s AGAINST b682`S %d ; BY b670`S HEADING-TEXT READER %s.**' % (
             stage.upper(), m2.group(2) if m2 else '### UNREAD', K.B682_DISTANCE[0], m3.group(1) if m3 else '### UNREAD', K.B682_DISTANCE[1],
             m1.group(1) if m1 else '### UNREAD'), '',
         '### THE ANCHORED RE-READ, WHOLE:'] + T2
    put_txt('b686_correspondence_%s.txt' % stage, L)
    put_json('b686_correspondence_%s.json' % stage, dict(at=utc(), behind=int(m2.group(2)) if m2 else None, claim=int(m3.group(1)) if m3 else None,
                                                       heading_reader=int(m1.group(1)) if m1 else None))
    print(L[11])


def partner(*a):
    """the author's word on (R296)(3): the one-copy partner of FOUNDATIONS, whose table differs, is not written; its differing lines entered by
    line in the diff bank (data/b686_correspondence_diff.txt, appended) with both tables' cells, carried under W-ORD-ONE-COPY as a reading,
    nothing moved. Carried from b682_record.py's partner."""
    import correspondence_gen as G
    t = [x for x in json.load(io.open(os.path.join(D, 'b672_roster_read.json'), encoding='utf-8'))['tables'] if x['doc'] == 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME'][0]
    A = rd(os.path.join(PP, t['path'])).split(NL)
    B = rd(os.path.join(PP, t['partner'])).split(NL)
    fa, fb = G.find_table(A, t), G.find_table(B, t)
    ta, tb = A[fa[0]:fa[1]], B[fb[0]:fb[1]]
    rows = []
    for i in range(max(len(ta), len(tb))):
        x = ta[i] if i < len(ta) else None
        y = tb[i] if i < len(tb) else None
        if x != y:
            rows.append((fa[0] + 1 + i if x is not None else None, x, fb[0] + 1 + i if y is not None else None, y))
    p = os.path.join(D, '%s.txt' % K.DIFF_STEM)
    old = open(p, 'rb').read()
    if b'THE ONE-COPY PARTNER NOT WRITTEN' in old:
        sys.exit('### THE PARTNER ROWS ARE IN THE DIFF BANK ALREADY -- NOTHING WRITTEN')
    L = ['', '### APPENDED %s by the record tool `partner` (the author`s word on (R296)(3)): THE ONE-COPY PARTNER NOT WRITTEN -- %s' % (
        utc(), t['partner']),
         '### its table (:%d-:%d) against the roster`s file %s (:%d-:%d), at PLACE-papers HEAD %s after the write; rows are table lines that differ,' % (
             fb[0] + 1, fb[1], t['path'], fa[0] + 1, fa[1], g(PP, 'rev-parse', '--short', 'HEAD').strip()),
         '### each with both tables` cells by line; carried under W-ORD-ONE-COPY as a reading, nothing moved:']
    for la, x, lb, y in rows:
        L += ['    ROSTER :%s | %s' % (la, x), '    PARTNER :%s | %s' % (lb, y)]
    L += ['### ### **PARTNER TABLE LINES DIFFERING %d ; WRITTEN 0 ; CARRIED UNDER W-ORD-ONE-COPY.**' % len(rows)]
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN')
    new = old + (NL.join(L) + NL).encode('utf-8')
    open(p + '.tmp', 'wb').write(new)
    os.replace(p + '.tmp', p)
    print(L[-1])


def cells(*a):
    """N3's second clause: the roster commit (the one PLACE-papers commit since the act's start touching the roster file) read line by line --
    every changed line one the generator's run bank (data/b686_correspondence_run.txt) lists, its new text carrying the generator's NEW cell,
    no other file in the commit. data/b686_cells.txt (.json)."""
    shas = g(PP, 'log', '--format=%H', '%s..HEAD' % K.PRE_PP, '--', K.FOUND).split()
    if len(shas) != 1:
        sys.exit('### THE ROSTER FILE CARRIES %d COMMITS SINCE THE ACT`S START, NOT ONE -- NOTHING WRITTEN' % len(shas))
    sha = shas[0]
    files = g(PP, 'show', '--name-only', '--format=', sha).split()
    d = g(PP, 'show', '--unified=0', '--format=', sha, '--', K.FOUND).replace(chr(13), '')
    adds = []
    for h in re.finditer(r'^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@', d, re.M):
        start, n = int(h.group(1)), int(h.group(2) or 1)
        adds += list(range(start, start + n))
    newl = rd(os.path.join(PP, *K.FOUND.split('/'))).split(NL)
    gen = [read_diff_row(l) for l in rdn('b686_correspondence_run.txt').split(NL) if DIFF_ROW.match(l)]
    gl = dict((x[1], x) for x in gen if x[0] == 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME')
    by_hand = [n for n in adds if n not in gl or gl[n][4] not in newl[n - 1]]
    L = ['b686 -- COMPONENT 2, (R296)(3): THE ROSTER COMMIT READ AGAINST THE GENERATOR`S RUN BANK, LINE BY LINE (%s)' % utc(), '',
         '### the commit: PLACE-papers %s (%s) ; files %s' % (sha[:7], g(PP, 'log', '-1', '--format=%s', sha).strip()[:120], files),
         '### the generator`s run bank: relay data/b686_correspondence_run.txt, %d diff rows, %d at the roster file' % (len(gen), len(gl)),
         '### rows are changed lines: line | listed by the generator | its NEW cell in the line:']
    L += ['  :%d | %s | %s' % (n, n in gl, (n in gl and gl[n][4] in newl[n - 1])) for n in adds]
    L += ['', '### ### **CHANGED LINES %d ; WRITTEN BY THE GENERATOR %d ; BY HAND %d ; FILES IN THE COMMIT %d.**' % (
        len(adds), len(adds) - len(by_hand), len(by_hand), len(files))]
    put_txt('b686_cells.txt', L)
    put_json('b686_cells.json', dict(at=utc(), commit=sha, files=files, changed=adds, by_hand=by_hand, generator_rows=len(gl)))
    print(L[-1])


# ================================================================================ THE LATE ROUTES (b685's, carried; every row read through READERS)
import collections                 # noqa: E402
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
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
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


MOVE_OR_DELETE = re.compile(r'\bgit\s+(-C\s+\S+\s+)?(mv|rm)\b|\bgit\s+(-C\s+\S+\s+)?branch\s+-[dD]\b|--delete\b|(^|[;&|]\s*|\s)rm\s+-|Remove'
                            + r'-Item|\bos\.remove\b')


def delete_shape(cmd):
    """(R296)(5): a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    return names, [ch for ch in '*?[' if ch in c]


IDENT = ('psinary', 'hotmail', 'seale', 'york', 'orcid', '0009-0008')


def outbound():
    """the act's outbound requests other than git: every WebSearch query and every subagent prompt from the ruling's line on, read from the
    assistant lines of the session transcript, with the author's identifiers searched in each."""
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
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    mv = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'(^|&&\s*|;\s*)gh workflow run\b', QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'Start-Process|\bnohup\b|run_in_background', r['cmd'])]
    seds = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'(^|[;&|(]\s*|\s)sed\s', QUOTED.sub('""', r['cmd']))]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    ob = outbound()
    L = ['b686 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (%d):' % len(disp)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN (%d):' % len(detach)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING sed IN ANY FORM (data/b685_rules.txt row (2)) (%d):' % len(seds)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in seds] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R296)(5): one branch per command, no glob in any half): ' + '; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes)]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git (web searches, subagent prompts and fetches), each with the author`s identifiers found in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; '
              'MOVE OR DELETE COMMANDS %d ; BRANCH DELETES OF ONE BRANCH AND NO GLOB %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), len(lean), len(disp), len(detach), len(seds), len(mv), sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl),
                  len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    put_txt('b686_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b686_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                        seds=[r['n'] for r in seds], moves_deletes=[r['n'] for r in mv],
                                        delete_shapes=[dict(n=n, deletes=d, globs=gl) for n, d, gl in shapes], outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle', 'SIDE-bijection', 'SIDE-class-number-anomaly',
                                   'SIDE-spinor', 'SIDE-li-map']


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    put_json('b686_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (the named kernel among them, after its merge and tag)' % len(ks))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b686_defects.txt').split(NL)
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
    t = rdn('b686_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b686_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b686_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b686_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


REPAIRS = [
    ('THE N4 SCORER READS BANKS AND NOT THE ENTRY (answering b685 defect (f), under (R296)(2); data/b686_rules.txt row (1)): b685`s sealed',
     '`_n4` (tools/b685_record.py :879-:896) read the landed FINDINGS entry`s head line while `_finding_text` (:969-:1005) composed the entry`s',
     'scores line from the scores bank. b686`s `_n4` reads the pre-push and post-push suite banks (data/b686_checks.txt,',
     'data/b686_checks_postpush.txt: the act arm G-ENTRY-SCORES-EQUAL`s row in each) and the scores bank (data/b686_scores.json), and no ledger',
     'line; the scores route writes the scores bank first, `findings` composes the entry`s scores line from it after, and the bank is not',
     'written again: the readings that wait on a later bank (N4 on the post-push suite, S2 on the root) stand PENDING there with the bank they',
     'wait on named, and are read at the close into data/b686_scores_close.json, which no ledger line reads. The diff of the scorer and of the',
     'entry`s scores line against b685`s sealed copy is printed whole below.'),
    ('THE STANDING SET FOR b686 (answering no defect: the act`s objects): the standing arms are b685`s face`s (G2) arms less b685`s act arms,',
     'the twenty rule arms among them; the runner arms read the last merged runs, this act`s named kernel`s after-run; the step-zero arms read',
     'this act`s banks -- five branches, no remote row.'),
]


def _fn_src(src, name):
    """a top-level function's source, from its `def` line to the next top-level line; '' where the tool carries no such function."""
    if ('\ndef %s(' % name) not in src:
        return ''
    i = src.index('\ndef %s(' % name) + 1
    m = re.search(r'\n(?=\S)', src[i + 1:])
    return src[i:i + 1 + m.start() + 1] if m else src[i:]


def repairs(*a):
    """data/b686_tool_repairs.txt: rows are repairs with the defect they answer. Each tool carried from a sealed b685 copy is read against
    b685's seal hash (relay data/b685_seal_hashes.json) first, and its diff against that copy counted by hunks; tools/rule_arms.py read
    against b685's seal record (unedited in this act); the N4 scorer's and the entry's scores-line diff against b685's sealed copy printed whole."""
    import difflib
    import hashlib
    seal = jl('b685_seal_hashes.json').get('tools') or {}
    rows = []
    for t0 in ('b685_citation.py', 'b685_closing.py', 'b685_reg_gate.py', 'b685_regspec.py', 'b685_tests.py', 'b685_worklist.py',
               'b685_record.py', 'b685_checks.py'):
        t1 = t0.replace('b685_', 'b686_')
        old, new = os.path.join(T, t0), os.path.join(T, t1)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
        rows.append((t0, t1, now, seal.get(t0), len(re.split(r'(?m)^(?=@@ )', d)[1:])))
    ra_now = hashlib.sha256(open(os.path.join(T, 'rule_arms.py'), 'rb').read()).hexdigest()
    ra_act = [x for x in ('b685', 'b684', 'b683') if (jl('%s_seal_hashes.json' % x).get('tools') or {}).get('rule_arms.py')][0]
    seal['rule_arms.py'] = jl('%s_seal_hashes.json' % ra_act)['tools']['rule_arms.py']     # ### b685 sealed none of it; the last record naming it
    s5, s6 = rd(os.path.join(T, 'b685_record.py')), rd(os.path.join(T, 'b686_record.py'))
    nd = []
    for f5, f6 in (('_n4', '_n4'), ('scores', 'scores'), ('_sv', 'scores_line'), ('_finding_text', '_finding_text')):
        nd += list(difflib.unified_diff(_fn_src(s5, f5).split(NL), _fn_src(s6, f6).split(NL), 'b685_record.py %s (sealed)' % f5,
                                        'b686_record.py %s' % f6, n=1, lineterm=''))
    L = ['b686 -- COMPONENT 1 AND COMPONENT 4, (R296)`S FERRY: THE CARRY-TIME READING OF THE TOOLS, AGAINST b685`S SEALED COPIES (%s)' % utc(), '',
         '### rows are the carried tools: b685`s sealed copy and its seal record; the hunks of the diff to b686`s copy. Every hunk is the act`s own',
         '### text -- its names, its banks, its sections and its predicates over this act`s banks -- save the repairs below, each with the defect',
         '### it answers.', '']
    for t0, t1, now, s, nh in rows:
        ex = os.path.exists(os.path.join(T, t1))
        L.append('  %-20s -> %-20s b685 sealed %s ; the seal`s record %s ; %s ; hunks %s' % (t0, t1, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh if ex else 'NOT YET CARRIED'))
    L.append('  %-20s    the standing instrument, unedited in this act: %s ; the last seal record naming it (%s`s) %s ; %s' % (
        'rule_arms.py', ra_now[:16], ra_act, (seal.get('rule_arms.py') or '### NONE')[:16], 'AGREE' if seal.get('rule_arms.py') == ra_now else '### DIFFER'))
    L.append('')
    for i, r in enumerate(REPAIRS, 1):
        L += ['  REPAIR %d -- %s' % (i, r[0])] + ['  ' + x for x in r[1:]]
    L += ['', '### THE DIFF OF THE N4 SCORER, THE SCORES ROUTE AND THE ENTRY`S COMPOSER AGAINST b685`S SEALED COPY (tools/b685_record.py, sha256 %s), '
          'WHOLE:' % (seal.get('b685_record.py') or '### NONE')[:16]] + ['    ' + l for l in nd]
    L += ['', '### ### **REPAIRS %d ; THE SEALED COPIES %s ; TOOLS CARRIED %d ; THE SCORER`S DIFF LINES %d.**' % (
        len(REPAIRS), 'AGREE' if all(s == now for _a, _b, now, s, _n in rows) and seal.get('rule_arms.py') == ra_now else '### DIFFER',
        sum(1 for r in rows if os.path.exists(os.path.join(T, r[1]))), len(nd))]
    put_txt('b686_tool_repairs.txt', L)
    print(L[-1])


def root_banks_state(banks, rev='HEAD'):
    """G-ROOT-BANKS-COMMITTED's reading (standing from (R291)(4)): for every bank the root names, its git status, whether HEAD carries it and
    whether HEAD's blob equals the working file; HEAD against the remote main (one ls-remote)."""
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


ROOT_EXCLUDE = re.compile(r'^b686_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*)\.?(txt|json|md|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b686_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(K.SHARED_APPENDED))


def rootbanks(*a):
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['b686 -- G-ROOT-BANKS-COMMITTED`S READING: THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ;'
         ' carried by HEAD ; HEAD`s blob equal to the file' % utc(), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('b686_root_banks.txt', L)
    put_json('b686_root_banks.json', dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b686_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### G-ROOT-BANKS-COMMITTED: A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b686'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b686_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='b686_ra_') as tmp:
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
    L = ['b686 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b686_root_arm.txt', L)
    put_json('b686_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b686 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b686_table_final.txt', L)
    put_json('b686_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


# ================================================================================ THE SCORES: (N1)-(N5) OF THE FERRY, THE SEAT'S (S1)-(S3)
# ### (R296)(2), data/b686_rules.txt row (1): a scorer reads banks and not the entry; the entry reads the scorer's bank. `scores` writes
# ### data/b686_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there, the bank it waits on named, and
# ### is read at the close by `scores close` into data/b686_scores_close.json, which no ledger line reads.
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b685_closing_push_out.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md', K.FOUND)
ENTRY_ARM = 'G-ENTRY-SCORES-EQUAL'
ARM_ROW = re.compile(r'^  (G-[A-Z0-9-]+)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+(OK|### FAILS|.*)$')


def _git_ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t.isdigit() else None


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s[:19] + 'Z', '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def _first_commit(repo, path):
    """the commit time of the first commit carrying a path (git log --diff-filter=A), or None."""
    t = g(repo, 'log', '--diff-filter=A', '--format=%ct', '--', path).split()
    return int(t[-1]) if t else None


def _arm_row(bank, arm):
    """an arm's row in a suite bank: (LIVE, NEG, POS, verdict) or None where the bank or the row is absent."""
    for l in rdn(bank).split(NL):
        m = ARM_ROW.match(l)
        if m and m.group(1) == arm:
            return m.group(2), m.group(3), m.group(4), m.group(5).strip()
    return None


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', 'FINDINGS.md', 'OPEN_TRAILS.md')
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _n1():
    cm = jl('b686_commands.json')
    ok = bool(cm) and not cm.get('local_lean')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches %d (relay data/b686_commands.txt, %d commands read)' % (
            cm.get('local_lean') if cm else '### UNREAD', len(cm.get('dispatches') or []), len(cm.get('rows') or [])))


def _n2():
    nj, named = jl('b686_naming.json'), jl('b686_naming.json').get('named')
    t_name = _first_commit(RELAY, 'data/b686_naming.txt')
    kwrites = []
    if named:
        td = 'D:/' + named
        base = (jl('b686_kernels_face.json').get('base') or {}).get(named) or ''
        kwrites = [int(x) for x in g(td, 'log', '--format=%ct', '%s..main' % base if base else 'main', '--since=%s' % K.DATE).split() if x.isdigit()]
    printed = 'THE RULE, verbatim' in rdn('b686_naming.txt') and 'THE TABLE ROWS, verbatim' in rdn('b686_naming.txt')
    rows_first = bool(t_name) and (not kwrites or t_name <= min(kwrites))
    calls = jl('b686_author_answers.json').get('calls') or []
    t_prompt = _iso(calls[0]['ts']) if calls and calls[0].get('ts') else None
    t_diff = _first_commit(RELAY, 'data/%s.txt' % K.DIFF_STEM)
    t_roster = _first_commit(PP, K.FOUND) and int((g(PP, 'log', '-1', '--format=%ct', '%s..HEAD' % K.PRE_PP, '--', K.FOUND).split() or ['0'])[0]) or None
    cells_first = bool(t_prompt and t_diff and t_diff <= t_prompt) and (t_roster is None or t_roster == 0 or t_prompt < t_roster)
    t_rep, t_seal = _first_commit(RELAY, 'data/b686_tool_repairs.txt'), _first_commit(RELAY, 'data/b686_seal_hashes.json')
    rep_first = bool(t_rep) and (t_seal is None or t_rep < t_seal)
    ok = printed and rows_first and bool(named) and cells_first and rep_first
    return ('HELD' if ok else 'REFUTED'), (
        'the order`s line, the rule row and the table rows printed from their banks (relay data/b686_naming.txt): %s, committed before any kernel '
        'write (%s, the named document %s): %s; the cell diff (relay data/%s.txt) committed and raised as the act`s first prompt before any roster '
        'write: %s; the scorer`s diff (relay data/b686_tool_repairs.txt) committed before the seal: %s' % (
            printed, 'kernel writes since the act %d' % len(kwrites), named, rows_first, K.DIFF_STEM, cells_first, rep_first))


def _n3():
    cj, cl = jl('b686_cut.json'), jl('b686_cells.json')
    db, da = cj.get('distance_before'), cj.get('distance_after')
    dist = db is not None and da is not None and da <= db
    hand = cl.get('by_hand')
    cells = cl != {} and hand == []
    pe = cj.get('prints_equal')
    prints_ok = (pe is True) if cj.get('kind') == 'kernel' else True
    ok = dist and cells and prints_ok
    return ('HELD' if ok else 'REFUTED'), (
        'the distance by the b670 method before %s, after %s (relay data/b686_cut.txt): at or below %s; Correspondence cells written by hand: %s '
        '(relay data/b686_cells.txt -- every changed line of the roster commit one the generator wrote); the named document a %s`s, its prints '
        'before and after equal line for line: %s' % (db, da, dist, hand if hand is not None else '### UNREAD', cj.get('kind'), pe))


def _n4():
    """(R296)(2): N4 read from the suite banks -- the act arm G-ENTRY-SCORES-EQUAL`s row in the pre-push and the post-push bank, each the
    comparison of the landed entry`s scores line with the scores bank as the suite read them -- and the scores bank itself; no ledger line."""
    pre, post = _arm_row('b686_checks.txt', ENTRY_ARM), _arm_row('b686_checks_postpush.txt', ENTRY_ARM)
    S = jl('b686_scores.json')
    sb = bool(S) and all(k in S for k in SCORE_KEYS)
    good = lambda r: r is not None and r[0] == 'PASS' and r[3] == 'OK'   # noqa: E731
    if post is None:
        return 'PENDING', ('waits on the post-push suite bank (relay data/b686_checks_postpush.txt); %s`s pre-push row %s; the scores bank '
                           '(relay data/b686_scores.json) %s' % (ENTRY_ARM, ' '.join(pre) if pre else '### NOT YET RUN', 'written' if sb else '### UNWRITTEN'))
    ok = sb and good(pre) and good(post)
    return ('HELD' if ok else 'REFUTED'), (
        'the entry`s scores line equal to the scores bank`s reading, read by %s in the pre-push suite (%s) and the post-push suite (%s), relay '
        'data/b686_checks.txt and data/b686_checks_postpush.txt; the scores bank relay data/b686_scores.json %s; N4 read from these banks and no '
        'ledger line (data/b686_rules.txt row (1))' % (ENTRY_ARM, ' '.join(pre) if pre else '### ABSENT', ' '.join(post), 'written' if sb else '### UNWRITTEN'))


def _n5():
    face = jl('b686_kernels_face.json').get('kernels') or {}
    named = jl('b686_naming.json').get('named')
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b686_|audit_b686_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    kmain = []
    if named:
        td = 'D:/' + named
        base = (jl('b686_kernels_face.json').get('base') or {}).get(named) or ''
        kmain = [l for l in g(td, 'log', '--first-parent', '--format=%h %s', '%s..main' % base).split(NL) if l.strip()] if base else ['### NO BASE READ']
        wfile = _show(td, 'main', '.github/workflows/build-module.yml') or ''
        widents = [w for w in IDENT if w in wfile.lower()]
    else:
        widents = []
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import importlib
    argv, sys.argv = sys.argv, sys.argv[:1]
    try:
        CH = importlib.import_module('b686_checks')
    finally:
        sys.argv = argv
    new_arms = sorted(set(a_[0] for a_ in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    ob = jl('b686_commands.json').get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = k_ok and not pp_beyond and not kinds_beyond and not differ and not new_arms and not ident and not pat and not widents
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it %s, the named kernel %s`s '
            'main written by the first-parent commits %s alone; standing arms added: %s (the act`s arms over its own banks %d); sealed tools not '
            'agreeing %s; PLACE-papers beyond FINDINGS, OPEN_TRAILS and the regenerated roster file: %s; relay files of a kind beyond the act`s '
            'banks and tools, the table, the root list and b685`s push-out bank: %s; "patent" in the lines written: %s; outbound requests: the '
            'seat`s git reads and pushes at github.com and %d web searches, subagent prompts and fetches (relay data/b686_commands.txt), an '
            'identifier of the author in %s; in the named kernel`s workflow file %s' % (
                K.DRAFT, k_ok, named, kmain or 'NONE', new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE',
                kinds_beyond or 'NONE', pat or 'NONE', len(ob), [r['line'] for r in ident] or 'NONE', widents or 'NONE'))


def _s_scores():
    TF, RA_ = jl('b686_table_final.json'), jl('b686_root_arm.json')
    _r, _n, sh = seal_hashes()
    return {
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))
               if TF else 'waits on the final table (relay data/b686_table_final.json)'),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally' if RA_
               else 'waits on the root and its arm (relay data/b686_root_arm.json), computed after the entry'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }


def scores(*a):
    """`scores [dry]` writes data/b686_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads N4 and the
    readings that waited into data/b686_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:700]))
    if 'dry' in a:
        return
    if close:
        put_json('b686_scores_close.json', dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, 'b686_scores.json')):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('b686_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def scores_line(S):
    """the entry's scores line, composed from the scores bank alone (the act arm G-ENTRY-SCORES-EQUAL composes it the same way and compares)."""
    return '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.'


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, answers=answers, naming=naming, runner=runner, prints=prints, cutdiff=cutdiff,
              commands=commands, kernels=kernels, defects=defects, repairs=repairs, rootbanks=rootbanks, root=root, root_arm=root_arm,
              table_final=table_final, scores=scores, gendry=gendry, dist=dist, partner=partner, cells=cells)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b686_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
