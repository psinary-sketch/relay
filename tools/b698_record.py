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


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, c1=c1, bridge=bridge, uses=uses, cells=cells,
              dispatch=dispatch, runstatus=runstatus, runner=runner, prints=prints, quote=quote, readmecut=readmecut)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b698_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
