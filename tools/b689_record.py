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


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, armread=armread, answers=answers, runner=runner, prints=prints, grade=grade)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b689_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
