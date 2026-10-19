# -*- coding: utf-8 -*-
"""b690_record.py -- THE ACT'S RECORD TOOL, b690 under (R300).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b690's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b689_record.py in stages: the helpers, the guarded landing, the readers, step zero's rowgen and branches
### routes, Component 1's weight line and the answers route first; the late routes at Component 4. Every python child is started as
### `python -X utf8`, no environment mapping passed. Routes: `python tools/b690_record.py <route> [dry]`. After the seal this tool's own print
### is how the entry, the dry entry and the trail are read (data/b690_rules.txt row (1), kept ahead of its binding).
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
import b690_worklist as K          # noqa: E402

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
        'b690_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b690_findings.json': dict(entry_line=99999, title='stand-in'),
        'b690_trail.json': dict(line=99999),
        'b690_act_root.json': dict(root='0' * 64, previous='7b2d6772' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b690's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b690_scanfile_%s.md' % tag)
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
    """a row of data/b690_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


P3_STATES = ('STATED', 'DERIVED', 'NAMED')


def read_p3_row(r):
    """a row of data/b690_r3_p3.json: the repository, the file, the line (an int), the wording (non-empty) and the reading (one of P3_STATES);
    returns (file, line, reading)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('file') or not isinstance(r.get('line'), int) or not (r.get('text') or '').strip() \
            or r.get('reading') not in P3_STATES:
        raise ValueError('P3 row of another shape: %r' % (str(r)[:120],))
    return r['file'], r['line'], r['reading']


READERS = ['read_score_row', 'read_head', 'read_branch_row', 'read_p3_row']


# ================================================================================ STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE (b670's route, carried)
def roster():
    """the 19 roster tables of data/b586_corroboration.txt :34, at the paths that bank read (carried from b670_record.py :548-:552)."""
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b690_rowgen_<stage>.txt."""
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
    L = ['b690 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b690_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R300)(6))
def branches(*a):
    """every branch (R300)(6) names, its tip read before any delete, its fate; the one remote branch the ruling names (SIDE-explicit-formula's
    strip-free-b689) read by its remote-tracking ref and listed by `git branch -r --merged main`; any branch of b689 that --merged lists and the
    ruling does not name, reported and KEPT. data/b690_branches.txt (.json)."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    for repo, b in K.DELETE_REMOTE:
        tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/remotes/origin/' + b).strip()
        rem = (g(repo, 'ls-remote', 'origin', 'refs/heads/' + b).split() or [''])[0]
        merged = ('origin/' + b) in g(repo, 'branch', '-r', '--merged', 'main', '--list', 'origin/' + b)
        rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=merged and rem == tip, fate='DELETED', remote_read=rem))
    named = set((r['repo'], r['branch']) for r in rows)
    extra = []
    for repo, _bs in K.DELETE:
        for x in g(repo, 'branch', '--merged', 'main', '--format=%(refname:short)').split(NL):
            x = x.strip()
            if (x.startswith('push-b689') or x.endswith('-b689')) and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b690 -- STEP ZERO, (R300)(6): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; listed by `git branch [-r] --merged main --list <name>` ; fate. Deleted',
         '### by name in the house form, each delete command naming one branch with no glob in any half, one command per message, in sequence; no',
         '### branch the ruling does not name. The remote row`s tip is the remote-tracking ref, read against one ls-remote of that branch.']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s%s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                                 r['fate'], (' ; at the remote %s' % r['remote_read']) if r['where'] == 'remote' else '')
          for r in rows]
    L += ['', '### branches of b689 that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; TO BE DELETED %d ; UNNAMED OF b689 %d.**' % (
        len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), len(rows), len(extra))]
    put_txt('b690_branches.txt', L)
    put_json('b690_branches.json', dict(at=utc(), rows=rows, extra=[list(x) for x in extra]))
    print(NL.join(L[6:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R300)(1)
WH = ('*Appended 2026-10-19 by b690 to b689’s entry (:9348), under `(R300)`(1) -- b689 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b689_closing.txt), ITS UNDECLARED POST-SEAL FAILURE ENTERED BY A GENERATED CORRIGENDUM:*')
WB = (' “b689 closed: relay c975b150, PLACE-papers a5b86a5; suite 115 of 116; root 7b2d6772a03792f6…; 2 prompts answered; 5 defects” '
      '(data/b689_closing.txt :1), the closing pushed and read back at relay c8afcb43 (data/b689_closing_push_out.txt). '
      'Wide.li_nonneg_cfg_imp_online_ne_zero on WideConfig, HCount Z A₀ and ∀ ρ ∈ Z.carrier, ρ ≠ 0, HExcl’s half on (−1/2, 0) dropped and the '
      'dominant set split at w = 1 with at most one point by injectivity; section 11 committed alone before any plan row; the 22 strip uses '
      'classified 13 DISCHARGED, 9 RE-PROVED, 0 OBSTRUCTED; the plan raised before any Lean file existed and answered “run as written”; one tree '
      'state and one dispatch (run 39255737373, its artifact’s sha256 agreeing); 11 new names at the standard three, v0.33’s 49 terminals '
      'printing the same by name; no sorry on main; merged --no-ff at 8fbc27b on the gate’s reading, the merged tree the built tree, v0.34 peeled '
      'and read back (data/b689_landing.txt, data/b689_merge_push_out.txt). The grade INTERFACES on the named premise Wide.HCount, read from the '
      'statement before the merge, the E0 rule agreeing as the check with its lexicon extended in that act’s tool alone, the salt-check passing '
      '(data/b689_grade.txt). The controls from the runner’s print: C2 {−1/4, 5/4}, excluded by v0.33, meeting ρ ≠ 0 with its dominant point at '
      'w = 1 and λ₁ < 0; C3 recording the real segment admitted; C2b {0, 1} failing ρ ≠ 0 at 0, b679’s lesson living in that hypothesis. 8 of 8 '
      'constant rows equal to v0.33’s, n*’ = 63676 (data/b689_constants.txt); Q0 meeting ρ ≠ 0 on Z_Q(0) = −1 alone, the faces page untouched and '
      'its successor row drafted and held (data/b689_q0_reread.txt, data/b689_faces_rows.txt); the corrigendum for b688’s (f) at FINDINGS :9342 '
      'in b678’s form, the corrigenda bank at row (3); the head-line arm in the whitespace-removal form reading b688 OK and b689 OK, rule_arms.py '
      'sealed with the act and its hash agreeing at the close. All eight scores HELD; mirror-refresh-2026-10-19-b689.zip CLEAN with the root '
      'line. Five defects (data/b689_defects.txt): (a) seven redirects onto /dev/null in six commands; (b) readfirst line numbers written before '
      'the lines were read, corrected; (c) the navigator’s, b688’s ferry breaking the head-line quote after a hyphen; (d) the sealed title’s '
      'needle against the bank’s wording, repaired by banking the arm route’s verdict verbatim; (e) one sed read of the dry entry after the seal, '
      'G-EDIT-ROUTE failing pre-push and post-push with the face locked and the failure undeclared -- entered at b690 by the generated '
      'corrigendum that follows; three carry faults caught by the pre-run and repaired before the lock. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b690_record_lines.json', 'c1', entry=K.B689_ENTRY,
         check=[('FINDINGS.md', K.B689_ENTRY, '## SIDE-explicit-formula strip-free Li converse'), ('OPEN_TRAILS.md', K.B689_TRAIL, '### b689')], dry=dry)


# ================================================================================ THE ANSWERS BANK (b689's route, carried)
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
    """data/b690_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
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
    head = ['### b690 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b690_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b690_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 2: THE FACES LINE, (R300)(3) AND THE AUTHOR'S WORD (b688's route, carried)
def faces(*a):
    """b688's form (tools/b688_record.py :322-:366): the control (b688's list re-emits the committed page byte for byte) and the emission of
    data/b690_nodes_zeta.txt, both by tools/chain_page.py --from-output data/b643_probe_out_zeta.txt into the scratchpad (no lean); the diff
    printed; with `write`, the control and the emission clean first, the page written by the generator itself (its --out the page), read
    back equal to the emission, and the diff banked as data/b690_faces_diff.txt."""
    import difflib
    import hashlib
    page = os.path.join(PP, K.FACES_PAGE)
    probe = os.path.join(ROOT, *K.PROBE.split('/'))

    def emit(nodes, out):
        r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'chain_page.py'), '--nodes', os.path.join(ROOT, *nodes.split('/')),
                            '--probe-dir', SP, '--out', out, '--from-output', probe], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.returncode, ((r.stdout or '') + (r.stderr or '')).strip().split(NL)[-1:]
    committed = open(page, 'rb').read()
    head = g(PP, 'show', 'HEAD:' + K.FACES_PAGE).encode('utf-8')
    cpath, npath = os.path.join(SP, 'b690_faces_control.md'), os.path.join(SP, 'b690_faces_emit.md')
    rc0, t0 = emit(K.NODES, cpath)
    ctl = open(cpath, 'rb').read() if os.path.exists(cpath) else b''
    control = rc0 == 0 and ctl == committed
    rc1, t1 = emit(K.NODES_NEW, npath)
    new = open(npath, 'rb').read() if os.path.exists(npath) else b''
    d = list(difflib.unified_diff(committed.decode('utf-8').split(NL), new.decode('utf-8').split(NL), 'committed', 'b690', n=0, lineterm=''))
    add = sum(1 for l in d if l.startswith('+') and not l.startswith('+++'))
    rem = sum(1 for l in d if l.startswith('-') and not l.startswith('---'))
    # ### beside b688's count, the lines that differ with difflib's autojunk off (a line as common as the blank one is junk to the default
    # ### matcher, which then reports an equal blank line inside a hunk)
    ca, cb = committed.decode('utf-8').split(NL), new.decode('utf-8').split(NL)
    real = [(i1 + 1, i2, j1 + 1, j2) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ca, cb, autojunk=False).get_opcodes() if op != 'equal']
    written, back = False, False
    if 'write' in a:
        if not control or rc1 != 0:
            sys.exit('### THE CONTROL OR THE EMISSION FAILED -- THE PAGE IS NOT WRITTEN')
        rc2, t2 = emit(K.NODES_NEW, page)
        written = rc2 == 0
        back = open(page, 'rb').read() == new
    old_l = rdn(os.path.basename(K.NODES)).split(NL)
    new_l = rdn(os.path.basename(K.NODES_NEW)).split(NL)
    only = [i + 1 for i in range(max(len(old_l), len(new_l))) if (old_l[i:i + 1] or [None]) != (new_l[i:i + 1] or [None])]
    row = new_l[K.NODES_ROW - 1]
    L = ['b690 -- COMPONENT 2, (R300)(3): THE FACES LINE THROUGH THE GENERATOR, ON THE AUTHOR`S WORD (%s)' % utc(), '',
         '### the generator: relay tools/chain_page.py --from-output relay %s (no elaboration; no lean on this host)' % K.PROBE,
         '### the control: b688`s list (relay %s) re-emits the committed page byte for byte: %s (%d bytes ; exit %d ; the committed page equal to HEAD`s '
         'blob %s)' % (K.NODES, control, len(ctl), rc0, committed.replace(b'\r\n', b'\n') == head.replace(b'\r\n', b'\n')),
         '### the new list: relay %s (b688`s %d lines, the lines differing %s -- :%d replaced by the amended row of data/b689_faces_rows.txt, every '
         'other line unchanged); emitted %d bytes, exit %d, sha256 %s' % (K.NODES_NEW, len(old_l) - 1, only, K.NODES_ROW, len(new), rc1,
                                                                       hashlib.sha256(new).hexdigest()[:16]),
         '### the diff, committed page -> b690 emission (lines added %d, removed %d, by b688`s count; with difflib`s autojunk off the lines that '
         'differ, committed -> b690: %s):' % (add, rem, '; '.join(':%d-:%d -> :%d-:%d' % r for r in real))] + ['    ' + l for l in d] + [
         '', '### the page written by the generator and read back equal to the emission: %s' % (back if 'write' in a else 'NOT YET (dry)'),
         '### the row carries "(b689)" after the strip-free phrase, T-COUNT beside P3 and no backtick: %s' % (
             'unchanged under the strip-free form (b689))' in row and 'T-COUNT (P3) derived' in row and '`' not in row), '',
         '### ### **CONTROL EQUAL %s ; LINES ADDED %d ; REMOVED %d ; PAGE WRITTEN %s.**' % (control, add, rem, written and back)]
    if 'write' in a:
        put_txt('b690_faces_diff.txt', L)
    print(NL.join(L[2:6] + L[-4:]))


# ================================================================================ COMPONENT 3: THE ORDER, (R300)(4) (b688's route, carried)
OH = ('*Appended 2026-10-19 by b690 beneath b689’s trail record (:14952), under `(R300)`(4) -- `W-ORD-CIRCUIT-READING` ENTERED:*')
OB = (' the dependency-circuit reading, an instrument on the author’s word, specified at b690 (relay data/b690_circuit_spec.txt): for a kernel at '
      'a tag, each declaration’s transitive constant closure emitted by a runner step from the kernel’s environment (INPUT, a gz beside a text '
      'hashes bank), read as SERIES, TERMINALS, SHORTS, WIDTH, LOAD and CLAUSE-DOMINANCE -- the last across the faces kernels, whether the '
      'clause’s compiled face lies in the closure of each main theorem -- with READFIRST-CLOSURE on the author’s word at b690’s faces prompt '
      '(a ruling and ferry text in place of a theorem, its cited banks closed transitively, output as a readfirst bank), and OUTPUT a DOT bank '
      'rendered to PNG beside its hashes bank. No tool, Lean file or runner step written at b690; the INSTRUMENTS page unedited until the build '
      'act. Trigger: the research act after b691. Status OPEN.')


def order(*a):
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', OH, NL + OH + OB + NL)], 'b690_orders_lines.json', 'order', entry=K.B689_TRAIL,
         check=[('OPEN_TRAILS.md', K.B689_TRAIL, '### b689 — lane two')], dry=dry)


# ================================================================================ THE COMMAND BANK (b689's route, carried; the previous act in this same session)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402

SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
PREV_ACT, PREV_ANCHOR = 'b689', 'RULING (R299) BEGIN'


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


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    bg = _bg_calls()
    for i, r in enumerate(rows):
        r['n'] = i + 1
        r['bg'] = (r.get('ts'), r.get('cmd')) in bg
    return rows


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


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')
SED = re.compile(r'(^|[;&|(]\s*|\s)sed\s')
PY_PRINT_READ = re.compile(r'python[^\n]*\s-c\s')


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def sed_cmd(cmd):
    """data/b685_rules.txt row (2): a command carrying sed in any form, read outside quoted strings."""
    return SED.search(QUOTED.sub('""', cmd)) is not None


SED_KIND = 'R sed in any form (data/b685_rules.txt row (2))'


def prev_capture():
    """G-EDIT-ROUTE's window over the previous act (b687's repair; b690's reading, the same session): b689's capture AFTER ITS POST-PUSH
    SUITE -- every command of this session from the call that combined b689's post-push parts into data/b689_checks_postpush.txt to the
    first user line of (R300), b689's closing's commands among them; this act's own capture starts at that line."""
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
    """the arm's offences (b687's repair, carried): tools/edit_route.py's arms (unchanged) and sed in any form, read outside quoted strings."""
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
    """(R300)(6): a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    return names, [ch for ch in '*?[' if ch in c]


IDENT = ('psinary', 'hotmail', 'seale', 'york', 'orcid', '0009-0008')


def outbound():
    """the act's outbound requests other than git: every WebSearch query, WebFetch URL and subagent prompt from the ruling's line on."""
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
    disp = [r for r in sh_ if re.search(r'(^|&&\s*|;\s*)gh workflow run\b', QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in sh_ if (r.get('bg') or re.search(r'Start-Process|\bnohup\b|run_in_background', QUOTED.sub('""', r['cmd'])))]
    seds = [r for r in sh_ if sed_cmd(r['cmd'])]
    nulls = [r for r in sh_ if REDIRECT_NULL.search(QUOTED.sub('""', r['cmd']))]
    pyreads = [r for r in sh_ if PY_PRINT_READ.search(r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    ob = outbound()
    L = ['b690 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (b689, this same session %s, from its post-push combine to (R300)`s line): %d '
              'commands from %s, its offences printed whole (%d):' % (K.SESSION_ID[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (%d):' % len(disp)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN, BY THEIR TEXT OR THE TOOL`S run_in_background PARAMETER (%d):' % len(
        detach)] + (['  #%d %s%s' % (r['n'], '[run_in_background] ' if r.get('bg') else '', r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING sed IN ANY FORM (data/b685_rules.txt row (2)) (%d):' % len(seds)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in seds] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT ONTO /dev/null, read outside quoted strings (%d):' % len(nulls)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], r['cmd'].split(NL)[0][:200]) for r in nulls] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT RUN AN INTERPRETER`S ONE-LINE PROGRAM (python -c), each its first line -- the reads among them entered as this',
              'act`s defect (a) where the Read tool would have read the lines (%d):' % len(pyreads)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:220]) for r in pyreads] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R300)(6): one branch per command, no glob in any half): ' + ('; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git (web searches, subagent prompts and fetches), each with the author`s identifiers found in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; REDIRECTS ONTO /dev/null %d ; '
              'ONE-LINE PROGRAMS %d ; MOVE OR DELETE COMMANDS %d ; BRANCH DELETES OF ONE BRANCH AND NO GLOB %d OF %d ; OUTBOUND REQUESTS %d, AN '
              'IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(nulls), len(pyreads), len(mv),
                  sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl), len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    put_txt('b690_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b690_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        prev=dict(act=PREV_ACT, session=K.SESSION_ID, rows=len(prev),
                                                  offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                        seds=[r['n'] for r in seds], null_redirects=[r['n'] for r in nulls], py_programs=[r['n'] for r in pyreads],
                                        moves_deletes=[r['n'] for r in mv],
                                        delete_shapes=[dict(n=n, deletes=d, globs=gl) for n, d, gl in shapes], outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r, o in phits:
        print('  PREVIOUS-ACT OFFENCE #%s %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b690_defects.txt').split(NL)
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
    t = rdn('b690_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b690_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


# ================================================================================ THE LATE ROUTES (b689's, carried with b690's names)
def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle', 'SIDE-bijection', 'SIDE-class-number-anomaly',
                                   'SIDE-spinor', 'SIDE-li-map']


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    put_json('b690_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (no kernel written in this act; none written after this read)' % len(ks))


def seal_hashes():
    import hashlib
    rec_ = jl('b690_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b690_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


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


ROOT_EXCLUDE = re.compile(r'^b690_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*)\.?(txt|json|md|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b690_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(K.SHARED_APPENDED))


def rootbanks(*a):
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['b690 -- G-ROOT-BANKS-COMMITTED`S READING: THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ;'
         ' carried by HEAD ; HEAD`s blob equal to the file' % utc(), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('b690_root_banks.txt', L)
    put_json('b690_root_banks.json', dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b690_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### G-ROOT-BANKS-COMMITTED: A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b690'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b690_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='b690_ra_') as tmp:
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
    L = ['b690 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b690_root_arm.txt', L)
    put_json('b690_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b690 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(ROOT, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b690_table_final.txt', L)
    put_json('b690_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


# ================================================================================ THE PER-ARM SECONDS, (R300)(3) AND THE FERRY'S COMPONENT 4
def armsecs(*a):
    """the standing arms' seconds at HEAD, from the pre-run's four parts (tools/b690_checks.py clocks each arm's three readings -- LIVE, NEG,
    POS -- beside its part's shared phases): data/b690_arm_seconds.txt (.json), rows are standing arms by part, slowest first; the three
    slowest named; the part's phases beside, since the sources an arm reads are built once per part and not per arm."""
    import b689_worklist as K689
    st = sorted(set(_g2_of(os.path.join(D, 'b689_registration_2026-10-19.txt'))) - set(K689.ACT_ARMS))
    rows, phases = [], {}
    for p in K.PARTS:
        j = jl('b690_arm_seconds_%s.json' % p)
        phases[p] = j.get('phases') or {}
        for nm, s in (j.get('arms') or {}).items():
            rows.append(dict(arm=nm, part=p, secs=s, standing=nm in st))
    srows = sorted([r for r in rows if r['standing']], key=lambda r: -r['secs'])
    miss = sorted(set(st) - set(r['arm'] for r in srows))
    L = ['b690 -- THE STANDING ARMS` SECONDS AT HEAD, BY PART, FROM THE PRE-RUN (%s): (R300)(3)`s reading, banked for the census' % utc(), '',
         '### the source: data/b690_arm_seconds_<part>.json, written by tools/b690_checks.py at its pre-run, each arm`s seconds the sum of its',
         '### three readings (LIVE on the sources, NEG on a copy, POS on a mutated copy); the part`s phases -- the sources built once for all its',
         '### arms -- printed beside, not divided among them. Rows are standing arms, slowest first:']
    L += ['  %-46s %-11s %8.3f s' % (r['arm'], r['part'], r['secs']) for r in srows]
    L += ['', '### THE PARTS` PHASES (seconds): ' + ' | '.join('%s: %s' % (p, '; '.join('%s %.0f' % kv for kv in ph.items())) for p, ph in phases.items()),
          '### the standing arms not clocked: %s' % (miss or 'NONE'),
          '', '### ### **STANDING ARMS CLOCKED %d OF %d ; THE THREE SLOWEST %s ; THEIR SECONDS SUMMED %.1f.**' % (
              len(srows), len(st), ', '.join('%s (%s, %.2f s)' % (r['arm'], r['part'], r['secs']) for r in srows[:3]) or 'NONE',
              sum(r['secs'] for r in srows))]
    put_txt('b690_arm_seconds.txt', L)
    put_json('b690_arm_seconds.json', dict(at=utc(), rows=srows, phases=phases, standing=len(st), clocked=len(srows), missing=miss,
                                           slowest=[r['arm'] for r in srows[:3]]))
    print(L[-1])


def _g2_of(path):
    t = rd(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


# ================================================================================ THE SCORES: (N1)-(N5) OF (R300)'S FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and not the entry; the entry reads the scorer's bank. `scores` writes
# ### data/b690_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there, the bank it waits on named, and
# ### is read at the close by `scores close` into data/b690_scores_close.json, which no ledger line reads.
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b689_closing_push_out.txt')
KERN = 'D:/SIDE-explicit-formula'


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


def _n1():
    cm = jl('b690_commands.json')
    ok = bool(cm) and not cm.get('local_lean') and not cm.get('dispatches')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches: %s (relay data/b690_commands.txt, %d commands read)' % (
            cm.get('local_lean') if cm else '### UNREAD', cm.get('dispatches') if cm else '### UNREAD', len(cm.get('rows') or [])))


R3_BANKS = ('licensed', 'corr', 'ceiling', 'orders', 'methods', 'lag', 'residues', 'rules', 'arms', 'p3', 'onecopy', 'pair')


def _readings_order():
    """N2's first clause: the twelve route banks and their tool committed (d23e0d1b) before the aggregate (2c0e2c28), each carrying its
    verdict line; the aggregate's rows naming their tool or the hand."""
    files = _files_of(ROOT, K.READINGS_COMMIT)
    want = ['data/b690_r3_%s.%s' % (n, x) for n in R3_BANKS for x in ('txt', 'json')] + ['tools/b690_readings.py']
    t1, t2 = _git_ct(ROOT, K.READINGS_COMMIT), _git_ct(ROOT, K.READING3_COMMIT)
    agg = _show(ROOT, K.READING3_COMMIT, 'data/b690_reading3.txt') or ''
    verdicts = all(re.search(r'^### ### \*\*', rdn('b690_r3_%s.txt' % n), re.M) for n in R3_BANKS)
    blocks = re.split(r'(?m)^(?=  \(\d+\) )', agg)[1:]
    rows = [b_ for b_ in blocks if re.search(r'\| (?:tool\b|by hand)', ' '.join(b_.split()))]
    return dict(all_banked=sorted(want) == sorted(f for f in files if f in want) and len(set(want) & set(files)) == len(want), before=bool(t1 and t2 and t1 < t2),
                verdicts=verdicts, rows=len(rows))


def _p3_state():
    j = jl('b690_r3_p3.json')
    hits = j.get('hits') or []
    t = rdn('b690_r3_p3.txt')
    ok_rows = True
    for h in hits:
        try:
            read_p3_row(h)
        except ValueError:
            ok_rows = False
    listed = all(('%s :%d [' % (h['file'], h['line'])) in t for h in hits)
    return dict(hits=len(hits), rows_read=ok_rows, listed=listed, outside=j.get('outside'), stated=j.get('stated'))


def _n2():
    o, p = _readings_order(), _p3_state()
    ok = o['all_banked'] and o['before'] and o['verdicts'] and o['rows'] >= 18 and p['rows_read'] and p['listed'] and p['hits'] > 0
    return ('HELD' if ok else 'REFUTED'), (
        'the twelve reading banks and tools/b690_readings.py committed at relay %s, every one present: %s, before the aggregate data/b690_reading3.txt '
        'at %s: %s; every route bank carrying its verdict line: %s; the aggregate`s rows naming their tool or the hand: %d; the P3 grep`s hits %d, '
        'each read by the record tool`s reader %s and listed by file and line with its wording %s (relay data/b690_r3_p3.txt)' % (
            K.READINGS_COMMIT, o['all_banked'], K.READING3_COMMIT, o['before'], o['verdicts'], o['rows'], p['hits'], p['rows_read'], p['listed']))


SPEC_ROWS = ('INPUT', 'SERIES', 'TERMINALS', 'SHORTS', 'WIDTH', 'LOAD', 'CLAUSE-DOMINANCE', 'READFIRST-CLOSURE', 'OUTPUT')


def _spec_state():
    t = rdn('b690_circuit_spec.txt').split(NL)
    rows = {}
    for i, l in enumerate(t):
        m = re.match(r'^  ([A-Z-]+)\s+reads: ', l)
        if m and m.group(1) in SPEC_ROWS:
            blk = []
            for x in t[i:]:
                if x is not l and re.match(r'^  [A-Z-]+\s+reads: ', x):
                    break
                if x.startswith('###'):
                    break
                blk.append(x)
            rows[m.group(1)] = ' '.join(blk)
    full = sorted(rows) == sorted(SPEC_ROWS) and all(('output: ' in v) for v in rows.values())
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    tool = [x for x in relay_ch if x.startswith('tools/') and 'circuit' in x.lower()]
    lean = [x for x in relay_ch if x.endswith('.lean')]
    return dict(rows=len(rows), full=full, alone=_files_of(ROOT, K.SPEC_COMMIT) == ['data/b690_circuit_spec.txt'], tool=tool, lean=lean)


def _n3():
    s = _spec_state()
    ok = s['full'] and s['alone'] and not s['tool'] and not s['lean']
    return ('HELD' if ok else 'REFUTED'), (
        'the circuit specification (relay data/b690_circuit_spec.txt) names for each of its %d rows -- INPUT, the seven readings, OUTPUT -- the '
        'object it reads and the form of its output: %s; committed alone at relay %s: %s; a tool written for it: %s; a Lean file written in the '
        'act: %s' % (s['rows'], s['full'], K.SPEC_COMMIT, s['alone'], s['tool'] or 'NONE', s['lean'] or 'NONE'))


def _kernels_moved():
    """every kernel's main and tags against the act's start, (R300)'s line: commits on main after it, tags created after it."""
    t0 = _iso_epoch(_anchor_ts(K.ANCHOR) or '')
    moved = []
    for k in dict.fromkeys(_kerns()):
        p = 'D:/' + k
        ct = _git_ct(p, 'main')
        if ct and t0 and ct > t0:
            moved.append('%s main' % k)
        for l in g(p, 'for-each-ref', '--format=%(refname:short) %(creatordate:unix)', 'refs/tags').split(NL):
            x = l.split()
            if len(x) == 2 and x[1].isdigit() and t0 and int(x[1]) > t0:
                moved.append('%s tag %s' % (k, x[0]))
    return t0, moved


def _faces_state():
    import hashlib
    fd = rdn('b690_faces_diff.txt')
    page = g(PP, 'show', 'HEAD:' + K.FACES_PAGE)
    m = re.search(r'emitted (\d+) bytes, exit 0, sha256 ([0-9a-f]{16})', fd)
    sha = hashlib.sha256(page.encode('utf-8')).hexdigest()[:16]
    calls = jl('b690_author_answers.json').get('calls') or []
    ans = [_iso_epoch(c.get('result_ts') or '') for c in calls]
    tp = _git_ct(PP, K.FACES_PP)
    return dict(control='CONTROL EQUAL True ; LINES ADDED 3 ; REMOVED 3 ; PAGE WRITTEN True' in fd, emitted=bool(m) and m.group(2) == sha,
                alone=_files_of(PP, K.FACES_PP) == [K.FACES_PAGE], after_word=len(ans) >= 2 and all(ans) and bool(tp) and max(ans) < tp,
                page_commits=[l for l in g(PP, 'log', '--format=%h', K.PRE_PP + '..HEAD', '--', K.FACES_PAGE).split() if l])


def _n4():
    t0, moved = _kernels_moved()
    f = _faces_state()
    ok = bool(t0) and not moved and f['control'] and f['emitted'] and f['alone'] and f['after_word'] and f['page_commits'] == [K.FACES_PP]
    return ('HELD' if ok else 'REFUTED'), (
        'no kernel main written and no tag moved since the act began (%s): %s; the faces page written by the generator alone -- the control equal '
        'and the page written and read back (relay data/b690_faces_diff.txt) %s, the page at PLACE-papers HEAD the generator`s emission by sha256 '
        '%s, its commit %s the page alone %s and the act`s one write of it %s -- and on the author`s word alone, both answers returned before that '
        'commit: %s' % (time.strftime('%H:%M:%SZ', time.gmtime(t0)) if t0 else '?', moved or 'NONE', f['control'], f['emitted'], K.FACES_PP,
                        f['alone'], f['page_commits'] == [K.FACES_PP], f['after_word']))


def _n5():
    face = jl('b690_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b690_', x)]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b690_|audit_b690_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA) or x in K.SHARED_APPENDED)]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import importlib
    argv, sys.argv = sys.argv, sys.argv[:1]
    try:
        CH = importlib.import_module('b690_checks')
    finally:
        sys.argv = argv
    new_arms = sorted(set(a_[0] for a_ in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    ob = jl('b690_commands.json').get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    wf = g(KERN, 'show', 'main:.github/workflows/build-module.yml').lower()
    wf_ident = [w for w in IDENT if w in wf]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = k_ok and not pp_beyond and not kinds_beyond and not shared_tools and not differ and not new_arms and not ident and not wf_ident and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; standing arms added: %s '
            '(the act`s arms over its own banks %d); the shared tools edited %s; sealed tools not agreeing %s; PLACE-papers beyond FINDINGS, '
            'OPEN_TRAILS and the regenerated faces page: %s; relay files of a kind beyond the act`s banks and tools, the table, the root list, '
            'b689`s push-out bank and the shared files appended (%s): %s; "patent" in the lines written: %s; outbound requests other than git %d, '
            'an identifier of the author in %s; in SIDE-explicit-formula`s workflow file: %s' % (
                K.DRAFT, k_ok, new_arms or 'NONE', len(K.ACT_ARMS), shared_tools or 'NONE', differ or 'NONE', pp_beyond or 'NONE',
                ', '.join(K.SHARED_APPENDED), kinds_beyond or 'NONE', pat or 'NONE', len(ob), [r['line'] for r in ident] or 'NONE', wf_ident or 'NONE'))


def _s_scores():
    import collections
    TF, RA_ = jl('b690_table_final.json'), jl('b690_root_arm.json')
    _r, _n, sh = seal_hashes()
    return {
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))
               if TF else 'waits on the final table (relay data/b690_table_final.json)'),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally' if RA_
               else 'waits on the root and its arm (relay data/b690_root_arm.json), computed after the entry'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }


def scores(*a):
    """`scores [dry]` writes data/b690_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b690_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        return
    if close:
        put_json('b690_scores_close.json', dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, 'b690_scores.json')):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('b690_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def scores_line(S):
    """the entry's scores line, composed from the scores bank alone (the act arm G-ENTRY-SCORES-EQUAL composes it the same way and compares)."""
    return '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.'


# ================================================================================ THE RECORD: THE ENTRY BEFORE THE ROOT, THE TRAIL CARRYING IT
def TRAIL_HEAD():
    return ('### b690 — lane two, act one hundred and seventeen, the reading act under (R300): reading 3; b689’s post-seal failure by corrigendum; '
            'P3 across the corpus; the faces line at Q0 regenerated; the dependency-circuit reading specified; three rules banked')


def _calls():
    return jl('b690_author_answers.json').get('calls') or []


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _figs():
    """the figures the title and the entry carry, each read from its bank."""
    lic, res, rul, lag, p3 = (jl('b690_r3_%s.json' % n) for n in ('licensed', 'residues', 'rules', 'lag', 'p3'))
    return dict(outside=lic.get('total'), outside_b680=lic.get('b680'), zero=lic.get('zero'), residues=len(res.get('rows') or []),
                carried=len(res.get('carried') or []), rules=len(rul.get('rows') or []), armed=rul.get('armed'), median=lag.get('median'),
                median_b680=(lag.get('b680') or {}).get('median'), maximum=lag.get('maximum'), p3=p3.get('outside'), stated=p3.get('stated'),
                hits=len(p3.get('hits') or []), p3_named=p3.get('named'))


def _title():
    """the ferry's form, adjusted to what the act read: "Reading 3: <rows outside LICENSED or CITED>, <n> residues, <n> rules with <n> arms,
    keystone lag median <n>; P3 named at <n> lines, <n> still reading stated; the faces line at Q0 <regenerated | held>; the dependency-circuit
    reading specified; b689's post-seal failure by corrigendum"."""
    f = _figs()
    faces = 'regenerated' if 'PAGE WRITTEN True.**' in rdn('b690_faces_diff.txt') else 'held'
    spec = 'the dependency-circuit reading specified' if _spec_state()['full'] else 'the dependency-circuit reading not yet specified'
    corr = 'b689’s post-seal failure by corrigendum' if 'THE ENTRY AT FINDINGS :%d' % K.CORRIGENDUM_LINE in rdn('b690_corrigendum.txt') else \
        'b689’s post-seal failure carried'
    return ('## Reading 3: %s rows outside LICENSED or CITED, %s residues, %s rules with %s arms, keystone lag median %s; P3 named at %s lines, %s '
            'still reading stated; the faces line at Q0 %s; %s; %s' % (f['outside'], f['residues'], f['rules'], f['armed'], f['median'], f['p3'],
                                                                 f['stated'], faces, spec, corr))


def _finding_text():
    """the FINDINGS entry, composed before the root: its scores line from the scores bank alone (data/b686_rules.txt row (1)); the root is
    carried by the trail record."""
    S = jl('b690_scores.json')
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b690_author_answers.txt'), re.M))
    c1 = _rl_lines('b690_record_lines.json') + ['?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    corr, ords, pair, onec, asec = (jl(n) for n in ('b690_r3_corr.json', 'b690_r3_orders.json', 'b690_r3_pair.json', 'b690_r3_onecopy.json',
                                                    'b690_arm_seconds.json'))
    rj = jl('b690_r3_rules.json').get('counts') or {}
    arm_last = ([r for r in jl('b690_r3_arms.json').get('rows') or [] if r.get('act') == 'b689'] or [{}])[0]
    slow = ', '.join(asec.get('slowest') or []) or '?'
    e = ['', _title(), '',
         'The third reading of the programme’s own state, each figure by the tool that reads it with the hand count beside: %s rows stand '
         'outside LICENSED or CITED across the agenda against b680’s %s, the drop the seven kernels cut since b680, and the pair rule’s four '
         'conditions hold at both reading acts in %s of 4; P3 at Q0, derived and not compiled since b687, is named at %s lines outside the '
         'ledgers, %s of them kernel docstrings still reading it stated; the faces line at Q0 now carries v0.34’s strip-free face; and the '
         'dependency-circuit reading is specified for a later act to build.' % (f['outside'], f['outside_b680'], pair.get('both', '?'), f['p3'],
                                                                                 f['stated']), '',
         '*Filed at b690 on the author’s ruling `(R300)` and the author’s words at its prompts; %d questions put. Banks: relay '
         '`data/b690_reading3.txt` and its twelve route banks `data/b690_r3_<route>.txt`, `data/b690_faces_diff.txt`, '
         '`data/b690_nodes_zeta.txt`, `data/b690_circuit_spec.txt`, `data/b690_rules.txt`, `data/b690_corrigendum.txt`, '
         '`data/b690_arm_seconds.txt`, `data/b690_tool_repairs.txt`; the tool `tools/b690_readings.py`.*' % n_ans, '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed; %d answers checked before they were acted '
         'on. b689 at its weight (FINDINGS :%s), its head line quoted.' % (cc.group(1) if cc else '?', cc.group(2) if cc else '?',
                                                                       cc.group(3) if cc else '?', checks, c1[0]), '',
         '**The corrigendum** (`(R300)`(2)): FINDINGS :%d, generated in b678’s form -- b689’s face declared no arm failing on real state; '
         'G-EDIT-ROUTE failed after the lock on the seat’s sed read of the dry entry, pre-push and post-push, the count 115 of 116; the sealed '
         'face unedited, the corrigenda bank’s row (4) appended.' % K.CORRIGENDUM_LINE, '',
         '**Reading 3** (`(R300)`(3), b680’s figure beside each): rows outside LICENSED or CITED %s (%s), documents at zero %s; Correspondence '
         'rows behind by b670’s method %s (%s), at the generator’s claim %s, five cells held by hand; orders %s, open %s, discharged %s, two '
         'entered since b680, open and older than ten acts without a trigger %s; methods READY %s of 12 by code, 12 with the hand cells; '
         'keystone lag median %s (%s), maximum %s; W-ORD-ONE-COPY %s lines differing, unchanged; the ceiling equal at its three placements.' % (
             f['outside'], f['outside_b680'], f['zero'], corr.get('behind'), (corr.get('b680') or {}).get('behind'), corr.get('claim'),
             ords.get('total'), ords.get('open'), ords.get('discharged'), ords.get('unsteady'), jl('b690_r3_methods.json').get('ready_code'),
             f['median'], f['median_b680'], f['maximum'], onec.get('differing')), '',
         '**The census**: %s rules over the rules banks b674 through b690, %s with an arm, %s PROSE, %s traceable and vacuous, %s traceable with a '
         'live trace and no arm, %s not yet sorted; the arms %s standing and %s act-local at b689, the standing arms clocked at HEAD by part, the '
         'three slowest %s; %s residues, %s carried -- R3b and the two of SIDE-li-map, each with its trigger -- b689 leaving none.' % (
             f['rules'], f['armed'], rj.get('PROSE', '?'), rj.get('TRACEABLE, VACUOUS', '?'), rj.get('TRACEABLE, LIVE', '?'),
             sum(v for k, v in rj.items() if k.startswith('NOT SORTED')), (arm_last.get('standing') if arm_last else '?'),
             (arm_last.get('act_local') if arm_last else '?'), slow, f['residues'], f['carried']), '',
         '**P3** (`(R300)`(3)): git grep over the papers, the faces page, the keystones and every kernel’s Lean, bounded to the source trees -- '
         '%s hits, %s at Q0 naming P3; outside the ledgers %s: the faces page reads it derived, and SIDEExplicitFormula/Schema/EpsteinQ0.lean :106 '
         'and :110-:111 still read it “stated, not proved; open”, against its status of record, derived and not compiled (relay '
         'data/b687_p3_status.txt) -- a reading for the act that compiles it, not an edit here.' % (f['hits'], f['p3_named'], f['p3']), '',
         '**The faces line** (`(R300)`(3) and the author’s two words): the input row and the successor raised as one prompt; a word-level diff '
         'and the tail checked, the tail differing by one phrase raised again and amended to carry its act “(b689)”; the control re-emitting '
         'the committed page byte for byte, then `tools/chain_page.py` writing the page from the new list, two lines changed. The page’s header '
         'still names its generation tag v0.26 = 82550e4, read from the list’s pin line, while the kernel stands at v0.34: entered as a reading.', '',
         '**The instrument** (`(R300)`(4)): the dependency-circuit reading specified row by row -- INPUT, SERIES, TERMINALS, SHORTS, WIDTH, LOAD, '
         'CLAUSE-DOMINANCE, READFIRST-CLOSURE on the author’s word, OUTPUT -- each with the object it reads and its output form; '
         '`W-ORD-CIRCUIT-READING` entered (OPEN_TRAILS :%d); no tool written.' % K.ORDER_LINE, '',
         '**The rules** (`(R300)`(5)): the entry, the dry entry and the trail read after the seal through the Read tool or the record tool’s print '
         '(from b691, kept here ahead of it); every line a re-cut removes searched across the kernel’s tree before the merge (from b691); the '
         'ferry on long lines, no quoted line wrapped (the navigator’s, from b690).', '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b680’s reading 2, b687’s status of P3 and b689’s faces successor '
         'row, and is re-read by b691, whose re-cut carries rule (2) and the residues’ triggers, and by the research act that builds the '
         'dependency-circuit reading. It strengthens the programme’s offering of a reading of its own state made by code wherever a tool reads, '
         'each figure beside the last reading’s.', '',
         '**Carried to:** b691 (the re-cut act: the tie between SIDE-archimedean and SIDE-rcurve, rule (2) binding, the arms for rules (1) and (2) '
         'sorted); `W-ORD-CIRCUIT-READING` and `W-ORD-EPSTEIN-COUNT-LEAN` for the author’s word at b691 -- the kernel docstrings that read P3 '
         'stated among the second’s readings; the faces page’s header tag for a regeneration with a fresh probe; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the title’s “<licensed rows> rows licensed” read as the figure the reading takes, the rows outside LICENSED or CITED; (2) “each '
              'rule’s arm or its PROSE/VACUOUS sort” read in relay data/b683_arms_sort.txt’s words, SORT and STATE, the two traceable rules with a '
              'live trace and no arm named apart; (3) the pair-rule readings in b680’s form read as the rule’s own four conditions at both acts, '
              'not the figures’ equality; (4) the orders’ steadiness by b670’s predicate with the age from 690, as b680 aged it from 680; (5) the P3 '
              'grep over every D:/SIDE-* kernel, T-COUNT read as a word and a sentence wrapped through a grep line read whole; (6) relay '
              'data/b689_faces_rows.txt appended on the author’s answers and read as a shared additive file; (7) the faces diff counted with '
              'difflib’s autojunk off beside b688’s count; (8) “a seventh reading” placed between INPUT and OUTPUT')


def _trail_text():
    S, J = jl('b690_scores.json'), jl('b690_act_root.json')
    fj = jl('b690_findings.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b690_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b690_record_lines.json') + ['?']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R300) ratified.** (1) b689 at its weight. (2) The post-seal failure by corrigendum. (3) Reading 3. (4) The dependency-circuit '
             'reading. (5) Three rules. (6) The branches. (7) The read-first bank. (8) The draft held at v5. (9) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b689’s weight), :%d (the corrigendum), :%s (the entry); OPEN_TRAILS.md:%d (`W-ORD-CIRCUIT-READING`); '
             'this record.' % (c1[0], K.CORRIGENDUM_LINE, fj.get('entry_line'), K.ORDER_LINE), '',
             '**Act root:** b690 `%s` (previous `%s`, b689’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s (relay data/b690_author_answers.txt); none after the root.' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The kernels:** none written; SIDE-explicit-formula at v0.34 (peeled 8fbc27b), b689’s run and merge read by the standing runner arms.', '',
             '**The readings:** relay data/b690_reading3.txt and its route banks data/b690_r3_<route>.txt (tools/b690_readings.py); the faces line '
             'relay data/b690_faces_diff.txt; the instrument relay data/b690_circuit_spec.txt; the rules relay data/b690_rules.txt.', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b690_closing.txt).', '',
             '**The open orders:** `W-ORD-CIRCUIT-READING` (the research act after b691); `W-ORD-EPSTEIN-COUNT-LEAN` (a research act after b690); '
             '`W-ORD-CORRESPONDENCE-CARRIED-AT` (before any generator run that writes a page -- the faces generator writes no Correspondence cell); '
             '`W-ORD-LEDGER-SPLIT-RESOLVER` (on the author’s word); `W-ORD-CHAIN-PAGE-B638-CASES`; `W-ORD-PRINT-TARGETS`; `W-ORD-ONE-COPY`; '
             '`W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; `W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; `W-ORD-ROOT-BINARY-BANK`.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b690_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S, C = jl('b690_scores.json'), jl('b690_scores_close.json')
    L = ['=' * 104, 'b690 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s%s' % (
        k2, S[k2][0], S[k2][1], ('  ### AT THE CLOSE: %s -- %s' % (C[k2][0], C[k2][1])) if (S[k2][0] == 'PENDING' and C.get(k2)) else '')
        for k2 in SCORE_KEYS]
    L += [''] + rdn('b690_defects.txt').rstrip(NL).split(NL)
    put_txt('b690_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b690_scores.json', 'b690_findings.json', 'b690_trail.json', 'b690_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b690_record_lines.json') + ['?']
    L = ['b690 -- THE COMPONENTS, BANKED UNDER (R300).', '',
         '### COMPONENT 0 : the citation check (data/b690_citation_check.txt), step zero (data/b690_ferry.txt, data/b690_readfirst.txt, '
         'data/b690_stepzero.txt, data/b690_tests_stepzero.txt, data/b690_rowgen_stepzero.txt, data/b690_branches.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b689`s weight FINDINGS :%s ; the corrigendum FINDINGS :%d (data/b690_corrigendum.txt) ; the corrigenda bank`s row (4)' % (
             c1[0], K.CORRIGENDUM_LINE),
         '### COMPONENT 2 : reading 3 (data/b690_reading3.txt, data/b690_r3_<route>.txt), the P3 grep, the residues, the faces line regenerated '
         '(data/b690_faces_diff.txt) ; N2 %s ; N4 %s' % (S['N2'][0], S['N4'][0]),
         '### COMPONENT 3 : the circuit specification (data/b690_circuit_spec.txt), W-ORD-CIRCUIT-READING (OPEN_TRAILS :%d), the rules '
         '(data/b690_rules.txt) ; N3 %s' % (K.ORDER_LINE, S['N3'][0]),
         '### COMPONENT 4 : the carry-time reading (data/b690_tool_repairs.txt), the dry-run steps (data/b690_reg_gate.txt), the seal '
         '(data/b690_seal_hashes.json), the suite in four parts, the per-arm seconds (data/b690_arm_seconds.txt) ; S3 %s' % S['S3'][0],
         '### COMPONENT 5 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('b690_components.txt', L)
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
    cells_, fired = screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells_)
        return
    if not os.path.isfile(os.path.join(D, 'b690_scores.json')):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, 'b690_findings.json', dict(title=t))
    j = jl('b690_findings.json')
    j['entry_line'] = ln
    put_json('b690_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b690_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


FACE_REL = 'data/b690_registration_2026-10-19.txt'
FACE = os.path.join(D, 'b690_registration_2026-10-19.txt')


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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b690_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b690_regspec.py')], 'b690_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b690_satisfiable.json', '--emit', 'b690'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b690_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b690_census_stepzero.txt'), ('b327_faces_census.py', 'b690_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b690_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b690'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b690_reg_gate.txt', 'data/b690_reg_termscan.txt', 'data/b690_regspec_run.txt', 'data/audit_b690_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b689's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '2026-10-19-b690'
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
    put_json('b690_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b690':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b690`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b690_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b690_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b690_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b690 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b690 (the last export b689`s, D:/MY-DOwnloads/mirror-refresh-2026-10-19-b689.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b690_mirror.txt', L)
    put_json('b690_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


# ================================================================================ THE CARRY-TIME READING (the ferry's Component 4)
REPAIRS = [
    ('THE STANDING SET FOR b690 (answering no defect: the act`s objects): the standing arms are b689`s face`s (G2) arms less b689`s act arms,',
     'the twenty rule arms among them, no standing arm added; the runner arms read the last merged run -- b689`s run and its merge (8fbc27b,',
     'v0.34) on SIDE-explicit-formula -- as b685`s suite read b684`s, no run in this act; the step-zero arms read eight branches in three',
     'repositories, seven local and one remote; the count arms` floors are this act`s (two prompts in two calls, two mid-act checks, the',
     'defects as lettered at the seal).'),
    ('THE STEP-ZERO TESTS` SET (answering the carried argument): G-STEPZERO-TESTS reads the step-zero bank`s failing set -- test_chain_page.py',
     '(9) against b688`s list, the list the page named at step zero, and test_chain_page_b638.py (4)-(7), the standing cases since b638; no',
     're-run against another list is needed, the run`s list being the page`s.'),
    ('THE FACES PAGE OUT OF THE FILES READ UNEDITED (answering no defect: (R300)(3) and the author`s word regenerate it): CURRENTS loses',
     'THE_CLAUSE_AND_ITS_COMPILED_FACES.md, as b688 took it out to regenerate it; G-PP-SCOPE allows FINDINGS, OPEN_TRAILS and the page',
     '(tools/b690_worklist.py PP_WRITTEN).'),
    ('THE PREVIOUS ACT`S WINDOW IN THIS SAME SESSION (answering no defect: this act continues b689`s session): G-EDIT-ROUTE`s previous-act',
     'window reads b689`s capture after its post-push suite -- from the call that combined b689`s post-push parts to (R300)`s line, in',
     'session 2c300355 -- the window b688`s form read before b689 moved to a new session (tools/b690_record.py `prev_capture`).'),
    ('b689`S FACES ROWS BANK AMONG THE SHARED ADDITIVE FILES (answering no defect: the author`s two answers at the prompt of (R300)(3) order',
     'the word-level diff, the tail and the amended row written beneath its two rows): G-PRIORBANK-UNCHANGED reads every relay bank tracked',
     'before the act but the shared appended files; data/b689_faces_rows.txt joins data/b675_corrigenda.txt there, each read as a prefix',
     'extension carrying b690`s rows (tools/b690_worklist.py SHARED_APPENDED; G-SHARED-ROWS-APPENDED).'),
    ('THE PER-ARM CLOCK (answering (R300)(3)`s reading, the standing arms` seconds at HEAD by part: no suite before this act clocked an arm by',
     'itself, b689`s parts banking their phases): tools/b690_checks.py clocks each arm`s three readings -- LIVE, NEG, POS -- and banks',
     'data/b690_arm_seconds_<part>.json at the pre-run, the shared phases beside; the record tool`s `armsecs` gathers the four into',
     'data/b690_arm_seconds.txt, the three slowest named.'),
    ('tools/rule_arms.py BACK AMONG THE STANDING INSTRUMENTS (answering no defect: no shared tool is repaired in this act): b689 sealed it with',
     'its act after (R299)(2)`s repair; here REPAIRED_TOOLS is empty and G-INSTRUMENTS-UNEDITED reads it, before, working tree and HEAD.'),
    ('THE COMMAND BANK NAMES ONE-LINE PROGRAMS (answering this act`s defect (a)): beside the edit route`s offences, the command bank lists every',
     'command that runs python -c, so the reads it made through an interpreter`s print, where the Read tool would have read the lines, are',
     'counted by the bank and not by recollection; no arm reads them.'),
]
CARRY_HEAD = '### THE CARRY-TIME READING OF THE TOOLS (the ferry`s Component 4), AGAINST b689`S SEALED COPIES'


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


INST_READ = ('rule_arms.py', 'edit_route.py', 'e0_rule.py', 'b678_corrigendum.py', 'chain_page.py', 'b680_readings.py', 'b670_record.py',
             'b672_record.py', 'correspondence_gen.py')


def repairs(*a):
    """the carry-time section of data/b690_tool_repairs.txt: each tool carried from a sealed b689 copy read against b689's seal hash first and
    its diff counted by hunks; the standing instruments this act's tools import read against the last seal record naming them and against
    relay before the act; the repaired readings' diffs against b689's sealed copies printed whole. The bank's head, written by the Write tool
    before, is kept: the route replaces only its own section, from its head line to the bank's end."""
    import difflib
    import hashlib
    seal = jl('b689_seal_hashes.json').get('tools') or {}
    rows = []
    for t0 in ('b689_citation.py', 'b689_closing.py', 'b689_reg_gate.py', 'b689_regspec.py', 'b689_tests.py', 'b689_worklist.py',
               'b689_record.py', 'b689_checks.py'):
        t1 = t0.replace('b689_', 'b690_')
        old, new = os.path.join(T, t0), os.path.join(T, t1)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        ex = os.path.exists(new)
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8',
                           errors='replace').stdout if ex else ''
        rows.append((t0, t1, now, seal.get(t0), len(re.split(r'(?m)^(?=@@ )', d)[1:]), ex))
    inst = {}
    for t in INST_READ:
        nowh = hashlib.sha256(open(os.path.join(T, t), 'rb').read()).hexdigest()
        acts = [x for x in ('b689', 'b688', 'b687', 'b686', 'b685', 'b684', 'b683') if (jl('%s_seal_hashes.json' % x).get('tools') or {}).get(t)]
        headh = hashlib.sha256(subprocess.run(['git', '-C', ROOT, 'show', '%s:tools/%s' % (K.PRE_RELAY, t)], capture_output=True).stdout).hexdigest()
        inst[t] = (nowh, acts[0] if acts else None, (jl('%s_seal_hashes.json' % acts[0])['tools'][t]) if acts else None, headh,
                   g(ROOT, 'log', '-1', '--format=%h %cI', '--', 'tools/' + t).strip())
    s9r, s0r = rd(os.path.join(T, 'b689_record.py')), rd(os.path.join(T, 'b690_record.py'))
    s9c, s0c = rd(os.path.join(T, 'b689_checks.py')), rd(os.path.join(T, 'b690_checks.py'))
    nd = []
    for (a9, f9), (a0, f0), s9, s0 in ((('b689_record.py', 'prev_capture'), ('b690_record.py', 'prev_capture'), s9r, s0r),
                                       (('b689_checks.py', 'tests_ok'), ('b690_checks.py', 'tests_ok'), s9c, s0c),
                                       (('b689_checks.py', 'branches_ok'), ('b690_checks.py', 'branches_ok'), s9c, s0c),
                                       (('b689_checks.py', 'main'), ('b690_checks.py', 'main'), s9c, s0c)):
        nd += list(difflib.unified_diff(_fn_src(s9, f9).split(NL), _fn_src(s0, f0).split(NL) if s0 else [],
                                        '%s %s (sealed)' % (a9, f9), '%s %s%s' % (a0, f0, '' if s0 else ' (NOT YET CARRIED)'), n=1, lineterm=''))
    for c in ('CURRENTS', 'STEPZERO_FAILING'):
        nd += list(difflib.unified_diff(_const_src(s9c, c).split(NL), _const_src(s0c, c).split(NL), 'b689_checks.py %s (sealed)' % c,
                                        'b690_checks.py %s' % c, n=1, lineterm=''))
    L = [CARRY_HEAD + ' (%s)' % utc(), '',
         '### rows are repairs with the defect they answer, after the carried tools: b689`s sealed copy and its seal record; the hunks of the diff',
         '### to b690`s copy. Every hunk is the act`s own text -- its names, its banks, its sections and its predicates over this act`s banks --',
         '### save the repairs below.', '']
    for t0, t1, now, s, nh, ex in rows:
        L.append('  %-20s -> %-20s b689 sealed %s ; the seal`s record %s ; %s ; hunks %s' % (t0, t1, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh if ex else 'NOT YET CARRIED'))
    for t, (nowh, act, sh, headh, last) in inst.items():
        L.append('  %-22s  the standing instrument, unedited in this act: %s ; at relay %s %s ; the last seal record naming it (%s`s) %s ; its last '
                 'commit %s' % (t, nowh[:16], K.PRE_RELAY, headh[:16], act or 'NONE', (sh or '### NONE')[:16], last))
    L.append('')
    for i, r in enumerate(REPAIRS, 1):
        L += ['  REPAIR %d -- %s' % (i, r[0])] + ['  ' + x for x in r[1:]]
    L += ['', '### THE DIFF OF THE REPAIRED READINGS AGAINST b689`S SEALED COPIES (tools/b689_record.py sha256 %s, tools/b689_checks.py sha256 %s), '
          'WHOLE:' % ((seal.get('b689_record.py') or '### NONE')[:16], (seal.get('b689_checks.py') or '### NONE')[:16])]
    L += ['    ' + l for l in nd]
    carried = sum(1 for r in rows if r[5])
    unedited = all(v[0] == v[3] for v in inst.values())
    L += ['', '### ### **REPAIRS %d ; THE SEALED COPIES %s ; TOOLS CARRIED %d OF %d ; THE STANDING INSTRUMENTS UNEDITED %s ; A REPAIRED SHARED '
          'TOOL NONE ; THE REPAIRED READINGS` DIFF LINES %d.**' % (
              len(REPAIRS), 'AGREE' if all(s == now for _a, _b, now, s, _n, _e in rows) else '### DIFFER', carried, len(rows), unedited, len(nd))]
    old = rdn('b690_tool_repairs.txt')
    keep = old[:old.index(CARRY_HEAD)].rstrip(NL) if CARRY_HEAD in old else old.rstrip(NL)
    put_txt('b690_tool_repairs.txt', keep.split(NL) + ['', ''] + L)
    print(L[-1])


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, answers=answers, faces=faces, order=order, commands=commands, defects=defects,
              repairs=repairs, kernels=kernels, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final, armsecs=armsecs,
              scores=scores, desk=desk, components=components, findings=findings, trail=trail, drycheck=drycheck, gatebanks=gatebanks,
              mbuild=mbuild, mroot=mroot, mverify=mverify, mbank=mbank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b690_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
