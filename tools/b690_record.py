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


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, answers=answers, faces=faces)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b690_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
