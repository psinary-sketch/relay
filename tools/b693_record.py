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


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, c1=c1, defects=defects, tie=tie, dispatch=dispatch, runner=runner, prints=prints, quote=quote)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b693_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
