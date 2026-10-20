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


# ================================================================================ COMPONENT 2: THE CLOSURE STEP ON THE RUNNER ((R304)(3); b692's routes, carried)
STD3 = ('propext', 'Classical.choice', 'Quot.sound')


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def dispatch(*a):
    """`dispatch <kernel> <ref sha> <label> <target> [dry]`: ONE dispatch of build-module.yml at main with the ref input and the lake target;
    refused where data/b694_dispatches.json already carries the ref's tree (one dispatch per tree state). The run id read from the run list
    (the newest workflow_dispatch run created after the dispatch); a row banked."""
    kernel, ref, label, target = a[0], a[1], a[2], a[3]
    repo = 'psinary-sketch/' + kernel
    full = g('D:/' + kernel, 'rev-parse', ref).strip()
    tree = g('D:/' + kernel, 'rev-parse', full + '^{tree}').strip()
    j = jl('%s_dispatches.json' % ACT)
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
    put_json('%s_dispatches.json' % ACT, dict(rows=rows))
    print('  dispatched %s ; run id %s' % (t0, run_id))


def runstatus(*a):
    """`runstatus <kernel> <run id>`: the run's status and conclusion, printed only (a foreground read, no wait)."""
    rc, out, err = _gh('run', 'view', a[1], '-R', 'psinary-sketch/' + a[0], '--json', 'status,conclusion,createdAt,updatedAt')
    print('  ' + (out.decode('utf-8', 'replace').strip() or err.strip()))


def _deps(ax):
    """the axioms output read per terminal: [(name, [axioms])], wrapped lists rejoined."""
    out = []
    for n, d in re.findall(r"^'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)",
                           re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', ax), re.M):
        out.append((n, [x.strip() for x in d.split('[', 1)[1].rstrip(']').split(',') if x.strip()] if d.startswith('depends') else []))
    return out


def _wf_list(kernel, ref):
    """the print list at the ref: print_targets.txt where it stands, else the workflow's own `#print axioms` lines (SIDE-lv-conservation's form)."""
    pt = subprocess.run(['git', '-C', 'D:/' + kernel, 'show', '%s:print_targets.txt' % ref], capture_output=True)
    if pt.returncode == 0:
        return [l.strip() for l in pt.stdout.decode('utf-8').split(NL) if l.strip()], 'print_targets.txt'
    wf = g('D:/' + kernel, 'show', '%s:.github/workflows/build-module.yml' % ref)
    return re.findall(r'^\s*#print axioms (\S+)\s*$', wf, re.M), '.github/workflows/build-module.yml`s #print axioms lines'


def read_runner_row(r):
    """a row of data/b694_runner_rows.json: the kernel, its label, the ref (40 hex), the run id and the gate; returns (kernel, label, gate)."""
    if not isinstance(r, dict) or not re.match(r'^SIDE-[\w-]+$', r.get('kernel') or '') or not re.match(r'^[\w-]+$', r.get('label') or '') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['kernel'], r['label'], r['gate']


READERS.append('read_runner_row')


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <tag> <note...>`: b692's route, carried: the run read by its id; the artifact listed, downloaded by
    its id into memory, its sha256 against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low;
    the axioms output banked whole, every name of the list matched to one printed line; the closure step's out/closure.jsonl.gz banked as
    data/b694_circuit_<kernel>_<tag>_<tip>.jsonl.gz beside its text hashes bank (data/b680_rules.txt row (1))."""
    import gzip
    import hashlib
    import io as _io
    import zipfile
    kernel, run_id, ref, label, tag, note = a[0], int(a[1]), a[2], a[3], a[4], ' '.join(a[5:])
    repo = 'psinary-sketch/' + kernel
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(kernel=kernel, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None, closure=None)
    L = ['%s -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (ACT, kernel, label.upper(), utc()), '',
         '### the dispatch: %s ; the ref input %s' % (note, ref),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt'))]
    T_, B_ = {}, {}
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
                    B_[n] = z.read(n)
                    if not n.endswith('.gz'):
                        T_[n] = B_[n].decode('utf-8', 'replace').replace(chr(13), '')
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
    tg, tg_src = _wf_list(kernel, ref)
    printed = [n for n, _d in deps]
    unmatched = [n for n in tg if n not in printed]
    outside = [(n, d) for n, d in deps if not set(d) <= set(STD3)]
    clog = T_.get('closure_log.txt', '').rstrip(NL)
    gzb = B_.get('closure.jsonl.gz')
    cl_rows, cl_head = 0, {}
    if gzb:
        txt = gzip.decompress(gzb).decode('utf-8')
        lines = [l for l in txt.split(NL) if l.strip()]
        cl_head = json.loads(lines[-1]) if lines and '"header"' in lines[-1] else {}
        cl_rows = len(lines) - (1 if cl_head else 0)
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d:' % (row['build_exit'], len(row['errors']))] + ['    ' + l for l in row['errors'][:40]] + [
          '### the log`s last lines:'] + ['    ' + l for l in blog.rstrip(NL).split(NL)[-6:]] + [
          '### the closure step: its log`s last lines:'] + ['    ' + l for l in clog.split(NL)[-8:]] + [
          '### the closure bank: %s' % (('out/closure.jsonl.gz %d bytes, sha256 %s ; records %d ; the header`s count %s ; programme modules %d' % (
              len(gzb), hashlib.sha256(gzb).hexdigest(), cl_rows, cl_head.get('records'), len(cl_head.get('modules') or []))) if gzb else '### NONE IN THE ARTIFACT'),
          '### the print step: the list (%s at the ref) %d names ; terminals printed %d ; every name printed once %s ; axiom-free %d ; '
          'sorryAx %d ; outside the standard three %d' % (
              tg_src, len(tg), len(deps), not unmatched and len(printed) == len(set(printed)) == len(tg), sum(1 for _n, d in deps if not d),
              sum(1 for _n, d in deps if 'sorryAx' in d), len(outside)),
          '### rows are terminals: name | the axioms printed | within the standard three:']
    L += ['  %-62s %s %s' % (n, d, 'STD3' if set(d) <= set(STD3) else '### OUTSIDE') for n, d in deps]
    L += ['  %-62s ### NOT PRINTED' % n for n in unmatched]
    ok = run.get('conclusion') == 'success' and row['artifact_sha256'] and row['build_exit'] == '0' and not row['errors'] and not row['stopped'] \
        and row['mem_low'] is not None and row['mem_low'] >= K.HOLD and deps and not unmatched and not outside
    row['gate'] = 'DERIVES' if ok else 'NOT DERIVES'
    if gzb and row['artifact_sha256']:
        stem = '%s_circuit_%s_%s_%s' % (ACT, kernel, tag, ref[:7])
        p = os.path.join(D, stem + '.jsonl.gz')
        with open(p + '.tmp', 'wb') as fh:
            fh.write(gzb)
        os.replace(p + '.tmp', p)
        row['closure'] = dict(bank=stem + '.jsonl.gz', sha256=hashlib.sha256(gzb).hexdigest(), bytes=len(gzb), records=cl_rows)
        put_txt(stem + '_hashes.txt', [
            '%s -- THE CLOSURE BANK`S HASHES, %s AT %s (the tip %s), BY THE RUNNER (%s)' % (ACT, kernel, tag, ref, utc()), '',
            '### rows are binary banks this text bank roots (data/b680_rules.txt row (1)): the bank | sha256 | bytes | the run | the artifact.',
            '  data/%s.jsonl.gz | %s | %d | run %d | artifact %s sha256 %s' % (stem, row['closure']['sha256'], len(gzb), run_id, art.get('id'),
                                                                            row['artifact_sha256']),
            '', '### ### **RECORDS %d ; THE HEADER`S COUNT %s ; PROGRAMME MODULES %d ; THE REF %s.**' % (
                cl_rows, cl_head.get('records'), len(cl_head.get('modules') or []), ref)])
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d OF %d ; SORRYAX %d ; '
          'OUTSIDE THE STANDARD THREE %d ; CLOSURE RECORDS %d ; GATE %s.**' % (
              run_id, label, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']),
              len(deps), len(tg), sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), cl_rows, row['gate'])]
    read_runner_row(row)
    put_txt('%s_runner_%s_%s.txt' % (ACT, kernel, label), L)
    if row['artifact_sha256']:
        put_txt('%s_axioms_%s_%s.txt' % (ACT, kernel, label), ax.split(NL) if ax else ['### EMPTY'])
        put_txt('%s_closurelog_%s_%s.txt' % (ACT, kernel, label), clog.split(NL) if clog else ['### EMPTY'])
    j = jl('%s_runner_rows.json' % ACT)
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('%s_runner_rows.json' % ACT, dict(rows=rows))
    print(NL.join(L[:14] + L[-3:]))


# ================================================================================ COMPONENT 2: THE READER, IMPORTED UNCHANGED ((R304)(3))
def _reader():
    """tools/circuit_read.py imported and unedited (N5: the carry-time repair the one edit to a shared tool): its kernel table extended at runtime
    by SIDE-lv-conservation's library, its two writers pointed at this act's names (its `read` names its banks b692_..., so a run as it stands
    would overwrite b692's root-named banks -- b693's readfirst lesson, data/b693_tool_repairs.txt row (1))."""
    import circuit_read as CR
    CR.LIBS.setdefault('SIDE-lv-conservation', (('SIDELvConservation', ''),))
    put0, out0 = CR.put, CR.output

    def put_(name, lines):
        if not name.startswith('b692_'):
            sys.exit('### THE READER ASKED TO WRITE %s -- NOTHING WRITTEN' % name)
        lines = list(lines)
        if lines and lines[0].startswith('b692 -- '):
            lines[0] = '%s -- %s [the reader imported unchanged by tools/b694_record.py, its banks named for %s]' % (ACT, lines[0][8:], ACT)
        put0(ACT + name[4:], lines)

    CR.put = put_
    CR.output = lambda stem, *r: out0(ACT + stem[4:], *r)
    return CR


def circuit(*a):
    """`circuit <bank> <kernel> <tag> <tip> <main>`: the reader's `read` (SERIES, TERMINALS, SHORTS, WIDTH, LOAD, OUTPUT) over a closure bank,
    its banks data/b694_circuit_<kernel>_<tag>.txt (.dot, .png, _png_hashes.txt)."""
    CR = _reader()
    CR.read(*a[:5])


def prints(*a):
    """the print list at main before and after, line for line: before -- run 38305820585 at c230e6d, whose tree 59109b72 is main 8e3bc76's, its
    eight terminals' profiles (relay data/b657_runner_SIDE-lv-conservation.txt :118-:125); after -- this act's run, data/b694_axioms_SIDE-lv-
    conservation_after.txt; the list itself, the workflow's #print axioms lines at 8e3bc76 and at d38f3e8. data/b694_prints_SIDE-lv-conservation.txt."""
    kernel = 'SIDE-lv-conservation'
    bl_ = rdn('b657_runner_SIDE-lv-conservation.txt').split(NL)
    before = []
    for l in bl_[117:125]:
        m = re.match(r"^  (\S+)\s+(\[[^\]]*\])", l)
        if m:
            before.append((m.group(1), sorted(x.strip(" '") for x in m.group(2).strip('[]').split(','))))
    after = dict((n, sorted(d)) for n, d in _deps(rdn('%s_axioms_%s_after.txt' % (ACT, kernel))))
    l0, l1 = _wf_list(kernel, '8e3bc76')[0], _wf_list(kernel, 'd38f3e8')[0]
    rows = [(n, b, after.get(n)) for n, b in before]
    eq = len(before) == 8 and all(b == f for _n, b, f in rows) and l0 == l1
    L = ['%s -- THE PRINTS OF %s AT MAIN BEFORE AND AFTER THE CLOSURE STEP, LINE FOR LINE (%s)' % (ACT, kernel, utc()), '',
         '### before: run 38305820585 at c230e6d (tree 59109b72a76b, main 8e3bc76`s tree; relay data/b657_runner_SIDE-lv-conservation.txt :118-:125) ;',
         '### after: run 39465780735 at d38f3e8 (relay data/b694_axioms_SIDE-lv-conservation_after.txt) ; the list (the workflow`s #print axioms lines) at',
         '### 8e3bc76 %d names, at d38f3e8 %d names, equal %s. Rows are terminals: name | before | after | equal.' % (len(l0), len(l1), l0 == l1), '']
    L += ['  %-62s | %s | %s | %s' % (n, b, f, 'EQUAL' if b == f else '### DIFFER') for n, b, f in rows]
    L += ['', '### ### **BEFORE %d TERMINALS ; EACH PRINTED AFTER %s ; THE LIST EQUAL %s ; EQUAL LINE FOR LINE %s.**' % (
        len(before), all(f is not None for _n, _b, f in rows), l0 == l1, eq)]
    put_txt('%s_prints_%s.txt' % (ACT, kernel), L)
    print(NL.join(L[6:]))


def readings(*a):
    """(R304)(3): the readings the author asked for after b692, printed again from the banks -- CLAUSE-DOMINANCE, WIDTH's pairs by name, LOAD's
    three highest -- for each faces kernel, each line cited by bank and line. data/b694_circuit_readings.txt."""
    def lines_of(name):
        return rdn(name).split(NL)

    def cite(name, pred):
        return [(i, l) for i, l in enumerate(lines_of(name), 1) if pred(l)]

    ef, lv = 'b692_circuit_SIDE-explicit-formula_v0.34.1.txt', 'b694_circuit_SIDE-lv-conservation_v0.13.0.txt'
    L = ['%s -- THE THREE READINGS PRINTED AGAIN FROM THE BANKS, (R304)(3) (%s)' % (ACT, utc()), '',
         '### rows are readings per faces kernel, each line read from its bank and cited by line; nothing recomputed here.', '']
    dm = cite('%s_circuit_dominance.txt' % ACT, lambda l: l.startswith('### ### **CLAUSE-DOMINANCE'))
    L += ['## CLAUSE-DOMINANCE   relay data/%s_circuit_dominance.txt :%d | %s' % (ACT, dm[0][0], dm[0][1].strip('# *'))]
    npairs = {}
    for kname, bank in (('SIDE-explicit-formula', ef), ('SIDE-lv-conservation', lv)):
        wl = lines_of(bank)
        h = [i for i, l in enumerate(wl) if l.startswith('## WIDTH -- theorem pairs')]
        pairs = []
        if h:
            for l in wl[h[0] + 2:]:
                if not l.strip():
                    break
                pairs.append(l.strip())
        ld = cite(bank, lambda l: l.startswith('### ### **RECORDS'))
        load3 = re.search(r'LOAD`S THREE HIGHEST (.+?)\.\*\*\s*$', ld[0][1]).group(1) if ld else '### NOT READ'
        L += ['', '## %s (relay data/%s)' % (kname, bank),
              '   WIDTH`s pairs at or under FEW = 5, by name (:%d-:%d), rows are pairs: meet | the one | the other:' % (h[0] + 3, h[0] + 2 + len(pairs))]
        npairs[kname] = len(pairs)
        L += ['     ' + p for p in pairs] or ['     NONE']
        L += ['   LOAD`s three highest (:%d): %s' % (ld[0][0], load3)]
    tm = cite(lv, lambda l: l.startswith('   PREMISE  liCriterion'))
    L += ['', '### the clause`s one meeting with SIDE-lv-conservation: no record of its compiled face in that kernel`s closure bank (the lakefile`s',
          '### federation line: no Lake dependency on a sister kernel), and among its main theorem`s TERMINALS the premise %s (relay data/%s :%d),' % (
              tm[0][1].split(':', 1)[0].replace('PREMISE', '').strip() if tm else '### NOT READ', lv, tm[0][0] if tm else 0),
          '### the open end the faces page`s correspondence row discharges on SIDE-explicit-formula`s side (relay data/b690_nodes_zeta.txt :126).']
    L += ['', '### ### **%s ; WIDTH AT FEW = 5: SIDE-explicit-formula %d PAIRS, SIDE-lv-conservation %d ; LOAD READ FOR BOTH.**' % (
        re.search(r'CLAUSE-DOMINANCE \d+ OF \d+', dm[0][1]).group(0), npairs['SIDE-explicit-formula'], npairs['SIDE-lv-conservation'])]
    put_txt('%s_circuit_readings.txt' % ACT, L)
    print(NL.join(L))


FACE = 'SIDEExplicitFormula.B321.h2_sign'
KERNEL_MAINS = (('SIDE-explicit-formula', 'b692_circuit_SIDE-explicit-formula_v0.34.1_4313875.jsonl.gz', 'SIDEExplicitFormula.B321.h2_sign_iff_rh',
                 'data/b690_nodes_zeta.txt :97 (the face h2_sign_iff_rh, a kernel row of :94-:164); b692`s closure bank'),
                ('SIDE-lv-conservation', None, 'residue_irreducible', 'data/b690_nodes_zeta.txt :126 (@corr SIDE-lv-conservation | residue_irreducible); '
                 'this act`s closure bank'))


def dominance(*a):
    """`dominance <lv bank>`: CLAUSE-DOMINANCE read whole over the faces kernels (data/b690_nodes_zeta.txt :94-:164, :126; the author`s answer
    at prompt 2): rows are faces kernels with the clause's compiled face named, the closure's reading HOLDS / ABSENT, the declaration through
    which it enters; the fraction printed. data/b694_circuit_dominance.txt."""
    CR = _reader()
    rows = []
    for kernel, bank, main, why in KERNEL_MAINS:
        bank = bank or a[0]
        recs, head = CR.load(bank)
        mains = [n for n in recs if n == main or n.endswith('.' + main)]
        if len(mains) != 1:
            sys.exit('### %s: THE MAIN THEOREM %s MATCHES %d RECORDS -- NOTHING WRITTEN' % (kernel, main, len(mains)))
        m = mains[0]
        cl = set(recs[m]['c'])
        holds = FACE in cl or FACE == m
        enters = ''
        if holds:
            direct = [x for x in recs[m]['c'] if x in recs and (x == FACE or FACE in recs[x]['c'])]
            enters = sorted(direct, key=lambda x: (x != FACE, len(recs[x]['c'])))[0] if direct else FACE
        face_rec = FACE in recs
        rows.append(dict(kernel=kernel, main=m, bank=bank, records=len(recs), holds=holds, enters=enters, face_a_record=face_rec,
                         closure=len(cl), why=why, modules=len(head.get('modules') or [])))
    n = sum(1 for r in rows if r['holds'])
    L = ['%s -- CLAUSE-DOMINANCE READ WHOLE, (R304)(3) AND THE AUTHOR`S ANSWER AT PROMPT 2 (%s)' % (ACT, utc()), '',
         '### the faces kernels: the kernels the faces page`s generator input names (relay data/b690_nodes_zeta.txt :94-:164, SIDE-explicit-formula`s',
         '### kernel rows; :126, SIDE-lv-conservation by its correspondence row); the clause`s compiled face %s (:95). Rows are faces kernels:' % FACE,
         '### the kernel | the face named | the main theorem | the closure`s reading HOLDS or ABSENT | the declaration through which it enters | the bank.', '']
    for r in rows:
        L.append('  %-24s | face %s | main %s | %s | %s | relay data/%s (records %d, programme modules %d, the main`s closure %d names ; the face a record '
                 'of the bank %s) | %s' % (r['kernel'], FACE, r['main'], 'HOLDS' if r['holds'] else 'ABSENT',
                                           ('enters through ' + r['enters']) if r['holds'] else 'enters through none',
                                           r['bank'], r['records'], r['modules'], r['closure'], r['face_a_record'], r['why']))
    L += ['', '### b692`s fraction re-read: %s (relay data/b692_circuit_dominance.txt :21).' % CR.rd(os.path.join(D, 'b692_circuit_dominance.txt')).strip().split(NL)[-1].strip('# *'),
          '', '### ### **CLAUSE-DOMINANCE %d OF %d FACES KERNELS (%s).**' % (n, len(rows), ' ; '.join('%s %s' % (r['kernel'], 'HOLDS' if r['holds'] else 'ABSENT')
                                                                                  for r in rows))]
    put_txt('%s_circuit_dominance.txt' % ACT, L)
    put_json('%s_circuit_dominance.json' % ACT, dict(at=utc(), rows=rows))
    print(NL.join(L[6:]))


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


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, repairs=repairs, c1=c1, dispatch=dispatch, runstatus=runstatus, runner=runner,
              circuit=circuit, dominance=dominance, prints=prints, readings=readings)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b694_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
