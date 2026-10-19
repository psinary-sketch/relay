# -*- coding: utf-8 -*-
"""b687_record.py -- THE ACT'S RECORD TOOL, b687 under (R297).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b687's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b686_record.py (the helpers, the guarded landing, the readers, step zero's rowgen and branches routes --
### the branches route reading a remote branch and its ancestry this act --, the answers route, the command bank, the defects) in stages: the
### step-zero and Component 1 routes first; the late routes (seal hashes, repairs, root, scores, entry, trail) added at Component 4.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b687_record.py <route> [dry]`.
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
import b687_worklist as K          # noqa: E402

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
    none a number any bank carries; a stand-in run writes no bank. Carried from b686_record.py with b687's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b687_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b687_findings.json': dict(entry_line=99999, title='stand-in'),
        'b687_trail.json': dict(line=99999),
        'b687_act_root.json': dict(root='0' * 64, previous='c51755ee' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b687's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b687_scanfile_%s.md' % tag)
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
    """a row of data/b687_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
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
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b687_rowgen_<stage>.txt."""
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
    L = ['b687 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b687_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R297)(6))
def branches(*a):
    """every branch (R297)(6) names, its tip read before any delete, its fate; the remote branch recut-spinor-b686 read at the remote (one
    ls-remote) with its tip printed as an ancestor of main at v0.1.1; any branch under the push-b686 prefix that --merged lists and the ruling
    does not name, reported and KEPT. data/b687_branches.txt (.json)."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    anc = []
    for repo, b in K.DELETE_REMOTE:
        o = g(repo, 'ls-remote', '--heads', 'origin', b).split()
        tip = o[0] if o else ''
        main_tag = g(repo, 'rev-parse', K.SPINOR_TAG + '^{commit}').strip()
        main = g(repo, 'rev-parse', 'main').strip()
        is_anc = bool(tip) and grc(repo, 'merge-base', '--is-ancestor', tip, main) == 0
        anc.append(dict(repo=repo, branch=b, tip=tip, main=main, tag=K.SPINOR_TAG, tag_commit=main_tag, main_at_tag=main == main_tag, ancestor=is_anc))
        rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=is_anc, fate='DELETED'))
    named = set((r['repo'], r['branch']) for r in rows)
    extra = []
    for repo, _bs in K.DELETE:
        for x in g(repo, 'branch', '--merged', 'main', '--format=%(refname:short)').split(NL):
            x = x.strip()
            if x.startswith('push-b686') and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b687 -- STEP ZERO, (R297)(6): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; listed by `git branch --merged main --list <name>` (for the remote',
         '### branch: its tip an ancestor of main) ; fate. Deleted by name in the house form, each delete command naming one branch with no glob in',
         '### any half, one command per message, in sequence; no branch the ruling does not name.']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                               r['fate']) for r in rows]
    L += ['', '### the remote branch`s ancestry ((R297)(6)): ' + '; '.join(
        '%s %s at the remote %s ; main %s ; %s at %s (main at the tag %s) ; ANCESTOR OF MAIN %s' % (
            os.path.basename(x['repo']), x['branch'], x['tip'], x['main'][:12], x['tag'], x['tag_commit'][:12], x['main_at_tag'], x['ancestor'])
        for x in anc)]
    L += ['', '### branches under the push-b686 prefix that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; TO BE DELETED %d ; UNNAMED UNDER THE PREFIX %d.**' % (
        len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), len(rows), len(extra))]
    put_txt('b687_branches.txt', L)
    put_json('b687_branches.json', dict(at=utc(), rows=rows, ancestry=anc, extra=[list(x) for x in extra]))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R297)(1)
WH = ('*Appended 2026-10-18 by b687 to b686’s entry (:9260), under `(R297)`(1) -- b686 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b686_closing.txt):*')
WB = (' “b686 closed: relay b0249275, PLACE-papers 9b9a7c6; suite 110 of 110; root c51755eea1318579…; 1 prompt answered; 2 defects” '
      '(data/b686_closing.txt :1), the closing pushed and read back at relay 3e547498 (data/b686_closing_push_out.txt). The citation check '
      '72 of 72 after the seat’s own check row was corrected (data/b686_citation_check.txt); b685’s weight line at FINDINGS :9258 with its '
      'head line quoted. The N4 scorer reads the suite banks and the scores bank and not the entry; the scores bank written once before the '
      'entry, N4 and S2 read at the close into data/b686_scores_close.json; the rule at data/b686_rules.txt row (1), the diff in '
      'data/b686_tool_repairs.txt. The three FOUNDATIONS cells (:628-:630) written by the generator alone at PLACE-papers f5111a2, v0.2.1 to '
      'v0.2.2; the distance 55 by b670’s method and 0 at the generator’s claim, as at b682 (data/b686_correspondence_after.txt :12). '
      'SIDE-spinor named at 3 by the larger table (15 rows against SIDE-li-map’s 13, data/b686_naming.txt :57), the workflow and the print '
      'list alone on main, both runner builds DERIVES with 15 prints equal line for line, merged at aca59d1 and tagged v0.1.1; the distance '
      '3 to 1, SpinorLeg.lean :21 “(salt-checked)” carried as R4. Suite 110 of 110 (89 standing, 21 over the act’s banks) pre-push and '
      'post-push, no declared failure; all eight scores HELD at the close; root c51755ee over 57 banks; '
      'mirror-refresh-2026-10-18-b686.zip CLEAN with the root line. Two defects, both the seat’s: (a) the partner copy’s differing lines '
      'given as 4 from a figure the generator stores, the live count 13, all 13 entered under `W-ORD-ONE-COPY` and the diff bank corrected; '
      '(b) a combine call piped into sed after the post-push suite, the third sed across acts, entered and counted in the command bank -- on '
      'which G-EDIT-ROUTE’s reading is extended at b687’s carry to the whole act’s command bank, the closing’s capture included. Nothing '
      'deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b687_record_lines.json', 'c1', entry=K.B686_ENTRY,
         check=[('FINDINGS.md', K.B686_ENTRY, '## '), ('OPEN_TRAILS.md', K.B686_TRAIL, '### b686')], dry=dry)


# ================================================================================ THE ANSWERS BANK (b686's route, carried)
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
    """data/b687_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
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
    for cid, (i, t, _ts) in results.items():      # ### a word opened by BEGIN with no END after it: noted, its text read in the RESULT line above
        for mm in re.finditer(r'="BEGIN(?:(?!END").)*?"(?=, "|\.\s|$)', t or '', re.S):
            if not re.search(r'END"\s*$', mm.group(0)):
                W += ['### NOTE (transcript line %s): a word opened by BEGIN and carrying NO END marker -- %r ... %r; the seat asked before acting '
                      '(the tail check), and the navigator`s answer reads it complete as received, the END dropped by the paste. Its text is the '
                      'RESULT line above.' % (i, mm.group(0)[2:80], mm.group(0)[-60:]), '']
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %s), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b687 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b687_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b687_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE COMMAND BANK (b686's route, carried)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402

SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')
SED = re.compile(r'(^|[;&|(]\s*|\s)sed\s')


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def sed_cmd(cmd):
    """data/b685_rules.txt row (2): a command carrying sed in any form, read outside quoted strings."""
    return SED.search(QUOTED.sub('""', cmd)) is not None


PREV_ACT, PREV_SESSION, PREV_ANCHOR = 'b686', '3bd076e1-80b3-48c6-919f-407447a1df25', 'RULING (R296) BEGIN'
SED_KIND = 'R sed in any form (data/b685_rules.txt row (2))'


def prev_capture():
    """(R297)(1), the carry-time repair of G-EDIT-ROUTE's reading (the navigator's answer on miss (b), option 1): the previous act's capture
    AFTER ITS POST-PUSH SUITE -- every command of b686's session (and its subagents) timestamped at or after the call that combined its
    post-push parts into data/b686_checks_postpush.txt, the closing's commands among them -- read at this act's step zero."""
    rows = ER.capture('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % PREV_SESSION, PREV_ANCHOR,
                      'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % PREV_SESSION)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV_ACT in r['cmd'] and '--combine' in r['cmd']]
    if not first:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE IS NOT IN ITS CAPTURE -- NOTHING READ')
    out = [dict(r, src='%s %s' % (PREV_ACT, r['src'])) for r in rows if r['ts'] >= first[0]]
    for i, r in enumerate(out):
        r['n'] = 'p%d' % (i + 1)
    return out


def edit_route_offences(rows):
    """the arm's offences, repaired: tools/edit_route.py's arms (unchanged) and, beside them, sed in any form (data/b685_rules.txt row (2)),
    read outside quoted strings; [(row, [(kind, text)])] for the offending rows."""
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


def delete_shape(cmd):
    """(R297)(6): a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    return names, [ch for ch in '*?[' if ch in c]


IDENT = ('psinary', 'hotmail', 'seale', 'york', 'orcid', '0009-0008')


def outbound():
    """the act's outbound requests other than git: every WebSearch query, WebFetch URL and subagent prompt from the ruling's line on, read
    from the assistant lines of the session transcript, with the author's identifiers searched in each."""
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
    lean =[r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    mv = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'(^|&&\s*|;\s*)gh workflow run\b', QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'Start-Process|\bnohup\b|run_in_background', r['cmd'])]
    seds = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and sed_cmd(r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    ob = outbound()
    L = ['b687 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE ((R297)(1), the repaired window): %s commands of session %s from %s, '
              'its offences printed whole (%d):' % (len(prev), PREV_SESSION[:8], prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
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
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R297)(6): one branch per command, no glob in any half): ' + ('; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git (web searches, subagent prompts and fetches), each with the author`s identifiers found in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; '
              'MOVE OR DELETE COMMANDS %d ; BRANCH DELETES OF ONE BRANCH AND NO GLOB %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(mv), sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl),
                  len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    put_txt('b687_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b687_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        prev=dict(act=PREV_ACT, session=PREV_SESSION, rows=len(prev),
                                                  offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                        seds=[r['n'] for r in seds], moves_deletes=[r['n'] for r in mv],
                                        delete_shapes=[dict(n=n, deletes=d, globs=gl) for n, d, gl in shapes], outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r in seds:
        print('  sed #%d: %s' % (r['n'], r['cmd'].split(NL)[0][:200]))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b687_defects.txt').split(NL)
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
    t = rdn('b687_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b687_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


# ================================================================================ THE CARRY-TIME READING ((R297)(1); Component 1 and Component 4)
REPAIRS = [
    ('G-EDIT-ROUTE`S READING EXTENDED (answering b686 defect (b) and this act`s (a), under (R297)(1) and the navigator`s answer on miss (b),',
     'option 1; relay data/b687_author_answers.txt): b686`s arm (tools/b686_checks.py :1045, predicate `edit_route_ok` :582-:583) read',
     'ER.scan over its own act`s capture alone, and tools/edit_route.py`s (S) arm reads `sed -i` alone -- so b686`s combine piped into',
     '`sed -n 0p` after its post-push suite, and this act`s five `sed -n` reads, were no offence. b687`s reading, written once in the shared',
     'writer (tools/b687_record.py `prev_capture`, `edit_route_offences`) and read by both the command bank and the arm: (1) the WINDOW -- this',
     'act`s whole capture through the closing, and the previous act`s capture from the call that combined its post-push parts on (its',
     'closing`s commands among them), read at step zero; (2) the OFFENCES -- tools/edit_route.py`s arms unchanged, and beside them sed in any',
     'form (data/b685_rules.txt row (2)), read outside quoted strings. The arm then FAILS for b687 on defect (a) (five commands) and reads',
     'b686`s (b) in the previous act`s window; it is declared on the face by name, and the capture is not trimmed. The diff of the',
     'command bank`s reading and of the arm`s predicate against b686`s sealed copies is printed whole below.'),
    ('THE STANDING SET FOR b687 (answering no defect: the act`s objects): the standing arms are b686`s face`s (G2) arms less b686`s act arms,',
     'the twenty rule arms among them; the runner arms read the last merged runs (b686`s SIDE-spinor runs; this act dispatches none); the',
     'step-zero arms read this act`s banks -- nine branches, one remote row.'),
]


def _fn_src(src, name):
    """a top-level function's source, from its `def` line to the next top-level line; '' where the tool carries no such function."""
    if ('\ndef %s(' % name) not in src:
        return ''
    i = src.index('\ndef %s(' % name) + 1
    m = re.search(r'\n(?=\S)', src[i + 1:])
    return src[i:i + 1 + m.start() + 1] if m else src[i:]


def repairs(*a):
    """data/b687_tool_repairs.txt: rows are repairs with the defect they answer. Each tool carried from a sealed b686 copy is read against
    b686's seal hash (relay data/b686_seal_hashes.json) first, and its diff against that copy counted by hunks (NOT YET CARRIED where the
    act has not written it); tools/rule_arms.py and tools/edit_route.py read against the last seal record naming them (unedited in this act);
    the arm's reading's diff against b686's sealed copies printed whole."""
    import difflib
    import hashlib
    seal = jl('b686_seal_hashes.json').get('tools') or {}
    rows = []
    for t0 in ('b686_citation.py', 'b686_closing.py', 'b686_reg_gate.py', 'b686_regspec.py', 'b686_tests.py', 'b686_worklist.py',
               'b686_record.py', 'b686_checks.py'):
        t1 = t0.replace('b686_', 'b687_')
        old, new = os.path.join(T, t0), os.path.join(T, t1)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        ex = os.path.exists(new)
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8',
                           errors='replace').stdout if ex else ''
        rows.append((t0, t1, now, seal.get(t0), len(re.split(r'(?m)^(?=@@ )', d)[1:]), ex))
    inst = {}
    for t in ('rule_arms.py', 'edit_route.py'):
        nowh = hashlib.sha256(open(os.path.join(T, t), 'rb').read()).hexdigest()
        acts = [x for x in ('b686', 'b685', 'b684', 'b683', 'b682', 'b681') if (jl('%s_seal_hashes.json' % x).get('tools') or {}).get(t)]
        inst[t] = (nowh, acts[0] if acts else None, (jl('%s_seal_hashes.json' % acts[0])['tools'][t]) if acts else None,
                   g(ROOT, 'log', '-1', '--format=%h %cI', '--', 'tools/' + t).strip())
    s6r, s7r = rd(os.path.join(T, 'b686_record.py')), rd(os.path.join(T, 'b687_record.py'))
    s6c, s7c = rd(os.path.join(T, 'b686_checks.py')), rd(os.path.join(T, 'b687_checks.py'))
    nd = []
    for (a6, f6), (a7, f7), s6, s7 in ((('b686_record.py', 'commands'), ('b687_record.py', 'commands'), s6r, s7r),
                                       (('b686_record.py', '(none)'), ('b687_record.py', 'prev_capture'), s6r, s7r),
                                       (('b686_record.py', '(none)'), ('b687_record.py', 'edit_route_offences'), s6r, s7r),
                                       (('b686_checks.py', 'edit_route_ok'), ('b687_checks.py', 'edit_route_ok'), s6c, s7c)):
        nd += list(difflib.unified_diff(_fn_src(s6, f6).split(NL) if f6 != '(none)' else [], _fn_src(s7, f7).split(NL) if s7 else [],
                                        '%s %s (sealed)' % (a6, f6), '%s %s%s' % (a7, f7, '' if s7 else ' (NOT YET CARRIED)'), n=1, lineterm=''))
    L = ['b687 -- COMPONENT 1 AND COMPONENT 4, (R297)`S FERRY: THE CARRY-TIME READING OF THE TOOLS, AGAINST b686`S SEALED COPIES (%s)' % utc(), '',
         '### rows are repairs with the defect they answer, after the carried tools: b686`s sealed copy and its seal record; the hunks of the diff',
         '### to b687`s copy. Every hunk is the act`s own text -- its names, its banks, its sections and its predicates over this act`s banks --',
         '### save the repairs below.', '']
    for t0, t1, now, s, nh, ex in rows:
        L.append('  %-20s -> %-20s b686 sealed %s ; the seal`s record %s ; %s ; hunks %s' % (t0, t1, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh if ex else 'NOT YET CARRIED'))
    for t, (nowh, act, sh, last) in inst.items():
        clean = grc(ROOT, 'diff', '--quiet', 'HEAD', '--', 'tools/' + t) == 0 and grc(ROOT, 'merge-base', '--is-ancestor', last.split()[0], K.PRE_RELAY) == 0
        if sh is None:      # ### no seal record names it: unedited read as the working file equal to HEAD, its last commit before the act
            inst[t] = (nowh, act, nowh if clean else None, last)
        L.append('  %-20s    the standing instrument, unedited in this act: %s ; the last seal record naming it (%s`s) %s ; %s ; its last commit %s%s' % (
            t, nowh[:16], act or 'NONE', (sh or '### NONE')[:16], 'AGREE' if inst[t][2] == nowh else '### DIFFER', last,
            (' ; read by the tree: the working file equal to HEAD and its last commit before the act %s' % clean) if sh is None else ''))
    L.append('')
    for i, r in enumerate(REPAIRS, 1):
        L += ['  REPAIR %d -- %s' % (i, r[0])] + ['  ' + x for x in r[1:]]
    L += ['', '### THE DIFF OF THE COMMAND BANK`S READING AND OF THE ARM`S PREDICATE AGAINST b686`S SEALED COPIES (tools/b686_record.py sha256 %s, '
          'tools/b686_checks.py sha256 %s), WHOLE:' % ((seal.get('b686_record.py') or '### NONE')[:16], (seal.get('b686_checks.py') or '### NONE')[:16])]
    L += ['    ' + l for l in nd]
    carried = sum(1 for r in rows if r[5])
    L += ['', '### ### **REPAIRS %d ; THE SEALED COPIES %s ; TOOLS CARRIED %d OF %d ; THE ARM`S DIFF LINES %d.**' % (
        len(REPAIRS), 'AGREE' if all(s == now for _a, _b, now, s, _n, _e in rows) and all(v[0] == v[2] for v in inst.values()) else '### DIFFER',
        carried, len(rows), len(nd))]
    put_txt('b687_tool_repairs.txt', L)
    print(L[-1])


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, answers=answers, commands=commands, defects=defects, repairs=repairs)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b687_record.py %s [dry]' % ' | '.join(ROUTES))
        sys.exit(2)
    fn(*sys.argv[2:])
