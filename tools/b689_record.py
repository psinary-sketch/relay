# -*- coding: utf-8 -*-
"""b689_record.py -- THE ACT'S RECORD TOOL, b689 under (R299).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b689's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b688_record.py in stages: the helpers, the guarded landing, the readers, step zero's rowgen and branches
### routes and Component 1's weight line and arm reading first; the plan, runner and build routes at Components 2-4; the late routes at
### Component 5. Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b689_record.py
### <route> [dry]`.
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
import b689_worklist as K          # noqa: E402

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
        'b689_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b689_findings.json': dict(entry_line=99999, title='stand-in'),
        'b689_trail.json': dict(line=99999),
        'b689_act_root.json': dict(root='0' * 64, previous='f168527e' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b689's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b689_scanfile_%s.md' % tag)
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
    """a row of data/b689_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


def read_runner_row(r):
    """a row of data/b689_runner_rows.json: the kernel, its label, the ref (40 hex), the run id and the gate; returns (kernel, label, gate)."""
    if not isinstance(r, dict) or not re.match(r'^SIDE-[\w-]+$', r.get('kernel') or '') or not re.match(r'^[\w-]+$', r.get('label') or '') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['kernel'], r['label'], r['gate']


def read_use_row(r):
    """a row of data/b689_plan.json's uses: the strip-uses bank's line (9-30), its file :line, the class (one of USE_CLASSES) and the reason;
    returns (row, class)."""
    if not isinstance(r, dict) or not isinstance(r.get('row'), int) or not 9 <= r['row'] <= 30 or not re.match(r'^Li\w+\.lean :\d+$', r.get('at') or '') \
            or r.get('cls') not in USE_CLASSES or not (r.get('why') or '').strip():
        raise ValueError('use row of another shape: %r' % (r,))
    return r['row'], r['cls']


USE_CLASSES = ('DISCHARGED', 'RE-PROVED', 'OBSTRUCTED')
READERS = ['read_score_row', 'read_head', 'read_branch_row', 'read_runner_row', 'read_use_row']


# ================================================================================ STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE (b670's route, carried)
def roster():
    """the 19 roster tables of data/b586_corroboration.txt :34, at the paths that bank read (carried from b670_record.py :548-:552)."""
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b689_rowgen_<stage>.txt."""
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
    L = ['b689 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b689_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R299)(6))
def branches(*a):
    """every branch (R299)(6) names, its tip read before any delete, its fate; any branch under the push-b688 prefix that --merged lists and
    the ruling does not name, reported and KEPT. No remote branch is named this act. data/b689_branches.txt (.json)."""
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
            if (x.startswith('push-b688') or x.endswith('-b688') or x.endswith('-b688r')) and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b689 -- STEP ZERO, (R299)(6): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local ; tip ; listed by `git branch --merged main --list <name>` ; fate. Deleted by name in',
         '### the house form, each delete command naming one branch with no glob in any half, one command per message, in sequence; no branch',
         '### the ruling does not name.']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                               r['fate']) for r in rows]
    L += ['', '### branches of b688 that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; TO BE DELETED %d ; UNNAMED OF b688 %d.**' % (
        len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), len(rows), len(extra))]
    put_txt('b689_branches.txt', L)
    put_json('b689_branches.json', dict(at=utc(), rows=rows, extra=[list(x) for x in extra]))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R299)(1)
WH = ('*Appended 2026-10-19 by b689 to b688’s entry (:9314), under `(R299)`(1) -- b688 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b688_closing.txt), ITS DEFECT (f) REPAIRED BY A GENERATED CORRIGENDUM ENTRY:*')
WB = (' “b688 closed: relay 4bee98dc, PLACE-papers c3af808; suite 116 of 117; root f168527e8655305c…; 4 prompts answered; 6 defects” '
      '(data/b688_closing.txt :1), the closing pushed and read back at relay 007d4ead (data/b688_closing_push_out.txt). SIDE-li-map’s three '
      'docstring rows outside LICENSED/CITED went to 0, comment and docstring lines alone, both builds on the hosted runner, 14 prints equal '
      'before and after (data/b688_prints_SIDE-li-map.txt), merged at 9e02bc0 and tagged v0.1.1, with b515e6b named as v0.1 carrying no tag '
      'and the pin row beneath the licensed table (data/b670_licensed_table.txt :285); two SIDE-li-map residues carried -- '
      'PrimeLedgerPositivity.lean :29-:31 quoting a removed line of LiLinearMap.lean, and NonnegStream’s docstring :51-:54 naming the real-valued '
      'Λ as an instance of an integer stream (data/b688_cut.txt). The Correspondence cells held on the author’s word, '
      '`W-ORD-CORRESPONDENCE-CARRIED-AT` at OPEN_TRAILS :14922, both dry runs banked. R4 applied: “(salt-checked)” struck at SpinorLeg.lean :21 '
      'and nothing else, :18 making no such claim, so no R4b; 15 prints equal (data/b688_prints_SIDE-spinor.txt), merged at 7e570ee, tagged '
      'v0.1.2. The faces line regenerated with the amendment “the local count T-COUNT (P3) derived ..., not compiled” after the control '
      're-emitted the old page byte for byte. The lattice-sum route entered with seven steps, its tail bound marked as the seat’s own, the '
      'three-point check against b667’s route overlapping at all three, the six consuming rows of b687’s steps bank named '
      '(data/b688_lattice_route.txt). Suite 116 of 117 pre-push and post-push, G-RULE-HEAD-LINE-QUOTED declared by name -- the quote correct by '
      'the citation check’s row, the arm matching one unbroken string against a quote pasted over three lines; all eight scores HELD; root '
      'f168527e over 61 banks; mirror-refresh-2026-10-19-b688.zip CLEAN with the root line; the eight sealed tools’ hashes matching at the close. '
      'Six defects, every one the seat’s (data/b688_defects.txt): (a) the piped push of recut-li-map-b688; (b) a commit message calling the print '
      'bank absent where the bank says present; (c) a duplicated section of the citation bank, fixed before commit; (d) a prompt mixing the '
      'file’s line numbers with the generator’s; (e) two waits backgrounded, the command bank’s reader repaired; (f) the entry at :9314 '
      'saying two commit cites were tested directly (its citation sentence, :9320) where the citation bank tests three, found after the seal -- '
      'repaired at b689 by the generated corrigendum entry that follows, the sealed entry itself unedited. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b689_record_lines.json', 'c1', entry=K.B688_ENTRY,
         check=[('FINDINGS.md', K.B688_ENTRY, '## SIDE-li-map re-cut'), ('OPEN_TRAILS.md', K.B688_TRAIL, '### b688')], dry=dry)


# ================================================================================ COMPONENT 1: THE ARM'S READING AT HEAD, (R299)(2)
def _arm_inputs(act):
    """rule_arms.sources' two inputs for G-RULE-HEAD-LINE-QUOTED, read the way rule_arms.py :228-:229 reads them: the act's ferry bank and the
    previous act's closing :1."""
    n = int(act[1:])
    return dict(n=n, ferry=rdn('%s_ferry.txt' % act), prev_head=(rdn('b%d_closing.txt' % (n - 1)).split(NL) or [''])[0])


def armread(*a):
    """the arm G-RULE-HEAD-LINE-QUOTED read through tools/rule_arms.py's own `reading` at HEAD (the shared tool imported, not copied) against
    b688's ferry bank and this act's; then its planted case (rule_arms.py :466-:467) over each, which must fail. Prints only, unless `bank`:
    then the reading is appended to data/b689_tool_repairs.txt's ARM READING section by the Edit tool's hand, not here -- this route writes
    nothing."""
    import rule_arms as RA
    out = []
    for act in ('b688', 'b689'):
        R = _arm_inputs(act)
        ok, n, bad, how = RA.reading('G-RULE-HEAD-LINE-QUOTED', R)
        Rp = dict(R, prev_head=R['prev_head'] + ' planted')
        pok, _pn, pbad, _ph = RA.reading('G-RULE-HEAD-LINE-QUOTED', Rp)
        out.append((act, ok, n, bad, how, pok))
        print('  %s : the arm %s (count %d, failing %d) -- %s ; the planted case %s' % (act, 'PASSES' if ok else 'FAILS', n, bad, how,
                                                                                    'FIRES' if not pok else 'DOES NOT FIRE'))
    print('### ### **THE ARM AT HEAD: b688 %s ; b689 %s ; THE PLANTED CASE FIRES ON BOTH %s.**' % (
        'OK' if out[0][1] else 'FAILS', 'OK' if out[1][1] else 'FAILS', all(not x[5] for x in out)))


# ================================================================================ THE ANSWERS BANK (b688's route, carried)
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
    """data/b689_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
    every word of the author delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim; a word opened by
    BEGIN with no END noted (b688's route)."""
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
    head = ['### b689 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b689_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b689_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE RUNS AND THE PRINTS (b688's routes, carried; per terminal)
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
    the standard three. data/b689_runner_<kernel>_<label>.txt, data/b689_axioms_<kernel>_<label>.txt and a row of data/b689_runner_rows.json.
    Carried from b688_record.py's runner, the per-terminal reading added."""
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
    L = ['b689 -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (kernel, label.upper(), utc()), '',
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
    put_txt('b689_runner_%s_%s.txt' % (kernel, label), L)
    if row['artifact_sha256']:
        put_txt('b689_axioms_%s_%s.txt' % (kernel, label), ax.split(NL) if ax else ['### EMPTY'])
        put_txt('b689_buildlog_%s_%s.txt' % (kernel, label), blog.rstrip(NL).split(NL))
    j = jl('b689_runner_rows.json') if os.path.isfile(os.path.join(D, 'b689_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('b689_runner_rows.json', dict(rows=rows))
    print(NL.join(L[:14] + L[-3:]))


def prints(*a):
    """`prints <kernel> <before bank> <after bank>`: the 'before' terminals' printed lines compared with the same names' lines in the 'after'
    bank, line for line by name (the after bank prints more names; the new ones are listed apart). data/b689_prints_<kernel>.txt."""
    kernel, bb, ab = a[0], a[1], a[2]
    b, f = rdn(bb), rdn(ab)
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bd, fd = dict(_deps(b)), dict(_deps(f))
    diff = [(n, bd[n], fd.get(n)) for n in bd if fd.get(n) != bd[n]]
    new = [n for n in fd if n not in bd]
    L = ['b689 -- THE PRINTS OF %s: v0.33`S TERMINALS BEFORE AND AFTER THE BRANCH, BY NAME (%s)' % (kernel, utc()), '',
         '### before: relay data/%s (%d terminals) ; after: relay data/%s (%d terminals) ; rows are the terminals that differ:' % (bb, len(bd), ab, len(fd))] + (
             ['    %s : %s | %s' % d for d in diff] or ['    NONE']) + ['### the names printed after and not before (the branch`s new names): %d' % len(new)] + [
             '    %s %s' % (n, fd[n]) for n in new]
    L += ['', '### ### **BEFORE %d TERMINALS ; EACH PRINTED AFTER %s ; DIFFERING %d ; NEW %d ; EQUAL BY NAME %s.**' % (
        len(bd), all(n in fd for n in bd), len(diff), len(new), not diff)]
    put_txt('b689_prints_%s.txt' % kernel, L)
    print(L[-1])


# ================================================================================ THE GRADE AND THE SALT-CHECK, (R299)(4) AND THE AUTHOR'S WORD AT THE SECOND PROMPT
MAIN = 'li_nonneg_cfg_imp_online_ne_zero'
MAIN_FILE = 'SIDEExplicitFormula/Schema/Wide/StripFree.lean'
# ### the seat's reading of the statement's binders, by hand, BEFORE the E0 check (the author's word: the lexicon is a check on that reading
# ### and not its source): each binder, its class and the line that decides it
HAND = (('Z', 'WideConfig', 'the object: a structure (Schema/Wide/Config.lean :28), data, no hypothesis'),
        ('A₀', 'ℝ', 'a real parameter, implicit, no hypothesis'),
        ('hc', 'HCount Z A₀', 'A NAMED PROP OF A KERNEL MODULE (def HCount, Schema/Wide/Config.lean :49): a premise passed through -- the E0 rule (1)'),
        ('hnz', '∀ ρ ∈ Z.carrier, ρ ≠ 0', 'a membership and an inequality on the object`s own carrier: a domain condition -- the E0 rule (2)'))
HAND_GRADE = 'INTERFACES'
HAND_PREMISE = 'hc : HCount Z A₀'
# ### the E0 rule's lexicon, extended at run time in THIS tool (relay tools/e0_rule.py not edited), with the three heads it lacks, each at its
# ### declaration at v0.33 (95f8dc8)
E0_EXTENSION = {'WideConfig': ('data', 'SIDE-explicit-formula SIDEExplicitFormula/Schema/Wide/Config.lean :28'),
                'HCount': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/Schema/Wide/Config.lean :49'),
                'HExcl': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/Schema/Wide/Config.lean :54')}


def _statement(rev, path, name):
    """the theorem's statement verbatim from the file at rev: its declaration line through the `:=` that opens its proof; and its header (the
    text between the name and that `:=`)."""
    src = _show(K.KERNEL, rev, path) or ''
    L = src.split(NL)
    i = next(k for k, l in enumerate(L) if l.startswith('theorem %s ' % name))
    j = next(k for k in range(i, len(L)) if ':= by' in L[k] or L[k].rstrip().endswith(':='))
    st = NL.join(L[i:j + 1])
    head = st.split('theorem %s' % name, 1)[1].rsplit(':=', 1)[0]
    return i + 1, j + 1, st, head


def grade(*a):
    """`grade <rev>`: data/b689_grade.txt -- the main theorem's statement verbatim from the branch at rev, the seat's reading of its binders by
    hand and the grade it gives, then the shared E0 rule's grade as the check (its lexicon extended here), the two compared; the salt-check of
    REGISTRY.md :544 read on the statement, each clause with its reading; the runner's print of the statement's name."""
    import e0_rule as E
    rev = a[0]
    i, j, st, head = _statement(rev, MAIN_FILE, MAIN)
    E.LEXICON.update(E0_EXTENSION)
    eg, why, read = E.grade(head, 'theorem')
    rows = jl('b689_runner_rows.json').get('rows') or []
    run = next((r for r in rows if r.get('ref', '').startswith(rev[:7])), None)
    ax = rdn('b689_axioms_SIDE-explicit-formula_%s.txt' % run['label']) if run else ''
    prof = dict(_deps(ax)).get('SIDEExplicitFormula.Schema.Wide.' + MAIN)
    concl = E.conclusion(E.statement_only(head)) or ''
    salt = [('no True-typed conclusion, no uniformly-True predicate', not re.search(r'\bTrue\b', concl),
             'the conclusion %r: as a predicate on WideConfig it is false at C2b, every coefficient nonnegative with 1 off the line (c2b_lesson, '
             'DERIVES in the run); its consequent is false at C2 too, where the implication holds because λ₁ < 0 (c2_liCoeff_one_neg)' % concl.strip()),
            ('no X = X', not re.search(r'\b(\w+)\s*=\s*\1\b', concl), 'the conclusion`s equation ρ.re = 1 / 2 compares two different terms'),
            ('no hypothesis that is the claim', all('re = 1 / 2' not in t for _n, t in read),
             'the hypotheses %s say nothing of Re ρ = 1/2; the empty configuration and every on-line one meet them' % [n for n, _t in read]),
            ('no fabricated witness', '∃' not in concl, 'the conclusion constructs nothing'),
            ('hypotheses named', all(n for n, _t in read), ', '.join('%s : %s' % x for x in read)),
            ('#print axioms profiled after the first three', prof is not None and set(prof) <= set(STD3),
             'run %s: %s' % (run['run_id'] if run else '### NO RUN', prof))]
    L = ['b689 -- THE GRADE OF THE MAIN THEOREM, READ FROM ITS STATEMENT, AND THE SALT-CHECK, (R299)(4) (%s)' % utc(), '',
         '### rows are the statement verbatim, the binders with their class read by hand, the grade they give, the E0 rule`s check, and the',
         '### salt-check`s clauses with their readings. The statement: SIDE-explicit-formula %s, %s :%d-:%d (the branch strip-free-b689):' % (
             rev[:7], MAIN_FILE, i, j), '']
    L += ['    ' + l for l in st.split(NL)]
    L += ['', '### THE BINDERS, READ BY HAND (the seat`s reading, before the check):']
    L += ['  %-4s : %-28s %s' % b for b in HAND]
    L += ['  THE GRADE READ FROM THE STATEMENT: %s ON THE NAMED PREMISE %s (Wide.HCount); the domain condition hnz is no premise.' % (HAND_GRADE, HAND_PREMISE),
          '', '### THE CHECK: relay tools/e0_rule.py`s grade() on the header, its LEXICON extended in this tool (tools/b689_record.py E0_EXTENSION, '
          'the shared file not edited) with %s:' % ', '.join('%s (%s, %s)' % (k, v[0], v[1]) for k, v in E0_EXTENSION.items()),
          '  E0 GRADE %s ; its reason: %s ; the hypotheses it read: %s' % (eg, why, read),
          '  THE HAND READING AND THE CHECK %s' % ('AGREE' if eg == HAND_GRADE and why == HAND_PREMISE else '### DIFFER'),
          '', '### THE SALT-CHECK (REGISTRY.md :544, the E0 salt-check), clause by clause:']
    L += ['  %-55s %s -- %s' % (c, 'PASS' if ok else '### FAIL', how) for c, ok, how in salt]
    L += ['', '### ### **THE STATEMENT AT %s :%d ; GRADE %s ON %s (READ BY HAND) ; THE E0 CHECK %s, %s ; SALT-CHECK %s ; PROFILE %s.**' % (
        MAIN_FILE.rsplit('/', 1)[1], i, HAND_GRADE, HAND_PREMISE, eg, 'AGREE' if eg == HAND_GRADE and why == HAND_PREMISE else '### DIFFER',
        'PASS' if all(ok for _c, ok, _h in salt) else '### FAIL', prof)]
    put_txt('b689_grade.txt', L)
    print(NL.join(L[-12:]))


# ================================================================================ THE COMMAND BANK (b688's route, carried; the previous act in its own session)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402

SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
PREV_ACT, PREV_ANCHOR, PREV_SESSION_ID = 'b688', 'RULING (R298) BEGIN', 'a90bcdb6-256f-4841-97ff-9638e378446c'
PREV_SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % PREV_SESSION_ID
PREV_SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % PREV_SESSION_ID


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


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def sed_cmd(cmd):
    """data/b685_rules.txt row (2): a command carrying sed in any form, read outside quoted strings."""
    return SED.search(QUOTED.sub('""', cmd)) is not None


SED_KIND = 'R sed in any form (data/b685_rules.txt row (2))'


def prev_capture():
    """G-EDIT-ROUTE's window over the previous act (b687's repair, carried; b689's reading, a new session): b688's capture AFTER ITS POST-PUSH
    SUITE -- every command of b688's session (a90bcdb6) from the call that combined b688's post-push parts into data/b688_checks_postpush.txt
    to that session's end, its closing's commands among them; this act runs in a session of its own."""
    rows = ER.capture(PREV_SESSION, PREV_ANCHOR, PREV_SUBAGENTS)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV_ACT in r['cmd'] and '--combine' in r['cmd']]
    if not first:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE IS NOT IN ITS SESSION`S CAPTURE -- NOTHING READ')
    out = [dict(r, src='%s %s' % (PREV_ACT, r['src'])) for r in rows if first[0] <= r['ts']]
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
    """(R299)(6): a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
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
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    ob = outbound()
    L = ['b689 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (b688`s session %s, from its post-push combine to the session`s end): %d '
              'commands from %s, its offences printed whole (%d):' % (PREV_SESSION_ID[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
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
    L += ['', '### THE COMMANDS CARRYING A REDIRECT ONTO /dev/null, read outside quoted strings (this act`s defect (a), entered there) (%d):' % len(
        nulls)] + (['  #%d %s %s' % (r['n'], r['ts'], r['cmd'].split(NL)[0][:200]) for r in nulls] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R299)(6): one branch per command, no glob in any half): ' + ('; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git (web searches, subagent prompts and fetches), each with the author`s identifiers found in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; REDIRECTS ONTO /dev/null %d ; '
              'MOVE OR DELETE COMMANDS %d ; BRANCH DELETES OF ONE BRANCH AND NO GLOB %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(nulls), len(mv), sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl),
                  len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    put_txt('b689_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b689_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        prev=dict(act=PREV_ACT, session=PREV_SESSION_ID, rows=len(prev),
                                                  offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                        seds=[r['n'] for r in seds], null_redirects=[r['n'] for r in nulls], moves_deletes=[r['n'] for r in mv],
                                        delete_shapes=[dict(n=n, deletes=d, globs=gl) for n, d, gl in shapes], outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r, o in phits:
        print('  PREVIOUS-ACT OFFENCE #%s %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b689_defects.txt').split(NL)
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
    t = rdn('b689_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b689_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


# ================================================================================ THE LATE ROUTES (b688's, carried at Component 5 with b689's names)
def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle', 'SIDE-bijection', 'SIDE-class-number-anomaly',
                                   'SIDE-spinor', 'SIDE-li-map']


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    put_json('b689_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-explicit-formula at v0.34, written under Component 3; no kernel written after this read)' % len(ks))


def seal_hashes():
    import hashlib
    rec_ = jl('b689_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b689_seal_hashes.json')) else {}
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


ROOT_EXCLUDE = re.compile(r'^b689_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*)\.?(txt|json|md|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b689_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(K.SHARED_APPENDED))


def rootbanks(*a):
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['b689 -- G-ROOT-BANKS-COMMITTED`S READING: THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ;'
         ' carried by HEAD ; HEAD`s blob equal to the file' % utc(), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('b689_root_banks.txt', L)
    put_json('b689_root_banks.json', dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b689_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### G-ROOT-BANKS-COMMITTED: A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b689'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b689_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='b689_ra_') as tmp:
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
    L = ['b689 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b689_root_arm.txt', L)
    put_json('b689_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b689 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b689_table_final.txt', L)
    put_json('b689_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


# ================================================================================ THE SCORES: (N1)-(N5) OF (R299)'S FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and not the entry; the entry reads the scorer's bank. `scores` writes
# ### data/b689_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there, the bank it waits on named, and
# ### is read at the close by `scores close` into data/b689_scores_close.json, which no ledger line reads.
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b688_closing_push_out.txt')
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


def _n1():
    cm = jl('b689_commands.json')
    ok = bool(cm) and not cm.get('local_lean')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches %d, each built on the hosted runner (relay '
        'data/b689_commands.txt, %d commands read)' % (cm.get('local_lean') if cm else '### UNREAD', len(cm.get('dispatches') or []),
                                                        len(cm.get('rows') or [])))


def _section11_state():
    """N2's first clause: the plan bank's section 11 equal to data/b679_strip_plan.txt :224-:239; the commit that wrote the plan bank first
    carrying section 11 and no plan row; the plan rows' commit after it."""
    src = rdn('b679_strip_plan.txt').split(NL)[223:239]
    plan = rdn('b689_plan.txt').split(NL)
    head = '== S11. relay data/b679_strip_plan.txt :224-:239, VERBATIM:'
    eq = head in plan and src == plan[plan.index(head) + 1:plan.index(head) + 17]
    first = _show(RELAY, K.SECTION11_COMMIT, 'data/b689_plan.txt') or ''
    alone = head in first and '== 1. THE HYPOTHESIS SET' not in first and 'THE PLAN ROWS' not in first
    t11, tp = _git_ct(RELAY, K.SECTION11_COMMIT), _git_ct(RELAY, K.PLAN_COMMIT)
    return dict(equal=eq, alone=alone, before=bool(t11 and tp and t11 < tp), t11=t11, tplan=tp)


def _strip_free_write_ts():
    """the first moment a Lean file of the strip-free form existed: the Write tool's call on Schema/Wide/StripFree.lean in this act's session,
    and the first commit touching it on any ref of the kernel."""
    ts = []
    for _i, o, _st, _sid in _session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') in ('Write', 'Edit') and 'StripFree.lean' in str(
                    (c.get('input') or {}).get('file_path')):
                ts.append(_iso_epoch(o.get('timestamp')))
    cts = [int(x) for x in g(KERN, 'log', '--all', '--format=%ct', '--', 'SIDEExplicitFormula/Schema/Wide/StripFree.lean').split() if x.isdigit()]
    return (min(ts) if ts else None), (min(cts) if cts else None)


def _n2():
    s11 = _section11_state()
    calls = jl('b689_author_answers.json').get('calls') or []
    plan_call = calls[1] if len(calls) >= 2 else {}        # ### the act's second call: the prompt of (R299)(3), the first being the arm's
    plan_ans = _iso_epoch(plan_call.get('result_ts') or '')
    plan_ask = _iso_epoch(plan_call.get('ts') or '')
    w, c = _strip_free_write_ts()
    order_ = bool(plan_ask and plan_ans and w and c and s11['t11']) and s11['t11'] < plan_ask < plan_ans < w and plan_ans < c
    ok = s11['equal'] and s11['alone'] and s11['before'] and order_
    return ('HELD' if ok else 'REFUTED'), (
        'section 11 printed verbatim into the plan bank (relay data/b689_plan.txt, its 16 lines equal to data/b679_strip_plan.txt :224-:239): %s; '
        'the bank`s first commit (%s) carrying section 11 and no plan row: %s, the plan rows`s commit (%s) after it: %s; the plan prompt put '
        '(%s) and answered (%s) before the first Lean file of the form existed -- the Write tool`s call on Schema/Wide/StripFree.lean (%s), the '
        'first kernel commit touching it on any ref (%s): %s' % (
            s11['equal'], K.SECTION11_COMMIT, s11['alone'], K.PLAN_COMMIT, s11['before'], time.strftime('%H:%M:%SZ', time.gmtime(plan_ask)) if plan_ask else '?',
            time.strftime('%H:%M:%SZ', time.gmtime(plan_ans)) if plan_ans else '?', time.strftime('%H:%M:%SZ', time.gmtime(w)) if w else '?',
            time.strftime('%H:%M:%SZ', time.gmtime(c)) if c else '?', order_))


def _grade_state():
    """N3's reading: the grade bank's statement against the branch's lines; its grade and its check; its commit before the merge's; the
    runner's print of C2b under the strip-free form."""
    gt = rdn('b689_grade.txt')
    i, j, st, _h = _statement(K.BRANCH_FIRST, MAIN_FILE, MAIN)
    verb = all(('    ' + l) in gt.split(NL) for l in st.split(NL))
    graded = 'GRADE INTERFACES ON hc : HCount Z A₀ (READ BY HAND) ; THE E0 CHECK INTERFACES, AGREE ; SALT-CHECK PASS' in gt
    tg, tm = _git_ct(RELAY, K.GRADE_COMMIT), _git_ct(KERN, K.MERGE_COMMIT)
    banked_in = 'data/b689_grade.txt' in g(RELAY, 'show', '--name-only', '--pretty=format:', K.GRADE_COMMIT)
    ax = dict(_deps(rdn(K.RUNNER_BANK)))
    c2b = all(set(ax.get('SIDEExplicitFormula.Schema.Wide.' + n) or ['x']) <= set(STD3) for n in ('c2b_not_ne_zero', 'c2b_lesson'))
    return dict(verbatim=verb, graded=graded, before=bool(tg and tm and tg < tm and banked_in), c2b=c2b, lines=(i, j))


def _n3():
    s = _grade_state()
    ok = s['verbatim'] and s['graded'] and s['before'] and s['c2b']
    return ('HELD' if ok else 'REFUTED'), (
        'the grade read from the statement and banked with it verbatim beside it (relay data/b689_grade.txt, StripFree.lean :%d-:%d at %s): '
        'verbatim %s, the grade INTERFACES on hc : HCount Z A₀ read by hand with the E0 rule`s check agreeing and the salt-check passing: %s; '
        'banked at relay %s before the merge %s: %s; C2b`s reading under the strip-free form printed from the runner -- c2b_not_ne_zero and '
        'c2b_lesson at the standard three in the run`s axioms bank (relay data/%s): %s' % (
            s['lines'][0], s['lines'][1], K.BRANCH_FIRST, s['verbatim'], s['graded'], K.GRADE_COMMIT, K.MERGE_COMMIT, s['before'], K.RUNNER_BANK, s['c2b']))


def _n4():
    main_src = _show(KERN, 'main', MAIN_FILE) or ''
    code = NL.join(l.split('--', 1)[0] for l in re.sub(r'/-[\s\S]*?-/', '', main_src).split(NL))
    sorry_code = len(re.findall(r'\bsorry\b', code))
    ax = _deps(rdn(K.RUNNER_BANK))
    sorry_ax = sum(1 for _n, d in ax if 'sorryAx' in d)
    held = os.path.isfile(os.path.join(D, 'b689_obstruction.txt'))
    ok = bool(main_src) and sorry_code == 0 and sorry_ax == 0 and not held
    return ('HELD' if ok else 'REFUTED'), (
        'no sorry reaches main: SIDE-explicit-formula main`s Schema/Wide/StripFree.lean carries %d sorry in code, and the run`s print %d sorryAx '
        'of %d terminals (relay data/%s); a held branch with its obstruction banked and a work-order -- VACUOUS in this act: no step reached a '
        'sorry, no branch was held (relay data/b689_obstruction.txt %s)' % (sorry_code, sorry_ax, len(ax), K.RUNNER_BANK, 'PRESENT' if held else 'absent'))


def _kernel_writes():
    out = {}
    for k, _pre, _tip, merge, tag, before, files in K.MERGES:
        p = 'D:/' + k
        ch = sorted(x for x in g(p, 'diff', '--name-only', before, 'main').split(NL) if x.strip())
        peel = g(p, 'rev-parse', '--short=7', tag + '^{commit}').strip()
        out[k] = dict(files=ch, want=sorted(files), tag=peel == merge[:7])
    return out


def _n5():
    face = jl('b689_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    kw = _kernel_writes()
    kw_ok = all(v['files'] == v['want'] and v['tag'] for v in kw.values()) and len(kw) == 1
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b689_', x)]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b689_|audit_b689_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA) or x in K.SHARED_APPENDED
                                                or x in ['tools/' + t for t in K.REPAIRED_TOOLS])]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import importlib
    argv, sys.argv = sys.argv, sys.argv[:1]
    try:
        CH = importlib.import_module('b689_checks')
    finally:
        sys.argv = argv
    new_arms = sorted(set(a_[0] for a_ in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    ob = jl('b689_commands.json').get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    wf = g(KERN, 'show', 'main:.github/workflows/build-module.yml').lower()
    wf_ident = [w for w in IDENT if w in wf]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = k_ok and kw_ok and not pp_beyond and not kinds_beyond and shared_tools == ['tools/rule_arms.py'] and not differ and not new_arms \
        and not ident and not wf_ident and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; the kernel main '
            'written by the act (SIDE-explicit-formula: %s) the merge and the tag alone, v0.34 peeled to the merge: %s; standing arms added: %s '
            '(the act`s arms over its own banks %d); the shared tools edited %s -- the (R299)(2) repair the one, sealed with the act; sealed tools '
            'not agreeing %s; PLACE-papers beyond FINDINGS and OPEN_TRAILS: %s; relay files of a kind beyond the act`s banks and tools, the table, '
            'the root list, b688`s push-out bank, the repaired arm and the shared file appended (%s): %s; "patent" in the lines written: %s; '
            'outbound requests other than git %d, an identifier of the author in %s; in SIDE-explicit-formula`s workflow file: %s' % (
                K.DRAFT, k_ok, ', '.join(kw.get('SIDE-explicit-formula', {}).get('files') or []), kw_ok, new_arms or 'NONE', len(K.ACT_ARMS),
                shared_tools or 'NONE', differ or 'NONE', pp_beyond or 'NONE', ', '.join(K.SHARED_APPENDED), kinds_beyond or 'NONE', pat or 'NONE',
                len(ob), [r['line'] for r in ident] or 'NONE', wf_ident or 'NONE'))


def _s_scores():
    import collections
    TF, RA_ = jl('b689_table_final.json'), jl('b689_root_arm.json')
    _r, _n, sh = seal_hashes()
    return {
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))
               if TF else 'waits on the final table (relay data/b689_table_final.json)'),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally' if RA_
               else 'waits on the root and its arm (relay data/b689_root_arm.json), computed after the entry'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }


def scores(*a):
    """`scores [dry]` writes data/b689_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b689_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        return
    if close:
        put_json('b689_scores_close.json', dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, 'b689_scores.json')):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('b689_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def scores_line(S):
    """the entry's scores line, composed from the scores bank alone (the act arm G-ENTRY-SCORES-EQUAL composes it the same way and compares)."""
    return '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.'


# ================================================================================ THE RECORD: THE ENTRY BEFORE THE ROOT, THE TRAIL CARRYING IT
def TRAIL_HEAD():
    return ('### b689 — lane two, act one hundred and sixteen, the research act under (R299): the strip-free Li converse planned from its banks, '
            'raised and built, SIDE-explicit-formula v0.34; defect (f) of b688 by corrigendum; the head-line arm repaired')


def _calls():
    return jl('b689_author_answers.json').get('calls') or []


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _title():
    """the ferry's form, its parts read from the banks: "SIDE-explicit-formula strip-free Li converse: <the theorem's name>, <hypothesis set in
    brief>, <grade>, <v0.34 | branch held at the obstruction>; defect (f) of b688 by corrigendum; G-RULE-HEAD-LINE-QUOTED reading across line
    breaks"."""
    gt = rdn('b689_grade.txt')
    name = 'Wide.' + MAIN if ('theorem %s ' % MAIN) in gt else '?'
    grade_ = 'INTERFACES on Wide.HCount' if 'GRADE INTERFACES ON hc : HCount Z A₀' in gt else '?'
    where = 'v0.34' if 'tag v0.34 peeled local 8fbc27b' in rdn('b689_merge_push_out.txt') else 'branch held at the obstruction'
    hyp = 'ρ ≠ 0 for every point under the local count over the widened class' if 'hnz : ∀ ρ ∈ Z.carrier, ρ ≠ 0' in gt else '?'
    arm = 'G-RULE-HEAD-LINE-QUOTED reading across line breaks' if 'b688 OK ; b689 OK' in ' '.join(rdn('b689_tool_repairs.txt').replace('###', ' ').split()) \
        else 'G-RULE-HEAD-LINE-QUOTED carried'
    corr = 'defect (f) of b688 by corrigendum' if 'THE ENTRY AT FINDINGS :%d' % K.CORRIGENDUM_LINE in rdn('b689_corrigendum.txt') else 'defect (f) of b688 carried'
    return '## SIDE-explicit-formula strip-free Li converse: %s, %s, %s, %s; %s; %s' % (name, hyp, grade_, where, corr, arm)


def _finding_text():
    """the FINDINGS entry, composed before the root: its scores line from the scores bank alone (data/b686_rules.txt row (1)); the root is
    carried by the trail record."""
    S = jl('b689_scores.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b689_author_answers.txt'), re.M))
    c1 = _rl_lines('b689_record_lines.json') + ['?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    cj = jl('b689_corrigendum.json')
    cn = len(cj.get('bank_rows') or [])
    lb = rdn('b689_landing.txt')
    landed_ = re.search(r'LANDED (\d+) OF (\d+) DERIVES AT THE STANDARD THREE', lb)
    pr = re.search(r'BEFORE (\d+) TERMINALS ; EACH PRINTED AFTER True ; DIFFERING (\d+) ; NEW (\d+)', rdn('b689_prints_SIDE-explicit-formula.txt'))
    cs = re.search(r'ROWS (\d+) ; EQUAL OR OVERLAPPING (\d+) ;.*?n\*` (\d+)', rdn('b689_constants.txt'))
    uses = re.search(r'DISCHARGED (\d+), RE-PROVED (\d+), OBSTRUCTED (\d+)', ' '.join(rdn('b689_plan.txt').replace('###', ' ').split()))
    e = ['', _title(), '',
         'The Li converse over the widened class holds with HExcl’s half on (−1/2, 0) dropped: SIDE-explicit-formula v0.34’s '
         'Wide.li_nonneg_cfg_imp_online_ne_zero says that a configuration in the open strip (−1/2, 3/2) with no point at 0, under the local count, '
         'with every Li coefficient nonnegative, has every point on the line -- the dominant set split at w = 1 in place of the step that half '
         'closed, at the standard three, graded INTERFACES on the named premise Wide.HCount; and b688’s figure of two commit cites is corrected '
         'to three by a generated entry, and the head-line arm now reads a quote across line breaks.', '',
         '*Filed at b689 on the author’s ruling `(R299)` and the author’s words at its prompts; %d questions put. Banks: relay '
         '`data/b689_plan.txt`, `data/b689_landing.txt`, `data/b689_grade.txt`, `data/b689_constants.txt`, `data/b689_q0_reread.txt`, '
         '`data/b689_faces_rows.txt`, `data/b689_corrigendum.txt`, `data/b689_tool_repairs.txt`.*' % n_ans, '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed; %d answers checked before they were acted '
         'on. b688 at its weight (FINDINGS :%s), its head line quoted.' % (cc.group(1) if cc else '?', cc.group(2) if cc else '?',
                                                                       cc.group(3) if cc else '?', checks, c1[0]), '',
         '**The corrigendum** (`(R299)`(2)): FINDINGS :%d, generated in b678’s form -- the sentence at :9320 quoted, the figure as written two, '
         'the citation bank’s %d directly tested rows by line, the trail record’s defects line (OPEN_TRAILS :14946) the source; the sealed entry '
         'unedited, the corrigenda bank’s row (3) appended.' % (K.CORRIGENDUM_LINE, cn), '',
         '**The arm** (`(R299)`(2) and the author’s word): G-RULE-HEAD-LINE-QUOTED in tools/rule_arms.py now compares the two strings with every '
         'whitespace character and line break removed; the ruled form, one space for each run, still failed b688’s quote, broken after a hyphen '
         'by the navigator’s ferry, and was struck at the prompt. At HEAD it reads b688 OK and b689 OK, its planted case firing on both.', '',
         '**The plan** (`(R299)`(3)): section 11 of b679’s strip plan printed verbatim into the plan bank and committed alone before any row; the '
         'hypothesis set WideConfig, the local count and ρ ≠ 0 for every point; the 22 strip uses classified -- DISCHARGED %s, RE-PROVED %s, '
         'OBSTRUCTED %s; raised as one prompt before any Lean, and run as written on the author’s word.' % (
             uses.group(1) if uses else '?', uses.group(2) if uses else '?', uses.group(3) if uses else '?'), '',
         '**The build** (`(R299)`(4)): strip-free-b689 cut at v0.33’s 95f8dc8, one new file Schema/Wide/StripFree.lean; one tree state, one '
         'dispatch -- run 39255737373, its artifact verified by sha256 first, %s of %s new names DERIVES at the standard three, v0.33’s %s '
         'terminals equal by name; merged --no-ff at 8fbc27b on the gate’s reading alone, the merged tree the built tree, tagged v0.34.' % (
             landed_.group(1) if landed_ else '?', landed_.group(2) if landed_ else '?', pr.group(1) if pr else '?'), '',
         '**The grade** (`(R299)`(4)): read from the statement, banked with it verbatim before the merge -- INTERFACES on hc : HCount Z A₀, ρ ≠ 0 '
         'a domain condition; the shared E0 rule, its lexicon extended in this act’s tool alone, agreeing as the check; the salt-check passing.', '',
         '**The controls**: C2 {−1/4, 5/4}, excluded at v0.33, meets ρ ≠ 0, has its dominant point at w = 1 and λ₁ < 0; C3 records the real '
         'segment so admitted; C2b {0, 1} fails ρ ≠ 0 at 0 while every coefficient is nonnegative with 1 off the line -- b679’s lesson, that '
         'the exclusion of 0 is necessary, lives in that hypothesis. Each read from the runner’s print.', '',
         '**The constants** (`(R299)`(4)): %s of %s rows equal under the strip-free form, n*’ %s as at v0.33 -- at Q0’s bench the dominant set has '
         'no point with w = 1, its θ certified apart from 0.' % (cs.group(2) if cs else '?', cs.group(1) if cs else '?', cs.group(3) if cs else '?'), '',
         '**Q0** (`(R299)`(5)): re-read against the strip-free set -- ρ ≠ 0 holds on Z_Q(0) = −1 alone, HExcl is out of the set and the real '
         'segment no longer required, the local count derived and not compiled; the faces line untouched, its successor row drafted for b690.', '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b679’s strip plan and its controls, b676’s strip uses and b687’s '
         'status of P3, and is re-read by b690, whose reading 3 raises the faces successor row and reads P3 across every line naming T-COUNT. It '
         'strengthens the programme’s offering of the Li converse over configurations with no point at 0, the exclusion of 0 shown necessary by '
         'its control and the real segment admitted.', '',
         '**Carried to:** b690 (the reading act: the faces successor row, P3’s status, the residues, the keystone lag, the rules and arms); the '
         'kernel branches strip-free-b689 and push-b689-merge for the next ferry’s list; `W-ORD-EPSTEIN-COUNT-LEAN`; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the corrigendum generated in b678’s form by relay tools/b689_corrigendum.py, b678’s quoting helper imported unchanged, its '
              'compose (hard-coded to b676’s rows) not run; (2) the ruling’s “(−1/2, 0] half” and section 11’s “(-1/2, 0) half dropped” read as one '
              'set, section 11’s governing (relay data/b689_plan.txt == 1); (3) the split written with Finset.erase at the one w = 1 point in place '
              'of the filter lemmas section 11 names; (4) the root module left unedited, the plan’s row naming one import (relay '
              'data/b689_landing.txt); (5) the real-segment control C3 drawn on C2; (6) the faces successor keeping v0.33’s face beside the new '
              'one; (7) defect (a) counted by a transcript read the command bank now carries')


def _trail_text():
    S, J = jl('b689_scores.json'), jl('b689_act_root.json')
    fj = jl('b689_findings.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b689_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b689_record_lines.json') + ['?']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R299) ratified.** (1) b688 at its weight. (2) Defect (f) by corrigendum and the head-line arm. (3) The research question from its '
             'banks. (4) The build. (5) Q0 under the strip-free form. (6) The branches. (7) The read-first bank. (8) The draft held at v5. (9) The '
             'acts after.', '',
             '**Entered:** FINDINGS.md:%s (b688’s weight), :%d (the corrigendum), :%s (the entry); this record.' % (c1[0], K.CORRIGENDUM_LINE,
                                                                                                                 fj.get('entry_line')), '',
             '**Act root:** b689 `%s` (previous `%s`, b688’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s (relay data/b689_author_answers.txt); none after the root.' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The kernels:** SIDE-explicit-formula v0.34 (peeled 8fbc27b; relay data/b689_landing.txt, data/b689_merge_push_out.txt).', '',
             '**The route:** relay data/b689_plan.txt (section 11 first, then the plan rows); the grade relay data/b689_grade.txt; the constants relay '
             'data/b689_constants.txt.', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b689_closing.txt).', '',
             '**The open orders:** `W-ORD-CORRESPONDENCE-CARRIED-AT` (before any generator run that writes a page); `W-ORD-EPSTEIN-COUNT-LEAN` (a '
             'research act after b690); `W-ORD-LEDGER-SPLIT-RESOLVER` (on the author’s word); `W-ORD-CHAIN-PAGE-B638-CASES`; `W-ORD-PRINT-TARGETS`; '
             '`W-ORD-ONE-COPY`; `W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; `W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; `W-ORD-ROOT-BINARY-BANK`.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b689_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S, C = jl('b689_scores.json'), jl('b689_scores_close.json')
    L = ['=' * 104, 'b689 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s%s' % (
        k2, S[k2][0], S[k2][1], ('  ### AT THE CLOSE: %s -- %s' % (C[k2][0], C[k2][1])) if (S[k2][0] == 'PENDING' and C.get(k2)) else '')
        for k2 in SCORE_KEYS]
    L += [''] + rdn('b689_defects.txt').rstrip(NL).split(NL)
    put_txt('b689_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b689_scores.json', 'b689_findings.json', 'b689_trail.json', 'b689_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b689_record_lines.json') + ['?']
    L = ['b689 -- THE COMPONENTS, BANKED UNDER (R299).', '',
         '### COMPONENT 0 : the citation check (data/b689_citation_check.txt), step zero (data/b689_ferry.txt, data/b689_readfirst.txt, '
         'data/b689_stepzero.txt, data/b689_tests_stepzero.txt, data/b689_rowgen_stepzero.txt, data/b689_branches.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b688`s weight FINDINGS :%s ; the corrigendum FINDINGS :%d (data/b689_corrigendum.txt) ; the arm (data/b689_tool_repairs.txt)' % (
             c1[0], K.CORRIGENDUM_LINE),
         '### COMPONENT 2 : the plan (data/b689_plan.txt), section 11 first, the prompt and the author`s word ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the build (data/b689_runner_SIDE-explicit-formula_run1.txt, data/b689_landing.txt), the grade (data/b689_grade.txt), '
         'SIDE-explicit-formula v0.34, the constants (data/b689_constants.txt) ; N3 %s ; N4 %s' % (S['N3'][0], S['N4'][0]),
         '### COMPONENT 4 : Q0 re-read (data/b689_q0_reread.txt), the faces successor row held (data/b689_faces_rows.txt)',
         '### COMPONENT 5 : the carry-time reading (data/b689_tool_repairs.txt), the dry-run steps (data/b689_reg_gate.txt), the seal '
         '(data/b689_seal_hashes.json), the suite in four parts ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('b689_components.txt', L)
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
    if not os.path.isfile(os.path.join(D, 'b689_scores.json')):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, 'b689_findings.json', dict(title=t))
    j = jl('b689_findings.json')
    j['entry_line'] = ln
    put_json('b689_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b689_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


FACE_REL = 'data/b689_registration_2026-10-19.txt'
FACE = os.path.join(D, 'b689_registration_2026-10-19.txt')


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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b689_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b689_regspec.py')], 'b689_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b689_satisfiable.json', '--emit', 'b689'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b689_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b689_census_stepzero.txt'), ('b327_faces_census.py', 'b689_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b689_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b689'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b689_reg_gate.txt', 'data/b689_reg_termscan.txt', 'data/b689_regspec_run.txt', 'data/audit_b689_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b688's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '2026-10-19-b689'
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
    put_json('b689_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b689':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b689`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b689_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b689_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b689_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b689 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b689 (the last export b688`s, D:/MY-DOwnloads/mirror-refresh-2026-10-19-b688.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b689_mirror.txt', L)
    put_json('b689_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


# ================================================================================ THE CARRY-TIME READING (the ferry's Component 5)
REPAIRS = [
    ('THE HEAD-LINE ARM (answering b688`s declared failure and this act`s defect (c), the navigator`s): tools/rule_arms.py :387-:393, in the',
     'author`s form at the prompt -- every whitespace character and line break removed from both strings, no space retained; the rows (1) above',
     'carry its diff, its readings and the author`s word. The shared tool sealed with the act (tools/b689_worklist.py SEALED), so N5 reads its',
     'hash at the close; it leaves INST (the instruments read unedited) for REPAIRED_TOOLS.'),
    ('THE STANDING SET FOR b689 (answering no defect: the act`s objects): the standing arms are b688`s face`s (G2) arms less b688`s act arms,',
     'the twenty rule arms among them, no standing arm added; the runner arms read this act`s run (39255737373) and its merge (8fbc27b, v0.34)',
     'on SIDE-explicit-formula alone; the step-zero arms read ten branches in four repositories, every one local -- G-BRANCHES-DELETED reads',
     'the local lists, the recut branches standing at their remotes as the ruling names no remote branch; the count arms` floors are this',
     'act`s (two prompts in two calls, two mid-act checks, the defects as lettered at the seal).'),
    ('THE STEP-ZERO TESTS` SET (answering the carried argument of row (2)): G-STEPZERO-TESTS reads the step-zero bank`s failing set --',
     'test_chain_page.py (1), (9), (14) against b680`s list as carried, test_chain_page_b638.py (4)-(7) -- and the re-run against the list',
     'the page names, data/b689_tests_b688list.json, test_chain_page.py (9) alone, the standing case since b638.'),
    ('THE FACES PAGE BACK AMONG THE FILES READ UNEDITED (answering no defect: (R299)(5) leaves the page untouched): CURRENTS regains',
     'THE_CLAUSE_AND_ITS_COMPILED_FACES.md, which b688 took out to regenerate it; G-PP-SCOPE allows FINDINGS and OPEN_TRAILS alone',
     '(tools/b689_worklist.py PP_WRITTEN).'),
    ('THE PREVIOUS ACT`S WINDOW IN ITS OWN SESSION (answering no defect: this act opens a new session): G-EDIT-ROUTE`s previous-act window,',
     'b687`s repair, read b688`s capture after its post-push suite in this same session; b688 ran in session a90bcdb6 and this act in',
     '2c300355, so `prev_capture` reads a90bcdb6 from b688`s post-push combine to that session`s end (tools/b689_record.py), and the',
     'command bank names the redirects onto /dev/null beside the edit route`s offences (defect (a)), no arm reading them.'),
    ('G-WORKFLOW-FILES READ AGAINST THE MAIN BEFORE THE ACT (answering no defect: a kernel whose workflow the act did not write): b688`s',
     'predicate compared each merged kernel`s workflow with the workflow at its own first commit, true of SIDE-li-map`s, written at b688;',
     'SIDE-explicit-formula`s workflow (7317db4, b654) took a later edit (f18ab7e, b658) before this act, so the first commit is not its state',
     'before the act. b689`s `wf_state` reads the workflow at the main before the act where the act wrote none -- b679`s reading of this',
     'kernel (tools/b679_checks.py `wf_state`, W_PRE_MAIN) -- and at its first commit where the act wrote it. Found by the pre-run.'),
]
CARRY_HEAD = '### THE CARRY-TIME READING OF THE TOOLS (the ferry`s Component 5), AGAINST b688`S SEALED COPIES'


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


def repairs(*a):
    """the carry-time section of data/b689_tool_repairs.txt: each tool carried from a sealed b688 copy read against b688's seal hash first and
    its diff counted by hunks; the standing instruments read against the last seal record naming them; the repaired readings' diffs against
    b688's sealed copies printed whole. The bank's rows (1)-(3), written by the Write and Edit tools before, are kept as they stand: the route
    replaces only its own section, from its head line to the bank's end."""
    import difflib
    import hashlib
    seal = jl('b688_seal_hashes.json').get('tools') or {}
    rows = []
    for t0 in ('b688_citation.py', 'b688_closing.py', 'b688_reg_gate.py', 'b688_regspec.py', 'b688_tests.py', 'b688_worklist.py',
               'b688_record.py', 'b688_checks.py'):
        t1 = t0.replace('b688_', 'b689_')
        old, new = os.path.join(T, t0), os.path.join(T, t1)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        ex = os.path.exists(new)
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8',
                           errors='replace').stdout if ex else ''
        rows.append((t0, t1, now, seal.get(t0), len(re.split(r'(?m)^(?=@@ )', d)[1:]), ex))
    inst = {}
    for t in ('rule_arms.py', 'edit_route.py', 'e0_rule.py', 'b678_corrigendum.py'):
        nowh = hashlib.sha256(open(os.path.join(T, t), 'rb').read()).hexdigest()
        acts = [x for x in ('b688', 'b687', 'b686', 'b685', 'b684', 'b683') if (jl('%s_seal_hashes.json' % x).get('tools') or {}).get(t)]
        headh = hashlib.sha256(subprocess.run(['git', '-C', ROOT, 'show', '%s:tools/%s' % (K.PRE_RELAY, t)], capture_output=True).stdout).hexdigest()
        inst[t] = (nowh, acts[0] if acts else None, (jl('%s_seal_hashes.json' % acts[0])['tools'][t]) if acts else None, headh,
                   g(ROOT, 'log', '-1', '--format=%h %cI', '--', 'tools/' + t).strip())
    s8r, s9r = rd(os.path.join(T, 'b688_record.py')), rd(os.path.join(T, 'b689_record.py'))
    s8c, s9c = rd(os.path.join(T, 'b688_checks.py')), rd(os.path.join(T, 'b689_checks.py'))
    nd = []
    for (a8, f8), (a9, f9), s8, s9 in ((('b688_record.py', 'prev_capture'), ('b689_record.py', 'prev_capture'), s8r, s9r),
                                       (('b688_checks.py', 'tests_ok'), ('b689_checks.py', 'tests_ok'), s8c, s9c),
                                       (('b688_checks.py', 'branches_ok'), ('b689_checks.py', 'branches_ok'), s8c, s9c),
                                       (('b688_checks.py', 'wf_state'), ('b689_checks.py', 'wf_state'), s8c, s9c)):
        nd += list(difflib.unified_diff(_fn_src(s8, f8).split(NL), _fn_src(s9, f9).split(NL) if s9 else [],
                                        '%s %s (sealed)' % (a8, f8), '%s %s%s' % (a9, f9, '' if s9 else ' (NOT YET CARRIED)'), n=1, lineterm=''))
    for c in ('CURRENTS', 'STEPZERO_FAILING'):
        nd += list(difflib.unified_diff(_const_src(s8c, c).split(NL), _const_src(s9c, c).split(NL), 'b688_checks.py %s (sealed)' % c,
                                        'b689_checks.py %s' % c, n=1, lineterm=''))
    L = [CARRY_HEAD + ' (%s)' % utc(), '',
         '### rows are repairs with the defect they answer, after the carried tools: b688`s sealed copy and its seal record; the hunks of the diff',
         '### to b689`s copy. Every hunk is the act`s own text -- its names, its banks, its sections and its predicates over this act`s banks --',
         '### save the repairs below.', '']
    for t0, t1, now, s, nh, ex in rows:
        L.append('  %-20s -> %-20s b688 sealed %s ; the seal`s record %s ; %s ; hunks %s' % (t0, t1, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh if ex else 'NOT YET CARRIED'))
    for t, (nowh, act, sh, headh, last) in inst.items():
        rep = t in K.REPAIRED_TOOLS
        L.append('  %-20s    %s: %s ; at relay %s %s ; the last seal record naming it (%s`s) %s ; its last commit %s' % (
            t, 'THE REPAIRED SHARED TOOL, sealed with this act' if rep else 'the standing instrument, unedited in this act', nowh[:16], K.PRE_RELAY,
            headh[:16], act or 'NONE', (sh or '### NONE')[:16], last))
    L.append('')
    for i, r in enumerate(REPAIRS, 1):
        L += ['  REPAIR %d -- %s' % (i, r[0])] + ['  ' + x for x in r[1:]]
    L += ['', '### THE DIFF OF THE REPAIRED READINGS AGAINST b688`S SEALED COPIES (tools/b688_record.py sha256 %s, tools/b688_checks.py sha256 %s), '
          'WHOLE:' % ((seal.get('b688_record.py') or '### NONE')[:16], (seal.get('b688_checks.py') or '### NONE')[:16])]
    L += ['    ' + l for l in nd]
    carried = sum(1 for r in rows if r[5])
    unedited = all(v[0] == v[3] for t, v in inst.items() if t not in K.REPAIRED_TOOLS)
    L += ['', '### ### **REPAIRS %d ; THE SEALED COPIES %s ; TOOLS CARRIED %d OF %d ; THE STANDING INSTRUMENTS UNEDITED %s ; THE REPAIRED SHARED '
          'TOOL 1 ; THE REPAIRED READINGS` DIFF LINES %d.**' % (
              len(REPAIRS), 'AGREE' if all(s == now for _a, _b, now, s, _n, _e in rows) else '### DIFFER', carried, len(rows), unedited, len(nd))]
    old = rdn('b689_tool_repairs.txt')
    keep = old[:old.index(CARRY_HEAD)].rstrip(NL) if CARRY_HEAD in old else old.rstrip(NL)
    put_txt('b689_tool_repairs.txt', keep.split(NL) + ['', ''] + L)
    print(L[-1])


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, armread=armread, answers=answers, runner=runner, prints=prints, grade=grade,
              commands=commands, defects=defects, repairs=repairs, kernels=kernels, rootbanks=rootbanks, root=root, root_arm=root_arm,
              table_final=table_final, scores=scores, desk=desk, components=components, findings=findings, trail=trail, drycheck=drycheck,
              gatebanks=gatebanks, mbuild=mbuild, mroot=mroot, mverify=mverify, mbank=mbank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b689_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
