# -*- coding: utf-8 -*-
"""b698_record.py -- THE ACT'S RECORD TOOL, b698 under (R308).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b698's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b697_record.py in stages: the helpers, the guarded landing, the readers, step zero's rowgen and branches
### routes, the answers and defects routes first (stage one); Component 1's weight line and the plan's row; the dominance, uses and residue
### routes at Components 2-4; the late routes at Component 5. Every python child is started as `python -X utf8`, no environment mapping passed.
### Routes: `python tools/b698_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
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
import b698_worklist as K          # noqa: E402

SP = K.SP
STANDIN = 'standin' in sys.argv[2:]          # ### the dry-run step's stand-ins, by argument (environment variables left as they are)
RELAY = ROOT
ACT, PREV = 'b698', 'b697'


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


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank (b697's, carried)."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b698_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b698_findings.json': dict(entry_line=99999, title='stand-in'),
        'b698_trail.json': dict(line=99999),
        'b698_act_root.json': dict(root='0' * 64, previous='afc141e1' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


def _vl(name):
    return ([x for x in rdn(name).split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b698's)
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


# ================================================================================ THE READERS, ONE PER ROW SHAPE A ROUTE READS ((R263)(3))
BRANCH_FATES = ('DELETED', 'KEPT', 'RAISED')


def read_branch_row(r):
    """a row of data/b698_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
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
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b698_rowgen_<stage>.txt."""
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


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R308)(7); b697's form)
def _remote_heads(repo):
    out = {}
    for l in g(repo, 'ls-remote', '--heads', 'origin').split(NL):
        x = l.split()
        if len(x) == 2 and x[1].startswith('refs/heads/'):
            out[x[1][len('refs/heads/'):]] = x[0]
    return out


def branches(*a):
    """`branches before`: data/b698_branches_before.json -- every branch (R308)(7) names, its tip resolved to 40 hex, merged into main by
    ancestry, and the remote's heads read once per repository; written before any delete. `branches`: data/b698_branches.txt (.json) -- each
    branch's fate read now against the tips banked before."""
    if a and a[0] == 'before':
        rows, remotes = [], {}
        for repo, bs in K.DELETE:
            remotes[repo] = _remote_heads(repo)
            for b in bs:
                tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/%s^{commit}' % b).strip()
                merged = bool(tip) and grc(repo, 'merge-base', '--is-ancestor', tip, 'main') == 0
                rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, at_remote=remotes[repo].get(b)))
        for repo, b in K.DELETE_REMOTE:
            tip = remotes.get(repo, {}).get(b, '')
            merged = bool(tip) and grc(repo, 'merge-base', '--is-ancestor', tip, 'main') == 0
            rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=merged, at_remote=tip))
        put_json('%s_branches_before.json' % ACT, dict(at=utc(), rows=rows, remotes=remotes))
        for r in rows:
            print('  %-18s %-28s %-6s %s merged %s at the remote %s' % (os.path.basename(r['repo']), r['branch'], r['where'], (r['tip'] or '### NONE')[:12],
                                                                       r['merged'], (r['at_remote'] or 'no')[:12]))
        return
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b698_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in _remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R308)(7): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b698_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after.']
    L += ['  %-18s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[]))
    print(NL.join(L[4:]))


# ================================================================================ THE ANSWERS BANK (b697's route, carried)
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
    """data/b698_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
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


# ================================================================================ THE DEFECTS BANK (b697's route and its row reader, carried)
DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short(act=ACT):
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
    t = rdn('%s_defects.txt' % ACT)
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('%s_defects.json' % ACT, dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R308)(1)
WH = ('*Appended 2026-10-21 by b698 to b697’s entry (:9654), under `(R308)`(1) -- b697 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b697_closing.txt):*')
WB = (' “b697 closed: relay 5d4932b5, PLACE-papers f5a4a6e; suite 120 of 120; root afc141e1f2179e86…; 1 prompt answered; 3 defects” '
      '(data/b697_closing.txt :1), the closing dcce6eed pushed and read back at relay main (data/b697_closing_push_out.txt :5). The Weil-face '
      'line at Q0 regenerated on the author’s word, its head’s date read as the act’s opening UTC date, the convention the earlier rows and the '
      'mirror names follow (data/b697_faces_date.txt :23); b695’s list re-emitting the committed page byte for byte before any write, the new '
      'list replacing :168 alone, the page differing at :3 and :734 alone (data/b697_faces_diff.txt :20), the row carrying ± 3.68e-23 and the '
      'caveat in (R307)(2)’s words. SIDE-simplicity re-cut, tied with SIDE-substrate-cluster at the top count and named by b674’s rule at its '
      'OVERREACHES step, 1 against 0 (data/b697_tie.txt :44); the module header’s comment lines alone cut, the ACTION verbatim; the runs '
      '39530030132 and 39530116146 on the hosted runner with the five terminals printing equal line for line (data/b697_cut.txt :9); merged at '
      '53df27f and tagged v0.1.1 naming v0.1.0; the distance 1 to 0 (:13, :21). The quotation search found one quoting line, SIDE-simplicity '
      'README.md :9 restating the old claim (“Section I.2 … and Section III … are already proved in SIDE-kernel”), outside the table’s rows, '
      'carried as a residue and named (:17); one Correspondence cell made stale by the tag, SIMPLICITY_OF_RIEMANN_ZEROS :441 with the kernel '
      'token v0.1.0, held because the order regenerated cells for a paper’s cut alone (:19; data/b697_correspondence_dry.txt :32). The third '
      'face priced and not run: by li_identity_sym the arithmetic limit at n is λ_n read from the prime side, blPoly a Laguerre polynomial so '
      'the prime sum must reach m ≈ e^(4n); Route A at 3 foreground parts for n ≤ 2 and not priceable at the siblings’ n ≈ 10^4; Route B '
      '(Lagarias’s Lemma 4.2), the seat’s addition, priceable at n in the tens alone (data/b697_arith_plan.txt :40-:48, :112). The suite 120 of '
      '120 before and after the push, every control behaving (data/b697_checks.txt, data/b697_checks_postpush.txt); all eight scores HELD '
      '(data/b697_scores_close.json); the sealed tools 8 of 8 (data/b697_closing.txt :14); the root afc141e1 over 69 banks; no lean on the '
      'host; mirror-refresh-2026-10-21-b697.zip CLEAN with the root line. Three defects, all the seat’s -- (a) the carried faces route '
      'miscounting its diff, caught in the dry run and repaired before the page write, (b) 18 of 60 Read calls reading a file whole '
      '(data/b697_read_calls.txt :23), (c) long turns between reads and bank writes -- and one event beneath, an act arm stricter than the '
      'ferry failing the pre-run on real state and corrected before the seal (data/b697_defects.txt :6-:19, :26-:28). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B697_ENTRY,
         check=[('FINDINGS.md', K.B697_ENTRY, '## SIDE-simplicity re-cut: 1 row outside LICENSED/CITED to 0, v0.1.1'),
                ('OPEN_TRAILS.md', K.B697_TRAIL, '### b697')], dry=dry)


# ================================================================================ COMPONENT 2: W-ORD-H2-BRIDGE READ AGAINST THE RESULT, (R308)(3)
BH = ('*Appended 2026-10-21 by b698 beneath `W-ORD-H2-BRIDGE` (:10257, annotated at :15200), under `(R308)`(3) -- CORRESPONDENCE-DOMINANCE '
      'READ, DIFFERS; THE BINDER NAMED IS THE BRIDGE’S OPEN OBJECT:*')


def _bridge_text():
    j = jl('%s_correspondence_dominance.json' % ACT)
    v = j.get('verdict') or ''
    if not v.startswith('DIFFERS at binder 1') or not (j.get('controls') or {}).get('c1') or not (j.get('controls') or {}).get('c2'):
        sys.exit('### THE DOMINANCE BANK DOES NOT READ DIFFERS AT BINDER 1 WITH BOTH CONTROLS -- NOTHING WRITTEN (%r)' % v[:80])
    return (' the reader relay tools/circuit_correspondence.py, run at b698 on the author’s two answers to the citation misses '
            '(data/b698_author_answers.txt), compared h2_sign’s statement -- its print at SIDE-explicit-formula v0.26 (data/b643_probe_out_zeta.txt '
            ':43-:52), every file defining a name it carries byte-identical to v0.34 -- with SIDE-lv-conservation’s compiled face residue_irreducible '
            'as its source writes it at v0.13.0 (ZeroActingPartial.lean :111-:121; no hosted run at that tag can print it), the two kernels’ '
            'namespaces stripped and the binders aligned by position. Its controls first: h2_sign against itself reading HOLDS at every binder, a '
            'planted statement with binder 1’s type changed reading DIFFERS there alone. The reading, source against print: DIFFERS at binder 1 -- '
            'h2_sign’s explicit (k : ℝ → ℂ), a test window ranging over classK, against residue_irreducible’s implicit {lam_A : ℕ → ℝ}, a '
            'sequence; 2 binders against 13, and the conclusions differing, 0 of 14 rows agreeing (data/b698_correspondence_dominance.txt). '
            'CLAUSE-DOMINANCE reads 1 of 2 by closure and DIFFERS at binder 1 by correspondence. The bridge’s open object, as the reading names '
            'it: a statement joining the clause’s quantifier over test windows k in classK to the sequence quantifiers the face carries -- the '
            'row’s own reach runs through the face’s last binder, liCriterion : Register4_positivity lam → RiemannHypothesis, discharged at '
            'λ := LiCoeff by register4_positivity_liCoeff_imp_rh (data/b690_nodes_zeta.txt :126), a Li-coefficient form and not h2_sign’s. '
            'Status OPEN.')


def bridge(*a):
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', BH, NL + BH + _bridge_text() + NL)], '%s_bridge_line.json' % ACT, 'bridge', entry=10257,
         check=[('OPEN_TRAILS.md', 10257, '(2) **`W-ORD-H2-BRIDGE`**'), ('OPEN_TRAILS.md', 15200, 'beneath `W-ORD-H2-BRIDGE` (:10257)')], dry=dry)


# ================================================================================ COMPONENT 3: THE REGULARITY-USES BANK READ BACK, (R308)(4)
USE_ROW = re.compile(r'^  ([UP]\d+) +(\S+\.lean) :(\d+) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \| (DISCHARGED|RE-PROVED \(s\d\)|OBSTRUCTED \(o\d\)) \| '
                     r'(DISCHARGED|RE-PROVED \(s\d\)|OBSTRUCTED \(o\d\)) \| (DISCHARGED|RE-PROVED \(s\d\)|OBSTRUCTED \(o\d\))$')
VERDICTS = ('DISCHARGED', 'RE-PROVED', 'OBSTRUCTED')


def read_use_row(l):
    """a row of data/b698_regularity_uses.txt: id | file :line | the line | the declaration | the hypothesis | the step | W1 | W2 | W3; returns
    (id, path, line, text, (W1, W2, W3)) with each verdict's word."""
    m = USE_ROW.match(l)
    if not m:
        raise ValueError('use row of another shape: %r' % l[:100])
    return m.group(1), m.group(2), int(m.group(3)), m.group(4), tuple(m.group(k).split(' (')[0] for k in (8, 9, 10))


READERS.append('read_use_row')


def uses(*a):
    """data/b698_regularity_counts.txt: every row of the uses bank read by read_use_row; its quoted line compared with the file's line at v0.34
    (git show, whitespace collapsed); the count per column for the U-rows and the P-rows; and the completeness read -- every code line of
    SIDEExplicitFormula/ at v0.34 naming classK or destructuring a classK hypothesis cited by the bank (file :line), comment lines apart."""
    t = rdn('%s_regularity_uses.txt' % ACT)
    rows = [read_use_row(l) for l in t.split(NL) if re.match(r'^  [UP]\d+ ', l)]
    src = {}
    bad = []
    for rid, f, ln, text, _v in rows:
        path = (f if f.startswith('Zeta23/') else 'SIDEExplicitFormula/' + f)
        if path not in src:
            src[path] = (_show(K.EF_DIR, K.EF_TAG, path) or '').split(NL)
        L = src[path]
        have = ' '.join(L[ln - 1].split()) if 0 < ln <= len(L) else ''
        if ' '.join(text.split()) != have:
            bad.append((rid, f, ln, have[:90]))
    out = ['%s -- COMPONENT 3, (R308)(4): THE REGULARITY-USES BANK READ BACK BY ITS ROW READER (%s)' % (ACT, utc()), '',
           '### the bank: relay data/%s_regularity_uses.txt ; each row`s quoted line compared with its file`s line at SIDE-explicit-formula %s '
           '(git show), whitespace collapsed ; rows are counts.' % (ACT, K.EF_TAG), '']
    for kind, nm in (('U', 'THE USES (SIDEExplicitFormula/)'), ('P', 'THE PATH (the two explicit formulas` leaves)')):
        rs = [r for r in rows if r[0].startswith(kind)]
        out.append('  %s: rows %d' % (nm, len(rs)))
        for j, col in enumerate(('W1 C¹ with absolutely integrable second derivative', 'W2 even C² of rapid decay without compact support',
                                 'W3 finite sums of autocorrelations')):
            c = dict((v, sum(1 for r in rs if r[4][j] == v)) for v in VERDICTS)
            out.append('    %-52s DISCHARGED %2d ; RE-PROVED %2d ; OBSTRUCTED %2d ; sum %d (= rows %s)' % (
                col, c['DISCHARGED'], c['RE-PROVED'], c['OBSTRUCTED'], sum(c.values()), sum(c.values()) == len(rs)))
    rc_ = subprocess.run(['git', '-C', K.EF_DIR, 'grep', '-n', '-E', r'classK|⟩ := hk$|hk\.2\.2\.1|classK at hk', K.EF_TAG, '--',
                          'SIDEExplicitFormula/*.lean'], capture_output=True)
    code, prose = [], 0
    for l in rc_.stdout.decode('utf-8', 'replace').replace(chr(13), '').split(NL):
        m = re.match(r'^[^:]+:SIDEExplicitFormula/(.+?):(\d+):(.*)$', l)
        if not m:
            continue
        body = m.group(3).strip()
        if body.startswith(('/-', '--', '*', '`')) or not re.search(r'classK|hk', body.split('--')[0]) or _is_comment(m.group(1), int(m.group(2))):
            prose += 1
            continue
        code.append((m.group(1), int(m.group(2))))
    cited = set()
    for f, a_, b_ in re.findall(r'(\S+\.lean) :(\d+)(?:-:(\d+))?', t):
        for n in range(int(a_), int(b_ or a_) + 1):
            cited.add((f, n))
    for l in t.split(NL):
        if re.match(r'^  [UP]\d+ ', l):
            f0 = l.split()[1]
            for n in re.findall(r'(?<![\w.]) ?:(\d+)\b', l.split('|', 1)[1]):
                cited.add((f0, int(n)))
    for blk in re.findall(r'(?m)^  (?:PRODUCERS|STATEMENTS|THE MEMBERSHIP CONSUMED WHOLE|A NAMESAKE)[^\n]*', t):
        cur = None
        for tok in re.findall(r'(\S+\.lean) :(\d+)(?:-:(\d+))?|, :(\d+)(?:-:(\d+))?| and :(\d+)', blk):
            if tok[0]:
                cur = tok[0]
                rng = (int(tok[1]), int(tok[2] or tok[1]))
            else:
                n0 = tok[3] or tok[5]
                rng = (int(n0), int(tok[4] or n0))
            for n in range(rng[0], rng[1] + 1):
                cited.add((cur, n))
    unl = [c for c in code if c not in cited]
    out += ['', '  QUOTED LINES EQUAL TO THE FILE AT %s: %d of %d%s' % (K.EF_TAG, len(rows) - len(bad), len(rows), (' -- differing ' + '; '.join(
        '%s %s :%d (%s)' % x for x in bad)) if bad else ''),
            '  THE COMPLETENESS READ: code lines of SIDEExplicitFormula/ naming classK or destructuring a classK hypothesis %d ; cited by the bank %d ; '
            'unlisted %s ; comment and docstring lines %d' % (len(code), len(code) - len(unl), ['%s :%d' % u for u in unl] or 'NONE', prose)]
    us = [r for r in rows if r[0].startswith('U')]
    ob = [j for j in range(3) if any(r[4][j] == 'OBSTRUCTED' for r in us)]
    out += ['', '### ### **USES %d (SIDEExplicitFormula/) AND PATH LEAVES %d ; W1 %s ; W2 %s ; W3 %s ; QUOTES EQUAL %d OF %d ; UNLISTED %d ; NO LEAN WRITTEN.**' % (
        len(us), len(rows) - len(us), *['%d/%d/%d' % tuple(sum(1 for r in us if r[4][j] == v) for v in VERDICTS) for j in range(3)],
        len(rows) - len(bad), len(rows), len(unl))]
    if 'dry' not in a:
        put_txt('%s_regularity_counts.txt' % ACT, out)
    print(NL.join(out))
    return ob


def _is_comment(f, n):
    """the line n of SIDEExplicitFormula/<f> at the tag lies inside a /- ... -/ block."""
    L = (_show(K.EF_DIR, K.EF_TAG, 'SIDEExplicitFormula/' + f) or '').split(NL)
    depth = 0
    for i, l in enumerate(L[:n], 1):
        if i == n:
            return depth > 0 or l.strip().startswith(('/-', '--'))
        depth += l.count('/-') - l.count('-/')
    return False


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, c1=c1, bridge=bridge, uses=uses)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b698_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
