# -*- coding: utf-8 -*-
"""b694_record.py -- THE ACT'S RECORD TOOL, b694 under (R304).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b694's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b693_record.py in stages: the helpers, the guarded landing, the readers, step zero's rowgen and branches
### routes and the answers route first (stage one); Component 1's weight line and corrigendum at Component 1; the circuit and witness routes
### at Components 2-3; the late routes at Component 4. Every python child is started as `python -X utf8`, no environment mapping passed.
### Routes: `python tools/b694_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
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
import b694_worklist as K          # noqa: E402

SP = K.SP
STANDIN = 'standin' in sys.argv[2:]          # ### the dry-run step's stand-ins, by argument (environment variables left as they are)
RELAY = ROOT
ACT, PREV = 'b694', 'b693'


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
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def grc(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').returncode


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b694's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, '%s_scanfile_%s.md' % (ACT, tag))
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


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R304)(1)
WH = ('*Appended 2026-10-20 by b694 to b693’s entry (:9506), under `(R304)`(1) -- b693 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b693_closing.txt):*')
WB = (' “b693 closed: relay a96d5c38, PLACE-papers dba03d2; suite 121 of 122; root eb2323dc6295a480…; 4 prompts answered; 8 defects” '
      '(data/b693_closing.txt :1), the closing 48ca2540 pushed and read back at relay main (data/b693_closing_push_out.txt :5). The host rebooted '
      'between relay 0574078e (Components 0-3 done) and 91c2df0c (the resume bank, data/b693_resume.txt, committed alone), entered as an event; '
      'the act resumed from the tree and the banks in a new session and ran Components 4-5 after it. The four mid-act answers carried out: '
      'b692’s weight line with both triage figures (FINDINGS :9498); the closing tool reading its defects range from the bank, “(a)–(m)” on '
      'b692’s (data/b693_range_exercise.txt); the chain split by act, standing-b2 over b624-b658 carrying no arm and standing-b3 over b659-b693 '
      'running G-ACTROOT-VERIFY once over both halves, the boundary b658 -> b659 equal in both, the whole-chain control 70 of 70 AGREE and the '
      'three verdicts equal (data/b693_chain_control.txt); push-b693-root pushed alone by push_gated’s branch mode and read back at 59de04e1, '
      'main pushed from it (data/b693_root_branch_push_out.txt :9, data/b693_root_push_out.txt). The re-cut: SIDE-archimedean, 2 rows outside '
      'LICENSED/CITED to 0, tag v0.1.1, prints equal, 3 quoting lines each a residue carried (data/b693_cut.txt :28). The suite 121 of 122 before '
      'and after the push, G-DELETES-ONE-BRANCH failing all act and declared on the face, each of step zero’s eight deletes chained with '
      '“; echo EXIT $?” (data/b693_checks.txt, data/b693_checks_postpush.txt; data/b693_defects.txt (f) :33). The closing’s push-b693-root row '
      'printed ABSENT (data/b693_closing.txt :226) where ls-remote showed the branch at 59de04e1: the sealed closing tool looked the remote up '
      'under D:\\relay while its reads were stored under D:/relay (data/b693_defects.txt (h) :47; the corrigendum beneath). A transient empty '
      'remote read of SIDE-fano-darkness at the post-push standing-a run’s opening read, read directly and alone, entered as an event, the part '
      're-run alone. Eight defects (a)-(h) (data/b693_defects.txt :7-:54): (a) the faces page the generator now lists differently, found at '
      'step zero; (b) the navigator’s, two misses of the ruling; (c) stream redirects at the resume; (d) listings through a shell filter; (e) a '
      'bank read through an interpreter’s print; (f) the chained deletes; (g) three first forms of the carried suite and record tool caught by '
      'their own pre-run and repaired before the seal; (h) the closing row. The root eb2323dc over 71 banks (data/act_roots.txt); the entry at '
      'FINDINGS :9506 and the trail at OPEN_TRAILS :15138 carrying the root; the sealed tools 15 of 15 at the close (data/b693_closing.txt :21); '
      'mirror-refresh-2026-10-19-b693.zip CLEAN with the root line (data/b693_closing.txt :43). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B693_ENTRY,
         check=[('FINDINGS.md', K.B693_ENTRY, '## SIDE-archimedean re-cut: 2 rows outside LICENSED/CITED to 0, v0.1.1'),
                ('OPEN_TRAILS.md', K.B693_TRAIL, '### b693')], dry=dry)


# ================================================================================ THE READERS, ONE PER ROW SHAPE A ROUTE READS ((R263)(3))
BRANCH_FATES = ('DELETED', 'KEPT', 'RAISED')


def read_branch_row(r):
    """a row of data/b694_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


READERS = ['read_branch_row']


# ================================================================================ STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE (b670's route, carried)
def roster():
    """the 19 roster tables of data/b586_corroboration.txt :34, at the paths that bank read (carried from b670_record.py :548-:552)."""
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b694_rowgen_<stage>.txt."""
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
    L = ['%s -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (ACT, stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('%s_rowgen_%s.txt' % (ACT, stage), L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R304)(5))
def _remote_tip(repo, b):
    out = g(repo, 'ls-remote', 'origin', 'refs/heads/' + b)
    return out.split('\t')[0].strip() if '\t' in out else ''


def branches(*a):
    """every branch (R304)(5) names for step zero, its tip read before any delete, whether --merged lists it, its fate DELETED; the two remote
    branches read by one ls-remote each, in sequence; any branch of b693 that --merged lists and the ruling does not name, reported and KEPT.
    data/b694_branches.txt (.json)."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    for repo, b in K.DELETE_REMOTE:
        tip = _remote_tip(repo, b)
        merged = bool(tip) and grc(repo, 'merge-base', '--is-ancestor', tip, 'main') == 0
        rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=merged, fate='DELETED'))
    named = set((r['repo'], r['branch']) for r in rows)
    extra = []
    for repo in sorted(set(r_ for r_, _bs in K.DELETE)):
        for x in g(repo, 'branch', '--merged', 'main', '--format=%(refname:short)').split(NL):
            x = x.strip()
            if (x.startswith('push-' + PREV) or x.endswith('-' + PREV)) and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R304)(5): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % (ACT, utc()), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; merged into main ; fate. The ten named deleted by name in the house',
         '### form after --merged lists each, each delete command naming one branch with no glob in any half, one command per message, in sequence,',
         '### nothing chained after any (data/b694_rules.txt row (1)).', '',
         '### THE TEN (R304)(5) NAMES:']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### branches of %s that --merged lists and the ruling does not name (reported and KEPT): %s' % (PREV, ', '.join(
        '%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **NAMED %d (MERGED %d) ; UNNAMED OF %s %d.**' % (len(rows), sum(1 for r in rows if r['merged']), PREV, len(extra))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[list(x) for x in extra]))
    print(NL.join(L[7:]))


# ================================================================================ THE ANSWERS BANK (b693's route, carried)
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
    """data/b694_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
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
    head = ['### %s -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                ACT, n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('%s_author_answers.txt' % ACT, [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('%s_author_answers.json' % ACT, dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                                for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE CARRY-TIME REPAIRS BANK ((R304)(2))
def _fn_src(src, name):
    """a top-level def's source, from its `def` line to the next top-level statement."""
    L = src.split(NL)
    i = next((k for k, l in enumerate(L) if l.startswith('def %s(' % name)), None)
    if i is None:
        return []
    j = next((k for k in range(i + 1, len(L)) if L[k] and not L[k].startswith((' ', '#', ')'))), len(L))
    while j > i and not L[j - 1].strip():
        j -= 1
    return L[i:j]


REPAIR_FNS = ('repo_key', '_ls', 'read_remotes', 'remote_refs', 'remote_tag')


def repairs(*a):
    """data/b694_tool_repairs.txt: rows are repairs with the defect they answer; each diff beneath its row (difflib, unified, over the functions
    the repair touches, b693's sealed copy against this act's), and the row that printed ABSENT beside its repaired form."""
    import difflib
    import hashlib
    old, new = rd(os.path.join(T, 'b693_closing.py')), rd(os.path.join(T, 'b694_closing.py'))
    ob, nb = [hashlib.sha256(open(os.path.join(T, n), 'rb').read()).hexdigest()[:16] for n in ('b693_closing.py', 'b694_closing.py')]
    sealed = (jl('b693_seal_hashes.json').get('tools') or {}).get('b693_closing.py', '')
    o_lines, n_lines = [], []
    for f in REPAIR_FNS:
        o_lines += _fn_src(old, f) + ['']
        n_lines += _fn_src(new, f) + ['']
    o_row = [l for l in old.split(NL) if 'push-b693-root' in l and 'remote_refs' in l]
    n_row = [l for l in new.split(NL) if 'push-b693-root' in l and 'remote_refs' in l]
    diff = list(difflib.unified_diff(o_lines + o_row, n_lines + n_row, 'tools/b693_closing.py (the look-up, sealed %s)' % sealed[:16],
                                     'tools/b694_closing.py (the look-up, this act)', lineterm=''))
    lc = rdn('b694_lookup_control.txt')
    ctl = re.findall(r'(?m)^### ### \*\*(.*)\*\*$', lc)
    L = ['%s -- THE CARRY-TIME REPAIRS, UNDER (R304)(2) AND THE AUTHOR`S ANSWERS AT PROMPTS 1 AND 6 (%s)' % (ACT, utc()), '',
         '### rows are repairs with the defect they answer: the tool ; the blob before -> after ; what it answers ; the form ; the reading.',
         '### Each diff beneath its row, written by this route (difflib over the functions the repair touches).', '',
         '  (1) tools/b694_closing.py, carried from tools/b693_closing.py (sha256 %s, its seal %s; this act`s copy %s) -- ANSWERS b693 (h) (relay' % (
             ob, 'AGREE' if sealed[:16] == ob else '### DIFFER', nb),
         '      data/b693_defects.txt :47-:54): the sealed closing`s row asked the remote reads for D:\\relay (its ROOT, by os.path) where they were',
         '      stored under D:/relay, and printed push-b693-root ABSENT (data/b693_closing.txt :226). THE FORM (the author`s answer at prompt 1): one',
         '      key, repo_key(), \'D:/\' + the path below the drive, applied at the store (read_remotes) and at every look-up (remote_refs,',
         '      remote_tag), so D:\\relay, D:/relay and /d/relay (the push tool`s capture form) resolve to one key; the rest of the tool b693`s',
         '      form with b694`s act text. THE READING (data/b694_lookup_control.txt, the author`s answer at prompt 6): %s.' % (ctl[-1].rstrip('.') if ctl else '### NOT RUN'),
         '']
    L += ['      ' + l for l in diff]
    L += ['', '### ### **REPAIRS 1 ; THE CLOSING TOOL`S LOOK-UP UNDER ONE KEY ; THE SEALED b693 COPY %s ; DIFF LINES %d ; THE CONTROL AS WANTED %s.**' % (
        'AGREE' if sealed[:16] == ob else '### DIFFER', len(diff), 'THE CONTROL AS WANTED True' in lc)]
    put_txt('%s_tool_repairs.txt' % ACT, L)
    print(NL.join(L[-1:]))


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, repairs=repairs, c1=c1)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b694_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
