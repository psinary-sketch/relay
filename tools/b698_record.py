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


# ================================================================================ COMPONENT 4: THE STALE CELL, (R308)(5)
ROSTER_ALL = 'b672_roster_read.json'
ROSTER_ONE = 'b698_roster_simplicity.json'


def _gen(mode, roster, *extra):
    r = subprocess.run([sys.executable, '-X', 'utf8', '-B', os.path.join(T, 'correspondence_gen.py'), mode, os.path.join(D, roster)] + list(extra),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=ROOT, timeout=580)
    return r.returncode, ((r.stdout or '') + (r.stderr or '')).replace(chr(13), '')


def cells(*a):
    """`cells dry`: data/b698_roster_simplicity.json -- b672's roster with its SIMPLICITY_OF_RIEMANN_ZEROS table alone, every key carried -- and
    data/b698_correspondence_dry.txt -- the generator run dry (full) on that roster and on b672's whole roster, nothing written by it.
    `cells run` (on the author's word "run"): the generator run on the one-table roster, its diff banks under b698_correspondence_run; the
    page's git diff banked in data/b698_correspondence_page_diff.txt."""
    if a and a[0] == 'run':
        before = g(PP, 'rev-parse', 'HEAD').strip()
        if g(PP, 'status', '--porcelain', '--untracked-files=no').strip():
            sys.exit('### PLACE-papers HAS TRACKED CHANGES -- NOTHING RUN')
        rc, out = _gen('run', ROSTER_ONE, '--diff', '%s_correspondence_run' % ACT)
        changed = [l for l in g(PP, 'diff', '--name-only').split(NL) if l.strip()]
        diff = g(PP, 'diff', '-U0', '--', K.STALE_PAGE and 'phase1.5/simplicity/' + K.STALE_PAGE)
        L = ['%s -- COMPONENT 4, (R308)(5): THE STALE CELL REGENERATED BY THE GENERATOR ALONE, ON THE AUTHOR`S WORD "run" (%s)' % (ACT, utc()), '',
             '### the run: `python -X utf8 -B tools/correspondence_gen.py run data/%s --diff %s_correspondence_run` (exit %d), PLACE-papers at %s ; '
             'files changed by it: %s' % (ROSTER_ONE, ACT, rc, before[:7], changed or 'NONE'), '', '### the page`s diff (git diff -U0), verbatim:']
        L += ['    ' + l for l in diff.rstrip(NL).split(NL)]
        L += ['', '### the generator`s own verdict line: ' + ([l for l in out.split(NL) if l.startswith('### ### **TABLES')] or ['### NOT READ'])[-1]]
        ok = changed == ['phase1.5/simplicity/' + K.STALE_PAGE] and diff.count('\n-|') == 1 and diff.count('\n+|') == 1
        L += ['', '### ### **THE STALE CELL %s :%d REGENERATED: FILES CHANGED %d ; CELL LINES CHANGED %d ; THE PAGE ALONE %s.**' % (
            K.STALE_PAGE.replace('.md', ''), K.STALE_LINE, len(changed), diff.count('\n-|'), ok)]
        put_txt('%s_correspondence_page_diff.txt' % ACT, L)
        print(NL.join(L))
        return
    roster = jl(ROSTER_ALL)
    one = [t for t in roster['tables'] if t['doc'] == 'SIMPLICITY_OF_RIEMANN_ZEROS']
    if len(one) != 1:
        sys.exit('### THE ROSTER DOES NOT CARRY ONE SIMPLICITY TABLE -- NOTHING WRITTEN')
    sub = dict((k, v) for k, v in roster.items() if k != 'tables')
    sub['tables'] = one
    sub['b698'] = 'b672`s roster (relay data/b672_roster_read.json) with its SIMPLICITY_OF_RIEMANN_ZEROS table alone, every key carried, under (R308)(5)'
    put_json(ROSTER_ONE, sub)
    rc1, o1 = _gen('dry', ROSTER_ONE, 'full')
    rc2, o2 = _gen('dry', ROSTER_ALL, 'full')
    pick = lambda o, h: list(dict.fromkeys(l for l in o.split(NL) if l.startswith(h) and ' | ' not in l))   # noqa: E731
    diff1 = [l for l in o1.split(NL) if re.match(r'^    \S+ :\d+ \| ', l)]
    diff2 = [l for l in o2.split(NL) if re.match(r'^    \S+ :\d+ \| ', l)]
    pair1 = [l for l in o1.split(NL) if 'SIMPLICITY_OF_RIEMANN_ZEROS' in l and ';' in l and 'partner' not in l.lower() and l.startswith('    SIMPLICITY')]
    L = ['%s -- COMPONENT 4, (R308)(5): THE CORRESPONDENCE GENERATOR RUN DRY OVER THE CELLS NAMING SIDE-simplicity (%s)' % (ACT, utc()), '',
         '### the runs, nothing written by either: `python -X utf8 -B tools/correspondence_gen.py dry data/%s full` (exit %d) -- the one-table '
         'roster, b672`s SIMPLICITY_OF_RIEMANN_ZEROS entry alone (data/%s, every key carried) -- and the same on b672`s whole roster '
         'data/%s (exit %d), the local clones` tags read, no remote call.' % (ROSTER_ONE, rc1, ROSTER_ONE, ROSTER_ALL, rc2), '',
         '### THE DIFF ON THE ONE-TABLE ROSTER (rows are cells changed; document :line ; column ; kernel ; old ; new), verbatim:']
    L += diff1 or ['    NONE']
    L += ['### its one-copy pair line, verbatim:'] + (pick(o1, '    SIMPLICITY_OF_RIEMANN_ZEROS ') or ['    none']) + [
          '### its verdict line, verbatim:'] + pick(o1, '### ### **TABLES')
    L += ['', '### THE DIFF ON THE WHOLE ROSTER, verbatim (the cells beyond SIDE-simplicity`s are SIDE-archimedean`s, held since b693 and not raised '
              'by (R308)(5)):']
    L += diff2 or ['    NONE']
    L += ['### its verdict line, verbatim:'] + pick(o2, '### ### **TABLES')
    simp = [l for l in diff1 if 'SIDE-simplicity' in l]
    L += ['', '### ### **CELLS NAMING SIDE-simplicity THE GENERATOR WOULD CHANGE %d (%s) ; ON THE ONE-TABLE ROSTER CELLS CHANGED %d ; ON THE WHOLE '
              'ROSTER %d ; NOTHING WRITTEN.**' % (len(simp), '; '.join(l.strip() for l in simp) or 'NONE', len(diff1), len(diff2))]
    put_txt('%s_correspondence_dry%s.txt' % (ACT, '_after' if 'after' in a else ''), L)
    print(NL.join(L))


# ================================================================================ COMPONENT 4: THE README RE-CUT ON THE AUTHOR'S WORD (b697's routes, carried)
STD3 = ('Classical.choice', 'Quot.sound', 'propext')


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def dispatch(*a):
    """`dispatch <kernel> <ref sha> <label> <target> [dry]`: ONE dispatch of build-module.yml at main with the ref input and the lake target;
    refused where data/b698_dispatches.json already carries the ref's tree (one dispatch per tree state). The run id read from the run list
    (the newest workflow_dispatch run created after the dispatch); a row banked."""
    kernel, ref, label, target = a[0], a[1], a[2], a[3]
    repo = 'psinary-sketch/' + kernel
    full = g('D:/' + kernel, 'rev-parse', ref).strip()
    tree = g('D:/' + kernel, 'rev-parse', full + '^{tree}').strip()
    j = jl('%s_dispatches.json' % ACT) if os.path.isfile(os.path.join(D, '%s_dispatches.json' % ACT)) else {}
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
    """`runstatus <kernel> <run id>`: the run's status and conclusion, read once (a foreground read, no wait)."""
    rc, out, err = _gh('run', 'view', a[1], '-R', 'psinary-sketch/' + a[0], '--json', 'status,conclusion,updatedAt,headSha')
    print('  %s' % (out.decode('utf-8', 'replace').strip() or err.strip()))


def _deps(ax):
    """the axioms output read per terminal: [(name, [axioms] or None for 'does not depend on any axioms')], wrapped lists rejoined."""
    out = []
    for n, d in re.findall(r"^'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)",
                           re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', ax), re.M):
        out.append((n, [x.strip() for x in d.split('[', 1)[1].rstrip(']').split(',') if x.strip()] if d.startswith('depends') else []))
    return out


def read_runner_row(r):
    """a row of data/b698_runner_rows.json: the kernel, its label, the ref (40 hex), the run id and the gate; returns (kernel, label, gate)."""
    if not isinstance(r, dict) or not re.match(r'^SIDE-[\w-]+$', r.get('kernel') or '') or not re.match(r'^[\w-]+$', r.get('label') or '') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['kernel'], r['label'], r['gate']


READERS.append('read_runner_row')


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <note...>`: the kernel's run read by its id; the artifact listed, downloaded by its id into
    memory, its sha256 against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP;
    the axioms output of the print step banked whole, every name of the list matched to one printed line, each terminal's axioms read against
    the standard three. data/b698_runner_<kernel>_<label>.txt, data/b698_axioms_<kernel>_<label>.txt and a row of data/b698_runner_rows.json."""
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
    L = ['b698 -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (kernel, label.upper(), utc()), '',
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
    put_txt('%s_runner_%s_%s.txt' % (ACT, kernel, label), L)
    if row['artifact_sha256']:
        put_txt('%s_axioms_%s_%s.txt' % (ACT, kernel, label), ax.split(NL) if ax else ['### EMPTY'])
        put_txt('%s_buildlog_%s_%s.txt' % (ACT, kernel, label), blog.rstrip(NL).split(NL))
    j = jl('%s_runner_rows.json' % ACT) if os.path.isfile(os.path.join(D, '%s_runner_rows.json' % ACT)) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('%s_runner_rows.json' % ACT, dict(rows=rows))
    print(NL.join(L[:14] + L[-3:]))


def prints(*a):
    """`prints <kernel> <before bank> <after bank>`: the 'before' terminals' printed lines compared with the same names' lines in the 'after'
    bank, line for line by name; the raw axioms banks compared byte for byte beside. data/b698_prints_<kernel>.txt."""
    kernel, bb, ab = a[0], a[1], a[2]
    b, f = rdn(bb), rdn(ab)
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bd, fd = dict(_deps(b)), dict(_deps(f))
    diff = [(n, bd[n], fd.get(n)) for n in bd if fd.get(n) != bd[n]]
    new = [n for n in fd if n not in bd]
    L = ['b698 -- THE PRINTS OF %s BEFORE AND AFTER THE README RE-CUT, BY NAME AND LINE FOR LINE (%s)' % (kernel, utc()), '',
         '### before: relay data/%s (%d terminals) ; after: relay data/%s (%d terminals) ; the two banks equal line for line: %s ; rows are the '
         'terminals that differ:' % (bb, len(bd), ab, len(fd), b == f)] + (['    %s : %s | %s' % d for d in diff] or ['    NONE']) + [
        '### the names printed after and not before: %d' % len(new)] + ['    %s %s' % (n, fd[n]) for n in new]
    L += ['', '### ### **BEFORE %d TERMINALS ; EACH PRINTED AFTER %s ; DIFFERING %d ; NEW %d ; EQUAL LINE FOR LINE %s.**' % (
        len(bd), all(n in fd for n in bd), len(diff), len(new), b == f)]
    put_txt('%s_prints_%s.txt' % (ACT, kernel), L)
    print(L[-1])


# ### the quotation search, data/b690_rules.txt row (2): one distinctive substring per removed or changed line of the README cut (README.md :9
# ### at 53df27f), checked to stand in its own removed line before it is searched; the second shape case-insensitive and shorter
QUOTE_NEEDLES = ('are already proved in SIDE-kernel',)
QUOTE_WIDE = ('already proved',)
QUOTE_SETS = {'quote_simplicity_readme': (QUOTE_NEEDLES, QUOTE_WIDE)}


def quote(*a):
    """`quote <kernel dir> <base> <tip> <bank stem>`: every line the cut removes or changes (the `-` lines of git diff base..tip) read, one
    needle of the set assigned to each by containment and refused where a removed line carries none or a needle stands in no removed line;
    each needle searched with git grep -n -F at the tip across the kernel's whole tracked tree, in two shapes; every hit printed with its
    quoting line and entered as a residue; the control at the base. data/b698_<stem>.txt (.json)."""
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
    L = ['b698 -- THE QUOTATION SEARCH BEFORE THE MERGE, data/b690_rules.txt row (2), OVER %s (%s)' % (os.path.basename(kd), utc()), '',
         '### the cut: git diff %s..%s ; the lines it removes or changes %d ; one needle each, checked to stand in its own removed line; each searched' % (
             base, tip, len(rows)),
         '### with git grep -n -F at the tip %s across the kernel`s whole tracked tree. Rows are removed lines: needle | hits (file:line: the quoting' % tip,
         '### line):']
    for r in rows:
        L.append('  %-44s | %d hit(s) ; case-insensitive %-26r %d hit(s) | removed: %s' % (r['needle'], len(r['hits']), r['wide'], len(r['hits_wide']),
                                                                                    r['line'].strip()[:100]))
        L += ['      %s' % h for h in r['hits_wide']]
    q = sorted(set(h.split(':', 2)[1] + ':' + h.split(':', 3)[2] for _n, h in hits))
    ctl = [(r['needle'], len([x for x in g(kd, 'grep', '-n', '-F', r['needle'], base, '--').split(NL) if x.strip()]),
            len([x for x in g(kd, 'grep', '-n', '-i', '-F', r['wide'], base, '--').split(NL) if x.strip()])) for r in rows]
    L += ['', '### THE CONTROL: each needle at the base %s, where the removed line stands (needle ; case-exact hits ; case-insensitive hits):' % base]
    L += ['  %-44s ; %d ; %d' % c for c in ctl]
    L += ['### the control %s' % ('FIRES FOR EVERY NEEDLE IN BOTH SHAPES' if all(c[1] and c[2] for c in ctl) else '### DOES NOT FIRE FOR EVERY NEEDLE')]
    L += ['', '### THE QUOTING LINES, DISTINCT (file:line): %s' % (', '.join(q) or 'NONE'),
          '### the yields: the case-exact shape %d hit(s) on %d line(s) ; the case-insensitive shape %d hit(s) on %d line(s)' % (
              sum(len(r['hits']) for r in rows), len(set(h.split(':', 3)[1] + ':' + h.split(':', 3)[2] for r in rows for h in r['hits'])),
              len(hits), len(q)),
          '', '### ### **REMOVED OR CHANGED LINES %d ; NEEDLES SEARCHED %d IN TWO SHAPES ; QUOTING LINES %d -- EACH ENTERED AS A RESIDUE.**' % (
              len(rows), len(rows), len(q))]
    put_txt('%s_%s.txt' % (ACT, stem), L)
    put_json('%s_%s.json' % (ACT, stem), dict(at=utc(), kernel=kd, base=base, tip=tip, rows=rows, hits=[list(h) for h in hits]))
    print(NL.join(L))


RECUT = dict(kernel='SIDE-simplicity', base='53df27f', branch='recut-simplicity-readme-b698', tag='v0.1.2', prior='v0.1.1', file='README.md',
             line=9, prints_before='b697_axioms_SIDE-simplicity_after.txt', prints_after='b698_axioms_SIDE-simplicity_after.txt')


def readmecut(*a):
    """data/b698_readme_cut.txt (.json): the README re-cut on the author's word -- the branch and its one commit, the line before and after
    (git show at the base and at the merge), the run and the prints, the quotation search, the merge (parents, merged tree against the built
    tree), the tag peeled and its message naming the prior tag."""
    k = RECUT['kernel']
    kd = 'D:/' + k
    rr = [r for r in (jl('%s_runner_rows.json' % ACT).get('rows') or []) if r.get('kernel') == k]
    if len(rr) != 1:
        sys.exit('### THE RUNNER ROWS DO NOT CARRY ONE SIDE-simplicity RUN -- NOTHING WRITTEN')
    tip = rr[0]['ref']
    mainc = g(kd, 'rev-parse', 'main').strip()
    parents = g(kd, 'rev-list', '--parents', '-n', '1', mainc).split()
    mt, tt = g(kd, 'rev-parse', mainc + '^{tree}').strip(), g(kd, 'rev-parse', tip + '^{tree}').strip()
    tag_peel = g(kd, 'rev-parse', '--verify', '--quiet', RECUT['tag'] + '^{commit}').strip()
    tag_msg = g(kd, 'tag', '-l', '--format=%(contents:subject)', RECUT['tag']).strip()
    prior_peel = g(kd, 'rev-parse', RECUT['prior'] + '^{commit}').strip()
    l0 = ((_show(kd, RECUT['base'], RECUT['file']) or '').split(NL) + [''] * 20)[RECUT['line'] - 1]
    l1 = ((_show(kd, mainc, RECUT['file']) or '').split(NL) + [''] * 20)[RECUT['line'] - 1]
    act = [x for x in rdn('%s_residue_actions.txt' % ACT).split(NL)]
    i = next((n for n, x in enumerate(act) if x.strip().startswith('THE SUCCESSOR LINE, whole:')), None)
    want = ''
    if i is not None:
        j = i + 1
        blk = [act[i].split('whole:', 1)[1]]
        while j < len(act) and act[j].startswith('    ') and not act[j].strip().startswith('SOURCE ROWS'):
            blk.append(act[j])
            j += 1
        want = ' '.join(' '.join(blk).split()).strip('"')
    pv = _vl('%s_prints_%s.txt' % (ACT, k))
    qv = _vl('%s_quote_simplicity_readme.txt' % ACT)
    others = [l for l in g(kd, 'diff', '--name-only', RECUT['base'], mainc).split(NL) if l.strip()]
    L = ['b698 -- COMPONENT 4, (R308)(5): THE README RE-CUT OF %s ON THE AUTHOR`S WORD "apply" (%s)' % (k, utc()), '',
         '### the branch %s from main %s, its one commit %s (README.md alone), pushed alone by push_gated`s branch mode named --scratch (relay '
         'data/b698_simplicity_cut_push_out.txt)' % (RECUT['branch'], RECUT['base'], tip[:7]),
         '### the run: %d at the tip (relay data/b698_runner_%s_after.txt), gate %s; the prints against b697`s after-run at b491ac5: %s' % (
             rr[0]['run_id'], k, rr[0]['gate'], pv.strip('#* ')),
         '### the quotation search (relay data/b698_quote_simplicity_readme.txt): %s' % qv.strip('#* '),
         '### the merge %s by --no-ff, its parents %s, the merged tree %s the built tree %s (%s); the files the merge changes from the base: %s' % (
             mainc[:7], ' '.join(p[:7] for p in parents[1:]), mt[:12], tt[:12], 'EQUAL' if mt == tt else '### DIFFER', others),
         '### the tag %s peeled to %s (%s), its message %r naming the prior tag %s = %s (relay data/b698_simplicity_merge_push_out.txt)' % (
             RECUT['tag'], tag_peel[:12] or '### ABSENT', 'THE MERGE' if tag_peel == mainc else '### NOT THE MERGE', tag_msg, RECUT['prior'], prior_peel[:7]),
         '', '### README.md :9 at the base %s, verbatim:' % RECUT['base'], '    ' + l0,
         '### README.md :9 at the merge %s, verbatim:' % mainc[:7], '    ' + l1,
         '### the successor line of relay data/b698_residue_actions.txt, whitespace collapsed, equal to the merged line: %s' % (want == ' '.join(l1.split()))]
    ok = want == ' '.join(l1.split()) and mt == tt and tag_peel == mainc and others == [RECUT['file']] and 'EQUAL LINE FOR LINE True' in pv \
        and 'QUOTING LINES 0' in qv and rr[0]['gate'] == 'DERIVES'
    L += ['', '### ### **SIDE-simplicity README :9 RE-CUT: THE ACTION APPLIED %s ; RUN %d %s ; PRINTS EQUAL %s ; QUOTING LINES LEFT %s ; TAG %s AT THE MERGE %s.**' % (
        want == ' '.join(l1.split()), rr[0]['run_id'], rr[0]['gate'], 'EQUAL LINE FOR LINE True' in pv, (re.findall(r'QUOTING LINES (\d+)', qv) or ['?'])[0],
        RECUT['tag'], ok)]
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('%s_readme_cut.txt' % ACT, L)
    put_json('%s_readme_cut.json' % ACT, dict(at=utc(), kernel=k, tip=tip, merge=mainc, parents=parents[1:], merged_tree=mt, built_tree=tt,
                                              tag=RECUT['tag'], tag_peel=tag_peel, prior_peel=prior_peel, line_before=l0, line_after=l1, ok=ok))
    print(NL.join(L))


# ================================================================================ COMPONENT 4: THE AUTHOR'S WORD ON "run", ITS TWO ENTRIES
ONECOPY_H = ('*Appended 2026-10-21 by b698 beneath `W-ORD-ONE-COPY` (:14386, its trigger re-written at :14450), under `(R308)`(5) and the '
             'author’s word on the stale cell -- THE PARTNER COPY’S DIFFERING LINES, THIS ACT’S READING:*')


def onecopy(*a):
    """data/b698_onecopy.txt: the SIMPLICITY_OF_RIEMANN_ZEROS table and its partner copy's, each found by the generator's own find_table with
    the roster's anchor (data/b698_roster_simplicity.json), at PLACE-papers HEAD after the cell was written; the lines that differ, each with its
    line in both files; and `onecopy land [dry]` -- the reading entered beneath W-ORD-ONE-COPY through the guarded landing."""
    import correspondence_gen as CG
    t = jl(ROSTER_ONE)['tables'][0]
    A = (_show(PP, 'HEAD', t['path']) or '').split(NL)
    B = (_show(PP, 'HEAD', t['partner']) or '').split(NL)
    fa, fb = CG.find_table(A, t), CG.find_table(B, t)
    if isinstance(fa, str) or isinstance(fb, str):
        sys.exit('### A TABLE NOT FOUND: %r ; %r -- NOTHING WRITTEN' % (fa, fb))
    ta, tb = A[fa[0]:fa[1]], B[fb[0]:fb[1]]
    import difflib
    ops = difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes()
    rows = []
    for tag, i1, i2, j1, j2 in ops:
        if tag == 'equal':
            continue
        for k in range(max(i2 - i1, j2 - j1)):
            ia, ib = (i1 + k if i1 + k < i2 else None), (j1 + k if j1 + k < j2 else None)
            rows.append(dict(op=tag, a=(fa[0] + ia + 1) if ia is not None else None, b=(fb[0] + ib + 1) if ib is not None else None,
                             ta=ta[ia] if ia is not None else '', tb=tb[ib] if ib is not None else ''))
    if 'land' in a:
        n = len(rows)
        body = (' the generator, run on the author’s word at b698 on a one-table roster, wrote SIMPLICITY_OF_RIEMANN_ZEROS.md :441 alone and left '
                'its partner copy SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md unwritten. Read line by line at PLACE-papers HEAD after the write, by the '
                'generator’s own table finder (relay data/b698_onecopy.txt), the two copies’ Correspondence tables differ in %d lines -- %d before '
                'the write, :441 now among them: the copy’s %s against the partner’s %s, the partner citing older kernel versions and carrying '
                'longer status cells. The figure 6 the generator prints, and the seat’s prompt carried, is b672’s roster field '
                'partner_lines_differing, stored at b672 and not recounted (relay data/b698_defects.txt). The reading is this act’s; neither copy '
                'is moved by it and the one copy of record stays the order’s question. Status OPEN.' % (
                    n, n - 1, ', '.join(':%s' % r['a'] for r in rows), ', '.join(':%s' % r['b'] for r in rows)))
        land([('OPEN_TRAILS.md', ONECOPY_H, NL + ONECOPY_H + body + NL)], '%s_onecopy_line.json' % ACT, 'onecopy', entry=14386,
             check=[('OPEN_TRAILS.md', 14386, '**`W-ORD-ONE-COPY`**'), ('OPEN_TRAILS.md', 14450, '**`W-ORD-ONE-COPY`**')], dry='dry' in a)
        return
    L = ['%s -- COMPONENT 4, (R308)(5) AND THE AUTHOR`S WORD ON "run": THE PARTNER COPY`S DIFFERING LINES, READ AT PLACE-papers HEAD %s (%s)' % (
        ACT, g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc()), '',
         '### the tables: %s :%d-:%d and its partner %s :%d-:%d, each found by tools/correspondence_gen.py`s find_table with the roster`s anchor;'
         % (t['path'], fa[0] + 1, fa[1], t['partner'], fb[0] + 1, fb[1]),
         '### compared line by line (SequenceMatcher, autojunk off). Rows are differing lines: op | the copy`s line | the partner`s line | the two texts.', '']
    for r in rows:
        L += ['  %-8s | :%-4s | :%-4s' % (r['op'], r['a'] or '-', r['b'] or '-'), '      copy:    ' + r['ta'], '      partner: ' + r['tb']]
    L += ['', '### ### **THE TWO TABLES DIFFER IN %d LINES (the generator`s reading: 6) ; NEITHER COPY MOVED BY THIS READING.**' % len(rows)]
    put_txt('%s_onecopy.txt' % ACT, L)
    print(NL.join(L))


def heldcells(*a):
    """the three SIDE-archimedean cells the whole roster's dry run would move (data/b698_correspondence_dry_after.txt), named in the cut bank
    (data/b698_readme_cut.txt) as the cells data/b698_rules.txt row (1) regenerates at b699's step, on the author's word; appended beneath the
    bank's verdict line by this route alone."""
    dry = [l.strip() for l in rdn('%s_correspondence_dry_after.txt' % ACT).split(NL) if l.startswith('    PATHS_TO_THE_CRITICAL_LINE :285 |')]
    cut = rdn('%s_readme_cut.txt' % ACT)
    if len(dry) != 3 or 'THE CELLS HELD SINCE b693' in cut:
        sys.exit('### NOT THREE HELD CELLS (%d), OR ALREADY NAMED -- NOTHING WRITTEN' % len(dry))
    add = ['', '### THE CELLS HELD SINCE b693, NAMED ON THE AUTHOR`S WORD ON "run" (data/b698_author_answers.txt): the whole roster`s dry run after the',
           '### tag (data/b698_correspondence_dry_after.txt) moves three SIDE-archimedean cells at PLACE-papers PATHS_TO_THE_CRITICAL_LINE :285,',
           '### held at b693, b695 and b697; data/b698_rules.txt row (1) regenerates them at b699`s step (rows are cells, the generator`s lines with',
           '### each cell`s old and new text cut at 90 characters):']
    add += ['  ' + ' | '.join(x[:90] for x in l.split(' | ')) for l in dry]
    add += ['### ### **THE CELLS HELD SINCE b693: 3, AT PATHS_TO_THE_CRITICAL_LINE :285 (kernel, profile, status), FOR b699 BY RULE (1).**']
    put_txt('%s_readme_cut.txt' % ACT, cut.rstrip(NL).split(NL) + add)
    print(NL.join(add))


# ================================================================================ THE LATE ROUTES (b697's, carried at Component 5 with b698's names)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
# ### the previous act's window: b697 ran in its own session (b97f6790); this act opens a new one (c677eaf2) -- b689's form for a new session
PREV_ACT, PREV_SESSION, PREV_ANCHOR = 'b697', 'b97f6790-cfa6-43ae-aa06-9d3a07249ec4', 'RULING (R307) BEGIN'
PREV_SESSION_PATH = '%s/%s.jsonl' % (PROJ, PREV_SESSION)
PREV_SUBAGENTS = '%s/%s/subagents' % (PROJ, PREV_SESSION)


def _bg_calls():
    out = set()
    for _i, o, _st, _sid in _session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and (c.get('input') or {}).get('run_in_background'):
                out.add((o.get('timestamp'), (c.get('input') or {}).get('command')))
    return out


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
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
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def sed_cmd(cmd):
    return SED.search(QUOTED.sub('""', cmd)) is not None


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


def prev_capture():
    """G-EDIT-ROUTE's window over the previous act (b689's form, carried for a new session): b697's capture AFTER ITS POST-PUSH SUITE -- every
    command of b697's session (b97f6790) from the call that combined b697's post-push parts into data/b697_checks_postpush.txt to that
    session's end, its closing's commands among them; this act runs in a session of its own."""
    rows = ER.capture(PREV_SESSION_PATH, PREV_ANCHOR, PREV_SUBAGENTS)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV_ACT in r['cmd'] and '--combine' in r['cmd']]
    if not first:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE IS NOT IN ITS SESSION`S CAPTURE -- NOTHING READ')
    out = [dict(r, src='%s %s' % (PREV_ACT, r['src'])) for r in rows if first[0] <= r['ts']]
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
    """(R308)(7) and the ferry: a delete command names one branch and carries no glob and no variable in any half; b693's reader, carried."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    vs = SHELL_VAR.findall(c)
    return names, [ch for ch in '*?[' if ch in SHELL_VAR.sub('', c)], vs


def chained_after(cmd):
    """data/b694_rules.txt row (1): anything chained after a delete in the same command (`;`, `&&`, `||`, `|`), read outside quoted strings."""
    c = QUOTED.sub('""', cmd)
    m = re.search(r'(--delete\s+\S+|branch\s+-[dD]\s+\S+)', c)
    return bool(m) and bool(re.search(r'[;&|]', c[m.end():]))


IDENT = ('psinary', 'hotmail', 'seale', 'york', 'orcid', '0009-0008')


def outbound():
    """the outbound requests other than git and gh: the session's web searches, subagent prompts and fetches since the anchor. No tool of this
    act makes a request of its own; the runner's reads go by gh to github.com."""
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
    disp = [r for r in sh_ if re.search(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py dispatch\b(?![^\n]*\bdry\b)', QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in sh_ if (r.get('bg') or re.search(r'Start-Process|\bnohup\b|run_in_background', QUOTED.sub('""', r['cmd'])))]
    seds = [r for r in sh_ if sed_cmd(r['cmd'])]
    nulls = [r for r in sh_ if REDIRECT_NULL.search(QUOTED.sub('""', r['cmd']))]
    redir = [r for r in sh_ if REDIRECT_ANY.search(QUOTED.sub('""', r['cmd']))]
    pipes = [r for r in sh_ if PIPE_FILTER.search(QUOTED.sub('""', r['cmd']))]
    pyreads = [r for r in sh_ if PY_PRINT_READ.search(r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    chained = [r['n'] for r in mv if delete_shape(r['cmd'])[0] and chained_after(r['cmd'])]
    halves = dict((r['n'], len([x for x in re.split(r'&&|\|\||;|\|', QUOTED.sub('""', r['cmd'])) if x.strip()])) for r in mv)
    ob = outbound()
    L = ['%s -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % (ACT, utc()), '',
         '### the source: the seat`s session %s from its first user line carrying %r, with its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (b697, its own session %s, from its post-push combine to that session`s '
              'end): %d commands from %s, its offences printed whole (%d):' % (PREV_SESSION[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES, ONE PER TREE STATE (relay data/b698_dispatches.json) (%d):' % len(disp)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN, BY THEIR TEXT OR THE TOOL`S run_in_background PARAMETER (%d):' % len(
        detach)] + (['  #%d %s%s' % (r['n'], '[run_in_background] ' if r.get('bg') else '', r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING sed IN ANY FORM (data/b685_rules.txt row (2)) (%d):' % len(seds)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in seds] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT ONTO /dev/null, read outside quoted strings (%d):' % len(nulls)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], r['cmd'].split(NL)[0][:200]) for r in nulls] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT OF ANY STREAM, read outside quoted strings (%d):' % len(redir)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in redir] or ['  NONE'])
    L += ['', '### THE COMMANDS PIPING INTO A SHELL FILTER (head, tail, wc, grep and the like), read outside quoted strings (%d):' % len(pipes)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in pipes] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT RUN AN INTERPRETER`S ONE-LINE PROGRAM (python -c), each its first line (%d):' % len(pyreads)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:220]) for r in pyreads] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R308)(7) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
              'nothing chained after): ' + ('; '.join('#%d deletes %s, halves %d, globs %s, variables %s, chained after %s' % (
                  n, d, halves.get(n, 0), gl or 'none', vs or 'none', n in chained) for n, d, gl, vs in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git AND gh (web searches, subagent prompts and fetches), each with the author`s identifiers found '
              'in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    good = sum(1 for n, d, gl, vs in shapes if len(d) == 1 and not gl and not vs and n not in chained)
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; REDIRECTS ONTO /dev/null %d ; '
              'REDIRECTS OF ANY STREAM %d ; PIPES INTO A SHELL FILTER %d ; ONE-LINE PROGRAMS %d ; MOVE OR DELETE COMMANDS %d ; BRANCH DELETES OF ONE '
              'BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(nulls), len(redir), len(pipes), len(pyreads), len(mv), good, len(shapes), len(ob),
                  sum(1 for r in ob if r['identifiers']))]
    if 'dry' in a:
        print(L[-1])
        return
    put_txt('%s_commands.txt' % ACT, [l.replace('\r', '') for l in L])
    put_json('%s_commands.json' % ACT, dict(at=utc(), anchor=K.ANCHOR, rows=rows,
                                           offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                           prev=dict(act=PREV_ACT, session=PREV_SESSION, rows=len(prev),
                                                     offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                           local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                           seds=[r['n'] for r in seds], null_redirects=[r['n'] for r in nulls], redirects=[r['n'] for r in redir],
                                           pipes=[r['n'] for r in pipes], py_programs=[r['n'] for r in pyreads], moves_deletes=[r['n'] for r in mv],
                                           delete_shapes=[dict(n=n, deletes=d, globs=gl, variables=vs, halves=halves.get(n), chained=n in chained)
                                                          for n, d, gl, vs in shapes],
                                           outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r, o in phits:
        print('  PREVIOUS-ACT OFFENCE #%s %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


def _lines_now(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().count(NL)
    except OSError:
        return None


def reads(*a):
    """data/b698_rules.txt row (2), binding from b698: the Read tool reads a file whole where the file is under two hundred lines, and by
    offset and limit otherwise. Every Read call of the seat since the anchor, read from the session by assistant message, the file's line
    count read now beside it; a whole read of a file of two hundred lines or more is an offence. data/b698_read_calls.txt."""
    rows = []
    for i, o, _st, _sid in _session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'Read':
                inp = c.get('input') or {}
                p = inp.get('file_path') or ''
                rows.append(dict(line=i, ts=o.get('timestamp'), path=p, offset='offset' in inp, limit='limit' in inp, lines=_lines_now(p)))
    whole = [r for r in rows if not (r['offset'] and r['limit'])]
    bad = [r for r in whole if r['lines'] is None or r['lines'] >= 200]
    L = ['%s -- THE READ CALLS SINCE THE ANCHOR, BY data/b698_rules.txt ROW (2) (%s)' % (ACT, utc()), '',
         '### the rule: whole where the file is under two hundred lines, by offset and limit otherwise. Rows are Read calls without both offset and',
         '### limit: transcript line | time | the file`s lines read now | WITHIN THE RULE or ### AN OFFENCE | path']
    L += ['  %s | %s | %s | %s | %s' % (r['line'], r['ts'], r['lines'], '### AN OFFENCE' if r in bad else 'WITHIN THE RULE', r['path']) for r in whole] or ['  NONE']
    L += ['', '### ### **READ CALLS %d ; WITH OFFSET AND LIMIT %d ; WHOLE %d ; WHOLE OF A FILE OF 200 LINES OR MORE %d.**' % (
        len(rows), len(rows) - len(whole), len(whole), len(bad))]
    if 'dry' not in a:
        put_txt('%s_read_calls.txt' % ACT, L)
    print(NL.join(L[-1 - len(bad):]) if bad else L[-1])


# ================================================================================ THE LATE ROUTES (b697's, carried with b698's names)
def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle', 'SIDE-bijection', 'SIDE-class-number-anomaly',
                                   'SIDE-spinor', 'SIDE-li-map', 'SIDE-rcurve', 'SIDE-archimedean', 'SIDE-interfaces', 'SIDE-simplicity']


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    put_json('%s_kernels_face.json' % ACT, dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-simplicity read after its README merge and tag v0.1.2; no kernel written after this read)' % len(ks))


def seal_hashes():
    import hashlib
    rec_ = (jl('%s_seal_hashes.json' % ACT).get('tools') or {}) if os.path.isfile(os.path.join(D, '%s_seal_hashes.json' % ACT)) else {}
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


ROOT_EXCLUDE = re.compile(r'^b698_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*|close_sentence|read_calls)\.?(txt|json|md|jsonl|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('%s_' % ACT) and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(K.SHARED_APPENDED))


def rootbanks(*a):
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['%s -- G-ROOT-BANKS-COMMITTED`S READING: THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ;'
         ' carried by HEAD ; HEAD`s blob equal to the file' % (ACT, utc()), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('%s_root_banks.txt' % ACT, L)
    put_json('%s_root_banks.json' % ACT, dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/%s_seal_hashes.json' % ACT in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### G-ROOT-BANKS-COMMITTED: A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', ACT] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('%s_act_root.json' % ACT)
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='%s_ra_' % ACT) as tmp:
        cp_ = os.path.join(tmp, os.path.basename(bank_))
        b_ = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
        b_[0] ^= 0x01
        with open(cp_, 'wb') as fh:
            fh.write(bytes(b_))
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
    L = ['%s -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % (ACT, utc()), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '-')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('%s_root_arm.txt' % ACT, L)
    put_json('%s_root_arm.json' % ACT, dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['%s -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (ACT, utc(), r.returncode, g(ROOT, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('%s_table_final.txt' % ACT, L)
    put_json('%s_table_final.json' % ACT, dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                              gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


def _g2_of(path):
    t = rd(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _standing():
    import b697_worklist as K697
    return sorted(set(_g2_of(os.path.join(ROOT, *K.B697_FACE.split('/')))) - set(K697.ACT_ARMS))


def standing(*a):
    """the standing arms b698 carries: b697's face's (G2) arms less b697's act arms (R264)(2); printed only."""
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


def armsecs(*a):
    st = _standing()
    rows, phases, runs = [], {}, {}
    for p in K.PARTS:
        j = jl('%s_arm_seconds_%s.json' % (ACT, p))
        phases[p] = j.get('phases') or {}
        runs[p] = j.get('run_secs')
        for nm, s in (j.get('arms') or {}).items():
            rows.append(dict(arm=nm, part=p, secs=s, standing=nm in st))
    srows = sorted([r for r in rows if r['standing']], key=lambda r: -r['secs'])
    miss = sorted(set(st) - set(r['arm'] for r in srows))
    L = ['%s -- THE STANDING ARMS` SECONDS AT HEAD, BY PART, FROM THE PRE-RUN (%s): the per-part seconds of the six parts' % (ACT, utc()), '',
         '### the source: data/b698_arm_seconds_<part>.json, written by tools/b698_checks.py at its pre-run, each arm`s seconds the sum of its',
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
    put_txt('%s_arm_seconds.txt' % ACT, L)
    put_json('%s_arm_seconds.json' % ACT, dict(at=utc(), rows=srows, phases=phases, run_secs=runs, standing=len(st), clocked=len(srows), missing=miss,
                                              slowest=[r['arm'] for r in srows[:3]]))
    print(L[-1])


# ================================================================================ THE SCORES: (N1)-(N5) OF (R308)'S FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and commits and not the entry; the entry reads the scorer's bank. `scores`
# ### writes data/b698_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there and is read at the close.
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b697_closing_push_out.txt', 'b697_arith_plan.txt')
N5_RELAY_TOOLS = ('tools/circuit_correspondence.py',)      # ### the reader (R308)(3) builds, named by N5


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


READERS += ['read_score_row', 'read_head']


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


def _n1():
    """N1: no lean process on this host; a runner dispatched for the README re-cut alone, where the word is given (the author's answer 1
    amending it to the lv-conservation print at v0.13.0 as well, where a hosted run could print it -- it could not, and none was dispatched)."""
    cm = jl('%s_commands.json' % ACT)
    dj = jl('%s_dispatches.json' % ACT).get('rows') or []
    rc = jl('%s_readme_cut.json' % ACT)
    tip_tree = g(K.KERNEL_DIR, 'rev-parse', (rc.get('tip') or 'x') + '^{tree}').strip()
    ok = bool(cm) and not cm.get('local_lean') and len(dj) == len(cm.get('dispatches') or []) == 1 and dj[0].get('kernel') == K.KERNEL \
        and dj[0].get('ref') == rc.get('tip') and dj[0].get('tree') == tip_tree
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches %s (relay data/b698_dispatches.json: %d row(s), %s at %s, '
        'the README cut`s tip %s): one, for the README re-cut, none at SIDE-lv-conservation (relay data/b698_correspondence_dominance.txt: a hosted '
        'run at v0.13.0 cannot print the face) (relay data/b698_commands.txt, %d commands read)' % (
            cm.get('local_lean') if cm else 'unread', cm.get('dispatches') if cm else 'unread', len(dj), dj[0].get('kernel') if dj else '-',
            (dj[0].get('ref') or '')[:7] if dj else '-', (rc.get('tip') or '')[:7], len(cm.get('rows') or [])))


def _n2():
    """N2: the two controls print as stated before the real reading -- HOLDS at every binder on the self-comparison, DIFFERS at the planted
    binder and there alone."""
    t = rdn('%s_correspondence_dominance.txt' % ACT)
    j = jl('%s_correspondence_dominance.json' % ACT)
    ic, ir = t.find('== THE CONTROLS, PRINTED BEFORE THE REAL READING'), t.find('== THE READING:')
    c1 = re.search(r'\(C1\) h2_sign against itself[^\n]*: HOLDS-BY-CORRESPONDENCE', t) is not None
    c2 = re.search(r'\(C2\) h2_sign against a planted statement[^\n]*: DIFFERS at binder 1\n', t) is not None
    vl = 'CONTROLS: C1 HOLDS AT EVERY BINDER True ; C2 DIFFERS AT THE PLANTED BINDER (1) AND THERE ALONE True' in t
    ok = 0 <= ic < ir and c1 and c2 and vl and (j.get('controls') or {}) == dict(c1=True, c2=True)
    return ('HELD' if ok else 'REFUTED'), (
        'the controls` block at %d before the reading at %d in relay data/b698_correspondence_dominance.txt: %s; C1 HOLDS-BY-CORRESPONDENCE: %s; '
        'C2 DIFFERS at binder 1: %s; both at every row as stated: %s' % (ic, ir, 0 <= ic < ir, c1, c2, vl))


def _n3():
    """N3: every binder of the two statements side by side in the dominance bank with its own verdict, the summary verdict following the rows;
    no verdict written from the Correspondence row's text alone."""
    t = rdn('%s_correspondence_dominance.txt' % ACT)
    j = jl('%s_correspondence_dominance.json' % ACT)
    rows = j.get('rows') or []
    nb = len([r for r in rows if r[0] != 'conclusion'])
    each = all(len(r) == 5 and r[3] in ('AGREE', 'DIFFERS') for r in rows) and rows[-1][0] == 'conclusion' if rows else False
    m = re.search(r'binders (\d+) against (\d+)', t)
    side = bool(m) and nb == max(int(m.group(1)), int(m.group(2)))
    i_last = t.rfind('             | DIFFERS |') if 'DIFFERS' in t else -1
    i_sum = t.find('### the summary follows the rows')
    follows = 0 <= i_last < i_sum
    srcs = 'h2_sign: its #print at SIDE-explicit-formula v0.26' in t and 'SIDE-lv-conservation`s face: residue_irreducible at v0.13.0' in t
    ok = each and side and follows and srcs
    return ('HELD' if ok else 'REFUTED'), (
        'rows in relay data/b698_correspondence_dominance.json: %d (binders %d and the conclusion), each with its own verdict: %s; every binder of '
        'both statements present (%s): %s; the summary after the last row: %s; the verdict read from the two statements, their sources named '
        '(the print and the source text), not from the row`s text: %s' % (len(rows), nb, each, m.group(0) if m else '-', side, follows, srcs))


def _n4():
    """N4: every regularity use cited by file and line with the hypothesis it consumes; the per-column counts equal the rows."""
    t = rdn('%s_regularity_uses.txt' % ACT)
    c = rdn('%s_regularity_counts.txt' % ACT)
    try:
        rows = [read_use_row(l) for l in t.split(NL) if re.match(r'^  [UP]\d+ ', l)]
    except ValueError:
        rows = []
    hyp = all(re.search(r'\| (C2|EVEN|COMPACT SUPPORT|THE FORM)', l) for l in t.split(NL) if re.match(r'^  [UP]\d+ ', l))
    sums = re.findall(r'sum (\d+) \(= rows (True|False)\)', c)
    eq = len(sums) == 6 and all(s[1] == 'True' for s in sums)
    quotes = re.search(r'QUOTED LINES EQUAL TO THE FILE AT v0\.34: (\d+) of (\d+)', c)
    q_ok = bool(quotes) and quotes.group(1) == quotes.group(2) == str(len(rows))
    unl = 'unlisted NONE' in c
    ok = bool(rows) and hyp and eq and q_ok and unl
    return ('HELD' if ok else 'REFUTED'), (
        'rows read by read_use_row in relay data/b698_regularity_uses.txt: %d, each with its file :line and the hypothesis it consumes: %s; the six '
        'column counts (relay data/b698_regularity_counts.txt) each summing to its rows: %s; every quoted line equal to its file at v0.34: %s; '
        'the completeness read, no code line unlisted: %s' % (len(rows), hyp, eq, quotes.group(0) if quotes else '-', unl))


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
    out = []
    for l in g(repo, 'reflog', '--date=unix', '--format=%gd %gs').split(NL):
        m = re.match(r'HEAD@\{(\d+)\} (commit \(amend\).*)$', l.strip())
        if m and lock and int(m.group(1)) >= lock:
            out.append(m.group(2)[:60])
    return out


def _one_git_write():
    """the standing rule arm G-RULE-ONE-GIT-WRITE's own reading over this act's session (tools/rule_arms.py, unedited)."""
    import rule_arms as RA
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    try:
        S = RA.sources(ACT, SESSION, K.ANCHOR, K.PARTS, lock, K.PRE_RELAY, K.PRE_PP)
        ok, n, b, note = RA.reading('G-RULE-ONE-GIT-WRITE', S)
    except Exception as e:
        return False, 'the rule arm raised %s' % type(e).__name__
    return ok, note[:200]


def _n5():
    import rule_arms as RA
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    t0, moved, tags = _kernels_moved()
    moved_beyond = [m for m in moved if m[0] != K.KERNEL]
    tags_beyond = [t for t in tags if t != (K.KERNEL, K.NEXT_TAG)]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b698_', x) and x not in N5_RELAY_TOOLS]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b698_|audit_b698_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA) or x in N5_RELAY_TOOLS)]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    arms_added = sorted(set(RA.NAMES) - set(K.STANDING_ADDED) - set(_g2_of(os.path.join(ROOT, *K.B697_FACE.split('/')))))
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock) + _amended_after(K.KERNEL_DIR, lock)) if lock else []
    ob = jl('%s_commands.json' % ACT).get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    wf = (_show(K.KERNEL_DIR, 'main', '.github/workflows/build-module.yml') or '').lower()
    wf_ident = [w for w in IDENT if w in wf]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    chained = [d['n'] for d in (jl('%s_commands.json' % ACT).get('delete_shapes') or []) if d.get('chained')]
    gw_ok, gw_note = _one_git_write()
    rc = jl('%s_readme_cut.json' % ACT)
    word = rc.get('ok') is True and [m[1] for m in moved if m[0] == K.KERNEL] and all(
        m[1] in (rc.get('merge') or '')[:len(m[1])] or m[1] == (rc.get('tip') or '')[:len(m[1])] for m in moved if m[0] == K.KERNEL)
    ok = k_ok and not moved_beyond and not tags_beyond and not pp_beyond and not kinds_beyond and not shared_tools and not differ \
        and not arms_added and not amended and not ident and not wf_ident and not pat and not chained and gw_ok and bool(word)
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; kernel main commits '
            'since the act began beyond SIDE-simplicity`s README re-cut on the author`s word (its commits %s, the re-cut bank ok %s): %s; tags made '
            'beyond %s %s: %s; no standing arm added (tools/rule_arms.py`s names beyond b697`s face): %s; shared tools edited: %s; sealed tools not '
            'agreeing: %s; commits amended after the seal: %s; deletes with anything chained after: %s; one git write per message '
            '(G-RULE-ONE-GIT-WRITE`s reading: %s): %s; PLACE-papers beyond the two ledgers and the regenerated page: %s; relay files of a kind beyond '
            'the act`s banks and tools, the reader, the table, the root list, b697`s push-out bank and the plan`s row: %s; "patent" in the lines '
            'written: %s; outbound requests other than git and gh %d, an identifier of the author in %s; in the workflow file %s' % (
                K.DRAFT, k_ok, [m[1] for m in moved if m[0] == K.KERNEL] or 'NONE', rc.get('ok'), moved_beyond or 'NONE', K.KERNEL, K.NEXT_TAG,
                tags_beyond or 'NONE', arms_added or 'NONE', shared_tools or 'NONE', differ or 'NONE', amended or 'NONE', chained or 'NONE', gw_note,
                gw_ok, pp_beyond or 'NONE', kinds_beyond or 'NONE', pat or 'NONE', len(ob), [r['line'] for r in ident] or 'NONE', wf_ident or 'NONE'))


def _s_scores():
    import collections
    TF, RA_ = jl('%s_table_final.json' % ACT), jl('%s_root_arm.json' % ACT)
    _r, _n, sh = seal_hashes()
    return {
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))
               if TF else 'waits on the final table (relay data/b698_table_final.json)'),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally' if RA_
               else 'waits on the root and its arm (relay data/b698_root_arm.json), computed after the entry'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }


def scores(*a):
    """`scores [dry]` writes data/b698_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b698_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        return
    if close:
        put_json('%s_scores_close.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('%s_scores.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def scores_line(S):
    """the entry's scores line, composed from the scores bank alone (the act arm G-ENTRY-SCORES-EQUAL composes it the same way and compares)."""
    return '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.'


# ================================================================================ THE RECORD: THE ENTRY BEFORE THE ROOT, THE TRAIL CARRYING IT
FACE = os.path.join(D, 'b698_registration_2026-10-21.txt')


def TRAIL_HEAD():
    return ('### b698 — lane two, act one hundred and twenty-five, the research act under (R308): b697 at its weight; CORRESPONDENCE-DOMINANCE '
            'built and read; the regularity-uses bank; the SIMPLICITY README line and the stale cell; two rules banked')


def _calls():
    return jl('%s_author_answers.json' % ACT).get('calls') or []


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _figs():
    """the figures the title and the entry carry, each read from its bank by a needle that passes a dotted name and leaves a closing period."""
    dj = jl('%s_correspondence_dominance.json' % ACT)
    v = dj.get('verdict') or '-'
    vb = re.match(r'(DIFFERS at binder \d+|HOLDS-BY-CORRESPONDENCE)', v)
    rows = dj.get('rows') or []
    c = rdn('%s_regularity_counts.txt' % ACT)
    cols = re.findall(r'DISCHARGED +(\d+) ; RE-PROVED +(\d+) ; OBSTRUCTED +(\d+) ; sum (\d+)', c)
    nu = re.search(r'THE USES \(SIDEExplicitFormula/\): rows (\d+)', c)
    npth = re.search(r'THE PATH \(the two explicit formulas` leaves\): rows (\d+)', c)
    rc = jl('%s_readme_cut.json' % ACT)
    pdiff = _vl('%s_correspondence_page_diff.txt' % ACT)
    oc = re.search(r'DIFFER IN (\d+) LINES', _vl('%s_onecopy.txt' % ACT))
    return dict(verdict=vb.group(1) if vb else '-', rows=len(rows), agree=sum(1 for r in rows if r[3] == 'AGREE'),
                nb=len([r for r in rows if r[0] != 'conclusion']), uses=nu.group(1) if nu else '-', path=npth.group(1) if npth else '-',
                w=['%s/%s/%s' % x[:3] for x in cols[:3]] + ['-'] * 3, wp=['%s/%s/%s' % x[:3] for x in cols[3:6]] + ['-'] * 3,
                readme=('re-cut, %s' % rc.get('tag')) if rc.get('ok') else 'carried', merge=(rc.get('merge') or '-')[:7],
                cell='regenerated' if 'THE PAGE ALONE True' in pdiff else 'held', onecopy=oc.group(1) if oc else '-')


def _title():
    f = _figs()
    return ('## CLAUSE-DOMINANCE by closure and by correspondence: 1 of 2 by closure, %s by correspondence; the regularity uses of classK in '
            'SIDE-explicit-formula: %s uses, W1 %s, W2 %s, W3 %s; SIDE-simplicity README :9 %s; the stale cell %s' % (
                f['verdict'], f['uses'], f['w'][0], f['w'][1], f['w'][2], f['readme'], f['cell']))


def _finding_text():
    """the FINDINGS entry, composed before the root: its scores line from the scores bank alone (data/b686_rules.txt row (1)); the root is
    carried by the trail record."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    br = _rl_lines('%s_bridge_line.json' % ACT) + ['-']
    oc = _rl_lines('%s_onecopy_line.json' % ACT) + ['-']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'SIDE-lv-conservation’s compiled face, residue_irreducible, is not the clause’s statement: read binder by binder against h2_sign, its source '
         'against h2_sign’s print, it differs at the first binder -- a test window ranging over classK against a sequence -- and at every one of '
         'its %d rows, the conclusion among them; CLAUSE-DOMINANCE stays 1 of 2, and the bridge’s open object is named. The %s uses of classK’s '
         'hypotheses in SIDE-explicit-formula admit, by the bank’s one-line sketches and with no Lean written, C¹ windows with an integrable '
         'second derivative and finite sums of autocorrelations, and stop at rapid decay without compact support, at the explicit formula’s '
         'strip, its prime sum and the detection join.' % (
             f['rows'], f['uses']), '',
         '*Filed at b698 on the author’s ruling `(R308)` and the author’s words at its prompts; %d question%s put. Banks: relay '
         '`data/b698_correspondence_dominance.txt`, `data/b698_regularity_uses.txt`, `data/b698_regularity_counts.txt`, '
         '`data/b698_residue_actions.txt`, `data/b698_readme_cut.txt`, `data/b698_correspondence_dry_after.txt`, '
         '`data/b698_correspondence_page_diff.txt`, `data/b698_onecopy.txt`, `data/b698_rules.txt`; the reader `tools/circuit_correspondence.py`.*' % (
             n_ans, '' if n_ans == 1 else 's'), '',
         '**The dominance** (`(R308)`(3), the eleventh row of the circuit specification): the reader compares two statements by identity after each '
         'kernel’s namespaces are stripped, binders aligned by position, bound names read by position. Its controls ran first -- h2_sign against '
         'itself holding at every binder, a planted copy with binder 1’s type changed differing there alone. On the author’s answers to the two '
         'citation misses, h2_sign was read from its print in the faces page’s generator input at v0.26, every file defining a name it carries '
         'byte-identical to v0.34, and residue_irreducible from its source at SIDE-lv-conservation v0.13.0, since no hosted run at that tag can '
         'print it. The reading, source against print: %s, the face’s %d binders against h2_sign’s 2, %d of %d rows agreeing. The open object '
         'is entered beneath '
         'W-ORD-H2-BRIDGE (OPEN_TRAILS :%s): the face reaches the clause only through its last binder, a Li-coefficient criterion.' % (
             f['verdict'], f['nb'], f['agree'], f['rows'], br[0]), '',
         '**The regularity uses** (`(R308)`(4), in b676’s form, no Lean written): %s uses in the programme’s modules and %s leaves of the two '
         'explicit formulas beneath them, each cited by file and line at v0.34 and its quoted line checked there; the completeness read leaves no '
         'line unlisted. Per class (DISCHARGED/RE-PROVED/OBSTRUCTED over the uses): C¹ with an integrable second derivative %s; even C² of rapid '
         'decay without compact support %s; finite sums of autocorrelations %s. The wider class named: the first and the third together. Rapid '
         'decay stops at three places -- the strip, where the transform must be bounded off the real line; the prime sum, finite only for a '
         'bounded support; and the detection join’s support bound.' % (f['uses'], f['path'], f['w'][0], f['w'][1], f['w'][2]), '',
         '**The README and the cell** (`(R308)`(5), on the author’s words): SIDE-simplicity README.md :9 re-cut to the header’s wording, the runner '
         'once at the branch tip, its prints equal to b697’s, no quoting line left; merged at `%s`, tagged v0.1.2. The generator alone then wrote '
         'SIMPLICITY_OF_RIEMANN_ZEROS :441 on a one-table roster, its token v0.1.0 to v0.1.2. Its partner copy was left as it stands; read line '
         'by line its table differs in %s lines, not the 6 the generator’s stored field prints, entered beneath W-ORD-ONE-COPY (OPEN_TRAILS :%s).' % (
             f['merge'], f['onecopy'], oc[0]), '',
         '**The third face and the rules** (`(R308)`(2), (5), (6)): the arithmetic-limit plan carried as priced, its row appended beneath it. '
         'Row (1) has a kernel’s tag move regenerate the Correspondence cells naming it, from b699. Row (2) has the Read tool read a file whole '
         'under two hundred lines and by offset and limit otherwise, from b698.', '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed on two objects, each raised before the '
         'component that cites it; %d answer check%s, each before its answer was acted on. b697 at its weight (FINDINGS :%s).' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's', c1_[0]), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b694’s CLAUSE-DOMINANCE reading and b695’s eleventh specification row '
         'against the faces page’s Correspondence row; b676’s strip uses as the uses’ template; b697’s README residue and held cell. It is re-read '
         'by b699, where row (1) binds and the three SIDE-archimedean cells held since b693 come due; by b700’s reading, which takes the regularity '
         'bank; and by a later research act on a wider class. It strengthens the programme’s offering of a located clause: the one open premise '
         'shown to reach the second faces kernel by no statement identity, the object a bridge must build named, and a wider test class read '
         'from the uses by one-line sketches, not compiled.', '',
         '**Carried to:** W-ORD-H2-BRIDGE (the open object, binder 1); b699 (row (1), the three SIDE-archimedean cells); b700 (the regularity '
         'bank); W-ORD-ONE-COPY (the partner copy); `W-ORD-EPSTEIN-COUNT-LEAN`; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) on the answer to the first miss, no hosted run at SIDE-lv-conservation v0.13.0 can print the face, so its source was read '
              '(data/b698_correspondence_dominance.txt); (2) the three candidate classes read as each varying the hypothesis it names, the '
              'wider class named the first and the third together; (3) the leaves of the two explicit formulas counted apart from the uses; (4) the stale '
              'cell written on a one-table roster, so the page alone moved; (5) the partner copy`s 18 differing lines entered with the stored 6 '
              'named; (6) the act`s answer check widened to the act`s kernels')


def _trail_text():
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    br = _rl_lines('%s_bridge_line.json' % ACT) + ['-']
    oc = _rl_lines('%s_onecopy_line.json' % ACT) + ['-']
    f = _figs()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R308) ratified.** (1) b697 at its weight. (2) The third face carried as priced. (3) CORRESPONDENCE-DOMINANCE built and read. (4) '
             'The regularity-uses bank. (5) The README residue and the stale cell, with rule (1). (6) The read rule. (7) The branches. (8) The '
             'readfirst bank. (9) The draft held at v5. (10) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b697`s weight), :%s (the entry); OPEN_TRAILS :%s (beneath W-ORD-H2-BRIDGE), :%s (beneath W-ORD-ONE-COPY); '
             'this record.' % (c1_[0], fj.get('entry_line'), br[0], oc[0]), '',
             '**Act root:** b698 `%s` (previous `%s`, b697`s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s (relay data/b698_author_answers.txt); none after the root.' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The dominance:** %s by correspondence, source against print, %d of %d rows agreeing; CLAUSE-DOMINANCE 1 of 2 by closure (relay '
             'data/b698_correspondence_dominance.txt).' % (f['verdict'], f['agree'], f['rows']), '',
             '**The regularity uses:** %s uses and %s leaves; W1 %s, W2 %s, W3 %s over the uses (relay data/b698_regularity_uses.txt).' % (
                 f['uses'], f['path'], f['w'][0], f['w'][1], f['w'][2]), '',
             '**The residues:** SIDE-simplicity README :9 %s at %s; SIMPLICITY_OF_RIEMANN_ZEROS :441 %s by the generator alone; the partner copy`s '
             '%s differing lines read (relay data/b698_readme_cut.txt, data/b698_correspondence_page_diff.txt, data/b698_onecopy.txt).' % (
                 f['readme'], f['merge'], f['cell'], f['onecopy']), '',
             '**The kernels:** SIDE-simplicity alone written -- the README re-cut, its merge and tag v0.1.2, on the author`s word; the runner '
             'dispatched once, at the cut`s tip; no lean or lake on this host.', '',
             '**The rules:** relay data/b698_rules.txt (1) a kernel`s tag move regenerates its Correspondence cells, binding from b699; (2) the read '
             'rule, binding from b698.', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b698_closing.txt).', '',
             '**The open orders:** `W-ORD-B518-FLOAT` (the reading act b700); `W-ORD-H2-BRIDGE` (its open object named at :%s); `W-ORD-ONE-COPY`; '
             '`W-ORD-EPSTEIN-COUNT-LEAN` or a wider class (b701, on the author`s word).' % br[0], '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b698_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S, C = jl('%s_scores.json' % ACT), jl('%s_scores_close.json' % ACT)
    L = ['=' * 104, '%s -- THE DESK.' % ACT, '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s%s' % (
        k2, S[k2][0], S[k2][1], ('  ### AT THE CLOSE: %s -- %s' % (C[k2][0], C[k2][1])) if (S[k2][0] == 'PENDING' and C.get(k2)) else '')
        for k2 in SCORE_KEYS]
    L += [''] + rdn('%s_defects.txt' % ACT).rstrip(NL).split(NL)
    put_txt('%s_desk_notes.txt' % ACT, L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('%s_scores.json' % ACT, '%s_findings.json' % ACT, '%s_trail.json' % ACT, '%s_act_root.json' % ACT))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    L = ['%s -- THE COMPONENTS, BANKED UNDER (R308).' % ACT, '',
         '### COMPONENT 0 : the citation check (data/b698_citation_check.txt), step zero (data/b698_ferry.txt, data/b698_readfirst.txt, '
         'data/b698_stepzero.txt, data/b698_tests_stepzero.txt, data/b698_rowgen_stepzero.txt, data/b698_branches.txt, data/b698_rules.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b697`s weight FINDINGS :%s ; the plan`s row beneath data/b697_arith_plan.txt' % c1_[0],
         '### COMPONENT 2 : CORRESPONDENCE-DOMINANCE (tools/circuit_correspondence.py, data/b698_correspondence_dominance.txt), W-ORD-H2-BRIDGE '
         'annotated ; N2 %s ; N3 %s' % (S['N2'][0], S['N3'][0]),
         '### COMPONENT 3 : the regularity-uses bank (data/b698_regularity_uses.txt, data/b698_regularity_counts.txt) ; N4 %s' % S['N4'][0],
         '### COMPONENT 4 : the README ACTION and re-cut, the generator`s dry runs and the cell (data/b698_residue_actions.txt, data/b698_readme_cut.txt, '
         'data/b698_correspondence_page_diff.txt, data/b698_onecopy.txt)',
         '### COMPONENT 5 : the carry-time reading (data/b698_tool_repairs.txt), the dry-run steps (data/b698_reg_gate.txt), the seal '
         '(data/b698_seal_hashes.json), the suite in six parts, the per-part seconds (data/b698_arm_seconds.txt) ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('%s_components.txt' % ACT, L)
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
    if not os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, '%s_findings.json' % ACT, dict(title=t))
    j = jl('%s_findings.json' % ACT)
    j['entry_line'] = ln
    put_json('%s_findings.json' % ACT, j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, '%s_trail.json' % ACT, {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


FACE_REL = 'data/b698_registration_2026-10-21.txt'


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them, converted by conv and run
    through the screens their landing runs, the needles the face names read in each; DRY-RUN STEP : CLEAN only when both screens are quiet and
    every needle is found. Writes no bank."""
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
            with open(p + '.tmp', 'wb') as fh:
                fh.write(b_)
            os.replace(p + '.tmp', p)
        return r.returncode, b_.decode('utf-8', 'replace')
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], '%s_reg_termscan.txt' % ACT)
    rc2, t2 = runb([os.path.join(T, '%s_regspec.py' % ACT)], '%s_regspec_run.txt' % ACT)
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/%s_satisfiable.json' % ACT, '--emit', ACT], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_%s_reg_satisfiable.txt' % ACT).split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', '%s_census_stepzero.txt' % ACT), ('b327_faces_census.py', '%s_faces_census_stepzero.txt' % ACT),
                      ('b303_pins.py', '%s_pins_stepzero.txt' % ACT)):
        rc, t = runb([os.path.join(T, tool), ACT], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/%s_reg_gate.txt' % ACT, 'data/%s_reg_termscan.txt' % ACT, 'data/%s_regspec_run.txt' % ACT, 'data/audit_%s_reg_satisfiable.txt' % ACT):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b697's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
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
    put_json('%s_mirror_build.json' % ACT, dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != ACT:
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT %s`s -- NOTHING WRITTEN' % (last[0], ACT))
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
    with open(man_p, 'wb') as fh:
        fh.write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    ps = subprocess.run(['powershell', '-NoProfile', '-Command', "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)],
                        capture_output=True, text=True)
    after = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    put_json('%s_mirror_root.json' % ACT, dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_txt('%s_mirror_verify.txt' % ACT, (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('%s_mirror_verify.txt' % ACT)
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['%s -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % (ACT, utc()),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b698 (the last export b697`s, D:/MY-DOwnloads/mirror-refresh-2026-10-21-b697.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


# ================================================================================ THE CARRY-TIME READING (the ferry's Component 5)
def _fn_src(src, name):
    if ('\ndef %s(' % name) not in src:
        return ''
    i = src.index('\ndef %s(' % name) + 1
    m = re.search(r'\n(?=\S)', src[i + 1:])
    return src[i:i + 1 + m.start() + 1] if m else src[i:]


REPAIR_ROWS = []      # ### filled at Component 5, after the carry: (text, carried tool, carried function, this act's tool)


def repairs(*a):
    """data/b698_tool_repairs.txt: the carry-time repairs, each with the defect or order it answers, its diff written by this route (difflib
    opcodes over the carried function's source at relay HEAD against this act's). No shared tool is edited by this act."""
    import difflib
    L = ['%s -- THE CARRY-TIME READING: THE REPAIRS (%s)' % (ACT, utc()), '',
         '### rows are repairs with the defect or order they answer: the tool and its part ; what it answers ; the form. Each diff beneath its',
         '### row, written by this route (difflib over the function`s source, relay HEAD`s carried tool against this act`s).', '']
    n = 0
    for text, src_tool, fn, new_tool in REPAIR_ROWS:
        old = _fn_src(_show(ROOT, 'HEAD', 'tools/' + src_tool) or '', fn).split(NL)
        new = _fn_src(rd(os.path.join(T, new_tool)), fn).split(NL)
        d = list(difflib.unified_diff(old, new, 'tools/%s %s (sealed)' % (src_tool, fn), 'tools/%s %s (this act)' % (new_tool, fn), lineterm=''))
        n += len(d)
        L += ['  ' + text, ''] + ['      ' + x for x in d] + ['']
    L += ['### ### **REPAIRS %d ; NO SHARED TOOL EDITED ; DIFF LINES %d ; NO FROZEN BANK EDITED.**' % (len(REPAIR_ROWS), n)]
    if 'dry' not in a:
        put_txt('%s_tool_repairs.txt' % ACT, L)
    print(L[-1])


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, c1=c1, bridge=bridge, uses=uses, cells=cells,
              dispatch=dispatch, runstatus=runstatus, runner=runner, prints=prints, quote=quote, readmecut=readmecut, onecopy=onecopy,
              heldcells=heldcells, commands=commands, reads=reads, kernels=kernels, rootbanks=rootbanks, root=root, root_arm=root_arm,
              table_final=table_final, standing=standing, armsecs=armsecs, scores=scores, desk=desk, components=components, findings=findings,
              trail=trail, drycheck=drycheck, gatebanks=gatebanks, mbuild=mbuild, mroot=mroot, mverify=mverify, mbank=mbank, repairs=repairs)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b698_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
