# -*- coding: utf-8 -*-
"""b693_record.py -- THE ACT'S RECORD TOOL, b693 under (R303).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b693's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b692_record.py in stages: the helpers, the guarded landing, the readers, step zero's rowgen and branches
### routes and the answers route first; Component 1's weight line and corrigendum at Component 1; the cut routes at Component 2; the late
### routes at Component 4. Every python child is started as `python -X utf8`, no environment mapping passed. Routes:
### `python tools/b693_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail are read
### (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
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
import b693_worklist as K          # noqa: E402

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
        'b693_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b693_findings.json': dict(entry_line=99999, title='stand-in'),
        'b693_trail.json': dict(line=99999),
        'b693_act_root.json': dict(root='0' * 64, previous='f0fd2849' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b693's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b693_scanfile_%s.md' % tag)
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
    """a row of data/b693_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
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
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b693_rowgen_<stage>.txt."""
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
    L = ['b693 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b693_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R303)(5))
def branches(*a):
    """every branch (R303)(5) names for step zero, its tip read before any delete, whether --merged lists it, its fate DELETED; any branch of
    b692 that --merged lists and the ruling does not name, reported and KEPT. data/b693_branches.txt (.json)."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    named = set((r['repo'], r['branch']) for r in rows)
    extra = []
    for repo in sorted(set(r_ for r_, _bs in K.DELETE)):
        for x in g(repo, 'branch', '--merged', 'main', '--format=%(refname:short)').split(NL):
            x = x.strip()
            if (x.startswith('push-b692') or x.endswith('-b692')) and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    L = ['b693 -- STEP ZERO, (R303)(5): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; merged into main ; fate. The eight named deleted by name in the house',
         '### form after --merged lists each, each delete command naming one branch with no glob in any half, one command per message, in sequence.', '',
         '### THE EIGHT (R303)(5) NAMES:']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### branches of b692 that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **NAMED %d (MERGED %d) ; UNNAMED OF b692 %d.**' % (len(rows), sum(1 for r in rows if r['merged']), len(extra))]
    put_txt('b693_branches.txt', L)
    put_json('b693_branches.json', dict(at=utc(), rows=rows, extra=[list(x) for x in extra]))
    print(NL.join(L[5:]))


# ================================================================================ THE ANSWERS BANK (b692's route, carried)
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
    """data/b693_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
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
    head = ['### b693 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b693_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b693_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R303)(1)
WH = ('*Appended 2026-10-19 by b693 to b692’s entry (:9462), under `(R303)`(1) -- b692 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b692_closing.txt):*')
WB = (' “b692 closed: relay cb41d267, PLACE-papers 62b632f; suite 123 of 123; root f0fd28492c58f143…; 4 prompts answered; 13 defects” '
      '(data/b692_closing.txt :1), the closing 1749abbb pushed and read back at relay main (data/b692_closing_push_out.txt). The suite 123 of 123 '
      'before and after the push, every control behaving (data/b692_checks.txt, data/b692_checks_postpush.txt); the eight scores HELD '
      '(data/b692_scores_close.json); the root f0fd2849 over 88 banks (data/act_roots.txt, data/b692_act_root.json); the entry at FINDINGS '
      ':9462, the trail at OPEN_TRAILS :15110 carrying the root; the face locked after the gate CLEAR and the lock gate’s 8 of 8, no arm '
      'declared failing (data/b692_reg_gate.txt, data/b692_lockgate_notes.txt :65); the sealed tools 12 of 12 at the close (data/b692_closing.txt '
      ':18); mirror-refresh-2026-10-19-b692.zip CLEAN with the root line (data/b692_mirror_verify.txt, data/b692_mirror.txt); the scratch branch '
      'circuit-shorts-control-b692 deleted local and remote, the local delete by -D, the branch merged at no point (data/b692_closing.txt :224). '
      'The dependency-circuit reading at SIDE-explicit-formula v0.34.1: CLAUSE-DOMINANCE 1 of 1 faces kernels reached, SIDE-explicit-formula '
      'IN, the clause’s face in the closures of 2 of the 9 faces the page names, SIDE-lv-conservation not reached and carried to b694 '
      '(data/b692_circuit_dominance.txt :21, data/b692_closure_step.txt); SERIES of h2_sign_iff_rh 576 names, the longest chain 26; SHORTS 0; '
      'WIDTH 41 same-type theorem pairs, 25 meeting in at most FEW = 5 names; LOAD led by Zeta23.reflect (825), Zeta23.ZeroConfig.mk (716) '
      'and Zeta23.ZeroConfig (716) (data/b692_circuit_SIDE-explicit-formula_v0.34.1.txt :707); READFIRST-CLOSURE against the hand list, 23 '
      'lines differ (data/b692_readfirst_diff.txt :31); SUITE-LOAD, 11 of 24 rule arms reading a source defect, the factor 1.53 '
      '(data/b692_suite_load.txt :59); the tenth row in data/b692_circuit_spec.txt :46. The triage, on the author’s answer amending the '
      'ruling’s figures (data/b693_author_answers.txt, prompt 1): the classes as triaged CARRY 11, DISCHARGED-BY-READING 24, RETIRE 0 '
      '(data/b692_triage_counts.txt :6); the entries as written CARRIED 12, DISCHARGED BY READING 23, RETIRED 0 (OPEN_TRAILS :15040-:15108), '
      'one row demoted, W-ORD-PROBE-HOLD, on the author’s check because its reading cites a tool by path and line (tools/chain_page.py :919) and '
      'no bank (OPEN_TRAILS :15088). Thirteen defects (data/b692_defects.txt :5-:60): (a) a listing read through a shell filter; (b) the closure '
      'script’s first form refused on the runner; (c) its second form under the heartbeat ceiling; (d) the reader’s first forms; (e) a file '
      'write routed through git’s own option; (f) the citation check’s own row; (g) the ferry bank’s first write; (h) the corrigendum route’s '
      'first dry; (i) the shorts branch pushed outside the push tool, a ruled exception on the author’s word; (j) the navigator’s, the parts '
      'repair as worded unable to meet its own test; (k) the navigator’s, h2_sign_iff_rh not on the print list; (l) a score read through an '
      'interpreter’s print before the lock; (m) two needles of the sealed record tool mis-reading their banks, its two figures entered by the '
      'corrigendum beneath. The closing record’s carried-forward row (i) reads “(a)-(k)”, a fixed string in the closing tool '
      '(data/b692_closing.txt :258, tools/b692_closing.py :115), repaired at this act’s carry. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b693_record_lines.json', 'c1', entry=K.B692_ENTRY,
         check=[('FINDINGS.md', K.B692_ENTRY, '## The dependency-circuit reading at SIDE-explicit-formula v0.34.1'),
                ('OPEN_TRAILS.md', K.B692_TRAIL, '### b692')], dry=dry)


# ================================================================================ COMPONENT 2: THE NAMING, (R303)(3) (b691's tie route, carried)
LICENSED_NOW = 'b690_r3_licensed.txt'      # ### reading 3's per-document rows, b648 -> b680 -> b690
KROW = re.compile(r'^  (SIDE-[\w-]+) docstrings \(read at (\w+)\)\s+(\d+) ->\s+(\d+) ->\s+(\d+)\s+\[(.*?)\]')


def tie(*a):
    """data/b674_rules.txt row (2) printed verbatim (:8-:11) and b652's order (data/b652_ferry.txt :19) verbatim; then every kernel row of
    reading 3's licensed table (relay data/b690_r3_licensed.txt, b648 -> b680 -> b690) by line, each kernel cut since b690 replaced by its cut
    bank's line (b691: SIDE-rcurve, data/b691_cut.txt :33); the kernels by descending count; the tie rule applied only where two stand at the
    top count; and only then the document named. data/b693_tie.txt (.json)."""
    rl = rdn('b674_rules.txt').split(NL)[7:11]
    if not rl or not rl[0].startswith('  (2) THE TIE-BREAK BEYOND THE COUNT'):
        sys.exit('### data/b674_rules.txt :8 DOES NOT CARRY ROW (2) -- NOTHING WRITTEN')
    order = rdn('b652_ferry.txt').split(NL)[18]
    if 'the next kernel by descending count' not in order:
        sys.exit('### data/b652_ferry.txt :19 DOES NOT CARRY b652`s ORDER -- NOTHING WRITTEN')
    lt = rdn(LICENSED_NOW).split(NL)
    cb = rdn('b691_cut.txt').split(NL)
    rc_ = re.search(r'SIDE-rcurve RE-CUT: THE DISTANCE BEFORE (\d+), AFTER (\d+)', cb[32] if len(cb) > 32 else '')
    if not rc_:
        sys.exit('### data/b691_cut.txt :33 DOES NOT CARRY SIDE-rcurve`s DISTANCE -- NOTHING WRITTEN')
    rows = []
    for i, l in enumerate(lt, 1):
        m = KROW.match(l)
        if m:
            k, now, src = m.group(1), int(m.group(5)), 'relay data/%s :%d' % (LICENSED_NOW, i)
            if k == 'SIDE-rcurve':
                now, src = int(rc_.group(2)), 'relay data/b691_cut.txt :33 (cut at b691, THE DISTANCE BEFORE %s, AFTER %s)' % rc_.groups()
            rows.append(dict(kernel=k, line=i, row=l.strip(), now=now, source=src, table=m.group(6).split(' ')[0].replace('data/', '')))
    rows.sort(key=lambda r: -r['now'])
    top = [r for r in rows if r['now'] == rows[0]['now']] if rows and rows[0]['now'] > 0 else []
    named = top[0] if len(top) == 1 else None
    vl = ''
    if named:
        t = rdn(named['table'])
        vl = ([x for x in t.split(NL) if x.startswith('### ### **%s: ROWS' % named['kernel'])] or [''])[0]
    L = ['b693 -- COMPONENT 2, (R303)(3): THE LICENSED TABLE`S NEXT DOCUMENT, b652`S ORDER AND b674`S TIE-BREAK RULE PRINTED BEFORE IT IS NAMED (%s)' % utc(), '',
         '### b652`S ORDER, VERBATIM FROM relay data/b652_ferry.txt :19:', '    ' + order, '',
         '### b674`S TIE-BREAK RULE, VERBATIM FROM relay data/b674_rules.txt :8-:11:'] + ['  ' + l for l in rl] + [
         '', '### THE KERNEL ROWS, VERBATIM (reading 3, relay data/%s, b648 -> b680 -> b690), A KERNEL CUT SINCE b690 BY ITS CUT BANK; rows are'
         % LICENSED_NOW, '### kernels: the count now | the row | the source of the count now, in descending count:']
    L += ['  %3d | %s | %s' % (r['now'], r['row'], r['source']) for r in rows]
    L += ['', '### THE ORDER APPLIED: the top count %s ; the kernels standing at it %s ; b674`s rule %s' % (
        rows[0]['now'] if rows else '### NONE', [r['kernel'] for r in top] or 'NONE',
        'NOT REACHED (one document at the top count, no tie)' if len(top) == 1 else ('REACHED: %d documents tied -- raised' % len(top))),
          '### the named document`s table (relay data/%s): %s' % (named['table'], vl) if named else '### NO DOCUMENT NAMED',
          '', '### ### **THE NEXT DOCUMENT BY b652`S ORDER: %s AT %s, ALONE AT THE TOP COUNT ; b674`S TIE-BREAK NOT REACHED.**' % (
              named['kernel'], named['now']) if named else '### ### **NO DOCUMENT NAMED -- RAISED.**']
    put_txt('b693_tie.txt', L)
    put_json('b693_tie.json', dict(at=utc(), rule=rl, order=order, rows=rows, named=named['kernel'] if named else None))
    print(NL.join(L))


# ================================================================================ THE DISPATCH, THE RUNS AND THE PRINTS (b692's and b691's routes, carried)
STD3 = ('Classical.choice', 'Quot.sound', 'propext')


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def dispatch(*a):
    """`dispatch <kernel> <ref sha> <label> <target> [dry]`: ONE dispatch of build-module.yml at main with the ref input and the lake target;
    refused where data/b693_dispatches.json already carries the ref's tree (one dispatch per tree state). The run id read from the run list
    (the newest workflow_dispatch run created after the dispatch); a row banked."""
    kernel, ref, label, target = a[0], a[1], a[2], a[3]
    repo = 'psinary-sketch/' + kernel
    full = g('D:/' + kernel, 'rev-parse', ref).strip()
    tree = g('D:/' + kernel, 'rev-parse', full + '^{tree}').strip()
    j = jl('b693_dispatches.json') if os.path.isfile(os.path.join(D, 'b693_dispatches.json')) else {}
    rows = j.get('rows') or []
    seen = [r for r in rows if r.get('tree') == tree]
    if seen:
        sys.exit('### THE TREE %s IS ALREADY BUILT (run %s) -- NOT DISPATCHED' % (tree[:12], seen[0].get('run_id')))
    if not re.match(r'^[A-Za-z0-9_. ]+$', target):
        sys.exit('### THE TARGET %r IS OUTSIDE THE LAKE GRAMMAR -- NOT DISPATCHED' % target)
    print('  kernel %s ; ref %s ; tree %s ; target %s' % (kernel, full, tree, target))
    if 'dry' in a[4:]:
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
    rows.append(dict(kernel=kernel, label=label, ref=full, tree=tree, target=target, dispatched=t0, run_id=run_id))
    put_json('b693_dispatches.json', dict(rows=rows))
    print('  dispatched %s ; run id %s' % (t0, run_id))


def _deps(ax):
    """the axioms output read per terminal: [(name, [axioms] or None for 'does not depend on any axioms')], wrapped lists rejoined."""
    out = []
    for n, d in re.findall(r"^'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)",
                           re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', ax), re.M):
        out.append((n, [x.strip() for x in d.split('[', 1)[1].rstrip(']').split(',') if x.strip()] if d.startswith('depends') else []))
    return out


def read_runner_row(r):
    """a row of data/b693_runner_rows.json: the kernel, its label, the ref (40 hex), the run id and the gate; returns (kernel, label, gate)."""
    if not isinstance(r, dict) or not re.match(r'^SIDE-[\w-]+$', r.get('kernel') or '') or not re.match(r'^[\w-]+$', r.get('label') or '') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['kernel'], r['label'], r['gate']


READERS.append('read_runner_row')


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <note...>`: the kernel's run read by its id; the artifact listed, downloaded by its id into
    memory, its sha256 against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP;
    the axioms output of the print step banked whole, every name of the list matched to one printed line, each terminal's axioms read against
    the standard three. data/b693_runner_<kernel>_<label>.txt, data/b693_axioms_<kernel>_<label>.txt and a row of data/b693_runner_rows.json."""
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
    L = ['b693 -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (kernel, label.upper(), utc()), '',
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
    put_txt('b693_runner_%s_%s.txt' % (kernel, label), L)
    if row['artifact_sha256']:
        put_txt('b693_axioms_%s_%s.txt' % (kernel, label), ax.split(NL) if ax else ['### EMPTY'])
        put_txt('b693_buildlog_%s_%s.txt' % (kernel, label), blog.rstrip(NL).split(NL))
    j = jl('b693_runner_rows.json') if os.path.isfile(os.path.join(D, 'b693_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('b693_runner_rows.json', dict(rows=rows))
    print(NL.join(L[:14] + L[-3:]))


def prints(*a):
    """`prints <kernel> <before bank> <after bank>`: the 'before' terminals' printed lines compared with the same names' lines in the 'after'
    bank, line for line by name; the raw axioms banks compared byte for byte beside. data/b693_prints_<kernel>.txt."""
    kernel, bb, ab = a[0], a[1], a[2]
    b, f = rdn(bb), rdn(ab)
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bd, fd = dict(_deps(b)), dict(_deps(f))
    diff = [(n, bd[n], fd.get(n)) for n in bd if fd.get(n) != bd[n]]
    new = [n for n in fd if n not in bd]
    L = ['b693 -- THE PRINTS OF %s BEFORE AND AFTER THE CUT, BY NAME AND LINE FOR LINE (%s)' % (kernel, utc()), '',
         '### before: relay data/%s (%d terminals) ; after: relay data/%s (%d terminals) ; the two banks equal line for line: %s ; rows are the '
         'terminals that differ:' % (bb, len(bd), ab, len(fd), b == f)] + (['    %s : %s | %s' % d for d in diff] or ['    NONE']) + [
        '### the names printed after and not before: %d' % len(new)] + ['    %s %s' % (n, fd[n]) for n in new]
    L += ['', '### ### **BEFORE %d TERMINALS ; EACH PRINTED AFTER %s ; DIFFERING %d ; NEW %d ; EQUAL LINE FOR LINE %s.**' % (
        len(bd), all(n in fd for n in bd), len(diff), len(new), b == f)]
    put_txt('b693_prints_%s.txt' % kernel, L)
    print(L[-1])


# ================================================================================ COMPONENT 2: THE QUOTATION SEARCH, data/b690_rules.txt row (2) (b691's route, carried)
# ### one distinctive substring per removed or changed line of the cut, each checked to stand in its own removed line before it is searched
QUOTE_NEEDLES = ('The Archimedean / √ IDENTIFICATION', 'An IDENTIFICATION kernel — same', 'status as Voice1 (Euler balance)',
                 'verifies the Archimedean machinery', 'POINTS at σ = 1/2. It does NOT prove RH', 'the exhaustive mechanism catalogue',
                 'The path: n² → θ(τ)', '→ Focus (ξ real on the', 'critical line, codim 2 → 1)', 'the Archimedean functional-equation',
                 'structure forces σ = 1/2')
# ### the second shape, case-blind and shorter (b690's lesson: a case-exact needle misses a quote re-set in bold or another case), one per
# ### removed line by case-blind containment; both shapes' yields printed
QUOTE_WIDE = ('archimedean / √ identification', 'identification kernel — same', 'Voice1 (Euler balance)', 'Archimedean machinery',
              'prove RH on its own', 'exhaustive mechanism catalogue', '√ transformation θ(−1/τ)', 'focus (ξ real', 'codim 2 → 1',
              'archimedean functional-equation', 'structure forces')
QUOTE_SETS = {'quote_archimedean': (QUOTE_NEEDLES, QUOTE_WIDE)}


def quote(*a):
    """`quote <kernel dir> <base> <tip> <bank stem>`: every line the cut removes or changes (the `-` lines of git diff base..tip, comments
    alone) read, one needle of the set assigned to each by containment and refused where a removed line carries none or a needle stands
    in no removed line; each needle searched with git grep -n -F at the tip across the kernel's whole tracked tree, in two shapes; every hit
    printed with its quoting line and entered as a residue; the control at the base. data/b693_<stem>.txt (.json)."""
    kd, base, tip, stem = a[0], a[1], a[2], a[3]
    needles, wide = QUOTE_SETS[stem]
    d = g(kd, 'diff', '--unified=0', base, tip)
    removed = [l[1:].rstrip(chr(13)) for l in d.split(NL) if l.startswith('-') and not l.startswith('---')]
    removed = [l for l in removed if l.strip()]
    rows, unassigned = [], []
    for l in removed:
        nd = [n for n in needles if n in l]
        if not nd:
            unassigned.append(l)
        rows.append(dict(line=l, needle=nd[0] if nd else None))
    unused = [n for n in needles if not any(n in r['line'] for r in rows)]
    if unassigned or unused:
        sys.exit('### A REMOVED LINE WITHOUT A NEEDLE %s OR A NEEDLE IN NO REMOVED LINE %s -- NOTHING WRITTEN' % (unassigned, unused))
    for r in rows:
        w = [n for n in wide if n.lower() in r['line'].lower()]
        r['wide'] = w[0] if w else None
    wu = [n for n in wide if not any(n.lower() in r['line'].lower() for r in rows)]
    if any(r['wide'] is None for r in rows) or wu:
        sys.exit('### THE SECOND SHAPE: A REMOVED LINE WITHOUT A NEEDLE OR A NEEDLE IN NO REMOVED LINE %s -- NOTHING WRITTEN' % wu)
    hits = []
    for r in rows:
        out = g(kd, 'grep', '-n', '-F', r['needle'], tip, '--')
        r['hits'] = [x for x in out.split(NL) if x.strip()]
        out2 = g(kd, 'grep', '-n', '-i', '-F', r['wide'], tip, '--')
        r['hits_wide'] = [x for x in out2.split(NL) if x.strip()]
        hits += [(r['wide'], h) for h in r['hits_wide']]
    L = ['b693 -- THE QUOTATION SEARCH BEFORE THE MERGE, data/b690_rules.txt row (2), OVER %s (%s)' % (os.path.basename(kd), utc()), '',
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
    put_txt('b693_%s.txt' % stem, L)
    put_json('b693_%s.json' % stem, dict(at=utc(), kernel=kd, base=base, tip=tip, rows=rows, hits=[list(h) for h in hits]))
    print(NL.join(L))


# ================================================================================ COMPONENT 2: THE CUT BANK, (R303)(3) (b691's route, carried)
CUT = dict(kernel='SIDE-archimedean', table='b647_table_SIDE-archimedean.txt', base='8019d9d', main='fcecc45', tip='2bd9cc8', tag='v0.1.1',
           prior='v0.1.0', workflow='79a8527', targets='7769d0e', before=39360158384, after=39360543605)
# ### each quoting line's reading, by hand after the search (data/b693_quote_archimedean.txt): (file, line) -> its disposition
RESIDUE_READ = {
    ('README.md', 15): 'CARRIED -- a README line quoting the removed headline docstring ("the Archimedean FE structure forces sigma = 1/2"), '
                       'outside the docstring rows the cut reaches; trigger: the next re-cut of SIDE-archimedean or a README pass',
    ('README.md', 19): 'CARRIED -- a README line quoting the removed header ("verifies the Archimedean machinery *points at* sigma = 1/2", the '
                       'status as Voice1, the exhaustive mechanism catalogue), outside the docstring rows the cut reaches; trigger: the next '
                       're-cut of SIDE-archimedean or a README pass',
    ('SIDEArchimedean/Reflection.lean', 39): 'CARRIED AS IT STANDS -- the T3 block`s own kept line (its "(codim 2 → 1)" the defined count), a '
                                             'MATCHES row at b647 (data/b647_table_SIDE-archimedean.txt :25, Reflection.lean :40 at 8019d9d), '
                                             'not a quote of the removed claim; the second shape`s needle "codim 2 → 1" meets it',
}


def _norm(t):
    return ' '.join(t.replace('--', ' ').replace('—', ' ').split())


def cut(*a):
    """data/b693_cut.txt (.json): the document named by data/b693_tie.txt; the commits on its main (the workflow and the print list alone, the
    cut on recut-archimedean-b693, the merge, the tag); the before and after runs and the prints; the distance before and after by the b670
    method -- each non-MATCHES row of its b647 table read whole, its ACTION's text (the words after `RE-CUT:`) searched, whitespace normalized,
    in the file at the merge; the quotation search's quoting lines each entered as a residue with its line and its reading; the generator's
    dry reading (cells held); the :301 residue read where the cut document carries it."""
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
    q = jl('b693_quote_archimedean.json')
    qlines = sorted(set((h.split(':')[1], int(h.split(':')[2]), h.split(':', 3)[3]) for _n, h in q.get('hits') or []), key=lambda x: (x[0], x[1]))
    unread = [(f, ln) for f, ln, _t in qlines if (f, ln) not in RESIDUE_READ]
    if unread:
        sys.exit('### A QUOTING LINE WITHOUT ITS HAND READING %s -- NOTHING WRITTEN' % unread)
    tie_v = vl_ = ([x for x in rdn('b693_tie.txt').split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]
    cd = ([x for x in rdn('b693_correspondence_dry.txt').split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]
    tag_peel = g(kd, 'rev-parse', CUT['tag'] + '^{commit}').strip()
    prior_peel = g(kd, 'rev-parse', CUT['prior'] + '^{commit}').strip()
    mt, tt = g(kd, 'rev-parse', CUT['main'] + '^{tree}').strip(), g(kd, 'rev-parse', CUT['tip'] + '^{tree}').strip()
    L = ['b693 -- COMPONENT 2, (R303)(3): THE RE-CUT OF %s, ITS DISTANCE, ITS RESIDUES (%s)' % (k, utc()), '',
         '### the document: %s, named by b652`s order alone at the top count (relay data/b693_tie.txt: %s)' % (k, tie_v.strip('#* ')),
         '### the commits on its main: the workflow %s alone, the print list %s alone (the Mathlib form, carried from SIDE-rcurve`s bb14e89); the cut %s'
         % (CUT['workflow'], CUT['targets'], CUT['tip']),
         '### on recut-archimedean-b693 (comments only: the module header and the headline docstring, the two ACTIONs verbatim), pushed alone by',
         '### push_gated`s branch mode named --scratch (relay data/b693_archimedean_cut_push_out.txt); the merge %s by --no-ff, the merged tree %s the'
         % (CUT['main'], mt[:12]),
         '### built tree %s (%s); the tag %s peeled to %s, its message naming the prior tag %s = %s (relay data/b693_archimedean_merge_push_out.txt)' % (
             tt[:12], 'EQUAL' if mt == tt else '### DIFFER', CUT['tag'], tag_peel[:12], CUT['prior'], prior_peel[:7]),
         '### the runs: before %d at main %s, after %d at the tip %s, both DERIVES 5 of 5 at the standard three; the prints equal line for line'
         % (CUT['before'], CUT['targets'], CUT['after'], CUT['tip']),
         '### (relay data/b693_runner_SIDE-archimedean_before.txt, _after.txt, data/b693_prints_SIDE-archimedean.txt)', '',
         '### THE DISTANCE BY THE b670 METHOD: each non-MATCHES row of relay data/%s, its ACTION`s text searched in the file at %s:' % (CUT['table'], CUT['main'])]
    L += ['  %s | %s | ACTION applied %s | %s' % (r['row'], r['verdict'], r['applied'], r['action'][:100]) for r in rows]
    L += ['', '### THE RESIDUES (data/b690_rules.txt row (2); relay data/b693_quote_archimedean.txt, two shapes): each quoting line, the line verbatim,',
          '### its reading by hand:']
    L += ['  R-%d  %s :%d | %s | %s' % (i, f, ln, RESIDUE_READ[(f, ln)], t[:180]) for i, (f, ln, t) in enumerate(qlines, 1)]
    L += ['', '### THE CORRESPONDENCE CELLS (relay data/b693_correspondence_dry.txt, the generator run dry): %s' % cd.strip('#* '),
          '', '### THE SIDE-kernel ROW`S RESIDUE OF b691 (R-K1, relay data/b691_cut.txt :22-:27), read where the cut document carries it:',
          '### PATHS_TO_THE_CRITICAL_LINE_v0_7.md :301 names SIDE-kernel v1.8 (carried at lv-conservation v0.7.0), not SIDE-archimedean; the cut',
          '### document does not carry it; CARRIED, held by the generator as CARRIED AT: VERSION DIFFERS (relay data/b693_correspondence_dry.txt).',
          '### b691`s residues R-1 to R-4 (SIDE-rcurve README.md :3, :9, :11, :19) carried as b691`s closing names them.',
          '', '### ### **%s RE-CUT: THE DISTANCE BEFORE %d, AFTER %d ; TAG %s ; PRINTS EQUAL ; QUOTING LINES %d, EACH A RESIDUE CARRIED ; THE '
          'CORRESPONDENCE CELLS HELD ; THE :301 RESIDUE CARRIED.**' % (k, before, after, CUT['tag'], len(qlines))]
    put_txt('b693_cut.txt', L)
    put_json('b693_cut.json', dict(at=utc(), kernel=k, rows=rows, before=before, after=after, residues=[list(x) for x in qlines], main=CUT['main'],
                                   tip=CUT['tip'], tag=CUT['tag'], tag_peel=tag_peel, merged_tree=mt, built_tree=tt, run_before=CUT['before'],
                                   run_after=CUT['after']))
    print(NL.join(L))


# ================================================================================ THE DEFECTS BANK (b692's route and its row reader, carried)
DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short(act='b693'):
    out = []
    L = rdn('%s_defects.txt' % act).split(NL)
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
    t = rdn('b693_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b693_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


# ================================================================================ THE CAPTURE AND THE COMMANDS (b692's, carried; TWO SESSIONS)
# ### Component 4, after the host's reboot: the act's transcript is two sessions -- 2c300355 from (R303)'s line to the reboot, and the resume
# ### session from the author's resume order (K.SESSIONS_AFTER) -- so the capture reads each from its own anchor and joins them by time. The
# ### shared readers (tools/edit_route.py capture, tools/rule_arms.py transcript) are called once per session, unedited.
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
SESSIONS = ((SESSION, K.ANCHOR, SUBAGENTS),) + tuple(('%s/%s.jsonl' % (PROJ, s), a, '%s/%s/subagents' % (PROJ, s)) for s, a in K.SESSIONS_AFTER)
PREV_ACT, PREV_ANCHOR = 'b692', 'RULING (R302) BEGIN'


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
    """every Bash and PowerShell command of the act: each session read from its own anchor by edit_route's capture, joined by time, numbered."""
    rows = []
    for path, anc, sub in SESSIONS:
        got = ER.capture(path, anc, sub)
        if not got and path != SESSION:
            sys.exit('### THE RESUME SESSION`S ANCHOR %r READ NO COMMAND -- NOTHING READ' % anc)
        rows += [dict(r, src=('%s %s' % (os.path.basename(path)[:8], r['src'])) if path != SESSION else r['src']) for r in got]
    rows.sort(key=lambda r: r['ts'])
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
    """G-EDIT-ROUTE's window over the previous act (b687's repair; the same first session): b692's capture AFTER ITS POST-PUSH SUITE -- every
    command from the call that combined b692's post-push parts into data/b692_checks_postpush.txt to the first user line of (R303)."""
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


SHELL_VAR = re.compile(r'\$(?:\?|\{[^}]*\}|[A-Za-z_]\w*|\d)')


def delete_shape(cmd):
    """(R303)(5) and the ferry: a delete command names one branch and carries no glob and no variable in any half: (the branches it deletes,
    any glob character, any shell variable). b693, Component 4: a variable is read as itself (`$?`, `$x`, `${x}`) and no longer as a glob --
    step zero's deletes carried `; echo EXIT $?`, whose `?` the carried reader named a glob (this act's defect (f))."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    vs = SHELL_VAR.findall(c)
    return names, [ch for ch in '*?[' if ch in SHELL_VAR.sub('', c)], vs


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
    disp = [r for r in sh_ if re.search(r'(^|&&\s*|;\s*)gh workflow run\b|b693_record\.py dispatch [^\s;]+ [^\s;]+ [^\s;]+ [^\s;]+\s*(?:;|$)',
                                        QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in sh_ if (r.get('bg') or re.search(r'Start-Process|\bnohup\b|run_in_background', QUOTED.sub('""', r['cmd'])))]
    seds = [r for r in sh_ if sed_cmd(r['cmd'])]
    nulls = [r for r in sh_ if REDIRECT_NULL.search(QUOTED.sub('""', r['cmd']))]
    redir = [r for r in sh_ if REDIRECT_ANY.search(QUOTED.sub('""', r['cmd']))]
    pipes = [r for r in sh_ if PIPE_FILTER.search(QUOTED.sub('""', r['cmd']))]
    pyreads = [r for r in sh_ if PY_PRINT_READ.search(r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    halves = dict((r['n'], len([x for x in re.split(r'&&|\|\||;|\|', QUOTED.sub('""', r['cmd'])) if x.strip()])) for r in mv)
    ob = outbound()
    L = ['b693 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and the resume session%s from the author`s resume order%s, '
         'with their subagents` transcripts' % (K.SESSION_ID, K.ANCHOR, ''.join(' ' + s for s, _a in K.SESSIONS_AFTER),
                                                 ''.join(' (%r)' % a_ for _s, a_ in K.SESSIONS_AFTER)),
         '### commands read: %d (the first session %d, after the reboot %d)' % (len(rows), sum(1 for r in rows if not r['src'].startswith(
             tuple(s[:8] for s, _a in K.SESSIONS_AFTER))), sum(1 for r in rows if r['src'].startswith(tuple(s[:8] for s, _a in K.SESSIONS_AFTER)))),
         '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (b692, the first session %s, from its post-push combine to (R303)`s line): %d '
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
    L += ['', '### THE COMMANDS CARRYING A REDIRECT ONTO /dev/null, read outside quoted strings -- this act`s defect (c) among them (%d):' % len(nulls)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], r['cmd'].split(NL)[0][:200]) for r in nulls] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT OF ANY STREAM, read outside quoted strings (%d):' % len(redir)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in redir] or ['  NONE'])
    L += ['', '### THE COMMANDS PIPING INTO A SHELL FILTER (head, tail, wc, grep and the like), read outside quoted strings -- this act`s defect (d) '
              'among them (%d):' % len(pipes)] + (['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in pipes] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT RUN AN INTERPRETER`S ONE-LINE PROGRAM (python -c), each its first line -- this act`s defect (e) among them (%d):'
          % len(pyreads)] + (['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:220]) for r in pyreads] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R303)(5) and the ferry: one branch per command, no glob and no variable in any half): ' + ('; '.join(
        '#%d deletes %s, halves %d, globs %s, variables %s' % (n, d, halves.get(n, 0), gl or 'none', vs or 'none') for n, d, gl, vs in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git (web searches, subagent prompts and fetches), each with the author`s identifiers found in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; REDIRECTS ONTO /dev/null %d ; '
              'REDIRECTS OF ANY STREAM %d ; PIPES INTO A SHELL FILTER %d ; ONE-LINE PROGRAMS %d ; MOVE OR DELETE COMMANDS %d ; BRANCH DELETES OF ONE '
              'BRANCH, NO GLOB AND NO VARIABLE %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(nulls), len(redir), len(pipes), len(pyreads), len(mv),
                  sum(1 for _n, d, gl, vs in shapes if len(d) == 1 and not gl and not vs), len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    put_txt('b693_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b693_commands.json', dict(at=utc(), anchor=K.ANCHOR, sessions_after=[list(x) for x in K.SESSIONS_AFTER], rows=rows,
                                        offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        prev=dict(act=PREV_ACT, session=K.SESSION_ID, rows=len(prev),
                                                  offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                        seds=[r['n'] for r in seds], null_redirects=[r['n'] for r in nulls], redirects=[r['n'] for r in redir],
                                        pipes=[r['n'] for r in pipes], py_programs=[r['n'] for r in pyreads], moves_deletes=[r['n'] for r in mv],
                                        delete_shapes=[dict(n=n, deletes=d, globs=gl, variables=vs, halves=halves.get(n)) for n, d, gl, vs in shapes],
                                        outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r, o in phits:
        print('  PREVIOUS-ACT OFFENCE #%s %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


# ================================================================================ THE LATE ROUTES (b692's, carried with b693's names)
def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle', 'SIDE-bijection', 'SIDE-class-number-anomaly',
                                   'SIDE-spinor', 'SIDE-li-map', 'SIDE-rcurve', 'SIDE-archimedean']


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    put_json('b693_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-archimedean read after its merge and tag, its cut branch and push branches standing; none written after '
          'this read)' % len(ks))


def seal_hashes():
    import hashlib
    rec_ = jl('b693_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b693_seal_hashes.json')) else {}
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


# ### the banks a later step writes (the scores, the record, the suite's runs, the chain halves and their control, the pushes, the mirror) are
# ### not named by the root; the scan files stay untracked
ROOT_EXCLUDE = re.compile(r'^b693_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*|close_sentence)\.?(txt|json|md|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b693_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(K.SHARED_APPENDED))


def rootbanks(*a):
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['b693 -- G-ROOT-BANKS-COMMITTED`S READING: THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ;'
         ' carried by HEAD ; HEAD`s blob equal to the file' % utc(), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('b693_root_banks.txt', L)
    put_json('b693_root_banks.json', dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b693_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### G-ROOT-BANKS-COMMITTED: A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b693'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b693_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='b693_ra_') as tmp:
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
    L = ['b693 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '-')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b693_root_arm.txt', L)
    put_json('b693_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_final(*a):
    before = _rows_state(json.loads(_show(ROOT, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b693 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(ROOT, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b693_table_final.txt', L)
    put_json('b693_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
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
    import b692_worklist as K692
    return sorted((set(_g2_of(os.path.join(D, 'b692_registration_2026-10-19.txt'))) - set(K692.ACT_ARMS)) | set(K.STANDING_ADDED))


def armsecs(*a):
    st = _standing()
    rows, phases, runs = [], {}, {}
    for p in K.PARTS:
        j = jl('b693_arm_seconds_%s.json' % p)
        phases[p] = j.get('phases') or {}
        runs[p] = j.get('run_secs')
        for nm, s in (j.get('arms') or {}).items():
            rows.append(dict(arm=nm, part=p, secs=s, standing=nm in st))
    srows = sorted([r for r in rows if r['standing']], key=lambda r: -r['secs'])
    miss = sorted(set(st) - set(r['arm'] for r in srows))
    L = ['b693 -- THE STANDING ARMS` SECONDS AT HEAD, BY PART, FROM THE PRE-RUN (%s): the per-part seconds of the six parts' % utc(), '',
         '### the source: data/b693_arm_seconds_<part>.json, written by tools/b693_checks.py at its pre-run, each arm`s seconds the sum of its',
         '### three readings (LIVE on the sources, NEG on a copy, POS on a mutated copy); each part`s run seconds and its phases -- the sources',
         '### built once for all its arms -- printed beside, not divided among them. standing-b2 carries no arm and is clocked by its run alone.',
         '### Rows are standing arms, slowest first:']
    L += ['  %-46s %-11s %8.3f s' % (r['arm'], r['part'], r['secs']) for r in srows]
    L += ['', '### THE PARTS` SECONDS: ' + ' | '.join('%s %s s' % (p, runs[p]) for p in K.PARTS),
          '### THE PARTS` PHASES (seconds): ' + ' | '.join('%s: %s' % (p, '; '.join('%s %.0f' % kv for kv in ph.items())) for p, ph in phases.items()),
          '### the standing arms not clocked: %s' % (miss or 'NONE'),
          '', '### ### **STANDING ARMS CLOCKED %d OF %d ; THE THREE SLOWEST %s ; THEIR SECONDS SUMMED %.1f.**' % (
              len(srows), len(st), ', '.join('%s (%s, %.2f s)' % (r['arm'], r['part'], r['secs']) for r in srows[:3]) or 'NONE',
              sum(r['secs'] for r in srows))]
    put_txt('b693_arm_seconds.txt', L)
    put_json('b693_arm_seconds.json', dict(at=utc(), rows=srows, phases=phases, run_secs=runs, standing=len(st), clocked=len(srows), missing=miss,
                                           slowest=[r['arm'] for r in srows[:3]]))
    print(L[-1])


# ================================================================================ THE SCORES: (N1)-(N5) OF (R303)'S FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and commits and not the entry; the entry reads the scorer's bank. `scores`
# ### writes data/b693_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there and is read at the close.
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b692_closing_push_out.txt')


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


def _vl(name):
    return ([x for x in rdn(name).split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]


def _n1():
    cm = jl('b693_commands.json')
    rows = jl(K.RUNNER_ROWS).get('rows') or []
    arts = len(rows) == len(K.RUNNER_LABELS) and all(r.get('artifact_sha256') and r.get('gate') == 'DERIVES' for r in rows)
    ok = bool(cm) and not cm.get('local_lean') and arts
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s (relay data/b693_commands.txt, %d commands read over both sessions); runner '
        'rows %d, each run read by its id with the artifact`s sha256 equal to the platform`s before any reading, each DERIVES: %s' % (
            cm.get('local_lean') if cm else 'unread', len(cm.get('rows') or []), len(rows), arts))


def _first_prerun_epoch():
    m = re.search(r'### run at \(UTC\) : (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', rdn('b693_arms_prerun_standing-a.txt'))
    return _iso_epoch(m.group(1)) if m else None


def _n2():
    t = rdn('b693_tie.txt')
    named = _git_ct('D:/' + K.ARCH, K.ARCH_WF)
    tie_t = _git_ct(ROOT, K.TIE_RELAY)
    tie_ok = '### b674`S TIE-BREAK RULE, VERBATIM FROM relay data/b674_rules.txt :8-:11:' in t and '### THE KERNEL ROWS, VERBATIM' in t \
        and 'b693_tie.txt' in ' '.join(_files_of(ROOT, K.TIE_RELAY)) and bool(tie_t) and bool(named) and tie_t <= named
    pp_t, pr = _git_ct(ROOT, K.PARTS_RELAY), _first_prerun_epoch()
    probe = 'THE SIX-PART RUN PASS' in _vl('b693_parts_probe.txt') and 'data/b693_parts_probe.txt' in _files_of(ROOT, K.PARTS_RELAY)
    parts_ok = probe and bool(pp_t) and bool(pr) and pp_t <= pr
    return ('HELD' if tie_ok and parts_ok else 'REFUTED'), (
        'the tie-break rule and the kernel rows printed verbatim from their banks (relay data/b693_tie.txt, relay %s at %s) before the document`s first '
        'write (SIDE-archimedean %s at %s): %s; the parts arm`s reading of a three-part run printed (relay data/b693_parts_probe.txt, relay %s at %s: '
        '"%s") before the suite`s first part (the pre-run at %s): %s' % (
            K.TIE_RELAY, tie_t, K.ARCH_WF, named, tie_ok, K.PARTS_RELAY, pp_t, _vl('b693_parts_probe.txt').strip('#* ')[:60], pr, parts_ok))


def _n3():
    c = rdn('b693_cut.txt')
    m = re.search(r'THE DISTANCE BEFORE (\d+), AFTER (\d+)', c)
    dist = bool(m) and int(m.group(2)) <= int(m.group(1))
    prints = 'EQUAL LINE FOR LINE True' in _vl('b693_prints_SIDE-archimedean.txt')
    q_t, merge_t = _git_ct(ROOT, K.CUTRUN_RELAY), _git_ct('D:/' + K.ARCH, K.ARCH_MERGE)
    qv = _vl('b693_quote_archimedean.txt')
    qn = re.search(r'QUOTING LINES (\d+)', qv)
    quote = bool(qn) and 'data/b693_quote_archimedean.txt' in _files_of(ROOT, K.CUTRUN_RELAY) and bool(q_t) and bool(merge_t) and q_t <= merge_t
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    cells = 'HELD, NONE WRITTEN' in _vl('b693_correspondence_dry.txt') and all(x in K.PP_WRITTEN for x in pp_ch)
    ok = dist and prints and quote and cells
    return ('HELD' if ok else 'REFUTED'), (
        'the distance by the b670 method before %s, after %s (relay data/b693_cut.txt): at or below %s; the before and after prints equal line for '
        'line (relay data/b693_prints_SIDE-archimedean.txt): %s; the quotation search committed (relay %s at %s) before the merge (SIDE-archimedean '
        '%s at %s), its hit count printed -- quoting lines %s: %s; no Correspondence cell written by hand -- the generator dry, its cells held, '
        'PLACE-papers files changed %s: %s' % (
            m.group(1) if m else '?', m.group(2) if m else '?', dist, prints, K.CUTRUN_RELAY, q_t, K.ARCH_MERGE, merge_t,
            qn.group(1) if qn else '?', quote, pp_ch or 'NONE', cells))


LOAD_NEEDLE = 'Zeta23.reflect (825), Zeta23.ZeroConfig.mk (716), Zeta23.ZeroConfig (716)'


def _n4():
    d692 = ' '.join(rdn('b692_defects.txt').split())
    corr = rdn('b693_corrigendum.txt')
    land_ = jl('b693_corrigendum_landing.json').get('lines') or []
    load = LOAD_NEEDLE in d692 and LOAD_NEEDLE in corr and bool(land_) and land_[0].get('line') == K.CORRIGENDUM_LINE \
        and re.search(r'THE ENTRY AT \w+ :%d\.' % K.CORRIGENDUM_LINE, corr) is not None
    rx = rdn('b693_range_exercise.txt')
    rng = '(i) The defects (a)–(m) for the next ruling' in rx and '(i) The defects (a)–(k) for the next ruling.' in rx
    return ('HELD' if load and rng else 'REFUTED'), (
        'the corrigendum`s bank and landing (relay data/b693_corrigendum.txt, data/b693_corrigendum_landing.json, the landing bank`s line :%d) '
        'carry the three LOAD names and figures as b692`s defects bank gives them ("%s", relay data/b692_defects.txt (m)): %s; the closing tool`s dry '
        'run of the carried-forward row, on the author`s word the tool that takes the repair (relay data/b693_author_answers.txt, prompt 2), prints '
        '"(a)–(m)" from b692`s bank and "(a)–(k)" from b691`s, its control (relay data/b693_range_exercise.txt): %s' % (
            K.CORRIGENDUM_LINE, LOAD_NEEDLE, load, rng))


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
    face = jl('b693_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    t0, moved, tags = _kernels_moved()
    allowed = set((k, c[:7]) for k, cs in K.KERNEL_COMMITS.items() for c in cs)
    beyond_main = [m for m in moved if (m[0], m[1][:7]) not in allowed]
    tags_beyond = [t for t in tags if t not in K.KERNEL_TAGS]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b693_', x) and x[6:] not in K.REPAIRED_TOOLS + K.NEW_TOOLS]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b693_|audit_b693_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA) or x in K.SHARED_APPENDED
                                                or (x.startswith('tools/') and x[6:] in K.REPAIRED_TOOLS + K.NEW_TOOLS))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import rule_arms as RA
    import b692_worklist as K692
    arms_added = sorted(set(RA.NAMES) - set(K692.STANDING_ADDED) - set(_g2_of(os.path.join(D, 'b692_registration_2026-10-19.txt'))))
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock)) if lock else []
    ob = jl('b693_commands.json').get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    wf_ident = [w for w in IDENT if w in g('D:/' + K.ARCH, 'show', 'main:.github/workflows/build-module.yml').lower()]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = k_ok and not beyond_main and not tags_beyond and not pp_beyond and not kinds_beyond and not shared_tools and not differ and not arms_added \
        and not amended and not ident and not wf_ident and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; kernel main commits '
            'since the act began beyond the re-cut`s four (%s): %s; tags made since the act began beyond %s: %s; no standing arm added '
            '(tools/rule_arms.py`s names beyond b692`s face): %s; the shared tools edited beyond the carry-time repairs %s: %s; sealed tools not '
            'agreeing (the repaired shared tools among them): %s; commits amended after the seal: %s; PLACE-papers beyond FINDINGS and OPEN_TRAILS: '
            '%s; relay files of a kind beyond the act`s banks and tools, the repaired tools, the corrigenda bank, the table, the root list and '
            'b692`s push-out bank: %s; "patent" in the lines written: %s; outbound requests other than git %d, an identifier of the author in %s; '
            'in SIDE-archimedean`s workflow file: %s' % (
                K.DRAFT, k_ok, ', '.join(K.KERNEL_COMMITS[K.ARCH]), beyond_main or 'NONE', '%s %s' % K.KERNEL_TAGS[0], tags_beyond or 'NONE',
                arms_added or 'NONE', list(K.REPAIRED_TOOLS), shared_tools or 'NONE', differ or 'NONE', amended or 'NONE', pp_beyond or 'NONE',
                kinds_beyond or 'NONE', pat or 'NONE', len(ob), [r['line'] for r in ident] or 'NONE', wf_ident or 'NONE'))


def _s_scores():
    import collections
    TF, RA_ = jl('b693_table_final.json'), jl('b693_root_arm.json')
    _r, _n, sh = seal_hashes()
    return {
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))
               if TF else 'waits on the final table (relay data/b693_table_final.json)'),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally' if RA_
               else 'waits on the root and its arm (relay data/b693_root_arm.json), computed after the entry'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }


def scores(*a):
    """`scores [dry]` writes data/b693_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b693_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        return
    if close:
        put_json('b693_scores_close.json', dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, 'b693_scores.json')):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('b693_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def scores_line(S):
    """the entry's scores line, composed from the scores bank alone (the act arm G-ENTRY-SCORES-EQUAL composes it the same way and compares)."""
    return '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.'


# ================================================================================ THE RECORD: THE ENTRY BEFORE THE ROOT, THE TRAIL CARRYING IT
def TRAIL_HEAD():
    return ('### b693 — lane two, act one hundred and twenty, the re-cut act under (R303): b692 at its weight; its post-seal figures by '
            'corrigendum; the push tool`s branch mode and the closing tool`s defects range repaired at carry time; SIDE-archimedean cut under the '
            'quotation rule; the suite in six parts, the act-root chain split by act')


def _calls():
    return jl('b693_author_answers.json').get('calls') or []


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _figs():
    """the figures the title and the entry carry, each read from its bank by a needle that passes a dotted name and leaves a closing period
    (b692's defect (m), answered)."""
    c = rdn('b693_cut.txt')
    dm = re.search(r'THE DISTANCE BEFORE (\d+), AFTER (\d+) ; TAG (v[\d.]*\d)', c)
    ql = re.search(r'QUOTING LINES (\d+)', _vl('b693_quote_archimedean.txt'))
    tie = re.search(r'(SIDE-[\w-]+) AT (\d+), ALONE AT THE TOP COUNT', _vl('b693_tie.txt'))
    tb = re.search(r'ROWS (\d+) ; MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+)', rdn('b693_tie.txt'))
    pr = re.search(r'BEFORE (\d+) TERMINALS ; EACH PRINTED AFTER (\w+) ; DIFFERING (\d+)', _vl('b693_prints_SIDE-archimedean.txt'))
    bm = re.search(r'THE TEST (\d+) OF (\d+)', _vl('b693_branch_mode.txt'))
    rx = re.search(r"BANK READ AS (\([a-z]\)–\([a-z]\))", _vl('b693_range_exercise.txt'))
    ld = re.search(r'LOAD LED BY (.*?) ; THE FACTOR ([\d]+(?:\.\d+)?)', _vl('b693_corrigendum.txt'))
    rf = re.search(r'LINES DIFFERING (\d+) \(HAND ONLY (\d+), OF WHICH IN THE CLOSURE (\d+) ; TEXT ONLY (\d+)\)', rdn('b693_readfirst_diff.txt'))
    i = lambda m, k: int(m.group(k)) if m else None   # noqa: E731
    return dict(before=i(dm, 1), after=i(dm, 2), tag=dm.group(3) if dm else '', quoting=i(ql, 1), doc=tie.group(1) if tie else '',
                count=i(tie, 2), rows=i(tb, 1), matches=i(tb, 2), over=i(tb, 4), terminals=i(pr, 1), differing=i(pr, 3),
                test=(i(bm, 1), i(bm, 2)), range=rx.group(1) if rx else '', load=ld.group(1) if ld else '', factor=ld.group(2) if ld else '',
                rf=(i(rf, 1), i(rf, 2), i(rf, 3), i(rf, 4)))


def _title():
    """the ferry's form, adjusted to what the act did: the document a kernel, its rows outside LICENSED/CITED before and after, its tag."""
    f = _figs()
    return ('## %s re-cut: %s rows outside LICENSED/CITED to %s, %s; b692’s LOAD figures by corrigendum; push_gated.sh branch mode; the closing '
            'tool’s defects range read from the bank' % (f['doc'], f['before'], f['after'], f['tag']))


def _chain_text():
    """the chain split's reading, from the whole-chain control's bank where it is written (after the pre-push halves), else a stand-in line."""
    v = _vl('b693_chain_control.txt')
    return v.strip('#* ') if v != '### NOT READ' else 'the whole-chain control is run once beside the pre-push halves'


def _finding_text():
    """the FINDINGS entry, composed before the root: its scores line from the scores bank alone (data/b686_rules.txt row (1)); the root is
    carried by the trail record."""
    S = jl('b693_scores.json')
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b693_author_answers.txt'), re.M))
    c1_ = _rl_lines('b693_record_lines.json') + ['-']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'SIDE-archimedean, the licensed table’s next document by b652’s order and alone at its top count, is cut under the quotation rule: its '
         'module header and headline docstring take the two ACTIONs of its b647 table verbatim on a scratch branch, the quotation search runs '
         'across the kernel before the merge, and the distance by the b670 method falls from %s rows outside LICENSED/CITED to %s, the prints of its '
         '%s terminals equal line for line before and after, the merge tagged %s.' % (f['before'], f['after'], f['terminals'], f['tag']), '',
         '*Filed at b693 on the author’s ruling `(R303)` and the author’s words at its prompts; %d questions put. Banks: relay `data/b693_tie.txt`, '
         '`data/b693_cut.txt`, `data/b693_quote_archimedean.txt`, `data/b693_prints_SIDE-archimedean.txt`, `data/b693_correspondence_dry.txt`, '
         '`data/b693_corrigendum.txt`, `data/b693_range_exercise.txt`, `data/b693_branch_mode.txt`, `data/b693_parts_probe.txt`, '
         '`data/b693_tool_repairs.txt`, `data/b693_resume.txt`.*' % n_ans, '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed, each miss raised before the component that '
         'cites it; %d answers checked before they were acted on, and checked again at the resume. b692 at its weight (FINDINGS :%s), its head line '
         'quoted, the triage’s classes and its entries as written both from the banks.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, c1_[0]), '',
         '**The corrigendum** (`(R303)`(2)): b692’s two post-seal figures entered by one generated entry in b678’s form (FINDINGS :%d) -- LOAD led '
         'by %s, the factor %s -- the sealed entry unedited, the corrigenda bank appended.' % (K.CORRIGENDUM_LINE, f['load'], f['factor']), '',
         '**The repairs** (`(R303)`(2)): on the author’s word the closing tool takes the range repair, its carried-forward row reading %s from b692’s '
         'defects bank through the record tool’s reader; push_gated.sh gains a branch mode, one branch pushed alone and read back, refused unmerged '
         'unless named a scratch branch, its test %s of %s; the mode exercised on push-b693-root at the pre-root push.' % (
             f['range'], f['test'][0], f['test'][1]), '',
         '**The naming** (`(R303)`(3)): b652’s order and b674’s tie-break printed verbatim from their banks with every kernel row before the '
         'document was named; %s at %s, alone at the top count, its table %s rows -- %s MATCHES, %s OVERREACHES; the tie rule not reached.' % (
             f['doc'], f['count'], f['rows'], f['matches'], f['over']), '',
         '**The cut** (`(R303)`(3)): the workflow and the print list each alone on main; the cut on recut-archimedean-b693, pushed alone by the branch '
         'mode named a scratch branch; runs before and after read by their ids, the artifacts by sha256 first, the prints %s terminals, %s differing; '
         'the merge by --no-ff, its tree the built tree; the tag %s naming the prior tag v0.1.0.' % (f['terminals'], f['differing'], f['tag']), '',
         '**The quotation search** (data/b690_rules.txt row (2)): eleven removed lines, a needle each in two shapes, searched across the kernel’s '
         'tracked tree before the merge with a control at the base firing for every needle; %s quoting lines, each entered as a residue -- two README '
         'lines carried, the T3 block’s own kept line carried as it stands.' % f['quoting'], '',
         '**The Correspondence cells**: the generator run dry, its three cells for SIDE-archimedean held, none written by hand; the SIDE-kernel '
         'row’s :301 residue read where the cut document carries it, not there, and carried.', '',
         '**The parts** (`(R303)`(4)): the parts arm’s family comparison read in memory before the suite meets a governing part by any numbered '
         'subdivision, so it took no repair; on the author’s word the act-root chain is split by act, standing-b2 verifying b624-b658 and banking '
         'its verdicts, standing-b3 verifying b659-b693 and counting the arm once over both; %s.' % _chain_text(), '',
         '**The reboot**: the host rebooted after Component 3 (relay 0574078e); on the author’s resume order the state was read from the tree and '
         'the banks into relay data/b693_resume.txt, the four mid-act answers checked again, and the act continued from Component 4 in a new session '
         'whose commands the act’s readers take beside the first.', '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b692’s closing, defects, corrigendum route and parts probe, b690’s '
         'reading-3 table and b674’s tie rule; it is re-read by b694’s research act, which takes SIDE-lv-conservation’s closure among its candidates, '
         'and by the next re-cut act, which takes the README residues. It strengthens the programme’s offering of a located clause by bringing '
         'one more kernel’s words within what its prints license.', '',
         '**Carried to:** b694 (the research act on the author’s word; relay origin/push-b693-root and the re-cut’s branches on its step-zero '
         'list); the next re-cut act (SIDE-archimedean README.md :15, :19; the faces page’s regeneration); the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the next document read from reading 3’s per-document rows with SIDE-rcurve read at its b691 cut; (2) the cut’s needles one '
              'per removed line in two shapes, the control at the base; (3) the T3 block’s kept line (Reflection.lean :39) carried as it stands, '
              'not a quote of the removed claim; (4) the merged tree checked against the built tree before the tag; (5) the branch mode’s '
              '--scratch used for the cut branch’s push, unmerged until its merge; (6) the whole-chain control run once, after the pre-push halves; '
              '(7) the resume session read beside the first by every reader of the act’s transcript, its anchor the resume order’s first line')


def _trail_text():
    S, J = jl('b693_scores.json'), jl('b693_act_root.json')
    fj = jl('b693_findings.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b693_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1_ = _rl_lines('b693_record_lines.json') + ['-']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R303) ratified.** (1) b692 at its weight. (2) The corrigendum and the two carry-time repairs. (3) The re-cut. (4) The parts. (5) The '
             'branches. (6) The readfirst bank. (7) The draft held at v5. (8) The act after.', '',
             '**Entered:** FINDINGS.md:%s (b692’s weight), :%d (the corrigendum), :%s (the entry); this record.' % (
                 c1_[0], K.CORRIGENDUM_LINE, fj.get('entry_line')), '',
             '**Act root:** b693 `%s` (previous `%s`, b692’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s (relay data/b693_author_answers.txt); none after the root.' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The kernels:** SIDE-archimedean -- the workflow 79a8527 and the print list 7769d0e on main; the cut 2bd9cc8 on recut-archimedean-b693; '
             'the merge fcecc45, tag v0.1.1; runs 39360158384 and 39360543605, each read by its run id.', '',
             '**The banks:** the naming relay data/b693_tie.txt; the cut relay data/b693_cut.txt, data/b693_quote_archimedean.txt, '
             'data/b693_prints_SIDE-archimedean.txt, data/b693_correspondence_dry.txt; the corrigendum relay data/b693_corrigendum.txt; the repairs '
             'relay data/b693_tool_repairs.txt, data/b693_branch_mode.txt, data/b693_range_exercise.txt; the parts relay data/b693_parts_probe.txt; '
             'the resume relay data/b693_resume.txt.', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b693_closing.txt).', '',
             '**The open orders:** `W-ORD-EPSTEIN-COUNT-LEAN` and the candidates of `(R302)`(5) (b694, on the author’s word); '
             '`W-ORD-CORRESPONDENCE-BEHIND-SCOPE` (the next re-cut act); SIDE-archimedean’s README residues (README.md :15, :19) to the next re-cut '
             'act or a README pass.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b693_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S, C = jl('b693_scores.json'), jl('b693_scores_close.json')
    L = ['=' * 104, 'b693 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s%s' % (
        k2, S[k2][0], S[k2][1], ('  ### AT THE CLOSE: %s -- %s' % (C[k2][0], C[k2][1])) if (S[k2][0] == 'PENDING' and C.get(k2)) else '')
        for k2 in SCORE_KEYS]
    L += [''] + rdn('b693_defects.txt').rstrip(NL).split(NL)
    put_txt('b693_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b693_scores.json', 'b693_findings.json', 'b693_trail.json', 'b693_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1_ = _rl_lines('b693_record_lines.json') + ['-']
    L = ['b693 -- THE COMPONENTS, BANKED UNDER (R303).', '',
         '### COMPONENT 0 : the citation check (data/b693_citation_check.txt), step zero (data/b693_ferry.txt, data/b693_readfirst.txt, '
         'data/b693_stepzero.txt, data/b693_tests_stepzero.txt, data/b693_rowgen_stepzero.txt, data/b693_branches.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b692`s weight FINDINGS :%s, the corrigendum :%d (data/b693_corrigendum.txt), the range repair and the branch mode '
         '(data/b693_range_exercise.txt, data/b693_branch_mode.txt) ; N4 %s' % (c1_[0], K.CORRIGENDUM_LINE, S['N4'][0]),
         '### COMPONENT 2 : the naming (data/b693_tie.txt), the cut (data/b693_cut.txt, data/b693_quote_archimedean.txt, '
         'data/b693_prints_SIDE-archimedean.txt) ; N2 %s ; N3 %s' % (S['N2'][0], S['N3'][0]),
         '### COMPONENT 3 : the parts (data/b693_parts_probe.txt), the chain split (data/b693_tool_repairs.txt rows 6-7)',
         '### THE REBOOT : the resume bank (data/b693_resume.txt), the event in data/b693_defects.txt',
         '### COMPONENT 4 : the carry-time reading (data/b693_tool_repairs.txt), the dry-run steps (data/b693_reg_gate.txt), the seal '
         '(data/b693_seal_hashes.json), the suite in six parts, the per-part seconds (data/b693_arm_seconds.txt) ; S3 %s' % S['S3'][0],
         '### COMPONENT 5 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('b693_components.txt', L)
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
    if not os.path.isfile(os.path.join(D, 'b693_scores.json')):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, 'b693_findings.json', dict(title=t))
    j = jl('b693_findings.json')
    j['entry_line'] = ln
    put_json('b693_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b693_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


FACE_REL = 'data/b693_registration_2026-10-19.txt'
FACE = os.path.join(D, 'b693_registration_2026-10-19.txt')


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

    def runb(args, out):
        r = subprocess.run([sys.executable, '-X', 'utf8'] + args, capture_output=True, cwd=ROOT)
        b_ = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            open(p + '.tmp', 'wb').write(b_)
            os.replace(p + '.tmp', p)
        return r.returncode, b_.decode('utf-8', 'replace')
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b693_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b693_regspec.py')], 'b693_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b693_satisfiable.json', '--emit', 'b693'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b693_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b693_census_stepzero.txt'), ('b327_faces_census.py', 'b693_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b693_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b693'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b693_reg_gate.txt', 'data/b693_reg_termscan.txt', 'data/b693_regspec_run.txt', 'data/audit_b693_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b692's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '%s-b693' % K.DATE
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
    put_json('b693_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b693':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b693`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b693_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_txt('b693_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b693_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b693 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b693 (the last export b692`s, D:/MY-DOwnloads/mirror-refresh-2026-10-19-b692.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b693_mirror.txt', L)
    put_json('b693_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


# ================================================================================ THE CARRY-TIME READING (the ferry's Component 4)
REPAIRS = [
    ('THE STANDING SET FOR b693 (answering N5: no standing arm added): the standing arms are b692`s face`s (G2) arms less b692`s act arms, the',
     'twenty-four rule arms of tools/rule_arms.py among them; STANDING_ADDED empty (tools/b693_worklist.py).'),
    ('THE SIX PARTS AND THE CHAIN SPLIT (answering (R303)(4) and the author`s word at prompt 3): standing-b2 verifies b624-b658 through',
     'act_root.verify(acts=...) (row 6 above) and banks its verdicts with the boundary link read from data/act_roots.txt, carrying no arm;',
     'standing-b3 verifies b659-b693, prints the same link, and runs G-ACTROOT-VERIFY once over both halves` banked verdicts, the first',
     'half`s bank read at the same HEAD; `--chain-control` runs the whole chain once in the old form beside the pre-push halves, this act alone,',
     'and banks the three verdicts equal or not (data/b693_chain_control.txt).'),
    ('THE REPAIRED SHARED TOOLS SEALED (answering N5): circuit_read.py (row 1), push_gated.sh and its test (rows 3-4), act_root.py and its',
     'test (rows 6-7) sealed with the act`s tools (tools/b693_worklist.py SEALED), their hashes compared at the close; G-INSTRUMENTS-UNEDITED',
     'reads every other instrument unedited, rule_arms.py (b692`s repair, unedited this act, row 5) back among them.'),
    ('THE RUNNER ARMS OVER THIS ACT`S TWO RUNS AND ONE MERGE (answering (R303)(3)): G-RUNNER-READ reads the before run at the print list`s',
     'commit and the after run at the cut`s tip; G-RUNNER-GATE their gate readings; G-MERGES-ON-GATE reads SIDE-archimedean`s main at the',
     'merge, its first parent the print list`s commit, its second the gated tip, the tag v0.1.1 peeled to the merge and v0.1.0 unmoved;',
     'G-WORKFLOW-FILES reads the workflow at main equal to the one the act wrote at 79a8527, its print list against the after run`s bank.'),
    ('THE PLACE-papers SCOPE (answering N5): G-PP-SCOPE allows FINDINGS and OPEN_TRAILS alone; no Correspondence cell, no INSTRUMENTS line.',),
    ('THE ACT`S TRANSCRIPT IN TWO SESSIONS (the reboot, between relay 0574078e and 91c2df0c): the command capture, the answers route and the',
     'rule arms` call trace read the first session from (R303)`s line and the resume session from the resume order`s line, joined by time;',
     'tools/edit_route.py and tools/rule_arms.py are called once per session, unedited. G-EDIT-ROUTE`s previous-act window reads b692`s',
     'capture after its post-push suite in the first session.'),
    ('THE STEP-ZERO TESTS` SET: G-STEPZERO-TESTS reads the step-zero bank`s failing set -- test_chain_page.py (1), (9), (14),',
     'test_chain_page_b638.py (4)-(7) and test_g_chain_page.py (1) -- as the bank recorded it, against the tests tracked at relay 1749abbb.'),
    ('THE BRANCHES ARMS OVER EIGHT DELETES (answering (R303)(5)): G-BRANCHES-DELETED reads the eight names gone from relay, PLACE-papers and',
     'SIDE-explicit-formula; G-DELETES-ONE-BRANCH reads eight deletes of one branch each, no glob.'),
    ('THE CLOSING TOOL`S ROWS FOR THIS ACT`S KERNEL: SIDE-archimedean added to its repositories and its tags v0.1.1 and v0.1.0 to its tag',
     'rows; its carried-forward row (e) names the re-cut`s branches left for b694 beside push-b693-root; its closing sentence carried in the',
     'tool as b692`s was, in this act`s words -- act text, the range repair of row 2 untouched.'),
    ('THE DELETE READER READS A VARIABLE AS A VARIABLE (answering the ferry`s "no variable, no glob in any half" and this act`s defect (f)):',
     'tools/b693_record.py delete_shape, carried from b692`s, read the `?` of `$?` as a glob; it now returns the shell variables of a delete',
     'command beside its globs and its halves, the command bank printing each, and G-DELETES-ONE-BRANCH reads no glob and no variable. Step',
     'zero`s eight deletes, each chained to `echo EXIT $?`, read 0 of 8 -- the arm fails on real state and is declared.'),
]
CARRY_HEAD = '### THE CARRY-TIME READING OF THE TOOLS (the ferry`s Component 4), AGAINST b692`S SEALED COPIES'
INST_READ = ('edit_route.py', 'e0_rule.py', 'b678_corrigendum.py', 'chain_page.py', 'b670_record.py', 'b672_record.py', 'repair_snapshot.py',
             'correspondence_gen.py', 'rule_arms.py')


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
    """the carry-time section of data/b693_tool_repairs.txt: each tool carried from a sealed b692 copy read against b692's seal hash first and
    its diff counted by hunks; the standing instruments this act's tools import read against the last seal record naming them and against
    relay before the act; the repaired readings' diffs against b692's sealed copies printed whole; rows (1)-(7) above it read. The bank's head
    is kept: the route replaces only its own section, from its head line to the bank's end."""
    import difflib
    import hashlib
    seal = jl('b692_seal_hashes.json').get('tools') or {}
    rows = []
    for t0 in ('b692_citation.py', 'b692_closing.py', 'b692_reg_gate.py', 'b692_regspec.py', 'b692_tests.py', 'b692_worklist.py',
               'b692_record.py', 'b692_checks.py', 'b692_corrigendum.py', 'b692_parts_probe.py'):
        t1 = t0.replace('b692_', 'b693_')
        old, new = os.path.join(T, t0), os.path.join(T, t1)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        ex = os.path.exists(new)
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8',
                           errors='replace').stdout if ex else ''
        rows.append((t0, t1, now, seal.get(t0), len(re.split(r'(?m)^(?=@@ )', d)[1:]), ex))
    inst = {}
    for t in INST_READ:
        nowh = hashlib.sha256(open(os.path.join(T, t), 'rb').read()).hexdigest()
        acts = [x for x in ('b692', 'b691', 'b690', 'b689', 'b688', 'b687', 'b686', 'b685', 'b684', 'b683') if (jl('%s_seal_hashes.json' % x).get('tools') or {}).get(t)]
        headh = hashlib.sha256(subprocess.run(['git', '-C', ROOT, 'show', '%s:tools/%s' % (K.PRE_RELAY, t)], capture_output=True).stdout).hexdigest()
        inst[t] = (nowh, acts[0] if acts else None, (jl('%s_seal_hashes.json' % acts[0])['tools'][t]) if acts else None, headh,
                   g(ROOT, 'log', '-1', '--format=%h %cI', '--', 'tools/' + t).strip())
    s0r, s1r = rd(os.path.join(T, 'b692_record.py')), rd(os.path.join(T, 'b693_record.py'))
    s0c, s1c = rd(os.path.join(T, 'b692_checks.py')), rd(os.path.join(T, 'b693_checks.py'))
    nd = []
    for (a0, f0), (a1, f1), s0, s1 in ((('b692_record.py', 'capture'), ('b693_record.py', 'capture'), s0r, s1r),
                                       (('b692_checks.py', 'sources'), ('b693_checks.py', 'sources'), s0c, s1c),
                                       (('b692_checks.py', 'verify_ok'), ('b693_checks.py', 'verify_ok'), s0c, s1c),
                                       (('b692_checks.py', 'runner_ok'), ('b693_checks.py', 'runner_ok'), s0c, s1c),
                                       (('b692_checks.py', 'merges_ok'), ('b693_checks.py', 'merges_ok'), s0c, s1c),
                                       (('b692_checks.py', 'wf_ok'), ('b693_checks.py', 'wf_ok'), s0c, s1c),
                                       (('b692_checks.py', '_part_of'), ('b693_checks.py', '_part_of'), s0c, s1c)):
        nd += list(difflib.unified_diff(_fn_src(s0, f0).split(NL), _fn_src(s1, f1).split(NL) if s1 else [],
                                        '%s %s (sealed)' % (a0, f0), '%s %s%s' % (a1, f1, '' if s1 else ' (NOT YET CARRIED)'), n=1, lineterm=''))
    for c in ('CURRENTS', 'NEED', 'STEPZERO_FAILING'):
        nd += list(difflib.unified_diff(_const_src(s0c, c).split(NL), _const_src(s1c, c).split(NL), 'b692_checks.py %s (sealed)' % c,
                                        'b693_checks.py %s' % c, n=1, lineterm=''))
    old = rdn('b693_tool_repairs.txt')
    head = old[:old.index(CARRY_HEAD)] if CARRY_HEAD in old else old
    rows_above = len(re.findall(r'^  \((\d)\) tools/', head, re.M))
    L = [CARRY_HEAD + ' (%s)' % utc(), '',
         '### rows are repairs with the defect or order they answer, after the carried tools: b692`s sealed copy and its seal record; the hunks of',
         '### the diff to b693`s copy. Every hunk is the act`s own text -- its names, its banks, its sections and its predicates over this act`s',
         '### banks -- save the repairs below. The repaired shared tools are rows (1)-(7) above, each with its diff.', '']
    for t0, t1, now, s, nh, ex in rows:
        L.append('  %-22s -> %-22s b692 sealed %s ; the seal`s record %s ; %s ; hunks %s' % (t0, t1, now[:16], (s or '### NONE')[:16],
                                                                                         'AGREE' if s == now else '### DIFFER', nh if ex else 'NOT YET CARRIED'))
    for t, (nowh, act, sh, headh, last) in inst.items():
        L.append('  %-22s  the standing instrument, unedited in this act: %s ; at relay %s %s ; the last seal record naming it (%s`s) %s ; its last '
                 'commit %s' % (t, nowh[:16], K.PRE_RELAY, headh[:16], act or 'NONE', (sh or '### NONE')[:16], last))
    L.append('')
    for i, r in enumerate(REPAIRS, 1):
        L += ['  REPAIR %d -- %s' % (i, r[0])] + ['  ' + x for x in r[1:]]
    L += ['', '### THE DIFF OF THE REPAIRED READINGS AGAINST b692`S SEALED COPIES (tools/b692_record.py sha256 %s, tools/b692_checks.py sha256 %s), '
          'WHOLE:' % ((seal.get('b692_record.py') or '### NONE')[:16], (seal.get('b692_checks.py') or '### NONE')[:16])]
    L += ['    ' + l for l in nd]
    carried = sum(1 for r in rows if r[5])
    unedited = all(v[0] == v[3] for v in inst.values())
    L += ['', '### ### **REPAIRS %d ; THE SEALED COPIES %s ; TOOLS CARRIED %d OF %d ; THE STANDING INSTRUMENTS UNEDITED %s ; THE REPAIRED SHARED '
          'TOOLS` ROWS ABOVE %d ; THE REPAIRED READINGS` DIFF LINES %d.**' % (
              len(REPAIRS), 'AGREE' if all(s == now for _a, _b, now, s, _n, _e in rows) else '### DIFFER', carried, len(rows), unedited, rows_above, len(nd))]
    put_txt('b693_tool_repairs.txt', head.rstrip(NL).split(NL) + ['', ''] + L)
    print(L[-1])


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, c1=c1, defects=defects, tie=tie, dispatch=dispatch, runner=runner, prints=prints, quote=quote, cut=cut,
              commands=commands, kernels=kernels, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final, armsecs=armsecs,
              scores=scores, desk=desk, components=components, findings=findings, trail=trail, drycheck=drycheck, gatebanks=gatebanks, mbuild=mbuild,
              mroot=mroot, mverify=mverify, mbank=mbank, repairs=repairs)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b693_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
