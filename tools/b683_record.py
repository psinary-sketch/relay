# -*- coding: utf-8 -*-
"""b683_record.py -- THE ACT'S RECORD TOOL, b683 under (R293).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b683's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b682_record.py (the helpers, the guarded landing, the readers, step zero's rowgen and branches routes,
### the answers route); the later routes are added at their components.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b683_record.py <route> [dry]`.
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
import b683_worklist as K          # noqa: E402

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
    none a number any bank carries; a stand-in run writes no bank. Carried from b682_record.py with b683's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b683_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b683_findings.json': dict(entry_line=99999, title='stand-in'),
        'b683_trail.json': dict(line=99999),
        'b683_act_root.json': dict(root='0' * 64, previous='4882d95a' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b683's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b683_scanfile_%s.md' % tag)
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
    """a row of data/b683_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
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
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b683_rowgen_<stage>.txt."""
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
    L = ['b683 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b683_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R293)(7))
def branches(*a):
    """every branch (R293)(7) names, its tip read before any delete, its fate; the one remote branch with its tip printed as an ancestor of
    main at the tag; any branch under the push-b682 prefix that --merged lists and the ruling does not name, reported and KEPT.
    data/b683_branches.txt (.json)."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    anc = []
    for repo, b, tag in K.DELETE_REMOTE:
        ls = g(repo, 'ls-remote', '--heads', 'origin', b).split()
        tip = ls[0] if ls else ''
        a1 = bool(tip) and grc(repo, 'merge-base', '--is-ancestor', tip, tag) == 0
        a2 = grc(repo, 'merge-base', '--is-ancestor', tag, 'main') == 0
        rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=a1 and a2, fate='DELETED'))
        anc.append('%s %s at the remote: tip %s ; an ancestor of %s %s ; %s an ancestor of main %s ; %s at %s' % (
            os.path.basename(repo), b, tip, tag, a1, tag, a2, tag, g(repo, 'rev-parse', tag + '^{commit}').strip()))
    named = set((r['repo'], r['branch']) for r in rows)
    extra = []
    for repo, _bs in K.DELETE:
        for x in g(repo, 'branch', '--merged', 'main', '--format=%(refname:short)').split(NL):
            x = x.strip()
            if x.startswith('push-b682') and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b683 -- STEP ZERO, (R293)(7): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; listed by `git branch --merged main --list <name>` (the remote: its',
         '### tip an ancestor of main at the tag) ; fate. Deleted by name in the house form, each delete command naming one branch with no glob in',
         '### any half, one command per message, in sequence; no branch the ruling does not name.']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                               r['fate']) for r in rows]
    L += ['', '### the remote branch: ' + ('; '.join(anc) or 'NONE')]
    L += ['', '### branches under the push-b682 prefix that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; TO BE DELETED %d ; UNNAMED UNDER THE PREFIX %d.**' % (
        len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), len(rows), len(extra))]
    put_txt('b683_branches.txt', L)
    put_json('b683_branches.json', dict(at=utc(), rows=rows, extra=[list(x) for x in extra], remote=anc))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R293)(1)
WH = ('*Appended 2026-10-18 by b683 to b682’s entry (:9140), under `(R293)`(1) -- b682 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b682_closing.txt):*')
WB = (' “b682 closed: relay d62f7192, PLACE-papers dc5613b; suite 89 of 90; root 4882d95a927d5417…; 2 prompts answered; 5 defects” '
      '(data/b682_closing.txt :1), the closing pushed and read back at relay fbc1053a (data/b682_closing_push_out.txt). The Correspondence '
      'generator (relay tools/correspondence_gen.py) reads the runner print banks in the form b674, b676 and b678 banked them, committed alone at '
      '60e8de3e; five planted cases as wanted, the fifth reading ABSENT where a print bank exists and the declaration is absent; the five cells at '
      'FOUNDATIONS :628–:630 written by the generator alone (SIDE-silence-principle v0.2.1; profile “axiom-free (none)” at :628 and :629 from '
      'b678’s bank at the tag); the distance 55 by b670’s method and 0 at the generator’s claim, before and after, equal to b680’s -- the five '
      'clauses carry no backticked commit, so b670’s method counts none of them; the unversioned partner copy not written, its table differing '
      'in 13 lines, entered by line and carried under `W-ORD-ONE-COPY`; `W-ORD-CORRESPONDENCE-RUNNER-BANKS` DISCHARGED (OPEN_TRAILS :14744). '
      'SIDE-bijection alone at 4: the workflow and a 15-name print list committed alone on its main, both runner builds DERIVES, 15 prints '
      'equal line for line, merged and tagged v0.2.1, its rows outside LICENSED/CITED 4 to 0 with no residue; the residues of b674, b676 and b678 '
      'carried. The author’s word “arms for the traceable ones, the seat sorts them” banked at data/b682_rules.txt row (1) and OPEN_TRAILS '
      ':14742. The suite 89 of 90 before and after the record push, G-EDIT-ROUTE failing on a sed command the seat sent, declared on the face '
      'before the lock; five defects, four the seat’s -- (a) five deletes in one message, (b) a test part past 600 s moved to the background '
      '(test_asof.py 563 s at about 1.9 GB free), (d) the naming route sent without its timeout, (e) the sed command -- and (c) the '
      'navigator’s, “the 13 roster files”; N1–N5 and S1–S3 HELD, the sealed tools 8 of 8; the root 4882d95a… chained from b681’s over 56 banks '
      'committed and pushed before it; mirror-refresh-2026-10-18-b682.zip CLEAN with the root line. The sed command: the rule as written, the '
      'entry its repair, the arm’s reading at this act’s seal expected clean. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b683_record_lines.json', 'c1', entry=K.B682_ENTRY,
         check=[('FINDINGS.md', K.B682_ENTRY, '## The Correspondence reader'), ('OPEN_TRAILS.md', K.B682_TRAIL, '### b682')], dry=dry)


# ================================================================================ THE ANSWERS BANK (b682's route, carried)
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
    """data/b683_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
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
    head = ['### b683 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b683_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b683_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 3: THE LANDING, (R293)(5)
ORDERS = 'b670_work_orders.txt'
OH = ('*Appended 2026-10-18 by b683 beneath b682’s trail record (:14746), under `(R293)`(5) -- `W-ORD-MAP-ANGLE-FORM` (:14398, :14714) '
      'DISCHARGED:*')
OB = (' the detection map in the angle form (relay tools/b677_epstein_map_angle.py, imported unchanged through tools/b683_epstein_map_angle.py, '
      'its four changes named in data/b683_map_plan.txt section 1) run over the b681 balls at half-width 1e-30, the hash chain verified 7 of 7 '
      'before any ball was read (data/b683_chain.txt): all 123 controls of b671’s list PASS -- Z₁ 41 of 41, Q0 41 of 41 at 200 bits and 41 of '
      '41 at 400, the rung forced by the ruling, not the tool’s own choice; of the 46 that b671 read INSTRUMENT, 46 PASS (H1 HELD); the radius '
      'at j = 64 2.073e-9 at 200 bits and 2.063e-9 at 400 against the bar 2^-20 = 9.54e-7, 2.17e-3 of it (H2 HELD), beside the plan’s price '
      '1.3e-10 to 7.7e-8. On the passing instrument: H3 HELD, every hypothesis of zeroSide_neg_at_rate_cfg certified by name (hQtie 41 of 41) '
      'and hrate holding at j₀ = 38 ≤ D + 40 = 64 -- hA by the named premise P3 (Q0Count, stated, not proved), so H3 holds on that premise; '
      'H4 SCORABLE and HELD, j₀ = 38 and the zero side [-7.570971095704516e+39 +/- 2.40e+23] below 0; H5 HELD, b677’s instrument-side row '
      'agreeing at the 15 j where both exist, 24–38 (relay data/b683_map.txt, data/b683_map_run.txt, data/b683_map_h.txt, data/b683_landing.txt). '
      'Pin: relay data/b683_map.txt. Status DISCHARGED.')
ORDER_ROW = re.compile(r'^  (W-ORD-[A-Z0-9-]+)\s+:(\d+)\s+(b\d+)\s+(\d+)\s+(OPEN|DISCHARGED|ACTED|NOT STATED|CLOSED)\s+:(\d+)\s+(.+?) \[:(\d+)\]$')


def read_order_row(line):
    """a row of the orders bank: order, entry line, act entered, age in acts, Status, the line of its last mark, the trigger or pin, and that
    line again; returns (order, Status, mark line)."""
    m = ORDER_ROW.match(line or '')
    if not m or m.group(6) != m.group(8):
        raise ValueError('order row of another shape: %r' % (line,))
    return m.group(1), m.group(5), int(m.group(6))


READERS.append('read_order_row')


def c3(*a):
    """(R293)(5): the discharge line on OPEN_TRAILS, then its row appended to the orders bank additively ((R254)(2))."""
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', OH, NL + OH + OB + NL)], 'b683_landing.json', 'c3',
         check=[('OPEN_TRAILS.md', K.ORDER_LINE, 'W-ORD-MAP-ANGLE-FORM'), ('OPEN_TRAILS.md', K.B682_TRAIL, '### b682')], dry=dry)
    if dry:
        return
    ln = jl('b683_landing.json')['lines'][0]['line']
    rows = ['### Appended 2026-10-18 by b683 under (R293)(5) (additive, (R254)(2)): W-ORD-MAP-ANGLE-FORM DISCHARGED, its pin the map bank; its '
            'Status cell filled and its line its pin.',
            '  %-44s :%d  %s   %-5d %-16s :%d  %s [:%d]' % ('W-ORD-MAP-ANGLE-FORM', K.ORDER_FIRST, 'b671', 12, 'DISCHARGED', ln,
                                                            'pinned by data/b683_map.txt', ln)]
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


# ================================================================================ COMPONENT 4: THE RULES-TO-ARMS BANK RE-READ ((R293)(6))
import collections                 # noqa: E402
PROSE = ('b671 row 1', 'b671 row 5', 'b673 row 4')
SUPERSEDED = {'b677 row 1': 'G-RULE-SUITE-PARTS'}
RA_ROW = re.compile(r'^  (b\d{3})  row (\d+)\s+(data/b\d{3}_rules\.txt :\d+)\s+(\S+)\s+(.*)$')


def rulesarms(*a):
    """data/b683_rules_arms.txt: b680's rules-to-arms rows (data/b680_rules_arms.txt :7-:32) re-read with the arms the author's word on the
    sort names (tools/rule_arms.py), the superseded rule read through b678 row 1's arm, the PROSE rules NONE; the NONE count against 24."""
    import rule_arms as RA
    by_rule = dict((v, k) for k, v in RA.RULE_OF.items())
    rows = []
    for l in rdn(K.RULES_ARMS).split(NL):
        m = RA_ROW.match(l)
        if not m:
            continue
        key = '%s row %s' % (m.group(1), m.group(2))
        was = m.group(4)
        if was != 'NONE':
            now, how = was, 'the standing arm b680 read'
        elif key in by_rule:
            now, how = by_rule[key], 'TRACEABLE, armed on the author`s word (tools/rule_arms.py)'
        elif key in SUPERSEDED:
            now, how = SUPERSEDED[key] + ' (through b678 row 1)', 'TRACEABLE, SUPERSEDED by data/b678_rules.txt row 1; read through its arm, no arm of its own'
        elif key in PROSE:
            now, how = 'NONE', 'PROSE: read at the step-zero citation check and in the defects banks'
        else:
            now, how = 'NONE', '### UNSORTED'
        rows.append((m.group(1), m.group(2), m.group(3), was, now, how, m.group(5).strip()))
    none_before = sum(1 for r in rows if r[3] == 'NONE')
    none_now = sum(1 for r in rows if r[4] == 'NONE')
    L = ['b683 -- COMPONENT 4, (R293)(6): THE RULES-TO-ARMS BANK RE-READ AFTER THE ARMS (%s)' % utc(), '',
         '### rows are rules: act ; row ; bank :line ; the arm b680 read ; the arm now ; how ; its head. Read from data/b680_rules_arms.txt :7-:32',
         '### through the arms of tools/rule_arms.py, the author`s word on the sort (data/b683_author_answers.txt), the sort at data/b683_arms_sort.txt.', '']
    L += ['  %s  row %s  %-28s b680 %-22s now %-44s %s -- %s' % (r[0], r[1], r[2], r[3], r[4], r[5], r[6]) for r in rows]
    L += ['', '### ### **RULE ROWS %d ; NONE AT b680 %d ; NONE NOW %d (expected 3, the PROSE rules) ; ARMED NOW BY THE WORD %d ; THROUGH ANOTHER`S ARM %d ; '
              'UNSORTED %d.**' % (len(rows), none_before, none_now, sum(1 for r in rows if r[3] == 'NONE' and r[4].startswith('G-RULE-') and '(through' not in r[4]),
                                  sum(1 for r in rows if '(through' in r[4]), sum(1 for r in rows if 'UNSORTED' in r[5]))]
    put_txt('b683_rules_arms.txt', L)
    print(NL.join(L[-1:]))


# ================================================================================ THE LATE ROUTES (b682's, carried; every row read through READERS)
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
    """(R293)(7): a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
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
    L = ['b683 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE DISPATCHES, THE MOVES AND DELETES (%s)' % utc(), '',
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
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R293)(7): one branch per command, no glob in any half): ' + '; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes)]
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; MOVE OR DELETE '
              'COMMANDS %d ; BRANCH DELETES OF ONE BRANCH AND NO GLOB %d OF %d.**' % (len(rows), len(hits), len(lean), len(disp), len(detach), len(mv),
                                                                                   sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl), len(shapes))]
    put_txt('b683_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b683_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
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
    put_json('b683_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (no kernel written this act)' % len(ks))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b683_defects.txt').split(NL)
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
    t = rdn('b683_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b683_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b683_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b683_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


REPAIRS = [
    ('THE SUITE`S STANDING SET FOR b683, ON THE AUTHOR`S WORD ON THE SORT (answering no defect: (R293)(6) adds standing arms): tools/b683_checks.py`s',
     'standing arms are b682`s face`s (G2) arms less b682`s act arms, carried, and the twenty G-RULE arms of tools/rule_arms.py added as standing',
     '(the worklist`s STANDING_ADDED, N5 amended to them); the instruments take in b682`s sealed tools, tools/correspondence_gen.py and its test',
     '(no longer the act`s object) and leave out this act`s own; G-PP-SCOPE reads the two ledgers alone; G-CURRENTS-UNEDITED takes in',
     'FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md; the standing runner arms read the last merged run, b682`s SIDE-bijection run 39126858721,',
     'from b682`s banks; G-CLOSING-SENTENCE reads this act`s closing sections (the map, the hypotheses, the arms).'),
    ('THE MAP WRAPPER`S HYPOTHESES ROUTE (answering defect (a)): tools/b683_epstein_map_angle.py `hyp` read the ball reading`s hrate from a JSON',
     'key the b677 tool does not bank and compared 0 j; it reads the run bank`s own hrate lines after the 400-bit marker (`_ball_hrate`), before',
     'the seal; the map itself not re-run.'),
    ('THE RULE ARMS` TRANSCRIPT READER AND TWO READERS, BEFORE ANY ARM WAS DECLARED (answering their first exercise at HEAD, before the face):',
     'tools/rule_arms.py read tool calls from the api-request-blob lines too (copies without ids, so every call fell into one message); it',
     'reads the assistant lines alone; the consumers reader took a plan title naming the section for the section, and reads the "== n." header;',
     'the naming reader took b200`s sector naming bank, and reads from the rule`s act, b674.'),
    ('THE SCORE ROUTES` TWO READERS (answering their dry run on the real banks before the seal, data/b672_rules.txt row 3): N2 searched the',
     'plan for the H3 and H4 quotations line by line and the quotations wrap, so it read False; it reads the plan joined. N4 asked every',
     'TRACEABLE row for its own trace and failing reading, and the SUPERSEDED row (23) gives its trace as row (24)`s; it reads that row so.',
     'The same two readers in tools/b683_checks.py (G-PLAN-BEFORE-RUN, G-ARMS-SORTED) repaired alike.'),
]


def repairs(*a):
    """data/b683_tool_repairs.txt: rows are repairs with the defect they answer. Each tool carried from a sealed b682 copy is read against
    b682's seal hash (relay data/b682_seal_hashes.json) first, and its diff against that copy counted by hunks."""
    import hashlib
    seal = jl('b682_seal_hashes.json').get('tools') or {}
    rows = []
    for t0 in ('b682_citation.py', 'b682_closing.py', 'b682_reg_gate.py', 'b682_regspec.py', 'b682_tests.py', 'b682_worklist.py',
               'b682_record.py', 'b682_checks.py'):
        t1 = t0.replace('b682_', 'b683_')
        old, new = os.path.join(T, t0), os.path.join(T, t1)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
        rows.append((t0, t1, now, seal.get(t0), len(re.split(r'(?m)^(?=@@ )', d)[1:])))
    L = ['b683 -- COMPONENT 5, (R293)`S FERRY: THE CARRY-TIME READING OF THE TOOLS, AGAINST b682`S SEALED COPIES (%s)' % utc(), '',
         '### rows are the carried tools: b682`s sealed copy and its seal record; the hunks of the diff to b683`s copy. Every hunk is the act`s own',
         '### text -- its names, its banks, its sections and its predicates over this act`s banks -- save the repairs below, each with the defect',
         '### it answers. This act`s new tools: tools/b683_epstein_map_angle.py (the run`s wrapper) and tools/rule_arms.py (the twenty arms).', '']
    for t0, t1, now, s, nh in rows:
        L.append('  %-20s -> %-20s b682 sealed %s ; the seal`s record %s ; %s ; hunks %d' % (t0, t1, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh))
    L.append('')
    for i, r in enumerate(REPAIRS, 1):
        L += ['  REPAIR %d -- %s' % (i, r[0])] + ['  ' + x for x in r[1:]]
    L += ['', '### ### **REPAIRS %d ; THE SEALED COPIES %s ; TOOLS CARRIED %d.**' % (
        len(REPAIRS), 'AGREE' if all(s == now for _a, _b, now, s, _n in rows) else '### DIFFER', len(rows))]
    put_txt('b683_tool_repairs.txt', L)
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


ROOT_EXCLUDE = re.compile(r'^b683_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*)\.?(txt|json|md|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b683_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(K.SHARED_APPENDED))


def rootbanks(*a):
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['b683 -- G-ROOT-BANKS-COMMITTED`S READING: THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ;'
         ' carried by HEAD ; HEAD`s blob equal to the file' % utc(), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('b683_root_banks.txt', L)
    put_json('b683_root_banks.json', dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b683_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### G-ROOT-BANKS-COMMITTED: A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b683'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b683_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='b683_ra_') as tmp:
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
    L = ['b683 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b683_root_arm.txt', L)
    put_json('b683_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b683 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b683_table_final.txt', L)
    put_json('b683_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b683_registration_2026-10-18.txt'
FACE = os.path.join(D, 'b683_registration_2026-10-18.txt')


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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b683_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b683_regspec.py')], 'b683_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b683_satisfiable.json', '--emit', 'b683'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b683_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b683_census_stepzero.txt'), ('b327_faces_census.py', 'b683_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b683_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b683'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b683_reg_gate.txt', 'data/b683_reg_termscan.txt', 'data/b683_regspec_run.txt', 'data/audit_b683_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES: (N1)-(N5) OF THE FERRY, THE SEAT'S (S1)-(S3)
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b682_closing_push_out.txt', 'b670_work_orders.txt')
N5_RELAY_TOOLS = ('rule_arms.py',)
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
VL = re.compile(r'### ### \*\*(.*?)\*\*')
PLAN_COMMIT, SORT_COMMIT = 'ba0f2b34', 'dfef47b8'


def TRAIL_HEAD():
    return ('### b683 — lane two, act one hundred and ten, the research act under (R293): the detection map in the angle form over the b681 '
            'balls, its controls and H3 and H4 read; the 24 rules sorted and the traceable ones armed')


def _calls():
    return jl('b683_author_answers.json').get('calls') or []


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


def _first_commit_ct(path):
    t = g(RELAY, 'log', '--reverse', '--format=%ct', '%s..HEAD' % K.PRE_RELAY, '--', path).split()
    return int(t[0]) if t and t[0].isdigit() else None


def _bank_ts(name):
    m = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', (rdn(name).split(NL) or [''])[0]) or re.search(r'(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', rdn(name))
    return _iso(m.group(1)) if m else None


def _map_counts():
    t = rdn('b683_map.txt')
    rows = re.findall(r'^  (THE CONTROL Z₁\(0\.8, 29\.6\)|Q0 AT qE0)\s+(\d+) j\s*(\d+) : angle rad \S+ ; (.*?) ; rad max (\S+) ; rad/bar (\S+) ; (\w+)', t, re.M)
    radded = all(len(re.findall(r'\|mid\| \S+ rad \S+', r[3])) == 4 for r in rows)
    return rows, radded


def _n1():
    cm = jl('b683_commands.json')
    ok = bool(cm) and not cm.get('local_lean')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches %d (relay data/b683_commands.txt, %d commands read)' % (
            cm.get('local_lean') if cm else '### UNREAD', len(cm.get('dispatches') or []), len(cm.get('rows') or [])))


def _n2():
    plan = ' '.join(rdn('b683_map_plan.txt').split())          # ### the quotations wrap across the plan's lines
    t_plan, t_run, t_chain = _git_ct(RELAY, PLAN_COMMIT), _bank_ts('b683_map_run.txt'), _bank_ts('b683_chain.txt')
    q3 = 'every hypothesis of zeroSide_neg_at_rate_cfg certifies by name and hrate holds at some j₀ ≤ D' in plan
    q4 = 'prints j₀ = 38 and a zero side below zero, each with its ball' in plan
    run = rdn('b683_map_run.txt')
    tally = re.search(r'powers in the angle form (\d+) ; squares by one product of a ball holding 0 (\d+)', run)
    rows, radded = _map_counts()
    chain_ok = 'THE CHAIN VERIFIED ; FILES 7 EQUAL 7' in rdn('b683_chain.txt')
    ok = q3 and q4 and bool(t_plan and t_run and t_chain) and t_plan < t_run and t_chain <= t_run and chain_ok and bool(tally) \
        and tally.group(2) == '0' and len(rows) == 123 and radded
    return ('HELD' if ok else 'REFUTED'), (
        'H3 (b663 :131) and H4 (b667 :124-:125) quoted in the plan (relay data/b683_map_plan.txt, committed %s) before the run (data/b683_map_run.txt): %s, %s; '
        'the hash chain VERIFIED 7 of 7 (data/b683_chain.txt) in the run`s own process before any ball was read: %s; every one of the %d rows of '
        'data/b683_map.txt carries its four residuals` radii: %s; powers in the angle form %s, squares by one product of a ball holding 0 %s' % (
            PLAN_COMMIT, q3, q4, chain_ok, len(rows), radded, tally.group(1) if tally else '?', tally.group(2) if tally else '?'))


def _n3():
    rows, _r = _map_counts()
    h = rdn('b683_map_h.txt')
    cells = collections.Counter((c, int(b)) for c, b, _j, *_rest in rows)
    ok = len(rows) == 123 and cells == collections.Counter({('THE CONTROL Z₁(0.8, 29.6)', 200): 41, ('Q0 AT qE0', 200): 41, ('Q0 AT qE0', 400): 41}) \
        and 'ROWS 123 (the b671 list: 41 + 41 + 41) ; NONE DROPPED True' in rdn('b683_map.txt') \
        and 'data/b663_epstein_plan.txt :131' in h and 'data/b667_epstein_plan.txt :124-:125' in h and 'data/b683_map_run.txt' in h
    return ('HELD' if ok else 'REFUTED'), (
        'b671`s 123 controls re-planted and read, none dropped (Z₁ 41, Q0 41 at 200 bits, 41 at 400 -- the rung forced by the ruling): %s; H3 and '
        'H4 cite their plans by line and the run bank that decides them (relay data/b683_map_h.txt)' % dict(cells))


def _n4():
    srt = rdn('b683_arms_sort.txt')
    t_sort, t_arms = _git_ct(RELAY, SORT_COMMIT), _first_commit_ct('tools/rule_arms.py')
    calls = _calls()
    t_prompt = _iso(calls[1]['ts']) if len(calls) > 1 else None
    rows = re.findall(r'^  \((\d+)\)\s+(b\d{3} row \d+)', srt, re.M)
    keys = [k for _n, k in rows]
    trace_ok = all(('trace:' in blk and 'fails:' in blk) or ('STATE SUPERSEDED' in blk and re.search(r"its trace is row \(\d+\)'s", blk))
                   for blk in re.split(r'(?m)^  \(\d+\)', srt)[1:] if 'SORT TRACEABLE' in blk)
    ok = len(rows) == 24 and len(set(keys)) == 24 and trace_ok and bool(t_sort and t_prompt) and t_sort < t_prompt \
        and (t_arms is None or t_prompt < t_arms)
    return ('HELD' if ok else 'REFUTED'), (
        'the sort prints the 24 rules once each (%d rows, %d distinct), every TRACEABLE row with its trace and failing reading %s (relay '
        'data/b683_arms_sort.txt, committed %s) before the prompt; no arm written before the author`s word: tools/rule_arms.py first committed '
        'after the answer %s' % (len(rows), len(set(keys)), trace_ok, SORT_COMMIT, t_arms is None or (t_prompt is not None and t_prompt < t_arms)))


def _n5():
    import rule_arms as RA
    face = jl('b683_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b683_|audit_b683_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA)
                                                or (x.startswith('tools/') and x[6:] in N5_RELAY_TOOLS))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import importlib
    argv, sys.argv = sys.argv, sys.argv[:1]
    try:
        CH = importlib.import_module('b683_checks')
    finally:
        sys.argv = argv
    new_arms = sorted(set(a_[0] for a_ in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = k_ok and not pp_beyond and not kinds_beyond and not differ and new_arms == sorted(RA.NAMES) and sorted(K.STANDING_ADDED) == sorted(RA.NAMES) \
        and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it, no kernel main written %s; '
            'PLACE-papers beyond FINDINGS and OPEN_TRAILS: %s; standing arms added: %d, the twenty the author`s word on (R293)(6) names %s (N5 '
            'amended to them; the act`s arms over its own banks %d); sealed tools not agreeing %s; relay files of a kind beyond the act`s banks and '
            'tools, the arms` module, the table, the root list, b682`s push-out bank and the orders bank`s rows: %s; "patent" in the lines written: '
            '%s; outbound requests: the seat`s git reads and pushes at github.com, no identifier of the author placed in a request; the mirror zip '
            'outside every repository' % (K.DRAFT, k_ok, pp_beyond or 'NONE', len(new_arms), new_arms == sorted(RA.NAMES), len(K.ACT_ARMS),
                                          differ or 'NONE', kinds_beyond or 'NONE', pat or 'NONE'))


def scores(*a):
    TF, RA_ = jl('b683_table_final.json'), jl('b683_root_arm.json')
    _r, _n, sh = seal_hashes()
    S = {
        'N1': _n1(), 'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:700]))
    if 'dry' in a:
        return
    put_json('b683_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _mh():
    return jl('b683_map_h.json')


def _title():
    m = _mh()
    big = max((r for _b, r in m.get('rad64') or [(0, 0.0)]), default=0.0)
    return ('## The detection map in the angle form over the 1e-30 balls at Q0: controls %d of %d; radius at j = 64 %.2e against the bar 9.54e-7; '
            'H3 %s, j₀ = %s; H4 %s, hQtie %s of 41; W-ORD-MAP-ANGLE-FORM DISCHARGED; rules sorted 21 TRACEABLE / 3 PROSE, 20 arms added' % (
                m.get('pass_all', 0), m.get('rows', 0), big, 'HELD' if m.get('H3') else 'REFUTED', m.get('j0'),
                'HELD' if m.get('H4_held') else m.get('H4', '?'), (m.get('hqtie') or ['?'])[0]))


def _finding_text():
    S, J, m = jl('b683_scores.json'), jl('b683_act_root.json'), _mh()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b683_author_answers.txt'), re.M))
    c1 = _rl_lines('b683_record_lines.json') + ['?']
    c3 = _rl_lines('b683_landing.json') + ['?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    ra = re.search(r'NONE NOW (\d+)', rdn('b683_rules_arms.txt'))
    rad = dict((b_, r) for b_, r in m.get('rad64') or [])
    e = ['', _title(), '',
         'Over the 163 certified zeros of Q0 narrowed to half-width 1e-30, the detection map in the angle form passes every one of its 123 tie '
         'controls to j = 64, so its instrument reads; on it, every hypothesis of zeroSide_neg_at_rate_cfg certifies by name at Q0, hrate holds '
         'at j₀ = 38 and the zero side at j₀ is below zero in certified arithmetic -- with hA certified by the named premise P3 (Q0Count, stated, '
         'not proved), so the reading holds on that premise. Nothing here proves RH or GRH.', '',
         '*Filed at b683 on the author’s ruling `(R293)`%s. Banks: relay `data/b683_map_plan.txt`, `data/b683_chain.txt`, `data/b683_map.txt`, '
         '`data/b683_map_run.txt`, `data/b683_map_h.txt`, `data/b683_landing.txt`, `data/b683_arms_sort.txt`, `data/b683_rules_arms.txt`, '
         '`data/b683_act_root.txt`; the tools `tools/b683_epstein_map_angle.py` (b677’s map imported unchanged) and `tools/rule_arms.py`.*' % (
             (' and the author’s and navigator’s answers (%d questions)' % n_ans) if n_ans else ''), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed. b682 at its weight (FINDINGS :%s).' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', c1[0]), '',
         '**The plan** (`(R293)`(3)): b677’s plan carried by section with every figure re-read for 1e-30; the hash chain of the b681 bank '
         'verified 7 of 7 before any ball was read; the price at j = 64 1.3e-10 to 7.7e-8 against the bar 9.54e-7, b677’s measurement scaled '
         '2.05e-9; H3 quoted from the b663 plan :131 and H4 from the b667 plan :124–:125; one prompt, answered: run as planned, the 400-bit rung '
         'forced by the ruling so all 123 rows are read.', '',
         '**The map** (`(R293)`(4)): controls %d of %d PASS -- Z₁ 41, Q0 41 at 200 bits and 41 at 400; of the 46 b671 read INSTRUMENT, 46 PASS '
         '(H1 HELD); the radius at j = 64 %.3e at 200 bits and %.3e at 400 against the bar, %.2e of it (H2 HELD); every power exp(n·log z), no '
         'square of a ball holding 0 by product.' % (m.get('pass_all', 0), m.get('rows', 0), rad.get(200, 0.0), rad.get(400, 0.0),
                                                      max(rad.values() or [0.0]) / K.BAR), '',
         '**The hypotheses**: H3 HELD, j₀ = %s ≤ D + 40 = 64, hQtie %s of 41 and every hypothesis certified by name (hA on P3); H4 SCORABLE and '
         'HELD, j₀ = 38 and the zero side below 0 with its ball; H5 HELD, b677’s instrument-side reading (hQtie from coeffs_exist and the orbit '
         'identity) agreeing with the ball reading at all 15 j where both exist, 24–38. `W-ORD-MAP-ANGLE-FORM` DISCHARGED (OPEN_TRAILS :%s), its '
         'pin relay data/b683_map.txt; the bench line’s draft held in data/b683_landing.txt for a later act.' % (
             m.get('j0'), (m.get('hqtie') or ['?'])[0], c3[0]), '',
         '**The arms** (`(R293)`(6)): the 24 rules without arms sorted 21 TRACEABLE (15 live, 5 declaration-only, 1 superseded) and 3 PROSE; on '
         'the author’s word, twenty standing VALUE arms G-RULE-<name> in tools/rule_arms.py, the five declaration-only arms VACUOUS until a '
         'declaration is written, the walk arm from b684 with b679’s untipped walk bank the breach before its floor; the rules-to-arms bank '
         're-read, NONE %s of 24.' % (ra.group(1) if ra else '?'), '',
         '**The root.** b683 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b677’s map and b681’s narrowing through each other -- the width '
         'b677 measured as the consumer’s tolerance is the width b681 reached, and the map passes on it as priced. It strengthens the '
         'programme’s offering of a certified detection reading at Q0 whose instrument is shown to pass before its object reading is taken, and '
         'of standing rules that a suite now reads.', '',
         '**Carried to:** `W-ORD-EPSTEIN-COUNT` (the premise P3 the reading rests on, b685’s candidate); the re-cut residues of b674, b676 and '
         'b678 (b684); the bench line’s draft; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the 400-bit rung forced at Q0 by a named trigger in the wrapper, so b671’s 400-bit rows are read where the tool alone would '
              'not re-read them; (2) H4 read on b677’s angle-form map, the b667 map’s computation lines in the angle form, as b677 read it; (3) a '
              'declaration, for the five declaration-only arms, is a bank or ledger line of the form “DECLARED: <state> MET”; (4) the progress arm '
              'reads banks from b672, b671’s being the table read after its run; (5) the dispatch arm reads every runner bank from b673')


def _trail_text():
    S, J = jl('b683_scores.json'), jl('b683_act_root.json')
    fj = jl('b683_findings.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b683_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b683_record_lines.json') + ['?']
    c3 = _rl_lines('b683_landing.json') + ['?']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R293) ratified.** (1) b682 at its weight. (2) The object. (3) The plan. (4) The run. (5) The landing. (6) The arms. (7) The '
             'branches. (8) The tests. (9) The read-first bank. (10) The draft held at v5. (11) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b682’s weight), :%s (the entry); OPEN_TRAILS.md:%s (`W-ORD-MAP-ANGLE-FORM` DISCHARGED); this record.' % (
                 c1[0], fj.get('entry_line'), c3[0]), '',
             '**Act root:** b683 `%s` (previous `%s`, b682’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d call%s (relay data/b683_author_answers.txt); none after the root.' % (
                 n_ans, len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The map:** 123 of 123 controls PASS over the 1e-30 balls; the radius at j = 64 about 2.1e-9 against 2^-20; H1–H5 HELD, H3 at j₀ = 38 '
             'on the premise P3 (relay data/b683_map.txt, data/b683_map_h.txt).', '',
             '**The arms:** 20 standing G-RULE arms on the author’s word (tools/rule_arms.py); NONE 3 of 24, the PROSE rules (relay '
             'data/b683_rules_arms.txt).', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b683_closing.txt).', '',
             '**The open orders:** `W-ORD-EPSTEIN-COUNT` (b685, on the author’s placement); `W-ORD-LEDGER-SPLIT-RESOLVER` (on the author’s word); '
             '`W-ORD-CHAIN-PAGE-B638-CASES`; `W-ORD-PRINT-TARGETS`; `W-ORD-ONE-COPY`; `W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; '
             '`W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; `W-ORD-ROOT-BINARY-BANK`.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b683_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.**', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b683_scores.json')
    L = ['=' * 104, 'b683 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b683_defects.txt').rstrip(NL).split(NL)
    put_txt('b683_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b683_scores.json', 'b683_findings.json', 'b683_trail.json', 'b683_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b683_record_lines.json') + ['?']
    c3 = _rl_lines('b683_landing.json') + ['?']
    L = ['b683 -- THE COMPONENTS, BANKED UNDER (R293).', '',
         '### COMPONENT 0 : the citation check (data/b683_citation_check.txt), step zero (data/b683_ferry.txt, data/b683_readfirst.txt, '
         'data/b683_stepzero.txt, data/b683_tests_stepzero.txt, data/b683_rowgen_stepzero.txt, data/b683_branches.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b682`s weight FINDINGS :%s' % c1[0],
         '### COMPONENT 2 : the plan (data/b683_map_plan.txt at %s), the chain (data/b683_chain.txt), one prompt ; N2 %s' % (PLAN_COMMIT, S['N2'][0]),
         '### COMPONENT 3 : the map (data/b683_map.txt, data/b683_map_run.txt), the hypotheses (data/b683_map_h.txt), the landing '
         '(data/b683_landing.txt), the order DISCHARGED OPEN_TRAILS :%s ; N3 %s' % (c3[0], S['N3'][0]),
         '### COMPONENT 4 : the sort (data/b683_arms_sort.txt at %s), one prompt, the twenty arms (tools/rule_arms.py), the re-read '
         '(data/b683_rules_arms.txt) ; N4 %s' % (SORT_COMMIT, S['N4'][0]),
         '### COMPONENT 5 : the carry-time reading (data/b683_tool_repairs.txt), the dry-run steps (data/b683_reg_gate.txt), the seal '
         '(data/b683_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N5'][0])]
    put_txt('b683_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b683_findings.json', dict(title=t))
    j = jl('b683_findings.json')
    j['entry_line'] = ln
    put_json('b683_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b683_trail.json', {})
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


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b682's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '2026-10-18-b683'
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
    put_json('b683_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b683':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b683`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b683_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b683_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b683_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b683 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b683 (the last export b682`s, D:/MY-DOwnloads/mirror-refresh-2026-10-18-b682.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b683_mirror.txt', L)
    put_json('b683_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, answers=answers, c3=c3, rulesarms=rulesarms,
              mbuild=mbuild, mroot=mroot, mverify=mverify, mbank=mbank,
              commands=commands, kernels=kernels, defects=defects, repairs=repairs,
              rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final, gatebanks=gatebanks, scores=scores,
              desk=desk, components=components, findings=findings, trail=trail, drycheck=drycheck)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b683_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
