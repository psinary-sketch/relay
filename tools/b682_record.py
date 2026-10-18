# -*- coding: utf-8 -*-
"""b682_record.py -- THE ACT'S RECORD TOOL, b682 under (R292).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b682's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b681_record.py (the helpers, the guarded landing, the readers, step zero's rowgen and branches routes);
### the later routes are added at their components.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b682_record.py <route> [dry]`.
"""
import collections
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
import b682_worklist as K          # noqa: E402

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
    none a number any bank carries; a stand-in run writes no bank. Carried from b681_record.py with b682's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b682_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b682_findings.json': dict(entry_line=99999, title='stand-in'),
        'b682_trail.json': dict(line=99999),
        'b682_act_root.json': dict(root='0' * 64, previous='13735beb' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b682's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b682_scanfile_%s.md' % tag)
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
    """a row of data/b682_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


READERS = ['read_score_row', 'read_head', 'read_branch_row']


# ================================================================================ STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE (b670's route, carried)
def roster():
    """the 19 roster tables of data/b586_corroboration.txt :34, at the paths that bank read (carried from b670_record.py :548-:552)."""
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b682_rowgen_<stage>.txt."""
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
    L = ['b682 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b682_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R292)(6))
def branches(*a):
    """every branch (R292)(6) names, its tip read before any delete, its fate; any branch under the push-b681 prefix that --merged lists and
    the ruling does not name, reported and KEPT. No remote branch is named this act. data/b682_branches.txt (.json)."""
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
            if x.startswith('push-b681') and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b682 -- STEP ZERO, (R292)(6): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local ; tip ; listed by `git branch --merged main --list <name>` ; fate. Deleted by name in',
         '### the house form, each delete command naming one branch with no glob in any half, one command per call, in sequence; no branch the',
         '### ruling does not name.']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                               r['fate']) for r in rows]
    L += ['', '### branches under the push-b681 prefix that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; TO BE DELETED %d ; UNNAMED UNDER THE PREFIX %d.**' % (
        len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), len(rows), len(extra))]
    put_txt('b682_branches.txt', L)
    put_json('b682_branches.json', dict(at=utc(), rows=rows, extra=[list(x) for x in extra]))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R292)(1)
WH = ('*Appended 2026-10-18 by b682 to b681’s entry (:9110), under `(R292)`(1) -- b681 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b681_closing.txt):*')
WB = (' “b681 closed: relay aa5a33a7, PLACE-papers 837ba79; suite 90 of 90; root 13735beb3696824b…; 1 prompt answered; 1 defect” '
      '(data/b681_closing.txt :1), the closing pushed and read back at relay f17fef29 (data/b681_closing_push_out.txt :4-:5). The suite 90 of 90 '
      'before and after the record push; all 163 certified zeros of Q0 narrowed to half-width 1e-30, the measured h_tol(64) = 3.162e-28 less two '
      'decimal orders, each by the form b671 used for it -- 146 on the line by the sign change, 17 off it by the quarter count -- no (4a) offset '
      'needed, no point stopped; 68 foreground parts against the plan’s 72, 27,693 s, the longest 471 s, no run detached; the Bessel bar 2^-200 '
      'met at every evaluation across 88,128 segment units; C1 ten ζ zeros narrowed and inside, C2 refused; the new bank '
      'data/b681_epstein_zeros_narrowed.json.gz with its hashes bank chaining from b671’s, which stands beside it; the root repair -- the '
      'corrigendum row, act_root.py repaired and sealed, the chain AGREE b624 to b680, 57 of 57, b681 chained from b680’s root as recorded; '
      'G-ROOT-BANKS-COMMITTED declared; `W-ORD-EPSTEIN-BALL-WIDTH` DISCHARGED (OPEN_TRAILS :14712); `W-ORD-MAP-ANGLE-FORM` entered (:14714); one '
      'defect (a), the seat’s -- the author’s word on the pause acted on before its mid-act check, the check run after and finding nothing to '
      'verify in a word naming no path, line or commit. The mirror mirror-refresh-2026-10-18-b681.zip made at b681’s close, CLEAN with the root '
      'line. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b682_record_lines.json', 'c1', entry=K.B681_ENTRY,
         check=[('FINDINGS.md', K.B681_ENTRY, '## The 163 certified zeros'), ('OPEN_TRAILS.md', K.B681_TRAIL, '### b681')], dry=dry)


# ================================================================================ THE ANSWERS BANK (b681's route, carried)
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
    """data/b682_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
    every word of the author delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim."""
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
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((ln, c['id'], c['input'], o.get('timestamp')))
                ask.add(c['id'])
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask:
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
    head = ['### b682 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b682_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b682_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 2: THE GENERATOR'S DRY RUN, BANKED AS A CELL DIFF ((R292)(3))
DIFF_ROW = re.compile(r'^    (\S+) :(\d+) \| (kernel|profile|status) \| (SIDE-[a-z0-9-]+) \| OLD (.*) \| NEW (.*)$')


def read_diff_row(line):
    """a row of the generator's diff: document, line, column, kernel, the cell before and after; returns (document, line, column, old, new)."""
    m = DIFF_ROW.match(line or '')
    if not m:
        raise ValueError('diff row of another shape: %r' % ((line or '')[:120],))
    return m.group(1), int(m.group(2)), m.group(3), m.group(5), m.group(6)


READERS += ['read_diff_row']


def gendry(*a):
    """tools/correspondence_gen.py `dry full` over the roster the generator reads (data/b672_roster_read.json, 20 tables), nothing written to any
    roster file; its whole print banked as data/b682_correspondence_diff.txt, rows the cells with before and after, the figures 20 / 14 beside
    the ruling's 13 (the navigator's answer on the roster)."""
    t0 = time.time()
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'correspondence_gen.py'), 'dry', 'full'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', cwd=ROOT, timeout=560)
    out = (r.stdout or '') + (r.stderr or '')
    full = out.split(NL)
    k = max(i for i, l in enumerate(full) if l.startswith('b672 -- THE CORRESPONDENCE GENERATOR'))
    body = [l for l in full[k:] if l != '### DRY: nothing written']
    rows = [read_diff_row(l) for l in body if DIFF_ROW.match(l)]
    v = [l for l in body if l.startswith('### ### **TABLES')]
    tm = re.search(r'TABLES (\d+) ; SHAPED (\d+)', v[0]) if v else None
    five = [x for x in rows if x[0] == 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME' and x[1] in K.FIVE]
    L = ['b682 -- COMPONENT 2, (R292)(3): THE CORRESPONDENCE GENERATOR`S DRY RUN AFTER THE READER`S EXTENSION, BANKED AS A CELL DIFF (%s)' % utc(), '',
         '### tools/correspondence_gen.py at relay %s (the reader extended, committed alone at 60e8de3e) run `dry full` over the roster it reads,' % (
             g(ROOT, 'rev-parse', '--short=8', 'HEAD').strip()),
         '### relay data/b672_roster_read.json: TABLES %s ; SHAPED %s (the navigator`s answer on the roster: all 20 tables, 14 in the generator`s' % (
             tm.group(1) if tm else '?', tm.group(2) if tm else '?'),
         '### shape and 6 held as NOT IN THE GENERATOR`S SHAPE, beside the ruling`s "13 roster files", a count carried from (R283)(1)); the local',
         '### clones` tags, no remote call; NOTHING WRITTEN to any roster file. Rows are cells with before and after (the THE DIFF section below:',
         '### document :line | column | kernel | OLD | NEW); exit %d ; %d s.' % (r.returncode, int(time.time() - t0)), '',
         '### THE FIVE CELLS OF (R292)(2) (FOUNDATIONS :628-:630), from the diff: %d' % len(five)]
    L += ['    :%d %s | OLD %s | NEW %s' % (x[1], x[2], x[3][:90], x[4][:90]) for x in five]
    L += ['', '### THE GENERATOR`S PRINT, WHOLE:'] + body
    L += ['', '### ### **CELLS CHANGED %d ; THE FIVE CELLS AT FOUNDATIONS :628-:630 %d ; TABLES %s (THE RULING`S 13) ; SHAPED %s ; GENERATOR EXIT %d ; '
              'NOTHING WRITTEN TO THE ROSTER.**' % (len(rows), len(five), tm.group(1) if tm else '?', tm.group(2) if tm else '?', r.returncode)]
    put_txt('b682_correspondence_diff.txt', L)
    print(NL.join(L[8:9 + len(five)] + L[-1:]))


# ================================================================================ THE AUTHOR'S WORD, A DATED LINE AT THE b680 ARMS CENSUS
ARMS_CENSUS = 14694
AH = ('*Appended 2026-10-18 by b682 to b680’s arms census (:14694), under `(R292)` -- THE AUTHOR’S WORD ON THE RULES WITHOUT ARMS, given '
      '2026-10-18, verbatim:*')
AB = (' “arms for the traceable ones, the seat sorts them”. Its reading for b683’s ruling: of the 24 rules without arms in relay '
      'data/b680_rules_arms.txt, the seat sorts each as TRACEABLE (its breach leaves a trace a suite can read in a bank, a capture or the tree) '
      'or PROSE (its breach leaves no such trace), prints the sort with the trace each TRACEABLE rule would be read from, and the TRACEABLE '
      'rules receive standing arms under b683’s ruling after the author has seen the sort; no arm written in this act. Banked as relay '
      'data/b682_rules.txt row (1).')


def word(*a):
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', AH, NL + AH + AB + NL)], 'b682_record_lines_word.json', 'word',
         check=[('OPEN_TRAILS.md', ARMS_CENSUS, '**The arms and the rules:**')], dry=dry)


# ================================================================================ COMPONENT 3: THE CORRESPONDENCE DISTANCE BY BOTH METHODS ((R292)(4))
def dist(*a):
    """the distance by b670's method (tools/b672_record.py `after`, b670's method over the stable anchors, as b680 read it in
    tools/b680_readings.py `corr` :122-:150) and by the generator's claim, each route run by import with its bank writers captured in memory
    so nothing of b670's or b672's is written; printed beside b680's 55 and 0. data/b682_correspondence_<stage>.txt (.json)."""
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
    L = ['b682 -- COMPONENT 3, (R292)(4): THE CORRESPONDENCE DISTANCE %s THE GENERATOR`S WRITE, BY b670`S METHOD AND BY THE GENERATOR`S CLAIM (%s)' % (
        stage.upper(), utc()), '',
         '### the methods as b680 ran them (tools/b680_readings.py `corr` :122-:150): b670`s (tools/b670_record.py `corr`) by its heading-text',
         '### reader; b672`s re-read of b670`s method over the stable anchors (tools/b672_record.py `after`), its last two verdicts the distance',
         '### by b670`s method and at the generator`s claim; each run by import, its bank writers captured, nothing of b670`s or b672`s written.',
         '### PLACE-papers HEAD %s.' % g(PP, 'rev-parse', '--short', 'HEAD').strip(), '',
         '### BY b670`S HEADING-TEXT READER: ' + v1,
         '### BY THE STABLE ANCHORS (b672`s re-read): ' + (vv[-2] if len(vv) >= 2 else '### UNREAD'),
         '### THE GENERATOR`S CLAIM: ' + (vv[-1] if vv else '### UNREAD'), '',
         '### ### **%s: BEHIND BY b670`S METHOD %s AGAINST b680`S 55 ; AT THE GENERATOR`S CLAIM %s AGAINST b680`S 0 ; BY b670`S HEADING-TEXT READER %s.**' % (
             stage.upper(), m2.group(2) if m2 else '### UNREAD', m3.group(1) if m3 else '### UNREAD', m1.group(1) if m1 else '### UNREAD'), '',
         '### THE ANCHORED RE-READ, WHOLE:'] + T2
    put_txt('b682_correspondence_%s.txt' % stage, L)
    put_json('b682_correspondence_%s.json' % stage, dict(at=utc(), behind=int(m2.group(2)) if m2 else None, claim=int(m3.group(1)) if m3 else None,
                                                       heading_reader=int(m1.group(1)) if m1 else None))
    print(L[11])


def partner(*a):
    """the navigator's answer on the roster write: the one-copy partner of FOUNDATIONS, whose table differs, is not written; the difference
    entered as rows of the diff bank (data/b682_correspondence_diff.txt, appended) with both tables' cells by line, carried under
    W-ORD-ONE-COPY as a reading, nothing moved."""
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
    L = ['', '### APPENDED %s by the record tool `partner` (the navigator`s answer on the roster write): THE ONE-COPY PARTNER NOT WRITTEN -- %s' % (
        utc(), t['partner']),
         '### its table (:%d-:%d) against the roster`s file %s (:%d-:%d), at PLACE-papers HEAD %s after the write; rows are table lines that differ,' % (
             fb[0] + 1, fb[1], t['path'], fa[0] + 1, fa[1], g(PP, 'rev-parse', '--short', 'HEAD').strip()),
         '### each with both tables` cells by line; carried under W-ORD-ONE-COPY as a reading, nothing moved:']
    for la, x, lb, y in rows:
        L += ['    ROSTER :%s | %s' % (la, x), '    PARTNER :%s | %s' % (lb, y)]
    L += ['### ### **PARTNER TABLE LINES DIFFERING %d ; WRITTEN 0 ; CARRIED UNDER W-ORD-ONE-COPY.**' % len(rows)]
    p = os.path.join(D, 'b682_correspondence_diff.txt')
    old = open(p, 'rb').read()
    new = old + (NL.join(L) + NL).encode('utf-8')
    open(p + '.tmp', 'wb').write(new)
    os.replace(p + '.tmp', p)
    print(L[-1])


# ================================================================================ COMPONENT 3: THE ORDER DISCHARGED ((R292)(4))
ORDERS = 'b670_work_orders.txt'
OH = ('*Appended 2026-10-18 by b682 beneath the order’s entry (:14648) and b681’s trail record (:14716), under `(R292)`(4) -- '
      '`W-ORD-CORRESPONDENCE-RUNNER-BANKS` DISCHARGED:*')
OB = (' relay tools/correspondence_gen.py’s reader extended to the runner print banks as b674, b676 and b678 banked them (the axioms bank beside '
      'its runner bank, the built commit read from the runner bank’s header), committed alone (relay 60e8de3e); five planted cases as wanted '
      '(relay data/b682_gen_test.txt); the generator’s run over the 20 roster tables wrote 5 cells, the five at FOUNDATIONS_OF_THE_SIDE_PROGRAMME '
      ':628-:630 that b678 carried at :14620 -- the kernel SIDE-silence-principle v0.2.0 to v0.2.1 in the three rows, the profile “NO PRINT BANK '
      'AT v0.2.0” to “axiom-free (none)” at :628 and :629 from the runner print bank at the tag v0.2.1 (relay '
      'data/b678_axioms_SIDE-silence-principle_after.txt), the profile at :630 held as two tokens and agreeing with the bank. The distance '
      'by b670’s method 55 before and after, against b680’s 55 -- the five clauses carry no backticked commit, so that method does not count '
      'them -- and at the generator’s claim 0 against 0. The partner copy’s differing table not written, carried under `W-ORD-ONE-COPY` as a '
      'reading. Pin: relay data/b682_correspondence_diff.txt. Status DISCHARGED.')


def c3(*a):
    """(R292)(4): the discharge line on OPEN_TRAILS, then its row appended to the orders bank additively ((R254)(2))."""
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', OH, NL + OH + OB + NL)], 'b682_record_lines_c3.json', 'c3',
         check=[('OPEN_TRAILS.md', K.ORDER_LINE, 'W-ORD-CORRESPONDENCE-RUNNER-BANKS'), ('OPEN_TRAILS.md', K.B681_TRAIL, '### b681')], dry=dry)
    if dry:
        return
    ln = jl('b682_record_lines_c3.json')['lines'][0]['line']
    rows = ['### Appended 2026-10-18 by b682 under (R292)(4) (additive, (R254)(2)): W-ORD-CORRESPONDENCE-RUNNER-BANKS DISCHARGED, its pin the diff bank; '
            'its Status cell filled and its line its pin.',
            '  %-44s :%d  %s   %-5d %-16s :%d  %s [:%d]' % ('W-ORD-CORRESPONDENCE-RUNNER-BANKS', K.ORDER_LINE, 'b679', 3, 'DISCHARGED', ln,
                                                            'pinned by data/b682_correspondence_diff.txt', ln)]
    for r in rows[1:]:
        read_order_row(r)
    p = os.path.join(D, ORDERS)
    old = open(p, 'rb').read()
    sep = NL if old.endswith(b'\n') else NL + NL
    new = old + (sep + NL.join(rows) + NL).encode('utf-8')
    if not new.startswith(old):
        sys.exit('### THE ORDERS BANK APPEND IS NOT ADDITIVE -- NOTHING WRITTEN')
    open(p + '.tmp', 'wb').write(new)
    os.replace(p + '.tmp', p)
    print('  data/%s appended (%d bytes before, %d after)' % (ORDERS, len(old), len(new)))


ORDER_ROW = re.compile(r'^  (W-ORD-[A-Z0-9-]+)\s+:(\d+)\s+(b\d+)\s+(\d+)\s+(OPEN|DISCHARGED|ACTED|NOT STATED|CLOSED)\s+:(\d+)\s+(.+?) \[:(\d+)\]$')


def read_order_row(line):
    """a row of data/b670_work_orders.txt: the order, its entry line, its act, its age, its Status, its status line and its trigger or pin;
    returns (order, status, trigger)."""
    m = ORDER_ROW.match(line or '')
    if not m:
        raise ValueError('order row of another shape: %r' % ((line or '')[:120],))
    return m.group(1), m.group(5), m.group(7)


READERS += ['read_order_row']


# ================================================================================ COMPONENT 4: THE NAMING, (R292)(5) -- before any kernel write (b678's route)
def _kern_rows():
    """the kernels table's rows (data/b647_table_kernels.txt): rows | MATCHES | UNDERSTATES | OVERREACHES | UNLICENSED (its header :4)."""
    out = []
    for i, l in enumerate(rdn(K.KERNELS_BANK).split(NL), 1):
        m = re.match(r'^  (SIDE-[\w-]+)\s+([0-9a-f]{7}) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|', l)
        if m:
            out.append(dict(line=i, text=l, kernel=m.group(1), pin=m.group(2), rows=int(m.group(3)), under=int(m.group(5)),
                            over=int(m.group(6)), unlic=int(m.group(7))))
    return out


def naming(*a):
    """(R292)(5) and N4: the order's line (data/b652_ferry.txt :19), the tie-break rule's row and the table rows printed verbatim from their
    banks; every kernel's standing count read from the licensed table (a kernel cut since its read stands at its cut bank's figure); the
    document named by the descending count and, at a tie, by the rule's letter; then the named kernel's workflow directory, print list and
    print bank read or declared absent -- before any kernel write. data/b682_naming.txt (.json). Carried from b678_record.py's naming."""
    rules = rdn(K.RULES_BANK).split(NL)
    i0 = [i for i, l in enumerate(rules) if l.startswith('  (%d) ' % K.TIE_RULE_ROW)][0]
    rule = [rules[i0]] + [l for l in __import__('itertools').takewhile(lambda x: x.startswith('      '), rules[i0 + 1:])]
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
        m = re.search(r'THE DISTANCE BEFORE (\d+), AFTER (\d+)', t)
        if m and needle in t:
            cut_since[k] = (int(m.group(2)), bank)
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
    pfx = 'SIDEBijection' if named == 'SIDE-bijection' else 'X'
    pshape = r"'%s\.[A-Za-z0-9_.']+' (depends on axioms|does not depend on any axioms)|^  %s\.[A-Za-z0-9_.']+ +\[" % (pfx, pfx)
    pb = sorted(set(g(ROOT, 'grep', '-lE', pshape, '--', 'data/').split()))
    ctl = sorted(set(g(ROOT, 'grep', '-lE', r"'SIDESilencePrinciple\.[A-Za-z0-9_.']+' (depends on axioms|does not depend on any axioms)", '--', 'data/').split()))
    tags = sorted(g(td, 'tag', '--list').split(), key=lambda x: [int(n) for n in re.findall(r'\d+', x)]) if td else []
    L = ['b682 -- COMPONENT 4, (R292)(5): THE ORDER, THE RULE ROW AND THE TABLE ROWS, VERBATIM, BEFORE THE DOCUMENT IS NAMED (%s)' % utc(), '',
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
        L.append('### A TIE: the rule of row %d by its letter -- rows outside LICENSED/CITED of any kind: %s' % (
            K.TIE_RULE_ROW, ', '.join('%s %d (rows %d)' % (x[3], x[1], x[2]) for x in tied)))
    L += ['### NAMED: %s docstrings' % (named or '### NONE'),
          '', '### THE NAMED KERNEL`S WORKFLOW DIRECTORY, PRINT LIST AND PRINT BANK (read before any kernel write):',
          '  %s main %s ; its tags %s, the last %s at %s: .github/workflows/ carries %s -- %s' % (
              named, g(td, 'rev-parse', '--short', 'main').strip(), tags, tags[-1] if tags else '-',
              g(td, 'rev-parse', '--short', (tags[-1] if tags else 'main') + '^{commit}').strip(),
              wf or 'NOTHING', 'a build-module.yml' if any('build-module' in f for f in wf) else 'NO build-module.yml (no dispatch input; no print step)'),
          '  print_targets.txt at its root: %s ; AxiomCheck*.lean at its root: %s' % ('print_targets.txt' in pt, [f for f in pt if f.startswith('AxiomCheck')] or 'NONE'),
          '  relay tracked banks carrying a printed axiom line of a %s declaration (git grep -lE over data/): %s -- %s' % (
              pfx, pb or 'NONE', 'NO PRINT BANK' if not pb else 'a print bank'),
          '  the control, the same shape over SIDE-silence-principle`s declarations: %d bank(s), b678`s after bank among them %s' % (
              len(ctl), 'data/b678_axioms_SIDE-silence-principle_after.txt' in ctl),
          '  its dependency form: lakefile.lean, no require (Mathlib-free) %s ; lean-toolchain %s' % (
              'require' not in (_show(td, 'main', 'lakefile.lean') or 'require'), (_show(td, 'main', 'lean-toolchain') or '').strip()),
          '', '### ### **NAMED %s ; TIED %d ; WORKFLOW build-module.yml %s ; PRINT LIST %s ; PRINT BANK %s.**' % (
              named or '### NONE', len(tied), 'PRESENT' if any('build-module' in f for f in wf) else 'ABSENT',
              'PRESENT' if 'print_targets.txt' in pt else 'ABSENT', 'PRESENT' if pb else 'ABSENT')]
    put_txt('b682_naming.txt', L)
    put_json('b682_naming.json', dict(at=utc(), named=named, tied=[x[3] for x in tied], top=top, workflows=wf, print_banks=pb, tags=tags,
                                      rank=[[x[0], x[1], x[2], x[3], x[4]] for x in rank]))
    print(NL.join(L[-12:]))


# ================================================================================ COMPONENT 4: THE RUNS, THE PRINTS, THE CUT'S DIFF (b678's routes, carried)
def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def read_runner_row(r):
    """a row of data/b682_runner_rows.json: the kernel, its label (before or after), the ref (40 hex), the run id and the gate; returns
    (label, gate)."""
    if not isinstance(r, dict) or r.get('label') not in ('before', 'after') or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') \
            or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['label'], r['gate']


READERS += ['read_runner_row']


def runner(*a):
    """`runner <run id> <ref> <label>`: the named kernel's run read by its id; the artifact listed, downloaded by its id into memory, its sha256
    against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP; the axioms output
    of the print step banked whole, every name of the list matched to one printed line. data/b682_runner_<kernel>_<label>.txt,
    data/b682_axioms_<kernel>_<label>.txt and a row of data/b682_runner_rows.json. Carried from b678_record.py's runner."""
    import hashlib
    import io as _io
    import zipfile
    run_id, ref, label = int(a[0]), a[1], a[2]
    repo = 'psinary-sketch/' + K.CANDIDATE
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(kernel=K.CANDIDATE, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None)
    L = ['b682 -- COMPONENT 4, (R292)(5): THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (K.CANDIDATE, label.upper(), utc()), '',
         '### the dispatch: at main (the workflow %s, the print list %s), the ref input %s ; the target `%s`' % (K.T_WORKFLOW, K.T_MAIN, ref, K.T_TARGET)]
    if label == 'before':
        L.append('### THE PRINT BANK AT MAIN: main %s is the tag %s (%s) with the workflow and print-list commits atop it (%s past %s), no .lean '
                 'byte changed' % (K.T_MAIN, K.T_LAST_TAG, K.T_PRE_MAIN, g(K.TD, 'rev-list', '--count', '%s..%s' % (K.T_LAST_TAG, K.T_MAIN)).strip(),
                                   K.T_LAST_TAG))
    L.append('### the run: id %s ; %s ; status %s ; conclusion %s ; %s to %s' % (run_id, run.get('url'), run.get('status'), run.get('conclusion'),
                                                                               run.get('createdAt'), run.get('updatedAt')))
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
    put_txt('b682_runner_%s_%s.txt' % (K.CANDIDATE, label), L)
    if row['artifact_sha256']:
        put_txt('b682_axioms_%s_%s.txt' % (K.CANDIDATE, label), ax.split(NL))
    j = jl('b682_runner_rows.json') if os.path.isfile(os.path.join(D, 'b682_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if r.get('label') != label] + [row]
    put_json('b682_runner_rows.json', dict(rows=rows))
    print(NL.join(L))


def prints(*a):
    """the 'before' and 'after' axioms outputs compared line for line (the merge only where they are equal at every line).
    data/b682_prints_compare.txt."""
    b, f = rdn('b682_axioms_%s_before.txt' % K.CANDIDATE), rdn('b682_axioms_%s_after.txt' % K.CANDIDATE)
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bl, fl = b.rstrip(NL).split(NL), f.rstrip(NL).split(NL)
    diff = [(i + 1, x, y) for i, (x, y) in enumerate(zip(bl, fl)) if x != y] + ([('length', len(bl), len(fl))] if len(bl) != len(fl) else [])
    L = ['b682 -- COMPONENT 4: THE PRINTS BEFORE AND AFTER THE CUT, LINE FOR LINE (%s)' % utc(), '',
         '### before: relay data/b682_axioms_%s_before.txt (%s, %d lines) ; after: relay data/b682_axioms_%s_after.txt (%s, %d lines)' % (
             K.CANDIDATE, K.T_MAIN, len(bl), K.CANDIDATE, K.T_CUT, len(fl)), '### the lines that differ:'] + (['    %s : %s | %s' % d for d in diff] or ['    NONE'])
    L += ['', '### ### **PRINTS BEFORE %d LINES ; AFTER %d LINES ; DIFFERING %d ; EQUAL LINE FOR LINE %s.**' % (len(bl), len(fl), len(diff), not diff)]
    put_txt('b682_prints_compare.txt', L)
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


CONTROL_NEEDLE = 'theorem sideIDS_total_seven'


def cutdiff(*a):
    """(R292)(5): the cut's diff (the print-list main to the cut tip), printed whole; the files it touches; each file's text with its comments
    stripped compared before and after (equal = no line the elaborator reads changed), with a positive control (a one-word code change in
    the after text must make the comparison unequal). data/b682_cut_diff.txt."""
    files = g(K.TD, 'diff', '--name-only', K.T_MAIN, K.T_CUT).split()
    d = g(K.TD, 'diff', '--unified=0', K.T_MAIN, K.T_CUT).replace(chr(13), '')
    rows = []
    for f in files:
        b, n = _show(K.TD, K.T_MAIN, f) or '', _show(K.TD, K.T_CUT, f) or ''
        eq = _strip_comments(b) == _strip_comments(n)
        ctl = _strip_comments(b) == _strip_comments(n.replace(CONTROL_NEEDLE, CONTROL_NEEDLE + '_', 1))
        rows.append((f, eq, ctl, CONTROL_NEEDLE in n))
    plus = [l for l in d.split(NL) if l.startswith('+') and not l.startswith('+++')]
    minus = [l for l in d.split(NL) if l.startswith('-') and not l.startswith('---')]
    L = ['b682 -- COMPONENT 4, (R292)(5): THE CUT`S DIFF, RESTRICTED TO COMMENT AND DOCSTRING LINES (%s)' % utc(), '',
         '### %s %s (main, the print list) -> %s (the cut, %s); files %s ; lines added %d, removed %d' % (
             K.CANDIDATE, K.T_MAIN, K.T_CUT, K.T_BRANCH, files, len(plus), len(minus)),
         '### rows are files: the text with every comment stripped equal before and after ; the control (a one-word code change in the after',
         '### text) unequal ; the control`s needle present:']
    L += ['  %-34s CODE EQUAL %s ; CONTROL UNEQUAL %s ; NEEDLE PRESENT %s' % (f, eq, not ctl, nd) for f, eq, ctl, nd in rows]
    L += ['', '### the diff, whole:'] + ['    ' + l for l in d.rstrip(NL).split(NL)]
    ok = files == list(K.T_CUT_FILES) and all(eq and not ctl and nd for _f, eq, ctl, nd in rows)
    L += ['', '### ### **FILES %d ; CODE EQUAL WITH COMMENTS STRIPPED %s ; CONTROLS UNEQUAL %s ; COMMENT AND DOCSTRING LINES ALONE %s.**' % (
        len(files), all(r[1] for r in rows), all(not r[2] for r in rows), ok)]
    put_txt('b682_cut_diff.txt', L)
    print(L[-1])


# ================================================================================ THE LATE ROUTES (b681's, carried; every row read through READERS)
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
    """(R292)(6): a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    return names, [ch for ch in '*?[' if ch in c]


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    mv = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'(^|&&\s*|;\s*)gh workflow run\b', QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'Start-Process|\bnohup\b|run_in_background', r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    L = ['b682 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE DISPATCHES, THE MOVES AND DELETES (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (%d):' % len(disp)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN (%d):' % len(detach)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R292)(6): one branch per command, no glob in any half): ' + '; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes)]
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; MOVE OR DELETE '
              'COMMANDS %d ; BRANCH DELETES OF ONE BRANCH AND NO GLOB %d OF %d.**' % (len(rows), len(hits), len(lean), len(disp), len(detach), len(mv),
                                                                                   sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl), len(shapes))]
    put_txt('b682_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b682_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                        moves_deletes=[r['n'] for r in mv], delete_shapes=[dict(n=n, deletes=d, globs=gl) for n, d, gl in shapes]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle', 'SIDE-bijection']


def kernels(*a):
    ks = list(_kerns())
    put_json('b682_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-bijection among them, after its merge and tag)' % len(ks))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b682_defects.txt').split(NL)
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
    t = rdn('b682_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b682_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b682_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b682_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


REPAIRS = [
    ('THE SUITE`S ACT LISTS SET FOR b682 (answering no defect; the act`s object is a shared tool): tools/b682_checks.py`s instrument list',
     'leaves out tools/correspondence_gen.py and tools/test_correspondence_gen.py, which (R292)(3) orders changed, and takes in b681`s tools',
     'and act_root.py (no longer sealed with the act); G-PP-SCOPE reads FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md beside the two ledgers;',
     'the standing runner arms read this act`s merged run, SIDE-bijection`s, the last merged; all declared on the face.'),
]


def repairs(*a):
    """data/b682_tool_repairs.txt: rows are repairs with the defect they answer. Each tool carried from a sealed b681 copy is read against
    b681's seal hash (relay data/b681_seal_hashes.json) first, and its diff against that copy counted by hunks."""
    import hashlib
    seal = jl('b681_seal_hashes.json').get('tools') or {}
    rows = []
    for t0 in ('b681_citation.py', 'b681_closing.py', 'b681_reg_gate.py', 'b681_regspec.py', 'b681_tests.py', 'b681_worklist.py',
               'b681_record.py', 'b681_checks.py'):
        t1 = t0.replace('b681_', 'b682_')
        old, new = os.path.join(T, t0), os.path.join(T, t1)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
        rows.append((t0, t1, now, seal.get(t0), len(re.split(r'(?m)^(?=@@ )', d)[1:])))
    L = ['b682 -- COMPONENT 5, (R292)`S FERRY: THE CARRY-TIME READING OF THE TOOLS, AGAINST b681`S SEALED COPIES (%s)' % utc(), '',
         '### rows are the carried tools: b681`s sealed copy and its seal record; the hunks of the diff to b682`s copy. Every hunk is the act`s own',
         '### text -- its names, its banks, its sections and its predicates over this act`s banks -- save the repairs below, each with the defect',
         '### it answers.', '']
    for t0, t1, now, s, nh in rows:
        L.append('  %-20s -> %-20s b681 sealed %s ; the seal`s record %s ; %s ; hunks %d' % (t0, t1, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh))
    L.append('')
    for i, r in enumerate(REPAIRS, 1):
        L += ['  REPAIR %d -- %s' % (i, r[0])] + ['  ' + x for x in r[1:]]
    L += ['', '### ### **REPAIRS %d ; THE SEALED COPIES %s ; TOOLS CARRIED %d.**' % (
        len(REPAIRS), 'AGREE' if all(s == now for _a, _b, now, s, _n in rows) else '### DIFFER', len(rows))]
    put_txt('b682_tool_repairs.txt', L)
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


ROOT_EXCLUDE = re.compile(r'^b682_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*)\.?(txt|json|md|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b682_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(K.SHARED_APPENDED))


def rootbanks(*a):
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['b682 -- G-ROOT-BANKS-COMMITTED`S READING: THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ;'
         ' carried by HEAD ; HEAD`s blob equal to the file' % utc(), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('b682_root_banks.txt', L)
    put_json('b682_root_banks.json', dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b682_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### G-ROOT-BANKS-COMMITTED: A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b682'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b682_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='b682_ra_') as tmp:
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
    L = ['b682 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b682_root_arm.txt', L)
    put_json('b682_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b682 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b682_table_final.txt', L)
    put_json('b682_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b682_registration_2026-10-18.txt'
FACE = os.path.join(D, 'b682_registration_2026-10-18.txt')


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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b682_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b682_regspec.py')], 'b682_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b682_satisfiable.json', '--emit', 'b682'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b682_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b682_census_stepzero.txt'), ('b327_faces_census.py', 'b682_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b682_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b682'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b682_reg_gate.txt', 'data/b682_reg_termscan.txt', 'data/b682_regspec_run.txt', 'data/audit_b682_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES: (N1)-(N5) OF THE FERRY, THE SEAT'S (S1)-(S3)
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b681_closing_push_out.txt', 'b670_work_orders.txt')
N5_RELAY_TOOLS = ('correspondence_gen.py', 'test_correspondence_gen.py')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md', K.FOUNDATIONS)
VL = re.compile(r'### ### \*\*(.*?)\*\*')
GEN_COMMIT, TEST_COMMIT, DIFF_COMMIT, NAMING_COMMIT = '60e8de3e', 'e86b327b', '68d61764', '3940e8f1'
CELLS_COMMIT = 'f3bbe06'


def TRAIL_HEAD():
    return ('### b682 — lane two, act one hundred and nine, the re-cut act under (R292): the Correspondence reader over the runner print banks, '
            'the five cells regenerated, SIDE-bijection’s docstrings re-cut')


def _calls():
    return jl('b682_author_answers.json').get('calls') or []


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', 'FINDINGS.md', 'OPEN_TRAILS.md')
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _git_ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t.isdigit() else None


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s[:19] + 'Z', '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def _n1():
    cm = jl('b682_commands.json')
    ok = bool(cm) and not cm.get('local_lean')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches %d, each a hosted run (relay data/b682_commands.txt, %d '
        'commands read)' % (cm.get('local_lean') if cm else '### UNREAD', len(cm.get('dispatches') or []), len(cm.get('rows') or [])))


def _n2():
    gt = rdn('b682_gen_test.txt')
    t_test, t_diff, t_cells = _git_ct(RELAY, TEST_COMMIT), _git_ct(RELAY, DIFF_COMMIT), _git_ct(PP, CELLS_COMMIT)
    calls = _calls()
    t_prompt = _iso(calls[1]['ts']) if len(calls) > 1 else None
    ok = 'PLANTED CASES 5 ; AS WANTED 5 ; PASS' in gt and all(x for x in (t_test, t_diff, t_cells, t_prompt)) and t_test < t_cells \
        and t_diff < t_prompt < t_cells
    return ('HELD' if ok else 'REFUTED'), (
        'the five planted cases printed with their expected and read cells (relay data/b682_gen_test.txt, committed %s) before the first roster '
        'write (PLACE-papers %s); the dry run`s diff banked (relay %s) and raised as the prompt of (R292)(3) before that write: %s' % (
            TEST_COMMIT, CELLS_COMMIT, DIFF_COMMIT, bool(ok)))


def _n3():
    run_ = jl('b682_correspondence_run.json')
    ch = []
    for t_ in run_.get('tables') or []:
        if isinstance(t_.get('changes'), list):
            ch += t_['changes']
    d = g(PP, 'show', '--unified=0', '--format=', CELLS_COMMIT)
    files = sorted(set(x for x in g(PP, 'show', '--name-only', '--format=', CELLS_COMMIT).split(NL) if x.strip()))
    plus = [l for l in d.split(NL) if l.startswith('+') and not l.startswith('+++')]
    b, a = jl('b682_correspondence_before.json'), jl('b682_correspondence_after.json')
    ok = len(ch) == 5 and files == [K.FOUNDATIONS] and len(plus) == 3 and all(c['line'] in K.FIVE for c in ch) \
        and a.get('behind') is not None and a['behind'] <= b.get('behind', -1) and a.get('claim') is not None and a['claim'] <= b.get('claim', -1)
    return ('HELD' if ok else 'REFUTED'), (
        'the generator`s run bank names %d cells changed, every one at FOUNDATIONS :628-:630; the roster commit (PLACE-papers %s) touches %s, its '
        'lines the three rows those cells sit in; no cell by hand; the distance %s -> %s by b670`s method and %s -> %s at the generator`s claim '
        '(the five clauses carry no backticked commit, so that method does not count them)' % (
            len(ch), CELLS_COMMIT, files, b.get('behind'), a.get('behind'), b.get('claim'), a.get('claim')))


def _n4():
    t_name, t_wf = _git_ct(RELAY, NAMING_COMMIT), _git_ct(K.TD, K.T_WORKFLOW)
    pc, cd = rdn('b682_prints_compare.txt'), rdn('b682_cut_diff.txt')
    ok = 'NAMED SIDE-bijection' in rdn('b682_naming.txt') and t_name and t_wf and t_name < t_wf and 'DIFFERING 0 ; EQUAL LINE FOR LINE True' in pc \
        and 'COMMENT AND DOCSTRING LINES ALONE True' in cd
    return ('HELD' if ok else 'REFUTED'), (
        'the order`s line, the rule row and the table rows printed from their banks (relay data/b682_naming.txt, committed %s) before the kernel`s '
        'first write (%s); "%s"; "%s"' % (NAMING_COMMIT, K.T_WORKFLOW, (VL.findall(pc) or ['### UNREAD'])[-1], (VL.findall(cd) or ['### UNREAD'])[-1]))


def _n5():
    face = jl('b682_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    kw = sorted(set(x for x in g(K.TD, 'diff', '--name-only', K.T_PRE_MAIN, 'main').split(NL) if x.strip()))
    wf = _show(K.TD, 'main', '.github/workflows/build-module.yml') or ''
    ident = [w for w in ('psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008') if w in wf.lower()]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b682_|audit_b682_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA)
                                                or (x.startswith('tools/') and x[6:] in N5_RELAY_TOOLS))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import importlib
    argv, sys.argv = sys.argv, sys.argv[:1]
    try:
        CH = importlib.import_module('b682_checks')
    finally:
        sys.argv = argv
    new_arms = sorted(set(a_[0] for a_ in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = k_ok and kw == ['.github/workflows/build-module.yml', 'SIDEBijection/Theorem.lean', 'print_targets.txt'] and not ident \
        and not pp_beyond and not kinds_beyond and not differ and not new_arms and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it %s, SIDE-bijection`s main '
            'written only by its workflow, print list and docstring merge, tagged v0.2.1 (files since %s: %s); author identifiers in the workflow '
            'file: %s; PLACE-papers beyond FINDINGS, OPEN_TRAILS and FOUNDATIONS v0_2_5: %s; standing arms added: %s (the act`s arms over its own '
            'banks %d); sealed tools not agreeing %s; relay files of a kind beyond the act`s banks and tools, the generator and its test, the '
            'table, the root list, b681`s push-out bank and the orders bank`s rows: %s; "patent" in the lines written: %s; outbound requests: the '
            'seat`s git reads and pushes and the runner`s dispatches and reads at github.com, no identifier of the author placed in a request; the '
            'mirror zip outside every repository' % (K.DRAFT, k_ok, K.T_PRE_MAIN, kw, ident or 'NONE', pp_beyond or 'NONE', new_arms or 'NONE',
                                                     len(K.ACT_ARMS), differ or 'NONE', kinds_beyond or 'NONE', pat or 'NONE'))


def scores(*a):
    TF, RA = jl('b682_table_final.json'), jl('b682_root_arm.json')
    _r, _n, sh = seal_hashes()
    S = {
        'N1': _n1(), 'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:700]))
    if 'dry' in a:
        return
    put_json('b682_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _title():
    return ('## The Correspondence reader over the runner print banks: 5 cells changed, the 5 at FOUNDATIONS :628–:630 read; distance 55 against '
            '55 by b670’s method, 0 against 0 by the generator’s; SIDE-bijection’s docstrings re-cut: 4 rows outside LICENSED/CITED to 0, v0.2.1')


def _finding_text():
    S, J = jl('b682_scores.json'), jl('b682_act_root.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b682_author_answers.txt'), re.M))
    c1 = _rl_lines('b682_record_lines.json') + ['?']
    cw = _rl_lines('b682_record_lines_word.json') + ['?']
    c3 = _rl_lines('b682_record_lines_c3.json') + ['?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    e = ['', _title(), '',
         'The generator that writes the papers’ Correspondence cells now reads the runner print banks the re-cut acts bank, so the five cells at '
         'FOUNDATIONS :628–:630 that read “NO PRINT BANK” now carry SIDE-silence-principle v0.2.1 and, where the bank prints the declaration, its '
         'profile “axiom-free (none)”; and SIDE-bijection’s four overreaching docstrings are re-cut to their licensed readings, its prints equal '
         'line for line before and after, merged and tagged v0.2.1. Nothing here proves RH or GRH.', '',
         '*Filed at b682 on the author’s ruling `(R292)`%s. Banks: relay `data/b682_gen_test.txt`, `data/b682_correspondence_diff.txt`, '
         '`data/b682_correspondence_run.txt`, `data/b682_correspondence_before.txt`, `data/b682_correspondence_after.txt`, `data/b682_naming.txt`, '
         '`data/b682_cut.txt`, `data/b682_act_root.txt`; the tool `tools/correspondence_gen.py`.*' % (
             (' and the navigator’s answers (%d questions)' % n_ans) if n_ans else ''), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed -- the ruling’s “13 roster files” against '
         'the roster’s 20 tables, raised and answered. b681 at its weight (FINDINGS :%s).' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', c1[0]), '',
         '**The reader** (`(R292)`(3)): relay tools/correspondence_gen.py given the runner print banks’ path form -- the axioms bank beside its '
         'runner bank, the built commit read from the runner bank’s header -- in one commit alone; five planted cases as wanted, the fifth a '
         'declaration absent at a tag where a print bank stands, reading ABSENT; the dry run’s diff, 5 cells, raised before any write.', '',
         '**The cells** (`(R292)`(4)): written by the generator alone into FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md; the distance 55 and 0 '
         'before and after, beside b680’s 55 and 0; `W-ORD-CORRESPONDENCE-RUNNER-BANKS` DISCHARGED (OPEN_TRAILS :%s); the partner copy’s '
         'differing table carried under `W-ORD-ONE-COPY`.' % c3[0], '',
         '**The next document** (`(R292)`(5)): SIDE-bijection’s docstrings, 4 standing and alone at the top of the count; the workflow and the '
         'print list each committed alone on its main, the ‘before’ print bank at main, the cut on recut-bijection-b682, the ‘after’ print bank '
         'at its tip, 15 prints equal line for line, merged with the merged tree the built tree, tagged v0.2.1; the distance 4 to 0.', '',
         '**The author’s word** on the rules without arms banked at once (OPEN_TRAILS :%s): the seat sorts the 24 for b683’s ruling.' % cw[0], '',
         '**The root.** b682 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b678’s carried cells and b674–b678’s runner banks through the '
         'generator, and is re-read by the next re-cut act. It strengthens the programme’s offerings of a Correspondence table written by a tool '
         'from the banks the runs leave, and of kernel docstrings that say what their declarations compile.', '',
         '**Carried to:** the map in the angle form over the narrowed balls (`W-ORD-MAP-ANGLE-FORM`, b683’s candidate); `W-ORD-EPSTEIN-COUNT`; the '
         '24 rules without arms, sorted for the author; the re-cut residues of b674, b676 and b678; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the runner print bank read as the re-cut acts bank it, the axioms bank beside its runner bank, an act’s after bank before its '
              'before; (2) a declaration declared at the tag and not printed keeps b672’s NOT PRINTED, and ABSENT stays the word for a declaration '
              'absent at the tag; (3) the run’s diff banks under their own stem, so b672’s banks stand as they are; (4) SIDE-bijection’s print '
              'list every declaration of its one module, 15 names')


def _trail_text():
    S, J = jl('b682_scores.json'), jl('b682_act_root.json')
    fj = jl('b682_findings.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b682_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b682_record_lines.json') + ['?']
    cw = _rl_lines('b682_record_lines_word.json') + ['?']
    c3 = _rl_lines('b682_record_lines_c3.json') + ['?']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R292) ratified.** (1) b681 at its weight. (2) The object. (3) The reader. (4) The cells. (5) The licensed table’s next document. '
             '(6) The branches. (7) The read-first bank. (8) The draft held at v5. (9) The act after.', '',
             '**Entered:** FINDINGS.md:%s (b681’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the author’s word on the rules without arms), :%s '
             '(`W-ORD-CORRESPONDENCE-RUNNER-BANKS` DISCHARGED); PLACE-papers FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md :628-:630 (the five cells, '
             'by the generator); SIDE-bijection v0.2.1; this record.' % (c1[0], fj.get('entry_line'), cw[0], c3[0]), '',
             '**Act root:** b682 `%s` (previous `%s`, b681’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d call%s (relay data/b682_author_answers.txt); none after the root.' % (
                 n_ans, len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The cells:** 5 written by the generator, the five of FOUNDATIONS :628-:630 (relay data/b682_correspondence_run.txt); the distance '
             '55 and 0 before and after (relay data/b682_correspondence_before.txt, data/b682_correspondence_after.txt).', '',
             '**The cut:** SIDE-bijection’s docstrings, 4 rows to 0, the prints equal 15 = 15, merged b800504, tag v0.2.1 (relay data/b682_cut.txt).', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b682_closing.txt).', '',
             '**The open orders:** `W-ORD-MAP-ANGLE-FORM` (b683, on the author’s placement); `W-ORD-EPSTEIN-COUNT` (the alternative); '
             '`W-ORD-LEDGER-SPLIT-RESOLVER` (on the author’s word); `W-ORD-CHAIN-PAGE-B638-CASES`; `W-ORD-PRINT-TARGETS`; `W-ORD-ONE-COPY`; '
             '`W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; `W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; `W-ORD-ROOT-BINARY-BANK`.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b682_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.**', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b682_scores.json')
    L = ['=' * 104, 'b682 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b682_defects.txt').rstrip(NL).split(NL)
    put_txt('b682_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b682_scores.json', 'b682_findings.json', 'b682_trail.json', 'b682_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b682_record_lines.json') + ['?']
    c3 = _rl_lines('b682_record_lines_c3.json') + ['?']
    L = ['b682 -- THE COMPONENTS, BANKED UNDER (R292).', '',
         '### COMPONENT 0 : the citation check (data/b682_citation_check.txt), step zero (data/b682_ferry.txt, data/b682_readfirst.txt, '
         'data/b682_stepzero.txt, data/b682_tests_stepzero.txt, data/b682_rowgen_stepzero.txt, data/b682_branches.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b681`s weight FINDINGS :%s' % c1[0],
         '### COMPONENT 2 : the reader (tools/correspondence_gen.py at %s alone), the five cases (data/b682_gen_test.txt), the diff '
         '(data/b682_correspondence_diff.txt), one prompt ; N2 %s' % (GEN_COMMIT, S['N2'][0]),
         '### COMPONENT 3 : the cells (data/b682_correspondence_run.txt), the distance (data/b682_correspondence_before.txt, _after.txt), the order '
         'DISCHARGED OPEN_TRAILS :%s ; N3 %s' % (c3[0], S['N3'][0]),
         '### COMPONENT 4 : the naming (data/b682_naming.txt), the cut (data/b682_cut.txt, data/b682_cut_diff.txt), the runs, the prints ; N4 %s' % S['N4'][0],
         '### COMPONENT 5 : the carry-time reading (data/b682_tool_repairs.txt), the dry-run steps (data/b682_reg_gate.txt), the seal '
         '(data/b682_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N5'][0])]
    put_txt('b682_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b682_findings.json', dict(title=t))
    j = jl('b682_findings.json')
    j['entry_line'] = ln
    put_json('b682_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b682_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written -- converted by conv and run through the screens their landing runs, the needles the face names read in
    each; prints DRY-RUN STEP : CLEAN and exits 0 only when both screens are quiet and every needle is found. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
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


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b681's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '2026-10-18-b682'
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
    put_json('b682_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b682':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b682`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b682_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b682_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b682_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b682 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b682 (the last export b681`s, D:/MY-DOwnloads/mirror-refresh-2026-10-18-b681.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b682_mirror.txt', L)
    put_json('b682_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'answers': answers, 'gendry': gendry, 'word': word, 'dist': dist, 'partner': partner,
          'c3': c3, 'naming': naming, 'runner': runner, 'prints': prints, 'cutdiff': cutdiff,
          'mbuild': mbuild, 'mroot': mroot, 'mverify': mverify, 'mbank': mbank,
          'commands': commands, 'kernels': kernels, 'defects': defects, 'repairs': repairs,
          'rootbanks': rootbanks, 'root': root, 'root_arm': root_arm, 'table_final': table_final, 'gatebanks': gatebanks, 'scores': scores,
          'desk': desk, 'components': components, 'findings': findings, 'trail': trail, 'drycheck': drycheck}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b682_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
